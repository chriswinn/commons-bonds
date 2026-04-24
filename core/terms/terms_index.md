# Commons Bonds — Term Provenance Index

**Version:** 0.1.0 (skeleton, established 2026-04-24)
**Purpose:** registry of framework vocabulary with full provenance — rigor support, dependency tracking, staleness triggers, versioning — replacing prior "canonical" claims that masked the testing-dependent nature of every term.

---

## §0. Why this index exists

The framework's prior vocabulary discipline used words like *canonical*, *locked*, and *final* to mark terms as settled. Those claims hid the fact that every framework term rests on specific testing-suite decisions that can and do change when the suite finds issues with upstream or downstream elements.

Today's three rigor passes demonstrated the stakes:

- **Path F rigor pass (2026-04-24)** reframed the 10 abundances from "canonical taxonomy" to "variables AIT has discovered." A word previously used as a truth-claim ("canonical") became inaccurate.
- **Tier-reframing rigor pass (2026-04-24)** exposed the v10 tier schema as a mis-labeled variable list. The "Canonical v10" label it carried was not reflecting reality — the schema failed under its own weight on a duplication check.
- **Macro-grouping rigor pass (2026-04-24)** would have produced an attractive but harmful "canonical macro-category" layer if the rigor had not caught the abstraction-hides-severance concern.

A system that called any of these "canonical" at the time would have masked the dependencies that later testing exposed. The Term Provenance Index replaces truth-claim language with traceable-reasoning discipline: every term carries the rigor that supports it, the decisions it depends on, and the triggers that would require re-testing.

## §1. How to read a record

Each term has a Provenance Record with the following fields:

### Template

```markdown
### <Term>

**Working definition:** <current definition — no claim of finality>

**Status:** <CURRENT | PENDING-RIGOR | UNDER-REVIEW | SUPERSEDED | RETIRED>

**Term-spec version:** v<N.M>

**Last reviewed:** <YYYY-MM-DD>

**Rigor provenance:**
- <Rigor pass filename / version / §ref / date / commit> — <what that pass established about this term>
- <Additional rigor passes, session handoffs, or ratified decisions>

**Depends on (framework decisions this term rests on):**
- <Decision 1> — <brief description>
- <Decision 2>

**Staleness triggers (what would require re-review):**
- <Upstream change 1>
- <Upstream change 2>

**Commit trail:** <most relevant commit refs>

**Supersedes / superseded by:** <if applicable>

**Notes:** <optional — any caveats, pending questions, or edge cases>
```

### Status indicators

| Status | Meaning |
|---|---|
| `CURRENT` | In active use; has passed applicable rigor; no known staleness. |
| `PENDING-RIGOR` | Introduced but not yet rigor-tested; use at own risk until pass runs. |
| `UNDER-REVIEW` | Rigor pass in progress; term may be revised or retired when pass ratifies. |
| `SUPERSEDED` | Replaced by newer term; preserved for historical reference with pointer to replacement. |
| `RETIRED` | Dropped without replacement (e.g., dissolved concepts). |

**Critical property:** no status claims truth. `CURRENT` means "this survives our most recent applicable rigor." It does not mean "this is correct." Framework decisions are always downstream of rigor testing, which is always subject to new pressure.

### Staleness detection

Each record lists *dependencies* and *staleness triggers* explicitly. When an upstream framework decision changes (tracked by rigor-pass commit or handoff ratification), records whose dependencies reference the changed decision are flipped to `UNDER-REVIEW` and queued for re-testing. The discipline: every rigor-pass ratification ends with a terms-index impact assessment — which records flip to `UNDER-REVIEW`, which are confirmed still `CURRENT`.

### Versioning

Each term carries its own `term-spec version` independent of document versions. When a term's definition or status changes materially (rigor re-test flips verdict, supersession, retirement), the term-spec bumps (v1.0 → v2.0). When re-confirmed with minor clarification, patch bumps (v1.0 → v1.1). Readers can spot stale terms at a glance: if a term's provenance lists v3.0 as the current spec but a chapter draft reflects v1.0 vocabulary, the staleness is visible.

## §2. Integration with other framework docs

- **Glossary (`core/glossary/commons_bonds_updated_glossary_v2.html`)** is updated to short gloss entries that reference their full record in this index. Glossary becomes the user-facing lookup; this index is the provenance source-of-truth.
- **Rigor passes** produce provenance records as their primary deliverable. When a pass ratifies, it updates affected records in this index.
- **Session handoffs** reference this index's current state rather than repeating "canonical" summaries.
- **README** canonical-state table links to relevant provenance records.
- **Today's three rigor passes** (Path F, tier-reframing, macro-grouping) get a `§ Subsequent developments` section appended with dated annotations as downstream decisions affect them. Their bodies remain historical record per the live-vs-archive policy ratified 2026-04-24.

