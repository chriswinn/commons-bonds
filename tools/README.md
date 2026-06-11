# tools/ — Canonical Working Methodology

This folder holds the canonical methodology documents for the Commons Bonds project — the set of files uploaded to Claude at the start of each work session.

**Convention:** `tools/` top-level = session upload set. Subfolders = session-upload-adjacent material (recent pass records, triage inputs, superseded versions).

---

## Session-start workflow (current as of 2026-05-31)

This section was refreshed 2026-05-31 per memory-process-review v2 B.1 ratification. Prior to that refresh, this section documented an upload-set workflow (Drive-era; v1.28.0 handoff + v2.2.0 rigor protocol + abundance-dimensions methodology upload) that no longer matches how sessions actually start. Current discipline:

1. **First tool call MUST be `git worktree add`** — every fresh CC session creates an isolated git worktree (`/Users/c17n/commons-bonds-<workstream-slug>-<harness-id>`) before any other operation. Branch-contamination is the failure mode this prevents under sustained 20-35+ concurrent-session operation (per author observation 2026-05-26). Canonical reference: [`memory/feedback_worktree_isolation_for_parallel_sessions.md`](memory/feedback_worktree_isolation_for_parallel_sessions.md). Defense in depth: a SessionStart hook ([`scripts/session-start-worktree-isolation.sh`](scripts/session-start-worktree-isolation.sh)) emits a warning + the worktree-isolation paste-text ([`drafting-templates/worktree-isolation-paste-text.md`](drafting-templates/worktree-isolation-paste-text.md)) is embedded in every kickoff template.
2. **Paste-text kickoff** — workstream-specific kickoff paste-texts live in [`drafting-templates/`](drafting-templates/) for class-level templates (Stage 0/1/2/3 templates; audience-pressure-test-construction; worktree-isolation paste-text) and in [`workstream-handoffs/`](workstream-handoffs/) for instance-level paste-texts (per-workstream kickoffs, dated). Sessions launch by pasting the relevant kickoff text after the worktree-add step.
3. **PM-coordination sessions** — start by reading the latest `tools/workstream-handoffs/pm-session-handoff_<DATE>.md` PM dashboard. That document holds the current state-of-week snapshot: priority-labeled status buckets, per-chapter Stage state, per-essay submission state, decisions pending, date-anchored action list. Index at [`workstream-handoffs/README.md`](workstream-handoffs/README.md).
4. **Always-load context is automatic** — `CLAUDE.md` + the three `@import`-hooked memory files (audience-aware drafting v3.1 doctrine; named-subject consent; verify-stale-claims) load into every session by default. See [`memory/README.md`](memory/README.md) for the always-load set + situational discipline files.

The session-start workflow no longer relies on a fixed upload set; required context loads automatically via the always-load hooks + the kickoff paste-text names whatever situational context the session needs.

---

## Subfolders

**Updated 2026-05-28** — inventory refreshed to match actual subdir contents; pre-2026-05-28 versions of this section referenced `tools/triage/` (no longer present) and omitted most active subdirs.

### `tools/conventions/`

Cross-cutting convention references. Currently one entry: [`conventions/status-markers.md`](conventions/status-markers.md) — codifies file-header `Status:` values, rigor-pass filename conventions, per-essay directory-name tags, commit-message escape-hatch markers (`MERGE-HOLD` / `MERGE-AFTER`), PM dashboard emoji conventions, and the state-transition diagram. Added 2026-05-28 per project-review S7. Cross-linked from `CLAUDE.md`, `publishing/essays/README.md`, and `tools/memory/feedback_pm_dashboard_structure.md`.

### `tools/pipeline-doctrine/`

Canonical pipeline doctrine: four files (v1.0.0 main + Stage 1 / Stage 4 / Stage 5 deep-dives) covering the six-stage architecture, two-class cascade, invariant-gate infrastructure, and cross-chapter workstream lifecycle. Promoted from `tools/` top-level into this subdir 2026-05-28 (S6 of the structure-cleanup-followup session). Index + when-to-read-which guide at [`pipeline-doctrine/README.md`](pipeline-doctrine/README.md).

### `tools/rigor-passes/`

Chapter-side + cross-essay rigor history (per-essay rigor lives with each essay since 2026-05-28). ~98 live files + ~97 April-era artifacts in `rigor-passes/archive/` (2026-06-10 era split). Naming pattern: `commons_bonds_rigor_pass_YYYY-MM-DD_<slug>_<stage>_v#_#_#.md`.

