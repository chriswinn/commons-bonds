# memory-process-review_2026-05-28.md

**Status:** PROPOSED 2026-05-28 — author-action-required (per-recommendation disposition); AWAITING author ratification.
**Amended 2026-05-28** (same session) — author pushback on the bulk-promotion recommendation (§1.3 Rec A/B/C + §3) ratified Option E architecture: short CLAUDE.md paragraph for `no-invented-factual-claims` only; the other two newcomers stay situational because the SessionStart hook + CLAUDE.md §"Branch discipline" already cover their operational rules. Original §1.3 Rec A/B/C + §3 preserved for reasoning trail; revised recommendation at §3.0 (replaces §3) and §5 menu refreshed (A.1, A.3 → withdrawn; A.2 → CLAUDE.md addition instead of full-file promotion).
**Workstream:** `claude/memory-process-review-260528-67ca7b`
**Author kickoff:** "fresh CC session doing a reflective review of the commons-bonds project's memory + process documents, looking for streamlining + pruning opportunities. Author requested this as a follow-up to the 2026-05-28 process + structure changes ratified by the PM session at `tools/workstream-handoffs/pm-session-handoff_2026-05-28.md`."
**Method:** Phase A (memory layer review via 3 parallel Explore sub-agents, ~23 files) + Phase B (process documents drift scan) + Phase C (synthesis + recommendation report — this file).
**Mode:** read-then-recommend. DO NOT prune until author ratifies. Pruning execution is a separate follow-up chip.

---

## Top-of-mind takeaway (TL;DR)

The memory + process layer is **substantively healthy** (24 entries, no obvious legacy junk, clear cross-linking) but has accumulated three identifiable inefficiencies that the 2026-05-28 ratifications make easier to fix:

1. **One load-bearing 2026-05-28 discipline (`no-invented-factual-claims`) is not yet captured in any always-loaded context. The other two newcomers (`merge-on-ratification`, `worktree-isolation`) are already covered operationally** — CLAUDE.md §"Branch discipline + merge-to-main" canonicalizes the first; the SessionStart hook + kickoff paste-text enforce the second at the harness layer. **Revised recommendation (Option E, §3.0): add a short paragraph to CLAUDE.md capturing the no-invented-facts rule (~1KB); leave the other two as situational.** Original §1.3 Rec A/B/C bulk-promotion reasoning preserved below for trail; superseded by §3.0.

2. **`feedback_git_workflow.md` is now redundant + partially stale.** Its 2026-04-29 ".claude/worktrees/" pattern was superseded 2026-05-26 by the parallel-session worktree pattern; its session-end-merge cadence was superseded 2026-05-28 by merge-on-ratification. Its content survives as canonical in CLAUDE.md §"Branch discipline + merge-to-main" + the two newer memory entries. **Recommendation: major amendment OR merge into pointer.** Either trim to a 3-line pointer or archive entirely (the canonical content is now in CLAUDE.md + the newer memory entries).

3. **AGENTS.md has substantial drift.** The "Current canonical state" table is heavily dated to 2026-05-06/17 (open insights tracker, outreach pipeline, Aeon pitch state, current handoff cell). It does not mention merge-on-ratification, status-markers, workstream-handoffs/ system, or the 2026-05-25 marketing-phase reframing. **Recommendation: substantial refresh OR convert most of it to pointers to live artifacts.**

