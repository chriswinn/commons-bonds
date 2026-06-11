#!/usr/bin/env python3
"""
Generate the bidirectional use-case worksheet PDF (forward RCV + reverse CSD).

v4 format (2026-06-10, author feedback round 3):
  * HARD INVARIANT: every worksheet shows ALL FIVE STEPS, in order, in BOTH
    directions — no merged steps, no skipped steps. A step with no number
    shows its STATE instead (Filled / Open / Cited / Zero / Available).
    The build asserts this (24 direction-blocks x Steps 1-5).
  * Five-step recipe + appraisers/receipts analogy on page 1.
  * Step 2v: hedonic/VSL revealed-valuation estimator (Rosen 1974; Viscusi
    1993), worked in case 11 (offshore rig) with the asymmetry-measurement
    note and why-it-is-useful rationale.

Companion to csd_rcv_calculations.py — computed numbers trace to its verified
output (21/21 checks PASS) or the merged TA v2.0.0 (main @ 2026-06-10).
Regenerate: /tmp/pdfenv/bin/python gen_use_cases_pdf.py

Font discipline (reportlab base-14): no raw Greek / Unicode sub-superscripts.
B1/B2/M1/M2/M3/t0 written without subscripts in calc lines; Greek spelled
(alpha, sigma-f = the TA's final-sigma).
"""
from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch
from reportlab.lib import colors
from reportlab.platypus import (SimpleDocTemplate, Paragraph, Spacer,
                                PageBreak, Preformatted)

OUT = "csd-rcv-bidirectional-use-cases_2026-06-10.pdf"
S = getSampleStyleSheet()

h1 = ParagraphStyle("h1x", parent=S["Heading1"], fontSize=15, spaceAfter=6)
h2 = ParagraphStyle("h2x", parent=S["Heading2"], fontSize=11.5, spaceBefore=10,
                    spaceAfter=3, textColor=colors.HexColor("#1a3a5c"))
body = ParagraphStyle("bodyx", parent=S["Normal"], fontSize=9.2, leading=12.6)
small = ParagraphStyle("smallx", parent=S["Normal"], fontSize=7.8, leading=10.2,
                       textColor=colors.HexColor("#444444"))
banner = ParagraphStyle("bannerx", parent=S["Normal"], fontSize=8.6, leading=11.6,
                        textColor=colors.HexColor("#7a1f1f"))
calc = ParagraphStyle("calcx", parent=S["Code"], fontName="Courier",
                      fontSize=7.6, leading=9.7, leftIndent=8,
                      backColor=colors.HexColor("#f4f6f8"),
                      borderPadding=4, spaceBefore=2, spaceAfter=2)

story = []
A = story.append
direction_blocks = []   # collected for the five-step invariant check


def case(title, blocks, note=None, extra=None):
    A(Paragraph(title, h2))
    for label, text, src in blocks:
        if label:
            A(Paragraph("<b>" + label + "</b>", body))
        t = text.strip("\n")
        if label and (label.startswith("FORWARD") or label.startswith("REVERSE")):
            direction_blocks.append((title, label, t))
        A(Preformatted(t, calc))
        if src:
            A(Paragraph("Source: " + src, small))
    if extra:
        label, text, src = extra
        A(Paragraph("<b>" + label + "</b>", body))
        A(Preformatted(text.strip("\n"), calc))
        if src:
            A(Paragraph("Source: " + src, small))
    if note:
        A(Paragraph("<b>Note.</b> " + note, small))
    A(Spacer(1, 7))


A(Paragraph("Commons Bonds — Bidirectional Use-Case Worksheets (v4: five steps, every time)", h1))
A(Paragraph("Forward RCV and Reverse CSD across the full case portfolio (2026-06-10)", S["Heading3"]))
A(Spacer(1, 4))
A(Paragraph(
    "<b>INTERNAL WORKING DOCUMENT — author-facing.</b> Not publisher-facing prose. The Reparations "
    "worksheet is a structural capability test built entirely from the reparations field's published "
    "figures (candidate share with Prof. Darity); the coercion vector remains an Open slot throughout, "
    "per the author's first-person abstention. Figures marked [verify] need re-verification before any "
    "external use. Subscripts are omitted in calculation lines (B1, B2, t0); Greek is spelled "
    "(alpha, sigma-f).", banner))
