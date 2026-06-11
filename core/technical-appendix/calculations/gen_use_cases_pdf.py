#!/usr/bin/env python3
"""
Generate the bidirectional use-case worksheet PDF (forward RCV + reverse CSD).

v3 format (2026-06-10, author feedback):
  * Uniform FIVE-STEP RECIPE on every worksheet: two appraisals (M1, M3) ->
    overlap = VALUE -> M2 reads the receipts -> ONE subtraction = the gap.
    M1 and M3 are never subtracted from each other.
  * Appraisers/receipts analogy on page 1.
  * Step "2v": the hedonic/VSL revealed-VALUATION estimator (Rosen 1974;
    Viscusi 1993) demonstrated on a worked offshore-rig case (case 11),
    with the why-it-is-useful box.

Companion to csd_rcv_calculations.py — computed numbers trace to its verified
output (21/21 checks PASS) or the merged TA v2.0.0 (main @ 2026-06-10).
Regenerate: /tmp/pdfenv/bin/python gen_use_cases_pdf.py

Font discipline (reportlab base-14): no raw Greek / Unicode sub-superscripts.
In calculation lines B1/B2/M1/M2/M3/t0 are written without subscripts; Greek
is spelled (alpha, sigma-f = the TA's final-sigma).
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
box = ParagraphStyle("boxx", parent=body, backColor=colors.HexColor("#eef3e8"),
                     borderPadding=6, borderWidth=0.5,
                     borderColor=colors.HexColor("#8aa86e"))

story = []
A = story.append


def case(title, blocks, note=None):
    A(Paragraph(title, h2))
    for label, text, src in blocks:
        if label:
            A(Paragraph("<b>" + label + "</b>", body))
        A(Preformatted(text.strip("\n"), calc))
        if src:
            A(Paragraph("Source: " + src, small))
    if note:
        A(Paragraph("<b>Note.</b> " + note, small))
    A(Spacer(1, 7))


A(Paragraph("Commons Bonds — Bidirectional Use-Case Worksheets (v3: the five-step recipe)", h1))
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

A(Paragraph("The recipe (every worksheet, every direction, same five steps)", h2))
A(Preformatted("""
  Step 1   M1 = FIRST APPRAISAL    forward: engineer-a-substitute cost  |  reverse: cost-to-cure
  Step 2   M3 = SECOND APPRAISAL   option value, both directions:
              value_M3 = V_market x scarcity_mult(sigma-f) x irrev_premium(alpha)
              scarcity_mult = 1 + ln(1+sigma-f) x 0.05        irrev_premium = 1 / (1 - alpha)
              (reverse: V_market = extinguished optionality / foregone service flow;
               sigma-f at extraction; alpha observed; ex-post vs ex-ante fork exposed)
           >> COMPARE Step 1 with Step 2 — NEVER subtract them. Their overlap is the result;
              their divergence is a diagnostic (which feature one appraiser cannot see).
  Step 2v  (where a behavioral observable exists) VALUATION ESTIMATOR from the cost-bearer's
           own behavior — hedonic / value-of-statistical-life (Rosen 1974; Viscusi 1993):
              VSL = delta-wage / delta-risk     (a third appraiser; see case 11)
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

  SLOT STATES: Zero (abundance; CIT toggle) =/= Filled (number entered, work shown)
               =/= Open (admitted, deliberately empty -> total is a LOWER BOUND)
               Cited = named by the TA, not computed in this volume.
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
           = $812-1,658/ton at-scale (center ~$1,235); full DAC-horizon range $290-2,702
Step 2  M3 : low  40 x 1.27 x 1/(1-0.85)= 6.67  -> $339/ton
            high 140 x 1.31 x 1/(1-0.95)= 20    -> $3,668/ton
            geometric center sqrt(339 x 3668) ~ $1,115/ton
        compare: centers $1,235 vs $1,115 agree to ~10%  ->  appraisal trusted
