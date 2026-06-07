# Method-3 Path-B Rework — Proposal Record (2026-06-07)

**Status: PROPOSED.** Author-ratified DIRECTION (Path B, 2026-06-07); the specific reworked numbers + exact TA edits require author + lead ratification before applying. **No TA edits made.** Supersedes "item 14" (the interim §11.8 V_option $50–500 reconciliation — known mis-specified: market-price underlying).

(Record captured by parent session from the rework agent's return — the agent's full draft (sections 1–7, exact quote-and-replace edits, 19-source bib list, cascade table) hit a sandbox write-block on `tools/rigor-passes/`; the exact edits will be regenerated at execution from the audit files + this record. Research inputs: `ta-m3-sigma-scarcity-grounding`, `ta-m3-alpha-irreversibility-grounding`, `ta-m3-voption-derivation`, `ta-method3-parameter-provenance`.)

## The Path-B formula
Single Dixit–Pindyck option premium, replacing `V_option × scarcity_multiplier × irreversibility_premium` (which double-counted volatility + irreversibility):

`RCV_M3 = M × V_underlying`, where `M = β/(β−1)`, and β = positive root of `½σ²β(β−1) + (r−δ)β − r = 0`.

Inputs (all sourced or flagged assumption): σ = coal price volatility ≈ 0.40 (EIA/IEA-anchored, range-central); V_underlying = social value, bounded by carbon (~$496/ton) → M1 ceiling (~$2,702/ton); r = 0.05, δ = 0.04 (standard assumptions — sensitivity required).

## Reworked McDowell-coal M3 (headline)
σ=0.40, r=0.05, δ=0.04 → β≈1.34, M≈3.94. On the carbon-floor underlying ($496): **RCV_M3 ≈ $1,950/ton central-conservative** (option premium (M−1)×$496 ≈ $1,460/ton). Band ~$1,500–8,300/ton across σ 0.30–0.50 and carbon-floor→central underlying; ceiling ~$14,000/ton at the M1-ceiling underlying.

## Convergence: HOLDS and tightens
Prior M3 mid (~$2,500) sat just above M1's band ($1,595–2,702); Path-B central-conservative (~$1,950 option-inclusive / ~$1,460 premium) lands inside/just below it. All three methods within one order of magnitude. Caveat: the band's high corner (~$14,000) exceeds M1 (as the old formula's $13,100 high corner did) — report the headline on the conservative anchor and disclose the band.

## Cascades to recompute
- §9.5 McDowell RCV-Model cell (currently 67–134×) and §11.11 ("50–555×" upper bound) → likely ~39–280×; re-verify the ✓.
- §3.5 (replace scarcity_multiplier + irreversibility_premium defs with the D-P premium); §11.6 (~4740–4801, re-present McDowell M3); §11.8 (~5228–5350, α-dominance → D-P sensitivity; V_option $50–500 superseded).

## OPEN QUESTIONS for author + lead (must resolve before applying)
1. **Headline quantity:** report option-inclusive `M×V` (~$1,950, agent-recommended) or option premium `(M−1)×V` (~$1,460)?
2. **Norway cascade — HIGHEST RISK.** Old moderate α (0.50–0.75) encoded "GPFG funds restoration optionality → out of α-dominance" — the institutional-architecture story central to Norway's canonical-B₂-exemplar role. Path B has no α dial; that story must be re-expressed (lower effective underlying? narrative caveat?). Needs an explicit decision.
3. **r and δ (0.05 / 0.04) are assumptions** — add a one-line sensitivity so they aren't load-bearing-by-stealth.
4. **σ's former "scarcity" role splits:** reserves-to-production scarcity → into V_underlying; price volatility → into M. Confirm no residual scarcity multiplier remains.
5. **β symbol collision:** old β = risk-posture exponent (β=1/β=2); Path-B β = D-P quadratic root — add a one-line note retiring the old meaning.

## Bibliography additions (to add when executing)
σ R/P (EIA/BP/USGS); α irreversibility (Palmer 2010, Bernhardt & Palmer 2011, Lindberg 2011, Solomon 2009, IPCC AR6 SPM B.5, Archer 2009); commodity volatility (CBOE OVX / EIA / IMF / World Bank). Dixit-Pindyck 1994 + Arrow-Fisher 1974 already in bib (extend D-P use-note to the M3 premium).
