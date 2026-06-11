# MAP.md — repository orientation (read this first)

**What this is.** The single orientation document for this repo. A fresh session reads this
file, then [STATE.md](STATE.md) for live status, then goes to work. If you only read two
files, read those two.

**Maintenance rule.** Update MAP.md only when the repo's *structure* changes (a directory is
added, retired, or changes meaning). Day-to-day status changes go in STATE.md, never here.
Established 2026-06-10 (repo-reorg session); see `tools/conventions/archival-policy.md` for
the lifecycle rules this map assumes.

---

## Top-level taxonomy — what each directory IS (and is NOT)

| Directory | Purpose | Canonical content | What is NOT here |
|---|---|---|---|
| `manuscript/` | **The book.** Chapters + front matter + back matter. | `chapters/Chapter__1..10*.md`; `_BOOK_MANIFEST.md` (the authority on "what is the book"); `back-matter/` (generated reader-facing bib/glossary/notation) | The Technical Appendix body (lives in `core/`, symlinked here). Internal drafting inputs live in `manuscript/ledgers/`; superseded campaign state in `manuscript/archive/`. |
| `core/` | **The framework apparatus.** Technical Appendix + glossary + terms + methodology. | `manuscript/technical-appendix/TechnicalAppendix_v2.0.0.html` (canonical TA, formulas live ONLY here); `core/glossary/commons_bonds_updated_glossary_v4.html` (canonical); `core/terms/terms_index.md`; `manuscript/technical-appendix/symbol-registry_2026-06-07.md` (notation source of truth) | Chapters. (Historical chapter/case-study *audits* that used to sit in `core/chapters/` + `core/case-studies/` now live in `tools/audits/`.) |
| `publishing/` | **Everything outbound.** Essays, op-eds, book proposal, agents, venues, blurbs. | `essays/<venue>/` packages (essay.md + cover-letter.md + rigor/); `op-eds/<slug>/`; `book-proposal/` (numbered prose sections); `essays/_pipeline/` (cascade plan, schedule, todos, decisions log) | Book chapters. Research substrate. Submission *status* (that's STATE.md). |
| `research/` | **Source material.** Case studies, bibliography master, outreach, story substrate. | `research/literature/bibliography.md` (THE bibliographic source of truth, superset); `research/case-studies/` (17 case files); `research/outreach/subjects/<name>/` + consent tracker; `research/story-drafts/` (raw scene substrate) | Polished prose. The reader-facing bibliography (generated to `manuscript/back-matter/`). |
| `tools/` | **Methodology + session machinery.** Doctrine, conventions, memory, handoffs, rigor history, scripts, gates. | `pipeline-doctrine/` (canonical 6-stage pipeline); `conventions/` (status markers, archival policy); `memory/` (cross-session discipline, indexed); `workstream-handoffs/` (live session coordination); `rigor-passes/` (chapter-side + cross-essay rigor history); `scripts/` (render, invariants, link check, back-matter build); `quality-gates/` | Per-essay rigor history (migrated to `publishing/essays/<venue>/rigor/` per the 2026-05-28 consolidation). |
| `alignment/` | **Framework positioning documents.** Five live root docs. | `commons_bonds_working_principles_v1.0.0.md`, `..._framework_positioning_disciplines_...`, `..._vocabulary_strategy_...`, `..._open_insights_...`, `..._personal_stories_candidates_...` | Live session state. `sessions/` is the LEGACY pre-2026-05-09 session-handoff system, superseded by `tools/workstream-handoffs/`; `decisions/` + `patches/` are April-2026 historical records. |
| `archive/` | **Project-wide retired + deferred.** | `_OneDayMaybe/` (deferred work, books 2/3 material); retired frameworks (`decomposition/`, `dimensions/`) | Per-directory version history (that lives in each directory's local `archive//_archive/`; see archival policy). |
| Root files | Entry points. | `MAP.md` (this), `STATE.md` (live status), `CLAUDE.md` (session discipline, auto-loaded), `README.md` (project intro), `AGENTS.md` | — |

## "Where do I find …?" — routing table

| Question | Go to |
|---|---|
| Status of any essay / op-ed / proposal / workstream? | [STATE.md](STATE.md) (then the per-unit README it points to) |
| What is "the book" — complete component list? | `manuscript/_BOOK_MANIFEST.md` |
| How does the writing pipeline work (stages, passes)? | `tools/pipeline-doctrine/README.md` |
| What do PROPOSED / RATIFIED / MERGE-HOLD etc. mean? | `tools/conventions/status-markers.md` |
| Branch / merge / worktree discipline? | `CLAUDE.md` (auto-loaded) |
| Cross-session lessons + author preferences? | `tools/memory/README.md` (index) |
| Current strategic plan + submission schedule? | `publishing/essays/_pipeline/cascade-plan_v2_2026-05-24.md` + `june-2026-submission-schedule.md` |
| What is every live session doing right now? | newest `tools/workstream-handoffs/pm-session-handoff_<date>.md` (detail layer behind STATE.md) |
| A specific essay's text, cover letter, rigor history? | `publishing/essays/<venue>/` (self-contained package) |
| The math / formulas / symbols? | `manuscript/technical-appendix/TechnicalAppendix_v2.0.0.html` (formulas exist ONLY there); notation source: `manuscript/technical-appendix/symbol-registry_2026-06-07.md` Part 7 |
| Which sources back a figure? | `research/literature/bibliography.md` (+ `tools/back-matter/citation-crossref-index.md` for where-cited) |
| Why was X archived / where did it go? | the local `archive/` subdir of its home directory; policy in `tools/conventions/archival-policy.md` |

## Lifecycle conventions (summary)

- **Status vocabulary** is codified in `tools/conventions/status-markers.md`. Use it; do not invent markers.
- **Active vs archive:** every coordination directory keeps only LIVE files at its top level;
  closed/superseded artifacts move into its local `archive/` subdir (audit trail is preserved,
  never deleted). Policy: `tools/conventions/archival-policy.md`.
- **Dated one-shot artifacts** (`<topic>_<date>.md`) archive when their workstream closes.
- **Reader-facing back matter** is GENERATED (`tools/back-matter/build.py gen-all`), never hand-edited.
- **Link integrity:** `python3 tools/scripts/check-repo-links.py --summary` before/after moving files; zero new breaks.

## Live-session ownership (do not edit from other sessions)

Check `git worktree list` + STATE.md §Workstreams before touching:
- `manuscript/` `_`-prefixed root files + `manuscript/chapters/` + `research/literature/bibliography.md` — **redraft campaign**.
- `publishing/book-proposal/` prose — **book-proposal sprint**.

## Known deferred structural debt (tracked, intentional)

- ~~`manuscript/` `_`-file reorg~~ **EXECUTED 2026-06-10** (fact-ground → `manuscript/ledgers/`; campaign state → `manuscript/archive/redraft-campaign-2026-06/`). Source-file relocations + TA→manuscript move remain deferred: `tools/workstream-handoffs/back-matter-deferred-moves-handoff_2026-06-09.md`.
- Directory status tags (`_SUBMITTED-<date>` renames): deferred past Wave 1 (author call 2026-06-10); STATE.md serves the need meanwhile.
- In-TA Notation section + symbol-registry Part 7 completeness: same deferred-moves handoff, items 7–8.
- ~2.5k pre-existing broken path references in historical files (measured 2026-06-10): left as-is in audit-trail docs; gate is zero NEW breaks.
