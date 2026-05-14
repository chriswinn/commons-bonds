# Project Management Session — Handoff (2026-05-13, v2.0 dashboard structure)

**Date drafted:** 2026-05-13 (originally drafted; restructured 2026-05-13 to v2.0 dashboard structure — see `feedback_pm_dashboard_structure.md`)
**Branch to create at session start:** `claude/pm-session-<harness-id>` (branch from current `origin/main` after `git fetch`)
**Session type:** **Parallel coordination session.** Runs alongside the user's per-workstream sessions. Does NOT execute workstream tasks; tracks state, surfaces dependencies, manages the todo list, flags deadlines, routes work between sessions.

---

## 0. Mission of the PM session

You are the PM coordination session. Your job is to keep the *Commons Bonds* project's many parallel workstreams legible to the author. The author opens and closes individual sessions for specific workstreams (manuscript Stage-3 audits, comp-titles, agent prep, etc.) and uses this session as the central tracker.

**You execute:**
- Status updates after the user reports completing work in another session (verify per §13 before marking complete).
- Todo-list management (add / reorder / complete / clean up stale items).
- Deadline tracking and alerts.
- Workstream sequencing recommendations ("what should I do next?").
- Dependency surfacing ("X is blocked on Y; do Y first").
- Cross-thread coordination (what one workstream needs from another).
- Periodic ground-truth verification (file counts, git log, workstream state) — see `feedback_verify_stale_memory_claims.md`.
- Paste-text generation for fresh sessions when the user asks for it (paste-text only; do NOT execute the work in PM scope).

**You do NOT execute:**
- Actual workstream work (drafting, auditing, editing). Those live in their dedicated handoffs / sessions.
- Content decisions (those need user input).
- Submissions (those happen in dedicated sessions per submission strategy).
- Memory updates beyond status corrections (substantive memory work happens in topical sessions).

**Dashboard structure discipline:** This file follows v2.0 dashboard structure codified in `feedback_pm_dashboard_structure.md` (ratified 2026-05-13). When writing a successor handoff, inherit the structure — only the content under each header updates. Priority assignments should be re-evaluated on each refresh.

---

## 1. Read order

1. THIS file (you are here) — read §2–§6 first for at-a-glance orientation; §7+ as you dive into specifics.
2. `tools/workstream-handoffs/README.md` — the index of all workstream handoffs.
3. The staleness-aware memory entries: `feedback_verify_stale_memory_claims.md`, `feedback_audit_recent_active_review_default.md`, `feedback_audit_open_illustrative_default.md`, `feedback_pm_dashboard_structure.md`, `project_book1_state_2026-05-10.md`.
4. `publishing/strategy/cross-thread-todos.md` — items requiring another thread's action.
5. `publishing/strategy/cascade-plan_2026-05-06.md` — strategic cascade state.
6. `publishing/strategy/decisions-log.md` — strategic decisions history.

You do NOT need to read the individual workstream handoffs unless the user asks for details on a specific one. Index-level knowledge is enough for coordination.

---

## 2. Next 72 hours — TOP OF MIND

