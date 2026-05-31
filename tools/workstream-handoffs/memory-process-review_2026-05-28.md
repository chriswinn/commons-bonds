# memory-process-review_2026-05-28.md

**Status:** RATIFIED 2026-05-31 — 13 of 14 §5 items ratified in-session via 4-question batch. Decisions: A.4 = D1 (collapse to 3-line pointer); A.8 = KEEP-LOCAL (Out-of-scope flag); B.4.a = Config γ (hybrid AGENTS.md). Batch-ratified as-recommended: A.5, A.6, A.7, A.9, B.1, B.2, B.3, B.4.b, B.6. Declined per recommendation: B.5 (optional CLAUDE.md cross-ref). Option E (A.2) carries forward from v1 mid-session ratification. Execution chip spawning per §7 next.
**Version:** **v2** — fresh-eyes redo per author request 2026-05-28 afternoon. Supersedes v1 (commits `e3b082b` + `c852336` on origin/main). v1 produced first-pass findings + Option E always-load architecture (already ratified by author mid-session). v2 expands on v1 with findings missed on first pass: (a) **laptop MEMORY.md vs in-repo mirror drift**, (b) **AGENTS.md vs PM-dashboard "primary home for PM state" conflict** (S5 still DOC-pending per PM handoff), (c) **`tools/writing-process/`** portable-extracts folder, (d) **V-D audit cluster** flag, (e) **alignment with the broader project-review G/S items** still pending from `tools/workstream-handoffs/pm-session-handoff_2026-05-28.md`. Option E (always-load recalibration) from v1 is preserved as the load-bearing recommendation; v2 adds rather than replaces.
**Workstream:** `claude/memory-process-review-260528-67ca7b`
**Author kickoff:** "fresh CC session doing a reflective review of the commons-bonds project's memory + process documents, looking for streamlining + pruning opportunities. Author requested this as a follow-up to the 2026-05-28 process + structure changes ratified by the PM session at `tools/workstream-handoffs/pm-session-handoff_2026-05-28.md`."
**Author redo prompt 2026-05-28 afternoon:** "update branch; then redo your investigation + report + recommendations."
**Method:** Phase A (memory layer review via 3 parallel Explore sub-agents in v1; verified in v2 — files unchanged since v1) + Phase B (process documents drift scan; expanded in v2 with PM-handoff context + `tools/writing-process/` discovery + AGENTS.md ↔ PM-dashboard conflict articulation) + Phase A.2 (NEW in v2 — laptop MEMORY.md vs in-repo mirror drift) + Phase C (synthesis + recommendation report — this file).
**Mode:** read-then-recommend. DO NOT prune until author ratifies. Pruning execution is a separate follow-up chip.
**Branch state:** rebased onto current `origin/main` 2026-05-28 afternoon; 65+ parallel-session commits intervened (all V-D essay audits + Berggruen scaffold + Atlantic Ideas Stage 5 consolidation); **none of those commits touched the memory + process layer**, so v1's per-file analysis remains valid; v2 expands scope rather than re-analyzing the same files.

---

## §0. Top-of-mind takeaway (TL;DR v2)

The memory + process layer is **substantively healthy** (23 in-repo entries; clean index; clear cross-linking) but has accumulated five identifiable inefficiencies. The first three are carried forward from v1; the last two are new findings from the v2 fresh-eyes pass.

1. **The `no-invented-factual-claims` rule (2026-05-28) is the only newcomer not yet captured in always-loaded context.** Add a ~5-sentence CLAUDE.md paragraph capturing the hard rule (~1KB); full memory file stays situational. (**Option E**; v1 finding; author ratified mid-session.) The other two newcomers (`merge-on-ratification`, `worktree-isolation`) are already covered at always-load layer (CLAUDE.md §"Branch discipline") or harness layer (SessionStart hook + drafting-templates first-action discipline). [§3]

2. **`feedback_git_workflow.md` (2026-04-29) is now substantively superseded.** Its `.claude/worktrees/<session-name>` pattern was superseded 2026-05-26 by parallel-session worktrees; its session-end-merge cadence was superseded 2026-05-28 by merge-on-ratification. Disposition: **collapse to 3-line pointer (Option D1) OR archive entirely (Option D2)**. Recommended: D1. [§1.3 Rec D]

3. **AGENTS.md has substantial drift + an unresolved structural question.** Table dated 2026-05-06/17; no mention of merge-on-ratification, status-markers, workstream-handoffs/ system, or 2026-05-25 marketing-phase reframing. **NEW IN V2:** the AGENTS.md vs `tools/workstream-handoffs/pm-session-handoff_<DATE>.md` conflict for "primary home for PM state" is **S5 (MED) still DOC-pending per `pm-session-handoff_2026-05-28.md`** — my v1 recommendation to "substantially refresh AGENTS.md" did not acknowledge this. Refresh-vs-radically-slim is a decision the author should make, not a foregone refresh. [§2.3 v2 revised]

4. **NEW IN V2 — Laptop MEMORY.md vs in-repo `tools/memory/README.md` drift.** Three entries on in-repo are missing from laptop index (the three 2026-05-24-to-28 newcomers); one entry on laptop is missing from in-repo (`project_chapter_draft_suffix_consent_marker.md`, 2026-05-18); one description on laptop is stale (audience-aware-drafting v2.0 → actual v3.1). This is a recurring drift class — the laptop index lags repo amendments by ~1-2 weeks. Recommend: **mirror the 3 newcomers to laptop; either mirror the `__Draft suffix` entry to in-repo OR mark it KEEP-LOCAL in tools/memory/README.md "Out of scope" section**. [§1.5 NEW]

