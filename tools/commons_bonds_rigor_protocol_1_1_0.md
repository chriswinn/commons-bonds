# Commons Bonds — Canonical Rigor Protocol

**Version:** 1.1.0
**Date:** 2026-04-20
**Status:** Canonical methodology. Upload at session start alongside relevant context files.
**Supersedes:** v1.0.0 (same date). Changes: Tier 3/Tier 6 transcription fix in §4.2; off-Earth/engineered-habitat exemplar added to Test 3 in §6; stress-test memo promoted to second worked example in §10.
**Absorbs:** Ten-critic content from `commons-bonds-rigor-testing-roles.html` (B2); rigor-test methodology from `commons-bonds-rigor-test.docx` (D3, pending conversion).
**References (not absorbed):** `eight-tier-v10.html` (AIT source), `commons-bonds-c5-two-path-rigor.md` (two-path source), `commons-bonds-success-criteria_11.html` (success criteria source), `commons_bonds_c6_decision_memo_2_0_0.html` (first worked example), `commons_bonds_layer_tier_stress_test_1_0_0.md` (second worked example).

---

## 1. Purpose

The Commons Bonds project has repeatedly produced high-stakes decisions (taxonomy reconciliation, architectural patches, tier definitions, stakeholder framings) where the applicable rigor test was re-derived session by session. In session v1.18.0 this failure mode became explicit: the C6 decision memo was produced in v1.0.0 using AIT + ten-critic but *without* the C5 two-path test, then had to be rerun as v2.0.0 when the user flagged the missing test. The rerun surfaced a decisive new finding (the Tier 8 absence in the older FGC taxonomy) that the original battery had not produced.

This protocol exists to prevent that failure mode. It consolidates every validated rigor test the project uses into a single modular methodology document that can be uploaded at the start of any session and applied consistently.

**Scope:** Any non-trivial claim in the Commons Bonds project — tier-level, architectural, stakeholder-facing, novelty/scholarly, or applied-policy.

**Non-scope:** Copy-editing, formatting decisions, session mechanics. These do not require rigor testing.

---

## 2. How to use this protocol

**At session start:**
Upload this file alongside the session handoff and any context files relevant to the claim under evaluation. The protocol is reference material; it is not modified during the session.

**When a claim arises:**
1. State the claim explicitly (a claim that cannot be stated precisely cannot be rigor-tested).
2. Classify using the routing rule in §3.
3. Run the applicable tests (§§4–8) in the order recommended in §9.
4. Document results in the fill-in template (§11).
5. Reference the test record in the session handoff.

**A failing test is a finding, not a veto.** The test makes a gap measurable. The response is either to refine the claim to close the gap, accept the gap as a known limitation with explicit handling, or reject the claim. All three are legitimate outcomes. What is illegitimate is silence — a claim shipped without the applicable tests run, or with tests that fail but are not documented.

---

## 3. Routing Rule

Not every decision needs every test. Classify first; route second. When multiple categories apply, union the tests.

| Claim type | Description | Apply |
|---|---|---|
| **Tier-level** | Is tier N real? Does this content belong in tier N or M? Does AIT hold for tier N? | AIT + two-path + multi-scale |
| **Architectural** | How should the framework organize its taxonomy, relationships, or structure? (C6 was architectural.) | Two-path + multi-scale + ten-critic + success criteria |
| **Stakeholder-facing** | Will this land with legislators, corporate leaders, academic audiences, tribal councils, or individual readers? (Op-eds, testimony, pitches, public speeches.) | Two-path + ten-critic with stakeholder sub-battery |
| **Novelty/scholarly** | Does this claim beat, extend, or supersede existing literature? Is the vocabulary citeable? | Ten-critic with Novelty Critic primary + success criteria |
| **Applied-policy** | Should this jurisdiction, firm, or council adopt a specific instrument based on the framework? | Two-path + ten-critic with governance sub-battery + success criteria |

**Example of unioning:** C6 was primarily architectural but had tier-level implications (Tier 8 finding). Applied tests: two-path + multi-scale + ten-critic + success criteria + AIT (corroborative for tier-level component).

**AIT is often corroborative rather than primary** for architectural and stakeholder claims, but it is *primary* for tier-level claims. When in doubt, run it.

---

## 4. Test 1 — AIT Falsifiability Gate

**Source:** `eight-tier-v10.html` (canonical AIT methodology).

**Core question:** Does this claim / tier / distinction survive abundance stripping?