**Migration queue (2026-05-28).** Per-essay rigor consolidation pattern ratified 2026-05-28 (see `publishing/essays/README.md` §Per-essay directory layout). Per-essay rigor artifacts (5 passes + Stage 1 brief + Stage 4 + Stage 5 + pre-pub-review-queue) are migrating into `publishing/essays/<venue>/rigor/` subdirs. After migration, `tools/rigor-passes/` will hold only:
- Cross-essay rigor (e.g., Wave 2 derivative-planning Stage 0 batch covering Ch 2 + Ch 3 + Ch 4 + Ch 8)
- Chapter-side rigor for `manuscript/chapters/Chapter__N_*` (book-side, not essay-side)
- Pre-2026-05-28 historical artifacts retained for lineage

### `tools/workstream-handoffs/`

Live session coordination: ACTIVE/QUEUED handoffs + the CURRENT PM dashboard (~13 live files); ~98 closed handoffs in `workstream-handoffs/archive/` (2026-06-10 lifecycle split). Naming patterns: `pm-session-handoff_YYYY-MM-DD.md` (PM dashboards), `<workstream-slug>-handoff_YYYY-MM-DD.md` (workstream handoffs), `<workstream-slug>-paste-text_YYYY-MM-DD.md` (kick-off scaffolds). Index at [`workstream-handoffs/README.md`](workstream-handoffs/README.md).

### `tools/memory/`

In-repo mirror of the cross-session discipline registry (laptop copy at `~/.claude/projects/-Users-c17n-commons-bonds/memory/`). 19+ situational + 3 always-loaded discipline files (feedback / project / reference). Index at [`memory/README.md`](memory/README.md); always-loaded set hooked from `CLAUDE.md` via `@import`.

### `tools/quality-gates/`

Live gate-status records + invariant-gate registries. Subdirs:
- `scaffolding-patterns.yaml` + `regressed-patterns.yaml` — pattern registries for invariant-gate scans
- `clean-baselines/` — per-chapter + per-essay Stage 1a invariant-gate-pass records
- `coherence-checks/` — per-chapter + per-essay Stage 1c coherence-check records
- `render-baselines/` — Docker container outputs for Stage 4 render audits
- `sign-offs/` — per-chapter + per-essay Stage 5 sign-off records

Updates per session as artifacts move through Stage 1 + Stage 4 + Stage 5 gates.

### `tools/drafting-templates/`

Reusable class-level templates: `stage-0-publishing-strategy-rigor-test.md`, `stage-1-audience-aware-structure-pass.md`, `stage-2-audience-blind-flow-draft.md`, `stage-3-three-pass-rigor-audit.md`, `audience-pressure-test-construction.md`. Plus session-scaffolding paste-texts (worktree-isolation, session-checkin). Don't change per-session; instance-level paste-texts go in `workstream-handoffs/`.

### `tools/stage-1-briefs/`

Chapter-side Stage-1 briefs (ready-to-draft gate for workstreams that touch chapters, not essays). Per-essay Stage 1 briefs live in `publishing/essays/<venue>/rigor/stage-1-brief.md` per 2026-05-28 consolidation.

### `tools/pre-submission-reviews/`

Stage-5 hand-off artifacts: per-essay + per-chapter pre-publication review queue records. Naming: `<slug>_pre_pub_review_queue_v#_#_#.md`. Also holds historical PCR (pre-submission comprehensive review) artifacts from earlier project phases.

### `tools/memory-updates/`

Staging area for memory-discipline updates. New / amended discipline files land here first, then mirror into `tools/memory/` once the in-repo mirror is updated. Active class even at low volume (one file as of 2026-05-28); kept per S8 decision 2026-05-28.

### `tools/scripts/`

CLI utilities + supporting binaries: `build-derivatives.sh` (.md / .html → .docx + .pdf), `check-corpus-invariants.sh` (scaffolding + regressed-pattern scanner), `session-start-worktree-isolation.sh` (SessionStart hook), `reference.docx` (canonical style template). Not session-upload set; run from CLI. See `tools/scripts/README.md` for usage.

### `tools/audits/`

Strategic-snapshot inventories. Distinct from the live `quality-gates/` records + `rigor-passes/` audit trail in that audits here are infrequent one-shot or standing-reference artifacts (cross-chapter consistency inventory; pre-submission readiness audit). Two files as of 2026-05-28 (one is a long-lived standing reference; the other a one-shot 2026-05-01 strategic snapshot). Decided to keep + document per S8 decision 2026-05-28.

### `tools/writing-process/`

Portable / lift-and-reuse process docs (rigor-pipeline-overview, audience-character-roster). Distinct from `drafting-templates/` (project-specific templates) and `pipeline-doctrine/` (project doctrine) in that these are designed to be extractable to standalone references for other writing projects. Three files as of 2026-05-28. Decided to keep + document per S8 decision 2026-05-28.

### `tools/archive/`

Superseded versions of canonical methodology docs (older rigor protocol versions; deprecated test artifacts). Not uploaded; retained for lineage. Most supersession lives in git history; this folder catches the explicit "do not load" cases.

### `tools/routines/`

