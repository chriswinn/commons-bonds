# Commons Bonds — Canonical Figure Ledger

**Status: RATIFIED 2026-06-04 (author). J1–J7 resolved below; J5 resolved to a framing pending a primary-source year-lock. This file is now the single source of truth for the book's shared figures.**
Once ratified, this file is the SINGLE SOURCE OF TRUTH for the book's shared figures. Every
chapter, the Technical Appendix, and every derivative essay/op-ed must match it. Built from the
cross-artifact number sweep (`publishing/essays/_pipeline/coal-figure-canonical-sweep_2026-06-04.md`)
and this session's McDowell reconciliation (book-amendment-candidate #5/#7).

**Provenance caveat:** the sweep ran (sandboxed) against the main repo working copy, which lagged
this session's pushed fixes, so its raw discrepancy table shows Ch8/Atlantic/op-ed in their
*pre-fix* state. The canonical set below is current; the "still needs editing" list is the live
cascade.

## Canonical set (McDowell coal / magnitude)

| Figure | Canonical value (pinned label) |
|---|---|
| Mine-mouth price, 1960 | **~$4.70–4.85/ton** — **AMENDED 2026-06-04** (was $4.50). EIA 1960 nominal mine-mouth ≈ $4.71 (bituminous) / $4.83 (all coal); phrase as "just under five dollars." The old $4.50 undershot the EIA primary series ~5–7%. Cite EIA. |
| CO₂ emission factor | **2.32 t/short ton** (framework / national-bituminous default) — **2.61** (McDowell-specific, Pocahontas seam). Ratified two-basis split; keep both with rationale. **AMENDED 2026-06-04:** 2.61 is NOT an anthracite assumption — it derives from EPA AP-42 §1.1 (93.28 kg CO₂/mmBtu) × Pocahontas-seam heat content (~28 mmBtu/short ton), per Ch8 §72. **Cite the heat-content source explicitly** (USGS/EIA Pocahontas data) so a reviewer cannot swap in 2.32 (which would drop the carbon term to ~$443). |
| Social cost of carbon | **$190/t = the EPA 2023 central estimate.** **AMENDED 2026-06-04:** cite **EPA 2023** as the source of $190 (EPA *drew on* Rennert et al. 2022 *Nature*, whose own central figure was ~$185 — do NOT attribute $190 to Rennert). Ch8 §74 already phrases this correctly; the TA must adopt the EPA-2023 attribution in the cascade. |
| **Carbon term — McDowell** ("foreclosure component") | **$496** ( = 2.61 × $190 ). **Pins "$496" = carbon term.** Corrects the old $510. |
| Carbon term — national basis | **$441** ( = 2.32 × $190 ) |
| 4-component Pigouvian floor | **~$504–518** ( $496 + ~$8–22 non-carbon heads ). Corrects $518–532. |
| **8-component honest TOTAL** | **$510/ton**. **Pins "$510" = the TOTAL, never the carbon term.** Corrects the old $524. |
| **RCV integral (the headline value)** | **$525–540/ton** — AMENDED 2026-11-11 (TA v2.0.1 §11.1; adopted calibration of 2026-06-10, now the headline). $526 (Stern) / $537 (4%) / $541 (Nordhaus). Carbon term ≈92% of the level; foreclosure ≈7%. **NOT a damage-function total; never conflate with $510.** ~~$580–620~~ RETIRED (unrecorded parameterization; gate `regressed-figure-580-620`). |
| **Multiples (consistent price basis only)** | **AMENDED 2026-11-11 (author decision 4).** Integral **about 4–13×** ($525–540 over the contemporary $40–140/ton, EIA); damage floor about 3.6–13×; Method 3 **8.5–26× (center ~15×)**, price-independent and ≥ 1 by construction (not evidence of direction). **"$4.71 then, $525 now" = two prices in two eras; NO ratio.** RETIRED: ~~107–110×~~, ~~61–115×~~, ~~67–134×~~, ~~33–122×~~, and the unsourced ~~$8.66~~ "contemporary price". |
| ~~IPG triangulated central ~50×~~ | **SUPERSEDED 2026-06-09** — no single triangulated central (the lenses measure different quantities; see amendment). |
| IPG 555× | TA-internal full-triangulation ceiling only; **never quote bare** (TA §11.6 disowns it as an inflation artifact) |
| McDowell 2020 population | **~19,000 / "under 20,000"** (retire "18,000") |

