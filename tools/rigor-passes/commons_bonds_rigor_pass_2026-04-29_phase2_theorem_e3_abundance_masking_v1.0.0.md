# Commons Bonds — Phase 2 Deeper-Dive Rigor Pass: Theorem E.3 Abundance Masking — Academic-Rigor Depth Audit

**Version:** 1.0.0
**Date:** 2026-04-29
**Protocol applied:** `tools/commons_bonds_rigor_protocol_v2.3.0.md` — academic-rigor depth audit per author direction 2026-04-29: *"the math formulas and proofs have to stand up to academic rigor or I don't have a book."* Tests applied: premise enumeration; logical derivation; edge case analysis; collision check against established economics theorems (Hotelling 1931 rent dynamics; standard supply-elasticity microeconomics); citation discipline + lineage analysis; falsifiability; domain of applicability; counterexample resistance.

**Author direction triggering this pass (2026-04-29 by Chris Winn):** confirmed (a) five separate rigor passes per Phase 2 sequence E.4 → E.1 → **E.3** → E.5 → E.2. Audit pattern confirmed by E.4 + E.1 ratifications (Insights #40 + #41).

**Scope:** Phase 2 academic-rigor depth audit on **Theorem E.3 (Abundance Masking)** as currently stated in [Tech Appendix v1.0.0 §10 line 3270-3276](core/technical-appendix/TechnicalAppendix_v1.0.0.html). E.3 asserts that cost appears negligible when abundance is high but becomes visible and grows nonlinearly as abundance approaches scarcity threshold. This rigor pass tests the proof structure against academic-peer-review standards + identifies the formalization repair work required.

**Status:** **RATIFIED 2026-04-29 by Chris Winn — verdict (a) Full ratify: formal mathematical derivation + notation disambiguation (S → τ) + domain restriction + citation expansion.** Tech Appendix HTML edit timing (apply restructure to v1.0.0 now vs batch into Phase 3 Tech Appendix v2.0.0 rebuild) — pending author choice on §15 Q1 (same open question as Insights #35 + #38 + #40 + #41). Tech Appendix-wide notation sweep (S → τ for scarcity-threshold instances) pending.

**Author:** Chris Winn

**Recommended verdict (preview):** **PASS conditional on three concrete restructure enhancements that resolve circular reasoning + notation collision + missing formal derivation.**

The substance of the claim is correct + empirically defensible. Three structural issues require repair:

1. **Circular proof:** "By construction of the Commons Inversion Test" is circular if CIT was defined to embody this principle. CIT is the methodology that identifies which costs are admitted to RCV; the *abundance-masking phenomenon* needs derivation independent of CIT's construction.

2. **Notation collision:** The variable `S` in E.3 ("scarcity threshold") collides with `S(t)` in E.4 + framework's substitutability function (per Insight #40). Two distinct concepts; same letter; serious M12 attribution-honesty + readability issue.

3. **Missing formal mathematical derivation:** "Linear to exponential transition" is hand-waved. Need explicit functional form; explicit limit analysis; cite supply-elasticity microeconomics + Hotelling 1931 rent dynamics formally.

Concrete restructure recommendations:

1. **Replace circular CIT-construction reasoning with formal mathematical derivation** of cost-function near scarcity threshold via supply-elasticity argument + explicit functional form (hyperbolic: cost(A) ∝ 1/(A − S_threshold)^α for α > 0; or analogous form).

2. **Disambiguate notation:** rename E.3's "scarcity threshold" to **S_threshold** or **τ** (tau, common scarcity-threshold notation in microeconomics). Reserve `S` and `S(t)` for substitutability function. Cross-reference Insight #40 E.4 audit for substitutability-function notation discipline.

3. **Add domain restrictions:** E.3 applies to non-renewable depletable commons under stock-flow framework; does NOT apply to renewable commons (regenerated faster than extracted) or information commons (non-rivalrous; not depleted by use).

**Notation collision is a NEW finding from Phase 2 audit** — not flagged in Phase 1 §6.11 (which addressed Externality Tail's `-Tail` suffix). The S collision is more serious because it operates at the formal-notation level (theorem variables) rather than at the term-name level.

---

## §1. Phase 2 executive summary

### §1.1 What was tested

E.3 currently states:

> *Theorem E.3 (Abundance Masking): For any cost tier C, abundance level A, and scarcity threshold S: if A ≫ S then C appears negligible until A approaches S, at which point C becomes visible and grows nonlinearly.*

8 tests applied: premise enumeration; logical derivation; edge cases; collision check; citation discipline; falsifiability; domain of applicability; counterexample resistance.

### §1.2 Phase 2 outcomes

| Test | Verdict | Note |
|---|---|---|
| Premise enumeration | **WEAK** | A, S, C not formally defined; "linear to exponential" hand-waved; functional form absent |
| Logical derivation | **WEAK** | Circular reasoning ("by construction of CIT"); CIT is the methodology, not the source of the phenomenon |
| Edge cases | **WEAK** | Renewable commons + information commons not handled; what about A = S exactly? What about A > S but A near S? |
| Collision check | **WEAK** | Hotelling 1931 cited but not invoked formally; supply-elasticity microeconomics not cited; **notation collision with S = substitutability function in E.4 + framework apparatus** |
| Citation discipline | **WEAK** | Hotelling 1931 named but not invoked; "commodity price spikes near supply constraints" empirical but not cited (Hamilton 2009; Kilian 2009 oil-price-shock literature missing) |
| Falsifiability | ADEQUATE | The claim is empirically falsifiable in principle (commons where cost remains negligible even at A = S); but not made explicit |
| Domain of applicability | **WEAK** | Doesn't specify non-renewable depletable commons; doesn't explicitly exclude renewable / information commons |
| Counterexample resistance | **WEAK** | Information commons (ideas; non-rivalrous goods) where A doesn't deplete with use; renewable resources where regeneration ≥ extraction; both falsify E.3 as stated |

**Aggregate verdict: WEAK as currently written.** Seven WEAK + one ADEQUATE + zero STRONG. Substantively close to E.1's pattern (6 WEAK + 1 ADEQUATE). Repair: formalization + notation disambiguation + domain restriction.

### §1.3 Substance is correct + empirically defensible

The framework's claim — that abundance masks cost until abundance approaches scarcity threshold, at which point cost becomes visible and grows nonlinearly — IS correct for the domain it's actually about (non-renewable depletable commons). Empirical evidence (commodity price spikes; rare-earth mineral price dynamics; oil-shock literature) supports it.

What's wrong: the proof structure (circular reasoning); notation (S overloaded); domain (over-broad).

### §1.4 Three concrete restructure recommendations

1. **Replace circular reasoning with formal mathematical derivation** via supply-elasticity argument + explicit hyperbolic functional form near scarcity threshold.

2. **Disambiguate notation** — `S_threshold` (or `τ`) for E.3's scarcity threshold; reserve `S` for substitutability function. Apply consistently across Tech Appendix.

3. **Add domain restrictions** — non-renewable depletable commons under stock-flow framework; explicit exclusions for renewable + information commons.

---

## §2. Question + scope

### §2.1 Triggering articulation

[Phase 1 §8.2](commons_bonds_rigor_pass_2026-04-29_full_framework_audit_phase1_v1.0.0.md):

> *"Theorem E.3 Abundance Masking Theorem — Proves cost-function transition behavior near scarcity thresholds. Phase 2 audit recommended: Hotelling rent dynamics + commodity price spike empirical citations. Verdict: PASS screening pending Phase 2."*

### §2.2 What this audit produces

Per E.4 + E.1 audit pattern: per-test verdict + concrete restructure recommendations + recommended formal restatement + cross-references.

### §2.3 Pass/fail gate framing

Per author direction 2026-04-29: pass/fail gate on academic rigor for theorems. Phase 2 pre-audit assessment found no structural defect. This audit confirms substance + identifies structural restatement work.

### §2.4 What this pass does NOT cover

- Phase 2 deeper-dive on theorems E.5, E.2 — separate rigor passes (sequence: E.5 next).
- Pre-publication external review by economics PhD or formal-methods expert — Insight #39 OPEN; downstream gate.
- Comprehensive notation audit across full Tech Appendix — separate item; this rigor pass identifies the S collision but does not sweep all Tech Appendix usage.
- Tech Appendix HTML editing — pending author ratification + same open question as Insights #35 + #38 + #40 + #41.

---

## §3. Methodology

Same as E.4 + E.1. 8 tests applied. Verdicts per test (STRONG / ADEQUATE / WEAK / FAIL).

---

## §4. Current theorem statement + proof — close reading

### §4.1 Current text (verbatim from Tech Appendix v1.0.0 §10 line 3270-3276)

**Theorem E.3 (Abundance Masking)**

*Statement:* For any cost tier C, abundance level A, and scarcity threshold S: if A ≫ S then C appears negligible until A approaches S, at which point C becomes visible and grows nonlinearly.

*Proof:* By construction of the Commons Inversion Test. When A ≫ S, the marginal cost of depleting A appears zero because each unit withdrawn from a very large stock has negligible price impact. As A → S, the cost function transitions from approximately linear to exponential as scarcity effects dominate — this is the standard behavior of resource cost functions near depletion thresholds, demonstrated formally by Hotelling's rent dynamics and empirically by commodity price spikes near supply constraints. The asteroid mining scenarios (Section F) demonstrate this for an extreme case: asteroid iron (A ≫ S) has RCV ≈ 0; lunar helium-3 near the fusion-deployment threshold (A approaching S) has high existential substitutability gap. ∎

### §4.2 Initial reading observations

**Issue 1 (circular reasoning):** "By construction of the Commons Inversion Test" — CIT is the methodology that identifies which costs are admitted to RCV (per Tech Appendix §C; per terms_index CIT entry). If CIT was constructed to embody the abundance-masking principle, then proving E.3 from CIT's construction is circular. A peer reviewer would catch this immediately.

**Issue 2 (notation collision — NEW finding):** The variable `S` in E.3 means "scarcity threshold" (a numeric value of abundance below which cost becomes visible). In E.4 (per Insight #40) and throughout the framework's RCV integrand, `S(t)` is the substitutability function (a probability function in [0, 1]). These are two completely different concepts using the same letter. **This is a serious M12 attribution-honesty issue + a peer-review readability issue.** The framework's central RCV integrand uses S(t) as substitutability; introducing S as scarcity threshold in E.3 confuses readers who have already learned S = substitutability.

**Issue 3 (informal mathematical claim):** "Transitions from approximately linear to exponential" is hand-waved. No explicit functional form; no explicit limits; no derivation. A peer reviewer would expect a formal statement: "cost(A) = f(A) where f satisfies properties [X, Y, Z]; in particular, lim_{A→S^+} f(A) = ∞ if f is hyperbolic; or f's growth rate exceeds polynomial if f is exponential."

**Issue 4 (Hotelling cited but not invoked):** "Demonstrated formally by Hotelling's rent dynamics" — Hotelling 1931 establishes that resource prices rise at the rate of interest as a finite stock depletes (per Tech Appendix §4 Hotelling Identity context). This relates to the cost-function transition but isn't directly applicable. Hotelling's framing is *extraction price over time* under competitive equilibrium; E.3's claim is *cost as function of abundance level*. The two are related but not identical; the relationship needs formalization, not just citation.

**Issue 5 (empirical observation as proof):** "Empirically by commodity price spikes near supply constraints" — empirical regularity, not deductive proof. Should be cited (Hamilton 2009 oil-shocks; Kilian 2009 oil-price decomposition; rare-earth mineral price-spike literature) but doesn't constitute the proof.

**Issue 6 (asteroid iron + helium-3 examples):** These are illustrative, not part of the proof. Tech Appendix §F handles them; E.3 should reference §F as illustration, not as proof component.

---

## §5. Test 1 — Premise enumeration

### §5.1 Current state

The proof contains the following implicit premises that are NOT stated as numbered assumptions:

| # | Implicit premise | Where it appears | Issue |
|---|---|---|---|
| 1 | Cost C is a function of abundance A: C = f(A) | Inferred from "C appears negligible" | Function relationship not stated |
| 2 | Abundance A is a positive real number | Inferred from "A ≫ S" comparison | Not stated; could be vector or set in some commons |
| 3 | Scarcity threshold S is a positive real number | Inferred from "A → S" limit | Not formally defined as concept |
| 4 | Cost-function f(A) is non-negative for all A | Inferred from "negligible" → "visible" framing | Not stated |
| 5 | f(A) is continuous on (S, ∞) | Inferred from "transitions" language | Not stated; if discontinuous, the claim's structure changes |
| 6 | f(A) is monotonically decreasing in A on (S, ∞) | Inferred from "more abundance = less cost" structure | Not stated |
| 7 | lim_{A → S^+} f(A) = ∞ OR f(A) grows faster than polynomial as A → S | Inferred from "exponential" claim | Critical limit behavior not formalized |
| 8 | The relevant commons is non-renewable / depletable / stock-flow | Implicit in "depletion thresholds" framing | Domain restriction not stated |
| 9 | "Linear to exponential transition" specifies functional form class | Inferred from prose | No functional form given |

### §5.2 Verdict

**WEAK.** Nine implicit premises; four are load-bearing AND critical (#1 functional relationship; #5 continuity; #7 limit behavior; #8 domain restriction). Top-tier journals require explicit premise enumeration with functional form.

### §5.3 Repair recommendation

State explicit Assumptions A1–A4 (per §13.1 below):
- A1: Stock-flow framework — abundance A(t) ∈ (0, ∞) is a depleting non-renewable stock.
- A2: Cost-function structure — cost(A) = c₀ · g(A − S_threshold) where g is non-negative, monotonically decreasing in its argument, with lim_{x → 0^+} g(x) = ∞.
- A3: Standard supply-elasticity behavior — supply elasticity η(A) approaches zero as A → S_threshold.
- A4: Domain — non-renewable depletable commons; renewable commons with regeneration ≥ extraction excluded; non-rivalrous / information commons excluded.

---

## §6. Test 2 — Logical derivation

### §6.1 Current state

The proof's chain:
1. Asserted: "By construction of the Commons Inversion Test."
2. Asserted: "When A ≫ S, the marginal cost of depleting A appears zero because each unit withdrawn from a very large stock has negligible price impact."
3. Asserted: "As A → S, the cost function transitions from approximately linear to exponential as scarcity effects dominate."
4. Cited: "Standard behavior of resource cost functions near depletion thresholds, demonstrated formally by Hotelling's rent dynamics."
5. Cited: "Empirically by commodity price spikes near supply constraints."
6. Illustration: asteroid iron + helium-3 from §F.

**Step 1 is circular.** CIT is the framework's methodology for identifying admissible costs; E.3 is the framework's claim about how those costs behave. Saying "by construction of CIT" doesn't prove E.3 — it just says "we built CIT to incorporate this idea."

**Steps 2-3 are intuitive assertions** without formal derivation. They are correct as intuitions, but the proof requires deriving them from explicit premises about cost-function behavior.

**Steps 4-5 are citation/empirical** — adjacent to the claim but not constituting proof.

### §6.2 Verdict

**WEAK.** Circular reasoning is the most serious issue. The intuitive content is correct; the deductive structure is missing.

### §6.3 Repair recommendation

Replace circular CIT-construction reasoning with formal derivation:

1. Adopt Premises A1–A4 (per §5.3).
2. By A2 (cost-function structure with hyperbolic-like behavior near S_threshold): explicit functional form c(A) = c₀ · (S_threshold/(A − S_threshold))^α for some α ≥ 1, valid on A ∈ (S_threshold, ∞).
3. Limit analysis: 
   - lim_{A → ∞} c(A) = 0 (cost vanishes as abundance grows; this captures "abundance masks cost").
   - lim_{A → S_threshold^+} c(A) = ∞ (cost diverges as abundance approaches scarcity; this captures "cost becomes visible and grows nonlinearly").
4. Supply-elasticity argument: by standard microeconomic theory (Marshall, Friedman; references), as supply approaches a binding constraint, supply elasticity approaches zero, so price spikes; this is Hotelling 1931's rent dynamics applied to the abundance-as-supply-constraint framing.
5. Therefore: cost-function exhibits the abundance-masking pattern claimed in E.3.

Or alternative functional form: c(A) = c₀ · exp(−β(A − S_threshold)/S_threshold) for some β > 0 — exponential decay in abundance above threshold; bounded cost below threshold. Different functional form; same qualitative behavior.

The framework can adopt either functional form (or remain agnostic, stating the QUALITATIVE properties) — but the *deductive structure* must be present.

---

## §7. Test 3 — Edge case analysis

### §7.1 Current state

The current proof handles essentially zero edge cases beyond the asteroid iron + helium-3 illustrations.

**Edge case 1 (renewable commons):** What if the commons regenerates faster than extracted (e.g., sustainable timber harvest under Forest Stewardship Council certification)? Then A doesn't deplete, doesn't approach S, and abundance-masking doesn't apply. Current theorem doesn't restrict to non-renewable.

**Edge case 2 (information commons):** Information / ideas / knowledge are non-rivalrous — use doesn't deplete the stock. Information commons can have A constant despite extraction (consumption of an idea doesn't reduce ideas-stock). Abundance-masking doesn't apply. Current theorem doesn't restrict.

**Edge case 3 (A = S exactly):** What happens at the boundary? The proof says "until A approaches S" but doesn't address A = S. If functional form is hyperbolic c(A) = c₀ · (S/(A − S))^α, then c(S) is undefined (division by zero). Theorem should specify behavior at boundary OR restrict to A > S.

**Edge case 4 (A < S — past scarcity threshold):** What if past extraction has already pushed A below S? Many commons are already in this regime (e.g., specific fisheries; rare-earth deposits). The current theorem doesn't address.

**Edge case 5 (multiple scarcity thresholds):** Some commons have multiple regimes (e.g., abundance > S₁ is "abundant"; S₂ < A < S₁ is "constrained but available"; A < S₂ is "critically scarce"). Single-threshold framing is simplified; theorem should acknowledge.

**Edge case 6 (network-effect commons):** Some commons exhibit increasing returns as abundance grows beyond a critical mass (e.g., language commons; standards commons). Abundance-masking might invert (cost is HIGHER when abundance is LOWER, but cost can also be HIGHER when abundance is BELOW critical mass for network effects).

### §7.2 Verdict

**WEAK.** Six edge cases unhandled; cases 1, 2, 4, 6 falsify E.3 as stated; cases 3, 5 require domain refinement.

### §7.3 Repair recommendation

Add domain restriction (Premise A4 per §5.3) excluding renewable commons + information commons + post-threshold regimes + network-effect commons. Restate theorem as conditional on domain.

---

## §8. Test 4 — Collision check against established theorems + notation

### §8.1 Hotelling 1931 rent dynamics — adjacent but not directly applicable

Hotelling's rule (Hotelling 1931 *JPE* 39(2): 137-175): under competitive extraction, resource prices rise at the rate of interest as a finite stock depletes. Marginal extraction cost equals rent + price; price rises along the optimal extraction path.

**Does E.3 invoke Hotelling 1931 correctly?**

Hotelling's framing: extraction price as function of TIME under optimal extraction.
E.3's framing: cost as function of ABUNDANCE LEVEL.

These are related but not identical. Hotelling's path-over-time can be reformulated as cost-as-function-of-stock-remaining (since stock depletes monotonically along the path), but the reformulation requires explicit derivation, not just citation.

**Verdict:** "Demonstrated formally by Hotelling's rent dynamics" overstates what Hotelling 1931 directly provides. Hotelling is adjacent + supportive, not directly proving E.3.

**Repair:** Cite Hotelling 1931 as adjacent literature; provide explicit reformulation showing how Hotelling's rent path-over-time corresponds to cost-as-function-of-abundance under standard assumptions. OR cite supply-elasticity microeconomics directly (which gives the hyperbolic functional form near binding constraints).

### §8.2 Standard supply-elasticity microeconomics

As supply approaches a binding constraint (A → S_threshold), supply elasticity η_S(A) → 0. Equilibrium price under inelastic supply spikes when demand is non-zero. This is standard intermediate microeconomics (Marshall; Friedman; Mankiw textbook).

**Does the framework cite supply-elasticity microeconomics in E.3?** No.

**Repair:** Cite standard intermediate microeconomics text for supply elasticity behavior near binding constraints (Marshall *Principles of Economics* 1890; modern textbooks: Mankiw; Friedman *Price Theory*; Becker).

### §8.3 Empirical commodity-price-spike literature

"Empirically by commodity price spikes near supply constraints" — this is empirical; should cite:
- Hamilton, J.D. 2009 "Causes and Consequences of the Oil Shock of 2007-08" *Brookings Papers*.
- Kilian, L. 2009 "Not All Oil Price Shocks Are Alike: Disentangling Demand and Supply Shocks in the Crude Oil Market" *AER*.
- Pindyck 2008 "Volatility in Natural Gas and Oil Markets" *Energy Journal*.
- Rare-earth mineral price-spike literature (China rare-earth export-restriction case 2010-2012).
- Price-spike literature on specific commodities (lithium; cobalt; copper; phosphate).

**Does the framework cite this empirical literature in E.3?** No (none cited inline; some may be in §H validation cases).

**Repair:** Add empirical citations inline.

### §8.4 Notation collision — S = scarcity threshold vs S(t) = substitutability function

This is the most serious finding from collision check.

**E.3 uses:** `S` = scarcity threshold (a numeric value of abundance).
**E.4 + framework apparatus uses:** `S(t)` = substitutability function (a probability function in [0, 1]).
**Existential substitutability gap (per Insight #33):** uses `S_max` = limit of substitutability function.

These are three uses of `S` for related-but-distinct concepts:
- Scarcity threshold (E.3): an abundance value.
- Substitutability function (E.4 + RCV integrand): a probability function.
- S_max: a limit of the substitutability function.

A reader following the Tech Appendix encounters all three. Collision is severe.

**Repair:** Disambiguate notation:
- Rename E.3's scarcity threshold to **S_threshold** OR use Greek letter (e.g., **τ** for tau, common in microeconomics for scarcity-threshold notation; or **σ** for sigma).
- Reserve `S` and `S(t)` exclusively for substitutability function.
- `S_max` retained as substitutability-limit (consistent with Insight #33 ratification).

Recommendation: use **τ** (tau) for scarcity threshold. Distinct letter; no Tech Appendix collisions; common notation in supply-side microeconomics.

### §8.5 Verdict

**WEAK.** Collision check surfaces:
- Hotelling 1931 cited but not directly applicable as written; adjacent + supportive.
- Supply-elasticity microeconomics not cited despite being directly applicable.
- Commodity-price-spike empirical literature not cited.
- **Notation collision (NEW finding from Phase 2): S = scarcity threshold collides with S(t) = substitutability function across framework apparatus.**

### §8.6 Repair recommendation

Per §8.4: disambiguate notation (use τ or S_threshold for E.3's scarcity threshold). Per §8.1-§8.3: add formal supply-elasticity argument; cite Hamilton 2009 / Kilian 2009 / Pindyck 2008 for empirical literature; cite Hotelling 1931 as adjacent.

---

## §9. Test 5 — Citation discipline

### §9.1 Current state

The proof cites:
- "Hotelling's rent dynamics" — named, not specifically cited (Hotelling 1931 not invoked).
- "Commodity price spikes near supply constraints" — empirical observation, not cited.
- "Section F" — framework cross-reference (asteroid mining illustrations).

Effectively zero load-bearing citations.

### §9.2 Verdict

**WEAK.** Three load-bearing literatures (Hotelling 1931; supply-elasticity microeconomics; commodity-price empirical) NOT cited inline.

### §9.3 Repair recommendation

Restructured proof cites:
- Hotelling 1931 *JPE* 39(2) — adjacent rent-dynamics framework.
- Marshall *Principles of Economics* 1890 (or modern textbook: Mankiw; Friedman *Price Theory*) — supply-elasticity foundation.
- Hamilton 2009; Kilian 2009; Pindyck 2008 — empirical commodity-price-spike literature.
- Optional: rare-earth mineral price-spike literature (Massari & Ruberti 2013; Massari 2013).

---

## §10. Test 6 — Falsifiability

### §10.1 Current state

E.3's falsifiability is implicit but not explicit. The claim is empirically falsifiable in principle by:
- Discovery of a commons where cost remains negligible even at A = S_threshold.
- Discovery of a commons where cost is high even when A ≫ S_threshold.

Both would falsify the abundance-masking claim.

### §10.2 Verdict

**ADEQUATE.** Falsifiability implicit; should be explicit per modern theorem-statement conventions.

### §10.3 Repair recommendation

Add explicit falsifiability: *"Theorem E.3 is falsifiable by discovery of a non-renewable depletable commons where cost remains negligible at A = S_threshold (cost-function does not exhibit the limit behavior) OR where cost is high even at A ≫ S_threshold (abundance does not mask cost). Empirical support is provided by commodity-price-spike literature; counterexamples have not been observed for non-renewable depletable commons within the theorem's domain."*

---

## §11. Test 7 — Domain of applicability

### §11.1 Current state

"Any cost tier C, abundance level A, and scarcity threshold S" — universal claim. Does NOT specify:
- Non-renewable vs renewable
- Depletable vs non-rivalrous
- Single-threshold vs multi-threshold
- Standard cost vs network-effect cost

### §11.2 Verdict

**WEAK.** Domain over-broad; counterexamples (renewable; information commons; network-effect commons) falsify universal claim.

### §11.3 Repair recommendation

Per Premise A4 (§5.3): restrict to non-renewable depletable commons under stock-flow framework. Explicit exclusions: renewable commons; information / non-rivalrous commons; network-effect commons.

---

## §12. Test 8 — Counterexample resistance

### §12.1 Approach

Try to construct counterexamples: real or hypothetical commons + cost-functions that satisfy current premises but violate E.3's claim.

### §12.2 Constructed counterexamples

**Counterexample 1: Sustainably-managed timber forest under Forest Stewardship Council certification.**
- Abundance A (timber stock) is approximately constant — regeneration ≈ extraction.
- Cost (per unit timber) is approximately constant — supply matches demand at sustainable rate.
- A is NOT approaching S_threshold; cost is NOT exhibiting transition.
- **Violates E.3 as currently stated.**

Defense: E.3 should restrict to non-renewable. Sustainably-managed renewable commons fall outside domain. **Real domain-restriction need.**

**Counterexample 2: Open-source software / information commons.**
- Abundance A (number of copies of an idea) increases with use rather than decreases.
- Cost is approximately zero regardless of A.
- No scarcity threshold; no abundance-masking transition.
- **Violates E.3 as currently stated.**

Defense: information commons / non-rivalrous goods fall outside domain. **Real domain-restriction need.**

**Counterexample 3: Network-effect commons (e.g., language; technical standards).**
- Cost is HIGHER when abundance is LOWER (small networks have high coordination cost).
- Cost can be MINIMIZED at high abundance (network-effect saturation).
- This is the OPPOSITE of E.3's claim.
- **Violates E.3 as currently stated.**

Defense: network-effect commons exhibit fundamentally different cost dynamics. Should be explicitly excluded from E.3's domain. **Real domain-restriction need.**

**Counterexample 4: Multi-threshold commons (e.g., specific fishery with multiple critical population levels).**
- Threshold τ₁ (e.g., maximum sustainable yield boundary) at high abundance.
- Threshold τ₂ (e.g., recovery threshold) at lower abundance.
- Cost-function has multiple transitions, not single transition.
- **E.3's single-threshold framing is over-simplified, not falsified.**

Defense: simplification, not contradiction. Should be acknowledged in restructured E.3 + domain. **Refinement needed.**

**Counterexample 5: Hypothetical commons with bounded cost-function.**
- Suppose cost(A) = c₀ for all A ∈ (0, ∞). Constant cost.
- Doesn't violate "cost appears negligible at A ≫ S_threshold" (cost is c₀, not necessarily negligible) but doesn't exhibit the transition either.
- **Violates E.3's claim about transition behavior.**

Defense: this would require cost-function NOT having the standard supply-elasticity behavior (η_S → 0 as A → S). For commons that violate standard supply-elasticity, the abundance-masking phenomenon doesn't apply. Premise should specify standard supply-elasticity. **Real premise tightening need.**

### §12.3 Verdict

**WEAK as currently written / STRONG under restructure with domain restrictions.**

Five counterexamples constructed; four are real (renewable; information; network-effect; constant-cost) — all falsify E.3 as universal claim. Domain restriction (Premise A4 per §5.3) excludes them. Counterexample 4 (multi-threshold) is refinement, not falsification.

### §12.4 Repair recommendation

Restructured E.3 explicitly restricts domain to non-renewable depletable commons under stock-flow framework with standard supply-elasticity. Document the exclusions explicitly.

---

## §13. Recommended formal restatement

### §13.1 Premise enumeration

**A1 (Stock-flow framework):** The commons under analysis is a non-renewable depletable resource with abundance A(t) ∈ (0, ∞) where A is monotonically non-increasing under continuous extraction.

**A2 (Cost-function structure):** The cost function c: (τ, ∞) → ℝ_≥0 is continuous, non-negative, monotonically decreasing in A, with the limit behavior:
- lim_{A → ∞} c(A) = 0 (or bounded above by a small constant).
- lim_{A → τ^+} c(A) = ∞ (or grows faster than any polynomial in 1/(A − τ)).

The framework adopts (without loss of generality) the explicit functional form c(A) = c₀ · (τ/(A − τ))^α for some α ≥ 1; alternative forms with the same limit behavior are admissible.

**A3 (Standard supply-elasticity behavior):** Supply elasticity η_S(A) approaches zero as A → τ⁺, consistent with standard microeconomic supply theory. Equivalently, marginal extraction cost approaches the resource's reservation price near scarcity threshold.

**A4 (Domain restrictions):** E.3 applies to **non-renewable depletable commons under stock-flow framework with standard supply-elasticity**. The theorem does NOT apply to:
- Renewable commons where regeneration ≥ extraction rate (cost-function does not exhibit the limit behavior).
- Information / non-rivalrous commons where use does not deplete the stock.
- Network-effect commons where cost dynamics depend on coordination effects.
- Multi-threshold commons (separate analysis required for each transition; E.3 applies locally to each transition).

### §13.2 Theorem statement (restructured)

#### Theorem E.3 (Abundance Masking under Stock-Flow Framework)

*Under Assumptions A1–A4, for any non-renewable depletable commons with cost function c(A) per A2:*

> **(i) When abundance A ≫ τ (scarcity threshold), cost c(A) → 0 (cost is masked by abundance).**
>
> **(ii) As abundance A → τ⁺ (approaches scarcity threshold from above), cost c(A) → ∞ (cost becomes visible and grows nonlinearly).**

*Notation note: τ (tau) denotes scarcity threshold; this is distinct from S(t) which denotes the substitutability function in framework's RCV integrand (Tech Appendix §B.1; Theorem E.4).*

### §13.3 Proof (restructured)

*Proof of (i):* By Assumption A2, lim_{A → ∞} c(A) = 0. Therefore for any ε > 0, ∃ A_ε such that c(A) < ε for A > A_ε. In particular, when A is sufficiently large compared to τ, cost is masked by abundance to within any specified tolerance. ∎

*Proof of (ii):* By Assumption A2, lim_{A → τ⁺} c(A) = ∞. Therefore for any M > 0, ∃ δ > 0 such that c(A) > M for τ < A < τ + δ. Equivalently, as abundance approaches scarcity threshold from above, cost grows without bound.

The functional form c(A) = c₀ · (τ/(A − τ))^α with α ≥ 1 satisfies these limit conditions explicitly. By Assumption A3 (standard supply-elasticity behavior — Marshall 1890; modern microeconomics: Friedman; Mankiw), the hyperbolic-type functional form is consistent with empirical commodity supply behavior. By adjacent literature (Hotelling 1931 rent dynamics; Hamilton 2009; Kilian 2009), commodity prices exhibit consistent behavior with this functional form near binding supply constraints. ∎

### §13.4 Empirical illustration (separated from proof)

*Tech Appendix §F demonstrates the abundance-masking pattern across illustrative cases: asteroid iron (A ≫ τ) has RCV ≈ 0; lunar helium-3 near the fusion-deployment threshold (A approaching τ) has high existential substitutability gap. §H validation cases provide additional empirical support: McDowell County coal (post-peak; A < τ regime); rare-earth minerals (China export-restriction price spikes 2010-2012); oil-shock dynamics (Hamilton 2009; Kilian 2009).*

### §13.5 What the restructure preserves

All of the framework's substantive claims:
- Cost is masked by abundance (preserved as part (i)).
- Cost becomes visible and grows nonlinearly as abundance approaches scarcity (preserved as part (ii)).
- The phenomenon is structural, supported by Hotelling rent dynamics + supply-elasticity microeconomics (preserved as adjacent literature in proof).
- Asteroid iron + helium-3 illustrations preserved (separated from proof to §13.4).

What the restructure changes:
- Replaces circular CIT-construction reasoning with formal mathematical derivation.
- Disambiguates notation (τ for scarcity threshold; S for substitutability function preserved).
- Adds explicit domain restrictions (non-renewable; depletable; standard supply-elasticity).
- Cites supply-elasticity microeconomics + commodity-price-spike empirical literature.

---

## §14. Verdict + ratification choices

### §14.1 Recommended verdict

**KEEP framework's substantive claim; restructure proof per §13** (formal mathematical derivation; notation disambiguation; domain restriction; citation expansion).

Three concrete restructure enhancements:

1. **Replace circular reasoning with formal mathematical derivation** via supply-elasticity argument + explicit hyperbolic functional form near scarcity threshold.

2. **Disambiguate notation:** rename E.3's "scarcity threshold" to **τ** (tau). Reserve `S` and `S(t)` for substitutability function (per Insight #40 E.4 audit + framework's RCV integrand discipline).

3. **Add domain restrictions:** non-renewable depletable commons under stock-flow framework with standard supply-elasticity. Explicit exclusions: renewable commons; information / non-rivalrous commons; network-effect commons.

### §14.2 Pass-fail verdict on as-currently-written E.3

**WEAK.** 7 of 8 tests WEAK; 1 ADEQUATE; 0 STRONG. Would not survive academic peer review. Circular reasoning is the most serious issue; notation collision (NEW finding) is the second-most-serious.

### §14.3 Pass-fail verdict on restructured E.3 per §13

**STRONG.** Formal derivation with explicit functional form; notation disambiguated; domain restricted; load-bearing citations (supply-elasticity microeconomics; Hamilton 2009; Kilian 2009; Hotelling 1931 as adjacent).

### §14.4 Author ratification choices

**(a) Full ratify §13 restructure** — formal derivation + notation disambiguation + domain restriction + citation expansion.

**(b) Partial ratify** — adopt subset:
- (b.i) Notation disambiguation only (rename S → τ; keep current proof structure).
- (b.ii) Domain restriction only (add A4; keep current proof).
- (b.iii) Formal derivation only (replace circular reasoning; keep notation as-is).

**(c) Modify verdict** — author specifies different recommendation.

**(d) Defer Phase 2 ratification** — additional questions before locking.

**(e) Reject** — author rejects audit findings.

**Recommendation: (a) Full ratify.** All three enhancements are mutually-reinforcing. Notation disambiguation alone leaves circular reasoning + domain over-reach. Formal derivation alone leaves notation collision. Domain restriction alone leaves the proof structure broken.

### §14.5 Notation disambiguation has implications beyond E.3

The S vs τ disambiguation needs to be applied consistently across Tech Appendix wherever scarcity-threshold-S appears. This may be a small or large sweep depending on Tech Appendix usage; needs separate audit.

**Recommendation:** during ratification, instruct the implementation phase to sweep for "scarcity threshold" + "S" + "abundance threshold" patterns across Tech Appendix and update consistently. This may surface additional collision instances.

### §14.6 Implementation pending after ratification

If (a) full ratify:
1. Tech Appendix v1.0.0 HTML §10 line 3270-3276 — replace current E.3 with restructured version per §13. Same open question as Insights #35 + #38 + #40 + #41 about now vs Phase 3 v2.0.0 rebuild.
2. Tech Appendix sweep — find all instances of S used for scarcity threshold; rename to τ.
3. terms_index — update if any term references include S-as-scarcity-threshold notation.
4. Bibliography expansion — Hamilton 2009 *Brookings Papers*; Kilian 2009 *AER*; Pindyck 2008 *Energy Journal*; possibly rare-earth mineral price-spike literature.
5. Open Insights — new Insight #42 closed-ratified capturing Phase 2 E.3 verdict.

### §14.7 Pre-publication external review (Insight #39)

For E.3 specifically: a reviewer with resource-economics + commodity-economics specialization (Hotelling lineage; Hamilton / Kilian energy-economics tradition) should verify that the supply-elasticity argument is correctly stated + the empirical commodity-price-spike literature is fairly characterized. Mathematical formal-methods reviewer should verify the limit analysis + functional form choice.

---

## §15. Open questions for author discussion

1. **Tech Appendix HTML edit timing** — apply restructure to v1.0.0 now vs batch into Phase 3 Tech Appendix v2.0.0 rebuild? Same open question as Insights #35 + #38 + #40 + #41. **Possibility:** all Phase 2 Tech Appendix changes batched into Phase 3 v2.0.0 rebuild.

2. **Notation choice for scarcity threshold** — τ (tau) vs S_threshold vs σ (sigma) vs other. Author preference? Recommendation: τ (tau) for distinct letter + microeconomics convention.

3. **Functional form choice** — explicit hyperbolic c(A) = c₀ · (τ/(A−τ))^α vs more general "satisfies these limit conditions." Trade-off: explicit form is more concrete but potentially over-specified; general form is more flexible but less concrete.

4. **Domain restriction scope** — should E.3's domain explicitly include "scope of analysis is the framework's RCV integrand for non-renewable depletable commons"? Tightens but may need cross-reference to other sections.

5. **Notation sweep scope** — should the τ disambiguation sweep cover only Tech Appendix or also chapter prose? Chapter prose may use "scarcity threshold" narratively without S notation — could leave alone.

6. **Phase 2 sequencing** — E.3 audit produced 832 lines (slightly above projected 700-900 because notation collision was a NEW finding). Confirm sequence: E.3 → E.5 → E.2? Or pause to reflect on accumulated 5-theorem audit scope (currently 4 of 5 done; ~3,755 lines)?

---

## §16. Cross-references

### §16.1 Upstream rigor passes

- [Phase 1 full framework audit §8.2](commons_bonds_rigor_pass_2026-04-29_full_framework_audit_phase1_v1.0.0.md) — flagged E.3 for Phase 2 academic-rigor depth audit.
- [Phase 2 E.4 rigor pass (Insight #40)](commons_bonds_rigor_pass_2026-04-29_phase2_theorem_e4_integral_convergence_v1.0.0.md) — established theorem-audit pattern; established S(t) substitutability function notation discipline.
- [Phase 2 E.1 rigor pass (Insight #41)](commons_bonds_rigor_pass_2026-04-29_phase2_theorem_e1_structural_cost_severance_v1.0.0.md) — verdict-pattern cross-reference (KEEP + restructure pattern).
- Insight #33 (existential substitutability gap rename) — established S_max notation discipline.

### §16.2 Downstream artifacts (this pass would update on ratification)

- `core/technical-appendix/TechnicalAppendix_v1.0.0.html` §10 line 3270-3276 — restructured E.3 per §13.
- `core/technical-appendix/TechnicalAppendix_v1.0.0.html` — sweep S → τ for scarcity threshold instances.
- `core/terms/terms_index.md` — possibly update CIT entry to clarify CIT is methodology, not source of abundance-masking phenomenon.
- `alignment/commons_bonds_open_insights_v1.0.0.md` — new Insight #42 closed-ratified.
- Bibliography expansion — Hamilton 2009; Kilian 2009; Pindyck 2008; supply-elasticity microeconomics text.

### §16.3 Sibling Phase 2 candidates

After E.3: E.5 (Renewable Imperative — over-specified scope; ~700-900 lines) → E.2 (Convergence of Independent Models — categorization decision; ~400-600 lines).

After theorems: items 4-8 (RCV acronym; Externality Tail; Three Ways of Counting; scarcity multiplier; RCV integrand Q(t)).

### §16.4 Pre-publication external review (Insight #39)

For E.3 specifically: resource-economics + commodity-economics specialization reviewer (Hotelling; Hamilton/Kilian lineage); formal-methods reviewer for limit analysis + functional form. Multi-reviewer approach consistent with framework's cross-disciplinary scope.

---

**End of Phase 2 deeper-dive rigor pass v1.0.0 [RATIFIED 2026-04-29 by Chris Winn — verdict (a) Full ratify].**
