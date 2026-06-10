# Comp-Titles Deep Matrix — Phase 2 Web Verification Handoff (2026-05-11)

**Date drafted:** 2026-05-11
**Branch to create at session start:** `claude/comp-titles-deep-matrix-phase-2-<harness-id>` (branch from current `origin/main`)
**Status going in:** `publishing/book-proposal/02_comp-titles.md` is at v0 + Phase 1 verified (6 lead + 9 bench, 15 total entries) per the original handoff `comp-titles-deep-matrix-handoff_2026-05-10.md`. **Phase 1 closed the load-bearing agent-pipeline questions; Phase 2 closes the remaining `[verify]` cells just in time for Wave 1 query deployment.**

**Trigger:** **2-3 weeks before Wave 1 query goes out** (current target: late July / early August 2026). **Suggested fire date: early-to-mid July 2026.** Triggering earlier wastes session time on intel that decays before deployment (acquiring editors move imprints; reviewer-of-record at outlets shifts; sales arcs evolve).

---

## Why this is a deferred Phase 2 (not done in the original session)

The original session ran Phase 1 verification (priorities 1+2+3: Mazzucato/Wylie anchor + Wylie-cluster Tooze/Sandel + Darity & Mullen pre-interview) and stopped. Rationale captured in the original session's commit history:

- **Just-in-time intel beats ahead-of-time intel** for fast-moving fields like acquiring-editor identities + sales arcs + review-outlet rosters.
- **The truly load-bearing agent-pipeline questions resolved in Phase 1.** Wylie anchor confirmed (Mazzucato + Tooze); Sandel-on-Wylie falsified; Felicity Bryan / Susskind falsified → PFD/Caroline Michel new hypothesis; Pistor & Christophers likely no-trade-agent (academic-press / Verso direct).
- **Phase 2 remaining cells are matrix polish** — useful for marketing plan §04 + proposal §02 prose, but not blocking the load-bearing decisions in the 10+ weeks between session-end (2026-05-10/11) and Wave 1 deployment.

Phase 2 trigger is therefore explicitly "just-in-time before deployment" — not "complete the original handoff's full 7-12h budget."

---

## Phase 2 scope (remaining `[verify]` cells)

### Priority 1 — Acquiring-editor IDs at the 4 lead imprints

Drives the **editor-target list** (downstream of agents, feeds `publishing/agents/_pipeline/targets.md`).

1. **Public Affairs (Mazzucato — *Value of Everything*)** — who acquired? Imprint changes since 2018 may matter.
2. **Princeton University Press (Pistor — *Code of Capital*)** — likely a politics / law / political-economy editor; possibly Bridget Flannery-McCoy or successor.
3. **Verso (Christophers — *Price is Wrong*)** — Verso US vs. UK distinction matters.
4. **Belknap Press of Harvard University Press (Susskind — *Growth: A Reckoning*)** — Belknap acquiring editor; Allen Lane UK side separate.

**Plus Lead 6:**

5. **University of North Carolina Press (Darity & Mullen — *From Here to Equality*)** — **may already be resolved** by 2026-05-12 Darity interview (matrix Lead 6 carries "Brandon Proia [MEDIUM-confidence]" — the 10-second interview question "Was Brandon Proia your editor?" was queued for the call). Check matrix Lead 6 + Darity interview notes at trigger time before re-researching.

### Priority 2 — Sandel agent ID (FSG lane)

Phase 1 confirmed Sandel is **NOT Wylie** (HIGH) but did not identify his actual agent. Plausible: Tina Bennett (Bennett Literary) or Esther Newberg (ICM/CAA). Acknowledgments-page check of *The Tyranny of Merit* (FSG 2020) is the cleanest path. **~30 min.**

### Priority 3 — Sales-arc verification

