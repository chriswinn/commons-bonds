# Technical Appendix — Master Symbol Registry & Notation Audit (2026-06-07)

**Status: SYNCED to merged TA (`origin/main` fd12275) 2026-06-09.** Built from a 7-agent exhaustive catalog of every symbol in `TechnicalAppendix_v2.0.0.html` (lines 1–8041), consolidated + collision-swept + standard-notation-checked. Internal source-of-truth; the reader-facing Notation section (`manuscript/back-matter/symbol-registry.html`) is curated FROM this.

> **SYNC BANNER (2026-06-09, refactor-bib-consolidation session).** Every Batch I + Batch II rename and the closeout notation changes are now **verified APPLIED in the merged TA** (grep-confirmed, HTML-entity forms): δ-decay→**κ** (`&kappa;`×2, defined on first use L7299); §16.3 region E→**Ω** (`&Omega;`×6, L7320 w/ collision note); §16.2 innovation α→**ζ**, β→**ω** (`&zeta;`/`&omega;`×4, L7308, noted distinct from M3 α); σ→**ς** (`&sigmaf;`, 0 literal-σ stragglers); **log→ln** (0 residual `log(`); **V_option→V_market** (28/0); **τ overload RESOLVED** (`S(τ|t₀)`=0; substitutability written `S(t | t₀)`); **β fully removed** (0); **§10 A1–A4/P1–P4 relabeled to roman (i)–(iv) + (a)–(d)** (0 old labels; 12 `Assumption (i…)`), so the A/P collision is resolved by RENAME, not note. Remaining genuinely-open items routed to WS3 standard-notation pass: E externality-fn vs E[·] expectation; bare B vs "billion" suffix; M vs "million"; Theorem 10.3 (i)–(iv) used for both clauses + assumptions. The 2 residual `&delta;` (L3522) are the standard ε–δ analysis variable — correct, not a stray decay-δ.

**Method:** 7 parallel catalog agents (one per line-range), each recording every symbol-occurrence (glyph · meaning · role · section · line · units · provenance) + within-range collisions + existing disambiguation notes. This file consolidates to distinct (symbol × meaning) pairs and flags cross-section collisions.

**Legend:** Role D=definition site, u=use. Collision severity: 🔴 HIGH (same glyph, genuinely different quantity, reader-confusing) · 🟠 MED (case/subscript-distinguished or one-section-local) · 🟢 OK (already disambiguated in text, or standard).

---

## PART 1 — COLLISIONS REQUIRING ACTION (the headline)

### 🔴 HIGH — same glyph, genuinely different quantity, NOT disambiguated

