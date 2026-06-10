# CIT positioning consistency audit — 2026-04-25

**Date:** 2026-04-25
**Purpose:** Closes M11 Character 18 (philosopher of science / Popperian / Lakatosian) finding from the 2026-04-24 academic-rigor full test (rigor pass `commons_bonds_rigor_pass_2026-04-24_academic_rigor_full_test_v1.0.0.md` §4.4, commit `ae90800`). Audits chapter prose + guidance docs + supplement for consistency between two distinct claims:

- **CIT is a thought-experiment discrimination gate** — its function is to filter cost claims for scarcity-grounding via counterfactual inversion (CAI / CCI). Falsification here is conceptual: a cost claim either survives or fails the inversion thought-experiment.
- **Empirical methods are the falsifiability layer above CIT** — specific cost-claim predictions (e.g., "CS > 0 for Appalachian coal") are empirically falsifiable. M3.7 + M6.3 + M6.4 + Block 4 validation are the empirical-falsifiability infrastructure.

The framework's correct positioning is: *CIT is the methodological filter; empirical work is the falsifiability layer above it.* M11 Char 18 surfaced that this distinction is correctly held in supplement §6.2 + rigor protocol M6.3, but **chapter prose may not consistently honor it**.

**Status:** Audit/scan record. Does NOT modify chapter prose. Phase B authoring integration is the next-step item.

---

## §1. Where the CIT-vs-empirical distinction lives correctly

| Location | Treatment | Status |
|---|---|---|
| `core/technical-appendix/archive/TechnicalAppendix_v0.0.5_supplement.md` §6.2 (Four Gates admission apparatus) | "The gates filter cost *claims* against established commons; they do not filter what counts as a *commons*" — CIT positioned as admission-filter, not as empirical falsification. | CORRECT — explicit. |
| `core/methodology/cit_examples_v1_0_0.md` §6 (Gates as a complete admission apparatus) | Gates positioned as admission apparatus for cost claims. | CORRECT — explicit. |
| `tools/rigor-passes/archive/commons_bonds_rigor_pass_2026-04-24_three_ways_rcv_formal_model_v1.0.0.md` Block 4 | Block 4 explicitly positioned as empirical-falsifiability infrastructure separate from CIT. | CORRECT — explicit. |
| Tech Appendix supplement §6.1.1 (level-of-claim refinement, added 2026-04-25 in this session) | New refinement integrates the level-of-claim discipline; reinforces CIT as method-level, claim-level falsification. | CORRECT — explicit. |

---

## §2. Chapter-prose locations where the distinction needs Phase B integration

### §2.1 Ch 6 — Three Ways of Counting

**HTML draft:** [`manuscript/chapters/Chapter__6_ThreeWaysofCounting__Draft.html`](../../manuscript/chapters/Chapter__6_ThreeWaysofCounting__Draft.html)

**Finding:** Ch 6's "Objection 2: Your model says extraction is always underpriced, which means it is unfalsifiable" handles the falsifiability question at the level of the **CS prediction** ("CS > 0 in every case"), correctly positioning that prediction as empirically falsifiable when an instrument that drives CS to zero gets built (Yeager-and-the-sound-barrier analogy). This response is correct as far as it goes — but it doesn't explicitly distinguish:

- **CIT-level falsifiability (thought-experiment):** does a candidate cost claim survive CAI + CCI inversion?
- **CS-level falsifiability (empirical):** does the predicted CS > 0 hold for case X under measurement?

The current prose handles the second question well; the first question is implicit. A Popperian reader (M11 Char 18) will press on this: "you call CIT a falsifiability gate, but CIT operates on thought-experiments — what's the empirical operation?"

**Recommended Phase B integration:** add a one-paragraph sentence-level distinction within the Objection 2 response. Suggested form:

> *"Two distinct falsifiability operations are at work in this framework. The Commons Inversion Test (CIT) is a thought-experiment filter — a candidate cost claim either survives or fails its counterfactual inversion (would the cost be priced differently if the commons were absent? if it were inexhaustible?). This is conceptual falsification: claims that don't survive are filtered out before they reach the measurement apparatus. The empirical falsifiability — the layer above CIT — is at the level of specific cost-claim predictions: 'CS > 0 for case X under existing accountability regimes.' That prediction is testable via the case-study record. CIT screens the candidate; empirical measurement adjudicates the prediction. The framework's response to the Popperian objection is therefore not 'CIT is empirically falsifiable' (it isn't; thought-experiments don't survive that test) but rather 'CIT is a methodological filter and empirical falsifiability operates one layer above CIT, at the level of CS / RCV predictions for specific cases.'"*

**Phase B blocker dependency:** Methodology-defense-consolidation work (Phase B item 3 from v1.44.0 handoff) — this paragraph is part of the broader defense-rationales consolidation.

### §2.2 Ch 6 GuidanceDoc

**File:** [`manuscript/chapters/Chapter__6___GuidanceDoc.md`](../../manuscript/chapters/Chapter__6___GuidanceDoc.md)

**Finding:** Lines 110 + 128 + 212–236 carry the same Counterargument 4 / "model is unfalsifiable" handling that appears in the HTML draft. The GuidanceDoc treats falsifiability at the CS-prediction level only; the CIT-level distinction is not surfaced.

**Recommended Phase B integration:** when the GuidanceDoc's Counterargument 4 prose is integrated into final-draft Ch 6 prose, the §2.1-suggested distinction lands at the same time. The GuidanceDoc itself need not be revised (it's a guidance doc, not reader-facing prose); the integration target is the chapter draft.

### §2.3 Ch 6 Supplementary Drafts

