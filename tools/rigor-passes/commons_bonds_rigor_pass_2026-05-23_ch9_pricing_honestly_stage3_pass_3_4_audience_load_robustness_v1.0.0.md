# Commons Bonds — Ch 9 *Pricing Honestly* — Stage 3 Pass 3.4 (Audience-Load Robustness)

**Date:** 2026-05-23
**Workstream:** Manuscript Stage-3 Rigor Pass (PM dashboard #20), Phase A
**Chapter file:** [Chapter__9_PricingHonestly.md](../../manuscript/chapters/Chapter__9_PricingHonestly.md) (294 lines, post Pass 1 + Pass 2 + Stage 1c Phase C)
**Discipline:** v3.0 Amendment B Pass 3.4 (audience-load robustness; adversarial / detractor character set; thread-pull synthesis verdict; verdict-floor EXCLUDE per character) per [tools/drafting-templates/stage-3-three-pass-rigor-audit.md](../drafting-templates/stage-3-three-pass-rigor-audit.md) §"Pass 3.4: Audience-load (robustness)"
**Mode:** audit-existing-prose
**Format model:** [Ch 1 REAUDIT v3 §5.3 adversarial thread-pull synthesis](commons_bonds_ch1_stage_3_pass_3_audience_load_REAUDIT_2026-05-17_PROPOSED.md) (canonical)
**Status:** RATIFIED 2026-05-25 — verdict CONDITIONALLY ROBUST accepted; T3 ratified + Phase C applied per §10 disposition log; pre-publication review queue items (§6.4) accepted as Stage 5 sign-off input. See §11 ratification record.

---

## §0. Source artifacts read

1. [Chapter__9_PricingHonestly.md](../../manuscript/chapters/Chapter__9_PricingHonestly.md) — 294 lines, post Pass 1 + Pass 2 + Stage 1c Phase C state (origin/main).
2. [Pass 3.3 acceptance artifact 2026-05-23](commons_bonds_rigor_pass_2026-05-23_ch9_pricing_honestly_stage3_pass_3_3_audience_load_acceptance_v1.0.0.md) — §2 per-character verdicts (18 INCLUDE / 0 EXCLUDE; aggregate READY TO SUBMIT AS-IS); §5.1 Pass 3.4 future-session pre-population; §6.4 readiness note.
3. [Pass 2 voice-polish artifact 2026-05-19](commons_bonds_rigor_pass_2026-05-19_ch9_pricing_honestly_stage3_voice_polish_v1.0.0.md) §6 + §11 — Pass-2-surfaced Pass-3 carry-forward; Reading C v3 substantive rewrite disposition log + informal audience-load test conducted during ratification.
4. [Pass 1 fact-check artifact 2026-05-16](commons_bonds_rigor_pass_2026-05-16_ch9_pricing_honestly_stage3_fact_check_v1.0.0.md) §7 — Pass-3 audience character inventory (original).
5. [Stage 1c coherence check 2026-05-21](commons_bonds_stage_1c_coherence_check_2026-05-21_ch8_rent_seeking_v1.0.0.md) — Ch 8:122 Option A spot-fix landed at commit `cbef9bd`; cross-chapter framing consistent across Ch 8 + Ch 9.
6. [Ch 1 REAUDIT v3 §5.3](commons_bonds_ch1_stage_3_pass_3_audience_load_REAUDIT_2026-05-17_PROPOSED.md) — adversarial thread-pull synthesis canonical format model.
7. [Stage-3 template](../drafting-templates/stage-3-three-pass-rigor-audit.md) §"Pass 3.4: Audience-load (robustness)" — verdict scale + thread-pull synthesis structure.
8. [Audience-pressure-test construction](../drafting-templates/audience-pressure-test-construction.md) §3 — adversarial character types + selection methodology.
9. [Manuscript Stage-3 rigor-pass handoff](../workstream-handoffs/manuscript-stage-3-rigor-pass-handoff_2026-05-11.md) — Ch 9 row.
10. [feedback_audience_aware_drafting_discipline.md](../memory/feedback_audience_aware_drafting_discipline.md) v3.0 + Amendment B; [feedback_named_subject_consent.md](../memory/feedback_named_subject_consent.md) public-record exception; [feedback_verify_stale_memory_claims.md](../memory/feedback_verify_stale_memory_claims.md).

Verification (per `feedback_verify_stale_memory_claims.md`):
- ✓ Chapter file path + 294 lines verified against current origin/main.
- ✓ Commit `4c8bc02` (Ch 9 Pass 1 Phase C) exists on origin/main.
- ✓ Commit `78a26c2` (Ch 9 Pass 2 Phase C + Reading C v3 rewrite) exists on origin/main.
- ✓ Commit `cbef9bd` (Ch 8 Stage 1c Phase C Option A) exists on origin/main.
- ✓ Commit `a6b7df5` (Ch 9 Pass 3.3 acceptance PROPOSED) exists on origin/main.

---

## §1. Pass-3.4 scope reminder

Pass 3.4 applies the **adversarial / detractor character set** to the chapter. Verdict-floor for adversarial characters is EXCLUDE; INCLUDE / NEUTRAL are not in scope. **The diagnostic is NOT pass/fail per character.** All adversarial characters return EXCLUDE — that is expected and required. The diagnostic is **which threads they collectively find** (§3 thread-pull synthesis) and whether those threads are (a) load-bearing chapter claims the chapter must hold against (acknowledge in pre-pub review queue; cross-chapter handoff if warranted) or (b) procedural / cosmetic flags (spot-fixable without damaging Pass 3.3 acceptance verdicts).

**Specifically tested under hostile read** (per framing carry-forward from Pass 3.3 §5.1):

- Does the Reading C v3 (Ch 9:134–148) asymmetric framework-Public-Choice framing survive a libertarian Public Choice hostile-reviewer read, or does the *"the angles are not symmetric"* + *"makes possible different decisions about future extraction... including the extractors themselves"* language read as ideological commandeering of rent-seeking methodology?
- Does the *"is a number"* four-fold anaphora at Ch 9:142 hold against an adversarial reader who pressure-tests each of the four cost-bearer realities (McDowell life-expectancy gap; Niger Delta mangrove; Baotou tailings dust; 2008 foreclosures) as either not-actually-a-cost or not-attributable-to-the-mechanism the framework names?
- Does the eleven-cent-difference passage rent-extractor-cluster sector-naming (Ch 9:206) hold against an adversarial reader who reads it as left-policy targeting that the *"structural observation, not advocacy"* disclaimer (Ch 9:208) cannot neutralize?
- Does the framework's three property-rights exceptions argument (Ch 9:160–164) hold against a Coase / property-rights-only adversarial reader who pushes back on each exception?
- Does the Asymmetric Regret Rule (Ch 9:56) + framework's decision-tool framing (Ch 9:144) hold against a Stern / Nordhaus IAM-tradition adversarial reader who pressure-tests overclaiming?

Adversarial set: 8 characters drawn from the categorical hostile-read positions per [audience-pressure-test construction](../drafting-templates/audience-pressure-test-construction.md) §3.2, scoped to Ch 9's specific framework-claims:

1. Libertarian Public Choice hostile reviewer (Cato / Mercatus / GMU economics / Heritage policy-cluster)
2. MacLean-sympathetic Buchanan-critical adversarial reader (*Democracy in Chains* tradition)
3. Resource-extraction-industry-funded reviewer (Coal Council / API / NMA / industry-funded think tank)
4. Climate-denier-policy-cluster adversarial reader (CEI / Heritage climate-policy cluster)
5. Free-market-environmental adversarial (Coase / pure-property-rights reader; PERC / Heartland)
6. Old-line public-sector IAM economist (Stern / Nordhaus tradition adversarial)
7. Hard-left anti-capital adversarial reader (Jacobin / Marxist-tradition cluster)
8. Right-populist adversarial reader (American Compass / JD-Vance-policy-cluster)

---

## §2. Per-character adversarial verdicts

### Character 1 — Libertarian Public Choice hostile reviewer (Cato / Mercatus / GMU)

**Verdict: ⚠⚠ EXCLUDE.** Reading C v3's open-question disclaimer at Ch 9:148 partially defuses the directional-prescription read, and the explicit B&T attribution + co-citation discipline at Ch 9:138, 144 preserves the scholarly-bridge that Pass 3.3 Character 6 returned qualified ✓ INCLUDE on. But under hostile read, the chapter's Christophers public-ownership endorsement at Ch 9:168 re-arms the attack the open-question closing was designed to defuse: the framework substantively supports *"public ownership, public investment, and public-purpose criteria for capital allocation,"* which a libertarian hostile reviewer reads as the policy direction the decision-tool framing was alleged to merely "make possible."

**Hostile-read posture.** Reads for ideological commandeering of B&T canon; alert to cost-accounting frameworks implying more government intervention; scans the framework's policy implications for prescriptive-by-implication directional moves.

**Threads pulled.**

- **Ch 9:144 decision-tool framing — *"makes possible different decisions about future extraction by every party who was previously maximizing under incomplete cost-information — including the extractors themselves."*** Under hostile read this is prescriptive-by-implication: the framework's claim that complete cost-visibility *"makes possible different decisions"* is, in the libertarian hostile reviewer's reading, a directional claim (toward internalization / regulation / less extraction) the framework refuses to own explicitly.
- **Ch 9:168 Christophers paragraph — *"public ownership, public investment, and public-purpose criteria for capital allocation are not 'extreme'; they are what honest accounting requires when the price-and-profit gap is the structural problem the framework prices."*** Hostile reviewer reads this as the framework substantively endorsing the policy direction the decision-tool framing alleged to leave open. The framework's open-question closing at Ch 9:148 *"What the same extractor's reasoning produces under complete cost-visibility is a different question — and an open one"* is read as inconsistent with the Christophers-endorsement directionality.
- **Ch 9:206 rent-extractor cluster sector-naming — *"insurance, pharmaceutical, private-education-finance, student-loan-servicing — that captures the value public provision would have absorbed."*** Hostile reviewer reads this as left-policy targeting; the *"structural observation, not advocacy"* disclaimer at Ch 9:208 cannot neutralize the directional-targeting that explicit sector-naming carries.
- **Ch 9:110 deadweight-loss reframe — *"The ten to fifteen trillion dollars per year of severed costs that Chapter 8 identified are not a deadweight loss. They are a wealth transfer."*** Hostile reviewer reads this as displacement of Tullock's deadweight-loss analysis with a redistributive framing the libertarian wing rejects.

**Chapter's structural moves that disarm.**

- **Ch 9:148 explicit open-question closing.** *"What the same extractor's reasoning produces under complete cost-visibility is a different question — and an open one."* Partial defuse; the framework leaves the directional question open at the section's last word.
- **Ch 9:138–140 Buchanan + Tullock + six-decade-lineage attribution.** *"founded by James M. Buchanan and Gordon Tullock at Virginia and developed over six decades by their successors"* — full lineage-naming credit; no faint-praise framing.
- **Ch 9:144 positive co-citation — *"should read Buchanan and Tullock alongside this book."*** Explicit recommendation hostile reviewer must engage rather than dismiss.
- **Ch 9:158 + 166 property-rights honoring — *"The framework does not deny any of this. It agrees, in fact, with most of it. Property rights do extraordinary work for a specific class of resources... This is not a refutation of property rights."*** Domain-bounded scope-discipline preserves the bridge.
- **Ch 9:208 structural-observation-not-advocacy disclaimer.**

**Net read.** The open-question closing + property-rights honoring + B&T scholarly-bridge work survive at the structural-move level; the Christophers public-ownership endorsement + sector-naming + deadweight-loss-reframe re-arm the hostile-read attack. The framework's actual direction (toward visibility-of-costs that the framework substantively believes will produce internalization, even as it disclaims advocating for it) is legible to a hostile reviewer who reads for direction. ⚠⚠ EXCLUDE: would actively reject; finds load-bearing thread (decision-tool framing implies prescriptive direction) the framework's open-question disclaimer partially defuses but does not eliminate.

---

### Character 2 — MacLean-sympathetic Buchanan-critical adversarial reader (*Democracy in Chains*)

**Verdict: ⚠⚠ EXCLUDE.** Reading C v3's *"the angles are not symmetric"* + *"Public Choice supplied the vocabulary for analyzing the extractor's reasoning"* framing carries implicit distance from Buchanan's broader political project. But under hostile read, the absence of explicit MacLean engagement + the explicit *"should read Buchanan and Tullock alongside this book"* recommendation at Ch 9:144 + the explicit AEI / Cato / Mercatus / GMU audience-courting at Ch 9:148 read as the framework either unaware of or evading the *Democracy in Chains* controversy. A MacLean-sympathetic reader carrying the controversy at the front of their attention finds load-bearing thread the asymmetric framing's implicit-distance cannot disarm.

**Hostile-read posture.** Reads Buchanan's Virginia-school Public Choice as rooted in 1950s segregationist-school-funding resistance + designed to insulate concentrated wealth from democratic accountability per MacLean's *Democracy in Chains* (2017). Rejects any framework that recommends "reading Buchanan and Tullock alongside this book" as papering over Buchanan's contested political project. Demands explicit engagement with the controversy.

**Threads pulled.**

- **Ch 9:144 explicit B&T co-citation recommendation — *"A reader who wants to understand how rent-seeking-shaped architectures come to be... should read Buchanan and Tullock alongside this book."*** Under hostile read this is the framework recommending the Virginia-school canon without engaging the political-project contestation MacLean's reading turns load-bearing.
- **Ch 9:148 explicit audience-courting — *"The practical implication for readers in the policy-economy traditions Public Choice has shaped — readers at AEI, Cato, the Mercatus Center, George Mason economics, and the broader policy-think-tank cluster influenced by Virginia-school analysis — is that the framework here is not a competitor for the analytical space they occupy. It is the ledger..."*** Hostile reviewer reads this as the framework courting the Virginia-school-aligned policy cluster without acknowledging the cluster's contested political genealogy.
- **Ch 9:138–148 absence of MacLean engagement.** No reference to *Democracy in Chains*; no acknowledgment of the controversy; no discussion of segregationist-funding-resistance origins; no acknowledgment of contested-political-project framing.
- **Ch 9:138 Tullock 1967 *"Welfare Costs of Tariffs, Monopolies, and Theft"* anchoring.** Hostile reviewer reads as confirmation that the framework treats the Virginia-school canon as canonical-methodology-source without engaging the political-project critique.

**Chapter's structural moves that disarm.**

- **Ch 9:144 *"the angles are not symmetric"* asymmetric framing.** *"Public Choice supplied the vocabulary for analyzing the extractor's reasoning; the framework supplies the accounting that changes what the extractor is reasoning about."* Carries implicit distance: the framework takes methodology, not political project.
- **Chapter-wide structural-injustice framing.** Niger Delta + Baotou + DRC cost-bearers at Ch 9:90–94; *"is a number"* four-fold at Ch 9:142; *"cost column borne by communities that did not negotiate the terms of the architecture absorbing them"* at Ch 9:142; reparations-economics implicit lineage (named at Ch 8:122 post-cascade) — the chapter's politics are substantively opposed to the political project MacLean attributes to Buchanan.
- **Ch 9:148 closing aphorism — *"Someone designed it, and we can identify them, in Public Choice's idiom; the ledger then shows what they designed has been costing, and to whom, in the framework's."*** Frames Public Choice as upstream-articulation; the framework's downstream-accounting work has different political direction than B&T's.

**Net read.** Implicit distance via asymmetric framing + chapter-wide structural-injustice politics carry at the substantive-direction level; but the explicit B&T recommendation + AEI / Cato / Mercatus / GMU audience-courting + absence of any MacLean engagement read as procedural blindness to the controversy. ⚠⚠ EXCLUDE: would actively reject; finds load-bearing thread (insufficient distance from Buchanan's broader project) that asymmetric framing does not fully disarm. **Note: this thread is procedurally spot-fixable** — Pass 3.3 Character 15 Option A (one sentence acknowledging methodological-vs-political distinction) would disarm without damaging acceptance verdicts; see §3 below.

---

### Character 3 — Resource-extraction-industry-funded reviewer (Coal Council / API / NMA / industry-funded think tank)

**Verdict: ⚠⚠⚠ EXCLUDE.** Industry-funded reviewer is predisposed-hostile by financial-incentive: the framework's apparatus IS the threat to their funders. Chapter does not try to land this reader and cannot land them without abandoning the book's purpose. This is the canonical non-chapter-disarmable predisposed-hostile-by-financial-incentive case per Ch 1 REAUDIT v3 §5.3 framing; mitigation is reception-cycle level (supportive reception from non-hostile venues offsets industry-funded hostility — a normal cost of doing structural-economic-critique work).

**Hostile-read posture.** Pressure-tests foundational cost-attribution claims (does the 13-year life-expectancy gap actually attribute to coal industry vs. confounders); pressure-tests per-ton arithmetic; pressure-tests "subsidy" framing as legitimate-pricing-of-externalities-in-different-political-architecture; rejects structural-injustice frame entirely; advocates for industry-friendly cost-accounting.

**Threads pulled.**

- **Ch 9:12 + 116 cost-attribution math — *"one ton of McDowell County coal, sold at the mine mouth in 1960 for four dollars and fifty cents, actually cost — conservatively, floor-estimated, cost-component by cost-component — somewhere between five hundred and six hundred dollars when every severed cost was priced honestly."*** Hostile reviewer demands the cost-attribution math: does the 13-year life-expectancy gap actually attribute to coal industry, or to confounders (smoking, diet, deprivation-independent-of-coal, in-migration / out-migration selection bias)?
- **Ch 9:92–94 international cost attributions — Niger Delta + Baotou + DRC.** Hostile reviewer demands each attribution be defensible against industry-funded counter-narratives.
- **Ch 9:142 *"is a number"* four-fold.** Hostile reviewer pressure-tests each: McDowell's life-expectancy gap (attribution contested); Niger Delta mangrove (spillage attribution to specific operators contested); Baotou tailings (radioactive-slurry sourcing claims contested); 2008 foreclosures (causation between financial sector and household-debt distress contested by financial-services industry-funded research).
- **Ch 9:118 *"subsidies have constituencies on both sides... 'The coal industry extracted approximately $550 per ton of value in unpriced damage while selling the coal for $40' is a sentence that describes a subsidy."*** Hostile reviewer reframes as subsidy-vs-pricing-of-externalities-in-different-political-architecture; the $550 figure is contested IAM-modeling territory.
- **Ch 9:240 reclamation-bond framing — *"structurally underpriced... bankruptcy-driven transfer of liability to the public."*** Hostile reviewer reads as left-policy assault on extractive-industry economic structure.

**Chapter's structural moves that disarm.**

- **Cross-chapter reliance.** Chapter explicitly relies on Ch 8 for the $550/ton arithmetic; Ch 9 is the policy-architecture chapter, not the case-walk chapter. Ch 8 Pass 1 + Pass 2 + Stage 1c Phase C addressed cost-attribution precision (commit `cbef9bd` + earlier Pass-1/Pass-2 Phase C commits).
- **Ch 9:208 structural-observation-not-advocacy disclaimer.**
- **Ch 9:244 explicit acknowledgment — *"Each of these is a partial, imperfect, politically achievable implementation of one slice."*** Chapter doesn't claim foundational-arithmetic perfection.
- **Ch 9:256–260 framework-not-blueprint discipline — *"This is not a legislative blueprint. It is a framework."*** Chapter explicitly disclaims policy-prescription scope.

**Net read.** Industry-funded hostile reviewer would write a hostile review regardless of chapter structural moves; the chapter's framework-promise IS the threat to their funders. ⚠⚠⚠ EXCLUDE: would weaponize chapter against itself by demanding each cost-attribution claim survive industry-funded counter-narratives; will publish in industry-aligned venue (Heritage Foundation Backgrounder / *RealClearEnergy* / industry-association policy paper). Not chapter-disarmable; reception-cycle mitigation only.

---

### Character 4 — Climate-denier-policy-cluster adversarial reader

**Verdict: ⚠⚠ EXCLUDE.** Chapter's Reassess step at Ch 9:80–82 + quantification of type-1 over-reservation cost as "small" at Ch 9:50 + explicit acknowledgment that carbon-pricing prices are below SCC at Ch 9:230 are real structural moves; they hold against the hostile-read attack on the Asymmetric Regret Rule at the structural-move level. But the framework's externality-tail-unbounded category + biosphere-collapse framing at Ch 9:70 + dependence on SCC anchoring (Ch 9:230 + cross-reference to Ch 8 SCC sourcing) are load-bearing claims the climate-denier-policy-cluster reader will not concede; hostile read sticks because the reader's prior ideological commitment treats the framework's anchoring as fear-mongering.

**Hostile-read posture.** Rejects SCC framing (EPA 2023 + Rennert et al. 2022) as based on contested IAM modeling; rejects externality-tail-unbounded category as unfalsifiable / fear-mongering; pushes back on Asymmetric Regret Rule as one-sided risk-framing (counts type-2 errors of under-reservation but does not count type-1 cost of foregone economic development in present generations).

**Threads pulled.**

- **Ch 9:56 Asymmetric Regret Rule — *"If the reserve turns out to have been unnecessary... the cost was a modest amount of foregone revenue, distributed across a century, spread across the global economy. If the reserve turns out to have been necessary... the cost is civilizational. The first error is measured in dollars. The second is measured in possibilities foreclosed forever. When the insurance is cheap and the downside is unbounded, the rational move is obvious."*** Hostile reviewer reads as one-sided risk framing: type-1 cost is quantitatively bounded (foregone economic development); type-2 cost is framed as *"civilizational"* / *"possibilities foreclosed forever"* — a framing the climate-denier reader treats as unfalsifiable catastrophism.
- **Ch 9:68 renewable-research framing — *"Renewable substitution research is the only expenditure that simultaneously reduces present harm, future harm, and future need."*** Hostile reviewer reads as climate-policy advocacy embedded in framework.
- **Ch 9:70 biosphere framing — *"An asteroid has no communities bearing spatial cost severance. It has no ecosystems whose collapse cascades through a biosphere."*** Hostile reviewer reads *"biosphere collapse"* as climate-catastrophism.
- **Ch 9:230 carbon-pricing framing — *"the prices, in most cases, are below the social cost of carbon as estimated by every major economic body that has tried to estimate it."*** Hostile reviewer reads SCC framing as based on contested IAM modeling; the *"every major economic body"* gesture is read as appeal-to-consensus rather than substantive engagement.
- **Ch 9:234 CCZ framing — *"externality-tail-unbounded category."*** Hostile reviewer reads *"unbounded"* as unfalsifiable.

**Chapter's structural moves that disarm.**

- **Ch 9:56 ARR names both error types.** *"If the reserve turns out to have been unnecessary..."* — chapter does name the type-1 over-reservation case; the framework's valuation of the two errors is asymmetric (the framework's claim) but its acknowledgment is symmetric (the structural disarm).
- **Ch 9:80–82 Reassess step.** *"A resource classified today as high-existential-substitutability-gap may become low-existential-substitutability-gap in thirty years if a substitutability breakthrough matures... When that happens, the reserved fraction can be reclassified. Some of it may be released to the extraction market."* Explicitly accounts for type-1 over-reservation correction; reserved fractions are not irrevocable.
- **Ch 9:50 type-1 cost quantified — *"designating twenty percent of reserves as strategic — six million tons, twenty years of current production held in reserve — costs essentially nothing in the near term."*** Chapter shows type-1 cost is small in expectation under reasonable parameters.
- **Ch 9:230 SCC framing honest about contested-status — *"the prices, in most cases, are below the social cost of carbon."*** Chapter acknowledges the SCC critique honestly.

**Net read.** Chapter's structural moves at the ARR + Reassess level hold; hostile reviewer cannot disarm the chapter at structural-claim level. But the climate-denier-policy-cluster reader's prior ideological commitment treats the SCC anchoring + externality-tail-unbounded category + biosphere framing as fear-mongering; hostile read sticks at the framing-rejection level. ⚠⚠ EXCLUDE: would actively reject; finds load-bearing thread (ARR + SCC anchoring) the chapter's structural moves engage but cannot eliminate at the ideological-commitment level.

---

### Character 5 — Free-market-environmental adversarial (Coase / property-rights-only; PERC / Heartland)

**Verdict: ⚠ EXCLUDE.** Chapter's three-exceptions argument at Ch 9:160–164 is precisely the kind of intellectually-serious property-rights pushback this reader would engage at scholarly-disagreement level; chapter's domain-bounded framing at Ch 9:166 + framework-as-supplement-not-replacement framing hold against the hostile read. Hostile reviewer would publish a critical review but at scholarly-disagreement-within-shared-domain level, not chapter-disqualification level.

**Hostile-read posture.** Pushes back on each of the framework's three property-rights exceptions; argues each is technically resolvable within the property-rights tradition; reads the framework's *"supplement, not replacement"* framing as conceding the PERC argument without acknowledging it.

**Threads pulled.**

- **Ch 9:160 intergenerational foreclosure — *"Property rights are held by living agents. Future generations hold no deeds, sign no contracts, cannot participate in the bargaining Coase described, and cannot bid against current uses of a finite stock."*** Hostile reviewer pushes back: future generations can be represented by current owners' bequest motives (Cowen, Caplan tradition); property-rights tradition has bequest-motive answers; the chapter's *"if those future humans mattered they would bid — and the absence of their bid is taken as evidence that they do not matter at the margin"* is a strawman of the bequest-motive argument.
- **Ch 9:162 transboundary externality — *"Property rights work when the property owner bears the costs and benefits of the asset's use. They work less well when the costs escape the property line."*** Hostile reviewer pushes back: border-adjustment can extend property rights to transboundary cases — the chapter's own example (CBAM at Ch 9:98) is a property-rights extension, not a property-rights critique. Acid mine drainage / atmospheric carbon / aquifer depletion can be addressed through harmonization-of-property-rights regimes.
- **Ch 9:164 information asymmetry at civilizational scale — *"Property markets price what participants currently know. They do not price what we will discover we needed only after the resource is gone."*** Hostile reviewer pushes back: futures markets price expected discoveries; option-value pricing accommodates information asymmetry; insurance markets price tail-risk routinely.
- **Ch 9:166 supplement-not-replacement framing — *"The residual commons value framework is the supplement, not the replacement."*** Hostile reviewer reads as concession of the PERC argument without acknowledging it.

**Chapter's structural moves that disarm.**

- **Ch 9:158 explicit property-rights honoring — *"The framework does not deny any of this. It agrees, in fact, with most of it. Property rights do extraordinary work for a specific class of resources — those that are rivalrous, excludable, and valued mostly in the present tense. For those resources, the price system aggregates dispersed information and incentivizes stewardship far better than any central planning alternative."*** Substantive honoring of the property-rights tradition; not strawman dismissal.
- **Ch 9:166 domain-bounded scope-discipline — *"This is not a refutation of property rights. It is an identification of the domain within which they are complete and the domain within which they are not. For most goods, property rights are the right tool and we should leave them alone."*** Frames the three exceptions as domain-bounded, not as refutation.
- **Ch 9:160 irreversibility argument — *"Substitutability, stock depletion, and irreversibility are real constraints whether or not anyone alive today chooses to price them, and a pricing system that ignores them is not 'efficient' in any defensible sense; it is incomplete."*** Pre-empts the bequest-motive answer by naming structural irreversibility (not just intergenerational preference-revelation).
- **Ch 9:162 accounting-tool framing — *"The residual commons value framework is, at its core, a systematic accounting of the leakage — the component of value that cannot be captured by any single property owner because it is held in common by everyone downstream, downwind, and downstream in time."*** Frames the framework as accounting, not as policy-prescription / property-rights-replacement.
- **Ch 9:170 Adam Smith framing — *"It is not a departure from the market mechanism. It is the completion of it."*** Explicitly inside-the-tradition framing.

**Net read.** Free-market-environmental hostile reviewer would publish a critical review but the critique would operate within shared scholarly-disagreement-within-domain framing rather than chapter-disqualification. Hostile reviewer's pushback on each exception is exactly the kind of conversation the chapter invites with its domain-bounded framing. ⚠ EXCLUDE: would push back but chapter holds against the pushback; thread is acknowledged.

---

### Character 6 — Old-line public-sector IAM economist (Stern / Nordhaus tradition adversarial)

**Verdict: ⚠⚠ EXCLUDE.** Chapter's open-question closing at Ch 9:148 + structural-observation-not-advocacy disclaimer at Ch 9:208 + Ch 6 methodology-grounding cross-reference work at the structural-move level. But under hostile IAM-tradition read, the framework's decision-tool widening at Ch 9:144 reads as overclaiming relative to what the framework actually delivers (cost-visibility without incentive-structure / regulatory-architecture); the absence of Stern / Nordhaus / Savage / Loomes & Sugden citations in Ch 9 itself reinforces the overclaim read. The hostile IAM reader pressure-tests the chapter for what the framework's apparatus *actually* predicts versus what it claims to *make possible*.

**Hostile-read posture.** Pressure-tests decision-tool framing as overclaiming; pushes back on *"extract from the lowest-RCV source first"* framing (Ch 9:72) as requiring policy intervention the framework disclaims attempting; pressure-tests ARR grounding (Savage 1951 minimax-regret; Loomes & Sugden 1982 regret-theory) as extension-without-citation.

**Threads pulled.**

- **Ch 9:144 decision-tool widening — *"The framework is both a measurement tool and a decision tool. It counts the costs of past and ongoing extraction; it also makes possible different decisions about future extraction by every party who was previously maximizing under incomplete cost-information — including the extractors themselves."*** IAM-tradition hostile reviewer reads as overclaiming: the framework supplies cost-visibility but does not actually predict different decisions absent changed incentive structure / regulatory architecture. The framework names what *could* change, not what *will* change; calling that a *"decision tool"* claims more than the apparatus delivers.
- **Ch 9:72 lowest-RCV-source-first framing — *"It says extract from the lowest residual commons value (RCV) source first."*** IAM-tradition hostile reviewer reads as decision-rule that requires policy implementation the framework disclaims at Ch 9:208 (*"structural observation, not advocacy"*); tension between derived decision-rule and disclaimed-advocacy.
- **Ch 9:56 ARR methodology grounding gap.** Asymmetric Regret Rule deployed without explicit Savage 1951 / Loomes & Sugden 1982 citation; hostile reviewer reads as extension-without-citation that overclaims methodological inheritance.
- **Ch 9:234–236 CCZ derived-position-then-disclaimed — *"Asymmetric-regret reasoning under these parameters produces a clear preserve-and-study verdict... The framework is structural-observational here, not prescriptive."*** Hostile reviewer reads as the chapter deriving a substantive policy implication from its own apparatus + then disclaiming the implication; the tension reads as evasion of the analytical conclusion.

**Chapter's structural moves that disarm.**

- **Ch 9:148 open-question closing — *"What the same extractor's reasoning produces under complete cost-visibility is a different question — and an open one."*** Explicit acknowledgment that the framework's apparatus does not deliver a complete decision theory.
- **Ch 9:208 structural-observation-not-advocacy disclaimer.**
- **Ch 9:236 explicit derived-vs-prescriptive framing — *"The framework is structural-observational here, not prescriptive. It does not take a position on the mining decision. It reads the case the way it reads any extraction case..."*** Chapter does name the tension between derived-position and disclaimed-prescription.
- **Cross-chapter methodology grounding.** Chapter explicitly relies on Ch 6 for ARR + CIT + Three Ways of Counting + Hotelling Identity methodology (per Pass 3.3 Character 16 acceptance verdict).
- **Ch 9:184 historical-contingency framing.** *"Yes, specific decision points have passed. Yes, the conditions that would have produced different outcomes at those decision points have changed."* Chapter is honest about what decisions the framework's apparatus does and does not predict.

**Net read.** IAM-tradition hostile reviewer accepts the framework's apparatus as substantive contribution but pressure-tests the *"decision tool"* framing at Ch 9:144 as overclaim. Open-question closing partially defuses but the decision-tool framing carries the load-bearing claim that complete cost-visibility *"makes possible different decisions"* — which the IAM tradition reads as either (a) trivially true (information-without-incentive-change rarely changes behavior) or (b) directional-by-implication (the framework expects different decisions, even as it disclaims predicting them). Methodology-grounding gap (no Savage / Loomes & Sugden citations) reinforces overclaim read. ⚠⚠ EXCLUDE: would actively reject; finds load-bearing thread (decision-tool framing overclaims relative to delivered apparatus) the chapter's structural moves partially but not fully defuse.

---

### Character 7 — Hard-left anti-capital adversarial reader (Jacobin / Marxist-tradition cluster) **(optional)**

**Verdict: ⚠⚠ EXCLUDE.** Chapter's Christophers public-ownership endorsement at Ch 9:168 + named class-power dynamic at Ch 9:110–118 + rent-extractor-cluster sector-naming at Ch 9:206 reach substantively further-left than the natural-fit Pass 3.3 acceptance verdict (Character 14 ✓✓ INCLUDE) would suggest from the framing alone. But under hostile hard-left read, the Adam Smith *"completion of the market mechanism"* framing at Ch 9:170 + structural-observation-not-advocacy discipline at Ch 9:208 + Reading C v3 engagement with Public Choice tradition + framework-as-measurement-AND-decision-tool framing at Ch 9:144 read as ideological accommodation of capital that lets the actual class-power dynamic escape into impartial-accounting framing.

**Hostile-read posture.** Rejects continued engagement with market mechanisms + Public Choice tradition as accommodation rather than confrontation; pushes back on *"completion of the market mechanism"* close as ideological accommodation of capital; argues structural-observation discipline lets the actual class-power dynamic escape into impartial-accounting framing.

**Threads pulled.**

- **Ch 9:170 Adam Smith framing — *"Adam Smith, who spent a good portion of *The Wealth of Nations* arguing against producers who externalized costs onto the public, would have recognized what this framework does. It is not a departure from the market mechanism. It is the completion of it."*** Hard-left hostile reviewer reads as ideological accommodation of capital; framework is bolstering the market mechanism rather than confronting capital. The Adam-Smith-as-progenitor framing is read as canonical-economics-history move that papers over the political-economy critique Marxist tradition demands.
- **Ch 9:138–148 Reading C v3 Public Choice engagement.** Hard-left hostile reviewer reads engagement with Public Choice tradition (founded by the figure MacLean traces to segregationist-school-funding resistance) as accommodation rather than confrontation; the asymmetric framing is read as polite handshake with the tradition rather than direct critique.
- **Ch 9:168 Christophers reframe — *"Christophers names the why; the framework names the how-to-see-it."*** Hard-left hostile reviewer reads as separating diagnosis from political action; framework refuses to take the political-economic action Christophers' diagnosis demands.
- **Ch 9:208 structural-observation-not-advocacy disclaimer.** Hard-left hostile reviewer reads as deliberate disavowal of political work; framework refuses to advocate even where its own apparatus would demand advocacy (the CCZ preserve-and-study verdict at Ch 9:234, then disclaimed at Ch 9:236, is the case-study).
- **Ch 9:144 framework-as-measurement-AND-decision-tool framing.** Hard-left hostile reviewer reads *"the extractors themselves"* as accommodation of extractor agency rather than confrontation of extractor power; the framework gives extractors more information without demanding they cease extraction.

**Chapter's structural moves that disarm.**

- **Ch 9:168 Christophers public-ownership endorsement — *"public ownership, public investment, and public-purpose criteria for capital allocation are not 'extreme'; they are what honest accounting requires when the price-and-profit gap is the structural problem the framework prices."*** Substantive endorsement of public-ownership / public-investment / public-purpose criteria; framework is not market-fundamentalist.
- **Ch 9:142 *"is a number"* four-fold + cost-bearer-centered framing — *"the cost column borne by communities that did not negotiate the terms of the architecture absorbing them, the cost column borne by future generations who cannot vote, the cost column borne by ecosystems whose recovery timescales exceed the relevant political horizon."*** Centers cost-bearer realities; aligns substantively with anti-capital cost-bearer framing.
- **Ch 9:110–118 Mancur Olson engagement + named class-power dynamic.** *"The beneficiaries are concentrated, organized, well-represented in every jurisdiction that matters, and capable of deploying resources in defense of the arrangement. The bearers of severed costs... are diffuse, unorganized, and, in the case of the unborn, entirely unrepresented."* Chapter names class-power dynamic explicitly; not hidden.
- **Ch 9:206 rent-extractor-cluster sector-naming — *"insurance, pharmaceutical, private-education-finance, student-loan-servicing."*** Names specific extractor classes; direct structural-critique.
- **Ch 9:122–130 2008 financial-crisis architecture critique.** Mian & Sufi *House of Debt* engagement; explicit reading of bank-rescue-architecture as concentrated-beneficiary-political-economy choice.

**Net read.** Hard-left hostile reviewer reads *"completion of the market mechanism"* framing at Ch 9:170 as ideological accommodation despite the chapter's substantive endorsement of public ownership / public investment / public-purpose criteria at Ch 9:168. The Christophers endorsement + named class-power dynamic + sector-naming + 2008-architecture critique do real work to defuse the hard-left hostile read, but the structural-observation-not-advocacy discipline + Adam Smith framing reach a point where the hard-left tradition cannot follow without abandoning its political-economy commitments. ⚠⚠ EXCLUDE: would actively reject; finds load-bearing thread (ideological accommodation of capital) the chapter's substantive moves cannot fully disarm at the political-tradition level. **Note: spot-fix would damage Pass 3.3 Character 14 natural-fit verdict AND Pass 3.3 Character 6 libertarian-PC qualified-INCLUDE verdict.** See §3 thread T7.

---

### Character 8 — Right-populist adversarial reader (American Compass / JD-Vance-policy-cluster) **(optional)**

**Verdict: ⚠ EXCLUDE.** Chapter's Nordic-objection four-condition steelman at Ch 9:178 + sub-national-implementation argument at Ch 9:182 + Chattanooga foregrounding at Ch 9:222 are precisely the kind of structural disarm moves a right-populist reader would register as the chapter taking the foreign-model objection seriously. Hostile reviewer pushes back on European-comparator framing but at scholarly-disagreement level not chapter-disqualification level. Pass 3.3 Character 8 (American center-right policy reader) returned ✓ INCLUDE on this very basis; the adversarial-direction read tightens the verdict by one increment but does not flip the disarm.

**Hostile-read posture.** Pushes back on transboundary-cost-severance + border-adjustment framing as globalist; on Sweden comparator as foreign-model importation; on Mondragon / Vienna / Saltsjöbaden case-bank as European-model importation that doesn't honor American-specific institutional traditions.

**Threads pulled.**

- **Ch 9:100 border adjustment — *"A generalized border adjustment — scaled to existential substitutability gap, applied to a widening set of resource categories as the classification matures — is the international-dimension analog of what national pricing does domestically."*** Right-populist hostile reviewer reads as globalist economic architecture proposal.
- **Ch 9:198 Sweden comparator — *"Americans pay nearly as much as Swedes in total tax burden and receive almost none of it back as guaranteed services."*** Right-populist hostile reviewer reads as foreign-model comparator; Sweden as European-social-democratic ideal that Americans should aspire to.
- **Ch 9:222–226 Chattanooga + Mondragon + Vienna case-bank.** Right-populist hostile reviewer reads Mondragon (Basque cooperative) + Vienna (Austrian municipal) as European-model importation alien to American institutional tradition.
- **Ch 9:126–128 Saltsjöbaden 1938 framing.** Swedish labor-bargaining as policy template.
- **Ch 9:182 sub-national-implementation framing — *"Every Nordic welfare-state feature has U.S.-domestic partial implementations at state or municipal scale."*** Right-populist hostile reviewer pressure-tests whether the partial-implementations actually exist or whether the framing is rhetorical move to avoid the foreign-model objection.

**Chapter's structural moves that disarm.**

- **Ch 9:182 sub-national-implementation argument.** Medicare + Medicaid + Massachusetts / California / Washington healthcare + Alaska Permanent Fund + Mitchell-Lama (NYC) + Montgomery County Housing Opportunities Commission — chapter explicitly names U.S.-domestic implementations.
- **Ch 9:184 demographic-homogeneity pressure-test.** *"On demographic homogeneity, the steelman's strongest claim. Three responses pressure-test the claim."* Chapter explicitly engages the steelman + offers three responses.
- **Ch 9:186 resource-base pressure-test.** *"The U.S. has a different but equivalent revenue base... The constraint is not revenue-generation capacity; it is political will to direct revenue to public provision."* Chapter explicitly engages U.S.-vs-Norway revenue-base difference.
- **Ch 9:188 historical-contingency pressure-test.** *"Yes, specific decision points have passed."*
- **Ch 9:222 Chattanooga anchoring — *"In Chattanooga, Tennessee — in the heart of the kind of political economy where the framework is supposed to be impossible — the municipally owned electric utility EPB..."*** Chapter pre-empts the foreign-model objection by foregrounding the American case.
- **Ch 9:218 + Alaska Permanent Fund anchoring.** American sovereign-wealth-fund existence-proof.

**Net read.** Right-populist hostile reviewer pushes back on European-comparator framing but the chapter's explicit Nordic-objection four-condition steelman + sub-national-implementation argument + Chattanooga foregrounding hold against the pushback. Thread is acknowledged. The chapter does not abandon European examples but does anchor them within American-domestic-implementation framing. ⚠ EXCLUDE: would push back but chapter holds against the pushback. Hostile reviewer would publish critical review but at scholarly-disagreement-within-shared-domain level not chapter-disqualification level.

---

### §2.x — Per-character verdict tally

| Character | Verdict | Type |
|---|---|---|
| 1 — Libertarian Public Choice hostile reviewer | ⚠⚠ EXCLUDE | Active rejection; load-bearing thread (T1 + T2) |
| 2 — MacLean-sympathetic Buchanan-critical | ⚠⚠ EXCLUDE | Active rejection; procedurally-spot-fixable thread (T3) |
| 3 — Resource-extraction industry-funded | ⚠⚠⚠ EXCLUDE | Predisposed-hostile-by-financial-incentive; non-chapter-disarmable |
| 4 — Climate-denier-policy-cluster | ⚠⚠ EXCLUDE | Active rejection; load-bearing thread (T5) at ideological-commitment level |
| 5 — Free-market-environmental (Coase) | ⚠ EXCLUDE | Acknowledged thread; chapter holds (T4) |
| 6 — IAM-tradition (Stern / Nordhaus) | ⚠⚠ EXCLUDE | Active rejection; load-bearing thread (T1 + methodology-grounding) |
| 7 — Hard-left anti-capital (optional) | ⚠⚠ EXCLUDE | Active rejection; load-bearing thread (T7) at political-tradition level |
| 8 — Right-populist (optional) | ⚠ EXCLUDE | Acknowledged thread; chapter holds (T6) |

**All 8 EXCLUDE as expected per template verdict-floor.** Per-character verdicts are inputs to the §3 thread-pull synthesis, not the diagnostic itself.

---

## §3. Thread-pull synthesis (the central diagnostic)

Per canonical [Ch 1 REAUDIT v3 §5.3](commons_bonds_ch1_stage_3_pass_3_audience_load_REAUDIT_2026-05-17_PROPOSED.md) format. Threads found, ranked by adversarial-character pull-frequency. Pre-populated threads (T1–T7 from framing) confirmed below; one additional thread (T8) surfaced during the audit.

| Thread | Pulled by adversarial chars # | Type | Recommendation |
|---|---|---|---|
| **T1.** Decision-tool framing at Ch 9:144 implies prescriptive direction. *"Makes possible different decisions about future extraction by every party who was previously maximizing under incomplete cost-information — including the extractors themselves."* Under hostile read, the framework's claim that complete cost-visibility *"makes possible different decisions"* is read as directional-by-implication (toward internalization / regulation); the open-question closing at Ch 9:148 partially defuses but Christophers public-ownership endorsement at Ch 9:168 re-arms the attack. | Char 1 (libertarian PC); Char 6 (IAM-tradition); Char 7 (hard-left, in inverted form — reads as insufficient direction) | **Load-bearing chapter claim.** Decision-tool framing IS the substantive contribution of Reading C v3 (canonical per author ratification 2026-05-21). Spot-fixing toward weaker framing would damage Pass 3.3 Character 3 (environmental-economics ✓✓), Character 5 (Lindsey & Teles center-left PC ✓✓), Character 14 (left-progressive natural-fit ✓✓) acceptance verdicts. The cross-pressure structure (Char 1 reads as too-much-direction; Char 7 reads as too-little) is the canonical sign of a load-bearing claim positioned correctly in the political-economy debate. | **HOLD.** Open-question closing at Ch 9:148 + structural-observation-not-advocacy disclaimer at Ch 9:208 provide structural disarm; acknowledge thread in pre-pub review queue. |
| **T2.** Rent-extractor cluster sector-naming at Ch 9:206 reads as left-policy targeting. *"Insurance, pharmaceutical, private-education-finance, student-loan-servicing — that captures the value public provision would have absorbed."* | Char 1 (libertarian PC); Char 3 (industry-funded); Char 8 (right-populist) | **Load-bearing chapter claim.** Pass 3.3 §5.3 already flagged that softening risks Pass 3.3 Character 14 (natural-fit ✓✓) verdict. Sector-naming is substantive structural-observation about which actors capture the value the eleven-cent gap routes through; the chapter's structural-observation discipline depends on naming the architecture concretely. | **HOLD.** Structural-observation-not-advocacy disclaimer at Ch 9:208 + eleven-cent framing as *"Americans already pay comparable tax burden"* (Ch 9:206) rather than *"Americans should pay more"* provide structural disarm. Acknowledge in pre-pub review queue. |
| **T3.** Buchanan implicit endorsement insufficient at Ch 9:144. *"Should read Buchanan and Tullock alongside this book"* recommendation + absence of explicit MacLean (*Democracy in Chains*) engagement. | Char 2 (MacLean-sympathetic) | **Procedural / cosmetic flag.** Spot-fixable. Pass 3.3 Character 15 returned ✓ INCLUDE with optional Option A flagged (one sentence acknowledging methodological-vs-political distinction); Pass 3.4 confirms the optional spot-fix would disarm the hostile read without damaging acceptance verdicts. | **SPOT-FIX (optional; author judgment).** Pass 3.3 Character 15 Option A: one sentence at Ch 9:144 or 148 acknowledging that *"the rent-seeking analytical vocabulary survives many readings of Buchanan's broader political project, and this book draws on the vocabulary rather than endorsing the project."* Alternative: HOLD per Pass 3.3 §5.3 default (asymmetric framing carries implicit distance + chapter-wide structural-injustice politics provide substantive distance). Author judgment. |
| **T4.** Three property-rights exceptions at Ch 9:160–164 resolvable within Coase tradition. Bequest-motive answer to intergenerational foreclosure; border-adjustment / harmonization answer to transboundary externality; futures-markets / option-value answer to information asymmetry. | Char 5 (free-market-environmental) | **Load-bearing chapter claim.** Three-exceptions argument is the chapter's substantive engagement with the property-rights tradition; spot-fixing would damage Pass 3.3 Character 3 (environmental-economics ✓✓), Character 4 (Susskind / Christophers / Pistor-literate ✓✓), Character 16 (IAM-tradition ✓ acceptance verdict). | **HOLD.** Domain-bounded scope-discipline at Ch 9:166 (*"identification of the domain within which they are complete and the domain within which they are not"*) + framework-as-supplement-not-replacement framing + irreversibility-argument structural disarm at Ch 9:160 hold against the Coase-tradition pushback. Acknowledge in pre-pub review queue. |
| **T5.** Asymmetric Regret Rule at Ch 9:56 one-sided risk-framing. *"The first error is measured in dollars. The second is measured in possibilities foreclosed forever."* Read as catastrophism that counts type-2 errors but not type-1 over-reservation cost. | Char 4 (climate-denier); Char 6 (IAM-tradition; partial — reads as methodology-grounding gap) | **Load-bearing chapter claim.** ARR is the chapter's load-bearing risk-reasoning move; spot-fixing toward more-symmetric framing would damage Pass 3.3 Character 1 (trade-press ✓✓), Character 2 (policy reader ✓✓), Character 3 (environmental-economics ✓✓), Character 4 (Susskind / Christophers / Pistor ✓✓), Character 16 (IAM-tradition acceptance ✓, which returned INCLUDE precisely because ARR aligns with Stern's social-discount-rate position). | **HOLD.** Reassess step at Ch 9:80–82 explicitly accounts for type-1 over-reservation correction (reserved fractions can be reclassified + released); type-1 cost quantified as "small" at Ch 9:50; ARR explanation at Ch 9:56 names both error types. Structural disarm sufficient against intellectually-serious adversarial read; ideological-commitment-level rejection (Char 4) is not chapter-disarmable. Acknowledge in pre-pub review queue. |
| **T6.** Foreign-model importation at Ch 9:198 (Sweden comparator) + Ch 9:222–226 (Mondragon + Vienna) + Ch 9:126–128 (Saltsjöbaden). | Char 8 (right-populist) | **Load-bearing claim with structural disarm built in.** Chapter's Nordic-objection four-condition steelman at Ch 9:178 + sub-national-implementation argument at Ch 9:182 + Chattanooga foregrounding at Ch 9:222 are precisely the structural disarm moves Pass 3.3 Character 8 (American center-right) returned ✓ INCLUDE on. | **HOLD.** Structural disarm is sufficient; the chapter is explicitly defended against this thread. Acknowledge in pre-pub review queue. |
| **T7.** Ideological accommodation of capital at Ch 9:170. *"It is not a departure from the market mechanism. It is the completion of it."* + structural-observation-not-advocacy discipline at Ch 9:208 + Reading C v3 engagement with Public Choice tradition read as accommodation rather than confrontation. | Char 7 (hard-left, optional) | **Load-bearing chapter claim.** Adam Smith framing + completion-of-market-mechanism close is the chapter's load-bearing intellectual-history honesty move; spot-fixing would damage Pass 3.3 Character 6 (libertarian PC qualified-INCLUDE), Character 8 (American center-right ✓), Character 17 (fiscal-conservative ✓) acceptance verdicts. **The cross-pressure structure between T1 (libertarian-PC reads as too-much-direction) and T7 (hard-left reads as ideological accommodation) is the canonical sign that the chapter is positioned correctly in the political-economy debate — both directional adversaries find the chapter unsatisfying, which is the structural feature of a chapter that holds the ledger-discipline middle ground.** | **HOLD.** Christophers public-ownership endorsement at Ch 9:168 + named class-power dynamic at Ch 9:110–118 + rent-extractor-cluster sector-naming at Ch 9:206 + 2008-architecture critique at Ch 9:122–130 reach substantively further-left than the Adam-Smith framing alone suggests; framework is not market-fundamentalist. Acknowledge in pre-pub review queue; flag as a cross-chapter consideration for Ch 10 closing-reflection register (which forward-references the framework-as-honest-accounting close). |
| **T8.** Cost-attribution math foundations contested (NEW from audit). Industry-funded reviewer pressure-tests each cost-attribution claim against industry-funded counter-narratives: McDowell life-expectancy gap (confounder analysis); Niger Delta spillage operator-attribution; Baotou tailings sourcing claims; 2008 foreclosure causation. | Char 3 (industry-funded) | **Already-resolved-via-cross-chapter routing.** Chapter explicitly relies on Ch 8 for the $550/ton arithmetic; Ch 8 Pass 1 + Pass 2 + Stage 1c Phase C addressed cost-attribution precision (commits `cbef9bd` + earlier). Industry-funded reviewer is predisposed-hostile-by-financial-incentive (per Ch 1 REAUDIT v3 §5.3 canonical framing); not chapter-disarmable; mitigation is reception-cycle level. | **HOLD.** Cross-chapter routing is correct; Ch 8 carries the math; Ch 9 carries the policy-architecture. Acknowledge in pre-pub review queue + flag for reception-cycle mitigation note (supportive reception from non-hostile venues offsets industry-funded hostility). |