| Glyph | Meaning A | Meaning B | Locations | Note |
|---|---|---|---|---|
| **α** | Method-3 **irreversibility probability** ∈[0,1] (§3.5, §11.5–11.8) | §16.2 **scarcity effect on innovation incentives** (coefficient >0) | A: 893–4, 4295ff, 5063ff · B: 7305ff | ✅ **RESOLVED** — §16.2 innovation-α renamed → **ζ** (`&zeta;`, noted distinct from M3 α at L7308). M3 α kept. |
| **β** | Method-3 **risk-posture exponent** in 1/(1−α)^β (§3.5, §11.8) | §16.2 **scarcity-elasticity exponent** on (Q_crit/Q) (innovation) | A: — · B: 7305ff | ✅ **RESOLVED** — M3-β DROPPED (Path A; no free exponent); §16.2-β renamed → **ω** (`&omega;`). bare β = 0 in merged TA. |
| **δ** | §16.1 **discount-rate decay constant** in r(t)=r₀·e^(−δt)+r_min | §10.3 proof **ε–δ neighborhood width** (standard analysis variable) | A: → κ (7296,7299) · B: 3522 | ✅ **RESOLVED** — decay δ renamed → **κ**, **defined on first use** (L7299). Only the standard ε–δ proof variable remains (L3522), which is correct. Path-B third-δ pre-empted. |
| **τ** | **scarcity threshold** τ_j (§1.8 line 485; §10.3, with a local "throughout this theorem" note) | ~~§5.4 future time in S(τ\|t₀)~~ (RESOLVED) | A: 485, 3488 | ✅ **RESOLVED** — the §5.4 future-time overload fixed to `S(t\|t₀)`; `S(τ\|t₀)` = 0 in merged TA. τ is now scarcity-threshold only. |
| **E** | **externality-tail function** E(R,t) (§1.4, §16.1, §17) | ~~§16.3 extraction region~~ → **Ω** (RESOLVED) | A: 404, 7338, 7659 · Ω: 7317,7320,7323 | ⚠️ **PARTIAL** — region E→**Ω** applied (`&Omega;`×6, L7320 note). **STILL OPEN (→WS3):** E(R,t) function vs standard expectation operator **E[·]** (reader-expectation collision). |
| **P** | **market price** P / P(t) (§1.3, §10.5, §14.1) | ~~§10 Premise labels P1–P4~~ (RESOLVED) | A: 371, 3692, 6542 | ✅ **RESOLVED** — §10 Premise labels relabeled to roman **(i)–(iv)** (and cost-function properties → **(a)–(d)**); P1–P4 = 0 in merged TA. P is market-price only. |
| **A** | **abundance** variable A(t) (§10.3, lines 3434–3552) | ~~§10 Assumption labels A1–A4~~ (RESOLVED) | A: 3434ff | ✅ **RESOLVED** — §10 Assumption labels relabeled to roman **(i)–(iv)**; A1–A4 = 0 in merged TA. Abundance A(t) and §1.8 commons-category Aⱼ remain (subscript-distinguished, benign). |
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
| B̂_M2 | Method-2 **realized-Bond reading** (observed internalization: fund accumulation + taxation capture + restitution paid + restraint exercised), per unit of extraction. A **strict lower bound on RCV (RCV ≥ B̂_M2), NOT an RCV estimator** — the two value-estimators are M1 + M3 (§3.6). Hat = "reading/estimate of," distinguishing it from the posted-instrument B of Def 1.7. | $·res⁻¹ | D §3.4 (~849; added 2026-06-10 reverse-CSD merge) | — | ✓ (hat = empirical estimate, standard) | 🟢 (hat distinguishes from posted-B; encoded `B&#770;`; author considered alternatives + KEPT the hat 2026-06-10) |
| CS, CSD | Cost Severance (=RCV−B); Cost Severance Damages (backward) | $ | D §1.7, §2.1 (465,474) | — | — | — |
| CSD_M3 | backward Method-3 composite: CSD_M3 = V_market × scarcity_multiplier(ς) × irreversibility_premium(α), with V_market in its **backward reading** (extinguished optionality / foregone service flow), ς the scarcity at the extraction moment, α the **realized** irreversibility. Carries the ex-post vs ex-ante valuation fork the framework exposes rather than settles. | $·res⁻¹ | D §5.5 (1397; added 2026-06-10 §5.5 reverse-method upgrade) | quasi-option value (Arrow–Fisher 1974; Henry 1974), run on realized parameters | — | 🟢 (subscript-disambiguated within the CS/CSD family) |
| Aⱼ, τⱼ | commons category j; its scarcity threshold | —; category-dep | D §1.8 (485) | — | — | 🔴 τ (see Part 1); 🟠 A |
| CIT | Commons Inversion Test | — | D §1.8 (477) | — | — | — |
| IPG(R,t₀) | Intergenerational Pricing Gap = RCV/P | dimensionless (×) | D §3.2 (759) | — | — | — |
| S_threshold, existential substitutability gap | criticality threshold; S_max(ind)−S_max(exist) | dimensionless | D §1.9 (616); §13 (6380) | — | — | 🟢 (gap deliberately left unnamed, 6380) |

### Method-3 cluster (§3.5 / §11.5–11.8) — **✅ PATH A applied 2026-06-08 (σ→ς; β dropped; log→ln)**