A(Spacer(1, 8))

A(Paragraph("The recipe — all five steps appear on every worksheet, in both directions", h2))
A(Preformatted("""
  Step 1   M1 = FIRST APPRAISAL    forward: engineer-a-substitute cost  |  reverse: cost-to-cure
  Step 2   M3 = SECOND APPRAISAL   option value, both directions:
              value_M3 = V_market x scarcity_mult(sigma-f) x irrev_premium(alpha)
              scarcity_mult = 1 + ln(1+sigma-f) x 0.05        irrev_premium = 1 / (1 - alpha)
              (reverse: V_market = extinguished optionality / foregone service flow;
               sigma-f at extraction; alpha observed; ex-post vs ex-ante fork exposed)
           >> COMPARE Step 1 with Step 2 — NEVER subtract them. Their overlap is the result;
              their divergence is a diagnostic (which feature one appraiser cannot see).
  Step 2v  (only where a behavioral observable exists) VALUATION ESTIMATOR from the
           cost-bearer's own behavior — hedonic / VSL (Rosen 1974; Viscusi 1993):
              VSL = delta-wage / delta-risk     (a third appraiser; worked in case 11)
  Step 3   VALUE = the appraisals' overlap      forward: RCV   |   reverse: CSD
           (one appraiser only, or M3 Open  ->  VALUE = that appraisal, a LOWER BOUND)
  Step 4   M2 = READ THE RECEIPTS — the bond actually posted; never a third appraiser:
              forward: B2-hat (Foreclosure Bond, e.g. Norway GPFG)
              reverse: B1-hat (Restitution Bond — restitution actually paid, and BY WHOM)
  Step 5   GAP = VALUE - M2 reading             << the ONLY minus sign in the framework >>
              CS_forward = RCV - B2-hat         CSD_gap = CSD - B1-hat
              Identity:  total CS = (CSD - B1) + (RCV - B2)

  ANALOGY: M1 and M3 are two APPRAISERS valuing what was (or would be) taken; M2 is the
  RECEIPTS for what was actually paid. Trust the appraisal where the appraisers agree;
  the severance is appraisal minus receipts. You never subtract one appraiser from the other.

  STEP STATES (a step with no number still gets its line — its state explains why):
    Filled    = number entered, work shown            Zero  = genuinely $0 (abundance; CIT toggle)
    Open      = admitted, deliberately empty -> the computed VALUE is a LOWER BOUND
    Cited     = named by the TA, not computed in this volume
    Available = an observable exists; no sourced number entered yet
""", calc))
A(Paragraph(
    "Provenance: computed values reproduce in core/technical-appendix/calculations/"
    "csd_rcv_calculations.py (21/21 checks PASS vs the merged TA); every input names its external "
    "source. TA = TechnicalAppendix_v2.0.0.html, main @ 2026-06-10.", small))
A(PageBreak())

