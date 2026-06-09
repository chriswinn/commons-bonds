# Ch 2 — The Miner (McDowell coal spine) — Citation Apply-Spec

**Created:** 2026-06-08
**Chapter prose (clean):** `manuscript/chapters/Chapter__2_TheMiner_Draft.md`
**Purpose:** per-figure reconciliation of the 2026-06-04 citation-evidence ledger + JSON detail with the 2026-06-08 corpus primary-source register (§1A/1B + §6), against the canonical figure ledger. One row per empirical figure/claim in Ch2. This is an APPLY-SPEC (internal scaffolding); the chapter is end-user-facing prose → all applications require author ratification per the merge-on-ratification pipeline. Do NOT unilaterally edit chapter prose from this file.

**Status legend:**
- **READY-TO-CITE** — external primary source located, URL in hand; attach citation as-is.
- **NEEDS-PIN** — source CATEGORY known + figure corroborated, but the exact locatable document/URL still has to be regenerated or pinned (often "regenerate the agency query" or "find the specific CRS/GAO doc").
- **AUTHOR-CONFIRM** — memoir / on-record-quote / personal; verify quote accuracy or get courtesy-notify, not library research.
- **UNVERIFIABLE** — no primary source found; relabel as estimate, attribute to secondary origin, or cut.
- **FRAMEWORK-OUTPUT** — book-computed (IPG/RCV/CS/per-ton allocation); label "framework-computed, derivation shown," never external-cite.

---

## Part A — Socioeconomic / demographic spine (recurs Ch6/Ch8)