### Label-pinning (the load-bearing discipline)
- **$496** = carbon term / foreclosure component (McDowell basis).
- **$510** = the 8-component honest TOTAL. The old error labeled $510 as the *carbon term*; corrected, $510 is the *total*. These are opposite meanings — always state which.
- **$504–518** = 4-component Pigouvian floor.
- **$525–540** = RCV integral, the TA's headline value (method-distinct; keep out of the "total" slot). ($580–620 retired.)

## Judgment calls — RATIFIED 2026-06-04 (author)

- **J1. RATIFIED.** Carbon = **$496**, total = **$510**, book-wide (arithmetic-driven; more conservative). Already applied to Ch8 + Atlantic + the op-ed draft; cascade the rest (Technical Appendix, Ch6, Ch2, canonical `op-ed.md`, the 2026-05-11 inventory, the Ch8 pre-pub queue) — this is the execution of book-amendment-candidate #7.
- **J2. RATIFIED 2026-06-04 → SUPERSEDED 2026-06-09.** ~~Public IPG = 33–122×; ~50× = triangulated central~~ — both **retired** (see amendment below): the bare 33–122× reproduces from no consistent input ("33" = the §3.2 definitional 1/0.03; "122" = one carbon-inclusive-RCV ÷ 1960-price point) and was internal-case-file-sourced (Class-4). Use the **lens-explicit IPG**. **50–555× DISOWNED; never quote.**
- **J3. AMENDED 2026-06-04 (author).** ~~Harmonize → $4.50~~ → harmonize the 1960 mine-mouth price to **~$4.70–4.85 (EIA)** / "just under five dollars"; the earlier $4.50 undershot the EIA primary series. Cascade to Ch8/Ch6 in the redrafts. *(Three canonical-figure amendments ratified 2026-06-04: this J3 price fix; the SCC $190 = EPA-2023-not-Rennert attribution; the 2.61 = AP-42 × Pocahontas-heat-content basis with explicit heat-content sourcing. All three flow into the coal cascade / redrafts.)*
- **J4. RESOLVED.** Keep the dated **"$4.5B (2021)"** as a defensible vintage anchor (low-stakes); if a single current figure is later preferred, use the most recent DOL Black Lung Disability Trust Fund debt *with its year*.
- **J5. RESOLVED to a framing (hard-year still needs a primary source).** The U.S. Steel McDowell/Gary shutdown was a **phased wind-down across the 1980s into the early 1990s** (Gary closure often cited ~1986; broader U.S. Steel McDowell exit toward ~1992, ~1,200 jobs), not a single year — which is exactly why the artifacts disagree. **Canonical framing: harmonize every artifact to "across the 1980s" / "by the late 1980s,"** NOT a contested point-year. A specific hard year (1986 vs 1990) must not be stated as fact until locked against a primary source (a Gary/McDowell history, U.S. Steel records, or a contemporaneous news archive) — flagged for the gather/drafting stage.
- **J6. RATIFIED.** Ch6 national-basis carbon = **$441** (= 2.32 × $190); relabel the "$449–464" band accordingly (carbon $441 + non-carbon heads).
- **J7. RESOLVED; figure AMENDED 2026-11-11 → $525–540.** The RCV-model band (formerly $580–620) lives in the **Technical Appendix** (method-distinct, Weitzman declining-rate); chapters/essays use the **$510 total** and may point to the appendix for the higher model estimate. Never conflate the integral ($525–540) with the $510 total.

## Cascade targets (expands book-amendment-candidate #7)

- ✅ **Already fixed this session** (worktree + origin/main): **Ch8** ($496/$510/$504–518/IPG 120→ confirm), **Atlantic Ideas** ("more than $500"), **McDowell op-ed** fresh draft.
- ✅ **Technical Appendix DONE (closeout 2026-06-09, branch `claude/ta-closeout-260607-92165f`):** §11.1/§11.6/§9.5/§11.11 — 33–122× retired → lens-explicit, coal $4.71, M3 Path-A, carbon/total reconciled, Deepwater §11.2, Norway $48. ⛔ **Still need editing:** **Ch6** (national-basis labels + $518–532); **Ch2** (IPG framing); the **canonical `op-ed.md`** (sweep found 2.86 factor / $544 carbon / $558 total — **highest exposure**, NYT/WaPo/PS target — verify and fix); **cross-chapter-consistency-inventory_2026-05-11**; **Ch8 pre-pub queue** (retract its "arithmetic verified" note).
- **Aeon candidate:** no edits ("more than $500" + the shown $496 are already correct).

