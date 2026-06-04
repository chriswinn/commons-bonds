# Deep Editorial Cut-and-Fix Memo — Chapter 6, "Three Ways of Counting"

**Date:** 2026-06-04
**File audited:** `manuscript/chapters/Chapter__6_ThreeWaysofCounting.md` (366 lines, ~13,431 words)
**Lens:** contribution-matrix / landing-point taxonomy / canonical-figure drift
**Register:** real editorial cut-and-fix memo, not a profile

---

## 0. Headline judgment

Ch 6 is the book's **load-bearing methods chapter** and it is doing far too much. The irreducible job is tight (three estimation methods → convergence → "the direction never flips"). But the chapter has accreted **a second, parallel chapter's worth of apparatus-naming material** — the etymology of "externality tail," the etymology of "Residual Commons Value," the etymology of "Commons Inversion Test," the etymology of "Asymmetric Regret Rule," the Four Gates, the Ten Commons Categories, Two Kinds of Commons, Parfit, Sen — most of which belongs in the Technical Appendix or in the chapters that own those objects (Ch 1, Ch 5, Ch 7, Ch 9). The chapter currently reads as if it is trying to be the framework's master reference rather than its convergence demonstration.

The single most consequential prose problem is **defensive over-explanation**: roughly 30-35% of the word count is the chapter pre-litigating objections and justifying its own naming choices in a tone that signals anxiety rather than authority. The convergence result — the actual contribution — is buried under it.

There is also **one real figure-drift problem** (the carbon term and total never reach the canonical $496/$510 values; the chapter runs $441/$449-464 nationally and $518-532 McDowell-specifically, with the canonical $496/$510 absent), and a **Norway figure inconsistency** (~$48/BOE vs ~$50/BOE vs "$48/BOE" in-table) worth reconciling.

---

## 1. The chapter's irreducible job (the spine)

**Job:** Establish that the cost-severance gap is *measurable* and *not a methodological artifact*, by computing it three independent ways and showing the estimates converge in range and never flip direction. Distill to the through-question: "Am I looking at the full honest accounting?"

The minimal spine, in order:
1. **Setup** — cases so far show the mechanism; the serious reader asks "how do we know they're representative / how large is the gap?" (¶10-20)
2. **Approach 1 — bottom-up damage accounting** → a floor; lives/dies on SCC; honest about its blind spot. (§Approach 1)
3. **Approach 2 — real-options** → speaks to the CFO; social option value > private; direction holds. (§Approach 2)
4. **Approach 3 — RCV** → the integral, foreclosure + externality-tail, the two-term formula; CS = RCV − B; IPG = RCV/P. (§Approach 3, formula only)
5. **The convergence** → the table; "different foundations, same direction; never flips." (§Convergence)
6. **Norway backtest** → the model differentiates; even the best case has CS > 0. (§Norway)
7. **Close** → "the difference is the subsidy by which the extraction economy runs." (final ¶)

Everything else in the current chapter is **either appendix material, other-chapter material, or defensive padding** layered onto this spine. The spine itself is excellent and should survive intact.

---

## 2. ISSUE LIST — every place it goes beyond what it needs

Ordered roughly by severity of excess.

