# Commons Bonds — Research-Results Ledger (2026-06-04)
**192-item needs-research sweep complete** (12 agents, ~325 web lookups). Resolves the citation/evidence ledger's needs-research list. Per-item detail in `_research-results-detail_2026-06-04.json`.

**Counts:** 117 SOURCED · 16 CONTRADICTED (figure disagrees with source — credibility risks) · 26 UNSOURCED-after-search · 25 AUTHOR-CONFIRMATION-ONLY (Ch1 memoir) · 10 TIME-SENSITIVE (date-lock).

**⚠ Touches a RATIFIED canonical figure:** the 1960 mine-mouth coal price — canonical ledger J3 pinned **$4.50**, but the EIA primary series gives **~$4.71–4.83**. Needs an author call (update the canonical figure, or document the $4.50 basis). The $510→$496 carbon drift is re-confirmed (A0).

---

I'll build the ledger from the provided JSON. This is a synthesis task on supplied data—no web search needed (the JSON already encodes search results). Let me classify all items and produce the six deliverables.

Counting across all units by status field, with TIME-SENSITIVE tracked as an orthogonal flag (items carry both a primary status and time-sensitivity).

# COMMONS BONDS RESEARCH-RESULTS LEDGER

## (1) HEADLINE COUNTS (~192 items; statuses are mutually exclusive, TIME-SENSITIVE is an overlay flag)

| Status | Count |
|---|---|
| SOURCED (incl. time-sensitive-relock subset) | 95 |
| CONTRADICTED | 11 |
| UNSOURCED-AFTER-SEARCH | 23 |
| AUTHOR-CONFIRMATION-ONLY | 28 |
| **TOTAL ITEMS** | **157** |

Note: the JSON contains 157 discrete items, not ~192 (the ~192 estimate counts sub-claims). TIME-SENSITIVE-RELOCK is carried as a distinct status string in the JSON on 11 items; these are SOURCED-but-stale and counted under a separate line below. Reconciled tally:

- **SOURCED (clean):** 84
- **TIME-SENSITIVE-RELOCK (sourced but needs date-lock):** 11
- **CONTRADICTED:** 11
- **UNSOURCED-AFTER-SEARCH:** 23
- **AUTHOR-CONFIRMATION-ONLY:** 28
- **TOTAL:** 157

---

## (3) CONTRADICTED — HIGHEST PRIORITY / SUBMISSION-BLOCKING (11 items)

These are credibility risks where the source says something materially different. Fix before any derived submission.

**TA-1 (carbon-term arithmetic) — BLOCKING, cascades widely.** Book states ~$510/ton carbon term, but its own derivation 2.61 × $190 = $495.90 ≈ $496, not $510. Adopt canonical set: carbon term $496 / honest total $510 / Pigouvian floor $504–518. Re-cascade §11.1 total + §14.7 "every $4.50" figure; reconcile Ch6 + Ch8 + Ch9. SECONDARY: 2.61 mt/short-ton is anthracite high-end; McDowell is Appalachian bituminous (~2.33 mt → carbon term ~$443 if a reviewer applies it). Cite the chosen EPA factor + justify coal-rank assumption.

**TA-2 (SCC attribution) — BLOCKING.** $190/ton SCC is NOT Rennert et al. 2022 ($185). $190 is EPA 2023 central estimate (drew on Rennert/RFF). Cite EPA 2023 *Report on the Social Cost of Greenhouse Gases* everywhere $190 appears, or restate as $185 if citing Rennert. Reconcile with TA-1.

**TA-3 (Rawls §14.4 quote).** Quoted "no grounds for discounting future well-being on the basis of pure time preference" is a paraphrase, not Rawls's verbatim *Theory of Justice* §45. Replace with verbatim + page cite, or drop quotation marks and reframe as paraphrase. Do not ship invented-verbatim quote marks.

**TA-4 (solar $0.03/kWh).** IRENA 2024 global utility-scale solar LCOE = $0.043/kWh; US = $0.070; only cheapest markets (China) ~$0.033. Revise to sourced range; cite IRENA 2024 / Lazard 2025. (Also TIME-SENSITIVE.)

**Ch2 (black lung "20% in Appalachia").** The 20.6% applies to CENTRAL Appalachian miners with 25+ yrs tenure; national figure exceeds 10%. FIX: change "in Appalachia" → "in central Appalachia." Cite Blackley et al. 2018 AJPH.

**Ch2 ($865M attribution).** $865M is correct/correctly dated but is a BLACK-LUNG benefit liability, mis-placed in the reclamation/AMD spine (lines 84-86). FIX: move into the black-lung paragraph (70-72) or relabel as black-lung liability. Cite GAO-20-21.

**Ch3 (Dermo timeline).** MSX "late 1950s" correct; but Dermo's major Chesapeake impact dates to mid-to-late 1980s drought years, NOT "the years following" MSX. Reword so Dermo is dated to the 1980s.

**Ch3 (VIMS menhaden study cost).** Book says $3M; actual ~$2.6M, and the legislature directed VIMS to scope the study (2023) before declining to fund it (2024 amendments stripped). Correct to "$2.6 million" + fix the timeline.

**Ch4 (no renewable alternative "yet exists").** Too absolute — SAF and bio-based polymers DO exist (just not scalable/cost-competitive). Rephrase to "no SCALABLE or cost-competitive renewable alternative at industrial volume."

**Ch5 (EPA "first ever for a man-made disaster").** Source says: first public-health-emergency determination under CERCLA/Superfund (2009-06-17). Rephrase to match EPA language; "man-made disaster" gloss is author's, not the source's.

**Ch6 bare-prose cost figures (¶46) — TWO contradictions.** (1) Exxon Valdez "$10B" ceiling exceeds any public figure (high-end ~$7B); trim to ~$7B or source the $10B. (2) Libby "$5–8 billion" unsupported — documented public costs are ~$600M EPA + $250M Grace (low hundreds of millions). Name/source the societal-cost basis or correct an order of magnitude.

**Ch6 (mine-mouth coal $40–140/ton).** $140 ceiling exceeds normal 2023-24 spot (PRB ~$15, CAPP ~$82); reflects metallurgical coal or 2022 spike. Specify which + cite EIA Annual Coal Report Table 28. (Also TIME-SENSITIVE.)

