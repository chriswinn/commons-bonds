# Project Management Session — Handoff (2026-05-10)

**Date drafted:** 2026-05-10
**Branch to create at session start:** `claude/pm-session-<harness-id>` (branch from current `origin/main`)
**Session type:** **Parallel coordination session.** Runs alongside the user's per-workstream sessions. Does NOT execute workstream tasks; tracks state, surfaces dependencies, manages the todo list, flags deadlines, routes work between sessions.

---

## 0. Mission of the PM session

You are the PM coordination session. Your job is to keep the *Commons Bonds* project's many parallel workstreams legible to the author. The author opens and closes individual sessions for specific workstreams (Path B audit, comp-titles deep matrix, agent prep, etc.) and uses this session as the central tracker.

**You execute:**
- Status updates after the user reports completing work in another session
- Todo-list management (add / reorder / complete / clean up stale items)
- Deadline tracking and alerts
- Workstream sequencing recommendations ("what should I do next?")
- Dependency surfacing ("X is blocked on Y; do Y first")
- Cross-thread coordination (what one workstream needs from another)
- Periodic ground-truth verification (file counts, git log, workstream state) — see `feedback_verify_stale_memory_claims.md`

**You do NOT execute:**
- Actual workstream work (drafting, auditing, editing). Those live in their dedicated handoffs.
- Content decisions (those need user input).
- Submissions (those happen in dedicated sessions per submission strategy).
- Memory updates beyond status corrections (substantive memory work happens in topical sessions).

When the user asks "what's next?" — synthesize from this dashboard + their recent activity + upcoming deadlines.
When the user reports finishing a task — update this file's status, mark the todo complete, surface what unblocks.
When the user wants to add a task — capture, prioritize, flag dependencies.

---

## 1. Read order

1. THIS file (you are here).
2. `tools/workstream-handoffs/README.md` — the index of all workstream handoffs.
3. The two staleness-aware memory entries: `feedback_verify_stale_memory_claims.md` and `project_book1_state_2026-05-10.md`.
4. `publishing/strategy/cross-thread-todos.md` — items requiring another thread's action.
5. `publishing/strategy/cascade-plan_2026-05-06.md` — strategic cascade state.
6. `publishing/strategy/decisions-log.md` — strategic decisions history.

You do NOT need to read the individual workstream handoffs unless the user asks for details on a specific one. Index-level knowledge is enough for coordination.

---

## 2. Current phase summary (as of 2026-05-10)

The project is in the **manuscript-verification + publishing-pipeline-deepening + parallel-essay-submissions** phase. Drafting phase complete (10 chapters + AuthorsNote drafted).

Three work streams are active simultaneously:

- **Manuscript verification** — making sure chapters meet success criteria. Triggered by Path B discovery on 2026-05-10 (Noema essay had ~14 verbatim sentences from Ch 1; same dynamic plausibly exists across chapter pairs).
- **Publishing pipeline** — book proposal + agent target list + comp-titles deep matrix. Late-June 2026 proposal-sprint target; late-July / early-August Wave 1 agent queries.
- **Essay submissions** — Aeon pitch (Mon Jun 1 portal); Noema essay (late May / early June); Boston Review pitch + essay (TBD); Berggruen Prize essay (deadline 2026-08-17, AI-free).

Plus a meta-experiment **complete** as of 2026-05-10: **two-stage drafting discipline test** (Stage 2 + Stage 3 both completed; meta-verdict synthesized; v2.0 ratified by user 2026-05-10 with Amendments A + B + C; codification committed to main as `9caccdc`).

---

## 3. Workstream dashboard

