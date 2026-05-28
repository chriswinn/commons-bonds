---
name: Never invent factual claims in publisher-facing non-fiction prose
description: In publisher-facing non-fiction (book chapters, essays, op-eds, cover letters, queries, AI-disclosure paragraphs), Claude must not invent factual claims — biographical specifics about real people, scene-rendered encounters that didn't happen, period-specific civic-infrastructure details, quoted speech, documentary-record specifics, motivation attributions. The single narrow exception is explicit thought-experiment register where the hypothetical is reader-signaled in the prose itself. Ratified 2026-05-28.
type: feedback
---

# Never invent factual claims in publisher-facing non-fiction prose (ratified 2026-05-28)

**The rule.** In publisher-facing non-fiction prose — book chapters, derivative essays, op-eds, cover letters, query letters, agent correspondence, author bios, AI-disclosure paragraphs, sign-off artifacts that go to publishers / agents / editors — Claude must **not invent factual claims**. This includes:

- **Biographical specifics about named real people** (ages, family details, career timelines, work-method specifics, motivations) beyond what canonical-facts inventories anchor.
- **Scene-rendered encounters** that didn't happen — composite-encounter prose presented in testimonial register ("the waitress at the diner told me..."), invented conversations, recall-anchored vignettes the author never lived through.
- **Period-specific civic-infrastructure detail** ("two banks faced each other across the intersection"; "the surgical wing had X beds"; "civic clubs met on Tuesday evenings") absent verification against local-history source material.
- **Quoted speech** the subject didn't actually say, on or off the record. Verbatim quotes from on-record sources are fine; invented quotes are not, even if "in character."
- **Documentary-record specifics** (internal corporate documents; litigation discovery; archival contents) not anchored against the actual documentary record.
- **Motivation attributions** to named historical actors ("He went to McDowell County because he had been told...") beyond what the historical record supports.

The asymmetric stakes:
- An unshipped essay is recoverable; an unshipped scene can be re-drafted from substrate.
- A shipped-with-fabrication essay is not recoverable. Fact-checker / fact-checker-adjacent reader catches it; credibility collapses; the collapse propagates from the artifact to the book to future work because verification is reputational not local.
- Better to hold or ship-shorter than to invent. The substance-drives-length discipline ([`feedback_substance_drives_length.md`](feedback_substance_drives_length.md)) explicitly supports shorter-but-true over longer-with-invention.

## The thought-experiment exception (narrow + explicitly reader-signaled)

The single legitimate exception: **explicit thought-experiment register** where the hypothetical is signaled to the reader **in the prose itself**, not in the writer's intent alone. Empirical anchor: Ch 7 *On Other Worlds*, which works because:

1. The thought-experiment frame is announced ("Imagine a world where..."; "Consider a counterfactual..."; "Suppose, for the sake of argument...").
2. The invented detail is doing **illustrative not testimonial** work — the prose is saying *"if X were the case, here's what would follow,"* not *"X is the case."*
3. The reader is in the right interpretive register from the first sentence of the experiment; nothing inside the hypothetical is presented as documented event.
4. The experiment is structurally bounded — the reader knows where the hypothetical ends and the analytical-register returns.

This exception **does not** extend to:
- Composite-encounter scenes that read as recall, even if internally labeled "composite" (the reader processes them as recall on first pass).
- "Period-typical" civic-infrastructure detail asserted as observation of a specific place at a specific time.
- "Plausible per the historical record" invented detail about named individuals.
- Quoted speech "in character" with the subject.
- Documentary-record detail "consistent with what was likely in the file."

All of those are testimonial-register, not thought-experiment-register, even if structurally similar to fiction.

## How to apply

### In drafting / restoration / voice-polish generation (Stage 2 + Pass 3.1 + Pass 3.5 + Stage 5 + sub-agent prose production)

