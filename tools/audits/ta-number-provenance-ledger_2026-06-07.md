# TA Number-Provenance Ledger

**Created:** 2026-06-07 (Foundation session; work executed 2026-06-07 → 2026-06-08)
**Branch:** `claude/ta-provenance-260607-ad2dfc` (off the HELD `claude/ta-rigor-audit-260606-f537b4`; **not merged to main** — author reviews).
**Target file:** `core/technical-appendix/TechnicalAppendix_v2.0.0.html`
**Companion:** `tools/audits/ta-number-provenance-DECISION-MEMO_2026-06-07.md` (the author-judgment items NOT applied this session).

## Disciplines (carried from the resume doc + ratified this session)

Every worked number is classified into exactly one **defensibility class**:

1. **SOURCED** — traceable to a named **external** authority (institution / paper / dataset).
2. **DERIVED** — computed from cited inputs, with the arithmetic shown and reproducing.
3. **LABELED ASSUMPTION** — explicitly flagged in-text as assumption / estimate / posited / illustrative (ideally with sensitivity).
4. **UNSUPPORTED** — a bare number with no external source, no shown derivation, no assumption-label. **This is the defect to kill.**

**Hard rule:** a number is **not** "sourced" because the TA's own table / ledger / "canonical" / "terms_index" status asserts it. Cite the **external** authority, never our own apparatus. TA-internal-only backing = class 4 (or class 2 if it genuinely derives from cited external inputs). No invented factual claims — every source recorded here is real, with a URL where applicable.

## How this ledger was built

Six exhaustive read-only enumeration passes (one per section cluster) over the full ~8,000-line TA, cross-checked against the pre-existing `empirical_sourcing_pass_2026-04-25.md`, `method3_sensitivity_analysis_2026-04-25.md`, `ta-method1-input-provenance_2026-06-06.md`, and `ta-11.10-space-economics-sourcing_2026-06-07.md`. Every numeric value-dependent fix was **independently re-verified against a primary external source before application** (per author direction 2026-06-07, after the prior session was found to be context-saturated). The committed prior-session edits were also re-verified (results below).

---

## Summary

| Class | Meaning | Approx. count (distinct) | Status |
|---|---|---|---|
| 1 SOURCED | external authority cited | ~45 | Solid; several need a formal §18/§23 bib entry (see Part 4). |
| 2 DERIVED | arithmetic shown, reproduces | ~70 | Mostly reproduce; **a subset inherits class-4 inputs** (see Part 3C). |
| 3 LABELED ASSUMPTION | posited/illustrative | ~35 | Mostly the M3 σ/α/V_option/β parameters + regime-map cells + illustrative walkthroughs. |
| **4 UNSUPPORTED** | **the defects** | **~50–60 distinct** | **Registered in Part 3. Most are NOT fixed this session — they require author judgment (decision memo).** |

