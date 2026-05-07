# Framework scope-explicitness discipline (lead-them-to-water)

**Created:** 2026-05-06 by Claude per author direction.
**Source:** Captured during Darity interview prep work (2026-05-06). Author flagged that the bibliography Ostrom entry, the Darity pre-read brief, and Claude's chat language were all using regime-agnostic phrasing or non-renewable-only examples while *technically* covering both renewable-past-regen and non-renewable extraction. Per author's sales experience: regime-agnostic phrasing in proximity to non-renewable-only examples reads as effectively non-renewable framing — readers default to the more familiar interpretation, and the framework's contribution gets understated at exactly the moment we're trying to land it.
**Status:** Working discipline; promote to canonical scaffolding (alongside working principles / vocabulary strategy in `alignment/`) if it earns the slot.

---

## The discipline

**Whenever the framework's regime coverage matters — Ostrom extension, RCV definition, the cost-severance mechanism's domain, or any framework-positioning paragraph — name BOTH regimes (non-renewable AND renewable-past-regen) explicitly with an example pair.**

Don't rely on:
- Regime-agnostic phrasing alone (e.g., "commons that are drawn down during extraction" without specifying what kinds)
- Non-renewable-only example lists (e.g., "fossil fuels, non-renewable minerals, climate stability")
- Reader interpretive work to extend the framework's domain

Readers default to the more familiar interpretation (non-renewable only) and the framework's contribution gets understated. Forwardability and adoption depend on grasping the full scope without interpretive work.

