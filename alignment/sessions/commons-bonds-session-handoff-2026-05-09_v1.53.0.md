# Session handoff v1.53.0 — full project state-snapshot — 2026-05-09

**Purpose:** Comprehensive state-snapshot across all workstreams as of 2026-05-09 evening. Supersedes v1.52.0 (2026-05-06). Layered as the canonical orientation file for next-session-Claude across drafting, outreach, essay-track, agent-prep, book-proposal, and framework-cascade work.

**Reading time:** ~10 minutes. Self-contained — pick up any single workstream without re-reading prior handoffs.

**Going-forward operating mode:** per author direction 2026-05-09, fresh sessions start on per-workstream dedicated branches from current `origin/main`. Per-workstream handoffs at `tools/workstream-handoffs/` (this branch) provide self-contained orientation for each workstream. The Ch 3 mini-handoff at `alignment/sessions/ch3-drafting-handoff_2026-05-09.md` is the equivalent for the Ch 3 drafting session.

---

## §1. Where things stand

**Manuscript:** **10 of 10 Book One chapters drafted.** Ch 3 ("The Waterman") drafted 2026-05-09 (commit `3a8b096` on `claude/schedule-darity-interview-6RUlG`; PR #2 open against main as of this handoff). All other chapters drafted earlier; substantive Pistor + Christophers + Susskind paragraph engagement landed in Ch 5 + Ch 9 + bibliography on 2026-05-08 (commit `d78872e` already on main). Substance-drives-length discipline ratified; no chapter-padding to hit minimum word counts.

**Essay tracks active in parallel:**
- **Aeon** — pitch complete + READY TO SEND. Version C ratified as the locked submission cut (300w; commits `384b2df` + `24d2e79`); Version A held as alternative; Version B deleted. Title ratified as "The Mask of Abundance" (rigor pass v1.0.0). AI disclosure included; cultural-engagement Dunbar/Du Bois/Ellison/Fanon lineage commitment locked in. **Submission window: June 1–7, 2026** (Aeon portal first-week-of-month).
- **Noema** — original submission withdrawn 2026-05-01; rewrite plan ratified (Path B). **Hybrid operational approach ratified 2026-05-09** (commit `9aee18d`): 100% drafted-able now. Section V Darity sub-portion now drafts from public-record quote-mining (substitution-hypothesis applied symmetrically to Darity + Colden); May 12 interview = upgrade opportunity, not precondition. Submission target accelerates from August to **late May / early June** if drafting capacity allows.
- **Boston Review** — pitch + essay both not yet drafted. Source chapter Ch 5 is current; Pistor + Christophers engagement landed (`d78872e`). Cascade-plan timing: pitch mid-June; essay mid-July submission via Submittable.
- **Berggruen** — independent track; deadline 2026-08-17; AI-free content required; isolated workflow not yet stood up. Soft target Aug 5 (12-day buffer).

**Outreach pipeline (state as of 2026-05-09 evening):**
- **William ("Sandy") Darity Jr.** (Duke) — INTERVIEW CONFIRMED 2026-05-12 @ 14:00 ET (phone, 1 hr). Full prep stack at `research/outreach/subjects/darity/` (prereadbrief, background-brief, interview-prep, live-call companion HTML+MD).
- **Mariana Mazzucato** (UCL/IIPP) — HOLDING via Adam Albrecht 2026-05-06; awaiting substantive follow-up. Full prep stack at `research/outreach/subjects/mazzucato/`.
- **Allison Colden** (CBF Maryland via Val DiMarzio) — response SENT 2026-05-06; **public-record brief landed 2026-05-08** (commits `0e83dc5` + `fffd202`); substitution-hypothesis CONFIRMED — Ch 3 + Noema §V both drafted from public-record alone. Full prep stack at `research/outreach/subjects/colden/`.
- **Karen Moore** (CBF Virginia via David Sherfinski) — response SENT 2026-05-06; **public-record brief landed 2026-05-08** (commit `c352d9a`); substitution-analysis verdict noted. Full prep stack at `research/outreach/subjects/moore/`.
- **Dagan Cohen** (Amsterdam DEAL implementation team) — response SENT 2026-05-08 via Beth Ingledew warm intro; awaiting Dagan's reply. Full prep stack at `research/outreach/subjects/dagan/`.
- **A. Kirsten Mullen** (#3) — Gmail draft on hold; activation deferred to end of Darity interview if call goes well.
- **8 cold-outreaches awaiting reply** (Boyce/Buller/Mian/Sufi/Alperovitz/Mondragon press/ACLC/NCBLR) within standard 2–3 wk academic window (sent ~2026-05-05; soft trigger for second-attempt nudges 2026-05-19).

**Outreach folder structure:** restructured 2026-05-09 (commit `16225b5` + downstream) into per-subject folders + meta-folder buckets:
- `research/outreach/subjects/<subject>/` — per-subject prep stacks
- `research/outreach/_pipeline/` — outreach-drafts pipeline files
- `research/outreach/_protocols/` — Q0 attribution + framework-scope-explicitness disciplines
- `research/outreach/_templates/` — reusable templates

**Publishing-strategy artifacts** stood up 2026-05-06 → 2026-05-09 across:
- `publishing/strategy/cascade-plan_2026-05-06.md` — 12-month cascade strategy + decisions due + risks + verification + critical files (latest version on `claude/plan-publishing-strategy-9Yubv` branch)
- `publishing/strategy/decisions-log.md` — append-only strategic-decisions history (latest on feature branch)
- `publishing/strategy/rights-register.md` — per-essay rights / exclusivity / overlap tracking (latest on feature branch)
- `publishing/strategy/cross-thread-todos.md` — single living source-of-truth for cross-thread coordination items (on feature branch; not yet on main)
- `publishing/book-proposal/*.md` — seven section files (skeletons + comp-titles substantive + bio polished)
- `publishing/agents/*.md` — 25-target list (1/25 populated: Sarah Chalfant / Wylie Agency Priority A); query-letter template; query-tracker; personalization-snippets (1/25)
- `publishing/essay-drafts/templates/ai-disclosure-paragraph.md` — Aeon master + Noema variant + generic
- `tools/routines/proposed_routines_v1.0.0.md` — **v2.0.0** ratified 2026-05-09: Routine 1' (cross-thread state-snapshot, every other day) + Routine 2 refined + Routine 3' (branch hygiene, weekly Friday) + Routine 4' (stale-reference scan, weekly Sunday); v1.0.0 Routines 1, 3, 4 deprecated/deferred
- `tools/workstream-handoffs/` — seven mini per-workstream handoffs + README (on feature branch; not yet on main)

---

## §2. Active workstreams (per dedicated session going forward)

Per author direction 2026-05-09: each workstream gets a fresh dedicated session on a per-workstream branch. Self-contained handoffs at `tools/workstream-handoffs/` (currently on `claude/plan-publishing-strategy-9Yubv` feature branch; pending PR to main).

| Workstream | Handoff file | Recommended branch prefix | Status |
|---|---|---|---|
| Aeon submission | `aeon-submission-handoff_2026-05-09.md` | `claude/aeon-submission-` | Pitch ready; awaiting June 1–7 portal window |
| Boston Review essay | `boston-review-essay-handoff_2026-05-09.md` | `claude/boston-review-essay-` | Source ready; pitch + essay not yet drafted |
| Berggruen track | `berggruen-track-handoff_2026-05-09.md` | `claude/berggruen-track-` | Workflow not isolated; AI-free required; coordination only |
| Outreach pipeline | `outreach-pipeline-handoff_2026-05-09.md` | `claude/outreach-pipeline-` | 6 subjects in flight; Darity May 12 |
| Book proposal | `book-proposal-handoff_2026-05-09.md` | `claude/book-proposal-sprint-` | Late-June 2026 sprint target (~3 weeks) |
| Agent prep | `agent-prep-handoff_2026-05-09.md` | `claude/agent-prep-` | 1/25 targets; Wave 1 late July / early August |
| Manuscript completion (excluding Ch 3) | `manuscript-completion-handoff_2026-05-09.md` | `claude/manuscript-completion-` | Bibliography flag updates queued; Tech Appendix v2.0.0 + Glossary v4 rebuilds queued |

**Handled separately (no handoff in `tools/workstream-handoffs/`):**
- **Noema essay drafting** — `manuscript/essay/Noema/noema-essay-drafting-plan_2026-05-08.md` is the operational drafting plan; `rewrite-plan_2026-05-01.md` REVISION 2026-05-08 is the canonical structure; 100% drafted-able under hybrid operational approach (commit `9aee18d`).
- **Ch 3 drafting** — `alignment/sessions/ch3-drafting-handoff_2026-05-09.md` was the mini-handoff (Ch 3 has since been drafted; PR #2 lands the draft on main).

---

## §3. Manuscript drafting state by chapter

| Ch | Title | Status | File | Length |
|---|---|---|---|---|
| 1 | The Quiet Math | **Drafted 2026-05-04**; tentatively final (sunrise bookend with Ch 10; consent-rejection plan applied; framework-felt-not-named discipline applied) | `Chapter__1_TheQuietMath__Draft.md` | ~3,400w |
| 2 | The Miner | Drafted; Phase 1 framework audit applied; 3 INTERVIEW NEEDED placeholders flagged per weekly-audit-2026-04-28 | `Chapter__2_TheMiner__Draft.md` | ~4,957w |
| 3 | The Waterman | **Drafted 2026-05-09** (commit `3a8b096`); from public-record material per substitution-hypothesis | `Chapter__3_TheWaterman__Draft.md` | ~192 lines |
| 4 | The Existence Proof | Drafted; Norway sovereign-wealth-fund case load-bearing | `Chapter__4_THEEXISTENCEPROOF__Draft.md` | ~3,975w |
| 5 | The Accountability Gap | Drafted; "Restitution and Foreclosure" two-instrument decomposition load-bearing; Pistor + Christophers paragraph engagement landed 2026-05-08 (`d78872e`) | `Chapter__5_THEACCOUNTABILITYGAP__Draft.md` | ~9,574w |
| 6 | Three Ways of Counting | Drafted (clean semantic HTML); Insight #21 closed 2026-05-04 | `Chapter__6_ThreeWaysofCounting__Draft.html` | ~75KB |
| 7 | On Other Worlds | Drafted; Aeon pitch source material | `Chapter__7_OnOtherWorlds__Draft.md` | ~8,537w |
| 8 | What Things Actually Cost | Drafted; Dunbar/Du Bois/Ellison/Fanon engagement applied 2026-05-08 (165w) | `Chapter__8_WhatThingsActuallyCost_Draft.md` | ~6,026w |
| 9 | Pricing Honestly | Drafted; Christophers + Susskind paragraph engagement landed 2026-05-08 (`d78872e`); Mondragon material locks Noema solutions cluster | `Chapter__9_PricingHonestly__Draft.md` | ~10,178w |
| 10 | Common Bonds | Drafted; sunrise → sunset close (sunrise bookend with Ch 1) | `Chapter_10_CommonBonds__Draft.md` | ~7,366w |

**Bibliography:** comprehensive (~18,312w; 156 sections); §13 has Mazzucato (load-bearing) + Pistor / Christophers / Susskind (added 2026-05-08; engagement-pending flags pending update to "engaged in Ch X §Y" per cross-thread item #3).

**Tech Appendix Phase 3 v2.0.0 rebuild** + **Glossary v4 rebuild** queued post-proposal-sprint.

---

## §4. Pending PRs (as of this handoff)

| PR | Branch → base | What lands | Status |
|---|---|---|---|
| **#2** | `claude/schedule-darity-interview-6RUlG` → `main` | Ch 3 draft + ch3-drafting-handoff + AGENTS.md update | **OPEN** as of 2026-05-09; per author direction 2026-05-09 |
| **(this handoff's PR — to be opened)** | `claude/plan-publishing-strategy-9Yubv` → `main` | Workstream-handoffs/ + cross-thread-todos.md + routines v2.0.0 + bio polish + cascade-plan/decisions-log/rights-register cleanup + this session-handoff doc + much more | Pending; recommended to merge before fresh per-workstream sessions begin so they have access to workstream-handoffs/ from main |

---

## §5. Active branches (as of 2026-05-09 evening)

| Branch | Status | Notes |
|---|---|---|
| `main` | Canonical state | At commit `7eab17e` (pre-Ch-3-merge); PR #2 pending |
| `claude/plan-publishing-strategy-9Yubv` | Active; this session's branch | At commit `b9bad8b` post-merge of Ch 3 + handoff; substantial publishing-strategy work + workstream-handoffs accumulated |
| `claude/schedule-darity-interview-6RUlG` | Active; Ch 3 source | At commit `37b14cf`; PR #2 head |
| `claude/respond-to-valerie-inquiry-mV3Na` | Recent activity | (verify status; outreach restructure source) |
| `claude/great-thompson-2T7uk` | Older feature branch | (verify status) |
| `claude/serene-franklin-1d85a7` | Older feature branch | (verify status) |
| `claude/youthful-brahmagupta-79b445` | Older feature branch | (verify status) |
| `claude/epic-lamport-d7a6a7` | Older feature branch | (verify status) |
| `claude/outreach-followups` | Recent | (verify status) |

**Recommendation:** Routine 3' (branch hygiene scan, weekly Friday 5pm ET; ratified v2.0.0) will categorize each branch as ACTIVE / HIBERNATING / MERGE-AND-RETIRE / ABANDONED once scheduled. Pre-empt the rescue-from-frozen-sessions pattern.

---

## §6. Open insights (as of 2026-05-09 — verify against `alignment/commons_bonds_open_insights_v1.0.0.md`)

| # | Title | Status | Action |
|---|---|---|---|
| 21 | Tech Appendix + Ch 6 HTML structural placement | **CLOSED-RATIFIED 2026-05-04** | Folded into Phase 3 Tech Appendix rebuild |
| 36 | Ch 1 + Ch 3 conversational drafting | Ch 1 + Ch 3 NOW DRAFTED 2026-05-04 + 2026-05-09 | Effectively closed; verify |
| 39 | Pre-publication external review | Pending (post-completion) | Triggers entire-book citations audit + Insight #63 focused rigor pass |
| 63 | "Tier" word-level conceptual collision | Quick-fix applied; focused rigor pass queued | Fold into Insight #39 pre-publication review |
| 64 | "Unpriced subsidies" as candidate framework lens | Capture-only | Watch for re-surfacing |
| 65 | Six-mechanism cost-severance enumeration | Cascade execution partially applied (Ch 1, 5, 7); further sweeping pending | (verify status) |
| 66 | Universal computational claim (bad-actor / no-bad-actor symmetry) | Ch 1 plant + Ch 7 three-case parallel ratified placement | Ch 1 plant placed; Ch 7 three-case integration pending |

(Reconfirm against `alignment/commons_bonds_open_insights_v1.0.0.md` at next-session start.)

---

## §7. Pending decisions

| Decision | Trigger / status | Notes |
|---|---|---|
| **Atlantic Ideas vs. Phenomenal World** for slot-3 primary venue | Open per cascade plan + cross-thread-todos #4 | Recommend Phenomenal World (more accessible without prior clips); Atlantic Ideas as fallback. Source chapter for slot-3: Ch 9 *Pricing Honestly*. |
| **Acknowledgments-page check on Sarah Chalfant ↔ Mazzucato** | Open per cross-thread-todos #1 | Verify before Wylie query goes out (Wave 1, late July / early August 2026). Check *Mission Economy* (2021) or *The Value of Everything* (2018) acknowledgments pages. |
| **Mullen warm-intro activation** | Trigger: end of Darity interview 2026-05-12 if call goes well | Per cross-thread-todos #2 |
| **Bibliography engagement-pending flag updates** | Open per cross-thread-todos #3 | Pistor / Christophers / Susskind §13 entries: "engagement pending" → "engaged in Ch X §Y" with section refs. Useful before late-June proposal sprint. |
| **Berggruen workflow isolation protocol** | Open | Stand up isolated working directory or strict no-AI-tools discipline before drafting begins |
| **Sample chapters for proposal** | Recommend Ch 7 + Ch 5 (per cascade plan) | Confirm before late-June sprint |
| **Aeon post-Darity revision** | Optional polish; Version C is locked | Decision contingent on Darity interview material yielding upgrade-worthy substance |

---

## §8. Operating rules unchanged

- **Two-layer content origination per WP#10:** classify at origination; default to internal-scaffolding when uncertain.
- **Worktree-isolation per WP#9:** harness-issued feature branches; ratified-chunk fast-forward to `main` (or via PR per push restrictions) when the rescue-pattern doesn't apply.
- **Substance drives length:** no chapter-padding to hit minimum word counts; cuts and additions are content-driven; venue word limits are constraints to fit, not floors.
- **Path B no-overlap rule:** chapter prose feeds essay paraphrases (Aeon / Noema / BR), not direct sentence reuse.
- **Substitution-hypothesis discipline:** public-record briefs are sufficient for Ch 3 + Noema §V third-anchor + (per analogy) Darity Section V; live interviews are upgrades, not preconditions.
- **Don't reintroduce wife details** (consent-rejection rewrite plan standing 2026-05-01).
- **Don't use retired vocabulary** (Value Capture · AIT · Dynastic Labor Cost · Reparations Bond · Resource-Foreclosure Bond · Knowledge and Culture · Triangulated RCV Estimation · "dimension" as framework-register).
- **Pattern 2 register** throughout drafting (demonstrate the affordance; don't codify).
- **Q0 attribution-permission protocol** on every interview (`research/outreach/_protocols/interview-attribution-protocol_2026-05-06.md`).
- **GuidanceDocs stay in place** under WP#10 + staleness disclaimers; per-section staleness audit deferred to Insight #39 pre-publication external review.
- **Pitch-vs-essay terminology discipline** (introduced 2026-05-09):
  - Aeon = pitch (300w via portal); essay post-acceptance via editor
  - Noema = full essay draft on submission (~3,700w)
  - Boston Review = ~1pp pitch via Submittable, full essay if accepted
  - Atlantic Ideas = pitch in body of email, essay on assignment
- **Routine v2.0.0 ratified 2026-05-09:** Routine 1' (cross-thread state-snapshot, every other day) + Routine 2 refined + Routine 3' (branch hygiene, weekly Friday) + Routine 4' (stale-reference scan, weekly Sunday). v1.0.0 Routine 1 deprecated; Routines 3 + 4 deferred. Scheduling pending.
- **Never touch `manuscript/essay/berggruen/`** via AI tools (AI-free competition); coordination only.

---

## §9. Next-session protocol (going-forward operating mode 2026-05-09)

Per author direction 2026-05-09, fresh sessions:

1. **Branch from current `origin/main`** with a per-workstream branch name. Per-workstream prefixes documented in `tools/workstream-handoffs/README.md`.
2. **Read only the relevant workstream handoff** at `tools/workstream-handoffs/<workstream>-handoff_2026-05-09.md` + this session-handoff (v1.53.0 once landed on main).
3. **Cross-coordination via:**
   - `publishing/strategy/cross-thread-todos.md` — items requiring other threads' action
   - `publishing/strategy/cascade-plan_2026-05-06.md` — cascade state + decisions due
   - `publishing/strategy/decisions-log.md` — strategic-decisions history
   - Routine 1' state-snapshot (every other day) once scheduled
4. **Operate within workstream scope.** Out-of-scope items either go to `cross-thread-todos.md` or are deferred.
5. **End-of-session discipline:** push the branch; surface any cross-thread items in the todos doc; update Date modified on any artifacts touched.

---

## §10. Cross-references

**Authoritative orientation files (read these first if picking up cold):**

- [`AGENTS.md`](../../AGENTS.md) — current canonical state table; repository structure; working discipline; queued workstreams; operating rules
- [`README.md`](../../README.md) — publisher-facing landing page
- [`alignment/commons_bonds_open_insights_v1.0.0.md`](../commons_bonds_open_insights_v1.0.0.md) — open insights tracker
- [`alignment/commons_bonds_working_principles_v1.0.0.md`](../commons_bonds_working_principles_v1.0.0.md) — 10 working principles (WP#9, #10 most operationally relevant)
- [`alignment/commons_bonds_framework_positioning_disciplines_v1.0.0.md`](../commons_bonds_framework_positioning_disciplines_v1.0.0.md) — FPD v1.0.0 (eight canonical positioning disciplines)

**Workstream entry points (post-PR consolidation):**

- All seven workstreams: `tools/workstream-handoffs/<workstream>-handoff_2026-05-09.md` (currently on `claude/plan-publishing-strategy-9Yubv`; pending PR to main)
- Noema essay drafting: `manuscript/essay/Noema/noema-essay-drafting-plan_2026-05-08.md` + `rewrite-plan_2026-05-01.md`
- Ch 3 drafting: `alignment/sessions/ch3-drafting-handoff_2026-05-09.md` (PR #2 pending; Ch 3 already drafted)

**Publishing-strategy artifacts:**

- `publishing/strategy/cascade-plan_2026-05-06.md`
- `publishing/strategy/decisions-log.md`
- `publishing/strategy/rights-register.md`
- `publishing/strategy/cross-thread-todos.md` (NEW 2026-05-09; pending PR consolidation)
- `publishing/book-proposal/*.md` (seven section files + sample-chapters placeholder + master assembly spec)
- `publishing/agents/*.md` (targets, query-letter-template, query-tracker, personalization-snippets)
- `publishing/essay-drafts/templates/ai-disclosure-paragraph.md`

**Tools:**

- `tools/routines/proposed_routines_v1.0.0.md` (v2.0.0 ratified 2026-05-09; pending PR consolidation)
- `tools/workstream-handoffs/` (NEW 2026-05-09; pending PR consolidation)
- `tools/rigor-passes/` (historical audit trail)

**Prior handoffs for context (most recent first):**

- [`v1.52.0`](commons-bonds-session-handoff-2026-05-06_v1.52.0.md) — multi-thread state-snapshot 2026-05-06
- [`v1.51.0`](commons-bonds-session-handoff-2026-05-03_v1.51.0.md) — Ch 1 + Ch 3 drafting handoff (Ch 1 since drafted; Ch 3 now also drafted)
- [`v1.50.0`](commons-bonds-session-handoff-2026-05-02_v1.50.0.md) — outreach record updates
- [`v1.49.0`](commons-bonds-session-handoff-2026-04-30_v1.49.0.md) — parallel-execution plan
- [`v1.48.0`](commons-bonds-session-handoff-2026-04-30_v1.48.0.md) — state-snapshot foundation

---

## §11. What changed between v1.52.0 and v1.53.0

**Manuscript:**
- Ch 1 drafted 2026-05-04 (was undrafted); now tentatively final
- **Ch 3 drafted 2026-05-09** (was undrafted; substitution-hypothesis applied; PR #2 lands)
- Pistor + Christophers + Susskind paragraph engagement applied to Ch 5 + Ch 9 + bibliography (commit `d78872e`)
- Dunbar/Du Bois/Ellison/Fanon engagement applied to Ch 8 (165w; tied to Aeon "Mask of Abundance" title)
- 10 of 10 chapters drafted

**Aeon:**
- Title ratified ("The Mask of Abundance"; rigor pass v1.0.0)
- Version C ratified as locked submission cut (commits `384b2df` + `24d2e79`)
- Cultural-engagement Dunbar aside drafts preserved
- Submission strategy doc landed
- Submission window: June 1–7, 2026

**Noema:**
- Hybrid operational approach ratified 2026-05-09 (commit `9aee18d`); 100% drafted-able now
- Section V Darity sub-portion drafts from public-record quote-mining
- Submission target accelerates from August → late May / early June

**Outreach:**
- Folder restructured into per-subject + meta-folder buckets (commit `16225b5`)
- Mazzucato + CBF prep stacks built out (parallel session work)
- Live-call companions for Colden + Moore + CBF + Mazzucato
- Substitution-hypothesis CONFIRMED for both Colden + Moore briefs

**Publishing strategy:**
- Cascade plan recalibration: green-light rule (proposal + ≥1 essay at editor-review + ≥1 interview), Wave 1 timing shifted to late July / early August
- Bibliography Pistor + Christophers + Susskind additions (§13)
- 02_comp-titles restructured around bibliography ⊆ comps relationship (Tier 1/2/3)
- Author-platform bios polished across three lengths (~50w / ~85w / ~135w)
- AI-disclosure paragraph standardized template (Aeon master + Noema variant + generic)
- First concrete agent target: Sarah Chalfant / Wylie Agency (Priority A)
- Cross-thread-todos.md stood up

**Routines:**
- v2.0.0 ratified: Routine 1 deprecated (regression sentinel); Routine 1' new (cross-thread state-snapshot every other day); Routine 3' new (branch hygiene weekly); Routine 4' new (stale-reference scan weekly); Routine 2 refined; Routines 3 + 4 deferred

**Operating mode:**
- Per-workstream handoffs at `tools/workstream-handoffs/` enable per-workstream dedicated sessions on per-workstream branches
- Cross-thread coordination via `cross-thread-todos.md` + Routine 1'
- Pitch-vs-essay terminology discipline introduced

---

## §12. Known follow-ups

1. **PR #2** (Ch 3 → main) needs review + merge.
2. **Second PR** for `claude/plan-publishing-strategy-9Yubv` → main needs to be opened to land workstream-handoffs/ + cross-thread-todos.md + routines v2.0.0 + bio polish + cascade-plan/decisions-log/rights-register cleanup before fresh per-workstream sessions begin (otherwise those sessions can't read workstream-handoffs from main).
3. **Routine 1'** (cross-thread state-snapshot) scheduling once tooling configured.
4. **Stale-reference cleanup** of older session handoffs that still reference Insight #21 as open or Aeon Version A/B (not blocking; routine 4' will surface candidates weekly once scheduled).

---

*v1.53.0 drafted 2026-05-09 evening on `claude/plan-publishing-strategy-9Yubv` (this branch is pending PR to main). Supersedes v1.52.0 (2026-05-06) as the canonical state-snapshot.*