**Rationale:** The Commons Bonds framework derives costs from scarcity structure. A proposed cost category that persists even under abundance is not scarcity-grounded and therefore not a framework-compatible cost. AIT falsifiability protects the framework from absorbing phenomenological or moral categories that masquerade as structural.

### 4.1 Procedure

1. Name the scarcity the claim depends on.
2. Imagine that scarcity inverted (abundance).
3. Ask: does the claim / tier / cost persist?
4. If the claim persists under abundance → it is not grounded in scarcity architecture → FAIL AIT.
5. If the claim evaporates under abundance → it is scarcity-grounded → PASS AIT.

### 4.2 Worked examples (from canonical usage)

| Candidate | Scarcity | Under abundance | Verdict |
|---|---|---|---|
| Tier 6 (Ecological Carrying Cost) | Ecosystem service abundance (pollination, hydrology, soil) | Services infinite → tier evaporates | PASS |
| Tier 3 (Dynastic Labor Cost) | Temporal separation between generations creating below-FGC compensation | No temporal separation → tier evaporates | PASS |
| Tier 8 (Political Capture) | Distributional conflict over scarce allocations | No conflict to capture → tier evaporates | PASS |
| "Existential/Meaning Cost" (older FGC tier) | None identifiable | Phenomenological struggles persist even with abundance | FAIL |
| "Immediate Survival Cost" (older FGC tier) | Same scarcity as Tier 1 | Redundant with Tier 1 | FAIL (redundancy variant) |

### 4.3 Verdict form

- **PASS** — scarcity-grounded; claim can proceed to subsequent tests.
- **FAIL** — not scarcity-grounded; claim is rejected or refactored.
- **CORROBORATIVE** — used alongside a primary test (two-path or ten-critic) as cross-check.

### 4.4 C6 application

Three of four non-mapping FGC tiers (Relationship/Family, Opportunity, Existential/Meaning) failed AIT. The fourth (Immediate Survival) was redundant with Tier 1. See `commons_bonds_c6_decision_memo_2_0_0.html` §8.

---

## 5. Test 2 — Two-Path Rigor

**Source:** `commons-bonds-c5-two-path-rigor.md` (C5 patch, 2026-04-20).

**Canonical statement (restated for reference):**

> The Commons Bonds rigor test operates on two paths. Path 1 (allocation symmetry) tests whether the claim correctly identifies who captures value and who bears cost, and whether that asymmetry is structural. Path 2 (shield absence) tests whether the claim correctly identifies the distance condition that prevents the asymmetry from being recognized or corrected. A claim that passes Path 1 but not Path 2 identifies a real harm but cannot explain why it persists. A claim that passes Path 2 but not Path 1 names a structural condition but cannot locate the cost. Rigor requires both paths.

**Default assumption:** All rigor tests in the Commons Bonds project default to the two-path structure per the C5 patch dated 2026-04-20.

### 5.1 Path 1 — Allocation Symmetry

For the claim under evaluation:

- **Who captures value?** (Identify explicitly — a person, role, firm, or class; not an abstraction.)
- **Who bears cost?** (Identify explicitly, at the same level of specificity.)
- **Is the asymmetry structural?** (Yes if derived from allocation architecture; no if reducible to individual moral failure, bad luck, or transient market condition.)
- **Is the tier assignment unambiguous?** (Ambiguous-by-design = FAIL. Example: parallel taxonomies that permit switch-arguing between tiers.)

**Verdict:** PASS / FAIL / CONDITIONAL (per scale if multi-scale applies).

### 5.2 Path 2 — Shield Absence

For the claim under evaluation:

- **What is the shield?** (The distance condition preventing recognition or correction. Types: epistemic, institutional, political, fiduciary, spatial, temporal. See C3 mechanism/shield architecture patch for canonical typology.)
- **Is the shield structural?** (Shield persists with full knowledge = structural.)
- **Does the claim correctly name the shield?** (Unnamed shields cannot be dissolved.)
- **Does the architecture of the claim itself create a new shield?** (Serious Path 2 failure. Example from C6: parallel taxonomies create a switch-arguing shield where claims are rescued by reassignment.)

**Verdict:** PASS / FAIL / CONDITIONAL.

### 5.3 Combined verdict

- Both paths PASS → claim passes two-path.
- Either path FAIL → claim fails two-path.
- Both CONDITIONAL → define the execution condition measurably (see §7.3 of C6 memo for the technique of converting soft worries into pass/fail gates).