5. **NEW IN V2 — `tools/writing-process/` portable-extracts folder (2026-05-19) is a third home for pipeline content** alongside `tools/pipeline-doctrine/` (project-specific) and `feedback_audience_aware_drafting_discipline.md` (always-load summary). Three documents (rigor-pipeline-overview, audience-character-roster, planned interview-prep-process). Not a drift problem — the three layers serve distinct audiences (portable extract / project doctrine / always-load summary) — but worth flagging in §2 so future amendments to the v3.1 doctrine don't drift across the three locations. [§2.4 NEW]

The 19 other memory files are well-calibrated, currently load-bearing, and need only minor amendments. The §4 sequenced execution plan + §5 author-action menu reflect v2's expanded scope.

---

## §1. Phase A — Memory layer review

### §1.1 Summary table — 23 in-repo memory files

(Unchanged from v1; files were not touched by the 65 parallel-session commits between v1 and v2.)

| # | File | Type | Ratified | Status | Recommended disposition |
|---|---|---|---|---|---|
| 1 | feedback_audience_aware_drafting_discipline.md | always-load | v3.1 (2026-05-18) | current | **keep-as-is** |
| 2 | feedback_named_subject_consent.md | always-load | 2026-05-09 + 05-12 + 05-20 | current | **keep-as-is** |
| 3 | feedback_verify_stale_memory_claims.md | always-load | 2026-05-10 | current | **keep-as-is** |
| 4 | feedback_merge_on_ratification.md | situational | 2026-05-28 | current (NEW) | **keep situational** (Option E; CLAUDE.md §Branch discipline already canonicalizes) |
| 5 | feedback_no_invented_factual_claims_in_publisher_facing_prose.md | situational | 2026-05-28 | current (NEW) | **add ~5-sentence CLAUDE.md paragraph; full file stays situational** (Option E) |
| 6 | feedback_worktree_isolation_for_parallel_sessions.md | situational | 2026-05-26 | current (NEW) | **keep situational** (Option E; SessionStart hook + kickoff paste-text already enforce) |
| 7 | feedback_parallel_session_ratification_cadence.md | situational | 2026-05-24 | current | **keep-as-is** (situational is right) |
| 8 | feedback_git_workflow.md | situational | 2026-04-29 (+ 05-10, 05-24, 05-25 extensions) | partially superseded | **major amendment OR archive** [Option D1 or D2] |
| 9 | feedback_two_layer_content_discipline.md | situational | 2026-04-30 (WP#10) | current | **keep-as-is** |
| 10 | feedback_audit_recent_active_review_default.md | situational | 2026-05-12 | current | **keep-as-is** |
| 11 | feedback_audit_open_illustrative_default.md | situational | 2026-05-12 | current | **keep-as-is** |
| 12 | feedback_pm_dashboard_structure.md | situational | 2026-05-13 | minor drift | **minor amendment** (line 44 → status-markers.md; add Class-column note) |
| 13 | feedback_rigor_vs_bookkeeping_distinction.md | situational | 2026-05-27 | current | **keep-as-is** |
| 14 | feedback_substrate_critical_editorial_input.md | situational | 2026-05-21 | current | **keep-as-is** |
| 15 | feedback_em_dash_overuse.md | situational | 2026-05-21 | current | **keep-as-is** |
| 16 | feedback_dual_audience_test.md | situational | 2026-05-11 | current | **keep-as-is** |
| 17 | feedback_grammatical_role_cross_references.md | situational | 2026-05-11 | current | **keep-as-is** |
| 18 | feedback_substance_drives_length.md | situational | 2026-05-02 | current | **keep-as-is** (one stale chapter-status anecdote does not affect rule) |
| 19 | feedback_voice_polish_pipeline.md | situational | 2026-05-04 | current | **keep-as-is** |
| 20 | reference_ostrom_illustrative_register.md | situational | 2026-05-02 | current | **keep-as-is** (verify Cᵢ list before audit-side use) |
| 21 | reference_pattern_2_register.md | situational | (Insight-anchored, pre-2026-05-01) | current | **keep-as-is** |
| 22 | reference_sandel_hybrid_pattern.md | situational | 2026-05-11 | current | **keep-as-is** |
| 23 | project_book_complete_marketing_phase.md | situational | 2026-05-25 | mostly-current with stale operational anchors | **minor amendment** (split phase-reframing rule from operational status claims) |

### §1.2 ARCHIVE.md candidate ranking

Bar for archival: fully-resolved AND no longer informing current practice.

| Rank | Candidate | Rationale | Disposition |
|---|---|---|---|
| 1 | `feedback_git_workflow.md` | The 2026-04-29 `.claude/worktrees/<session-name>` pattern + session-end-merge cadence are both superseded (2026-05-26 worktree-isolation; 2026-05-28 merge-on-ratification). The 2026-05-24 internal-scaffolding extension + 2026-05-25 path update lived inside this file but are now codified in CLAUDE.md + `feedback_merge_on_ratification.md`. The file no longer adds load-bearing content vs the canonical CLAUDE.md section. | **Archive (Option D2) OR collapse to 3-line pointer (Option D1)** |
| — | (none others rank high enough) | All other 22 memory entries remain operationally live in some form. | — |

**Discipline reminder:** ARCHIVE.md is the safe disposal target. Do NOT delete a memory file — archive it (move the entry into `ARCHIVE.md` with a one-paragraph retirement rationale, then delete the source file). The 2026-05-17 `project_book1_state_2026-05-10.md` ARCHIVE.md entry is the format precedent.

### §1.3 Per-file justification for the four headline recommendations (carried from v1)

#### Rec A — keep `feedback_merge_on_ratification.md` situational (per Option E)

CLAUDE.md §"Branch discipline + merge-to-main" already canonicalizes the rule at always-load level. The memory file is the empirical-anchor + escape-hatch-syntax + worked-examples deep reference; loaded situationally when a session wants to litigate the rule. Promoting full file to always-load adds ~7.5KB for content already covered by CLAUDE.md. **Keep situational.**

#### Rec B — add CLAUDE.md prose paragraph for `feedback_no_invented_factual_claims_in_publisher_facing_prose.md` (full file stays situational, per Option E)

Hard rule. Reputational asymmetry: shipped-with-fabrication propagates essay → book → future work. Ch 2 → Harper's Pass 3.5 near-miss + Pass 3.1 F-3.1-H1 empirical anchors demonstrate that at high parallelism, sub-agents WILL produce invented testimonial-register prose at HIGH confidence with substrate-critical flags unless the discipline is in the always-loaded context. Unlike Rec A + Rec C, this rule has **no CLAUDE.md analog + no harness-layer mechanism**. The ~5-sentence CLAUDE.md prose paragraph (drafted at §3.0.2) is the always-load form; the full 17KB memory file is the situational deep reference (9-case "how to apply" detail; Ch 2 Harper's anchors; Pass 3.1 precedent). **Net always-load delta: ~1KB.**