Step 3  VALUE (RCV) = overlap ~$340-2,700/ton; center ~$1,000-1,500 (worked at $1,115)
Step 4  M2 reads realized B = $50-88/ton societally paid ($8-15 industry-paid)
Step 5  GAP: CS_forward = 1,115 - (50..88) = $1,027-1,065/ton
        IPG: 339/40 = 8.5x .. 3668/140 = 26.2x (center ~15x); integral lens 67-134x""",
     "TA Sec. 11.6; Sec. 3.3 DAC bands; engine Parts 1-2 (exact reproductions)"),
    ("REVERSE — CSD heads", """
Step 1  M1 heads: reclamation shortfall $3.7-6B documented; life-expectancy gap, community
        collapse, knowledge loss: Cited/Open
Step 2  M3: Open                       Step 3  VALUE: lower-bound, per-head basis
Step 4  M2 reads B1-hat = Black Lung ~$44B through 2009 (restitution-type)
Step 5  GAP computable per documented head (e.g. reclamation shortfall vs $0 industry posting)""",
     "TA Sec. 11.1; GAO/CRS via Sec. 11.6")],
    "Bidirectional finding: the TA's 'realized B ~$53-60B' needs a B1/B2 split — Black Lung payouts are B1 "
    "(restitution); reclamation bonds are B2 (posted forward). Flagged for Sec. 11.6.")

case("2. Norway petroleum (forward exemplar; backward quantified illustratively)", [
    ("FORWARD — RCV per BOE", """
Step 1  M1 = $161-422/BOE (DAC-anchored replacement floor)
Step 2  M3 = 80 x (1 + ln(101)x0.05 = 1.2308) x (1/(1-0.65) = 2.857) = $281/BOE central
            corners: 40 x 1.1966 x 2.0 = $96   |   120 x 1.2651 x 4.0 = $607
        compare: $281 sits inside M1's $161-422  ->  appraisal trusted
Step 3  VALUE (RCV) ~ $281/BOE center
Step 4  M2 reads B2-hat = GPFG $2.0T / 0.75 capture / 55e9 BOE = $48.5/BOE
Step 5  GAP: CS_forward = 281 - 48.5 = $233/BOE;  x 55B BOE cumulative = ~$12.8T""",
     "TA Sec. 11.5 (NBIM NOK 21,268B; Norwegian Offshore Directorate); engine Parts 1-2"),
    ("REVERSE — illustrative (labeled)", """
Step 1  CSD ~ 20.35 Gt CO2 combusted x $190/t (EPA SCC) ~ $3.9T   [SCC-basis assumption]
Step 2  M3: not entered          Step 3  VALUE ~ $3.9T (single-appraiser lower bound)
Step 4  M2 reads B1-hat ~ 0 for non-Norwegian cost-bearers (welfare state = B1-for-Norwegians)
Step 5  GAP ~ $3.9T borne outside the GPFG's coverage""",
     "Emissions TA Sec. 11.5 (sourced); EPA 2023 SCC")],
    "Norway's architecture lowers effective alpha to 0.50-0.75 — it attacks the foreclosure premium itself; "
    "the backward run shows whom it does not cover.")

case("3. Deepwater Horizon (backward-dominant; the industry-paid-B1 exemplar)", [
    ("REVERSE — CSD, total dollars", """
Step 1  documented CSD = $61.6B all-in (BP 2016; $65B+ by 2018) + $8-12B ongoing ecosystem
                       = ~$69.6-73.6B
Step 2  M3: not separately entered     Step 3  VALUE = $69.6-73.6B (lower bound)
Step 4  M2 reads B1-hat = $61.6B — INDUSTRY-paid (litigation-forced): the corpus's largest
Step 5  GAP = (69.6..73.6) - 61.6 = ~$8-12B (ongoing externalities beyond BP's charges)
checks: IPG ~ 61.6/4.0 = 15.4x documented; (61.6+8..12)/4.0 = 17-18x with ongoing""",
     "TA Sec. 11.2 (settlement components; revenue = labeled framework estimate ~50M bbl x $80)"),
    ("FORWARD", """
Steps 1-3 (remaining-well class): Cited     Step 4: decommissioning bonds (BSEE/BLM), Cited""", None)],
    "Contrast set: reef B1 = public-paid; reparations B1 = absent; Deepwater B1 = industry-paid post-hoc. "
    "The instrument exists at every assignment.")

