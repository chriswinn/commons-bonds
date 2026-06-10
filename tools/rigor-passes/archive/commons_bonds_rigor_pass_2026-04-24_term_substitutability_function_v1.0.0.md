# Commons Bonds — Full Rigor Pass: Substitutability Function (S)

**Version:** 1.0.0
**Date:** 2026-04-24
**Protocol applied:** `tools/commons_bonds_rigor_protocol_v2.2.0.md` — full 11-module suite + §22 Path Comparison Mode + §22.4 usefulness-vs-goals alignment + Principle-#2 concept audit + Principle-#3 primitive-distinctness check.
**Scope:** Ring-2 individual rigor pass on Substitutability Function — meta-pass §10.2 classifies as "framework's most novel single component." This pass confirms/revises Ring placement and tests load-bearing status.
**Status:** rigor pass executed 2026-04-24; pending author ratification.
**Author:** Chris Winn

---

## §1. Executive summary

**RECOMMENDED: Option A — CONFIRM Ring 2 (internal load-bearing). Hold at Ring 2, not Ring 1.** The Substitutability Function S(t|t₀) is load-bearing for framework CORE math (appears in C₁ foreclosure-cost formula), actively used across 98 references in 25 files, distinct from other framework primitives, and the framework's most novel single mathematical component. However, it operates framework-internally — readers encounter it to understand the model; non-reader policymakers don't adopt "Substitutability Function" as travel-ready vocabulary. Ring 2 (internal load-bearing) is the correct placement.

**Principle-#2 concept audit:** 98 refs across Ch 6 Draft + Ch 6 GuidanceDoc + Ch 7 GuidanceDoc + Tech Appendix + multiple audit/decision docs. Active operational use; not phrase-only. S is used both (a) as a probability function S(t|t₀) in formula and (b) as a conceptual handle ("the substitutability function shows that...") in prose. Both usages are load-bearing.

**Principle-#3 distinctness check (vs other framework primitives):**

| Primitive | Role | Distinct from S? |
|---|---|---|
| RCV | Outcome — integrates over all Cᵢ | YES — RCV is an integral; S is a function-input |
| Cᵢ | Cost category (C₁…Cₙ) | YES — Cᵢ is a category; S is a mathematical object inside Cᵢ (specifically C₁) |
| AIT | Methodology for admitting candidate costs | YES — AIT tests individual costs; S describes a dynamic (probability-over-time) |
| B (Accountability Bond) | Dollar amount priced | YES — B is a scalar; S is a function |
| CS = RCV − B | Equation | YES — equation, not primitive |
| Abundances (the 10) | Organizational scaffolding | YES — categorical; S is functional |
| Externality Tail (E) | Second canonical cost term | YES — E is its own function E(R, t); sibling not synonym |

S is structurally distinct. No reduction to another primitive. **Principle #3 PASSES.**

**Key analytical distinction (S vs. S_max):**

S(t|t₀) is the **function** (probability over time). S_max is a **scalar derived from S** (supremum over some evaluation range). The CSG retirement pass (commit `3ec3707`) retires CSG as a derived-scalar-from-S while retaining S itself as primitive. This pass confirms that structural asymmetry: S earns Ring 2; derived scalars from S do not.

**Options tested:**

- **A — CONFIRM Ring 2** (meta-pass default). **RECOMMENDED.**
- **B — PROMOTE to Ring 1** (public adoption target). REJECTED — S is mathematical-internal; policymakers / lawyers don't adopt function-names.
- **C — DEMOTE to prose** (remove from glossary; describe in Ch 6 + Tech Appendix only). REJECTED — breaks glossary coverage of the C₁ formula.
- **D — RENAME** (candidates: "Substitutability Probability Function," "Substitutability S(t)"). REJECTED — current name is precise.
- **E — SPLIT into S(t|t₀) and S_max** (treat as two named objects). REJECTED — S_max is a derivation; naming it separately adds footprint without load-bearing gain.

