# Commons Bonds — Phase 2 Deeper-Dive Rigor Pass: Theorem E.3 (Abundance Masking) — Circular-Proof Audit

**Version:** 1.0.0
**Date:** 2026-04-29
**Protocol applied:** `tools/commons_bonds_rigor_protocol_v2.3.0.md` — academic-rigor depth audit per author direction 2026-04-29: *"the math formulas and proofs have to stand up to academic rigor or I don't have a book."* Tests applied: premise enumeration; logical derivation (does the proof actually derive the theorem from premises, or invoke the test that operationalizes the theorem's claim?); circular-reasoning detection; edge case analysis; collision check against established resource-economics + tipping-point + scarcity-pricing literature; citation discipline; falsifiability; domain of applicability; counterexample resistance; **circular-proof-resolution decision** (Option α delete-redundant vs Option β substantive-derivation vs Option γ mutual-derivation framing).

**Author direction triggering this pass (2026-04-29 by Chris Winn):** *"Go ahead and start either E.3 or E.5 the other session is still spinning on E.1"* — sibling theorem-rigor session is running E.1 audit (~3 hours in at this pass start); E.3 picked over E.5 because (a) circular-proof concern is more contained than over-specified-scope concern; (b) audit task is structural-fix-driven with clear option-space; (c) E.3 doesn't depend on E.1 outcome.

**Scope:** Phase 2 academic-rigor depth audit on **Theorem E.3 (Abundance Masking)** as stated at [Tech Appendix v1.0.0 §10 lines 3270-3276](manuscript/technical-appendix/TechnicalAppendix_v1.0.0.html). Phase 1 §8.2 + E.4 rigor pass §16.3 flagged: *"E.3 (Abundance Masking) — circular proof; full formalization needed; ~700-900 lines."*

**Status:** **SUPPLEMENTARY to canonical Insight #42** (other-session E.3 audit at `tools/rigor-passes/archive/commons_bonds_rigor_pass_2026-04-29_phase2_theorem_e3_abundance_masking_v1.0.0.md`, RATIFIED 2026-04-29 on main, commit `dcafa45`). Subject-collision resolution per author direction 2026-04-29: both audits independently arrived at the same load-bearing findings (circular proof; S → τ notation collision; functional-form derivation; domain-restriction; commodity-economics + supply-elasticity lineage). The other session's audit was ratified first (Insight #42); this rigor pass is preserved as supplementary perspective with distinctive contribution: **CIT-as-operational-corollary reframing** (§13.4 + §13.5 — explicit clarifying paragraph at Definition A.8 + backward-pointer at E.3 statement establishing E.3 as analytic theorem and CIT as operational corollary). The CIT-corollary structural refactor strengthens framework's logical organization beyond the canonical #42 verdict. Original PROPOSED Insight #54 retired in favor of canonical #42. Tech Appendix HTML edit timing: BATCH into Phase 3 v2.0.0 rebuild per shared open question with Insights #35 + #38 + #40 + #41 + #42 + #47 + #48 + #49 + #50 + #51 + #52 + #53. **No separate Insight # claimed** for this supplementary rigor pass — it operates under #42's umbrella.

**Author:** Chris Winn

**Recommended verdict (preview):** **OPTION β + γ COMBINED (substantive derivation from resource-economics primitives, framed as analytic theorem with CIT as operational corollary)** — RECOMMENDED. The current proof is **circular**: E.3 asserts the abundance-masking phenomenon and "proves" it "by construction of the Commons Inversion Test" — but CIT (Definition A.8) is the methodological protocol that operationalizes the very phenomenon E.3 claims as theorem. Top-tier academic peer review will flag the circularity on first read.

The substantive content of E.3 is correct + derivable. The repair path: **derive E.3 from standard resource-economics cost-function primitives** (Hotelling 1931 rent dynamics + Pindyck 1978 stock-dependent cost behavior + Dasgupta-Heal 1979 scarcity-tipping-point analysis + Barnosky et al. 2012 *Nature* ecological tipping-point literature). This produces a genuine theorem with substantive derivation independent of CIT. CIT then becomes the **operational corollary** — the methodological protocol that detects the abundance-masking phenomenon E.3 establishes analytically.

Three concrete enhancements: (1) **explicit premise enumeration** (P1 monotonicity in abundance; P2 abundance limit C → 0; P3 convexity in scarcity ratio; P4 nonlinear growth near scarcity threshold); (2) **substantive derivation** invoking Hotelling rent dynamics + scarcity-tipping-point cost-function structure + Lebesgue-style limit analysis; (3) **CIT-as-operational-corollary reframing** — restate the relationship between E.3 (analytic theorem) and CIT (operational protocol) such that CIT's validity follows from E.3, eliminating the circularity.

The substance survives the restructure: the abundance-masking phenomenon is preserved; CIT's operational role is preserved; the framework's commons-categories apparatus is preserved. What changes is the **logical relationship** between E.3 and CIT — E.3 derives the phenomenon analytically; CIT operationalizes detection of the phenomenon.

---

## §1. Phase 2 executive summary

### §1.1 What was tested

E.3 currently states (Tech Appendix v1.0.0 line 3273):

> *Theorem E.3 (Abundance Masking)*
>
> For any cost tier C, abundance level A, and scarcity threshold S: if A ≫ S then C appears negligible until A approaches S, at which point C becomes visible and grows nonlinearly.

With proof (line 3276):

> *Proof:* By construction of the Commons Inversion Test. When A ≫ S, the marginal cost of depleting A appears zero because each unit withdrawn from a very large stock has negligible price impact. As A → S, the cost function transitions from approximately linear to exponential as scarcity effects dominate — this is the standard behavior of resource cost functions near depletion thresholds, demonstrated formally by Hotelling's rent dynamics and empirically by commodity price spikes near supply constraints. The asteroid mining scenarios (Section F) demonstrate this for an extreme case: asteroid iron (A ≫ S) has RCV ≈ 0; lunar helium-3 near the fusion-deployment threshold (A approaching S) has high existential substitutability gap. ∎

The audit tests:
1. **Premise enumeration** — what are the formal premises of E.3?
2. **Logical derivation** — does "by construction of the Commons Inversion Test" derive E.3, or invoke the test that operationalizes E.3's claim?
3. **Circular-reasoning detection** — is the proof structurally circular?
4. **Edge case analysis** — limit cases (A → ∞; A → S; A < S; transition zone behavior).
5. **Collision check** — adjacent literature (Hotelling 1931; Pindyck 1978; Dasgupta-Heal 1979; tipping-point ecological economics).
6. **Citation discipline** — load-bearing references.
7. **Falsifiability** — under what conditions does the claim fail?
8. **Domain of applicability** — where applies; where not.
9. **Counterexample resistance** — try constructing counterexamples.
10. **Circular-proof-resolution decision** — Option α (delete) vs Option β (substantive derivation) vs Option γ (mutual-derivation framing).

### §1.2 Phase 2 outcomes

| Test | Verdict | Note |
|---|---|---|
| Premise enumeration | **WEAK** | Four implicit premises (monotonicity in abundance; abundance limit; convexity in scarcity ratio; nonlinear growth near threshold); none stated as numbered assumptions |
| Logical derivation | **FAIL — circular** | "By construction of the Commons Inversion Test" invokes the methodological protocol that operationalizes the very phenomenon E.3 asserts as theorem. Structurally circular |
| Circular-reasoning detection | **CONFIRMED CIRCULAR** | CIT Definition A.8 says: *"the cost is latent when Aⱼ ≫ Sⱼ and becomes visible as Aⱼ → Sⱼ."* E.3 says: *"if A ≫ S then C appears negligible until A approaches S, at which point C becomes visible."* These are the same statement; CIT cannot prove E.3 |
| Edge cases | **STRONG** | A → ∞ (negligible cost; correct); A → S (nonlinear growth; correct); A < S (resource-collapse regime; not addressed but defensible on Hotelling-extension grounds) |
| Collision check | **WEAK** | Hotelling 1931 cited informally; Pindyck 1978 + Dasgupta-Heal 1979 + Barnosky et al. 2012 *Nature* ecological tipping-points not invoked or cited |
| Citation discipline | **WEAK** | Hotelling rent dynamics referenced informally; no formal citations to load-bearing literature |
| Falsifiability | **STRONG** | Falsifiable in principle: a cost tier that does NOT exhibit abundance-masking behavior would falsify the universal-quantifier claim |
| Domain of applicability | **ADEQUATE** | "Any cost tier C, abundance level A, scarcity threshold S" — claims universal applicability across framework's cost-tier landscape; should be explicit about domain limits |
| Counterexample resistance | **MEDIUM-WEAK** | Standard cost functions exhibit abundance-masking; but **constant-marginal-cost regimes** (e.g., manufactured goods with stable supply chains) violate the claim — need scope statement |

**Aggregate verdict: OPTION β + γ COMBINED — restructure with substantive derivation from resource-economics primitives + reframe CIT as operational corollary.**

The substantive content is correct + derivable. The proof structure is circular and must be rewritten. Repair work is derivation-substitution + CIT-relationship reframing, not abandonment of the theorem.

### §1.3 Three concrete repair enhancements

**ENHANCEMENT 1: Explicit premise enumeration (Assumptions P1–P4)**

State the load-bearing premises as numbered assumptions:

> **P1 (Monotonicity in abundance):** Cost tier C(A, S) is monotonically non-increasing in A: ∂C/∂A ≤ 0 for A > S. (More abundance → lower or equal per-unit cost.)
>
> **P2 (Abundance limit):** lim_{A → ∞} C(A, S) = 0. (In the abundance limit, per-unit cost approaches zero.)
>
> **P3 (Convexity in scarcity ratio):** Cost tier C(A, S) is convex in (S/A): ∂²C/∂(S/A)² ≥ 0 for S/A ∈ (0, 1]. (Cost-function curvature near scarcity threshold.)
>
> **P4 (Nonlinear growth near scarcity threshold):** lim_{A → S⁺} ∂C/∂A = -∞ OR ∂C/∂A grows without bound as A → S⁺ from above. (Cost gradient diverges near scarcity threshold.)

These premises are derivable from standard resource-economics cost-function primitives (per Pindyck 1978 *JPE*; Dasgupta-Heal 1979; Hotelling 1931 rent dynamics extended to cost-function form).

**ENHANCEMENT 2: Substantive derivation (replacing circular "By construction of CIT")**

Replace the current proof with a substantive derivation invoking standard resource-economics + tipping-point cost-function structure:

> **Proof.** By P1 + P2, lim_{A → ∞} C(A, S) = 0; combined with monotonicity, for any ε > 0 ∃ A* > S such that C(A, S) < ε for all A > A*. Hence when A ≫ S, C ≈ 0 ("negligible").
>
> By P3 + P4, the cost gradient ∂C/∂A grows without bound as A → S⁺. Equivalently, the scarcity-ratio (S/A) → 1 as A → S⁺, and cost-function convexity in (S/A) produces the nonlinear-growth pattern.
>
> The transition from C ≈ 0 (at A ≫ S) to C → large (at A → S⁺) is therefore guaranteed by P1–P4 + standard real-analysis limit theorems (cf. Royden 1988 §4.4; Folland 1999 §2.4).
>
> **Lineage:** P1–P2 (monotonicity + abundance limit) follow from standard resource-economics cost-function primitives (Pindyck 1978 *JPE* "The Optimal Exploration and Production of Nonrenewable Resources"; Dasgupta & Heal 1979 *Economic Theory and Exhaustible Resources*). P3–P4 (convexity + nonlinear growth near threshold) follow from Hotelling 1931 *JPE* rent dynamics extended to cost-function form, and from ecological tipping-point literature (Barnosky et al. 2012 *Nature* "Approaching a state shift in Earth's biosphere"; Lenton et al. 2008 *PNAS* "Tipping elements in the Earth's climate system"). ∎

**ENHANCEMENT 3: CIT-as-operational-corollary reframing**

Restate the relationship between E.3 (analytic theorem) and CIT (operational protocol) to eliminate circularity:

Add to Tech Appendix §B Definition A.8 (CIT definition) an explicit forward-pointer:

> *(Per Theorem E.3 (Abundance Masking) at §10, the abundance-masking phenomenon is established analytically from resource-economics cost-function primitives. CIT operationalizes detection of the phenomenon: stripping away dimensions of abundance and observing which cost tiers transition from C ≈ 0 to C → large is the empirical signature of E.3's analytic prediction. CIT's validity as a discovery methodology follows from E.3's analytic establishment of the abundance-masking phenomenon.)*

Add to Tech Appendix §10 E.3 statement (after the restructured proof) a backward-pointer:

> *(Operational corollary: CIT (Definition A.8) is the methodological protocol that detects the abundance-masking phenomenon established analytically here. CIT's validity follows from E.3.)*

Together, these clarify: E.3 is the analytic theorem; CIT is the operational protocol; the relationship is theorem → operational corollary, not circular.

### §1.4 Why Option β + γ (not α)

**Option α (delete E.3 as redundant with CIT) — REJECTED.**

The abundance-masking phenomenon is a **substantive analytic claim** about cost-function behavior near scarcity thresholds — derivable from standard resource-economics primitives. Deleting E.3 as redundant with CIT would lose the analytic claim's status. CIT alone is a methodological protocol; without E.3, the protocol's validity is unanchored.

The framework would lose:
- The analytic justification for why CIT works (without E.3, CIT is "we look for hidden costs by stripping away abundance" — without theoretical foundation).
- The connection to Hotelling rent dynamics + scarcity-pricing literature (currently weak; Option β strengthens; deletion eliminates).
- The "5 theorems" pedagogical structure (already weakened by Phase 2 #3.4 [E.2] Option A relabel; further loss compounds).

**Option β (substantive derivation) + Option γ (mutual-derivation framing) — RECOMMENDED.**

Combined, β + γ:
- Preserve E.3 as a genuine theorem (substantive derivation from resource-economics primitives).
- Resolve the circularity (CIT becomes operational corollary, not load-bearing premise).
- Strengthen the framework's academic-citation infrastructure (Pindyck 1978; Dasgupta-Heal 1979; Hotelling 1931; Barnosky et al. 2012 + Lenton et al. 2008).
- Maintain "5 theorems" structure (E.1 + E.3 + E.4 + E.5 + Empirical Observation E.2 — though E.2 categorization is per Phase 2 #3.4 still pending).

### §1.5 What changes vs what doesn't

**What changes:**
- Premise enumeration (P1–P4 stated).
- Proof restructured: circular "By construction of CIT" → substantive derivation from resource-economics primitives + Hotelling + tipping-point literature.
- CIT Definition A.8 + E.3 statement: add forward/backward pointers clarifying analytic-theorem-vs-operational-corollary relationship.
- Citations: Hotelling 1931 (already in bibliography); Pindyck 1978; Dasgupta-Heal 1979; Barnosky et al. 2012 *Nature*; Lenton et al. 2008 *PNAS* added.

**What does NOT change:**
- The substantive abundance-masking phenomenon claim.
- CIT's role as discovery methodology.
- E.3's chapter / case-study cross-references (continue to refer to "E.3" by number).
- The framework's cost-tier-categorical-abundance apparatus.
- Any other theorem in E.1 / E.2 / E.4 / E.5.

The framework's load-bearing claims survive intact; the logical structure (E.3 derives from primitives; CIT operationalizes) replaces circularity.

### §1.6 Integration of four parallel-session-audit findings (added 2026-04-29 per author direction)

Parallel-session E.3 audit surfaced four load-bearing findings absent from this audit's original v1.0.0 [PROPOSED]. Per author direction, they are integrated:

**Finding F1 — S vs τ notation collision (most important).** E.3 currently uses **S** for scarcity threshold (*"For any cost tier C, abundance level A, and scarcity threshold S..."*). But the framework reserves **S** for the **substitutability function** (Tech Appendix §B Definition A.2; load-bearing in RCV integrand + E.4 + E.5). Same letter, two different concepts across theorems. Critical reader confusion: a quant reader encountering "scarcity threshold S" in E.3 alongside "substitutability function S(t)" in adjacent theorems pattern-matches to a single concept and finds incoherence.

**Repair (Enhancement 4):** Rename E.3's scarcity threshold **S → τ** (Greek tau). τ is unused elsewhere in the framework + reads naturally as a "threshold" parameter in resource-economics convention (Pindyck 1978; Dasgupta-Heal 1979 use threshold-style Greek letters for stock-state parameters). All E.3 statements + proof + Definition A.8 (CIT) reframing must use τ instead of S for scarcity threshold. terms_index entry for CIT also requires the rename.

**Finding F2 — Commodity-economics + supply-elasticity lineage.** Original audit's collision-check (§8) cited tipping-point ecological-economics lineage (Barnosky et al. 2012; Lenton et al. 2008) but missed the parallel commodity-economics + supply-elasticity lineage that addresses abundance-masking from the price-discovery angle:
- **Marshall, Alfred. 1890.** *Principles of Economics*. London: Macmillan. — foundational supply-elasticity treatment; near-vertical supply curve at scarcity threshold.
- **Hamilton, James D. 2009.** "Causes and Consequences of the Oil Shock of 2007–08." *Brookings Papers on Economic Activity* (Spring): 215-261. — empirical commodity-shock literature on abundance-to-scarcity transition price dynamics.
- **Kilian, Lutz. 2009.** "Not All Oil Price Shocks Are Alike: Disentangling Demand and Supply Shocks in the Crude Oil Market." *American Economic Review* 99(3): 1053-1069. — supply-elasticity + scarcity-threshold empirical methodology.

These are **complementary**, not competing, with the tipping-point lineage. Tipping-point literature establishes nonlinear dynamics near critical thresholds in ecological systems; commodity-economics literature establishes the same pattern in priced-market systems via supply-elasticity collapse. Both lineages support P3 + P4 (convexity in scarcity ratio + nonlinear growth near threshold).

**Repair (integrated into Enhancement 2 substantive derivation):** Cite both lineages in restructured proof — Marshall 1890 + Hamilton 2009 + Kilian 2009 alongside Barnosky 2012 + Lenton 2008. Bibliography expansion absorbs both lineages.

**Finding F3 — Specific functional form c(A) = c₀ · (τ/(A−τ))^α as concrete realization.** Original audit's P1–P4 premises specify abstract conditions (monotonicity; abundance limit; convexity; nonlinear-growth-near-threshold) but didn't provide a concrete functional form satisfying all four. Parallel audit surfaces the form:

> **c(A, τ) = c₀ · (τ/(A−τ))^α** where c₀ > 0, α > 0, A > τ.

Properties:
- Monotonically decreasing in A: ∂c/∂A = −c₀ · α · τ · (τ/(A−τ))^(α-1) · 1/(A−τ)² < 0 for A > τ ✓ (P1)
- Abundance limit: as A → ∞, (τ/(A−τ)) → 0, so c → 0 ✓ (P2)
- Convex in (τ/(A-τ)) ratio: ∂²c/∂(τ/(A-τ))² ≥ 0 for α ≥ 1 ✓ (P3)
- Nonlinear growth near threshold: as A → τ⁺, (τ/(A−τ)) → ∞, so c → ∞ ✓ (P4)

The α parameter calibrates curvature: α = 1 gives linear-in-(τ/(A−τ)) growth; α > 1 gives super-linear divergence near threshold (matches commodity-shock empirical patterns per Hamilton 2009 + Kilian 2009).

**Repair (integrated as supplementary derivation example in §13.2):** Add c(A, τ) = c₀ · (τ/(A−τ))^α as concrete realization of P1–P4 — gives readers a working specification rather than only abstract premises. Connects to commodity-economics literature (specific form is recognizable from supply-elasticity + Hotelling-rent-near-exhaustion economics).

**Finding F4 — Four counterexample classes drive expanded domain restriction.** Original audit's counterexample resistance (§12) caught only constant-marginal-cost regimes (manufactured goods with elastic supply). Parallel audit surfaces three additional counterexample classes that violate E.3's universal-quantifier claim:

| Counterexample class | Premise violated | Domain implication |
|---|---|---|
| **Constant-marginal-cost** (manufactured goods; elastic supply) | P1 (∂C/∂A = 0; flat) + P2 (C → c₀, not 0) | Original audit caught |
| **Renewable resources** (regeneration faster than extraction) | A doesn't decrease monotonically; abundance-masking pattern N/A because A self-restores | NEW — must exclude |
| **Information goods** (non-rival; A doesn't decrease as units consumed) | Abundance never approaches scarcity threshold; concept doesn't apply | NEW — must exclude |
| **Network-effect goods** (value increases with adoption; ∂U/∂A > 0) | Inverts P1 — utility increases as more consumed; opposite of scarcity-utility relationship | NEW — must exclude |

**Repair (integrated into Enhancement 3 domain-of-applicability):** Expand domain restriction to exclude four counterexample classes:

> *Domain of applicability:* This theorem applies to **non-renewable, rival, anti-network-effect, non-constant-marginal-cost** cost tiers c(A, τ) on the domain A > τ where c is non-constant in A and satisfies P1–P4 (i.e., standard exhaustible-resource cost-function behavior per Pindyck 1978; Dasgupta-Heal 1979; Hotelling 1931 + commodity-shock empirical patterns per Hamilton 2009; Kilian 2009; Marshall 1890 supply-elasticity lineage). Out of scope: (a) constant-marginal-cost regimes (elastic-supply manufactured goods); (b) renewable resources (where A self-restores faster than depletion); (c) information goods (non-rival; A doesn't decrease through consumption); (d) network-effect goods (where ∂U/∂A > 0 inverts the scarcity-utility relationship).

This restricts E.3's universal-quantifier claim to its actual structural domain — non-renewable extraction with rivalry + standard scarcity-utility relationship.

### §1.7 Updated enhancement count: four enhancements (was three)

After integration of parallel-session findings, the recommended verdict is **four concrete enhancements** (not three):

1. **Premise enumeration P1–P4** (per §13.1; updated to use τ for scarcity threshold).
2. **Substantive derivation** (per §13.2; cites Pindyck 1978 + Dasgupta-Heal 1979 + Hotelling 1931 + Marshall 1890 + Hamilton 2009 + Kilian 2009 + Barnosky et al. 2012 + Lenton et al. 2008; includes specific functional form c(A, τ) = c₀ · (τ/(A−τ))^α per F3).
3. **Domain-of-applicability statement** (per §13.3; expanded to exclude four counterexample classes per F4).
4. **NEW: S → τ notation rename** (per F1) — eliminate notation collision between E.3's scarcity threshold and framework's substitutability function.

Plus: CIT-relationship reframing (§13.4 + §13.5) + bibliography expansion (§13.6).

---

## §2. Question + scope

### §2.1 Triggering articulation

[Phase 1 full framework audit §8.2](commons_bonds_rigor_pass_2026-04-29_full_framework_audit_phase1_v1.0.0.md):

> *"Theorem E.3 (Abundance Masking) ... PASS screening pending Phase 2 academic-rigor depth audit on circular-proof concern."* [Quote updated 2026-04-30 per double-Theorem cleanup.]

[Phase 2 Theorem E.4 Integral Convergence rigor pass §16.3](commons_bonds_rigor_pass_2026-04-29_phase2_theorem_e4_integral_convergence_v1.0.0.md):

> *"E.3 (Abundance Masking) — circular proof; full formalization needed; ~700-900 lines."*

Phase 2 (this rigor pass) executes the screening-recommended audit at academic-rigor depth.

### §2.2 What this audit produces

For pass/fail academic-rigor gate at top-tier journals (AER, QJE, JPE, JEEM, JPubE, *Journal of Economic Theory*, *Resource and Energy Economics*) and academic-trade hybrid presses, E.3's proof must meet the following standards:

- All premises stated as numbered assumptions.
- Proof derives from premises + previously-established results — not from the methodological protocol that operationalizes the theorem's claim.
- Edge cases handled with explicit limit analysis.
- Established results invoked by name where load-bearing (Hotelling 1931 rent dynamics; Pindyck 1978 cost functions; Dasgupta-Heal 1979; tipping-point literature).
- Falsifiability conditions explicit.

This audit produces:
1. Per-test verdict.
2. Circular-reasoning detection + Option α/β/γ analysis.
3. Concrete repair recommendations.
4. Recommended formal restatement (premises + derivation).
5. CIT-relationship reframing.

### §2.3 Pass/fail gate framing

Per author direction 2026-04-29: pass/fail gate on academic rigor for theorems. Circular-proof concerns are categorical disqualifiers at top-tier journals — a theorem cannot prove itself by invoking the test that operationalizes its claim. Option β + γ combined repair the circularity at the proof-structure level.

### §2.4 What this pass does NOT cover

- **Phase 2 deeper-dive on theorems E.1, E.2, E.5, Renewable Imperative** — separate rigor passes (sibling session in progress for E.1; E.2 [PROPOSED] per Phase 2 #3.4; E.5 + Renewable Imperative pending).
- **Theorem E.4 (Integral Convergence)** — already RATIFIED Insight #40.
- **CIT methodological audit** — separate territory (CIT's operational protocol details not re-litigated; only its logical relationship to E.3 is reframed).
- **Commons-categories framework** — separate territory.
- **Case-by-case empirical validation** — Block 4 numerical territory.
- **Pre-publication external review** — Insight #39 OPEN; downstream gate.

---

## §3. Methodology

### §3.1 Academic-rigor depth audit framework

For each test below, the audit (a) reads E.3's current statement + proof + adjacent CIT context (Tech Appendix §B Definition A.8); (b) tests against academic-peer-review standards including circular-proof detection; (c) produces verdict; (d) flags concrete repair work.

### §3.2 Tests applied

1. **Premise enumeration** — implicit assumptions identified.
2. **Logical derivation** — proof structure analyzed for circularity vs valid derivation.
3. **Circular-reasoning detection** — explicit comparison of E.3's claim and CIT's definition for structural identity.
4. **Edge case analysis** — limit cases (A → ∞; A → S; A < S).
5. **Collision check** — adjacent resource-economics + tipping-point literature.
6. **Citation discipline** — load-bearing references.
7. **Falsifiability** — explicit conditions for falsification.
8. **Domain of applicability** — universal-quantifier scope analysis.
9. **Counterexample resistance** — construct counterexamples under stated/restructured premises.
10. **Circular-proof-resolution decision** — Option α/β/γ analysis.

### §3.3 What the audit does NOT do

- Does NOT verify the empirical abundance-masking phenomenon across additional cost tiers (Block 4 territory).
- Does NOT redesign CIT's operational protocol.
- Does NOT replace pre-publication external review.

---

## §4. Current state — close reading

### §4.1 Current text (Tech Appendix v1.0.0 lines 3270-3276, verbatim)

> **Theorem E.3 (Abundance Masking)**
>
> For any cost tier C, abundance level A, and scarcity threshold S: if A ≫ S then C appears negligible until A approaches S, at which point C becomes visible and grows nonlinearly.
>
> *Proof:* By construction of the Commons Inversion Test. When A ≫ S, the marginal cost of depleting A appears zero because each unit withdrawn from a very large stock has negligible price impact. As A → S, the cost function transitions from approximately linear to exponential as scarcity effects dominate — this is the standard behavior of resource cost functions near depletion thresholds, demonstrated formally by Hotelling's rent dynamics and empirically by commodity price spikes near supply constraints. The asteroid mining scenarios (Section F) demonstrate this for an extreme case: asteroid iron (A ≫ S) has RCV ≈ 0; lunar helium-3 near the fusion-deployment threshold (A approaching S) has high existential substitutability gap. ∎

### §4.2 Adjacent context — CIT Definition A.8 (Tech Appendix v1.0.0 line 496-499)

> **Definition A.8 (Commons Inversion Test — Methodological Protocol)**
>
> To identify hidden cost tiers in any extraction transaction, systematically strip away dimensions of abundance and observe which costs become visible at each dimension. Formally: for a cost tier Cᵢ, commons category Aⱼ, and scarcity threshold Sⱼ, the cost is latent when Aⱼ ≫ Sⱼ and becomes visible as Aⱼ → Sⱼ. The test proceeds by hypothetically removing each commons category in sequence...

### §4.3 The structural identity problem

E.3 claim:

> *"For any cost tier C, abundance level A, and scarcity threshold S: if A ≫ S then C appears negligible until A approaches S, at which point C becomes visible and grows nonlinearly."*

CIT Definition A.8 statement:

> *"the cost is latent when Aⱼ ≫ Sⱼ and becomes visible as Aⱼ → Sⱼ."*

**These are the same statement.** E.3 just adds the "grows nonlinearly" qualifier and quantifies over "any cost tier C." Definition A.8 is exactly what E.3 claims as theorem.

The proof "By construction of the Commons Inversion Test" therefore amounts to: *"E.3 is true because we have a test that detects E.3's phenomenon."* That's circular. CIT doesn't prove the phenomenon; CIT operationalizes detection of the phenomenon.

### §4.4 Initial reading observations

- **The circularity is structural, not a phrasing issue.** E.3 and CIT Definition A.8 make the same claim about the same phenomenon. The proof can't appeal to CIT to establish E.3 because CIT presupposes E.3's phenomenon as its operational target.

- **The substantive content of E.3 is derivable.** The abundance-masking phenomenon follows from standard resource-economics cost-function primitives (monotonicity in abundance + abundance limit + convexity in scarcity ratio + nonlinear growth near threshold). This is a real theorem with a real derivation.

- **The proof's secondary content is sound.** "When A ≫ S, marginal cost appears zero because each unit withdrawn from a very large stock has negligible price impact" — this is correct standard cost-function behavior, derivable from monotonicity + abundance limit. The asteroid iron / lunar helium-3 examples are correct illustrations.

- **The "Hotelling's rent dynamics" reference is informal.** Hotelling 1931 establishes the price-path of exhaustible resource extraction (P(t) = P(0) · e^{r·t} along Hotelling rule); extending to cost-function-near-threshold form is straightforward but currently unspecified.

- **No formal citations.** Hotelling 1931 referenced informally ("Hotelling's rent dynamics"); no Pindyck / Dasgupta-Heal / Barnosky / Lenton citations.

- **"For any cost tier C" is a strong universal quantifier.** Some cost tiers may not exhibit abundance-masking (e.g., constant-marginal-cost manufacturing). Domain-of-applicability needs scope statement.

---

## §5. Test 1 — Premise enumeration

### §5.1 Implicit premises in current text

| # | Implicit premise | Where it appears | Status |
|---|---|---|---|
| 1 | C(A, S) monotonically non-increasing in A | "marginal cost appears zero... each unit from very large stock" | Implicit; not numbered |
| 2 | lim_{A → ∞} C(A, S) = 0 (or near 0) | "appears negligible" | Implicit |
| 3 | C(A, S) convex in (S/A) | "transitions from approximately linear to exponential" | Implicit; informal |
| 4 | ∂C/∂A → -∞ as A → S⁺ | "grows nonlinearly... scarcity effects dominate" | Implicit; informal |
| 5 | "Standard behavior of resource cost functions" | proof reference | Implicit Pindyck/Dasgupta-Heal lineage |
| 6 | Hotelling rent dynamics applicable | proof reference | Cited informally |

### §5.2 Verdict

**WEAK.** Six implicit premises; four are load-bearing for the abundance-masking claim (P1–P4 in restructure). Top-tier journals require explicit premise enumeration; current text would not pass JEEM / JPubE referee review.

### §5.3 Repair recommendation

State as numbered Assumptions P1–P4 per §13.1 below. Each premise cites where in the framework's broader apparatus or in adjacent literature it is established.

---

## §6. Test 2 — Logical derivation + Test 3 — Circular-reasoning detection

### §6.1 Current proof structure analysis

The proof has two layers:

**Layer 1: "By construction of the Commons Inversion Test."**

This is the load-bearing proof move. It says: *"E.3 is true because the Commons Inversion Test is constructed to detect E.3's phenomenon."* But CIT is defined (Definition A.8) precisely in terms of the abundance-masking phenomenon E.3 asserts. So Layer 1 reduces to: *"E.3 is true because we have a test that operationalizes E.3."* This is **circular**.

**Layer 2: "When A ≫ S, marginal cost appears zero because each unit withdrawn from a very large stock has negligible price impact... As A → S, the cost function transitions from approximately linear to exponential as scarcity effects dominate — this is the standard behavior of resource cost functions near depletion thresholds, demonstrated formally by Hotelling's rent dynamics."**

This is the substantive content. It invokes:
- Standard cost-function behavior (monotonicity + abundance limit).
- Hotelling rent dynamics (informal).
- Empirical commodity price spikes (anecdotal).

Layer 2 by itself, properly formalized, would be a valid derivation. But Layer 1 frames Layer 2 as merely "explaining why CIT works" — Layer 2 is positioned as supporting context for Layer 1's circular move, not as the standalone derivation.

### §6.2 Verdict

**FAIL — circular.** The proof's load-bearing move (Layer 1) is circular: invoking CIT (which operationalizes E.3's phenomenon) to prove E.3. Layer 2 contains substantive content that, properly formalized, would be a valid derivation; but Layer 2 is currently positioned as supporting context, not as the proof itself.

### §6.3 Repair recommendation

**Promote Layer 2 to standalone proof; eliminate Layer 1 reference to CIT.** Layer 2's content (cost-function behavior + Hotelling rent dynamics + scarcity-tipping-point) is exactly the substantive derivation the theorem needs. Reformulate as standalone derivation per §13.2 below.

CIT becomes the operational corollary: once E.3 is established analytically, CIT is the methodological protocol that detects E.3's phenomenon empirically.

### §6.4 Aggregate verdict on derivation + circularity

The current proof is **structurally circular at the top level**, but contains **substantive derivable content beneath the circular framing**. Repair by promoting the substantive content to standalone derivation status.

---

## §7. Test 4 — Edge case analysis

### §7.1 Edge case 1: A → ∞

Per P2 (abundance limit): C(A, S) → 0. Combined with monotonicity (P1), for any ε > 0, ∃ A* > S such that C(A, S) < ε for all A > A*. **STRONG** — well-established cost-function limit behavior.

Asteroid iron example (Tech Appendix §F): A ≫ S → RCV ≈ 0. Correct.

### §7.2 Edge case 2: A → S⁺

Per P3 + P4 (convexity + nonlinear growth): C(A, S) → large (possibly unbounded). The cost gradient ∂C/∂A grows without bound. **STRONG** — well-established near-threshold cost-function behavior.

Lunar helium-3 example: A approaching S → high existential substitutability gap. Correct.

### §7.3 Edge case 3: A < S (resource collapse regime)

Not addressed in current text. If abundance falls below scarcity threshold, the cost function may be undefined (no stable extraction equilibrium) or follow different dynamics (collapse-regime literature; Diamond 2005 *Collapse*; Tainter 1988 *The Collapse of Complex Societies*).

The framework's intended scope is A > S (scarcity-approaching, not scarcity-crossed). Recommended: add domain restriction A ≥ S in Domain of Applicability.

### §7.4 Edge case 4: constant-marginal-cost regimes

Some cost tiers may exhibit constant marginal cost over a wide range (e.g., manufactured-goods with stable supply chains; service-economy outputs with elastic supply). Such tiers do NOT exhibit abundance-masking — abundance level doesn't change cost behavior because the cost function is flat.

The "For any cost tier C" universal-quantifier in E.3 is too strong if it includes constant-marginal-cost regimes. Recommended: add domain restriction excluding constant-marginal-cost cost tiers.

### §7.5 Verdict

- **STRONG** for currently-handled edge cases (A → ∞; A → S⁺).
- **WEAK** for missing edge cases (A < S; constant-marginal-cost regimes).

### §7.6 Repair recommendation

Add domain-of-applicability statement per §13.3:

> *Domain of applicability:* This theorem applies to cost tiers C(A, S) on the domain A ≥ S where C is non-constant in A (i.e., where standard resource-economics cost-function behavior applies). Constant-marginal-cost regimes (e.g., elastic-supply manufactured goods) are out of scope; resource-collapse regimes (A < S) are out of scope and require separate analysis (cf. Diamond 2005; Tainter 1988).

---

## §8. Test 5 — Collision check against established literature

### §8.1 Resource-economics cost-function lineage

| Reference | Cost-function behavior addressed |
|---|---|
| **Hotelling 1931 *JPE*** "The Economics of Exhaustible Resources" | Foundational rent dynamics + price-path of exhaustible resource extraction |
| **Pindyck 1978 *JPE*** "The Optimal Exploration and Production of Nonrenewable Resources" | Stock-dependent cost-function behavior; convexity near depletion |
| **Dasgupta & Heal 1979 *Economic Theory and Exhaustible Resources*** | Comprehensive textbook treatment; scarcity-tipping-point analysis |
| **Solow 1974 *Rev Econ Stud*** | Intergenerational equity baseline (adjacent) |
| **Hartwick 1977 *AER*** | Sustainable-investment rule (adjacent) |
| **Slade & Thille 2009 *J Econ Lit*** | Survey of Hotelling-rule tests; cost-function behavior |

### §8.2 Tipping-point ecological economics lineage

| Reference | Tipping-point concept |
|---|---|
| **Barnosky et al. 2012 *Nature*** "Approaching a state shift in Earth's biosphere" | Ecological tipping-point literature; nonlinear growth near critical thresholds |
| **Lenton et al. 2008 *PNAS*** "Tipping elements in the Earth's climate system" | Climate tipping-point literature; nonlinear cost-function growth |
| **Scheffer 2009 *Critical Transitions in Nature and Society*** | Comprehensive tipping-point treatment |
| **Folke et al. 2010** | Resilience + tipping-point framework |

### §8.3 Verdict

**WEAK.** The substantive content of E.3 is anchored in two literature streams (resource-economics cost functions + tipping-point ecological economics) but neither is invoked or cited in current text. Hotelling 1931 referenced informally; no other citations.

### §8.4 Repair recommendation

Add formal citations to restructured proof per §13.2:
- Pindyck 1978 *JPE* — for stock-dependent cost-function convexity (premise P3).
- Dasgupta-Heal 1979 — for scarcity-tipping-point analysis (premises P3 + P4).
- Hotelling 1931 — for rent dynamics (already in bibliography per Hotelling Identity §12; P3 + P4 lineage).
- Barnosky et al. 2012 *Nature* — for ecological tipping-point literature (premise P4).
- Lenton et al. 2008 *PNAS* — for climate tipping-point literature (premise P4).
- Royden 1988 / Folland 1999 — for limit-theorem invocation in derivation.

---

## §9. Test 6 — Citation discipline

### §9.1 Current state

"Hotelling's rent dynamics" referenced once (informal). No formal citations. "Standard behavior of resource cost functions near depletion thresholds" asserted without lineage.

### §9.2 Verdict

**WEAK.** Top-tier journals require formal citations for load-bearing arguments. Currently: no formal citations.

### §9.3 Repair recommendation

Per Enhancement 2 §13.2 — add formal citations as listed in §8.4.

---

## §10. Test 7 — Falsifiability

### §10.1 Falsifiability conditions

E.3 is falsified if:
- A cost tier C exhibits abundance-masking violation: C(A, S) is non-negligible at A ≫ S, or C does NOT grow nonlinearly as A → S⁺.
- A cost tier C is constant-marginal in A across the relevant range (P1 violated).
- A cost tier C does not exhibit nonlinear-growth near threshold (P3 + P4 violated).

The framework's universal-quantifier ("for any cost tier C") makes E.3 strongly falsifiable in principle: a single counterexample would falsify the universal claim.

### §10.2 Verdict

**STRONG.** Falsifiability conditions are explicit. Restricting domain (per §7.6) to non-constant-marginal-cost tiers preserves the universal-quantifier claim within scope while excluding falsifiers (constant-marginal-cost manufactured goods).

### §10.3 Repair recommendation

Restate domain-of-applicability per §13.3 to make scope of universal-quantifier explicit.

---

## §11. Test 8 — Domain of applicability

### §11.1 Current state

E.3 claims universal applicability across "any cost tier C, abundance level A, scarcity threshold S." This is strongly universal; some cost tiers may not satisfy P1–P4 (e.g., constant-marginal-cost manufactured goods).

### §11.2 Verdict

**ADEQUATE-WEAK.** Universal-quantifier claim is too strong without domain restriction; should be explicit about scope (resource-economics cost functions on domain A ≥ S, exhibiting standard scarcity-pricing behavior).

### §11.3 Repair recommendation

Add scope statement per §13.3 — restrict to cost tiers exhibiting standard resource-economics cost-function behavior (monotonicity + abundance limit + scarcity-threshold convexity + nonlinear-growth-near-threshold).

---

## §12. Test 9 — Counterexample resistance

### §12.1 Approach

Construct cost tier C(A, S) satisfying the (restructured) premises P1–P4 but violating E.3's claim.

### §12.2 Constructed attempts

**Attempt 1 (constant cost):** C(A, S) = c₀ for all A. P1 monotonicity is satisfied (∂C/∂A = 0; non-increasing). P2 (abundance limit) is violated (C → c₀ ≠ 0). Premise violation prevents counterexample. ✓ E.3 holds under restructured premises.

**Attempt 2 (linear decline):** C(A, S) = max(c₀ · (S/A), 0). P1 satisfied; P2 satisfied (C → 0); P3 (convexity in S/A) is satisfied with equality (linear in S/A); P4 (nonlinear growth near threshold) is violated. Counterexample under P3 alone, but P4 closes the gap. ✓ E.3 holds.

**Attempt 3 (exponential cost):** C(A, S) = c₀ · exp(-A/S). P1 satisfied; P2 satisfied (C → 0); P3 satisfied (exp decay convex); P4 satisfied (gradient growth). All premises satisfied; E.3 holds — abundance-masking pattern present. ✓

**Attempt 4 (real-world: manufactured goods constant cost):** C(A) = $c per unit, independent of stock-abundance. Violates P1 (∂C/∂A = 0; flat is borderline-monotonic). Violates P2 (C → c, not 0). Excluded by domain-restriction (not a "resource-economics cost function"). ✓ Domain restriction handles.

**Attempt 5 (cost increasing in abundance):** C(A) increasing in A. Violates P1. Premise violation prevents counterexample.

### §12.3 Verdict

**STRONG.** No counterexamples constructible under restructured premises P1–P4 + domain restriction. Constant-marginal-cost manufactured goods (Attempt 4) are excluded by domain restriction. Resource-economics cost functions exhibiting standard scarcity-pricing behavior are guaranteed to exhibit E.3's abundance-masking pattern by P1–P4 + standard real-analysis limit theorems.

### §12.4 Repair recommendation

Include the domain restriction (per §11.3) as part of theorem statement to make counterexample resistance explicit.

---

## §13. Recommended formal restatement

### §13.1 Premise enumeration (Assumptions P1–P4) — UPDATED with τ rename per Finding F1

**P1 (Monotonicity in abundance):** Cost tier c: ℝ_>0 × ℝ_>0 → ℝ_≥0 satisfies ∂c/∂A ≤ 0 for all A > τ. (More abundance → lower or equal per-unit cost.) Standard resource-economics cost-function premise (Pindyck 1978 *JPE*; Dasgupta-Heal 1979; Marshall 1890 *Principles of Economics* supply-elasticity foundations).

**P2 (Abundance limit):** lim_{A → ∞} c(A, τ) = 0. (Per-unit cost vanishes in the abundance limit.) Standard premise (Pindyck 1978; Hartwick 1977).

**P3 (Convexity in scarcity ratio):** c(A, τ) is convex in (τ/A) for τ/A ∈ (0, 1]: ∂²c/∂(τ/A)² ≥ 0. (Cost-function curvature near scarcity threshold; Hotelling 1931 rent dynamics extended to cost-function form; Marshall 1890 supply-elasticity collapse near scarcity.)

**P4 (Nonlinear growth near scarcity threshold):** ∂c/∂A → -∞ as A → τ⁺ from above (or the gradient grows without bound). Tipping-point cost-function behavior near critical scarcity threshold (Barnosky et al. 2012 *Nature* ecological tipping-points; Lenton et al. 2008 *PNAS* climate tipping-points; Hamilton 2009 *Brookings Papers* + Kilian 2009 *AER* commodity-shock empirical patterns).

**Notation note (per Finding F1):** Scarcity threshold is denoted **τ** (Greek tau), NOT S — to avoid notation collision with the framework's substitutability function S(t) (Tech Appendix §B Definition A.2; load-bearing in RCV integrand + Theorems E.4 + E.5). The Commons Inversion Test (CIT) operational protocol per Definition A.8 + terms_index entry must use τ to match.

### §13.2 Theorem statement (restructured) — UPDATED with τ rename + functional form per Findings F1 + F3

**Theorem E.3 (Abundance Masking).**

*Under Assumptions P1–P4, for any cost tier c(A, τ) on the domain A > τ exhibiting standard exhaustible-resource cost-function behavior:*

- *(i) When A ≫ τ, c(A, τ) ≈ 0 (per-unit cost is negligible).*
- *(ii) As A → τ⁺, c(A, τ) grows nonlinearly without bound (cost gradient diverges).*

*The transition from (i) to (ii) is the abundance-masking phenomenon.*

**Proof.** By P1 + P2, lim_{A → ∞} c(A, τ) = 0; combined with monotonicity, for any ε > 0 ∃ A* > τ such that c(A, τ) < ε for all A > A*. Hence when A ≫ τ, c(A, τ) < ε for ε arbitrarily small — establishing (i).

By P3 + P4, the cost gradient ∂c/∂A grows without bound as A → τ⁺ from above. Equivalently, for any M > 0 ∃ δ > 0 such that ∂c/∂A < -M for all A ∈ (τ, τ+δ). Integrating, c(A, τ) grows nonlinearly without bound as A → τ⁺ — establishing (ii).

The transition from (i) to (ii) follows by intermediate-value continuity of c(A, τ) on (τ, ∞). The cost function transitions from c ≈ 0 (at A ≫ τ) to c → ∞ (at A → τ⁺) through a nonlinear-growth regime determined by P3 + P4 convexity behavior.

By Lebesgue dominated convergence theorem (Royden 1988 §4.4; Folland 1999 §2.4), the integrated cost ∫_{τ}^{A_max} c(A, τ) dA can be computed pointwise on the domain.

The abundance-masking phenomenon is therefore guaranteed by P1–P4 + standard real-analysis limit theorems. ∎

**Concrete realization (working specification per Finding F3):** A specific functional form satisfying all P1–P4 premises is:

> **c(A, τ) = c₀ · (τ/(A−τ))^α** where c₀ > 0, α > 0, A > τ.

Properties (verifying P1–P4):
- (P1) Monotonically decreasing: ∂c/∂A = −c₀ · α · τ · (τ/(A−τ))^(α-1) · 1/(A−τ)² < 0 for A > τ ✓
- (P2) Abundance limit: as A → ∞, (τ/(A−τ)) → 0 ⇒ c → 0 ✓
- (P3) Convex in (τ/(A-τ)) ratio for α ≥ 1 ✓
- (P4) Nonlinear growth near threshold: as A → τ⁺, c → ∞ ✓

The α parameter calibrates curvature: α = 1 gives linear-in-(τ/(A−τ)) growth; α > 1 gives super-linear divergence near threshold (matching empirical commodity-shock patterns per Hamilton 2009 + Kilian 2009; matching ecological-tipping-point behavior per Barnosky 2012 + Lenton 2008; consistent with Hotelling 1931 rent-near-exhaustion dynamics).

This functional form is offered as a working specification — the theorem holds for any function satisfying P1–P4; this is one concrete realization consistent with both commodity-economics + ecological-tipping-point lineages.

### §13.3 Domain of applicability — UPDATED with four counterexample-class restrictions per Finding F4

> *Domain of applicability:* This theorem applies to cost tiers c(A, τ) on the domain A > τ exhibiting **non-renewable, rival, anti-network-effect, non-constant-marginal-cost** structural properties + satisfying P1–P4 (standard exhaustible-resource cost-function behavior per Pindyck 1978; Dasgupta-Heal 1979; Hotelling 1931 + commodity-shock empirical patterns per Hamilton 2009; Kilian 2009; Marshall 1890 supply-elasticity lineage). **Out of scope (four counterexample classes):**
>
> - *(a) Constant-marginal-cost regimes* — elastic-supply manufactured goods where ∂c/∂A = 0 violates P1 + c → c₀ ≠ 0 violates P2.
> - *(b) Renewable resources* — where A self-restores faster than depletion; abundance-masking phenomenon doesn't apply because A doesn't decrease monotonically.
> - *(c) Information goods* — non-rival; abundance never approaches scarcity threshold because consumption doesn't decrease A.
> - *(d) Network-effect goods* — where ∂U/∂A > 0 (utility increases with adoption) inverts the scarcity-utility relationship that grounds the abundance-masking phenomenon.
>
> Resource-collapse regimes (A < τ) are also out of scope and require separate analysis (cf. Diamond 2005 *Collapse*; Tainter 1988 *The Collapse of Complex Societies*).

### §13.4 CIT-as-operational-corollary reframing (Tech Appendix §B Definition A.8)

Add to Tech Appendix §B Definition A.8 (CIT definition) the following clarifying paragraph:

> *Relationship to Theorem E.3 (Abundance Masking).* The abundance-masking phenomenon — the transition of cost tier c from c ≈ 0 (at A ≫ τ) to c → ∞ (at A → τ⁺) — is established analytically in Theorem E.3 (§10) from standard resource-economics cost-function primitives (P1–P4). CIT is the **methodological protocol** that detects this phenomenon empirically in any extraction transaction: stripping away dimensions of abundance and observing which cost tiers transition from latent-to-visible is the empirical signature of E.3's analytic prediction. **CIT's validity as a discovery methodology follows from E.3.** Equivalently: E.3 tells us why CIT works; CIT is how we operationalize E.3-based detection of hidden cost tiers. *Notation note:* CIT Definition A.8 must use τ (Greek tau) for scarcity threshold to match E.3's notation, eliminating notation collision with the framework's substitutability function S(t).

### §13.5 Backward-pointer at E.3 statement

Add to E.3 statement (after the restructured proof in §13.2) a one-line backward-pointer to CIT:

> *Operational corollary:* The Commons Inversion Test (Definition A.8) operationalizes detection of the abundance-masking phenomenon established here. CIT's validity as discovery methodology follows from E.3.

### §13.6 Bibliography expansion — UPDATED with commodity-economics + supply-elasticity lineage per Finding F2

Add to bibliography (commodity-economics + supply-elasticity lineage NEW per F2):
- **Marshall, Alfred. 1890.** *Principles of Economics*. London: Macmillan. — foundational supply-elasticity treatment; near-vertical supply curve at scarcity threshold; underwrites P3 + P4 from price-discovery angle. (NEW per Finding F2.)
- **Hamilton, James D. 2009.** "Causes and Consequences of the Oil Shock of 2007–08." *Brookings Papers on Economic Activity* (Spring): 215-261. — empirical commodity-shock literature on abundance-to-scarcity transition price dynamics. (NEW per Finding F2.)
- **Kilian, Lutz. 2009.** "Not All Oil Price Shocks Are Alike: Disentangling Demand and Supply Shocks in the Crude Oil Market." *American Economic Review* 99(3): 1053-1069. — supply-elasticity + scarcity-threshold empirical methodology. (NEW per Finding F2.)

Resource-economics lineage (mostly already in framework's bibliography per other ratified rigor passes):
- **Pindyck, Robert S. 1978.** "The Optimal Exploration and Production of Nonrenewable Resources." *Journal of Political Economy* 86(5): 841-861. — premise P1 + P3 anchor (already added per Insight #52 Q(t) notation audit).
- **Dasgupta, Partha, and Geoffrey Heal. 1979.** *Economic Theory and Exhaustible Resources*. Cambridge: Cambridge University Press. — premises P1–P4 textbook anchor (already added per Insight #52).
- **Hotelling, Harold. 1931.** "The Economics of Exhaustible Resources." *Journal of Political Economy* 39(2): 137-175. — premise P3 + P4 rent-dynamics anchor (already in bibliography per Hotelling Identity §12).
- **Hartwick, John M. 1977.** "Intergenerational Equity and the Investing of Rents from Exhaustible Resources." *American Economic Review* 67(5): 972-974. — premise P2 abundance-limit anchor (already in bibliography per Hotelling Identity §12).

Tipping-point ecological-economics lineage (NEW per this audit):
- **Barnosky, Anthony D., et al. 2012.** "Approaching a state shift in Earth's biosphere." *Nature* 486(7401): 52-58. — premise P4 ecological tipping-point anchor.
- **Lenton, Timothy M., et al. 2008.** "Tipping elements in the Earth's climate system." *Proceedings of the National Academy of Sciences* 105(6): 1786-1793. — premise P4 climate tipping-point anchor.

Real-analysis lineage (already in framework bibliography per Insight #40 Theorem E.4):
- **Royden, H. L. 1988.** *Real Analysis*, 3rd ed. New York: Macmillan.
- **Folland, Gerald B. 1999.** *Real Analysis: Modern Techniques and Their Applications*, 2nd ed. New York: Wiley-Interscience.

(Optional secondary additions: Diamond 2005 *Collapse*; Tainter 1988 *The Collapse of Complex Societies* — for resource-collapse-regime out-of-scope reference.)

**Aggregate bibliography expansion:** 3 NEW references (Marshall 1890; Hamilton 2009; Kilian 2009) + 2 NEW references (Barnosky 2012; Lenton 2008) = 5 net-new references for Phase 3 v2.0.0 rebuild bibliography. The remaining references (Pindyck 1978; Dasgupta-Heal 1979; Hotelling 1931; Hartwick 1977; Royden 1988; Folland 1999) overlap with prior ratified Insights #40 + #52 and absorb once at rebuild time.

---

## §14. Verdict + ratification choices

### §14.1 Recommended verdict

**OPTION β + γ COMBINED (substantive derivation from resource-economics primitives + CIT-as-operational-corollary reframing) per §13.** The substance survives the restructure; the circular proof is replaced with substantive derivation from standard resource-economics cost-function primitives + tipping-point literature; CIT's role is preserved but reframed as operational corollary rather than load-bearing premise.

Three concrete enhancements:

1. **Premise enumeration P1–P4 per §13.1** — explicit numbered premises (monotonicity in abundance; abundance limit; convexity in scarcity ratio; nonlinear growth near scarcity threshold) anchored to Pindyck 1978 + Dasgupta-Heal 1979 + Hotelling 1931 + Barnosky et al. 2012 + Lenton et al. 2008.

2. **Substantive derivation per §13.2** — replace circular "By construction of CIT" with derivation invoking P1–P4 + Lebesgue dominated convergence theorem + intermediate-value continuity. Cite Royden 1988 / Folland 1999 for limit-theorem invocation.

3. **Domain-of-applicability statement per §13.3** — restrict universal-quantifier scope to non-constant-marginal-cost cost tiers exhibiting standard resource-economics cost-function behavior.

Plus: **CIT-relationship reframing per §13.4 + §13.5** — clarifying paragraph at Definition A.8 + backward-pointer at E.3 statement establishes E.3 as analytic theorem and CIT as operational corollary.

### §14.2 Pass-fail verdict on as-currently-written E.3

**FAIL — circular proof.** The proof's load-bearing move ("By construction of the Commons Inversion Test") is structurally circular: invoking the methodological protocol that operationalizes E.3's claim. Top-tier academic peer review will flag this as categorical disqualifier.

### §14.3 Pass-fail verdict on enhanced E.3 per §13

**STRONG.** With substantive derivation + premise enumeration + domain-of-applicability + CIT-relationship reframing applied, theorem meets academic-peer-review standards. Premises explicit and anchored to established literature; derivation invokes standard real-analysis tools (Lebesgue dominated convergence; intermediate-value continuity); domain restriction excludes counterexamples; CIT relationship clarified.

### §14.4 Author ratification choices

**(a) Full ratify Option β + γ per §13** — premise enumeration + substantive derivation + domain-of-applicability + CIT-relationship reframing + bibliography expansion. **Recommended.**

**(b) Ratify Option α (delete E.3 as redundant with CIT)** — drops the analytic claim; CIT alone carries the methodology; framework loses theoretical foundation for CIT. **Considered + rejected** per §1.4 but author override possible.

**(c) Ratify Option γ alone (CIT-relationship reframing without substantive derivation)** — keeps current proof but adds clarifying language about E.3-vs-CIT relationship. **Rejected** because it leaves the circular-proof structure unfixed; only addresses the relationship clarity.

**(d) Partial ratify Option β + γ** — adopt subset:
- (d.i) Premise enumeration only (Enhancement 1) — minimum viable repair.
- (d.ii) Premise + substantive derivation (Enhancements 1 + 2); defer domain-of-applicability + CIT-reframing.
- (d.iii) All except CIT-relationship reframing (defer §13.4 + §13.5 to separate audit).

**(e) Modify verdict** — author specifies different recommendation (e.g., narrower citation set; different premise structure; different domain restriction).

**(f) Defer ratification** — additional questions before locking; possibly bundle with sibling theorem rigor passes for combined ratification.

**(g) Reject** — author rejects audit findings; would require justifying why current circular proof survives academic peer review.

**Recommendation: (a) Full ratify Option β + γ.** Three enhancements + CIT-reframing are mutually-reinforcing; partial ratification leaves either premise gaps (option d.i), domain-quantifier issues (d.ii), or CIT-relationship circularity (d.iii) unfixed. Total scope: ~250 words replacement + 5-7 bibliography entries (most already added per other Phase 2 audits).

### §14.5 Implementation pending after ratification

If (a) full ratify Option β + γ:
1. Tech Appendix v1.0.0 HTML §10 lines 3270-3276 — replace E.3 statement + proof per §13.1 + §13.2 + §13.3 + §13.5.
2. Tech Appendix v1.0.0 HTML §B Definition A.8 (line 496-499) — add §13.4 clarifying paragraph.
3. Bibliography expansion per §13.6 — Pindyck 1978; Dasgupta-Heal 1979; Barnosky et al. 2012; Lenton et al. 2008; Royden 1988; Folland 1999 (most already added per other Phase 2 audits or per Insight #40 E.4).
4. terms_index — append Phase 2 verdict entry; cross-reference to this rigor pass.
5. Open Insights — new Insight # closed-ratified entry capturing Phase 2 #3.2 verdict.

**Same open question as Insights #35 + #38 + #40 + #47 + #48 + #49 + #50 + Phase 2 #8 + Phase 2 #3.4 Tech Appendix HTML edit timing:** apply now to v1.0.0 vs batch into Phase 3 v2.0.0 rebuild. **Recommended:** unified batch into v2.0.0 rebuild.

### §14.6 Pre-publication external review (Insight #39)

This rigor pass produces Claude's assessment of E.3 circular-proof concern. Per Insight #39, eventual external review by economics PhD or formal-methods expert is warranted. For E.3 specifically, a real-analysis-trained economics reviewer should verify:
- Premises P1–P4 are exhaustive (no hidden assumptions).
- Substantive derivation invokes Lebesgue dominated convergence + intermediate-value continuity correctly.
- Domain restriction adequately excludes counterexamples.
- CIT-relationship reframing eliminates the circularity to peer-review satisfaction.

This rigor pass does NOT replace external review; it produces the substrate that external review would test.

---

## §15. Open questions for author discussion

1. **Option β + γ vs Option α — confirmation.** §13 + §14 recommend Option β + γ (substantive derivation + CIT-reframing). Option α (delete E.3 as redundant with CIT) is considered + rejected. Author preference?

2. **Domain restriction language.** §13.3 restricts to "cost tiers C(A, S) on the domain A ≥ S where C is non-constant in A and satisfies P1–P4." Author preference: tighter restriction (exclude additional regimes; e.g., service-economy cost tiers); looser (include some constant-marginal-cost regimes with caveats); or current?

3. **Bibliography citation scope.** §13.6 adds 5-7 references; most already present per other Phase 2 audits or Insight #40. Are all needed at E.3 specifically, or can citation set be tighter (e.g., Pindyck 1978 + Hotelling 1931 only as primary anchors)?

4. **CIT-relationship reframing language.** §13.4 + §13.5 propose specific clarifying language for Definition A.8 and E.3 statement. Author preference on phrasing — alternative options include "E.3 is the analytic foundation; CIT is the discovery methodology" vs "Theorem E.3 establishes analytically; CIT operationalizes empirically" vs current §13.4 wording.

5. **Tech Appendix HTML edit timing.** Same open question as Insights #35 + #38 + #40 + #47 + #48 + #49 + #50 + Phase 2 #8 + Phase 2 #3.4: apply now to v1.0.0 vs batch into Phase 3 v2.0.0 rebuild?

6. **Coordination with sibling E.1 session.** Sibling theorem-rigor session is auditing E.1 (~3 hours in at this pass start). E.1 (Structural Cost Severance) is the framework's central theorem; its restructure may produce premise-formalization patterns parallel to E.3's. Should E.3's restructure be ratified before or after E.1's? **Recommended:** ratify independently; E.3's restructure doesn't depend on E.1's audit outcome.

7. **Phase 2 theorem-audit aggregate observation.** With E.4 RATIFIED (Insight #40), E.2 [PROPOSED] (Phase 2 #3.4), and now E.3 [PROPOSED] (this pass), three of five theorems have been audited at depth. Pattern: each theorem has a distinct concern (E.4 = formalization gaps; E.2 = categorization; E.3 = circular proof) and a distinct resolution (E.4 = restructure premises + Lebesgue invocation; E.2 = relabel as empirical observation; E.3 = substantive derivation + CIT-reframing). E.1 (sibling session) + E.5 (pending) likely produce different concerns + resolutions. The framework's theorem-audit discipline is producing per-theorem-tailored academic-rigor enhancements at consistent quality.

---

## §16. Cross-references

### §16.1 Upstream rigor passes

- [Phase 1 full framework audit §8.2](commons_bonds_rigor_pass_2026-04-29_full_framework_audit_phase1_v1.0.0.md) — flagged E.3 for Phase 2 academic-rigor depth audit on circular-proof concern.
- [Phase 2 Theorem E.4 Integral Convergence rigor pass §16.3](commons_bonds_rigor_pass_2026-04-29_phase2_theorem_e4_integral_convergence_v1.0.0.md) — RATIFIED 2026-04-29 (Insight #40); methodology template; sequencing recommendation.
- [Phase 2 #3.4 [E.2] Theorem E.2 categorization audit](commons_bonds_rigor_pass_2026-04-29_phase2_theorem_e2_categorization_v1.0.0.md) — [PROPOSED] 2026-04-29; sibling theorem-audit; methodology-precedent.
- [Phase 2 Foreclosure Bond housing-crisis collision](tools/rigor-passes/archive/commons_bonds_rigor_pass_2026-04-29_phase2_foreclosure_bond_housing_crisis_collision_v1.0.0.md) — RATIFIED 2026-04-29 (Insight #38); methodology template.
- [Phase 2 Cost Severance + Severed Cost Tier 2d](tools/rigor-passes/archive/commons_bonds_rigor_pass_2026-04-29_phase2_cost_severance_severed_cost_tier2d_v1.0.0.md) — RATIFIED 2026-04-29 (Insight #35); methodology template.
- This session's reverse-priority Phase 2 sweep (P2#8 [Q(t)] + P2#7 + P2#6 + P2#5 + P2#4) — RATIFIED Insights #47 + #48 + #49 + #50 + P2#8 [PROPOSED]; methodology-precedent for collision-disambiguation patterns (informs E.3 citation expansion via Pindyck 1978 + Dasgupta-Heal 1979 already added in P2#8).

### §16.2 Sibling Phase 2 candidates (concurrent + remaining)

- **Phase 2 #3.1 Theorem E.1 Structural Cost Severance** — sibling session in progress 2026-04-29 (~3 hours in at this pass start; framework-central theorem; ~800-1000 lines estimated).
- **Phase 2 #3.3 Theorem E.5 Renewable Imperative** — pending; over-specified scope; scope-tightening + practical-corollary separation; ~700-900 lines estimated.
- **Phase 2 #3.4 [E.2] Theorem E.2 Convergence of Independent Models** — [PROPOSED] 2026-04-29 (this session, prior).
- **P2#8 [Q(t)] RCV integrand notation** — [PROPOSED] sibling Phase 2 audit (this session).

### §16.3 Downstream artifacts (this pass would update on ratification)

- `manuscript/technical-appendix/TechnicalAppendix_v1.0.0.html` §10 lines 3270-3276 — replace E.3 statement + proof per §13.1 + §13.2 + §13.3 + §13.5.
- `manuscript/technical-appendix/TechnicalAppendix_v1.0.0.html` §B Definition A.8 (line 496-499) — add §13.4 clarifying paragraph.
- `manuscript/technical-appendix/TechnicalAppendix_v1.0.0.html` bibliography section — Pindyck 1978; Dasgupta-Heal 1979; Barnosky et al. 2012; Lenton et al. 2008 (+ Royden 1988 / Folland 1999 already per Insight #40).
- `tools/back-matter/sources/terms_index.md` — append Phase 2 verdict entry; cross-reference to this rigor pass.
- `alignment/commons_bonds_open_insights_v1.0.0.md` — new Insight # closed-ratified capturing Phase 2 #3.2 verdict (number TBD).

### §16.4 Pre-publication external review (Insight #39)

This rigor pass + sibling Phase 2 deeper-dive passes produce Claude's pre-external-review assessment substrate. For E.3 specifically, a real-analysis-trained economics reviewer should verify the substantive derivation + CIT-relationship reframing adequately resolve the circular-proof concern.

---

**End of Phase 2 deeper-dive rigor pass v1.0.0 [PROPOSED — pending author ratification].**
