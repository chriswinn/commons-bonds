# TA Method-3 α (irreversibility fraction) — empirical-irreversibility grounding

**Date:** 2026-06-07
**Workstream:** Commons Bonds "M3-rigor" — grounding Method-3 parameters in real evidence.
**Parameter:** α (alpha), the IRREVERSIBILITY fraction (share of extraction loss
that is irreversible). Currently POSITED at α ≈ 0.85–0.95 in
`manuscript/technical-appendix/TechnicalAppendix_v2.0.0.html` §3.5 (formula, ~line 889–897)
+ §11.6 McDowell-coal build (~line 4744) + §11.8 sensitivity (~lines 5233, 5258, 5283).
**Stakes:** highest of the five M3 parameters. Output ∝ irreversibility_premium =
1/(1−α)^β. At β=1: α=0.85 → premium 6.67; α=0.95 → premium 20 (a 3× swing across
the posited band). At β=2 the band swings 44→400. α is the load-bearing dial.
**Discipline:** HARD no-invented-claims. Every citation below was web-verified and
quoted only to the extent the source actually supports. Where the literature
grounds a *direction* but not a *number*, that distinction is stated explicitly.
**Scope:** READ-ONLY research. Nothing in the TA was edited.

---

## How this complements the prior provenance audit

`tools/audits/ta-method3-parameter-provenance_2026-06-06.md` already established the
*status* verdict: **α ≈ 0.85–0.95 is a POSITED ASSUMPTION** — no source supplies an
empirical irreversibility *fraction* for coal/MTR; the real-options + quasi-option-value
literature (Arrow & Fisher 1974; Dixit & Pindyck 1994) grounds the *form/motivation*
of an irreversibility premium but not the numeric band. That verdict stands and is not
disturbed here.

This audit asks the *next* question the M3-rigor mandate poses: **does the physical
irreversibility record let class-1/class-2 evidence REPLACE the posited assumption, and
is 0.85–0.95 conservative relative to that record?** The answer is that the physical
record cannot pin α to a *point* (α is a modeling abstraction, not a measured quantity),
but it can do three useful things: (1) ground the *direction and high-end placement* of α
with authoritative citations; (2) support the framework's prose claim that McDowell sits
in the α-dominance regime; and (3) support the assessment that **0.85–0.95 is, if
anything, conservative** for the resource-depletion and carbon-persistence components.

---

## Dimension (a) — coal / mountaintop-removal ecological irreversibility

**Strongest verbatim anchor — Bernhardt & Palmer 2011 (peer-reviewed review).**
> "There is, to date, no evidence to suggest that the extensive chemical and
> hydrologic alterations of streams by MTVF [mountaintop mining with valley fill]
> can be offset or reversed by currently required reclamation and mitigation practices."

