# Technical Appendix — Master Symbol Registry & Notation Audit (2026-06-07)

**Status: PROPOSED working artifact.** Built from a 7-agent exhaustive catalog of every symbol in `TechnicalAppendix_v2.0.0.html` (lines 1–8041), consolidated + collision-swept + standard-notation-checked. Internal source-of-truth; the reader-facing Notation section is to be curated FROM this.

**Method:** 7 parallel catalog agents (one per line-range), each recording every symbol-occurrence (glyph · meaning · role · section · line · units · provenance) + within-range collisions + existing disambiguation notes. This file consolidates to distinct (symbol × meaning) pairs and flags cross-section collisions.

**Legend:** Role D=definition site, u=use. Collision severity: 🔴 HIGH (same glyph, genuinely different quantity, reader-confusing) · 🟠 MED (case/subscript-distinguished or one-section-local) · 🟢 OK (already disambiguated in text, or standard).

---

## PART 1 — COLLISIONS REQUIRING ACTION (the headline)

### 🔴 HIGH — same glyph, genuinely different quantity, NOT disambiguated

| Glyph | Meaning A | Meaning B | Locations | Note |
|---|---|---|---|---|
| **α** | Method-3 **irreversibility probability** ∈[0,1] (§3.5, §11.5–11.8) | §16.2 **scarcity effect on innovation incentives** (coefficient >0) | A: 893–4, 4295ff, 5063ff · B: 7350, 7353 | Two unrelated quantities. §16.2 has no note. The framework's *best-grounded* parameter name is being reused for an unrelated extension coefficient. |
| **β** | Method-3 **risk-posture exponent** in 1/(1−α)^β (§3.5, §11.8) | §16.2 **scarcity-elasticity exponent** on (Q_crit/Q) (innovation) | A: 897–8, 5350 · B: 7350, 7353 | Same pattern as α. |
| **δ** | §16.1 **discount-rate decay constant** in r(t)=r₀·e^(−δt)+r_min | §10.3 proof **ε–δ neighborhood width** (standard analysis variable) | A: 7341 · B: 3520 | Plus: δ is **undefined on first use** at 7341 (prose names r₀, r_min, never δ). Plus LATENT: if M3 Path B adopts a Dixit–Pindyck δ (convenience yield), that's a THIRD δ. |
| **τ** | **scarcity threshold** τ_j (§1.8 line 485; §10.3 lines 3440–3546, with a local "throughout this theorem" note) | §5.4 **future time** in S(τ\|t₀) (line 1348) | A: 485, 3488 · B: 1348 | §10.3 disambiguates τ *locally*, then §5.4 re-overloads it for a different meaning — the worst kind: the document shows it knows the symbol is contested and reuses it anyway. |
| **E** | **externality-tail function** E(R,t) (§1.4, §16.1, §17) | §16.3 **extraction region** (spatial set) | A: 404, 7338, 7659 · B: 7362, 7365, 7368 | §16.3 disambiguates K-vs-C and V-vs-B in the SAME sentence but misses E(function)-vs-E(region). Also collides with the standard probability **expectation operator E[·]** (reader expectation). |
| **P** | **market price** P / P(t) (§1.3, §10.5, §14.1) | §10 **Premise labels** P1–P4 | A: 371, 3692, 6542 · B: 3335–3357, 3688–3712 | Within §10, "P" the price and "P1–P4" the premises sit paragraphs apart. Also §10.3 uses P1–P4 AGAIN for abstract cost-function *properties* (line 3482) — a third P-labelling. |
| **A** | **abundance** variable A(t) (§10.3, lines 3434–3552) | §10 **Assumption labels** A1–A4 | A: 3434ff · B: 3269, 3310ff | Abundance A and Assumption A1–A4 coexist within §10.3. Also §1.8 "Aⱼ" = commons category (third A). |
| **B** (bare) | **Accountability Bond** ($ quantity) | **"billion"** magnitude suffix in worked numbers ("55B BOE", "$942B") | A: 462, 6633 · B: 4241, 4533, 4605 | The billion-suffix B in §11 worked calcs sits next to the bond variable B. Sloppy in exactly the quantitative passages a referee reads closely. |

### 🟠 MED — case- or subscript-distinguished, or single-section-local (lower risk, worth a note)

