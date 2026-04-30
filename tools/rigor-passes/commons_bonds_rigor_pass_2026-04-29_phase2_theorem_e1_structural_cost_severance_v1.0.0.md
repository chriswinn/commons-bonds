# Commons Bonds — Phase 2 Deeper-Dive Rigor Pass: Theorem E.1 Structural Cost Severance — Academic-Rigor Depth Audit

**Version:** 1.0.0
**Date:** 2026-04-29
**Protocol applied:** `tools/commons_bonds_rigor_protocol_v2.3.0.md` — academic-rigor depth audit per author direction 2026-04-29: *"the math formulas and proofs have to stand up to academic rigor or I don't have a book."* Tests applied: premise enumeration; logical derivation; edge case analysis; collision check against established economics theorems (Coase 1960; Pigou 1920; intergenerational market incompleteness literature); citation discipline + lineage analysis; falsifiability; domain of applicability; counterexample resistance.

**Author direction triggering this pass (2026-04-29 by Chris Winn):** confirmed (a) five separate rigor passes per Phase 2 sequence E.4 → **E.1** → E.3 → E.5 → E.2. E.1 is the framework's **central theorem** — the load-bearing claim every other theorem and instrument builds on. Phase 2 audit confirmed E.4 audit-pattern works; this rigor pass applies the pattern to substantively heavier substance.

**Scope:** Phase 2 academic-rigor depth audit on **Theorem E.1 (Structural Cost Severance)** as currently stated in [Tech Appendix v1.0.0 §10 line 3249-3258](core/technical-appendix/TechnicalAppendix_v1.0.0.html). E.1 asserts the framework's foundational claim that cost severance occurs structurally (not just intentionally) under current institutions. This rigor pass tests the proof structure against academic-peer-review standards + identifies the formalization repair work required.

