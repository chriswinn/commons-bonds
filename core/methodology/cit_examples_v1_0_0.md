# Commons Bonds — CIT Walkthrough Examples (Four Gates Applied to Cases)

**Version:** 1.0.0
**Date:** 2026-04-24
**Purpose:** Methodology illustration showing the Four Gates (Commons Inversion Test [CIT] + Units Consistency + Boundedness + Independence) applied to a varied set of framework cases. Each walkthrough demonstrates how candidate costs are admitted (or rejected) for inclusion in RCV. Captures findings from author-directed walkthroughs 2026-04-24 (Chris Winn).
**Status:** Working illustration document. Primary audience: framework readers seeking concrete operationalization of the methodology. Secondary audience: rigor-pass infrastructure validating that the gates do operationally distinct work.
**Cross-references:**
- Four Gates cluster rigor pass `tools/rigor-passes/commons_bonds_rigor_pass_2026-04-24_four_gates_cluster_v1.0.0.md`
- Commons-as-structural-identity rigor pass `tools/rigor-passes/commons_bonds_rigor_pass_2026-04-24_commons_as_structural_identity_v1.0.0.md`
- CIT rename rigor pass `tools/rigor-passes/commons_bonds_rigor_pass_2026-04-24_term_cit_rename_v1.0.0.md`
- Personal Stories Candidates Candidate #1 (commute-trade)
- `core/terms/terms_index.md` — CIT + Four Gates records.
- `core/case-studies/` — per-case research material these examples reference.

---

## §0. The Four Gates as a system

**CIT (Commons Inversion Test)** — content gate. Does the cost depend on a commons? Two sub-forms:
- **Commons-Absence Inversion:** imagine the commons not existing. Cost = replacement cost.
- **Commons-Consumption Inversion:** imagine the commons not being consumed. Cost = opportunity cost.

**Units Consistency** — mathematical-form gate. Is cost expressed in commensurable units (dollars × time-domain)?

**Boundedness** — mathematical-form gate. Does the cost integral converge?

**Independence** — mathematical-form gate. Is the cost not redundantly correlated with already-admitted Cᵢ (no double-counting)?

**Structural distinction:** CIT is a TEST (procedural methodology); the other three are CONDITIONS (static mathematical properties). Naming asymmetry honors the layer distinction.

---

## §1. McDowell County coal: Black Lung healthcare cost

**Candidate cost:** Black Lung healthcare expenditures + lost productivity + premature death — borne by miners, families, Medicare/Medicaid, McDowell County's social-service infrastructure.

**Gate 1 — CIT:**
Imagine the habitability commons of McDowell County absent. Picture extraction stripping the place of clean air, healthy bodies, intact community life-support. Does the cost become visible? Yes — Black Lung pathology is exactly what becomes visible when the habitability commons is eroded by the dust the regulators didn't enforce against, the medical supervision the company resisted, the community's transition reserve no one funded. **Commons-Absence Inversion.** PASSES.

**Gate 2 — Units Consistency:**
Healthcare costs in dollars; integrate over years of patient life + cohort effects + intergenerational life-expectancy gap. Dollars × time-domain. PASSES.

**Gate 3 — Boundedness:**
Each patient's healthcare cost over their lifetime is bounded. The cohort effect (13-year life-expectancy gap × population × earnings × healthcare costs) sums to a bounded total. Intergenerational health-effects extension (developmental + grandchildren mortality patterns) extends but doesn't blow up. PASSES.

**Gate 4 — Independence:**
Black Lung healthcare cost is mostly independent of the *ecosystem-remediation cost* (orange creeks, hillside scarring) and the *community-collapse cost* (population loss, school closures). Some correlation exists — community collapse worsens health outcomes — but at the level of Cᵢ admission, healthcare-cost-on-bodies and community-cost-on-population structure are distinct cost streams. PASSES with note: double-count audits at integration level needed.

**Verdict:** All four gates PASS. Black Lung health cost admits to RCV.