| Figure | Status | Source (+URL) | Note |
|---|---|---|---|
| Population 98,887 (1950) → 19,111 (2020) (lines 54, 26) | READY-TO-CITE | US Census 1950 Census of Population Vol. II WV (https://www2.census.gov/library/publications/decennial/1950/pc-02/pc-2-02.pdf) + QuickFacts McDowell Co. (https://www.census.gov/quickfacts/fact/table/mcdowellcountywestvirginia/PST045224). HIGH | 1950 PDF didn't machine-parse — **visually confirm the 98,887 cell before print.** Canonical ledger says "~19,000 / under 20,000" — prose's exact 19,111 is fine + sourced. |
| Male life expectancy ~63.5 vs national ~76.5 (13-yr gap) (line 56) | READY-TO-CITE / NEEDS-PIN | Dwyer-Lindgren et al. (IHME), *JAMA Internal Medicine* 2017 (https://jamanetwork.com/journals/jamainternalmedicine/fullarticle/2626194; PMID 28492829); exact county figures in IHME county dataset (healthdata.org). MED-HIGH. Darity packet (§6A) also attributes the 13-yr gap to CDC + RWJF County Health Rankings | **Regenerate the IHME county profile to cite the exact 63.5/76.5 directly** (paper gives method; county dataset gives the cell). Chapter spine figure, recurs Ch6 ¶32/295 + Ch8. |
| Drug-death rate ~141/100k vs national ~16 (lines 56, 194) | NEEDS-PIN | CDC NCHS / CDC WONDER (drug-induced mortality, McDowell FIPS 54047). MED | Figure surfaced via Rockefeller Institute analysis; **regenerate the CDC WONDER query to cite CDC directly.** Chapter says "from the same period" — pin the year (register notes 2015) and confirm national ~16 same-year. Recurs Ch8. |
| Poverty ~37.6%; median household income ~$28,235 (line 56) | READY-TO-CITE | US Census ACS 5-yr via QuickFacts (URL above). HIGH | **Confirm ACS vintage year matches book's stated period.** |
| Ranks 55th of 55 WV counties in health outcomes (line 56) | NEEDS-PIN | RWJF County Health Rankings (countyhealthrankings.org), McDowell Co WV. Category known via Darity packet §6A; specific edition/year not yet pinned | Pin the specific ranking-year edition. |
| First food stamps under the modern (1961 pilot) program issued here (line 56) | NEEDS-PIN | Historical claim (Welch / McDowell Co., May 1961 pilot under the Kennedy EO). Tier-2 in ledger; no primary doc attached yet | Locate USDA FNS SNAP history / Kennedy-era pilot record (Paul & Pauline Williams = first recipients, Welch WV). Low-risk historical but currently uncited. |

## Part B — Mechanization / income / closure

| Figure | Status | Source (+URL) | Note |
|---|---|---|---|
| U.S. Steel Gary mine closed 1986, >1,200 jobs (line 50) | UNVERIFIABLE (year) / NEEDS-PIN (jobs) | Register §3: conflicting years (1982/1984/1986) across sources; no primary employment record. Canonical ledger J5 RESOLVED → harmonize to "across the 1980s" framing, NOT a point-year | **Conflict with canonical ledger.** Prose currently states "1986" + "more than twelve hundred jobs." J5 says do not state a hard year as fact until locked to a primary source; soften to "across the 1980s / mid-1980s." 1,200-jobs count needs a contemporaneous record. Ch8 flags 1986 contested. |
| Income fell ~13% in a single year + ~15% across mid-decade peak (line 52) | NEEDS-PIN | BEA local-area personal income (CAINC series, McDowell Co.) — candidate, not yet pulled | **NB prose was already softened** from the prior "two-thirds / dropped by two-thirds" claim (JSON detail flags the old line-40 "two-thirds" as striking+unsourced) to ~13%/~15%. Pull BEA CAINC to confirm the new figures. Lower-risk than the retired version. |

## Part C — Black lung: epidemiology + program

| Figure | Status | Source (+URL) | Note |
|---|---|---|---|
| ~1 in 5 (20%) central-Appalachian miners w/ 25+ yrs underground have black lung (line 78) | NEEDS-PIN | NIOSH Coal Workers' Health Surveillance Program / Blackley et al. (NIOSH), *AJPH* 2018 PMP-prevalence studies. Category known (NIOSH); specific paper not yet pinned | Pin the NIOSH/AJPH prevalence paper (Blackley, Halldin, Laney 2018 reported ~1-in-5 in central Appalachia). |
| Nationally >1 in 10 long-tenured miners (line 78) | NEEDS-PIN | Same NIOSH surveillance line | Pin alongside the 20% central-Appalachia figure. |
| Disease costs 8–13 years of life per case (line 78) | NEEDS-PIN | Epidemiology cite needed (NIOSH / years-of-life-lost study) | Source category known; specific YLL study not pinned. |
| Resurgence — rising again, fastest among younger miners, severe/rapid PMF (line 80) | NEEDS-PIN | NIOSH + Blackley et al. (progressive massive fibrosis resurgence, central Appalachia) | High-visibility/contested claim — pin a NIOSH/epidemiology cite. Case-study note #5 flags longwall/silica-dust mechanism as expansion territory. |
| Black Lung Benefits Program established 1969 (lines 82, implied) | READY-TO-CITE | Public-record institutional founding fact; federal Black Lung Benefits Act of 1969 | Statute/founding date safe as named public record. |
| **Program has paid out ~$44 billion in benefits** (line 82) | UNVERIFIABLE / NEEDS-PIN (likely STALE) | Register §3 + §6B: in-house Darity docs attribute to "DOL OWCP / BLDTF annual reports" (TA) and **"$44B through 2009 (GAO/CRS)"** (Ch6). Exhaustive search (GAO-18-351, Brookings 2021, web) found no "$44B" — consistent with a **~2009 figure (likely CRS R45261, which 403'd)** | **FLAGGED — highest-priority integrity item in Ch2.** The same number is presented as "through 2009" (Ch6) AND "cumulative 1969–present" (TA §11.6) — a number can't be both. Ch2 prose says "paid out around forty-four billion" with no end-year → reads as current cumulative; likely a stale 2009 figure undercounting if anything. **Action:** pin the GAO/CRS "through 2009" doc and relabel "≈$44B through 2009 (GAO/CRS)," OR pull current cumulative from DOL OWCP annual reports. Do NOT let it stand as bare current cumulative. |
| Trust Fund "debt of several billion" (line 82) | READY-TO-CITE | GAO-18-351 + GAO-19-622t + Brookings 2021 → **$5.1B outstanding debt** (register §1B). HIGH | Prose hedges to "several billion" (safe); can pin exact $5.1B w/ year. Canonical ledger J4: keep dated "$4.5B (2021)" as defensible vintage anchor if a single figure is wanted — reconcile $5.1B (register) vs $4.5B (2021, ledger J4) by stating the year. |
| Borrowed from general fund almost every year since 1979 (line 82) | READY-TO-CITE | GAO-18-351 / GAO-19-622t (register §1B). HIGH | Safe; pin the GAO doc. |
| Projected to owe ~$15 billion by 2050 (line 82) | READY-TO-CITE | GAO → **$15.4B projected by 2050** (register §1B). HIGH | Prose "roughly fifteen billion by 2050" matches GAO $15.4B. Pin GAO. |
| ~$865M black-lung obligations moved to public via 3 coal bankruptcies, 2014–2016 (line 82) | READY-TO-CITE | **GAO-20-21, Feb 2020** (https://www.gao.gov/products/gao-20-21). HIGH. (3 cos = Alpha, James River, Patriot.) Darity §6A corroborates via OSMRE bankruptcy filings | Strong, locatable, dated. Prose "around 2014 to 2016, three large coal companies" + "$865 million" matches GAO-20-21 exactly. **READY.** |

## Part D — Reclamation / acid mine drainage

| Figure | Status | Source (+URL) | Note |
|---|---|---|---|
| SMCRA 1977 reclamation-bond requirement (line 92) | READY-TO-CITE | Surface Mining Control and Reclamation Act of 1977 — named statute, public record | Safe as named statute. |
| >633,000 acres need remediation; cleanup $7.5–9.8B; bonds ~$3.8B; gap ~$4–6B (line 94) | READY-TO-CITE | **Appalachian Voices, *Repairing the Damage*, 2021** (https://appvoices.org/coal-impacts/repairing-the-damage/). HIGH. Already in TA §23 bib | **READY.** NB §6A: the Darity packet's separate number was "150,000 McDowell acres / $3.7–6B national" (OSMRE/GAO-17-207R/Yang & Davis 2021) — a DIFFERENT figure; Ch2's 633k-acre / $7.5–9.8B is the Appalachian Voices figure. Keep them straight; cite Appalachian Voices for the prose as written. Register §2.14 flags reclamation-gap stated inconsistently across Ch6/Ch8 — reconcile to the Appalachian Voices arithmetic book-wide. |
| Acid mine drainage chemistry (orange iron sulfide; persists post-closure) (line 90) | READY-TO-CITE | General AMD science — safe as descriptive; can anchor to USGS/EPA AMD pages if a cite is wanted | Descriptive, low-risk. |

## Part E — Vocabulary / intellectual lineage

| Figure | Status | Source (+URL) | Note |
|---|---|---|---|
| Mazzucato, *The Value of Everything* (2018) — making vs taking (lines 138) | READY-TO-CITE | Named work, cited by title/year. Ledger Part 1A | Lineage cite, submission-ready. |
| Harvey, *The New Imperialism* (2003), Ch4 — accumulation by dispossession (line not in clean draft? — verify) | READY-TO-CITE w/ CAVEAT | Named work. Ledger 1A; JSON flags the sub-claim "Harvey is the lineage behind Mazzucato" (deep-pass ISSUE B) as contestable/unsourced | **NB:** the Harvey citation is in the JSON's existing-citation list (prior draft line 152) but I did NOT find the Harvey sentence or the "lineage behind Mazzucato" claim in the current clean draft (the clean draft's lineage para ends at Mazzucato, line 138). If a redline reintroduces Harvey, drop/soften the contestable intellectual-history sub-claim. |
| Nancy Fraser — "expropriation, accumulation by means other than the wage contract" (line 192) | NEEDS-PIN | Fraser, "Behind Marx's Hidden Abode," *New Left Review* 86 (2014), or *Cannibal Capitalism* (2022) | **Ledger Tier-0 #3** flags Polanyi/Fraser as having "zero textual presence" doing load-bearing meta-claim work book-wide. Ch2 invokes Fraser's "expropriation" by name → pin the specific Fraser work. |

## Part F — Mine-mouth price + magnitude (canonical-figure interlock)

| Figure | Status | Source (+URL) | Note |
|---|---|---|---|
| 1960 mine-mouth price "just under five dollars a ton" (line 68) | READY-TO-CITE | **EIA Total Energy Table 7.9 / ptb0709** (https://www.eia.gov/totalenergy/data/annual/showtext.php?t=ptb0709): ~$4.71/short ton bituminous ($4.83 all-coal). HIGH | Canonical ledger J3 AMENDED: harmonize to ~$4.70–4.85 (EIA), phrase "just under five dollars." Ch2 prose ALREADY says "just under five dollars a ton" → **compliant; cite EIA.** (Old $4.50 undershot; not present in clean draft.) |
| IPG / 33–122× magnitude band ("the whole-cost ledger dwarfs the price") (implicit; case-study line 14) | FRAMEWORK-OUTPUT | Register §4 / canonical ledger J2: framework-computed; "framework-computed, derivation shown" labeling, never external-cite | Canonical ledger cascade target lists **Ch2 (IPG framing)** as "still needs editing." Public headline 33–122×; ~50× triangulated central; 555× confined to TA. If Ch2 surfaces an IPG multiple, label it framework-output + match the canonical band. (Clean draft is light on explicit multiples — verify none drift.) |

## Part G — Second cycle (opioid / Purdue-Sackler)

| Figure | Status | Source (+URL) | Note |
|---|---|---|---|
| Purdue targeted high-prescribing physicians + "large unmet need for a vulnerable, underserved, stigmatized population" (line 190) | NEEDS-PIN | Litigation record — *Commonwealth v. Purdue* (Massachusetts AG) unsealed complaint + unsealed internal documents | Quoted internal-document language → pin the specific unsealed complaint/exhibit. Keefe, *Empire of Pain* (2021) is the secondary anchor already cited. |
| McKinsey "turbocharge sales" / "evolve the prescriber base to higher volumes" (line 190) | NEEDS-PIN | Documents surfaced through the 2021 McKinsey multistate settlement (NAAG) | Pin the settlement-document source for the verbatim phrases. |
| Art Van Zee 2009, *AJPH* — Purdue's 1996 push into distressed mining/logging areas (line 192) | READY-TO-CITE | Van Zee A., "The Promotion and Marketing of OxyContin," *American Journal of Public Health* 99(2):221–227 (2009) (PMC2622774) | Named author/journal/year present in prose → **READY**, pin DOI/PMC. |
| "Economists later traced the same geography with hard causal methods" (line 192) | NEEDS-PIN | Candidate: Alpert, Powell, Pacula (NBER/AEJ) opioid-supply causal work; or Evans-Lieber-Power | Vague gesture → pin a specific causal-econ paper or soften the "hard causal methods" claim. |
| Sackler family pulled ~$11 billion out before bankruptcy (line 194) | NEEDS-PIN | Litigation/settlement record — DOJ 2020 + 2021 Purdue bankruptcy disclosures (~$10.4B figure cited in court records); Keefe secondary | Pin the bankruptcy-record / DOJ source for the ~$11B. Case-study file uses ~$11B. |
| Big Three distributors (McKesson, Cardinal Health, AmerisourceBergen) settled 2022 for $21 billion (line 194) | READY-TO-CITE / NEEDS-PIN | National Prescription Opiate Litigation / state-AG global settlement, Feb 2022 (~$21B distributors; $26B incl. J&J). NAAG / settlement site | Locatable public settlement → pin the NAAG/AG announcement URL. Prose "$21 billion" = distributor share (correct). |
| Purdue pleaded guilty twice: 2007 felony misbranding + 2020 three federal felony counts (lines 194) | READY-TO-CITE | DOJ press releases: 2007 (W.D. Va.) misbranding plea; 2020 (DOJ, Oct 21 2020) global resolution | Public DOJ record → pin both DOJ URLs. Prose accurate. |
| 141/100k overdose rate re-used as "signature of a vulnerability that was found" (line 194) | (cross-ref Part A) | CDC WONDER (see Part A drug-death row) | Same figure as Part A; one CDC WONDER pin clears both uses. |

## Part H — On-record interview quotes (public-record exception → courtesy-notify, NOT consent)

| Figure | Status | Source (+URL) | Note |
|---|---|---|---|
| JFK Canton OH speech, Sept 1960 ("mines more coal... than any county") (line 16) | AUTHOR-CONFIRM (quote-accuracy) | JFK campaign speech, Canton OH, Sept 1960 (public record, JFK Library) | Public utterance; verify verbatim wording vs JFK Library transcript. |
| Robert Bailey — "almost like drowning"; "most laws... written with blood" (lines 38, 42) | AUTHOR-CONFIRM (quote-accuracy) | WV Public Broadcasting / *Inside Appalachia*, host Jessica Lilly, Feb 2019 | Public-record exception (named on-record interview). Deceased Feb 2019 → courtesy-notify-family discipline; verify quote accuracy. Per no-invented-facts memo, Bailey biographical specifics were a prior Pass-3.1 near-miss — confirm no invented detail. |
| Ted Latusek — "bag over my face"; "outlive Consol"; "loyalty wasn't there for me" (lines 156–160) | AUTHOR-CONFIRM (quote-accuracy) | Chris Hamby, Center for Public Integrity, 2013 | Public-record exception. Redline note (chapter header) flags "Latusek 'knife in my gut' restore" — verify any restored quote against the CPI source verbatim. |

---

## Summary — status counts (≈27 distinct figures/claims)

- **READY-TO-CITE:** ~10 (population, life-exp paper, poverty/income, $865M GAO-20-21, trust-fund debt/borrowing/$15B-2050, reclamation 633k/$7.5–9.8B Appalachian Voices, SMCRA, Mazzucato, EIA $4.71 coal price, Van Zee 2009, Big-Three $21B settlement, Purdue plea record)
- **NEEDS-PIN:** ~12 (drug-death CDC WONDER, health-ranking edition, food-stamp history, BEA income %, black-lung 20%/1-in-10/8–13yr/resurgence NIOSH cluster, Fraser work, Purdue internal-doc + McKinsey phrases, causal-econ paper, Sackler ~$11B)
- **AUTHOR-CONFIRM:** 3 (JFK, Bailey, Latusek on-record quotes — verify verbatim + courtesy-notify)
- **UNVERIFIABLE / FLAGGED:** 2 (U.S. Steel Gary year+1,200 jobs; $44B black-lung payout likely-stale-2009)
- **FRAMEWORK-OUTPUT:** 1 (IPG 33–122× magnitude band)

## Highest-priority still-unsourced / flagged

1. **$44B black-lung payout (line 82) — FLAGGED likely-stale.** Reads as current cumulative but is most likely a "through 2009" GAO/CRS figure (probably CRS R45261). Pin the 2009 doc + relabel "≈$44B through 2009," or pull current DOL OWCP cumulative. Integrity exposure, not just a missing cite.
2. **U.S. Steel Gary closure "1986 / 1,200 jobs" (line 50) — conflicts canonical ledger J5.** Soften the hard year to "across the 1980s" per J5; 1,200-jobs count has no primary employment record.
3. **Black-lung epidemiology cluster (lines 78–80)** — 20% / >1-in-10 / 8–13yr / resurgence all NEEDS-PIN to NIOSH (Blackley et al. 2018 + PMF-resurgence work). One NIOSH sourcing pass clears four claims.
4. **Purdue/McKinsey internal-document verbatim phrases (line 190)** — pin the Massachusetts unsealed complaint + McKinsey 2021 settlement docs for the quoted language; Sackler ~$11B needs the bankruptcy-record cite.
5. **Fraser "expropriation" (line 192)** — pin the specific Fraser work (ledger Tier-0 Polanyi/Fraser empty-anchor item).

## Cross-chapter note
Life-expectancy 13-yr gap, drug-death 141/100k, poverty/income, reclamation gap, and the black-lung program figures all recur in Ch6/Ch8. One sourcing pass on this spine clears three chapters (per ledger Part 4 recommendation (c)). Keep the reclamation-gap arithmetic reconciled to Appalachian Voices book-wide (register §2.14).
