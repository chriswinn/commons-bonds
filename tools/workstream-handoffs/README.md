# Workstream Handoffs

**Lifecycle (added 2026-06-10).** Top level holds ONLY live coordination: ACTIVE/QUEUED
handoffs + the CURRENT PM dashboard (newest `pm-session-handoff_<date>.md`). Handoffs whose
workstream has closed (completed / merged / ratified / superseded) live in [`archive/`](archive/)
— 98 closed handoffs moved there 2026-06-10 per `tools/conventions/archival-policy.md`; audit
trail preserved, nothing deleted. Live project status: root [`STATE.md`](../../STATE.md).
Orientation: root [`MAP.md`](../../MAP.md).

**Date drafted:** 2026-05-09. Updated 2026-05-10 with five additional handoffs from the manuscript-verification + publishing-pipeline-deepening phase, and with Ch 3 exclusion resolved (Ch 3 drafted 2026-05-09 via commit `3a8b096`; moved to Resolved exclusions).

**Purpose.** Per-workstream session handoff documents enabling fresh sessions to pick up specific workstreams from scratch without inheriting context drift. Each handoff is self-contained: a fresh session reads only the relevant handoff + the files it cross-references, and operates on a dedicated feature branch for that workstream.

**Branch discipline.** Each workstream gets a dedicated feature branch. A fresh session opens with `git checkout -b claude/<workstream>-<harness-id>` from a current `origin/main` after `git fetch`. Per-workstream branches reduce cross-contamination + make rescue / merge-to-main cleaner.

**Pipeline doctrine.** All publisher-facing prose moves through the canonical six-stage pipeline codified at [`tools/pipeline-doctrine/commons_bonds_pipeline_doctrine_v1.0.0.md`](../pipeline-doctrine/commons_bonds_pipeline_doctrine_v1.0.0.md) (v1.0.0 ratified 2026-05-17). Workstream sessions producing rigor-pass artifacts or content edits must respect the change-cascade routing rules in that doctrine + the cross-chapter workstream lifecycle codified there.

**Merge-to-main default (established 2026-05-16; superseded 2026-05-28 by merge-on-ratification).** Per the canonical CLAUDE.md §"Branch discipline + merge-to-main" + `tools/memory/feedback_merge_on_ratification.md`, end-user-facing prose now auto-merges to main on author ratification, same mechanism as internal scaffolding. Escape hatches: `MERGE-HOLD: <reason>` + `MERGE-AFTER: <gate>` commit-message-body markers. The 2026-05-16 "wait for explicit author merge" gate is superseded — sessions should NOT fall back to it. Never force-push `main`; never amend a commit already on `origin/main`.

## Handoffs

### Existing (2026-05-09)

| Workstream | Handoff file | Recommended branch prefix |
|---|---|---|
| Aeon submission (pitch) | `archive/aeon-submission-handoff_2026-05-09.md` | `claude/aeon-submission-` |
| Boston Review essay | `archive/boston-review-essay-handoff_2026-05-09.md` | `claude/boston-review-essay-` |
| Berggruen track | `archive/berggruen-track-handoff_2026-05-09.md` | `claude/berggruen-track-` |
| Outreach pipeline | `archive/outreach-pipeline-handoff_2026-05-09.md` | `claude/outreach-pipeline-` |
| Book proposal | `archive/book-proposal-handoff_2026-05-09.md` | `claude/book-proposal-sprint-` |
| Agent prep (target list) | `archive/agent-prep-handoff_2026-05-09.md` | `claude/agent-prep-` |
| Manuscript completion | `archive/manuscript-completion-handoff_2026-05-09.md` | `claude/manuscript-completion-` |

### Added 2026-05-10 (manuscript-verification + publishing-pipeline-deepening)

| Workstream | Handoff file | Recommended branch prefix |
|---|---|---|
| Path B audit (cross-chapter) | `archive/path-b-audit-cross-chapter-handoff_2026-05-10.md` | `claude/path-b-audit-cross-chapter-` |
| Apparatus register decision sweep | `archive/apparatus-register-sweep-handoff_2026-05-10.md` | `claude/apparatus-register-sweep-` |
| Cross-chapter consistency audit | `archive/cross-chapter-consistency-handoff_2026-05-10.md` | `claude/cross-chapter-consistency-` |
| Comp-titles deep matrix v0 | `archive/comp-titles-deep-matrix-handoff_2026-05-10.md` | `claude/comp-titles-deep-matrix-` |
| Aeon essay (post-acceptance, two-stage) — CONDITIONAL | `archive/aeon-essay-post-acceptance-two-stage-handoff_2026-05-10.md` | `claude/aeon-essay-drafting-` |

