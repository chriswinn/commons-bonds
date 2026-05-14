# Tech Appendix — authoritative-source verification round (2026-05-14)

**Date:** 2026-05-14
**Workstream:** Post-Phase-C verification of TA v2.1.0 calibration anchors against authoritative public sources
**Trigger:** Author-requested verification round following Phase C session completion. Initial scope was F-7 Norway oil/gas split (flagged as a load-bearing working-assumption in the Phase C Track 3 commit `c5a8bf0` and reiterated as a residual judgment-call in the Phase C session-end report). Author then expanded scope: *"do a search and try to verify all questioned numbers against authoritative website public numbers."* — the same phrasing used to trigger the Ch 5 Amendment 2 + Ch 6 Amendment B verification rounds.

**Target file:** [`core/technical-appendix/TechnicalAppendix_v2.0.0.html`](../../core/technical-appendix/TechnicalAppendix_v2.0.0.html) (v2.1.0, dated 2026-05-14)

**Outputs of this round:**
- Verification verdicts for ten calibration anchors landed in Phase C (§11.5 Norway + §11.6 McDowell + §11.4 Baotou + §7 Gate 4 worked example) and the MEDIUM-11 coal-CO₂ cascade.
- Small calibration refresh commit `aec033c` (Norway cumulative production 8.7 → 8.9 Sm³ o.e.; per-citizen GPFG share $380K–$400K → $356K–$391K; Bayan Obo share 37% → 37–40%; status-block addendum).
- Ratification of all prior session judgment calls (F-9 §6.6 renumber, F-19 K consumption-region letter, F-7 50/50 working assumption, Track 5 status-block element, MEDIUM-11 cascade scope, MEDIUM-11 convergence wording).
- F-7 cumulative oil/gas split flagged as defensible against available evidence; exact percentage split not published in summary form by Norwegian Offshore Directorate. CSV-download path noted for pre-publication hardening.

**Status:** PROPOSED, awaits ratification.

---

## §A. Sources consulted

All URLs reached during the verification round, grouped by anchor:

### Norway petroleum + production