| Glyph pair | A vs B | Locations |
|---|---|---|
| **r vs R** | discount rate r (§1.5, §14.1 Hotelling) vs resource R (argument) | 416, 6542 vs 327, 1459 |
| **s vs S** | integration dummy s in ∫r(s)ds vs substitutability S | 3585 vs 3577 |
| **m vs M** | externality growth exponent m vs divergence bound M (proof) | 3573 vs 3520 |
| **k vs K** | utility growth exponent k vs proof constant K | 3567 vs 3630 |
| **δ vs Δ** | ε–δ width δ vs change-operator Δ (ΔForeclosure_cost) | 3520 vs 3747 |
| **T vs t/t₀** | proof threshold time T vs time variable t | 3624 vs throughout |
| **c vs C vs 𝒞** | cost function c(A) vs cost component C/Cᵢ vs commons set 𝒞 (script) | 3440 vs 327 vs 327 |
| **V(x,t) vs V_option** | spatial value vs Method-3 option value | 7365 vs 889 |
| **C₁ vs B₁** | Foreclosure Cost C₁ (forward) vs Restitution Bond B₁ (backward) — subscript-1 carries *opposite* temporal valence | 1276 vs 1219 |
| **2%** | EPA SCC discount rate vs one of Weitzman's candidate rates | 5740 vs 6564 |
| **× (times)** | multiplication vs ratio-magnitude suffix ("33–122×") vs Cartesian product (ℝ×[t₀,∞)) | many |
| **→** | limit "approaches" vs function-domain map vs "yields" arrow | many |

### Units / undefined-notation issues (not collisions, same class of referee-risk)

- **log** — used in scarcity_multiplier `1+log(1+σ)×Hotelling_anchor`; worked value `log(101)≈4.6` is **natural log (ln 101≈4.615; log₁₀≈2.004)**, but **"log" is never defined as ln anywhere** in the document. (Lines 896, 4311, 4761, 5245.)
- **σ units** — defined as "commons-stock / sustainable-flow ratio" (line 892); a stock÷flow-rate ratio is **time-dimensioned**, yet σ is used as the dimensionless argument of `log(1+σ)`. Internal units inconsistency.

---

## PART 2 — MASTER SYMBOL REGISTRY (distinct symbol × meaning)

> Standard-notation column: ✓ = matches standard usage in the relevant literature; ⚠ = deviates from a strong standard convention (referee-risk); — = framework-specific/neutral. Items marked **VERIFY** need confirmation against the cited source (Part 4).

### Core framework quantities

| Glyph | Meaning | Units | Role/loc | Provenance | Std-notation | Collision |
|---|---|---|---|---|---|---|
| R | resource unit | — | D §1.1 (327) | — | — | (r vs R 🟠) |
| 𝒞 (script) | commons-territory set; R∈𝒞 | set | D §1.1 (327) | — | — | 🟢 (typographically distinguished from C) |
| Q, Q(t) | remaining in-situ stock | resource-class units | D §1.1 (327,334) | — | ⚠ Hotelling uses q=flow; Dasgupta–Heal use S=stock | 🟢 (disambiguated 377–399) |
| ρ | regeneration rate of stock | resource·time⁻¹ | D §1.1 (334) | — | — | — |
| S(t\|t₀), S_max | substitutability function; its ceiling | dimensionless [0,1] | D §1.2 (341–355) | — | ⚠ resource econ often uses S=stock | 🟢 (disambiguated vs Dasgupta–Heal) |
| λ | substitution rate (in S=S_max(1−e^(−λ(t−t₀)))) | time⁻¹ | D §1.2 (355) | — | ✓ | — |
| U(R,t,Q(t)) | stock-dependent utility flow | $·res⁻¹·time⁻¹ | D §1.3 (361) | — | — | 🟢 |
| ∂U/∂Q | marginal utility wrt stock (<0) | — | D §1.3 (368) | — | ✓ | — |
| P, P(t) | market price | $·res⁻¹ | u §1.3 (371) | — | ✓ | 🔴 vs Premises P1–P4 |
| E(R,t) | externality-tail flow | $·res⁻¹·time⁻¹ | D §1.4 (404) | — | ⚠ collides w/ expectation operator E[·] | 🔴 vs extraction region E (§16.3) |
| D(t,t₀), r(t), r₀, g(t) | discount factor; rate; initial rate; decline fn | (0,1]; rate; rate; — | D §1.5 (416) | Weitzman 2001 | ✓ | — |
| RCV(R,t₀) | Residual Commons Value (the integral) | $·res⁻¹ | D §1.6 (425) | — | — | 🟢 (acronym collisions noted 427–445) |
| B, B₁, B₂ | Accountability Bond; Restitution (backward); Foreclosure (forward) | $ | D §1.7, §2.1 (462,474) | Darity–Mullen 2020 (B₁); Hotelling/Hartwick (B₂) | — | 🔴 bare B vs "billion" suffix; 🟠 C₁ vs B₁ valence |
| CS, CSD | Cost Severance (=RCV−B); Cost Severance Damages (backward) | $ | D §1.7, §2.1 (465,474) | — | — | — |
| Aⱼ, τⱼ | commons category j; its scarcity threshold | —; category-dep | D §1.8 (485) | — | — | 🔴 τ (see Part 1); 🟠 A |
| CIT | Commons Inversion Test | — | D §1.8 (477) | — | — | — |
| IPG(R,t₀) | Intergenerational Pricing Gap = RCV/P | dimensionless (×) | D §3.2 (759) | — | — | — |
| S_threshold, existential substitutability gap | criticality threshold; S_max(ind)−S_max(exist) | dimensionless | D §1.9 (616); §13 (6380) | — | — | 🟢 (gap deliberately left unnamed, 6380) |

