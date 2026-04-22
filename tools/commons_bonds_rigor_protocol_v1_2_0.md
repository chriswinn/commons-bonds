# Commons Bonds — Canonical Rigor Protocol

**Version:** 1.2.0
**Date:** 2026-04-21
**Status:** Proposed — awaiting ratification. Lineage-reconciliation revision.
**Supersedes:** v1.1.0 (2026-04-20) and v1.0.0 (2026-04-21 parallel-lineage artifact).
**Absorbs:** v1.0.0's expanded test catalog (Groups B/C/D/E/F), expanded character pressure suite (25 characters across Groups G–L), full-vs-light rigor axis, and formal revisitability section. Also ships the v1.21.0 drafted additions (merger gate, primitiveness gate, rejected-candidates-revisitable) as formal protocol content.
**Supersession notes:** v1.1.0's Test 5 (four realistic success criteria) is superseded by the newer success-criteria articulation in Group E (Goal-1 / Goal-2 / labor-lawyer-in-2039) that emerged in the v1.24.0 scope work. v1.1.0's ten-critic standing battery is mapped into the expanded 25-character roster; four unmapped critics are preserved as a Methodological Defense sub-battery.
**References (not absorbed):** `eight-tier-v10.html` (AIT source), `commons-bonds-c5-two-path-rigor.md` (two-path source), `commons-bonds-success-criteria_11.html` (earlier success criteria source), `commons_bonds_c6_decision_memo_2_0_0.html` (first worked example), `commons_bonds_layer_tier_stress_test_1_0_0.md` (second worked example), `commons_bonds_rigor_pass_2026-04-21_v1_0_0.md` (third worked example — v1.24.0 scope rigor passes), `c9_ait_canonical_positioning_patch.md` (AIT scaffolding-vs-load-bearing canonical).

---

## 1. Purpose

The Commons Bonds project has repeatedly produced high-stakes decisions (taxonomy reconciliation, architectural patches, tier definitions, stakeholder framings, scope boundaries) where the applicable rigor test was re-derived session by session. Two concrete failure modes motivate this protocol:

**Failure mode 1 (protocol-incompleteness):** In session v1.18.0, the C6 decision memo was produced in v1.0.0 using AIT + ten-critic but *without* the C5 two-path test, then had to be rerun as v2.0.0 when the missing test was flagged. The rerun surfaced a decisive new finding (the Tier 8 absence in the older FGC taxonomy) that the original battery had not produced.

**Failure mode 2 (lineage-drift):** In session v1.24.0, a new rigor protocol was produced and labeled v1.0.0 without awareness that v1.1.0 was already canonical. The new artifact introduced expanded coverage (25 tests, 25 characters) but silently dropped three canonical elements from v1.1.0: the AIT Falsifiability Gate, the Multi-scale × 2 environments requirement, and the procedural fill-in template. The v1.24.0 session also silently regressed the abundance-layer set from 10 (canonical per v1.21.0) to 7, which the three rigor passes then assumed.

This protocol (v1.2.0) exists to prevent both failure modes. It consolidates every validated rigor test the project uses — v1.1.0's procedural battery plus v1.0.0's expanded coverage — into a single modular methodology document that can be uploaded at the start of any session and applied consistently.

**Scope:** Any non-trivial claim in the Commons Bonds project — tier-level, architectural, stakeholder-facing, novelty/scholarly, applied-policy, or scope-level (including chapter-level structural changes, publishing-path decisions, success-criteria revisions).

**Non-scope:** Copy-editing, formatting decisions, session mechanics. These do not require rigor testing.

---

## 2. How to use this protocol

### 2.1 Session start

Upload this file alongside the session handoff and any context files relevant to the claim under evaluation. The protocol is reference material; it is not modified within a session. If the operating core (preferences) has been updated since the canonical protocol version, flag the delta before running tests.

### 2.2 When a claim arises

1. State the claim explicitly (a claim that cannot be stated precisely cannot be rigor-tested).
2. Select rigor depth using §3 (full vs. light).
3. Classify the claim type using the routing rule in §4.
4. Run the applicable tests (§§5–11) in the order recommended in §12.
5. Document results in the fill-in template (§14).
6. Reference the test record in the session handoff and, if substantial, in a rigor-pass record (pattern: `commons_bonds_rigor_pass_YYYY-MM-DD_v#_#_#.md`).

### 2.3 A failing test is a finding, not a veto

The test makes a gap measurable. The response is either to refine the claim to close the gap, accept the gap as a known limitation with explicit handling, or reject the claim. All three are legitimate outcomes. What is illegitimate is silence — a claim shipped without the applicable tests run, or with tests that fail but are not documented.

### 2.4 Rigor pass record pattern

Protocol (standing reference) and rigor pass record (historical audit) serve different purposes. The protocol defines what tests exist; the pass record documents what was tested on a specific date and what was found. Each substantial rigor pass produces its own pass-record document with the naming pattern above, building a traceable audit trail. This avoids both duplication (protocol bloating with session-specific findings) and disappearance (findings not captured anywhere).

---

## 3. Rigor depth — full vs. light

### 3.1 Full rigor

All applicable tests from the routing in §4, plus the full 25-character pressure suite (§10).

Required for:

- Scope decisions (book boundaries, chapter scope, deferrals)
- Architectural moves (new layers, new tiers, framework structural changes)
- AIT methodology changes (adding/removing abundance layers, inversion-test modifications)
- Publishing path decisions (cascade restructuring, venue changes)
- Success criteria revisions
- New layer candidates during naming cohorts
- Chapter-level structural changes (adding, removing, reordering chapters)
- Canonical decisions affecting Book One / Two / Three scope
- Any decision whose reversal would require rewriting already-drafted content

### 3.2 Light rigor

A subset of tests applied judgmentally. Always runs the three framework tests (§5.1, §5.2, §5.3 — AIT, two-path, merger+primitiveness gates). Additional tests run when obviously relevant. Character suite skipped unless a specific character's pressure area covers the decision.

Appropriate for:

