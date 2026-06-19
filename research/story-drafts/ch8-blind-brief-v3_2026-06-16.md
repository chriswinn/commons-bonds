<!-- STATUS: PROPOSED v3 | 2026-06-16 | supersedes ch8-blind-brief-v2_2026-06-10.md | session: claude/br-V-G-structural-choice-V-handoff-260601-7f8e9d -->

# Chapter 8 Structural Drafting Brief v3 (BLIND): "What Things Actually Cost"
**Book: *Commons Bonds* by Chris Winn**
**Date: 2026-06-16. Supersedes the 2026-06-10 v2 brief in full (v2 sections 0-6 are preserved verbatim below; the v3 deltas are in the ADDENDUM at the end of the file).**
**Status: drafting brief for a whole-cloth blind drafter. Fresh drafts are written FROM THIS BRIEF ALONE plus the listed register-model files. Everything needed to reproduce the chapter's obligations, figures, lineage, and structural decisions is contained here. The drafter MUST read the ADDENDUM v3 section in full: it adds REQUIRED beats (matrix fills) and REQUIRED structural specs to the v2 architecture; where the addendum and a v2 beat both speak, the addendum's instruction is additive and binding.**

**What changed v2 -> v3 (summary).** (a) Two matrix-positioning fills become
REQUIRED beats: the "just-rebranded-externality / it's only Pigou" objection
and its rebuttal (previously UNANSWERED in the worked-ton chapter), answered on
the chapter's own terms without a citation roll-call; and a single
load-bearing, named-once resolution of the Hotelling / Pigou / Daly / Weitzman
attribution (the worked-ton chapter currently does their work voicelessly).
(b) Two structural specs become HARD: the per-component close formula must VARY
(no uniform component-close refrain such as "the walk prices $N a ton" or
"almost certainly an undercount" repeated across components); and a fidelity
hard constraint bars any invented-class assertion about what real people
say or do beyond the documented record (the prior winning draft carried one
"what real men say" line that required a mandatory cut). (c) The prior winner's
strengths are pinned as PRESERVE requirements so a fresh blind draft rebuilds
them rather than losing them. All v2 fact ground, figures, citations, lens
discipline, and prose rules carry forward UNCHANGED.

**What changed v1 -> v2 (summary).** (a) The Intergenerational Pricing Gap is
now LENS-EXPLICIT everywhere; the bare "33-122x" public headline is RETIRED
(author-ratified 2026-06-09), along with "~50x," "555x," "50-555x," and the
chapter's stray "120 times." (b) The Three-Ways method canon (TA merged
2026-06-09/10) governs every reference to the measurement chapter: Methods 1
and 3 are the two value estimators; Method 2 reads the realized bond and sets
a revealed lower bound; "three independent estimates converge" is retired.
(c) The scope correction is folded in: cost severance is positive when
consumption forecloses future access faster than restoration; zero within
restoration. (d) The housing block shrinks to roughly 300 words with the
supply-side steelman relocated to Chapter 9; the cross-case sweep gets its
proportions back. (e) Citation corrections: Hendryx OR 2.03 (not "60,000
cases"); $11T = Federal Reserve Z.1; completed foreclosures ~4.1M; black-lung
cumulative always dated "through 2009"; Trust Fund debt $5.1B as of Sept 2024.
(f) The regional-collapse and mobility-loss per-ton figures are labeled as
framework allocations on named anchors (Path A); no bare "economists" at
load-bearing pricing moments. (g) The duplicated Direct Health per-ton
allocation sentence is an editing seam: state the allocation once. (h) Full
prose rules (em-dash zero, antithesis budget, no self-narration, no
white-paper register) embedded in §5.

---

## 0. Role, purpose, and posture

**What Chapter 8 is.** The book's single worked number: the chapter that takes
one ton of Appalachian coal and prices it, cost component by cost component,
against the price it actually sold for at the mine mouth. Every prior chapter
built the vocabulary and the method; this chapter performs the arithmetic on
one specific extraction and shows the reader the gap between the invoice and
the true cost. It is an analytical chapter, not a memoir-scene chapter. Its
power comes from the arithmetic landing cleanly and the magnitude being felt.

**What Chapter 8 is NOT.** Not a policy recommendation, not degrowth, not
anti-capitalism, not anti-market. It is an accounting exercise. What gets
built from the visibility is named as the separate, political work of others
and as out of scope for this book. The disclaimer that the framework does not
legislate may appear AT MOST ONCE in the whole chapter (see §5, rule 3); place
it in Beat 1 and do not repeat it in Beat 15.

**Emotional center of gravity.** The reader should leave feeling that a real
and very large cost was borne by real and specific people who could not bill
it back, and that the market price never reflected it. The posture is
"no villain" honest accounting, not indictment. The cost is structural,
created by markets working exactly as designed. (Book-level guidance: the
most effective structural-critique books avoid easy villains; if the villain
is "greedy corporations" the book preaches to the choir. The problem is a
missing instrument, not bad people. Where the chapter touches operators,
engineers, or industry actors, render them as people responding to incentives
that never required them to price the collapse.)

**Hard register discipline (read §5 in full before drafting):** zero em-dashes
and zero en-dashes anywhere in the file; antithesis budget ~1 per 1,500 words;
no self-narration; no white-paper register; named external authority on every
load-bearing number; substrate-safe anchors only; no invented factual claims;
minimum 6,000 words, no maximum; no "End of Chapter" marker of any kind.

**Register models (read both before drafting):**
- `manuscript/chapters/Chapter_10_CommonBonds.md`, the harbor frame (opening
  and closing).
- `manuscript/chapters/Chapter__3_TheWaterman.md`, the Biggie section.

---

## 1. Ratified fact ground + canonical figure table

These figures are RATIFIED in the canonical figure ledger
(`manuscript/ledgers/_CANONICAL_FIGURE_LEDGER.md`, RATIFIED 2026-06-04,
AMENDED 2026-06-09) and verified against the Technical Appendix
(`manuscript/technical-appendix/TechnicalAppendix_v2.0.0.html`, closeout
merged 2026-06-09/10). Carry them EXACTLY. Verify the arithmetic yourself.

| Figure | Exact value and required phrasing |
|---|---|
| 1960 mine-mouth price | **$4.71/ton** (EIA Total Energy Table 7.9, bituminous; all-coal $4.83). Prose may say **"just under five dollars"**; use $4.71 where a point value is shown. Do NOT use the old "$4.50" or a loose "four to five dollars." Hyphen only if a range is shown ($4.70-4.85). |
| CO2 emission factor (McDowell) | **2.61 metric tons CO2 per short ton**, derived from the EPA AP-42 §1.1 bituminous-combustion factor (93.28 kg CO2 per mmBtu) applied to the Pocahontas-seam heat content (~28 mmBtu per short ton). Cite the heat-content source explicitly (USGS / EIA Pocahontas data) so a reviewer cannot swap in the lower national factor. NOT an anthracite assumption. |
| CO2 emission factor (national framework default) | **2.32 metric tons CO2 per short ton**; reference only as the national-bituminous-average figure the measurement chapter introduced; 2.61 is the McDowell-specific calibration of it. |
| Social cost of carbon | **$190 per metric ton**, attributed to the **EPA 2023 central estimate** (NOT to Rennert et al., whose own central was ~$185; see §3). |
| Carbon / foreclosure term (McDowell) | **$496** ( = 2.61 x $190 ). Phrase as "just under five hundred dollars." **$496 = the carbon term, NEVER the total.** |
| Carbon term, national basis | **$441** ( = 2.32 x $190 ). Belongs to the measurement chapter; if it appears here at all it is labeled national-basis carbon, never McDowell's. |
| Four-component conservative floor | **$504-518 per ton** ( carbon $496 plus the roughly $8-22 of the first three non-carbon heads ). |
| 8-component honest TOTAL | **$510 per ton.** **$510 = the TOTAL, never the carbon term.** |
| Intergenerational Pricing Gap | **LENS-EXPLICIT ONLY; see §1.2 below and §4.** The bare "33-122x" is RETIRED (author-ratified 2026-06-09). |
| McDowell population | ~98,887 (1950) to ~19,111 (2020); phrase 2020 as **"just over nineteen thousand" / "under twenty thousand"** (retire "18,000"). |
| Today's coal price range | $40 to $140 per ton depending on grade (used for the carbon-term-vs-today ratio of roughly three at the market peak). |

**The eight component figures (must sum EXACTLY to $510):**
- Direct Health: **$2**
- Environmental Degradation: **$1**
- Community Disruption: **$5**
- Foreclosure (carbon term): **$496**
- Lineage Labor: **$2**
- Knowledge and Cultural: **$1**
- Political Capture: **$1**
- Temporal Displacement: **$2**
- **Total: $510** ( verify: 2 + 1 + 5 + 496 + 2 + 1 + 1 + 2 = 510 ).

**Walk-range vs summary-figure discipline.** In the component-walk beats you
may state the conservative RANGE for a component (direct health "between two
and four dollars"; environmental "one to three dollars"; community disruption
"five to fifteen dollars") AND state that you use the low end. The summary
list in Beat 11 uses the low-end single figure for each. Make the
low-end-selection explicit so the range-in-walk and single-figure-in-summary
do not read as a contradiction.

**The running-total reconciling progression (REQUIRED).** The reader must
never reconcile the running total unaided. Carry the progression visibly:
**$8 (first three components) -> $504-518 (four-component floor including
carbon) -> $510 (full eight-component total).** Specifically: after the
Community Disruption beat, state that the first three components sum to
roughly eight dollars per ton, already near twice the 1960 price, with carbon
not yet priced. After the Foreclosure beat, state the four-component
conservative floor at $504-518. At the sum, land the full total at $510.

### 1.1 FORBIDDEN figures (must not appear anywhere in the chapter)

- **$524** (stale pre-correction total; the total is $510).
- **"33-122x"** in any phrasing, including "thirty-three and one hundred
  twenty-two times" and the chapter's old stray "thirty-three and one hundred
  and twenty times" (the 120-vs-122 self-inconsistency dissolves because both
  are retired).
- **"~50x" triangulated central**, **"555x"**, **"50-555x"** (TA-internal
  artifacts, disowned).
- **$580-620** RCV-model band (superseded even TA-side by the documented
  calibration; never conflate with $510).
- **$108 trillion Social Security** and its 3x-debt / 4x-GDP / $300k-per-person
  scalings (disavowed book-wide).