| # | Where | Issue | Approx words | Why it exceeds |
|---|---|---|---|---|
| I-1 | ¶121 — "externality tail" etymology | Premature depth / digression. A full 350-word disquisition on why "tail" beats "aftermath," "trail," "legacy," "long-run," "persistent," plus the Weitzman fat-tail lineage. This is a *naming-defense* essay embedded mid-formula. | ~350 | The reader needs the *concept* (damage with a non-vanishing long tail). The lexicographic defense of the word is appendix material; it interrupts the term-by-term formula walk at its most cognitively loaded moment. |
| I-2 | ¶303 — "Commons Inversion Test" naming defense | Same pattern: ~310 words defending "inversion" over "reversal/recovery/counterfactual," plus the David Lewis lineage, plus a *second* revealed-preference rejection. | ~310 | Pure naming-defense + redundant with ¶305 (which re-litigates revealed-preference at the gate AGAIN). Two consecutive paragraphs make the same revealed-preference point. |
| I-3 | ¶305 | Redundant revealed-preference rejection. Restates ¶303's closing move ("uses revealed preference as estimation input, not as the discrimination gate") at length. | ~190 | Wholly duplicative of ¶303's last four sentences. |
| I-4 | ¶325 — "Residual Commons Value" naming defense | ~290 words on Hartwick/Ostrom/Mazzucato sub-choices + why "resource/public good/natural capital/cost/wealth/worth" were rejected. | ~290 | The Hartwick/Ostrom/Mazzucato *positioning* is load-bearing (matrix cells A); the per-word rejection list is appendix material. Keep the positioning, cut the thesaurus. |
| I-5 | ¶361 — "Asymmetric Regret Rule" naming defense | ~190 words on "regret vs risk" and "asymmetric vs one-sided." | ~190 | The ARR itself is introduced one paragraph earlier (¶359) and explicitly deferred to the Appendix and Ch 9. The name-defense is doubly out of place — it justifies the name of an object the chapter just said it isn't introducing. |
| I-6 | §The Four Gates (¶287-315) | Whole section is premature/misplaced. The chapter introduces the two-term formula in §Approach 3 and tells the reader "that is the entire mathematical apparatus this chapter requires" (¶131). Then 150 lines later it introduces the Four Gates admission apparatus in full (Commons Inversion + Units Consistency + Boundedness + Independence) with sub-forms, naming defenses, and worked rejections. | ~1,500 | The Four Gates are the *admission* discipline — they belong with the formula (Approach 3) compressed, or in the Appendix in full. As a free-standing late section they re-open the apparatus after the convergence result has already landed, deflating the chapter's climax. |
| I-7 | §Ten Commons Categories (¶233-253) | Misplaced / belongs to Ch 1 + Appendix. Lists ten categories, then spends most of the section on the *autonomy* contested-case + three political-tradition readings + the Ch 1 120-hour-week recap. | ~1,150 | The chapter's stated scope is "walk two of the ten at depth" — but it actually relitigates the universality-of-commons debate (classical-liberal / civic-republican / lived-oppression readings) that Ch 1 owns. This is the framework's *ontology*, not its *measurement*. |
| I-8 | §Two Kinds of Commons (¶275-285) | Belongs adjacent to Ostrom-positioning, and partially duplicates §The Contribution. Coordination-commons vs extraction-commons + the heterogeneous-stakeholder / stratification-economics extension. | ~900 | Valuable matrix content (Ostrom parallel/extend; Darity-Hamilton stratification extend) but it is the third place in the chapter that distinguishes this framework from Ostrom (also ¶279, ¶323). The Ostrom-distinction is made 3x. |
| I-9 | §What Is Owed (¶255-273) — Parfit + Sen | Belongs to Ch 5 (two-instrument apparatus) or Ch 7. Parfit non-identity (full treatment) + Sen capability-valuation (full treatment). | ~1,050 | This is the *moral grounding*, not the *measurement*. The chapter even concedes (¶269) "Chapter 6's role here is methodological" — an explicit admission the Parfit/Sen material is off-spine. Sen in particular (¶273) is a single dense block that adds a second philosopher to a chapter already overweight. |
| I-10 | ¶54-57 + ¶52 | Over-argued SCC-is-political passage. The point (every SCC choice is a political statement; zero is also a choice) is made, then re-made, then made a third time with the weather-model analogy and the "parameters are becoming more estimable" coda. | ~450 | The core point is one strong paragraph. The chapter spends four. The weather-model analogy is good and can stay; the "parameters narrowing" optimism coda is a digression that invites the Simon-Ehrlich substitution-optimism objection it doesn't want. |
| I-11 | ¶58-62 — DAC horizons | Premature depth. Four DAC cost horizons (Climeworks Orca/Mammoth/Gen-3, Carbon Engineering Stratos, IEA, IPCC AR6) with summit dates and facility commissioning timelines. | ~400 | Approach 1 is "the method that needs no theory." This is a research-note level dump of DAC engineering economics that properly belongs to Method 1 (Replacement Cost) in Approach 3, where DAC is actually used. It arrives ~80 lines early and at far more granularity than Approach 1 needs. |
| I-12 | ¶137 | Over-explained "three ways inside RCV" framing. The institutional-asymmetry rationale (markets price future profit via DCF but not future harm) is restated twice within the paragraph. | ~120 | Good idea, said once would be stronger. The "missing market mechanism" metaphor is repeated. |
| I-13 | ¶183-194 | Reconciliation-thicket. Eleven lines reconciling the 33-122x (Ch 2) vs 50-555x (triangulated) IPG ranges, plus Libby 40x, plus Deepwater 40%-recovery, plus "every figure carries an implicit method-and-time-horizon attribution." | ~600 | Necessary reconciliation exists, but at this length it reads as anxious bookkeeping. The reader who needs the full reconciliation has the Appendix (§11.11) flagged. Compress to the one load-bearing sentence (the two ranges differ by *time horizon anchored*, not by contradiction). |
| I-14 | ¶205-211 — falsifiability | Over-long. Yeager/sound-barrier analogy + two CS≈0 worked cases (plantation timber, construction sand) + the CIT-vs-empirical two-layer falsifiability distinction. | ~650 | The falsifiability objection deserves a real answer (it's a flagged objection-to-survive: "unfalsifiable"). But the two-layer distinction (¶209) re-explains what ¶205-207 already established. The Yeager analogy and ONE worked CS≈0 case suffice. |
| I-15 | ¶34 — Darity longevity-gap methodology | Premature cross-reference depth. Three sentences establishing that McDowell's 13-year gap uses "the same methodology" as Darity's 6-7yr Black-white longevity gap. | ~110 | The Darity link is matrix-valuable (extend: legacy-effect pricing) but it's worked at length again in Ch 5 and recapped in ¶269. Here it interrupts the bottom-up community-cost walk. One sentence + cross-ref suffices. |
| I-16 | §The Contribution (¶319-349) | Partially redundant with §Approach 3 + §Two Kinds + the four naming-defenses. Restates substitutability-weighting, integrated architecture, and the CIT as "three additions," then re-applies them to McDowell/Deepwater/Libby. | ~1,400 (section); ~500 redundant | The "three additions" framing is the cleanest statement of the contribution in the chapter and should arguably be PROMOTED. But the per-case re-application (¶343-347) re-walks McDowell/Deepwater/Libby a third time after the convergence table and the bottom-up walk already did. |
| I-17 | Buried spine | The chapter's actual thesis sentence — "the difference is not a rounding error; it is the subsidy by which the entire extraction economy runs" — appears only in the final line (¶363), and a near-twin at ¶199. The convergence result (the spine's payoff) lands at ¶195-199, then is followed by ~170 lines of additional apparatus before the chapter ends. | n/a | The climax is at ~line 199; the chapter runs to line 365. The strongest landing is structurally buried under appendix-grade material. |

