# Project Management Session — Handoff (2026-05-18, v2.0 dashboard structure)

**Date drafted:** 2026-05-18 (Mon). Supersedes `pm-session-handoff_2026-05-13.md` (which covered the 2026-05-13 → 2026-05-17 window via in-place updates).
**Companion artifact:** `pm-mobile-todo-dashboard_2026-05-15.md` — mobile-scope cut. Refresh after major in-flight items land.
**Branch to create at session start:** `claude/pm-session-<harness-id>` (branch from current `origin/main` after `git fetch`).
**Session type:** Parallel coordination session. Tracks state, surfaces dependencies, manages todos, flags deadlines, routes work between sessions. Does NOT execute workstream tasks.

**Structure:** Follows v2.0 dashboard structure codified in `feedback_pm_dashboard_structure.md` (ratified 2026-05-13). Memory entries now mirrored at `tools/memory/` per memory-migration apply 2026-05-17 (`b62c2f1`).

---

## 0. Mission of the PM session

You are the PM coordination session. Your job is to keep the *Commons Bonds* project's many parallel workstreams legible to the author.

**You execute:** status updates (with auto-verify per §13); todo management; deadline tracking; sequencing recommendations; dependency surfacing; cross-thread coordination; paste-text generation for fresh sessions.

**You do NOT execute:** workstream work (drafting, auditing, editing); content decisions; submissions; memory updates beyond status corrections.

---

## 1. Read order

1. THIS file (you are here) — §2–§6 first for at-a-glance orientation; §7+ as you dive into specifics.
2. `tools/workstream-handoffs/README.md` — workstream handoff index.
3. `tools/workstream-handoffs/pm-mobile-todo-dashboard_2026-05-15.md` — mobile-scope todos (may need refresh).
4. Memory entries — now mirrored at `tools/memory/` (canonical) plus `~/.claude/projects/-Users-c17n-commons-bonds/memory/`:
   - `feedback_pm_dashboard_structure.md` — v2.0 structure
   - `feedback_audience_aware_drafting_discipline.md` — v2.0 two-stage discipline
   - `feedback_verify_stale_memory_claims.md` — staleness
   - `feedback_audit_recent_active_review_default.md` + `feedback_audit_open_illustrative_default.md`
   - `project_book1_state_2026-05-10.md` — **now 8 days old; treat all time-sensitive claims as stale**
5. `publishing/strategy/cross-thread-todos.md`
6. `publishing/strategy/cascade-plan_2026-05-06.md` + `publishing/strategy/decisions-log.md`
7. `CLAUDE.md` — canonical workflow doctrine; merge-to-main default extended to rigor-pass artifacts (`abccb43` + `3d52a0e`)
8. `tools/commons_bonds_pipeline_doctrine_v1.0.0.md` — pipeline doctrine ratified 2026-05-17

You do NOT need to read individual workstream handoffs unless drilling into one. Index-level knowledge is enough for coordination.

---

## 2. Next 72 hours — TOP OF MIND

