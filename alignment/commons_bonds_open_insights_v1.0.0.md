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

### Insight #9 — Framework as decision-time severance-detection tool (not just ex-post analysis)

- **Raised:** 2026-04-24 by Chris Winn (via the commute-story conversation) + me (naming the pattern)
- **Status:** raised
- **Category:** framework-structure · book-scope · application-domain
- **Content:** The book's framing to date has centered on *ex-post* cost-severance analysis — pricing what McDowell County bore after extraction, what Deepwater Horizon left behind, what Libby lost to asbestos. But the commute-story conversation surfaced a distinct and arguably more practically-useful application: **the framework as a decision-time tool.** At the moment a decision is being made (signing an apartment lease, accepting a job, consenting to a medical treatment, purchasing a house, pivoting careers), informal AIT + informal RCV can surface costs the decision-maker would otherwise miss. Chris's commute story demonstrated this: *"the quick mental what would a day in the life of living here and getting to/from my office be like/entail"* is informal AIT (testing whether the cost is scarcity-grounded in time) + informal RCV (mentally multiplying hours × days × year). The framework doesn't need math-fluent readers to be useful at decision-time; it needs readers who know the two-step (test for scarcity-grounding → compute informal cost over the affected horizon).
- **Why it matters:** (a) expands the book's practical reach substantially — most readers encounter cost severance from the OTHER side of the transaction (as consumers, employees, residents) more often than from the extractor side. Decision-time tooling is the application most readers can use. (b) Reinforces the "no villain" structural argument — the commute-story apartment manager wasn't the adversary; the information architecture was. Decision-time tooling is what closes the information gap. (c) Potentially addresses a Ch 8 or Ch 10 scope question — where does the applications discussion live? (d) Affects the framework's contribution-claim — the book offers not just a theory but a usable instrument.
- **Proposed resolution:** Decide whether to:
  - (a) Foreground decision-time application in a dedicated chapter or appendix ("How to Apply the Framework Before Signing") with worked examples for employment, medical, housing, major-life decisions.
  - (b) Thread decision-time application through multiple chapters (Ch 8 picks it up during the walkthrough; Ch 10 gestures at it reflectively; no dedicated section).
  - (c) Keep the focus on ex-post analysis; mention decision-time application briefly without making it structural.
  - (d) Something else that surfaces during further exploration.
- **Dependencies / Links:**
  - Personal Stories Candidate #1 (commute trade) carries the opening example for decision-time application; story is captured + tagged with framework connections.
  - May require its own rigor pass if (a) is ratified — decision-time framework application as a chapter/appendix-level scope addition.
  - Related to candidate Working Principle: "When the author's intent is knowable, ask before recommending" — informal framework application requires the reader to know what they're deciding about; formal AIT + RCV requires data the reader may not have. Different usability tiers.
- **Todo link:** "Review Open Insight #9: framework as decision-time tool — book-scope decision."

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

### Insight #14 — Norway's sovereign wealth fund as canonical intergenerational-CS mitigation exemplar + epistemic-humility discipline for B

- **Raised:** 2026-04-24 by Chris Winn (during Accountability Bond scope-creep clarification): *"I think the commonwealth fund of Norway is the most impressive mitigation solution I have found to address intergenerational cost severance yet it obviously can't exist in societies where a government is allowed to plunder accounts of people currently living and accounts of people not yet born so the Norway solution isn't a perfect solution."*
- **Status:** raised · load-bearing for Book 1 authorial-voice calibration around Accountability Bond + Ch 4 Norway treatment
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
- **Proposed resolution:** capture in Accountability Bond rigor pass §7.3 + Terms Index Accountability Bond record (done 2026-04-24 with this commit). Apply during chapter drafting as authorial-voice calibration. No further decision needed; this is discipline not option-selection.
- **Dependencies / Links:** Accountability Bond rigor pass (Terms Index record); Open Insight #13 (book-scope creep); v1.0.3 book-scope doc; Norway case-study file; Ch 4 guidance; Ostrom-successor bibliography entries (Hess & Ostrom 2007 Knowledge Commons; Ostrom 1990 Governing the Commons — North 1990 institutional-economics).
- **Todo link:** "Review Open Insight #14: authorial-voice discipline during chapter drafting (Ch 4 Norway treatment; Ch 5 accountability-gap framing; Ch 6/9/10 remediation discussion)."

---

### Insight #13 — Book-scope creep monitoring (Book 1 vs Book 2 vs Book 3 boundary per `tools/commons_bonds_book_scope_v1_0_3.md`)