---

## §2. The question under test

### §2.1 V2 definition

> *"Substitutability Function: The probability that a functionally adequate substitute exists at any given future time. Determines whether foreclosure cost approaches zero (high substitutability) or remains high (low substitutability). S(t) may be influenced by extraction timing — earlier extraction can slow innovation by reducing economic pressure to develop alternatives."*

### §2.2 CORE-math role

S enters the framework's foreclosure cost equation:
- **C₁ = [1 − S(t|t₀)] · U(R, t, Q(t))**

Where:
- C₁ is the first canonical cost term (foreclosure cost).
- S(t|t₀) is the probability a substitute for resource R exists at time t, given baseline t₀.
- U(R, t, Q(t)) is the utility cost if foreclosure occurs.
- (1 − S) is the probability foreclosure persists.

S(t|t₀) is **structurally load-bearing for C₁** — removing S would require rebuilding C₁ around a different substitutability treatment.

### §2.3 What makes S "framework's most novel single component" (per meta-pass §10.2)

Established economics has:
- Elasticity of substitution (Hicks 1932, Allen).
- Intertemporal substitution (macro theory).
- Technology-adoption probability functions.

Framework novelty of S:
- Expressed as a probability over future time (not as a point elasticity).
- Conditional on baseline t₀ (captures "given current tech state, what's the probability a substitute emerges by t?").
- Feedback term: "earlier extraction can slow innovation" — S isn't exogenous; depends on extraction timing.
- Used with S_max ceilings for scoping (industrial vs. existential — see CSG retirement pass).

This combination is framework-specific. Removing S and substituting elasticity-of-substitution would lose the probability-over-time + endogeneity features.

### §2.4 Options

As in §1.

### §2.5 Sub-claims

**Option A (confirm Ring 2):**
- SC-A1: S is load-bearing for CORE math (C₁ formula depends on it).
- SC-A2: S is distinct from all other primitives.
- SC-A3: Active operational use across 98 refs.
- SC-A4: Not a public-adoption target (mathematical object, not travel-ready phrase).

**Option B (promote Ring 1):**
- SC-B1: S's novelty earns adoption-target status.
- SC-B2: Policy discourse could adopt "substitutability probability" as framing.

**Option C (demote):**
- SC-C1: S is mathematical, not conceptual — could live only in Tech Appendix.

### §2.6 Falsifiers

**Option A is falsified if:**
- S collapses into established concept (elasticity of substitution) with no framework-specific residue.
- 98 refs all reduce to S_max uses (in which case the PRIMITIVE S might not be load-bearing, only S_max).

**Option B is falsified if:**
- Policymakers / lawyers don't use function-names.
- Travel-ready adoption requires phrase-level terms, not mathematical objects.

---

## §3. Principle #3 primitive-distinctness check (decisive module)

### §3.1 Reduction test

Can S reduce to an established economics concept without framework-specific residue?

