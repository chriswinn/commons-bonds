# Archival policy — where retired things go and when

**Established 2026-06-10 (repo-reorg session), codifying the previously-implicit pattern.**
Nothing is ever deleted; archival is relocation for navigation's sake. Audit trail is sacred.

## The two-layer rule

1. **Local `archive/` (or `_archive/`) subdir** — per-directory version history and closed
   artifacts that belong to that directory's story. Examples: `tools/workstream-handoffs/archive/`
   (closed handoffs), `core/technical-appendix/archive/` (old TA versions),
   `publishing/essays/<venue>/_archive/` (draft variants), `manuscript/chapters/archive/`
   (guidance docs, regressed drafts).
2. **Central `/archive/`** — project-WIDE deferred or retired material that has no live home:
   `_OneDayMaybe/` (books 2/3, deferred ideas), retired frameworks (`decomposition/`,
   `dimensions/`).

Rule of thumb: if a future session debugging THAT directory's history would look for it, archive
locally. If it is detached from any live directory's concern, archive centrally.

## When to archive

- **Workstream handoffs:** when the workstream CLOSES (its work merged / its decision ratified /
  superseded by a newer handoff) → `tools/workstream-handoffs/archive/`. The newest PM dashboard
  stays at top level; superseded dashboards archive.
- **Dated one-shot artifacts** (`<topic>_<date>.md` audits, comparisons, sweeps): when the
  workstream that consumed them closes → the local archive of where they live.
- **Superseded versions** (glossary v2/v3, cascade-plan v1, old protocol versions): immediately
  upon a successor being marked canonical → local archive.
- **Rigor passes:** per-essay rigor lives with the essay (`publishing/essays/<venue>/rigor/`,
  2026-05-28 consolidation). Chapter-side + cross-essay rigor in `tools/rigor-passes/`; historical
  eras (superseded framework versions, pre-pipeline-v3 artifacts) → `tools/rigor-passes/archive/`.

## How to archive (mechanics)

1. `git mv` (preserves history) — never copy-and-delete.
2. **Before moving, check inbound references:** `grep -rl "<filename>" --include=*.md .` —
   fix references in LIVE files; references inside other archived/historical files may stay.
3. After the batch: `python3 tools/scripts/check-repo-links.py --summary` — zero NEW breaks
   vs the pre-move count.
4. If a directory's README indexes its contents, update the index in the same commit.

## What never moves without explicit author direction

- Anything a LIVE session owns (check `STATE.md` §Active workstreams + `git worktree list`).
- Canonical files (the current TA, chapters, bibliography master, current glossary, doctrine).
- `UNCLEAR`-status artifacts — classify first, move later.

## Retired/SUPERSEDED markers and reader-facing prose

Markers like SUPERSEDED/RETIRED/HELD belong ONLY in internal files. They must never appear in
reader-facing documents (chapters, TA, essays, proposal prose, generated back matter) — the
back-matter generator enforces this by construction; the invariants gate scans for leaks.
