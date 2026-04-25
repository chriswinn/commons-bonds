# Commons Bonds — Framework-Level Rigor Pass: Three Ways of Counting + RCV Formal-Model Blocks (1–4)

**Version:** 1.0.0
**Date:** 2026-04-24

> **Naming update header (added 2026-04-24 post-ratification per Principle #4 Tier-1 active-doc-update):**
> This pass uses the working labels "Reparations Bond" and "Resource-Foreclosure Bond" for B1 and B2 throughout (~5 references). Per the dedicated B1 + B2 naming rigor pass (commit `8e6a5b2`) ratified 2026-04-24 by Chris Winn, the FINAL ratified sub-instrument names are:
> - **B1 = Restitution Bond** (replaces "Reparations Bond" working label)
> - **B2 = Foreclosure Bond** (replaces "Resource-Foreclosure Bond" working label)
>
> Working labels preserved in the body of this pass for narrative integrity (the pass was written before the naming sub-decision); when reading, mentally substitute final names. Working labels' political-loading concern (B1) and length/redundancy concern (B2) drove the rename per dedicated rigor pass.

**Protocol applied:** `tools/commons_bonds_rigor_protocol_v2.3.0.md` — full 12-module suite + §22 Path Comparison Mode + §22.4 goals alignment + all 6 Working Principles + ratified corollaries.
**Scope:** Tests the four interlocking blocks of the April 19, 2026 RCV formal-model session that have remained "pending review" while terminology rigor work consumed Phase A3 attention. These blocks are the framework's central VALUE-ESTIMATION apparatus (distinct from the Four Gates, which is the ADMISSION apparatus). Per author surfacing of the gap 2026-04-24: *"Run the Three Ways + RCV formal-model rigor pass."*
**Status:** rigor pass executed 2026-04-24; pending author ratification.
**Author:** Chris Winn

**Pass-specific scope notes:**
- This pass operates on FRAMEWORK STRUCTURE level (similar in scale to commons-as-structural-identity reframing pass).
- M12 audit critical: each block has rich prior-art lineage (Hotelling 1931 + reparations-economics + replacement-cost methodology + revealed-preference + real-options theory).
- The pass surfaces a HIDDEN Ring-? framework element: **CSD (Cost Severance Damages)** that has not yet had a Terms Index record despite being structurally load-bearing.

**Cross-references:**
- `alignment/decisions/april-19-rcv-two-instrument-distinction.md` — Block 1 (CSD vs RCV).
- `alignment/decisions/april-19-rcv-triangulated-estimation.md` — Block 2 (Three Methods).
- `alignment/decisions/april-19-rcv-hotelling-identity.md` — Block 3 (Hotelling identity).
- `alignment/decisions/april-19-rcv-validation-strategy.md` — Block 4 (validation strategy).
- Four Gates cluster pass (commit `d188e6f`) — admission apparatus (this pass = estimation apparatus).
- Open Insight #14 — Norway-as-canonical-mitigation-exemplar + epistemic-humility (load-bearing for Block 2 Method 2).

---

## §1. Executive summary

**RECOMMENDED: RATIFY all four blocks (PASS WITH CONDITIONS). Promote three framework elements to formal Ring placement:**

1. **CSD (Cost Severance Damages) — promote to Ring 2** as the framework's backward-looking instrument. Block 1's two-instrument distinction surfaces CSD as a structurally distinct quantity from RCV; CSD has been operating implicitly in the framework but never had a Terms Index record. **This is the pass's most important framework-structure finding.**

2. **Hotelling Identity (RCV − Hotelling rent = CS per unit) — promote to Ring 2** as the framework's clean mathematical bridge to standard resource economics (Hotelling 1931). M6 academic positioning enormously strengthened.

3. **Three Ways of Counting (triangulated estimation methodology) — confirm as Ring-2 estimation apparatus** under the formal name "Triangulated RCV Estimation." Three methods (Replacement Cost lower bound + Norway Revealed Preference middle estimate + Scarcity-Adjusted Option Value upper bound) bracket RCV; convergence/divergence diagnostic is methodologically sound.

**Conditions for ratification:**

A. **CSD-RCV correlation claim flagged for Block 4 validation.** Block 1's "deepest claim" — that CSD and uncaptured RCV are structurally correlated — is empirically testable but unvalidated. Frame as a hypothesis the framework predicts and Block 4's case-study validation is designed to test, not as a settled framework claim.

B. **Method 2 (Norway calibration) requires Open Insight #14 epistemic-humility integration.** Norway is anchor BUT Norway didn't fully capture RCV (per just-ratified epistemic-humility discipline). Method 2's calibration must explicitly note: "Norway's per-barrel capture is a strong middle-estimate ANCHOR but is itself a lower bound on true RCV; method gives a Norway-anchored value that is correct as Norway-bound, conservative as RCV-bound."

C. **Block 3's "identity" claim requires careful framing.** "RCV − Hotelling rent = Cost Severance" is presented as identity (not analogy). This is true at the per-unit definitional level but requires Tech Appendix specification to avoid ambiguity (e.g., RCV is integrated; Hotelling rent is a per-period quantity — they need explicit reconciliation).

D. **Block 2 sensitivity-analysis on σ, α, V_option** (Block 4) needs to be EXECUTED, not just specified. If the framework's RCV estimate is dominated by one parameter (say σ — substitutability), the Tech Appendix should foreground that — the real debate becomes a debate about substitutability, narrowing the framework's contested surface.

**Cross-block integration verdict:** the four blocks form a coherent system. Block 1 (two instruments) defines what's being measured; Block 2 (three methods) measures one of them (RCV); Block 3 (Hotelling) connects to standard economics math; Block 4 (validation) makes the system falsifiable. Together they constitute the framework's central value-estimation apparatus, complementing the Four Gates admission apparatus.

**M12 aggregate verdict:** All four blocks are EXTENSIONS of established economics traditions, NOT original coinage:
- Block 1 extends reparations-economics + resource-economics with a two-instrument framing.
- Block 2 extends established estimation methodologies (replacement-cost + revealed-preference + real-options) with triangulation discipline.
- Block 3 directly connects to Hotelling 1931 — extension via identity claim.
- Block 4 is standard validation methodology adapted to framework cases.

**M12 framework-honesty positioning** (Tech Appendix recommended): *"The framework's contribution is not the individual estimation methods (each established in resource economics) but the integration: a two-instrument framework (CSD + RCV) for distinct moral-economic measurements; a triangulation discipline; a Hotelling-identity bridge to standard resource economics; and a falsifiable validation strategy."* Extension-with-integration claim survives reviewer scrutiny.

---

## §2. The four blocks under test

### §2.1 Block 1 — Two-Instrument Distinction (CSD vs RCV)

**Core claim:** the framework needs two separate measurement instruments:
- **CSD (Cost Severance Damages):** backward-looking; measures realized human harm; reparations-model-grounded; uses VSL + DALY + intergenerational-mobility research.
- **RCV (Residual Commons Value):** forward-looking; measures resource permanent-foreclosure; the harder, more original problem.

**Critical secondary claim:** CSD and uncaptured RCV may be CORRELATED across cases. If communities bearing higher CSD also sit on higher uncaptured RCV, that correlation is structural — the same underlying extraction event measured from different directions.

**Five holes in reparations-only model identified:** counterfactual problem · attribution · demographic branching · unlived-lives infinity · CSD-doesn't-equal-RCV (the critical distinction).

### §2.2 Block 2 — Triangulated RCV Estimation Framework (Three Ways of Counting)

**Core claim:** three independent methods approaching RCV from different directions — convergence → robust; divergence → reveals real disagreements:
- **Method 1 — Replacement Cost** (lower bound): cost to provide same service from next-best substitute.
- **Method 2 — Revealed Preference via Norway Calibration** (middle estimate): Norway sovereign-fund per-barrel value as anchor.
- **Method 3 — Scarcity-Adjusted Option Value** (upper bound): real-options theory at extraction-decision.

### §2.3 Block 3 — Hotelling Identity + Total Extraction Damages

**Core claim:** *RCV − Hotelling rent = Cost Severance per unit.*

This is presented as an IDENTITY (not analogy). Connects framework directly to Hotelling 1931 standard resource-economics math.

**Total extraction damages** = CSD + uncaptured RCV (per-community).

### §2.4 Block 4 — Validation Strategy

**Core claim:** the formal model is falsifiable through specific case-study calibration:
- Norway as calibration anchor (Methods 1 + 3 should bracket Method 2's Norway figure).
- Primary cases: Appalachian coal · Niger Delta · Canadian tar sands.
- Boundary case: Chesapeake fisheries (renewable pushed to non-renewable).
- Cross-domain case: Indigenous land dispossession (enclosure not depletion).
- Sensitivity analysis: σ + α + V_option across plausible ranges.

### §2.5 Options for the rigor pass

- **A — RATIFY all four blocks (PASS WITH CONDITIONS).** **RECOMMENDED.**
- **B — RATIFY Blocks 2-4; defer Block 1's CSD-as-Ring-2.** REJECTED — CSD is structurally already operating; ratifying its Ring placement makes the framework's two-instrument architecture explicit.
- **C — RATIFY Blocks 1+2+4; defer Block 3 (Hotelling Identity).** REJECTED — Hotelling Identity is the strongest M6 academic positioning move; deferring forfeits academic-credibility upside.
- **D — REJECT (return to current implicit handling).** REJECTED — "pending review" status for 5 days has masked critical framework structure.

### §2.6 Sub-claims for Option A

- SC-A1: CSD is structurally distinct from RCV (Block 1) and warrants Ring-2 status.
- SC-A2: Three Methods bracket RCV reliably (Block 2).
- SC-A3: Hotelling Identity holds at the per-unit definitional level (Block 3).
- SC-A4: Validation strategy is sufficiently falsifiable (Block 4).
- SC-A5: All four blocks pass M12 with extension-of-established-economics positioning.
- SC-A6: Cross-block integration is coherent — distinct framework layers (instruments + methods + bridge + validation).

### §2.7 Falsifiers

**Option A falsified if:**
- Hotelling Identity proves not to hold (analogy not identity) under Tech Appendix specification.
- Three-method triangulation produces wildly divergent estimates on test cases (Block 4 sensitivity-analysis when executed).
- CSD-RCV correlation claim proves empirically false (Block 4 validation when executed).
- M12 audit reveals framework is closer to adoption-of-Hotelling than extension-of-Hotelling.

---

## §3. Block 1 rigor — CSD vs RCV Two-Instrument Distinction

### §3.1 Structural soundness

The two-instrument distinction surfaces a real architectural feature of the framework that has been operating implicitly. Let me name the implicit operation:

- When the framework discusses McDowell County's Black Lung healthcare costs, life-expectancy gap, community collapse — that's CSD (human harm, backward-looking).
- When the framework discusses the coal extracted from the mountains being permanently gone, foreclosing future uses — that's RCV (resource permanent-foreclosure, forward-looking).
- The framework has been treating both under the umbrella of "cost severance" but the two measurements ARE distinct.

**Verdict:** Block 1's two-instrument distinction makes explicit what was implicit. Strong PASS.

### §3.2 Principle #3 distinctness check

**Test:** Are CSD and uncaptured RCV the same thing measured differently, or genuinely distinct?

Block 1's Hole 5 establishes the answer: distinct.

> *"You could fully compensate every descendant of every Appalachian coal miner — make them whole on health, education, housing, income — and the coal is still gone. The resource is still permanently foreclosed."*

CSD and RCV are orthogonal — they measure different aspects of the extraction event:
- CSD: damage done to people (compensable in principle via reparations)
- RCV: damage done to resource (NOT compensable via reparations — the resource is gone)

**Verdict:** Genuinely distinct. PASSES Principle #3 distinctness.

### §3.3 The correlation claim (deepest claim)

> *"If CSD and uncaptured RCV are correlated across cases — if communities bearing higher severed costs also sit on top of higher permanently foreclosed resource value — that would be a genuinely important empirical finding."*

Status: **empirically testable but unvalidated.** Block 4's validation strategy is designed to test this.

Recommended framing in Tech Appendix:
> *"The framework predicts CSD and uncaptured RCV will correlate across extraction cases — the same underlying extraction event measured from different directions. This is a hypothesis the framework's case-study record should test. Strong correlation would be the framework's deepest empirical claim; weak correlation would weaken the two-instrument architecture; no correlation would force reconsideration of whether CSD and RCV are independent measurements after all."*

This is a falsifiable empirical prediction the framework makes. M11 critic survives strongly.

### §3.4 CSD as framework element (Ring-? promotion question)

**Surfaced finding: CSD has been operating in the framework without a Terms Index record.**

Examples of implicit CSD operation:
- McDowell County 13-year life-expectancy gap (CSD measurement).
- Healthcare-end-of-life family-caregiver labor-time (CSD measurement).
- Opioid Appalachia 141/100K overdose deaths (CSD measurement).
- 2008 financial crisis 10M home foreclosures (CSD measurement).

These have been treated under "cost severance" + "Cᵢ admitted via Four Gates" — but they're more specifically CSD measurements (backward-looking realized human harm).

**Recommended Ring placement:** **Ring 2** (internal load-bearing). CSD is the backward-looking instrument; RCV is forward-looking. Both Ring-1 status would dilute the adoption-bet focus on Severed Cost + Cost Severance + Commons Bonds. Both Ring 2 with Tech Appendix formalism is the right scope.

### §3.5 Verdict on Block 1

PASSES. Two-instrument distinction is structurally important, makes implicit operation explicit, and surfaces CSD as a hidden Ring-2 framework element warranting promotion via this pass.

---

## §4. Block 2 rigor — Triangulated RCV Estimation (Three Ways)

### §4.1 Method 1 (Replacement Cost) — lower bound

**Test:** Does replacement cost actually provide a lower bound for RCV?

YES. Replacement cost captures the substitutable component of RCV. Non-substitutable component (irreplaceable geological functions, future-uses-not-yet-invented) isn't priced. So replacement cost ≤ RCV. PASSES.

**Boundary check (per Block 2):** Sand → low replacement-cost gap → low RCV. Helium → effectively-infinite replacement-cost → very high RCV. The method differentiates appropriately. PASSES.

### §4.2 Method 2 (Norway Calibration) — middle estimate

**Test:** Is Norway's per-barrel capture a defensible middle-estimate anchor?

**Per Open Insight #14 (just ratified):** Norway is the canonical existing real-world exemplar of B (Accountability Bond) approaching RCV — but Norway didn't fully capture RCV. So Norway's per-barrel value is itself a LOWER BOUND on true RCV, not a middle estimate.

This raises a question for Block 2: should Method 2 be reframed as a *floor* (what one country actually accomplished) rather than a *middle estimate*?

**Reconciliation:** Method 2 functions as a middle estimate WITHIN the triangulation framework because:
- Method 1 (replacement cost) is a STRICTER lower bound (only substitutable component).
- Method 2 (Norway) captures a broader claim than Method 1 because Norway internalized more than substitutable replacement cost.
- Method 3 (option value) is theoretical upper bound.

So within the triangulation: Method 1 ≤ Method 2 ≤ Method 3 ≤ true RCV (approximately). All three are actually lower bounds on RCV; their convergence/divergence reveals where uncertainty lives.

**Refinement recommended:** Tech Appendix should clarify that Method 2 is a "REVEALED-PREFERENCE-ANCHORED MIDDLE ESTIMATE bounded above by Method 3 and below by Method 1" — not a true middle of true RCV but a structurally-positioned middle within the triangulation.

This integrates Open Insight #14's epistemic humility cleanly.

### §4.3 Method 3 (Scarcity-Adjusted Option Value) — upper bound

**Test:** Does scarcity-adjusted option value provide an upper bound for RCV?

This requires more specification than Block 2 provides. Real-options theory (Dixit-Pindyck 1994) values the option to delay extraction; the "scarcity-adjusted" framing modifies for declining substitutability.

**Open question:** what's the formal model? Block 4 mentions parameters σ + α + V_option — these are presumably substitutability-related, scarcity-rate, and option-value-of-preservation. The Tech Appendix needs explicit formalism.

**Conditional PASS:** Method 3 is sound in principle but underspecified. Tech Appendix v0.0.5 must publish the specific model.

### §4.4 Triangulation discipline

**Test:** Does running three independent methods produce robust RCV estimates?

This is methodologically sound. Triangulation is standard validation in social-science research; replacement-cost + revealed-preference + option-value cover three distinct epistemological angles. Convergence reduces uncertainty; divergence reveals where the real disagreements live.

**M12 audit:** triangulation methodology is established (general validation strategy). Framework's contribution is the SPECIFIC three methods chosen for RCV estimation.

### §4.5 Verdict on Block 2

PASSES with refinements:
- Reframe Method 2 explicitly per Open Insight #14 epistemic humility.
- Tech Appendix v0.0.5 publishes Method 3 formal model.
- Block 4 sensitivity-analysis on σ/α/V_option must be executed.

---

## §5. Block 3 rigor — Hotelling Identity (the M6 academic-positioning win)

### §5.1 The claim

> *"In standard resource economics, Hotelling's rule says the resource rent (market price minus extraction cost) should rise over time at the rate of interest. That rent represents the extractor's scarcity premium. RCV represents the commons' scarcity premium — the value that the community and future generations lose, which the extractor doesn't pay for."*
>
> *"RCV − Hotelling rent = Cost severance per unit."*
>
> *"This is not an analogy. It is an identity."*

### §5.2 Identity verification

Per Hotelling 1931:
- Hotelling rent (per unit) = Market price − Extraction cost
- Hotelling rent represents scarcity-priced extractor revenue

The framework's claim:
- RCV (per unit) = community + future-generations scarcity-related loss
- RCV − Hotelling rent = the gap = Cost Severance per unit

**Algebraic check:** Cost Severance per unit = (community's true cost loss per unit) − (extractor's market-priced scarcity premium) = RCV − Hotelling rent. ✓

This holds AT THE DEFINITIONAL LEVEL. Whether it holds in practice depends on: (a) RCV being correctly estimated (Block 2 triangulation); (b) Hotelling rent being correctly priced (standard market-data lookup).

### §5.3 Why this is identity (not analogy)

Hotelling rent and RCV are NOT just analogous metaphors — they're complementary measurements of the same scarcity event from different sides:
- Hotelling rent: extractor's view (market-priced).
- RCV: commons' view (true cost).
- The gap is, by mathematical definition, Cost Severance.

**M12 framing:** Hotelling 1931 is canonical resource-economics; framework's contribution is the IDENTITY relation positioning RCV as Hotelling-complementary measurement. Massive M6 academic-positioning win.

### §5.4 Open question — temporal integration

Hotelling rent is a per-period quantity (rises at rate of interest over time). RCV is integrated over time. So "RCV − Hotelling rent = CS per unit" needs Tech Appendix care:
- At per-unit per-period level: RCV(t) − Hotelling-rent(t) = CS(t).
- At integrated level: ∫RCV(t) dt − ∫Hotelling-rent(t) dt = ∫CS(t) dt.

Both make sense but the framing in Block 3 ("RCV − Hotelling rent = Cost severance per unit") suggests per-unit per-period; Tech Appendix should formalize.

**Conditional PASS:** Identity holds; Tech Appendix specification needed.

### §5.5 Bibliography addition required (Hotelling 1931)

Hotelling, Harold. "The Economics of Exhaustible Resources." *Journal of Political Economy* 39, no. 2 (1931): 137–175. — foundational resource-economics paper. Add to bibliography under §16 (Decision theory and uncertainty) or new section on resource economics.

This is a load-bearing M6 academic citation — the Hotelling identity is THE clean bridge from framework vocabulary to standard resource economics. Bibliography MUST include it.

### §5.6 Verdict on Block 3

PASSES. Identity claim holds at definitional level; Tech Appendix specification required for temporal-integration framing; Hotelling 1931 must be added to bibliography.

---

## §6. Block 4 rigor — Validation Strategy

### §6.1 Falsifiability assessment

Block 4 specifies five test cases + sensitivity analysis. Standard scientific-method validation infrastructure.

- **Calibration case (Norway):** Methods 1 + 3 should bracket Method 2's Norway figure. Falsifiable.
- **Primary cases (Appalachian coal · Niger Delta · Canadian tar sands):** model should produce qualitatively-correct ranking. Falsifiable.
- **Boundary case (Chesapeake fisheries):** S(t) drops below regeneration threshold → renewable becomes non-renewable → RCV should spike. Falsifiable.
- **Cross-domain case (Indigenous land dispossession):** enclosure, not depletion. Tests model's scope. Falsifiable.
- **Sensitivity analysis:** σ + α + V_option across plausible ranges. Diagnostic.

### §6.2 Quality of the validation infrastructure

**Strong M2 + M6:** the validation strategy is methodologically rigorous. Multiple test types (calibration + primary + boundary + cross-domain + sensitivity) cover different aspects of model robustness.

**Operational gap:** the validation strategy is SPECIFIED but not EXECUTED. Block 4 prescribes; the actual case-study calculations haven't happened (or aren't documented in current rigor work).

**Recommended:** Tech Appendix v0.0.5 should INCLUDE the executed validation calculations (Method 1 + 2 + 3 numerical estimates for at least Norway calibration + Appalachian coal). Without execution, the falsifiability infrastructure is hypothetical.

### §6.3 Sensitivity-analysis insight (potential framework strength)

> *"If one parameter dominates — if the answer is always 80% determined by σ regardless of other parameters — that's critical to know. It means the real debate about RCV is a debate about substitutability."*

This is a M11-critic-survival insight. If σ (substitutability) dominates, the framework reframes the central debate as: *"the real disagreement about Cost Severance magnitude is a disagreement about substitutability, not about discount rates or pricing approaches."* This narrows the contested surface.

Either:
- σ dominates → framework's contribution is in S(t|t₀) modeling (the ratified Substitutability Function rigor pass aligns with this).
- α (scarcity-rate) dominates → framework focuses on scarcity-modeling.
- V_option dominates → framework focuses on real-options-theory specification.
- No clear dominance → framework explains where uncertainty lives across all three.

**All scenarios are M11-survivable.** Sensitivity analysis WHEN EXECUTED produces useful framework positioning regardless of result.

### §6.4 Verdict on Block 4

PASSES as validation-strategy SPECIFICATION. Conditional on EXECUTION — Tech Appendix v0.0.5 should publish the actual numerical validation results for at least the Norway calibration case to substantiate falsifiability.

---

## §7. Cross-block integration (do the four blocks form a coherent system?)

### §7.1 Block-to-block dependencies

- **Block 1 → Block 2:** Block 2's three methods are specifically for RCV (the forward-looking instrument from Block 1). CSD has its own measurement methodology (reparations-economics; Block 1 specifies). Two-instrument architecture is preserved.
- **Block 1 → Block 3:** Block 3's "Total Extraction Damages = CSD + uncaptured RCV" depends on Block 1's two-instrument distinction.
- **Block 2 → Block 4:** Block 4 validates Block 2's three methods.
- **Block 3 → Tech Appendix:** Block 3's identity claim provides academic-positioning anchor for the framework.

### §7.2 Layer ordering with already-ratified framework elements

```
Layer 1: COMMONS IDENTIFICATION (commons-as-structural-identity reframing)
   ↓
Layer 2: COST ADMISSION (Four Gates — CIT + Units + Boundedness + Independence)
   ↓
Layer 3: COST QUANTIFICATION (Cᵢ admitted; backward = CSD; forward = RCV)
   ↓
Layer 4: VALUE ESTIMATION (Three Ways for RCV; reparations economics for CSD)
   ↓
Layer 5: HOTELLING BRIDGE (RCV − Hotelling rent = CS per unit; standard-economics integration)
   ↓
Layer 6: ACCOUNTABILITY GAP (CS = RCV − B; CSD measures realized severance damages)
```

**Verdict:** The four blocks slot cleanly into layers 3-5. Coherent integration.

### §7.3 Two-instrument architecture (Block 1) implications

Per Block 1, the framework actually has TWO accountability gaps, not one:
- **B1: Reparations Bond** = should equal CSD (compensate measured human harm); under-bonded everywhere.
- **B2: Resource-Foreclosure Bond** = should equal RCV (price the permanent foreclosure); under-bonded everywhere.

Currently the framework has been treating B (Accountability Bond) as a single quantity. Block 1's two-instrument architecture suggests B should be decomposed: B = B1 + B2.

Norway's sovereign wealth fund is approximately B2 (resource-foreclosure bond — captures permanent-foreclosure value via investment returns). It's NOT B1 (reparations bond — Norway pays for its citizens' welfare separately via tax-funded social programs; that's distinct from the SWF).

**This is potentially a framework refinement worth flagging:** the Accountability Bond ratification (commit `7fa1c1b`) was at the AGGREGATE level. Block 1 surfaces a decomposition into B1 + B2 that's not yet integrated into the Accountability Bond record.

**Recommended:** Tech Appendix v0.0.5 includes this decomposition; Terms Index Accountability Bond record updated to reflect two-instrument architecture; Open Insight #14 epistemic-humility framing updated to specify Norway's SWF as B2-canonical (not B-canonical).

### §7.4 Verdict on cross-block integration

PASSES. The four blocks cohere as a system + integrate cleanly with already-ratified framework elements + surface a refinement to the Accountability Bond architecture (B = B1 + B2 decomposition).

---

## §8. M12 cross-block prior-art audit

### §8.1 Established prior-art anchors

**Block 1 (Two-Instrument Distinction):**
- Reparations economics: Darity & Mullen (2020 + earlier work) is canonical. Block 1 cites them implicitly via "the reparations literature... uses wealth gap calculations against comparable households."
- VSL + DALY methodologies: established health-economics + social-cost-of-illness literature.
- Intergenerational mobility: Chetty et al. (already in bibliography §4).

**Block 2 (Triangulated Estimation):**
- Method 1 — Replacement-cost methodology: established environmental-economics; Costanza et al. (1997) ecosystem-services valuation.
- Method 2 — Revealed-preference: established consumer-economics + environmental-valuation literature.
- Method 3 — Real-options theory (Dixit-Pindyck 1994 — already in bibliography).

**Block 3 (Hotelling Identity):**
- Hotelling 1931 — canonical.
- Resource-economics tradition since.

**Block 4 (Validation Strategy):**
- Standard scientific validation methodology (multiple test cases + sensitivity analysis).
- No specific prior-art collision.

### §8.2 Bibliography additions required

For Tech Appendix v0.0.5 academic positioning:

1. **Hotelling, Harold. "The Economics of Exhaustible Resources." *Journal of Political Economy* 39, no. 2 (1931): 137–175.** (LOAD-BEARING — Block 3 identity claim)
2. **Darity, William A., Jr., and A. Kirsten Mullen. *From Here to Equality: Reparations for Black Americans in the Twenty-First Century.* University of North Carolina Press, 2020.** (Block 1 reparations-model anchor)
3. **Costanza, Robert, et al. "The value of the world's ecosystem services and natural capital." *Nature* 387 (1997): 253–260.** (Block 2 Method 1 ecosystem-valuation precedent — optional but useful)
4. **Sandel, Michael J. *What Money Can't Buy: The Moral Limits of Markets.* Farrar, Straus and Giroux, 2012.** (Block 1's deepest claim about CSD-RCV correlation has moral-economic-philosophy resonance with Sandel — optional, lower priority)

