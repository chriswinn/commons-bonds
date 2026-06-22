#!/usr/bin/env python3
"""
check-prose-clarity.py — deterministic prose-clarity detector for publisher-facing prose.

Flags the measurable tics that survive subjective "smooth it" passes:
  - em-dash density per paragraph   (overuse / clause-splicing)
  - over-long sentences             (clause-stacking)
  - noun-pile compounds             (3+ hyphenated-word chains; advisory)

Enforces the testable rules in tools/conventions/prose-clarity-contract.md.
NOT a redrafter — it produces a ranked worklist and a regression gate.

Severity (HIGH is the only gating tier; conservative by design -> ~0 false positives):
  HIGH    em-dashes >= 5 in a paragraph, OR any sentence > 60 words
  MEDIUM  em-dashes 3-4, OR a sentence 46-60 words, OR >= 3 noun-piles
  LOW     em-dashes == 2, OR >= 1 noun-pile

Usage:
  check-prose-clarity.py <file|dir> ...            ranked worklist + summary
  check-prose-clarity.py --summary <files...>      per-file counts only
  check-prose-clarity.py --top N <files...>        worst N paragraphs
  check-prose-clarity.py --emit-baseline <files>   write per-file HIGH counts to --baseline
  check-prose-clarity.py --check-staged            gate: fail (exit 1) if a staged, baselined
                                                   file's HIGH count rose above baseline
  --baseline PATH   baseline json (default tools/quality-gates/prose-clarity-baseline.json)

The gate is REGRESSION-ONLY (pre-existing clunk does not block) and FAIL-SAFE
(any error, missing baseline, or unbaselined file -> exit 0, never blocks a commit).
"""
import argparse, html, json, os, re, subprocess, sys

EMDASH = "—"  # — (U+2014); en-dash/hyphen are fine and not counted
SENT_HIGH = 60     # words
SENT_MED = 46
# legit multi-hyphen terms that are NOT noun-pile clutter
NOUNPILE_ALLOW = {
    "scope-of-applicability", "cost-to-cure", "social-cost-of-carbon",
    "willingness-to-pay", "value-of-a-statistical-life", "matter-of-fact",
    "show-then-flinch", "lower-bound", "real-cost-of-value", "three-states",
}
NOUNPILE_RE = re.compile(r"\b[A-Za-z]+(?:-[A-Za-z]+){2,}\b")
SENT_SPLIT = re.compile(r"(?<=[.!?])\s+(?=[A-Z(“\"])|\s+[-–]\s+")  # sentence-enders + inline dash-bullets


def paragraphs_from_html(text):
    out = []
    for m in re.finditer(r"<p\b[^>]*>(.*?)</p>", text, re.S | re.I):
        raw = m.group(1)
        plain = html.unescape(re.sub(r"<[^>]+>", "", raw))
        plain = re.sub(r"\s+", " ", plain).strip()
        if plain:
            line = text.count("\n", 0, m.start()) + 1
            out.append((line, plain))
    return out


def paragraphs_from_md(text):
    out, buf, start_line, in_fence = [], [], 0, False
    for i, ln in enumerate(text.split("\n"), 1):
        if ln.strip().startswith("```"):
            in_fence = not in_fence
            continue
        if in_fence:
            continue
        s = ln.strip()
        is_block = (not s) or s.startswith(("#", ">", "|", "-", "*", "    ", "<"))
        if is_block:
            if buf:
                out.append((start_line, " ".join(buf))); buf = []
        else:
            if not buf:
                start_line = i
            buf.append(s)
    if buf:
        out.append((start_line, " ".join(buf)))
    return [(l, p) for (l, p) in out if len(p) > 40]


def analyze_paragraph(text):
    em = text.count(EMDASH)
    sents = SENT_SPLIT.split(text)
    max_sent = max((len(s.split()) for s in sents), default=0)
    npiles = [t for t in NOUNPILE_RE.findall(text) if t.lower() not in NOUNPILE_ALLOW]
    if em >= 5 or max_sent > SENT_HIGH:
        sev = "HIGH"
    elif em >= 3 or max_sent > SENT_MED or len(npiles) >= 3:
        sev = "MEDIUM"
    elif em == 2 or npiles:
        sev = "LOW"
    else:
        sev = "CLEAN"
    return {"em": em, "max_sent": max_sent, "npiles": npiles, "sev": sev}


