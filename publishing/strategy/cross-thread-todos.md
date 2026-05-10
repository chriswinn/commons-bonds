# Cross-thread TODOs

**Date drafted:** 2026-05-09  ·  **Date modified:** 2026-05-10

**Purpose.** Single living source-of-truth for items where one thread surfaces work that another thread needs to act on. Reduces lookup cost — currently these items are scattered across decisions-log entries, commit messages, and cascade-plan notes, and risk being lost between threads.

**Discipline.** Append-only. Each item: surfaced-by · for-thread · status · context · target-resolution. Move to "Resolved" section when closed (with date + resolving commit/decision).

**Not the right home for:**
- Decisions internal to a single thread (those live in that thread's decisions-log)
- General open questions not requiring another thread's action
- Routine-thread work (handled by scheduled-agent routines per `tools/routines/proposed_routines_v1.0.0.md`)

---

## Open

### 1. Acknowledgments-page check: Sarah Chalfant ↔ Mazzucato

- **Surfaced by:** publishing-strategy thread (2026-05-08 agent-prep work; cascade plan Decisions due #8; commit `406e522`)
- **For-thread:** any thread/session with access to *Mission Economy* (2021) physical book or Publishers Marketplace deal records
- **Status:** partially-progressed (2026-05-10) — *Value of Everything* check completed and did NOT resolve; *Mission Economy* check still pending; resolution paths broadened
- **Context:** Sarah Chalfant identified as top Wylie-agent candidate via public-record check 2026-05-08. Acknowledgments-page check 2026-05-10 read *The Value of Everything* (2018) Acknowledgments in full from the Penguin/Allen Lane edition PDF: **no literary agent is named at all**. Editor Tom Penn at Penguin is thanked, along with copy editor Michael Prest, academic readers, IIPP staff, and family — but no agent. The original premise "Mazzucato almost certainly thanks her agent by name" is partially falsified — academic authors often omit agents from acknowledgments. *Mission Economy* (2021) Acknowledgments not yet accessible online (Perlego TOC confirms section exists but text behind paywall; archive.org / Scribd searches turned up no full-text PDF). Mazzucato's own contact page (`marianamazzucato.com/about/contact/`) lists "The Wylie Agency" generically with an Executive Assistant, no individual agent named. The Wylie clients page lists Mazzucato but provides no individual-agent attribution.
- **Resolution paths remaining:** (a) physical-book check of *Mission Economy* Acknowledgments — most efficient if a copy is reachable; (b) Publishers Marketplace deal-record subscription lookup for *The Value of Everything* (PublicAffairs 2018) or *Mission Economy* (Harper Business 2021) — deal records typically name the selling agent; (c) direct query via Mazzucato/IIPP network if the Adam Albrecht warm-thread converts to substantive contact. If none of these resolve before Wave 1, fall back to generic agency intake `mail@wylieagency.co.uk` (degraded path but workable).
- **Target resolution:** before any Wylie query goes out (Wave 1, target late July / early August 2026). Soft target: prior to proposal sprint completion (late June 2026). If still unresolved by then, plan for generic-intake submission.

### 2. Mullen warm-intro activation post-Darity

- **Surfaced by:** outreach thread (Darity-track decision)
- **For-thread:** outreach thread
- **Status:** held
- **Context:** A. Kirsten Mullen (co-author with Darity of *From Here to Equality* + *Umbrellas Don't Make It Rain*) — Gmail draft on hold; activation deferred to end of Darity interview 2026-05-12 if conversation goes well. Decision criterion: Sandy Darity's reception of the framework + willingness to facilitate Mullen connection.
- **Target resolution:** end of Darity interview 2026-05-12 (hard trigger: post-call decision).

### 3. Bibliography engagement-pending flag updates

- **Surfaced by:** publishing-strategy thread (2026-05-08 cross-thread TODO; commit `6c08112` queued the engagement work)
- **For-thread:** manuscript / bibliography thread
- **Status:** in-flight (manuscript engagement landed via commit `d78872e`; bibliography flag updates pending)
- **Context:** Pistor, Christophers, Susskind entries in `research/literature/bibliography.md` §13 carry "engagement pending" status flags from when they were added 2026-05-08. The Ch 5 + Ch 9 engagement paragraphs landed on main 2026-05-08 (commit `d78872e` "Comp author engagement: Pistor + Christophers + Susskind across Ch 5 + Ch 9 + bibliography"). The bibliography entries should be updated from "engagement pending" → "engaged in Ch X §Y" with specific section references, so future pre-publication review (Insight #39) sees the engagement-state correctly without needing footnote audits.
- **Target resolution:** before late-June proposal sprint (so chapter summaries can cite the bibliography's current engagement state).

### 4. Decision: Atlantic Ideas vs. Phenomenal World for slot-3 primary venue

- **Surfaced by:** publishing-strategy thread (2026-05-09 venue-survey work)
- **For-thread:** publishing-strategy thread (decision required from author)
- **Status:** open
- **Context:** Cascade plan currently lists Atlantic Ideas as essay-slot-3 fallback. Phenomenal World (Jain Family Institute) is more accessible without prior clips; Atlantic Ideas has more name-recognition prestige but expects established bylines. With Boston Review taking Ch 5 (essay slot 2), the slot-3 source chapter is naturally Ch 9 *Pricing Honestly*. Decision determines which venue gets the Ch 9 pitch and timing.
- **Target resolution:** before slot-3 pitch drafting begins (target Sept-Oct 2026 per cascade plan).

---

## Resolved

| Resolved date | Item | Resolution |
|---|---|---|
| 2026-05-08 | Ch 5 + Ch 9 paragraph engagement (Pistor + Christophers + Susskind) | Landed in commit `d78872e` "Comp author engagement: Pistor + Christophers + Susskind across Ch 5 + Ch 9 + bibliography" |
| 2026-05-08 | Aeon Version A vs. B fate | Resolved via Version C ratification (commits `384b2df` + `24d2e79`); Version A held as alternative; Version B deleted |
| 2026-05-08 | `draft2.md` overlap quarantine | Archived to `archive/_OneDayMaybe/withdrawn-essays/draft2_withdrawn-noema_2026-05-01.md` with §I wife's-illness excised (commit `2d8da6a`) |
| 2026-05-08 | Colden + Moore CBF substitution-hypothesis (Ch 3 + Noema §V third-anchor) | Public-record briefs landed (Colden `0e83dc5` + `fffd202`; Moore `c352d9a`); substitution-hypothesis CONFIRMED for both |
| 2026-05-09 | Noema essay 100% drafted-able | Hybrid operational approach ratified (commit `9aee18d`); Section V Darity sub-portion now draftable from public-record quote-mining; May 12 interview = upgrade opportunity, not precondition |
| 2026-05-10 | #5 — Two-stage drafting discipline v2.0: codify Boston Review essay application | v2.0 ratified 2026-05-10 (Amendments A + B + C). `tools/workstream-handoffs/boston-review-essay-handoff_2026-05-09.md` updated with v2.0-application section flagging regime fit (clauses a + b + c all fire), three-pass Stage 3 structure, and Path B preemptive policy. Codification + handoff update landed in same-session commit (this commit). |
| 2026-05-10 | #6 — Two-stage drafting discipline v2.0: codify Aeon post-acceptance essay application | v2.0 ratified 2026-05-10 (Amendments A + B + C). `tools/workstream-handoffs/aeon-essay-post-acceptance-two-stage-handoff_2026-05-10.md` updated with v2.0-application section flagging regime fit (clauses a + b + c all fire — long-form derived from Ch 7 + Ch 8 + Ch 1, no strong iterated control), Stage 1 canonical-factual-ground-truth requirement (per Amendment A — driven by Noema Stage 3's 5+ factual drift catalog), three-pass Stage 3 structure, and Path B preemptive policy. Codification + handoff update landed in same-session commit (this commit). |

---

## Update log

- **2026-05-09.** File created. Four open items captured: Sarah Chalfant acknowledgments-page check; Mullen warm-intro activation post-Darity; bibliography engagement-pending flag updates; Atlantic Ideas vs. Phenomenal World slot-3 decision. Five resolved items logged from 2026-05-08 through 2026-05-09.
- **2026-05-10.** Item #1 (Sarah Chalfant acknowledgments check) updated: status moved open → partially-progressed. *Value of Everything* (2018) Acknowledgments read in full — no agent named, partially falsifying the original "agent thanked by name" assumption. *Mission Economy* check + Publishers Marketplace lookup remain outstanding. Resolution paths broadened; generic-intake fallback explicitly contemplated.
- **2026-05-10.** Two-stage drafting discipline v2.0 codification session landed. Items #5 (Boston Review v2.0 application) and #6 (Aeon post-acceptance v2.0 application) created and resolved in the same atomic commit — both workstream handoffs updated with v2.0-application sections per the ratified Amendments A (Stage 1 canonical factual ground truth, not just beats), B (three distinct Stage 3 passes — fact-check, voice-polish, audience-load), and C (domain-of-applicability rule). Empirical basis: Noema Stage 3 verdict (`tools/rigor-passes/commons_bonds_rigor_pass_2026-05-10_noema_stage3_comparison_v1.0.0.md`, commit `a9b627c`) drove Amendments A + B; Aeon Pitch Stage 3 verdict (`tools/rigor-passes/commons_bonds_rigor_pass_2026-05-10_aeon_pitch_stage3_comparison_v1.0.0.md`, commit `db4798e`) drove Amendment C. Memory entry `feedback_audience_aware_drafting_discipline.md` updated v1.0 → v2.0; MEMORY.md index updated. Items #5 and #6 are tracked here as resolved (not previously open) because they are coordination markers for downstream sessions to discover that the two workstream handoffs now embed v2.0 as default — they are not future work to-do.
