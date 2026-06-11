<!-- STATUS: PROPOSED v2 | 2026-06-10 | supersedes ch6-blind-brief_2026-06-06.md | session: claude/pm-book-completion-260610-07b75f -->

# Chapter 6 — "Three Ways of Counting" — Structural Drafting Brief v2 (BLIND)

**Date:** 2026-06-10
**For:** a whole-cloth drafting agent who has NOT read and will NOT read the current Chapter 6.
**Supersedes:** `research/story-drafts/ch6-blind-brief_2026-06-06.md` in full (including its 2026-06-09 M3 override banner, which is folded into the body here).
**Verified against:** `manuscript/technical-appendix/TechnicalAppendix_v2.0.0.html` (the TA is canonical; all method figures below were re-extracted from the TA on 2026-06-10), `manuscript/ledgers/_CANONICAL_FIGURE_LEDGER.md` (RATIFIED 2026-06-04 + 2026-06-09 amendments), and `manuscript/chapters/_BookLevelGuidance.md`.

This brief is self-contained. Draft the entire chapter from this brief alone, plus the two named register-model files in §5. Do NOT seek out the existing Chapter 6; nothing here is lifted from it. Every beat is abstracted to its function and obligation, not its wording. Invent your own sentences for everything.

**The one-paragraph version of what changed since v1:** the chapter's method spine has been rebuilt. M2 (Revealed Preference) is NOT a third independent estimator of RCV; the convergence claim inside the RCV apparatus is M1 ∩ M3 only, and M2 reads the realized Bond, revealing (a) a lower bound on RCV and (b) WHO PAID. The bare IPG multiples (33-122x, ~50x, 555x, 50-555x) are retired in favor of lens-explicit IPGs. M3 is now the Arrow-Fisher/Henry quasi-option value (the Dixit-Pindyck $420-13,100 framing is gone). The Norway backtest mechanism is irreversibility-reduction, not rent-capture. Four naming digressions compress to one sentence + TA pointer each. Em-dash count goes from 193 to 0.

---

## 1. RATIFIED FACT GROUND + FIGURE TABLE (updated to canon 2026-06-10)