### 5.4 C6 application

All four options (a / b / c / c-refined) were run through two-path at all four scales. Only (c-refined) passed both paths at every scale. See `commons_bonds_c6_decision_memo_2_0_0.html` §§3–4.

**Failure signature worth remembering:** Option (b) — parallel layers — failed Path 2 not because the shield was unnamed but because the architecture itself *created* a new shield (switch-arguing between taxonomies). This is the worst kind of Path 2 failure because the rigor test's own structure becomes the shield.

---

## 6. Test 3 — Multi-Scale Application

**Source:** User architectural requirement, ratified 2026-04-20:

> "This framework if done well should be useable for an individual considering a job/contract or even a career path. Just as much as it should be valuable for a community administrator on Mars, a Government managing a commons, or a corporation evaluating if they should be transitioning their revenue streams and/or their supply chain to something different."

**Operative constraint:** The framework's universality claim is an operative design requirement, not a theoretical flourish. A claim that serves one scale well but fails at another violates the universality claim.

### 6.1 The four scales × two environment types

Every scale is tested against at least one **Earth-baseline exemplar** and at least one **off-Earth / engineered-habitat exemplar**. Architectural and stakeholder claims that pass at one environment type but fail at the other do not satisfy the framework's universality claim. This two-axis structure was added in protocol v1.1.0 after the "Planetary" candidate name passed at Earth-individual scale in mid-session but failed at off-Earth-individual (asteroid-belt operations have no "planet" to be on). The lesson: Earth-only exemplars can mask off-Earth failure modes silently.

| Scale | Earth-baseline exemplar readers | Off-Earth / engineered-habitat exemplar readers | Core question |
|---|---|---|---|
| **Individual** | Worker evaluating a job offer; contractor evaluating a project; student evaluating a career path | Asteroid miner evaluating a long-duration contract; Mars-colony crew member; LEO-habitat maintenance technician; Lagrange-point logistics operator | Can this person identify whether they are personally bearing a tier of cost in their actual situation? |
| **Community** | Commons administrator; tribal council; municipal government; HOA or cooperative | Mars-colony administrator; orbital-habitat civic authority; lunar base council | Can this body identify where uncaptured cost is accumulating in the commons it manages? |
| **Government** | Legislature pricing externalities; sovereign wealth fund sizing a reserve; regulatory agency evaluating permits | Outer Space Treaty signatory regulator; planetary-body licensing authority; celestial-mining-jurisdiction oversight body | Can the state identify the regulatory/fiscal instrument that would price the tier, and the political shield preventing it? |
| **Corporate** | Board evaluating supply chain transition; CEO deciding a revenue pivot; sustainability officer pricing transition risk | Asteroid-mining firm evaluating a contract; orbital-services operator; off-Earth logistics corporation | Can the firm identify whether a product line, contract, or vendor captures value via unpriced cost, and what a transition costs? |

**On off-Earth speculation:** the off-Earth exemplars are used even where near-term feasibility is low. The framework's universality claim explicitly covers these cases (ratified scope language: "a community administrator on Mars"), and exercising it against engineered-habitat readers now surfaces issues that would otherwise only appear in real application, when recovery is expensive. Treat off-Earth exemplars as thought-experiment stress tests, not as predictions about near-term commercial activity.

### 6.2 Procedure

1. State the claim.
2. For each scale, name at least one Earth-baseline exemplar reader AND at least one off-Earth / engineered-habitat exemplar reader. (Naming forces concreteness.)
3. Run the applicable tests (usually two-path) at each scale × environment combination.
4. Document per-scale, per-environment verdicts.
5. Aggregate into the multi-scale usability matrix.

A claim that passes at all scales on Earth but fails at any scale off-Earth fails the universality claim. Do not silently drop off-Earth cases as "speculative" — if the claim is architectural (framework-level), both environment types are in scope by design.

### 6.3 Multi-scale usability matrix (template)

| Option / Claim | Individual (Earth) | Individual (off-Earth) | Community (Earth) | Community (off-Earth) | Government (Earth) | Government (off-Earth) | Corporate (Earth) | Corporate (off-Earth) | Overall |
|---|---|---|---|---|---|---|---|---|---|
| | | | | | | | | | |

For architectural claims where an eight-column matrix is impractical, the compressed form is acceptable:

| Option / Claim | Individual | Community | Government | Corporate | Off-Earth delta (where different) | Overall |
|---|---|---|---|---|---|---|
| | | | | | | |

The compressed form is used when Earth and off-Earth verdicts match at every scale; any scale where they differ must be expanded.

### 6.4 Failure handling

If a claim fails at any scale:
- Is the failure fixable within the claim? → refine and rerun.
- Is the failure fundamental? → reject the claim or scope it explicitly to the scales where it holds.
- Is the failure at a scale the framework does not claim to serve? → document the scoping and proceed.

**Do not silently drop scales.** A claim scoped to individual-only should say so; a claim that happens to fail at government scale but silently presents as universal is a framework integrity violation.

### 6.5 C6 application

The multi-scale matrix is the centerpiece of `commons_bonds_c6_decision_memo_2_0_0.html` §6. The Tier 8 finding surfaced specifically by running Path 2 at government scale: the older FGC taxonomy had no analog for Tier 8 (Political Capture) because FGC is phenomenological and political capture is institutional. This made options (b) and (c) unrepairable at government scale and gave the decision an independent decisive reason beyond anything AIT or ten-critic had produced. See §5 of that memo.

---

## 7. Test 4 — Ten-Critic Steelman Battery

**Source:** `commons-bonds-rigor-testing-roles.html` (B2) — 20-role roster. Validated subset in `eight-tier-v10.html`.

### 7.1 Standing battery (ten critics — always applied when this test routes)

| # | Critic | What they press on |
|---|---|---|
| 1 | Academic Economist | Coasean, Pigouvian, or market-internalization objections. Does the claim survive mainstream cost-externality theory? |
| 2 | Analytic Philosopher | Are the categories coherent? Is terminology doing real definitional work, or is it aesthetic? |
| 3 | AI Adversary | Can the claim be gamed, misread, or weaponized by a sophisticated optimizer? |
| 4 | Writerly Editor | Does the prose carry the argument? Is anything over-technical or under-specified? Does the reader have to take things on faith? |
| 5 | Future-Proofer | Will this claim survive in 20 years? Is it tied to a present-moment artifact (specific technology, political moment, regulatory regime)? |
| 6 | Novelty Critic | Is this genuinely new, or is it restating Polanyi / Ostrom / externality theory / a standing literature? |
| 7 | Falsifiability | What observation or argument would refute this claim? If none exists, the claim is unfalsifiable and fails. |
| 8 | Completeness | Does the claim cover its own scope? What does it exclude that it should include? Are there edge cases that break it? |
| 9 | Libertarian | Does the claim over-regulate? Does it assume illegitimate state authority or coercive intervention? |
| 10 | Leftist | Does the claim under-specify power asymmetries? Does it naturalize a contingent arrangement? Does it let capital off the hook? |

### 7.2 Optional extended battery (per Q5 two-tier structure)

The remaining ten critics from B2 are grouped into sub-batteries activated by claim type:

| Sub-battery | Activated by | Critics |
|---|---|---|
| **Stakeholder** | Stakeholder-facing claims (op-eds, testimony, pitches, public speeches) | Legislator · Corporate Executive · Commons Administrator · Individual Worker · Tribal Elder |
| **Methodological / scientific-standards** | Peer-review contexts, academic submissions, methods sections | Peer Reviewer · Replication Critic · Methodological Purist |
| **Meta** | Claims about the framework's own architecture or self-application | Meta-Critic · Self-Dissolution Critic |

**Reference:** see `commons-bonds-rigor-testing-roles.html` (B2) for the full 20-role roster and detailed role prompts. The extended battery is **additive**, not a replacement — the standing ten always run first.

### 7.3 Procedure

