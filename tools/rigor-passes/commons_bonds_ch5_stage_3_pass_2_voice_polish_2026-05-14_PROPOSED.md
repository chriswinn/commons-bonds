# Stage-3 Rigor Pass — Chapter 5 (The Accountability Gap) — Pass 2: Voice-polish [PROPOSED]

**Date:** 2026-05-14
**Workstream:** #20 Manuscript Stage-3 Rigor Pass — Phase B — Ch 5 — Pass 2 (voice-polish)
**Chapter:** 5 — *The Accountability Gap*
**File audited:** [Chapter__5_THEACCOUNTABILITYGAP__Draft.md](manuscript/chapters/Chapter__5_THEACCOUNTABILITYGAP__Draft.md) — **237 lines** (post-Phase-C-α state verified 2026-05-14 against origin/main `da26bdc`)
**Status:** **PROPOSED — awaits author ratification. Phase C-β applies after ratification, paralleling Ch 1 Pass 2 commit `0b78449` → Phase C-γ commit `fa08c10`.**
**Mode:** Audit-existing-prose (post-Phase-C-α chapter is the baseline; v2.0 Amendment B voice-polish as a distinct pass from Pass 1 fact-check and Pass 3 audience-load).
**Pass scope:** Pass 2 (Voice-polish) only. Pass 1 ratified + Phase C-α applied (commit `da26bdc`); Pass 3 (Audience-load) deferred per per-pass serial cadence.
**Hard constraint observed:** No fixes applied to chapter file. Phase C-β (post-ratification) applies recommended edits.
**Branch:** `claude/ch5-pass-2-ecstatic-ardinghelli-d9376e` (off origin/main `da26bdc`).

---

## §0. Why this pass matters now

Ch 5 ships in the Sandy Darity send packet (Ch 5 + Ch 6 + Tech Appendix) post-2026-05-13 interview. Sandy is a labor economist who reads prose carefully and knows the underlying economics — Social Security, financial-crisis architecture, reparations-economics methodology — cold. Pass-2 voice-polish is the discipline that catches what fact-check (Pass 1) and audience-load (Pass 3) both miss: sentence-level coherence breaks, register-tells, repeated phrasings, apparatus residue in body prose, and the LLM-tic patterns trade-press editors flag on a careful read.

Pass 1 + Phase C-α resolved the chapter's gating fact-check items (MUST-FIX-2 $108T misattribution; MEDIUM-2 NOAA biological-magnitude; MEDIUM-3 depletion year 2033 at lines 108 + 110; MEDIUM-4 BP-Mexico 2018; N-3 foreclosure measure tightening; MEDIUM-1A + N-1 + N-2 + MEDIUM-5 integrated forward-pointer). The Phase C-α status section explicitly scoped five Pass-2-bound judgment calls forward to this session, and the task brief folded in two additional Pass-1 Tier-2 cleanup items that touch the same passages (MEDIUM-1 CBO $150B hedge at line 46; N-5 $16T cumulative-not-peak at line 82).

This pass audits the Phase-C-α prose at full strength for voice-polish issues and produces the spot-fix recommendations Phase C-β will apply verbatim before the Sandy send.

---

## §1. Source artifacts read