| Glyph | Meaning | Units | Provenance | Std-notation | Collision |
|---|---|---|---|---|---|
| RCV_M3 | Method-3 estimate = V_market × scarcity_multiplier(ς) × irreversibility_premium(α) | $·res⁻¹ | quasi-option value (Arrow–Fisher 1974; Henry 1974) — NOT DP investment-timing, per §3.5 line 901 | — | — |
| V_market | resource's own market / underlying value (abundance baseline; renamed from V_option under Path A — the premium emerges from the ς/α weights, not the base) | $ | Arrow–Fisher 1974 / Henry 1974 | — | 🟠 vs V(x,t) |
| **ς** (final sigma) | M3 scarcity parameter (accessible-recoverable stock vs long-horizon demand; reserves-to-production-grounded) | dimensionless | — | **σ→ς applied 2026-06-08 (Path A)** to escape the σ=volatility read; ς is sigma-adjacent (scarcity mnemonic) | ✅ resolved (old-σ stragglers cleaned by M3) |
| α | irreversibility probability ∈[0,1] | dimensionless | — (aligned to IPCC AR6 SPM B.5; Bernhardt & Palmer 2011) | — | ✅ resolved (§16.2 α→ζ via I-3, now merged) |
| ~~β~~ | **DROPPED from M3 (Path A, 2026-06-08):** irreversibility_premium = 1/(1−α), no free exponent (§3.5 line 901). M3-side β collision gone. | — | — | — | ✅ resolved |
| scarcity_multiplier(ς) | 1+ln(1+ς)×Hotelling_anchor | dimensionless | Hotelling 1931; Atkinson 1970 | log→ln applied §3.5 | ✅ |
| irreversibility_premium(α) | 1/(1−α) (no free exponent — Path A) | dimensionless | quasi-option value (Arrow–Fisher 1974; Henry 1974) | — | — |
| Hotelling_anchor | ~5%/yr Hotelling-rate proxy coefficient | ~rate | Hotelling 1931 | — | — |

### §10 proof apparatus

| Glyph | Meaning | loc | Std-notation | Collision |
|---|---|---|---|---|
| (i)–(iv) [Assumptions] | Assumption labels, roman (relabeled off A1–A4) | 3269ff | ✓ (labels) | ✅ resolved vs abundance A |
| (i)–(iv) [Premises] / (a)–(d) [cost-fn properties] | Premise + property labels, roman (relabeled off P1–P4) | 3335ff, 3482 | ✓ | ✅ resolved vs price P |
| A, A(t) | abundance | 3434 | — | 🔴 |
| c(A), c₀, ξ | cost function; scale; curvature exponent (ξ≥1) | 3440–3523 | ✓ (ξ local-noted) | 🟢 (3488 note) |
| η_S(A) | supply elasticity (→0 as A→τ⁺) | 3455 | ✓ (η=elasticity standard) | 🟢 (unique glyph) |
| τ | scarcity threshold | 3440ff | — | ✅ resolved (§5.4 future-time overload fixed → `S(t\|t₀)`) |
| ε, δ, M, A_ε | standard ε–δ analysis variables | 3499–3522 | ✓ | ✅ resolved (§16.1 decay δ→κ; only the standard proof δ remains) |
| U,U₀,k / E,E₀,m | utility & externality polynomial-growth bounds | 3567–3573 | ✓ | 🟠 m/M, k/K |
| S, s | substitutability map; integration dummy | 3577,3585 | ✓ | 🟠 |
| D(t,t₀), exp, r(s), r_∞, D_∞ | discount machinery; long-run rate; limit | 3585–3661 | ✓ | — |
| T, K | proof threshold time; proof constant | 3624–3630 | ✓ | 🟠 |
| SW, ∂SW/∂U | social welfare; marginal SW | 3704 | ✓ | — |
| P, Investment_cost, Path A/B, S* | price; substitute-investment cost; paths; substitute substitutability | 3692–3747 | ✓ | ✅ resolved (Premise P1–P4 relabeled roman; P = price only) |
| Δ(…) | change operators (ΔForeclosure_cost, ΔOption_value, …) | 3747–3766 | ✓ | 🟠 δ/Δ |
| ∎ | QED | 3303ff | ✓ | — (but should NOT appear on Empirical Observations — see §10.1b item) |

### §16 extension symbols

| Glyph | Meaning | loc | Collision |
|---|---|---|---|
| r(t), r₀, **κ**, r_min | declining-rate machinery; **decay constant κ** (defined on first use, L7299) | 7296–7299 | ✅ (δ→κ) |
| S(t\|t₀,Q(t)), S_base(t), **ζ, ω**, Q_critical | stock-dependent substitutability + **innovation coefficients ζ,ω** (local to §16.2, distinct from M3 α) | 7305–7311 | ✅ (α,β→ζ,ω) |
| SCS, x, **Ω (region)**, K, Ω∖K, C(x,t), V(x,t) | spatial cost severance machinery | 7317–7323 | ✅ (E-region→Ω, noted L7320) |
| Σᵢ₌₁ⁿ, n, i, Cᵢ, C₁…Cₙ₊₁, Context | n-term generalization | 7548–7695 | 🟠 Cᵢ vs C(x,t) |