**Headline finding:** the class-4 problem is **substantially larger than the resume-doc scope.** The handoff named §11.10, §11.6-M2, §11.5-M1, Norway-vintage, Eco/Cohesion. Enumeration shows class-4 figures pervade **every empirical case** (§11.1–11.4, §11.7, §6.7, §7) and **the entire IPG / three-model-convergence apparatus** (§9.5's 12 cells; the 33–122× / 50–555× "canonical" ranges; the per-case multiples). The space-economics cluster (§11.10) is the cleanest to fix because its corrections are externally verifiable; the convergence apparatus is the hardest because its numbers are framework *outputs*, not external facts.

---

## Part 1 — APPLIED THIS SESSION (verified-safe only)

All independently verified against primary sources before applying. Numbers unchanged except where an external source proved the prior value wrong.

### §11.10 space-economics cluster (HTML)
| Fix | Old → New | Verification |
|---|---|---|
| Keck asteroid mass + $/kg | "7-**ton** asteroid … ~$370,000/kg" → "~500-ton (~7 m diameter) … ~$5,200/kg ($2.6B ÷ ~500,000 kg)" | KISS 2012 *Asteroid Retrieval Feasibility Study*: "7 m diameter, ~500,000 kg," $2.6B. The "7" is the **diameter in meters**; the $370k/kg reproduced only from the wrong 7-ton mass. [Centauri Dreams](https://www.centauri-dreams.org/2012/05/02/bringing-an-asteroid-to-lunar-orbit/), [Space.com](https://www.space.com/15405-asteroid-mining-feasibility-study.html). |
| Planetary Resources "$50–500/kg" | replaced with "no primary-source per-kg target locatable; not traceable to any PR primary document" + **new peer-reviewed row** | PR range unverifiable against any primary PR document. Substituted [Colvin, Crane & Lal 2020, *Acta Astronautica* 176](https://www.sciencedirect.com/science/article/abs/pii/S009457652030312X): "at least **$3,000/kg**" delivered to cis-lunar space. |
| Bennu $9.5M/g | now shown as derivation "(= $1.16B ÷ 121.6 g)" | NASA: 121.6 g (2024-02-15 final accounting); ~$1.16B/15yr (New Frontiers). |
| Keck study title | "Asteroid Retrieval **Mission** Study" → "…**Feasibility** Study" | Correct title of the 2012 KISS report. |
| Falcon Heavy | year/config-stamped: "$90M (2018 list) ÷ 63.8 t expendable-max; lower payload when boosters recovered" | Wikipedia price history; expendable-max capacity. |
| Falcon 9 | "expendable-max" clarification added; **$74M / 2026 price RE-VERIFIED CORRECT** | SpaceX raised the dedicated Falcon 9 price to **$74M in early 2026** (from $70M in 2025). [SatBase 2026](https://satbase.com/articles/spacex-falcon-9-price-increase-2026), [NextBigFuture Feb 2026](https://www.nextbigfuture.com/2026/02/spacex-falcon-9-true-cost-to-launch-is-about-300-per-pound-which-is-25-of-selling-price-to-customers.html). |

### Bibliography (§18 HTML) — provenance gaps closed
Three sources cited inline but absent from §18 (confirmed by grep), added in alphabetical position:
- **Black, Fischer, and Myron Scholes.** "The Pricing of Options and Corporate Liabilities." *Journal of Political Economy* 81, no. 3 (1973): 637–654. (cited 6723)
- **Brennan, Michael J., and Eduardo S. Schwartz.** "Evaluating Natural Resource Investments." *The Journal of Business* 58, no. 2 (1985): 135–157. (cited 6710, 6723; verified via [JSTOR](https://www.jstor.org/stable/2352967))
- **Knight, Frank H.** *Risk, Uncertainty and Profit.* Boston: Houghton Mifflin, 1921. (cited 6895)

### Bibliography (§23 repo `research/literature/bibliography.md`) — space-economics sources added
NASA OSIRIS-REx/Bennu; KISS 2012 (with the mass/$-per-kg correction recorded); Colvin/Crane/Lal 2020; Falcon 9 price-verification note. All flagged "verified 2026-06-08 (this session)."

### Notation (HTML) — B-glyph collision
**C1 (symbol-sweep):** the abbreviation "B" = billion collides with the defined Accountability-Bond variable **B** in exactly the quantitative passages a referee reads closely. 53 occurrences (grep-confirmed). Spelled out "billion" (55 total replacements incl. 2 newly introduced in §11.10); **value-preserving — no number changed.** Verified: 0 digit-then-B remaining; B₁/B₂/bare-B Bond variables untouched (48 still present). *Note: "M" (million) and "T" (trillion) were left abbreviated — they collide with no defined variable. A global million/trillion spell-out would be a stylistic choice for the author, not a collision fix.*

---

## Part 2 — RE-VERIFICATION of prior-session committed edits (per author direction)

The prior (saturated) session committed ~14 TA edits, not yet merged. Re-verified independently:

| Committed edit | Verdict |
|---|---|
| Carbon $510 → **$496**/ton | ✓ CORRECT. 2.61 mt CO₂ × $190 = $495.9. Old $510 implied 2.68 mt (≠ stated 2.61). |
| Total $518–532 → **$504–518** | ✓ CORRECT cascade of the carbon fix. |
| Population 18,000 → **~19,000** | ✓ CORRECT. 2020 census McDowell = 19,111. |
| M1 combined $1,421–2,412 → **$1,595–2,702** | ✓ CORRECT. Old sum was below its own Habitability component ($1,566) — impossible. New = 1566+12+17 … 2610+50+42. (Eco/Cohesion addends rest on class-4 inputs → memo.) |
| scarcity_multiplier 6–7 → **1.27–1.31** | ✓ CORRECT given the formula. 1+ln(201)×0.05=1.27; 1+ln(501)×0.05=1.31. (The 0.05 Hotelling anchor + the natural-log reading are themselves class-4/ambiguous → memo.) |
| Falcon 9 $2,700 → **$3,245/kg** ($74M/22,800 kg, 2026) | ✓ NOW VERIFIED. I initially suspected the $74M; it is correct — SpaceX's early-2026 price. |
| Norway CS-reduction 84% → **16%** | ⚠ Arithmetically correct given inputs ($48/$300 = 16%; old "84%" computed the *remaining* fraction, not the reduction). **BUT** it (a) rests on the disputed $300 RCV anchor (class-4, see 3C) and (b) **inverts the Norway "dramatically reduced CS" narrative** (16% reduction is not "dramatic"). The resume doc already flags Norway as the **highest-risk** Path-B open question. → **Session D / decision memo, NOT mine to resolve.** |
| V_option $500–2,000 → **$50–500**/ton | Interim Path-B reconciliation; class-3 either way. → Session D. |
| IPG label "(without carbon)" → carbon-inclusive relabel | Part of the class-4 IPG apparatus → memo. |

**Net:** no committed edit is a factual error. The five arithmetic/cascade fixes are correct; Falcon 9 is verified; the two "soft" edits (Norway, V_option) are flagged-pending **by design** and belong to Session D.

---

## Part 3 — CLASS-4 (UNSUPPORTED) DEFECT REGISTER

The actionable core. Organized by defect *type* (recurring figures consolidated). **None of 3B/3C/3D/3E are applied this session** — they require author judgment and are carried in the decision memo. Line numbers are pre-billion-spellout (shifted +0–10 after Part-1 edits; re-grep at apply-time).

### 3A — Real-case empirical figures that ARE externally sourceable but are currently UNCITED in-text
*Treatment: add the external citation. Many anchors already sit in §23 (Census, BP/DOJ, EPA, USGS) or §23.2 candidates. These are the lowest-risk class-4 fixes — the numbers are likely right; they just name no authority.*

| Figure | § / line | Sourceable from |
|---|---|---|
| BP legal settlements $18.7B; federal criminal penalty $4B | §11.2 / 3911, 3914 | DOJ 2012/2015 BP resolutions (in §23: "$18.7B" + $20.8B DOJ) |
| Well-lifetime revenue ~$1.1B; 40–60M barrels | §11.2 / 3904 | **Conflicts with §23 reconciliation (rev ~$3–4B).** See memo — Deepwater cluster (Session E). |
| Libby: $600M+ Superfund; $250M+ asbestos; $50M+/yr monitoring; 80% world vermiculite | §11.3 / 3939–3952 | EPA Superfund record; W.R. Grace bankruptcy trust; USGS vermiculite |
| McDowell: 13-yr life-expectancy gap; ~100,000→~19,000 pop.; highest per-capita opioid death; 141/100K overdose | §11.1, §11.7, §6.7, §7.6, §16.3 (recurs) | US Census (in §23); CDC/RWJF county health rankings; CDC WONDER |
| Baotou: 11 km² tailings lake; ~10M t/yr tailings; ~$2–4B/yr RE export revenue; 100M Yellow-River-basin pop. | §11.4 / 3971–3987 | USGS MCS (already cited for the 69%/49% figures); peer-reviewed Baotou studies |
| Atmospheric CO₂ half-life ~100 yr / ~1000 yr residual | §7.3, §17.6 | IPCC AR6; Archer et al. — needs a real cite |
| 1960 coal price $4.50/ton; $4.50→$50 (2025) inflation | §11.6, §7.6 | EIA historical coal series (§23: ~$4.71–4.83/ton 1960); BLS CPI for the deflator |
| Sackler ~$11B; Big Three $21B (2022) | §6.7 / 2265 | Keefe *Empire of Pain* + litigation record (cited; confirm bib §12 covers specifics) |
| Katy Butler reimbursement $461 vs $54; ~80 hr/wk; GoFundMe 25× / 88% | §6.7 / 2189 | Butler (*Knocking on Heaven's Door*) — needs bib entry; the 25×/88% need their own source (Ly & Soman 2020 covers only racial disparity) |

### 3B — Framework-internal IPG / convergence multiples (the largest cluster; an editorial-frame question, not a sourcing one)
*The §9.5 twelve-cell table (33–122× / 45–89× / 67–134× McDowell; 15–17× / 12–21× / 16–19× Deepwater; 55–82× / 48–76× / 61–91× Libby; 12–35× / 18–48× / 22–41× Baotou), plus the "canonical" 33–122×, the "triangulated" 50–555×, the §3.2 IPG=33 illustration, and the §16.4 33×–122× sensitivity output. These are CIT **model outputs**, not external statistics. Calling them "class 4 unsupported" is half-right: they are unsupported **as external facts**, but they may be legitimate **class-2 derived** outputs IF the derivation is shown and they stop being labeled "canonical/documented." Treatment is an author judgment — see memo §"IPG apparatus."* **Do not mass-relabel without the author.**

### 3C — Posited per-unit anchors that feed downstream derivations (the load-bearing class-4)
*These are the dangerous ones: bare numbers that propagate into headline results. Treatment: estimate-label + cite the closest real anchor, OR source, OR route the non-substitutable remainder to M3.*

| Anchor | § / line | Feeds | Closest real anchor (from input-provenance audit) |
|---|---|---|---|
| Foreclosure-of-non-energy-use +$50–200/BOE | §11.5 / 4201 | M1 combined $161–422/BOE | none yet — **POSITED**; needs label or source |
| V_option $30–200/BOE (Norway); $50–500/ton (McDowell) | §11.5, §11.6, §11.8 | M3 RCV | class-3 parameter; Session D Path-B |
| Hotelling-rate proxy 0.05 (5%/yr) | §11.5, §11.6, §3.5 | scarcity_multiplier | attributed loosely to Hotelling 1931; **anchor value itself unsourced**; also natural-log-vs-base-10 ambiguity |
| $50/BOE & $300/BOE (Norway "17% captured") | §11.7 / 4943 | 17%/83% capture; the disputed $300 RCV | $48 M2 is derived; **$300 RCV is the disputed table figure (§11.5 body says $161–422)** |
| restoration $50,000–200,000/acre; 150,000 acres disturbed | §11.6 / 4649 | Ecosystem floor $12–50/ton | documented reclamation ~$12,000–15,500/acre (Appalachian Voices, §23); Pericak 2018 acreage (§23.2) |
| $200,000–500,000/displaced-resident; 50,000 out-migration | §11.6 / 4666 | Cohesion floor $17–42/ton | Isle de Jean Charles ~$1.3M/household (§23.2); Census ~80K decline |
| industry-paid $5–8B; other-compensation $5–10B; reclamation-net $3–5B | §11.6 / 4719, 4702, 4696 | M2 realized-B $53–60B / $8–88/ton | OSMRE/GAO $4–6B gap (§23); rest are back-outs |
| S_max ≈ 0.85; RCV $580–620/ton (§11.1) | §11.1 / 3886 | §11.1 IPG | bare; "Weitzman" named but uncited |
| Norway M1 $300–650/BOE (table) vs body $161–422 | §11.5 / 4374; §3.6 / 1094 | triangulation | **internal contradiction** — table ≠ body |
| McDowell M1 $310–1,800/ton (§3.6) vs §11.6 $290–2,702 | §3.6 / 1111 | triangulation | **stale vs the corrected §11.6 anchor** |

### 3D — Method-3 parameters (currently class-3; mostly OK, two real issues)
σ / α / V_option / β across §3.5, §11.5, §11.6, §11.8 are explicitly posited (class-3) and acceptable as labeled calibration. **Two non-cosmetic issues:** (1) the **Hotelling 0.05 anchor** is unsupported (3C); (2) `scarcity_multiplier = 1 + log(1+σ)×0.05` **reproduces only under natural-log** — the notation `log` is ambiguous and base-10 gives a different (~1.12) result. Flag for the author. The M3 midpoints ($280 Norway, $2,500 McDowell) are **not arithmetic means** of their stated ranges and carry no stated weighting rule.

### 3E — §11.9 DAC intro internal inconsistency (clean internal-correctness fix)
§11.9's intro paragraph states $600–**1,200** / $**150**–500 / $100–**200** per ton CO₂, but every **sourced** element of the section (facility table, consolidated range, anchor blockquote, IEA/IPCC/NAS lit) supports **$600–1,000 / $300–600 / $100–300**. The intro's $1,200/$150/$500/$200 bounds are unsupported and contradict the section's own cited body. *Treatment: correct the intro to match the sourced body. No external sourcing needed — pure internal consistency. Candidate for the internal-correctness sweep (Session C) or a fast author ratify.*

---

## Part 4 — CLASS-1 SOURCED-ANCHOR INVENTORY (what is solid)

External authorities genuinely cited in-text (the framework's defensible empirical spine). Those marked **(bib?)** need a formal §18 or §23 entry confirmed.

- **Norway/GPFG (§11.5, §3.4):** Norwegian Offshore Directorate (cumulative ~55B BOE; 8.9/15.6 Sm³; 50/50 split); NBIM Annual Report 2025 (NOK 21,268B end-2025 — **verified** [NBIM](https://www.nbim.no/en/news-and-insights/reports/2025/annual-report-2025/); USD "~$2.0T / $2.2T peak" is FX-date-sensitive, see memo); Statistics Norway (pop. 5.62M); Norway fiscal rule 2001 (3%, **verify current ~2%**). **(bib?)** — add NBIM + NOD + Statistics Norway to §23.
- **DAC (§3.3, §11.6, §11.9):** Climeworks Orca/Mammoth; IEA *DAC 2022* + *Net Zero 2050*; IPCC AR6 WG III Ch.12; US National Academies 2019; Realmonte et al. 2019; House et al. 2011; Keith et al. *Joule* 2018; Carbon Engineering/1PointFive. **Strongly sourced** (URLs in §11.9). The bands are class-1 by attribution; **but §11.5/§3.3 cite no source *inline*** — they rely on §11.9 / the sourcing-pass file. Recommend inline cites.
- **Carbon/SCC:** EPA 2023 SCC $190/ton (attribute to EPA 2023, **not** Rennert et al. 2022 ≈ $185); §23 records this distinction.
- **Coal emission factor (§11.1, §11.6, §7.4):** EPA AP-42 §1.1 (93.28 kg/mmBtu); USGS PP 1625-C + WV Geological Survey (~28 mmBtu/short ton); EIA (24.93 mmBtu national avg). → 2.61 / 2.32 mt CO₂/short ton (derived, reproduces).
- **Black Lung / reclamation (§11.6):** DOL OWCP + Black Lung Disability Trust Fund ($44B; $5.1B outstanding 9/2024); OSMRE + GAO-17-207R ($4–6B gap); OSMRE bankruptcy filings (~$865M). **(bib?)**
- **Baotou (§11.4):** USGS *Mineral Commodity Summaries 2025* (69% production; 49% China reserves; ~37–40% Bayan Obo). The one well-formed external cite in §11.4.
- **Discount-rate sensitivity (§16.4, §6.7):** Stern (1.4%); Nordhaus (5.5%); Weitzman 2001 (declining rate; in §18). EPA SCC $190 / $51 prior.
- **§6.7 walkthrough sources:** Keefe *Empire of Pain* (2021); Ly & Soman 2020; Katy Butler **(bib?)**; opioid litigation record.
- **§11.10 space (this session):** NASA OSIRIS-REx; KISS 2012; Colvin/Crane/Lal 2020; SpaceX; all now in §23.

---

## Part 5 — Sources VERIFIED this session (added to bibliography)

| Source | For | URL |
|---|---|---|
| KISS 2012 *Asteroid Retrieval Feasibility Study* | Keck $5,200/kg correction | kiss.caltech.edu/final_reports/Asteroid_final_report.pdf |
| Colvin, Crane & Lal 2020, *Acta Astronautica* 176 | per-kg asteroid-propellant anchor ≥$3,000/kg | sciencedirect.com/science/article/abs/pii/S009457652030312X |
| NASA OSIRIS-REx (121.6 g; ~$1.16B) | Bennu derivation | science.nasa.gov/mission/osiris-rex/ |
| SpaceX Falcon 9 $74M (2026) | Falcon 9 $/kg | SatBase 2026; NextBigFuture 2026-02 |
| NBIM Annual Report 2025 (NOK 21,268B) | Norway GPFG vintage | nbim.no/.../annual-report-2025/ |
| Brennan & Schwartz 1985; Black–Scholes 1973; Knight 1921 | §18 inline-citation gaps | JSTOR / canonical |

**Still to add to §23 (sourceable, deferred to decision-memo apply):** NBIM/NOD/Statistics Norway formal entries; CDC/RWJF (life-expectancy); EPA Superfund + W.R. Grace trust (Libby); CDC WONDER (overdose); IPCC/Archer (CO₂ half-life); BLS CPI (inflation deflator); Katy Butler.

---

## Part 6 — Goal state & what remains

**Goal:** a TA where every surviving number is class 1/2/3, zero class-4, all sources in the bib.

**This session delivered:** the full classification (this ledger); the §11.10 cluster to class 1/2; the §18 + §23 bib gaps for applied items; the B-collision fix; re-verification of all committed edits. **The §11.10 cluster is now class-4-free.**

**Remaining to reach zero class-4 (decision memo + later sessions):**
- 3A: add citations (low-risk; ~12 figures) — needs author OK on which to source vs cut.
- 3B: resolve the IPG-apparatus frame (relabel-as-derived vs show-derivation) — author judgment.
- 3C: estimate-label / source the load-bearing per-unit anchors — overlaps Session D (M3 Path-B) for V_option/$300-RCV/Norway.
- 3D: fix the `log` ambiguity + Hotelling-0.05 source.
- 3E: §11.9 DAC intro internal-consistency fix (fast).
- Deepwater $1.1B-revenue reconciliation (Session E).
- C3 Solow 1956→1974: coordinate with the correctness sweep; see memo.

---

*End ledger. Companion decision memo carries the author-judgment items. No merge to main; author reviews the branch.*
