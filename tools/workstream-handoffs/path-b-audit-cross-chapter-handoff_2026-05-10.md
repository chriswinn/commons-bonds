# Path B Audit — Cross-Chapter — Workstream Handoff (2026-05-10)

**Date drafted:** 2026-05-10
**Branch to create at session start:** `claude/path-b-audit-cross-chapter-<harness-id>` (branch from current `origin/main`)
**Status going in:** Path B issue surfaced 2026-05-10 in the Noema essay audit (~14 verbatim sentences, 9 high-echo paragraphs cloned from Ch 1). Same dynamic could exist between chapter pairs across the manuscript. No prior cross-chapter Path B audit has been run. Pre-trigger condition for the workstream: any future essay extraction from the chapters (Boston Review essay from Ch 5; future Aeon Dunbar aside material from Ch 8; Berggruen essay from anywhere) will inherit whatever cross-chapter echoes already exist. **Catch them now, fix once, every downstream essay benefits.**

---

## Workstream scope

Run a project-wide Path B audit across all 10 drafted chapters of *Commons Bonds* + the Tech Appendix + the AuthorsNote. Identify:

1. **Sentence-level reuse** — verbatim sentences appearing in two or more chapters.
2. **High-echo paragraph pairs** — paragraphs in chapter X that close-paraphrase paragraphs in chapter Y.
3. **Framework definition drift / duplication** — same framework concept defined slightly differently in multiple chapters; same case described with overlapping phrasing.
4. **Cross-chapter rhetorical echoes** — distinctive phrases that repeat across chapters and don't earn their repetition.

For each finding, propose a fix: which chapter keeps the canonical version; which chapter rewrites; whether to consolidate into a single load-bearing instance.

---

## Why this matters

The Noema essay was discovered to be structurally Ch 1 with light variations because the drafting process close-paraphrased Ch 1 rather than generating fresh prose. The same close-paraphrasing dynamic is plausible between chapters — Ch 3 (*The Waterman*) may echo Ch 2 (*The Miner*)'s extraction-cost case-walks; Ch 6 (*Three Ways of Counting*) may echo Ch 5 (*The Accountability Gap*)'s framework definitions; Ch 9 (*Pricing Honestly*) may echo Ch 6's apparatus.

Echoes between chapters of the *same book* are not a copyright issue (the author owns all chapters), but they are:

- **A reading experience problem.** A reader who just read Ch 5's framework definition does not need to read it again in Ch 6.
- **An essay-extraction landmine.** Every essay derived from a chapter inherits whatever sentences that chapter shares with other chapters. If Ch 5 and Ch 9 share text, an essay derived from Ch 9 may unwittingly re-echo Ch 5's text (which is what Path B is supposed to prevent).
- **A signal of where compression/consolidation can save chapter weight.** Heavy duplication between chapters often means one chapter is doing work the other should do, OR both are.

---

## Methodology

Use the validated two-stage discipline framework if Stage 3 of the Noema/Aeon experiment validates it (per `feedback_audience_aware_drafting_discipline.md`). If validated, the cross-chapter Path B audit becomes a "Stage 3 retrospective rigor pass" applied to chapter pairs.

Concrete steps per chapter pair (10 chapters → 45 unique pairs; not all need full audit):

1. **Pair selection.** Prioritize chapter pairs that share thematic territory (Ch 5 + Ch 6; Ch 5 + Ch 9; Ch 2 + Ch 3 + Ch 8; Ch 1 + Ch 10). Skip pairs with low overlap.
2. **Lexical overlap scan.** Use grep / word-frequency to identify candidate echo passages. Tools: `git grep` for distinctive phrases; manual diff of comparable sections.
3. **Sentence-level audit.** For each candidate echo passage, compare paragraphs side by side. Flag verbatim sentences and high-echo paragraphs.
4. **Decision per finding:** which chapter keeps the canonical version; which rewrites; whether to consolidate into a load-bearing single instance with a cross-reference.
5. **Apply fixes.** Edit the chapters with sentence-level rewrites that preserve substance but vary prose.
6. **Verify.** Re-run lexical scan to confirm fixes landed.