### §8.3 M12 framework-honesty positioning (recommended Tech Appendix passage)

> *"The framework's central value-estimation apparatus draws on established economics across multiple traditions: Hotelling 1931 for the resource-rent identity; Dixit-Pindyck 1994 for real-options theory; Costanza 1997 for ecosystem-services replacement-cost valuation; Darity & Mullen 2020 for reparations-economics. The framework's contribution is not the individual estimation methods (each established in resource economics) but the integration: a two-instrument framework (CSD + RCV) for distinct moral-economic measurements; a triangulation discipline for RCV; a Hotelling-identity bridge between RCV and standard resource economics; and a falsifiable validation strategy."*

This is the M12-honest framework-positioning passage. Extension-with-integration claim survives reviewer scrutiny.

### §8.4 Aggregate M12 verdict

All four blocks PASS M12. The framework is honestly extending established economics traditions, not coining novel methodology. Tech Appendix v0.0.5 + bibliography additions implement Principle #6 Corollary D action ladder Level 1 + Level 4.

---

## §9. Verdict + framework structure additions

### §9.1 Ratifications recommended

1. **Block 1 (Two-Instrument Distinction): RATIFY.** Promote CSD to Ring 2 as backward-looking instrument. New Terms Index record.

2. **Block 2 (Triangulated RCV Estimation): RATIFY** with refinements:
   - Method 2 framing per Open Insight #14 epistemic humility.
   - Tech Appendix v0.0.5 publishes Method 3 formal model.
   - Sensitivity-analysis execution flagged for Block 4.
   New Terms Index record for "Triangulated RCV Estimation" (or absorbed into "Three Ways of Counting" methodology entry).