Single source of truth for every number the chapter touches. **Label-pinning is load-bearing: state which quantity each number is, every time.** Where this table and any other artifact disagree, this table (which follows the TA's current text) wins; discrepancies vs. the figure ledger are flagged in §6 — do not resolve them yourself.

### 1.1 McDowell coal / magnitude

| Figure | Canonical value (pinned label) |
|---|---|
| 1960 mine-mouth coal price | **$4.71/ton** (EIA Total Energy Table 7.9, bituminous; all-coal $4.83). Prose may say "just under five dollars"; use $4.71 wherever a point value appears. Never $4.50. Contemporary mine-mouth band ~$40-140/ton by region/grade (EIA/USGS). |
| CO2 emission factor (two bases, carry BOTH with rationale) | National-bituminous default **2.32 t CO2/short ton**; McDowell-specific Pocahontas-seam **2.61 t/short ton** ( = EPA AP-42 §1.1 93.28 kg CO2/mmBtu × Pocahontas heat content ~28 mmBtu/short ton; cite the heat-content source, USGS/EIA Pocahontas data, explicitly so 2.61 cannot be mistaken for an anthracite assumption). Ch6 introduces the 2.32 national figure at framework-introduction register so the downstream 2.61-vs-2.32 calibration footnote is not stranded. |
| Social cost of carbon | **$190/t CO2 = the EPA 2023 central estimate** (EPA *Report on the Social Cost of Greenhouse Gases*, drawing on Rennert et al. 2022 *Nature*, whose own central figure was ~$185). **Never attribute $190 to Rennert alone.** |
| Carbon term, national basis | **$441** ( = 2.32 × $190 ). Label: carbon term on the national-bituminous basis. |
| Carbon term, McDowell basis | **$496** ( = 2.61 × $190 ). **$496 = the carbon term / foreclosure component ONLY. $496 is NEVER the total.** |
| 8-component honest TOTAL | **$510/ton**. **$510 = the TOTAL, never the carbon term.** ($496 and $510 are opposite meanings; always state which.) |
| 4-component Pigouvian floor | **~$504-518/ton** ( $496 carbon + ~$8-22 non-carbon heads ). Replaces any "$518-532" or "$449-464"-as-McDowell figure. |
| Bottom-up non-carbon tiers | Health **$2-4/ton**; environment **$1-3/ton**; community **$5-15/ton**; non-carbon subtotal **$8-22/ton**. |
| Bottom-up national-basis total | carbon $441 + non-carbon $8-22 ≈ **$449-463/ton**, labeled as the national-bituminous-basis arithmetic (not a McDowell figure). |
| McDowell 2020 population | **~19,000 / "under 20,000"** (retire "18,000"). Decline from ~100,000. |
| McDowell life expectancy | male **63.5 vs 76.5** national (13-year gap); IHME / Dwyer-Lindgren et al., *JAMA Intern Med* 2017; cite as the ~2013 estimate, not "current." |
| US Steel McDowell exit | phrase as **"across the 1980s" / "by the late 1980s"** — NEVER a point-year (1986 vs 1990 unlocked; ledger J5). |
| Black lung cumulative paid | **"~$44 billion through 2009 (GAO/CRS)" — always dated**; no authoritative post-2009 cumulative exists (program reports annual disbursements thereafter; a conservative floor for 1969-present). |
| Black Lung Trust Fund DEBT | **$5.1B as of September 2024** (DOL/GAO). DISTINCT from cumulative-paid; never blur the two. |
| Reclamation-bond shortfall | **$3.7-6 billion** across Appalachia (Ch2 owns the derivation; reference). |

### 1.2 IPG — lens-explicit ONLY (bare multiples RETIRED)

Every IPG the chapter quotes MUST name (a) the lens and (b) the price basis. **Retired and never to be quoted: bare "33-122x", "~50x triangulated central", "555x", "50-555x".** The McDowell lenses, per the TA's current text:

| Lens | Value | Basis |
|---|---|---|
| Carbon-externality / Damage-Function | **~107-110x** | ÷ the $4.71 1960 mine-mouth price |
| Real-options (Approach 2 model, TA §9.5) | **45-89x** | TA three-model table |
| RCV-integral (Weitzman) | **61-115x** | $525-540/ton across the contemporary ~$8.66 and 1960 $4.71 price bases; calibration documented at TA §11.1 |
| Method-3 foreclosure-premium | **8.5-26x, center ~15x** | price-independent (scarcity × irreversibility premium itself); the most conservative lens |

⚠ **Ledger-vs-TA discrepancy (do NOT resolve; see §6):** the figure ledger's RCV-integral entry reads 67-134x; the TA's current text (4 occurrences, including the §9.5 table and §11.6) reads **61-115x**. Drafts follow the TA: **61-115x**.

Other-case IPGs (TA §9.5 / §11.2 / §11.3, all damage-function lens unless noted): **Deepwater ~15-16x** (BP all-in ~$61.6B ÷ ~$4B revenue; real-options 12-21x; RCV ~17-18x); **Libby ≈65-100x** (VSL-vintage sensitivity 65-77x on 2006$ → 78-102x updated; real-options 57-93x; RCV 72-111x); **Exxon Valdez ~1,200-1,900x** (bottom-up enumeration vs product value of the spilled oil — state that base qualifier; Valdez is public-record-sourced, not in the TA). Baotou: not computable on documented inputs (TA §11.4); do not invent a Baotou IPG.

### 1.3 Inner-method figures (the recast convergence table; TA §3.6 worked-example block + §11.5/§11.6)

Column architecture (load-bearing — this IS the spine recast): **M1 and M3 are the two RCV estimators; RCV = the M1 ∩ M3 convergence; M2 is the realized-Bond READING (who paid), not an estimator.**

| Case | Market price | M1 — Replacement Cost (RCV estimator) | M3 — Option Value (RCV estimator) | RCV (M1 ∩ M3 convergence) | M2 — realized-Bond reading (who paid) | Implied CS |
|---|---|---|---|---|---|---|
| McDowell coal | $4.71/ton (1960 mine-mouth, bituminous) | **$290-2,702/ton** across DAC horizons; at-scale center ~$1,235 (TA §11.6; horizon bands: $290-875 optimistic-2050 / $812-1,658 at-scale / $1,595-2,702 conservative) | **$340-3,670/ton; geometric center ~$1,115** (TA §11.6) | **~$1,000-1,500/ton center; overlap ~$340-2,700** | **$50-88/ton societally-paid (incl. Black Lung); $8-15/ton industry-paid** (~$5-8B reclamation bonds + private medical settlements) | **~$1,025-1,065/ton**; CS dwarfs realized B by ~12-20x; CS > 0 |
| Norway petroleum | ~$80/BOE central crude value (~$40-120/BOE across price regimes; Brent/EIA) | **$161-422/BOE** (TA §11.5) | **$96-610/BOE; central ~$281** (TA §11.5) | **~$281/BOE center** (bands overlap) | **$48/BOE (GPFG = realized forward Bond B₂)** | **~$233/BOE; ~$12.8T cumulative**; CS > 0 |
| Deepwater Horizon | ~$4B Macondo revenue (framework derivation: ≈50M bbl × ~$80/BOE 2010 crude; $3.2-4.8B band; label as derived, NOT a sourced figure) | ~$22B engineering + ecological restoration (BP response ~$14B + NRDA $8.8B per 2016 Consent Decree) | backward-only† | n/a (one-event; see †) | **~$20-25B actually paid** (CWA $5.5B + DOJ criminal $4.5B + class-action economic ~$10-15B) | CS > 0 |
| Libby, Montana | ~$100M lifetime revenue (industry estimate; no primary source confirms it — carry the qualifier) | ~$0.6B EPA Superfund committed + mortality-inclusive long-tail ≈$5.1-7.6B (694 documented deaths through 2011, Naik et al. 2017, × EPA VSL $7.4-11.0M; a floor — mortality ongoing) | backward-only† | n/a† | **~$0.3B W.R. Grace settlements actually paid** ($250M 2008 EPA + $18.5M 2023 NRDA + $5.1M 2008 DEQ) | CS > 0 |
| Exxon Valdez | $5.5M product spilled (product value of the spilled crude, NOT extraction-lifetime revenue — state the qualifier) | ~$2.3B cleanup + ecological restoration (Exxon $2.2B + NRDA ~$100M per 1991 settlement) | backward-only† | n/a† | **~$1.9B actually paid** (1991 civil $900M + private claims ~$507M + punitive $507M + criminal $25M) | CS > 0 |

† M3 prices forward foreclosure; for completed one-event cases the forward question is moot. The backward Method-3 form (option value extinguished at the time of extraction, CSD composite per TA §5.5) is structurally available but outside this volume's empirical scope. Keep this as a table footnote.

Supporting Libby figures (TA §11.3): documented-cash floor ≈$2.6B (≈$1.35B committed + ≈$1.25B accrued monitoring 2000-2025 at $50M+/yr) → **≈26:1** against the ~$100M revenue (≥13:1 even if true revenue were twice the estimate). Mortality-inclusive total ≈$6.5-10.2B. W.R. Grace knew of contamination from 1963 and concealed it 27 years; B ≈ 0 throughout the operating period. (The old "~40x documented cost-to-revenue" Libby line is dead; use ≈26:1 cash floor or the ≈65-100x damage-function IPG, labeled.)

Supporting Deepwater figures (TA §11.2): BP all-in pre-tax charge **~$61.6B** (BP final estimate June 2016; risen to $65B+ by 2018, consistent with Ch5's ~$65B); ongoing Gulf ecosystem/fisheries externalities beyond BP's charges ~$8-12B (through 2025). Express Deepwater's M2 reading as a recovery share (BP paid roughly a third to forty percent of total documented cost through settlements; the remainder ran through restoration spending and uncounted long-tail damage), not as a multiplicative IPG.

### 1.4 Method-3 specification (chapter register — see prose rules before writing any of this)

- M3 = the **quasi-option value of preservation (Arrow-Fisher 1974 / Henry 1974)**, NOT the Dixit-Pindyck investment-timing model. (Dixit & Pindyck 1994 remains the lineage for OUTER Approach 2, standard finance real options; do not cite it as M3's lineage.)
- McDowell M3 = **$340-3,670/ton, geometric center ~$1,115/ton**. The old "$420-13,100 / mid ~$2,500" and the "$13,100 ceiling" are GONE; new top ~$3,670.
- Norway M3 = **$96-610/BOE, central ~$281/BOE; M3-IPG ~2.4-5.1x**.
- Structure (TA notation; the chapter should NOT print these symbols — see prose rule 4): CSD/RCV_M3 = V_market × scarcity_multiplier(ς) × irreversibility_premium(α); V_market = the resource's own market value; **no β exponent**. If the chapter ever needs the notation (it should not), per `manuscript/technical-appendix/symbol-registry_2026-06-07.md`: V_market (not V_option), ς (not σ), irreversibility 1/(1−α).
- Irreversibility is weighted **because the empirical record and the Asymmetric Regret Rule say so** (IPCC AR6 SPM B.5; Bernhardt & Palmer 2011), NOT a "discovered α-dominance." Never use "α-dominance" or any symbol-rename/process history in prose.

### 1.5 Norway / GPFG

- **GPFG value: NOK 21,268 billion at end-2025 (NBIM — the FX-invariant anchor); ≈ $2.0 trillion at the end-2025 USD/NOK rate, with an intra-2025 peak ≈ $2.2 trillion.** Anchor prose on the ~$2.0T figure (or the NOK figure); the USD number is exchange-rate-and-date dependent. This RESOLVES the v1 brief's $2.0T-vs-$2.2T flag: NOK-anchored ~$2.0T wins.
- **Fiscal rule: the 2017 revision sets the withdrawal ceiling at 3% expected real return; the original 2001 rule was 4%.** The chapter must present 3% as the 2017 revision (per-chapter citation correction, ledger). ⚠ The TA's source table still labels the ~3% rule "(2001)" — a TA-side mislabel; flagged in §6; do not copy it.
- Fund mechanics at Ch6's level: statute-established 1990, first deposit 1996; spending rule limiting withdrawal to expected real return (3%, 2017 revision); 1991 carbon tax; ethics-council governance and divestment. Ch4 is the canonical home; state the mechanics ONCE and point to Ch4 (seam R-4).
- Per-capita: **~$390k per Norwegian citizen** (where a per-capita figure is wanted).
- M2 anchor derivation (TA §11.5): GPFG ~$2.0T at ~75% capture rate of net petroleum wealth implies ~$2.67T total petroleum wealth ÷ ~55 billion BOE cumulative production ≈ **$48/BOE realized** (the M2 reading; the realized forward Bond B₂). Use $48 consistently (the old $48-vs-$50 inconsistency resolves to $48).
- **The backtest mechanism is IRREVERSIBILITY-REDUCTION, NOT rent-capture.** The GPFG's restoration optionality lowers Norway's effective irreversibility (α from ~1 absent the fund toward ~0.50-0.75), collapsing the Method-3 premium out of the divergent regime (to roughly 2-4x). Do NOT carry "16% rent captured," "$48/BOE rent captured," or "$300" framings. In chapter-register English: the fund does not buy back the barrel; it preserves the polity's option to restore and compensate, which is what shrinks the irreversible part of the loss.

### 1.6 Other shared figures the chapter may brush against

- **$108T Social Security figure is DISAVOWED** (the dishonest version); the honest version (Ch5 owns it) is "a few trillion, not a hundred." Ch6 should not need it; if it surfaces, route to Ch5's framing.
- **$11T household-wealth destruction (2008)** = **Federal Reserve Z.1**; Mian & Sufi = the housing-wealth (~$5.5T) + leverage/MPC analysis only. Attribute accordingly.
- **Foreclosures: ~4.1M completed.**
- **RCV-model per-ton estimate (TA): $525-540/ton** (Weitzman declining-rate integral; calibration TA §11.1). ⚠ The TA explicitly supersedes the previously printed $580-620 band ("rested on an unrecorded parameterization"); the figure ledger still lists $580-620 — flagged in §6. Chapters use the $510 honest TOTAL and may point to the appendix for the integral estimate; never conflate.
- DAC cost horizons (B5): Climeworks Orca ~$1,000+/ton first-of-a-kind; Mammoth (operational 2024) + Gen-3 trajectory toward ~$400-600/ton net-removal by 2030, ~$250-350/ton capture-only target (disclosed June 2024 Zurich Carbon Removal Summit); Carbon Engineering Stratos (Texas; commissioning, ramp through ~mid-2026) ~$300-600/ton; IEA *Direct Air Capture 2022* ~$230-600/ton; IPCC AR6 WGIII optimistic ~$100-300/ton mid-century. Present all four horizons; the answer is honestly horizon-dependent.
- SCC-as-political-object history (B4): ~$42 (Obama, EO 12866) / $1-7 (first Trump) / ~$51 (Biden interim) / $190 (EPA 2023). The load-bearing attribution is $190 = EPA 2023.
- Darity reparations field figure: **$14T (From Here to Equality 2nd ed. / JEP 2022)** — ONLY where a figure must be cited, and only as the field's figure, never the framework's. See §4 backward-direction rules.

---

## 2. REQUIRED BEATS + SECTION ARCHITECTURE

### 2.0 Role of the chapter (unchanged from v1 in function)

Chapter 6 is the book's measurement chapter and the formal hinge. Prior chapters showed the gap case by case; Ch6 computes it, names what the computation does not resolve, and formalizes the apparatus (RCV integral, the two-estimators-plus-reading triangulation, Four Gates, Commons Inversion Test), handing forward the Asymmetric Regret Rule and the two-instrument architecture. Register: analytical; human-texture density low by design, but one person or sensory anchor opens every technical stretch (prose rule 6). Within the arc: Ch5 names the two instruments; **Ch6 formalizes and measures**; Ch7 stress-tests universality; Ch8 walks one ton; Ch9 operationalizes.

### 2.1 THE REBUILT METHOD SPINE (read this before any beat; the v1 spine is dead)

Two distinct triads, which must NOT blur (use "Approach 1/2/3" for the outer and "Method 1/2/3" for the inner; make the nesting explicit where the inner triad is introduced):

**Outer triad (the chapter's frame):** Approach 1 bottom-up damage accounting; Approach 2 real options; Approach 3 the RCV framework. The outer convergence claim is alive and TA-backed (§9.5 three-model table): across the computable cases the three approaches produce IPGs far above 1 with overlapping ranges, and the direction never flips (McDowell 107-110x / 45-89x / 61-115x; Deepwater ~15-16x / 12-21x / ~17-18x; Libby 65-100x / 57-93x / 72-111x).

**Inner structure (inside Approach 3 — the recast):** the RCV estimate is produced by **two independent estimators**: M1 Replacement Cost (prices substitution; the floor; engineering data) and M3 Scarcity-Adjusted Option Value (prices option-bearing scarcity; Arrow-Fisher/Henry quasi-option value; market price plus context weights). **RCV = the M1 ∩ M3 convergence range.** Where the two estimators agree within a tight range from independent data, the RCV estimate is well-supported; where they diverge, the divergence is itself empirically informative. **M2 Revealed Preference is NOT a third estimator.** It reads the **realized Bond** — the B term of CS = RCV − B. The same observable cannot serve as an estimate of RCV and as the B subtracted from it. The M2 reading delivers two findings: (a) a **revealed lower bound** (a rational polity internalizes no more than it values, so RCV ≥ the M2 reading), and (b) **WHO PAID** — the mis-assignment finding. For McDowell, the realized bond is $50-88/ton societally-paid (including Black Lung) against $8-15/ton industry-paid: the instrument exists, at scale, charged to the wrong party (the Black Lung Trust Fund's federal-general-fund share is the documented analogue, TA §11.6). Forward, M2 reads the realized B₂ (Norway's GPFG); backward, the realized B₁ (restitution actually paid).

**The title conceit SURVIVES, re-conceived, and is arguably stronger:** two independent ways of counting what the commons was worth converge; the third way of counting reads what society has already paid, and finds both that it is a small fraction of the converged value and that the wrong party paid most of it. The old "three agree, therefore the gap is real" becomes "two agree, and the third shows the bill already being paid, by the wrong party." The chapter must state this spine explicitly and never revert to "three independent estimates converge" for the inner triad.

**Reporting discipline (carry as the framework's rule):** every CS estimate publishes both RCV estimators individually + the convergence range + the M2 realized-Bond reading (with who paid it) + identified divergence sources. No single-method CS claim has standing.

### 2.2 Ordered beats (hit every one; fresh prose throughout)

**B0 — Opening frame (no heading).** Recall the prior chapters' case-by-case gap; pose the representativeness + magnitude question. Escalation: one demonstration = anecdote; many = pattern; a price computable by independent methods whose direction never flips = a structural claim. Name the three outer approaches (bottom-up damage accounting, a real-options model, the RCV framework) and preview honestly what the computation cannot settle (carbon-term dominance + political volatility; substitutability uncertainty). The framework structures uncertainty rather than eliminating it. **State the thesis ONCE here; the old draft restated it three times in the first quarter — do not.** One person or sensory anchor opens the chapter (substrate-safe only; the McDowell substrate in §1.1 and Ch2-owned material referenced, not re-derived).

**B1 — Approach 1: bottom-up damage accounting.** One ton of Appalachian coal; enumerate, price, add. Health tier $2-4/ton (black-lung distributions "~$44 billion through 2009 (GAO/CRS)" allocated across national tonnage — always dated; Medicare/Medicaid cost-shifting; downwind cardio-respiratory harm; Ch2 owns Trust Fund mechanics — reference, including the debt: $5.1B as of Sept 2024, distinct from cumulative-paid). Environment tier $1-3/ton (acid mine drainage; failing tailings liners; buried headwaters; the $3.7-6B reclamation-bond shortfall is Ch2's figure — reference). Community tier $5-15/ton (NOT the jobs; what remained: outmigration, school closures, drug-epidemic costs, the 13-year life-expectancy gap, male 63.5 vs 76.5, ~2013 IHME estimate). The gap is a legacy effect; tie the legacy-effect pricing methodology to Darity and collaborators on the six-to-seven-year Black-white longevity gap (anchored as the historical NCHS-scale gap, NOT the headline of the 2022 wealth-mediated paper, whose figure is ~4 years; keep McDowell's 13-year gap clearly the coal-calibrated figure). Sum: non-carbon floor $8-22/ton vs the $4.71 1960 mine-mouth price ("just under five dollars") and the contemporary $40-140 band. A factor, not a rounding error.

**B2 — Add carbon.** Emission factor at the national-bituminous basis (2.32 t CO2/short ton), flagging the McDowell Pocahontas basis (2.61; AP-42 × ~28 mmBtu/short ton, heat-content source named) used by Ch8 + TA. × $190 (EPA 2023 central estimate) = **$441 national-basis carbon term**; the McDowell-basis carbon term is **$496 (carbon ONLY, never the total)**. National-basis bottom-up total ≈ $449-463 (labeled arithmetic). State the honest McDowell totals with pins: $510 = the 8-component honest TOTAL; ~$504-518 = the 4-component Pigouvian floor. Carbon is an order of magnitude larger than every other tier combined; state the implied capture fraction.

**B3 — Approach 1 across cases + define IPG.** Walk Deepwater (revenue ~$4B, a labeled framework derivation; BP all-in ~$61.6B June 2016, $65B+ by 2018; +$8-12B ongoing ecosystem externalities; damage-function IPG ~15-16x), Libby (revenue ~$100M industry estimate, unconfirmed; documented-cash floor ≈$2.6B ≈26:1; mortality-inclusive ≈$6.5-10.2B; IPG ≈65-100x with the VSL-vintage sensitivity available as a footnote), and Exxon Valdez (Ch6 OWNS Valdez — render in full: $5.5M product value spilled, with the one-event qualifier; $7-10B-scale cleanup + litigation + ecological damage from the public record; bottom-up IPG ~1,200-1,900x). Define the **Intergenerational Pricing Gap (IPG) = true cost ÷ market price**, and install the **lens discipline at the definition**: every IPG quoted in this book names its lens and its price basis, because a single bare multiple across mixed lenses and mixed price eras misleads (TA §11.11 carries the full decomposition). One-event disasters are bounded by what has been counted; state that qualifier.

**B4 — Limits of bottom-up + SCC as political object.** Bottom-up prices only what someone thought to count (flashlight-in-a-warehouse image, reinvented). SCC history: ~$42 Obama / $1-7 first Trump / ~$51 Biden interim / $190 EPA 2023. The SCC fight is a proxy war over tolerated cost severance; the qualitative result is robust for any SCC above zero; the zero-externality default is itself a contestable assumption, and a less rigorous one. Close on structures-uncertainty (weather-model analogy available, reinvented) and keep the "uncertainty is narrowing" coda SHORT (do not arm the Simon-Ehrlich substitution-optimism objection).

**B5 — Damage vs replacement (bridge to M1).** SCC prices what carbon does once emitted (damage side); DAC prices the engineering reversal (replacement side). Both belong in honest carbon accounting; they answer different questions. Walk the four DAC horizons (§1.6 figures). The replacement-side question belongs to Approach 3's Method 1; keeping the two separated is the framework's reporting discipline.

**B6 — Approach 2: the real options model.** A unit in the ground is an option; premature exercise destroys information value. Standard finance (Dixit & Pindyck 1994 lineage lives HERE, not at M3); how oil majors value undeveloped reserves. The standard model omits the social side: externality costs avoided by waiting, substitutability that develops, criticality information that accumulates. When social option value exceeds today's net extraction revenue, extraction is socially premature. Apply to 1960 McDowell coal ($4.71 mine-mouth; social option value tens-to-hundreds of dollars). A failure of pricing, not only of information — do NOT assert "the information was suppressed deliberately" (unsupported; soften to a defensible form or drop). The CFO-reachability point. Across cases the direction does not flip (the real-options column of TA §9.5 backs this: 45-89x McDowell, 12-21x Deepwater, 57-93x Libby).

**B7 — Approach 3: RCV, plain-English first, then formula.** Two unpriced components: foreclosure cost (substitutability-weighted; high-and-rising for coal-in-electricity, low for rare earths, near zero for helium cryogenics and fossil-aquifer water) and externality tail (independent of substitutability: black lung decades later, acid drainage for generations, carbon for centuries). Formula as a SUMMARY of the argument (TA §3 link): integrand [1 − S]·U + E, discount D per Weitzman declining rates; derived definitions CS = RCV − B and IPG = RCV ÷ market price. The appendix carries the proofs.
- **SCOPE CORRECTION (canonical; supersedes any "the framework only prices non-renewables + over-harvested renewables" framing):** the framework prices cost severance, the foreclosure of commons value, which is positive whenever consumption forecloses future access **faster than the commons can restore itself**: always for non-renewables (restoration is zero); for renewables only when harvest outpaces regeneration; for non-resource commons when degradation outruns recovery. Within restoration, the price is correctly zero. The commons floor is scarcity dynamics (ρ ≥ 0), NOT physical finiteness. "CS strictly positive for non-renewables" is a property of the fossil-fuel CASES tested, not a scope claim. Hard rules: NO "all extraction severs costs" overclaim; NO renewables-in-harmony normative inference.
- **Externality-tail naming: ONE sentence + TA pointer.** The single sentence may carry the load-bearing point (statistical-tail sense; no end-date; bond must carry forward indefinitely; Weitzman 2009 fat-tail lineage adjacency) — but no rejected-names catalogue, no multi-paragraph defense. (This replaces v1's "keep it tight"; the budget is now one sentence plus the pointer.)

**B8 — The counting structure inside RCV (REBUILT — the chapter's most important structural beat).** Deliver §2.1's spine in full prose:
- Motivate by the institutional asymmetry: markets price future profitability (DCF aggregated through equity/debt markets) but have no mechanism pricing future harms; the apparatus is the substitute for the missing harms-side mechanism.
- **M1 — Replacement Cost** (estimator; floor; engineer the substitute; DAC for McDowell's carbon dimension; $290-2,702/ton across DAC horizons, at-scale center ~$1,235; underprices irreplaceable commons — DAC does not restore foreclosed hydrocarbons or destroyed communities; Costanza-lineage). TA §3.3 pointer.
- **M3 — Scarcity-Adjusted Option Value** (estimator; the quasi-option value of preservation, Arrow-Fisher 1974 / Henry 1974; the resource's own market value carried up by scarcity and irreversibility weights; McDowell $340-3,670/ton, geometric center ~$1,115; Norway $96-610/BOE, central ~$281; the wide range is parameter uncertainty, not imprecision; irreversibility weighted because the empirical record and the Asymmetric Regret Rule say so — IPCC AR6 SPM B.5; Bernhardt & Palmer 2011). No Greek letters, no parameter intervals in running prose (prose rule 4). TA §3.5 pointer.
- **RCV = M1 ∩ M3.** McDowell ~$1,000-1,500/ton center (overlap ~$340-2,700); Norway ~$281/BOE center.
- **M2 — Revealed Preference reads the realized Bond** (NOT a third estimator; the B of CS = RCV − B; the same observable cannot estimate RCV and be the B subtracted from it). Norway anchor: GPFG ≈ $48/BOE realized (derivation §1.5). Two findings: the revealed lower bound (RCV ≥ the reading) and WHO PAID (McDowell: $50-88/ton societally-paid vs $8-15/ton industry-paid; the mis-assigned bond — the instrument exists, at scale, charged to the wrong party). This is where the chapter's strongest new sentence lives; land it.
- **Forward and backward.** Methodology is direction-agnostic; calibration adjusts. Backward: M1 specializes to remediation cost; M2 to the realized B₁ — **restitution actually paid**, and Ch6 OWNS the reverse-restitution roster (seam D4): Holocaust reparations, the 1988 Civil Liberties Act (Japanese-American internment redress), Black Lung Trust Fund payouts, the South African Truth and Reconciliation Commission, and the reparations-economics methodology of Darity and Mullen 2020. Equally diagnostic backward is who posted the realized B₁: where repair is publicly funded while the extractive beneficiary contributes nothing, the M2 reading reveals a mis-assigned bond. M3 backward = the option value extinguished at extraction time (the TA exposes, without settling, the ex-post vs ex-ante valuation fork). TA §5.5 pointer. Observe the §4 backward-direction rules (three states; coercion Open slot; no reef citation).

**B9 — The substitutability function.** Unchanged from v1: discount-rate impasse (Ramsey 1928; Stern low, Nordhaus higher, Weitzman declining; philosophers against any positive rate) sidestepped by an empirical question ("how quickly can we develop alternatives?"); four natural properties (near zero at extraction; monotone rising; asymptote ≤ 1; investment-dependent); concede the critic's fair objection (we moved the hard problem) and answer (a better hard problem: error bars shrink with research). TA §13 pointer.

**B10 — The Convergence (REBUILT).** Two layers, in order:
1. **Outer convergence:** the three approaches, different foundations, produce IPGs far above 1 with overlapping ranges across the computable cases, and the direction never flips (TA §9.5 values in §1.2). Make the why-three argument (each approach's blind spot illuminated by the others; triangulation as the standard scientific response — Campbell & Fiske 1959).
2. **The recast inner table:** present the 5-case table EXACTLY per §1.3 column architecture (M1 estimator / M3 estimator / RCV = M1 ∩ M3 / M2 realized-Bond reading / implied CS), with the † footnote on M3 for one-event cases. After the table: figures anchor to the TA worked-validation blocks (cite TA §11, the case-specific §11.2/§11.3/§11.5/§11.6 anchors — NOT "Block 4"/§3.6 triangulation-logic; correction flag 6); disaster-case cells cross-referenced to public sources (NOAA/DOJ/2016 BP Consent Decree; EPA Libby Superfund/Montana DOJ/W.R. Grace filings; Exxon Valdez Oil Spill Trustee Council/DOJ 1991).
3. **The old 33-122x / 50-555x reconciliation paragraphs are GONE.** In their place, the lens-explicit IPG statement per §1.2: name the lens and price basis whenever a McDowell multiple appears (carbon/damage-function ~107-110x against $4.71; RCV-integral 61-115x; Method-3 foreclosure premium 8.5-26x center ~15x, price-independent). State that these are different lenses on the same gap, not competing point estimates, and that on a consistent price basis they converge (TA §11.11 pointer). Do not attribute any bare-multiple headline to Ch2 or anyone; the bare multiples no longer exist anywhere in the book.
4. Case-ratio forms: Libby ≈26:1 documented-cash floor (≥13:1 under revenue doubt); Deepwater expressed as a recovery share through the M2 reading rather than a multiplicative IPG.
5. Land the central finding in the recast voice: the two estimators converge; the realized-bond reading shows the bill already being paid, mostly by the wrong party; across approaches and cases the direction never flips.

**B11 — The three follow-on objections.** As v1: (1) parameter-arbitrariness answered by convergence (now: M1 ∩ M3 from genuinely independent data — engineering cost vs market-price-plus-context-weights — plus the outer three-approach agreement); (2) Popperian falsifiability (CS = RCV − B can be ≤ 0; the two near-zero case-classes — sustainably managed renewable with full accountability; abundant non-renewable under stringent bonding; both testable; sound-barrier analogy reinvented; CIT = thought-experiment filter vs empirical falsifiability one layer up); note the M2 reading STRENGTHENS falsifiability — the B side is now directly observed, not modeled; (3) reproducibility (transparent disagreement; ranges are how applied cost-accounting works; failure is undisclosed sensitivity).

**B12 — The Norway Backtest (REBUILT mechanism).** Best-managed extraction case; GPFG per §1.5 (NOK-anchored ~$2.0T; statute 1990, first deposit 1996; 3% withdrawal ceiling per the 2017 revision of the 2001 rule; 1991 carbon tax; ethics council) — state once, point to Ch4 (seam R-4). Hartwick's Rule made real. Apply the apparatus: the fund is the realized forward Bond, read by M2 at ≈$48/BOE; the RCV estimators put the value at ~$281/BOE center; implied CS ≈ $233/BOE, ~$12.8T cumulative. **The fund's real mechanism is irreversibility-reduction:** it preserves restoration optionality, pulling the irreversibility of the loss down (out of the worst regime), which is why Norway's M3 premium is modest (M3-IPG ~2.4-5.1x) — render this in plain English (the fund cannot manufacture subsurface petroleum, but it keeps open the polity's capacity to restore and compensate; that is what it bought). NOT rent-capture; never "16% / $48 rent captured / $300." Result: CS small but positive; the externality non-Norwegians bear is not in the fund; the model differentiates; Norway is closest to honest pricing and still not all the way there.

**B13 — Ten commons categories (illustrative).** Unchanged from v1: Habitability, Spatial, Temporal, Institutional, Kindred, Ecosystem, Political, Cohesion, Epistemic, Autonomy; explicitly illustrative, not closed (Ostrom eight principles / Sen-Nussbaum capabilities / Rawls primary goods precedent); traditions differ on what is shared (classical-liberal, civic-republican, socialist/communitarian, Marxist, lived-oppression) and the framework works within any; reject the legislative posture; linger on Autonomy (Anderson, Pettit, Skinner; three readings accommodated); reference Ch1's 120-hour-week as the most-favorable-conditions test (Ch1 owns it; do not re-render — seam R-10). If only the habitability half gets fresh depth, soften the "two categories at depth" promise so it is kept honestly (BP-6).

**B14 — What Is Owed (Parfit).** Unchanged in structure: non-identity problem stated as the deepest objection; Parfit's outcomes-level (impersonal) response adopted; RCV operates in that register; the two-instrument architecture inherits the forward-impersonal / backward-person-affecting distinction; different methodological work per direction (reparations economics vs environmental-bond economics); honest concession that the framework operates WITHIN the vocabulary rather than solving the problem; Darity-Mullen engaged at depth in Ch5 — reference. **The closing empirical anchor must be lens-explicit** (the old draft closed on a bare "IPG of 33"): recommended figure = the Method-3 foreclosure-premium lens, 8.5-26x with center ~15x, named as the most conservative, price-independent lens (author call A1 if a different lens is preferred).

**B15 — Sen capabilities.** Unchanged: Parfit grounds standing, Sen grounds valuation; RCV as a measurement of the capability set extraction forecloses; the pairing makes the claim defensible across moral philosophy and welfare economics simultaneously.

**B16 — Two kinds of commons (Ostrom boundary).** Unchanged: coordination commons (Ostrom's eight design principles; Hardin contradicted via Ostrom's empirical refutation — the book's one clean contradiction) vs extraction commons (value-capturers are not shared-stakeholders with cost-bearers; structural asymmetry); CIT sub-forms make it operational; adjacent and complementary, parallel analyses where both elements present; heterogeneous-stakeholder break-point connecting to stratification economics (Darity, Hamilton). State the coordination-vs-extraction distinction ONCE, cleanly (seam R-5).

**B17 — The Four Gates.** Unchanged in content: Gate 1 CIT (two sub-forms: Commons-Absence Inversion → replacement cost; Commons-Consumption Inversion → opportunity cost; the two run different filters, including the Ostrom routing; revealed preference declined as the discrimination gate but retained as estimation input — and note the M2-recast makes this cleaner: revealed preference's "blind spot" (it reads what was paid, never what is owed) is precisely what makes it the right instrument for the B side, and the wrong one for the gate). Gate 2 units-consistency (DALY example); Gate 3 boundedness; Gate 4 independence (Cohesion/Habitability double-count example). Gates jointly necessary; TA Four-Gates + formula-generalization pointers. **CIT naming: ONE sentence + TA §6 pointer** (the sentence may carry the Lewis-counterfactual one-premise-flip point; no rejected-names catalogue).

**B18 — The Contribution.** Unchanged in content: extends Pigou + Ostrom into extraction contexts; the three additions (substitutability-weighting with the Hotelling Identity — RCV − Hotelling rent = CS per unit, Hotelling 1931 credited cleanly; integrated architecture — one gate-disciplined formula; CIT as discovery method — generative, not inherited categories); apply the additions to McDowell, Deepwater, Libby ("standard Pigouvian analysis has no principled reason to exclude these costs; it simply has no method for including them"). **Numbers in this beat use the §1.1 pins** ($496 carbon McDowell-basis / $510 honest total / ~$504-518 Pigouvian floor / $441 national-basis; the old "$518-532" is dead). **RCV naming: ONE sentence + TA pointer** (Hartwick residual + Ostrom commons + Mazzucato value may be named inside the one sentence; no thesaurus walk). Optional one-clause Pistor/financialization inoculation (accounting the cost, not coding the asset) — keep light; Ch9 owns the full version.

**B19 — What the chapter leaves for later + ARR.** Unchanged: forward handoffs (Ch7 Mars test; Ch8 one worked ton); introduce and name the **Asymmetric Regret Rule** (Savage 1951 minimax-regret specialized to decisions where one direction of regret is commons-extinction; does not replace CBA where CBA works), deferred to Ch9. **ARR naming: ONE sentence + TA §8 pointer** (regret-not-risk and asymmetric-not-one-sided may live inside the sentence). The empirical support sentence must follow §1.4's framing: the rule's irreversibility weighting is grounded in the empirical record (IPCC AR6 SPM B.5; Bernhardt & Palmer 2011) — NOT "Method 3's α-dominance finding."

**B20 — Close.** The central finding restated with force, in the recast voice: independent methods built on different decades and schools, applied to the same extractions, agree in direction and overlap in magnitude; the realized-bond reading shows the bill is already being paid, by the wrong party; the gap is a feature of how the extraction economy runs. A short, earned closing cadence is permitted (it is the chapter's ONE budgeted antithesis/cadence flourish — see prose rule 2); write fresh words. NO "End of Chapter" marker.

### 2.3 Landing points the chapter owns (updated)

1. Unpriced costs are real, MEASURABLE costs: **two independent estimators converge on what the commons was worth, and the realized-bond reading shows what has actually been paid and by whom** — producing a legible number against market price. (Spine.)
2. Magnitude: honest cost exceeds market price by an order of magnitude or more (McDowell), lens-explicit, carbon/foreclosure dominating. (Shared with Ch2 + Ch8.)
3. The framework DIFFERENTIATES (Norway small CS via irreversibility-reduction; worse-governed extraction large CS). (Norway Backtest.)
4. The framework names its own limits honestly (discount rate unsettled; non-denominable unpriced; substitute timelines unpredicted; "count, not stop").
5. The framework EXTENDS existing traditions (Pigou, Ostrom, Hotelling, Hartwick, reparations economics). (Contribution.)
6. NEW: the mis-assignment finding — where an accountability instrument exists, it is routinely charged to the public rather than the extractor; M2 is the instrument that sees this.

### 2.4 Threads + seams (carried forward, updated)

- Ch6 SETS UP: ARR (→ Ch9; relied on in Ch7); the RCV integral + the two-estimators-plus-reading structure + substitutability gap (→ Ch7); backward/Restitution grounding + the reverse-restitution roster (Ch6 OWNS, seam D4); the carbon externality tail closure deferred from Ch2.
- Ch6 RELIES ON (reference, never re-derive): Norway/GPFG mechanics (Ch4; seam R-4 — one statement); black-lung Trust Fund + reclamation-bond shortfall (Ch2); 120-hour-week (Ch1; seam R-10); Darity-Mullen depth (Ch5); the worked $510 ton (Ch8).
- Ch6 OWNS Exxon Valdez in its enumeration (seam D10/B-3); render in full here from the public record.
- TA anchor precision (seam D13): method links point to §3.3/§3.4/§3.5 anchors; worked figures cite the §11 validation blocks (§11.2 Deepwater, §11.3 Libby, §11.5 Norway, §11.6 McDowell, §11.11 IPG reconciliation); never "Block 4."
- The Restitution-Bond worked empirical case is NOT Ch6's to deliver. **The volume's single computed backward case (the Chesapeake reef, TA §11.12) is MERGE-HELD until Ch3 prices it and is NOT in the current TA build — Ch6 must not cite §11.12 or the reef computation.** Ch6's backward-direction material stays at "structurally available but outside this volume's empirical scope" for the disaster cases.
- Rule 7: treat every seam above as DECIDED. State forward-handoffs cleanly; no "this will be addressed elsewhere" hedges for content this brief assigns to Ch6.
- Structural constraints carried from v1: outer/inner triads must not blur (distinct labels, explicit nesting); honest-limits posture mandatory; no scaffolding language in prose (no "Option A/B," "ratified," INCLUDE/EXCLUDE glyphs, process vocabulary, TK/TODO); no end-marker.

### 2.5 Word floor

**MINIMUM 11,000 words; NO maximum; substance drives length.** The ~1,500 words of naming digressions and the dead reconciliation paragraphs do not count toward substance; the rebuilt B8/B10/B12 material (who-paid finding, lens discipline, irreversibility-reduction backtest) is new substance that replaces them. Do not pad; do not compress the three approaches, the inner structure, the case applications, the Four Gates, the objections, the contribution, or the philosophical groundings.

---

## 3. REQUIRED CITATIONS + LITERATURE POSITIONING

### 3.1 Citations to carry (substrate-safe; attribute as stated)

- Carbon arithmetic: EPA AP-42 §1.1 (93.28 kg CO2/mmBtu) × heat content (national ~24.9 / Pocahontas ~28 mmBtu/short ton; USGS/EIA) × EPA-2023 SCC $190.
- SCC attribution (blocking): $190 = **EPA 2023 central estimate**, "drawing on Rennert et al. 2022" whose own central was ~$185. Never $190-to-Rennert.
- 1960 coal price: EIA Total Energy Table 7.9 ($4.71 bituminous; $4.83 all-coal).
- SCC political history: ~$42 Obama (EO 12866) / $1-7 first Trump / ~$51 Biden interim / $190 EPA 2023.
- DAC horizons: Climeworks (Orca; Mammoth 2024; Gen-3 trajectory, June 2024 Zurich Carbon Removal Summit); Carbon Engineering Stratos (~mid-2026 ramp); IEA *Direct Air Capture 2022*; IPCC AR6 WGIII.
- Convergence-table public anchors: NOAA Office of Response and Restoration / DOJ / 2016 BP Consent Decree (Deepwater; BP all-in ~$61.6B = BP's own June 2016 final estimate); EPA Libby Asbestos Superfund record / Montana DOJ / W.R. Grace filings + **Naik et al. 2017** (694 documented deaths through 2011) + EPA VSL $7.4-11.0M (Libby); Exxon Valdez Oil Spill Trustee Council / DOJ 1991 settlement (Valdez).
- McDowell life expectancy: IHME / Dwyer-Lindgren et al., *JAMA Intern Med* 2017 (~2013 vintage).
- Norway: NBIM (NOK 21,268 bn end-2025); Norwegian Petroleum Directorate / Norwegianpetroleum.no (cumulative production ~55B BOE); Ministry of Finance (fiscal rule; 3% = 2017 revision); 1991 carbon tax.
- Irreversibility empirical record: **IPCC AR6 SPM B.5; Bernhardt & Palmer 2011.**
- Lineage: Pigou 1920; Hotelling 1931; Hartwick 1977; Weitzman 2001/2009; **Arrow-Fisher 1974 / Henry 1974 (M3)**; Dixit & Pindyck 1994 (Approach 2 ONLY); Savage 1951; Lewis 1973; Parfit 1984; Sen; Nussbaum; Mazzucato 2018; Darity & Mullen 2020 (+ JEP 2022 / 2nd ed. for the $14T field figure, only if a figure must be cited); Costanza et al.; Campbell & Fiske 1959; Pettit 1997 / Skinner 1998 / Anderson 2017; Ostrom 1990; Hardin (via Ostrom's refutation); Ramsey 1928; Stern / Nordhaus.

### 3.2 Lineage placements (claims unchanged from v1 except as noted)

Spine: "extend-into-a-setting-they-could-not-reach" for the formal canon (Pigou, Hotelling, Hartwick); "add-to" for diagnostic/critical traditions (Daly, Mazzucato, Darity-Mullen, Costanza, Sen/Nussbaum, Parfit); "parallel/extend" for Ostrom and civic republicans; "adopt-directly" for Weitzman discounting; "contradict" ONLY Hardin (via Ostrom); "refuse-to-settle" the Nordhaus-Stern rate dispute. Specific claims per the v1 inventory, with TWO updates:
1. **Method 3's lineage is Arrow-Fisher/Henry quasi-option value** (option value of preservation under irreversibility). Dixit & Pindyck 1994 is cited at Approach 2 (investment-timing real options, what oil majors already use) and may be named in the TA's option-value tradition; do NOT present D&P as M3's model.
2. **Revealed preference (Samuelson, Hicks lineage):** retained as the instrument for the B side (the realized-Bond reading), rejected as the discrimination gate AND no longer presented as an RCV estimator. Its blind spot (reads what was paid, never what is owed) is exactly what makes it correct for B.

Positioning gaps (do not invent content to fill, do not aggravate): Nancy Fraser absent book-wide (separate ratified workstream; only weave a Fraser/Polanyi anchor if substrate-safe and brief); Pistor/financialization objection gets at most the B18 one-clause inoculation (Ch9 owns the full answer).

### 3.3 Correction flags (carried + new; all blocking unless noted)

1. Longevity gap: six-to-seven-year Black-white gap = the HISTORICAL NCHS-scale figure (the 2022 Himmelstein/Darity et al. *JAMA Netw Open* wealth-mediated headline is ~4 years — do not conflate); McDowell 13-year gap kept separate and clearly coal-calibrated.
2. SCC $190 = EPA-2023-not-Rennert.
3. "Darity 2026" private-interview hazard: do NOT cite any unpublished interview or attribute endorsement to a living scholar; published Darity sources only.
4. Norway $48/BOE used consistently (no $50); it is the M2 realized reading, never "rent captured."
5. TA citation locations: §11 worked-validation blocks + §3.3/§3.4/§3.5 method anchors (never "Block 4").
6. Deepwater revenue ~$4B is a labeled framework derivation (reserve × price), not a sourced figure; the old $4.25B is retired.
7. Libby revenue ~$100M is an industry estimate no primary source confirms; carry the qualifier (the ≥13:1 robustness note covers it).
8. No invented factual claims (see prose rule 6); the real-options "information was suppressed deliberately" causal claim remains unsupported — soften or drop.

---

## 4. TA-STATE METHOD CANON AS IT APPLIES TO THIS CHAPTER (merged 2026-06-09/10)

Every draft MUST match the TA (`manuscript/technical-appendix/TechnicalAppendix_v2.0.0.html`); verify there where in doubt. The items below are the chapter-relevant canon, re-verified against the TA on 2026-06-10.

1. **Estimator structure (§3.4/§3.6):** M1 + M3 are the two RCV estimators; RCV = M1 ∩ M3 convergence. M2 reads the realized Bond (forward B₂ = Norway's GPFG; backward B₁ = restitution actually paid) and sets a revealed LOWER BOUND on RCV (RCV ≥ the M2 reading). **"Three independent estimates converge" is retired** for the inner triad. The outer three-approach convergence (TA §9.5) remains valid and is a different claim — keep them distinct.
2. **IPG is lens-explicit ONLY:** Method-3 foreclosure-premium 8.5-26x (center ~15x, price-independent); carbon/Damage-Function ~107-110x (against $4.71); RCV-integral **61-115x per the TA's current text** ($525-540/ton; calibration §11.1) — the figure ledger reads 67-134x; flagged, not resolved here. Bare "33-122x", "~50x", "555x", "50-555x" are RETIRED; never quote.
3. **M3 = quasi-option value (Arrow-Fisher/Henry);** composite V_market × scarcity × irreversibility, no β; McDowell $340-3,670/ton center ~$1,115; Norway $96-610/BOE central ~$281, M3-IPG 2.4-5.1x.
4. **Norway:** CS-reduction = IRREVERSIBILITY-REDUCTION (restoration optionality; α from ~1 toward ~0.50-0.75), NOT rent-capture; ~$48/BOE realized (M2 reading); fiscal rule 3% = 2017 revision (2001 rule was 4%); per-capita ~$390k; GPFG NOK 21,268bn end-2025 ≈ $2.0T.
5. **Coal:** $4.71/ton 1960 mine-mouth ("just under five dollars"); $496 = McDowell carbon term ONLY; $510 = 8-component honest TOTAL; $441 = national-basis carbon; $504-518 = four-component floor.
6. **Black lung:** "$44 billion through 2009 (GAO/CRS)", always dated; Trust Fund DEBT $5.1B Sept 2024, distinct from cumulative-paid.
7. **Scope correction (author-ratified 06-09):** CS positive when consumption forecloses future access faster than restoration (always non-renewables; renewables only past regeneration; zero within restoration); commons floor = scarcity dynamics, not finiteness; no "all extraction severs" overclaim; no renewables-harmony inference.
8. **Backward direction:** §5.5 three states of a gate-admitted cost slot — **Zero** (under abundance the cost genuinely is $0), **Filled** (value entered, derivation shown), **Open** (a real, gate-admitted slot deliberately left empty; Open ≠ Zero ≠ unpriceable). The reef is the volume's single computed backward case (§11.12) but is **merge-held until Ch3 prices it and absent from the current TA build — do not cite it**. **Coercion/reparations = an Open slot, first-person-abstention voice only** (the author declines, in first person, to fill that column for a group he is not part of; NO standing-gatekeeping language like "theirs to enter" / "only the affected"); **NEVER a coercion/reparations dollar figure in publisher-facing prose**; Darity field figure $14T (2nd ed/JEP 2022) only where a figure must be cited, credited to the field (Darity, Mullen, Hamilton, Coates, Conley, et al.).
9. **Shared-figure hygiene:** $108T Social Security DISAVOWED; $11T household wealth = Federal Reserve Z.1 (Mian & Sufi = housing ~$5.5T + leverage/MPC only); foreclosures ~4.1M completed; US Steel McDowell exit "across the 1980s" (no point-year); McDowell 2020 population ~19,000 / "under 20,000".

---

## 5. PROSE RULES (hard requirements; verified against the whole corpus 2026-06-10)

1. **ZERO em-dashes and en-dashes in prose.** Use commas, periods, parentheses, or restructured clauses; numeric ranges use a plain hyphen ("$8-22", "61-115x"). Verify with grep before returning. (The canonical Ch6 has 193 em-dashes + 12 en-dashes; the target is 0 + 0.)
2. **Antithesis budget:** "Not X. It is Y." / "is not A; it is B" constructions at most ~1 per 1,500 words. Vary paragraph endings — some paragraphs simply end; NO aphorism-epigram at every paragraph/section close. The B20 closing cadence is the chapter's one budgeted flourish.
3. **NO self-narration:** never narrate what the chapter/book/framework is doing or about to do ("Hold onto that...", "The chapter has done its work", "I want to say/engage/be specific...", "this chapter is about..."). The disclaimer "the framework does not legislate" may appear AT MOST once. "The framework" is never the subject of consecutive sentences.
4. **NO white-paper register:** terminology defenses = one sentence + a Technical Appendix pointer, never a digression (applies to externality tail, CIT, RCV, ARR — all four); method description at chapter register (no Greek-letter regime names or parameter intervals in running prose); numbers as numerals (no spelled-out number walls); NO workshop vocabulary (steelman, pressure-test); no archival/process vocabulary ("named ... in the record").
5. **Every load-bearing number carries a named external authority** (never bare "economists" / "studies"). If the substrate has no namable source, restructure to not need the number (Path A) and leave a structure-note.
6. **One person or sensory anchor opens every technical stretch — substrate-safe ONLY. NO INVENTED FACTS:** every biographical detail, scene element, quoted speech, number, date, name from this brief / the listed substrate / canonical chapters only; gaps get `<!-- structure-note: ... -->` comments, never invention. Preserve all consent/anonymization decisions.
7. **Register models:** the harbor frame of `manuscript/chapters/Chapter_10_CommonBonds.md` (opening + closing) and the Biggie section of `manuscript/chapters/Chapter__3_TheWaterman.md`. Read both before drafting; match their grain.
8. **Substance drives length; do not pad, do not cut substance.**

Additional Ch6-specific prose directives (from the 06-08/06-10 review cycle):
- **Thesis stated ONCE** (B0). The convergence finding lands again only at B10/B20 as a computed result, not as a re-preview.
- The four name-defense digressions of the old draft (~1,500 words total) are each ONE sentence + TA pointer (B7, B17, B18, B19).
- Globally Inclusive Plain English; dual-audience (lay + specialist); lead with the plain-English argument before any formula; the math is a summary of an argument that already stands without it.
- Keep the B4 "uncertainty is narrowing" coda short (Simon-Ehrlich exposure).

---

## 6. OPEN AUTHOR CALLS (carried forward + new)

**New in v2:**
- **A1 — Parfit-close lens choice (B14).** Brief recommends the Method-3 foreclosure-premium lens (8.5-26x, center ~15x; most conservative, price-independent) as the lens-explicit figure anchoring the close. Alternatives: carbon/damage-function ~107-110x (more vivid, price-basis-dependent) or RCV-integral 61-115x. Default to the recommendation unless the author overrides.
- **A2 — Ledger-vs-TA discrepancies (route to the figure-ledger owner; drafts follow the TA).** (i) RCV-integral IPG: ledger 67-134x vs TA current 61-115x. (ii) RCV-model per-ton band: ledger $580-620 vs TA $525-540 (TA explicitly supersedes the $580-620 as an unrecorded parameterization). Do not edit the ledger from the Ch6 workstream.
- **A3 — M1 pending refresh.** The TA §11.9 DAC-anchor refresh is expected to move the M1 conservative cap ~20%. Drafts use the TA's current $290-2,702 (which already supersedes the old chapter's $261-2,412); the rigor pass re-verifies M1 against the TA at fact-check.
- **A4 — Norway fiscal-rule label in the TA.** The TA's source table shows "~3% ... Norway fiscal rule (2001)"; canon is 3% = the 2017 revision (2001 = 4%). Chapter says 2017@3%; the TA label routes to the TA owner.
- **A5 — Valdez retention.** The TA carries no Valdez case (its case set: McDowell, Norway, Deepwater, Libby, Baotou). Ch6 retains Valdez per seam D10/B-3 from the public record. Flag only if the author prefers to harmonize the chapter's case set to the TA's.

**Carried forward from v1 (still open):**
- **A6 — Fraser/Polanyi positioning gap** (separate ratified workstream; weave only if substrate-safe and brief).
- **A7 — Pistor one-clause inoculation in B18** (optional; Ch9 owns the full version).
- **A8 — BP-6 "two categories at depth" promise** (soften if the time/autonomy half is only a Ch1 recap).
- **A9 — TA §11.9 DAC refresh + the formerly flagged Ch6↔TA M1 reconciliation** are the same workstream as A3; the v1 "route to correctness/IPG owner" flag is now satisfied by drafting to the TA's current values, with A3's re-verify note.

**Resolved since v1 (no longer open):** GPFG AUM vintage (NOK-anchored ~$2.0T end-2025; intra-2025 peak $2.2T — v1 flag 8 closed); the $48-vs-$50/BOE inconsistency ($48); the M3 ceiling caveat (the $13,100 ceiling no longer exists); the 33-122x attribution-to-Ch2 instruction (the bare range is retired book-wide; no attribution needed or permitted).

---

*End of brief.*