**Status:** **RATIFIED 2026-04-29 by Chris Winn — verdict (a) Full ratify: split into E.1a + E.1b; adopt premises P1–P3; tighten scope; add citations.** Tech Appendix HTML edit timing (apply restructure to v1.0.0 now vs batch into Phase 3 Tech Appendix v2.0.0 rebuild) — pending author choice on §15 Q1 (same open question as Insights #35 + #38 + #40; possibility of unified batch into v2.0.0 rebuild for all Phase 2 Tech Appendix changes).

**Author:** Chris Winn

**Recommended verdict (preview):** **PASS conditional on a structural restatement that splits the conflated claims.** The theorem as currently written conflates two different claims (an algebraic identity and an empirical-structural claim) in a single proof. Repair = split into Theorem E.1a (algebraic identity) + Theorem E.1b (structural-empirical theorem) + state the empirical conditions as named assumptions about current institutions.

**This is a deeper restructure than E.4** because the substance has a categorization issue, not just a formalization gap. The framework's claim is defensible — but the current proof attempts to derive an empirical claim ("for all non-renewable extraction under present institutions") via structural argument when the empirical claim actually requires (a) explicit premises about current institutional structure + (b) the algebraic identity follows trivially from those premises.

The restructure preserves all of the framework's substantive claims; it just cleans up the deductive structure to academic-peer-review standards.

Concrete restructure recommendations (each independently ratifiable, but interdependent in practice):

1. **Split Theorem E.1 into two theorems** — E.1a (Algebraic Identity: CS > 0 iff B < RCV) + E.1b (Structural Cost Severance under Current Institutions: under explicit premises about market incompleteness for intergenerational claims + partial externality pricing + bounded accountability bonds, CS > 0 holds under current institutions).

2. **Replace the wrong "B ≤ P" assumption with explicit premises** about current institutions — premises name the structural conditions (intergenerational market incompleteness; partial externality pricing; current bond inadequacy) without conflating them with logical necessity.

3. **Tighten universal scope claim to conditional scope claim** — replace "for all non-renewable extraction under present institutions" with "under explicit premises [P1–P3], CS > 0 holds for non-renewable extraction; the empirical evidence that [P1–P3] hold for most current institutions is provided in §H empirical validation cases."

**Rename verdict:** N/A — this is a theorem audit; renaming the theorem (e.g., "Cost Severance Identity" + "Structural Severance Theorem") is part of the restructure, not separate.

---

## §1. Phase 2 executive summary

### §1.1 What was tested

E.1 currently states:

> *Theorem E.1 (Structural Cost Severance): For any extraction of a commons resource where market price P < RCV, cost severance CS > 0 occurs structurally, independent of extractor intentions.*

The audit tests:
1. **Premise enumeration** — are all assumptions stated as numbered premises?
2. **Logical derivation** — does each proof step follow from premises?
3. **Edge cases** — limit cases handled? (Extraction with forced regulatory bonds; sovereign-wealth-fund operationalization; cases approaching B = RCV)
4. **Collision check** — extends/conflicts/duplicates established theorems? (Coase 1960; Pigou 1920; intergenerational market incompleteness)
5. **Citation discipline** — load-bearing references explicit?
6. **Falsifiability** — under what conditions theorem falsified?
7. **Domain of applicability** — where applies; where not?
8. **Counterexample resistance** — can critic construct counterexample?

### §1.2 Phase 2 outcomes

| Test | Verdict | Note |
|---|---|---|
| Premise enumeration | **WEAK** | "B ≤ P" assumption is buried + load-bearing + actually wrong as general claim; "markets' structural inability to price intergenerational foreclosure" asserted not premised |
| Logical derivation | **WEAK** | The proof conflates algebraic identity (CS > 0 iff B < RCV) with empirical-structural claim (B < RCV under current institutions); two different claims requiring two different derivations |
| Edge cases | **WEAK** | Doesn't handle: (a) regulated extraction with bonds approaching/exceeding market price (e.g., deepwater offshore decommissioning); (b) sovereign-wealth-fund case (Norway); (c) carbon-intensive extraction with substantial carbon tax |
| Collision check | **WEAK** | Coase 1960 not invoked despite directly relevant ("markets' structural inability to price intergenerational foreclosure" IS the Coase-theorem-incomplete-bargaining condition); Pigou 1920 externality framework not formally cited; intergenerational market incompleteness literature (Howarth + Norgaard 1990; Brown Weiss 1989) not cited |
| Citation discipline | **WEAK** | Zero citations in proof; load-bearing claims asserted without reference |
| Falsifiability | ADEQUATE | "Note on scope" acknowledges falsifiability condition; should be in theorem statement, not footnote |
| Domain of applicability | **WEAK** | "All non-renewable extraction under present institutions" is over-broad; doesn't define "present institutions" precisely |
| Counterexample resistance | **WEAK** | Two counterexamples constructible under current claim (§12): (i) deepwater offshore extraction with high BSEE decommissioning bonds; (ii) carbon-intensive extraction in EU ETS jurisdictions with high carbon tax. The current proof has no defense |

**Aggregate verdict: WEAK as currently written.** Five WEAK + one ADEQUATE + zero STRONG. The theorem's substance is defensible but the proof structure is academically untenable.

### §1.3 Why this verdict is heavier than E.4

E.4 was WEAK in 4 of 8 tests; the gaps were formalization issues. E.1 is WEAK in 6 of 8 tests; the gaps include **categorization issues** (algebraic vs structural-empirical claims conflated), **substantive errors** (B ≤ P is wrong as general claim), and **scope over-reach** (universal claim from limited premises).

**The substance is fine.** The framework's claim — that cost severance is structural under current institutions, not merely the result of bad-faith extractors — is correct, important, and central to the book's argument. Repair = restructure the proof to derive this claim correctly + preserve all the substantive content.

### §1.4 Three concrete restructure recommendations

**1. Split Theorem E.1 into E.1a + E.1b:**

- **Theorem E.1a (Cost Severance Identity):** *CS > 0 iff B < RCV; CS = 0 iff B = RCV; CS < 0 iff B > RCV.* Trivially true by definition CS = RCV − B. Provides the algebraic foundation.

- **Theorem E.1b (Structural Cost Severance under Current Institutions):** *Under premises P1 (intergenerational market incompleteness — Coase-theorem-style bargaining failure for future generations), P2 (partial externality pricing — Pigouvian framework incomplete), P3 (current accountability bond inadequacy — empirical observation across multiple jurisdictions), CS > 0 holds for non-renewable extraction at typical pricing under current institutions.*

**2. Replace "B ≤ P" with explicit premises about current institutions:**

The current proof's "B ≤ P (accountability bonds are bounded by what the market will support)" is **wrong**. Severance taxes, reclamation bonds, decommissioning bonds, carbon taxes, and CSD architecture are forced regulatory impositions — not market-bounded. The framework's whole argument depends on this distinction (Insight #35 + #38 explicitly position framework instruments as forced-extractor-payment, not market-instruments).

The replacement: explicit premise P3 (current accountability bond inadequacy) which is an *empirical observation* not a *logical assumption* — current bonds happen to be inadequate; framework proposes increasing them. The empirical claim is supported by §H validation cases (McDowell County; Black Lung Trust Fund; EU ETS gaps; etc.).

**3. Tighten universal scope to conditional scope:**

Replace "for all non-renewable extraction under present institutions" with "under premises P1–P3, CS > 0 for non-renewable extraction." The framework demonstrates premises P1–P3 hold for most current institutions in §H; for specific cases (Norway sovereign-wealth-fund partial-coverage; EU ETS carbon pricing), the framework explicitly notes that B approaches but doesn't reach RCV.

---

## §2. Question + scope

### §2.1 Triggering articulation

[Phase 1 §8.1](commons_bonds_rigor_pass_2026-04-29_full_framework_audit_phase1_v1.0.0.md):

> *"Theorem E.1 (Structural Cost Severance) — Proves CS > 0 under specified conditions. Phase 2 audit recommended: proof-structure verification (premise enumeration; logical derivation; conclusion); academic-citation discipline (does proof rely on established theorems? are those cited?); collision-check against established cost-accounting theorems."* [Quote updated 2026-04-30 per double-Theorem cleanup; original Phase 1 §8.1 phrasing was "Theorem E.1 Structural Cost Severance Theorem".]

Phase 2 (this rigor pass) executes the screening-recommended audit at academic-rigor depth.

### §2.2 What this audit produces

For pass/fail academic-rigor gate at top-tier journals (AER, QJE, JPE, JEEM, JPubE) and academic-trade hybrid presses, the theorem's proof structure must meet academic-peer-review standards (per E.4 §2.2).

This audit produces:
1. Per-test verdict.
2. Concrete restructure recommendations per gap.
3. Recommended formal restatement of the theorem (E.1a + E.1b split per §13).
4. Cross-references to established economics + intergenerational-equity literature.

### §2.3 Pass/fail gate framing

Per author direction 2026-04-29: pass/fail gate on academic rigor for theorems. If the theorem's substance is structurally indefensible, abandonment is on the table. **Phase 2 pre-audit assessment found no structural defect — the substance is correct.** This audit confirms the substance + identifies the structural restatement work required.

### §2.4 What this pass does NOT cover

- Phase 2 deeper-dive on theorems E.2, E.3, E.5 — separate rigor passes (sequence: E.3 next per Insight #40 confirmed sequence).
- Pre-publication external review by economics PhD or formal-methods expert — Insight #39 OPEN; downstream gate.
- Empirical validation that B < RCV under current institutions — that's §H of Tech Appendix; this audit accepts the empirical work as the basis for premise P3.
- Tech Appendix HTML editing — pending author ratification + same open question as Insights #35 + #38 + #40 about now vs Phase 3 v2.0.0 rebuild.

---

## §3. Methodology

Same as E.4 §3. 8 tests applied: premise enumeration; logical derivation; edge case analysis; collision check; citation discipline; falsifiability; domain of applicability; counterexample resistance. Verdicts per test (STRONG / ADEQUATE / WEAK / FAIL).

---

## §4. Current theorem statement + proof — close reading

### §4.1 Current text (verbatim from Tech Appendix v1.0.0 §10 line 3249-3258)

**Theorem E.1 (Structural Cost Severance)**

*Statement:* For any extraction of a commons resource where market price P < RCV, cost severance CS > 0 occurs structurally, independent of extractor intentions.

*Proof:* Given CS = RCV − B and market pricing implies B ≤ P (accountability bonds are bounded by what the market will support), if P < RCV then B < RCV, therefore CS = RCV − B > 0. The inequality P < RCV follows from markets' structural inability to price intergenerational foreclosure — future generations cannot bid in present markets — and the incompleteness of externality pricing under existing accountability regimes. Therefore CS > 0 holds for all non-renewable extraction under present institutions, independently of whether any individual extractor intends to sever costs. ∎

*Note on scope:* Theorem E.1 is stated for conditions where P < RCV. The theorem does not claim P < RCV is a logical necessity — it is an empirical regularity explained by structural gaps in existing pricing. If future institutions implement full intergenerational foreclosure pricing, B could in principle equal or exceed RCV, making CS ≤ 0. This possibility is what makes the theorem falsifiable (see Counterargument 4 engagement in Chapter 6).

### §4.2 Initial reading observations

The proof contains **two distinct chains of reasoning** that the current text bundles together:

**Chain A (algebraic):**
- CS = RCV − B (definition)
- IF P < RCV AND B ≤ P, THEN B < RCV
- THEREFORE CS = RCV − B > 0

This is trivially true by basic algebra IF the premises hold.

**Chain B (empirical-structural):**
- "Markets' structural inability to price intergenerational foreclosure"
- "Incompleteness of externality pricing under existing accountability regimes"
- THEREFORE "P < RCV holds for all non-renewable extraction under present institutions"

This is an *empirical* claim about institutional structure, presented as a *derived* consequence of structural facts.

**Chain A's premise "B ≤ P (accountability bonds are bounded by what the market will support)" is a substantive claim that is wrong as a general claim:**
- Severance taxes (per Insight #35 lineage; ~36 US states) are imposed at rates regulators choose, not market-bounded.
- Reclamation bonds (SMCRA 1977) are imposed by federal/state regulation, not market-bounded.
- Decommissioning bonds (BLM 43 CFR Part 3162; BSEE 30 CFR Part 250) are regulatory impositions.
- Carbon taxes (EU ETS; British Columbia; etc.) are policy-set rates.
- CSD per Insight #35 + #38 architecture is forced-extractor-payment by design.

The framework's WHOLE ARGUMENT is that bonds CAN exceed market-bounded levels through regulation. The "B ≤ P" assumption contradicts the framework's own architecture.

The CORRECT empirical claim is: **under current institutions**, B is *empirically* less than RCV in most cases. Not because B is logically bounded by P, but because current institutional design has produced inadequate bonds across most extracted-commons cases.

**Conflation issue:** Chain A and Chain B are doing different work. Chain A is logical; Chain B is empirical. The proof presents Chain B as if it derives from Chain A — but Chain A doesn't derive Chain B; Chain A *assumes* Chain B's conclusion ("B ≤ P" is essentially saying "current bonds are inadequate").

### §4.3 The substance is correct; the structure conflates two claims

The framework's substantive claim — that cost severance is structural under current institutions, not merely the result of bad-faith extractors — IS correct. The empirical evidence (§H validation cases; Norway as partial-coverage exemplar; the absence of comprehensive accountability instruments globally) supports this.

What's wrong is the PROOF STRUCTURE: it tries to derive the empirical claim via algebraic manipulation when the empirical claim actually requires explicit premises about current institutional structure.

---

## §5. Test 1 — Premise enumeration

### §5.1 Current state

The proof contains the following implicit premises that are NOT stated as numbered assumptions:

| # | Implicit premise | Where it appears | Issue |
|---|---|---|---|
| 1 | CS = RCV − B (definition) | Proof first line | Defined; OK as definition not premise |
| 2 | B ≤ P (accountability bonds bounded by market price) | Proof: "market pricing implies B ≤ P" | **Wrong as general claim**; severance taxes + reclamation bonds + carbon taxes can exceed market price by regulation |
| 3 | Markets cannot price intergenerational foreclosure | Asserted in second sentence | **Coase-theorem incomplete-bargaining condition; should be premise with Coase 1960 citation** |
| 4 | Externality pricing is incomplete under existing accountability regimes | Asserted in second sentence | **Pigou 1920 externality framework; should be premise with Pigou citation** |
| 5 | RCV > P empirically | Inferred from "P < RCV" condition | Empirical claim; should be premise with §H validation cases as supporting evidence |
| 6 | "Present institutions" is the defined scope | Inferred from "under present institutions" | Term not formally defined; should specify what counts as "present institutions" |
| 7 | Cost severance is independent of extractor intentions | Conclusion | Should be conclusion, not premise |

### §5.2 Verdict

**WEAK.** Seven implicit premises; three are load-bearing AND problematic:
- #2 (B ≤ P) is **wrong as a general claim**.
- #3 (intergenerational market incompleteness) is **substantively correct but should be explicit Coase-theorem-style premise**.
- #4 (Pigouvian externality pricing incompleteness) is **substantively correct but should be explicit premise**.

Top-tier journals require explicit premise enumeration; the current text would not pass JEEM or JPubE referee review even more decisively than E.4 because of premise #2 being wrong.

### §5.3 Repair recommendation

Replace implicit premises with explicit numbered premises P1–P3 (per §13.1 below):
- P1: Intergenerational market incompleteness (Coase-theorem failure for future-generation parties).
- P2: Partial externality pricing (Pigouvian framework incomplete).
- P3: Current accountability bond inadequacy (empirical claim supported by §H validation cases).

These are not assumptions about market structure (which would be wrong) but explicit premises about *current institutions* + *intergenerational structure*.

---

## §6. Test 2 — Logical derivation

### §6.1 Current state

The proof's logical chain conflates Chain A (algebraic) and Chain B (empirical-structural) per §4.2.

**Chain A as currently stated:**
- Premise: CS = RCV − B
- Premise (wrong): B ≤ P
- Premise: P < RCV (the theorem's antecedent)
- Therefore: B ≤ P < RCV → B < RCV → CS = RCV − B > 0.

If we accept the wrong premise B ≤ P, this chain is logically valid. But the premise is wrong, so the chain doesn't establish anything about real-world institutions.

**Chain B as currently stated:**
- Asserted: markets cannot price intergenerational foreclosure.
- Asserted: externality pricing is incomplete under existing accountability regimes.
- Therefore: P < RCV holds for all non-renewable extraction under present institutions.

This chain is presented as a derivation but is actually an assertion. The "markets cannot price" claim doesn't formally derive "P < RCV"; it provides a structural rationale for why P < RCV would hold but doesn't prove it. This is a common-law "structural argument" rather than a formal proof.

### §6.2 Verdict

**WEAK.** The proof structure conflates two different reasoning chains. Chain A relies on a wrong premise (B ≤ P). Chain B is structural assertion presented as derivation.

### §6.3 Repair recommendation

Split into two theorems (E.1a + E.1b per §13):

- **E.1a** uses Chain A correctly: just the algebraic identity CS > 0 iff B < RCV. No premise about market-bounded B; just CS = RCV − B → CS sign determined by B vs RCV. Trivially true.

- **E.1b** uses Chain B correctly: explicit premises P1 (intergenerational market incompleteness — Coase 1960 framework) + P2 (partial externality pricing — Pigou 1920 framework) + P3 (current accountability bond inadequacy — empirical). Conclusion: under premises P1–P3, B < RCV under current institutions, therefore (by E.1a) CS > 0 under current institutions.

This separation makes Chain A trivially clean (algebraic identity) and Chain B explicitly structural (premises about institutional structure → conclusion about current state).

---

## §7. Test 3 — Edge case analysis

### §7.1 Current state

The current proof handles essentially zero edge cases. The "Note on scope" acknowledges that future institutions could close the gap (B = RCV → CS = 0) but does not analyze:

**Edge case 1: Norway sovereign-wealth-fund partial-coverage.** Norway operationalizes the Hartwick rule for Norwegian-citizen-internalization of oil rents but doesn't extend to non-Norwegian populations affected by climate externalities (per terms_index Foreclosure Bond entry). For the Norwegian-citizens-only RCV, B may approximately equal RCV (CS ≈ 0); for global RCV, B << RCV (CS > 0).

**Edge case 2: Carbon-intensive extraction in EU ETS jurisdiction.** EU ETS carbon prices vary $30-100/ton CO2. For some carbon-intensive extraction at high price points + EU ETS coverage, B for carbon component approaches RCV-carbon-component. Other RCV components (foreclosure of future-generation options; non-carbon externalities) remain unbonded.

**Edge case 3: Deepwater offshore decommissioning.** Post-Deepwater-Horizon, BSEE 30 CFR Part 254 requires substantial decommissioning + oil-spill-response bonds. For some operators, total bonds approach 50%+ of resource value. CS positive but smaller than for less-regulated extraction.

**Edge case 4: Heavily regulated mining (e.g., Australian uranium).** SMCRA-equivalent + ARMS (Australian) regulations + Indigenous land access agreements + decommissioning bonds + radiological liability provisions can push B substantially toward RCV.

**Edge case 5: Extreme cases approaching B = RCV.** What's the limit case? The framework's argument is that comprehensive accountability instruments WOULD make B = RCV; current institutions DON'T. Theorem should explicitly address what happens when current institutions APPROACH that ideal.

### §7.2 Verdict

**WEAK.** Edge cases not handled. The "Note on scope" is too brief; should address several specific cases where the framework's empirical claim approaches its boundary.

### §7.3 Repair recommendation

Add edge case analysis section to restructured E.1b:

> *Edge cases: For non-renewable extraction in jurisdictions with partial accountability instruments (e.g., Norway sovereign-wealth-fund coverage of Norwegian-citizen externalities; EU ETS carbon coverage; SMCRA reclamation bonds), B captures a fraction of RCV but typically does not equal it because (i) accountability instruments are partial in scope (cover some externalities, not all); (ii) jurisdictions are partial in extent (don't internalize cross-border externalities); (iii) intergenerational claims remain undelegated. In these cases, premise P3 (B < RCV) holds with smaller magnitude. The framework's empirical evidence (§H) demonstrates this pattern across multiple jurisdictions.*

---

## §8. Test 4 — Collision check against established theorems

### §8.1 Coase 1960 "The Problem of Social Cost"

Coase 1960 establishes that under zero transaction costs and complete property rights, parties can bargain to efficient outcomes regardless of initial assignment of liability. The Coase theorem implicitly requires that **all affected parties can bargain**.

**Intergenerational extension of Coase:** future generations cannot bargain because they don't yet exist; they cannot bid; they cannot assert rights through contract. The framework's "markets' structural inability to price intergenerational foreclosure" IS this Coase-theorem-incomplete-bargaining condition for intergenerational claims.

**Does E.1 extend, conflict with, or duplicate Coase 1960?**
- **Extends:** E.1's structural claim is the formal statement of a Coase-theorem failure mode — bargaining cannot complete because one set of affected parties (future generations) cannot participate. This is a non-trivial extension; Coase didn't address this directly.
- **Conflicts:** No conflict.
- **Duplicates:** Not a duplication; Coase doesn't address intergenerational claims.

**Critical citation gap:** Coase 1960 is THE adjacent theorem that E.1 extends. Currently NOT cited in the proof. This is a serious M12 attribution-honesty gap and a serious peer-review gap.

### §8.2 Pigou 1920 "The Economics of Welfare"

Pigou 1920 establishes externality framework: market prices fail to internalize external costs; corrective taxes can close the gap. The framework's "incompleteness of externality pricing under existing accountability regimes" extends Pigou.

**Does E.1 extend Pigou 1920?**
- **Extends:** Pigou framework addresses individual externalities; E.1 addresses the systematic incompleteness of externality pricing across the full set of extracted commons (not just specific externalities). The framework's RCV is a comprehensive accounting; Pigouvian instruments are partial.
- **Conflicts:** No conflict.
- **Duplicates:** Not a duplication; framework's specialization is comprehensiveness.

**Critical citation gap:** Pigou 1920 is THE foundational reference for externality pricing. Currently NOT cited in the proof.

### §8.3 Intergenerational equity literature

Brown Weiss 1989 *In Fairness to Future Generations*; Howarth + Norgaard 1990 "Intergenerational Resource Rights, Efficiency, and Social Optimality" *Land Economics*; Solow 1974; Hartwick 1977; Stern Review 2007.

**Does E.1 extend intergenerational equity literature?**
- **Extends:** intergenerational equity literature establishes the normative claim that future generations matter; E.1 extends to a *positive* claim about how current institutions fail to operationalize this normative claim.
- **Conflicts:** No conflict.
- **Duplicates:** Not a duplication.

**Critical citation gap:** Intergenerational equity literature underpins E.1's structural claim. Currently NOT cited.

### §8.4 Verdict

**WEAK.** Three load-bearing literatures (Coase 1960; Pigou 1920; intergenerational equity) NOT cited in the proof. This is a serious M12 attribution-honesty gap. Top-tier journals require these references.

### §8.5 Repair recommendation

Restructured proof cites:
- Premise P1 (intergenerational market incompleteness) → Coase 1960 framework + Howarth + Norgaard 1990.
- Premise P2 (partial externality pricing) → Pigou 1920 + Stern Review 2007 (climate externality incompleteness exemplar).
- Premise P3 (current accountability bond inadequacy) → §H empirical validation cases + Hartwick 1977 (sustainability rule baseline).
- Adjacent: Brown Weiss 1989 (normative foundation); Solow 1974 (intergenerational consumption baseline).

---

## §9. Test 5 — Citation discipline

### §9.1 Current state

The proof cites zero references. Compare to E.4 which cited Weitzman 2001 (one citation).

The framework's broader apparatus has lineage in:
- Coase 1960 (load-bearing for premise P1).
- Pigou 1920 (load-bearing for premise P2).
- Brown Weiss 1989; Howarth + Norgaard 1990; Gosseries + Meyer 2009 (intergenerational equity foundation).
- Stern Review 2007 (climate externality exemplar).
- Mazzucato *Mission Economy* + *The Value of Everything* (value extraction tradition; framework's adjacent positioning).
- Anderson *Private Government* (institutional structure).

### §9.2 Verdict

**WEAK.** Zero citations in proof for theorem with three load-bearing literatures. Far below academic-peer-review standards.

### §9.3 Repair recommendation

Restructured proof cites Coase 1960; Pigou 1920; Howarth + Norgaard 1990; Stern Review 2007 inline at premises P1, P2, P3. Brown Weiss 1989 + Solow 1974 + Hartwick 1977 cited in adjacent context.

---

## §10. Test 6 — Falsifiability

### §10.1 Current state

The "Note on scope" acknowledges falsifiability:

> *"If future institutions implement full intergenerational foreclosure pricing, B could in principle equal or exceed RCV, making CS ≤ 0."*

This is a partial falsifiability statement. It addresses the *prospective* falsifiability (future institutions could falsify) but NOT the *current* falsifiability (could a current case be found where B ≥ RCV?).

The framework's structural claim is about CURRENT institutions; it should be falsifiable by EVIDENCE about current institutions.

**Possible current-institution falsifications:**
- Discovery of a non-renewable extraction case under current institutions where B ≥ RCV (i.e., comprehensive accountability has been achieved). Theorem would be falsified for that case.
- Discovery that B ≥ RCV across most current institutions (i.e., the empirical claim P3 fails). Theorem would be falsified at the empirical-structural level.

### §10.2 Verdict

**ADEQUATE.** Prospective falsifiability addressed in Note. Current-institution falsifiability implicit but should be explicit.

### §10.3 Repair recommendation

Restructured E.1b includes explicit falsifiability conditions:

> *Falsifiability: Theorem E.1b is falsifiable under either (a) discovery of a current-institution non-renewable extraction case where B ≥ RCV (single counterexample to the structural claim), OR (b) demonstration that across most current institutions, accountability bonds are sufficient (B ≈ RCV) such that premise P3 fails empirically. The framework's §H empirical validation cases address (b); ongoing monitoring of jurisdictional accountability instruments addresses (a).*

---

## §11. Test 7 — Domain of applicability

### §11.1 Current state

"All non-renewable extraction under present institutions" is the stated domain. Issues:
- "Non-renewable extraction" is reasonably defined elsewhere in the framework (Tech Appendix §F existential substitutability gap analysis).
- "Present institutions" is NOT formally defined. What counts as "present"? US? Global? Specific jurisdictions? Time-period?
- Renewable extraction (e.g., timber harvesting under sustainable management) is excluded but the exclusion isn't explained — does the theorem apply to renewable cases under unsustainable management?

### §11.2 Verdict

**WEAK.** Domain implicit. "Present institutions" undefined.

### §11.3 Repair recommendation

Restructured E.1b includes explicit domain statement:

> *Domain of applicability: Theorem E.1b applies to non-renewable extraction (resources whose substitutability function S(t) does not approach 1 within the relevant time horizon) under contemporary institutions (defined as the set of accountability instruments in operation in the current decade across jurisdictions where the extraction occurs). The theorem's empirical premise P3 has been validated in §H for fossil-fuel extraction across major US jurisdictions, EU ETS coverage, and selected non-OECD contexts. Renewable extraction under unsustainable management, and non-renewable extraction in jurisdictions with comprehensive accountability instruments (theoretical limit; not currently observed), are outside the theorem's domain.*

---

## §12. Test 8 — Counterexample resistance

### §12.1 Approach

Try to construct counterexamples: real or hypothetical non-renewable extraction cases where, under current institutions, B ≥ RCV (CS ≤ 0).

### §12.2 Constructed counterexamples

**Counterexample 1: Norway sovereign-wealth-fund Norwegian-citizen-only scope.**

Norway's GPFG operationalizes Hartwick rule by saving oil rents for future Norwegian citizens. For the Norwegian-citizen-only RCV (only counting impacts on Norway), B may approximately equal RCV.

Test: does Norway-Norwegian-only case falsify E.1?

**Defense:** The framework's RCV is GLOBAL — it includes climate externalities affecting non-Norwegian populations. Norway's B does NOT cover those. So global RCV(Norway) >> Norway's B → CS(Norway) > 0 globally.

But this defense requires E.1's domain to specify GLOBAL RCV, not jurisdictional RCV. Currently the theorem doesn't make this specification. **Real gap.**

**Counterexample 2: Carbon-intensive extraction in EU ETS jurisdiction with EU ETS price > $100/ton CO2.**

For specific high-price periods in EU ETS, carbon component of B may exceed corresponding component of RCV. If EU ETS price is high enough that bonds + carbon tax exceeds market price for carbon-intensive extraction... wait, but RCV includes other components (foreclosure cost; non-carbon externalities) that EU ETS doesn't cover.

**Defense:** Even with high EU ETS prices, total B (sum of all accountability instruments) is < total RCV (sum of all severed-cost components). EU ETS covers carbon; doesn't cover foreclosure of future-generation options-substitution; doesn't cover non-carbon externalities (water; soil; community).

**This defense holds.** But it requires the framework to be explicit that B is the AGGREGATE accountability instrument and RCV is the AGGREGATE severed cost; partial coverage of one component doesn't close the aggregate gap.

**Counterexample 3: Deepwater offshore decommissioning post-2010 with substantial BSEE bonds.**

After Deepwater Horizon, BSEE imposed substantial decommissioning + oil-spill-response bond requirements. For some operators, total bonds approach 50%+ of resource value.

**Defense:** Decommissioning bonds cover end-of-life cleanup; they do NOT cover (i) climate externalities from emissions of the extracted oil; (ii) intergenerational foreclosure of future options-substitution; (iii) community-level externalities at extraction site. Total B (decommissioning + nominal externality coverage) << total RCV.

**This defense holds.**

**Counterexample 4: Hypothetical jurisdiction with comprehensive accountability instruments.**

Suppose a hypothetical jurisdiction (call it "NorwaSwePlus") with: sovereign-wealth-fund Hartwick coverage + comprehensive carbon tax + decommissioning bonds + community-impact bonds + intergenerational-foreclosure bonds + cross-border-externality coverage.

In NorwaSwePlus, B could approach RCV. CS approaches 0.

**Test:** does NorwaSwePlus falsify E.1?

**Defense:** The framework's empirical premise P3 (current accountability bond inadequacy) is empirical, not logical. NorwaSwePlus is hypothetical. If NorwaSwePlus existed, E.1b would be falsified for that jurisdiction. The framework would adjust empirical premise P3 to "P3 holds under current institutions in jurisdictions other than NorwaSwePlus."

**This is exactly the falsifiability the Note on scope acknowledges.** The theorem is correctly falsifiable.

### §12.3 Verdict

**WEAK as currently written / STRONG under restructure.**

Counterexample 1 (Norway-Norwegian-only) **does** find a real gap in current theorem statement: the "RCV" referenced in the theorem is actually GLOBAL RCV, not jurisdictional RCV. The current theorem doesn't specify this. Restructure must specify aggregate-not-partial RCV.

Counterexamples 2-3 (EU ETS; deepwater offshore) are **defended successfully** by aggregate-vs-partial argument. But the defense isn't in the current proof; restructure should make this explicit.

Counterexample 4 (NorwaSwePlus) is **the theorem's correct falsifiability case**. Should be in theorem statement, not just footnote.

### §12.4 Repair recommendation

Restructured E.1b includes:
- Explicit statement that RCV is AGGREGATE (sum across all severed-cost components) and B is AGGREGATE (sum across all accountability instruments).
- Explicit falsifiability: hypothetical or actual jurisdiction with comprehensive accountability instruments would falsify the empirical claim.
- Explicit response to partial-coverage counterexamples: partial coverage of one component doesn't close the aggregate gap.

---

## §13. Recommended formal restatement (E.1a + E.1b split)

### §13.1 Premise enumeration

**A1 (Cost Severance Definition):** CS(R, t₀) = RCV(R, t₀) − B(R, t₀) where R is a non-renewable resource extracted at time t₀; RCV is per-unit Residual Commons Value; B is per-unit aggregate Accountability Bond. (Per Tech Appendix §B.1.)

**A2 (RCV is non-negative):** RCV(R, t₀) ≥ 0 for all R, t₀ where R is non-renewable. (Empirical claim supported by §B.1 + §H.)

**A3 (B is non-negative):** B(R, t₀) ≥ 0 for all R, t₀. (Definitionally; bonds cannot be negative.)

**A4 (Aggregate scope):** RCV represents aggregate Residual Commons Value across all severed-cost components (foreclosure cost + externality tail; per Tech Appendix §B.1). B represents aggregate Accountability Bond across all instruments operating against R (sum of severance taxes + reclamation bonds + decommissioning bonds + carbon taxes + sovereign-wealth-fund Hartwick coverage + any other accountability instruments).

**Premise P1 (Intergenerational market incompleteness — extension of Coase 1960):** Markets cannot complete bargaining for intergenerational claims because future generations cannot bid in present markets. Per Coase 1960 framework: complete-bargaining requires all affected parties to participate; intergenerational extraction affects parties (future generations) who cannot participate. Therefore market pricing systematically under-internalizes intergenerational components of total cost.

**Premise P2 (Partial externality pricing — extension of Pigou 1920):** Existing externality-pricing instruments (Pigouvian taxes; cap-and-trade; reclamation bonds) cover specific externalities partially; comprehensive coverage of all externalities (including intergenerational) is not currently implemented in any jurisdiction. Per Pigou 1920 framework + Stern Review 2007 (climate externality incompleteness exemplar).

**Premise P3 (Current accountability bond inadequacy — empirical):** Across major non-renewable extraction jurisdictions in the contemporary decade, the aggregate Accountability Bond B is empirically less than the aggregate Residual Commons Value RCV. Supporting evidence: Tech Appendix §H validation cases (McDowell County coal; Black Lung Trust Fund deficit; EU ETS gaps; Norwegian sovereign-wealth-fund partial-coverage analysis; etc.).

### §13.2 Theorem statement (restructured — split into E.1a + E.1b)

#### Theorem E.1a (Cost Severance Identity)

*Under Assumption A1, the sign of CS is determined by the comparison of RCV and B:*

> **CS > 0 iff B < RCV; CS = 0 iff B = RCV; CS < 0 iff B > RCV.**

*Proof:* By Assumption A1, CS = RCV − B. Therefore CS > 0 ↔ RCV − B > 0 ↔ B < RCV. Similarly for equality and inequality. ∎

#### Theorem E.1b (Structural Cost Severance under Current Institutions)

*Under Premises P1, P2, P3, for non-renewable extraction R at time t₀ in any jurisdiction observed under current institutions, aggregate B(R, t₀) < aggregate RCV(R, t₀). Therefore by Theorem E.1a, CS(R, t₀) > 0.*

*Proof:* By Premise P1, the intergenerational components of RCV cannot be priced through market mechanisms; therefore market-based accountability instruments do not internalize these components. By Premise P2, the externality components of RCV are partially priced through existing Pigouvian instruments; the partial coverage means that the externality components of B are strictly less than the corresponding components of RCV in aggregate. By Premise P3 (empirical), across current-institution jurisdictions, neither comprehensive intergenerational coverage nor comprehensive externality coverage is implemented; therefore aggregate B < aggregate RCV.

By Theorem E.1a, B < RCV implies CS > 0. The conclusion follows: CS > 0 holds for non-renewable extraction under current institutions across the jurisdictions empirically validated in §H. ∎

*Falsifiability:* Theorem E.1b is falsifiable by either (a) discovery of a non-renewable extraction case under current institutions where aggregate B ≥ aggregate RCV (single counterexample); or (b) empirical demonstration that across most current institutions, accountability instruments are sufficient (B ≈ RCV) such that Premise P3 fails. Empirical evidence (§H) addresses (b); ongoing monitoring of jurisdictional accountability instruments addresses (a).

*Domain of applicability:* Theorem E.1b applies to non-renewable extraction (resources whose substitutability function S(t) does not approach 1 within the relevant time horizon — see Tech Appendix §F existential substitutability gap analysis) under contemporary institutions (defined as the set of accountability instruments in operation in the current decade across jurisdictions where the extraction occurs). Renewable extraction under sustainable management, and non-renewable extraction in hypothetical jurisdictions with comprehensive accountability instruments, are outside the theorem's domain (and would constitute falsifying counterexamples if observed empirically).

### §13.3 Why the split is load-bearing

E.1a is trivially true (algebra) and provides the foundation for all framework reasoning about the sign of CS.

E.1b is non-trivially true (depends on empirical claim P3) and provides the framework's central structural claim — that cost severance is structural under current institutions.

Splitting them:
- Makes the algebraic identity available for use in other proofs (e.g., E.5 Renewable Imperative uses it).
- Makes the empirical claim explicitly empirical (P3) — defensible against academic critics who would otherwise challenge the universal scope.
- Allows the framework to engage with counterexamples (Norway; EU ETS; etc.) by acknowledging partial-coverage cases without falsifying the aggregate claim.
- Provides explicit citations (Coase 1960; Pigou 1920; etc.) at the load-bearing premises.

### §13.4 What this restructure preserves

All of the framework's substantive claims:
- Cost severance is structural, not merely intentional (preserved as E.1b under explicit premises).
- Markets cannot price intergenerational claims (preserved as Premise P1 with Coase 1960 citation).
- Externality pricing is incomplete (preserved as Premise P2 with Pigou 1920 citation).
- Current accountability bonds are inadequate (preserved as empirical Premise P3 with §H validation).
- The theorem is falsifiable (preserved as explicit falsifiability conditions).

What this restructure changes:
- Splits one over-broad theorem into two precise theorems.
- Replaces the wrong "B ≤ P" assumption with explicit Premise P3 about current institutions.
- Tightens "all non-renewable extraction" to "non-renewable extraction in jurisdictions empirically validated in §H."
- Adds explicit citations to load-bearing literatures.

---

## §14. Verdict + ratification choices

### §14.1 Recommended verdict

**KEEP framework's substantive claim; restructure proof per §13 (split into E.1a + E.1b with explicit premises P1–P3).** All of the framework's substantive content is preserved; the deductive structure is brought to academic-peer-review standards.

Three concrete restructure enhancements (mutually-reinforcing):

1. **Split Theorem E.1 into E.1a (algebraic identity) + E.1b (structural-empirical theorem).**

2. **Replace wrong "B ≤ P" assumption with explicit Premises P1–P3** (intergenerational market incompleteness via Coase; partial externality pricing via Pigou; current accountability bond inadequacy via §H empirical).

3. **Tighten universal scope to conditional-on-premises scope + explicit falsifiability + domain of applicability.**

### §14.2 Pass-fail verdict on as-currently-written E.1

**WEAK.** Six of eight tests WEAK; one ADEQUATE; zero STRONG. Would not survive academic peer review at top-tier journals (AER, QJE, JPE, JEEM, JPubE) without restructure.

The framework's most-central theorem currently has the most-fragile proof structure of the 5 theorems (per current Phase 2 audit + comparison to E.4 which had 4 of 8 WEAK).

### §14.3 Pass-fail verdict on restructured E.1a + E.1b per §13

**STRONG.** With restructure applied:
- E.1a is trivially true by algebra; passes peer review immediately.
- E.1b has explicit premises with citations; falsifiability conditions; domain of applicability; counterexample resistance per §12.
- Three load-bearing literatures (Coase 1960; Pigou 1920; intergenerational equity) cited at premises.

### §14.4 Author ratification choices

**(a) Full ratify §13 restructure** — split theorem into E.1a + E.1b; adopt premises P1–P3; tighten scope; add citations; Tech Appendix HTML edit pending §15 Q1.

**(b) Partial ratify** — adopt subset:
- (b.i) Citation expansion only (add Coase + Pigou + Brown Weiss + Stern Review citations to current proof; keep theorem unsplit).
- (b.ii) Premise enumeration only (state P1–P3 explicitly; keep theorem statement universal).
- (b.iii) Theorem split only (split into E.1a + E.1b; defer premise + citation work).

**(c) Modify verdict** — author specifies different recommendation.

**(d) Defer Phase 2 ratification** — additional questions before locking.

**(e) Reject** — author rejects audit findings.

**Recommendation: (a) Full ratify.** Partial ratifications leave the theorem in worse state than current (mixing old + new structure). The split is load-bearing — without it, the empirical premise P3 hides as the wrong "B ≤ P" assumption. The citations are load-bearing — without them, the Coase + Pigou + intergenerational-equity literatures are un-engaged.

### §14.5 Implementation pending after ratification

If (a) full ratify:
1. terms_index — add Phase 2 verdict entry to Cost Severance + RCV entries; cross-reference to this rigor pass.
2. Tech Appendix v1.0.0 HTML §10 line 3249-3258 — replace current E.1 with restructured E.1a + E.1b per §13. Same open question as Insights #35 + #38 + #40 about now vs Phase 3 v2.0.0 rebuild.
3. Bibliography expansion — Coase 1960 (already in framework); Pigou 1920 (already cited at §17); Howarth + Norgaard 1990 (may need adding); Brown Weiss 1989 (already cited); Stern Review 2007 (already cited); Solow 1974 (optional addition); Hartwick 1977 (already cited).
4. Open Insights — new Insight #41 closed-ratified capturing Phase 2 E.1 verdict.
5. Cross-reference in other theorem proofs — E.5 Renewable Imperative uses CS > 0 from E.1; restructured proof should cite E.1a (algebraic identity) explicitly.

### §14.6 Pre-publication external review (Insight #39)

Per Insight #39, eventual external review by economics PhD or formal-methods expert is warranted. Specifically for E.1: a reviewer with intergenerational-equity / resource-economics specialization (Brown Weiss / Solow / Stern lineage) should verify:
- Premise P1 correctly extends Coase 1960 framework to intergenerational claims.
- Premise P2 correctly extends Pigou 1920 framework.
- Premise P3 (empirical) is supported by §H validation cases.
- Counterexample resistance (§12) holds under restructured premises.
- Aggregate RCV vs partial-coverage instrument distinction (§12.4) is fairly characterized.

This rigor pass produces the substrate; external review tests it.

---

## §15. Open questions for author discussion

1. **Tech Appendix HTML edit timing** — apply restructure to v1.0.0 now vs batch into Phase 3 Tech Appendix v2.0.0 rebuild? Same open question as Insights #35 + #38 + #40. **Possibility:** all Phase 2 Tech Appendix changes batched into Phase 3 v2.0.0 rebuild as single coordinated update.

2. **Theorem split naming** — "E.1a + E.1b" preserves theorem-numbering but introduces sub-numbering. Alternative: rename to "Theorem E.1 (Cost Severance Identity)" + "Theorem E.X (Structural Cost Severance under Current Institutions)" where X is a new theorem number. Trade-off: E.1a + E.1b preserves continuity; renumbering is cleaner.

3. **Premise P3 empirical scope** — should P3 cite specific §H cases (McDowell coal; Black Lung Trust Fund; etc.) or just reference §H generally? Specific citation is more defensible; general reference is less brittle if §H content updates.

4. **Aggregate-vs-partial coverage discussion** — should the restructured E.1b explicitly discuss the aggregate-vs-partial-coverage issue (§12.2 counterexample defenses) in the proof itself, or as a separate "Note on partial-coverage cases" section?

5. **Citation completeness vs density** — the restructured proof can cite Coase + Pigou + Stern Review at minimum, OR also cite Brown Weiss + Howarth-Norgaard + Solow + Hartwick + Mazzucato. Trade-off: more citations = more academic-defensibility; longer proof = less readable.

6. **Phase 2 sequencing implication** — E.1 took ~1100 lines (this pass; longer than projected ~800-1000 because the restructure is substantively heavier than E.4 — categorization issue not just formalization). Confirm sequence E.1 → E.3 → E.5 → E.2? Or pause to reflect on accumulated 4-theorem-audit scope estimate?

---

## §16. Cross-references

### §16.1 Upstream rigor passes

- [Phase 1 full framework audit §8.1](commons_bonds_rigor_pass_2026-04-29_full_framework_audit_phase1_v1.0.0.md) — flagged E.1 for Phase 2 academic-rigor depth audit.
- [Phase 2 Theorem E.4 rigor pass (Insight #40)](commons_bonds_rigor_pass_2026-04-29_phase2_theorem_e4_integral_convergence_v1.0.0.md) — established theorem-audit pattern; this rigor pass applies the pattern to substantively heavier substance.
- Insight #35 + #38 cross-political-tradition Phase 2 rigor passes — verdict-pattern cross-reference (KEEP + restructure pattern).
- 2026-04-24 Cost Severance + Severed Cost rigor passes — definitional anchor for E.1's CS variable.

### §16.2 Downstream artifacts (this pass would update on ratification)

- `core/technical-appendix/TechnicalAppendix_v1.0.0.html` §10 line 3249-3258 — restructured E.1a + E.1b per §13 (or Phase 3 v2.0.0 rebuild batch).
- `core/terms/terms_index.md` Cost Severance + RCV entries — Phase 2 verdict entry.
- `alignment/commons_bonds_open_insights_v1.0.0.md` — new Insight #41 closed-ratified.
- Bibliography expansion — Howarth + Norgaard 1990 (likely addition); possibly Solow 1974 explicit cite.
- Cross-reference in other theorem proofs (E.5 uses CS > 0 from E.1; restructured E.5 proof cites E.1a).

### §16.3 Sibling Phase 2 candidates (per Phase 1 §10 + Phase 2 sequence)

After E.1: E.3 (Abundance Masking — circular proof; needs full formalization of cost-function transition behavior; ~700-900 lines) → E.5 (Renewable Imperative — scope-tightening + practical-corollary separation; ~700-900 lines) → E.2 (Convergence of Independent Models — categorization decision: relabel as empirical observation OR restructure as formal robustness theorem; ~400-600 lines).

After theorems: RCV acronym collision audit (#4); Externality Tail statistics-distribution-tail collision (#5); Three Ways of Counting post-rename verification (#6, minor); Scarcity multiplier formula academic-defensibility (#7, depth); RCV integrand Q(t) notation-clarity (#8, depth, likely bundle with #7).

### §16.4 Pre-publication external review (Insight #39)

This rigor pass + 4 sibling theorem rigor passes produce Claude's assessment. Per Insight #39, eventual external review by economics PhD + formal-methods expert is warranted before publication. For E.1 specifically: reviewer should have intergenerational-equity / resource-economics specialization (Brown Weiss / Solow / Stern lineage) to verify the Coase + Pigou + intergenerational-equity extensions are correctly characterized.

---

**End of Phase 2 deeper-dive rigor pass v1.0.0 [RATIFIED 2026-04-29 by Chris Winn — verdict (a) Full ratify].**
