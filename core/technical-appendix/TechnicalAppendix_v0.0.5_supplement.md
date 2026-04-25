# Technical Appendix v0.0.5 — Supplement (canonical-source-of-truth pointer + new-section drafts)

**Date:** 2026-04-24
**Version:** v0.0.5 supplement
**Status:** Tier-1 update sidecar per Working Principle #4. Pairs with `TechnicalAppendix_v0.0.5.html` (in-place sweep of v0.0.4 — see §1 below).
**Supersedes:** Tech Appendix v0.0.4 (file renamed to v0.0.5 in same commit; sweeps documented in §1).

---

## §1. What changed when v0.0.4 → v0.0.5 (in-place sweep summary)

The HTML file `TechnicalAppendix_v0.0.5.html` is `TechnicalAppendix_v0.0.4.html` after a targeted in-place sweep applied 2026-04-24 to materialize same-day framework ratifications. **Per-section content (formulas, prose, examples) NOT changed**; only stale terminology updated. Remaining v0.0.5 work (substantive new sections — see §2 onward) is captured in this supplement document and pending integration into the HTML on Chris's next Tech Appendix authoring pass.

**Sweep applied:**

| Original term (v0.0.4) | Replacement (v0.0.5) | Count | Source rigor pass |
|---|---|---|---|
| AIT | CIT | 18 | `commons_bonds_rigor_pass_2026-04-24_term_cit_rename_v1.0.0.md` (commit `b294c79`) |
| Abundance Inversion Test | Commons Inversion Test | 7 | (same) |
| abundance dimension | commons category | 10 | `commons_bonds_rigor_pass_2026-04-24_10_commons_list_dissolution_v1.0.0.md` (commit `e30087e`) |
| Asymmetric Regret Principle | Asymmetric Regret Rule | 2 | `commons_bonds_rigor_pass_2026-04-24_arp_rename_v1.0.0.md` (commit `b8b62e3`) |
| Spatial CS (proper-noun) | Cost Severance | 2 | `commons_bonds_rigor_pass_2026-04-24_term_cost_severance_collision_v1.0.0.md` (commit `28fe34f`) |
| Version 0.0.4 (header) | Version 0.0.5 | 1 | (this commit) |
| v0.0.4 (filename refs) | v0.0.5 | 2 | (this commit) |

**Stale terms — sweep status (corrected 2026-04-24 in M12 sweep rigor pass `..._m12_intellectual_honesty_sweep_v1.0.0.md`):**

| Stale term | Count (originally) | Status | Successor / sweep disposition |
|---|---|---|---|
| CSG (**Civilizational Substitutability Gap** — *NOT* "Cost Severance Gap"; the original v0.0.5 supplement misexpanded the acronym; corrected here) | 22 | RETIRED 2026-04-24 on parsimony grounds (commit `3ec3707`) — CSG is a derivation of S (S_max(industrial) − S_max(existential)); framework doesn't name derived scalars. | **SWEPT 2026-04-24 in M12 sweep.** Replaced inline with prose "industrial-existential substitutability gap" per terms_index §792 ratified replacement. Tech Appendix §G formula retained as sub-entry under Substitutability Function. (Some passages may carry redundant "(CSG)" parentheticals after sed sweep — Phase B Tech Appendix authoring pass should clean those up.) |
| FGC | 15 | RETIRED (8-tier-vintage acronym) — context-meaning shifts per occurrence | NOT swept (passage rewrite required, not string substitution). Phase B Tech Appendix authoring pass — replace with Foreclosure Cost (C₁) or appropriate tier-name spelled out per local context. |
| Universality Test | 1 | RETIRED — replaced by structural-vs-topical pairing diagnostic (no single named referent). | NOT swept (passage rewrite required). Phase B Tech Appendix authoring pass. See rigor pass `commons_bonds_rigor_pass_2026-04-24_term_universality_test_re_examination_v1.0.0.md`. |