### Method-3 cluster (§3.5 / §11.5–11.8) — **coordinate with M3 Path-A/B decision**

| Glyph | Meaning | Units | Provenance | Std-notation | Collision |
|---|---|---|---|---|---|
| RCV_M3 | Method-3 estimate = V_option × scarcity_multiplier(σ) × irreversibility_premium(α) | $·res⁻¹ | Dixit–Pindyck 1994 | — | — |
| V_option | real-options option value | $ | Dixit–Pindyck 1994 **VERIFY** | — | 🟠 vs V(x,t) |
| σ | scarcity parameter = stock/flow ratio | "dimensionless" (but defined as a ratio → time-dimensioned; **units conflict**) | — | ⚠⚠ **In Dixit–Pindyck/Black–Scholes σ = VOLATILITY.** Reusing σ for a scarcity ratio inside an option-value formula is the single most reader-confusing choice. **VERIFY** | (units issue, Part 1) |
| α | irreversibility probability ∈[0,1] | dimensionless | — (aligned to IPCC tipping-point lit) | — | 🔴 vs §16.2 α |
| β | risk-posture exponent in 1/(1−α)^β | dimensionless | — | ⚠ finance β = CAPM systematic risk | 🔴 vs §16.2 β |
| scarcity_multiplier(σ) | 1+log(1+σ)×Hotelling_anchor | dimensionless | Hotelling 1931; Atkinson 1970 | — | log undefined (Part 1) |
| irreversibility_premium(α) | 1/(1−α)^β | dimensionless | Dixit–Pindyck 1994 | — | — |
| Hotelling_anchor | ~5%/yr Hotelling-rate proxy coefficient | ~rate | Hotelling 1931 | — | — |

### §10 proof apparatus

| Glyph | Meaning | loc | Std-notation | Collision |
|---|---|---|---|---|
| A1–A4 | Assumption labels (content differs per theorem) | 3269ff | ✓ (labels) | 🔴 vs abundance A; label-content-reuse across theorems |
| P1–P4 | Premise labels (also abstract properties in 10.3) | 3335ff, 3482 | ✓ | 🔴 vs price P |
| A, A(t) | abundance | 3434 | — | 🔴 |
| c(A), c₀, ξ | cost function; scale; curvature exponent (ξ≥1) | 3440–3523 | ✓ (ξ local-noted) | 🟢 (3488 note) |
| τ | scarcity threshold | 3440ff | — | 🔴 (re-overloaded §5.4) |
| ε, δ, M, A_ε | standard ε–δ analysis variables | 3499–3520 | ✓ | 🔴 δ vs §16.1 δ |
| U,U₀,k / E,E₀,m | utility & externality polynomial-growth bounds | 3567–3573 | ✓ | 🟠 m/M, k/K |
| S, s | substitutability map; integration dummy | 3577,3585 | ✓ | 🟠 |
| D(t,t₀), exp, r(s), r_∞, D_∞ | discount machinery; long-run rate; limit | 3585–3661 | ✓ | — |
| T, K | proof threshold time; proof constant | 3624–3630 | ✓ | 🟠 |
| SW, ∂SW/∂U | social welfare; marginal SW | 3704 | ✓ | — |
| P, Investment_cost, Path A/B, S* | price; substitute-investment cost; paths; substitute substitutability | 3692–3747 | ✓ | 🔴 P |
| Δ(…) | change operators (ΔForeclosure_cost, ΔOption_value, …) | 3747–3766 | ✓ | 🟠 δ/Δ |
| ∎ | QED | 3303ff | ✓ | — (but should NOT appear on Empirical Observations — see §10.1b item) |

### §16 extension symbols

