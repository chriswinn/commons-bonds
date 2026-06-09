# Corpus-Wide Primary-Source Register (TA + Chapters)

**Created:** 2026-06-08
**Trigger:** author directive — "find a primary source for everything in the citations; never cite ourselves." Corpus-wide scope (TA + Ch 1–10), confirmed.
**Method:** read-only enumeration of every empirical figure in the TA + 10 chapters (3 agents), then primary-source hunt (4 web-research agents). HARD RULE applied throughout: no invented sources; real primary source + URL or marked UNVERIFIABLE; framework-computed numbers (IPG/RCV/CS) are NOT sourced — they get honest "framework-computed, derivation shown" labeling.
**Companion artifacts:** `ta-number-provenance-ledger_2026-06-07.md` (TA figures) · `ta-number-provenance-DECISION-MEMO_2026-06-07.md` (judgment items) · the TA self-citation kill-list (LIST A/B, below §4).
**UPDATE 2026-06-08 (§6):** mined `research/outreach/subjects/{darity,colden,cbf,moore}/` (4 agents, author steer). The **Darity "with-citations" Ch5/Ch6/TA docs already attribute most empirical figures to agency sources** (inline only — TA §18 bib is theory-only). New §6 records those + the Chesapeake primary sources from Colden/Moore/CBF + reconciliation flags. **$44B status changed — see §6 + §3.**

**STATUS:** sources verified this session; **NOT yet applied to chapter prose** (chapters are end-user-facing prose → author/chapter-session pipeline + ratification). §23 bib updated with the new entries. The CORRECTIONS in §2 are the highest-value findings — several are factual errors, not missing cites.

---

## §1. VERIFIED PRIMARY SOURCES (bibliography-ready; figure → source → URL → confidence)

