# Ch 6 — Three Ways of Counting — Citation Apply-Spec

**Created:** 2026-06-08 · **Chapter:** Ch 6 (coal accounting; Methods 1/2/3; DAC; SCC; convergence table)
**Clean prose:** `manuscript/chapters/Chapter__6_ThreeWaysofCounting.md`
**Status:** internal scaffolding (NOT applied to prose — chapter prose is end-user-facing → author/chapter-session pipeline + ratification).

**Sources merged:** Citation Evidence Ledger (Ch6 block) + `_citation-evidence-detail` JSON (Ch6) + `_CANONICAL_FIGURE_LEDGER.md` + `corpus-primary-source-register_2026-06-08.md` (§1/§2/§6) + the Darity **with-citations PDF** (`research/outreach/subjects/darity/Chapter_6_..._with-citations_2026-05-14.pdf`).

**What the with-citations PDF covers (and doesn't):** It is the same prose as the clean chapter, with the **convergence-table cells already carrying inline source attributions** (Deepwater → BP response ~$14B + NRDA $8.8B per **2016 Consent Decree** [NOAA/DOJ]; Libby → ~$0.6B **EPA Superfund** + W.R. Grace components [Montana DOJ/W.R. Grace filings]; Exxon Valdez → Exxon $2.2B + NRDA ~$100M per **1991 settlement** [EVOSTC/DOJ 1991]) plus the ¶181 prose naming those agencies. It carries **NO separate bibliography, footnotes, or per-figure cites** for the bottom-up tiers, the 1960 coal price, DAC bands, or the Norway/Method-2 figures — those remain inline-prose-only or unsourced. It still carries the **pre-fix $4.50** and **$48-vs-$50 Norway** figures (PDF predates the canonical-ledger amendments).

**Status legend:** READY-TO-CITE (source+URL in hand) · NEEDS-PIN (source family known, exact doc/page not locked) · AUTHOR-CONFIRM (author fact/decision needed) · UNVERIFIABLE (no primary located) · FRAMEWORK-OUTPUT (framework-computed → derivation-shown label, NOT external cite).

---

## A. Empirical figures

| Figure | Status | Source (+URL) | Note |
| --- | --- | --- | --- |
| 1960 mine-mouth coal price "$4.50/ton" (¶38, ¶80, table ¶173) | **AUTHOR-CONFIRM / correction** | EIA Total Energy Table 7.9 / ptb0709 — 1960 bituminous **$4.71** (all-coal $4.83) — https://www.eia.gov/totalenergy/data/annual/showtext.php?t=ptb0709 (HIGH) | **CORRECTION.** Canonical ledger (RATIFIED 2026-06-04, J3) amends $4.50 → **~$4.70–4.85 / "just under five dollars"**; old $4.50 undershoots EIA primary series ~5–7%. Cascades into IPG ratios + the table Market-Price cell. PDF still shows $4.50. |
| CO₂ emission factor 2.32 t/short ton (national-bituminous, ¶42) | **READY-TO-CITE** | EPA AP-42 §1.1, 93.28 kg CO₂/mmBtu × ~24.9 mmBtu/short ton — https://www.epa.gov/air-emissions-factors-and-quantification/ap-42-compilation-air-emissant-and-quantification (verify exact AP-42 §1.1 URL) (HIGH) | Two-basis split ratified: 2.32 national / **2.61** McDowell-Pocahontas (28 mmBtu/short ton). Keep both with rationale; cite the heat-content source (USGS/EIA Pocahontas) explicitly so a reviewer can't swap 2.32 into the McDowell case. |
| SCC $190/ton CO₂ (¶42, ¶48, ¶56, ¶60, ¶62, ¶153) | **READY-TO-CITE / attribution-fix** | **EPA 2023** Report on the SCGG (central estimate at 2% discount) — EPA *drew on* Rennert et al. 2022 *Nature* (whose own central was ~$185) — https://www.epa.gov/environmental-economics/scghg (HIGH) | **CANONICAL ATTRIBUTION FIX:** cite **EPA 2023** for $190; do NOT attribute $190 to Rennert. ¶62 currently says "drawn from Rennert and colleagues 2022" — relabel to EPA-2023-drawing-on-Rennert. |
| Carbon externality "$441/ton" national basis (¶42) | **FRAMEWORK-OUTPUT (derivation-shown)** | = 2.32 × $190 (cited inputs) | Output of cited inputs; label "derivation shown." Already matches canonical J6 ($441 national). ✓ Consistent in both clean chapter and PDF. |
| Bottom-up total "$449 to $464/ton" (¶44) | **FRAMEWORK-OUTPUT / cascade-check** | = $441 carbon + $8–22 non-carbon heads | Derivation-shown. Internally consistent with $441 national basis. Leave (national-basis band); do NOT confuse with McDowell-basis figures below. |
| Pigouvian floor "$518 to $532/ton" (¶343) | **FRAMEWORK-OUTPUT / CORRECTION** | = $496 carbon (McDowell 2.61 basis) + $8–22 heads → **$504–518** | **CASCADE CORRECTION (J1/J6 live in Ch6).** Canonical 4-component Pigouvian floor = **$504–518**, NOT $518–532. ¶343 currently overshoots. This is the live "$510→$496"-family carbon cascade item for Ch6. Recompute after input-fix. |
| Carbon term McDowell basis "$496" (¶343 implied; ¶42 cross-ref) | **FRAMEWORK-OUTPUT (derivation-shown)** | = 2.61 × $190 = $495.90 ≈ **$496** | Canonical: **$496 = carbon term** (McDowell). Pin label; never label $510 as carbon term. |
| Black Lung Program "~$44B distributions through 2009 (GAO/CRS)" (¶28) | **NEEDS-PIN / likely-stale** | GAO/CRS — pin specific doc (likely **CRS R45261**, 403'd in search); register §3/§6B (MED) | $44B is attributed to "GAO/CRS" category, not a locatable doc; date-discrepant ("through 2009" here vs "1969–present/56-yr" in TA §11.6). **Likely a ~2009 figure presented as current.** Action: pin the 2009 GAO/CRS doc and relabel "≈$44B through 2009," OR get current cumulative from DOL OWCP annual reports. |
| Black Lung health-tier "$1–1.5/ton" + "$2–4/ton conservative" (¶28) | **FRAMEWORK-OUTPUT / NEEDS-PIN** | $44B ÷ national tonnage (derivation); aggregate $2–4 tier has no inline cite beyond Black Lung sub-component | Per-ton allocation is framework-computed (derivation-shown); the $44B input needs pinning (row above). The $2–4 aggregate health tier is otherwise unsourced. |
| Reclamation bonds "$3.7 to $6 billion short" (¶30) | **READY-TO-CITE / reconcile** | Darity packet: **OSMRE + GAO-17-207R + Yang & Davis 2021** ($4–6B; $865M bankruptcy transfer = OSMRE filings) (§6A). Alt: Appalachian Voices *Repairing the Damage* 2021 (633,000 ac / $7.5–9.8B cleanup / ~$3.8B bonds / ~$4–6B gap) — https://appvoices.org/coal-impacts/repairing-the-damage/ (HIGH) | **RECONCILE:** Ch6 says "$3.7–6B"; Ch8 says "$3.5–6B / $4–6B" (register §2.14). Two source families: packet's 150,000 McDowell-acre / $3.7–6B national vs Appalachian Voices 633,000-acre. Pick one basis and harmonize Ch6↔Ch8. |
| Environment tier "$1–3/ton" (¶30) | **NEEDS-PIN** | no inline public source | Aggregate tier asserted as "conservative"; no cite. |
| Community-cost tier "$5–15/ton" (¶32, ¶36, ¶343) | **NEEDS-PIN** | no inline public source | Aggregate tier unsourced. |
| 13-yr life-expectancy gap, McDowell (¶32, ¶295) | **READY-TO-CITE** | Dwyer-Lindgren et al. (IHME), *JAMA Internal Medicine* 2017 — https://jamanetwork.com/journals/jamainternalmedicine/fullarticle/2626194 (PMID 28492829); county figures in IHME dataset. **Darity packet attributes: CDC + RWJF County Health Rankings** (§6A) (MED-HIGH) | Regenerate IHME county profile to cite exact 63.5/76.5 directly. Recurs Ch2/Ch8 — one sourcing pass clears three chapters. |
| Darity "6–7 yr Black-vs-white longevity gap" priced as legacy effect (¶34) | **READY-TO-CITE** | **Bassett-Bell, Williams, Darity et al.,** "Association Between Racial Wealth Inequities and Racial Disparities in Longevity…1992–2018," *JAMA Network Open* 5(11):e2240519 (2022) (already in TA §18; §6A) (HIGH) | Was "needs-research" in JSON (methodology attributed only to "Darity Jr. and collaborators"); **now pinned** via Darity packet. Add to §23 bib. |
| Contemporary mine-mouth "$40 to $140/ton" (¶38) | **NEEDS-PIN** | EIA / USGS coal price series (region/grade) — not yet pinned | No source cited for contemporary range. |
| Solar "$0.03/kWh" (¶76); "renewables already displacing coal at scale" (¶100) | **NEEDS-PIN** | LBNL / Lazard LCOE (public) — not yet pinned | LCOE figure needs LBNL or Lazard cite. |
| DAC: Climeworks Orca ~$1000+/ton; Mammoth 2024; Gen-3 → $400–600 net / $250–350 capture-only by 2030 (June 2024 Zurich Carbon Removal Summit) (¶60) | **READY-TO-CITE** | Climeworks corporate disclosure (June 2024 Zurich Summit); register §1F/§6A (Climeworks/CE-1PointFive/IEA/IPCC/NAS already verified) (HIGH) | DAC bands verified earlier this session (register §1F). |
| DAC: Carbon Engineering Stratos (TX) $300–600/ton full op (¶60) | **READY-TO-CITE** | Carbon Engineering / 1PointFive Stratos disclosure; register §1F (HIGH) | |
| DAC: IEA *Direct Air Capture 2022* $230–600/ton scaled (¶60) | **READY-TO-CITE** | IEA, *Direct Air Capture 2022* — https://www.iea.org/reports/direct-air-capture-2022 (HIGH) | |
| DAC: IPCC AR6 WGIII $100–300/ton mid-century (¶60) | **READY-TO-CITE** | IPCC AR6 WGIII (2022) (HIGH) | |
| Government Pension Fund Global "~$2.2 trillion (early 2025 NBIM)" (¶219) | **READY-TO-CITE / vintage-flag** | NBIM — NOK 21,268B (>$2T) end-2025 — https://www.nbim.no/en/investments/the-funds-value/ (HIGH) | Time-sensitive; packet states GPFG three ways ($1.9T/$2.0T/$2.2T) — reconcile to one vintage (register §6D-16). Per-citizen now ~$390k. |
| Norway carbon tax "introduced 1991, one of world's earliest"; "highest rates" (¶221) | **NEEDS-PIN** | Norwegian Petroleum (78% combined marginal petroleum tax) — https://www.norskpetroleum.no/en/economy/petroleum-tax/ (HIGH for 78%); carbon-tax-1991 date needs its own pin | Multiple sourceable claims, none cited. "Highest rates" recast needed (don't conflate marginal rate with aggregate take, register §2). |
| Norway fiscal rule "expected real return, currently around three percent" (¶221) | **AUTHOR-CONFIRM / correction** | regjeringen.no — rule introduced **2001 at 4%**, lowered to **3% in 2017** (HIGH) | **CORRECTION (register §2.1).** The 3% figure is correct as the *current* rate, but the chapter must not imply 3%-since-inception; rule was **4% in 2001 → 3% in 2017**. Flagged in prompt as "fiscal-rule 3%-in-2017-not-2001 (Ch6:221)." Ch6:221 as written ("currently around three percent") is defensible *if* no 2001-origin claim is attached; confirm the date pairing isn't asserted elsewhere. |
| Norway ethics-council public divestments (¶221) | **NEEDS-PIN** | Council on Ethics / NBIM exclusions list (public) — not yet pinned | Sourceable, uncited. |
| "Information suppressed deliberately" re coal industry (¶82; also ¶80) | **AUTHOR-CONFIRM** | no source | Strong causal/factual assertion, no source. Needs sourcing or softening (JSON gap #5). |

## B. Convergence-table cells (¶171–181) — PDF inline attributions captured

| Figure | Status | Source (+URL) | Note |
| --- | --- | --- | --- |
| Deepwater Horizon: BP response ~$14B + **NRDA $8.8B per 2016 Consent Decree**; CWA $5.5B + DOJ criminal $4.5B + class-action ~$10–15B (¶175) | **READY-TO-CITE** | **2016 BP Consent Decree** (NOAA Office of Response & Restoration + DOJ); DOI/DOJ Apr 4 2016 — https://www.doi.gov/pressreleases/us-and-five-gulf-states-reach-historic-settlement-bp-... ; NOAA PDARP/PEIS 2016 — https://www.gulfspillrestoration.noaa.gov (HIGH) | **PDF cell carries this attribution verbatim.** Full settlement: $20.8B (2016): $5.5B CWA + $8.8B NRDA + $4.9B states + $600M other (register §1D). NRDA assessed = $8.8B (NOT $150B). |
| Libby: ~$0.6B **EPA Superfund** cleanup; W.R. Grace $250M 2008 EPA + $18.5M 2023 NRDA + $5.1M 2008 DEQ; long-tail illness $4–7B (¶176) | **READY-TO-CITE** | **EPA Libby Asbestos Superfund Site record** — https://cumulis.epa.gov/supercpad/cursites/csitinfo.cfm?id=0801744 ; **Montana DOJ/DEQ**; **W.R. Grace** filings; DOJ Press #08-194 (Mar 11 2008, $250M) — https://www.justice.gov/archive/opa/pr/2008/March/08_enrd_194.html (HIGH for components) | **PDF cell carries this attribution verbatim.** ">$4B consolidated total" mixes site + company-wide bankruptcy trust — document components, don't aggregate (register §3). |
| Exxon Valdez: Exxon $2.2B + NRDA ~$100M per **1991 settlement**; 1991 civil $900M + private ~$507M + punitive $507M + criminal $25M (¶177) | **READY-TO-CITE** | **EVOSTC** — https://evostc.state.ak.us/oil-spill-facts/settlement/ ; **DOJ/EPA 1991** — $900M civil + $125M criminal ($25M fine + $100M restitution) — https://www.epa.gov/archive/epa/aboutepa/exxon-pay-record-one-billion-dollars... (HIGH) | **PDF cell carries this attribution verbatim.** "$5.5M product spilled" + "$7–10B all-in" are derived/aggregate, not single-source (register §3, UNVERIFIABLE). |
| ¶181 prose naming the three agency sets (NOAA/DOJ/Consent Decree; EPA/MT DOJ/Grace; EVOSTC/DOJ 1991) | **READY-TO-CITE** | as above | PDF + clean chapter ¶181 already name these; formalize into §23 bib. |
| ¶46 PROSE totals: Deepwater "$65–70B"; Libby "$5–8B"; Valdez "$7–10B" | **NEEDS-PIN / align-to-table** | BP cumulative charge ~$61.6B (2016) → ~$65B (2018) BP SEC 6-K/20-F (HIGH for $65B); Libby/Valdez aggregates derived (register §3) | **JSON gap #4 + ledger.** The ¶46 prose figures are unsourced while the table cells ARE sourced — **align ¶46 prose to the table sourcing.** Valdez "$5.5M product value" basis UNVERIFIABLE. |
| McDowell coal table cells: M1 $261–2,412; M2 $8–88; M3 $420–13,100 mid $2,500 (¶173) | **FRAMEWORK-OUTPUT (derivation-shown)** | TA §3.6 Block 4 worked-example calibration (internal, NOT a public cite) | Framework-computed; "derivation shown." Inputs (coal price, DAC, SCC) get sourced; outputs labeled ours. |
| Norway table cells: M1 $161–422/BOE; **M2 $48/BOE**; M3 $70–1,000 mid $280 (¶174) | **FRAMEWORK-OUTPUT / CORRECTION** | TA §3.6 Block 4 (internal) | Output, derivation-shown. **CORRECTION:** internal $48-vs-$50 inconsistency — ¶141 prose says "approximately fifty dollars," table ¶174 says "$48/BOE." Reconcile to one figure (register §6D-16; ledger). |

## C. Framework-output figures (derivation-shown, NOT external cites)

| Figure | Status | Source | Note |
| --- | --- | --- | --- |
| IPG 33–122× (McDowell, Ch2 framing, ¶187, ¶363) | **FRAMEWORK-OUTPUT** | framework-computed | Canonical public headline = **33–122×**. Derivation-shown label. |
| IPG ~50× triangulated central (¶185, ¶187) | **FRAMEWORK-OUTPUT** | framework-computed | Inflation-corrected central; sits inside 33–122×. |
| IPG 50–555× triangulated range (¶185, ¶187) | **FRAMEWORK-OUTPUT** | framework-computed | **TA-internal only; never quote 555× bare** (canonical J2; TA §11.6 disowns it as inflation artifact). |
| IPG 15–17× Deepwater; 55–82× Libby (¶46); 1,200–1,900× Valdez (¶46) | **FRAMEWORK-OUTPUT** | framework-computed | Derivation-shown. Note ¶46 input totals (the cost figures) are NEEDS-PIN (§B). |
| Method 1 range $310–1,800/ton-coal (¶139); $261–2,412 (table ¶173) | **FRAMEWORK-OUTPUT** | framework-computed from DAC bands × emission factor | Derivation-shown; DAC inputs are READY-TO-CITE (§A). |
| Method 2 range $8–88/ton (¶141, ¶173) | **FRAMEWORK-OUTPUT** | framework-computed from Norway revealed-preference | Derivation-shown; Norway BOE input has $48-vs-$50 correction (§B). |
| Method 3 range $420–13,100/ton, mid ~$2,500; **$13,100 ceiling**; α-dominance 0.9–1.0 (¶143, ¶173) | **FRAMEWORK-OUTPUT** | framework-computed (Dixit & Pindyck 1994 base + scarcity/irreversibility params; TA cross-case sensitivity) | **$13,100 ceiling has no public anchor** (JSON gap #7) — but it's a framework output, so it gets derivation-shown labeling, NOT an external cite. The *method base* (Dixit & Pindyck 1994) is a tradition-citation (§D). |
| RCV / CS / per-ton component allocations | **FRAMEWORK-OUTPUT** | framework-computed | Per register §4: all IPG multiples, RCV/CS/floor figures, per-ton component allocations are owned-outputs. |
| Libby 40:1 ratio (¶189); Deepwater 40% cost-recovery (¶191) | **FRAMEWORK-OUTPUT** | framework-computed | Derivation-shown. |

## D. Intellectual-tradition citations (theory anchors — name + work, not empirical sourcing)

| Anchor | Status | Source | Note |
| --- | --- | --- | --- |
| Dixit & Pindyck 1994 (real options → Method 3) ¶143 | **READY-TO-CITE** | Dixit & Pindyck, *Investment Under Uncertainty* (Princeton, 1994) | Tradition citation. |
| Weitzman (declining-rate discount ¶119; 2009 fat-tail ¶121) | **NEEDS-PIN** | Weitzman 2001 "Gamma Discounting" *AER* 91(1):260–271 AND/OR Weitzman 2009 fat-tail — **pin which paper per claim** | Ledger flags "pin specific paper." ¶119 = gamma-discounting (2001); ¶121 = fat-tail (2009). |
| Darity & Mullen 2020 (Method 2 backward / Restitution Bond) ¶145, ¶269 | **READY-TO-CITE** | Darity & Mullen, *From Here to Equality* (UNC Press, 2020) | |
| Savage 1951 (minimax-regret → Asymmetric Regret Rule) ¶359, ¶361 | **READY-TO-CITE** | Savage 1951 | Tradition citation. |
| Hartwick 1977 (Hartwick's Rule; "Residual") ¶219, ¶325 | **READY-TO-CITE** | Hartwick 1977, *AER* 67(5):972–974 | |
| Hotelling 1931 (Hotelling Identity) ¶331 | **READY-TO-CITE** | Hotelling 1931, *JPE* 39(2):137–175 | |
| Parfit (non-identity problem) ¶259–265 | **READY-TO-CITE** | Parfit, *Reasons and Persons* (1984) | |
| Mazzucato 2018 ("Value" in RCV) ¶325 | **READY-TO-CITE** | Mazzucato, *The Value of Everything* (2018) | |
| Ostrom (commons; coordination vs extraction) ¶277–325 | **READY-TO-CITE** | Ostrom, *Governing the Commons* (1990) | |
| Sen (capability/SWF) ¶273 | **READY-TO-CITE** | Sen — pin specific work | |
| Ramsey 1928; Stern Review 1.4%; Nordhaus ~4% (¶153) | **NEEDS-PIN** | Ramsey 1928 *EJ*; Stern Review 2006; Nordhaus DICE | Discount-rate-debate name-checks; pin if a reviewer demands. |
| Dwyer/Lewis counterfactual tradition (¶303 — CIT naming) | n/a | David Lewis counterfactual reasoning | Methodological lineage, not empirical. |

---

## Highest-priority corrections (submission-blocking / reputational)

1. **$4.50 → ~$4.71 coal price (¶38/¶80/table ¶173)** — EIA primary series; cascades into every IPG ratio. Canonical-ledger RATIFIED. PDF still carries $4.50.
2. **Pigouvian floor $518–532 → $504–518 (¶343)** — the live Ch6 carbon cascade ("$510→$496" family); recompute on McDowell 2.61/$496 basis.
3. **Norway $48-vs-$50 internal inconsistency (¶141 prose vs ¶174 table)** — pick one BOE figure.
4. **SCC $190 attribution: EPA-2023, not Rennert (¶62)** — Rennert's own central was ~$185.
5. **Norway fiscal-rule date (¶221)** — 4%-in-2001 → 3%-in-2017; ensure no since-inception-3% implication.
6. **¶46 prose totals unsourced** ($65–70B / $5–8B / $7–10B) while table cells ARE sourced — align prose to table.

## Counts

- **READY-TO-CITE:** 18 (incl. 3 convergence-table cells w/ verbatim PDF attributions, DAC ×4, life-expectancy, Bassett-Bell/Darity, GPFG, + 9 tradition anchors)
- **NEEDS-PIN:** 11 ($44B, env tier, community tier, contemporary coal price, solar LCOE, carbon-tax-1991, ethics-council, ¶46 prose totals, Weitzman paper-pin, Ramsey/Stern/Nordhaus, Sen)
- **AUTHOR-CONFIRM:** 3 ($4.50 price-fix ratify, fiscal-rule date, "information suppressed deliberately")
- **UNVERIFIABLE:** 2 (Valdez $5.5M product value; Valdez/Libby "$7–10B"/">$4B" aggregates)
- **FRAMEWORK-OUTPUT:** 13 (all IPG multiples, M1/M2/M3 ranges incl. $13,100 ceiling, RCV/CS, $441/$496/floor derivations, Libby 40:1 / Deepwater 40%)

**Highest-priority unsourced (NEEDS-PIN):** the **$44B Black Lung** figure (load-bearing health-tier input, date-discrepant + likely a stale 2009 figure presented as current; pin CRS R45261-or-equivalent or relabel "≈$44B through 2009") and the **bare ¶46 case-total bands** ($65–70B / $5–8B / $7–10B) that anchor the IPG multiples while their own table cells are already sourced.