---

## §2. The commute trade (Personal Stories Candidate #1): foregone-life-time cost

**Candidate cost:** 1,800 hours/year of life-time consumed by 5-hour daily commute — costs incurred by you (foregone language-learning, exercise, family time, professional development, leisure, sleep). Information-asymmetric self-severance: past-you signed the lease without knowing what future-you would pay.

**Gate 1 — CIT:**
Imagine the time-commons UNCONSUMED — picture the 5 hours/day returned to you. Does the cost become visible? Yes — the language you didn't learn, the relationships not built, the rest not taken, the skills not acquired all become visible against the un-consumed-commons counterfactual. **Commons-Consumption Inversion.** PASSES.

**Gate 2 — Units Consistency:**
Time can be valued in dollars (hourly opportunity cost; revealed-preference for course tuition). 1,800 hours × revealed-preference rate = dollar value. Dollars × time-domain. PASSES.

**Gate 3 — Boundedness:**
1,800 hours × duration-of-lease (1 year). Bounded. PASSES.

**Gate 4 — Independence:**
Cost is independent of other extraction costs in the case (apartment manager's costs; landlord profits — separate Cᵢ). The case is special because value-capturer = cost-bearer (past-you = future-you), but the gates still operate cleanly. Information-asymmetric self-severance is admissible — the framework handles it. PASSES.

**Verdict:** All four gates PASS. Foregone-life-time cost admits to RCV.

**Methodology note:** This case demonstrates how CIT's Commons-Consumption sub-form admits opportunity-cost-on-time as a legitimate Cᵢ. Cases where extraction draws down a commons (rather than destroying it) require the Consumption sub-form; AIT's pre-CIT framing obscured this.

---

## §3. Norwegian oil extraction: future-generation climate damage

**Candidate cost:** Cumulative atmospheric carbon damage from a barrel of Norwegian oil, borne by future generations — sea-level rise; ecosystem disruption; agricultural loss; climate-disaster damages; biosphere-stability costs.

**Gate 1 — CIT:**
Imagine the atmospheric-stability commons absent for future generations. Does the cost become visible? Yes — climate damage is the canonical case of cost severed across generations. **Commons-Absence Inversion across the temporal gap.** PASSES.

**Gate 2 — Units Consistency:**
Climate damage in dollars; integrate forward across centuries with discount-rate convention. Dollars × time. PASSES.

**Gate 3 — Boundedness — this is where the gate actively works:**
A naive integration of climate damage forward across centuries with a low discount rate **doesn't converge** — Stern Review's argument turns on declining-or-zero discount rate which makes the integral effectively infinite over very long horizons. The gate would FAIL without an explicit convention.

**Framework's treatment:** apply Nordhaus DICE / Stern Review discount-rate convention. With a sensible discount rate (Stern's ~1.4%, or hyperbolic-declining per Weitzman), the integral converges to a bounded value. The framework's M9 risk register notes that the discount-rate choice is politically contested and dominates the SCC magnitude — the QUALITATIVE result (CS > 0) is robust across discount rates above zero, but the MAGNITUDE varies by an order of magnitude. **PASSES with explicit convention applied; magnitude depends on discount-rate choice; framework is honest about this.**

**Gate 4 — Independence:**
Climate cost is independent of, e.g., oil-well-decommissioning cost (different physical process), local-pollution cost from refineries (different time scale), labor-market disruption cost from energy transition. PASSES.

**Verdict:** All four gates PASS (with §3 boundedness condition explicitly stating discount-rate convention). Future-generation climate damage admits to RCV.