- **Raised:** 2026-04-24 by Chris Winn (during Accountability Bond ratification: *"flag to see if it starts to cause book scope creep, creep towards things that are perhaps best left for book 2, book 3, etc. for scope of book and reasons for separating books"*). Refined 2026-04-24 after Chris corrected an initial oversimplified "Book 1 = diagnosis; Book 2/3 = fix" framing — *"The above said, I can accept the... Review the book 1 vs. book 2 vs. book 3 publication strategy documents and reasons. That is the guiding book scope, not my earlier over simplified sentence."* Governing document: `tools/commons_bonds_book_scope_v1_0_3.md` (2026-04-21 proposed canonical).
- **Status:** raised · ongoing monitoring discipline (cross-cutting across framework; not a per-term decision)
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
- **Dependencies / Links:** v1.44.0 session handoff (Phase B item: Tech Appendix v0.0.5 HTML integration of supplement §2-§7); commit `351817c` (2026-04-25 partial integration block); supplement file (`core/technical-appendix/TechnicalAppendix_v0.0.5_supplement.md`); Block 4 validation work (`core/technical-appendix/block4_validation_2026-04-25.md`); Method 3 sensitivity analysis (`core/technical-appendix/method3_sensitivity_analysis_2026-04-25.md`); empirical sourcing pass (`core/technical-appendix/empirical_sourcing_pass_2026-04-25.md`); Ch 6 supplementary drafts §6.5–§6.10 (Phase B authoring passages with Tech Appendix companions); current Ch 6 HTML draft.
- **Todo link:** "Schedule dedicated session for Tech Appendix v0.0.5 + Ch 6 full HTML rewrite in Option A pretty-printed semantic HTML (Insight #21)."

---

### Insight #22 — Chapter titles fall within chapter-by-chapter prose-sweep scope

- **Raised:** 2026-04-27 by Chris Winn during Ch 9 holistic review
- **Status:** raised · pending memory-rule clarification + verification sweep across remaining chapter titles
- **Category:** sweep-discipline · craft · framework consistency
- **Content:** During Ch 9 holistic review, the author surfaced the diagnosis that the original chapter title "The Renewable Imperative" was likely a carry-over from before the Book 1 / Book 2 split (per `tools/commons_bonds_book_scope_v1_0_3.md` v1.0.3 §6.1). The chapter's substantive content had been disciplined into Book 1 scope through prior sweeps (explicit "framework, not blueprint" framing; "framework's role here is structural observation, not advocacy" framing in tax-tradeoff section; "this is not a legislative blueprint. It is a framework" closing). But the title itself had not been swept for Book-1/Book-2-split-carry-over. The full-depth Round 1+2+3 chapter-title rigor pass (`tools/rigor-passes/commons_bonds_rigor_pass_2026-04-27_ch9_title_candidates_v1.0.0.md`) confirmed the diagnosis was rigor-grounded — the original title failed simultaneously on M3.4 + M6 + M8 + M9 + M10 + M11 + §22.4 modules. Author ratified replacement title "Pricing Honestly" 2026-04-27.
- **Why it matters:** the chapter-by-chapter prose-sweep discipline memory rule (per `feedback_always_expand_rule.md`) names "every prose element in every chapter (not just newly-drafted AUTHOR ZONE passages)" as in-scope, with three rigor questions. **Chapter titles are prose elements.** They should fall in the same sweep that catches terminology regressions, vocabulary mismatches, applied-advocacy-vs-framework-establishment register drift, and Book-1/Book-2-split carry-overs. Without explicit memorialization, future sweeps may miss title-level concerns the way the Ch 9 sweep nearly missed "Renewable Imperative." The Ch 7 title swap from "The Colony Administrator" to "On Other Worlds" was caught under separate vocabulary-sweep discipline; the Ch 9 title swap was caught only because the author flagged the political-charge concern. The discipline gap is real and worth closing.
- **What would resolve this:** memory-rule clarification adding chapter titles to the chapter-by-chapter sweep scope, OR formal capture as Working Principle, OR addition to the protocol document. The clarification should specify: (a) chapter titles are prose elements; (b) sweeps should check title for Book-1/Book-2-split carry-over, applied-advocacy register drift, and vocabulary regressions; (c) title rigor passes follow the same protocol as Ch 7 and Ch 9 title rigor passes (full 14-module evaluation when carry-over or register concern surfaces).
- **Verification sweep recommended:** the remaining Book 1 chapters with titles already in the set (Ch 2 "The Miner"; Ch 4 "The Existence Proof"; Ch 5 "The Accountability Gap"; Ch 6 "Three Ways of Counting"; Ch 8 "What Things Actually Cost"; Ch 10 "Common Bonds") have already passed informal sweep per the Ch 9 set-rigor analysis (none carry obvious carry-over concerns). Ch 1 + Ch 3 are not yet drafted; their titles should be rigor-tested when they land. The set-level rigor analysis (Ch 9 title rigor pass §10) may be worth memorializing as a once-per-major-revision check.
- **Dependencies / Links:** `feedback_always_expand_rule.md` (memory rule on chapter-by-chapter sweep discipline); Ch 7 title rigor pass (`commons_bonds_rigor_pass_2026-04-26_ch7_title_candidates_v1.0.0.md`); Ch 9 title rigor pass (`commons_bonds_rigor_pass_2026-04-27_ch9_title_candidates_v1.0.0.md`); v1.0.3 §6.1 book-scope governance; `tools/commons_bonds_rigor_protocol_v2.2.0.md`.
- **Todo link:** "Review Open Insight #22: chapter-titles-in-sweep-scope memory-rule clarification + remaining-chapters verification sweep."

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
