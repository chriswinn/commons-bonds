# TA Method-3 σ (scarcity parameter) — empirical-grounding audit

**Date:** 2026-06-07
**Workstream:** M3-rigor (make Method 3 antagonist-proof by grounding posited
parameters in cited data).
**Parameter:** σ (sigma) — the framework's effective-scarcity parameter,
defined in TA §3.5 as **commons-stock / sustainable-flow ratio**. Currently
POSITED at σ ≈ 200–500 for McDowell coal (§11.6, line 4742) and σ ≈ 50–200 for
Norwegian oil (§11.5/§11.8 calibration, line 4292).
**Discipline:** HARD no-invented-claims. Every figure below carries a real
source with a URL. Where a figure could not be located, that is stated as such.
Target standard: replace the bare posit with class-1 (sourced) or class-2
(derived-from-cited-inputs) grounding.
**Companion artifact:** `ta-method3-parameter-provenance_2026-06-06.md` (sibling
audit) gives the overall SOURCED/DERIVABLE/POSITED verdict across all five M3
inputs and confirms σ/α/V_option are currently analytical sensitivity ranges
with no external citation attached to any numeric endpoint. This audit supplies
the missing empirical anchor specifically for σ.

---

## 1. What σ means and how R/P maps to it

TA §3.5 (line 892): **σ = scarcity parameter (commons-stock / sustainable-flow
ratio).** For a renewable resource, sustainable flow is the regeneration rate
and σ is finite and modest. For a **functionally non-renewable** resource (coal,
oil, rare earths), the geological regeneration timescale is ~10⁶–10⁸ years —
effectively zero on civilizational timescales — so the *literal* stock /
regeneration-flow ratio diverges to ~10⁶+ (this is the §3.5 "structurally
unbounded as σ → ∞" regime). That literal ratio is not operationally useful for
calibration.

The **operational proxy** the extractive-resource literature already uses for
"stock / flow" is the **reserves-to-production (R/P) ratio**: remaining proved
reserves ÷ annual production = years the reserve would last at current extraction
rate. R/P is *exactly* a stock/flow ratio, in years. This is the natural,
citable empirical anchor for σ.

**Definition (R/P), per the Energy Institute / BP Statistical Review and EIA:**
"R/P ratios represent the length of time that remaining reserves would last if
production were to continue at the previous year's rate; calculated by dividing
remaining reserves at the end of the year by production in that year."
([Energy Institute Statistical Review](https://www.energyinst.org/statistical-review/about);
[Reserves-to-production ratio, Wikipedia](https://en.wikipedia.org/wiki/Reserves-to-production_ratio).)

Crucially, R/P has **two registers** that bracket the answer:

- **Total-recoverable-reserve R/P** — all reserves a country/world could ever
  mine ÷ current production. Large (centuries for coal).
- **Producing-mine R/P** ("working inventory at active mines") — only the
  reserves at currently-operating mines ÷ production. Much smaller (decades).

Both are EIA-published. The choice between them is the load-bearing modeling
decision for σ (see §5).

---

## 2. COAL — R/P data (US, Central Appalachia / McDowell, world)

### 2a. World coal
- **World coal R/P ≈ 133 years** (proven reserves ≈ 133× annual consumption).
  Derived from Energy Institute / BP Statistical Review reserve + production
  data. ([Worldometer World Coal, citing EI/BP Statistical Review](https://www.worldometers.info/coal/);
  cross-checked at [PSU EGEE-102, citing Statistical Review](https://www.e-education.psu.edu/egee102/node/1932):
  petroleum 47.1 yr / natural gas 52.4 yr / coal 133 yr.)

### 2b. United States coal (EIA — authoritative)
EIA "How large are U.S. coal reserves?" (FAQ id=70) and "How much coal is left":
- Demonstrated Reserve Base: **~468–470 billion short tons** (remaining as of
  Jan 1, 2024 / Jan 1, 2025 vintages).
- Estimated **recoverable reserves: ~249–250 billion short tons**.
- **Recoverable reserves at producing mines: ~11.7 billion short tons** (Jan 1,
  2022 vintage).
  ([EIA FAQ id=70](https://www.eia.gov/tools/faqs/faq.php?id=70&t=2);
  [EIA How much coal is left](https://www.eia.gov/energyexplained/coal/how-much-coal-is-left.php);
  [EIA U.S. Coal Reserves](https://www.eia.gov/coal/reserves/).)

**US coal R/P, both registers (EIA's own arithmetic, 2022 production ≈ 0.594 Bt):**
- Total recoverable reserves → **~422 years**.
- Reserves **at producing mines → ~20 years**.
  (Both figures stated verbatim by EIA, [How much coal is left](https://www.eia.gov/energyexplained/coal/how-much-coal-is-left.php).)
  NB: 2024 US production fell to 512.5 Mt ([EIA Annual Coal Report 2024](https://www.eia.gov/coal/annual/pdf/acr.pdf)),
  which lengthens both ratios modestly; the EIA-published 422 / 20 split is the
  citable anchor.

### 2c. Central Appalachia / McDowell County (the §11.6 case)
- USGS / Appalachian-basin assessment: Central Appalachian coal "has been mined
  aggressively for more than a century"; remaining reserves are deeper / in
  thinner seams, raising cost, and **production trends lower over the next ~20
  years as dwindling reserves make the coal uncompetitive**, most acutely in
  southern West Virginia. ([USGS Prof. Paper 1625-F Ch. H, Appalachian/Illinois
  basin depletion](https://pubs.usgs.gov/pp/1625f/downloads/ChapterH.pdf);
  [USGS Prof. Paper 1708-D3, Appalachian-basin bituminous production past/present/future](https://pubs.usgs.gov/pp/1708/d3/pdf/pp1708_d3.pdf).)
- **McDowell County specifically** (UNT Digital Library / USGS coking-coal
  estimate): original mineable reserves **5.34 billion tons**; reported
  production 1883–1995 **1.50 billion tons**; estimated loss **1.00 billion
  tons**; **estimated recoverable reserves remaining ~1.70 billion tons**.
  ([UNT Digital Library — Estimate of Known Recoverable Reserves of Coking Coal
  in McDowell County, WV](https://digital.library.unt.edu/ark:/67531/metadc38590/);
  [WV Geological Survey, McDowell County](http://www.wvgs.wvnet.edu/www/geology/geolmcdo.htm).)
  McDowell peaked as the world's largest coal producer in the early 1950s and
  has since depopulated as reserves were drawn down — i.e. the producing-mine
  register has essentially collapsed there, which is the framework's point.

**Coal σ-relevant takeaway:** depending on register, coal R/P spans **~20 years
(US producing-mine inventory)** to **~133 years (world total)** to **~422 years
(US total recoverable)**. McDowell is at the depleted end of the producing-mine
register.

---

## 3. OIL — R/P data (world, Norway-relevant)

- **World oil R/P ≈ 47–53.5 years.** EI/BP Statistical Review: 53.5 years (2020
  vintage); ~47 years on 2024 reserves/consumption. World proven reserves
  ≈ 1,570 Bbbl (end-2023, EI 2024 edition) rising to ~1.77 Tbbl (2025 vintage);
  global production ≈ 95.2 Mbbl/d (2023).
  ([Worldometer World Oil, citing EI/BP](https://www.worldometers.info/oil/);
  [PSU EGEE-102](https://www.e-education.psu.edu/egee102/node/1932) (47.1 yr);
  [BP Statistical Review 2021 — Oil](https://www.bp.com/content/dam/bp/business-sites/en/global/corporate/pdfs/energy-economics/statistical-review/bp-stats-review-2021-oil.pdf);
  [EIA — Does the world have enough oil](https://www.eia.gov/tools/faqs/faq.php?id=38&t=6).)
- Norway-specific R/P not separately pinned here; the §11.5/§11.8 Norway σ build
  can lean on the world-oil R/P band (~47–53 yr) plus Norway's documented
  depletion-rate discipline, already narrated in
  `research/case-studies/norway-swf.md`.

**Oil σ-relevant takeaway:** world oil R/P ≈ **47–53 years** — roughly a quarter
to a third of world coal's total-reserve register and an order of magnitude below
coal's total-recoverable US register. Oil is "scarcer" than coal on the R/P
metric, which is consistent with the TA's *lower* σ band for oil (50–200) vs
coal (200–500) ONLY if σ is read as a depletion-severity index rather than a raw
R/P number — see §5, where this tension matters.

---

## 4. RARE EARTHS — R/P data (world; Baotou/China context)

USGS *Mineral Commodity Summaries* is the authoritative source.
- **World reserves ≈ 90–110 million tons REO** (USGS MCS 2025 reports ~90 Mt;
  the prior ~110 Mt figure is the MCS 2024 vintage).
- **World mine production ≈ 390,000 tons REO (2024)**, up from ~350,000 t,
  driven by China, Nigeria, Thailand.
- China reserves ~44 Mt (~49% of world); Brazil ~21–22 Mt; Vietnam ~22 Mt
  (per-country figures vary by vintage).
  ([USGS MCS 2025 — Rare Earths](https://pubs.usgs.gov/periodicals/mcs2025/mcs2025-rare-earths.pdf);
  [USGS MCS 2024 — Rare Earths](https://pubs.usgs.gov/periodicals/mcs2024/mcs2024-rare-earths.pdf);
  [USGS Rare Earths statistics hub](https://www.usgs.gov/centers/national-minerals-information-center/rare-earths-statistics-and-information).)
  TA §3971 already cites USGS MCS 2025 for the Baotou/Bayan Obo reserve share —
  consistent source family.

**Rare-earth R/P (derived from cited USGS inputs):**
- 90 Mt ÷ 0.39 Mt/yr ≈ **231 years**.
- 110 Mt ÷ 0.39 Mt/yr ≈ **282 years**.

**Rare-earth σ-relevant takeaway:** world R/P ≈ **230–280 years** — the longest
of the three resources on the total-reserve register. Rare earths are
"non-renewable + strategically critical" but *not* near-term reserve-scarce; the
binding scarcity is geopolitical concentration + processing toxicity (Baotou
tailings), not R/P exhaustion.

---

## 5. Mapping R/P → σ, and whether σ = 200–500 is supportable

### 5a. The unit problem
σ is dimensionless (a stock/flow *ratio*); R/P is in **years** but is *also* a
stock/flow ratio (reserve-tons / annual-tons). So R/P-in-years is numerically a
candidate σ directly. The collected numbers:

| Resource | R/P register | R/P (years) | Source |
|---|---|---|---|
| Coal — US producing mines | working inventory | **~20** | EIA |
| Oil — world | total proved | **~47–53** | EI/BP, EIA |
| Coal — world | total proved | **~133** | EI/BP |
| Rare earths — world | total reserves | **~230–280** | USGS (derived) |
| Coal — US total recoverable | total recoverable | **~422** | EIA |

### 5b. Is σ = 200–500 (coal) supportable?
**Partly, and only under one specific register choice — not as currently
narrated.** Findings:

1. **The posit IS bracketable by real data**, which is the win: σ = 200–500 for
   coal sits squarely inside the empirical R/P envelope IF σ is read as the
   **total-recoverable US-coal R/P (~422 yr)** blended toward the world figure
   (~133 yr). The high end (500) slightly exceeds the 422-yr anchor; the low end
   (200) sits between world-coal (133) and US-total (422). So **σ ≈ 200–422 is
   class-2 defensible** (derived from EIA + EI/BP R/P), and σ = 500 is a modest
   round-up beyond the strongest single anchor.

2. **But the narrative justification in §11.6 ("coal regenerates over geological
   time; functionally non-renewable; high effective scarcity") points the OTHER
   way.** "High effective scarcity" + "near critical-stock threshold" is the
   *producing-mine* register (~20 yr for US coal; collapsed for McDowell), not
   the 200–500 band. The text justifies σ with a scarcity-severity story but the
   number 200–500 actually corresponds to the *abundance* register
   (total recoverable). This is an internal mismatch an antagonist would catch:
   the prose says "nearly exhausted," the number says "centuries of reserves."

3. **Cross-resource ordering is INVERTED vs the TA's own bands.** On R/P, the
   scarcity ordering (scarcest → most abundant) is:
   oil (~47–53) < world coal (~133) < rare earths (~230–280) < US-total coal
   (~422). But the TA assigns oil the *lower* σ band (50–200) and coal the
   *higher* (200–500) — i.e. it treats coal as scarcer than oil, the reverse of
   the total-reserve R/P ordering. This is reconcilable (oil is more
   substitutable; coal's *local* McDowell producing-mine R/P is ~exhausted) but
   the reconciliation is NOT currently stated, and the σ numbers don't transmit
   it. Coincidentally σ=50–200 for oil brackets the world-oil R/P (~47–53) at its
   low end, so oil's band is actually better-anchored than coal's.

### 5c. Recommendation (for a future apply session — this audit edits nothing)
1. **Re-anchor σ to a named R/P register explicitly.** Add one sentence to §3.5
   defining σ's empirical proxy as the reserves-to-production ratio (cite the
   EI/BP + EIA R/P definition) and stating which register each case uses.
2. **Pick the register that matches the scarcity story.** For McDowell's
   "high effective scarcity / functionally exhausted" framing, the honest anchor
   is the **producing-mine R/P (~20 yr) → σ ≈ 20–130** (producing-mine to
   world-coal), NOT 200–500. If the author instead wants the
   "centuries of physical coal still in the ground, but foreclosed for THIS
   community" framing, keep σ ≈ 130–422 and re-narrate explicitly as the
   total-reserve register. **The two cannot both be claimed with one number.**
3. **State the cross-resource ordering and its reconciliation** (substitutability
   for oil; local-vs-global reserve register for coal) so the inverted σ bands
   read as deliberate, not erroneous.
4. **Rare earths**: σ ≈ 230–280 (USGS-derived) is clean class-2; if the framework
   adds a rare-earth σ it should use this and flag that the binding scarcity is
   geopolitical/processing, not R/P.
5. Because the log form compresses σ heavily — scarcity_multiplier(σ=20) ≈ 1+ln(21)×0.05
   ≈ 1.15 vs scarcity_multiplier(σ=300) ≈ 1.29 vs σ=422 ≈ 1.30 — **the headline
   RCV is nearly insensitive to which register is chosen** (≤13% swing in the
   multiplier across the entire 20–422 range). This is the strongest defensive
   point: the σ posit can be re-grounded to real R/P data with negligible effect
   on the published per-ton numbers, so re-anchoring is low-risk and high-rigor.

---

## 6. Verdict

- σ = 200–500 (coal) is **currently a posit (class-0)**, narrated with a
  scarcity-severity story that does not match the number's register.
- It is **upgradable to class-2 (derived-from-cited-inputs)** using EIA US-coal
  R/P (20 yr producing-mine; 422 yr total recoverable) + EI/BP world-coal R/P
  (133 yr). σ ≈ 200–422 survives as a total-recoverable-register reading; the
  "high effective scarcity" prose instead supports σ ≈ 20–130.
- Oil σ = 50–200 brackets world-oil R/P (~47–53 yr) at its low end — **already
  near-class-2** with the EI/BP citation added.
- Rare-earth R/P ≈ 230–280 yr is cleanly derivable from USGS MCS.
- **No figure in this audit was invented.** Every R/P number traces to EIA, USGS,
  or the Energy Institute / BP Statistical Review via the URLs above. The one
  derived computation (rare-earth R/P = reserves ÷ production) is arithmetic on
  cited USGS inputs and is labeled as such.

---

## Sources

- EIA — How much coal is left: https://www.eia.gov/energyexplained/coal/how-much-coal-is-left.php
- EIA — How large are U.S. coal reserves (FAQ id=70): https://www.eia.gov/tools/faqs/faq.php?id=70&t=2
- EIA — U.S. Coal Reserves: https://www.eia.gov/coal/reserves/
- EIA — Annual Coal Report 2024: https://www.eia.gov/coal/annual/pdf/acr.pdf
- EIA — Does the world have enough oil (FAQ id=38): https://www.eia.gov/tools/faqs/faq.php?id=38&t=6
- Energy Institute — Statistical Review of World Energy (about / definition): https://www.energyinst.org/statistical-review/about
- Energy Institute — Statistical Review of World Energy 2024 (73rd ed.): https://www.energyinst.org/__data/assets/pdf_file/0006/1542714/684_EI_Stat_Review_V16_DIGITAL.pdf
- BP Statistical Review 2021 — Oil: https://www.bp.com/content/dam/bp/business-sites/en/global/corporate/pdfs/energy-economics/statistical-review/bp-stats-review-2021-oil.pdf
- Worldometer — World Coal (citing EI/BP): https://www.worldometers.info/coal/
- Worldometer — World Oil (citing EI/BP): https://www.worldometers.info/oil/
- PSU EGEE-102 — Energy Reserves (R/P by fuel): https://www.e-education.psu.edu/egee102/node/1932
- USGS — Appalachian/Illinois basin coal depletion (PP 1625-F Ch. H): https://pubs.usgs.gov/pp/1625f/downloads/ChapterH.pdf
- USGS — Appalachian-basin bituminous production past/present/future (PP 1708-D3): https://pubs.usgs.gov/pp/1708/d3/pdf/pp1708_d3.pdf
- UNT Digital Library — Known Recoverable Reserves of Coking Coal in McDowell County, WV: https://digital.library.unt.edu/ark:/67531/metadc38590/
- WV Geological Survey — McDowell County: http://www.wvgs.wvnet.edu/www/geology/geolmcdo.htm
- USGS — Mineral Commodity Summaries 2025, Rare Earths: https://pubs.usgs.gov/periodicals/mcs2025/mcs2025-rare-earths.pdf
- USGS — Mineral Commodity Summaries 2024, Rare Earths: https://pubs.usgs.gov/periodicals/mcs2024/mcs2024-rare-earths.pdf
- USGS — Rare Earths statistics and information: https://www.usgs.gov/centers/national-minerals-information-center/rare-earths-statistics-and-information
- Reserves-to-production ratio (definition): https://en.wikipedia.org/wiki/Reserves-to-production_ratio