**Methodology note:** This case demonstrates Boundedness as a non-trivial gate that actively works on intergenerational/climate cases. The Norway sovereign wealth fund (per Open Insight #14) is the canonical real-world example of B (Accountability Bond) approaching RCV via commons-management instrument, even though the climate-cost integral has Boundedness-gate complexity.

---

## §4. 2008 financial crisis: institutional-commons damage with multi-stream Independence-gate exercise

**Candidate cost streams:**
- 10M home foreclosures (foreclosure cost)
- Retirement savings destroyed for cohort approaching retirement (retirement cost)
- Small-business failures from credit contraction (business cost)
- State-budget shortfalls + austerity-driven public-service cuts (institutional cost)
- Mortgage-system trust damage (institutional commons)
- Wealth-destruction concentrated on Black + Hispanic households (kindred + cohesion + institutional commons)
- Long-term wage stagnation for the labor cohort that lost employment in 2008-2010 (labor-time cost)

**Gate 1 — CIT:**
Imagine the institutional commons (financial-regulatory architecture; trust in market integrity; mortgage-system reliability; cohort-protective fiscal architecture) absent. Does the cost become visible? Yes. Each cost stream above maps to a different commons-grounding (institutional / kindred / cohesion / autonomy / temporal). **Commons-Absence across multiple commons categories simultaneously.** PASSES per cost stream.

**Gate 2 — Units Consistency:**
Each cost stream in dollars × time-domain. PASSES.

**Gate 3 — Boundedness:**
Each cost stream is bounded — crisis period (2007-2010) + recovery period (2010-2020) + lingering effects (2020-present). Finite range. PASSES.

**Gate 4 — Independence — THIS is where the 2008 case earns its complexity:**

Cost streams are *correlated* through the crisis itself. The same household may have:
- Lost their home (foreclosure cost)
- Lost their retirement savings (retirement cost)
- Lost their job (labor-time cost)
- Watched institutional trust collapse (institutional commons)

Admitting all four as separate Cᵢ would *double-count* — the household experiences a single integrated extraction event; counting each stream as fully independent overstates total severance.

**The Independence gate forces careful decomposition.** Tech Appendix §L formal specification requires: when admitting multiple Cᵢ from the same case, demonstrate linear independence. For 2008, this means: admit the cost streams at the level where they don't overlap (e.g., foreclosure cost = housing wealth lost, NOT counting retirement-savings-loss separately if those losses are correlated through the same household-balance-sheet collapse).

**Operationally:** either admit the costs at higher-level categories (household-wealth-destruction as one Cᵢ) and forgo the granularity, OR admit them granularly with explicit correlation-correction (subtract the overlap mathematically).

**PASSES with non-trivial Independence-gate work required.**

**Methodology note:** This case demonstrates the Independence gate as the framework's double-counting prevention apparatus. Without it, RCV computations on multi-stream cases would systematically inflate. With it, the framework can be defended at peer-review depth on cost decomposition.

---

## §5. The asteroid miner (Ch 7 Mars habitat / Europa thought-experiment): multi-commons absent simultaneously

**Setting:** Hypothetical extraction operation in space — asteroid mining, Mars habitat resource extraction, or hypothetical Europa-ice mining. Used in Ch 7 as the framework's universality test ("if it works on Mars, it works on Earth").

**Candidate cost streams:**
- Life-support infrastructure cost (oxygen, food, water production replacement)
- Communication-delay cost (relativistic + physical-distance limits on Earth-contact)
- Return-trip cost (spatial commons consumed; one-way journey foreclosed)
- Psychological-isolation cost (autonomy + kindred commons consumed)
- Medical / specialist-care cost (epistemic commons absent at distance)
- Habitat-ecosystem cost (no Earth biosphere; closed-loop replacement)

**Gate 1 — CIT:**
Imagine Earth's habitability commons absent — the atmosphere, ecosystem, social network, medical infrastructure, mobility, cohesion-of-Earth-community. Does the cost become visible? Yes — at extreme. Multiple commons absent simultaneously: habitability + ecosystem + spatial + kindred + epistemic + autonomy + cohesion. **Commons-Absence Inversion at maximum.** PASSES — and powerfully, because the case foregrounds what we don't notice on Earth (we don't price oxygen because the atmospheric commons is so abundant).

**Gate 2 — Units Consistency:**
Hypothetical pricing applied (cost-per-pound-to-orbit; replacement-cost of Earth ecosystems; etc.). Dollars × time-domain. PASSES with hypothetical inputs.

**Gate 3 — Boundedness:**
Bounded over the colony lifetime + return-mission window + post-colony recovery period (if any). Finite. PASSES.

**Gate 4 — Independence:**
Multiple commons producing multiple Cᵢ — life-support (replaces atmospheric + ecosystem commons); communication-delay (epistemic + kindred commons); return-trip (spatial); psychological (autonomy + kindred). Some correlation (psychological cost worsens with longer communication delay), but at first order distinct cost streams. PASSES with care.

**Verdict:** All four gates PASS. The asteroid-miner case admits multiple Cᵢ across multiple commons categories.

**Methodology note (universality test function):** The asteroid case's pedagogical work is to show CIT operating where Earth readers most viscerally feel the commons-absence (oxygen in space; water on Mars; community in isolation). It doesn't introduce new mechanism — it foregrounds what Earth's commons-abundance hides. **The universality claim becomes legible:** if the framework works in space (where every commons is priced because it must be replaced), it works on Earth (where commons-abundance lets extractors externalize what they would have paid for if the commons weren't free). Strong M5 dinner-table case.

---

## §6. Healthcare end-of-life (Butler pacemaker case): Commons-Consumption applied to medical-commons

**Setting:** Katy Butler's reporting on her father's pacemaker — a procedure that extended his cognitive decline 5+ years, while Medicare reimbursement architecture systematically routed physicians toward procedures over conversations ($461 procedural payment vs. $54 end-of-life conversation payment historically). Butler's mother caregiver-burnout (~80 hr/week). 25× growth in medical GoFundMe campaigns 2011-2020. 88% medical-GoFundMe failure rate. Racial disparity in crowdfunding success (Ly & Soman 2020).

**Candidate cost streams:**
- Patient's prolonged-cognitive-decline cost (autonomy + kindred + dignity loss)
- Family caregiver labor-time cost (Butler's mother's 80 hr/week × years)
- Family-financial-resource depletion cost
- Lost end-of-life-quality cost (kindred + cohesion + autonomy commons)
- Medicare/Medicaid system-distortion cost (institutional commons)
- Foregone-conversation cost (epistemic commons — informed consent about end-of-life options)

**Gate 1 — CIT:**
Imagine the medical-commons of dying-with-dignity-with-family-present UNCONSUMED — picture the medical architecture not drawing down patient autonomy, family time, dignified end-of-life process. Does the cost become visible? Yes — the procedural-medical-financial architecture extracts these by incentivizing prolongation over comfort, billable procedure over conversation. **Commons-Consumption Inversion** (the medical commons exists in society but is being drawn down by the extraction architecture). PASSES.

This is a distinctive case — it demonstrates Commons-Consumption Inversion in a non-time-commons context. The medical commons (informed end-of-life choices + family presence + dignified process) was *available in principle* but actively *consumed by extraction*. Different from McDowell (Commons-Absence — habitability destroyed); different from Norway oil (Commons-Absence — atmospheric stability damaged). Here, the commons existed and was drawn down, not destroyed.

**Gate 2 — Units Consistency:**
Healthcare costs in dollars × time. Caregiver-time can be valued (replacement-cost of professional care). Family-financial-depletion already in dollars. PASSES.

**Gate 3 — Boundedness:**
Bounded over patient lifetime (with prolongation) + family caregiving period + financial-resource depletion period. PASSES.

**Gate 4 — Independence:**
Multi-stream — patient's suffering, family caregiver's labor-time, financial resources, system distortion. Some correlation (financial depletion correlates with caregiving-time), but distinct cost streams at first order. PASSES with care.

**Verdict:** All four gates PASS. End-of-life cost admits to RCV.

**Methodology note:** This case demonstrates Commons-Consumption Inversion outside the time/attention-economy domain. The medical-commons of dying-with-dignity is consumed by the procedural-reimbursement architecture, not destroyed. The framework's CIT operates on this mode cleanly. Also a key adoption case for medical professionals + healthcare policy reformers (the framework's vocabulary travels into medical-ethics discourse).