- Within-chapter structural decisions after chapter scope is set
- Glossary additions where the concept is already established elsewhere in the book
- Naming decisions within established frameworks
- Citation and footnote decisions
- Prose-level revisions
- Counterargument wording within already-identified counterargument slots
- Integration edits applying already-ratified decisions

### 3.3 Default

When ambiguous, default to full. Drift from light to full is cheap (brief additional review). Drift the other way is expensive (re-argument of decisions that should have been ratified with more structure). Operating discipline: push harder so we only rewrite once.

---

## 4. Routing Rule

Not every decision needs every test. Classify first; route second. When multiple categories apply, union the tests.

| Claim type | Description | Apply |
|---|---|---|
| **Tier-level** | Is tier N real? Does this content belong in tier N or M? Does AIT hold for tier N? | AIT + two-path + multi-scale + merger/primitiveness gates |
| **Architectural** | How should the framework organize its taxonomy, relationships, or structure? (C6 was architectural.) | Two-path + multi-scale + character suite + success criteria + merger/primitiveness gates |
| **Scope-level** | Book boundaries, chapter scope, deferrals, publishing-path, success-criteria revisions. | Full test battery (Groups A–F) + full character suite |
| **Stakeholder-facing** | Will this land with legislators, corporate leaders, academic audiences, tribal councils, or individual readers? (Op-eds, testimony, pitches, public speeches.) | Two-path + character suite with stakeholder sub-battery |
| **Novelty / scholarly** | Does this claim beat, extend, or supersede existing literature? Is the vocabulary citeable? | Character suite with Novelty Critic primary + success criteria + decade-out durability |
| **Applied-policy** | Should this jurisdiction, firm, or council adopt a specific instrument based on the framework? | Two-path + character suite with governance sub-battery + success criteria |

**Example of unioning:** C6 was primarily architectural but had tier-level implications (Tier 8 finding). Applied tests: two-path + multi-scale + character suite + success criteria + AIT (corroborative for tier-level component).

**AIT is often corroborative rather than primary** for architectural and stakeholder claims, but it is *primary* for tier-level claims. When in doubt, run it.

---

## 5. Group A — Framework tests (canonical; always run on framework decisions)

### 5.1 Test 1 — AIT Falsifiability Gate

**Source:** `eight-tier-v10.html` (canonical AIT methodology); C9 patch §3 (scaffolding-vs-load-bearing canonical positioning).

**Core question:** Does this claim / tier / distinction survive abundance stripping?

**Rationale:** The Commons Bonds framework derives costs from scarcity structure. A proposed cost category that persists even under abundance is not scarcity-grounded and therefore not a framework-compatible cost. AIT falsifiability protects the framework from absorbing phenomenological or moral categories that masquerade as structural.

**Canonical positioning (C9 patch §3):** The Abundance Interference Taxonomy is the framework's epistemic core. Layers are organizational scaffolding, not load-bearing structure. Layer additions, mergers, or renames are organizational revisions, not framework-integrity events.

**Procedure:**

1. Name the scarcity the claim depends on.
2. Imagine that scarcity inverted (abundance).
3. Ask: does the claim / tier / cost persist?
4. If the claim persists under abundance → it is not grounded in scarcity architecture → **FAIL AIT**.
5. If the claim evaporates under abundance → it is scarcity-grounded → **PASS AIT**.

**Worked examples (from canonical usage):**

| Candidate | Scarcity | Under abundance | Verdict |
|---|---|---|---|
| Tier 6 (Ecological Carrying Cost) | Ecosystem service abundance (pollination, hydrology, soil) | Services infinite → tier evaporates | PASS |
| Tier 3 (Dynastic Labor Cost) | Temporal separation between generations creating below-FGC compensation | No temporal separation → tier evaporates | PASS |
| Tier 8 (Political Capture) | Distributional conflict over scarce allocations | No conflict to capture → tier evaporates | PASS |
| "Existential/Meaning Cost" (older FGC tier) | None identifiable | Phenomenological struggles persist even with abundance | FAIL |
| "Immediate Survival Cost" (older FGC tier) | Same scarcity as Tier 1 | Redundant with Tier 1 | FAIL (redundancy variant) |

**Verdict form:**

- **PASS** — scarcity-grounded; claim can proceed to subsequent tests.
- **FAIL** — not scarcity-grounded; claim is rejected or refactored.
- **CORROBORATIVE** — used alongside a primary test (two-path or character suite) as cross-check.

### 5.2 Test 2 — Two-Path Rigor

**Source:** `commons-bonds-c5-two-path-rigor.md` (C5 patch, 2026-04-20).

**Canonical statement:**

> The Commons Bonds rigor test operates on two paths. Path 1 (allocation symmetry) tests whether the claim correctly identifies who captures value and who bears cost, and whether that asymmetry is structural. Path 2 (shield absence) tests whether the claim correctly identifies the distance condition that prevents the asymmetry from being recognized or corrected. A claim that passes Path 1 but not Path 2 identifies a real harm but cannot explain why it persists. A claim that passes Path 2 but not Path 1 names a structural condition but cannot locate the cost. Rigor requires both paths.

**Default assumption:** All rigor tests in the Commons Bonds project default to the two-path structure per the C5 patch dated 2026-04-20.

**Path 1 — Allocation Symmetry:**

For the claim under evaluation:

- Who captures value? (Identify explicitly — a person, role, firm, or class; not an abstraction.)
- Who bears cost? (Identify explicitly, at the same level of specificity.)
- Is the asymmetry structural? (Yes if derived from allocation architecture; no if reducible to individual moral failure, bad luck, or transient market condition.)
- Is the tier assignment unambiguous? (Ambiguous-by-design = FAIL. Example: parallel taxonomies that permit switch-arguing between tiers.)

Verdict: PASS / FAIL / CONDITIONAL (per scale if multi-scale applies).

**Path 2 — Shield Absence:**

For the claim under evaluation:

