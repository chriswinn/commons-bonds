# Prose-clarity contract

**Status:** active 2026-06-11. Enforced by `tools/scripts/check-prose-clarity.py`
(detector + regression gate) and the pre-commit hook. Scannable companion to the
em-dash-overuse and audience-aware-drafting disciplines.

## Why this exists

The Technical Appendix accumulated hard-to-read prose — em-dash splicing,
noun-pile jargon, clause-stacked sentences — that survived several "smooth it"
refactors. Those failed for four reasons: no **testable target**, no
**regression gate**, agent-redrafting that **reintroduces the same LLM tics**,
and a file too big to edit holistically. This contract is the testable target;
the detector + gate are the regression-proofing. Fixes therefore *stick*.

## The rules (testable)

| Rule | Prefer | MEDIUM (worklist) | HIGH (gating) |
|---|---|---|---|
| **Em-dashes per paragraph** | ≤1; each justified, not default punctuation | 3–4 | **≥5** |
| **Sentence length (words)** | <35 | 46–60 | **>60** |
| **Noun-pile compounds** (3+ hyphenated-word chains, e.g. `legacy-effects pricing pathway`) | none — define jargon in plain words | ≥3 in a paragraph | — (advisory) |

Plus two non-mechanical principles (reviewer-checked, not gated):
- **Plain-language register.** Prefer verbs over nominalizations — "X is disrupted," not "the disruption of X."
- **Define jargon once.** Introduce a technical compound once with a plain gloss; don't stack new compounds in the same passage.

Em-dashes are not banned — they do real work occasionally — but **≥3 in one
paragraph is a reliable splicing signal, and ≥5 is always clutter** (the worst
TA paragraph carried 11). Default to commas, colons, periods, or restructuring.

## The detector

```
tools/scripts/check-prose-clarity.py <file|dir> ...     # ranked worklist + per-file HIGH/MEDIUM/LOW
tools/scripts/check-prose-clarity.py --summary <files>  # counts only
tools/scripts/check-prose-clarity.py --top 20 <file>    # worst 20 paragraphs
```
It parses paragraphs (HTML `<p>` / Markdown blocks), is stdlib-only, and is a
REVIEW AID — it locates clunk, it does not rewrite. Rewriting is the section-pass
job (surgical, substance-preserving, author-ratified — never wholesale redraft).

## The regression gate

The pre-commit hook runs `check-prose-clarity.py --check-staged`, which is:
- **regression-only** — it blocks a commit only when a *baselined* file's HIGH
  count rises above `tools/quality-gates/prose-clarity-baseline.json`. Pre-existing
  clunk does not block (it is worked down by the section passes, then re-baselined
  downward).
- **scoped** — currently the Technical Appendix only (technical prose, where
  clunk is unambiguous). The detector runs on any prose; the *gate* enforces the
  baselined files. Extend by adding files to the baseline.
- **fail-safe** — any error, a missing baseline, or an unbaselined file → exit 0.
  It never blocks a commit except on a genuine HIGH regression in a baselined file.

Baseline as of 2026-06-11: **TA = 28 HIGH paragraphs** (28 → 0 is the section-pass
target). Whenever a section pass lowers the count, re-run `--emit-baseline` so the
floor ratchets down and cannot creep back up.

## Workflow

1. **Now (regression-proofed):** new/worsened HIGH clunk in the TA is refused at commit.
2. **Section passes (deferred, token-heavy):** `check-prose-clarity.py` ranks the
   worst paragraphs; an agent proposes a de-clunked version of each (not a redraft);
   a verifier confirms substance preserved + flag-count down + no new tics; author
   ratifies in batches; re-baseline downward. Repeat until HIGH = 0, then MEDIUM.