# ------------------------------------------------------------------ cases
case("1. McDowell County coal (forward-dominant; both directions live)", [
    ("FORWARD — RCV per ton", """
Step 1  M1 = DAC at-scale $300-600/t-CO2 x 2.61 t-CO2/ton + eco/cohesion floors
           = $812-1,658/ton at-scale (center ~$1,235); full DAC-horizon range $290-2,702  [Filled]
Step 2  M3 = low  40 x 1.27 x 1/(1-0.85)= 6.67  -> $339/ton
             high 140 x 1.31 x 1/(1-0.95)= 20    -> $3,668/ton
             geometric center sqrt(339 x 3668) ~ $1,115/ton                               [Filled]
        compare 1 vs 2: centers $1,235 vs $1,115 agree to ~10%  ->  appraisal trusted
Step 3  VALUE (RCV) = overlap ~$340-2,700/ton; center ~$1,000-1,500 (worked at $1,115)
Step 4  M2 reads realized B = $50-88/ton societally paid ($8-15 industry-paid)            [Filled]
Step 5  GAP: CS_forward = 1,115 - (50..88) = $1,027-1,065/ton
        IPG: 339/40 = 8.5x .. 3668/140 = 26.2x (center ~15x); integral lens 67-134x""",
     "TA Sec. 11.6; Sec. 3.3 DAC bands; engine Parts 1-2 (exact reproductions)"),
    ("REVERSE — CSD per legacy head", """
Step 1  M1 (cost-to-cure heads): reclamation shortfall $3.7-6B [Filled, documented];
        life-expectancy gap, community collapse, knowledge loss                  [Cited/Open]
Step 2  M3 (extinguished option value of the foreclosed heads)                   [Open]
Step 3  VALUE (CSD) = the documented heads only  ->  a LOWER BOUND
Step 4  M2 reads B1-hat = Black Lung ~$44B through 2009 (restitution-type)       [Filled]
Step 5  GAP: per documented head — e.g. reclamation shortfall $3.7-6B vs $0 industry posting""",
     "TA Sec. 11.1; GAO/CRS via Sec. 11.6")],
    "Bidirectional finding: the TA's 'realized B ~$53-60B' needs a B1/B2 split — Black Lung payouts are B1 "
    "(restitution); reclamation bonds are B2 (posted forward). Flagged for Sec. 11.6.")

case("2. Norway petroleum (forward exemplar; backward quantified illustratively)", [
    ("FORWARD — RCV per BOE", """
Step 1  M1 = $161-422/BOE (DAC-anchored replacement floor)                        [Filled]
Step 2  M3 = 80 x (1 + ln(101)x0.05 = 1.2308) x (1/(1-0.65) = 2.857) = $281/BOE central
             corners: 40 x 1.1966 x 2.0 = $96   |   120 x 1.2651 x 4.0 = $607     [Filled]
        compare 1 vs 2: $281 sits inside M1's $161-422  ->  appraisal trusted
Step 3  VALUE (RCV) ~ $281/BOE center
Step 4  M2 reads B2-hat = GPFG $2.0T / 0.75 capture / 55e9 BOE = $48.5/BOE        [Filled]
Step 5  GAP: CS_forward = 281 - 48.5 = $233/BOE;  x 55B BOE cumulative = ~$12.8T""",
     "TA Sec. 11.5 (NBIM NOK 21,268B; Norwegian Offshore Directorate); engine Parts 1-2"),
    ("REVERSE — CSD, illustrative (labeled)", """
Step 1  M1 ~ 20.35 Gt CO2 combusted x $190/t (EPA SCC) ~ $3.9T   [Filled, SCC-basis assumption]
Step 2  M3 (option value extinguished by realized combustion)                     [Open]
Step 3  VALUE (CSD) ~ $3.9T  ->  single-appraiser LOWER BOUND
Step 4  M2 reads B1-hat ~ 0 for non-Norwegian cost-bearers
        (welfare state = B1-for-Norwegians only)                                  [Zero, by scope]
Step 5  GAP ~ $3.9T - 0 = ~$3.9T borne outside the GPFG's coverage""",
     "Emissions TA Sec. 11.5 (sourced); EPA 2023 SCC")],
    "Norway's architecture lowers effective alpha to 0.50-0.75 — it attacks the foreclosure premium itself; "
    "the backward run shows whom it does not cover.")