1. [`tools/drafting-templates/stage-3-three-pass-rigor-audit.md`](tools/drafting-templates/stage-3-three-pass-rigor-audit.md) §"Pass 2: Voice-polish" — canonical scaffold for this pass.
2. Memory: [`feedback_voice_polish_pipeline.md`](/Users/c17n/.claude/projects/-Users-c17n-commons-bonds/memory/feedback_voice_polish_pipeline.md) (dump → sift → polish; polish actively for grammar/flow; don't preserve raw author voice).
3. Memory: [`feedback_dual_audience_test.md`](/Users/c17n/.claude/projects/-Users-c17n-commons-bonds/memory/feedback_dual_audience_test.md) (every rewrite tested against layman + specialist; "shorter = better" is wrong; substance drives length).
4. Memory: [`feedback_substance_drives_length.md`](/Users/c17n/.claude/projects/-Users-c17n-commons-bonds/memory/feedback_substance_drives_length.md) (no arbitrary word-count targets).
5. Memory: [`feedback_audience_aware_drafting_discipline.md`](/Users/c17n/.claude/projects/-Users-c17n-commons-bonds/memory/feedback_audience_aware_drafting_discipline.md) (v2.0 Amendment B — distinct passes).
6. Memory: [`feedback_grammatical_role_cross_references.md`](/Users/c17n/.claude/projects/-Users-c17n-commons-bonds/memory/feedback_grammatical_role_cross_references.md) (chapter→appendix cross-reference discipline).
7. [`manuscript/chapters/Chapter__5_THEACCOUNTABILITYGAP__Draft.md`](manuscript/chapters/Chapter__5_THEACCOUNTABILITYGAP__Draft.md) — 237 lines, post-Phase-C-α state.
8. [`tools/rigor-passes/commons_bonds_ch5_stage_3_pass_1_fact_check_2026-05-13_PROPOSED.md`](tools/rigor-passes/commons_bonds_ch5_stage_3_pass_1_fact_check_2026-05-13_PROPOSED.md) — Pass 1 + Amendments 1 + 2 + §B.7 + Phase C-α status section.
9. [`tools/rigor-passes/commons_bonds_rigor_pass_2026-05-13_ch1_the_quiet_math_stage3_voice_polish_v1.0.0.md`](tools/rigor-passes/commons_bonds_rigor_pass_2026-05-13_ch1_the_quiet_math_stage3_voice_polish_v1.0.0.md) — Ch 1 Pass 2 structural reference.

---

## §2. Pass-2 scope reminder

Pass 2 audits prose for the LLM tics + voice issues trade-press editors flag, plus the audit-existing-prose mode's consistency-check addendum. The named-inventory categories applied below:

- **Rule of three / declarative-three-in-a-row** — A. B. C. constructions; flag if pattern-dense.
- **Em-dash crutches** — em-dashes used as connective tissue rather than as deliberate parenthetical extension or punch.
- **Tidy parallels** — He did X. She did Y. They did Z. structures; anaphoric repetition that becomes visible cadence.
- **Hedge phrases** — "I will argue that…" / "Perhaps…" / "It seems likely that…"
- **Connective-tissue clichés** — "in short" / "ultimately" / "moreover" / "furthermore" / "that being said"
- **Meta-commentary** — "That is the whole sentence." / "Let me explain…"
- **Expository flatness** — "The plain definition is this:" / "Here is what I think:"
- **Cadence repetition** — "It changed me. It humbled me. It made…" patterns; chiastic emotional-symmetry codas.
- **Apparatus residue** — Greek letters, subscripts, formula-shorthand acronyms appearing in body prose where Ch 5's plain-language register prohibits.
- **Consistency check (audit-existing-prose mode)** — does the prose align with the chapter's own argument? Surfaces logic-inversions and conceptual-coherence breaks the Phase-C-α prose may have introduced (post-spot-fix prose is reviewed for coherence at distance from the spot-fix moment).
- **Closely-repeated phrasing** — same content-word or phrase appearing two-or-more times within a small window where one usage is rhetorical and the rest are redundancy.
- **Grammatical-role discipline for cross-references** — per `feedback_grammatical_role_cross_references.md`: sections-as-nouns named only; sections-as-citations name + §; theorems/definitions compound identifier.

Ch 5's specific emphasis per the Phase C-α Judgment Calls + the task brief's named targets: (a) post-Phase-C-α line-138 internal-consistency residual; (b) line-46 duplicate "estimated" + CBO $150B hedge; (c) line-82 "larger than Ohio" antecedent + $16T cumulative reframe; (d) lines-116–124 prose-flow tightening around the line-112 opportunity-cost reframe; (e) line-220 near-duplicate phrasing.

---

## §3. Summary verdict

| Severity | Count | Disposition |
|---|---|---|
| **MUST-FIX** | 5 | Sandy-send-gating; both grammar errors + the inverted-logic sentence at line 86 are catch-on-first-read items |
| **SHOULD-FIX** | 5 | High-priority pre-send; covers the remaining task-brief named targets + apparatus residue at line 50 |
| **MEDIUM** | 6 | Precision-tightening; recommended pre-send but author-discretion |
| **LOW** | 7 | Style preferences / hold-as-is default |

**Total findings:** 23.

**Aggregate verdict:** **READY AFTER PHASE C-β SPOT-FIXES.** The chapter's analytical-essay register is fundamentally strong; counter-argument structure is rigorous; reparations-economics lineage prose is intellectually honest. The five MUST-FIX findings are all isolated spot-fixable items (one grammar error, one inverted-logic sentence, one comparison whose antecedent broke under Phase C-α, one internal-consistency residual, one multi-paragraph conceptual-coherence tightening). The SHOULD-FIX set absorbs the remaining task-brief targets cleanly. No structural voice revision needed.

---

## §4. Findings — MUST-FIX (Sandy-send gating)

Issues that any careful reader catches on first pass; multiple are grammar errors or logic-inversions that a fact-checker / Sandy / a trade-press editor would all flag immediately.

### F-V1 — Inverted information-asymmetry sentence at 2008 counter-argument [MUST-FIX]

**Location:** [Chapter__5_THEACCOUNTABILITYGAP__Draft.md:86](manuscript/chapters/Chapter__5_THEACCOUNTABILITYGAP__Draft.md:86)

**Chapter text (post-Phase-C-α):**
> "Cost severance does not require borrower-as-victim framing; in the 2008 case it operated through deliberate information asymmetry — **the cost-bearing party had information the value-extracting party did not,** and the information structure was structurally adversarial."

**Why this flags.** The clause inverts the paragraph's own argument. The surrounding text argues, at length, that lenders/originators had information borrowers did not — *"originator commissions were tied to volume rather than to default rates… broker-disclosed terms differed materially from contract terms… adjustable-rate products were marketed to borrowers whose understanding of rate-reset mechanics was, by industry-internal acknowledgment, expected to be incomplete."* The information asymmetry the paragraph documents is value-extractor-had-more-information; the spot-fix sentence reads the reverse. A reader following the argument will register the sentence as flat-contradictory.

**Severity rationale.** (a) Sandy Darity reads paragraph-by-paragraph and will spot the inversion on first read; (b) the inversion is concrete and falsifiable against the paragraph's own evidence; (c) the chapter's counter-argument-handling discipline is one of its load-bearing strengths — an inverted sentence inside a counter-argument paragraph erodes the chapter's argumentative authority more than the same error elsewhere would.

**Recommended rewrite (apply verbatim at Phase C-β):**
> "Cost severance does not require borrower-as-victim framing; in the 2008 case it operated through deliberate information asymmetry — the value-extracting party had information the cost-bearing party did not, and the information structure was structurally adversarial."

(Single-word swap: *"the cost-bearing party had information the value-extracting party did not"* → *"the value-extracting party had information the cost-bearing party did not"*. Reverses the subject and object of the comparison; aligns the clause with the surrounding paragraph's argument.)

**Cross-pass flag.** This is a Pass-2-surfaced consistency-check finding within the audit-existing-prose mode (Pass 4 / consistency check in the canonical scaffold). It is logic-coherence, not fact-check against canonical sources, but if Phase C-β prefers to confirm the substantive direction with Pass 1 before applying, the confirmation is trivial: read the preceding 100 words of the same paragraph. The fix is single-word and low-risk.

---

### F-V2 — Missing article: "Social Security is not Ponzi scheme" [MUST-FIX]

**Location:** [Chapter__5_THEACCOUNTABILITYGAP__Draft.md:122](manuscript/chapters/Chapter__5_THEACCOUNTABILITYGAP__Draft.md:122)

**Chapter text:**
> "**Social Security is not Ponzi scheme** — it is a genuine intergenerational transfer program providing essential benefits to millions of Americans."

**Why this flags.** Missing indefinite article before *"Ponzi scheme"*. Standard English requires *"is not a Ponzi scheme"*. The error is glaring on read; a fact-checker / copyeditor / trade-press editor / Sandy Darity will all spot it on first pass. The sentence sits at a load-bearing rhetorical moment (the chapter's most-cited Ponzi-scheme-rebuttal beat for Social Security).

**Severity rationale.** (a) Grammar error of the type any reader catches; (b) sits at a high-attention rhetorical pivot (rebutting the Ponzi-scheme framing); (c) one-character fix.

**Recommended rewrite (apply verbatim at Phase C-β):**
> "Social Security is not a Ponzi scheme — it is a genuine intergenerational transfer program providing essential benefits to millions of Americans."

(Single insertion: *"a"* before *"Ponzi scheme"*.)

---

### F-V3 — "Larger than Ohio" comparison broken by Phase-C-α antecedent shift [MUST-FIX]

**Location:** [Chapter__5_THEACCOUNTABILITYGAP__Draft.md:82](manuscript/chapters/Chapter__5_THEACCOUNTABILITYGAP__Draft.md:82)

**Chapter text (post-Phase-C-α):**
> "Meanwhile, approximately ten million American households received foreclosure filings between 2008 and 2012, with roughly five million resulting in completed foreclosure — **a population larger than Ohio,** displaced in under five years."

**Why this flags.** The Phase-C-α N-3 spot-fix correctly tightened the foreclosure measure to distinguish filings (~10M) from completed foreclosures (~5M). The original "larger than Ohio" comparison anchored to the earlier "10M households lost their homes" framing (10M households × ~2.5 persons/household ≈ 25M people, comfortably larger than Ohio's ~11.8M population). Post-spot-fix, the em-dash appositive *"— a population larger than Ohio, displaced in under five years"* now reads as modifying the immediately-preceding clause (*"with roughly five million resulting in completed foreclosure"*). Five million people is less than half of Ohio's population; the comparison reads as wrong on a careful read. Even read generously as modifying the filings clause, the antecedent is ambiguous and the comparison reads loosely.

**Severity rationale.** (a) The comparison is mathematically wrong under the post-spot-fix antecedent; (b) Sandy Darity engages displacement / household-wealth-loss methodology and will know CoreLogic / Census magnitudes; (c) the comparison sits at the chapter's load-bearing 2008-rescue-asymmetry beat — its rhetorical force depends on the magnitude landing correctly.

**Recommended rewrite (apply verbatim at Phase C-β):**

Author selects one. All three preserve the foreclosure-measure tightening that Phase C-α intentionally introduced; the choice is whether to recover the Ohio comparison, swap to a different anchor, or drop the comparison and let the raw numbers carry the magnitude.

- **Option A — re-target to a Census comparison that fits the post-spot-fix measure.** Replace *"— a population larger than Ohio, displaced in under five years"* with *"— more households than there are in the entire state of Pennsylvania, foreclosed in under five years."* (Pennsylvania has ~5.7M households per the 2020 Census; the 5M completed-foreclosure measure now lands comfortably under the comparison. The displacement framing shifts from "population" to "households," which matches the measure CoreLogic actually publishes.)
- **Option B — broaden the antecedent back to the filings figure.** Replace *"with roughly five million resulting in completed foreclosure — a population larger than Ohio, displaced in under five years"* with *"with roughly five million resulting in completed foreclosure. The cumulative filings reached more households than live in Ohio and Pennsylvania combined."* (Splits the sentence; the Ohio + Pennsylvania household-pair anchor matches the ~10M filings measure more cleanly than the original Ohio-population anchor matched it; preserves the geographic-magnitude framing the original sentence reached for.)
- **Option C — drop the comparison entirely; let the raw numbers carry.** Replace *"with roughly five million resulting in completed foreclosure — a population larger than Ohio, displaced in under five years."* with *"with roughly five million resulting in completed foreclosure. Five million households is roughly the entire state of Tennessee, foreclosed over the same window."* (Tennessee has ~2.7M households; 5M completed foreclosures ≈ 2x Tennessee households. Quietly accurate; less rhetorical reach than the Ohio comparison but uncontestable on the math.)

Author preference recommended: **Option A** — closest to the original sentence shape; one-clause swap; preserves the displacement framing the chapter argument needs.

**Why the original Ohio comparison fit the pre-Phase-C-α prose but not the post.** Original: "10M households lost their homes" → ~25M+ people displaced → comfortably larger than Ohio. Post-spot-fix: ~5M completed foreclosures → with ~2.5 persons/household ≈ ~12.5M people, near Ohio but no longer comfortably larger; if the antecedent reads as the bare 5M number, the comparison breaks. Phase C-α intentionally tightened the measure (filings vs completed) and the comparison was downstream of that tightening; Pass 2 catches the residual.

---

### F-V4 — Line 138 "2034" residual contradicts post-Phase-C-α lines 108 + 110 at 2033 [MUST-FIX]

**Location:** [Chapter__5_THEACCOUNTABILITYGAP__Draft.md:138](manuscript/chapters/Chapter__5_THEACCOUNTABILITYGAP__Draft.md:138)

**Chapter text (post-Phase-C-α):**
> "The timeline-and-tractability objection holds that the framework's account inflates what is, on a sober reading, a soluble public-finance problem. The trust fund will not run out tomorrow; **it will run out in 2034,** more than half a century after the legislative expansions that generated the obligations."

**Why this flags.** Phase C-α applied the OASI-2033 correction at lines 108 + 110 per the 2024 Trustees Report. Line 138 retained "2034" — the 2023 Trustees Report's old OASDI-combined date (now superseded for both OASI-alone and OASDI-combined framings; 2024 Trustees: OASI 2033 / OASDI 2035). The chapter now says 2033 twice early and 2034 once in a counter-argument paragraph 30 lines later. Sandy Darity knows the Trustees-Report dates; the internal inconsistency reads as either a slip or a different-data-source ambiguity. Either way, it erodes precision.

The line 138 use sits inside the counter-argument's voice (*"the trust fund will not run out tomorrow; it will run out in 2034"*) — the year functions as the counter-argument's anchor for the *"more than half a century after the legislative expansions"* claim. The substance the counter-argument is making (timeline-tractability over a generational horizon) is preserved by either year; only the date-specific anchor needs alignment.

**Severity rationale.** (a) Internal inconsistency within the same chapter at two points 30 lines apart; (b) Sandy will notice; (c) trivial fix.

**Recommended rewrite (apply verbatim at Phase C-β):**
> "The timeline-and-tractability objection holds that the framework's account inflates what is, on a sober reading, a soluble public-finance problem. The trust fund will not run out tomorrow; it will run out in 2033, more than half a century after the legislative expansions that generated the obligations."

(Single-character fix: *"2034"* → *"2033"*. Aligns line 138 with lines 108 + 110 OASI framing.)

**Note for Phase C-β.** The Pass-1 §B.2 verification verdict at MEDIUM-3 noted the OASI-2033 / OASDI-2035 fork; Phase C-α chose OASI (minimum-edit at lines 108 + 110 preserving the canonical "77%" benefit-rate). Line 138's correction follows the same OASI framing. If the author later opts to shift the chapter to OASDI-combined (2035 + 83%), that's a separate cross-paragraph re-anchoring requiring both 108/110 and 138 to move together, plus the line 110 "seventy-seven percent" → "eighty-three percent" cascade.

---

### F-V5 — Lines 116–124 prose-flow still tuned to unfunded-liability framing under line-112 opportunity-cost reframe [MUST-FIX]

**Location:** [Chapter__5_THEACCOUNTABILITYGAP__Draft.md:116-124](manuscript/chapters/Chapter__5_THEACCOUNTABILITYGAP__Draft.md:116)

**Chapter text (post-Phase-C-α):** Lines 116, 118, 120, 122, and 124 carry the post-Phase-C-α opportunity-cost reframe of line 112's foundational claim. The Phase-C-α status section flagged that the surrounding paragraphs still carry wording originally anchored to the unfunded-liability framing that MUST-FIX-2 corrected. Pass 2 confirms the diagnosis and proposes the integrated tightening.

The specific phrasings that read as residual unfunded-liability framing under the new line-112 opportunity-cost anchor:

| Line | Phrase | Tension with line-112 opportunity-cost framing |
|---|---|---|
| 116 | *"The cost of paying for those promises was severed from the politicians who made them"* | The cost severance under opportunity-cost framing is the foregone compounding of payroll-tax surpluses, not "the cost of paying for promises." |
| 118 | *"the affected community is every future American taxpayer"* | Under opportunity-cost framing, the affected community is the working-class payroll-tax contributors over 88 years whose contributions failed to compound at productive rates, not "every future taxpayer." (Future taxpayers are *one* affected community; the original cost-bearing parties are the principal one the opportunity-cost framing prices.) |
| 120 | *"The bill was transferred to their children and grandchildren"* / *"a system that promises more than it can deliver"* | "The bill" is unfunded-liability metaphor. Under opportunity-cost framing, what was transferred is foregone-investment-return; what the system "delivers" is the compounded result of the Treasury-IOU routing choice, not a promise-delivery question. |
| 122 | *"One hundred and eight trillion dollars in costs, severed from the generations who created them and transferred to generations who had no say in creating them"* | Under opportunity-cost framing, $108T isn't a "cost severed from generations who created them" — it's the compounded foregone investment return on 88 years of working-class payroll-tax contributions extracted via the Treasury-IOU mechanism. The "transferred to generations who had no say" framing imports the unfunded-liability metaphor that line 112 specifically replaced. |
| 124 | *"the cost severance the U.S. choice produces"* | This line is already well-aligned with the architectural-choice framing of line 112; flagged here only to note where the tightening should land cleanly (no rewrite needed at line 124). |

**Why this flags.** MUST-FIX-2's Option-A spot-fix at line 112 was load-bearing; the chapter's most-cited Social Security figure is now correctly framed as foregone-investment opportunity cost rather than as unfunded actuarial liability. But the surrounding 4-paragraph cluster (116, 118, 120, 122) still speaks in the unfunded-liability register at multiple points. A reader who arrives at line 112 with the new framing and then reads forward will hit the unfunded-liability metaphors in 116, 118, 120, 122 and either (a) read them as inconsistent with the new line-112 framing or (b) re-import the unfunded-liability framing the chapter's MUST-FIX-2 was specifically correcting. Sandy Darity will notice the framing inconsistency on careful read; a less-careful reader may simply absorb the inconsistency without noticing it as inconsistency, which is the worse outcome (the chapter's MUST-FIX-2 correction lands less cleanly than it should).

**Severity rationale.** (a) The tightening is the completion-of-work that Phase C-α intentionally scoped forward to Pass 2; (b) the substantive coherence between line 112 and surrounding paragraphs is load-bearing for the chapter's most-cited number; (c) Sandy Darity will engage the framing rigor in detail; (d) Phase C-α already named this as the dominant Pass-2 work in the Social Security section.

**Recommended rewrite (apply verbatim at Phase C-β).**

Author selects one integration depth. The recommended depth: **Option B (paragraph-level tightening at 116, 118, 120, 122)**. The Ch 5 substance argument is preserved; the framing aligns cleanly across 112 → 124; the rhetorical force of the Social Security section's most-quoted lines is preserved through targeted phrase-level swaps rather than wholesale rewrite.

- **Option A — minimum edit (target only the most-glaring unfunded-liability metaphors).** Touch lines 120 and 122 only; leave 116 and 118 as-is. Specific edits:

  Line 120, replace:
  > "The bill was transferred to their children and grandchildren, who will inherit a system that promises more than it can deliver and face the political choice between honoring promises they did not make or breaking commitments that older Americans organized their lives around."

  with:
  > "The foregone compounding was transferred to their children and grandchildren, who will inherit a system whose surpluses were routed through the Treasury-IOU mechanism instead of into productive sovereign capital, and face the political choice between absorbing the resulting funding gap themselves or breaking commitments that older Americans organized their lives around."

  Line 122, replace:
  > "One hundred and eight trillion dollars in costs, severed from the generations who created them and transferred to generations who had no say in creating them."

  with:
  > "One hundred and eight trillion dollars in foregone return, extracted from the architecture by the routing choice that earlier generations made and transferred to generations who had no say in making it."

- **Option B — paragraph-level tightening across 116, 118, 120, 122 (RECOMMENDED).** Apply Option A's line 120 + 122 edits plus the following:

  Line 116, replace:
  > "The cost of paying for those promises was severed from the politicians who made them and the voters who rewarded them, and transferred forward in time to generations who were either too young to vote or not yet born."

  with:
  > "The foregone-investment cost the Treasury-IOU routing produced was severed from the politicians who chose that routing and the voters who rewarded the benefit-expansions it underwrote, and transferred forward in time to generations who were either too young to vote or not yet born."

  Line 118, replace:
  > "The mechanism is identical to what happened in Libby, the Gulf, and Baotou. Value was extracted by one group of actors. Costs were severed from those actors and transferred to a different group — one with less power to refuse the transfer. The difference is that in the Social Security case, the transfer was accomplished through time rather than space, and the affected community is every future American taxpayer."

  with:
  > "The mechanism is identical to what happened in Libby, the Gulf, and Baotou. Value was extracted by one group of actors. Costs were severed from those actors and transferred to a different group — one with less power to refuse the transfer. The difference is that in the Social Security case, the transfer was accomplished through time rather than space, and the affected community is the working-class payroll-tax contributors whose surpluses failed to compound, plus every future American taxpayer who will absorb the resulting funding gap."

- **Option C — full rewrite of the 116–124 cluster.** Not recommended. Substance is sound; rhetorical force of the section's quoted lines (especially "Social Security is not a Ponzi scheme…" beat at 122 and "the largest cost severance in human history…" coda at 122) is preserved by Option B's targeted swaps.

**Cross-pass flag.** None of Option A or B introduces new factual claims; both stay within the canonical opportunity-cost framing the case-study brief's $108T-as-foregone-investment-counterfactual already supports. The edits are voice-coherence, not fact-check.

---

## §5. Findings — SHOULD-FIX (high-priority pre-send)

Issues that any careful copyedit pass catches; high-priority for Sandy send but not on the same gating level as the MUST-FIX set.

### F-V6 — Duplicate "estimated" within the NOAA biological-magnitude rewrite [SHOULD-FIX]

**Location:** [Chapter__5_THEACCOUNTABILITYGAP__Draft.md:46](manuscript/chapters/Chapter__5_THEACCOUNTABILITYGAP__Draft.md:46)

**Chapter text (post-Phase-C-α MEDIUM-2 application):**
> "Even that number understates the true cost. **The National Oceanic and Atmospheric Administration estimated that the spill killed an estimated 4 to 8 billion oysters** and 2 to 5 trillion newly hatched fish, along with tens of thousands of birds and sea turtles that would have supported Gulf fisheries and ecosystems for years."

**Why this flags.** Two *"estimated"* tokens within ten words. The first (*"NOAA estimated that…"*) attributes the figure to the agency; the second (*"killed an estimated 4 to 8 billion"*) hedges the magnitude inside the attribution. The redundancy is glaring on read; a copyeditor catches it immediately. Phase C-α status section flagged this explicitly under the "Do NOT improvise prose" directive — the recommended-rewrite text was applied verbatim including the duplicate, with the cleanup forwarded to Pass 2.

**Severity rationale.** (a) Verbatim duplicate-token within one clause; (b) glaring on read; (c) trivial fix; (d) sits in the chapter's most-cited NOAA paragraph.

**Recommended rewrite (apply verbatim at Phase C-β):**
> "Even that number understates the true cost. The National Oceanic and Atmospheric Administration estimated that the spill killed 4 to 8 billion oysters and 2 to 5 trillion newly hatched fish, along with tens of thousands of birds and sea turtles that would have supported Gulf fisheries and ecosystems for years."

(Single-word cut: drop the second *"an estimated"*. The NOAA attribution at the sentence's head carries the hedge for the entire clause.)

---

### F-V7 — CBO $150B attribution at line 46 unverifiable; replace with multi-source aggregate hedge [SHOULD-FIX]

**Location:** [Chapter__5_THEACCOUNTABILITYGAP__Draft.md:46](manuscript/chapters/Chapter__5_THEACCOUNTABILITYGAP__Draft.md:46) (final sentence of the same paragraph as F-V6)

**Chapter text:**
> "The Congressional Budget Office estimated total economic losses — including losses that no court could assign to any single responsible party — at over one hundred and fifty billion dollars."

**Why this flags.** Per Pass 1 §B.2 Amendment-2 verification, **no CBO publication carries a $150B total-economic-losses figure for Deepwater Horizon**. The aggregate is order-of-magnitude-defensible from multi-source aggregation (tourism ~$23B over 3 years per US Travel Association; fishing ~$2.5B; BP cumulative costs ~$65B+) but the CBO attribution is unsupportable. Sandy Darity reads carefully and a fact-checker following CBO citations will catch the absence. This is Pass-1 MEDIUM-1 (deferred from Phase C-α as Tier-2 cleanup; folded into Pass 2 per task brief because it touches the same passage as F-V6).

**Severity rationale.** (a) Citation attribution is unsupportable; (b) Sandy Darity reads with attention to source-citations; (c) the multi-source aggregate framing is defensible and substance-preserving.

**Recommended rewrite (apply verbatim at Phase C-β):**
> "Aggregate estimates from academic, insurance-industry, and federal sources place total economic losses at over one hundred and fifty billion dollars."

(Replaces the CBO-specific attribution with a multi-source aggregate framing that the actual numerical evidence supports.)

**Sequencing note.** F-V6 + F-V7 both target line 46. Apply F-V6 first (drop duplicate "estimated"), then F-V7 (replace final sentence). The two are independent edits in the same paragraph.

---

### F-V8 — "$16T at peak" mis-frames the GAO 2011 figure; replace with cumulative framing [SHOULD-FIX]

**Location:** [Chapter__5_THEACCOUNTABILITYGAP__Draft.md:82](manuscript/chapters/Chapter__5_THEACCOUNTABILITYGAP__Draft.md:82)

**Chapter text (post-Phase-C-α):**
> "TARP provided seven hundred billion dollars in public funds to stabilize financial institutions. The Federal Reserve's emergency lending facilities, the full scale of which emerged only through later congressional requests and litigation, **exceeded sixteen trillion dollars at peak.**"

**Why this flags.** Per Pass 1 §B.3 N-5 + GAO-11-696 + CRS R44185: the $16T figure is the **cumulative sum of all loans across the crisis** (regardless of term), not the peak outstanding balance. Peak outstanding Fed-facility loans were ~$1T in late 2008; Bloomberg's $7.77T figure included guarantees and commitments. *"At peak"* is technically misleading. Sandy Darity knows Federal Reserve emergency-lending accounting and will flag the framing. This is Pass-1 N-5 (deferred from Phase C-α as Tier-2 cleanup; folded into Pass 2 per task brief because it touches the same line as F-V3 + the F-V3 antecedent question).

**Severity rationale.** (a) Mis-frames a GAO-canonical figure; (b) Sandy will flag; (c) trivial fix; (d) preserves the chapter's substantive point (Fed-facility scale was enormous regardless of how it's framed).

**Recommended rewrite (apply verbatim at Phase C-β):**
> "TARP provided seven hundred billion dollars in public funds to stabilize financial institutions. The Federal Reserve's emergency lending facilities, the full scale of which emerged only through later congressional requests and litigation, exceeded sixteen trillion dollars in cumulative emergency loans across the crisis (per the GAO's 2011 audit)."

(Replaces *"exceeded sixteen trillion dollars at peak"* with *"exceeded sixteen trillion dollars in cumulative emergency loans across the crisis (per the GAO's 2011 audit)"*. Preserves the magnitude; corrects the framing; adds the GAO 2011 attribution that anchors the figure.)

**Sequencing note.** F-V3 + F-V8 both target line 82. The two edits are independent (different sentences within the same long paragraph); apply both.

---

### F-V9 — Near-duplicate "framework reaches coerced cases through legacy effects" phrasing at line 220 [SHOULD-FIX]

**Location:** [Chapter__5_THEACCOUNTABILITYGAP__Draft.md:220](manuscript/chapters/Chapter__5_THEACCOUNTABILITYGAP__Draft.md:220)

**Chapter text (post-Phase-C-α):**
> "Coerced extraction is different: the cost-bearer knows, and is forced to bear it anyway. **The framework reaches coerced cases through their legacy effects** — wealth gaps, longevity gaps, cultural-knowledge transmission disruption, intergenerational trauma. The direct pricing of the coercion vector remains an open question. The Technical Appendix's scope-of-applicability boundary at §1.10 names the variable explicitly (informed by Darity, personal communication, May 2026); **the framework reaches coerced cases through legacy-effects pricing,** and the direct pricing of coercion-as-cost-dimension is acknowledged outside the book's empirical scope."

**Why this flags.** Two near-duplicate phrasings within ~50 words: *"The framework reaches coerced cases through their legacy effects"* and *"the framework reaches coerced cases through legacy-effects pricing"*. The first introduces the legacy-effects pathway and lists the specific gaps the framework prices; the second appended sentence repeats the framing without adding substance, then continues to the *"direct pricing of coercion-as-cost-dimension is acknowledged outside the book's empirical scope"* qualifier.

Phase C-α status section flagged this explicitly: *"the recommended-rewrite text was applied verbatim"* (per the task brief's no-improvise directive); Pass 2's job is to tighten without losing the load-bearing TA §1.10 forward-pointer or the Darity-personal-communication attribution.

**Severity rationale.** (a) Visible near-duplicate phrasing on read; (b) tightens cleanly without losing substance; (c) the load-bearing TA cross-reference (per `feedback_grammatical_role_cross_references.md` — TA §1.10 is a sections-as-citation, so name + § format is correct) and the Darity attribution both need to survive the tightening.

**Recommended rewrite (apply verbatim at Phase C-β):**
> "Coerced extraction is different: the cost-bearer knows, and is forced to bear it anyway. The framework reaches coerced cases through their legacy effects — wealth gaps, longevity gaps, cultural-knowledge transmission disruption, intergenerational trauma. The direct pricing of the coercion vector remains an open question, acknowledged outside the book's empirical scope; the Technical Appendix's scope-of-applicability boundary at §1.10 names the variable explicitly (informed by Darity, personal communication, May 2026)."

(Drops the redundant *"the framework reaches coerced cases through legacy-effects pricing"*. Folds the *"direct pricing of coercion-as-cost-dimension is acknowledged outside the book's empirical scope"* qualifier into the prior sentence. Preserves the TA §1.10 forward-pointer + Darity attribution at the paragraph's close. Grammatical-role: TA §1.10 is a sections-as-citation parenthetical pointer, name + § format retained.)

---

### F-V10 — Apparatus residue: "B postings" in body prose at line 50 [SHOULD-FIX]

**Location:** [Chapter__5_THEACCOUNTABILITYGAP__Draft.md:50](manuscript/chapters/Chapter__5_THEACCOUNTABILITYGAP__Draft.md:50)

**Chapter text:**
> "American Gulf-state litigation operated under the Oil Pollution Act of 1990 + extensive state-level environmental and tort jurisprudence + a class-action infrastructure that allowed individual claimants to aggregate at scale. Mexican claimants operated under a substantially weaker legal-architecture for cross-border environmental claims against a foreign-domiciled corporation. **Same spill, same operator, same physical-mechanism of damage, structurally different B postings.** The international architectural-asymmetry is not a bug of the framework's accounting — it is a feature the framework's accounting makes visible."

**Why this flags.** *"B postings"* uses the Technical-Appendix B-notation (B₁ Restitution Bond / B₂ Foreclosure Bond) as apparatus shorthand in body prose. Ch 5 is otherwise apparatus-clean: the chapter uses *"Restitution Bond"*, *"Foreclosure Bond"*, *"accountability bond posting"*, *"bond posted"* throughout body prose — full names, not B-notation. The single capital-B token here is leftover apparatus that escaped earlier polishing. Per Ch 5's plain-language register decision (the chapter speaks the framework's vocabulary in full forms; the B-notation lives in the Technical Appendix), this is a residue catch.

**Severity rationale.** (a) Apparatus residue per the Stage-3 Pass-2 inventory's named category; (b) Sandy Darity reads carefully and the capital-B shorthand will register as either typo or unmotivated jargon; (c) one-word fix; (d) the chapter's apparatus-discipline (named flagship terms in body prose; B-notation in TA) is otherwise clean.

**Recommended rewrite (apply verbatim at Phase C-β):**
> "American Gulf-state litigation operated under the Oil Pollution Act of 1990 + extensive state-level environmental and tort jurisprudence + a class-action infrastructure that allowed individual claimants to aggregate at scale. Mexican claimants operated under a substantially weaker legal-architecture for cross-border environmental claims against a foreign-domiciled corporation. Same spill, same operator, same physical-mechanism of damage, structurally different bond postings. The international architectural-asymmetry is not a bug of the framework's accounting — it is a feature the framework's accounting makes visible."

(*"B postings"* → *"bond postings"*. Aligns with chapter-wide named-flagship-term discipline in body prose; preserves the quadruple-anaphora structure of the sentence.)

---

## §6. Findings — MEDIUM (precision-tightening)

Patterns that any careful copyedit pass catches; recommended pre-send but not Sandy-send-gating. Many are isolated phrasing-tightenings; one is a chapter-wide phrase-repetition pattern.

### F-V11 — Close repetition: "significantly less" at line 156 [MEDIUM]

**Location:** [Chapter__5_THEACCOUNTABILITYGAP__Draft.md:156](manuscript/chapters/Chapter__5_THEACCOUNTABILITYGAP__Draft.md:156)

**Chapter text:**
> "Medical fundraising campaigns organized by individuals with distinctively African American or Hispanic surnames **raise significantly less and are significantly less likely** to meet their goals, even controlling for geography and time period."

**Why this flags.** *"Significantly less"* used twice within five words. The first describes a magnitude-of-fundraising disparity; the second describes a probability-of-meeting-goals disparity. The repetition is a minor copyedit catch; trade-press editors will register it on a careful read.

**Severity rationale.** (a) Visible close repetition; (b) one-word swap clears it; (c) sits at the chapter's most-cited GoFundMe disparity beat — small but visible.

**Recommended rewrite (apply verbatim at Phase C-β):**
> "Medical fundraising campaigns organized by individuals with distinctively African American or Hispanic surnames raise substantially less and are significantly less likely to meet their goals, even controlling for geography and time period."

(Single-word swap: first *"significantly less"* → *"substantially less"*. Preserves the magnitude-vs-probability distinction; eliminates the verbatim repetition.)

---

### F-V12 — Hyphenation: "off world" → "off-world" at line 214 [MEDIUM]

**Location:** [Chapter__5_THEACCOUNTABILITYGAP__Draft.md:214](manuscript/chapters/Chapter__5_THEACCOUNTABILITYGAP__Draft.md:214)

**Chapter text:**
> "In later chapters we will walk through a theoretical use case of the abundance of clean air being stripped — by an **off world colony** on Mars engineering its own atmosphere, by a climate crisis on Earth — costs of atmospheric services become visible that the abundance had masked."

**Why this flags.** *"Off world colony"* is a compound adjective modifying *"colony"*; standard style requires hyphenation: *"off-world colony"*. The chapter elsewhere uses *"off-Earth extraction"* at line 230 (hyphenated correctly), so the line-214 unhyphenated form is internally inconsistent with the chapter's own usage.

**Severity rationale.** (a) Hyphenation error; (b) internal inconsistency with line 230; (c) trivial fix.

**Recommended rewrite (apply verbatim at Phase C-β):**
> "In later chapters we will walk through a theoretical use case of the abundance of clean air being stripped — by an off-world colony on Mars engineering its own atmosphere, by a climate crisis on Earth — costs of atmospheric services become visible that the abundance had masked."

(*"off world"* → *"off-world"*. Aligns with line 230's *"off-Earth extraction"* usage.)

---

### F-V13 — Chapter-wide phrase repetition: "most vulnerable stretches of life" [MEDIUM]

**Locations:** [Chapter__5_THEACCOUNTABILITYGAP__Draft.md:10](manuscript/chapters/Chapter__5_THEACCOUNTABILITYGAP__Draft.md:10), [Chapter__5_THEACCOUNTABILITYGAP__Draft.md:152](manuscript/chapters/Chapter__5_THEACCOUNTABILITYGAP__Draft.md:152), [Chapter__5_THEACCOUNTABILITYGAP__Draft.md:164](manuscript/chapters/Chapter__5_THEACCOUNTABILITYGAP__Draft.md:164)

**Chapter text:**
- Line 10: *"the healthcare system that now routes its shortfalls through crowdfunding campaigns and unpaid caregiving labor during **the most vulnerable stretches of life.**"*
- Line 152: *"because it operates on individual bodies during **the most vulnerable stretches of life,** and because the costs it severs are not abstract externalities but the specific financial ruin of specific households."*
- Line 164: *"The cost-severance the framework names is operating on individual bodies during **the most vulnerable stretches of human life,** and the costs it severs are not abstract externalities but the specific financial ruin and unpaid labor of specific households."*

**Why this flags.** Three near-verbatim repetitions of *"the most vulnerable stretches of [human] life"* — at the chapter opening (line 10), the Healthcare Commons section opening (line 152), and the Healthcare Commons section close (line 164). The repetition between lines 152 and 164 is the most-visible: it bookends the healthcare section with the same phrase. The line 10 instance is the chapter-opening roadmap and can be read as the chapter's introducing the phrase for later use; the lines 152 + 164 bookend pattern is the trade-press editor's most-likely flag.

**Severity rationale.** (a) Three-instance phrase repetition within one chapter; (b) the 152 + 164 bookend is the most-visible cluster; (c) the phrase is substantive (the chapter's framing of healthcare cost-severance hinges on the vulnerability-at-end-of-life dimension) so cuts should preserve the framing.

**Recommended rewrite (apply verbatim at Phase C-β):**

Author selects one approach. Recommended: **Option B** (preserve line 10 + 152; revise line 164 to vary the bookend).

- **Option A — preserve line 152 verbatim; revise lines 10 + 164.** Heavier touch.
- **Option B — preserve lines 10 + 152; revise line 164 to vary the closing.** (RECOMMENDED) The line 10 instance roadmaps the chapter's structure; the line 152 instance opens the section; the line 164 instance closes the section. Revising the closer breaks the 152→164 verbatim bookend without disrupting either of the structural-cue uses.

  Line 164, replace:
  > "The cost-severance the framework names is operating on individual bodies during the most vulnerable stretches of human life, and the costs it severs are not abstract externalities but the specific financial ruin and unpaid labor of specific households."

  with:
  > "The cost-severance the framework names is operating on individual bodies at the points in life where they are least able to refuse the transfer, and the costs it severs are not abstract externalities but the specific financial ruin and unpaid labor of specific households."

- **Option C — preserve line 10; revise both lines 152 + 164.** Surgical. Replace each healthcare-section instance with a different vulnerability-framing. Heavier than necessary.

---

### F-V14 — Close repetition: "the framework's accounting" at line 50 [MEDIUM]

**Negative-finding note:** A surface-read of line 32's Libby-legal-architecture paragraph close — *"Libby's full record is the cost severance the framework's accounting names; the criminal acquittal is evidence that the existing legal architecture was not built to recognize the mechanism the framework prices"* — caught what looked like a similar near-repetition (*"the framework's accounting"* + *"the framework prices"*). Closer read resolves: the two phrasings do different work (*accounting names* vs *framework prices*) and the sentence's chiastic structure earns both. Hold line 32 as-is; the line-50 instance below is the genuine finding.

**Location:** [Chapter__5_THEACCOUNTABILITYGAP__Draft.md:50](manuscript/chapters/Chapter__5_THEACCOUNTABILITYGAP__Draft.md:50) (final sentence of the international-asymmetry paragraph)

**Chapter text:**
> "The international architectural-asymmetry is not a bug of **the framework's accounting** — it is a feature **the framework's accounting** makes visible."

**Why this flags.** *"The framework's accounting"* used twice within fourteen words. The first usage names the thing the asymmetry is not a bug of; the second names the thing the asymmetry is a feature of. The rhetorical move is the standard *"not X, but Y"* construction — substantive — but the verbatim repetition of *"the framework's accounting"* on both sides makes the cadence visible as repetition rather than as the chiastic move it's reaching for.

**Severity rationale.** (a) Visible verbatim phrase-repetition within one sentence; (b) the rhetorical move is good; the phrasing can be tightened.

**Recommended rewrite (apply verbatim at Phase C-β):**
> "The international architectural-asymmetry is not a bug of the framework's accounting — it is a feature the accounting makes visible."

(Drop *"framework's"* from the second instance; *"the accounting"* with definite article carries the reference back to *"the framework's accounting"* in the same sentence. Minimum disruption; preserves the chiastic move; eliminates the verbatim repetition.)

---

### F-V15 — Em-dash density in single sentence at line 210 (post-Phase-C-α TA cross-reference) [MEDIUM]

**Location:** [Chapter__5_THEACCOUNTABILITYGAP__Draft.md:210](manuscript/chapters/Chapter__5_THEACCOUNTABILITYGAP__Draft.md:210)

**Chapter text (post-Phase-C-α MEDIUM-1A + N-1 + MEDIUM-5 integrated forward-pointer):**
> "The methodology this book has been demonstrating runs in one direction. Each case study — McDowell's coal, Norway's oil, the Macondo well, Libby vermiculite, Baotou's tailings — has been priced forward. **The framework's apparatus — the four gates and the three ways of counting (Technical Appendix §5.5 develops both directions of the apparatus formally; Chapter 6 develops each) — does that work.**"

**Why this flags.** The third sentence carries an em-dash-bracketed appositive that itself contains a semicolon-separated parenthetical. The construction is *"The framework's apparatus — [appositive with embedded parenthetical] — does that work"*. The embedded parenthetical breaks reader-flow between *"three ways of counting"* and the cross-reference content; the cross-reference is structurally heavy for memoir-adjacent register. Phase C-α applied this construction verbatim (per the no-improvise directive); Pass 2 evaluates whether the construction can be tightened without losing the cross-reference work.

The cross-reference grammatical-role check (per `feedback_grammatical_role_cross_references.md`): *"Technical Appendix §5.5"* and *"Chapter 6"* are parenthetical citations / "see X" constructions, so the name + § / name format is correct under that discipline. The issue is sentence-shape, not grammatical-role.

**Severity rationale.** (a) Single-sentence em-dash density (one pair) + embedded semicolon-bound parenthetical reads as structurally heavy; (b) the cross-reference work is load-bearing (TA §5.5 + Chapter 6 forward-pointers); (c) sentence-shape can be tightened without losing the cross-reference work.

**Recommended rewrite (apply verbatim at Phase C-β):**

Author selects one approach.

- **Option A — split the sentence in two.** (RECOMMENDED — preserves the cross-references at full strength; removes the em-dash-pair-with-embedded-parenthetical structure.)

  Replace:
  > "The framework's apparatus — the four gates and the three ways of counting (Technical Appendix §5.5 develops both directions of the apparatus formally; Chapter 6 develops each) — does that work."

  with:
  > "The framework's apparatus — the four gates and the three ways of counting — does that work. The Technical Appendix §5.5 develops both directions formally; Chapter 6 develops each."

  Drops the embedded parenthetical; restores reader-flow through the main sentence; the cross-references land cleanly in a follow-up sentence.

- **Option B — convert the embedded parenthetical to a follow-up clause.**

  Replace:
  > "The framework's apparatus — the four gates and the three ways of counting (Technical Appendix §5.5 develops both directions of the apparatus formally; Chapter 6 develops each) — does that work."

  with:
  > "The framework's apparatus — the four gates and the three ways of counting — does that work, with the formal development carried in the Technical Appendix §5.5 (both directions) and in Chapter 6 (each apparatus piece)."

  Single-sentence; preserves the embedded forward-pointer; less crisp than Option A.

- **Option C — hold as-is.** Defensible as substantive integration of the methodology-forward-pointer with the methodology-substance claim. Author judgment.

---

### F-V16 — Parallel-paragraph chiasmus density at line 214 (atmosphere + freedom) [MEDIUM]

**Location:** [Chapter__5_THEACCOUNTABILITYGAP__Draft.md:214](manuscript/chapters/Chapter__5_THEACCOUNTABILITYGAP__Draft.md:214)

**Chapter text:**
> "In later chapters we will walk through a theoretical use case of **the abundance of clean air being stripped — by an off world colony on Mars engineering its own atmosphere, by a climate crisis on Earth — costs of atmospheric services become visible that the abundance had masked.** The framework gates and triangulates them. This is the forward case. When **the abundance of freedom is stripped — by slavery, by forced labor, by the variants of coercion that have organized large parts of human history — costs of the autonomy commons become visible that the abundance had masked.** The framework's apparatus reaches these costs too. They yield to the same four gates. They triangulate through the same three methods, applied backward: substitution cost becomes remediation cost; revealed restraint becomes revealed restitution; forward option value becomes the option value extinguished at the time of past extraction, evaluable from what we know now."

**Why this flags.** Two adjacent paragraphs share near-identical syntactic structure: *"the abundance of X being/is stripped — by Y [, by Z [, by W]] — costs of [W] become visible that the abundance had masked."* The parallel structure is rhetorically deliberate (the forward-direction air case mirrored by the backward-direction freedom case is the load-bearing methodological-symmetry claim). But the verbatim *"costs of [X] become visible that the abundance had masked"* construction repeats across both paragraphs; cumulatively the structure reads as cadence-heavy on a careful read.

The substantive payoff at the close — *"substitution cost becomes remediation cost; revealed restraint becomes revealed restitution; forward option value becomes the option value extinguished at the time of past extraction"* — is a triple-method-translation in serial that further densifies the cadence in the same paragraph.

**Severity rationale.** (a) The parallel-paragraph mirroring is substantively load-bearing (forward-vs-backward methodology symmetry); (b) but the verbatim *"costs of X become visible that the abundance had masked"* repetition makes the cadence visible as cadence rather than as the methodological-symmetry claim it's enacting; (c) author judgment on whether the rhetorical force of the parallel earns the cadence-density.

**Recommended rewrite (apply verbatim at Phase C-β):**

Author selects one approach. The MEDIUM severity reflects that this is closer to style preference than to a stopping issue; hold-as-is is defensible.

- **Option A — vary the verb in the second paragraph's mirror sentence.** Minimum touch.

  Replace, in the second paragraph:
  > "When the abundance of freedom is stripped — by slavery, by forced labor, by the variants of coercion that have organized large parts of human history — **costs of the autonomy commons become visible that the abundance had masked.**"

  with:
  > "When the abundance of freedom is stripped — by slavery, by forced labor, by the variants of coercion that have organized large parts of human history — the costs of the autonomy commons surface that the abundance had hidden."

  Single-word swaps: *"become visible"* → *"surface"*; *"masked"* → *"hidden"*. Preserves the parallel structure but breaks the verbatim cadence-repeat.

- **Option B — restructure the second paragraph's opening to break the parallel construction entirely.** Heavier rewrite.

  Replace:
  > "When the abundance of freedom is stripped — by slavery, by forced labor, by the variants of coercion that have organized large parts of human history — costs of the autonomy commons become visible that the abundance had masked. The framework's apparatus reaches these costs too."

  with:
  > "The same move runs in reverse for the autonomy commons. When abundance of freedom is stripped — by slavery, by forced labor, by the variants of coercion that have organized large parts of human history — the framework's apparatus reaches the costs the abundance had hidden."

  Drops the verbatim cadence-mirror; preserves the substantive methodological-symmetry claim.

- **Option C — hold as-is.** The parallel construction is the methodological-symmetry-of-direction claim's rhetorical enactment. Author judgment.

---

## §7. Findings — LOW (style preferences / hold-as-is default)

Patterns that are style preferences rather than stoppers. Author discretion; default recommendation is hold-as-is across the LOW set unless author opts otherwise.

### F-V17 — Opening declarative-three at line 12 (LOW)

**Location:** [Chapter__5_THEACCOUNTABILITYGAP__Draft.md:12](manuscript/chapters/Chapter__5_THEACCOUNTABILITYGAP__Draft.md:12)

> "Each case tells the same story. The arithmetic is different. The mechanism is identical."

Three declaratives with sentence-length uniformity in the second pair. Substantively the cadence works as opener punch — naming the chapter's structural claim (cases vary; mechanism doesn't) in three crisp sentences. Defensible as deliberate chapter-opening rhetorical move.

**Recommended action:** Hold as-is.

---

### F-V18 — Anaphoric "It knew that X" triplet at line 22 (LOW)

**Location:** [Chapter__5_THEACCOUNTABILITYGAP__Draft.md:22](manuscript/chapters/Chapter__5_THEACCOUNTABILITYGAP__Draft.md:22)

> "**It knew that** its workers were developing lung disease at rates that defied statistical explanation. **It knew that** the families of workers, exposed to dust carried home on clothing, were developing mesothelioma and asbestosis. **It knew that** children who played near the mine's waste piles were inhaling fibers that would kill them decades later."

Anaphoric *"It knew that X"* triplet. The named tidy-parallel pattern, but rhetorically earned: the cumulative-knowledge claim across three levels of victim (workers / workers' families / children) is the load-bearing fact-finding the entire Libby section rests on. The repetition enacts the cumulative-knowledge case.

**Recommended action:** Hold as-is.

---

### F-V19 — Triple-archetype anaphora at line 58 (rare-earth uses) (LOW)

**Location:** [Chapter__5_THEACCOUNTABILITYGAP__Draft.md:58](manuscript/chapters/Chapter__5_THEACCOUNTABILITYGAP__Draft.md:58)

> "**The rare earths in your phone came from Baotou. The rare earths in the wind turbine that generated the electricity you used today came from Baotou. The rare earths in the electric vehicle that represents our best current plan for decarbonizing transportation came from Baotou.**"

Anaphoric three-times structure naming three consumer-side use cases. Each sentence carries different substantive content (phone / wind turbine / EV); each enumerates a different sector dependent on Baotou. Substantively a roadmap; rhetorically earned.

**Recommended action:** Hold as-is.

---

### F-V20 — Triple-archetype anaphora at line 70 (consumer-end actors) (LOW)

**Location:** [Chapter__5_THEACCOUNTABILITYGAP__Draft.md:70](manuscript/chapters/Chapter__5_THEACCOUNTABILITYGAP__Draft.md:70)

> "the consumer at the other end of the supply chain — **the engineer in California with the smartphone in their pocket; the driver in Norway with the electric vehicle on the highway; the family in Berlin with the wind-generated electricity in their home** — is not a villain in this account."

Three consumer-archetype enumerations inside an em-dash-bracketed appositive. Each archetype names a different country + a different use case + a different family-or-individual scale. Substantively the structural-participant-not-villain framing the entire paragraph develops; rhetorically earned.

**Recommended action:** Hold as-is.

---

### F-V21 — Triple-negation-then-affirmation at line 180 (LOW)

**Location:** [Chapter__5_THEACCOUNTABILITYGAP__Draft.md:180](manuscript/chapters/Chapter__5_THEACCOUNTABILITYGAP__Draft.md:180)

> "Cost severance is not an accident. It is not an unintended consequence. It is the mechanism by which every extractive economy has ever operated, and it is still operating today."

Three declaratives with negation-negation-affirmation cadence — the named pattern. Rhetorically the triplet does load-bearing work (defining cost severance by saying twice what it is not, then naming what it is). The structure parallels Ch 1's F-V14 finding (line 103: *"It does not undo it. It is not a redemption mechanism. It is an honest accounting."*) — both substantively-earned framework-defining moments.

**Recommended action:** Hold as-is.

---

### F-V22 — Triple "X do this" bond-marshaling anaphora at line 192 (LOW)

**Location:** [Chapter__5_THEACCOUNTABILITYGAP__Draft.md:192](manuscript/chapters/Chapter__5_THEACCOUNTABILITYGAP__Draft.md:192)

> "**The reclamation bonds mining companies post under the Surface Mining Control and Reclamation Act do this. The decommissioning bonds oil-and-gas operators post against well closure do this. The sovereign wealth fund Norway built against its petroleum extraction does this on a national scale.**"

Three sentences with *"X do this"* anaphoric structure marshalling three established-instrument examples in support of the bond-vocabulary defense. The anaphora is methodology-defense load-bearing — the chapter's bond-naming argument depends on showing the convergent instrument-pattern across regulatory regimes. Substantively earned.

**Recommended action:** Hold as-is.

---

### F-V23 — CSD acronym usage at line 196 (LOW)

**Location:** [Chapter__5_THEACCOUNTABILITYGAP__Draft.md:196](manuscript/chapters/Chapter__5_THEACCOUNTABILITYGAP__Draft.md:196)

> "The framework's **CSD (Cost Severance Damages)** instrument is a structural extension of Coates's argument-architecture into extraction-community contexts: name the specific extraction mechanism (cost severance), name the specific harm (the documented life-expectancy gap, the institutional collapse, the cumulative health-care costs externalized to families and Medicare), name the specific debt (**CSD** as backward-looking accounting)."

CSD appears twice within one paragraph: first with parenthetical expansion (introduction), then as bare acronym at the same paragraph's close. Per the Sandel hybrid pattern (single-use → expand; dense intra-paragraph → keep): both uses are within the same paragraph, so the hybrid pattern supports keeping the second instance as CSD. The treatment is also discipline-aligned with the chapter's named-flagship-term register (the full-form expansion at first use carries the substantive content; the second use is intra-paragraph-dense and the acronym is acceptable).

**Recommended action:** Hold as-is. (Pass 3 audience-load may revisit if it tests CSD-acronym-tolerance against the trade-press-editor pressure-test set; not a Pass-2 stopper.)

---

## §8. Memoir-register / tense / apparatus / named-subject checks

Per the Pass-2 inventory's last few categories.

### §8.1 Register consistency — ✓ HOLDS

Voice is analytical-essay register throughout. The chapter uses third-person analytical voice (cases described from outside; framework introduced as method-instrument); counter-argument paragraphs adopt structured *"A reader will object… The serious version… The framework's response is…"* form; closing-section synthesis remains analytical. No first-person memoir intrusion observed; no register-break between case-study sections and counter-argument paragraphs. (Note: line 86's F-V1 inverted-sentence is logic-coherence, not register-break.)

### §8.2 Tense-consistency — ✓ HOLDS

Past-tense for case events (Libby 1963–1990; Deepwater Horizon April 2010; 2008 crisis); present-tense for ongoing-state claims (Baotou's costs accumulate; Social Security's depletion projection; the GoFundMe pattern); future-tense for explicit projections (line 188 *"the harm not yet done"*). All shifts are content-cued and clean. No tense-leakage observed.

### §8.3 Apparatus residue — ⚠ ONE FINDING (F-V10 at line 50)

Per F-V10 above: *"B postings"* at line 50 is residual apparatus shorthand for *"Bond postings"*. Otherwise the chapter is apparatus-clean:

- No Greek letters, subscripts, or integrals in body prose.
- Named-flagship terms appear in full forms: *"Cost Severance"*, *"Residual Commons Value"*, *"Restitution Bond"*, *"Foreclosure Bond"*, *"accountability bond"*, *"four gates"*, *"three ways of counting"*, *"Commons Inversion Test"*, *"Hotelling Identity"*, *"Cost Severance Damages"* (with CSD acronym at line 196 per F-V23 hybrid-pattern).
- Cross-references to the Technical Appendix follow grammatical-role discipline correctly: *"Technical Appendix §5.5"* + *"§1.10"* are sections-as-citation parentheticals (name + § format; per `feedback_grammatical_role_cross_references.md`). Standard non-apparatus acronyms appearing in body prose: NASA, TARP, GAO, CBO, EPA, BP, NOAA, MBS, CDO, FMLA, GDP, CFPB, ESG. All standard; trade-press tolerable.

### §8.4 Hedge phrases — ✓ NONE

No *"I will argue that…"* / *"It seems likely that…"* / *"Perhaps…"* patterns. The chapter speaks declaratively throughout, including in the counter-argument paragraphs (which adopt *"The serious version is…"* / *"The framework's response is…"* — analytical-rebuttal phrasings, not hedges).

### §8.5 Connective-tissue clichés — ✓ NONE

No *"in short"* / *"ultimately"* / *"moreover"* / *"furthermore"* / *"that being said"* patterns. The chapter manages transitions through case-section breaks + counter-argument anchoring phrases + framework-vocabulary cross-references rather than connective-tissue clichés.

### §8.6 Expository flatness — ✓ NONE

No *"The plain definition is this:"* / *"Here is what I think:"* / *"The argument is simple:"* patterns. The chapter's expository moments (line 188 two-temporal-faces framing; line 192 bond-vocabulary defense; line 210 forward-methodology summary; line 224 reverse-methodology summary) are integrated into analytical register rather than flagged with expository-frame phrases.

### §8.7 Named-subject register — ✓ HOLDS

**Corporate entities (named without consent issue):** W.R. Grace; British Petroleum; Federal Reserve; specific Chinese state-owned enterprises (unnamed at company level — *"a mix of Chinese state-owned enterprises and private firms"*). Standard public-record naming.

**Public-figure academics + authors (named per public-record exception):** Katy Butler (memoir/journalism on-record); Atul Gawande (*Being Mortal* on-record); Brett Christophers (*The Price is Wrong* on-record); William Darity Jr.; A. Kirsten Mullen; Hamilton (*Umbrellas*); Price; Sridharan; Tippett; Dalton Conley; Katharina Pistor; Ta-Nehisi Coates; Lawrence Mishel; Josh Bivens; Jacob Hacker; Philip Pettit; Quentin Skinner; Derek Parfit. All on-record public/academic figures; Pass-1 disposition holds.

**Private-figure references handled through anonymization:** *"Butler's father"* (named only via her published work's framing); *"her eighty-year-old mother"* (likewise); *"Mexican fishermen"* / *"Yucatán-Peninsula coastlines"* (placenames, not named individuals); *"the engineer in California"* / *"the driver in Norway"* / *"the family in Berlin"* (consumer-archetypes, deliberately anonymized).

**Personal-communication citation:** *"informed by Darity, personal communication, May 2026"* at line 220 — Sandy is a project collaborator and the citation attribution is on-record per project context.

No consent regressions or named-subject discipline breaks observed in Pass 2.

---

## §9. Out-of-scope-for-Pass-2 — flagged for Pass 3 (audience-load) future-session input

Items that crossed Pass-2 attention during paragraph-by-paragraph read; flagged here so the Pass-3 (audience-load) session has them ready. **Not scored as Pass-2 findings.**

- **Line 32 — long Libby legal-architecture paragraph.** The paragraph runs ~280 words single-sentence-dense with legal-analytical claims about the 2009 acquittal + criminal-law-architectural-limits. Pass 3 should test how the paragraph lands for Tier-1 trade-press-editor (does the legal-analytical density survive the trade-press-editor pressure-test against the chapter's broader register?) and for Tier-1 layman-policy-reader (is the criminal-law-vs-structural-mechanism distinction legible without prior legal-architecture context?).

- **Lines 86–94 — four-fold counter-argument structure.** The 2008 section's four counter-argument paragraphs (line 86 borrower-agency / line 88 global-crisis / line 90 TARP-repaid / line 92 Dodd-Frank-reform) follow rigid *"A [first/second/third/most-reformist] reader will object… The serious version… The framework's response is…"* form. Pass 3 should test whether the structural rigor reads as careful argumentation (lands for academic / specialist reader) or as repetitive cadence (potentially flags for trade-press-editor pressure-test). The same structural-rigor question applies to lines 126–144's two-fold counter-argument cluster in the Social Security section.

- **Lines 126–144 — Social Security counter-argument depth.** Two counter-arguments (public-finance-prudence at 128–136; timeline-and-tractability at 138–144) developed at trade-comp-shelf depth. Pass 3 should test whether the depth reads as Sandy-target-audience-appropriate or as over-elaborated for the trade-press-editor pressure-test.

- **Lines 184–230 — Restitution-and-Foreclosure section.** Newly-added section (Pass 1's load-bearing audit target). Pass 3 should test how the academic-and-legal lineage prose (Coates / Darity-Mullen / Hamilton / Conley / Pistor / Pettit / Skinner / Parfit) lands across Tier-1 + Tier-2 + Tier-3 audience characters. Particular attention: line 194 Restitution-vs-Reparations vocabulary-asymmetry passage (does it land for a Black-Studies-resonance reader as honest lineage-attribution or as appropriative-vocabulary-claim?); line 218 Darity-Mullen vocabulary-note (does it land for a reparations-economics-specialist reader as faithful intellectual-history?).

- **Section-break rhythm.** Seven section-headed sections (Libby / Deepwater / Baotou / 2008 / Social Security / Healthcare / Pattern Made Visible + Restitution-and-Foreclosure subsection) in a ~9,500-word chapter. Pass 3 should test whether the break-rhythm supports or undermines cumulative reader-load through the chapter.

- **Line 196 CSD acronym.** Pass-2 hybrid-pattern hold-as-is; Pass 3 should re-test against the trade-press-editor + Tier-1 layman-reader audience characters.

- **Black Lung Trust Fund figures at line 226.** Pass 1 N-4 flagged the *"$4.5B in debt"* as stale (current ~$6.5B); deferred to copyedit. Pass 3 input: does the stale figure interact with audience-load (likely no — it's pre-publication-refresh territory).

---

## §10. Out-of-scope-for-Pass-2 — flagged for Pass 1 fact-check follow-up

Items that surfaced during Pass-2 reading but belong to Pass-1's fact-check scope (or to consistency-check / Pass 4 of the audit-existing-prose mode).

- **F-V1 (line 86 inverted information-asymmetry sentence).** Surfaced in Pass 2 as MUST-FIX consistency-coherence; if Phase C-β prefers to confirm the substantive direction against Pass-1 canonical sources before applying, the confirmation is trivial (read the preceding 100 words of the same paragraph). The fix recommendation is included above at F-V1 and is low-risk single-word swap.

- **Line 226 "forty-four billion dollars across half a century" for the Black Lung Trust Fund total payout.** Pass 1 did not flag this figure; Pass-2 surface-read noted it without independent verification. The $44B-cumulative-payout claim is plausible-magnitude-defensible per CRS R45261 (which Pass 1 §B.2 cited for the $4.5B debt figure), but Pass-2 cannot verify against canonical sources within its scope. Recommend Pass-1 follow-up disposition if author opts for pre-send verification; otherwise defer to pre-publication copyedit refresh.

Otherwise no new factual concerns surfaced during Pass-2 reading. Pass 1 + Phase C-α spot-fixes cover the externally-verifiable claim set comprehensively.

---

## §11. Verdict synthesis

### §11.1 Findings tally

| Severity | Count | Findings |
|---|---|---|
| **MUST-FIX** | 5 | F-V1 (line 86 inverted info-asymmetry); F-V2 (line 122 missing "a" before Ponzi); F-V3 (line 82 "larger than Ohio" antecedent broken); F-V4 (line 138 "2034" residual); F-V5 (lines 116–124 prose-flow tightening around line-112 opportunity-cost reframe) |
| **SHOULD-FIX** | 5 | F-V6 (line 46 duplicate "estimated"); F-V7 (line 46 CBO $150B hedge — Pass-1 MEDIUM-1 folded in); F-V8 (line 82 "$16T at peak" cumulative reframe — Pass-1 N-5 folded in); F-V9 (line 220 near-duplicate "framework reaches coerced cases"); F-V10 (line 50 "B postings" apparatus residue) |
| **MEDIUM** | 6 | F-V11 (line 156 "significantly less" repetition); F-V12 (line 214 "off world" hyphenation); F-V13 (3-instance "most vulnerable stretches of life" phrase repetition at lines 10/152/164); F-V14 (line 50 "the framework's accounting" close repetition); F-V15 (line 210 em-dash density at TA cross-reference); F-V16 (line 214 parallel-paragraph chiasmus density) |
| **LOW** | 7 | F-V17 (line 12 declarative-three opener); F-V18 (line 22 "It knew that" triplet); F-V19 (line 58 rare-earth triplet); F-V20 (line 70 consumer-archetype triplet); F-V21 (line 180 triple-negation-then-affirmation); F-V22 (line 192 bond-marshaling triplet); F-V23 (line 196 CSD hybrid-pattern usage) |

**Total findings:** 23 (5 MUST-FIX + 5 SHOULD-FIX + 6 MEDIUM + 7 LOW).

### §11.2 Aggregate Pass-2 verdict

**READY AFTER PHASE C-β SPOT-FIXES.** The chapter's analytical-essay register is fundamentally strong; counter-argument structure is rigorous and load-bearing for Sandy-target-reader engagement; reparations-economics lineage prose at lines 184–230 is intellectually honest and well-attributed. No structural voice revision needed.

The five MUST-FIX findings split into three categories: (a) two clear grammar / writing errors (F-V2 missing "a"; F-V12 hyphenation — F-V12 is MEDIUM not MUST-FIX); (b) one logic-inversion that breaks the surrounding paragraph's argument (F-V1 line 86); (c) two Phase-C-α residuals where prior spot-fixes scoped Pass-2 follow-up correctly (F-V3 line 82 "larger than Ohio" antecedent; F-V4 line 138 internal-consistency residual; F-V5 lines 116–124 conceptual-coherence tightening). All five are isolated and spot-fixable.

The five SHOULD-FIX findings absorb the remaining Phase-C-α-scoped follow-up items (F-V6 duplicate "estimated"; F-V9 line 220 near-duplicate phrasing) + the two task-brief Pass-1-Tier-2 folded items (F-V7 CBO hedge; F-V8 $16T cumulative reframe) + one apparatus-residue catch (F-V10 line 50 "B postings"). All have low-risk verbatim-apply rewrites.

The six MEDIUM findings cluster around standard voice-polish patterns: phrase-repetition (F-V11, F-V13, F-V14), hyphenation (F-V12), and em-dash / parallel-cadence density (F-V15, F-V16). Author discretion; recommended pre-send but not gating.

The seven LOW findings are all substantively-earned anaphoric / declarative-three / chiastic patterns; hold-as-is is the recommendation across the set.

### §11.3 Phase C-β disposition recommendation

Recommended Phase C-β sequencing:

1. **Apply all 5 MUST-FIX findings (F-V1 through F-V5).** All are isolated spot-fixes (single-word, single-character, or one-paragraph scope). F-V5 is the most-effortful (lines 116–124 cluster-tightening); recommend Option B (paragraph-level tightening at 116, 118, 120, 122). F-V5 + F-V3 + F-V4 in particular complete the Phase-C-α work Pass 2 was scoped to finish.

2. **Apply all 5 SHOULD-FIX findings (F-V6 through F-V10).** F-V6 + F-V7 both target line 46; apply F-V6 first then F-V7. F-V3 + F-V8 both target line 82; both are independent within the long paragraph. F-V10 line 50 is a one-word fix. F-V9 line 220 absorbs the Phase-C-α near-duplicate-phrasing flag.

3. **Apply all 6 MEDIUM findings (F-V11 through F-V16).** All are isolated phrase-level edits with low-risk verbatim-apply rewrites except F-V15 (em-dash density at TA cross-reference, where Option A is recommended) and F-V16 (parallel-paragraph chiasmus, where Option A's minimum-touch is recommended). F-V13 multi-instance phrase repetition has Option B recommended (revise line 164 only).

4. **Hold the 7 LOW findings.** All are substantively-earned cadence patterns; the chapter's rhetorical force benefits from holding them. Author may revisit individual items if Pass 3 audience-load surfaces concerns.

Phase C-β estimated scope: ~60–90min for the integrated spot-fix application across 16 edits (MUST + SHOULD + MEDIUM). Single integrated commit per Working Principle #9.

### §11.4 Sandy-send-packet readiness assessment

With Phase C-β applied at MUST-FIX + SHOULD-FIX depth (10 edits), Ch 5 reaches Sandy-Darity-send-packet readiness for the voice-polish dimension alongside the fact-check dimension already cleared by Phase C-α. The MEDIUM findings, applied or not, do not gate the send: they are precision-tightenings that improve trade-press-editor readiness but do not affect Sandy's substantive reading of the chapter. The LOW findings explicitly do not gate.

Pass 3 (audience-load) remains the recommended pre-send rigor pass per per-pass serial cadence; Pass 3's audience-load verdict + final-stage spot-fixes (Phase C-δ) are the last gate before send.

---

## §12. Cross-thread flags

- **Ch 5 cross-chapter consistency inventory** (`tools/audits/cross-chapter-consistency-inventory_2026-05-11.md` §3): No new entries required from Pass 2 findings. The recurring-stat entries Phase C-α added for Social Security depletion year + benefit rate + $108T recategorization + BP-Mexico settlement + 2008 foreclosure measure remain canonical; Pass 2 findings do not introduce new cross-chapter recurring-stat material.

- **Workstream #20 Phase B per-chapter table.** Ch 5 Pass 2 verdict goes into the workstream table: 5 MUST-FIX + 5 SHOULD-FIX + 6 MEDIUM + 7 LOW; READY AFTER PHASE C-β SPOT-FIXES; Sandy-send-packet-readiness-gated by Pass 3 (audience-load).

- **Ch 6 parallel session.** Per Pass 1 §B.7.2, Ch 6 carries the bulk of the residual Darity-synthesis-incorporation gap (MI-3 + SI-1 sharpening + SI-2 + C-3). Ch 5 Pass 2 surfaces no new Ch-6-cross-flags beyond what §B.7 already named.

- **Pass 3 (audience-load) input.** §9 above lists 7 items flagged forward to the Pass-3 session; the Pass-3 session should pick these up as starting input.

- **Endnote sweep (cross-thread #11).** Pass 2 surfaces no new endnote items; Pass-1's 16 Major + 14 Low/Minor inventory remains canonical for Ch 5's #11 contribution.

---

## §13. What this pass did NOT do

Per author's per-pass serial cadence + v2.0 Amendment B distinct-pass discipline:

- **Did NOT re-run Pass 1 (fact-check).** Pass 1 ratified 2026-05-13 + Amendment 1 + Amendment 2 + §B.7 (2026-05-14); Phase C-α applied 2026-05-14 (commit `da26bdc`). Pass-1 findings are not re-litigated. Two incidental Pass-1-territory observations surfaced (F-V1 inverted-sentence at line 86 — consistency-check finding within audit-existing-prose mode; $44B Black Lung total payout at line 226 — verification deferred) and are flagged forward at §10 for Pass-1 disposition if author opts to verify.

- **Did NOT score Pass 3 (audience-load).** Pass 3 is a separate session per the workstream handoff. Pass-2-surfaced audience-load concerns are flagged at §9 for Pass-3 input but are not scored here.

- **Did NOT apply spot-fixes to the chapter file.** Phase C-β (per-chapter spot-fix application session) does that after author ratification.

- **Did NOT re-write paragraphs.** Findings + proposed verbatim revision text + STOP, per the Pass-2 template's hard constraint. (Where multiple options exist — F-V3, F-V5, F-V13, F-V15, F-V16 — each option is presented as fully-formed verbatim text that Phase C-β can apply directly without further drafting.)

- **Did NOT contact named subjects.** Per consent discipline.

- **Did NOT propose new framework concepts or meta-conclusions about the v2.0 discipline.** Per Pass-2 template's hard constraint.

- **Did NOT touch the Technical Appendix, Ch 6, or other chapters.** Per task brief explicit scope.

---

## §14. Hard constraints honored

- ✓ Did NOT apply spot-fixes to `Chapter__5_THEACCOUNTABILITYGAP__Draft.md`.
- ✓ Did NOT re-run Pass 1 (fact-check) — referenced only for context + Phase-C-α-scoped forward-pointers; two incidental observations flagged forward at §10.
- ✓ Did NOT score Pass 3 (audience-load) — concerns flagged forward to that session at §9.
- ✓ Did NOT re-write paragraphs — proposed-revision options offered as verbatim-apply text without applying.
- ✓ Did NOT contact named subjects.
- ✓ Did NOT propose new framework concepts.
- ✓ Did NOT touch Technical Appendix, Ch 6, or other chapters.
- ✓ Verified post-Phase-C-α chapter line count (237 lines, 2026-05-14) and key line anchors (46, 50, 82, 86, 108, 110, 112, 116, 118, 120, 122, 124, 138, 156, 164, 192, 210, 214, 220).
- ✓ Verified worktree HEAD matches origin/main `da26bdc` and that Phase C-α single integrated commit landed per Working Principle #9.
- ✓ Built feature branch `claude/ch5-pass-2-ecstatic-ardinghelli-d9376e` off origin/main per task brief branch discipline.

---

*End of Ch 5 Stage-3 Pass 2 (Voice-Polish) rigor pass — pending author ratification of recommended spot-fixes. Phase C-β applies after ratification (paralleling Ch 1 Pass 2 commit `0b78449` → Phase C-γ commit `fa08c10`). Pass 3 (Audience-load) is a separate session.*

---

## Phase C-β status (2026-05-14)

**Status:** APPLIED. Doc moves from PROPOSED-pending-Phase-C-β to PROPOSED-Phase-C-β-applied. Author ratified "all as recommended" in the parent session before this commit.

### What was applied

All 16 ratified findings (5 MUST-FIX + 5 SHOULD-FIX + 6 MEDIUM) applied as single integrated commit. The 7 LOW findings held as-is per the Pass 2 recommendation.

- **F-V1 (MUST-FIX, line 86 inverted info-asymmetry sentence) — applied.** Single-word swap: subject and object of the *"X had information the Y did not"* clause reversed. Line 86 now reads *"the value-extracting party had information the cost-bearing party did not, and the information structure was structurally adversarial"* — aligned with the surrounding paragraph's argument.
- **F-V2 (MUST-FIX, line 122 missing article before "Ponzi scheme") — applied.** Single-character insertion of *"a"* between *"is not"* and *"Ponzi scheme"*.
- **F-V3 (MUST-FIX, line 82 "larger than Ohio" antecedent break) — Option A applied, then tightened post-verification.** Initial Phase-C-β application: *"— a population larger than Ohio, displaced in under five years."* → *"— more households than there are in the entire state of Pennsylvania, foreclosed in under five years."* Post-verification (Pennsylvania households confirmed at ~5.36M per 2020 Census / 2024 ACS, not ~5.7M as the Pass 2 doc's justification text claimed) the comparison was parse-ambiguous: strict parse (em-dash attaches to 5M completed-foreclosure clause) made the comparison wrong (5M < 5.36M); loose parse (attaches to the 10M filings sentence-subject) made it right (10M > 5.36M). Author-ratified follow-up tightening removes the ambiguity: *"— more households affected than there are in the entire state of Pennsylvania, in under five years."* The single-word swap *"foreclosed"* → *"affected"* attaches the comparison unambiguously to the broader 10M-households-affected scale; math now uncontroversially holds (10M > 5.36M PA).
- **F-V4 (MUST-FIX, line 138 "2034" residual) — applied.** Single-character fix: *"it will run out in 2034"* → *"it will run out in 2033"*. Line 138 now aligned with the post-Phase-C-α OASI pairing at lines 108 + 110.
- **F-V5 (MUST-FIX, lines 116–124 prose-flow tightening) — Option B applied (paragraph-level tightening across 116, 118, 120, 122).** Four sentence-level rewrites applied verbatim per recommendation:
  - Line 116: *"The cost of paying for those promises was severed…"* → *"The foregone-investment cost the Treasury-IOU routing produced was severed…"*
  - Line 118 closing: *"the affected community is every future American taxpayer"* → *"the affected community is the working-class payroll-tax contributors whose surpluses failed to compound, plus every future American taxpayer who will absorb the resulting funding gap"*
  - Line 120: *"The bill was transferred…system that promises more than it can deliver…honoring promises they did not make…"* → *"The foregone compounding was transferred…system whose surpluses were routed through the Treasury-IOU mechanism instead of into productive sovereign capital…absorbing the resulting funding gap themselves…"*
  - Line 122 third sentence: *"One hundred and eight trillion dollars in costs, severed from the generations who created them…"* → *"One hundred and eight trillion dollars in foregone return, extracted from the architecture by the routing choice that earlier generations made and transferred to generations who had no say in making it."*
- **F-V6 (SHOULD-FIX, line 46 duplicate "estimated") — applied.** *"killed an estimated 4 to 8 billion oysters"* → *"killed 4 to 8 billion oysters"*. NOAA attribution at the sentence's head carries the hedge for the entire clause.
- **F-V7 (SHOULD-FIX, line 46 CBO $150B attribution) — applied.** Final sentence of the NOAA paragraph replaced with multi-source aggregate framing per recommended-rewrite text.
- **F-V8 (SHOULD-FIX, line 82 "$16T at peak" cumulative reframe) — applied.** *"exceeded sixteen trillion dollars at peak."* → *"exceeded sixteen trillion dollars in cumulative emergency loans across the crisis (per the GAO's 2011 audit)."* See Judgment Calls below — line 90 carries a second instance Pass 2 missed.
- **F-V9 (SHOULD-FIX, line 220 near-duplicate phrasing) — applied.** Sentence-level reorganization per recommended-rewrite text; load-bearing TA §1.10 forward-pointer + Darity personal-communication attribution preserved at the paragraph's close.
- **F-V10 (SHOULD-FIX, line 50 "B postings" apparatus residue) — applied.** *"structurally different B postings"* → *"structurally different bond postings"*. Aligned with chapter-wide named-flagship-term discipline.
- **F-V11 (MEDIUM, line 156 "significantly less" repetition) — applied.** First instance: *"significantly less"* → *"substantially less"*; second instance preserved.
- **F-V12 (MEDIUM, line 214 "off world" hyphenation) — applied.** *"off world colony"* → *"off-world colony"*. Aligned with line 230's existing *"off-Earth extraction"* usage.
- **F-V13 (MEDIUM, "most vulnerable stretches of life" 3-instance repetition) — Option B applied (revise line 164 only).** Line 164 closing rewritten to vary the bookend phrasing; lines 10 + 152 preserved as structural-cue uses.
- **F-V14 (MEDIUM, line 50 "framework's accounting" close repetition) — applied.** Second instance dropped: *"a feature the framework's accounting makes visible"* → *"a feature the accounting makes visible"*. Definite article carries the reference back.
- **F-V15 (MEDIUM, line 210 em-dash density at TA cross-reference) — Option A applied.** Sentence split into two: the main *"The framework's apparatus — the four gates and the three ways of counting — does that work."* + the follow-up *"The Technical Appendix §5.5 develops both directions formally; Chapter 6 develops each."* Embedded parenthetical eliminated; reader-flow restored.
- **F-V16 (MEDIUM, line 214 parallel-paragraph chiasmus density) — Option A applied (minimum touch).** Second paragraph's mirror sentence varied: *"costs of the autonomy commons become visible that the abundance had masked"* → *"the costs of the autonomy commons surface that the abundance had hidden"*. Parallel structure preserved; verbatim cadence-repeat broken.

### Files touched

- `manuscript/chapters/Chapter__5_THEACCOUNTABILITYGAP__Draft.md` — 19 individual line-level edits across 16 findings, applied verbatim per recommended-rewrite text. Line count preserved at 237 (single-line-per-paragraph format; F-V15's sentence split is contained within line 210). Key line anchors verified post-edit: 46, 50, 82, 86, 90 (see Judgment Calls), 108, 110, 112, 116, 118, 120, 122, 124, 138, 156, 164, 210, 212, 214, 220.
- `tools/audits/cross-chapter-consistency-inventory_2026-05-11.md` — Section 3 entries updated: (a) Fed-emergency-lending row reframed from "at peak" to "cumulative-vs-peak framing" with Ch 5 line 82 post-Phase-C-β citation + DRIFT-FLAGGED note for the unresolved line-90 instance; (b) Social Security OASI depletion-year row updated to list lines 108 + 110 + 138 (all aligned at 2033); (c) Social Security $108T-foregone-investment-opportunity-cost row updated to cite lines 112–124 (Phase C-β surrounding-paragraph tightening) instead of 112–114 only.
- `tools/rigor-passes/commons_bonds_ch5_stage_3_pass_2_voice_polish_2026-05-14_PROPOSED.md` — this Phase C-β status section appended.

### Commit hash

Single integrated commit; hash captured at commit time. See `git log --oneline` for the canonical reference (look for "Ch 5 Phase C-β — Pass 2 voice-polish spot-fixes applied" message).

### Judgment calls / soft observations (not fixes)

- **⚠ Line 90 carries a second "$16T at peak" instance Pass 2 missed.** Phase C-β's F-V8 application at line 82 ("cumulative emergency loans across the crisis (per the GAO's 2011 audit)") has now exposed an internal inconsistency: line 90's third-pushback paragraph still reads *"The Federal Reserve's facilities at peak — the sixteen-trillion-dollar figure that emerged through congressional request — were repaid in nominal terms…"* The "at peak" framing here carries the same N-5 inaccuracy F-V8 corrected at line 82 (peak outstanding was ~$1T; the $16T is cumulative). Per the established Phase-C scope discipline (apply only what was ratified; flag forward for separate ratification), this instance was NOT corrected in Phase C-β. Recommended follow-up spot-fix (for separate ratification): replace *"The Federal Reserve's facilities at peak — the sixteen-trillion-dollar figure that emerged through congressional request — were repaid in nominal terms"* with *"The Federal Reserve's cumulative emergency lending — the sixteen-trillion-dollar figure that emerged through congressional request — was repaid in nominal terms"*. Both Pass 1 and Pass 2 missed this instance; the cross-chapter inventory's prior "Ch 5 line 82 (only)" claim was inaccurate. Pass 3 (audience-load) session should not pick this up; it is a fact-check / consistency-check item belonging to a Pass-1 follow-up.

- **The $44B Black Lung total-payout figure at line 226 was not independently verified during Pass 2.** Pass 2 §10 flagged this for Pass-1 follow-up disposition if author opts for pre-send verification; otherwise defer to pre-publication copyedit refresh. Phase C-β did not touch line 226.

- **The chapter's section-break rhythm + counter-argument paragraph density** were both flagged for Pass 3 (audience-load) at Pass 2 §9. Phase C-β did not modify section-break placement or counter-argument structure.

### What remains for post-send

- **Line 90 "$16T at peak" residual** — separate ratification recommended; small spot-fix (~30sec to apply once ratified).
- **LOW findings (F-V17 through F-V23)** — all held as substantively-earned cadence patterns per Pass 2 recommendation. Author may revisit individual items if Pass 3 audience-load surfaces specific concerns.
- **Pass 3 (audience-load)** — separate workstream; final pre-send rigor pass. Pass 2 §9 listed 7 items as Pass-3-input.
- **Pre-publication copyedit refresh / endnote sweep (cross-thread #11)** — Ch 5 contributes 16 Major + 14 Low/Minor items; separate workstream.
- **Black Lung debt ($4.5B vs current ~$6.5B) + Kenworthy & Igra cite-form (line 154)** — pre-publication-refresh territory; not Phase C-β scope.

### Sandy-send-packet readiness

With Phase C-β applied (16 of 16 ratified Pass-2 findings landed; 7 LOW findings held; 1 line-90 residual flagged for follow-up), Ch 5 reaches Sandy-Darity-send-packet voice-polish readiness alongside the fact-check readiness Phase C-α delivered. The line-90 residual is the only outstanding internal-consistency item; severity is approximately equivalent to the line-138 residual Phase C-α intentionally scoped forward to Pass 2 (single-instance phrase-replacement to align with corrected primary instance). Pass 3 (audience-load) remains the recommended pre-send rigor pass per per-pass serial cadence.

---

*End of Phase C-β status section. Pass 2 PROPOSED doc state: Phase C-β applied. Pass 3 (audience-load) deferred to subsequent session.*