### §3.1 Synthesis observation: cross-pressure positions chapter correctly

The diagnostic value of running the full 8-character adversarial set is in the **cross-pressure structure** the synthesis reveals:

- **T1 cross-pressure.** Char 1 (libertarian PC) reads the decision-tool framing as *too-much* direction; Char 7 (hard-left) reads the same framing as *too-little* direction. Both adversarial reads point at the same chapter passage (Ch 9:144) from opposite ideological positions. **This is the canonical sign of a load-bearing claim positioned correctly in the political-economy debate** — a chapter whose framework is calibrated to the ledger-discipline middle ground will produce exactly this cross-pressure pattern.
- **T7 + T2 + T6 cross-pressure on the eleven-cent passage.** Char 1 + Char 3 + Char 8 read the rent-extractor-cluster sector-naming as left-policy targeting; Char 7 reads the same passage's structural-observation discipline as insufficient confrontation. Again: opposite-direction adversarial pressure on the same chapter passage; canonical sign of correct positioning.
- **T4 cross-pressure within the property-rights tradition.** Char 5 (free-market-environmental) reads the three exceptions as resolvable within Coase tradition; the inverse direction (a Marx-tradition Char 7) would read the exceptions as insufficient critique of property-rights tradition entirely. Chapter's domain-bounded framing at Ch 9:166 holds the middle.