---

## 3. PRIORITIZED CUT LIST (SAFE = no argument loss; TRADE = some loss)

Ordered by recommended cut sequence (highest value-per-word first).

| Item | Tag | Approx words | Note |
|---|---|---|---|
| **C-1.** Cut "externality tail" etymology (I-1, ¶121) to 2 sentences: keep the statistical-tail concept + Weitzman fat-tail cite; drop the aftermath/trail/legacy/long-run/persistent rejections. | SAFE | −300 | Concept survives; lexicography → Appendix. |
| **C-2.** Cut "Commons Inversion Test" naming defense (I-2, ¶303) entirely; fold the one operational sentence ("would the same extraction impose this cost if the commons were non-scarce?") into the §Four Gates first-gate description. | SAFE | −300 | The *test* is described elsewhere; only the name-defense is lost. |
| **C-3.** Delete redundant revealed-preference rejection (I-3, ¶305). | SAFE | −190 | Verbatim-duplicative of ¶303. |
| **C-4.** Cut "Residual Commons Value" naming defense (I-4, ¶325) to keep Hartwick/Ostrom/Mazzucato positioning (1-2 sentences), drop the resource/public-good/natural-capital/cost/wealth/worth rejection list. | SAFE | −230 | Matrix positioning kept; thesaurus → Appendix. |
| **C-5.** Delete "Asymmetric Regret Rule" naming defense (I-5, ¶361). | SAFE | −190 | ARR is explicitly deferred to Appendix §8 + Ch 9; the name-defense has no home here. |
| **C-6.** Move §Ten Commons Categories (I-7) to a compressed 1-paragraph pointer: "Across the eighteen cases the CIT surfaced ten illustrative categories (named in the Appendix); this chapter walks two — habitability via McDowell, time/autonomy via the Ch 1 examples." Cut the autonomy contested-case + 3-tradition readings (Ch 1 owns these). | TRADE | −950 | Loss: the explicit political-tradition-neutrality demonstration. Mitigant: Ch 1 + Appendix carry it. This is the most defensible TRADE because it removes the framework's *ontology* debate from its *measurement* chapter. |
| **C-7.** Cut Sen block (I-9, ¶273) entirely; keep Parfit non-identity but compress (I-9, ¶255-269) to ~1 strong paragraph + the two-instrument/forward-backward mapping. Move full Parfit+Sen grounding to Ch 5 or Ch 7. | TRADE | −800 | Loss: the dual moral-philosophy anchor (Parfit standing + Sen valuation) stated in-chapter. Mitigant: the through-question's "moral weight deferred to those with standing" is a Ch 5 job; Ch 6 self-describes as "methodological." Keep a 3-sentence Parfit nod so the non-identity objection isn't left fully exposed. |
| **C-8.** Compress DAC horizons (I-11, ¶58-62) to 2 sentences (DAC currently ~$400-1000/t, trending toward $200-600/t; full horizon table → Method 1). | SAFE | −330 | Approach 1 doesn't need DAC engineering depth; Method 1 (Approach 3) does and already flags it. |
| **C-9.** Compress §The Four Gates (I-6) — keep gates 2-4 as a single tight paragraph each (Units / Boundedness / Independence), cut the CIT naming-defense (already C-2) and the two redundant "each gate does work the others can't" restatements (¶313 duplicates ¶289). | TRADE | −600 | Loss: some of the Four-Gates pedagogy in-chapter. Mitigant: full apparatus is in Appendix §7 (flagged). Consider relocating the whole compressed Four Gates to immediately after the formula (Approach 3) so apparatus is introduced once, not re-opened post-climax. |
| **C-10.** Compress IPG reconciliation thicket (I-13, ¶183-194) to 3 sentences: the 33-122x and 50-555x ranges differ by *which time horizon is anchored* (M1-only engineering-scale vs all-three multi-generational), not by contradiction; full reconciliation in Appendix §11.11. | SAFE | −450 | The one load-bearing sentence survives; the per-case (Libby/Deepwater) micro-reconciliations are appendix-grade. |
| **C-11.** Compress SCC-is-political (I-10, ¶52-57): keep one paragraph + the weather-model analogy; cut the "parameters are becoming more estimable / uncertainty is narrowing" coda (invites Simon-Ehrlich). | TRADE | −300 | Loss: the "research is converging" optimism. Mitigant: it's a hostage to the substitution-optimism objection; cleaner to drop. |
| **C-12.** Cut the per-case re-application in §The Contribution (I-16, ¶343-347) to a single McDowell sentence; the convergence table + Approach-1 walk already did Deepwater/Libby. | TRADE | −400 | Loss: the "same case, larger number" pedagogy repeated per case. Mitigant: McDowell alone carries it; the table carries the others. |
| **C-13.** Compress §Two Kinds of Commons (I-8) — keep coordination-vs-extraction distinction + stratification-economics extension (both matrix-load-bearing) but cut the third Ostrom-distinction restatement and merge with the Ostrom material in §The Contribution. | TRADE | −350 | Loss: standalone framing. Mitigant: the Ostrom parallel/extend is made 3x; once, well, is stronger. Keep the Darity-Hamilton stratification extension (it's the divided-stakeholder matrix cell and appears nowhere else at this depth). |
| **C-14.** Compress falsifiability (I-14): keep Yeager analogy + ONE CS≈0 worked case (timber); cut the second worked case (construction sand) and the two-layer CIT/empirical distinction (¶209). | TRADE | −350 | Loss: belt-and-suspenders falsifiability. Mitigant: one clean worked CS≈0 case answers the "unfalsifiable" objection; two is overkill. |
| **C-15.** Trim Darity longevity-gap (I-15, ¶34) to 1 sentence + Ch 5 cross-ref. | SAFE | −80 | Methodology link kept; the worked depth is Ch 5's. |
| **C-16.** Trim institutional-asymmetry restatement (I-12, ¶137). | SAFE | −90 | Say the DCF-prices-profit-not-harm point once. |

---

## 4. TIERS

Current length: **~13,431 words.**

**Tier 1 — SAFE cuts only** (C-1, C-2, C-3, C-4, C-5, C-8, C-10, C-15, C-16):
- Words removed: ~1,960
- **Resulting length: ~11,470 words**
- Effect: removes all four naming-defense thesaurus passages, the redundant revealed-preference paragraph, the DAC engineering dump, the IPG reconciliation thicket, and two minor restatements. **Zero argument loss.** The chapter reads materially more authoritative because the defensive over-explanation is the first thing to go. This is the floor recommendation — do this regardless.

**Tier 2 — SAFE + TRADE** (add C-6, C-7, C-9, C-11, C-12, C-13, C-14):
- Additional words removed: ~3,750
- **Resulting length: ~7,720 words**
- Effect: relocates Ten Commons Categories, Parfit/Sen grounding, and (optionally) the full Four Gates apparatus to their owning chapters/Appendix; de-duplicates the three Ostrom-distinctions and the per-case re-walks; tightens falsifiability and SCC-politics. The chapter becomes a focused convergence-demonstration with a clean climax.

**Recommended landing: ~8,500–9,000 words.**
Take all of Tier 1, plus C-6 (Ten Categories → pointer), C-7 (Sen out, Parfit compressed), C-10/C-11/C-12 (the de-duplications), but **keep a compressed Four Gates in-chapter** (relocated to follow the formula, not as a post-climax section) and **keep §Two Kinds of Commons in compressed form** because the coordination/extraction distinction and the stratification-economics extension are matrix cells that appear at adequate depth nowhere else. This preserves every matrix cell and every flagged objection-engagement while cutting ~4,500 words of appendix-grade and defensive material. The chapter's spine (§1) is untouched in all tiers.

---

## 5. LANDING POINTS CARRIED (A–P) — with specifics; and THIN/DROPPED

**Carried well:**
- **A (contribution / lit-positioning):** Strong. §The Contribution explicitly positions as *extending* Pigou + Ostrom into extraction settings; Hotelling Identity bridge (RCV − Hotelling rent = CS); Hartwick/Ostrom/Mazzucato in the RCV naming.
- **B (core claims):** Strong. CS = RCV − B; IPG = RCV/P; foreclosure + externality-tail two-term integrand; substitutability-weighting as the novel move.
- **E (worked demonstrations):** Strong. McDowell, Deepwater, Libby, Exxon Valdez, Norway in the convergence table + Approach-1 walk. (Over-delivered — worked 2-3x; see I-16.)
- **F (originality/credibility):** Strong via the "three additions" framing + triangulation-is-standard-scientific-method argument.
- **L (falsifiability):** Carried (¶205-211) — directly engages the "unfalsifiable" objection with the Yeager analogy + CS≈0 worked cases.
- **M (domain/boundary):** Carried — §What the Chapter Leaves for Later + Norway-not-perfect + the coordination-vs-extraction commons boundary.
- **N (concealment-taxonomy / covers):** Carried via the CIT discovery-method framing ("discover previously unpriced costs") and the Four Gates.
- **D (limits named):** Carried — bottom-up is "a flashlight in a warehouse"; substitutability function "most novel and most vulnerable"; Method 1 underprices irreplaceable commons; Norway CS small-but-positive.

**Thin:**
- **C (objections to survive):** Carried for the *methodological* objections (choose-your-own-adventure, unfalsifiable, double-counting via the independence gate) but THIN on the *positioning* objections — see §7. Financialization/Pistor and Fraser are absent.
- **H (values / emotional arc):** THIN. This is a numbers chapter and that's appropriate, but the human spine (McDowell's 13-year gap, the buried headwater streams) is present only as cost line-items. No emotional through-line; the chapter is almost entirely analytical. Acceptable for a methods chapter but worth one anchoring image at the close.
- **K (reader takeaway):** Present but BURIED (I-17) — the takeaway sentence is the final line; the convergence climax at ¶199 is followed by 170 lines of apparatus.
- **O (stakes / why-now):** THIN. The "subsidy by which the extraction economy runs" close gestures at stakes but the chapter never says why *now*. Appropriate to defer to other chapters.