---

## §7. Opioid Appalachia (Sackler / Purdue Pharma): documented extraction with multi-commons damage + both CIT sub-forms simultaneously

**Setting:** Per Patrick Radden Keefe's *Empire of Pain* (2021) + public litigation record. Purdue Pharma deliberately targeted vulnerable communities (including McDowell County) with OxyContin, suppressing internal evidence of addiction risk. Sackler family extracted ~$11B before bankruptcy filing. Big Three distributors (McKesson, Cardinal Health, AmerisourceBergen) settled for $21B in 2022. 141 overdose deaths per 100K in McDowell County. Communities still in crisis.

**Candidate cost streams:**
- Patient deaths + addictive-harm cost (autonomy + epistemic + kindred commons)
- Family destruction cost (kindred + cohesion commons)
- Community-collapse cost (cohesion + institutional commons)
- Healthcare-system overload cost (institutional commons)
- Multi-generational trauma cost (intergenerational + temporal commons)
- Foster-care-system overload cost (institutional + kindred commons)
- Lost-life-trajectory cost (autonomy + temporal commons consumed by addiction)

**Gate 1 — CIT — both sub-forms simultaneously:**

**Commons-Absence sub-form:** Imagine the epistemic commons (truthful information about OxyContin's addictive risk) absent — that is what was suppressed. Imagine community-cohesion commons absent — that is what 141/100K overdose deaths produces. Imagine kindred commons of intact families absent — that is what addiction-driven family destruction produces. **Multiple commons in Absence Inversion.**

**Commons-Consumption sub-form:** Imagine individual life-time UNCONSUMED by addiction — picture the 1990s-2010s cohort of working-age adults in extraction-targeted Appalachia counties not having their lifetime drawn down by pharmaceutical-engineered addiction. Lost-life-trajectory cost becomes visible. **Commons-Consumption Inversion at individual scale operating simultaneously with Commons-Absence at community scale.**

**This case is the framework's clearest example of both sub-forms operating simultaneously** — the pharmaceutical extraction destroyed community-level commons (Absence) while consuming individual-level life-time commons (Consumption). PASSES at full strength.

**Gate 2 — Units Consistency:**
Statistical-life-value × excess deaths; addiction-treatment costs; foster-care system costs; healthcare-system overload costs. All in dollars × time-domain. PASSES.

**Gate 3 — Boundedness:**
Bounded over the crisis period (1996-present) + community-recovery period (extending; potentially decades). Finite. PASSES.

**Gate 4 — Independence:**
Multi-stream — patient deaths, family destruction, community collapse, healthcare overload, foster-care overload, multi-generational trauma. Significant correlation (community collapse causes family destruction; addiction-deaths cause foster-care overload). The Independence gate forces careful decomposition. The framework can use higher-level admission (community-extraction-cost as one Cᵢ) OR granular admission with explicit correlation-correction. Both operationally valid. PASSES with non-trivial Independence-gate work required.

**Verdict:** All four gates PASS. Opioid-extraction-Appalachia cost streams admit to RCV.

**Methodology note (empirical validation of framework):** This case is the framework's strongest empirical validation. The diagnostic the framework makes (extraction operating across multiple commons, severing cost from value extraction) was **already empirically validated by the public litigation record** before the framework was built. Sackler $11B extraction = framework's predicted value extraction; $21B settlement = framework's predicted partial Accountability Bond (B); the $11B + $21B is still vastly less than RCV (deaths × statistical-life-value + community-recovery costs + multi-generational trauma). The framework's prediction matches what the courts found. Strong M2 + M6 + M11 case.

**Cross-reference:** This case is the framework's most-direct refutation of Vance's *Hillbilly Elegy* cultural-pathology framing. The framework demonstrates, via public litigation record, that the "cultural pathology" Vance describes was in significant part a deliberately manufactured pharmaceutical market. Per bibliography §12.

---

## §8. Cross-cutting findings across all 7 walkthroughs

### What each gate does in operational practice

**CIT** does the heaviest lifting consistently. Every case requires identifying the commons + applying the right sub-form. The framework's substantive content gate. Universal application.

**Units Consistency** is mostly boilerplate in well-formed cases. Catches edge cases like trying to admit a probability or dimensionless ratio as if it were a cost — would FAIL there. In practice, well-formed candidate costs already pass.

**Boundedness** sleeps on most cases but **wakes up dramatically on climate / intergenerational cases** where the integral can diverge without explicit discount-rate convention. The Norway oil case (§3) is paradigmatic. This is where the gate earns its keep.

**Independence** sleeps on simple single-stream cases but **wakes up on multi-stream correlated cases** — 2008 financial crisis (§4); McDowell County (§1) where health, community, ecosystem, and institutional costs flow from the same extraction; opioid Appalachia (§7) with multiple cost streams correlating through community-collapse dynamics. Prevents double-counting that would inflate RCV illegitimately.

### CIT sub-form distribution across cases

| Case | CIT sub-form |
|---|---|
| McDowell coal | Absence (habitability destroyed) |
| Commute trade | Consumption (time drawn down) |
| Norwegian oil / climate | Absence (atmospheric stability damaged for future) |
| 2008 crisis | Absence (institutional commons damaged) |
| Asteroid miner | Absence (multiple Earth commons absent) |
| Healthcare end-of-life | Consumption (medical commons drawn down) |
| Opioid Appalachia | **Both** (community Absence + individual Consumption) |

**Pattern:** physical-resource-extraction cases tend toward Absence; personal-scale + medical / time / attention cases tend toward Consumption; multi-commons-multi-stream cases (opioid; large-scale crisis) can exercise both sub-forms simultaneously.

### Cost-stream complexity scales with case scope

- Single-cost-stream cases (commute trade): trivial Independence; gates flow easily.
- Multi-cost-stream cases (McDowell; healthcare): non-trivial Independence; some correlation; manageable.
- Highly-multi-stream cases (2008 crisis; opioid Appalachia; asteroid miner): Independence is decisive; framework's careful decomposition discipline is what makes RCV defensible.

### Empirical validation cases

The opioid Appalachia case (§7) is the framework's strongest empirical-validation case — public litigation record predates framework construction; framework's predictions match court findings. The 2008 crisis case (§4) has comparable public-record validation through Financial Crisis Inquiry Commission.

These cases serve M2 (case study) + M6 (academic) + M11 (critic) modules together — the framework didn't predict from theory then check; the predictions and the public record converge on the same diagnosis from independent starting points.

### Gates as a complete admission apparatus

- CIT determines what's IN.
- Units Consistency keeps the math well-formed.
- Boundedness keeps the integral finite.
- Independence keeps the integral honest.

Together they're a complete system. CIT is the framework's intellectual contribution; the other three are the mathematical hygiene any well-formed cost-integrand needs. Naming asymmetry (test vs. condition-properties) honors the division of intellectual labor.

---

## §9. Maintenance + extension

**Adding new cases:** when a new case is researched + admitted to the framework's case library, the case-study file should include a §"Four Gates walkthrough" passage applying the four gates to the case's primary cost streams. This file aggregates those passages across cases for methodology-reader convenience.

**Updating walkthroughs:** if framework methodology updates (e.g., RCV integrand restructured; new sub-form surfaces), update the walkthroughs to reflect the change. Version-bump this file.

**Cross-references stay current:** when rigor passes update terminology (e.g., AIT → CIT 2026-04-24), this file's vocabulary updates to match.

---

*End of CIT walkthrough examples v1.0.0. Established 2026-04-24. 7 cases captured; methodology-illustration document for framework readers + rigor infrastructure validation.*