| Established concept | Overlap with S | Residue (what S has that the concept doesn't) |
|---|---|---|
| Elasticity of substitution | Both describe substitute availability | Elasticity is a point-measure; S is a time-indexed probability with feedback. |
| Technology-adoption probability | Probability framing | No built-in baseline t₀ conditioning; no extraction-timing feedback. |
| Intertemporal substitution | Time element | Different domain (consumption vs. resources); no substitute-availability probability. |
| Real-options theory (Dixit-Pindyck) | Dynamic uncertainty + irreversibility | Close conceptually; S extends this to substitute-availability specifically. |

**Closest established concept:** real-options theory's approach to irreversible investment under uncertainty. But S's specific form (substitute-availability probability conditional on baseline, with extraction-timing feedback) isn't a real-option; it's a framework-specific formulation.

**Verdict:** S has framework-specific residue. Doesn't reduce cleanly to any established concept. **Principle #3 PASSES.**

### §3.2 Ring-1 vs Ring-2 distinguishing question

Why S is Ring 2 (not Ring 1):
- Ring 1 terms travel outside the book to policy/legal/academic adoption.
- Policymakers don't adopt named functions ("the Substitutability Function").
- They might adopt concepts ("substitutability matters over time") — but that's prose, not term.
- Book readers DO encounter S as a named function; they need it to understand C₁.
- Net: S is internal-load-bearing, not adoption-target. Ring 2 correct.

Compare with RCV — a named COMPOSITE QUANTITY that can travel ("the Residual Commons Value for this extraction is $X"). RCV is Ring 1. S doesn't travel that way because it's a function, not a quantity.

---

## §4. 98-ref concept audit (Principle #2)

### §4.1 Usage mode breakdown (estimated from grep + Ch 6/Ch 7 spot-read)

- **Mathematical-formal references** (in formula, Tech Appendix, CORE derivations): ~30–40%.
- **Conceptual-prose references** ("the substitutability function shows..."): ~40–50%.
- **Teaching/pedagogy references** (Ch 6 GuidanceDoc, Ch 7 GuidanceDoc): ~20%.

All three usage modes earn the term. Mathematical usage requires precise named function; prose usage benefits from named-concept handle; pedagogy benefits from named-concept anchor.

### §4.2 Ch 6 anchoring

Ch 6 GuidanceDoc places "The Substitutability Function" as §5 in the chapter structure — a dedicated section. This is the term's pedagogical home. Cannot demote without restructuring Ch 6.

### §4.3 S_max usage

S_max appears in CSG context (retired per commit `3ec3707` — S_max industrial vs existential gap). Even with CSG retired, S_max remains a derivation from S used in prose. No separate term needed — S_max is just "maximum of S over [scope]." Preserves primitive/derivation discipline.

---

## §5. M1–M11 abbreviated results

- **M1 CORE:** S is core-math load-bearing (in C₁ formula). Confirmed.
- **M2 Case study:** McDowell (coal substitutability over renewable-energy transition), Mars colony (rare-earth substitutability under industrial vs existential scopes), Chesapeake watermen (oyster substitutability across species decline). S applies cleanly.
- **M3 Book content:** 98 refs; Ch 6 dedicated section; heavy Tech Appendix anchoring. Active use.
- **M4 Craft:** "Substitutability function" is technical-academic register but unavoidable for mathematical discussion. Prose sections can use "substitutability probability" or "substitute availability" for register flexibility.
- **M5 Dinner-table:** "Probability a substitute exists by time t" parses for attentive general readers. Less for casual readers — but that's acceptable for Ring-2 internal term.
- **M6 Academic:** Positions as framework-specific extension of real-options / intertemporal-substitution. Tech Appendix citations recommended.
- **M7 Originality:** S is the framework's most novel mathematical element (per meta-pass). Originality claim survives.
- **M8 Long-term:** Ring-2 durability depends on framework adoption. If framework travels, S travels with it as internal vocabulary.
- **M9 Risk:** Minor — readers may confuse S (function) with S_max (scalar). Mitigable via Ch 6 + Tech Appendix clarification.
- **M10 Publishing:** Tech Appendix heaviness carries cost but acceptable.
- **M11 Critic:** *"Isn't this just elasticity of substitution?"* — Response: no — S is time-indexed probability with feedback; elasticity is a point measure. Survives.

**§22.4 alignment:** Option A positive (Ring 2 serves both internal coherence and appropriate-adoption-scope).

---

## §6. Verdict

**OPTION A — CONFIRM Ring 2.** S is the framework's most novel single mathematical component; load-bearing for C₁ formula; 98 active refs; distinct from other primitives; not a public-adoption target. Ring 2 (internal load-bearing) is the correct placement.

### §6.1 What changes

- **Terms Index:** S record populated as `CURRENT` at Ring 2 (first individual rigor pass).
- **Glossary v3:** keep v2 definition with minor edits — add sentence clarifying "S_max derivations (including the retired CSG formula) are compositional uses of S, not separate primitives."
- **Tech Appendix §L:** add methodological footnote citing real-options / intertemporal-substitution / elasticity-of-substitution literatures for academic positioning.
- **Ch 6 §Substitutability Function:** unchanged (already Ring-2 appropriate).

### §6.2 What doesn't change

- CORE math — unchanged.
- C₁ formula — unchanged.
- S's role in RCV integrand — unchanged.
- All 98 existing references — unchanged.

---

## §7. Term Provenance Record

### Substitutability Function (S)

**Working definition:** Probability function S(t|t₀) — probability that a functionally adequate substitute for resource R exists at future time t, conditional on baseline technological state at t₀. Appears in foreclosure-cost term C₁ = [1 − S(t|t₀)] · U(R, t, Q(t)). Influenced by extraction-timing feedback: earlier extraction can reduce innovation pressure and lower S(t) for future t.

**Status:** `CURRENT` at Ring 2 (recommended by this pass).

**Term-spec version:** v1.0 (first individual rigor pass on this term).

**Last reviewed:** 2026-04-24

**Rigor provenance:**
- Meta-pass §10.2 (commit `46600bc`) — identified as "framework's most novel single component"; Ring-2 default.
- This individual rigor pass — Option A (confirm Ring 2) verified with concept audit + distinctness check.

**Why Ring 2 (not Ring 1):**
- Mathematical function; not a travel-ready phrase for policy/legal discourse.
- Book readers need it to understand C₁; non-readers don't adopt.

**Why NOT demoted:**
- Load-bearing for CORE math.
- 98 active refs across 25 files.
- Ch 6 has a dedicated section built around it.

**Depends on:** C₁ formula structure · definition of "functionally adequate substitute" · baseline t₀ convention.

**Pairs with:**
- Externality Tail (E) — the other canonical cost term; sibling function, not derivation.
- Foreclosure Cost (C₁) — S is a factor in C₁.
- Extraction-timing feedback — S is not exogenous; depends on extraction choices.

**Staleness triggers:**
- CORE math restructured in a way that eliminates C₁ as a separate term.
- Academic field adopts an established term (e.g., "substitution elasticity function") that should displace "substitutability function."

**Notes:**
- S_max derivations (including retired CSG formula) are compositional uses of S, not separate primitives.
- Framework-specific features that distinguish S from elasticity of substitution + real-options theory: (1) time-indexed probability not point measure; (2) baseline-conditional; (3) endogenous feedback from extraction timing.

---

## §8. Author-ratified resolutions

**Ratified 2026-04-24 by Chris Winn — Option A (CONFIRM Ring 2).** Substitutability Function (S) confirmed as framework's most novel single mathematical component at Ring 2 (internal load-bearing). 98 active refs; structurally distinct from all other primitives; CORE-math load-bearing for C₁ foreclosure-cost formula; not a public-adoption target (function name, not travel-ready quantity).

**M12 citations activated (flipped from queued to ratified per Principle #6 Corollary C):**
- Hicks, John R. *The Theory of Wages* (1932) — foundational substitutability / elasticity-of-substitution lineage.
- Dixit, Avinash K. & Pindyck, Robert S. *Investment under Uncertainty* (Princeton 1994) — real-options theory / irreversibility-under-uncertainty closest established concept.

Both to be cited in Tech Appendix §L methodological footnote positioning S as framework-specific extension (time-indexed probability with baseline-conditional + extraction-timing feedback). Bibliography entries upgraded to ratified status.

---

## §9. Rerun gate

Rerun if:
- CORE math restructures to eliminate C₁ or redefine S's role.
- Academic field produces established terminology that should displace "Substitutability Function."
- Ring-1 vs Ring-2 boundary redrawn such that S becomes a public-adoption target.

---

*End of individual rigor pass v1.0.0. Option A (confirm Ring 2) recommended. S is framework's most novel single mathematical primitive; load-bearing for CORE; Ring-2 (internal) correct scope. Pending author ratification.*
