# Workstream Handoffs

**Date drafted:** 2026-05-09

**Purpose.** Per-workstream session handoff documents enabling fresh sessions to pick up specific workstreams from scratch without inheriting context drift. Each handoff is self-contained: a fresh session reads only the relevant handoff + the files it cross-references, and operates on a dedicated feature branch for that workstream.

**Branch discipline.** Each workstream gets a dedicated feature branch. A fresh session opens with `git checkout -b claude/<workstream>-<harness-id>` from a current `origin/main` after `git fetch`. Per-workstream branches reduce cross-contamination + make rescue / merge-to-main cleaner.

## Handoffs

| Workstream | Handoff file | Recommended branch prefix |
|---|---|---|
| Aeon submission | `aeon-submission-handoff_2026-05-09.md` | `claude/aeon-submission-` |
| Boston Review essay | `boston-review-essay-handoff_2026-05-09.md` | `claude/boston-review-essay-` |
| Berggruen track | `berggruen-track-handoff_2026-05-09.md` | `claude/berggruen-track-` |
| Outreach pipeline | `outreach-pipeline-handoff_2026-05-09.md` | `claude/outreach-pipeline-` |
| Book proposal | `book-proposal-handoff_2026-05-09.md` | `claude/book-proposal-sprint-` |
| Agent prep | `agent-prep-handoff_2026-05-09.md` | `claude/agent-prep-` |
| Manuscript completion (excluding Ch 3) | `manuscript-completion-handoff_2026-05-09.md` | `claude/manuscript-completion-` |

## Excluded from these handoffs

- **Noema essay** — handled separately via `manuscript/essay/Noema/noema-essay-drafting-plan_2026-05-08.md` + `manuscript/essay/Noema/rewrite-plan_2026-05-01.md`. 100% drafted-able under hybrid operational approach (commit `9aee18d`).
- **Ch 3 draft (Watermen / Chesapeake)** — handled via separate dedicated session per author direction. Source material: Colden + Moore public-record briefs; substitution-hypothesis CONFIRMED 2026-05-08.

## Cross-coordination

All workstreams should consult:
- `publishing/strategy/cross-thread-todos.md` — items requiring another thread's action
- `publishing/strategy/cascade-plan_2026-05-06.md` — cascade state + decisions due
- `publishing/strategy/decisions-log.md` — strategic decisions history
- Routine 1' (cross-thread state-snapshot, every other day) will surface drift across workstreams once scheduled (per `tools/routines/proposed_routines_v1.0.0.md` v2.0.0)