Across the eight adversarial characters, **the chapter is not finding load-bearing threads that any single ideological tradition can weaponize against it.** The threads found are either (a) load-bearing claims the chapter is correctly making, with cross-pressure structure as the diagnostic confirmation; (b) procedurally-spot-fixable cosmetic flags (T3); or (c) industry-funded predisposed-hostility that is not chapter-disarmable (T8).

---

## §4. Apparatus / consistency / named-subject sub-checks

Pass 3.3 §3 verified apparatus + hyphenation + italicization disciplines all clean post-Pass-2 Phase C; Reading C v3 *"complete ledger"* vs *"honest ledger"* register substitution audience-load-clean; named-subject consent clean (public-record exception for cited scholars). Pass 3.4 incidental check:

- **§4.1 No new apparatus thread surfaced by adversarial set.** No adversarial character flagged a register / convention / named-subject thread the acceptance test missed.
- **§4.2 Adversarial-reviewer institutional affiliations cited via public-record exception.** Cato, Mercatus, GMU, AEI, Heritage, CEI, PERC, Heartland, American Compass, Jacobin, Stern, Nordhaus institutional affiliations cited in the framing context per [feedback_named_subject_consent.md](../memory/feedback_named_subject_consent.md) public-record exception (institutional positions stated on-the-record in the institutional capacity). No living-named-subject consent issue.
- **§4.3 Hard constraint honored.** Did NOT contact named subjects (including adversarial-reviewer institutional affiliations — public-record exception applies for citation but not for outreach per hard constraint).

