#!/usr/bin/env python3
"""
Generate the bidirectional use-case worksheet PDF (forward RCV + reverse CSD).

Companion to csd_rcv_calculations.py — every computed number here traces to
that engine's verified output (21/21 reproduction checks PASS) or to the
merged TA v2.0.0 (main @ 2026-06-10). Regenerate after any cascade:
    /tmp/pdfenv/bin/python gen_use_cases_pdf.py

Font discipline (reportlab base-14): no raw Greek glyphs or Unicode
sub/superscripts — Greek is spelled (alpha, sigma-f); subscripts use <sub>.
"""
from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch
from reportlab.lib import colors
from reportlab.platypus import (SimpleDocTemplate, Paragraph, Spacer, Table,
                                TableStyle, PageBreak, KeepTogether)

OUT = "csd-rcv-bidirectional-use-cases_2026-06-10.pdf"
S = getSampleStyleSheet()

h1 = ParagraphStyle("h1x", parent=S["Heading1"], fontSize=15, spaceAfter=6)
h2 = ParagraphStyle("h2x", parent=S["Heading2"], fontSize=12, spaceBefore=10,
                    spaceAfter=4, textColor=colors.HexColor("#1a3a5c"))
body = ParagraphStyle("bodyx", parent=S["Normal"], fontSize=9.2, leading=12.6)
small = ParagraphStyle("smallx", parent=S["Normal"], fontSize=8, leading=10.5,
                       textColor=colors.HexColor("#444444"))
cell = ParagraphStyle("cellx", parent=S["Normal"], fontSize=8.4, leading=11)
cellb = ParagraphStyle("cellbx", parent=cell, fontName="Helvetica-Bold")
banner = ParagraphStyle("bannerx", parent=S["Normal"], fontSize=8.6, leading=11.6,
                        textColor=colors.HexColor("#7a1f1f"))

TBL = TableStyle([
    ("BACKGROUND", (0, 0), (-1, 0), colors.HexColor("#dde6ef")),
    ("GRID", (0, 0), (-1, -1), 0.4, colors.HexColor("#9aa7b5")),
    ("VALIGN", (0, 0), (-1, -1), "TOP"),
    ("LEFTPADDING", (0, 0), (-1, -1), 4),
    ("RIGHTPADDING", (0, 0), (-1, -1), 4),
    ("TOPPADDING", (0, 0), (-1, -1), 3),
    ("BOTTOMPADDING", (0, 0), (-1, -1), 3),
])
W = [0.85 * inch, 1.05 * inch, 2.55 * inch, 2.55 * inch]


def P(t, st=cell):
    return Paragraph(t, st)


def case_block(title, verdict, rows, notes):
    els = [Paragraph(title, h2)]
    data = [[P("Direction", cellb), P("Slot", cellb), P("Value / state", cellb),
             P("Source / basis", cellb)]]
    for r in rows:
        data.append([P(x) for x in r])
    els.append(Table(data, colWidths=W, style=TBL, repeatRows=1))
    if notes:
        els.append(Spacer(1, 3))
        els.append(P("<b>Notes.</b> " + notes, small))
    els.append(P("<i>Identity check: " + verdict + "</i>", small))
    els.append(Spacer(1, 8))
    return els


story = []
story.append(Paragraph("Commons Bonds — Bidirectional Use-Case Worksheets", h1))
story.append(Paragraph("Forward RCV and Reverse CSD, worked across the full case portfolio "
                       "(2026-06-10)", S["Heading3"]))
story.append(Spacer(1, 4))
story.append(P(
    "<b>INTERNAL WORKING DOCUMENT — author-facing.</b> Not publisher-facing prose; not book "
    "content as formatted here. The Reparations worksheet is a structural capability test built "
    "entirely from the reparations field's published figures (candidate share with Prof. Darity); "
    "the coercion vector remains an Open slot throughout, per the author's first-person "
    "abstention. Figures marked [verify] need re-verification before any external use.", banner))
story.append(Spacer(1, 8))