case("3. Deepwater Horizon (backward-dominant; the industry-paid-B1 exemplar)", [
    ("REVERSE — CSD, total dollars", """
Step 1  M1 (documented cure + damage) = $61.6B all-in (BP 2016; $65B+ by 2018)
                                      + $8-12B ongoing ecosystem = ~$69.6-73.6B   [Filled]
Step 2  M3 (option value of the foreclosed Gulf ecosystem services)               [Open]
Step 3  VALUE (CSD) = $69.6-73.6B  ->  a LOWER BOUND (Step-2 slot open)
Step 4  M2 reads B1-hat = $61.6B — INDUSTRY-paid, litigation-forced
        (the corpus's largest realized B1)                                        [Filled]
Step 5  GAP = (69.6..73.6) - 61.6 = ~$8-12B (ongoing externalities beyond BP's charges)
        checks: IPG ~ 61.6/4.0 = 15.4x documented; (61.6+8..12)/4.0 = 17-18x with ongoing""",
     "TA Sec. 11.2 (settlement components; revenue = labeled framework estimate ~50M bbl x $80)"),
    ("FORWARD — RCV of the remaining-well class", """
Step 1  M1 (replacement cost of what new drilling would foreclose)                [Cited]
Step 2  M3 (option value of deferral across the remaining-well class)             [Cited]
Step 3  VALUE (RCV): not computed in this volume                                  [Cited]
Step 4  M2 reads B2-hat = decommissioning bonds (BSEE 30 CFR 250/254; BLM)        [Cited]
Step 5  GAP: not computable until Steps 1-3 are entered — the TA names the
        direction; a successor computation fills it""",
     "TA Sec. 11.2; Sec. 5.1.2 (instrument cluster)")],
    "Contrast set: reef B1 = public-paid; reparations B1 = absent; Deepwater B1 = industry-paid post-hoc. "
    "The instrument exists at every assignment.")

case("4. Libby, Montana vermiculite (backward-dominant; mixed-assignment B1)", [
    ("REVERSE — component arithmetic written out (which is what exposes the gap)", """
Step 1  M1 components: $600M+ Superfund + $250M+ settlements + $50M+/yr medical + $500M+ property
        component sum ~ $1.35B + medical accrual (~50M x ~26 yrs ~ $1.3B) ~ $2.7B [Filled]
        stated TA total "$4B+ (40:1)" NOT reachable from listed components -> provenance pass
Step 2  M3 (option value of foreclosed health/community)                          [Open]
Step 3  VALUE (CSD) >= $1.35B documented  ->  conservative LOWER BOUND
Step 4  M2 reads B1-hat = $600M public (Superfund) + $250M industry (settlements)
        ->  ~70/30 public/industry                                                [Filled]
Step 5  GAP >= 1.35B - 0.85B = $0.5B+ on components alone;
        ratio check: 1.35B / $100M lifetime revenue >= 13.5x""",
     "TA Sec. 11.3; component-sum + ratio checks are this worksheet's own arithmetic. "
     "IPG triplet (55-82x/48-76x/61-91x): no work shown — queued [verify]"),
    ("FORWARD — RCV of further extraction", """
Step 1  M1: mine closed 1990; nothing left to substitute against                  [Zero]
Step 2  M3: no remaining optionality to price                                     [Zero]
Step 3  VALUE (RCV) ~ 0
Step 4  M2 reads B2-hat: no forward instrument needed                             [Zero]
Step 5  GAP ~ 0 — the case lives entirely in the backward term""", None)],
    "Epistemic-commons case: 27-year concealment held B ~ 0 while costs accrued. Concealment also "
    "suppressed the workers' wage premium — see case 11's asymmetry measurement.")

case("5. Baotou rare earths (both directions live and large simultaneously)", [
    ("REVERSE — CSD", """
Step 1  M1 (cure): tailings-lake remediation $5-15B (cited estimate);
        health / agricultural / relocation heads                                  [Cited]
Step 2  M3 (option value of foreclosed land, water, health)                       [Open]
Step 3  VALUE (CSD) >= $5-15B  ->  LOWER BOUND
Step 4  M2 reads B1-hat ~ 0 identified restitution                                [Zero, identified]
Step 5  GAP >= $5-15B;  scale check: remediation / annual export revenue
        = (5..15)/(2..4) = 1.3x-7.5x of a full year's revenue  [illustrative, not the TA's IPG]""",
     "TA Sec. 11.4. IPG triplet (12-35x/18-48x/22-41x): denominator unstated — queued [verify]"),
    ("FORWARD — RCV of ongoing extraction", """
Step 1  M1 (substitute REE supply / recycling at scale)                           [Cited]
Step 2  M3: ongoing extraction, high-sigma-f REE register
        (2010-12 export-restriction price spikes ground the scarcity dial)        [Cited]
Step 3  VALUE (RCV): not computed in this volume                                  [Cited]
Step 4  M2 reads B2-hat ~ 0 identified                                            [Zero, identified]
Step 5  GAP = the forward premium, ongoing — both directions live at once""",
     "TA Sec. 11.4 / 11.8")],
    "Forward-only accounting misses half this case: total CS needs BOTH (CSD - B1) and (RCV - B2).")

