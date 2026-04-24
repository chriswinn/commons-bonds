# Commons Bonds — Extreme-Rigor Pass: Tier Reframing (with Duplication Check)

**Version:** 1.0.0
**Date:** 2026-04-24
**Protocol applied:** `tools/commons_bonds_rigor_protocol_v2.2.0.md` (M1 + M2 + M3 + M6 + M7 + M11 at maximum depth)
**Scope:** verification that the reframing claim — *tiers recast as empirical groupings of specific Cᵢ cost terms surfaced across the 18 case studies, rather than as a canonical decomposition* — survives extreme rigor. Includes an empirical duplication check (variables vs. tiers) at §5.3 that proved decisive for the verdict.
**Status:** Post-Phase-A2 gate. Prior history: the framework's 8-tier decomposition was examined for academic rigor after dimensions reached an acceptable state; the canonical-tier framing was recognized as unlikely to survive real academic pressure on the same grounds as canonical-dimensions before Path F. The test suite was revised to modular + Path-Comparison-enabled form (v2.0.0 → v2.2.0), and rerun on dimensions produced Path F. The canonical-tier position is **not** a live alternative under test here — it is the already-rejected status quo. What this pass tests is whether the *reframing* claim (tiers as empirical groupings of {Cᵢ}) survives the same level of extreme rigor Path F survived. The duplication check at §5.3 reveals it does not survive — not because the reframing is weaker than Path F, but because its premise (that tiers ARE groupings of Cᵢ) is empirically false in the v10 tier specification.
**Author:** Chris Winn

---

## §1. Executive summary

**The reframing claim — tiers as empirical groupings of specific Cᵢ cost terms — FAILS SC-1 (the premise that tiers are groupings of variables) on the empirical duplication check at §5.3.** Five of the nine v10 tiers are themselves single variables (not groupings). One tier (Foreclosure Cost) is pure duplication with C₁ in the RCV formula. Three tiers are ambiguous (could be single variables or small groupings). Zero tiers are clear groupings of multiple distinct sub-variables. The v10 tier list is structurally a mis-labeled variable list, not a grouping over variables.

**Recommended path: full dissolution of the tier schema at the framework-specification level.** The framework operates cleanly at the variable level (Sections L and M of Technical Appendix v0.0.4). Most v10 tiers become individually-named variables in the Cᵢ set (C_foreclosure, C_community_transition, C_dynastic_labor, C_political_capture, C_individual_risk, C_mission_failure_reserve). Ambiguous tiers get resolved into one or more specific Cᵢ as needed per Context. The Tier 4 / C₁ duplication is cleaned up by retaining C₁ as the formula term and dropping "Tier 4" as a parallel label. The Tier 6 / E overlap is cleaned up via the independence gate (L.4) — either by redefining E to exclude ecological-carrying content or by merging the two terms.

**What the book retains:** the *specific content* of each v10 tier persists as named variables in the Cᵢ set. Nothing is lost analytically. Ch 8's worked example becomes "one extraction walked through the specific Cᵢ AIT surfaces in this Context" rather than "one extraction walked through eight canonical tiers." Reader legibility is preserved by naming the variables clearly (not by grouping them under an ontological tier label).

**What's optional for a future question:** if the author wants coarse pedagogical groupings at a clearly-higher level of abstraction than variables (e.g., Health + Community + Environmental + Intergenerational as four macro-categories, each containing multiple distinct Cᵢ), that's a design choice that can be made separately with its own rigor pass. It is NOT the v10 tier schema. The v10 tiers don't convert cleanly to such a macro-grouping because they aren't consistently-at-a-higher-level-of-abstraction than variables.

**The four tests and their verdicts:**

| Test | Verdict | Key finding |
|---|---|---|
| **§3 Mathematical / structural** | PASS (for reframing) | Formula is indifferent to grouping structure; this is why dissolution is mathematically admissible. |
| **§4 Philosopher-of-science** | PASS for reframing framing in principle; MOOT for v10 tier set | Reframing logic is coherent, but v10 tiers don't instantiate it. |
| **§5.3 Duplication check (decisive)** | **FAIL on SC-1** | 5 of 9 v10 tiers are variables, 1 is pure C₁ duplication, 3 are ambiguous, 0 are clear groupings of multiple distinct sub-variables. The v10 tier schema cannot be reframed as "groupings of Cᵢ" because it is empirically not that. |
| **§5.4 Dissolution (recommended)** | PASS-WITH-CONDITIONS | Dissolving tiers and working directly on named variables is internally consistent, preserves the book's analytical content, and closes the duplication and category-confusion gaps. Conditions specified in §8. |
| **§6 AI-adversary** | PASS | Adversarial tier proposals fail at the gate level (Section L). Dissolution does not weaken this. |

**Aggregate verdict:** The specific reframing claim as stated (tiers recast as empirical groupings) FAILS on the duplication check because the v10 tiers are not groupings to reframe. **Recommended path: dissolve the tier schema; variables replace tiers; optional future question about coarse macro-groupings at a higher abstraction level.** Conditions at §8.