3. **Block 3 (Hotelling Identity): RATIFY** with conditions:
   - Tech Appendix v0.0.5 specifies temporal-integration framing.
   - Hotelling 1931 added to bibliography.
   - Promote to Ring 2 as framework-economics bridge.
   New Terms Index record for "Hotelling Identity."

4. **Block 4 (Validation Strategy): RATIFY** as specification; conditional on execution.
   - Tech Appendix v0.0.5 publishes executed validation calculations for at least Norway calibration + Appalachian coal.

### §9.2 Framework structure additions surfaced

**A. CSD (Cost Severance Damages) — Ring 2 promotion.** Backward-looking instrument; reparations-model-grounded; structurally distinct from RCV; new Terms Index record.

**B. Hotelling Identity (RCV − Hotelling rent = CS per unit) — Ring 2.** Bridge to standard resource economics; new Terms Index record.

**C. Triangulated RCV Estimation methodology — Ring 2.** Three Methods (Replacement Cost + Norway Revealed Preference + Scarcity-Adjusted Option Value) + convergence/divergence diagnostic.

**D. Accountability Bond decomposition surfaced (B = B1 + B2).** B1 = Reparations Bond (closes CSD gap); B2 = Resource-Foreclosure Bond (closes RCV gap). Update Accountability Bond Terms Index record.