case("6. Chesapeake oyster reef (the worked REVERSE case; Restitution Bond design)", [
    ("REVERSE — the five steps end-to-end", """
Step 1  M1 (cost-to-cure) = foreclosed extent x realized restoration unit-cost    [Filled]
          realized basis : 2,738 ac x ($907,000/124 ac = $7,314/ac)  = $20.0M
          headline basis : 2,738 ac x $13,500/ac construction-only   = $37.0M
          robust central : 2,738 ac x $77,000/ac bay-wide average    = $210.8M (center, not floor)
Step 2  M3 (foregone-fishery option value): admitted, deliberately NOT entered
          ("bond only the unassailable floor")                                    [Open, by design]
Step 3  VALUE (CSD) = $20-37M floor / ~$211M central  ->  a LOWER BOUND
Step 4  M2 reads B1-hat = MD $93.52M + VA $21.77M = $115.29M itemized (>$92M MD)  [Filled]
          funders 100% public (NOAA, USACE, MD DNR, VMRC); industry share = $0
          corroboration: $108M/1,900 ac = $56,842/ac -> inside the Step-1 unit band
          ($13,500 < $57K < $77,000)  ->  appraisal and receipts agree on unit cost
Step 5  GAP, floor basis  : B1-hat ($115M) already EXCEEDS the $20-37M floor — restoration
          is happening; the finding is MIS-ASSIGNMENT (public paid, industry $0)
        GAP, central basis: 210.8 - 115.3 = ~$95.5M unrestituted even crediting every public $""",
     "Schulte 2017 Front. Mar. Sci. 4:127; NOAA per-tributary table (Dec 2024); Great Wicomico "
     "Tributary Plan Sec. 5; MD DNR / Gov. Moore Aug 26 2025; engine Part 4 (exact)"),
    ("FORWARD — RCV of the remaining reef", """
Step 1  M1 (engineer substitute reef function for what further loss would take)   [Cited]
Step 2  M3 (regeneration-function foreclosure — the renewal structure itself)     [Cited]
Step 3  VALUE (RCV): not computed in this volume                                  [Cited]
Step 4  M2 reads B2-hat = sanctuary designations (in-kind forward instrument)     [Cited]
Step 5  GAP: successor computation (TA Sec. 11.12, GATE-2-gated)""",
     "Merges only after a book chapter carries the priced claim")],
    "Formally distinct object: a RENEWABLE commons with its renewal structure extracted (the substrate "
    "the next generation sets on). AREA basis only; the Darling shell-mountain stays narrative.")

case("7. Reparations for Black American descendants of US slavery — STRUCTURAL TEST, not book content", [
    ("REVERSE — the field's own figures in the framework's slots", """
Step 1  M1 (cost-to-cure) = per-person remedy x eligible population               [Filled, field's own]
                          = ~$350,000 x ~40,000,000 = ~$14.0T
          basis: 2019 SCF mean Black-white household wealth gap $840,900
          trajectory: 1st ed (2016 SCF) $267K x 40M = $10.7T -> 2nd ed $14.0T
          (an unpaid CSD accrues as the gap compounds; B1 delay is not cost-neutral)
Step 2  M3 + the coercion vector: the floor deliberately excludes the coercion vector
          (author's first-person abstention; field flags direct pricing unresolved),
          the longevity gap (Himmelstein et al. 2022), cultural-knowledge severance,
          intergenerational trauma                                                [Open]
Step 3  VALUE (CSD) >= $14.0T  ->  a strict LOWER BOUND (Step-2 slots open)
Step 4  M2 reads B1-hat = federal $0 (no program; H.R. 40 never enacted)
          + municipal pilots O($10M) ~ 0                                          [Zero, paid]
          comparators (the instrument exists for acknowledged harms): Civil Liberties
          Act 1988 ~ $20K x ~82K internees ~ $1.6B [verify]; Black Lung ~$44B
          ->  $0 here is an acknowledgment gap, not an affordability gap
Step 5  GAP = 14.0T - ~0  >=  $14.0T""",
     "Darity & Mullen, From Here to Equality 2nd ed. (UNC Press 2022); Darity-Mullen-Slaughter, "
     "J. Econ. Perspectives 36(2) 2022 (verified 2026-06-10); public record for B1"),
    ("FORWARD — ongoing-harm streams", """
Step 1  M1 (cure-cost of ongoing-harm streams)                                    [Cited]
Step 2  M3 (option value of what continuing harm forecloses)                      [Cited]
Step 3  VALUE (RCV): outside current scope                                        [Cited]
Step 4  M2 reads B2-hat: no forward instrument exists                             [Open]
Step 5  GAP: not computable until Steps 1-3 are entered""", None)],
    "Same five steps as the reef; one structural difference made visible: reef B1 = large but MIS-ASSIGNED; "
    "reparations B1 = ABSENT. No framework-generated dollar figure appears — every number is the field's own.")