**What this means for the author's intuition:** the framing "I have a feeling tiers might have a similar fate as dimensions" was tracking a real structural issue — not a parallel-reframing opportunity but a category-confusion that the reframing surfaces. Dimensions under Path F survived because the 10 abundance dimensions ARE real organizational scaffolding over variables AIT has surfaced (each dimension corresponds to an abundance-condition that structures a class of scarcity-grounded costs). Tiers under v10 do NOT parallel that — they are mostly single-variable alt-names that collided with the formula's C₁ in one case (Foreclosure) and with the E term in another (Ecological Carrying). The parallel to dimensions breaks because the dimension list is genuinely grouping-level while the tier list is genuinely variable-level.

**What this means for next steps:** Phase A3 (or Phase B Task 12 integration) executes the dissolution: variables named and enumerated, tier schema archived, Technical Appendix Section C.4 rewritten or removed, Ch 8 restructured, the decomposition doc retired or reconceived. Conditions at §8 specify each move.

---

## §2. The specific claim under test

### §2.1 The claim (as stated by the author)

"Tiers recast as empirical groupings of specific Cᵢ cost terms surfaced across the 18 case studies, rather than as a canonical decomposition."

The claim has three load-bearing moves:

1. **Groupings over taxonomy.** Tiers are groupings of cost variables — subsets of {Cᵢ} — not a claimed universal or ontological decomposition of extraction costs.
2. **Empirical over canonical.** The groupings are observed across the 18 case studies in the framework's development history; they are not asserted as definitional categories.
3. **Specific variables over abstract categories.** Each grouping's content is the specific Cᵢ that AIT + the four gates have surfaced in the 18 cases, not a claimed-complete enumeration of what that grouping must always contain.

### §2.2 What the claim repositions away from

The starting point for this rigor pass is the recognition that the prior framing — an eight-tier canonical decomposition of Full Generational Cost — would not survive real academic pressure. Canonical tiers inherit the same unfalsifiability, reproducibility, and bounded-set concerns that Path F had to defeat for canonical dimensions, and arguably in sharper form, because tiers never had the AIT-derived or RCV-mathematical justification that dimensions had. A published framework claiming the eight tiers as the universal decomposition would be committed to a taxonomic closure the framework cannot demonstrate. The reframing strips that commitment.

### §2.3 The claim decomposed into testable sub-claims

1. **SC-1 (Premise — the tier schema IS a grouping structure).** Each v10 tier groups multiple distinct Cᵢ variables. Tiers sit at a higher level of abstraction than variables.

2. **SC-2 (Empirical).** The eight groupings published in the book are empirically supported by convergence across 18 case studies. Groupings emerged from applying AIT to cases and recording what surfaced, not from top-down taxonomic choice.

3. **SC-3 (Pedagogical).** Groupings carry non-zero cognitive + audit value. Walking one extraction through eight named groupings is more cognitively legible than walking through ~20–40 individual Cᵢ terms without grouping.

4. **SC-4 (Extensibility).** New extraction contexts may surface Cᵢ that group naturally under a structure different from the eight published groupings. The framework supports per-Context grouping choices.

5. **SC-5 (Dispositional).** The book's text, the Technical Appendix Section C.4, and the decomposition doc must each state the empirical-groupings-not-canonical-decomposition status explicitly.

### §2.4 What falsifies the reframing claim

**The claim is falsified if:**

- **SC-1 fails.** The v10 tiers are not, in fact, groupings of multiple distinct Cᵢ — they are either alt-named single variables or they overlap with variables already specified elsewhere in the framework. **This is tested in §5.3 and found to occur.**
- The eight-grouping structure is shown to be load-bearing in the RCV mathematics.
- Empirical testing across the 18 cases reveals that groupings do NOT converge.
- Ch 8's didactic argument collapses under the reframing.

**Verdict below (§7):** the claim is falsified on SC-1 per the §5.3 duplication check. The recommended path pivots to full dissolution (§5.4), which is internally consistent and addresses the duplication + category-confusion problems the v10 tier schema carries.

---

## §3. Mathematical / structural test

### §3.1 The formula's indifference to grouping structure

**Canonical two-term RCV (Section B.1):**

```
RCV(R, t₀) = ∫ₜ₀^∞ {[1 − S(t | t₀)] · U(R, t, Q(t)) + E(R, t)} · D(t, t₀) dt
```

**Generalized sum-of-costs (Section M):**

```
RCV(R, t₀, Context) = ∫ₜ₀^∞ {Σᵢ₌₁ⁿ Cᵢ(R, t, Context)} · D(t, t₀) dt
```

Neither form references grouping structure. The integrand is expressed in terms of individual cost terms {Cᵢ}. Any labeling applied to subsets of {Cᵢ} — including v10 tiers, alternative groupings, or no grouping at all — is invisible to the integrator. Under the formula, a sum over {Cᵢ} is identical to a sum over (Σ_{group-1-members} Cᵢ + Σ_{group-2-members} Cᵢ + ... + Σ_{group-k-members} Cᵢ) for any partitioning of {Cᵢ} into k groups. The partition is invisible.