## §3. Provenance records

*This section populates as rigor passes produce records. Initially empty; fills as the Tier A extreme-rigor work lands on each framework term and each glossary term.*

### Pending records (awaiting rigor-pass completion)

**Terminology decisions (4):**
- Variable vs Cost (atomic unit of measurement)
- Dimension vs Abundance (class term for the 10)
- Dimensional Consistency vs Units Consistency (Gate L.2 name)
- Closed-count "10 abundances" vs generative framing

**Core framework terms (6):**
- Commons Bonds
- Cost Severance
- Value Capture
- Severed Cost
- Spatial Cost Severance
- Temporal Cost Severance

**Methodology terms (4):**
- Abundance Inversion Test (AIT)
- Abundance Masking
- Abundance Dimension
- Universality Test

**Mathematical and measurement terms (9):**
- Full Generational Cost (FGC)
- Residual Commons Value (RCV)
- Accountability Bond (B)
- Foreclosure Cost
- Externality Tail
- Substitutability Function
- Intergenerational Pricing Gap (IPG)
- Civilizational Substitutability Gap (CSG)
- Asymmetric Regret Principle

**Tier entries (8, being dissolved per 2026-04-24 tier-reframing ratification):**
- Lifetime Survival Cost
- Actuarial Risk Cost
- Mission Failure Reserve
- Dynastic Labor Cost
- Community Transition Reserve
- Ecological Carrying Cost
- Knowledge and Culture Cost
- Political Capture Cost

**Records populated in §4 (2026-04-24):**

*Retirement / demotion records (4):*
- Spatial Cost Severance — `RETIRED` (misnamed; abundance-cost not severance).
- Temporal Cost Severance — `RETIRED` (replaced by lowercase prose phrase).
- Cost Bearing — `SUPERSEDED` (demoted from glossary to prose-only).
- Value Capture — `RETIRED` (duplicative with Value Extraction).

