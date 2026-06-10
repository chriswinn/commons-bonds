# Reader-facing scaffolding-leak audit (WS4) — 2026-06-09

**Session:** refactor-bib-consolidation. **Rule audited:** retired/historical/SUPERSEDED/process-
scaffolding markers must NEVER appear in reader-facing documentation (TA, chapters, book proposal,
essays, op-eds); they belong only in internal working files (rigor/, _archive/, _pipeline/, ledgers).

## Method

Grepped the **actual reader-facing prose files** (not their scaffolding subdirs) for hard
scaffolding markers: `SUPERSEDED|RETIRED|DEPRECATED|RATIFIED|PROPOSED|MERGE-HOLD|Phase C|Pass 3.x|
F-Vn|Amendment A–E`. Surfaces: 10 chapters + front matter (`_AUTHORSNOTE`, `_Dedication`,
`_ACKNOWLEDGMENTS`), 9 `essay.md` + cover-letters, 2 `op-ed.md`, book-proposal prose, and the TA.

## Findings

| Surface | Reader-facing prose result | Action |
|---|---|---|
| **TA** (`TechnicalAppendix_v2.0.0.html`) | **CLEAN** — 0 markers | none needed (this session owns it; confirmed clean) |
| **10 chapters + front matter** | **CLEAN** — 0 markers | none |
| **9 essays + cover-letters** (`essay.md`/`cover-letter.md`) | **CLEAN** — 0 markers | none |
| **2 op-eds** (`op-ed.md`) | **CLEAN** — 0 markers | none |
| **New `manuscript/back-matter/` outputs** | **CLEAN by construction** — generator strips scaffolding + asserts | none |
| **book-proposal `00_overview.md`** | **1 LEAK** — a `**Status.** **RATIFIED 2026-06-09** … Pass 3.1 … Stage 5 …` header block at the top | **FLAG (live-owned)** — see below |

**Important framing.** The large raw counts a naive `grep -r` produces over `publishing/essays/`
(22k+), `publishing/op-eds/` (476), and `publishing/book-proposal/` (145) are **all inside
scaffolding subdirs** (`rigor/`, `_archive/`, `_pipeline/`, dated planning files, news-peg variant
siblings) where the markers BELONG. Scoped to the files that actually ship to a reader, the corpus
is clean save the one item below. The earlier "649 repo-wide HIGH" (TA closeout note) is the same
phenomenon — concentrated in internal scaffolding, not reader-facing prose.

## The one finding — book-proposal `00_overview.md` (FLAG, do not fix here)

`publishing/book-proposal/00_overview.md:5` opens with a process-scaffolding status block:
`**Status.** **RATIFIED 2026-06-09** via Stage 5 sign-off … Pass 3.1 … Pass 3.5 … Stage 4 render-
audit deferred …`. This is editorial-pipeline metadata; it must be **stripped before the overview
ships in the proposal package** to literary agents / acquisitions editors.

- **Not fixed this session:** the book proposal is owned by a LIVE session
  (`claude/book-proposal-sprint-260603-e402b7`). Editing it here would collide.
- **Recommended disposition:** the book-proposal-sprint session (or package-assembly step) either
  (a) moves the status block into the file's `rigor/` sibling, or (b) confirms the package-assembly
  step strips status headers before send. Either resolves the leak. Low urgency (the package is not
  yet sent; send window ~Jun 24–Jul 1, 2026 per the file).

## Conclusion

Reader-facing prose is **clean of hard scaffolding markers** across the TA, all chapters, all
essays/cover-letters, and both op-eds. The new `manuscript/back-matter/` outputs enforce the rule
by construction (generator strips scaffolding and asserts zero leakage). The single exception is a
status header in `book-proposal/00_overview.md`, flagged to its live owner. **No reader-facing
in-place edits were required by this audit** beyond the back-matter generation already done.