case("4. Libby, Montana vermiculite (backward-dominant; mixed-assignment B1)", [
    ("REVERSE — component arithmetic written out (which is what exposes the gap)", """
Step 1  CSD components: $600M+ Superfund + $250M+ settlements + $50M+/yr medical + $500M+ property
        component sum ~ $1.35B + medical accrual (~50M x ~26 yrs ~ $1.3B) ~ $2.7B
        stated TA total "$4B+ (40:1)" NOT reachable from listed components -> provenance pass owns it
Step 2  M3: Open       Step 3  VALUE >= $1.35B documented (conservative floor)
Step 4  M2 reads B1-hat = $600M public (Superfund) + $250M industry  ->  ~70/30 public/industry
Step 5  GAP >= 1.35B - 0.85B = $0.5B+ on components alone; ratio check 1.35B/$100M revenue >= 13.5x""",
     "TA Sec. 11.3; component-sum + ratio checks are this worksheet's own arithmetic, shown so the "
     "shortfall is visible. IPG triplet (55-82x/48-76x/61-91x): no work shown — queued [verify]"),
    ("FORWARD", """
Steps 1-5 ~ Zero (mine closed 1990; no forward instrument needed)""", None)],
    "Epistemic-commons case: 27-year concealment held B ~ 0 while costs accrued. See case 11's "
    "asymmetry-measurement note — concealment also suppressed the workers' wage premium.")

case("5. Baotou rare earths (both directions live and large simultaneously)", [
    ("REVERSE", """
Step 1  CSD: tailings-lake remediation $5-15B (cited); health/agric/relocation heads Cited
Step 2  M3: Open       Step 3  VALUE >= $5-15B (lower bound)
Step 4  M2 reads B1-hat ~ 0 identified
Step 5  GAP >= $5-15B;  scale check: remediation / annual export revenue = (5..15)/(2..4)
        = 1.3x-7.5x of a full year's export revenue  [illustrative, not the TA's IPG]""",
     "TA Sec. 11.4. IPG triplet (12-35x/18-48x/22-41x): denominator unstated — queued [verify]"),
    ("FORWARD", """
Step 2  M3: ongoing extraction, high-sigma-f REE register     Step 4  B2-hat ~ 0
Step 5  GAP = the forward premium, ongoing — both directions live at once""",
     "TA Sec. 11.4 / 11.8")],
    "Forward-only accounting misses half this case: total CS needs BOTH (CSD - B1) and (RCV - B2).")