**§3.1.1 Merger test.** Collapse tiers 2a and 2b into a single "Risk Cost" label. If 2a and 2b are distinct variables, the combined grouping now contains two Cᵢ. RCV unchanged. **PASS.**

**§3.1.2 Split test.** Split tier 7 (Knowledge and Culture Cost) into two sub-items (Knowledge Cost + Cultural Cost). {Cᵢ} unchanged; labels subdivided. RCV unchanged. **PASS.**

**§3.1.3 Rearrangement test.** Reorder labels. RCV unchanged. **PASS.**

**§3.1.4 Dissolution test.** Remove all grouping labels; work directly on named {Cᵢ}. RCV unchanged. **PASS.** This is the test the §5.4 recommended path will exercise.

### §3.2 Convergence, dimensional consistency, CS relation

- **Convergence** (Section M.2): depends on individual Cᵢ convergence per gate L.3, not on grouping structure.
- **Dimensional consistency** (Section M.3): requires each Cᵢ to have units [$ · res-unit⁻¹ · time-unit⁻¹]. Groupings do not alter unit analysis.
- **CS = RCV − B** (Section M.4): depends on RCV as a scalar output, not on internal assembly.

### §3.3 Mathematical proof test — aggregate verdict

**PASS.**

The mathematics has never seen tier structure. The prior canonical-tier framing was carrying a rhetorical claim (universal decomposition) that the formula did not require and could not verify. Both the reframing path (if SC-1 held) and the dissolution path (§5.4) are mathematically admissible. No mathematical pre-Phase-A3 condition is required from §3.

---

## §4. Philosopher-of-science extreme pressure

*Note: this section tests the reframing framing in principle. The challenges below are defeatable under the reframing's published discipline. The §5.3 duplication check then reveals that the v10 tiers don't actually instantiate the reframing, which makes the §4 challenges moot for the v10 set — but the logic remains valid for any future genuine grouping structure.*

### §4.1 Challenge — Unfalsifiability

**The challenge:** "If tiers are 'just organizational,' then any new tier label can be introduced whenever convenient. Tier structure is unfalsifiable because it is not a claim about anything."

**Response:** Under the reframing, tier structure makes three falsifiable claims: (a) empirical-grouping claim (the published groupings match observed convergences across cases), (b) pedagogical-legibility claim (grouped walkthrough is more cognitively legible than ungrouped), (c) audit-comparability claim (shared vocabulary enables cross-case analysis). Each is falsifiable by appropriate evidence. **DEFEATED in principle.**

**In practice (post-§5.3):** if the v10 "tiers" are not groupings, the empirical-grouping claim does not apply to them — it would apply only to a genuine grouping structure that has not yet been specified. The reframing framing is defensible; the v10 schema does not instantiate it.

### §4.2 Challenge — Reproducibility at the tier level

**The challenge:** "Different analysts will produce different grouping structures over the same {Cᵢ}, so tier-level outputs are irreproducible."

**Response under reframing:** Reproducibility at the grouping level is a weaker requirement than at the variable level. Different analysts can legitimately produce different groupings; what must agree is the underlying {Cᵢ} admitted by the gates. **DEFEATED.**

**In practice (post-§5.3):** since v10 tiers are largely variables, this challenge applies at the variable level where reproducibility IS required — and variables are reproducible under the gate discipline. The challenge collapses into the already-addressed variable-level reproducibility question from the Path F rigor pass.

### §4.3 Challenge — Bounded tier set

**The challenge:** "What bounds the number of tiers?"

**Response under reframing:** In principle unbounded; in practice constrained by cognitive load and community-vocabulary conventions. **DEFEATED** in principle.

**In practice (post-§5.3):** bound is currently unenforced because v10 is a mixed variable/grouping list, not a clean grouping hierarchy. Under dissolution, this question ceases to apply at the framework level.

### §4.4 Challenge — Arbitrary-dissolution

**The challenge:** "If tiers are optional, dissolve them."

**Response pre-§5.3:** tiers earn their place through pedagogical and audit affordance; retention is justified by utility. **DEFEATED** in principle.

**Response post-§5.3:** the challenge is correct for the v10 tier set. The v10 tiers earn less than they cost (duplication + category confusion), and dissolution is the preferred path. The "earn their place" defense applies to HYPOTHETICAL groupings that are genuinely grouping-level, not to the v10 set.

---

## §5. Applied-economist extreme pressure

### §5.1 Challenge — Chapter 8's argument structure

**The challenge:** "Ch 8 walks one extraction through eight tiers. Under the reframing, its didactic argument weakens."

**Response under reframing:** Ch 8 reframed slightly loses ontological-claim power but gains accuracy. Preserved, slightly rephrased.

