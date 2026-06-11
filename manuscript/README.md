# manuscript/ — the book

**Authority on "what is the book": [`_BOOK_MANIFEST.md`](_BOOK_MANIFEST.md).** Any whole-book
operation must include every component listed there (the TA lives in `manuscript/technical-appendix/`,
symlinked at `technical-appendix/`).

## Layout

- `chapters/` — the 10 canonical chapters + front matter (`_Dedication`, `_AUTHORSNOTE…`,
  `_ACKNOWLEDGMENTS`). `_Draft` suffix = working draft, redline pending. `chapters/archive/` =
  guidance docs + regressed drafts.
- `back-matter/` — GENERATED reader-facing bibliography / glossary / notation
  (`python3 tools/back-matter/build.py gen-all`; never hand-edit).
- `technical-appendix/` — symlink to the canonical TA in `manuscript/technical-appendix/`.

## Layout of internal scaffolding (reorganized 2026-06-10)

- **`ledgers/`** — the fact-ground inputs for chapter drafting: canonical figure ledger
  (RATIFIED figure source of truth), citation-evidence / research-results / deep-source /
  dangling-reference ledgers (+ JSON detail), seam map, book-coherence map, cross-chapter +
  contribution-matrix + essay-reveal ledgers, per-chapter coherence-gap audits (Ch1–Ch3),
  candidate beats. **Drafting sessions read these; update in place.**
- **`archive/redraft-campaign-2026-06/`** — the 2026-06 redraft-compare campaign's working
  state (comparison verdicts, action list, readiness map, resume doc), preserved as record.
  The campaign was superseded 2026-06-10 by the whole-cloth prose campaign.
- Root keeps only: the chapters, [`_BOOK_MANIFEST.md`](_BOOK_MANIFEST.md) (the authority on
  "what is the book"), `back-matter/` (generated), and any live draft-comparison candidates
  (e.g. `_CH1-FABLE-VARIANT_2026-06-10.md`).