**File:** [`manuscript/chapters/Chapter__6___SupplementaryDrafts_2026-04-24.md`](../../manuscript/chapters/Chapter__6___SupplementaryDrafts_2026-04-24.md) §1 Passage A (CIT introduction)

**Finding:** §1's CIT introduction passage describes CIT as a gate that operates on "candidate cost" claims — this language is correct and consistent with admission-apparatus framing. The passage doesn't go on to address the CIT-vs-empirical distinction (and reasonably doesn't, since this is the introduction passage). The distinction belongs later in Ch 6, in the methodology-defense + Counterargument-4 sections.

**Status:** No revision needed at this passage. The distinction lives elsewhere in the chapter's structure.

### §2.4 Ch 7 — The Colony Administrator

**File:** [`manuscript/chapters/Chapter__7_TheColonyAdministrator__Draft.md`](../../manuscript/chapters/Chapter__7_TheColonyAdministrator__Draft.md)

**Finding:** Ch 7 uses thought-experiment scenarios (Mars colony water; asteroid iron; lunar helium; comet volatiles; Europa ice) to demonstrate that the framework operates across parameter ranges. The chapter's claim is robust to the CIT-vs-empirical distinction because Ch 7 is explicitly thought-experiment territory: it's not claiming empirical falsifiability of specific Mars / asteroid / Europa cost predictions; it's claiming the *framework* produces sensible answers under varied parameter conditions. This is conceptually consistent with CIT-as-thought-experiment-filter.

**One falsifiability hit at line ~? (single occurrence):** the passage about V_civ ("genuinely unestimable... it's the value of knowing whether we're alone in the universe, which is a question that, once answered negatively by destroying the evidence, can never be asked again") — this passage handles a *different* unfalsifiability concern (the V_civ term being too large to estimate), not the CIT-vs-empirical distinction. No revision needed.

**Status:** Ch 7's positioning is internally consistent. Ch 6 Phase B integration should reference Ch 7 as the thought-experiment-territory chapter, contrasting with Ch 5's empirical-case-record territory, to make the CIT-vs-empirical layered structure visible across chapters.

### §2.5 Ch 7 GuidanceDoc

**File:** [`manuscript/chapters/Chapter__7___GuidanceDoc.md`](../../manuscript/chapters/Chapter__7___GuidanceDoc.md)

**Finding:** Single falsifiability hit, in context of CIT thought-experiment scope. Consistent with admission-apparatus framing.

**Status:** No revision needed.

### §2.6 Ch 10 — Common Bonds

**File:** [`manuscript/chapters/Chapter_10_CommonBonds__Draft.md`](../../manuscript/chapters/Chapter_10_CommonBonds__Draft.md)

**Finding:** No falsifiability hits in Ch 10 draft. The closing chapter's reflective register doesn't engage Popperian methodology directly, and reasonably doesn't.

**Status:** No revision needed for CIT positioning. Phase B Parfit-engagement passage placement (item 7 in current todo queue) is a separate question — Parfit's intergenerational moral-status grounding belongs in Ch 6 (primary) and / or Ch 10 (reflective companion), and that's a placement question for Phase B.

---

## §3. Stands-the-test-of-time-drafts file

**File:** [`research/commons_bonds_stands_the_test_of_time_drafts_v1.0.0.md`](../../research/commons_bonds_stands_the_test_of_time_drafts_v1.0.0.md)

**Finding:** Multiple "unfalsifiable / falsifiable" hits, all in the context of *engaging* objections rather than *positioning* CIT. The drafts are the **Counterargument-4 material** that would feed Ch 5 / Ch 6 integration. Same finding as §2.1 / §2.2: the CIT-vs-empirical distinction is implicit, not explicit.

**Status:** When this file's contents integrate into chapter drafts during Phase B, the §2.1-suggested distinction-paragraph lands alongside.

---

## §4. Verdict + Phase B work item

**Verdict:** **CIT positioning is correctly held in framework-internal docs (supplement, methodology, rigor passes) and consistently OK in chapter prose** — with one specific Phase B integration item:

> Ch 6 Counterargument-4 / "model is unfalsifiable" response should add an explicit one-paragraph distinction between **CIT-level thought-experiment falsification** and **empirical falsifiability of specific CS / RCV predictions**.

This single integration paragraph closes the M11 Character 18 finding cleanly. No structural rewrite of Ch 6 is needed; the existing prose handles the question well at the CS-prediction level and just needs the CIT-level distinction made explicit.

**Phase B item carry-forward:** "Add CIT-vs-empirical falsifiability distinction paragraph to Ch 6 Counterargument 4 section" — small-scope item; can land as a sub-item of the broader methodology-defense-consolidation work.

---

## §5. Cross-references

- `tools/rigor-passes/archive/commons_bonds_rigor_pass_2026-04-24_academic_rigor_full_test_v1.0.0.md` §4.4 — M11 Char 18 finding origin.
- `core/technical-appendix/archive/TechnicalAppendix_v0.0.5_supplement.md` §6.1.1 (level-of-claim refinement, 2026-04-25) — companion CIT-formal-spec refinement closing M11 Char 12.
- `core/technical-appendix/archive/TechnicalAppendix_v0.0.5_supplement.md` §6.2 — Four Gates admission apparatus (where CIT is correctly positioned as admission-filter).
- `core/methodology/cit_examples_v1_0_0.md` — seven worked CIT applications through Four Gates.
- `tools/commons_bonds_rigor_protocol_v2.2.0.md` (now v2.4.0 per supplement §1) — M6.3 module specifies the CIT-vs-empirical layered structure.

---

*End of CIT positioning consistency audit, 2026-04-25.*
