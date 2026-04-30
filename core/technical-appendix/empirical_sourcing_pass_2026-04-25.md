# Empirical sourcing pass — DAC + space-economics numerical anchors

**Date:** 2026-04-25
**Purpose:** Closes the M6.4 sourcing-pass-needed flags from the 2026-04-24 academic-rigor full test (rigor pass `commons_bonds_rigor_pass_2026-04-24_academic_rigor_full_test_v1.0.0.md`, commit `ae90800`). Produces sourced numerical anchors for two locations where the framework's Method 1 (Replacement Cost) and Ch 7 thought-experiment work depend on empirical figures: **direct-air-capture (DAC) cost per ton CO₂** (Tech Appendix supplement §3.1 worked-example) and **space-economics numerical anchors** (Ch 7 calibration data).

**Status:** Sourcing record. Does NOT modify any chapter or supplement directly. Phase B authoring integration into the relevant docs is a separate work item; this document gives the integrator the citation-ready figures to draw on.

**Reading-discipline note:** All figures below are best-public-estimates as of late-2025 / early-2026 industry reporting. Where ranges are given, the range reflects (a) different deployment scales (pilot / first-of-a-kind / nth-of-a-kind), (b) different sources, or (c) different cost-component scopes (capture-only vs capture-plus-sequestration vs lifecycle). Phase B integration should refresh primary sources to publication-of-Book-1 vintage and prefer the most recent primary-source citation available at integration time.

---

## §1. Direct-air-capture (DAC) cost per ton CO₂ — Tech Appendix supplement §3.1 anchor

The supplement §3.1 (Method 1 Replacement Cost) uses DAC cost-per-ton as the worked-example anchor for the Habitability commons (atmospheric ecosystem). The Method 1 logic: the floor on Habitability-commons Residual Commons Value is the engineering cost to replace the substitutable component of the commons (the CO₂-removal function the atmosphere provides at zero marginal cost via natural sinks).

### §1.1 Operational DAC facilities (2024-2025 cost figures)

| Facility | Operator | Operational since | Capture capacity | Cost per ton CO₂ (current) | Cost per ton CO₂ (target at scale) | Source |
|---|---|---|---|---|---|---|
| **Orca** (Iceland) | Climeworks | 2021 | ~4,000 tons/year | ~$600–$1,000/ton | n/a (pilot) | Climeworks public reporting; IEA *Direct Air Capture 2022* |
| **Mammoth** (Iceland) | Climeworks | 2024 | ~36,000 tons/year (target full scale) | ~$600–$1,000/ton initial; targeting ~$300–$400/ton at full operation | $300–$400/ton | Climeworks public reporting (2024 commissioning); MIT Technology Review coverage |
| **Stratos** (Texas, US) | Carbon Engineering / 1PointFive (Occidental) | construction; targeting 2025 commissioning | ~500,000 tons/year (target) | n/a (pre-operational) | $94–$232/ton (Carbon Engineering 2018 *Joule* paper basis); ~$300–$600/ton more conservative third-party estimates | Keith et al., "A Process for Capturing CO2 from the Atmosphere," *Joule* (2018); 1PointFive announcements |

**Provisional consolidated range for Habitability-commons Method 1 anchor:**

- **Conservative (current operational, first-of-a-kind):** $600–$1,000/ton CO₂.
- **Mid-range (declared targets at-scale, next 5–10 years):** $300–$600/ton CO₂.
- **Optimistic (industry-target nth-of-a-kind by 2050):** $100–$300/ton CO₂.

The framework's Method 1 anchor should report all three ranges with explicit time-horizon attribution, not a single point estimate.

### §1.2 Authoritative review-literature ranges

| Source | DAC cost range | Time horizon | Notes |
|---|---|---|---|
| **IEA, *Direct Air Capture: A Key Technology for Net Zero*** (2022) | $125–$335/ton CO₂ for early commercial-scale; $100/ton achievable by 2030 in optimistic scenarios | 2025–2030 commercial-scale; 2030+ optimistic | IEA's reference framing. https://www.iea.org/reports/direct-air-capture-2022 |
| **IEA, *Net Zero by 2050*** (2021) | $130–$330/ton CO₂ | 2030 commercial-scale | Net-Zero scenario assumption. |
| **IPCC AR6 Working Group III** (2022), Chapter 12 | $100–$300/ton CO₂ in optimistic deployment scenarios; >$1,000/ton in pessimistic | 2030–2050 | https://www.ipcc.ch/report/ar6/wg3/ |
| **National Academies (US), *Negative Emissions Technologies and Reliable Sequestration*** (2019) | $100–$600/ton CO₂ over a wide deployment-scenario sensitivity | 2030–2050 | Pre-Stratos; figures may underrepresent recent learning curves. |
| **Realmonte et al., *Nature Communications*** (2019) | $100–$600/ton CO₂ at multi-gigaton scale | 2050 | Modeled at-scale figure. |
| **House et al., *PNAS*** (2011) | $1,000+/ton CO₂ early estimate | 2010s pessimistic | Early-literature pessimistic floor; useful for steelman engagement on M6.4. |