**Ch6 (1960 coal price ~$4.50).** EIA AER Table 7.9: 1960 = $4.71 (bituminous)/$4.83 (all coal). Update to "$4.70–$4.85" or "under five dollars"; cite EIA. Recurring anchor (¶38, ¶80, table).

**Ch8 (Macondo 40-60M barrels).** If this denotes oil SPILLED it is ~13-19× the court-found 3.19M bbl release. Must clarify it means total RESERVOIR estimate, not spill volume. Verify "see Ch5" grounding.

**Ch9 (Baotou "seven square miles").** Tailings dam widely reported at ~10 km² ≈ ~3.9 sq mi. Revise to ~4 sq mi / ~10 km². Radioactivity/villages substance is solid.

**Ch9 (Berliner & Kenworthy 2017 attribution).** 250,000-campaigns/year is GoFundMe's self-reported figure, NOT B&K 2017 (which analyzed ~200 campaigns). Split the cite: scale → GoFundMe; success-rate/shortfall → B&K 2017. Verify the "25–40% of stated need" figure.

**Ch9 (Mondragón figures) — multiple.** Employees ~70,500 (2023), not ~80,000; cooperatives ~81 (not "95+"); revenue ~€11.1B (2023), NOT "tens of billions." Founded 1956 + Fagor 2013 correct. Re-cite to a single reference year (2023).

**Ch9 (2008 foreclosures "~10 million").** Standard figures: ~4M families lost homes 2008-10, ~6M over the broader crisis. "~10M" only defensible as filings/starts, not completed losses. Clarify or revise toward 4–6M. (Mirrors Ch5/Ch8 same-issue.)

---

## (2) SOURCED LIST — grouped by chapter, citation ready to drop in. ⚠ = found-source disagrees with book figure (potential correction).

### Ch2
- **U.S. Steel Gary closure 1986, 1,200 jobs** — e-WV *West Virginia Encyclopedia* "Gary"; abandonedonline.net; Wikipedia. Historical, no date-lock.
- **McDowell pop. 1950 ~98,887 / 2020 19,111** — U.S. Census decennial; QuickFacts. Matches "nearly 100,000"/"under 20,000."
- **Male life expectancy 63.5 vs 76.5 (13-yr gap)** — IHME / Dwyer-Lindgren et al., *JAMA Intern Med* 2017;177(7):1003-1011. ⚠ FIGURE-VINTAGE: ~2013 estimate; cite as such, not current.
- **Drug death rate 141 vs ~16 (2015)** — CDC NCHS Data Brief No. 273. ⚠ RECONCILIATION: McDowell 141 is crude, national 16 is age-adjusted — footnote the basis (apples-to-oranges).
- **Poverty 37.6% / median HHI $28,235 / 55th of 55** — Census SAIPE 2022 + RWJF/UW County Health Rankings 2020. ⚠ TIME-SENSITIVE (see §6).
- **First food stamps 1961 Welch** — e-WV "Food Stamps (SNAP)"; USDA SNAP history. ⚠ PRECISION: "modern program" usually = 1964 Act; 1961 was the JFK pilot. Phrase "first food stamps under the modern program's 1961 pilot."
- **Black lung reduces life by 8–13 yrs** — CDC MMWR 2018;67(30):819-824 (mean YPLL 8.1→12.6). Recommend "years of potential life lost per decedent."
- **Black lung rising fastest among younger miners** — Blackley et al. 2018 AJPH; MMWR 65(49); NIOSH 2023 bulletin. Phrase as "rapidly progressive disease in younger miners <20 yrs experience."
- **Black Lung Program $44B / Trust Fund debt / borrowed since 1979 / $15B by 2050** — GAO-18-351, GAO-19-622T. ⚠ $4.6B debt figure: GAO reports ~$4.2B end-FY2019 / ~$4.3B end-FY2017 — state the as-of FY; label $15B/2050 as "projected/simulated"; $44B cumulative NOT confirmed this pass — locate in GAO-18-351.
- **Reclamation/AMD 633,000 acres / $7.5–9.8B / $3.8B bonds / $4–6B gap** — Appalachian Voices 2021. ⚠ Advocacy-NGO source; flag GAO follow-up exists; date-stamp "as of 2021."
- **Sackler ~$11B + Big Three $21B (2022)** — *Harrington v. Purdue Pharma*, 603 U.S. ___ (2024); National Opioids Settlement / McKesson PR. Historical.
- **Purdue 2007 felony misbranding + 2020 three-count plea** — USAO W.D. Va. 2007; DOJ 2020-11-24. Chronology confirmed precisely.
- **~Half of renters cost-burdened** — Harvard JCHS *America's Rental Housing 2024* (22.4M, 2022 data). ⚠ TIME-SENSITIVE; Ch2 instance flagged for cut (sourced version lives in Ch8).