- **Any coercion / reparations dollar figure** (see §4, coercion discipline).
- TA-internal Method-3 dollar bands ($340-3,670; ~$1,115 center) in running
  prose: appendix material, not chapter material.

### 1.2 The lens-explicit Intergenerational Pricing Gap (the load-bearing v2 change)

Author-ratified 2026-06-09 (TA retirement decision record); applied in the TA
closeout (§9.5 / §11.1 / §11.6 / §11.11). The gap is not a single number; it
depends on which lens prices it and which era's price sits in the denominator.
The chapter REPORTS THE LENS AND THE PRICE BASIS, never a bare multiple.
Verified against the TA's current text 2026-06-10:

| Lens | Value | Basis |
|---|---|---|
| Carbon-externality / damage-function | **~107-110x** | against the $4.71 1960 mine-mouth price (TA §9.5) |
| Method-3 foreclosure premium | **8.5-26x, center ~15x** | price-independent (the market price cancels); the most conservative lens (TA §11.6/§11.11) |
| RCV-integral (Weitzman) | **61-115x** | $525-540/ton across the contemporary ~$8.66 and 1960 $4.71 price bases (TA §11.11; NOTE: the figure ledger shows 67-134x; this brief follows the TA's current text per instruction; the discrepancy is flagged in §6, do not resolve it in the draft) |

**Chapter-register usage (what the prose actually says).** The chapter does
not reproduce this table. It uses plain-English, lens-explicit anchors:

1. The carbon term against era prices (in-file anchor, KEEP): the carbon term
   alone exceeds every era's market price "by a factor running from roughly
   three against today's market peak to more than a hundred against the 1960
   mine mouth."
2. The total against the 1960 invoice: the $510 honest total runs "more than a
   hundred times what the county was paid" (matches the damage-function lens,
   ~107-110x; safe phrasing "more than a hundred times," or "roughly a
   hundredfold").
3. The most conservative lens, in plain words: the framework's most
   conservative way of pricing the gap, the premium of what was foreclosed
   over what the market paid, which does not depend on which era's price you
   use, still returns roughly 8.5 to 26 times, centering near 15.
4. Optional, one sentence plus pointer: the appendix's full multi-generational
   integral returns roughly 61 to 115 times against the same prices; the
   Technical Appendix carries the decomposition.

If the phrase "Intergenerational Pricing Gap" appears, spell it in full (no
acronym) and bind it to a named lens and price basis in the same sentence.
Magnitude summaries like "two orders of magnitude" must be lens-qualified:
true against the 1960 invoice on the damage lens; NOT true unqualified across
eras (against today's $40-140 prices the carbon term runs roughly 3 to 12x).

### 1.3 Other ratified fact ground (state-and-obey)

1. **U.S. Steel wind-down: "across the 1980s."** Per ledger judgment call J5,
   the McDowell/Gary wind-down was a phased process across the 1980s into the
   early 1990s. Do NOT state a hard year ("1986") or "two-thirds in a single
   year." Harmonize to "across the 1980s" / "by the late 1980s."
2. **McDowell socioeconomics (date-locked):** sixteenth-poorest in the United
   States (2022); median household income $28,235 against a national median
   ~$67,521; poverty 37.6% (Census SAIPE / ACS 2022). Drug-induced death rate
   141 per 100,000 (2015) against a national ~16 per 100,000 (CDC NCHS /
   WONDER); date-lock "(2015)" and note the McDowell figure is crude while
   the national is age-adjusted (footnote-grade basis difference).
   Mechanization cut the workforce by more than half within a decade of the
   1960 visit. Kennedy's 1960 campaign visit may be named (substrate-safe).
   Optional detail, pin before print: the county's last Walmart closed in
   2016 (news-archive pin still open; omit if not pinned).
3. **Exxon Valdez: "eleven million gallons"** (restored; see Beat 12).
4. **Black lung figures are always dated.** Cumulative benefits paid:
   "$44 billion through 2009 (GAO/CRS)," never presented as current. Trust
   Fund DEBT: $5.1B as of September 2024 (DOL/GAO), distinct from
   cumulative-paid; never conflate the two. (Supersedes the v1 brief's
   "$4.5B (2021)" anchor.) Black-lung life-shortening: "8-13 years of
   potential life lost per decedent."
5. **Life-expectancy gap: the thirteen-year figure is male-specific** ("for
   men"); the all-population divergence is ~10-12 years ("more than a
   decade").
6. **2008 (compact beat only):** ~$11 trillion in U.S. household wealth
   destroyed, attributed to the **Federal Reserve Financial Accounts (Z.1)**,
   NOT to Mian and Sufi (their own central magnitude is ~$5.5T housing
   wealth; keep Mian and Sufi for the response-architecture and
   leverage/distribution analysis only). Foreclosures: roughly **4.1 million
   completed** (CoreLogic, through 2012); "roughly ten million" is defensible
   only as filings/starts, clearly labeled, never as completed losses. TARP
   ~$700B direct authorization plus trillions in liquidity and guarantees
   (if a "$16T" figure is ever invoked it must carry the "gross cumulative
   originations" caveat, GAO-11-696; simplest is not to invoke it).
7. **Falsification surface (REQUIRED; two zero-conditions).** The chapter must
   show the model CAN return zero, in plain English, without apparatus
   jargon: (a) the honest cost is zero exactly when a perfect substitute
   exists, because nothing is then actually foreclosed; and (b) the cost is
   zero when use stays within what the commons can restore: for renewables,
   harvest within regeneration severs nothing. Place near the Foreclosure
   beat (where substitutability is the operative idea) or in the
   closing/limits material.
8. **Scope correction (author-ratified 2026-06-09).** Cost severance is
   positive when consumption forecloses future access FASTER THAN
   RESTORATION: always for non-renewables; for renewables only when harvest
   outpaces regeneration; zero within restoration. The commons floor rests on
   scarcity dynamics, not physical finiteness. NO "all extraction severs
   costs" overclaim anywhere; NO normative inference that renewables are
   inherently harmonious. Beat 14's non-fossil list already carries the
   correct scoping ("fisheries harvested above regeneration"): preserve that
   scoping discipline wherever extraction is generalized.

---

## 2. Required beats + section architecture

Draft the chapter in this order. Each beat is described by its job, not by any
existing sentence. Compose all prose fresh. Substrate-safe sensory anchors
available for openings of technical stretches (from the canonical chapter; do
NOT invent others): the lungs; the creek running orange; the rail car clearing
the last tunnel; the retired miner who knew exactly how the West Fork ran in
February; the house in a hollow that cannot be sold; the grocery store an hour
away.

**Beat 0: The paradox opener.**
Open with the question of what the world would look like if everything were
priced at what it actually costs. Frame it as deliberately non-ideological:
the answer falls out of arithmetic, not preference or politics. Issue a short
sequence of imperatives that put the reader to work pricing each hidden cost
in turn (the lungs, the poisoned water, the community that absorbed the loss,
the foreclosure handed to every later generation, the dispersed families, the
lost knowledge, the political effort spent keeping it invisible, the
compression of centuries of extraction into a few decades). Have the reader
add them up, look at the total, look at the price on the invoice, and notice
the distance. Make the reader DO the pricing rather than read about it being
done. Self-narration caution: the opener must not announce what "this
chapter" will do; the imperatives carry the structure without the chapter
narrating itself (see §5, rule 3).

**Beat 1: Statement of the exercise and its limits.**
State plainly that the exercise runs once, on a single ton of coal from the
county the book has followed since its early chapters, so the gap can be seen
unaggregated, undissolved in policy language, priced item by item. Then
disclaim hard: not degrowth, not anti-capitalism, not a policy
recommendation; an accounting exercise; what to do with the accounting is a
separate, political question deliberately not answered here. THIS IS THE ONE
permitted "the framework does not legislate" placement. Name that the cost
components walked here are the ones THIS extraction surfaces; a different
extraction surfaces a different set. The method is universal; the components
are case-specific. Scope discipline applies (§1.3.8): universality means the
method runs anywhere, NOT that all extraction severs costs; consumption
within restoration severs nothing. Gesture at the discipline that admits a
component WITHOUT naming the apparatus (no "Four Gates," no "Commons
Inversion Test," no "C-sub-i"; describe the operations: the inversion that
surfaces a hidden cost, the consistency of units, the bound that keeps the
number finite, the independence that prevents double-counting).

**Beat 2: "The coal, again."**
Return the reader to McDowell County: the county a presidential candidate
visited in 1960, the county that out-produced every other in the nation while
its residents queued for surplus food. State the 1960 mine-mouth price:
$4.71 a ton, "just under five dollars" (EIA). Describe how, as far as the
market was concerned, the accounting was complete the moment the rail car
cleared: a buyer paid, a seller was paid, the transaction cleared, the coal
was gone. Then name what the market did not price and assert it was not a
rounding error but the majority of the actual cost. Where the measurement
chapter is invoked, obey the Three-Ways canon (§4): two independent ways of
pricing what was lost land in the same range, and what polities have actually
paid back sets a floor beneath both; NEVER "every serious pricing methodology
agrees" as a three-way convergence claim. State the conservatism rule
explicitly: low end of every range, contested externalities omitted, because
the goal is a defensible FLOOR, and even the floor sits far above the cleared
price.

**Beats 3 through 10: the eight-component walk.**
Walk the eight components in this order. For each: name the component, ground
it in a concrete McDowell-specific reality (substrate-safe anchor opens each
technical stretch), state the per-ton figure used, keep the running total
visible. The carbon / foreclosure component (Beat 6) is the mid-chapter
gut-punch and dominates every other. **Vary the component closes:** the
"almost certainly an undercount" formula may appear AT MOST ONCE across the
whole chapter; other components simply end, or close on the concrete anchor,
not on an epigram (see §5, rule 2).

- **Beat 3: Direct Health Cost.** Open with the lungs; the canonical
  "Begin with the lungs" beat is genuinely good and is KEPT. Black lung as
  the most completely documented externality coal has produced: federally
  tracked, specifically attributable, and shifted onto the public ledger when
  company bankruptcies discharge the original liability. Note the earlier
  chapter walked the federal Black Lung Benefits Program and trust-fund gap
  in detail; here use only the per-ton headline: between one and one and a
  half dollars per ton allocated against national coal tonnage since the
  Program's 1969 establishment. **STATE THIS ALLOCATION EXACTLY ONCE** (the
  prior draft carried a duplicated allocation sentence, an editing seam; do
  not reproduce it). Any cumulative-paid figure is dated ("$44 billion
  through 2009, GAO/CRS"); Trust Fund debt, if invoked, is $5.1B as of
  September 2024 and distinct from cumulative-paid. Add the other direct
  health costs (excess cardiovascular mortality from particulates, elevated
  respiratory illness in mining communities whose children never entered a
  mine, cancers near processing facilities, the medical costs of populations
  whose life expectancy diverges from the national average by more than a
  decade; the thirteen-year figure, where used, is "for men"). Land the
  component range ($2-4) and the low-end selection ($2), labeled as the
  framework's conservative allocation built on the named anchors (the $2-4
  itself is a framework estimate, not an external fact). Make the point that
  the single most-documented component alone already returns most of what the
  coal sold for.

- **Beat 4: Environmental Degradation Cost.** Open at the creek. Acid mine
  drainage as a specific hydrochemical process, not a metaphor: exposed
  sulfide minerals oxidize in water and air, producing sulfuric acid that
  mobilizes heavy metals into the watershed for a century or more; treatment
  is perpetual and does not end when the mine closes. State the
  reclamation-bond shortfall under the 1977 Surface Mining Control and
  Reclamation Act as ONE consistent band: available bonds ~$3.8B against
  cleanup estimated at $7.5-9.8B, a gap of roughly $4-6B, per the Appalachian
  Voices 2021 analysis (*Repairing the Damage*); date-lock "(2021)." Do not
  carry two different gap bands. Acreage: roughly 633,000 acres awaiting
  cleanup across Appalachia (same source); "close to a million nationwide"
  only if attributed to OSMRE e-AMLIS. Mountaintop-removal epidemiology:
  state the Hendryx 2012 finding as the peer-reviewed result, an
  approximately doubled odds of cancer in mountaintop-removal communities
  (odds ratio 2.03, self-reported-survey design); do NOT state "sixty
  thousand cancer cases" as a Hendryx finding (it is an advocacy
  extrapolation not in the paper; if used at all it must be explicitly
  labeled as such, and the cleaner choice is the odds ratio). Add ecosystem
  service losses from valley fill burying streams, soil contamination
  downstream of processing, and coal-combustion mercury in fish as far as the
  North Atlantic (Lee et al. 2016). Land the component range ($1-3, framework
  allocation; low end $1), and note that added to direct health the severed
  cost is already comparable to the 1960 market price before any foreclosure
  pricing at all.

- **Beat 5: Community Disruption Cost.** The human-scale collapse: the county
  peaked near one hundred thousand residents around mid-century (98,887,
  1950 Census) and fell to just over nineteen thousand by 2020; mechanization
  cut the workforce by more than half within a decade of the 1960 visit. The
  U.S. Steel wind-down "across the 1980s" (J5; NO hard year, NO "two-thirds
  in a single year"). Poverty, median-income, and national-rank figures per
  §1.3.2, including "sixteenth-poorest in the United States (2022)." The 2015
  drug-induced death rate against the national rate, framed as the shape of
  community-disruption cost at human scale. Name the carrying costs of a
  community that drops to a fifth of its population: infrastructure
  maintained regardless of headcount with per-capita burden rising as
  headcount falls; economic-multiplier losses; public-program costs absorbed
  by state and federal government in a county that had generated billions in
  coal revenue that did not stay. **Authority discipline (Path A, REQUIRED):
  the five-to-fifteen-dollar band is the framework's own allocation, built on
  the named anchors above (Census population collapse, the income and
  mortality series). Do NOT attribute it to bare "economists who study
  regional collapse"; there is no namable external source for the per-ton
  band, so the prose must own it as a conservative framework estimate
  resting on named data, or restructure to carry the point without the
  band.** <!-- structure-note: if the author later commissions an external
  regional-decline costing source, the band can be re-anchored; until then
  the framework owns it explicitly. --> Land at the low end: $5. **Then place
  the FIRST running-total reconciling clause:** the first three components
  sum to roughly eight dollars per ton, near twice the 1960 price, and carbon
  has not yet been priced.

- **Beat 6: Foreclosure Cost (the carbon term: the dominant component).**
  State the combustion arithmetic carefully: one ton of this coal, burned,
  releases approximately 2.61 metric tons of CO2, derived from the EPA AP-42
  §1.1 bituminous-combustion factor (93.28 kg CO2 per mmBtu) applied to the
  Pocahontas-seam heat content (~28 mmBtu per short ton; cite the
  heat-content source explicitly so a reviewer cannot swap in the lower 2.32
  national factor, which would drop the carbon term to roughly $441,
  national-basis). Note 2.61 is the McDowell-specific calibration of the
  framework figure the measurement chapter introduced on the
  national-bituminous average. State the social cost of carbon: $190 per
  metric ton, the EPA 2023 central estimate (NOT attributed to Rennert et
  al.). Do the multiplication and land the carbon term exactly: $496, "just
  under five hundred dollars." State that this single term, before any of the
  other seven components, exceeds every era's market price for a ton of coal,
  **"by a factor running from roughly three against today's market peak to
  more than a hundred against the 1960 mine mouth"** (the lens-explicit
  in-file anchor; KEEP). Add the option-value foreclosure the carbon number
  does not capture (future metallurgical applications, future
  chemical-feedstock applications, future uses not yet imaginable for a
  carbon resource whose existing stock is being burned for electricity in a
  world where electricity can now be generated without combustion). State the
  foreclosure floor for coal burned in any era after viable renewable
  substitutes existed. **Place the falsification surface here or in the
  closing material (§1.3.7, both zero-conditions, plain English).** **Then
  place the SECOND running-total reconciling clause:** the conservative floor
  across the first four components is now $504-518 per ton.

- **Beat 7: Lineage Labor Cost (OWNS the literary lineage IN FULL; see §3.2).**
  Name the component the inversion surfaces: the cost borne not by the worker
  but by the worker's family and the generations downstream of the family's
  dispersal. Ground it concretely: a community that collapses by eighty
  percent does not take its children with it uniformly; the children who stay
  grow up in a food desert with the nearest grocery an hour away and one of
  the country's lowest graduation rates; the children who leave were raised
  by parents whose work was physically destructive enough that many did not
  live to see grandchildren; intergenerational wealth transmission becomes
  impossible when a family's entire asset base is a house in a hollow that
  cannot be sold. State that this is visible in the data, not rhetorical: a
  child born in the county in the bottom income quintile has among the lowest
  odds in the United States of reaching the top quintile; name the source,
  the public Opportunity Insights mobility data (Chetty and colleagues'
  Opportunity Atlas), which places the county at the floor of national
  outcomes. **Then render the full Dunbar / Du Bois / Fanon / Ellison lineage
  per §3.2, including the author's first-person infosec-"masking" provenance
  credited back to the tradition.** This lineage is a full owned passage, NOT
  a compensating gesture for a thin dollar figure. **This beat's
  Dunbar / Du Bois / Opportunity Insights texture is the chapter's best
  material; protect it at full depth.** State the component dollar figure
  honestly as small next to the carbon term and enormous next to the life of
  a child whose income possibility was fixed by the zip code of birth.
  Authority discipline (Path A): the per-ton band ($1-5) is a framework
  allocation anchored on the named mobility data; do not attribute it to bare
  "development economists." Price at $2 as the conservative placeholder.
  Invite the reader to judge whether that per-ton figure, multiplied across
  sixty years of extraction, is anything like a fair accounting.

- **Beat 8: Knowledge and Cultural Cost.** The component hardest to see while
  it happens because it is invisible until already lost. Every mining
  community carried practical knowledge: how to read the seams, how to manage
  risk on a specific geology, how to keep a particular valley's water system
  working, how the weather behaved in that hollow across a century. That
  knowledge existed because specific people stayed in specific places long
  enough to accumulate it. When the community dispersed, the knowledge went
  to places where it had no application (the retired miner who knew exactly
  how the West Fork ran in February did not move somewhere that needed to
  know it). Add the cultural-continuity loss (congregations, civic
  organizations, mutual-aid networks that could absorb a personal crisis
  because everyone knew everyone); replacement cost for the civic
  infrastructure of a community of a hundred thousand is not
  straightforwardly priced but is certainly not zero. Land the component
  figure ($1). Note it belongs in the accounting because the inversion
  surfaces it and a careful reader cannot omit the part of the cost that fell
  outside the ledger only because it was not denominated in dollars.

- **Beat 9: Political Capture Cost.** The reason the earlier components were
  invisible in the moment was not unavailable information; it was that the
  industry whose invoices omitted the costs had a financial incentive to keep
  them unpriced and did so for decades through documented lobbying,
  regulatory capture, and suppression of research. Black lung was
  identifiable as an occupational disease by the early twentieth century but
  was not a basis for federal compensation until 1969, and only after a
  miners' strike (the 1968 Farmington disaster context) and the West Virginia
  Black Lung Association forced the issue (MSHA record; Derickson 1998). Note
  that the mine workers' union under its mid-century leadership reportedly
  declined to press the issue at several points on the grounds that it would
  interfere with the mechanization producing higher wages, the same
  mechanization that produced the disease (KEEP the hedge "reportedly"). Then
  make the social cost of carbon itself an object of political capture across
  administrations: roughly $42 under one administration on a global-scope
  calculation (attribute to the interagency working group technical support
  document, NOT to Executive Order 12866, which is the cost-benefit framework
  rather than the SCC source); cut to between $1 and $7 under the next by
  limiting the calculation to the United States rather than global
  externalities, a change academic commentary (Wagner, Anthoff, Cropper et
  al. 2021) flagged as ungrounded in standard cost-benefit practice; restored
  to roughly $51 on a return to global scope; raised to the $190 used in this
  chapter by the 2023 EPA update. Make the point that the number is uncertain
  not because carbon physics is uncertain but because how much of the cost
  should be priced is a political fight, and one side has more resources than
  the other. Name that the cost of the fight is itself a severed cost
  (lobbying expenditure, captured agencies, funded think tanks, diverted
  civic attention); fossil-fuel lobbying alone runs into the hundreds of
  millions annually (OpenSecrets; date-lock the cycle and specify
  oil-and-gas-only ~$124-150M vs broader energy sector ~$435M, 2024). Credit
  the reparations-economics tradition (Coates, Darity and Mullen, Hamilton,
  Conley) for the actor-and-coalition vocabulary and the Public Choice /
  rent-seeking tradition (Buchanan, Tullock) for the extractor's reasoning,
  noting the book draws on the rent-seeking vocabulary rather than endorsing
  the broader political project, and that the next chapter develops the
  relationship at greater length (a real forward promise; the receiving
  chapter must honor it). **Coercion discipline (§4): the reparations credit
  is vocabulary-credit only; NEVER attach a coercion/reparations dollar
  figure; if a field figure must be cited, it is Darity's $14T (From Here to
  Equality 2nd ed / JEP 2022), attributed to the field, not computed by the
  framework.** Land the component figure ($1) as a deliberately low floor
  chosen to keep the running total conservative. (If the "almost certainly an
  undercount" formula is spent anywhere, this is the natural home; it may
  appear at most once in the chapter.)

- **Beat 10: Temporal Displacement Cost.** The cost of WHEN. The coal sat in
  the ground for hundreds of millions of years; its extraction was compressed
  into roughly a century, with the bulk moved in the few decades after
  mechanization, not because the country needed coal at that rate but because
  machinery raised the extractable rate and the industry's financial
  structure rewarded speed over measure. The component is the cost of
  foregone optionality: the value of having extracted more slowly, with time
  to develop alternatives, time for communities to diversify, time for the
  externality tail to be absorbed at a survivable rate rather than all at
  once. Note the 1970s oil shocks drove a large improvement in U.S. energy
  intensity over the following two decades because prices signaled that
  efficiency mattered (EIA energy-intensity series; specify the metric,
  energy per real GDP, and endpoints rather than asserting a bare "50%"); had
  coal been priced closer to its honest cost in 1960 the same signal would
  have driven the same adaptation at a pace communities could have survived.
  Instead mechanization compressed the timeline, the suppressed price killed
  the signal, and the adaptation did not happen until the damage forced it.
  Land the component figure ($2) without re-spending the "undercount"
  formula if already used.

**Beat 11: The sum.**
Present the eight components as a clean itemized list with the per-ton figure
beside each, then the total: $510. **The list must sum exactly to $510;
verify the arithmetic yourself.** State the total against the 1960 mine-mouth
price ($4.71, "just under five dollars") and against the range coal has sold
for since ($40-140 today depending on grade). **Then state the gap
LENS-EXPLICITLY per §1.2:** the honest total runs more than a hundred times
what the county was paid in 1960 (the damage lens against the 1960 price);
the framework's most conservative lens, the foreclosure premium over market
price, which does not depend on the era's price at all, still returns roughly
8.5 to 26 times, centering near 15; optionally, one sentence with appendix
pointer, the full multi-generational integral returns roughly 61 to 115 times
against the same prices. The carbon term alone exceeds even today's prices by
a factor of at least three. The structural finding holds across every era:
the honest cost of a ton of this coal has always exceeded what the market
paid; against the 1960 invoice, by roughly two orders of magnitude on the
damage lens. NO bare multiple anywhere. **Place the THIRD running-total
reconciling clause here if the full $8 -> $504-518 -> $510 progression is not
already woven across the section breaks.**

**Beat 12: The pattern made legible (cross-case sweep).**
Establish that the case is not a special exception by sweeping across the
other extraction cases the book examined earlier, all returning the same
structural gap in shape if not in scale. Move fast, an accelerando, not a
catalogue, **but give the cases room: Deepwater, Libby, Baotou, and Valdez
must NOT share a single paragraph while housing sprawls (the prior draft
inverted these proportions; v2 inverts them back: the cases get the space,
housing gets ~300 words).** Include:

- **Deepwater Horizon:** documented costs against projected well revenue give
  a gap in the mid-teens (the TA's current damage-function reading is ~15-16x).
  The framework adds a foreclosure layer the documented-costs accounting
  omits: the Macondo well's **projected lifetime production of 40-60 million
  barrels (the total reservoir / projected-production estimate, NOT spilled
  volume; the court-found release was ~3.19M barrels; phrase so a reviewer
  cannot read it as spill volume)** would release roughly 17-26 million tons
  of CO2 when combusted, an additional ~$3-5B in carbon-tail externality at
  the $190 anchor. The addition shifts the gap only slightly because
  documented direct costs already exceed revenue by an order of magnitude,
  but the methodological consistency matters: the framework that prices
  coal's carbon tail prices oil's the same way.
- **The Libby, Montana vermiculite mine (W. R. Grace):** state the multiple
  lens-explicitly or qualitatively. The TA's current convergence table
  (§9.5) gives roughly 65-100x on the damage lens (57-111x across lenses);
  the prior draft's "forty to eighty" predates the TA closeout and must NOT
  be used without author confirmation (open call, §6). Safe phrasings:
  "roughly sixty-five to a hundred times its lifetime revenue" or "tens of
  times its lifetime revenue."
- **Baotou rare earths:** the documented environmental and health costs to
  villagers next to the tailings lake give the same structural shape, but
  **do NOT state a computed multiple: the TA (§11.4) records Baotou's gap as
  not computable on documented inputs.** Frame qualitatively. If a
  remediation figure is needed, the documented range is ~$5-15B (NOT
  ">$100B," a retired inflation).
- **Exxon Valdez:** measured against the market value of the **eleven million
  gallons** spilled into the sound, a gap that defies simple calculation only
  because the recovery was never completed. Treat Valdez as a generic "case
  after case" invocation; it is a KNOWN DANGLING REFERENCE (the case
  substance lives in the measurement chapter, not the deep-case chapter); do
  NOT assert it was worked at depth in a specific earlier chapter.

Then scale the SAME structure beyond conventional extraction:

- **The rent-burdened household (housing block: ROUGHLY 300 WORDS TOTAL,
  HARD).** Run the cost-component arithmetic against a cost-burdened renter
  and the components populate: foreclosure-of-mobility cost, lineage-labor
  cost, political-capture cost from the zoning and tenant-law architecture.
  Value flows to absentee asset owners; costs accumulate at the household
  scale. About half of renters pay more than thirty percent of income on
  housing (Harvard JCHS, *America's Rental Housing 2024*; date-lock). The
  arithmetic differs from McDowell's; the structure is identical. **Then ONE
  crisp objection-and-deferral paragraph maximum:** name that this finding
  will meet a serious objection from the supply side (that housing costs are
  driven by zoning restrictions on supply rather than by landlord-surplus
  capture), concede the objection is not weak, and defer it explicitly to the
  next chapter, which makes the full supply-side case and answers it there.
  **Do NOT draft the steelman: no Glaeser, no Gyourko, no Schuetz, no JCHS
  supply-elasticity taxonomy, no supply-restricted-vs-supply-expanded metro
  walk, no RealPage / DOJ antitrust chronology (the steelman and its
  apparatus are RELOCATED to Chapter 9 per decision D3).** If RealPage is
  touched at all it is a passing past-tense fact (the DOJ proposed settlement
  landed 2025-11-24), but the cleaner choice at 300 words is omission.
- **The Canadian tar sands:** bitumen priced against heavy-crude markets while
  ecological damage falls on boreal forests and peatlands, treaty violations
  fall on indigenous First Nations whose territories host the operations, and
  the carbon tail follows the barrels wherever burned. Name the Athabasca
  Chipewyan First Nation, Mikisew Cree First Nation, and Fort McKay First
  Nation, and Treaty 8 of 1899 (accurate, public record). **Attribute
  elevated downstream cancer rates and contamination to the studies (O'Connor
  2006; Alberta Cancer Board 2009; the Mikisew Cree study) and treat
  causation as alleged / contested, not settled.** Framework application
  returns the same order-of-magnitude gap coal returns.
- **2008 at the architecture scale (ONE compact paragraph plus forward
  pointer; the full case is consolidated in the deep-case chapter):** the
  housing-bubble collapse destroyed roughly $11 trillion in U.S. household
  wealth (Federal Reserve Z.1) and led to roughly 4.1 million completed
  foreclosures (filings ran far higher; label any larger figure as
  filings/starts). The federal response deployed roughly $700B in direct
  authorization plus trillions in liquidity and guarantees, almost all
  directed at recapitalizing bank balance sheets rather than restructuring
  household debt. The scope-choice was contested at the time and documented
  since (Mian and Sufi 2014, for the response-architecture analysis, NOT as
  the source of the $11T). The next chapter returns to what the alternative
  architecture would have looked like under honest pricing. Do NOT draft the
  four-objection 2008 apparatus or the Sweden-1930s comparison here.

Close the beat: across different industries, geographies, decades, and
resources, the same mechanism produces the same gap between what the invoice
said and what the extraction actually cost; the accounting system was built
to track only one side of the ledger.

**Beat 13: What honest pricing does NOT mean (three misreadings).**
Name and answer three misreadings:
1. That honest pricing claims the extraction should never have happened. It
   does not: cheap energy, even severely mispriced energy, lifted billions
   out of poverty, and no responsible reader should accept an account that
   pretends otherwise. The narrower claim: whoever bore the cost should have
   been compensated at rates reflecting what they actually sacrificed. The
   miners, the collapsed communities, the children born into a foreclosed
   county, the generations absorbing the climate cost are real people who
   paid and are still paying. The question is who paid and whether they
   consented.
2. That honest pricing claims the market is fake. It does not: prices cleared
   transactions, money changed hands, real coal left on real rail cars. The
   claim is that the price cleared the transaction the market could see and
   did not clear the transaction actually occurring; the severed costs were a
   second transaction running alongside the first, unpriced, unwitnessed,
   binding on parties never consulted. (Antithesis-budget note: if the
   chapter spends its "is not A; it is B" constructions anywhere, the
   market-incomplete turn here is the highest-value placement; budget is ~1
   per 1,500 words chapter-wide, see §5 rule 2.)
3. That honest pricing is a ladder-pull by already-industrialized nations
   against developing economies. Take it seriously: if true it would be a
   compelling moral defeater. The response is structural: whoever created the
   historical cost owes its repayment, and differentiated transition
   timelines are a structural feature of honest accounting, not an
   afterthought. Developed nations built wealth by severing costs onto the
   global commons for two centuries; honest pricing creates the revenue to
   fund clean-industrialization pathways for developing nations as repayment
   of historical severance, not charity; solar electricity is now cheaper
   than coal across most of the developing world; the transition timeline
   should be asymmetric and the framework requires exactly that.

**Beat 14: The brief extrapolation (civilizational scale, explicitly gestured).**
Scale the finding to a bounded, explicitly gestured global figure. **The
premise must be LENS-EXPLICIT (the old "if coal is mispriced locally by 33 to
122 times" premise is RETIRED):** premise the extrapolation on the
lens-explicit finding, for example that the most conservative lens the
framework runs still returns a multiple in the double digits' lower range
(roughly 15-fold at center) and the carbon term alone runs more than a
hundredfold against the 1960 invoice, with the same shape returning across
every case examined. Then the bounded arithmetic: the global fossil-fuel
industry turns over roughly $4-5 trillion in annual revenue (IEA / BP
Statistical Review class source; pin); if full-cost pricing would multiply
that by two to three (a conservative factor given the carbon term alone), the
annual global severed cost from fossil extraction is on the order of $8-10
trillion; adding non-fossil extraction (mining, logging, fisheries harvested
above regeneration, aquifer drawdown, topsoil loss; KEEP this
above-regeneration scoping per §1.3.8) lands the global figure somewhere
between $10 and $15 trillion annually. Put the number in human scale: larger
than every government subsidy program combined, larger than all international
development assistance, larger than all charitable giving on Earth combined;
as far as the author can tell, the largest continuous wealth transfer in
human history, flowing in one direction (from communities closest to
extraction to consumers farthest away; from the future to the present; from
those with no voice in the market to those who do). **Explicitly flag this as
a gestured claim:** one sentence of supporting arithmetic against an
assertion that, taken seriously as a policy agenda, would require years of
sectoral simulation and implementation work that cannot honestly be
compressed into a framework book's closing pages. Then disarm the degrowth
misreading: GDP measures market transactions, not welfare (cleanup spending,
medical bills, and addiction-treatment spending all count as production; GDP
does not fall when people die young); honest pricing reduces GDP in the
narrow technical sense while increasing welfare in every sense the
measurement was meant to proxy, shifting the composition of activity rather
than the total. Offer the leaded-gasoline precedent (banned, refineries
reformulated, industry did not collapse, children's cognitive outcomes
improved; EPA phaseout record / CDC NHANES blood-lead decline) as the pattern
honest pricing repeats at larger scale. Conclude that the author will name
the figure and leave it there rather than compress it.

**Beat 15: The closing line (cascade of deferred questions).**
Close with the cascade of real questions the repricing raises (what happens
to energy costs in the short, medium, and new-equilibrium terms; who absorbs
the transition; what happens to a household in the bottom forty percent when
essentials rise sharply; where the pricing surplus goes and who decides;
whether the economy on the other side is still recognizably capitalist).
Affirm these questions are real and that the framework's mathematics,
simulations, and the structural necessity of a universal floor produce
specific answers, but that the answers are outside this book's scope. DO NOT
re-spend the "framework does not legislate" disclaimer here (already spent in
Beat 1) and do not narrate what the book or its chapters have done; hand the
pursuit of the deferred questions to policy-makers, scholars, communities,
and coalitions, and assert that honest accounting at civilizational scale
would reveal not a catastrophe but a more stable, more resilient economy with
a floor beneath it. End on the one worked example: a ton of coal, priced
honestly, at a floor around $510; the gap between that number and the
just-under-five-dollar invoice is the severed cost; the invoice is what the
county was paid, the severed cost is what the county bore. Hand forward to
the final two chapters (the next sketches the direction a civilization
committed to honest accounting would move; the final chapter closes with the
recurring figures recognizing each other across the distance the mechanism
was built to maintain), in one or two sentences, without self-narration
("Chapter 1 through Chapter 8 have done that" is the banned register).

**Do NOT append any "End of Chapter" marker or equivalent.**

### 2.1 Landing points Chapter 8 OWNS (must land, here, cleanly)

1. **Unpriced costs are real and measurable.** A legible per-ton number
   ($510) set against the market price ($4.71). Co-owned with the measurement
   chapter; Chapter 8 makes it concrete on one ton.
2. **The magnitude claim, lens-explicit:** the honest cost has ALWAYS
   exceeded market price, with the carbon / foreclosure term dominating every
   other component, and the gap stated per §1.2 (never a bare multiple). The
   carbon term must visibly dominate the other seven components combined.
3. **The single worked ton: the full eight-component decomposition**, summing
   exactly to $510.

Secondary landing points carried (owned elsewhere, reinforced here): the
no-villain structural posture; the framework as honest-accounting instrument
rather than polemic; the framework names its own limits (the falsification
surface, §1.3.7); the miner as the book-opening community returned to.

### 2.2 Threads relied on and threads set up

**Relied on (reference as already established; do not re-derive):**
- The combustion / climate externality tail was explicitly DEFERRED from the
  early coal case chapter; Chapter 8 (with the measurement chapter) prices
  the deferred tail via the carbon term. This thread CLOSES here.
- The McDowell magnitude was asserted in the early case chapter on a forward
  promise that THIS chapter would land it. Honor it lens-explicitly (§1.2).
- The single worked ton was promised by the early case chapter, the deep case
  chapter, the measurement chapter (the Pocahontas-seam basis), and the
  off-world chapter. Deliver the full decomposition.
- The miner as comparator / book-opening community returned to at the close.
- The measurement chapter formalized the residual-commons-value integral; the
  per-ton arithmetic here is the time-snapshot version of that summation. The
  formal integral lives in the Technical Appendix; do not reproduce it.
- The deep-case chapter promised the McDowell matched comparison, the one-ton
  full decomposition, and the thirteen-year life-expectancy gap (male-specific;
  "for men"). Deliver all three.

**Set up here (forward promises later chapters must honor):**
- Public Choice relationship developed at greater length in the next chapter
  (Beat 9).
- 2008 alternative architecture returns in the next chapter (Beat 12).
- Housing supply-side (YIMBY) objection answered in full in the next chapter
  (Beat 12; steelman relocated there per D3).
- Civilizational-scale deferred questions pursued by others / sketched in the
  next chapter / closed humanly in the final chapter (Beat 15).

---

## 3. Required citations + literature positioning

Cite in the chapter's light in-prose manner (no footnote markers; attributions
woven in). Do not fabricate any figure or attribution not anchored here or in
the canonical ledger. **Every load-bearing number carries a named external
authority; where no authority exists the number is owned explicitly as a
framework allocation on named anchors (Path A), never attributed to bare
"economists" or "studies."**

### 3.1 Empirical anchors

**Carbon arithmetic (flagship).**
- EPA AP-42 §1.1 factor 93.28 kg CO2 per mmBtu; Pocahontas-seam heat content
  ~28 mmBtu per short ton (cite USGS / EIA Pocahontas heat-content data
  explicitly; a reviewer who substitutes the 2.32 national factor would drop
  the carbon term to roughly $441, the national-basis figure).
- $190 SCC = **EPA 2023 central estimate** (Report on the Social Cost of
  Greenhouse Gases, EPA-HQ-OAR-2021-0317). EPA drew on Rennert et al. 2022
  (*Nature*), whose own central was ~$185. **Do NOT attribute $190 to
  Rennert.**

**SCC as political object (Beat 9).** $42 (interagency working group
technical support document, NOT Executive Order 12866) / $1-7 (US-only scope;
academic flag = Wagner, Anthoff, Cropper et al. 2021) / $51 restored (IWG
interim) / $190 (EPA 2023). Cite the IWG technical support documents directly
for the $42 and $51 values.

**Direct health.** Excess cardiovascular/respiratory mortality and the
more-than-a-decade life-expectancy divergence: Epstein et al. 2011 and
Hendryx & Ahern 2009; pin the exact ">10-year" figure to a named Hendryx
paper or IHME. The thirteen-year gap is **male-specific** ("for men";
all-population ~10-12 years). Black-lung life-shortening: "8-13 years of
potential life lost per decedent." Black-lung cumulative paid: "$44 billion
through 2009 (GAO/CRS)," always dated, never presented as current. Trust Fund
DEBT $5.1B as of September 2024 (DOL/GAO), distinct from cumulative-paid.

**Environmental degradation.** Reclamation-bond shortfall: bonds ~$3.8B vs
cleanup $7.5-9.8B, gap ~$4-6B, ~633,000 Appalachian acres; **single
consistent band; Appalachian Voices, *Repairing the Damage* (2021)**
(GAO-18-305 as secondary); distinct from the larger historic
abandoned-mine-land figure; nationwide ~1M acres only via OSMRE e-AMLIS.
**Mountaintop-removal epidemiology: Hendryx, Wolfe, Luo, Webb, *Journal of
Community Health* 37(2), 2012 reports an odds ratio of 2.03 (self-reported
survey); "60,000 cancer cases" is an advocacy extrapolation NOT in the paper
and must not be attributed to Hendryx; prefer the odds-ratio restatement.**
Coal-combustion mercury in North Atlantic fish: Lee et al. 2016. SMCRA 1977 =
public-record statute.

**Community disruption.** Population 98,887 (1950 Census, decennial) to
19,111 (2020, Census QuickFacts). Poverty 37.6%, median household income
$28,235, national median ~$67,521, sixteenth-poorest: Census SAIPE / ACS;
date-lock "(2022)." Drug-induced deaths 141 per 100,000 (2015) vs national
~16: CDC NCHS / WONDER (regenerate the WONDER query to cite CDC directly;
crude vs age-adjusted basis difference noted). U.S. Steel wind-down: "across
the 1980s" (J5). The $5-15/ton band: FRAMEWORK ALLOCATION on these named
anchors (no external source exists for the band; own it, §2 Beat 5).

**Lineage labor.** Opportunity Insights / Chetty et al., Opportunity Atlas
(bottom-quintile child's odds of reaching the top quintile among the lowest
in the United States; pin the McDowell county/tract data point). The $1-5
band: FRAMEWORK ALLOCATION on the named mobility data.

**Political capture.** Black-lung 1969 Act, strike-driven (1968 Farmington
disaster; West Virginia Black Lung Association): MSHA record / Derickson
1998. Mine workers' union "reportedly declined to press": KEEP the hedge
(provenance is an open author-confirm, §6). Fossil-fuel lobbying: OpenSecrets
(oil and gas ~$124-150M; broader energy sector ~$435M, 2024); date-lock the
cycle and specify which scope is cited.

**Temporal displacement.** EIA energy-intensity series (energy per real GDP,
1973 to the 1990s); specify metric and endpoints rather than a bare "50%."

**Cross-case sweep.** Deepwater: Macondo 40-60M barrels = projected lifetime
production / reservoir estimate, NOT spill (court-found release ~3.19M
barrels); 17-26M tons CO2; ~$3-5B carbon tail at $190. Libby: per TA §9.5
(see Beat 12 and open call §6). Baotou: no computed multiple (TA §11.4);
remediation ~$5-15B documented if needed. Valdez: eleven million gallons;
generic invocation only (dangling-reference rule). Tar sands: Treaty 8
(1899) + the three named First Nations = public record; health/contamination
claims attributed to O'Connor 2006 / Alberta Cancer Board 2009 / the Mikisew
Cree study, causation alleged/contested. 2008: Federal Reserve Z.1 ($11T);
CoreLogic (~4.1M completed, through 2012); Treasury (TARP $700B authorized);
Mian & Sufi 2014 *House of Debt* (response-architecture argument only).
Housing: Harvard JCHS *America's Rental Housing 2024* (cost-burdened share;
date-lock). Global fossil revenue $4-5T/yr: IEA / BP Statistical Review class
source (pin). Leaded gasoline: EPA phaseout record; CDC NHANES blood-lead
decline.

### 3.2 Literary lineage (Chapter 8 OWNS this in full; Beat 7)

RATIFIED structural decision (action-list A1b; supersedes an earlier
one-sentence plan). Chapter 8 renders the full four-author lineage plus the
author's provenance disclosure. It must read as a substantive owned passage,
NOT a rhetorical flourish compensating for the small dollar figure. An early
chapter establishes the canonical "the pricing is new, the move is old"
framing once; do NOT reword or duplicate that exact framing; render the
lineage at greater length in fresh prose credited to the same tradition.

The master interpretive move the lineage names: pricing what hides behind a
mask or veil; Black American writing carried this work for over a century.
Render each contribution distinctly, in fresh prose:

- **Paul Laurence Dunbar, "We Wear the Mask" (1896).** Dunbar named the
  STRATEGY of survival: the mask that grins and lies, a debt paid to human
  guile. The miner told the dust is better now is wearing the same mask. The
  framework's addition: the mask is not the wearer's alone; it belongs to the
  system that produces the disease at industrial scale and asks the wearer to
  grin while it does. Public-domain; the title and a short accurate line may
  be quoted. **Quotation boundary discipline: the poem's own punctuation
  includes a dash; select the quotation boundary so the quoted text carries
  no em-dash (for example, end at "...and shades our eyes" or quote only the
  first line), because the zero-dash rule applies to the chapter file as a
  whole and is grep-verified.** Verify the verbatim text against the
  canonical poem.
- **W.E.B. Du Bois, *The Souls of Black Folk* (1903).** Du Bois named the
  CONDITION beneath Dunbar's strategy: the veil and the doubled
  consciousness, always seeing oneself through the eyes of a world that looks
  on in contempt.
- **Frantz Fanon, *Black Skin, White Masks* (1952).** Fanon carried the
  mask-analysis into the colonial and economic register, the register nearest
  the framework's extraction-community cases.
- **Ralph Ellison, *Invisible Man* (1952).** Ellison gave the long-form
  NARRATIVE of life under the mask: seen by everyone and witnessed by no one.

Then the framework's own addition: the cost-accounting mechanism by which the
mask remains structurally necessary, the ledger that counts what the
tradition described, and to whom.

**Author's first-person provenance disclosure (REQUIRED).** Credit the
author's own interpretive instinct (the "masking" framing carried from an
information-security background, where masking names hiding a true value
behind a presented one) BACK to this tradition: in the author's voice, in
fresh prose, to the effect that he wants the move credited to that tradition,
because that writing saw the human cost of the hidden ledger long before he
had a spreadsheet for it. Genuinely first-person and modest; it credits the
lineage, it does not claim it.

