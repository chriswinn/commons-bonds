#!/usr/bin/env python3
"""
Generate the bidirectional use-case worksheet PDF (forward RCV + reverse CSD).
v2 format (2026-06-10, author feedback): worked-calculation blocks — formula,
inputs, arithmetic, result — instead of slot-state tables. Role equations up
front: M1 -> RCV_floor (fwd) | CSD_floor (rev); M3 -> option value both
directions; M2 reads B2-hat (fwd) + B1-hat (rev); CS = (M1 ^ M3) - M2 reading.

Companion to csd_rcv_calculations.py — computed numbers trace to its verified
output (21/21 checks PASS) or the merged TA v2.0.0 (main @ 2026-06-10).
Regenerate: /tmp/pdfenv/bin/python gen_use_cases_pdf.py

Font discipline (reportlab base-14): no raw Greek / Unicode sub-superscripts.
In calculation lines B1/B2/M1/M2/M3/t0 are written without subscripts; Greek
is spelled (alpha, sigma-f).
"""
from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch
from reportlab.lib import colors
from reportlab.platypus import (SimpleDocTemplate, Paragraph, Spacer,
                                PageBreak, Preformatted, KeepTogether, Table,
                                TableStyle)

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
                      fontSize=7.6, leading=9.6, leftIndent=10,
                      backColor=colors.HexColor("#f4f6f8"),
                      borderPadding=4, spaceBefore=2, spaceAfter=2)

story = []
A = story.append


def case(title, blocks, note=None):
    """blocks = list of (label, multiline-calc-text, source-line-or-None)."""
    els = [Paragraph(title, h2)]
    for label, text, src in blocks:
        if label:
            els.append(Paragraph("<b>" + label + "</b>", body))
        els.append(Preformatted(text.strip("\n"), calc))
        if src:
            els.append(Paragraph("Source: " + src, small))
    if note:
        els.append(Paragraph("<b>Note.</b> " + note, small))
    els.append(Spacer(1, 7))
    story.extend(els)


A(Paragraph("Commons Bonds — Bidirectional Use-Case Worksheets (v2: worked calculations)", h1))
A(Paragraph("Forward RCV and Reverse CSD across the full case portfolio (2026-06-10)", S["Heading3"]))
A(Spacer(1, 4))
A(Paragraph(
    "<b>INTERNAL WORKING DOCUMENT — author-facing.</b> Not publisher-facing prose. The Reparations "
    "worksheet is a structural capability test built entirely from the reparations field's published "
    "figures (candidate share with Prof. Darity); the coercion vector remains an Open slot throughout, "
    "per the author's first-person abstention. Figures marked [verify] need re-verification before any "
    "external use. Subscripts are omitted in calculation lines (B1, B2, t0); Greek is spelled "
    "(alpha, sigma-f = the TA's final-sigma).", banner))
A(Spacer(1, 8))

A(Paragraph("How every worksheet computes (the role equations)", h2))
A(Preformatted("""
ROLES (one line each — what each Way of Counting measures):
  M1  ->  RCV_floor   (forward: engineer-a-substitute cost)   |  CSD_floor (reverse: cost-to-cure)
  M3  ->  RCV option value (forward)                          |  CSD option value (reverse)
          RCV_M3  = V_market x scarcity_mult(sigma-f) x irrev_premium(alpha)
          CSD_M3  = same form, realized parameters: V_market = extinguished optionality /
                    foregone service flow; sigma-f at extraction; alpha observed
                    (ex-post strict-liability vs ex-ante negligence fork: exposed, not settled)
          scarcity_mult(sigma-f) = 1 + ln(1 + sigma-f) x 0.05      irrev_premium(alpha) = 1 / (1 - alpha)
  M2  ->  reads the REALIZED BOND, never a third estimator:
          M2 reads B2-hat (forward: e.g. Norway GPFG)          |  B1-hat (reverse: restitution paid)
          (B2 = Foreclosure Bond, pairs with forward RCV; B1 = Restitution Bond, pairs with reverse CSD)

PER DIRECTION (the gap each worksheet computes):
  CS_forward  =  (M1 ^ M3 convergence on RCV)  -  B2-hat        [^ = the two estimators' overlap]
  CSD_gap     =  (M1 ^ M3 on CSD; M3 often Open) -  B1-hat

IDENTITY (the whole framework in one line):
  total CS  =  (CSD - B1)  +  (RCV - B2)

SLOT STATES:  Zero (abundance: CIT toggle)  =/=  Filled (number entered, work shown)
              =/=  Open (admitted, deliberately empty  ->  computed total is a LOWER BOUND)
              Cited = named by the TA, not computed in this volume.
""", calc))
A(Paragraph(
    "Provenance: computed values reproduce in core/technical-appendix/calculations/"
    "csd_rcv_calculations.py (21/21 checks PASS vs the merged TA); every input names its external "
    "source. TA = TechnicalAppendix_v2.0.0.html, main @ 2026-06-10.", small))
