# Commons Bonds — Phase 2 Deeper-Dive Rigor Pass: RCV Integrand Q(t) Notation-Clarity Audit

**Version:** 1.0.0
**Date:** 2026-04-29
**Protocol applied:** `tools/commons_bonds_rigor_protocol_v2.3.0.md` — academic-rigor depth audit per author direction 2026-04-29: *"the math formulas and proofs have to stand up to academic rigor or I don't have a book."* Tests applied: premise enumeration (notation-introduction discipline); logical derivation (does Q(t)-reading affect proofs?); edge case analysis (Q → 0 limit); collision check against established economics-notation conventions; citation discipline; falsifiability (does the notation choice carry a falsifiable claim?); domain of applicability; counterexample resistance (can a reader construct a misreading that produces framework conclusions?).

**Scope:** Phase 2 academic-rigor depth audit on the **Q(t) notation** as it appears in U(R, t, Q(t)) inside the RCV integrand and downstream theorem statements + chapter prose. Phase 1 §7.2 + §7.16 flagged this as Phase 2 candidate #8 with rationale: *"M11: notation collision check — U(R, t, Q(t)) utility function, D(t, t₀) discount factor, S(t|t₀) substitutability; all standard. Phase 2 verification recommended on Q(t) ambiguity (quality? quantity? per chapter context disambiguates)."*