case("8. Asteroid iron, pre-extraction (the zero-anchor)", [
    ("FORWARD — RCV per unit", """
Step 1  M1 ~ market price: the substitute for one asteroid is the next asteroid
        (substitutability across asteroids ~ 1)                                   [Filled, by abundance]
Step 2  M3 = market x (1 + ln(1+(1..10)) x 0.05 = 1.03-1.12) x (1/(1-(0.05..0.2)) = 1.05-1.25)
           = ~1.1-1.4x market                                                     [Filled]
        compare 1 vs 2: both land at ~market  ->  appraisal trusted
Step 3  VALUE (RCV) ~ market price (CIT abundance: both weights ~ 1)
Step 4  M2 reads B2-hat: regime design question — nothing posted yet              [Cited]
Step 5  GAP ~ the small premium only (~0.1-0.4x market)""",
     "TA Sec. 11.8 asteroid calibration; Sec. 10.5 Corollary (lowest-RCV-first sequencing)"),
    ("REVERSE — CSD", """
Step 1  M1: nothing extracted yet — no realized loss to cure                      [Zero]
Step 2  M3: no optionality extinguished yet                                       [Zero]
Step 3  VALUE (CSD) ~ 0
Step 4  M2 reads B1-hat: nothing owed, nothing paid                               [Zero]
Step 5  GAP ~ 0 — the identity assembles trivially, which is the point""", None)],
    "That the framework prices abundance at ~market — no premium — is the calibration check.")

case("9. Closed-world habitat — ISS anchor (the CIT demonstration)", [
    ("FORWARD — what Earth's free commons cost to engineer", """
Step 1  M1 unit anchor: water up-mass ~$21,000/kg (why ECLSS exists: ~90% recovery;
        93 -> >98% loop closure)                                                  [Filled, parked]
        program scale: ~$150B all-partner build (~2010); US-only ~$75B through 2013 (a SUBSET);
        ~$3.1B/yr NASA ops
        scope contrast: $3.1B/yr / ~7 crew ~ $440M/person-yr ALL-IN program
        vs TA Sec. 6.2 ~$1M-10M/person-yr life-support-only — never conflate
Step 2  M3: planetary-scale atmosphere loss -> alpha -> 1 -> Sec. 12 boundary + ARR [Cited]
Step 3  VALUE (RCV) = the engineered-substitute cost band (M1-led)
Step 4  M2 reads B2-hat ~ 0 — no off-world commons bond posted                    [Zero, posted]
Step 5  GAP = the entire engineered cost is unbonded""",
     "Parked candidates, bib Sec. 23.2 — re-verify vs NASA OIG (IG-18-021, IG-22-005) [verify]"),
    ("REVERSE — CSD", """
Step 1  M1: no commons severed — the habitat IMPORTS its commons                  [Zero]
Step 2  M3: nothing extinguished                                                  [Zero]
Step 3  VALUE (CSD) ~ 0
Step 4  M2 reads B1-hat: not applicable — nothing owed                            [Zero]
Step 5  GAP ~ 0""", None)],
    "The cleanest Commons Inversion Test on record: strip abundance and the same commons function "
    "acquires a documented price.")