**E. Open Insight #19 — CSD-RCV correlation hypothesis.** Block 1's deepest claim; falsifiable; Block 4 case-study record should test. Currently UNVALIDATED but structurally important.

### §9.3 Sweep targets activated

- Tech Appendix v0.0.4 → v0.0.5 (Hotelling identity + Three Methods formal model + validation execution + B1/B2 decomposition).
- Glossary v3 — entries for CSD + Hotelling Identity + Triangulated RCV Estimation.
- Terms Index — 3 new records (CSD; Hotelling Identity; Triangulated RCV Estimation).
- Bibliography — Hotelling 1931 (LOAD-BEARING); Darity & Mullen 2020; Costanza 1997 (optional).
- Methodology doc v1.4.0 — integrated formal-model section (currently focused on commons + dimensions; expand to include estimation apparatus).
- Accountability Bond Terms Index record — B = B1 + B2 decomposition note.
- Open Insight #14 (Norway-as-canonical) — update with Norway-as-B2-canonical specifically.

Estimated sweep effort: ~10-15 hours additional Phase A3 Stream A work.

### §9.4 Open Insights to capture

- **Open Insight #19 — CSD-RCV correlation hypothesis (validated by Block 4 cases).**
- **Open Insight #20 — Sensitivity-analysis execution (σ vs α vs V_option dominance).**