**Dropped:**
- **G (human/narrative spine):** Effectively DROPPED. No person is rendered; McDowell is a calibration case, not a place with people. Defensible for a methods chapter — flag, don't fix.
- **I (audience-landing):** Implicit only (the CFO/real-options aside in ¶84 is the one explicit audience-targeting move). No staged audience-load work in-chapter.
- **J (citations + gaps):** See §9 — several quantitative claims lack inline public sourcing.
- **P (comps / market):** Not a chapter job; correctly absent.

---

## 6. MATRIX CELLS positioned against (which works, how)

| Work | Relationship as positioned in Ch 6 | Where |
|---|---|---|
| **Hotelling (1931)** | EXTEND — Hotelling Identity: RCV − standard Hotelling rent = CS; Hotelling prices private extraction rent, not in-situ option value for future generations. | ¶331 |
| **Pigou** | EXTEND — RCV adds foreclosure + CIT-discovered costs Pigouvian accounting "has no method for including"; B < RCV (partial externality). | ¶323, ¶329, ¶343-347 |
| **Coase** | (CONTRADICT, implicit, THIN) — "future generations cannot bid" is present only via Parfit/non-identity, not named as a Coase rebuttal. See §7. | — |
| **Ostrom** | PARALLEL + EXTEND — coordination-commons (Ostrom) vs extraction-commons (this framework); "each method does work the other can't"; extends into heterogeneous-stakeholder commons Ostrom's design principles don't reach. Made 3x (¶279, ¶283, ¶323). | §Two Kinds, §Contribution |
| **Hartwick (1977)** | GENERALIZE — Norway as "the closest working example of Hartwick's Rule"; "residual" in the Hartwick family; (S_max ≤ 1 generalization is Appendix, flagged not stated). | ¶219, ¶325 |
| **Weitzman (2009)** | ADOPT — declining discount rate as D(t,t₀); fat-tail climate damages as the adjacent tradition for "externality tail." | ¶119, ¶121 |
| **Rawls** | (OPERATIONALIZE — THIN) — listed in passing ("Rawls listed primary goods," ¶239) but the "veil on extraction" operationalization is NOT made in Ch 6. | ¶239 |
| **Daly** | (OPERATIONALIZE — DROPPED) — strong-sustainability-quantified is not engaged; Daly is absent. | — |
| **Harvey** | (MEASUREMENT-TOOL — DROPPED) — "diagnoses mechanism / RCV measures magnitude" framing is the book's meta-claim but Harvey is not named in Ch 6. | — |
| **Darity + Mullen / stratification economics** | EXTEND — backward Restitution Bond (Darity-Mullen reparations methodology) + divided-stakeholder human commons (Darity-Hamilton stratification economics). Both present. | ¶34, ¶145, ¶269, ¶285 |
| **Parfit** | OPERATIONALIZE — non-identity → impersonal-outcomes; Foreclosure Bond = forward/impersonal, Restitution Bond = backward/person-affecting. | ¶259-265 |
| **Sen** | OPERATIONALIZE — capability-set valuation grounds the *how* of future-generation valuation. | ¶273 |
| **Mazzucato** | EXTEND (value created vs extracted) — the "Value" in RCV. | ¶325 |
| **Dixit & Pindyck (1994)** | ADOPT — real-options base for Method 3 scarcity-adjusted option value. | ¶143 |
| **Savage (1951)** | ADOPT/SPECIALIZE — minimax-regret → Asymmetric Regret Rule. | ¶359-361 |
| **Polanyi + Fraser** | **ABSENT — GAP.** The structural-commons / fictitious-commodity anchor is the book's #1 positioning gap and Ch 6 does not engage it at all. See §7 + §10. | — |
| **Pistor (Code of Capital)** | **ABSENT — GAP.** Financialization objection (bonds extend commodification) not engaged. See §7. | — |
| **Christophers / Susskind** | ABSENT (mechanism/metric) — acceptable for this chapter. | — |
| **Sandel** | (commodification-limit) — present only via the autonomy/120-hour-week material; the partial-commodification objection is not directly named. | ¶249-251 |