case("10. NFL concussions (information-asymmetry case-class; both directions)", [
    ("REVERSE — CSD for the pre-disclosure cohort", """
Step 1  M1 (care + career-shortening cure-costs)                                  [Cited]
Step 2  M3 (option value of foreclosed careers/health)                            [Open]
Step 3  VALUE (CSD): per-head lower bound as heads are entered
Step 4  M2 reads B1-hat ~ $1B+ uncapped settlement, industry-paid,
        litigation-forced [verify]                                                [Filled]
Step 5  GAP: per-head vs the settlement's coverage classes""",
     "Public record; framework case-class per Ch 5 lineage"),
    ("FORWARD — RCV for current players (post-2013 disclosure)", """
Step 1  M1 (medical care + career-transition replacement cost)                    [Cited]
Step 2  M3 (option value of career/health optionality at risk)                    [Cited]
Step 2v wage premium on DISCLOSED risk = revealed valuation
        (method worked in case 11; no sourced NFL premium entered here)           [Available]
Step 3  VALUE (RCV): not computed in this volume                                  [Cited]
Step 4  M2 reads B2-hat = CBA health funds + settlement-funded monitoring         [Filled, cited]
Step 5  GAP: not computable until Steps 1-3 are entered""",
     "TA Sec. 3.4 note (ratified 2026-06-10)")],
    "Pre-2013, concealment suppressed the wage premium — case 11's asymmetry measurement applies. "
    "Post-2013 severance moves from unknowing to priced-risk.")

case("11. Offshore oil rig — the hedonic/VSL estimator demonstrated (Step 2v worked)", [
    ("FORWARD — with the valuation estimator written out (ILLUSTRATIVE parameters, labeled)", """
Step 1  M1 (safety-engineering substitute: what eliminating the risk would cost)  [Cited]
Step 2  M3 (option value of the worker's health/career optionality at risk)       [Cited]
Step 2v VALUATION estimator (Rosen 1974 hedonic wages; Viscusi 1993 VSL):         [Filled, illustrative]
          VSL = delta-wage / delta-risk
          textbook line: delta-wage = $1,000/yr for delta-risk = 1/10,000 fatality/yr
          VSL = 1,000 / 0.0001 = $10M   [US regulatory practice ~$10-13M (2020s) [verify]]
          risk-priced premium per worker-year = VSL x delta-risk (= the $1,000)
        column discipline: hazard pay = what workers REVEAL the risk is worth (THIS step);
          insurance / bonds / settlement funds = what the operator POSTED (Step 4)
Step 3  VALUE (RCV, human-risk component) ~ the Step-2v reading where 1 and 2
        are not entered  ->  single-appraiser LOWER BOUND
Step 4  M2 reads B2-hat = operator postings per worker (insurance, bonds)         [Cited]
Step 5  GAP demo: if (VSL x delta-risk) per worker-yr > operator posting per worker-yr,
        the difference is severance priced into wages but never bonded""",
     "Method: Rosen 1974 JPE 82(1); Viscusi 1993 JEL 31(4) — TA Sec. 3.4 note (construct, not "
     "calibration). Parameters illustrative; a real application needs a sourced premium study [verify]"),
    ("REVERSE — CSD for realized harms", """
Step 1  M1 (realized injury/fatality cure-and-compensation costs)                 [Cited]
Step 2  M3 (option value extinguished for the harmed cohort)                      [Open]
Step 3  VALUE (CSD): per-head lower bound as heads are entered
Step 4  M2 reads B1-hat = workers' comp + settlements actually paid               [Cited]
Step 5  GAP: per-head vs what was actually paid, and BY WHOM""", None)],
    "Why this estimator earns its place: (1) the only appraiser built from the cost-bearer's own "
    "behavior — M1 prices engineering, M3 optionality, M2 receipts; none reads what the risk-bearer "
    "priced it at; (2) labor-market cases gain a third appraiser and a tighter Step-3 overlap; "
    "(3) its divergence from the informed baseline measures information asymmetry in dollars (below); "
    "(4) mainstream welfare economics (Rosen/Viscusi) — inside the literature, not beside it. "
    "Kept strictly in the valuation column: never plugged into M2.",
    extra=("THE ASYMMETRY MEASUREMENT (what Step 2v uniquely adds)", """
A worker cannot charge for risk they do not know about. Under concealment:
  revealed premium  =  VSL x (risk as KNOWN to the worker)
  informed premium  =  VSL x (risk as it ACTUALLY was)
  informed - revealed  =  VSL x (concealed risk)   <-- the information asymmetry, IN DOLLARS
This turns "the severance the cost-bearer bore unknowingly" (NFL pre-2013; Libby's 27 years;
the apartment signed after a midnight test-drive) from a narrative claim into a computable quantity.""",
           None))

