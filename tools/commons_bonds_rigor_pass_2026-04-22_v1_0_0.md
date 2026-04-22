# Commons Bonds — Rigor Pass Record

**Date:** 2026-04-22
**Version:** 1.0.0
**Protocol version applied:** `commons_bonds_rigor_protocol_v1_2_0.md`
**Next protocol version:** v1.2.1 (clarifications patch produced same session, integrating this record's findings)
**Input document:** `commons_bonds_rigor_vs_layers_triage_v1_0_0.md` (triage assessment)
**Status:** Ratified findings — v1.2.0 is canonical effective 2026-04-22; v1.2.1 patch follows.

---

## 1. Purpose

This rigor pass record documents the Part 1 ratification work of session v1.25.0 → v1.26.0: formal ratification of rigor protocol v1.2.0 as canonical, correction of two triage findings (one error, one refinement), and capture of a conceptual finding about the shield mechanism in the two-path test. It also records the canonical merger/primitiveness examples table for reference in the book's methodology appendix.

Per protocol §2.4, this record is separate from the protocol itself: the protocol defines what tests exist; this record documents what was tested, what was found, and what was ratified on this specific date.

---

## 2. Ratification — rigor protocol v1.2.0

**Ratified:** `commons_bonds_rigor_protocol_v1_2_0.md` is canonical effective 2026-04-22.

**Basis for ratification:** The triage applied each of the protocol's ~26 tests to the 10 canonical abundance layers and found that the test suite collectively does real work. Load-bearing tests (Group A) are foundational; scaffolding tests in Groups B–F earn their keep at appropriate scales (layer, chapter, case, book). No test was found to be empty scaffolding. Five consolidation candidates were identified — these are cross-reference edits, not structural changes, and are appropriately handled by the v1.2.1 clarifications patch per protocol §17.3.

**Supersession effect:** v1.1.0 and v1.0.0 (parallel-lineage artifact) are formally superseded. The three worked examples in §16 remain canonical; no rigor-pass-record convention was in force when they were produced, so they are grandfathered under the protocol's own historical record.

---

## 3. Triage findings summary

Full details in the triage file. Headline tally applied against the 10 canonical abundance layers (Atmospheric, Geographic, Temporal, Institutional, Demographic, Ecological, Political, Cohesion, Informational, Agency):

**Load-bearing (6 tests):** 1 (AIT), 2 (Two-Path), 3 (Merger/Primitiveness), 4 (Multi-Scale × 2 Envs), 20 (Vocabulary portability), 23 (Labor-lawyer-2039).

**Scaffolding that earns its keep (5 tests):** 7 (Cross-spectrum preservation), 17 (Target reader recognition), 18 (Competitor/overlap), 19 (Decade-out durability), 25 (Steelmannability).

**Process-only at the layer level (10 tests, one corrected — see §4):** 6, 9, 10, 11, 14, 15, 16, 21, 24, 27.

**Consolidation candidates (5 tests):** 8 (subsume into 1), 12 (converge with 7), 22 (converge with 17), 26 (annotate against 1), 20/23 (mark as companion pair).

---

## 4. Corrections to triage

### 4.1 Test 13 — layer-level relevance via canonical cases (CORRECTION)

The triage verdict of "PROCESS-ONLY, NON-DIFFERENTIATING ON LAYERS" was wrong. The correction is structural.

**Corrected finding:** Test 13 (career-risk compatibility) does real work at the layer level when a layer's canonical cases involve industries capable of professional retaliation against the author. At minimum:

- **Informational.** Canonical cases include tobacco-industry internal-research suppression, pharma data suppression, and the mapping of pharmaceutical sales geography to opioid-death rates in Appalachian counties. Any of these, even presented straightforwardly, can generate industry backlash that routes through professional channels (nursing boards, employer-adjacent networks, insurance credentialing bodies).
- **Political.** Canonical cases include regulatory capture by specific industries whose lobbying networks interlock with healthcare financing. Discussion of how political capture interferes with public-health regulation could trigger similar routed backlash.
- **Institutional (secondary).** CEO-era case content carries related career-risk exposure, partially addressed by the pre-drafting anonymization and NDA gates.

**Implication:** The claim that career-risk is "layer-level non-differentiating" was a category mistake. A layer's canonical cases are not incidental to the layer — they are what the layer means in practice. Career-risk for specific layers is inherent, not incidental. Mitigation remains primarily case-level (how a specific case is presented and framed) rather than layer-level (the layer itself is not the risk), but the test does gate certain layers differently from others.

**Protocol action:** v1.2.1 updates Test 13 to acknowledge layer-level relevance via canonical cases. The triage tally moves Test 13 from "process-only" to "scaffolding, earns it for specific layers."

### 4.2 Test 3 — book-visibility note (REFINEMENT)

**Note for the canonical record:** Test 3 (merger / primitiveness gates) is load-bearing for taxonomy integrity but doesn't need heavy book-front prose. A short methodology passage and an appendix table (which candidates passed or failed which gate, and why) carries it. This is where the book earns credibility with the Ostrom-successor reader without belaboring the reader who just wants to price their situation.

**Implication for the book:** The appendix table in §6 of this record is the canonical source for that passage. Chapter-level prose should note the existence of the gates briefly when introducing the layer set (one paragraph) and point readers to the appendix for the examples that establish the discipline.

**Protocol action:** v1.2.1 adds this as a book-visibility note to §5.3 and cross-references the examples table in this record.

---

## 5. Conceptual finding — consent does not dissolve cost severance

### 5.1 The observation

A knowledge worker who is fully aware of the trade they are making — trading personal life for compensation while working 120+ hour weeks — and who agrees to it, is still bearing cost severance. The individual's awareness and agreement do not eliminate the structural allocation asymmetry.

### 5.2 Why this matters for Path 2

The two-path test names "shield absence" as the condition for cost severance to be structural and persistent. Path 2 asks: what is the distance condition preventing recognition or correction?

The observation sharpens what "distance" and "shield" mean. Individual awareness is not the shield. In the 120-hour-week case, the worker *sees* the cost clearly. Yet the cost severance persists. The shield is therefore not at the individual-recognition level — it operates at a different level.

**The shield is consent-normalization.** When individual consent is treated by the surrounding social, legal, and institutional framework as *closing* the accounting — "they chose it, no one owes them anything" — then consent becomes a structural social shield. It does not prevent the individual from seeing the cost; it prevents society from *owing* the individual for bearing it. The shield operates at the level of social-accounting terminus, not individual epistemics.

This is consistent with the canonical statement in v1.2.0 §5.2: allocation asymmetry (Path 1) is the cost severance; shield absence (Path 2) explains why it persists. Chris's observation refines the shield typology: consent-normalization joins epistemic, institutional, political, fiduciary, spatial, and temporal distance as a recognized shield type.

### 5.3 Implications

**For the framework:** Path 2's shield typology is expanded to explicitly include consent-normalization. A claim in which an individual knowingly agrees to a cost-bearing arrangement is not automatically a shield-absent case; it may be a consent-normalization shield case where the individual's agreement *is itself* the shielding mechanism at the social level.

**For the book:** This shield type is pedagogically important because it sidesteps the "but they knew what they were signing up for" counterargument that conservative and libertarian critics will raise. The author's 120-hour-week consulting years are a canonical case for this shield type: the narrator *saw* the trade, *agreed* to it, and was *still* bearing structural cost severance — because the trade was allocated structurally (the firm captures vastly more value than the labor cost), and consent was treated terminally by the surrounding labor-market framework.

Chris's framing: "even if someone is aware they are trading off cost for being used to create or provide value... and they agree to it... that doesn't stop it from being cost severance." This goes in the book as narrative — personal stories where awareness and agreement coexisted with structural cost-bearing — in support of the shield-typology expansion.

**For the layer set:** The consent-normalization shield applies particularly to Institutional (employment relationships, contract labor), Temporal (knowing trade of future-self compensation for present-self income), and Agency (coercion that routes through formal consent).

**Protocol action:** v1.2.1 adds a brief shield-typology note to §5.2 referencing consent-normalization and cross-references this rigor pass record §5 for the full treatment.

---

## 6. Merger / primitiveness examples table

This table is the canonical reference for the book's methodology appendix (per §4.2). It records, in one place, which candidates passed or failed the taxonomy-integrity gates, and why. Entries are sourced from prior rigor passes; candidates currently under evaluation are listed separately.

### 6.1 Ratified outcomes

| Candidate | Tested against | Gate | Verdict | Reason | Source |
|---|---|---|---|---|---|
| Cohesion | Demographic | Merger | **PASS** (bilateral independence) | Case A: Bowling Alone suburban US metros (demographic abundance, cohesion scarcity). Case B: small cohesive religious communities below specialist-sustaining threshold (demographic scarcity, cohesion abundance). Both directions confirmed → layers remain distinct. | v1.21.0 ratification |
| Cohesion | Existing 7 layers | Primitiveness | **PASS** | Revealed costs (isolation-at-density, trust-erosion, civic-infrastructure decay) do not decompose cleanly into existing layers. Cohesion is a distinct scarcity form. | v1.21.0 ratification |
| Informational | Existing 8 layers | Merger + Primitiveness | **PASS** | Tobacco, pharma, and opioid data-suppression cases reveal an allocation asymmetry not priced by Political (regulatory capture) or Institutional (intra-organizational governance). Informational scarcity is primitive — knowledge cannot be substituted for capital, coercion, cohesion, or time. | v1.21.0 ratification |
| Agency | Existing 9 layers | Primitiveness | **PASS** (strongest primitiveness result of the three v1.21.0 candidates) | Coercion-structure is irreducible to any composition of the other layers. Cross-ideological traction (libertarian non-coercion + leftist anti-exploitation) is a corroborative signal of primitiveness. | v1.21.0 ratification |
| Survivability | Existing layers | Primitiveness | **FAIL** | Revealed costs decompose cleanly into Tier 4 (Foreclosure Cost) extended to civilization-scale timescales. Retained as valid cross-layer concept; rejected as independent layer. | v1.21.0 rejection |
| "Existential / Meaning Cost" (older FGC tier) | N/A | AIT | **FAIL** (prior gate) | No identifiable scarcity. Phenomenological struggles persist under abundance → not scarcity-grounded → not a framework-compatible cost. | v1.2.0 §5.1 worked examples |
| "Immediate Survival Cost" (older FGC tier) | Tier 1 | AIT (redundancy variant) | **FAIL** (prior gate) | Same scarcity as Tier 1. Redundant, not distinct. | v1.2.0 §5.1 worked examples |

### 6.2 Candidates under evaluation (not yet ratified)

The v1.24.0 → v1.25.0 handoff flagged several concept candidates as potentially redundant with the canonical 10. These are queued for Part 2 rigor passing; they are recorded here as watch items, not findings.

| Candidate | Likely merger with | Likely primitiveness outcome | Pass required |
|---|---|---|---|
| Social / relational | Cohesion | Likely merger (if so: already covered) | Part 2 |
| Cognitive / psychological | Agency | Likely subsumption under Agency | Part 2 |
| Information / data | Informational | Likely subsumption under Informational | Part 2 |
| Biological / species | Ecological | Likely subsumption under Ecological | Part 2 |
| Cosmic / physical-law | None existing | Worth testing — may be primitive | Part 2 |

### 6.3 How to read the table

Entries in §6.1 are ratified. Entries in §6.2 are hypotheses to be tested. In the book's methodology appendix, only §6.1 should appear as established taxonomy discipline; §6.2 is internal to the rigor pipeline and does not need to be in the book. The book's message via this table is: *the framework disciplines itself — candidates are tested and rejected when they don't pass, and when they do pass, they earn their place*.

---

## 7. Scope of the v1.2.1 patch

The v1.2.1 protocol file (`commons_bonds_rigor_protocol_v1_2_1.md`) is produced same session. Its scope is exactly what this record has ratified:

1. Test 3 book-visibility note + cross-reference to §6 of this record.
2. Tests 7 and 12 layer-level convergence note.
3. Test 8 subsumption under Test 1 at layer level.
4. Test 13 correction — layer-level relevance via canonical cases.
5. Tests 17 and 22 layer-level convergence note.
6. Tests 20 and 23 marked as companion pair at layer level.
7. Test 26 annotated as "falsifiability beyond AIT" at layer level.
8. §5.2 Path 2 shield-typology note — consent-normalization added as recognized shield type; cross-reference to §5 of this record.
9. §17.7 change log entry for v1.2.1.

No structural changes. No new tests. No removed tests. All edits are cross-references and clarifications per §17.3 patch-level semantics.

---

## 8. Next steps

1. **v1.2.1 produced** same session; ready for upload.
2. **Character suite triage** produced same session (`commons_bonds_character_suite_vs_layers_triage_v1_0_0.md`), same treatment as test triage but against the 25-character pressure suite.
3. **Part 2 — rigor pass on the 10 canonical layers using v1.2.1** is the next substantive work. Per the handoff, this produces `commons_bonds_abundance_layers_v1_0_0.md` and its own rigor pass record. The gap-close against Groups B–F is light for already-ratified layers; the set-completeness sweep against §6.2 candidates is the new work.
4. **Part 3 — audit v1.24.0 outputs against 10-layer canonical set** continues as previously scoped.
5. **Book methodology appendix** should reference §6.1 of this record as the canonical merger/primitiveness examples table, per §4.2.

---

## 9. Documentation hooks

Files produced or updated by this rigor pass:
- `commons_bonds_rigor_pass_2026-04-22_v1_0_0.md` — this file
- `commons_bonds_rigor_protocol_v1_2_1.md` — clarifications patch integrating this record's findings
- `commons_bonds_character_suite_vs_layers_triage_v1_0_0.md` — companion to the test triage, produced same session

Inputs to this rigor pass:
- `commons_bonds_rigor_protocol_v1_2_0.md` — ratified
- `commons_bonds_rigor_vs_layers_triage_v1_0_0.md` — proposed assessment, triaged and partially corrected here
- `commons-bonds-session-handoff-2026-04-21_v1_25_0.html` — session context

Chris's conceptual input to §5 of this record (consent-does-not-dissolve-severance, 120-hour-week case, shield-as-consent-normalization) is attributed in the protocol's v1.2.1 change log.

---

*End of Commons Bonds Rigor Pass Record 2026-04-22 v1.0.0.*