case("6. Chesapeake oyster reef (the worked REVERSE case; Restitution Bond design)", [
    ("REVERSE — the five steps end-to-end", """
Step 1  M1 (cost-to-cure) = foreclosed extent x realized restoration unit-cost
          realized basis : 2,738 ac x ($907,000/124 ac = $7,314/ac)  = $20.0M
          headline basis : 2,738 ac x $13,500/ac construction-only   = $37.0M
          robust central : 2,738 ac x $77,000/ac bay-wide average    = $210.8M (center, not floor)
Step 2  M3 (foregone-fishery option value): OPEN BY DESIGN — admitted, deliberately not entered
          ("bond only the unassailable floor")
Step 3  VALUE (CSD) = $20-37M floor / ~$211M central  ->  a LOWER BOUND (Step-2 slot open)
Step 4  M2 reads B1-hat = MD $93.52M + VA $21.77M = $115.29M itemized (>$92M MD alone)
          funders 100% public (NOAA, USACE, MD DNR, VMRC); industry share = $0
          corroboration: $108M/1,900 ac = $56,842/ac -> inside the Step-1 unit-cost band
          ($13,500 < $57K < $77,000)  ->  the appraisal and the receipts agree on unit cost
Step 5  GAP, floor basis  : B1-hat ($115M) already EXCEEDS the $20-37M floor — restoration is
          happening; the finding is MIS-ASSIGNMENT (public paid, extractive industry $0)
        GAP, central basis: 210.8 - 115.3 = ~$95.5M unrestituted even crediting every public $""",
     "Schulte 2017 Front. Mar. Sci. 4:127; NOAA per-tributary table (Dec 2024); Great Wicomico "
     "Tributary Plan Sec. 5; MD DNR / Gov. Moore Aug 26 2025; engine Part 4 (exact)"),
    ("FORWARD", """
Steps 1-3 (remaining-reef regeneration-function foreclosure): Cited    Step 4: sanctuaries, Cited""",
     "Successor session: TA Sec. 11.12, GATE-2-gated (merges only after a book chapter prices the claim)")],
    "Formally distinct object: a RENEWABLE commons with its renewal structure extracted (the substrate the "
    "next generation sets on). AREA basis only; the Darling shell-mountain stays narrative.")

case("7. Reparations for Black American descendants of US slavery — STRUCTURAL TEST, not book content", [
    ("REVERSE — the field's own figures in the framework's slots", """
Step 1  M1 (cost-to-cure) = per-person remedy x eligible population   [field's published figure]
                          = ~$350,000 x ~40,000,000 = ~$14.0T
          basis: 2019 SCF mean Black-white household wealth gap $840,900
          trajectory: 1st ed (2016 SCF) $267K x 40M = $10.7T -> 2nd ed $14.0T
          (an unpaid CSD accrues as the gap compounds; B1 delay is not cost-neutral)
Step 2  M3 + coercion vector: OPEN — floor deliberately excludes the coercion vector (author's
          first-person abstention; field flags direct pricing unresolved), longevity gap
          (Himmelstein et al. 2022), cultural-knowledge severance, intergenerational trauma
Step 3  VALUE (CSD) >= $14.0T — a strict LOWER BOUND (Step-2 slots open)
Step 4  M2 reads B1-hat = federal $0 (no program; H.R. 40 never enacted) + pilots O($10M) ~ 0
          comparators (the instrument exists for acknowledged harms):
          Civil Liberties Act 1988 ~ $20K x ~82K internees ~ $1.6B [verify]; Black Lung ~$44B
          ->  $0 here is an acknowledgment gap, not an affordability gap
Step 5  GAP = 14.0T - ~0  >=  $14.0T""",
     "Darity & Mullen, From Here to Equality 2nd ed. (UNC Press 2022); Darity-Mullen-Slaughter, "
     "J. Econ. Perspectives 36(2) 2022 (verified 2026-06-10); public record for B1"),
    ("FORWARD", """
Steps 1-3: ongoing-harm streams, Cited (outside current scope)    Step 4: no instrument (Open)""", None)],
    "Same five steps as the reef; one structural difference made visible: reef B1 = large but MIS-ASSIGNED; "
    "reparations B1 = ABSENT. No framework-generated dollar figure appears — every number is the field's own.")

case("8. Asteroid iron, pre-extraction (the zero-anchor)", [
    ("FORWARD", """
Step 2  M3 = market x (1 + ln(1+(1..10)) x 0.05 = 1.03-1.12) x (1/(1-(0.05..0.2)) = 1.05-1.25)
           = ~1.1-1.4x market  ->  Step 3  VALUE ~ market (CIT abundance: both weights ~ 1)
Step 4  B2-hat: regime design question (Cited)        Step 5  GAP ~ the small premium only""",
     "TA Sec. 11.8; Sec. 10.5 Corollary (lowest-RCV-first sequencing)"),
    ("REVERSE", """
Steps 1-5 ~ 0 (nothing realized yet) — the identity assembles trivially, which is the point""", None)],
    "That the framework prices abundance at ~market — no premium — is the calibration check.")