**Response under dissolution (§5.4):** Ch 8 becomes "one extraction walked through the specific named Cᵢ that AIT + the four gates surface in this Context." Reader legibility is preserved by named variables. The eight-category scaffolding is replaced by a variable-walkthrough that names each cost specifically (black-lung cost, acid-mine-drainage remediation, carbon externality, community-transition cost, political-capture cost, etc.) without ambient ontological commitment. This is arguably MORE legible than the tier version because each cost is specified at the level the framework actually operates on.

### §5.2 Challenge — Technical Appendix Section C.4

Section C.4 currently enumerates the Eight-Tier FGC Decomposition as "Canonical v10." Under dissolution, Section C.4 is retired or restructured as "Variables surfaced in the 18 case studies" — a catalog of specific Cᵢ terms that have been admitted under the gates, indexed by case and by Context, without tier groupings.

### §5.3 The duplication check — variables vs. tiers

**This is the decisive empirical test.** Each v10 tier is mapped against the framework's variable apparatus (Section B.1 canonical two-term formula, Section M sum-of-costs generalization, Section L four-gate discipline, Section L.6 worked example introducing C₃). The question for each tier: is this a grouping of multiple distinct variables, or is it itself a variable (or variable-overlap)?

| Tier | Name | Status | Finding |
|---|---|---|---|
| 1 | Lifetime Survival Cost | **AMBIGUOUS** | Reads as a grouping (black-lung + cardiovascular + asbestosis + burnout + ...) but published as a single tier without sub-variables named. Could be either. Needs per-case specification at the variable level. |
| 2a | Individual Risk Cost | **VARIABLE** | Single actuarial-risk cost term per unit extraction. Not a grouping. |
| 2b | Mission Failure Reserve | **VARIABLE** | Single contingency-cost term per unit extraction. Not a grouping. |
| 3 | Dynastic Labor Cost | **VARIABLE** | Single intergenerational-labor cost term per unit extraction. Not a grouping. |
| 4 | Foreclosure Cost | **IS C₁** | The tier IS the variable. Section B.1 and Section M explicitly specify foreclosure as C₁ = [1 − S(t \| t₀)] · U(R, t, Q(t)). Tier 4 is not a grouping of variables; it is one specific variable that already has formula status under a different name. Pure duplication. |
| 5 | Community Transition Reserve | **VARIABLE** | Single community-transition-cost term. Same as C₃ in the Section L.6 worked example. Not a grouping. |
| 6 | Ecological Carrying Cost | **AMBIGUOUS + OVERLAP** | Could be a single aggregated variable or a grouping (hydrological + biodiversity + carbon-sequestration + pollination). Additionally overlaps with canonical E externality tail (Section B.1) — independence-gate concern under L.4. |
| 7 | Knowledge and Culture Cost | **AMBIGUOUS** | Could be a single knowledge-and-cultural variable, or split into knowledge-cost + cultural-cost. Not obviously a grouping of many distinct sub-variables. |
| 8 | Political Capture Cost | **VARIABLE** | Single political-capture cost term per unit extraction. Not a grouping. |

**Tally:**

- **VARIABLES:** 5 (2a, 2b, 3, 5, 8)
- **IS C₁ (pure duplication):** 1 (Tier 4 Foreclosure Cost)
- **AMBIGUOUS (single variable or small grouping):** 3 (1, 6, 7)
- **CLEAR GROUPINGS of multiple distinct sub-variables:** 0
- **Total:** 9 tiers checked

**Finding:** SC-1 (the premise that tiers ARE groupings of variables) **FAILS** for the v10 tier schema. Five tiers are explicitly single variables. One tier is pure duplication with a formula term. Three are ambiguous but defensibly resolvable into single variables or small variable-pairs. Zero tiers are unambiguous groupings of multiple distinct sub-variables at a level-of-abstraction above the variable level.

**Independence gate violation identified:** Tier 6 (Ecological Carrying Cost) overlaps with the canonical E externality-tail term (Section B.1). Under L.4, this overlap requires resolution by redefinition, merger, or rejection. The overlap has not been explicitly resolved in v10 because v10 predates Section L.

**Formula duplication identified:** Tier 4 (Foreclosure Cost) is identical to C₁ under Section B.1 / Section M specifications. Under a clean variable specification, C₁ is the formula term and "Tier 4" is a redundant second name for the same quantity.

**Implication:** the v10 tier schema cannot be reframed as "empirical groupings of Cᵢ" because the schema is not structurally a grouping schema. It is a mixed list of single-variable-named items with at least one formula duplicate and at least one formula overlap. The reframing as stated in §2.1 fails SC-1.

### §5.4 The preferred path — full dissolution with variables replacing tiers

**What this path does:**