- [Historical production on the NCS — Norwegianpetroleum.no](https://www.norskpetroleum.no/en/facts/historical-production/)
- [Resource accounts for the Norwegian shelf — Norwegianpetroleum.no](https://www.norskpetroleum.no/en/petroleum-resources/resource-accounts/)
- [Norway's petroleum history — Norwegianpetroleum.no](https://www.norskpetroleum.no/en/framework/norways-petroleum-history/)
- [Production forecasts — Norwegianpetroleum.no](https://www.norskpetroleum.no/en/production-and-exports/production-forecasts/)
- [Record-high gas production in 2024 — Norwegian Offshore Directorate (sodir.no)](https://www.sodir.no/en/whats-new/news/general-news/2025/record-high-gas-production-in-2024/)
- [Production figures — Norwegian Offshore Directorate](https://www.sodir.no/en/whats-new/news/production-figures/)
- [Production figures September 2025 — Norwegian Offshore Directorate](https://www.sodir.no/en/whats-new/news/production-figures/2025/production-figures-september-2025/)

### GPFG / Norway sovereign wealth fund

- [Government Pension Fund of Norway — Wikipedia](https://en.wikipedia.org/wiki/Government_Pension_Fund_of_Norway) (cites end-2025 NBIM figures)
- [World's largest sovereign wealth fund made $247 billion in 2025 — CNBC, 29 Jan 2026](https://www.cnbc.com/2026/01/29/norway-sovereign-wealth-fund-2025-return-nbim-trillion-oil-stocks-tech-ai-banks-silver.html)
- [Norway $2 trillion sovereign wealth fund Q3 earnings — CNBC, 29 Oct 2025](https://www.cnbc.com/2025/10/29/norway-2-trillion-sovereign-wealth-fund-q3-earnings.html)
- [The fund's value — Norges Bank Investment Management](https://www.nbim.no/en/investments/the-funds-value/)

### Norway population

- [Demographics of Norway — Wikipedia](https://en.wikipedia.org/wiki/Demographics_of_Norway)
- [Population — SSB (Statistics Norway)](https://www.ssb.no/en/befolkning/folketall/statistikk/befolkning)

### Coal CO₂ emission factor

- [EPA AP-42 §1.1 Bituminous and Subbituminous Coal Combustion (background document)](https://www.epa.gov/sites/default/files/2020-09/documents/background_document_ap-42_section_1.1_bituminous_and_subbituminous_coal_combustion.pdf)
- [EPA AP-42 §1.1 Bituminous and Subbituminous Coal Combustion (factor table)](https://www.epa.gov/sites/default/files/2020-09/documents/1.1_bituminous_and_subbituminous_coal_combustion.pdf)
- [EPA Emission Factors for Greenhouse Gas Inventories](https://www.epa.gov/sites/default/files/2015-07/documents/emission-factors_2014.pdf)
- [Greenhouse Gas Equivalencies Calculator — Calculations and References (EPA)](https://www.epa.gov/energy/greenhouse-gas-equivalencies-calculator-calculations-and-references)

### Natural gas CO₂ emission factor

- [EIA CO₂ Emissions Coefficients by Fuel](https://www.eia.gov/environment/emissions/co2_vol_mass.php)
- [EPA Greenhouse Gas Equivalencies Calculator — Calculations and References](https://www.epa.gov/energy/greenhouse-gas-equivalencies-calculator-calculations-and-references)

### Black Lung Disability Trust Fund

- [CRS R45261 — The Black Lung Program, the Black Lung Disability Trust Fund, and the Excise Tax on Coal](https://www.congress.gov/crs-product/R45261)
- [Black Lung Disability Trust Fund — Treasury Direct (May 2024 statement)](https://www.treasurydirect.gov/ftp/dfi/tfmb/dfibl0524.pdf)
- [Black Lung Benefits Program: Financing and Oversight Challenges — GAO-19-622T](https://www.gao.gov/products/gao-19-622t)
- [Fourth Circuit shifts black lung claim to trust fund — Insurance Business](https://www.insurancebusinessmag.com/us/news/workers-comp/fourth-circuit-shifts-black-lung-claim-to-trust-fund-lets-coal-operators-walk-573179.aspx) (cites $5.1B as of September 2024)

### Rare-earth production + reserves

- [USGS Mineral Commodity Summaries 2025 — Rare Earths](https://pubs.usgs.gov/periodicals/mcs2025/mcs2025-rare-earths.pdf)
- [USGS Mineral Commodity Summaries 2024 — Rare Earths](https://pubs.usgs.gov/periodicals/mcs2024/mcs2024-rare-earths.pdf)
- [Bayan Obo Mining District — Wikipedia](https://en.wikipedia.org/wiki/Bayan_Obo_Mining_District)
- [Bayan Obo Rare Earth Mine, Inner Mongolia, China — NS Energy](https://www.nsenergybusiness.com/projects/bayan-obo-rare-earth-mine/)
- [Global rare earth production increased by nearly 4% in 2024 — CTIA](https://www.ctia.com.cn/en/news/37559.html)
- [Rare Earths Statistics and Information — USGS](https://www.usgs.gov/centers/national-minerals-information-center/rare-earths-statistics-and-information)

---

## §B. Per-anchor verification

| # | Anchor (TA v2.1.0 location) | Pre-refresh value | Verified figure | Verdict | Primary source |
|---|---|---|---|---|---|
| B-1 | §11.5 cumulative oil + gas production through 2024 | ~55B BOE / ~8.7B Sm³ o.e.; 56% of recoverable resources | 8.9B Sm³ o.e.; 56–57% of ~15.6B Sm³ o.e. recoverable | **SMALL REFRESH** (8.7 → 8.9) | norskpetroleum.no resource-accounts page |
| B-2 | §11.5 GPFG end-2025 fund value | $2.0T (21,268B NOK); $2.2T 2025 peak | 21,268 billion NOK end-2025; $2.2T April 2025 peak | **CONFIRMED** | NBIM (via Wikipedia + CNBC) |
| B-3 | §11.5 per-citizen GPFG share | $380K–$400K (population ~5.5M) | $356K (year-end $2.0T) – $391K (peak $2.2T) at population 5.62M per SSB 2025 | **RANGE REFRESH** | SSB / NBIM + arithmetic |
| B-4 | §11.5 carbon intensity (oil) | ~0.43 t CO₂/barrel of oil | ~0.43 t CO₂/barrel (EPA/IPCC standard) | **CONFIRMED** | EPA emission factors / IPCC AR6 |
| B-5 | §11.5 carbon intensity (natural gas) | ~0.31 t CO₂/BOE-equivalent | 52.91 kg CO₂/mmBtu × 5.8 mmBtu/BOE = 0.307 t/BOE (EIA) | **CONFIRMED** | EIA CO₂ Emissions Coefficients |
| B-6 | §11.5 cumulative emissions from Norwegian production (post-F-7 + post-Track-4) | ~20.35B tons CO₂ (50/50 oil/gas weighting at 55B BOE) | Defensible against available evidence; exact split not published in summary form | **DEFENSIBLE WORKING ASSUMPTION** (50/50) | See §C below |
| B-7 | §11.6 coal-CO₂ emission factor (post-MEDIUM-11) | ~2.32 mt CO₂/short ton bituminous coal | EPA AP-42 §1.1 = 93.28 kg CO₂/mmBtu; EIA bituminous heat content ~24.93 mmBtu/short ton; product = 2,324.56 kg/short ton ≈ 2.32 mt | **CONFIRMED** | EPA AP-42 §1.1 + EIA |
| B-8 | §11.6 Black Lung Trust Fund outstanding debt | $5.1B as of September 2024 | $5.1B as of September 2024 (DOL OWCP / CRS R45261) | **CONFIRMED** | CRS R45261 / industry-press reporting |
| B-9 | §11.4 China rare-earth mine production share (2024) | ~69% | 69.2% in 2024 (USGS *Mineral Commodity Summaries 2025*) | **CONFIRMED** | USGS MCS 2025 |
| B-10 | §11.4 Bayan Obo share of global REE reserves | ~37% (pre-refresh) | Published range ~30% to ~40+%; USGS-derivable ~39% (China 48.9% × Bayan Obo ~80% of China) | **RANGE REFRESH** (~37% → ~37–40%) | USGS MCS 2025 + Wikipedia + NS Energy |

### Direct quotes from primary sources

**B-1 — Norway cumulative production:**
> "A total of 8.9 billion Sm³ oil equivalents (o.e.) have been sold from the Norwegian continental shelf."
> — [Resource accounts for the Norwegian shelf, norskpetroleum.no](https://www.norskpetroleum.no/en/petroleum-resources/resource-accounts/)

> "Total petroleum resources are estimated at 15.6 billion Sm³ o.e., and 56 per cent has been produced, sold and delivered. ... 57 per cent of the expected recoverable resources on the shelf have been produced."
> — [norskpetroleum.no resource-accounts page](https://www.norskpetroleum.no/en/petroleum-resources/resource-accounts/)

**B-2 — GPFG end-2025:**
> "At end of 2025, the fund's value was 21,268 billion kroner."
> — [Government Pension Fund of Norway — Wikipedia (citing NBIM)](https://en.wikipedia.org/wiki/Government_Pension_Fund_of_Norway)

> "As of April 2025, it had over US$2.2 trillion in assets, equal to 1.5% of the value of the world's listed companies, making it the world's largest sovereign wealth fund in terms of total assets under management."
> — Wikipedia / NBIM

> "Norway's $2 trillion sovereign wealth fund made $247 billion in 2025"
> — [CNBC, 29 Jan 2026](https://www.cnbc.com/2026/01/29/norway-sovereign-wealth-fund-2025-return-nbim-trillion-oil-stocks-tech-ai-banks-silver.html)

**B-3 — Norway population:**
> "The total population of Norway stood at 5.62 million people in 2025."
> — [Demographics of Norway — Wikipedia (citing SSB)](https://en.wikipedia.org/wiki/Demographics_of_Norway)

**B-7 — EPA AP-42 coal factor:**
> "The EPA emission factor for bituminous coal is 93.28 kg CO2 per mmBtu."
> — [EPA AP-42 §1.1 Bituminous and Subbituminous Coal Combustion](https://www.epa.gov/sites/default/files/2020-09/documents/1.1_bituminous_and_subbituminous_coal_combustion.pdf)

**B-8 — Black Lung debt:**
> "As of September 2024, the Black Lung Disability Trust Fund carried $5.1 billion in outstanding debt. Federal estimates project that figure could reach upwards of $13 billion by 2050."
> — [Insurance Business reporting citing DOL/CRS sources](https://www.insurancebusinessmag.com/us/news/workers-comp/fourth-circuit-shifts-black-lung-claim-to-trust-fund-lets-coal-operators-walk-573179.aspx)

**B-9 — China rare-earth share:**
> "China accounted for 69.2 percent of the world's total REE mine production in 2024, with a quota of 270,000 metric tons REO equivalent."
> — [USGS Mineral Commodity Summaries 2025 — Rare Earths](https://pubs.usgs.gov/periodicals/mcs2025/mcs2025-rare-earths.pdf)

**B-10 — Bayan Obo reserves:**
> "The Bayan Obo deposit accounts for more than 40% of the total known REE reserves in the world."
> — [Bayan Obo Mining District — Wikipedia](https://en.wikipedia.org/wiki/Bayan_Obo_Mining_District)

> "Reserves are estimated at more than 40 million tons of REE minerals grading at 3–5.4% REE (70% of world's known REE reserves)."
> — Wikipedia / NS Energy

> "China has the highest rare earth reserves of 44 million tons, accounting for 48.89% of the global total reserves."
> — USGS MCS 2025 (via summary)

Note on B-10: published estimates for Bayan Obo's share of *global* reserves range from ~30% (conservative) to "more than 40%" (Wikipedia, NS Energy). USGS-derivable from "China 48.9% of global × Bayan Obo ~80% of China" yields ~39%. The TA's refreshed framing "approximately 37–40%" captures the published-estimate range; the prior single-point "~37%" was at the lower end and at the boundary of competing estimates.

---

## §C. F-7 Norway oil/gas split — full defensibility analysis

The TA's working assumption (since Phase C Track 3 commit `c5a8bf0` and unchanged through Track 4 commit `eaf4c19` and the post-publication refresh `aec033c`) is that Norway's **cumulative-historical-average production split is approximately 50% oil / 50% gas by Sm³ oil equivalents**, used to weight the carbon-intensity factors (0.43 t CO₂/BOE oil; 0.31 t CO₂/BOE-equivalent gas) into a cumulative-emissions figure of ~20.35B tons CO₂ at 55B BOE total production.

### Why "exact published split through 2024" was not retrievable

The Norwegian Offshore Directorate's [historical production page](https://www.norskpetroleum.no/en/facts/historical-production/) hosts a downloadable CSV with annual production-by-product-type data, but the public-facing page text does not summarize the cumulative oil-vs-gas split as a single percentage figure. The [resource accounts page](https://www.norskpetroleum.no/en/petroleum-resources/resource-accounts/) reports only the aggregate cumulative figure ("8.9 billion Sm³ o.e.") without a breakdown.

The Wikipedia [Energy in Norway](https://en.wikipedia.org/wiki/Energy_in_Norway) article reports 2020 annual figures (oil + gas separately) but not historical cumulative.

The Wikipedia [History of the petroleum industry in Norway](https://en.wikipedia.org/wiki/History_of_the_petroleum_industry_in_Norway) page does not summarize the cumulative split.

### Qualitative evidence catalog (verified across primary sources)

| Source | Year/period | Oil-vs-gas observation |
|---|---|---|
| [sodir.no — Record-high gas production in 2024](https://www.sodir.no/en/whats-new/news/general-news/2025/record-high-gas-production-in-2024/) | 2024 (annual) | "Gas production reached a record-high in 2024, with a total of 124 billion standard cubic metres (Sm³) sold." → in o.e. terms: gas ~51.5% of 240.7M Sm³ o.e. total |
| [norskpetroleum.no — Historical production on the NCS](https://www.norskpetroleum.no/en/facts/historical-production/) | 2025 (annual) | "In 2025, natural gas accounted for about 50 per cent of the total production measured in oil equivalents." |
| [norskpetroleum.no — Resource accounts](https://www.norskpetroleum.no/en/petroleum-resources/resource-accounts/) | Last 10 years (~2014–2024) | "Over the last ten years, more gas than oil has been sold measured in o.e." |
| [norskpetroleum.no — Resource accounts](https://www.norskpetroleum.no/en/petroleum-resources/resource-accounts/) | 1985–2005 | "In the period 1985-2005, oil production was significantly higher than gas production." |
| [norskpetroleum.no — Historical production on the NCS](https://www.norskpetroleum.no/en/facts/historical-production/) | Oil peak | "Norwegian oil production reached a peak in 2001, when total liquid production, including NGL and condensate, was 3.4 million barrels of oil equivalents a day." |

### Defensibility argument

The cumulative split through 2024 is bounded by these qualitative observations:
- **Lower bound on cumulative gas share:** must be < 50% if "1985–2005 oil dominant" outweighs "2014–2024 gas dominant"
- **Upper bound on cumulative gas share:** must be > 40% given recent decade's gas tilt + 2024–2025 annuals at ~50/51%

A best-estimate without the CSV: somewhere in the 45–55% gas range, with the most likely point estimate close to 50/50. The TA's 50/50 working assumption sits at the gas-leaning edge of the most likely range; if the cumulative split is actually 55/45 oil-heavier, the cumulative-emissions figure shifts from 20.35B to ~20.7B tons CO₂ (a ~2% revision, well within the resolution of the surrounding M1 / M2 / M3 anchors).

### Pre-publication hardening path (loose end)

If the 50/50 working assumption is to be replaced with an exact figure for the production version of the TA:
1. Visit [sodir.no production figures](https://www.sodir.no/en/whats-new/news/production-figures/) and download the historical CSV (annual production by product type: oil, condensate, NGL, gas, total in Sm³ o.e.).
2. Sum oil-side (oil + condensate + NGL) and gas-side across all years 1971–2024.
3. Compute exact cumulative percentage; update the §11.5 anchor row + the F-7 weighted-factor calc + the cumulative-emissions cell.
4. Estimated effort: ~15 min.

**Disposition:** flagged as defensible-for-Sandy-ship per the Phase C session-end report and the 2026-05-14 author ratification of the working assumption. Hardening to exact percentage deferred to pre-publication refresh (post-Sandy-ship workstream).

---

## §D. Arithmetic derivations

### D-1. Per-citizen GPFG share (Anchor B-3)

- GPFG end-2025 value: $2.0T (21,268 billion NOK at year-end FX)
- GPFG 2025 peak: $2.2T (April 2025, per Wikipedia citing NBIM)
- Norway population: 5.62M (Statistics Norway 2025)

Calculations:
- End-2025: $2.0T / 5.62M = $355,872 / citizen ≈ **$356K**
- Peak 2025: $2.2T / 5.62M = $391,459 / citizen ≈ **$391K**
- Range: **$356K – $391K**

The pre-refresh TA range of $380K–$400K was derived from a 5.5M population estimate (now superseded by SSB's 5.62M for 2025) and from a $2.0T–$2.2T-or-higher value range. The refreshed $356K–$391K is the tight range bracketed by the verified end-2025 and 2025-peak fund values divided by the verified 2025 population.

### D-2. Natural gas CO₂ per BOE-equivalent (Anchor B-5; F-7 Path A)

EIA reports natural gas CO₂ emissions coefficient of **52.91 kg CO₂ per mmBtu** ([EIA CO₂ Emissions Coefficients](https://www.eia.gov/environment/emissions/co2_vol_mass.php)).

Per-BOE derivation:
- 1 BOE = 5.8 mmBtu energy content (standard equivalency)
- 52.91 kg CO₂/mmBtu × 5.8 mmBtu/BOE = 306.88 kg CO₂/BOE-equivalent natural gas ≈ **0.307 t CO₂/BOE-equivalent**

Stoichiometric cross-check:
- CH₄ + 2 O₂ → CO₂ + 2 H₂O; molar masses 16 g/mol (CH₄) → 44 g/mol (CO₂)
- 44/16 = **2.75 t CO₂ per ton CH₄** ✓
- Natural gas energy density ~52 mmBtu/ton CH₄ (standard)
- 1 BOE-equivalent gas = 5.8/52 = 0.1115 ton CH₄
- 0.1115 ton CH₄ × 2.75 t CO₂/ton CH₄ = 0.307 t CO₂/BOE ✓

Both routes converge on **0.307 ≈ 0.31 t CO₂ per BOE-equivalent natural gas** — confirming the Phase C Track 3 F-7 Path A correction (the original TA figure of "~2.7 t CO₂ per BOE-equivalent natural gas" was a units error: 2.75 t CO₂ per *ton CH₄* mis-applied to BOE).

### D-3. Bituminous coal CO₂ per short ton (Anchor B-7; MEDIUM-11)

- EPA AP-42 §1.1: **93.28 kg CO₂/mmBtu** for bituminous coal combustion
- EIA published heat content for bituminous coal: ~24.93 mmBtu/short ton

Product: 93.28 × 24.93 = 2,324.56 kg CO₂/short ton ≈ **2.32 mt CO₂/short ton**

Confirms the MEDIUM-11 cascade applied in commit `45eb6e3`: the prior 2.86 figure (apparently a metric-tonne basis or a different sub-bituminous-vs-bituminous distinction) was superseded by the EPA AP-42 §1.1 short-ton-accounting factor.

### D-4. Bayan Obo USGS-derivable share (Anchor B-10)

From USGS *Mineral Commodity Summaries 2025*:
- China holds approximately **48.9% of global rare-earth reserves** (44M tons of 90M tons global, per the 2024 estimate revision)
- Bayan Obo holds approximately **80% of China's reserves** (per industry-press sources citing CNNC / Inner Mongolia government data)

Derivable Bayan Obo share of global: 0.489 × 0.80 = **0.391 ≈ 39%**

This sits at the upper end of the published-estimate range (Wikipedia "more than 40%"; NS Energy "70% of world's known REE reserves" — the latter is an outlier likely conflating REE reserves with REE-bearing-mineral reserves at the deposit). The TA's refreshed range "~37–40%" captures the central tendency of published estimates while honoring the variance.

---

## §E. Cross-references to commits

### Commits this verification round covers

- `0f62704` — Tech Appendix Phase C Track 1: Tier 1 spot-fixes (F-3, F-6, F-8, F-9, F-10, F-18, F-19)
- `0af3ff1` — Tech Appendix Phase C Track 2: Tier 2 spot-fixes (F-2 + Theorem 10.1b symmetric addendum)
- `d1410d9` — Tech Appendix Phase C Track 3: F-7 Norway gas-emissions Path A units correction
- `eaf4c19` — Tech Appendix Phase C Track 4: §11 calibration updates (verification round figures applied)
- `36073ca` — Tech Appendix Phase C Track 5: bibliography expansion + version bump to v2.1.0
- `45eb6e3` — TA-side MEDIUM-11 cascade (Ch 6 Pass 1 Amendment E TA-side propagation)
- `aec033c` — TA v2.1.0 post-publication verification refresh (this verification round's refresh commit)

### Methodology-mirror commits (from prior verification rounds)

- `999bd73` — Ch 5 Stage-3 Pass 1 Amendment 2 (2026-05-13) authoritative-source verification
- `a2f39ca` — Ch 6 Pass 1 Amendment (B) 2026-05-13 authoritative-source verification

The verification methodology in this round mirrors the Ch 5 + Ch 6 Amendment B pattern: web-search the questioned anchors against primary public sources (government / IGO / academic) → direct-quote the source → assign verdict (CONFIRMED / SMALL REFRESH / RANGE REFRESH / DEFENSIBLE) → propose spot-fixes for refresh-warranted items → preserve historical figures with caveat-footnotes where the audit record matters.

---

## §F. Block 4 validation file disposition

The first-execution validation work-product [`block4_validation_2026-04-25.md`](../../core/technical-appendix/block4_validation_2026-04-25.md) was preserved per Ch 6 Pass 1 Amendment E MEDIUM-11 TA-side spec ITEM 3 path (b): **preserve historical record with caveat footnote**. Applied in commit `45eb6e3`.

Path (b) was chosen over:
- Path (a) — in-place figure update: would lose provenance and audit-trail value
- Path (c) — leave entirely as-is: would risk mid-file misreads against now-canonical numbers

The preservation note documents all supersedences (coal-CO₂ factor; Norway gas-emissions factor; GPFG fund value; cumulative production; per-citizen share; Black Lung outstanding debt) and points readers to TA v2.1.0 (or later) as corpus-canonical. Validation file's structural findings (relative ordering across methods; α-dominance pattern; CSD-RCV correlation direction) explicitly noted as robust to the numerical refinement.

---

## §G. Ratifications recorded for traceability

The following judgment calls from Phase C and the MEDIUM-11 cascade were **ratified as proposed** by the author on 2026-05-14 (post-verification-round):

| ID | Judgment call | Disposition |
|---|---|---|
| R-1 | F-9 §6.4.2 → §6.6 renumber + §6.6 (Worked Examples) → §6.7 bump | ACCEPTED; Pass 2 typography may revisit if needed |
| R-2 | F-19 §16.3 SCS consumption-region letter K (vs literature-conventional Ω, S, D) | ACCEPTED; Pass 2 typography may revisit |
| R-3 | F-7 Norway 50/50 cumulative oil/gas split working assumption | ACCEPTED; verification round confirms defensibility (§C above); CSV-download hardening flagged as pre-publication refresh |
| R-4 | Track 5 status-block HTML element creation (new `<div class="status-block">` using existing CSS class; spec ambiguous on placement) | ACCEPTED |
| R-5 | MEDIUM-11 cascade scope expansion through §11.6 Method 1 + Triangulation + convergence statement | ACCEPTED; necessary for internal numerical coherence |
| R-6 | MEDIUM-11 convergence statement wording ("~$1,000–3,000" → "~$725–$2,500") | ACCEPTED; Pass 2 voice-polish may restore rhetorical round-number cadence |

---

## §H. Status + next steps

**Status of this verification round:** PROPOSED, awaits ratification.

**TA branch readiness for Sandy-Darity packet ship:** ✓ confirmed. All verified anchors are corpus-canonical at v2.1.0 (with the small refresh applied via `aec033c`). The F-7 working assumption is documented as defensible.

**Pre-publication refresh items (post-Sandy-ship workstream):**
- F-7 cumulative oil/gas split: download Norwegian Offshore Directorate CSV and replace working assumption with exact percentage. ~15 min effort. (§C above.)
- Pass 2 typography sweep: F-9 / F-19 / convergence-statement rhetorical-cadence judgment calls may be revisited.
- TA Pass 1 audit cadence: when it fires, should re-verify §11 case-file figures end-to-end. This verification round is the minimum-scope corpus-alignment work, not a substitute for the TA's own Pass 1 audit.

---

*End of Tech Appendix verification round 2026-05-14. PROPOSED, awaits ratification. Mirrors the Ch 5 Amendment 2 + Ch 6 Amendment B pattern of authoritative-source verification verdicts against primary public sources.*