- What is the shield? (The distance condition preventing recognition or correction. Types: epistemic, institutional, political, fiduciary, spatial, temporal. See C3 mechanism/shield architecture patch for canonical typology.)
- Is the shield structural? (Shield persists with full knowledge = structural.)
- Does the claim correctly name the shield? (Unnamed shields cannot be dissolved.)
- Does the architecture of the claim itself create a new shield? (Serious Path 2 failure. Example from C6: parallel taxonomies create a switch-arguing shield where claims are rescued by reassignment.)

Verdict: PASS / FAIL / CONDITIONAL.

**Combined verdict:**

- Both paths PASS → claim passes two-path.
- Either path FAIL → claim fails two-path.
- Both CONDITIONAL → define the execution condition measurably.

**Failure signature worth remembering:** The worst kind of Path 2 failure is when the architecture of the claim itself creates a new shield — e.g., parallel taxonomies that enable switch-arguing. In that case the rigor test's own structure becomes the shield.

### 5.3 Test 3 — Merger and Primitiveness Gates

**Source:** v1.21.0 drafted protocol additions (merger gate, primitiveness gate), formally shipped in this version.

Any proposed layer addition, split, merger, or rename must clear two gates before ratification.

**Merger gate (outward):**

Does the candidate substantially overlap with any existing layer such that they should be merged? Test by searching for bilateral independence cases — real-world instances where one is abundant and the other is scarce, in both directions. If independence cases don't exist in both directions, merger is indicated.

Example (from v1.21.0 Cohesion ratification): Cohesion vs. Demographic. Case A (Demographic abundance, Cohesion scarcity): Bowling Alone suburban US metros. Case B (Demographic scarcity, Cohesion abundance): small cohesive religious communities below specialist-sustaining threshold. Both directions confirmed → layers remain distinct.

**Primitiveness gate (inward):**

Does the candidate reduce to a composition of existing layers? Test by decomposing the candidate's revealed costs and checking whether each cost is already priced by an existing layer (or composition thereof). If all revealed costs decompose cleanly, the candidate is valid as a concept but redundant as a layer.

Example (from v1.21.0 Survivability rejection): Survivability's revealed costs decomposed cleanly into Tier 4 Foreclosure extended to civilization-scale timescales. Survivability was retained as a valid cross-layer concept but rejected as an independent layer.

**Combined verdict:**

A layer passes the distinctness gates when it clears AIT, passes both merger and primitiveness checks, and passes two-path and multi-scale. A candidate that fails either gate may still be useful as a cross-layer concept, manifestation-level framing, or tier-level attribution — but not as a standalone layer.

**Revisitability note:** Rejected candidates remain revisitable. A candidate concept that fails one framing may succeed under another as understanding of its underlying scarcity sharpens. Failure is a finding about the tested form, not a permanent verdict on the concept space. Re-test is warranted whenever new cases surface that existing layers don't price cleanly.

### 5.4 Test 4 — Multi-Scale × Two-Environments Application

**Source:** User architectural requirement, ratified 2026-04-20; off-Earth exemplar added in v1.1.0 after the "Planetary" naming failure.

**Operative constraint:** The framework's universality claim is an operative design requirement, not a theoretical flourish. A claim that serves one scale well but fails at another violates the universality claim. A claim that passes Earth-baseline at all scales but fails off-Earth fails the universality claim.

**The four scales × two environment types:**

Every scale is tested against at least one **Earth-baseline exemplar** and at least one **off-Earth / engineered-habitat exemplar**. Architectural and stakeholder claims that pass at one environment type but fail at the other do not satisfy the framework's universality claim.

| Scale | Earth-baseline exemplar readers | Off-Earth / engineered-habitat exemplar readers | Core question |
|---|---|---|---|
| **Individual** | Worker evaluating a job offer; contractor evaluating a project; student evaluating a career path | Asteroid miner evaluating a long-duration contract; Mars-colony crew member; LEO-habitat maintenance technician; Lagrange-point logistics operator | Can this person identify whether they are personally bearing a tier of cost in their actual situation? |
| **Community** | Commons administrator; tribal council; municipal government; HOA or cooperative | Mars-colony administrator; orbital-habitat civic authority; lunar base council | Can this body identify where uncaptured cost is accumulating in the commons it manages? |
| **Government** | Legislature pricing externalities; sovereign wealth fund sizing a reserve; regulatory agency evaluating permits | Outer Space Treaty signatory regulator; planetary-body licensing authority; celestial-mining-jurisdiction oversight body | Can the state identify the regulatory/fiscal instrument that would price the tier, and the political shield preventing it? |
| **Corporate** | Board evaluating supply chain transition; CEO deciding a revenue pivot; sustainability officer pricing transition risk | Asteroid-mining firm evaluating a contract; orbital-services operator; off-Earth logistics corporation | Can the firm identify whether a product line, contract, or vendor captures value via unpriced cost, and what a transition costs? |

**On off-Earth speculation:** Off-Earth exemplars are used even where near-term feasibility is low. The framework's universality claim explicitly covers these cases ("a community administrator on Mars"), and exercising it against engineered-habitat readers now surfaces issues that would otherwise only appear in real application when recovery is expensive. Treat off-Earth exemplars as thought-experiment stress tests, not as predictions.

**Procedure:**

1. State the claim.
2. For each scale, name at least one Earth-baseline exemplar reader AND at least one off-Earth / engineered-habitat exemplar reader.
3. Run the applicable tests (usually two-path) at each scale × environment combination.
4. Document per-scale, per-environment verdicts.
5. Aggregate into the multi-scale usability matrix.

**A claim that passes at all scales on Earth but fails at any scale off-Earth fails the universality claim.** Do not silently drop off-Earth cases as "speculative" — if the claim is architectural (framework-level), both environment types are in scope by design.

**Multi-scale usability matrix (template):**

| Option / Claim | Individual (Earth) | Individual (off-Earth) | Community (Earth) | Community (off-Earth) | Government (Earth) | Government (off-Earth) | Corporate (Earth) | Corporate (off-Earth) | Overall |
|---|---|---|---|---|---|---|---|---|---|
| | | | | | | | | | |