- **Framework specification:** drop tier schema entirely at the framework level. The framework operates on {Cᵢ} per Sections B.1, L, M. There is no "tier" layer in the framework's canonical specification.
- **Variables:** retain the analytical content of each v10 tier by naming individual Cᵢ in the variable set. For example:
  - C_foreclosure = [1 − S(t | t₀)] · U(R, t, Q(t)) (was Tier 4)
  - C_community_transition = community-transition-reserve cost per unit extraction (was Tier 5)
  - C_dynastic_labor = intergenerational-labor cost per unit extraction (was Tier 3)
  - C_political_capture = political-capture cost per unit extraction (was Tier 8)
  - C_individual_risk = actuarial-risk cost per unit extraction (was Tier 2a)
  - C_mission_failure = mission-failure-reserve cost per unit extraction (was Tier 2b)
  - Tier 1 (Lifetime Survival): resolved per Context into specific health variables (black-lung, cardiovascular, asbestosis, etc.) or into a single aggregated C_lifetime_survival. Per-Context specification.
  - Tier 6 (Ecological Carrying): resolved per Context into ecosystem-service sub-variables OR merged into E under Section L.4 independence-gate discipline. Per-Context specification; overlap with E resolved transparently.
  - Tier 7 (Knowledge and Culture): resolved per Context into knowledge-cost + cultural-cost as separate variables, or treated as single aggregated variable.
- **Decomposition doc (`core/decomposition/eight-tier-v10.html`):** retired with a historical note. Contents preserved in archive. The decomposition doc is no longer canonical.
- **Technical Appendix Section C.4:** rewritten as "Catalog of Variables Surfaced in 18 Case Studies" — a flat index of named Cᵢ with their per-Context specifications, gate verification status, and convergence properties.
- **Ch 8 draft:** restructured to walk McDowell coal through the specific named Cᵢ that AIT + the four gates surface for that Context. Each Cᵢ gets named and priced. Reader legibility is carried by the named variables, not by tier groupings.
- **Ch 6 draft:** minor update acknowledging that variables are the framework's unit of measurement. No tier references needed.

**What this path preserves:**

- Every analytical cost the v10 tiers pointed at. Nothing is lost by dissolution; only the tier label is lost. The substance becomes named variables.
- Ch 8's didactic structure (one extraction, multiple costs). The walkthrough just happens at the variable level, not the tier level.
- Cross-case comparability. Cases are compared by variable set (which Cᵢ are present in each Context) rather than by tier structure. This is actually MORE granular and legible than tier-level comparison.

**What this path closes:**

- Tier 4 / C₁ duplication (the two names for the same quantity).
- Tier 6 / E overlap (independence-gate violation, now resolved explicitly under L.4).
- Category confusion between grouping-level and variable-level entities in the v10 schema.
- The rhetorical burden of defending an eight-tier canonical decomposition that could not survive academic pressure.

**What this path does NOT do:**

- Does NOT decide whether to introduce a HIGHER-LEVEL coarse grouping (3–4 macro-categories) as a pedagogical device above the variable level. That is a separate design choice — see §10.

### §5.5 The side-question — coarse macro-groupings

A legitimate open design choice: would the book benefit from a clearly-higher-level macro-grouping over variables (e.g., 3–4 categories at a single step of abstraction above Cᵢ)? An illustrative candidate structure:

- **Household costs:** C_individual_risk, C_lifetime_survival (or its sub-variables), C_mission_failure, C_dynastic_labor, ...
- **Community costs:** C_community_transition, C_knowledge_culture, C_political_capture, ...
- **Environmental costs:** E (carbon, hydrological, atmospheric), C_ecological_carrying (or sub-variables), ...
- **Intergenerational foreclosure costs:** C_foreclosure (= C₁), stock-dependent-utility-loss, substitutability-window-loss, ...

Each macro-category would contain multiple distinct Cᵢ at the variable level. This IS grouping-over-variables, unlike v10. Whether to introduce such a structure is a pedagogical choice for Ch 6 / Ch 8 / the Technical Appendix.

**This side-question is NOT part of the dissolution decision.** It is preserved as §10 Condition 6 for separate ratification. The dissolution decision is about whether to retire the v10 tier schema (answer: yes). The macro-grouping question is about whether to add a new coarser structure (answer: optional, to be decided).

---

## §6. AI-adversary extreme pressure

### §6.1 Adversarial case — "The reframing fails; therefore the framework fails"

**Adversarial claim:** "If tiers were the framework's canonical decomposition and the decomposition fails rigor, the framework is unsound."

**Response:** The framework's authority sits at the variable and gate level (Section L), not at the tier level. Tiers were pedagogical scaffolding layered on top of the framework's actual math. Removing them does not weaken the framework; it aligns the framework's presentation with what the framework actually is. **DEFEATED.**

### §6.2 Adversarial case — "Variables are just renamed tiers; nothing has changed"

**Adversarial claim:** "You moved from 'tier' to 'C_foo' and called it a dissolution. Semantic only."

**Response:** Not quite. The framework's Cᵢ variables are specified at the formula level (Sections B.1, M) with dimensional, boundedness, AIT, and independence gates (Section L). Each Cᵢ has a formal statement, a units signature, a convergence verification, and an independence check. The v10 tiers had none of these — they had a definition paragraph and an abundance-dimension invocation that became circular once Path F reframed dimensions. The dissolution is not a rename; it is a move from informally-specified cost categories to formally-gate-tested cost variables. **DEFEATED.**