**Status:** **RATIFIED 2026-04-29 by Chris Winn — verdict (a) Full ratify all three enhancements** with specific author elections per §15: Q3 **comprehensive bibliography** (all 6 references); Q4 **full cross-reference scope** (3 mandatory + 5+ optional = 8+ locations including §F existential analysis + §K formula breakdowns + terms_index entries + glossary v3); Q5 **batch into Phase 3 Tech Appendix v2.0.0 rebuild** (unified with Insights #35 + #38 + #40 + #47 + #48 + #49 + #50 + #51 Tech Appendix HTML edits). Insight #52 closed-ratified entry added to `alignment/commons_bonds_open_insights_v1.0.0.md`.

**Author:** Chris Winn

**Recommended verdict (preview):** **PASS conditional on three concrete notation-discipline enhancements** to bring Q(t) notation to academic-peer-review readiness. Rename to X(t) considered + rejected (downstream cost > clarity gain). Three enhancements: (1) definition-anchor with explicit disambiguation at §B Definition A.3; (2) cross-reference discipline at every theorem-statement and illustrative-example appearance; (3) bibliography note explaining convention choice vis-à-vis Hotelling / Pindyck / Dasgupta-Heal / Mussa-Rosen lineages.

The substance of Q(t) is sound: it consistently means "remaining in-situ stock of resource R at time t" across all 13+ framework appearances. The notation collision risk is real (Hotelling/Pindyck resource-econ convention uses Q for extraction-rate flow; Mussa-Rosen/Spence IO convention uses Q for product quality) but local context and the math itself (∂U/∂Q < 0 monotonicity in scarcity per Definition A.3) force the stock-reading for any careful reader. The repair work is notation-discipline, not re-derivation or rename.

---

## §1. Phase 2 executive summary

### §1.1 What was tested

The Q(t) notation currently appears in:
- **Tech Appendix §B Definition A.3 (Stock-Dependent Utility)** — primary definition: *"U(R, t, Q(t)) represents generation t's utility from resource R being available in situ, conditional on remaining stock Q(t)"* — with monotonicity ∂U/∂Q < 0 + non-negativity + market-price lower bound.
- **Tech Appendix §B Definition A.6 (RCV Core Formula)** — RCV(R, t₀) = ∫_{t₀}^∞ {[1 − S(t | t₀)] · U(R, t, Q(t)) + E(R, t)} · D(t, t₀) dt.
- **Tech Appendix §10 Theorem E.4 statement** — Q(t) inside U(R, t, Q(t)) without local re-definition.
- **Tech Appendix McDowell illustrative example** — Q(t) inside RCV_McDowell formula without local re-definition.
- **Tech Appendix §M general-form recovery** — Q(t) inside C₁(R, t, Context) two-term special case without local re-definition.
- **Chapter 6 §B integrand introduction** — *"U(R, t, Q(t)) is the utility future generation t derives from having one unit of R available in situ, given the remaining stock Q at time t. As stock depletes, U rises because each remaining unit becomes more valuable."*
- **Chapter 7 GuidanceDoc (Off-Earth scenarios)** — Q(t) used 8+ times in case-walkthroughs (asteroid iron, Mars ice, Moon He-3, lunar regolith, ocean comet, deuterium); each instance contextually disambiguates as stock-quantity through phrases "Q decreases / Q is large / stock-dependent utility activates."
- **Tech Appendix Ripple Effects 1.0 update** — *"S(t | t₀, Q(t)) = S_base(t) · [1 − α · (Q_critical / Q(t))^β]"* — Q(t) coupled to Q_critical threshold, reinforcing stock-reading.

The audit tests:
1. **Premise enumeration** — is Q(t) explicitly defined at first formula appearance? at every subsequent appearance?
2. **Logical derivation** — does the framework's mathematics depend on the quantity-reading vs admit a quality-reading?
3. **Edge cases** — what happens when Q(t) → 0? when Q(t) → ∞? when Q(t) is non-monotonic?
4. **Collision check** — does Q(t)-as-stock collide with established economics-notation conventions?
5. **Citation discipline** — is the convention choice cited?
6. **Falsifiability** — does the notation carry an empirical claim that could be falsified?
7. **Domain of applicability** — where does Q(t) apply consistently as stock?
8. **Counterexample resistance** — can a reader misread Q(t) and produce the framework's conclusions?

### §1.2 Phase 2 outcomes

| Test | Verdict | Note |
|---|---|---|
| Premise enumeration | **ADEQUATE** | Defined twice (Tech App §B + Ch 6 §B); not re-defined at theorem statements, illustrative examples, or general-form section |
| Logical derivation | **STRONG** | Math operates on Q(t) as state-variable abstraction; ∂U/∂Q < 0 + Q_critical threshold + stock-depletion path force stock-reading internally |
| Edge cases | STRONG | Q(t) → 0 produces U → ∞ (unbounded scarcity utility under Definition A.3 monotonicity); this scarcity-tail behavior is incoherent under quality-reading, so internal math disambiguates |
| Collision check | **WEAK** | Hotelling 1931 / Pindyck 1978 / Slade-Thille 2009 use Q (or q) for extraction-rate flow; X(t) / x(t) / S(t) for stock. Mussa-Rosen 1978 / Spence 1976 / Tirole 1988 use Q for product-quality index. Framework's Q-as-stock convention diverges from both lineages; reader from either lineage will pause at U(R, t, Q(t)) without explicit definition |
| Citation discipline | **WEAK** | No citation explaining Q-as-stock notation choice; convention divergence not acknowledged |
| Falsifiability | N/A | Notation-choice is not a claim; underlying concept (stock-dependent utility) is falsifiable but that's separate (Definition A.3 #2 monotonicity assumption) |
| Domain of applicability | STRONG | Q(t) used consistently as stock across all framework appearances; no instances where Q(t) reads as quality or as flow |
| Counterexample resistance | ADEQUATE | Internal math forces stock-reading; skim-reader can misread but cannot construct counterexample where quality-reading produces framework's RCV claims |

**Aggregate verdict: PASS conditional on three concrete notation-discipline enhancements.**

No structural defect. The substance is clean: Q(t) consistently means stock; the math forces this reading; chapter-prose context disambiguates locally. The repair work is academic-publication notation-discipline (definition-anchor + cross-reference + citation), not re-derivation or rename.

### §1.3 Three concrete notation-discipline enhancements

1. **Definition-anchor with explicit disambiguation at §B Definition A.3:** expand current definition to one additional clarifying sentence: *"Q(t) denotes remaining in-situ stock of resource R at time t, in mass-or-volume units appropriate to the resource class (barrels of oil, tonnes of copper ore, cubic meters of aquifer water). Q(t) is a stock variable, not an extraction-rate flow (cf. Hotelling 1931 q for extraction rate) and not a quality index (cf. Mussa-Rosen 1978 product-quality literature). The framework's choice of Q for stock follows the utility-function convention U(R, t, Q(t)), where Q indexes the marginal-utility-relevant state of the resource."*

2. **Cross-reference discipline at every theorem-statement, illustrative-example, and general-form appearance:** at Theorem E.4 statement, at McDowell illustrative example, and at §M general-form recovery, add one parenthetical referring to §B Definition A.3 — e.g., *"(per Definition A.3, Q(t) = remaining in-situ stock at time t)"*. This costs ~20 words across the Tech Appendix; eliminates the skim-reader misread risk.

3. **Bibliography note on convention choice:** in Tech Appendix §B (or in a new "Notational Conventions" subsection) add a citation-anchored note: *"The framework's Q-for-stock notation diverges from Hotelling 1931 + Pindyck 1978 (q/Q for extraction-rate flow) and from Mussa-Rosen 1978 + Spence 1976 + Tirole 1988 (Q for product quality). It follows the utility-function-of-state convention common in dynamic public-economics models (e.g., Dasgupta & Heal 1979 §8 use S for stock; we reserve S for substitutability, hence Q). Readers comparing the framework to resource-economics literature should map our Q(t) to Dasgupta-Heal S(t) or to Pindyck X(t)."*

### §1.4 Why this verdict pattern (not rename Q → X)

Considered alternative: rename Q(t) → X(t) (Pindyck-Slade-Thille convention). **Rejected** because:

- **Downstream sweep cost is substantial.** Q(t) appears in Tech Appendix v1.0.0 (13+ formula instances), Chapter 6 (3+ instances), Chapter 7 GuidanceDoc (8+ instances), terms_index entries for Substitutability Function + Externality Tail + RCV, glossary v3, and 4 prior rigor passes. Estimated rename effort: 1-2 days across all surfaces, plus regression check on chapter prose (where "Q is large" / "Q decreases" phrasing is currently fluent — would need rewriting to "X is large" / "X decreases" or to "stock is large" / "stock decreases").
- **Clarity gain is marginal.** A reader who pauses at U(R, t, Q(t)) and reads Definition A.3 disambiguates immediately. A reader who skims still gets the right reading from chapter prose (which always says "remaining stock Q at time t"). The misread risk is bounded.
- **Q-for-stock has internal coherence in the framework.** The framework's letter conventions are: R = resource (categorical), t = time, S = substitutability, U = utility, E = externality, D = discount, B = bond, P = price. Q sits in the third slot of U(R, t, Q) and reads naturally as "the resource-state at time t that determines utility." X(t) reads less naturally in U(R, t, X(t)) — feels like a generic state-space variable rather than a stock-of-this-specific-resource.
- **Three enhancements achieve the academic-peer-review readiness gate without the rename cost.** The journals that would reject the framework over Q(t) ambiguity (JEEM, JPubE, JEEM, AER, RAND) are exactly the journals that respond to definition-anchor + cross-reference + citation discipline. Adding a one-paragraph notational-conventions note + 3-5 cross-references closes the gap.

If the author preference is divergent (e.g., "the rename cost is acceptable for clean Pindyck-convention alignment"), §14.4 option (b) keeps the rename on the table with explicit cost estimate.

---

## §2. Question + scope

### §2.1 Triggering articulation

[Phase 1 §7.2 + §7.16 + §10 #7](commons_bonds_rigor_pass_2026-04-29_full_framework_audit_phase1_v1.0.0.md):

> *"Verdict: PASS — screening clean. Phase 2 notation-clarity verification recommended."* (§7.2)
>
> *"2 flagged for Phase 2 deeper dive: scarcity multiplier (academic-defensibility); RCV integrand Q(t) notation-clarity"* (§7.16)
>
> *"7. RCV integrand Q(t) notation-clarity (quality vs quantity ambiguity)"* (§10 item #7; handoff numbering #8)

Phase 2 (this rigor pass) executes the screening-recommended notation-clarity verification at academic-rigor depth.

### §2.2 What this audit produces

For pass/fail academic-rigor gate at top-tier journals (AER, QJE, JPE, JEEM, JPubE, RAND, *Resource and Energy Economics*) and academic-trade hybrid presses, the Q(t) notation must meet the following standards:

- Defined explicitly at first formula appearance with units, type (stock vs flow), and disambiguation against adjacent literatures.
- Cross-referenced at every subsequent appearance OR re-defined locally.
- Convention divergence from established literatures acknowledged with citation.
- Reader from any of the relevant adjacent lineages (resource economics, IO/quality-economics, environmental economics, welfare-economics) can immediately disambiguate the framework's usage.

This audit produces:
1. Per-test verdict (premise enumeration; logical derivation; collision check; etc.).
2. Concrete notation-discipline recommendations per gap.
3. Recommended formal disambiguation language for §B Definition A.3.
4. Cross-references to established economics-notation conventions (Hotelling 1931; Pindyck 1978; Dasgupta-Heal 1979; Mussa-Rosen 1978; Spence 1976; Tirole 1988; Slade-Thille 2009).

### §2.3 Pass/fail gate framing

Per author direction 2026-04-29: pass/fail gate on academic rigor for mathematical apparatus including notation. This audit applies the same standard to notation-clarity that the Theorem E.4 audit applied to proof-structure. Notation that produces a literature-collision-readable misreading at first encounter would not survive top-tier referee review.

### §2.4 What this pass does NOT cover

- Phase 2 deeper-dive on theorems E.1, E.2, E.3, E.5 — separate rigor passes per Insight #39 cross-reference (sibling session in progress 2026-04-29).
- Theorem-restructure ratification timing for Tech Appendix HTML edits — same open question as Insights #35 + #38 + #40.
- Scarcity multiplier formula academic-defensibility (Phase 2 candidate #7) — separate rigor pass; will follow this one in reverse-priority sequence.
- Chapter-prose Q-language sweep — if rename Q → X chosen at §14.4 option (b), full chapter-prose sweep is downstream implementation work, not rigor-pass scope.
- Bibliography accuracy + completeness audit (Insight #39 territory) — this pass identifies citation gaps but does not execute full bibliography expansion.

---

## §3. Methodology

### §3.1 Academic-rigor depth audit framework

For each test below, the audit (a) reads every appearance of Q(t) across Tech Appendix + chapters + terms_index + glossary + prior rigor passes; (b) tests against academic-peer-review notation-discipline standards as practiced at top-tier journals; (c) produces verdict (STRONG / ADEQUATE / WEAK / FAIL); (d) flags concrete repair work where verdict < STRONG.

### §3.2 Tests applied

1. **Premise enumeration** — is Q(t) explicitly defined at first formula appearance? Do subsequent appearances re-define locally OR cross-reference the canonical definition?
2. **Logical derivation** — does the framework's math depend on the stock-reading of Q(t), or does it admit equally well to a quality-reading or flow-reading?
3. **Edge case analysis** — what happens at Q(t) → 0 (stock depletion)? at Q(t) → ∞ (abundance)? at non-monotonic Q(t) (e.g., resource regenerated)?
4. **Collision check** — does Q-as-stock collide with established conventions in resource economics, IO/quality economics, environmental economics, welfare economics?
5. **Citation discipline** — is the notation choice anchored to a citable convention (e.g., Dasgupta-Heal 1979) or stranded?
6. **Falsifiability** — does the notation choice carry a claim that could be falsified, or is it pure convention?
7. **Domain of applicability** — does Q(t) read consistently as stock across all framework appearances, or does it shift meaning in some contexts?
8. **Counterexample resistance** — can a careful reader construct a reading of Q(t) (other than stock) under which the framework's equations still hold? If yes, the notation is genuinely ambiguous; if no, internal math forces the intended reading.

### §3.3 What the audit does NOT do

- Does NOT re-derive the RCV integrand or its components; that's §B definitional territory.
- Does NOT verify the empirical claim that ∂U/∂Q < 0 (utility increases as stock depletes); that's a Definition A.3 assumption.
- Does NOT replace pre-publication external review by credentialed third party (Insight #39 territory).
- Does NOT extend to other notation choices in the framework (S, U, E, D, B, R, t, t₀, λ, σ, etc. — separate discipline if needed).

---

## §4. Current state — close reading

### §4.1 Canonical definition (Tech Appendix §B Definition A.3)

[Tech Appendix v1.0.0 line 432-449](manuscript/technical-appendix/TechnicalAppendix_v1.0.0.html):

> **Definition A.3 (Stock-Dependent Utility) — UPDATED per Ripple Effects 1.0**
>
> U(R, t, Q(t)) represents generation t's utility from resource R being available in situ, conditional on remaining stock Q(t). U is:
>
> 1. Non-negative: U(R, t, Q) ≥ 0
> 2. Increasing in scarcity: ∂U/∂Q < 0 (utility per remaining unit increases as stock depletes)
> 3. Bounded below by market price: U(R, t, Q(t)) ≥ P(t) for all t ≥ t₀
>
> U(R, t, Q(t)) includes direct economic value, option value, and ecological function value. The ecological component is small at abundant stock levels and rises nonlinearly as Q approaches ecological thresholds, capturing keystone effects and ecosystem cascades.

### §4.2 All 13+ formula appearances

| Location | Line | Form | Locally defined? |
|---|---|---|---|
| Tech App §B Def A.3 | 435 | U(R, t, Q(t)) — primary definition | ✓ canonical |
| Tech App §B Def A.6 | 470 | RCV integrand full form | ✗ relies on §B.1 |
| Tech App §10 Theorem E.4 | 3285 | f(t) = {[1−S(t)]·U(R,t,Q(t)) + E(R,t)}·D | ✗ no re-def |
| Tech App McDowell example | 2821 | RCV_McDowell integrand | ✗ no re-def |
| Tech App McDowell C3 extension | 2845 | Three-term RCV with C3 | ✗ no re-def |
| Tech App §F existential analysis | 2552 | U(R, t, Q(t)) standalone | ✗ no re-def |
| Tech App §M general-form | 6924, 7062 | RCV(R, t0, Context) general-form | ✗ no re-def |
| Tech App §M.5 two-term recovery | 6948, 7020 | C1(R, t, Context) recovery | ✗ no re-def |
| Tech App Ripple Effects | 6732 | S(t \| t₀, Q(t)) coupling | ✗ no re-def (but Q_critical context disambiguates) |
| Tech App Hotelling cross-ref | 6086 | ∫[1−S(t)]U(R,t,Q(t))D(t)dt | ✗ no re-def |
| Tech App Rawlsian veil | 6125 | "stock-dependent utility term U(R,t,Q(t))" | ✓ phrase "stock-dependent" disambiguates |
| Tech App Asteroid biosphere | 5888 | "cannot be priced in commensurable units with U(R,t,Q(t))" | ✗ no re-def |
| Tech App §K formula breakdown | 1423, 1447, 1459 | various component breakdowns | ✗ no re-def |
| Ch 6 §B integrand intro | 320, 333 | RCV integrand + explicit local def | ✓ "remaining stock Q at time t" |
| Ch 7 GuidanceDoc | 99, 117, 123, 137, 157, 195, 235, 267, 295, 331, 333, 363 | 12 case-walkthrough instances | △ contextually disambiguates per case |
| terms_index Substitutability | 952, 962 | C₁(R, t, Q(t)) form | ✗ no re-def |
| terms_index Externality Tail | 1023 | RCV expanded form | ✗ no re-def |
| terms_index RCV definition | 1465 | "integrand form" listing | ✗ no re-def |
| Glossary v3 RCV | (search needed) | — | TBD |

**Pattern:** Q(t) is canonically defined at one place (Tech App §B Definition A.3) + chapter-prose redefined at one place (Ch 6 §B line 333) + contextually disambiguates at all Chapter 7 case walkthroughs. All other Tech Appendix appearances rely on the §B canonical definition without explicit cross-reference.

### §4.3 Initial reading observations

- **The math itself disambiguates.** Definition A.3 #2 (∂U/∂Q < 0) is the load-bearing premise: utility increases as Q decreases. This is the marginal-utility-of-scarcity claim, which is meaningful only if Q is a stock-quantity (more stock = lower marginal utility per unit). Under quality-reading, ∂U/∂Q < 0 would say "as quality decreases, utility increases" — which is the opposite of every IO model's quality-utility relationship (Mussa-Rosen 1978 et seq. all have ∂U/∂Q > 0 for higher quality). Under flow-reading (Q = extraction rate), ∂U/∂Q < 0 would say "as extraction rate decreases, utility increases" — which is non-standard and reads as a degrowth claim, not a stock-dependent-utility claim. The Definition A.3 #2 monotonicity locks in the stock-reading.

- **Chapter-prose disambiguates aggressively.** Every Chapter 7 case walkthrough uses the phrase "stock-dependent utility" or "remaining stock" or "Q decreases as stock depletes" — making the stock-reading impossible to miss in narrative form.

- **Tech Appendix appearances rely on canonical-definition-elsewhere.** Theorem E.4's recently-restructured statement (per Insight #40 ratified 2026-04-29) inherits Q(t) without re-defining it. Same for McDowell, §F, §M, §K. A referee reading E.4 without cross-referencing §B Definition A.3 could pause on Q(t).

- **Q_critical pairing reinforces stock-reading.** The Ripple Effects 1.0 update (Tech App line 6732) introduces Q_critical as a threshold; the pairing Q(t) → Q_critical in S(t | t₀, Q(t)) = S_base(t) · [1 − α · (Q_critical / Q(t))^β] is unambiguously a stock-threshold-approach pattern.

- **Convention divergence is real and uncited.** Hotelling 1931 used q (lowercase) for extraction-rate flow; Pindyck 1978 used X for stock + q for flow; Dasgupta-Heal 1979 used S for stock + R for extraction rate; Slade & Thille 2009 *J Econ Lit* survey uses x_t for stock + q_t for flow. None of these literatures use Q (uppercase) for stock. Mussa-Rosen 1978 uses Q for product-quality-index. Tirole 1988 *Theory of Industrial Organization* uses q for quantity. None of the established conventions match the framework's choice. This is not necessarily wrong (notation is convention, conventions can diverge with justification), but the divergence is currently unmarked.

---

## §5. Test 1 — Premise enumeration (notation introduction)

### §5.1 Current state

- Canonical definition exists at one location (Tech App §B Definition A.3).
- Chapter 6 redefines locally at line 333.
- All other appearances inherit silently.

For academic-publication discipline, the standard is: define at first appearance + cross-reference (or redefine) at every subsequent appearance in a separable section. The current approach satisfies "define at first appearance" but not "cross-reference at every subsequent appearance."

### §5.2 Verdict

**ADEQUATE.** Canonical definition is rigorous (units implicit, monotonicity stated, lower bound stated). Multiple appearances inherit without cross-reference; this is conventional in monograph-style prose but suboptimal for top-tier journal articles where each section is read standalone.

### §5.3 Repair recommendation

Add cross-reference parenthetical at three load-bearing appearances:
1. Theorem E.4 statement (Tech App §10 line 3285) — *"(Q(t) = remaining in-situ stock at time t per Definition A.3)"*.
2. McDowell illustrative example (Tech App §M McDowell, line 2821) — same parenthetical.
3. General-form §M.5 two-term recovery (line 6948 or 7020) — same parenthetical.

This costs ~30 words. Eliminates the standalone-section misread risk.

---

## §6. Test 2 — Logical derivation (does math depend on stock-reading?)

### §6.1 Current state

The framework's mathematics operates on Q(t) through three load-bearing channels:

**Channel 1: Definition A.3 #2 monotonicity (∂U/∂Q < 0).**
- Stock-reading: utility per unit increases as stock depletes. **Standard scarcity-utility claim.** Coherent with Hotelling 1931 + Hartwick 1977 + Solow 1974 lineages.
- Quality-reading: utility increases as quality decreases. **Backwards from IO literature.** Coherent with no established framework.
- Flow-reading: utility increases as extraction rate decreases. **Non-standard.** Reads as a degrowth claim, not a stock-dependent-utility claim.
- Verdict: monotonicity premise locks the stock-reading. Math is structurally incoherent under quality- or flow-readings.

**Channel 2: Definition A.3 #3 market-price lower bound (U(R, t, Q(t)) ≥ P(t)).**
- Stock-reading: in-situ utility per unit ≥ market price per unit. **Coherent.** P(t) is per-unit price; U is per-unit utility; both indexed to current stock state.
- Quality-reading: in-situ utility ≥ market price evaluated at quality Q. **Coherent in a different framework** (one with quality-differentiated pricing). Not what the framework asserts.
- Flow-reading: in-situ utility ≥ market price evaluated at extraction rate Q. **Coherent under Hotelling-rent-equals-extraction-rent framing**, which is exactly what Hotelling 1931 + the framework's §B.5 Hotelling Identity discusses. So flow-reading would conflate U with the Hotelling-rent path, which is not what the integrand intends.
- Verdict: market-price-bound premise admits multiple readings; the stock-reading is the simplest and matches Definition A.3 #2.

**Channel 3: Q_critical threshold coupling (Tech App line 6732, Ripple Effects 1.0).**
- S(t | t₀, Q(t)) = S_base(t) · [1 − α · (Q_critical / Q(t))^β]
- Stock-reading: as Q(t) → Q_critical, the substitutability function falls (the more depleted the stock, the harder to substitute). **Coherent.** Q_critical is the depletion threshold below which the resource enters tipping-point dynamics.
- Quality-reading: as Q(t) → Q_critical, substitutability falls. **Incoherent.** Q_critical wouldn't be a "quality threshold" in any standard framework; substitutability doesn't depend on quality of the depleted resource in this way.
- Flow-reading: as Q(t) (extraction rate) → Q_critical (extraction-rate threshold), substitutability falls. **Possibly coherent under degrowth framing** but doesn't match the framework's broader apparatus (which has Q as state, not flow).
- Verdict: Q_critical coupling forces stock-reading.

### §6.2 Verdict

**STRONG.** The framework's math operates on Q(t) through monotonicity (∂U/∂Q < 0), market-price boundedness, and Q_critical threshold coupling. The combination forces stock-reading. A reader who tries to substitute quality- or flow-reading produces incoherence (channel 1) or framework-divergent claims (channels 2, 3). Internal math is the strongest disambiguation discipline.

### §6.3 Repair recommendation

No repair needed at math level. Notation-discipline repair (definition-anchor + cross-reference) sufficient.

---

## §7. Test 3 — Edge case analysis

### §7.1 Q(t) → 0 (stock depletion)

Under Definition A.3 #2 (∂U/∂Q < 0), as Q(t) → 0, U(R, t, Q(t)) → ∞ (or to a very large value bounded by some context-specific ceiling). Under stock-reading, this is the marginal-utility-of-extreme-scarcity claim — the last unit of an irreplaceable resource has near-infinite per-unit utility (consistent with existential-substitutability-gap framing per [Phase 2 §F](commons_bonds_rigor_pass_2026-04-29_phase2_foreclosure_bond_housing_crisis_collision_v1.0.0.md) sibling).

This is the framework's intended behavior and matches Theorem E.4's knife-edge case (S_max < 1 ∧ r_∞ = 0 ∧ U unbounded above → divergence; per Insight #40 RATIFIED).

Under quality-reading, Q → 0 would mean "quality approaches zero" — interpretation: the resource's quality has degraded to nothing. ∂U/∂Q < 0 would imply utility goes UP as quality goes DOWN, which is incoherent. Edge case fails under quality-reading.

Under flow-reading, Q → 0 would mean "extraction rate approaches zero" — interpretation: nobody is extracting. U → ∞ would imply utility approaches infinity as extraction stops. This is a degrowth-style claim; coherent in some frameworks (e.g., Hartwick rule with non-renewable: stop extraction → preserve stock → infinite future-utility), but inconsistent with the framework's RCV-integrand structure (where Q(t) is the state of the stock at time t, not a control variable on extraction).

Verdict for Q → 0: **STRONG (stock-reading) / FAILS (quality-reading) / INCOHERENT-WITH-FRAMEWORK (flow-reading).**

### §7.2 Q(t) → ∞ (abundance)

Under Definition A.3 #2 (∂U/∂Q < 0), as Q → ∞, ∂U/∂Q < 0 means U decreases. With Definition A.3 #3 (U ≥ P(t)), U bounded below by market price; P(t) presumably also low under abundance. So U → P(t) → low bound under abundance. **Coherent under stock-reading.** This is the framework's correct prediction: abundant stocks have low marginal utility per unit (the iron-asteroid case in Ch 7).

Under quality-reading, Q → ∞ would mean "quality approaches infinity" — meaningless edge case. Quality-indices are bounded (typically [0, 1] or [0, Q_max]).

Under flow-reading, Q → ∞ would mean "extraction rate approaches infinity" — coherent in a flow framework but not what the integrand encodes.

Verdict for Q → ∞: **STRONG (stock-reading) / INCOHERENT (quality-reading) / FRAMEWORK-DIVERGENT (flow-reading).**

### §7.3 Non-monotonic Q(t) (e.g., regenerated stock)

If Q(t) increases over time (e.g., renewable resource recovering after extraction event), Definition A.3 implies U decreases (more stock → lower per-unit utility). **Coherent under stock-reading.** This matches the renewable-imperative framing.

Under quality-reading, non-monotonic Q means quality fluctuating — possible in some frameworks but the integrand's coupling to S(t | t₀, Q(t)) doesn't naturally accommodate quality-fluctuation interpretation.

Under flow-reading, non-monotonic Q means extraction rate fluctuating — coherent but separate from what U(R, t, Q(t)) is asserting.

Verdict: **STRONG (stock-reading) / WEAK BUT COHERENT (quality-reading) / FRAMEWORK-DIVERGENT (flow-reading).**

### §7.4 Aggregate edge case verdict

**STRONG.** Stock-reading is coherent across all edge cases; quality-reading fails or is incoherent; flow-reading is framework-divergent. Internal edge-case behavior provides additional disambiguation discipline.

### §7.5 Repair recommendation

No repair needed at edge case level.

---

## §8. Test 4 — Collision check against established conventions

### §8.1 Resource economics lineage (Hotelling, Pindyck, Dasgupta-Heal, Slade-Thille)

| Reference | Notation for stock | Notation for flow |
|---|---|---|
| Hotelling 1931 *JPE* "The Economics of Exhaustible Resources" | (implicit; cumulative production R(t) → R_max) | q (lowercase) |
| Pindyck 1978 *JPE* "The Optimal Exploration and Production of Nonrenewable Resources" | X(t) | q(t) |
| Dasgupta & Heal 1979 *Economic Theory and Exhaustible Resources* | S(t) | R(t) |
| Solow 1974 *Rev Econ Stud* "Intergenerational Equity and Exhaustible Resources" | (per Hartwick lineage) | — |
| Hartwick 1977 *AER* "Intergenerational Equity and the Investing of Rents" | S (cumulative reserve) | — |
| Slade & Thille 2009 *J Econ Lit* "Whither Hotelling: Tests of the Theory of Exhaustible Resources" | x_t | q_t |
| Pindyck 2007 *J Econ Lit* "Uncertainty in Environmental Economics" | X (or various) | — |

**Convention pattern:** Q (uppercase) is **not used** for stock in the major resource-economics lineage. The framework's use of Q for stock is non-standard.

**Why does this matter?** A reader from resource economics (the natural primary academic audience for Tier 2a) sees U(R, t, Q(t)) and recognizes neither X(t) nor S(t) for stock. Default reading at first encounter could be: q-extraction-rate (Hotelling), product-quality (IO), or generic "quantity." Each requires correction by cross-referencing Definition A.3.

### §8.2 IO / quality-economics lineage (Mussa-Rosen, Spence, Tirole)

| Reference | Notation for quality |
|---|---|
| Spence 1976 *Rev Econ Stud* "Product Selection, Fixed Costs, and Monopolistic Competition" | q (or u) |
| Mussa & Rosen 1978 *J Econ Theory* "Monopoly and Product Quality" | q (lowercase) |
| Tirole 1988 *The Theory of Industrial Organization* | s (for quality), q (for quantity) |
| Anderson & Renault 2009 *J Econ Theory* | q (quality) |

**Convention pattern:** Q (uppercase) appears for both quality (Mussa-Rosen et seq.) and quantity (generic micro). A reader from IO/quality-economics sees U(R, t, Q(t)) and can reasonably default to "Q is a quality index of the resource."

**Why does this matter?** The framework's adjacent-literature citations include Hotelling Identity (resource economics) but also welfare-economics (Pigou, Stern Review, Rawls) and policy-economics (Mazzucato 2020). A multi-literature audience inherits multiple Q-conventions. The collision risk is real.

### §8.3 Environmental / ecological-economics lineage

| Reference | Notation for ecosystem stock |
|---|---|
| Costanza et al. 1997 *Nature* | (various; ES_i) |
| Hartwick rule literature | S (sustainability rule) |
| Stern Review 2007 | (various; not standardized) |
| Daly 1973 *Toward a Steady-State Economy* | S, K |

**Convention pattern:** No standard. Environmental economics has not converged on a Q/X/S convention for stock. Framework's Q is no more divergent here than alternatives.

### §8.4 Welfare / public-economics lineage

Welfare economics (Pigou 1920; Pareto; Samuelson 1954; Stiglitz 2000; Mazzucato 2020) typically uses U for utility without specifying a stock-dependent argument. The framework's U(R, t, Q(t)) is a specialization that introduces Q(t) as a third argument. Convention is not collision-relevant here because welfare economics doesn't have a standard Q-stock convention to collide with.

### §8.5 Verdict

**WEAK.** The framework's Q-for-stock notation collides with:
- Resource economics convention (Q is not used for stock; X(t), x_t, or S(t) is).
- IO/quality-economics convention (Q is used for quality).

The collision is uncited and unmarked. A referee from JEEM, AER, *Resource and Energy Economics*, or *J Environ Econ Manage* would flag this on first read. The repair work is acknowledgment + citation, not rename.

### §8.6 Repair recommendation

In §B Definition A.3 (or in a new §B.0 "Notational Conventions" subsection), add a citation-anchored note explicitly acknowledging the divergence:

> **Notational note on Q(t).** The framework's choice of Q (uppercase) for remaining in-situ stock diverges from established resource-economics convention (Hotelling 1931 q for extraction rate; Pindyck 1978 X(t) for stock; Dasgupta & Heal 1979 S(t) for stock; Slade & Thille 2009 x_t for stock) and from industrial-organization quality-economics convention (Mussa & Rosen 1978; Spence 1976; Tirole 1988 — Q for product-quality index). Our choice follows the utility-function-of-state pattern: in U(R, t, Q(t)), Q indexes the marginal-utility-relevant state of the resource, which for non-renewable extraction is remaining stock. We reserve S for the substitutability function (per Definition A.2), which precludes the Dasgupta-Heal S-for-stock notation. Readers comparing this framework to the Pindyck or Dasgupta-Heal apparatus should map our Q(t) to their X(t) or S(t) respectively.

This note costs ~120 words. Closes the collision-check gap.

---

## §9. Test 5 — Citation discipline

### §9.1 Current state

No citation explaining the Q-for-stock notation choice. Definition A.3 defines Q(t) operationally without convention-anchor.

### §9.2 Verdict

**WEAK.** Top-tier journal review expects notation choices that diverge from established conventions to be (a) acknowledged and (b) cited. Currently: not acknowledged; not cited.

### §9.3 Repair recommendation

Per §8.6 above, add the notational note with inline citations to:
- Hotelling 1931 *JPE* — for the q-extraction-rate convention divergence.
- Pindyck 1978 *JPE* — for the X-for-stock convention divergence.
- Dasgupta & Heal 1979 *Economic Theory and Exhaustible Resources* — for the S-for-stock convention divergence.
- Mussa & Rosen 1978 *J Econ Theory* — for the Q-for-quality convention divergence.
- Slade & Thille 2009 *J Econ Lit* — for the x-for-stock + q-for-flow modern convention.

Bibliography expansion: add Pindyck 1978, Dasgupta-Heal 1979, Mussa-Rosen 1978, Slade-Thille 2009 (Hotelling 1931 already in bibliography per Hotelling Identity §12 multi-audience re-rigor).

---

## §10. Test 6 — Falsifiability

### §10.1 Current state

Notation-choice is not a claim that can be falsified. The underlying concept (stock-dependent utility per Definition A.3 #2 monotonicity) IS falsifiable (∂U/∂Q < 0 is an empirical claim), but that's a separate Definition A.3 audit, not a Q(t) notation audit.

### §10.2 Verdict

**N/A.**

### §10.3 Repair recommendation

None at notation level. (Definition A.3 #2 monotonicity falsifiability would be a separate audit if needed.)

---

## §11. Test 7 — Domain of applicability

### §11.1 Current state

Q(t) appears 13+ times across Tech Appendix + 12+ times in Ch 7 + 3+ times in Ch 6 + 3+ times in terms_index. Every appearance reads as remaining-in-situ-stock.

No instance found where Q(t) reads as quality-index or extraction-rate-flow.

### §11.2 Verdict

**STRONG.** Domain of applicability for the framework's Q(t) usage is consistent across all surfaces.

### §11.3 Repair recommendation

None at domain level. (Cross-reference discipline per §5.3 closes the academic-publication gap.)

---

## §12. Test 8 — Counterexample resistance

### §12.1 Approach

Try to construct a reading of Q(t) other than stock under which the framework's RCV equations still produce the framework's policy claims.

### §12.2 Constructed attempts

**Attempt 1 (Q = quality):** U(R, t, Q(t)) = utility from resource of quality Q at time t. Definition A.3 #2 (∂U/∂Q < 0): utility decreases as quality increases. **FAILS.** Quality-reading produces wrong-direction monotonicity. The framework's claim is incoherent under quality-reading.

**Attempt 2 (Q = extraction-rate flow):** U(R, t, Q(t)) = utility from extraction at rate Q at time t. Definition A.3 #2 (∂U/∂Q < 0): utility decreases as extraction rate increases. **WEAKLY COHERENT** (extraction-utility curves can be concave in flow under congestion or social-cost framings) **BUT FRAMEWORK-DIVERGENT.** RCV integrand semantics require U to be in-situ utility (the value to future generations of the resource being available, not yet extracted). Flow-reading conflates U with extraction-flow utility, which is closer to producer-surplus than to in-situ-future-generation utility. The framework's claim survives flow-reading but is no longer the framework's claim.

**Attempt 3 (Q = consumption rate):** U(R, t, Q(t)) = utility from consumption at rate Q at time t. ∂U/∂Q < 0: utility decreases as consumption rate increases. **NOT STANDARD** (consumption utility is typically ∂U/∂Q > 0). Framework-divergent.

**Attempt 4 (Q = some abstract quality-quantity composite):** U(R, t, Q(t)) where Q is an aggregated state-variable. ∂U/∂Q < 0. **POSSIBLE BUT VACUOUS** — the framework would need to specify what Q is composed of; absent specification, this is just stock-reading with extra steps.

### §12.3 Verdict

**ADEQUATE.** Quality-reading is incoherent. Flow-reading and consumption-reading produce framework-divergent claims (the math survives but the framework's policy claim doesn't). No reading other than stock produces the framework's intended RCV claims under the Definition A.3 monotonicity premise.

### §12.4 Repair recommendation

None at counterexample-resistance level. The math + Definition A.3 monotonicity premise jointly force stock-reading. Notation-discipline repairs (§5 + §8 + §9) close the academic-publication gap; counterexample resistance is already strong.

---

## §13. Recommended formal restatement

### §13.1 §B Definition A.3 expansion (recommended replacement text)

> **Definition A.3 (Stock-Dependent Utility).**
>
> U(R, t, Q(t)) represents generation t's per-unit utility from resource R being available in situ at time t, conditional on remaining stock Q(t).
>
> *Notation:* Q(t) denotes remaining in-situ stock of resource R at time t, in mass-or-volume units appropriate to the resource class (barrels of oil, tonnes of copper ore, cubic meters of aquifer water, square kilometers of intact ecosystem). Q(t) is a stock state-variable, not an extraction-rate flow (cf. Hotelling 1931 q for extraction rate; Pindyck 1978 q(t)) and not a quality index (cf. Mussa & Rosen 1978; Spence 1976; Tirole 1988 — Q for product quality). The framework's choice of Q for stock follows the utility-function-of-state convention U(R, t, Q(t)), where Q indexes the marginal-utility-relevant state of the resource. We reserve S for the substitutability function (per Definition A.2), which precludes Dasgupta & Heal 1979's S-for-stock convention; readers comparing this framework to Pindyck 1978's X(t) or Dasgupta-Heal's S(t) should map our Q(t) accordingly.
>
> U is:
>
> 1. **Non-negative:** U(R, t, Q) ≥ 0.
> 2. **Increasing in scarcity:** ∂U/∂Q < 0 (per-unit utility increases as stock depletes).
> 3. **Bounded below by market price:** U(R, t, Q(t)) ≥ P(t) for all t ≥ t₀ (in-situ value cannot be less than the market-price-revealed extraction value).
>
> U(R, t, Q(t)) includes direct economic value, option value, and ecological function value. The ecological component is small at abundant stock levels and rises nonlinearly as Q approaches ecological thresholds, capturing keystone effects and ecosystem cascades.

### §13.2 Cross-reference parentheticals (recommended additions)

At three load-bearing Tech Appendix appearances, add a one-line parenthetical:

- **Theorem E.4 statement (line 3285):** add *"(per Definition A.3, Q(t) = remaining in-situ stock at time t)"* on first Q(t) appearance in the proof.
- **McDowell illustrative example (line 2821):** add *"(Q(t) = remaining stock per Definition A.3)"* after first Q(t) appearance.
- **General-form §M.5 two-term recovery (line 6948 or 7020):** add *"(Q(t) per Definition A.3)"* after first Q(t) appearance.

Optional additional cross-references:
- §F existential analysis (line 2552).
- §K formula breakdowns (lines 1423, 1447, 1459).
- terms_index Substitutability Function entry (line 952, 962).
- terms_index Externality Tail entry (line 1023).
- terms_index RCV integrand entry (line 1465).
- Glossary v3 RCV entry.

### §13.3 Bibliography expansion

Add to bibliography (per §9.3):
- Pindyck, Robert S. 1978. "The Optimal Exploration and Production of Nonrenewable Resources." *Journal of Political Economy* 86(5): 841-861.
- Dasgupta, Partha, and Geoffrey Heal. 1979. *Economic Theory and Exhaustible Resources*. Cambridge: Cambridge University Press.
- Mussa, Michael, and Sherwin Rosen. 1978. "Monopoly and Product Quality." *Journal of Economic Theory* 18(2): 301-317.
- Slade, Margaret E., and Henry Thille. 2009. "Whither Hotelling: Tests of the Theory of Exhaustible Resources." *Journal of Economic Literature* 47(4): 1067-1102.
- Spence, A. Michael. 1976. "Product Selection, Fixed Costs, and Monopolistic Competition." *Review of Economic Studies* 43(2): 217-235.
- Tirole, Jean. 1988. *The Theory of Industrial Organization*. Cambridge, MA: MIT Press.

(Hotelling 1931 already in bibliography per Hotelling Identity §12 multi-audience re-rigor 2026-04-29.)

---

## §14. Verdict + ratification choices

### §14.1 Recommended verdict

**KEEP Q(t) notation with three concrete notation-discipline enhancements per §13.** The substance is sound; the math forces stock-reading; the repair work is academic-publication notation-discipline, not re-derivation or rename.

Three concrete enhancements:

1. **§B Definition A.3 expansion (per §13.1)** — explicit notational note with units, type-disambiguation, citation to divergent conventions, mapping advice for resource-economics readers.

2. **Cross-reference parentheticals at three load-bearing Tech Appendix appearances (per §13.2)** — Theorem E.4 statement; McDowell illustrative example; §M.5 general-form two-term recovery. Optionally extend to §F, §K, and terms_index entries.

3. **Bibliography expansion (per §13.3)** — Pindyck 1978; Dasgupta-Heal 1979; Mussa-Rosen 1978; Slade-Thille 2009; Spence 1976; Tirole 1988.

### §14.2 Pass-fail verdict on as-currently-written Q(t) usage

**ADEQUATE-WEAK.** Would survive sympathetic-referee review at top-tier journals on internal-coherence grounds (math forces stock-reading) but would be flagged on convention-divergence grounds (uncited Q-for-stock choice diverges from Hotelling/Pindyck/Dasgupta-Heal lineage and from Mussa-Rosen IO lineage; the divergence is unmarked).

### §14.3 Pass-fail verdict on enhanced Q(t) usage per §13

**STRONG.** With three enhancements applied, notation discipline meets academic-peer-review standards. Citation-anchored convention divergence; consistent cross-reference; explicit type-disambiguation in primary definition.

### §14.4 Author ratification choices

**(a) Full ratify §13 enhancements** — all three enhancements applied; Tech Appendix HTML edited to add notational note + cross-reference parentheticals + bibliography. **Recommended.**

**(b) Rename Q(t) → X(t) full sweep** — Pindyck-Slade-Thille convention alignment. Cost estimate: 1-2 days across Tech Appendix (13+ instances) + Ch 6 (3+ instances) + Ch 7 GuidanceDoc (8+ instances; chapter-prose phrasing rewrites) + terms_index (3+ instances) + glossary v3 + 4 prior rigor passes (cross-reference updates). Trade-off: clean convention-alignment but high downstream cost; net clarity gain marginal because internal math already disambiguates.

**(c) Partial ratify** — adopt subset:
- (c.i) §B Definition A.3 expansion only (highest-leverage enhancement).
- (c.ii) §B Definition A.3 expansion + bibliography expansion; defer cross-reference parentheticals.
- (c.iii) Cross-reference parentheticals only; defer §B expansion.

**(d) Modify verdict** — author specifies different recommendation (e.g., simpler note; different citation set; different rename target like N(t) or W(t)).

**(e) Defer Phase 2 ratification** — additional questions before locking; possibly bundle with Phase 2 #7 scarcity multiplier formula audit (sibling next rigor pass) for combined notation-discipline ratification.

**(f) Reject** — author rejects audit findings (would require justifying why current Q(t) usage survives academic peer review without enhancement).

**Recommendation: (a) Full ratify.** Three enhancements are mutually-reinforcing and total ~150 words of Tech Appendix text plus 6 bibliography entries; partial ratification leaves the convention-divergence gap open. Rename (option b) achieves no additional clarity over option (a) given the internal-math disambiguation, and incurs substantially higher downstream cost.

### §14.5 Implementation pending after ratification

If (a) full ratify:
1. Tech Appendix v1.0.0 HTML §B Definition A.3 — replace current text with §13.1 expansion.
2. Tech Appendix v1.0.0 HTML §10 Theorem E.4 + McDowell + §M.5 — add §13.2 cross-reference parentheticals (3 load-bearing locations; optionally 5+ additional locations).
3. Bibliography expansion per §13.3.
4. terms_index — add Phase 2 verdict entry; cross-reference to this rigor pass.
5. Open Insights — new Insight # closed-ratified entry capturing Phase 2 #8 verdict (number TBD; coordinate with sibling theorem rigor pass session).

**Same open question as Insights #35 + #38 + #40 Tech Appendix HTML edit timing:** apply now to v1.0.0 vs batch into Phase 3 v2.0.0 rebuild. **Possible unification:** all Phase 2 Tech Appendix changes batched into Phase 3 v2.0.0 rebuild as single coordinated update.

### §14.6 Pre-publication external review (Insight #39)

This rigor pass produces Claude's assessment of Q(t) notation discipline. Per Insight #39, eventual external review by economics PhD or formal-methods expert is warranted before publication. Specifically for Q(t): a resource-economist reviewer should verify:
- The Q-for-stock convention is stated with sufficient prominence to disambiguate at first formula encounter.
- The Hotelling/Pindyck/Dasgupta-Heal/Mussa-Rosen citation set is the right disambiguation lineage to cite (vs. a reduced or expanded set).
- The mapping advice ("readers should map our Q(t) to Pindyck X(t)") is helpful rather than confusing.

This rigor pass does NOT replace external review; it produces the substrate that external review would test.

---

## §15. Open questions for author discussion

1. **Cross-coordination with sibling theorem-rigor-pass session.** The sibling session is currently auditing E.1, E.3, E.5, Renewable Imperative theorems; those proofs reference Q(t) in U(R, t, Q(t)). If this Phase 2 #8 audit recommends Q-notation enhancements, the theorem-rigor recommendations should coordinate (either inherit the §13 enhancements automatically, or flag at ratification time for batched application). **Recommended:** ratify Phase 2 #8 first (this rigor pass) so the theorem-rigor recommendations can reference §13.1 Definition A.3 expansion as the canonical Q(t) definition.

2. **Notational note placement.** Current §13.1 puts the notational note inside Definition A.3. Alternative: create a new §B.0 "Notational Conventions" subsection that consolidates Q(t) note + any other notation-discipline notes (e.g., S(t|t₀) substitutability conditional notation; D(t,t₀) discount notation; R categorical-vs-extracted-unit notation). Trade-off: A.3 placement is local + immediate; §B.0 placement is consolidated + cleaner but requires future notation audits to populate.

3. **Bibliography expansion scope.** Current §13.3 adds 6 references (Pindyck 1978, Dasgupta-Heal 1979, Mussa-Rosen 1978, Slade-Thille 2009, Spence 1976, Tirole 1988). Are all 6 needed, or can the citation set be reduced to (e.g.) 3 (Pindyck 1978, Dasgupta-Heal 1979, Mussa-Rosen 1978) for tighter discipline? Trade-off: 6 covers all major divergence sources comprehensively; 3 is leaner but leaves IO-quality lineage less fully cited.

4. **Cross-reference scope.** §13.2 recommends 3 mandatory cross-reference parentheticals (Theorem E.4, McDowell, §M.5) + 5+ optional (§F, §K, terms_index entries, glossary). Author preference on scope: minimal (3 mandatory only), full (3 + all 5+ optional), or extended (cross-reference at every Q(t) appearance).

5. **Tech Appendix HTML edit timing.** Same open question as Insights #35 + #38 + #40 — apply now to v1.0.0 vs batch into Phase 3 v2.0.0 rebuild?

6. **Glossary v3 update.** Should the glossary v3 RCV entry inherit the §13.1 Q(t) notational note, or keep glossary entries terse and cross-reference Tech Appendix for notation? The author's vocabulary-strategy v1.0.1 multi-audience matrix suggests glossary should serve Tier 1 + Tier 2c (lay + policy-practitioner) audiences who need quick reference; full notational note may exceed glossary scope. **Recommended:** glossary keeps its current terse RCV entry; Tech Appendix carries the full §13.1 expansion.

7. **Phase 2 #7 (scarcity multiplier) bundling.** Phase 1 §16.3 noted #7 + #8 "likely bundle." After producing this #8 audit, my assessment is they are conceptually distinct (notation-clarity vs functional-form-defensibility) and should ratify separately. Confirm or override?

---

## §16. Cross-references

### §16.1 Upstream rigor passes

- [Phase 1 full framework audit §7.2 + §7.16 + §10 #7](commons_bonds_rigor_pass_2026-04-29_full_framework_audit_phase1_v1.0.0.md) — flagged Q(t) notation-clarity for Phase 2 deeper-dive.
- [Phase 2 Theorem E.4 Integral Convergence §13.2 + §16.3](commons_bonds_rigor_pass_2026-04-29_phase2_theorem_e4_integral_convergence_v1.0.0.md) — RATIFIED 2026-04-29 (Insight #40); restructured E.4 statement uses Q(t) in U(R, t, Q(t)) without re-definition (this pass's §13.2 cross-reference parenthetical fills that gap).
- [Phase 2 Foreclosure Bond housing-crisis collision](commons_bonds_rigor_pass_2026-04-29_phase2_foreclosure_bond_housing_crisis_collision_v1.0.0.md) — RATIFIED 2026-04-29 (Insight #38); methodology template.
- [Phase 2 Cost Severance + Severed Cost Tier 2d](commons_bonds_rigor_pass_2026-04-29_phase2_cost_severance_severed_cost_tier2d_v1.0.0.md) — RATIFIED 2026-04-29 (Insight #35); methodology template.
- [Vocabulary strategy v1.0.1 §2 + §8 multi-audience matrix](alignment/commons_bonds_vocabulary_strategy_v1.0.1.md) — Tier 2a + 2e collision-check discipline applied here.

### §16.2 Sibling Phase 2 candidates (concurrent + remaining)

- **Phase 2 #3 Theorems E.1, E.3, E.5, Renewable Imperative academic-rigor proof-structure audit** — sibling session in progress 2026-04-29 (started ~2 hours before this pass; on E.1 sub-audit 3.1). Theorem-rigor recommendations should coordinate with this Phase 2 #8 verdict (cross-coordination per §15 Q1).
- **Phase 2 #7 Scarcity multiplier formula academic-defensibility** — next in reverse-priority sequence (this session, after Phase 2 #8 ratification or in parallel as separate proposed doc).
- **Phase 2 #6 Three Ways of Counting post-rename adoption-fit verification** — minor; pending.
- **Phase 2 #5 Externality Tail statistics-distribution-tail collision** — pending.
- **Phase 2 #4 RCV acronym collision audit** — pending.

### §16.3 Downstream artifacts (this pass would update on ratification)

- `manuscript/technical-appendix/TechnicalAppendix_v1.0.0.html` §B Definition A.3 (line 432-449) — expanded text per §13.1.
- `manuscript/technical-appendix/TechnicalAppendix_v1.0.0.html` §10 Theorem E.4 statement (line 3285) + McDowell (line 2821) + §M.5 (line 6948 or 7020) — cross-reference parentheticals per §13.2.
- `manuscript/technical-appendix/TechnicalAppendix_v1.0.0.html` bibliography section — Pindyck 1978, Dasgupta-Heal 1979, Mussa-Rosen 1978, Slade-Thille 2009, Spence 1976, Tirole 1988 additions.
- `tools/back-matter/sources/terms_index.md` — Phase 2 verdict entry; cross-reference to this rigor pass.
- `alignment/commons_bonds_open_insights_v1.0.0.md` — new Insight # closed-ratified capturing Phase 2 #8 verdict (number TBD; coordinate with sibling theorem-rigor passes).

### §16.4 Pre-publication external review (Insight #39)

This rigor pass + 4 sibling Phase 2 deeper-dive passes (#7, #6, #5, #4) + 4 sibling theorem rigor passes (E.1, E.2, E.3, E.5) produce Claude's pre-external-review assessment substrate. Per Insight #39, eventual external review by economics PhD + formal-methods expert is warranted before publication. Multi-reviewer approach likely needed given the framework's cross-disciplinary scope (resource economics + welfare economics + IO/quality economics + intergenerational economics).

---

**End of Phase 2 deeper-dive rigor pass v1.0.0 [PROPOSED — pending author ratification].**
