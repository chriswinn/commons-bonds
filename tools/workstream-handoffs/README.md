# Workstream Handoffs

**Date drafted:** 2026-05-09. Updated 2026-05-10 with five additional handoffs from the manuscript-verification + publishing-pipeline-deepening phase, and with Ch 3 exclusion resolved (Ch 3 drafted 2026-05-09 via commit `3a8b096`; moved to Resolved exclusions).

**Purpose.** Per-workstream session handoff documents enabling fresh sessions to pick up specific workstreams from scratch without inheriting context drift. Each handoff is self-contained: a fresh session reads only the relevant handoff + the files it cross-references, and operates on a dedicated feature branch for that workstream.

**Branch discipline.** Each workstream gets a dedicated feature branch. A fresh session opens with `git checkout -b claude/<workstream>-<harness-id>` from a current `origin/main` after `git fetch`. Per-workstream branches reduce cross-contamination + make rescue / merge-to-main cleaner.

**Pipeline doctrine.** All publisher-facing prose moves through the canonical six-stage pipeline codified at [`tools/commons_bonds_pipeline_doctrine_v1.0.0.md`](../commons_bonds_pipeline_doctrine_v1.0.0.md) (v1.0.0 ratified 2026-05-17). Workstream sessions producing rigor-pass artifacts or content edits must respect the change-cascade routing rules in that doctrine + the cross-chapter workstream lifecycle codified there.

**Merge-to-main default (established 2026-05-16 by author direction).** Sessions that complete *author-ratified content changes* — Phase C spot-fix application sessions, chapter-text edits ratified by the author before the session begins, and similar work where the author has explicitly approved the change set ahead of the session — autonomously fast-forward merge their feature branch into `main` and push `origin/main` at session close, instead of stopping at the feature branch. Sessions that produce *PROPOSED artifacts awaiting ratification* (e.g., Stage-3 rigor-pass artifacts at any of the three passes; Stage-2 audience-blind drafts; audit findings prior to author disposition) and *direct content edits without prior author ratification* continue to stop at feature branch and wait for explicit author merge. Never force-push `main`; never amend a commit already on `origin/main`.

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

### Added 2026-05-17 (cross-chapter coherence work surfaced via Stage-3 rigor passes + pipeline-revision)

| Workstream | Handoff file | Recommended branch prefix |
|---|---|---|
| Cross-chapter rent-seeking engagement (Public Choice complementarity) — surfaced by Ch 1 Pass 3 REAUDIT v3 adversarial test; four touches across Ch 5 + Ch 9 + Tech Appendix + Ch 8 + bibliography expansion | `cross-chapter-rent-seeking-engagement-handoff_2026-05-17.md` | `claude/rent-seeking-engagement-` |
| Pipeline-revision (drafting + fact-check + voice-polish + audience-load + rendering + sign-off pipeline doctrine — comprehensive revision) — **COMPLETED 2026-05-17.** Produced the full doctrine cluster (Stage 0→5 architecture in [`tools/commons_bonds_pipeline_doctrine_v1.0.0.md`](../commons_bonds_pipeline_doctrine_v1.0.0.md) + per-stage docs + invariant-gate infrastructure + YAML registries + check-corpus-invariants script + pre-pub-review-queue template). All 11 decisions ratified at session start. All chapters retrofit through new pipeline per ratified decision #9 — see "Pipeline-doctrine retrofit workstreams" section below. | `pipeline-revision-handoff_2026-05-17.md` | `claude/pipeline-revision-` |
| **Render-pipeline-standardization** — Stage 4 canonical-pipeline decision (laptop `build-derivatives.sh` vs remote-container pipeline vs dual-pipeline). Surfaced 2026-05-17 by author observation that remote-container renders better than current laptop pipeline. Standardization-workstream pre-renders 2026-05-17 confirmed byte-level match with Sandy packet artifacts (`research/outreach/subjects/darity/`) for markdown-side outputs. **Co-fires in parallel with first 4 retrofit workstreams** (Ch 1 + Ch 5 + Ch 6 + TA) per the parallel-firing sequencing model. | `render-pipeline-standardization-handoff_2026-05-17.md` | `claude/render-pipeline-standardization-` |

### Pipeline-doctrine retrofit workstreams (post-2026-05-17 pipeline-revision)

Per ratified decision #9 (2026-05-17 brainstorm), all chapters run through the new pipeline once the doctrine cluster lands on `main`. The retrofit workstreams below apply the new-to-the-pipeline elements (Stage 1a invariant scan + Stage 1c cross-artifact coherence + Pass 3.4 audience-load robustness + Stage 4 render-integrity + Stage 5 sign-off + pre-pub review queue) to existing chapters. Per-chapter retrofit scope is detailed in [`pipeline-revision-handoff_2026-05-17.md`](pipeline-revision-handoff_2026-05-17.md) §6.2.

Retrofit workstreams spin up per chapter (parallelizable). PM session sequences after doctrine cluster lands on `main`.