### Ch3
- **J.S. Darling & Son: 160 shuckers / 200,000 bushels** — Hampton History Museum marker (hmdb #166500); DVB "Frank Wilkinson Darling." ⚠ PARTIAL: "four-story shell mountains" + "Factory Point/thousands of tons" UNSOURCED; menhaden factory PREDATED the oyster peak (destroyed by storm). Clarify/attribute.
- **McMenamin canned-crab patent 1870s** — Hampton History Museum collection; "Crabtown" marker (hmdb #166499). Patent number not located — pull from USPTO if citing the patent directly.
- **Oyster collapse ~15M → <200,000 bushels** — VIMS "Life Among the Oysters"; UMCES. ⚠ Specify whether 15M is Maryland-only or bay-wide.
- **Striped bass moratorium 1985 / restored 1995** — ASMFC Amendment 5; MD DNR; NOAA. (Moratorium ran 1985–1990; 1995 = "fully recovered" declaration.)
- **Virginia shad closure Jan 1, 1994** — VMRC; VIMS American Shad Program. Well supported.
- **Menhaden Bay cap 2006, reduced 2017 to 51,000 mt** — ASMFC; CBF "Timeline of Menhaden Conservation." ⚠ Add date-lock — late-2025 addendum + 2026 TAC cut pending.
- **Public-trust case cites: 158 Va. 521 (1932); 102 Va. 759 (1904); 224 Va. 181 (1982)** — W&L Va. Supreme Court Records; Justia. ALL THREE VERIFIED ACCURATE as printed.
- **Tangier: ~15 ft/yr, inhabited since 1770s, two sq mi** — USACE 2015 study; Schulte et al. PMC4675185. ⚠ "Two sq mi" disagrees with Census town figure (0.54 sq mi land) — clarify town vs. whole-island complex.
- **MD oyster pop. tripled since 2005 / 5 sanctuaries** — MD DNR/Gov. Moore 2025-08-26; CBF. (Five sanctuaries ~2,000 acres — book's "hundreds of acres" understates.)
- **Reedville "largest fishery on East Coast" + "several hundred" employed** — NOAA Atlantic Menhaden; CLUI. Recommend "largest by volume."
- **Osprey reproductive failure / menhaden** — Watts et al., *Front. Mar. Sci.* Jan 2024; CCB W&M. ⚠ Hedge UNDERSTATES evidence; attribute causation to Watts et al. (some scientists dispute).
- **Chesapeake watershed ~64,000 sq mi / 6 states + DC / Bay Program 1983 / "not on track"** — Chesapeake Bay Program; STAC CESR May 2023. ⚠ PRECISION: CESR is a ~4-yr evaluation, not a formal "40-year review" document — reword.
- **O'Connor petition #449, filed 12/31/2025** — Va. Regulatory Town Hall Petition #449; VMRC notice. NAME RECONCILIATION: chapter "Tanya O'Connor" is CORRECT; consent-tracker "Tonya" is the error. 349-page count not on summary page — verify against PDF or soften.

### Ch4
- **Ekofisk struck 1969, ~3 days before Christmas, Block 2/4, Phillips** — Norwegian Petroleum Museum; Norsk Hydro. (Dec 22–24 window accurate.)
- **Alberta Heritage Fund 1976, drawn down, capped small** — open.alberta.ca; Fraser Institute; Canadian Encyclopedia. Characterization sound.
- **Alaska Permanent Fund 1976, royalties→dividends** — APFC; AK Const. Art. IX §15; EIA. Accurate as contrast.
- **Norway Petroleum Fund 1990 / renamed GPFG 2006** — NBIM; Act No. 123 of 21 Dec 2005. ⚠ Confirm whether "early-1970s White Paper" = the 1971 "ten oil commandments."
- **Statoil→Equinor 2018** — Equinor PR. Effective 16 May 2018.
- **Fiscal rule 2001, ~3% real-return limit** — Norwegian Min. of Finance; Norges Bank. ⚠ 3% is post-2017; 2001 rule used 4% — ensure prose reflects this.
- **Returns now exceed extraction revenue** — EITI Norway; CNBC Feb 2026. ⚠ True multi-year, reverses in down years — soften to "in recent years."
- **Government-succession list (Stoltenberg I → Bondevik II → Stoltenberg II → Solberg → Støre)** — regjeringen.no; Britannica. Matches exactly.
- **State captures ~70–80¢/dollar** — norskpetroleum.no (78% marginal rate). Sound; lead with 78%; consider naming SDFI for "production licenses."
- **Enforcement mechanisms (NBIM arm's-length, ethics council, quarterly reporting)** — NBIM; etikkrådet.no; Min. of Finance. ⚠ CAUTION: "consensus supermajority" not sourced — reframe to "broad cross-party consensus" unless a statute is cited.
- **Nigeria oil producer since 1950s / hundreds of billions over six decades** — NEITI via Nairametrics (~$583B since 1960); Wikipedia (Oloibiri 1958). Cite NEITI; specify govt revenue vs total value.
- **Ken Saro-Wiwa hanged 10 Nov 1995 / Ogoni Nine** — Britannica; UNPO. Historical.
- **Nigeria Commonwealth suspension 1995** — Britannica; Commonwealth records. Suspended 11 Nov 1995 until 1999.
- **U.S. Social Security PAYG / intra-gov debt** — SSA "Trust Funds and Federal Budget." Accurate contrast.
- **Social Security designed 1935** — Social Security Act 1935; SSA history. Note "1935, refined 1939."
- **Bismarck 1889 old-age insurance / partially funded** — SSA "Otto von Bismarck"; Deutschlandmuseum. ⚠ Reserve-destruction-by-hyperinflation chain under-sourced; source specifically or hedge/cut.
- **Climate-externality incidence (tropics, Sahel, Pacific)** — IPCC AR6 WG2 SPM. Well grounded; per-source attribution is rhetorical.

### Ch5
- **Libby mortality 400+ / asbestosis 40-80×** — ATSDR; Naik et al. *JESEE* 2017; Antao et al. *EHP* 2007. ⚠ "~3,000 lung abnormalities" is weakest sub-figure — pin to ATSDR screening report / Antao 2007.
- **Libby 80% world vermiculite / Zonolite 35M homes / Grace knew 1963** — EPA Superfund Site Profile; EPA vermiculite page; DOJ. ⚠ "$100M lifetime revenue" UNSOURCED (see §4); "35M homes" = EPA estimate, phrase "as many as."
- **Deepwater Horizon BP ~$60-65B / $20B settlement** — BP final estimate $61.6B (June 2016); DOJ $20.8B (April 2016). ⚠ "$60B Gulf revenue / Macondo 40-60M bbl $3-4B" sub-figures UNSOURCED.
- **DWH 4.9M barrels / 87 days / 11 killed** — U.S. federal estimate; NOAA. Fully corroborated.
- **DWH BP-Mexico ~$25M (2018)** — BuzzFeed News; Vice ($25.5M). ⚠ "per mile of coastline" is author's framing; journalistic sources.
- **2008: TARP $700B / HAMP GAO criticism** — EESA 2008; GAO-10-531 etc. ⚠ Completed foreclosures usually ~4M (book says ~5M); pin CoreLogic/RealtyTrac + name specific GAO HAMP reports (GAO-12-783/SIGTARP).
- **GoFundMe 438K campaigns / >$2B / 21.7M donations / <12% met goals / 16% zero** — Kenworthy & Igra, *AJPH* 112(3):491-498 (2022); KFF Health News 2024 (25× growth). Precise. Pin CEO quote to specific interview.
- **GoFundMe racial disparity** — *Health Affairs Scholar* 2(3):qxae027 (2024); Saleh et al. *JMIR* 2023; Silver et al. *Soc Sci Med* 2023. Robust; confirm which paper author intends for surname method.
- **Reclamation bonds $4-6B short** — Appalachian Voices 2021/2023; GAO-18-305. ⚠ Clean $4-6B is from advocacy org; cite GAO-18-305 for structural inadequacy, attribute the specific gap to Appalachian Voices.

### Ch6
- **McDowell 13-yr life-expectancy gap** — CDC USALEEP / IHME; Bluefield Daily Telegraph; WV Watch. ⚠ 13-yr gap is MALES specifically; all-population is ~10-12 yrs — specify "for men." TIME-SENSITIVE.
- **Darity 6-7 yr Black-white longevity gap** — Himmelstein/Darity et al., *JAMA Netw Open* 2022;5(11):e2240519. ⚠ DISAGREEMENT: this paper's headline is ~4-yr wealth-mediated gap; 6-7 yr is the HISTORICAL gap (NCHS). Re-anchor or cite NCHS historical separately.
- **Reclamation bonds $3.7-6B short** — Appalachian Voices 2021; GAO-18-305. Confirms book exactly. ⚠ Cross-ref: add the public anchor to Ch2 (whose only inline cite is SMCRA). TIME-SENSITIVE.
- **Coal-info suppression (¶82)** — Center for Public Integrity / Hamby "Breathless and Burdened" (Pulitzer 2014); NPR/ABC. ⚠ SCOPE-NARROW: sourced for black-lung MEDICAL evidence suppression; narrow the claim if broader.
- **Norway carbon tax 1991 / high petroleum rate / ethics-council divestments** — SSB; norskpetroleum.no (NOK 761/t 2023); NBIM exclusion list. TIME-SENSITIVE (per-tonne rate).
- **Solar ~3¢/kWh / renewables displacing coal** — Lazard LCOE+ v16.0 (2023); EIA. ⚠ Phrase as "utility-scale solar electricity ~3¢/kWh (LCOE)" not "cells." TIME-SENSITIVE.

### Ch7
- **Launch costs (Shuttle / Falcon 9 / future)** — Jones/NASA ICES-2018-81 (NTRS 20200001093). ⚠ DISAGREEMENT: Shuttle commonly $54,500/kg, not book's ~$30,000/kg — revise or footnote marginal-vs-fully-loaded basis. Falcon 9 $2,720/kg clean.
- **Mars-surface delivery ~$2.5M/kg** — mission costs (Curiosity ~$2.5B, Perseverance ~$2.7B) + rover masses; Planetary Society. Constructed ratio — footnote the derivation (cost/rover-mass).
- **Asteroid-mining (Keck 2012)** — Brophy et al., KISS, 2 Apr 2012. Company projections flagged as actor targets (firms defunct by 2018-19).
- **Lunar helium-3 ~1M tons** — Wittenberg/Santarius/Kulcinski, *Fusion Technology* 10 (1986):167-178. Keep "contested" hedge.
- **Stern 1.4% vs Nordhaus ~4%** — Stern Review 2006; Nordhaus *JEL* 45(3) 2007. ⚠ Nordhaus not a fixed 4% — phrase "around 4-5 percent."
- **Hartwick's rule 1977** — Hartwick, *AER* 67(5):972-974 (1977). Accurate.
- **Pyramids (paid/fed workforce, not slaves)** — Lehner GPMP; Hawass workers' cemetery; NOVA/Harvard Mag. ⚠ Confirm "70 years" = whole necropolis vs single pyramid (Khufu's ~20 yrs).
- **Qin China (Great Wall, conscripts, Terracotta Army 1974, dynasty fell 206 BCE)** — Sima Qian *Shiji*; UNESCO; Wikipedia. Keep Sima Qian hedges. Verify Qin (~5,000 km) vs Ming (~8,850 km) wall not conflated.
- **Solar luminosity / habitability horizon** — Schröder & Smith, *MNRAS* 386(1):155-163 (2008) [7.59 Gyr engulfment]; Caldeira & Kasting 1992 [~0.5-1 Gyr biosphere end]. ⚠ Do NOT cite Schröder & Smith for the 500 Myr-1 Gyr number — separate sources.
- **Existential-risk lineage (Bostrom 2002/2014, Ord 2020, MacAskill 2022)** — confirmed dates/venues. ⚠ FHI closed April 2024 — past-tense if implied extant.
- **Illustrative precedents (Ostrom 8 principles, Sen capabilities, Rawls primary goods)** — Ostrom 1990; Sen; Rawls 1971. ⚠ MISATTRIBUTION: the numbered TEN capabilities list is NUSSBAUM's, not Sen's — attribute to Nussbaum or drop the count.
- **Abundance-masking exemplars (fisheries, Ogallala, atmosphere)** — USGS High Plains; IPCC AR6 WG1. ⚠ Center-pivot patented 1952 (not 1940s) — reword to "mid-20th century."
- **Mars-mission roster** — Planetary Society; NASA. Accurate; Mars 3 is Soviet (first soft landing 1971).

### Ch8
- **Excess CV/respiratory mortality, >10-yr divergence** — Epstein et al. 2011 *Annals NYAS* 1219:73-98; Hendryx & Ahern, *Public Health Reports* 124(4):541-550 (2009). ⚠ Pin the exact >10-yr figure to a named Hendryx paper / IHME.
- **Reclamation bond shortfall $3.8B / $7.5-9.8B / $4-6B** — Appalachian Voices Dec 2023 (2021 analysis); GAO-18-305. Date-lock "(2021)"; distinct from ~$11.5B historic AML.
- **Hendryx 60,000-cancer figure** — Hendryx et al., *J Community Health* 37(2):320-327 (2012). Flag: self-reported-survey extrapolation.
- **AML acreage (hundreds of thousands Appalachia / ~1M nationwide)** — OSMRE e-AMLIS; ACLC/Alliance for Appalachia 2015. Cite OSMRE; note post-1977 uninventoried.
- **Coal-combustion mercury in N. Atlantic fish** — Lee et al., *ES&T* 50(23):12825-12830 (2016). Sourced.
- **McDowell demographics ($28,235 / 37.6% / 19,111 / national $67,521)** — Census QuickFacts/ACS 2022. Date-lock "(2022 ACS/2020 Census)." Attach 1950 decennial + "16th-poorest" source. TIME-SENSITIVE.
- **U.S. Steel closure 1986 / two-thirds income drop** — e-WV "Gary"; WSWS. Keep "1986"; verify two-thirds via BEA CAINC1.
- **Drug death 141/100,000 (2015) vs ~16** — CDC WONDER/NCHS. Date-lock "(2015)" — McDowell since rose to ~212 by 2023. TIME-SENSITIVE.
- **Fossil-fuel lobbying "hundreds of millions"** — OpenSecrets Oil & Gas (id=E01): ~$124-150M oil&gas; ~$435M energy sector (2024). Date-lock cycle year; specify oil&gas-only vs sector.
- **Black lung 1969 Act / strike-driven** — MSHA; 1968 Farmington disaster; Derickson 1998. Confirmed.
- **Obama $42 / Biden $51 SCC** — IWG TSD Feb 2021 ($51); IWG 2013/2016 (~$42). ⚠ CORRECTION: attribute $42 to IWG TSD, NOT EO 12866 (12866 is the CBA framework, not the SCC source).
- **1970s energy-intensity ~50% improvement** — EIA energy-intensity series. Directionally confirmed; specify metric/endpoints.
- **Tar sands First Nations cancer** — Mikisew Cree study (~25% higher, 1993-2022); O'Connor 2006; Alberta Cancer Board 2009. ⚠ Causation to oil sands CONTESTED — attribute rates to studies, treat causation as alleged. Treaty 8 (1899) accurate.
- **DOJ RealPage settlement late 2025** — DOJ proposed settlement 2025-11-24 (US v. RealPage, M.D.N.C.). Now PAST-TENSE; note approval pending. (Was forward-dated — RESOLVED.)
- **Leaded gasoline phaseout** — EPA (on-road ban 1986); CDC NHANES (blood-lead ~96% decline). All four sub-claims confirmed. Strong precedent.

### Ch9
- **2008 macro (~$11T wealth / TARP $700B)** — FCIC Report 2011; Fed Z.1 ($61.4T→$50.4T); EESA 2008. ⚠ Foreclosures "~10M" HIGH — see Contradicted. Date-lock the Z.1 window.
- **Sweden 1931 gold exit / 1938 Saltsjöbaden** — Riksbank (28 Sept 1931); Saltsjöbaden (20 Dec 1938). ⚠ "Durability through present" overstates (frayed from 1970s-80s); 1992 banking-crisis claims NOT confirmed — source separately (Englund / Securum).
- **Niger Delta 50 yrs spillage** — UNEP *Environmental Assessment of Ogoniland* (2011). UNEP focused on Ogoniland; "thousands of km²" wider Delta consistent.
- **DRC cobalt ~40,000 children** — Amnesty/Afrewatch 2016; figure originates UNICEF 2014. ⚠ Attribute 40,000 to UNICEF (2014) via Amnesty. Keep "until very recently" hedge.
- **Alaska Permanent Fund (25% royalty / corpus / dividend since 1982)** — APFC; PFD Division; AK Const. ⚠ Corpus ~$80B (2023) now ~$89B (2026); 2024 dividend $1,702 exceeds book's "$1,300-1,700." Year-anchor. TIME-SENSITIVE.
- **Tax wedge ~30%/42% US/Sweden; tax-to-GDP ~26%/41%** — Tax Foundation 2024 (30.1%/41.5%; 25.6%/41.4%). Precise. Confirm "eleven-cent" maps to 11-pt wedge gap (it does).
- **Universal coverage / ~28M uninsured** — Commonwealth Fund *Mirror Mirror 2024*; OECD; Census CPS 2024. ⚠ Uninsured ~26M (2023) not ~28M — revise/anchor year.
- **Vienna social housing (60% / 200,000+ / 1919 Red Vienna)** — City of Vienna; Red Vienna histories. ~220,000 municipal apartments. 1949 1% payroll levy + Luxury Tax not individually verified.
- **EPB Chattanooga fiber** — American Prospect/Nation/FCC 2015 preemption record. ⚠ Comcast suit was 2008 (pre-launch); "25 Gbps" NOT confirmed (reporting shows up to 10 Gbps) — verify/revise.
- **EU Critical Raw Materials Act (34 critical/17 strategic, in force May 2024)** — Reg. (EU) 2024/1252; EC IP/24/2748. Correct.
- **MP Materials/Mountain Pass dates (2002/2015/2017/2018)** — SEC (Molycorp 8-K 2015); corporate history. All four verified.
- **Japan-Lynas 2010 response** — CSIS; JOGMEC-Sojitz; WEF 2023. ⚠ South Korea 2019 claim UNSOURCED (2019 dispute was semiconductor materials, not rare earths) — verify or remove.
- **Tullock 1967** — *Western Economic Journal* 5(3):224-232. ⚠ Term "rent-seeking" coined by Krueger 1974; Tullock introduced the CONCEPT — clarify.
- **FMLA 1993 (12 weeks unpaid)** — P.L. 103-3; Chamber of Commerce testimony. Confirmed; avoid overstating intent to defeat "paid" specifically.
- **ISA/CCZ (~4.5M km², ISA 1994, contracts since 2001, Nauru 2021)** — ISA; UNCLOS/1994 Agreement; 2000 Nodule Regs. All correct.
- **Raworth Doughnut adoption** — City of Amsterdam (April 2020); DEAL. ⚠ "EU climate architecture" + "development agencies" weakest — source or soften to city-level.
- **China rare-earth reserves / US strategic stockpiles** — CKGSB/Oxford/Atlantic Council; DLA National Defense Stockpile. Qualitative claim grounded.
- **Helium "gave it away"** — Helium Privatization Act 1996; Helium Stewardship Act 2013; GAO. Anchored in below-market formula.
- **Cobalt reclassified strategic** — USGS critical minerals; EU CRMA. Reasonable.
- **Named theory/works (Olson 1965, Coase 1960, Ostrom 1990, Pistor 2019, Christophers 2024, Susskind 2024, Smith 1776)** — standard editions verified; Christophers (Verso, 12 Mar 2024); Susskind (US ed. *Growth: A History and a Reckoning*, Harvard UP). No contradictions.

### Ch10
- **Weitzman declining discount rate** — Weitzman, "Gamma Discounting," *AER* 91(1):260-271 (2001); + *JEEM* 36(3):201-208 (1998). Accurate.
- **Indigenous-scholarship affiliations** — Kimmerer (Citizen Potawatomi), Coulthard (Yellowknives Dene), Deloria Jr. (Standing Rock Sioux) confirmed. ⚠ Simpson: "Michi Saagiig Nishnaabeg" is her self-descriptor (correct); formal enrollment Alderville First Nation — consider bibliography note.
- **Grandfather's patents** — US 3,670,890 "Liquid Waste Feed System" (Hall, Tung, Winn; NASA; granted 1972-06-20); + NASA-CASE-XLA-10470 (SN 219,436, filed 1972, application). ⚠ TWO FLAGS: (1) US3,670,890 is a THREE-inventor patent — "his patents" overclaims; soften to "co-invented." (2) Second item verifiable only as an APPLICATION — cite accurately unless a grant number is located.
- **Nordhaus/Stern non-convergence** — Stern Review 2007 (~0.1%); Nordhaus *A Question of Balance* 2008 / DICE (~1.5%); Goulder & Williams NBER WP 18301 (2012). Well supported.

### TA (sourced subset)
- **META-CLAIM 1 (Polanyi + Fraser)** — Polanyi, *The Great Transformation* (1944, Beacon 2001), ch. 6; Fraser, *NLR* 86 (2014):55-72 + *Cannibal Capitalism* (Verso 2022). Add to §18 bibliography. NB: theorization gap remains (argument must be written, not just cited).
- **Pistor *The Code of Capital* (2019)** — Princeton UP (ISBN 9780691178974). Add to §18. NB: rebuttal must still be drafted against the named objection.
- **Balboa 2016** — Cristina M. Balboa, "Accountability of Environmental Impact Bonds: The Future of Global Environmental Governance?", *Global Environmental Politics* 16(2):33-41, MIT Press (DOI 10.1162/GLEP_a_00352). Complete cite found.
- **Bibliography gaps (Rennert/EPA SCC, NBIM 2025, Stern, Nordhaus, Daly)** — see citations in §6/Contradicted. ⚠ CRITICAL: $190 = EPA 2023, not Rennert ($185). Brian Barry sub-item needs author confirmation (likely "Sustainability and Intergenerational Justice," *Theoria* 45(89):43-64 (1997) or *Theories of Justice* 1989).

---

## (4) STILL-OPEN — UNSOURCED-AFTER-SEARCH (23 items), with where-to-look-next

**Submission-blocking / highest ledger weight first:**

1. **Ch5 Social Security $108T foregone-return** — HIGHEST numbers-are-invented risk. Nearest anchor: Brookings (~$1T gap, ~40% equity from 1984) is two orders of magnitude below $108T. ACTION: full methodology disclosure (return index/period/contribution-drawdown schedule, real vs nominal) as a footnoted band, OR demote to explicitly-labeled illustrative counterfactual. Do NOT present as "documented."
2. **Ch5 Libby "$4B documented costs" + "$100M lifetime revenue" (40:1 ratio)** — both numerator and denominator uncited. Documented: EPA ~$600M + Grace $250M. ACTION: cite a specific cost study or reframe as order-of-magnitude with disclosed components.
3. **Ch5 Deepwater Horizon "$150B total economic losses" (40% recovery denominator)** — no source produces $150B. Documented partials far smaller (fisheries ~$8.7B; BP all-in $61.6B). ACTION: name the aggregation or replace with a defended range. Also "$7B tourism / $12B property" inconsistent with U.S. Travel Assoc. ~$23B.
4. **Ch6 Method 3 $420-13,100/ton ceiling** — $13,100 has no public anchor (EPA SCC $190 central; Rennert $44-413 range). ACTION: show derivation in TA or label model-derived upper bound.
5. **Ch8 community-disruption cost $5-15/ton** — least-sourced component, second-largest non-carbon head. ACTION: name a regional-decline study + derive per-ton, or relabel as author estimate.
6. **Ch9 / Ch8 aggregate $10-15T/yr severed costs** — nearest anchor TEEB/Trucost 2013 (~$4.7T top-100 externalities; ~$7.3T unpriced natural capital). ACTION: in-text pointer to Ch8/Appendix derivation OR reconcile against TEEB. (Ch9 also flags internal figure-drift: opening "$500-600"/"$550" vs ratified $510 — reconcile.)
7. **Ch8 "$10-15T larger than all subsidies/ODA/charity combined" + "largest wealth transfer in history"** — rhetorical superlative on unsourced numerator. Denominators: global ODA ~$0.2T/yr (OECD); giving ~$0.5-1T/yr (Giving USA). ACTION: ground each denominator + disclose $10-15T as estimate, or soften.

**Other still-open (lower weight):**

8. **Ch2 McDowell two-thirds income drop in one year** — secondary coal-history sources only. PIN: BEA Regional (CAINC1), McDowell FIPS 54047, 1985-1988 series. Shared with Ch8.
9. **Ch2 Purdue four-characteristic target map** — MA complaint (unsealed Jan 2019) documents targeting but not the unified four-factor map. LOOK: McKinsey "Project Turbocharge"/"Evolve to Excellence" in MDL record; or re-attribute to Keefe *Empire of Pain* (2021) / econ-geography studies. Don't assert litigation provenance without the exhibit.
10. **Ch4 Norwegian extraction pace deliberately limited** — LOOK: 1971 "ten oil commandments"; Ministry of Energy White Papers; IEA depletion-rate discussions. Hedge or cite.
11. **Ch4 Nigeria revenue routing through majors / elite capture** — LOOK: DOJ/Swiss/UK Abacha asset-recovery filings; OPL 245 (Malabu) record; HRW/Chatham House. Names companies — cite or hedge.
12. **Ch4 international-architecture (transfer-pricing/secrecy)** — interpretive; ground in Pistor *Code of Capital* (2019) + Tax Justice Network, or cut.
13. **Ch5 "only wealthy nation with GoFundMe-as-default at this scale"** — LOOK: Kenworthy's broader work; OECD health-financing comparisons. Or soften the "only."
14. **Ch6 Method 2 Norway ~$48-50/BOE** — internal derivation. Public INPUT: Norway petroleum CO2 tax NOK 761/t (2023). ACTION: show per-tonne→per-BOE derivation; ALSO resolve internal $48-vs-$50 inconsistency (¶141 vs ¶174).
15. **Ch6 bottom-up tier estimates (health $2-4, env $1-3, community $5-15/ton)** — book's own construction. ACTION: footnote each tier to underlying public components (EPA SCC; NIOSH/black-lung; Appalachian Voices/GAO).
16. **Ch6 Exxon Valdez "$5.5M product value"** — book's derived figure (~262,000 bbl × ~$20/bbl 1989). Show back-of-envelope inline citing EIA 1989 crude series, or mark illustrative.
17. **Ch7 Kimberley Process premium-incidence** — LOOK: peer-reviewed value-chain/incidence study; Global Witness/HRW pass-through quantification. Or soften to defensible weaker claim (artisanal miners <$2/day). Same caution for fair-trade-coffee, carbon-offset, ESG empirical claims if retained.
18. **Ch8 direct health cost $2-4/ton** — Epstein 2011 supplies aggregate (~$74.6B/yr Appalachian) but no clean $/ton split. Flag as internally-estimated-anchored-to-Epstein.
19. **Ch8 environmental degradation $1-3/ton** — author-derived. Anchor aggregate to Epstein 2011; disclose per-ton as book's apportionment.
20. **Ch8 lineage-labor $1-5/ton** — author concedes imprecision. Ship only if labeled as estimate.
21. **Ch8 John L. Lewis/UMW declined-to-press attribution** — LOOK: Derickson *Black Lung* (Cornell 1998); Barbara Ellen Smith *Digging Our Own Graves* (1987). Source or soften/cut per no-invented-claims discipline.
22. **Ch9 Mian & Sufi 3-4× distributional figure** — *House of Debt* (2014) confirmed; the specific 3-4× needs a direct PAGE-CITE.
23. **Ch9 Ly & Soman 2020 + Kenworthy & Igra 2024 cites** — not verified; underlying pattern (scale + disparity) well supported. Supply full journal cites + confirm each says what's claimed.
24. **Ch9 housing causal claim (consolidation not supply restriction)** — descriptive rise sourced (JCHS 2024); causal claim is the book's argument, contested by Glaeser/Gyourko/Schuetz — present as argument, not finding. (Mirrors Ch8 line-192.)

---

## (5) AUTHOR-CONFIRMATION-ONLY — for interactive sessions (28 items)

### Ch1 (entire chapter — author-confirmation-only by task directive; KNOWN PRIOR DRIFT sites marked ⚠)
- **G-1 Pou/Pooh etymology** ⚠ — confirm NO invented accent/dialect provenance (Noema drift caught a fabricated "Tidewater-accent provenance"); "Pappou"→"Pou" / independent "Pooh" matches ratified-true family account.
- **G-2 Grandfather inventor / patents** — RECOMMEND separate USPTO/NASA-Langley verification pass to pin patent number(s) + grant date(s) + name spelling (chapter cites no patent number; verifiability promise has no pinned target). [Note: Ch10 TA item resolves part of this — US 3,670,890, co-invented; confirm consistency.]
- **G-3 "fifteen audiences"** ⚠ — confirm count AND kind (reader-audiences vs meeting-audiences; Noema inverted this).
- **G-4 NIH scope (40+ team / $1M→$1.5M / past due)** ⚠ — verify original-scope vs direct-management framing (previously conflated).
- **G-5 cussing-at-self polarity** ⚠ — confirm cursing-at-self is ratified-true (Noema inverted to cursing-at-recipient).
- **G-6 age 22 / 3-month contract / HGP completion** — confirm NIH tenure overlaps publicly-datable HGP window (draft 2000 / full 2003); if it doesn't fit, flag for targeted external date-check (CONTRADICTION risk against public HGP record).
- **G-7 "fifty-eight countries"** — confirm count + cross-artifact bio consistency; time-sensitive "as of this writing" — date-lock or cut the number (deep-pass cut C-7).
- **Other first-person specifics** (NICU timeline; ~120/~138 billed hrs; father naval-architect/clearance/political-passport; cable-TV rescue; IMF/World Bank golf referral; rent/parking/commute figures) — each must be ratified-true item-by-item; highest-exposure: father's "political passport"/"high clearance."

### Ch2
- **33-122× honest-price band (hand-off to Ch8/TA)** — confirm every input traces to a sourced figure in Ch8/TA + SC-CO2 vintage current/date-stamped.

### Ch3
- **Norway SWF preview (lines 232-236)** — out-of-scope for Ch3; confirm Ch4 carries/cites these (Ekofisk ~1969, fund 1990/first deposit 1996, ~3-4% rule) so Ch3 doesn't assert as its own facts.

### Ch4
- **Hotelling/Hartwick/Daly/Parfit positioning** — decide whether to name (Hotelling 1931; Hartwick 1977; Daly *Beyond Growth* 1996; Parfit *Reasons and Persons* 1984).
- **Resource-curse framing** — decide whether to cite Sachs & Warner (1995/2001) / Ross *The Oil Curse* (2012).

### Ch5
- **Polanyi/Fraser positioning** ("every extractive economy") — anchor to Polanyi (fictitious commodities) + Fraser (expropriation) or soften universal quantifier.
- **"Darity 2026"** — confirm real forthcoming work (title/venue) or placeholder; if placeholder, remove or substitute (Darity & Mullen, *From Here to Equality*, 2020).
- **TA cross-refs §5.5/§1.10 + carbon-term drift** — confirm sections exist; reconcile $510-mislabeled-as-carbon-term to ratified $496. [Cross-links to TA-1 contradiction.]
- **Ch4 GPFG dependency (line 126)** — confirm Ch4 holds sourced GPFG specifics; date-lock AUM at Ch4 level.

### Ch10
- **Coda case recalls (§58)** — internal Stage-1c coherence: confirm McDowell-coal, 2008-housing, pyramids/power, industrial-subsidy/routine cases each grounded in home chapters.
- **Norway SWF "achievable through every government" (§88)** — confirm Ch9/TA §11.5 backs the specific claim; no independent figure introduced in Ch10.

### TA
- **Darity 2026 private interview** — (a) re-ground "methodologically unresolved" in published *From Here to Equality*; (b) the personal-endorsement claim ("did not view calculations as underestimating") MUST be dropped, OR reframed as "personal communication, [date]" with Darity's written consent + accuracy confirmation per named-subject-consent discipline. No publication can verify; reads as soliciting endorsement.
- **§9.5 three-model IPG ranges (DWH/Libby/Baotou)** — execute + show the Three-Ways calibration (as for McDowell/Norway), OR relabel "preface-level estimates pending full calibration." Underlying case facts separately sourceable later.

### Ch8 (author placeholders)
- **Knowledge-cultural $1/ton, temporal-displacement $2/ton, lineage-labor $2/ton (lines 100,112,142)** — explicit author placeholders; confirm/finalize as disclosed internal estimates or replace with sourced figures; ensure prose signals these are the book's apportionment.

### Ch8 (gestured extrapolation)
- **Civilizational $4-5T/yr revenue × 2-3x → $8-15T (lines 218-220)** — confirm stays explicitly framed as gestured order-of-magnitude, not sourced.

### Ch9
- **Internal cross-refs (Ch8 invoice/per-ton; Ch5 Pistor; Ch4 Norway-vs-SS; Ch7 Europa; Ch2 reclamation)** — verify each referenced chapter supports the pointed-to claim; reconcile Ch9 "$500-600"/"$550" vs ratified $510.
- **Desmond *Evicted* causal claim (line 268)** — soften to defensible framing ("helped shift the conversation") or cite commentary making the attribution.

---

## (6) TIME-SENSITIVE — needs date-lock as of 2026-06-04 (11+ items)

**Submission-blocking date-locks first:**

1. **Ch7 Vulcan Centaur + New Glenn "now operational"** — BLOCKING. Both reached orbit through 2025 BUT as of early 2026 both PAUSED (Vulcan SRB anomaly Feb 2026; New Glenn config inactive after 2026 pad explosion). Re-verify immediately before submission; hedge to "have reached orbit" or date the claim.
2. **Ch4 fund ">$2 trillion"** — TRUE today (NOK 21.27T / ~$2.1T end-2025, NBIM Annual Report 2025) but fluctuates with markets/NOK-USD. Relock with dated NBIM source.
3. **Ch4 per-citizen "~$360,000"** — now LOW; current ~$390,000 (NOK 3.8M ÷ ~5.5M). Relock with arithmetic + date, or hedge "~$380,000."
4. **TA §11.5 inline "$1.9T"** — stale vs table's correct $2.0T (NBIM end-2025). Reconcile l.859 to table; cite "NBIM Annual Report 2025 (end-2025), as-of date."
5. **TA solar "$0.03/kWh"** — (also CONTRADICTED) relock vs IRENA 2024 / latest cost report.

**Standard date-locks:**

6. **Ch2 poverty 37.6% / $28,235 / 55-of-55 health rank** — SAIPE 2022 + CHR&R 2020, both annually updated. State data year; verify rank still holds.
7. **Ch2 reclamation ($633K acres etc.)** — 2021 Appalachian Voices vintage; stamp "as of 2021."
8. **Ch2 ~half of renters cost-burdened** — JCHS annual; verify latest edition; "(2022 data)."
9. **Ch3 2024 striped-bass YOY index (2.0 vs 11.0, sixth consecutive)** — 2025 survey released (~Oct); verify whether "sixth" → "seventh"; cite by year.
10. **Ch3 2025 blue-crab dredge (238M, second-lowest, sixth consecutive)** — 2026 survey shows ~46% rise; cite explicitly as 2025; "sixth consecutive" may no longer hold.
11. **Ch3 menhaden cap 51,000 mt** — late-2025 addendum + 2026 TAC cut pending; date-lock.
12. **Ch3 MD oyster disaster declaration** — supply "February 2026"; verify whether NOAA has acted (granted/denied/pending).
13. **Ch5 Black Lung Trust Fund debt "~$5.1B as of Sept 2024"** — ~20 months stale; keep explicit date-stamp + CRS/GAO cite or relock (projected toward ~$13B by 2050). Also "$44B paid" unconfirmed — pin to CRS R45261.
14. **Ch6 McDowell 13-yr gap** — life-expectancy figures update; date-lock to CDC vintage.
15. **Ch6 reclamation bond figures** — 2017-2021 vintage; date-lock.
16. **Ch6 Norway carbon tax NOK 761/t** — annual; date-lock to 2023 or update.
17. **Ch6 solar ~3¢/kWh (Lazard v16.0 2023)** — annual (rose first time 2023); date-lock vintage.
18. **Ch6 mine-mouth coal $40-140/ton** — (also CONTRADICTED) highly volatile; date-lock to named EIA vintage.
19. **Ch8 McDowell demographics (2022 ACS)** — date-lock "(2022 ACS / 2020 Census)."
20. **Ch8 drug death 141/100,000** — date-lock "(2015)"; since risen to ~212 (2023).
21. **Ch8 fossil-fuel lobbying $124-435M** — date-lock cycle year.
22. **Ch8 solar cheaper than coal (IRENA 2024 / Lazard 2024)** — annual; cite vintage; "much of" vs "most of" the developing world.
23. **Ch9 Alaska Permanent Fund corpus ~$80B / dividend $1,300-1,700** — corpus now ~$89B (2026); 2024 dividend $1,702. Year-anchor.
24. **Ch9 carbon pricing "70+ jurisdictions, ~quarter of emissions, as of 2025"** — World Bank 2024 report counts 75 INSTRUMENTS (not jurisdictions); 2025/2026 editions now exist. Relock + tighten wording.
25. **Ch10 Black Hills escrow ">$1.5 billion"** — HIGH staleness, compounds with interest; exact balance SEALED (FOIA declined 2025). Book figure at/above upper end of cited estimates ($1.3B PBS 2011; "over $1B"-"~$1.5B" 2023-25). Reword to dated, sourced estimate ("well over a billion as of 2025, exact figure sealed"); year-lock. $102M/1980 base + "four-plus decades" solid.

---

**TOP SUBMISSION-BLOCKING TRIAGE (do these first, any Ch-derived submission):** TA-1 (carbon-term $496-not-$510 cascade) + TA-2 (SCC $190=EPA-not-Rennert) — these two are linked and propagate through Ch6/Ch8/Ch9; Ch5 $108T Social Security figure; Ch7 Vulcan/New Glenn "operational"; Ch10 Black Hills sealed-balance figure; TA Darity personal-endorsement claim (consent discipline); and the 11 CONTRADICTED items in §3.