### Added 2026-05-11 (terminology-defense sweep + comp-titles Phase 2 + publishing pipeline)

| Workstream | Handoff file | Recommended branch prefix |
|---|---|---|
| Flagship-equation terminology defense sweep (narrow) | `archive/flagship-terms-defense-sweep-handoff_2026-05-11.md` | `claude/flagship-terms-defense-sweep-` |
| Comp-titles deep matrix v0 Phase 2 (just-in-time verification deferred) | `archive/comp-titles-deep-matrix-phase-2-handoff_2026-05-11.md` | `claude/comp-titles-deep-matrix-phase-2-` |
| Tech Appendix numbering reconciliation + chapter cross-reference re-validation (COMPLETE — Phases 1–5 landed on main 2026-05-11) | `archive/appendix-numbering-reconciliation-handoff_2026-05-11.md` | `claude/appendix-numbering-reconciliation-` |
| Publishing pipeline (markdown → .docx + HTML → PDF for publisher-ready artifacts) | `archive/publishing-pipeline-handoff_2026-05-11.md` | `claude/publishing-pipeline-` |
| Tech Appendix Scheme-4 cleanup (locally-restarted h4/h5 §-numbering inside §6.6 + §11.5–§11.11) | `archive/appendix-scheme-4-cleanup-handoff_2026-05-11.md` | `claude/appendix-scheme-4-cleanup-` |
| Ch 6 HTML → markdown conversion (eliminate hybrid-format anomaly) | `archive/ch6-html-to-markdown-conversion-handoff_2026-05-11.md` | `claude/ch6-html-to-markdown-` |
| $100 Barrel essay (derivative from withdrawn Noema §III) | `archive/100-barrel-essay-handoff_2026-05-11.md` | `claude/100-barrel-essay-` |
| Manuscript Stage-3 Rigor Pass (per-chapter + whole-book three-pass audit; 10+ parallel sessions paced over 2–3 weeks) | `archive/manuscript-stage-3-rigor-pass-handoff_2026-05-11.md` | `claude/manuscript-stage-3-` |

### Added 2026-05-17 (cross-chapter coherence work surfaced via Stage-3 rigor passes + pipeline-revision)

| Workstream | Handoff file | Recommended branch prefix |
|---|---|---|
| Cross-chapter rent-seeking engagement (Public Choice complementarity) — surfaced by Ch 1 Pass 3 REAUDIT v3 adversarial test; four touches across Ch 5 + Ch 9 + Tech Appendix + Ch 8 + bibliography expansion | `archive/cross-chapter-rent-seeking-engagement-handoff_2026-05-17.md` | `claude/rent-seeking-engagement-` |
| Pipeline-revision (drafting + fact-check + voice-polish + audience-load + rendering + sign-off pipeline doctrine — comprehensive revision) — **COMPLETED 2026-05-17.** Produced the full doctrine cluster (Stage 0→5 architecture in [`tools/pipeline-doctrine/commons_bonds_pipeline_doctrine_v1.0.0.md`](../pipeline-doctrine/commons_bonds_pipeline_doctrine_v1.0.0.md) + per-stage docs + invariant-gate infrastructure + YAML registries + check-corpus-invariants script + pre-pub-review-queue template). All 11 decisions ratified at session start. All chapters retrofit through new pipeline per ratified decision #9 — see "Pipeline-doctrine retrofit workstreams" section below. | `archive/pipeline-revision-handoff_2026-05-17.md` | `claude/pipeline-revision-` |
| **Render-pipeline-standardization** — Stage 4 canonical-pipeline decision (laptop `build-derivatives.sh` vs remote-container pipeline vs dual-pipeline). Surfaced 2026-05-17 by author observation that remote-container renders better than current laptop pipeline. Standardization-workstream pre-renders 2026-05-17 confirmed byte-level match with Sandy packet artifacts (`research/outreach/subjects/darity/`) for markdown-side outputs. **Superseded 2026-05-18 by render-toolchain-containerization (below); canonical-pipeline question is now resolved via Docker + remote-container sharing one apt-installed toolchain.** | `archive/render-pipeline-standardization-handoff_2026-05-17.md` | `claude/render-pipeline-standardization-` |

