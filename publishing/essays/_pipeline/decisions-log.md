# Publishing Decisions Log

**Date drafted:** 2026-05-06  ·  **Date modified:** 2026-05-09

**Purpose.** Append-only record of publishing-strategy decisions — what was decided, when, and why. Mirrors the discipline in `alignment/decisions/`. Use for: venue choices, sequencing, rights questions, agent-query gating, deadline shifts.

**Discipline.** Newest at top. Each entry has date, decision, context, and (when relevant) what it supersedes.

---

## 2026-05-09 — Stale-reference cleanup pass: Aeon Version C ratification + outreach folder restructure + Noema 100% drafted-able

**Decision.** Multi-artifact stale-reference cleanup pass after second `origin/main` merge (`db11f96`). Captures four substantive state changes that landed on main while the publishing-strategy thread had been working on its own artifacts; aligns publishing/essays/_pipeline/* with current canonical state.

**State changes captured:**

1. **Aeon pitch Version C ratified 2026-05-08** (commits `384b2df` + `24d2e79`) — Version C is the locked submission cut (300w, READY TO SEND); Version A held as alternative; Version B deleted. Aeon's pitch-first model: submit pitch via portal; essay developed via editor collaboration if accepted. Post-Darity revision May 13–31 is *optional* polish, not a precondition.

2. **Outreach folder restructured** (commit `16225b5` — `claude/respond-to-valerie-inquiry-mV3Na`) — `research/outreach/X` flat paths replaced with per-subject folders + meta-folder buckets:
   - `research/outreach/subjects/<subject>/X` for darity / colden / moore / dagan / mazzucato / cbf
   - `research/outreach/_pipeline/X` for outreach-drafts files
   - `research/outreach/_protocols/X` for attribution + scope-explicitness protocols
   - `research/outreach/_templates/X` for reusable templates
   - All path references in the cascade plan + decisions log earlier entries updated inline; new prep stacks (Mazzucato + CBF) now visible.

3. **Noema 100% drafted-able** — hybrid operational approach ratified 2026-05-09 (commit `9aee18d`). Section V Darity reparations sub-portion (~100–200w) is now draftable now via public-record quote-mining: *From Here to Equality* (Darity & Mullen 2020), *Umbrellas Don't Make It Rain* (Hamilton, Darity, et al. 2015), *Explorations in Economic History* Jan 2026 paper, *Freedmen Fridays* commentary. **May 12 Darity interview = upgrade opportunity, not precondition.** Symmetry with Colden treatment locked: substitution-hypothesis applies consistently across both interview targets. Noema drafting plan moves from ~95% drafted-able → **100% drafted-able**.

4. **Ch 3 unblocked** — risk + abort/pivot wording softened. Drafting bottleneck no longer source-material availability (Colden + Moore briefs cover Chesapeake fisheries restoration); now drafting-capacity allocation only.

**Files updated:**

- `publishing/essays/_pipeline/archive/cascade-plan_2026-05-06.md` — Current state Aeon line; outreach pipeline Colden + Moore bullets; interview-attribution protocol path; May A-track; August A-track Noema; Risks (Ch 3 stalls struck); Decisions due #1 (resolved); Abort/pivot Ch 3; Critical files Aeon block (Version C + Version A + submission strategy + Dunbar drafts) + outreach block (subjects/<subject>/ + _pipeline/ + _protocols/ + _templates/); Update log new 2026-05-09 entry.
- `publishing/essays/_pipeline/rights-register.md` — Aeon row updated (Version C ratified; Version A alt; Version B deleted; pitch-vs-essay distinction); Update log new 2026-05-09 entry.
- `publishing/essays/_pipeline/decisions-log.md` — this entry; ~5 inline outreach-path updates in earlier 2026-05-08 entries (Colden unblock, De-risk Colden + Moore); Date modified bumped 2026-05-08 → 2026-05-09.

**Pitch-vs-essay terminology discipline.** Going forward, distinguish:
- **Aeon submission** = pitch (300 words via `aeon.co/pitch` portal); essay developed post-acceptance via editor collaboration.
- **Noema submission** = full essay draft (best chance per Noema's stated process); ~3,700 words.
- **Boston Review submission** = ~1pp pitch via Submittable, then full essay if accepted; published essays 2,500–5,000w.
- **Atlantic Ideas submission** = pitch in body of email; essay on assignment.

**Cross-references.**
- Source commits: `384b2df` (Version C committed), `24d2e79` (Version C READY TO SEND), `16225b5` (outreach restructure), `9aee18d` (Noema hybrid), `db11f96` (this branch's main-merge).
- Affected-file paths consolidated in cascade plan Critical files block.

**Supersedes.** Stale references in cascade plan + rights register + decisions-log earlier entries pointing at: Aeon Version A as primary; Aeon Version B alternate-frame on hand; flat `research/outreach/X` paths; "~95% drafted-able" Noema status; Ch 3 stalls / gated risks.

---

## 2026-05-08 (Colden unblock) — Public-record brief lands; substitution-hypothesis CONFIRMED; Noema submission accelerates

**Decision.** The parallel session's Colden public-record brief landed 2026-05-08 (commits `0e83dc5` + `fffd202`; now at `research/outreach/subjects/colden/background-brief_2026-05-08.md` post-2026-05-09 outreach folder restructure — ~11,900 words, 719 lines, ~117KB; ~150-source citation list). **Substitution-hypothesis CONFIRMED:** Ch 3 (Watermen / Chesapeake fishery) is draftable from public-record material alone, and Noema essay §V third-anchor (Chesapeake fisheries) is unblocked from the same brief. The live Colden interview becomes a bonus rather than a blocker.

**Implications:**

1. **Noema essay drafting unblocks materially.** Section VI third-anchor (~200w of the essay) was the second-largest blocked portion. Moves to Unblocked. Combined with Sections I–IV + Norway portion of V + Mazzucato/Mondragon portions of VI + Close, the drafted-able portion expands from ~89% (~3,300+ words) to ~95% (~3,500+ words). Only Section V's Darity reparations sub-portion (~100–200w) remains blocked, pending the May 12 interview + quote-confirmation.

2. **Submission timeline accelerates.** Cascade plan A-track originally scheduled the Noema rewrite for August (gated on Colden interview + Ch 1 stable). Both gates are now satisfied earlier than expected — Ch 1 tentatively final 2026-05-04; Colden material now in hand. Realistic submission window shifts from August to **late May / early June**, possibly in parallel with or shortly after the Aeon submission (first week of June).

3. **Ch 3 drafting unblocks for the manuscript thread.** Independent of Noema-essay implications: Ch 3 was the only undrafted Book 1 chapter; gated on CBF interview material. Now draftable from public-record material. Manuscript-thread coordination item — `Chapter__3___GuidanceDoc.md` is the natural place for the manuscript thread to record this unblock.

4. **Moore (CBF VA) public-record prep no longer a Noema dependency.** May still proceed in the parallel session for Ch 3 dual-perspective coverage (Maryland + Virginia CBF positions), but Noema §V third-anchor is satisfied with Colden material alone.

**Cross-thread context.** The 2026-05-08 (De-risk Colden + Moore) decision committed earlier today (`bfcf882`) queued the public-record prep work; the parallel session executed within the same day, lands the brief, and confirms the substitution hypothesis. The de-risk → unblock cycle ran in <12 hours — fastest cross-thread coordination loop the publishing-strategy thread has executed to date.

**Updated artifacts in this commit:**
- `publishing/essays/noema-commons-bonds/_archive/planning/noema-essay-drafting-plan_2026-05-08.md` — Section VI moved to Unblocked; Phase 3 expanded; Phase 4 shrunk; submission timeline notes updated.
- `publishing/essays/noema-commons-bonds/_archive/planning/rewrite-plan_2026-05-01.md` REVISION 2026-05-08 — Section VI gating row updated; "What stays unchanged" third-anchor bullet rewritten as resolved.
- `publishing/essays/_pipeline/archive/cascade-plan_2026-05-06.md` — three Colden references updated (Outreach pipeline / August A-track / Decisions due #6); update log gains 2026-05-08 (Colden unblock) entry.

**Cross-references.**
- Source brief: `research/outreach/subjects/colden/background-brief_2026-05-08.md` (commits `0e83dc5` + `fffd202`; path post-2026-05-09 restructure)
- Prior decision: 2026-05-08 (De-risk Colden + Moore) entry below — established the substitution hypothesis the brief tested.
- Methodology pattern: `research/outreach/subjects/darity/background-brief_2026-05-06.md` + `subjects/dagan/prereadbrief_2026-05-08.md`.

**Supersedes.** Prior gating language across the cascade plan + rewrite plan REVISION + drafting plan that left Section VI third-anchor + Ch 3 as blocked. Previously these were "blocked on Colden interview *or* sufficient public-record material"; now resolved by the latter.

---

## 2026-05-08 — De-risk Colden + Moore CBF dependency via parallel public-record prep (queued for manuscript/outreach thread)

**Decision.** The Ch 3 (Watermen / Chesapeake fishery) and Noema essay §V third-anchor decision are currently single-failure-point dependencies on Colden + Moore CBF interview outcomes. To de-risk, queue parallel public-record prep work on both subjects — mirror the methodology already applied to Darity (`research/outreach/subjects/darity/background-brief_2026-05-06.md`) and Dagan (`research/outreach/subjects/dagan/prereadbrief_2026-05-08.md`): build background briefs of public quotes, congressional/state-legislature testimony, op-eds, podcast appearances, and CBF press releases. Output is useful whether or not interviews land — pre-interview prep + fallback if interviews decline.

**Cross-thread coordination.** Actual research-dossier work belongs to the manuscript / outreach thread (lives in `research/outreach/`). The publishing-strategy thread captures the strategic rationale here and updates the gating language in the Noema rewrite plan REVISION + the cascade plan to reflect the relaxed dependency.

**Implications:**
- **§V third-anchor gating**: "Colden interview" → "Colden interview OR sufficient public-record material on Chesapeake fisheries restoration as renewable-past-regeneration case."
- **Ch 3 drafting** unblocks earlier if public-record yield is sufficient — manuscript thread retains discretion on whether interview material is essential or substitutable for the chapter's narrative arc.
- **Aeon submission (first week of June)** and **proposal sprint (late June)** are not affected — both already proceeded independently of Colden/Moore tracks.

**Three scenarios this prep covers:**
- *Both decline* → public-record material is the only material; Ch 3 + §V can still be written from it.
- *One lands* → the other's prep covers gaps in the interview material.
- *Both land* → prep is "redundant" but the live calls were sharper (less time spent rediscovering public material).

The downside of skipping is losing Ch 3 and the Noema §V slot if both interviews decline — material risk to "arguably the whole book" per author 2026-05-08.

**Time-box.** ~1 day per subject (mirror Darity background-brief scope). Total ~2 days. Recommended during the Aeon-wait window when other essay work is gated. Subjects: **Allison Colden** (CBF Maryland Executive Director); **Karen Moore** (CBF Virginia Executive Director). David Sherfinski (Moore's Reuters-journalist gatekeeper) provides cross-coverage as a secondary public-record source.

**Cross-references.**
- Methodology pattern: `research/outreach/subjects/darity/background-brief_2026-05-06.md` + `subjects/darity/interview-prep_2026-05-06.md` + `subjects/darity/live-call-companion_2026-05-06.md` (HTML+MD).
- Amsterdam DEAL parallel: `research/outreach/subjects/dagan/prereadbrief_2026-05-08.md` (template at `_templates/amsterdam-donut-prereadbrief_2026-05-06.md`).
- Rewrite plan §V gating relaxed in `publishing/essays/noema-commons-bonds/_archive/planning/rewrite-plan_2026-05-01.md` REVISION 2026-05-08 section (this commit).
- Cascade plan §V references updated at three locations (Outreach pipeline + August A-track + Decisions due #6) in `publishing/essays/_pipeline/archive/cascade-plan_2026-05-06.md` (this commit).

**Supersedes.** Prior gating language across the rewrite plan and cascade plan that treated Colden interview as a hard dependency for §V third-anchor and Ch 3 drafting.

---

## 2026-05-08 — Noema rewrite-plan revised in place; Ch 1 absorbed Phase C structural work

**Decision.** Edit `publishing/essays/noema-commons-bonds/_archive/planning/rewrite-plan_2026-05-01.md` in place to add a "REVISION 2026-05-08" section above the original Phase C structure, capturing the divergence between what the 2026-05-01 plan anticipated and what Ch 1 actually became when drafted 2026-05-04 (title-rigor pass v2.0.0; tentatively final at ~3,400 words). The revision section supersedes Phase C; the original plan is preserved below in the same file as historical record.

**Cross-thread context.** Discovered while answering author's question 2026-05-08 ("isn't the way the actual Chapter 1 turned out a bit different than this?"). Pressure-tested the rewrite plan against the actual Ch 1 draft. Confirmed Ch 1 absorbed: (1) three-generations lineage thread (Pooh / father / Chris); (2) Cable-TV-station rescue + DMV commute scenes; (3) Human Scale close (was Section VI in original); (4) Common Bonds + Sisyphus close (was Section VII); (5) marriage-ending material at a consent-OK level (was "drop" in original). What remains essay-specific: framework naming brief; cross-history beat; solutions cluster γ; brief close paraphrasing Ch 1's actual close.

**Revised section structure (now operative):**

- I (~600 words): vignette opener — paraphrase Ch 1 ¶¶1–4 (already written)
- II (~700 words): lineage + work-formation — paraphrase Ch 1 middle (already written)
- III (~600 words): cost made visible — paraphrase Ch 1 second half (already written)
- IV (~400 words): framework named in plain language — NEW prose
- V (~500 words): cross-history beat (Norway + possibly Darity reparations material) — NEW prose, gated on Darity May 12 quote-confirmation
- VI (~700 words): solutions cluster γ — NEW prose, third-anchor still gated on Colden interview
- Close (~200 words): vignette callback + framework-for-the-ones-who-come-after — paraphrase Ch 1 close

Total ~3,700 words; inside Noema's 2,500–4,000 band.

**What stays unchanged from 2026-05-01:** Path B no-overlap rule; hook decision (plane scene at sunrise); cluster γ architecture; cluster γ third-anchor gated on Colden; Darity integration into Section V; pitch model structure (hook → tension → plan → solutions → characters → differentiation); cold resubmit to `edit@noemamag.com`.

**Cascade plan implications.** Cascade plan's August A-track Noema rewrite description still aligns; the section structure detail in this revision deepens but doesn't change timing or gating. No cascade-plan edit required (the rewrite plan is the canonical artifact for section-level structure).

**Supersedes.** `publishing/essays/noema-commons-bonds/_archive/planning/rewrite-plan_2026-05-01.md` Phase C section structure (Sections I–VII as originally laid out). Original preserved below the REVISION section in the rewrite plan itself.

**Cross-references.**
- Ch 1 draft: `manuscript/chapters/Chapter__1_TheQuietMath__Draft.md`
- AI-disclosure template (committed earlier today, `9effbef`): `publishing/essays/_shared/templates/ai-disclosure-paragraph.md` (Noema variant)
- v1.52.0 handoff §2.4 (Noema rewrite track)
- Colden interview thread (Ch 3 + Noema §V third-anchor gating)
- Darity interview 2026-05-12 (Section V cross-history beat material)

---

## 2026-05-08 — Bibliography additions (Pistor + Christophers + Susskind); manuscript engagement queued for Ch 5 / Ch 9

**Decision.** Add three entries to `research/literature/bibliography.md` §13 (Framework-adjacent) on substantive grounds, and queue the corresponding manuscript engagement work for the manuscript thread:

1. **Pistor, Katharina — *The Code of Capital* (2019)** — STRONG SUPPORT (candidate; engagement pending Ch 5 / Ch 9 paragraph integration). Structural-mechanism neighbor: Pistor names the legal-coding architecture that *produces* capital from things; Commons Bonds names the cost-severance architecture that *separates* value-capture from cost-bearing.
2. **Christophers, Brett — *The Price is Wrong* (2024)** — STRONG SUPPORT (candidate; engagement pending Ch 9 paragraph integration). Direct mechanism-level engagement with how pricing fails — the same territory Commons Bonds enters with Residual Commons Value (RCV).
3. **Susskind, Daniel — *Growth: A Reckoning* (2024)** — SUPPORT (candidate; engagement pending Ch 9 paragraph integration). Adjacent register: Susskind takes "the costs of growth" as the explicit subject; Commons Bonds operates at the per-extraction-event mechanism level.

**Cross-thread TODO (manuscript thread).** Each addition flags an engagement-depth decision and a paragraph-or-two integration in the manuscript:

- **Pistor → Ch 5 (Accountability Gap)** primary; Ch 9 secondary. Most likely Ch 5, where the institutional-architecture-of-accountability frame intersects Pistor's legal-architecture-of-capital frame.
- **Christophers → Ch 9 (Pricing Honestly)** primary; Ch 5 secondary. Ch 9 is the pricing-instrument home — natural place to mark the diagnosis-vs-prescription distinction.
- **Susskind → Ch 9 (Pricing Honestly)** primary; Ch 1 secondary. Ch 9's policy-economy framing is the natural place to position Commons Bonds as a mechanism-specific complement to Susskind's macro reckoning.

Until those engagements land, the new bibliography entries carry **"engagement pending"** status flags; the comp-titles section in the proposal is honest about candidate-pending status.

**Context.** Author surfaced the comps↔bibliography gap 2026-05-08: of the 8 comps in `02_comp-titles.md`, only Mazzucato was in the bibliography (load-bearing as Ring-1 flagship "Value Extraction"); the other 7 were market-positioning instinct rather than substantive intellectual neighbors. Two corrective options: (Option 1) tighten the comp list to bibliography-anchored picks now; (Option 2) bibliography-side work first — add the substantively-relevant comps, then refine. Author chose Option 2 with the three additions explicitly named (Pistor + Christophers + Susskind). The remaining four working-list comps (Mission Economy, Sassen, Patel & Moore, Rodrik) stay in `02_comp-titles.md` as Tier 2 / Tier 3 (register-adjacent or market-signal-only).

**`02_comp-titles.md` updated** to reflect the bibliography ⊆ comps relationship. New tier structure:
- **Tier 1** — bibliography-anchored, mechanism-level neighbors (Mazzucato, Pistor, Christophers).
- **Tier 2** — bibliography-anchored, register-adjacent (Mission Economy, Susskind).
- **Tier 3** — market-signal candidates only, not in bibliography (Sassen, Patel & Moore, Rodrik); use sparingly with explicit "audience overlap" framing.
- Selection-rule revised: target final-5 = Mazzucato + Pistor + Christophers + Susskind + at most one Tier 3.

**Supersedes.**
- `publishing/book-proposal/02_comp-titles.md` Tier 1 / Tier 2 structure (revised to Tier 1 / Tier 2 / Tier 3 with bibliography-anchored vs. market-signal-only distinction).
- Selection rule rewritten around bibliography-anchored leads + at most one Tier 3 round-out.

**Cross-references.**
- `research/literature/bibliography.md` §13 — new entries inserted after Mazzucato (line 511), before §14 (line 515 pre-insertion).
- `publishing/book-proposal/02_comp-titles.md` — bibliography ⊆ comps relationship explicit; Cross-thread dependency section added pointing back at the queued manuscript work.
- Author's stated decision: Option 2 (bibliography-first), with Pistor + Christophers + Susskind named as the additions.

---

## 2026-05-08 — GuidanceDocs stay in place under WP#10; staleness audit deferred to Insight #39

**Decision.** GuidanceDocs (`manuscript/chapters/Chapter__N___GuidanceDoc.md`) remain in place at their current paths. They are not archived, not deleted, and not consulted as source material for any publisher-facing artifact. Their per-section staleness audit is deferred to **Insight #39 pre-publication external review**.

**Context.** Author surfaced the question 2026-05-08: most GuidanceDocs are stale because the chapters they scaffolded are mostly finished and just need polish — should they be archived?

The reasoning for not archiving now:

1. **They self-declare as scaffolding.** Each GuidanceDoc carries WP#10 layer-classification frontmatter ("Layer: internal-scaffolding per Working Principle #10") plus a staleness disclaimer added 2026-04-30 ("This file accumulates content across earlier dates… Sections from earlier dates may reference retired vocabulary or superseded direction. Verify against current state before applying. Per-section staleness audit deferred to future pass."). A reader who opens a GuidanceDoc cannot mistake it for current canonical content.

2. **They preserve ~65 cross-references.** Per the Insight #37 separation pass (closed-ratified 2026-04-30), scaffolding extracted from chapter Drafts was consolidated *into* the existing GuidanceDocs at their existing filenames specifically to preserve cross-reference integrity. Premature archive would break the navigability of the drafting-provenance web for ambiguous gain.

3. **The natural archive moment is Insight #39.** Pre-publication external review triggers the entire-book citations audit + Insight #63 focused rigor pass. That is when per-section staleness audit + per-chapter archive/retain decisions are properly batched. Doing it sooner introduces churn that the pre-publication pass would re-do anyway.

**Exception (case-by-case, not a sweep).** If a particular GuidanceDoc generates real friction relative to its now-finalized chapter — confusing a reader who consults both, or carrying volume that obscures the current state — it can be moved to `archive/decomposition/` with a redirect-stub at the original path to preserve cross-reference reachability. This is a per-doc judgment call, not a project-wide cleanup.

**Implications for publishing strategy.** The book proposal's chapter summaries, overview voice samples, and sample chapters all source from drafted chapters in `manuscript/chapters/Chapter__N__*__Draft.md` — never from GuidanceDocs. This is already reflected in `publishing/book-proposal/05_chapter-summaries.md` (corrected in the 2026-05-08 (later) commit `73a0b70`).

**Supersedes.** Nothing — confirms status quo with explicit reasoning. Closes the open question raised in conversation.

---

## 2026-05-08 (later) — Recalibrate green-light rule and Wave 1 timing; correct chapter-summaries source

**Decision.** Three corrections to `cascade-plan_2026-05-06.md` and `publishing/book-proposal/05_chapter-summaries.md`:

1. **Chapter-summaries source corrected.** GuidanceDocs are scaffolding artifacts (WP#10 layer-classification + staleness disclaimers), not content sources for publisher-facing artifacts. The book proposal's chapter summaries pull from the drafted chapters in `manuscript/chapters/Chapter__N__*__Draft.md` — *not* from `Chapter__N___GuidanceDoc.md`. Same logic applies to overview voice samples (use chapter prose) and sample chapters (use chapter drafts directly).

2. **"Two to four published derivative works at respected venues" framing dropped.** That was a generic-first-author rule of thumb, miscalibrated for this project's actual material strength: 9 of 10 chapters drafted, named-source interview pipeline already converting (Darity ACCEPTED), formal framework apparatus (RCV + Cost Severance), Pattern-2 implementation channel open (Amsterdam DEAL via Dagan). Replaced with the realistic floor: complete book proposal + ≥1 essay at editor-review stage at a top-tier venue + ≥1 substantive named-source interview recorded with quote-permission. "Under consideration at \_\_\_\_" is queryable in good faith if real and current.

3. **Wave 1 agent-query target shifted from November 2026 to late July / early August 2026.** The November target was driven by the higher-bar 2-4 placements assumption. Under the lower floor — and given this author's actual drafting pace (~12K words/week sustained during book writing) — the proposal can be assembled in a 3-week focused sprint targeting late June completion, with the comp-titles section already 80% drafted and chapter summaries pulling from already-drafted chapters. ~3-month acceleration. Wave 2 shifts from Jan to Sept-Oct 2026; Wave 3 shifts from Mar 2027 to Q4 2026 / Q1 2027. Strategic frame point 5 reframed: format mix (magazines + op-eds + academic/policy) builds platform breadth across waves rather than gating Wave 1.

**Context.** Author surfaced the 2-4 placements framing as miscalibrated against earlier-conversation guidance from other Claude sessions, which had suggested one placement (or one substantive submission under consideration) could suffice within the response window. Pressure-tested the math: drafting pace, comp-titles section already drafted, chapter drafts as sample-chapter source, Darity interview May 12 effectively banked — confirms the lower floor and faster timeline are realistic for this project specifically. Also clarified the source-of-truth pointer for chapter summaries (chapters, not GuidanceDocs) — the GuidanceDocs stay in place under WP#10 layer-classification with their staleness disclaimers; they are not consulted for publisher-facing content. Their archive moment is at pre-publication external review (Insight #39), not now.

**Supersedes.**
- `cascade-plan_2026-05-06.md` Context-section "two to four published derivative works at respected venues" framing.
- `cascade-plan_2026-05-06.md` Strategic frame point 5 (format mix as Wave 1 prerequisite → ongoing build); point 6 (green-light rule recalibrated).
- `cascade-plan_2026-05-06.md` 12-month sequence June through April 2027 (proposal sprint inserted in June; Wave 1 shifted to July-Aug; Wave 2 to Sept-Oct; Wave 3 to Q4-Q1).
- `cascade-plan_2026-05-06.md` Verification section (3-month checkpoint added; 6-month checkpoint reframed; green-light line updated; abort/pivot Wave-2 calendar context).
- `publishing/book-proposal/05_chapter-summaries.md` source-mapping table + drafting-rules section (GuidanceDocs → chapter drafts).

---

## 2026-05-08 — Cascade plan refresh: integrate v1.52.0 + post-handoff state; resolve two open decisions

**Decision.** Refresh `cascade-plan_2026-05-06.md` and `rights-register.md` to reflect canonical state per session-handoff v1.52.0 (2026-05-06) plus subsequent commits through 2026-05-08. Two `Decisions due in 2–4 weeks` items resolve out: the Aeon title and the `draft2.md` fate.

**Captures the following state changes:**

1. **Aeon pitch title ratified** — "The Mask of Abundance" (rigor pass v1.0.0, 2026-05-08); five candidates evaluated through full rigor pass (`publishing/essays/aeon-mask-of-abundance/rigor/title-candidates_2026-05-08.md`); selected for "X of Y" pattern matching Sandel/Pistor/Mazzucato/Raworth + frame-agnosticism + threading to pitch's own signature phrasing. Cultural-engagement commitment to Dunbar/Du Bois/Ellison/Fanon lineage — explicit acknowledgment in Aeon essay + book Ch 8 + Ch 1; bibliography §21 added; mask-terminology pivot prepared for Darity May 12 call. Version B alternate-frame draft preserved on hand.
2. **Darity interview confirmed** — 2026-05-12 @ 14:00 ET, phone, 1 hr (author calls Sandy). Pre-read brief, background brief, internal interview-prep doc, live-call companion (HTML+MD), framework-decline contingency plan all drafted. Mullen warm-intro deferred to end-of-call.
3. **Outreach pipeline state per v1.52.0 + post-handoff:**
   - Mazzucato HOLDING via Adam Albrecht (UCL/IIPP).
   - Beth Ingledew → Dagan (Amsterdam DEAL implementation team) warm intro materialized 2026-05-08; response sent. Strongest Noema solutions-cluster-γ candidate now that channel is open.
   - Colden (CBF Maryland) via Val DiMarzio: SENT 2026-05-06; 7-question batch stashed.
   - Karen Moore (CBF Virginia) via David Sherfinski: SENT 2026-05-06; parallel CBF track to Colden, both feeding Ch 3.
   - Mullen held until end of Darity call.
   - 8 cold outreaches still awaiting reply within standard 2–3 wk academic window.
   - Interview attribution Q0 protocol now canonical for every interview.
4. **Withdrawn-Noema essay archived** — `draft2.md` moved to `archive/_OneDayMaybe/withdrawn-essays/draft2_withdrawn-noema_2026-05-01.md` 2026-05-08 with §I wife's-illness EXCISED per Candidate #4 discipline. **Resolves** the cascade-plan decision item "Decide whether `draft2.md` becomes Public Books or raw material" — *not* slated for any venue; held as historical record only.
5. **FPD v1.0.0 ratified 2026-05-06** — `alignment/commons_bonds_framework_positioning_disciplines_v1.0.0.md`; eight canonical positioning disciplines including "Why bonds vs. funds/accounts/trusts/reserves" rationale. Feeds book-proposal `00_overview.md` + `02_comp-titles.md` framing.
6. **Personal-story material relocations** — Candidates #2 (Neeraj) + #3 beats (Afghanistan war-zone, company buyout, CEO-setup/Roberts-rules) all moved from `research/story-drafts/` to `archive/_OneDayMaybe/personal-story-material/`. `ch1_aftermath-and-return-to-work_2026-05-01.md` deleted. Story-drafts substrate now 6 files (down from 8); leaner and explicitly curated.
7. **Two new outreach tracks in publishing scope** — Karen Moore (CBF VA) parallel to Colden (CBF MD); Amsterdam DEAL implementation team via Dagan.

**Context.** This branch (`claude/plan-publishing-strategy-9Yubv`) merged `origin/main` twice today (commits `747e47e` + `004c311`), bringing in 73 commits of work from concurrent threads. Refresh keeps cascade plan a living document rather than a 2026-05-06 morning snapshot. v1.52.0 remains the canonical state-snapshot file; the cascade plan is the publishing-strategy-specific projection of it.

**Supersedes.** Selected items in `cascade-plan_2026-05-06.md` Current state, 12-month sequence (May A/B/D + June A + August A), Risks, Decisions due, Verification, and Critical files sections — see commit diff for line-level changes.

---

## 2026-05-06 — Cascade plan ratified; Path B overridden in favor of parallel tracks

**Decision.** Adopt the parallel-tracks publishing strategy in `cascade-plan_2026-05-06.md`. Overrides the May 1 "Path B: book-first" decision: Aeon (Ch 7-derived) is no longer gated on Ch 1 stabilizing; book and essay tracks run concurrently.

**Scope expansion.** Derivative works for this strategy include literary/ideas magazines, op-eds in major newspapers, and academic/policy outlets. Excludes podcasts and owned channels (no Substack/newsletter).

**Load-bearing constraint preserved.** Non-partisan framework positioning remains in force. No specialized applications (abortion, reparations-specific, climate-specific) before the framework's universality is publicly established.

**Supersedes.** `publishing/essays/noema-commons-bonds/_archive/planning/rewrite-plan_2026-05-01.md` Path B sequencing constraint (only the sequencing — the Noema rewrite plan content itself remains in force).

---

## Template for future entries

```
## YYYY-MM-DD — Short title

**Decision.** What was decided.

**Context.** Why. What inputs led here.

**Supersedes.** What earlier decision (if any) this replaces. File path + date.
```
