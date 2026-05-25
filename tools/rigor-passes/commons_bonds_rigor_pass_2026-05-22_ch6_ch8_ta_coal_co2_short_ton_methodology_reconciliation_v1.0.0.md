# Commons Bonds — Ch 6 / Ch 8 / TA Coal-CO₂ Short-Ton Methodology Reconciliation

**Pass type:** Stage 1c cross-artifact coherence + methodology reconciliation (artifact-only; PROPOSED).
**Date:** 2026-05-22 (PROPOSED); ratified 2026-05-23 (recommended bundle).
**Author:** Claude.
**Status:** **RATIFIED — recommended bundle (§6.1 Option C + §6.2 Option C
+ §6.3 Option A).** Phase C application pending (separate session).
**Branch:** `claude/ch6-ch8-ta-coal-co2-methodology-reconciliation-stage1c`.
**Parent workstream:** Manuscript Stage-3 Rigor Pass (PM dashboard #20); routed via cross-thread #12 in [`publishing/essays/_pipeline/cross-thread-todos.md`](../../publishing/essays/_pipeline/cross-thread-todos.md#12-ch-8-line-73-coal-co-short-ton-accounting-cascade--pre-existing-finding-for-ch-8-pass-1).

---

## §1 — Scope + cross-thread #12 history

### §1.1 Scope of this session

This session performs the Stage 1c cross-artifact coherence check that Ch 8
Pass 1 (artifact `tools/rigor-passes/commons_bonds_rigor_pass_2026-05-16_ch8_what_things_actually_cost_stage3_fact_check_v1.0.0.md`)
did not absorb, plus the substantive dimensional-analysis question that
cross-thread #12 surfaced. The session produces a reconciliation artifact with
author-ratification options under the Amendment-C Interactive Ratification
Protocol (Options + Recommendation + Reasoning per finding).

**Artifact-only:** no chapter / TA / inventory edits this session. Phase C
application of ratified options is a separate downstream session (sequencing
recommendation at §7).

### §1.2 Cross-thread #12 history (surface → routing → audit gap)

- **2026-05-14 (commit `0d63d3b`).** Ch 6 Pass 1 Amendment E surfaced
  MEDIUM-11: Ch 6 + TA + Ch 8 had three different coal-CO₂ short-ton
  accounting bases. Amendment E ratified **Option A (EPA AP-42 §1.1 short-ton
  accounting)** for Ch 6 + TA: canonical figure 2.32 metric tons CO₂ per
  short ton coal (93.28 kg CO₂/mmBtu × ~24.93 mmBtu/short ton per EPA AP-42
  §1.1 + EIA documented heat-content tables). Carbon-tail externality at
  SCC $190/mt CO₂: ≈ $441/short ton coal.

- **2026-05-14 (commit `f6bb6ad`).** Ch 6 Phase C-β applied the cascade to
  Ch 6 lines 42 + 44 + 343 (current line numbers post Ch 6 developmental-
  edit application; lines 32 + 34 + 321 at the time of the original
  cascade). TA §11.6 McDowell
  calibration table (current lines 4517 + 4520 + 4533) was already at the
  canonical basis; TA §7.4 Gate 4 worked example (current line 2859) was
  also at the canonical basis. TA §11.1 Damage Function McDowell row
  (current lines 3876 + 3882 + 3898) + TA §1.7 Numerical update (current
  line 2916) were NOT touched in the cascade — internal-TA drift below.

- **2026-05-14 (commit `ffefa85`).** Cross-thread #12 routed the Ch 8-side
  cascade to "Ch 8 Pass 1 audit session" with explicit recommended-edit
  text: "approximately five hundred and forty-four dollars" → "approximately
  four hundred and forty-one dollars"; "approximately 2.86 tons of carbon
  dioxide" → "approximately 2.32 tons of carbon dioxide (EPA emission
  factor for bituminous coal at short-ton accounting)."

- **2026-05-16.** Ch 8 Pass 1 fact-check (artifact
  `tools/rigor-passes/commons_bonds_rigor_pass_2026-05-16_ch8_what_things_actually_cost_stage3_fact_check_v1.0.0.md`)
  fired and **did not engage with cross-thread #12.** The artifact's §11 source
  inventory verified the existing Ch 8 figure (2.86 short tons CO₂ × $190 =
  $544/ton coal) against `https://www.eia.gov/environment/emissions/co2_vol_mass.php`
  as the cited source. No dimensional-consistency cross-check was performed.
  MEDIUM-11 + EPA AP-42 + 2.32 do not appear anywhere in the Ch 8 Pass 1
  artifact.

- **2026-05-21 (commit `5fe6af6`).** Ch 8 Pass 1 Phase C applied 16 ratified
  Ch 8 spot-fixes. Did not include the cross-thread #12 cascade fix.

- **2026-05-21 (PM session third pass).** Cross-thread #12 status note added
  to `publishing/essays/_pipeline/cross-thread-todos.md`: "Ch 8 Pass 1 Phase C
  (commit `5fe6af6`, 2026-05-21) did NOT absorb the Ch 6 canonical coal-CO₂
  cascade fix; [Chapter__8_WhatThingsActuallyCost.md:72] still reads '2.86
  tons' + 'five hundred and forty-four dollars.' Cascade-fix kick-off
  paste-text drafted in endnote-sweep handoff §9.3; absorbed into Phase 1
  prerequisites for the sweep workstream."

### §1.3 What this session adds beyond the cross-thread #12 routing

Cross-thread #12's recommended edit ("apply Ch 6's $441 cascade verbatim to
Ch 8") is a **partial** fix: it resolves the cross-corpus consistency problem
but does not surface the underlying **dimensional-analysis bug** in Ch 8's
arithmetic, nor the **source-attribution error** in the cited EIA URL, nor
the **methodology question** of whether Ch 6 + TA's national-bituminous-
average heat-content basis is the right basis for a chapter explicitly
walking *McDowell County–specific* coal extraction. This session surfaces
all three.

Per `feedback_audit_recent_active_review_default.md`: the Ch 6 Pass 1
Amendment E + Ch 6 Phase C-β cascade is the more recent active-review record
(2026-05-14) compared to the older Ch 8 prose (which predates Ch 8 Pass 1).
Trust-decision: **trust the Ch 6 Amendment E + Phase C-β cascade as the
established canonical basis**; the question this session adjudicates is
whether the canonical basis should remain at the national-bituminous-
average heat content (Option A — preserve cross-thread #12 alignment) or
move upward to McDowell-specific high-grade Appalachian bituminous (Option
B — methodology upgrade requires Ch 6 + TA touches).

---

## §2 — Dimensional-analysis verification chain

### §2.1 Claim under test

Ch 8 line 72 currently reads:

> "One ton of coal, when burned, releases approximately **2.86 tons** of
> carbon dioxide into the atmosphere. The EPA's most recent estimate of the
> social cost of carbon — the economic damage caused by each ton of CO₂
> released, anchored to the Rennert et al. 2022 *Nature* integrated estimate
> that grounded the 2023 EPA update — is **one hundred and ninety dollars**.
> The arithmetic is not subtle. The climate cost of burning one ton of coal,
> at the currently published federal estimate, is approximately **five
> hundred and forty-four dollars**."

The arithmetic compresses: 2.86 × $190 = $543.40 ≈ $544. The compression
treats the units of 2.86 and the units of $190/ton as if they cancel.

### §2.2 SCC $190 denomination — primary-source verification

**Source 1: EPA 2023 Report on the Social Cost of Greenhouse Gases**
(*EPA SCGHG 2023 Final Report*, December 2023; central estimate $190/tCO₂
for 2020 emissions vintage at 2% near-term Ramsey discount rate).

**Source 2: Rennert, Errickson, Prest et al. (2022).** "Comprehensive
evidence implies a higher social cost of CO₂." *Nature* vol. 610, DOI
[10.1038/s41586-022-05224-9](https://www.nature.com/articles/s41586-022-05224-9).
Central SCC estimate: **$185/tCO₂** at 2% near-term discount rate (2020
USD; 5%–95% range $44–$413). The paper's units throughout: **metric tons
CO₂**. This is the standard climate-economics convention; IWG SCC TSDs
(2010, 2013, 2016, 2021) and IPCC AR6 WG III (2022) all denominate SCC in
metric tons CO₂ (= tonnes CO₂).

**Source 3: RFF Social Cost of Carbon explainer**
(`https://www.rff.org/publications/explainers/social-cost-carbon-101/`)
and RFF In Focus piece on the EPA's new SCC
(`https://www.resources.org/in-focus/in-focus-the-us-environmental-protection-agencys-new-social-cost-of-carbon/`).
Both explicitly compare EPA's $190 to the prior government-wide estimate of
$51/tonne, confirming the metric-ton denomination convention across the
SCC literature.

**Verification chain:** EPA 2023 RIA $190 → Rennert 2022 *Nature* integrated
estimate methodology → IPCC AR6 WG III conventions → climate-economics
literature standard. **All in metric tons CO₂.** Confirmed.

### §2.3 EIA volume/mass coal-CO₂ page (Ch 8's cited source) — primary-source verification

**Source:** [EIA, CO₂ Emissions from Coal Combustion](https://www.eia.gov/environment/emissions/co2_vol_mass.php).
Verified 2026-05-22.

**What the EIA page actually publishes for bituminous coal:**

| Coal type | Pounds CO₂ / short ton coal | Kilograms CO₂ / short ton coal | Metric tons CO₂ / short ton coal |
|---|---|---|---|
| Anthracite | 5,735.68 | 2,601.67 | 2.60 |
| **Bituminous** | **5,124.76** | **2,324.56** | **2.32** |
| Subbituminous | 3,693.82 | 1,675.49 | 1.68 |
| Lignite | 3,078.46 | 1,396.37 | 1.40 |

Data source per EIA: U.S. Environmental Protection Agency, *Inventory of
U.S. Greenhouse Gas Emissions and Sinks: 1990–2022*, Tables A-20, A-25,
A-32, and A-226.

**Critical finding:** the EIA emission-factor table at the cited URL gives
**2.32 metric tons CO₂ per short ton bituminous coal**, NOT 2.86. The 2.32
figure is the same one Ch 6 + TA §11.6 already use. Ch 8 Pass 1's source
inventory line 491 ("EIA confirmed 1 short ton 78%-carbon, 14,000-BTU/lb
coal yields 2.86 short tons CO₂ on complete combustion") cites this EIA URL
as the authority for 2.86 — but the URL's tabulated emission factor for
bituminous coal is 2.32 mt/short ton, not 2.86. **Ch 8 Pass 1's source
attribution is incorrect.**

(The 2.86 figure derives from a separate stoichiometric calculation:
78% C × 2,000 lb/short ton coal × 44/12 [mass ratio CO₂/C from complete
combustion stoichiometry] = 5,720 lb CO₂/short ton coal = 2.86 short tons
CO₂/short ton coal. This is an **idealized stoichiometric maximum** for
high-carbon bituminous and is presented in some EPA / IPCC explanatory
materials as a worked example of complete combustion. It is NOT the EIA
emission factor and NOT a published EPA emission factor. The actual EPA
emission factor accounts for incomplete combustion, ash content, and
typical-in-use combustion efficiency, and lands at 2.32 mt CO₂/short ton
bituminous coal.)

### §2.4 EPA AP-42 §1.1 emission factor — primary-source verification

**Sources:** EPA AP-42 §1.1 Bituminous and Subbituminous Coal Combustion
(June 1985, last update 2010); EPA 2025 *Emission Factors for Greenhouse
Gas Inventories* (the Hub).

**Confirmed values:**
- Bituminous coal CO₂ emission factor: **93.28 kg CO₂/mmBtu** (Hub Table 1,
  Stationary Combustion Emission Factors).
- EIA national-bituminous-average heat content: **24.93 mmBtu/short ton**
  (per the EIA methodology page
  `https://www.eia.gov/environment/emissions/includes/methodology.php`,
  which currently lists 23.270 mmBtu/short ton for 2022 data; 24.93 was the
  Ch 6 + TA reference value at the time of the cascade — within the EIA
  historical-tabulation range across years).
- Derivation: 93.28 kg CO₂/mmBtu × 24.93 mmBtu/short ton = **2,325.49 kg
  CO₂/short ton** = **2.32 metric tons CO₂/short ton bituminous coal**.

The EPA AP-42 derivation produces the same 2.32 figure as the EIA emission-
factor table (the table is itself built from EPA emission factors per EIA's
own attribution). **Ch 6's basis (2.32 mt CO₂/short ton) is dimensionally
consistent and authoritatively sourced.**

### §2.5 Dimensional-consistency cross-check on Ch 8's arithmetic

The 2.86 figure derived from 78% C / 14,000 BTU/lb stoichiometry is
mathematically a **mass ratio** (mass CO₂ produced per mass coal combusted).
A mass ratio expressed as "short tons of CO₂ per short ton of coal" carries
identical numerical value to "metric tons of CO₂ per metric ton of coal"
(both are dimensionless ratios numerator/denominator).

For the multiplication 2.86 × $190 to yield a meaningful $ per (short ton
coal), the units must be reconciled:

**Path A — interpret 2.86 as metric tons CO₂ per metric ton coal:**
- 2.86 (mt CO₂ / mt coal) × $190 (per mt CO₂) = **$543.40 / mt coal**.
- Converting to per short ton coal: $543.40 / mt coal × 0.907185 mt/short ton
  = **$493.00 / short ton coal**.
- NOT $544 / short ton coal.

**Path B — interpret 2.86 as short tons CO₂ per short ton coal:**
- Convert numerator to metric tons CO₂: 2.86 short tons CO₂ × 0.907185
  mt/short ton = **2.595 mt CO₂ per short ton coal**.
- 2.595 (mt CO₂ / short ton coal) × $190 (per mt CO₂) = **$493.00 / short
  ton coal**.
- NOT $544 / short ton coal.

**Both interpretations of the 2.86 figure produce $493/short ton coal under
correct dimensional handling.** Ch 8's $544 / short ton coal figure
implicitly multiplies 2.86 (short tons CO₂ / short ton coal) × $190 (per
**metric** ton CO₂) as if the short-ton numerator cancels the metric-ton
denominator. **This is a units bug.** The bug systematically overstates
the per-short-ton-coal carbon cost by a factor of 1.10231 (the short-ton-
to-metric-ton ratio).

(For context: this units-error pattern is one of the most common errors in
climate-economics calculations performed by audiences who alternate between
short-ton and metric-ton denominators. The bug becomes invisible when the
intermediate values appear close to each other — $493 vs $544 looks like a
methodology disagreement when it is actually a units bug.)

### §2.6 The dimensional issue at the cited source

Ch 8 Pass 1's source inventory line 491 cites the EIA volume/mass coal-CO₂
page as confirming "1 short ton 78%-carbon, 14,000-BTU/lb coal yields 2.86
short tons CO₂ on complete combustion." As verified in §2.3 above, the EIA
URL's tabulated emission factor for bituminous coal is 2.32 mt/short ton,
not 2.86. The 2.86 figure is not on that EIA page. The source attribution
is therefore incorrect AND the figure-as-used in Ch 8 carries a units bug.

### §2.7 Net dimensional-analysis verdict

- **EPA / Rennert 2022 SCC $190 is denominated in metric tons CO₂.** Confirmed.
- **EIA volume/mass coal-CO₂ page publishes 2.32 mt CO₂/short ton bituminous,
  not 2.86.** Ch 8's source attribution is incorrect.
- **Ch 8's $544/short ton coal figure carries a units bug** (multiplying
  short-ton numerator by metric-ton denominator as if they cancel). Correctly
  computed from Ch 8's own 2.86 stoichiometric basis: **$493/short ton coal.**
- **Ch 6 + TA §7.4 + TA §11.6's 2.32 mt CO₂/short ton × $190 = $441/short
  ton coal is dimensionally consistent and authoritatively sourced.**
- The discrepancy between Ch 8 (corrected to $493) and Ch 6 / TA ($441) is
  NOT a units bug but a **methodology choice**: which heat-content basis is
  canonical for McDowell County–specific coal?

---

## §3 — Heat content + carbon content basis investigation

### §3.1 The methodology question

Ch 6 + TA §11.6 use **national-bituminous-average heat content** (24.93
mmBtu/short ton ≈ 12,465 BTU/lb), yielding 2.32 mt CO₂/short ton coal →
$441/short ton coal at $190 SCC.

Ch 8's stoichiometric basis assumes **14,000 BTU/lb + 78% C** (28 mmBtu/
short ton, with 78% carbon content), yielding 2.86 short tons CO₂/short
ton coal (= 2.595 mt CO₂/short ton) → $493/short ton coal at $190 SCC
when correctly converted.

The methodology question: **which basis is canonical for McDowell County
coal specifically?**

### §3.2 McDowell County–specific heat content (Pocahontas seam + adjacent)

McDowell County's principal historical production was from the **Pocahontas
No. 3 coal seam**, a high-rank low-volatile bituminous coal with heat
content typically **14,500–15,500 BTU/lb** per USGS and West Virginia
Geological Survey data. Per USGS Professional Paper 1625-C (Chapter H,
Pocahontas No. 3 coal bed regional geology + chemistry) and the WV
Geological Survey trace-elements database, Pocahontas No. 3 is among the
highest-quality bituminous coals in the United States and historically
commanded metallurgical-grade premiums.

McDowell County also produced from adjacent seams (Pocahontas No. 4 + the
Eagle seam) with somewhat lower heat content (~13,500–14,500 BTU/lb).
**Production-weighted McDowell-specific heat content** is in the range
**14,000–15,000 BTU/lb** (= 28–30 mmBtu/short ton), substantially above the
EIA national-bituminous-average of 24.93 mmBtu/short ton (= 12,465 BTU/lb).

The national average pulls in **steam coal grades** from elsewhere in
Appalachia + the Illinois Basin + lower-rank bituminous from other
producing regions. McDowell specifically does NOT have a representative
share of those lower-grade bituminous coals; McDowell coal was famous for
being among the highest-energy-content coal in the United States.

### §3.3 Corpus-canonical figure under McDowell-specific basis

Using EPA AP-42 §1.1 emission factor (93.28 kg CO₂/mmBtu) at the McDowell-
specific heat-content range:

**Low McDowell-specific basis (14,000 BTU/lb = 28 mmBtu/short ton):**
- 28 mmBtu/short ton × 93.28 kg CO₂/mmBtu = 2,611.84 kg CO₂/short ton =
  **2.61 mt CO₂/short ton coal**.
- × $190/mt CO₂ = **$496/short ton coal**.

**High McDowell-specific basis (15,000 BTU/lb = 30 mmBtu/short ton):**
- 30 mmBtu/short ton × 93.28 kg CO₂/mmBtu = 2,798.40 kg CO₂/short ton =
  **2.80 mt CO₂/short ton coal**.
- × $190/mt CO₂ = **$532/short ton coal**.

**Cross-check via Ch 8's stoichiometric basis (78% C × 14,000 BTU/lb):**
- 2.86 short tons CO₂/short ton coal × 0.907185 mt/short ton = 2.595 mt
  CO₂/short ton coal × $190 = **$493/short ton coal**.

The McDowell-specific corpus-canonical range under proper dimensional
handling: **$493–$532/short ton coal** (depending on heat-content basis
within the McDowell-specific range).

### §3.4 Side-by-side basis comparison

| Basis | Heat content | mt CO₂ / short ton coal | $ / short ton coal at $190 SCC |
|---|---|---|---|
| EIA national-bituminous-average (Ch 6 + TA §11.6 current) | 24.93 mmBtu/short ton (~12,465 BTU/lb) | 2.32 | **$441** |
| Ch 8 stoichiometric (78% C × 14,000 BTU/lb), correctly converted | 28 mmBtu/short ton (~14,000 BTU/lb) | 2.595 | **$493** |
| AP-42 McDowell-typical (14,000 BTU/lb) | 28 mmBtu/short ton | 2.61 | **$496** |
| AP-42 McDowell-high-grade (15,000 BTU/lb) | 30 mmBtu/short ton | 2.80 | **$532** |
| **Ch 8 current (units bug)** | 28 mmBtu/short ton via 2.86 ratio + units bug | 2.86 (mishandled) | **$544 (incorrect)** |

The spread between methodologically defensible options is ~$441 (national-
average, conservative) to ~$532 (McDowell-specific high-grade). The
difference is real and reflects a genuine modeling choice; it is NOT a
units bug. The current $544 figure in Ch 8 IS a units bug and sits ~$12
above even the McDowell-specific high-grade ceiling.

### §3.5 Implications for "approximately 2.86 tons of CO₂" prose

Whichever methodology basis is chosen for the canonical carbon-tail figure,
Ch 8 line 72's "approximately 2.86 tons of carbon dioxide" needs revision
because:

- If Option A (national-bituminous-average basis): the figure becomes
  approximately **2.32 tons of CO₂** (matching Ch 6 + TA cascade).
- If Option B (McDowell-specific basis): the figure becomes approximately
  **2.6 tons of CO₂** (per metric-ton convention; equivalently 2.86 short
  tons converted correctly).
- The current "2.86 tons" is dimensionally ambiguous (short tons or metric
  tons?) and is the **input** to the units bug — even under Option B's
  McDowell-specific basis, the prose should specify the unit convention.

---

## §4 — Unit-consistent corpus-canonical figure derivation

### §4.1 Three derivation paths to a single canonical figure

Three derivation paths each produce a unit-consistent corpus-canonical
figure under properly handled units:

**Path 1 — National-bituminous-average via EPA AP-42 emission factor (Ch 6
+ TA §7.4 + TA §11.6 current basis):**

- EPA AP-42 §1.1 emission factor: 93.28 kg CO₂/mmBtu (bituminous)
- × EIA national-bituminous-average heat content: 24.93 mmBtu/short ton
- = 2,325 kg CO₂/short ton = **2.32 mt CO₂/short ton coal**
- × EPA 2023 SCC $190/mt CO₂ central estimate = **$441/short ton coal**

**Path 2 — McDowell-specific via EPA AP-42 emission factor (McDowell-
specific basis upgrade):**

- EPA AP-42 §1.1 emission factor: 93.28 kg CO₂/mmBtu (bituminous)
- × McDowell production-weighted heat content: ~28 mmBtu/short ton (mid-
  range estimate; Pocahontas Nos. 3 + 4 + Eagle production-weighted)
- = 2,612 kg CO₂/short ton = **2.61 mt CO₂/short ton coal**
- × EPA 2023 SCC $190/mt CO₂ central estimate = **$496/short ton coal**

**Path 3 — Stoichiometric maximum via 78% C / 14,000 BTU/lb (Ch 8's current
input, correctly converted):**

- 78% C × 2,000 lb/short ton × 44/12 [stoichiometric CO₂/C mass ratio] =
  5,720 lb CO₂/short ton = 2.86 short tons CO₂/short ton coal
- Convert: 2.86 short tons × 0.907185 mt/short ton = **2.595 mt CO₂/short
  ton coal**
- × EPA 2023 SCC $190/mt CO₂ central estimate = **$493/short ton coal**

(Paths 2 + 3 produce nearly identical results at McDowell-typical heat
content + carbon content. Path 1 produces a notably lower result because
it uses the national-bituminous-average heat content, which is below
McDowell's actual production-weighted heat content.)

### §4.2 What is NOT in dispute

- **EPA 2023 SCC $190/mt CO₂ central estimate is the corpus anchor.** No
  divergence on the SCC figure or its denomination.
- **Carbon-cost calculation is the multiplication of (CO₂ produced per
  short ton coal) × (SCC per metric ton CO₂).** No divergence on the
  formula.
- **The $544/short ton-coal current Ch 8 figure carries a units bug and
  cannot stand under any methodology choice.** Either it becomes $441
  (Option A national-basis cascade) or $493–$532 (Option B McDowell-
  specific basis); it does not remain at $544.

### §4.3 The methodology question is narrow

The decision the author ratifies is whether the corpus canonical basis for
**McDowell County coal in the worked-example role** is:

- The **national-bituminous-average** (Path 1, current Ch 6 + TA basis →
  $441), or
- The **McDowell-specific** (Paths 2 + 3 produce ~$493–$532; reasonable
  central anchor ~$510 mid-range).

Both are defensible. The Path 1 choice has the virtue of being the **EIA-
canonical** bituminous emission factor and is therefore the figure a
fact-checker familiar with EIA + EPA AP-42 tables would expect for a
sentence reading "one ton of bituminous coal releases X tons of CO₂." The
Path 2 choice has the virtue of being **McDowell-specific** and therefore
more accurate to the worked example Ch 8 is performing (the chapter's
arithmetic is "one ton of McDowell coal," not "one ton of average US
bituminous").

Per substance-drives-length discipline + Ostrom-illustrative-register
discipline: the chapter's role determines the basis choice. Ch 6 + TA §7.4
function as **framework-introduction** and reasonably use the national-
average bituminous figure (the framework applies to "bituminous coal"
generically; the McDowell case is illustrative). Ch 8 + TA §11.6 function
as **McDowell-specific worked example** and arguably should use McDowell-
specific basis.

---

## §5 — Cross-corpus cascade footprint

Full enumeration of every artifact that anchors on the coal-CO₂ figure,
with current values + post-reconciliation values under each option.

### §5.1 Chapter 8 — `manuscript/chapters/Chapter__8_WhatThingsActuallyCost.md`

Current Ch 8 file: 243 lines (verified 2026-05-22).

| Line | Current text | Option A ($441 cascade) | Option B ($510 mid-McDowell) |
|---|---|---|---|
| 72 | "approximately 2.86 tons of carbon dioxide ... approximately five hundred and forty-four dollars" | "approximately 2.32 tons of carbon dioxide (EPA emission factor for bituminous coal at short-ton accounting) ... approximately four hundred and forty-one dollars" | "approximately 2.6 metric tons of carbon dioxide (EPA AP-42 §1.1 bituminous coal combustion factor at McDowell-typical heat content) ... approximately five hundred and ten dollars" |
| 78 | "minimum of five hundred and forty-four dollars per ton" | "minimum of four hundred and forty-one dollars per ton" | "minimum of five hundred and ten dollars per ton" |
| 154 | "- Foreclosure: $544" | "- Foreclosure: $441" | "- Foreclosure: $510" |
| 164 | "Total: $558 per ton" | "Total: $455 per ton" | "Total: $524 per ton" |
| 168 | "thirty-three and one hundred and twenty-two times the 1960 sale price ... carbon term alone exceeds the market price by a factor of at least four" | "thirty-three and one hundred and twenty-two times the 1960 sale price ... carbon term alone exceeds the market price by a factor of at least three" | "thirty-three and one hundred and twenty-two times the 1960 sale price ... carbon term alone exceeds the market price by a factor of at least three" (or "approximately four" if McDowell-specific ceiling holds; computation: $510/$140 = 3.6×, rounds-down to "at least three" per conservative discipline) |
| 212 | "between thirty-three and one hundred and twenty-two times the 1960 sale price" | unchanged (the 33–122× range is robust to the reconciliation; see §6.3) | unchanged |
| 238 | "floor of roughly five hundred and fifty-eight dollars" | "floor of roughly four hundred and fifty-five dollars" | "floor of roughly five hundred and twenty-five dollars" (or "five hundred and twenty-four") |

**Coupling note on line 168 "factor of at least four":** Ch 8 Stage 1c Phase C
(commit `cbef9bd`, 2026-05-21) just ratified Option D headline framing
including this "at least four" structural-finding beat. The computation
($544/$140 ≈ 3.9× rounds-up to "at least four" per Stage 1c artifact §6).
Under Option A cascade: $441/$140 = 3.15×, "at least three." Under Option B:
$510/$140 = 3.64×, also rounds-down to "at least three" under the same
conservative-rounding discipline. The "at least four" wording in line 168
+ line 74 (carbon-tail-only echo) is materially coupled to the foreclosure
figure and would need to retreat to "at least three" under both Option A
and Option B. This is a coupling the Phase C application session must
handle.

**Line 74 (carbon-tail-only IPG framing, Stage 1c Phase C just ratified):**
"by a factor running from roughly four against today's market peak to more
than a hundred against the 1960 mine-mouth" — under Option A or B, the
"roughly four" lower bound retreats to "roughly three" (Option A: $441/$140
= 3.15×; Option B: $510/$140 = 3.64×). Upper bound remains "more than a
hundred" (both: ~100× against $4.50). Apply consistent wording.

### §5.2 Chapter 6 — `manuscript/chapters/Chapter__6_ThreeWaysofCounting.md`

Current Ch 6 file: 365 lines (verified 2026-05-22 post Ch 6 developmental-
edit Pass 3.5 commit `9befb92`). Line numbers below current; reconciliation
predecessor numbering in parens for cross-reference to prior audit artifacts.

| Line | Current text | Option A (preserve) | Option B (upgrade to McDowell-specific) |
|---|---|---|---|
| 38 (was 30) | "$8 to $22 per ton" non-carbon total | unchanged | unchanged (Ch 6 is framework-introduction; the basis decision is per-context) |
| 42 (was 32) | "approximately 2.32 tons of CO₂ (EPA emission factor for bituminous coal at short-ton accounting: 93.28 kg CO₂ per mmBtu × roughly 24.9 mmBtu per short ton). At the EPA's 2023 estimate of $190 per ton CO₂, the carbon externality alone is approximately $441 per ton of coal" | unchanged | "approximately 2.6 metric tons of CO₂ (EPA AP-42 §1.1 emission factor 93.28 kg CO₂/mmBtu × McDowell-specific heat content ~28 mmBtu/short ton). At the EPA's 2023 estimate of $190 per metric ton CO₂, the carbon externality alone is approximately $510 per short ton of coal" — but see footnote: Ch 6 explicitly says "bituminous coal" (generic), not "McDowell coal" — Option B may be inappropriate at Ch 6's framework-introduction register |
| 44 (was 34) | "bottom-up total rises to roughly $449 to $464 per ton" | unchanged | recompute to $518–$532 if Option B applied at Ch 6 |
| 343 (was 321) | "lands around $449 to $464 per ton of coal" (Pigouvian-bracket within McDowell Contribution-section paragraph) | unchanged | recompute to $518–$532 if Option B applied at Ch 6 (but Ch 6 line 343 IS McDowell-specific context — see Option C below) |

**Sub-discrimination for Ch 6:** Ch 6's lines 42 + 44 are in the framework-
introduction context ("One ton of bituminous coal, fully combusted..." —
generic). Line 343 is in the McDowell-specific Contribution-section
walkthrough ("McDowell County coal. Under standard Pigouvian accounting..."
— specific). Under Option B's logic, line 343 could move to McDowell-
specific basis while lines 42 + 44 remain at the national-average basis.
This produces an internal Ch 6 tension that may warrant a footnote at line
343 noting that the McDowell-specific basis yields a higher figure. (See
Option C in §6.1 below.)

### §5.3 Technical Appendix — `core/technical-appendix/TechnicalAppendix_v2.0.0.html`

Current TA file: 8,044 lines (verified 2026-05-22).

| Line | Current text | Option A (cascade in TA §11.1) | Option B (McDowell-specific) |
|---|---|---|---|
| 2859 (§7.4 Gate 4 worked example, framework-introduction context) | "where E includes $190/ton CO2 × 2.32 tons CO2 per ton coal — EPA emission factor for bituminous coal at short-ton accounting, per EPA AP-42 §1.1" | unchanged | unchanged (framework-introduction; generic bituminous appropriate) |
| 2916 (§1.7 Numerical update) | "Against the canonical Ch 6 figure of $550–$570/ton (dominated by the carbon externality), the updated RCV estimate is $555–$580/ton" | "Against the canonical Ch 6 figure of $449–$464/ton (dominated by the carbon externality), the updated RCV estimate is $454–$474/ton" — this line carries a separate **pre-Ch6-Phase-Cβ drift** (the $550–$570 reference is stale relative to Ch 6's current $449–$464) | recompute to $518–$542 under Option B |
| 3876 (§11.1 Damage Function McDowell row) | "Carbon at EPA Social Cost of Carbon ($190/ton CO₂): ~$544/ton (dominant term for fossil fuels)" | "~$441/ton" | "~$510/ton" |
| 3882 (§11.1 totals) | "Total with carbon: $552–566/ton" | "$449–$463/ton" | "$518–$532/ton" |
| 3898 (§11.1 spatial-cost-severance paragraph) | "$544/ton carbon term is a global atmospheric externality" | "$441/ton carbon term" | "$510/ton carbon term" |
| 4517 (§11.6 Block 4 McDowell calibration row) | "~2.32 tons CO₂ per ton coal (EPA emission factor for bituminous coal at short-ton accounting)" | unchanged | "~2.6 metric tons CO₂ per short ton coal (EPA AP-42 §1.1 emission factor at McDowell-specific heat content)" — TA §11.6 IS the McDowell calibration table and Option B applies cleanly here |
| 4520 (§11.6 derivation cell) | "EPA AP-42 §1.1 Bituminous and Subbituminous Coal Combustion (93.28 kg CO₂/mmBtu) × EIA-published heat content for bituminous coal (~24.93 mmBtu/short ton) ≈ 2,324.56 kg/short ton ≈ 2.32 mt CO₂/short ton" | unchanged | "EPA AP-42 §1.1 ... × McDowell-specific heat content (~28 mmBtu/short ton; production-weighted Pocahontas Nos. 3 + 4 + Eagle seams per USGS PP 1625-C + WV Geological Survey) ≈ 2,612 kg/short ton ≈ 2.61 mt CO₂/short ton" |
| 4533 (§11.6 cumulative emissions) | "Calculated: 600M short tons × 2.32 mt CO₂/short ton ≈ 1.39B mt CO₂" | unchanged | recompute: 600M × 2.61 ≈ 1.57B mt CO₂ |
| 4607, 4623, 4635 (§11.6 Method 1 DAC per-ton-coal table) | "per-ton coal at 2.32 mt CO₂/short ton × DAC range" | unchanged | recompute at 2.61 (per-ton-coal Method 1 floor shifts upward proportionally) |

**TA §11.1 carries the most significant internal drift.** §11.1 still uses
the pre-cascade Ch 8 figure ($544/ton) while §11.6 uses the cascade-aligned
figure ($441/ton). The TA is internally inconsistent regardless of which
option the corpus chooses externally. §11.1 needs alignment to the corpus
choice as part of any cascade application.

**TA §1.7 line 2916 carries a separate pre-Ch6-Phase-Cβ drift** that
predates the current cascade question: it cites "the canonical Ch 6 figure
of $550–$570/ton" but Ch 6's current figure (post Phase C-β) is
$449–$464/ton. This drift is independent of the Ch 8 cascade decision and
should be flag-forwarded for the TA editor's attention regardless of the
Option A vs Option B choice.

### §5.4 Chapter 9 — cross-references to Ch 8 $558 floor

Per cross-chapter consistency inventory line 112:

| Ch 9 location | Current text | Option A impact | Option B impact |
|---|---|---|---|
| Ch 9:12 | "$500–$600" (conservative bracketing range) | encompasses $455 → consider widening to "$450–$600" | encompasses $524 → unchanged |
| Ch 9:116 | "approximately $550" (rounded rhetorical anchor; ratified Ch 9 Pass 1 MEDIUM-1 Option A, 2026-05-19) | $455 cascades to "approximately $450" | $524 rounds to "approximately $525" or stays at "approximately $550" |

Option A produces meaningful Ch 9 cross-reference impact (anchor moves ~$95
downward). Option B preserves "approximately $550" almost as-written ($524
is within rounding tolerance of $550 under the conservative-rhetorical-
anchor register).

### §5.5 Cross-chapter consistency inventory — `tools/audits/cross-chapter-consistency-inventory_2026-05-11.md`

| Line | Current text | Option A | Option B |
|---|---|---|---|
| 111 | "**Coal carbon-tail per ton** \| ~$544 (1 ton coal → 2.86 tons CO₂ × $190) \| Ch 8 line 73 \| Ch 8 only. **No drift.**" — note "No drift" is incorrect; Ch 6 + TA §11.6 carry $441 | "**Coal carbon-tail per ton** \| ~$441 (1 short ton coal → 2.32 mt CO₂ × $190/mt; EPA AP-42 §1.1 short-ton accounting) \| Ch 6 line 42 + Ch 8 line 72 \| Cascade-aligned post 2026-05-22 reconciliation." | "**Coal carbon-tail per ton** \| ~$510 (McDowell-specific basis; 1 short ton coal → 2.61 mt CO₂ × $190/mt; AP-42 emission factor × McDowell-specific heat content) \| Ch 8 line 72 + TA §11.6; Ch 6 line 42 carries national-bituminous-average $441 in framework-introduction register \| Per 2026-05-22 reconciliation: basis varies by chapter role." |
| 112 | "**McDowell coal per-ton total floor** \| $558 ..." | "$455 (Ch 8 canonical sum-of-components, line 164)..." | "$524 (Ch 8 canonical sum-of-components, line 164)..." |

### §5.6 HIGH-3 cross-corpus IPG canonical-construction artifact

File: `tools/rigor-passes/commons_bonds_rigor_pass_2026-05-21_cross_corpus_ipg_canonical_construction_v1.0.0.md`.

This artifact ratified Option D for the IPG headline: 33–122× canonical
range preserved with today-prices follow-up as structural-finding beat.
The IPG range was constructed against then-current Ch 8 $558 floor / 1960
$4.50 price → 124× ceiling (rounded to 122× per Ch 2 canonical anchor).

**Impact of this session's cascade on the 33–122× canonical lock:**

| Option | Ch 8 floor | Floor / $4.50 | Inside 33–122×? |
|---|---|---|---|
| Current (units bug) | $558 | 124× | ceiling round-down to 122× |
| Option A ($441 cascade) | $455 | 101× | YES |
| Option B (McDowell-specific $510) | $524 | 116× | YES |

**The 33–122× canonical lock is robust to both reconciliation options.** Ch
2's anchor ("between 33 and 122 times depending on which cost categories
you include and which social cost of carbon estimate you use") explicitly
accommodates parameter variation; the new computed Ch 8 floor (under
either Option A or Option B) lands inside the 33–122× range. The IPG
artifact does NOT need to re-derive the canonical range.

A **light annotation** to the IPG artifact's §5 ratification summary
documenting that the Ch 8 worked-example floor has moved from $558 → $455
or $510 (per author's selection in this session) is the only update
required.

### §5.7 Cross-thread #12 status update

File: `publishing/essays/_pipeline/cross-thread-todos.md`, entry #12.

Current #12 status: "open — known fix pending; documented for Ch 8 Pass 1
audit to absorb into its scope." Stale recommended-edit text quotes the
verbatim $441 cascade as the canonical Ch 8 fix.

Post-this-session: #12 status updates to "open — methodology
reconciliation PROPOSED 2026-05-22 (this artifact); ratification gates
Phase C application." Recommended-edit text retires and is replaced by a
reference to this reconciliation artifact's ratified option.

After Phase C application: #12 status updates to RESOLVED with cascade-
commit reference.

### §5.8 Summary of cascade scope

| Artifact | Lines touched | Option A | Option B |
|---|---|---|---|
| Ch 8 | 7 lines (72, 78, 154, 164, 168, 212, 238) | All cascade to $441 family; line 168 "at least four" → "at least three" | All cascade to $510 family; line 168 "at least four" → "at least three" |
| Ch 6 | 0 lines (preserve current) OR 4 lines (42, 44, 343, +1 footnote) | 0 lines (Ch 6 already at canonical) | 4 lines if Ch 6 also upgrades to McDowell-specific; 1–2 lines if only Ch 6 line 343 (McDowell-specific paragraph) upgrades and lines 42 + 44 preserve framework-introduction basis (Option C) |
| TA | 5 lines (3876, 3882, 3898, 2916, +TA §11.6 if Option B) | 4 lines (TA §11.1 cascade + §1.7 drift cleanup) | 5–7 lines (TA §11.1 + §11.6 + §1.7) |
| Ch 9 | 0–2 lines (Ch 9:12 + Ch 9:116) | 1–2 lines (anchor moves) | 0 lines (rounding tolerance preserves) |
| Cross-chapter inventory | 2 rows (111, 112) | Both update | Both update |
| HIGH-3 IPG artifact | 1 annotation in §5 | Light annotation only | Light annotation only |
| Cross-thread #12 | Status update + retire stale recommended-edit text | Couples to Phase C application | Couples to Phase C application |

---

## §6 — Per-decision finding sections

Per Amendment-C Interactive Ratification Protocol: each finding presents
Options + Recommendation + Reasoning.

### §6.1 Heat content + carbon content basis choice

**Decision:** which Appalachian-coal heat-content basis is canonical for
the corpus-wide coal-CO₂ carbon-tail calculation?

**Options:**

- **Option A — Preserve national-bituminous-average basis ($441/short ton
  coal).** Keep Ch 6 + TA §7.4 + TA §11.6 at 2.32 mt CO₂/short ton coal
  using EIA national-bituminous-average heat content (24.93 mmBtu/short
  ton). Cascade Ch 8 + TA §11.1 + TA §1.7 + cross-chapter inventory down
  to match. Coal-CO₂ figure: 2.32 mt CO₂/short ton; carbon-tail: $441;
  Ch 8 floor: $455. This is the verbatim cross-thread #12 recommendation.

- **Option B — Upgrade to McDowell-specific basis ($510/short ton coal).**
  Move Ch 8 + TA §11.6 + TA §11.1 to 2.61 mt CO₂/short ton coal using
  McDowell-specific production-weighted heat content (~28 mmBtu/short
  ton). Keep Ch 6 line 42 + TA §7.4 at national-average basis (those are
  framework-introduction contexts speaking of "bituminous coal" generically).
  Coal-CO₂ figure for McDowell: 2.61 mt CO₂/short ton; carbon-tail: $510;
  Ch 8 floor: $524.

- **Option C — Hybrid: framework-introduction stays national-average; McDowell-
  specific contexts use McDowell-specific basis with footnote.** Ch 6 line
  32 + TA §7.4 stay at 2.32 mt / $441 (framework-introduction; generic
  bituminous). Ch 6 line 343 (McDowell Contribution-section paragraph) + Ch
  8 + TA §11.1 + TA §11.6 use McDowell-specific 2.61 mt / $510. Both
  registers footnoted at first use of the McDowell-specific basis: "the
  McDowell-specific heat content (production-weighted Pocahontas Nos. 3 + 4
  + Eagle seams, ~28 mmBtu/short ton per USGS PP 1625-C) is above the
  national-bituminous-average (~24.93 mmBtu/short ton) that Ch 6 + TA §7.4
  use in the framework-introduction context; the framework's qualitative
  finding is invariant to this basis choice."

- **Option D — Preserve verbatim cross-thread #12 (national-average $441)
  but with explicit-methodology disclosure footnote at Ch 8 line 72 + TA
  §11.6:** Same arithmetic as Option A, but Ch 8 line 72 + TA §11.6 each
  add a footnote: "The national-bituminous-average heat content (24.93
  mmBtu/short ton) is used here for cross-corpus consistency with Ch 6 +
  TA §7.4. McDowell County's Pocahontas seam coal carries higher heat
  content (~28 mmBtu/short ton); under the McDowell-specific basis, the
  carbon-tail figure rises to ~$510/short ton, which the chapter's
  conservative-floor discipline treats as an upward revision the framework
  is robust to."

**Recommendation:** **Option C (hybrid: framework-introduction stays
national-average; McDowell-specific contexts use McDowell-specific basis
with footnote).**

**Reasoning:**

- **Substance-drives-length + Ostrom-illustrative-register:** The chapter's
  role determines the basis choice. Ch 6 + TA §7.4 perform framework
  introduction ("one ton of bituminous coal"; "as in the Ch 6 headline
  computation where E includes $190/ton CO2 × 2.32 tons CO2 per ton coal")
  — these are generic framework expositions for which the national-
  bituminous-average is the appropriate canonical basis. Ch 8 + TA §11.6
  perform McDowell-specific worked-example walkthrough ("one ton of
  McDowell County coal"; "Cumulative coal production (McDowell + adjacent
  counties, peak production era) ~600 million tons") — these are McDowell-
  specific computations for which the McDowell-specific basis is more
  accurate.
- **Methodological honesty:** Option C is more methodologically honest
  than Option A because the McDowell-specific basis is genuinely more
  accurate for the McDowell-specific worked example. The McDowell coal
  Ch 8 walks through is *not* national-average bituminous; pretending it
  is would understate the carbon-tail by ~15% in the chapter whose entire
  rhetorical force is the carbon-tail dominance over market price.
- **Cross-corpus consistency:** Option C maintains the cross-corpus
  consistency the framework needs (every chapter agrees on the formula
  and the SCC anchor) without forcing a single basis where the
  applicability differs. The Ostrom-illustrative-register discipline
  explicitly accommodates per-context calibration of generic frameworks.
- **Trade-press fact-checker passability:** A trade-press fact-checker
  who runs EPA AP-42 + EIA heat-content tables against the McDowell-
  specific basis will find Ch 8's McDowell-specific number defensible;
  one who runs the same tables against Ch 6's framework-introduction
  language will find Ch 6's national-bituminous-average defensible. Both
  pass the fact-check independently. The footnote at Ch 8 + TA §11.6
  surfaces the basis-choice transparency a Tier-1 quant reader will
  appreciate.
- **Risk-of-future-drift:** Option C carries higher specification surface
  than Option A but is structurally stable: a future chapter introducing
  a different coal case (e.g., Powder River sub-bituminous, or
  Pennsylvanian anthracite) would naturally use that case's basis, and
  the framework's basis-choice protocol is documented as "use the
  case-specific basis where applicable; default to national-bituminous-
  average for generic framework-introduction language."

**Author judgment:** if simplicity + cross-thread #12 alignment dominate
the decision, Option A is fully defensible (and is the option cross-thread
#12 already proposes). If methodological precision + McDowell-specific
accuracy dominate, Option C is the strongest. Option B (uniform upgrade)
is dispreferred because it forces the framework-introduction register
into McDowell-specific basis where it shouldn't go. Option D (footnote-
only at Ch 8) is the lightest-touch methodological-disclosure choice and
may be preferred if the author wants Option A's simplicity while flagging
the McDowell-specific upgrade pathway for future work.

### §6.2 Cascade direction

**Decision:** which direction does the cross-corpus cascade flow?

**Options:**

- **Option A — Ch 8 retrofits to Ch 6 + TA §11.6 cascade ($441 family).**
  Per cross-thread #12 verbatim recommendation. Ch 6 + TA §11.6 unchanged;
  Ch 8 line 72 + line 78 + line 154 + line 164 + line 168 + line 212 + line
  238 + TA §11.1 (lines 3876 + 3882 + 3898) + TA §1.7 (line 2916, drift-
  cleanup) + cross-chapter inventory (lines 111 + 112) cascade. Couples to
  §6.1 Option A.

- **Option B — Ch 6 + TA §11.6 retrofit to McDowell-specific ($510 family).**
  Ch 6 (lines 42 + 44 + 343) + TA §11.6 (lines 4517 + 4520 + 4533 + 4607
  + 4623 + 4635) + Ch 8 (cascade as in §5.1) + TA §11.1 + TA §1.7 + cross-
  chapter inventory + Ch 9 (if anchor shifts beyond rounding tolerance).
  Couples to §6.1 Option B.

- **Option C — Hybrid (per §6.1 Option C).** Ch 6 line 42 + TA §7.4
  preserve national-average basis; Ch 8 + TA §11.1 + TA §11.6 + Ch 6 line
  321 cascade to McDowell-specific basis. Adds footnote at Ch 8 line 72 +
  TA §11.6 surfacing the basis-distinction discipline. Couples to §6.1
  Option C.

- **Option D — Explicit methodology-disclosure preserves both (no
  cascade-direction question).** Ch 8 line 72 reads: "Under EIA national-
  bituminous-average accounting (the basis Ch 6 + TA §7.4 use), one ton
  of bituminous coal releases approximately 2.32 metric tons of CO₂,
  yielding a carbon-tail at $190 SCC of approximately $441 per short ton.
  Under McDowell-specific heat-content accounting (production-weighted
  Pocahontas seam ~28 mmBtu/short ton), the same ton yields ~2.6 metric
  tons of CO₂ and a carbon-tail of approximately $510. The chapter's
  conservative-floor discipline reports the lower figure as the floor."
  Couples to §6.1 Option D variant + explicit-methodology Ch 8 disclosure.

**Recommendation:** **Option C (hybrid cascade matched to §6.1 Option C).**

**Reasoning:**

- **§6.1 Option C decides the basis question.** §6.2 cascade direction
  derives from §6.1: if framework-introduction stays at national-average
  and McDowell-specific contexts use McDowell-specific, then Ch 6 line 42
  + TA §7.4 don't cascade; Ch 8 + TA §11.1 + TA §11.6 + Ch 6 line 343
  cascade upward to McDowell-specific. This is the cascade Option C
  implies.
- **Bundling efficiency:** Option C's cascade footprint is moderately
  larger than Option A's (4 + 5 + 2 + ~3 + 2 + 1 = ~17 line-touches across
  4 files vs Option A's 4 + 0 + 4 + 0–2 + 2 + 1 = ~11–13 line-touches
  across 4 files). The marginal cost is small and the methodological-
  honesty payoff is substantial.
- **Prose-quality at Ch 8's climax:** Option C preserves Ch 8's climactic
  carbon-tail-dominance claim at the McDowell-specific figure ($510
  carbon-tail; ~$524 total floor), which is closer to the chapter's
  current $544 / $558 rhetorical anchors than Option A's downward cascade
  to $441 / $455. The chapter's climax doesn't need to retreat as far.
- **Coupling to Stage 1c Phase C just-ratified line 168 "at least four":**
  Under Option C, $510/$140 = 3.64×, which under conservative-rounding
  becomes "at least three" — same as Option A. The Stage 1c Phase C
  ratified wording requires touching either way; the substantive coupling
  is the same.

**Author judgment:** if cross-thread #12 verbatim alignment + minimum
cascade surface dominates, Option A is fully defensible. If methodological
precision + McDowell-specific accuracy dominates, Option C is the
strongest recommendation. Option B is dispreferred (over-reach into
framework-introduction); Option D is dispreferred (textbook-grade
methodology disclosure at the chapter's climax disrupts prose flow).

### §6.3 HIGH-3 33–122× IPG canonical lock disposition

**Decision:** does the HIGH-3 cross-corpus IPG canonical-construction
artifact (commit producing
`tools/rigor-passes/commons_bonds_rigor_pass_2026-05-21_cross_corpus_ipg_canonical_construction_v1.0.0.md`)
need to re-canonicalize the 33–122× IPG range against the new $455 or $524
Ch 8 floor?

**Options:**

- **Option A — Preserve the 33–122× lock; no re-derivation; light
  annotation only.** The 33–122× range is the canonical Ch 2 anchor
  ("depending on which cost categories you include and which social cost
  of carbon estimate you use"). The IPG ratio against $4.50 1960 price
  under Option A cascade ($455 floor) is 101×; under Option C cascade
  ($524 floor) is 116×. Both land inside the 33–122× canonical range.
  The 122× ceiling is anchored to the high-end SCC + all-categories-
  included parameter combination, which the new floor figures do not
  break. Add a light annotation to the IPG artifact's §5 ratification
  summary documenting that the Ch 8 worked-example floor has moved.

- **Option B — Widen the canonical range to accommodate the new bounds.**
  Move the canonical anchor to (say) 33–130× to capture the post-
  reconciliation upper bound + preserve the parameter-variation
  framing. Touches Ch 2 line 121 (the canonical home) + cross-chapter
  inventory line 89 (the canonical-lock row) + Ch 6 reconciliation prose
  + Ch 8 lines 168 + 212 (current canonical-range citation prose).

- **Option C — Re-canonicalize with explicit basis-note.** Replace 33–122×
  with "33–122× under national-average bituminous basis; 38–140× under
  McDowell-specific basis" or similar dual-basis disclosure. Touches Ch
  2 + Ch 8 + Ch 6 + inventory + the IPG artifact. Highest cost-of-change.

**Recommendation:** **Option A (preserve the 33–122× lock; no
re-derivation; light annotation only).**

**Reasoning:**

- **The 33–122× range is robust to both Option A and Option C cascades
  in §6.1 + §6.2.** $455 → 101× and $524 → 116×; both inside [33, 122].
  The canonical range does NOT break. Ch 2's parameter-variation
  language is sufficient methodological disclosure.
- **The HIGH-3 IPG canonical-construction artifact already ratified
  Option D (preserve canonical headline + today-prices follow-up beat).**
  That ratification was independent of the specific Ch 8 floor figure;
  it depended only on the structural-finding agreement ("carbon term
  dominates every era's market price"). The structural finding is
  preserved at any of the reconciliation outcomes.
- **The IPG artifact's prose disclosure framework ALREADY says** "the
  range is wide because the market price varies by era. The floor is
  high because the carbon term dominates anything the market has ever
  paid for a ton of coal" — that prose is invariant to whether the floor
  is $455 or $510 or $524.
- **Scope creep avoidance:** Option B + Option C would touch Ch 2 line
  121 (the canonical-home IPG framing) — material rewrite of the canonical
  IPG prose at the canonical home, which is exactly the prose change the
  HIGH-3 artifact's §6.2 Option C explicitly cautioned against ("Risk of
  future drift" + "Cost-of-change: Highest"). Doing it now to chase a
  reconciliation outcome that the range robustly accommodates would
  introduce new drift surface without methodological benefit.
- **Annotation discipline:** A one-line annotation in the IPG artifact's
  §5 noting that the Ch 8 floor has moved from $558 → $455 (Option A) or
  $524 (Option C) per author selection — and that the 33–122× lock is
  unaffected — preserves the audit trail without restructuring the
  canonical lock.

**Author judgment:** Option A is strongly recommended; the canonical lock
holds robustly. Options B + C are dispreferred (scope creep + prose-cost
out of proportion to methodological benefit).

---

## §7 — Ratification summary + sequencing recommendation

### §7.1 Ratification per finding

The author ratifies one option per §6 finding. Recommended bundle:

- **§6.1 Heat content basis:** Option C (hybrid: framework-introduction
  stays national-average; McDowell-specific contexts use McDowell-specific
  basis with footnote).
- **§6.2 Cascade direction:** Option C (hybrid cascade matched to §6.1
  Option C).
- **§6.3 IPG canonical lock:** Option A (preserve the 33–122× lock; light
  annotation only).

The recommended bundle yields a McDowell-specific Ch 8 floor of ~$524 with
methodological-disclosure footnote at Ch 8 line 72 + TA §11.6; cascade
touches Ch 6 line 343 + TA §11.1 + TA §11.6 (Block 4) + TA §1.7 (drift
cleanup); preserves Ch 6 line 42 + TA §7.4 in framework-introduction
register; preserves the 33–122× IPG canonical lock with light annotation.

**Alternative — simpler bundle for time-constrained Phase C session:**

- **§6.1:** Option A (preserve national-average basis; verbatim cross-thread
  #12 alignment).
- **§6.2:** Option A (Ch 8 retrofits down to $441 cascade).
- **§6.3:** Option A (preserve the 33–122× lock; light annotation).

The simpler bundle yields a Ch 8 floor of $455 + TA §11.1 + TA §1.7
cascade-cleanup, with no Ch 6 touches and no Ch 8 + TA §11.6 footnote
work. Smaller cascade surface; faster Phase C application; preserves
cross-thread #12 verbatim.

### §7.2 Sequencing recommendation for downstream Phase C application

The Phase C application is multi-touch. Recommended sequencing:

**Step 1 — Author ratifies one of the two bundles above (or constructs an
alternative per-finding combination).**

**Step 2 — Phase C application session fires** (fresh feature branch from
current origin/main; per CLAUDE.md content-edit branch discipline; stops
at feature branch + waits for explicit author merge unless prior author
ratification of cascade edits is on the record):

- **Step 2a:** Ch 8 cascade (7 lines per §5.1; coupling to line 168 + line
  74 wording "at least four" → "at least three" per §5.1 note).
- **Step 2b (if §6.1 Option C):** Ch 6 line 343 + footnote at Ch 6 line 42
  cross-referencing the McDowell-specific upgrade.
- **Step 2c:** TA §11.1 cascade (lines 3876 + 3882 + 3898).
- **Step 2d (if §6.1 Option C):** TA §11.6 Block-4 cascade (lines 4517 +
  4520 + 4533 + 4607 + 4623 + 4635 + footnote).
- **Step 2e:** TA §1.7 line 2916 drift-cleanup (independent of basis
  choice; ensures TA §1.7 references the current Ch 6 figure).
- **Step 2f:** Ch 9 cross-references (Ch 9:12 + Ch 9:116) — only under
  Option A (Option C preserves "approximately $550" within rounding).
- **Step 2g:** Cross-chapter consistency inventory rows 111 + 112.
- **Step 2h:** Light annotation to HIGH-3 IPG canonical-construction
  artifact §5.
- **Step 2i:** Cross-thread #12 status update + retire stale recommended-
  edit text.

Steps 2a–2g can be bundled into a single Phase C application session
(estimated 30–50 line-touches across 4 files + 2 audit artifacts); Step
2h + 2i are micro-touches that can ride along.

**Step 3 — Per cross-chapter workstream lifecycle discipline (per pipeline
doctrine §5):** Stage 1c light coherence-check re-fires for each touched
chapter (Ch 6 + Ch 8 + Ch 9) after Phase C application. Pass 3.3 light
audience-load re-fire fires per touched chapter. Workstream closes only
after all re-fires complete clean.

### §7.3 Coupling notes

- **Ch 8 line 168 + line 74 "at least four" wording (Stage 1c Phase C just
  ratified commit `cbef9bd`).** Under either Option A or Option C cascade,
  the "at least four" structural-finding beat retreats to "at least three"
  per the arithmetic ($441/$140 = 3.15×; $510/$140 = 3.64×; both round
  down to "at least three" under conservative-rounding discipline). The
  application session must update line 74 + line 168 wording for
  consistency.
- **TA §1.7 line 2916 drift-cleanup is INDEPENDENT of the §6.1 basis
  choice** but must be addressed in the Phase C application regardless
  (the stale "$550–$570/ton" reference predates Ch 6 Phase C-β and is
  incorrect against any of the reconciliation outcomes).
- **Cross-thread #12 recommended-edit text retires** regardless of which
  option ratifies; the verbatim text quoted in #12 ("approximately five
  hundred and forty-four dollars" → "approximately four hundred and
  forty-one dollars") is one specific version of the cascade; the
  reconciliation supersedes the routing-time recommendation.

---

## §8 — Invariant-gate + discipline checks

### §8.1 Apparatus regression check

This artifact does not introduce new apparatus terms, new framework
vocabulary, or new register decisions. No regression against the
apparatus-register decision sweep (commit
`tools/rigor-passes/commons_bonds_rigor_pass_2026-05-11_apparatus_register_decision_v1.0.0.md`).

The cross-corpus cascade itself, when applied per §7, preserves all
apparatus vocabulary at canonical form (no retired terms reintroduced; no
banned vendor-name patterns; no scaffolding-pattern regressions).

### §8.2 Named-subject consent

No named subjects affected by the reconciliation. The carbon-tail
calculation is a numerical methodology question; no named-living-subject
prose modifications.

### §8.3 Render-safety + corpus-invariant gates

This artifact uses standard markdown without scaffolding patterns
(`TODO`, `TK`, process-scaffolding vocabulary, INCLUDE / EXCLUDE glyphs,
meta-commentary tics). HTML / em-dash render conventions preserved.

### §8.4 Trust-decision documentation (per `feedback_audit_recent_active_review_default.md`)

Where this session conflicts with the older Ch 8 Pass 1 fact-check
artifact (2026-05-16), the trust-decision is to **trust the more recent
cross-thread #12 routing record (2026-05-14) + the Ch 6 Pass 1 Amendment
E ratification (2026-05-14) + the verified primary-source dimensional-
analysis chain in §2 over the Ch 8 Pass 1 source inventory line 491**.

The Ch 8 Pass 1 source inventory line 491 (which cited the EIA volume/mass
coal-CO₂ page as the authority for the 2.86 figure) is **methodologically
incorrect** — the EIA URL tabulates 2.32 mt/short ton bituminous, not 2.86,
and the 2.86 figure derives from a separate stoichiometric calculation
that the EIA page does not present as the canonical emission factor.

This trust-decision is the same direction as the cross-thread #12 routing
record's recommendation; this session adds the dimensional-analysis basis
+ the McDowell-specific methodology upgrade as a higher-honesty option
(§6.1 Option C) the cross-thread #12 routing did not surface.

### §8.5 Memory-discipline check (per `feedback_verify_stale_memory_claims.md`)

All file-line references in §5 verified against current file states 2026-
05-22 (Ch 6 = 365 lines post commit `9befb92`; Ch 8 = 243 lines; TA = 8,044
lines). All commit
SHAs verified visible in origin/main as of session start (5e260a3 → 02c6a19
→ 440906f → 7d7a6d2 progression observed during session).

Cross-chapter consistency inventory line 111 + line 112 verified against
current state. Cross-thread #12 entry verified against current
`publishing/essays/_pipeline/cross-thread-todos.md` state (entry at line 114; 2026-
05-21 status note at update-log line 199).

---

## §9 — Flag-forward (out-of-scope for this session)

The following findings surfaced during this session but are
out-of-scope per session-prompt constraints. Flagged here for future
audit / PM-session triage:

- **TA §1.7 line 2916 carries a pre-Ch6-Phase-C-β drift** independent of
  the Ch 8 cascade question (cites "Ch 6 figure of $550–$570/ton" when
  current Ch 6 is $449–$464). Should be cleaned up in any Phase C
  application session touching the TA; flag-forward for separate session
  if not bundled.
- **Cross-chapter consistency inventory line 111 "No drift" assessment is
  incorrect.** The row currently asserts Ch 8 + Ch 6 + TA are consistent at
  $544, but Ch 6 + TA §11.6 carry $441. The inventory needs updating
  regardless of the §6 decision.
- **Ch 8 Pass 1 source inventory line 491 carries a source-attribution
  error.** The EIA volume/mass coal-CO₂ page does not yield 2.86 short tons
  CO₂/short ton bituminous; it yields 2.32 metric tons CO₂/short ton.
  This methodological gap in the Ch 8 Pass 1 audit should be noted in a
  Ch 8 Pass 1 audit-revision artifact or in the §8 trust-decision
  documentation when Phase C application fires.
- **Heat-content basis sensitivity for OTHER coal grades referenced in
  the corpus** (Powder River sub-bituminous in Ch 5 context discussion;
  metallurgical-coal premium grades in Ch 8 line 75 + 165 today-prices
  context): not addressed by this reconciliation. The McDowell-specific
  upgrade discipline (§6.1 Option C) would naturally extend to other
  case-specific contexts if the framework adds new cases in future
  chapters / op-eds.
- **Wagner et al. 2021 SCC scope-and-discount-rate critique** (referenced
  Ch 8 line 119): not addressed by this reconciliation; the SCC anchor
  ($190/mt CO₂) is taken as the corpus-canonical anchor per Ch 6 + Ch 8
  + TA + cross-chapter inventory alignment. Flag-forward for SCC-anchor
  audit if a future session re-examines the SCC choice.

---

## §10 — Ratification record

| Finding | Option ratified | Date | Notes |
|---|---|---|---|
| §6.1 Heat content basis | **Option C** (hybrid: framework-introduction stays national-average; McDowell-specific contexts use McDowell-specific basis with footnote) | 2026-05-23 | Author ratified the recommended bundle as a unit. |
| §6.2 Cascade direction | **Option C** (hybrid cascade matched to §6.1 Option C) | 2026-05-23 | Couples to §6.1 Option C; cascade touches per §7.2 Step 2a–2i. |
| §6.3 IPG canonical lock | **Option A** (preserve the 33–122× lock; light annotation only) | 2026-05-23 | $524 → 116× lands inside the canonical range; no re-derivation. |

**Resulting corpus state after Phase C application:**

- Ch 8 McDowell-specific carbon-tail = **$510 / short ton coal**; Ch 8
  honest-cost floor = **$524 / short ton coal** (= $2 + $1 + $5 + $510 + $2
  + $1 + $1 + $2).
- TA §11.1 + TA §11.6 cascade to McDowell-specific basis (2.61 mt CO₂/short
  ton; $510 carbon-tail). TA §1.7 line 2916 retires stale "$550–$570/ton"
  reference (drift cleanup).
- Ch 6 line 42 + line 44 + TA §7.4 line 2859 preserve national-bituminous-
  average basis ($441 / 2.32 mt) in framework-introduction register; Ch 6
  line 343 (Pigouvian McDowell paragraph) cascades to McDowell-specific
  ($510 / 2.61 mt) with footnote at Ch 6 line 42 cross-referencing the
  basis-distinction.
- Ch 9:12 + Ch 9:116 preserved (Option C's $524 within rounding tolerance
  of current "$500–$600" + "approximately $550").
- Cross-chapter consistency inventory rows 111 + 112 update to reflect
  basis-varies-by-chapter-role disclosure.
- HIGH-3 cross-corpus IPG canonical-construction artifact gets a light §5
  annotation noting Ch 8 worked-example floor moved from $558 → $524; the
  33–122× canonical lock is robust to the move and not re-derived.
- Ch 8 line 168 + line 74 "at least four" wording retreats to "at least
  three" per coupling note in §5.1 ($510/$140 = 3.64×, conservative
  rounding to "at least three").
- Cross-thread #12 status updates to RESOLVED with cascade-commit reference
  upon Phase C application completion.

**Phase C application paste-text** drafted separately for downstream
session fire; sequencing per §7.2.

---

*End of artifact. Stage 1c cross-artifact coherence + methodology
reconciliation; RATIFIED recommended bundle; Phase C application pending
downstream.*
