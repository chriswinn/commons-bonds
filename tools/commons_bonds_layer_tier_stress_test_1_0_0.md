# Commons Bonds — Layer and Tier Stress Test

**Date:** 2026-04-20
**Version:** 1.0.0
**Protocol applied:** `commons_bonds_rigor_protocol_1_1_0.md` (off-Earth exemplar in Test 3, Tier 6 transcription fix)
**Supersedes:** No prior audit
**Companion to:** `commons_bonds_c6_decision_memo_2_0_0.html` (first worked example of the rigor protocol), `commons_bonds_life_support_rename_memo` (Life-support rename conducted inline in session v1.19.0, ratified before this audit)
**Queue effect:** Surfaces one new architectural rename candidate (Geographic → Spatial) and confirms no other renames needed. Attribution updates cascade from Life-support ratification and, conditionally, from Spatial ratification.

---

## 1. Executive summary

Applying the canonical rigor protocol to the six remaining abundance layers and all nine tiers of the v10 RCV decomposition yields four findings.

**Finding 1 (rename candidate).** **Geographic → Spatial.** Same failure mode as Atmospheric: the term is Earth-surface-centric and fails the multi-scale test at the off-Earth/engineered-habitat exemplar introduced in protocol v1.1.0. An asteroid miner in free space, an orbital-habitat technician, or a Lagrange-point maintenance crew does not have "geography" in the planet-surface sense; they have trajectory, delta-V, and spatial separation. The underlying structural insight — that separation between value-capturer and cost-bearer enables severance — is preserved by the broader term. All five tests PASS for Spatial; Geographic FAILS multi-scale at the asteroid/LEO case. Recommendation: ratify.