Operational routine specs — RATIFIED 2026-05-09 routines for cron-scheduled remote agents (currently Routines 1', 2 refined, 3', 4' on unified 6:30am ET cadence). One file as of 2026-05-28. Decided to keep + document per S8 decision 2026-05-28.

---

## Related content outside tools/

These are referenced from `tools/` content but live elsewhere:

| Location | What's there |
|---|---|
| `alignment/patches/` | **Architectural C-patches** (c2 scale-abstract, c3 mechanism-shield, c4 decision-A-sweep, c5 two-path-rigor, c9 AIT-canonical-positioning, tier-2a rename). Referenced by the rigor protocol as source material for specific tests. Not typically uploaded at session start; protocol incorporates their content operationally. |
| `alignment/sessions/` | Session handoffs (current at top level; older in `archive/`). Current handoff is first upload at session start. |
| `alignment/decisions/` | Project-meta decisions — housekeeping reviews, workstreams-superseded mapping, sociology-paper-to-book transition, c6 decision memos. Uploaded on demand when relevant. |
| `core/` | Canonical framework content (eight-tier decomposition, glossary, technical appendix — math-heavy `.html` that stays `.html` per watch items). |
| `manuscript/chapters/` | Chapter drafts + guidance docs. Uploaded on demand when drafting/revising. |
| `research/case-studies/` | Standalone case study files (Appalachian coal, Norway SWF, Libby, Deepwater Horizon, opioid-extraction-Appalachia, 2008-financial-crisis, healthcare-end-of-life, housing-enforced-immobility, tax-tradeoff-US-Sweden). Uploaded on demand. |
| `tools/back-matter/sources/bibliography.md` | Consolidated bibliography with support/contradict annotations. Upload when scholarly engagement is active. |

---

## Copy-paste session-start block

The Drive-era copy-paste block previously documented here (a v1.28.0 handoff + v2.2.0 rigor-protocol upload list) is retired as of 2026-05-31. Current session-start does not use a fixed upload list; the worktree-add command + the relevant kickoff paste-text together constitute the session start. See §"Session-start workflow" above + [`drafting-templates/worktree-isolation-paste-text.md`](drafting-templates/worktree-isolation-paste-text.md) for the canonical first-action paste.

---

## Naming conventions

| Type | Pattern |
|---|---|
| Methodology / handoff / scope | `commons_bonds_{topic}_v#_#_#.md` or `.html` |
| Rigor pass records | `commons_bonds_rigor_pass_YYYY-MM-DD_v#_#_#.md` |
| Triage files | `commons_bonds_{topic}_triage_v#_#_#.md` |
| Architectural patches | `c{N}_{topic}_patch.md` or `{topic}_patch.md` (in `alignment/patches/`) |
| Session handoffs | `commons-bonds-session-handoff-YYYY-MM-DD_v#_#_#.html` (in `alignment/sessions/`) |
| Chapter drafts / guidance | `Chapter_#_Title_Draft.md` / `Chapter_#___GuidanceDoc.md` (in `manuscript/chapters/`) |

Versioned files: `_v#_#_#` suffix; increment rightmost digit per minor update.

---

## Notes for agents working in this folder

- **Worktree-isolation is the first action** — every fresh session creates an isolated worktree under `/Users/c17n/commons-bonds-<workstream-slug>-<harness-id>` BEFORE any other tool call. See [`memory/feedback_worktree_isolation_for_parallel_sessions.md`](memory/feedback_worktree_isolation_for_parallel_sessions.md).
- **Merge-on-ratification is the merge gate** — ratification of an end-user-facing prose change (or session-close for internal scaffolding) IS the authorization to fast-forward `origin/main`. See `CLAUDE.md` §"Branch discipline + merge-to-main" + [`memory/feedback_merge_on_ratification.md`](memory/feedback_merge_on_ratification.md). Escape hatches: `MERGE-HOLD: <reason>` + `MERGE-AFTER: <gate>` commit-message-body markers.
- **Pre-push reconcile before every push** — `git fetch origin main && git rebase origin/main` to inherit any parallel-session work; add a reconciliation commit if a parallel session changed anything load-bearing for the chunk being pushed. Hard constraints (unchanged): never force-push `main`; never amend a commit already on `origin/main`; never skip hooks (`--no-verify`) without explicit author direction.
- **Math files stay `.html`** — never convert `.html` to `.md` for math-heavy content (eight-tier decomposition, technical appendix, error-out, glossary).
- **Privacy rule active** — scrub personal financial specifics from external-facing outputs by default.
- **No invented factual claims** — in publisher-facing non-fiction prose, do NOT invent factual claims about real subjects. See `CLAUDE.md` §"No invented factual claims" + [`memory/feedback_no_invented_factual_claims_in_publisher_facing_prose.md`](memory/feedback_no_invented_factual_claims_in_publisher_facing_prose.md).