Targets: Mazzucato *Value of Everything* + Pistor *Code of Capital* + Christophers *Price is Wrong* + Tooze *Crashed*. Susskind already confirmed via §19 (Obama's Favourite Books 2024 + FT Business Book of the Year 2024 runner-up). **~30 min per title.** BookScan / Publishers Marketplace if accessible; NYT bestseller appearances; major-prize shortlists; foreign-rights deal counts.

### Priority 4 — Chalfant-vs-Bohan close (cross-thread-todos #1)

**Check status at trigger time first.** Cross-thread-todos #1 is partially-progressed as of 2026-05-10 (commit `e4da76c`); parallel sessions may resolve before Phase 2 triggers. If still open at trigger:

- Resolution paths (per cross-thread-todos #1): (a) *Mission Economy* (2021) physical-book acknowledgments check; (b) Publishers Marketplace deal-record lookup; (c) IIPP-network direct query if Albrecht warm-thread converts.
- Wave 1 fallback if unresolved: generic intake `mail@wylieagency.co.uk`.

### Priority 5 — Review-outlet network expansion

Per-comp review-outlet rosters drive `publishing/book-proposal/04_marketing-plan.md`. Cross-check against the partial verifications already inlined in Lead 6 (NYRB Garrett-Scott, Kirkus starred — verified Phase 1). **~15-20 min per comp** for the lead-6 entries; bench entries lower priority.

---

## Budget

| Priority | Budget | Confidence in budget |
|---|---|---|
| 1. Acquiring editors × 4 (5 if UNC Press still open) | ~2h | High |
| 2. Sandel agent ID | ~30 min | Medium (depends on acknowledgments-page access) |
| 3. Sales arcs × 4 | ~2h | Medium (depends on Publishers Marketplace access) |
| 4. Chalfant-vs-Bohan close | ~30 min (if still open) | Low (depends on Mission Economy access at trigger time) |
| 5. Review-outlet network × 6 lead comps | ~2h | High |
| **Total** | **~5-6h** | |

**If parallel sessions have closed Priorities 4 + 5 + some of 1 by trigger time, budget collapses to ~2-3h.** Check cross-thread-todos.md + `publishing/agents/_pipeline/targets.md` + commit log first.

---

## Methodology

1. **State check first.** Read the matrix at current state on main, the cross-thread-todos list, `publishing/agents/_pipeline/targets.md`, and the `publishing/book-proposal/04_marketing-plan.md` (if it's been deepened by parallel sessions). Identify which `[verify]` cells are still open.
2. **Re-verify Phase 1 intel briefly.** Web data shifts. Confirm Wylie cluster (Mazzucato + Tooze) is still current; Sandel still not on Wylie; Felicity Bryan still doesn't list Daniel Susskind. ~10 min.
3. **Work priorities 1-5 in order.** Stop at any natural break if budget runs short — Priority 1 (acquiring editors) is the most load-bearing for proposal-finalization.
4. **Update matrix entries inline** with `[HIGH/MEDIUM/LOW-confirmed 2026-07-XX]` confidence markers (same pattern as Phase 1 commit `18a49af`).
5. **Update `publishing/agents/_pipeline/targets.md`** with editor-target entries derived from Priority 1 findings.
6. **Update `publishing/book-proposal/04_marketing-plan.md`** with review-outlet roster derived from Priority 5 findings.
7. **Commit + push to main per ratified chunk** (per `feedback_git_workflow.md` working principle — active-push expectation).

---

## What NOT to do

- **Don't re-run Phase 1 priorities.** Mazzucato/Wylie anchor + Wylie-cluster Tooze/Sandel + Darity & Mullen pre-interview were all closed in Phase 1. Re-check at the briefly-update level only.
- **Don't research bench entries** unless they've been promoted to lead between sessions. Bench 1-9 are proposal-finalization optionality only; web research budget should serve lead entries.
- **Don't burn budget on Mullen-specific research.** Mullen has been deprioritized per the post-Darity warm-intro reframe (commit `3205e79`, cross-thread-todos #2). Any Mullen-related research only if the Darity interview surfaces an unexpected pathway.
- **Don't try to close every `[verify]` cell.** The matrix carries cells as `[verify]` even when verification is low-priority for deployment. Use judgment — query-letter-and-proposal-deployment cells first; nice-to-have cells only if budget remains.
- **Don't duplicate cross-thread-todos #1 work.** Check its status first; if parallel session has closed it, defer to that resolution.

---

## Deliverables

1. **Updated `publishing/book-proposal/02_comp-titles.md`** — `[verify]` cells closed with confidence-marked findings inline.
2. **Updated `publishing/agents/_pipeline/targets.md`** — editor-target entries added with priority rankings.
3. **Updated `publishing/book-proposal/04_marketing-plan.md`** — review-outlet roster populated.
4. **Cross-thread-todos updates:**
   - `#1 Chalfant ↔ Mazzucato` — moved to Resolved if closed; otherwise status updated.
   - `#8 Comp-titles deep matrix Phase 2 verification` (this item) — moved to Resolved at session end.
5. **Verification log entry** in the matrix's verification log section: "2026-07-XX Phase 2 completed" with summary of what closed vs. what remains open (e.g., generic-intake fallback for Chalfant if unresolved).

---

## First actions for fresh session

1. Read this handoff end-to-end.
2. Read `publishing/book-proposal/02_comp-titles.md` (state check — particularly the verification log section at top of the matrix and the per-entry `[HIGH/MEDIUM/LOW-confirmed]` markers).
3. Read `publishing/essays/_pipeline/cross-thread-todos.md` — items #1 (Chalfant) and #2 (post-Darity warm-intro) and #8 (this) for status.
4. Read `publishing/agents/_pipeline/targets.md` — current agent-target list state.
5. Skim original handoff `tools/workstream-handoffs/archive/comp-titles-deep-matrix-handoff_2026-05-10.md` for context.
6. Identify open `[verify]` cells; cross-reference against parallel-session activity in commit log since 2026-05-11.
7. Begin Priority 1 (acquiring editors).

---

## Reference files

- `publishing/book-proposal/02_comp-titles.md`
- `publishing/agents/_pipeline/targets.md`
- `publishing/agents/_shared/personalization-snippets.md`
- `publishing/book-proposal/04_marketing-plan.md`
- `publishing/essays/_pipeline/cross-thread-todos.md` (items #1 + #2 + #8)
- `research/literature/bibliography.md` §13 (comp-title entries)
- `tools/workstream-handoffs/archive/comp-titles-deep-matrix-handoff_2026-05-10.md` (original handoff)
- `tools/workstream-handoffs/archive/agent-prep-handoff_2026-05-09.md` (downstream consumer)

---

*End of handoff.*