#### Rec C — keep `feedback_worktree_isolation_for_parallel_sessions.md` situational (per Option E)

Three operational layers already enforce the discipline:
1. **SessionStart hook** (`tools/scripts/session-start-worktree-isolation.sh`) fires automatically on every fresh session; emits warning if session starts in main cwd.
2. **First-action paste-text** (`tools/drafting-templates/worktree-isolation-paste-text.md`) is embedded in every kickoff template per `tools/drafting-templates/README.md` line referencing "FIRST ACTION REQUIREMENT (2026-05-26)".
3. **Memory file** is the cross-session discipline pointer (situational).

Promoting the memory file to always-load is belt-and-suspenders-and-a-third-belt. The first two layers operate before context window assembly + at template-paste time; the situational memory load handles the deep-reference case. **Keep situational.**

#### Rec D — Major-amendment (or archive) `feedback_git_workflow.md` (Option D1 or D2)

The file is heavily superseded (per §1.2 ranking). Two options:

- **Option D1 (recommended): collapse to a 3-line pointer.** Replace lines 10-30 with: "Canonical content moved to CLAUDE.md §'Branch discipline + merge-to-main' (2026-05-28 merge-on-ratification rule). Worktree-isolation pattern at [`feedback_worktree_isolation_for_parallel_sessions.md`](feedback_worktree_isolation_for_parallel_sessions.md). This file retained for historical reference to the 2026-04-29 ratification of WP#9 + the iCloud-incident empirical anchor."
- **Option D2: archive entirely.** Add an entry to ARCHIVE.md noting the supersession; delete the source file. Cleaner but loses the iCloud-incident historical anchor.

Recommendation: **D1**. Aligns with PM-handoff S3 (HIGH) "Move superseded files to `_archive/`" if author prefers D2.

### §1.4 Minor-amendment cases (carried from v1)

- **`feedback_pm_dashboard_structure.md`**: Add a sentence after line 44 pointing to `tools/conventions/status-markers.md` as the authoritative source for emoji + status-marker conventions. Optional addition: a "Class column recommendation" note pointing to `feedback_rigor_vs_bookkeeping_distinction.md` for PM dashboards that need rigor-vs-bookkeeping discrimination.

- **`project_book_complete_marketing_phase.md`**: Split the phase-reframing rule (load-bearing; foundational to cascade plan + venue strategy) from the operational status claims (which chapters in which stage; cascade-plan version; Q2-Q3 2027 timing). The phase-reframing should remain in the memory; the operational status should either (a) be removed (stale-prone) or (b) be marked as "verify against current state before quoting." Recommend (a).

### §1.5 NEW IN V2 — Laptop MEMORY.md vs in-repo `tools/memory/README.md` drift

Comparison performed against the laptop MEMORY.md content auto-loaded at session start (`~/.claude/projects/-Users-c17n-commons-bonds/memory/MEMORY.md`) vs the in-repo `tools/memory/README.md`.

**In-repo perfect sync:** 23 README entries ↔ 23 actual files in `tools/memory/`. No mismatch.

**Laptop ↔ in-repo drift:**