story.append(Paragraph("The architecture in one page", h2))
story.append(P(
    "The framework prices extraction in both temporal directions through one identity, the "
    "<b>Cost Severance Decomposition</b>:  <b>total CS = (CSD - B<sub>1</sub>) + "
    "(RCV - B<sub>2</sub>)</b>, where CSD is realized backward severance, RCV is prospective "
    "forward foreclosure, and B<sub>1</sub>/B<sub>2</sub> are the restitution and foreclosure "
    "bonds actually <i>posted</i> (posted, not owed - Def 1.7). The <b>Three Ways of Counting "
    "count the identity</b> (TA Sec. 3.6, ratified 2026-06-10): Methods 1 and 3 are the two "
    "independent value estimators - their convergence range is the supported RCV (or CSD); "
    "Method 2 <i>reads the realized Bond</i> - a strict lower bound on value, never a third "
    "estimator. The same observable is never both an estimate of value and the B subtracted "
    "from it.", body))
story.append(Spacer(1, 4))
mdef = [[P("Method", cellb), P("Forward (RCV)", cellb), P("Reverse (CSD)", cellb)],
        [P("<b>M1</b> - Replacement / Remediation"),
         P("Cost to engineer a substitute commons function (e.g. DAC $/ton; ISS life support). The floor."),
         P("Cost-to-cure: repair the realized loss (e.g. reef restoration $/acre; wealth-gap closure). The floor.")],
        [P("<b>M3</b> - Scarcity-adjusted option value"),
         P("RCV_M3 = V_market x scarcity_mult(sigma-f) x irrev_premium(alpha); "
           "scarcity_mult = 1 + ln(1+sigma-f) x 0.05; irrev_premium = 1/(1-alpha). "
           "Quasi-option value (Arrow-Fisher/Henry). alpha near 1 routes to Sec. 12 ARR."),
         P("Same multiplier form on realized parameters: V_market takes its backward reading "
           "(extinguished optionality / foregone service flow); sigma-f at the extraction moment; "
           "alpha observed. Ex-post (strict-liability) vs ex-ante (negligence) fork exposed, not settled.")],
        [P("<b>M2</b> - Realized-Bond reading"),
         P("Reads B<sub>2</sub> posted (Norway GPFG = $48/BOE). Reveals a lower bound on RCV."),
         P("Reads B<sub>1</sub> posted (restitution actually paid - and by whom). "
           "Reveals a lower bound and the mis-assignment diagnostic.")]]
story.append(Table(mdef, colWidths=[1.35 * inch, 2.8 * inch, 2.85 * inch], style=TBL))
story.append(Spacer(1, 4))
story.append(P(
    "<b>Three states of a cost slot (TA Sec. 5.5):</b> <i>Zero</i> (under abundance the cost "
    "genuinely is $0 - the CIT toggle) is not <i>Filled</i> (a value entered, derivation shown) "
    "is not <i>Open</i> (a real, gate-admitted slot deliberately left empty). An Open slot makes "
    "the computed total a <b>lower bound</b> - a sum missing a non-negative term. It is never a "
    "claim of zero, and never a claim of unpriceability. <i>Cited</i> below marks a direction "
    "the TA names but does not compute.", body))
story.append(Spacer(1, 2))
story.append(P(
    "Provenance: every computed value below reproduces in core/technical-appendix/calculations/"
    "csd_rcv_calculations.py (21/21 checks PASS against the merged TA) or is quoted from TA "
    "v2.0.0 (main, 2026-06-10) with its external source named.", small))
story.append(PageBreak())

# ---------------- worked cases ----------------
story += case_block(
    "1. McDowell County coal (forward-dominant; both directions live)",
    "RCV (M1/M3 convergence) minus realized B2-side reading = CS ~ $1,025-1,065/ton. Backward term real and large; needs the B1/B2 split.",
    [["Forward", "M1 (RCV)", "$290-2,702/ton across DAC horizons; at-scale $812-1,658, center ~$1,235",
      "TA Sec. 11.6; DAC bands Sec. 3.3 (Climeworks/Carbon Engineering/IEA-IPCC)"],
     ["Forward", "M3 (RCV)", "$339-3,668/ton; geometric center ~$1,115 (V=$40-140, mult 1.27-1.31, alpha 0.85-0.95)",
      "TA Sec. 11.6; engine Part 1 (exact reproduction)"],
     ["Forward", "M2 reads B", "$50-88/ton societally paid; $8-15/ton industry-paid",
      "TA Sec. 11.6 (Black Lung + reclamation + settlements)"],
     ["Forward", "CS", "~$1,025-1,065/ton; IPG 8.5-26x (premium basis), 67-134x (integral lens)",
      "TA Sec. 11.6 / Sec. 11.11; engine Part 2"],
     ["Reverse", "CSD (M1 heads)", "Reclamation shortfall $3.7-6B documented; 13-yr life-expectancy gap + legacy heads: Cited/Open",
      "TA Sec. 11.1; Sec. 5.5 example variables"],
     ["Reverse", "M2 reads B<sub>1</sub>", "Black Lung Trust Fund ~$44B cumulative through 2009 (restitution-type)",
      "GAO/CRS via TA Sec. 11.6"]],
    "The bidirectional run forces a split the forward-only TA never needed: Black Lung payouts are B<sub>1</sub> "
    "(realized-harm restitution); reclamation bonds are B<sub>2</sub> (posted against future damage). "
    "Flagged for Sec. 11.6."),