For architectural claims where an eight-column matrix is impractical, the compressed form is acceptable (compressed form used only when Earth and off-Earth verdicts match at every scale):

| Option / Claim | Individual | Community | Government | Corporate | Off-Earth delta (where different) | Overall |
|---|---|---|---|---|---|---|
| | | | | | | |

**Failure handling:**

If a claim fails at any scale:
- Is the failure fixable within the claim? → refine and rerun.
- Is the failure fundamental? → reject the claim or scope it explicitly to the scales where it holds.
- Is the failure at a scale the framework does not claim to serve? → document the scoping and proceed.

**Do not silently drop scales.** A claim scoped to individual-only should say so; a claim that happens to fail at government scale but silently presents as universal is a framework integrity violation.

---

## 6. Group B — Scope tests

Apply to scope-level claims, chapter-level structural changes, and decisions whose reversal would require rewriting drafted content.

6. **Trying-to-do-too-much.** Does this increase chapter or book load without proportionate utility increase? A scope expansion must earn its position against the displacement it causes.
7. **Cross-spectrum preservation.** Does this maintain the book's non-partisan framework positioning? Content that aligns with one political pole without independent framework grounding weakens the cross-spectrum claim.
8. **Load-bearing vs. scaffolding.** Is this structural (load-bearing) or organizational (scaffolding)? Scaffolding changes are cheap; load-bearing changes require higher bar. The AIT itself is load-bearing; abundance layers are scaffolding (C9 canonical).
9. **Displacement test.** What currently-planned content gets pushed out to make room for this? An addition without displacement is rare; most require something else to shrink or move.

---

## 7. Group C — Authorial / practical tests

Apply to decisions that change the author's exposure surface or operational constraints.

10. **Lone-author vulnerability.** How does this expose the author to targeted response from concentrated interests? A framework-level book by a lone author is structurally more vulnerable than an institutionally-affiliated author's equivalent work.
11. **Legal exposure.** Defamation, privacy, contract risk, NDA compatibility. Applies especially to CEO-era material, identifiable third parties, and policy claims about named actors.
12. **Cross-spectrum attack surface.** What attacks does this invite from any direction (left, right, industry, academic)? Different from Test 7 (cross-spectrum preservation) — this is the reception/attack dimension; Test 7 is the positioning dimension.
13. **Career-risk compatibility.** Nursing licensing exposure, professional-community exposure, identifiability through workplace or credentialing bodies.

---

## 8. Group D — Strategic / reception tests

Apply to decisions that affect publishing path, reception, or institutional placement.

14. **Publisher appeal.** Does this strengthen the publisher pitch? Publisher-appeal and framework-rigor can point in the same direction or opposite; when they diverge, rigor wins but the divergence must be named.
15. **Noema / Berggruen placement fit.** Does this align with the cascade's venue profiles? Noema favors cross-spectrum long-form with intellectual-platform fit; Berggruen favors long-horizon institutional thinking with methodological depth.
16. **Agent interest.** Commercial viability, media-appeal, pitch clarity.
17. **Target reader recognition.** Can the intended readers (labor lawyers, community organizers, graduate students, individual workers) pattern-match their situation to this content?
18. **Competitor / overlap.** Does substantively similar work already exist that would reduce this material's distinctiveness? The Harvey/Klein/Raworth compression test.
19. **Decade-out durability.** Will this still hold in 13+ years? The canonical success criterion is a 13+-year horizon; claims that depend on present-moment artifacts (specific technologies, political moments, regulatory regimes) need explicit durability handling.

---

## 9. Group E — Success criteria alignment

**Supersedes v1.1.0 Test 5.** The four realistic success criteria in v1.1.0 (vocabulary portability, individual applicability, community usability, next-gen scholarship) are superseded by the following tests, which tie to the specific goals and canonical sentence that emerged in the v1.24.0 scope work.

20. **Vocabulary portability.** Does this help book vocabulary travel (Harvey/Klein/Raworth compression test)? Can the framework's key terms be compressed into citable phrases?
21. **Upstream-of-Goal-1.** Does this strengthen the book's contribution to "future generations compensated more fairly"? Goal-1 is the framework-success goal; contribution is indirect (through vocabulary adoption and institutional uptake).
22. **Direct-to-Goal-2.** Does this strengthen the book's direct contribution to "people accept a job or project with open eyes and honest accounting"? Goal-2 is the individual-reader goal; contribution is direct (through individual-scale applicability).
23. **Labor-lawyer-in-2039 test.** Does this strengthen the canonical 13+-year success sentence — a labor lawyer using the vocabulary in a brief or open court without needing to explain it?

**"When in doubt, trim" heuristic (retained from v1.1.0):** If a proposed structure dilutes any of the four criteria, prefer the trimmed version. A simpler framework that travels beats a more sophisticated framework that does not.

**Verdict:** PASS (serves majority, neutral on the rest) / FAIL (dilutes any without offsetting gain) / CONDITIONAL (trade-off requires author judgment; document explicitly).

---

## 10. Group F — Content quality tests

Apply to any content claim, prose-level or framework-level.

24. **Counterargument coverage.** Are the counterarguments this material invites identified and addressed? Especially: are "memoir dressed as framework," "self-serving reframing," and "selective case selection" covered where applicable?
25. **Steelmannability.** Can the strongest critic engage with this, or does it rely on opponents being weaker than they would be?
26. **Falsifiability.** Can specific claims be tested — is there empirical work that could disconfirm them? Absorbs v1.1.0's AIT-adjacent falsifiability critic into a general test.
27. **Empirical grounding.** Is this documented, or asserted? Asserted claims in a framework book require either explicit scoping ("illustrative," "argued") or upgrade to documented.

---

## 11. The 25-character pressure suite

For full rigor, run the proposal past each imagined reader and identify what each would press on. Look for red flags from any single character. Look especially for flags from multiple characters on the same weakness — that's structural, not idiosyncratic.

### 11.1 Group G — Critics (attacking)

