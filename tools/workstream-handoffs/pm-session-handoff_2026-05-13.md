# Project Management Session — Handoff (2026-05-13)

**Date drafted:** 2026-05-13 (supersedes `pm-session-handoff_2026-05-10.md`)
**Branch to create at session start:** `claude/pm-session-<harness-id>` (branch from current `origin/main` after `git fetch`)
**Session type:** **Parallel coordination session.** Runs alongside the user's per-workstream sessions. Does NOT execute workstream tasks; tracks state, surfaces dependencies, manages the todo list, flags deadlines, routes work between sessions.

---

## 0. Mission of the PM session

You are the PM coordination session. Your job is to keep the *Commons Bonds* project's many parallel workstreams legible to the author. The author opens and closes individual sessions for specific workstreams (manuscript Stage-3 audits, comp-titles, agent prep, etc.) and uses this session as the central tracker.

**You execute:**
- Status updates after the user reports completing work in another session (verify per §10.5 before marking complete).
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

When the user asks "what's next?" — synthesize from this dashboard + their recent activity + upcoming deadlines.
When the user reports finishing a task — verify per §10.5; then update this file's status, mark the todo complete, surface what unblocks.
When the user wants to add a task — capture, prioritize, flag dependencies.

---

## 1. Read order

1. THIS file (you are here).
2. `tools/workstream-handoffs/README.md` — the index of all workstream handoffs.
3. The staleness-aware memory entries: `feedback_verify_stale_memory_claims.md`, `feedback_audit_recent_active_review_default.md`, `feedback_audit_open_illustrative_default.md`, `project_book1_state_2026-05-10.md`.
4. `publishing/strategy/cross-thread-todos.md` — items requiring another thread's action.
5. `publishing/strategy/cascade-plan_2026-05-06.md` — strategic cascade state.
6. `publishing/strategy/decisions-log.md` — strategic decisions history.

You do NOT need to read the individual workstream handoffs unless the user asks for details on a specific one. Index-level knowledge is enough for coordination.

---

## 2. Current phase summary (as of 2026-05-13)

The project is in the **manuscript Stage-3 rigor pass + outreach-execution (Darity interview today) + publishing-pipeline-deepening + parallel-essay-submissions** phase. Drafting phase complete (10 chapters + AuthorsNote drafted).

Active work streams:

