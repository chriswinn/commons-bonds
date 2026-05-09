# Cross-thread TODOs

**Date drafted:** 2026-05-09  ·  **Date modified:** 2026-05-09

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
- **For-thread:** any thread/session with access to Mazzucato's books or Publishers Marketplace deal records
- **Status:** open
- **Context:** Sarah Chalfant identified as top Wylie-agent candidate via public-record check 2026-05-08. Acknowledgments-page confirmation of her Mazzucato representation hasn't been done. Check *Mission Economy* (2021) or *The Value of Everything* (2018) acknowledgments pages — Mazzucato almost certainly thanks her agent by name. If a different agent is named (likely Tracy Bohan, the senior London-office agent), update `publishing/agents/targets.md` + `publishing/agents/personalization-snippets.md` accordingly.
- **Target resolution:** before any Wylie query goes out (Wave 1, target late July / early August 2026). Soft target: prior to proposal sprint completion (late June 2026).

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

---

## Update log

- **2026-05-09.** File created. Four open items captured: Sarah Chalfant acknowledgments-page check; Mullen warm-intro activation post-Darity; bibliography engagement-pending flag updates; Atlantic Ideas vs. Phenomenal World slot-3 decision. Five resolved items logged from 2026-05-08 through 2026-05-09.