### Operators & units (catalogued; mostly standard)

∫ dt ds · × − + = > < ≥ ≤ ≈ ≫ → ⇒ ⇔ ∀ ∃ ∈ ⊆ ∖ ∩ ∞ ± ∂ ∎ ✓ ↑ — all standard (∩ added 2026-06-10: range-intersection in §3.6 "(M1 ∩ M3 convergence)"). Units: $·res⁻¹·time⁻¹ (integrand), $·res⁻¹ (integral result), BOE, ton, tCO₂, mmBtu, Sm³, km², NOK, %, dimensionless. The "×" and "→" dual-roles are flagged 🟠 above.

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
| **σ→ς** | **Volatility of the underlying** — universal in Black–Scholes & Dixit–Pindyck (HIGH conf.) | scarcity ratio | (was) direct conflict | (was) dismissal-grade | ✅ **DONE — σ→ς applied + stragglers cleaned.** Literal-σ = 0 in merged TA; ς present as `&sigmaf;`. |
| **δ** | **Convenience yield / payout rate** in Dixit–Pindyck (HIGH conf.) | §16.1 discount-rate decay constant | direct conflict (latent) | (was) MED→HIGH | ✅ **DONE — renamed → κ, defined on first use (L7299).** Path-B third-δ pre-empted. Only the standard ε–δ proof variable remains (L3522). |
| **β** | CAPM systematic risk + D–P fundamental-quadratic root (HIGH conf.) | (was) risk-posture exponent | — | — | ✅ **RESOLVED — DROPPED from M3 (Path A)**; no free exponent. |
| **α** | no dominant conflicting convention; ∈[0,1] reads naturally (MED–HIGH) | irreversibility probability (M3) | none (external) | LOW ext. / MED internal | **keep** M3 α; rename the §16.2 innovation-α instead. |
| **E** | **Expectation operator E[·]** (HIGH conf.) | externality fn E(R,t) + §16.3 extraction *region* | partial→direct | MED–HIGH | ✅ region → **Ω** DONE (`&Omega;`×6). ⚠️ **STILL OPEN → WS3:** externality fn E(R,t) vs expectation E[·] (consider fn → ℰ/X). |
| **r** | interest/discount rate — Hotelling (HIGH) | discount/interest rate | none | LOW | keep (preserve r-vs-R case discipline). |
| **Q, S** | Hotelling q=flow; Dasgupta–Heal S=stock (HIGH) | Q=stock; S=substitutability (deliberate redefinitions) | partial (intentional) | LOW | keep — disambiguation already present & adequate; reproduce in reader Notation section. |
| **log→ln** | `log(101)≈4.6` ⇒ natural log (HIGH — arithmetic) | unspecified-base log | ambiguity | LOW–MED | ✅ **DONE — ln applied throughout; 0 residual `log(` in merged TA** (`ln(`×5). |

**Verified bottom line (updated 2026-06-09 — all applied except the E-function residual):** σ→ς ✅ done (literal-σ=0); δ→κ ✅ done (defined L7299); β ✅ resolved (M3 drop + §16.2→ω); E-region→Ω ✅ done; log→ln ✅ done (0 residual). **The single remaining standard-notation item is the externality function E(R,t) vs the expectation operator E[·]** — routed to the WS3 standard-notation pass (propose→ratify→apply). α/r/Q/S remain defensible with their existing notes.

---

## PART 5 — REMEDIATION PLAN (proposed; ratify before applying)

Free Greek letters (unused anywhere in the TA, per the completeness sweep): γ ζ θ ι κ μ ν π φ χ ψ ω (capitals aside). Used: α β δ Δ ε η λ ξ ρ σ Σ τ.

### Batch I — M3-INDEPENDENT (✅ I-1/I-2/I-3 APPLIED + MERGED to `origin/main` fd12275 2026-06-09; I-6 SUPERSEDED by roman relabel; I-4 done; I-5 deferred→WS3)

