# Post-audit structural TODOs (2026-06-06)

**Status: DEFERRED.** Do NOT action items 1–2 until the chapter redrafts + TA rigor audit
complete (author direction 2026-06-06: "get through all of these redrafts and TA audits
before that comes up"). Recorded here so they are not lost.

---

## 1. Relocate internal scaffolding out of end-user / editor-prose space (DEFERRED)

**Problem.** `manuscript/` currently mixes *shipped* content (`chapters/`, and the symlinked
`technical-appendix/`) with a large pile of *internal scaffolding* — `_CANONICAL_FIGURE_LEDGER.md`,
`_CANDIDATE-BEATS-AND-DEVICES.md`, `_REDRAFT-CAMPAIGN-RESUME`, `_BOOK-REDRAFT-ACTION-LIST`, and the
deep-pass `_*.json` / `_*.md` analysis artifacts. End-user/editor-facing space should hold only
reader-facing content.

**Action (later).** Move the `manuscript/_*` scaffolding to a proper internal home (e.g.
`manuscript/_scaffolding/`, `research/manuscript-analysis/`, or `tools/`), leaving `manuscript/`
holding only `chapters/` + `technical-appendix/` (+ the generated references at assembly).
**Cascade:** many files cross-reference `manuscript/ledgers/_CANONICAL_FIGURE_LEDGER.md`,
`manuscript/ledgers/_CANDIDATE-BEATS-AND-DEVICES.md`, etc. — update all references when moving.

**Trigger.** Part of the folder-structure revision, after redrafts + TA audit.

---

## 2. Generate reader-facing References / Works-Cited (PLAN — needed BEFORE publication)

**Why now (planning).** Editors will need a clean references version *well before* publication, as
part of the editor-delivery / proposal package — not just at final assembly.

**The two-artifact distinction.** The master `tools/back-matter/sources/bibliography.md` is an *annotated
internal tool* (per-entry summary / relevance / support-contradict / chapter-relevance / status /
character-reader mappings). The shipped book + editor package need a **clean, reader-facing
References / Works-Cited** *derived from* it — citations only, no annotations.

**Action.** At editor-delivery prep, generate the clean References from the master: strip every
annotation field; keep author / title / venue / year / DOI-or-URL; organize per publisher norm
(alphabetical, or sectioned). Feeds: all scholarly sections (§§1–22) + §23 primary-data sources.

**Output location.** With the manuscript at assembly (`manuscript/references.md`) and/or the editor
package (`publishing/book-proposal/`). **The master STAYS in `research/literature/` — do not move it.**

**Trigger.** Editor-delivery package prep (earlier than publication).

---

## 3. TA symlink (DONE 2026-06-06)

`manuscript/technical-appendix/TechnicalAppendix_v2.0.0.html` is a **relative symlink** →
`manuscript/technical-appendix/TechnicalAppendix_v2.0.0.html`. Co-locates the TA under `manuscript/` for
assembly/editor discovery **without moving the canonical file** (which stays in `core/` until the
item-1 folder-structure revision). Chosen specifically to avoid a mid-rigor-pass move that would
scramble the held-branch `git diff origin/main` review.