---

## §5. Cross-chapter coherence sub-check

Pass 3.3 §4 verified Ch 8 → Ch 9 sequential-reader experience coherent post commit `cbef9bd`; Ch 5 + Ch 6 + Ch 7 + Ch 10 incidental sweep clean. Pass 3.4 incidental check for cross-chapter thread that adversarial-direction read surfaces:

- **§5.1 T7 (hard-left) Ch 10 closing-reflection touch.** Hard-left adversarial read flags Ch 9:170 *"completion of the market mechanism"* framing + Ch 9:208 structural-observation-not-advocacy discipline + Ch 9:290 forward-reference to Ch 10 (*"That is where the book goes from here"*). Ch 10 carries the closing reflection register; whether Ch 10's framework-as-honest-accounting close re-triggers the hard-left ideological-accommodation thread is a question Ch 10's own Pass 3.4 should pressure-test. Pass 3.3 §4.2 swept Ch 10 + Reading C v3 coherence at "no coherence issue surfaced"; Pass 3.4 confirms no new cross-chapter inconsistency specific to Ch 9 → Ch 10 sequential read, but flags T7 as a Ch 10 Pass 3.4 future-session input.
- **§5.2 T3 (MacLean) Stage 1c D-3 deferred sibling-coherence-check.** Per Stage 1c §8 deferred: Ch 5 + Tech Appendix §1.10 sibling-coherence-check. The rent-seeking-engagement workstream (commits `a1e54d9` → `bc02767`) inserted Public Choice engagement sections at Ch 5 + Ch 9 + TA §1.10; whether Ch 5 + TA §1.10 also operate without explicit MacLean engagement is a sibling-coherence question. If Ch 5 + TA §1.10 are also MacLean-silent, T3 might be best resolved at the cross-chapter level (one consolidated MacLean-acknowledgment note that applies to all three locations) rather than as a Ch 9-only spot-fix. **Not blocking Pass 3.4 verdict** — D-3 is already deferred per Stage 1c §8.
- **§5.3 T8 (cost-attribution) cross-chapter routing.** Industry-funded reviewer's cost-attribution pushback already routes to Ch 8 (which carries the math); Ch 9 is correctly scoped as policy-architecture chapter. No new cross-chapter incoherence; routing is correct.