| Drift | Direction | Detail | Recommended fix |
|---|---|---|---|
| D-L1 | In-repo → laptop missing | `feedback_merge_on_ratification.md` (2026-05-28) not yet in laptop index. | Mirror to laptop on next sync. |
| D-L2 | In-repo → laptop missing | `feedback_worktree_isolation_for_parallel_sessions.md` (2026-05-26) not yet in laptop index. | Mirror to laptop on next sync. |
| D-L3 | In-repo → laptop missing | `feedback_parallel_session_ratification_cadence.md` (2026-05-24) not yet in laptop index. | Mirror to laptop on next sync. |
| D-L4 | Laptop → in-repo missing | `project_chapter_draft_suffix_consent_marker.md` (laptop entry; "__Draft suffix on chapter filenames = consent-pending marker; author flagged 2026-05-18"). NOT in tools/memory/. NOT flagged KEEP-LOCAL in tools/memory/README.md "Out of scope" section. | **Author decision:** either mirror to in-repo (treat as discipline that should be cross-session-load-bearing), OR mark KEEP-LOCAL in tools/memory/README.md Out-of-scope section + add note to laptop entry. |
| D-L5 | Description staleness on laptop | `feedback_audience_aware_drafting_discipline.md` described on laptop as "Two-stage audience-aware drafting discipline (v2.0)". Actual file is v3.1 (Amendments A + B ratified 2026-05-18). | Refresh laptop description on next sync. Could automate via `tools/memory-updates/` spec discipline. |

**Pattern.** The laptop index lags in-repo amendments by ~1-2 weeks. The `tools/memory-updates/` staging area exists to mediate this (per S8 decision 2026-05-28 keep documented in `tools/README.md`) but is not running as a regular sync routine. The 3 newcomers in D-L1/L2/L3 have been ratified for 4 days, 2 days, and the same day respectively — laptop drift is recoverable on next manual sync.

**Recommended sync routine.** Spawn a periodic (~weekly?) "memory sync" chip that:
1. Diffs laptop MEMORY.md vs in-repo `tools/memory/README.md`.
2. Mirrors new in-repo entries into laptop.
3. Mirrors version/description updates into laptop.
4. Flags laptop-only entries as either KEEP-LOCAL (in-repo Out-of-scope) or mirror-to-in-repo (depending on author decision).

Or fold this into the existing `tools/memory-updates/` staging discipline by adding a "laptop sync verification" step.

---

## §2. Phase B — Process documents drift scan (expanded in v2)

### §2.1 Drift table (carried from v1 + expanded)

| Document | Current state | Drift assessment | Recommended disposition |
|---|---|---|---|
| `CLAUDE.md` | 207 lines; refreshed 2026-05-28 for merge-on-ratification + status-markers section + per-essay rigor consolidation note. | **Current.** | **Keep-as-is + add §"No invented factual claims" section per Option E §3.0.2.** |
| `AGENTS.md` | 168 lines; "Current canonical state" table dated 2026-05-06/07/09/17. | **Substantially drifted + S5 unresolved (NEW IN V2).** Drift specifics: no mention of merge-on-ratification, status-markers, workstream-handoffs/ system, marketing-phase reframing. Open-insights tracker says "7 OPEN as of 2026-05-17" (11 days stale). Outreach pipeline cell dated 2026-05-05. Aeon essay cell dated 2026-05-04. "Current handoff" cell references `v1.52.0` (old `alignment/sessions/` system). "Session workflow" section (lines 135-144) references obsolete upload-set workflow. "What's queued" section (lines 115-133) is dated 2026-05-06. **PM-handoff S5 (MED) still DOC-pending:** "Pick primary home for PM state — discussion-required." AGENTS.md and the `tools/workstream-handoffs/pm-session-handoff_<DATE>.md` PM dashboard both claim canonical-state-of-project role; they're redundant + drift-prone (PM dashboards refresh ~weekly; AGENTS.md has not been comprehensively refreshed in ~3 weeks). | **Decision-then-disposition — see §2.3 v2 revised.** |
| `tools/README.md` | 156 lines; refreshed 2026-05-28 for subfolders inventory; "Session-start upload set" sections retained from earlier era. | **Partially drifted.** Subfolders inventory (lines 28-101) is current. Session-start upload set (lines 11-22) + copy-paste session-start block (lines 121-131) + "Notes for agents" (lines 152-156) are stale — they reference `alignment/sessions/` handoffs, v2.2.0 rigor protocol upload set, `/Noema/` and `/Berggruen Institute - Essay/` Drive folders (Drive-era; not current). | **Minor amendment** — strip or refresh the upload-set sections; explicitly note current session start = worktree-isolation first, paste-text kickoff per `tools/drafting-templates/`. |
| `tools/pipeline-doctrine/README.md` | 36 lines; created 2026-05-28 as part of S6. | **Current.** | **Keep-as-is.** |
| `tools/conventions/status-markers.md` | 150 lines; codified 2026-05-28 as part of S7. | **Current.** | **Keep-as-is.** |
| `tools/conventions/` (directory) | Holds only `status-markers.md`. Bare-minimum directory. | **Not a drift problem; observation:** could be a home for future cross-cutting conventions (commit-message conventions; review-cadence conventions; etc.) as they get codified. | **Keep-as-is.** Use as a deliberate home for future convention codifications. |
| `tools/workstream-handoffs/README.md` | 122 lines; last refreshed 2026-05-28 for merge-on-ratification at line 11. | **Partial drift.** Lines 11 are current. Lines 17-83 list workstream handoffs by date through 2026-05-18; the branch-prefix conventions (`claude/aeon-submission-`, `claude/boston-review-essay-`, etc.) are stale — actual current branches use `claude/<workstream>-<harness-id>` with auto-generated harness IDs per worktree-isolation discipline. PM-handoff G2 (HIGH) "Require deliberate workstream slugs — DOC pending" overlaps with this; the branch-prefix convention REFRESH should also resolve G2. | **Minor amendment** — remove or restructure branch-prefix column; add paragraph noting current `claude/<workstream>-<harness-id>` format per `feedback_worktree_isolation_for_parallel_sessions.md`; this commit also resolves G2 documentation. |
| `publishing/essays/README.md` | 123 lines; refreshed 2026-05-28 for `rigor/` + `editor-iteration/` + `_archive/pre-submission/` subdirs. | **Mostly current.** "Active essay packages (as of 2026-05-25)" table is 3 days stale — Atlantic Ideas pitch ratified 2026-05-28; verify Aeon timing. | **Minor amendment** — refresh table to 2026-05-28 state. |
| `tools/drafting-templates/README.md` | 50+ lines; refreshed 2026-05-24 (v3.1 doctrine reflected). | **Current.** Already references worktree-isolation paste-text + SessionStart hook + the memory file as defense-in-depth (NEW IN V2: this validates Option E architecture; the three-layer enforcement is already operational). | **Keep-as-is.** |
| `tools/writing-process/README.md` | NEW V2 OBSERVATION; created 2026-05-19. Holds portable / lift-and-reuse process docs (rigor-pipeline-overview v1.0.0, audience-character-roster v1.0.0, planned interview-prep-process). | **Not drifted; observation.** Three-home structure: (a) `feedback_audience_aware_drafting_discipline.md` (always-load summary); (b) `tools/pipeline-doctrine/` (project-specific full doctrine); (c) `tools/writing-process/` (portable extracts for lift-and-reuse). Three distinct audiences justify three homes. **Drift risk:** future amendments to v3.1 doctrine could land in only one or two of the three locations. | **Keep-as-is + flag.** Add an explicit cross-reference paragraph in the v3.1 always-load memory summary noting all three homes exist + naming them. Any future doctrine amendment session should update all three. |
| `tools/quality-gates/README.md` | Current. Holds invariant-gate registries + sign-off artifact subdirs. | **Current.** Not pertinent to memory pruning. | **Keep-as-is.** |