| # | Workstream | Handoff | Status | Next action | Blocker | Owner |
|---|---|---|---|---|---|---|
| 1 | **Aeon pitch submission** | [aeon-submission-handoff](aeon-submission-handoff_2026-05-09.md) | READY TO SEND. Version C ratified 2026-05-08; Stage 3 verdict 2026-05-10 (commit `db4798e`) confirmed Version C beats Pitch B decisively. Submit verbatim, no fusion. | Submit Mon Jun 1 ~00:01 AEST. | None — awaiting submission date. | User (manual portal submission) |
| 2 | **Boston Review essay** | [boston-review-essay-handoff](boston-review-essay-handoff_2026-05-09.md) | UNBLOCKED 2026-05-10 by meta-verdict. Pitch + essay not yet drafted. Source Ch 5 ready. **Cross-thread:** apply two-stage discipline v2.0 (RATIFIED 2026-05-10) as default — long-form publisher-facing essay drafted from chapter prose = the regime v2.0 covers. Stage 1 enrichment with canonical facts required if memoir register present. | Draft pitch (~1pp) + essay (~4,500w from Ch 5). | None blocking — workstream-ready. | Fresh session needed |
| 3 | **Berggruen Prize essay** | [berggruen-track-handoff](berggruen-track-handoff_2026-05-09.md) | **AI-free required.** Deadline 2026-08-17. Soft target 2026-08-05. | Author drafts outside any AI-assisted session. | AI-free constraint. | User (manual writing) |
| 4 | **Outreach pipeline** | [outreach-pipeline-handoff](outreach-pipeline-handoff_2026-05-09.md) | 6 subjects in flight. **Darity interview TODAY Wed May 13 14:00 ET.** Consolidated CBF response draft (Val DiMarzio + David Sherfinski) landed 2026-05-13 via PR #4 merge `75d74e6` + 3 prior commits — awaits author send. Colden pre-publication citation-verification packet landed 2026-05-13 (`15c6b0f`) — ahead of Ch 3 publication courtesy. | Conduct Darity interview today; post-call synthesis tonight or tomorrow; send CBF consolidated response when ready; send Colden citation-verification packet ahead of book publication. Mazzucato follow-up via Adam Albrecht. | Awaiting Mazzucato substantive reply; awaiting other cold-outreach replies. | User (interviews + sends) + future session (synthesis) |
| 5 | **Book proposal** | [book-proposal-handoff](book-proposal-handoff_2026-05-09.md) | Skeletons stood up; comp-titles substantive (~80%); bio polished. | Late-June 2026 sprint (~3-week focused effort). | Comp-titles deep matrix work (#11) feeds this. | Fresh session for sprint |
| 6 | **Agent prep / target list** | [agent-prep-handoff](agent-prep-handoff_2026-05-09.md) | 1/25 populated (Sarah Chalfant / Wylie). Template + tracker + snippets seeded. | Populate 7 more Priority A targets. Wave 1 late July / early Aug 2026. | Comp-titles deep matrix (#11) feeds agent intelligence. | Fresh session (research-heavy) |
| 7 | **Manuscript completion** | [manuscript-completion-handoff](manuscript-completion-handoff_2026-05-09.md) | Stale-header fix landed 2026-05-10 (commit `5cd2c15`). All 10 chapters now reflected accurately. Bibliography flag-updates + Tech Appendix v2.0.0 + Glossary v4 still pending. | Continue bibliography flag-updates + appendix/glossary rebuild. | Tech Appendix + Glossary rebuilds best to wait until #9 apparatus sweep commits land. | Fresh session |
| 8 | **Path B audit cross-chapter** | [path-b-audit-cross-chapter-handoff](path-b-audit-cross-chapter-handoff_2026-05-10.md) | **COMPLETE 2026-05-11** (commits `5643f70` + `71146da` + final-deliverable `bbf06f2`). Two contaminations resolved (Ch 5↔Ch 6 Restitution Lineage; Ch 2↔Ch 6↔Ch 8 Black Lung); one verified clean (Ch 5↔Ch 9 Sweden); remaining priority pairs deliberately deferred (diminishing returns). Standing-reference doc at `research/audits/cross-chapter-path-b-audit_2026-05-11.md`. | — | — | — |
| 9 | **Apparatus register decision sweep** | [apparatus-register-sweep-handoff](apparatus-register-sweep-handoff_2026-05-10.md) | **COMPLETE 2026-05-11** (final-deliverable `bbf06f2`). 13 ratified items (Items 1–11, 14, 15); 2 Path B fixes; adjacent issues handled in-session; adjacent issues flagged for separate workstreams. Standing-reference rigor-pass at `tools/rigor-passes/commons_bonds_rigor_pass_2026-05-11_apparatus_register_decision_v1.0.0.md`. | — | — | — |
| 10 | **Cross-chapter consistency audit** | [cross-chapter-consistency-handoff](cross-chapter-consistency-handoff_2026-05-10.md) | **COMPLETE 2026-05-11** (5 commits: `46b175b` Phases 1+2 + `b645806` Batch 1 + `9695b67` Batch 2 + `93dd2c4` Batch 3 + `c3b0cc9` Batch 4). Standing-reference artifacts at `research/audits/cross-chapter-consistency-audit_2026-05-11.md` + `tools/audits/cross-chapter-consistency-inventory_2026-05-11.md`. Headline finding: manuscript in unusually strong consistency shape; 2 of 8 dimensions returned ZERO drift. | — | — | — |
| 11 | **Comp-titles deep matrix** | [comp-titles-deep-matrix-handoff](comp-titles-deep-matrix-handoff_2026-05-10.md) | **COMPLETE 2026-05-10** (commits `519bbce` + `4860530` + `18a49af` + `d64a9ab`). 6 lead + 9 bench (15 total) with full per-comp matrix; Phase 1 web verification on Wylie cluster + Darity & Mullen pre-interview; Chalfant cross-thread reconciliation embedded. | Feeds book-proposal sprint (#5) §02 + agent target list (#6) per use-plan column of each entry. | None — completed. | — |
| 12 | **Aeon essay (post-acceptance, two-stage)** | [aeon-essay-post-acceptance-two-stage-handoff](aeon-essay-post-acceptance-two-stage-handoff_2026-05-10.md) | **CONDITIONAL — DORMANT.** Stage 3 verdict landed 2026-05-10. **Cross-thread:** when this fires, apply discipline v2.0 (RATIFIED 2026-05-10) — Stage 1 enrichment with canonical Ch 7 facts required since the essay derives from Ch 7 (Path B risk identical to the Noema test). | Fires only after Aeon accepts the pitch (#1). | Aeon acceptance only (Stage 3 verdict no longer a blocker). | Future session post-trigger |
| 13 | **Flagship-equation terminology defense sweep (narrow)** | [flagship-terms-defense-sweep-handoff](flagship-terms-defense-sweep-handoff_2026-05-11.md) | NEW 2026-05-11. Triggered by bond-defense work (commits `f5f905e` → `1c83753`) surfacing a generalizable gap pattern: foundational framework choices asserted but never defended in body prose. Narrow first over 4 terms (CS / RCV / Restitution Bond / Foreclosure Bond) before any widening. | Gap-audit per term; draft + 3-pass rigor pass for confirmed gaps; widening recommendation. | None blocking — workstream-ready. Complementary to #9 (apparatus = jargon decisions; this = "keep these names + justify them"). | Fresh session (paste-text drafted by PM) |
| 14 | **Comp-titles deep matrix v0 Phase 2** | [comp-titles-deep-matrix-phase-2-handoff](comp-titles-deep-matrix-phase-2-handoff_2026-05-11.md) | NEW 2026-05-11 (commit `38dbc15`). Phase 1 v0 landed 2026-05-10 (#11 marked complete); Phase 2 is the just-in-time deferred verification work (specific BookScan numbers, blurb verification across full comp set, etc. — items marked `[verify]` in v0). | Resume verification on per-comp `[verify]` flags. | None blocking. | Future session |
| 15 | **Tech Appendix numbering reconciliation + chapter cross-reference re-validation** | [appendix-numbering-reconciliation-handoff](appendix-numbering-reconciliation-handoff_2026-05-11.md) | **COMPLETE 2026-05-11** (4 commits: `7002003` Phase 1 + `b903f0f` Phase 3A canonical-scheme application + `8f5c416` Phase 3B annotated TOC + `4b53320` Phase 4 chapter + glossary + terms-index re-validation). Scope-expansion finding during Phase 1: 4 intersecting numbering schemes, not 2; reconciliation handled all four. Audit inventory at `tools/workstream-handoffs/appendix-numbering-audit-inventory_2026-05-11.md`. | — | — | — |
| 16 | **$100 Barrel essay** (derivative from withdrawn Noema §III; Phenomenal World primary target) | [100-barrel-essay-handoff](100-barrel-essay-handoff_2026-05-11.md) | Q1 publishing-strategy rigor pass landed 2026-05-11 (`76d6fcf`) with verdict CONDITIONAL. **PM verification of Conditions 2b + 2c cleared 2026-05-11 → verdict FLIPS TO GO** with Condition 1 (non-partisan framing discipline) carrying forward into Stage 1 brief. Apply v2.0 audience-aware drafting; PW-specific Stage 1 brief with non-partisan framing pressure-test set per Condition 1. Q1 rigor pass at `tools/rigor-passes/commons_bonds_rigor_pass_2026-05-11_100_barrel_essay_q1_go_no_go_v1.0.0.md`. | Fire Session 2 — Stage 1 audience-aware brief with Condition 1 embedded. | None blocking. | Fresh session — fire when ready |
| 17 | **Publishing pipeline** (markdown → .docx + HTML → PDF for publisher-ready artifacts) | [publishing-pipeline-handoff](publishing-pipeline-handoff_2026-05-11.md) | NEW 2026-05-11 (`19338e9`). Surfaced during Tech Appendix #15 Phase 5 — draft-format-vs-submission-format question. Current state: 9 chapters .md + Ch 6 .html + Tech Appendix v2.0.0 styled HTML + Glossary v4 styled HTML. US trade publishing convention requires .docx manuscript-formatted for agent/publisher submission. Apply Pandoc-based pipeline + headless-Chrome HTML→PDF. | Build reference.docx template + Makefile/script + Tech Appendix PDF + Glossary PDF + tools/publishing/README.md. ~3–5h initial build. | None blocking; **trigger to schedule = first submission deliverable queued** (book proposal completion; sample-chapter request; full manuscript request). | Fresh session (eventual; schedule per trigger) |
| 18 | **Ch 6 .html → .md conversion** (companion to publishing pipeline #17; independent) | [ch6-html-to-markdown-conversion-handoff](ch6-html-to-markdown-conversion-handoff_2026-05-11.md) | NEW 2026-05-11 (`377d2e0`). ~1–2h focused session; eliminates Ch 6 hybrid-format anomaly. Pipeline (#17) handles Ch 6 in either format, so this is convenience not requirement. | Convert Chapter__6_ThreeWaysofCounting__Draft.html → .md preserving math + semantic structure. | None blocking; independent of #17. | Fresh session when convenient |
| 19 | **Tech Appendix Scheme-4 cleanup** (companion to #15) | [appendix-scheme-4-cleanup-handoff](appendix-scheme-4-cleanup-handoff_2026-05-11.md) | NEW 2026-05-11 (`377d2e0`). Deferred from #15 Phase 1 inventory — the "embedded supplement re-started §-numbering at h4/h5 level" scheme that the main reconciliation deferred. Smaller-scope follow-up to #15. | Audit + apply canonical scheme to the deferred Scheme-4 references. | None blocking; companion to (completed) #15. | Fresh session when convenient |
| 20 | **Manuscript Stage-3 Rigor Pass** (per-chapter + whole-book three-pass audit) | [manuscript-stage-3-rigor-pass-handoff](manuscript-stage-3-rigor-pass-handoff_2026-05-11.md) | **IN FLIGHT 2026-05-13.** Phased: Phase A = 10 parallel per-chapter Stage-3 audits; Phase B = whole-book audit; Phase C = per-chapter spot-fix application. User interleaving Pass-1→spot-fix→Pass-2→spot-fix cadence (valid scale-down). **Status by chapter:** Ch 1 Pass 1 (fact-check) COMPLETE + 11 spot-fixes applied (incl. F-3 today `008ac3f`); Ch 1 Pass 2 (voice-polish) RIGOR-PASS LANDED `0b78449` [PROPOSED — awaits author ratification]; Ch 1 Pass 3 + Ch 3 Pass 1 in flight; remaining chapters pending. | Author ratifies Ch 1 Pass 2 voice-polish findings → Phase C application sessions per ratified findings. Trigger Ch 1 Pass 3 (audience-load) when ready. | None blocking. **Critical dependency:** must complete BEFORE late-June book-proposal sprint. | Per-chapter sessions paced by user |

---

## 4. Special-case fresh-session handoffs (one-shot, not workstreams)

These drive single fresh-session tasks for the two-stage drafting discipline experiment. Each produces a single artifact and stops.

| Task | Handoff | Status | Output |
|---|---|---|---|
| **Stage 2 — Noema essay (Essay B)** | [noema-session-handoff_2026-05-10](../../manuscript/essay/Noema/noema-essay-fresh-session-draft_2026-05-10.md) | **COMPLETE 2026-05-10**. | `manuscript/essay/Noema/noema-essay-fresh-session-draft_2026-05-10.md` |
| **Stage 2 — Aeon pitch (Pitch B)** | [aeon-session-handoff_2026-05-10](../../manuscript/essay/aeon/aeon-pitch-fresh-session_2026-05-10.md) | **COMPLETE 2026-05-10**. | `manuscript/essay/aeon/aeon-pitch-fresh-session_2026-05-10.md` |
| **Stage 3 — Noema comparison** | n/a (PM-paste-driven session) | **COMPLETE 2026-05-10. Verdict: B WINS, mixed.** Submit Essay B with surgical Stage 3 polish (5 factual fixes + 2 voice improvements). | `tools/rigor-passes/commons_bonds_rigor_pass_2026-05-10_noema_stage3_comparison_v1.0.0.md` |
| **Stage 3 — Aeon pitch comparison** | n/a (PM-paste-driven session) | **COMPLETE 2026-05-10. Verdict: A WINS, decisive.** Submit Version C verbatim Mon Jun 1; no fusion. | `tools/rigor-passes/commons_bonds_rigor_pass_2026-05-10_aeon_pitch_stage3_comparison_v1.0.0.md` |
| **Meta-verdict synthesis (PM session)** | this file §7 | **COMPLETE 2026-05-10. Partial validation, refined regime:** discipline = default for long-form publisher-facing essays (~3,000+w) drafted from chapter prose; not for short-form pitches against iterated controls. | Recorded in §7 below + as new application-rule todo for substantive memory codification. |
| **Stage 3 polish — Essay B → submission-ready** | (NEW workstream; needs handoff) | **PENDING — not yet triggered.** Surgical spot-fixes only; no Path B reintroduction. | Updated Essay B file ready for late May / early June Noema submission. |

---

## 5. Submission timeline + deadline calendar

Sorted by date.

| Date | Event | Workstream | Action required |
|---|---|---|---|
| **Wed May 13 2026 14:00 ET** | Darity interview (phone, 1 hr) — rescheduled 2026-05-11 from Tue May 12 14:00 ET (Sandy's granddaughter pickup conflict) | #4 Outreach | User conducts interview; PM session prompts post-call synthesis |
| **Late May / early June 2026** | Noema essay submission (`edit@noemamag.com`) | #2 (post-Stage-3-polish workstream) | Essay B confirmed by Stage 3 verdict 2026-05-10; submit after surgical polish session lands the 6 factual fixes + 2 voice improvements per Noema verdict §6 |
| **Mon Jun 1 2026 ~00:01 AEST = Sun May 31 14:01 UTC** | Aeon pitch portal submission | #1 Aeon pitch | User submits Version C verbatim via aeon.co/pitch |
| **Jun–Aug 2026** | Aeon response window (4–8 wk) | #1 / #12 | Monitor inbox; if accepted, trigger #12 |
| **Late June 2026** | Book proposal sprint target (3-week focused effort) | #5 Book proposal | Fresh session for sprint |
| **Late July / early August 2026** | Agent Wave 1 (8 Priority A queries) | #6 Agent prep | After comp-titles matrix complete + book proposal substantive |
| **Tue Aug 5 2026** | Soft target Berggruen Prize submission | #3 Berggruen | User drafts manually (AI-free) |
| **Sun Aug 17 2026** | Hard deadline Berggruen Prize | #3 Berggruen | Submit if not already submitted |
| **Sept–Oct 2026** | Agent Wave 2 (8 Priority B) | #6 Agent prep | After Wave 1 outcomes |
| **Q4 2026 / Q1 2027** | Agent Wave 3 (9 Priority C) | #6 Agent prep | After Wave 2 outcomes |

Critical near-term sequence (next 30 days):
1. **May 11–13:** Darity interview prep complete; **interview rescheduled 2026-05-11 → Wed May 13 14:00 ET** (Sandy's granddaughter pickup conflict on Tue May 12). User maintaining prep state across 2-day buffer. Post-call synthesis (~5% of remaining weekly budget) fires May 13 evening or May 14. Post-call confirmation email window May 14–16.
2. **May 11–25:** Stage 2 + Stage 3 + meta-verdict + v2.0 ratification + codification — **all complete 2026-05-10**. Trigger Noema Essay B Stage 3 polish session for the 6 surgical fact-fixes per Noema verdict §6.1. Optionally fire other parallel-safe workstreams (#11 comp-titles; #8+#9 Path B + apparatus bundle; #1 cross-thread Chalfant follow-up).
3. **May 25–31:** Noema Essay B submission (post-polish). Final pre-submission verification of Aeon Version C.
4. **Sun May 31 14:01 UTC:** Aeon pitch submission.

---

## 6. Cross-thread coordination

Items where one workstream needs something from another. Update as cross-thread items resolve.

| Item | Producer | Consumer | Status |
|---|---|---|---|
| Comp-titles deep matrix | #11 Comp-titles | #5 Book proposal §02; #6 Agent prep target list; #5 §04 marketing plan | Pending — start when ready |
| Path B + apparatus findings | #8 Path B audit + #9 Apparatus sweep | #2 Boston Review essay (Ch 5 source); #12 Aeon essay (Ch 7 source); future essays | Pending — start when ready |
| Bibliography engagement-pending → engaged flag updates | #7 Manuscript completion | All future essays + #5 book proposal | In progress per `manuscript-completion-handoff_2026-05-09.md` cross-thread item #3 |
| Stage 3 methodology verdict | Stage 3 comparison session | Determines whether two-stage discipline becomes default for #2, #12, future essays, and #5 cover letter | **RESOLVED 2026-05-10.** v2.0 ratified with Amendments A + B + C; codified into memory + Boston Review handoff + Aeon-post-acceptance handoff via commit `9caccdc`. |
| Darity interview material | #4 Outreach | #2 Boston Review essay (potentially); #5 book proposal author-platform §03 (interview-placement table) | Will land May 12 evening; synthesize day-of or next day |
| Author-bio updates as essays place / interviews land | #4 + essay submissions | #5 Book proposal §03 author platform | Continuous; update as events happen |

---

## 7. Two-stage drafting discipline experiment status

The methodology experiment is the meta-workstream. Track separately.

| Stage | Status | Artifact |
|---|---|---|
| **Stage 1 (pre-draft, both tests)** | COMPLETE 2026-05-10 | Noema: `tools/rigor-passes/commons_bonds_rigor_pass_2026-05-10_noema_essay_pre_draft_audience_structure_v1.0.0.md`. Aeon: `tools/rigor-passes/commons_bonds_rigor_pass_2026-05-10_aeon_pitch_pre_draft_audience_structure_v1.0.0.md`. |
| **Stage 2 (fresh-session draft, Noema)** | **COMPLETE 2026-05-10** | `manuscript/essay/Noema/noema-essay-fresh-session-draft_2026-05-10.md` |
| **Stage 2 (fresh-session draft, Aeon pitch)** | **COMPLETE 2026-05-10** | `manuscript/essay/aeon/aeon-pitch-fresh-session_2026-05-10.md` |
| **Stage 3 (comparison)** | **COMPLETE 2026-05-10**. Per-test verdicts: Noema **B WINS, mixed**; Aeon **A WINS, decisive**. | `tools/rigor-passes/commons_bonds_rigor_pass_2026-05-10_noema_stage3_comparison_v1.0.0.md` + `..._aeon_pitch_stage3_comparison_v1.0.0.md` |
| **Meta-verdict (PM session synthesis)** | **COMPLETE 2026-05-10**. Per the verdict matrix entry "B wins / A wins" → "Long-form / weak-control benefits; short / strong-control doesn't." **Partial validation, refined regime:** discipline = default for long-form publisher-facing essays (~3,000+w) drafted from chapter prose; not default for short-form pitches against iterated controls. Untested for short-form material with no iterated control. | Recorded inline below + memory codification queued as separate topical-session todo. |
| **Methodology v2.0 ratification (user)** | **RATIFIED 2026-05-10.** Amendments A + B + C accepted: Stage 1 canonical-facts enrichment; Stage 3 split into fact-check + voice-polish + audience-load passes; domain-of-applicability rule. | Memory codification + cross-thread handoff updates queued as topical session (paste-text drafted by PM session). |

**Verdict matrix** (per Stage 1 brief §10):

| Noema test | Aeon test | Interpretation |
|---|---|---|
| B wins | B wins | **Strong validation.** Discipline becomes default. |
| B wins | A wins | Long-form / weak-control benefits; short / strong-control doesn't. Diagnose. |
| A wins | B wins | Inverse — surprising. Diagnose. |
| A wins | A wins | **Falsified.** Reconsider whether to keep the framework. |
| Mixed | Mixed | Most likely outcome. **Partial validation.** Codify v2.0 framework. |

---

## 8. Outreach pipeline detail

Per `outreach-pipeline-handoff_2026-05-09.md`. Update as responses land.

| Subject | Affiliation | Status | Date | Notes |
|---|---|---|---|---|
| **William ("Sandy") Darity Jr.** | Duke | INTERVIEW CONFIRMED | Tue May 12 14:00 ET (1 hr phone) | Full prep stack ready. Substitution-hypothesis-applied draft of Section V already exists; interview is upgrade opportunity. |
| **Mariana Mazzucato** | UCL/IIPP | HOLDING via Adam Albrecht | Held since 2026-05-06 | Awaiting substantive follow-up. Not blocking any submission. |
| **Allison Colden** | CBF Maryland | RESPONSE SENT via Val DiMarzio | 2026-05-06 | Public-record brief landed 2026-05-08. **Substitution-hypothesis CONFIRMED.** Live interview not load-bearing. |
| **Karen Moore** | CBF Virginia | RESPONSE SENT via David Sherfinski | 2026-05-06 | Public-record brief landed 2026-05-08. Live interview not load-bearing. |
| **Boyce, Buller, Mian, Sufi, Alperovitz, Mondragon, Klein, Coalition of Clinics, Raworth, ACLC, Lipcius, Mann** | Various | Cold-outreach sent | 2026-05-05 | Standard 2–3 wk academic-response window. Some replies may have landed since 2026-05-09 — verify before quoting. |

---

## 9. Active todo list (synthesized from all workstreams + experiments + memory)

Sorted by urgency. **The PM session maintains this list.** Update as items complete or new items surface.

### This week (by Sun May 17)

- [x] **Trigger Stage 2 fresh session for Noema essay** (Essay B). Triggered + completed 2026-05-10.
- [x] **Trigger Stage 2 fresh session for Aeon pitch** (Pitch B). Triggered + completed 2026-05-10.
- [x] **Receive Stage 2 Noema artifact** at `manuscript/essay/Noema/noema-essay-fresh-session-draft_2026-05-10.md`. ✓
- [x] **Receive Stage 2 Aeon-pitch artifact** at `manuscript/essay/aeon/aeon-pitch-fresh-session_2026-05-10.md`. ✓
- [x] **Run Stage 3 comparison** for both methodology tests. ✓ Both verdicts landed 2026-05-10.
- [x] **Decide which Noema essay (A or B) to submit** based on Stage 3 verdict. ✓ **Decision: submit Essay B** (post-surgical-Stage-3-polish).
- [ ] **Trigger Noema Essay B Stage 3 polish session.** Surgical spot-fixes; spot-fix-only, no Path B reintroduction. **The 6 fixes per Noema Stage 3 verdict §6.1:**
  1. Restore canonical Pou/Pooh nickname etymology (sister's-son-pointing-and-naming origin; replace invented Tidewater-accent backstory).
  2. Verify or correct predawn-Appalachian-drives framing (canonical: hunting-trip, not Navy commute).
  3. Reconstruct air-compressor anecdote as a scene (per Stage 1 §4 anchor list; Section II Lock per audience-load).
  4. Correct "fifteen audiences" framing (canonical: 15 distinct reader audiences for the research, not 15 meetings).
  5. Correct "responsible for forty-five people" framing (canonical: project planned for 45; author cut back to proof-of-concept).
  6. Revert cussing-scene direction to cursing-at-self (not cursing-at-recipient).
  Plus the 2 voice improvements per §6.2 (tighten expository flatness; optionally import bundling-synthesis sentence). Blocks Noema submission.
- [ ] **Conduct Darity interview** Tue May 12 14:00 ET.
- [ ] **Post-Darity synthesis** (~5% of remaining weekly budget). Capture insights for #2 Boston Review essay + #5 book proposal author platform + Section V upgrade decision.

### Methodology v2.0 — RATIFIED 2026-05-10

User ratified v2.0 with all three amendments A + B + C on 2026-05-10. The discipline is now v2.0 canonical for future application; v1.0 superseded. Memory codification + cross-thread handoff updates remain to be applied (topical session).

**The three ratified v2.0 amendments:**

- [x] **Amendment A — Stage 1 brief enrichment for personal-narrative content.** Stage 1 briefs must include canonical factual ground truth (not just beats), so fresh Stage 2 sessions don't improvise facts. Driven by Noema Stage 3 finding: 5+ factual drift points in Essay B (Pou nickname etymology fabricated; predawn-drives reframed as commute; fifteen-audiences misread as meetings; 45-people misframed as managed; cussing scene redirected; air-compressor compressed to summary). Fix at Stage 1, not at Stage 3.
- [x] **Amendment B — Stage 3 split into three distinct passes** (rather than one bundled rigor pass): (a) **fact-check pass** — does prose match canonical author truth; (b) **voice-polish pass** — catches expository flatness, meta-commentary, LLM tics that pass-1 used to catch; (c) **audience-load pass** — the existing v1.0 pass. Distinct passes prevent fact-check signal from being lost in voice-polish noise.
- [x] **Amendment C — Domain-of-applicability rule.** Apply when (a) artifact derives from existing chapter/source prose at Path B contamination risk, OR (b) source has apparatus/jargon that would tripwire the venue, OR (c) artifact is long-form publisher-facing material drafted without a strong iterated control. **Don't apply when:** a strong iterated control already exists for short-form material — iterate carefully instead. **Untested:** short-form material with no iterated control.

**Pending application of the ratification:**

- [x] **v2.0 codification session — COMPLETE 2026-05-10** (commit `9caccdc`). Memory `feedback_audience_aware_drafting_discipline.md` updated v1.0 → v2.0; Boston Review handoff updated; Aeon-post-acceptance handoff updated; cross-thread-todos items #5 and #6 created-and-resolved as coordination markers.

### Next 2–3 weeks (by Fri May 31)

- [ ] **Final pre-submission verification of Aeon Version C** (1–2 days before Jun 1).
- [ ] **Submit Noema essay** to `edit@noemamag.com`. Gated on USER ACTION 1 + 2 above (Phat's consent decision applied to line 136).
- [ ] **Submit Aeon pitch** Mon Jun 1 ~00:01 AEST.

### Recently landed (2026-05-10 PM session window)

- [x] **A2 Op-ed pipeline drafts** — COMPLETE 2026-05-10 (commit `5167edd`). Three artifacts on main: canonical-facts inventory + Norway op-ed (1,016w body) + McDowell op-ed (1,024w body). Both Path-B-clean (0 verbatim from source chapters); both apparatus-clean (0 framework terms). News-peg lede slots adapt-able. Pipeline activated — ready for 1–2 day turnaround when triggers arrive. Notable: the session's own Stage 3 fact-check pass caught real drift (GPFG founding-date conflation; Bondevik-coalition timing), validating v2.0 Amendment B in practice on first run.
- [x] **A3 Comp-titles deep matrix v0** — COMPLETE 2026-05-10 (commits `519bbce` + `4860530` + `18a49af` + `d64a9ab`). 6 lead + 9 bench (15 total) with full per-comp matrix structure: bibliographic anchor, positioning, sales arc, agent intelligence (with HIGH/MEDIUM/LOW confidence flags), mechanism overlap, network signals, audience overlap, use plan. Phase 1 web verification covered Wylie cluster (Mazzucato/Tooze/Sandel) + Darity & Mullen pre-interview. Chalfant cross-thread finding reconciled via `d64a9ab`.
- [x] **Bibliography §13 engagement-flag updates (cross-thread #3)** — COMPLETE 2026-05-10 (bundled into `519bbce`). Pistor / Christophers / Susskind (Growth) + Susskind (A World Without Work) all updated from "engagement pending" → specific section references with word counts. Cross-thread-todos item #3 ready to move to Resolved.
- [x] **Apparatus register Item 1 — Ch 8 inline integral removed from trade prose** — COMPLETE 2026-05-10 (`d1f6e2d`). Plain-English summation + Tech Appendix cross-reference preserved. Surgical fix, no collateral damage.
- [x] **Apparatus register Item 2 — Ch 6 formula lead-in tightened** — COMPLETE 2026-05-10 (`baf3776`). Defensive 35-word lead-in compressed to "a summary of the plain-English argument just made". Formula block + term translation kept (Ch 6 = methodology chapter, earns apparatus).
- [x] **Apparatus register Item 3 — Ch 6 keep CS/IPG shorthand identities; fix subscript + encoding** — COMPLETE 2026-05-10 (`39a8416`).
- [x] **Apparatus register Item 4 — Ch 5 Deepwater B / RCV ≈ 0.40 symbol rewrite** — COMPLETE 2026-05-10 (`4d012fb`).
- [x] **Apparatus register Item 5 — Ch 5 Restitution/Foreclosure Bond names; drop B₁/B₂ subscripts** — COMPLETE 2026-05-10 (`19e91d1`).
- [x] **Apparatus register Item 6 — CSD acronym + residual B/B₁/B₂ subscript cleanup** — COMPLETE 2026-05-10 (`547346a`).
- [x] **Apparatus register Item 7 — Ch 6 CIT acronym expanded → Commons Inversion Test** — COMPLETE 2026-05-11 (`4f32743`).
- [x] **Apparatus register Item 8 — Ch 6 Hotelling Identity polish (Option C)** — COMPLETE 2026-05-11 (`067f5a1`).
- [x] **Path B fix — Ch 5 ↔ Ch 6 Restitution Lineage clone resolved** — COMPLETE 2026-05-11 (`5643f70`).
- [x] **Path B fix — Ch 2 ↔ Ch 6 ↔ Ch 8 Black Lung Trust Fund three-way echo resolved** — COMPLETE 2026-05-11 (`71146da`).
- [x] **Ch 3 — Fox Hill / Biggie / Phat integration + register pass + VMRC date correction** — COMPLETE 2026-05-11 (`b5692f1`).
- [x] **Phat consent package (inventory + document + process guide; Ch 3 extension; name framing + shop contact)** — COMPLETE 2026-05-11 (commits `585d535` + `721c094` + `9aee0af`). Package ready for user to take to Phat.
- [x] **Bibliography §13 — Darity & Mullen *From Here to Equality* entry added** — COMPLETE 2026-05-11 (`629a25e`).
- [x] **Post-Darity warm-intro discovery reframe + template-set (4 candidates: Kendi lead, Cook Center colleagues, Gates wildcard, Mullen implicit secondary)** — COMPLETE 2026-05-11 (`e24251a`). Cross-thread #2 reframed.
- [x] **Sandy post-interview template — v2 protocol layers + warm-intro reframe** — COMPLETE 2026-05-11 (`cd094bb`). Refines the initial template per cross-thread #7 + #2.
- [x] **Why-bonds umbrella-term justification paragraph (Ch 5 insertion)** — COMPLETE 2026-05-11 (commits `f5f905e` + `47bd6d4` + `2c8138f` + `1c83753`). Bond-defense methodology established; mirrored in workstream #13.
- [x] **Comp-titles Phase 2 handoff stood up** — COMPLETE 2026-05-11 (`38dbc15`). Just-in-time verification deferred work; workstream #14.
- [x] **Apparatus register Item 9 — Ch 6 α-dominance replaced with named navigation aid** — COMPLETE 2026-05-11 (`cf682be`).
- [x] **Apparatus register Item 10 — Ch 6 + Ch 7 appendix cross-references with named content (Abundance Masking + Theorem E.3 etc.)** — COMPLETE 2026-05-11 (`16876a1`). Surfaced the Tech Appendix dual-numbering issue → workstream #15 stood up.
- [x] **Tech Appendix §7-vs-§8 ARR numbering reconcile** — COMPLETE 2026-05-11 (`ede6d88`). Partial / first-pass fix; full reconciliation queued in workstream #15.
- [x] **Tech Appendix numbering reconciliation workstream stood up** at `tools/workstream-handoffs/appendix-numbering-reconciliation-handoff_2026-05-11.md` + dashboard row #15 added. (UNBLOCKED 2026-05-11 by #9 finishing.)
- [x] **Apparatus register Items 11 + 14 + 15 + Item 11 follow-up + Item 14 follow-up** — COMPLETE 2026-05-11 (`76cb0e4` + `cfde88c` + `214af4a` + `5f143b0` + `b1c17d8`).
- [x] **#8 Path B audit cross-chapter — COMPLETE** 2026-05-11 (final-deliverable `bbf06f2`). Two contaminations fixed, one verified clean, remaining priority pairs deliberately deferred. Standing-reference at `research/audits/cross-chapter-path-b-audit_2026-05-11.md`.
- [x] **#9 Apparatus register decision sweep — COMPLETE** 2026-05-11 (final-deliverable `bbf06f2`). 13 ratified items + standing-reference rigor-pass at `tools/rigor-passes/commons_bonds_rigor_pass_2026-05-11_apparatus_register_decision_v1.0.0.md`.
- [x] **#13 Flagship-equation terminology defense sweep (narrow) — COMPLETE** 2026-05-11 (`f0cebe5`). **4/4 GAP CONFIRMED + WIDENING RECOMMENDED.** 4 draft defense paragraphs + 4 audience-load rigor passes landed; all 4 awaiting author ratification for chapter insertion.
- [x] **#10 Cross-chapter consistency audit — UNBLOCKED** by #8 + #9 finishing.
- [x] **Interview-attribution protocol v2 codification session — COMPLETE** 2026-05-11 (`998166f`). Recording-consent + jurisdiction-aware + EU/UK GDPR layers + post-interview correspondence template-set. Time-sensitive deadline met (before 2026-05-13 post-Darity workflow).
- [x] **Proposal §05 chapter summaries — COMPLETE** 2026-05-11 (`733ba8e`). All 10 chapters covered; ~514w per chapter (5,137w total); drafting notes section appended. Pre-work for late-June book-proposal sprint landed.
- [x] **Path B audit documentation patch — Ch 2 ↔ Ch 3 + Ch 3 ↔ Ch 8 priority pair** — COMPLETE 2026-05-11 (`9c189b3`). Fills the documentation gap in the Path B audit final-deliverable doc; Ch 2/Ch 3 priority pair coverage was always done but not previously written up.
- [x] **Stale-reference sweep — central equation + Ch 7 illustrative-not-exhaustive** — COMPLETE 2026-05-11 (`42e8644`). Cleanup commit.
- [x] **Narrow-sweep flagship-term defense paragraphs RATIFIED + INSERTED into chapters** — COMPLETE 2026-05-11. All 4 verdicts (a) INCLUDE as-is. Commits: Ch 2 Cost Severance (`8e61cd1`); Ch 5 Restitution + Foreclosure Bond (`caa987e`); Ch 6 Residual Commons Value (`1f3ad9c`). Results doc appended with ratification record (`28efce3`).
- [x] **Widened flagship-terms-defense sweep — COMPLETE 2026-05-11** (`34dd5b6`). 7 widened terms audited: 4 GAP CONFIRMED + INCLUDE (CIT, ARR, Externality Tail, Abundance Masking); 3 NO GAP (Hotelling Identity, Cᵢ component set, three-method-convergence-for-RCV). Cumulative narrow + widened: 8/11 GAP + INCLUDE. 4 new draft defense paragraphs + audience-load rigor passes await author ratification.
- [x] **Noema Essay B Stage 3 polish session** — COMPLETE 2026-05-10 (commit `44c66b6`). All 6 fact-fixes per verdict §6.1 + 2 voice improvements per §6.2 + §6.2.8 bundling-synthesis import applied. Verified directly: Pou/Pappou canonical scene replaces Tidewater backstory; air-compressor scene reconstructed; cursing-at-self reverted; bundling sentence in Section VI; locked Section I closing paragraph verbatim. Path B residual ~3–4 verbatim sentences (unchanged from pre-polish). Body word count 4,930w.

### User actions gating Noema submission

- [ ] **USER ACTION 1 — Reach out to Phat (or Phat's family if Phat unavailable) for signed consent to use his name in publisher-facing prose.** Per `feedback_named_subject_consent.md`, living named subjects must be anonymized until signed.
- [ ] **USER ACTION 2 (after Action 1 resolves) — Apply consent decision to Essay B at line 136 of `manuscript/essay/Noema/noema-essay-fresh-session-draft_2026-05-10.md`.** Current anonymized text reads: *"a crabber and fisherman my father had known since he was small."* Decision branches:
  - If consent **signed** → restore Phat's actual name (replace the anonymized phrasing with the named version).
  - If consent **not signed / declined / unreachable** → leave anonymization as-drafted; no edit required.
  - Either decision unblocks the Noema submission.

### Substantive backlog (no specific date — sequence based on user priority + dependencies)

- [x] **Path B audit cross-chapter** (#8) — **COMPLETE 2026-05-11** (final-deliverable `bbf06f2`).
- [x] **Apparatus register decision sweep** (#9) — **COMPLETE 2026-05-11** (final-deliverable `bbf06f2`; 13 ratified items + standing-reference rigor-pass artifact).
- [x] **Cross-chapter consistency audit** (#10). **COMPLETE 2026-05-11** (5 commits: Phases 1+2 inventory+findings + Batches 1-4 fixes). Headline: manuscript in unusually strong consistency shape; 2 of 8 dimensions returned ZERO drift.
- [x] **Comp-titles deep matrix v0** (#11). **COMPLETE 2026-05-10** (4 commits).
- [ ] **Comp-titles deep matrix v0 Phase 2** (#14). Just-in-time verification deferred work; future session.
- [x] **Flagship-equation terminology defense sweep (narrow)** (#13). **COMPLETE 2026-05-11** (`f0cebe5`). 4/4 narrow drafts ratified + inserted into chapters (Ch 2 / Ch 5×2 / Ch 6).
- [x] **Tech Appendix numbering reconciliation + chapter cross-reference re-validation** (#15). **COMPLETE 2026-05-11** (4 commits Phases 1+3A+3B+4). Scope expanded mid-flight: 4 intersecting numbering schemes (not 2); all reconciled.
- [x] **Widened flagship-terms-defense sweep** — COMPLETE 2026-05-11 (`34dd5b6` + ratification + insertion `2a7c336`). All 4 widened drafts (CIT, ARR, Externality Tail, Abundance Masking) ratified + inserted into Ch 6 + Ch 7. Cumulative narrow+widened: 8/11 gap-confirmed terms now have name-defense paragraphs in the manuscript.
- [x] **Update manuscript-completion-handoff** to remove the stale "9 of 10 chapters; excluding Ch 3" header. **DONE 2026-05-10** (commit `5cd2c15`); Ch 3 row + title + status line + workstream scope + README "Excluded" → "Resolved exclusions" all updated cleanly.
- [ ] **Bibliography engagement-pending → engaged flag updates** (#7 cross-thread item #3).
- [ ] **Tech Appendix Phase 3 v2.0.0 rebuild** (#7 queued). **UNBLOCKED 2026-05-11** by #15 finishing — canonical numbering scheme now stable.
- [ ] **Glossary v4 rebuild** (#7 queued). **UNBLOCKED 2026-05-11** by #9 + #15 both finishing.
- [ ] **Publishing pipeline** (#17). Trigger = first submission deliverable queued. Connects to book proposal (#5) + agent prep (#6) + manuscript completion (#7) — those workstreams' submission artifacts depend on this infrastructure.
- [ ] **Ch 6 .html → .md conversion** (#18). Independent of #17; convenience cleanup. ~1–2h focused session when scheduling permits.
- [ ] **Boston Review pitch + essay drafting** (#2). **UNBLOCKED 2026-05-10** by Stage 3 meta-verdict — apply two-stage discipline as default (long-form publisher-facing essay; meta-verdict-validated regime).

### Late summer (by mid-August)

- [ ] **Berggruen Prize essay** drafting (#3). User-only, AI-free. Soft target 2026-08-05; hard deadline 2026-08-17.
- [ ] **Book proposal sprint** (#5). Late June 2026 target.

### Conditional / dormant

- [ ] **#12 Aeon essay (post-acceptance two-stage)** — fires only if Aeon accepts the pitch.
- [ ] **Phat's signed consent** (per `feedback_named_subject_consent.md`) — restore name in essays if/when signed before submission.
- [ ] **Biggie courtesy-notify-surviving-family-if-reachable** before any essay using his name publishes.

---

## 10. How to handle common user prompts

The user will likely come to you with questions like these. Suggested responses:

- **"What should I do next?"** → Cross-reference §3 (status) + §5 (deadlines) + §9 (todos). Recommend the highest-leverage unblocked item that fits the user's available time/energy.
- **"I just finished X."** / **"X session is done."** → Auto-verify per §10.5 (origin/main + artifact spot-check) BEFORE marking complete. Then mark the todo complete in §9, update the workstream's status in §3 with the verifying commit hash + one-line evidence, surface what unblocks (§6 cross-thread).
- **"What's blocked?"** → §3 column "Blocker." Filter on items with non-empty blockers.
- **"What's overdue?"** → §5, items with past dates that aren't marked complete.
- **"How is the methodology experiment going?"** → §7. Surface what stage we're at.
- **"What does workstream X need?"** → Read the workstream's handoff (linked in §3). Summarize: read order, deliverables, first actions.
- **"Add a todo: ..."** → Insert into §9 at appropriate priority. If it's substantive enough to warrant its own workstream, propose creating a new handoff.
- **"Status update on the budget / token usage"** → User's Anthropic weekly budget tracker is external; you can ask the user to report state and reflect it back.

When you don't know — say so. Verify before asserting (per `feedback_verify_stale_memory_claims.md`).

---

## 10.5. Auto-verify discipline (RATIFIED 2026-05-10)

**Trigger conditions.** PM session auto-verifies origin/main canonical state before marking ANY workstream / todo / dashboard row complete. Triggers:

- User reports a session finished ("X session is done" / "X completed and pushed").
- PM session notices new commits on origin/main during a routine fetch.
- PM session is about to mark anything complete on the dashboard.

No formal "Note & Verify" gate is required from the user — the auto-verify is the PM session's own discipline.

**Why this exists.** Sessions sometimes report "complete and pushed" when they only pushed to their feature branch, not origin/main. The auto-verify catches that failure mode + several others before stale-state reaches the dashboard.

**The verification protocol.**

1. **Fetch origin/main.** `git fetch origin main`.
2. **Confirm the commit(s) exist on origin/main.** `git log origin/main --oneline | grep <hash>` — if the commit is only on a feature branch, report back to user and do NOT mark complete.
3. **Direct-inspect the artifact(s).** `ls` the expected files, spot-check key content against the session's spec (header metadata, expected sections, expected diff pattern, word counts within bands, etc.).
4. **If clean:** mark complete on the dashboard with the commit hash + a one-line verification evidence note (e.g., "verified: artifact at `<path>` contains `<expected content>`; commit on origin/main").
5. **If something's off:** flag it before marking anything. Common failure modes:
   - Commit only on local branch (not pushed to origin/main).
   - Artifacts missing one or more deliverables (e.g., session promised 3 files; only 2 landed).
   - Content doesn't match spec (headers wrong, word counts outside band, named-subject discipline broken, apparatus terms present where prohibited).
   - Conflicts with parallel session work (same file modified in incompatible ways).

**Verbosity tradeoff.** Default rigor: medium — verify commit on origin/main + key content spot-check, report a tight 3–5 line summary. User can request lighter ("just confirm commit on main + filename match") or heavier ("read the full draft and report any issues") on a per-session basis.

**What the user provides.** Just the trigger — "X session finished" — is enough. PM does the verification work; user spot-checks the dashboard's verification-evidence notes.

---

## 11. Updating this handoff

This file IS the PM session's working memory. Update it as state changes:

- When a workstream's status changes (e.g., #1 from "ready to send" → "submitted"), update §3.
- When a deadline passes, archive it (move to a "history" section at the bottom or delete) and update §5.
- When a todo completes, mark it `[x]` in §9 (for short-term retention) or remove it (for cleanup).
- When new workstreams emerge, add to §3 + create their handoff in `tools/workstream-handoffs/` per existing pattern.
- When stale claims are surfaced (per `feedback_verify_stale_memory_claims.md`), correct in place.

**Periodic full-file refresh:** every ~7–14 days, or after any significant phase shift, write a successor file (`pm-session-handoff_<NEW-DATE>.md`) that supersedes this one. Update the workstream-handoffs README.md to point to the latest. Delete or archive the predecessor.

---

## 12. Reference inventory

**This handoff's index files:**
- `tools/workstream-handoffs/README.md` — workstream handoff index
- `publishing/strategy/cross-thread-todos.md`
- `publishing/strategy/cascade-plan_2026-05-06.md`
- `publishing/strategy/decisions-log.md`

**Memory entries (read MEMORY.md for full index):**
- `project_book1_state_2026-05-10.md` — current project state snapshot
- `feedback_audience_aware_drafting_discipline.md` — two-stage rule
- `feedback_named_subject_consent.md` — naming discipline (Biggie / Phat's)
- `feedback_voice_polish_pipeline.md` — dump → sift → polish
- `feedback_substance_drives_length.md` — no arbitrary word targets
- `feedback_verify_stale_memory_claims.md` — verification discipline (added 2026-05-10)
- `feedback_two_layer_content_discipline.md` — internal-vs-external content origination

**Workstream handoffs (full index in §3 above):**
- 7 from 2026-05-09 + 5 from 2026-05-10. See `tools/workstream-handoffs/README.md`.

**Two-stage discipline experiment artifacts:**
- Stage 1 briefs: `tools/rigor-passes/commons_bonds_rigor_pass_2026-05-10_*_pre_draft_audience_structure_v1.0.0.md`
- Stage 2 handoffs: `manuscript/essay/Noema/noema-session-handoff_2026-05-10.md` + `manuscript/essay/aeon/aeon-session-handoff_2026-05-10.md`
- Stage 3 protocol: embedded in Stage 1 brief §10/§11 of each test

---

*End of PM session handoff. Update in place as state evolves; write successor file ~weekly.*
