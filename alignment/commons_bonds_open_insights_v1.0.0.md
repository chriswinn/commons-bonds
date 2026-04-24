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
- **Status:** addressed (tiered-ring architecture ratified 2026-04-24; Ring-3 dispositions + reshaped-queue adoption still pending ratification)
- **Category:** vocabulary · meta
- **Content:** The framework currently carries ~20+ named terms: cost severance, severed cost, value capture, cost bearing, RCV, CS, AIT, IPG, CSG, FGC, foreclosure cost, externality tail, substitutability function, accountability bond, the ten abundances, the four gates, context, dimensions, abundances, variable/cost, and more. Each named concept competes for reader adoption bandwidth. The success criterion (labor lawyer uses "severed cost" in a brief) favors sharpness + concision; proliferation works against that.
- **Why it matters:** If the framework's adoption-durability is limited by vocabulary bandwidth, running 31 individual term rigor-passes is lower-leverage than running one meta-pass that tests the whole vocabulary for redundancy, load-bearing-ness, retirement candidates, and merger opportunities. A ~20-pass queue after the meta-pass beats a 31-pass queue without it.
- **Proposed resolution:** Vocabulary-footprint meta-rigor pass (M1 + M4 + M5 + M6 + M11 at depth, plus §22.4 alignment) that tests the whole vocabulary as a system. Output reshapes the remaining pass queue.
- **Dependencies / Links:** `tools/rigor-passes/commons_bonds_rigor_pass_2026-04-24_vocabulary_footprint_meta_v1.0.0.md` (2026-04-24, commit 46600bc). §13.1 tiered-ring architecture APPROVED 2026-04-24; §13.2 Ring-3 dispositions and §13.3 reshaped-queue adoption still pending.
- **Todo link:** "Await author ratification of meta-pass §13.2 + §13.3" (current in-progress todo).

### Insight #2 — Gate names are inconsistent in convention

- **Raised:** 2026-04-24 by me
- **Status:** raised
- **Category:** vocabulary · framework-structure
- **Content:** The four gates' names follow inconsistent conventions. Gate 1 = acronym (AIT). Gate 2 = phrase (Dimensional Consistency, pending rename to Units Consistency). Gate 3 = single word (Boundedness). Gate 4 = single word (Independence). A well-designed naming cohort would pick one convention (all acronyms? all single words? all phrases?) and apply it uniformly. The drift suggests the gates were named opportunistically rather than as a cohort.
- **Why it matters:** Inconsistent naming cohorts read as unserious / under-theorized to academic audiences. It also costs prose — some gates are referred-to by acronym (AIT), others by word (Boundedness, Independence), others by phrase (Dimensional Consistency / Units Consistency). Reader must hold four naming shapes instead of one.
- **Proposed resolution:** Gate-naming-cohort rigor pass that tests whether convergence to a single convention (e.g., all single words: AIT could become "Scarcity-Grounding Gate" or similar) improves the cohort, or whether the current mix is actually optimal (each name chosen for clarity in its own right, accepting inconsistency). Include option-space breadth per author direction.
- **Dependencies / Links:** Relates to Insight #1 (vocabulary footprint) — simpler gate names reduce vocabulary load. Relates to Terminology Decision 3 (Dimensional → Units Consistency) which only addresses Gate 2.
- **Todo link:** "Review Open Insight #2: Gate-naming-cohort consistency."

### Insight #3 — "Severance" vocabulary cluster needs cluster-level internal-consistency review