story = [e for sub in story for e in (sub if isinstance(sub, list) else [sub])]

story += case_block(
    "2. Norway petroleum (forward exemplar; backward quantified illustratively)",
    "Forward: CS ~ $233/BOE -> ~$12.8T cumulative. Backward: CSD ~ $3.9T with B1 ~ 0 for non-Norwegians - the same accountability gap, seen from behind.",
    [["Forward", "M1 (RCV)", "$161-422/BOE replacement-cost floor", "TA Sec. 11.5"],
     ["Forward", "M3 (RCV)", "$96-610/BOE; central ~$281 (sigma-f=100, alpha=0.65, V=$80 crude)",
      "TA Sec. 11.5; engine Part 1 (exact)"],
     ["Forward", "M2 reads B<sub>2</sub>", "GPFG ~$2.0T (NOK 21,268B, NBIM) at ~75% capture / 55B BOE = ~$48/BOE",
      "NBIM 2025; TA Sec. 3.4/11.5; engine Part 2"],
     ["Forward", "CS", "~$233/BOE; ~$12.8T cumulative (233 x 55B BOE)", "Engine Part 2"],
     ["Reverse", "CSD (illustrative)", "20.35 Gt CO2 combusted x $190/t SCC ~ $3.9T realized damage [labeled assumption: SCC basis]",
      "Emissions: TA Sec. 11.5 (sourced); SCC: EPA 2023"],
     ["Reverse", "M2 reads B<sub>1</sub>", "~0 for non-Norwegian cost-bearers (welfare state = B<sub>1</sub>-for-Norwegians only)",
      "TA Sec. 5.3/11.5 (the TA's own qualitative claim, now arithmetic)"]],
    "Norway's institutional architecture lowers effective alpha (0.50-0.75) - it attacks the foreclosure "
    "premium itself. The backward run shows whom it does NOT cover."),

story += case_block(
    "3. Deepwater Horizon (backward-dominant; the industry-paid B<sub>1</sub> exemplar)",
    "CSD - B1 ~ $8-12B (ongoing ecosystem externalities beyond BP's charges). Proves B1 CAN be industry-paid at scale - post-hoc, litigation-forced.",
    [["Reverse", "CSD", "~$61.6B all-in (BP 2016; $65B+ by 2018) + $8-12B ongoing Gulf ecosystem/fisheries",
      "TA Sec. 11.2 (DOJ/BP settlement components itemized)"],
     ["Reverse", "M2 reads B<sub>1</sub>", "$61.6B industry-paid - the largest realized B<sub>1</sub> in the corpus",
      "TA Sec. 11.2"],
     ["Reverse", "IPG", "~15-16x documented-cost basis; ~17-18x adding ongoing externalities",
      "TA Sec. 11.2 (aligned to inline arithmetic, 2026-06-10 fix)"],
     ["Forward", "RCV", "Remaining-well-class foreclosure: Cited (not computed in TA)", "TA Sec. 11.2"],
     ["Forward", "M2 reads B<sub>2</sub>", "Decommissioning bonds (BSEE 30 CFR 250/254; BLM): Cited, small vs RCV",
      "TA Sec. 5.1.2"]],
    "Structural contrast point: reef B<sub>1</sub> = public-paid; reparations B<sub>1</sub> = absent; "
    "Deepwater B<sub>1</sub> = industry-paid after litigation. The instrument exists at every assignment."),