**Reading-discipline note for v0.0.5 HTML:** Wherever the HTML references FGC / "Universality Test", read those passages with the reader-correction in mind. Phase B authoring pass will rewrite the affected sections. CSG references have been swept inline as of M12 sweep. Until then, this supplement + `core/glossary/commons_bonds_updated_glossary_v3.html` + `core/terms/terms_index.md` are canonical-source-of-truth.

---

## §2. New section: Two-Instrument Architecture (CSD + RCV)

**Status:** v0.0.5 NEW SECTION — not yet in HTML; awaiting integration.
**Source rigor passes:**
- CSD ratification: `commons_bonds_rigor_pass_2026-04-24_term_csd_v1.0.0.md` (commit `98fc8e6`)
- CS = RCV − B equation: `commons_bonds_rigor_pass_2026-04-24_term_cs_rcv_b_equation_v1.0.0.md` (commit `220914f`)
- B1 + B2 decomposition + naming: `commons_bonds_rigor_pass_2026-04-24_b1_b2_naming_v1.0.0.md` (commit `8e6a5b2`)

### §2.1 Architecture overview

The framework operates two distinct accounting instruments — one **backward-looking** (already-extracted commons), one **forward-looking** (potential / claim-bearing commons). Both are governed by the same primitive equation `CS = RCV − B` (Cost Severance equals Residual Commons Value minus Bond posting). The two instruments differ in which side of the equation is being measured.

**CSD — Cost Severance Damages (backward-looking):**
- Question answered: *What was severed?*
- Measures CS that has already accumulated through past extraction.
- Anchors restitution claims (B₁ Restitution Bond — see §4 below).
- Empirical input: realized extraction history; realized commons-degradation; realized cost-bearer claims.
- Discount-rate posture: low / zero / negative (already-realized harm; reparations-economics traditions per Darity & Mullen 2020).

**RCV — Residual Commons Value (forward-looking):**
- Question answered: *What's left, and what would severing it more cost?*
- Measures commons-value that the extraction relationship has NOT yet captured / consumed / extinguished.
- Anchors foreclosure-prevention claims (B₂ Foreclosure Bond — see §4 below).
- Empirical input: replacement cost (Method 1 — see §3.1) + revealed preference (Method 2 — §3.2) + scarcity-adjusted option value (Method 3 — §3.3).
- Discount-rate posture: option-value-bearing; scarcity-adjusted (commons-finite Hotelling-like rents — see §5 Hotelling Identity).

**Why two instruments + one equation:** the framework's structural identity is *commons-governance extended to extraction* (per the commons-as-structural-identity rigor pass, commit `c4b09dc`). Past extraction (already-realized commons-loss) is governance-relevant for restitution. Pending extraction (un-realized commons-claim) is governance-relevant for foreclosure prevention. Same equation reads each direction; same Bond aggregate (B = B₁ + B₂) discharges both.

### §2.2 CSD–RCV correlation hypothesis (Open Insight #19)