def analyze_file(path):
    text = open(path, encoding="utf-8").read()
    paras = paragraphs_from_html(text) if path.endswith((".html", ".htm")) else paragraphs_from_md(text)
    rows = []
    for line, p in paras:
        a = analyze_paragraph(p)
        if a["sev"] != "CLEAN":
            a.update(line=line, snippet=p[:90])
            rows.append(a)
    return rows


def high_count(rows):
    return sum(1 for r in rows if r["sev"] == "HIGH")


def iter_files(args_paths):
    for p in args_paths:
        if os.path.isdir(p):
            for root, _d, files in os.walk(p):
                for f in files:
                    if f.endswith((".html", ".md")):
                        yield os.path.join(root, f)
        else:
            yield p


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("paths", nargs="*")
    ap.add_argument("--summary", action="store_true")
    ap.add_argument("--top", type=int, default=0)
    ap.add_argument("--severity", choices=["HIGH", "MEDIUM", "LOW"], default="LOW")
    ap.add_argument("--emit-baseline", action="store_true")
    ap.add_argument("--check-staged", action="store_true")
    ap.add_argument("--baseline", default="tools/quality-gates/prose-clarity-baseline.json")
    args = ap.parse_args()
    order = {"HIGH": 3, "MEDIUM": 2, "LOW": 1}
    minsev = order[args.severity]

    if args.check_staged:
        # FAIL-SAFE regression gate: never raise, never block on pre-existing clunk.
        try:
            root = subprocess.check_output(["git", "rev-parse", "--show-toplevel"]).decode().strip()
            base = json.load(open(os.path.join(root, args.baseline)))
            staged = subprocess.check_output(
                ["git", "diff", "--cached", "--name-only", "--diff-filter=ACM"]).decode().split()
            regressed = []
            for rel in staged:
                if rel not in base:
                    continue  # only enforce on baselined files
                fp = os.path.join(root, rel)
                if not os.path.exists(fp):
                    continue
                cur = high_count(analyze_file(fp))
                if cur > base[rel]:
                    regressed.append((rel, base[rel], cur))
            if regressed:
                print("[prose-clarity] BLOCKED — new HIGH-severity clunk (em-dashes>=5 or a sentence>60 words):")
                for rel, b, c in regressed:
                    print(f"  {rel}: HIGH {b} -> {c}")
                    for r in analyze_file(os.path.join(root, rel)):
                        if r["sev"] == "HIGH":
                            print(f"     L{r['line']}  em={r['em']} maxSent={r['max_sent']}  {r['snippet']}...")
                print("  Fix the flagged paragraph(s) or, if genuinely justified, update the baseline.")
                return 1
            return 0
        except Exception as e:
            sys.stderr.write(f"[prose-clarity] skipped (fail-safe): {e}\n")
            return 0

    files = list(iter_files(args.paths))
    if args.emit_baseline:
        base = {}
        root = subprocess.check_output(["git", "rev-parse", "--show-toplevel"]).decode().strip()
        for fp in files:
            rel = os.path.relpath(os.path.abspath(fp), root)
            base[rel] = high_count(analyze_file(fp))
        json.dump(dict(sorted(base.items())), open(args.baseline, "w"), indent=2)
        open(args.baseline, "a").write("\n")
        print(f"wrote baseline {args.baseline}: {len(base)} files, "
              f"{sum(base.values())} HIGH paragraphs total")
        return 0

    grand = []
    for fp in files:
        rows = [r for r in analyze_file(fp) if order[r["sev"]] >= minsev]
        if not rows:
            continue
        tot = {s: sum(1 for r in rows if r["sev"] == s) for s in ("HIGH", "MEDIUM", "LOW")}
        print(f"\n{fp}  HIGH={tot['HIGH']} MEDIUM={tot['MEDIUM']} LOW={tot['LOW']}")
        if not args.summary:
            rows.sort(key=lambda r: (-order[r["sev"]], -r["em"], -r["max_sent"]))
            for r in (rows[:args.top] if args.top else rows):
                print(f"  [{r['sev']:6}] L{r['line']:<5} em={r['em']} maxSent={r['max_sent']} "
                      f"npile={len(r['npiles'])}  {r['snippet']}...")
        grand.extend(rows)
    g = {s: sum(1 for r in grand if r["sev"] == s) for s in ("HIGH", "MEDIUM", "LOW")}
    print(f"\nTOTAL  HIGH={g['HIGH']} MEDIUM={g['MEDIUM']} LOW={g['LOW']}  across {len(files)} file(s)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