— Bernhardt, E. S. & Palmer, M. A. (2011). "The environmental costs of mountaintop
mining valley fill operations for aquatic ecosystems of the Central Appalachians."
*Annals of the New York Academy of Sciences* 1223(1):39–57.
DOI: 10.1111/j.1749-6632.2011.05986.x
https://nyaspubs.onlinelibrary.wiley.com/doi/abs/10.1111/j.1749-6632.2011.05986.x
(abstract verified via PubMed 21449964: https://pubmed.ncbi.nlm.nih.gov/21449964/)

Same abstract documents the scale of the foreclosure: MTVF "have converted 1.1 million
hectares of forest to surface mines and buried more than 2,000 km of stream channel
beneath mining overburden," with impacts "propagated throughout the river networks of the
region." This is the single most directly on-point sentence in the literature for α: a
peer-reviewed statement that the alteration is, under the actual policy/reclamation
regime, **not reversed** — which is precisely the operational meaning of α (probability
the commons cannot be restored at finite cost once extracted, TA line 893–894).

**Persistence-decades evidence — Lindberg et al. 2011 (PNAS).**
Mines "reclaimed nearly two decades ago continue to contribute significantly to water
quality degradation"; weathering-derived ions (sulfate, calcium, magnesium) "continue to
be exported at high concentrations even decades after surface mines have been reclaimed."
EPA estimate cited: ~1,944 km of headwater streams buried 1992–2002, projected to roughly
double to ~4,000 km by 2012.

— Lindberg, T. T., Bernhardt, E. S., Bier, R., Helton, A. M., Merola, R. B.,
Vengosh, A., & Di Giulio, R. T. (2011). "Cumulative impacts of mountaintop mining on an
Appalachian watershed." *PNAS* 108(52):20929–20934. DOI: 10.1073/pnas.1112381108
https://www.pnas.org/doi/10.1073/pnas.1112381108

**Foundational policy/science statement — Palmer et al. 2010 (Science).**
The landmark *Science* policy-forum paper documenting forest clearance, valley-fill
stream burial, and downstream water-chemistry degradation (elevated conductivity, total
dissolved solids, sulfate, heavy metals), and arguing that mitigation/reclamation does
not compensate for the lost ecological functions.

— Palmer, M. A., Bernhardt, E. S., Schlesinger, W. H., et al. (2010). "Mountaintop
mining consequences." *Science* 327(5962):148–149. DOI: 10.1126/science.1180543
https://www.science.org/doi/abs/10.1126/science.1180543
(PubMed 20056876 — no abstract on PubMed; cite for the policy-forum claims, verified via
the title/venue and the companion Bernhardt & Palmer 2011 review which restates them).

**What (a) supports:** the MTR-habitat component of α sits at the high end. Bernhardt &
Palmer's "no evidence … can be offset or reversed" is a *categorical-under-current-regime*
statement, which maps to α near 1 for the habitat sub-component, not to a moderate value.
It does NOT supply a number; it supports "high, near-1" rather than "0.85 specifically."

---

## Dimension (b) — atmospheric CO₂ persistence / climate irreversibility

**Strongest institutional anchor — IPCC AR6 WG1 SPM B.5 (verbatim headline statement).**
> "Many changes due to past and future greenhouse gas emissions are irreversible for
> centuries to millennia, especially changes in the ocean, ice sheets and global sea
> level."

— IPCC, 2021: *Summary for Policymakers.* In *Climate Change 2021: The Physical Science
Basis* (WG1 contribution to AR6), statement B.5.
https://www.ipcc.ch/report/ar6/wg1/chapter/summary-for-policymakers/
(headline statements: https://www.ipcc.ch/report/ar6/wg1/downloads/report/IPCC_AR6_WGI_Headline_Statements.pdf)
B.5 sub-statements add that changes are irreversible on centennial-to-millennial scales
in global ocean temperature, deep-ocean acidification, and deoxygenation; and that global
sea level "will continue to rise for thousands of years" even at net-zero CO₂.

**Foundational peer-reviewed anchor — Solomon et al. 2009 (PNAS), title is the claim.**
> "the climate change that takes place due to increases in carbon dioxide concentration
> is largely irreversible for 1,000 years after emissions stop."

> "Future carbon dioxide emissions in the 21st century will hence lead to adverse climate
> changes on both short and long time scales that would be essentially irreversible."

On atmospheric persistence: "a quasi-equilibrium amount of CO₂ is expected to be retained
in the atmosphere by the end of the millennium … typically ≈40% of the peak concentration
enhancement."

— Solomon, S., Plattner, G.-K., Knutti, R., & Friedlingstein, P. (2009). "Irreversible
climate change due to carbon dioxide emissions." *PNAS* 106(6):1704–1709.
DOI: 10.1073/pnas.0812721106
https://www.pnas.org/doi/10.1073/pnas.0812721106

**Long-tail anchor — Archer et al. 2009 (Annual Review).**
CO₂ from fossil-fuel combustion equilibrates among atmosphere/ocean/biosphere over "a few
centuries," but "20–35% of the CO₂ remains in the atmosphere after equilibration with the
ocean (2–20 centuries)," with a residual fraction persisting on weathering timescales of
hundreds of thousands of years before return to the solid earth.

— Archer, D., Eby, M., Brovkin, V., Ridgwell, A., Cao, L., Mikolajewicz, U., Caldeira, K.,
Matsumoto, K., Munhoven, G., Montenegro, A., & Tokos, K. (2009). "Atmospheric lifetime of
fossil fuel carbon dioxide." *Annual Review of Earth and Planetary Sciences* 37:117–134.
DOI: 10.1146/annurev.earth.031208.100206
https://www.annualreviews.org/doi/abs/10.1146/annurev.earth.031208.100206

**What (b) supports:** the carbon-cycle component of α is **near-1 by the consensus
record**. IPCC AR6 calls the relevant changes "irreversible for centuries to millennia";
Solomon et al. call them "essentially irreversible"; Archer et al. show a fraction
persisting on hundred-thousand-year scales. On the human/civilizational timescale the
framework operates over, the carbon-persistence sub-component is effectively α → 1. This
is the firmest of the three dimensions for asserting "0.85–0.95 is conservative."

---

## Dimension (c) — resource-depletion irreversibility (coal non-regenerating)

**The resource itself is non-regenerating on human timescales.** Coal forms over
geological time: peat → lignite → bituminous → anthracite under sustained heat and
pressure across tens to hundreds of millions of years; the great Appalachian/Carboniferous
coal-forest deposits date to the Carboniferous (~359–299 Ma). Even the youngest (lignite)
ranks require on the order of 10⁷ years; higher ranks 10⁸ years. There is no human-timescale
replenishment path; once a seam is mined and combusted, the stock is foreclosed permanently
relative to any decision horizon.

This is uncontroversial geology rather than a contested empirical estimate. Citable to a
standard geology/USGS treatment of coal formation (e.g., USGS coal-geology resources;
National Geographic "Carboniferous Period"
https://www.nationalgeographic.com/science/article/carboniferous) and to the resource-
economics non-renewability framing already in the TA (Hotelling 1931, in bib).

**Tie to the TA's own model.** TA §3.1/§3.2 (line ~331) already states the structural
point: "When ρ = 0 (strict non-renewability), extraction is irreversible and foreclosure
is permanent." Coal is the ρ ≈ 0 case. The resource-stock sub-component of α is therefore
α = 1 *by the framework's own definition*, not by external measurement.

**What (c) supports:** the stock-depletion sub-component is definitionally α = 1. This is
the cleanest of the three: it requires no contested number, only the geological fact that
coal does not regenerate on human timescales plus the framework's own ρ=0 definition.

---

## Assessment: where does α ≈ 0.85–0.95 sit relative to the record?

**α is a composite of (at least) three sub-components for the McDowell case** — as the TA
itself states at line 4745: "mountaintop-removal habitat irreversible at finite engineering
cost; cultural-and-community commons irreversible without targeted intervention;
atmospheric carbon-cycle disruption irreversible at climate-tipping-point boundary." Reading
the literature against each:

| Sub-component | Literature verdict | Implied α sub-value |
|---|---|---|
| Resource stock (coal) | Non-regenerating on human timescales; framework's own ρ=0 ⇒ permanent foreclosure | **≈ 1.0** (definitional) |
| Atmospheric carbon | IPCC AR6 "irreversible for centuries to millennia"; Solomon "essentially irreversible"; Archer long tail | **≈ 1.0** on human timescale |
| MTR aquatic/forest habitat | Bernhardt & Palmer: "no evidence … can be offset or reversed" under current regime; decades-persistent post-reclamation | **high, near-1** under current policy |
| Community/cultural commons | Not addressed by physical-science literature; framework calls it "partially recoverable through targeted intervention" (§11.8 line 5233) | the one component plausibly **< 1** |

**Verdict: α ≈ 0.85–0.95 is CONSERVATIVE for the physical/resource components and
defensible overall.**

- For the **resource-stock and carbon-persistence components, the record supports α → 1**,
  i.e. *above* the 0.85–0.95 band. A reader could legitimately argue the framework
  *understates* irreversibility for these two channels.
- The band is held *below* 1 primarily by the **community/cultural-commons component**,
  which the framework explicitly treats as "partially recoverable through targeted
  intervention." That is the right reason for α < 1, and it is honestly the component
  with the *least* external grounding (no physical-science literature pins it).
- So the band's placement is reasonable, and the *direction* of any defensible objection
  is that 0.85–0.95 is too LOW, not too high. That is the conservative direction for a
  cost-of-extraction estimate, consistent with the framework's epistemic-humility posture
  (RCV figures are lower bounds).

**Important caveat — α remains a posited composite, not a measured fraction.** The
literature grounds (i) the *direction* (high, approaching 1 for the physical channels),
(ii) the *qualitative* claim that McDowell is in the α-dominance regime, and (iii) the
*assessment* that 0.85–0.95 is conservative. It does NOT convert α into a class-1
(directly measured) or class-2 (derived-from-measured-inputs) quantity. There is no
published "irreversibility fraction" for coal/MTR; α is an abstraction that aggregates
heterogeneous, differently-reversible sub-losses into one [0,1] dial. The honest status
after this audit is **"posited composite parameter whose high-end placement is now
empirically corroborated for its physical sub-components,"** not "sourced value." This is
an *upgrade* of the provenance verdict (from bare-posited to direction-grounded), not a
replacement of posited-with-measured.

**Sensitivity note (why this matters and why it partly doesn't).** Because output ∝
1/(1−α)^β, the 0.85→0.95 band is genuinely high-leverage (premium 6.67→20 at β=1). The
literature does not let us narrow *within* the band — it argues only that the band is, if
anything, low. The practical implication: the framework should NOT present α as precisely
known, but CAN defend the band as conservative and cite the direction-grounding sources.
The §11.8 α-dominance framing ("the debate about RCV is a debate about irreversibility")
is itself supported: the load-bearing empirical question genuinely is "is this loss
irreversible?", and for two of the three physical channels the consensus answer is
unambiguously yes.

---

## Recommended bibliography additions

These are the genuinely on-point, web-verified sources currently ABSENT from
`tools/back-matter/sources/bibliography.md`. (Bib grep 2026-06-07 confirms none of Palmer,
Bernhardt, Lindberg, Solomon, Archer, or an IPCC AR6 WG1 SPM entry are present; only
Nordhaus DICE, Stern, and the Rio precautionary-principle entry exist on the climate side.)

1. **Palmer, M. A., Bernhardt, E. S., Schlesinger, W. H., et al. (2010).** "Mountaintop
   mining consequences." *Science* 327(5962):148–149. DOI: 10.1126/science.1180543. —
   Foundational MTR-irreversibility / reclamation-failure anchor. Ch 8 (McDowell);
   TA §11.6/§11.8 α grounding.
2. **Bernhardt, E. S. & Palmer, M. A. (2011).** "The environmental costs of mountaintop
   mining valley fill operations for aquatic ecosystems of the Central Appalachians."
   *Annals of the New York Academy of Sciences* 1223(1):39–57.
   DOI: 10.1111/j.1749-6632.2011.05986.x. — **Primary verbatim α anchor** ("no evidence …
   can be offset or reversed").
3. **Lindberg, T. T., Bernhardt, E. S., Bier, R., et al. (2011).** "Cumulative impacts of
   mountaintop mining on an Appalachian watershed." *PNAS* 108(52):20929–20934.
   DOI: 10.1073/pnas.1112381108. — Decades-persistent degradation; stream-burial scale.
4. **Solomon, S., Plattner, G.-K., Knutti, R. & Friedlingstein, P. (2009).** "Irreversible
   climate change due to carbon dioxide emissions." *PNAS* 106(6):1704–1709.
   DOI: 10.1073/pnas.0812721106. — Carbon-irreversibility anchor (also relevant to Ch 2
   carbon footnote + the ARR irreversibility-weighting lineage).
5. **IPCC, 2021. WG1 Summary for Policymakers, statement B.5** (in *Climate Change 2021:
   The Physical Science Basis*). https://www.ipcc.ch/report/ar6/wg1/chapter/summary-for-policymakers/ —
   Consensus-institutional "irreversible for centuries to millennia" anchor. Note: TA §11.6
   line 5394 already *claims alignment* with "IPCC AR6 / climate-tipping-point literature"
   but does not cite it; this closes that gap.
6. **Archer, D., Eby, M., Brovkin, V., et al. (2009).** "Atmospheric lifetime of fossil
   fuel carbon dioxide." *Annual Review of Earth and Planetary Sciences* 37:117–134.
   DOI: 10.1146/annurev.earth.031208.100206. — Long-tail CO₂ persistence (20–35% over 2–20
   centuries; residual over 10⁵ yr). Supports both α (carbon channel) and the σ→non-renewable
   framing.

Plus, carried over from the prior provenance audit as the *construct/form* citations α
should footnote (already recommended there, not re-litigated here):
**Arrow & Fisher 1974** *QJE* 88(2):312–319 (quasi-option value of preserving an
irreversibly-losable resource — currently absent from the bib and from §3.5) and
**Dixit & Pindyck 1994** (real-options irreversibility; in bib for S(t) only).

## Suggested framing language for the TA (not applied — author ratification gate)

α should be presented as: *a posited composite irreversibility parameter whose high-end
placement (0.85–0.95) is corroborated, for its physical sub-components, by the
irreversibility record — the coal stock does not regenerate on human timescales (ρ=0,
§3.1); atmospheric carbon disruption is "irreversible for centuries to millennia" (IPCC
AR6 SPM B.5; Solomon et al. 2009); and MTR stream/forest alteration shows "no evidence …
can be offset or reversed by currently required reclamation" (Bernhardt & Palmer 2011).
The band is held below 1 only by the partially-recoverable community/cultural component;
for the physical channels the literature supports α → 1, so 0.85–0.95 is conservative.*

---

## Sources (all web-verified 2026-06-07)
- Palmer et al. 2010 *Science*: https://www.science.org/doi/abs/10.1126/science.1180543 ; PubMed https://pubmed.ncbi.nlm.nih.gov/20056876/
- Bernhardt & Palmer 2011 *Ann. NYAS*: https://nyaspubs.onlinelibrary.wiley.com/doi/abs/10.1111/j.1749-6632.2011.05986.x ; PubMed https://pubmed.ncbi.nlm.nih.gov/21449964/
- Lindberg et al. 2011 *PNAS*: https://www.pnas.org/doi/10.1073/pnas.1112381108 ; PMC https://pmc.ncbi.nlm.nih.gov/articles/PMC3248525/
- Solomon et al. 2009 *PNAS*: https://www.pnas.org/doi/10.1073/pnas.0812721106 ; PMC https://pmc.ncbi.nlm.nih.gov/articles/PMC2632717/
- IPCC AR6 WG1 SPM (B.5): https://www.ipcc.ch/report/ar6/wg1/chapter/summary-for-policymakers/ ; headline statements PDF https://www.ipcc.ch/report/ar6/wg1/downloads/report/IPCC_AR6_WGI_Headline_Statements.pdf
- Archer et al. 2009 *Annu. Rev. Earth Planet. Sci.*: https://www.annualreviews.org/doi/abs/10.1146/annurev.earth.031208.100206
- Coal formation / non-renewability (dimension c): https://www.nationalgeographic.com/science/article/carboniferous
- Prior in-repo audit: `tools/audits/ta-method3-parameter-provenance_2026-06-06.md`