### §2.2 Recommended CLAUDE.md addition

The Option E paragraph from v1 §3.0.2. **Retained verbatim:**

```markdown
### No invented factual claims

In publisher-facing non-fiction prose (book chapters, derivative essays,
op-eds, cover letters, query letters, agent correspondence, AI-disclosure
paragraphs, Stage 5 sign-offs), do NOT invent factual claims about real
subjects — biographical specifics, scene-rendered encounters, period-typical
civic-infrastructure detail, quoted speech, documentary-record specifics,
motivation attributions. Substrate-safe attributions ARE permitted
(verifiable published-work citations; on-record quotes). For restoration
recommendations needing substrate the canonical-facts inventory doesn't
anchor, surface the structure-only recommendation; do not generate
illustrative invented prose, even with `[Substrate-critical note: ...]`
flags. The single exception is explicit thought-experiment register
signaled to the reader in the prose itself (Ch 7 *On Other Worlds* model).
Sub-agent kickoff paste-texts must specify this discipline explicitly;
parent-session ratify-as-recommended defaults are conditional on
substrate-safety. Hard rule — reputational asymmetry: shipped-with-
fabrication propagates from essay to book to future work and is not
recoverable. See [`tools/memory/feedback_no_invented_factual_claims_in_publisher_facing_prose.md`](tools/memory/feedback_no_invented_factual_claims_in_publisher_facing_prose.md)
for empirical anchors (Ch 2 → Harper's Pass 3.5 near-miss 2026-05-27;
Pass 3.1 F-3.1-H1 invented Bailey biographical specifics) + 9-case
"how to apply" detail + sub-agent design discipline.
```

~205 words / ~1.4KB. Insertion point: after CLAUDE.md §"Named-subject consent" (lines 181-188), as a new §"No invented factual claims" section.

### §2.3 AGENTS.md disposition — REVISED IN V2 ("decision-then-refresh" framing)

**v1 framing was wrong.** v1 recommended "substantial refresh" as Option 1 (the default) without acknowledging that the AGENTS.md ↔ workstream-handoffs/ PM-dashboard tension is **S5 (MED) still DOC-pending per `tools/workstream-handoffs/pm-session-handoff_2026-05-28.md`**.

**v2 framing.** The disposition is a two-step:

**Step 1 — decide the structural question (S5 resolution).** Three configurations:

- **Config α — AGENTS.md retains canonical-state-of-project role.** Workstream-handoffs/ PM dashboards become operational state-of-week snapshots; AGENTS.md is refreshed to reflect substantive project state. AGENTS.md needs substantial refresh (~30-60 min) on a regular cadence (~weekly?).
- **Config β — workstream-handoffs/ PM dashboards become primary; AGENTS.md radically slims to a pointer + repo-structure-orientation doc.** AGENTS.md "Current canonical state" table collapses to ~5 rows of authoritative-source pointers; the rest becomes either workstream-handoffs/ entries or moves to `tools/conventions/` / `tools/pipeline-doctrine/` / `tools/memory/`. AGENTS.md becomes ~30 lines instead of 168.
- **Config γ — hybrid: AGENTS.md holds STRUCTURAL orientation (repo structure, working principles, working-discipline conceptual foundations) but DROPS operational state.** "Current canonical state" table goes away entirely; PM dashboards own operational state; AGENTS.md owns "how this repo works conceptually." AGENTS.md becomes ~80-100 lines.