---

## §6. Out-of-scope flagging

### §6.1 Cross-chapter cascade flags

- **T7 (hard-left) → Ch 10 Pass 3.4 future-session input.** Ch 10's closing reflection register touches the framework-as-honest-accounting close; Ch 10's Pass 3.4 should pressure-test whether the hard-left ideological-accommodation thread re-triggers there. **Not blocking Ch 9 Pass 3.4 verdict.**
- **T3 (MacLean) → Stage 1c D-3 deferred sibling-coherence-check.** If the deferred Ch 5 + TA §1.10 sibling-coherence-check fires, a consolidated MacLean-acknowledgment note across Ch 5 + Ch 9 + TA §1.10 may be more coherent than a Ch 9-only spot-fix. **Not blocking; not routing per pipeline doctrine §5 (no chapter-level structural revision needed; procedural-and-optional).**
- **T8 (industry-funded cost-attribution) — cross-chapter routing already correct.** Ch 8 carries the math; Ch 9 carries the policy-architecture; the cross-chapter cascade reconciliation Phase C (commit `9befb92`) already addressed Ch 8 MED-3 + MED-6 cost-attribution precision.

### §6.2 Stage 1c sibling-coherence-check follow-ups

Per Stage 1c §8 deferred:
- **D-2 (book-wide "honest" → "complete" sweep).** Pass 3.3 §4.3 verified Pass 3.4 does not surface new urgency for D-2 sweep; Ch 9's *"honestly"* verb-modifier uses are audience-load-defensible. Pass 3.4 confirms no adversarial character flagged the chapter's *"Pricing Honestly"* title + *"honestly"* verb-modifier uses as register-mismatch. D-2 remains deferred at separate-session pace.
- **D-3 (Ch 5 + TA §1.10 sibling-coherence-check).** Pass 3.3 §4.2 swept clean; Pass 3.4 surfaces T3 (MacLean) as a thread D-3 could consolidate cross-chapter if it fires. Not blocking; not routing.

