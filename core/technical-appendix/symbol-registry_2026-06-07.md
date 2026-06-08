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
| η_S(A) | supply elasticity (→0 as A→τ⁺) | 3455 | ✓ (η=elasticity standard) | 🟢 (unique glyph) |
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

## PART 4 — STANDARD-NOTATION DEVIATIONS (VERIFIED 2026-06-07 against cited sources)

Verified by a standard-notation agent against Black–Scholes (Columbia/Haugh), Dixit–Pindyck (NBER w12486, MIT Pindyck lectures, Princeton UP), Hotelling. Confidence per row.

| Symbol | Standard meaning (source) | Framework use | Deviation | Risk | Decision |
|---|---|---|---|---|---|
| **σ** | **Volatility of the underlying** — universal in Black–Scholes & Dixit–Pindyck (HIGH conf.) | scarcity ratio *inside* the cited option-value product | **direct conflict** | **HIGH — dismissal-grade** | **RENAME** (Path-A) → ς / κ / descriptive. *M3-coupled: dissolves under Path B if proper DP σ=volatility is adopted.* |
| **δ** | **Convenience yield / payout rate** in Dixit–Pindyck (HIGH conf.) | §16.1 discount-rate decay constant (undefined on first use) | direct conflict (latent) | MED → HIGH if Path B adds DP δ | **RENAME now → κ** + define on first use. *M3-independent (§16.1).* |
| **β** | CAPM systematic risk + D–P fundamental-quadratic root (HIGH conf.) | risk-posture exponent in 1/(1−α)^β | partial | MED | note or rename → ψ. *M3-coupled.* |
| **α** | no dominant conflicting convention; ∈[0,1] reads naturally (MED–HIGH) | irreversibility probability (M3) | none (external) | LOW ext. / MED internal | **keep** M3 α; rename the §16.2 innovation-α instead. |
| **E** | **Expectation operator E[·]** (HIGH conf.) | externality fn E(R,t) + §16.3 extraction *region* | partial→direct | MED–HIGH | **RENAME region → Ω**; consider fn → ℰ/X. *M3-independent.* |
| **r** | interest/discount rate — Hotelling (HIGH) | discount/interest rate | none | LOW | keep (preserve r-vs-R case discipline). |
| **Q, S** | Hotelling q=flow; Dasgupta–Heal S=stock (HIGH) | Q=stock; S=substitutability (deliberate redefinitions) | partial (intentional) | LOW | keep — disambiguation already present & adequate; reproduce in reader Notation section. |
| **log** | `log(101)≈4.6` ⇒ natural log (HIGH — arithmetic) | unspecified-base log | ambiguity | LOW–MED | **write ln**, or define "log ≡ ln" once. |

**Verified bottom line:** σ is the one dismissal-grade problem (rename-blocking, but M3-coupled — Path B may vindicate it). δ is rename-now (D–P payout glyph; pre-empts the Path-B second-δ). β and E are real second-tier (rename-or-strong-note). log→ln is trivial but checkable arithmetic a referee will run. α/r/Q/S are defensible with their existing notes.

---

## PART 5 — REMEDIATION PLAN (proposed; ratify before applying)

Free Greek letters (unused anywhere in the TA, per the completeness sweep): γ ζ θ ι κ μ ν π φ χ ψ ω (capitals aside). Used: α β δ Δ ε η λ ξ ρ σ Σ τ.

### Batch I — M3-INDEPENDENT (apply on ratification; survives either Path-A/B outcome)

| # | Collision | Fix | Locations |
|---|---|---|---|
| I-1 | §16.1 δ (decay) vs §10.3 ε–δ; undefined; pre-empts Path-B DP-δ | rename δ → **κ**; define "κ = decay constant" on first use | 7341, 7344 |
| I-2 | §16.3 E (extraction region) vs E(R,t) externality + E[·] | rename region E → **Ω** (and E∖K → Ω∖K) + note | 7362, 7365, 7368 |
| I-3 | §16.2 innovation α,β vs Method-3 α,β | rename §16.2 α→**ζ**, β→**ω** (keep Method-3 α,β) + note | 7350, 7353, 7356 |
| I-4 | log base unspecified | define **"log ≡ ln (natural logarithm)"** once at first use; verify worked values | 896 (+4311, 4761, 5245 unchanged) |
| I-5 | bare B vs "billion" suffix | spell out "billion" in worked numbers ("55 billion BOE") | §11 numeric passages |
| I-6 | §10 A1–A4 (Assumptions) vs A(t) abundance; P1–P4 (Premises) vs P price | add a one-line §10 local-notation note distinguishing labels from variables (no rename — labels entrenched) | §10.3 head |
| I-7 | registry completeness | add η_S (3455) ✓done; note integration dummies s (§10.3) / u (§16.1) | registry only |

### Batch II — M3-COUPLED (HOLD for the Path-A/B direction decision)

| # | Symbol | If Path A (keep σ/α/β architecture) | If Path B (DP premium) |
|---|---|---|---|
| II-1 | **σ** (dismissal-grade) | RENAME σ (scarcity) → **ς** or descriptive; reserve σ for nothing | likely DISSOLVES — adopt proper DP σ=volatility; our scarcity term goes away |
| II-2 | **β** (M3 risk-posture exponent) | rename → **ψ** or strong note | replaced by DP exponent structure |
| II-3 | **α** (M3 irreversibility) | keep (defensible) | replaced by DP δ in Path B |

### Sequencing
1. Apply Batch I on author ratification (M3-independent, low-risk renames).
2. Resolve M3 Path-A/B → then apply Batch II against the final §3.5/§11.8.
3. Build the reader-facing Notation section from Part 2 AFTER Batch I + II land.
4. Hand Part 3 bib gaps (Brennan–Schwartz, Black–Scholes, Knight) to the bib-consolidation session.

**Note:** the verified σ finding is a *third* reason to resolve the M3 Path-A/B question — the direction determines whether σ must be renamed (Path A) or is vindicated as proper volatility (Path B).