---

## §10. Term Provenance Records (proposed)

### §10.1 Cost Severance Damages (CSD) — Ring 2 (NEW)

**Working definition:** Backward-looking framework instrument measuring realized human harm from cost severance — health damages, intergenerational disadvantage, community-level suffering, foreclosed life-trajectories. Distinct from RCV (forward-looking resource permanent-foreclosure measure). CSD draws on reparations economics (Darity & Mullen 2020), VSL + DALY methodologies, intergenerational mobility research. Companion instrument to RCV in framework's two-instrument architecture per April 19, 2026 Block 1.

**Status:** [PROPOSED — pending ratification of this rigor pass; would supersede implicit-operation status.]

**Pairs with:** RCV (forward-looking companion); Reparations Bond (B1); Cost Severance mechanism.

### §10.2 Hotelling Identity — Ring 2 (NEW)

**Working definition:** Identity claim *RCV − Hotelling rent = Cost Severance per unit*. Bridge between framework vocabulary and standard resource-economics math (Hotelling 1931). Per-unit per-period definitional identity; integrated form at extraction-event level. Provides M6 academic positioning anchor.

**Status:** [PROPOSED — pending ratification of this rigor pass.]

**Pairs with:** RCV (numerator); Cost Severance equation (CS = RCV − B in framework; extends to per-unit form via Hotelling).

