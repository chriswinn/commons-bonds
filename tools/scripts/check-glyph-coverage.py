#!/usr/bin/env python3
"""check-glyph-coverage.py — render-font glyph-coverage gate.

Extracts every non-ASCII codepoint actually used in the given HTML/MD files and
checks whether the render toolchain can draw each one. A glyph the toolchain
cannot draw renders as a tofu box (.notdef) in the PDF — a silent, reviewer-
visible defect. The source-encoding check (no U+FFFD) does NOT catch this; only
font coverage does.

Two coverage backends:
  --container   (default) authoritative: probe the built render image's fonts via
                fontconfig (`fc-list :charset=<cp>`). Matches what wkhtmltopdf/Qt
                actually has available. Requires the image to be built + docker up.
  --font <ttf>  offline: parse one TrueType font's cmap (stdlib; no deps). Fast,
                but only checks that one font — not the whole fallback chain.

Exit code 0 = every used codepoint is covered; 1 = at least one gap (tofu risk).
Intended as a Stage-4 pre-render gate.

Usage:
  python3 tools/scripts/check-glyph-coverage.py            # TA + back-matter, container backend
  python3 tools/scripts/check-glyph-coverage.py FILE...    # specific files
  python3 tools/scripts/check-glyph-coverage.py --font ~/Library/Fonts/DejaVuSerif.ttf
  python3 tools/scripts/check-glyph-coverage.py --image commons-bonds-render
"""
import sys, os, re, glob, html as H, struct, subprocess, unicodedata

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
DEFAULT_FILES = [os.path.join(ROOT, "manuscript/technical-appendix/TechnicalAppendix_v2.0.0.html")] + \
                sorted(glob.glob(os.path.join(ROOT, "manuscript/back-matter/*.html")))
IMAGE = "commons-bonds-render"


def used_codepoints(files):
    cnt = {}
    for f in files:
        t = open(f, encoding="utf-8").read()
        t = H.unescape(re.sub(r"<[^>]+>", " ", t))   # rendered text, entities resolved
        for ch in t:
            if ord(ch) > 0x7F and not ch.isspace():
                cnt[ch] = cnt.get(ch, 0) + 1
    return cnt


def font_cmap_covered(ttf):
    """Return the set of codepoints the font's cmap can draw (formats 4 + 12)."""
    d = open(ttf, "rb").read()
    n = struct.unpack(">H", d[4:6])[0]; off = 12; cmap = None
    for _ in range(n):
        if d[off:off+4] == b"cmap":
            cmap = struct.unpack(">I", d[off+8:off+12])[0]
        off += 16
    nsub = struct.unpack(">H", d[cmap+2:cmap+4])[0]; subs = []; p = cmap+4
    for _ in range(nsub):
        _pid, _eid, so = struct.unpack(">HHI", d[p:p+8]); subs.append(cmap+so); p += 8
    cov = set()
    for so in subs:
        fmt = struct.unpack(">H", d[so:so+2])[0]
        if fmt == 4:
            x2 = struct.unpack(">H", d[so+6:so+8])[0]; seg = x2//2; b = so+14
            end = struct.unpack(">%dH" % seg, d[b:b+x2]); b += x2+2
            start = struct.unpack(">%dH" % seg, d[b:b+x2]); b += x2
            idd = struct.unpack(">%dH" % seg, d[b:b+x2]); b += x2
            ip = b; idro = struct.unpack(">%dH" % seg, d[b:b+x2])
            for s in range(seg):
                for c in range(start[s], end[s]+1):
                    if c == 0xFFFF:
                        continue
                    if idro[s] == 0:
                        g = (c+idd[s]) & 0xFFFF
                    else:
                        gi = ip+s*2+idro[s]+(c-start[s])*2
                        g = struct.unpack(">H", d[gi:gi+2])[0] if gi+2 <= len(d) else 0
                    if g:
                        cov.add(c)
        elif fmt == 12:
            ng = struct.unpack(">I", d[so+12:so+16])[0]; gp = so+16
            for _ in range(ng):
                sc, ec, _sg = struct.unpack(">III", d[gp:gp+12]); gp += 12
                cov.update(range(sc, ec+1))
    return cov


def container_covered(cps, image):
    """One docker run; inside, fc-list :charset per codepoint. Returns covered set."""
    hexes = " ".join("%x" % ord(c) for c in cps)
    script = ('for cp in %s; do '
              'if fc-list ":charset=$cp" family | grep -q .; then echo "$cp"; fi; done' % hexes)
    out = subprocess.run(
        ["docker", "run", "--rm", "--platform=linux/amd64", "--entrypoint", "bash",
         image, "-c", script],
        capture_output=True, text=True, timeout=600)
    if out.returncode != 0 and not out.stdout:
        sys.exit(f"docker probe failed (is the image '{image}' built + docker up?):\n{out.stderr[:400]}")
    return {int(line, 16) for line in out.stdout.split() if line.strip()}


def main():
    args = sys.argv[1:]
    backend, ttf, image, files = "container", None, IMAGE, []
    i = 0
    while i < len(args):
        a = args[i]
        if a == "--font":
            backend, ttf = "font", args[i+1]; i += 2
        elif a == "--image":
            image = args[i+1]; i += 2
        elif a == "--container":
            backend = "container"; i += 1
        else:
            files.append(a); i += 1
    files = files or DEFAULT_FILES
    cnt = used_codepoints(files)
    if backend == "font":
        cov = font_cmap_covered(ttf)
        covered = {c for c in cnt if ord(c) in cov}
        src = os.path.basename(ttf)
    else:
        cset = container_covered(list(cnt), image)
        covered = {c for c in cnt if ord(c) in cset}
        src = f"container image '{image}' (all installed fonts)"
    missing = sorted(((c, n) for c, n in cnt.items() if c not in covered), key=lambda x: -x[1])
    print(f"Glyph-coverage check vs {src}")
    print(f"  files: {len(files)} | distinct non-ASCII glyphs used: {len(cnt)} | covered: {len(covered)}")
    if not missing:
        print("  ✅ all used glyphs are covered — no tofu risk.")
        return 0
    print(f"  ❌ {len(missing)} glyph(s) NOT covered → would render as tofu "
          f"({sum(n for _, n in missing)} occurrences):")
    for ch, n in missing:
        try:
            nm = unicodedata.name(ch)
        except ValueError:
            nm = "?"
        print(f"     {ch!r}  U+{ord(ch):04X}  x{n:<4} {nm}")
    return 1


if __name__ == "__main__":
    sys.exit(main())