### §6.3 Adversarial case — "Dissolving tiers makes Ch 8 worse"

**Adversarial claim:** "Ch 8 reads cleanly with the eight-tier walkthrough. Dissolving tiers replaces named categories with abstract Cᵢ notation."

**Response:** The dissolution preserves names, not notation. "C_community_transition" in the framework specification becomes "Community Transition Cost" in Ch 8's prose. The variable has a readable name; the subscripted notation is for the Technical Appendix. Ch 8's reader sees "Community Transition Cost," "Dynastic Labor Cost," "Political Capture Cost" — the same category names that used to be called "Tier 5," "Tier 3," "Tier 8." What's removed is the "Tier N:" prefix and the implicit claim of canonical decomposition. Readability is unchanged; ontological commitment is dropped. **DEFEATED.**

### §6.4 AI-adversary extreme pressure — aggregate verdict

**PASS.** Dissolution does not weaken the framework under any adversarial attack because the framework's authority never sat at the tier level.

---

## §7. Aggregate verdict

**THE REFRAMING CLAIM AS STATED (TIERS RECAST AS EMPIRICAL GROUPINGS OF Cᵢ) FAILS ON THE §5.3 DUPLICATION CHECK BECAUSE THE v10 TIER SCHEMA IS NOT A GROUPING STRUCTURE.**

**RECOMMENDED PATH: FULL DISSOLUTION PER §5.4.** Variables replace tiers at the framework-specification level. Analytical content is preserved as named Cᵢ. Ch 8, Technical Appendix Section C.4, and the decomposition doc are restructured accordingly. Independence-gate violations (Tier 6 vs E) and formula duplications (Tier 4 vs C₁) are resolved in the restructuring.

| Test | Verdict |
|---|---|
| §3 Mathematical / structural | PASS (both reframing and dissolution are admissible) |
| §4 Philosopher-of-science (reframing in principle) | PASS-WITH-CONDITIONS |
| §5.3 Duplication check (empirical) | **SC-1 FAIL for v10 schema** |
| §5.4 Dissolution (recommended) | PASS-WITH-CONDITIONS |
| §5.5 Coarse macro-grouping (side-question) | OPTIONAL, separate decision |
| §6 AI-adversary | PASS |

---

## §8. Conditions for dissolution to land

Four conditions, each addressable in Phase A3 (a brief follow-on to Phase A2) or absorbed into Phase B chapter-drafting work.

### Condition 1 — Decomposition doc retirement

**What:** Archive `core/decomposition/eight-tier-v10.html` with a retirement note stating the dissolution decision and pointing readers to the variable-level catalog replacing it.

**Effort:** 0.5 day.

**Where:** `core/decomposition/` — move to archive, or add a prominent retirement banner at the top.

### Condition 2 — Technical Appendix Section C.4 restructure

**What:** Rewrite Section C.4 of Technical Appendix v0.0.4 from "Eight-Tier FGC Decomposition (Canonical v10)" to "Catalog of Variables Surfaced in Case Studies." A flat index of named Cᵢ with their per-Context specifications, gate verification status, and convergence properties. The 18-case empirical content is preserved; only the tier-grouping structure is removed.

**Effort:** 2–3 days.

**Where:** `core/technical-appendix/TechnicalAppendix_v0.0.4.html` Section C.4.

### Condition 3 — Ch 8 draft restructure for variable walkthrough

**What:** Revise Ch 8 to walk McDowell coal through named Cᵢ directly. Each variable gets its prose-name (Community Transition Cost, Dynastic Labor Cost, Political Capture Cost, etc.), its AIT-pass justification, its dimensional check, and its dollar-value estimate. No "Tier N:" framing. The chapter's didactic structure (one extraction, systematic accounting across costs) is preserved.

**Effort:** 2–4 days. Consistent with Phase B Task 12 (Ch 8 worked-example reframing) — can be absorbed into that task without scope expansion, or executed standalone in Phase A3.

**Where:** `manuscript/chapters/Chapter__8_WhatThingsActuallyCost_Draft.md`.

### Condition 4 — Ch 6 draft minor update

**What:** Ch 6's current "The Four Gates" section and "The Contribution" section stand as is. Add a single sentence or phrase acknowledging that the book's unit of measurement is the cost variable Cᵢ — not a tier or dimension. Remove any implicit eight-tier references in Ch 6.

**Effort:** 0.25–0.5 day.

**Where:** `manuscript/chapters/Chapter__6_ThreeWaysofCounting__Draft.html`.

### Optional Condition 5 — Resolve Tier 6 / E overlap explicitly

**What:** Under the independence gate L.4, decide: either (a) narrow E to exclude ecological-carrying-cost content and introduce C_ecological_carrying as a separate variable, or (b) merge ecological-carrying-cost content into the E term and retire the separate variable. Document the decision in the Technical Appendix Section M.4 or Section L.4 examples.

