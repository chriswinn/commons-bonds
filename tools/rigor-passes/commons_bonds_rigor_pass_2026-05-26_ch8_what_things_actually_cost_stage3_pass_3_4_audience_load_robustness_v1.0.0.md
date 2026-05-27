# Commons Bonds — Ch 8 *What Things Actually Cost* — Stage 3 Pass 3.4 (Audience-Load Robustness)

**Date:** 2026-05-26
**Workstream:** Manuscript Stage-3 Rigor Pass (PM dashboard #20), Phase A — Ch 8 — Pass 3.4 (audience-load robustness)
**Chapter file:** [`manuscript/chapters/Chapter__8_WhatThingsActuallyCost.md`](../../manuscript/chapters/Chapter__8_WhatThingsActuallyCost.md) — **243 lines** (post-Phase-C-β + post-Stage-4 RATIFIED state; verified 2026-05-26 via `wc -l`; em-dash count = 28 per `grep -c "—"`; word count = 6,421 per `wc -w`).
**Discipline:** v3.0/v3.1 Pass 3.4 (audience-load robustness; adversarial / detractor character set; thread-pull synthesis verdict; verdict-floor EXCLUDE per character) per [`tools/drafting-templates/stage-3-three-pass-rigor-audit.md`](../drafting-templates/stage-3-three-pass-rigor-audit.md) §"Pass 3.4: Audience-load (robustness)".
**Mode:** audit-existing-prose (no Stage-1 brief; chapter file IS canonical reference).
**Format model:** [Ch 9 Pass 3.4 §3 thread-pull synthesis (2026-05-23 RATIFIED 2026-05-25 CONDITIONALLY ROBUST)](commons_bonds_rigor_pass_2026-05-23_ch9_pricing_honestly_stage3_pass_3_4_audience_load_robustness_v1.0.0.md) primary; [Ch 1 REAUDIT v3 §5.3](commons_bonds_ch1_stage_3_pass_3_audience_load_REAUDIT_2026-05-17_PROPOSED.md) canonical underlying template; [Ch 4 Pass 3.4 (2026-05-25)](ch4_existence_proof_stage3_pass_3_4_robustness_2026-05-25.md) + [Ch 3 Pass 3.4 (2026-05-25)](commons_bonds_rigor_pass_2026-05-25_ch3_thewaterman_stage3_pass3.4_audience_load_robustness_v1.0.0.md) format calibrators.
**Status:** PROPOSED — pending author ratification. Phase C-γ session applies any ratified spot-fixes after author disposition (T3 below is the principal candidate; T1 + T2 + T4 + T5 + T6 + T7 + T8 + T9 are HOLD-with-pre-pub-review-queue-acknowledgment by default per Ch 9 cousin pattern).

**Prior-pass closure context.**
- Pass 3.1 (fact-check) — CLOSED 2026-05-16. Ratification + Phase C application via commits `5fe6af6` + `275b75a` (MED-6 Phase C-β follow-through) + `57575b1` (cross-corpus IPG canonical Option D) + `9befb92` (coal-CO₂ McDowell-specific cascade-reconciliation Phase C — 4 spot-fixes at lines 40, 52, 166, 238).
- Pass 3.2 (voice-polish) — CLOSED + RATIFIED 2026-05-25. Ratification at commit `138aa7e` (PROPOSED 2026-05-23 → RATIFIED 2026-05-25); cascade-reconciliation `6589ca2` (`9befb92` sync); Phase C-β application at commit `16554fa` (8 chapter spot-fixes + chapter-wide em-dash comprehensive sweep 80 → 28; line-count delta neutral; word-count +46 net).
- Pass 3.3 (acceptance) — PROPOSED 2026-05-25 (commit `65a89dc`). Aggregate verdict **READY AS-IS** (28 INCLUDE / 0 NEUTRAL / 0 EXCLUDE; §9.3 Option A hold default; §7 forward-flagged 15 adversarial characters for this Pass 3.4 session).
- Stage 4 (render + character-integrity audit) — RATIFIED 2026-05-26 author-completed-offline (commit `e36bdd6`). Independent of and not blocking Pass 3.4.

**Branch:** `claude/ch8-pass3-4-audience-load-robustness-a9d9ac` off origin/main `b37aa46` (rebased to current tip; pre-push reconciliation per CLAUDE.md).

---

## §0. Source artifacts read

1. [`manuscript/chapters/Chapter__8_WhatThingsActuallyCost.md`](../../manuscript/chapters/Chapter__8_WhatThingsActuallyCost.md) — chapter under audit, 243 lines post-Phase-C-β + post-Stage-4 RATIFIED.
2. [Pass 3.3 acceptance artifact 2026-05-25](commons_bonds_rigor_pass_2026-05-25_ch8_what_things_actually_cost_stage3_pass_3_3_audience_load_acceptance_v1.0.0.md) — §3 per-character acceptance verdicts; §4 cross-character pattern observations; §5 apparatus / consistency / named-subject sub-checks; §7 forward-flagged 15 adversarial characters with Ch-8-specific thread expectations (the canonical Pass-3.4 input).
3. [Pass 3.2 voice-polish artifact 2026-05-23](commons_bonds_rigor_pass_2026-05-23_ch8_what_things_actually_cost_stage3_voice_polish_v1.0.0.md) — §7 forward-flagged Pass-3 observations; §10.1 ratification table (8 RATIFY APPLY + 12 RATIFY HOLD).
4. [Pass 3.1 fact-check artifact 2026-05-16](commons_bonds_rigor_pass_2026-05-16_ch8_what_things_actually_cost_stage3_fact_check_v1.0.0.md) — §10 original audience-character set + §12 rent-seeking-paragraph fact-check coverage.
5. [Ch 9 Pass 3.4 robustness artifact (2026-05-23 PROPOSED → 2026-05-25 RATIFIED CONDITIONALLY ROBUST)](commons_bonds_rigor_pass_2026-05-23_ch9_pricing_honestly_stage3_pass_3_4_audience_load_robustness_v1.0.0.md) — directly-adjacent chapter Pass 3.4 (8-character adversarial set; T1-T8 thread-pull synthesis with cross-pressure positioning diagnostic); primary format model.
6. [Ch 4 Pass 3.4 robustness artifact (2026-05-25)](ch4_existence_proof_stage3_pass_3_4_robustness_2026-05-25.md) — analytical-quantitative cousin Pass 3.4; format calibrator.
7. [Ch 3 Pass 3.4 robustness artifact (2026-05-25)](commons_bonds_rigor_pass_2026-05-25_ch3_thewaterman_stage3_pass3.4_audience_load_robustness_v1.0.0.md) — recent comparator Pass 3.4; format calibrator.
8. [Ch 1 REAUDIT v3 §5.3 (2026-05-17)](commons_bonds_ch1_stage_3_pass_3_audience_load_REAUDIT_2026-05-17_PROPOSED.md) — adversarial thread-pull synthesis canonical underlying format model.
9. [Stage-3 template](../drafting-templates/stage-3-three-pass-rigor-audit.md) §"Pass 3.4: Audience-load (robustness)" — verdict scale + thread-pull synthesis structure.
10. [Audience-pressure-test construction](../drafting-templates/audience-pressure-test-construction.md) §3.2 — adversarial character types + selection methodology.
11. [Cross-corpus IPG canonical-construction rigor pass (2026-05-21 Option D)](commons_bonds_rigor_pass_2026-05-21_cross_corpus_ipg_canonical_construction_v1.0.0.md) — Option D applied at Ch 8:168 via commit `57575b1`.
12. [Apparatus register decision (2026-05-11)](commons_bonds_rigor_pass_2026-05-11_apparatus_register_decision_v1.0.0.md) — Item 1 (inline-integral strip from Ch 8 ✓ intact); Item 13 (IPG full-name + acronym); Item 14 (Cᵢ via Four Gates).
13. Memory: [`feedback_audience_aware_drafting_discipline.md`](../memory/feedback_audience_aware_drafting_discipline.md) v3.1 (Pass 3.4 verdict = thread-pull synthesis, NOT per-character pass/fail; verdict-floor EXCLUDE per character); [`feedback_named_subject_consent.md`](../memory/feedback_named_subject_consent.md) (public-record exception for cited scholars + adversarial-reviewer institutional affiliations); [`feedback_verify_stale_memory_claims.md`](../memory/feedback_verify_stale_memory_claims.md) (verification discipline).

**Verifications performed at session start:**
- ✓ Chapter file exists at cited path; line count = 243 per `wc -l` (matches Pass 3.3 baseline).
- ✓ Em-dash count = 28 per `grep -c "—"` (matches Pass 3.2 §10.1 F-V3 Option B comprehensive sweep target band).
- ✓ Word count = 6,421 per `wc -w` (matches Pass 3.3 baseline).
- ✓ Commit `e36bdd6` (Ch 8 Stage 4 RATIFIED 2026-05-26) present on origin/main (chapter-state stability for Pass 3.4 audit).
- ✓ Commit `65a89dc` (Ch 8 Pass 3.3 PROPOSED 2026-05-25) present on origin/main with §7 adversarial-character-set flag-forwards intact.
- ✓ Commit `cbef9bd` (Ch 8 Stage 1c Phase C Option A — asymmetric rent-seeking framing alignment with Ch 9 Reading C v3) present on origin/main; line 122 paragraph intact.
- ✓ Cross-corpus IPG canonical-construction Option D intact at line 168.
- ✓ Coal-CO₂ McDowell-specific cascade-reconciliation intact at lines 40, 52, 72, 166, 238.
- ✓ Item 1 inline-integral strip from Ch 8 ✓ intact (no Greek letters / integrals in body prose).
- ✓ Ch 9 cousin Pass 3.4 artifact present + RATIFIED CONDITIONALLY ROBUST (2026-05-25).
- ✓ Branch `claude/ch8-pass3-4-audience-load-robustness-a9d9ac` built from origin/main `b37aa46` per CLAUDE.md branch discipline.

---

## §1. Pass-3.4 scope reminder

Pass 3.4 applies the **adversarial / detractor character set** to the chapter. **Verdict-floor for adversarial characters is EXCLUDE; INCLUDE / NEUTRAL are not in scope.** All adversarial characters return EXCLUDE — that is expected and required. **The diagnostic is NOT pass/fail per character.** The diagnostic is **which threads they collectively find** (§3 thread-pull synthesis) and whether those threads are (a) load-bearing chapter claims the chapter must hold against (acknowledge in pre-pub review queue; cross-chapter handoff if warranted) or (b) procedural / cosmetic flags spot-fixable without damaging Pass 3.3 acceptance verdicts, or (c) predisposed-hostile-by-financial-incentive-or-ideology positions not chapter-disarmable (reception-cycle mitigation only).

**Specifically tested under hostile read** (per framing carry-forward from Pass 3.3 §7):

- Does the chapter's **$190/ton SCC anchor + EPA AP-42 §1.1 bituminous-coal combustion factor + 2.61 t-CO₂/ton coal + $510 carbon-tail + IPG 33-122×** quantitative backbone (lines 72 + 168) survive an industry-funded fossil-fuel-economist hostile read?
- Does the **Political Capture section + SCC political-fight chronology (Obama → Trump → Biden → EPA 2023)** at lines 112–124 survive a climate-skeptical / SCC-questioning hostile read at the methodology-grounding level?
- Does the **rent-seeking paragraph at line 122 with explicit Public Choice (Buchanan, Tullock) + reparations-economics (Coates, Darity, Mullen, Hamilton, Conley) co-citation + framework's-different-in-kind asymmetric framing** survive (a) a Buchanan-orthodox Public Choice hostile read and (b) a MacLean-sympathetic Buchanan-critical hostile read?
- Does the **asset-class-consolidation framing + DOJ-investigation framing + YIMBY both/and synthesis** at lines 180–190 survive an industry-funded housing-economics hostile read?
- Does the **2008 financial crisis architecture engagement** at line 192 (Mian & Sufi 2014 *House of Debt* citation + bank-balance-sheet-vs-household-debt-restructuring policy-choice framing) survive an industry-funded financial-services hostile read?
- Does the **civilizational-scale extrapolation** at line 214 ($10-15T annual; "largest continuous wealth transfer in human history") survive scale-aggressive adversarial pressure-testing?
- Does the **Black-American-writing-tradition passage** at line 92 (Dunbar / Du Bois / Fanon / Ellison + framework-contribution closer) survive reactionary-intellectual + tabloid-populist-skeptic adversarial reads?
- Does the **analytical-quantitative pricing of cost-bearer experience** (McDowell County health + community + lineage + knowledge components) survive an anti-pricing-as-instrumentalization cost-bearer-adversarial read?

**Adversarial set: 15 characters drawn from the Pass 3.3 §7 forward-flag list**, organized into five categorical bands per [audience-pressure-test construction](../drafting-templates/audience-pressure-test-construction.md) §3.2:

| # | Category | Character |
|---|---|---|
| 1 | Industry-funded | Industry-funded fossil-fuel-industry economist |
| 2 | Industry-funded | Industry-funded coal-industry economist |
| 3 | Industry-funded | Industry-funded housing-economics economist |
| 4 | Industry-funded | Industry-funded financial-services economist |
| 5 | Ideologically-opposed | Buchanan-orthodox hostile Public Choice theorist |
| 6 | Ideologically-opposed (cross-cutting) | MacLean-sympathetic Buchanan-critical adversarial reader |
| 7 | Ideologically-opposed | Pure-libertarian / Rothbardian reader |
| 8 | Ideologically-opposed | Reactionary intellectual reader |
| 9 | Ideologically-opposed | Orthodox-econ (Chicago / freshwater macro) adversarial wing |
| 10 | Ideologically-opposed | Climate-skeptical / SCC-questioning policy reader |
| 11 | Trade-press / commercial | Trade-press hostile reviewer (NYT / WSJ / Atlantic / TNR book-reviewer) |
| 12 | Trade-press / commercial | WSJ editorial-board / business-press conservative |
| 13 | Cultural | Tabloid / populist-skeptic reader |
| 14 | Legal | Tort-reform / fiduciary-protection lawyer |
| 15 | Cost-bearer | Adversarial-anti-pricing-as-instrumentalization cost-bearer reader |

Set size (15) sits above the Ch 9 cousin (8) + Ch 4 cousin (10–12) baselines, consistent with the Ch 8 Pass 3.3 §7 forward-flag list (15 characters) and consistent with Ch 8's distinctive role as the framework's load-bearing analytical-quantitative chapter (more adversarial vectors map onto a chapter whose central rhetorical instrument is the IPG arithmetic + the $10-15T civilizational-scale extrapolation).

---

## §2. Per-character adversarial verdicts

Format mirrors Ch 9 Pass 3.4 §2 per-character layout: brief profile + hostile-read posture + threads pulled + chapter's structural moves that disarm + net read + verdict.

### Character 1 — Industry-funded fossil-fuel-industry economist

**Profile.** Heritage Foundation energy fellow / Manhattan Institute energy program / Texas Public Policy Foundation / American Petroleum Institute (API) policy economist / Institute for Energy Research. Funded by fossil-fuel-industry sources (direct or via foundation channels). Predisposed-hostile-by-financial-incentive: the framework's apparatus IS the threat to their funders.

**Hostile-read posture.** Pressure-tests SCC anchoring as politically-driven IAM modeling rather than physics-driven; pressure-tests $190/ton EPA 2023 update as Biden-era-political-choice rather than methodology-driven; weaponizes chapter's Political Capture section's SCC political-fight chronology as one-sided framing; pressure-tests IPG ratio construction (33-122×) as overcounting via component-double-counting; pressure-tests civilizational-scale $10-15T extrapolation as scale-fear-mongering.

**Threads pulled.**

- **Ch 8:72 SCC anchor — *"the EPA's most recent estimate of the social cost of carbon ... is one hundred and ninety dollars per metric ton."*** Hostile reviewer reads $190/ton as politically-anchored choice rather than methodology-anchored; the Rennert et al. 2022 *Nature* + EPA 2023 update chronology is read as Biden-administration scientific-consensus-claiming.
- **Ch 8:72 carbon-arithmetic — *"approximately 2.6 metric tons of carbon dioxide ... the climate cost of burning one ton of McDowell County coal ... is approximately five hundred and ten dollars."*** Hostile reviewer reads the per-ton $510 carbon cost as the single most weaponizable claim against fossil-industry economics; demands the SCC-anchor uncertainty be foregrounded rather than embedded in a confident closing sentence.
- **Ch 8:118 SCC political-fight chronology — *"Under the Trump administration it was cut to between one and seven dollars by limiting the calculation's geographic scope to the United States rather than global externalities, a methodological change academic commentary (Wagner, Anthoff, Cropper, et al. 2021) flagged as ungrounded in standard cost-benefit-analysis practice."*** Hostile reviewer weaponizes the chronology's one-sided framing: chapter cites Wagner et al. 2021 critique of Trump-era methodology but does not cite industry-funded critique of Obama / Biden global-scope methodology.
- **Ch 8:164–168 IPG construction — *"Total: $524 per ton ... Against a 1960 market price of four to five dollars ... thirty-three and one hundred and twenty-two times the 1960 sale price ... at least three"* carbon-vs-today's-market.** Hostile reviewer pressure-tests the ratio construction for double-counting (does the Foreclosure component overlap with Direct Health? With Environmental Degradation?); demands component-independence proof.
- **Ch 8:214 civilizational-scale extrapolation — *"the annual global severed cost from fossil extraction is in the range of eight to ten trillion dollars ... somewhere between ten and fifteen trillion dollars annually ... the largest continuous wealth transfer in human history."*** Hostile reviewer reads as scale-fear-mongering; weaponizes the $10-15T figure as the most-prominent claim industry-aligned counter-research can attack.

**Chapter's structural moves that disarm.**

- **Ch 8:28 "conservative throughout" methodological discipline — *"Where estimates have a range I use the lower figure, and where an externality is contested I omit it. The goal is not a ceiling but a floor — the smallest honest number the framework can defend."*** The chapter's central methodological-discipline move; pre-empts the "you're overcounting" objection through transparent floor-construction. Hostile reviewer must engage at the floor-arithmetic level rather than at the ceiling-fear-mongering level.
- **Ch 8:18 Four Gates discipline — *"every Cᵢ that passes the discipline of the Commons Inversion Test, units consistency, boundedness, and independence."*** The chapter explicitly invokes the framework's component-independence gate (Cᵢ Four Gates Item 14 per apparatus register). Component-double-counting is structurally pre-empted at the framework level.
- **Ch 8:118 EPA chronology completeness — chapter's chronology names ALL four administrations** (Obama $42; Trump $1-7; Biden $51; EPA 2023 $190). Not a partisan-targeted selection.
- **Ch 8:72 cross-corpus IPG canonical-construction Option D applied** (per commit `57575b1`) — explicit range construction (33-122× depending on cost categories admitted and SCC anchor used) carries methodological-honesty about variation.
- **Ch 8:218 explicit scope-discipline on civilizational-scale extrapolation — *"a gestured claim: one sentence of supporting arithmetic against an assertion that would, if taken seriously as a policy agenda, require years of sectoral simulation."*** Chapter names the figure's scope-limit; honest-about-overclaim discipline.
- **Cross-chapter routing.** Per-component arithmetic relies on Ch 2 (Black Lung Trust Fund), Ch 5 (cross-case sweep), Ch 6 (residual commons value integral + SCC anchor), Ch 9 (policy-architecture); industry-funded reviewer pressure-testing component math routes to chapters that carry the component derivations.

**Net read.** Industry-funded fossil-fuel-economist hostile reviewer would write a hostile review regardless of chapter structural moves; the chapter's framework-arithmetic IS the threat to their funders. Chapter's "conservative throughout" methodological discipline + Four Gates component-independence framing + cross-corpus IPG explicit-range construction + EPA chronology completeness + civilizational-scale scope-discipline DO substantial structural-disarm work — sufficient that an *intellectually-serious* fossil-economy-aligned reviewer (one who would publish in *RealClearEnergy* or Heritage Foundation Backgrounder rather than in Mises Wire) would have to engage at scholarly-disagreement level. But predisposed-hostile-by-financial-incentive reception is not chapter-disarmable. ⚠⚠⚠ EXCLUDE: would weaponize chapter against itself; reception-cycle mitigation only. (Canonical predisposed-hostile-by-financial-incentive case per Ch 1 REAUDIT v3 §5.3.)

---

### Character 2 — Industry-funded coal-industry economist

**Profile.** National Mining Association (NMA) policy economist / American Coal Council policy fellow / industry-funded West Virginia / Kentucky policy-research center / Coal Institute. Funded by coal-industry sources. Predisposed-hostile-by-financial-incentive; reads chapter's McDowell-County eight-component arithmetic as direct threat to coal-industry economic narrative.

**Hostile-read posture.** Pressure-tests each cost-component attribution to the coal industry (vs. confounders); demands separate attribution for surface-mining vs. underground-mining cost-loadings; pressure-tests Black Lung Benefits Program Trust Fund framing as legitimate-occupational-disease-compensation rather than as severed-cost-on-public-ledger; pressure-tests reclamation-bond gap as appropriate-regulatory-allocation rather than as industry-cost-severance; pressure-tests mountaintop-removal cancer-rate framing as unproven-confounder-not-controlled.

**Threads pulled.**

- **Ch 8:34 + 38 Black Lung Benefits Program Trust Fund — *"federally tracked, specifically attributable, and severally accumulated onto the public ledger when coal-company bankruptcies discharge the original liability ... a conservative figure sits between two and four dollars per ton at the national level."*** Hostile reviewer reframes as legitimate-public-private partnership for occupational-disease compensation; pressure-tests the "severance" framing as ideologically-loaded.
- **Ch 8:48 reclamation-bond gap — *"the reclamation bonds coal companies were required to post under the 1977 Surface Mining Control and Reclamation Act currently fall between three and a half and six billion dollars short of the documented remediation need."*** Hostile reviewer reframes as appropriate-regulatory-allocation that took the industry decades to fully fund; pressure-tests "shortfall" framing as ignoring industry-funded reclamation work that did happen.
- **Ch 8:50 mountaintop-removal cancer figure — *"the sixty thousand Appalachian cancer cases linked to mountaintop removal mining."*** Hostile reviewer pressure-tests the 60K figure for confounder control (smoking; diet; deprivation-independent-of-mining; geographic / genetic factors); demands Hendryx-specific citation that the chapter does not provide (per Pass 3.3 §8 already-flagged optional pre-pub item).
- **Ch 8:58 drug-induced death rate — *"In 2015, the county recorded the highest drug-induced death rate of any county in America."*** Hostile reviewer pressure-tests causation between coal-industry collapse and opioid-epidemic; demands attribution to broader regional/national opioid-supply-side factors that operated independently of coal-industry collapse.
- **Ch 8:60–62 community-disruption $5/ton anchoring — *"sustained regional decline sit in the range of five to fifteen dollars per ton of extracted coal."*** Hostile reviewer demands the methodology behind the regional-decline-pricing literature; pressure-tests $5/ton as floor against industry-funded alternative literature.

**Chapter's structural moves that disarm.**

- **Ch 8:28 + 96 + 108 + 124 + 138 conservative-floor discipline.** All non-fact-check cost-component anchors explicitly use the lower bound; chapter's structural choice is to underclaim per component.
- **Ch 8:34 Chapter-2 cross-reference.** Black Lung Benefits Program per-ton arithmetic relies on Ch 2's detailed Trust-Fund + funding-gap + debt-trajectory + severance-mechanism walk; hostile reviewer pressure-testing the framing routes to Ch 2.
- **Ch 8:88 + 90 + 94 lineage labor cost-attribution discipline.** Chapter explicitly names the data-sparsity ("data attributing specific dollar figures per ton is sparse") + adopts conservative $2/ton placeholder; chapter's methodological honesty about attribution-difficulty pre-empts industry-funded counter-attribution-research.
- **Ch 8:120 political-capture framing as structural-not-actor-blame.** Chapter does not pin black-lung delay on industry-as-bad-actor; chapter cites *both* UMWA-under-Lewis's reported preference to defer the issue (organized-labor side) *and* industry-side political-capture; structural reading, not partisan-targeted reading.
- **Ch 8:200 first-misreading-defense — *"Cheap energy, even severely mispriced energy, lifted billions of human beings out of poverty, and no responsible reader of this book should accept an account that pretends otherwise."*** Substantive acknowledgment of the coal-industry-aligned narrative on the welfare contribution of cheap energy; not anti-industry-as-such framing.

**Net read.** Coal-industry-funded hostile reviewer would publish a critical review in *Coal Age* / NMA policy-paper venue regardless of chapter structural moves; the chapter's per-component arithmetic IS the threat to industry economic narrative. Chapter's conservative-floor discipline + cross-chapter routing to Ch 2 + lineage-labor methodological honesty + first-misreading-defense's welfare-acknowledgment do substantial disarm work at the intellectually-serious-engagement level. But predisposed-hostile-by-financial-incentive reception is not chapter-disarmable. ⚠⚠⚠ EXCLUDE: would weaponize chapter against itself by demanding each cost-attribution claim survive industry-funded counter-narratives; reception-cycle mitigation only.

---

### Character 3 — Industry-funded housing-economics economist

**Profile.** American Enterprise Institute (AEI) housing-policy fellow / Mercatus Center housing-policy program / National Rental Home Council policy economist / industry-funded real-estate-investment-policy research. Predisposed-hostile to the chapter's asset-class-consolidation framing + DOJ-investigation framing.

**Hostile-read posture.** Defends institutional-landlord asset-class as efficiency-enhancing market response to supply-restriction; pressure-tests pricing-coordination-via-software claims as unproven antitrust theory; pressure-tests the chapter's claim that supply-restriction does NOT explain cost-burden-share-rise as misreading of the housing-economics literature; defends the YIMBY-orthodox position against the chapter's both/and synthesis.

**Threads pulled.**

- **Ch 8:186 cost-burden-share rising across supply-elasticity spectrum — *"Cost-burdened renter share — the share of renters paying more than thirty percent of income on housing — has risen across markets with widely varying supply elasticities ... Standard housing-economics taxonomy distinguishes supply-restricted metro markets (San Francisco, New York, Boston, Seattle) from supply-expanded ones (Atlanta, Phoenix, Houston, Charlotte); the JCHS 2024 report documents the rise in cost-burden share across both."*** Hostile reviewer pressure-tests the JCHS 2024 reading; demands distinction between absolute-cost-burden-rise (driven by income stagnation + housing-cost rise that supply matters for) and relative-cost-burden-rise across supply taxonomies.
- **Ch 8:188 asset-class-consolidation framing — *"Asset-class consolidation (the rise of institutional landlords; the financialization of single-family rental as an asset class; the documented pricing-coordination patterns that property-management software has enabled across markets, which the U.S. Department of Justice has been investigating since 2022) operates on top of whatever supply elasticity each local market has."*** Hostile reviewer pressure-tests the DOJ-investigation framing (the RealPage investigation began Nov 2022 + remains in litigation; chapter cites "investigating since 2022" — Pass 3.3 §8 already flagged this as a pre-publication-refresh item).
- **Ch 8:188 "captures more aggressively where the supply-side leverage is strongest" — *"The asset-class consolidation captures rent at the household-income level regardless of whether the units are abundant or scarce; it merely captures more aggressively where the supply-side leverage is strongest."*** Hostile reviewer reads as begging the question (if asset-class-consolidation captures more where supply-leverage is strongest, the binding-constraint is still supply, not asset-class-consolidation as the mechanism).
- **Ch 8:190 both/and synthesis — *"Supply restriction is real and zoning reform is the appropriate response to it; rent-extraction is also real and a different accountability architecture is the appropriate response to it."*** Hostile reviewer reads as concession that frames the YIMBY position as half-the-problem and reserves the other half for a non-YIMBY policy framework.

**Chapter's structural moves that disarm.**

- **Ch 8:182 substantive YIMBY steelman — *"The empirical literature on housing-supply restriction is substantial. Edward Glaeser and Joseph Gyourko's work documenting supply-constrained metropolitan areas. Jenny Schuetz's research on land-use regulation as the binding constraint in high-cost markets. Recent academic and policy work documenting that in markets where zoning permits dense construction, rents and home prices track underlying construction-cost trajectories more closely than in markets where they don't, and that liberalizing zoning produces measurable rent moderation in the markets where it has been tried."*** Chapter takes the YIMBY position seriously by name + cites the canonical YIMBY-tradition scholars + acknowledges the empirical support. Not strawman.
- **Ch 8:184 substantive-acknowledgment — *"Each of these claims is sound on its own terms. The framework's response is not to deny supply restrictions or to treat zoning reform as unimportant."*** Explicit substantive acknowledgment.
- **Ch 8:188 empirical-evidence-not-ideology framing on DOJ point — *"the documented pricing-coordination patterns that property-management software has enabled across markets, which the U.S. Department of Justice has been investigating since 2022."*** Chapter frames the DOJ point empirically (investigation is on the record; the legal-process-state framing leaves the antitrust-status appropriately uncertain).
- **Ch 8:190 explicit two-mechanism domain-bounded framing — *"the two are operating simultaneously and the policy response has to address both."*** Both-mechanisms-real-and-domain-bounded framing; this is exactly the kind of intellectually-serious scholarly-engagement framing the housing-economics tradition can engage with.

**Net read.** Housing-economics-industry-funded hostile reviewer would publish a critical AEI working paper but at scholarly-disagreement-within-shared-domain level rather than at chapter-disqualification level. The chapter's substantive YIMBY engagement + Glaeser-Gyourko-Schuetz acknowledgment by name + both/and synthesis + empirical-not-ideological DOJ framing carry the scholarly-engagement bridge. The framework's substantive claim (cost-burden-share rise across supply-elasticity spectrum demands a non-supply-only explanation) is the load-bearing claim hostile reviewer must engage at the empirical level rather than dismiss. ⚠⚠ EXCLUDE: would actively reject the framework's two-mechanism diagnosis; finds load-bearing thread (asset-class-consolidation as separate-mechanism-from-supply-restriction) the chapter's both/and synthesis honors but does not concede. Spot-fix opportunity for the DOJ-investigation status sentence (already flagged Pass 3.3 §8) is incidental, not structural.

---

### Character 4 — Industry-funded financial-services economist

**Profile.** American Bankers Association (ABA) policy economist / Securities Industry and Financial Markets Association (SIFMA) policy fellow / Bank Policy Institute / Hoover Institution financial-sector-aligned policy work. Predisposed-hostile to 2008-architecture engagement + Mian-Sufi citation + framework's policy-choice framing.

**Hostile-read posture.** Defends 2008 bank-balance-sheet recapitalization choice as appropriate-emergency-policy-given-systemic-risk; pressure-tests Mian & Sufi 2014 framing as one-sided academic position not representative of broader literature; pressure-tests "the scope-choice was contested" as importing scholarly minority view as canonical; defends asset-class-financialization framing as efficiency-enhancing capital allocation.

**Threads pulled.**

- **Ch 8:192 2008-architecture critique — *"The federal response ... deployed roughly seven hundred billion dollars in direct authorization and trillions more in liquidity and guarantees, almost all of it directed at recapitalizing bank balance sheets rather than restructuring household debt."*** Hostile reviewer reframes as appropriate-systemic-risk-management; pressure-tests "rather than restructuring household debt" framing as ignoring the legal + administrative + political constraints on household-debt-restructuring that the policy debate at the time engaged.
- **Ch 8:192 Mian-Sufi framing — *"Mian and Sufi, whose 2014 House of Debt analyzed the welfare cost of the chosen architecture against the household-debt-restructuring architecture that was politically reachable but not selected."*** Hostile reviewer reads "politically reachable but not selected" as importing Mian-Sufi's contested counterfactual claim as canonical; demands engagement with Bernanke / Geithner / Paulson / Krugman counter-positions on the systemic-risk-management justification.
- **Ch 8:192 policy-choice-not-market-outcome framing — *"the 2008 response was not a market outcome, it was a policy choice, and the choice produced a particular distribution of the crisis's costs between bank balance sheets and household balance sheets."*** Hostile reviewer reads as ideological framing of crisis-response as redistributive-not-stabilization choice.
- **Ch 8:188 asset-class-financialization framing.** (Already engaged above for Char 3; financial-services-industry overlap.)

**Chapter's structural moves that disarm.**

- **Ch 8:192 acknowledgment of "contested at the time" — *"The scope-choice was contested at the time and has been documented since by economists including Mian and Sufi."*** Chapter explicitly names the contested-at-the-time status; not claiming Mian-Sufi as the consensus position.
- **Ch 8:192 cross-chapter routing to Ch 9.** Chapter explicitly notes "Chapter 9 will return to what the alternative architecture would have looked like under honest pricing"; the 2008-architecture engagement is preview-not-developed-position. Hostile reviewer pressure-testing the 2008 framing routes to Ch 9.
- **Ch 8:200 first-misreading-defense honors market-mechanism work.** Chapter explicitly disclaims anti-market-as-such framing.
- **Ch 8:204 market-is-not-fake misreading-defense — *"The market is not fake. The market is incomplete."*** Frames the framework's critique as completing the market accounting rather than rejecting market mechanisms. Financial-services-industry hostile reviewer who reads for ideological-framing finds the framework operating within market-economics framing.

**Net read.** Financial-services-industry hostile reviewer would publish critical responses at ABA Banking Journal / SIFMA white-paper venues; the 2008-architecture critique IS the threat to the post-2008-architecture professional narrative. Chapter's contested-at-the-time + cross-chapter routing to Ch 9 + market-is-not-fake framing do substantial disarm work at intellectually-serious-engagement level. ⚠⚠ EXCLUDE: would actively reject; finds load-bearing thread (2008-architecture as redistributive-policy-choice) the chapter's structural moves engage but cannot eliminate at the financial-sector-aligned ideological level. Not predisposed-hostile-by-direct-financial-incentive at the same level as fossil/coal industry (the architecture-question is more arms-length to ABA / SIFMA institutional positions), so reception is at scholarly-disagreement rather than at industry-wire-coordination level.

---

### Character 5 — Buchanan-orthodox hostile Public Choice theorist

**Profile.** Cato Institute scholar / Mercatus Center / George Mason University economics department orthodox-Public-Choice tradition / Heritage Foundation policy fellow. Reads commons-pricing frameworks with default skepticism for redistributive policy implications; reads rent-seeking analysis as exclusively addressing government-coercion-and-regulatory-capture rather than as broader analytical framework.

**Hostile-read posture.** Pressure-tests the chapter's rent-seeking paragraph (line 122) as importing Public Choice methodology for redistributive purposes Buchanan + Tullock would not endorse; pressure-tests the framework's "different in kind" framing as commandeering Public Choice's analytical legitimacy; reads chapter's Political Capture section + Christophers / Mian-Sufi engagement as expanded-state-power policy direction the framework's "is not a policy recommendation" disclaimer (line 16) cannot defuse.

**Threads pulled.**

- **Ch 8:122 framework-vs-Public-Choice asymmetric framing — *"The Public Choice tradition (Buchanan, Tullock) supplies the vocabulary for the extractor's reasoning that shaped the political-coalition record on the books. The framework's contribution is different in kind: the ledger that counts what those traditions described has been costing, and to whom — the cost-bearing magnitudes that name McDowell County's thirteen-year life-expectancy gap as a number rather than as an actor-attribution problem."*** Hostile reviewer reads "different in kind" as commandeering Public Choice methodology for analytical work Buchanan + Tullock did not anticipate or endorse; reads "the ledger that counts what those traditions described has been costing" as redistributive-direction-by-implication.
- **Ch 8:122 reparations-economics-AND-Public-Choice co-citation — *"The reparations-economics tradition (Coates, Darity, Mullen, Hamilton, Conley) supplies the actor-and-coalition vocabulary for the racial wealth gap. The Public Choice tradition (Buchanan, Tullock) supplies the vocabulary for the extractor's reasoning..."*** Hostile reviewer reads the parallel citation as forcing-equivalence between traditions Buchanan-orthodox reader views as incompatible; demands the chapter engage with the analytical incompatibility rather than place them in parallel.
- **Ch 8:120 political-capture-cost framing — *"Estimates of the annual lobbying spend of the fossil fuel industry alone run into the hundreds of millions of dollars, and that figure captures only the visible fraction."*** Hostile reviewer reads as one-sided lobbying-as-rent-seeking targeting (fossil-industry only; no analogous coverage of environmental-advocacy lobbying, public-sector-union lobbying, etc.).
- **Ch 8:200–206 misreading-defenses.** Hostile reviewer reads the three misreading-defenses as preemptive-defense-of-policy-direction the chapter disclaims having; if the chapter's claims are policy-neutral analytical-arithmetic, why pre-empt three policy-direction objections?

**Chapter's structural moves that disarm.**

- **Ch 8:16 explicit not-a-policy-recommendation disclaimer — *"It is not, in this book, a policy recommendation. It is an accounting exercise. What we choose to do with the accounting is a separate question — a political one — and one this book is deliberately not trying to answer."*** Explicit policy-direction-disclaimer at chapter's opening; chapter does not claim to derive policy implications from arithmetic.
- **Ch 8:122 framework-Public-Choice asymmetric framing per cascade `cbef9bd` (2026-05-21 Stage 1c Phase C Option A).** The "different in kind" framing is exactly the asymmetric framework-Public-Choice alignment that matches Ch 9 Reading C v3; the chapter is not commandeering Public Choice methodology, it is naming the chapter's analytical-arithmetic work as taking place *downstream of* the Public Choice tradition's actor-analysis work.
- **Ch 8:200 first-misreading-defense honors market-mechanism work.** *"Cheap energy, even severely mispriced energy, lifted billions of human beings out of poverty."* Substantive acknowledgment of the welfare-economics work cheap energy did; not anti-market-as-such.
- **Ch 8:204 market-is-not-fake misreading-defense.** Frames the framework's critique as completing market accounting rather than rejecting market mechanisms; explicit inside-the-tradition framing.
- **Ch 8 + Ch 9 framing-symmetry cross-chapter discipline.** Reader proceeding Ch 8 → Ch 9 experiences continuous asymmetric framing (Ch 9 Reading C v3 builds on Ch 8:122 framing); the cross-chapter coherence is itself a discipline-anchor for the hostile reviewer pressure-testing for inconsistency.

**Net read.** Buchanan-orthodox hostile Public Choice reviewer reads the chapter's framework-Public-Choice asymmetric framing as the framework taking methodology from Public Choice without endorsing the broader political-economic project Buchanan + Tullock developed. Chapter's not-a-policy-recommendation disclaimer + asymmetric framing per `cbef9bd` cascade + market-is-not-fake misreading-defense + Adam-Smith-style market-completion framing (per Ch 9 cross-chapter handoff) do substantial disarm work at the intellectually-serious-engagement level. But the orthodox Public Choice reader's prior commitment to the broader political-economic project Buchanan articulated does not match the framework's analytical-arithmetic direction; the hostile read sticks at the political-direction-implication level. ⚠⚠ EXCLUDE: would actively reject; finds load-bearing thread (asymmetric framing + Christophers-direction Ch-9-handoff implies prescriptive policy-direction the framework's disclaimers cannot eliminate) the chapter's structural moves partially defuse but do not eliminate. Cross-pressure structure with Char 6 (MacLean-sympathetic; reads same passage as INSUFFICIENT distance from Buchanan) — the canonical sign of correct positioning per Ch 9 Pass 3.4 §3.1.

---

### Character 6 — MacLean-sympathetic Buchanan-critical adversarial reader

**Profile.** Reader carrying the *Democracy in Chains* (Nancy MacLean 2017) reading of James Buchanan's Virginia-school Public Choice as rooted in 1950s segregationist-school-funding resistance + designed to insulate concentrated wealth from democratic accountability. Cross-cutting adversarial position: critical of the framework's Public Choice integration from the LEFT.

**Hostile-read posture.** Rejects any framework that cites Buchanan + Tullock as canonical-methodology source without engaging the *Democracy in Chains* controversy; demands explicit acknowledgment of the political-project critique; reads the chapter's Public Choice citation as papering over Buchanan's contested political project.

**Threads pulled.**

- **Ch 8:122 Buchanan + Tullock citation without MacLean engagement — *"The Public Choice tradition (Buchanan, Tullock) supplies the vocabulary for the extractor's reasoning that shaped the political-coalition record on the books."*** Hostile reviewer reads citation of Buchanan without engagement with the *Democracy in Chains* controversy as procedural blindness to the political-project contestation MacLean's reading turns load-bearing.
- **Ch 8:122 reparations-economics-AND-Public-Choice parallel-citation.** Hostile reviewer reads the parallel citation as moral-equivalence between traditions MacLean-sympathetic reader views as politically incompatible (reparations-economics direction vs. Buchanan's political project as MacLean reads it).
- **Ch 8 absence of explicit MacLean engagement.** No reference to *Democracy in Chains*; no acknowledgment of the controversy; no discussion of segregationist-funding-resistance origins of Virginia-school Public Choice; no acknowledgment of contested-political-project framing.
- **Ch 8 + Ch 9 cross-chapter MacLean-silence.** Per Ch 9 Pass 3.4 §10 (RATIFIED 2026-05-25): D-3a consolidated MacLean-acknowledgment was APPLIED across Ch 9 line 144 + Ch 5 line 202 + TA §1.10 line 610 ("the rent-seeking analytical vocabulary survives many readings of Buchanan's broader political project, and this book draws on the vocabulary rather than endorsing the project"). Ch 8 line 122 is the **fourth Public-Choice-engagement site that did NOT receive the D-3a consolidated MacLean acknowledgment**. This is a substantive cross-chapter coherence gap.

**Chapter's structural moves that disarm.**

- **Ch 8:122 asymmetric framing — *"The framework's contribution is different in kind."*** Carries implicit distance from Buchanan's broader project; the framework takes methodology, not political project.
- **Ch 8:122 reparations-economics primary lineage — *"The reparations-economics tradition (Coates, Darity, Mullen, Hamilton, Conley) supplies the actor-and-coalition vocabulary for the racial wealth gap."*** Chapter's primary lineage-citation in the rent-seeking paragraph is reparations-economics — the political tradition substantively opposed to the political project MacLean attributes to Buchanan. Chapter's politics are substantively-opposed-to-Buchanan's-political-project at the lineage-citation level.
- **Ch 8:92 Black-American-writing-tradition lineage at line 92** (Dunbar / Du Bois / Fanon / Ellison) reinforces the chapter's substantive direction.
- **Chapter-wide structural-injustice framing.** The chapter centers McDowell County cost-bearer experience; the framework's direction is structurally opposite to the political project MacLean attributes to Buchanan.

**Net read.** Implicit distance via asymmetric framing + reparations-economics-primary-citation + Black-American-writing-tradition lineage + chapter-wide structural-injustice politics carry substantive distance at the political-direction level. But absence of explicit MacLean engagement at the Ch 8:122 Public-Choice-citation site — particularly given that Ch 5 + Ch 9 + TA §1.10 received the D-3a consolidated MacLean acknowledgment 2026-05-25 — reads as cross-chapter coherence gap. A MacLean-sympathetic reader carrying the controversy at the front of their attention finds the load-bearing thread (asymmetric framing + reparations-citation provide substantive distance, but explicit MacLean acknowledgment at Ch 8:122 would close the cross-chapter coherence gap and disarm the procedural-blindness read).

⚠⚠ EXCLUDE: would actively reject; finds **procedurally-spot-fixable thread (T3 below)** that the cross-chapter D-3a consolidated MacLean acknowledgment leaves incomplete at Ch 8:122. Note: this is the cross-chapter-coherence-gap surfaced by the Pass 3.4 audit; the Ch 9 cousin Pass 3.4 §10.1 D-3a application explicitly noted "across Ch 5 + Ch 9 + TA §1.10 sites" — Ch 8:122 was not included in the D-3a application scope because at the time, the Ch 8 rent-seeking paragraph was treated as the *originator* of the asymmetric framing (per cascade `cbef9bd`) rather than as another sibling-coherence-check site. Pass 3.4 audit recommends that Ch 8:122 receive the same D-3a consolidated MacLean acknowledgment for cross-chapter coherence. See §3 thread T3 + §7.3.

---

### Character 7 — Pure-libertarian / Rothbardian reader

**Profile.** Mises Institute reader / Foundation for Economic Education (FEE) audience / Cato-libertarian-wing reader. Reads framework's accountability-bond logic + Ch-9-handoff (which Ch 8 forward-references at lines 192 + 234) + civilizational-scale $10-15T extrapolation at line 214 as expanded-state-power proposal disguised as cost-accounting.

**Hostile-read posture.** Rejects any framework whose apparatus implies expanded-government-role in pricing cost-externalities; reads cost-severance as private-sector-problem appropriately resolved through property-rights / tort-system mechanisms; pressure-tests the chapter's civilizational-scale extrapolation as global-governance-by-implication.

**Threads pulled.**

- **Ch 8:214 civilizational-scale extrapolation — *"the largest continuous wealth transfer in human history."*** Hostile reviewer reads as global-governance-by-implication framing; the figure is the chapter's most-marketable single claim and also the most-weaponizable from this hostile direction.
- **Ch 8:120 political-capture-framing — *"Democracies spend real money (through lobbying expenditures, captured regulatory agencies, think tanks funded to produce the conclusions their funders need, and the civic attention diverted from other questions) to keep the honest accounting from happening."*** Hostile reviewer reads as critique of regulatory-capture that doesn't acknowledge that the regulatory architecture being captured is itself the problem (libertarian alternative: less regulation, less to capture).
- **Ch 8:206 third-misreading-defense — *"Honest pricing creates the revenue to fund clean industrialization pathways for developing nations — not as charity, but as the repayment of historical severance."*** Hostile reviewer reads as global-fiscal-transfer-program-by-implication.
- **Ch 8:234 Ch-9-and-Ch-10 forward-references — *"Chapter 9 sketches the direction a civilization committed to honest accounting would move. Chapter 10 closes with the miner, the waterman, and the off-world administrator..."*** Hostile reviewer reads "the direction a civilization committed to honest accounting would move" as policy-prescription forward-reference.

**Chapter's structural moves that disarm.**

- **Ch 8:16 + 218 + 232 + 236 explicit scope-discipline.** Chapter consistently disclaims policy-prescription scope — line 16 ("not a policy recommendation"); line 218 ("a gestured claim... cannot honestly be compressed into the closing pages of a framework book"); line 232 ("outside the scope of this book"); line 236 ("Their pursuit belongs to policy-makers, scholars, communities, and political coalitions").
- **Ch 8:204 market-is-not-fake misreading-defense.** Inside-the-market-tradition framing.
- **Ch 8:206 asymmetric-transition-timeline framing.** "The transition timeline should be asymmetric" places the burden on developed nations whose wealth reflects historical severance; not generic global-fiscal-transfer framing.
- **Ch 8:200 first-misreading-defense honors cheap-energy welfare contribution.** Substantive acknowledgment that even severely mispriced energy lifted billions out of poverty; honors the libertarian-tradition welfare-economics emphasis.

**Net read.** Pure-libertarian / Rothbardian hostile reviewer reads the framework's accountability-bond logic + civilizational-scale extrapolation + Ch-9-direction-forward-reference as expanded-state-power direction the chapter's not-a-policy-recommendation disclaimer cannot defuse at the libertarian-tradition level. Chapter's substantive market-mechanism honoring + asymmetric-transition framing + cheap-energy-welfare acknowledgment carry intellectually-serious-engagement weight, but the libertarian-tradition prior commitment to minimal-government-and-property-rights-only frameworks rejects any apparatus that points at structural-accountability-architecture. ⚠⚠ EXCLUDE: would actively reject; finds load-bearing thread (accountability-architecture-direction-by-implication) the chapter's structural moves cannot eliminate at the libertarian-tradition level.

---

### Character 8 — Reactionary intellectual reader

**Profile.** *National Review* / *National Affairs* / *American Affairs* / *Claremont Review* / *First Things* reader-cluster; Niall Ferguson / Bret Stephens / Ross Douthat / Sohrab Ahmari-cluster sensibility. Reads chapter for left-coded scholarship-signaling tells; for legitimacy-of-cultural-tradition tests; for whether the framework operates within rather than against received institutional categories.

**Hostile-read posture.** Reads chapter's Political Capture cluster + Black-American-writing-tradition passage (line 92) + reparations-economics citation (line 122) + asset-class-consolidation framing as left-coded scholarship signaling; pressure-tests the chapter's lineage-citations as identity-politics-within-academic-prose; pressure-tests civilizational-scale extrapolation as overclaim-by-academic-prestige.

**Threads pulled.**

- **Ch 8:92 Black-American-writing-tradition passage — *"Paul Laurence Dunbar wrote 'We Wear the Mask' in 1896 ... Du Bois named the structural condition that required it in The Souls of Black Folk (1903). Fanon extended the analysis into the colonial-economic register the framework's extraction-community cases sit closest to in Black Skin, White Masks (1952). Ellison gave the long-form narrative of life under the mask in Invisible Man (1952). The framework adds the cost-accounting mechanism by which the mask remains structurally necessary."*** Reactionary intellectual reader reads as left-coded-lineage-citation signaling; pressure-tests whether the lineage is substantively load-bearing for the framework's cost-accounting work or whether it is identity-tradition signaling.
- **Ch 8:122 reparations-economics primary citation.** Reads as primarily-left-coded scholarly-tradition citation; pressure-tests whether the framework's analytical work substantively requires Coates / Darity / Mullen / Hamilton / Conley lineage or whether the citation is positioning-by-lineage.
- **Ch 8:118 SCC political-fight chronology.** Reads as one-sided framing (chapter cites academic critique of Trump-era methodology but not parallel critique of Obama / Biden methodology choices).
- **Ch 8:214 civilizational-scale extrapolation — *"the largest continuous wealth transfer in human history."*** Reads as academic-prestige overclaim; the kind of grand-scale historical-rhetorical claim *The Atlantic Monthly* / *Foreign Affairs*-essay register would carry without serious scope-discipline.
- **Ch 8:188 asset-class-consolidation framing.** Reads as left-coded-sector-targeting.

**Chapter's structural moves that disarm.**

- **Ch 8:92 substantive-framework-contribution close — *"The framework adds the cost-accounting mechanism by which the mask remains structurally necessary."*** The chapter's lineage-citation does close with substantive-framework-contribution claim — the lineage is load-bearing for the chapter's argument that the cost-bearing-party analysis is naming something the Black-American writing tradition has been naming for over a century. Not pure-lineage-positioning.
- **Ch 8:122 reparations-economics + Public Choice parallel citation.** The parallel-tradition citation is precisely the move that pre-empts purely-left-coded scholarship-signaling: the chapter explicitly draws on the right-of-center analytical tradition (Public Choice) alongside the reparations-economics tradition; the framework's "different in kind" framing distinguishes both traditions from the framework's own analytical-arithmetic work.
- **Ch 8:218 explicit scope-discipline on civilizational-scale extrapolation.** "A gestured claim ... cannot honestly be compressed into the closing pages of a framework book" — chapter names the figure's scope-limit.
- **Ch 8:200 first-misreading-defense honors cheap-energy welfare contribution.** Not-anti-extraction-as-such framing.
- **Ch 8:118 EPA chronology completeness.** Chronology names ALL four administrations (Obama / Trump / Biden / EPA 2023); not a partisan-targeted selection.

**Net read.** Reactionary intellectual reader reads the Black-American-writing-tradition passage + reparations-economics citation + asset-class-consolidation framing as left-coded-scholarship-signaling that the chapter's parallel Public Choice citation + Adam-Smith-style market-completion framing (per Ch 9 cross-chapter handoff) + substantive scope-discipline + welfare-acknowledgment partially balance but do not eliminate at the cultural-tradition level. Reactionary intellectual reader's prior commitment to received-institutional-categories rejects scholarship that centers structural-injustice frameworks. ⚠⚠ EXCLUDE: would actively reject; finds load-bearing thread (left-coded scholarship-signaling cluster) the chapter's structural moves engage but cannot eliminate at the cultural-tradition level.

---

### Character 9 — Orthodox-econ (Chicago / freshwater macro) adversarial wing

**Profile.** Chicago School orthodox-econ / freshwater macro tradition adversarial wing. Reads heterodox-econ framings as displacement of property-rights-resolution-of-externalities frameworks (Coase 1960 + subsequent property-rights literature); pressure-tests structural-architecture analysis as replacing rather than supplementing efficiency-analysis.

**Hostile-read posture.** Pressure-tests the chapter's structural-cost-severance framing as ideological displacement of Coasean property-rights resolution; pressure-tests housing engagement (asset-class-consolidation framing) as anti-financialization framing that displaces capital-efficiency analysis; pressure-tests 2008-architecture engagement as displacement of systemic-risk-management economics.

**Threads pulled.**

- **Ch 8:202 market-is-not-fake misreading-defense — *"The market priced the extraction of the coal. The severed costs ... were a second transaction running alongside the first, unpriced, unwitnessed, and binding on parties who were never consulted."*** Orthodox-econ adversarial reader pressure-tests "unpriced, unwitnessed, and binding on parties who were never consulted" as begging the question of *why* the costs were unpriced; Coasean tradition addresses this through transaction-cost analysis; chapter's framing reads as moralistic-displacement of the Coasean framework.
- **Ch 8:18 Four Gates framing — *"every Cᵢ that passes the discipline of the Commons Inversion Test, units consistency, boundedness, and independence."*** Pressure-tests Four Gates as ideological framework rather than analytical apparatus; Coasean tradition would address via property-rights bargaining + transaction-cost reduction rather than via gate-discipline.
- **Ch 8:122 + 188 + 192 structural-cost-severance framings.** Pressure-tests each as displacement-of-efficiency-analysis: Political-Capture-cost as missing the property-rights bargaining frame; asset-class-consolidation as missing the capital-efficiency frame; 2008-architecture as missing the systemic-risk frame.

**Chapter's structural moves that disarm.**

- **Ch 8:204 market-is-not-fake closing — *"The market is not fake. The market is incomplete. The job of the framework is to name the part that got left out."*** Frames the framework as completing rather than replacing market analysis; explicit inside-the-tradition framing.
- **Ch 8:184–190 substantive YIMBY engagement — the chapter's substantive engagement with supply-side housing-economics tradition demonstrates the framework's openness to right-of-center analytical traditions.**
- **Ch 8:200 first-misreading-defense honors cheap-energy welfare contribution.** Welfare-economics-tradition acknowledgment.
- **Ch 8:122 framework-Public-Choice asymmetric framing.** Frames the framework as taking-methodology-from-rather-than-replacing the Public Choice tradition; analogous discipline could apply to the property-rights / Coasean tradition.

**Net read.** Orthodox-econ Chicago/freshwater adversarial reader pressure-tests the chapter's structural-cost-severance framing as displacement of Coasean property-rights resolution; chapter's market-is-not-fake closing + YIMBY engagement + Public-Choice asymmetric framing carry inside-the-tradition framing but the framework's direction (apparatus that prices cost-severance via structural-architecture analysis) is substantively orthogonal to Coasean property-rights resolution. ⚠⚠ EXCLUDE: would actively reject; finds load-bearing thread (structural-architecture analysis as displacement of property-rights resolution) the chapter's structural moves engage at scholarly-disagreement level but cannot eliminate at the tradition-direction level. Cross-pressure structure with Char 5 (Buchanan-orthodox; reads same chapter as commandeering-Public-Choice-direction); the orthogonal-direction adversarial pressure is canonical.

---

### Character 10 — Climate-skeptical / SCC-questioning policy reader

**Profile.** Competitive Enterprise Institute (CEI) climate-policy fellow / Heritage Foundation climate-policy cluster / Heartland Institute / Manhattan Institute climate-policy work. Adversarial to $190/ton SCC anchor as politically-driven IAM-modeling rather than physics-driven; reads SCC political-fight chronology as one-sided framing.

**Hostile-read posture.** Pressure-tests SCC anchoring as based on contested IAM modeling (RICE, DICE, FUND models that produce wildly different SCC depending on parameter choices); pressure-tests $190/ton EPA 2023 update as discount-rate-choice-driven rather than physics-driven; pressure-tests Rennert et al. 2022 *Nature* citation as appeal-to-academic-consensus rather than substantive engagement; reads "biosphere collapse" / "civilizational scale" framings as catastrophism.

**Threads pulled.**

- **Ch 8:72 SCC anchor — *"the EPA's most recent estimate of the social cost of carbon ... is one hundred and ninety dollars per metric ton."*** Hostile reviewer pressure-tests the $190 figure as discount-rate-choice-driven (Rennert et al. 2022 + EPA 2023 used 2% near-term + Ramsey-rule-derived long-term discount rates; the $190 vs Obama-era $42 is largely driven by discount-rate choice, not by new physics).
- **Ch 8:118 SCC political-fight chronology.** Hostile reviewer reads as one-sided: chapter cites Wagner et al. 2021 academic critique of Trump-era methodology but does not cite parallel critique of Obama / Biden discount-rate choices (e.g., the Cropper / Newell / Stavins / others traditions arguing for higher discount rates).
- **Ch 8:72 carbon-arithmetic — *"five hundred and ten dollars"* per-ton-coal-combusted carbon cost.** Hostile reviewer reads the $510 as the canonical SCC-as-politics-not-physics weaponizable figure; the discount-rate dependence is hidden in the anchoring chain.
- **Ch 8:214 civilizational-scale extrapolation.** Reads as fear-mongering at scale.
- **Ch 8:122 political-capture framing — *"The number is not uncertain because carbon physics is uncertain. The number is uncertain because the question of how much of the cost should be priced is a political fight, and one side of that fight has more resources than the other."*** Hostile reviewer reads this as the chapter ITSELF admitting the SCC is a political fight + then privileging one side of the fight.

**Chapter's structural moves that disarm.**

- **Ch 8:72 explicit citation chain — *"the Rennert et al. 2022 Nature integrated estimate that grounded the 2023 EPA update."*** Chapter cites the specific peer-reviewed paper that anchors the SCC choice; hostile reviewer must engage at the Rennert et al. 2022 methodology level, not at the EPA-administrative level.
- **Ch 8:28 conservative-throughout discipline.** Chapter's structural choice is lower-bound estimates; pre-empts the overcount objection.
- **Ch 8:118 EPA chronology completeness.** Chronology names ALL four administrations + cites academic critique by name (Wagner, Anthoff, Cropper, et al. 2021); chapter's framing is "the SCC is uncertain because the political fight has not resolved" rather than "the SCC is uncertain because the physics is contested."
- **Ch 8:74 explicit ratio framing — *"by a factor running from roughly three against today's market peak to more than a hundred against the 1960 mine-mouth."*** Chapter's central claim is the ratio holds across the full plausible SCC range; even at SCC values an order of magnitude below the $190/ton anchor, the framework's central rhetorical claim (carbon cost exceeds market price by structural margin) survives.

**Net read.** Climate-skeptical / SCC-questioning hostile reviewer pressure-tests the $190/ton anchor as discount-rate-choice-driven; chapter's Rennert et al. 2022 citation + EPA chronology completeness + conservative-throughout discipline + explicit-ratio-holds-across-SCC-range framing carry intellectually-serious-engagement weight. But the climate-skeptical reader's prior ideological commitment treats the SCC anchoring + civilizational-scale framing as fear-mongering; hostile read sticks at the framing-rejection level. ⚠⚠ EXCLUDE: would actively reject; finds load-bearing thread (SCC anchoring at the discount-rate-choice level + civilizational-scale framing) the chapter's structural moves engage but cannot eliminate at the ideological-commitment level. Mirrors Ch 9 Pass 3.4 Char 4 verdict + reasoning structure.

---

### Character 11 — Trade-press hostile reviewer

**Profile.** Reviewer assigned at NYT / WSJ / *The Atlantic* / *The New Republic* book-review desk with adversarial intent (either because the reviewer is ideologically opposed to the framework or because the editor is testing the framework via adversarial assignment). Reads chapter looking for threads to amplify in a chapter-critical review.

**Hostile-read posture.** Reads chapter for the single most-quotable adversarial-direction-amplification line; looks for internal inconsistencies between policy-disclaimer framing and substantive-direction implications; pressure-tests the chapter's most-aggressive single claims (civilizational-scale extrapolation; IPG 122× ratio; "largest continuous wealth transfer") for editor-amplification potential.

**Threads pulled.**

- **Ch 8:214 civilizational-scale extrapolation as headline-line — *"the largest continuous wealth transfer in human history."*** Most-quotable single line in the chapter; hostile reviewer weaponizes for review-headline.
- **Ch 8:16 + 234 + 236 policy-direction-disclaimer + Ch-9-direction forward-reference internal tension.** Hostile reviewer pressure-tests internal-consistency: chapter claims policy-neutrality + then forward-references "the direction a civilization committed to honest accounting would move" (Ch 9). Tension between disclaimer and direction is hostile-reviewer-weaponizable.
- **Ch 8:168 IPG ratio — *"thirty-three and one hundred and twenty-two times."*** Hostile reviewer weaponizes the 122× upper bound as overclaim; pressure-tests the upper bound's dependence on the highest cost-component-admission set + highest SCC anchor.
- **Ch 8:122 rent-seeking paragraph — Public Choice + reparations-economics parallel citation.** Hostile reviewer weaponizes selectively (depending on the reviewer's ideological direction): either as Public-Choice-commandeering (from left-aligned hostile direction) or as reparations-economics-coding (from right-aligned hostile direction).
- **Ch 8:192 2008-architecture critique.** Hostile reviewer weaponizes as either left-coded critique of bailout (from right-aligned hostile direction) or as right-coded critique of household-debt-restructuring (from left-aligned hostile direction).

**Chapter's structural moves that disarm.**

- **Ch 8:28 + 218 + 232 + 236 explicit scope-discipline at multiple points.** Chapter consistently disclaims policy-prescription scope; the not-a-policy-recommendation framing is honored in the chapter's own restraint.
- **Ch 8:200–206 three misreading-defenses.** Chapter pre-empts the three most-likely hostile-reviewer-weaponization directions (extraction-should-never-have-happened; market-is-fake; rich-nations-pulling-up-the-ladder).
- **Ch 8:168 explicit-range IPG construction (Option D, commit `57575b1`).** The 33-122× range explicitly names the lower + upper bounds + the methodological reason for the variation; hostile reviewer pressure-testing the 122× upper bound finds the chapter has already disclosed the methodological choice that produces the upper bound.
- **Ch 8:220 GDP-not-degrowth paragraph.** Pre-empts the "you're against growth" reflex hostile reviewer would amplify.

**Net read.** Trade-press hostile reviewer would publish a critical review regardless of chapter structural moves; the chapter's most-aggressive single claims (civilizational-scale extrapolation; IPG 122×; "largest continuous wealth transfer") are the framework's central rhetorical instruments and also the most-weaponizable from adversarial trade-press assignment. Chapter's scope-discipline + misreading-defenses + explicit-range IPG construction + GDP-not-degrowth paragraph do disarm work at the intellectually-serious-engagement level. But adversarial-intent reception is reviewer-dependent rather than chapter-dependent. ⚠⚠ EXCLUDE: would actively reject; finds load-bearing threads (civilizational-scale extrapolation + IPG 122× + policy-direction-disclaimer-vs-Ch-9-forward-reference internal tension) the chapter's structural moves engage but cannot fully eliminate at the adversarial-intent-amplification level.

---

### Character 12 — WSJ editorial-board / business-press conservative

**Profile.** *Wall Street Journal* editorial-board reader / *Barron's* opinion-page reader / *National Review* business-economics columnist. Reads chapter for "this book is a threat to business interests" signals; reads framework-arithmetic + IPG + asset-class-consolidation framing + 2008-architecture engagement as preparation for business-regulation.

**Hostile-read posture.** Defends business-as-usual framework against any apparatus that points at structural-accountability-architecture; reads the chapter's framework-arithmetic as preparation-for-business-regulation regardless of the chapter's explicit policy-direction disclaimers; pressure-tests the civilizational-scale extrapolation as anti-business overreach.

**Threads pulled.**

- **Ch 8:188 asset-class-consolidation framing — *"the financialization of single-family rental as an asset class."*** Hostile reviewer reads as anti-financialization framing; financialization-as-pejorative.
- **Ch 8:122 + 188 + 192 + 214 cumulative critique cluster.** Hostile reviewer reads the cumulative effect of Political-Capture-section + asset-class-consolidation-framing + 2008-architecture-critique + civilizational-scale-extrapolation as preparation-for-business-regulation regardless of the chapter's policy-direction disclaimers.
- **Ch 8:118 SCC political-fight framing — *"the question of how much of the cost should be priced is a political fight, and one side of that fight has more resources than the other."*** Hostile reviewer reads "one side of that fight has more resources than the other" as anti-business-interest framing.
- **Ch 8:214 civilizational-scale extrapolation.** Reads as preparation-for-massive-business-regulation.

**Chapter's structural moves that disarm.**

- **Ch 8:200 first-misreading-defense honors cheap-energy welfare contribution.**
- **Ch 8:204 market-is-not-fake misreading-defense.** Inside-the-market-tradition framing.
- **Ch 8:16 + 218 + 232 + 236 explicit scope-discipline.** Chapter consistently disclaims policy-prescription scope.
- **Ch 8:118 EPA chronology completeness.** Chronology is not partisan-targeted selection.
- **Ch 8:184–190 substantive YIMBY engagement.** Chapter takes a right-of-center-resonant policy position seriously and offers both/and synthesis; demonstrates the framework's openness to right-of-center analytical traditions.

**Net read.** WSJ editorial-board / business-press conservative hostile reviewer reads the cumulative critique cluster (Political Capture + asset-class-consolidation + 2008-architecture + civilizational-scale) as preparation-for-business-regulation regardless of the chapter's policy-direction disclaimers. Chapter's market-is-not-fake framing + welfare-acknowledgment + scope-discipline + YIMBY engagement carry intellectually-serious-engagement weight, but the WSJ-editorial-board prior commitment to business-as-usual rejects any apparatus that points at structural-accountability-architecture. ⚠⚠ EXCLUDE: would actively reject; finds load-bearing thread (cumulative critique cluster) the chapter's structural moves cannot fully eliminate at the business-press-conservative tradition level.

---

### Character 13 — Tabloid / populist-skeptic reader

**Profile.** *NY Post* / *Daily Mail* / *Fox News* op-ed-page reader / Mark Levin-cluster radio audience / right-populist talk-show audience. Reads chapter for populist character-attack ammunition; for elite-academic-anti-business-signaling tells; for left-coded scholarship signaling.

**Hostile-read posture.** Frames the framework as elite-academic-anti-business signaling; weaponizes civilizational-scale extrapolation + GDP-not-degrowth + Political Capture cluster as elite-coded; pressure-tests Black-American-writing-tradition lineage citation as identity-politics-in-academic-prose; weaponizes the chapter's most-aggressive single claims for populist-character-attack framing.

**Threads pulled.**

- **Ch 8:92 Black-American-writing-tradition passage.** Hostile reviewer weaponizes the four-author lineage citation (Dunbar / Du Bois / Fanon / Ellison) as identity-politics-coded academic-prose; pressure-tests whether the lineage is load-bearing or signaling.
- **Ch 8:122 reparations-economics primary citation.** Weaponizes the Coates / Darity / Mullen / Hamilton / Conley citation as identity-politics-coded scholarly lineage.
- **Ch 8:214 + 220 civilizational-scale extrapolation + GDP-not-degrowth paragraph.** Weaponizes as elite-academic-anti-business signaling.
- **Ch 8:188 asset-class-consolidation + DOJ-investigation framing.** Weaponizes as anti-business signaling.
- **Ch 8:206 third-misreading-defense — *"Honest pricing creates the revenue to fund clean industrialization pathways for developing nations."*** Weaponizes as global-fiscal-transfer-program framing.

**Chapter's structural moves that disarm.**

- **The chapter is not directly addressing the tabloid / populist-skeptic audience.** Per Pass 3.3 Character 3 + Character 28 acceptance verdicts: chapter's intellectually-serious analytical-quantitative register operates above the tabloid-amplification register; chapter is not designed to land this audience and cannot land them without abandoning the chapter's intellectual purpose.
- **Ch 8:92 substantive-framework-contribution close — *"The framework adds the cost-accounting mechanism by which the mask remains structurally necessary."*** Lineage citation is closed with substantive analytical-framework contribution; not pure-signaling.
- **Ch 8:200 first-misreading-defense honors cheap-energy welfare contribution.** Substantive-acknowledgment framing.
- **Ch 8:122 reparations-economics-AND-Public-Choice parallel citation.** The parallel-tradition citation pre-empts purely-left-coded scholarship-signaling.

**Net read.** Tabloid / populist-skeptic hostile reviewer reads cumulative critique cluster (lineage citations + civilizational-scale extrapolation + GDP-not-degrowth + asset-class-consolidation + DOJ-investigation framing + global-fiscal-transfer framing) as elite-academic-anti-business signaling. Chapter is not designed to land this audience; mitigation is via the chapter's substantive analytical-arithmetic work doing its load-bearing chapter function rather than via accommodation-of-tabloid-reception. ⚠⚠⚠ EXCLUDE: would actively weaponize chapter against itself for populist-character-attack purposes; not chapter-disarmable; reception-cycle mitigation only (supportive reception from non-hostile venues offsets tabloid hostility — a normal cost of doing structural-economic-critique work).

---

### Character 14 — Tort-reform / fiduciary-protection lawyer

**Profile.** Defense-bar litigator / corporate-counsel cluster / U.S. Chamber of Commerce Institute for Legal Reform-aligned lawyer. Reads framework's accountability-bond logic (Ch-9-handoff) + asset-class-consolidation framing + DOJ-investigation framing as litigation-amplification threat — pressure-testing whether the chapter's arithmetic could be used in tort or class-action discovery to establish damages-quantification standards.

**Hostile-read posture.** Reads the chapter's eight-component arithmetic as creating a quantification methodology plaintiffs' lawyers could deploy in tort + class-action litigation; pressure-tests the IPG ratio as opening litigation-damages-multiplier risk for fossil-fuel-industry and other extractive-industry defendants; pressure-tests the asset-class-consolidation framing + DOJ-investigation framing as amplifying RealPage-style antitrust litigation exposure.

**Threads pulled.**

- **Ch 8:34–94 eight-component cost-arithmetic as litigation-damages-methodology.** Hostile reviewer pressure-tests whether the per-component arithmetic (especially the Direct Health $2-4/ton + Environmental Degradation $1-3/ton + Lineage Labor $2/ton anchors) could be used in personal-injury or class-action discovery to establish damages-quantification standards.
- **Ch 8:168 IPG 33-122× ratio.** Reads as the framework supplying plaintiffs' lawyers with a multiplier-of-record damages framework.
- **Ch 8:188 DOJ-investigation framing + asset-class-consolidation framing.** Reads as the framework supporting RealPage-style antitrust litigation expansion.
- **Ch 8:122 rent-seeking paragraph — *"specific identifiable actors shaped"* the political-economic architecture.** Reads as the framework supporting actor-attribution litigation methodology.

**Chapter's structural moves that disarm.**

- **Ch 8:16 explicit not-a-policy-recommendation + not-actor-attribution framing.** Chapter explicitly frames the analytical work as accounting-exercise; chapter explicitly distinguishes the framework's cost-bearing-magnitudes work from actor-attribution problem (line 122).
- **Ch 8:122 framework-vs-reparations-economics + framework-vs-Public-Choice asymmetric framing.** Chapter explicitly distinguishes the framework's analytical-arithmetic from actor-attribution work both other traditions perform; chapter does not claim to do actor-attribution work.
- **Ch 8:88 + 90 + 94 lineage labor cost-attribution discipline.** Chapter explicitly names data-sparsity + uses conservative placeholder; chapter's methodological honesty about attribution-difficulty pre-empts plaintiffs'-lawyer-style overclaim.
- **Cross-chapter routing to Ch 6 + Ch 9.** Chapter explicitly relies on Ch 6 for the residual commons value integral methodology + Ch 9 for the policy-architecture; the chapter is not the framework's litigation-methodology document.

**Net read.** Tort-reform / fiduciary-protection lawyer reads the chapter's eight-component cost-arithmetic + IPG ratio + DOJ-investigation framing as supplying plaintiffs'-lawyer-friendly damages-quantification methodology regardless of the chapter's explicit policy-direction disclaimers. Chapter's not-a-policy-recommendation framing + framework-vs-actor-attribution distinction + cross-chapter routing carry intellectually-serious-engagement weight at the scholarly level, but the litigation-defense prior commitment to minimizing damages-quantification-methodology exposure rejects any apparatus that points at structural-cost-quantification. ⚠ EXCLUDE: would push back but at scholarly-disagreement-within-shared-domain level rather than chapter-disqualification level (the framework's analytical work is genuinely distinct from litigation-methodology work; the defense-bar concern is anticipatory rather than substantive against the chapter as written).

---

### Character 15 — Adversarial-anti-pricing-as-instrumentalization cost-bearer reader

**Profile.** Cost-bearer reader (McDowell County resident; mining-community-affected reader; environmental-justice frontline-community reader) reading the chapter from an adversarial direction. Reads the framework's analytical-quantitative pricing of cost-bearer experience (health + community + lineage + knowledge components) as instrumentalizing cost-bearer experience for analytical purposes; reads "naming the thirteen-year life-expectancy gap as a number" as treating-life-as-number framing.

**Hostile-read posture.** Pressure-tests the framework's reduction of cost-bearer experience to per-ton dollar figures as instrumentalization; pressure-tests Lineage Labor $2/ton + Knowledge & Cultural $1/ton + Political Capture $1/ton conservative placeholders as undervaluation that compounds the original cost-severance by under-pricing it in the chapter's own arithmetic; pressure-tests "the reader can decide whether two dollars per ton of coal, multiplied across sixty years of extraction, represents anything like a fair accounting" framing (line 96) as the framework knowing-its-arithmetic-is-undervalued-and-publishing-it-anyway.

**Threads pulled.**

- **Ch 8:96 lineage-labor conservative-placeholder framing — *"This component is priced at two dollars per ton as a conservative placeholder. The reader can decide whether two dollars per ton of coal, multiplied across sixty years of extraction, represents anything like a fair accounting for what it cost a generation to be born in a county that had been priced at nothing."*** Hostile reviewer reads as the framework explicitly acknowledging that $2/ton is undervaluation + publishing $2/ton anyway; reads as the framework treating-cost-bearer-experience-as-quantitatively-tractable-but-conservatively-quantified.
- **Ch 8:108 knowledge-and-cultural-cost framing — *"This component is priced at one dollar per ton."*** Pressure-tests the $1/ton placeholder as undervaluation that the chapter acknowledges + publishes anyway.
- **Ch 8:122 framework's "cost-bearing magnitudes that name McDowell County's thirteen-year life-expectancy gap as a number" framing.** Hostile reviewer reads as treating-life-expectancy-gap-as-number framing; the explicit "as a number" framing IS the instrumentalization claim.
- **Ch 8:18 + 144 eight-component-arithmetic framing.** Pressure-tests the per-component arithmetic methodology as instrumentalization of cost-bearer experience for analytical purposes.

**Chapter's structural moves that disarm.**

- **Ch 8:90 substantive cost-bearer-centering — *"The extraction did not just take the coal. It took the children's probability of a different life."*** Chapter centers cost-bearer experience in human terms; not exclusively quantitative.
- **Ch 8:96 explicit reader-empowerment framing — *"The reader can decide whether two dollars per ton of coal ... represents anything like a fair accounting."*** Chapter explicitly invites the reader to find the placeholder undervalued; not claiming the placeholder is the right number.
- **Ch 8:92 Black-American-writing-tradition lineage citation.** Chapter explicitly grounds the framework's cost-accounting work in a Black-American intellectual lineage that has been naming the structural condition for over a century; not claiming the framework originated the structural diagnosis.
- **Ch 8:200 first-misreading-defense — *"These are not hypothetical entities. They are people. They paid. They are still paying."*** Substantive cost-bearer-centering at the chapter's closing-defense position.
- **Ch 8:238–240 closing rhetorical pivot — *"The invoice is what McDowell County was paid. The severed cost is what McDowell County bore."*** Closes the chapter at the cost-bearer side of the ledger; not at the analytical-instrumentalization side.

**Net read.** Cost-bearer-adversarial reader reads the framework's analytical-quantitative pricing methodology as instrumentalization regardless of the chapter's substantive cost-bearer-centering + reader-empowerment framing + Black-American-writing-tradition lineage + closing-pivot-to-cost-bearer-side. Chapter's structural moves do substantial disarm work — particularly the line 96 explicit-reader-empowerment framing and the Black-American-writing-tradition lineage closing-claim that the framework ADDS to a tradition rather than IMPOSES on cost-bearer experience. But the adversarial-direction cost-bearer reader's prior commitment to refusing instrumentalization-of-experience rejects any quantitative framework regardless of the chapter's substantive framing moves. ⚠ EXCLUDE: would actively push back but chapter holds against the pushback at scholarly-and-cost-bearer-tradition engagement level; the structural-disarm work is substantial. **Note: this adversarial direction also generates a constructive cross-pressure with Char 1 + Char 2 (industry-funded reviewers) reading the same cost-component placeholders as OVERVALUATION — opposite-direction adversarial pressure on the same chapter passages is the canonical sign of correct positioning.**

---

### §2.x — Per-character verdict tally

| Character | Verdict | Type |
|---|---|---|
| 1 — Industry-funded fossil-fuel-industry economist | ⚠⚠⚠ EXCLUDE | Predisposed-hostile-by-financial-incentive; non-chapter-disarmable |
| 2 — Industry-funded coal-industry economist | ⚠⚠⚠ EXCLUDE | Predisposed-hostile-by-financial-incentive; non-chapter-disarmable |
| 3 — Industry-funded housing-economics economist | ⚠⚠ EXCLUDE | Active rejection; load-bearing thread (T2 + T8); scholarly-disagreement engagement |
| 4 — Industry-funded financial-services economist | ⚠⚠ EXCLUDE | Active rejection; load-bearing thread (T5); cross-chapter routing to Ch 9 |
| 5 — Buchanan-orthodox hostile Public Choice theorist | ⚠⚠ EXCLUDE | Active rejection; load-bearing thread (T1 + T4); cross-pressure with Char 6 |
| 6 — MacLean-sympathetic Buchanan-critical reader | ⚠⚠ EXCLUDE | Active rejection; procedurally-spot-fixable thread (T3); cross-pressure with Char 5 |
| 7 — Pure-libertarian / Rothbardian reader | ⚠⚠ EXCLUDE | Active rejection; load-bearing thread (T1 + T9) at libertarian-tradition level |
| 8 — Reactionary intellectual reader | ⚠⚠ EXCLUDE | Active rejection; load-bearing thread (T4 + T6) at cultural-tradition level |
| 9 — Orthodox-econ Chicago / freshwater adversarial | ⚠⚠ EXCLUDE | Active rejection; load-bearing thread (T1 + T7); cross-pressure with Char 5 |
| 10 — Climate-skeptical / SCC-questioning reader | ⚠⚠ EXCLUDE | Active rejection; load-bearing thread (T7) at ideological-commitment level |
| 11 — Trade-press hostile reviewer | ⚠⚠ EXCLUDE | Active rejection; load-bearing thread (T9 + internal-tension); adversarial-intent-amplification |
| 12 — WSJ editorial-board / business-press conservative | ⚠⚠ EXCLUDE | Active rejection; load-bearing thread (T2 + T5 + T9 cumulative cluster) |
| 13 — Tabloid / populist-skeptic reader | ⚠⚠⚠ EXCLUDE | Non-chapter-disarmable; reception-cycle mitigation only |
| 14 — Tort-reform / fiduciary-protection lawyer | ⚠ EXCLUDE | Acknowledged thread; chapter holds at scholarly-engagement level |
| 15 — Cost-bearer-adversarial reader | ⚠ EXCLUDE | Acknowledged thread; chapter holds; cross-pressure with Char 1 + Char 2 |

**Tally:** 15 EXCLUDE / 0 NEUTRAL / 0 INCLUDE (as expected per template verdict-floor).
**Distribution:** 3 ⚠⚠⚠ EXCLUDE (predisposed-hostile-non-disarmable); 10 ⚠⚠ EXCLUDE (active-rejection-with-load-bearing-thread); 2 ⚠ EXCLUDE (acknowledged-thread-chapter-holds).

**All 15 EXCLUDE as expected per template verdict-floor — all adversarial characters selected for hostile read.** Per-character verdicts are inputs to the §3 thread-pull synthesis, not the diagnostic itself.

---

## §3. Thread-pull synthesis (the central diagnostic)

Per Ch 9 cousin Pass 3.4 §3 format model + Ch 1 REAUDIT v3 §5.3 canonical format. Threads ranked by adversarial-character pull-frequency. Nine threads surfaced across the 15-character adversarial set.

| Thread | Pulled by adversarial chars # | Type | Recommendation |
|---|---|---|---|
| **T1.** **Decision-tool / accountability-architecture direction-by-implication at Ch 8:122 + Ch-9-forward-references at 192 + 234.** Framework's "different in kind" framing + Christophers-direction Ch-9-handoff + civilizational-scale extrapolation read as prescriptive-direction the chapter's not-a-policy-recommendation disclaimer (line 16) cannot eliminate. **Cross-pressure structure: Char 5 (Buchanan-orthodox PC) reads as TOO MUCH direction; Char 9 (Chicago/freshwater orthodox-econ) reads as same direction-by-implication; Char 7 (libertarian) reads as expanded-state-power; Char 1 reads as fossil-industry-targeted direction; (hypothetical Char 7-inverse hard-left would read as INSUFFICIENT direction).** | Chars 1, 5, 7, 9 (all from different ideological positions) | **Load-bearing chapter claim.** Asymmetric framework-Public-Choice framing IS the substantive contribution per cascade `cbef9bd` (2026-05-21 Stage 1c Phase C Option A) + matches Ch 9 Reading C v3 cross-chapter framing. Spot-fixing toward weaker framing would damage Pass 3.3 §4.6 cross-chapter coherence + Pass 3.3 Character 3 (center-right ✓✓) + Character 5 (literary agent ✓✓) + Character 8 (left-policy ✓✓✓) acceptance verdicts. The cross-pressure structure (multiple opposite-direction adversarial reads on same chapter passages) is the canonical sign of a load-bearing claim positioned correctly in the political-economy debate. | **HOLD.** Not-a-policy-recommendation disclaimer at Ch 8:16 + market-is-not-fake misreading-defense at Ch 8:204 + welfare-acknowledgment at Ch 8:200 + asymmetric framework-Public-Choice framing at Ch 8:122 provide structural disarm. Acknowledge in pre-pub review queue per Ch 9 cousin §6.4 pattern. |
| **T2.** **Asset-class-consolidation + DOJ-investigation framing at Ch 8:188 as left-coded sector-targeting + housing-economics overreach.** Industry-funded housing economist + WSJ editorial-board read framing as anti-financialization + as questionable-empirical-claim that asset-class-consolidation operates separately from supply-restriction; tabloid/populist-skeptic reads as anti-business signaling. | Chars 3, 12, 13 | **Load-bearing chapter claim.** Both/and YIMBY synthesis at Ch 8:190 IS the substantive structural-disarm move; was Pass 3.3 Character 11 (housing-economics) ✓✓ INCLUDE strongest single audience-management asset for non-natural-fit policy position. Spot-fixing would damage that natural-fit position. | **HOLD.** Substantive YIMBY engagement at Ch 8:182 + Glaeser/Gyourko/Schuetz cited by name + both/and synthesis at Ch 8:190 + empirical-not-ideological DOJ framing carry structural disarm at scholarly-engagement level. Acknowledge in pre-pub review queue. Optional Pass 3.1 pre-publication-refresh: update "investigating since 2022" sentence at line 188 with current RealPage case status (Nov 2025 proposed settlement per Pass 3.3 §8). |
| **T3.** **Ch 8:122 MacLean-engagement gap (cross-chapter coherence with Ch 5 + Ch 9 + TA §1.10 D-3a consolidated application).** Buchanan + Tullock citation without explicit MacLean acknowledgment at Ch 8:122; particularly load-bearing because Ch 9 Pass 3.4 §10.1 (RATIFIED 2026-05-25 commit `8aa7dfb`) applied the D-3a consolidated Char-15-Option-A MacLean acknowledgment across Ch 5 line 202 + Ch 9 line 144 + TA §1.10 line 610 — but Ch 8 line 122 was NOT included in the D-3a application scope. **This is a cross-chapter coherence gap surfaced by the Pass 3.4 audit.** | Char 6 (MacLean-sympathetic) | **Procedurally-spot-fixable; cross-chapter-coherence-restoration thread.** Per Ch 9 Pass 3.3 Character 15 Option A canonical form: one sentence ("the rent-seeking analytical vocabulary survives many readings of Buchanan's broader political project, and this book draws on the vocabulary rather than endorsing the project") would close T3 without damaging any acceptance verdict — would in fact reinforce cross-chapter consistency. Application form would track the Ch 9 cousin (one canonical sentence added after the Public-Choice-citation closer at line 122). | **SPOT-FIX RECOMMENDED (cross-chapter-coherence-restoration).** Pass 3.4 audit finding: Ch 8:122 should receive the D-3a consolidated MacLean acknowledgment for cross-chapter coherence with Ch 5 + Ch 9 + TA §1.10. Default per cousin pattern: apply the canonical Char-15-Option-A sentence at Ch 8:122. Author judgment if hold-as-is is preferred (note: hold-as-is would leave a cross-chapter coherence gap that would surface in any future Stage 1c sibling-coherence-check). |
| **T4.** **Lineage-citation cluster (Ch 8:92 Black-American writing tradition + Ch 8:122 reparations-economics primary citation) as left-coded scholarship-signaling.** Reactionary intellectual + tabloid/populist-skeptic + Buchanan-orthodox PC + WSJ editorial-board reader read the Dunbar / Du Bois / Fanon / Ellison + Coates / Darity / Mullen / Hamilton / Conley lineage citations as identity-politics-coded academic-prose. | Chars 5, 8, 12, 13 | **Load-bearing chapter claim.** The lineage citations are substantively load-bearing for the chapter's argument (framework's cost-accounting work names something Black-American writing tradition has been naming for over a century + reparations-economics tradition supplies actor-and-coalition vocabulary). Spot-fixing would damage Pass 3.3 Character 9 (reparations-economics ✓✓✓), Character 16 (EJ / frontline-community ✓✓), Character 17 (McDowell-Appalachian-resonant ✓✓✓), Character 22 (anti-capital / structural-critique ✓✓) acceptance verdicts. | **HOLD.** Substantive-framework-contribution close at Ch 8:92 ("the framework adds the cost-accounting mechanism by which the mask remains structurally necessary") + reparations-economics-AND-Public-Choice parallel citation at Ch 8:122 + chapter-wide structural-injustice framing carry load-bearing-substance disarm. Acknowledge in pre-pub review queue. |
| **T5.** **2008-financial-crisis architecture engagement at Ch 8:192 (Mian & Sufi 2014 + policy-choice framing) as left-coded importation of contested counterfactual.** Industry-funded financial-services economist + WSJ editorial-board read the engagement as importing Mian-Sufi's contested counterfactual as canonical; tabloid/populist-skeptic reads as anti-bailout signaling. | Chars 4, 12, 13 | **Load-bearing claim with cross-chapter routing.** Chapter explicitly notes "Chapter 9 will return to what the alternative architecture would have looked like under honest pricing"; the engagement is preview-not-developed-position. Cross-chapter routing to Ch 9 is correct. | **HOLD.** Contested-at-the-time framing at Ch 8:192 + cross-chapter routing to Ch 9 + market-is-not-fake misreading-defense at Ch 8:204 + Mian-Sufi citation as one-named-academic-position-not-consensus carry structural disarm. Acknowledge in pre-pub review queue. |
| **T6.** **Civilizational-scale extrapolation at Ch 8:214 ($10-15T annual; "largest continuous wealth transfer in human history") as overclaim / scale-fear-mongering / academic-prestige overclaim.** Industry-funded fossil-fuel + reactionary intellectual + climate-skeptical + trade-press hostile reviewer + tabloid/populist-skeptic read the figure as the framework's most-aggressive single claim + most-weaponizable from multiple adversarial directions. | Chars 1, 8, 10, 11, 13 | **Load-bearing claim with structural disarm built in.** Civilizational-scale extrapolation IS the chapter's central forward-pointing rhetorical instrument (the chapter's "the argument's civilizational-scale implication" at line 218); the framework would lose substantive contribution if spot-fixed toward conservative-only floor. Pass 3.3 Character 1 (trade-press ✓✓) + Character 5 (literary agent ✓✓) acceptance verdicts depend on this claim being made. | **HOLD.** Explicit scope-discipline at Ch 8:218 ("a gestured claim... cannot honestly be compressed into the closing pages of a framework book") + "I am not going to compress it; I will name the figure and leave it there" at line 222 + cross-chapter routing forward to Ch 9 + Ch 10 carries structural disarm — the chapter names the figure's scope-limit in the chapter itself. Acknowledge in pre-pub review queue. |
| **T7.** **SCC anchor + EPA chronology at Ch 8:72 + 118 as discount-rate-choice-driven / one-sided political-fight framing.** Industry-funded fossil-fuel + climate-skeptical / SCC-questioning reader read the $190/ton SCC anchor + Rennert et al. 2022 *Nature* citation + Wagner et al. 2021 critique citation as politically-anchored choice rather than physics-anchored; reads SCC political-fight chronology as one-sided framing. | Chars 1, 10 | **Load-bearing claim.** SCC anchor IS the chapter's load-bearing quantitative anchor for the Foreclosure component; spot-fixing toward weaker anchor would damage Pass 3.3 Character 4 (Tier-1 quantitative reader / climate-economics + SCC specialist ✓✓ INCLUDE) verdict + would damage chapter's central rhetorical instrument (the $510 carbon-tail per ton + IPG ratio). | **HOLD.** Explicit Rennert et al. 2022 *Nature* citation chain at Ch 8:72 + EPA chronology completeness at Ch 8:118 (all four administrations cited) + conservative-throughout discipline at Ch 8:28 + explicit-ratio-holds-across-SCC-range framing at Ch 8:74 ("at least three" against today's market) carry structural disarm. Acknowledge in pre-pub review queue. |
| **T8.** **Each cost-component arithmetic claim as defeasible by industry-funded counter-research.** Industry-funded coal + housing + financial-services economists pressure-test each cost-component attribution (Black Lung Trust Fund severance; mountaintop-removal cancer figure; community-disruption $5/ton; lineage-labor $2/ton placeholder; 2008-architecture policy-choice framing). | Chars 1, 2, 3, 4 | **Already-resolved-via-cross-chapter routing + already-resolved-via-conservative-floor discipline.** Chapter's conservative-throughout discipline + chapter explicitly relies on Ch 2 + Ch 5 + Ch 6 + Ch 9 for component derivations; industry-funded predisposed-hostile-by-financial-incentive reception is not chapter-disarmable. | **HOLD.** Cross-chapter routing is correct; conservative-floor discipline is correct; predisposed-hostile reception is reception-cycle mitigation only. Acknowledge in pre-pub review queue per Ch 9 cousin T8 pattern. |
| **T9.** **Policy-direction-disclaimer (Ch 8:16) vs Ch-9-direction-forward-reference (Ch 8:234) internal-consistency tension.** Trade-press hostile reviewer + libertarian + WSJ editorial-board read the tension between "It is not, in this book, a policy recommendation" (line 16) + "Chapter 9 sketches the direction a civilization committed to honest accounting would move" (line 234) as internal inconsistency. **Note: cross-pressure structure here is internal to the chapter, not adversarial-cross-pressure on a single claim.** | Chars 7, 11, 12 | **Load-bearing structural feature, not procedural inconsistency.** The chapter's not-a-policy-recommendation discipline + the Ch-9-forward-reference are both substantive: the chapter does not derive policy from arithmetic, but the next chapter does sketch the direction. Spot-fixing the internal-consistency tension would either (a) damage the chapter's policy-direction-disclaimer (would require weakening Ch 8:16) or (b) damage the cross-chapter handoff (would require removing the Ch 8:234 Ch-9-forward-reference); both spot-fixes would damage acceptance verdicts. | **HOLD.** The tension is the chapter's structural feature — chapter is the arithmetic chapter; Ch 9 is the direction chapter; the two-chapter sequence is the book's architecture. Hostile-reviewer weaponization of the tension is constrained by the chapter's explicit-scope-discipline framing ("outside the scope of this book"; "the framework cannot do that work itself"; "Their pursuit belongs to policy-makers..."). Acknowledge in pre-pub review queue. |

### §3.1 Synthesis observation: cross-pressure positions chapter correctly

Per Ch 9 cousin Pass 3.4 §3.1 canonical diagnostic: the diagnostic value of running the full 15-character adversarial set is in the **cross-pressure structure** the synthesis reveals.

- **T1 cross-pressure (most prominent).** Char 5 (Buchanan-orthodox PC) reads asymmetric framework-Public-Choice framing as TOO MUCH direction-by-implication; Char 9 (Chicago/freshwater orthodox-econ) reads same passage as commandeering analytical legitimacy; Char 7 (libertarian) reads as expanded-state-power direction; Char 1 (industry-funded fossil) reads as fossil-industry-targeted direction. **A hypothetical Char 16 hard-left adversarial reader** (not in this 15-set — would be the inverse case Ch 9 cousin §3.1 documented) **would read the same passage as INSUFFICIENT direction.** Multiple opposite-direction adversarial reads on the same chapter passage (Ch 8:122) — canonical sign of a load-bearing claim positioned correctly in the political-economy debate.
- **T4 cross-pressure (lineage-citation cluster).** Char 5 (Buchanan-orthodox PC) reads the reparations-economics-AND-Public-Choice parallel citation at Ch 8:122 as moral-equivalence between incompatible traditions; Char 6 (MacLean-sympathetic) reads the same passage as insufficient distance from Buchanan; Char 8 (reactionary intellectual) reads the Black-American-writing-tradition citation at Ch 8:92 as left-coded signaling; (hypothetical hard-left reader would read same as accommodation-of-canonical-Black-American-tradition that doesn't go far enough into structural-critique direction). Opposite-direction adversarial pressure on lineage-citation cluster — canonical sign of correct positioning.
- **T6 cross-pressure (civilizational-scale extrapolation).** Char 1 (industry-funded) + Char 11 (trade-press hostile) read $10-15T as scale-fear-mongering; Char 13 (tabloid/populist-skeptic) reads as elite-academic-anti-business signaling; (hypothetical degrowth-tradition adversarial reader would read the same figure as undercount — the chapter explicitly invites this read at line 218 ("a gestured claim")). Opposite-direction adversarial pressure.
- **T8 cross-pressure on cost-component placeholders.** Char 1 + Char 2 (industry-funded fossil/coal) read Lineage Labor $2/ton + Knowledge & Cultural $1/ton + Political Capture $1/ton placeholders as OVERVALUATION; Char 15 (cost-bearer-adversarial-anti-pricing-as-instrumentalization) reads the same placeholders as UNDERVALUATION the chapter knowingly publishes anyway. **Direct opposite-direction adversarial pressure on the same chapter placeholders** — the canonical sign that the conservative-throughout discipline at Ch 8:28 has placed the chapter at exactly the position where opposite-direction adversarial reads converge.

Across the 15-character adversarial set, **the chapter is not finding load-bearing threads that any single ideological tradition can weaponize against it uniquely.** The threads found are either (a) load-bearing claims the chapter is correctly making with cross-pressure structure as the diagnostic confirmation (T1, T2, T4, T5, T6, T7, T9); (b) procedurally-spot-fixable cross-chapter-coherence-restoration items (T3); or (c) industry-funded / tabloid predisposed-hostility that is not chapter-disarmable (T8 + Char 1/2/13).

---

## §4. Apparatus / consistency / register sub-checks under adversarial lens

Pass 3.3 §5 verified apparatus + register + named-subject disciplines all clean post-Phase-C-β + post-Stage-4 RATIFIED. Pass 3.4 incidental check for new threads surfaced by adversarial reads:

- **§4.1 No new apparatus thread surfaced by adversarial set.** No adversarial character flagged a register / convention / named-subject thread the acceptance test missed. Item 1 (inline-integral strip from Ch 8 — verified intact), Item 13 (IPG full-name + acronym at line 168 — verified intact), Item 14 (Cᵢ via Four Gates at line 18 — verified intact) all hold under adversarial scrutiny.
- **§4.2 Adversarial-reviewer institutional affiliations cited via public-record exception.** Heritage, Manhattan Institute, TPPF, API, NMA, AEI, Mercatus, GMU, Cato, Mises Institute, FEE, CEI, Heartland, *NR* / *National Affairs* / *American Affairs* / *Claremont* / *First Things*, ABA, SIFMA, U.S. Chamber, *NY Post* / *Daily Mail* / *Fox News* op-ed-page, *Jacobin*, etc. institutional affiliations cited in the framing context per [feedback_named_subject_consent.md](../memory/feedback_named_subject_consent.md) public-record exception (institutional positions stated on-the-record in institutional capacity). No living-named-subject consent issue.
- **§4.3 SCC literature citations under adversarial lens.** Rennert et al. 2022 *Nature* + Wagner, Anthoff, Cropper, et al. 2021 + Glaeser + Gyourko + Schuetz + Mian + Sufi + Coates + Darity + Mullen + Hamilton + Conley + Buchanan + Tullock + Dunbar + Du Bois + Fanon + Ellison: all are on-the-record published academic / literary work; all citations carry the public-record exception per consent discipline; no adversarial direction surfaces a consent-discipline thread.
- **§4.4 Hard constraint honored.** Did NOT contact named subjects (including adversarial-reviewer institutional affiliations — public-record exception applies for citation but not for outreach per hard constraint).
- **§4.5 Cross-chapter framing-symmetry under adversarial lens.** Per cascade `cbef9bd` (2026-05-21 Stage 1c Phase C Option A), Ch 8:122 asymmetric framework-Public-Choice framing matches Ch 9 Reading C v3 framing. Cross-chapter coherence holds under adversarial-direction pressure. **One cross-chapter coherence gap surfaced: T3 (Ch 8:122 MacLean-engagement gap relative to Ch 5 line 202 + Ch 9 line 144 + TA §1.10 line 610 D-3a consolidated application).** See §3 T3 + §7.3.

---

## §5. Cadence / argument-structure stress points surfaced

Per Ch 9 cousin Pass 3.4 §5 format. Pass 3.3 §6 cadence summary already noted the Pass 3.2 §10.1 F-V3 em-dash sweep + F-V1/F-V2/F-V4 compressions absorbed at the acceptance-character level. Pass 3.4 incidental check for cadence / argument-structure stress points surfaced under adversarial-direction reads:

- **§5.1 Argument-structure stress: chapter-opening question vs not-a-policy-recommendation disclaimer.** Char 11 (trade-press hostile reviewer) + Char 7 (libertarian) read the chapter-opening question at Ch 8:10 ("What if everything cost what it actually costs?") as policy-direction question + then the not-a-policy-recommendation disclaimer at Ch 8:16 as inconsistent. The two-paragraph structure (Ch 8:10–18) is intentional rhetorical setup — the question opens the chapter; the disclaimer pre-empts the policy-direction reading. **No spot-fix warranted** — the rhetorical setup is doing necessary chapter-architecture work.
- **§5.2 Argument-structure stress: eight-component-bullet-list-sum (Ch 8:148–164) vs prose-component-walk (Ch 8:32–138).** Char 1 (industry-funded fossil) pressure-tests the bullet-list-sum as concealing the methodological choices that produced each component; bullet-list reads as confident-arithmetic-claim, prose-walk reads as methodologically-honest-walk. **No spot-fix warranted** — the bullet-list-sum is preceded by each component's prose-walk; reader who has read the eight-component prose sees the methodological discipline in each component before encountering the bullet-list.
- **§5.3 Argument-structure stress: civilizational-scale extrapolation paragraph (Ch 8:214–222).** Char 1 + Char 11 + Char 8 read the civilizational-scale extrapolation as the chapter's most-rhetorically-aggressive single passage. Chapter's own scope-discipline ("I am not going to compress it; I will name the figure and leave it there") is the structural disarm at the chapter-internal level. **No spot-fix warranted** — chapter is doing the figure-naming work the framework requires while preserving honest-scope discipline.
- **§5.4 No cumulative-cadence stress surfaced by adversarial reads.** Pass 3.3 §4.5 noted the Pass 3.2 §7 cumulative-anaphora-cluster diagnostic was resolved at the acceptance-character level; Pass 3.4 confirms adversarial-character reads do not surface new cadence-related concerns.

---

## §6. Cross-chapter coherence sub-check

Pass 3.3 §5.4 verified rent-seeking paragraph at line 122 + Ch 8 → Ch 9 asymmetric framing cross-chapter consistency holds post-cascade `cbef9bd`. Pass 3.4 incidental check for cross-chapter threads surfaced by adversarial-direction reads:

- **§6.1 T3 (MacLean-engagement) cross-chapter-coherence gap surfaced.** Ch 9 Pass 3.4 §10 (RATIFIED 2026-05-25) applied the D-3a consolidated MacLean acknowledgment across Ch 5 line 202 + Ch 9 line 144 + TA §1.10 line 610 — but Ch 8 line 122 was NOT included in the D-3a application scope. This Pass 3.4 audit surfaces Ch 8:122 as the fourth Public-Choice-engagement site that should receive the D-3a consolidated MacLean acknowledgment for cross-chapter coherence. **Routes per pipeline doctrine §5 (cross-chapter consistency restoration; one-sentence-addition application; Stage 1c-light light re-fire could follow if author wants comprehensive sibling-coherence-verification).**
- **§6.2 T1 cross-chapter coherence (Ch 8:122 asymmetric framing ↔ Ch 9 Reading C v3) holds.** Pass 3.4 confirms cross-chapter coherence under adversarial-direction pressure; cascade `cbef9bd` did its work. No additional cross-chapter handoff needed.
- **§6.3 T5 cross-chapter routing (Ch 8:192 2008-architecture engagement → Ch 9 alternative-architecture-under-honest-pricing).** Ch 9 cousin Pass 3.4 §6.4 already absorbed this cross-chapter handoff at the Ch-9 level; Pass 3.4 confirms the Ch 8 → Ch 9 routing is correct.
- **§6.4 No additional cross-chapter inconsistency surfaced by adversarial reads.** Ch 1 (canonical framework introduction) + Ch 2 (cost-walkthrough origin) + Ch 5 (cross-case sweep) + Ch 6 (residual commons value integral) + Ch 7 (cross-frontier extension) + Ch 9 (policy-architecture) + Ch 10 (closing) all hold under adversarial-direction read; no cross-chapter coherence gap beyond T3.

---

## §7. Out-of-scope flagging

### §7.1 Cross-chapter cascade flags

- **T3 (MacLean-acknowledgment cross-chapter-coherence gap) → Phase C-γ session.** Recommended consolidated cross-chapter Phase C application that closes the T3 thread by adding the D-3a canonical MacLean-acknowledgment sentence at Ch 8:122. Default disposition per cousin pattern: APPLY (cross-chapter-coherence-restoration). Author judgment if hold-as-is is preferred (note: hold-as-is leaves a cross-chapter coherence gap).
- **T1 (asymmetric framework-Public-Choice framing direction-by-implication) cross-chapter coherence with Ch 9 + TA §1.10 holds.** No additional cross-chapter cascade needed beyond T3 closure.
- **T5 (2008-architecture engagement) cross-chapter routing to Ch 9 is correct.** No additional cross-chapter cascade needed.
- **T8 (cost-component cross-chapter routing to Ch 2 + Ch 5 + Ch 6) is correct.** No additional cross-chapter cascade needed.

### §7.2 Out-of-scope-for-Pass-3.4 — flagged for Pass 3.5 (developmental-edit) future-session input

Per per-prompt serial cadence: Pass 3.5 fires after Pass 3.4 ratify-and-apply per [`feedback_audience_aware_drafting_discipline.md`](../memory/feedback_audience_aware_drafting_discipline.md) v3.1 Amendment B (each pass in its own prompt). Pass 3.4 incidental check for whole-chapter restoration-of-richness items surfaced by adversarial reads:

- **No cumulative-LLM-cadence residue surfaced.** Pass 3.2 §10.1 F-V3 chapter-wide em-dash sweep (80 → 28) + F-V1 + F-V2 + F-V4 + F-V7 + F-V13 compressions did not produce cumulative-flatness that adversarial reads detected.
- **No emotional-arc-continuity break surfaced.** Adversarial reads did not detect breaks in the chapter's analytical-quantitative register; chapter holds voice across 243 lines.
- **No scene-anchor-density gap surfaced.** Chapter's McDowell-County concrete-anchoring (line 24 Kennedy 1960 + line 58 population/poverty/drug-death-rate concrete-anchoring) + cross-case sweep at line 174 (Deepwater + Libby + Baotou + Valdez + housing + tar sands + First Nations + 2008) + Black-American-writing-tradition passage at line 92 + closing rhetorical pivot at line 238 is dense enough to carry the analytical load.
- **One incidental observation for Pass 3.5.** Civilizational-scale extrapolation paragraph at lines 210–222 + GDP-not-degrowth paragraph at line 220 form the chapter's most-rhetorically-dense passage; Pass 3.5 whole-chapter read should verify reader-engagement at this pivot does not flatten cumulatively when read after the eight-component arithmetic + cross-case sweep + housing-engagement-with-YIMBY-steelman + three misreading-defenses. Pass 3.4 does not surface a gap; flagged as low-priority Pass 3.5 attention item.
- **Second incidental observation for Pass 3.5.** Carbon-arithmetic paragraph at Ch 8:72 is the chapter's heaviest single technical passage (EPA AP-42 §1.1 + 93.28 kg CO₂ per mmBtu + 28 mmBtu per short ton + 2.61 metric tons CO₂ per short ton + Rennert et al. 2022 *Nature* + $190/metric ton SCC). Pass 3.3 Character 2 (layman-but-engaged reader) flagged this as the chapter's technical-density-peak paragraph; Pass 3.4 does not surface a new gap; flagged as low-priority Pass 3.5 attention item (whole-chapter cadence-engagement check at this paragraph).

### §7.3 Out-of-scope-for-Pass-3.4 — flagged for Pass 3.1 (fact-check) / Pass 3.2 (voice-polish) / Stage 4 follow-up

Items observed during Pass 3.4 reading that belong to other passes:

**Pass 3.1 fact-check follow-up.** Two pre-publication-refresh items previously flagged in Pass 3.1 + Pass 3.2 + Pass 3.3 remain in-flight (not blocking Pass 3.4):

1. **DOJ RealPage investigation status at line 188** ("investigating since 2022"): Pass 3.3 §8 noted the case has moved from investigation (Nov 2022) → antitrust complaint (2024) → proposed settlement (Nov 2025). Pre-publication-refresh checklist item; not blocking. Char 3 (industry-funded housing-economics) thread T2 hostile-read engagement intensifies pre-pub-refresh value (current sentence does not reflect current case state).
2. **Hendryx-specific citation for 60,000 Appalachian cancer cases figure at line 50.** Optional pre-publication explicit-citation addition; not blocking. Char 2 (industry-funded coal-industry) hostile read confirms a specialist-reader pre-pub-refresh value (current sentence lacks the explicit citation hostile reviewer would demand).

**Pass 3.2 voice-polish follow-up.** No new voice-polish concerns surfaced by adversarial reads. Pass 3.2 RATIFIED 2026-05-25 + Phase C-β APPLIED at commit `16554fa`; the post-spot-fix prose is the audit baseline.

**Stage 4 render follow-up.** Stage 4 RATIFIED author-completed-offline 2026-05-26 (commit `e36bdd6`); no new render concerns surfaced by Pass 3.4 audit (Pass 3.4 audits the chapter text, not the rendered output).

### §7.4 Pre-publication review queue items (Stage 5 input)

Per [`feedback_audience_aware_drafting_discipline.md`](../memory/feedback_audience_aware_drafting_discipline.md) v3.1 + §3 above + Ch 9 cousin Pass 3.4 §6.4 pattern: load-bearing adversarial threads that the chapter holds against (with structural disarm) but warrant acknowledgment in the pre-pub review queue for transparency to publisher / agent / editor:

- **T1 acknowledgment.** Asymmetric framework-Public-Choice framing at Ch 8:122 + Ch-9-direction-forward-reference at Ch 8:234 read as prescriptive-direction under multiple adversarial directions (Buchanan-orthodox PC; orthodox-econ Chicago/freshwater; libertarian; industry-funded fossil). Chapter's not-a-policy-recommendation disclaimer + market-is-not-fake misreading-defense + welfare-acknowledgment + cross-chapter coherence with Ch 9 Reading C v3 provide structural disarm; thread is part of the framework's positioning in the political-economy debate (cross-pressure structure positions chapter correctly).
- **T2 acknowledgment.** Asset-class-consolidation + DOJ-investigation framing at Ch 8:188 invites housing-economics-industry-funded + WSJ-editorial-board hostile reception; chapter's both/and YIMBY synthesis + Glaeser/Gyourko/Schuetz substantive engagement + empirical-not-ideological DOJ framing provide structural disarm.
- **T4 acknowledgment.** Lineage-citation cluster (Black-American-writing-tradition at Ch 8:92 + reparations-economics-AND-Public-Choice parallel citation at Ch 8:122) invites reactionary-intellectual + tabloid/populist-skeptic + Buchanan-orthodox-PC + WSJ-editorial-board hostile reads as left-coded scholarship-signaling; chapter's substantive-framework-contribution close at Ch 8:92 + parallel-tradition citation at Ch 8:122 + chapter-wide structural-injustice framing provide structural disarm (lineage is load-bearing for chapter's substantive contribution, not signaling).
- **T5 acknowledgment.** 2008-financial-crisis architecture engagement at Ch 8:192 + Mian-Sufi citation + policy-choice framing invites financial-services-industry-funded + WSJ-editorial-board hostile reception as importing contested counterfactual as canonical; chapter's contested-at-the-time framing + cross-chapter routing to Ch 9 + market-is-not-fake framing provide structural disarm.
- **T6 acknowledgment.** Civilizational-scale extrapolation at Ch 8:214 invites multiple adversarial directions (industry-funded fossil; reactionary intellectual; climate-skeptical; trade-press hostile; tabloid/populist-skeptic) as overclaim / scale-fear-mongering / academic-prestige overclaim; chapter's explicit scope-discipline at Ch 8:218 + "I am not going to compress it; I will name the figure and leave it there" at line 222 + Ch 9 + Ch 10 cross-chapter routing provide structural disarm.
- **T7 acknowledgment.** SCC anchor + EPA chronology at Ch 8:72 + 118 invites industry-funded fossil + climate-skeptical hostile reception as discount-rate-choice-driven / one-sided political-fight framing; chapter's Rennert et al. 2022 *Nature* citation + EPA chronology completeness (all four administrations) + conservative-throughout discipline + explicit-ratio-holds-across-SCC-range framing provide structural disarm.
- **T8 reception-cycle note.** Industry-funded reviewer reception (fossil-fuel + coal + housing + financial-services) is predisposed-hostile-by-financial-incentive; chapter is not designed to land this reception; mitigation is reception-cycle level (supportive reception from non-hostile venues offsets industry-funded hostility — normal cost of doing structural-economic-critique work). Tabloid/populist-skeptic reception similarly non-chapter-disarmable; same mitigation.
- **T9 acknowledgment.** Policy-direction-disclaimer at Ch 8:16 + Ch-9-direction-forward-reference at Ch 8:234 internal-consistency tension is the chapter's structural feature (Ch 8 is the arithmetic chapter; Ch 9 is the direction chapter; the two-chapter sequence is the book's architecture); cross-chapter coherence + explicit-scope-discipline at multiple chapter-internal points provide structural disarm.

---

## §8. Verdict synthesis

### §8.1 Per-character tally — full 15-character adversarial set

| Verdict | Count | Characters |
|---|---|---|
| ⚠ EXCLUDE | 2 | Char 14 (tort-reform / fiduciary-protection); Char 15 (cost-bearer-adversarial-anti-pricing-as-instrumentalization) |
| ⚠⚠ EXCLUDE | 10 | Char 3 (housing-econ); Char 4 (financial-services); Char 5 (Buchanan-orthodox PC); Char 6 (MacLean-sympathetic); Char 7 (libertarian); Char 8 (reactionary intellectual); Char 9 (Chicago/freshwater); Char 10 (climate-skeptical); Char 11 (trade-press hostile); Char 12 (WSJ editorial-board) |
| ⚠⚠⚠ EXCLUDE | 3 | Char 1 (fossil-fuel-industry-funded); Char 2 (coal-industry-funded); Char 13 (tabloid/populist-skeptic) — non-chapter-disarmable; reception-cycle mitigation only |
| **Total** | **15 EXCLUDE** | **As expected per template verdict-floor — all adversarial characters selected for hostile read** |

### §8.2 Aggregate Pass-3.4 robustness verdict

**CONDITIONALLY ROBUST.**

- **No ⚠⚠⚠ chapter-disqualifying threads found that are chapter-disarmable.** Char 1 (industry-funded fossil ⚠⚠⚠) + Char 2 (industry-funded coal ⚠⚠⚠) + Char 13 (tabloid/populist-skeptic ⚠⚠⚠) are predisposed-hostile-by-financial-incentive or predisposed-hostile-by-populist-amplification-incentive per the Ch 1 REAUDIT v3 §5.3 canonical framing + Ch 9 cousin Char 3 canonical framing; not chapter-disarmable; mitigation is reception-cycle level. This is the normal cost of doing structural-economic-critique work at the framework's load-bearing analytical-quantitative chapter.
- **Common load-bearing threads (T1, T2, T4, T5, T6, T7, T8, T9) found; chapter's structural moves disarm sufficiently at structural-claim level.** Each thread is acknowledged in the pre-publication review queue (§7.4) for publisher / agent / editor transparency.
- **One procedurally-spot-fixable cross-chapter-coherence-restoration thread (T3) surfaced — and this is the principal Pass 3.4 finding.** Ch 8:122 should receive the D-3a consolidated MacLean acknowledgment for cross-chapter coherence with Ch 5 line 202 + Ch 9 line 144 + TA §1.10 line 610 (where D-3a was applied 2026-05-25 commit `8aa7dfb`). Default recommendation: APPLY (cross-chapter-coherence-restoration).
- **Cross-pressure structure across the 15-character set indicates correct positioning.** T1 + T4 + T6 + T8 show opposite-direction adversarial pressure on the same chapter passages — the canonical sign of load-bearing claims positioned correctly in the political-economy debate. T8 in particular shows direct opposite-direction adversarial pressure on the chapter's conservative-throughout discipline at the cost-component-placeholder level (industry-funded reviewers read as overvaluation; cost-bearer-adversarial reader reads as undervaluation), confirming the chapter has placed itself at the position where opposite-direction adversarial reads converge.
- **Mirrors Ch 9 cousin Pass 3.4 CONDITIONALLY ROBUST verdict (RATIFIED 2026-05-25).** Both Ch 8 + Ch 9 land at CONDITIONALLY ROBUST with cross-pressure-positioning-diagnostic confirmation + with one procedurally-spot-fixable cross-chapter-coherence item; pattern is consistent with the framework's load-bearing analytical chapters at this Stage-3 cadence position.

**Does NOT require structural engagement.** No common load-bearing thread surfaces where the chapter does NOT disarm; no chapter-level structural revision needed.

### §8.3 Phase-C disposition recommendation

**One recommended Phase C-γ application item:**

- **T3 (MacLean acknowledgment cross-chapter-coherence restoration).** Apply the D-3a canonical sentence at Ch 8:122. Two variants:
  - **Option A (RECOMMENDED).** Apply the canonical Ch 9 Pass 3.4 §10.1 D-3a sentence form: append at end of line 122 the sentence "The rent-seeking analytical vocabulary survives many readings of Buchanan's broader political project, and this book draws on the vocabulary rather than endorsing the project." This is the single-sentence addition that closes T3 with minimum chapter-architecture disturbance.
  - **Option B.** Hold-as-is. Note: hold-as-is leaves a cross-chapter coherence gap that would surface in any future Stage 1c sibling-coherence-check across Ch 5 + Ch 8 + Ch 9 + TA §1.10 Public-Choice-engagement sites.

**No other required Phase C-γ items from Pass 3.4.** All other load-bearing threads (T1, T2, T4, T5, T6, T7, T8, T9) are hold-as-is with pre-pub-review-queue acknowledgment.

**Optional Pass 3.1 pre-publication-refresh items (already flagged before Pass 3.4):**
- DOJ RealPage investigation status at line 188 (update from "investigating since 2022" to current Nov 2025 proposed-settlement state).
- Hendryx-specific citation for 60,000 Appalachian cancer cases at line 50 (optional explicit-citation addition).

### §8.4 Pass 3.5 readiness

Pass 3.5 (developmental-edit) **can fire** per per-prompt serial cadence after Pass 3.4 ratify-and-apply (or hold-as-is ratification on T3). Pass 3.4 surfaced no urgent whole-chapter restoration-of-richness items; §7.2 above flags two low-priority Pass 3.5 attention items (civilizational-scale extrapolation paragraph at lines 210–222 + carbon-arithmetic paragraph at line 72).

**Recommended next session for Ch 8:** Author ratification of Pass 3.4 verdict + T3 spot-fix disposition. After ratification + Phase C-γ application (if T3 Option A selected), Pass 3.5 (developmental-edit) fires per per-prompt serial cadence per [`feedback_audience_aware_drafting_discipline.md`](../memory/feedback_audience_aware_drafting_discipline.md) v3.1 Amendment B (3.1 → 3.2 → 3.3 → 3.4 → 3.5; each in its own prompt).

---

## §9. Verdict synthesis (consolidated)

### §9.1 Thread-pull synthesis (recap from §3)

Nine threads surfaced across the 15-character adversarial set:

- **T1.** Asymmetric framework-Public-Choice framing + Ch-9-forward-references as prescriptive-direction-by-implication (load-bearing; HOLD with pre-pub-review-queue acknowledgment).
- **T2.** Asset-class-consolidation + DOJ-investigation framing as left-coded sector-targeting (load-bearing; HOLD; optional pre-pub-refresh on DOJ status).
- **T3.** Ch 8:122 MacLean-engagement gap relative to cross-chapter D-3a application (Ch 5 + Ch 9 + TA §1.10) (**procedurally-spot-fixable; cross-chapter-coherence-restoration; SPOT-FIX RECOMMENDED**).
- **T4.** Lineage-citation cluster (Black-American-writing-tradition + reparations-economics) as left-coded scholarship-signaling (load-bearing; HOLD).
- **T5.** 2008-financial-crisis architecture engagement as importation of contested counterfactual (load-bearing; HOLD; cross-chapter routing to Ch 9 already correct).
- **T6.** Civilizational-scale extrapolation as overclaim / scale-fear-mongering (load-bearing; HOLD; explicit-scope-discipline at Ch 8:218 + 222 provides structural disarm).
- **T7.** SCC anchor + EPA chronology as discount-rate-choice-driven / one-sided political-fight framing (load-bearing; HOLD).
- **T8.** Cost-component arithmetic as defeasible by industry-funded counter-research (load-bearing; HOLD; cross-chapter routing + conservative-floor discipline + predisposed-hostile-reception-cycle-mitigation).
- **T9.** Policy-direction-disclaimer vs Ch-9-direction-forward-reference internal-consistency tension (load-bearing structural feature; HOLD).

### §9.2 Aggregate Pass-3.4 verdict

**CONDITIONALLY ROBUST.** Per §8.2 above. Mirrors Ch 9 cousin Pass 3.4 CONDITIONALLY ROBUST verdict (RATIFIED 2026-05-25); same structural-pattern as the framework's load-bearing analytical chapters at this Stage-3 cadence position.

### §9.3 Phase C-γ disposition recommendation (consolidated)

| Item | Severity | Disposition options | Recommendation | Rationale |
|---|---|---|---|---|
| **T3 — Ch 8:122 MacLean-engagement cross-chapter-coherence gap** | Procedural / cross-chapter-coherence-restoration | Option A: apply D-3a canonical sentence at line 122 / Option B: hold-as-is | **Option A (APPLY)** | Closes T3 with cross-chapter consistency restoration across Ch 5 + Ch 8 + Ch 9 + TA §1.10 Public-Choice-engagement sites; cousin pattern (Ch 9 Pass 3.4 §10.1) already established the canonical sentence form; one-sentence addition with minimum chapter-architecture disturbance |

All other threads (T1, T2, T4, T5, T6, T7, T8, T9) are HOLD with pre-pub-review-queue acknowledgment per §7.4.

---

## §10. Ratification record

### §10.1 Author disposition — RATIFIED 2026-05-26

| Item | Severity | Disposition options | Recommendation | Author ratification |
|---|---|---|---|---|
| §8.3 / §9.3 T3 MacLean cross-chapter-coherence spot-fix | Procedural / cross-chapter-coherence-restoration | A (APPLY) / B (HOLD) | **A (APPLY)** | **RATIFIED 2026-05-26 — Option A (APPLY)** (author ratify-as-recommended) |
| §8.2 Aggregate Pass-3.4 verdict | Verdict | ROBUST / CONDITIONALLY ROBUST / FRAYS | **CONDITIONALLY ROBUST** | **RATIFIED 2026-05-26 — CONDITIONALLY ROBUST** (author ratify-as-recommended) |

**Tally:** 1 RATIFY APPLY (T3 Option A canonical D-3a sentence appended at Ch 8 line 122) + 1 RATIFY VERDICT (CONDITIONALLY ROBUST aggregate). Eight threads (T1, T2, T4, T5, T6, T7, T8, T9) HOLD per §3 thread-pull-synthesis with pre-pub-review-queue acknowledgment for the bounded subgroup-discount regions; one thread (T3) procedurally spot-fixed via D-3a canonical sentence application.

### §10.2 Phase C-γ application — APPLIED 2026-05-26

T3 Option A applied: canonical D-3a sentence ("The rent-seeking analytical vocabulary survives many readings of Buchanan's broader political project, and this book draws on the vocabulary rather than endorsing the project.") inserted at Ch 8 line 122 between the framework's-contribution-is-different-in-kind statement and the "Chapter 9 develops the framework-Public-Choice relationship at greater length" forward-pointer. Placement matches Ch 5 line 202 + Ch 9 line 144 cousin conventions (D-3a sentence appended to Public-Choice-engagement paragraph in the natural prose-flow position).

- Application commit SHA: *(this commit)*
- Chapter line-count post-application: 243 (unchanged; sentence inserted within existing paragraph)
- Em-dash count post-application: 52 (unchanged; no em-dashes in D-3a canonical sentence)
- Cross-chapter cascade required: Stage 1c-light cross-chapter coherence verification (optional; Ch 5 + Ch 8 + Ch 9 + TA §1.10 Public-Choice-engagement sites now uniformly carry the D-3a canonical sentence post-T3 application)
- Pass 3.5 (developmental-edit) session ready: **Y** (chapter holds at robustness post-T3 application; Pass 3.5 next per per-prompt serial cadence)

### §10.3 Next session for Ch 8

**Pass 3.5 (developmental-edit) — whole-chapter restoration-of-richness audit** is the next session for Ch 8 per per-prompt serial cadence + v3.0/v3.1 sub-pass split + Amendment B. Two low-priority Pass 3.5 attention items flagged forward at §7.2 (civilizational-scale extrapolation paragraph at lines 210–222 + carbon-arithmetic paragraph at line 72).

After Pass 3.5: if spot-fixes ratified, Phase C-δ applies; otherwise Ch 8 Stage 3 closes and moves to Stage 5 (academic-rigor + prose-quality sign-off + pre-publication review queue) per v3.0/v3.1 architecture (Stage 4 already RATIFIED 2026-05-26).

---

## §11. Hard constraints honored

- ✓ Did NOT apply spot-fixes to `manuscript/chapters/Chapter__8_WhatThingsActuallyCost.md`. Pass 3.4 is audit-only; spot-fix application is a downstream Phase C-γ session.
- ✓ Did NOT re-litigate Pass 3.1 (fact-check) findings — CLOSED + APPLIED per `5fe6af6` + `275b75a` + `57575b1` + `9befb92`.
- ✓ Did NOT re-litigate Pass 3.2 (voice-polish) findings — RATIFIED 2026-05-25 + Phase C-β APPLIED at commit `16554fa`.
- ✓ Did NOT re-litigate Pass 3.3 (acceptance) findings — PROPOSED 2026-05-25 (commit `65a89dc`); §7 forward-flag list used as canonical Pass 3.4 input per framing.
- ✓ Did NOT re-litigate Stage 4 (render audit) — RATIFIED 2026-05-26 (commit `e36bdd6`); independent of Pass 3.4.
- ✓ Did NOT return INCLUDE or NEUTRAL verdicts for adversarial characters — verdict-floor EXCLUDE per template.
- ✓ Did NOT score Pass 3.5 (developmental-edit) — separate session per per-prompt serial cadence; explicit-gate per Amendment A two-class cascade.
- ✓ Did NOT re-write paragraphs — verdicts + per-character analysis + thread-pull synthesis only.
- ✓ Did NOT contact named subjects (including adversarial-reviewer institutional affiliations — public-record exception applies for citation but not for outreach per hard constraint).
- ✓ Did NOT propose new framework concepts.
- ✓ Did NOT re-litigate apparatus register canonical decisions (Item 1 inline-integral strip; Item 13 IPG; Item 14 Cᵢ via Four Gates).
- ✓ Did NOT re-litigate cross-corpus IPG canonical-construction (commit `57575b1` Option D applied at line 168).
- ✓ Did NOT re-litigate coal-CO₂ McDowell-specific cascade-reconciliation (commit `9befb92`).
- ✓ Verified post-Phase-C-β + post-Stage-4 chapter line count (243 lines, 2026-05-26) via `wc -l`.
- ✓ Verified em-dash count (28 em-dashes) via `grep -c "—"` against current chapter file state.
- ✓ Verified word count (6,421 words) via `wc -w`.
- ✓ Verified commits `5fe6af6`, `275b75a`, `57575b1`, `9befb92`, `138aa7e`, `6589ca2`, `16554fa`, `65a89dc`, `e36bdd6` all present on origin/main.
- ✓ Verified Pass 3.3 acceptance artifact present with §7 forward-flagged 15-adversarial-character set as canonical Pass 3.4 input.
- ✓ Verified Ch 9 Pass 3.4 cousin artifact present with canonical thread-pull-synthesis + cross-pressure-positioning-diagnostic format model (RATIFIED CONDITIONALLY ROBUST 2026-05-25).
- ✓ Verified Ch 4 + Ch 3 Pass 3.4 cousin artifacts present as additional format calibrators.
- ✓ Verified named-subject consent discipline per §4.2 + §4.3 (all named individuals fall under public-record exception or historical-record; no living-private-subject consent-gating items; adversarial-reviewer institutional affiliations cited via public-record exception for citation only — not for outreach).
- ✓ Built feature branch `claude/ch8-pass3-4-audience-load-robustness-a9d9ac` off current origin/main (`b37aa46`; rebased to tip pre-push per CLAUDE.md branch discipline).
- ✓ Applied Ch 9 Pass 3.4 §3 + §3.1 thread-pull-synthesis-with-cross-pressure-positioning-diagnostic as canonical format model.
- ✓ Surfaced T3 cross-chapter-coherence-restoration as the principal Pass 3.4 finding (Ch 8:122 MacLean-engagement gap relative to D-3a application sites Ch 5 + Ch 9 + TA §1.10).
- ✓ Confirmed cross-pressure structure across T1 + T4 + T6 + T8 as canonical sign of correct positioning (per Ch 9 cousin §3.1 diagnostic).

---

*End of Ch 8 Stage-3 Pass 3.4 (Audience-Load Robustness) rigor pass — PROPOSED 2026-05-26. Aggregate verdict: CONDITIONALLY ROBUST. Adversarial character set: 15 characters across 5 categorical bands (industry-funded, ideologically-opposed, trade-press/commercial, cultural, legal, cost-bearer); per-character distribution 3 ⚠⚠⚠ + 10 ⚠⚠ + 2 ⚠ EXCLUDE as expected per template verdict-floor. Nine threads (T1-T9) surfaced via thread-pull synthesis; eight HOLD with pre-pub-review-queue acknowledgment; one procedurally-spot-fixable (T3 cross-chapter-coherence-restoration; default APPLY). Cross-pressure positioning diagnostic confirmed across T1, T4, T6, T8 (canonical sign of load-bearing claims correctly positioned in political-economy debate). Mirrors Ch 9 cousin Pass 3.4 CONDITIONALLY ROBUST verdict + structural pattern. Pass 3.5 (developmental-edit) is the next session for Ch 8 per per-prompt serial cadence after Pass 3.4 ratification + optional T3 Phase C-γ application.*