A(PageBreak())

# ----------------------------------------------------------------- cases
case("1. McDowell County coal (forward-dominant; both directions live)", [
    ("FORWARD — RCV per ton", """
M1 (replacement floor):   DAC at-scale $300-600/t-CO2 x 2.61 t-CO2/ton + eco/cohesion floors
                          = $812-1,658/ton (at-scale; center ~$1,235)
                          full DAC-horizon range $290-2,702/ton
M3 (option value):        low : 40  x 1.27 x 1/(1-0.85)= 6.67  ->  $339/ton
                          high: 140 x 1.31 x 1/(1-0.95)= 20    ->  $3,668/ton
                          geometric center = sqrt(339 x 3668)  ~  $1,115/ton
RCV (M1 ^ M3):            overlap ~$340-2,700; centers $1,115 (M3) vs $1,235 (M1) agree to ~10%
M2 reads B2-hat:          realized $50-88/ton societally paid  ($8-15/ton industry-paid)
CS_forward  = 1,115 - (50..88)  =  $1,027-1,065/ton
IPG (premium basis): 339/40 = 8.5x ... 3668/140 = 26.2x (geo center ~15x); integral lens 67-134x""",
     "TA Sec. 11.6 (M1 bands, realized B); Sec. 3.3 DAC; engine Part 1-2 (exact reproductions)"),
    ("REVERSE — CSD heads", """
CSD components:  reclamation shortfall $3.7-6B (documented)  +  13-yr life-expectancy gap,
                 community collapse, knowledge loss (Cited/Open heads)
M2 reads B1-hat: Black Lung Trust Fund ~$44B cumulative through 2009 (restitution-type)""",
     "TA Sec. 11.1; GAO/CRS via Sec. 11.6")],
    "The bidirectional run forces a split the forward-only TA never needed: Black Lung payouts are "
    "B1 (realized-harm restitution); reclamation bonds are B2 (posted against future damage). Flagged for Sec. 11.6.")

case("2. Norway petroleum (forward exemplar; backward quantified illustratively)", [
    ("FORWARD — RCV per BOE", """
M1 (replacement floor):   $161-422/BOE (DAC-anchored)
M3 (option value):        central: 80  x (1 + ln(101)x0.05 = 1.2308) x 1/(1-0.65)= 2.857  -> $281/BOE
                          corners: 40 x 1.1966 x 2.0 = $96   |   120 x 1.2651 x 4.0 = $607
RCV (M1 ^ M3):            ~$281/BOE center (bands overlap)
M2 reads B2-hat:          GPFG $2.0T / 0.75 capture / 55e9 BOE  =  $48.5/BOE
CS_forward  = 281 - 48.5  =  $233/BOE     x 55B BOE cumulative  =  ~$12.8T""",
     "TA Sec. 11.5 (NBIM NOK 21,268B; Norwegian Offshore Directorate 55B BOE); engine Parts 1-2"),
    ("REVERSE — illustrative (labeled)", """
CSD ~ 20.35 Gt CO2 combusted x $190/t-CO2 (EPA SCC)  ~  $3.9T realized damage   [SCC-basis assumption]
M2 reads B1-hat: ~0 for non-Norwegian cost-bearers (welfare state = B1-for-Norwegians only)
CSD_gap ~ $3.9T - 0  =  ~$3.9T borne outside the GPFG's coverage""",
     "Emissions TA Sec. 11.5 (sourced); EPA 2023 SCC; the TA's own qualitative claim, made arithmetic")],
    "Norway's architecture lowers effective alpha to 0.50-0.75 — it attacks the foreclosure premium itself. "
    "The backward run shows whom it does not cover.")