| Glyph | Meaning | loc | Collision |
|---|---|---|---|
| r(t), r₀, **δ**, r_min | declining-rate machinery; **decay constant δ (UNDEFINED)** | 7341–7344 | 🔴 δ |
| S(t\|t₀,Q(t)), S_base(t), **α, β**, Q_critical | stock-dependent substitutability + **innovation coefficients α,β** | 7350–7356 | 🔴 α,β |
| SCS, x, **E (region)**, K, E∖K, C(x,t), V(x,t) | spatial cost severance machinery | 7362–7368 | 🔴 E; 🟢 K,V (noted 7365) |
| Σᵢ₌₁ⁿ, n, i, Cᵢ, C₁…Cₙ₊₁, Context | n-term generalization | 7548–7695 | 🟠 Cᵢ vs C(x,t) |

### Operators & units (catalogued; mostly standard)

∫ dt ds · × − + = > < ≥ ≤ ≈ ≫ → ⇒ ⇔ ∀ ∃ ∈ ⊆ ∖ ∞ ± ∂ ∎ ✓ ↑ — all standard. Units: $·res⁻¹·time⁻¹ (integrand), $·res⁻¹ (integral result), BOE, ton, tCO₂, mmBtu, Sm³, km², NOK, %, dimensionless. The "×" and "→" dual-roles are flagged 🟠 above.

---

## PART 3 — BIBLIOGRAPHY PROVENANCE GAPS

Symbol/formula provenance citations used inline but **NOT found as bibliography entries** (flag for the bib-consolidation session; do not fix here):

| Cited inline for | Work | Status |
|---|---|---|
| V_option / σ real-options provenance | **Brennan & Schwartz 1985** (commodity-investment real options) | ❌ ABSENT (cited 6706, 6719, 6723) |
| V_option option-pricing foundation | **Black–Scholes 1973** | ❌ ABSENT (cited 6723) |
| risk-vs-uncertainty | **Knight 1921** | ❌ ABSENT (cited 6895) |

Confirmed PRESENT (symbol-provenance-relevant): Solow 1956 (7981) & 1974 (7984); Weitzman 2001 (8026); Dixit & Pindyck 1994 (7807); Hotelling 1931 (7855); Hartwick 1977 (7834); Dasgupta & Heal 1979 (7801); Atkinson 1970 (7741); Cobb & Douglas 1928 (7777); Arrow & Fisher 1974 (7738); Henry 1974 (7840); Pindyck 1978 (7945) & 2008 (7948); Pigou 1920 (7942); Nordhaus & Boyer 2000 (7915); Stern 2007 (7993); Royden 1988 (7966); Folland 1999 (7822).

*(Note: Solow 1956 is currently cited only at §3.5 line 917 — the misattribution item in the separate correctness sweep. If that swaps to Solow 1974, the Solow 1956 entry may be orphaned.)*

---

## PART 4 — STANDARD-NOTATION DEVIATIONS NEEDING EXTERNAL VERIFICATION

The biggest referee-risk is not the internal collisions but **deviation from strong cross-literature conventions** in the option-value formula. Verify each against the cited source before deciding rename vs. keep-with-note:

1. **σ = scarcity ratio vs. σ = volatility (Dixit–Pindyck, Black–Scholes).** In every real-options / option-pricing text σ is the volatility of the underlying. Our σ is a stock/flow scarcity ratio inside an option-value product. A finance-literate referee will misread it on sight. **VERIFY** Dixit–Pindyck notation; recommend rename (e.g. ς or "scar" or a descriptive subscript).
2. **δ = discount-rate decay (§16.1) vs. δ = convenience yield/payout (Dixit–Pindyck).** **VERIFY**; relevant if M3 Path B introduces a DP δ.
3. **β = risk-posture exponent vs. β = CAPM systematic risk.** Lower risk (no CAPM nearby) but worth a note.
4. **E = externality vs. E[·] = expectation operator.** Pervasive; the §16.3 E-as-region makes it worse.
5. **α = irreversibility probability** — non-standard but not in conflict with a dominant convention; OK to keep with a definition.

---

## NEXT STEPS (proposed, not executed)

1. **Resolve each 🔴 collision**: rename to eliminate (preferred — e.g. §16.2 innovation α,β → distinct letters; §16.3 extraction-region E → Ω or 𝓔; bond B vs "billion" → spell out "billion") OR explicit local-notation note where coexistence is unavoidable.
2. **Define on first use**: δ (§16.1); log = ln (§3.5).
3. **Coordinate the Method-3 σ/α/β decisions with the M3 Path-A/B direction** (don't rename twice).
4. **Build the reader-facing Notation section** as a curated view of Part 2.
5. **Hand Part 3 bib gaps to the bib-consolidation session.**