**Effort:** 0.5 day (decision + documentation).

**Where:** `core/technical-appendix/TechnicalAppendix_v0.0.4.html` — Section L.4 (add to worked examples) and/or Section M (corollary).

### Optional Condition 6 — Macro-grouping design decision (§5.5 side-question)

**What:** Decide whether to introduce a coarse macro-grouping (3–4 macro-categories like Household / Community / Environmental / Intergenerational) at a level clearly above the variable level. If yes, run a brief rigor pass on the proposed macro-structure and integrate into Ch 6 + Ch 8 + Technical Appendix C.4. If no, leave the variable-level catalog as the only structural layer.

**Effort:** 0 days if deferred; 3–5 days if executed (including rigor-pass). Separate decision from Conditions 1–5.

**Where:** new rigor pass + multiple docs if executed.

---

## §9. Mapping to existing work

### §9.1 Already landed (Phase A1 / Phase A2)

- `core/decomposition/eight-tier-v10.html` — Path F preamble callout landed Phase A1 Task 4 (2026-04-24, commit f227d08). Under dissolution, the doc is retired rather than strengthened.
- `core/technical-appendix/TechnicalAppendix_v0.0.4.html` — Section C.4 currently v10-canonical. Under dissolution, restructured per Condition 2.
- `tools/rigor-passes/commons_bonds_rigor_pass_2026-04-24_path_f_variable_addability_v1.0.0.md` — the parallel dimension-level rigor pass that established the variable-and-gate framework this tier pass builds on.

### §9.2 Landed in this rigor pass

- `tools/rigor-passes/commons_bonds_rigor_pass_2026-04-24_tier_reframing_v1.0.0.md` — this document.

### §9.3 Phase A3 or Phase B integration

Conditions 1–4 above can land as a new Phase A3 (4–7 days before Phase B begins) or absorbed into Phase B chapter-drafting. Recommendation is Phase A3 — produces a clean boundary between framework-specification-work and chapter-drafting-work. Optional Condition 5 runs with or shortly after Phase A3. Optional Condition 6 is deferred to separate decision.

---

## §10. Naming — the open optional side-question

### §10.1 What the dissolution changes about vocabulary

With tiers dissolved, the book's working vocabulary is:

- **Variables (Cᵢ)** — cost terms admitted to the RCV integrand under the four gates.
- **Dimensions** — the 10 abundance dimensions under Path F v1.3.0 (Habitability · Spatial · Temporal · Institutional · Kindred · Ecosystem · Political · Cohesion · Epistemic · Autonomy).
- **Contexts** — specific extraction situations defining which Cᵢ apply.
- **Gates** — the four admission tests (AIT, dimensional, boundedness, independence).

"Tier" disappears from the canonical vocabulary. It may persist in prose descriptions ("the several costs," "the various categories") but is not a defined term in the framework.

### §10.2 What replaces "tier" in prose

Where the book previously said "the Community Transition Reserve tier," it now says "the Community Transition Reserve cost" or "the community-transition variable." Where it said "the eight tiers," it now says "the cost variables surfaced by this case" (specific) or "the costs the framework prices" (general).

### §10.3 Whether to introduce macro-category vocabulary

If §5.5 Condition 6 is ratified (introduce coarse macro-grouping), the macro-groupings would need names — e.g., "Household Costs," "Community Costs," "Environmental Costs," "Intergenerational Costs." These are at a clearly higher level of abstraction than variables and would not be called "tiers" (that term is retired).

### §10.4 Recommendation

Retire "tier" from canonical vocabulary per the dissolution. Defer the macro-grouping-vocabulary decision to Condition 6 if and when that side-question is taken up.

---

## §11. Author-ratified resolutions

*Ratified 2026-04-24 by Chris Winn. Full dissolution path chosen. §5.5 macro-grouping side-question escalated to its own rigor pass per §11.6 (a). Sequencing TBD pending macro-grouping rigor-pass outcome; Conditions 1–4 proceed in either (a) or (b) sequencing case.*

### §11.1 Condition 1 — Decomposition doc retirement

**Ratified decision:** APPROVED (dissolution path). Archive `core/decomposition/eight-tier-v10.html` with a retirement banner stating the dissolution decision and pointing readers to Technical Appendix Section C.4 variable catalog.

**Execution spec:** Per §8 Condition 1. Effort: 0.5 day.

### §11.2 Condition 2 — Section C.4 restructure

**Ratified decision:** APPROVED. Rewrite Section C.4 as "Catalog of Variables Surfaced in Case Studies." Flat index format.

**Execution spec:** Per §8 Condition 2. Effort: 2–3 days.

### §11.3 Condition 3 — Ch 8 restructure

**Ratified decision:** APPROVED. Restructure Ch 8 walkthrough from tier-level to variable-level. Preserve analytical content; preserve didactic structure. Placement (Phase A3 standalone vs. Phase B Task 12 absorption) depends on §11.7 sequencing choice.