For each critic in the applicable battery:
1. Write the steelman objection (the critic's strongest version of the pushback, not a strawman).
2. Write the claim's best defense.
3. Score: **Accept** / **Reject** / **Execution-dependent**.
4. If execution-dependent, define the execution condition measurably (per §7 of C6 memo v2.0.0 — convert soft worries into pass/fail gates).
5. Record the scoreboard.

### 7.4 Verdict form

- **PASS** — clear majority Accept, zero or minor Reject.
- **FAIL** — clear majority Reject, or any single Reject on a critic whose objection is structural rather than cosmetic.
- **CONDITIONAL** — pass depends on execution-dependent critics. Conditional must be made measurable.

### 7.5 C6 application

(c-refined) scored 10 Accept / 0 Reject with 1 execution-dependent critic (manifestation paragraph thinness). The execution-dependent verdict was converted into a measurable pass/fail gate in `commons_bonds_c6_decision_memo_2_0_0.html` §7. See §8 of that memo for the corroborative scoreboard.

---

## 8. Test 5 — Success Criteria Alignment

**Source:** `commons-bonds-success-criteria_11.html`.

### 8.1 The four realistic success criteria

| # | Criterion | Single-sentence test |
|---|---|---|
| 1 | Vocabulary portability | A labor lawyer uses "severed cost" (or equivalent canonical term) in a brief without explanation, 10 years out. |
| 2 | Individual applicability | A worker can identify whether they are bearing a tier of cost in their own situation without a PhD. |
| 3 | Community usability | A commons administrator (terrestrial or Martian) can price a transition reserve using the framework. |
| 4 | Next-gen scholarship | A graduate student 5–10 years out builds a thesis on a tier or on the broader framework. |

### 8.2 "When in doubt, trim" heuristic

If a proposed structure dilutes any of the four criteria, prefer the trimmed version. A simpler framework that travels beats a more sophisticated framework that does not.

### 8.3 Procedure

For each criterion:
1. Ask: does the claim serve it, dilute it, or have no effect?
2. A claim that serves ≥3/4 with neutral effect on the rest is passing.
3. A claim that dilutes any criterion must either be modified or must demonstrate net gain elsewhere that offsets the dilution. Document the trade explicitly.

### 8.4 Verdict form

- **PASS** — serves majority, neutral on the rest.
- **FAIL** — dilutes any criterion without offsetting gain.
- **CONDITIONAL** — serves some, dilutes others; trade-off requires author judgment.

### 8.5 C6 application

(c-refined) serves all four success criteria. The single-sentence benchmark specifically favored a single taxonomy with scale-specific manifestations over two co-canonical taxonomies — two taxonomies dilute the citation slot; one with prose texture at each scale is what travels. See `commons_bonds_c6_decision_memo_2_0_0.html` §9.

---

## 9. Application Protocol — sequencing and parallelism

### 9.1 Recommended sequence for architectural claims

1. Frame the claim explicitly.
2. Run **two-path** first (Paths 1 and 2 at all relevant scales).
3. Apply **multi-scale matrix**.
4. Run **AIT** as corroboration (especially for tier-level components of the architectural claim).
5. Run **ten-critic** as independent cross-check.
6. Confirm **success criteria** alignment.
7. Document findings in a decision memo using the template in §11.

### 9.2 Recommended sequence for tier-level claims

1. Frame the tier.
2. Run **AIT** first (is it scarcity-grounded?).
3. Run **two-path** (is there real allocation asymmetry and a real shield?).
4. Run **multi-scale** (does it work at all observer scales, or is it scale-locked?).
5. Document. Ten-critic and success criteria are optional for tier-level; apply when the tier is being proposed for the canonical decomposition or retired from it.

### 9.3 Recommended sequence for stakeholder-facing claims

1. Frame the claim and the target audience.
2. Run **two-path** (is the claim structurally correct at all?).
3. Run **ten-critic standing battery**.
4. Run **stakeholder sub-battery** (activates critics matching the target audience).
5. Document. Multi-scale and AIT are optional.

### 9.4 Parallelism is encouraged when tests are independent

Two-path and AIT cross-check each other rather than feeding each other — running them in parallel reduces confirmation bias. Ten-critic is independent of two-path. Success criteria is downstream of everything and should run last.

### 9.5 When tests disagree

Disagreement between tests is a finding, not a failure. A claim that passes AIT but fails two-path is not the same as a claim that passes both. Surface the disagreement in the decision memo; do not paper over it. The C6 v1.0.0 → v2.0.0 rerun is the object lesson: running only some of the applicable tests produced a recommendation that was technically defensible on the narrow battery but missed a decisive finding the full battery would have surfaced.

---

## 10. Worked Examples

### 10.1 First worked example — C6 Decision Memo v2.0.0

The C6 memo is the first complete application of this protocol. It evaluates four options (retire FGC / parallel layers / reconcile / collapse via manifestations) against the two-path test at four scales, with AIT + ten-critic + success criteria as corroborative cross-checks. Specific section mapping:

| Test | Section in C6 memo v2.0.0 |
|---|---|
| Two-path canonical form | §3 |
| Two-path applied to each option | §4 (four sub-sections) |
| Tier 8 finding — Path 2 failure at government scale | §5 |
| Multi-scale usability matrix | §6 |
| Execution gate (making conditional verdicts measurable) | §7 |
| AIT + ten-critic corroboration | §8 |
| Success criteria alignment | §9 |
| Implementation plan | §10 |

**Lesson from the v1.0.0 → v2.0.0 rerun:** The first memo applied AIT + ten-critic without the two-path test, because the C5 patch had not yet been integrated into a canonical methodology doc. The rerun with two-path surfaced a decisive new finding (the Tier 8 absence in the older FGC taxonomy) that the original battery had not produced. **This is the failure mode this protocol is designed to prevent.** Future claims run through the applicable battery from the start.

### 10.2 Second worked example — Layer and Tier Stress Test v1.0.0

`commons_bonds_layer_tier_stress_test_1_0_0.md` is the second complete application, conducted in session v1.19.0 after protocol v1.1.0's off-Earth exemplar addition was drafted. It applies the full protocol (architectural routing) to six remaining abundance layers and (tier-level routing) to all nine tiers of the v10 RCV decomposition. Specific test mapping:

| Test | Section in stress test memo |
|---|---|
| Protocol application per layer (AIT + two-path + multi-scale with off-Earth exemplar + abbreviated ten-critic + success criteria) | §3 (seven sub-sections, one per layer) |
| Layer summary table with verdicts and actions | §3.8 |
| Tier-level rigor (AIT + two-path + multi-scale) per tier | §4 (nine sub-sections, one per tier) |
| Tier summary table with verdicts and attribution updates | §4.10 |
| Aggregate findings and required file-level changes | §5 |
| Recommended next actions | §6 |

**Lesson from the stress test:** The off-Earth exemplar was added to Test 3 in v1.1.0 specifically because, mid-session, the "Planetary" candidate name for Atmospheric passed at Earth-individual scale but failed at off-Earth-individual (asteroid belt has no planet). Without the off-Earth exemplar, Planetary would have been ratified and the failure would only have surfaced during WS02/WS03 manifestation drafting for off-Earth tiers. **This is a second failure mode the protocol now guards against:** Earth-only exemplar readers silently approving claims that will fail at the environment types the framework claims to cover. Protocol v1.1.0 makes this exercise mandatory.

**Why reference both memos rather than embed them:** Both memos are large (~32k chars each) and live as separate files. Embedding would bloat the protocol and couple edits. The reference pattern keeps the protocol lean and allows the memos to evolve independently (e.g., as C6 ratifies into a patch, as the stress test produces C8 patch recommendations).

---

## 11. Fill-in template

Copy-paste into a new decision memo file named `commons_bonds_{topic}_{vN_N_N}.md` (or `.html` if math rendering is required). Replace all bracketed placeholders.

```markdown
# Commons Bonds — [Topic] Decision Memo

**Date:** YYYY-MM-DD
**Version:** X.Y.Z
**Supersedes:** [prior version or "none"]
**Protocol version applied:** commons_bonds_rigor_protocol_1.0.0

---

## Claim under evaluation

[One-paragraph precise statement. Name alternatives if they exist.]

## Routing classification

- **Claim type(s):** [tier-level / architectural / stakeholder-facing / novelty / applied-policy]
- **Tests to run:** [from routing rule, §3 of protocol]
- **Scales in scope:** [individual / community / government / corporate — check all that apply]

## Preliminary recommendation

[One sentence. Will be confirmed or modified by the tests below.]

---

## Test 1 — AIT (if applicable)

For each sub-claim or tier:
- **Scarcity:** [name]
- **Under abundance:** [persists / evaporates]
- **Verdict:** [PASS / FAIL / CORROBORATIVE]

## Test 2 — Two-Path

### Path 1 — Allocation Symmetry
- **Who captures value:** [explicit]
- **Who bears cost:** [explicit]
- **Structural?** [yes / no]
- **Tier assignment unambiguous?** [yes / no]
- **Verdict:** [PASS / FAIL / CONDITIONAL]

### Path 2 — Shield Absence
- **Shield type:** [epistemic / institutional / political / fiduciary / spatial / temporal / other]
- **Structural?** [yes / no]
- **Correctly named?** [yes / no]
- **Does architecture create a new shield?** [no / yes — specify]
- **Verdict:** [PASS / FAIL / CONDITIONAL]

## Test 3 — Multi-Scale

| Scale | Path 1 | Path 2 | Overall |
|---|---|---|---|
| Individual | | | |
| Community | | | |
| Government | | | |
| Corporate | | | |

[Narrative on scale-specific findings, especially any scale where the claim cannot be fixed within itself.]

## Test 4 — Ten-Critic

### Standing battery

| # | Critic | Objection (steelmanned) | Response | Verdict |
|---|---|---|---|---|
| 1 | Academic Economist | | | |
| 2 | Analytic Philosopher | | | |
| 3 | AI Adversary | | | |
| 4 | Writerly Editor | | | |
| 5 | Future-Proofer | | | |
| 6 | Novelty Critic | | | |
| 7 | Falsifiability | | | |
| 8 | Completeness | | | |
| 9 | Libertarian | | | |
| 10 | Leftist | | | |

**Scoreboard:** [N accept / M reject / K execution-dependent]

### Extended battery (if activated)

Sub-battery: [stakeholder / methodological / meta]

| # | Critic | Objection | Response | Verdict |
|---|---|---|---|---|

## Test 5 — Success Criteria

| Criterion | Effect | Notes |
|---|---|---|
| Vocabulary portability | [serves / dilutes / neutral] | |
| Individual applicability | [serves / dilutes / neutral] | |
| Community usability | [serves / dilutes / neutral] | |
| Next-gen scholarship | [serves / dilutes / neutral] | |

## Findings summary

[Aggregate matrix. Highlight any decisive finding (a test whose result is sufficient on its own to determine the recommendation).]

## Recommendation (confirmed)

[Final recommendation. Reasoning sharpened by the tests above.]

## Implementation plan (if applicable)

[File-level actions. Completion criteria. Queue position relative to other pending patches.]

## Open questions / execution gates

[Any CONDITIONAL verdicts converted to measurable pass/fail gates. Any issues deferred to a later session.]
```

---

## 12. Versioning and maintenance

### 12.1 Current version

**1.0.0** (2026-04-20)

### 12.2 Upload pattern

Upload at session start alongside the current session handoff. Do not modify within-session.

### 12.3 When to revise

- A new rigor test is validated across multiple claims and becomes a standing test.
- A routing category needs expansion (a new claim type surfaces that does not fit the five in §3).
- The ten-critic battery needs modification (a critic is retired, added, or has its prompt refined).
- A worked example reveals a protocol gap (e.g., the C6 v1.0.0 → v2.0.0 rerun, which is exactly what motivated this protocol).

### 12.4 When not to revise

- A single decision memo fails. That failure is the finding, not a protocol problem.
- A test produces an unexpected verdict. Document and move on.
- Stylistic or formatting preferences change. Use the session handoff for those.

### 12.5 Version numbering

- **Patch (1.0.1, 1.0.2):** clarifications, typo fixes, worked-example additions.
- **Minor (1.1.0, 1.2.0):** new routing category, new sub-battery, additional worked example promoted to top-level reference.
- **Major (2.0.0):** structural change to the test battery itself (e.g., a sixth primary test added, or two-path restructured).

### 12.6 Change log

**v1.1.0 (2026-04-20):** Minor revision. (1) Test 3 (multi-scale) expanded: each scale now tested against at least one Earth-baseline exemplar AND one off-Earth / engineered-habitat exemplar. Rationale: the universality claim covers off-Earth contexts, and Earth-only exemplars silently approved the "Planetary" candidate name mid-session before off-Earth testing caught the failure. This was a protocol gap. (2) §4.2 AIT worked-examples table transcription fix: Tier 3 is Dynastic Labor Cost; Tier 6 is Ecological Carrying Cost. Prior version had Tier 3 listed with the Tier 6 content. (3) §10 expanded from "First Worked Example" to "Worked Examples" with the layer-and-tier stress test promoted to second canonical worked example. Protocol constitution unchanged; test battery unchanged; routing rule unchanged.

**v1.0.0 (2026-04-20):** Initial canonical protocol. Consolidates AIT + two-path + multi-scale + ten-critic + success criteria into a single modular methodology. Five-route routing rule (tier-level · architectural · stakeholder-facing · novelty · applied-policy). Two-tier critic battery (standing 10 + optional extended sub-batteries: stakeholder · methodological · meta). Fill-in template. `commons_bonds_c6_decision_memo_2_0_0.html` referenced as first complete worked example. Supersedes no prior canonical version.

---

*End of Commons Bonds Canonical Rigor Protocol v1.1.0.*
