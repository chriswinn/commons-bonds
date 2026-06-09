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
| RCV-model estimate (method-distinct) | **$580–620/ton** — Weitzman declining-rate model estimate; **NOT a damage-function total; never conflate with $510.** |
| **IPG (lens-explicit)** | **"33–122×" RETIRED 2026-06-09** (author-ratified; see amendment below). Now lens-explicit: carbon-externality/Damage-Function **~107–110×** (÷ $4.71 1960 price); RCV-integral **67–134×**; Method-3 foreclosure-premium **8.5–26× (center ~15×)**, price-independent. Report the lens + price basis, not a bare range. |
| ~~IPG triangulated central ~50×~~ | **SUPERSEDED 2026-06-09** — no single triangulated central (the lenses measure different quantities; see amendment). |
| IPG 555× | TA-internal full-triangulation ceiling only; **never quote bare** (TA §11.6 disowns it as an inflation artifact) |
| McDowell 2020 population | **~19,000 / "under 20,000"** (retire "18,000") |

### Label-pinning (the load-bearing discipline)
- **$496** = carbon term / foreclosure component (McDowell basis).
- **$510** = the 8-component honest TOTAL. The old error labeled $510 as the *carbon term*; corrected, $510 is the *total*. These are opposite meanings — always state which.
- **$504–518** = 4-component Pigouvian floor.
- **$580–620** = RCV-model estimate (method-distinct; keep out of the "total" slot).

## Judgment calls — RATIFIED 2026-06-04 (author)

- **J1. RATIFIED.** Carbon = **$496**, total = **$510**, book-wide (arithmetic-driven; more conservative). Already applied to Ch8 + Atlantic + the op-ed draft; cascade the rest (Technical Appendix, Ch6, Ch2, canonical `op-ed.md`, the 2026-05-11 inventory, the Ch8 pre-pub queue) — this is the execution of book-amendment-candidate #7.
- **J2. RATIFIED 2026-06-04 → SUPERSEDED 2026-06-09.** ~~Public IPG = 33–122×; ~50× = triangulated central~~ — both **retired** (see amendment below): the bare 33–122× reproduces from no consistent input ("33" = the §3.2 definitional 1/0.03; "122" = one carbon-inclusive-RCV ÷ 1960-price point) and was internal-case-file-sourced (Class-4). Use the **lens-explicit IPG**. **50–555× DISOWNED; never quote.**
- **J3. AMENDED 2026-06-04 (author).** ~~Harmonize → $4.50~~ → harmonize the 1960 mine-mouth price to **~$4.70–4.85 (EIA)** / "just under five dollars"; the earlier $4.50 undershot the EIA primary series. Cascade to Ch8/Ch6 in the redrafts. *(Three canonical-figure amendments ratified 2026-06-04: this J3 price fix; the SCC $190 = EPA-2023-not-Rennert attribution; the 2.61 = AP-42 × Pocahontas-heat-content basis with explicit heat-content sourcing. All three flow into the coal cascade / redrafts.)*
- **J4. RESOLVED.** Keep the dated **"$4.5B (2021)"** as a defensible vintage anchor (low-stakes); if a single current figure is later preferred, use the most recent DOL Black Lung Disability Trust Fund debt *with its year*.
- **J5. RESOLVED to a framing (hard-year still needs a primary source).** The U.S. Steel McDowell/Gary shutdown was a **phased wind-down across the 1980s into the early 1990s** (Gary closure often cited ~1986; broader U.S. Steel McDowell exit toward ~1992, ~1,200 jobs), not a single year — which is exactly why the artifacts disagree. **Canonical framing: harmonize every artifact to "across the 1980s" / "by the late 1980s,"** NOT a contested point-year. A specific hard year (1986 vs 1990) must not be stated as fact until locked against a primary source (a Gary/McDowell history, U.S. Steel records, or a contemporaneous news archive) — flagged for the gather/drafting stage.
- **J6. RATIFIED.** Ch6 national-basis carbon = **$441** (= 2.32 × $190); relabel the "$449–464" band accordingly (carbon $441 + non-carbon heads).
- **J7. RESOLVED.** The RCV-model **$580–620** band lives in the **Technical Appendix** (method-distinct, Weitzman declining-rate); chapters/essays use the **$510 total** and may point to the appendix for the higher model estimate. Never conflate $580–620 with the $510 total.

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
- **UNCHANGED:** public headline IPG **33–122×** (line 26); §9.5 cross-MODEL **67–134×**.

**$108T Social Security — DONE (Ch5 landed).** $108T disavowed as the dishonest version; honest version = investable base ~$2.7T surplus peak, compounded net of payouts → "a few trillion, not a hundred"; ~$22.6T 75-yr shortfall kept distinct. Any OTHER chapter (Ch8/Ch9) still citing $108T or its 3×-debt / 4×-GDP / $300k-per-person scalings → delete/align.

**$44B black lung — RELABEL.** "≈$44 billion through 2009 (GAO/CRS)" — a conservative, honestly-dated floor for 1969–present (no authoritative post-2009 cumulative total exists; modern GAO/CRS/DOL report only ~$150–184M/yr + Trust-Fund debt). Keep the Trust-Fund-DEBT clause ($5.1B as of Sept 2024, DOL/GAO) DISTINCT from cumulative-paid. [Ch2, Ch5 §194, Ch6, Ch8]

**$11T household net worth — RE-ATTRIBUTE.** The ~$11T total-household-net-worth peak→trough is the **Federal Reserve Z.1** figure, NOT Mian & Sufi (whose own central magnitude is ~$5.5T HOUSING wealth). Attribute $11T to the Fed; keep Mian & Sufi for the leverage / distribution / MPC analysis. [Ch5 §76, Ch8, Ch9]

**Carbon cascade — canonical UNCHANGED, re-cascade still live.** carbon $496 / total $510 / floor $504–518 (J1/J6). Mechanical re-cascade still owed in the TA + Ch6 + Ch9 (README §B).

*(The per-chapter citation corrections — Norway fiscal rule 2001@4%→2017@3%; Fed $16T = "cumulative"; Hendryx OR 2.03; menhaden cap 2017/2018 not 2006; Baotou $5–15B; Deepwater ">$150B" not NOAA; GoFundMe AJPH-2022/437,596; Tangier ~1.7 ft/yr exposed-max; Libby >70%-of-US; Norway per-capita ~$390k; foreclosures ~4.1M completed; reclamation-gap single figure; US-Steel "across the 1980s" — are chapter-level, not cross-chapter shared figures; they live in the reconciliation artifact + the per-chapter briefs.)*