### §1.3 Recommended Method 1 anchor specification (for Tech Appendix supplement §3.1 + Ch 6 main-text integration)

**Recommended language (Phase B integration):**

> The Habitability-commons Method 1 anchor is the engineering cost to remove and sequester one ton of CO₂ via direct-air-capture (DAC). Operational DAC facilities (Climeworks Orca and Mammoth in Iceland, 2021 and 2024) currently report capture costs in the range of $600–$1,000 per ton CO₂. Targets for at-scale commercial deployment over the next decade are in the $300–$600/ton range (Climeworks Mammoth full-operation target; Carbon Engineering / 1PointFive Stratos pre-operational projection). Authoritative review literature (IEA *Direct Air Capture 2022*; IPCC AR6 Working Group III, 2022; US National Academies 2019) places the achievable cost by 2050 in the $100–$300/ton range under optimistic deployment scenarios. The Method 1 anchor accordingly reports a three-horizon range: $600–$1,000/ton (current operational), $300–$600/ton (at-scale commercial within the next decade), $100–$300/ton (optimistic 2050 nth-of-a-kind). The atmospheric-commons CS arithmetic uses the appropriate-horizon figure for the comparison being made; the McDowell-coal carbon term (Ch 6 convergence table) uses the IPCC-aligned $190/ton SCC for a reason distinct from DAC replacement-cost: SCC prices the damage caused, DAC prices the engineering reversal of that damage, and the two should not be conflated.

**Distinction discipline:**

- **Social Cost of Carbon (SCC):** prices the damage that one ton of CO₂ emission causes (current US EPA central estimate: $190/ton CO₂ at 2% discount rate; Rennert et al. 2022 *Nature*).
- **DAC cost-per-ton:** prices the engineering cost to remove one ton already emitted.
- **Method 1 (Replacement Cost) Habitability anchor:** uses DAC, NOT SCC. The Method 1 logic is "what would it cost to engineer a substitute for the commons function" — the substitute function for the atmospheric CO₂-removal capacity is DAC. SCC is the damage-side number; Method 1 is the substitution-side number. They appear together in the convergence-table presentation but answer different questions.

---

## §2. Space-economics numerical anchors — Ch 7 (asteroid miner) calibration

Ch 7 uses thought-experiment-style scenarios (Mars colony water; asteroid iron; lunar helium; comet volatiles; Europa ice; exoplanet hypotheticals) to demonstrate that CIT operates across parameter ranges. The chapter is intentionally light on numerical anchoring — the demonstration is that CIT produces different verdicts at different parameter values, not that any specific numerical estimate holds. M6.4 nonetheless flags that selected numerical anchors would strengthen academic-credibility positioning, particularly for the asteroid-iron extrapolation where the "RCV approaches market price" claim depends on substitutability and externality being approximately zero.

### §2.1 Launch-cost anchors (Earth-to-LEO and Earth-to-GTO)

| Vehicle | Operator | Cost per kg to LEO (current, 2024–2025 estimates) | Notes |
|---|---|---|---|
| **Falcon 9** | SpaceX | ~$2,700/kg (LEO; full-stack rate based on $67M/22.8t) | Operational since 2010; reusable booster. |
| **Falcon Heavy** | SpaceX | ~$1,400/kg (LEO; $90M/63.8t LEO capacity) | Operational since 2018. |
| **Starship (early-operational target)** | SpaceX | ~$200–$1,000/kg (LEO; targeted; not yet validated) | Pre-operational as of 2024–2025; figures are SpaceX-stated targets, not third-party-validated. |
| **Vulcan Centaur** | ULA | ~$5,000–$8,000/kg (LEO) | Operational 2024. |
| **New Glenn** | Blue Origin | ~$2,000–$6,000/kg (LEO; targeted) | First flight 2025; cost figures are pre-operational. |