case("3. Deepwater Horizon (backward-dominant; the industry-paid-B1 exemplar)", [
    ("REVERSE — CSD, total dollars", """
CSD        =  $61.6B all-in (BP 2016; $65B+ by 2018)  +  $8-12B ongoing Gulf ecosystem
           =  ~$69.6-73.6B
M2 reads B1-hat:  $61.6B — INDUSTRY-paid (litigation-forced); largest realized B1 in the corpus
CSD_gap    =  (69.6..73.6) - 61.6  =  ~$8-12B (the ongoing externalities beyond BP's charges)
IPG checks =  61.6 / ~4.0 revenue = ~15.4x ;  (61.6 + 8..12) / 4.0 = ~17-18x""",
     "TA Sec. 11.2 (settlement components itemized; revenue = labeled framework estimate ~50M bbl x $80)"),
    ("FORWARD", """
RCV (remaining-well class): Cited, not computed   |   M2 reads B2-hat: decommissioning bonds (BSEE/BLM), Cited""",
     None)],
    "Contrast set: reef B1 = public-paid; reparations B1 = absent; Deepwater B1 = industry-paid post-hoc. "
    "The instrument exists at every assignment.")

case("4. Libby, Montana vermiculite (backward-dominant; mixed-assignment B1)", [
    ("REVERSE — CSD components (written out, which is what exposes the gap)", """
CSD components = $600M+ Superfund + $250M+ settlements + $50M+/yr medical + $500M+ property
component sum  ~ $1.35B  +  medical accrual (50M/yr x ~26 Superfund-era yrs ~ $1.3B)  ~  $2.7B
stated total   = "$4B+ (40:1)"  ->  NOT reachable from the listed components: provenance pass owns it
M2 reads B1-hat: $600M public (Superfund) + $250M industry (settlements)  ->  ~70/30 public/industry
documented-ratio check: $1.35B+ / $100M lifetime revenue  >=  13.5x  (on components alone)""",
     "TA Sec. 11.3; component-sum and ratio checks are this worksheet's arithmetic, shown so the "
     "shortfall is visible. IPG triplet (55-82x/48-76x/61-91x): no work shown in TA — queued [verify]"),
    ("FORWARD", """
RCV ~ Zero (mine closed 1990)   |   B2: not applicable""", None)],
    "Epistemic-commons case: 27-year concealment held B ~ 0 while costs accrued (Sec. 6.3 Epistemic -> B mapping).")

case("5. Baotou rare earths (both directions live and large simultaneously)", [
    ("REVERSE", """
CSD: tailings-lake remediation $5-15B (cited estimate); health/agric/relocation heads Cited
M2 reads B1-hat: ~0 identified restitution
scale check (illustrative, not the TA's IPG): remediation alone / annual export revenue
   = (5..15) / (2..4)  =  1.3x - 7.5x of a full year's export revenue""",
     "TA Sec. 11.4. IPG triplet (12-35x/18-48x/22-41x): denominator not stated — queued [verify]"),
    ("FORWARD", """
M3: ongoing extraction, high-sigma-f REE register (2010-12 export-restriction spikes)  |  B2-hat ~ 0""",
     "TA Sec. 11.4 / 11.8")],
    "Forward-only accounting misses half the case: total CS = (CSD - B1) + (RCV - B2) needs BOTH terms here.")