### §10.3 Triangulated RCV Estimation — Ring 2 (NEW)

**Working definition:** Three-method estimation methodology for RCV — Method 1 (Replacement Cost lower bound) + Method 2 (Revealed Preference via Norway calibration, middle estimate) + Method 3 (Scarcity-Adjusted Option Value upper bound). Convergence reduces uncertainty; divergence reveals real disagreements. Estimation apparatus complements Four Gates admission apparatus.

**Status:** [PROPOSED — pending ratification of this rigor pass.]

**Pairs with:** RCV (the quantity estimated); Four Gates (admit costs first, estimate value second); Hotelling Identity (provides cross-validation against Hotelling rent).

---

## §11. Author-ratified resolutions

**Ratified 2026-04-24 by Chris Winn — PASS WITH CONDITIONS, with explicit directive that each new framework element gets its own dedicated full rigor pass before being added to the framework.** Author directive: *"we can't add new terms Cost Severance Damages, Triangulated RCV Estimation, Reparations Bonds, Resource-Foreclosure Bond, methods, or things to the framework without due rigor."*

**Foundation-level ratifications activated by this pass:**
1. **All four blocks PASS WITH CONDITIONS** at the framework-architecture level.
2. **CSD identified as Ring-2 candidate** — promotion requires dedicated rigor pass before Terms Index record creation.
3. **Hotelling Identity identified as Ring-2 candidate** — promotion requires dedicated rigor pass.
4. **Triangulated RCV Estimation identified as Ring-2 methodology candidate** — promotion requires dedicated rigor pass.
5. **B = B1 + B2 decomposition identified as refinement to ratified Accountability Bond** — refinement requires dedicated rigor pass.
6. **Hotelling 1931 + Darity & Mullen 2020 added to bibliography** as load-bearing on this ratification.
7. **Open Insights #19 (CSD-RCV correlation hypothesis) + #20 (sensitivity-analysis execution) opened.**