---

## 7. OBJECTIONS — ENGAGED vs EXPOSED

**ENGAGED (well):**
- **Choose-your-own-adventure / overcounting** — ¶203: convergence is itself evidence against arbitrariness. Strong.
- **Unfalsifiable** — ¶205-211: Yeager analogy + CS≈0 worked cases + "falsified the day a jurisdiction demonstrates CS ≤ 0." Strong (over-long).
- **Discount-rate fight** — §Substitutability Function: sidesteps via the empirical-substitutability move; Weitzman declining rate. Strong.
- **Just-Pigou / just-rebranded-externality** — §The Contribution: "three additions" + "no method for including these costs." Strong.
- **Double-counting** — the independence gate (fourth gate). Engaged.
- **Numbers-are-invented** — ¶52-56: SCC-zero is also a choice; "structures uncertainty." Engaged.
- **Ostrom-already-did-it** — §Two Kinds: coordination vs extraction commons. Strong.
- **Reproducibility ("two analysts, two numbers")** — ¶211: transparent disagreement vs uniform outputs. Engaged.
- **Non-identity (partial)** — Parfit, ¶259-265. Engaged.
- **Norway-not-transferable** — Method 2 explicitly does NOT translate Norway's per-barrel figure arithmetically (¶141). Engaged.