This is the same family as the **forwardability criterion** captured 2026-05-06 (don't make readers do interpretive work; spell out the categories so recipients can self-identify). The mechanism is identical: assume readers won't connect dots; lead them to water.

## Framework scope (precise)

**RCV pricing instrument applies to commons being drawn down. Two regime cases:**

1. **Non-renewable resources from the start** — finite stock; every unit extracted reduces remaining stock; foreclosure is structural to the resource type. *Examples: coal, oil, rare-earth minerals, climate stability (one-shot atmospheric carbon budget).*
2. **Renewable resources pushed past regenerative capacity** — finite recovery rate; extraction past rate causes population/ecosystem decline; foreclosure begins at the threshold-crossing. Once across the threshold, the renewable resource becomes effectively non-renewable, and the same RCV accounting applies. *Examples: Chesapeake Bay fisheries, oyster reefs, exhausted soil systems, depleted forest systems, collapsed groundwater aquifers.*

**Both regimes are co-equal cases the framework was built to cover, not a primary case + boundary test.** (Earlier "boundary test" framing of the renewable-past-regen case is dated — predates Path F structural decisions; should be retired in any document using it.)

## Framework application (broader)

The framework's *cost-severance vocabulary* and *accountability-instrument architecture* (Restitution Bond + Foreclosure Bond) apply broadly to any extraction system where costs are externalized — including extraction systems that aren't directly priced by the RCV instrument.

**The renewable-energy-systems clarifying note:**

> Renewable-energy systems (solar, wind, hydro) fall within the framework's analytical reach via their material-extraction (non-renewable scope), ecosystem-impact (renewable-past-regen scope), and end-of-life waste-disposal components — *not* by expanding the framework's renewable-side scope to cover non-depletable energy fluxes. Solar irradiance and wind kinetic energy are continuous fluxes, not stocks; there's no foreclosure mechanism for the energy itself, so RCV ≈ 0 for the energy. But the *systems* that capture this energy have:
>
> 1. **Material extraction** (rare earths, lithium, copper, silicon, neodymium for magnets) — non-renewable extraction. Framework's primary non-renewable scope. RCV pricing applies cleanly.
> 2. **Land use / ecosystem disruption** (solar farms displacing soil ecosystems, wind farms with bird mortality, hydropower disrupting river ecosystems) — these are renewable-past-regen cases for the affected ecosystem (the soil, the bird population, the river ecosystem). RCV pricing applies to the affected commons.
> 3. **End-of-life / decommissioning waste** — depletable commons (landfill capacity, processing infrastructure). RCV pricing applies.
>
> So the framework's RCV pricing *does* apply to solar/wind systems, but through the *non-renewable mining + ecosystem-past-regen + waste-disposal* paths — not by adding "renewables not yet past regen" to the framework's domain.

This distinction matters because:
- Without it, a careful reader (Darity-class) would push: "your RCV formula assumes foreclosure; sunlight doesn't have foreclosure; explain." We'd then walk back the broad claim.
- With it, the framework's analytical reach is preserved (solar/wind systems are within scope) AND the RCV instrument's structural condition is preserved (foreclosure required).

## Standard framings to use (drop-in replacements)

**One-line Ostrom-extension framing:**

> Ostrom extension: commons-governance for the full extraction spectrum — non-renewable resources from the start (coal, oil, minerals, climate stability) AND renewable resources pushed past regenerative capacity (Chesapeake fisheries, oyster reefs, forest systems) — where sustained-yield management is no longer possible.

**RCV definition (drop-in standard):**

> Residual commons value (RCV) is the worth permanently foreclosed when a non-renewable resource, or a renewable resource pushed past regenerative capacity, is drawn down.

**Where the framework lives in extraction-domain space (drop-in standard):**

> The framework prices commons drawn down during extraction — both non-renewable resources from the start AND renewable resources pushed past regenerative capacity. The cost-severance mechanism operates the same way across both regimes, even though their physics differ.

## Application checklist (2026-05-06 corrections)

| File | Issue | Status |
|---|---|---|
| `research/literature/bibliography.md` Ostrom entry | Listed only non-renewable examples | ✓ FIXED 2026-05-06 (both regimes named explicitly with example pairs) |
| `research/outreach/darity-prereadbrief_2026-05-05.md` framework paragraph | RCV defined only for non-renewable | ✓ FIXED 2026-05-06 (RCV definition expanded to both regimes; accounting-equation thesis sentence expanded) |
| `research/outreach/amsterdam-donut-prereadbrief_2026-05-06.md` framework paragraph | RCV defined only for non-renewable | ✓ FIXED 2026-05-06 (RCV definition expanded to both regimes) |
| `research/outreach/darity-interview-prep_2026-05-06.md` follow-up Q6 | RCV phrasing mismatch with corrected pre-read | ✓ FIXED 2026-05-06 |
| `research/case-studies/chesapeake-fisheries.md` | Treats renewable-past-regen as a *boundary test* of a non-renewable formula, rather than a co-equal case the framework was built to cover. Pre-Path-F framing. | ⏳ Deferred to broader manuscript review session — flagged for treatment when chesapeake case study is developed past placeholder. |
| `core/technical-appendix/TechnicalAppendix_v1.0.0.html` (formal apparatus) | Worth a separate scope-explicitness review pass | ⏳ Deferred to v2.0.0 rebuild (already queued per AGENTS.md current state) |
| `core/glossary/commons_bonds_updated_glossary_v3.html` (RCV / cost-severance entries) | Worth a separate scope-explicitness review pass | ⏳ Deferred to v4 rebuild (already queued) |
| `manuscript/chapters/Chapter__6_ThreeWaysofCounting__Draft.html` (math-heavy chapter) | Worth a scope-explicitness pass when the chapter develops past placeholder math | ⏳ Deferred to chapter-development session |
| `README.md` (publisher-facing) | Currently says "across extraction domains — coal mining, oil drilling, fisheries..." — fisheries are named so the renewable-past-regen case is implicitly included, but not framed as co-equal regime | ⏳ Worth reviewing in next manuscript-rigor pass |

## Cross-references

- `research/outreach/interview-attribution-protocol_2026-05-06.md` — sibling discipline document; same family (reusable pipeline disciplines captured during outreach work).
- Forwardability criterion (captured 2026-05-06 in `research/outreach/response-draft_2026-05-06_moore-via-sherfinski.md` §"Forwardability design criterion") — same underlying principle (don't make readers do interpretive work).
- `alignment/commons_bonds_working_principles_v1.0.0.md` — canonical working principles; this discipline is a candidate for promotion to that document if it earns the slot.
- `alignment/commons_bonds_vocabulary_strategy_v1.0.1.md` — canonical vocabulary strategy; the scope-explicitness discipline applies most directly to the framework's vocabulary positioning.
- `tools/commons_bonds_book_scope_v1_0_3.md` — book scope canonical; should reflect the both-regimes-co-equal framing.