case("9. Closed-world habitat — ISS anchor (the CIT demonstration)", [
    ("FORWARD — Step 1 written out (what Earth's free commons cost to engineer)", """
Step 1  M1 unit anchor: water up-mass ~$21,000/kg (why ECLSS exists: ~90% recovery; 93->98%+)
        program scale: ~$150B all-partner build (~2010); US-only ~$75B through 2013 (a SUBSET);
        ~$3.1B/yr NASA ops
        scope contrast: $3.1B/yr / ~7 crew ~ $440M/person-yr ALL-IN program
        vs TA Sec. 6.2 ~$1M-10M/person-yr life-support-only — different scopes; never conflate
Step 2  M3: planetary-scale atmosphere loss -> alpha -> 1 -> Sec. 12 boundary + ARR
Step 3  VALUE: the engineered-substitute cost band       Step 4  B2-hat ~ 0 (nothing posted)
Step 5  GAP = the entire engineered cost is unbonded""",
     "Parked candidates, bib Sec. 23.2 — re-verify vs NASA OIG (IG-18-021, IG-22-005) [verify]"),
    ("REVERSE", """
Steps 1-5 ~ 0 (the habitat IMPORTS its commons; nothing severed)""", None)],
    "The cleanest Commons Inversion Test on record: strip abundance and the same commons function "
    "acquires a documented price.")

case("10. NFL concussions (information-asymmetry case-class; both directions)", [
    ("REVERSE", """
Step 1  CSD: career-shortening + CTE-class health costs (Cited; heads Open)
Step 4  M2 reads B1-hat ~ $1B+ uncapped settlement, industry-paid, litigation-forced [verify]
Step 5  GAP: per-head vs the settlement's coverage classes""",
     "Public record; framework case-class per Ch 5 lineage"),
    ("FORWARD", """
Step 2v VALUATION estimator AVAILABLE: post-2013 wage premium on disclosed risk = revealed
        valuation (see case 11 for the method) — no sourced premium entered here
Step 4  M2 reads B2-hat: CBA health funds + settlement-funded monitoring (Filled, cited)""",
     "TA Sec. 3.4 note (ratified 2026-06-10)")],
    "Pre-2013, concealment suppressed the wage premium — see case 11: the informed-VSL gap "
    "MEASURES that asymmetry. Post-2013 severance moves from unknowing to priced-risk.")