**EXPOSED (left open):**
- **FINANCIALIZATION / Pistor-Code-of-Capital** — *fully exposed.* The chapter prices commons via bonds (financial instruments) without engaging the objection that bonds *extend* commodification (the Pistor "code of capital" critique). Flagged in the brief as a GAP-to-fill; Ch 6 is a natural place to at least gesture at it (the Two Instruments + re-embedding/double-movement answer). **Recommend a 1-paragraph engagement** — currently the chapter's biggest exposed flank given that it's the chapter that introduces the bond-as-RCV-sized instrument.
- **FRASER / Polanyi structural-commons** — *fully exposed / GAP.* The "same object" structural claim (reef = atmosphere = labor = future generation) is exactly what §Two Kinds of Commons gestures toward (extraction-commons class) but never grounds in Polanyi's fictitious commodities or Fraser's expropriation. This is the book's #1 ratified GAP. Ch 6's extraction-commons section is the single best insertion point in the chapter for it.
- **Coase / voluntary-trades** — exposed except via Parfit. The Coasean "why not just bargain" answer ("future generations cannot bid") is implied by non-identity but never stated as a Coase rebuttal. THIN.
- **ESG / reformist-capture** — not engaged. (Defensible to defer.)
- **Degrowth-in-disguise** — not engaged.
- **Too-statist (partial)** — the Norway/sovereign-wealth-fund framing invites it; not addressed.
- **Cost-severance-metaphor-commodifies-labor** — the autonomy/120-hour-week material (¶251) is precisely where this objection lives (pricing a spouse's dying, a son's childhood) and the chapter does NOT address the commodification worry it raises. Partially exposed.
- **Public-choice / capture (partial)** — not engaged (the SCC-is-a-proxy-war point ¶50 gestures at it without naming capture).
- **Simon-Ehrlich substitution-optimism** — *the chapter invites it* with the "uncertainty is narrowing / parameters becoming more estimable" coda (¶56) and the substitutability-rising-fast framing, without defending against it. C-11 (cut the coda) reduces this exposure.

---

## 8. FIGURE DRIFT vs the canonical set

**This is the section with a real, actionable problem.** The canonical ratified McDowell figures are: **carbon term = $496 (= 2.61 t × $190); honest TOTAL = $510; Pigouvian floor = $504–518.** The chapter never reaches these numbers.

