# Project Management Session — Handoff (2026-05-18, v2.0 dashboard structure)

> **🟡 SUPERSEDED 2026-05-24 by [`pm-session-handoff_2026-05-24.md`](pm-session-handoff_2026-05-24.md).** Retained as audit-trail for the 2026-05-18 → 2026-05-23 session window (refresh `aa04a4a` 2026-05-21 captured Phat anonymization + Ch 3 augmentation + Aeon Pass 3.1 + Chs 7/8/9 Phase C applications).

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
| ~~Mon May 18 8am ET — CBF v6.1 auto-send~~ | DONE — both VERIFIED SENT |
| ~~Tue May 19 + Wed May 20~~ | DONE — Phat anonymization RATIFIED + applied across Ch 3 v1 + Noema Essay B; Ch 3 augmentation Stage 1 brief RATIFIED + Stage 2 landed (11 named voices); Aeon Pass 3.1 RATIFIED + applied; Ch 7 Pass 1 RATIFIED + Phase C applied; Ch 8 Pass 1 Phase C applied; Ch 9 Pass 1 Phase C applied; live-call-companion refreshed; cross-corpus IPG construction RATIFIED |
| **🔴 TODAY Thu May 21** | **(1) 2:00 PM ET — CBF MEETING** (Microsoft Teams; Chris + Val + David; Teams link in inbox). Prep at [`research/outreach/subjects/cbf/live-call-companion_2026-05-21_thursday-meeting.html`](../../research/outreach/subjects/cbf/live-call-companion_2026-05-21_thursday-meeting.html) — refreshed 2026-05-20 (`bb61fa1`). **(2) Sandy reply window opens** (1 week post-packet; soft check-in only if silence). **(3) Ratification queue is the day's other anchor** — 8 PROPOSED rigor-pass artifacts await disposition; see §5.1 + §6. |
| **This week (by Sun May 24)** | Work through the ratification queue: Ch 6 Pass 3.5 dev-edit; Ch 3 v1 step-back KEEP/REPLACE; Ch 3 Pass 3.2; Ch 4 Pass 2; Ch 7 Pass 2; Ch 9 Pass 2; Aeon Pass 3.2; Noema Pass 3.1 (apply spot-fixes then SUBMIT). Continue Chs 8/10 toward Pass 2 trigger. Continue pipeline retrofits (Chs 2/3/4/7/8/9/10 + AuthorsNote + Dedication still pending). |
| **Sun May 31** | **Aeon Version C submission** (14:01 UTC = Mon Jun 1 ~00:01 AEST). Pre-submission verify Fri May 29. |

---

## 3. Critical path bottleneck

**Critical path is now THE RATIFICATION QUEUE.** Most chapter rigor cycles are in flight; what gates progress is author disposition on the ~9 PROPOSED artifacts (Ch 6 Pass 3.5; Ch 3 Pass 3.2 + v1 step-back; Ch 4 Pass 2; Ch 7 Pass 2; Ch 9 Pass 2; Ch 10 Pass 1; Aeon Pass 3.2; Noema Pass 3.1). Each ratification unlocks a Phase C spot-fix application; cumulative cadence is what gates the book proposal sprint (late June) and the Aeon deadline (Sun May 31).

**Infrastructure now mostly resolved.** Render-toolchain canonical pipeline RATIFIED 2026-05-19 (`b3f4af5`); render-output policy in place; docker-render.sh convenience wrapper landed (`7e88701`); CI render-verify workflow active (`6ebda00`). **Stage 4 audits unblocked.** Pipeline retrofits for Ch 1 + Ch 5 + Ch 6 + TA fired 2026-05-18; Chs 2/3/4/7/8/9/10 + AuthorsNote + Dedication retrofits still queued.

Apparatus Phase A (Bibliography / Glossary / TA per-chapter call-site verification) still gated on chapter-level Stage-3 completion — most chapters now far enough along that this gate is becoming visible.