- **Manuscript Stage-3 rigor pass (#20).** The dominant work right now. Phase A per-chapter (three-pass: fact-check + voice-polish + audience-load) running in parallel sessions, paced by the user, interleaved with Phase C spot-fix application. Ch 1 Pass 1 + Phase C complete (11 spot-fixes); Ch 1 Pass 2 PROPOSED (awaits ratification); Ch 1 Pass 3 not yet fired. Ch 2 Pass 1 + Pass 2 + 14 spot-fixes complete; Ch 2 Pass 3 pending. Ch 3 Pass 1 LANDED. Ch 4 Pass 1 + 5 MEDIUM + 2 LOW spot-fixes complete; Ch 4 Passes 2 + 3 pending. Chs 5-10 Phase A not yet started. **Critical dependency:** must complete before late-June book-proposal sprint.
- **Outreach execution.** Darity interview **today Wed May 13 14:00 ET**. CBF consolidated response **scheduled-send Wed May 20 8am EDT**. Colden pre-publication citation-verification packet pre-staged (user-action to send). Biggie family courtesy-notification process guide pre-staged.
- **Essay submissions.** Aeon pitch (Version C ratified, ready to submit Mon Jun 1 ~00:01 AEST). Noema Essay B (post-Stage-3 polish complete, gated only on Phat consent). Boston Review pitch + essay drafting unblocked. Berggruen Prize essay (AI-free; soft target Aug 5).
- **Publishing pipeline (#17 + #18 + #19).** Stood up; trigger to schedule = first submission deliverable queued.
- **Book proposal (#5) + agent prep (#6).** Pre-work landed (proposal §05 chapter summaries; comp-titles deep matrix v0). Sprint target late June (gated on #20). Wave 1 target late July / early August (gated on #20 + #5).

Two-stage drafting discipline v2.0 RATIFIED 2026-05-10 and CODIFIED 2026-05-10 (commit `9caccdc`). Amendments A + B + C all in force.

---

## 3. Workstream dashboard

Status legend: `IN FLIGHT` = active sessions; `READY TO FIRE` = paste-text or handoff exists, awaiting trigger; `BLOCKED` = waiting on another workstream; `DORMANT` = conditional; `COMPLETE` = done + verified.

| # | Workstream | Handoff | Status | Next action | Blocker |
|---|---|---|---|---|---|
| 1 | **Aeon pitch submission** | [aeon-submission-handoff](aeon-submission-handoff_2026-05-09.md) | READY TO SEND. Version C ratified 2026-05-08; Stage 3 verdict 2026-05-10 confirmed Version C beats Pitch B decisively. Submit verbatim, no fusion. | Submit Mon Jun 1 ~00:01 AEST. Final pre-submission verification 1–2 days prior. | None — awaiting submission date. |
| 2 | **Boston Review essay** | [boston-review-essay-handoff](boston-review-essay-handoff_2026-05-09.md) | UNBLOCKED 2026-05-10 by meta-verdict. v2.0 discipline application embedded in handoff. Not yet drafted. | Draft pitch (~1pp) + essay (~4,500w from Ch 5) when scheduling permits. | None blocking — workstream-ready. |
| 3 | **Berggruen Prize essay** | [berggruen-track-handoff](berggruen-track-handoff_2026-05-09.md) | **AI-free required.** Deadline 2026-08-17. Soft target 2026-08-05. | Author drafts outside any AI-assisted session. | AI-free constraint. |
| 4 | **Outreach pipeline** | [outreach-pipeline-handoff](outreach-pipeline-handoff_2026-05-09.md) | 6 subjects in flight. **Darity interview TODAY Wed May 13 14:00 ET.** CBF consolidated response (Val DiMarzio + David Sherfinski) **SCHEDULED via Gmail scheduled-send for Wed May 20 8:00am EDT** (`b200664`). Colden pre-publication citation-verification packet landed 2026-05-13 (`15c6b0f`) — user-action to send. Biggie family courtesy-notification process guide pre-staged 2026-05-13 (`164b9e2`). | Conduct Darity interview today; post-call synthesis tonight or tomorrow; send Sandy post-interview confirmation email May 14–16; CBF response auto-sends Wed May 20; user-action send Colden citation-verification packet ahead of book publication. | Awaiting Mazzucato substantive reply; awaiting cold-outreach replies. |
| 5 | **Book proposal** | [book-proposal-handoff](book-proposal-handoff_2026-05-09.md) | Skeletons stood up; comp-titles substantive (~80%); bio polished. Proposal §05 chapter summaries landed 2026-05-11 (`733ba8e`; 10 chapters, ~514w each, 5,137w total). | Late-June 2026 sprint (~3-week focused effort). | Gated on #20 completion (Stage-3 rigor pass). #11 feeds §02. |
| 6 | **Agent prep / target list** | [agent-prep-handoff](agent-prep-handoff_2026-05-09.md) | 1/25 populated (Sarah Chalfant / Wylie). Template + tracker + snippets seeded. | Populate 7 more Priority A targets. Wave 1 late July / early Aug 2026. | Comp-titles deep matrix (#11/#14) feeds agent intelligence. Gated on #20. |
| 7 | **Manuscript completion** | [manuscript-completion-handoff](manuscript-completion-handoff_2026-05-09.md) | Stale-header fix landed 2026-05-10 (`5cd2c15`). All 10 chapters reflected accurately. Bibliography flag-updates + Tech Appendix v2.0.0 + Glossary v4 still pending — UNBLOCKED 2026-05-11 by #9 + #15 finishing. | Continue bibliography flag-updates; rebuild Tech Appendix Phase 3 v2.0.0; rebuild Glossary v4. | None blocking. |
| 8 | **Path B audit cross-chapter** | [path-b-audit-cross-chapter-handoff](path-b-audit-cross-chapter-handoff_2026-05-10.md) | **COMPLETE 2026-05-11** (commits `5643f70` + `71146da` + final-deliverable `bbf06f2`; doc patch `9c189b3`). Standing-reference at `research/audits/cross-chapter-path-b-audit_2026-05-11.md`. | — | — |
| 9 | **Apparatus register decision sweep** | [apparatus-register-sweep-handoff](apparatus-register-sweep-handoff_2026-05-10.md) | **COMPLETE 2026-05-11** (final-deliverable `bbf06f2`). 13 ratified items + 2 Path B fixes. Standing-reference at `tools/rigor-passes/commons_bonds_rigor_pass_2026-05-11_apparatus_register_decision_v1.0.0.md`. | — | — |
| 10 | **Cross-chapter consistency audit** | [cross-chapter-consistency-handoff](cross-chapter-consistency-handoff_2026-05-10.md) | **COMPLETE 2026-05-11** (Phases 1+2 + Batches 1-4 fixes; Batch 5 verified clean via `b55850d`; chapter-end marker standardization `fa8abfe`). Standing-reference at `research/audits/cross-chapter-consistency-audit_2026-05-11.md` + `tools/audits/cross-chapter-consistency-inventory_2026-05-11.md`. | — | — |
| 11 | **Comp-titles deep matrix v0** | [comp-titles-deep-matrix-handoff](comp-titles-deep-matrix-handoff_2026-05-10.md) | **COMPLETE 2026-05-10** (4 commits). 6 lead + 9 bench (15 total) with per-comp matrix. Phase 1 web verification complete. Phase 2 deferred — see #14. | Feeds #5 §02 + #6 target list via use-plan column. | — |
| 12 | **Aeon essay (post-acceptance, two-stage)** | [aeon-essay-post-acceptance-two-stage-handoff](aeon-essay-post-acceptance-two-stage-handoff_2026-05-10.md) | **CONDITIONAL — DORMANT.** v2.0 discipline application embedded in handoff. | Fires only after Aeon accepts the pitch (#1). | Aeon acceptance. |
| 13 | **Flagship-equation terminology defense sweep (narrow + widened)** | [flagship-terms-defense-sweep-handoff](flagship-terms-defense-sweep-handoff_2026-05-11.md) | **COMPLETE 2026-05-11.** Narrow sweep `f0cebe5` + ratification/insertion (Ch 2 `8e61cd1`; Ch 5 `caa987e`; Ch 6 `1f3ad9c`). Widened sweep `34dd5b6` + insertion `2a7c336`. Cumulative: 8/11 gap-confirmed terms now have name-defense paragraphs in the manuscript. | — | — |
| 14 | **Comp-titles deep matrix v0 Phase 2** | [comp-titles-deep-matrix-phase-2-handoff](comp-titles-deep-matrix-phase-2-handoff_2026-05-11.md) | READY TO FIRE — just-in-time verification deferred work. Suggested fire window early-to-mid July 2026 (2–3 weeks before Wave 1). | Resume verification on `[verify]` flags + acquiring-editor IDs + sales-arc verification. | None blocking. |
| 15 | **Tech Appendix numbering reconciliation + chapter cross-reference re-validation** | [appendix-numbering-reconciliation-handoff](appendix-numbering-reconciliation-handoff_2026-05-11.md) | **COMPLETE 2026-05-11** (4 commits Phases 1+3A+3B+4). Scope expanded: 4 intersecting numbering schemes (not 2); all reconciled. | — | — |
| 16 | **$100 Barrel essay** (derivative from withdrawn Noema §III; Phenomenal World primary target) | [100-barrel-essay-handoff](100-barrel-essay-handoff_2026-05-11.md) | Q1 publishing-strategy rigor pass landed 2026-05-11 (`76d6fcf`) — verdict CONDITIONAL → **FLIPPED TO GO** after PM verified Conditions 2b + 2c (`b7fd20f`). Condition 1 (non-partisan framing discipline) carries forward into Stage 1 brief. | Fire Session 2 — Stage 1 audience-aware brief with Condition 1 embedded. | None blocking. |
| 17 | **Publishing pipeline** (markdown → .docx + HTML → PDF) | [publishing-pipeline-handoff](publishing-pipeline-handoff_2026-05-11.md) | NEW 2026-05-11 (`19338e9`). Apply Pandoc-based pipeline + headless-Chrome HTML→PDF. ~3–5h initial build. | Build reference.docx template + Makefile/script + Tech Appendix PDF + Glossary PDF + `tools/publishing/README.md`. | **Trigger to schedule = first submission deliverable queued** (book proposal completion; sample-chapter request; full manuscript request). |
| 18 | **Ch 6 .html → .md conversion** (companion to #17; independent) | [ch6-html-to-markdown-conversion-handoff](ch6-html-to-markdown-conversion-handoff_2026-05-11.md) | READY TO FIRE 2026-05-11 (`377d2e0`). ~1–2h focused session; convenience cleanup. | Convert `Chapter__6_ThreeWaysofCounting__Draft.html` → .md preserving math + semantic structure. | None blocking; independent of #17. |
| 19 | **Tech Appendix Scheme-4 cleanup** (companion to #15) | [appendix-scheme-4-cleanup-handoff](appendix-scheme-4-cleanup-handoff_2026-05-11.md) | READY TO FIRE 2026-05-11 (`377d2e0`). Deferred Scheme-4 work from #15 Phase 1 inventory. | Audit + apply canonical scheme to deferred Scheme-4 references. | None blocking. |
| 20 | **Manuscript Stage-3 Rigor Pass** (per-chapter + whole-book three-pass audit) | [manuscript-stage-3-rigor-pass-handoff](manuscript-stage-3-rigor-pass-handoff_2026-05-11.md) | **IN FLIGHT 2026-05-13.** Phased: Phase A = 10 parallel per-chapter Stage-3 audits (3 passes each); Phase B = whole-book audit; Phase C = per-chapter spot-fix application. User interleaving Pass-1→spot-fix→Pass-2→spot-fix cadence (valid scale-down). **Per-chapter status:**<br/>• **Ch 1:** Pass 1 COMPLETE + 11 Phase C spot-fixes applied (last `008ac3f` F-3 NASA Langley / Hampton VA). Pass 2 PROPOSED `0b78449` (v2 `6fb6510`) — awaits author ratification. Pass 3 not yet fired.<br/>• **Ch 2:** Pass 1 + Pass 2 COMPLETE + 14 spot-fixes applied (Phase C-α/β fact-check `5bc6edb` + Phase C-γ voice-polish `fa08c10`). Pass 3 (audience-load) pending — paste-text drafted.<br/>• **Ch 3:** Pass 1 LANDED `2f76e37` (Colden naming + Norway fund-age correction). Passes 2 + 3 pending.<br/>• **Ch 4:** Pass 1 COMPLETE + 5 MEDIUM + 2 LOW spot-fixes applied (`e67b8b8` + `8f792ee`). Passes 2 + 3 pending.<br/>• **Chs 5-10:** Phase A not yet started.<br/>**Cross-thread #11 (endnote/citation sweep)** accumulating M-cluster citation-tightening findings across chapters. **Audit-discipline memories captured:** `feedback_audit_recent_active_review_default.md` + `feedback_audit_open_illustrative_default.md` (both 2026-05-12). | Ratify Ch 1 Pass 2; trigger Ch 1 Pass 3; trigger Ch 2 Pass 3; trigger Ch 3 Pass 2 + Pass 3; trigger Ch 4 Pass 2 + Pass 3; fire Chs 5-10 Phase A. | None blocking. **Critical dependency:** must complete before late-June book-proposal sprint (#5) + late-July agent Wave 1 (#6). |

---

## 4. Reusable drafting-session templates (2026-05-11)

Five reusable scaffolds at `tools/drafting-templates/` (commit `e29db8c`) for fresh-session paste-text generation in any future drafting task. v2.0 discipline applied. Templates:

- Stage 1 pre-draft brief (audience-aware + canonical-facts).
- Stage 2 fresh-session draft (audience-blind).
- Stage 3 Pass 1 fact-check.
- Stage 3 Pass 2 voice-polish.
- Stage 3 Pass 3 audience-load.

Use these as starting points when generating paste-text for new fresh sessions, rather than re-deriving from scratch.

---

## 5. Submission timeline + deadline calendar

Sorted by date.

| Date | Event | Workstream | Action required |
|---|---|---|---|
| **Wed May 13 2026 14:00 ET (TODAY)** | Darity interview (phone, 1 hr) | #4 Outreach | User conducts interview; post-call synthesis triggered tonight or tomorrow |
| **Thu May 14 – Sat May 16 2026** | Sandy post-interview confirmation email window | #4 Outreach | User sends per template + warm-intro discovery reframe |
| **Wed May 20 2026 8:00am EDT** | CBF consolidated response auto-sends (Gmail scheduled-send) | #4 Outreach | No user action — automatic at 8am Wed May 20 |
| **Late May / early June 2026** | Noema Essay B submission (`edit@noemamag.com`) | #2 (post-Stage-3-polish) | Submit after USER ACTIONS 1 + 2 (Phat consent decision applied to line 136) |
| **Mon Jun 1 2026 ~00:01 AEST = Sun May 31 14:01 UTC** | Aeon pitch portal submission | #1 Aeon pitch | User submits Version C verbatim via aeon.co/pitch |
| **Jun–Aug 2026** | Aeon response window (4–8 wk) | #1 / #12 | Monitor inbox; if accepted, trigger #12 |
| **Late June 2026** | Book proposal sprint target (3-week focused effort) | #5 Book proposal | Gated on #20 completion |
| **By late June 2026** | Publishing-lawyer consultation (per cross-thread #7) | Outreach + cascade plan | User-action to schedule |
| **Late July / early August 2026** | Agent Wave 1 (8 Priority A queries) | #6 Agent prep | Gated on #20 + #5 + #14 (Phase 2 comp-titles verification) |
| **Tue Aug 5 2026** | Soft target Berggruen Prize submission | #3 Berggruen | User drafts manually (AI-free) |
| **Sun Aug 17 2026** | Hard deadline Berggruen Prize | #3 Berggruen | Submit if not already submitted |
| **Sept–Oct 2026** | Agent Wave 2 (8 Priority B) | #6 Agent prep | After Wave 1 outcomes |
| **Q4 2026 / Q1 2027** | Agent Wave 3 (9 Priority C) | #6 Agent prep | After Wave 2 outcomes |

**Critical near-term sequence (next 30 days):**

1. **Today (Wed May 13):** Darity interview at 14:00 ET. Post-call synthesis tonight or tomorrow (~5% of weekly budget). Capture insights for #2 + #5 author platform + #4 warm-intro discovery decision.
2. **May 14–20:** Sandy post-interview confirmation email (per v2 template). Continue Ch 1/2/3/4 Phase A passes. CBF response sends Wed May 20.
3. **May 20–31:** USER ACTION on Phat consent (cf. §9 below). Apply consent decision to Noema Essay B line 136. Submit Noema Essay B. Continue Stage-3 audits Chs 5-10. Final pre-submission verification of Aeon Version C.
4. **Sun May 31 14:01 UTC:** Aeon pitch submission.
5. **June:** Continue Stage-3 audits through completion. Begin book proposal sprint when #20 complete.

---

## 6. Cross-thread coordination

Items where one workstream needs something from another. Update as cross-thread items resolve. Full inventory at `publishing/strategy/cross-thread-todos.md`.

| Item | Producer | Consumer | Status |
|---|---|---|---|
| #1 Acknowledgments-page check: Sarah Chalfant ↔ Mazzucato | Outreach / verification | #6 agent prep Wave 1 | Open — partially progressed; *Value of Everything* read (no agent named); *Mission Economy* still pending |
| #2 Post-Darity warm-intro discovery | #4 Outreach | #6 Agent prep | Held — template-set drafted, awaiting Darity-interview trigger (TODAY) |
| #4 Atlantic Ideas vs. Phenomenal World slot-3 venue | Publishing strategy | Future essay slot-3 | Open — may be implicitly resolved by #16 ($100 Barrel → PW) |
| #5 Boston Review v2.0 application | PM meta-verdict | #2 Boston Review session | RESOLVED 2026-05-10 (handoff updated) |
| #6 Aeon post-acceptance v2.0 application | PM meta-verdict | #12 Aeon post-acceptance session | RESOLVED 2026-05-10 (handoff updated) |
| #7 Interview-attribution protocol jurisdictional gaps | PM session | Protocol-update session + publishing-lawyer | Protocol v2 codification COMPLETE 2026-05-11 (`998166f`); publishing-lawyer consultation user-action target by late June |
| #8 Comp-titles deep matrix Phase 2 | #11 → #14 | #6 Agent prep Wave 1; #5 §04 marketing plan | Open — dormant until early-to-mid July 2026 |
| #9 Ch 2 GuidanceDoc stale "$100 barrel passage" references | #10 audit | Insight #37 GuidanceDoc→Draft staleness Batch-D | Open — small standalone fix-session or bundled into Batch-D pass |
| #10 PM-verified apparatus-stability checkpoint for $100 Barrel (#16) | Q1 rigor pass | #16 fire decision | RESOLVED 2026-05-11 — Conditions 2b + 2c verified; #16 verdict flipped CONDITIONAL → GO with Condition 1 carry-forward |
| #11 Endnote / citation-finalization sweep (accumulating) | Per-chapter Phase A audits (#20) | Eventual coordinated endnote sweep | Open — accumulating; Ch 2 contributed 9 M + 1 L items; Ch 4 contributed 5 M + 3 L; soft target after Phase B; hard target before late-July Wave 1 |
| Author-bio updates as essays place / interviews land | #4 + essay submissions | #5 author platform | Continuous |

---

## 7. Two-stage drafting discipline v2.0 — RATIFIED + CODIFIED

Status: **RATIFIED 2026-05-10. CODIFIED 2026-05-10 (commit `9caccdc`).**

The methodology meta-experiment closed. v2.0 amendments A + B + C all in force:

- **Amendment A — Stage 1 brief enrichment for personal-narrative content.** Stage 1 briefs must include canonical factual ground truth (not just beats).
- **Amendment B — Stage 3 split into three distinct passes** (fact-check + voice-polish + audience-load).
- **Amendment C — Domain-of-applicability rule.** Apply when (a) artifact derives from existing chapter/source prose at Path B contamination risk, OR (b) source has apparatus/jargon that would tripwire the venue, OR (c) artifact is long-form publisher-facing material drafted without a strong iterated control. Don't apply when a strong iterated control already exists for short-form material. Untested for short-form with no iterated control.

Memory: `feedback_audience_aware_drafting_discipline.md` (v2.0).
Application: every long-form publisher-facing essay session inherits this by default. Boston Review handoff (#2) + Aeon post-acceptance handoff (#12) embed v2.0-application sections. Stage-3-rigor-pass workstream (#20) is the manuscript-level analogue.

Reusable scaffolds at `tools/drafting-templates/` (see §4).

---

## 8. Outreach pipeline detail

Per `outreach-pipeline-handoff_2026-05-09.md`. Update as responses land.

| Subject | Affiliation | Status | Date | Notes |
|---|---|---|---|---|
| **William ("Sandy") Darity Jr.** | Duke | INTERVIEW TODAY | Wed May 13 14:00 ET (1 hr phone) | Full prep stack ready. Substitution-hypothesis-applied draft of Section V already exists; interview = upgrade opportunity. Post-call: send confirmation email per v2 template May 14–16; surface warm-intro discovery (Kendi / Cook Center / Gates / Mullen implicit). |
| **Mariana Mazzucato** | UCL/IIPP | HOLDING via Adam Albrecht | Held since 2026-05-06 | Awaiting substantive follow-up. Not blocking any submission. |
| **Allison Colden** | CBF Maryland | RESPONSE SENT via Val DiMarzio (consolidated thread) | 2026-05-13 (drafted; scheduled-send Wed May 20 8am EDT) | Public-record brief landed 2026-05-08. **Substitution-hypothesis CONFIRMED.** Pre-publication citation-verification packet pre-staged 2026-05-13 (`15c6b0f`) — user-action to send ahead of book publication. |
| **Karen Moore** | CBF Virginia | RESPONSE SENT via David Sherfinski (consolidated thread) | 2026-05-13 (drafted; scheduled-send Wed May 20 8am EDT) | Public-record brief landed 2026-05-08. |
| **Biggie family (Ch 3 deceased subject)** | — | Process guide pre-staged 2026-05-13 (`164b9e2`) | — | Courtesy-notification process ready; outreach pending user-decision per `feedback_named_subject_consent.md`. |
| **Boyce, Buller, Mian, Sufi, Alperovitz, Mondragon, Klein, Coalition of Clinics, Raworth, ACLC, Lipcius, Mann** | Various | Cold-outreach sent | 2026-05-05 | Standard 2–3 wk academic-response window. Some replies may have landed — verify before quoting. |

---

## 9. Active todo list

Sorted by urgency. **The PM session maintains this list.** Update as items complete or new items surface.

### Today (Wed May 13)

- [ ] **Conduct Darity interview** Wed May 13 14:00 ET (phone, 1 hr).
- [ ] **Post-Darity synthesis** (tonight or tomorrow; ~5% weekly budget). Capture insights for #2 Boston Review essay + #5 author platform + warm-intro discovery decision.

### This week (by Sun May 17)

- [ ] **Send Sandy post-interview confirmation email** (window May 14–16) per v2 template at `research/outreach/subjects/sandy/post-interview-email-template_v2_2026-05-11.md`. Apply warm-intro discovery reframe based on what Darity surfaced.
- [ ] **Ratify Ch 1 Pass 2 (voice-polish) findings** `0b78449` (re-landed v2 `6fb6510`) → apply Phase C voice-polish spot-fixes for Ch 1.
- [ ] **Trigger Ch 1 Pass 3 (audience-load).** Paste-text generation from PM session.
- [ ] **Trigger Ch 2 Pass 3 (audience-load).** Paste-text drafted; user to fire.
- [ ] **Trigger Ch 3 Pass 2 (voice-polish) + Pass 3 (audience-load).** Paste-text generation from PM session.
- [ ] **Trigger Ch 4 Pass 2 (voice-polish) + Pass 3 (audience-load).** Paste-text generation from PM session.
- [ ] **Fire Chs 5-10 Phase A** as bandwidth permits — parallel sessions paced by user.

### USER ACTIONS gating Noema submission

- [ ] **USER ACTION 1 — Reach out to Phat (or Phat's family if Phat unavailable) for signed consent to use his name in publisher-facing prose.** Package ready at `research/outreach/subjects/phat/` per commits `585d535` + `721c094` + `9aee0af`. Per `feedback_named_subject_consent.md`, living named subjects must be anonymized until signed.
- [ ] **USER ACTION 2 (after Action 1 resolves) — Apply consent decision to Essay B at line 136 of `manuscript/essay/Noema/noema-essay-fresh-session-draft_2026-05-10.md`.** Current anonymized text: *"a crabber and fisherman my father had known since he was small."* Branches:
  - If consent **signed** → restore Phat's actual name.
  - If consent **not signed / declined / unreachable** → leave anonymization as-drafted.
  - Either decision unblocks Noema submission.
- [ ] **USER ACTION 3 — Apply same consent decision to Ch 3** wherever Phat appears in `manuscript/chapters/Chapter__3_TheWaterman__Draft.md`.

### Next 2–3 weeks (by Fri May 31)

- [ ] **Fire $100 Barrel essay (#16) Session 2** — Stage 1 audience-aware brief with Condition 1 (non-partisan framing discipline) embedded.
- [ ] **Continue Stage-3 audits Chs 5-10 Phase A.**
- [ ] **Final pre-submission verification of Aeon Version C** (1–2 days before Jun 1).
- [ ] **Submit Noema essay** to `edit@noemamag.com` (gated on USER ACTIONS 1 + 2 above).
- [ ] **Submit Aeon pitch** Mon Jun 1 ~00:01 AEST.
- [ ] **Send Colden pre-publication citation-verification packet** ahead of Ch 3 publication courtesy (user-action; `15c6b0f`).

### Substantive backlog

- [ ] **Boston Review pitch + essay drafting** (#2). UNBLOCKED; v2.0 discipline application embedded. Fire when bandwidth permits.
- [ ] **Bibliography engagement-pending → engaged flag updates** (#7 cross-thread).
- [ ] **Tech Appendix Phase 3 v2.0.0 rebuild** (#7). UNBLOCKED 2026-05-11 by #15.
- [ ] **Glossary v4 rebuild** (#7). UNBLOCKED 2026-05-11 by #9 + #15.
- [ ] **Ch 6 .html → .md conversion** (#18). ~1–2h focused session when scheduling permits.
- [ ] **Tech Appendix Scheme-4 cleanup** (#19). Smaller-scope follow-up to #15.
- [ ] **Comp-titles Phase 2** (#14). Suggested fire window early-to-mid July 2026.
- [ ] **Cross-thread #9 — Ch 2 GuidanceDoc stale "$100 barrel passage" references.**

### Late summer (by mid-August)

- [ ] **Berggruen Prize essay** drafting (#3). User-only, AI-free. Soft target 2026-08-05; hard deadline 2026-08-17.
- [ ] **Book proposal sprint** (#5). Late June 2026 target. Gated on #20.

### Conditional / dormant

- [ ] **#12 Aeon essay (post-acceptance two-stage)** — fires only if Aeon accepts the pitch.
- [ ] **Biggie courtesy-notify-surviving-family-if-reachable** before any essay using his name publishes. Process guide pre-staged 2026-05-13.
- [ ] **Publishing pipeline (#17)** — trigger to schedule = first submission deliverable queued.

---

## 10. How to handle common user prompts

- **"What should I do next?"** → Cross-reference §3 (status) + §5 (deadlines) + §9 (todos). Recommend the highest-leverage unblocked item that fits the user's available time/energy.
- **"I just finished X." / "X session is done."** → Auto-verify per §10.5 (origin/main + artifact spot-check) BEFORE marking complete. Then mark the todo complete in §9, update the workstream's status in §3 with verifying commit hash + one-line evidence, surface what unblocks (§6 cross-thread).
- **"Give me text to paste into a fresh session for X."** → Generate paste-text per the appropriate handoff + drafting-templates scaffold. Paste-text only; do NOT execute the work yourself.
- **"What's blocked?"** → §3 column "Blocker." Filter on items with non-empty blockers.
- **"What's overdue?"** → §5, items with past dates that aren't marked complete.
- **"What does workstream X need?"** → Read the workstream's handoff (linked in §3). Summarize: read order, deliverables, first actions.
- **"Add a todo: ..."** → Insert into §9 at appropriate priority. If substantive enough, propose creating a new handoff.
- **Day-of-week / date assertions** → Verify against a known anchor before asserting. Today (per harness): **Wed May 13, 2026.** Past day-of-week errors in PM session caused calendar drift; treat date claims with staleness discipline.

When you don't know — say so. Verify before asserting (per `feedback_verify_stale_memory_claims.md`).

---

## 10.5. Auto-verify discipline (RATIFIED 2026-05-10)

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
   - Artifacts missing one or more deliverables (session promised 3 files; only 2 landed).
   - Content doesn't match spec (headers wrong, word counts outside band, named-subject discipline broken, apparatus terms where prohibited).
   - Conflicts with parallel session work (same file modified incompatibly).

**Verbosity tradeoff.** Default rigor: medium — verify commit on origin/main + key content spot-check; report tight 3–5 line summary. User can request lighter or heavier on per-session basis.

---

## 10.6. Parallel-PM-session collision risk

**Pattern observed during 2026-05-10 → 2026-05-13 session window:** multiple PM sessions running in parallel sometimes edit the same handoff file, causing rebase failures on push. Resolution that worked: abort the in-progress rebase, reset to origin/main, accept the parallel session's canonical state.

**Mitigation for this session forward:** before any edit to `pm-session-handoff_<DATE>.md` or related coordination files, fetch origin/main first. If a parallel PM session has just pushed, reconcile rather than rebase-and-overwrite. Prefer SHORT, ATOMIC edits to the dashboard rather than long pending diffs that risk collision.

---

## 11. Updating this handoff

This file IS the PM session's working memory. Update it as state changes:

- When a workstream's status changes, update §3.
- When a deadline passes, archive it (move to history section or delete) and update §5.
- When a todo completes, mark `[x]` in §9 (short-term retention) or remove (cleanup).
- When new workstreams emerge, add to §3 + create their handoff in `tools/workstream-handoffs/`.
- When stale claims surface, correct in place.

**Periodic full-file refresh:** every ~7–14 days, or after any significant phase shift, write a successor file (`pm-session-handoff_<NEW-DATE>.md`) that supersedes this one. Update `tools/workstream-handoffs/README.md` to point to the latest. Mark the predecessor superseded (header note + dashboard-handoff pointer).

**Predecessor:** `pm-session-handoff_2026-05-10.md` (covers 2026-05-10 → 2026-05-13 session window; superseded by this file).

---

## 12. Reference inventory

**Index files:**
- `tools/workstream-handoffs/README.md` — workstream handoff index
- `publishing/strategy/cross-thread-todos.md`
- `publishing/strategy/cascade-plan_2026-05-06.md`
- `publishing/strategy/decisions-log.md`

**Memory entries (read MEMORY.md for full index):**
- `project_book1_state_2026-05-10.md` — current project state snapshot
- `feedback_audience_aware_drafting_discipline.md` — v2.0 two-stage discipline
- `feedback_named_subject_consent.md` — naming discipline (Biggie / Phat)
- `feedback_voice_polish_pipeline.md` — dump → sift → polish
- `feedback_substance_drives_length.md` — no arbitrary word targets
- `feedback_verify_stale_memory_claims.md` — verification discipline
- `feedback_two_layer_content_discipline.md` — internal-vs-external content origination
- `feedback_audit_recent_active_review_default.md` — audit conflict resolution (2026-05-12)
- `feedback_audit_open_illustrative_default.md` — open/illustrative audit default (2026-05-12)
- `feedback_grammatical_role_cross_references.md` — chapter→appendix cross-reference discipline
- `feedback_dual_audience_test.md` — trade-press polish dual-audience test
- `reference_sandel_hybrid_pattern.md` — acronym treatment hybrid pattern

**Workstream handoffs (full index in §3):**
- 7 from 2026-05-09 + 5 from 2026-05-10 + 8 from 2026-05-11. See `tools/workstream-handoffs/README.md`.

**Reusable drafting-session templates:**
- `tools/drafting-templates/` — Stage 1 pre-draft brief, Stage 2 fresh-session draft, Stage 3 Passes 1+2+3 (commit `e29db8c`).

---

*End of PM session handoff. Update in place as state evolves; write successor file ~weekly.*
