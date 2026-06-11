# AGENTS.md — Internal collaborator orientation

**Layer:** internal scaffolding (per Working Principle #10).
**Audience:** author + AI collaborator + future-Claude.

This is the structural orientation document for the Commons Bonds project — how the repo works conceptually, where to find live operational state, and what disciplines apply when collaborating on the project. Per WP#10, this document lives at the internal-scaffolding layer; the publisher-facing landing page is [`README.md`](README.md). **Refreshed 2026-05-31** per memory-process-review v2 B.4 Config γ ratification — pre-2026-05-31 versions carried a "Current canonical state" table that duplicated (and drifted from) the PM dashboards; that table has been dropped in favor of the pointers below.

## Live operational state lives elsewhere

This document carries structural orientation (working principles, repo layout, key conceptual foundations) but deliberately does NOT carry per-component version numbers, per-essay submission state, per-chapter Stage state, or other operational anchors that drift faster than this document refreshes. For live state, read:

- **[`CLAUDE.md`](CLAUDE.md)** — current discipline (branch + merge-to-main; named-subject consent; no-invented-factual-claims; three-pass rigor; status markers). Loaded automatically into every session.
- **[`tools/workstream-handoffs/pm-session-handoff_<DATE>.md`](tools/workstream-handoffs/)** — latest PM dashboard. Per-essay + per-chapter state, priority-labeled buckets, date-anchored actions, decisions pending.
- **[`tools/memory/README.md`](tools/memory/README.md)** — cross-session discipline registry (3 always-loaded + ~19 situational discipline files).
- **[`tools/conventions/status-markers.md`](tools/conventions/status-markers.md)** — authoritative source for status values, file-header `Status:` markers, commit-message escape hatches (`MERGE-HOLD:` / `MERGE-AFTER:`), per-essay directory tags, PM dashboard emoji conventions, state-transition diagram.
- **[`tools/pipeline-doctrine/`](tools/pipeline-doctrine/)** — canonical six-stage pipeline doctrine + per-stage deep-dives (Stage 1 / 4 / 5). Memory-summary mirror at [`tools/memory/feedback_audience_aware_drafting_discipline.md`](tools/memory/feedback_audience_aware_drafting_discipline.md); portable extracts at [`tools/writing-process/`](tools/writing-process/).
- **[`publishing/essays/README.md`](publishing/essays/README.md)** — current per-essay submission state (snapshot, not live).
- **[`alignment/commons_bonds_open_insights_v1.0.0.md`](alignment/commons_bonds_open_insights_v1.0.0.md)** — open-insights tracker (live).
- **[`alignment/commons_bonds_framework_positioning_disciplines_v1.0.0.md`](alignment/commons_bonds_framework_positioning_disciplines_v1.0.0.md)** — 11 framework-positioning disciplines (FPD-1 through FPD-11) + canonical framework articulations for interview / outreach use.

## Working discipline

Ten working principles (v1.0.0 canonical at [`alignment/commons_bonds_working_principles_v1.0.0.md`](alignment/commons_bonds_working_principles_v1.0.0.md)). Selected, with current extensions:

- **WP#1** Vocabulary parsimony.
- **WP#3** Two-path rigor — allocation symmetry + shield absence; both paths must confirm.
- **WP#4** Retirement-trace discipline — REFINED 2026-04-30 (tiered policy by document type; canonical retirement-archive at [`archive/retirements/index.md`](archive/retirements/index.md)).
- **WP#7** Earning-its-place + scaffolding-vs-book-worthy.
- **WP#8** Publisher-facing artifacts scrubbed of scaffolding.
- **WP#9** NEW 2026-04-29 — worktree-isolation git workflow. Extended 2026-05-26 (parallel-session worktree isolation; first-action discipline enforced via SessionStart hook + kickoff paste-text + [`tools/memory/feedback_worktree_isolation_for_parallel_sessions.md`](tools/memory/feedback_worktree_isolation_for_parallel_sessions.md)). Extended 2026-05-28 (merge-on-ratification: ratification IS the merge authorization for end-user-facing prose, same mechanism as internal scaffolding). Canonical: [`CLAUDE.md`](CLAUDE.md) §"Branch discipline + merge-to-main".
- **WP#10** NEW 2026-04-30 — Two-layer content origination discipline (internal-scaffolding vs external-publisher-facing).

### WP#10 layer classification

| Layer | What lives here | Discipline |
|---|---|---|
| **Internal scaffolding** | `.claude/` · `tools/` · `alignment/methodology/` · `alignment/` · `research/` · `archive/` · this `AGENTS.md` | Rich; preserves methodology, worked examples, audit trail, decision-time-application drafts, Book 2 / Book 3 seed material. Auto-merges to main at session close per `CLAUDE.md` §"Branch discipline + merge-to-main". |
| **External publisher-facing** | `manuscript/chapters/*` · `tools/back-matter/sources/glossary/*` · `manuscript/technical-appendix/*` · `publishing/essays/<venue>/essay.md` · `publishing/op-eds/<slug>/op-ed.md` · `publishing/book-proposal/*` · `README.md` | WP#8 (scrubbed of audit-trail content) + Pattern 2 demonstration (threaded through cases rather than codified in dedicated how-to / methodology sections — the *Doughnut Economics* / *Mission Economy* / *Mine!* model). Auto-merges to main on author ratification (merge-on-ratification 2026-05-28). |

**Default when uncertain:** classify new content as internal scaffolding. Easier to promote internal material to external (when it earns the slot via Pattern 2 demonstration) than to scrub publisher-facing artifacts of accumulated scaffolding.

### Project-phase framing (2026-05-25)

The book is content-complete (all 10 chapters drafted + Tech Appendix + AuthorsNote). Active work is iterative polish (chapter Stage 3 / 4 / 5 cycles) running in parallel with an essay/op-ed marketing strategy aimed at landing an agent + trade-publisher contract. **Essays are downstream marketing instruments, NOT platform-builders writing-the-book-as-they-go.** See [`tools/memory/project_book_complete_marketing_phase.md`](tools/memory/project_book_complete_marketing_phase.md) for the load-bearing reframing rule (Stage 0 dimension reweighting; PARK-as-legitimate-verdict; pre-pub-launch-vs-platform-deepening contingency framing).

## Repository structure

- **[`manuscript/`](manuscript/)** — book content. Ten chapter drafts under `chapters/` (one HTML for math-heavy Ch 6; rest markdown) + 10 GuidanceDocs + dedication + author's note. End-user-facing per WP#10.
- **[`publishing/`](publishing/)** — derivative output. `essays/<venue>-<short-title>/` per-essay submission packages (`essay.md` + `cover-letter.md` + `rigor/` + `editor-iteration/` + `_archive/`); `op-eds/<slug>/` per-op-ed packages; `book-proposal/`; `agents/<agent-slug>/`; `essays/_pipeline/` cross-essay strategy (cascade plan + decisions log + cross-thread-todos + rights register + submission schedule); `op-eds/_pipeline/` op-ed news-peg + submission tracking. End-user-facing per WP#10.
- **`core/` — RETIRED 2026-06-10** (structural-debt closeout). Its contents moved to their natural homes: Technical Appendix → `manuscript/technical-appendix/` (the book is whole under `manuscript/`); glossary + terms_index + bibliography master → `tools/back-matter/sources/` (co-located with the generator); methodology → `alignment/methodology/`; the old chapter/case-study audits → `tools/audits/`. See MAP.md for the live taxonomy.
- **[`research/`](research/)** — `case-studies/`, `literature/` (bibliography), `outreach/` (per-subject folders + `_pipeline/` consent-tracker + interview-outreach-drafts), `story-drafts/` (author substrate dumps).
- **[`alignment/`](alignment/)** — project-meta scaffolding: top-level working principles + vocabulary strategy + framework-positioning-disciplines + open-insights tracker + personal-stories candidates; `decisions/`; `patches/`; `sessions/` (legacy; current operational handoffs live under [`tools/workstream-handoffs/`](tools/workstream-handoffs/)).
- **[`tools/`](tools/)** — canonical working methodology. Subdir inventory at [`tools/README.md`](tools/README.md). Key subdirs: `memory/` (cross-session discipline registry); `conventions/` (status-markers + future cross-cutting conventions); `pipeline-doctrine/` (six-stage doctrine); `drafting-templates/` (class-level templates incl. worktree-isolation paste-text); `workstream-handoffs/` (PM dashboards + per-workstream handoffs + kickoff paste-texts); `rigor-passes/` (cross-essay + chapter-side rigor; per-essay rigor migrated into `publishing/essays/<venue>/rigor/` per 2026-05-28 consolidation pattern); `quality-gates/` (invariant-gate registries + clean baselines); `pre-submission-reviews/` (Stage-5 hand-off artifacts); `memory-updates/` (staging area for memory amendments); `scripts/` (CLI utilities + render toolchain + SessionStart hook); `writing-process/` (portable extracts for lift-and-reuse); `audits/`; `routines/`; `archive/` (superseded methodology versions).
- **[`archive/`](archive/)** — cross-domain retirement material + multi-book seed material: `retirements/index.md` (canonical retirement-trace index per refined WP#4); `decomposition/` (retired 8-tier per Insight #55); `_OneDayMaybe/` (Book 2 / Book 3 / satellite-essay seed material).

### Archive convention (Insight #62 ratified 2026-04-30)

Hybrid structure. Top-level `archive/` carries cross-domain retirement material + multi-book seed material. Per-domain `<domain>/archive/` carries domain-specific historical predecessors kept adjacent to live work (`manuscript/technical-appendix/archive/`, `manuscript/chapters/archive/`, `tools/archive/`, per-essay `_archive/`). Single search location for retirement provenance: [`archive/retirements/index.md`](archive/retirements/index.md). Per-domain archives encode origin context next to live work per WP#10's "internal scaffolding can be rich" license.

## Operating rules

- **Worktree-isolation first action.** Every fresh session creates an isolated worktree at `/Users/c17n/commons-bonds-<workstream-slug>-<harness-id>` BEFORE any other tool call. Canonical: [`tools/memory/feedback_worktree_isolation_for_parallel_sessions.md`](tools/memory/feedback_worktree_isolation_for_parallel_sessions.md) + SessionStart hook at `tools/scripts/session-start-worktree-isolation.sh`.
- **Merge-on-ratification.** Author ratification of end-user-facing prose IS the merge authorization (2026-05-28); internal scaffolding auto-merges at session close (2026-05-24). Escape hatches: `MERGE-HOLD: <reason>` + `MERGE-AFTER: <gate>` commit-message-body markers. Pre-push reconcile (`git fetch origin main && git rebase origin/main`) before every push. Hard constraints: never force-push `main`; never amend a commit already on `origin/main`; never skip hooks (`--no-verify`) without explicit author direction.
- **No invented factual claims** in publisher-facing non-fiction prose — biographical specifics, scene-rendered encounters, period-typical infrastructure details, quoted speech, motivation attributions. Substrate-safe attributions (published-work citations; on-record quotes) ARE permitted. See `CLAUDE.md` §"No invented factual claims".
- **Math files stay `.html`.** Never convert `.html` to `.md` for math-heavy content (Ch 6, Technical Appendix, glossary). The eight-tier decomposition is RETIRED 2026-04-24 + archived 2026-04-30 (Insight #55); replaced by Cᵢ admission via Four Gates per Path F.
- **Privacy.** Scrub personal financial specifics from external-facing outputs.
- **Named-subject consent.** Living-private = named-pending-consent; deceased = named with courtesy-notify; public officials quoted from on-record speech = courtesy-notify-NOT-consent. Places safe. See `CLAUDE.md` §"Named-subject consent" + [`tools/memory/feedback_named_subject_consent.md`](tools/memory/feedback_named_subject_consent.md).
- **`.DS_Store`, `.claude/`, `.chriswinn/` are in `.gitignore`** — never commit.
- **Berggruen Prize 2026 essay text is AI-free** — never modify text under `publishing/essays/berggruen-prize-2026/` essay material.
- **Retirement traces** per refined WP#4: tiered policy by document type; canonical retirement audit-trail at [`archive/retirements/index.md`](archive/retirements/index.md).

## Key conceptual foundations (internal vocabulary)

- **Two-path rigor** — allocation symmetry + shield absence. Both paths must confirm.
- **Merger gate + primitiveness gate** — applied to any new or renamed dimension.
- **Commons Inversion Test (CIT)** — epistemic core; scarcity-grounded cost claims survive counterfactual inversion (CAI / CCI). Operates as a thought-experiment discrimination gate within the Four Gates admission apparatus (Path F per Insight #21 + tier-reframing). Renamed from AIT; replaces 8-tier decomposition discipline.
- **Earning-its-place + Scaffolding-vs-book-worthy** — standing book-integrity tests (Tests 28 + 29) applied at every rigor depth.
- **Canonical cases are dimension-inherent** — not incidental illustrations.
- **Single-dimension cost severance** — one-dimension cases are full instances; framework doesn't require multi-dimension co-occurrence.
- **Path F variables-not-dimensions reframing** — dimensions are organizational scaffolding over variables CIT has surfaced across cases; illustrative, not closed ontological taxonomy.

## Ten dimensions (locked)

Habitability · Spatial · Temporal · Institutional · Kindred · Ecosystem · Political · Cohesion · Epistemic · Autonomy.