**Source:** FAA/AST commercial-space launch reports; Aerospace Corporation Center for Space Policy and Strategy briefings; SpaceX public statements; *Space News* coverage.

**Order-of-magnitude framing:** Earth-launch infrastructure has reduced cost-per-kg by approximately one order of magnitude (from ~$30,000/kg Space Shuttle era to ~$2,000–$5,000/kg current commercial-launch baseline) over 2010–2025; a further order-of-magnitude reduction to $200–$500/kg is plausible-but-not-validated for the next decade dependent on Starship operational maturity.

### §2.2 Asteroid sample-return mission costs (per gram returned)

| Mission | Operator | Sample mass returned | Mission cost (USD, mission-vintage) | Cost per gram returned | Notes |
|---|---|---|---|---|---|
| **OSIRIS-REx → Bennu** | NASA | 121.6 g (final accounting; 2023 capsule return) | ~$1.16B (lifecycle; 2016 launch through 2023 return) | ~$9.5M/g | Single-mission, single-asteroid; primarily science-mission, not optimized for cost-per-gram. |
| **Hayabusa2 → Ryugu** | JAXA | 5.4 g (2020 capsule return) | ~$300M (lifecycle, 2014 launch through 2020 return) | ~$56M/g | Smaller mission profile; technology-demonstration-and-science. |
| **Hayabusa → Itokawa** | JAXA | 1500 microscopic particles, ~mg total (2010 return) | ~$170M (lifecycle) | n/a (sample-mass too small for meaningful $/g framing) | First-generation; mission profile not optimized for sample mass. |

**Source:** NASA OSIRIS-REx mission lifecycle accounting; JAXA Hayabusa/Hayabusa2 mission accounting; *Nature Astronomy* and *Science* coverage of sample-return missions.

**Framing for Ch 7 calibration:** science-mission sample-return at ~$9.5M/g (Bennu) is approximately **5–7 orders of magnitude** above the per-gram cost framework that asteroid-mining commercial proposals operate in (which assume per-gram costs in the $1–$100 range at scale, contingent on (a) full-mass extraction not single-sample-return; (b) substantial Starship-class or post-Starship launch-cost reduction; (c) in-situ resource utilization eliminating the return-to-Earth requirement for many use-cases). The 5–7 order-of-magnitude gap is the framework's relevant calibration point: Ch 7's "RCV approaches market price for asteroid iron" claim depends on cost-per-kg dropping by ~6 orders of magnitude relative to current science-mission economics, AND on substitutability remaining high (which is the core CIT claim, not a launch-cost-dependent claim).

### §2.3 Asteroid-mining commercial-proposal cost estimates (for context)

| Source | Asteroid-mining cost per ton extracted material (target / projection) | Notes |
|---|---|---|
| **Keck Institute Asteroid Retrieval Mission Study** (2012) | ~$2.6B for retrieval of a 7-ton asteroid to lunar orbit (~$370,000/kg retrieved) | Pre-Starship; mission profile assumes existing launch infrastructure. |
| **Planetary Resources commercial estimates** (2013–2018, pre-acquisition) | $50–$500/kg at scale (water; iron); not validated by operational missions | Company-stated targets; broadly skeptical reception in space-economics literature. |
| **Deep Space Industries commercial estimates** (2013–2018, pre-acquisition) | Comparable order of magnitude to Planetary Resources estimates | Same caveat. |

**Source:** Keck Institute for Space Studies, *Asteroid Retrieval Mission Study* (2012); industry-presentation materials from Planetary Resources and Deep Space Industries; *Space Resources Roundtable* proceedings.

**Caveat for Ch 7:** commercial asteroid-mining cost projections are actor-stated targets, not validated operational figures. The 5–7 order-of-magnitude reduction implicit in commercial projections has not been demonstrated by any operational mission. The framework's Ch 7 thought-experiment use of "asteroid iron is approximately market-priced under any reasonable accountability bond" is robust to wide variance in this projection because the structural argument is about substitutability and externality (both ~0 for asteroid iron), not about specific cost-per-kg numbers.

### §2.4 Mars surface-operations cost reference (for thought-experiment grounding)