A current open insight (logged in `alignment/commons_bonds_open_insights_v1.0.0.md` #19) is whether CSD and RCV correlate empirically across the 18 cases. Hypothesis: contexts with high CSD (large past extraction) tend to have low RCV (commons largely consumed); contexts with low CSD (early-stage extraction) tend to have high RCV (commons largely intact). If correlation holds, the two instruments triangulate a single commons-value reality from two empirical directions. If correlation doesn't hold, the two instruments are independent governance levers and the framework's two-instrument architecture is structurally vindicated.

**Open empirical work** (Block 4 validation): test correlation across Norway (high RCV, moderate CSD) + Appalachian coal (high CSD, low RCV) + opioid Appalachia (moderate CSD, dynamic RCV).

---

## §3. New section: Triangulated RCV Estimation (Three Ways of Counting)

**Status:** v0.0.5 NEW SECTION — drafted here; awaiting HTML integration.
**Source rigor passes:**
- Three Ways formal model: `commons_bonds_rigor_pass_2026-04-24_three_ways_rcv_formal_model_v1.0.0.md` (commit `1c8e4dd`)
- Triangulated RCV Estimation Ring 2: `commons_bonds_rigor_pass_2026-04-24_term_triangulated_rcv_estimation_v1.0.0.md` (commit `4f48c48`)

### §3.1 Method 1 — Replacement Cost

**Question:** What would it cost to engineer a substitute for the commons that extraction is consuming?

**Formal:** RCV_M1 = ∑ᵢ (replacement-cost per unit commons-i × commons-i remaining quantity)

**Worked-example anchor:** Habitability commons (atmospheric ecosystem) — direct-air-capture cost per ton CO₂ at engineering scale; substrate-engineering cost for life-support analogs (per Ch 7 asteroid-miner Habitability proxy).

**Strengths:** Most directly priced; smallest epistemic-ambition step.
**Limits:** Anchors floor only — replacement is rarely full functional substitute (see substitutability function rigor pass, commit `302dffb`). Underprices irreplaceable commons.

### §3.2 Method 2 — Revealed Preference (Norway-Style)

**Question:** What does a polity that explicitly chose NOT to extract reveal about commons-value?

**Formal:** RCV_M2 = (foregone-extraction value at observed restraint) + (preserved commons-quality observed) − (substitute-revenue path)

**Worked-example anchor:** Norway sovereign-wealth-fund + petroleum-conservation policy — Norwegian polity foregoes a known fraction of available extraction value, preserving long-horizon commons-claim. The foregone amount + preservation observed are the revealed-preference signal.

**Strengths:** Empirically grounded in actual policy choices (not hypothetical).
**Limits:** Norway-as-canonical-B2 carries epistemic-humility concern (Open Insight #14) — Norway is one polity; revealed-preference generalization needs cross-tradition sampling.

### §3.3 Method 3 — Scarcity-Adjusted Option Value

**Question:** What is the option value of preserving the commons in irreversibility-aware scarcity-aware terms?

**Formal (sketch — full derivation pending):**

```
RCV_M3 = V_option × scarcity_multiplier(σ) × irreversibility_premium(α)

where:
  V_option       = standard real-options option value (Dixit-Pindyck 1994)
  σ              = scarcity parameter (commons-stock / sustainable-flow ratio)
  α              = irreversibility parameter (probability commons cannot be restored
                   at any finite cost once extracted)
  scarcity_multiplier(σ): increasing in scarcity; bounded by Hotelling-rent
                           identity (see §5)
  irreversibility_premium(α): increasing in irreversibility; converges on infinity
                              as α → 1 (commons-extinction case)
```

**Worked-example anchors:**
- McDowell coal: low σ (coal stocks well-characterized), high α (mountain-top removal irreversible).
- Norwegian oil: moderate σ (proven reserves), moderate α (oil-field exhaustion partially-recoverable via secondary extraction).
- Asteroid mining: high σ (cosmic-scale stocks); α currently uncalibrated (planetary-protection unknowns).

**Strengths:** Incorporates two structural dimensions (scarcity + irreversibility) the other two methods can't price directly.
**Limits:** Requires σ and α calibration — sensitivity analysis needed (Open Insight #20).

### §3.4 Triangulation logic

The three methods price the same commons-claim from three independent directions:
- M1 prices *substitution* — what would replace the commons cost?
- M2 prices *revealed restraint* — what does observed forgoing reveal?
- M3 prices *option-bearing scarcity* — what is the commons worth when irreversibility is honored?

**Triangulation rule:** RCV estimate is the convergence range across M1, M2, M3 with documented divergences. Where the three methods agree within a tight range, RCV estimate is well-supported. Where they diverge widely, the divergence itself is empirically informative — surfacing what feature of the commons each method captures and which features it misses.

**Reporting discipline:** every RCV estimate published under the framework reports all three methods individually + the convergence range + identified divergence sources. No single-method RCV claim has standing.

---

## §4. New section: B = B₁ + B₂ decomposition + naming

**Status:** v0.0.5 NEW SECTION — drafted here; awaiting HTML integration.
**Source rigor passes:**
- B = B₁ + B₂ decomposition: `commons_bonds_rigor_pass_2026-04-24_b1_b2_decomposition_v1.0.0.md` (commit `ab24a8e`)
- B₁ + B₂ naming (Restitution + Foreclosure): `commons_bonds_rigor_pass_2026-04-24_b1_b2_naming_v1.0.0.md` (commit `8e6a5b2`)

### §4.1 The decomposition

`B = B₁ + B₂`

where:
- **B₁ — Restitution Bond.** The bond posting that discharges accumulated CSD (already-realized commons-loss). Restitution-economics lineage (Darity & Mullen 2020 reparations economics; Hicks 1932 compensation principle in cross-context-translation form). Posted by extractor against historical extraction-portfolio.
- **B₂ — Foreclosure Bond.** The bond posting that discharges potential CS (forward-looking commons-loss claim). Posted against ongoing or proposed extraction. Foreclosure-cost lineage (term-pair coherent with Foreclosure Cost C₁ in 8-tier).

### §4.2 Naming-rigor outcome

Earlier working labels included "Reparations Bond" for B₁. Naming-rigor pass on 2026-04-24 (commit `8e6a5b2`) selected **Restitution Bond** over Reparations Bond for the following reasons:

1. **Cross-political-tradition adoption breadth.** "Reparations" carries US-political-loading that narrows audience. "Restitution" carries broader cross-tradition adoption (legal-scholarship; civil-law; international-law; classical-philosophy).
2. **Per Option C' political-philosophical-accommodation discipline** (10-list dissolution rigor pass): the framework should not legislate political-tradition-specific terminology where structurally-broader alternatives exist with equivalent technical fit.
3. **Term-pair coherence:** Restitution Bond + Foreclosure Bond reads as natural pair (both bonds against commons-loss, one backward-looking, one forward-looking). Reparations Bond + Foreclosure Bond reads as non-parallel categories.

**B₂ — Foreclosure Bond** was selected for term-pair coherence with Foreclosure Cost C₁ in the 8-tier decomposition (the cost-severance tier the bond is posted against).

### §4.3 Independence note

B₁ and B₂ are **structurally independent** — a context with high CSD but low forward-looking RCV (e.g., post-mining Appalachian sites where commons largely already lost) carries high B₁ obligation but low B₂ obligation. A context with low CSD but high RCV (e.g., asteroid mining proposed but not yet executed) carries low B₁ obligation but high B₂ obligation. The aggregate B captures the total bond posture; the decomposition captures the temporal structure of the obligation.

---

## §5. New section: Hotelling Identity (extension of Hotelling 1931)

**Status:** v0.0.5 NEW SECTION — drafted here; awaiting HTML integration.
**Source rigor pass:** `commons_bonds_rigor_pass_2026-04-24_term_hotelling_identity_v1.0.0.md` (commit `5b8ff42`)

### §5.1 Hotelling 1931 — the part that's Hotelling's

Hotelling (1931, "The Economics of Exhaustible Resources," *Journal of Political Economy*) established that for an exhaustible resource extracted competitively under a discount rate r, the resource rent (price minus marginal extraction cost) must rise at rate r. Otherwise the owner would prefer to extract earlier (if rent rises faster) or later (if slower). This is the **Hotelling rent rule** — a foundational result in resource economics.

Hotelling's framing assumes:
- Resource is exhaustible (finite stock).
- Owner is private (extracts to maximize NPV of rent).
- Cost is private extraction-cost (not commons-loss-cost).

### §5.2 What the Commons Bonds framework adds (the "Identity" extension)

The Commons Bonds framework extends Hotelling 1931 with the following identity:

**Hotelling Identity:**

```
RCV per unit − Hotelling rent per unit = CS per unit
```

In words: *the residual commons value per unit of extraction, minus the standard Hotelling rent per unit, equals the cost severance per unit*.

**What this surfaces:** when extraction prices the standard Hotelling rent (i.e., honors private resource-economics rent-rules), the *excess* residual commons value beyond that rent is precisely the cost-severance — the commons-extraction cost the extractor is not paying. The Hotelling rent prices private exhaustibility; the framework prices commons-extraction. The difference is the asymmetry the framework names.

**Worked-example anchor:** Norwegian oil. Norway prices Hotelling rent appropriately (sovereign-fund accumulation; depletion-rate discipline). The Hotelling Identity asks: even with proper Hotelling-rent pricing, what's the residual commons value Norway preserves through its restraint? Answer: the difference between the Norwegian-fund's accumulation and the full RCV (per Method 2 revealed preference, §3.2). That difference is the commons-loss Norway is NOT incurring — and thus also reveals what other extraction contexts ARE incurring when they price Hotelling rent only.

### §5.3 Citation discipline (M12 intellectual honesty)

Per M12 module + Working Principle #6: when the framework references Hotelling Identity, the citation discipline is:

> The Hotelling Identity (RCV − Hotelling rent = CS, where Hotelling rent is the standard rent rule from Hotelling 1931) extends Hotelling's exhaustible-resource economics to commons-extraction contexts. Hotelling's contribution: the rent rule for private exhaustible resources. The Commons Bonds framework's contribution: the identity extension showing that commons-extraction cost is precisely the residual value beyond standard Hotelling rent.

This positioning:
- Acknowledges Hotelling 1931 as foundational.
- Specifies what the framework extends and how (the identity addition).
- Avoids overclaiming: Hotelling's rent rule is Hotelling's; the identity-form extension is the framework's.

---

## §6. New section: CIT (Commons Inversion Test) — formal spec

**Status:** v0.0.5 NEW SECTION — drafted here; awaiting HTML integration.
**Source rigor passes:**
- CIT rename: `commons_bonds_rigor_pass_2026-04-24_term_cit_rename_v1.0.0.md` (commit `b294c79`)
- Four Gates cluster: `commons_bonds_rigor_pass_2026-04-24_four_gates_cluster_v1.0.0.md` (commit `d188e6f`)
- Worked examples: `core/methodology/cit_examples_v1_0_0.md` (commit `9ab3dc2`)

### §6.1 Two sub-forms

**Commons-Absence Inversion (CAI).** Given a cost claim that names a commons, ask: *would the extraction price differently if the commons claim did not exist at all?* If yes → cost claim is commons-grounded. If no → cost claim is private-property externality (different framework applies).

**Commons-Consumption Inversion (CCI).** Given a commons-grounded cost claim, ask: *would the extraction price differently if the commons were inexhaustible / self-restoring at zero marginal cost?* If yes → cost claim is consumption-of-finite-commons (Cost Severance proper). If no → cost claim is coordination-of-mutually-acceptable-use (Ostrom-tradition commons-management; framework's CS does not apply).

The two sub-forms run in sequence: CAI first (is this commons-grounded at all?), then CCI (is this consumption-grounded?). Only claims passing both qualify as Cost Severance.

### §6.2 Four Gates admission apparatus

Per the Four Gates cluster rigor pass, a commons-extraction-cost claim is admitted to the framework's CS accounting if and only if it passes all four gates:

1. **CIT (Commons Inversion Test)** — passes both CAI and CCI sub-forms.
2. **Units Consistency** — claim's units match the underlying commons's units (avoids unit-conflation across heterogeneous commons categories).
3. **Boundedness** — claim has finite bounds (rules out unbounded "infinity" claims that would dominate any aggregation).
4. **Independence** — claim is not double-counted across overlapping commons categories (the merger / primitiveness discipline from earlier Path F — re-cast under the Independence gate).

**Gate-test asymmetry:** gates 1 + 2 + 3 + 4 are tests *of* a candidate cost claim. They are NOT *conditions* for what counts as a commons (Option C' political-philosophical-accommodation: the candidate commons comes from the political-philosophical tradition, not from the framework's gates). The gates filter cost *claims* against established commons; they do not filter what counts as a *commons*.

### §6.3 Worked examples

Seven canonical CIT applications worked end-to-end through the Four Gates are documented in `core/methodology/cit_examples_v1_0_0.md`:
- McDowell coal (Spatial + Habitability + Ecosystem activations)
- Commute trade (Temporal + Cohesion activations)
- Norwegian oil (Habitability + Ecosystem; passes Hotelling-Identity test)
- 2008 financial crisis (Institutional + Political activations)
- Asteroid mining (Habitability + Spatial + Cosmic-physical-law candidate)
- Healthcare end-of-life (Temporal + Autonomy + Kindred activations)
- Opioid Appalachia (Epistemic + Autonomy + Cohesion activations)

---

## §7. New section: Asymmetric Regret Rule (ARR — renamed from ARP/RD)

**Status:** v0.0.5 NEW SECTION — drafted here; awaiting HTML integration.
**Source rigor pass:** `commons_bonds_rigor_pass_2026-04-24_arp_rename_v1.0.0.md` (commit `b8b62e3` — same-day flip from initial Reversibility Default)

### §7.1 The rule

When facing a decision whose error has asymmetric regret structure — where one direction of error produces small recoverable cost and the other direction produces large irreversible cost — the framework's decision rule is to choose the direction with smaller maximum regret.

### §7.2 Lineage acknowledgment (M12 intellectual honesty)

ARR draws on:
- **Savage 1951** ("The Theory of Statistical Decision," *JASA*) — minimax-regret decision theory foundations.
- **Loomes & Sugden 1982** ("Regret Theory: An Alternative Theory of Rational Choice under Uncertainty," *Economic Journal*) — regret-based individual decision theory.
- **Lempert, Popper & Bankes 2003** (*Shaping the Next One Hundred Years: New Methods for Quantitative, Long-Term Policy Analysis*) — robust-decision-making under deep uncertainty.

The framework's contribution: applying minimax-regret discipline specifically to commons-extraction decisions where one direction of regret is *commons-extinction* (irreversible by definition under the CCI sub-form). The asymmetry — commons-loss is structurally irreversible; commons-preservation can be revisited — converts a generic minimax-regret rule into a commons-specific maximum-protective rule.

### §7.3 Same-day-flip lesson (from rename rigor pass)

Initial v0.0.4-era working name was "Reversibility Default" (RD). Same-day rigor flip on 2026-04-24 surfaced an M6 academic-rigor concern: ARR has stronger M6 direct lineage in name (regret theory is established academic terminology); RD requires footnote-dependency to surface its decision-theory lineage. ARR was selected for direct-name-visibility.

**Working Principle #5 corollary** (added 2026-04-24): when M5 (cross-political-tradition adoption) and M6 (academic-rigor lineage) tradeoffs appear close in a naming decision, foreground M6 direct-name-visibility EXPLICITLY in the executive summary recommendation. The earlier RD recommendation had buried the M6 cost; this flip surfaced it.

---

## §8. New section: Working Principles + Open Insights cross-reference

**Status:** v0.0.5 NEW SECTION — drafted here; awaiting HTML integration.

The framework now codifies six **Working Principles** (in `alignment/commons_bonds_working_principles_v1.0.0.md`):

1. **Naming discipline** — Corollary A: "no name is locked until ratified through full naming rigor pass." Corollary B (added 2026-04-24): "when a working name has carried framework reasoning for >24 hours, treat its rename as a Tier-1 update event with cascade audit."
2. **Bibliography additions discipline** — load-bearing-on-ratified-decisions rule (auto-add); pending-candidate rule (queue).
3. **Terminology regression check** — on every read/edit, scan for stale terminology; surface findings inline.
4. **Tier-1 update header pattern** — when canonical docs need supersession framing without full rewrite, add Tier-1 update header at top citing source rigor passes; preserve content; defer full rewrite to Phase B.
5. **Context-flipping rules** (added 2026-04-24) — when a same-day flip occurs (e.g., RD → ARR), the flip rigor pass + commit must explicitly surface what was missed in the original recommendation; lessons captured prevent recurrence.
6. **M12 Intellectual Honesty audit** (added 2026-04-24) — Corollary D 7-level action ladder for prior-art findings: (1) original-coinage / (2) independent-rediscovery-acknowledged / (3) lexical-collision-disambiguated / (4) collision-rename-required / (5) prior-art-citation-required / (6) extension-positioning-required / (7) borrowed-term-acknowledged.

The framework's current **Open Insights** queue (in `alignment/commons_bonds_open_insights_v1.0.0.md`) includes:
- #14 — Norway-as-canonical-B2 epistemic-humility (cross-tradition sampling needed).
- #16 — CIT two-sub-forms refinement (CAI + CCI distinct gate-runs).
- #17 — Option C' political-philosophical-accommodation discipline tracking.
- #18 — Autonomy-as-commons placement (under Pettit / Skinner republican tradition).
- #19 — CSD–RCV correlation hypothesis (Block 4 validation).
- #20 — Sensitivity analysis execution (σ + α + V_option in Method 3).

---

## §9. Cross-references

| Document | Relationship |
|---|---|
| `core/glossary/commons_bonds_updated_glossary_v3.html` | Canonical glossary v3 (commit `5123da6`) — Ring 1 / Ring 2 / Architecture / Commons Categories / Retired Terms |
| `core/terms/terms_index.md` | Provenance source-of-truth for every term's origin, status, retire/rename history |
| `core/dimensions/commons_bonds_abundance_dimensions_v1_3_0.md` | Methodology doc v1.4.0 (commit `00e877b`) — Tier-1 reframed for Option C' commons-as-structural-identity |
| `tools/commons_bonds_rigor_protocol_v2.2.0.md` | Rigor protocol v2.4.0 (commit `4304cb5`) — AIT→CIT swept; M12 module preserved |
| `core/methodology/cit_examples_v1_0_0.md` | Seven worked CIT examples through Four Gates |
| `research/literature/bibliography.md` | Bibliography (commit `f96158a`) — load-bearing citations for all v0.0.5 new sections |
| `alignment/commons_bonds_working_principles_v1.0.0.md` | Working Principles 1-6 |
| `alignment/commons_bonds_open_insights_v1.0.0.md` | Open Insights queue (#10-#20) |
| `alignment/sessions/commons-bonds-session-handoff-2026-04-24_v1.42.0.html` | Session handoff capturing the day's ~50+ commits |

---

## §10. Phase B materialization plan

The HTML integration of §2-§7 new sections is deferred to Phase B (post-coursework). Materialization order:

1. §2 Two-Instrument Architecture (CSD + RCV) — anchors the rest.
2. §6 CIT formal spec + Four Gates — required upstream of §3.
3. §3 Triangulated RCV Estimation — depends on §2 + §6.
4. §4 B = B₁ + B₂ decomposition — depends on §2.
5. §5 Hotelling Identity — extends §3.3 Method 3.
6. §7 ARR — independent of §2-§5; can land any time.
7. §8 Working Principles + Open Insights — closing cross-reference section.

**Until Phase B materialization:** this supplement file is canonical-source-of-truth pointer for v0.0.5 new content. The HTML carries v0.0.4 baseline content swept in place per §1; supplement carries v0.0.5 delta.

---

*End of Technical Appendix v0.0.5 Supplement. Phase B materialization through full HTML rewrite pending.*