- **Raised:** 2026-04-24 by me
- **Status:** raised
- **Category:** vocabulary
- **Content:** "Cost Severance" (mechanism), "Severed Cost" (result), "Spatial Cost Severance" (variant), "Temporal Cost Severance" (variant), "Value Capture" (the other half of the gap), and related cluster terms are tightly interconnected. Testing them individually in sequence may produce verdicts that are internally inconsistent — e.g., Option-B for one cluster-member may contradict Option-A for another if both are rigor-tested in isolation.
- **Why it matters:** Cluster inconsistency shows up in prose as jarring mismatches between closely-related terms. Individual rigor passes can miss this because each pass sees only one term. A cluster-level rigor pass tests the cluster as a system.
- **Proposed resolution:** Severance-cluster rigor pass that evaluates all cluster members simultaneously (M4 + M5 + M6 + M11 + §22.4). Output is a set of coordinated decisions rather than six unrelated term decisions.
- **Dependencies / Links:** May be absorbed into or supersede some individual passes in the current Tier A queue (Cost Severance, Severed Cost, Spatial Cost Severance, Temporal Cost Severance, Value Capture).
- **Todo link:** "Review Open Insight #3: Severance cluster-level rigor."

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
- **Status:** raised
- **Category:** vocabulary · craft
- **Content:** "Foreclosure Cost" appears twice in glossary v2: once under Mathematical and Measurement Terms, once as Tier 4. Under tier dissolution the duplicate resolves automatically (Tier 4 vanishes). But the fact the duplicate was there in the v2 glossary at all is a sign the glossary predates some of the framework's structural decisions.
- **Why it matters:** Low-severity, but signals that the glossary v2 → v3 bump needs more than a dimension-rename sweep; it needs a structural walk-through to catch other potential duplicates or stale entries.
- **Proposed resolution:** When glossary bumps to v3 (post-rigor-pass work), do a full structural audit pass rather than just a rename sweep. Flag any other duplicate or stale entry found.
- **Dependencies / Links:** Glossary v2 → v3 bump is on the Phase A3 wrap-up task list.
- **Todo link:** "Review Open Insight #5: Glossary structural audit during v3 bump."

### Insight #6 — Running 31 individual rigor passes may be the wrong structural approach

- **Raised:** 2026-04-24 by me
- **Status:** addressed (vocabulary-footprint meta-pass in progress)
- **Category:** method · meta
- **Content:** The initial 31-pass queue loaded after author's "full rigor on every term" ratification assumes each term is independently testable. Many terms are tightly coupled (severance cluster, gate cohort, variable-vs-cost affecting dimension-vs-abundance). Individual-pass approach reproduces each other's findings and misses cluster-level insights.
- **Why it matters:** Resource allocation. A handful of well-scoped cluster passes + a meta-pass produces more insight per unit effort than 31 isolated passes.
- **Proposed resolution:** Run vocabulary-footprint meta-pass first; it will reshape the remaining queue into cluster passes + a smaller number of individual passes for terms that genuinely stand alone.
- **Dependencies / Links:** Addresses Insight #1 structurally. Insights #2 and #3 will be partially absorbed.
- **Todo link:** vocabulary-footprint meta-pass (in todo list, in-progress).

### Insight #7 — Value Capture vs Value Extraction terminology decision

- **Raised:** 2026-04-24 by Chris Winn (pointed out Value Capture OR Value Extraction as the causal event that produces Cost Severance)
- **Status:** raised
- **Category:** vocabulary · framework-structure
- **Content:** The framework currently uses "Value Capture" (16 proper-noun refs + 42+ concept refs in chapter drafts). Author flagged that "Value Extraction" is an alternative candidate for the same causal event. Since this is the event that produces Cost Severance — the extractor captures/extracts value, leaving the "bill" of severance on the community, ecosystem, future generations — the naming choice matters. "Value Extraction" pairs naturally with "extraction economy" vocabulary; "Value Capture" is broader (applies to non-extractive contexts like financial instruments).
- **Why it matters:** This is the causal-event term in the framework's three-concept chain (Value Capture/Extraction → Cost Severance → Severed Cost). Naming it clearly matters for prose consistency and for the framework's causal-chain legibility. It's also Berggruen-essay-relevant vocabulary (likely to appear in the essay).
- **Proposed resolution:** Run a focused rigor pass on Value Capture vs Value Extraction — full option-space (Capture, Extraction, both-interchangeable, different-term-entirely) tested against the ratified modules + §22.4 alignment. Promote the resolved term to Ring 2 of the tiered-ring architecture.
- **Dependencies / Links:** Relates to Insight #3 (severance cluster internal consistency) — the causal-event term is part of the severance vocabulary cluster. May be absorbed into the severance cluster rigor pass or run standalone before it.
- **Todo link:** "Review Open Insight #7: Value Capture vs Value Extraction naming."

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