| # | Collision | Fix | Locations |
|---|---|---|---|
| I-1 | §16.1 δ (decay) vs §10.3 ε–δ; undefined; pre-empts Path-B DP-δ | rename δ → **κ**; define "κ = decay constant" on first use | 7341, 7344 |
| I-2 | §16.3 E (extraction region) vs E(R,t) externality + E[·] | rename region E → **Ω** (and E∖K → Ω∖K) + note | 7362, 7365, 7368 |
| I-3 | §16.2 innovation α,β vs Method-3 α,β | rename §16.2 α→**ζ**, β→**ω** (keep Method-3 α,β) + note | 7350, 7353, 7356 |
| ~~I-4~~ | log base unspecified | ✅ **DONE via Path A (M3 session):** ln applied in §3.5; residual `log(` at TA 4314 pending M3 cleanup. | 896/904/4761/5245 ✓; 4314 pending |
| ~~I-5~~ | bare B vs "billion" suffix | **DEFERRED:** ~50 occurrences, all sourced numbers owned by the provenance session (§6/§11/§15); coordinate with that session rather than unilaterally edit its lines. NOT applied. | §6/§11/§15 |
| ~~I-6~~ | §10 A1–A4 (Assumptions) vs A(t) abundance; P1–P4 (Premises) vs P price | ✅ **SUPERSEDED — closeout went further than the proposed note:** labels RENAMED to roman (i)–(iv) (Assumptions/Premises) + (a)–(d) (cost-function properties). A1–A4/P1–P4 = 0; collision removed by rename, not note. | §10 |
| I-7 | registry completeness | add η_S (3455) ✓done; note integration dummies s (§10.3) / u (§16.1) | registry only |

### Batch II — M3-COUPLED — ✅ RESOLVED by Path A (2026-06-08, M3 session)

| # | Symbol | Resolution (Path A applied) |
|---|---|---|
| II-1 | **σ → ς** | ✅ applied in §3.5 (final sigma; reserves-to-production-grounded). Residual old-σ stragglers pending M3 cleanup: TA 4295, 4309, 4314, 4332, 4338, 6732. |
| II-2 | **β** | ✅ **DROPPED from M3** (not renamed to ψ) — irreversibility_premium = 1/(1−α), no free exponent (§3.5 line 901). M3-side β collision gone. |
| II-3 | **α** | ✅ kept; α-dominance narrative reframed to empirically-grounded + theorem-backed (§3.5 line 901) — substantially addresses correctness item #6 (verify the ~line 922 header still / no longer says "Sensitivity finding"). |

**Cross-branch merge dependency:** ✅ **RESOLVED.** The notation-sweep §16/§10 Batch I edits and the M3 §3.5 Path-A edits both landed in the TA closeout merged to `origin/main` fd12275 (2026-06-09). Both M3's α and §16.2's ζ-rename now coexist in one tree; the collision is gone (grep-verified).

### Sequencing
1. ✅ Batch I applied + merged (fd12275).
2. ✅ M3 Path-A resolved; Batch II applied + merged.
3. **▶ IN PROGRESS (this session):** reader-facing Notation section built from Part 2 → `manuscript/back-matter/symbol-registry.html`.
4. **▶ IN PROGRESS (this session):** Part 3 bib gaps (Brennan–Schwartz, Black–Scholes, Knight) folded into `research/literature/bibliography.md` (Step B).

**Note:** the verified σ finding is a *third* reason to resolve the M3 Path-A/B question — the direction determines whether σ must be renamed (Path A) or is vindicated as proper volatility (Path B).

---

## PART 6 — RESERVE POOL (unused letters + standard-notation baggage)

**Added 2026-06-08** (author request, during the M3 Path-A σ→ς decision). Purpose: a vetted pool of symbols to draw from as the book adds quantities, so future choices avoid both *internal* collisions (Part 1) and *reader-expectation* collisions.

**Governing principle (the σ=volatility lesson generalized):** "unused in this corpus" ≠ "free of meaning a reader brings." Before adopting any symbol, check it against (a) the used-symbol inventory (Part 2) for an internal collision, AND (b) the standard-notation baggage below for a reader-expectation collision. A symbol can be internally free yet still mislead — exactly the §3.5 σ problem (internally "scarcity," but every finance-literate reader reads volatility).

### Greek — unused in the corpus, with reader-expectation baggage flags

