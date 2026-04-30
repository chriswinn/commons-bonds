# Commons Bonds — Phase 2 Deeper-Dive Rigor Pass: Theorem E.2 (Convergence of Independent Models) — Academic-Rigor Categorization Audit

**Version:** 1.0.0
**Date:** 2026-04-29
**Protocol applied:** `tools/commons_bonds_rigor_protocol_v2.3.0.md` — academic-rigor depth audit per author direction 2026-04-29: *"the math formulas and proofs have to stand up to academic rigor or I don't have a book."* Tests applied: premise enumeration; logical derivation (does the proof sketch actually derive convergence?); edge case analysis; collision check against established multi-method-convergence + meta-analysis + diversity-of-models literature; citation discipline; falsifiability; domain of applicability; counterexample resistance; **categorization decision** (theorem vs empirical observation vs formal robustness theorem).

**Author direction triggering this pass (2026-04-29 by Chris Winn):** *"Would it be possible for you to work on the other P2#3 items outside of P2#3.1 that is currently still running... Like e.g. 'Theorem E.2 Convergence of Independent Models'"* — sibling theorem-rigor session is running E.1 audit (~3 hours in at time of this pass start); reverse-priority Phase 2 sweep complete (Insights #47 + #48 + #49 + #50 ratified; P2#8 [Q(t)] [PROPOSED]); E.2 picked as parallel work because lightest of remaining theorems per E.4 rigor pass §16.3 estimate (~400-600 lines depending on Option A vs B).

**Scope:** Phase 2 academic-rigor depth audit on **Theorem E.2 (Convergence of Independent Models)** as stated at [Tech Appendix v1.0.0 §10 lines 3261-3267](core/technical-appendix/TechnicalAppendix_v1.0.0.html). The audit's load-bearing decision per E.4 rigor pass §16.3: **categorization** — Option A (relabel as empirical observation) vs Option B (restructure as formal robustness theorem).

**Status:** **RATIFIED 2026-04-29 by Chris Winn — verdict (a) Full ratify Option A (relabel as Empirical Observation E.2 (Cross-Model Convergence))** with three concrete repair enhancements per §14. Tech Appendix HTML edit timing pending author choice on §16 Q7 (same open question as Insights #35 + #38 + #40 + #47 + #48 + #49 + #50). Insight #51 closed-ratified entry added to `alignment/commons_bonds_open_insights_v1.0.0.md`.

**Author:** Chris Winn

**Recommended verdict (preview):** **OPTION A (relabel as empirical observation)** with three concrete repair enhancements. The current E.2 statement + proof are honestly an **empirical-evidence finding**, not a derivable theorem: the proof sketch invokes case-evidence + uncorrelated-data-sources reasoning rather than premise-derivation. Forcing E.2 into the theorem mold creates a structural inconsistency between its claim form (statistical regularity across N cases) and its proof form (probabilistic-evidence reasoning) that academic peer review will flag.

Three concrete repair enhancements: (1) **relabel** to "Empirical Observation E.2 (Cross-Model Convergence)" — preserves E.2 numbering for cross-reference continuity; (2) **case-count consistency fix** — current text has internal contradiction ("six tested cases" vs "all four empirical cases" in same paragraph); resolve to single canonical case count + clarify which cases are empirical vs thought-experiment-tested; (3) **independence-defense reformulation** — make the Model Independence Defense (currently at Tech Appendix §D Section VIII) the explicit foundation of E.2's empirical-observation status rather than a separable section.

Option B (restructure as formal robustness theorem) considered + rejected: would require independence assumptions on the three estimators' biases + probabilistic-convergence framework + coverage assumption + sample-size analysis — substantial scaffolding for marginal payoff over Option A's honesty-in-claiming framing. Option C (hybrid: keep "Theorem E.2" numbering but clarify proof status) considered + rejected: title-only fix preserves the structural-inconsistency surface that academic peer review flags.

The framework's load-bearing claim survives the relabel: **multi-method convergence as evidence of structural-correctness** is preserved at the empirical-observation level; the framework loses no analytical leverage. The relabel honors academic-rigor honesty without abandoning the substance.

---

## §1. Phase 2 executive summary

### §1.1 What was tested

E.2 currently states (Tech Appendix v1.0.0 line 3264):

> *Theorem E.2 (Convergence of Independent Models)*
>
> Under reasonable parameter assumptions, the Damage Function approach, Real Options approach, and RCV model converge to the same order of magnitude for IPG across tested cases.

With proof sketch (line 3267):

> *Proof sketch:* All three models capture the same fundamental gap: the difference between current pricing and full social cost. They differ in how they approach that gap — from identified costs (Damage Function), from market-referenced option value (Real Options), and from substitutability-weighted integral (RCV). Because their data sources are uncorrelated (litigation records, market volatility, materials science substitutability estimates) and because they share a common target (the true social cost), systematic divergence beyond one order of magnitude would require all three to err in opposite directions simultaneously — a probability inconsistent with their demonstrated empirical behavior across six tested cases. Convergence within one order of magnitude across all four empirical cases validates the underlying cost severance structure. ∎

The audit tests:
1. **Premise enumeration** — what assumptions does the proof rely on?
2. **Logical derivation** — does the proof sketch actually derive convergence?
3. **Edge case analysis** — what would falsify the convergence claim?
4. **Collision check** — does this collide with established multi-method-convergence / meta-analysis / diversity-of-models literature?
5. **Citation discipline** — load-bearing references?
6. **Falsifiability** — under what conditions does the claim fail?
7. **Domain of applicability** — where does it apply?
8. **Counterexample resistance** — can a critic construct counterexamples?
9. **Categorization decision** — Option A (empirical observation) vs Option B (formal robustness theorem) vs Option C (hybrid)?

### §1.2 Phase 2 outcomes

| Test | Verdict | Note |
|---|---|---|
| Premise enumeration | **WEAK** | Three implicit premises (independence of data sources; common target; uncorrelated bias structure); none stated as numbered assumptions |
| Logical derivation | **FAIL (as theorem)** | Proof is empirical-evidence reasoning + probabilistic-implausibility argument, not derivation from premises. Academic peer review reads this as "evidence-based convergence finding," not "theorem" |
| Edge cases | **WEAK** | If all three models share systematic bias (e.g., all use similar discount-rate framework), independence-defense fails. Currently not tested or scoped |
| Collision check | **WEAK** | Hong-Page 2004 *PNAS* diversity-of-predictors theorem; Mosteller-Tukey 1977 multiple-estimator convergence; Cochrane meta-analysis discipline; not invoked or cited |
| Citation discipline | **WEAK** | No formal citations in the proof; "Model Independence Defense" referenced informally to "Ripple Effects 2.0, Section VIII" |
| Falsifiability | **STRONG** | More cases could produce divergence; explicit empirical falsifiability |
| Domain of applicability | **ADEQUATE** | IPG estimation across tested case landscape; not scoped beyond |
| Counterexample resistance | **WEAK** | Critic can construct hypothetical case where Damage Function = floor + Real Options = market-volatility-anchored + RCV = high-Weitzman-discount = systematic bias in same direction → divergence within tolerance illusory |
| **Internal-text consistency** | **FAIL** | "Six tested cases" vs "all four empirical cases" in same paragraph — internal contradiction needing resolution |

**Aggregate verdict: OPTION A (relabel as empirical observation) — recommended.**

The current "theorem" framing creates structural inconsistencies that academic peer review will flag. The substance survives the relabel: the multi-method convergence finding is genuinely informative as an empirical observation supported by the Model Independence Defense. The relabel honors academic-rigor honesty.

### §1.3 Three concrete repair enhancements (under Option A)

**ENHANCEMENT 1: Relabel from "Theorem E.2" to "Empirical Observation E.2 (Cross-Model Convergence)"**

Preserves E.2 numbering for cross-reference continuity (the framework already has 7+ Tech Appendix + chapter cross-references to "Theorem E.2" / "Convergence Theorem"); changes the categorization to honor the proof's actual structure. Recommended replacement:

> **Empirical Observation E.2 (Cross-Model Convergence).** Across the framework's tested calibration cases, the Damage Function approach, Real Options approach, and RCV model produce IPG estimates within one order of magnitude. This empirical regularity is consistent with the underlying cost severance structure being approximately characterized by all three approaches.

The "Theorem" label is dropped; the "Convergence of Independent Models" subtitle becomes "Cross-Model Convergence" (cleaner; "Independent Models" suggests probabilistic-independence which is not formally established).

**ENHANCEMENT 2: Case-count consistency fix**

Current text has internal contradiction in same paragraph:
- "demonstrated empirical behavior across **six tested cases**"
- "Convergence within one order of magnitude across **all four empirical cases**"

Resolve to single canonical case count. The Tech Appendix table at line 3234 references "All four cases produce IPG ≫ 1 across all three models" — suggesting **4 empirical cases** is the canonical count. The "6 tested cases" reference (also at line 3048 Model Independence Defense) likely includes 2 thought-experiment cases (asteroid + lunar from Ch 7) that don't appear in the §11 calibration table.

Recommended language:

> *"Convergence within one order of magnitude across the four empirical-calibration cases (McDowell coal; Norway oil; Deepwater Horizon; Libby vermiculite) plus two thought-experiment scenarios (asteroid mining; lunar regolith — see §F) — six tested cases total."*

This resolves the contradiction (clarifies 4 empirical + 2 thought-experiment = 6 total tested) while preserving the data substance.

**ENHANCEMENT 3: Independence-defense reformulation**

The Model Independence Defense (currently at Tech Appendix §D Section VIII line 3048) carries the weight of E.2's empirical-observation claim but is currently a separable section. Recommended: make it the explicit foundation of E.2's empirical-observation status by:

(a) Moving the load-bearing independence-defense paragraph (line 3048's "uncorrelated error modes" argument) into E.2's body as the foundation of the empirical-observation;
(b) Adding citation to **Hong & Page 2004 *PNAS* "Groups of diverse problem solvers can outperform groups of high-ability problem solvers"** as the academic anchor for diversity-of-models convergence reasoning;
(c) Adding a **failure-mode acknowledgment**: "the empirical regularity may break if all three approaches share systematic bias (e.g., all rely on similar discount-rate framework, similar substitutability assumptions, or similar litigation-data-bias structure). Future case additions or empirical recalibration may surface such failure modes."

The reformulation makes E.2 academically defensible as an empirical observation with explicit failure modes, rather than a "theorem" whose proof is empirical-evidence reasoning.

### §1.4 Why Option A (not B or C)

**Option B (restructure as formal robustness theorem) — REJECTED.**

A formal robustness theorem would require:
- **Independence assumption:** explicit probabilistic independence of the three estimators' biases. (Currently: claimed informally; not formally established.)
- **Common-target convergence:** probabilistic statement that with N → ∞ samples, the three estimators converge to common target. (Currently: not invoked.)
- **Coverage assumption:** the three approaches together span the relevant cost-classes. (Currently: implicit.)
- **Sample-size analysis:** how many cases are needed for the convergence claim to hold with probability p? (Currently: not addressed.)

These would constitute substantial new scaffolding. The payoff over Option A: marginal — academic peer review would still ask "is the independence assumption empirically justified?" Option A acknowledges the empirical-observation nature directly and produces the same epistemic claim with less formal apparatus.

**Option C (hybrid: keep "Theorem E.2" numbering with title-only fix) — REJECTED.**

Title-only fix (e.g., "Theorem E.2 (Empirical Robustness Result)") leaves the structural inconsistency between "Theorem" framing and empirical-evidence proof unfixed. Academic peer review would still flag the mismatch. The label change isn't substantively-meaningful unless paired with proof-restructure (which moves toward Option B); proof-restructure without categorization-honesty (Option A) is half-measures.

**Option A wins on three criteria:**
1. **Honesty** — categorizes E.2 by what its proof actually is.
2. **Minimal scope** — relabel + case-count fix + reformulation = ~150 words; no new theoretical apparatus.
3. **Cross-reference continuity** — E.2 numbering preserved.

### §1.5 What changes vs what doesn't

**What changes:**
- "Theorem E.2 (Convergence of Independent Models)" → "Empirical Observation E.2 (Cross-Model Convergence)"
- Proof reformulation acknowledging empirical-evidence basis
- Case-count consistency fix
- Independence-defense citation anchor

**What does NOT change:**
- The substantive convergence finding (multiple methods converge across tested cases)
- The framework's broader Three Ways of Counting + RCV + Damage Function + Real Options three-model architecture
- Cross-references in chapter prose / case studies (continue to refer to "E.2" by number)
- The Model Independence Defense substance (only its placement + citation discipline change)
- Any other theorem in the E.1-E.5 set

The framework's load-bearing claim about cross-model convergence is preserved; only the categorization changes.

---

## §2. Question + scope

### §2.1 Triggering articulation

[Phase 2 Theorem E.4 Integral Convergence rigor pass §16.3 + author direction 2026-04-29](commons_bonds_rigor_pass_2026-04-29_phase2_theorem_e4_integral_convergence_v1.0.0.md):

> *"E.2 (Convergence of Independent Models) ~400-600 lines depending on Option A vs B (categorization decision: relabel as empirical observation OR restructure as formal robustness theorem)"*
>
> *"sequence Claude-decided as **E.4 → E.1 → E.3 → E.5 → E.2** (lightest first as proof-of-concept; framework-central second; bigger lift third; scope-tightening fourth; categorization decision last)"*

Phase 2 (this rigor pass) executes the categorization decision audit. Scheduled out-of-sequence (sibling session running E.1 in parallel; E.2 picked as available work given lighter scope).

### §2.2 What this audit produces

For pass/fail academic-rigor gate at top-tier journals (AER, QJE, JPE, JEEM, JPubE, *Journal of Economic Methodology*) and academic-trade hybrid presses, E.2's categorization must meet the following standards:

- The claim's form (statistical regularity across tested cases) must match the proof's form (empirical-evidence reasoning OR formal derivation; not mismatched).
- Case-count + scope must be internally consistent.
- Independence-defense argument must be cited or formally established.
- Failure modes must be explicit (when does the convergence break?).

This audit produces:
1. Per-test verdict.
2. Categorization-decision rationale (Option A vs B vs C).
3. Concrete repair enhancements per recommendation.
4. Cross-references to multi-method-convergence / diversity-of-models literature.

### §2.3 Pass/fail gate framing

Per author direction 2026-04-29: pass/fail gate on academic-rigor for theorems. This audit applies the same standard to E.2's categorization that the Theorem E.4 audit (RATIFIED Insight #40) applied to proof-structure. Categorization that misrepresents what a proof proves (e.g., calling an empirical-evidence finding a "theorem") would not survive top-tier referee review.

### §2.4 What this pass does NOT cover

- **Phase 2 deeper-dive on theorems E.1, E.3, E.5** — separate rigor passes (sibling session in progress 2026-04-29 for E.1; E.3 + E.5 pending).
- **Theorem E.4 (Integral Convergence)** — already RATIFIED Insight #40.
- **Renewable Imperative theorem** — likely covered within E.5 audit per E.4 §16.3 sequencing.
- **Three Ways of Counting Method 1 / 2 / 3 sub-method audits** — separate methodology rigor passes (commit `1c8e4dd` Three Ways + RCV Formal-Model rigor pass + per-method individual passes).
- **Cross-model architecture audit (Damage Function + Real Options + RCV)** — Tech Appendix §D + §10 territory; this audit is on E.2 specifically, not the broader three-model architecture.
- **Case-list completeness audit** — separate concern; this audit identifies the case-count contradiction but does not audit case-selection.
- **Pre-publication external review by economics PhD or formal-methods expert** — Insight #39 OPEN; downstream gate.

---

## §3. Methodology

### §3.1 Academic-rigor depth audit framework

For each test below, the audit (a) reads E.2's current statement + proof + adjacent Tech Appendix context (§D Three Models + §10 Theorems + §11 Calibration Cases); (b) tests against academic-peer-review standards; (c) produces verdict; (d) flags concrete repair work.

### §3.2 Tests applied

1. **Premise enumeration** — implicit premises identified and assessed.
2. **Logical derivation** — does the proof sketch derive convergence from premises, or invoke empirical evidence?
3. **Edge case analysis** — what conditions break the convergence claim?
4. **Collision check** — adjacent multi-method-convergence + meta-analysis + diversity-of-models literature.
5. **Citation discipline** — load-bearing references.
6. **Falsifiability** — explicit conditions for falsification.
7. **Domain of applicability** — where applies; where not.
8. **Counterexample resistance** — try constructing counterexample under stated premises.
9. **Categorization decision** — Option A vs B vs C analysis.

### §3.3 What the audit does NOT do

- Does NOT verify the empirical convergence claim across additional cases (Block 4 numerical territory).
- Does NOT redesign the three-model architecture (Damage Function + Real Options + RCV).
- Does NOT replace pre-publication external review.

---

## §4. Current state — close reading

### §4.1 Current text (Tech Appendix v1.0.0 lines 3261-3267, verbatim)

> **Theorem E.2 (Convergence of Independent Models)**
>
> Under reasonable parameter assumptions, the Damage Function approach, Real Options approach, and RCV model converge to the same order of magnitude for IPG across tested cases.
>
> *Proof sketch:* All three models capture the same fundamental gap: the difference between current pricing and full social cost. They differ in how they approach that gap — from identified costs (Damage Function), from market-referenced option value (Real Options), and from substitutability-weighted integral (RCV). Because their data sources are uncorrelated (litigation records, market volatility, materials science substitutability estimates) and because they share a common target (the true social cost), systematic divergence beyond one order of magnitude would require all three to err in opposite directions simultaneously — a probability inconsistent with their demonstrated empirical behavior across **six tested cases**. Convergence within one order of magnitude across **all four empirical cases** validates the underlying cost severance structure. ∎

### §4.2 Adjacent context — Tech Appendix §D Three Models (lines 3038-3050)

- Line 3038: "Damage Function (bottom-up): Audit all identifiable costs tier by tier."
- Line 3041: "Real Options (market-referenced): Price the social option value of keeping the resource in situ."
- Line 3048: **"Model Independence Defense (from Ripple Effects 2.0, Section VIII):** The sharpest attack on this three-model framework is that Real Options and RCV may share deep mathematical structure — both price irreversibility plus uncertainty. The defense: they package uncertainty differently. Real Options calibrates volatility from market data; RCV calibrates substitutability from engineering and materials science. These calibrations come from genuinely different data sources with uncorrelated error modes. A model that overestimates S(t) (substitutability) does not necessarily overestimate market volatility, and vice versa. The convergence therefore cannot be explained by shared error structure. The Damage Function uses a third, entirely separate data source: documented litigation outcomes, epidemiological studies, and remediation cost estimates. All three sources are uncorrelated in the sense that matters for convergence: correlated measurement error would not consistently produce IPG estimates within one order of magnitude across **six tested cases**."

### §4.3 Adjacent context — Tech Appendix §11 calibration table (line 3234)

> "All four cases produce IPG ≫ 1 across all three models. The ranges overlap within one order of magnitude in every case, consistent with the Convergence Theorem (E.2)."

References **four cases**, consistent with calibration table at lines 3300+ (McDowell + Norway + Deepwater + Libby).

### §4.4 Initial reading observations

- **The proof is empirical-evidence reasoning, not derivation.** It argues: data sources uncorrelated + common target + 6 tested cases → divergence beyond 1 OOM is improbable. This is a **probabilistic-evidence argument**, not a derivation from premises. Academic peer review reads this as "convergence finding supported by case-count + independence reasoning," not "theorem."

- **Internal case-count contradiction.** "Six tested cases" + "all four empirical cases" in same paragraph. Likely resolution: 4 empirical (McDowell + Norway + Deepwater + Libby) + 2 thought-experiment (asteroid + lunar from Ch 7) = 6 total. The current text obscures the distinction, which an attentive reader will notice.

- **The Model Independence Defense is load-bearing.** The independence-of-data-sources claim is the central plausibility argument; without it, the convergence finding could be explained by shared bias structure. This argument is currently in §D as separate scaffolding rather than integrated into E.2's body.

- **No formal citations.** "Hong-Page 2004 *PNAS*" diversity-of-predictors result is the natural academic anchor for "diverse models converge to common target"; not cited. "Mosteller & Tukey 1977 *Data Analysis and Regression*" multiple-estimator convergence treatment is also relevant; not cited.

- **"Theorem" label is overclaiming.** A theorem is a derivable mathematical statement; this is an empirical-regularity finding. The label creates a categorization mismatch that referee review will flag.

- **The substance survives relabeling.** Cross-model convergence is genuinely informative as an empirical observation. The framework loses no analytical leverage by acknowledging the empirical-observation nature.

---

## §5. Test 1 — Premise enumeration

### §5.1 Implicit premises in current proof

1. **(Implicit)** The three approaches' data sources have uncorrelated error structures.
2. **(Implicit)** All three approaches target the same underlying social cost (common-target convergence).
3. **(Implicit)** The 6 tested cases are representative of the framework's intended case landscape.
4. **(Implicit)** Independence of bias structure (a stronger claim than uncorrelated data sources).
5. **(Implicit)** Sample size of 6 cases is sufficient for the convergence claim.

### §5.2 Verdict

**WEAK.** None of the five implicit premises is stated as a numbered assumption; none is formally established. Top-tier journals require explicit premise enumeration for theorems; current text would not pass peer review at this level.

### §5.3 Repair recommendation

For Option A (relabel as empirical observation): premises don't need numbered-assumption form (empirical observations are evidence-supported, not premise-derived). Repair is reformulation per Enhancement 3 §1.3 — explicit independence-defense + failure-mode acknowledgment.

For Option B (formal robustness theorem): would require Premises P1-P5 numbered enumeration with formal probabilistic statements + sample-size analysis. Heavier lift; rejected per §1.4.

---

## §6. Test 2 — Logical derivation

### §6.1 Current proof structure

The proof sketch:
1. States that all three models capture the same fundamental gap.
2. Asserts data-source independence (Damage Function: litigation records; Real Options: market volatility; RCV: substitutability estimates).
3. Argues that "systematic divergence beyond one order of magnitude would require all three to err in opposite directions simultaneously."
4. Concludes this is "a probability inconsistent with their demonstrated empirical behavior across six tested cases."

### §6.2 Is this a derivation?

**NO.** The argument structure is:
- (Step 1) Three approaches share common target.
- (Step 2) Data sources are uncorrelated.
- (Step 3) Therefore: divergence is improbable.
- (Step 4) Empirical evidence (6 cases) confirms convergence.

This is an **empirical-evidence-based argument**, not a derivation. Step 3 invokes probability informally (no probabilistic framework formalized); Step 4 invokes empirical evidence.

A theorem's proof would derive convergence from formal premises (e.g., "If estimators X, Y, Z have independent biases under measure μ, then by [formal theorem] their convergence-band probability is at least p"). E.2's proof does not have this structure.

### §6.3 Verdict

**FAIL (as theorem-derivation).** The proof is empirical-evidence reasoning, not derivation. This is the audit's load-bearing finding.

**STRONG (as empirical-observation argument).** As an empirical-observation supporting argument, the structure is sensible and matches what empirical-observation defenses look like. Categorization-correct framing produces a STRONG verdict; categorization-incorrect framing produces a FAIL verdict.

### §6.4 Repair recommendation

**Categorization correction (Option A).** Relabel as "Empirical Observation E.2 (Cross-Model Convergence)"; the proof structure becomes correctly categorized as empirical-observation supporting argument.

---

## §7. Test 3 — Edge case analysis

### §7.1 Edge case 1: shared systematic bias

If all three approaches share systematic bias in the same direction (e.g., all rely on similar discount-rate framework that underestimates long-horizon costs), the convergence finding could be illusory — the three approaches would converge but to a wrong target.

Currently not addressed in E.2 text. The Model Independence Defense argues against shared error structure but does not address shared systematic bias from common framework choices.

### §7.2 Edge case 2: small-sample regime

Convergence across 6 cases is suggestive but not statistically robust. With more cases, divergence patterns could emerge.

Currently not addressed.

### §7.3 Edge case 3: case-selection bias

The 6 tested cases are framework-author-selected (McDowell + Norway + Deepwater + Libby + 2 thought-experiments). If case-selection biases toward cases where convergence is expected, the empirical-observation overstates the framework's claim.

Currently not addressed.

### §7.4 Verdict

**WEAK.** Three plausible failure modes are unaddressed in the current text. The empirical-observation framing (Option A) makes addressing failure modes natural (empirical observations have explicit failure-mode acknowledgments); the theorem framing (status quo) treats them as "outside the proof scope" which is academic-rigor problematic.

### §7.5 Repair recommendation

Per Enhancement 3 §1.3 — failure-mode acknowledgment in reformulated empirical-observation: *"The empirical regularity may break if (a) all three approaches share systematic bias (e.g., similar discount-rate framework); (b) the case set is too small to surface failure modes; (c) case selection biases toward convergent cases."*

---

## §8. Test 4 — Collision check against established literature

### §8.1 Diversity-of-models literature

| Reference | Concept | Relevance to E.2 |
|---|---|---|
| **Hong & Page 2004 *PNAS*** "Groups of diverse problem solvers can outperform groups of high-ability problem solvers" | Diversity-of-predictors theorem — diverse models converge to better aggregate predictions than less-diverse ensembles | Direct anchor for E.2's "uncorrelated data sources" → "convergence to common target" reasoning |
| **Hong & Page 2001 *J Econ Theory*** "Problem solving by heterogeneous agents" | Earlier formalization | Adjacent |
| **Page 2007 *The Difference: How the Power of Diversity Creates Better Groups, Firms, Schools, and Societies*** | Popularization | Trade-press anchor |

### §8.2 Multiple-estimator convergence literature

| Reference | Concept | Relevance to E.2 |
|---|---|---|
| **Mosteller & Tukey 1977 *Data Analysis and Regression*** | Foundational treatment of multiple-estimator convergence + jackknife / bootstrap | Anchor for "estimator convergence" framing |
| **Efron 1979 *Ann Stat*** "Bootstrap methods" | Bootstrap convergence theory | Adjacent |
| **Stigler 1986 *The History of Statistics*** Ch 6 (combinations of observations) | Historical lineage of multi-method-convergence | Adjacent |

### §8.3 Meta-analysis literature

| Reference | Concept | Relevance to E.2 |
|---|---|---|
| **Cochrane Collaboration Handbook** | Meta-analysis discipline; pooled-estimator convergence | Adjacent (E.2 is not formal meta-analysis but invokes similar reasoning) |
| **Higgins & Thompson 2002** I² heterogeneity statistic | Quantifies cross-study heterogeneity | Adjacent |

### §8.4 Verdict

**WEAK.** None of the relevant adjacent literature is invoked or cited. Hong-Page 2004 *PNAS* is the natural academic anchor for diversity-of-models convergence reasoning; not currently cited.

### §8.5 Repair recommendation

Per Enhancement 3 §1.3 — add citation to Hong & Page 2004 *PNAS* in reformulated E.2 as the academic anchor for "uncorrelated data sources → convergence to common target" reasoning. Optional: cite Mosteller & Tukey 1977 for multiple-estimator convergence framing.

---

## §9. Test 5 — Citation discipline

### §9.1 Current state

No formal citations in E.2's proof. "Model Independence Defense" referenced informally to "Ripple Effects 2.0, Section VIII" (an internal framework document, not a published reference).

### §9.2 Verdict

**WEAK.** Top-tier journals require formal citations for load-bearing arguments. Hong & Page 2004 + Mosteller & Tukey 1977 are natural anchors; not invoked.

### §9.3 Repair recommendation

Per Enhancement 3 §1.3 — add Hong & Page 2004 *PNAS* + (optional) Mosteller & Tukey 1977. Ripple Effects 2.0 internal-document reference can remain (provenance-acknowledgment) but should be supplemented with academic anchors.

---

## §10. Test 6 — Falsifiability

### §10.1 Falsifiability conditions

- More cases (beyond the current 6) could produce divergence beyond 1 OOM.
- Failure modes per §7 (shared systematic bias; small sample; case-selection bias) could explain illusory convergence.
- Discovery that any of the three approaches has hidden correlation in error structure could undermine independence-defense.

### §10.2 Verdict

**STRONG.** Falsifiability conditions are clear in principle. The empirical-observation framing (Option A) makes them explicit; the theorem framing currently obscures them.

### §10.3 Repair recommendation

Failure-mode acknowledgment per Enhancement 3 §1.3 makes falsifiability conditions explicit in the reformulated text.

---

## §11. Test 7 — Domain of applicability

### §11.1 Current state

Implicit: the convergence finding applies to the framework's tested calibration cases (4 empirical + 2 thought-experiment per case-count consistency fix per Enhancement 2 §1.3). Outside this domain (e.g., new resource classes; new geographies; new extraction regimes), the claim is untested.

### §11.2 Verdict

**ADEQUATE.** Domain is implicit but reasonable; should be explicit in reformulated text.

### §11.3 Repair recommendation

Add scope statement to reformulated empirical-observation: *"This empirical regularity is observed across the framework's tested calibration case landscape (4 empirical + 2 thought-experiment cases). Generalization to additional resource classes / geographies / extraction regimes requires further empirical work (Block 4 numerical Monte Carlo + future case additions)."*

---

## §12. Test 8 — Counterexample resistance

### §12.1 Constructed counterexamples

**Counterexample 1: shared discount-rate framework bias.** All three approaches use Weitzman 2001 declining-discount-rate framework (per Tech Appendix §B Definition A.5). If this framework systematically biases long-horizon costs, all three approaches inherit the bias; convergence within 1 OOM does not validate accuracy.

**Counterexample 2: shared substitutability assumption.** Real Options + RCV both depend on substitutability estimates (S(t) function). Damage Function does not directly depend on S but inherits some substitutability assumptions through the framework's broader apparatus. Shared substitutability bias could explain convergence.

**Counterexample 3: small-sample illusion.** With only 6 cases, the empirical convergence finding is not statistically robust. Standard meta-analysis (Cochrane discipline) requires k ≥ 10-15 studies for robust convergence claims.

### §12.2 Verdict

**WEAK.** Three counterexamples constructible under stated premises. The Model Independence Defense addresses Counterexample 1 partially (argues against shared error structure) but does not fully address Counterexamples 2 + 3.

### §12.3 Repair recommendation

Per Enhancement 3 §1.3 — failure-mode acknowledgment + future-empirical-work pointer addresses Counterexamples 1 + 2 + 3 honestly within Option A's empirical-observation framing.

---

## §13. Categorization decision (Option A vs B vs C)

### §13.1 Option A — Relabel as Empirical Observation E.2

**Pros:**
- Honest about claim form (empirical regularity, not derivable theorem).
- Honest about proof form (empirical-evidence reasoning, not derivation).
- Minimal scope (~150 words).
- Cross-reference continuity (E.2 numbering preserved).
- Failure modes natural to articulate.
- Hong-Page 2004 + Model Independence Defense → empirical-observation foundation.

**Cons:**
- Loses "theorem" pedagogical force ("we have 5 theorems!").
- Asymmetry with E.1 / E.3 / E.4 / E.5 (which are derivable).

**Verdict: RECOMMENDED.**

### §13.2 Option B — Restructure as Formal Robustness Theorem

**Pros:**
- Preserves "theorem" pedagogical structure.
- Symmetry with E.1 / E.3 / E.4 / E.5.

**Cons:**
- Requires substantial new scaffolding (independence assumptions; probabilistic-convergence framework; coverage assumption; sample-size analysis).
- Marginal payoff: even with formal theorem, peer review will ask "is the independence assumption empirically justified?" — same epistemic position as Option A, with more apparatus.
- Heavy lift (~700-900 lines additional).

**Verdict: REJECTED.** Heavy lift, marginal payoff, same epistemic position as Option A.

### §13.3 Option C — Hybrid: Title-Only Fix

**Pros:**
- Preserves E.2 numbering.
- Modest scope.

**Cons:**
- Title-only fix without proof restructure leaves the categorization mismatch unfixed.
- Academic peer review reads "Theorem E.2 (Empirical Robustness Result)" as half-measures: the title acknowledges empirical-evidence nature but the framing as "Theorem" is preserved.
- Doesn't gain Option A's honesty-in-claiming benefit.

**Verdict: REJECTED.** Half-measures problem; doesn't fix the core issue.

### §13.4 Aggregate categorization recommendation

**Option A (relabel as Empirical Observation E.2 (Cross-Model Convergence)) — RECOMMENDED.**

The framework's E.1 / E.3 / E.4 / E.5 are derivable theorems with mathematical-derivation proofs. E.2 is a categorically different claim form — empirical regularity supported by case-evidence + independence reasoning. Honoring the categorization difference is academic-rigor-honest; Option A produces this with minimal scope.

---

## §14. Recommended formal restatement (under Option A)

### §14.1 Replacement text for Tech Appendix v1.0.0 §10 lines 3261-3267

**Current:**

> Theorem E.2 (Convergence of Independent Models)
>
> Under reasonable parameter assumptions, the Damage Function approach, Real Options approach, and RCV model converge to the same order of magnitude for IPG across tested cases.
>
> Proof sketch: All three models capture the same fundamental gap... [as currently written]

**Recommended replacement:**

> **Empirical Observation E.2 (Cross-Model Convergence).**
>
> Across the framework's tested calibration case landscape — four empirical cases (McDowell coal; Norway oil; Deepwater Horizon; Libby vermiculite) plus two thought-experiment scenarios (asteroid mining; lunar regolith — see §F): six cases total — the Damage Function approach, Real Options approach, and RCV model produce IPG estimates within one order of magnitude. This empirical regularity is consistent with the underlying cost severance structure being approximately characterized by all three approaches.
>
> *Supporting argument (per §D Model Independence Defense):* The three approaches use uncorrelated data sources — Damage Function from documented litigation outcomes + epidemiological studies + remediation cost estimates; Real Options from market volatility data; RCV from materials-science substitutability estimates. Under these data-source-independence conditions and a common target (true social cost), correlated measurement error would not consistently produce IPG estimates within one order of magnitude across the tested case landscape (cf. Hong & Page 2004 *PNAS* "Groups of diverse problem solvers can outperform groups of high-ability problem solvers"; Mosteller & Tukey 1977 *Data Analysis and Regression* on multiple-estimator convergence).
>
> *Failure modes (when the empirical regularity may break):* (a) the three approaches share systematic bias from common framework choices (e.g., similar discount-rate framework, similar substitutability assumptions); (b) the tested case landscape is too small to surface latent divergence patterns; (c) case selection biases toward cases where convergence is expected. Future empirical work (Block 4 numerical Monte Carlo + additional case calibrations) may surface failure modes.
>
> *Domain of applicability:* tested calibration case landscape per §11. Generalization to additional resource classes / geographies / extraction regimes requires further empirical work.

### §14.2 Cross-reference cleanup

Existing references to "Theorem E.2" / "Convergence Theorem (E.2)" / "the Convergence Theorem" appear in:
- Tech Appendix line 3234: *"consistent with the Convergence Theorem (E.2)"*
- Tech Appendix §D Section VIII (Model Independence Defense, line 3048).
- Possibly other chapter / case study cross-references.

Recommended cross-reference cleanup: replace "Theorem" with "Empirical Observation" in references; preserve "(E.2)" numbering. E.g.:
- Line 3234: *"consistent with the Cross-Model Convergence Empirical Observation (E.2)"* OR *"consistent with E.2 (Cross-Model Convergence)"*.

This is a sweep-style edit; can be batched with Tech Appendix HTML edit timing per the shared open question across Insights #35 + #38 + #40 + #47 + #48 + #49 + #50 + Phase 2 #8.

---

## §15. Verdict + ratification choices

### §15.1 Recommended verdict

**OPTION A (relabel as Empirical Observation E.2 (Cross-Model Convergence)) with three concrete repair enhancements per §14.** The substance survives the relabel; the framework loses no analytical leverage; academic-rigor honesty is gained.

Three concrete enhancements:

1. **Relabel + replacement text per §14.1** — "Theorem E.2 (Convergence of Independent Models)" → "Empirical Observation E.2 (Cross-Model Convergence)" with reformulated supporting argument + failure-mode acknowledgment + domain-of-applicability statement.

2. **Case-count consistency fix** — resolve "six tested cases" vs "all four empirical cases" contradiction per Enhancement 2 §1.3 (4 empirical + 2 thought-experiment = 6 total).

3. **Citation discipline upgrade** — add Hong & Page 2004 *PNAS* + (optional) Mosteller & Tukey 1977 *Data Analysis and Regression* as load-bearing references.

Plus: cross-reference cleanup per §14.2 — replace "Theorem" with "Empirical Observation" in cross-references; preserve E.2 numbering.

### §15.2 Pass-fail verdict on as-currently-written E.2

**WEAK** (under theorem framing). Categorization mismatch between claim form (empirical regularity) and proof form (empirical-evidence reasoning) would be flagged at academic peer review. Internal text inconsistency (case-count) compounds the issue.

### §15.3 Pass-fail verdict on enhanced E.2 per §14 (Option A)

**STRONG.** Empirical-observation framing matches the proof form; case-count resolved; failure modes explicit; falsifiability clear; citations anchored. Meets academic-peer-review standards for empirical-observation-class claims.

### §15.4 Author ratification choices

**(a) Full ratify Option A per §14** — relabel + reformulation + case-count fix + citation expansion. **Recommended.**

**(b) Ratify Option B (formal robustness theorem)** — substantial restructure (~700-900 lines additional); rejected per §13.2 but author override possible.

**(c) Ratify Option C (hybrid title-only fix)** — rejected per §13.3 but author override possible.

**(d) Partial ratify Option A** — adopt subset:
- (d.i) Relabel only — minimum viable fix; defer case-count + citation work.
- (d.ii) Relabel + case-count fix; defer citation expansion.
- (d.iii) Relabel + citation expansion; defer cross-reference sweep.

**(e) Modify verdict** — author specifies different recommendation.

**(f) Defer ratification** — additional questions before locking; bundle with sibling theorem rigor passes for combined ratification.

**(g) Reject** — author rejects audit findings; would require justifying why current "theorem" framing survives academic peer review without categorization correction.

**Recommendation: (a) Full ratify Option A.** Three enhancements are mutually-reinforcing; partial ratification leaves either the categorization mismatch (option d.i which doesn't go far enough), case-count contradiction (option d.ii), or citation gap (option d.iii) unfixed. Total scope: ~150 words replacement + 1-2 new bibliography entries + cross-reference sweep.

### §15.5 Implementation pending after ratification

If (a) full ratify Option A:
1. Tech Appendix v1.0.0 HTML §10 lines 3261-3267 — replace E.2 statement + proof per §14.1.
2. Tech Appendix v1.0.0 HTML §11 line 3234 — cross-reference cleanup (Theorem → Empirical Observation).
3. Tech Appendix v1.0.0 HTML §D Section VIII line 3048 — case-count "six tested cases" reconciled with §14.1 replacement (4 empirical + 2 thought-experiment).
4. Bibliography expansion — Hong & Page 2004 *PNAS*; (optional) Mosteller & Tukey 1977.
5. Other cross-references in chapter prose / case studies — sweep for "Theorem E.2" / "Convergence Theorem"; replace with "E.2" / "Cross-Model Convergence Empirical Observation."
6. terms_index — append Phase 2 verdict entry; cross-reference to this rigor pass.
7. Open Insights — new Insight # closed-ratified entry capturing Phase 2 #3.4 verdict (number TBD; coordinate with sibling theorem-rigor passes).

**Same open question as Insights #35 + #38 + #40 + #47 + #48 + #49 + #50 + Phase 2 #8 Tech Appendix HTML edit timing:** apply now to v1.0.0 vs batch into Phase 3 v2.0.0 rebuild. **Recommended:** unified batch into v2.0.0 rebuild.

### §15.6 Pre-publication external review (Insight #39)

This rigor pass produces Claude's assessment of E.2 categorization. Per Insight #39, eventual external review by economics PhD or formal-methods expert is warranted. For E.2 specifically, an empirical-economics reviewer should verify:
- The empirical-observation framing adequately characterizes the convergence finding's nature.
- The Hong-Page 2004 + Mosteller-Tukey 1977 citation set is appropriate vs. alternative anchors.
- The failure-mode acknowledgment covers the right set of failure modes (shared bias; small sample; case selection).
- The case-count resolution (4 empirical + 2 thought-experiment) matches the framework's intended claim.

---

## §16. Open questions for author discussion

1. **Categorization-decision confirmation.** §13 recommends Option A (relabel as empirical observation). Is there author preference for Option B (formal robustness theorem) despite the heavier scope? Or for Option C (hybrid title-only)?

2. **Numbering preservation.** §14.1 retains "(E.2)" numbering for cross-reference continuity. Alternative: full renumbering to "Observation O.1" or similar. Trade-off: numbering preservation maintains existing cross-references; renumbering signals categorization clearly. **Recommended: preserve E.2 numbering.**

3. **"Theorem" pedagogical accounting.** Under Option A, framework drops from "5 theorems" to "4 theorems + 1 empirical observation." Does this affect framework's external positioning (e.g., academic-trade hybrid press claim of "5 formal theorems")? **Recommended:** the honest claim is more defensible than the inflated claim; positioning should be "4 derivable theorems + 1 empirical observation supporting cross-model robustness."

4. **Cross-reference sweep scope.** §14.2 + §15.5 step 5 recommend chapter-prose + case-study cross-reference sweep. Author preference: sweep all cross-references at ratification time, OR defer sweep to chapter pre-submission review?

5. **Bibliography citation set.** §14.1 cites Hong & Page 2004 *PNAS* primarily; Mosteller & Tukey 1977 optionally. Author preference: include Mosteller & Tukey or keep tighter?

6. **Failure-mode acknowledgment depth.** §14.1 lists 3 failure modes (shared bias; small sample; case selection). Adequate scope, or should the framework be more specific about which framework-elements could produce shared bias (e.g., explicit Weitzman discount-rate cross-dependency)?

7. **Tech Appendix HTML edit timing.** Same open question as Insights #35 + #38 + #40 + #47 + #48 + #49 + #50 + Phase 2 #8: apply now to v1.0.0 vs batch into Phase 3 v2.0.0 rebuild?

8. **Coordination with E.1 sibling session.** Sibling theorem-rigor session is auditing E.1 (~3 hours in at this pass start). E.1's audit will likely produce restructure recommendations comparable to E.4's Insight #40. Should E.2's relabel be ratified before or after E.1's restructure to maintain coordinated theorem-set framing? **Recommended:** ratify independently; the categorization decision (Option A) doesn't depend on E.1's audit outcome.

---

## §17. Cross-references

### §17.1 Upstream rigor passes

- [Phase 2 Theorem E.4 Integral Convergence §16.3](commons_bonds_rigor_pass_2026-04-29_phase2_theorem_e4_integral_convergence_v1.0.0.md) — RATIFIED 2026-04-29 (Insight #40); methodology template; sequencing recommendation (E.4 → E.1 → E.3 → E.5 → E.2); E.2 categorization-decision flag.
- [Three Ways + RCV Formal Model rigor pass 2026-04-24](tools/rigor-passes/commons_bonds_rigor_pass_2026-04-24_three_ways_rcv_formal_model_v1.0.0.md) — RATIFIED 2026-04-24 commit `1c8e4dd`; cross-model architecture (Damage Function + Real Options + RCV) ratified.
- [Phase 2 Foreclosure Bond housing-crisis collision](tools/rigor-passes/commons_bonds_rigor_pass_2026-04-29_phase2_foreclosure_bond_housing_crisis_collision_v1.0.0.md) — RATIFIED 2026-04-29 (Insight #38); methodology template.
- [Phase 2 Cost Severance + Severed Cost Tier 2d](tools/rigor-passes/commons_bonds_rigor_pass_2026-04-29_phase2_cost_severance_severed_cost_tier2d_v1.0.0.md) — RATIFIED 2026-04-29 (Insight #35); methodology template.
- This session's reverse-priority Phase 2 sweep (P2#8 [Q(t)] [PROPOSED] + P2#7 [scarcity-multiplier] RATIFIED #47 + P2#6 [TWoC-adoption] RATIFIED #48 + P2#5 [ExtTail-collision] RATIFIED #49 + P2#4 [RCV-acronym] RATIFIED #50).

### §17.2 Sibling Phase 2 candidates (concurrent + remaining)

- **Phase 2 #3.1 Theorem E.1 Structural Cost Severance** — sibling session in progress 2026-04-29 (~3 hours in at this pass start; framework-central theorem; ~800-1000 lines estimated).
- **Phase 2 #3.2 Theorem E.3 Abundance Masking** — pending; circular proof; full formalization needed; ~700-900 lines estimated.
- **Phase 2 #3.3 Theorem E.5 Renewable Imperative** — pending; over-specified scope; scope-tightening + practical-corollary separation; ~700-900 lines estimated.
- **Phase 2 #8 [Q(t)] RCV integrand notation** — [PROPOSED] sibling Phase 2 audit (this session).

### §17.3 Downstream artifacts (this pass would update on ratification)

- `core/technical-appendix/TechnicalAppendix_v1.0.0.html` §10 lines 3261-3267 — replace E.2 statement + proof per §14.1.
- `core/technical-appendix/TechnicalAppendix_v1.0.0.html` §11 line 3234 + §D Section VIII line 3048 — cross-reference + case-count cleanup.
- `core/technical-appendix/TechnicalAppendix_v1.0.0.html` bibliography section — Hong & Page 2004 *PNAS* additions; (optional) Mosteller & Tukey 1977.
- Chapter prose + case study cross-references — sweep for "Theorem E.2" / "Convergence Theorem"; replace.
- `core/terms/terms_index.md` — append Phase 2 verdict entry; cross-reference to this rigor pass.
- `alignment/commons_bonds_open_insights_v1.0.0.md` — new Insight # closed-ratified capturing Phase 2 #3.4 verdict (number TBD).

### §17.4 Pre-publication external review (Insight #39)

This rigor pass + sibling Phase 2 deeper-dive passes (#8 + #3.1 + #3.2 + #3.3 + the four reverse-priority sweep audits) produce Claude's pre-external-review assessment substrate. Per Insight #39, eventual external review by economics PhD + empirical-economics methodologist is warranted. For E.2 specifically, the categorization decision (Option A vs B vs C) is the load-bearing review question; an empirical-economics reviewer should verify the Option A relabel adequately characterizes the convergence finding's nature.

---

**End of Phase 2 deeper-dive rigor pass v1.0.0 [PROPOSED — pending author ratification].**