### §6.3 Pass 3.5 (developmental-edit) future-session input

Per per-prompt serial cadence: Pass 3.5 fires after Pass 3.4 ratify-and-apply per [feedback_audience_aware_drafting_discipline.md](../memory/feedback_audience_aware_drafting_discipline.md) v3.0 Amendment B. Pass 3.4 incidental check for whole-chapter restoration-of-richness items surfaced by adversarial reads:

- **No cumulative-LLM-cadence residue surfaced.** Pass 2 Phase C compression (F-V7 + F-V12) + Reading C v3 substantive rewrite did not produce cumulative-flatness that adversarial reads detected.
- **No emotional-arc-continuity break surfaced.** Adversarial reads did not detect breaks in the chapter's expository-policy register; chapter holds voice across 294 lines.
- **No scene-anchor-density gap surfaced.** Adversarial reads operated at structural-claim level rather than scene-anchor level; chapter's case-bank (McDowell + Niger Delta + Baotou + DRC + Alaska + Norway + Chattanooga + Mondragon + Vienna + CCZ + Saltsjöbaden + 2008) is dense enough to carry the analytical load.
- **One incidental observation for Pass 3.5.** The eleven-cent-difference passage (Ch 9:192–208) is the chapter's analytically-densest passage; Pass 3.5 whole-chapter read should verify reader-engagement at this pivot does not flatten cumulatively when read after the Property-Rights + Nordic-Objection scholarly-engagement-heavy sections. Pass 3.4 does not surface a gap; flagged as low-priority Pass 3.5 attention item.

### §6.4 Pre-publication review queue items (Stage 5 input)

Per [feedback_audience_aware_drafting_discipline.md](../memory/feedback_audience_aware_drafting_discipline.md) v3.0 Pre-publication review queue: load-bearing adversarial threads that the chapter holds against (with structural disarm) but warrant acknowledgment in the pre-pub review queue for transparency to publisher / agent / editor:

- **T1 acknowledgment.** Decision-tool framing at Ch 9:144 implies prescriptive direction under hostile read; chapter's open-question closing + structural-observation discipline provide structural disarm; thread expected to draw libertarian-PC adversarial reception which is part of the framework's positioning in the political-economy debate.
- **T2 acknowledgment.** Rent-extractor cluster sector-naming at Ch 9:206 reads as left-policy targeting under hostile read; chapter's structural-observation-not-advocacy disclaimer + eleven-cent comparable-burden framing provide structural disarm.
- **T4 acknowledgment.** Three property-rights exceptions argument at Ch 9:160–164 invites scholarly-disagreement-within-domain pushback from free-market-environmental tradition; chapter's domain-bounded framing + framework-as-supplement framing hold; this is the canonical scholarly-engagement framing for the property-rights tradition.
- **T5 acknowledgment.** Asymmetric Regret Rule at Ch 9:56 invites scholarly-engagement pressure-test from IAM tradition (methodology-grounding-gap; no Stern / Nordhaus / Savage / Loomes & Sugden citations in Ch 9 itself; Ch 6 carries the methodology); not chapter-disqualifying.
- **T6 acknowledgment.** Foreign-model framing at Ch 9:198 + Mondragon / Vienna / Saltsjöbaden case-bank invites right-populist-tradition pushback; chapter's Nordic-objection four-condition steelman + sub-national-implementation argument + Chattanooga foregrounding provide structural disarm.
- **T7 acknowledgment.** Adam Smith *"completion of the market mechanism"* framing at Ch 9:170 invites hard-left-tradition pushback; chapter's Christophers public-ownership endorsement + named class-power dynamic + rent-extractor sector-naming reach substantively further-left than the framing-alone suggests; framework is not market-fundamentalist.
- **T8 reception-cycle note.** Industry-funded reviewer reception is predisposed-hostile-by-financial-incentive; chapter is not designed to land this reception; mitigation is reception-cycle level (supportive reception from non-hostile venues offsets).

---

## §7. Verdict synthesis

### §7.1 Per-character tally — full 8-character adversarial set

| Verdict | Count | Characters |
|---|---|---|
| ⚠ EXCLUDE | 2 | Char 5 (free-market-environmental); Char 8 (right-populist) |
| ⚠⚠ EXCLUDE | 5 | Char 1 (libertarian PC); Char 2 (MacLean-sympathetic); Char 4 (climate-denier); Char 6 (IAM-tradition); Char 7 (hard-left) |
| ⚠⚠⚠ EXCLUDE | 1 | Char 3 (industry-funded) — predisposed-hostile-by-financial-incentive; non-chapter-disarmable |
| **Total** | **8 EXCLUDE** | **As expected per template verdict-floor — all adversarial characters selected for hostile read** |

### §7.2 Aggregate Pass-3.4 robustness verdict

**CONDITIONALLY ROBUST.**

- **No ⚠⚠⚠ chapter-disqualifying threads found that are chapter-disarmable.** Char 3 (industry-funded ⚠⚠⚠ EXCLUDE) is predisposed-hostile-by-financial-incentive per the Ch 1 REAUDIT v3 §5.3 canonical framing; not chapter-disarmable; mitigation is reception-cycle level. This is the normal cost of doing structural-economic-critique work.
- **Common load-bearing threads (T1, T2, T4, T5, T6, T7) found; chapter's structural moves disarm sufficiently at structural-claim level.** Each thread is acknowledged in the pre-publication review queue (§6.4) for publisher / agent / editor transparency.
- **One procedurally-spot-fixable thread (T3) flagged for optional author ratification.** Pass 3.3 Character 15 Option A (one sentence acknowledging methodological-vs-political distinction relative to *Democracy in Chains* / MacLean controversy) would disarm T3 without damaging acceptance verdicts. Author judgment; default per Pass 3.3 §6.3 is hold-as-is.
- **One cross-chapter cascade flag (T7 → Ch 10 Pass 3.4 future-session input).** Hard-left thread on Ch 9:170 closing reflection extends to Ch 10's closing register; Ch 10's Pass 3.4 should pressure-test the thread there. Not blocking Ch 9 Pass 3.4 verdict; routes per pipeline doctrine §5 cross-chapter workstream lifecycle only if Ch 10 Pass 3.4 confirms the thread re-triggers.
- **Cross-pressure structure across the 8-character set indicates correct positioning.** T1 + T2 + T7 show opposite-direction adversarial pressure on the same chapter passages — the canonical sign of load-bearing claims positioned correctly in the political-economy debate.

**Does NOT require structural engagement.** No common load-bearing thread surfaces where the chapter does NOT disarm; no cross-chapter workstream needed beyond the optional Ch 10 Pass 3.4 forward-flag.

### §7.3 Phase-C disposition recommendation

**No required Phase C spot-fix application session from Pass 3.4.** All load-bearing threads (T1, T2, T4, T5, T6, T7) are hold-as-is with pre-pub-review-queue acknowledgment; T8 is reception-cycle mitigation only.

**One optional Phase C item:**

- **T3 (MacLean acknowledgment).** Pass 3.3 Character 15 Option A: one sentence at Ch 9:144 or 148. Two coordinated approaches if the author chooses to apply:
  - **Option A1.** Apply at Ch 9-only level (per Pass 3.3 Character 15 Option A recommendation).
  - **Option A2.** Apply as consolidated cross-chapter MacLean-acknowledgment note across Ch 5 + Ch 9 + TA §1.10 sites (per §5.2 above; routes through Stage 1c D-3 deferred sibling-coherence-check if it fires).
  - **Option B (default per Pass 3.3 §6.3).** Hold as-is. Reading C v3 asymmetric framing + chapter-wide structural-injustice politics provide substantive distance from Buchanan's broader political project; explicit acknowledgment may expand chapter scope into MacLean engagement that the chapter doesn't otherwise carry.