**Recommendation: Config γ.** It cleanest-resolves the redundancy without losing the structural-orientation function (which workstream-handoffs/ dashboards do NOT cover). Config α perpetuates the dual-source-of-truth + drift problem. Config β risks losing structural orientation altogether.

**Step 2 — execute the refresh per chosen config.** Once author rules on α/β/γ, the actual AGENTS.md edit is mechanical:
- α: substantial refresh (v1 plan)
- β: radical slim
- γ: drop "Current canonical state" table; keep working-discipline + repo-structure + key-conceptual-foundations sections; refresh those to 2026-05-28 reality

Estimated effort: α = 60-90 min, β = 20-30 min, γ = 30-45 min.

**Coordination note.** PM-handoff S5 lists this as "DOC pending; discussion-required" — author has not yet ruled. v2 surfaces the decision; this review does NOT presume to make it. Suggest spawn a dedicated S5-decision chip OR fold the decision into the next PM session.

### §2.4 NEW IN V2 — `tools/writing-process/` three-home pipeline observation

**Three homes for the v3.1 audience-aware drafting pipeline content:**

| Home | Audience | Granularity | When refresh |
|---|---|---|---|
| `tools/memory/feedback_audience_aware_drafting_discipline.md` (always-load) | Every CC session | Scan-friendly summary (~18KB) | When the doctrine itself amends |
| `tools/pipeline-doctrine/` (subdir; 4 files) | Sessions executing the pipeline | Full canonical doctrine + per-stage deep-dives (~90KB total) | When the doctrine itself amends |
| `tools/writing-process/` (3 docs incl. 1 planned) | External readers + future projects | Portable extracts; project-specific examples generalized; lift-and-reuse-ready | When portable form needs refresh (lags doctrine amendments) |

**This is not a drift problem; it's deliberate architecture.** Three distinct audiences justify three homes. The drift RISK is that a future doctrine amendment (e.g., Amendment D, Amendment E) lands in `tools/pipeline-doctrine/` + the memory file but is forgotten in `tools/writing-process/` extracts.

**Mitigation.** Add an explicit cross-reference paragraph in the v3.1 always-load memory summary noting all three homes exist, naming them, and stating that any future doctrine amendment session should update all three. Low-effort safeguard against three-way drift.

---

## §3. Phase C — Always-load set recalibration (Option E — carried from v1; verified under v2 fresh-eyes pass)

**Author already ratified Option E mid-session via AskUserQuestion 2026-05-28.** v2 verifies under fresh-eyes pass: Option E architecture holds.

### §3.0.1 Revised always-load architecture (Option E)

**Current always-load (unchanged):**
- `feedback_audience_aware_drafting_discipline.md` (v3.1; ~18KB)
- `feedback_named_subject_consent.md` (~5.6KB)
- `feedback_verify_stale_memory_claims.md` (~2.5KB)

**Net change:** No file promotions. **Add a ~5-sentence paragraph to CLAUDE.md** capturing the no-invented-factual-claims hard rule (§2.2 above; ~1KB). Full memory file stays situational.

**Net always-load delta: ~1KB instead of ~40KB.**

| Discipline | Where it's covered |
|---|---|
| Merge-on-ratification | CLAUDE.md §"Branch discipline + merge-to-main" (always-load); memory file at `tools/memory/feedback_merge_on_ratification.md` supplementary |
| Worktree isolation | SessionStart hook + drafting-templates first-action paste-text discipline + status-markers.md cross-refs; memory file deep-dive |
| No-invented-factual-claims | **Gap until Option E lands.** Add CLAUDE.md paragraph (§2.2); memory file stays situational. |

### §3.0.2 V2 verification under fresh-eyes pass