1. **Hostile coal-industry defender.** Attacks the coal case, the carbon-pricing implication, and any framing that reads as anti-fossil-fuel moralism. Typical pressure: "cheap energy lifted billions out of poverty," miner-dignity framing, claim-of-bias.
2. **Left critic ("reformed capitalism").** Attacks the framework as insufficiently radical, as soft-pedaling exploitation, as legitimizing extraction by reforming its accounting rather than ending it.
3. **Right critic ("anti-market").** Attacks the framework as hostile to markets, as regulation in disguise, as redistribution dressed as accounting.
4. **Journalist looking for hit-piece angle.** Looks for contradiction, self-serving framing, selective data, ad hominem opportunities.

### 11.2 Group H — Gatekeepers (evaluating)

5. **Noema editor.** Evaluates intellectual-platform fit, cross-spectrum reach, long-form coherence, originality of contribution.
6. **Berggruen Prize judge.** Evaluates long-term institutional thinking, methodological rigor, philosophical depth, lived-experience grounding.
7. **Publisher's legal counsel.** Evaluates defamation exposure, privacy risk, NDA compatibility, identifiability of third parties.
8. **Literary agent evaluating representation.** Evaluates commercial viability, media-pitch clarity, author-platform potential.
9. **Tenured economics chair.** Evaluates methodological rigor, mathematical grounding, empirical base, academic usability. (Maps to v1.1.0's Academic Economist.)

### 11.3 Group I — Intended users

10. **Labor lawyer in 2039.** The Group E canonical-sentence reader. Evaluates whether the vocabulary is usable in a brief without explanation.
11. **Community organizer.** Evaluates whether the framework gives language for negotiation without requiring demonization of the other side.
12. **Graduate student building on the work.** Evaluates citability, method-portability, extendability. (Absorbs v1.1.0's Novelty Critic to this extent.)
13. **Policy researcher at a think tank.** Evaluates applied-scholarship fit, connection to existing policy discourse.

### 11.4 Group J — Cultural readers

14. **Appalachian reader** (Ch. 2's implied audience). Evaluates whether the framework respects miner-dignity or subtly condescends.
15. **Young worker** (Ch. 1's implied audience). Evaluates whether the framework makes visible something they recognize.
16. **Fellow former IT consultant.** Evaluates authenticity of the knowledge-worker material.
17. **Ostrom successor scholar.** Evaluates compatibility with and extension of commons-governance literature.
18. **Harvey / Klein reader.** Evaluates vocabulary compression relative to "accumulation by dispossession" and "disaster capitalism."

### 11.5 Group K — Personal / proximal readers

19. **Family-member reader.** Evaluates accessibility to non-specialist. Tests whether complex ideas land for intelligent general readers.
20. **SGA constituent.** Evaluates coherence with the author's current public role.
21. **Nursing colleague.** Evaluates professional-context compatibility — does this enhance or conflict with nursing identity?
22. **MFA writing program critic.** Evaluates prose quality, register consistency, structural discipline of the writing itself. (Maps to and refines v1.1.0's Writerly Editor.)

### 11.6 Group L — Ethical and legacy tests

23. **Former subordinate from CEO days.** The anonymization pressure. Evaluates whether any specific person from the author's CEO history could identify themselves and either (a) feel analyzed without consent, (b) face professional exposure from the book, or (c) have legal claim. Requires specific mitigation protocols.
24. **Reader in 2040 looking back.** The durability test. Evaluates whether the book's specific references (companies, institutions, cases) will still make sense and hold up. (Maps to v1.1.0's Future-Proofer.)
25. **Personal legacy coherence — Chris's grandfather at NASA Langley.** Evaluates whether the book honors institutional integrity (the existence-proof side of the framework) as much as it names institutional failure. Tests that the framework is not purely critical — it recognizes what honest institutions can do.

### 11.7 Methodological Defense sub-battery (optional; absorbs v1.1.0 ten-critic remnants)

The four v1.1.0 critics not directly mapped above are preserved as a sub-battery activated for methodological-defense pressure.

M1. **Analytic Philosopher.** Are the categories coherent? Is terminology doing real definitional work, or is it aesthetic?
M2. **AI Adversary.** Can the claim be gamed, misread, or weaponized by a sophisticated optimizer?
M3. **Novelty Critic.** Is this genuinely new, or is it restating Polanyi / Ostrom / externality theory / a standing literature? (Overlaps with Character 12 grad student and Test 18 competitor/overlap; activate when either is insufficient.)
M4. **Completeness.** Does the claim cover its own scope? What does it exclude that it should include? Are there edge cases that break it?

### 11.8 Stakeholder sub-battery (optional; retained from v1.1.0)

Activated for stakeholder-facing claims (op-eds, testimony, pitches, public speeches).

S1. Legislator · S2. Corporate Executive · S3. Commons Administrator · S4. Individual Worker · S5. Tribal Elder.

### 11.9 Meta sub-battery (optional; retained from v1.1.0)

Activated for claims about the framework's own architecture or self-application.

X1. Meta-Critic · X2. Self-Dissolution Critic.

---

## 12. Applying the characters

For each character in a full rigor pass, briefly answer three questions:

1. What would this character press on?
2. What's the weakest point of the proposal from this character's perspective?
3. What mitigation exists, or is required before ratification?

**Red flag rules:**

- A single critical flag from any character warrants mitigation before ratification.
- Flags from multiple characters on the same weakness indicate the weakness is structural, not idiosyncratic, and require structural mitigation (not just tactical).
- Flags that require pre-drafting work (e.g., legal review, anonymization protocols, permissions) must be tracked separately as pre-drafting items and cannot be left to drafting-stage resolution.

**Character output format:**

A short paragraph per character (one to three sentences) identifying the pressure point, the strength of the pressure, and the mitigation. Full rigor passes may condense groups with no pressure detected into a single line ("Group K characters detected no structural pressure; flags recorded below").

---

## 13. Application Protocol — sequencing and parallelism

### 13.1 Recommended sequence for architectural claims

1. Frame the claim explicitly.
2. Run **two-path** (§5.2) first at all relevant scales.
3. Apply **multi-scale × 2 environments matrix** (§5.4).
4. Run **merger and primitiveness gates** (§5.3) if the claim proposes or modifies a layer.
5. Run **AIT** (§5.1) as corroboration (especially for tier-level components).
6. Run **character suite** (§11) as independent cross-check.
7. Confirm **success criteria** alignment (Group E, §9).
8. Run scope/authorial/strategic tests (Groups B/C/D, §§6–8) as applicable.
9. Run content-quality tests (Group F, §10).
10. Document findings using the template in §14.

### 13.2 Recommended sequence for tier-level claims

1. Frame the tier.
2. Run **AIT** first (is it scarcity-grounded?).
3. Run **two-path** (is there real allocation asymmetry and a real shield?).
4. Run **multi-scale × 2 environments** (does it work at all observer scales, or is it scale-locked?).
5. Run **merger and primitiveness gates** against adjacent layers.
6. Document. Character suite and success criteria are optional for tier-level; apply when the tier is being proposed for the canonical decomposition or retired from it.

### 13.3 Recommended sequence for stakeholder-facing claims

1. Frame the claim and the target audience.
2. Run **two-path** (is the claim structurally correct at all?).
3. Run **character suite** with Group H (gatekeepers) and the relevant Group J/K characters.
4. Activate **stakeholder sub-battery** (§11.8).
5. Document. Multi-scale and AIT are optional.

### 13.4 Recommended sequence for scope-level claims

1. Frame the claim and what is being in-scoped or out-scoped.
2. Run **Group B scope tests** (§6).
3. Run **two-path** applied reflexively (does this scope decision create an allocation asymmetry on the author? does it create a shield?).
4. Run **character suite** including Groups G/H/I/L (critics, gatekeepers, users, legacy).
5. Run **Group C authorial tests** (§7) — scope decisions change exposure surface.
6. Run **Group D strategic tests** (§8) — scope decisions often determine placement.
7. Confirm **success criteria alignment** (§9).
8. Document findings in a rigor-pass record (pattern: `commons_bonds_rigor_pass_YYYY-MM-DD_v#_#_#.md`).

### 13.5 Parallelism is encouraged when tests are independent

Two-path and AIT cross-check each other rather than feeding each other — running them in parallel reduces confirmation bias. Character suite is independent of two-path. Success criteria is downstream of everything and should run last.

### 13.6 When tests disagree

Disagreement between tests is a finding, not a failure. A claim that passes AIT but fails two-path is not the same as a claim that passes both. Surface the disagreement in the decision memo; do not paper over it. The C6 v1.0.0 → v2.0.0 rerun is the object lesson: running only some of the applicable tests produced a recommendation that was technically defensible on the narrow battery but missed a decisive finding the full battery would have surfaced.

---

## 14. Fill-in template

Copy-paste into a new decision memo file named `commons_bonds_{topic}_{v#_#_#}.md` (or `.html` if math rendering is required). Replace all bracketed placeholders.

````markdown
# Commons Bonds — [Topic] Decision Memo

**Date:** YYYY-MM-DD
**Version:** X.Y.Z
**Supersedes:** [prior version or "none"]
**Protocol version applied:** commons_bonds_rigor_protocol_v1_2_0.md
**Rigor depth:** [full / light]

---

## Claim under evaluation

[One-paragraph precise statement. Name alternatives if they exist.]

## Routing classification

- **Claim type(s):** [tier-level / architectural / scope-level / stakeholder-facing / novelty / applied-policy]
- **Tests to run:** [from routing rule §4]
- **Scales in scope:** [individual / community / government / corporate — check all that apply]
- **Environments in scope:** [Earth / off-Earth / both]
- **Character sub-batteries activated:** [methodological / stakeholder / meta / none]

## Preliminary recommendation

[One sentence. Will be confirmed or modified by the tests below.]

---

## Group A — Framework tests

### Test 1 — AIT (if applicable)

For each sub-claim or tier:
- **Scarcity:** [name]
- **Under abundance:** [persists / evaporates]
- **Verdict:** [PASS / FAIL / CORROBORATIVE]

### Test 2 — Two-Path

#### Path 1 — Allocation Symmetry
- **Who captures value:** [explicit]
- **Who bears cost:** [explicit]
- **Structural?** [yes / no]
- **Tier assignment unambiguous?** [yes / no]
- **Verdict:** [PASS / FAIL / CONDITIONAL]

#### Path 2 — Shield Absence
- **Shield type:** [epistemic / institutional / political / fiduciary / spatial / temporal / other]
- **Structural?** [yes / no]
- **Correctly named?** [yes / no]
- **Does architecture create a new shield?** [no / yes — specify]
- **Verdict:** [PASS / FAIL / CONDITIONAL]

### Test 3 — Merger / Primitiveness Gates (if layer claim)

- **Merger gate:** [Case A direction: abundance of candidate, scarcity of adjacent; Case B direction: reverse. Bilateral independence: yes/no]
- **Primitiveness gate:** [decomposition attempt; clean decomposition = FAIL; resists decomposition = PASS]
- **Verdict:** [PASS / FAIL]

### Test 4 — Multi-Scale × 2 Environments

| Scale | Earth | Off-Earth | Overall |
|---|---|---|---|
| Individual | | | |
| Community | | | |
| Government | | | |
| Corporate | | | |

[Narrative on scale-specific and environment-specific findings, especially any scale/environment where the claim cannot be fixed within itself.]

---

## Group B — Scope tests

[For each of Tests 6–9, state: finding / verdict / mitigation if any.]

## Group C — Authorial / practical tests

[For each of Tests 10–13, state: finding / verdict / mitigation if any.]

## Group D — Strategic / reception tests

[For each of Tests 14–19, state: finding / verdict / mitigation if any.]

## Group E — Success criteria alignment

| Criterion | Effect | Notes |
|---|---|---|
| Vocabulary portability | [serves / dilutes / neutral] | |
| Upstream-of-Goal-1 | [serves / dilutes / neutral] | |
| Direct-to-Goal-2 | [serves / dilutes / neutral] | |
| Labor-lawyer-in-2039 | [serves / dilutes / neutral] | |

## Group F — Content quality tests

[For each of Tests 24–27, state: finding / verdict / mitigation if any.]

---

## Character pressure suite

### Group G — Critics

| # | Character | Pressure point | Strength | Mitigation |
|---|---|---|---|---|
| 1 | Hostile coal-industry defender | | | |
| 2 | Left critic | | | |
| 3 | Right critic | | | |
| 4 | Journalist (hit-piece angle) | | | |

### Group H — Gatekeepers

| # | Character | Pressure point | Strength | Mitigation |
|---|---|---|---|---|
| 5 | Noema editor | | | |
| 6 | Berggruen judge | | | |
| 7 | Publisher's legal counsel | | | |
| 8 | Literary agent | | | |
| 9 | Tenured economics chair | | | |

### Group I — Intended users

| # | Character | Pressure point | Strength | Mitigation |
|---|---|---|---|---|
| 10 | Labor lawyer 2039 | | | |
| 11 | Community organizer | | | |
| 12 | Graduate student | | | |
| 13 | Policy researcher | | | |

### Group J — Cultural readers

| # | Character | Pressure point | Strength | Mitigation |
|---|---|---|---|---|
| 14 | Appalachian reader | | | |
| 15 | Young worker | | | |
| 16 | Former IT consultant | | | |
| 17 | Ostrom scholar | | | |
| 18 | Harvey / Klein reader | | | |

### Group K — Personal / proximal

| # | Character | Pressure point | Strength | Mitigation |
|---|---|---|---|---|
| 19 | Family-member reader | | | |
| 20 | SGA constituent | | | |
| 21 | Nursing colleague | | | |
| 22 | MFA critic | | | |

### Group L — Ethical and legacy

| # | Character | Pressure point | Strength | Mitigation |
|---|---|---|---|---|
| 23 | Former subordinate | | | |
| 24 | Reader in 2040 | | | |
| 25 | Grandfather at NASA Langley | | | |

### Sub-batteries (if activated)

[Methodological Defense M1–M4 / Stakeholder S1–S5 / Meta X1–X2 — same table format.]

---

## Findings summary

[Aggregate matrix. Highlight any decisive finding (a test or character whose result is sufficient on its own to determine the recommendation). Highlight any structural weakness (flagged by multiple characters / tests on the same point).]

## Recommendation (confirmed)

[Final recommendation. Reasoning sharpened by the tests above.]

## Pre-drafting items surfaced

[Items that cannot be deferred to drafting-stage resolution — e.g., legal review, anonymization protocols, permissions.]

## Implementation plan (if applicable)

[File-level actions. Completion criteria. Queue position relative to other pending patches.]

## Open questions / execution gates

[Any CONDITIONAL verdicts converted to measurable pass/fail gates. Any issues deferred to a later session or gate-check.]
````

---

## 15. Documentation requirements

When a full rigor pass is applied, the output should be recorded as part of the decision's documentation. Specifically:

- The decision memo references the protocol version (e.g., "v1.2.0 protocol applied; see §4 routing").
- Substantial rigor passes produce a pass-record document (`commons_bonds_rigor_pass_YYYY-MM-DD_v#_#_#.md`) separate from the protocol doc itself.
- Critical flags from the character suite that create pre-drafting items are tracked in the relevant scope or workstream document.
- If a rigor pass reveals a finding that contradicts or corrects earlier decisions, the correction is explicitly named with the test or character that surfaced it.
- The session handoff's files-produced table references the rigor pass record.

This documentation requirement exists so that future sessions can review what was tested and what survived, rather than re-running rigor from scratch.

---

## 16. Worked Examples

### 16.1 First worked example — C6 Decision Memo v2.0.0

The C6 memo is the first complete application of v1.1.0. It evaluates four options (retire FGC / parallel layers / reconcile / collapse via manifestations) against the two-path test at four scales, with AIT + ten-critic + success criteria as corroborative cross-checks.

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

**Lesson:** The first memo applied AIT + ten-critic without the two-path test, because the C5 patch had not yet been integrated into a canonical methodology doc. The rerun with two-path surfaced a decisive new finding (the Tier 8 absence in the older FGC taxonomy) that the original battery had not produced. **This is the failure mode v1.1.0 was designed to prevent.**

### 16.2 Second worked example — Layer and Tier Stress Test v1.0.0

`commons_bonds_layer_tier_stress_test_1_0_0.md` is the second complete application, conducted in session v1.19.0 after the off-Earth exemplar was drafted.

| Test | Section in stress test memo |
|---|---|
| Protocol application per layer | §3 (seven sub-sections) |
| Layer summary table | §3.8 |
| Tier-level rigor per tier | §4 (nine sub-sections) |
| Tier summary table with verdicts | §4.10 |
| Aggregate findings | §5 |
| Recommended next actions | §6 |

**Lesson:** The off-Earth exemplar was added to Test 3 in v1.1.0 specifically because, mid-session, the "Planetary" candidate name passed at Earth-individual scale but failed at off-Earth-individual. Earth-only exemplars silently approved the failure. **This is a second failure mode the protocol now guards against.**

### 16.3 Third worked example — v1.24.0 scope rigor passes

`commons_bonds_rigor_pass_2026-04-21_v1_0_0.md` records three rigor passes conducted during the v1.24.0 scope session, producing scope v1.0.1 → v1.0.3. The passes surfaced four corrections (PCC reclassification tier → shielding condition, publishing-path reclassification orthogonal → integral, Book Two precondition restructuring, Ch. 8 coal rationale explicit). The third pass introduced a new worked structure: the pass-record-separate-from-protocol pattern formalized in §2.4.

**Lesson about protocol governance:** The v1.24.0 session produced a parallel-lineage protocol artifact (v1.0.0) without awareness that v1.1.0 was already canonical. The parallel-lineage artifact had expanded coverage but silently dropped AIT, multi-scale × 2 environments, and the procedural template. **This is a third failure mode: lineage-drift, where protocol work is done without reconciliation against canonical state.** Mitigation (formalized here): at session start, verify the canonical protocol version against the operating core; before producing a new protocol artifact, run reconciliation against the current canonical version.

**Why reference rather than embed the memos:** All three memos are large and live as separate files. Embedding would bloat the protocol and couple edits. The reference pattern keeps the protocol lean and allows the memos to evolve independently.

---

## 17. Versioning and maintenance

### 17.1 Current version

**1.2.0** (2026-04-21) — proposed, awaiting ratification.

### 17.2 Upload pattern

Upload at session start alongside the current session handoff. Do not modify within-session. If the canonical protocol version has drifted from what the session is using, flag the delta before running tests.

### 17.3 Version numbering

- **Patch (1.2.1, 1.2.2):** clarifications, typo fixes, worked-example additions.
- **Minor (1.3.0, 1.4.0):** new routing category, new sub-battery, additional worked example promoted to top-level reference, new test added to a group.
- **Major (2.0.0):** structural change to the test battery itself (e.g., a new primary test added, a group restructured, routing rule overhaul).

### 17.4 When to revise

1. A new type of decision emerges that doesn't fit the routing categories cleanly.
2. A rigor test proves systematically redundant with another across multiple applications.
3. A character type emerges as standardly important that is not currently on the list.
4. A character type on the list proves systematically non-differentiating (never produces pressure).
5. The CB operating core itself is revised in a way that affects the framework tests (Group A).
6. A systematic attack pattern emerges in cascade reception (e.g., Noema decline with specific feedback) that the character suite didn't anticipate — suggesting a missing character.
7. A new rigor test is validated across multiple claims and becomes a standing test.
8. A worked example reveals a protocol gap.

### 17.5 When not to revise

- A single decision memo fails. That failure is the finding, not a protocol problem.
- A test produces an unexpected verdict. Document and move on.
- Stylistic or formatting preferences change. Use the session handoff for those.

### 17.6 Revisitability of rejected tests and characters

A test or character that fails to differentiate on one pass may differentiate on another. Rejection is a finding about the tested application, not a permanent verdict. Re-test warranted when new decision types surface that existing tests don't cover cleanly.

### 17.7 Change log

**v1.2.0 (2026-04-21):** Lineage-reconciliation revision. Absorbs v1.0.0 (parallel-lineage artifact produced in v1.24.0 session) into the v1.1.0 canonical lineage. Changes:
- (1) Restored AIT Falsifiability Gate and Multi-scale × 2 Environments from v1.1.0, which v1.0.0 had silently dropped.
- (2) Absorbed v1.0.0's expanded test catalog: scope tests (Group B), authorial tests (Group C), strategic tests (Group D), content-quality tests (Group F). Integrated as modular test groups.
- (3) Absorbed v1.0.0's 25-character pressure suite (Groups G–L) as the canonical character roster. Mapped v1.1.0's ten-critic standing battery into the expanded roster; preserved the four unmapped critics (Analytic Philosopher, AI Adversary, Novelty Critic, Completeness) as a Methodological Defense sub-battery.
- (4) Superseded v1.1.0 Test 5 (four realistic success criteria) with v1.0.0 Group E (Goal-1 / Goal-2 / labor-lawyer-in-2039), which is tied to the canonical 13+-year success sentence.
- (5) Shipped the v1.21.0 drafted additions formally: merger gate, primitiveness gate, rejected-candidates-revisitable.
- (6) Added full-vs-light rigor depth axis as orthogonal to routing.
- (7) Added scope-level as a new claim type in the routing rule, with its own sequencing in §13.4.
- (8) Added third worked example (v1.24.0 rigor pass record) and captured a third failure mode (lineage-drift) that this revision itself guards against.

**v1.1.0 (2026-04-20):** Minor revision of v1.0.0 (original canonical). (1) Test 3 (multi-scale) expanded: each scale now tested against at least one Earth-baseline exemplar AND one off-Earth / engineered-habitat exemplar. (2) §4.2 AIT worked-examples table transcription fix. (3) §10 expanded to two worked examples with layer/tier stress test promoted.

**v1.0.0 (2026-04-20):** Initial canonical protocol. Consolidated AIT + two-path + multi-scale + ten-critic + success criteria. Five-route routing rule. Two-tier critic battery. Fill-in template. C6 Decision Memo v2.0.0 referenced as first complete worked example.

**v1.0.0 parallel-lineage (2026-04-21, superseded by this v1.2.0):** v1.24.0 session artifact. Produced without awareness of v1.1.0 canonical state. Contributed the expanded test catalog (Groups B/C/D/E/F), expanded character roster (25), full/light rigor axis, and formal revisitability. Absorbed into this v1.2.0 revision.

---

## 18. Appendix — cross-references

- **Operating core:** preferences, session handoffs through v1.24.0, C9 patch §3 (AIT canonical positioning).
- **AIT source:** `eight-tier-v10.html`.
- **Two-path source:** `commons-bonds-c5-two-path-rigor.md` (C5 patch).
- **Success criteria source:** `commons-bonds-success-criteria_11.html` (earlier) and v1.24.0 scope v1.0.3 §7 (newer, referenced by Group E).
- **Scaffolding-vs-load-bearing canonical:** `c9_ait_canonical_positioning_patch.md`.
- **First worked example:** `commons_bonds_c6_decision_memo_2_0_0.html`.
- **Second worked example:** `commons_bonds_layer_tier_stress_test_1_0_0.md`.
- **Third worked example:** `commons_bonds_rigor_pass_2026-04-21_v1_0_0.md`.
- **Superseded protocol lineage documents:** `commons_bonds_rigor_protocol_1_1_0.md` (v1.1.0), `commons_bonds_rigor_protocol_v1_0_0.md` (v1.0.0 parallel-lineage).

---

*End of Commons Bonds Canonical Rigor Protocol v1.2.0.*