---

## 4. USER ACTIONS

~~Three USER ACTIONS gating Noema (2026-05-13)~~ → ~~Two anonymization edits (2026-05-20)~~ → **🟢 NOEMA SUBMISSION CLEARED 2026-05-21.**

- [x] **Phat anonymization RATIFIED 2026-05-20** (`12caa26`) — applied across Ch 3 v1 (`8a55395`) + Noema Essay B (`2815433`) + memory + tracking artifacts.
- [x] **Noema Essay B step-back replacement-analysis RATIFIED 2026-05-21** — verdict **KEEP anonymized + SUBMIT NOW** (`3e17ef7`).
- [ ] **Open: Apply Noema Pass 3.1 fact-check spot-fixes** (PROPOSED `b7fbc92`) → then submit. The fact-check artifact is the last gate before the essay leaves the building.
- [ ] **Open: Ch 3 v1 step-back replacement-analysis** PROPOSED `8e3bf25` — disposition pending (KEEP anonymized vs REPLACE with named public-record subject). Not a publishing gate (Ch 3 is book-track, not essay-track) but feeds Stage 2 v2 drafting.
- [ ] **Open: Send Colden citation-verify packet** (pre-staged `15c6b0f`; user-action; timing flexible).

**Phat consent pursuit at relationship-pace; no publishing-timeline pressure.** Outreach package at `research/outreach/subjects/phat/` remains available; name restores in future printings if consent lands. **Biggie** remains named with courtesy-notify-family discipline.

---

## 5. Workstream status (by bucket, by priority)

Priority within bucket: **HIGH** = time-pressured or gates large downstream cascade. **MED** = important but not yet gating. **LOW** = small / dormant / waiting.

### 5.1 IN FLIGHT

