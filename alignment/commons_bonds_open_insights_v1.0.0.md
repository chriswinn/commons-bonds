# Commons Bonds — Open Insights Log

**Version:** 1.0.0
**Established:** 2026-04-24
**Purpose:** persistent capture of insights, observations, and concerns raised during working sessions that don't yet have a ratified resolution. Replaces the prior pattern where valuable observations surfaced in conversation could be lost between sessions unless the author happened to ask the right question next time.

---

## §0. Why this file exists

Per author direction 2026-04-24: *"I want you to always feel you have the freedom to think & express your ideas so we can work more collaboratively vs. me asking the right questions. You had real valuable insights into the testing suite revisions that would have been lost if I didn't explicitly ask for them, let's not make that a possible mistake again."*

The Open Insights Log is the mechanism for preventing that loss. Every insight raised by either party during a session — whether acted on immediately, deferred, rejected, or pending decision — lands here with a status and a traceable link to follow-up work. The discipline operates at two levels:

1. **Capture.** Whenever a non-trivial insight surfaces (framework-structure observation, vocabulary concern, option-space gap, cross-cutting consistency issue, meta-question about method), it gets logged here before the session ends.
2. **Review.** Every logged insight carries a corresponding todo item (*Review Open Insight #N*) so it is not lost in the backlog. The todo gets worked until the insight is resolved, deferred with explicit rationale, or closed-rejected.

New insights automatically get added to the todo list in both states: one entry for **raising** (surface to the author with context) if not yet raised, and one for **reviewing** (decide action) once raised. The "automatic" discipline is enforced by me — whenever I notice an insight, I log it here and add the todos, not at end-of-session but at the moment of noticing.

---

## §1. Format for each insight

```markdown
### Insight #N — <short title>

- **Raised:** YYYY-MM-DD by <me / author / collaborative>
- **Status:** <raised | under-review | addressed | deferred | closed-ratified | closed-rejected>
- **Category:** <framework-structure | vocabulary | method | craft | publishing | meta>
- **Content:** <the insight itself, in enough detail to act on>
- **Why it matters:** <consequence if not addressed / value if addressed>
- **Proposed resolution:** <what acting on this would entail>
- **Dependencies / Links:** <rigor passes, decisions, commits, handoffs, other insights>
- **Todo link:** <todo item that tracks this insight through to resolution>
```

### Status definitions

| Status | Meaning |
|---|---|
| `raised` | Logged but not yet reviewed by author; awaiting engagement. |
| `under-review` | Author engaged; rigor pass or decision work in progress. |
| `addressed` | Concrete action has begun (rigor pass written, decision drafted, fix applied). |
| `deferred` | Acknowledged but intentionally not acted on now; carries reason + trigger for re-review. |
| `closed-ratified` | Author ratified action taken; insight absorbed into framework. |
| `closed-rejected` | Author considered and rejected; carries reason for rejection. |

---

## §2. Open insights

### Insight #1 — Framework may be naming too many things (vocabulary footprint)

- **Raised:** 2026-04-24 by me
- **Status:** **closed-ratified 2026-04-26** — vocabulary-footprint meta-pass executed and operationalized; tiered-ring architecture ratified; Ring-1 / Ring-2 / retired-term partition completed via subsequent individual rigor passes + integrated synthesis.
- **Category:** vocabulary · meta
- **Content:** The framework originally carried ~20+ named terms (cost severance, severed cost, value capture, cost bearing, RCV, CS, AIT, IPG, CSG, FGC, foreclosure cost, externality tail, substitutability function, accountability bond, the ten abundances, the four gates, context, dimensions, abundances, variable/cost, and more). Each named concept competes for reader adoption bandwidth. The success criterion favors sharpness + concision; proliferation works against that.
- **Closure (2026-04-26):** Closed via the cumulative work of:
  - **Vocabulary-footprint meta-pass** (`tools/rigor-passes/commons_bonds_rigor_pass_2026-04-24_vocabulary_footprint_meta_v1.0.0.md`, commit `46600bc`) — established Ring-1 / Ring-2 / Ring-3 architecture; identified retirement candidates; reshaped the rigor-pass queue from 31 individual passes to ~10-14 cluster + targeted individual passes
  - **Ring-1 individual rigor passes** (Cost Severance + Severed Cost + Value Extraction + CIT + RCV + Cᵢ + Commons Bonds) — each ratified individually
  - **Synthesis Ring-1 rigor pass** (`commons_bonds_rigor_pass_2026-04-24_synthesis_ring1_terms_v1.0.0.md`) — verdict: "All four standalone verdicts hold under synthesis. The Ring-1 vocabulary architecture is COHERENT and PASSES extreme rigor as an integrated whole"
  - **Ring-1 full integrated rigor pass** (`commons_bonds_rigor_pass_2026-04-24_ring1_full_integrated_v1.0.0.md`) — verdict: "ALL 7 RING-1 TERMS PASS INTEGRATED RIGOR UNCONDITIONALLY"
  - **Subsequent retirements** of Value Capture (→ Value Extraction; sweep executed 2026-04-26 commit `90f9c3f`); Spatial Cost Severance + Temporal Cost Severance (re-examined and reframed); CSG (parsimony retirement); FGC (8-tier-vintage retirement); Universality Test; AIT (→ CIT)
- **Vocabulary footprint as of 2026-04-26:** 7 Ring-1 terms (Cost Severance · Severed Cost · Value Extraction · CIT · RCV · Cᵢ · Commons Bonds) + ~10-12 Ring-2 operational terms + retired-term provenance preserved in `core/terms/terms_index.md`. Footprint substantially reduced from original ~20+; rigor backing complete.
- **Dependencies / Links:** vocabulary-footprint meta-pass + 7 Ring-1 individual passes + synthesis + integrated passes; `core/terms/terms_index.md` for current ring-membership provenance.
- **Todo link:** N/A (closed).

### Insight #2 — Gate names are inconsistent in convention

- **Raised:** 2026-04-24 by me
- **Status:** **closed-ratified 2026-04-26** — option space exhaustively tested across two cluster passes; cohort confirmed with naming asymmetry acknowledged as load-bearing structural distinction.
- **Category:** vocabulary · framework-structure
- **Content:** The four gates' names follow what initially looked like inconsistent conventions. Gate 1 = acronym (CIT, renamed from AIT). Gate 2 = compound noun phrase (Units Consistency, T2-resolved from "Dimensional Consistency"). Gate 3 = single word (Boundedness). Gate 4 = single word (Independence). The original concern: a well-designed naming cohort would pick one convention and apply it uniformly; the drift suggested opportunistic rather than cohort-coordinated naming.
- **Resolution path (2026-04-24 → 2026-04-26):** Two cluster rigor passes tested the option space exhaustively:
  1. `tools/rigor-passes/commons_bonds_rigor_pass_2026-04-24_four_gates_cluster_v1.0.0.md` — tested cohort-level renaming for parallelism (Option B with all-test-suffix and all-property-noun sub-options), cohort restructuring (Options C collapse 4→3 and D split 4→5), and status-quo confirmation (Option A). Option A RECOMMENDED on structural-asymmetry grounds: CIT is a methodological TEST (action; methodology); the other three are mathematical CONDITIONS (property; state). Naming asymmetry honors the structural distinction; uniform naming would falsely conflate kinds.
  2. `tools/rigor-passes/commons_bonds_rigor_pass_2026-04-26_term_consistency_gate_rename_v1.0.0.md` — tested the previously-untested single-gate rename (Gate 2 from "Units Consistency" → "Consistency"), plus surfaced an alternative single-word path (Option C — "Commensurability"). Option B (RETAIN "Units Consistency") RECOMMENDED on specificity + M6 + M12 + §22.4 + decisive reader-inference test.
- **Ratified decision (2026-04-26, Chris Winn):** Option A from `four_gates_cluster` (carried forward via the Gate-2-rename pass's ratification). Cohort confirmed with naming asymmetry preserved as load-bearing.
- **Why the cohort question dissolved rather than resolved within original framing:** The original concern presupposed the cohort *should* be uniform. The rigor pass found this premise wrong: CIT-vs-others is a real structural asymmetry (test vs condition; action vs state); naming should honor it. The cohort-uniformity gain from any rename is small and non-load-bearing; the structural-asymmetry argument applies regardless of which specific renaming is proposed. Together the two passes cover: cohort-level rename (rejected); cohort restructuring (rejected); single-gate rename to single-word property-noun (rejected on specificity); single-gate rename with units-meaning preservation via "Commensurability" (defensible-but-not-preferred); status quo (ratified).
- **Implementation status:** No sweep needed. The verdict was operationally adopted across the framework (terms_index Four Gates record CURRENT; Tech Appendix supplement §6.2 uses CIT + Units Consistency + Boundedness + Independence; glossary v3 reflects the cohort) before formal ratification. The sweep had already been done; only the formal ratification statement was outstanding.
- **Dependencies / Links:** Relates to Insight #1 (vocabulary footprint — addressed by meta-pass). Relates to T2 terminology decision (Dimensional → Units Consistency — resolved in `four_gates_cluster`). Cross-reference to `four_gates_cluster_v1.0.0.md` §9 + `term_consistency_gate_rename_v1.0.0.md` §20 for full ratification provenance.
- **Todo link:** N/A (closed).

### Insight #3 — "Severance" vocabulary cluster needs cluster-level internal-consistency review

- **Raised:** 2026-04-24 by me
- **Status:** **closed-ratified 2026-04-26** — cluster tested at three levels (head-to-head + synthesis + integrated); cluster verdict CLEAN.
- **Category:** vocabulary
- **Content:** The original concern was that "Cost Severance" (mechanism) + "Severed Cost" (result) + "Spatial Cost Severance" (variant) + "Temporal Cost Severance" (variant) + "Value Capture" (causal-event term) + related cluster terms are tightly interconnected; testing them individually in sequence might produce internally inconsistent verdicts.
- **Closure (2026-04-26):** Closed via the cumulative work of multiple cluster-level rigor passes:
  - **Vocabulary-footprint meta-pass** (`commons_bonds_rigor_pass_2026-04-24_vocabulary_footprint_meta_v1.0.0.md`) — explicitly addressed Insight #3 and identified the severance cluster as cluster-level pass C1
  - **Cost Severance vs Severed Cost head-to-head** (`commons_bonds_rigor_pass_2026-04-24_term_cost_severance_vs_severed_cost_v1.0.0.md`) — tests two cluster members head-to-head; verdict: Option A (keep both with role discipline)
  - **Cost Severance collision rigor pass** (`commons_bonds_rigor_pass_2026-04-24_term_cost_severance_collision_v1.0.0.md`) — Option C (rhetorical bridge) ratified
  - **Value Capture vs Value Extraction rigor pass** (`commons_bonds_rigor_pass_2026-04-24_term_value_capture_vs_extraction_v1.0.0.md`) — Option B (Value Extraction) ratified; Value Capture retired
  - **Spatial Cost Severance re-examination** + **Temporal Cost Severance** + **Intergenerational Cost Severance** rigor passes — variants reframed as lowercase-descriptive-phrase compositions of "cost severance" (not capitalized proper-noun compounds)
  - **Synthesis Ring-1 rigor pass** — verdict: "All four standalone verdicts hold under synthesis. The Ring-1 vocabulary architecture is COHERENT and PASSES extreme rigor as an integrated whole"
  - **Ring-1 full integrated rigor pass** — verdict: "ALL 7 RING-1 TERMS PASS INTEGRATED RIGOR UNCONDITIONALLY"
- **Cluster as of 2026-04-26:** Cost Severance + Severed Cost + Value Extraction (Ring 1; cluster-coherent). Spatial / Temporal / Intergenerational cost severance retired as proper-noun-compounds; preserved as lowercase descriptive phrases composed from "cost severance." Value Capture retired (sweep executed commit `90f9c3f`).
- **Dependencies / Links:** see closure provenance above; cluster-level rigor work is complete.
- **Todo link:** N/A (closed).

### Insight #4 — "Commons Bonds" (book title + framework name) has not been through the current rigor suite

- **Raised:** 2026-04-24 by me
- **Status:** closed-ratified 2026-04-24 — Commons Bonds name rigor-tested + ratified
- **Category:** vocabulary · framework-structure
- **Content:** "Commons Bonds" is the book title and the framework's identifying name. It has been in use throughout the project but has not been run through the rigor protocol v2.2.0 suite. Given that (a) the framework's structure has materially resettled this session (Path F + tier dissolution + macro-grouping Option A), and (b) "Commons Bonds" is arguably the most load-bearing single vocabulary item (readers encounter it first; editors and librarians index against it), running rigor on the name itself is overdue.
- **Why it matters:** If the name doesn't survive current-state rigor, changing it is cheaper now than after publication. If it survives cleanly, the rigor pass itself becomes publication-defense material.
- **Resolution (2026-04-24):** Full extreme-rigor pass executed (`tools/rigor-passes/commons_bonds_rigor_pass_2026-04-24_term_commons_bonds_v1.0.0.md`, commit `be6646f`). Verdict: Option A PASSES UNCONDITIONALLY. Polysemy confirmed as load-bearing (three meanings: accountability bonds / relational bonds / structural bonds — each does framework-serving work). 7 rename candidates tested; none improves on decisive axes. Reinforced by full Ring-1 integrated rigor pass (commit `d4c4be4`) showing Commons Bonds pairs coherently with every other Ring-1 term. Batch-ratified 2026-04-24 by Chris Winn.
- **Dependencies / Links:** Commons Bonds CURRENT Ring-1 record in `core/terms/terms_index.md` §4. Rigor passes at `tools/rigor-passes/`.
- **Todo link:** N/A (closed).

### Insight #5 — Glossary v2 has a Foreclosure Cost duplicate (pre-existing hygiene issue)

- **Raised:** 2026-04-24 by me
- **Status:** **closed-ratified 2026-04-26** — glossary v3 was built from scratch with M12 audit per term; structural audit complete.
- **Category:** vocabulary · craft
- **Content:** "Foreclosure Cost" appeared twice in glossary v2: once under Mathematical and Measurement Terms, once as Tier 4. The duplicate resolved automatically when tier dissolution happened, but the original concern was broader: the glossary v2 → v3 bump might need more than a rename sweep — a full structural walk-through to catch other duplicates or stale entries.
- **Closure (2026-04-26):** Closed via the cumulative work of:
  - **M12 intellectual-honesty sweep** (`tools/rigor-passes/commons_bonds_rigor_pass_2026-04-24_m12_intellectual_honesty_sweep_v1.0.0.md`, commit `c07a7c1`) — comprehensive M12 sweep across **every term currently in `core/terms/terms_index.md` plus every term referenced in `core/glossary/commons_bonds_updated_glossary_v3.html`**. Each term verified against M12 Corollary D 7-level action ladder. Surfaced + corrected v1.43.0 misframing on CSG; comprehensive structural audit completed.
  - **Glossary v3 build** (commit `5123da6`) — glossary v3 was constructed from scratch with provenance discipline, not as a rename sweep over v2. Each entry was created with its current ratified status + rigor-pass cross-reference. The "structural walk-through" the original insight asked for IS the v3 build itself.
  - **Glossary v2** (`core/glossary/commons_bonds_updated_glossary_v2.html`) — retired; preserved as lineage record. The Foreclosure Cost duplicate that triggered the insight is in v2 only and does not propagate to v3.
- **Glossary as of 2026-04-26:** v3 is current canonical (commit `5123da6`); covers Ring-1 / Ring-2 / Architecture / Commons Categories / Retired Terms with provenance per entry. Cross-checked by M12 sweep against terms_index. No outstanding structural-audit items.
- **Dependencies / Links:** M12 sweep + glossary v3 build; `core/glossary/commons_bonds_updated_glossary_v3.html` (current canonical); `core/terms/terms_index.md` (cross-referenced by every glossary entry).
- **Todo link:** N/A (closed).

### Insight #6 — Running 31 individual rigor passes may be the wrong structural approach

- **Raised:** 2026-04-24 by me
- **Status:** **closed-ratified 2026-04-26** — vocabulary-footprint meta-pass executed; queue reshaped from 31 individual passes to ~10-14 cluster + targeted individual passes; reshaped queue worked through to completion.
- **Category:** method · meta
- **Content:** The initial 31-pass queue loaded after author's "full rigor on every term" ratification assumed each term was independently testable. Many terms are tightly coupled (severance cluster, gate cohort, variable-vs-cost affecting dimension-vs-abundance). Individual-pass approach reproduces findings + misses cluster-level insights.
- **Closure (2026-04-26):** Closed via:
  - **Vocabulary-footprint meta-pass** (`commons_bonds_rigor_pass_2026-04-24_vocabulary_footprint_meta_v1.0.0.md`) — explicitly addressed Insight #6; reshaped queue from 31 → ~10-14 passes; identified cluster-level passes (severance cluster C1; four gates cluster C2; tier-dissolution C3); identified retirement candidates; identified terms warranting individual deep rigor.
  - **Reshaped queue executed:** ~10-14 individual + cluster + integrated rigor passes ran across 2026-04-24 through 2026-04-26. Examples: Ring-1 individual passes (Cost Severance + Severed Cost + Value Extraction + AIT/CIT + RCV + Cᵢ + Commons Bonds); cluster passes (Four Gates cluster; severance cluster via head-to-head + synthesis + integrated); Ring-2 passes (Accountability Bond, CSD, Hotelling Identity, Substitutability Function, Asymmetric Regret Rule rename, Triangulated RCV Estimation, Externality Tail, etc.); meta-passes (Path F variable-addability, commons-as-structural-identity, 10-commons-list dissolution, macro-grouping, tier-reframing); synthesis (synthesis_ring1_terms; ring1_full_integrated); per-cluster (academic_rigor_full_test; m12_intellectual_honesty_sweep; three_ways_rcv_formal_model).
- **Method outcome:** the meta-pass approach was decisively validated. Cluster passes did substantially more work per unit effort than 31 individual passes would have. The 47 rigor-pass files in `tools/rigor-passes/` represent the executed reshaped queue + supplements; the queue is substantially complete.
- **Dependencies / Links:** Addresses Insights #1 (closed) + #2 (closed) + #3 (closed) structurally. The meta-pass approach is now the standing methodology for cluster-level rigor work.
- **Todo link:** N/A (closed).

### Insight #7 — Value Capture vs Value Extraction terminology decision

- **Raised:** 2026-04-24 by Chris Winn (pointed out Value Capture OR Value Extraction as the causal event that produces Cost Severance)
- **Status:** **closed-ratified 2026-04-24** (rigor passes complete + ratified) · **sweep executed 2026-04-26**
- **Category:** vocabulary · framework-structure
- **Content:** The framework originally used "Value Capture" (16 proper-noun refs + 42+ concept refs in chapter drafts). Author flagged that "Value Extraction" was an alternative candidate for the same causal event. Two rigor passes ran 2026-04-24:
  1. `tools/rigor-passes/commons_bonds_rigor_pass_2026-04-24_term_value_capture_vs_extraction_v1.0.0.md` — head-to-head + causal-chain-bridge testing across full option space (Capture / Extraction / both-interchangeable / Value Appropriation / Value Severance / Accumulation by Dispossession only)
  2. `tools/rigor-passes/commons_bonds_rigor_pass_2026-04-24_term_value_extraction_standalone_v1.0.0.md` — standalone rigor on Value Extraction with v1.1.0 addendum on Mazzucato 2018 prior-art finding + canonical citation form
- **Resolution (2026-04-24, Chris Winn):**
  - **Option B — Value Extraction as sole causal-event term — RATIFIED**
  - **Value Capture RETIRED** as duplicative (per author's own admission that the two were interchangeable)
  - **Value Extraction promoted to Ring 1**
  - **Mazzucato 2018 citation discipline + Harvey 2003 lineage** ratified per v1.1.0 addendum; canonical citation form drafted
- **Why it matters:** This is the causal-event term in the framework's three-concept chain (Value Extraction → Cost Severance → Severed Cost). Decisive test was the causal-chain-bridge: extraction IS the severance mechanism (separation-from-source semantics pairs with Cost Severance's severance-from-capturer semantics); capture would have required reader inference to bridge.
- **Sweep execution (2026-04-26):** Phase A3 sweep completed in commit `90f9c3f`. Chapter drafts (Ch 2 / Ch 4 / Ch 5 GuidanceDoc / Ch 7 draft + GuidanceDoc / Ch 10) + `core/methodology/cit_examples_v1_0_0.md` swept. Mazzucato + Harvey lineage citation paragraph added at Ch 2 first-use of Value Extraction (AUTHOR ZONE annotation; pending author register-review). Tech Appendix dedicated Mazzucato lineage footnote / §G subsection deferred to Insight #21 dedicated session per recommended workflow. Provenance preserved in `core/terms/terms_index.md` + retired glossary v2.
- **Dependencies / Links:** Relates to Insight #3 (severance cluster internal consistency) — the causal-event term resolution is now an INPUT to any cluster pass that runs, not an open question. Relates to Insight #21 (Tech Appendix dedicated session) for Mazzucato lineage footnote integration.
- **Todo link:** N/A (closed; sweep executed).

### Insight #9 — Framework as decision-time severance-detection tool (not just ex-post analysis) — CLOSED-RATIFIED 2026-04-30

- **Raised:** 2026-04-24 by Chris Winn (via the commute-story conversation) + me (naming the pattern)
- **Status:** **closed-ratified 2026-04-30 (Chris Winn) — verdict (b) at the external layer + rich internal scaffolding for everything else.** Two-layer reframe surfaced during Thread δ surfacing 2026-04-30: *"hmm, I think perhaps I should have asked the question differently as what we are archiving isn't necessarily going to end up as end reader, publisher, literary agent facing. So I guess a better question is what should be internal vs external, then apply the earlier question to the external facing material."* The two-layer discipline generalized into Working Principle #10 (Two-layer content origination discipline; ratified same-day).
- **Category:** framework-structure · book-scope · application-domain
- **Content:** The book's framing to date has centered on *ex-post* cost-severance analysis — pricing what McDowell County bore after extraction, what Deepwater Horizon left behind, what Libby lost to asbestos. But the commute-story conversation surfaced a distinct and arguably more practically-useful application: **the framework as a decision-time tool.** At the moment a decision is being made (signing an apartment lease, accepting a job, consenting to a medical treatment, purchasing a house, pivoting careers), informal CIT + informal RCV can surface costs the decision-maker would otherwise miss. Chris's commute story demonstrated this: *"the quick mental what would a day in the life of living here and getting to/from my office be like/entail"* is informal CIT (testing whether the cost is scarcity-grounded in time) + informal RCV (mentally multiplying hours × days × year). The framework doesn't need math-fluent readers to be useful at decision-time; it needs readers who know the two-step (test for scarcity-grounding → compute informal cost over the affected horizon).
- **Why it matters:** (a) expands the book's practical reach substantially — most readers encounter cost severance from the OTHER side of the transaction (as consumers, employees, residents) more often than from the extractor side. Decision-time tooling is the application most readers can use. (b) Reinforces the "no villain" structural argument — the commute-story apartment manager wasn't the adversary; the information architecture was. Decision-time tooling is what closes the information gap. (c) Affects the framework's contribution-claim — the book offers not just a theory but a usable instrument. (d) Surfaced the meta-question that became Working Principle #10: what lives in internal scaffolding vs external publisher-facing artifacts, and how does that shape the discipline applied to each layer?
- **Verdict (closed-ratified 2026-04-30):** **(b) — threaded at the external layer; rich internal scaffolding for everything else.**
  - **External layer (publisher-facing):** Pattern 2 / threaded — Ch 1 commute trade as opening decision-time anchor; Ch 3 waterman as second anchor when drafted; Ch 8 walkthrough integrates decision-time framing as the framework gets applied to McDowell / Deepwater / Libby + reader-side framings ("imagine the buyer / employee / resident asking..."); Ch 10 reflective close gestures at decision-time application as one of the framework's affordances. **No "how to apply" chapter or appendix; no prescribed decision-time methodology** — readers extract the methodology by watching the framework get used. Mirrors *Doughnut Economics* (Raworth 2017), *Mission Economy* (Mazzucato 2021), *Mine!* (Heller 2021) model.
  - **Internal layer (scaffolding):** rich; preserves methodology notes, worked decision-time examples (apartment leases, employment offers, medical-treatment decisions, career pivots), literature-pattern audit (Pattern 1 / 2 / 3 from comparable books), Book 2 seed material. Canonical home: [`core/methodology/decision_time_application_internal_v1.0.0.md`](../core/methodology/decision_time_application_internal_v1.0.0.md) (created 2026-04-30 with this ratification).
  - **Cross-layer flow:** internal feeds external (worked examples can become chapter prose; literature audits inform chapter framing); external must NOT carry internal contamination (per WP#8 + WP#10); internal bridges to Book 2 / Book 3 (research not landing in Book 1 publisher-facing accumulates internally as seed material).
- **Why this verdict (literature-pattern grounding):**
  - Pattern 1 (foregrounded "how to apply" chapter — *Nudge* / Thaler & Sunstein 2008) **strains framework thickness + author shield + Insight #13 register.** Framework is thick (5 theorems + 7 + 13 terms + Cᵢ); author shield is being-source-of-framework + Berggruen/Noema track + nursing career, not Sunstein-class institutional shield for prescription. Failure mode flagged by Insight #13.
  - Pattern 2 (threaded — *Doughnut* / *Mission Economy* / *Mine!*) **fits on every dimension** — framework thickness, author shield, audience choice (academic-trade hybrid + supplementary policy-practitioner per Insight #25), epistemic-humility discipline (Insight #14 Norway register), Book 1 vs Book 2 boundary (Insight #13), and the personal stories already in scope (commute trade; waterman).
  - Pattern 3 (ex-post only — *Capital in 21st Century* / *Governing the Commons*) **underclaims practical reach** for the chosen audience — Commons Bonds is closer to Raworth/Mazzucato register than Piketty/Ostrom register.
  - Full literature-pattern analysis preserved in [`core/methodology/decision_time_application_internal_v1.0.0.md`](../core/methodology/decision_time_application_internal_v1.0.0.md) §3.
- **Implementation:**
  - Working Principle #10 ratified same-day codifying the two-layer discipline as project-wide pattern (not just for #9 specifically)
  - Internal scaffolding artifact created at `core/methodology/decision_time_application_internal_v1.0.0.md`
  - Insight #36 (Ch 1 + Ch 3 conversational drafting) absorbs Pattern 2 threading discipline as part of natural drafting; no separate sub-task
  - Ch 8 + Ch 10 prose-sweep at next sweep cycle checks decision-time framing presence per Pattern 2 discipline
  - No new rigor pass required (this is scope/register discipline; literature-pattern analysis preserved internally)
- **Dependencies / Links:**
  - Personal Stories Candidate #1 (commute trade) — opening external-layer demonstration anchor; already captured + tagged with framework connections
  - **Working Principle #10** (Two-layer content origination discipline; ratified 2026-04-30) — generalized from this verdict
  - [`core/methodology/decision_time_application_internal_v1.0.0.md`](../core/methodology/decision_time_application_internal_v1.0.0.md) — internal-scaffolding canonical artifact
  - Insight #13 (book-scope creep monitoring) — reinforced by WP#10
  - Insight #14 (Norway treatment + epistemic-humility discipline) — compatible Pattern 2 register
  - Insight #25 (academic-trade hybrid audience choice) — Pattern 2 fits this audience natively
  - Insight #28 (three-tier retirement-trace classification) — compatible internal/external axis
  - Insight #36 (Ch 1 + Ch 3 conversational drafting) — absorbs Pattern 2 threading at external layer
  - Insight #37 (scaffolding-vs-publisher-facing separation pass) — WP#10 prevents contamination at origination, reducing #37 scope going forward
- **Todo link:** N/A (closed).

### Insight #8 — Audit methodology failure risk (captured as Working Principle #2)

- **Raised:** 2026-04-24 by me
- **Status:** closed-ratified (promoted to Working Principle #2)
- **Category:** method
- **Content:** My original audit methodology used case-sensitive exact-phrase grep, which returned 0 matches for Value Capture / Cost Bearing / Asymmetric Regret — terms that actually have 16 / 46 / 24+ occurrences when audited case-insensitively + concept-level. Risk: future audits produce misleading verdicts if methodology isn't disciplined.
- **Why it matters:** Audit methodology is part of the rigor. A retirement recommendation based on a flawed audit creates exactly the chapter-rewrite cost the meta-pass was supposed to prevent.
- **Proposed resolution:** Formalize as Working Principle #2 in `alignment/commons_bonds_working_principles_v1.0.0.md`.
- **Dependencies / Links:** Working Principle #2 landed 2026-04-24 (commit 72825a4).
- **Todo link:** N/A (closed).

### Insight #10 — Framework vocabulary literature audit (prior-art check against established economics/political-economy terminology)

- **Raised:** 2026-04-24 by Chris Winn
- **Status:** under-review (findings reported + 2 decisions ratified; remaining decisions + Phase A3 citation sweep pending)
- **Category:** vocabulary · method · publishing (intellectual honesty)
- **Content:** Chris raised concern that some framework terms may collide with or unknowingly appropriate established economics / political-economy terminology. Comprehensive web-literature audit conducted 2026-04-24 across all framework vocabulary. Key findings:
  - **"Value Extraction"** — Mariana Mazzucato, *The Value of Everything* (2018), is the dominant established usage in political economy. Chris independently rediscovered the term through sociology-essay work. **Decision ratified 2026-04-24: cite Mazzucato + position framework as extension into physical-resource domain.**
  - **"Cost Severance"** — **semantic collision** with established HR/accounting "severance costs" (employee termination, per IAS 37, US GAAP). Chris's usage is totally different but reader-confusion risk is real. **Decision pending** (options: keep + disambiguate / rename / lean into collision rhetorically).
  - **"Accountability Bond"** — adjacent to established "Reclamation Bond" / "Financial Assurance" literature in mining/oil-gas regulation (OSMRE; GAO-17-207R). **Decision ratified 2026-04-24: cite reclamation-bond / financial-assurance literature in Tech Appendix + Ch 5.**
  - **"Abundance Inversion Test" (AIT)** — low-risk collision with Christopher Alletto's 2024 SSRN paper "The Abundance Inversion" (different concept: AI + public-sector efficiency). **Recommended:** Tech Appendix footnote for due diligence.
  - **"Asymmetric Regret"** — already identified in ARP rigor pass; Loomes-Sugden 1982 + Savage 1951 minimax regret; Tech Appendix footnote recommended.
  - **"Substitutability Function S"** — concept of substitutability is from Hicks 1932 + CES literature + Dixit-Pindyck real options; specific S(t|t₀) probability-over-time-with-extraction-feedback form appears novel. Recommended: cite Hicks + Dixit-Pindyck.
  - **"Commons Bonds"** — adjacent to Environmental Impact Bonds (EIB) literature; specific phrase appears novel. Recommended: cite EIB literature in Ch 5/Tech Appendix.
  - Appears novel (no prior art found): Severed Cost, RCV, Externality Tail (as term), Four Gates, Abundance Masking, IPG.
- **Why it matters:** Chris's intellectual-honesty commitment requires explicit acknowledgment of prior art. Framework adoption credibility depends on being seen as extending established work, not appropriating or ignoring it. Mazzucato + reclamation-bond citations are the most load-bearing; Cost Severance naming collision is the highest-stakes open decision.
- **Proposed resolution:**
  - **(Done 2026-04-24):** Terms Index Value Extraction record updated with Mazzucato citation + extension positioning + canonical citation form.
  - **(Phase A3 sweep):** Ch 1 + Ch 6 + Tech Appendix add Mazzucato citation at Value Extraction first use.
  - **(Phase A3 sweep):** Ch 5 + Tech Appendix add reclamation-bond / financial-assurance citations at Accountability Bond first use.
  - **(Pending decision):** Cost Severance naming collision — needs dedicated rigor pass on whether to (a) keep + disambiguate, (b) rename, (c) lean into rhetorically.
  - **(Recommended, low priority):** Tech Appendix footnotes for AIT (Alletto), Substitutability Function (Hicks/Dixit-Pindyck), Asymmetric Regret (Savage/Loomes-Sugden), Commons Bonds (EIB literature).
- **Dependencies / Links:** Web literature search results 2026-04-24. Terms Index update v1.1 (this commit). Phase A3 citation sweep pending.
- **Todo link:** "Review Open Insight #10 remainders: (i) Cost Severance naming collision rigor pass; (ii) Phase A3 citation sweep plan."

### Insight #18 — Autonomy-as-commons treatment in Ch 1, Ch 6, Tech Appendix (with political-philosophical acknowledgment)

- **Raised:** 2026-04-24 by Chris Winn at Option C' ratification: *"Additionally capture where the autonomy as a commons example should be discussed in the book, and how, and then add it to the guidance documents for that/those chapter(s). Then add it to the drafts of the associated chapter(s) as I think you already have the supporting reasons and guidance for it in your memory."*
- **Status:** addressed (guidance docs updated + light prose added to drafts via this work; chapter-revision phase will integrate further).
- **Category:** craft · chapter-placement · framework-coherence · political-philosophical positioning
- **Content:** Autonomy is the politically-most-contested of the 10 commons categories. Whether autonomy operates as a commons depends on political tradition (classical liberalism vs civic republicanism vs socialist vs Marxist vs lived-oppression vs dominant-class perspectives). Framework's response per Option C' ratification: don't argue universal ontology; show how cost severance operates across whatever-commons-the-reader-identifies; treat the 10 as examples not canonical.
- **Where in the book autonomy-as-commons should be discussed:**

  **Ch 1 (origin story + 120-hour-week thread):**
  - Anderson 2017 *Private Government* canonical for autonomy dimension per bibliography (already cited).
  - Ch 1's 120-hour-week thread already has consent-problem passage. Extend with autonomy-as-commons framing: knowledge-worker case demonstrates autonomy-supporting-infrastructure (employment law; labor protections; severance norms; contract enforceability) functioning AS commons that extraction (120-hour weeks) severs costs from.
  - Connects to Personal Stories Candidate #1 (commute-trade) — both 120-hour-week and commute-trade are Commons-Consumption Inversion cases on the autonomy/time commons axis.

  **Ch 2 (The Miner — Appalachian coal):**
  - Sen's capabilities framework + consent-under-constraint already invoked.
  - Coal miner's autonomy-supporting-infrastructure (mobility options; alternative employment; community wealth as exit option; epistemic resources to evaluate Black Lung risk) was systematically depleted — autonomy-commons hollowed out. Add explicit framing.

  **Ch 6 (methodology — Three Ways of Counting):**
  - When introducing CIT, autonomy is the politically-most-contested example. Use it as the case where political-philosophical-acknowledgment is most explicit.
  - Tech Appendix carries fuller treatment; Ch 6 prose names the contestation and proceeds.

  **Tech Appendix §F (or methodology section):**
  - Full Anderson + Pettit + Skinner civic-republican lineage citation.
  - Explicit political-philosophical-acknowledgment passage (the recommended authorial-voice positioning text).
  - Note that Autonomy commons-framing is one tradition among several; framework operates regardless of which.

  **Ch 9 (policy economy):**
  - Community Transition Reserve as named policy rec includes autonomy-supporting-infrastructure (income transition + retraining + relocation support = autonomy-commons restoration).

  **Ch 10 (closing):**
  - Reflective passage can return to autonomy-as-commons framing as one example of the framework's reach.

- **How autonomy-as-commons should be discussed (authorial-voice):**

  The recommended Ch 1 / Ch 6 framing (ratified 2026-04-24 with Option C'):
  > *"This framework doesn't argue that autonomy is universally a commons, or that habitability is, or that time is. It argues that when any of these operate AS commons in a given society — shared, depended-on, collectively enabling — extraction can sever cost from that commons, and this methodology measures the severance. Different political traditions have different commitments about what is shared and what is individual. The framework works within any of those commitments. What it doesn't accept is extraction without accountability, regardless of which commons is being extracted from."*

  For autonomy specifically:
  > *"Autonomy is the most contested of the commons categories examined here. Classical liberals will recognize autonomy as individual natural-right; the supporting infrastructure (rule of law; contract enforceability; labor protections; severance norms) is enabling but not itself commons. Civic republicans (in the tradition of Anderson, Pettit, Skinner) will recognize autonomy as non-domination, requiring shared institutions to remain sustainable — institutions that function as commons. The framework doesn't settle this. It accommodates both readings — and the lived-oppression reading, where autonomy is something extracted not shared. What the framework asks: when extraction operates on whatever-autonomy-supporting-infrastructure your case treats as load-bearing, the cost-severance methodology applies. That's the through-line."*

- **Why this matters:**
  - Honors political-philosophical diversity (Option C' ratified positioning).
  - Protects framework from "autonomy ISN'T a commons in MY tradition" attack — framework accommodates rather than asserts.
  - Strengthens the framework's tool-use positioning across audiences.
  - Makes Anderson + Pettit + Skinner lineage explicit (already in bibliography for Anderson; Pettit + Skinner can be added if Tech Appendix treatment goes deep).
  - Ties Ch 1's 120-hour-week and commute-trade narratives to the Autonomy commons-framing without forcing political commitment on the reader.

- **Bibliography additions (potentially needed):**
  - Pettit, Philip. *Republicanism: A Theory of Freedom and Government* (1997) — civic-republican autonomy-as-non-domination.
  - Skinner, Quentin. *Liberty Before Liberalism* (1998) — historical-republican-tradition.
  - Both optional Tech Appendix depth additions; not load-bearing for Book 1 chapter prose.

- **Action: this commit captures the discipline.**
  Phase 2 (this commit): guidance docs updated for Ch 1 + Ch 6 + Tech Appendix.
  Phase 3 (this commit or follow-on): light prose insertions into chapter drafts at natural points.

- **Dependencies / Links:** Option C' ratification (10-list dissolution rigor pass commit `e30087e`); Anderson 2017 + Sen 1999 + Nussbaum 2011 (already in bibliography); Personal Stories Candidate #1 (commute-trade as Consumption-Inversion paradigm); Open Insights #13 (scope-creep), #15 (chapter revision thread), #16 (two CIT sub-forms); Ch 1 + Ch 6 guidance docs + drafts (Phase 2 + 3 of this work).
- **Todo link:** "Review Open Insight #18: autonomy-as-commons placement — verify Ch 1 + Ch 6 + Tech Appendix integration during Phase B chapter revision."

### Insight #17 — Option C' political-philosophical positioning (commons-as-examples-not-canonical)

- **Raised:** 2026-04-24 by Chris Winn during 10-list dissolution exchange: *"You would likely get very different answers from a person living in a modern socialist, or democratic society and a slave, a slave owner. I'm curious to lean into this..."*
- **Status:** closed-ratified 2026-04-24 by Option C' ratification (10-commons-list dissolution rigor pass).
- **Category:** framework-structure · craft · publishing
- **Content:** What counts as a commons is politically-traditionally contested. Framework strengthens by accommodating rather than settling. Ratified positioning: the 10 are EXAMPLES not canonical; framework's universality is about METHOD (CIT applies anywhere extraction operates on commons-like resources), not enumeration canonicity. Tech Appendix names political-contestation explicitly for politically-contested commons (Autonomy especially; also Political, Kindred, Epistemic).
- **Why it matters:**
  - Reduces framework's political-commitment surface.
  - Increases framework's usability across political traditions.
  - Honors lived-experience variance (slave/owner/citizen all face cost-severance under different ontologies of commons).
  - Matches successful adjacent-framework publishing pattern (Ostrom, Sen/Nussbaum, Raworth, Klinenberg, Mazzucato).
- **Resolution:** Option C' ratified via 10-commons-list dissolution rigor pass (commit `e30087e`). See Open Insight #18 for autonomy-as-commons specific chapter-placement implementation.
- **Dependencies / Links:** 10-list dissolution rigor pass; Open Insight #18 (autonomy-as-commons placement); Terms Index Abundances v1.2 record.
- **Todo link:** N/A (closed).

### Insight #16 — Two CIT sub-forms (Absence-Inversion + Consumption-Inversion) as methodology-contribution book content

- **Raised:** 2026-04-24 by Chris Winn + me collaboratively. Surfaced during commons-as-structural-identity rigor pass. Author direction: *"Make sure we capture this as that is a marvelous insight that likely needs to be somewhere in the book."*
- **Status:** **closed-ratified 2026-04-26** — captured at multiple operationalization levels (Tech Appendix supplement §6.1 + §6.1.1 + §6.1.2; cit_examples per-case worked-examples; supplement HTML integration block); chapter-level prose treatment drafted in Ch 6 supplementary drafts §6.5–§6.10 cluster.
- **Closure (2026-04-26):** Two-sub-form CIT operationalized across:
  - **Tech Appendix supplement §6.1** — formal spec of CAI + CCI as sub-forms in sequence (CAI first; CCI second; only claims passing both qualify as Cost Severance)
  - **Tech Appendix supplement §6.1.1** (added 2026-04-25) — level-of-claim specification discipline (closes M11 Char 12 finding from academic-rigor full test); commit `b566d66`
  - **Tech Appendix supplement §6.1.2** (added 2026-04-25) — domain distinction (extraction commons vs coordination commons; CCI failure routes to Ostrom-tradition, not framework rejection); closes M11 Char 17 finding; commit `408a37d`
  - **Tech Appendix HTML partial integration block** — §6 included in commit `351817c` integration of supplement §2-§7
  - **`core/methodology/cit_examples_v1_0_0.md`** — seven worked CIT applications through Four Gates with both sub-forms exercised
  - **Ch 6 supplementary drafts** §6.5 (Parfit) + §6.6 (CIT-vs-empirical falsifiability) + §6.7 (IPG reconciliation) + §6.8 (DAC three-horizon) + §6.9 (Ostrom-vs-extraction) + §6.10 (reparations-economics) + §6.11 (methodology defense consolidation) — chapter-prose-register treatments drafted, AUTHOR ZONE-flagged for register review pending Ch 6 finalization
- **Chapter placement decisions made:** Ch 6 is primary placement (formal methodology + worked examples). Optional reflective companion in Ch 10 (per §6.5.3 draft). Ch 1 commute-story is paradigm Consumption-Inversion case if Chris's personal-stories drafting cycle integrates it. Ch 7 asteroid miner is paradigm Absence-Inversion. Cross-chapter framing flagged for Phase B chapter revision.
- **Dependencies / Links:** CIT rename rigor pass (commit `b294c79`); commons-as-structural-identity rigor pass (commit `c4b09dc`); academic-rigor full test (commit `ae90800`) for M11 Char 12 + Char 17 findings; Ch 6 supplementary drafts file (multiple commits 2026-04-25 / 2026-04-26).
- **Todo link:** N/A (closed at framework + supplement level; chapter-level prose finalization is Phase B chapter-revision work governed by Insight #15 thread).
- **Category:** framework-methodology contribution · chapter placement · craft
- **Content:** AIT's "invert the abundance state" language collapsed two operationally distinct modes of the test. Under the CIT reframing, the two sub-forms become visible:

  **Commons-Absence Inversion** — imagine the commons not existing at all.
  - **Paradigm cases:** oxygen in space; water on Mars; McDowell habitability destroyed by coal extraction; Deepwater's Gulf ecosystem absent; Libby's protected-workplace-health commons eliminated.
  - **Operational question:** *what would it take to replace the commons?* (Or: what costs does the commons carry for free that would become visible bills if the commons were gone?)
  - **Typical application:** physical-resource extraction cases; civilizational-scale destruction; hypothetical off-Earth scenarios.

  **Commons-Consumption Inversion** — imagine the commons not being consumed.
  - **Paradigm cases:** commute time returned (5 hours/day saved); forest uncut; attention not harvested; lifetime-hours not sold to employer beyond needed work.
  - **Operational question:** *what could the commons do if not drawn down?* (What opportunities does the consumed commons foreclose that weren't visible at the moment of choice?)
  - **Typical application:** time-commons + attention-commons + opportunity-commons cases; personal-scale extractions; information-asymmetric self-severance cases.

- **Why it matters for the book:**
  - **Methodology clarity:** two named sub-forms make CIT's operational flexibility visible. Readers learn when each applies.
  - **Audience bridging:** Absence-Inversion resonates with readers who think about extraction in environmental/resource terms (Ostrom / Klein / Raworth reader). Consumption-Inversion resonates with knowledge-worker readers whose own lives have been commons-consumed by the attention/time economy. The framework reaches both audiences by naming both modes.
  - **Case-class organization:** the framework's 18+ cases naturally split by sub-form. McDowell, Deepwater, Libby, Chesapeake, Norway, asteroid scenarios = Absence. Commute, healthcare-time, 2008-retirement-savings-consumed, 120-hour-week = Consumption. Some cases exercise both (mining destroys habitability AND consumes land).
  - **Pedagogical economy:** Ch 6 can introduce CIT with ONE paradigm from each sub-form (e.g., Habitability-Absence for McDowell; Time-Consumption for commute-story). Two cases teach the full method. Without the sub-form distinction, readers have to infer the flexibility from scattered examples.
  - **Adoption durability:** having two distinct framed modes gives the framework more surface area for travel — a legal brief, policy paper, or academic article can cite CIT with the appropriate sub-form, which is more useful than citing "the abundance inversion test" abstractly.

- **Proposed book placements:**
  - **Ch 6 (methodology)** — introduce CIT with both sub-forms + one paradigm case each. Most likely primary placement.
  - **Tech Appendix methodological section** — full formalization with more paradigm cases + operational guidance for each sub-form. Already captured via CIT rigor pass.
  - **Ch 1 (if personal narrative opens)** — the commute-story (Candidate #1) is paradigm Consumption-Inversion. If Ch 1 opens with commute, the sub-form is implicitly introduced there and formalized in Ch 6.
  - **Ch 7 (asteroid miner)** — paradigm Absence-Inversion. The two-sub-form framing could cross-reference: "Ch 1's commute story was Commons-Consumption; the asteroid miner is Commons-Absence; the framework handles both."
  - **Ch 10 (closing)** — possible reflective use showing framework's operational flexibility across both modes.

- **Distinction vs prior capture:**
  - **Tech Appendix methodology** (via CIT rigor pass): formal mechanism-level treatment. Captured.
  - **Terms Index CIT record:** ready-reference. Captured.
  - **This Open Insight:** tracks the CHAPTER-LEVEL prose treatment + placement decisions. Additive to Tech Appendix treatment.

- **Dependencies / Links:** CIT rigor pass; commons-as-structural-identity rigor pass; Open Insight #15 (chapter revision thread — Ch 6 methodology treatment); Personal Stories Candidates Candidate #1 (commute trade — paradigm Consumption case).
- **Todo link:** "Review Open Insight #16: two CIT sub-forms chapter placement — decide Ch 1 / Ch 6 / Tech Appendix distribution during chapter revision."

---

### Insight #15 — Chapter revision thread: apply Accountability-Bond epistemic-humility discipline across Ch 4 / Ch 5 / Ch 6 / Ch 9 / Ch 10

- **Raised:** 2026-04-24 by Chris Winn (during epistemic-humility discipline ratification): *"capture this as a possible thread to review when we get past the terminology and start revising chapters"*
- **Status:** deferred · picks up when terminology-rigor work completes + chapter revision begins (Phase B or later). **Triggering condition:** Phase A3 audit sweep lands + we move from vocabulary-level work to chapter-level drafting / revision.
- **Category:** craft · chapter-specific · framework-coherence
- **Content:** Per Insight #14's ratified authorial-voice discipline for Accountability Bond (B is framework CATEGORY, not single-instrument prescription; Norway canonical real-world exemplar; preconditions load-bearing; no claim to having solved intergenerational CS; framework-appropriate pondering not prescription), the following chapter-specific implications need application during revision:

  - **Ch 4 (Norway)** — Norway as the framework's canonical real-world mitigation exemplar for intergenerational cost severance. Preconditions (rule of law + institutional architecture preventing plundering of current-population / not-yet-born-generation accounts) are load-bearing — not incidental context, but part of what makes the Norway solution function. Chapter should honor "this works AND these preconditions are why it works AND most societies lack these preconditions" rather than "look, Norway did it, others could too."
  - **Ch 5 (Accountability Gap)** — B as framework CATEGORY throughout (not single-instrument named). Norway referenced as the strongest existing example approaching B ≈ RCV. American regimes framed as radically distant (B << RCV). The "accountability gap" is the empirical-present-state of B far below RCV, not a prescription for a specific instrument.
  - **Ch 6 (methodology)** — B introduced as framework element + equational-closure role in CS = RCV − B. Avoid instrument-prescription (specific carbon-tax architecture, specific bond-design, specific insurance mechanism). Category-level treatment only.
  - **Ch 9 (policy)** — Community Transition Reserve is explicitly in-scope named policy recommendation per v1.0.3 book-scope doc. Additional specific instrument prescription (if any) tested against the epistemic-humility discipline: *does this prescribe a specific instrument design as THE fix, or does it present a candidate direction for the policy design space?* If the former → Book 2 territory; if the latter → OK with appropriate pondering-not-prescribing framing.
  - **Ch 10 (closing)** — honor what the framework HAS (diagnostic + naming + equational closure + Norway as best existing exemplar + Community Transition Reserve as one named candidate direction) without claiming a single-instrument cure. The book's contribution is identifying the problem rigorously and pointing toward known-working directions, not legislating the fix.

- **Why it matters:** Chapter revision is where the authorial-voice discipline either lands or slips. Terminology rigor (current phase) establishes what terms mean + how framework elements relate; chapter revision applies those terms in author-voice to specific chapters. If the epistemic-humility discipline isn't carried forward to chapter revision, chapters may subtly over-prescribe (present B as THE solution rather than framework category) or under-present Norway (treating it as just-another-case rather than canonical exemplar with load-bearing preconditions). Both failures would compromise Book 1's scope-appropriateness + adoption-durability.
- **Proposed resolution:** during Phase B (or whenever chapter revision begins), run each chapter's B / accountability / Norway content against the 5 specific implications above. Annotate revisions with explicit Open-Insight-#14 + Open-Insight-#15 provenance. If a chapter's draft conflicts with the discipline, triage: either revise the draft to match the discipline, or reopen the discipline for author-ratification-with-revision if new argument warrants.
- **Dependencies / Links:** Open Insight #14 (Norway-canonical + epistemic-humility discipline — originating content); Open Insight #13 (book-scope creep monitoring per v1.0.3); Accountability Bond Terms Index record; `tools/commons_bonds_book_scope_v1_0_3.md` (Ch 9 Community Transition Reserve + scope boundary); Ch 4/5/6/9/10 chapter drafts + guidance docs.
- **Todo link:** "Review Open Insight #15: chapter revision thread — apply epistemic-humility discipline to Ch 4/5/6/9/10 when chapter revision begins."

---

### Insight #14 — Norway's sovereign wealth fund as canonical intergenerational-CS mitigation exemplar + epistemic-humility discipline for B — CLOSED-RATIFIED 2026-04-30 (by reference)

- **Raised:** 2026-04-24 by Chris Winn (during Accountability Bond scope-creep clarification): *"I think the commonwealth fund of Norway is the most impressive mitigation solution I have found to address intergenerational cost severance yet it obviously can't exist in societies where a government is allowed to plunder accounts of people currently living and accounts of people not yet born so the Norway solution isn't a perfect solution."*
- **Status:** **closed-ratified 2026-04-30 (by reference) during Thread δ Insight #14 surfacing.** The discipline articulated in this insight body was already operationally captured 2026-04-24 (Accountability Bond rigor pass §7.3 + Terms Index Accountability Bond record); the original "raised · load-bearing for Book 1 authorial-voice calibration" status reflected ongoing chapter-drafting application, not pending decision. As of 2026-04-30 the discipline is reinforced + generalized across three downstream items, making Insight #14 the canonical mother-case for the broader "demonstrate the affordance; don't codify it" register: (i) **Insight #25** (academic-trade hybrid audience choice; ratified 2026-04-28) confirms #14's epistemic-humility register fits the chosen audience natively; (ii) **Working Principle #10** (Two-layer content origination discipline; ratified 2026-04-30) generalizes the "demonstrate, don't prescribe" discipline #14 articulated specifically for Norway/Accountability Bond into a project-wide content-origination pattern; (iii) **Insight #9** (verdict (b) ratified 2026-04-30) applies the same Pattern 2 / threaded register to decision-time tooling. The five-point discipline below remains operative as standing chapter-drafting guidance — nothing operational changes with this closure; the insight moves off the OPEN list because the discipline is fully captured + applied + reinforced.
- **Category:** craft · framework-structure · publishing
- **Content:** Author-specified discipline for Book 1's treatment of the framework's remediation-side variable (Accountability Bond, B):
  - **B is a framework CATEGORY, not a novel single-instrument prescription.** B = "every mechanism that forces cost-bearing onto extractors" (sovereign wealth funds, carbon taxes, insurance, reclamation bonds, direct liability, etc.). The framework's claim is mathematical: B = RCV is honest accounting. Which SPECIFIC instrument-mix best realizes that equality is a live policy design space, not a framework pre-commitment.
  - **Norway's Government Pension Fund Global (sovereign wealth fund) is the canonical existing real-world exemplar** — the most impressive intergenerational-cost-severance mitigation humanity has produced. Framework-canonical case material; Ch 4 anchor (already structured around Norway per bibliography + Ostrom successor literature).
  - **Norway's solution presupposes governance preconditions** — rule of law; institutional architecture preventing plundering current-population accounts or not-yet-born-generation accounts. Not universal; preconditions load-bearing.
  - **No claim to having solved it.** Book 1 frames the problem rigorously (CS = RCV − B; current regimes produce B < RCV); offers Norway as the best existing real-world example; PONDERS Accountability Bond as one possible direction; does NOT prescribe a specific instrument design as THE fix.
  - **Book 1 authorial voice:** *"perhaps something like an accountability bond could bridge this, though the Norway example shows what actually works and under what preconditions — and no society has yet solved this completely."* That register is framework-appropriate pondering. What's out of scope: "The Commons Bonds Framework Accountability Bond Act of 20XX" (that's applied-advocacy Book 2 territory with all the rigor-asymmetry concerns v1.0.3 §6.1 identifies).
- **Why it matters:**
  - Prevents Book 1 from over-reaching into instrument-prescription that would (a) trigger applied-advocacy scope-creep (Insight #13); (b) pre-commit the framework to a specific instrument design the evidence may not support; (c) undermine the framework's adoption credibility by appearing to sell a specific product rather than present a diagnostic + measurement tool.
  - Centers Norway at appropriate prominence — the framework's strongest empirical example of what intergenerational-CS mitigation can look like when preconditions hold.
  - Preserves intellectual honesty about what the framework HAS and HASN'T achieved: it has the diagnostic apparatus (naming + measurement); it has identified one existing example that works; it has NOT proven that any one specific instrument design is universally right.
- **Implications for chapter drafting:**
  - **Ch 4 (Norway)** — treat Norway's sovereign wealth fund as the canonical real-world mitigation exemplar with preconditions-are-load-bearing framing. Norway is the book's strongest empirical anchor on the remediation side.
  - **Ch 5 (Accountability Gap)** — frame B as framework category; reference Norway as the strongest existing example approaching B ≈ RCV; frame current American regimes as radically distant (B << RCV).
  - **Ch 6 (methodology)** — introduce B as framework element + equational closure; avoid specific-instrument prescription.
  - **Ch 9 (policy economy)** — Community Transition Reserve named policy rec is framework-appropriate; additional specific instrument-prescription tested against the epistemic-humility discipline.
  - **Ch 10 (closing)** — final reflection can honor that framework identifies the problem + offers diagnostic + points toward known-working examples without claiming a single-instrument cure.
- **Proposed resolution (original 2026-04-24):** capture in Accountability Bond rigor pass §7.3 + Terms Index Accountability Bond record (done 2026-04-24 with this commit). Apply during chapter drafting as authorial-voice calibration. No further decision needed; this is discipline not option-selection.
- **Closure (2026-04-30 by reference):** the discipline remains operative as standing chapter-drafting guidance for Ch 4 Norway treatment + Ch 5 accountability-gap framing + Ch 6 methodology + Ch 9 policy + Ch 10 close (per the 5-point implications above). It is reinforced + generalized by:
  - **Working Principle #10** (Two-layer content origination discipline; ratified 2026-04-30) — generalizes "demonstrate the affordance; don't codify it" project-wide
  - **Insight #9 verdict (b)** (ratified 2026-04-30) — Pattern 2 / threaded register applied to decision-time tooling, same register family as #14's Norway treatment
  - **Insight #25** (academic-trade hybrid audience; ratified 2026-04-28) — confirms Pattern 2 register fits the chosen audience natively
  - **Insight #15** (chapter revision discipline; OPEN) — operationalizes the 5-point implications during chapter revision; carries #14's discipline forward at the prose level
  - Routine 1 + 2 sentinel checks for vocabulary regression do not directly enforce #14 register (this is prose-level, not term-level), so chapter-by-chapter prose-sweep at Phase B / pre-submission editing remains the operational gate
- **Dependencies / Links:** Accountability Bond rigor pass (Terms Index record); Open Insight #9 (closed-ratified 2026-04-30; same register applied to decision-time tooling); Open Insight #13 (book-scope creep; reinforced by WP#10); Open Insight #15 (chapter revision discipline; carries forward 5-point implications); Insight #25 (audience choice); **Working Principle #10** (`alignment/commons_bonds_working_principles_v1.0.0.md`); v1.0.3 book-scope doc; Norway case-study file; Ch 4 guidance; Ostrom-successor bibliography entries (Hess & Ostrom 2007 Knowledge Commons; Ostrom 1990 Governing the Commons — North 1990 institutional-economics); [`core/methodology/decision_time_application_internal_v1.0.0.md`](../core/methodology/decision_time_application_internal_v1.0.0.md) (companion Pattern 2 register documentation).
- **Todo link:** N/A (closed). Chapter-drafting application carried by Insight #15 todo + per-chapter prose-sweep cycles.

---

### Insight #13 — Book-scope creep monitoring (Book 1 vs Book 2 vs Book 3 boundary per `tools/commons_bonds_book_scope_v1_0_3.md`)

- **Raised:** 2026-04-24 by Chris Winn (during Accountability Bond ratification: *"flag to see if it starts to cause book scope creep, creep towards things that are perhaps best left for book 2, book 3, etc. for scope of book and reasons for separating books"*). Refined 2026-04-24 after Chris corrected an initial oversimplified "Book 1 = diagnosis; Book 2/3 = fix" framing — *"The above said, I can accept the... Review the book 1 vs. book 2 vs. book 3 publication strategy documents and reasons. That is the guiding book scope, not my earlier over simplified sentence."* Governing document: `tools/commons_bonds_book_scope_v1_0_3.md` (2026-04-21 proposed canonical).
- **Status:** raised · ongoing monitoring discipline (cross-cutting across framework; not a per-term decision) · **REINFORCED by Working Principle #10 (ratified 2026-04-30)** — WP#10's two-layer content origination discipline gives book-scope-creep pressure a structural release valve: rich material that would otherwise pressure Book 1 publisher-facing accumulates in internal scaffolding instead, where it serves as Book 2 / Book 3 seed. This reinforces Insight #13 without closing it; #13 remains the standing discipline for publisher-facing scope decisions, with WP#10 as the companion origination-time pattern.
- **Category:** craft · publishing · meta (framework-scope discipline)
- **Content:** Several Ring-2 framework elements — Accountability Bond especially, but also Abundances scaffolding, Four Gates, and Cᵢ cost categories — invite treatment that would push Book 1 past the scope articulated in v1.0.3. The earlier oversimplified framing ("Book 1 = tool, Book 2/3 = fix") is REJECTED; the correct scope boundary is the **framework-naming vs. applied-advocacy distinction** grounded in the rigor-test reasoning of v1.0.3 §6.1.
- **Why it matters:** Scope creep has two failure modes: (a) Book 1 bloats toward a comprehensive-manual size that loses its framework-introduction role AND exposes the lone author to applied-advocacy risk the v1.0.3 rigor test identifies as structurally asymmetric; (b) Book 2/3 lose their clearest subject matter if Book 1 absorbs it. Both failure modes damage the three-book ladder's cumulative value.

**Actual scope boundary (per v1.0.3):**

**Book 1 (*Commons Bonds* — framework-naming book, 2026–2027 target, ACTIVE):**
- Names the mechanism (Cost Severance), prices the unpriceable residual (RCV), demonstrates universality via Abundance Inversion Test.
- 10 chapters + Technical Appendix + Glossary.
- Worked applications at **4 scales:** (1) individual narrative — the Miner; (2) individual analytical — worker/CEO dual-position cases (Ch 6); (3) hypothetical maximum-stripped — asteroid miner (Ch 7); (4) civilizational — coal at full tier depth (Ch 8).
- **Includes framework-level policy recommendations** — e.g., Community Transition Reserve named in Ch 9.
- **Includes the Accountability Bond concept** as framework element — states CS = RCV − B; articulates that B should equal RCV; describes the accountability-gap problem structurally; illustrates via flagship cases (McDowell, Deepwater, Libby, Social Security, 2008, healthcare, Chesapeake, Norway, opioid, tax-tradeoff, housing).
- **Includes Political Capture Cost as structural mechanism** (shielding condition in AIT; political-abundance dimension); NOT as applied critique of named industries.
- One-paragraph signposts acceptable (e.g., $10–15T aggregate subsidy in Ch 8 is signpost, not full simulation).

**Book 2 (*The Subsidy Economy* — applied-advocacy book, 2029+ target, NOTES-ONLY):**
- Applied, politically charged. Presupposes Book 1 framework + applies it to named beneficiaries.
- Full-economy simulations; resource-by-resource transition mechanics; named industries with documented lobbying histories; regulatory capture events; policy architecture for extraction-honest economy.
- **Activation gates (both required):** coauthor relationship OR institutional affiliation (economist, journalist, policy researcher); publisher with strong legal infrastructure.
- Reason Book 2 is a SEPARATE BOOK not a later Book 1 chapter: per v1.0.3 §6.1 rigor test — lone-author advocacy work on named beneficiaries is asymmetric (bears political cost while benefits distribute to others) + shield-absent (no institutional distance from named beneficiaries). Coauthor/institution restores balance. Nursing career + Berggruen + being-the-framework-source are safer than also authoring the applied-advocacy.

**Book 3 (*Pricing the Final Frontier* — horizon, NOTES-ONLY):**
- Off-Earth extraction, space law, cross-planetary institutional architecture.
- Expands Book 1 Ch 7's asteroid-miner seed into full institutional treatment.

**The load-bearing reason for the split (per v1.0.3 §6.1):**
- Book 1 (naming mechanisms) passes rigor test: **symmetric + shielded** (author bears intellectual cost + authorship burden; distance from named beneficiaries preserves shield).
- Book 2 as lone-author work FAILS rigor test: **asymmetric + unshielded** (author bears political cost while benefits distribute; no institutional shield from named beneficiaries).
- Book 3 as horizon work is future-safe: off-Earth extraction is post-adoption territory where framework vocabulary has had time to circulate.
- **NOT diagnosis-vs-fix** — Book 1 includes framework-level prescription (Community Transition Reserve; B = RCV as ideal; Accountability Bond as central instrument concept). What Book 1 EXCLUDES is applied-advocacy-on-named-beneficiaries.

**Trigger indicators (watch during chapter drafting + rigor passes):**
- A passage names specific industries with documented lobbying histories (→ Book 2).
- A passage attempts full-economy simulation rather than signpost (→ Book 2).
- A passage does resource-by-resource transition mechanics depth (→ Book 2).
- A passage names specific beneficiaries of extraction systematically (→ Book 2).
- A passage does exhaustive space-law / cross-planetary institutional design (→ Book 3).
- A passage goes textbook-depth on any single Abundance, Cᵢ, or instrument-type implementation (→ may be Book 2 or future specialist work).

**Mitigation:**
- Book 1 can POINT TO future books ("a fuller treatment of named industries' lobbying histories is beyond this book's framework scope and is the subject of future applied work") rather than absorbing the depth.
- Preserve detailed notes in `.claude/` or `archive/_OneDayMaybe/book-two/` or `archive/_OneDayMaybe/book-three/` directories.
- Use footnotes sparingly — footnotes that become mini-essays are scope-creep signal.
- The v1.0.3 scope-boundary table (in that doc, §2) is the authoritative reference for specific material allocation decisions.

**Trigger-heavy terms flagged (watch during chapter drafting):**
- **Accountability Bond (B)** — Ring-2, ratified 2026-04-24. Likely-heaviest source of pressure **not because remediation is out-of-scope** (framework-level prescription IS in scope) **but because applied instrument-design on specific named industries + resource-by-resource B calibration is Book 2 territory**. Book 1 names B + states B = RCV as ideal + describes the gap empirically via cases; Book 2 would do the applied work of raising specific industries' B via specific instruments.
- **Abundances (10-element scaffolding)** — Ring-2, pending rigor pass. Textbook-depth elaboration on each abundance could pull Book 1 toward comprehensive-manual mode.
- **Four Gates** — Ring-2 cluster, pending rigor pass. Gate-implementation specifics for named regulatory contexts would cross into applied territory.
- **Cᵢ cost categories** — ratified Ring-1; each category (health, community, intergenerational, etc.) has Book-2 applied depth (industry-specific pricing methodologies) that belongs to advocacy work.

- **Proposed resolution (operational monitoring, not decision):** during Phase A3 chapter drafting + future sessions, when a rigor pass or chapter-drafting session encounters scope pressure, explicitly apply the v1.0.3 boundary test (framework-naming vs applied-advocacy-on-named-beneficiaries). Annotate scope-creep decisions in chapter drafts / rigor passes / guidance docs. If pattern persists across multiple terms, consider promoting to a Working Principle (Principle #7: Book-scope discipline grounded in v1.0.3).
- **Governing document:** `tools/commons_bonds_book_scope_v1_0_3.md` (2026-04-21 proposed canonical).
- **Dependencies / Links:** Accountability Bond rigor pass; Terms Index Accountability Bond record (scope-creep flag); cross-references to upcoming Abundances + Four Gates rigor passes; `archive/_OneDayMaybe/book-two/` and `book-three/` repositories for future-book notes.
- **Todo link:** "Review Open Insight #13: book-scope-creep monitoring grounded in v1.0.3 — watch during chapter drafting + future rigor passes; consider Principle #7 promotion if pattern persists."

---

### Insight #12 — Asymmetric Regret Principle rename sub-decision — CLOSED-RATIFIED 2026-04-24 (FINAL after same-day flip)

**Resolution 2026-04-24 by Chris Winn (FINAL):** **Asymmetric Regret Rule (ARR)** ratified as new name. Replaces "Asymmetric Regret Principle." Per ARP rename rigor pass commit `b8b62e3`.

**Same-day flip provenance:** A preliminary ratification of "Reversibility Default (RD)" was reversed same-day 2026-04-24 after M6 academic-rigor question surfaced post-ratification. RD would have required Tech-Appendix-footnote + Ch 7 prose + Glossary entries to make Savage / Loomes-Sugden lineage visible to reviewers; ARR has regret-theory direct lineage IN THE NAME — M6 maximum-protective without footnote dependency.

**Why "Rule" over "Principle":** Operational decision rule, not foundational ethical principle. "Rule" downgrades overclaim while preserving "Asymmetric Regret" framing's direct-lineage value.

**Phase A3 sweep activated (smaller than RD's would have been — last-word rename only):** ~20 chapter refs (Ch 7 GuidanceDoc + Ch 7/9/10 drafts + Tech Appendix) — replace "Asymmetric Regret Principle" / "ARP" with "Asymmetric Regret Rule" / "ARR"; Glossary v3 entry rename; Working Principle #5 example-reference updates; CSG record cross-pairing reference update; older docs Tier-2 retirement-note headers per Principle #4.

**Lesson captured for future passes:** when M5 + cross-tradition-adoption tradeoffs appear close, foreground M6 direct-name-visibility EXPLICITLY in the executive summary recommendation. The M5/M6 weighing should be visible at ratification time, not surfaced post-ratification. (Captured in ARP rename rigor pass §7 final.)

---

### Insight #12 (original content — preserved for provenance)

- **Raised:** 2026-04-24 by me (surfaced during ARP rigor pass; flagged at ratification 2026-04-24 by Chris Winn)
- **Status:** raised · awaiting author decision (rename is independent of rigor verdict; primary verdict Option A promote Ring 2 already ratified)
- **Category:** vocabulary · craft
- **Content:** "Principle" in "Asymmetric Regret Principle" may overclaim given ARP is an operational decision rule (not a foundational ethical principle). Chris engaged 2026-04-24 with candidates "Asymmetric Rule," "Asymmetric Regret Rule," "Asymmetry Rule." Rigor pass offered additional candidates. At ARP ratification 2026-04-24, rename sub-decision held open pending author deliberation.
- **Why it matters:** Rename ripples through 20+ chapter refs (Ch 7 + Ch 9 + Ch 10 + Ch 7 GuidanceDoc + Tech Appendix). Chosen name affects how academic reviewers + general readers process the rule — "Principle" sets foundational expectations; "Rule" sets operational expectations; "Default" sets procedural expectations.
- **Candidate set (ratified 2026-04-24 by Chris Winn's engagement + my analysis):**
  - **Retain "Asymmetric Regret Principle"** — status quo; preserves existing draft prose; "Principle" may overclaim.
  - **"Asymmetric Regret Rule"** — minimal change from current; "Rule" downgrades overclaim while preserving "regret" framing.
  - **"Asymmetric Rule"** — short; strips "regret" framing (may lose specificity).
  - **"Asymmetry Rule"** — short; abstract (may read too vague).
  - **"Reversibility Default"** — operational framing; clearest instruction ("default to reversible"); loses "asymmetric" intellectual content.
  - **"Irreversibility Bias"** — psychology-framed; may read as cognitive-bias rather than decision rule.
  - **"Regret Asymmetry Rule"** — emphasizes asymmetric-regret as property; clear rule status.
  - **"Option-Preservation Rule"** — elegant bidirectional framing (preserve options either way); bigger conceptual shift to option-theory language.
- **Proposed resolution:** Author selects from candidate set (or proposes new candidate) at whatever pace suits authorial voice development. No urgency — primary verdict ratified + Principle #5 (context-flipping rules earn named-rule status) holds for whichever name is chosen.
- **Dependencies / Links:** ARP rigor pass (commit `7f35783`); ARP ratification (this commit `TBD`); Principle #5 (commit `cae4936`); Terms Index ARP record.
- **Todo link:** "Review Open Insight #12: ARP rename sub-decision — author's paced decision."

---

### Insight #11 — "Cost Severance" semantic collision with HR/accounting "severance costs"

- **Raised:** 2026-04-24 by me (surfaced during Insight #10 literature audit)
- **Status:** closed-ratified 2026-04-24 — Option C (rhetorical bridge) ratified by Chris Winn via dedicated rigor pass `tools/rigor-passes/commons_bonds_rigor_pass_2026-04-24_term_cost_severance_collision_v1.0.0.md`
- **Category:** vocabulary · craft · publishing
- **Content:** "Severance costs" / "cost of severance" is an established HR/accounting term for employee termination payments (IAS 37, US GAAP, PwC, KPMG, Bloomberg). Every corporate accountant, HR professional, tax lawyer, and policy professional reads "cost severance" as "employment termination cost." Chris's Ring-1 flagship "Cost Severance" (the separation of cost-bearer from value-capturer) is totally different meaning but collides in reading. Collision risk is high because the target audiences (policy, legal, academic econ) include exactly the people who know the HR/accounting meaning.
- **Why it matters:** Cost Severance is the framework's Ring-1 flagship — the term the book's adoption-durability bet rests on. Semantic collision at first-encounter degrades adoption: a reader processing "cost severance" as HR-severance-costs before picking up the framework's meaning has to back-parse on every occurrence. If the term can't reliably communicate on first read in target audiences, the flagship fails its job.
- **Resolution:**
  - **Option C — Keep + lean into collision rhetorically — RATIFIED 2026-04-24.** Ch 1 opening uses the HR familiarity as a teaching bridge: "Corporate America knows the word 'severance.' [...] Cost severance works the opposite direction. [...] Same move, applied to the relationship between value-capturers and the commons they draw from — except the bill never comes due to the severing party."
  - Option A (disambiguate) held as fallback if Ch 1 drafting reveals bridge is authorially unsustainable.
  - Option B (rename — 6 candidates tested, Accountability Severance was strongest) rejected on M12 + M4 + M11 grounds.
  - Ratification also established **rhetorical bridge as Level 5 on the M12 action ladder** (Principle #6 Corollary D, ratified 2026-04-24).
- **Dependencies / Links:** Insight #10 (literature audit); Cost Severance collision rigor pass; Principle #6 Corollary D (M12 action ladder); Ring-1 ratification of Cost Severance (commit `0aafed7`); Severed Cost Ring-1 ratification (unaffected; distinct term with no collision).
- **Todo link:** N/A (closed).

---

### Insight #21 — Tech Appendix v0.0.5 + Chapter 6 HTML full-rewrite (dedicated session)

- **Raised:** 2026-04-26 by Chris Winn during Phase B authoring session
- **Scope expanded 2026-04-26:** added Chapter 6 to scope when format question surfaced during Ch 7 register-review (Ch 6 carries the same legacy Google-Docs-export single-line HTML form that the Tech Appendix does; both warrant the same conversion treatment).
- **Status:** raised · queued for dedicated session · format decision locked
- **Category:** craft · publishing · Phase B authoring
- **Content:** The Tech Appendix v0.0.5 HTML and Chapter 6 HTML both carry Google-Docs-export styling (now legacy artifact — Google Docs round-trip stopped 4-5 days before this session). The Tech Appendix additionally carries the partial integration block from 2026-04-25 (commit `351817c`) that added supplement §2-§7 in inline-styled form before `</body></html>`. A full HTML rewrite is warranted to: (1) reformat in clean canonical authoring style rather than Google-Docs-export CSS; (2) reconcile the partial integration block with the rest of the doc structurally (move §2-§7 sections into the doc's natural section ordering rather than at-end appended-block); (3) execute the 15 FGC + 1 Universality Test passage rewrites flagged in supplement §1 (not string-substitutable); (4) reframe §K Decomposition Layer cluster for the retired 8-tier scheme; (5) integrate the Block 4 numerical results + Method 3 sensitivity findings + DAC three-horizon + IPG-table reconciliation as canonical sections rather than supplement-staged; (6) integrate the Phase B authoring passages from Ch 6 supplementary drafts (§6.5 Parfit; §6.6 CIT-vs-empirical falsifiability; §6.7 IPG-table reconciliation; §6.8 DAC three-horizon; §6.9 Ostrom-vs-extraction; §6.10 reparations-economics) where they have Tech Appendix companions; (7) convert Chapter 6 to the same clean format with proper section structure for math-formula-heavy prose.
- **Format decision (locked 2026-04-26):** **Option A — pretty-printed semantic HTML.** Author-ratified 2026-04-26. Decision-set evaluated: Option A (pretty-printed semantic HTML); Option B (markdown with LaTeX); Option C (AsciiDoc); Option D (LaTeX); Option E (status-quo single-line Google-Docs-export). Option A wins because: (a) preserves math display via existing inline-MathJax markup without toolchain migration; (b) Edit-tool-friendly with proper line breaks and indentation; (c) semantic HTML structure (proper `<section>` / `<figure>` / `<blockquote>` elements rather than div-soup); (d) clean readable source for both author and reviewer; (e) compatible with existing publishing workflow (HTML-as-final-output remains intact). Applies to both Tech Appendix v0.0.5 → v0.0.6 (or v1.0.0) AND Chapter 6 HTML conversion. Format conversion timing: bundled into this dedicated session rather than executed as separate quick-win commit, so that the conversion + content rewrites happen with full structural awareness rather than mid-stream context-switching.
- **Why it matters:** the Tech Appendix is the framework's academic-rigor showpiece; for Berggruen-window submission readiness (2026-08-17), the doc should land in clean, methodologically-current, well-organized form rather than the current accreted-state form (v0.0.4 baseline + 2026-04-24 in-place sweep + 2026-04-25 partial integration block + supplement-staged Phase B drafts). Chapter 6 carries the formal-apparatus prose that academic reviewers will read most carefully; its current single-line export form makes editing painful and reads more like an artifact than a manuscript. Reader experience matters; academic reviewer experience especially matters.
- **Why dedicated session:** the work is large enough (~7 substantive tasks now; multi-cycle rigor) that batching it with other Phase B work fragments attention and risks the kind of partial-rewrite that creates new inconsistencies. A dedicated session can hold the Tech Appendix + Ch 6 in working memory, walk through each task with full structural awareness, and produce a clean v0.0.6 (or v1.0.0 if the rewrite is substantial enough to warrant the version bump) plus a properly-formatted Ch 6.
- **Proposed resolution:** schedule a dedicated session for Tech Appendix v0.0.5 → v0.0.6 (or v1.0.0) + Chapter 6 full HTML rewrite, both in Option A pretty-printed semantic HTML. Session plan: walk each section in order; consolidate from supplement + integration block + Ch 6 supplementary drafts; reconcile IPG-table numerical anchors; produce clean canonical structure; commit per-section per push-cadence rule. Pre-session prep no longer needed (Option A confirmed; toolchain migration question resolved by Option A choice).
- **Trigger condition for session start:** Chris signals readiness — likely after current Phase B Tier 1 + Tier 4 batch + chapter-by-chapter prose-sweep cycle lands (currently in progress in 2026-04-25/26 session), and either before or after the personal-stories drafting cycle depending on Chris's priority sequence.
- **Dependencies / Links:** v1.44.0 session handoff (Phase B item: Tech Appendix v0.0.5 HTML integration of supplement §2-§7); commit `351817c` (2026-04-25 partial integration block); supplement file (`core/technical-appendix/archive/TechnicalAppendix_v0.0.5_supplement.md`); Block 4 validation work (`core/technical-appendix/block4_validation_2026-04-25.md`); Method 3 sensitivity analysis (`core/technical-appendix/method3_sensitivity_analysis_2026-04-25.md`); empirical sourcing pass (`core/technical-appendix/empirical_sourcing_pass_2026-04-25.md`); Ch 6 supplementary drafts §6.5–§6.10 (Phase B authoring passages with Tech Appendix companions); current Ch 6 HTML draft.
- **Todo link:** "Schedule dedicated session for Tech Appendix v0.0.5 + Ch 6 full HTML rewrite in Option A pretty-printed semantic HTML (Insight #21)."

---

### Insight #22 — Chapter titles fall within chapter-by-chapter prose-sweep scope

- **Raised:** 2026-04-27 by Chris Winn during Ch 9 holistic review
- **Status:** **closed-ratified 2026-04-27** — memory rule `feedback_always_expand_rule.md` updated to add chapter titles + section headers to chapter-by-chapter sweep scope, with explicit Book-1/Book-2-carry-over check + applied-advocacy register check + vocabulary regression check + full chapter-title rigor pass protocol when a concern surfaces. MEMORY.md index hook updated to reflect the included scope. Verification sweep across remaining chapter titles (Ch 2 / Ch 4 / Ch 5 / Ch 6 / Ch 8 / Ch 10) confirmed clean per Insight #22 §10 set-rigor analysis at the time of raising; Ch 1 + Ch 3 titles will be rigor-tested when those chapters are drafted.
- **Category:** sweep-discipline · craft · framework consistency
- **Content:** During Ch 9 holistic review, the author surfaced the diagnosis that the original chapter title "The Renewable Imperative" was likely a carry-over from before the Book 1 / Book 2 split (per `tools/commons_bonds_book_scope_v1_0_3.md` v1.0.3 §6.1). The chapter's substantive content had been disciplined into Book 1 scope through prior sweeps (explicit "framework, not blueprint" framing; "framework's role here is structural observation, not advocacy" framing in tax-tradeoff section; "this is not a legislative blueprint. It is a framework" closing). But the title itself had not been swept for Book-1/Book-2-split-carry-over. The full-depth Round 1+2+3 chapter-title rigor pass (`tools/rigor-passes/commons_bonds_rigor_pass_2026-04-27_ch9_title_candidates_v1.0.0.md`) confirmed the diagnosis was rigor-grounded — the original title failed simultaneously on M3.4 + M6 + M8 + M9 + M10 + M11 + §22.4 modules. Author ratified replacement title "Pricing Honestly" 2026-04-27.
- **Why it matters:** the chapter-by-chapter prose-sweep discipline memory rule (per `feedback_always_expand_rule.md`) names "every prose element in every chapter (not just newly-drafted AUTHOR ZONE passages)" as in-scope, with three rigor questions. **Chapter titles are prose elements.** They should fall in the same sweep that catches terminology regressions, vocabulary mismatches, applied-advocacy-vs-framework-establishment register drift, and Book-1/Book-2-split carry-overs. Without explicit memorialization, future sweeps may miss title-level concerns the way the Ch 9 sweep nearly missed "Renewable Imperative." The Ch 7 title swap from "The Colony Administrator" to "On Other Worlds" was caught under separate vocabulary-sweep discipline; the Ch 9 title swap was caught only because the author flagged the political-charge concern. The discipline gap is real and worth closing.
- **What would resolve this:** memory-rule clarification adding chapter titles to the chapter-by-chapter sweep scope, OR formal capture as Working Principle, OR addition to the protocol document. The clarification should specify: (a) chapter titles are prose elements; (b) sweeps should check title for Book-1/Book-2-split carry-over, applied-advocacy register drift, and vocabulary regressions; (c) title rigor passes follow the same protocol as Ch 7 and Ch 9 title rigor passes (full 14-module evaluation when carry-over or register concern surfaces).
- **Verification sweep recommended:** the remaining Book 1 chapters with titles already in the set (Ch 2 "The Miner"; Ch 4 "The Existence Proof"; Ch 5 "The Accountability Gap"; Ch 6 "Three Ways of Counting"; Ch 8 "What Things Actually Cost"; Ch 10 "Common Bonds") have already passed informal sweep per the Ch 9 set-rigor analysis (none carry obvious carry-over concerns). Ch 1 + Ch 3 are not yet drafted; their titles should be rigor-tested when they land. The set-level rigor analysis (Ch 9 title rigor pass §10) may be worth memorializing as a once-per-major-revision check.
- **Dependencies / Links:** `feedback_always_expand_rule.md` (memory rule on chapter-by-chapter sweep discipline — UPDATED 2026-04-27 to include chapter titles + section headers); MEMORY.md index hook updated 2026-04-27; Ch 7 title rigor pass (`commons_bonds_rigor_pass_2026-04-26_ch7_title_candidates_v1.0.0.md`); Ch 9 title rigor pass (`commons_bonds_rigor_pass_2026-04-27_ch9_title_candidates_v1.0.0.md`); v1.0.3 §6.1 book-scope governance; `tools/commons_bonds_rigor_protocol_v2.2.0.md`.
- **Todo link:** N/A (closed).

---

### Insight #23 — Community Transition Reserve (CTR) Book-1-vs-Book-2 boundary question — deferred for combined deliberation across Ch 2 + Ch 9

- **Raised:** 2026-04-27 by Chris Winn during Ch 9 Phase 3 surfacing ("Let's save the discussion on CTR for later as it feels like I'm suggesting a solution vs. talking about a framework. I want to sit with this a bit and see if I still feel that in a day or so or if there is a different angle I can approach this where that doesn't feel like what I'm doing."). Cross-chapter scope flagged 2026-04-27 during Ch 2 holistic review when the Ch 2 line 97 CTR mention surfaced as another instance of the same boundary question.
- **Status:** **closed-ratified 2026-04-27 (Chris Winn) — Path 2 selected; Version G (D + subsidy clarification) integrated across Ch 2 + Ch 9 in Book-2-mention-free form pending Insight #24 resolution.** Original "raised · deferred · cross-chapter scope identified · pending combined deliberation" status superseded by the ratification.
- **Category:** book-scope · framework boundary · craft
- **Content:** "Community Transition Reserve" appears as a defined-instrument noun in two chapters:
  - **Ch 2 line 97** (THE MINER): "The community transition reserve — the fund that should have been set aside to retrain workers, maintain services during the adjustment, attract replacement industries, keep the hospitals open — was never established, because establishing it would have reduced the profitability of extraction. So when the extraction ended, the community absorbed the full cost of transition alone. It is still absorbing it." Framing: structural-historical observation ("was never established"). The instrument is named without prescription about future implementation; the description is what didn't happen rather than what should be built. Gentler register than Ch 9's mention.
  - **Ch 9 line 125** (PRICING HONESTLY, formerly THE RENEWABLE IMPERATIVE): "The Community Transition Reserve mechanism — a sovereign wealth instrument funded by the resource rents of extraction, structurally designated for the communities bearing the direct spatial cost, paying out over the entire life cycle of the extraction and its externality tail — is the framework's answer to the distributional problem." Framing: prescriptive ("is the framework's answer to..."). The instrument is named with prescriptive language about what the framework recommends.
- **The boundary question:** does CTR-as-named-instrument cross from Book 1 (framework-naming + framework-establishment) into Book 2 (applied-advocacy + policy-prescription) territory? The author's instinct on this is captured in their 2026-04-27 framing: it "feels like I'm suggesting a solution vs. talking about a framework." The chapter-by-chapter prose-sweep discipline that caught the "Renewable Imperative" carry-over from before the Book-1/Book-2 split (per Open Insight #22) suggests the same sweep should engage CTR mentions across all chapters that name the instrument. The Ch 2 mention's gentler framing makes it a lighter case than Ch 9's; the Ch 9 mention's prescriptive framing makes it the load-bearing decision. Both have the same underlying question.
- **Why it matters:** if CTR-as-named-instrument violates Book 1 scope discipline, the term's appearance in two chapters is structurally inconsistent with the discipline the rest of the book maintains. The chapters have been disciplined into Book 1 scope (per Open Insight #15 standing thread + the explicit "framework, not blueprint" landings, "framework's role here is structural observation, not advocacy" framings, "this is not a legislative blueprint. It is a framework" closings); CTR mentions may be the only places where the discipline is partially relaxed. Resolving this is not a single-mention fix; it requires a Book-1-scope-aligned framing for the underlying question (how does the framework engage the distributional question that CTR is currently named to address?) that lands consistently across both chapters.
- **What would resolve this:** the author has explicitly deferred the deliberation to allow time to find "a different angle ... where that doesn't feel like" solution-proposing. Three resolution paths the deliberation might land on:
  1. **Retain CTR as named instrument** — accept the Book-1 boundary as inclusive of named instruments described historically (Ch 2 form) and named structurally (Ch 9 form); maintain current text.
  2. **Replace CTR with structural framing only** — name the distributional question without naming the specific instrument; let the question stand without proposing the specific mechanism. Both chapters revised.
  3. **Retain CTR in Ch 2 (historical-observation register) and revise Ch 9 (currently prescriptive)** — accept that Ch 2's "should have been set aside" framing stays within Book 1 scope (describes what didn't happen) while Ch 9's "is the framework's answer" framing crosses into Book 2. Asymmetric treatment.
  
  The author may also surface a fourth resolution path the rigor pass has not anticipated.
- **Dependencies / Links:** Open Insight #22 (chapter-titles-in-sweep-scope; same sweep-discipline-gap pattern); v1.0.3 §6.1 book-scope governance; `feedback_always_expand_rule.md` (chapter-by-chapter sweep rule); Ch 2 holistic review 2026-04-27 (where the Ch 2 instance was surfaced); Ch 9 Phase 3 surfacing 2026-04-27 (where the deferral originated).
- **Todo link:** "Review Open Insight #23: Community Transition Reserve Book-1-vs-Book-2 boundary question (deferred; sit with it). Resolve across Ch 2 + Ch 9 simultaneously when the deliberation lands."

---

### Insight #24 — Book 1 references to Book 2 — full rigor + question pass needed

- **Raised:** 2026-04-27 by Chris Winn during Ch 2 holistic-review CTR rigor exercise. Author framing: *"I'm yet not convinced that we should mention a book 2 in book 1."*
- **Status:** **closed-ratified 2026-04-27 (Chris Winn) — Scenario B selected; all Book 2 references removed from Book 1.** Full-depth rigor pass executed 2026-04-27 produced decisive verdict (Scenario B at +13 net rigor; Scenario A at 0; Scenario C at 0). Five surgical edits across Ch 5 + Ch 8 integrated 2026-04-27. Original "raised · pending full rigor + question pass · author skeptical" status superseded by ratification.
- **Category:** book-scope · framework boundary · publishing path · craft
- **Content:** During Ch 2 holistic-review CTR rigor exercise, the recommended Version G (principle-first + subsidy clarification) included an explicit cross-reference to Ch 8's closing section that references Book 2 by working title (*The Subsidy Economy*). The author flagged the broader question of whether Book 1 should reference Book 2 at all. Currently Book 1 contains at minimum:
  - **Ch 8 closing (lines 231-247)** — explicit "subject of a different book ... working title is *The Subsidy Economy*" framing; structurally treats Ch 8's closing as a Book 2 forward-pointer
  - **Possibly other forward-pointers in Ch 9 / Ch 10** — verification sweep needed; the recommended Version G CTR resolution would add another reference in Ch 9 if ratified
- **The boundary question:** does Book 1's identity as a self-contained framework book require absence of Book 2 references? Or do Book 2 references serve scope-discipline by explicitly naming what THIS book doesn't do (and where that work lives)?

  **Pro-mention argument:** explicit Book 2 references operationalize scope-discipline by deferring specific applied-advocacy questions to Book 2; without the deferral mechanism, Book 1 may be tempted to half-do Book 2's work. Naming Book 2 is the framing device that makes "framework, not blueprint" credible.

  **Anti-mention argument:** Book 1 should stand alone. References to a future book may read as: (a) premature publishing commitment; (b) implicit promise of more material that may not materialize on the timeline implied; (c) scope-bridging that undermines Book 1's self-contained identity; (d) editorial/craft cost — readers may flag "why mention a sequel?"; (e) potential reader-frustration if Book 2 takes longer than implied or doesn't materialize at all.

- **What would resolve this:** full rigor + question pass following the same protocol as Open Insights #22 (chapter-titles-in-sweep-scope) and #23 (CTR boundary question). Pass would evaluate:
  - Module-level rigor on Book 2 references (M1.5 / §22.4 / M3.4 / M9 / M10 publishing path / M11 / M12)
  - Greatness question (does Book 1 stand alone better with or without Book 2 references?)
  - Standing-the-test-of-time question (does mentioning a future book age well or poorly?)
  - Identification of all Book 2 references currently in Book 1 (verification sweep across all chapters)
  - Three resolution paths: retain all references / remove all references / asymmetric (some retain, some remove)

- **Connection to Open Insight #23:** the recommended Version G framing for the CTR resolution explicitly references Ch 8's *Subsidy Economy* framing as a Book 2 forward-pointer. **If Insight #24 resolves toward removing Book 2 references, Version G needs revision; Versions D / E / F (which can be revised to not reference Book 2 by name) become more attractive.** The two insights should be deliberated together OR Insight #24 should be resolved before Insight #23 final integration.

- **Insight #23 update 2026-04-27:** author selected Path 2 — ratified Version G structurally (D + subsidy clarification) but integrated in BOOK-2-MENTION-FREE form pending Insight #24 resolution. Specifically: Ch 2 line 97 + Ch 9 line 125 both received Version G prose, but the *Subsidy Economy* / Book 2 working-title reference that the original Version G Ch 9 draft included was removed. If Insight #24 resolves toward keeping Book 2 references being acceptable, Ch 9 line 125 can be lightly enhanced to add the *Subsidy Economy* reference back. If Insight #24 resolves toward removing Book 2 references, Ch 8 closing lines 231-247 will need parallel revision (and the integration is already aligned with that direction).

- **Dependencies / Links:** Open Insight #23 (CTR boundary question — direct connection); Open Insight #22 (chapter-titles-in-sweep-scope — methodologically similar Book-1/Book-2-discipline question); v1.0.3 §6.1 book-scope governance; Ch 8 lines 231-247 closing section.

- **Todo link:** "Review Open Insight #24: Book 1 references to Book 2 — run full rigor + question pass; identify all Book 2 references in Book 1; resolve before/with Insight #23 CTR final integration."

---

### Insight #25 — Book-level audience choice — CLOSED-RATIFIED 2026-04-28 (Option B + supplementary D)

- **Raised:** 2026-04-28 by Chris Winn during the intergenerational-cluster vocabulary rigor-pass methodology refinement. Author articulation: *"let's ask the question about a holistic strategy to approach when to leverage terminology I create for the framework/book, when to replace with academic words, when to replace with prose from the perspective of what is the right answer for the intended audience the book is trying to reach as well as the additional audiences the book will need to reach based on subject matter, publisher, and literary agent."* Followed by clarification that audience choice is a book-level question (not per-term) requiring its own rigor test prior to the terminology strategy.
- **Status:** **closed-ratified 2026-04-28 (Chris Winn) — Option (a) full ratify Option B (academic-trade hybrid) primary + Option D (policy-practitioner) supplementary in adoption-travel chapters.** Full-depth rigor pass executed 2026-04-28 (`tools/rigor-passes/commons_bonds_rigor_pass_2026-04-28_book_audience_choice_v1.0.0.md`); six audience options enumerated (A trade / B academic-trade hybrid / C pure academic / D policy-practitioner / E public-intellectual / F cross-tradition); B dominates 7 of 10 criteria in cross-option matrix; loses on success-criterion-reachability only (mitigated by D supplementation).
- **Category:** publishing · craft · framework boundary · vocabulary
- **Content:** *Commons Bonds* is written to the academic-trade hybrid crossover audience (Mazzucato / Raworth / Anderson / Sen / Acemoglu-Robinson / Stiglitz / Hickel register; Princeton / Yale / Harvard / MIT / U-Chicago press landing) as primary register, with policy-practitioner (Brookings / Roosevelt-Institute / Tooze) supplementary register in chapters where legal/policy adoption-travel is the success-criterion (Ch 9 *Pricing Honestly* canonical; Ch 7 instrument-design sections; Ch 10 regulatory-architecture sections).
- **Decisive findings (full detail in rigor pass file):**
  1. Content profile (math + multi-discipline lineage + Option-C' cross-tradition + personal narrative + 18 case studies) only threads through B without sacrificing components.
  2. Author intuition (*"approachable for non-economists; not dismissed by economists"*) IS the B brief.
  3. Success criterion (severed-cost into legal/policy vocabulary) requires D supplementation.
  4. Author voice already operates in B; switching to A/C/D/E/F primary would require substantial voice rewrite.
  5. Realistic publisher landing is the major academic-trade presses (Princeton/Yale/Harvard/MIT/U-Chicago/Belknap/Norton-academic-trade).
  6. M11 critic-survival is strongest under B.
- **Implementation implications (per rigor pass §10):**
  - Terminology rigor pass (`commons_bonds_rigor_pass_2026-04-28_intergenerational_cluster_vocabulary_consolidation_v1.0.0.md`) inherits B + supplementary D as fixed input. Tier A→D decision rule reshapes accordingly.
  - Suffix-convention coherence test runs against B reader (Mazzucato/Raworth profile) as audience-of-record.
  - Vocabulary strategy scaffolding doc (`alignment/commons_bonds_vocabulary_strategy_v1.0.1.md`, to be drafted) codifies the audience as standing input for future vocabulary decisions.
  - Each chapter's drafting calibrates explicitly: B default; D modulation in Ch 9 + Ch 7 instrument-design + Ch 10 regulatory-architecture sections; light F-flavor preserved within B in Ch 4 + Ch 10 cross-tradition sections.
  - Marketing positioning leverages B + supplementary D: comp titles Mazzucato/Raworth/Anderson; realistic publisher targets the major academic-trade presses; realistic agent class is the specific subset who represent academic-trade hybrid authors.
- **Dependencies / Links:** Rigor pass file `tools/rigor-passes/commons_bonds_rigor_pass_2026-04-28_book_audience_choice_v1.0.0.md`; downstream rigor pass `commons_bonds_rigor_pass_2026-04-28_intergenerational_cluster_vocabulary_consolidation_v1.0.0.md`; downstream scaffolding doc `alignment/commons_bonds_vocabulary_strategy_v1.0.1.md` (to be drafted); v1.0.3 §6.1 book-scope governance; Working Principles file (possible new Principle #7 codifying audience-discipline as standing commitment).
- **Todo link:** Reshape cluster vocabulary rigor pass with B+D as fixed input; draft vocabulary strategy scaffolding doc; consider drafting new Working Principle #7.

---

### Insight #26 — Vocabulary decision framework shape — CLOSED-RATIFIED 2026-04-28 (Option 1 four-move A/B/C/D + refinements)

- **Raised:** 2026-04-28 by Chris Winn during vocabulary strategy scaffolding doc review: *"do a rigor pass on if the four-move framework is the right shape or if it should be framed differently."*
- **Status:** **closed-ratified 2026-04-28 (Chris Winn) — verdict (a) full ratify Option 1 four-move A/B/C/D framework + refinements (a) and (b).** Focused rigor pass executed 2026-04-28 (`tools/rigor-passes/commons_bonds_rigor_pass_2026-04-28_vocabulary_decision_framework_shape_v1.0.0.md`); 8 alternative shapes enumerated (3-move collapses, 5-move D split, two-axis matrix, continuous spectrum, role-first framing, decision-tree); Option 1 dominates 5 of 6 criteria; 8 of 8 past framework vocabulary decisions map cleanly via hindsight test.
- **Category:** vocabulary · method
- **Content:** Four-move A/B/C/D framework (Tier A academic verbatim / Tier B academic + specialization / Tier C descriptive prose / Tier D framework coinage) ratified as the standing shape for vocabulary discipline. Refinement (a): §5 D-modulation guidance covers engineered-for-adoption-travel design intent (D1/D2 distinction operationally captured without elevating to separate tier slot); Refinement (b): §4 of vocabulary strategy doc gets supplementary decision-tree representation for pedagogical accessibility.
- **Implementation:**
  - `alignment/commons_bonds_vocabulary_strategy_v1.0.1.md` v1.0.0 → v1.0.1 with refinements applied: §4.5 decision-tree representation added; §5.5 engineered-for-adoption-travel design intent added.
  - Four-move framework cited as standing-shape reference in all future vocabulary decisions.
- **Dependencies / Links:** Rigor pass file `commons_bonds_rigor_pass_2026-04-28_vocabulary_decision_framework_shape_v1.0.0.md`; scaffolding doc `alignment/commons_bonds_vocabulary_strategy_v1.0.1.md`; book-audience rigor pass (RATIFIED 2026-04-28 Insight #25).
- **Todo link:** Apply refinements to vocabulary strategy scaffolding doc.

---

### Insight #27 — Vocabulary strategy scaffolding doc v1.0.1 — CLOSED-RATIFIED 2026-04-28

- **Raised:** 2026-04-28 by collaborative drafting during cluster vocabulary rigor pass execution. Author articulation: *"let's capture the resulting solution/approach that we decide on in a scaffolding document like core/terms/terms_index.md."*
- **Status:** **closed-ratified 2026-04-28 (Chris Winn) — v1.0.1 with refinements per Insight #26 applied.** The scaffolding document codifies the standing vocabulary discipline that flows from the ratified book-level audience (Insight #25) and the ratified four-move framework shape (Insight #26). Future framework vocabulary decisions inherit this discipline without re-running the audience or methodology rigor passes.
- **Category:** vocabulary · method · scaffolding
- **Content:** `alignment/commons_bonds_vocabulary_strategy_v1.0.1.md` (now v1.0.1 with refinements) is the standing source-of-truth for vocabulary decisions. Sits alongside `commons_bonds_working_principles_v1.0.0.md` as parallel discipline-record. Sections §1-§12 cover: scope; inherited audience input (B + supplementary D); four vocabulary moves (Tier A/B/C/D); decision rule + decision-tree supplement; D-modulation guidance + engineered-for-adoption-travel design intent; suffix-convention discipline; capitalization-discipline; cross-political-tradition robustness; decision-record format; worked examples (selection deferred per author 2026-04-28); versioning + revision triggers; cross-references.
- **§10 case-study selection — deferred:** audience for scaffolding is Chris + AI assistants applying discipline to future vocabulary decisions; case studies serve future-AI pattern-matching but per-term rigor passes themselves are the canonical examples. Explicit selection deferred until specific vocabulary decision needs a worked-example anchor.
- **Implementation:**
  - Document committed at v1.0.0 (cae3c70); refined to v1.0.1 (this commit).
  - Cited as standing-discipline reference from terms_index entries + future per-term rigor passes.
- **Dependencies / Links:** Scaffolding doc file; book-audience rigor pass (Insight #25); vocabulary framework shape rigor pass (Insight #26); cluster vocabulary rigor pass (in flight); architecture rigor pass S1 schema (`commons_bonds_rigor_pass_2026-04-27_publication_architecture_terms_index_glossary_tech_appendix_v1.0.0.md`).
- **Todo link:** Update `MEMORY.md` to reflect new standing discipline document; consider drafting new Working Principle #7 codifying audience-discipline as standing commitment.

---

### Insight #28 — Retirement traces / scaffolding-vs-publisher-facing — CLOSED-RATIFIED 2026-04-28

- **Raised:** 2026-04-28 by Chris Winn during Value Capture sweep scope discussion: *"perhaps this is the sort of thing that's perfect to keep living in scaffolding along with reasons that we regressed the use of that term/word/etc. and that means the publisher facing documents will be scrubbed clean."*
- **Status:** **closed-ratified 2026-04-28 (Chris Winn) — verdict (a) full ratify A2 + L2 + S1.** Refines Working Principle #4 (Retirements preserve their history in-document, ratified 2026-04-24) by surfacing a missing third tier — scaffolding / decision-record documents — that the existing Tier 1 / Tier 2 dichotomy elides. Provides per-folder Tier classification across the repo + concrete Value Capture sweep plan + routine 1 Tier-aware exclusion update.
- **Category:** vocabulary · method · scaffolding · publishing
- **Content:** Three-tier classification ratified:
  - **Tier 1 — Reader-facing (publisher-facing) live documents** → SWEEP retired terms (manuscript chapters, current glossary v3, current Tech Appendix, current case-study audits, research case-study writeups).
  - **Tier 2 — Reader-facing archived / superseded versions** → header-note retirement annotation; body intact (archived prior glossary versions, archived Tech Appendix versions, archived sessions, archived rigor protocol versions).
  - **Tier 3 — Scaffolding / decision-record / author-facing** (NEW) → preserve all retirement traces in full (terms_index, rigor passes, working principles, open insights, current sessions, alignment patches, tools/routines, core/scaffolding).
  - Per-instance lowercase judgment (Axis L2): proper-noun "Value Capture" sweeps uniformly; lowercase "value capture / value captured" reviewed for framework-vs-descriptive-English sense.
  - Routine 1 Tier-aware exclusion (Axis S1): exclusion list reframed to Tier 3 scaffolding paths (principled rule that scales to future retirements without per-term routine updates).
- **Implementation phases triggered:**
  1. Update Working Principle #4 — add Tier 3 row to format table.
  2. Apply Value Capture → Value Extraction publisher-facing sweep per rigor pass §4 plan: Ch 4 (1), Ch 5 (4), glossary v3 (2), case-study audit (4), research case studies (~7 with per-instance review), tools/rigor-protocol (1).
  3. Update routine 1 — Tier-aware exclusions + add `\bValue Capture\b` regression pattern.
- **Dependencies / Links:** Rigor pass file `commons_bonds_rigor_pass_2026-04-28_retirement_traces_scaffolding_vs_publisher_facing_v1.0.0.md`; Working Principle #4 (`alignment/commons_bonds_working_principles_v1.0.0.md`); routine 1 in claude.ai; Value-Capture-vs-Extraction rigor pass `commons_bonds_rigor_pass_2026-04-24_term_value_capture_vs_extraction_v1.0.0.md`.
- **Todo link:** Apply Value Capture → Value Extraction publisher-facing sweep (Phases 1-3); ratify Working Principle #4 Tier-3 row addition.

---

### Insight #29 — Working Principle #8 (Publisher-facing artifacts scrubbed of scaffolding/audit-trail content) — CLOSED-RATIFIED 2026-04-28

- **Raised:** 2026-04-28 by Chris Winn during the cluster vocabulary rigor pass synthesis review. Author articulation: *"regarding the Tier 3 / scaffolding-vs-publisher-facing principle in the still-PROPOSED retirement-traces rigor pass — scaffolding is internal; reasoning chains preserved in the rigor passes themselves; don't over-engineer for external readability. Let's expand that to every external facing document. So all chapter drafts, glossary items, and technical appendix."*
- **Status:** **closed-ratified 2026-04-28 (Chris Winn) — full ratification of Working Principle #8 generalizing the retirement-traces Tier 1 / Tier 3 split to ALL scaffolding/audit-trail content.** Two scope clarifications also confirmed: (i) prospective application only — no retroactive sweep of existing chapter drafts (routine 2 catches violations naturally during pre-submission readiness audit); (ii) lineage citations + framework-specialization footnotes are explicitly OUT of scope for scrub (they serve the reader, not the audit trail).
- **Category:** scaffolding · publishing · framework-discipline · publisher-facing
- **Content:** Generalizes the principle from the retirement-traces rigor pass (Insight #28) — instead of just retirement-traces being scrubbed from publisher-facing artifacts and preserved in scaffolding, ALL scaffolding/audit-trail content gets that treatment. Specifically, publisher-facing artifacts (Tier 1: chapter drafts, glossary, Tech Appendix, research case-study writeups) carry only reader-facing content. They DO NOT carry: rigor-pass commit references, M11 critic-survival probes inline, "Per Insight #N" / "Per Working Principle #M" cross-references, decision-record narratives, status indicators (CURRENT/RETIRED inline markers), version-progression archaeology, author-meta-notes, rigor-pass commit references. Reasoning chains for ALL framework decisions live exclusively in Tier 3 scaffolding documents (terms_index, rigor passes, working principles, vocabulary strategy, open insights, sessions, alignment patches).
- **Out of scope for scrub** (these stay in publisher-facing artifacts because they serve the reader): lineage citations on first-use; Tier B framework-specialization footnotes; Tech Appendix §L methodological footnotes that situate the framework in established traditions; reader-facing cross-references between chapters; case-study sources / data citations.
- **Implementation:**
  1. Working Principle #8 added to `alignment/commons_bonds_working_principles_v1.0.0.md` (this commit).
  2. Retirement-traces rigor pass §3 updated with note generalizing Tier 1 / Tier 3 split per Principle #8 (this commit).
  3. Vocabulary strategy scaffolding doc §9.5 added — publisher-facing-scrubbing discipline cross-reference (this commit).
  4. Phase 3 Tech Appendix v2.0.0 rebuild + Phase 4 Glossary v4 rebuild inherit Principle #8 as standing input (when those phases land).
  5. Routine 2 (pre-submission readiness audit) — pattern checks expand to include scaffolding-content patterns. (Separate update via RemoteTrigger; deferred to follow-up commit.)
- **Application discipline:** prospective only. Current chapter drafts may contain residual author-meta-notes etc. that get cleaned during normal pre-submission readiness audit (routine 2), not via dedicated retroactive sweep.
- **Interaction with other principles:**
  - Principle #4 (retirements preserve their history in-document) — Principle #8 generalizes Principle #4's retirement-trace logic to ALL audit-trail content.
  - Principle #7 (pre-publication-state discipline) — Principle #8 reinforces: pre-publication artifacts that get scrubbed before publication don't carry the audit trail forward.
- **Dependencies / Links:** Working Principle #8 file location; retirement-traces rigor pass `commons_bonds_rigor_pass_2026-04-28_retirement_traces_scaffolding_vs_publisher_facing_v1.0.0.md` (Insight #28); vocabulary strategy scaffolding doc `alignment/commons_bonds_vocabulary_strategy_v1.0.1.md` §9.5; architecture rigor pass `commons_bonds_rigor_pass_2026-04-27_publication_architecture_terms_index_glossary_tech_appendix_v1.0.0.md` (Phase 3 + Phase 4 rebuild deliverables inherit Principle #8); routine 2.
- **Todo link:** Update routine 2 pattern-check list to include scaffolding-content patterns (separate commit).

---

### Insight #30 — Hotelling Identity attribution review — CLOSED-RATIFIED 2026-04-28

- **Raised:** 2026-04-28 by Chris Winn during cluster vocabulary rigor pass review: *"Hotelling Identity as mentioned in the book is actually a derivative of Hotelling's work he did a long time ago, but I'm taking that work and adding to it with the 'Hotelling Identity' as mentioned in the Chapter. See if that should be in the in the glossary / terms_index as well as how that should be cited. I don't recall how I left it in the latest edit... I think I might have awkwardly mention it's Hotelling's work three times in the Technical Appendix but don't really clearly explain what is mine and what is his, and I honestly need you to review how that is cited in the Chapter as well. And for that matter how I'm taking the Hotelling rent and using that in the formula."*
- **Status:** **closed-ratified 2026-04-28 (Chris Winn) — verdict (a) ratify minor cleanup pass per `commons_bonds_rigor_pass_2026-04-28_hotelling_identity_attribution_review_v1.0.0.md` §5.** Underlying attribution discipline ratified 2026-04-24 is sound; cleanup needed only for 3 Working Principle #8 violations in Tech Appendix §4 + numbering inconsistency + Tier-classification of Ch 6 supplementary drafts file.
- **Category:** vocabulary · framework-discipline · publisher-facing · attribution
- **Content:** Hotelling Identity is the framework's extension of Hotelling 1931, not a coinage. terms_index entry §1816-1822 is explicit on the attribution split (Hotelling's part vs framework's part). Tech Appendix §5.1/5.2/5.3 cleanly separates the two contributions. Hotelling rent appears ONLY in the bridging Identity (RCV − Hotelling rent = CS per unit), NOT in the primary CS = RCV − B equation — clean attribution. Chapter 6 HTML line 799 handles attribution discipline correctly.
- **Cleanup applied 2026-04-28:**
  1. Tech Appendix §4 attribution paragraph — removed "Source: Hotelling Identity individual rigor pass (commit `5b8ff42`); see `core/terms/terms_index.md`..." sentence + standalone "Source rigor pass: Hotelling Identity (commit 5b8ff42)." line (Working Principle #8 scrub).
  2. Renumbered §5.1/5.2/5.3 → §4.1/4.2/4.3 (mechanical fix).
  3. Reframed §4.3 (formerly §5.3) — removed "Per M12 module + Working Principle #6:" framing + meta-commentary closing line; replaced with reader-facing "Citation discipline. Anywhere the framework references the Hotelling Identity, the canonical attribution form is:" framing.
  4. Fixed line 638 cross-reference: "see §5 Hotelling Identity" → "see §4 Hotelling Identity".
  5. **Tier classification of `Chapter__6___SupplementaryDrafts_2026-04-24.md`** — resolved as Tier 2 archive (file moved to `manuscript/chapters/archive/` 2026-04-28 with archive header note documenting content disposition). Line 297 rigor-pass-record cross-references preserved as Tier 2 historical trace per retirement-traces rigor pass discipline.
- **Dependencies / Links:** Hotelling Identity attribution review rigor pass; underlying 2026-04-24 ratification at `commons_bonds_rigor_pass_2026-04-24_term_hotelling_identity_v1.0.0.md`; retirement-traces rigor pass (Insight #28); Working Principle #8 (Insight #29).

---

### Insight #31 — Three Ways of Counting (renamed from "Triangulated RCV Estimation") — CLOSED-RATIFIED 2026-04-28

- **Raised:** 2026-04-28 by Chris Winn during cluster vocabulary rigor pass review: *"For the other item in the Suffix-convention coherence 'Triangulated RCV Estimation' that is the result from the 3 ways test and should probably have a cleaner & more citable name... As it stands now the result is just referred to as 'triangulated three-method range'... perhaps that's all we really need?"*
- **Status:** **closed-ratified 2026-04-28 (Chris Winn) — Option B verdict per `commons_bonds_rigor_pass_2026-04-28_triangulated_rcv_estimation_naming_review_v1.0.0.md`.** Drop "Triangulated RCV Estimation" as separate Ring-2 term; promote "Three Ways of Counting" as primary methodology name; preserve "the triangulated three-method range" as inline result description.
- **Category:** vocabulary · framework-discipline · parsimony
- **Content:** Framework had 3 names for the same thing (formal "Triangulated RCV Estimation" + pedagogical "Three Ways of Counting" + result-description "the triangulated three-method range"). Per Working Principle #1 parsimony + four-move tier ladder, "Three Ways of Counting" alone serves as both pedagogical and primary methodology name. The three Methods themselves (Replacement Cost; Revealed Preference; Scarcity-Adjusted Option Value) carry their own academic lineage — Costanza 1997, Hartwick 1977 + Solow 1974, Dixit + Pindyck 1994 + Henry 1974 + Arrow + Fisher 1974. Removes the one-off `-Estimation` suffix.
- **Implementation applied 2026-04-28:**
  1. terms_index entry header renamed: `### Triangulated RCV Estimation ("Three Ways of Counting" pedagogically)` → `### Three Ways of Counting (formerly "Triangulated RCV Estimation"; renamed 2026-04-28)` with supersession record.
  2. Tech Appendix §B "Sources:" block — removed "Triangulated RCV Estimation" reference + WP#8-violating rigor-pass commit references (3 commits: 1c8e4dd, 4f48c48, 5dea091); simplified to clean prose.
  3. Tech Appendix §B "Source rigor passes:" line — removed (rigor-pass commit references; WP#8 scrub).
  4. Tech Appendix §I "Hotelling Identity instead" passage line ~6353 — renamed "Triangulated RCV Estimation individual rigor pass" → "Three Ways of Counting individual rigor pass".
  5. Methods 1/2/3 sub-records preserved unchanged with academic lineage.
- **Pending:** routine 1 pattern-list update to add `\bTriangulated RCV Estimation\b` as retired-vocabulary regression pattern (separate RemoteTrigger update).
- **Dependencies / Links:** Triangulated RCV Estimation naming review rigor pass; Working Principle #1 parsimony + Corollary B (CSG retirement origination 2026-04-24); vocabulary strategy v1.0.1 §3 four-move tier ladder.

---

### Insight #32 — Cluster items-not-flagged batch rigor — CLOSED-RATIFIED 2026-04-28 (24 items PASS)

- **Raised:** 2026-04-28 by Chris Winn: *"batch run all Items you did NOT flagging for specific review through the same full rigor, audience, and academic rigor tests."*
- **Status:** **closed-ratified 2026-04-28 (Chris Winn) — verdict (a) ratify all batch-tested verdicts as previously recommended.** All 24 items PASS full rigor + audience + academic rigor tests per `commons_bonds_rigor_pass_2026-04-28_cluster_items_not_flagged_batch_rigor_v1.0.0.md`. Cluster rigor pass §10.2 + §10.3 + §10.4 + §11.2 verdicts hold without modification.
- **Category:** vocabulary · framework-discipline · batch-verification
- **Content:** 24 items batch-tested across 5 categories: 9 Tier A borrowed academic concept adoptions (intergenerational equity / mobility / wealth transmission / transfers / fiscal architecture / transfer programs / obligations / claims / stocks); 7 Tier C descriptive prose preservation groups; 4 Tier D coinage defers (Lifetime Survival Cost / Community Disruption Cost / Political Capture Cost / Temporal Displacement Cost — all stay in Cᵢ illustrative-list at terms_index line 411 until cross-chapter recurrence emerges); 2 chapter-prose KEEP-per-existing-discipline (Ch 7:205 universality test lowercase; Ch 10 GuidanceDoc:119 FGC preserved per Tier-3); 11 Ch 5 cost severance KEEP verdicts. Common pattern: items not flagged because they don't change framework vocabulary set; batch run formally verifies discipline holds.
- **Dependencies / Links:** Items-not-flagged batch rigor pass; cluster vocabulary rigor pass §10 + §11; vocabulary strategy v1.0.1.

---

### Insight #33 — Group 3 Tier-1 sweep regressions ratified — CLOSED-RATIFIED 2026-04-29

- **Raised:** 2026-04-28 by Chris Winn during cluster vocabulary rigor pass review (Group 3 framework-word touches).
- **Status:** **closed-ratified 2026-04-29 (Chris Winn) — both Group 3 items applied.**
  - **Item 3.1** — *"industrial-existential substitutability gap"* renamed to **"existential substitutability gap"** per Candidate P verdict (`commons_bonds_rigor_pass_2026-04-28_csg_descriptive_prose_renaming_v1.0.0.md` §13.7). Multi-audience matrix (12 sub-audience cells) STRONG/STRONGEST across all cells. M11 + M12 + plagiarism/copyright/legal-exposure probes all SURVIVE with disambiguation discipline. Bostrom 2002 + 2014 + MacAskill 2022 + Ord 2020 existential-risk economics lineage citation added at Ch 7 first-introduction (line 117) with explicit disambiguation from longtermism's specific ethical commitments + framework's gap-concept positioned as one input to existential-risk reasoning.
  - **Item 3.2** — Ch 5:145 cost-severance compression Author Structure B applied 2026-04-29 (commit `90540b9`). Pattern: bbb-A-bb (drop "cost" prefix on instances 1, 2, 3; KEEP "cost severance" only on instance 4 immediately before climax). Multi-audience matrix STRONG/STRONGEST across 11 of 12 cells; specifically benefits socialist/communitarian reading by emphasizing the civilizational-scale public-finance line.
- **Category:** vocabulary · framework-discipline · attribution · publisher-facing
- **Implementation applied 2026-04-29:**
  1. terms_index CSG retirement record updated — preserved-prose-form citation changed from "industrial-existential substitutability gap" to "existential substitutability gap" + added 2026-04-29 rename note.
  2. Ch 7 *On Other Worlds* draft swept (~9 occurrences); disambiguation footnote added at line ~117 first introduction citing Bostrom + MacAskill + Ord lineage + explicit longtermism-disambiguation.
  3. Ch 9 *Pricing Honestly* draft swept (~15 occurrences) including Ch 9:247 specific case ("civilizational substitutability gap" → "existential substitutability gap" — resolves Tier-1 sweep regression).
  4. Tech Appendix v1.0.0 §G + scattered references swept (~17 occurrences); §3 sensitivity-analysis prose at line 4831 reframed ("industrial-existential extraction" → "extraction of resources with high existential substitutability gaps").
  5. Ch 5:145 paragraph compression applied (Author Structure B per §6.5 + §12).
- **Pending:** routine 1 pattern-list update — add `industrial.?existential substitutability gap` as retired-vocabulary regression pattern (separate RemoteTrigger update). Glossary v3 sub-entry rename deferred to Phase 4 v4 rebuild (auto-derives from terms_index per S1 schema).
- **Dependencies / Links:** CSG renaming rigor pass (Item 3.1); cluster rigor pass §11.2.12 (Item 3.2); Ch 5:145 chapter edit commit `90540b9`; Ch 7/Ch 9/Tech Appendix sweep + disambiguation footnote in this commit.

---

### Insight #34 — Group 2 Knowledge and Cultural Cost naming consistency — CLOSED-RATIFIED 2026-04-29

- **Raised:** 2026-04-28 by collaborative inventory work (cluster vocabulary rigor pass §10.4 surfaced the naming drift between Ch 8:105 "Knowledge and Cultural Cost" and Glossary v3:373 retired-list "Knowledge and Culture Cost").
- **Status:** **closed-ratified 2026-04-29 (Chris Winn) — verdict (a) C1 "Knowledge and Cultural Cost" as canonical form** per `tools/rigor-passes/commons_bonds_rigor_pass_2026-04-29_group2_knowledge_culture_cost_naming_v1.0.0.md`. Multi-audience matrix STRONG on 5 of 12 cells (Tier 2b legal/policy + Tier 2c intergenerational ethics + Tier 2d indigenous + heterodox + civic-republican + lived-oppression); ADEQUATE on 6; ADEQUATE-WEAK on 1 (Tier 3b academic-trade hybrid copy-editor concern, mitigable via editorial-review defense protocol). M11 + M12 + plagiarism/copyright/legal-exposure all SURVIVE/PASS.
- **Category:** vocabulary · framework-discipline · Cᵢ-class naming
- **Content:** Cᵢ-class extraction cost referring to community-knowledge-and-cultural-continuity loss compounding from community dispersal. Per Ch 8:107-113 chapter prose, the two facets (practical/ecological knowledge + cultural continuity / civic infrastructure) are conceptually unified ("the loss compounds"); single Cᵢ-class entry preferred over splitting (C3 split rejected per parsimony + chapter conceptual unity).
- **Decisive criterion:** Cross-political-tradition Option C' commitment (load-bearing per book-audience ratification 2026-04-28, Insight #25) favors C1's lived-oppression-reading + Tier 2d indigenous + heterodox-alignment STRONG fit. Cultural-loss vocabulary in lived-oppression literatures uses adjective form ("cultural genocide," "cultural erasure," "cultural extraction"); "Cultural [X]" pattern dominant in cultural-studies + indigenous-studies literatures.
- **Implementation applied 2026-04-29:**
  1. Glossary v3 line 373 retired-list entry — swept "Knowledge and Culture Cost" → "Knowledge and Cultural Cost"
  2. terms_index line 128 (8-tier-being-dissolved listing) — swept to match
  3. terms_index line 411 (Cᵢ illustrative-list) — already used C1 form (verified)
  4. Ch 8 line 105 subsection header — already C1 form (no edit needed)
- **Editorial-review defense protocol:** when academic-trade hybrid press copy-editor flags C1 mixed-parts-of-speech during pre-submission editorial review, framework defends C1 by citing rigor pass §4.1 (lived-oppression reading + Tier 2d indigenous + heterodox alignment) + Ch 8 prose context. If editor insists on C2, framework can defer at publication (single-form choice; rigor-pass record preserves the rationale).
- **Pending (low priority):** routine 1 pattern addition for "Knowledge and Culture Cost" (without "al") as retired-form regression pattern; deferrable.
- **Adjacent literature for future Tech Appendix §L methodological footnote** (when this Cᵢ promoted to dedicated terms_index entry): Bourdieu 1986 *The Forms of Capital* (cultural capital framing); Lemkin 1944 *Axis Rule in Occupied Europe* (cultural genocide concept); UN-IP-Declaration 2007 (cultural rights); Polanyi 1958 *Personal Knowledge* (tacit knowledge); Scott 1998 *Seeing Like a State* (mētis / local knowledge); Ostrom 1990 *Governing the Commons* (community-embedded knowledge); Caudill 1962 *Night Comes to the Cumberlands* (Appalachian community-knowledge dispersal).
- **Dependencies / Links:** Group 2 rigor pass; cluster vocabulary rigor pass §10.4; book-audience Insight #25 (Option C' political-philosophical accommodation).

---

### Insight #35 — Cost Severance + Severed Cost Tier 2d Phase 2 deeper-dive — CLOSED-RATIFIED 2026-04-29

- **Raised:** 2026-04-29 by Phase 1 full framework audit §5.2 + §5.3 + §9.1 (flagged Tier 2d cross-political-tradition concern).
- **Status:** **closed-ratified 2026-04-29 (Chris Winn) — verdict (a) Full ratify all three enhancements + KEEP terms** per `tools/rigor-passes/commons_bonds_rigor_pass_2026-04-29_phase2_cost_severance_severed_cost_tier2d_v1.0.0.md`. Full 12-cell multi-audience matrix (vocabulary strategy v1.0.1 §2 + §8) at Phase 2 depth; M6 academic rigor + M11 critic-survival from 5 critic positions + M12 attribution-honesty depth audit + Ch 1 Option C bridge plan verification at Tier 2d depth. **No cell FAILS.** Tier 2a + Tier 2d + Lived-oppression conditional STRONG-with-enhancement / WEAK-without. Rename rejected (6 alternatives tested; none dominates).
- **Category:** vocabulary · framework-discipline · Ring-1 · cross-political-tradition robustness
- **Content:** Three concrete enhancements ratified:
  1. **M12 lineage citation expansion** to terms_index Cost Severance + Severed Cost Rigor-provenance — Coulthard 2014 *Red Skin, White Masks*; Tuck & Yang 2012 "Decolonization is not a metaphor"; Darity & Mullen 2020 *From Here to Equality*; Anderson 2017 *Private Government*; Patel & Moore 2017 *A History of the World in Seven Cheap Things*; Federici 2004 *Caliban and the Witch*; Hickel 2020 *Less Is More* + *The Divide*; Whyte (indigenous environmental ethics); Wolfe 1999 *Settler Colonialism*; DuBois / Robinson / Wilderson; Marx *Capital* Vol. 1; Demsetz 1967; Coase 1960 (severance-context); Hayek 1960; Pettit 1997; US severance-tax law (state statutes — Texas, Alaska, Wyoming, North Dakota, Montana; ~36 states).
  2. **Ch 1 Option C bridge prose extension** from one-register (labor-severance) to three-register (labor + severance-tax + colonial). v2 DRAFT ratified per Phase 2 §7.4; supersedes 2026-04-24 v1 single-register version. v1 preserved in terms_index Cost Severance entry as historical record per Working Principle #4.
  3. **Tech Appendix §L methodological footnote** on Cost Severance + Severed Cost commodification + decolonial framing + reparations-economics parallel. DRAFT in Phase 2 §8.2. **Placement choice (now vs Phase 3 Tech Appendix v2.0.0 rebuild) PENDING** per Phase 2 §12.3 open question.
- **Decisive criterion:** Rename rejected because no alternative dominates Cost Severance + Severed Cost across all 12 audience cells under genuine pass/fail discipline (Working Principle #1 effort-to-repair-not-rigor + author direction 2026-04-29 "this book being understandable and passing rigor each of these audiences is truly a pass/fail gate"). The Tier 2d concern is M12 lineage gap, not vocabulary fit gap; the term *severance* has multi-register strength (labor + severance-tax + property-law + colonial + capital-severance-of-labor-from-product) that the prior 2026-04-24 ratification under-invoked. Significant Tier 2b adoption-travel finding: severance-tax precedent (36 US states) is the existing legal vocabulary closest to what CSD/Restitution Bond/Foreclosure Bond extend.
- **Implementation applied 2026-04-29:**
  1. terms_index Cost Severance Rigor-provenance section — Phase 2 entry added; cross-political-tradition lineage section added (16+ citations across 7 traditions including US severance-tax law).
  2. terms_index Severed Cost Rigor-provenance section — Phase 2 entry added; cross-references Cost Severance lineage symmetrically.
  3. terms_index Cost Severance "Notes" section — canonical Ch 1 framing v2 (three-register extended) ratified; v1 (2026-04-24 single-register) preserved as historical record.
  4. M12 bridge-commitment discipline note updated to cover three-register bridge approach.
- **Pending implementation:**
  - **Tech Appendix §L methodological footnote placement decision** (now in TechnicalAppendix_v1.0.0.html vs batched into Phase 3 v2.0.0 rebuild) — Phase 2 §12.3 open question; awaits author choice.
  - **Ch 1 + Ch 3 conversational drafting session** (deferred per author direction 2026-04-29 — to follow remaining Phase 2 priority list + terms_index revision + scaffolding-vs-publisher-facing separation pass + word-count recompute). Chris will type personal stories + waterman stories; Claude asks follow-up questions as needed to meet chapter + bridge needs. Bridge prose v2 lands in Ch 1 during this session.
- **Phase 2 verdict on bridge effectiveness:** "PLAN HOLDS conditionally pending execution + enhancement." Execution = Ch 1 drafting to 5K-6K target with v2 bridge prose landed at appropriate placement. Until then, Phase 2 verdict is provisional.
- **Dependencies / Links:** Phase 1 full framework audit (`commons_bonds_rigor_pass_2026-04-29_full_framework_audit_phase1_v1.0.0.md`); 2026-04-24 Cost Severance collision pass + standalone pass + CS-vs-SC triage pass; vocabulary strategy v1.0.1 §2 + §8 12-cell multi-audience matrix; Working Principle #1 (effort-to-repair-not-rigor); Working Principle #8 (publisher-facing scaffolding scrub); Insight #36 (deferred Ch 1 + Ch 3 conversational drafting session); Insight #37 (scaffolding-vs-publisher-facing separation pass + word-count recompute).

---

### Insight #36 — Ch 1 + Ch 3 conversational drafting session (deferred) — OPEN

- **Raised:** 2026-04-29 by author direction following Insight #35 ratification: *"Let's plan a session where I type my personal stories and stories from several watermen and let's make it a conversation where you ask additional information if / when needed to meet the needs of the chapter and the bridge as intended."*
- **Status:** **OPEN; deferred until prerequisites complete.**
- **Category:** chapter-drafting · session-design · Ch 1 + Ch 3
- **Content:** Conversational drafting session for Ch 1 (currently 1,446-word starter scaffold; target 5K-6K) + Ch 3 *waterman chapter* (currently 0 words; not yet drafted; target 5K-6K). Format: Chris types personal stories + stories from several watermen; Claude asks follow-up questions in real time to surface (a) bridge prose v2 placement + author-voice refinement (per Insight #35 enhancement 2); (b) Ch 1 personal-narrative spine completion (per Ch 1 GuidanceDoc + Personal Stories Candidates v1.0.0); (c) Ch 3 waterman-narrative draft from scratch (Hampton sailboat context + watermen stories + Ch 1 cross-reference); (d) the consent problem in its sharpest form (per Ch 1 §AUTHOR-ZONE-3); (e) lived-experience demonstration of each cost-category per Ch 1 GuidanceDoc lines 142-149. **Note:** Ch 2 *The Miner* is already drafted at ~5,200 words (within target); its outstanding work is 3 INTERVIEW NEEDED placeholders for McDowell County voices (former miner / miner's widow / young person who stayed / young person who left) — **separate from Chris's personal stories**; tracked as pending work §5.3 (interview-based drafting; not part of this Insight's scope).
- **Prerequisites (sequenced per author direction 2026-04-29):**
  1. Remaining Phase 2 priority list items completed (per Phase 1 §10 — Foreclosure Bond housing-crisis collision + theorem audit + RCV/Q(t)/scarcity multiplier bundle + Externality Tail statistics-tail collision + Three Ways of Counting post-rename verification; ~5 deeper-dive rigor passes).
  2. terms_index revision (lineage citation expansions; status sweeps; v0.1.0 → v1.0.0 version bump per session pending work §5.4).
  3. **Possibly:** scaffolding-vs-publisher-facing separation pass on each public-facing document (Insight #37) + word-count recompute (because current chapter-length tracking may include scaffolding content not present in actual publisher-facing prose).
- **Why deferred:** Ch 1 bridge prose v2 cannot be effectively author-refined until prerequisites complete. Specifically: word-count gap to 5K-6K target may differ substantially after scaffolding-vs-publisher-facing separation; Phase 2 priority items may surface additional vocabulary-discipline changes that would update bridge content; terms_index revision affects citation density Chris references during drafting.
- **Decision-needed at session start:** session length (likely multi-session work given Ch 1 partial + Ch 3 needs full drafting from 0 words). Whether to draft Ch 1 + Ch 3 together OR sequentially.
- **Dependencies / Links:** Insight #35 (Phase 2 ratification with bridge v2 ratified-but-not-applied); Insight #37 (scaffolding separation prerequisite); Phase 1 §10 remaining flagged items; session pending work §5.3 chapter-drafting list.

---

### Insight #37 — Scaffolding-vs-publisher-facing separation pass + word-count recompute — OPEN

- **Raised:** 2026-04-29 by author direction following Insight #35 ratification: *"possibly after we do a pass to separate the scaffolding from the publisher, agent, end reader view of each public facing document. As our document length estimates might include internal scaffolding words vs. what the actual end documents will actually include."*
- **Status:** **OPEN; pending decision (whether to do this pass now vs at chapter pre-submission editing).**
- **Category:** working-principle-application · publisher-facing-discipline · word-count-honesty
- **Content:** Working Principle #8 (Publisher-facing artifacts scrubbed of scaffolding/audit-trail content) generalized to apply across ALL public-facing documents — chapter drafts, glossary, Tech Appendix — with two specific deliverables:
  1. **Scaffolding-vs-publisher-facing separation:** identify scaffolding content (author-meta-notes; status indicators; "Per Insight #N" cross-references; rigor-pass commit references; M11 probe markers; AUTHOR-ZONE blocks; STARTER DRAFT SCAFFOLD framing notes; Register-discipline notes; etc.) vs publisher-facing content (actual prose readers will encounter) on a per-document basis. Quantify the split.
  2. **Word-count recompute:** current chapter-length tracking (Ch 1: 1,446 words; Ch 2: 5,200; Ch 4: 5,400; Ch 5: 5,800; Ch 6: 12,000; Ch 7: 5,500; Ch 8: 5,400; Ch 9: 5,600; Ch 10: 5,800) may include scaffolding content. True publisher-facing word counts may differ substantially. Recompute under WP#8 discipline.
- **Why this matters now:**
  - **Ch 1 drafting decisions** (Insight #36) depend on accurate publisher-facing word-count gap to 5K-6K target.
  - **Pre-submission readiness audit (routine 2)** already runs WP#8 pattern checks; this would extend the discipline to a deliberate one-time-pass rather than ongoing-sentinel.
  - **Tech Appendix v2.0.0 rebuild** (Phase 3 of architecture work) is the natural place to apply WP#8 at Tech Appendix scale; this insight surfaces whether to do similar pass on chapter drafts now or defer to chapter pre-submission editing.
- **Decision question for author:**
  - **(a) Do the separation pass now** — comprehensive across all chapters + glossary + Tech Appendix; produces accurate publisher-facing word counts; ~3-5 hours work.
  - **(b) Do per-chapter separation at pre-submission editing** — defer the comprehensive pass; handle each chapter's scaffolding scrub at the chapter's individual pre-submission editing cycle. May leave Ch 1 drafting (Insight #36) without accurate word-count target.
  - **(c) Partial separation now: Ch 1 + Ch 2 only** — separation only on the chapters Insight #36 will draft; defer the rest.
- **Dependencies / Links:** Working Principle #8; Insight #28 retirement-traces / scaffolding-vs-publisher-facing (RATIFIED 2026-04-28); Insight #36 (Ch 1 + Ch 3 conversational drafting session — depends on this pass for accurate word-count target).

---

### Insight #38 — Foreclosure Bond housing-crisis collision Phase 2 deeper-dive — CLOSED-RATIFIED 2026-04-29

- **Raised:** 2026-04-29 by Phase 1 full framework audit §6.14 (flagged housing-crisis connotation collision with post-2008 audience proximity).
- **Status:** **closed-ratified 2026-04-29 (Chris Winn) — verdict (a) Full ratify all three enhancements + KEEP term** per `tools/rigor-passes/commons_bonds_rigor_pass_2026-04-29_phase2_foreclosure_bond_housing_crisis_collision_v1.0.0.md`. Full 12-cell multi-audience matrix (vocabulary strategy v1.0.1 §2 + §8) at Phase 2 depth; M6 academic rigor + M11 critic-survival from 5 critic positions + M12 attribution-honesty depth audit + affective-valence dimension. Re-tested 2026-04-24 b1_b2_naming pass verdict against 12-cell matrix that did not exist at original ratification; verdict held. **No cell FAILS.** Tier 1 + Tier 2b + Tier 2d/Lived-oppression conditional STRONG-with-enhancement / WEAK-without (heavier failure-mode than Cost Severance Phase 2 due to housing-foreclosure trauma-affect vs HR-severance bureaucratic-affect). Tier 3a + 3b ADEQUATE due to inherent trauma-affect on jacket-marketing (structural property; not fixable by enhancement). Rename rejected (6 alternatives tested at Phase 2 depth: Resource-Foreclosure Bond; Future-Options Bond; Long-Horizon Bond; Intergenerational Resource Bond; Hartwick Bond; Sovereign Reserve Bond; Forward Accountability Bond).
- **Category:** vocabulary · framework-discipline · Ring-2 · cross-political-tradition robustness · trauma-affect handling
- **Content:** Three concrete enhancements ratified:
  1. **M12 lineage citation expansion** to terms_index Foreclosure Bond Rigor-provenance — Mian & Sufi 2014 *House of Debt* (already cited Ch 9:119 but not in Foreclosure Bond entry); Rothstein 2017 *The Color of Law*; Taylor 2019 *Race for Profit*; Coates 2014 "The Case for Reparations" *Atlantic*; Hyman 2011 *Debtor Nation*; Sugrue 1996 *The Origins of the Urban Crisis*; Desmond 2016 *Evicted*; cross-reference Cost Severance Phase 2 colonial-foreclosure lineage (Wolfe 1999; Coulthard 2014; Tuck & Yang 2012; Whyte); cross-reference Restitution Bond reparations-economics lineage (Darity & Mullen 2020 — already cited; symmetric application as forward-looking analog of backward-looking restitution); BLM 43 CFR Part 3162 + BSEE 30 CFR Part 250 + state oil-and-gas commission rules (Texas Railroad Commission Form W-1; Wyoming Oil and Gas Conservation Commission Rule Ch 3 §8; Oklahoma Corporation Commission rules; ~36 states); CERCLA / RCRA financial-assurance requirements; Environmental Impact Bonds (Balboa 2016 — already cited).
  2. **Ch 9 *Pricing Honestly* bridge prose at Foreclosure Bond first-introduction** — v1 DRAFT ratified per Phase 2 §7.3 (~250-350 words); lands in terms_index entry as scaffolding ratification; awaits author voice refinement during Ch 9 revision cycle. Bridges from Ch 9:119 housing-crisis material (already in chapter prose) to framework's Foreclosure Bond; engages racial disproportionality explicitly; positions framework as "the instrument we didn't have" + cluster-name for existing regulatory precedent.
  3. **Tech Appendix §L methodological footnote** on Foreclosure Bond housing-crisis-affect handling. v1 DRAFT in Phase 2 §8.2 (~250-300 words). **Placement choice (now vs Phase 3 Tech Appendix v2.0.0 rebuild) PENDING** per Phase 2 §12.5 open question; option for **unification with Cost Severance Phase 2 §L footnote into single cross-political-tradition methodological-framing section** PENDING per Phase 2 §12.4 open question.
- **Decisive criterion:** Rename rejected because no alternative dominates Foreclosure Bond + enhancements across all 12 audience cells under genuine pass/fail discipline (Working Principle #1 + author direction 2026-04-29 pass/fail-gate). The 2026-04-24 b1_b2_naming pass relied on three grounds: term-pair coherence with Foreclosure Cost (C₁ in RCV integrand); shorter form; M5 dinner-table strong via mortgage-foreclosure analogy. Phase 2 audit at 12-cell depth confirmed all three plus surfaced **affective-valence dimension** the older M-suite did not deeply audit: housing-foreclosure trauma-affect is heavier than HR-severance bureaucratic-affect; bridge prose at Ch 9 first-introduction converts collision-friction to motivating-exemplar (analogous to severance-bridge for Cost Severance). Significant Tier 2b adoption-travel finding: existing US regulatory precedent (decommissioning bonds + reclamation bonds + Environmental Impact Bonds + sovereign-wealth-fund Hartwick-rule operationalization) positions framework's Foreclosure Bond as principled extension of existing US regulatory practice that 36+ states + federal agencies recognize.
- **Implementation applied 2026-04-29:**
  1. terms_index Foreclosure Bond entry (B2 sub-instrument) — Phase 2 verdict entry added to M12 lineage section.
  2. terms_index Foreclosure Bond entry — cross-political-tradition lineage section added (3 categories: race+housing-economics + decolonial/colonial-foreclosure + reparations economics + US regulatory precedent).
  3. terms_index Foreclosure Bond entry — Ch 9 bridge prose v1 DRAFT inserted as scaffolding ratification; bridge prose status note explains pending author voice refinement.
  4. "Pairs with" entry expanded to include cross-reference to Restitution Bond B1 (forward-looking analog of backward-looking restitution; symmetric bond-as-forced-extractor-payment positioning).
- **Pending implementation:**
  - **Tech Appendix §L methodological footnote placement decision** (now in TechnicalAppendix_v1.0.0.html vs batched into Phase 3 v2.0.0 rebuild) — Phase 2 §12.5 open question; awaits author choice. **Same open question as Insight #35 Cost Severance Phase 2.**
  - **Tech Appendix §L unification question** — should Cost Severance Phase 2 §L footnote and Foreclosure Bond Phase 2 §L footnote be unified into single cross-political-tradition methodological-framing section that handles both terms? Phase 2 §12.4 open question.
  - **Ch 9 bridge prose insertion** — v1 DRAFT ratified; awaits author voice refinement during Ch 9 revision cycle. Bridge prose insertion deferred to Ch 9 revision cycle (analogous deferral to Cost Severance Ch 1 bridge per Insight #36).
- **Phase 2 verdict on bridge effectiveness:** "PLAN HOLDS conditionally pending execution + enhancement." Execution = Ch 9 bridge prose landed at appropriate placement during author revision cycle. Until then, Phase 2 verdict is provisional.
- **Verdict pattern observation:** Cost Severance + Foreclosure Bond Phase 2 both ratify same KEEP+three-enhancements verdict structure (lineage + bridge prose + Tech Appendix §L footnote). Suggests dominant pattern for vocabulary-collision-with-affective-weight items. May apply to Externality Tail (statistics-distribution-tail collision) — Phase 2 candidate #5.
- **Dependencies / Links:** Phase 1 full framework audit §6.14 (`commons_bonds_rigor_pass_2026-04-29_full_framework_audit_phase1_v1.0.0.md`); 2026-04-24 b1_b2 decomposition + b1_b2 naming rigor passes; Insight #35 Cost Severance Phase 2 (verdict-pattern cross-reference; shared lineage on colonial-foreclosure + reparations-economics; shared open question on Tech Appendix §L placement + unification); vocabulary strategy v1.0.1 §2 + §8 12-cell multi-audience matrix; Working Principle #1 (effort-to-repair-not-rigor); Working Principle #8 (publisher-facing scaffolding scrub); Insight #14 (Norway-as-canonical-B2 refinement; Foreclosure Bond is the cluster, Norway is the exemplar).

---

### Insight #39 — Pre-publication external review for academic-rigor pass/fail gate — OPEN

- **Raised:** 2026-04-29 by Phase 2 theorem-audit kickoff. Surfaced when Claude began Phase 2 deeper-dive on theorems E.1–E.5 (Phase 1 §10 candidate #3) per author direction 2026-04-29: *"the math formulas and proofs have to stand up to academic rigor or I don't have a book."*
- **Status:** **OPEN; pre-publication-state work; not blocking until manuscript reaches submission-ready state.**
- **Category:** academic-rigor · pass-fail-gate · external-review · pre-publication
- **Content:** The Phase 2 theorem audits (and the Phase 2 mathematical-formula audits — RCV integrand; scarcity multiplier; integral convergence) produce **Claude's assessment** of the proofs and formulas. Claude is not formally credentialed in economics or formal methods. For a pass/fail academic-rigor gate at top-tier journals (AER, QJE, JPE, JEEM, JPubE) and at academic-trade hybrid presses (Princeton, Yale, Harvard, MIT, U-Chicago), eventual external review by a credentialed third party is warranted before publication. Without it, the framework's published academic claims rest on Claude's review alone — which is a defensible-but-thin foundation for the book's pass/fail success criterion (severed cost migrating into legal/policy text + book taken seriously by economics + ethics + policy-economics communities).

- **Scope of external review proposed:**
  1. **Theorems E.1–E.5 (post-Phase 2 restructure)** — proof-structure verification by economics PhD or formal-methods expert. Prerequisites: Phase 2 theorem audits complete (Insights #40–#50 or similar; one per theorem per Phase 1 §10 #3).
  2. **Mathematical formulas** — RCV integrand notation; scarcity multiplier formula academic-defensibility; Hotelling Identity (already partially audited per Insight #30 §12.3 with three pre-publication safe-practice steps recommended). Prerequisites: Phase 2 mathematical-formula audits complete.
  3. **Bibliography accuracy + completeness** — separate todo item per author direction 2026-04-28; tied to Phase 3 Tech Appendix v2.0.0 rebuild. External review can verify lineage citations resolve correctly + framework's positioning vis-à-vis cited literature is fairly characterized.
  4. **Cross-political-tradition lineage citations** — Insight #35 Phase 2 + Insight #38 Phase 2 added substantial lineage (Coulthard; Tuck & Yang; Darity & Mullen; Anderson; Federici; Patel & Moore; Hickel; Mian & Sufi; Rothstein; Taylor; Coates; Hyman; Sugrue; Desmond). External review can verify the framework's positioning vis-à-vis these traditions is fair + non-extractive.

- **Reviewer profile candidates:** economics PhD with intergenerational-equity / resource-economics specialization (Brown Weiss tradition; Solow tradition; Stern Review tradition); formal-methods reviewer for theorem proofs; potentially a heterodox-economics reviewer for cross-political-tradition discipline; potentially a reparations-economics reviewer (Darity & Mullen tradition) for racial-justice + housing-economics positioning. Multi-reviewer approach likely warranted given the framework's cross-disciplinary scope.

- **Why this is OPEN now (raised but not yet executable):** the framework's academic-rigor restructure is in progress (Phase 2 theorem audits underway). External review is most useful AFTER the restructure produces academic-peer-review-ready proofs. Premature review (pre-restructure) would surface issues already known internally; post-restructure review tests whether the Phase 2 work succeeded.

- **Implementation pending (when triggered):**
  - Identify reviewer candidates (network search; Brown Weiss / Solow / Stern lineage academics; reparations-economics scholars).
  - Determine compensation / honorarium structure.
  - Determine review scope per reviewer (full theorem suite vs partial; full bibliography vs partial).
  - Set timeline relative to manuscript submission.

- **Why this is **not** blocking the Phase 2 work:** Phase 2 audits are valuable in themselves; they restructure the proofs to academic-rigor standards. External review tests the restructure but doesn't replace it. Phase 2 work proceeds; external review is a downstream gate.

- **Dependencies / Links:** Phase 2 theorem audits (Phase 1 §10 candidate #3; ~5 separate rigor passes per Insight #38 verdict pattern observation suggests not unique to vocabulary items); Phase 2 mathematical-formula audits (Phase 1 §10 candidates #4 + #7 + #8); bibliography accuracy + completeness audit (per author direction 2026-04-28; tied to Phase 3 Tech Appendix v2.0.0 rebuild); Hotelling Identity §12 (Insight #30) already-recommended pre-publication safe-practice steps (Google Scholar + JSTOR + Web of Science literature collision-check; bibliography Hotelling 1931 cross-check; Tech Appendix v2.0.0 rebuild attribution audit).

---

### Insight #40 — Phase 2 Theorem E.4 Integral Convergence academic-rigor depth audit — CLOSED-RATIFIED 2026-04-29

- **Raised:** 2026-04-29 by Phase 1 §8.3 (E.4 flagged for Phase 2 academic-rigor depth audit).
- **Status:** **closed-ratified 2026-04-29 (Chris Winn) — verdict (a) Full ratify all three enhancements** per `tools/rigor-passes/commons_bonds_rigor_pass_2026-04-29_phase2_theorem_e4_integral_convergence_v1.0.0.md`. First Phase 2 theorem audit; lightest of the 5 theorems per pre-audit assessment, executed first as proof-of-concept for the theorem-audit pattern. Tests applied (8): premise enumeration; logical derivation; edge case analysis; collision check against established convergence theorems (Lebesgue dominated convergence; monotone convergence; Weitzman 2001; Hartwick 1977; Solow 1974; Stern Review 2007); citation discipline; falsifiability; domain of applicability; counterexample resistance. **No structural defect in theorem's substance.** Repair work is formalization, not re-derivation.
- **Category:** academic-rigor · pass-fail-gate · theorem-audit · Phase 2
- **Content:** Three concrete restructure enhancements ratified:
  1. **Premise enumeration (Assumptions A1–A4 per rigor pass §13.1):** explicit numbered premises including polynomial-growth bounds on U (utility) + E (externality tail); substitutability monotonicity + admissible function class on S; Weitzman declining-rate framework on D (discount factor).
  2. **Restructured theorem statement (per rigor pass §13.2):** clean case decomposition (SC1: r_∞ > 0; SC2: sufficient substitutability convergence) + knife-edge divergence corollary promoted from footnote to theorem statement. Reformulates ambiguous theorem-statement-vs-case-analysis mapping in current text.
  3. **Restructured proof (per rigor pass §13.3):** explicit Lebesgue dominated convergence theorem invocation; Weitzman 2001 cited as load-bearing premise A4; standard real-analysis text cited (Royden 1988 / Folland 1999 / Rudin 1987 — citation choice pending §15 Q4).
- **Decisive criterion:** counterexamples constructed under current premises (rigor pass §12) that prove the theorem-as-currently-written is provably weak: (1) S(t) = 0.5 constant + r = 0 + U = 1 + E = 0 → RCV = ∞ but does not match the "knife-edge" footnote condition (which assumed U unbounded); actual divergence condition is "[1 − S_max] · U does not decay" not "U unbounded." (2) S(t) = 1 − 1/(1+t)² + r = 0 + U = (1+t)³ → RCV = ∫(1+t)dt = ∞; SC2 requires speed of S→1 to dominate U's growth, not just any convergence. The restructure handles both counterexamples explicitly via SC1/SC2 conditions.
- **Pass-fail verdict on as-currently-written E.4:** WEAK — would not survive academic peer review at top-tier journals (AER, QJE, JPE, JEEM, JPubE) without restructure.
- **Pass-fail verdict on restructured E.4 per rigor pass §13:** STRONG — meets academic-peer-review standards. Citations explicit; premises numbered; case decomposition clean; counterexample resistance verified; falsifiability condition explicit (knife-edge corollary).
- **Pattern observation (audit-pattern proof-of-concept):** E.4 audit produced 612-line rigor pass + ~140 lines analytical substrate. Audit pattern works. Per-test verdict structure surfaces specific gaps. Counterexample construction is genuinely productive (found 2 real gaps). Recommended restatement is concrete + ratifiable. **Scope projection for remaining theorems:** E.1 (framework's central theorem) ~800-1000 lines; E.3 (circular proof; full formalization needed) ~700-900 lines; E.5 (over-specified scope; scope-tightening + practical-corollary separation) ~700-900 lines; E.2 (categorization decision: relabel as empirical observation OR restructure as formal robustness theorem) ~400-600 lines depending on Option A vs B. Aggregate Phase 2 theorem audit scope estimate: ~3000-3800 lines across 5 rigor passes (slightly above original 2800-3700 estimate).
- **Implementation pending:**
  - **Tech Appendix v1.0.0 HTML §10 line 3279-3285 — restructured E.4 text per rigor pass §13.** Same open question as Insights #35 + #38 Tech Appendix §L footnotes: apply now vs batch into Phase 3 Tech Appendix v2.0.0 rebuild. Possibility of unified batch into v2.0.0 rebuild for all Phase 2 Tech Appendix changes.
  - **Bibliography expansion** — add Royden 1988 + Folland 1999 + Rudin 1987 (real analysis) per author choice on §15 Q4.
  - **Pre-publication external review** (per Insight #39) — real-analysis-trained economics PhD or formal-methods expert verifies the restructured E.4. Downstream gate; this Phase 2 audit produces the substrate.
- **Dependencies / Links:** Phase 1 full framework audit §8.3 (`commons_bonds_rigor_pass_2026-04-29_full_framework_audit_phase1_v1.0.0.md`); Insight #39 (pre-publication external review; downstream gate); Insights #35 + #38 (verdict-pattern cross-reference; shared open question on Tech Appendix HTML edit timing); Weitzman 2001 (load-bearing premise A4); Hartwick 1977 + Solow 1974 + Stern Review 2007 (adjacent literature; cleanly extended without conflict per rigor pass §8); standard real-analysis literature (Lebesgue dominated convergence; monotone convergence — invoked via Royden 1988 / Folland 1999 / Rudin 1987).

### Insight #41 — Phase 2 Theorem E.1 Structural Cost Severance academic-rigor depth audit — CLOSED-RATIFIED 2026-04-29

- **Raised:** 2026-04-29 by Phase 1 §8.1 (E.1 flagged for Phase 2 academic-rigor depth audit).
- **Status:** **closed-ratified 2026-04-29 (Chris Winn) — verdict (a) Full ratify: split into E.1a + E.1b; adopt premises P1–P3; tighten scope; add citations** per `tools/rigor-passes/commons_bonds_rigor_pass_2026-04-29_phase2_theorem_e1_structural_cost_severance_v1.0.0.md`. Second Phase 2 theorem audit; framework's central theorem. Tests applied (8); 6 of 8 verdicts WEAK on as-currently-written; 0 STRONG. Heaviest restructure of the 5 theorems because the substance has a categorization issue (algebraic identity conflated with empirical-structural claim), not just formalization gaps.
- **Category:** academic-rigor · pass-fail-gate · theorem-audit · Phase 2 · framework-central-theorem
- **Content:** Three concrete restructure enhancements ratified:
  1. **Split Theorem E.1 into E.1a + E.1b:**
     - **E.1a (Cost Severance Identity):** *CS > 0 iff B < RCV; CS = 0 iff B = RCV; CS < 0 iff B > RCV.* Trivially true by algebra (CS = RCV − B). Provides definitional sign rule + foundation for all framework reasoning about CS sign (e.g., E.5 Renewable Imperative uses E.1a's identity).
     - **E.1b (Structural Cost Severance under Current Institutions):** under explicit Premises P1–P3, aggregate B(R, t₀) < aggregate RCV(R, t₀) for non-renewable extraction under current institutions; therefore by E.1a, CS(R, t₀) > 0.
  2. **Replace wrong "B ≤ P" assumption with explicit Premises P1–P3:**
     - **P1 (Intergenerational market incompleteness — Coase 1960 extension):** Markets cannot complete bargaining for intergenerational claims; future generations cannot bid in present markets. Per Coase 1960 framework: complete-bargaining requires all affected parties to participate.
     - **P2 (Partial externality pricing — Pigou 1920 extension):** Existing externality-pricing instruments (Pigouvian taxes; cap-and-trade; reclamation bonds) cover specific externalities partially; comprehensive coverage not currently implemented in any jurisdiction. Per Pigou 1920 + Stern Review 2007.
     - **P3 (Current accountability bond inadequacy — empirical):** Across major non-renewable extraction jurisdictions in the contemporary decade, aggregate B is empirically less than aggregate RCV. Supporting evidence: Tech Appendix §H validation cases (McDowell County coal; Black Lung Trust Fund; EU ETS gaps; Norwegian sovereign-wealth-fund partial-coverage analysis).
  3. **Tighten universal scope to conditional scope + explicit falsifiability + domain of applicability:** "Aggregate RCV vs partial-coverage instruments" distinction made explicit in proof; non-renewable extraction defined via S(t) substitutability function; "current institutions" defined as accountability instruments in operation in current decade across jurisdictions where extraction occurs.
- **Decisive criterion:** the current proof's "B ≤ P" assumption is **wrong as a general claim**. Severance taxes (~36 US states), reclamation bonds (SMCRA), decommissioning bonds (BLM/BSEE), carbon taxes (EU ETS), and CSD per Insight #35 + #38 architecture are *forced regulatory impositions* — explicitly NOT market-bounded. Per Insights #35 + #38, the framework positions these instruments as forced-extractor-payment, not capital-instrument-deployment. The framework's whole argument depends on bonds being able to exceed market-bounded levels through regulation. The "B ≤ P" assumption contradicts the framework's own architecture. Replacement = explicit empirical Premise P3 (current bonds happen to be inadequate; framework proposes increasing them) supported by §H validation.
- **Counterexample finding (rigor pass §12):** "Norway-Norwegian-only" case finds real gap — current theorem doesn't specify aggregate-vs-jurisdictional RCV. Norway's sovereign-wealth-fund operationalizes Hartwick rule for Norwegian-citizen-internalization of oil rents; for Norwegian-citizen-only RCV, B may approximately equal RCV. Defense: framework's RCV is GLOBAL (includes climate externalities affecting non-Norwegian populations); Norway's B does NOT cover those. Restructure must specify aggregate-not-partial RCV.
- **Citation gap (rigor pass §8):** Coase 1960 NOT cited despite "intergenerational market incompleteness" IS the Coase-theorem-incomplete-bargaining condition; Pigou 1920 NOT cited despite externality framework load-bearing; intergenerational equity literature (Brown Weiss 1989; Howarth + Norgaard 1990) NOT cited. Restructure cites all three at premises P1, P2, P3 inline.
- **Pass-fail verdict on as-currently-written E.1:** WEAK (6 of 8 tests). Would not survive academic peer review at top-tier journals (AER, QJE, JPE, JEEM, JPubE) without restructure. Framework's most-central theorem currently has the most-fragile proof structure of the 5 theorems — heavier than E.4 (4 of 8 WEAK).
- **Pass-fail verdict on restructured E.1a + E.1b per rigor pass §13:** STRONG. Citations explicit; premises numbered; falsifiability conditions explicit; domain specified; counterexample resistance verified.
- **Pattern observation (audit-pattern after 2 theorem audits):** audits surface substantive finds, not formalization gaps. E.4 found 2 counterexamples + ambiguous statement-vs-case-analysis. E.1 found 1 wrong premise + 1 categorization conflation + 1 real counterexample + 3 missing citations to load-bearing literatures. Pattern suggests audit is doing real work, not box-checking. Scope projection holds (~2800-3800 lines aggregate across 5 rigor passes).
- **Implementation pending:**
  - **Tech Appendix v1.0.0 HTML §10 line 3249-3258 — restructured E.1a + E.1b per rigor pass §13.** Same open question as Insights #35 + #38 + #40: apply now vs batch into Phase 3 Tech Appendix v2.0.0 rebuild. Possibility of unified batch.
  - **Bibliography expansion** — Howarth + Norgaard 1990 (likely addition); possibly Solow 1974 explicit cite. Coase 1960 + Pigou 1920 + Brown Weiss 1989 + Stern Review 2007 + Hartwick 1977 already in framework bibliography.
  - **Cross-reference in other theorem proofs** — E.5 Renewable Imperative uses CS > 0 from E.1; restructured E.5 proof should cite E.1a (algebraic identity) explicitly.
  - **Pre-publication external review** (per Insight #39) — economics PhD with intergenerational-equity / resource-economics specialization (Brown Weiss / Solow / Stern lineage) verifies the Coase + Pigou + intergenerational-equity extensions are correctly characterized + counterexample resistance holds + aggregate-vs-partial-coverage distinction is fairly characterized. Downstream gate.
- **Dependencies / Links:** Phase 1 full framework audit §8.1 (`commons_bonds_rigor_pass_2026-04-29_full_framework_audit_phase1_v1.0.0.md`); Insight #40 (E.4 audit; established theorem-audit pattern); Insights #35 + #38 (Cost Severance + Foreclosure Bond verdict-pattern cross-reference; B as forced-extractor-payment positioning is central to E.1 restructure); Insight #39 (pre-publication external review; downstream gate); Coase 1960 "The Problem of Social Cost" (load-bearing for premise P1); Pigou 1920 *Economics of Welfare* (load-bearing for premise P2); Brown Weiss 1989 + Howarth + Norgaard 1990 + Stern Review 2007 (adjacent intergenerational-equity literature); Hartwick 1977 + Solow 1974 (sustainability rule baselines); Mazzucato + Anderson (institutional-structure adjacent positioning).

---

### Insight #42 — Phase 2 Theorem E.3 Abundance Masking academic-rigor depth audit — CLOSED-RATIFIED 2026-04-29

- **Raised:** 2026-04-29 by Phase 1 §8.2 (E.3 flagged for Phase 2 academic-rigor depth audit).
- **Status:** **closed-ratified 2026-04-29 (Chris Winn) — verdict (a) Full ratify: formal mathematical derivation + notation disambiguation (S → τ) + domain restriction + citation expansion** per `tools/rigor-passes/commons_bonds_rigor_pass_2026-04-29_phase2_theorem_e3_abundance_masking_v1.0.0.md`. Third Phase 2 theorem audit; circular-reasoning case. Tests applied (8); 7 of 8 verdicts WEAK on as-currently-written; 1 ADEQUATE; 0 STRONG. **Expanded post-ratification 2026-04-29 to 4 enhancements (was 3) per parallel-session findings integration** — adds CIT-as-operational-corollary reframing (parallel-session distinctive structural finding) + resource-economics + tipping-point lineage citations (Pindyck 1978; Dasgupta-Heal 1979; Barnosky et al. 2012 *Nature*; Lenton et al. 2008 *PNAS*) complementary to this audit's commodity-economics + supply-elasticity lineage. Parallel-session rigor pass `tools/rigor-passes/commons_bonds_rigor_pass_2026-04-29_phase2_theorem_e3_circular_proof_v1.0.0.md` retained as SUPPLEMENTARY to this canonical record; both audits independently arrived at most of the same load-bearing findings. See §17 of canonical rigor pass for parallel-session findings integration detail.
- **Category:** academic-rigor · pass-fail-gate · theorem-audit · Phase 2 · notation-discipline
- **Content:** Four concrete restructure enhancements ratified (3 original + 1 added post-ratification per parallel-session integration):
  1. **Replace circular CIT-construction reasoning with formal mathematical derivation** via supply-elasticity argument + explicit hyperbolic functional form near scarcity threshold: c(A) = c₀ · (τ/(A−τ))^α with α ≥ 1. Limit analysis: lim_{A → ∞} c(A) = 0 (abundance masks cost); lim_{A → τ⁺} c(A) = ∞ (cost diverges as abundance approaches scarcity). Lineage spans BOTH commodity-economics + supply-elasticity (Marshall 1890; Hamilton 2009 *Brookings*; Kilian 2009 *AER*) AND resource-economics + tipping-point (Pindyck 1978 *JPE*; Dasgupta-Heal 1979; Barnosky et al. 2012 *Nature*; Lenton et al. 2008 *PNAS*); both lineages support the same conclusions from complementary angles (price-discovery ⊕ biophysical-state-shift).
  2. **Disambiguate notation:** rename E.3's "scarcity threshold" to **τ (tau)**. Reserve `S` and `S(t)` exclusively for substitutability function (per Insight #40 E.4 audit + framework's RCV integrand discipline). Apply consistently across Tech Appendix including CIT Definition A.8 reframing.
  3. **Add domain restrictions:** non-renewable depletable commons under stock-flow framework with standard supply-elasticity. Explicit exclusions: (a) constant-marginal-cost regimes (elastic-supply manufactured goods); (b) renewable commons (regeneration ≥ extraction; A self-restores); (c) information / non-rivalrous commons (use does not deplete stock); (d) network-effect commons (cost dynamics depend on coordination effects; ∂U/∂A > 0 inverts scarcity-utility relationship).
  4. **CIT-as-operational-corollary reframing** (parallel-session distinctive finding integrated post-ratification): Tech Appendix Definition A.8 (CIT) gets explicit forward-pointer establishing E.3 as analytic theorem and CIT as operational protocol that detects the phenomenon; Tech Appendix §10 E.3 statement gets backward-pointer noting CIT's validity follows from E.3. Eliminates the structural circularity at the *logical-organization* level (not just the *proof-content* level addressed by Enhancement 1). Strengthens framework's logical organization: theorem → operational corollary, not circular.
- **Decisive finding (NEW Phase 2 — distinctive from parallel-session audit):** **NOTATION COLLISION** between three distinct concepts using letter S:
  - E.3 `S`: scarcity threshold (a numeric value of abundance)
  - E.4 `S(t)` + framework RCV integrand: substitutability function (a probability function in [0, 1])
  - Insight #33 `S_max`: limit of substitutability function (existential substitutability gap)
  
  Same letter; three concepts; serious M12 attribution-honesty + readability issue. Only visible when looking ACROSS theorems (E.3 S vs E.4 S(t) vs framework integrand S vs Insight #33 S_max); single-theorem audit would not surface this. **NEW Phase 2 finding** not in Phase 1 §6.11 (which addressed Externality Tail's `-Tail` suffix) or §8.2 (which flagged Hotelling rent dynamics + commodity price spike empirical citations as Phase 2 scope).
- **Other findings (overlap likely with parallel session E.3 audit):**
  - Circular reasoning: "By construction of the Commons Inversion Test" — CIT is methodology for identifying admissible costs, NOT source of abundance-masking phenomenon.
  - Missing formal mathematical derivation: "linear to exponential transition" hand-waved without functional form.
  - Hotelling 1931 cited but not directly applicable as written; adjacent + supportive (extraction-price-over-time) but not directly proving E.3 (cost-as-function-of-abundance).
  - Empirical citation gap: Hamilton 2009 *Brookings Papers*; Kilian 2009 *AER*; Pindyck 2008 *Energy Journal* commodity-price-spike literature not cited.
  - Domain over-broad: 4 counterexamples constructed (renewable commons; information commons; network-effect commons; constant-cost commons); all real; all falsify universal claim. Repair = explicit domain restrictions per Premise A4.
- **Pass-fail verdict on as-currently-written E.3:** WEAK (7 of 8 tests). Would not survive academic peer review at top-tier journals.
- **Pass-fail verdict on restructured E.3 per rigor pass §13:** STRONG. Formal derivation with explicit hyperbolic functional form; notation disambiguated; domain restricted to non-renewable depletable commons; load-bearing citations explicit.
- **Pattern observation after 3 theorem audits:** audits surface substantive finds at Phase 2 depth that screening-level Phase 1 missed. E.4 found 2 counterexamples + ambiguous mapping; E.1 found 1 wrong premise + 1 categorization conflation + 1 real counterexample + 3 missing citations; E.3 found notation collision + circular reasoning + 4 domain-restriction counterexamples + 3 missing citations. Pattern doing real work.
- **Implementation pending:**
  - **Tech Appendix v1.0.0 HTML §10 line 3270-3276 — restructured E.3 per rigor pass §13 + §17 integrated content.** BATCHED into Phase 3 Tech Appendix v2.0.0 rebuild per shared open question with Insights #35 + #38 + #40 + #41 + #47 + #48 + #49 + #50 + #51 + #52 + #53.
  - **Tech Appendix-wide notation sweep — S → τ for scarcity-threshold instances.** Includes CIT Definition A.8 + adjacent text. May surface additional collision instances.
  - **Tech Appendix Definition A.8 (CIT) update** — add forward-pointer per rigor pass §17.2 establishing CIT-as-operational-corollary relationship to E.3.
  - **Tech Appendix §10 E.3 statement update** — add backward-pointer per rigor pass §17.2 + restructured proof per §13.3 + §17.3 (cite both lineages: commodity-economics + supply-elasticity AND resource-economics + tipping-point).
  - **Bibliography expansion (combined per §17.5)** — Pindyck 1978 *JPE* "The Optimal Exploration and Production of Nonrenewable Resources"; Dasgupta-Heal 1979 *Economic Theory and Exhaustible Resources*; Barnosky et al. 2012 *Nature* "Approaching a state shift in Earth's biosphere"; Lenton et al. 2008 *PNAS* "Tipping elements in the Earth's climate system"; Hamilton 2009 *Brookings*; Kilian 2009 *AER*; Marshall 1890 *Principles of Economics*; Pindyck 2008 *Energy Journal*; modern microeconomics text (Mankiw or Friedman *Price Theory* for supply-elasticity foundation). Pindyck 1978 + Dasgupta-Heal 1979 overlap with Insights #47 + #53 (P2#3.4 [E.2]) — combined bibliography absorbs once during Phase 3 rebuild.
  - **terms_index CIT entry update** — clarify per rigor pass §17.2 that CIT = operational protocol detecting E.3's analytic claim; CIT's validity follows from E.3 (resolves circular reasoning at terminology level).
  - **Pre-publication external review** (per Insight #39) — multi-reviewer (resource-economics + commodity-economics + ecological-economics + formal-methods) consistent with the cross-disciplinary lineage now invoked. Downstream gate.
- **Parallel-session integration (post-ratification 2026-04-29):** User ran parallel sessions on rest of Phase 2 list (E.5, E.2, items 4-8) while this session worked on E.1 + E.3. Both sessions independently produced E.3 audits arriving at most of the same load-bearing findings (circular proof; functional-form derivation; notation collision; counterexample classes). Reconciliation per author direction: this session's audit retained as canonical (Insight #42); parallel-session rigor pass retained as SUPPLEMENTARY with its distinctive contribution (CIT-as-operational-corollary reframing) integrated into this canonical record per §17. Original PROPOSED Insight #54 (parallel-session E.3) retired in favor of canonical #42.
- **Dependencies / Links:** Phase 1 full framework audit §8.2 (`commons_bonds_rigor_pass_2026-04-29_full_framework_audit_phase1_v1.0.0.md`); Insight #40 (E.4 audit; established S(t) substitutability-function notation discipline; cross-reference for notation-collision finding); Insight #41 (E.1 audit; verdict-pattern cross-reference); Insight #33 (existential substitutability gap rename; established S_max notation); Insight #39 (pre-publication external review; downstream gate); P2#3.2 [E.3] supplementary rigor pass `tools/rigor-passes/commons_bonds_rigor_pass_2026-04-29_phase2_theorem_e3_circular_proof_v1.0.0.md` (parallel-session audit; CIT-as-operational-corollary distinctive contribution integrated per §17); Insights #47 + #53 (Pindyck 1978 + Dasgupta-Heal 1979 bibliography overlap; combined absorbed once in Phase 3 rebuild); Hotelling 1931 (adjacent rent-dynamics framework; already in framework bibliography); Pindyck 1978 *JPE* + Dasgupta-Heal 1979 (resource-economics primitives for premise derivation); Barnosky et al. 2012 *Nature* + Lenton et al. 2008 *PNAS* (ecological tipping-point lineage); Hamilton 2009 + Kilian 2009 + Pindyck 2008 (empirical commodity-price-spike literature); Marshall 1890 + modern microeconomics (supply-elasticity foundation).

### Insight #47 — Phase 2 #7 Scarcity multiplier formula academic-defensibility audit — CLOSED-RATIFIED 2026-04-29

- **Raised:** 2026-04-29 by Phase 1 §7.10 (scarcity_multiplier formula flagged for Phase 2 academic-defensibility audit).
- **Status:** **closed-ratified 2026-04-29 (Chris Winn) — verdict (a) Full ratify all three enhancements + one structural correction** per `tools/rigor-passes/commons_bonds_rigor_pass_2026-04-29_phase2_scarcity_multiplier_academic_defensibility_v1.0.0.md`. First reverse-priority Phase 2 sweep audit ratified (sibling session #1: Q(t) notation P2#8 PROPOSED; this session #2: scarcity multiplier P2#7 RATIFIED).
- **Category:** academic-rigor · pass-fail-gate · functional-form-defensibility · Phase 2
- **Content:** Three concrete enhancements + one structural correction ratified:
  1. **Functional-form motivation note (per rigor pass §13.1):** add to Tech Appendix §10 + Method 3 sensitivity analysis §2.1; cites Hotelling 1931 (rent-path conjugate); Atkinson 1970 + Cobb-Douglas 1928 (welfare-economics log-utility precedent); bounded concavity argument; numerical tractability argument; sensitivity-robustness forward-pointer to Block 4 numerical Monte Carlo.
  2. **Discipline-claim correction (per rigor pass §13.2) — load-bearing structural fix:** replace inaccurate "bounded above by Hotelling-rent ceiling; should NOT diverge to infinity" language with accurate "slow-growing logarithmically; practically bounded across documented σ range; structurally unbounded as σ → ∞; alternative asymptotic-bounded forms admissible under sensitivity-robustness scoping." Eliminates the framework's structural mismatch between asserted property and actual formula behavior.
  3. **Alternative-functional-form sensitivity table (per rigor pass §13.3):** add Method 3 sensitivity analysis §2.1.5 comparing log(1+σ) [current] vs σ^0.3 [power] vs σ/(1+σ) [asymptotic-bounded] vs arctan(σ) [bounded] across σ ∈ [0, 10⁴] at H_a = 0.05; demonstrates α-dominance regime preserved across admissible concave forms.
  4. **Bibliography expansion (per rigor pass §13.4):** Atkinson 1970 *J Econ Theory*; Cobb & Douglas 1928 *AER*; Solow 1956 *QJE*; Bergson 1938 *QJE*. (Hotelling 1931 already in bibliography; Dixit-Pindyck 1994 already in bibliography.)
- **Decisive criterion:** Audit identified a structural inconsistency between the discipline claim ("bounded above by Hotelling-rent ceiling") and the formula's actual behavior (log(1+σ) is unbounded as σ → ∞). Top-tier journal review would flag this on first read. Repair is presentational + corrective, not re-derivational. The form is connectable to Hotelling rent-path (exponential price growth → log linearizes) and welfare-economics log-utility lineage (Atkinson 1970; Cobb-Douglas 1928); enhancements add the missing motivation + citation discipline. Cross-case α-dominance regime preserved across all admissible concave forms — the framework's load-bearing claim survives functional-form sensitivity.
- **Pass-fail verdict on as-currently-written scarcity_multiplier formula:** WEAK — would not survive academic peer review at top-tier journals (AER, QJE, JPE, JEEM, JPubE, *Resource and Energy Economics*, *J Environ Econ Manage*) without enhancement.
- **Pass-fail verdict on enhanced scarcity_multiplier per rigor pass §13:** STRONG — meets academic-peer-review standards. Functional choice motivated; discipline claim corrected; alternative-form sensitivity displayed; citations explicit.
- **Implementation pending:**
  - **Tech Appendix v1.0.0 HTML §10 line 866 — add §13.1 functional-form motivation note + §13.3 alternative-functional-form sensitivity table.** Same open question as Insights #35 + #38 + #40 + Phase 2 #8 + Phase 2 #6 Tech Appendix HTML edit timing: apply now vs batch into Phase 3 Tech Appendix v2.0.0 rebuild. Possibility of unified batch into v2.0.0 rebuild for all Phase 2 Tech Appendix changes.
  - **`core/technical-appendix/method3_sensitivity_analysis_2026-04-25.md` §2.1 — discipline-claim correction per §13.2.**
  - **`core/technical-appendix/method3_sensitivity_analysis_2026-04-25.md` §2.1.5 (new) — alternative-form sensitivity table per §13.3.**
  - **Bibliography expansion** — Atkinson 1970; Cobb-Douglas 1928; Solow 1956; Bergson 1938.
  - **Pre-publication external review** (per Insight #39) — resource-economist + welfare-economics PhD verifies Hotelling-rent-path-conjugate motivation + alternative-form sensitivity coverage + Block 4 numerical Monte Carlo scoping. Downstream gate; this Phase 2 audit produces the substrate.
- **Dependencies / Links:** Phase 1 full framework audit §7.10 + §10 #6; Method 3 sensitivity analysis 2026-04-25 §2.1 + §3.4 + §6.4; Insight #39 (pre-publication external review; downstream gate); Insights #35 + #38 + #40 + Phase 2 #8 [Q(t)] + Phase 2 #6 [TWoC-adoption] (verdict-pattern cross-reference; shared open question on Tech Appendix HTML edit timing); Hotelling 1931 (rent-path conjugate motivation); Atkinson 1970 + Cobb-Douglas 1928 (welfare-economics log-utility precedent); Dixit-Pindyck 1994 (option-value foundation, already in bibliography).

### Insight #48 — Phase 2 #6 Three Ways of Counting post-rename adoption-fit verification — CLOSED-RATIFIED 2026-04-29

- **Raised:** 2026-04-29 by Phase 1 §10 #5 (TWoC post-rename adoption-fit verification flagged for Phase 2; "minor; can defer until pre-submission review").
- **Status:** **closed-ratified 2026-04-29 (Chris Winn) — verdict (a) Full ratify (Option A clean drop)** per `tools/rigor-passes/commons_bonds_rigor_pass_2026-04-29_phase2_three_ways_of_counting_adoption_fit_v1.0.0.md`. Surface-by-surface adoption check across 10 surfaces; 9 of 10 cleanly adopt TWoC; one minor adoption-fix at Tech Appendix §3 section title (TOC line 225 + section header line 678).
- **Category:** vocabulary-discipline · post-rename adoption-verification · Phase 2 (minor)
- **Content:** One concrete adoption-fix ratified:
  1. **Tech Appendix v1.0.0 §3 section-title inversion fix at lines 225 (TOC) + 678 (section header H2).** Replace *"§3. RCV Quantification — Triangulated Estimation (Three Ways of Counting)"* with *"§3. RCV Quantification — Three Ways of Counting"* (Option A clean drop, recommended; aligns directly with Insight #31 Option B verdict — drop "Triangulated RCV Estimation" as primary, promote TWoC to primary methodology name).
- **Decisive criterion:** Audit confirmed Phase 1's "minor" classification — single 2-line HTML edit; no chapter-prose regressions; no terms_index inconsistencies; no glossary mismatches. The 9 cleanly-adopted surfaces include: Ch 6 chapter title (was always TWoC); Ch 6 chapter prose (uses "Triangulation" as concept-noun + "the triangulated three-method range" as preserved-form per Option B); Ch 6 GuidanceDoc; terms_index entry (with exemplary supersession-record discipline); glossary v3 entry; Tech Appendix Block 4 sections + body; Block 4 validation document; bibliography references (legitimate-historical provenance traces); older rigor passes (legitimate-historical internal references). The single ADOPTION GAP at Tech Appendix §3 section title is a stale-formatting artifact from a prior consolidation pass that never got the post-rename inversion fix.
- **Pass-fail verdict on as-currently-written TWoC adoption state:** ADEQUATE — 9 of 10 surfaces clean; one section-title gap at high-leverage TOC + section header surface.
- **Pass-fail verdict on enhanced TWoC adoption state per rigor pass §5.1:** STRONG — all 10 surfaces present TWoC as primary methodology name; legitimate-historical references in bibliography + older rigor passes correctly preserved as provenance traces.
- **Implementation pending:**
  - **Tech Appendix v1.0.0 HTML lines 225 + 678 — section-title fix per rigor pass §5.1 (single 2-line edit).** Same open question as Insights #35 + #38 + #40 + #47 Tech Appendix HTML edit timing: apply now vs batch into Phase 3 Tech Appendix v2.0.0 rebuild. Possibility of unified batch into v2.0.0 rebuild for all Phase 2 Tech Appendix changes.
  - **Pre-publication external review** (per Insight #39) — TWoC adoption-fit is comparatively low-stakes; external review will more naturally focus on heavier audits.
- **Dependencies / Links:** Phase 1 full framework audit §10 #5; Insight #31 (Triangulated RCV Estimation → Three Ways of Counting rename, RATIFIED 2026-04-28; Option B verdict that this audit verifies adoption against); Insight #39 (pre-publication external review; downstream gate); Insights #35 + #38 + #40 + #47 (verdict-pattern cross-reference; shared open question on Tech Appendix HTML edit timing).

### Insight #49 — Phase 2 #5 Externality Tail statistics-distribution-tail collision audit — CLOSED-RATIFIED 2026-04-29

- **Raised:** 2026-04-29 by Phase 1 §6.11 + §10 #3 (Externality Tail flagged for Phase 2 deeper-dive on statistics-tail collision; suffix-coherence bundling already-closed at Phase 1 §9.4).
- **Status:** **closed-ratified 2026-04-29 (Chris Winn) — verdict (a) Full ratify both enhancements** per `tools/rigor-passes/commons_bonds_rigor_pass_2026-04-29_phase2_externality_tail_statistics_collision_v1.0.0.md`. Reverse-priority Phase 2 sweep audit #4 ratified.
- **Category:** academic-rigor · pass-fail-gate · vocabulary-collision · Phase 2
- **Content:** Two concrete disambiguation enhancements ratified:
  1. **Disambiguation note at three load-bearing locations (per rigor pass §13.1):** terms_index Externality Tail entry (~120 words "Notational disambiguation" subsection); Tech Appendix v1.0.0 §B Definition A.4 (line 455) extended parenthetical clarifying "long tail in time" temporal sense vs statistics-distribution-tail; glossary v3 entry appended disambiguating sentence. Closes Tier 2a-finance/IO + Tier 2e (working-quant) collision-exposure gap by explicitly distinguishing temporal-persistence sense from statistics-distribution-tail conventions (Mandelbrot fat-tail; Taleb Black Swan; Embrechts et al. extreme-value-theory; Anderson long-tail).
  2. **Bibliography expansion (per rigor pass §13.2):** Mandelbrot 1963 *J Business* (fat-tailed price distributions); Taleb 2007 *The Black Swan*; Embrechts, Klüppelberg & Mikosch 1997 *Modelling Extremal Events*; Anderson 2006 *The Long Tail*. Anchors the disambiguation note for academic-recognition; not load-bearing on framework's substantive claims.
- **Decisive criterion:** Tier 2a-finance/IO + Tier 2e working-quant readers face high misread risk on first encounter of "Externality Tail" — pattern-match to extreme-value-theory / heavy-tail / Black Swan / tail-VaR vocabulary. Without explicit disambiguation, "Externality Tail" reads as "extreme-value externality cost" or "stochastic-tail externality" (framework-divergent readings; E(R, t) is deterministic, not probability distribution). Internal coherence (Definition A.4 "flow at time t" + 4-axis Pigouvian distinctness + temporal-persistence rhetorical anchor "runs on its own clock") forces correct reading after careful reading, but academic-publication discipline expects disambiguation at first encounter. Repair work is disambiguation-discipline + citation, not rename or re-derivation.
- **Rename considered + rejected:** Six alternatives tested (Persistent Externality / Externality Persistence / Post-Extraction Externality / Lingering Externality / Externality Aftermath / Temporal Externality); all rejected on rename-cost grounds (29+ publisher-facing instances + 4 prior rigor passes + chapter prose retraining + case-study sweep) and metaphor-loss grounds (the temporal-tail metaphor is genuinely useful; the "runs on its own clock" rhetorical anchor depends on it).
- **Suffix-coherence bundling closed-confirmed:** Per Phase 1 §9.4 prior disposition, "-Tail" one-off suffix is acceptable; no additional concerns surfaced at Phase 2 depth.
- **Pass-fail verdict on as-currently-written Externality Tail terminology:** ADEQUATE-WEAK — survives sympathetic-referee review on internal-coherence grounds but flagged on first-encounter misread risk for finance / IO / quant readers.
- **Pass-fail verdict on enhanced Externality Tail per rigor pass §13:** STRONG — multi-audience misread risk closed for highest-exposure tiers.
- **Implementation pending:**
  - **`core/terms/terms_index.md` Externality Tail entry — insert §13.1 (a) Notational disambiguation subsection (~120 words).**
  - **Tech Appendix v1.0.0 HTML §B Definition A.4 (line 455) — replace with §13.1 (b) extended text.**
  - **`core/glossary/commons_bonds_updated_glossary_v3.html` Externality Tail entry — append §13.1 (c) disambiguating sentence.**
  - **Bibliography expansion** — Mandelbrot 1963; Taleb 2007; Embrechts et al. 1997; Anderson 2006.
  - Same open question as Insights #35 + #38 + #40 + #47 + #48 + Phase 2 #8 Tech Appendix HTML edit timing: apply now to v1.0.0 vs batch into Phase 3 v2.0.0 rebuild.
  - **Pre-publication external review** (per Insight #39) — multi-disciplinary review (welfare economist + finance/risk practitioner or actuary).
- **Dependencies / Links:** Phase 1 full framework audit §6.11 + §9.4 + §10 #3; Externality Tail individual rigor pass 2026-04-24 (RATIFIED Ring-2 promotion under current naming; 4-axis Pigouvian distinctness preserved); Phase 2 Theorem E.4 RATIFIED Insight #40 (E in restructured premises A2 polynomial-growth bound; this audit's enhancements are non-disruptive to E.4 proof structure); Insight #39 (pre-publication external review; downstream gate); Insights #35 + #38 + #40 + #47 + #48 (verdict-pattern cross-reference; shared open question on Tech Appendix HTML edit timing); Pigou 1920 + Nordhaus & Boyer 2000 + Stern 2007 (already in bibliography per Externality Tail M12 lineage); Mandelbrot 1963 + Taleb 2007 + Embrechts et al. 1997 + Anderson 2006 (new bibliography additions for disambiguation anchor).

### Insight #50 — Phase 2 #4 RCV acronym collision audit — CLOSED-RATIFIED 2026-04-29

- **Raised:** 2026-04-29 by Phase 1 §5.5 + §10 #2 (RCV acronym flagged for Phase 2 collision audit).
- **Status:** **closed-ratified 2026-04-29 (Chris Winn) — verdict (a) Full ratify all three disambiguation enhancements** per `tools/rigor-passes/commons_bonds_rigor_pass_2026-04-29_phase2_rcv_acronym_collision_v1.0.0.md`, with §15 Q5 Ranked-Choice Voting reorder applied. Final audit in the session's reverse-priority Phase 2 sweep (P2#8 → P2#7 → P2#6 → P2#5 → P2#4); 4 of 5 ratified at session-end (P2#8 [Q(t)] remains [PROPOSED]).
- **Category:** academic-rigor · pass-fail-gate · vocabulary-collision · acronym-disambiguation · Phase 2
- **Content:** Three concrete disambiguation enhancements ratified:
  1. **Disambiguation note at three load-bearing locations (per rigor pass §13.1):** terms_index Residual Commons Value entry (~110-word "Notational disambiguation" subsection); Tech Appendix v1.0.0 §B Definition A.6 (line 467) parenthetical clarification; glossary v3 entry appended disambiguating sentence. Closes Tier 2c (policy-practitioner with civic-engagement / insurance-regulation overlap) + Tier 1 (lay with property-insurance experience) + Tier 2e (finance-quant with banking-regulatory) collision exposure. **Per §15 Q5 ratification:** RCV-as-Ranked-Choice-Voting reordered to **first** in disambiguation note given rising-salience trajectory through 2024+ (Maine 2018 / NYC 2021 / Alaska 2022 / multiple state initiatives 2024 — by framework's planned publication window, RCV-as-Ranked-Choice-Voting may overtake insurance Replacement Cost Value as primary collision risk).
  2. **First-introduction discipline codification (per rigor pass §13.2):** canonical practice "always introduce as 'Residual Commons Value (RCV)' on first appearance per chapter or major section before reusing acronym" added to terms_index RCV entry. Discipline already partially established (per 2026-04-24 individual rigor pass §17 census: 71 full-form + 658 acronym uses across 34 files = ~10% full-form ratio); codification ensures consistent application across future Phase 3 Tech Appendix v2.0.0 rebuild + Phase 4 Glossary v4 rebuild + chapter pre-submission sweeps.
  3. **Bibliography expansion (per rigor pass §13.3):** Reilly 2001 *Democracy and Diversity: Political Engineering in the Asia-Pacific* (Oxford UP) [academic anchor for ranked-choice voting]; Insurance Information Institute online resource on Replacement Cost vs Actual Cash Value (or Casualty Actuarial Society textbook alternative); Basel Committee on Banking Supervision 2017 *Basel III: Finalising Post-Crisis Reforms* (BIS).
- **Decisive criterion:** Three load-bearing real-world RCV-acronym collisions identified through real-world census: (1) **Insurance "Replacement Cost Value" — HIGH risk** for property-insurance-experienced lay readers + insurance-policy practitioners (vernacular in every U.S. homeowner / renter / auto policy); (2) **Voting "Ranked-Choice Voting" — MEDIUM-HIGH and rising salience** through 2024+ (Maine 2018 / NYC 2021 / Alaska 2022 / multiple state initiatives); (3) **Finance "Risk Capital Value" — MEDIUM risk** via Basel III + FDIC banking-regulatory. Internal mathematical apparatus (RCV integral form per Tech Appendix §B Definition A.6) forces correct reading via canonical-definition encounter — none of the real-world RCV-collisions can fit the integrand-and-integral form. Disambiguation closes pre-equation reading-friction without relying on equation-encounter for resolution. Rename foreclosed by 2026-04-24 individual RCV rigor pass §17 Option A unconditional PASS (~730 uses across 34 files; CS = RCV − B equation; 5 rename alternatives all rejected on precision/adoption/equation-integration grounds).
- **Pass-fail verdict on as-currently-written RCV terminology:** ADEQUATE-WEAK — survives sympathetic-referee review on internal-coherence grounds but flagged on first-encounter misread risk for high-collision tiers.
- **Pass-fail verdict on enhanced RCV terminology per rigor pass §13:** STRONG — multi-audience misread risk closed for highest-exposure tiers; first-introduction discipline codified; bibliography anchors disambiguation against established acronym-usages.
- **Implementation pending:**
  - **`core/terms/terms_index.md` Residual Commons Value entry — insert §13.1 (a) Notational disambiguation subsection (Ranked-Choice Voting first per §15 Q5) + §13.2 First-introduction discipline subsection.**
  - **Tech Appendix v1.0.0 HTML §B Definition A.6 (line 467) — add §13.1 (b) parenthetical note (Ranked-Choice Voting reorder applied).**
  - **`core/glossary/commons_bonds_updated_glossary_v3.html` Residual Commons Value entry — append §13.1 (c) disambiguating sentence (Ranked-Choice Voting reorder applied).**
  - **Bibliography expansion** — Reilly 2001; Insurance Information Institute; Basel Committee 2017.
  - Same open question as Insights #35 + #38 + #40 + #47 + #48 + #49 + Phase 2 #8 Tech Appendix HTML edit timing: apply now to v1.0.0 vs batch into Phase 3 v2.0.0 rebuild. **Recommended:** unified batch into v2.0.0 rebuild for all Phase 2 Tech Appendix changes.
  - **Pre-publication external review** (per Insight #39) — multi-perspective review (insurance-regulation + civic-engagement / electoral-policy + banking-finance practitioners).
- **Dependencies / Links:** Phase 1 full framework audit §5.5 + §10 #2; RCV individual rigor pass 2026-04-24 (RATIFIED Ring-1 promotion under current naming; Option A unconditional PASS; rename foreclosed); Phase 2 Theorem E.4 RATIFIED Insight #40 (RCV integral form preserved in restructured E.4; this audit's enhancements are non-disruptive to E.4 proof structure); Insight #39 (pre-publication external review; downstream gate); Insights #35 + #38 + #40 + #47 + #48 + #49 (verdict-pattern cross-reference; shared open question on Tech Appendix HTML edit timing); Insurance Information Institute / Casualty Actuarial Society (insurance Replacement Cost Value lineage); Basel Committee 2017 (banking-regulatory Risk Capital Value lineage); Reilly 2001 (academic ranked-choice voting lineage).
- **Phase 2 reverse-priority sweep aggregate observation:** This audit completes the session's reverse-priority Phase 2 sweep (P2#8 → P2#7 → P2#6 → P2#5 → P2#4). Cross-audit pattern: each audit identifies real collision-risk concerns + recommends disambiguation discipline within existing terminology; all 5 audits validate substantive vocabulary correctness (PASS-conditional verdicts) without rename. Aggregate enhancement scope: ~600 words across all five audits + ~14 new bibliography entries + multiple section-level disambiguation notes. Implementation timing: batch into Phase 3 Tech Appendix v2.0.0 rebuild as coordinated framework-rigor-discipline upgrade.

### Insight #51 — Phase 2 #3.4 Theorem E.2 Convergence of Independent Models categorization audit — CLOSED-RATIFIED 2026-04-29

- **Raised:** 2026-04-29 by E.4 rigor pass §16.3 (E.2 categorization-decision flag: relabel as empirical observation OR restructure as formal robustness theorem).
- **Status:** **closed-ratified 2026-04-29 (Chris Winn) — verdict (a) Full ratify Option A** per `tools/rigor-passes/commons_bonds_rigor_pass_2026-04-29_phase2_theorem_e2_categorization_v1.0.0.md`. Out-of-sequence theorem audit (sibling session running E.1 in parallel; E.2 picked as available work given lighter scope; ratified before E.1).
- **Category:** academic-rigor · pass-fail-gate · theorem-categorization · Phase 2
- **Content:** Three concrete repair enhancements ratified under Option A (relabel as empirical observation):
  1. **Relabel + replacement text per rigor pass §14.1:** "Theorem E.2 (Convergence of Independent Models)" → **"Empirical Observation E.2 (Cross-Model Convergence)"** with reformulated supporting argument + failure-mode acknowledgment + domain-of-applicability statement.
  2. **Case-count consistency fix per §1.3 Enhancement 2:** resolve internal contradiction "six tested cases" vs "all four empirical cases" → **4 empirical** (McDowell coal; Norway oil; Deepwater Horizon; Libby vermiculite) + **2 thought-experiment** (asteroid mining; lunar regolith from Ch 7) = **6 total tested cases**.
  3. **Citation discipline upgrade per §1.3 Enhancement 3:** add **Hong & Page 2004 *PNAS*** "Groups of diverse problem solvers can outperform groups of high-ability problem solvers" as load-bearing reference for diversity-of-models convergence reasoning. (Optional secondary: Mosteller & Tukey 1977 *Data Analysis and Regression* for multiple-estimator convergence framing.)
  
  Plus cross-reference cleanup per §14.2: replace "Theorem E.2" / "Convergence Theorem (E.2)" with "Empirical Observation E.2 (Cross-Model Convergence)" / "E.2 (Cross-Model Convergence)" in chapter prose + case study references (§11 line 3234 + §D Section VIII line 3048 + ad-hoc cross-references).
- **Decisive criterion:** The current E.2 proof is **empirical-evidence reasoning + probabilistic-implausibility argument**, not derivation from premises. Academic peer review reads this as categorization mismatch between claim form (statistical regularity across N cases) and proof form (case-evidence reasoning). Plus internal text contradiction ("six tested cases" + "all four empirical cases" in same paragraph). Option A (relabel as empirical observation) honors academic-rigor honesty without abandoning substance — the multi-method convergence finding is genuinely informative as empirical observation supported by Model Independence Defense + Hong-Page 2004 *PNAS* diversity-of-models lineage. Framework's load-bearing claim about cross-model robustness is preserved at the empirical-observation level.
- **Option B (restructure as formal robustness theorem) considered + rejected:** would require independence-of-bias-structure assumption + probabilistic-convergence framework + sample-size analysis (~700-900 lines additional scaffolding); marginal payoff over Option A given that academic peer review would still ask "is the independence assumption empirically justified?" — same epistemic position with more apparatus. Hybrid path noted for future Phase B / Phase C: Option A in book + future methodology paper formalizing convergence as Hong-Page-extension robustness theorem.
- **Option C (hybrid title-only fix) considered + rejected:** title-only change without proof restructure leaves categorization mismatch unfixed; half-measures.
- **Side-effect on framework's "5 theorems" pedagogical structure:** framework drops from "5 theorems" to "4 derivable theorems + 1 empirical observation." Honest claim is more defensible than inflated claim; positioning shifts to "4 derivable theorems + 1 empirical observation supporting cross-model robustness."
- **Pass-fail verdict on as-currently-written E.2:** WEAK — categorization mismatch + internal text inconsistency (case-count) + circular peer-review-flag risk.
- **Pass-fail verdict on enhanced E.2 per rigor pass §14:** STRONG — empirical-observation framing matches proof form; case-count resolved; failure modes explicit; falsifiability clear; citations anchored.
- **Implementation pending:**
  - **Tech Appendix v1.0.0 HTML §10 lines 3261-3267 — replace E.2 statement + proof per rigor pass §14.1.**
  - **Tech Appendix v1.0.0 HTML §11 line 3234 + §D Section VIII line 3048 — cross-reference + case-count cleanup.**
  - **Bibliography expansion** — Hong & Page 2004 *PNAS*; (optional) Mosteller & Tukey 1977.
  - **Chapter prose + case study cross-references** — sweep for "Theorem E.2" / "Convergence Theorem"; replace with "Empirical Observation E.2" / "Cross-Model Convergence" / "E.2."
  - Same open question as Insights #35 + #38 + #40 + #47 + #48 + #49 + #50 + Phase 2 #8 + Phase 2 #3.2 [E.3] Tech Appendix HTML edit timing: apply now to v1.0.0 vs batch into Phase 3 v2.0.0 rebuild. **Recommended:** unified batch into v2.0.0 rebuild.
  - **Pre-publication external review** (per Insight #39) — empirical-economics methodologist verifies the Option A relabel adequately characterizes the convergence finding's nature.
- **Dependencies / Links:** E.4 rigor pass §16.3 (categorization-decision flag); Phase 1 §8 (theorems screening); Insight #40 (Theorem E.4 RATIFIED — methodology template); Insight #39 (pre-publication external review; downstream gate); Insights #35 + #38 + #40 + #47 + #48 + #49 + #50 (verdict-pattern cross-reference; shared open question on Tech Appendix HTML edit timing); Hong & Page 2004 *PNAS* (diversity-of-models lineage anchor); Damage Function + Real Options + RCV three-model architecture (Three Ways + RCV Formal-Model rigor pass commit `1c8e4dd` ratified 2026-04-24).

### Insight #52 — Phase 2 #8 RCV integrand Q(t) notation-clarity audit — CLOSED-RATIFIED 2026-04-29

- **Raised:** 2026-04-29 by Phase 1 §7.2 + §7.16 + §10 #7 (Q(t) notation flagged for Phase 2 academic-rigor verification on quality-vs-quantity ambiguity).
- **Status:** **closed-ratified 2026-04-29 (Chris Winn) — verdict (a) Full ratify all three notation-discipline enhancements** per `tools/rigor-passes/commons_bonds_rigor_pass_2026-04-29_phase2_rcv_integrand_q_notation_clarity_v1.0.0.md`, with specific author elections: Q3 **comprehensive bibliography** (all 6 references); Q4 **full cross-reference scope** (8+ locations); Q5 **batch into Phase 3 Tech Appendix v2.0.0 rebuild**.
- **Category:** academic-rigor · pass-fail-gate · notation-discipline · Phase 2
- **Content:** Three concrete notation-discipline enhancements ratified:
  1. **§B Definition A.3 expansion (per rigor pass §13.1):** explicit notational note (~120 words) with units, type-disambiguation, citation to divergent conventions, mapping advice for resource-economics readers. Distinguishes framework's Q-as-stock from Hotelling 1931 q-as-extraction-flow / Pindyck 1978 X(t)-for-stock / Dasgupta-Heal 1979 S(t)-for-stock (collides with framework's S = substitutability) / Mussa-Rosen 1978 Q-as-quality-index.
  2. **Cross-reference parentheticals — FULL SCOPE (per author election Q4):** 3 mandatory locations (Theorem E.4 statement line 3285; McDowell illustrative example line 2821; §M.5 general-form recovery line 6948 or 7020) + 5+ optional locations (§F existential analysis line 2552; §K formula breakdowns lines 1423/1447/1459; terms_index Substitutability Function entry; terms_index Externality Tail entry; terms_index RCV integrand entry; glossary v3 RCV entry). Each adds parenthetical `(per Definition A.3, Q(t) = remaining in-situ stock at time t)`.
  3. **Bibliography expansion — COMPREHENSIVE (per author election Q3):** all 6 references — Pindyck 1978 *JPE*; Dasgupta & Heal 1979 *Economic Theory and Exhaustible Resources*; Mussa & Rosen 1978 *J Econ Theory*; Slade & Thille 2009 *J Econ Lit*; Spence 1976 *Rev Econ Stud*; Tirole 1988 *The Theory of Industrial Organization*. (Hotelling 1931 already in bibliography per Hotelling Identity §12 multi-audience re-rigor 2026-04-29.)
- **Decisive criterion:** Q(t) consistently means "remaining in-situ stock at time t" across 13+ framework appearances; internal mathematical apparatus (∂U/∂Q < 0 monotonicity per Definition A.3 + Q_critical threshold coupling per Ripple Effects 1.0) forces correct reading for careful readers. But academic-publication discipline expects disambiguation at first encounter — Tier 2a-finance/IO + Tier 2e working-quant readers face HIGH first-encounter misread risk pattern-matching to Hotelling q-as-flow / Mussa-Rosen Q-as-quality conventions. Repair is notation-discipline + citation, not rename or re-derivation.
- **Rename Q → X considered + rejected:** downstream sweep cost across 13+ Tech Appendix + 3+ Ch 6 + 8+ Ch 7 GuidanceDoc + terms_index + glossary v3 + 4 prior rigor passes exceeds clarity gain since internal math already disambiguates; chapter prose currently fluent with "Q is large" / "Q decreases" phrasing; rhetorical anchor preservation favors keep-Q.
- **Cross-coordination with sibling Phase 2 audits:** bibliography overlap with Insights #47 (Pindyck 1978 + Dasgupta-Heal 1979 referenced as Hotelling-rent + scarcity-multiplier anchors) and P2#3.2 [E.3] (Pindyck 1978 + Dasgupta-Heal 1979 for premise P1-P3 derivation lineage). Combined Phase 3 v2.0.0 rebuild absorbs these references once.
- **Pass-fail verdict on as-currently-written Q(t) usage:** ADEQUATE-WEAK — survives sympathetic-referee review on internal-coherence grounds but flagged on convention-divergence grounds (uncited Q-for-stock choice diverges from Hotelling/Pindyck/Dasgupta-Heal lineage and from Mussa-Rosen IO lineage; the divergence is unmarked).
- **Pass-fail verdict on enhanced Q(t) usage per rigor pass §13:** STRONG — citation-anchored convention divergence; consistent cross-reference; explicit type-disambiguation in primary definition.
- **Implementation pending — BATCHED into Phase 3 v2.0.0 rebuild per author election Q5:**
  - **Tech Appendix v1.0.0 HTML §B Definition A.3 (line 432-449)** — expanded text per §13.1.
  - **Tech Appendix v1.0.0 HTML §10 Theorem E.4 statement (line 3285) + McDowell (line 2821) + §M.5 (line 6948 or 7020) + §F (line 2552) + §K (lines 1423/1447/1459)** — cross-reference parentheticals per §13.2.
  - **`core/terms/terms_index.md`** — Substitutability Function + Externality Tail + RCV integrand entries cross-reference parentheticals.
  - **`core/glossary/commons_bonds_updated_glossary_v3.html`** — RCV entry cross-reference parenthetical.
  - **Bibliography expansion** — Pindyck 1978; Dasgupta-Heal 1979; Mussa-Rosen 1978; Slade-Thille 2009; Spence 1976; Tirole 1988 (overlaps with Insights #47 + P2#3.2 [E.3] absorbed once).
  - **terms_index** — append Phase 2 verdict entry; cross-reference to this rigor pass.
  - **Pre-publication external review** (per Insight #39) — resource-economist verifies Q-for-stock convention is stated with sufficient prominence to disambiguate at first formula encounter.
- **Dependencies / Links:** Phase 1 full framework audit §7.2 + §7.16 + §10 #7; Insight #40 (Theorem E.4 RATIFIED — Q(t) appears in restructured premises A1 polynomial growth on U; this audit's enhancements are non-disruptive to E.4 proof structure); Insight #47 (P2#7 RATIFIED — Pindyck 1978 + Dasgupta-Heal 1979 bibliography overlap); P2#3.2 [E.3] [PROPOSED] (Pindyck 1978 + Dasgupta-Heal 1979 for premise derivation); Insight #39 (pre-publication external review; downstream gate); Insights #35 + #38 + #40 + #47 + #48 + #49 + #50 + #51 (verdict-pattern cross-reference; shared open question on Tech Appendix HTML edit timing — RATIFIED batched into Phase 3 v2.0.0 rebuild per author election); Hotelling 1931 (already in bibliography per Hotelling Identity §12); Pindyck 1978 + Dasgupta-Heal 1979 + Mussa-Rosen 1978 + Slade-Thille 2009 + Spence 1976 + Tirole 1988 (new bibliography additions; comprehensive convention-divergence anchors).

### Insight #53 — Phase 2 #3.3 Theorem E.5 dual-scope audit (Renewable Imperative → Substitution Dominance + proof restructure) — CLOSED-RATIFIED 2026-04-29

- **Raised:** 2026-04-29 by Phase 1 §10 #8 + E.4 rigor pass §16.3 (E.5 over-specified scope flag) + author direction 2026-04-29 (cross-political-tradition vocabulary concern dual-scope mandate).
- **Status:** **closed-ratified 2026-04-29 (Chris Winn) — verdict (a) Full ratify Option α + β COMBINED** per `tools/rigor-passes/commons_bonds_rigor_pass_2026-04-29_phase2_theorem_e5_dual_scope_v1.0.0.md`. Author election: **"Substitution Dominance"** as rename target (SC8 substantive-claim accuracy weighted higher than Tier 1 + Tier 2c-climate-progressive bold-framing rhetorical force) per audience-cell scoring 8-2 favoring Dominance + register-splitting insight (chapter title carries bold framing; theorem name carries technical precision). Tech Appendix HTML edit timing batched into Phase 3 v2.0.0 rebuild.
- **Category:** academic-rigor · pass-fail-gate · vocabulary-collision · proof-structure · theorem-rename · Phase 2
- **Content:** Six concrete repair enhancements ratified across two dimensions:
  
  **DIMENSION 1 — Vocabulary collision:**
  1. **Rename theorem:** "Theorem E.5 (Renewable Imperative)" → **"Theorem E.5 (Substitution Dominance)"**. Aligns with framework's Substitutability Function (S) lineage; matches concept-noun naming pattern of E.1 (Structural Cost Severance) / E.3 (Abundance Masking) / E.4 (Integral Convergence) / E.2 (Cross-Model Convergence per Insight #51). Cross-political-tradition robust. Technically accurate to "weakly dominant" formal claim.
  2. **Chapter 9 title:** RESOLVED per author 2026-04-29 (already retitled "Pricing Honestly" at `manuscript/chapters/Chapter__9_PricingHonestly__Draft.md`); audit scope correctly theorem-name-only.
  
  **DIMENSION 2 — Proof structure:**
  3. **Premise enumeration P1–P4:** P1 (CS > 0 condition); P2 (substitutability-improvement structural premise — investment in S* shifts S(t) upward); P3 (future-generation positive welfare weight); P4 (investment-cost ≤ P opportunity-cost framing).
  4. **Universal quantifier scope-tightening:** "any discount rate" → "any discount rate consistent with P1 (CS > 0)"; "any ethical framework that does not assign zero weight to future generations" → "any ethical framework satisfying P3 (positive weight to future generations)"; "any S_max > 0" → "any S_max where P2 holds (investment can improve S(t))".
  5. **Failure-mode acknowledgment:** four explicit failure modes — (a) discount-rate failure (high discount drives CS to zero); (b) substitutability-investment failure (no substitute can improve S(t)); (c) ethical-framework failure (pure-presentism); (d) investment-cost regime failure (Investment_cost > P).
  6. **Practical-corollary separation as Corollary E.5.1 (Optimal Extraction Sequencing):** "extract from sources where RCV is lowest first" promoted from proof-appendage to standalone Corollary; preserves "navigation system, not a prohibition" rhetorical anchor as separate interpretation note.
  
  Plus: bibliography citations to Hartwick 1977 + Solow 1974 + Weitzman 2001 + Dixit-Pindyck 1994 + Stiglitz 2000 + Stern Review 2007 (most already in framework's bibliography per other ratified rigor passes).
- **Decisive criterion (vocabulary):** Theorem proves **weak dominance** (formal welfare-comparison result) under P1–P4. "Imperative" implies moral mandate; theorem proves comparison-ordering. Naming should match the formal claim. SC8 substantive-claim accuracy + theorem-family symmetry + cross-political-tradition robustness + Tier 2a finance/IO + Tier 2e working-quant + Tier 2d cross-political-tradition all favor "Substitution Dominance." Chapter 9 already retitled "Pricing Honestly" carries bold framing at chapter level; theorem name doesn't need to also carry bold framing — register-splitting insight: chapter prose carries colloquial-accessibility + mandate-framing layers; theorem stays technically precise.
- **Decisive criterion (proof-structure):** Three over-specified universal quantifiers ("any discount rate, any ethical framework, any S_max") with implicit failure modes. Practical corollary embedded in proof creates structural-classification ambiguity. Restructure tightens quantifier scope, makes failure modes explicit, separates corollary as standalone Corollary E.5.1.
- **Pass-fail verdict on as-currently-written E.5:** WEAK / FAIL — vocabulary politically-coded + technically inaccurate; proof over-specified + corollary embedded.
- **Pass-fail verdict on enhanced E.5 per rigor pass §15:** STRONG — politically-neutral + technically accurate naming; premises enumerated; quantifiers scoped; failure modes explicit; corollary separated; citations anchored.
- **Implementation pending — BATCHED into Phase 3 v2.0.0 rebuild:**
  - **Tech Appendix v1.0.0 HTML §10 lines 3288-3294** — replace E.5 statement + proof + corollary per rigor pass §15.1.
  - **Tech Appendix cross-references** (~5-10 instances of "Renewable Imperative theorem" → "Substitution Dominance theorem").
  - **Chapter prose retraining** — Ch 5 line 99 + other inline references.
  - **Case studies book-home pointers** (~10-15 instances).
  - **Bibliography chapter-relevance pointers** (~3-5 instances).
  - **`core/terms/terms_index.md`** — append Phase 2 verdict entry; cross-reference to this rigor pass.
  - **Provenance traces preserved:** older rigor passes + ratified-insight references retain "Renewable Imperative" historical naming per Working Principle #8 retirement-trace discipline parallel.
  - **Pre-publication external review** (per Insight #39) — multi-perspective review (welfare-economist + policy-economist + formal-methods reviewer).
- **Dependencies / Links:** Phase 1 full framework audit §10 #8 (Renewable Imperative theorem flagged); E.4 rigor pass §16.3 (over-specified-scope flag for E.5); Insight #40 (Theorem E.4 RATIFIED — methodology template); Insight #51 (P2#3.4 [E.2] RATIFIED — sibling theorem categorization audit); Insights #35 + #38 (cross-political-tradition robustness discipline); Insight #25 (academic-trade hybrid press strategy — Mazzucato/Raworth/Anderson exemplar; register-splitting insight); Insight #39 (pre-publication external review; downstream gate); P2#3.2 [E.3] [PROPOSED] (sibling theorem audit; Pindyck 1978 + Dasgupta-Heal 1979 bibliography overlap); Hartwick 1977 + Solow 1974 (already in framework bibliography per Hotelling Identity §12); Weitzman 2001 (already per Insight #40); Dixit-Pindyck 1994 (already per Insight #47); Stern Review 2007 (already per Externality Tail M12 lineage / Insight #49); Stiglitz 2000 (likely already in framework bibliography). Chapter 9 draft at `manuscript/chapters/Chapter__9_PricingHonestly__Draft.md` — already retitled away from "Renewable Imperative."

---

### Insight #63 — "Tier" word-level conceptual collision (vocabulary-strategy four-move ladder vs retired 8-tier decomposition) — OPEN

- **Raised:** 2026-04-30 by Claude during Insight #60 scaffolding cleanup pass; surfaced when author asked whether "vocabulary strategy worked examples §10.3 + §10.6 (pedagogical illustrations of the Tier framework)" referenced the retired 8-tier framework.
- **Status:** **OPEN** — quick-fix (B) applied 2026-04-30 (vocabulary strategy v1.0.1 §3.1 disambiguation note); focused rigor pass (D) queued for pre-publication external review window.
- **Category:** vocabulary · cross-document conceptual collision · pre-submission readiness
- **Content:** The word "Tier" is currently used for two entirely distinct framework concepts:
  - **(1) 8-tier decomposition** (RETIRED 2026-04-24 per tier-reframing rigor pass §11.2 + Path F variable-addability ratification): "Tier 1" through "Tier 8" — *cost categories* (Lifetime Survival Cost / Actuarial Risk Cost / Mission Failure Reserve / Lineage Labor Cost (formerly Dynastic) / Foreclosure Cost / Community Transition Reserve / Ecological Carrying Cost / Knowledge and Cultural Cost / Political Capture Cost). Number-qualified. Replaced by Cᵢ admission via Four Gates per Path F. Archived 2026-04-30 per Insight #55.
  - **(2) Vocabulary strategy four-move tier ladder** (RATIFIED 2026-04-28 per Insight #27): "Tier A" / "Tier B" / "Tier C" / "Tier D" — *vocabulary-decision moves* (adopt verbatim with citation / adopt with specialization footnote / descriptive prose / framework-coined term). Letter-qualified. Codified in vocabulary strategy v1.0.1 §3.

  Today's disambiguation is qualifier-based (number vs letter). This works *most* of the time, but: (a) standalone "Tier" without qualifier is ambiguous; (b) "Tier framework" without qualifier is ambiguous (which one?); (c) future readers + reviewers + publishers may still conflate. Insight #55 hypothesis (cross-document audits surface collisions single-document audits miss) generalizes from letter notation (S, α, τ) + multi-letter abbreviations (RCV, CIT) to **word-level conceptual collisions** — this is exactly that kind of finding.

- **Why it matters:** Per author direction 2026-04-29 ("if we get these wrong we will likely fail to get published"), vocabulary collisions matter for academic-trade hybrid + pre-publication external review reading. A reviewer encountering "Tier framework" without qualifier and lacking the framework-internal context could conflate the two concepts and either: (i) ask why the retired 8-tier scheme is still being referenced, undermining trust in the framework's discipline; or (ii) miss the vocabulary-strategy distinction entirely, reading "Tier B" as "second-tier of cost decomposition" rather than "second move in vocabulary-decision ladder." Both failure modes are pass/fail-gate hits per the author's framing.

- **Quick-fix applied (B) 2026-04-30:** Vocabulary strategy v1.0.1 §3.1 — added disambiguation note distinguishing letter-qualified vocabulary moves from number-qualified retired decomposition; instructs always-include-qualifier discipline; flags standalone "Tier framework" as ambiguous-not-to-be-used.

- **Deferred decision (D):** Focused rigor pass on whether qualifier-based disambiguation is sufficient OR whether a vocabulary-strategy rename is warranted. Decision questions:
  - **(α) No further action — qualifier-based disambiguation is sufficient.** Quick-fix (B) closes the most acute reader-confusion path; remaining ambiguity is acceptable.
  - **(β) Rename vocabulary-strategy "Tier" to alternative.** Candidates: "Move A/B/C/D" (action-noun; closer to ladder semantics); "Class A/B/C/D" (adopts taxonomy semantics); "Level A/B/C/D" (overloaded — risk of new collision with rigor-protocol module-level vocabulary); other. **Substantial change** — vocabulary strategy v1.0.1 is RATIFIED (Insight #27); rigor passes use "Tier A/B/C/D" extensively (Insights #34, #35, #38, #50–#58 all reference Tier classifications); rename cascades widely. Would warrant a focused rigor pass + multi-file sweep.
  - **(γ) Rename retired 8-tier to "the C₁–C₉ decomposition" or similar in residual references.** Less invasive — affects only retirement traces + archive references. But the retired scheme is already retired; renaming inert references may be lower-value than (β).

- **Why focused rigor pass (D):** This collision is exactly the methodology Insight #55 surfaced (cross-document audits catch what single-document audits miss). Insight #55 explicitly extended to word-level conceptual collisions in its scope-extension note; Insight #63 is the first such finding. The pass would: (1) audit usage frequency of "Tier" across active scaffolding + manuscript drafts + rigor passes to quantify ambiguity surface; (2) test all three decision options ((α) / (β) / (γ)) against pass/fail-gate criteria (academic reviewer; trade publisher; literary agent; intended audience); (3) recommend a verdict; (4) if (β) wins, apply the rename via dedicated rigor pass + sweep.

- **Trigger condition:** queue for pre-publication external review window (Insight #39); the rigor pass is most useful as part of pre-submission readiness rather than mid-Phase-3 work. Could land alongside or just before pre-publication external review begins.

- **Dependencies / Links:** Insight #21 (Path F + Four Gates supersedes 8-tier decomposition); Insight #27 (vocabulary strategy four-move ladder ratification); Insight #34, #35, #38, #50–#58 (rigor passes using Tier A/B/C/D classifications); Insight #39 (pre-publication external review; trigger window); Insight #55 (notation collision audit; methodology parent + scope-extension note explicitly extending to word-level conceptual collisions); Insight #60 (scaffolding cleanup pass during which this surfaced); vocabulary strategy v1.0.1 §3.1 (where quick-fix (B) lives); tier-reframing rigor pass `tools/rigor-passes/commons_bonds_rigor_pass_2026-04-24_tier_reframing_v1.0.0.md`.

- **Todo link:** "Focused rigor pass on Tier word-level collision (Insight #63) — schedule for pre-publication external review window."

---

### Insight #62 — Archive folder consolidation — CLOSED-RATIFIED 2026-04-30

- **Raised:** 2026-04-30 by author direction during Insight #60 scaffolding cleanup pass: *"we have a few archive folders floating around the project now, we can probably consolidate all of those to one main folder now."*
- **Status:** **closed-ratified 2026-04-30 (Chris Winn) — verdict (c) hybrid as canonical pattern.** Top-level `archive/` for cross-domain retirement material (retirements index, retired methodologies, multi-book seed); per-domain `<domain>/archive/` for domain-specific historical predecessors kept adjacent to live work. Convention documented in [`archive/retirements/index.md`](../archive/retirements/index.md) §0 + [`AGENTS.md`](../AGENTS.md) "Archive convention" section.
- **Category:** project-hygiene · archive-discipline · directory-structure
- **Content:** The project had 4+ archive locations:
  - `archive/` (top-level) — `_OneDayMaybe/` + `decomposition/` (post-Insight #55) + `retirements/` (per Insight #59)
  - `core/technical-appendix/archive/` — superseded TA versions + supplements
  - `manuscript/chapters/archive/` — Ch 6 supplementary drafts
  - `tools/archive/` — retired rigor protocols + old layer-tier-stress-test
- **Decision questions tested:**
  - **(a) Consolidate now to `archive/{technical-appendix,manuscript-chapters,tools}/`** — REJECTED. Low marginal navigability gain vs. ~10-20 path-update cost across rigor passes + scaffolding cross-references; would have lost domain-context proximity (origin domain encoded by subfolder adjacency to live work); would have broken external bookmarks for marginal benefit.
  - **(b) Leave per-domain archives** — REJECTED. No documented convention; status quo without ratification.
  - **(c) Hybrid: top-level `archive/` for cross-domain + per-domain archives for domain-specific historical** — **SELECTED.** Existing layout already approximated this; ratifying the convention locks the pattern. Reinforced by Working Principle #10 (NEW 2026-04-30) which explicitly licenses rich internal-scaffolding structure; per-domain archives align with internal-scaffolding richness discipline.
- **Why (c):**
  1. Zero migration cost; convention is documented rather than executed.
  2. Origin context preserved — file in `manuscript/chapters/archive/` is obviously a chapter-draft predecessor; flattened to `archive/manuscript-chapters/` it loses adjacency to live chapter directory.
  3. Cross-domain audit-trail need already solved by canonical retirement-archive index (refined WP#4); no centralization gap to fill.
  4. WP#10 "internal scaffolding can be rich" license endorses domain-proximity structure as design pattern, not navigability accident.
- **Implementation applied 2026-04-30 (this commit):**
  1. **`archive/retirements/index.md` §0 added** — archive structure convention documented as canonical pattern; v1.0 → v1.1 version bump.
  2. **`AGENTS.md` "Archive convention" section** — same convention surfaced for AI collaborator + author orientation; rationale referenced.
  3. **No file moves performed** — (c) is convention-only; existing file locations are now ratified-canonical.
- **Implementation NOT pending** — (c) verdict is convention-ratification, not execution. No further work required unless (a) is reconsidered later.
- **Dependencies / Links:** Insight #55 (notation collision audit + hygiene pass; established `archive/decomposition/` pattern); Insight #59 (Working Principle #4 refinement; established `archive/retirements/` pattern); Insight #60 (scaffolding cleanup pass; this insight surfaced during that work); Insight #61 (README maintenance; co-ratified this commit per Thread γ); Working Principle #10 (NEW 2026-04-30; reinforces verdict (c)); [`archive/retirements/index.md`](../archive/retirements/index.md) §0 (canonical convention text); [`AGENTS.md`](../AGENTS.md) (internal-orientation document carrying same convention).

---

### Insight #61 — README.md comprehensive update — CLOSED-RATIFIED 2026-04-30

- **Raised:** 2026-04-30 by author direction during Insight #60 scaffolding cleanup pass: *"Probably makes sense to update the README.md file in the root directory soon, let's add that to a to do list."*
- **Status:** **closed-ratified 2026-04-30 (Chris Winn) — verdict (R2): split publisher-facing landing page from internal-scaffolding orientation per Working Principle #10.** README rescoped as slim publisher-facing landing page; new [`AGENTS.md`](../AGENTS.md) holds the rich internal-scaffolding orientation (canonical-state table, repository structure, working discipline, routines, retirement archive references, queued work, session workflow, operating rules, internal-vocabulary key concepts).
- **Category:** project-hygiene · README-maintenance · publisher-prep · WP#10-application
- **Content (mid-resolution reframe):** Initial sweep landed comprehensive README updates per the original Insight body. WP#10 ratified mid-Thread-γ (α-thread parallel ratification 2026-04-30) reclassified README as publisher-facing layer; original sweep was identified as scaffolding-voice contamination (insight numbers; WP numbers; routine sentinels; phase labels; operating rules; session workflow). Author selected verdict (R2) — split now rather than scrub-later (which is exactly what Insight #37 captures as the scrubbing-pass cost; WP#10 prevents at origination).
- **Three response options tested:**
  - **(R1) Land hybrid sweep as-is, defer split** — REJECTED. Defers WP#10-compliance work; would later require an Insight #37-style scrubbing pass.
  - **(R2) Re-scope per WP#10 — split publisher-facing README from internal-scaffolding AGENTS.md** — **SELECTED.** Gets the principle right at the start; migration cost is low (most original sweep content moves cleanly to AGENTS.md); aligns Thread γ output with v1.49.0 §3.5 cross-thread discipline addendum.
  - **(R3) Light-touch scrub of hybrid README** — REJECTED. Compromise that doesn't fully comply with WP#10; would require further passes.
- **Implementation applied 2026-04-30 (this commit):**
  1. **`README.md` rescoped** — slim publisher-facing landing page: project description, success criterion, three-book structure, "where to find what" reading orientation, ten dimensions, migration note, pointer to `AGENTS.md` for collaborators. Pattern 2 discipline applied: demonstrates project orientation through pointer-to-content rather than codifying internal state.
  2. **`AGENTS.md` NEW** — canonical internal-scaffolding orientation document. Contains: current canonical state table (16+ rows), repository structure (full), archive convention (Insight #62), working discipline (10 WPs), WP#10 layer classification, what's queued, session workflow, operating rules, key conceptual foundations.
  3. **`archive/retirements/index.md` §0 archive convention added** — co-ratified with Insight #62 verdict (c).
- **Why this matters (post-resolution):**
  - First-time readers (publisher; agent; external reviewer) get the framework essence + book structure + reading orientation; not internal evolution-tracking.
  - AI collaborator + author + future-Claude get full canonical-state orientation in `AGENTS.md` without scaffolding-bleed into publisher-facing register.
  - WP#10 prevents the hybrid-contamination Insight #37 would later have to undo.
- **Dependencies / Links:** Insight #60 (scaffolding cleanup; partial README updates applied 2026-04-30 commit `47408e1`); Insight #62 (archive consolidation; co-ratified this commit per Thread γ); Insight #59 (refined WP#4; cross-references retirement-archive index); Working Principle #10 (NEW 2026-04-30; ratified during Thread δ; reframed Insight #61 mid-Thread-γ); Working Principle #8 (publisher-facing scrubbing; complementary to WP#10 origination discipline); v1.49.0 §3.5 (cross-thread discipline addendum); all Phase 2 + Group 1 ratifications (current canonical state preserved in `AGENTS.md`).

---

### Insight #60 — Scaffolding cleanup pass: refined WP#4 application + broken-paths + stale-claims sweep — CLOSED-RATIFIED 2026-04-30

- **Raised:** 2026-04-30 by author direction following Insight #59 ratification: *"(a) Insight #37 / scaffolding cleanup pass — apply refined WP#4 across active scaffolding (terms_index v1.0.0 bump; vocabulary strategy + working principles light-trace migration; broken-path + stale-claim sweep)."*
- **Status:** **closed-ratified 2026-04-30 (Chris Winn) — applied per author direction.** Mechanical fixes applied; further refined-WP#4 application (terms_index v1.0.0 version bump; vocabulary strategy v1.0.1 §6 + §7 + §13 light-trace migration) queued for separate session. Insight #37 scaffolding-vs-publisher-facing separation pass remains OPEN for original publisher-facing-side scope.
- **Category:** project-hygiene · scaffolding-cleanup · refined-WP#4-application · broken-paths · stale-claims · publisher-prep
- **Content:** Mechanical scaffolding cleanup pass applying refined WP#4 (Insight #59) + fixing broken paths + correcting stale current-state claims. ~13 file edits across 11 files:

**Broken-path fixes (post-iCloud-incident relocation + post-archive operations):**
1. `tools/routines/proposed_routines_v1.0.0.md` — 4 instances of `/Users/c17n/Documents/___WorkingOn/commons-bonds` → `/Users/c17n/commons-bonds` (lines 31, 148, 254, 304; daily sentinel + weekly pre-submission audit + rigor pass tracker + open insights status sync prompts).
2. `core/case-studies/commons_bonds_case_study_audit_v1.0.6.md` line 477 — `core/decomposition/eight-tier-v10.html` → `archive/decomposition/eight-tier-v10.html` with 8-tier RETIRED context note.
3. `alignment/patches/pending-framework-review/README.md` line 17 — `core/decomposition/` → `archive/decomposition/` with retirement context.
4. `core/technical-appendix/TechnicalAppendix_v1.0.0.html` line 3007 — supplement reference → `core/technical-appendix/archive/...`
5. `core/technical-appendix/empirical_sourcing_pass_2026-04-25.md` + `method3_sensitivity_analysis_2026-04-25.md` + `block4_validation_2026-04-25.md` — supplement references → archive path (3 files).
6. `alignment/patches/cit_positioning_consistency_audit_2026-04-25.md` — supplement references → archive path.

**Stale current-state claim fixes:**
7. Root `README.md` — Tech Appendix entry "v0.0.4 canonical" → "v1.0.0 canonical" with Phase 3 v2.0.0 rebuild note; Glossary entry "v2 canonical" → "v3 canonical" with Phase 4 v4 rebuild note.
8. `tools/README.md` line 65 — `commons_bonds_abundance_dimensions_v1_2_0.md` → `v1_3_0.md` (file listing).
9. `research/case-studies/indigenous-land-dispossession.md` line 197 — v1_2_0 → v1_3_0 with Phase 3 absorption note.
10. `research/literature/bibliography.md` line 935 — Tech Appendix v0.0.2 → v1.0.0 with Insight #60 note.
11. `core/case-studies/commons_bonds_case_study_audit_v1.0.6.md` line 1562 — Tech Appendix v0.0.3 → v1.0.0 with archive note.

**Header-note additions (per refined WP#4 retention discipline):**
12. `alignment/patches/canonical_term_regression_audit_2026-04-25.md` — header note added explaining v0.0.5 references describe historical state; current canonical is v1.0.0.

**Items intentionally NOT updated (preserved per refined WP#4):**
- `alignment/decisions/alternate-8-tier-individual-level-retired.md` — retired-decision document (filename indicates retired status); historical context preserved per WP#4 Tier 2.
- `alignment/commons_bonds_working_principles_v1.0.0.md` line 475 — references old iCloud path in WP#9 origination story (historical context per refined WP#4).
- `alignment/commons_bonds_open_insights_v1.0.0.md` line 509 — historical Insight reference to v0.0.5 work (preserved per WP#4 historical-context).
- `tools/pre-submission-reviews/commons_bonds_pcr_2026-04-23_v1.1.0.md` — dated frozen-snapshot per WP#4 Tier 2.
- Historical rigor passes — preserved per refined WP#4 (full traces in dated/ratified rigor pass files).
- Archived files (`archive/_OneDayMaybe/`, `tools/archive/`, etc.) — preserved per WP#4 Tier 2.

**Surfaces for future cleanup work (queued; NOT applied this commit):**
- terms_index v1.0.0 version bump applies summary-level retirement traces (Insight #59 §6.2 implementation pending) — substantial work; deferred to dedicated session.
- Vocabulary strategy v1.0.1 §6 + §7 + §13 light-trace migration (Insight #59 §6.2) — medium scope; deferred or absorbed into Insight #37.
- Working principles body cleanup (Insight #59 §6.2) — small; some inline traces could cross-reference archive (deferred).

**Insight #37 status:** remains OPEN. Insight #37's original scope is publisher-facing-side scaffolding-vs-publisher-facing separation pass + word-count recompute (chapters/glossary/Tech Appendix). Insight #60 covered scaffolding-side cleanup. Insight #37 remains OPEN for publisher-side work; coordinated with Insight #61 (README maintenance) + Insight #62 (archive consolidation).

**New Insights surfaced this pass:**
- **Insight #61 (OPEN):** README.md comprehensive update queued.
- **Insight #62 (OPEN):** Archive folder consolidation queued.

**Dependencies / Links:** Insight #59 (refined WP#4; this insight applies it); Insight #37 (scaffolding-vs-publisher-facing separation pass; remains OPEN for publisher-side scope); Insight #55 (notation collision audit + hygiene pass; established `archive/decomposition/` pattern); Insight #61 (README maintenance; new sibling); Insight #62 (archive consolidation; new sibling); Working Principle #4 (refined per Insight #59); Working Principle #8 (publisher-facing scrub; complementary).

---

### Insight #59 — Working Principle #4 refinement: Tiered retirement-trace policy + retirement-archive index — CLOSED-RATIFIED 2026-04-30

- **Raised:** 2026-04-30 by author direction *"Should I change the framework's discipline of keeping retirement traces in scaffolding documents?"* The question surfaced after Group 1 ratification batch + Insight #55 cleanup work, where retirement-trace volume across scaffolding docs became visible.
- **Status:** **closed-ratified 2026-04-30 (Chris Winn) — verdict: Tiered retirement-trace policy + retirement-archive index combined (Options B + C per `tools/rigor-passes/commons_bonds_rigor_pass_2026-04-30_working_principle_4_refinement_v1.0.0.md`).** Working Principle #4 refined; retirement-archive index created.
- **Category:** working-principle-revision · scaffolding-discipline · retirement-trace-policy · publisher-prep · framework-maturity
- **Content:** Refine WP#4 retirement-trace discipline as the framework matures from work-in-progress phase to publisher-prep phase. Tiered policy by document type:
  - **Open insights / pending rigor passes:** full traces (active discipline; status quo)
  - **Ratified rigor passes (frozen):** full traces preserved as historical record (status quo)
  - **Working principles + vocabulary strategy:** light traces in body; cross-reference retirement archive index
  - **terms_index v1.0.0+:** summary-level traces (1-line "renamed YYYY-MM-DD per Insight #N"); full traces in retirement archive
  - **Publisher-facing (Tier 1 per WP#8):** no traces (status quo)
  - **Tier 2 archived/superseded:** header-note only (status quo)
  
  PLUS: dedicated `archive/retirements/index.md` — single canonical retirement-archive index. Other scaffolding documents reference this index rather than carrying full retirement traces inline.
- **Decisive criterion:** at the publisher-prep phase, the discipline's costs (terms_index bloat; navigability decline; Phase 3+4 rebuild inheriting noise; pre-publication external review friction) began to outweigh its benefits (provenance + reversibility + M12 honesty). Refined discipline preserves the purpose (via retirement archive + ratified rigor passes) while addressing navigability cost.
- **5 alternatives tested at full rigor depth (per rigor pass §4):**
  - (A) Status quo — REJECTED (navigability declining)
  - **(B) Tiered policy** — STRONG (7/7 dimensions); selected
  - **(C) Retirement-archive index standalone** — STRONG with caveat (incomplete without active-scaffolding policy); paired with (B)
  - (D) Sunset clause — REJECTED (calendar overhead)
  - (E) Two-tier scaffolding — STRONG but functionally equivalent to (B) with less granularity
- **What this preserves:** provenance (retirement archive + ratified rigor passes); reversibility (rigor passes remain canonical); M12 attribution-honesty (academic lineage in rigor passes + vocabulary strategy); Routine 1+2 sentinels (cross-reference archive for remediation hints); Working Principle #8 publisher-facing scrub (unchanged; complementary).
- **What this changes:** terms_index v1.0.0+ reads as current-state document; working principles + vocabulary strategy less cluttered; single canonical retirement archive; Phase 3+4 rebuilds derive from cleaner sources; pre-publication external reviewer sees current state cleanly.
- **Implementation applied 2026-04-30:**
  1. **Working Principle #4 refinement note** added to `alignment/commons_bonds_working_principles_v1.0.0.md` Principle #4 (REFINEMENT 2026-04-30 per Insight #59 section). Per-document-type table updated with refined policy.
  2. **Retirement-archive index** created at `archive/retirements/index.md` — initial structure + populated with 16 vocabulary retirements + 2 methodology retirements + 3 file/artifact retirements + cross-references to ratifying rigor passes + maintenance discipline + index versioning.
- **Implementation pending (queued for Phase 3 + scaffolding cleanup):**
  - **terms_index v1.0.0 version bump** — apply summary-level traces; full traces moved to archive/retirements/index.md. Substantial work (~2,000+ lines of terms_index to review for retirement-trace migration).
  - **Working principles body cleanup** — replace inline retirement traces with archive cross-references where appropriate (small).
  - **Vocabulary strategy v1.0.1 §6 + §7 + §13 cleanup** — light retirement traces; cross-reference archive (medium).
  - **Insight #37 (scaffolding-vs-publisher-facing separation)** — incorporates this refined WP#4 discipline as part of separation pass scope.
  - **Phase 3 Tech Appendix v2.0.0 rebuild** — derives from cleaner terms_index v1.0.0+.
  - **Phase 4 Glossary v4 rebuild** — derives from cleaner terms_index v1.0.0+.
  - **Routine 1 + 2 patterns cosmetic update** — already function correctly; cross-reference retirement archive for remediation hints.
- **Pre-publication external review (Insight #39):** the refined discipline IMPROVES reviewer experience — current-state visible cleanly + full audit trail accessible via retirement archive + ratified rigor passes. Reviewer needs less scaffolding context to evaluate publisher-facing content.
- **Dependencies / Links:** `tools/rigor-passes/commons_bonds_rigor_pass_2026-04-30_working_principle_4_refinement_v1.0.0.md` (full audit trail); `archive/retirements/index.md` (new canonical retirement-archive); Working Principle #4 refinement note (this commit); Working Principle #8 (publisher-facing scrub; complementary; unchanged); Working Principle #1 (effort-to-repair-not-rigor; supports refinement); Insight #28 (retirement-traces / scaffolding-vs-publisher-facing trichotomy origin); Insight #37 (OPEN scaffolding-vs-publisher-facing separation; natural integration point); Insight #39 (pre-publication external review; refinement improves reviewer experience); Insight #55 (notation collision audit; sibling cleanup work that surfaced retirement-trace volume).

---

### Insight #57 — Group 1.2 Intergenerational Option Value Tier B promotion — CLOSED-RATIFIED 2026-04-30

- **Raised:** 2026-04-29 by holistic strategy §10 §5.1 — Tier B promotion vs defer discussion-needed verdict for newly-proposed framework Tier D coinage; subsequently elevated 2026-04-30 to Tier B classification via Group 1.2 rigor pass.
- **Status:** **closed-ratified 2026-04-30 (Chris Winn) — verdict (α) Tier B promotion + dedicated terms_index entry** per `tools/rigor-passes/commons_bonds_rigor_pass_2026-04-30_group1_2_intergenerational_option_value_v1.0.0.md`. Full-depth rigor test parallel to Phase 2 #3.# theorem audits on three options (α Tier B promotion; β defer; γ Tier C descriptive prose). Decisive criterion: argument-load-bearing distinction — Ch 4 *The Existence Proof* argument-spine depends on this concept; threshold-policy that defers other single-chapter Cᵢ items applies to illustrative mentions, not argument-spines.
- **Category:** vocabulary · framework-discipline · Ring-2 · Tier B classification · academic-anchor + framework-specialization
- **Content:** **Intergenerational Option Value** ratified at Ring-2 + Tier B with dedicated terms_index entry. Specialization of real-options theory's option-value concept (Henry 1974; Arrow + Fisher 1974; Dixit + Pindyck 1994) to intergenerational temporal-scope. Distinct from Substitutability Function S(t) — S captures probability of substitute existing; Intergenerational Option Value captures welfare value of preserving optionality.
- **Decisive criterion:** Argument-load-bearing distinction. Ch 4 *The Existence Proof* frames the entire chapter argument via option-value reasoning — the "existence proof" is that this option-value is non-zero under any reasonable preservation-of-future-utility assumption. Without this concept, Ch 4's argument structure collapses (substitutability-function-only OR externality-tail-only reformulations both lose precision per Group 1.2 rigor pass §4.2). Argument-load-bearing-ness is a separate axis from frequency-of-occurrence (per Insight #32 §32.3 corollary: usage-frequency-not-rigor-argument).
- **12-cell multi-audience matrix:** 9 STRONG + 3 ADEQUATE (Tier 2d Indigenous + heterodox; Socialist/communitarian; Lived-oppression — option-value reads as detached/abstract for present-suffering positions). Mitigable via Tech Appendix §L methodological footnote parallel to Insight #35 + #38 patterns. M11 SURVIVES all 5 probes. Cross-political-tradition robustness STRONG on classical-liberal + civic-republican; ADEQUATE on socialist/communitarian + lived-oppression (mitigable via §L footnote).
- **Tier-ladder:** Tier B clean (Henry 1974 + Arrow-Fisher 1974 + Dixit-Pindyck 1994 close-fit academic anchors + Howarth-Norgaard 1990 + 1992 intergenerational-extension; framework-specialization decodable via light footnote — intergenerational temporal-scope + framework-Cᵢ integration via CIT + Four Gates). Tier A FAILS strict-fit (composition novel as a unit); Tier C demotion not viable (Ch 4 argument-load-bearing); Tier D over-coining (Tier B suffices given lineage anchors).
- **Implementation applied 2026-04-30:**
  1. **terms_index dedicated Ring-2 entry** added (lines following Externality Tail / before Asymmetric Regret Principle); rendering fields per S1 schema (working definition; status; glossary_definition ~80 words; tech_appendix_definition ~280 words; rigor provenance; M12 lineage citations; cross-political-tradition robustness note; pre-publication external-review queue; implementation pending list; pairs-with notes).
- **Implementation pending Phase 3 v2.0.0 rebuild:**
  - **Tech Appendix §L methodological footnote** on Intergenerational Option Value commodification critique + intergenerational-temporal-scope specialization (parallel to Insight #35 + #38 §L footnote patterns). Mitigation for Tier 2d + socialist/communitarian + lived-oppression ADEQUATE cells.
  - **Glossary v3 → v4 rebuild** dedicated Intergenerational Option Value entry derived from terms_index per S1 schema.
  - **Optional Ch 4 prose tightening** — verify framework-specialization + lineage bridge readable; current Ch 4 use is unmarked first-introduction; could benefit from minor lineage-citation-bridge prose.
  - **Bibliography expansion** — Henry 1974 *AER* 64(6); Arrow & Fisher 1974 *QJE* 88(2); Howarth & Norgaard 1990 *Land Economics* 66(1); Howarth & Norgaard 1992 *AER* 82(2). Dixit-Pindyck 1994 already in framework bibliography per Insight #47 + Substitutability Function lineage.
- **Pre-publication external review (Insight #39):** economics PhD with real-options-theory specialization (Dixit-Pindyck tradition) + intergenerational-equity specialization (Brown Weiss + Howarth-Norgaard tradition) verifies framework-specialization is correctly characterized + Tier B classification appropriate. Downstream gate.
- **Dependencies / Links:** [Group 1.2 rigor pass `tools/rigor-passes/commons_bonds_rigor_pass_2026-04-30_group1_2_intergenerational_option_value_v1.0.0.md`]; [Holistic strategy §10 §5.1 origin]; Insight #32 (cluster items-not-flagged batch rigor; threshold-policy precedent + usage-frequency-not-rigor-argument corollary); Insights #35 + #38 (cross-political-tradition robustness discipline; Tech Appendix §L methodological footnote pattern); Insight #56 (Group 1.1 sibling Group 1 audit); Insight #58 (Group 1.3 sibling Group 1 audit); Insight #39 (pre-publication external review; downstream gate); Henry 1974 *AER*; Arrow-Fisher 1974 *QJE*; Dixit-Pindyck 1994 (already in framework bibliography); Howarth-Norgaard 1990 *Land Economics*; Howarth-Norgaard 1992 *AER*; Brown Weiss 1989 (intergenerational equity foundation; already in bibliography).

---

### Insight #58 — Group 1.3 intergenerational claims + intergenerational obligations Hohfeldian-dual — CLOSED-RATIFIED 2026-04-30

- **Raised:** 2026-04-29 by holistic strategy §10 §4.8 [⚠ RIGOR-SURFACED CONCERN] — possible redundancy: "intergenerational claims" and "intergenerational obligations" both Tier A vocabulary (Rawls + Parfit + Gosseries-Meyer political-philosophy lineage). Question: does framework deploy claims as distinct concept from obligations across chapters?
- **Status:** **closed-ratified 2026-04-30 (Chris Winn) — verdict (α) Keep both as deliberate Hohfeldian-dual** per `tools/rigor-passes/commons_bonds_rigor_pass_2026-04-30_group1_3_intergenerational_claims_v1.0.0.md`. Full-depth rigor test on three options (α keep both; β drop claims; γ replace claims with "future-generation entitlements"). Decisive criterion: chapter-prose audit confirms framework deploys both deliberately as Hohfeld 1913 jural-correlative framework — *obligation* in ethical-philosophy contexts; *claim* in quantification/instrument contexts.
- **Category:** vocabulary · framework-discipline · Tier A pattern · Hohfeldian jural-correlative · cross-political-tradition robustness
- **Content:** **No vocabulary changes ratified.** Documentation-only verdict: framework's existing usage of "intergenerational obligations" + "intergenerational claims" is preserved as deliberate Hohfeldian-dual. Both terms Tier A (established academic vocabulary; vocabulary-footprint cost +0). 12-cell multi-audience matrix on dual usage: 2 STRONGEST (Tier 2b legal/policy + Tier 2c intergenerational ethics — native register for Hohfeldian dual) + 10 STRONG + 0 weaker; cleanest matrix of three options.
- **Decisive criterion:** Chapter-prose audit confirmed deliberate dual usage:
  - **Obligation** = duty-side; ethical-philosophy register: Ch 5:205 *"intergenerational obligation embedded in the Social Security trust-fund accounting"*; Ch 6:670 *"established moral-philosophy vocabulary for intergenerational status, rather than treating intergenerational obligation as something the reader is asked to accept on faith"*.
  - **Claim** = entitlement-side; quantification/instrument register: Ch 4:95 *"how does a society capture an intergenerational claim and deploy it across generations"*; Ch 6:805 *"the cost is a scarcity-grounded intergenerational claim and belongs in the integrand"*; Ch 9:125 *"captured the crisis's cost as an intergenerational claim and distributed the cost across multiple constituencies"*; terms_index:957 *"foreclosure cost is the full intergenerational claim"*.

  Ch 6 uses BOTH in same chapter (line 670 obligation; line 805 claim) for different argumentative registers — definitive evidence of deliberate dual usage.
- **Hohfeldian framework:** Hohfeld 1913 *"Some Fundamental Legal Conceptions as Applied in Judicial Reasoning"* establishes the foundational right/duty + claim/obligation jural-correlative framework. Right/Claim (entitlement-side) and Duty/Obligation are jural correlatives; framework's parallel usage matches.
- **Tier-ladder analysis:** Both terms Tier A (established academic-literature terms per cluster pass §10.2). No tier-ladder differentiation needed; keep both.
- **Cross-political-tradition robustness:** STRONG across all four reading-positions (claim-rights central to classical-liberal; civic-republican claim-making tradition; class-claim register central to socialist/communitarian; reparations-claims + indigenous-land-claims register central to lived-oppression). Both terms work across all four; dual usage is robust.
- **M11 critic-survival:** SURVIVES all 5 probes (stylistic-variation; academic-literature-distinction; argument-precision; vocabulary-footprint; single-term-coverage).
- **Implementation applied 2026-04-30:** documentation-only. No chapter sweep; current usage preserved.
- **Implementation pending Phase 3 v2.0.0 rebuild:**
  - **Hohfeld 1913 bibliography addition** — *"Some Fundamental Legal Conceptions as Applied in Judicial Reasoning."* *Yale Law Journal* 23(1): 16-59. Foundational legal-philosophy reference; verify whether already in framework bibliography; add if not.
  - **Optional: Vocabulary strategy v1.0.1 §10 worked-example addition** — Hohfeldian-dual discipline as worked example #9 (deferred per recommendation; could fit naturally in vocabulary strategy worked-examples section).
- **Pre-publication external review (Insight #39):** legal-philosophy / political-philosophy reviewer (Hohfeld + Rawls + Parfit tradition) verifies framework's claim/obligation usage aligns with established jural-correlative framework. Downstream gate.
- **Dependencies / Links:** [Group 1.3 rigor pass `tools/rigor-passes/commons_bonds_rigor_pass_2026-04-30_group1_3_intergenerational_claims_v1.0.0.md`]; [Holistic strategy §10 §4.8 origin]; Insight #32 (Tier A pattern + cluster vocabulary §10.2); Insights #56 (Group 1.1) + Group 1.2 [PROPOSED] (sibling Group 1 audits); Insight #39 (pre-publication external review; downstream gate); Hohfeld 1913 *Yale Law Journal* (foundational legal-philosophy; bibliography addition pending Phase 3); Rawls 1971 *A Theory of Justice* (savings principle + intergenerational obligation); Parfit 1984 *Reasons and Persons* (intergenerational ethics); Gosseries-Meyer 2009 *Intergenerational Justice* (duty/entitlement dual canonical work); Brown Weiss 1989 *In Fairness to Future Generations*; Howarth-Norgaard 1990; Darity-Mullen 2020 (claim-side reparations economics); Coulthard 2014 + Tuck-Yang 2012 + Whyte (claim-side as native vocabulary in this tradition).

---

### Insight #56 — Group 1.1 Dynastic Labor Cost → Lineage Labor Cost rename — CLOSED-RATIFIED 2026-04-30

- **Raised:** 2026-04-29 by holistic strategy §10 full re-rigor §6.1 [⚠ RIGOR-SURFACED CONCERN] — class-connotation mismatch: "Dynastic" connotes ruling-class / wealth-class lineage; framework usage was for working-class extraction-affected family cascade. Multi-audience matrix: WEAK-RISK on lived-oppression cell; ADEQUATE-WEAK on Tier 2d + socialist/communitarian. Author direction 2026-04-30: *"Run a full depth rigor test like we used earlier on P2#3.# if 'Lineage Labor Cost' or 'Intergenerational Labor Cost' or some other variant scores better. Let's definitely not use Dynastic Labor Cost."*
- **Status:** **closed-ratified 2026-04-30 (Chris Winn) — verdict (a) Full ratify (β) Lineage Labor Cost** per `tools/rigor-passes/commons_bonds_rigor_pass_2026-04-30_group1_1_labor_cost_naming_v1.0.0.md`. Full-depth rigor test parallel to Phase 2 #3.# theorem audits on 7 candidate names (Lineage; Intergenerational; Generational; Family; Family-Lineage; Heritage; Descendant). Lineage Labor Cost dominates 12-cell multi-audience matrix (2 STRONGEST + 10 STRONG + 0 weaker; only candidate with zero ADEQUATE-or-weaker cells); STRONGEST on lived-oppression cell where Dynastic Labor Cost was WEAK-RISK.
- **Category:** vocabulary · framework-discipline · Cᵢ-class naming · class-connotation cleanup · cross-political-tradition robustness
- **Content:** Rename Dynastic Labor Cost → **Lineage Labor Cost** across publisher-facing artifacts + scaffolding. Tier B classification (close-fit academic term + framework-specialization footnote). Lineage citation discipline spans 5 traditions: family-economics (Becker 1981); decolonial/indigenous (Coulthard 2014; Tuck-Yang 2012; Whyte); primitive-accumulation (Federici 2004); race+housing economics (Mian-Sufi 2014; Rothstein 2017; Taylor 2019; Coates 2014); reparations economics (Darity-Mullen 2020); Appalachian community studies (Caudill 1962; Bell 2009).
- **Decisive criterion:** "Lineage" carries multi-tradition lineage hooks where "Dynastic" carries primarily ruling-class/wealth-class connotation. Cross-political-tradition matrix: Lineage STRONG/STRONGEST across all four reading-positions; Dynastic ADEQUATE-WEAK on socialist/communitarian + WEAK-RISK on lived-oppression. Per author direction 2026-04-29 pass/fail-gate framing, lived-oppression WEAK-RISK is exactly the type of finding that drives rename. Bridge to Ch 1:145 prose ("What was taken from your lineage by the displacement") creates **natural alignment** with renamed term — Ch 1:145 already used "your lineage" framing; Lineage Labor Cost matches.
- **Implementation applied 2026-04-30:**
  1. Chapter sweep — 7 instances renamed across Ch 1 GuidanceDoc (lines 119, 128, 145), Ch 6 (line 817 lowercase), Ch 8 (lines 91, 93, 159).
  2. Research case-study sweep — 4 instances renamed across `research/case-studies/healthcare-end-of-life.md` (line 75; "Tier 3 (Dynastic Labor)" + "dynastic cost" derivative), `research/case-studies/opioid-extraction-appalachia.md` (line 52; "Tier 3 (Dynastic Labor)" + "dynastic-labor cost" derivative), `research/case-studies/indigenous-land-dispossession.md` (line 115), `research/case-studies/social-security.md` (line 50; line 5 archived-quote preserved per WP#4).
  3. terms_index Cᵢ illustrative-list updates — lines 125 (historical 8-tier list with rename note); 424 + 433 + 453 (active Cᵢ examples lists) — all updated to "Lineage Labor Cost."
  4. tools/commons_bonds_book_scope_v1_0_3.md line 61 — vocabulary glossary entry updated with rename note.
  5. Vocabulary strategy v1.0.1 §6.1 suffix-convention example table — updated.
  6. Routine 1 daily sentinel pattern #8a added — "Dynastic Labor Cost" / "Dynastic Labor" / "dynastic labor cost" / "dynastic-labor cost" all flagged as retired-vocabulary regression with remediation hint.
- **Tier-ladder:** Tier B (academic-anchored + framework-specialization footnote). Tier A FAILS strict-fit (composition novel); Tier C demotion not viable (load-bearing chapter handle); Tier D over-coining (Tier B suffices given lineage anchors).
- **M11 critic-survival:** SURVIVES all 5 probes (family-economics traditionalist; reparations-economics critic; decolonial scholar; Marxist; academic-economics-publisher).
- **Cross-political-tradition robustness:** STRONGEST on lived-oppression (central vocabulary — Coulthard ancestral kinship; Whyte indigenous lineage; Federici reproductive-labor lineage; Mian-Sufi race+wealth lineage); STRONG on classical-liberal + civic-republican + socialist/communitarian.
- **Pre-publication external review (Insight #39):** economics PhD with family-economics specialization (Becker tradition) + race-economics specialization (Darity-Mullen tradition) + decolonial-scholarship reviewer (Coulthard tradition) verifies the rename is non-appropriating + correctly characterized. Downstream gate.
- **Implementation pending (Phase 3 v2.0.0 rebuild scope):**
  - Glossary v3 → v4 rebuild — Lineage Labor Cost dedicated entry derived from terms_index per S1 schema.
  - Tech Appendix v2.0.0 rebuild — Lineage Labor Cost lineage-citation footnote per Tier B framework-specialization discipline (Becker 1981 + Coulthard 2014 + Federici 2004 + Mian-Sufi 2014 + Darity-Mullen 2020 anchors).
- **Dependencies / Links:** [Group 1.1 rigor pass `tools/rigor-passes/commons_bonds_rigor_pass_2026-04-30_group1_1_labor_cost_naming_v1.0.0.md`]; [Holistic strategy §10 §6.1 origin]; Insights #35 + #38 (cross-political-tradition lineage discipline established; multi-tradition citation pattern); Insight #34 (Group 2 Knowledge and Cultural Cost — parallel cross-political-tradition robustness verdict); Vocabulary strategy v1.0.1 §3 + §8 (Tier-ladder + cross-political-tradition robustness check); Insight #39 (pre-publication external review; downstream gate); Becker 1981 *A Treatise on the Family*; Coulthard 2014 *Red Skin, White Masks*; Tuck & Yang 2012 "Decolonization is not a metaphor"; Federici 2004 *Caliban and the Witch*; Patel & Moore 2017 *A History of the World in Seven Cheap Things*; Hickel 2020 *Less Is More*; Mian-Sufi 2014 *House of Debt*; Rothstein 2017 *The Color of Law*; Taylor 2019 *Race for Profit*; Coates 2014 "The Case for Reparations"; Darity-Mullen 2020 *From Here to Equality*; Caudill 1962 *Night Comes to the Cumberlands*; Bell 2009 *Our Roots Run Deep as Ironweed*.

---

### Insight #55 — Framework-wide notation collision audit (one-time retroactive sweep) — CLOSED-RATIFIED 2026-04-30

- **Raised:** 2026-04-29 by Insight #42 Phase 2 E.3 audit + parallel-session integration §17. The S → τ collision (E.3 scarcity threshold colliding with E.4 substitutability function and Insight #33 S_max) was caught only because the cross-theorem viewing angle surfaced it; single-theorem audits would not have flagged it. Other collisions almost certainly exist that haven't been surfaced. Author direction 2026-04-29: implement four-layer notation discipline (Routine 1 prospective + Routine 2 retrospective + this Insight one-time retroactive + Vocabulary strategy v1.0.1 standing-discipline preventive).
- **Status:** **closed-ratified 2026-04-30 (Chris Winn) — verdict (a) Full ratify: apply all remediations + ledger additions** per `tools/rigor-passes/commons_bonds_rigor_pass_2026-04-30_phase2_insight55_notation_collision_audit_v1.0.0.md`. Audit produced 7 findings: 3 HIGH-severity collisions (α irreversibility-vs-curvature; τ integration-variable-vs-scarcity-threshold; C cost-variable-vs-commons-territory-set); 3 MEDIUM-severity reserved-letter ledger additions (β, σ, ρ); 1 LOW-severity informational (section-namespace overlap). Hypothesis confirmed: cross-document audit surfaces collisions single-theorem audits miss.
- **Remediations ratified:**
  - 3 HIGH-severity renames queued for **Phase 3 Tech Appendix v2.0.0 rebuild**: (1) α → ξ for Insight #42 E.3 cost-function curvature parameter (preserves α for §M scarcity-multiplier irreversibility parameter; smaller blast radius); (2) τ → u for integration variable at line 6720 (preserves τ for global scarcity-threshold reservation; standard math dummy convention); (3) C → 𝒞 (script C) for commons-territory set at line 398 (set-vs-variable typography disambiguation per standard math convention).
  - 3 MEDIUM-severity reserved-letter ledger additions applied 2026-04-30 to Vocabulary strategy v1.0.1 §13.2: β (risk-posture calibrator), σ (scarcity parameter), ρ (commons regeneration rate). Plus S_threshold subscript (substitutability critical value) added to subscript ledger.
  - Vocabulary strategy v1.0.1 §13.2.1 added (section-namespace overlap informational note) + §13.2.2 added (set-valued objects use script/calligraphic typography discipline).
  - Routine 1 daily sentinel pattern #10 reserved-letter ledger updated 2026-04-30 with all codified letters.
- **Category:** notation-discipline · academic-rigor · cross-document-sweep · pre-publication
- **Content:** Comprehensive sweep of all variable letters/symbols + abbreviations across the framework's apparatus to identify undisclosed notation collisions. Scope:
  - **Documents in scope:** Tech Appendix v1.0.0 HTML (all sections); terms_index.md (all entries); manuscript/chapters/Chapter_*Draft.{md,html} (all 10 chapters); core/glossary/commons_bonds_updated_glossary_v3.html.
  - **Categories to check:**
    1. **Single-letter overloads** — A; B; C; D; E; P; Q; R; S; U; plus Greek letters α; β; γ; δ; ε; η; θ; λ; μ; ν; π; ρ; σ; τ; φ; ψ; ω. For each, identify all distinct semantic uses across the document set.
    2. **Multi-letter abbreviations** — RCV; CIT; CSD; ARR; IPG; CS; AIT (retired); FGC (retired); ESG (retired). For each, identify all distinct semantic uses.
    3. **Subscript patterns** — B₁; B₂; Cᵢ; S_max; t₀; r_∞. For each, verify subscript-context discipline.
    4. **Greek-letter conventions** — verify any Greek letter introduced (α curvature; β coefficient; λ exponential parameter; τ scarcity threshold; etc.) is consistent across uses.
  - **Reserved-letter ledger (per Routine 1 pattern #10; codified in Vocabulary strategy v1.0.1 §13):**
    - **S, S(t)** — substitutability function (Tech Appendix §B Definition A.2)
    - **S_max** — substitutability function limit (Insight #33)
    - **τ (tau)** — scarcity threshold per Insight #42
    - **B, B₁, B₂** — Accountability Bond + sub-instruments
    - **C, Cᵢ** — cost / i-th cost component
    - **CS** — Cost Severance
    - **D, D(t, t₀)** — discount factor
    - **E, E(R, t)** — externality tail (function); also Theorem labels E.1–E.5
    - **R** — resource
    - **Q, Q(t)** — quality-stock per Insight #52
    - **U, U(R, t, Q(t))** — utility
    - **A** — abundance (Theorem E.3)
    - **r(s), r_∞** — discount rate (per Insight #40)
    - **α** — scarcity-multiplier exponent / cost-function curvature
    - **λ** — substitutability exponential parameter (per Insight #40)
- **Already-identified collisions (cross-reference pre-existing Insight resolutions):**
  - **Insight #42** (Phase 2 E.3) — S = scarcity threshold collision with S(t) = substitutability function and S_max. **RESOLVED**: rename S → τ in E.3 + CIT Definition A.8 reframing.
  - **Insight #50** (Phase 2 #4 RCV acronym collision) — RCV vs adjacent-field meanings (radio common variable; recreational vehicle; ranked-choice voting). **RESOLVED** via Phase 2 audit.
  - **Insight #52** (Phase 2 #8 RCV integrand Q(t) notation-clarity) — Q(t) convention divergence (framework's Q-as-quality-stock vs Hotelling 1931 q-as-extraction-flow vs Pindyck 1978 X(t)-for-stock vs Dasgupta-Heal 1979 S(t)-for-stock vs Mussa-Rosen 1978 Q-as-quality-index). **RESOLVED** via §B Definition A.3 expansion.
- **Output of audit:**
  - Collision report — per category (single-letter; multi-letter; subscript; Greek), list each collision found with file:line examples + severity (HIGH / MEDIUM / LOW).
  - Rename recommendations — for each collision, recommend which use stays vs which gets renamed; rationale + cross-reference to existing resolutions.
  - Cross-political-tradition robustness check — for new Greek letter or symbol choices, verify the choice doesn't collide with academic conventions in adjacent fields (resource economics; intergenerational ethics; commodity economics; tipping-point ecology).
- **Implementation venue:** feeds into Phase 3 Tech Appendix v2.0.0 rebuild (where most collision repairs will land). Some collisions may require chapter-prose updates (handled at Insight #36 Ch 1 + Ch 3 conversational drafting session OR as part of pre-submission editorial review).
- **Cadence relationship to routines:**
  - **Routine 1** (daily sentinel) — prospective; catches new collisions as introduced. Already extended per this Insight (pattern #9 + #10).
  - **Routine 2** (weekly pre-submission audit) — retrospective; comprehensive sweep against reserved-letter ledger. Already extended per this Insight (check #5 inserted between truncated-paragraphs and chapter-length-tracking).
  - **This Insight (one-time retroactive)** — covers the gap routines won't catch automatically; surfaces the *currently-existing* collisions before Phase 3 v2.0.0 rebuild.
  - **Vocabulary strategy v1.0.1 §13** — preventive standing discipline; guides new vocabulary decisions to avoid future collisions.
- **Pre-publication external review (per Insight #39):** notation-discipline reviewer (mathematical-economics formal-methods specialist) verifies collision audit is exhaustive + reserved-letter ledger is correct + recommended renames are non-disruptive to academic-economics readers. Downstream gate.
- **Implementation pending:**
  - **Execute the sweep** — comprehensive cross-document scan per categories above; estimated scope ~400-600 lines (rigor pass document) + collision-report findings.
  - **Update Vocabulary strategy v1.0.1 §13** with reserved-letter ledger codified (parallel to §6 suffix-convention discipline). Already drafted in this commit.
  - **Phase 3 Tech Appendix v2.0.0 rebuild scope** — incorporate all collision-resolution renames + reserved-letter ledger as discipline.
- **Dependencies / Links:** Insight #42 (Phase 2 E.3 — origin of NOTATION COLLISION finding); Insight #50 (Phase 2 RCV acronym collision); Insight #52 (Phase 2 RCV integrand Q(t) convention divergence); Insight #33 (existential substitutability gap rename — established S_max notation); Insight #40 (Theorem E.4 — established S(t) notation); Insight #39 (pre-publication external review; downstream gate); Routine 1 (`tools/routines/proposed_routines_v1.0.0.md` — extended with notation-collision patterns #9 + #10); Routine 2 (same file — extended with notation-collision sweep check #5); Vocabulary strategy v1.0.1 §13 (this commit — codifies reserved-letter ledger as standing discipline); Phase 3 Tech Appendix v2.0.0 rebuild (downstream implementation venue).

---

## §3. Closed insights

*(Empty. Insights move here when `closed-ratified` or `closed-rejected`.)*

---

## §4. Operating discipline

### §4.1 When to log an insight

Log any observation that meets at least one of:
- Surfaces a framework-structure concern (inconsistency, missing piece, category confusion).
- Identifies a vocabulary concern (too many terms, ambiguous term, stale term, coupling issue).
- Notes a method concern (current approach may be suboptimal, untested assumption, missing test).
- Raises a craft concern (register mismatch, prose-specification divergence, reader-accessibility issue).
- Spots a cross-cutting consistency issue between docs / chapters / decisions.
- Identifies an option-space gap (the current question should probably include options X and Y that weren't proposed).

Do not log:
- Single-file typos or minor wording fixes (handle inline).
- Questions already being actively worked (they're in the current todo).
- Insights entirely captured by existing rigor-pass output (reference the pass instead of duplicating).

### §4.2 Capture format

Follow §1 template. Keep content actionable — *what would it take to resolve this?* should have a concrete answer even if the answer is "run a rigor pass."

### §4.3 Todo-list interaction

Every open insight has exactly one todo item linked to it. Todo content: `Review Open Insight #N: <short title>`. When the insight moves to `addressed`, the todo can split into specific execution tasks. When the insight closes, the todo closes with it.

### §4.4 Session-handoff interaction

Session handoffs reference this file's current state — specifically, open insights that may need attention in the next session. A dedicated handoff section (standing) names any insights whose todos are not yet worked and highlights any that have time-sensitive triggers.

### §4.5 When the author raises an insight

Same discipline applies — log it here, link a todo, work to resolution. The file is a two-way capture, not just a me-raises-things mechanism.

---

*End of Open Insights Log v1.0.0. Established 2026-04-24. Active insights tracked in §2; closed insights archived in §3. Operating discipline per §4.*
