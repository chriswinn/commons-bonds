# Commons Bonds — Bidirectional Use-Case Cheat Sheet (forward RCV + reverse CSD)

**Purpose.** An at-a-glance walk-through of every use case, for a layman or an academic, to
test whether the framework actually holds: each worksheet runs the same five steps, shows its
arithmetic, names its sources, and ends with a clear bottom-line dollar figure (or an honest
lower bound). Bring your own numbers anywhere a slot is marked open or illustrative — the
framework is the recipe, not the ingredient list.

> **INTERNAL WORKING DOCUMENT — author-facing.** Not publisher-facing prose. The Reparations
> worksheet is a structural capability test built entirely from the reparations field's
> published figures (candidate share with Prof. Darity); the coercion vector remains an Open
> slot throughout, per the author's first-person abstention. Figures marked `[verify]` need
> re-verification before any external use. Demonstrations A and B at the end are deliberately
> **outside the book** — they exist so readers can run the framework themselves.
>
> Notation: subscripts omitted in calc lines (B1, B2, t0); Greek spelled (alpha; sigma-f = the
> TA's final-sigma ς). This .md is the canonical artifact — render via the document pipeline.
> Supersedes the 2026-06-10 PDF + generator. Code blocks are kept to 70 columns for the
> xelatex render path.

---

## The recipe — all five steps appear on every worksheet, in both directions

```
Step 1  M1 = FIRST APPRAISAL
        forward: engineer-a-substitute cost | reverse: cost-to-cure

Step 2  M3 = SECOND APPRAISAL (option value, both directions)
        value_M3 = V_market x scarcity_mult(sigma-f)
                            x irrev_premium(alpha)
        scarcity_mult = 1 + ln(1+sigma-f) x 0.05
        irrev_premium = 1 / (1 - alpha)
        reverse readings: V_market = extinguished optionality /
        foregone service flow; sigma-f at extraction; alpha
        observed; ex-post vs ex-ante fork exposed, not settled
        >> COMPARE Step 1 with Step 2 — NEVER subtract them.
           Overlap = the result. Divergence = a diagnostic
           (which feature one appraiser cannot see).

Step 2v (only where a behavioral observable exists)
        VALUATION ESTIMATOR from the cost-bearer's own behavior:
        hedonic / VSL (Rosen 1974; Viscusi 1993)
        VSL = delta-wage / delta-risk
        (a third appraiser; worked in case 11)

Step 3  VALUE = the appraisals' overlap
        forward: RCV | reverse: CSD
        (one appraiser only, or M3 Open -> VALUE = that
        appraisal, a LOWER BOUND)

Step 4  M2 = READ THE RECEIPTS — the bond actually posted.
        Never a third appraiser.
        forward: B2-hat (Foreclosure Bond, e.g. Norway GPFG)
        reverse: B1-hat (Restitution Bond — restitution
        actually paid, and BY WHOM)

Step 5  GAP = VALUE - M2 reading
        << the ONLY minus sign in the framework >>
        CS_forward = RCV - B2-hat      CSD_gap = CSD - B1-hat
        Identity: total CS = (CSD - B1) + (RCV - B2)
```

**Analogy.** M1 and M3 are two **appraisers** valuing what was (or would be) taken; M2 is the
**receipts** for what was actually paid. Trust the appraisal where the appraisers agree; the
severance is appraisal minus receipts. You never subtract one appraiser from the other.

**Step states** (a step with no number still gets its line — its state explains why):
`[Filled]` number entered, work shown · `[Zero]` genuinely $0 (abundance; CIT toggle) ·
`[Open]` admitted, deliberately empty → the VALUE is a **lower bound** · `[Cited]` named by
the TA, not computed in this volume · `[Available]` an observable exists; no sourced number yet.

---

## The bottom lines, at a glance

| # | Case | Bottom-line CS | Status of the number |
|---|------|----------------|----------------------|
| 1 | McDowell coal | **$1,027–1,065 per ton** forward; reverse heads ≥ $3.7–6B vs $0 industry | Filled (forward); lower bound (reverse) |
| 2 | Norway petroleum | **$233/BOE → ~$12.8T cumulative** forward; ~$3.9T reverse (illustrative) | Filled; reverse labeled |
| 3 | Deepwater Horizon | **$8–12B** unrestituted beyond BP's $61.6B | Lower bound |
| 4 | Libby vermiculite | **≥ $0.5B** unrestituted on documented components alone | Lower bound |
| 5 | Baotou rare earths | **≥ $5–15B** reverse (B1 = 0) + forward premium not yet computed | Lower bound |
| 6 | Chesapeake oyster reef | **$20–37M floor owed by industry** ($211M central); **$115M already paid — all public** | Filled; M3 Open by design |
| 7 | Reparations (test) | **≥ $14.0T**, B1 ≈ 0 → gap ≥ $14.0T | Strict lower bound; field's own figure |
| 8 | Asteroid iron | **≈ 0.1–0.4× market** premium only (≈ zero by terrestrial standards) | Filled, by abundance |
| 9 | ISS / closed world | **the entire engineered cost is unbonded** (~$21K/kg water; ~$3.1B/yr) `[verify]` | Filled, parked |
| 10 | NFL concussions | **$1B+ paid (B1)**; value side not yet computed | B1 Filled `[verify]`; value Cited |
| 11 | Offshore rig (VSL demo) | **$1,000/worker-yr** priced into wages (illustrative) vs operator posting | Illustrative method demo |
| 12 | Apartment lease | **1,800·v $/yr** (at v = $25/hr: **$45,000/yr**, illustrative) | Filled in v |

---

## 1. McDowell County coal (forward-dominant; both directions live)

**FORWARD — RCV per ton**

```
Step 1  M1 = DAC at-scale $300-600/t-CO2 x 2.61 t-CO2/ton
             + eco/cohesion floors                          [Filled]
           = $812-1,658/ton at-scale (center ~$1,235)
             full DAC-horizon range $290-2,702/ton
Step 2  M3 low : 40 x 1.27 x 1/(1-0.85)= 6.67 -> $339/ton   [Filled]
        M3 high: 140 x 1.31 x 1/(1-0.95)= 20  -> $3,668/ton
        geometric center sqrt(339 x 3668) ~ $1,115/ton
        compare 1 vs 2: $1,235 vs $1,115 agree to ~10%
Step 3  VALUE (RCV) = overlap ~$340-2,700/ton
        center ~$1,000-1,500 (worked at $1,115)
Step 4  M2 reads realized B = $50-88/ton societally paid    [Filled]
        ($8-15/ton industry-paid)
Step 5  GAP: CS_forward = 1,115 - (50..88) = $1,027-1,065/ton
        IPG: 339/40 = 8.5x .. 3668/140 = 26.2x (center ~15x)
        integral lens: 67-134x
```

*Source: TA §11.6; §3.3 DAC bands; engine Parts 1–2 (exact reproductions).*

**REVERSE — CSD per legacy head**

```
Step 1  M1 heads: reclamation shortfall $3.7-6B  [Filled, documented]
        life-expectancy gap, community collapse,
        knowledge loss                                  [Cited/Open]
Step 2  M3 (extinguished option value of the heads)          [Open]
Step 3  VALUE (CSD) = documented heads only -> LOWER BOUND
Step 4  M2 reads B1-hat = Black Lung ~$44B through 2009     [Filled]
        (restitution-type)
Step 5  GAP per documented head — e.g. reclamation
        shortfall $3.7-6B vs $0 industry posting
```

*Source: TA §11.1; GAO/CRS via §11.6.*

**Bottom line: every ton carried ~$1,027–1,065 of unpaid severance forward; the backward bill
opens at $3.7–6B documented, none of it industry-posted.**
*Note: the TA's "realized B ~$53–60B" needs a B1/B2 split — Black Lung payouts are B1
(restitution); reclamation bonds are B2 (posted forward). Flagged for §11.6.*

## 2. Norway petroleum (forward exemplar; backward quantified illustratively)

**FORWARD — RCV per BOE**

```
Step 1  M1 = $161-422/BOE (DAC-anchored floor)              [Filled]
Step 2  M3 central = 80 x (1 + ln(101)x0.05 = 1.2308)
                        x (1/(1-0.65) = 2.857) = $281/BOE   [Filled]
        corners: 40 x 1.1966 x 2.0 = $96
                 120 x 1.2651 x 4.0 = $607
        compare 1 vs 2: $281 sits inside $161-422 -> trusted
Step 3  VALUE (RCV) ~ $281/BOE center
Step 4  M2 reads B2-hat = GPFG $2.0T / 0.75 capture
        / 55e9 BOE = $48.5/BOE                              [Filled]
Step 5  GAP: CS_forward = 281 - 48.5 = $233/BOE
        x 55B BOE cumulative = ~$12.8T
```

*Source: TA §11.5 (NBIM NOK 21,268B; Norwegian Offshore Directorate); engine Parts 1–2.*

**REVERSE — CSD, illustrative (labeled)**

```
Step 1  M1 ~ 20.35 Gt CO2 combusted x $190/t (EPA SCC)
           ~ $3.9T              [Filled, SCC-basis assumption]
Step 2  M3 (option value extinguished by combustion)         [Open]
Step 3  VALUE (CSD) ~ $3.9T -> single-appraiser LOWER BOUND
Step 4  M2 reads B1-hat ~ 0 for non-Norwegian cost-bearers
        (welfare state = B1-for-Norwegians only)    [Zero, by scope]
Step 5  GAP ~ $3.9T borne outside the GPFG's coverage
```

*Source: emissions TA §11.5 (sourced); EPA 2023 SCC.*

**Bottom line: $233/BOE unbonded forward — ~$12.8T cumulative; plus ~$3.9T backward
(illustrative) borne by people the GPFG doesn't cover.**
*Note: Norway's architecture lowers effective alpha to 0.50–0.75 — it attacks the foreclosure
premium itself; the backward run shows whom it does not cover.*

## 3. Deepwater Horizon (backward-dominant; the industry-paid-B1 exemplar)

**REVERSE — CSD, total dollars**

```
Step 1  M1 (documented cure + damage)                       [Filled]
        = $61.6B all-in (BP 2016; $65B+ by 2018)
          + $8-12B ongoing ecosystem = ~$69.6-73.6B
Step 2  M3 (option value of foreclosed Gulf services)        [Open]
Step 3  VALUE (CSD) = $69.6-73.6B -> LOWER BOUND
Step 4  M2 reads B1-hat = $61.6B — INDUSTRY-paid,
        litigation-forced (the corpus's largest B1)         [Filled]
Step 5  GAP = (69.6..73.6) - 61.6 = ~$8-12B
        (ongoing externalities beyond BP's charges)
        checks: 61.6/4.0 = 15.4x documented
                (61.6+8..12)/4.0 = 17-18x with ongoing
```

*Source: TA §11.2 (settlement components; revenue = labeled framework estimate ~50M bbl × $80).*

**FORWARD — RCV of the remaining-well class**

```
Step 1  M1 (replace what new drilling would foreclose)      [Cited]
Step 2  M3 (option value of deferral)                       [Cited]
Step 3  VALUE (RCV): not computed in this volume            [Cited]
Step 4  M2 reads B2-hat = decommissioning bonds
        (BSEE 30 CFR 250/254; BLM)                          [Cited]
Step 5  GAP: not computable until Steps 1-3 are entered
```

**Bottom line: $8–12B of severance remains unrestituted beyond BP's $61.6B — and the $61.6B
proves an industry-paid B1 exists at scale (post-hoc, litigation-forced).**
*Contrast set: reef B1 = public-paid; reparations B1 = absent; Deepwater B1 = industry-paid.*

## 4. Libby, Montana vermiculite (backward-dominant; mixed-assignment B1)

**REVERSE — component arithmetic written out (which is what exposes the gap)**

```
Step 1  M1 components:                                      [Filled]
        $600M+ Superfund + $250M+ settlements
        + $50M+/yr medical + $500M+ property
        component sum ~ $1.35B + medical accrual
        (~50M x ~26 yrs ~ $1.3B) ~ $2.7B
        stated TA total "$4B+ (40:1)" NOT reachable from
        the listed components -> provenance pass owns it
Step 2  M3 (option value of foreclosed health/community)     [Open]
Step 3  VALUE (CSD) >= $1.35B documented -> LOWER BOUND
Step 4  M2 reads B1-hat = $600M public (Superfund)
        + $250M industry -> ~70/30 public/industry          [Filled]
Step 5  GAP >= 1.35B - 0.85B = $0.5B+ on components alone
        ratio check: 1.35B / $100M revenue >= 13.5x
```

*Source: TA §11.3; component-sum + ratio checks are this worksheet's own arithmetic. IPG
triplet (55–82×/48–76×/61–91×): no work shown — queued `[verify]`.*

**FORWARD — RCV of further extraction**

```
Step 1  M1: mine closed 1990; nothing to substitute          [Zero]
Step 2  M3: no remaining optionality to price                [Zero]
Step 3  VALUE (RCV) ~ 0
Step 4  M2 reads B2-hat: no forward instrument needed        [Zero]
Step 5  GAP ~ 0 — the case lives in the backward term
```

**Bottom line: ≥ $0.5B unrestituted on documented components alone, after crediting both the
public's $600M and industry's $250M.**
*Epistemic-commons case: 27-year concealment held B ≈ 0 while costs accrued; concealment also
suppressed the workers' wage premium — see case 11's asymmetry measurement.*

## 5. Baotou rare earths (both directions live and large simultaneously)

**REVERSE — CSD**

```
Step 1  M1 (cure): tailings-lake remediation $5-15B
        (cited estimate); health / agricultural /
        relocation heads                                    [Cited]
Step 2  M3 (option value of foreclosed land/water)           [Open]
Step 3  VALUE (CSD) >= $5-15B -> LOWER BOUND
Step 4  M2 reads B1-hat ~ 0 identified         [Zero, identified]
Step 5  GAP >= $5-15B
        scale check: remediation / annual export revenue
        = (5..15)/(2..4) = 1.3x-7.5x of one year's
        revenue                              [illustrative]
```

**FORWARD — RCV of ongoing extraction**

```
Step 1  M1 (substitute REE supply / recycling at scale)     [Cited]
Step 2  M3: high-sigma-f REE register (2010-12 export-
        restriction price spikes ground the dial)           [Cited]
Step 3  VALUE (RCV): not computed in this volume            [Cited]
Step 4  M2 reads B2-hat ~ 0 identified         [Zero, identified]
Step 5  GAP = the forward premium, ongoing
```

*Source: TA §11.4 / §11.8. IPG triplet (12–35×/18–48×/22–41×): denominator unstated — queued `[verify]`.*

**Bottom line: ≥ $5–15B backward with nothing posted, plus an uncomputed forward premium —
the case where forward-only accounting misses half the bill.** *(See Demonstration A for the
reservation question this case naturally raises.)*

## 6. Chesapeake oyster reef (the worked REVERSE case; Restitution Bond design)

**REVERSE — the five steps end-to-end**

```
Step 1  M1 (cost-to-cure) = foreclosed extent
        x realized restoration unit-cost                    [Filled]
        realized : 2,738 ac x ($907,000/124 ac
                   = $7,314/ac)              =  $20.0M
        headline : 2,738 ac x $13,500/ac     =  $37.0M
        central  : 2,738 ac x $77,000/ac     = $210.8M
        (central is the robust center, not the floor)
Step 2  M3 (foregone-fishery option value): admitted,
        deliberately NOT entered — "bond only the
        unassailable floor"                       [Open, by design]
Step 3  VALUE (CSD) = $20-37M floor / ~$211M central
        -> a LOWER BOUND
Step 4  M2 reads B1-hat = MD $93.52M + VA $21.77M
        = $115.29M itemized (>$92M MD alone)                [Filled]
        funders 100% public (NOAA, USACE, MD DNR, VMRC)
        industry share = $0
        corroboration: $108M/1,900 ac = $56,842/ac
        -> inside the Step-1 band ($13.5K < $57K < $77K)
Step 5  GAP, floor basis: B1-hat ($115M) already EXCEEDS
        the $20-37M floor — restoration is happening;
        the finding is MIS-ASSIGNMENT (public paid,
        extractive industry $0)
        GAP, central basis: 210.8 - 115.3 = ~$95.5M
        unrestituted even crediting every public dollar
```

*Source: Schulte 2017 Front. Mar. Sci. 4:127; NOAA per-tributary table (Dec 2024); Great
Wicomico Tributary Plan §5; MD DNR / Gov. Moore Aug 26 2025; engine Part 4 (exact).*

**FORWARD — RCV of the remaining reef**

```
Step 1  M1 (substitute reef function for further loss)      [Cited]
Step 2  M3 (regeneration-function foreclosure — the
        renewal structure itself)                           [Cited]
Step 3  VALUE (RCV): not computed in this volume            [Cited]
Step 4  M2 reads B2-hat = sanctuary designations
        (in-kind forward instrument)                        [Cited]
Step 5  GAP: successor computation (TA §11.12, GATE-2-gated)
```

**Bottom line: bond the floor — $20–37M owed by the industry that took the reef down; the
public has already paid $115M; at the robust central figure ~$95.5M remains unrestituted.**
*Formally distinct object: a renewable commons with its renewal structure extracted. AREA
basis only; the Darling shell-mountain stays narrative.*

## 7. Reparations for Black American descendants of US slavery — STRUCTURAL TEST, not book content

**REVERSE — the field's own figures in the framework's slots**

```
Step 1  M1 (cost-to-cure) = per-person remedy
        x eligible population            [Filled, field's own]
        = ~$350,000 x ~40,000,000 = ~$14.0T
        basis: 2019 SCF mean Black-white household
        wealth gap $840,900
        trajectory: 1st ed (2016 SCF) $267K x 40M = $10.7T
        -> 2nd ed $14.0T (an unpaid CSD accrues as the
        gap compounds; B1 delay is not cost-neutral)
Step 2  M3 + the coercion vector: the floor deliberately
        excludes the coercion vector (author's first-person
        abstention; field flags direct pricing unresolved),
        the longevity gap (Himmelstein et al. 2022),
        cultural-knowledge severance, intergenerational
        trauma                                               [Open]
Step 3  VALUE (CSD) >= $14.0T -> a strict LOWER BOUND
Step 4  M2 reads B1-hat = federal $0 (no program;
        H.R. 40 never enacted) + pilots O($10M) ~ 0    [Zero, paid]
        comparators (the instrument exists for
        acknowledged harms):
        Civil Liberties Act 1988 ~ $20K x ~82K
        internees ~ $1.6B [verify]; Black Lung ~$44B
        -> $0 here is an acknowledgment gap,
           not an affordability gap
Step 5  GAP = 14.0T - ~0 >= $14.0T
```

*Source: Darity & Mullen, From Here to Equality 2nd ed. (UNC Press 2022); Darity–Mullen–
Slaughter, J. Econ. Perspectives 36(2) 2022 (verified 2026-06-10); public record for B1.*

**FORWARD — ongoing-harm streams**

```
Step 1  M1 (cure-cost of ongoing-harm streams)              [Cited]
Step 2  M3 (option value of continuing foreclosure)         [Cited]
Step 3  VALUE (RCV): outside current scope                  [Cited]
Step 4  M2 reads B2-hat: no instrument exists                [Open]
Step 5  GAP: not computable until Steps 1-3 are entered
```

**Bottom line: CSD ≥ $14.0T and B1 ≈ 0, so the gap ≥ $14.0T — a strict lower bound, built
entirely from the field's own published numbers.**
*Same five steps as the reef; the structural difference made visible: reef B1 = large but
MIS-ASSIGNED; reparations B1 = ABSENT.*

## 8. Asteroid iron, pre-extraction (the zero-anchor)

**FORWARD — RCV per unit**

```
Step 1  M1 ~ market price: the substitute for one
        asteroid is the next asteroid
        (substitutability ~ 1)            [Filled, by abundance]
Step 2  M3 = market x (1.03-1.12) x (1.05-1.25)
           = ~1.1-1.4x market                               [Filled]
        compare 1 vs 2: both land at ~market -> trusted
Step 3  VALUE (RCV) ~ market (CIT abundance: weights ~ 1)
Step 4  M2 reads B2-hat: regime design question —
        nothing posted yet                                  [Cited]
Step 5  GAP ~ the small premium only (~0.1-0.4x market)
```

**REVERSE — CSD**

```
Step 1  M1: nothing extracted yet — no loss to cure          [Zero]
Step 2  M3: no optionality extinguished yet                  [Zero]
Step 3  VALUE (CSD) ~ 0
Step 4  M2 reads B1-hat: nothing owed, nothing paid          [Zero]
Step 5  GAP ~ 0 — assembles trivially, which is the point
```

**Bottom line: CS ≈ 0.1–0.4× market — effectively zero by terrestrial standards. That the
framework prices abundance at ~market, with no premium, is the calibration check.**

## 9. Closed-world habitat — ISS anchor (the CIT demonstration)

**FORWARD — what Earth's free commons cost to engineer**

```
Step 1  M1 unit anchor: water up-mass ~$21,000/kg
        (why ECLSS exists: ~90% recovery;
        93% -> >98% loop closure)                  [Filled, parked]
        program scale: ~$150B all-partner build (~2010)
        US-only ~$75B through 2013 (a SUBSET, not a
        rival total); ~$3.1B/yr NASA ops
        scope contrast: $3.1B/yr / ~7 crew
        ~ $440M/person-yr ALL-IN program, vs TA §6.2
        ~$1M-10M/person-yr life-support-only — never
        conflate the two scopes
Step 2  M3: planetary-scale atmosphere loss -> alpha -> 1
        -> §12 boundary + ARR                               [Cited]
Step 3  VALUE (RCV) = the engineered-substitute cost band
Step 4  M2 reads B2-hat ~ 0 — nothing posted          [Zero, posted]
Step 5  GAP = the entire engineered cost is unbonded
```

*Source: parked candidates, bib §23.2 — re-verify vs NASA OIG (IG-18-021, IG-22-005) `[verify]`.*

**REVERSE — CSD**

```
Step 1  M1: no commons severed — the habitat IMPORTS
        its commons                                          [Zero]
Step 2  M3: nothing extinguished                             [Zero]
Step 3  VALUE (CSD) ~ 0
Step 4  M2 reads B1-hat: not applicable — nothing owed       [Zero]
Step 5  GAP ~ 0
```

**Bottom line: strip the abundance and Earth's free commons acquire a documented price —
~$21K per kilogram of water, ~$3.1B a year to keep seven people alive — none of it bonded
anywhere. The cleanest Commons Inversion Test on record.**

## 10. NFL concussions (information-asymmetry case-class; both directions)

**REVERSE — CSD for the pre-disclosure cohort**

```
Step 1  M1 (care + career-shortening cure-costs)            [Cited]
Step 2  M3 (option value of foreclosed careers)              [Open]
Step 3  VALUE (CSD): per-head lower bound as entered
Step 4  M2 reads B1-hat ~ $1B+ uncapped settlement,
        industry-paid, litigation-forced [verify]           [Filled]
Step 5  GAP: per-head vs the settlement's coverage classes
```

**FORWARD — RCV for current players (post-2013 disclosure)**

```
Step 1  M1 (medical + career-transition replacement)        [Cited]
Step 2  M3 (option value of optionality at risk)            [Cited]
Step 2v wage premium on DISCLOSED risk = revealed
        valuation (method in case 11)                   [Available]
Step 3  VALUE (RCV): not computed in this volume            [Cited]
Step 4  M2 reads B2-hat = CBA health funds +
        settlement-funded monitoring                 [Filled, cited]
Step 5  GAP: not computable until Steps 1-3 are entered
```

**Bottom line: $1B+ has actually been paid (industry, post-hoc) — the B1 reading; the value
side awaits entry. Pre-2013, concealment suppressed the wage premium — case 11's asymmetry
measurement applies.**

## 11. Offshore oil rig — the hedonic/VSL estimator demonstrated (Step 2v worked)

**FORWARD — with the valuation estimator written out (ILLUSTRATIVE parameters, labeled)**

```
Step 1  M1 (safety-engineering substitute: the cost of
        eliminating the risk)                               [Cited]
Step 2  M3 (option value of the worker's health/career
        optionality at risk)                                [Cited]
Step 2v VALUATION estimator           [Filled, illustrative]
        VSL = delta-wage / delta-risk
        textbook line: delta-wage = $1,000/yr for
        delta-risk = 1/10,000 fatality/yr
        VSL = 1,000 / 0.0001 = $10M
        [US regulatory practice ~$10-13M (2020s) [verify]]
        risk-priced premium per worker-year
        = VSL x delta-risk (= the $1,000 above)
        column discipline:
          hazard pay = what workers REVEAL the risk is
          worth (THIS step); insurance / bonds /
          settlement funds = what the operator POSTED
          (Step 4)
Step 3  VALUE (RCV, human-risk component) ~ the Step-2v
        reading where 1 and 2 are not entered
        -> single-appraiser LOWER BOUND
Step 4  M2 reads B2-hat = operator postings per worker
        (insurance, bonds)                                  [Cited]
Step 5  GAP demo: if (VSL x delta-risk) per worker-yr
        > operator posting per worker-yr, the difference
        is severance priced into wages but never bonded
```

**REVERSE — CSD for realized harms**

```
Step 1  M1 (realized injury/fatality cure +
        compensation costs)                                 [Cited]
Step 2  M3 (option value extinguished, harmed cohort)        [Open]
Step 3  VALUE (CSD): per-head lower bound as entered
Step 4  M2 reads B1-hat = workers' comp + settlements
        actually paid                                       [Cited]
Step 5  GAP: per-head vs what was paid, and BY WHOM
```

**THE ASYMMETRY MEASUREMENT (what Step 2v uniquely adds)**

```
A worker cannot charge for risk they do not know about.
Under concealment:
  revealed premium = VSL x (risk as KNOWN to the worker)
  informed premium = VSL x (risk as it ACTUALLY was)
  informed - revealed = VSL x (concealed risk)
                      <-- the information asymmetry, IN DOLLARS
This turns "the severance the cost-bearer bore unknowingly"
(NFL pre-2013; Libby's 27 years; the apartment signed after
a midnight test-drive) from a narrative claim into a number.
```

**Bottom line (illustrative): ~$1,000 per worker-year is priced into wages for the risk;
whatever the operator hasn't posted against that same risk is severance the wage absorbed
but no bond covers.**
*Why this estimator earns its place: the only appraiser built from the cost-bearer's own
behavior; gives labor-market cases a third appraiser; measures information asymmetry in
dollars; mainstream welfare economics (Rosen/Viscusi). Kept strictly in the valuation
column — never plugged into M2.*

## 12. Apartment lease — the commute trade (n-of-1 self-severance; no bad actor)

**FORWARD — at signing (v = your revealed-preference hourly value; the input slot)**

```
Step 1  M1 (engineer the substitute: the close-in
        apartment's rent premium — the observable
        exists; no number entered here)                 [Available]
Step 2  M3 (time-value appraisal) = 1,800 hrs/yr
        foreclosed x v $/hr = 1,800v $/yr            [Filled, in v]
        compare 1 vs 2: when both are entered, the rent
        premium cross-checks 1,800v
Step 3  VALUE (RCV) = 1,800v -> single-appraiser LOWER
        BOUND until Step 1 is entered
Step 4  M2 reads B2-hat = 0 — no instrument exists           [Zero]
Step 5  GAP: CS_forward = 1,800v - 0 = 1,800v
```

**REVERSE — after the year**

```
Step 1  M1 = the same 1,800v, realized (the hours are
        gone; v now known with certainty)            [Filled, in v]
Step 2  M3: no further optionality for a completed year      [Zero]
Step 3  VALUE (CSD) = 1,800v realized
Step 4  M2 reads B1-hat = 0                                  [Zero]
Step 5  GAP = 1,800v
        case-11 note: the midnight test-drive =
        self-inflicted information asymmetry
```

**Bottom line: CS = 1,800·v dollars a year. At v = $25/hr (illustrative), the lease cost
$45,000 a year of severance nobody bonded — including you.**
*Value-capturer = cost-bearer; no extractor. The apparatus runs identically at n-of-1 — an
accounting framework, not a theory of villains.*

---

## Demonstration A — "Should we reserve some?" The reservation decision the framework already contains

> **Deliberately outside the book.** This demonstration exists so a reader can run it with
> their own numbers; the book supplies the recipe, not the conclusion.

```
THE DECISION RULE
(Def 1.9 + ARR §8.1 + Thm 10.5 + Cor 10.5.1 + §13):
  Reserve the marginal unit u whenever  RCV(u) > P(u)
  (equivalently IPG > 1 at the margin) — the option value
  of keeping it exceeds what extracting it fetches.
  Sequencing (Cor 10.5.1): extract lowest-RCV first
  -> reservation is not a separate policy; it is what
  naturally happens to the high-RCV tail that never
  clears the bar.
  Insurance framing (§13): cost of reserving fraction f
  = foregone revenue (deferred, not destroyed — Hotelling
  appreciation); benefit = avoided foreclosure of
  high-existential-gap units.
  Under uncertainty about the gap classification:
  ARR defaults HIGH — reserve. ("We can always extract
  later. We can never un-extract.")

BAOTOU ILLUSTRATION (all parameters illustrative):
  Step 2 with REE parameters: sigma-f HIGH (R/P register
  + the 2010-12 export-restriction price spikes — the
  scarcity dial firing in observed market data); alpha
  elevated for no-substitute magnet metals (Nd, Dy).
  Illustrative: RCV_M3 = P x 1.30 x (1/(1-0.8) = 5)
              = 6.5 x P  ->  IPG = 6.5 >> 1
  -> the marginal unit is worth ~6.5x more in the ground
  than at the dock: RESERVE, and fund substitution
  research (Thm 10.5) until the dial drops.
  What would flip it: alpha down (recycling proves out)
  or sigma-f down (new supply) -> IPG falls toward 1
  -> extraction of the marginal unit re-opens.
  The framework doesn't freeze the answer; it tells you
  exactly which dial to watch.
```

## Demonstration B — Coal vs wind/solar electricity, per MWh

> **Deliberately outside the book.** Same recipe, your numbers welcome.

```
COAL (per MWh, McDowell-class inputs from case 1):
  CS_forward ~ $1,027-1,065/ton (computed, case 1)
  conversion: ~2-2.5 MWh of electricity per ton
  (engineering assumption, labeled)
  -> hidden severance ~ $410-530 per MWh on top of the
  market price of coal power (dominated by the carbon
  term; inherits case 1's full provenance)

WIND / SOLAR (per MWh):
  Steps 1-3, fuel side: the fuel is a FLOW — sun and
  wind are not depleted by use. CIT: under abundance
  that extraction cannot foreclose, the foreclosure
  cost is genuinely $0 — the Zero state, not a
  subsidy assumption.                      [Zero, fuel side]
  Lifecycle side is NOT zero, and the framework prices
  it with the same five steps: materials upstream
  (REEs -> case 5 Baotou; turbine/panel minerals),
  land use, end-of-life. Real Ci, gate-admitted,
  orders smaller per MWh.                     [Cited/Open]
  M2: renewables post little B because little RCV
  needs bonding — same identity, small terms.

BOTTOM LINE: the framework does not "favor" renewables
by assumption. It runs the same five steps on both:
coal's fuel itself carries hundreds of dollars per MWh
of unbonded severance; sun and wind carry a fuel-side
Zero and an upstream materials bill the framework prices
separately (case 5 shows it is also currently unbonded).
The comparison is lopsided because the inputs are,
not because the method is.
```

---

## Provenance + regeneration

Computed values reproduce in `csd_rcv_calculations.py` (this directory); its run-output log
(dated 2026-06-10) records 21/21 reproduction checks PASS and 11/11 portfolio cases assembling
the identity with all slots in legal states. TA references are to `TechnicalAppendix_v2.0.0.html`
as merged 2026-06-10. Case 11's Step-2v parameters and both Demonstrations are illustrative
method demonstrations, not sourced figures. §11.12 (reef) merges to the TA only after a book
chapter carries the priced claim (GATE 2). This `.md` is the canonical artifact (renders via
the document pipeline; code blocks ≤70 columns for the xelatex path); it supersedes the
2026-06-10 PDF and its generator.