The 20 other memory files are well-calibrated, currently load-bearing, and need only minor amendments (mostly: update cross-references to newer files; refresh one or two stale chapter-status anecdotes that don't affect the load-bearing rule).

---

## §1. Phase A — Memory layer review

### §1.1 Summary table — 23 memory files

| # | File | Type | Ratified | Status | Recommended disposition |
|---|---|---|---|---|---|
| 1 | feedback_audience_aware_drafting_discipline.md | always-load | v3.1 (2026-05-18) | current | **keep-as-is** |
| 2 | feedback_named_subject_consent.md | always-load | 2026-05-09 + 05-12 + 05-20 | current | **keep-as-is** |
| 3 | feedback_verify_stale_memory_claims.md | always-load | 2026-05-10 | current | **keep-as-is** |
| 4 | feedback_merge_on_ratification.md | situational | 2026-05-28 | current (NEW) | **keep situational** (Option E; CLAUDE.md §Branch discipline already canonicalizes) |
| 5 | feedback_no_invented_factual_claims_in_publisher_facing_prose.md | situational | 2026-05-28 | current (NEW) | **add ~5-sentence CLAUDE.md paragraph; full file stays situational** (Option E) |
| 6 | feedback_worktree_isolation_for_parallel_sessions.md | situational | 2026-05-26 | current (NEW) | **keep situational** (Option E; SessionStart hook + kickoff paste-text already enforce) |
| 7 | feedback_parallel_session_ratification_cadence.md | situational | 2026-05-24 | current | **keep-as-is** (situational is right) |
| 8 | feedback_git_workflow.md | situational | 2026-04-29 (with 05-10, 05-24, 05-25 extensions) | partially superseded | **major amendment OR archive** |
| 9 | feedback_two_layer_content_discipline.md | situational | 2026-04-30 (WP#10) | current | **keep-as-is** |
| 10 | feedback_audit_recent_active_review_default.md | situational | 2026-05-12 | current | **keep-as-is** |
| 11 | feedback_audit_open_illustrative_default.md | situational | 2026-05-12 | current | **keep-as-is** |
| 12 | feedback_pm_dashboard_structure.md | situational | 2026-05-13 | minor drift | **minor amendment** (line 44 → status-markers.md; add Class-column note) |
| 13 | feedback_rigor_vs_bookkeeping_distinction.md | situational | 2026-05-27 | current | **keep-as-is** (consider promote) |
| 14 | feedback_substrate_critical_editorial_input.md | situational | 2026-05-21 | current | **keep-as-is** |
| 15 | feedback_em_dash_overuse.md | situational | 2026-05-21 | current | **keep-as-is** |
| 16 | feedback_dual_audience_test.md | situational | 2026-05-11 | current | **keep-as-is** |
| 17 | feedback_grammatical_role_cross_references.md | situational | 2026-05-11 | current | **keep-as-is** |
| 18 | feedback_substance_drives_length.md | situational | 2026-05-02 | current | **keep-as-is** (one stale chapter-status anecdote does not affect rule) |
| 19 | feedback_voice_polish_pipeline.md | situational | 2026-05-04 | current | **keep-as-is** (ditto) |
| 20 | reference_ostrom_illustrative_register.md | situational | 2026-05-02 | current | **keep-as-is** (verify Cᵢ list before audit-side use) |
| 21 | reference_pattern_2_register.md | situational | (Insight-anchored, pre-2026-05-01) | current | **keep-as-is** |
| 22 | reference_sandel_hybrid_pattern.md | situational | 2026-05-11 | current | **keep-as-is** |
| 23 | project_book_complete_marketing_phase.md | situational | 2026-05-25 | mostly-current with stale operational anchors | **minor amendment** (split phase-reframing rule from operational status claims) |

### §1.2 ARCHIVE.md candidate ranking

The bar for archival is high (the entry is fully-resolved AND no longer informing current practice). On that bar:

| Rank | Candidate | Rationale | Disposition |
|---|---|---|---|
| 1 | `feedback_git_workflow.md` | The 2026-04-29 worktree pattern (`/Users/c17n/commons-bonds/.claude/worktrees/<session-name>`) and the session-end-merge cadence are both superseded. The 2026-05-24 internal-scaffolding extension and 2026-05-25 path update lived inside this file but are now codified in CLAUDE.md + `feedback_merge_on_ratification.md`. The file no longer adds load-bearing content vs the canonical CLAUDE.md section. | **Archive OR collapse to 3-line pointer** |
| — | (none others rank high enough) | All other 22 memory entries remain operationally live in some form. | — |

**Discipline reminder:** ARCHIVE.md is the safe disposal target. Do NOT delete a memory file — archive it (move the entry into `ARCHIVE.md` with a one-paragraph retirement rationale, then delete the source file). The 2026-05-17 `project_book1_state_2026-05-10.md` ARCHIVE.md entry is the format precedent.

### §1.3 Per-file justification for the four headline recommendations

#### Rec A — Promote `feedback_merge_on_ratification.md` to always-load

**Argument.** Ratified 2026-05-28 (today). Codifies the new default merge cadence for ALL end-user-facing prose work (book chapters + every essay + op-eds + cover letters + agent correspondence + outreach packets). Every session touching publisher-facing prose needs this rule to avoid falling back to the 2026-05-16 explicit-merge gate. Empirical anchor (Foreign Affairs essay 2026-05-27, 6-hour stranded-ratified-prose incident) is recent and reputationally consequential. The escape-hatch markers (`MERGE-HOLD:` / `MERGE-AFTER:`) are vocabulary the session needs to recognize at commit-message-authoring time, which happens at every commit. Cost of loading: ~7.5KB (small file). Cost of NOT loading: a session falls back to 2026-05-16 logic and another piece of ratified prose strands on a feature branch.

**Counterargument.** The rule is already canonicalized in CLAUDE.md §"Branch discipline + merge-to-main" (which IS always-load). So the memory entry is duplicative.

**Resolution.** The CLAUDE.md section is the rule statement; the memory file is the empirical anchoring + escape-hatch syntax + worked examples. Both are useful, but the memory entry is the more grep-friendly + cross-link-friendly form. Recommended: keep CLAUDE.md as the rule, promote memory file to always-load as the operational reference. (Alternative: don't promote, but explicitly mark that CLAUDE.md §"Branch discipline" is the authoritative source and the memory entry is supplementary. Either works; promotion is mildly preferred for symmetry with the other two newcomers.)

#### Rec B — Promote `feedback_no_invented_factual_claims_in_publisher_facing_prose.md` to always-load

**Argument.** Ratified 2026-05-28 (today). HARD RULE. Reputational asymmetry is the load-bearing claim — shipped-with-fabrication propagates from essay → book → future work and is not recoverable. The empirical anchor (Ch 2 → Harper's Pass 3.5 near-miss with 4 illustrative-prose findings each containing invented testimonial-register specifics; Pass 3.1 F-3.1-H1 invented Bailey biographical specifics caught at HIGH severity) demonstrates that absent this discipline, sub-agents WILL produce invented testimonial-register prose at HIGH confidence. The discipline applies at every drafting + Pass 3.1 + Pass 3.5 + Stage 5 + sub-agent generation point. The "sub-agent discipline" section (§"In sub-agent design + kickoff paste-texts") is load-bearing for every kickoff paste-text Claude writes. Cost of loading: ~17KB. Cost of NOT loading: at high parallelism, a sub-agent generates invented prose with `[Substrate-critical note: ...]` flags + parent session ratifies-as-recommended without per-finding scrutiny + fabrication ships.

**Counterargument.** None of consequence. This is the most defensible promotion of the three.

**Resolution.** Promote.

#### Rec C — Promote `feedback_worktree_isolation_for_parallel_sessions.md` to always-load

**Argument.** Ratified 2026-05-26. Operating-model discipline at 20-35+ concurrent sessions. The SessionStart hook fires automatically (defense layer 1), but the hook only warns; the discipline depends on the session reading + heeding the warning AND doing the worktree-add correctly AND using absolute paths inside the new worktree for the entire session. A session that loads this memory has internalized the WHY (350-branch contamination empirical anchor) + the HOW (worktree-add bash snippet) + the failure mode (absolute paths, not `cd` back to main cwd). Cost of loading: ~16KB. Cost of NOT loading: at sustained parallel-session volume, contamination recurs; the 2026-05-26 incident demonstrated the contamination is silent (HEAD swap is not visible until commit lands on wrong branch).

**Counterargument.** The SessionStart hook + the kickoff paste-text already enforce this. Loading the memory is belt-and-suspenders.

**Resolution.** The empirical anchor (350+ contaminated branches; "sessions just swapping branches they were committing in seemingly at random") establishes that the hook alone is insufficient under volume. Belt-and-suspenders is justified for system-level operational safeguards at this stakes level. Promote.

#### Rec D — Major-amendment (or archive) `feedback_git_workflow.md`

**Argument.** The file is heavily superseded:

- Line 16-17: ".claude/worktrees/<session-name>" pattern — superseded 2026-05-26 by the parallel-session worktree pattern at `/Users/c17n/commons-bonds-<workstream>-<harness-id>` (siblings of main, not subdirectories).
- Line 19-25: "Session-end ritual" — superseded 2026-05-28 by merge-on-ratification (push per ratified chunk, not at session-end).
- Line 28: 2026-05-24 "end-user-facing prose requires author ratification before merge" — superseded 2026-05-28 by merge-on-ratification (ratification IS the merge).

The remaining load-bearing content is:
- The "pre-push reconciliation pattern" (line 27) — already in CLAUDE.md.
- The "active-push expectation" (line 26) — already in CLAUDE.md.
- The "internal scaffolding auto-merge" (line 28) — already in CLAUDE.md.

**Resolution.** Two options.

- **Option D1 (recommended): collapse to a 3-line pointer.** Replace lines 10-30 with: "Canonical content moved to CLAUDE.md §'Branch discipline + merge-to-main' (2026-05-28 merge-on-ratification rule). Worktree-isolation pattern at [`feedback_worktree_isolation_for_parallel_sessions.md`](feedback_worktree_isolation_for_parallel_sessions.md). This file retained for historical reference to the 2026-04-29 ratification of WP#9." Keeps the memory-index link working without duplicating content.
- **Option D2: archive entirely.** Add an entry to ARCHIVE.md noting the supersession, then delete the file. Cleaner but loses the small amount of historical context (the iCloud incident anchor for WP#9).

Recommendation: **D1**. The iCloud-incident historical anchor is small but useful for understanding why the project moved to worktree isolation in the first place.

### §1.4 Minor-amendment cases

- **`feedback_pm_dashboard_structure.md`**: Add a sentence after line 44 pointing to `tools/conventions/status-markers.md` as the authoritative source for emoji + status-marker conventions (the memory entry's summary remains useful; the canonical now lives elsewhere). Optional addition: a "Class column recommendation" note pointing to `feedback_rigor_vs_bookkeeping_distinction.md` for PM dashboards that need rigor-vs-bookkeeping discrimination.

- **`project_book_complete_marketing_phase.md`**: Split the phase-reframing rule (load-bearing; foundational to cascade plan + venue strategy) from the operational status claims (which chapters in which stage; cascade-plan version; Q2-Q3 2027 timing). The phase-reframing should remain in the memory; the operational status should either (a) be removed (stale-prone) or (b) be marked as "verify against current state before quoting." Recommend (a): remove the operational status; keep the phase-reframing.

---

## §2. Phase B — Process documents drift scan

### §2.1 Drift table

| Document | Current state | Drift assessment | Recommended disposition |
|---|---|---|---|
| `CLAUDE.md` | 207 lines; refreshed 2026-05-28 for merge-on-ratification + status-markers section + per-essay rigor consolidation note. | **Current.** Merge-on-ratification section is canonical authority for the new rule. Status-markers section is canonical pointer. | **Keep-as-is.** Consider one small addition (see §2.2 below). |
| `AGENTS.md` | 168 lines; "Current canonical state" table dated 2026-05-06/07/09/17. | **Substantially drifted.** No mention of merge-on-ratification, status-markers, workstream-handoffs/ system, or marketing-phase reframing. Open-insights tracker says "7 OPEN as of 2026-05-17" (11 days stale). Outreach pipeline cell dated 2026-05-05. Aeon essay cell dated 2026-05-04. Current handoff cell references `v1.52.0` (the old `alignment/sessions/` system, not the workstream-handoffs/ system). "Session workflow" section (lines 135-144) references old upload-set workflow that does not match current worktree-isolation + paste-text reality. "What's queued" section (lines 115-133) is dated 2026-05-06. | **Substantial refresh OR convert most to pointers.** See §2.3 for refresh plan. |
| `tools/README.md` | 156 lines; refreshed 2026-05-28 for subfolders inventory; "Session-start upload set" section retained from earlier era. | **Partially drifted.** Subfolders inventory (lines 28-101) is current. Session-start upload set (lines 11-22) + copy-paste session-start block (lines 121-131) + "Notes for agents" (lines 152-156) are stale — they reference `alignment/sessions/` handoffs, the v2.2.0 rigor protocol upload set, `/Noema/` and `/Berggruen Institute - Essay/` Drive folders (Drive-era; not current). | **Minor amendment** — strip or refresh the upload-set sections (lines 11-22 + 121-131); update notes section (lines 152-156) to remove Drive-era hard rules; explicitly note that current session start = worktree-isolation first, paste-text kickoff. |
| `tools/pipeline-doctrine/README.md` | 36 lines; created 2026-05-28 as part of S6. | **Current.** Clean. | **Keep-as-is.** |
| `tools/conventions/status-markers.md` | 150 lines; codified 2026-05-28 as part of S7. | **Current.** Clean. | **Keep-as-is.** |
| `tools/workstream-handoffs/README.md` | 122 lines; last refreshed 2026-05-28 for merge-on-ratification update at line 11. | **Partial drift.** Lines 11 are current. Lines 17-83 list workstream handoffs by date through 2026-05-18; the branch-prefix conventions (`claude/aeon-submission-`, `claude/boston-review-essay-`, etc.) are stale — actual current branches use `claude/<workstream>-<harness-id>` with auto-generated harness IDs per the worktree-isolation discipline. Lines 99-105 list PM dashboards through 2026-05-28 (current). "Excluded from these handoffs" section (lines 107-113) is fine. | **Minor amendment** — update branch-prefix column header or remove it (the auto-generated harness-ID format makes per-workstream branch prefixes lower-stakes than they were 2026-05-09). Add a paragraph in the branch-discipline section noting that current branches use the `claude/<workstream>-<harness-id>` format per `feedback_worktree_isolation_for_parallel_sessions.md`. |
| `publishing/essays/README.md` | 123 lines; refreshed 2026-05-28 for `rigor/` + `editor-iteration/` + `_archive/pre-submission/` subdirs. | **Mostly current.** "Active essay packages (as of 2026-05-25)" table is 3 days stale — current state has Atlantic Ideas pitch ratified 2026-05-28 (Aeon column says "Submission package scheduled 2026-05-31" — verify against actual current state). | **Minor amendment** — refresh the Active essay packages table to current 2026-05-28 state. |

### §2.2 Recommended CLAUDE.md addition (optional, low-priority)

CLAUDE.md currently mentions per-essay rigor consolidation in the "Internal scaffolding" bullets (line 109-112) but does not point to the per-essay layout standard. Consider adding a one-line cross-reference: "Per-essay layout: see [`publishing/essays/README.md`](publishing/essays/README.md) for the `rigor/` + `editor-iteration/` + `_archive/pre-submission/` subdirs and the per-essay-rigor-consolidation pattern ratified 2026-05-28."

Low priority — the current cross-references via the internal-scaffolding bullets are sufficient; this is a navigability nice-to-have.

### §2.3 AGENTS.md refresh plan

**Option 1 (recommended): substantial refresh.** Update the "Current canonical state" table to reflect 2026-05-28 reality:

- Add rows for: merge-on-ratification rule, status-markers convention, workstream-handoffs/ system, marketing-phase reframing.
- Refresh stale rows: open insights tracker (verify count and entries), manuscript drafting state (verify 10/10 still accurate; note Phat anonymization), Aeon essay (refresh to current state), outreach pipeline (heavy refresh).
- Update "Current handoff" row to point to `tools/workstream-handoffs/pm-session-handoff_2026-05-28.md` (not `v1.52.0`).
- Refresh "Session workflow" section (lines 135-144) to current discipline: worktree-isolation first action → workstream-handoffs/ paste-text kickoff → per-session protocol close.
- Refresh "What's queued" section (lines 115-133) to current workstreams.

Estimated effort: ~30-60 min substantive editing. Spawn as a dedicated chip after this review's recommendations are ratified.

**Option 2: convert most of AGENTS.md to pointers.** Many AGENTS.md rows duplicate content from canonical sources (working principles document, vocabulary strategy, framework-positioning disciplines, etc.). Converting the table to one-line pointers ("Pipeline doctrine: see `tools/pipeline-doctrine/`") reduces drift surface area at the cost of one-stop scannability.

**Option 3: lighter-touch refresh.** Refresh only the 2-3 most-stale rows (open insights tracker, current handoff, marketing-phase reframing) and leave the rest. Trades thoroughness for time.

Recommended: Option 1 (substantial refresh) as a dedicated post-this-review chip. AGENTS.md is the canonical internal-scaffolding orientation document; the value of currency is high. If author prefers a lighter touch given competing priorities, Option 3 is acceptable.

---

## §3.0 Phase C — Always-load set recalibration (REVISED — Option E, supersedes §3)

**Author pushback 2026-05-28 (same session):** the §3 bulk-promotion recommendation underweighted that (a) the load-bearing rule per discipline is ~1 paragraph while the 7-17KB files are mostly empirical anchors + worked examples + cross-references, and (b) two of the three newcomers are already covered operationally at the always-loaded layer (CLAUDE.md §"Branch discipline") or at the harness layer (SessionStart hook). The original symmetry-argument for promoting all three was thin.

### §3.0.1 Revised always-load architecture

**Current always-load (unchanged):**
- `feedback_audience_aware_drafting_discipline.md` (v3.1; ~18KB; justified because the rule IS the v3.1 pipeline architecture — 6 stages × 5 passes × change-cascade routing; the OS manual for every Stage 3 pass)
- `feedback_named_subject_consent.md` (~5.6KB)
- `feedback_verify_stale_memory_claims.md` (~2.5KB)

**Net change:** No file promotions. Instead, **add a ~5-sentence paragraph to CLAUDE.md** capturing the no-invented-factual-claims hard rule. Estimated CLAUDE.md addition: ~1KB. Full memory file (`feedback_no_invented_factual_claims_in_publisher_facing_prose.md`, ~17KB) stays situational; sessions doing Pass 3.1 / Pass 3.5 / Stage 5 / sub-agent kickoff work load it deliberately.

**Net always-load delta: ~1KB instead of 40KB.** All three newcomer rules covered operationally:

| Discipline | Where it's covered |
|---|---|
| Merge-on-ratification | CLAUDE.md §"Branch discipline + merge-to-main" (already always-load); memory file at `tools/memory/feedback_merge_on_ratification.md` is supplementary empirical anchor |
| Worktree isolation | SessionStart hook fires automatically on every fresh session + kickoff paste-text + `tools/conventions/status-markers.md` references; memory file remains the deep-dive |
| No-invented-factual-claims | **Gap.** No CLAUDE.md analog; no harness-layer mechanism. The Ch 2 → Harper's Pass 3.5 near-miss empirically demonstrated that the *situational-load-when-relevant* discipline can fail at high parallelism when sub-agents generate invented prose at HIGH confidence with substrate-critical flags. The discipline applies at *every* drafting + Pass 3.1 + Pass 3.5 + Stage 5 + sub-agent generation point — even sessions whose primary task isn't prose generation can spawn sub-agents that produce invented content. This is the one with the real always-load case, but the always-load form should be a short CLAUDE.md paragraph, not the full 17KB file. |

### §3.0.2 Draft CLAUDE.md addition (for ratification with Option E)

Recommended insertion point: after the existing §"Named-subject consent" section (CLAUDE.md lines 181-188), as a new §"No invented factual claims" section. Draft:

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

~205 words / ~1.4KB. Captures the hard-rule scope, the asymmetric stakes, the thought-experiment exception, the sub-agent kickoff discipline, the pointer to deep reference.

### §3.0.3 What replaces the original §3.2 "Compromise option"

Option E IS the compromise option the original §3.2 gestured at, but sharper: a ~1KB CLAUDE.md addition is meaningfully different from a 17KB always-loaded memory file. The original §3.2 compromise (promote only no-invented-facts; leave the other two situational) was already directionally correct; Option E refines it to "add the rule to CLAUDE.md prose; full memory file stays situational" which is the architecture pattern that already works for the v3.1 doctrine summary vs the full pipeline-doctrine files.

---

## §3. Phase C — Always-load set recalibration (SUPERSEDED — preserved for trail; see §3.0 for revised recommendation)

### §3.1 Current always-load set (3)

- `feedback_audience_aware_drafting_discipline.md` (v3.1)
- `feedback_named_subject_consent.md`
- `feedback_verify_stale_memory_claims.md`

### §3.2 Proposed always-load set (6)

Add:
- `feedback_merge_on_ratification.md` (rationale §1.3 Rec A)
- `feedback_no_invented_factual_claims_in_publisher_facing_prose.md` (rationale §1.3 Rec B)
- `feedback_worktree_isolation_for_parallel_sessions.md` (rationale §1.3 Rec C)

Keep all 3 existing.

**Demotion candidates:** None. All 3 current always-loads are foundational; none demotes.

**Total context-window impact:** Adding 3 files at ~7.5KB + 17KB + 16KB = ~40KB additional always-loaded context. The existing always-loaded set is ~26KB total (the audience-aware-drafting summary is the largest at 18KB). Combined new always-load = ~66KB, which is a meaningful chunk of context. Author may want to weigh that against the cognitive-overhead-on-every-session cost of loading 40KB of recurrent operational discipline.

**Compromise option:** Promote only `feedback_no_invented_factual_claims_in_publisher_facing_prose.md` (highest reputational stakes; least redundant with CLAUDE.md). Leave `feedback_merge_on_ratification.md` and `feedback_worktree_isolation_for_parallel_sessions.md` as situational on the rationale that (a) CLAUDE.md §"Branch discipline" already canonicalizes merge-on-ratification at always-load level, and (b) the SessionStart hook fires automatically for worktree-isolation. This compromise saves ~24KB of always-loaded context for the cost of a slightly thinner safety net. Defensible if context-budget is the binding constraint.

### §3.3 Considered-and-rejected always-load candidates

- `feedback_rigor_vs_bookkeeping_distinction.md` (2026-05-27) — load-bearing for PM session work and cross-essay portfolio reviews, but situational for the modal drafting session. Keep situational; the index entry is clear enough that PM sessions will load it.
- `feedback_parallel_session_ratification_cadence.md` (2026-05-24) — operating-model discipline; reasonable case for promotion but the kickoff paste-texts already enforce the per-session pattern + the PM session inherits the meta-tracker pattern via the dashboard. Keep situational.

---

## §4. Pruning execution plan (sequenced)

**Revised per Option E (§3.0):** Step 1 is now a CLAUDE.md prose addition, not an `@import` block update. The always-load file set stays at 3. Steps 5+ also adjusted (README index reflects situational status of the three newcomers; no always-load count change).

If author ratifies all (Option E version), execute in this strict order (each step depends on prior step landing):

1. **Add CLAUDE.md §"No invented factual claims" section** (~205 words, drafted at §3.0.2) after existing §"Named-subject consent" section. No `@import` changes. One commit. Pre-push reconcile + push (internal scaffolding; auto-merge per merge-on-ratification).
2. **Amend `feedback_pm_dashboard_structure.md`** (line 44 → status-markers.md pointer + Class-column note). One commit.
3. **Amend `project_book_complete_marketing_phase.md`** (split phase-reframing from operational status). One commit.
4. **Major-amendment `feedback_git_workflow.md`** (collapse to pointer per Option D1) OR **archive entirely** per Option D2. One commit. If archived, add ARCHIVE.md entry in same commit.
5. **Update `tools/memory/README.md`** index: confirm always-loads remain 3 (no change); update the disposition of `feedback_git_workflow.md`; optionally add a one-line note that `feedback_no_invented_factual_claims_in_publisher_facing_prose.md` is now also captured in CLAUDE.md §"No invented factual claims" as a short paragraph for always-loaded context. One commit.
6. **Refresh `tools/README.md`** session-start sections (lines 11-22 + 121-131 + 152-156). One commit.
7. **Refresh `tools/workstream-handoffs/README.md`** branch-prefix conventions. One commit.
8. **Refresh `publishing/essays/README.md`** Active essay packages table. One commit.
9. **Refresh AGENTS.md** (Option 1: substantial refresh OR Option 3: lighter-touch refresh). One commit (the largest).

Each commit is internal scaffolding; auto-merges to main per the merge-on-ratification rule. Pre-push reconcile (`git fetch origin main && git rebase origin/main`) before each push to inherit parallel-session work.

**Strict ordering rationale:**
- Step 1 (CLAUDE.md `@import` updates) lands first because subsequent memory amendments may want to verify the always-load set is updated.
- Step 4 (git_workflow disposition) before step 5 (README index update) because the index reflects the disposition.
- Step 9 (AGENTS.md refresh) last because it pulls from the now-clean state of all prior steps.

**Estimated total effort:** ~2-3 hours if substantial AGENTS.md refresh (Option 1); ~1-1.5 hours if lighter-touch (Option 3).

---

## §5. Author-action menu (per-recommendation disposition)

Author can ratify per-recommendation OR batch-ratify all. Each numbered item maps to a §1.3 or §1.4 or §2 recommendation.

**Memory layer (Phase A) — REVISED per §3.0 Option E:**

- ~~**A.1** Promote `feedback_merge_on_ratification.md` to always-load?~~ **WITHDRAWN per §3.0** — CLAUDE.md §"Branch discipline + merge-to-main" already canonicalizes; memory file stays situational.
- ☐ **A.2** ~~Promote `feedback_no_invented_factual_claims_in_publisher_facing_prose.md` to always-load?~~ **REVISED:** Add the ~5-sentence CLAUDE.md paragraph drafted at §3.0.2 (~1KB) as a new §"No invented factual claims" section after CLAUDE.md §"Named-subject consent". Full memory file stays situational. [§3.0]
- ~~**A.3** Promote `feedback_worktree_isolation_for_parallel_sessions.md` to always-load?~~ **WITHDRAWN per §3.0** — SessionStart hook + kickoff paste-text + status-markers.md cross-refs already enforce; memory file stays situational.
- ☐ **A.4** Dispose of `feedback_git_workflow.md` — Option D1 (3-line pointer) OR Option D2 (archive entirely)? (Recommendation: D1.) [§1.3 Rec D]
- ☐ **A.5** Minor amendment to `feedback_pm_dashboard_structure.md` (line 44 → status-markers.md; Class-column note)? [§1.4]
- ☐ **A.6** Minor amendment to `project_book_complete_marketing_phase.md` (split phase-reframing from operational status; remove stale operational anchors)? [§1.4]

**Process documents (Phase B):**

- ☐ **B.1** Refresh `tools/README.md` session-start sections (lines 11-22 + 121-131 + 152-156) to current discipline? [§2.1 + §2.3]
- ☐ **B.2** Refresh `tools/workstream-handoffs/README.md` branch-prefix conventions to `claude/<workstream>-<harness-id>` format? [§2.1]
- ☐ **B.3** Refresh `publishing/essays/README.md` Active essay packages table to 2026-05-28 state? [§2.1]
- ☐ **B.4** AGENTS.md refresh — Option 1 (substantial), Option 2 (pointers), or Option 3 (lighter-touch)? (Recommendation: Option 1 as a dedicated chip.) [§2.3]
- ☐ **B.5** Optional CLAUDE.md addition (one-line cross-reference to publishing/essays/README.md per-essay layout)? Low priority. [§2.2]

**~~Compromise option C.1~~ — SUPERSEDED by Option E (§3.0)** which is sharper than C.1 (CLAUDE.md paragraph, not full-file promotion). Original C.1 preserved below for trail; if author prefers the lighter touch, C.1 is also acceptable.

- ~~**C.1** Promote only A.2 (no-invented-factual-claims) to always-load; leave A.1 and A.3 as situational on the rationale that CLAUDE.md §"Branch discipline" + SessionStart hook already cover their core content. Saves ~24KB of always-loaded context. [§3.2]~~ Superseded by Option E.

---

## §6. What is explicitly NOT in scope (deferred / out-of-scope)

- **Local laptop memory layer** (`~/.claude/projects/-Users-c17n-commons-bonds/memory/`). The MEMORY.md index loaded into context at session start shows the laptop layer is in sync with the in-repo mirror at `tools/memory/`. This review confines its recommendations to the in-repo mirror; the laptop layer should mirror any ratified amendments via the next memory-sync routine. (Reference: `tools/memory-updates/` staging area.)
- **`tools/memory-updates/` staging-area review.** S8 decision 2026-05-28 kept this directory as low-volume-but-active. This review did not audit the staging-area entries.
- **Skill invocation.** The `anthropic-skills:consolidate-memory` skill was considered but not invoked because (a) its primary target is the local laptop memory, not the in-repo mirror under review here; and (b) the cross-document drift scan (Phase B) is broader than the skill's scope. If author wants a mechanical pass over the laptop memory after these in-repo ratifications land, the skill is the right tool — spawn as a separate chip.
- **Memory entry content correctness audit.** This review checked for staleness + supersession + overlap, not for whether each memory's load-bearing claim is empirically correct. The claims are the author's ratifications; this review respects those ratifications.
- **Execution of any pruning.** Per the kickoff brief: this is read-then-recommend. No pruning was executed in this session. Pruning execution is a follow-up chip spawnable after author ratifies the dispositions.

---

## §7. Spawn-after-ratification chip prompt (draft)

If author ratifies subset / all, spawn a follow-up "memory-process-pruning-execution" chip with the following:

```
Title: Execute memory-process review pruning (PROPOSED 2026-05-28)
TLDR: Execute the per-recommendation dispositions ratified at tools/workstream-handoffs/memory-process-review_2026-05-28.md per §4 sequenced execution plan.

Prompt (self-contained):

You are a fresh CC session executing the ratified pruning dispositions
from the 2026-05-28 memory-process review. Author has ratified the
following subset of recommendations: [author specifies which of A.1-A.6,
B.1-B.5, C.1 to execute].

Read tools/workstream-handoffs/memory-process-review_2026-05-28.md §4
"Pruning execution plan (sequenced)" and execute the ratified steps in
the order specified there. Each step is one commit; internal scaffolding;
auto-merge to main per merge-on-ratification rule with pre-push
reconcile.

MANDATORY FIRST ACTION: worktree isolation per CLAUDE.md +
feedback_worktree_isolation_for_parallel_sessions.md.

DO NOT execute steps the author did not ratify. DO NOT execute steps
out of the §4 sequenced order.

Expected output: each ratified disposition landed on origin/main; state
one-liner: "STATE: memory-process-pruning-execution COMPLETE; NEXT:
[next action]; AWAITING: nothing or author-direction."
```

---

## §8. State

**STATE:** memory-process-review PROPOSED 2026-05-28 (amended same session per author pushback — Option E architecture for always-load recalibration; see §3.0); NEXT: author-action-required (per-recommendation disposition per refreshed §5); AWAITING: author ratification.

**Per-session protocol close:** This report itself is internal scaffolding; auto-merge to main per merge-on-ratification rule. The report's recommendations are PROPOSED, not RATIFIED; the file landing on main does not constitute ratification of its recommendations. The Option E amendment IS ratified (author pushback → Option E selected via AskUserQuestion 2026-05-28); the per-recommendation dispositions inside Option E remain awaiting batch / per-item ratification.