| When | Action |
|---|---|
| **Wed May 13** | **Darity interview COMPLETE.** Synthesis commit `3e39061` surfaced MI-1, MI-2, MI-3, SI-1, SI-2, SI-3, C-1, C-2, C-3. **ALL MANUSCRIPT-SCOPE ITEMS APPLIED + VERIFIED 2026-05-14** in the Ch 5 / Ch 6 / TA versions that shipped to Sandy: MI-1 (Ch 5 + TA), MI-2 (Ch 5 line 220 + TA §1.10), MI-3 (Ch 6 lines 256 + 262 — heterogeneous-stakeholder break-point), SI-1 (Ch 6 line 124 — profitability-vs-harms asymmetry, commit `6a5ee42`), SI-2 (Ch 6 line 25 — longevity-gap as legacy-effect pricing, attributed to Darity-collaborators published work), C-3 (Ch 6 line 262 — stratification economics tie), SI-3 (Ch 6 line 250 — Sen paired with Parfit as philosophical grounding). **Cross-thread items remain on owning workstreams:** C-1 (Fogel-Engerman two-volume model → #14 comp-titles), C-2 (Du Bois → bibliography). **TA verification follow-on (optional, ~30min):** confirm TA has corresponding scope/grounding sections mirroring MI-3 (§1.10 heterogeneous-stakeholder scope-of-applicability) + SI-3 (Sen-capabilities grounding wherever TA grounds the valuation methodology). |
| **Thu May 14** | **Darity packet SENT.** Cover email + Ch 5 + Ch 6 + Technical Appendix shipped to Sandy mid-travel — see [packet-send-cover-email_2026-05-14.md](../../research/outreach/subjects/darity/packet-send-cover-email_2026-05-14.md). Author cleared the Ch 6 Pass-3 + TA Pass-3 gate by traveling-day decision. **Open for next PM session:** reconcile what state of Ch 6 / TA actually shipped vs. the Pass-3 plan; if deltas exist, surface in synthesis doc Section 2 and decide whether a follow-up "minor revisions since send" note to Sandy is warranted. |
| **NEXT FIRES (parallel)** | **Ch 5 + Ch 6 three-pass cycles CLOSED 2026-05-14** — both Pass 3 docs ratified as-proposed; clean READY TO SUBMIT AS-IS verdicts; no spot-fix work required. **All Darity-synthesis manuscript-scope items RESOLVED + VERIFIED 2026-05-14** — see Wed May 13 row for per-item line locations. Critical-path focus shifts to **(a) Chs 7–10 Phase A Pass 1** (parallel sessions, paced — highest-leverage critical-path target) and **(b) Ch 1 Pass 2 ratification → Pass 3** chain. **Optional: TA scope/grounding verification follow-on (~30min)** — confirm TA mirrors Ch 6 MI-3 + SI-3 additions. |
| **This week** | **Ratify Ch 1 Pass 2** `6fb6510` → apply voice-polish spot-fixes → fire Ch 1 Pass 3. Continue firing Ch 2 Pass 3 + Ch 3 Pass 2/3 + Ch 4 Pass 2/3. Fire Chs 7–10 Phase A Pass 1 as bandwidth permits. |
| **Wed May 20 8:00 EDT** | **CBF consolidated response auto-sends** (Gmail scheduled-send). No action required. |

---

## 3. Critical path bottleneck

**#20 Stage-3 Rigor Pass Chs 5–10 → unblocks → #5 Book proposal sprint (late June) → unblocks → #6 Agent Wave 1 (late July).** Also gates Apparatus Phase A (§6). **Ch 5 Pass 1 PROPOSED with 2 amendments (`d872776` + Amendment 2 pending push). Ch 6 Pass 1 PROPOSED with amendment (`f117831`). Chs 7–10 Phase A not yet started.** This chain drives roughly half the dashboard's "blocked / gated" items. **Immediate critical-path priority: Ch 5 Phase C-α (single integrated commit) before Sandy send.** Treat any Chs 7–10 Phase A firing as high-leverage in parallel.

---

## 4. USER ACTIONS gating Noema submission

These are uniquely user-action items (no Claude session fires them). Surfaced top-level because they are the *only* gates on a near-term submission.

- [ ] **Action 1 — Phat consent outreach** (or Phat's family if Phat unavailable). Package ready at `research/outreach/subjects/phat/` per commits `585d535` + `721c094` + `9aee0af`. Per `feedback_named_subject_consent.md`, living named subjects must be anonymized until signed.
- [ ] **Action 2 — Apply consent decision to Essay B line 136** of [noema-essay-fresh-session-draft_2026-05-10.md](manuscript/essay/Noema/noema-essay-fresh-session-draft_2026-05-10.md). Current anonymized text: *"a crabber and fisherman my father had known since he was small."* Signed → restore Phat's actual name. Not-signed/declined/unreachable → keep anonymization. Either decision unblocks Noema submission.
- [ ] **Action 3 — Apply same to Ch 3** in [Chapter__3_TheWaterman__Draft.md](manuscript/chapters/Chapter__3_TheWaterman__Draft.md).

---

## 5. Workstream status (by bucket, by priority)

Priority within bucket: **HIGH** = time-pressured or gates large downstream cascade. **MED** = important but not yet gating. **LOW** = small / dormant / waiting.

### 5.1 IN FLIGHT

| # | Pri | Workstream | Status | Next action |
|---|---|---|---|---|
| **4** | **HIGH** | Outreach pipeline | 6 subjects in motion. **Darity TODAY 14:00 ET.** CBF response auto-sends **Wed May 20 8am EDT** (`b200664`). Colden citation-verify packet pre-staged (`15c6b0f`). Biggie process guide pre-staged (`164b9e2`). [handoff](tools/workstream-handoffs/outreach-pipeline-handoff_2026-05-09.md) | Conduct Darity interview; synthesis tonight/tomorrow; Sandy email May 14–16; user-action send Colden packet. |
| **20** | **HIGH** | Manuscript Stage-3 Rigor Pass | Chs 1–4 partway; Chs 5–10 not started — **critical path bottleneck**. See per-chapter detail in §6. [handoff](tools/workstream-handoffs/manuscript-stage-3-rigor-pass-handoff_2026-05-11.md) | Per §6 per-chapter "next action" column. |

### 5.2 READY TO FIRE

| # | Pri | Workstream | Status | Fire window |
|---|---|---|---|---|
| **1** | **HIGH** | Aeon pitch | Version C ratified 2026-05-08; Stage 3 verdict 2026-05-10 confirmed Version C beats Pitch B decisively. [handoff](tools/workstream-handoffs/aeon-submission-handoff_2026-05-09.md) | **Sun May 31 14:01 UTC** (= Mon Jun 1 ~00:01 AEST). Pre-submission verify 1–2d prior. |
| **16** | MED | $100 Barrel essay → Phenomenal World | Q1 verdict flipped CONDITIONAL → **GO** (`b7fd20f`). Condition 1 (non-partisan framing) carries forward. [handoff](tools/workstream-handoffs/100-barrel-essay-handoff_2026-05-11.md) | Fire Session 2 — Stage 1 audience-aware brief w/ Condition 1 embedded. |
| **2** | MED | Boston Review essay | UNBLOCKED 2026-05-10 by meta-verdict. v2.0 discipline embedded. Not drafted. [handoff](tools/workstream-handoffs/boston-review-essay-handoff_2026-05-09.md) | When bandwidth permits. Pitch ~1pp + essay ~4,500w from Ch 5. |
| **14** | MED | Comp-titles deep matrix Phase 2 | Just-in-time verification deferred from #11. [handoff](tools/workstream-handoffs/comp-titles-deep-matrix-phase-2-handoff_2026-05-11.md) | Early-to-mid July 2026 (2–3wk before Wave 1). |
| **18** | LOW | Ch 6 .html → .md conversion | Convenience cleanup; independent of #17. [handoff](tools/workstream-handoffs/ch6-html-to-markdown-conversion-handoff_2026-05-11.md) | ~1–2h focused session. |
| **19** | LOW | Tech Appendix Scheme-4 cleanup | Deferred Scheme-4 work from #15. [handoff](tools/workstream-handoffs/appendix-scheme-4-cleanup-handoff_2026-05-11.md) | Smaller-scope follow-up. |

### 5.3 WAITING / BLOCKED / DORMANT

| # | Pri | Workstream | Gated on | Target |
|---|---|---|---|---|
| **5** | **HIGH** | Book proposal | #20 completion | Late-June 2026 sprint (~3wk). Skeletons up; §05 chapter summaries landed (`733ba8e`). [handoff](tools/workstream-handoffs/book-proposal-handoff_2026-05-09.md) |
| **6** | MED | Agent prep / target list | #20 + #5 + #14 | Wave 1 late Jul / early Aug 2026. 1/25 populated (Chalfant/Wylie). [handoff](tools/workstream-handoffs/agent-prep-handoff_2026-05-09.md) |
| **3** | MED | Berggruen Prize essay | AI-free constraint (user-only) | Soft 2026-08-05; hard 2026-08-17. [handoff](tools/workstream-handoffs/berggruen-track-handoff_2026-05-09.md) |
| **12** | LOW | Aeon essay post-acceptance | Aeon acceptance of #1 | Dormant. [handoff](tools/workstream-handoffs/aeon-essay-post-acceptance-two-stage-handoff_2026-05-10.md) |
| **17** | LOW | Publishing pipeline (md→docx + html→pdf) | First submission deliverable queued | Trigger = book proposal completion / sample-chapter request / full manuscript request. [handoff](tools/workstream-handoffs/publishing-pipeline-handoff_2026-05-11.md) |

### 5.4 COMPLETE (one-line; full standing-references in workstream handoffs)

6 workstreams complete since 2026-05-10: **#8** Path B audit cross-chapter • **#9** Apparatus register decision sweep • **#10** Cross-chapter consistency audit • **#11** Comp-titles deep matrix v0 • **#13** Flagship-equation terminology defense sweep • **#15** Tech Appendix numbering reconciliation. Their substance feeds downstream work; see individual handoffs for standing-reference paths.

**#7 Manuscript completion — RETIRED in this dashboard rev** (2026-05-13). Substance migrated into Apparatus section (§7). Handoff file `manuscript-completion-handoff_2026-05-09.md` left in place as historical record.

---

## 6. #20 Stage-3 Rigor Pass — per-chapter detail

| Ch | Pass 1 (fact-check) | Pass 2 (voice-polish) | Pass 3 (audience-load) | Phase C spot-fixes | **Next action** |
|---|---|---|---|---|---|
| **1** | COMPLETE | **PROPOSED** `0b78449` (v2 `6fb6510`) — awaits ratification | not fired | 11 applied (last `008ac3f` F-3 NASA Langley / Hampton VA) | **Ratify Pass 2** → apply voice-polish spot-fixes → fire Pass 3 |
| **2** | COMPLETE | COMPLETE | pending — paste-text drafted | 14 applied (C-α/β `5bc6edb` + C-γ `fa08c10`) | **Fire Pass 3** (audience-load) |
| **3** | LANDED `2f76e37` (Colden naming + Norway fund-age) | pending | pending | — | **Fire Pass 2** (voice-polish) — paste-text gen from PM |
| **4** | COMPLETE | pending | pending | 5 MEDIUM + 2 LOW (`e67b8b8` + `8f792ee`) | **Fire Pass 2** (voice-polish) — paste-text gen from PM |
| **5** | RATIFIED + Phase C-α applied (`da26bdc`) | RATIFIED + Phase C-β + C-β-followup applied (`d68d92e` + `7cbb9c1` + `d2ee178`) | **RATIFIED 2026-05-14** — 9 INCLUDE / 0 EXCLUDE; READY TO SUBMIT AS-IS; no Phase C-δ spot-fixes required | C-α + C-β + C-β-followup applied; C-δ placeholder closed empty | **Ch 5 three-pass cycle CLOSED.** Packet that shipped to Sandy 2026-05-14 is post-Pass-3-verified state. No further Stage-3 work on Ch 5 unless Sandy reply surfaces revision items. |
| **6** | RATIFIED + Phase C-α applied (`6a5ee42`) + Pass 1 Amendment E / math-check Phase C-β applied (`f6bb6ad`) | RATIFIED + Phase C-γ applied (`f081ceb`) + C-γ-followup (`ccd87f1`) + C-δ tighten (`bfafe47`) + cascade-followup convergence-table figures refresh (`e927e74`) | **RATIFIED 2026-05-14** — 7 INCLUDE / 0 EXCLUDE; READY TO SUBMIT AS-IS; no Phase C-ε spot-fixes required; Tier-B-optional items held as-is per audit | extensive — see commit chain; C-ε placeholder closed empty | **Ch 6 three-pass cycle CLOSED.** Cross-chapter line-21 Black Lung reframe already applied post-audit (`5569600`), so packet that shipped to Sandy 2026-05-14 is post-Pass-3-verified state. **Darity-synthesis status: ALL ITEMS RESOLVED + VERIFIED 2026-05-14** — SI-1 line 124 (`6a5ee42`), MI-3 lines 256/262, SI-2 line 25, C-3 line 262, SI-3 line 250. Q0 tier-S citation questions logged in cover-email reply-handling list (Ch 5 line 220 + Ch 6 line 124 + Ch 6 line 262). Optional TA scope/grounding verification follow-on remains (~30min). |
| **7–10** | not started | — | — | — | **Fire Phase A Pass 1** (parallel sessions, paced) — critical path. New chapters should inherit any post-audit Stage-3 structural change (see §8 Decisions pending — Stage-3 two-pass collapse proposal). |

Cross-thread #11 (endnote/citation sweep) accumulating: Ch 2 = 9M+1L; Ch 4 = 5M+3L; **Ch 5 = 16M + 14L + N-6 citation-form sharpening (Kenworthy & Igra 2022, not Igra et al. 2021)**. Soft target after Phase B; hard target before late-July Wave 1.

---

## 7. Apparatus + front-and-back-matter

**Framing:** Bibliography, Tech Appendix, and Glossary each need multi-phase treatment paralleling #20 — per-chapter Phase A (10 parallel sessions, paced) + book-wide Phase B audit reconciling cross-references and ensuring in-text citations / appendix-pointers / glossary terms line up across chapters. AI Statement and Dedication are short single-pass items.

| Item | Pri | Phase A (per-chapter) | Phase B (book-wide audit) | Current state | Fires when |
|---|---|---|---|---|---|
| **Bibliography** | MED | Per-chapter engagement-flag pass (engagement-pending → engaged) Chs 1–10 | Reconciliation: every in-text citation resolves to a bib entry; every bib entry ref ≥1×; format consistency | UNBLOCKED 2026-05-11. Not started. | Phase A per-chapter after that chapter's #20 voice-polish + audience-load passes land (cleaner stabilized surface). |
| **Technical Appendix** | MED | Per-chapter pass: every apparatus call-out points to correct section post-#15; every TA section has ≥1 chapter call-site | v2.0.0 rebuild + audit: numbering canonical (post-#15), Scheme-4 cleanup (#19) applied, cross-refs re-validated | Numbering reconciled 2026-05-11 (#15). v2.0.0 rebuild + #19 Scheme-4 cleanup pending. | #19 should land before Phase A. Per-chapter follows #20 stabilization. |
| **Glossary** | MED | Per-chapter pass: every defined term used in chapter has glossary entry; first-use convention applied; no orphan glossary terms | v4 rebuild + audit: alphabetization, cross-term consistency, register-discipline (illustrative vs canonical per Ostrom-path memory) | UNBLOCKED 2026-05-11 by #9 + #15. Not started. | Per-chapter after #20 voice-polish + audience-load (those passes change what's defined). |
| **AI Statement** | LOW | Single pass (no per-chapter component) | n/a | Current artifact: `manuscript/chapters/_AUTHORSNOTE_ON_WINDTUNNELS_AND_AI.md`. Source material now accumulating at [`research/process-narrative/`](../../research/process-narrative/) — origin-story narrative captured 2026-05-13 (`origin-story_2026-05-13.md`). Per memory, framing already shifted toward inventor reality after NASA Langley grandfather discovery (LaVern E. Winn). | Anytime; no gates. A future drafting session should sift the source material in `research/process-narrative/` + cross-reference inventor memory + apply v2.0 two-stage discipline. |
| **Dedication** | LOW | Single pass | n/a | Current state TBD — needs verification. | Anytime; no gates. |

---

## 8. Decisions pending

- **Apparatus Phase A sequencing.** Bibliography / Tech Appendix / Glossary per-chapter pass — run interleaved during #20 or after #20 completes? After-#20 gives cleaner reconciliation surface (voice-polish + audience-load passes change what apparatus is called out); interleaved catches inconsistencies earlier but risks rework. **PM recommendation:** for each chapter, run apparatus Phase A as a follow-up *after* that chapter's #20 Pass 3 lands. Compromise that lets the chapter stabilize before apparatus call-outs lock in.
- **AI Statement + Dedication current state.** Verify whether `manuscript/...AuthorsNote*` is the AI Statement or distinct; locate Dedication file (if exists). User input needed to populate §7 LOW rows.
- **#7 Manuscript completion workstream retirement.** Done in this dashboard rev (2026-05-13). Substance migrated to §7 Apparatus. Flag if author wants #7 kept standing instead.

---

## 9. Date-anchored action list

Merged deadline calendar + todos. Sorted forward in time.

### Wed May 13
- [x] **14:30 ET** — Darity interview COMPLETE (synthesis `3e39061` surfaced MI-1 + MI-2 + SI-1; MI-1 + MI-2 incorporated; SI-1 absence flagged for author check)
- [x] Ch 5 Pass 1 PROPOSED with 2 amendments (`d872776` + Amendment 2 this session)
- [x] Ch 6 Pass 1 PROPOSED with amendment (`f117831`)

### Today (Thu May 14) — author traveling
- [x] **Darity packet SENT** — Ch 5 + Ch 6 + Technical Appendix shipped to Sandy with cover email at [packet-send-cover-email_2026-05-14.md](../../research/outreach/subjects/darity/packet-send-cover-email_2026-05-14.md). Author cleared Pass-3 gate by traveling-day decision.
- **Open** — SI-1 disposition check (queued for Ch 6/Ch 9 or needs Ch 5 landing paragraph?) + Ch 5 Phase C-α single integrated commit (now post-send polish) + Ch 6 Pass 1 Amendment / Phase C-α (post-send catch-up)
- **Open** — Reconcile what state of Ch 6 / TA actually shipped to Sandy vs. the Pass-3 plan; if deltas exist, decide on follow-up "minor revisions since send" note

### This week (by Sun May 17)
- **Ratify Ch 1 Pass 2** `6fb6510` → apply voice-polish spot-fixes
- **Trigger Ch 1 Pass 3 + Ch 2 Pass 3 + Ch 3 Pass 2/3 + Ch 4 Pass 2/3** (paste-text gen from PM)
- **Fire Chs 5–10 Phase A** as bandwidth permits — critical path bottleneck

### Wed May 20
- **8:00 EDT** — CBF consolidated response auto-sends (no action; automatic)

### Late May / early June
- **Submit Noema essay** to `edit@noemamag.com` (gated on §4 USER ACTIONS)
- **Send Colden pre-publication citation-verification packet** ahead of Ch 3 publication courtesy (user-action; `15c6b0f`)
- **Final pre-submission verify of Aeon Version C** (1–2d before Jun 1)
- **Fire $100 Barrel essay (#16) Session 2** — Stage 1 brief w/ Condition 1 embedded
- **Continue Chs 5–10 Phase A**

### Sun May 31 14:01 UTC (= Mon Jun 1 ~00:01 AEST)
- **Submit Aeon pitch Version C** verbatim via aeon.co/pitch

### Late June
- **Book proposal sprint** (#5) — gated on #20 completion
- **Publishing-lawyer consultation** (cross-thread #7) — user-action to schedule

### July
- **Comp-titles Phase 2 verification** (#14) — fire window early-to-mid July
- **Late July / early August — Agent Wave 1** (8 Priority A) — gated on #20 + #5 + #14

### Late summer
- **Tue Aug 5** — Berggruen Prize soft target (AI-free; user-only)
- **Sun Aug 17** — Berggruen Prize hard deadline

### Backlog (no fixed date)
- Boston Review pitch + essay (#2)
- Ch 6 .html→.md conversion (#18) ~1–2h
- Tech Appendix Scheme-4 cleanup (#19)
- Cross-thread #9 — Ch 2 GuidanceDoc stale "$100 barrel passage" refs
- Apparatus Phase A per-chapter rolling fires (post each chapter's #20 Pass 3)

### Dormant / conditional
- #12 Aeon post-acceptance — fires on Aeon acceptance
- Biggie courtesy-notify before any essay using his name publishes
- Publishing pipeline (#17) — trigger = first submission deliverable queued

### Future agent waves
- **Sept–Oct 2026** — Wave 2 (8 Priority B), after Wave 1 outcomes
- **Q4 2026 / Q1 2027** — Wave 3 (9 Priority C), after Wave 2 outcomes

---

## 10. Cross-thread coordination

| # | Item | Producer | Consumer | Status |
|---|---|---|---|---|
| 1 | Acknowledgments check: Chalfant ↔ Mazzucato | Outreach / verification | #6 Wave 1 | Partial — *Value of Everything* read (no agent named); *Mission Economy* pending |
| 2 | Post-Darity warm-intro discovery | #4 Outreach | #6 Agent prep | Held — template-set ready, awaiting today's trigger |
| 4 | Atlantic Ideas vs. PW slot-3 venue | Publishing strategy | Future essay slot-3 | Open — may resolve implicitly via #16 → PW |
| 5 | Boston Review v2.0 application | PM meta-verdict | #2 session | RESOLVED 2026-05-10 |
| 6 | Aeon post-acceptance v2.0 application | PM meta-verdict | #12 session | RESOLVED 2026-05-10 |
| 7 | Interview-attribution protocol jurisdictional gaps | PM session | Protocol-update + publishing-lawyer | Protocol v2 COMPLETE (`998166f`); lawyer consult target by late June |
| 8 | Comp-titles Phase 2 | #11 → #14 | #6 Wave 1; #5 §04 | Open — dormant until early-to-mid July |
| 9 | Ch 2 GuidanceDoc stale "$100 barrel passage" refs | #10 audit | Insight #37 Batch-D | Open — small fix-session or bundled |
| 10 | PM-verified apparatus-stability checkpoint for #16 | Q1 rigor pass | #16 fire decision | RESOLVED 2026-05-11 |
| 11 | Endnote / citation-finalization sweep | Per-chapter #20 audits | Coordinated endnote sweep | Open — accumulating; Ch 2 = 9M+1L, Ch 4 = 5M+3L; hard target before Wave 1 |
| — | Author-bio updates as essays place | #4 + essay submissions | #5 author platform | Continuous |

Full inventory: `publishing/strategy/cross-thread-todos.md`.

---

## 11. PM session freshness — when to wrap and start fresh

The PM handoff file is durable; PM *sessions* (Claude chat windows) accumulate noise and context drift. The PM session should surface a recommendation to the author to wrap the current PM session and start a fresh one when ANY of:

- **Time-based:** session has run ≥ 3 calendar days. Predecessor PM session ran 2026-05-10 → 2026-05-13 (3 days) before wind-down — that's a reasonable cadence.
- **Phase-shift:** major restructuring of the dashboard (like 2026-05-13 v2.0 reorg); major event lands (Darity interview synthesis; Aeon submission; CBF response sends); chapter batch completes; submission deadline hits.
- **Context bloat:** in-session reasoning has accumulated past comfortable scan length, or you find yourself re-deriving state already in the handoff.

**When a wrap point hits, the PM session should:**
1. Refresh this handoff file in place if state has shifted.
2. If material structural shift OR ≥ 7 days elapsed, write a successor file (`pm-session-handoff_<NEW-DATE>.md`) and update `tools/workstream-handoffs/README.md` to point to it. Mark predecessor superseded (header note).
3. Explicitly surface to the author: *"This PM session has hit a natural wrap point. Handoff is current as of <date>. Recommend wrapping this session and starting fresh — open a new PM session and orient against the handoff."*

**This PM session (started 2026-05-13).** Natural wrap points ahead:
- (a) After Darity synthesis lands and verifies on origin/main.
- (b) After Sandy email goes out (May 14–16) and any reply lands.
- (c) After Wed May 20 CBF auto-send fires.
- (d) After ≥ 3 calendar days elapsed (by Sat May 16).

The PM session is OK to keep running through Darity synthesis + Sandy email + Ch 1 Pass 2 ratification. After those land, wrap and start fresh.

---

## 12. How to handle common user prompts

- **"What should I do next?"** → Lead with §2 (next 72h) + §3 (critical path) + §4 (USER ACTIONS). Cross-ref §5 status + §9 dates. Recommend the highest-priority unblocked item that fits available time/energy.
- **"I just finished X." / "X session is done."** → Auto-verify per §13 (origin/main + artifact spot-check) BEFORE marking complete. Then update §5 status with verifying commit hash + one-line evidence; mark §9 line complete; surface what unblocks (§10 cross-thread).
- **"Give me text to paste into a fresh session for X."** → Generate paste-text per the appropriate handoff + drafting-templates scaffold (`tools/drafting-templates/`). Paste-text only; do NOT execute.
- **"What's blocked?"** → §5.3 column "Gated on." Filter on items with non-empty gates.
- **"What's overdue?"** → §9, items with past dates not yet marked done.
- **"What does workstream X need?"** → Read the workstream's handoff (linked in §5). Summarize: read order, deliverables, first actions.
- **"Add a todo: ..."** → Insert into §9 at appropriate date bucket. If substantive enough, propose creating a new handoff.
- **Day-of-week / date assertions** → Verify against a known anchor before asserting. Today (per harness): **Wed May 13, 2026.** Past day-of-week errors in PM session caused calendar drift; treat date claims with staleness discipline.

When you don't know — say so. Verify before asserting (per `feedback_verify_stale_memory_claims.md`).

---

## 13. Auto-verify discipline (RATIFIED 2026-05-10)

**Trigger conditions.** PM session auto-verifies origin/main canonical state before marking ANY workstream / todo / dashboard row complete. Triggers:

- User reports a session finished ("X session is done" / "X completed and pushed").
- PM session notices new commits on origin/main during a routine fetch.
- PM session is about to mark anything complete on the dashboard.

No formal "Note & Verify" gate required from the user — auto-verify is PM session's own discipline.

**Why this exists.** Sessions sometimes report "complete and pushed" when they only pushed to their feature branch, not origin/main. Auto-verify catches that + several other failure modes before stale-state reaches the dashboard.

**The verification protocol.**

1. **Fetch origin/main.** `git fetch origin main`.
2. **Confirm commit(s) exist on origin/main.** `git log origin/main --oneline | grep <hash>` — if only on feature branch, report back; do NOT mark complete.
3. **Direct-inspect the artifact(s).** `ls` expected files; spot-check key content against the session's spec (header metadata, expected sections, expected diff pattern, word counts within bands, etc.).
4. **If clean:** mark complete on dashboard with commit hash + one-line verification evidence note.
5. **If something's off:** flag before marking. Common failure modes:
   - Commit only on local branch (not pushed to origin/main).
   - Artifacts missing one or more deliverables.
   - Content doesn't match spec.
   - Conflicts with parallel session work.

**Verbosity tradeoff.** Default rigor: medium — verify commit on origin/main + key content spot-check; report tight 3–5 line summary. User can request lighter or heavier per session.

---

## 14. Parallel-PM-session collision risk

**Pattern observed during 2026-05-10 → 2026-05-13 window:** multiple PM sessions running in parallel sometimes edit the same handoff file, causing rebase failures on push. Resolution that worked: abort the in-progress rebase, reset to origin/main, accept the parallel session's canonical state.

**Mitigation:** before any edit to `pm-session-handoff_<DATE>.md` or related coordination files, fetch origin/main first. If a parallel PM session has just pushed, reconcile rather than rebase-and-overwrite. Prefer SHORT, ATOMIC edits over long pending diffs that risk collision.

---

## 15. Reusable drafting-session templates (2026-05-11)

Five reusable scaffolds at `tools/drafting-templates/` (commit `e29db8c`) for fresh-session paste-text generation in any drafting task. v2.0 discipline applied:

- Stage 1 pre-draft brief (audience-aware + canonical-facts)
- Stage 2 fresh-session draft (audience-blind)
- Stage 3 Pass 1 fact-check
- Stage 3 Pass 2 voice-polish
- Stage 3 Pass 3 audience-load

Use these as starting points when generating paste-text for new fresh sessions, rather than re-deriving from scratch.

---

## 16. Two-stage drafting discipline v2.0 — RATIFIED + CODIFIED

Status: **RATIFIED 2026-05-10. CODIFIED 2026-05-10 (commit `9caccdc`).**

The methodology meta-experiment closed. v2.0 amendments A + B + C all in force:

- **Amendment A — Stage 1 brief enrichment for personal-narrative content.** Stage 1 briefs must include canonical factual ground truth (not just beats).
- **Amendment B — Stage 3 split into three distinct passes** (fact-check + voice-polish + audience-load).
- **Amendment C — Domain-of-applicability rule.** Apply when (a) artifact derives from existing chapter/source prose at Path B contamination risk, OR (b) source has apparatus/jargon that would tripwire the venue, OR (c) artifact is long-form publisher-facing material drafted without a strong iterated control. Don't apply when a strong iterated control already exists for short-form material.

Memory: `feedback_audience_aware_drafting_discipline.md` (v2.0).
Application: every long-form publisher-facing essay session inherits this by default.

---

## 17. Outreach pipeline detail

Per `outreach-pipeline-handoff_2026-05-09.md`. Update as responses land.

| Subject | Affiliation | Status | Date | Notes |
|---|---|---|---|---|
| **William ("Sandy") Darity Jr.** | Duke | **PACKET SENT 2026-05-14; ALL SYNTHESIS ITEMS RESOLVED** | Wed May 13 14:30 ET interview + Thu May 14 packet send | Interview conducted Wed. Synthesis commit `3e39061` surfaced MI-1 / MI-2 / MI-3 / SI-1 / SI-2 / SI-3 / C-1 / C-2 / C-3. **All manuscript-scope items RESOLVED + VERIFIED 2026-05-14:** MI-1 + MI-2 (Ch 5 + TA via `70dce3f` + downstream); SI-1 Ch 6 line 124 (`6a5ee42`); MI-3 Ch 6 lines 256/262; SI-2 Ch 6 line 25; C-3 Ch 6 line 262; SI-3 Ch 6 line 250. **Cross-thread items on owning workstreams:** C-1 → #14 comp-titles, C-2 → bibliography. **Thu May 14 — packet (Ch 5 + Ch 6 + TA) SENT** with cover email at [packet-send-cover-email_2026-05-14.md](../../research/outreach/subjects/darity/packet-send-cover-email_2026-05-14.md). Pass 3 ratified as-proposed for both chapters; cycles CLOSED. **Open follow-ups:** (1) Reply-handling protocol per cover-email §"What to do with Sandy's reply" — Ch 5 line-220 attribution clearance into synthesis Section 2, **three Q0 tier-S citation questions for Ch 6 lines 124 / 262 + Ch 5 line 220 (substantive paraphrase of spoken material per Sandy's Q0) — author call on raise-proactively vs. wait-and-see vs. not-required**, and warm-intro template activation (`publishing/agents/post-darity-warm-intro-templates_2026-05-10.md` Variant A) if a candidate is named. (2) Optional TA scope/grounding verification (~30min) to confirm TA mirrors Ch 6 MI-3 + SI-3 additions. |
| **Mariana Mazzucato** | UCL/IIPP | HOLDING via Adam Albrecht | Held since 2026-05-06 | Awaiting substantive follow-up. Not blocking. |
| **Allison Colden** | CBF Maryland | RESPONSE SENT via Val DiMarzio (consolidated) | 2026-05-13 (scheduled-send Wed May 20 8am EDT) | Public-record brief landed 2026-05-08. Substitution-hypothesis CONFIRMED. Pre-publication citation-verification packet pre-staged (`15c6b0f`). |
| **Karen Moore** | CBF Virginia | RESPONSE SENT via David Sherfinski (consolidated) | 2026-05-13 (scheduled-send Wed May 20 8am EDT) | Public-record brief landed 2026-05-08. |
| **Biggie family (Ch 3 deceased subject)** | — | Process guide pre-staged 2026-05-13 (`164b9e2`) | — | Outreach pending user-decision per `feedback_named_subject_consent.md`. |
| **Boyce, Buller, Mian, Sufi, Alperovitz, Mondragon, Klein, Coalition of Clinics, Raworth, ACLC, Lipcius, Mann** | Various | Cold-outreach sent | 2026-05-05 | Standard 2–3 wk academic-response window. Some replies may have landed — verify before quoting. |

---

## 18. Updating this handoff

This file IS the PM session's working memory. Update it as state changes:

- When a workstream's status changes, update §5.
- When a date passes, archive it (history section or delete) and update §9.
- When a todo completes, mark `[x]` in §9 or §4 (short-term retention) or remove (cleanup).
- When new workstreams emerge, add to §5 + create their handoff in `tools/workstream-handoffs/`.
- When stale claims surface, correct in place.

**Periodic full-file refresh:** every ~7–14 days, or after any significant phase shift, write a successor file (`pm-session-handoff_<NEW-DATE>.md`) that supersedes this one. Update `tools/workstream-handoffs/README.md` to point to the latest. Mark the predecessor superseded (header note + dashboard-handoff pointer).

**Structural discipline:** Successor handoffs inherit the v2.0 dashboard structure (§§2–11 ordering). See `feedback_pm_dashboard_structure.md`.

**Predecessor:** `pm-session-handoff_2026-05-10.md` (covered 2026-05-10 → 2026-05-13 session window; superseded by this file).

---

## 19. Reference inventory

**Index files:**
- `tools/workstream-handoffs/README.md` — workstream handoff index
- `publishing/strategy/cross-thread-todos.md`
- `publishing/strategy/cascade-plan_2026-05-06.md`
- `publishing/strategy/decisions-log.md`

**Memory entries (read MEMORY.md for full index):**
- `feedback_pm_dashboard_structure.md` — v2.0 dashboard structure (this file's structure)
- `project_book1_state_2026-05-10.md` — current project state snapshot
- `feedback_audience_aware_drafting_discipline.md` — v2.0 two-stage discipline
- `feedback_named_subject_consent.md` — naming discipline (Biggie / Phat)
- `feedback_voice_polish_pipeline.md` — dump → sift → polish
- `feedback_substance_drives_length.md` — no arbitrary word targets
- `feedback_verify_stale_memory_claims.md` — verification discipline
- `feedback_two_layer_content_discipline.md` — internal-vs-external content origination
- `feedback_audit_recent_active_review_default.md` — audit conflict resolution
- `feedback_audit_open_illustrative_default.md` — open/illustrative audit default
- `feedback_grammatical_role_cross_references.md` — chapter→appendix cross-reference discipline
- `feedback_dual_audience_test.md` — trade-press polish dual-audience test
- `reference_sandel_hybrid_pattern.md` — acronym treatment hybrid pattern

**Reusable drafting-session templates:**
- `tools/drafting-templates/` — Stage 1 brief, Stage 2 draft, Stage 3 Passes 1+2+3 (commit `e29db8c`)

---

*End of PM session handoff (v2.0 dashboard structure). Update in place as state evolves; write successor file ~weekly or after structural shift.*