**Per-pair budget:** ~30–60 minutes of focused work. **Total estimated effort:** ~10–15 high-priority pairs × ~45 min = 7–12 hours of session time over multiple sessions.

---

## Current state

**Known starting point:**
- Ch 1 has been audited against the Noema essay → ~14 verbatim sentences identified in the essay. Ch 1 itself has not been audited against other chapters.
- All 10 chapters drafted and audited individually. Cross-chapter audit has not been run.
- Tech Appendix exists with apparatus that may be referenced informally in chapters. Worth checking for duplicate definitions of *RCV*, *cluster-γ*, *accountability bond*, *cost severance*, etc.

**Coordination with apparatus register decision sweep:** This handoff and the apparatus register sweep handoff (`apparatus-register-sweep-handoff_2026-05-10.md`) should run together where they overlap — apparatus duplication and Path B duplication often live in the same paragraphs.

---

## Deliverables

1. **`research/audits/cross-chapter-path-b-audit_2026-05-10.md`** — audit findings: pair-by-pair flagged passages with severity, recommended fix, status.
2. **Edits applied to chapter files** in `manuscript/chapters/`. Each fix is a separate commit with clear message naming the pair and the verbatim/high-echo passage being resolved.
3. **Updated `tools/rigor-passes/`** entry if the audit reveals patterns worth codifying for future drafting.

---

## First actions for fresh session

1. Read this handoff end-to-end.
2. Read `tools/workstream-handoffs/README.md` for branch discipline.
3. Read the `feedback_audience_aware_drafting_discipline.md` memory entry. If Stage 3 of the methodology experiment has been completed, read its verdict — that may inform whether to use the two-stage discipline retrospectively or use a different audit approach.
4. Read the Noema essay Path B audit findings (in the conversation log on 2026-05-10 if available, or the Noema rigor-pass file `tools/rigor-passes/commons_bonds_rigor_pass_2026-05-09_noema_essay_audience_load_v1.0.0.md` for context on what Ch 1 echoes look like).
5. Confirm with user the priority pair list (which chapter pairs to audit first).
6. Begin with Ch 5 + Ch 6 pair (framework apparatus likely overlap), then Ch 5 + Ch 9 (pricing apparatus likely overlap), then Ch 2 + Ch 3 + Ch 8 (extraction-case-walks likely overlap).

---

## What NOT to do

- Do not edit chapter files without confirming each substantive fix with the user. Cross-chapter consolidation decisions are content decisions.
- Do not attempt to audit all 45 pairs — diminishing returns past the high-priority set.
- Do not conflate this with the apparatus register decision sweep — they are related but distinct (Path B is about sentence-level reuse; apparatus register is about whether a concept stays in trade body, migrates to tech appendix, or gets dropped).
- Do not introduce new content during the audit — this is rewrite-not-rewrite-bigger work. New content goes through normal drafting process.

---

## Reference files

- `manuscript/chapters/Chapter__1_TheQuietMath__Draft.md` through `Chapter_10_CommonBonds__Draft.md`
- `manuscript/chapters/_AUTHORSNOTE_ON_WINDTUNNELS_AND_AI.md`
- Tech Appendix (location varies; check `manuscript/` and `tools/` directories)
- `feedback_audience_aware_drafting_discipline.md` (memory)
- `tools/rigor-passes/commons_bonds_rigor_pass_2026-05-09_noema_essay_audience_load_v1.0.0.md` (the audit framework + Noema-essay findings)
- `publishing/essays/noema-commons-bonds/_archive/pre-pass1-drafts/noema-essay-pre-pass1_2026-05-09.md` and `noema-essay-post-pass1_2026-05-09.md` (Path B's worst-case effects on essay quality, useful as reference for severity calibration)

---

*End of handoff.*