case("12. Apartment lease — the commute trade (n-of-1 self-severance; no bad actor)", [
    ("FORWARD — at signing (v = your revealed-preference hourly value; the input slot)", """
Step 1  M1 (engineer the substitute: the close-in apartment's rent premium —
        the observable exists; no number entered here)                            [Available]
Step 2  M3 (time-value appraisal) = 1,800 hrs/yr foreclosed x v $/hr = 1,800v $/yr [Filled, in v]
        compare 1 vs 2: when both are entered, the rent premium cross-checks 1,800v
Step 3  VALUE (RCV) = 1,800v  ->  single-appraiser LOWER BOUND until Step 1 is entered
Step 4  M2 reads B2-hat = 0 — no instrument exists                                [Zero]
Step 5  GAP: CS_forward = 1,800v - 0 = 1,800v — the severance is the whole foreclosure""",
     "TA Sec. 6.7 Walkthrough 2 (all four gates PASS; Gate 2 dollar-conversion via revealed preference)"),
    ("REVERSE — after the year", """
Step 1  M1 = the same 1,800v, realized (the hours are gone; v now known with certainty) [Filled, in v]
Step 2  M3: no further optionality at issue for a completed lease year            [Zero]
Step 3  VALUE (CSD) = 1,800v realized
Step 4  M2 reads B1-hat = 0                                                       [Zero]
Step 5  GAP = 1,800v
        case-11 note: the midnight test-drive = self-inflicted information asymmetry —
        the 'premium' you charged yourself was priced on the risk as known, not as it was""", None)],
    "Value-capturer = cost-bearer; no extractor. The apparatus runs identically at n-of-1 — an "
    "accounting framework, not a theory of villains.")

A(Spacer(1, 8))
A(Paragraph("Provenance + regeneration", h2))
A(Paragraph(
    "Computed values reproduce in core/technical-appendix/calculations/csd_rcv_calculations.py "
    "(run-output_2026-06-10.txt: 21/21 reproduction checks PASS; 11/11 portfolio cases assemble the "
    "identity with all slots in legal states). TA references are to TechnicalAppendix_v2.0.0.html as "
    "merged 2026-06-10. Case 11's Step-2v parameters are illustrative method demonstrations, not "
    "sourced figures. Sec. 11.12 (reef) merges to the TA only after a book chapter carries the priced "
    "claim (GATE 2). Regenerate with gen_use_cases_pdf.py after any figure cascade.", small))

# ----- HARD INVARIANT: all five steps present in every direction block -----
errors = []
for title, label, text in direction_blocks:
    for n in (1, 2, 3, 4, 5):
        if f"Step {n}" not in text:
            errors.append(f"{title} / {label}: missing Step {n}")
assert len(direction_blocks) == 24, f"expected 24 direction blocks, got {len(direction_blocks)}"
assert not errors, "FIVE-STEP INVARIANT VIOLATED:\n" + "\n".join(errors)
print(f"five-step invariant: {len(direction_blocks)} direction blocks x Steps 1-5 all present")

doc = SimpleDocTemplate(OUT, pagesize=letter,
                        leftMargin=0.65 * inch, rightMargin=0.65 * inch,
                        topMargin=0.65 * inch, bottomMargin=0.65 * inch,
                        title="Commons Bonds - Bidirectional Use-Case Worksheets v4 (2026-06-10)",
                        author="Commons Bonds working session")
doc.build(story)
print("wrote", OUT)