| Canonical | Chapter says | Verdict |
|---|---|---|
| Carbon term $496 (2.61t × $190, McDowell Pocahontas basis) | ¶42: carbon = **$441** (2.32t × $190, national-bituminous 24.9 mmBtu basis). $496 never appears. | **DRIFT / DUAL-BASIS** — The chapter deliberately runs the *national-bituminous* basis (2.32t, ~24.9 mmBtu) at "framework-introduction register" (¶42) and flags the McDowell Pocahontas basis (2.61t-equivalent, ~28 mmBtu) as Ch 8 / Appendix §11. So $441 is internally justified as the national figure. BUT: the chapter never states the canonical McDowell $496 carbon figure even in the McDowell-specific passage (¶343 jumps to the $518–532 *total* without stating the $496 carbon component). **Action: confirm whether Ch 6 should carry the canonical $496 explicitly. If the dual-basis design is intended, it is defensible but should name $496 once as the McDowell carbon anchor to stay consistent with Ch 8 / the ratified set.** |
| Honest TOTAL $510 | ¶44: national total **$449–$464**; ¶343: McDowell total **$518–$532**. $510 never appears. | **DRIFT** — $510 (the ratified McDowell honest total) is bracketed by neither number cleanly. $518–532 is *above* the canonical $510 and *above* the Pigouvian floor $504–518; $449–464 is below. **Action: reconcile.** The $518–532 McDowell figure (¶343) appears to use 2.61t carbon ($496) + ~$22 non-carbon ≈ $518, which lands at the *bottom* of $518–532 and is consistent with the $504–518 Pigouvian floor's top — but the canonical honest TOTAL is $510, not $518–532. Either the canonical $510 is stale or ¶343's $518–532 has drifted up. **Flag for author reconciliation against the ratified cascade.** |
| Pigouvian floor $504–518 | ¶343 frames $518–532 as the "standard Pigouvian accounting" number. | **DRIFT** — $518–532 overlaps the *top* of the $504–518 floor but extends above it to $532. The label "Pigouvian floor" attaches to a number ($532-top) above the canonical floor's ceiling ($518). **Action: confirm the $532 upper bound or align to $518.** |
| RCV-model band $580–620 (Technical-Appendix-only, NEVER the total) | The chapter does NOT cite $580–620 anywhere — correct (it's TA-only). | **CLEAN** — the chapter respects the "never the total" rule; good. |
| IPG 33–122x public / ~50x central / 555x TA-internal-only (never bare) | ¶185: "~fifty times" central ✓; ¶187: "thirty-three to one hundred and twenty-two times" ✓; ¶185 + table-prose: "fifty-to-five-hundred-fifty-five-times triangulated range." 555x appears as the *top of a triangulated range* (50–555x), not bare. | **CLEAN but watch** — 555x is presented as a range endpoint with method attribution (M3 ceiling), not bare; this respects the "never bare" rule. ¶273 closes on "IPG of 33" — consistent with the public 33-122x set. The 50-555x range is the one place 555x surfaces in main prose; it is attributed (M3 scarcity-irreversibility, multi-generational horizon) so it is not "bare," but it is the most exposed instance — **confirm this triangulated range is intended for main-text prose vs TA-only.** |
| Mine-mouth 1960 = $4.50 | ¶38, ¶80, table ✓ | **CLEAN** |
| SCC = $190 (EPA 2023) | ¶42, ¶48, ¶54, ¶60 ✓ (¶60 attributes to Rennert et al. 2022 at 2% discount) | **CLEAN** |
| CO₂ factor 2.61 (McDowell) / 2.32–2.33 (national) | ¶42: national **2.32** ✓; McDowell 2.61 is *implied* via "~28 mmBtu Pocahontas" but the **2.61 figure is never stated numerically** in Ch 6. | **MINOR DRIFT** — national 2.32 is correct and stated; the McDowell 2.61 is gestured at via heat-content but not given as a number. If Ch 6 is meant to carry 2.61, state it once. |
| US Steel McDowell/Gary closure = "across the 1980s" (phased; no hard year) | Not mentioned in Ch 6 (Ch 8 material). | **N/A** — not a Ch 6 claim. |

**Norway internal inconsistency (not in the canonical set but worth flagging):**
- ¶141 (Method 2): "approximately **fifty dollars**" per BOE.
- Table (¶174): "**~$48/BOE** rent captured" and M2 = "**$48/BOE**."
- ¶225 narrative: "captures most of the financial value."
**Action:** reconcile $48 vs $50 per BOE — pick one and use it consistently, or state explicitly that ~$48 is the measured figure and "approximately fifty" is the rounded narrative form.

**Deepwater revenue inconsistency:** ¶46 "roughly $4.25 billion" vs table "$4.25B Macondo revenue" ✓ consistent. Libby: ¶46 "$5 to $8 billion" total cost vs table M1 "$0.6B cleanup + $4-7B illness flow" and M2 "$0.3B settlements" — the $5-8B aggregate in ¶46 is roughly the sum; **consistent but worth a verifying pass** since ¶46 says "$5 to $8 billion in direct settlements" which mislabels the *aggregate* as "settlements" (settlements are only ~$0.3B per the table). **Likely a real error at ¶46: "settlements" should read "total documented cost" or similar.**

---

## 9. CITATION GAPS (claims needing a public source)

Inline-citation present and adequate: Black Lung ~$44B through 2009 (GAO/CRS, ¶28); EPA bituminous emission factor 93.28 kg/mmBtu (¶42); EPA 2023 SCC $190 (¶42); Rennert et al. 2022 (¶60); IEA *DAC 2022* (¶60); IPCC AR6 WGIII (¶60); Climeworks June 2024 Carbon Removal Summit Zurich (¶60); NBIM early-2025 $2.2T (¶219); Dixit & Pindyck 1994 (¶143); Darity & Mullen 2020 (¶145); Savage 1951 (¶359).

**Gaps — claims asserted without a public source:**
1. **¶32: McDowell "thirteen-year" life-expectancy gap vs national average** — load-bearing, recurs (¶295); needs a county-health-rankings / CDC / academic source inline.
2. **¶34: Darity "six-to-seven year Black-versus-white longevity gap" priced "as a legacy effect"** — needs the specific Darity publication (the methodology claim is strong; the cite is named only as "Darity Jr. and collaborators").
3. **¶30: Appalachian reclamation bonds "$3.7 to $6 billion short"** — specific figure, no source (attributed to "Chapter 2" but Ch 2 should carry the public source; verify it does).
4. **¶46: Deepwater "$65 to $70 billion" total cost; Libby "$5 to $8 billion"; Exxon Valdez "$7 to $10 billion"** — the table cells (¶175-177) *do* cite (NOAA, DOJ, 2016 Consent Decree; EPA Libby Superfund record; Exxon Valdez Trustee Council) but the *prose* figures in ¶46 are bare. Align prose to table sourcing.
5. **¶80/¶82: "much of the information was suppressed deliberately"** — a strong factual/causal claim about coal-industry information suppression; needs a source or softening.
6. **¶219-221: Norway carbon tax 1991 "one of the world's earliest" + "highest rates in any oil-producing economy" + ethics-council divestments** — multiple sourceable claims, none cited.
7. **¶143: Method 3 range "$420 to $13,100/ton, mid ~$2,500" + "α-dominance regime 0.9–1.0"** — attributed to "Technical Appendix cross-case sensitivity analysis"; internal cite only, no public anchor (acceptable IF the Appendix derives it, but the $13,100 ceiling is the kind of number a hostile reader will demand provenance for).
8. **¶100: "renewables are already displacing coal at scale" / "solar cells at three cents per kilowatt-hour" (¶76)** — the 3¢/kWh figure needs a source (LBNL / Lazard LCOE).
9. **¶46: Exxon Valdez "$5.5 million of oil spilled (product value)"** — unusual framing; needs a source for the product-value basis.

---

## 10. CROSS-CHAPTER FLAGS (redundancies / broken-promises / dependencies)

**Redundancies (this chapter re-does what other chapters own):**
- **Ch 1 (autonomy commons, 120-hour week):** ¶251 re-walks the Ch 1 knowledge-worker example at length. Ch 6 should *reference* it, not re-render it. (C-6 territory.)
- **Ch 2 (Black Lung Trust Fund, reclamation-bond shortfall, McDowell IPG 33-122x):** ¶28, ¶30, ¶187 recap Ch 2 material. The ¶187 IPG reconciliation is necessary; the program-mechanics recap (¶28) leans on "Chapter 2 walks the program... in detail" — good, keep the pointer, but verify Ch 2 actually carries the $3.7-6B bond figure with a source.
- **Ch 5 (two-instrument apparatus, Darity-Mullen reparations, Deepwater $65B enumeration):** ¶145, ¶263-269, ¶345 recap. ¶269 *explicitly* says "Chapter 5's introduction of the two-instrument apparatus... Chapter 6's role here is methodological" — this is an admission that the Parfit/Sen/Restitution material is Ch 5's and is being re-litigated here (C-7 territory).
- **Ostrom distinction made 3x** within Ch 6 (¶279/283 §Two Kinds, ¶323 §Contribution) — internal redundancy.
- **Norway** appears as Method 2 anchor (¶141, ¶174), as the §Norway Backtest (¶215-229), AND in the revealed-preference gate discussion (¶305). The backtest and the Method-2 anchor partially overlap; consider consolidating.

**Broken-promises / forward-reference load:**
- ¶355-359: promises Ch 7 (Mars / Earth-parochial test), Ch 8 (one-ton McDowell full decomposition), Ch 9 (ARR applied). These are *dependencies the chapter creates*: Ch 6 defers the McDowell carbon $496/$510 canonical reconciliation to Ch 8 (¶42 explicitly: "the McDowell-specific worked example in Chapter 8"). **Dependency flag:** if Ch 8's main-repo copy is the pre-fix $510-carbon/$524-total version (Candidate-7, per the brief), then Ch 6's forward-reference at ¶42/¶343 points at a number that needs the ratified cascade. **Verify Ch 8 carries $496 carbon / $510 total before finalizing Ch 6's pointer.**
- ¶253: "This chapter walks two of the ten commons categories at depth" — promise is only half-kept (habitability via McDowell is at depth; time/autonomy is a Ch-1 recap, not a fresh depth-walk). Either deliver the time/autonomy depth-walk or soften the promise.

**Dependencies (Ch 6 relies on, correctly flagged to Appendix):**
- RCV formula derivation, convergence proof, CS > 0 proof → Appendix §3, §9 (flagged ✓).
- Four Gates formal statements → Appendix §7 (flagged ✓).
- Bidirectionality → Appendix §5.5 (flagged ✓ — but cited 3x: ¶145, ¶179, ¶315; consolidate).
- IPG-table reconciliation → Appendix §11.11 (flagged ✓).
- ARR → Appendix §8 + Ch 9 (flagged ✓).
These pointers are healthy; the chapter correctly offloads proofs. The concern is the *inverse*: the chapter pulls too much appendix *exposition* (naming defenses, Four Gates, DAC horizons) back INTO the chapter that the Appendix already owns.

**Internal anchor risk:** all TA hyperlinks point to `TechnicalAppendix_v2.0.0.html`; several Method links (§3.3/§3.4/§3.5) resolve to the same `#sec-3-rcv-quantification` anchor (¶139, ¶141, ¶143) rather than distinct sub-anchors — verify the Appendix has the §3.3/§3.4/§3.5 sub-anchors or fix the links.

---

## Summary recommendation

Do **Tier 1 (all SAFE cuts) unconditionally** — it removes ~1,960 words of defensive over-explanation with zero argument loss and is the single highest-leverage improvement to the chapter's authority. Then take the recommended ~8,500-9,000-word landing (Tier 1 + selective TRADE), relocating the Ten Categories, Parfit/Sen grounding, and naming-defenses to their owning chapters/Appendix while keeping the compressed Four Gates and the coordination/extraction commons + stratification-economics distinction in-chapter. Separately and urgently: (a) reconcile the carbon/total figures against the canonical $496/$510 set and decide whether Ch 6 carries the McDowell anchor explicitly; (b) reconcile $48 vs $50 Norway BOE; (c) fix the ¶46 "settlements" mislabel; (d) verify Ch 8 carries the ratified $496/$510 before relying on the Ch 8 forward-reference; and (e) insert a 1-paragraph Polanyi/Fraser structural-commons grounding and a 1-paragraph Pistor-financialization engagement into §Two Kinds of Commons — the chapter's two biggest exposed flanks.