**Per-element rigor passes commissioned by this ratification:**
- CSD (Cost Severance Damages) — individual full rigor pass.
- Hotelling Identity — individual full rigor pass.
- Triangulated RCV Estimation — full rigor pass (includes Method 1 + 2 + 3 as sub-tests).
- Accountability Bond B = B1 + B2 decomposition — full rigor pass.

**Phase A3 Stream A sweep work activated** (~10-15 hours) but gated on per-element rigor passes ratifying first.

**Tech Appendix v0.0.5 publication target:** publishes Hotelling identity formalism + 3-method specification + validation execution + B1/B2 decomposition. Drafted only after per-element passes ratify.

**Block 4 validation execution:** flagged for Phase A3 / Phase B; numerical calculations for at least Norway + Appalachian coal calibration cases to substantiate falsifiability infrastructure.

---

## §12. Rerun gate

Rerun if:
- Hotelling Identity proves not to hold under Tech Appendix specification.
- Block 4 validation execution shows triangulation produces wildly divergent estimates on test cases.
- CSD-RCV correlation claim proves empirically false.
- Sensitivity-analysis execution shows different parameter dominance than expected.
- Method 3 formal-model specification reveals inconsistency with rest of framework.

---

*End of framework-level rigor pass v1.0.0 on Three Ways + RCV Formal-Model Blocks (1-4). All four blocks PASS WITH CONDITIONS. CSD promoted to Ring 2 (hidden framework element surfaced). Hotelling Identity ratified as M6 academic-positioning win. Triangulated RCV Estimation ratified as estimation apparatus complementing Four Gates admission apparatus. Block 4 validation requires execution. Pending author ratification.*