*CURRENT records — active Ring-1 terms (6):*
- Cost Severance — `CURRENT` Ring 1 (mechanism; 227 uses).
- Severed Cost — `CURRENT` Ring 1 (result + flagship adoption phrase; 37 uses; success-criterion target).
- Value Extraction — `CURRENT` Ring 1 (causal event; promoted from Ring 2; 16 proper-noun + 42 concept-level uses; supersedes Value Capture).
- Abundance Inversion Test (AIT) — `CURRENT` Ring 1 (methodology + Gate L.1; 505 uses).
- Residual Commons Value (RCV) — `CURRENT` Ring 1 (quantification-anchor + equation component; 729 uses — framework's MOST-used term).
- intergenerational cost severance (lowercase prose phrase) — `CURRENT` (adopted as standard book descriptor for the intergenerational subtype of Cost Severance).

**Ring-1 synthesis batch — FULLY RATIFIED 2026-04-24:**
- Value Extraction: Option B ratified ✓
- Cost Severance + Severed Cost: Option A (keep both) ratified ✓
- AIT: Option A (keep current) ratified ✓
- RCV: Option A (keep current) ratified ✓
- Cost (Cᵢ): Option B (from earlier Variable-vs-Cost pass) — still pending individual ratification
- Commons Bonds: still pending rigor pass (Open Insight #4)

**Ring 1 now has 5 of 7 terms with populated records + 1 ratified-elsewhere + 1 pending rigor pass.**

---

## §4. Established records

*(Records below are populated as rigor passes land. Each record's body summarizes the pass's verdict; full pass documents live at `tools/rigor-passes/`.)*

---

### Cost Severance

**Working definition:** the structural mechanism by which extraction separates value capture from cost bearing. The process/mechanism noun that names the framework's core phenomenon. Middle position in the framework's causal chain: *Value Extraction → Cost Severance → Severed Cost.*

**Status:** `CURRENT` at Ring 1 (ratified 2026-04-24 by Chris Winn, Ring-1 synthesis batch).

**Term-spec version:** v1.0 (first sanctioned spec after CS-vs-SC triage).

**Last reviewed:** 2026-04-24

**Rigor provenance:**
- Variable-addability rigor pass (2026-04-24) — CORE mechanism preserved under Path F generalization.
- Tier-reframing + macro-grouping passes (2026-04-24) — mechanism preserved under all ratified framework changes.
- CS-vs-SC triage rigor pass `tools/rigor-passes/commons_bonds_rigor_pass_2026-04-24_term_cost_severance_vs_severed_cost_v1.0.0.md` (2026-04-24) §17 — Option A (keep both Cost Severance + Severed Cost with role discipline) PASSES extreme rigor.
- Ring-1 synthesis pass (2026-04-24) — verdict reinforced; CS = RCV − B equation integration verified.

**Role discipline:** Cost Severance is the *process/mechanism noun*. Use when naming the mechanism, describing how the phenomenon operates, or in theoretical discussion. *"McDowell suffers cost severance."* *"Cost severance operates through..."* Lexical slot: subject of analytical sentences about mechanism operation. Companion term: Severed Cost for result/quantity naming (see separate record).

**Usage audit:** 227 occurrences in 36 files as of 2026-04-24 — framework's most-used mechanism term.

**Depends on:**
- Value Extraction (causal event that triggers the mechanism — Ring 1)
- Severed Cost (result-side companion — Ring 1)
- RCV (quantification that measures the mechanism's output — Ring 1)
- CS = RCV − B equation (Cost Severance appears as "CS" in the equation)
- AIT (methodology for identifying costs within the mechanism's scope)

**Staleness triggers:**
- Framework CORE math redefines the CS = RCV − B relation.
- Academic adoption evidence shows "cost severance" failing to travel.
- Role-discipline slippage where prose blurs CS (mechanism) with SC (result).

**Commit trail:**
- CS-vs-SC rigor pass: commit `0021e24` (2026-04-24).
- Ring-1 synthesis: commit `2b70377` (2026-04-24).
- Ratification + Ring-1 record: this commit.

**Supersedes / superseded by:** N/A — retained under triage.

**Notes:**
- Pair with Severed Cost is grammatical complementarity (process noun vs result noun), NOT duplication. Standard economics convention (externality vs externality cost; rent-seeking vs rent).
- Style-discipline per CS-vs-SC rigor pass: use Cost Severance when naming the mechanism; use Severed Cost when quantifying specific instances.

---

### Severed Cost

**Working definition:** a specific cost that has been severed — value extracted by capturer while the cost remains at the source (community, ecosystem, future generation). The result/quantity noun naming the quantified outcome of the Cost Severance mechanism. **Flagship adoption target** for the framework's success criterion ("severed cost" used by labor lawyer in brief).

**Status:** `CURRENT` at Ring 1 (ratified 2026-04-24 by Chris Winn, Ring-1 synthesis batch).

**Term-spec version:** v1.0 (first sanctioned spec after CS-vs-SC triage).

**Last reviewed:** 2026-04-24

**Rigor provenance:**
- Same implicit rigor as Cost Severance — Severed Cost is the flagship adoption phrase tested across every rigor pass since Path F.
- CS-vs-SC triage rigor pass (2026-04-24) §17 — Option A ratified; Severed Cost retained as flagship adoption target alongside Cost Severance mechanism name.
- Ring-1 synthesis (2026-04-24) — role discipline reinforced.

**Role discipline:** Severed Cost is the *result/quantity noun* + *flagship adoption phrase*. Use when quantifying a specific instance, writing legal/policy-register prose, or using the framework's adoption-target vocabulary. *"McDowell bears a severed cost of $550/ton."* *"The severed cost shows up in community collapse."* Lexical slot: object or quantified predicate in accounting sentences. Companion: Cost Severance for mechanism naming.

**Usage audit:** 37 occurrences in 12 files as of 2026-04-24 — less framework-internal usage than Cost Severance, but higher adoption potential (shorter, quantifiable, legal-register).

**Success criterion:** THE framework's target for adoption. *"If, ten-plus years from now, a labor lawyer uses 'severed cost' in a brief or in open court and the judge does not need it explained — the book has succeeded."*

**Depends on:**
- Cost Severance (mechanism-side companion — Ring 1)
- CS = RCV − B equation (Severed Cost is the quantified CS in specific instances)
- Value Extraction (causal event upstream)
- RCV − B computation (mathematical basis)

**Staleness triggers:**
- Success criterion shifts away from "severed cost" adoption target.
- Legal/policy adoption evidence after publication shows different phrase traveling instead.
- Mechanism-name changes (Cost Severance) would force SC revisit.

**Commit trail:**
- CS-vs-SC rigor pass: commit `0021e24` (2026-04-24).
- Ring-1 synthesis: commit `2b70377` (2026-04-24).
- Ratification + Ring-1 record: this commit.

**Supersedes / superseded by:** N/A — retained under triage.

**Notes:**
- Flagship adoption phrase. When the book's rhetorical strategy is honest accounting, Severed Cost is the term that travels into legal briefs, policy memos, and journalism. Retirement or replacement would directly sabotage the success criterion.
- Style-discipline per CS-vs-SC rigor pass (and applies symmetrically with Cost Severance).

---

### Abundance Inversion Test (AIT)

**Working definition:** the framework's epistemic methodology for determining whether a candidate cost is scarcity-grounded (and therefore admissible to RCV computation). Procedure: invert the scarcity-condition underlying the cost to its abundance counterpart; if the cost vanishes under the counterfactual, it's scarcity-grounded and admits. Gate L.1 of the four-gate discipline. Chris's original methodology coinage. Short form "Abundance Test" acceptable in informal prose contexts.

**Status:** `CURRENT` at Ring 1 (ratified 2026-04-24 by Chris Winn, Ring-1 synthesis batch).

**Term-spec version:** v1.0 (first sanctioned spec after rigor-pass verification).

**Last reviewed:** 2026-04-24

**Rigor provenance:**
- Variable-addability rigor pass (2026-04-24) — AIT confirmed as CORE epistemic methodology.
- Path F rigor pass (2026-04-24) — AIT's role as admission-method for Cᵢ confirmed.
- Tier-reframing + macro-grouping passes (2026-04-24) — AIT role unchanged.
- AIT rigor pass `tools/rigor-passes/commons_bonds_rigor_pass_2026-04-24_term_ait_v1.0.0.md` (2026-04-24) §17 — Option A PASSES unconditionally. 505 embedded uses (439 acronym + 50 full-form + 16 short-form) across 30 files. Name-mechanism match exact. Vocabulary-coherence with abundance-architecture preserved.
- Ring-1 synthesis (2026-04-24) — AIT's position coherent with other Ring-1 terms.

**Role:** methodology/test-name + Gate L.1 (first of the four gates) + epistemology-anchor. Not a public-adoption target (not a brief phrase); academic-citation target.

**Short form:** "Abundance Test" acceptable in informal prose contexts (16 existing uses). Full form "Abundance Inversion Test" in formal/first-use contexts. Acronym "AIT" in technical/dense-reference contexts.

**Usage audit (2026-04-24):** 505 total uses across 30 files — framework-internal workhorse.

**Depends on:**
- Abundances (the 10 organizational scaffolding — AIT operates on abundance-conditions)
- Four Gates structure (AIT is Gate L.1)
- Cost (Cᵢ) (AIT admits Cᵢ to the integrand)
- RCV (AIT-admitted Cᵢ integrates into RCV)
- Framework CORE math

**Staleness triggers:**
- Framework's abundance vocabulary restructured in a way that misaligns "abundance inversion."
- Published peer review identifies academic citation ambiguity.
- Alternative methodology name surfaces with compelling rigor verdict (unlikely given passage of standalone rigor pass).

**Commit trail:**
- AIT rigor pass: commit `9abb263` (2026-04-24).
- Ring-1 synthesis: commit `2b70377` (2026-04-24).
- Ratification + Ring-1 record: this commit.

**Supersedes / superseded by:** N/A.

**Notes:**
- Name-mechanism match (Principle #3) is exact: "Abundance Inversion Test" literally describes what the test does (inverts to abundance counterfactually and tests whether the cost vanishes).
- Rename candidates (Scarcity-Grounding Test, Scarcity Test, Abundance Test primary, drop acronym) each failed rigor.
- Academic citation anchor: readers cite the framework's methodology as "AIT (Winn, Commons Bonds)."

---

### Residual Commons Value (RCV)

**Working definition:** the framework's central quantification — the true intergenerational cost of extraction that remains unpriced by conventional accounting (market prices + accountability bonds + existing externality instruments). Computed as the integral of the sum of admitted cost terms (Cᵢ) against a declining discount factor over infinite horizon:

RCV(R, t₀, Context) = ∫ₜ₀^∞ { Σᵢ Cᵢ(R, t, Context) } · D(t, t₀) dt

One side of the flagship equation CS = RCV − B, where CS is cost severance and B is the accountability bond.

**Status:** `CURRENT` at Ring 1 (ratified 2026-04-24 by Chris Winn, Ring-1 synthesis batch).

**Term-spec version:** v1.0 (first sanctioned spec after rigor-pass verification).

**Last reviewed:** 2026-04-24

**Rigor provenance:**
- Variable-addability rigor pass (2026-04-24) — RCV confirmed as CORE quantification; variable-addability generalization preserves RCV form.
- Path F rigor pass (2026-04-24) — RCV's role under the four-gate discipline confirmed.
- Tier-reframing + macro-grouping passes (2026-04-24) — RCV unchanged.
- RCV rigor pass `tools/rigor-passes/commons_bonds_rigor_pass_2026-04-24_term_rcv_v1.0.0.md` (2026-04-24) §17 — Option A PASSES unconditionally. 729 total uses (658 acronym + 71 full-form) across 34 files — framework's MOST-used term. Name-quantity match exact per word (Residual / Commons / Value each does load-bearing semantic work).
- Ring-1 synthesis (2026-04-24) — RCV's equation-anchor role reinforced.

**Role:** quantification-anchor + equation-component (CS = RCV − B) + academic-citation target.

**Semantic work per word:**
- *Residual* — what remains unpriced after conventional accounting
- *Commons* — the shared pools bearing the cost (communities, ecosystems, future generations)
- *Value* — dollar-denominated quantity

Removing any word creates ambiguity or unmoors the term.

**Usage audit (2026-04-24):** 729 total uses across 34 files — **framework's most-used term.**

**Depends on:**
- Cost Severance (RCV is one side of CS = RCV − B)
- Severed Cost (SC is the result of CS = RCV − B computation)
- Accountability Bond (B) (RCV pairs with B in the equation)
- AIT (AIT admits Cᵢ that RCV integrates)
- Four gates (filter Cᵢ admissible to RCV)
- Value Extraction (causal event upstream)
- Framework CORE math

**Staleness triggers:**
- CS = RCV − B equation redefined.
- Conventional accounting scope changes in a way that redefines "residual" reference.
- Academic adoption evidence shows RCV failing to travel as citation anchor.

**Commit trail:**
- RCV rigor pass: commit `5dea091` (2026-04-24).
- Ring-1 synthesis: commit `2b70377` (2026-04-24).
- Ratification + Ring-1 record: this commit.

**Supersedes / superseded by:** N/A.

**Notes:**
- Each word of "Residual Commons Value" is load-bearing per §3.1 of the RCV rigor pass.
- Rename candidates (True Intergenerational Cost, Commons Value, drop acronym, different root) each failed rigor on precision, equation integration, academic citation, or existing-usage continuity.
- The acronym's 658 framework-internal uses represent the framework's most durable citation infrastructure.
- Integration discipline: "RCV" as technical acronym; "Residual Commons Value" in first-use + formal contexts.

---

### Value Extraction

**Working definition:** the act by which value is separated from its source (a community, ecosystem, or future generation) and taken by a value-capturer. The causal event that produces Cost Severance — extraction severs cost from the capturer (who benefits) and leaves it with the source (who bears). Chris's original coinage, serving as an accessible-language reframing of David Harvey's "accumulation by dispossession." First position in the framework's causal chain: *Value Extraction → Cost Severance → Severed Cost.*

**Status:** `CURRENT` at Ring 1 (ratified 2026-04-24 by Chris Winn, promoted from Ring 2).

**Term-spec version:** v1.0 (first sanctioned spec after triage vs Value Capture).

**Last reviewed:** 2026-04-24

**Rigor provenance:**
- Full rigor pass `tools/rigor-passes/commons_bonds_rigor_pass_2026-04-24_term_value_capture_vs_extraction_v1.0.0.md` (2026-04-24) — Option B PASSES extreme rigor. Wins on decisive causal-chain bridge test + register alignment with book's extraction-economy critique + Harvey lineage + legal-register adoption + Berggruen fit + concept-level audit (extract-derivatives already dominate framework prose 42 refs).
- Cross-pairing synthesis `tools/rigor-passes/commons_bonds_rigor_pass_2026-04-24_synthesis_ring1_terms_v1.0.0.md` (2026-04-24) — Value Extraction verdict REINFORCED by synthesis: extraction's separation-from-source semantics pairs natively with Cost Severance's severance-from-capturer semantics. The chain flows.
- Vocabulary-footprint meta-pass §13.2.c (2026-04-24) — initial Ring-2 classification; corrected audit + author ratification promoted to Ring 1.

**Decisive test from rigor pass (causal-chain bridge):**
- *Value Extraction → Cost Severance → Severed Cost* reads as tight causal sequence because extraction IS the severance mechanism (the act of separating value from source is the same act that severs cost from the capturer).
- *Value Capture → Cost Severance → Severed Cost* required reader inference (capture is acquisition, not separation). Rejected.

**Harvey lineage:** Value Extraction is Chris's original-coinage accessible reframing of David Harvey's "accumulation by dispossession." The essay/book can cite Harvey in the setup (*"what I call value extraction — echoing David Harvey's accumulation by dispossession but more plainly named"*) preserving academic credibility + establishing originality as reframing-for-accessibility.

**Depends on:**
- Cost Severance (Ring 1; the mechanism that Value Extraction causes)
- Severed Cost (Ring 1; the result downstream of the chain)
- Abundance framework (the abundances that Value Extraction operates against — producing scarcity-grounded costs that AIT admits)
- Principle #3 (variant-mechanism-match discipline; Value Extraction passes)

**Staleness triggers:**
- Cost Severance concept redefined in a way that changes the causal-chain relationship.
- Published peer review identifies legal-register ambiguity with regulatory-capture or extraction-industry usage.
- Adoption evidence shows "value extraction" failing to travel in legal/policy/Berggruen contexts.

**Commit trail:**
- Full rigor pass: commit `daef46a` (2026-04-24).
- Cross-pairing synthesis: commit `2b70377` (2026-04-24).
- Ratification + Ring-1 promotion: this commit.

**Supersedes:** Value Capture (retired as duplicative per author 2026-04-24 admission that the two were interchangeable). Previous interchangeable-usage convention retired.

**Notes:**
- **Style discipline:** capitalized "Value Extraction" when naming the framework term; lowercase "value extraction" in prose when describing the act in context.
- First position in causal chain; Berggruen essay-critical per author direction 2026-04-24 ("that causal chain not landing means I lose the reader, reviewer, editor, et al at the very beginning").
- Phase A3 sweep target: 16 Value Capture proper-noun refs across 9 files → Value Extraction.
- Principle #4 (active-use traceability): chapter drafts using Value Extraction will gain provenance-pointer headers pointing to this Terms Index record during Phase A3 sweep.

---

### Value Capture

**Working definition (prior):** causal-event term used interchangeably with Value Extraction to describe the act of an extractor capturing/obtaining value from a source.

**Status:** `RETIRED` (ratified 2026-04-24 by Chris Winn as duplicative with Value Extraction).

**Term-spec version:** v1.0 final (retirement).

**Last reviewed:** 2026-04-24

**Rigor provenance:**
- Same as Value Extraction above — the pair was tested head-to-head in the Value-Capture-vs-Extraction rigor pass (2026-04-24, commit `daef46a`). Verdict: Option B (Value Extraction) passes on every decisive axis; Value Capture retires as duplicative.
- Author's own admission (2026-04-24): the two terms were interchangeable in meaning; triage picks one.

**Rationale for retirement (not demotion):**
- Value Capture was a duplicate of Value Extraction in meaning, not a distinct concept. Triage selects; doesn't preserve both.
- Rigor-pass decisive tests (causal-chain bridge, register alignment, Harvey lineage, concept-level audit, critic pressure) all preferred Value Extraction.
- Retaining Value Capture would carry redundant vocabulary footprint competing with Value Extraction — works against the success-criterion single-term adoption bet.

**Depends on (why the term was in the vocabulary):**
- Author's original dual coinage (Value Capture / Value Extraction as interchangeable accessible reframings of accumulation-by-dispossession).
- Glossary v2 carried both as glossary entries.
- Pre-rigor-pass loose naming discipline admitted duplicative entries.

**Staleness triggers (what would cause retirement revisit):**
- Academic or legal discourse separately adopts "value capture" as a framework-technical term with meaning distinct from "value extraction."
- Regulatory-capture collision-avoidance motivation emerges that argues for reinstating Value Capture as distinct term.
- (Neither expected.)

**Commit trail:**
- Triage rigor pass: commit `daef46a` (2026-04-24).
- Ratification + RETIRE: this commit.

**Supersedes / superseded by:** superseded by Value Extraction as the sole causal-event term.

**Notes:**
- Different retirement basis from Spatial Cost Severance (Principle-#3 misnaming) and Temporal Cost Severance (adjective-precision + framework-usage-evidence). Value Capture retires as DUPLICATE of a co-existing-and-preferred term.
- Phase A3 sweep targets: 16 proper-noun Value Capture references across 9 files rewritten to Value Extraction; glossary v2 Value Capture entry removed in v3.

---

### intergenerational cost severance (lowercase prose phrase)

**Working definition:** the intergenerational subtype of Cost Severance — value captured now, costs borne by future generations. Used as a lowercase descriptive phrase composing the framework's existing "intergenerational" adjective (109 framework uses) and "cost severance" Ring-1 term (227 framework uses). Not a capitalized proper-noun compound.

**Status:** `CURRENT` as lowercase prose phrase (ratified 2026-04-24 by Chris Winn). Replaces the retired capitalized "Temporal Cost Severance" term.

**Term-spec version:** v1.0 (first sanctioned spec).

**Last reviewed:** 2026-04-24

**Rigor provenance:**
- Focused rigor pass `tools/rigor-passes/commons_bonds_rigor_pass_2026-04-24_term_intergenerational_cost_severance_v1.0.0.md` (2026-04-24) — Option A PASSES UNCONDITIONALLY. Wins on every module with meaningful signal.
- Companion pass (same date): Temporal Cost Severance retirement — the paired move that retires the capitalized term in favor of this lowercase phrase.
- Audit finding: framework's natural language already composes "intergenerational" + "cost severance" ~109 + 227 times; this ratification formalizes consistency of the existing pattern.
- Principle-#3 variant-subtype check: PASSED (intergenerational IS a genuine subtype of Cost Severance).

**Lowercase discipline is LOAD-BEARING:**
- Capitalizing the phrase as a proper-noun compound would reintroduce the jargon-inflation problem that sank "Temporal Cost Severance."
- The phrase is the composition of two existing framework concepts (one abstract, one Ring-1); it does not warrant proper-noun status on its own.
- Style-guide discipline (per Conditions 3 of the rigor pass): use lowercase always; do not capitalize even at sentence start where possible (restructure sentence if needed).

**Academic connections:**
- Intergenerational equity (Weiss, Brown-Weiss)
- Intergenerational justice (Rawls, Parfit)
- Intergenerational ethics (Broome, Stern, Nordhaus)
- Intergenerational mobility (Chetty, Piketty)
- The phrase slots cleanly into these established discourses.

**Depends on:**
- Cost Severance (Ring 1 parent concept)
- "intergenerational" adjective (framework's existing heavy usage)
- Principle-#3 variant-subtype discipline (passed — genuine subtype, not misnaming)
- Lowercase discipline (prevents jargon inflation)

**Staleness triggers:**
- Cost Severance concept redefined in a way that changes the subtype-mapping.
- Phrase drifts into capitalized usage — triggers lowercase-discipline re-test.
- Published peer review identifies systematic ambiguity in compositional use.

**Commit trail:**
- Focused rigor pass: commit `1be07e0` (2026-04-24).
- Companion Temporal Cost Severance retirement ratification: commit `4435488` (2026-04-24).
- This adoption ratification: this commit.

**Supersedes:** implicit composition-only usage (0 prior exact-phrase occurrences; now formalized as the book's standard descriptor). Supersedes "Temporal Cost Severance" capitalized term as the replacement-phrase of choice.

**Notes:**
- This phrase is NOT a technical term like Cost Severance, RCV, or AIT. It is a descriptive compound used consistently per style-guide discipline.
- Completes the Option-C outcome from the Temporal-Cost-Severance rigor pass. Both passes together ratified 2026-04-24: retire "Temporal Cost Severance"; adopt "intergenerational cost severance" in prose.
- Phase A3 sweep targets: glossary v3 sub-entry under Cost Severance (~5 min); Ch 6 integration at Approach 3 (~10 min); Ch 6 guidance doc style-note (~5 min).

---

### Cost Bearing

**Working definition (prior, as glossary v2 entry):** descriptive term for the role a party plays when carrying cost severance (the cost-bearing community, ecosystem, or future generation).

**Status:** `SUPERSEDED` — demoted from glossary entry to prose-only usage. The concept persists in prose (*"the cost-bearer,"* *"the community bears,"* *"future generations bear the cost"*) but is not a framework-technical term.

**Term-spec version:** v1.0 final (demotion)

**Last reviewed:** 2026-04-24

**Rigor provenance:**
- Vocabulary-footprint meta-pass §13.2.c (2026-04-24, commit `46600bc`) — initial analysis as Ring-3 candidate (demote from glossary).
- Chapter-draft audit 2026-04-24 (per Principle #2 concept-level methodology, commit `af2f18e`): 46 concept-level references across 17 files.
- Author 2026-04-24 guidance: *"Cost Bearing is someone bearing the cost of cost severance, so perhaps prose vs. glossary."*
- Ratified 2026-04-24 by Chris Winn: DEMOTE from glossary; retain in prose.

**Rationale for demotion (not retirement):**
- Cost Bearing describes a ROLE (someone is bearing cost), not a framework-specific mechanism or event. Role-description doesn't need technical vocabulary.
- Contrast with Value Capture / Value Extraction (also a concept around the capture event): Value Extraction describes a discrete EVENT the framework prices; Cost Bearing describes the receiving-end position. The event earns framework-term status (Ring 1); the role is prose-level.
- Chapter-draft usage (46 refs) is already descriptive-register; no sweep required.

**Depends on:**
- Cost Severance (Cost Bearing is the receiving-end role of the Cost Severance mechanism).
- Severed Cost (Cost Bearing is what a party does with respect to Severed Cost).
- Both parent concepts preserve the Cost Bearing concept in prose automatically.

**Staleness triggers:**
- Framework redefines the cost-bearer role in a way that warrants a dedicated technical term (unlikely).
- Academic or legal discourse adopts "cost-bearer" as a technical-legal term (possible in employment / workers-rights law; would warrant revisit).

**Commit trail:**
- Meta-pass analysis: commit `46600bc` (2026-04-24).
- Audit correction: commit `af2f18e` (2026-04-24).
- Ratification + DEMOTE: this commit.

**Supersedes / superseded by:** N/A — concept persists in prose; only glossary-entry form superseded.

**Notes:**
- Phase A3 sweep target: glossary v2 Cost Bearing entry removed in v3 bump. Chapter-draft usage stays as-is (46 existing refs are descriptive prose).
- Principle #4 (active-use traceability): since Cost Bearing is prose-descriptive (not a framework term), no provenance-pointer needed in chapter drafts. This record is the audit trail.

---

### Temporal Cost Severance

**Working definition (prior):** a variant of Cost Severance naming the intergenerational dimension — value captured now; costs borne by future generations.

**Status:** `RETIRED` (ratified 2026-04-24 by Chris Winn)

**Term-spec version:** v1.0 final (retirement)

**Last reviewed:** 2026-04-24

**Rigor provenance:**
- Focused rigor pass `tools/rigor-passes/commons_bonds_rigor_pass_2026-04-24_term_temporal_cost_severance_v1.0.0.md` (2026-04-24) — Option C (retire capitalized term) recommended on adjective-choice + framework-usage-evidence grounds.
- Audit finding: framework uses "intergenerational" 109× across 27 files vs 6× usage of "Temporal Cost Severance" proper-noun — 18× preference for intergenerational.
- Principle-#3 variant-subtype check: PASSED (intergenerational IS a genuine subtype of Cost Severance — removing the generational gap eliminates this form of severance).
- Companion rigor pass on the replacement phrase: `commons_bonds_rigor_pass_2026-04-24_term_intergenerational_cost_severance_v1.0.0.md` (2026-04-24) — Option A (adopt "intergenerational cost severance" lowercase prose phrase) PASSES unconditionally.

**Depends on (why the term was in the vocabulary):**
- Glossary v2 carried this as a Cost Severance variant alongside Spatial Cost Severance.
- Loose variant-naming discipline (pre-Principle-#3) that admitted the variant without verifying adjective strength or framework-usage alignment.

**Staleness triggers (what would cause retirement revisit):**
- The Cost Severance concept redefined in a way that changes the subtype-mapping.
- Academic or policy usage patterns shift toward "temporal" over "intergenerational" for this subtype.
- (Neither expected; retirement stands.)

**Commit trail:**
- Focused rigor pass: commit `9df1958` (2026-04-24).
- Intergenerational cost severance rigor pass: commit `1be07e0` (2026-04-24).
- Ratification + RETIRE: this commit.

**Supersedes / superseded by:** replaced by lowercase prose phrase "intergenerational cost severance" (per `commons_bonds_rigor_pass_2026-04-24_term_intergenerational_cost_severance_v1.0.0.md` Option A ratification).

**Notes:**
- Different retirement basis from Spatial Cost Severance (which failed Principle #3 on misnaming grounds). Temporal Cost Severance PASSED Principle #3 (genuine subtype) but retired on adjective-precision + framework-usage-evidence grounds.
- Phase A3 sweep targets: 5 proper-noun references (Ch 2, Social Security case, Deepwater case) → rewrite as lowercase "intergenerational cost severance"; 1 glossary v2 entry → remove in v3 bump.

---

### Spatial Cost Severance

**Working definition (prior):** a variant of Cost Severance operating across spatial distance — extractors separated from affected communities by geography.

**Status:** `RETIRED` (ratified 2026-04-24 by Chris Winn)

**Term-spec version:** v1.0 final (retirement)

**Last reviewed:** 2026-04-24

**Rigor provenance:**
- Vocabulary-footprint meta-rigor pass §13.2.c (2026-04-24) — initial RETIRE/DEMOTE analysis based on 0 chapter refs.
- Author 2026-04-24: *"Spatial Cost Severance is probably misnamed, as that was just Cost Severance that happened only if and when distance between locations vanished. So that isn't really cost severance but really an abundance cost that vanishes or appears e.g. miner can teleport instantly to/from an asteroid for work each day = totally removes a lot of the cost severance of living on an asteroid."* — identified the misnaming at the phenomenon level; RETIRE (not DEMOTE) ratified.
- Principle-#3-candidate check (variant-subtype verification): FAILED — the phenomenon was abundance-cost mechanics mis-absorbed into the Cost Severance concept. Retirement corrects the misnaming.

**Depends on (why this term was in the vocabulary):**
- Glossary v2 carried this as a named Cost Severance variant alongside Temporal Cost Severance.
- Loose variant-naming discipline that didn't verify the variant's subtype status against the Cost Severance definition.

**Staleness triggers (what would cause this retirement to be revisited):**
- A new phenomenon surfacing that is genuinely spatial-severance (not abundance-cost) and requires a dedicated term.
- (Unlikely — the abundance-cost mechanics the old term was describing are fully captured by the Spatial abundance + Cᵢ framework.)

**Commit trail:**
- Meta-pass initial RETIRE/DEMOTE analysis: commit `46600bc` (2026-04-24).
- Author ratification + RETIRE (not DEMOTE): commit pending (this update).

**Supersedes / superseded by:** N/A — retired without replacement. Phenomenon captured by Spatial abundance + associated Cᵢ (framework already in place).

**Notes:**
- This is the first entry in §4. Serves as template format for future RETIRED-status records.
- The RETIRE verdict is on Principle-#3 grounds (variant-subtype check failed), not vocabulary-footprint grounds. A distinct decision class from terms retired via footprint pruning (e.g., FGC under tier dissolution).
- Sweep targets when Phase A3 lands: glossary v2 entry removal; any residual chapter/case-study references to "Spatial Cost Severance" proper-noun (audit confirmed 0 chapter refs; only glossary-level entry to retire).

---

*End of Term Provenance Index v0.1.0. Skeleton established 2026-04-24. Populated progressively as Tier A rigor work produces records.*