### Added 2026-05-18 (render-toolchain containerization)

| Workstream | Handoff file | Recommended branch prefix |
|---|---|---|
| **Render-toolchain containerization** — **COMPLETED 2026-05-18.** Produced the canonical apt-based installer ([`install-render-toolchain.sh`](../scripts/install-render-toolchain.sh)) + Dockerfile ([`Dockerfile.render`](../scripts/Dockerfile.render)) + SessionStart hook ([`.claude/settings.json`](../../.claude/settings.json)) + CI render-verify workflow ([`render-verify.yml`](../../.github/workflows/render-verify.yml)) + fixtures. Resolves Stage 4 doctrine §3.3 canonical-pipeline OPEN flag: Docker (laptop via Colima) + remote-container (Anthropic cloud) share one apt-installed canonical toolchain. Chrome intentionally NOT installed (wkhtmltopdf canonical for HTML→PDF per Sandy packet `e6ddf92`). Strict `--platform=linux/amd64` pinning. | [`archive/render-toolchain-containerization-handoff_2026-05-18.md`](archive/render-toolchain-containerization-handoff_2026-05-18.md) | `claude/render-toolchain-containerization-` |

### Added 2026-06-01 (portfolio triangulation discipline)

| Workstream | Handoff file | Recommended branch prefix |
|---|---|---|
| **Portfolio triangulation discipline** — PROPOSED 2026-06-01. Codifies three-audit triangulation (drafter's-self-audit + prior-independent + fresh-second-independent) as the default discipline for Wave 2+ derivative essays at the Pass 3.3 + 3.4 + 3.5 explicit-gate cascade. Wave 2 portfolio inventory + per-essay activation plan + PM-dashboard-integration spec + memory-entry draft at [`../memory/feedback_portfolio_triangulation_discipline.md`](../memory/feedback_portfolio_triangulation_discipline.md). Empirical anchor: Noema V-D second-independent audit 2026-05-28. Awaits author ratification. | [`archive/portfolio-triangulation-discipline-handoff_2026-06-01.md`](archive/portfolio-triangulation-discipline-handoff_2026-06-01.md) | `claude/noema-portfolio-triangulation-scaffolding-` |

### Pipeline-doctrine retrofit workstreams (post-2026-05-17 pipeline-revision)

Per ratified decision #9 (2026-05-17 brainstorm), all chapters run through the new pipeline once the doctrine cluster lands on `main`. The retrofit workstreams below apply the new-to-the-pipeline elements (Stage 1a invariant scan + Stage 1c cross-artifact coherence + Pass 3.4 audience-load robustness + Stage 4 render-integrity + Stage 5 sign-off + pre-pub review queue) to existing chapters. Per-chapter retrofit scope is detailed in [`archive/pipeline-revision-handoff_2026-05-17.md`](archive/pipeline-revision-handoff_2026-05-17.md) §6.2.

Retrofit workstreams spin up per chapter (parallelizable). PM session sequences after doctrine cluster lands on `main`.

| Chapter | Retrofit scope | Recommended branch prefix | Per-chapter handoff stub |
|---|---|---|---|
| Ch 1 (The Quiet Math) | 1a + 1c + 3.4 (already done; REAUDIT v3 PROPOSED) + 4 + 5 | `claude/ch1-pipeline-retrofit-` | [`archive/ch1-pipeline-retrofit-handoff_2026-05-17.md`](archive/ch1-pipeline-retrofit-handoff_2026-05-17.md) |
| Ch 2 (The Miner) | 1a + 1c + 3.2 + 3.3 + 3.4 + 4 + 5 | `claude/ch2-pipeline-retrofit-` | [`archive/ch2-pipeline-retrofit-handoff_2026-05-17.md`](archive/ch2-pipeline-retrofit-handoff_2026-05-17.md) |
| Ch 3 (The Waterman) | Full new pipeline application (Phase A not yet entered) | `claude/ch3-pipeline-retrofit-` | [`archive/ch3-pipeline-retrofit-handoff_2026-05-17.md`](archive/ch3-pipeline-retrofit-handoff_2026-05-17.md) |
| Ch 4 (The Existence Proof) | 1a + 1c + 3.1 verify + 3.2 verify + 3.3 + 3.4 + 4 + 5 | `claude/ch4-pipeline-retrofit-` | [`archive/ch4-pipeline-retrofit-handoff_2026-05-17.md`](archive/ch4-pipeline-retrofit-handoff_2026-05-17.md) |
| Ch 5 (The Accountability Gap) | 1a + 1c + 3.4 + 4 + 5 | `claude/ch5-pipeline-retrofit-` | [`archive/ch5-pipeline-retrofit-handoff_2026-05-17.md`](archive/ch5-pipeline-retrofit-handoff_2026-05-17.md) |
| Ch 6 (Three Ways of Counting) | 1a + 1c + 3.4 + 4 + 5 | `claude/ch6-pipeline-retrofit-` | [`archive/ch6-pipeline-retrofit-handoff_2026-05-17.md`](archive/ch6-pipeline-retrofit-handoff_2026-05-17.md) |
| Ch 7 (On Other Worlds) | 1a + 1c + 3.1 verify + 3.2 + 3.3 + 3.4 + 4 + 5 | `claude/ch7-pipeline-retrofit-` | [`archive/ch7-pipeline-retrofit-handoff_2026-05-17.md`](archive/ch7-pipeline-retrofit-handoff_2026-05-17.md) |
| Ch 8 (What Things Actually Cost) | 1a + 1c + 3.1 verify + 3.2 + 3.3 + 3.4 + 4 + 5 | `claude/ch8-pipeline-retrofit-` | [`archive/ch8-pipeline-retrofit-handoff_2026-05-17.md`](archive/ch8-pipeline-retrofit-handoff_2026-05-17.md) |
| Ch 9 (Pricing Honestly) | 1a + 1c + 3.1 verify + 3.2 + 3.3 + 3.4 + 4 + 5 | `claude/ch9-pipeline-retrofit-` | [`archive/ch9-pipeline-retrofit-handoff_2026-05-17.md`](archive/ch9-pipeline-retrofit-handoff_2026-05-17.md) |
| Ch 10 (Common Bonds) | 1a + 1c + 3.1 verify + 3.2 + 3.3 + 3.4 + 4 + 5 | `claude/ch10-pipeline-retrofit-` | [`archive/ch10-pipeline-retrofit-handoff_2026-05-17.md`](archive/ch10-pipeline-retrofit-handoff_2026-05-17.md) |
| Tech Appendix | 1a + 1c + 3.4 + 4 (highest stakes math-content) + 5 (academic-rigor sign-off most consequential) | `claude/ta-pipeline-retrofit-` | [`archive/ta-pipeline-retrofit-handoff_2026-05-17.md`](archive/ta-pipeline-retrofit-handoff_2026-05-17.md) |
| AuthorsNote | Full new pipeline application (likely abbreviated paratextual register) | `claude/authorsnote-pipeline-retrofit-` | [`archive/authorsnote-pipeline-retrofit-handoff_2026-05-17.md`](archive/authorsnote-pipeline-retrofit-handoff_2026-05-17.md) |
| Dedication (conditional) | Minimal-scope: 1a + 1c + 3.1 + 3.2 + 4 + 5. **Blocked until dedication text finalized.** | `claude/dedication-pipeline-retrofit-` | [`archive/dedication-pipeline-retrofit-handoff_2026-05-17.md`](archive/dedication-pipeline-retrofit-handoff_2026-05-17.md) |

Each per-chapter handoff stub scopes the per-chapter work (which sub-steps fire + why); the canonical procedure lives in the shared template [`archive/pipeline-retrofit-template_2026-05-17.md`](archive/pipeline-retrofit-template_2026-05-17.md). Future Claude sessions read the relevant stub + the template + the canonical doctrine to pick up a retrofit workstream from scratch.

### Special-case fresh-session handoffs (not workstream-handoffs; one-shot driving Stage-2 drafting)

These are stored elsewhere because they target a specific fresh-session task (Stage 2 of the two-stage discipline experiment) rather than a long-running workstream:

- `publishing/essays/noema-commons-bonds/_archive/session-handoffs/noema-session-handoff_2026-05-10.md` — drives Stage 2 fresh draft of Noema essay (Essay B in the experiment).
- `publishing/essays/aeon-mask-of-abundance/_archive/session-handoffs/aeon-session-handoff_2026-05-10.md` — drives Stage 2 fresh draft of Aeon pitch (Pitch B in the experiment).

### Project-management coordination session

A separate session that coordinates across all the above workstreams — tracks state, manages todos, surfaces dependencies, alerts to deadlines. Runs in parallel with topical sessions.

- **`pm-session-handoff_2026-06-04.md`** — **CURRENT PM session handoff / project dashboard.** Fresh PM sessions orient against this file. Captures the 2026-05-29 → 2026-06-04 session window: portfolio started SHIPPING (2 essays submitted — $100 Barrel + Boston Review; BR declined same-day and cascading to Public Books); Aeon-pattern V-D ratification workload effectively CLOSED (essays advanced into submission or RATIFIED-AWAITING-SUBMIT); live work is now submission cadence + cascade management + cover-letter rework + Aeon portal-watch. Process changes ratified this window: Amendment D (reception-chain audience weighting); G1 + G4 git-hygiene resolutions. **Update the branch first (`git fetch origin main && git rebase origin/main`) — parallel-session volume is high.**
- `archive/pm-session-handoff_2026-05-28-portfolio-aeon-pattern-complete.md` — superseded 2026-06-04; retained for audit trail (evening 2026-05-28; portfolio Aeon-pattern application complete — 11 units with V-D + audits).
- `archive/pm-session-handoff_2026-05-28.md` — superseded 2026-06-04; retained for audit trail (morning 2026-05-28; merge-on-ratification rule + per-essay rigor consolidation pattern; cascade-v2 amendments deferred).
- `archive/pm-session-handoff_2026-05-25.md` — superseded 2026-05-28; retained for audit trail (2026-05-25 → 2026-05-27 session window; Ch 1 + Ch 2 Stage 5 session close + portfolio refresh).
- `archive/pm-session-handoff_2026-05-24.md` — superseded 2026-05-25; retained for audit trail (2026-05-24 session — parallel-submission strategic call ratified; two new dashboards landed).
- `archive/pm-session-handoff_2026-05-18.md` — superseded 2026-05-24; retained as audit-trail for the 2026-05-18 → 2026-05-23 session window (refresh `aa04a4a` 2026-05-21 captured Phat anonymization + Ch 3 augmentation + Aeon Pass 3.1 + Chs 7/8/9 Phase C applications).
- `archive/pm-mobile-todo-dashboard_2026-05-15.md` — mobile-scope cut of the current dashboard (companion artifact; STALE; refresh after the 2026-05-24 submission sprint closes).
- `archive/pm-session-handoff_2026-05-13.md` — superseded 2026-05-18; retained as audit-trail for the 2026-05-13 → 2026-05-17 session window (Darity packet send + Chs 5/6 cycles closed + Chs 7-10 Pass 1 fired + pipeline doctrine v1.0.0).
- `archive/pm-session-handoff_2026-05-10.md` — superseded 2026-05-13; retained as audit-trail for the 2026-05-10 → 2026-05-13 session window.

## Excluded from these handoffs

*(None currently active. See Resolved exclusions below for historical record.)*

### Resolved exclusions

- **Ch 3 draft (The Waterman / Chesapeake)** — RESOLVED 2026-05-09. Was handled via a separate dedicated session per author direction; drafted as `manuscript/chapters/Chapter__3_TheWaterman__Draft.md` and landed on main via commit `3a8b096`. Source material: Colden + Moore public-record briefs (substitution-hypothesis CONFIRMED 2026-05-08). Ch 3 is now part of the all-10-chapters drafted set tracked in `archive/manuscript-completion-handoff_2026-05-09.md`.

## Cross-coordination

All workstreams should consult:
- `publishing/essays/_pipeline/cross-thread-todos.md` — items requiring another thread's action
- `publishing/essays/_pipeline/archive/cascade-plan_2026-05-06.md` — cascade state + decisions due
- `publishing/essays/_pipeline/decisions-log.md` — strategic decisions history
- Routine 1' (cross-thread state-snapshot, every other day) will surface drift across workstreams once scheduled (per `tools/routines/proposed_routines_v1.0.0.md` v2.0.0)