| When | Action |
|---|---|
| **TODAY Mon May 18 8:00 AM ET** | **CBF reply v6.1 auto-sends** (Gmail scheduled-send, `7141634`). Call-windows reply to Val DiMarzio (gatekeeper). No action — automatic. Verify it left outbox by mid-morning. |
| **Mon May 18 — Tue May 19** | **Triage Chs 7/8/9/10 Pass 1 findings.** All four chapters now have PROPOSED Pass 1 docs (`ff9a89a`/`210b02c`/`9720da0`/`c85c41d`). **Ch 8 = 4 HIGH / 8 MEDIUM / 7 LOW; READY AFTER SPOT-FIXES.** Need ratification cycles + Phase C-α applications for each. Also: ratify residual **Ch 1 Pass 3** items (items i + iv applied; check what's still PROPOSED in REAUDIT v3 `76ca8a6`) and **Ch 4 Pass 2** PROPOSED `3174cc8`. |
| **Wed May 20 8:00 AM EDT** | **CBF consolidated response auto-sends** (`b200664`) — distinct from v6.1; this is the original Val + David consolidated response. No action — automatic. Verify both fired correctly. |
| **This week (by Sun May 24)** | Fire **Ch 2 Pass 3** + **Ch 3 Pass 2** + **Ch 3 Pass 3** + **Ch 4 Pass 3** (paste-text gen from PM). Continue Phase C-α applications on Chs 7/8/9/10 as ratifications land. **Sandy reply window opens Thu May 21** (1 week post-send) — soft check-in only if no acknowledgment by then. |

---

## 3. Critical path bottleneck

**Critical path is now the Phase C-α applications for Chs 7/8/9/10** + the residual Pass 2/3 cycles for Chs 1/2/3/4. Sandy send is complete; Pass 1's are all fired across the manuscript; what gates the book proposal sprint (late June) is now the application + Pass 2/3 cadence catching up. Apparatus Phase A (Bibliography / Glossary / TA per-chapter call-site verification) still gated on chapter-level Stage-3 completion — but most chapters are now far enough along that this gate is becoming visible.

**New parallel critical-path candidate: pipeline doctrine retrofits** (11 handoffs landed 2026-05-17; see §7 Apparatus + §8 Decisions pending). Those retrofits are infrastructure rather than content, but they gate Stage 4 audits per the doctrine.

---

## 4. USER ACTIONS gating Noema submission

Still open from 2026-05-13. These remain the *only* gates on Noema submission and are uniquely user-action.

- [ ] **Action 1 — Phat consent outreach** (or Phat's family if Phat unavailable). Package ready at `research/outreach/subjects/phat/` per commits `585d535` + `721c094` + `9aee0af`. Living named subjects must be anonymized until signed.
- [ ] **Action 2 — Apply consent decision to Essay B line 136** of [noema-essay-fresh-session-draft_2026-05-10.md](manuscript/essay/Noema/noema-essay-fresh-session-draft_2026-05-10.md).
- [ ] **Action 3 — Apply same to Ch 3** in [Chapter__3_TheWaterman__Draft.md](manuscript/chapters/Chapter__3_TheWaterman__Draft.md).

These have been open ≥ 5 days. Worth deciding this week whether to escalate (e.g., a deadline-self-imposed forcing function — "I will reach out by Fri May 22 or accept the anonymized version") rather than letting it drift further.

---

## 5. Workstream status (by bucket, by priority)

Priority within bucket: **HIGH** = time-pressured or gates large downstream cascade. **MED** = important but not yet gating. **LOW** = small / dormant / waiting.

### 5.1 IN FLIGHT

| # | Pri | Workstream | Status | Next action |
|---|---|---|---|---|
| **20** | **HIGH** | Manuscript Stage-3 Rigor Pass | Chs 5+6 CLOSED 2026-05-14. Ch 1 Pass 2 RATIFIED 2026-05-15 + Pass 3 PROPOSED with reaudits. Ch 4 Pass 2 PROPOSED 2026-05-15. **Chs 7+8+9+10 Pass 1 PROPOSED 2026-05-16.** See per-chapter detail §6. [handoff](manuscript-stage-3-rigor-pass-handoff_2026-05-11.md) | Ratify Pass 1 findings for Chs 7/8/9/10 + apply Phase C-α; ratify residual Ch 1 Pass 3 items; ratify Ch 4 Pass 2 + apply. |
| **4** | MED | Outreach pipeline | Sandy packet SENT 2026-05-14; proactive Q0 citation-questions follow-up SENT 2026-05-15. CBF v6.1 scheduled-send TODAY 8am ET (`7141634`); original Val+David consolidated response auto-sends Wed May 20 8am EDT (`b200664`). Colden citation-verify packet pre-staged (`15c6b0f`) — user-action. Biggie process guide pre-staged (`164b9e2`). [handoff](outreach-pipeline-handoff_2026-05-09.md) | Monitor inbox for Sandy reply (window opens Thu May 21); verify CBF auto-sends fire; user-action send Colden packet. |
| **NEW** | MED | **Pipeline doctrine v1.0.0 retrofits** (per-chapter + TA + AuthorsNote + Dedication) | 11 retrofit handoffs landed 2026-05-17 (`a7c38e2` + `7c1aa57`). Render-pipeline-standardization workstream blocks Stage 4 audits (`3678ca2`). Pre-renders via remote-container pipeline for Ch 1 + 5 + 6 + TA landed (`27252f1`). Sandy-packet engine attribution corrected to wkhtmltopdf (`c0c4ae2`). | Fire retrofits per pipeline-revision handoff sequencing. Coordinate with #20 — retrofits shouldn't collide with Phase C applications. |
| **NEW** | MED | **Cross-chapter rent-seeking engagement** (Public Choice complementarity) | PROPOSED content edits 2026-05-17 (`a1e54d9`). Handoff at `cross-chapter-rent-seeking-engagement-handoff_2026-05-17.md`. | Author ratify; PM session can absorb into chapter Pass 2/3 cadence if scope is light. |

### 5.2 READY TO FIRE

| # | Pri | Workstream | Status | Fire window |
|---|---|---|---|---|
| **1** | **HIGH** | Aeon pitch | Version C ratified 2026-05-08; Stage 3 verdict 2026-05-10 confirmed. [handoff](aeon-submission-handoff_2026-05-09.md) | **Sun May 31 14:01 UTC** (= Mon Jun 1 ~00:01 AEST). Pre-submission verify by Fri May 29. |
| **2** | MED | Boston Review essay | UNBLOCKED 2026-05-10. **Source chapter (Ch 5) now stable** — three-pass cycle CLOSED. [handoff](boston-review-essay-handoff_2026-05-09.md) | Draft pitch (~1pp) + essay (~4,500w from Ch 5). When bandwidth permits. |
| **16** | MED | $100 Barrel essay → Phenomenal World | Q1 verdict GO (`b7fd20f`). Condition 1 (non-partisan framing) carries forward. [handoff](100-barrel-essay-handoff_2026-05-11.md) | Fire Session 2 — Stage 1 audience-aware brief w/ Condition 1 embedded. |
| **14** | MED | Comp-titles deep matrix Phase 2 | Just-in-time verification deferred from #11. [handoff](comp-titles-deep-matrix-phase-2-handoff_2026-05-11.md) | Early-to-mid July 2026 (2–3wk before Wave 1). |

### 5.3 WAITING / BLOCKED / DORMANT

| # | Pri | Workstream | Gated on | Target |
|---|---|---|---|---|
| **5** | **HIGH** | Book proposal | #20 Chs 7–10 completion (passes 2+3) | Late-June 2026 sprint (~3wk). [handoff](book-proposal-handoff_2026-05-09.md) |
| **6** | MED | Agent prep / target list | #20 + #5 + #14 | Wave 1 late Jul / early Aug 2026. 1/25 populated. [handoff](agent-prep-handoff_2026-05-09.md) |
| **3** | MED | Berggruen Prize essay | AI-free constraint (user-only) | Soft 2026-08-05; hard 2026-08-17. [handoff](berggruen-track-handoff_2026-05-09.md) |
| **12** | LOW | Aeon essay post-acceptance | Aeon acceptance of #1 | Dormant. [handoff](aeon-essay-post-acceptance-two-stage-handoff_2026-05-10.md) |
| **17** | LOW | Publishing pipeline | TRIGGERED + IN USE 2026-05-14 (Sandy packet) + 2026-05-17 (remote-container pre-renders). Standing capability. May want a small handoff update capturing the build-derivatives.sh / pipeline-doctrine v1.0.0 work. | Operational. |

### 5.4 COMPLETE since 2026-05-13 (one-line; full standing-references in workstream handoffs)

- **Sandy packet send (Ch 5 + Ch 6 + TA v2.1.0)** 2026-05-14 1pm ET — artifacts in `research/outreach/subjects/darity/*_2026-05-14.{docx,pdf}`
- **Sandy proactive Q0 citation-questions follow-up** SENT 2026-05-15
- **Ch 5 + Ch 6 Stage-3 three-pass cycles CLOSED** 2026-05-14 (Pass 3 ratified as-proposed for both)
- **Ch 1 Pass 2 RATIFIED + APPLIED** 2026-05-15 (`7b4aa92`; 10 spot-fixes)
- **Tech Appendix v2.1.0** (Phase C Tracks 1–5 + §5.5 bidirectionality + verification round)
- **Ch 10 bidirectional-reach insertion paragraph** ratified (`376eb3c`)
- **TA scope/grounding verification (Ch 6 MI-3 + SI-3 mirrors) — CLEAN** 2026-05-15 (`4a928f4`)
- **#18 Ch 6 .html → .md conversion** 2026-05-13 (`1d9b941`)
- **#19 TA Scheme-4 cleanup** 2026-05-13 (`2c880bc`)
- **$44B Program-vs-Trust-Fund canonical drift correction** across Ch 2 + Ch 8 (`cacb82d`)
- **Pipeline doctrine v1.0.0 cluster + invariant-gate infrastructure** (`3e31d9d` + `935633e` + `ed5f6cf`)
- **Memory migration audit + apply** 2026-05-17 (`d11f67a` + `d197449` + `b62c2f1`) — memory entries mirrored at `tools/memory/`
- **CBF outreach v6 → v6.1 finalized + scheduled-send Mon May 18** (`7141634`)

Earlier completions still standing (since 2026-05-10): #8 Path B audit, #9 Apparatus register, #10 Cross-chapter consistency, #11 Comp-titles v0, #13 Flagship terms defense, #15 TA numbering reconciliation.

**Retired:** #7 Manuscript completion (substance migrated to §7 Apparatus 2026-05-13).

---

## 6. #20 Stage-3 Rigor Pass — per-chapter detail

| Ch | Pass 1 (fact-check) | Pass 2 (voice-polish) | Pass 3 (audience-load) | Phase C spot-fixes | **Next action** |
|---|---|---|---|---|---|
| **1** | ✅ COMPLETE | ✅ **RATIFIED + APPLIED 2026-05-15** (`7b4aa92`; 10 spot-fixes) | PROPOSED `43f2b7a` + REAUDIT v3 `76ca8a6` (40-character adversarial); items (i) `013415f` + (iv) `f692164` RATIFIED + APPLIED; line 29 grandfather paragraph applied `54709e7`; item (iv) actually deferred to pre-pub `ea94684` | Pass 2 spot-fixes complete | **Ratify remaining Pass 3 REAUDIT items** (check what's still PROPOSED past i + iv); Phase C-γ if needed; then Stage-3 closed for Ch 1 |
| **2** | ✅ COMPLETE | ✅ COMPLETE | not started — paste-text drafted | 14 applied | **Fire Pass 3** (paste-text from PM) |
| **3** | ✅ LANDED `2f76e37` | not started | not started | — | **Fire Pass 2** (paste-text from PM) |
| **4** | ✅ COMPLETE | PROPOSED 2026-05-15 (`3174cc8`) | not started | 5 MEDIUM + 2 LOW (`e67b8b8` + `8f792ee`) | **Ratify Pass 2** + apply spot-fixes |
| **5** | ✅ CLOSED 2026-05-14 | ✅ CLOSED 2026-05-14 | ✅ CLOSED 2026-05-14 — RATIFIED as-proposed (READY TO SUBMIT AS-IS) | all applied through C-β-followup | **Cycle CLOSED.** No further work unless Sandy reply surfaces revisions. |
| **6** | ✅ CLOSED 2026-05-14 (with Amendments B/C/D/E) | ✅ CLOSED 2026-05-14 (through C-δ + cascade convergence-table refresh) | ✅ CLOSED 2026-05-14 — RATIFIED as-proposed (Tier-B-optional held) + Phase C-ε disposition recorded (`83431ab`) | all applied; α-dominance phrase-swap held as conditional trigger | **Cycle CLOSED.** α-dominance swap fires if any reviewer flags α-notation. |
| **7** | PROPOSED 2026-05-16 (`ff9a89a`) — rigor pass artifact at `tools/rigor-passes/commons_bonds_rigor_pass_2026-05-16_ch7_on_other_worlds_stage3_fact_check_v1.0.0.md` | — | — | — | **Ratify Pass 1 findings + apply Phase C-α** |
| **8** | PROPOSED 2026-05-16 (`210b02c`) — **4 HIGH / 8 MEDIUM / 7 LOW; READY AFTER SPOT-FIXES**; artifact at `tools/rigor-passes/commons_bonds_rigor_pass_2026-05-16_ch8_what_things_actually_cost_stage3_fact_check_v1.0.0.md` | — | — | $44B drift correction landed (`cacb82d`) | **Ratify Pass 1 (especially 4 HIGH) + apply Phase C-α** |
| **9** | PROPOSED 2026-05-16 (`9720da0`) — rigor pass artifact at `tools/rigor-passes/commons_bonds_rigor_pass_2026-05-16_ch9_pricing_honestly_stage3_fact_check_v1.0.0.md` | — | — | — | **Ratify Pass 1 + apply Phase C-α** |
| **10** | PROPOSED 2026-05-16 (`c85c41d`) — rigor pass artifact at `tools/rigor-passes/commons_bonds_rigor_pass_2026-05-16_ch10_common_bonds_stage3_fact_check_v1.0.0.md` | — | — | bidirectional-reach insertion already ratified (`376eb3c`) | **Ratify Pass 1 + apply Phase C-α** |

**Cross-thread #11 (endnote/citation sweep)** accumulating: Ch 2 = 9M+1L; Ch 4 = 5M+3L; Ch 5 = 16M + 14L + N-6 citation-form sharpening; Ch 6 substantial; Chs 7/8/9/10 contributions land with their Phase C applications. Hard target before late-July Wave 1.

---

## 7. Apparatus + front-and-back-matter

| Item | Pri | Phase A (per-chapter) | Phase B (book-wide audit) | Current state | Fires when |
|---|---|---|---|---|---|
| **Bibliography** | MED | Per-chapter engagement-flag pass Chs 1–10 | Book-wide reconciliation | TA Phase C Track 5 added bibliography expansion (`36073ca`); book-wide bib still needs per-chapter pass. **Du Bois** addition pending (Darity C-2 cross-thread). | Per-chapter after each Ch's Pass 3 lands. Chs 5 + 6 ready; Chs 1/4 nearly ready; Chs 2/3/7-10 pending. |
| **Technical Appendix** | LOW (was MED) | Per-chapter pass: every apparatus call-out points to correct §-numbers | v2.1.0 LIVE | **v2.1.0 SHIPPED TO SANDY.** Per-chapter call-site audit can run as chapters complete Stage-3. Pipeline doctrine v1.0.0 retrofit handoff at `ta-pipeline-retrofit-handoff_2026-05-17.md`. | Per-chapter after #20 stabilization + retrofit. |
| **Glossary** | MED | Per-chapter pass | v4 rebuild + audit | UNBLOCKED 2026-05-11. Not started. | Per-chapter after #20 voice-polish + audience-load. |
| **AI Statement** | LOW | Single pass | n/a | Current artifact: `manuscript/chapters/_AUTHORSNOTE_ON_WINDTUNNELS_AND_AI.md`. Source material at `research/process-narrative/origin-story_2026-05-13.md` (with reception-strategy notes). Pipeline doctrine retrofit handoff at `authorsnote-pipeline-retrofit-handoff_2026-05-17.md`. | Anytime; no gates. |
| **Dedication** | LOW | Single pass | n/a | At `manuscript/chapters/_Dedication.md` — state TBD; needs verification (P3 #15 mobile-todo). Pipeline doctrine retrofit handoff at `dedication-pipeline-retrofit-handoff_2026-05-17.md`. | Anytime; no gates. |

**Pipeline doctrine retrofits (NEW workstream cluster — 2026-05-17):**

11 retrofit handoffs at `tools/workstream-handoffs/ch{1-10}-pipeline-retrofit-handoff_2026-05-17.md` + `ta-pipeline-retrofit-handoff_2026-05-17.md` + `authorsnote-pipeline-retrofit-handoff_2026-05-17.md` + `dedication-pipeline-retrofit-handoff_2026-05-17.md` + `pipeline-retrofit-template_2026-05-17.md`. Plus `render-pipeline-standardization-handoff_2026-05-17.md` (blocks Stage 4 audits) and `pipeline-revision-handoff_2026-05-17.md` + `pipeline-revision-session-close_2026-05-17.md`. **Author should decide sequencing relative to in-flight #20 work** — see §8 Decisions pending.

---

## 8. Decisions pending

- **Pipeline retrofit sequencing.** 11 retrofit handoffs are stood up. They're infrastructure (alignment with pipeline doctrine v1.0.0), not content. Question: fire them in parallel with Phase C-α applications for Chs 7–10, OR sequence after #20 stabilizes? PM recommendation: **fire pipeline retrofits in batches paced by render-pipeline-standardization completion** — that workstream blocks Stage 4 audits per its handoff, so it sequences first. Retrofits can then run in parallel with Phase C application as long as branch isolation holds.
- **Cross-chapter rent-seeking engagement edits.** PROPOSED content edits at `a1e54d9` (Public Choice complementarity). Author ratify; absorb into chapter Pass 2/3 cadence if scope is light.
- **Phat consent escalation.** Action 1 has been open ≥ 5 days. Worth setting a self-imposed forcing deadline (e.g., Fri May 22) — either Phat outreach happens or anonymized version is accepted as final. Don't let it drift indefinitely.
- **Sandy reply triage protocol.** Reply window opens Thu May 21 (1 week post-send). If no acknowledgment by then, soft check-in. If reply lands earlier, follow P2 #12 triage in mobile dashboard.
- **TA per-chapter call-site audit timing.** Now that v2.1.0 is published + per-chapter Pass 1's are all PROPOSED, the TA call-site audit can be folded into Phase C-α applications for Chs 7–10 (catch TA references during the fix-up cycle) rather than waiting for a separate Apparatus Phase A run.
- **Boston Review essay fire.** Ch 5 source chapter now stable. Worth scheduling Boston Review pitch + essay drafting before #16 ($100 Barrel) Session 2 since it has the more direct chapter→essay path. Either order works; just be explicit about which fires when.

---

## 9. Date-anchored action list

### TODAY Mon May 18
- [ ] **8:00 AM ET** — CBF reply v6.1 auto-sends (`7141634`). Verify outbox by mid-morning.
- Triage Chs 7/8/9/10 Pass 1 findings (start with Ch 8's 4 HIGH items)
- Ratify residual Ch 1 Pass 3 items if any past i + iv remain PROPOSED in REAUDIT v3

### Tue May 19 — Wed May 20
- **Wed May 20 8:00 AM EDT** — original CBF consolidated response auto-sends (`b200664`)
- Continue Chs 7/8/9/10 ratification + Phase C-α apply
- Ratify Ch 4 Pass 2 + apply spot-fixes
- Decide Phat consent escalation deadline (recommend Fri May 22)

### This week (by Sun May 24)
- **Thu May 21** — Sandy reply window opens (1 week post-send); soft check-in only if silence
- Fire **Ch 2 Pass 3** (paste-text from PM)
- Fire **Ch 3 Pass 2** + **Ch 3 Pass 3** (paste-text from PM)
- Fire **Ch 4 Pass 3** (after Ch 4 Pass 2 spot-fixes apply)
- Continue Chs 7/8/9/10 cycles toward Pass 2 trigger

### Fri May 29
- **Aeon Version C pre-submission verify** — final read-through (~20min)

### Sun May 31 14:01 UTC (= Mon Jun 1 ~00:01 AEST)
- **Submit Aeon pitch Version C** verbatim via aeon.co/pitch

### Late May / early June
- **Submit Noema essay** (gated on §4 USER ACTIONS)
- **Send Colden pre-publication citation-verification packet** (user-action; `15c6b0f`)
- **Fire $100 Barrel essay (#16) Session 2** — Stage 1 brief w/ Condition 1
- **Boston Review pitch + essay drafting** (now unblocked — Ch 5 stable)

### Late June
- **Book proposal sprint** (#5) — gated on #20 Chs 7–10 Pass 2/3 completion
- **Publishing-lawyer consultation** (cross-thread #7) — user-action

### July
- **Comp-titles Phase 2 verification** (#14) — fire window early-to-mid July
- **Late July / early August — Agent Wave 1** (8 Priority A) — gated on #20 + #5 + #14

### Late summer
- **Tue Aug 5** — Berggruen Prize soft target (AI-free)
- **Sun Aug 17** — Berggruen Prize hard deadline

### Backlog (no fixed date)
- Pipeline retrofit batches (11 handoffs at `tools/workstream-handoffs/ch{1-10}+ta+authorsnote+dedication-pipeline-retrofit-handoff_2026-05-17.md`)
- Render-pipeline-standardization completion (blocks Stage 4 audits)
- Cross-thread #9 — Ch 2 GuidanceDoc stale "$100 barrel passage" refs (sibling on $44B drift; route via #9)
- Apparatus Phase A per-chapter rolling fires
- **Darity cross-thread C-1** Fogel-Engerman two-volume model → #14 comp-titles
- **Darity cross-thread C-2** Du Bois → bibliography
- Cross-chapter rent-seeking engagement ratification + apply

### Dormant / conditional
- #12 Aeon post-acceptance — fires on Aeon acceptance
- Biggie courtesy-notify before any essay using his name publishes
- Sandy substantive-response handling
- Ch 6 Tier-B α-dominance phrase-swap — fires if any reviewer flags α-notation

### Future agent waves
- **Sept–Oct 2026** — Wave 2 (8 Priority B)
- **Q4 2026 / Q1 2027** — Wave 3 (9 Priority C)

---

## 10. Cross-thread coordination

| # | Item | Producer | Consumer | Status |
|---|---|---|---|---|
| 1 | Acknowledgments check: Chalfant ↔ Mazzucato | Outreach / verification | #6 Wave 1 | Partial — `Value of Everything` read (no agent named); `Mission Economy` pending. Chalfant-check worktree state per session-handoff inventory. |
| 2 | Post-Darity warm-intro discovery | #4 Outreach | #6 Agent prep | **RESOLVED via synthesis** (`3e39061`). Findings folded into agent prep target intelligence. |
| 4 | Atlantic Ideas vs. PW slot-3 venue | Publishing strategy | Future essay slot-3 | Open — may resolve via #16 → PW |
| 5 | Boston Review v2.0 application | PM meta-verdict | #2 session | RESOLVED 2026-05-10 |
| 6 | Aeon post-acceptance v2.0 application | PM meta-verdict | #12 session | RESOLVED 2026-05-10 |
| 7 | Interview-attribution protocol jurisdictional gaps | PM session | Protocol-update + publishing-lawyer | Protocol v2 COMPLETE (`998166f`); lawyer consult target by late June |
| 8 | Comp-titles Phase 2 | #11 → #14 | #6 Wave 1; #5 §04 | Open — dormant until early-to-mid July |
| 9 | Ch 2 GuidanceDoc stale "$100 barrel passage" refs + sibling $44B Trust Fund drift | #10 audit + Mobile-todo `7141634`-era fix | Insight #37 Batch-D | Open — $44B drift fixed in chapter prose; GuidanceDoc sweep still pending |
| 10 | PM-verified apparatus-stability checkpoint for #16 | Q1 rigor pass | #16 fire decision | RESOLVED 2026-05-11 |
| 11 | Endnote / citation-finalization sweep | Per-chapter #20 audits | Coordinated endnote sweep | Open — accumulating; hard target before Wave 1 |
| 12 | Ch 8 coal-CO₂ short-ton cascade flag | TA Phase C Track | Ch 8 Pass 1 | **RESOLVED** — fixed via $44B drift correction batch + Ch 8 Pass 1 now PROPOSED (`210b02c`) |
| **13 NEW** | Darity Q0 tier-S citation outreach (3 paragraphs: Ch 5 line 220 + Ch 6 line 124 + Ch 6 line 262) | Sandy reply | Ch 5 + Ch 6 prose | SENT 2026-05-15 (proactive); awaiting Sandy ratification |
| **14 NEW** | Memory-mirror sync (entries at `tools/memory/` + `~/.claude/projects/.../memory/`) | Memory-migration apply 2026-05-17 | All future PM sessions | Operational — sessions should read from `tools/memory/` as canonical going forward |
| — | Author-bio updates as essays place | #4 + essay submissions | #5 author platform | Continuous |

Full inventory: `publishing/strategy/cross-thread-todos.md`.

---

## 11. PM session freshness — when to wrap and start fresh

**This PM session has been running 2026-05-13 → 2026-05-18 (5 calendar days; over 75 commits landed).** Multiple phase-shift triggers fired:
- ✅ Major event: Darity interview + synthesis + packet send
- ✅ Major event: Sandy citations follow-up
- ✅ Major chapter completions: Ch 5 + Ch 6 cycles CLOSED; Ch 1 Pass 2 applied
- ✅ Major infrastructure: Pipeline doctrine v1.0.0 + invariant gates + 11 retrofit handoffs
- ✅ Major event: Memory migration applied (mirroring to `tools/memory/`)
- ✅ All Chs 7/8/9/10 Pass 1 fired

**Strong recommendation: wrap this PM session and start a fresh one** orienting against this handoff. The next session's natural focus: Phase C-α applications for Chs 7/8/9/10 + pipeline retrofit sequencing + Sandy reply triage when it lands + Aeon submission countdown (Sun May 31).

Per protocol on wrap:
1. ✅ Successor file written (this file).
2. ✅ README index will be updated to point at this file.
3. ✅ Predecessor `pm-session-handoff_2026-05-13.md` will be marked superseded.
4. **User-facing recommendation:** wrap this session and start fresh.

---

## 12. How to handle common user prompts

- **"What should I do next?"** → Lead with §2 (next 72h) + §3 (critical path) + §4 (USER ACTIONS). Cross-ref §5 status + §9 dates. Recommend the highest-priority unblocked item that fits available time/energy.
- **"I just finished X." / "X session is done."** → Auto-verify per §13 (origin/main + artifact spot-check) BEFORE marking complete.
- **"Give me text to paste into a fresh session for X."** → Generate paste-text per the appropriate handoff + drafting-templates scaffold (`tools/drafting-templates/`). Paste-text only; do NOT execute.
- **"What's blocked?"** → §5.3 column "Gated on."
- **"What's overdue?"** → §9, items with past dates not yet marked done.
- **"What does workstream X need?"** → Read the workstream's handoff (linked in §5).
- **"Add a todo: ..."** → Insert into §9 at appropriate date bucket.
- **Day-of-week / date assertions** → Verify against a known anchor before asserting. Today (per harness): **Mon May 18, 2026.**

When you don't know — say so. Verify before asserting (per `feedback_verify_stale_memory_claims.md`).

---

## 13. Auto-verify discipline (RATIFIED 2026-05-10; extended 2026-05-15)

**Trigger conditions.** PM session auto-verifies origin/main canonical state before marking ANY workstream / todo / dashboard row complete. Triggers:
- User reports a session finished.
- PM session notices new commits on origin/main during a routine fetch.
- PM session is about to mark anything complete.

**Workflow default extended 2026-05-15** (`abccb43` + `3d52a0e`): autonomous merge-to-main for author-ratified content changes + rigor-pass artifacts. PM session should expect frequent main-branch updates from sister sessions.

**The verification protocol.**
1. `git fetch origin main`.
2. Confirm commit on origin/main (`git log origin/main --oneline | grep <hash>`).
3. Direct-inspect artifact(s).
4. If clean: mark complete on dashboard with commit hash + one-line evidence.
5. If something's off: flag before marking.

**Verbosity tradeoff.** Default: medium (verify commit on main + key content spot-check; 3–5 line summary).

---

## 14. Parallel-PM-session collision risk

Pattern observed 2026-05-13 → 2026-05-18: many parallel sessions landing commits to origin/main in tight succession. The 2026-05-13 dashboard was kept current via in-place updates by multiple parallel PM sessions. **Mitigation:** fetch origin/main before any edit to coordination files. Prefer SHORT, ATOMIC edits. If a parallel session has just pushed, reconcile rather than rebase-and-overwrite.

---

## 15. Reusable drafting-session templates

Five scaffolds at `tools/drafting-templates/` (`e29db8c`):
- Stage 1 pre-draft brief
- Stage 2 fresh-session draft (audience-blind)
- Stage 3 Pass 1 fact-check
- Stage 3 Pass 2 voice-polish
- Stage 3 Pass 3 audience-load

Use as starting points for paste-text generation.

---

## 16. Two-stage drafting discipline v2.0 — RATIFIED + CODIFIED

**RATIFIED 2026-05-10. CODIFIED 2026-05-10 (commit `9caccdc`).**

v2.0 amendments A + B + C in force. Memory: `feedback_audience_aware_drafting_discipline.md` (mirrored at `tools/memory/`). A v3.0 proposal exists at `tools/memory-updates/feedback_audience_aware_drafting_discipline_v3.0.md` (post 2026-05-17 audit) — **author input needed on whether to promote v3.0**.

---

## 17. Pipeline doctrine v1.0.0 — RATIFIED 2026-05-17

`tools/commons_bonds_pipeline_doctrine_v1.0.0.md` + stage docs (`stage_1`, `stage_4`, `stage_5`). Invariant-gate infrastructure: `.github/workflows/corpus-invariants.yml` + `tools/scripts/check-corpus-invariants.sh` + `tools/scripts/install-pre-commit-hook.sh` + `tools/quality-gates/` (regressed-patterns.yaml, scaffolding-patterns.yaml, render-baselines/build-environment.yaml). Render pipeline at `tools/scripts/build-derivatives.sh` + `-alt.sh`.

11 retrofit handoffs stood up 2026-05-17 (one per chapter + TA + AuthorsNote + Dedication). Render-pipeline-standardization workstream blocks Stage 4 audits. Sequencing decision pending (§8).

---

## 18. Outreach pipeline detail

| Subject | Affiliation | Status | Date | Notes |
|---|---|---|---|---|
| **William ("Sandy") Darity Jr.** | Duke | **PACKET SENT + Q0 follow-up SENT** | 2026-05-14 + 2026-05-15 | Awaiting response. Reply window opens Thu May 21. |
| **Val DiMarzio + David Sherfinski (CBF)** | CBF MD + VA | **Multiple scheduled-sends in flight** | Mon May 18 8am (v6.1) + Wed May 20 8am (consolidated) | Two distinct sends. Val gatekeeper-call request inbound 2026-05-15; v6.1 reply (`7141634`) addresses that. |
| **Mariana Mazzucato** | UCL/IIPP | HOLDING via Adam Albrecht | Held since 2026-05-06 | Not blocking. |
| **Allison Colden** | CBF MD | Pre-pub citation-verify packet pre-staged | `15c6b0f` | User-action to send. |
| **Karen Moore** | CBF VA | Public-record brief landed | 2026-05-08 | — |
| **Biggie family (Ch 3 deceased)** | — | Process guide pre-staged (`164b9e2`) | — | User-decision pending. |
| **Boyce, Buller, Mian, Sufi, Alperovitz, Mondragon, Klein, Coalition of Clinics, Raworth, ACLC, Lipcius, Mann** | Various | Cold-outreach sent | 2026-05-05 | 13 days out; verify inbox before quoting status. |

---

## 19. Updating this handoff

This file IS the PM session's working memory. Update in place as state changes. **For successor:** every ~7–14 days OR after significant phase shift, write `pm-session-handoff_<NEW-DATE>.md`, update `tools/workstream-handoffs/README.md`, mark predecessor superseded.

**Predecessor:** `pm-session-handoff_2026-05-13.md` (covered 2026-05-13 → 2026-05-17 window via in-place updates).

---

## 20. Reference inventory

**Index files:**
- `tools/workstream-handoffs/README.md`
- `publishing/strategy/cross-thread-todos.md`
- `publishing/strategy/cascade-plan_2026-05-06.md`
- `publishing/strategy/decisions-log.md`
- `CLAUDE.md` — workflow doctrine
- `AGENTS.md` — canonical-state index (refreshed `ed5f6cf`)

**Memory entries** (now mirrored at `tools/memory/` per `b62c2f1`):
- See `tools/memory/README.md` + `tools/memory/ARCHIVE.md` for full index

**Pipeline doctrine artifacts (NEW 2026-05-17):**
- `tools/commons_bonds_pipeline_doctrine_v1.0.0.md` + stage docs
- `tools/quality-gates/` registries
- `tools/scripts/` (build-derivatives + check-corpus-invariants + install-pre-commit-hook)
- `.github/workflows/corpus-invariants.yml`

**Recent rigor-pass + Sandy-packet artifacts:**
- `tools/rigor-passes/commons_bonds_rigor_pass_2026-05-{13,15,16}_*.md` (Pass 1's for Chs 7–10; Pass 2 for Ch 1 + Ch 4; reaudits)
- `tools/rigor-passes/commons_bonds_ch{1,5,6}_stage_3_pass_*_PROPOSED.md`
- `tools/rigor-passes/tech_appendix_*` (Pass 1 math audit + verification round + §5.5 bidirectionality proposal)
- `research/outreach/subjects/darity/post-interview-synthesis_2026-05-13.md`
- `research/outreach/subjects/darity/packet-send-cover-email_2026-05-14.md`
- `research/outreach/subjects/darity/proactive-q0-citation-questions_DRAFT_2026-05-14.md`
- `research/outreach/subjects/darity/ta-scope-grounding-verification_2026-05-15.md`
- `research/outreach/subjects/darity/*_2026-05-14.{docx,pdf}` — packet artifacts
- `research/outreach/subjects/darity/*_with-citations_2026-05-14.{docx,pdf}` — citations follow-up artifacts
- `research/outreach/subjects/cbf/inbound_2026-05-15_val-call-request.md`
- `research/outreach/subjects/cbf/response-draft_2026-05-15_call-windows.md`

**Reusable drafting-session templates:** `tools/drafting-templates/`

**Session handoff archives (v1.45 series):**
- `alignment/sessions/commons-bonds-session-handoff-2026-05-15_v1.45.0.html`
- `alignment/sessions/commons-bonds-session-handoff-2026-05-15_v1.45.1.html`

---

*End of PM session handoff (v2.0 dashboard structure). Update in place as state evolves; write successor file ~weekly or after structural shift.*
