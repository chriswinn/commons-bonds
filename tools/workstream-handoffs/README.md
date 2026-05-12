# Workstream Handoffs

**Date drafted:** 2026-05-09. Updated 2026-05-10 with five additional handoffs from the manuscript-verification + publishing-pipeline-deepening phase, and with Ch 3 exclusion resolved (Ch 3 drafted 2026-05-09 via commit `3a8b096`; moved to Resolved exclusions).

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
| Manuscript completion | `manuscript-completion-handoff_2026-05-09.md` | `claude/manuscript-completion-` |

### Added 2026-05-10 (manuscript-verification + publishing-pipeline-deepening)

| Workstream | Handoff file | Recommended branch prefix |
|---|---|---|
| Path B audit (cross-chapter) | `path-b-audit-cross-chapter-handoff_2026-05-10.md` | `claude/path-b-audit-cross-chapter-` |
| Apparatus register decision sweep | `apparatus-register-sweep-handoff_2026-05-10.md` | `claude/apparatus-register-sweep-` |
| Cross-chapter consistency audit | `cross-chapter-consistency-handoff_2026-05-10.md` | `claude/cross-chapter-consistency-` |
| Comp-titles deep matrix v0 | `comp-titles-deep-matrix-handoff_2026-05-10.md` | `claude/comp-titles-deep-matrix-` |
| Aeon essay (post-acceptance, two-stage) — CONDITIONAL | `aeon-essay-post-acceptance-two-stage-handoff_2026-05-10.md` | `claude/aeon-essay-drafting-` |

### Added 2026-05-11 (terminology-defense sweep + comp-titles Phase 2 + publishing pipeline)

| Workstream | Handoff file | Recommended branch prefix |
|---|---|---|
| Flagship-equation terminology defense sweep (narrow) | `flagship-terms-defense-sweep-handoff_2026-05-11.md` | `claude/flagship-terms-defense-sweep-` |
| Comp-titles deep matrix v0 Phase 2 (just-in-time verification deferred) | `comp-titles-deep-matrix-phase-2-handoff_2026-05-11.md` | `claude/comp-titles-deep-matrix-phase-2-` |
| Tech Appendix numbering reconciliation + chapter cross-reference re-validation (COMPLETE — Phases 1–5 landed on main 2026-05-11) | `appendix-numbering-reconciliation-handoff_2026-05-11.md` | `claude/appendix-numbering-reconciliation-` |
| Publishing pipeline (markdown → .docx + HTML → PDF for publisher-ready artifacts) | `publishing-pipeline-handoff_2026-05-11.md` | `claude/publishing-pipeline-` |
| Tech Appendix Scheme-4 cleanup (locally-restarted h4/h5 §-numbering inside §6.6 + §11.5–§11.11) | `appendix-scheme-4-cleanup-handoff_2026-05-11.md` | `claude/appendix-scheme-4-cleanup-` |
| Ch 6 HTML → markdown conversion (eliminate hybrid-format anomaly) | `ch6-html-to-markdown-conversion-handoff_2026-05-11.md` | `claude/ch6-html-to-markdown-` |
| $100 Barrel essay (derivative from withdrawn Noema §III) | `100-barrel-essay-handoff_2026-05-11.md` | `claude/100-barrel-essay-` |
| Manuscript Stage-3 Rigor Pass (per-chapter + whole-book three-pass audit; 10+ parallel sessions paced over 2–3 weeks) | `manuscript-stage-3-rigor-pass-handoff_2026-05-11.md` | `claude/manuscript-stage-3-` |

### Special-case fresh-session handoffs (not workstream-handoffs; one-shot driving Stage-2 drafting)

These are stored elsewhere because they target a specific fresh-session task (Stage 2 of the two-stage discipline experiment) rather than a long-running workstream:

- `manuscript/essay/Noema/noema-session-handoff_2026-05-10.md` — drives Stage 2 fresh draft of Noema essay (Essay B in the experiment).
- `manuscript/essay/aeon/aeon-session-handoff_2026-05-10.md` — drives Stage 2 fresh draft of Aeon pitch (Pitch B in the experiment).

### Project-management coordination session

A separate session that coordinates across all the above workstreams — tracks state, manages todos, surfaces dependencies, alerts to deadlines. Runs in parallel with topical sessions.

- `pm-session-handoff_2026-05-10.md` — PM session handoff. Updated in place as state evolves.

## Excluded from these handoffs

*(None currently active. See Resolved exclusions below for historical record.)*

### Resolved exclusions

- **Ch 3 draft (The Waterman / Chesapeake)** — RESOLVED 2026-05-09. Was handled via a separate dedicated session per author direction; drafted as `manuscript/chapters/Chapter__3_TheWaterman__Draft.md` and landed on main via commit `3a8b096`. Source material: Colden + Moore public-record briefs (substitution-hypothesis CONFIRMED 2026-05-08). Ch 3 is now part of the all-10-chapters drafted set tracked in `manuscript-completion-handoff_2026-05-09.md`.

## Cross-coordination

All workstreams should consult:
- `publishing/strategy/cross-thread-todos.md` — items requiring another thread's action
- `publishing/strategy/cascade-plan_2026-05-06.md` — cascade state + decisions due
- `publishing/strategy/decisions-log.md` — strategic decisions history
- Routine 1' (cross-thread state-snapshot, every other day) will surface drift across workstreams once scheduled (per `tools/routines/proposed_routines_v1.0.0.md` v2.0.0)