## AMENDED 2026-06-09 — TA → redraft reconciliation (supersedes the entries noted)

Provenance source of truth: `tools/audits/corpus-primary-source-register_2026-06-08.md` (§1 sourced / §2 the 14 corrections / §3 unverifiable) + `tools/audits/chapter-citation-specs/`. Full per-target application map: `tools/audits/_TA-redraft-reconciliation_2026-06-09.md`. Discipline: cite the EXTERNAL primary source, never our own ledger; framework outputs (IPG/RCV/CS/M3) are "framework-computed, derivation shown."

**Coal price — SHARPENED.** Supersedes line 18 / J3 "~$4.70–4.85": canonical 1960 mine-mouth = **$4.71/ton** (EIA Total Energy Table 7.9, bituminous; all-coal $4.83). Register §2.9. Prose may still say "just under five dollars"; use $4.71 where a point value is shown. Cascades into M1/IPG inputs. [Ch2, Ch6, Ch8, Ch9, TA]

**M3 (Method-3) Path-A rework — chapter M3 figures SUPERSEDED.** Replaces all prior chapter M3 ranges/centers/ceiling AND the 50–555× triangulated IPG (supersedes lines 27–28 + J2's "50–555×"):
- McDowell coal M3 = **~$340–3,670/ton, geometric center ~$1,115/ton** (V_option $40–140 × scarcity 1.27–1.31 × irreversibility 6.67–20). The old "$13,100 ceiling" / "$420–13,100 / mid ~$2,500" is GONE; new top ~$3,670.
- M3-IPG (market-anchored; V_market = market price) = scarcity × irreversibility = **8.5–26× (center ~15×)**, price-independent. The old **50–555× is DISOWNED** as an inconsistent-basis artifact; on a consistent basis the lenses converge to 8.5–26×. Never quote 50–555× as a triangulated IPG.

**"33–122×" public-headline IPG — RETIRED (supersedes line 26 + J2's "Public IPG = 33–122×").** Author-ratified 2026-06-09 (TA retirement decision-record `tools/audits/ta-mcdowell-33-122x-IPG-retire_decision-record_2026-06-09.md`); applied in the TA by the closeout consolidation (§9.5/§11.1/§11.6/§11.11; zero bare "33–122×" remain). The bare range reproduced from no consistent input ("33" = §3.2 definitional 1/0.03; "122" = one carbon-inclusive-RCV ÷ 1960-nominal-price point) and was sourced only to an internal case-file audit (Class-4). **Canonical IPG is now lens-explicit (TA §9.5/§11.11):** carbon-externality/Damage-Function **~107–110×** (÷ $4.71 1960 price); RCV-integral **67–134×** (Weitzman); Method-3 foreclosure-premium **8.5–26× (center ~15×)**, price-independent (the most conservative lens). Cite the lens + price basis, never a bare single range. **Cascade still open:** `publishing/book-proposal/05_chapter-summaries.md` + any chapter prose (Ch6/Ch8 verified clean of "33–122×" in this closeout; route any reintroduced instance through the redraft campaign).
- Norway M3 = **~$96–610/BOE, central ~$281/BOE**; M3-IPG **~2.4–5.1×**. Norway's CS-reduction is **irreversibility-reduction** (GPFG restoration optionality moves α from ~1 toward ~0.50–0.75), **NOT rent-capture** — drop the old "16% / $48/BOE rent captured / $300" framing (Ch6 backtest row).
- **Ch6 ↔ TA Method-1 discrepancy FLAG (route to correctness/IPG owner, do NOT fix blind):** Ch6 triangulation-table M1 column "$261–$2,412/ton" vs TA §11.6 M1 "$290–$2,702"; the pending §11.9 DAC refresh will move the M1 conservative cap ~20%. Reconcile M1 separately from the M3 propagation.
- Notation: scarcity = **ς**; irreversibility = **1/(1−α)** (no β exponent); V_option = the resource's own market/intrinsic value (premium emerges from scarcity × irreversibility). M3 = the **quasi-option value of preservation (Arrow–Fisher/Henry)**, NOT Dixit–Pindyck investment-timing. Irreversibility weighted by the empirical record + ARR (IPCC AR6 SPM B.5; Bernhardt & Palmer 2011; Thm 10.4/10.5), NOT a "discovered α-dominance." [Ch6, Ch8 + TA §3.5/§11.6/§11.8/§11.11]
- **CORRECTED 2026-06-09 (closeout):** the bare public headline IPG **33–122× is RETIRED** (see the retirement bullet above) — *not* unchanged. §9.5 cross-MODEL RCV-integral **67–134×** is unchanged.

**$108T Social Security — DONE (Ch5 landed).** $108T disavowed as the dishonest version; honest version = investable base ~$2.7T surplus peak, compounded net of payouts → "a few trillion, not a hundred"; ~$22.6T 75-yr shortfall kept distinct. Any OTHER chapter (Ch8/Ch9) still citing $108T or its 3×-debt / 4×-GDP / $300k-per-person scalings → delete/align.

**$44B black lung — RELABEL.** "≈$44 billion through 2009 (GAO/CRS)" — a conservative, honestly-dated floor for 1969–present (no authoritative post-2009 cumulative total exists; modern GAO/CRS/DOL report only ~$150–184M/yr + Trust-Fund debt). Keep the Trust-Fund-DEBT clause ($5.1B as of Sept 2024, DOL/GAO) DISTINCT from cumulative-paid. [Ch2, Ch5 §194, Ch6, Ch8]

**$11T household net worth — RE-ATTRIBUTE.** The ~$11T total-household-net-worth peak→trough is the **Federal Reserve Z.1** figure, NOT Mian & Sufi (whose own central magnitude is ~$5.5T HOUSING wealth). Attribute $11T to the Fed; keep Mian & Sufi for the leverage / distribution / MPC analysis. [Ch5 §76, Ch8, Ch9]

**Carbon cascade — canonical UNCHANGED, re-cascade still live.** carbon $496 / total $510 / floor $504–518 (J1/J6). Mechanical re-cascade still owed in the TA + Ch6 + Ch9 (README §B).

*(The per-chapter citation corrections — Norway fiscal rule 2001@4%→2017@3%; Fed $16T = "cumulative"; Hendryx OR 2.03; menhaden cap 2017/2018 not 2006; Baotou $5–15B; Deepwater ">$150B" not NOAA; GoFundMe AJPH-2022/437,596; Tangier ~1.7 ft/yr paper-avg, APPLIED to Ch 3 as Option A plain paper-figure, RATIFIED 2026-06-11 (15 ft/yr press/exposed-shore figure dropped entirely per author register call); Libby >70%-of-US; Norway per-capita ~$390k; foreclosures ~4.1M completed; reclamation-gap single figure; US-Steel "across the 1980s" — are chapter-level, not cross-chapter shared figures; they live in the reconciliation artifact + the per-chapter briefs.)*

## AMENDED 2026-11-11 — TA v2.0.1 (independent review Phase 2; decisions log 2026-11-10/11)

Source of record: `manuscript/technical-appendix/TechnicalAppendix_v2.0.1.html`; derivations in
`manuscript/technical-appendix/calculations/` (run-outputs 2026-11-11: 67/67 and 28/28, 0 mismatches). Every
retired figure below has a gate pattern in `tools/quality-gates/regressed-patterns.yaml` (same commit).
**Status: applied in the TA on the session branch; merge to main waits on the author's OK.**

| Figure | Canonical value (pinned label) |
|---|---|
| **McDowell headline RCV** | **$525–540/ton = the integral** (definition; conservative; survives rejection of Method 3). Methods 1 and 3 are **cross-checks**, never the headline, never "convergence". |
| **McDowell realized bond (derived)** | **$88–100/ton from all payers** ($53–60B ÷ 600M tons) — an **upper bound** (national numerators over McDowell-area tons). **$8–13/ton extractor-paid.** Forward instrument only (reclamation bonds): $5–8/ton. RETIRED: ~~$50–88~~ (the $50 had no derivation), ~~$8–15~~. |
| **McDowell cost severance** | **At least about $425–450/ton** (integral − all-payer bond). About $512–532 against extractor-paid. ⚠ The review packet said "about $440–490"; that used the underived $50. Corrected by arithmetic; **author to confirm.** RETIRED: ~~$1,025–1,065~~ (Method-3 centre as headline). |
| McDowell sensitivity | S_max = 0 → about $573. SCC $51 → about $165–180 (1.2–4.5× price). No carbon term → about $30–45, below the all-payer bond. The sign rests on a carbon cost of at least roughly $20–25/t CO₂. |
| **"Method 1"** | = replacement cost (DAC) **only**. The bottom-up audit priced at the SCC is the **damage-function floor** ($504–518), a separate lens. |
| **Method 3 α** | **Physical irreversibility only** (0.85–0.95 for fossil carbon). A fund does not lower α. |
| **Norway bond (B₂)** | **About $36/BOE** = fund (NOK 21,268bn ≈ $2.0T, end-2025) ÷ ~55bn BOE. Label **B₂** everywhere. RETIRED: ~~$48/BOE~~ (fund ÷ capture rate). |
| Norway rent (Hotelling split, TA §4) | State net cash flow 1971–2025 = **NOK ≈14,860bn (constant 2027 kr; Ministry of Finance / Statistics Norway via norskpetroleum.no)** ≈ NOK 270 ≈ **$25/BOE**; total rent ≈ **$32–36/BOE** at a 70–80% state share (proxy). |
| **Norway RCV / CS** | Value used = **carbon floor ≈ $70/BOE** (0.37 t CO₂ × $190). **CS ≥ about $34/BOE ≈ $1.9T cumulative** (a floor). Cross-checks: M1 $161–422; M3 **$320–3,040** (center ≈ $985; multiple 8–25). RETIRED: ~~M3 $96–610 / $281~~, ~~2.4–5.1×~~, ~~CS $233–250/BOE~~, ~~$12.8T / $13–15T~~, and the "irreversibility-reduction" account of Norway (ledger 2026-06-09 bullet above is SUPERSEDED: Norway bonded its rent; it did not lower α). ⚠ **Number change for author confirmation** (review item N4/C2). |
| **Hotelling Identity** | **RCV − B₂ = (RCV − H) + (H − B₂).** Worked for Norway only: (RCV − H) ≥ $34–39; (H − B₂) ≈ −$5 to $0. McDowell: bound only (H ≤ P → RCV − H ≥ $385). RETIRED form: ~~RCV − Hotelling rent = CS~~. |
| **Libby** | Federal cleanup **>$600M** (EPA). **$250M = W.R. Grace's 2008 reimbursement of federal cleanup costs (DOJ/EPA, Mar 11 2008)** — NOT wrongful-death settlements, NOT additive. Cleanup ≈ **6×** the ~$100M revenue (unconfirmed industry estimate). Mortality head $5.1–7.6B (694 deaths × EPA VSL; labeled). ⛔ $50M/yr monitoring and $500M property: **no source; Open.** RETIRED: ~~$2.6B documented-cash floor~~, ~~26:1~~, ~~65–102×~~, ~~70/30 split~~. The Ch 5 rings redraft already says "about six times" (cleanup only): consistent. |
| Deepwater | The **realized industry-paid bond** case: $61.6B paid of ~$70–74B documented + estimated. The ~15× cost/revenue ratio is **conditional on the blowout**; not an IPG. $8–12B continuing damage = estimate with **no primary source cited** (open). |
| Crowdfunding | **Kenworthy & Igra 2022 (AJPH):** about 12% met goal; about 16% received nothing. ⛔ "Ly & Soman 2020", "25× growth", "88% failure": untraceable; removed from the TA (still in Ch 9 L202 → fix at rebuild). |
| Community-transition cost | $5–15/ton **in total** (framework estimate); PV at 1960 ≈ $1–2/ton (baseline). Already inside the §11.1 non-carbon heads — **not additive** to $525–540. RETIRED: "adds ~$5–10/ton", "$454–474". |
| Long-run discount rate | **2%** (50-yr half-life) is the one long-run rate used in computations. |

**Terms.** "Three Ways of Counting" KEPT, with the gloss: two ways estimate what is owed, one reads what was
paid. All triangulation / convergence language removed from the TA. Bond definition (REVISED by the author 2026-11-11, replacing "priced with the cost in view"): B = what was set
against the cost by **(a) an instrument** (counts even if the cost was unknown or uncertain when posted) or
**(b) the bearer's informed consent** (counts only as far as the bearer could see the cost). Cost severance =
borne and neither bonded nor knowingly accepted (TA Definition 1.7); CSD and B₁ defined (Defs 1.11, 1.12) with the payer split; no fifth gate.

**Cascade still owed (not this session's files):** Ch 6 (rebuild: $48/BOE row L174; triangulation L137–187;
Ostrom L285); Ch 9 L202 (Ly & Soman); NYRB essay ¶35 (Ostrom claim; author decision before submit); proposal
§05 chapter summaries if they carry any retired multiple.

## Canonical set (Chesapeake reef / Restitution Bond) — ADDED 2026-06-10 (TA §11.12; status: GATE 2 OPEN — Ch 3 carries the priced claim as of 2026-06-11, origin/main 0d2ddef; MERGE-HOLD now only on three author-ratification calls)

Source of record: TA §11.12 (migrated onto the current repo layout 2026-06-11 on branch `claude/ta-reef-migration-260611-639919`; **GATE 2 satisfied** — Ch 3 promoted 2026-06-11 on origin/main `0d2ddef` carries the priced Restitution-Bond reef claim, so the TA-never-leads-the-book rule is met; the package retains **MERGE-HOLD pending author ratification of three flagged §11.12 calls**). Derivations reproduced in `manuscript/technical-appendix/calculations/csd_rcv_calculations.py` Part 4 (run-output 2026-06-10, all checks PASS). Every figure external-sourced (Schulte 2017; NOAA per-tributary table Dec 31 2024; Great Wicomico Tributary Plan §5; MD DNR/Gov. Moore Aug 26 2025 — bib §25).

| Figure | Canonical value (pinned label) |
|---|---|
| Foreclosed reef extent | **~2,738 acres** (James River high-quality oyster-rock, 7,047→4,309 ac, −38.9%, 1910→1981; Schulte 2017 citing Moore 1910 / Haven et al. 1981). **AREA basis only** — never build the dollar figure from shell volume; the Darling shell-mountain stays narrative, never a number. |
| Restoration unit-costs | **~$7,300/ac** (Great Wicomico realized = $907,000÷124 ac) / **~$13,500/ac** (forward-engineering, construction-only, natural recruitment — GW Plan §5) / **~$77,000/ac** (bay-wide completed-program avg, construction + seeding) |
| **Restitution Bond floor** | **$20M realized / $37M headline** ( = 2,738 × $7,300 / × $13,500). **Pins "$37M" = the headline floor** ("a conservative floor of roughly $20–37 million"). |
| **CSD central (robust)** | **~$211M** ( = 2,738 × $77,000; precisely $210,826,000). Cherry-pick-proof center, NOT the floor. |
| CSD ceiling | **Open by design** — Method-3 foregone-fishery option value admitted, named, deliberately not entered (strategic decline, "bond only the unassailable floor"; never show-then-flinch). NO foregone-fishery dollar figure anywhere in the corpus. |
| **Realized B₁ (public restitution already posted)** | **>$92M Maryland** (MD DNR/Gov. Moore, 5 sanctuaries ~1,300 ac) / **~$115M bay-wide itemized PRIMARY** (NOAA: MD $93.52M + VA $21.77M); **~$108M program-level = rounding corroborator only** (MEDIUM confidence). Unit-cost corroboration: $108M÷1,900 ac ≈ **$57K/ac** (inside the M1 band). |
| Industry contribution to B₁ | **$0** (all funders public: NOAA, USACE, MD DNR, VMRC). **The finding is MIS-ASSIGNMENT, not magnitude** — vs the floor, B₁ already exceeds it; vs the ~$211M central, ~$96M unrestituted. |
| Measure hygiene | −38.9% = **areal** extent (the floor's basis). ~99% structure loss (Woods 2005: ~30 ac of >2,471 ac vertical relief) and ~99.7% abundance loss (Wilberg 2011, upper-Bay MD) are DIFFERENT measures — **never multiply a 99% figure by a per-acre cost.** |
| Geography discipline | James River = the stated lower-Bay **proxy**; NO Hampton-Bar-specific acreage exists (Paxton 1858 is qualitative); NO NSA Hampton Roads dollar figure (qualitative only). |

**Cascade:** Ch 3 restitution section now carries the chapter-side priced Restitution-Bond claim (promoted 2026-06-11, origin/main `0d2ddef`) — **GATE 2 SATISFIED**; the remaining MERGE-HOLD is author ratification of the three flagged §11.12 calls (Wilberg 2011 + Woods 2005 bib additions beyond the enumerated four; §10.2 seven-cases census wording; Emp. Obs. 10.1b worked-instance note). Any reef-touching essay/op-ed inherits these pinned labels. TA §11.12 + §3.6 reef row + §10.2 census + §5.5/§1.7/§1.10/Emp. Obs. 10.1b/§17.5/§11.7 reconciliations all ride this MERGE-HOLD branch.

## Ch 5 case figures (Butler; BP–Mexico) — ADDED 2026-11-10 (author: "add the ledger entries where needed")

Sources of record: Butler, *NYT Magazine*, June 20, 2010 (verified page by page in
`research/citations/butler-2010-nyt_verification-and-quotes_2026-11-10.md`); BP–Mexico from BuzzFeed News
(N. Janowitz, 2018), Vice, and *El País* (V. Calderón, Apr 30, 2015, via BHRC). Journalistic sources for
Mexico: attribute, don't overstate.

| Figure | Canonical value (pinned label) |
|---|---|
| Medicare, internist | **$54** = the **standard office-visit rate** for what would have been a long meeting (never held); **$0** for the phone calls. NOT "a fee for a conversation about whether it was wise." |
| Medicare, surgeon | **$461** (implanting surgeon) |
| Hospital fee | **about $12,000** flat; **an estimated $7,500** of it to the device maker (St. Jude). ⛔ NOT "nearly half"; ⛔ NOT "~$6,000". |
| Caregiver | mother **77**, on duty **more than 80 hours a week**, in **2002** (before the Jan 2003 implant). Don't present 77 as an age reached after the implant. |
| Device | heart kept beating **nearly five years** (autumn 2007); battery expected to last **five more**; a meeting could have noted it would last **ten years** |
| Malpractice / liability motive | ⛔ **Not in Butler.** Keep out unless separately sourced and attributed. |
| Physician net income (ADDED 2026-11-12, author-confirmed) | Primary-care physicians **net about $173,000 a year**; noninvasive cardiologists **net about $419,000**. **Net, not gross.** Attribute to Butler (2010), p. 5 of the author's printout. Source text as relayed by the Ch 5 session, which read the full article; not yet in the Butler verification file — add there at the next Ch 5 pass. |
| Medical-sector lobbying (ADDED 2026-11-12) | **$545 million in 2009** — doctors, hospitals, drug companies, device makers and other medical professionals. Attribute to the **Center for Responsive Politics, as cited by Butler (2010)**; the year is 2009 ("last year" in a 2010 article). |
| Butler quotations in Ch 5 (ADDED 2026-11-12) | Five quotations, 47 words, all kept by the author. The chapter quotes "nobody makes money when medical interventions are declined" (p. 4), and names and paraphrases Dr. Ted Epperly, board chairman of the American Academy of Family Physicians (p. 5). |
| BP–Mexico settlement | **$25.5 million**, agreed **Feb 15, 2018** (BuzzFeed). "About $25 million" stays acceptable as a rounding. Split: **$15.3M** reimbursement of Mexico's monitoring and other costs; **$10.2M** to INECC for Gulf protection/restoration programs. BP opened at **$20M**; Mexico countered **$50M** (Oct 2017). The deal **released BP from responsibility for damage in Mexican waters**; Vice: no payment earmarked for affected communities. |
| Mexico's studies | Government funded **22** studies, kept them out of its lawsuit and withheld them; **20** published July 2018 after FOI requests (after the settlement), none claiming BP's fingerprint; **2** (IMP) remained classified as of the 2018 report. |
| Mexican fishermen's suit | **About 25,000** fishermen; US class action for compensatory and punitive damages; reported **April 2015** (*El País*); first class action by non-US citizens against BP over the spill. |
| ⛔ Coastline normalization | "Measured against comparable lengths of damaged coastline" has **no source** (no per-mile comparison exists in the record). Don't use. The raw totals ($61.6B+ US vs $25.5M Mexico) can be stated side by side only if the prose does not imply equal damage. |