Reading `tools/drafting-templates/README.md` (which I did NOT read on v1's first pass) explicitly confirms the worktree-isolation three-layer enforcement: SessionStart hook + first-action paste-text + memory-file deep-dive. Quoting:

> **FIRST ACTION REQUIREMENT (2026-05-26).** Every fresh session embeds the worktree-isolation paste-text at [`worktree-isolation-paste-text.md`](worktree-isolation-paste-text.md) as its first instruction — BEFORE the required-reads, BEFORE workstream-specific guidance. The session's first tool call MUST be the `git worktree add` step described in that paste-text. Defense-in-depth: a SessionStart hook at [`../scripts/session-start-worktree-isolation.sh`](../scripts/session-start-worktree-isolation.sh) also emits a session-context warning when a session starts in the main `/Users/c17n/commons-bonds` cwd. The hook + the embedded first-action block together prevent the branch-contamination failure mode documented at [`../memory/feedback_worktree_isolation_for_parallel_sessions.md`](../memory/feedback_worktree_isolation_for_parallel_sessions.md).

The drafting-templates README explicitly names the memory file as the THIRD defense layer (not the first). Promoting the memory file to always-load would belt-and-suspenders the third layer, leaving the first two layers (which do the enforcement work) untouched. **Option E architecture is the correct one.**

---

## §4. Pruning execution plan (sequenced) — v2 revised

Per Option E (always-load architecture) + v2 additions (laptop sync; AGENTS.md decision-then-refresh).

If author ratifies the recommended dispositions, execute in this strict order:

1. **Add CLAUDE.md §"No invented factual claims" section** (~205 words per §2.2). No `@import` changes. One commit. Pre-push reconcile + push (internal scaffolding; auto-merge per merge-on-ratification).
2. **Amend `feedback_pm_dashboard_structure.md`** (line 44 → status-markers.md pointer + Class-column note). One commit.
3. **Amend `project_book_complete_marketing_phase.md`** (split phase-reframing from operational status). One commit.
4. **Major-amendment OR archive `feedback_git_workflow.md`** (Option D1 collapse-to-pointer OR Option D2 archive entirely). One commit. If archived (D2), add ARCHIVE.md entry in same commit.
5. **Update `tools/memory/README.md`** index: confirm always-loads remain 3; update disposition of `feedback_git_workflow.md`; optionally add note that `feedback_no_invented_factual_claims_in_publisher_facing_prose.md` rule is also captured in CLAUDE.md §"No invented factual claims" as short-form always-load. **NEW v2:** if D-L4 disposition is "mark KEEP-LOCAL", add `project_chapter_draft_suffix_consent_marker.md` to the Out-of-scope section. One commit.
6. **Refresh `tools/README.md`** session-start sections (lines 11-22 + 121-131 + 152-156). One commit.
7. **Refresh `tools/workstream-handoffs/README.md`** branch-prefix conventions + add `claude/<workstream>-<harness-id>` format paragraph. This commit also documents PM-handoff G2 (HIGH) "Require deliberate workstream slugs" resolution. One commit.
8. **Refresh `publishing/essays/README.md`** Active essay packages table. One commit.
9. **AGENTS.md disposition (NEW V2 — two-step):**
   - **9a.** Surface S5 decision-question to author OR fold into next PM session. (No commit; author action.)
   - **9b.** After α/β/γ ruling: execute the refresh per chosen config. One commit.
10. **NEW V2 — Laptop MEMORY.md sync.** (No commit; laptop-only.) Mirror D-L1/L2/L3 newcomers; refresh D-L5 description; resolve D-L4 per author decision.
11. **NEW V2 — `tools/writing-process/` three-home cross-reference.** Add ~3-sentence cross-reference paragraph in `feedback_audience_aware_drafting_discipline.md` noting the three homes + the all-three-update discipline. One commit.

**Strict ordering rationale:**
- Step 1 (CLAUDE.md addition) lands first because subsequent memory amendments may want to verify the always-load set is updated.
- Step 4 (git_workflow disposition) before step 5 (README index update) because the index reflects the disposition.
- Step 9 (AGENTS.md) is conditional on S5 decision — pause if author hasn't ruled.
- Step 10 (laptop sync) is independent of in-repo commits; can fire anytime.
- Step 11 (three-home cross-reference) is small; can batch with step 5.

**Estimated total effort:** ~2-3 hours if AGENTS.md goes Config α (substantial refresh); ~1.5-2 hours if Config γ (hybrid); ~1-1.5 hours if Config β (radical slim).

---

## §5. Author-action menu (per-recommendation disposition) — v2 expanded

Author can ratify per-recommendation OR batch-ratify all.

**Ratification log 2026-05-31 batch:**

**Memory layer (Phase A):**

- ✓ **A.2** RATIFIED mid-session (v1 Option E). Add ~5-sentence CLAUDE.md §"No invented factual claims" section per §2.2.
- ✓ **A.4** RATIFIED — **Option D1** (collapse to 3-line pointer; preserve iCloud-incident historical anchor).
- ✓ **A.5** RATIFIED — minor amendment to `feedback_pm_dashboard_structure.md` (line 44 → status-markers.md; Class-column note) as-recommended.
- ✓ **A.6** RATIFIED — minor amendment to `project_book_complete_marketing_phase.md` (split phase-reframing from operational status; remove stale operational anchors) as-recommended.

**Laptop / in-repo mirror (NEW IN V2):**

- ✓ **A.7** RATIFIED — sync laptop MEMORY.md (mirror D-L1 + D-L2 + D-L3 + D-L5) as-recommended. Laptop-only; no commit.
- ✓ **A.8** RATIFIED — **mark KEEP-LOCAL** in tools/memory/README.md Out-of-scope section.
- ✓ **A.9** RATIFIED — fold periodic memory-sync verification into `tools/memory-updates/` discipline (no new chip; existing staging discipline owns).

**Process documents (Phase B):**

- ✓ **B.1** RATIFIED — refresh `tools/README.md` session-start sections (lines 11-22 + 121-131 + 152-156) to current discipline.
- ✓ **B.2** RATIFIED — refresh `tools/workstream-handoffs/README.md` branch-prefix conventions to `claude/<workstream>-<harness-id>` format. Commit ALSO documents PM-handoff G2 resolution.
- ✓ **B.3** RATIFIED — refresh `publishing/essays/README.md` Active essay packages table to current 2026-05-31+ state.
- ✓ **B.4.a** RATIFIED — **Config γ** (hybrid: drop "Current canonical state" table; keep working-discipline + repo-structure + key-conceptual-foundations sections; refresh to current state; target ~80-100 lines).
- ✓ **B.4.b** RATIFIED — execute Config γ refresh per B.4.a.
- ✗ **B.5** DECLINED per recommendation (optional CLAUDE.md → publishing/essays/README.md cross-ref; low-priority navigability boost; skipped).
- ✓ **B.6** RATIFIED — add three-home cross-reference paragraph to `feedback_audience_aware_drafting_discipline.md` (per §2.4).

**Cross-PM-handoff alignment (NEW IN V2):**

- ✓ **B.7** Covered — G2 resolution included in B.2 commit message; sufficient (no standalone chip).
- ✓ **B.8** Covered — A.4 Option D1 partially addresses S3; broader superseded-files sweep remains separate (out of scope here).
- ✓ **B.9** Covered — B.4.a Config γ ruling resolves S5 for AGENTS.md ↔ PM-dashboard tension.

---

## §6. What is explicitly NOT in scope

- **Local laptop memory layer FILES** (the `.md` files at `~/.claude/projects/-Users-c17n-commons-bonds/memory/`). v2 reviewed the laptop MEMORY.md INDEX vs in-repo `tools/memory/README.md` index; this surfaced 5 drift findings (§1.5). Full file-content comparison between laptop layer + in-repo mirror was not performed because this CC session does not have a direct read path into `~/.claude/projects/`; laptop file-content drift detection is on the next memory-sync routine.
- **`tools/memory-updates/` staging-area content review.** S8 decision 2026-05-28 kept this directory as low-volume-but-active. v2 references its discipline but does not audit the staging-area entries.
- **The V-D audit cluster workstream pattern.** ~30+ commits between v1 and v2 are Version A/B/C/D parallel-draft + independent-audit + hybrid pattern across the Wave 1 + Wave 2 essays. This MAY warrant codification as a `reference_` memory entry (alongside `reference_pattern_2_register.md`, `reference_ostrom_illustrative_register.md`, `reference_sandel_hybrid_pattern.md`) IF the pattern stabilizes. v2 flags but does not recommend codification — pattern is in-flight; let it stabilize first. Spawn a follow-up "V-D pattern codification?" decision chip after the cluster lands.
- **Skill invocation.** The `anthropic-skills:consolidate-memory` skill remains an appropriate tool for the laptop-side memory sweep (the in-repo mirror is the focus here). If author wants a mechanical pass over laptop memory after these in-repo ratifications land, the skill is the right tool — spawn as a separate chip per A.9.
- **Memory entry content correctness audit.** v2 (like v1) checks staleness + supersession + overlap + sync; not whether each memory's load-bearing claim is empirically correct. The claims are the author's ratifications.
- **Execution of any pruning.** v2 (like v1) is read-then-recommend. No pruning was executed in this session. Execution is a follow-up chip.

---

## §7. Spawn-after-ratification chip prompt (draft)

If author ratifies subset / all, spawn a follow-up "memory-process-pruning-execution" chip with the following:

```
Title: Execute memory-process review pruning v2 (PROPOSED 2026-05-28)
TLDR: Execute the per-recommendation dispositions ratified at
tools/workstream-handoffs/memory-process-review_2026-05-28.md per §4
sequenced execution plan (v2 revised).

Prompt (self-contained):

You are a fresh CC session executing the ratified pruning dispositions
from the 2026-05-28 memory-process review v2. Author has ratified the
following subset of recommendations: [author specifies which of A.2,
A.4-A.9, B.1-B.9 to execute].

Read tools/workstream-handoffs/memory-process-review_2026-05-28.md §4
"Pruning execution plan (sequenced) — v2 revised" and execute the
ratified steps in the order specified there. Each step is one commit;
internal scaffolding; auto-merge to main per merge-on-ratification rule
with pre-push reconcile.

MANDATORY FIRST ACTION: worktree isolation per CLAUDE.md +
feedback_worktree_isolation_for_parallel_sessions.md.

DO NOT execute steps the author did not ratify. DO NOT execute steps
out of the §4 sequenced order.

If B.4 (AGENTS.md) is ratified: confirm the chosen Config (α / β / γ)
before executing 9b. Pause if unclear.

If A.7 (laptop sync) is ratified: the laptop sync is laptop-only, no
commit; record completion in the session summary.

Expected output: each ratified disposition landed on origin/main (or
laptop, for sync items); state one-liner: "STATE: memory-process-
pruning-execution v2 COMPLETE; NEXT: [next action]; AWAITING: nothing
or author-direction."
```

---

## §8. State

**STATE:** memory-process-review RATIFIED 2026-05-31 — 13 of 14 §5 items ratified in-session via 4-question batch (A.4 D1; A.8 KEEP-LOCAL; B.4.a Config γ; remaining 9 minor items batch-ratified as-recommended; B.5 declined per recommendation). Execution chip spawning per §7.

**NEXT:** spawned execution chip lands the 9-10 ratified in-repo commits per §4 sequenced order + A.7 laptop sync as laptop-only step.

**AWAITING:** execution-chip completion. After chip lands, this report's status closes; no further author action required for the ratified items.

**Per-session protocol close:** This report itself is internal scaffolding; auto-merge to main per merge-on-ratification rule. The ratification IS the merge authorization per CLAUDE.md §"Branch discipline + merge-to-main". v2 RATIFIED-update commit pushes to main per the standard reconcile pattern.