### 1A. McDowell County / Appalachia
- **Population 98,887 (1950) → 19,111 (2020).** US Census Bureau, *Census of Population 1950, Vol. II WV* (https://www2.census.gov/library/publications/decennial/1950/pc-02/pc-2-02.pdf) + QuickFacts McDowell Co. (https://www.census.gov/quickfacts/fact/table/mcdowellcountywestvirginia/PST045224). HIGH. *(1950 PDF didn't machine-parse — visually confirm the table before print.)*
- **Male life expectancy ~63.5 vs national ~76.5 (≈13-yr gap).** Dwyer-Lindgren et al. (IHME), *JAMA Internal Medicine* 2017 (https://jamanetwork.com/journals/jamainternalmedicine/fullarticle/2626194; PMID 28492829); exact county figures in the IHME county dataset (healthdata.org). MED-HIGH. *(Regenerate the IHME county profile to cite the exact 63.5/76.5 directly.)*
- **Drug-overdose death rate ~141/100,000 (2015) vs national ~16.** CDC NCHS / CDC WONDER (drug-induced mortality, McDowell FIPS 54047). MED. *(Figure surfaced via Rockefeller Institute analysis; regenerate the CDC WONDER query to cite CDC directly.)*
- **Poverty ~37.6%; median household income ~$28,235.** US Census ACS 5-yr via QuickFacts (URL above). HIGH. *(Confirm vintage year matches the book's stated year.)*
- **1960 bituminous mine-mouth coal price ≈ $4.71/short ton (all-coal $4.83).** EIA Total Energy Table 7.9 / ptb0709 (https://www.eia.gov/totalenergy/data/annual/showtext.php?t=ptb0709). HIGH. **→ the book's "$4.50" is LOW; see §2.**

### 1B. Black Lung + reclamation
- **~$865M benefit obligations shifted to public by 3 coal bankruptcies (Alpha, James River, Patriot), 2014–2016.** GAO-20-21, Feb 2020 (https://www.gao.gov/products/gao-20-21). HIGH.
- **$5.1B Trust Fund outstanding debt; $15.4B projected by 2050; borrowing since 1979.** GAO-18-351 + GAO-19-622t + Brookings 2021. HIGH. **→ "$44B cumulative payouts" remains UNSOURCED; see §3.**
- **Reclamation: >633,000 acres; cleanup $7.5–9.8B; bonds ~$3.8B; gap ~$4–6B.** Appalachian Voices, *Repairing the Damage*, 2021 (https://appvoices.org/coal-impacts/repairing-the-damage/). HIGH. *(Already in §23.)*
- **MTR cancer odds ratio 2.03** (NOT "60,000 cases"). Hendryx, Wolfe, Luo, Webb, *J. Community Health* 37(2):320–327, 2012 (DOI 10.1007/s10900-011-9448-5). HIGH for OR; **"60,000 excess cases" is an advocacy extrapolation, UNVERIFIABLE — see §3.**

### 1C. Chesapeake fisheries
- **Oyster ~15M bushels/yr (1880s, Maryland portion); ~1–2% of historic population remains.** Maryland Sea Grant / Horn Point (UMCES) oyster history (https://hatchery.hpl.umces.edu/oyster-history-in-the-chesapeake-bay/) + NOAA Fisheries oyster restoration. HIGH for 15M + "1–2% remains." **The "<200,000 bushels (1990s) / 99% decline" endpoint is MED — source a specific MD DNR landings table or reframe to NOAA's "1–2% of population." See §2.**
- **Rockfish young-of-year 2.0 (2024) vs long-term avg 11.0; 6th consecutive poor year.** MD DNR, Oct 17 2024 (https://news.maryland.gov/dnr/2024/10/17/results-of-chesapeake-bay-2024-young-of-year-striped-bass-survey-show-little-change/). HIGH (exact).
- **Rockfish moratorium 1985–1989/90; recovered 1995.** NOAA Fisheries (https://www.fisheries.noaa.gov/feature-story/checking-chesapeake-bay-striped-bass) + ASMFC Amendment 5. HIGH.
- **Blue crab ~238M (2025 Winter Dredge Survey); 2nd-lowest since 1990 (lowest 226M, 2022).** MD DNR, May 22 2025 (https://news.maryland.gov/dnr/2025/05/22/...blue-crab-winter-dredge-survey/). HIGH (exact).
- **Menhaden Chesapeake reduction cap 51,000 mt.** ASMFC **Amendment 3 (adopted 2017, implemented 2018)** (https://asmfc.org/news/fact-check/atlantic-menhaden-faqs/). HIGH. **→ NOT "2006"/"reduced 2017"; see §2.** Omega Protein/Reedville confirmed. 2025: ASMFC Addendum II initiated to cut Bay cap up to 50%.
- **Watershed >64,000 sq mi; 6 states + DC.** Chesapeake Bay Program (https://www.chesapeakebay.net/discover/watershed). HIGH (exact).
- **Tangier: settled 1700s; ~66.75% landmass lost since 1850; erosion 0.5–1.3 m/yr (paper).** Schulte, Dridge, Hudgins (USACE), *Scientific Reports* 5:17890, 2015 (https://www.nature.com/articles/srep17890). HIGH for paper. **"~15 ft/yr" is USACE-via-press (exposed western shore), exceeds the paper's ~1.7 ft/yr average; "~2 sq mi" vs paper's ~1.2 sq mi remaining land — see §2.**
- **Maryland oyster adults 2.4B (2005) → 7.6B (2024) ≈ tripled.** MD DNR stock assessment, May 19 2025 (https://news.maryland.gov/dnr/2025/05/19/...oyster-abundance/). HIGH.

### 1D. Industrial-disaster case studies
- **Libby operated 1963–1990; ">70% of US vermiculite" (EPA).** EPA Libby Superfund Site Profile (https://cumulis.epa.gov/supercpad/cursites/csitinfo.cfm?id=0801744). HIGH dates; **"~80% of world" → EPA says >70% US; see §2.**
- **Libby asbestosis mortality 40–80× national; first-ever EPA Public Health Emergency (June 17 2009).** ATSDR, *Mortality in Libby 1979–1998*, 2002 (https://www.atsdr.cdc.gov/hac/pha/LibbyAsbestosSite/MT_LibbyHCMortalityRev8-8-2002_508.pdf). HIGH. **Deaths: >400 (early EPA) → ~694 by 2011 (Naik et al. 2017, https://www.nature.com/articles/jes201618); ~2,400+ diagnosed — see §2.**
- **W.R. Grace $250M federal reimbursement (2008, then-record Superfund); cleanup >$600M.** DOJ Press #08-194, Mar 11 2008 (https://www.justice.gov/archive/opa/pr/2008/March/08_enrd_194.html). HIGH for components. **">$4B total" mixes Libby-site + company-wide bankruptcy trust — document components; see §3.**
- **Deepwater Horizon: 4.9M barrels; 11 killed; 87 days (Apr 20–Jul 15 2010).** NOAA (https://response.restoration.noaa.gov/deepwater-horizon-oil-spill-case-study). HIGH.
- **BP $20.8B total settlement (2016): $5.5B CWA + $8.8B NRDA + $4.9B states + $600M other + up to $1B local; "up to $18.7B" = 2015 principal.** DOI/DOJ, Apr 4 2016 (https://www.doi.gov/pressreleases/us-and-five-gulf-states-reach-historic-settlement-bp-resolve-civil-lawsuit-over). HIGH. **BP cumulative charge ~$61.6B (2016) → ~$65B (2018):** BP SEC 6-K/20-F. HIGH.
- **NOAA NRDA ecological kill: 4–8.3B oysters; 2–5T larval fish; 51k–84k birds; 56k–166k turtles.** NOAA PDARP/PEIS 2016 (https://www.gulfspillrestoration.noaa.gov). HIGH. **">$150B total damages" is NOT a NOAA figure (NOAA assessed = $8.8B) — see §2/§3.**
- **Baotou tailings lake ~11 km² (~180 Mt waste).** Independent reporting (Baogang Tailings Dam). MED-HIGH. **Waste-per-ton: peer-reviewed "up to ~40 t tailings/t REO"** — Zapp et al. / review in PMC8929459 (https://pmc.ncbi.nlm.nih.gov/articles/PMC8929459/); **the "~10 tons" is journalism (Unknown Fields / Chinese Soc. of Rare Earths) — see §2.**
- **Exxon Valdez ~11M gallons (Mar 24 1989); $900M civil + $125M criminal ($25M fine + $100M restitution), 1991.** EVOSTC (https://evostc.state.ak.us/oil-spill-facts/settlement/) + EPA 1991 (https://www.epa.gov/archive/epa/aboutepa/exxon-pay-record-one-billion-dollars-...). HIGH. **"$5.5M cargo value" + "$7–10B all-in" are derived/aggregate, not single-source — see §3.**

### 1E. Macro-finance / funds / programs
- **Social Security: OASI depletion 2033; 77% payable thereafter; outgo > income since 2021; enacted 1935.** SSA, *2025 OASDI Trustees Report Highlights* (https://www.ssa.gov/oact/TR/2025/II_A_highlights.html) + 2024 Highlights. HIGH. *(Pay-as-you-go via 1939 amendments.)*
- **Household net worth fell ~$11–12T (2007 peak → 2009).** Federal Reserve *Financial Accounts (Z.1)* / FRED TNWBSHNO (https://fred.stlouisfed.org/series/TNWBSHNO). HIGH. **→ this is a FED figure, NOT Mian & Sufi (whose number is $5.5T housing wealth); see §2.**
- **Fed emergency lending $16.1T = GROSS CUMULATIVE originations (peak outstanding ~$1.1–1.6T).** GAO-11-696, July 2011 (https://www.gao.gov/products/gao-11-696). HIGH. **→ don't imply $16T was ever outstanding at once; see §2.** TARP $700B authorized (→$475B): Treasury (https://home.treasury.gov/data/troubled-assets-relief-program). HIGH.
- **~4.1M completed foreclosures through 2012** (CoreLogic 2017). HIGH. **"~5M completed / ~10M filings" overstated/RealtyTrac — see §2.** Mian & Sufi, *House of Debt*, 2014 (https://press.uchicago.edu/ucp/books/book/chicago/H/bo20832545.html).
- **Norway GPFG NOK 21,268B (>$2T) end-2025; per-citizen ~$390k now.** NBIM (https://www.nbim.no/en/investments/the-funds-value/). HIGH. Fund est. 1990; first deposit 1996; renamed GPFG 2006. **Fiscal rule introduced 2001 at 4%, lowered to 3% in 2017** (regjeringen.no). **→ "3% adopted 2001" is WRONG; per-capita "$360k" now ~$390k; see §2.**
- **Norway 78% combined marginal petroleum tax (22% + 56% special) + SDFI + Equinor dividends.** Norwegian Petroleum (https://www.norskpetroleum.no/en/economy/petroleum-tax/). HIGH for 78%. **"70–80% of net wealth" conflates marginal rate with aggregate take — recast; see §2.**
- **Alaska Permanent Fund: est. 1976 (constitutional); ≥25% mineral royalties; first dividend 1982 ($1,000); ~$80–89B; 2023 div $1,312 / 2024 $1,702.** APFC (https://apfc.org/who-we-are/history-of-the-alaska-permanent-fund/) + AK Dept. of Revenue PFD. HIGH.
- **Medical crowdfunding: 437,596 GoFundMe campaigns, >$2B, 21.7M donations, 2016–2020; 12% met goal, 16% got nothing.** Kenworthy, Igra et al., *AJPH* 112(3), 2022 (https://ajph.aphapublications.org/doi/10.2105/AJPH.2021.306617; open PMC8887155). HIGH. **→ correct cite is AJPH 2022 (not "Kenworthy & Igra 2024"); "campaigns cover 25–40% of need" needs its OWN source; see §2/§3.**
- **US v. Sioux Nation, 448 U.S. 371 (1980): $17.1M land + $0.45M gold + ~$88M interest (5%) ≈ $106M (1980); BIA escrow now >$1.5B.** Supreme Court (https://supreme.justia.com/cases/federal/us/448/371/). HIGH for case/$106M; escrow ">$1.5B" MED (grows yearly; ">$1B as of 2018" is the verifiable anchor).

### 1F. Already verified earlier this session (in §23; do not re-hunt)
DAC bands (Fuss 2018 / IPCC AR6 / IEA DAC 2022 / NAS 2019 / Climeworks; Keith/Realmonte/House 2011–2019); SCC $190 (EPA 2023, drawing on Rennert 2022 $185); space economics (Keck $5,200/kg, Bennu, Falcon 9 $74M/2026, Colvin-Crane-Lal 2020); EPA AP-42 coal emission factor (93.28 kg/mmBtu → 2.61/2.32 mt); USGS MCS 2025 Baotou reserve %s (69/40/80); NBIM NOK 21,268B; Census endpoints; BP/DOJ Deepwater settlement.

---

## §2. CORRECTIONS / DISCREPANCIES — figures that are WRONG or mis-attributed (highest value; escalate to author / chapter sessions)

These are not missing-citation issues — they are figures the primary sources contradict. **Reputational priority.**

1. **Norway 3% fiscal rule "adopted 2001" is WRONG.** The rule was introduced 2001 **at 4%**, lowered to **3% in 2017** (regjeringen.no). Appears Ch 4:28, Ch 6:221, TA §11.5. Fix the date/rate pairing.
2. **2008 "$11 trillion lost" attributed to Mian & Sufi is mis-attributed.** $11T is the **Federal Reserve** household-net-worth figure; *House of Debt*'s own number is **$5.5T housing wealth**. **CONFIRMED LIVE on canonical Ch5** (`Chapter__5_TheAccountabilityGap_Draft.md` §76, landed on main `dbde2e6` 2026-06-09: "the economists Atif Mian and Amir Sufi… household net worth fell by roughly eleven trillion dollars"). Also Ch 8:196 / Ch 9:122. **Re-attribute the ~$11T total-net-worth magnitude to the Fed (Z.1) while keeping Mian & Sufi for the leverage/distribution + MPC analysis (which is genuinely theirs)**, or use $5.5T housing-wealth for their number. This is the one residual correction on the otherwise-clean §100–104 honest-$108T recompute — apply-spec for redraft/author.
3. **Fed "$16 trillion" needs the cumulative caveat.** $16.1T is **gross cumulative loan originations** (GAO-11-696); peak outstanding ~$1.1–1.6T. As written it implies $16T outstanding. Ch 5:84. Add "cumulative."
4. **Menhaden cap "set 2006, reduced 2017 to 51,000 mt" is WRONG.** The 51,000 mt cap is **ASMFC Amendment 3 (2017/2018)**. Ch 3:111. Fix.
5. **"60,000 Appalachian cancer cases" is not in the peer-reviewed source.** Hendryx 2012 reports an **odds ratio of 2.03**; "60,000" is an advocacy extrapolation. Ch 8:50. Cite the OR, or attribute the extrapolation explicitly.
6. **Macondo well revenue "~$1.1B" is not reconcilable.** At ~50M bbl × 2010 price, gross ≈ **$3–4B**; the $1.1B figure has no basis unless net-of-cost. TA §11.2 + Ch 5/6. (Ledger Item 4 / Session E already flags the Deepwater reconciliation.)
7. **Baotou remediation ">$100B" is likely ~10× too high.** Documented: ~$43M (Baotou 2015 transfer); ~$5.5B (Jiangxi national, MIIT). Use **$5–15B**. Ch 5:68.
8. **DWH ">$150B total damages" must NOT be attributed to NOAA.** NOAA's assessed natural-resource damages = **$8.8B**; $150B+ is a broader economic estimate. Ch 5:48. Re-attribute or drop the NOAA tie.
9. **"$4.50/ton 1960 coal" → EIA says $4.71 (bituminous) / $4.83 (all-coal).** 7 TA spots + Ch 2/6/8. Cascades into IPG ratios (ledger Item 9b → Session C/D).
10. **Tangier "15 ft/yr" / "2 sq mi"** — the peer-reviewed average is ~1.7 ft/yr; ~1.2 sq mi remaining land. "15 ft/yr" is USACE-via-press for the exposed western shore. Ch 3:156. Reframe as exposed-shore max.
11. **Libby "~80% of world vermiculite"** → EPA says **>70% of US**. Ch 5:20. **Libby deaths ">400"** is the early count; ~694 by 2011 (Naik 2017). **"35M homes"** → cite as a range (~1M–35M).
12. **Per-capita Norway "$360,000" is now ~$390,000** (time-sensitive; NBIM end-2025). Ch 4:26.
13. **GoFundMe cite "Kenworthy & Igra 2024" → AJPH 2022;** "$438,000 campaigns" → 437,596. Ch 5:156 / Ch 9:202.
14. **Reclamation gap stated inconsistently:** "$3.7–6B" (Ch 6) vs "$3.5–6B / $4–6B" (Ch 8). Reconcile to the Appalachian Voices arithmetic.

---

## §3. UNVERIFIABLE — no primary source located (relabel as estimate, attribute to the secondary origin, or cut)

- **Black Lung "$44B cumulative payouts"** — **status updated (§6B):** the Darity with-citations docs attribute it to "DOL OWCP / BLDTF annual reports" (TA) and "**$44B through 2009 (GAO/CRS)**" (Ch 6). The "through 2009" vs "56-year/Sept-2024" date split means it's **likely a ~2009 figure presented as current** — stale, not just unsourced. **Action:** pin the GAO/CRS "through 2009" doc (likely CRS R45261) and relabel to "≈$44B through 2009," OR get the current cumulative from DOL OWCP annual reports; the "56-year" framing must not rest on a 2009 number. (Memo Item 9a.)
- **"60,000 MTR cancer cases"** — advocacy extrapolation, not in Hendryx 2012 (see §2.5).
- **Libby "~$100M lifetime revenue"; ">$4B consolidated total"; "35M homes" precise** — no federal point source (components verifiable separately).
- **Macondo well revenue (any figure)** — no government primary source; analyst estimate only.
- **DWH ">$150B"** as a total — not a NOAA figure; needs the originating economic study or drop.
- **Baotou ">$100B" remediation; "~10 t waste/t REO"; "$10–12B annual revenue" exact** — journalism/estimate; use peer-reviewed substitutes (§2.7, §1D).
- **Exxon Valdez "$5.5M cargo value"; "$7–10B all-in"** — derived/aggregate, not single-source.
- **U.S. Steel Gary closure "1986 / 1,200 jobs"** — conflicting years (1982 / 1984 / 1986) across sources; no primary employment record. Soften to "mid-1980s" or source a contemporaneous record.
- **"Campaigns cover 25–40% of need"** — not in the AJPH 2022 paper; needs its own source.

---

## §4. FRAMEWORK OUTPUTS — relabel, do NOT source (cross-ref the TA self-citation kill-list)

Per author direction, framework-computed numbers get "framework-computed, derivation shown" labeling — never an external cite. These are owned by the IPG-apparatus relabel (decision-memo Item 1 → Session C) + the M3 rework (Session D):
- **LIST B (TA):** the §9.5 12-cell IPG table; "Documented … canonical 33–122×" (§11.6 L4496/4503 — the most egregious self-citation, backed by "Case-study audit + terms_index"); §3.2 IPG=33; §16.4 sensitivity; the §3.6 triangulation outputs; Norway "$13–15T residual CS"; the M3-IPG premium-multiple (8.5–26×).
- **Chapters:** all IPG multiples (33–122×, 50–555×, 15–17×, etc.); RCV/CS/floor figures; the "$108T Social Security foregone return" (Ch 5:114 — the most aggressive; needs a transparent derivation, NOT an external cite); Libby 40:1, DWH 40% ratios; per-ton component allocations ($1–5/ton etc.).
**Discipline:** the empirical INPUTS to these derivations (coal price, damage figures, DAC bands, SCC) must be sourced (§1–§2); the OUTPUTS must be labeled ours. Fix the inputs first, then the outputs recompute.

---

## §5. Application plan (owners)

1. **§23 bibliography** — add the §1 sources (THIS session, internal scaffolding). Done in this commit for the new entries.
2. **Chapter prose citation pass** — apply §1 sources + §2 corrections to Ch 1–10. **AUTHOR / chapter sessions** (end-user-facing prose; ratification required; do NOT edit unilaterally).
3. **TA LIST-A empirical fixes** — coal price ($4.71), Eco/Cohesion estimate-labels, Deepwater reconciliation: this workstream (Eco/Cohesion) + Session E (Deepwater) + Session C/D (coal-price cascade).
4. **TA LIST-B framework-output relabels** — Session C (IPG apparatus) + Session D (M3).
5. **§2 corrections are the priority** — several are shippable-error risks in the published chapters.

---

## §6. Sources recovered from `research/outreach/subjects/` (2026-06-08)

Mined per author steer (the folders hold real source material). 4 agents: darity, colden, cbf, moore.

### 6A. The Darity "with-citations" packet (2026-05-14) — the biggest find
We already produced **citation-bearing versions of Ch 5, Ch 6, and the TA** for William Darity Jr. They **already attribute most empirical figures to agency sources** — but only *inline* (in the TA §11 anchor tables + Ch 6 parentheticals); the **TA §18 bibliography is academic-theory-only**, so none of these agency sources are formally entered. **This de-risks the whole sweep: the sources largely already exist in our own docs and need formalizing, not hunting.** Attributions found (verbatim source cells):
- **13-yr life-expectancy gap → CDC + Robert Wood Johnson Foundation County Health Rankings.**
- **Darity 6–7 yr Black–white longevity gap → Bassett-Bell, Williams, Darity et al., "Association Between Racial Wealth Inequities and Racial Disparities in Longevity…1992–2018," *JAMA Network Open* 5(11):e2240519 (2022)** (already in TA §18). ← real, specific, add to §23.
- **Reclamation bond gap → OSMRE + GAO-17-207R + Yang & Davis 2021** ($4–6B; $865M bankruptcy transfer = OSMRE bankruptcy filings). *NB the clean-chapter "633,000 acres / $7.5–9.8B" has NO match here — that's the separate Appalachian Voices figure (§1B); the packet's number is 150,000 McDowell acres / $3.7–6B national.*
- **SCC $190 → Rennert et al. 2022 *Nature***; **DAC bands → Climeworks/CE-1PointFive/IEA/IPCC/NAS**; **coal 2.32/2.61 t → EPA AP-42 §1.1 + EIA heat content**; **~600M tons → WV Geological Survey + USGS**; **Baotou shares → USGS MCS 2025**; **Norway → NBIM**; **Deepwater → NOAA Office of Response & Restoration + DOJ + 2016 BP Consent Decree (NRDA $8.8B)**; **Libby → EPA Libby Superfund record + Montana DOJ/DEQ + W.R. Grace filings**; **Exxon Valdez → EVOSTC + DOJ 1991**; **2008 → GAO 2011 audit ($16T) + FCIC 2011 + GAO HAMP reports**; **reparations → Darity & Mullen 2020 + Hamilton et al. 2015 + Coates 2014 + Conley 1999.** (All consistent with §1; the packet is the in-house corroboration.)

### 6B. $44B Black Lung — STATUS CHANGE (attributed, but date-discrepant + likely stale)
The with-citations docs DO attribute it: **TA §11.6 → "DOL Office of Workers' Compensation Programs; Black Lung Disability Trust Fund annual reports"**; **Ch 6 → "approximately $44 billion in distributions *through 2009* (GAO/CRS)."** **But:**
1. **Date discrepancy = red flag.** Ch 6 says "$44B **through 2009**"; TA §11.6 says "$44B cumulative **1969–present (56 years)**"; Ch 5 leads with it and cites **nothing**. The same number cannot be both "through 2009" and "through 2024." This strongly implies **$44B is a ~2009 figure being presented as current cumulative** — i.e. stale, and undercounting if anything.
2. **Still not pinned to a locatable document.** "DOL annual reports / GAO/CRS" is a category, not a citation; my earlier exhaustive search (GAO-18-351, Brookings 2021, web) found no "$44B" — consistent with it living in an **older CRS/GAO doc reporting "through ~2009"** (likely **CRS R45261**, which 403'd). **Action:** pin the specific GAO/CRS doc for "$44B through 2009," then EITHER relabel to "≈$44B through 2009 (GAO/CRS)" (what Ch 6 already says — honest + likely sourceable) OR get the current cumulative from DOL OWCP annual reports. The "56-year / Sept-2024" framing should NOT stand on a 2009 figure.

### 6C. Chesapeake primary sources (Colden / Moore / CBF)
- **Rockfish YOY 2.0 vs 11.0 (2024)** — MD DNR seine survey; surfaced via *Southern Maryland Chronicle* 2024-10-18 + **VIMS juvenile striped bass survey** (vims.edu). Colden's quotes attach here. *(Moratorium 1985–90/recovered-1995 dates are NOT in any folder — keep the NOAA/ASMFC source from §1C.)*
- **Menhaden 51,000 mt cap → ASMFC, Nov 2017, on Colden's OWN original motion** (she was CBF MD Senior Fisheries Scientist) — strong authority. Peer-reviewed architecture: **ASMFC Ecological Reference Points + Anstead et al., *Frontiers in Marine Science* 7:606417 (2020)**; the cut was **~41.5% (≈87,000 → 51,000 mt)**. *(Confirms §2.4 correction: Amendment 3 / 2017–18, not 2006.)*
- **Blue crab 238M (2025), 2nd-lowest since 1990 (lowest 226M, 2022)** — Winter Dredge Survey (MD DNR + VIMS); *Maryland Matters* 2025-05-23; VPM 2025-06-04 (Moore). Confirms §1C.
- **Maryland oysters tripled since 2005 (2.4B→7.6B adults)** — **MD DNR press release 2025-08-26** (Gov. Moore five-sanctuary completion). Confirms §1C. *(Packet flags Ch 3 softens to "roughly tripled" — tone, not claim.)*
- **Colden's own peer-reviewed science** (load-bearing for the "renewable-past-regeneration" construct): **Colden, Latour & Lipcius, "Reef height drives threshold dynamics of restored oyster reefs," *Marine Ecology Progress Series* 582:1–13 (2017)**; Colden & Lipcius 2015 (*MEPS* 527); Colden et al. 2016 (*Estuaries and Coasts* 39).
- **CBF named report: *Hope on the Half Shell* (Feb 2024)** — oyster restoration (20 additional rivers; **$56.8M MD+VA oyster revenue 2022**). **CESR / STAC 2023** — the 40-year Bay nutrient-effort evaluation. **Bryan Watts / W&M Center for Conservation Biology 2025** — 90% osprey-nesting decline on VA Eastern Shore.
- **Adversarial sources** (for Pass 3.4 balance, likely absent from a CBF-leaning bib): **Menhaden Fisheries Coalition rebuttal (Oct 2025)** + **Ocean Harvesters response (Aug 2025)** — dispute Moore's catch-distribution characterization.
- **NOT in any folder** (still need §1C web sources): historical oyster decline (15M→<200K bushels / 99%) and watershed 64,000 sq mi. Colden is NOT the source for either.

### 6D. New reconciliation flags (add to §2)
- **(15) $44B end-year**: "through 2009" (Ch 6) vs "1969–present / Sept-2024 / 56 yrs" (TA §11.6, Ch 5). Likely a stale 2009 figure.
- **(16) Norway GPFG value stated three ways across the packet**: $1.9T / $2.0T (end-2025) / $2.2T (early-2025 NBIM); per-BOE shifts $50→$48. Reconcile to one vintage (already a Session D item).
- **(17) Deepwater total**: Ch 5 prose "$65B / >$150B" vs TA §11.2 + Ch 6 table "$20–30B documented." Material divergence (Session E reconciliation).
- **(18) Menhaden "Bay cap 2007" (striped-bass-era, Goldsborough) vs "Nov 2017" (menhaden 51,000 mt)** — the folders use "Bay cap" for both; do not conflate.

### 6E. Application note
The Darity packet means **the chapter-citation pass is mostly a *formalization* job, not a research job**: lift the inline agency attributions from the with-citations docs into (a) the TA §18/§23 bibliography and (b) the clean chapters' citation apparatus. The genuinely-still-unsourced shrinks to: the $44B (pin the 2009 doc or relabel), the 633,000-acre/$7.5–9.8B figure (Appalachian Voices — §1B), historical oyster decline, watershed area, and the §3 UNVERIFIABLE set.
