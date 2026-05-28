# tools/ — Canonical Working Methodology

This folder holds the canonical methodology documents for the Commons Bonds project — the set of files uploaded to Claude at the start of each work session.

**Convention:** `tools/` top-level = session upload set. Subfolders = session-upload-adjacent material (recent pass records, triage inputs, superseded versions).

---

## Session-start upload set

For any substantive session work, upload these files plus the current session handoff (from `alignment/sessions/`):

| File | What it does |
|---|---|
| `tools/claude_prefs.md` | Operating preferences, file-format rules, privacy rules, Commons Bonds operating core |
| `tools/commons_bonds_rigor_protocol_v2.2.0.md` | Canonical rigor protocol — **Pre-Submission Peer Review Suite + Path Comparison Mode + 6 Informational Goals**. 11 purpose-driven modules (M1 Framework / M2 Case study / M3 Book content / M4 Craft / M5 Dinner-table / M6 Academic rigor / M7 Originality / M8 Long-term / M9 Risk / M10 Publishing / M11 Critic pressure). Five running modes (single-module / combined / full / light / path comparison). Two output deliverables: PSR (single-state) + PCR (comparative-state). PCR includes 4 primary goals (drive recommendations) + 6 informational goals (produce findings only — personal/ethical satisfaction + family wellbeing + career safety + time/capacity + movement utility + financial sustainability). v1.3.0 + v2.0.0 + v2.1.0 retired (git history preserves; mapping in v2.2.0 §0.2). |
| `tools/commons_bonds_guiding_constraints_v1_0_0.md` | Canonical Group D (strategic / publishing-path) + Group E (success criteria) inputs |
| `core/dimensions/commons_bonds_abundance_dimensions_v1_3_0.md` | Methodology document for the 10 abundance dimensions; **v1.3.0 current** (note: prior v1_2_0 reference was stale; corrected 2026-04-30 per Insight #55 hygiene pass). **Path F reframing applied** — dimensions are organizational scaffolding over variables CIT has surfaced across 18 case studies; not closed ontological taxonomy. **Queued for absorption into Tech Appendix v2.0.0 §C.2 during Phase 3 rebuild; directory will archive at that point per Insight #55 hygiene pass.** Originally promoted to `core/` 2026-04-22 per scaffolding-vs-book-worthy placement principle (parallel to `archive/decomposition/` (formerly `core/decomposition/`; archived 2026-04-30), `core/glossary/`, `core/technical-appendix/`). Naming cohort: Habitability, Spatial, Temporal, Institutional, Kindred, Ecosystem, Political, Cohesion, Epistemic, Autonomy. |
| `tools/commons_bonds_book_scope_v1_0_3.md` | Canonical Book One scope |
| `tools/rigor-passes/commons_bonds_rigor_pass_2026-04-22_v1_0_1.md` | Most recent rigor pass record (Part 2, session v1.28.0) |

Plus the current session handoff from `alignment/sessions/`.

---

## Subfolders

**Updated 2026-05-28** — inventory refreshed to match actual subdir contents; pre-2026-05-28 versions of this section referenced `tools/triage/` (no longer present) and omitted most active subdirs.

### `tools/pipeline-doctrine/`

Canonical pipeline doctrine: four files (v1.0.0 main + Stage 1 / Stage 4 / Stage 5 deep-dives) covering the six-stage architecture, two-class cascade, invariant-gate infrastructure, and cross-chapter workstream lifecycle. Promoted from `tools/` top-level into this subdir 2026-05-28 (S6 of the structure-cleanup-followup session). Index + when-to-read-which guide at [`pipeline-doctrine/README.md`](pipeline-doctrine/README.md).

### `tools/rigor-passes/`

Historical audit trail of rigor passes. ~260+ files spanning Stage 0 → Stage 5 work across chapters + essays. Naming pattern: `commons_bonds_rigor_pass_YYYY-MM-DD_<slug>_<stage>_v#_#_#.md`.

**Migration queue (2026-05-28).** Per-essay rigor consolidation pattern ratified 2026-05-28 (see `publishing/essays/README.md` §Per-essay directory layout). Per-essay rigor artifacts (5 passes + Stage 1 brief + Stage 4 + Stage 5 + pre-pub-review-queue) are migrating into `publishing/essays/<venue>/rigor/` subdirs. After migration, `tools/rigor-passes/` will hold only:
- Cross-essay rigor (e.g., Wave 2 derivative-planning Stage 0 batch covering Ch 2 + Ch 3 + Ch 4 + Ch 8)
- Chapter-side rigor for `manuscript/chapters/Chapter__N_*` (book-side, not essay-side)
- Pre-2026-05-28 historical artifacts retained for lineage

### `tools/workstream-handoffs/`

PM dashboards, per-workstream session handoffs, kick-off paste-texts, cross-essay portfolio reviews, parallel-session inventory snapshots. ~85+ files. Naming patterns: `pm-session-handoff_YYYY-MM-DD.md` (PM dashboards), `<workstream-slug>-handoff_YYYY-MM-DD.md` (workstream handoffs), `<workstream-slug>-paste-text_YYYY-MM-DD.md` (kick-off scaffolds). Index at [`workstream-handoffs/README.md`](workstream-handoffs/README.md).

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

Staging area for memory-discipline updates. New / amended discipline files land here first, then mirror into `tools/memory/` once the in-repo mirror is updated.

### `tools/scripts/`

CLI utilities + supporting binaries: `build-derivatives.sh` (.md / .html → .docx + .pdf), `check-corpus-invariants.sh` (scaffolding + regressed-pattern scanner), `session-start-worktree-isolation.sh` (SessionStart hook), `reference.docx` (canonical style template). Not session-upload set; run from CLI. See `tools/scripts/README.md` for usage.

### `tools/audits/`

Snapshot inventories (cross-chapter consistency, pre-submission readiness). Lower-volume bin distinct from live `quality-gates/` records + `rigor-passes/` audit trail.

### `tools/writing-process/`

Meta-reflection artifacts (rigor-pipeline-overview, drafting-flow notes).

### `tools/drafts/`

Intermediate prose drafts + working-session outputs. Lower-volume; distinct from manuscript / publishing canonical paths.

### `tools/archive/`

Superseded versions of canonical methodology docs (older rigor protocol versions; deprecated test artifacts). Not uploaded; retained for lineage. Most supersession lives in git history; this folder catches the explicit "do not load" cases.

### `tools/routines/`

Operational routine specs (low-volume).

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
| `research/literature/bibliography.md` | Consolidated bibliography with support/contradict annotations. Upload when scholarly engagement is active. |

---

## Copy-paste session-start block (from handoff v1.28.0)

```
Please read these files before responding:
- commons-bonds-session-handoff-2026-04-22_v1_28_0.html
- commons_bonds_rigor_protocol_v2.2.0.md
- commons_bonds_guiding_constraints_v1_0_0.md
- commons_bonds_abundance_dimensions_v1_3_0.md
- commons_bonds_rigor_pass_2026-04-22_v1_0_1.md
```

(Add `claude_prefs.md` and `commons_bonds_book_scope_v1_0_3.md` if they're not already session-implicit context.)

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

- **Math files stay `.html`** — never convert `.html` to `.md` for math-heavy content (eight-tier decomposition, technical appendix, error-out, glossary).
- **Privacy rule active** — scrub personal financial specifics from external-facing outputs by default.
- **Never write to Google Drive.** Drive-specific heredoc truncation risk. Drive uploads are manual on Chris's side.
- **Worktree writes + merges + pushes** are validated workflow as of 2026-04-22 (session v1.28.0). See `claude_prefs.md` §1 for current collaboration rules.
- **Hard rules** — never touch `/Noema/` or `/Berggruen Institute - Essay/` Drive folders; never rename Drive files.