**Secondary lineage credits (Beat 9):** reparations-economics tradition
(actor-and-coalition vocabulary) and Public Choice / rent-seeking tradition
(the extractor's reasoning), vocabulary-not-endorsement framing, forward
promise to the next chapter. The chapter as a whole instantiates the Harvey
"accumulation by dispossession" relationship along its PRICING dimension; you
need not name Harvey in running prose (no citation roll-calls); the chapter's
whole move, "the diagnosis exists; this adds the number," is that
relationship made concrete.

---

## 4. TA-state method canon as it applies to this chapter

Merged 2026-06-09/10; verified against
`manuscript/technical-appendix/TechnicalAppendix_v2.0.0.html` 2026-06-10.
Every draft MUST match. The chapter never reproduces TA apparatus (no Greek
letters, no parameter intervals, no regime names in running prose); it must
simply never CONTRADICT the TA.

1. **Three Ways (TA §3.4/§3.6).** Methods 1 and 3 are the two value
   estimators of what was lost (Method 1 prices substitution; Method 3 prices
   option-bearing scarcity); their convergence range is the well-supported
   estimate. Method 2 reads the realized BOND (what a polity actually
   internalized: forward, Norway's fund; backward, restitution actually paid)
   and thereby sets a revealed LOWER BOUND, not a third estimate. **"Three
   independent estimates converge" is RETIRED.** Chapter-register phrasing
   when the measurement chapter is invoked: two independent ways of pricing
   what was lost land in the same range, and what polities have actually paid
   back sets a floor beneath both.
2. **IPG lens-explicit only (§1.2 above).** Retired: bare 33-122x, ~50x,
   555x, 50-555x, the stray "120 times."
3. **Method 3 construct (background; appendix-resident).** Quasi-option value
   (Arrow-Fisher/Henry): market value times a scarcity multiplier times an
   irreversibility premium, no free exponent. McDowell M3 ~$340-3,670/ton,
   center ~$1,115; M3 gap 8.5-26x center ~15x, price-independent. The dollar
   bands stay OUT of chapter prose; only the plain-English "most conservative
   lens" anchor (§1.2) enters.
4. **Norway (guard; Ch 8 need not touch it).** If Norway is invoked at all:
   the fund's effect is IRREVERSIBILITY-REDUCTION (restoration optionality),
   NOT rent-capture; ~$48/BOE realized is the Method-2 reading; the fiscal
   rule is the 2017 revision at 3% (the 2001 rule was 4%); per-capita
   ~$390k. Never describe Norway as having "captured the rent."
5. **Scope correction (§1.3.8).** Severance positive only when consumption
   forecloses faster than restoration; renewables sever only above
   regeneration; zero within restoration; the floor rests on scarcity
   dynamics, not physical finiteness. No "all extraction severs costs"; no
   renewables-harmony inference.
6. **Backward direction (guard).** The backward ledger's three states
   (Zero / Filled / Open; Open is neither Zero nor unpriceable) live in TA
   §5.5; the reef is the volume's single computed backward case (§11.12,
   merge-held until the waterman chapter prices it): Chapter 8 does NOT
   introduce backward-case computations. Coercion / reparations pricing: the
   Open slot; FIRST-PERSON ABSTENTION voice only (the author declines, for
   himself, to assign a figure for a group he is not part of; no
   standing-gatekeeping language like "theirs to enter" or "only the
   affected"); NEVER a coercion/reparations dollar figure from the framework;
   Darity field figure $14T (From Here to Equality 2nd ed / JEP 2022) only
   where a figure must be cited, attributed to the field.
7. **Pinned dollar labels (book-wide).** $4.71 = 1960 mine-mouth (EIA);
   $496 = McDowell carbon term ONLY; $510 = 8-component honest TOTAL;
   $441 = national-basis carbon; $504-518 = four-component floor. Black lung
   always dated (§3.1). $108T Social Security disavowed. $11T = Federal
   Reserve Z.1. Foreclosures ~4.1M completed. U.S. Steel exit "across the
   1980s." McDowell 2020 population ~19,000 / "under 20,000."

---

## 5. Prose rules (HARD REQUIREMENTS; verified corpus-wide 2026-06-10)

1. **ZERO em-dashes and en-dashes in prose.** Hyphens only, and only inside
   numeric ranges ("$504-518," "8.5-26 times"). Where you would reach for a
   dash: comma, period, colon, parentheses, or restructure. This applies to
   the whole chapter file including quotations (see the Dunbar quotation
   boundary, §3.2). **Verify with grep before returning.**
2. **Antithesis budget:** "Not X. It is Y." / "is not A; it is B"
   constructions at most ~1 per 1,500 words. Vary paragraph endings; some
   paragraphs simply end; NO aphorism-epigram at every paragraph or section
   close. (Recommended spend: the market-incomplete turn in Beat 13. The
   "almost certainly an undercount" close appears at most once chapter-wide.)
3. **NO self-narration:** never narrate what the chapter, book, or framework
   is doing or about to do ("Hold onto that...", "The chapter has done its
   work," "I want to say / engage / be specific...", "this chapter is
   about..."). The disclaimer "the framework does not legislate" may appear
   AT MOST once (Beat 1). "The framework" is never the subject of consecutive
   sentences.
4. **NO white-paper register:** terminology defenses = one sentence plus a
   Technical Appendix pointer, never a digression; method description at
   chapter register (no Greek-letter regime names or parameter intervals in
   running prose); numbers as numerals (no spelled-out number walls); NO
   workshop vocabulary (steelman, pressure-test); no archival/process
   vocabulary ("named ... in the record").
5. **Named external authority on every load-bearing number** (never bare
   "economists" / "studies"). If the substrate has no namable source,
   restructure to not need the number (Path A) and leave a structure-note
   comment. (Applied in this brief at Beats 5 and 7: the per-ton allocations
   are owned as framework estimates on named anchors.)
6. **One person or sensory anchor opens every technical stretch,
   substrate-safe ONLY** (inventory at the head of §2). **NO INVENTED
   FACTS:** every biographical detail, scene element, quoted speech, number,
   date, and name comes from this brief, the listed substrate, or the
   canonical chapter; gaps get `<!-- structure-note: ... -->` comments, never
   invention. Preserve all consent/anonymization decisions. (Hard rule;
   reputational asymmetry: a shipped fabrication propagates from book to
   future work and is not recoverable. When in doubt, generalize.)
7. **Register models:** the harbor frame of
   `manuscript/chapters/Chapter_10_CommonBonds.md` (opening and closing) and
   the Biggie section of `manuscript/chapters/Chapter__3_TheWaterman.md`.
8. **Substance drives length; do not pad, do not cut substance.** Word floor
   6,000, no maximum; the eight-component walk, the full lineage passage, the
   rebalanced cross-case sweep, the three-misreadings defense, and the
   extrapolation clear it naturally.

Additional house discipline carried from v1: Globally Inclusive Plain English
(no US-centric idiom that does not travel; expand or avoid acronyms; spell
"Intergenerational Pricing Gap" in full, never an acronym); no
framework-jargon leakage (no "Four Gates," "Commons Inversion Test,"
"C-sub-i," "IPG" as running-prose labels; describe the operations); no
scaffolding language (no "Option A/B," "Phase," "RATIFIED," "PROPOSED,"
INCLUDE/EXCLUDE glyphs, "TODO," "TK"); concealment-pattern register present
without lecturing (the reader feels the unmasking, is not taught a taxonomy
of it); no-villain, honest-accounting, non-partisan tone throughout; no "End
of Chapter" marker.

---

## 6. Open author calls (carried forward + new)

**Carried forward from v1:**
1. **J5 hard year:** the U.S. Steel McDowell/Gary wind-down hard year (1986
   vs 1990s) still needs a primary source (Gary/McDowell history, U.S. Steel
   records, contemporaneous news archive); until locked, "across the 1980s"
   only. The income-drop figure also needs BEA local-area personal income.
2. **UMW / Lewis "reportedly declined to press":** provenance needs a
   labor-history source or stays explicitly hedged (AUTHOR-CONFIRM).
3. **Valdez dangling reference:** case substance lives in the measurement
   chapter; the sweep treats it generically. A future pass may either build
   the case where it lives or keep the generic invocation.
4. **Black-lung anchor pin:** the "$44B through 2009" document (likely CRS
   R45261) or a current DOL cumulative with its year.
5. **Drug-death rate:** regenerate the CDC WONDER query (McDowell FIPS 54047)
   to cite CDC directly rather than the Rockefeller Institute intermediary.
6. **Walmart 2016 departure:** low-stakes; pin to a news archive or omit.
7. **1950 Census 98,887:** PDF visual confirm before print.

**New in v2:**
8. **Ledger-vs-TA RCV-integral band discrepancy (FLAGGED, not resolved
   here):** the canonical figure ledger records the RCV-integral lens as
   67-134x; the TA's current text (§9.5/§11.6/§11.11, verified 2026-06-10)
   reads 61-115x ($525-540/ton across the contemporary ~$8.66 and 1960 $4.71
   price bases). This brief follows the TA per instruction. The ledger owner
   should sync the ledger line (or correct the TA) in a dedicated pass; the
   draft must not attempt to reconcile.
9. **Libby multiple:** the prior draft's "forty to eighty" predates the TA
   closeout; TA §9.5 now reads 65-100x (damage lens; 57-111x across lenses).
   The brief directs the TA value or a qualitative phrasing; author to
   confirm the preferred presentation.
10. **Hendryx restatement choice:** odds ratio 2.03 attributed to Hendryx
    2012 (recommended) vs an explicitly-labeled advocacy extrapolation for
    "60,000." The draft should use the odds ratio unless the author directs
    otherwise.
11. **Framework-allocation labeling (Beats 5 and 7):** the $5-15 community
    band and $1-5 mobility band are now owned in prose as framework
    allocations on named anchors (Path A applied). If the author prefers
    external anchoring, commissioning a regional-decline costing source is
    the alternative; until then the prose must not imply one exists.
12. **Housing compression (D3):** the ~300-word housing block depends on
    Chapter 9 actually receiving the full supply-side steelman (Glaeser /
    Gyourko / Schuetz / JCHS taxonomy / RealPage chronology). The Chapter 9
    brief must protect that hand-off; if Chapter 9's plan changes, this
    deferral needs re-deciding.
13. **Trust Fund debt figure:** v2 uses $5.1B as of September 2024 (DOL/GAO)
    per the merged canon, superseding v1's "$4.5B (2021)" J4 anchor; only
    relevant if the draft invokes the debt figure at all.

---

---

## ADDENDUM v3 2026-06-16 :: matrix fills + structural specs

**How to use this addendum.** Everything in sections 0-6 above stands. This
addendum is purely additive: it converts two matrix-positioning obligations
into REQUIRED beats and tightens two structural rules into HARD constraints,
and it pins the prior winning draft's strengths so a fresh blind draft rebuilds
them. The discipline-correct way an owed positioning beat reaches the chapter is
to be SPECIFIED in this brief and BUILT IN-REGISTER by the drafter from scratch.
Do NOT graft any of this onto an existing draft and do NOT reproduce any prior
draft's sentences; compose all prose fresh, in the chapter's plain-English,
no-villain, honest-accounting register, obeying every §5 prose rule (above all:
ZERO em-dashes and en-dashes; named external authority on every load-bearing
number; no white-paper register; no citation roll-calls; no self-narration).

Source authority for the fills: the re-mapped contribution matrix
(`manuscript/ledgers/_contribution-matrix-lens_v2_2026-06-15.md`) and the matrix
re-map gap list (`tools/audits/matrix-remap-gap-list_2026-06-15.md`, Ch8 items
1-2). The drafter does NOT need to read those files; everything required is
restated here.

### A. REQUIRED matrix-fill beats

#### Fill 1 (gap-list Ch8 item 2) :: the "it's only Pigou / just a rebranded externality" objection AND its rebuttal. **STATUS in prior drafts: UNANSWERED. Now REQUIRED.**

- **Relation to the named work: EXTEND.** The framework EXTENDS Pigouvian
  externality theory (A.C. Pigou, *The Economics of Welfare*, 1920) into a
  setting it could not reach. This is an extend-relation, not a parallel and not
  a contradiction: the chapter does not say Pigou was wrong; it says the
  externality frame stops short of what the inversion prices.
- **The objection to RAISE, in a hostile reader's own voice (one short
  paragraph).** Have the skeptic say, in plain words, that none of this is new:
  pricing the uncounted damage of a transaction is simply pricing its
  externalities, which economics has done since Pigou; the eight components are
  externalities with new names; the framework has relabeled a century-old idea
  and dressed it as discovery. Raise it as the strongest version of itself
  (it is not a weak objection), in the no-villain register, without sarcasm.
- **The rebuttal, ON THE CHAPTER'S OWN TERMS (this is the load-bearing move;
  do it WITHOUT a citation roll-call, per §5 rule 4 and the GIPE register).**
  Answer with the chapter's own machinery, not by listing thinkers:
  1. The externality frame prices a cost only once a market or a regulator has
     already decided the cost EXISTS and is someone's to bear; until then the
     externality frame carries that cost at zero. The framework's first move is
     the inversion that makes a hidden cost legible BEFORE any market prices it:
     it asks what the taking forecloses, and prices the foreclosure, not merely
     the measured spillover. The foreclosure / option-value layer (the carbon
     term's future-use tail in Beat 6; the lineage-labor and temporal-displacement
     components) is exactly the part a Pigouvian externality leaves at $0 until
     scarcity makes it legible, which is often after the resource is gone.
  2. State the distinction the chapter already owns: an externality is a
     spillover a transaction imposes on a bystander; what this chapter prices is
     a SECOND transaction running alongside the first, binding on parties never
     consulted (Beat 13's market-incomplete turn already carries this; the
     rebuttal should point the reader at that idea, not re-derive it). The
     externality framing asks how much to charge for the spillover; the
     inversion asks who else was a party to the deal and was never paid.
  3. The move the externality frame does NOT contain is the falsification
     surface (§1.3.7): the same machinery returns ZERO when a perfect substitute
     exists or when use stays within what the commons can restore. A relabeling
     could not do that; an externality charge has no built-in zero condition of
     this kind. The fact that the framework prices the McDowell ton at a floor
     and the renewable-within-regeneration ton at zero is what tells you it is a
     measurement instrument, not a synonym for "externality."
- **Attribution discipline for this fill.** Pigou is named ONCE, where the
  objection is raised (the objection is literally "it's only Pigou," so the name
  is load-bearing there and earns its single appearance). Do NOT add Coase,
  Coasean readers, law-and-economics, or any roster around it; the
  port-from-essay substance (the Public Books "externality-vs-cost-severance"
  distinction and "the legal architecture plus the power asymmetry" framing)
  enters as the chapter's OWN plain-English point, unattributed, not as a cited
  borrow. No "as economists have long noted"; no bare "studies."
- **Placement.** Natural homes: at or just after Beat 6 (the carbon /
  foreclosure term is where option-value beyond measured spillover is most
  visible) OR woven into Beat 13's misreadings defense as a fourth named
  misreading-and-answer. Pick ONE home; do not split it across both. If it lands
  in Beat 13, it does not consume the antithesis budget unless it uses an
  "is not A; it is B" turn (budget ~1 per 1,500 words, §5 rule 2). Keep it tight:
  one paragraph to raise, one to two to answer.

#### Fill 2 (gap-list Ch8 item 1) :: resolve the Hotelling / Pigou / Daly / Weitzman attribution AT THE CHAPTER'S REGISTER. **STATUS in prior drafts: the chapter does the foreclosure-pricing / conservative-floor / return-to-zero WORK with ZERO attribution. Now a REQUIRED, register-bounded resolution.**

This is the chapter-level instance of the book-wide "matrix work with zero
attribution" gap. The resolution is NOT a roll-call and NOT a parade. The brief
bans citation roll-calls (§5 rule 4); this fill is satisfied by naming AT MOST
the one or two figures who are genuinely load-bearing at a specific sentence,
ONCE each, where the work is actually happening, and leaving the rest to the
measurement chapter and the Technical Appendix (which carry the full lineage).
The relations, so the drafter knows what each name would be doing if used:

- **Pigou (1920) :: EXTEND.** Already consumed by Fill 1 (named once at the
  objection). Do NOT name Pigou a second time elsewhere. Fill 1 is the chapter's
  whole Pigou treatment.
- **Harold Hotelling (1931), Hotelling Identity :: ADD-TO / EXTEND.** The bridge
  to standard resource economics (the honest price equals the standard
  scarcity-rent accounting PLUS the severed-cost term the standard accounting
  omits). This bridge is the measurement chapter's and the Technical Appendix's
  to own in full; in THIS chapter it may be gestured at in ONE plain-English
  sentence (the price a resource economist would already recognize, plus the
  part their accounting leaves out) and Hotelling named ONCE only if that
  sentence is actually built. If it is not built, Hotelling is NOT named here:
  do not name a thinker whose relation the chapter does not work.
- **Herman Daly :: ADD-TO / OPERATIONALIZE-QUANTITATIVELY.** Daly's relation is
  "the warning becomes an invoice": ecological economics warned that throughput
  beyond regeneration is uncounted; the framework turns the warning into a
  per-ton number. If used, name Daly ONCE at the scope-correction / 
  within-restoration idea (Beat 1 or the Beat 6 zero-condition), in one clause,
  as the tradition the per-ton accounting operationalizes. Optional, not required.
- **Martin Weitzman :: ADD-TO / ADOPT-DIRECTLY.** The conservative-by-construction
  posture (declining / fat-tail discounting biases the estimate DOWNWARD, so the
  floor is conservative). If used, name Weitzman ONCE only where the chapter
  asserts the number is a floor and the truth is very likely larger (the
  RCV-integral pointer in Beat 11, or the conservatism rule in Beat 2). Optional,
  not required.
- **HARD CEILING on this fill.** Across the WHOLE chapter, the Fill-2 names
  (Hotelling, Daly, Weitzman) plus the Fill-1 Pigou name total AT MOST four
  proper-name appearances, each ONCE, each at the exact sentence where its
  relation is load-bearing. Pigou is required (Fill 1). Of Hotelling / Daly /
  Weitzman, name only those whose relation the prose actually performs in a
  sentence; the minimum acceptable is naming NONE of the three IF the chapter's
  plain-English machinery already carries the bridge / operationalization /
  conservatism without them, because the measurement chapter and the Technical
  Appendix carry the full lineage. The failure mode to avoid in BOTH directions:
  (i) leaving the work entirely voiceless (the prior state), and (ii) a
  four-name parade that reads as referee-proofing grafted from essay register
  (the §5 rule-4 white-paper failure; compare the Ch7 Bostrom/Ord/MacAskill
  parenthetical the audit flagged as a clunk). The target is "named once where
  load-bearing, not a parade."
- **No roll-call, restated for this fill.** Never a sentence of the form "as
  Hotelling, Daly, and Weitzman variously showed." Never a parenthetical list of
  surnames. Each name, if it appears, sits inside a sentence that is doing the
  pricing work, crediting exactly one relation.

### B. REQUIRED structural specs

#### Spec 1 :: VARY the per-component close formula (HARD; supersedes nothing but tightens Beats 3-10).

The eight-component walk (Beats 3-10) must NOT end its components on a uniform
refrain. Specifically BANNED as a repeated close:
- "the walk prices $N a ton" / "the walk takes $N a ton" and any single-template
  variant of it (the prior runner-up draft used this 7 times; it accumulated into
  affect-neutral bookkeeping and was the named reason it was not promoted).
- "almost certainly an undercount" as a recurring component close (§2 already
  caps this phrase at AT MOST ONCE chapter-wide; this spec reaffirms the cap and
  extends the principle to ANY templated close).
- "Take the low end" / "Take $1" / "Take the low end" as a recurring close (the
  promoted draft carried this 3x; vary at least two of any such cluster).

Positive requirement: each of the eight components ENDS DIFFERENTLY. Acceptable
endings, mix freely so no two adjacent components close the same way: end on the
concrete McDowell anchor (the creek, the house in the hollow, the West Fork);
end on the running-total reconciling clause where the brief already places one
(after Community Disruption, after Foreclosure); end on the per-ton figure
stated plainly with no epigram; end mid-thought into the next component; end on
a single declarative consequence. The per-ton FIGURE for each component is
mandatory and unchanged (the §1 ledger governs); it is the CLOSING CADENCE that
must vary, not the arithmetic. A blind drafter should be able to read back the
eight closes and find no two built on the same template.

#### Spec 2 :: FIDELITY HARD CONSTRAINT: bar invented-class assertions about what real people say or do beyond the documented record.

This is a hard rule, not a preference, and it is grep-and-read enforced. Across
the whole chapter, do NOT assert what a class of real people SAYS, DESCRIBES,
REPORTS, FEELS, or DOES unless that assertion is in the brief, the listed
substrate, or the canonical chapter as documented record. BANNED CLASS
(the prior winning draft carried exactly one line of this class and it required
a mandatory cut): generalized-testimony framings such as "men who have it
describe the same progression," "miners will tell you," "the families say,"
"everyone in the county knew," or any sentence that puts words, reports, or
described experience into the mouths of an undocumented class of real people.
- The underlying FACT may still be rendered if it is documented: render it as
  the documented course / the record / the data, NOT as reported speech. Example
  of the correct transform: instead of "Men who have it describe the same
  progression: first the hills get steeper, then the stairs do," write the
  clinical / documented course itself ("The progression is the same: first the
  hills get steeper, then the stairs do"), with no attribution to anyone's
  testimony. The image survives; the invented attribution does not.
- This sits under and reinforces §5 rule 6 (NO INVENTED FACTS) and the project's
  no-invented-factual-claims hard rule. It also covers attribution drift: do NOT
  attach a named institution (for example "(NIOSH)") to a brief-anchored figure
  the brief gives UNATTRIBUTED; if the brief does not name the source, the prose
  does not either. When the documented record does not anchor a piece of texture,
  generalize or cut; never invent the attribution. Reputational asymmetry
  applies: a shipped fabrication propagates from book to future work and is not
  recoverable.

### C. PRESERVE :: the prior winning draft's strengths (rebuild these from scratch; the drafter will NOT see that draft)

These are pinned so a fresh blind draft does not regress what the prior
comparison judged best. Build each IN-REGISTER from this brief; do not reproduce
any prior sentence.

1. **The full eight-component per-ton ledger walk** (Beats 3-10), each component
   grounded in a concrete McDowell-specific reality, the running total visible
   throughout, the carbon / foreclosure term (Beat 6) as the mid-chapter
   gut-punch that visibly dominates the other seven combined. Summing EXACTLY to
   $510 per the §1 ledger. This is the chapter's spine and must land cleanly.
2. **The Lineage Labor passage with the full Dunbar / Du Bois / Fanon / Ellison
   lineage** (Beat 7, owned in full per §3.2), rendered at full depth as a
   substantive owned passage, NOT a compensating gesture for a small dollar
   figure, including the author's first-person information-security "masking"
   provenance credited BACK to that tradition (in fresh first-person prose;
   obey §5 rule 3, do NOT use the banned "I want to say / I want to name" opener
   form; credit the lineage modestly without claiming it). This beat's
   Dunbar-to-Ellison plus Opportunity-Insights mobility texture is the chapter's
   best material; protect it at full depth.
3. **The three-misreadings close** (Beat 13: extraction-should-never-have-happened;
   the-market-is-fake; the-ladder-pull), each named and answered, with the
   market-incomplete turn as the highest-value antithesis placement. If Fill 1
   lands here, it is a fourth named misreading-and-answer in the same register.
4. **The pinned figures, stated exactly and lens-explicitly:** $496 = carbon
   term ONLY; $510 = the 8-component honest TOTAL; 2.61 metric tons CO2 per short
   ton (McDowell calibration, Pocahontas heat content cited so the 2.32 national
   factor cannot be swapped in); $4.71 = 1960 mine-mouth ("just under five
   dollars"); the Intergenerational Pricing Gap spelled in full, bound to a named
   lens and price basis in the same sentence, never a bare multiple (§1.2 / §4).

### D. Prose rules reaffirmed (UNCHANGED from §5; restated because they govern every line of the fills above)

- **ZERO em-dashes and en-dashes** anywhere in the file, including any quotation
  (Dunbar quotation boundary per §3.2). Grep-verify before returning.
- **Positioning is PRIMARY.** The chapter must illustrate how the book SUPPORTS,
  CONTRADICTS, and ADDS TO the adjacent literature; beat-capture is secondary.
  Fill 1 is an ADD-relation made legible (the framework adds what the externality
  frame leaves at $0); Fill 2 is the EXTEND / ADD-TO lineage made legible at
  register. The lineage passage (Beat 7) is the positioning center and carries
  the supports-then-adds turn.
- **Felt pressure / no flatness.** Score aliveness as you draft; the chapter's
  power is the magnitude being FELT, not merely stated. The known flat zones to
  guard (compliance prose) are the Beat-11 lens block and the 2008 block: let the
  "more than a hundred times" landing breathe before the lens taxonomy arrives;
  give the 2008 sweep one human-scale clause amid the figure inventory.
- **No self-narration** (§5 rule 3): never narrate what the chapter / book /
  framework is doing or about to do; "the framework" is never the subject of
  consecutive sentences; the "framework does not legislate" disclaimer appears
  AT MOST ONCE (Beat 1), never re-spent in Beat 15.
- **No invented facts** (§5 rule 6 + Spec 2 above): every biographical detail,
  scene element, quoted or reported speech, number, date, name, and institutional
  attribution comes from this brief, the listed substrate, or the canonical
  chapter; gaps get `<!-- structure-note: ... -->` comments, never invention.
- **Figures per the canonical ledger** (§1 + §4): carry every pinned figure
  EXACTLY; verify the eight-component sum to $510 yourself; obey the
  walk-range-vs-summary-figure discipline and the running-total reconciling
  progression ($8 -> $504-518 -> $510).
- **No canonical grafting.** Compose all prose fresh from this brief. Do not
  paste, lightly edit, or structurally trace any prior draft or the canonical
  chapter; do not graft any owed beat after drafting. Every owed beat above is
  specified here precisely so it can be BUILT in-register from scratch.

---

*End of brief.*


## ADDENDUM 2026-06-18 :: cross-session coordination (for the WHOLE-CLOTH rebuild)
Whole-cloth Ch 8 rebuild. Because this replaces the canonical, place inserted material BY CONTENT, not line number.
H1-H5 matrix insertion targeting Ch 8 (drafted prose in tools/workstream-handoffs/matrix-h1-h5-ratified-insertions-handoff_2026-06-18.md):
- Insertion K (H5 attribution pull-up) :: append the Hotelling/Costanza lineage sentence to the option-value-foreclosure material. HELD-gate note in the handoff: it attributes Hotelling's 1931 economics; respect that gate. Costanza was 0 book-wide, so this is the credit.
Keep consistent with the brief's own fills (the just-rebranded-externality objection; vary the component-close formula; the fidelity constraint barring "what real men say"-class assertions).