story += case_block(
    "4. Libby, Montana vermiculite (backward-dominant; mixed-assignment B<sub>1</sub>)",
    "Backward term dominates; forward ~ 0 (mine closed 1990). B1 split ~70/30 public/industry.",
    [["Reverse", "CSD (components)", "$600M+ Superfund + $250M+ settlements + $50M+/yr medical + $500M+ property "
      "(stated $4B+ total: derivation queued to provenance pass)", "TA Sec. 11.3"],
     ["Reverse", "M2 reads B<sub>1</sub>", "$600M public (Superfund) + $250M industry (settlements)", "TA Sec. 11.3"],
     ["Reverse", "IPG triplet", "55-82x / 48-76x / 61-91x: shown-work queued to provenance pass", "TA Sec. 11.3 [verify]"],
     ["Forward", "RCV / B<sub>2</sub>", "~Zero / not applicable (operations ceased)", "TA Sec. 11.3"]],
    "Epistemic commons case: 27-year concealment held B ~ 0 while costs accrued - the Sec. 6.3 "
    "Epistemic-to-B mapping in action."),

story += case_block(
    "5. Baotou rare earths (both directions live and large simultaneously)",
    "Forward-only accounting misses half the case: total CS needs BOTH (CSD - B1) and (RCV - B2), both positive.",
    [["Reverse", "CSD", "Tailings-lake remediation $5-15B (cited estimate); health/agricultural/relocation heads Cited",
      "TA Sec. 11.4"],
     ["Reverse", "M2 reads B<sub>1</sub>", "~0 identified restitution", "TA Sec. 11.4"],
     ["Forward", "M3 (RCV)", "Ongoing extraction; high-sigma-f REE register (export-restriction spikes 2010-12)",
      "TA Sec. 11.4 / 11.8"],
     ["Forward", "M2 reads B<sub>2</sub>", "~0 identified", "TA Sec. 11.4"],
     ["—", "IPG triplet", "12-35x / 18-48x / 22-41x: denominator/derivation queued to provenance pass",
      "TA Sec. 11.4 [verify]"]],
    "Spatial severance at maximum documented scale (~10,000 km between value-capturer and cost-bearer)."),

story.append(PageBreak())

story += case_block(
    "6. Chesapeake oyster reef (the worked REVERSE case; Restitution Bond design)",
    "Bond anchored at the unassailable M1 floor; M3 named-not-priced (Open); the finding is MIS-ASSIGNMENT: realized B1 exceeds the floor and is 100% public / $0 industry.",
    [["Reverse", "M1 (CSD floor)", "2,738 ac foreclosed (James R. oyster-rock, 1910-1981) x $7,314/ac realized = "
      "<b>$20.0M</b>; x $13,500/ac construction = <b>$37.0M</b> headline floor",
      "Schulte 2017 Front. Mar. Sci. 4:127; NOAA per-tributary table (Great Wicomico $907K/124 ac); "
      "Great Wicomico Tributary Plan Sec. 5. Engine Part 4 (exact)"],
     ["Reverse", "M1 (central)", "x $77,000/ac bay-wide average = <b>$210.8M</b> (robust center, not the floor)",
      "NOAA per-tributary table; engine Part 4"],
     ["Reverse", "M2 reads B<sub>1</sub>", ">$92M Maryland / ~$115M bay-wide itemized (MD $93.52M + VA $21.77M) - "
      "100% public funders; <b>$0 from the extractive industry</b>",
      "MD DNR / Gov. Moore Aug 26 2025; NOAA itemized (primary); $108M program-level = rounding corroborator"],
     ["Reverse", "M2 corroboration", "$108M / 1,900 restored ac = ~$57K/ac - sits inside the M1 unit-cost band "
      "($13.5K floor < $57K < $77K avg)", "Engine Part 4"],
     ["Reverse", "M3 (ceiling)", "<b>Open by design</b> - foregone-fishery option value admitted, deliberately not "
      "entered (strategic decline: bond the provable floor). Method fully specified in Sec. 5.5; computed CSD is a "
      "lower bound", "Author decision 2026-06-08; TA Sec. 5.5 three-states"],
     ["Forward", "RCV / B<sub>2</sub>", "Remaining-reef regeneration-function foreclosure: Cited; sanctuary "
      "designations as in-kind B<sub>2</sub>: Cited", "Successor session (Sec. 11.12, GATE-2-gated)"]],
    "Formally distinct object: the reef forecloses the REGENERATION FUNCTION (rho, Def 1.1) - a renewable "
    "commons with its renewal structure extracted - not a fixed non-renewable stock. AREA basis only; the "
    "Darling shell-mountain stays narrative. Sec. 11.12 merges only after a book chapter carries the priced claim."),