| Chapter | Retrofit scope | Recommended branch prefix | Per-chapter handoff stub |
|---|---|---|---|
| Ch 1 (The Quiet Math) | 1a + 1c + 3.4 (already done; REAUDIT v3 PROPOSED) + 4 + 5 | `claude/ch1-pipeline-retrofit-` | [`ch1-pipeline-retrofit-handoff_2026-05-17.md`](ch1-pipeline-retrofit-handoff_2026-05-17.md) |
| Ch 2 (The Miner) | 1a + 1c + 3.2 + 3.3 + 3.4 + 4 + 5 | `claude/ch2-pipeline-retrofit-` | [`ch2-pipeline-retrofit-handoff_2026-05-17.md`](ch2-pipeline-retrofit-handoff_2026-05-17.md) |
| Ch 3 (The Waterman) | Full new pipeline application (Phase A not yet entered) | `claude/ch3-pipeline-retrofit-` | [`ch3-pipeline-retrofit-handoff_2026-05-17.md`](ch3-pipeline-retrofit-handoff_2026-05-17.md) |
| Ch 4 (The Existence Proof) | 1a + 1c + 3.1 verify + 3.2 verify + 3.3 + 3.4 + 4 + 5 | `claude/ch4-pipeline-retrofit-` | [`ch4-pipeline-retrofit-handoff_2026-05-17.md`](ch4-pipeline-retrofit-handoff_2026-05-17.md) |
| Ch 5 (The Accountability Gap) | 1a + 1c + 3.4 + 4 + 5 | `claude/ch5-pipeline-retrofit-` | [`ch5-pipeline-retrofit-handoff_2026-05-17.md`](ch5-pipeline-retrofit-handoff_2026-05-17.md) |
| Ch 6 (Three Ways of Counting) | 1a + 1c + 3.4 + 4 + 5 | `claude/ch6-pipeline-retrofit-` | [`ch6-pipeline-retrofit-handoff_2026-05-17.md`](ch6-pipeline-retrofit-handoff_2026-05-17.md) |
| Ch 7 (On Other Worlds) | 1a + 1c + 3.1 verify + 3.2 + 3.3 + 3.4 + 4 + 5 | `claude/ch7-pipeline-retrofit-` | [`ch7-pipeline-retrofit-handoff_2026-05-17.md`](ch7-pipeline-retrofit-handoff_2026-05-17.md) |
| Ch 8 (What Things Actually Cost) | 1a + 1c + 3.1 verify + 3.2 + 3.3 + 3.4 + 4 + 5 | `claude/ch8-pipeline-retrofit-` | [`ch8-pipeline-retrofit-handoff_2026-05-17.md`](ch8-pipeline-retrofit-handoff_2026-05-17.md) |
| Ch 9 (Pricing Honestly) | 1a + 1c + 3.1 verify + 3.2 + 3.3 + 3.4 + 4 + 5 | `claude/ch9-pipeline-retrofit-` | [`ch9-pipeline-retrofit-handoff_2026-05-17.md`](ch9-pipeline-retrofit-handoff_2026-05-17.md) |
| Ch 10 (Common Bonds) | 1a + 1c + 3.1 verify + 3.2 + 3.3 + 3.4 + 4 + 5 | `claude/ch10-pipeline-retrofit-` | [`ch10-pipeline-retrofit-handoff_2026-05-17.md`](ch10-pipeline-retrofit-handoff_2026-05-17.md) |
| Tech Appendix | 1a + 1c + 3.4 + 4 (highest stakes math-content) + 5 (academic-rigor sign-off most consequential) | `claude/ta-pipeline-retrofit-` | [`ta-pipeline-retrofit-handoff_2026-05-17.md`](ta-pipeline-retrofit-handoff_2026-05-17.md) |
| AuthorsNote | Full new pipeline application (likely abbreviated paratextual register) | `claude/authorsnote-pipeline-retrofit-` | [`authorsnote-pipeline-retrofit-handoff_2026-05-17.md`](authorsnote-pipeline-retrofit-handoff_2026-05-17.md) |
| Dedication (conditional) | Minimal-scope: 1a + 1c + 3.1 + 3.2 + 4 + 5. **Blocked until dedication text finalized.** | `claude/dedication-pipeline-retrofit-` | [`dedication-pipeline-retrofit-handoff_2026-05-17.md`](dedication-pipeline-retrofit-handoff_2026-05-17.md) |

Each per-chapter handoff stub scopes the per-chapter work (which sub-steps fire + why); the canonical procedure lives in the shared template [`pipeline-retrofit-template_2026-05-17.md`](pipeline-retrofit-template_2026-05-17.md). Future Claude sessions read the relevant stub + the template + the canonical doctrine to pick up a retrofit workstream from scratch.

### Special-case fresh-session handoffs (not workstream-handoffs; one-shot driving Stage-2 drafting)

These are stored elsewhere because they target a specific fresh-session task (Stage 2 of the two-stage discipline experiment) rather than a long-running workstream:

- `manuscript/essay/Noema/noema-session-handoff_2026-05-10.md` — drives Stage 2 fresh draft of Noema essay (Essay B in the experiment).
- `manuscript/essay/aeon/aeon-session-handoff_2026-05-10.md` — drives Stage 2 fresh draft of Aeon pitch (Pitch B in the experiment).

### Project-management coordination session

A separate session that coordinates across all the above workstreams — tracks state, manages todos, surfaces dependencies, alerts to deadlines. Runs in parallel with topical sessions.

- **`pm-session-handoff_2026-05-13.md`** — **CURRENT PM session handoff.** Fresh PM sessions orient against this file.
- `pm-session-handoff_2026-05-10.md` — superseded 2026-05-13; retained as audit-trail for the 2026-05-10 → 2026-05-13 session window.

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
