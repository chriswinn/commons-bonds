# Workstream Handoffs

**Date drafted:** 2026-05-09. Updated 2026-05-10 with five additional handoffs from the manuscript-verification + publishing-pipeline-deepening phase.

**Purpose.** Per-workstream session handoff documents enabling fresh sessions to pick up specific workstreams from scratch without inheriting context drift. Each handoff is self-contained: a fresh session reads only the relevant handoff + the files it cross-references, and operates on a dedicated feature branch for that workstream.

**Branch discipline.** Each workstream gets a dedicated feature branch. A fresh session opens with `git checkout -b claude/<workstream>-<harness-id>` from a current `origin/main` after `git fetch`. Per-workstream branches reduce cross-contamination + make rescue / merge-to-main cleaner.

## Handoffs

### Existing (2026-05-09)

| Workstream | Handoff file | Recommended branch prefix |
|---|---|---|
| Aeon submission (pitch) | `aeon-submission-handoff_2026-05-09.md` | `claude/aeon-submission-` |
| Boston Review essay | `boston-review-essay-handoff_2026-05-09.md` | `claude/boston-review-essay-` |
| Berggruen track | `berggruen-track-handoff_2026-05-09.md` | `claude/berggruen-track-` |
| Outreach pipeline | `outreach-pipeline-handoff_2026-05-09.md` | `claude/outreach-pipeline-` |
| Book proposal | `book-proposal-handoff_2026-05-09.md` | `claude/book-proposal-sprint-` |
| Agent prep (target list) | `agent-prep-handoff_2026-05-09.md` | `claude/agent-prep-` |
| Manuscript completion (excluding Ch 3) | `manuscript-completion-handoff_2026-05-09.md` | `claude/manuscript-completion-` |

### Added 2026-05-10 (manuscript-verification + publishing-pipeline-deepening)

| Workstream | Handoff file | Recommended branch prefix |
|---|---|---|
| Path B audit (cross-chapter) | `path-b-audit-cross-chapter-handoff_2026-05-10.md` | `claude/path-b-audit-cross-chapter-` |
| Apparatus register decision sweep | `apparatus-register-sweep-handoff_2026-05-10.md` | `claude/apparatus-register-sweep-` |
| Cross-chapter consistency audit | `cross-chapter-consistency-handoff_2026-05-10.md` | `claude/cross-chapter-consistency-` |
| Comp-titles deep matrix v0 | `comp-titles-deep-matrix-handoff_2026-05-10.md` | `claude/comp-titles-deep-matrix-` |
| Aeon essay (post-acceptance, two-stage) — CONDITIONAL | `aeon-essay-post-acceptance-two-stage-handoff_2026-05-10.md` | `claude/aeon-essay-drafting-` |

### Special-case fresh-session handoffs (not workstream-handoffs; one-shot driving Stage-2 drafting)

These are stored elsewhere because they target a specific fresh-session task (Stage 2 of the two-stage discipline experiment) rather than a long-running workstream:

- `manuscript/essay/Noema/noema-session-handoff_2026-05-10.md` — drives Stage 2 fresh draft of Noema essay (Essay B in the experiment).
- `manuscript/essay/aeon/aeon-session-handoff_2026-05-10.md` — drives Stage 2 fresh draft of Aeon pitch (Pitch B in the experiment).

### Project-management coordination session

A separate session that coordinates across all the above workstreams — tracks state, manages todos, surfaces dependencies, alerts to deadlines. Runs in parallel with topical sessions.

- `pm-session-handoff_2026-05-10.md` — PM session handoff. Updated in place as state evolves.

## Excluded from these handoffs

- **Ch 3 draft (Watermen / Chesapeake)** — handled via separate dedicated session per author direction. Source material: Colden + Moore public-record briefs; substitution-hypothesis CONFIRMED 2026-05-08.

## Cross-coordination

All workstreams should consult:
- `publishing/strategy/cross-thread-todos.md` — items requiring another thread's action
- `publishing/strategy/cascade-plan_2026-05-06.md` — cascade state + decisions due
- `publishing/strategy/decisions-log.md` — strategic decisions history
- Routine 1' (cross-thread state-snapshot, every other day) will surface drift across workstreams once scheduled (per `tools/routines/proposed_routines_v1.0.0.md` v2.0.0)