story += case_block(
    "7. Reparations for Black American descendants of US slavery (STRUCTURAL TEST - not book content)",
    "CSD >= $14T (strict lower bound; Open slots unentered); B1 ~ $0 -> CSD - B1 >= $14T. The model supports the case: same three-slot shape as the reef.",
    [["Reverse", "M1 (CSD floor)", "<b>~$14T</b> = ~$350K/person x ~40M eligible (2019 SCF mean household gap "
      "$840.9K). The field's OWN published cure-cost - not a framework computation",
      "Darity & Mullen, From Here to Equality 2nd ed. (UNC Press 2022); Darity-Mullen-Slaughter, "
      "J. Econ. Perspectives 36(2) 2022. Verified 2026-06-10"],
     ["Reverse", "M1 trajectory", "1st ed. (2016 SCF): ~$10.7T -> 2nd ed. (2019 SCF): ~$14T - an unpaid CSD "
      "accrues as the gap compounds; B<sub>1</sub> delay is not cost-neutral", "Both editions, as published"],
     ["Reverse", "M2 reads B<sub>1</sub>", "Federal: <b>$0</b> (no program; H.R. 40 never enacted). Municipal pilots "
      "O($10M) - de minimis vs the floor", "Public record"],
     ["Reverse", "M2 comparators", "The restitution instrument exists for acknowledged harms: Civil Liberties Act "
      "1988 (~$20K/surviving internee [verify]); Black Lung ~$44B; Holocaust reparations lineage. "
      "The gap is acknowledgment, not affordability", "TA Sec. 5.5 case lineage; GAO/CRS"],
     ["Reverse", "M3 + coercion vector", "<b>Open</b> - the wealth-gap floor deliberately excludes the coercion "
      "vector (author's first-person abstention; field flags direct pricing unresolved), the longevity gap "
      "(Himmelstein et al., JAMA Netw Open 2022), cultural-knowledge severance, intergenerational trauma - "
      "each a named, non-negative, unentered term", "TA Sec. 5.5 three-states; Def 1.10 boundary"],
     ["Forward", "RCV / B<sub>2</sub>", "Ongoing-harm streams: Cited (outside current scope) / no instrument exists (Open)",
      "Engine Part 6"]],
    "Structural contrast the model makes visible: reef B<sub>1</sub> = large but MIS-ASSIGNED (public paid, "
    "industry $0); reparations B<sub>1</sub> = ABSENT (nobody paid; the instrument exists elsewhere). "
    "Candidate share with Prof. Darity; per the author's abstention, no framework-generated dollar figure "
    "appears in this worksheet - every number is the field's own."),

story.append(PageBreak())

story += case_block(
    "8. Asteroid iron, pre-extraction (the zero-anchor)",
    "Identity assembles trivially - and that it does so is the calibration: the framework prices abundance at ~market, not at a premium.",
    [["Forward", "M3 (RCV)", "~market price: sigma-f ~ 1-10, alpha 0.05-0.2 -> both weights ~ 1 (CIT abundance)",
      "TA Sec. 11.8 asteroid calibration"],
     ["Forward", "M2 reads B<sub>2</sub>", "Regime design question: Cited", "TA Sec. 10.5 Corollary (sequencing)"],
     ["Reverse", "CSD / B<sub>1</sub>", "~Zero / ~Zero (nothing realized yet)", "—"]],
    "Theorem 10.5 sequencing: extract lowest-RCV sources first - asteroid iron before Earth's critical deposits."),