case("11. Offshore oil rig — the hedonic/VSL estimator demonstrated (Step 2v worked)", [
    ("FORWARD — the valuation estimator, written out (ILLUSTRATIVE parameters, labeled)", """
THE METHOD (Rosen 1974 hedonic wages; Viscusi 1993 VSL):
  VSL = delta-wage / delta-risk     (what workers charge to accept a unit of fatality risk)
ILLUSTRATIVE WORKED LINE (textbook parameters, not a sourced rig study):
  a job paying delta-wage = $1,000/yr more for delta-risk = 1/10,000 higher annual fatality risk
  VSL = 1,000 / 0.0001 = $10M    [US regulatory practice uses ~$10-13M (2020s) [verify]]
WHERE IT PLUGS IN:
  Step 2v: a THIRD appraiser for the human-risk component of RCV — from the cost-bearer's
  OWN behavior (wages accepted), independent of M1 (engineering cost) and M3 (option value)
  risk-priced premium per worker-year = VSL x delta-risk  (= the $1,000 above)
WHY IT IS NOT M2 (the column discipline):
  hazard pay  = what workers REVEAL the risk is worth   -> VALUATION column (Step 2v)
  insurance / decommissioning bonds / settlement funds = what the operator POSTED -> Step 4
Step 5  GAP demo: if (VSL x delta-risk) per worker-year > operator's per-worker posting,
        the difference is severance priced into wages but never bonded""",
     "Method: Rosen 1974 JPE 82(1); Viscusi 1993 JEL 31(4) — TA Sec. 3.4 note (construct, not "
     "calibration). Parameters here are illustrative; a real rig application needs a sourced "
     "premium study [verify before any external use]"),
    ("THE ASYMMETRY MEASUREMENT (what this estimator uniquely adds)", """
A worker cannot charge for risk they do not know about. Under concealment:
  revealed premium  =  VSL x (risk as KNOWN to the worker)
  informed premium  =  VSL x (risk as it ACTUALLY was)
  informed - revealed  =  VSL x (concealed risk)   <-- the information asymmetry, IN DOLLARS
This turns "the severance the cost-bearer bore unknowingly" (NFL pre-2013; Libby's 27 years;
the apartment signed at midnight) from a narrative claim into a computable quantity.""", None)],
    "Why this estimator earns its place: (1) it is the only appraiser built from the cost-bearer's own "
    "behavior — M1 prices the engineering, M3 the optionality, M2 the receipts; none reads what the "
    "person bearing the risk priced it at; (2) it gives labor-market cases (rigs, NFL, mining) a third "
    "appraiser and a tighter Step-3 overlap; (3) its divergence from the informed baseline measures "
    "information asymmetry — the framework's core case-class — in dollars; (4) it is mainstream welfare "
    "economics (Rosen/Viscusi), positioning the framework inside the literature, not beside it. "
    "Kept strictly in the valuation column: never plugged into M2.")

case("12. Apartment lease — the commute trade (n-of-1 self-severance; no bad actor)", [
    ("FORWARD — at signing (v = your revealed-preference hourly value; the input slot)", """
Step 1/2  appraisal = 1,800 hrs/yr foreclosed x v $/hr = 1,800v $/yr   [Gate 2: dollar-convertible]
Step 3    VALUE (RCV) = 1,800v
Step 4    M2 reads B2-hat = 0 (no instrument exists)
Step 5    GAP: CS_forward = 1,800v - 0 = 1,800v — the severance is the whole foreclosure""",
     "TA Sec. 6.7 Walkthrough 2 (all four gates PASS)"),
    ("REVERSE — after the year", """
Steps 1-5: the same 1,800v, realized; B1-hat = 0; GAP = 1,800v
case-11 note: midnight test-drive = self-inflicted information asymmetry — the 'premium' you
charged yourself for the commute was priced on the risk as known, not as it actually was""", None)],
    "Value-capturer = cost-bearer; no extractor. The apparatus runs identically at n-of-1 — an "
    "accounting framework, not a theory of villains.")

A(Spacer(1, 8))
A(Paragraph("Provenance + regeneration", h2))
A(Paragraph(
    "Computed values reproduce in core/technical-appendix/calculations/csd_rcv_calculations.py "
    "(run-output_2026-06-10.txt: 21/21 reproduction checks PASS; 11/11 portfolio cases assemble the "
    "identity with all slots in legal states). TA references are to TechnicalAppendix_v2.0.0.html as "
    "merged 2026-06-10. Case 12's parameters are illustrative method demonstrations, not sourced "
    "figures. Sec. 11.12 (reef) merges to the TA only after a book chapter carries the priced claim "
    "(GATE 2). Regenerate with gen_use_cases_pdf.py after any figure cascade.", small))

doc = SimpleDocTemplate(OUT, pagesize=letter,
                        leftMargin=0.65 * inch, rightMargin=0.65 * inch,
                        topMargin=0.65 * inch, bottomMargin=0.65 * inch,
                        title="Commons Bonds - Bidirectional Use-Case Worksheets v3 (2026-06-10)",
                        author="Commons Bonds working session")
doc.build(story)
print("wrote", OUT)