**Author judgment item.** Pass 3.4 default recommendation: Option B (hold as-is). If the author wants to apply, Option A1 is lower-touch + lower-cross-chapter-scope than Option A2.

### §7.4 Pass 3.5 readiness

Pass 3.5 (developmental-edit) **can fire** per per-prompt serial cadence after Pass 3.4 ratify-and-apply (or hold-as-is ratification if no Phase C applies). Pass 3.4 surfaced no urgent whole-chapter restoration-of-richness items; §6.3 above flags the eleven-cent-difference passage (Ch 9:192–208) as the chapter's analytically-densest passage for low-priority Pass 3.5 attention.

**Recommended next session for Ch 9:** Author ratification of Pass 3.4 verdict + T3 optional spot-fix disposition. After ratification, Pass 3.5 (developmental-edit) fires per per-prompt serial cadence per [feedback_audience_aware_drafting_discipline.md](../memory/feedback_audience_aware_drafting_discipline.md) v3.0 Amendment B (3.1 → 3.2 → 3.3 → 3.4 → 3.5; each in its own prompt).

---

## §8. What this pass did NOT do

Per framing's hard constraints + v3.0 Amendment B per-prompt serial cadence:

- **Did NOT re-run Pass 1 (fact-check).** Pass 1 ratified + Phase C applied 2026-05-19 (commit `4c8bc02`).
- **Did NOT re-run Pass 2 (voice-polish).** Pass 2 ratified + Phase C applied 2026-05-21 (commit `78a26c2`).
- **Did NOT re-run Pass 3.3 (audience-load acceptance).** Pass 3.3 ratified + landed 2026-05-23 (commit `a6b7df5`; aggregate verdict READY TO SUBMIT AS-IS).
- **Did NOT return INCLUDE or NEUTRAL verdicts for adversarial characters.** Verdict-floor is EXCLUDE per template; adversarial characters are SELECTED for hostile read.
- **Did NOT apply spot-fixes to the chapter file.** Phase C (per-chapter spot-fix application session) does that after author ratification; no required spot-fixes from Pass 3.4 (T3 is optional).
- **Did NOT re-write paragraphs.** Findings + thread-pull synthesis + STOP, per the Pass-3.4 template hard constraint.
- **Did NOT re-litigate Reading C v3 framing.** Reading C v3 is canonical per author ratification 2026-05-21.
- **Did NOT contact named subjects.** Per consent discipline; public-record exception applies for citation of adversarial-reviewer institutional affiliations but not for outreach.
- **Did NOT spin up the deferred Stage 1c D-3 sibling-coherence-check.** Pass 3.4 surfaces T3 + T7 as potential D-3 / Ch 10 Pass 3.4 inputs but does not block on either; both routed per §6.1.
- **Did NOT pre-empt Pass 3.5 (developmental-edit).** Pass 3.5 fires per per-prompt serial cadence after Pass 3.4 ratification.

---

## §9. Hard constraints honored

- ✓ Did NOT apply spot-fixes to `manuscript/chapters/Chapter__9_PricingHonestly.md`.
- ✓ Did NOT re-write paragraphs.
- ✓ Did NOT re-score Pass 1 / Pass 2 / Pass 3.3 — all ratified + Phase C applied where applicable; referenced for context only.
- ✓ Did NOT re-litigate Reading C v3 framing — canonical per author ratification 2026-05-21.
- ✓ Did NOT contact named subjects (including adversarial-reviewer institutional affiliations — public-record exception applies for citation but not for outreach).
- ✓ Did NOT return INCLUDE or NEUTRAL verdicts for adversarial characters — verdict-floor EXCLUDE per template.
- ✓ DID produce a thread-pull synthesis table as the central diagnostic (§3); per-character verdicts (§2) are inputs to the synthesis, not the diagnostic itself.
- ✓ DID flag cross-chapter incoherence surfaced by adversarial-direction read beyond what Pass 3.3 §4 cleared — T7 (Ch 10 closing-reflection touch) + T3 (Stage 1c D-3 deferred sibling-coherence-check potential) per §5 + §6.1.
- ✓ Verified post-Pass-2-Phase-C + Stage-1c-Phase-C chapter line count (294 lines, 2026-05-23) against current origin/main.
- ✓ Verified commit `4c8bc02` (Ch 9 Pass 1 Phase C) exists on origin/main.
- ✓ Verified commit `78a26c2` (Ch 9 Pass 2 Phase C + Reading C v3 rewrite) exists on origin/main.
- ✓ Verified commit `cbef9bd` (Ch 8 Stage 1c Phase C Option A) exists on origin/main.
- ✓ Verified commit `a6b7df5` (Ch 9 Pass 3.3 acceptance PROPOSED) exists on origin/main.
- ✓ Verified Pass 3.3 acceptance test artifact §5.1 + §6.4 + §2 character verdicts as canonical Pass-3.4 input per framing.
- ✓ Built feature branch `claude/manuscript-stage-3-ch9-pass3-4-1fae85` from current origin/main per [tools/workstream-handoffs/README.md](../workstream-handoffs/README.md) workstream-as-feature-branch convention.
- ✓ Applied [Ch 1 REAUDIT v3 §5.3](commons_bonds_ch1_stage_3_pass_3_audience_load_REAUDIT_2026-05-17_PROPOSED.md) thread-pull synthesis as canonical format model.

---

*End of Ch 9 Stage-3 Pass 3.4 (Audience-Load Robustness) rigor pass — PROPOSED 2026-05-23. Aggregate verdict CONDITIONALLY ROBUST; no required Phase C spot-fixes; T3 (MacLean acknowledgment) optional per Pass 3.3 Character 15 Option A — author judgment. T1 + T2 + T4 + T5 + T6 + T7 hold-as-is with pre-pub-review-queue acknowledgment per §6.4. T8 reception-cycle mitigation only. T7 → Ch 10 Pass 3.4 forward-flag for cross-chapter pressure-test. Pass 3.5 (developmental-edit) is the next session for this chapter per per-prompt serial cadence after Pass 3.4 ratification.*

---

## §10. Disposition log (2026-05-25 Phase C session)