| Letter | Standard-notation baggage (reader expectation) | Use-cleanliness |
|---|---|---|
| **ι** (iota) | rarely used as a variable; "an iota" = a tiny amount | ✓ cleanest |
| **ζ** (zeta) | Riemann zeta function; damping ratio | ~ low |
| **ψ** (psi) | wavefunction; digamma function | ~ low (registry's suggested target for a retired M3 β) |
| **γ** (gamma) | Euler–Mascheroni constant; Lorentz factor; Γ gamma function; skewness | ⚠ moderate |
| **ν** (nu) | frequency; degrees of freedom; Poisson ratio | ⚠ moderate |
| **χ** (chi) | chi-squared; Euler characteristic | ⚠ moderate |
| **ω** (omega) | angular frequency; sample space; Omega ratio (finance) | ⚠ moderate |
| **φ** (phi) | golden ratio; **standard-normal density φ(·)**; potential; angle | ⚠ moderate–high |
| **θ** (theta) | angle; generic "the parameter"; **option Greek (time decay)** | ✗ avoid in option contexts |
| **π** (pi) | **the constant 3.14159 (universal)**; profit (econ); inflation (macro); Π product operator | ✗ avoid |
| **μ** (mu) | mean; micro- prefix; **drift in Black–Scholes / Dixit–Pindyck** | ✗ avoid (esp. option contexts) |
| **κ** (kappa) | curvature; option vega-adjacent | **TAKEN** — §16.1 decay constant (δ→κ, Batch I I-1) |

- **ς** (final sigma) — collision-free in the corpus (TA + chapters: 0 uses) and the recommended target for the §3.5 σ-scarcity rename (Part 4/5). Baggage: it *looks like* σ, so it only partially escapes the volatility-read — acceptable because its only association is sigma-adjacent (scarcity mnemonic), but **descriptive naming is the zero-baggage alternative.** Was omitted from the original used/free inventory (it's a sigma glyph-variant); record it here as RESERVED-for-M3-scarcity pending the Path-A apply.
- **Capitals** (Γ Θ Λ Ξ Π Φ Ψ Ω) are mostly free but inherit the same baggage as their lowercase forms (Π = product, Σ = sum [TAKEN], Ω = ohms/sample-space, Φ = normal CDF). Λ, Ξ unused-and-low-baggage if a capital is needed.

### Latin — guidance (not a full inventory)

Most single lowercase Latin letters are already in service as variables (Part 2: r, s, m, k, c, n, i, t, T, x, g, plus the framework set R, Q, S, P, E, B, C, D, U, A, V, K). Apparently-free and low-baggage: **f, h, j, w, y, z** (lowercase) and **G, H, J, L, M, N, W, X, Y, Z** (capitals) — **verify against Part 2 before use** (e.g., M is used as a proof bound and as a "million" suffix; E as expectation/region/externality). **Default for new quantities: a descriptive or subscripted name** (e.g., `S_RP`, `Cure_cost`) rather than a bare letter — descriptive names carry zero reader-expectation baggage, which is why they are the safe fallback whenever a clean single letter is unavailable.

> **Coordination note:** this Part 6 was appended from the `ta-m3-pathb` branch (the registry currently lives on `origin/main`). It is an end-append (low merge-conflict). Reconcile with the notation-sweep session's copy when branches merge; if that session has already advanced the registry, graft this section in.

---

## PART 7 — READER-FACING CANONICAL SYMBOL LIST (deduplicated; scan-verified complete)

**Added 2026-06-09 (back-matter consolidation).** Part 2 is the exhaustive per-section AUDIT
catalog (same glyph may recur across section tables). This Part 7 is the **deduplicated,
reader-facing canonical list** — each distinct quantity ONCE, grouped, with its canonical meaning.
The reader-facing `manuscript/back-matter/symbol-registry.html` is generated from THIS table
(`build.py gen-notation`). **Scan-verified complete:** `build.py scan-symbols` confirms the TA's
Greek set (Δ Σ Ω α δ ε ζ η κ λ ξ ρ ς τ ω — 15) is fully covered here with no gaps and no stale
entries; the Latin framework variables and compound/subscripted forms are included below.

| Group | Symbol | Meaning | Units |
|---|---|---|---|
| Core quantities | R | resource unit | — |
| Core quantities | 𝒞 | commons-territory set (R ∈ 𝒞) | set |
| Core quantities | Q, Q(t) | remaining in-situ stock | resource-class units |
| Core quantities | S(t\|t₀), S_max | substitutability function; its ceiling | dimensionless [0,1] |
| Core quantities | U(R,t,Q(t)) | stock-dependent utility flow | $·res⁻¹·time⁻¹ |
| Core quantities | P, P(t) | market price | $·res⁻¹ |
| Core quantities | E(R,t) | externality-tail flow (deterministic; not the expectation operator E[·]) | $·res⁻¹·time⁻¹ |
| Core quantities | D(t,t₀), r(t), r₀ | discount factor; discount rate; initial rate | (0,1]; rate; rate |
| Core quantities | RCV(R,t₀) | Residual Commons Value (the integral) | $·res⁻¹ |
| Core quantities | B, B₁, B₂ | Accountability Bond; Restitution Bond (backward); Foreclosure Bond (forward) | $ |
| Core quantities | B̂_M2 | Method-2 realized-Bond reading (observed internalization per unit of extraction); a strict lower bound on RCV (RCV ≥ B̂_M2), not an RCV estimator; the hat marks "reading/estimate of," distinct from the posted instrument B | $·res⁻¹ |
| Core quantities | CS, CSD | Cost Severance (= RCV − B); Cost Severance Damages (backward-looking) | $ |
| Core quantities | CSD_M3 | backward Method-3 composite: V_market × scarcity_multiplier(ς) × irreversibility_premium(α), with V_market in its backward reading (extinguished optionality / foregone service flow) and α the realized irreversibility | $·res⁻¹ |
| Core quantities | IPG(R,t₀) | Intergenerational Pricing Gap (= RCV / P) | dimensionless |
| Core quantities | CIT | Commons Inversion Test (the discovery method) | — |
| Core quantities | Cᵢ, C₁…Cₙ₊₁ | indexed cost components admitted via the Four Gates | $ |
| Core quantities | SCS, Ω | spatial cost severance (∫ over Ω∖K); Ω = extraction region | $; set |
| Core quantities | Aⱼ, τⱼ | commons category j; its scarcity threshold | —; category-dep |
| Parameters | ρ | regeneration rate of stock | resource·time⁻¹ |
| Parameters | λ | substitution rate (in S = S_max(1 − e^(−λ(t−t₀)))) | time⁻¹ |
| Parameters | ς | Method-3 scarcity parameter (reserves-to-production-grounded) | dimensionless |
| Parameters | α | Method-3 irreversibility probability ∈ [0,1] | dimensionless |
| Parameters | ξ | cost-function curvature exponent (ξ ≥ 1) | dimensionless |
| Parameters | η_S(A) | supply elasticity (→ 0 as A → τ⁺) | dimensionless |
| Parameters | τ | scarcity threshold | category-dep |
| Parameters | κ | discount-rate decay constant (§16.1; r(t) = (r₀ − r_min)·e^(−κt) + r_min) | time⁻¹ |
| Parameters | ζ, ω | §16.2 innovation-suppression coefficients (local to §16.2; distinct from M3 α) | dimensionless |
| Method-3 | RCV_M3 | Method-3 estimate = V_market × scarcity_multiplier(ς) × irreversibility_premium(α) | $·res⁻¹ |
| Method-3 | V_market | resource's own market / underlying value (abundance baseline) | $ |
| Method-3 | scarcity_multiplier(ς) | 1 + ln(1 + ς) × Hotelling_anchor | dimensionless |
| Method-3 | irreversibility_premium(α) | 1 / (1 − α) | dimensionless |
| Method-3 | Hotelling_anchor | ≈ 5%/yr Hotelling-rate proxy coefficient | ~rate |
| Operators & proof | Σ | summation operator | — |
| Operators & proof | Δ | change operator (ΔForeclosure_cost, ΔOption_value, …) | — |
| Operators & proof | ∂U/∂Q | partial derivative (marginal utility wrt stock; < 0) | — |
| Operators & proof | A, A(t), c(A), c₀ | abundance; cost function; cost scale (Theorem 10.3) | — |
| Operators & proof | ε, δ | ε–δ analysis neighborhood variables (Theorem 10.3) | — |
| Operators & proof | M, K, T | proof divergence bound; proof constant; threshold time (local to §10.3) | — |
| Operators & proof | s | integration dummy (∫ r(s) ds) | — |
| Operators & proof | (i)–(iv); (a)–(d) | enumerated assumption/premise labels; cost-function-property labels (§10) | — |
| Operators & proof | ∎ | QED (end of proof) | — |
