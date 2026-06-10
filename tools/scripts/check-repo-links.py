#!/usr/bin/env python3
"""check-repo-links.py — repo-wide path-reference integrity checker.

Scans git-tracked .md files for references to other repo files and reports the
ones that don't resolve. Two reference forms are checked:

  1. Markdown links:  [text](relative/or/repo/path.md)   (http/mailto/#anchor skipped)
  2. Backtick paths:  `tools/foo/bar.md`                  (the dominant form in this repo)

A reference resolves if the target exists relative to the referencing file's
directory OR relative to the repo root (both conventions are in active use).

Usage:
  python3 tools/scripts/check-repo-links.py                 # full report to stdout
  python3 tools/scripts/check-repo-links.py --summary       # counts only
  python3 tools/scripts/check-repo-links.py --baseline out  # write sorted ref list to <out>

Intended workflow for file moves: write a baseline, do the moves (fixing inbound
references), re-run, and diff — the gate is ZERO NEW broken references (the repo
has pre-existing breaks in historical/audit-trail files which are left as-is).

Stdlib only.
"""
import os, re, subprocess, sys

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))

MD_LINK = re.compile(r"\[[^\]]*\]\(([^)\s]+)\)")
TICK_PATH = re.compile(r"`([A-Za-z0-9_][A-Za-z0-9_./ -]*?\.(?:md|html|sh|py|yaml|yml|json|tex|docx|pdf|css|png|csv))`")
EXT_SKIP_SCHEMES = ("http://", "https://", "mailto:", "#", "tel:")


def tracked_md():
    out = subprocess.run(["git", "ls-files", "*.md"], cwd=ROOT,
                         capture_output=True, text=True, check=True)
    return [l for l in out.stdout.splitlines() if l.strip()]


def candidates(text):
    refs = []
    for m in MD_LINK.finditer(text):
        t = m.group(1).split("#")[0].strip()
        if t and not t.startswith(EXT_SKIP_SCHEMES) and "/" in t or (t and t.endswith(".md")):
            if t and not any(t.startswith(s) for s in EXT_SKIP_SCHEMES):
                refs.append(t)
    for m in TICK_PATH.finditer(text):
        t = m.group(1).strip()
        # require a directory separator so bare filenames (`essay.md` as a generic
        # pattern, `README.md` as a concept) don't false-positive
        if "/" in t and not t.startswith(EXT_SKIP_SCHEMES):
            refs.append(t)
    return refs


def resolves(ref, src_dir):
    ref = ref.split("#")[0].strip().rstrip("/")
    if not ref or "<" in ref or ">" in ref or "*" in ref or "${" in ref or "$(" in ref:
        return True   # templated/placeholder path — not checkable, don't flag
    for base in (src_dir, ROOT):
        if os.path.exists(os.path.normpath(os.path.join(base, ref))):
            return True
    return False


def main():
    mode = sys.argv[1] if len(sys.argv) > 1 else ""
    broken = []   # (src, ref)
    for rel in tracked_md():
        path = os.path.join(ROOT, rel)
        try:
            text = open(path, encoding="utf-8").read()
        except (OSError, UnicodeDecodeError):
            continue
        src_dir = os.path.dirname(path)
        for ref in candidates(text):
            if not resolves(ref, src_dir):
                broken.append((rel, ref))
    broken.sort()
    if mode == "--baseline" and len(sys.argv) > 2:
        with open(sys.argv[2], "w", encoding="utf-8") as f:
            for src, ref in broken:
                f.write(f"{src}\t{ref}\n")
        print(f"baseline written: {len(broken)} broken refs across "
              f"{len(set(s for s, _ in broken))} files -> {sys.argv[2]}")
        return 0
    if mode == "--summary":
        print(f"{len(broken)} broken refs across {len(set(s for s, _ in broken))} files")
        return 0
    for src, ref in broken:
        print(f"{src}\t{ref}")
    print(f"\nTOTAL: {len(broken)} broken refs across {len(set(s for s, _ in broken))} files",
          file=sys.stderr)
    return 0


if __name__ == "__main__":
    sys.exit(main())