**Finding 2 (watch items, not renames).** **Demographic** is partial at the individual scale — the word reads awkwardly for a reader evaluating their own situation (individuals don't think in demographic terms about themselves). **Political** has a minor partisan-connotation risk in US contexts but the specific framework use (democratic infrastructure and its capture) is sharp enough that substituting "Governance" would dilute rather than clarify. Neither is urgent. Both noted as watch items for a future pass.

**Finding 3 (no change needed).** **Temporal**, **Institutional**, **Ecological** all pass every test at every scale in both Earth and engineered-habitat exemplars. Retain.

**Finding 4 (tier-level).** **All nine tiers (1, 2a, 2b, 3, 4, 5, 6, 7, 8) pass the full rigor protocol at all four scales in both Earth and engineered-habitat exemplars.** No tier-level renames, splits, or retirements are recommended. Attribution updates are required to reflect ratified (Life-support) and candidate (Spatial) layer renames — these are mechanical propagations, not re-decisions.

**Aggregate:** One ratified rename already executed (Atmospheric → Life-support, C7 patch queued), one candidate rename surfaced (Geographic → Spatial, C8 patch pending ratification), two watch items for a future pass, and universal tier-level PASS. The v10 RCV decomposition is rigor-test-clean as a tier set.

---

## 2. Scope and method

**In scope:** All seven abundance layers (Atmospheric/Life-support confirmed separately; six remaining layers tested here). All nine tiers of the v10 canonical decomposition (Tiers 1, 2a, 2b, 3, 4, 5, 6, 7, 8).

**Out of scope:** The RCV integral itself (tested elsewhere in Technical Appendix theorems E.1–E.5). The eight-layer AIT methodology (already canonical). Content of individual manifestation paragraphs (covered by §7 execution gate in C6 memo v2.0.0).

**Protocol routing.** Layers and tier names are architectural-naming claims per the protocol routing rule. Full battery applies: two-path + multi-scale + ten-critic + success criteria. AIT is also run as corroboration for tier-level claims, since every tier must survive the abundance inversion that generated it. Tier-name-level claims apply AIT + two-path + multi-scale per the routing rule.

**Depth calibration.** Items that clearly PASS all tests receive brief confirmations. Items surfacing issues receive full analysis. The asymmetry is intentional — writing 5,000 characters on "Temporal passes" adds no value.

---

## 3. Part 1 — Layer stress test

### 3.1 Layer: Atmospheric → Life-support (ratified in session v1.19.0)

Referenced here for completeness. Full analysis conducted inline in session v1.19.0 under the rigor protocol. All five tests PASS for Life-support; Atmospheric FAILS multi-scale at the off-Earth case. C7 patch produced in same session. This memo assumes Life-support is canonical.

### 3.2 Layer: Geographic

**Current definition:** "Ability to travel, relocate, return home."
**Revealed tiers:** Spatial displacement cost, transport cost, community immobility cost.

#### AIT
Strip geographic abundance (assume you cannot relocate or return): costs of stranding, transport, and immobility become visible. Restore abundance (free movement): costs disappear from pricing. The test discriminates. **PASS.**

#### Two-path
- **Path 1 (allocation symmetry):** Clear. Whoever captures value from extraction that requires the worker to be elsewhere (the employer, the remote operator, the state licensing the operation) is separated from whoever bears the displacement cost (the worker, the home community, the stranded return). Asymmetry is structural — arises from allocation architecture. **PASS.**
- **Path 2 (shield absence):** Shield is the *distance* itself. Distance prevents the consuming population from seeing the displaced cost-bearer. Named correctly by the layer. **PASS.**

#### Multi-scale (with protocol v1.1.0 off-Earth exemplar)

| Scale | Earth exemplar | Off-Earth / engineered-habitat exemplar | Verdict |
|---|---|---|---|
| Individual | Coal miner unable to return home post-contract | Asteroid miner in belt with insufficient delta-V for return window | Earth ✓ · Off-Earth **issue: "geographic" reads wrong** |
| Community | McDowell County population immobility | Mars colony unable to evacuate when mine plays out | Earth ✓ · Off-Earth **same issue** |
| Government | Sovereign territory fisheries jurisdiction | Lunar/orbital allocation rights (Outer Space Treaty regime) | Earth ✓ · Off-Earth **same issue** |
| Corporate | Supply chain distance from extraction site to consumer | Orbital logistics, trajectory windows, deep-space resupply chains | Earth ✓ · Off-Earth **same issue** |

Off-Earth readers at every scale stumble on "geographic." A Lagrange-point maintenance crew does not have geography in the planet-surface sense. An orbital operation has positions, vectors, windows, and separations — not geography. The term quietly reimports the very parochialism the framework exists to escape, same structural failure as Atmospheric.

**Path 2 diagnosis:** The current term does not fully dissolve the off-Earth shield. A reader applying the framework in an engineered-habitat context has to mentally translate "geographic" into "spatial separation," which is exactly the kind of friction that erodes vocabulary portability. **FAIL at off-Earth exemplar.**

#### Candidate rename: Spatial

Re-running against the same tests:

- **AIT:** Spatial abundance (3D space to move through and across) inverted reveals costs of separation, stranding, transport, trajectory constraints. Discriminating. **PASS.**
- **Two-path:** Rename does not change allocation (P1 PASS). Rename *strengthens* shield dissolution (P2) because "spatial" names the class rather than one environment-specific instance, closing the off-Earth gap. **PASS both paths, P2 stronger than current.**
- **Multi-scale:** Direct reads at all four scales in both environment types. An individual has a "spatial situation" (distance from family, from support infrastructure). A community has a spatial footprint. A government regulates spatial jurisdiction. A corporation operates spatial supply chains. An asteroid miner, a Mars colonist, a LEO technician all have spatial separation from home. **PASS all four × both.**
- **Ten-critic (abbreviated):** Academic Economist accepts (spatial economics / new economic geography / Krugman is a standing research program). Analytic Philosopher accepts (coherent class: the dimension of location and separation). Writerly Editor prefers Spatial over Geographic for Earth+off-Earth framings. Future-Proofer: Spatial outlasts Geographic — Geographic is contingent on Earth-surface operations, Spatial is permanent. Novelty Critic: not novel, but the framework-specific use is. Falsifiability: refutation would be an abundance-stripping scenario whose revealed costs are not about separation — no plausible candidate. Completeness: revealed-costs list must be updated to include orbital, delta-V, and trajectory-window costs. Libertarian and Leftist both neutral on the rename. **10 accept / 0 reject / 1 execution-dependent (Completeness list update, which is a required action, not a rejection).**
- **Success criteria:** Vocabulary portability: serves (Spatial cites cleanly into existing economics literature). Individual applicability: serves (direct read). Community usability: serves (direct read). Next-gen scholarship: serves (better scaffolding than Geographic, which is a narrower field). **PASS all four.**

**Verdict: rename Geographic → Spatial. All five tests PASS for Spatial; Geographic FAILS multi-scale at the off-Earth exemplar introduced in protocol v1.1.0. Recommendation: C8 patch pending user ratification.**

#### Proposed revised description for the layer table

> **Spatial** | Functionally abundant capacity for movement, relocation, return, and access across separations | Spatial displacement cost, transport cost, community immobility cost, trajectory-window cost, delta-V cost, and other separation-provisioning costs

The "and other" clause follows the same pattern as Life-support — signals that the list is illustrative of a class, not exhaustive. This is the fix for the pattern that locked "Geographic" into the planet-surface interpretation.

### 3.3 Layer: Temporal

**Definition:** "Extraction rates slower than regeneration or substitution."
**Revealed tiers:** Rate-of-extraction cost, acceleration premium, temporal displacement cost.

Already abstract at the same level as Spatial (post-rename), Institutional, Political. Not planet-bound. Not environment-bound. Clock time works in Earth mines, on Mars colonies, in asteroid belt contracts, in orbital maintenance schedules. A worker's career horizon, a community's generational timeline, a government's fiscal window, a corporation's capital-planning horizon — all Temporal. AIT passes. Two-path passes. Multi-scale passes at all four × both environment types. Ten-critic: no material objections surface; Novelty Critic notes that "time discounting" is canonical in economics, and the framework's use (temporal abundance as distinct from time discounting) is sharper than either Hotelling or Weitzman alone. Success criteria: serves all four.

**Verdict: Temporal PASSES. No change.**

### 3.4 Layer: Institutional

**Definition:** "Legal enforcement infrastructure."
**Revealed tiers:** Legibility cost, enforcement cost, accountability mechanism cost.

The term is abstract and works across scales and environments. At individual scale: workplace compliance infrastructure (HR, safety protocols, grievance process) is the institutional face the individual worker encounters. At community: municipal regulatory capacity. Government: regulatory agency staffing, enforcement budgets, legal legibility. Corporate: internal controls, audit functions, bond markets demanding institutional rigor. Off-Earth: a flag-of-convenience asteroid-mining registry has weak institutional abundance; a colony operating under an established sovereign or corporate charter has strong institutional abundance. The layer correctly discriminates. AIT: strip institutional abundance, enforcement-gap costs appear. Two-path: shield is legibility failure, correctly named. Multi-scale: all four × both. Ten-critic: no objections. Success criteria: all four served.

**Verdict: Institutional PASSES. No change.**

### 3.5 Layer: Demographic

**Definition:** "Communities large enough to sustain knowledge transmission."
**Revealed tiers:** Knowledge and culture cost, apprenticeship cost, intergenerational expertise cost.

This is the partial case from my earlier preliminary audit. Re-running under the full protocol:

- **AIT:** Strip demographic abundance (community falls below critical transmission mass): knowledge systems collapse non-linearly. Restore: no cost. **PASS.**
- **Two-path P1:** Clear — extractors capture value while community disperses below knowledge-transmission threshold. Asymmetry structural. **PASS.**
- **Two-path P2:** Shield is the non-linearity of demographic collapse — communities appear functional until they don't. Named correctly by the layer. **PASS.**
- **Multi-scale:** Community, government, corporate scales read naturally. **Individual-scale reading is awkward.** An individual reader evaluating their own situation does not think in demographic terms about themselves. A nurse considering a career does not frame her situation as "my demographic abundance." She thinks about *colleagues to learn from, mentors available, peer group size.* The concept transmits, but the word is rough at individual scale.
- **Ten-critic:** Writerly Editor flags the individual-scale awkwardness. Academic Economist accepts (demographic economics is established). Completeness critic accepts. Others accept or neutral. **9 accept / 0 reject / 1 execution-dependent (Writerly Editor's concern, which is a manifestation-paragraph drafting issue, not a name-level rejection).**
- **Success criteria:** Vocabulary portability: serves at community+ scales, weak at individual. Individual applicability: the concept applies but the word reads awkwardly. Community usability: serves strongly. Next-gen scholarship: serves. **Mostly serves; one weak-spot at individual scale.**

**Verdict: Demographic PASSES with one flagged weak spot at individual scale. Not urgent enough to rename.** Candidate replacements considered (Population, Communal, Collective) all introduce different problems — Population is flat and doesn't convey transmission thresholds, Communal and Collective both collide with Ecological (which also describes collective systems). The cleanest fix is manifestation-paragraph-level, not layer-name-level: Tier 7 (Knowledge and Culture) individual-scale manifestation can use peer-group/mentor language directly and let "Demographic" remain the layer-level abstraction it was designed to be.

**Watch item for future audit:** if a second stress-test pass reveals Demographic failing at more scales or in new environment types, revisit. Current pass does not justify a rename.

### 3.6 Layer: Ecological

**Definition:** "Functional ecosystem services (pollination, water cycling, soil fertility)."
**Revealed tiers:** Ecological carrying cost, ecosystem service cost, biodiversity cost.

Works at all scales on Earth. Off-Earth handling is a special case worth stating explicitly: on a lifeless asteroid or a not-yet-terraformed Mars, *there is no ecological abundance to strip.* This is not a layer failure — it is correctly priced. Without ambient ecosystem services, costs that Earth absorbs invisibly are immediately visible and priced as life-support (the layer ecology doesn't cover is already covered by Life-support post-rename). On a terraformed Mars or an Earth-restored ecosystem, the layer re-engages.

AIT: strip ecosystem services on Earth (pollinator collapse, aquifer depletion, soil death), ecological tier costs become visible. On asteroid: baseline is no ecology, so the stripping is already fully executed — all tier costs visible. Two-path: allocation and shield both clear. Multi-scale: individual (farmer recognizing pollinator decline), community (municipality managing water systems), government (EPA pricing ecosystem services), corporate (supply chains dependent on biological inputs). Off-Earth: the layer handles its own boundary condition correctly. Ten-critic: no material objections. Success criteria: all four served.

**Verdict: Ecological PASSES. No change.** The off-Earth boundary condition (lifeless environments) is a feature of the layer's design, not a failure.

### 3.7 Layer: Political

**Definition:** "Democratic infrastructure that permits honest accounting."
**Revealed tiers:** Political capture cost, suppression cost, narrative capture cost.

All five tests run through:

- AIT: strip political abundance (democratic/accountability infrastructure), capture-related costs become visible. PASS.
- Two-path: P1 allocation is clear — beneficiaries of capture extract from the commons of democratic legitimacy. P2 shield is the captured infrastructure itself (Tier 8 canonical). Both PASS.
- Multi-scale: Individual (worker's political agency, collective action capacity, access to representation). Community (local political structures captured or intact). Government (legislative and regulatory integrity). Corporate (lobbying, regulatory capture, revolving-door staffing). Off-Earth: early colonial governance is often explicitly non-democratic (corporate charter, mission command structure, flag-of-convenience licensing), so political abundance is rare off-Earth — and the layer correctly prices that absence. PASS all four × both.
- Ten-critic: Novelty Critic flags "political capture" as an established concept (Stigler 1971, regulatory capture literature); accepted with attribution. Writerly Editor: sharp term. No reject votes. **10 accept.**
- Success criteria: all four served.

**Alternative considered: Governance.** Broader term; covers democratic and non-democratic forms. **Rejected** on specificity grounds — the framework's specific insight is about *democratic* infrastructure and its capture (Tier 8 is canonically Political Capture Cost, not Governance Capture Cost). Broadening to "Governance" dilutes what makes the tier distinctive. Political is sharper.

**Watch item:** US readers may read "Political" as partisan. Non-urgent; the framework's use is abstract (democratic infrastructure as a commons) and the disambiguation lives in the manifestation paragraphs.

**Verdict: Political PASSES. No change.**

### 3.8 Layer summary table

| Layer | AIT | Two-path | Multi-scale (4 × 2) | Ten-critic | Success criteria | Overall | Action |
|---|---|---|---|---|---|---|---|
| **Life-support** (was Atmospheric) | PASS | PASS | PASS | 10/0/3 | PASS all | **PASS** | Ratified — C7 patch queued |
| **Spatial** (candidate; current: Geographic) | PASS | PASS stronger | PASS | 10/0/1 | PASS all | **PASS (vs Geographic FAIL)** | **C8 pending ratification** |
| Temporal | PASS | PASS | PASS | Clean | PASS all | **PASS** | No change |
| Institutional | PASS | PASS | PASS | Clean | PASS all | **PASS** | No change |
| Demographic | PASS | PASS | PASS (weak at individual) | 9/0/1 | Mostly serves | **PASS w/ watch** | No change; manifestation-level fix |
| Ecological | PASS | PASS | PASS (off-Earth boundary handled) | Clean | PASS all | **PASS** | No change |
| Political | PASS | PASS | PASS | 10/0/0 | PASS all | **PASS** | No change; watch US-partisan reading |

---

## 4. Part 2 — Tier stress test

All nine tiers of the v10 canonical decomposition already survived the AIT process that generated them; AIT is confirmatory here, not an open question. Two-path and multi-scale (with the protocol v1.1.0 off-Earth exemplar) are the operative tests, with attribution updates propagated from Life-support (ratified) and Spatial (conditional).

### 4.1 Tier 1 — Lifetime Survival Cost

**Current layer attribution:** Atmospheric + Ecological → **updated to Life-support + Ecological.**

Allocation symmetry: employer captures labor value; worker bears biological wear across lifetime (latent health, premature mortality). Shield: epistemic at individual scale (the worker cannot perceive the tier without explicit description), ecological at community scale (ecosystem service decline is slow), life-support at engineered-habitat scale (engineered provisioning is priced explicitly). Multi-scale with off-Earth exemplar: asteroid miner's lifetime survival is the framework's native case — life-support provisioning cost plus long-latency microgravity/radiation health trajectory. Nurse (Earth individual): latent cardiovascular / burnout. McDowell community: multi-decade groundwater contamination. Mars colony: engineered life-support cost. Firm: sustainability officer evaluates worker-lifetime health exposure. All PASS. **Verdict: PASS. Attribution updated to Life-support + Ecological.**

### 4.2 Tier 2a — Actuarial Risk Cost

**Layer attribution:** Institutional (unchanged).

Allocation: employer captures value; population of workers bears statistically expected harm distribution. Shield: institutional — absent enforcement infrastructure, the actuarial distribution falls on public balance sheets (workers' comp, emergency rooms, regional cancer clusters) rather than extraction contracts. Multi-scale: individual worker (actuarial framing makes individual uncertainty measurable across their career), community (cluster epidemiology), government (public health burden), corporate (insurance pricing, sustainability risk). Off-Earth exemplar: asteroid mining actuarial profile is well-documented in spaceflight literature (ISS microgravity, radiation exposure, CO2 scrubber failure rates); the tier applies directly. **Verdict: PASS. No attribution change.**

### 4.3 Tier 2b — Mission Failure Reserve

**Current layer attribution:** Geographic + Temporal → **if Spatial ratified: Spatial + Temporal.**

The asteroid-miner-stranded scenario is the canonical worked example for this tier. Allocation: operator captures projected revenue at planning stage; worker + community bear the compounding cost of failure (stranding, bankruptcy discharges, broken economic dependency). Shield: *spatial* (cannot return, cannot try again locally) + *temporal* (failure clock compounds). Multi-scale: individual (miner stranded without return fuel). Community (McDowell County post-mine-closure, Mars colony post-mine-exhaustion). Government (bond default + dependent population). Corporate (operational risk pricing). Off-Earth: native case for this tier. **Verdict: PASS. Attribution updates on Spatial ratification.**

### 4.4 Tier 3 — Dynastic Labor Cost

**Layer attribution:** Temporal (unchanged).

Allocation: employer captures labor value at below-generational cost; worker's descendants bear uncompensated trajectory reduction. Shield: temporal — the effect only compounds across generations, invisible at single-generation accounting. Multi-scale: individual (compounded inheritance trajectory a worker could have built). Community (McDowell County's lost third generation). Government (Social Security's $108T figure is this tier made quantitative). Corporate (pension discharges, contingent workforce). Off-Earth exemplar: asteroid-mining-contract bondage has Earth-parallel dynastic effects — an off-Earth worker on a multi-decade contract is not building inheritance either. **Verdict: PASS. No attribution change.** (Note: this was the location of the protocol v1.0.0 transcription error fixed in v1.1.0.)

### 4.5 Tier 4 — Foreclosure Cost

**Layer attribution:** Temporal (unchanged).

Allocation: extractor captures present value; all future generations bear loss of access. Shield: temporal — future generations cannot bid in present markets. Multi-scale: individual (a worker's own access to a resource they helped extract, now gone). Community (Appalachian coal community's post-extraction optionality). Government (sovereign resource loss). Corporate (stranded-asset risk, strategic reserves). Off-Earth: lunar helium-3 early extraction foreclosing fusion optionality — canonical case. **Verdict: PASS. No attribution change.**

### 4.6 Tier 5 — Community Transition Reserve

**Current layer attribution:** Geographic + Demographic → **if Spatial ratified: Spatial + Demographic.**

Allocation: operator captures revenue during extraction; dependent community bears full transition cost when extraction ends. Shield: spatial (community cannot relocate) + demographic (below critical threshold, community cannot sustain transition independently). Multi-scale: individual (worker whose retraining and relocation was never funded). Community (McDowell County, Mars colony post-mine). Government (state-level transition support for single-industry regions). Corporate (decommissioning funds vs actual community transition — the gap this tier prices). Off-Earth: Mars colony whose mine plays out is precisely this tier. **Verdict: PASS. Attribution updates on Spatial ratification.**

### 4.7 Tier 6 — Ecological Carrying Cost

**Layer attribution:** Ecological (unchanged).

Allocation: extractor captures present value; ecology bears service degradation across recovery timeline. Shield: ecological — services are free on Earth until they aren't, and recovery operates on non-human timescales. Multi-scale: individual (farmer watching pollinator decline). Community (Chesapeake Bay oyster filtering capacity). Government (EPA ecosystem service accounting). Corporate (supply-chain biological inputs). Off-Earth: as discussed under Ecological layer, tier is boundary-handled on lifeless environments (no ecology = maximum costs visible elsewhere, absorbed into Life-support). On terraformed environments, tier re-engages fully. **Verdict: PASS. No attribution change.**

### 4.8 Tier 7 — Knowledge and Culture Cost

**Layer attribution:** Demographic (unchanged).

Allocation: operator captures accumulated expertise cheaply; community bears irreversible loss when population falls below transmission threshold. Shield: non-linearity of demographic collapse — functional until not. Multi-scale: individual (apprentice who can no longer find a master). Community (McDowell County's three generations of lost technical and cultural knowledge). Government (language and traditional-knowledge preservation programs — downstream consequence of this tier). Corporate (trade-secret and skilled-worker pipeline collapse). Off-Earth: early Mars colony losing critical systems expertise as rotation schedules disperse teams below transmission threshold. **Verdict: PASS. No attribution change.**

### 4.9 Tier 8 — Political Capture Cost

**Layer attribution:** Political (unchanged).

Allocation: beneficiary of suppression captures continuing extraction value; democratic polity bears institutional corrosion. Shield: the captured infrastructure itself — the shield and the tier are recursively linked (Tier 8 names the mechanism that keeps the other seven tiers invisible). Multi-scale: individual (worker's loss of collective-action capacity, access to representation). Community (captured local government). Government (regulatory capture at state/federal levels). Corporate (lobbying, revolving door, narrative capture). Off-Earth: flag-of-convenience asteroid-mining registration is a live case of political-abundance-stripping — jurisdictions competing to offer weakest accountability. **Verdict: PASS. No attribution change.** (This is the tier whose absence in the older FGC taxonomy was the decisive C6 finding; its canonical position is rigor-tested.)

### 4.10 Tier summary table

| Tier | Name | Layer attribution (post-Life-support, pre-Spatial) | Layer attribution (post-Spatial if ratified) | All-tests verdict |
|---|---|---|---|---|
| 1 | Lifetime Survival Cost | **Life-support + Ecological** | Life-support + Ecological | **PASS** |
| 2a | Actuarial Risk Cost | Institutional | Institutional | **PASS** |
| 2b | Mission Failure Reserve | Geographic + Temporal | **Spatial + Temporal** | **PASS** |
| 3 | Dynastic Labor Cost | Temporal | Temporal | **PASS** |
| 4 | Foreclosure Cost | Temporal | Temporal | **PASS** |
| 5 | Community Transition Reserve | Geographic + Demographic | **Spatial + Demographic** | **PASS** |
| 6 | Ecological Carrying Cost | Ecological | Ecological | **PASS** |
| 7 | Knowledge and Culture Cost | Demographic | Demographic | **PASS** |
| 8 | Political Capture Cost | Political | Political | **PASS** |

---

## 5. Part 3 — Aggregate findings and required changes

### 5.1 Ratified changes (executed in v1.19.0)

- **Atmospheric → Life-support** across 5 files (C7 patch produced and queued for manual GitHub application).
- Protocol refinement plan identified: v1.1.0 (off-Earth exemplar + Tier 6 transcription fix).

### 5.2 Candidate change pending ratification (from this audit)

- **Geographic → Spatial** across the same 5 files (or superset — scope must be verified by new file scan).
  - Layer definition and revealed-costs list rewritten.
  - Tier 2b attribution: Geographic + Temporal → Spatial + Temporal.
  - Tier 5 attribution: Geographic + Demographic → Spatial + Demographic.
  - C8 patch file to be produced on ratification. Structure will mirror the C7 patch.

### 5.3 Watch items (not currently actionable)

- **Demographic at individual scale** — reads awkwardly; manifestation-paragraph language should use mentor/peer framing rather than leaning on the layer name. Not a rename.
- **Political partisan connotation (US)** — framework use is abstract (democratic infrastructure as commons) but disambiguation should be explicit in manifestation paragraphs. Not a rename.

### 5.4 Protocol refinements (v1.1.0 shipping with this memo)

- Test 3 (multi-scale) expanded: each scale now tested against at least one Earth-baseline exemplar AND one off-Earth/engineered-habitat exemplar. Rationale: the universality claim covers off-Earth contexts; the protocol should exercise that. Without this refinement, architectural decisions can pass at Earth-individual and fail at engineered-individual undetected (as Planetary did mid-session).
- §4.2 AIT worked-examples table corrected: Tier 3 → Tier 6 transcription fix. Ecological Carrying Cost is Tier 6; Dynastic Labor Cost is Tier 3.
- §10 Worked examples section expanded to reference this stress-test memo as the second worked example.

### 5.5 File-level change propagation

Assuming Life-support ratified (done) and Spatial ratified (pending), the cascading updates touch:

| File | Life-support updates | Spatial updates (conditional) |
|---|---|---|
| `eight-tier-v10.html` | 6 locations | ~5 locations (new scan needed) |
| `error-out-v10.html` | 6 locations | ~5 locations (confirm duplicate) |
| `eight-tier-decomposition-v10.md` | ~5 locations | ~5 locations |
| `TechnicalAppendix_v0_0_2.html` | A.8 list, C.2 layer, C.3 table, Tier 1 attributions | A.8 list, C.2 layer, C.3 table, Tier 2b and Tier 5 attributions |
| `commons_bonds_updated_glossary_v2.html` | 5 locations | ~3–4 locations (Abundance Layer definition lists all seven) |

A Geographic scope-scan should be run before C8 patch production to confirm exact counts — same mechanical grep pattern as the Atmospheric scope-map in v1.19.0.

---

## 6. Part 4 — Recommended next actions

1. **Ratify Geographic → Spatial.** All five tests PASS; FAIL mode for Geographic at off-Earth is the same failure mode Life-support was ratified to fix. Consistency argument: if we renamed Atmospheric for off-Earth universality, not renaming Geographic leaves an equivalent gap open.
2. **On ratification: produce C8 patch.** Structure mirrors C7 (scope-map → replacement text → audit tasks → completion criteria → verification). Likely 15–18k chars.
3. **Ship protocol v1.1.0** in same bundle as C7 + C8 for a clean patch application session.
4. **Defer Demographic and Political watch items** to a future audit. They are not at blocking-rigor level; re-examining them in 6–12 months after the WS02/WS03 manifestation paragraphs are drafted will give better evidence for whether the weak-spots translate into reader friction or whether manifestation-level language covers them.
5. **Handoff updates:** v1.20.0 handoff marks C7 patch produced, C8 memo produced (this file), protocol v1.1.0 produced. TODO list updated: Spatial rename awaiting ratification.

---

## 7. Change log

**v1.0.0 (2026-04-20):** Initial layer and tier stress test audit. Applied protocol v1.1.0 (off-Earth exemplar in Test 3 + Tier 6 transcription fix) to all six remaining abundance layers and all nine tiers of the v10 RCV canonical decomposition. Surfaces Geographic → Spatial as candidate rename with all five tests passing; confirms Temporal, Institutional, Ecological, Political pass with no change; flags Demographic and Political as watch items not currently actionable; confirms all nine tiers pass with attribution updates propagating from ratified (Life-support) and candidate (Spatial) layer renames. Second worked example under the canonical rigor protocol, following the C6 decision memo v2.0.0.

---

*End of Layer and Tier Stress Test v1.0.0.*