**Author ratification 2026-05-25 (same session as this artifact's verdict reading):**

> "ratify Pass 3.3 Character 15 Option A as recommended; fire the Stage 1c D-3 deferred sibling-coherence-check"

### §10.1 T3 (MacLean acknowledgment) — RATIFIED + APPLIED (Option A2 consolidated)

Author selected Pass 3.4 §7.3 **Option A2** (consolidated cross-chapter MacLean-acknowledgment across Ch 5 + Ch 9 + TA §1.10 sites) over Option A1 (Ch-9-only). Selection inferred from the bundled instruction to "fire the Stage 1c D-3 deferred sibling-coherence-check" alongside the Char 15 Option A ratification — D-3 firing is the cross-chapter routing path Option A2 requires.

**Phase C application (this commit):**

| Site | Pre-application closing | Post-application addition | Voice register adaptation |
|---|---|---|---|
| **Ch 9 line 144** | *"should read Buchanan and Tullock alongside this book."* | + *"The rent-seeking analytical vocabulary survives many readings of Buchanan's broader political project, and this book draws on the vocabulary rather than endorsing the project."* | None — canonical Char 15 Option A form. |
| **Ch 5 line 202** | *"should read Buchanan and Tullock and their successors in parallel."* | + same canonical sentence | None — fits Ch 5's expository-policy register. |
| **TA §1.10 line 610** | *"...as a foundation their apparatus can apply to, not as an alternative to their apparatus."* | + *"...this **Appendix** draws on the vocabulary rather than endorsing the project."* | *"this book"* → *"this Appendix"* (single-word adaptation for TA self-reference register). |

**Thread disposition update:** T3 was classified as **procedural / cosmetic flag** in §3 thread-pull synthesis; spot-fixable without damaging acceptance verdicts. D-3a consolidated application closes T3 across all three Public-Choice-engagement sites. Pass 3.4 Char 2 (MacLean-sympathetic) ⚠⚠ EXCLUDE verdict would shift toward ⚠ EXCLUDE on adversarial re-read post-application (push-back but chapter holds against push-back).

### §10.2 Other threads (T1, T2, T4, T5, T6, T7, T8) — HOLD as ratified per §7.3

All non-T3 threads ratified at the Pass 3.4 §7.3 default (HOLD with pre-pub-review-queue acknowledgment per §6.4). Author's ratification scope was narrowly Char 15 Option A; T1 + T2 + T4 + T5 + T6 + T7 + T8 dispositions unchanged. T7 → Ch 10 Pass 3.4 forward-flag remains for future-session input.

### §10.3 D-3 firing scope

Author's "fire the Stage 1c D-3 deferred sibling-coherence-check" instruction fired the deferred Stage 1c check at two scopes:

- **D-3a (MacLean consolidation, NEW from Pass 3.4 §5.2 scope expansion)** — APPLIED in this session via §10.1 above.
- **D-3b (symmetric-vs-asymmetric framing alignment, original Stage 1c §6.2 IF-2 + IF-3 scope from 2026-05-21)** — fired as audit; finds Ch 5 line 202 ⚠⚠ INCOHERENT + TA §1.10 line 610 ⚠ DRIFT against Reading C v3 / Ch 8:122 Option A canonical form. Proposed Options A / B / C documented per site in companion D-3 artifact; PROPOSED state; awaits author ratification before Phase C application.

D-3 firing artifact: [`tools/rigor-passes/commons_bonds_stage_1c_coherence_check_2026-05-25_ch5_ta_public_choice_sibling_v1.0.0.md`](commons_bonds_stage_1c_coherence_check_2026-05-25_ch5_ta_public_choice_sibling_v1.0.0.md) (produced in this same commit).

### §10.4 Pass 3.4 verdict closure

Pass 3.4 verdict CONDITIONALLY ROBUST holds with T3 disarmed via D-3a application. The only optional spot-fix Pass 3.4 surfaced is now applied + consolidated; no further Pass 3.4 Phase C action required from author. The pre-publication review queue items (§6.4 T1 + T2 + T4 + T5 + T6 + T7 + T8 acknowledgments) remain as Stage 5 sign-off input.

**Pass 3.4 ratified state:** CLOSED as of this Phase C session. Per-prompt serial cadence advances to:
- **Next Pass 3.5 (developmental-edit) for Ch 9** — can fire per Pass 3.4 §7.4 readiness, after D-3b ratification + application (or after author ratifies D-3b deferral).
- **Cross-chapter cascade follow-ups:** D-3b ratification + Pass 3.3 light re-fire (across Ch 5 + Ch 9 + TA post-D-3b) recommended consolidated session per D-3 artifact §5.4.

### §10.5 What this Phase C session did NOT do

- Did NOT apply D-3b options to Ch 5 line 202 or TA §1.10 line 610 — PROPOSED state; awaits separate author ratification per per-prompt serial cadence.
- Did NOT fire Pass 3.3 light re-fire — flagged for separate session per D-3 artifact §5.4; recommended consolidated with D-3b post-ratification.
- Did NOT fire Pass 3.5 (developmental-edit) for Ch 9 — separate session per per-prompt serial cadence.
- Did NOT address T7 (hard-left thread) Ch 10 forward-flag — routes per Pass 3.4 §6.1 to Ch 10's Pass 3.4 future-session.
- Did NOT re-litigate Reading C v3 Ch 9 framing or Ch 8:122 Option A — canonical references.
- Did NOT contact named subjects.

---

*End of Pass 3.4 disposition log — Phase C 2026-05-25. T3 RATIFIED via Char 15 Option A + APPLIED (consolidated across Ch 5 + Ch 9 + TA §1.10). D-3a CLOSED; D-3b PROPOSED for separate ratification. Pass 3.4 verdict CONDITIONALLY ROBUST holds; per-prompt serial cadence advances toward Pass 3.5 (after D-3b sequencing).*

---

## §11. Ratification record (2026-05-25)

**Author ratification 2026-05-25 (same session as §10 disposition log, immediately after Phase C application landed at commit `8aa7dfb`):**

> "ratify the CONDITIONALLY ROBUST verdict now"

### §11.1 Verdict ratified

**Pass 3.4 aggregate verdict: CONDITIONALLY ROBUST — RATIFIED 2026-05-25.**

The CONDITIONALLY ROBUST classification (per [Stage-3 template](../drafting-templates/stage-3-three-pass-rigor-audit.md) §"Pass 3.4: Audience-load (robustness)") is the correct verdict for Ch 9 at this state:
- Common load-bearing threads (T1, T2, T4, T5, T6, T7) found that the chapter's structural moves DO disarm.
- T3 (procedural; spot-fixable) disarmed in Phase C 2026-05-25 via consolidated Char 15 Option A application across Ch 5 + Ch 9 + TA §1.10.
- T8 (industry-funded predisposed-hostile-by-financial-incentive) non-chapter-disarmable; reception-cycle mitigation only.
- All disarmed load-bearing threads acknowledged in the pre-publication review queue per §6.4 + §7.2.

**No upgrade to ROBUST warranted.** The ROBUST classification requires "no common load-bearing threads found; isolated procedural flags only." Pass 3.4 found six load-bearing threads (T1, T2, T4, T5, T6, T7); CONDITIONALLY ROBUST is the correct verdict even with T3 disarmed because the chapter's structural moves disarm rather than eliminate those threads. ROBUST would misrepresent the corpus's actual adversarial-pressure-test profile.

**No downgrade to REQUIRES STRUCTURAL ENGAGEMENT warranted.** No common load-bearing thread surfaced where the chapter does NOT disarm; no cross-chapter workstream or chapter-level structural revision needed beyond the optional T7 → Ch 10 Pass 3.4 future-session forward-flag (which is a forward-input, not a structural-engagement gate).

### §11.2 Thread dispositions confirmed at ratification

| Thread | Pre-ratification disposition | Post-ratification status |
|---|---|---|
| **T1** Decision-tool framing implies prescriptive direction | HOLD; pre-pub review queue acknowledgment | ✓ RATIFIED HOLD |
| **T2** Rent-extractor sector-naming as left-policy targeting | HOLD; pre-pub review queue acknowledgment | ✓ RATIFIED HOLD |
| **T3** Buchanan implicit endorsement insufficient (MacLean) | SPOT-FIX via Char 15 Option A | ✓ APPLIED 2026-05-25 (commit `8aa7dfb`); thread closed |
| **T4** Three property-rights exceptions resolvable within Coase | HOLD; pre-pub review queue acknowledgment | ✓ RATIFIED HOLD |
| **T5** Asymmetric Regret Rule one-sided risk-framing | HOLD; pre-pub review queue acknowledgment | ✓ RATIFIED HOLD |
| **T6** Foreign-model importation | HOLD; structural disarm built in | ✓ RATIFIED HOLD |
| **T7** Ideological accommodation of capital | HOLD + Ch 10 cross-chapter forward-flag | ✓ RATIFIED HOLD; forward-flag preserved |
| **T8** Cost-attribution math foundations contested (industry-funded) | Non-chapter-disarmable; reception-cycle mitigation | ✓ RATIFIED reception-cycle mitigation only |

### §11.3 Stage 5 sign-off input — pre-publication review queue items finalized

Per [feedback_audience_aware_drafting_discipline.md](../memory/feedback_audience_aware_drafting_discipline.md) v3.0 + §6.4 above: the seven pre-publication-review-queue acknowledgments (T1 + T2 + T4 + T5 + T6 + T7 + T8) are now **accepted as the canonical Stage 5 sign-off input for Ch 9**. The publisher / agent / editor receives these acknowledgments alongside the manuscript-submission package per pipeline-doctrine v1.0.0 Stage 5 protocol.

The pre-publication review queue's transparency-rather-than-overclaiming-verification posture is satisfied: the corpus does not claim to have eliminated adversarial-direction load-bearing threads where none can be eliminated without abandoning the framework's substantive contribution; it claims to have anticipated them, structurally disarmed where possible, and named what an external reader would still find for further scholarly engagement.

### §11.4 Phase A closure for Ch 9 Pass 3.4

Pass 3.4 PROPOSED → RATIFIED → CLOSED. The full per-prompt serial cadence sequence for Ch 9 Stage-3 rigor pass:

| Pass | PROPOSED commit | RATIFIED / APPLIED commit | Status |
|---|---|---|---|
| Pass 1 (fact-check) | — (earlier session) | `4c8bc02` (2026-05-19 Phase C) | ✓ CLOSED |
| Pass 2 (voice-polish) | `e68b505` | `78a26c2` (2026-05-21 Phase C + Reading C v3 substantive rewrite) | ✓ CLOSED |
| Stage 1c (Ch 8 cross-chapter cascade) | — (Ch 8 artifact) | `cbef9bd` (2026-05-21 Phase C Option A) | ✓ CLOSED |
| Pass 3.3 (acceptance) | `a6b7df5` (2026-05-23 PROPOSED — READY TO SUBMIT AS-IS) | (no Phase C required; aggregate INCLUDE) | ✓ CLOSED via ratification of recommended defaults this session |
| Pass 3.4 (robustness) | `f47dd1c` (2026-05-23 PROPOSED — CONDITIONALLY ROBUST) | `8aa7dfb` (2026-05-25 Phase C T3 Char 15 Option A + D-3 fired) + this ratification (2026-05-25) | ✓ **CLOSED 2026-05-25** |

### §11.5 What ratification of CONDITIONALLY ROBUST does NOT do

- Does NOT eliminate the pre-publication review queue acknowledgments (T1, T2, T4, T5, T6, T7) — those remain as Stage 5 sign-off transparency input.
- Does NOT pre-empt the T7 → Ch 10 Pass 3.4 forward-flag — Ch 10's Pass 3.4 future-session still needs to pressure-test whether the hard-left thread re-triggers at Ch 10's closing-reflection register.
- Does NOT pre-empt D-3b ratification (Ch 5 + TA §1.10 symmetric-vs-asymmetric framing alignment) — cross-thread-todos #16 still tracks; remains author-judgment item.
- Does NOT pre-empt Pass 3.5 (developmental-edit) Ch 9 sequencing — per §7.4, Pass 3.5 fires after Pass 3.4 ratification (now satisfied) + D-3b sequencing (still pending).
- Does NOT reception-cycle-mitigate T8 — industry-funded reception is what it is; mitigation operates via supportive non-hostile reception at publication-time.

### §11.6 What ratification advances

- **Pass 3.5 (developmental-edit) Ch 9 readiness now fully unblocked** at the Pass 3.4 gate (modulo D-3b sequencing per author judgment).
- **Stage 5 sign-off material for Ch 9 substantially complete** — pre-pub review queue items confirmed; only Pass 3.5 + pre-publication-date-refresh remain in Stage 3 → Stage 5 path.
- **PM dashboard #20 (Manuscript Stage-3 Rigor Pass) advances Ch 9 row to substantially-complete** — Pass 1 + Pass 2 + Stage 1c (Ch 8 cascade) + Pass 3.3 + Pass 3.4 all CLOSED; only Pass 3.5 + optional D-3b remain.
- **Cross-pressure structure validated as positioning diagnostic** — the T1 + T7 opposite-direction adversarial pressure on the same chapter passages (per §3.1 synthesis observation) confirms the chapter is correctly positioned in the political-economy debate; this validation is itself a publishable observation about the corpus.

---

*End of Pass 3.4 ratification record — author ratified CONDITIONALLY ROBUST verdict 2026-05-25. Pass 3.4 Phase A CLOSED; per-prompt serial cadence next advances to either D-3b ratification (cross-thread-todos #16) or Pass 3.5 (developmental-edit) per author sequencing choice.*

---

## §12. D-3b cascade closure note (2026-05-25 — same session)

**Author ratification 2026-05-25 (immediately after §11):**

> "ratify all outstanding decisions as recommended"

Selection per §11.5 forward-flag enumeration: D-3b-Ch5 + D-3b-TA Option A recommendations ratified + applied. Consolidated Pass 3.3 light re-fire across Ch 5 + Ch 9 + TA fired same session.

**D-3b closure effects on Pass 3.4 verdict:**

- **Pass 3.4 CONDITIONALLY ROBUST verdict UNCHANGED.** Per §11.5 closure discipline + D-3 artifact §9.6: D-3b reinforces rather than re-litigates. No upgrade to ROBUST and no downgrade to REQUIRES STRUCTURAL ENGAGEMENT warranted.
- **Pass 3.4 §3.1 cross-pressure structural observation STRENGTHENED.** Char 1 (libertarian-PC hostile) + Char 7 (hard-left hostile) cross-pressure now operates at the strongest posture — chapter positioned correctly + position structurally coherent across the Ch 5 + Ch 8 + Ch 9 + TA §1.10 corpus. See D-3 artifact §9.5.
- **Pass 3.4 T1 thread HOLD-disposition CONFIRMED.** D-3b consolidation removes the cross-chapter framing-shift compounding factor Char 1 / Char 6 hostile reads previously leveraged; chapter's structural-disarm continues to hold.

**Per-chapter cascade fully complete for Ch 9 Stage 3:**

| Stage | Status | Commit |
|---|---|---|
| Pass 1 (fact-check) | ✓ CLOSED | `4c8bc02` |
| Pass 2 (voice-polish + Reading C v3) | ✓ CLOSED | `78a26c2` |
| Stage 1c (Ch 8 cross-chapter cascade) | ✓ CLOSED | `cbef9bd` |
| Pass 3.3 (acceptance) | ✓ CLOSED | `a6b7df5` (PROPOSED; defaults ratified) |
| **Pass 3.4 (robustness)** | ✓ **CLOSED** | `f47dd1c` → `8aa7dfb` → `4a28275` |
| **Stage 1c D-3 sibling-coherence-check** | ✓ **CLOSED** (both sub-scopes) | `8aa7dfb` (D-3 artifact + D-3a) → this commit (D-3b + Pass 3.3 light re-fire) |

**Pass 3.5 (developmental-edit) Ch 9 — next session per per-prompt serial cadence.** All upstream gates cleared.

---

*End of Pass 3.4 D-3b cascade closure note — full Ch 9 Stage 3 sequence through Pass 3.4 + D-3 CLOSED 2026-05-25. Pass 3.5 (developmental-edit) is the next session for Ch 9.*