The Mars-colony water-extraction thought-experiment in Ch 7 does not depend on specific per-kg cost numbers, but the chapter's plausibility benefits from a one-paragraph reference that current operational Mars surface costs (Curiosity, Perseverance, Ingenuity, Mars Exploration Rovers) run in the order of $1B+ per mission for ~1-ton-class delivered surface mass. This anchors the thought-experiment's "small colony" framing in plausible-not-fantasy economics — the colony exists at the boundary of what operational Mars-surface presence has achieved, not at orders of magnitude beyond it.

| Mission | Operator | Delivered Mars surface mass | Mission cost (USD, mission-vintage) | Cost per kg surface-delivered |
|---|---|---|---|---|
| **Curiosity (Mars Science Laboratory)** | NASA | 899 kg rover (2012 landing) | ~$2.5B lifecycle | ~$2.8M/kg surface-delivered |
| **Perseverance (Mars 2020)** | NASA | 1,025 kg rover (2021 landing) | ~$2.7B lifecycle | ~$2.6M/kg surface-delivered |
| **InSight** | NASA | 358 kg lander (2018 landing) | ~$830M lifecycle | ~$2.3M/kg surface-delivered |

**Source:** NASA mission lifecycle accounting; *Planetary Society* mission cost analyses.

**Order-of-magnitude framing:** current Mars surface-presence economics are ~$2–3M per kg delivered, dominated by interplanetary-cruise + entry-descent-landing infrastructure rather than per-kg launch from Earth. A small colony (~10 person-class, ~10–100 ton delivered surface mass) under current operational economics would carry order-of-magnitude $30B–$300B delivery cost, before any consideration of in-situ resource utilization, Starship-class delivery cost reduction, or the speculative-but-plausible-decade-scale developments Ch 7's thought-experiment assumes.

---

## §3. Phase B integration recommendations

1. **Tech Appendix supplement §3.1:** integrate the §1.3 recommended Method 1 anchor specification (three-horizon DAC range) into the §3.1 worked-example. Replace the current "direct-air-capture cost per ton CO₂ at engineering scale" placeholder with the sourced range. Add the SCC-vs-DAC distinction discipline (§1.3 closing paragraph) as a methodological footnote.
2. **Ch 6 main-text:** the McDowell-coal convergence table currently uses $190/ton SCC for the carbon term. The Method 1 Habitability anchor should appear in Ch 6's convergence-table walkthrough as a distinct number from SCC, with the §1.3 distinction discipline made explicit. (This connects to Phase B methodology-defense-consolidation work — the Method 1 anchor is part of the Method 1 / Method 2 / Method 3 triangulation defense.)
3. **Ch 7 main-text:** add a one-paragraph numerical-anchoring footnote citing §2.1 launch-costs + §2.2 sample-return + §2.4 Mars-surface to ground the thought-experiment in plausible-economics. Avoid commitment to specific commercial-projection cost-per-ton numbers (§2.3) since those are unvalidated; cite them as actor-stated projections only.
4. **Ch 6 + Ch 7 IPG-reconciliation work** (per chapter audit §2.6): when Ch 6 IPG-reconciliation lands during Phase B (33-122× canonical → table reconciliation), the Method 1 anchor's three-horizon framing helps explain why some IPG reports are wider-range than others — the range reflects time-horizon attribution, not framework imprecision.

---

## §4. Cross-references

- `core/technical-appendix/archive/TechnicalAppendix_v0.0.5_supplement.md` §3.1 — the Method 1 anchor location these figures populate.
- `core/case-studies/commons_bonds_case_study_audit_v1.0.6.md` — IPG reconciliation flag for Ch 6 convergence table.
- `manuscript/chapters/Chapter__7_TheColonyAdministrator__Draft.md` — Ch 7 asteroid-iron / Mars-colony thought-experiment (lines 79, 163, etc.) — locations where §2 numerical-anchor footnotes would integrate.
- `tools/rigor-passes/commons_bonds_rigor_pass_2026-04-24_academic_rigor_full_test_v1.0.0.md` §M6.4 — the sourcing-pass-needed flag this document closes.
- Open Insight #14 (Norway-as-canonical-existing-B2-exemplar epistemic-humility) — adjacent: when sourcing claims are made, the same epistemic-humility discipline applies to the cost-per-ton anchors (these are best-public-estimates, not framework-canonical truths).

---

*End of empirical sourcing pass 2026-04-25. Phase B authoring integration of §1.3 + §3 recommendations is the next-step work item.*
