# manuscript/ — the book

**Authority on "what is the book": [`_BOOK_MANIFEST.md`](_BOOK_MANIFEST.md).** Any whole-book
operation must include every component listed there (the TA lives in `core/technical-appendix/`,
symlinked at `technical-appendix/`).

## Layout

- `chapters/` — the 10 canonical chapters + front matter (`_Dedication`, `_AUTHORSNOTE…`,
  `_ACKNOWLEDGMENTS`). `_Draft` suffix = working draft, redline pending. `chapters/archive/` =
  guidance docs + regressed drafts.
- `back-matter/` — GENERATED reader-facing bibliography / glossary / notation
  (`python3 tools/back-matter/build.py gen-all`; never hand-edit).
- `technical-appendix/` — symlink to the canonical TA in `core/technical-appendix/`.

## The `_`-prefixed root files (⚠ redraft-campaign working state)

The ~35 `_UPPERCASE`/`_lowercase` files at this level (action lists, comparison verdicts,
ledgers, coherence maps, `.json` detail pairs) are the LIVE working state of the
**redraft-compare campaign** (`_REDRAFT-CAMPAIGN-RESUME_2026-06-06.md` is its control file).
**Do not move, rename, or edit them from other sessions.** Their post-campaign relocation is
planned in `tools/workstream-handoffs/back-matter-deferred-moves-handoff_2026-06-09.md`.
Exceptions usable by any session (author-owned canonical references):
`_BOOK_MANIFEST.md`, `_CANONICAL_FIGURE_LEDGER.md` (RATIFIED figure source of truth).