case("6. Chesapeake oyster reef (the worked REVERSE case; Restitution Bond design)", [
    ("REVERSE — CSD, written end-to-end", """
M1 (CSD floor)   = foreclosed extent x realized restoration unit-cost
  realized basis = 2,738 ac x ($907,000/124 ac = $7,314/ac)   =  $20.0M
  headline basis = 2,738 ac x $13,500/ac (construction-only)  =  $37.0M
  robust central = 2,738 ac x $77,000/ac (bay-wide average)   =  $210.8M   (center, not floor)
M3 (ceiling var) = OPEN by design — foregone-fishery option value admitted, not entered
                   ("bond only the unassailable floor")  ->  computed CSD is a LOWER BOUND
M2 reads B1-hat  = MD $93.52M + VA $21.77M = $115.29M itemized (>$92M MD alone)
                   funders 100% public (NOAA, USACE, MD DNR, VMRC); industry share = $0
M2 corroboration = $108M / 1,900 restored ac = $56,842/ac  ->  inside the M1 band
                   ($13,500 floor < $57K < $77,000 average)  ->  unit-cost band corroborated
CSD_gap (floor basis):   B1-hat ($115M) already EXCEEDS the $20-37M floor -> restoration is
                         happening; the finding is MIS-ASSIGNMENT (public paid, industry $0)
CSD_gap (central basis): 210.8 - 115.3  =  ~$95.5M unrestituted even crediting every public dollar""",
     "Schulte 2017 Front. Mar. Sci. 4:127 (2,738 ac, 1910-1981); NOAA per-tributary table (Dec 2024); "
     "Great Wicomico Tributary Plan Sec. 5; MD DNR / Gov. Moore Aug 26 2025; engine Part 4 (exact)"),
    ("FORWARD", """
RCV (remaining reef): Cited — regeneration-function foreclosure (rho, Def 1.1)  |  B2: sanctuaries, Cited""",
     "Successor session: TA Sec. 11.12, GATE-2-gated (merges only after a book chapter prices the claim)")],
    "Formally distinct object: a RENEWABLE commons with its renewal structure extracted (the reef substrate "
    "the next generation sets on) — not a fixed non-renewable stock. AREA basis only; the Darling "
    "shell-mountain stays narrative.")

case("7. Reparations for Black American descendants of US slavery — STRUCTURAL TEST, not book content", [
    ("REVERSE — CSD, the field's own figures in the framework's slots", """
M1 (CSD floor)   = per-person remedy x eligible population        [the field's published cure-cost]
                 = ~$350,000 x ~40,000,000  =  ~$14.0T
                   basis: 2019 SCF mean Black-white household wealth gap $840,900
                   edition trajectory: 1st ed (2016 SCF) $267K x 40M = $10.7T  ->  2nd ed $14T
                   (an unpaid CSD accrues as the gap compounds; B1 delay is not cost-neutral)
M3 + coercion    = OPEN — wealth-gap floor deliberately excludes: the coercion vector (author's
                   first-person abstention; field flags direct pricing unresolved), the longevity
                   gap (Himmelstein et al. 2022), cultural-knowledge severance, intergenerational
                   trauma. Each: named, gate-admittable, non-negative, unentered.
M2 reads B1-hat  = federal $0 (no program; H.R. 40 never enacted) + municipal pilots O($10M) ~ 0
   comparators (the instrument exists for acknowledged harms):
                   Civil Liberties Act 1988 ~ $20K x ~82K internees ~ $1.6B [verify]
                   Black Lung ~ $44B (one occupational cohort)  ->  $0 here is not affordability
CSD  >=  $14.0T  (strict lower bound; Open slots unentered)
CSD_gap  =  14.0T - ~0  >=  $14.0T""",
     "Darity & Mullen, From Here to Equality 2nd ed. (UNC Press 2022); Darity-Mullen-Slaughter, "
     "J. Econ. Perspectives 36(2) 2022 (verified 2026-06-10); public record for B1"),
    ("FORWARD", """
RCV: ongoing-harm streams, Cited (outside current scope)   |   B2: no instrument exists (Open)""", None)],
    "Same three-slot shape as the reef, one structural difference made visible: reef B1 = large but "
    "MIS-ASSIGNED; reparations B1 = ABSENT. No framework-generated dollar figure appears here — every "
    "number is the field's own.")

case("8. Asteroid iron, pre-extraction (the zero-anchor)", [
    ("FORWARD", """
M3 = market x (1 + ln(1+ (1..10)) x 0.05 = 1.03-1.12) x (1/(1-(0.05..0.2)) = 1.05-1.25)
   = ~1.1x - 1.4x market price  ->  RCV ~ market (CIT abundance: both weights ~ 1)
M2 reads B2-hat: regime design question (Cited)""",
     "TA Sec. 11.8 asteroid calibration; Sec. 10.5 Corollary (lowest-RCV-first sequencing)"),
    ("REVERSE", """
CSD ~ 0 and B1 ~ 0 (nothing realized yet)  ->  identity assembles trivially""", None)],
    "That the framework prices abundance at ~market — no premium — is the calibration check, not a weakness.")