1. **Do not generate illustrative invented prose with substrate-critical flags as a hedge.** The "illustrative-but-flagged" pattern is too risky — it produces invented testimonial-register content at HIGH confidence and relies on flag-discipline to catch downstream. If the recommended restoration requires substrate the canonical-facts inventory doesn't anchor, surface the **structure-only recommendation**: where to add prose, what argumentative work it does, what substrate the author would need to draft it. Do **not** produce illustrative invented prose even with `[Substrate-critical note: ...]` callouts.

2. **Substrate-safe attributions ARE permitted.** Published-work citations (e.g., Catte *What You Are Getting Wrong About Appalachia* 2018; Hamby *Soul Full of Coal Dust* 2020; Mazzucato *The Value of Everything* 2018) are verifiable against the actual book; safe to draft + apply at standard literary-essay-register depth. On-record quotes verifiable against transcripts (Lilly's *Inside Appalachia* interview with Bailey) are safe to draft with attribution. These are NOT inventions — they're verifiable assertions about public-record texts.

3. **Generate scene-anchor prose only when canonical-facts inventory anchors it.** If the Stage 1 brief's §7 canonical-facts inventory anchors specific biographical / locational / period detail, restoration prose may use that detail. If §7 is silent on a needed specific, do not invent — surface the gap as a structure-only finding and let the author author the substrate from lived knowledge or source material.

4. **Author bios + cover letters + AI-disclosure paragraphs** are subject to the same rule. Author bio is the author's; cover letter framing must reflect the actual essay; AI-disclosure paragraph must reflect what AI actually did.

### In ratification posture (parent-session ratify-as-recommended)

5. **Substrate-critical flags are advisory, not licensing.** When ratifying "as recommended," verify per-finding that the recommended prose contains no invented testimonial-register specifics. If it does, treat the recommendation as RATIFIED-structure-only-DEFERRED-for-author-substrate, not as APPLY-the-illustrative-prose.

6. **"Ratify all as recommended and proposed" defaults are conditional on substrate-safety.** The single-batch ratification pattern ([`feedback_parallel_session_ratification_cadence.md`](feedback_parallel_session_ratification_cadence.md)) is efficient for chiseling work (Pass 3.2 cuts; verdict ratifications; structural decisions) where the recommended action is substrate-safe. For prose-additive work (Pass 3.5 restoration; Stage 5 cover letter drafting), the discipline-aware ratification verifies per-finding substrate-safety before applying.

7. **Pass 3.1 fact-check should catch any residual invention.** If invented prose somehow lands in essay.md, the next Pass 3.1 fact-check (against §7 canonical-facts inventory) should surface it. The Pass 3.1 F-3.1-H1 precedent (Ch 2 → Harper's: invented Bailey biographical specifics — "went underground at seventeen... fifty years later... thirty-six of those years actively mining" — cut at HIGH severity) is the canonical empirical anchor that fact-check works at the discipline level. But Pass 3.1 catching invention after the fact is the safety net, not the primary control; the primary control is not generating invention in the first place.

### In sub-agent design + kickoff paste-texts

8. **Kickoff paste-texts for restoration / drafting sub-agents must specify substrate-discipline explicitly.** Do not delegate the discipline-decision to sub-agent judgment. Specify: "Do not generate illustrative invented prose; produce structure-only restoration recommendations + word-deltas + substrate-source citations. Where substrate is verifiable against canonical-facts inventory or published-work citation, generate prose. Where substrate would require lived knowledge or local-history source material, surface the gap as a structure-only finding."

9. **Parent-session ratification of sub-agent output should default to scrutinize-illustrative-prose.** Treat any illustrative-prose-with-substrate-critical-flag as a near-miss signal: the sub-agent generated invention at HIGH confidence and relied on the flag-discipline to catch. The right response is to ratify structure-only and route to author authorship, not to apply the illustrative prose with the flag attached.

## Compatible with existing rigor

- [`feedback_substrate_critical_editorial_input.md`](feedback_substrate_critical_editorial_input.md) 2026-05-21 — substrate-critical-editorial-input discipline (author substrate gets critical editorial input). This memory file extends the discipline: not only should author substrate get critical input, but **Claude-generated substrate should not contain factual invention in the first place**.
- [`feedback_named_subject_consent.md`](feedback_named_subject_consent.md) 2026-05-09 + 2026-05-12 — named-subject consent discipline. Inventing biographical specifics about named subjects violates the public-record exception's "this exception does NOT extend to *characterizations* of the subject's personal views, motivations, or beliefs beyond what the on-record quotes themselves say."
- [`feedback_audience_aware_drafting_discipline.md`](feedback_audience_aware_drafting_discipline.md) v3.1 — Pass 3.1 fact-check is the systematic verification layer; this memory file specifies that the discipline must operate at **generation** not just at **audit**.
- [`feedback_substance_drives_length.md`](feedback_substance_drives_length.md) 2026-05-02 — substance-drives-length supports shorter-but-true over longer-with-invention. If the brief target word count cannot be hit with substrate-safe restoration, ship shorter.
- [`feedback_voice_polish_pipeline.md`](feedback_voice_polish_pipeline.md) 2026-05-04 — voice-polish polishes raw author voice into published-register prose; this is distinct from inventing factual content. Polish ≠ invent.

## Empirical anchors

### Ch 2 → Harper's Pass 3.5 near-miss (2026-05-27)

The canonical anchor for this discipline. Pass 3.5 (developmental-edit; restoration polarity) sub-agent produced 6 RESTORE recommendations. Of those, 4 included illustrative prose containing invented factual claims:

- **F-3.5-H1** §I + §IV scene-anchor cluster: invented a diner-and-waitress encounter at §I close with three-generation family specifics (named-subject fabrication); invented Bailey-at-19 + Bailey's-father-retired-with-same-disease + specific career-arc mining-method timeline at §IV (biographical fabrication beyond canonical-facts inventory).
- **F-3.5-H3** §VII Purdue scene-rendering: invented Purdue internal documentary specifics ("sales representatives identifying physicians in specific counties"; "senior management discussing the four-characteristic profile in the language of opportunity") plausible-per-Keefe but unverified against the actual *Empire of Pain* text.
- **F-3.5-M1** §II Kennedy WV-primary context: attributed specific Kennedy motivations ("He went to McDowell County because he had been told...") + tactical claims (Humphrey-as-Protestant + party-apparatus favoritism) beyond canonical-facts inventory.
- **F-3.5-M2** §III Welch civic-life scene-render: invented period-typical civic-infrastructure specifics (Pittsburgh coats and dresses in department-store windows; two specific banks at intersection; full surgical wing; Tuesday-evening civic clubs) absent local-history substrate verification.

Each was flagged with `[Substrate-critical note: ...]` callouts. The parent session caught the pattern because (a) Pass 3.1 F-3.1-H1 existed as recognizable precedent; (b) the substrate-critical-editorial-input memory was loaded; (c) the ratification was reading-carefully rather than mechanical-apply. The catch worked, but the architecture was fragile: if any of (a)/(b)/(c) had failed, the inventions would have landed in the Harper's submission package and propagated to the author's reputational record. This memory file hardens the discipline by moving the control upstream — generation should not produce illustrative invented prose in the first place.

### Pass 3.1 F-3.1-H1 precedent (2026-05-27, same cascade)

Pass 3.1 fact-check on the Ch 2 → Harper's Stage 2 audience-blind draft surfaced F-3.1-H1 (HIGH): the Stage 2 drafter had invented three Bailey biographical specifics — "went underground at seventeen," "came out for the last time, on a stretcher, fifty years later," "thirty-six of those years actively mining" — that were not in canonical-facts inventory and were internally inconsistent with Bailey's documented February 2019 death at age 63. The invention was cut at HIGH severity at Pass 3.1 ratification; the canonical 36-year-underground tenure was restored. This is the canonical empirical demonstration that fact-check catches invention — but Pass 3.1 is the safety net, not the primary control. The primary control is not generating the invention.

### Stage 5 substrate-safe applications (2026-05-27)

Where substrate was canonically anchored or published-work-verifiable, Pass 3.5 + Stage 5 generation worked correctly:

- **F-3.5-H2** Catte attribution at §V line 73: Elizabeth Catte's *What You Are Getting Wrong About Appalachia* (2018) attribution sentence — published-work citation; verifiable; safe to draft and apply. Closed 4-prior-pass regional-scholarship-lineage carry-forward.
- **F-3.5-H3 (b)** Hamby attribution at §V line 71: Chris Hamby's *Soul Full of Coal Dust* (2020) book attribution — published-work citation; safe.
- **F-3.5-M3 (b) revised** structural-not-moral primer at §V line 63: framework-clarification sentence; no factual claim; safe.

These applications demonstrate the distinction: substrate-safe attributions (published-work citations; on-record quotes; framework clarifications) are permitted; substrate-critical invention (biographical / scene / motivation / documentary fabrication) is not.

## Discipline carry-forward to future work

This rule applies to:
- All subsequent Wave 2 + Wave 3 derivative essays (Ch 1 → Noema; Ch 3 → Atlantic Main; Ch 4 → Foreign Affairs; Ch 5 → Boston Review; Ch 6/7/8 future; Ch 9 → Atlantic Ideas + $100 Barrel; Ch 10 → Aeon; NYRB multi-book review; Berggruen Prize; etc.).
- All op-ed drafts + their news-peg activation variants.
- All book-proposal prose (chapter sketches; author platform paragraph; query letter to agents).
- Manuscript chapter prose at any rigor pass (Pass 3.1 fact-check + Pass 3.5 developmental-edit + Stage 4 + Stage 5).
- AI-disclosure paragraph adaptations across venues.
- Cover-letter drafts to editors / agents.
- Outreach packets to named subjects (Sandy, Colden, CBF, Phat, Tonya O'Connor, etc.) — outreach prose must accurately reflect intent + claims.

This rule does **not** apply to:
- Internal scaffolding (rigor-pass artifacts; PM dashboards; workstream handoffs; memory entries; templates) — these are working-document register; discipline is honest-process-record not testimonial.
- Ch 7 *On Other Worlds* explicit thought-experiment passages — per the narrow exception above.
- Author-drafted substrate the author themselves authors from lived knowledge — that's author testimony, not Claude generation.

## Where to read more

- Full pipeline doctrine: [`tools/commons_bonds_pipeline_doctrine_v1.0.0.md`](../commons_bonds_pipeline_doctrine_v1.0.0.md) — Stage 1 §7 canonical-facts inventory + Pass 3.1 fact-check protocol.
- Ch 2 → Harper's Pass 3.1 RATIFIED + APPLIED artifact: [`tools/rigor-passes/commons_bonds_rigor_pass_2026-05-27_ch2_harpers_essay_stage3_pass_3_1_fact_check_v1.0.0.md`](../rigor-passes/commons_bonds_rigor_pass_2026-05-27_ch2_harpers_essay_stage3_pass_3_1_fact_check_v1.0.0.md) §2 F-3.1-H1 — canonical fact-check-catches-invention empirical anchor.
- Ch 2 → Harper's Pass 3.5 RATIFIED + APPLIED artifact: [`tools/rigor-passes/commons_bonds_rigor_pass_2026-05-27_ch2_harpers_essay_stage3_pass_3_5_developmental_edit_v1.0.0.md`](../rigor-passes/commons_bonds_rigor_pass_2026-05-27_ch2_harpers_essay_stage3_pass_3_5_developmental_edit_v1.0.0.md) §3.1 — canonical illustrative-prose-substrate-critical-near-miss empirical anchor.

## Update log

- **2026-05-28.** Initial entry. Codifies the never-invent-factual-claims rule + thought-experiment exception + sub-agent generation discipline + parent-session ratification posture. Empirically grounded in Ch 2 → Harper's Pass 3.5 near-miss + Pass 3.1 F-3.1-H1 precedent (both 2026-05-27). Author flagged the rule + asymmetric stakes 2026-05-28; ratified same day.

---

*End of feedback_no_invented_factual_claims_in_publisher_facing_prose memory entry.*