| # | Pri | Workstream | Status | Next action |
|---|---|---|---|---|
| **20** | **HIGH** | Manuscript Stage-3 Rigor Pass | **Chs 1 + 5 + 6 four-pass cycles CLOSED.** Ch 6 Pass 3.5 PROPOSED 2026-05-20 (`838a3f2`) — ratification pending. Ch 2 Pass 3 ratification rev landed (`f4ee16b` — pivot placeholders to published-record; cut #3). Ch 3 Pass 3.2 PROPOSED 2026-05-20 (`1d9c5ad`). Ch 4 Pass 2 PROPOSED `3174cc8` still awaiting ratification. Ch 7 Pass 1 RATIFIED + Phase C applied (`4987e59`, `4948dbb`); Pass 2 PROPOSED (`6f54514`). Ch 8 Pass 1 Phase C applied (`5fe6af6`). Ch 9 Pass 1 Phase C applied (`4c8bc02`); Pass 2 PROPOSED (`e68b505`). Ch 10 Pass 1 v1.0.1 refresh (`e026d5f`) still PROPOSED. See per-chapter detail §6. [handoff](manuscript-stage-3-rigor-pass-handoff_2026-05-11.md) | **Work the ratification queue** (8+ PROPOSED items). Apply spot-fixes as ratifications land. |
| **NEW** | **HIGH** | **Developmental-edit (Pass 3.5) workstream class** | **Ch 1 RATIFIED + applied 2026-05-18.** **Ch 6 PROPOSED 2026-05-20** (`838a3f2`) — first non-Ch-1 chapter; ratification pending. Codified via Amendment B (`316073e`). Chs 2/3/4/5/7-10 + AuthorsNote pending. [handoff](developmental-edit-workstream-handoff_2026-05-18.md) | **Ratify Ch 6 Pass 3.5 + apply.** Then queue next chapter (PM rec: Ch 5 next since cycle CLOSED; or Ch 2 per original sequence). |
| **NEW** | **HIGH** | **Ch 3 augmentation workstream** (post-petition voice-inventory integration) | **Stage 1 brief RATIFIED 2026-05-20** (`b8806fa`); **Stage 2 LANDED 2026-05-20** (`9a7cc7e` — 11 named voices placed across 9 chapter locations). Bay-cap chronology fact-check spot-fix bundled (`6785646`). G1-G10 bibliography scribe pass complete (`134b888` — Stage 1c HOLD resolved). | Ch 3 now ready for full Stage 3 four-pass cycle. Pass 3.2 already PROPOSED — see Workstream 20 row. |
| **4** | **HIGH** | Outreach pipeline | Sandy packet SENT 2026-05-14; CBF advance materials SENT Mon May 18; **CBF meeting TODAY 2pm ET** (Teams link in inbox). Live-call-companion refreshed 2026-05-20 (`bb61fa1`). Colden citation-verify packet pre-staged. Biggie process guide pre-staged. [handoff](outreach-pipeline-handoff_2026-05-09.md) | **EXECUTE CBF meeting at 2pm.** Sandy reply window opens today — soft check-in only if silence by EOD. |
| ~~NEW~~ | — | ~~**Pipeline doctrine v1.0.0 retrofits**~~ | **PARTIALLY APPLIED 2026-05-18.** Ch 1 (`3582823`) + Ch 5 (`782e6c9`) + Ch 6 (`5e08642`) + TA (`eb636c6`) retrofits fired (Stage 1a + 1c + Pass 3.4 + Stage 4 triple-render). TA rent-seeking-amendment retrofit also landed (`1e4d242`). **Chs 2/3/4/7/8/9/10 + AuthorsNote + Dedication retrofits remain queued.** Render-pipeline-standardization workstream resolved via canonical-pipeline ratification (`b3f4af5`). | Fire remaining 9 retrofits as bandwidth permits; can run in parallel with Phase C-α + developmental-edit fires. |
| ~~NEW~~ | — | ~~**Render-toolchain canonical pipeline**~~ | **RATIFIED 2026-05-19** (`b3f4af5`). Canonical installer + Dockerfile + CI fixture (`b7e784a`); Remote-container SessionStart hook + CI render-verify workflow (`6ebda00`); docker-render.sh convenience wrapper (`7e88701`). Stage 4 audits unblocked. Render-output policy in place. | Operational. Containerization workstream class continues via [`render-toolchain-containerization-handoff_2026-05-18.md`](render-toolchain-containerization-handoff_2026-05-18.md). |
| ~~NEW~~ | — | ~~**Cross-chapter rent-seeking engagement**~~ | **RATIFIED 2026-05-18.** Four touches APPLIED via `a1e54d9`. Residual follow-ons (mini-rigor-passes, bibliography Buchanan/Tullock, Ch 1 REAUDIT v3 doc state-update, cross-thread-todos entry) deferred per ratification-log §9 of handoff. | Verification reads absorbed into Ch 8+9 Pass 2/3 cycles; bibliography additions fold into Phase A. |

### 5.2 READY TO FIRE

| # | Pri | Workstream | Status | Fire window |
|---|---|---|---|---|
| **🟢 NOEMA** | **HIGH** | Noema essay | Phat anonymization applied (`2815433`); replacement-analysis RATIFIED KEEP+SUBMIT (`3e17ef7`); **Pass 3.1 fact-check PROPOSED `b7fbc92`** — last gate. | Apply Pass 3.1 spot-fixes → submit. No external deadline; submit when fact-check applies. |
| **1** | **HIGH** | Aeon pitch | Version C Pass 3.1 RATIFIED + APPLIED 2026-05-20 (`8b2ae31`); §4.1 cascade scan executed (`3e54015`); **Pass 3.2 voice-polish PROPOSED 2026-05-21 (`c722bb6`)**. [handoff](aeon-submission-handoff_2026-05-09.md) | Ratify Pass 3.2 + apply. **Submit Sun May 31 14:01 UTC**; pre-submission verify by Fri May 29. |
| **16** | MED | $100 Barrel essay → Phenomenal World | **Stage 1 brief RATIFIED 2026-05-19** (`53db177`); **Stage 2 audience-blind flow draft LANDED 2026-05-19** (`74953b9`). [handoff](100-barrel-essay-handoff_2026-05-11.md) | Fire Stage 3 four-pass cycle when bandwidth permits. |
| **2** | MED | Boston Review essay | UNBLOCKED 2026-05-10. **Source chapter (Ch 5) stable** — three-pass cycle CLOSED. [handoff](boston-review-essay-handoff_2026-05-09.md) | Draft pitch + essay (~4,500w from Ch 5). When bandwidth permits. |
| **14** | MED | Comp-titles deep matrix Phase 2 | Just-in-time verification deferred from #11. | Early-to-mid July 2026 (2–3wk before Wave 1). |

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

**Batch added 2026-05-19 / 05-20 / 05-21:**

- **Phat anonymization RATIFIED + applied across artifacts** (`12caa26`) + Ch 3 v1 (`8a55395`) + Noema Essay B (`2815433`); memory mirrors + tracking artifacts updated
- **Ch 3 v1 Phat-anonymization replacement-analysis PROPOSED** (`8e3bf25`; propose-only) — awaiting ratification
- **Noema Essay B Part B replacement analysis PROPOSED → RATIFIED** verdict **KEEP anonymized + SUBMIT NOW** (`0662408` + `3e17ef7`)
- **Ch 3 augmentation workstream**: Stage 1 brief PROPOSED → RATIFIED (`7628fe1` + `b8806fa`); Stage 2 LANDED (`9a7cc7e` — 11 named voices across 9 chapter locations); Bay-cap chronology fact-check bundled (`6785646`); G1-G10 bibliography scribe pass (`134b888`) — Stage 1c HOLD resolved
- **Ch 3 Pass 3.2 voice-polish PROPOSED** 2026-05-20 (`1d9c5ad`)
- **Ch 6 Pass 3.5 developmental-edit PROPOSED** 2026-05-20 (`838a3f2`) — first non-Ch-1 chapter in the dev-edit workstream class
- **Ch 7 Pass 1 RATIFIED + Phase C-α applied** 2026-05-20 (`4948dbb` ratification record + `4987e59` 7 spot-fixes); **Pass 2 PROPOSED** 2026-05-21 (`6f54514`)
- **Ch 8 Pass 1 Phase C applied** 2026-05-21 (`5fe6af6` — 16 Ch 8 + 1 Ch 2 + 1 Ch 6 + 5 inventory rows)
- **Ch 9 Pass 1 Phase C applied** (`4c8bc02` — 12 prose + 2 cross-corpus); **Pass 2 PROPOSED** (`e68b505`)
- **Ch 10 Pass 1 v1.0.1 refresh** (`e026d5f`) — re-anchored against current state
- **Ch 2 Pass 3 ratification rev landed** (`f4ee16b` — pivot placeholders #1+#2 to published-record; cut #3); Phase C-δ research inventory (`f5c4b71`)
- **Aeon pitch Version C**: Pass 3.1 PROPOSED → RATIFIED + APPLIED (`0142107` + `8b2ae31`); §4.1 cascade scan EXECUTED + 4 artifacts patched (`3e54015`); Pass 3.2 voice-polish PROPOSED (`c722bb6`)
- **Noema essay Pass 3.1 fact-check PROPOSED** 2026-05-19 (`b7fbc92`)
- **$100 Barrel essay → Phenomenal World**: Stage 1 brief PROPOSED → RATIFIED (`5cf5913` + `53db177`); Stage 2 audience-blind flow draft LANDED (`74953b9`)
- **Cross-corpus IPG canonical-construction artifact RATIFIED** (Option D — `f3def8a` + `57575b1`) — Ch 8 Pass 1 HIGH-3 follow-on resolved
- **Memory mirrors + scaffolding desc synced to Stage 3 five-pass** (`0be3a86`) — v3.1 Amendment B doctrine update reflected in mirrors
- **CBF live-call-companion refreshed** 2026-05-20 (`bb61fa1`) — post-Phat-ratification + post-petition-expansion posture
- **TA pre-pub queue note**: §1.1 Definition 1.1 notation legibility flagged for Sandy/publisher trigger (`9e2ef55`)
- **Ch 7 + Ch 8 Pass 1 artifact refreshes** for path + line-number drift post-rename (`e21b50a` + `dbef561`)

Earlier completions still standing (since 2026-05-10): #8 Path B audit, #9 Apparatus register, #10 Cross-chapter consistency, #11 Comp-titles v0, #13 Flagship terms defense, #15 TA numbering reconciliation.

**Retired:** #7 Manuscript completion (substance migrated to §7 Apparatus 2026-05-13).

---

## 6. #20 Stage-3 Rigor Pass — per-chapter detail

| Ch | Pass 1 | Pass 2 | Pass 3 | Pass 3.5 | **Next action (priority)** |
|---|---|---|---|---|---|
| **1** | ✅ | ✅ | ✅ | ✅ APPLIED | **✅ Stage-3 CLOSED 2026-05-19.** Remaining: Stage 4 + Stage 5 sign-off + pre-pub review queue artifact. |
| **2** | ✅ | ✅ | ✅ Pass 3 ratification rev `f4ee16b` (placeholders → published) | — | Apply Pass 3 rev + close cycle; queue Pass 3.5 |
| **3** | ✅ LANDED `2f76e37` + Bay-cap chronology spot-fix `6785646` + augmentation Stage 2 (`9a7cc7e`) + G1-G10 bib `134b888` + Phat anonymization `8a55395` | **🔴 PROPOSED `1d9c5ad`** 2026-05-20 | — | — | **Ratify Pass 3.2 + apply; ratify v1 step-back KEEP/REPLACE `8e3bf25`; fire Pass 3 (audience-load)** |
| **4** | ✅ | **🔴 PROPOSED `3174cc8`** | — | — | **Ratify Pass 2 + apply spot-fixes (5M + 2L already in)** |
| **5** | ✅ | ✅ | ✅ | — | Cycle CLOSED. Queue Pass 3.5. No further work unless Sandy reply surfaces revisions. |
| **6** | ✅ | ✅ | ✅ + Pass 3.4 retrofit `5e08642` | **🔴 PROPOSED `838a3f2`** 2026-05-20 | **Ratify Pass 3.5 + apply Phase C** (first non-Ch-1 dev-edit) |
| **7** | ✅ RATIFIED + Phase C applied (`4948dbb` + `4987e59` 7 spot-fixes) | **🔴 PROPOSED `6f54514`** 2026-05-21 | — | — | **Ratify Pass 2 + apply; fire Pass 3** |
| **8** | ✅ Phase C applied (`5fe6af6` — 16 Ch 8 edits + cross-corpus IPG canonical-construction `57575b1`); $44B drift fixed | — | — | — | **Fire Pass 2** |
| **9** | ✅ Phase C applied (`4c8bc02` — 12 prose + 2 cross-corpus) | **🔴 PROPOSED `e68b505`** | — | — | **Ratify Pass 2 + apply; fire Pass 3** |
| **10** | **🔴 PROPOSED `c85c41d`** (v1.0.1 refresh `e026d5f`) | — | — | — | **Ratify Pass 1 + apply Phase C-α**; bidirectional-reach already in (`376eb3c`) |

**🔴 ratification queue this week:** Ch 6 Pass 3.5 + Ch 3 Pass 3.2 + Ch 3 v1 step-back + Ch 4 Pass 2 + Ch 7 Pass 2 + Ch 9 Pass 2 + Ch 10 Pass 1 + Aeon Pass 3.2 + Noema Pass 3.1 = **9 PROPOSED artifacts awaiting disposition.**

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
- ~~**Developmental-edit (Pass 3.5) per-chapter fire order**~~ — **IN MOTION:** Ch 6 Pass 3.5 PROPOSED 2026-05-20 (`838a3f2`) ahead of Ch 2 (out of original sequence; consistent with workstream-class flexibility). Ratify + apply, then next: PM rec is now Ch 5 (cycle CLOSED) or Ch 2 (PM's original rec; deferred while Ch 6 fired ahead).
- ~~**Ch 1 Pass 3.3 light re-fire disposition.**~~ **RESOLVED-RATIFIED 2026-05-19** (`eb14171`). Verdict held: READY-TO-SUBMIT WITH CONFIDENCE-LEVEL STRENGTHENING. Ch 1 Stage-3 five-pass cycle now fully CLOSED.
- ~~**Chapter file rename completeness.**~~ **RESOLVED-INTENTIONAL 2026-05-19.** Author confirmed Chs 2/3 retain `__Draft` because they may need rewrite depending on consent outcomes (Phat / Biggie); pattern is "drop `__Draft` only on Stage-3 closure."
- ~~**Phat consent escalation.**~~ **RESOLVED 2026-05-20 — author ratified anonymization** per `feedback_named_subject_consent.md` discipline. Substantive material preserved; name restores in future printings if consent lands. Consent pursuit moves to relationship-pace, not publishing-gate. Two content-edits remain (Essay B line 136 + Ch 3 v1 draft) — see §4.
- **Sandy reply triage protocol.** Reply window OPENS TODAY (Thu May 21). Soft check-in only if EOD silence. If reply lands, follow P2 #12 triage in mobile dashboard.
- **NEW: Ch 3 v1 Phat-anonymization step-back disposition** (`8e3bf25` PROPOSED 2026-05-20). KEEP anonymized in-place vs REPLACE with named public-record subject. Noema verdict was KEEP — same logic likely applies to Ch 3, but author ratification needed.
- **NEW: Noema submission posture** — Pass 3.1 fact-check spot-fixes (`b7fbc92`) apply first, then submit? Or submit at-state? KEEP+SUBMIT verdict (`3e17ef7`) implies apply-then-submit; confirm before firing.
- **NEW: Stage 5 (academic-rigor + prose-quality sign-off + pre-pub review queue artifact) template.** Ch 1 is the first chapter to reach this gate (five-pass cycle CLOSED 2026-05-19). No chapter has run Stage 5 yet; first chapter through needs to also build the template. Defer or schedule?
- **TA per-chapter call-site audit timing.** TA call-site audit can fold into Phase C applications for Chs 7-10 (now mostly underway) rather than waiting for a separate Apparatus Phase A run.
- **Boston Review essay fire.** Ch 5 source chapter stable. Worth scheduling Boston Review pitch + essay drafting in late May / early June after Aeon submission and Noema clears.

---

## 9. Date-anchored action list

### Mon May 18 — COMPLETED
- [x] **8:00 AM ET** — CBF reply v6.1 auto-sent (`7141634`). **VERIFIED SENT by author.**
- [x] Cross-chapter rent-seeking engagement workstream RATIFIED + applied (`bc02767` + `a1e54d9`)
- [x] Pipeline doctrine Amendment A RATIFIED (`f049c0d`)
- [x] Pipeline retrofits Ch 1 + 5 + 6 + TA fired (`3582823` + `782e6c9` + `5e08642` + `eb636c6` + `1e4d242`)
- [x] Chapter file rename — Chs 1/4/5/6/7/8/9/10 dropped `__Draft` (`a09e319`); Chs 2/3 retained
- [x] Ch 1 developmental-edit review RATIFIED + 9 spot-fixes applied (`1f5c6ad` + `e69c61e`)

### Tue May 19 — DONE
- [x] Ch 1 Pass 3.3 light re-fire RATIFIED (`eb14171`) — Stage-3 five-pass cycle CLOSED for Ch 1
- [x] Darity C-2 (Du Bois → bibliography) RATIFIED; Darity C-1 DECLINED
- [x] $100 Barrel Stage 1 brief PROPOSED + RATIFIED (`5cf5913` + `53db177`); Stage 2 LANDED (`74953b9`)
- [x] Ch 9 Pass 1 Phase C applied (`4c8bc02`)
- [x] Noema essay Pass 3.1 fact-check PROPOSED (`b7fbc92`)
- [x] Aeon pitch Pass 3.1 PROPOSED (`0142107`)

### Wed May 20 — DONE
- [x] **Phat anonymization RATIFIED + applied across all artifacts** (`12caa26` + `8a55395` + `2815433`)
- [x] **Ch 3 augmentation workstream Stage 1 RATIFIED + Stage 2 LANDED** (`b8806fa` + `9a7cc7e` — 11 named voices); Bay-cap chronology fix (`6785646`); G1-G10 bibliography (`134b888`)
- [x] **Ch 3 Pass 3.2 voice-polish PROPOSED** (`1d9c5ad`)
- [x] **Ch 6 Pass 3.5 developmental-edit PROPOSED** (`838a3f2`)
- [x] **Ch 7 Pass 1 RATIFIED + Phase C applied** (`4948dbb` + `4987e59`)
- [x] **Aeon pitch Pass 3.1 RATIFIED + APPLIED + §4.1 cascade** (`8b2ae31` + `3e54015`)
- [x] **Replacement analyses PROPOSED for Ch 3 v1 + Noema** (`8e3bf25` + `0662408`)
- [x] **CBF live-call-companion refreshed** for today's meeting (`bb61fa1`)

### 🔴 TODAY Thu May 21
- [x] **Noema Essay B step-back RATIFIED — KEEP + SUBMIT** (`3e17ef7`)
- [x] Cross-corpus IPG canonical-construction RATIFIED (`57575b1`); Ch 8 Pass 1 Phase C applied (`5fe6af6`)
- [x] Ch 7 Pass 2 voice-polish PROPOSED (`6f54514`)
- [x] Aeon Pass 3.2 voice-polish PROPOSED (`c722bb6`)
- [ ] **🔴 2:00 PM ET — CBF Microsoft Teams meeting** (three-person; Teams link in inbox). Prep at [`live-call-companion_2026-05-21_thursday-meeting.html`](../../research/outreach/subjects/cbf/live-call-companion_2026-05-21_thursday-meeting.html).
- [ ] **Sandy reply window opens** — soft check-in only if EOD silence.
- [ ] **Begin ratification queue** (9 PROPOSED items — see §6): start with whichever you have head-space for; recommend Ch 6 Pass 3.5 first (newest, isolated chapter; sets dev-edit cadence) or Ch 3 v1 step-back (smallest decision; clears the Ch 3 path).

### This week (by Sun May 24)
- Work through ratification queue (see §6) — 9 PROPOSED items
- Apply Noema Pass 3.1 spot-fixes → **SUBMIT NOEMA**
- Continue pipeline retrofits (Chs 2/3/4/7/8/9/10 + AuthorsNote + Dedication still pending)
- Queue next Pass 3.5 dev-edit fire (recommend Ch 5 — CLOSED cycle, clean precedent)

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
| **Mariana Mazzucato** | UCL/IIPP | **DECLINED via Adam Albrecht; acknowledgment reply SENT** | 2026-05-21 | "Existing work commitments at this stage" — standard polite decline. Gracious close-out sent same day (preserves relationship; door open for post-publication courtesy copy via Adam's office). Pattern 2 cite via published work unaffected; cross-thread #1 resolution path (c) closes. |
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