case("9. Closed-world habitat — ISS anchor (the CIT demonstration)", [
    ("FORWARD — M1 written out (what Earth's free commons cost to engineer)", """
M1 unit anchor:  water up-mass ~ $21,000/kg  (why ECLSS exists: ~90% recovery; 93% -> >98% closure)
M1 program scale: ~$150B all-partner construction (~2010)   [US-only ~$75B through 2013 = a SUBSET]
                  ~$3.1B/yr NASA operations
scope contrast (illustrative): $3.1B/yr / ~7 crew  ~  $440M/person-yr all-in program cost
                  vs TA Sec. 6.2 Dimension 1: ~$1M-10M/person-yr life-support-only engineered
                  equivalents — different scopes; never conflate
M3: planetary-scale atmosphere loss -> alpha -> 1 -> Sec. 12 incommensurability boundary + ARR
M2 reads B2-hat: ~0 (no off-world commons bond posted)
CS_forward = the entire engineered cost is unbonded""",
     "Parked candidates, bib Sec. 23.2 — re-verify vs NASA OIG (IG-18-021, IG-22-005) before any "
     "publisher-facing use [verify]"),
    ("REVERSE", """
CSD ~ 0; B1 n/a (the habitat IMPORTS its commons; nothing severed)""", None)],
    "The cleanest Commons Inversion Test on record: strip abundance and the same commons function "
    "acquires a documented price.")

case("10. NFL concussions (information-asymmetry case-class; both directions)", [
    ("REVERSE", """
CSD: career-shortening + CTE-class health costs (Cited; heads Open)
M2 reads B1-hat: ~$1B+ uncapped settlement, industry-paid, litigation-forced [verify]""",
     "Public record; framework case-class per Ch 5 lineage"),
    ("FORWARD", """
valuation side (NOT M2): wage premium on risk = revealed VALUATION data — hedonic/VSL tradition
                         (Rosen 1974; Viscusi 1993) — the Sec. 3.4 future RCV-side estimator;
                         no sourced premium entered here -> slot AVAILABLE, not Filled
M2 reads B2-hat: CBA health funds + settlement-funded monitoring (Filled, cited)""",
     "TA Sec. 3.4 note (ratified 2026-06-10)")],
    "The taxonomy this portfolio enforces: hazard pay reveals what players price the risk at (valuation "
    "column); the settlement is what the league actually posted (bond column). Never conflated.")

case("11. Apartment lease — the commute trade (n-of-1 self-severance; no bad actor)", [
    ("FORWARD — at signing (v = your revealed-preference hourly value; the input slot)", """
RCV  =  1,800 hrs/yr foreclosed x  v $/hr   =  1,800v $/yr      [Gate 2: dollar-convertible]
M2 reads B2-hat = 0 (no instrument exists)
CS_forward = 1,800v - 0 = 1,800v   — the severance is the whole foreclosure""",
     "TA Sec. 6.7 Walkthrough 2 (all four gates PASS)"),
    ("REVERSE — after the year", """
CSD  =  the same 1,800v, realized   |   M2 reads B1-hat = 0   |   CSD_gap = 1,800v""", None)],
    "Information-asymmetric SELF-severance: past-you signed without knowing what future-you would pay; "
    "value-capturer = cost-bearer. The apparatus runs identically at n-of-1 with no extractor — an "
    "accounting framework, not a theory of villains.")

A(Spacer(1, 8))
A(Paragraph("Provenance + regeneration", h2))
A(Paragraph(
    "Computed values reproduce in core/technical-appendix/calculations/csd_rcv_calculations.py "
    "(run-output_2026-06-10.txt: 21/21 reproduction checks PASS; 11/11 portfolio cases assemble the "
    "identity with all slots in legal states). TA references are to TechnicalAppendix_v2.0.0.html as "
    "merged 2026-06-10. Sec. 11.12 (reef) merges to the TA only after a book chapter carries the "
    "priced claim (GATE 2). Regenerate with gen_use_cases_pdf.py after any figure cascade.", small))

doc = SimpleDocTemplate(OUT, pagesize=letter,
                        leftMargin=0.65 * inch, rightMargin=0.65 * inch,
                        topMargin=0.65 * inch, bottomMargin=0.65 * inch,
                        title="Commons Bonds - Bidirectional Use-Case Worksheets v2 (2026-06-10)",
                        author="Commons Bonds working session")
doc.build(story)
print("wrote", OUT)