story += case_block(
    "9. Closed-world habitat - ISS anchor (the CIT demonstration)",
    "RCV - B2 = the entire engineered cost: Earth's free air/water commons repriced at ISS rates. Reverse ~ 0 (the habitat imports its commons).",
    [["Forward", "M1 (RCV)", "Water up-mass ~$21,000/kg (why ECLSS exists: ~90% recovery; loop closure 93% -> >98%). "
      "Program scale: ~$150B all-partner construction (~2010); US-only ~$75B through 2013 (a SUBSET, not a rival "
      "total); ~$3.1B/yr NASA ops", "Parked candidates, bib Sec. 23.2 - re-verify vs NASA OIG (IG-18-021, IG-22-005) "
      "before any publisher-facing use [verify]"],
     ["Forward", "M3", "Planetary-scale atmosphere loss: alpha -> 1 routes to incommensurability boundary + ARR (Sec. 12)",
      "TA Sec. 12 (Europa/Mars scenarios)"],
     ["Forward", "M2 reads B<sub>2</sub>", "~0 - no off-world commons bond posted", "—"],
     ["Reverse", "CSD / B<sub>1</sub>", "~Zero / not applicable (no commons severed)", "—"]],
    "The cleanest Commons Inversion Test on record: strip abundance, the same commons function acquires a "
    "documented price. Use case parked; figures must be re-verified before print."),

story += case_block(
    "10. NFL concussions (information-asymmetry case-class; both directions)",
    "Backward term persists for the pre-disclosure cohort; post-2013 severance moves from unknowing to priced-risk. Wage premium and settlement are DIFFERENT columns.",
    [["Reverse", "CSD", "Career-shortening + CTE-class health costs: Cited; heads Open", "Framework case-class (Ch 5 lineage)"],
     ["Reverse", "M2 reads B<sub>1</sub>", "~$1B+ uncapped settlement, industry-paid, litigation-forced [verify before "
      "external use]", "Public record"],
     ["Forward", "Valuation (NOT M2)", "Wage premium on risk = revealed VALUATION data - hedonic/VSL tradition "
      "(Rosen 1974; Viscusi 1993), the Sec. 3.4 note's future RCV-side estimator", "TA Sec. 3.4 (ratified 2026-06-10)"],
     ["Forward", "M2 reads B<sub>2</sub>", "CBA health funds + settlement-funded monitoring: Filled (cited)", "Public record"]],
    "The taxonomy this portfolio enforces: hazard pay reveals what players price the risk at (valuation side); "
    "the settlement is what the league actually posted (bond side). Never conflated again."),

story += case_block(
    "11. Apartment lease - the commute trade (n-of-1 self-severance; no bad actor)",
    "Identity assembles with B = 0 on both sides; value-capturer = cost-bearer. The framework prices the severance regardless of whether anyone is to blame.",
    [["Forward", "RCV (at signing)", "~1,800 hrs/yr of foreclosed life-time x revealed-preference hourly value "
      "(dollar-convertible per Gate 2)", "TA Sec. 6.7 Walkthrough 2 (all four gates PASS)"],
     ["Forward", "M2 reads B<sub>2</sub>", "0 - no instrument", "—"],
     ["Reverse", "CSD (after the year)", "The same hours, realized; information-asymmetric self-severance "
      "(past-you signed without knowing what future-you would pay)", "TA Sec. 6.7"],
     ["Reverse", "M2 reads B<sub>1</sub>", "0", "—"]],
    "The smallest case in the portfolio, and the reason it matters: the apparatus runs identically at n-of-1 "
    "with no extractor, which is what makes it an accounting framework rather than a theory of villains."),

story.append(Spacer(1, 10))
story.append(Paragraph("Provenance + regeneration", h2))
story.append(P(
    "Computed values reproduce in <b>core/technical-appendix/calculations/csd_rcv_calculations.py</b> "
    "(run-output_2026-06-10.txt: 21/21 reproduction checks PASS; 11/11 portfolio cases assemble the identity "
    "with all slots in legal states). TA references are to TechnicalAppendix_v2.0.0.html as merged to main "
    "2026-06-10 (architecture: three ways count the identity; Sec. 5.5 reverse method applied). "
    "Sec. 11.12 (reef) merges to the TA only after a book chapter carries the priced restitution claim "
    "(GATE 2). Regenerate this PDF with gen_use_cases_pdf.py after any figure cascade.", small))

def _flatten(items):
    out = []
    for it in items:
        if isinstance(it, (list, tuple)):
            out.extend(_flatten(it))
        else:
            out.append(it)
    return out

story = _flatten(story)

doc = SimpleDocTemplate(OUT, pagesize=letter,
                        leftMargin=0.7 * inch, rightMargin=0.7 * inch,
                        topMargin=0.7 * inch, bottomMargin=0.7 * inch,
                        title="Commons Bonds - Bidirectional Use-Case Worksheets (2026-06-10)",
                        author="Commons Bonds working session")
doc.build(story)
print("wrote", OUT)
