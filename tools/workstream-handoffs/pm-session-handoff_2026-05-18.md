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
   - `project_book1_state_2026-05-19.md` — refreshed 2026-05-19 (supersedes `_2026-05-18.md` + `_2026-05-10.md`); still verify time-sensitive claims per stale-memory discipline
5. `publishing/strategy/cross-thread-todos.md`
6. `publishing/strategy/cascade-plan_2026-05-06.md` + `publishing/strategy/decisions-log.md`
7. `CLAUDE.md` — canonical workflow doctrine; merge-to-main default extended to rigor-pass artifacts (`abccb43` + `3d52a0e`)
8. `tools/commons_bonds_pipeline_doctrine_v1.0.0.md` — pipeline doctrine ratified 2026-05-17

You do NOT need to read individual workstream handoffs unless drilling into one. Index-level knowledge is enough for coordination.

---

## 2. Next 72 hours — TOP OF MIND

| When | Action |
|---|---|
| ~~Mon May 18 8:00 AM ET — CBF v6.1 + consolidated response both auto-send (`7141634` + `b200664`)~~ | **BOTH VERIFIED SENT by author Mon May 18 8am ET** — advance materials + call-windows in Val/David's inbox since Monday. |
| **TODAY Tue May 19** | Triage **Chs 7/8/9/10 Pass 1** findings; ratify residual **Ch 1 Pass 3** items in REAUDIT v3 `76ca8a6`; ratify **Ch 4 Pass 2** PROPOSED `3174cc8`. Queue **Ch 2 developmental-edit** session (Ch 1 cycle complete; see §5.1). |
| **🆕 Thu May 21 — 2:00 PM (ET, presumed) — CBF MEETING LOCKED** | **Three-person video call: Chris + Val DiMarzio + David Sherfinski.** Microsoft Teams; **Teams link RECEIVED 2026-05-19** (in author's inbox; add to calendar). Val + David have had advance materials since Mon May 18 — should arrive prepped. **Prep scope spans both MD (Colden) and VA (Moore) sides.** Pre-staged materials at `research/outreach/subjects/cbf/{interview-prep,live-call-companion,organizational-brief}_*.md` — review with dual-state scope in mind. Same day Sandy reply window opens — CBF meeting is the day's anchor. |
| **This week (by Sun May 24)** | Fire **Ch 2 Pass 3** + **Ch 3 Pass 2** + **Ch 3 Pass 3** + **Ch 4 Pass 3** (paste-text gen from PM). Continue Phase C-α applications on Chs 7/8/9/10 as ratifications land. Continue pipeline retrofits (Chs 2/3/4/7/8/9/10 + AuthorsNote + Dedication remain pending; Chs 1/5/6/TA fired 2026-05-18). Fire **Ch 2 developmental-edit** session. ~~Decide Phat consent escalation deadline~~ — **RESOLVED 2026-05-20: anonymization ratified.** |

---

## 3. Critical path bottleneck

**Critical path is the Phase C-α applications for Chs 7/8/9/10** + the residual Pass 2/3 cycles for Chs 1/2/3/4 + the new **developmental-edit (Pass 3.5) workstream** across Chs 2–10 + AuthorsNote (Ch 1 already RATIFIED + applied 2026-05-18 — see §5.1). Sandy send is complete; Pass 1's all fired manuscript-wide; what gates the book proposal sprint (late June) is the application + Pass 2/3 cadence catching up, plus the new Pass 3.5 layer now folded into Stage 3 per Pipeline doctrine Amendment B (`316073e`).

**Infrastructure now mostly resolved.** Render-toolchain canonical pipeline RATIFIED 2026-05-19 (`b3f4af5`); render-output policy in place; docker-render.sh convenience wrapper landed (`7e88701`); CI render-verify workflow active (`6ebda00`). **Stage 4 audits unblocked.** Pipeline retrofits for Ch 1 + Ch 5 + Ch 6 + TA fired 2026-05-18; Chs 2/3/4/7/8/9/10 + AuthorsNote + Dedication retrofits still queued.

Apparatus Phase A (Bibliography / Glossary / TA per-chapter call-site verification) still gated on chapter-level Stage-3 completion — most chapters now far enough along that this gate is becoming visible.

---

## 4. USER ACTIONS gating Noema submission

~~Three open USER ACTIONS from 2026-05-13~~ → **🟢 PHAT ANONYMIZATION RATIFIED 2026-05-20** per author direction. The Noema submission gate now clears as a metadata-decision. Two operational follow-ons remain:

- [ ] **Apply anonymization to Essay B line 136** of [noema-essay-fresh-session-draft_2026-05-10.md](manuscript/essay/Noema/noema-essay-fresh-session-draft_2026-05-10.md). Small content edit; user-action or dedicated session.
- [ ] **Apply anonymization to Ch 3 v1 draft** in [Chapter__3_TheWaterman__Draft.md](manuscript/chapters/Chapter__3_TheWaterman__Draft.md) before Stage 2 v2 drafting fires. Same edit pattern; lives in Ch 3 revision workstream.

**Phat consent pursuit MOVES TO relationship-pace, not publishing-gate.** Per `feedback_named_subject_consent.md` discipline: anonymization is the safe default; substantive material preserved; name restores in future printings if consent lands later. Outreach package at `research/outreach/subjects/phat/` (`585d535` + `721c094` + `9aee0af`) remains available for whenever the author chooses to use it; no submission timeline pressure.

**Biggie (deceased Fox Hill waterman; ~30+ years deceased) remains named with courtesy-notify-family discipline.** Unchanged.

Noema submission now gated only on the two small content-edits above + author's drafting bandwidth.

---

## 5. Workstream status (by bucket, by priority)

Priority within bucket: **HIGH** = time-pressured or gates large downstream cascade. **MED** = important but not yet gating. **LOW** = small / dormant / waiting.

### 5.1 IN FLIGHT

| # | Pri | Workstream | Status | Next action |
|---|---|---|---|---|
| **20** | **HIGH** | Manuscript Stage-3 Rigor Pass | **Chs 1 + 5 + 6 Stage-3 cycles all CLOSED** (Ch 1 closed 2026-05-19 via Pass 3.3 light re-fire RATIFIED `eb14171`; Chs 5+6 closed 2026-05-14). Ch 4 Pass 2 PROPOSED 2026-05-15. Chs 7+8+9+10 Pass 1 PROPOSED 2026-05-16. See per-chapter detail §6. [handoff](manuscript-stage-3-rigor-pass-handoff_2026-05-11.md) | Ratify Pass 1 findings for Chs 7/8/9/10 + apply Phase C-α; ratify Ch 4 Pass 2 + apply. Chs 1/5/6 now move to Stage 4 + Stage 5. |
| **NEW** | **HIGH** | **Developmental-edit (Pass 3.5) workstream class** (per-chapter; whole-chapter-scale restoration-of-richness) | **Ch 1 RATIFIED + applied 2026-05-18** — 9 spot-fixes (`e69c61e`) + §11 disposition log (`1f5c6ad`) + DMV-commute coda 2026-05-19 (`d36534f`). Codified into pipeline doctrine via **Amendment B** as Pass 3.5 (`316073e`). Chs 2–10 + AuthorsNote pending. [handoff](developmental-edit-workstream-handoff_2026-05-18.md) | Fire **Ch 2 developmental-edit** session next (one per session per branch discipline). |
| **4** | **HIGH** | Outreach pipeline | Sandy packet SENT 2026-05-14; proactive Q0 citation-questions follow-up SENT 2026-05-15. **Both CBF sends VERIFIED SENT Mon May 18 8am ET — v6.1 call-windows (`7141634`) + consolidated advance materials (`b200664`).** **🆕 Val DiMarzio responded 2026-05-19 confirming Thu May 21 2pm meeting** (Microsoft Teams; three-person — Chris + Val + David; Teams link forthcoming from Val). Colden citation-verify packet pre-staged (`15c6b0f`) — user-action. Biggie process guide pre-staged (`164b9e2`). [handoff](outreach-pipeline-handoff_2026-05-09.md) | Block Thu May 21 2pm calendar + prep CBF meeting (dual-state scope: MD + VA). Monitor inbox for Teams link + Sandy reply (window opens Thu). |
| ~~NEW~~ | — | ~~**Pipeline doctrine v1.0.0 retrofits**~~ | **PARTIALLY APPLIED 2026-05-18.** Ch 1 (`3582823`) + Ch 5 (`782e6c9`) + Ch 6 (`5e08642`) + TA (`eb636c6`) retrofits fired (Stage 1a + 1c + Pass 3.4 + Stage 4 triple-render). TA rent-seeking-amendment retrofit also landed (`1e4d242`). **Chs 2/3/4/7/8/9/10 + AuthorsNote + Dedication retrofits remain queued.** Render-pipeline-standardization workstream resolved via canonical-pipeline ratification (`b3f4af5`). | Fire remaining 9 retrofits as bandwidth permits; can run in parallel with Phase C-α + developmental-edit fires. |
| ~~NEW~~ | — | ~~**Render-toolchain canonical pipeline**~~ | **RATIFIED 2026-05-19** (`b3f4af5`). Canonical installer + Dockerfile + CI fixture (`b7e784a`); Remote-container SessionStart hook + CI render-verify workflow (`6ebda00`); docker-render.sh convenience wrapper (`7e88701`). Stage 4 audits unblocked. Render-output policy in place. | Operational. Containerization workstream class continues via [`render-toolchain-containerization-handoff_2026-05-18.md`](render-toolchain-containerization-handoff_2026-05-18.md). |
| ~~NEW~~ | — | ~~**Cross-chapter rent-seeking engagement**~~ | **RATIFIED 2026-05-18.** Four touches APPLIED via `a1e54d9`. Residual follow-ons (mini-rigor-passes, bibliography Buchanan/Tullock, Ch 1 REAUDIT v3 doc state-update, cross-thread-todos entry) deferred per ratification-log §9 of handoff. | Verification reads absorbed into Ch 8+9 Pass 2/3 cycles; bibliography additions fold into Phase A. |

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
- **CBF outreach: v6.1 call-windows + consolidated advance-materials BOTH VERIFIED SENT Mon May 18 8am ET** (`7141634` + `b200664`)
- **CBF meeting CONFIRMED** Thu May 21 2pm ET via Val DiMarzio reply 2026-05-19 — three-person video call (Chris + Val + David Sherfinski; Microsoft Teams; Teams link forthcoming)
- **Cross-chapter rent-seeking engagement workstream RATIFIED + applied** 2026-05-18 (`bc02767` + `a1e54d9`)
- **Pipeline doctrine v1.0.0 Amendment A — selective stage-firing RATIFIED** 2026-05-18 (`f049c0d`)
- **Pipeline-doctrine retrofits Ch 1 + Ch 5 + Ch 6 + TA fired** 2026-05-18 (`3582823` + `782e6c9` + `5e08642` + `eb636c6` + `1e4d242` rent-seeking amendment)
- **Chapter file rename** — all chapters except 2/3 dropped `__Draft` suffix 2026-05-18 (`a09e319`); Chs 2+3 retain pending Stage-3 completion
- **Chapter first-couple-lines render fix** across all chapters 2026-05-18 (`e1a533e`)
- **Ch 1 developmental-edit review RATIFIED + Phase C applied** 2026-05-18 (`1f5c6ad` disposition log + `e69c61e` 9 spot-fixes) + **DMV-commute coda** 2026-05-19 (`d36534f`)
- **Pipeline doctrine v1.0.0 Amendment B — Pass 3.5 developmental-edit RATIFIED** 2026-05-19 (`316073e`)
- **Pipeline doctrine v1.0.0 Amendment C — Interactive Ratification Protocol RATIFIED** 2026-05-19 (`9e68496`)
- **Canonical render-toolchain installer + Dockerfile + CI fixture** 2026-05-19 (`b7e784a`)
- **Remote-container SessionStart hook + CI render-verify workflow** 2026-05-19 (`6ebda00`)
- **Render-toolchain canonical-pipeline RATIFIED + render-output policy** 2026-05-19 (`b3f4af5`)
- **docker-render.sh convenience wrapper** 2026-05-19 (`7e88701`)
- **Ch 1 Pass 3.3 light re-fire RATIFIED** 2026-05-19 (`eb14171`) — verdict: READY-TO-SUBMIT HOLDS WITH CONFIDENCE-LEVEL STRENGTHENING; Ch 1 Stage-3 five-pass cycle now fully CLOSED
- **Darity cross-thread C-2 (Du Bois → bibliography) RATIFIED** by author 2026-05-19 — queue for next bibliography apparatus session
- **Darity cross-thread C-1 (Fogel-Engerman two-volume model → comp-titles) DECLINED** by author 2026-05-19 — out of bibliography scope
- **Decision: Chs 2/3 retain `__Draft` suffix = INTENTIONAL** (2026-05-19) — they may need rewrite depending on consent outcomes; keep `__Draft` until Stage-3 closure

Earlier completions still standing (since 2026-05-10): #8 Path B audit, #9 Apparatus register, #10 Cross-chapter consistency, #11 Comp-titles v0, #13 Flagship terms defense, #15 TA numbering reconciliation.

**Retired:** #7 Manuscript completion (substance migrated to §7 Apparatus 2026-05-13).

---

## 6. #20 Stage-3 Rigor Pass — per-chapter detail

| Ch | Pass 1 (fact-check) | Pass 2 (voice-polish) | Pass 3 (audience-load) | Phase C spot-fixes | **Next action** |
|---|---|---|---|---|---|
| **1** | ✅ COMPLETE | ✅ RATIFIED + APPLIED 2026-05-15 (`7b4aa92`; 10 spot-fixes) | ✅ REAUDIT v3 `76ca8a6` items (i) + (iv) APPLIED (`013415f` + `f692164`); item (iv) actually deferred to pre-pub `ea94684`; line 29 grandfather paragraph applied `54709e7`. **Pass 3.3 light re-fire RATIFIED 2026-05-19** (`eb14171`) — verdict: READY-TO-SUBMIT HOLDS WITH CONFIDENCE-LEVEL STRENGTHENING (40-char: 30 INCLUDE / 0 EXCLUDE; 9 confidence uplifts; 0 discounts; §11.5 chiastic-ellipsis reads as authorial craft). | Pass 3.5 developmental-edit RATIFIED + 9 spot-fixes applied 2026-05-18 (`e69c61e`) + DMV-commute coda 2026-05-19 (`d36534f`) | **✅ Stage-3 five-pass cycle CLOSED 2026-05-19.** Remaining for Ch 1: Stage 4 render + character-integrity audit; Stage 5 sign-off + pre-pub review queue artifact (per pipeline doctrine §4 + §5). |
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

**Pipeline doctrine retrofits (workstream cluster — 2026-05-17; in-progress):**

11 retrofit handoffs at `tools/workstream-handoffs/ch{1-10}-pipeline-retrofit-handoff_2026-05-17.md` + `ta-pipeline-retrofit-handoff_2026-05-17.md` + `authorsnote-pipeline-retrofit-handoff_2026-05-17.md` + `dedication-pipeline-retrofit-handoff_2026-05-17.md` + `pipeline-retrofit-template_2026-05-17.md`. **Fired so far (2026-05-18):** Ch 1 (`3582823`) + Ch 5 (`782e6c9`) + Ch 6 (`5e08642`) + TA (`eb636c6`) + TA rent-seeking-amendment (`1e4d242`). **Remaining (9):** Chs 2/3/4/7/8/9/10 + AuthorsNote + Dedication. Render-pipeline-standardization workstream RESOLVED via canonical-pipeline ratification 2026-05-19 (`b3f4af5`); Stage 4 audits now unblocked.

---

## 8. Decisions pending

- ~~**Pipeline retrofit sequencing.**~~ **IN MOTION 2026-05-18** — 5 retrofits fired (Ch 1 + Ch 5 + Ch 6 + TA + TA rent-seeking amendment); 9 remain (Chs 2/3/4/7/8/9/10 + AuthorsNote + Dedication). Render-pipeline-standardization gate cleared via canonical-pipeline ratification 2026-05-19 (`b3f4af5`).
- ~~**Cross-chapter rent-seeking engagement edits.**~~ **RESOLVED 2026-05-18.** Workstream RATIFIED; four touches applied via `a1e54d9`. Residuals deferred per ratification-log §9.
- ~~**Render-pipeline-standardization canonical-pipeline choice.**~~ **RESOLVED 2026-05-19** (`b3f4af5`). Canonical pipeline ratified; render-output policy in place; docker-render.sh convenience wrapper landed.
- **NEW: Developmental-edit (Pass 3.5) per-chapter fire order for Chs 2–10 + AuthorsNote.** Ch 1 ratified + applied 2026-05-18; pipeline doctrine Amendment B codified Pass 3.5 (`316073e`). Per handoff: one chapter per session per branch discipline. Open question: fire Ch 2 next (sequential), or interleave with Phase C-α applications for Chs 7–10 (which are Stage-3 Pass 1's still PROPOSED)? PM recommendation: **fire Ch 2 dev-edit next** as natural follow-on; Phase C-α applications for Chs 7–10 are independent and can run in parallel.
- ~~**Ch 1 Pass 3.3 light re-fire disposition.**~~ **RESOLVED-RATIFIED 2026-05-19** (`eb14171`). Verdict held: READY-TO-SUBMIT WITH CONFIDENCE-LEVEL STRENGTHENING. Ch 1 Stage-3 five-pass cycle now fully CLOSED.
- ~~**Chapter file rename completeness.**~~ **RESOLVED-INTENTIONAL 2026-05-19.** Author confirmed Chs 2/3 retain `__Draft` because they may need rewrite depending on consent outcomes (Phat / Biggie); pattern is "drop `__Draft` only on Stage-3 closure."
- ~~**Phat consent escalation.**~~ **RESOLVED 2026-05-20 — author ratified anonymization** per `feedback_named_subject_consent.md` discipline. Substantive material preserved; name restores in future printings if consent lands. Consent pursuit moves to relationship-pace, not publishing-gate. Two content-edits remain (Essay B line 136 + Ch 3 v1 draft) — see §4.
- **Sandy reply triage protocol.** Reply window opens Thu May 21 (1 week post-send). If no acknowledgment by then, soft check-in. If reply lands earlier, follow P2 #12 triage in mobile dashboard.
- **TA per-chapter call-site audit timing.** Now that v2.1.0 is published + per-chapter Pass 1's are all PROPOSED, the TA call-site audit can fold into Phase C-α applications for Chs 7–10 rather than waiting for a separate Apparatus Phase A run.
- **Boston Review essay fire.** Ch 5 source chapter now stable. Worth scheduling Boston Review pitch + essay drafting before #16 ($100 Barrel) Session 2 since it has the more direct chapter→essay path. Either order works; just be explicit about which fires when.

---

## 9. Date-anchored action list

### Mon May 18 — COMPLETED
- [x] **8:00 AM ET** — CBF reply v6.1 auto-sent (`7141634`). **VERIFIED SENT by author.**
- [x] Cross-chapter rent-seeking engagement workstream RATIFIED + applied (`bc02767` + `a1e54d9`)
- [x] Pipeline doctrine Amendment A RATIFIED (`f049c0d`)
- [x] Pipeline retrofits Ch 1 + 5 + 6 + TA fired (`3582823` + `782e6c9` + `5e08642` + `eb636c6` + `1e4d242`)
- [x] Chapter file rename — Chs 1/4/5/6/7/8/9/10 dropped `__Draft` (`a09e319`); Chs 2/3 retained
- [x] Ch 1 developmental-edit review RATIFIED + 9 spot-fixes applied (`1f5c6ad` + `e69c61e`)

### TODAY Tue May 19
- [x] **Ch 1 Pass 3.3 light re-fire RATIFIED** (`eb14171`) — Stage-3 five-pass cycle CLOSED for Ch 1
- [x] **Darity C-2 (Du Bois → bibliography) RATIFIED** — queue for next bibliography session
- [x] **Darity C-1 (Fogel-Engerman → comp-titles) DECLINED** — out of bibliography scope
- [x] **Chapter rename pattern confirmed INTENTIONAL** — Chs 2/3 retain `__Draft` pending Stage-3 closure
- [ ] Triage Chs 7/8/9/10 Pass 1 findings (start with Ch 8's 4 HIGH items)
- [ ] Decide Ch 2 developmental-edit fire timing (recommend: fire next)
- [ ] Generate paste-text for Boston Review essay + $100 Barrel essay → PW + Atlantic Ideas essay (delivered to author in chat)

### Tomorrow Wed May 20
- Continue Chs 7/8/9/10 ratification + Phase C-α apply
- Ratify Ch 4 Pass 2 + apply spot-fixes
- ~~Decide Phat consent escalation deadline~~ — **RESOLVED 2026-05-20:** anonymization ratified; consent pursuit at relationship-pace

### 🆕 Thu May 21
- **2:00 PM ET — CBF Microsoft Teams meeting** — three-person (Chris + Val + David). **Teams link received Tue May 19; add to calendar.** Prep: review `research/outreach/subjects/cbf/{interview-prep,live-call-companion,organizational-brief}_*.md` with dual-state scope (MD-Colden + VA-Moore).
- Sandy reply window opens (1 week post-packet); soft check-in only if silent.

### This week (by Sun May 24)
- **Thu May 21** — Sandy reply window opens (1 week post-send); soft check-in only if silence
- Fire **Ch 2 developmental-edit** session (next in workstream class)
- Fire **Ch 2 Pass 3** (paste-text from PM)
- Fire **Ch 3 Pass 2** + **Ch 3 Pass 3** (paste-text from PM)
- Fire **Ch 4 Pass 3** (after Ch 4 Pass 2 spot-fixes apply)
- Continue Chs 7/8/9/10 cycles toward Pass 2 trigger
- Continue remaining pipeline retrofits (9 of 14 remain: Chs 2/3/4/7/8/9/10 + AuthorsNote + Dedication)

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
- ~~**Darity cross-thread C-1** Fogel-Engerman two-volume model → #14 comp-titles~~ **DECLINED by author 2026-05-19** — does not belong in bibliography
- **Darity cross-thread C-2** Du Bois → bibliography — **RATIFIED by author 2026-05-19**; apply at next bibliography apparatus session
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
| 4 | Atlantic Ideas vs. PW slot-3 venue | Publishing strategy | Future essay slot-3 | **RESOLVED 2026-05-19 — BOTH FIRE.** Author kicked off $100 Barrel → PW + Atlantic Ideas (Ch 9-derived) in parallel; no slot-3 conflict. |
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

**This dashboard has been running 2026-05-13 → 2026-05-19 (6 calendar days; ~90+ commits landed; 2 successor PM sessions inherited from this file).** Phase-shift triggers fired:
- ✅ Major event: Darity interview + synthesis + packet send
- ✅ Major event: Sandy citations follow-up
- ✅ Major chapter completions: Ch 5 + Ch 6 cycles CLOSED; Ch 1 Pass 2 applied; Ch 1 developmental-edit RATIFIED + applied; Ch 1 DMV-commute coda applied
- ✅ Major infrastructure: Pipeline doctrine v1.0.0 + Amendments A/B/C + invariant gates + 14 retrofit handoffs (5 fired)
- ✅ Major infrastructure: Render-toolchain canonical pipeline RATIFIED; CI render-verify workflow live
- ✅ Major doctrinal: developmental-edit (Pass 3.5) workstream class proposed + first session RATIFIED + codified into Stage 3
- ✅ Major event: Memory migration applied (mirroring to `tools/memory/`)
- ✅ All Chs 7/8/9/10 Pass 1 fired
- ✅ Chapter file rename (Chs 1/4–10 dropped `__Draft`; Chs 2/3 retain)

**Strong recommendation: wrap this PM session and start a fresh one** orienting against this handoff. The next session's natural focus: Phase C-α applications for Chs 7/8/9/10 + Ch 2–10 developmental-edit fires + remaining 9 pipeline retrofits + Sandy reply triage when it lands + Aeon submission countdown (Sun May 31).

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

## 17. Pipeline doctrine v1.0.0 — RATIFIED 2026-05-17 + Amendments A/B/C

**Base doctrine** (`3e31d9d` + `935633e` + `ed5f6cf`): `tools/commons_bonds_pipeline_doctrine_v1.0.0.md` + stage docs (`stage_1`, `stage_4`, `stage_5`). Invariant-gate infrastructure: `.github/workflows/corpus-invariants.yml` + `tools/scripts/check-corpus-invariants.sh` + `tools/scripts/install-pre-commit-hook.sh` + `tools/quality-gates/` (regressed-patterns.yaml, scaffolding-patterns.yaml, render-baselines/build-environment.yaml).

**Amendments ratified since base doctrine:**
- **Amendment A — selective stage-firing** (`f049c0d`, 2026-05-18). Stages fire only when triggers fire; token-economy note in per-pass artifacts.
- **Amendment B — Pass 3.5 developmental-edit codified** (`316073e`, 2026-05-19). Per-chapter whole-chapter-scale developmental-edit review folded into Stage 3 as Pass 3.5. Catches what per-paragraph Pass 3.2 voice-polish misses (emotional arc, scene-anchor density, sensory-detail restoration, reader engagement at analytical pivots).
- **Amendment C — Interactive Ratification Protocol** (`9e68496`, 2026-05-19). Standard for author-Claude ratification cadence within rigor-pass sessions.

**Render-toolchain canonical pipeline RATIFIED** 2026-05-19 (`b3f4af5`). Canonical installer + Dockerfile + CI fixture (`b7e784a`); Remote-container SessionStart hook + CI render-verify workflow (`6ebda00`); docker-render.sh convenience wrapper (`7e88701`). Stage 4 audits now unblocked. Older laptop scripts (`build-derivatives.sh` / `-alt.sh`) superseded by canonical Docker pipeline.

**Retrofit progress:** 5 of 14 retrofits fired 2026-05-18 (Ch 1, Ch 5, Ch 6, TA, TA rent-seeking-amendment). 9 remain: Chs 2/3/4/7/8/9/10 + AuthorsNote + Dedication.

---

## 18. Outreach pipeline detail

| Subject | Affiliation | Status | Date | Notes |
|---|---|---|---|---|
| **William ("Sandy") Darity Jr.** | Duke | **PACKET SENT + Q0 follow-up SENT** | 2026-05-14 + 2026-05-15 | Awaiting response. Reply window opens Thu May 21. |
| **Val DiMarzio + David Sherfinski (CBF)** | CBF MD + VA | **🆕 MEETING CONFIRMED Thu May 21 2pm (Microsoft Teams)** — Val replied 2026-05-19 "Thursday at 2pm would work best for us. I will send over a Teams link." | Reply 2026-05-19; meeting Thu May 21 2pm | **Both CBF sends VERIFIED SENT Mon May 18 8am ET** — v6.1 call-windows (`7141634`) + consolidated advance materials (`b200664`). **Three-person video call: Chris + Val + David** (confirmed joint attendance). Prep scope spans both MD + VA sides. Val + David have had advance materials since Mon. |
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

**Pipeline doctrine artifacts (2026-05-17 base + Amendments A/B/C through 2026-05-19):**
- `tools/commons_bonds_pipeline_doctrine_v1.0.0.md` + stage docs
- `tools/quality-gates/` registries
- `tools/scripts/` (check-corpus-invariants + install-pre-commit-hook + session-start-render-toolchain + render-verify-fixtures/)
- `.github/workflows/corpus-invariants.yml` + render-verify workflow
- `tools/workstream-handoffs/developmental-edit-workstream-handoff_2026-05-18.md` (Pass 3.5 workstream class)
- `tools/workstream-handoffs/render-toolchain-containerization-handoff_2026-05-18.md`
- `tools/rigor-passes/ch1_developmental_edit_review_2026-05-18.md` (first Pass 3.5 session)
- Canonical render-toolchain: Dockerfile + installer + docker-render.sh convenience wrapper

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