**Execution spec:** Per §8 Condition 3. Effort: 2–4 days.

### §11.4 Condition 4 — Ch 6 minor update

**Ratified decision:** APPROVED. Single-sentence or phrase addition acknowledging variables as the framework's unit of measurement; remove any implicit tier references.

**Execution spec:** Per §8 Condition 4. Effort: 0.25–0.5 day.

### §11.5 Optional Condition 5 — Tier 6 / E overlap resolution

**Ratified decision:** *(pending — deferred pending macro-grouping rigor-pass outcome; the Tier 6 / E overlap may be affected by whether macro-grouping is ratified).*

**Options (preserved for later decision):**
- (a) Narrow E to exclude ecological-carrying content; introduce C_ecological_carrying as separate variable.
- (b) Merge ecological-carrying content into E; retire the separate variable.
- (c) Defer; address per-Context as cases demand.

### §11.6 Optional Condition 6 — Macro-grouping design

**Ratified decision (2026-04-24):** REJECTED via separate rigor pass. Macro-grouping pass verdict: Option A (reject macro-groupings at every level — no framework-canonical macro-categories, no chapter-layout permit for thematic section headings). Pure variable enumeration with narrative pacing is the book's structural approach. Author's prior (abstraction-hides-severance) was confirmed by §7 of the macro-grouping pass; rigor also identified negative alignment with success criterion (vocabulary dilution), academic reception (rigor concerns reproduce one layer up), and long-term project impact.

**Rigor pass:** [`tools/rigor-passes/commons_bonds_rigor_pass_2026-04-24_macro_grouping_v1.0.0.md`](commons_bonds_rigor_pass_2026-04-24_macro_grouping_v1.0.0.md) — Option A ratified at §10.

### §11.7 Sequencing decision

**Ratified decision:** *(pending author selection — macro-grouping pass has resolved, so the choice is now live).* Macro-grouping pass ratified Option A (reject entirely); Condition 6 adds minimal effort to any sequencing option. The three sequencing options remain available:

**Options:**
- (a) Phase A3 (4–7 days, before Phase B). Clean methodology-complete boundary. Recommended.
- (b) Absorb Conditions 1 + 2 + 4 into Phase A2.5 (1–2 days); defer Condition 3 into Phase B Task 12.
- (c) Defer all conditions into Phase B chapter-drafting work.

---

## §12. Sequenced task list (pending author ratification)

Ordered per dependency.

| # | Task | Location | Depends on | Est. effort | Lands in |
|---|---|---|---|---|---|
| 1 | **Condition 1: Decomposition doc retirement** | `core/decomposition/eight-tier-v10.html` → archive or retirement banner | — | 0.5 day | Phase A3 |
| 2 | **Condition 2: Section C.4 restructure** | `core/technical-appendix/TechnicalAppendix_v0.0.4.html` | — (can parallel Task 1) | 2–3 days | Phase A3 |
| 3 | **Condition 4: Ch 6 minor update** | `manuscript/chapters/Chapter__6_ThreeWaysofCounting__Draft.html` | — (can parallel Tasks 1–2) | 0.25–0.5 day | Phase A3 |
| 4 | **Optional Condition 5: Tier 6 / E overlap resolution** | `core/technical-appendix/TechnicalAppendix_v0.0.4.html` Section L.4 + M | Task 2 | 0.5 day | Phase A3 or deferred |
| 5 | **Condition 3: Ch 8 restructure** | `manuscript/chapters/Chapter__8_WhatThingsActuallyCost_Draft.md` | Tasks 1–2 | 2–4 days | Phase A3 or Phase B Task 12 |
| 6 | **Optional Condition 6: Macro-grouping mini-rigor-pass + multi-doc update** | Multiple docs | — (independent) | 3–5 days | Deferred unless ratified |

**Total Phase A3 effort (Conditions 1–4 + Condition 5, standalone):** ~6–8 days.
**Total Phase A2.5 effort (Conditions 1 + 2 + 4, defer Condition 3 to Phase B):** ~3–4 days.

---

## §13. Rerun gate

This rigor pass can be rerun at any time after Phase A3 methodology work lands to verify Conditions 1–4 have been met. Expected next rerun: after decomposition-doc retirement + Section C.4 restructure + Ch 6 minor update land. Verification: check that (a) the tier schema is retired in the three locations, (b) Section C.4 reflects a variable-catalog structure, (c) the independence-gate check for Tier 6 / E is resolved or deferred, (d) Ch 6 prose acknowledges variables as the unit. Partial rerun at end of Phase A2.5 + full rerun after Ch 8 restructure lands.

---

*End of Extreme-Rigor Pass v1.0.0. The reframing claim as stated FAILS SC-1 on the §5.3 duplication check — the v10 tier schema is not a grouping structure. Recommended path: full dissolution per §5.4; variables replace tiers at the framework-specification level. Conditions at §8 pending author ratification. Optional macro-grouping design question (§5.5) preserved as Condition 6 side-question. Rerunnable after any methodology-work landing.*
