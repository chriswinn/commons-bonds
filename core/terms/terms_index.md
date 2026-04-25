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

**Records populated in §4 (2026-04-24) — all 12 entries:**

*Retirement / demotion records (4):*
- Spatial Cost Severance — `RETIRED` (misnamed; abundance-cost not severance). **Note: re-examination rigor pass 2026-04-24 flipped recommendation to "spatial cost severance" lowercase prose phrase; pending author ratification of reversal.**
- Temporal Cost Severance — `RETIRED` (replaced by lowercase prose phrase).
- Cost Bearing — `SUPERSEDED` (demoted from glossary to prose-only).
- Value Capture — `RETIRED` (duplicative with Value Extraction).

*CURRENT Ring-1 records (7 — full Ring 1 architecture):*
- **Commons Bonds** — `CURRENT` Ring 1 (framework name + book title; polysemous; standalone rigor `be6646f` + integrated rigor `d4c4be4`).
- **Cost Severance** — `CURRENT` Ring 1 (mechanism; 227 uses; standalone rigor `0aafed7` + pair rigor `0021e24` + integrated `d4c4be4`).
- **Severed Cost** — `CURRENT` Ring 1 (result + flagship adoption phrase; 37 uses; pair rigor `0021e24` + integrated `d4c4be4`).
- **Value Extraction** — `CURRENT` Ring 1 (causal event; standalone rigor `18f5e82` + triage `daef46a` + integrated `d4c4be4`; supersedes Value Capture).
- **Abundance Inversion Test (AIT)** — `CURRENT` Ring 1 (methodology + Gate L.1; 505 uses; standalone rigor `9abb263` + integrated `d4c4be4`).
- **Residual Commons Value (RCV)** — `CURRENT` Ring 1 (quantification-anchor + equation component; 729 uses — framework's MOST-used term; standalone rigor `5dea091` + integrated `d4c4be4`).
- **Cost (Cᵢ)** — `CURRENT` Ring 1 (atomic unit; Variable-vs-Cost rigor `0c7547a` + integrated `d4c4be4`).

*Other CURRENT records:*
- intergenerational cost severance (lowercase prose phrase) — `CURRENT` (adopted as standard book descriptor for the intergenerational subtype of Cost Severance).

**Ring-1 architecture FULLY RATIFIED 2026-04-24 (all 7 terms):**
All 7 standalone rigor verdicts + cross-pairing synthesis ratified in batch 2026-04-24. Ring-1 vocabulary architecture locked.

**Pending updates (to be applied during Phase A3 sweep):**
- Spatial Cost Severance retirement reversal (pending author ratification of re-examination pass).
- Abundance Masking promotion to Ring 2 (pending author ratification of re-examination pass).
- CSG + Asymmetric Regret rigor passes + Universality Test re-examination (queued for non-Ring-1 queue run).
- Open Insight #4 → closed-ratified (Commons Bonds name rigor complete).

---

## §4. Established records

*(Records below are populated as rigor passes land. Each record's body summarizes the pass's verdict; full pass documents live at `tools/rigor-passes/`.)*

---

### Commons Bonds

**Working definition:** the framework's identifying name and the book's title. Polysemous compound naming three simultaneously-operating meanings: (1) **accountability bonds** — the formal instrument B in CS = RCV − B (reclamation bonds, performance bonds, community-transition reserves); (2) **relational bonds** — intergenerational duty, community-place attachment, labor solidarity, and other human-and-ecological bonds that cost severance breaks; (3) **structural bonds** — ecosystem interdependencies, atmospheric stability, economic interconnections that cost severance frays. All three meanings operate simultaneously in the book; contexts disambiguate.

**Status:** `CURRENT` at Ring 1 (ratified 2026-04-24 by Chris Winn, batch ratification with standalone + integrated rigor).

**Term-spec version:** v1.0 (first sanctioned spec after dedicated rigor pass).

**Last reviewed:** 2026-04-24

**Rigor provenance:**
- Commons Bonds standalone rigor pass `tools/rigor-passes/commons_bonds_rigor_pass_2026-04-24_term_commons_bonds_v1.0.0.md` (2026-04-24) §9 — Option A PASSES extreme rigor unconditionally. Polysemy confirmed as load-bearing (each of 3 meanings does framework work). 7 rename candidates tested; none improves.
- Full Ring-1 integrated rigor pass `tools/rigor-passes/commons_bonds_rigor_pass_2026-04-24_ring1_full_integrated_v1.0.0.md` (2026-04-24) §7 — Commons Bonds pairs coherently with every other Ring-1 term (21 pairings verified).
- Open Insight #4 (Commons Bonds name rigor) RESOLVED by these two passes.

**Polysemy per meaning, load-bearing verification:**
- Accountability bonds (Meaning #1): direct link to CS = RCV − B formula where B is the accountability bond.
- Relational bonds (Meaning #2): Ch 1's 120-hour-week thread, Ch 7's Mars colony bonds, Ch 10's closing reflection.
- Structural bonds (Meaning #3): ecosystem cases (Chesapeake, McDowell watersheds), atmospheric/climate stability, economic-community interdependencies.

**Role:** framework identifier + book title; umbrella under which all Ring-1 terms live.

**Depends on:** every Ring-1 term (title only name-works if the framework it names is coherent): Cost Severance + Severed Cost + Value Extraction + AIT + RCV + Cost (Cᵢ).

**Staleness triggers:**
- Framework scope changes materially (e.g., non-commons extraction becomes primary).
- One of the three meanings becomes obsolete.
- Adoption evidence after publication shows title failing to travel.

**Commit trail:**
- Standalone rigor pass: commit `be6646f` (2026-04-24).
- Full Ring-1 integrated pass: commit `d4c4be4` (2026-04-24).
- Batch ratification: this commit.

**Supersedes / superseded by:** N/A — retention. First-ever rigor pass on the name.

**Notes:**
- Subtitle choice is author's call + publisher convention; rigor-neutral. Examples discussed in standalone pass §9.1.
- Polysemy is asset, not liability. Parallel: "capital" in economics has multiple meanings (financial, human, social, political); context disambiguates; no one calls that imprecision.

---

### Cost Severance

**Working definition:** the structural mechanism by which extraction separates value capture from cost bearing. The process/mechanism noun that names the framework's core phenomenon. Middle position in the framework's causal chain: *Value Extraction → Cost Severance → Severed Cost.* **Specialization (not contradiction) of the familiar employment-severance concept** — inverted to describe the relationship between value-capturers and the commons they draw from (per M12 audit 2026-04-24 + Option C rhetorical-bridge ratification; canonical Ch 1 framing established).

**Status:** `CURRENT` at Ring 1 (Ring-1 synthesis batch ratified 2026-04-24 by Chris Winn; M12 collision audit + Option C ratified 2026-04-24 by Chris Winn).

**Term-spec version:** v1.1 (v1.0 was Ring-1 synthesis ratification; v1.1 adds M12 finding + Option C rhetorical-bridge ratification + Ch 1 canonical framing).

**Last reviewed:** 2026-04-24

**Rigor provenance:**
- Variable-addability rigor pass (2026-04-24) — CORE mechanism preserved under Path F generalization.
- Tier-reframing + macro-grouping passes (2026-04-24) — mechanism preserved under all ratified framework changes.
- CS-vs-SC triage rigor pass `tools/rigor-passes/commons_bonds_rigor_pass_2026-04-24_term_cost_severance_vs_severed_cost_v1.0.0.md` (2026-04-24) §17 — Option A (keep both Cost Severance + Severed Cost with role discipline) PASSES extreme rigor.
- Ring-1 synthesis pass (2026-04-24) — verdict reinforced; CS = RCV − B equation integration verified.
- **M12 collision rigor pass `tools/rigor-passes/commons_bonds_rigor_pass_2026-04-24_term_cost_severance_collision_v1.0.0.md` (2026-04-24)** — tested semantic collision with HR/accounting "severance costs" (IAS 37, US GAAP, Big-4 firms, corporate-law practice). Classification: lexical collision, different concept, HIGH severity for legal/accounting audience. **Option C (rhetorical bridge) ratified 2026-04-24 by Chris Winn** — the collision is converted into a Ch 1 teaching move that recruits reader's existing HR-severance schema as on-ramp ("THIS IS the same move, applied differently"). Option B (rename) tested 6 candidates including Accountability Severance as strongest; all rejected. First application of M12 as primary driver in a rigor pass; established rhetorical-bridge as Level 5 on M12 action ladder.

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
- **M12 bridge-commitment discipline (ratified 2026-04-24):** Ch 1 opening leans into HR/accounting collision as rhetorical bridge (see collision rigor pass §5 for canonical framing). Post-Ch-1 chapters use "Cost Severance" cleanly without defensive "not to be confused with..." language. Bridge does its work once; chapters trust it. If Ch 1 drafting reveals the bridge is authorially unsustainable, fallback to Option A (explicit disambiguation). Do NOT fallback to Option B (rename) unless both C and A attempts fail.
- **Canonical Ch 1 framing (recommended text):**
  > *"Corporate America knows the word 'severance.' When a company sheds workers to cut costs, we pay the severed employee — severance — and call it a cost of doing business. The word honors something: when you cut someone loose, you owe them. You sever the tie, and you pay for the severing. Cost severance works the opposite direction. When a company extracts value from a commons — a community, an ecosystem, a future generation — it sheds the COST of that value onto the source. The tie between value-capturer and cost-bearer gets severed, but the payment architecture of employment severance is absent. The cost-bearer gets stuck with the cost the value-capturer got paid to generate. So: severance we understand in employment. Cost severance is the same move, applied to the relationship between value-capturers and the commons they draw from — except the bill never comes due to the severing party. That's the problem this book is about."*

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

### Cost (Cᵢ)

**Working definition:** the framework's atomic unit of measurement — an indexed cost term admitted to the RCV integrand under the four gates of Section L. Each Cᵢ has units [$ · resource-unit⁻¹ · time-unit⁻¹], is identified through the Abundance Inversion Test (AIT) applied to a specific extraction Context, and contributes additively to RCV via the sum-of-costs form. The class of all costs is open and extensible — AIT applied to new Contexts may surface new costs the current framework does not enumerate.

**Status:** `CURRENT` at Ring 1 (ratified 2026-04-24 by Chris Winn as part of Ring-1 synthesis batch; standalone rigor via Variable-vs-Cost pass).

**Term-spec version:** v1.0 (first ratified spec; supersedes prior informal "variable" / "cost variable" / "cost term" usage).

**Last reviewed:** 2026-04-24

**Rigor provenance:**
- Variable-vs-Cost rigor pass `tools/rigor-passes/commons_bonds_rigor_pass_2026-04-24_term_variable_vs_cost_v1.0.0.md` (2026-04-24) §15 — Option B (replace "variable" with "cost") recommended. 5 options tested (A: variable / B: cost / C: hybrid / D: drop class term / E: ledger entry). Option B won on 9 of 11 modules; M1 and M7 indifferent.
- Full Ring-1 integrated rigor pass (2026-04-24) — Cost (Cᵢ) coheres with all other Ring-1 terms.

**Style discipline (inherited from D + E options as addenda):**
- *From Option D:* prefer specific named costs ("Black Lung Cost," "Community Transition Cost") to the class noun "cost" wherever prose allows. The class noun is fallback; specific names are default.
- *From Option E:* preserve bookkeeping metaphor at discourse level — framework voice is accountant's voice. "Cost" as atomic-unit name reinforces without needing more formal "ledger entry" / "accounting item" language.

**Notation:** Cᵢ (indexed by i) in formal/mathematical contexts; "cost" as class noun + specific-name (e.g., "black-lung cost") in prose contexts. "Cost term" remains admissible where math-as-term-of-sum is being explicitly invoked ("each cost term Cᵢ enters the integrand").

**Role:** atomic-unit-of-measurement across the framework's formula, gates, and accounting. Every named specific cost (Community Transition Cost, Dynastic Labor Cost, Political Capture Cost, etc.) is a Cᵢ.

**Depends on:**
- Four gates (L.1–L.4 admit Cᵢ to RCV)
- RCV formula (integrand is Σᵢ Cᵢ · D)
- AIT (identifies which Cᵢ admit — Gate L.1)
- Cost Severance (Cᵢ are what get severed)

**Staleness triggers:**
- Framework's atomic unit changes structurally (e.g., introduction of a higher-abstraction class above Cᵢ).
- Four-gate discipline materially revised.

**Commit trail:**
- Variable-vs-Cost rigor pass: commit `0c7547a` (2026-04-24).
- Ring-1 synthesis batch ratification: commit `af4b6d6` (2026-04-24).
- Integrated Ring-1 pass: commit `d4c4be4` (2026-04-24).

**Supersedes:** prior informal "variable" / "cost variable" / "cost term" usage in Path F rigor pass + Technical Appendix Sections L + M (usage continues as historical record in those docs per live-vs-archive policy).

**Notes:**
- Ambiguity with everyday "cost" in prose is managed by context-disambiguation — the same discipline economists apply to "utility" and "welfare."

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

**Working definition:** the act by which value is separated from its source (a community, ecosystem, or future generation) and taken by a value-capturer. The causal event that produces Cost Severance — extraction severs cost from the capturer (who benefits) and leaves it with the source (who bears). First position in the framework's causal chain: *Value Extraction → Cost Severance → Severed Cost.*

**Status:** `CURRENT` at Ring 1 (ratified 2026-04-24 by Chris Winn, promoted from Ring 2).

**Term-spec version:** v1.1 (Mazzucato citation addendum added 2026-04-24 after literature audit; v1.0 was first sanctioned spec after triage vs Value Capture).

**Last reviewed:** 2026-04-24

**Rigor provenance:**
- Full rigor pass `tools/rigor-passes/commons_bonds_rigor_pass_2026-04-24_term_value_capture_vs_extraction_v1.0.0.md` (2026-04-24) — Option B PASSES extreme rigor. Wins on decisive causal-chain bridge test + register alignment with book's extraction-economy critique + Harvey lineage + legal-register adoption + Berggruen fit + concept-level audit (extract-derivatives already dominate framework prose 42 refs).
- Cross-pairing synthesis `tools/rigor-passes/commons_bonds_rigor_pass_2026-04-24_synthesis_ring1_terms_v1.0.0.md` (2026-04-24) — Value Extraction verdict REINFORCED by synthesis: extraction's separation-from-source semantics pairs natively with Cost Severance's severance-from-capturer semantics. The chain flows.
- Vocabulary-footprint meta-pass §13.2.c (2026-04-24) — initial Ring-2 classification; corrected audit + author ratification promoted to Ring 1.

**Decisive test from rigor pass (causal-chain bridge):**
- *Value Extraction → Cost Severance → Severed Cost* reads as tight causal sequence because extraction IS the severance mechanism (the act of separating value from source is the same act that severs cost from the capturer).
- *Value Capture → Cost Severance → Severed Cost* required reader inference (capture is acquisition, not separation). Rejected.

**Literature positioning (added 2026-04-24 after prior-art audit):**

Mariana Mazzucato, *The Value of Everything: Making and Taking in the Global Economy* (Penguin/PublicAffairs, 2018), is the dominant established usage of the term "value extraction" in political economy. Mazzucato defines value extraction as *"activities focused on moving around existing resources and outputs, and gaining disproportionately from the ensuing trade"* — focused on rent-seeking in financial capitalism (asset managers, pharma patents, hedge funds, financial-sector extraction).

**Chris's relationship to Mazzucato's term:** Chris arrived at "value extraction" independently through his sociology-essay work as an accessible-language reframing of David Harvey's *"accumulation by dispossession"* (Harvey 2003). This was independent rediscovery of a parallel framing — not original coinage in the sense of priority in published discourse. Intellectual honesty requires acknowledging Mazzucato's prior published usage.

**The framework's extension of Mazzucato:** Where Mazzucato diagnoses value extraction as rent-seeking in financial capitalism (moving existing value without creating new), this framework operationalizes and specializes the diagnosis for physical-resource extraction — adding (a) a pricing mechanism (RCV, Severed Cost, Accountability Bond), (b) a causal chain (Value Extraction → Cost Severance → Severed Cost), (c) the Cost Severance mechanism specific to the separation of value-capturers from cost-bearers in resource extraction, (d) the Accountability Bond instrument that would price the severed costs into the extractor's ledger. The framework can be positioned as *"extending Mazzucato's value-extraction critique from financial rent-seeking into the physical-resource domain, with a specific accountability instrument."*

**Canonical citation form (recommended for Ch 1, Ch 6, Tech Appendix):**

> *"This framework extends Mariana Mazzucato's diagnosis of value extraction (Mazzucato 2018) — developed there for rent-seeking in financial capitalism — into the physical-resource domain. Where Mazzucato identifies value-extraction as activities that move existing value without creating new, this framework specifies the mechanism by which physical-resource extraction systematically separates value-capturers from cost-bearers (Cost Severance) and proposes a pricing instrument (Accountability Bond) to internalize the resulting Severed Cost. The framing echoes David Harvey's accumulation by dispossession (Harvey 2003), rendered in accessible accounting-register language."*

**Harvey lineage (preserved):** Value Extraction connects to David Harvey's *"accumulation by dispossession"* (Harvey 2003) as philosophical antecedent. Chris's usage reframes Harvey's critique in accessible accounting-register language suitable for policy / legal / non-academic audiences. Harvey's framing predates Mazzucato and is foundational for both usages.

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
- **Reconsider pass 2026-04-24 (ratified):** `tools/rigor-passes/commons_bonds_rigor_pass_2026-04-24_term_temporal_cost_severance_reconsider_v1.0.0.md` tested whether "temporal cost severance" should be adopted as a lowercase prose phrase parallel to the Spatial CS re-examination + intergenerational cost severance lowercase adoption. Verdict: Option A (KEEP RETIRED). Principle-#3 variant-subtype check FAILED for "temporal" — the qualifier describes a constitutive property of ALL cost severance (all severance has temporal offset between value-capture and cost-bearing), not a distinguishing gap-type. Spatial + intergenerational lowercase pair does NOT extend to a three-member cohort. Ratified 2026-04-24 by Chris Winn.

---

### Spatial Cost Severance / spatial cost severance

**Working definition:** the geographic subtype of Cost Severance — value extracted from an area disperses to distant consumers while costs (health, environmental, community) concentrate locally where extraction occurred. Used as **lowercase descriptive phrase** composing "spatial" modifier + Ring-1 "cost severance" term. Not capitalized as proper-noun compound (capitalized form produced jargon inflation and was retired via the earlier analysis; lowercase composition is the ratified form).

**Status:** `CURRENT` as lowercase prose phrase (ratified 2026-04-24 by Chris Winn — un-retirement via re-examination rigor pass). Supersedes earlier `RETIRED` status from 2026-04-24 which was a Principle-#2 failure (audited the wrong phenomenon).

**Term-spec version:** v1.1 (v1.0 was RETIRED status; v1.1 is CURRENT lowercase-prose-phrase after re-examination).

**Last reviewed:** 2026-04-24

**History and re-examination:**

The term was initially RETIRED 2026-04-24 (commit `2dc54aa`) on Principle-#3-candidate grounds, based on the author's asteroid-teleport articulation: *"Spatial Cost Severance is probably misnamed, as that was just Cost Severance that happened only if and when distance between locations vanished. So that isn't really cost severance but really an abundance cost that vanishes or appears e.g. miner can teleport instantly to/from an asteroid for work each day = totally removes a lot of the cost severance of living on an asteroid."*

**The re-examination (2026-04-24) revealed this was a Principle-#2 failure.** Two distinct phenomena had been conflated:
- The **asteroid-teleport example** described SPATIAL-ABUNDANCE MECHANICS (distance-as-abundance-condition producing abundance-costs).
- The **v2 glossary definition** described GEOGRAPHIC DISPERSAL OF VALUE vs CONCENTRATION OF COST: *"costs concentrate where extraction happens; value disperses to distant consumers. Geographic dimension of cost severance. The 13-year life expectancy gap between McDowell County and the national average is the human face of spatial cost severance."*

These are **two different framework elements.** The earlier retirement audited the asteroid-teleport description and concluded the phenomenon wasn't real severance — missing that the v2 definition describes a GENUINE severance subtype operating across a geographic gap.

**Principle-#3 variant-subtype check CORRECTED (re-examination pass §3):**
- Counterfactual: remove the spatial dispersal of value (imagine all electricity consumers live near McDowell County).
- Result: value-capturers and cost-bearers become the same community. Severance mechanism can't operate across a collapsed geography.
- Verdict: PASSES. Spatial dispersal is load-bearing for this form of severance.

**Rigor provenance:**
- Vocabulary-footprint meta-rigor pass §13.2.c (2026-04-24, commit `46600bc`) — initial RETIRE/DEMOTE analysis.
- Original retirement ratification (2026-04-24, commit `2dc54aa`) — based on author's asteroid-teleport description; later recognized as Principle-#2 failure (audited the wrong phenomenon).
- **Re-examination rigor pass `tools/rigor-passes/commons_bonds_rigor_pass_2026-04-24_term_spatial_cost_severance_re_examination_v1.0.0.md` (2026-04-24, commit `c04b7d8`)** — Option B (adopt as lowercase prose phrase) ratified; reverses earlier retirement.
- Principle-#3 check UNDER v2 DEFINITION: PASSES (spatial gap is load-bearing for this severance subtype).
- This re-examination **originated the "distinguishing gap-type" diagnostic** later reused in the Temporal CS reconsider pass: *"if removing a qualifier's condition doesn't leave other severance forms intact, the qualifier isn't a subtype qualifier."*

**Parallel to:** intergenerational cost severance (adopted 2026-04-24 commit `6e19f71`). Both are Cost Severance subtypes adopted as lowercase prose phrases. The spatial + intergenerational lowercase pair is the framework's subtype-descriptor set (Temporal was tested as potential third member via reconsider pass; FAILED Principle #3, kept retired).

**Depends on:**
- Cost Severance (Ring 1 parent concept)
- "spatial" adjective (framework-familiar; also used in Spatial abundance)
- Principle-#3 variant-subtype discipline
- Principle #2 (audit concept not phrase — principle origination includes this re-examination as a Principle-#2 recovery template)

**Staleness triggers:**
- Phrase drifts into capitalized usage → lowercase-discipline re-test.
- Cost Severance parent concept redefined.
- Academic field adopts established terminology that should displace.

**Commit trail:**
- Meta-pass initial analysis: commit `46600bc` (2026-04-24).
- Original retirement ratification: commit `2dc54aa` (2026-04-24).
- Re-examination rigor pass: commit `c04b7d8` (2026-04-24).
- Ratification of un-retirement: this commit.

**Supersedes / superseded by:** v1.1 (CURRENT lowercase-prose-phrase) supersedes v1.0 (RETIRED) from 2026-04-24. Earlier retirement preserved in history above as Principle-#2 recovery template.

**Notes:**
- **Distinct from Spatial abundance.** Spatial abundance is one of the 10 abundances (framework scaffolding). Spatial cost severance is a CS-subtype-by-geographic-gap. These are different framework elements; the conflation between them caused the original Principle-#2 failure.
- **Canonical example:** McDowell County 13-year life-expectancy gap (coal's value dispersed nationally while health + community collapse costs concentrated locally). Book prose already extensively describes this phenomenon; the lowercase phrase formalizes the subtype-handle.
- **Style discipline (lowercase always):** restructure sentences to avoid sentence-start capitalization where possible. Mirrors intergenerational cost severance discipline. Not a capitalized proper-noun compound.
- **Sweep targets (Phase A3):** glossary v2 → v3 sub-entry under Cost Severance; Ch 2 McDowell prose (where the phenomenon is already described) can use the phrase naturally; meta-pass §13.2.c table updated with un-retirement pointer.

---

### Universality Test

**Working definition (prior, retired):** A framework-internal validation check — run the framework against diverse extraction contexts (terrestrial + hypothetical extraterrestrial Mars/Europa) and verify it produces reasonable answers including self-identification of boundary conditions. Complements AIT as framework's validation methodology (vs AIT's discovery methodology).

**Status:** `RETIRED / DEMOTED` as capitalized named term (ratified 2026-04-24 by Chris Winn). Concept preserved in prose as scope-claim + boundary-awareness + Tech Appendix §F Mars/Europa illustration.

**Term-spec version:** v1.1 (supersedes v1.0 en-bloc demotion; individual-pass verification).

**Last reviewed:** 2026-04-24

**Rigor provenance:**
- Meta-pass §11.5 + §13.2.a en-bloc ratification (commit `d58b2cd`, 2026-04-24) — DEMOTE recommendation on "M1 of rigor protocol subsumes universality testing" grounds (rationale later corrected — see individual pass).
- Individual re-examination pass `tools/rigor-passes/commons_bonds_rigor_pass_2026-04-24_term_universality_test_re_examination_v1.0.0.md` (2026-04-24) — Option B (CONFIRM DEMOTE) with corrected rationale: named-test status requires the test to be EXERCISED; 0 chapter refs + no in-book exercise fails that threshold.
- AIT-pairing comparison vs Abundance Masking: UT's pairing with AIT is categorial (both methodologies), NOT structural (AIT's definition doesn't depend on UT being named) — differs from AM-AIT where AIT's definition requires AM named.

**Depends on (why this term was in the vocabulary):**
- Glossary v2 carried the term as a methodology paired with AIT.
- V2 definition's "complements AIT" language initially suggested load-bearing pairing.

**Staleness triggers:**
- Book cases start exercising a repeated universality-check methodology that benefits from a name-handle.
- AIT is restructured such that its definition becomes dependent on UT being named.
- Framework develops a formal boundary-condition protocol warranting its own named test.

**Commit trail:**
- Meta-pass en-bloc demotion: commit `d58b2cd`.
- Individual re-examination pass commit: `713beb7`.
- Ratification: this commit.

**Supersedes / superseded by:** N/A — concept preserved in prose + Tech Appendix §F; only capitalized term retired.

**Notes:**
- Tech Appendix §F retains Mars/Europa passage as "scope claim + boundary-awareness illustration" without the named test.
- Distinguishing from Abundance Masking (which PROMOTED to Ring 2 pending ratification via parallel re-examination): AM names an in-the-world mechanism active in every extraction case; UT names a validation methodology that isn't exercised anywhere. Different Principle-#3 outcomes despite both having AIT-pairing in v2.
- Phase A3 sweep targets: glossary v2 entry removed in v3; Tech Appendix §F reframed.

---

### Civilizational Substitutability Gap (CSG)

**Working definition (prior, retired):** A derived scalar CSG(R) = S_max(R, industrial) − S_max(R, existential) — the gap between industrial-context substitutability ceiling and existential-context substitutability ceiling for a resource R. Policy rule: high-gap resources warrant strategic in-situ preservation.

**Status:** `RETIRED` as capitalized named term (ratified 2026-04-24 by Chris Winn). Concept preserved in prose as "industrial-existential substitutability gap" + sub-entry under Substitutability Function in glossary v3 + Tech Appendix §G formula + policy rule retained.

**Term-spec version:** v1.0 final (retirement).

**Last reviewed:** 2026-04-24

**Rigor provenance:**
- Meta-pass §11.2 + §13.2.c rigor-only analysis (commit `af2f18e`, 2026-04-24) — RETIRE on "CSG is S-at-scale" grounds.
- Individual rigor pass `tools/rigor-passes/commons_bonds_rigor_pass_2026-04-24_term_csg_v1.0.0.md` (2026-04-24) — Option B (CONFIRM RETIRE) with corrected semantic test: CSG is specifically a DIFFERENCE between two S-evaluations (not just "S at scale"). Correction confirms (not rescues) retirement.
- Parsimony principle: framework doesn't name derived scalars. S(t) − S(t−1), max-S-over-uncertainty, S-for-rival-baselines — none are named separately. CSG belongs to that class.
- ARP pairing differentiator: CSG-ARP is TOPICAL pairing (ARP applies to high-CSG resources), NOT STRUCTURAL (ARP's definition doesn't depend on CSG being named). Contrasts with AM-AIT. Weaker pairing → doesn't reach Ring-2.
- Ratification produced a ratified Principle #1 Corollary B: **"usage frequency alone is not a rigor argument for retention."** CSG had 66 active refs (close-call flagged); ratification confirmed that usage frequency cannot override the derivation-from-primitive verdict.

**Depends on (why this term was in the vocabulary):**
- Glossary v2 carried CSG as a standalone entry under policy-instruments section.
- Active use in Ch 7 (Mars colony, asteroid-miner) + Ch 9 (Renewable Imperative) as decision-rule shorthand.

**Staleness triggers:**
- Ch 7 / Ch 9 chapter rewrites produce prose-quality issues that would be resolved by restoring CSG as a named term.
- A structural pairing emerges where CSG becomes load-bearing for another framework element's definition (analogous to Abundance Masking for AIT).
- Academic field adopts "CSG" as a travel-ready term that retirement would forfeit.

**Commit trail:**
- Meta-pass §13.2.c analysis: commit `af2f18e`.
- Individual rigor pass commit: `3ec3707`.
- Ratification: this commit.

**Supersedes / superseded by:** N/A — concept preserved in prose + Tech Appendix §G formula; only capitalized term retired. Prose replacement: "industrial-vs-existential substitutability gap" OR "industrial-existential substitutability gap" OR (for Tech Appendix mathematical contexts) simply "the difference between S_max(industrial) and S_max(existential)."

**Notes:**
- Close-call retirement: 66 active refs + active pedagogical use in Ch 7/Ch 9 + ARP pairing. Ratified as RETIRE on rigor grounds (parsimony + derivation-from-primitive) overriding usage-frequency argument. This ratification established Principle #1 Corollary B.
- ARP (Asymmetric Regret Principle) v2 reference "Applies across all uncertainty ranges for high-CSG resources" rewrites to "Applies across all uncertainty ranges for resources with large industrial-existential substitutability gaps." Downstream sweep.
- Phase A3 sweep targets (Stream A): Ch 7 (asteroid-miner + Mars-colony prose) + Ch 9 (Renewable Imperative) + glossary v2 → v3 removal + Tech Appendix §G retain formula as sub-entry under Substitutability Function. ~2-3 days sweep work per meta-pass estimate.

---

### Substitutability Function (S)

**Working definition:** Probability function S(t | t₀) — probability that a functionally adequate substitute for resource R exists at future time t, conditional on baseline technological state at t₀. Appears in foreclosure-cost term C₁ = [1 − S(t|t₀)] · U(R, t, Q(t)). Influenced by extraction-timing feedback: earlier extraction can reduce innovation pressure and lower S(t) for future t. Framework's most novel single mathematical component per meta-pass §10.2.

**Status:** `CURRENT` at Ring 2 (ratified 2026-04-24 by Chris Winn).

**Term-spec version:** v1.0 (first sanctioned spec).

**Last reviewed:** 2026-04-24

**Rigor provenance:**
- Meta-pass §10.2 (commit `46600bc`) — identified as framework's most novel single component; Ring-2 default classification.
- Individual rigor pass `tools/rigor-passes/commons_bonds_rigor_pass_2026-04-24_term_substitutability_function_v1.0.0.md` (2026-04-24) — Option A (confirm Ring 2) verified via distinctness check vs Hicks / real options / intertemporal substitution + 98-ref concept audit + Principle-#3 primitive-distinctness check.

**M12 classification:** Independent specialization (not adoption, not original coinage). Framework-specific features (time-indexed probability, baseline-conditional, endogenous to extraction timing) distinguish from Hicks 1932 elasticity of substitution + Dixit-Pindyck 1994 real options + intertemporal substitution macro theory.

**M12 citations (ratified 2026-04-24):**
- Hicks, John R. *The Theory of Wages* (1932) — foundational elasticity-of-substitution lineage.
- Dixit, Avinash K. & Pindyck, Robert S. *Investment under Uncertainty* (Princeton 1994) — real-options theory closest established concept.
Tech Appendix §L methodological footnote positions S as framework-specific extension.

**Why Ring 2 (not Ring 1):** S is a mathematical function; policymakers adopt named quantities (RCV), not named functions. Readers encounter S to understand C₁; non-readers don't adopt. Internal load-bearing is the correct scope.

**Depends on:** C₁ formula structure · definition of "functionally adequate substitute" · baseline t₀ convention.

**Pairs with:** Externality Tail E (sibling canonical cost term) · Foreclosure Cost C₁ (S is a factor in C₁) · Extraction-timing feedback loop.

**Staleness triggers:**
- CORE math restructured to eliminate C₁ as separate term.
- Academic field produces established terminology that should displace.
- Ring-1 vs Ring-2 boundary redrawn such that S becomes a public-adoption target.

**Commit trail:**
- Individual rigor pass: commit `302dffb` (2026-04-24).
- Ratification + Ring-2 record: this commit.

**Notes:**
- S_max derivations (including retired CSG formula) are compositional uses of S, not separate primitives. Primitive/derivation discipline established via CSG retirement pass.
- 98 active refs across 25 files as of 2026-04-24.
- Ch 6 §Substitutability Function is the term's pedagogical home.

---

### Externality Tail (E)

**Working definition:** Time-indexed cost function E(R, t) — damage from extraction of resource R at time t that persists independently of substitute availability. Sibling to foreclosure cost C₁ in the RCV integrand; runs on its own clock (temporally independent of S); structurally specializes Pigouvian externality concept with post-extraction persistence + substitutability-independence. "A substitute for coal doesn't clean up the mine. A substitute for oil doesn't remove carbon from the atmosphere."

**Status:** `CURRENT` at Ring 2 (ratified 2026-04-24 by Chris Winn).

**Term-spec version:** v1.0 (first sanctioned spec).

**Last reviewed:** 2026-04-24

**Rigor provenance:**
- Meta-pass §10.2 — Ring-2 internal load-bearing classification.
- Individual rigor pass `tools/rigor-passes/commons_bonds_rigor_pass_2026-04-24_term_externality_tail_v1.0.0.md` (2026-04-24) — Option A (confirm Ring 2) verified via distinctness check vs Pigouvian externalities + 46-ref concept audit + Principle-#3 check.

**M12 classification:** Framework-specific specialization of Pigouvian externality concept. Distinct via (a) post-extraction persistence, (b) substitutability-independence, (c) time-indexed function form, (d) "runs on its own clock" rhetorical anchor.

**M12 citations (ratified 2026-04-24):**
- Pigou, Arthur Cecil. *The Economics of Welfare* (1920, 4th ed. 1932) — foundational externality literature.
- Nordhaus, William D. & Boyer, Joseph. *Warming the World* (MIT Press 2000) — DICE model methodological parallel.
- Stern, Nicholas. *The Economics of Climate Change: The Stern Review* (Cambridge 2007) — intergenerational-equity framing.
Tech Appendix §L footnote positions E as temporal-specialization of Pigouvian externality.

**Why Ring 2 (not Ring 1):** E(R, t) is a function name; policymakers adopt named quantities, not named functions. Expanding Ring 1 dilutes adoption-bet focus on Severed Cost flagship.

**Phrase travel-potential flagged:** The PHRASE "externality tail" (not the function) may have Ring-1-travel potential if policy / legal discourse adopts. Monitoring note only; not a Ring-1 promotion recommendation.

**Depends on:** RCV integrand structure · "extraction" concept · "persistence" concept.

**Pairs with:** Substitutability Function (S) sibling · Foreclosure Cost (C₁) sibling · Four Gates (E passes through Gates like any admitted Cᵢ).

**Staleness triggers:**
- CORE math restructured to eliminate E as separate term.
- Academic field produces established terminology that should displace.
- Phrase "externality tail" adoption reaches threshold for Ring-1 promotion consideration.

**Commit trail:**
- Individual rigor pass: commit `bbe8069` (2026-04-24).
- Ratification + Ring-2 record: this commit.

**Notes:**
- "Tail" metaphor does NOT imply diminishing — E can compound (climate cumulative damage). Ch 6 clarification recommended.
- Ch 7 pedagogical role teaches foreclosure-vs-persistence distinction (C₁ vs E). Preserve.

---

### Asymmetric Regret Principle (ARP) — SUPERSEDED 2026-04-24 by Asymmetric Regret Rule (ARR)

**Status:** `SUPERSEDED` 2026-04-24 by Asymmetric Regret Rule (ARR) per ARP rename rigor pass (commit `b8b62e3`) ratified by Chris Winn 2026-04-24 (FINAL ratification after same-day flip from preliminary Reversibility Default ratification). The decision-theoretic CONTENT and aphorism *"We can always extract later. We can never un-extract."* preserved unchanged; the LAST WORD updated ("Principle" → "Rule") to address overclaim concern while preserving regret-theory direct-lineage in the name.

**Why renamed:** "Principle" overclaimed (operational decision rule, not foundational ethical principle). "Rule" downgrades while preserving "Asymmetric Regret" framing — direct M6 academic pattern-match to Loomes-Sugden 1982 + Savage 1951 regret-theory tradition. Maximum-protective M6 in the name without Tech-Appendix-footnote dependency.

**Supersession trail:** see Asymmetric Regret Rule record below for current framework element.

**Working definition (prior, retained for historical reference):** Framework-specific operational decision rule — when RCV tails cannot be precisely quantified, default to the reversible option. Specialization of Savage-style minimax-regret applied to resource-extraction decisions under quantification uncertainty. Bidirectional-flip-by-context — directs extract-aggressively (Comet flyby case: access window closes) OR preserve (Europa case: incommensurable externality) depending on which action is reversible.

**Phase A3 sweep targets activated by ARP rename ratification:**
- ~20 chapter refs (Ch 7 GuidanceDoc 11 refs + Ch 7/9/10 drafts + Tech Appendix) — Tier-1 sweep per Principle #4: replace "Asymmetric Regret Principle" / "ARP" with "Reversibility Default" / "RD."
- Older rigor passes + session handoffs — Tier-2 retirement-note headers per Principle #4.
- Working Principle #5 (context-flipping rules earn named-rule status) — example reference updates from ARP to Reversibility Default.
- CSG record cross-pairing reference: ARP-cited-CSG-context updates to RD-cited-CSG-context.

---

### Reversibility Default (RD) — RATIFICATION REVERSED 2026-04-24 (same-day flip)

**Status:** `RATIFICATION-REVERSED` 2026-04-24 same-day flip. Preliminary ratification of Reversibility Default (earlier 2026-04-24) reversed when M6 academic-rigor question surfaced post-ratification: RD required Tech Appendix footnote + Ch 7 prose + Glossary entries to make Savage / Loomes-Sugden lineage visible to reviewers; Asymmetric Regret Rule (ARR) has the lineage IN THE NAME — M6 maximum-protective without footnote dependency. Author flipped to ARR. Final ratified element is **Asymmetric Regret Rule (ARR)** per record below.

**Lesson captured (for ARP rename rigor pass + future similar passes):** when M5 + cross-tradition-adoption tradeoffs appear close, foreground M6 direct-name-visibility EXPLICITLY in the executive summary recommendation. The M5/M6 weighing should be visible to author at ratification time, not surfaced post-ratification.

**Preliminary working definition (preserved for provenance):** Framework-specific Ring-2 operational decision rule — when RCV tails cannot be precisely quantified, default to the option whose action is reversible. Same decision-theoretic content as Asymmetric Regret Rule (FINAL ratified name); only the name candidate differed.

---

### Asymmetric Regret Rule (ARR) — FINAL ratification 2026-04-24

**Working definition:** Framework-specific Ring-2 operational decision rule — when RCV tails cannot be precisely quantified, default to the option whose action is reversible: extraction when access window closes (Comet flyby), preservation when irreversible damage is at stake (Europa). Aphorism: *"We can always extract later. We can never un-extract."* Specialization of Savage 1951 minimax-regret with irreversibility-weighted regret tails (Loomes-Sugden 1982 regret-theory tradition). Bidirectional-flip-by-context (per Working Principle #5: context-flipping rules earn named-rule status). Aligned with Lempert-Popper-Bankes 2003 RDM + Rio Declaration 1992 precautionary tradition.

**Status:** `CURRENT` at Ring 2 (ratified 2026-04-24 by Chris Winn — supersedes Asymmetric Regret Principle; ratification finalized after same-day flip from preliminary Reversibility Default ratification).

**Term-spec version:** v2.0 (rename from Asymmetric Regret Principle v1.0; framework content unchanged; last word "Principle" → "Rule" to downgrade overclaim while preserving regret-theory direct-lineage in name).

**Last reviewed:** 2026-04-24

**Rigor provenance:**
- ARP rigor pass (commit `7f35783`, 2026-04-24) — Ring-2 promotion ratified for the underlying decision rule (originally as Asymmetric Regret Principle).
- ARP rename rigor pass `tools/rigor-passes/commons_bonds_rigor_pass_2026-04-24_arp_rename_v1.0.0.md` (commit `b8b62e3`, 2026-04-24) — 10 candidates tested; Reversibility Default identified as top M5 finalist; Asymmetric Regret Rule identified as M6 fallback. Pass's executive summary insufficiently surfaced M6 cost of RD's footnote-dependency; author M6 question post-ratification flipped final choice to ARR.
- Preliminary ratification (Reversibility Default) — REVERSED same-day 2026-04-24 after M6 question surfaced.
- Final ratification 2026-04-24 by Chris Winn — this commit. **Asymmetric Regret Rule (ARR) ratified.**

**Why "Asymmetric Regret Rule" (FINAL):**
- **M6 maximum-protective in the name.** Decision theorist + academic reviewer pattern-matches "Asymmetric Regret" to Loomes-Sugden 1982 + Savage 1951 regret-theory tradition immediately. No Tech-Appendix-footnote dependency.
- **"Rule" downgrades "Principle" overclaim** while preserving regret-theory framing — operational decision rule, not foundational ethical principle.
- **Minimal sweep cost** — ARP and ARR differ only in last word; existing chapter prose retains "asymmetric regret" framing largely intact.
- **Authorial-voice continuity** preserved — Ch 7 GuidanceDoc's existing "asymmetric regret" prose largely unchanged.
- **Decision-theoretic lineage in the name** stronger M6 than Reversibility Default's footnote-dependent lineage.
- **Aphorism preserved:** *"We can always extract later. We can never un-extract."* The aphorism describes the operational instruction; "Asymmetric Regret Rule" names the principled basis for that instruction (regret asymmetry under irreversibility).

**M12 classification:** Original specialization within counterfactual-reasoning + minimax-regret + precautionary-principle + real-options decision-theoretic lineage. Adjacent traditions cited; framework's contribution is specialization-with-bidirectional-flip + irreversibility-weighted regret-tail framing.

**M12 citations:**
- Savage, Leonard J. "The Theory of Statistical Decision." *Journal of the American Statistical Association* 46, no. 253 (1951): 55–67. — already in bibliography §16.
- Loomes & Sugden 1982 *Economic Journal* — already in bibliography §16. Asymmetric-regret theory.
- Lempert, Popper & Bankes 2003 *Shaping the Next One Hundred Years* — already in bibliography §16. Robust Decision Making.
- Dixit & Pindyck 1994 — already in bibliography §16. Real-options theory; reversibility-as-decision-axis.
- Rio Declaration 1992 Principle 15 — precautionary-principle tradition (general international-law reference; Tech Appendix footnote).

**Why Ring 2 (not Ring 1):**
- Framework-internal operational decision rule, not public-adoption-target vocabulary.
- Pedagogically useful across Ch 7 / Ch 9 / Ch 10 + Ch 7 GuidanceDoc but not flagship contribution.

**Why NOT retired (despite overlap with Precautionary Principle):**
- Bidirectional flip-by-context is RD-distinctive; PP is unidirectional.
- Trigger condition (cost-quantification uncertainty for RCV tails) is specific.
- 20+ active chapter refs.

**Pairs with:**
- RCV (Ring 1) — the function over whose tails uncertainty applies.
- Substitutability Function S (Ring 2) — RD governs decisions about high-substitutability-gap resources.
- Working Principle #5 (context-flipping rules earn named-rule status) — RD is the originating example.
- CSD + RCV two-instrument architecture — RD applies to uncertainty in either instrument's tails.

**Aphorism preserved:** *"We can always extract later. We can never un-extract."* This aphorism literally describes reversibility-default; renaming the rule to match the aphorism's actual content is consistent.

**Two paradigm cases (Ch 7) preserved:**
- **Comet flyby:** access window closes permanently → extraction is reversible-relative-to-losing-access → RD directs extract.
- **Europa:** incommensurable biosphere externality → preservation is reversible-relative-to-irreversible-damage → RD directs preserve.

**Open Insight #12** (ARP rename sub-decision) — closed-ratified 2026-04-24.

**Staleness triggers:**
- Framework develops formal minimax-regret treatment that subsumes RD mechanically.
- Academic adoption shows alternative naming displacing RD.
- Two paradigm cases (Comet/Europa) restructured in chapter drafting.

**Commit trail:**
- ARP Ring-2 promotion: commit `7f35783`.
- ARP rename rigor pass: commit `b8b62e3`.
- Ratification + Terms Index supersession + RD record: this commit.

**Notes:**
- Phase A3 sweep targets: Ch 7 GuidanceDoc + Ch 7/9/10 drafts (~20 refs); Tech Appendix v0.0.5 academic-anchor footnote; Glossary v3 entry rename; Working Principle #5 example-reference updates.
- Decision-theoretic content unchanged; only name updates.
- Same Option C' political-philosophical-accommodation discipline that resolved Restitution Bond + 10-list dissolution applies — Reversibility Default is operationally primary + cross-tradition-adoption-broad.

**Term-spec version:** v1.0 (first sanctioned spec).

**Last reviewed:** 2026-04-24

**Rigor provenance:**
- Meta-pass §13.2.c (commit `af2f18e`) — DEFERRED pending author re-read.
- Individual rigor pass `tools/rigor-passes/commons_bonds_rigor_pass_2026-04-24_term_asymmetric_regret_principle_v1.0.0.md` (2026-04-24) — Option A (PROMOTE to Ring 2) ratified with rename-sub-decision flagged.
- **Principle #5 origination:** ARP's bidirectional-flip behavior originated Working Principle #5 ("Context-flipping rules earn named-rule status") ratified 2026-04-24.

**M12 classification:** Framework-specific operational specialization of established decision-theoretic family. Related to Precautionary Principle (different: ARP bidirectional, PP unidirectional); related to Savage 1951 minimax-regret + Loomes-Sugden 1982 regret theory (framework-specialization with irreversibility-weighted regret tails); related to Lempert Popper Bankes 2003 Robust Decision Making (philosophically aligned).

**M12 citations (ratified 2026-04-24):**
- Savage, Leonard J. "The Theory of Statistical Decision" (JASA 1951).
- Loomes, Graham & Sugden, Robert. "Regret Theory: An Alternative Theory of Rational Choice Under Uncertainty" (Economic Journal 1982).
- Lempert, Popper & Bankes. *Shaping the Next One Hundred Years* (RAND 2003).
Tech Appendix footnote positions ARP as framework-specialization.

**Why Ring 2 (not Ring 1):** Framework-internal operational rule, not public adoption target. Pedagogically useful across Ch 7 / Ch 9 / Ch 10 but not the flagship contribution.

**Why NOT retired (despite overlap with Precautionary Principle):** Bidirectional flip-by-context is ARP-distinctive; PP is unidirectional. Trigger condition (cost-quantification uncertainty for RCV tails) is specific. 20+ active chapter refs.

**Rename sub-decision (OPEN — pending author decision, does not affect rigor verdict):**
Candidates: *Asymmetric Regret Principle (current)* · *Asymmetric Regret Rule* · *Asymmetric Rule* · *Asymmetry Rule* · *Reversibility Default* · *Irreversibility Bias* · *Regret Asymmetry Rule* · *Option-Preservation Rule*. Captured as Open Insight for author deliberation. Rename (if adopted) is Phase A3 Stream A sweep work.

**CSG-ARP cross-pairing:** CSG retired 2026-04-24; ARP's v2 reference "high-CSG resources" rewrites to "resources with large industrial-existential substitutability gaps" in Phase A3 sweep. Applies regardless of rename outcome.

**Depends on:** RCV (the function over whose tails uncertainty applies) · framework's cost-quantification methodology.

**Pairs with:**
- Substitutability Function (S) — ARP governs decisions about high-gap resources.
- Universality Test concept (demoted) — ARP is the rule for boundary-condition regime.

**Staleness triggers:**
- Framework develops a formal minimax-regret treatment that subsumes ARP mechanically.
- Academic community adopts "Reversibility Default" or analogous terminology that would displace current name.
- Rename ratified — rerun under new name to verify rigor transfers cleanly.

**Commit trail:**
- Individual rigor pass: commit `7f35783` (2026-04-24).
- Principle #5 ratified (originating context): commit `cae4936`.
- Ratification + Ring-2 record: this commit.

**Notes:**
- "Principle" in current name may overclaim given ARP is operational decision rule, not foundational principle. Rename sub-decision captures this concern.
- Academic-positioning: Tech Appendix footnote cites Savage 1951 + Rio Declaration 1992 (Precautionary Principle) + Lempert et al. 2003 RDM to position ARP as framework-specialization of established decision theory.

---

### Accountability Bond (B)

**Working definition:** Formal quantity B in the framework's flagship equation CS = RCV − B. Represents the total dollars forced onto extractors via accountability instruments — reclamation bonds, sovereign wealth funds, carbon taxes, insurance requirements, direct liability, severance agreements, any financial mechanism that internalizes extraction costs. Under the framework's ideal B = RCV (honest accounting). Under current regimes B < RCV (accountability gap = Cost Severance = RCV − B). Extends established environmental-bonding / Pigouvian-tax lineage from project-specific or single-externality scope to full Severed Cost spectrum.

**Distinguishing identity — B is the framework's REMEDIATION-side variable** *(author-specified framing 2026-04-24):* where RCV / AIT / Cost Severance / Severed Cost are **diagnostic** (they reveal, identify, name, quantify the problem), Accountability Bond is the **action-side** element. B is the dollars that actually flow onto the extractor's ledger to close (or attempt to close) the cost-severance gap. B doesn't measure severance; it REMEDIATES it. **Structurally the only remediation-side variable in the framework** — every other Ring-1/Ring-2 element works to make the gap visible; B is the element that does something about it. This is why B draws the heaviest scope-creep pressure (Open Insight #13) — action-side questions invite instrument-design depth (how specifically to raise B in case X for category Y?) that belongs to Book 2/3 not Book 1. The "Bond" metaphor reinforces the identity: a bond is POSTED (action), not MEASURED.

**Status:** `CURRENT` at Ring 2 (ratified 2026-04-24 by Chris Winn).

**Term-spec version:** v1.0 (first sanctioned spec).

**Last reviewed:** 2026-04-24

**Rigor provenance:**
- Meta-pass §10.2 (commit `46600bc`) — Ring-2 internal load-bearing classification.
- Literature audit + citation ratification commits `56a226f` + `f643e59` (2026-04-24) — M12 classification as extension of reclamation-bond + EIB + Pigouvian-tax lineage; bibliography citations ratified for Ch 5 + Tech Appendix.
- Individual rigor pass `tools/rigor-passes/commons_bonds_rigor_pass_2026-04-24_term_accountability_bond_v1.0.0.md` (2026-04-24) — Option A (confirm Ring 2) + two monitoring flags (phrase-travel + scope-creep).

**M12 classification:** Independent specialization + extension of established environmental-bonding / Pigouvian-tax lineage. Framework novelty is (a) full-Severed-Cost scope vs reclamation-only, (b) equational-closure role in CS = RCV − B. Not original coinage; consciously extends prior art.

**M12 citations (ratified 2026-04-24):**
- Pigou, Arthur Cecil. *The Economics of Welfare* (1920, 4th ed. 1932).
- Balboa, Cristina M. "Accountability of Environmental Impact Bonds" (*Global Environmental Politics* 2016).
- Yang, Peifang & Davis, Graham A. "Why Don't Environmental Bonds Fully Cover Reclamation Costs?" (*Energy Policy* 2021).
- U.S. GAO. *Financial Assurances for Reclamation* (GAO-17-207R, 2017).
- U.S. OSMRE. *Reclamation Bonds* (agency guidance).

Canonical Ch 5 + Tech Appendix first-use citation form drafted in rigor pass §3.5.

**Why Ring 2 (not Ring 1):**
- Scalar-variable role dominant (right-side of CS = RCV − B equation).
- Ring-1 focus discipline preserves adoption-bet focus on 7 current flagships.
- Phrase-travel-flag captures Ring-1-promotion upside without current commitment.

**Two monitoring flags (ratified 2026-04-24):**

**(i) Phrase-travel monitoring flag.** Watch for post-publication adoption evidence that "accountability bond" travels independently of framework uptake (legal briefs, policy papers, academic citation as load-bearing adoption term). Rerun trigger: reconsider Ring-1 promotion if phrase begins traveling in target-audience discourse.

**(ii) Scope-creep monitoring flag (cross-cutting; applies to whole framework, but Accountability Bond is likely-heaviest source of pressure). Governing doc: `tools/commons_bonds_book_scope_v1_0_3.md`.** Boundary is **framework-naming vs applied-advocacy-on-named-beneficiaries**, NOT diagnosis-vs-fix (corrected 2026-04-24 after author pointed to v1.0.3 strategy doc).
- **In-scope for Book 1 (framework-naming; passes v1.0.3 §6.1 rigor test as symmetric + shielded):** naming Accountability Bond; equational-closure role; lineage citation; flagship case illustration (McDowell, Deepwater, Libby, Social Security, etc.); framework-level prescription ("B should equal RCV" as stated ideal); Community Transition Reserve as named policy rec in Ch 9; one-paragraph signposts ($10–15T aggregate subsidy Ch 8 signpost).
- **Out-of-scope for Book 1, belongs in Book 2 (applied-advocacy; FAILS v1.0.3 §6.1 rigor test as asymmetric + unshielded for lone author):** full-economy B-vs-RCV simulation; resource-by-resource transition mechanics; named industries with documented lobbying histories that have kept their specific B below their specific RCV; named beneficiaries of the B < RCV gap; specific regulatory-capture events as case-study material; policy architecture at implementation level for named jurisdictions.
- **Trigger indicators during chapter drafting:** passage names specific industries with lobbying history; passage attempts full-economy simulation; passage does resource-by-resource transition mechanics; footnote becomes mini-essay on named industry.
- **Why B is heaviest scope-creep source:** B is the framework's **remediation-side variable** (only framework element that does something about the gap rather than measure it). Remediation role structurally pulls toward applied-advocacy on named beneficiaries. Book 1 names B + states B = RCV as ideal; Book 2 (requires coauthor/institutional shield) does applied work on specific industries' under-bonding + lobbying histories that sustain it.
- **Mitigation:** Book 1 points to future books ("a fuller treatment of named industries' lobbying histories is beyond this book's framework scope and is the subject of future applied work") rather than absorbing the depth. Preserve detailed notes in `archive/_OneDayMaybe/book-two/` for future.

**Rename candidates tested and rejected (per rigor pass §4):** *Accountability Severance* · *Severance Bond* · *Severed-Cost Bond* · *Commons Liability Bond*. Best fallback if rename ever needed: *Severed-Cost Bond* (pairs with Ring-1 flagship Severed Cost).

**Depends on:** CS = RCV − B equation · RCV definition · "accountability instrument" concept space.

**Pairs with:**
- RCV (left-side equation term; B is compared against RCV).
- Cost Severance (CS = gap between RCV and B).
- Commons Bonds (framework name; B is the instrument subtype of the broader commons-bonds category).

**Staleness triggers:**
- CS = RCV − B equation restructured.
- Phrase adoption in legal/policy discourse triggers Ring-1 reconsideration.
- Chapter drafting triggers scope-creep flag (instrument-design specifics beyond Book 1 scope).
- Established instrument terminology shifts (e.g., EIBs displace reclamation bonds as dominant policy frame).

**Commit trail:**
- Literature audit + citation ratification: commits `56a226f` + `f643e59` (2026-04-24).
- Individual rigor pass: commit `7fa1c1b` (2026-04-24).
- Ratification + Terms Index record: this commit.

**Notes:**
- B pairs structurally with RCV to close CS equation. Same mathematical-function-dominance as S and E but different role (output-side of equation vs integrand-components).
- "Accountability" vs "liability" distinction: accountability is the relational + constructive word (positive framing); liability is the defensive legal-action word. Framework uses "accountability" intentionally.
- "Bond" metaphor: operates both as financial-instrument (legal-register) and relational-bond (framework-title register). Double-entendre load-bearing for book's Commons Bonds positioning.

**Epistemic-humility discipline — author-specified framing 2026-04-24 (load-bearing for Book 1 authorial-voice calibration):**
- B is the framework CATEGORY for every mechanism that forces cost-bearing on extractors — NOT a novel single-instrument prescription. Book 1 should NOT present Accountability Bond as THE solution to cost severance.
- **Norway's Government Pension Fund Global (sovereign wealth fund) is Book 1's canonical existing real-world exemplar** of intergenerational-cost-severance mitigation. Norway is the most impressive existing solution humanity has produced for this problem class — framework-canonical case (Ch 4 anchor).
- **Norway's solution presupposes governance preconditions** (rule of law; institutional architecture preventing plundering current-population accounts or not-yet-born-generation accounts). Not a universal solution; its preconditions are load-bearing. Book 1 honors this — "even the best existing example isn't universal."
- **No claim to having solved it.** The framework's claim is mathematical (B = RCV is honest accounting); which specific instrument-mix best realizes that equality is a LIVE policy design space Book 1 frames but doesn't settle. Book 2 (or authors with institutional cover) are better positioned for applied instrument-design debate.
- **Book 1 CAN ponder.** Framework-appropriate pondering: *"perhaps something like an accountability bond could bridge this, though the Norway example shows what actually works and under what preconditions."* What's OUT of scope: prescribing a specific instrument design (e.g., "The Commons Bonds Framework Accountability Bond Act") as THE fix.

---

### Abundance Masking

**Working definition:** The mechanism by which abundance makes costs invisible to market pricing until scarcity forces them into view. Oxygen feels free because Earth's atmosphere is abundant. Ecological services feel free because ecosystems haven't collapsed yet. **Abundance Masking is the mechanism; Abundance Dimension is the dimension along which it operates** — distinct entries: masking is a process, dimension is a category (per v2 definition). Paired with AIT: masking is the process; AIT is the methodology that detects what masking hides.

**Status:** `CURRENT` at Ring 2 (ratified 2026-04-24 by Chris Winn — promoted from earlier DEMOTE-to-prose via re-examination).

**Term-spec version:** v1.1 (v1.0 was the meta-pass demote-to-prose recommendation; v1.1 corrects after Principle-#2 re-read under re-examination).

**Last reviewed:** 2026-04-24

**History and re-examination:**

The term was initially scheduled for DEMOTE-to-prose 2026-04-24 (meta-pass §13.2.c, commit `46600bc`) with rationale: *"Abundance Masking names the phenomenon that AIT detects — abundances mask costs by making them invisible to pricing. But the phenomenon is what AIT is FOR. Naming it as a separate term creates a term-per-mechanism bloat."*

**The re-examination (2026-04-24) revealed this was a Principle-#2 failure.** The reasoning got the direction BACKWARDS — it said "AIT detects AM, therefore AM is redundant with AIT." That's analogous to saying "we have 'severance mechanism detection,' so we don't need the term 'severance mechanism' itself." The DETECTOR and the DETECTED are complementary, not redundant.

The v2 definition makes the pairing structure explicit: *"Abundance Masking is the mechanism; Abundance Dimension is the dimension along which it operates. These are distinct entries: masking is a process, dimension is a category."*

**Decisive test — "What does AIT detect?":**
- Without Abundance Masking term: AIT's definition becomes circular or unanchored. Adversarial reader: *"What makes a cost scarcity-grounded vs not?"* The answer requires naming the phenomenon AIT is designed to detect.
- With Abundance Masking term: *"AIT tests whether a candidate cost survives abundance inversion — i.e., whether the cost is genuinely hidden by Abundance Masking or is intrinsic to the activity regardless of scarcity."* Clean + explanatorily complete.

**Parallel to Cost Severance vs Severed Cost pair:** framework benefits from naming both sides of flagship mechanism-pairs:

| Pair type | Left side | Right side |
|---|---|---|
| Mechanism + Result | Cost Severance | Severed Cost |
| **Mechanism + Methodology** | **Abundance Masking** | **AIT** |
| Event + Mechanism | Value Extraction | Cost Severance |

**Rigor provenance:**
- Meta-pass §11.3 + §13.2.c (commit `46600bc`, 2026-04-24) — initial DEMOTE-to-prose recommendation; Principle-#2 failure.
- Re-examination rigor pass `tools/rigor-passes/commons_bonds_rigor_pass_2026-04-24_term_abundance_masking_re_examination_v1.0.0.md` (2026-04-24, commit `cf02160`) — Option A (PROMOTE to Ring 2) recommended; supersedes earlier demote-to-prose.
- Ratification 2026-04-24 by Chris Winn — this commit.
- **Diagnostic originated here (cross-cutting):** "structural vs topical pairing" distinction that later guided Universality Test re-examination + CSG-ARP pairing analysis. Structural pairings (Partner-A's definition requires Partner-B named) justify Ring-2 promotion; topical pairings don't.

**M12 classification:** Framework-specific mechanism-name. The concept of abundance making costs invisible is adjacent to "rhetoric of abundance masks depletion" in ecological-economics literature + artificial-scarcity literature (Desai & Lemley 2022), but no established term captures the specific framework role as AIT-paired mechanism-name. **Appears novel as specific framework term.**

**Why Ring 2 (not Ring 1):**
- Framework-internal mechanism-name paired with AIT (also Ring 1).
- Not a public-adoption target. Readers encounter AM to understand AIT's object; non-readers don't adopt.
- Chapter usage pattern: the MECHANISM is active in every extraction case in the book (costs masked by atmospheric abundance, ecosystem-service abundance, etc. — McDowell, Deepwater, Libby, all exhibit the mechanism). Naming it at Ring 2 formalizes what's already operating.

**Depends on:**
- AIT (paired detection methodology — Ring 1)
- Abundances (the domain over which masking operates)
- Cost Severance (the phenomenon that masking enables by hiding costs)

**Pairs with:**
- **AIT (structural pairing).** AIT's definition requires Abundance Masking named. Retiring AM would break AIT's definition.
- **Abundance Dimension.** Process vs category distinction per v2 definition.

**Staleness triggers:**
- AIT methodology redefined in a way that changes what it detects.
- Framework's abundance vocabulary restructured.

**Commit trail:**
- Meta-pass initial DEMOTE-to-prose analysis: commit `46600bc` (2026-04-24).
- Re-examination rigor pass: commit `cf02160` (2026-04-24).
- Ratification + Ring-2 record: this commit.

**Supersedes / superseded by:** v1.1 (CURRENT Ring 2) supersedes v1.0 (DEMOTE-to-prose) from meta-pass §13.2.c. Earlier demotion preserved in history above as Principle-#2 recovery template.

**Notes:**
- Distinct from Abundance Dimension per v2 explicit distinction (process vs category).
- In-the-world mechanism: active in every extraction case in the book whether or not named in chapter prose. Naming formalizes what's already operating.
- **Diagnostic origination:** this re-examination surfaced the "structural vs topical pairing" distinction that is now part of the rigor protocol's working toolkit for evaluating AIT-pairing arguments. Formalized as M12 action-ladder input via Principle #6.

---

### CS = RCV − B equation (named relational claim)

**Working definition:** The framework's central relational claim — Cost Severance in a transaction equals specifically Residual Commons Value minus Accountability Bond (arithmetic subtraction). The equation asserts: (i) only RCV and B matter for computing CS; (ii) the accountability-gap is linear in B (each dollar of B reduces CS dollar-for-dollar); (iii) B = RCV defines the framework's ideal state quantitatively (CS = 0 ↔ honest accounting). **Named framework object distinct from its component terms** — CS, RCV, B each have their own Terms Index record + rigor pass; this equation record is the ratified-2026-04-24 classification of the equation itself as a distinct Ring-2 structural element.

**Status:** `CURRENT` at Ring 2 (ratified 2026-04-24 by Chris Winn — "named relational claim").

**Term-spec version:** v1.0 (first sanctioned spec).

**Last reviewed:** 2026-04-24

**Rigor provenance:**
- Meta-pass §10.2 + §12.1 item 7 (commit `46600bc`) — identified as Ring-2 internal load-bearing ("CS = RCV − B equation (as a single conceptual object)").
- Ring-1 full integrated pass (commit `d4c4be4`) — equation structurally tested in unified-system rigor; no reconsideration surfaced.
- Individual rigor pass `tools/rigor-passes/commons_bonds_rigor_pass_2026-04-24_term_cs_rcv_b_equation_v1.0.0.md` (2026-04-24) — Option A (CONFIRM Ring 2 as named relational claim) ratified 2026-04-24 by Chris Winn. Principle-#3 derivation check PASSES (light non-triviality: equation fixes arithmetic form + only-these-components claim + ideal-state definition beyond what's in components' prose definitions). M12 classification: independent specialization of established gap-accounting structure.

**M12 classification:** Independent specialization of established gap/deficit-accounting structure. Gap-form equations ubiquitous in adjacent literature:
- **Pigouvian gap:** externality − tax = unpriced amount (Pigou 1920).
- **Stern Review intergenerational framing:** present-cost-to-future minus current-priced = intergenerational transfer (Stern 2007).
- **Nordhaus DICE social-cost-of-carbon:** cumulative marginal damage − market carbon price = SCC gap (Nordhaus & Boyer 2000).
- **Accounting identity:** economic-cost − recorded-cost = unrecorded-cost.

Framework novelty is NOT the gap-form (ubiquitous) — it is the specific decomposition (what RCV is, what B is, what CS is as mechanism-result pair with Severed Cost).

**M12 citations (ratified 2026-04-24, already added to bibliography in prior commits):**
- Pigou, Arthur Cecil. *The Economics of Welfare* (1920) — Pigouvian gap lineage.
- Stern, Nicholas. *The Economics of Climate Change: The Stern Review* (Cambridge 2007) — intergenerational-gap parallel.
- Nordhaus, William D. & Boyer, Joseph. *Warming the World* (MIT Press 2000) — DICE social-cost-of-carbon parallel.

Tech Appendix §L methodological footnote positions the equation as extension of this established gap-accounting lineage with framework-specific decomposition.

**Why Ring 2 (not Ring 1):**
- Equations don't travel as adoption vocabulary the way terms do. Ring-1 adoption-targets are CS / SC / RCV / B / AIT / VE / Commons Bonds individually.
- Analogue: *F = ma* travels as vocabulary, but only AFTER Newtonian framework adoption; the framework-level terms (force, mass, acceleration) travel first. Same pattern: framework terms travel first; the equation holds them together internally.
- The equation is the internal structural anchor — Ring 2 (internal load-bearing) appropriate.

**Why NOT demoted to "just math" or merged into Cost Severance record:**
- Carries independent content (arithmetic form; only-B-and-RCV-matter claim; ideal-state definition).
- Citing the equation as a single object is rhetorically and pedagogically more economical than reconstructing the relationship each time.
- **Stability-anchor function** in rigor infrastructure: naming the equation forces consistency across term definitions. If a later rigor pass weakens one term, the equation surfaces the consequence for the whole framework immediately.
- **Scope-creep discipline (Insight #13):** equation-as-object helps chapter drafts stay at framework level ("CS = RCV − B; current regimes produce B < RCV") without sprawling into instrument-specific territory.

**Cross-reference to epistemic-humility discipline (Insight #14):**
The equation's statement "CS = RCV − B" is **framework-level prescription** (in-scope for Book 1 per v1.0.3). The equation does NOT commit to which specific instrument-mix realizes B. **Norway's sovereign wealth fund is the canonical real-world example of B approaching RCV;** the equation itself is the framework-level object that makes Norway's success measurable + that makes the American B << RCV gap visible. Book 1 presents the equation + points to Norway as best-existing-example + PONDERS Accountability Bond as one candidate direction — does NOT prescribe a specific instrument design as THE fix.

**Depends on (all these must hold for equation to hold):**
- CS definition (Ring 1) — mechanism/quantity.
- RCV definition (Ring 1) — integrand form ∫ᵗ₀^∞ {[1 − S(t|t₀)] · U(R, t, Q(t)) + E(R, t)} · D(t, t₀) dt.
- B definition (Ring 2) — full-Severed-Cost scope.
- Substitutability Function S (Ring 2) — appears in RCV integrand via C₁.
- Externality Tail E (Ring 2) — appears in RCV integrand.
- Abundance Masking + AIT (Ring 2/1) — govern which costs are admitted to RCV.
- Four Gates (Ring 2, pending) — admission apparatus for Cᵢ.

**Pairs with:**
- All component terms — equation is their combined structural anchor.
- Accountability-gap argument (the interpretive claim that CS > 0 in practice).
- Insight #14 epistemic-humility discipline (B = RCV is the ideal; Norway is canonical existing example; no single-instrument cure prescribed).

**Staleness triggers:**
- Any component definition changes in a way that affects the equation (stability-anchor function surfaces this immediately).
- CORE math restructured to use a different form (ratio, logarithm, multi-term).
- Academic adoption evidence shows gap-accounting form displaced by an alternative.

**Commit trail:**
- Individual rigor pass: this commit.
- Ratification + Terms Index record: this commit.

**Notes:**
- "CS = RCV − B" is the three-word / four-character / one-operator encapsulation of the framework's central claim. Maximum compressibility.
- Pedagogical role: readers who internalize the equation acquire the framework's central assertion in one expression.
- Rigor-infrastructure role: the equation acts as stability anchor — if later rigor weakens one component, the equation immediately surfaces the consequence for the whole.
- Scope-creep discipline: equation-as-object keeps chapter drafts at framework level rather than instrument-specific level (per Open Insight #13 + Insight #14).

---

### Intergenerational Pricing Gap (IPG)

**Working definition:** Ratio IPG = RCV / market_price — the factor by which markets underprice extraction at the point of transaction. "IPG = 33" means the market price covers approximately 3% of the true intergenerational cost captured in RCV. Framework-specific market-pricing-gap diagnostic, DISTINCT from Cost Severance (CS = RCV − B — accountability-pricing-gap diagnostic). Different diagnostic purpose, different denominator.

**Status:** `CURRENT` at Ring 2 (ratified 2026-04-24 by Chris Winn).

**Term-spec version:** v1.0 (first sanctioned spec).

**Last reviewed:** 2026-04-24

**Rigor provenance:**
- Meta-pass §10.2 + §12.1 item 10 (commit `46600bc`) — Ring-2 classification with flag for individual rigor to test demote-to-Ring-3 alternative.
- Individual rigor pass `tools/rigor-passes/commons_bonds_rigor_pass_2026-04-24_term_ipg_v1.0.0.md` (2026-04-24, commit `256e34d`) — Option A (CONFIRM Ring 2) ratified 2026-04-24. Principle-#3 derivation check PASSES.

**M12 classification:** Independent specialization. Adjacent intergenerational-pricing literature (Ramsey 1928, Stern 2007, Nordhaus DICE, declining-discount work from Weitzman/Gollier/Portney-Weyant) addresses "markets underprice intergenerational costs" qualitatively; no established work uses this specific ratio form with RCV-as-numerator. Framework-specific diagnostic composite.

**M12 citations (for Tech Appendix §L methodological footnote):**
- Ramsey, Frank P. "A Mathematical Theory of Saving" (1928) — foundational intergenerational-discount framework.
- Stern 2007 + Nordhaus DICE — already in bibliography for Externality Tail; cross-reference.
- Declining discount rate literature — optional Tech Appendix depth.

**Distinguishing from CS:**
- **CS uses B** (Accountability Bond — all accountability-instrument dollars; framework primitive). Measures what's not internalized by accountability mechanisms.
- **IPG uses market_price** (transaction price — external empirical reference). Measures what's not priced by markets at transaction time.
- Can diverge: Norway has small CS (sovereign wealth fund captures B ≈ RCV post-transaction) but potentially large IPG (oil market price below true intergenerational cost AT transaction). Complementary diagnostics.

**Parsimony-principle corollary established (ratified 2026-04-24):**
- **Internal derivations** (framework primitives only): NOT named (per CSG retirement — S_max, S(t)−S(t−1), etc.).
- **External-composites** (framework primitive composed with external empirical reference): CAN earn named-object status when load-bearing.
- IPG is canonical example of external-composite earning named status.
- Worth flagging as possible Principle #6 sub-corollary if pattern repeats.

**Epistemic-honesty note (for Ch 6 framing, ratified 2026-04-24):**
- "IPG ≫ 1 universally" is PARTLY by construction — RCV includes intergenerational costs markets don't price, so IPG > 1 is architectural for extraction cases.
- Empirical work quantifies MAGNITUDE (McDowell IPG = 33), not direction.
- Ch 6 convergence-table framing should present as "architecture + magnitude calibration," not "open empirical finding." Overclaiming the architectural-fact as empirical-discovery would be a rigor-integrity risk.

**Why Ring 2 (not Ring 3 demote per meta-pass flag):**
- Distinct diagnostic from CS (different denominator, different diagnostic purpose).
- 15+ active chapter/guidance refs + dedicated WS12 decision doc.
- Convergence-table pedagogy (Ch 6) depends on IPG as compressed scalar ("IPG = 33" is framework's canonical empirical compression).
- "IPG ≫ 1" architectural claim deserves a named handle.

**Depends on:**
- RCV definition (numerator — framework primitive).
- Market-price measurement (denominator — external empirical reference).
- Cost Severance (IPG is complementary diagnostic, not synonym).

**Pairs with:**
- CS = RCV − B (complementary gap diagnostic — different denominator).
- RCV (direct component).
- Accountability-gap narrative (IPG quantifies market-pricing-gap at transaction time; CS quantifies what accountability instruments cover).

**Staleness triggers:**
- RCV definition restructured.
- Framework develops more precise pricing-gap diagnostic that displaces.
- Empirical work reveals "IPG ≫ 1" not universal (would change both architectural claim and IPG's role).

**Commit trail:**
- Individual rigor pass: commit `256e34d` (2026-04-24).
- Ratification + Terms Index record: this commit.

**Notes:**
- Convergence-table pedagogy: 4 approaches converge on IPG ≫ 1. Chapter's numerical center of gravity.
- McDowell IPG = 33 (market covers ~3% of true cost) is framework's canonical empirical compression — readers remember single-number claim.
- WS12 IPG data table (`alignment/decisions/ws12-ipg-data-table-for-reconciliation.md`) is load-bearing for case-study cross-comparison.

---

### Commons Inversion Test (CIT) [supersedes AIT 2026-04-24]

**Working definition:** Framework-specific Ring-1 methodology for admitting candidate costs to RCV. Operates on commons categories: imagine the commons inverted (either absent or unconsumed); if the candidate cost becomes visible as commons-dependent, admit to Cᵢ via Four Gates. Two sub-forms:
- **Commons-Absence Inversion** — imagine commons not existing (paradigm: oxygen in space; McDowell habitability destroyed by coal extraction). Operational question: *what would it take to replace the commons?*
- **Commons-Consumption Inversion** — imagine commons not consumed (paradigm: commute-time returned; forest uncut). Operational question: *what could the commons do if not drawn down?*

Specialized extension of commons-governance methodology (Ostrom lineage) to extraction-contexts where commons are drawn down rather than managed-in-place.

**Status:** `CURRENT` at Ring 1 (ratified 2026-04-24 by Chris Winn). Supersedes AIT.

**Term-spec version:** v1.0 (first sanctioned spec).

**Last reviewed:** 2026-04-24

**Rigor provenance:**
- Author structural-identity insights 2026-04-24 — commons-as-structural-identity + AIT-as-CIT realizations.
- Commons-as-Structural-Identity rigor pass `tools/rigor-passes/commons_bonds_rigor_pass_2026-04-24_commons_as_structural_identity_v1.0.0.md` (commit `c4b09dc`) — broader reframing including CIT rename + 10-as-commons-categories. Option A ratified.
- Dedicated CIT rename rigor pass `tools/rigor-passes/commons_bonds_rigor_pass_2026-04-24_term_cit_rename_v1.0.0.md` (commit `b294c79`) — Option A (ratify CIT) ratified with full M12 audit + sub-form formalization.
- 10-Commons-List Dissolution rigor pass `tools/rigor-passes/commons_bonds_rigor_pass_2026-04-24_10_commons_list_dissolution_v1.0.0.md` (commit `e30087e`) — Option C' ratified (10 as examples-not-canonical; methodology-forward; political-philosophical acknowledgment).

**M12 classification:** Original specialization within counterfactual-reasoning methodological family. No prior-art collision on phrase or concept; acronym collisions in unrelated domains only (spell-out-at-first-use convention mitigates).

**M12 citations (for Tech Appendix methodological footnote):**
- Ostrom 1990 *Governing the Commons* — commons-governance lineage.
- Hess & Ostrom 2007 *Understanding Knowledge as a Commons* — knowledge commons extension; precedent for extending commons to novel domains.
- Counterfactual reasoning family (Lewis 1973 + subsequent philosophy-of-action literature) — operational lineage.

**Supersedes:** AIT (Abundance Inversion Test). AIT's semantic content preserved + refined via two sub-forms; name updated to match operational instruction (commons-inversion, not abstract abundance-inversion).

**Depends on:** commons-governance tradition (Ostrom lineage); commons as structural identity of formerly-named-abundances; Four Gates admission apparatus; "abundance" as state-name of each commons.

**Pairs with:**
- RCV (Ring 1) — CIT admits costs to RCV integrand.
- Four Gates (Ring 2) — CIT is one of four admission gates.
- Abundance Masking (Ring 2) — CIT detects what Abundance Masking hides.
- Cᵢ (Ring 1) — CIT-admitted costs become Cᵢ entries.
- Commons categories (the 10 examples) — CIT operates on each commons.

**Staleness triggers:**
- Commons-as-structural-identity reframing reversed.
- New methodology replaces CIT.
- Academic adoption evidence shows CIT failing to travel.

**Commit trail:**
- Commons-as-Structural-Identity pass: commit `c4b09dc` (2026-04-24).
- Dedicated CIT rename pass: commit `b294c79` (2026-04-24).
- 10-list dissolution pass: commit `e30087e` (2026-04-24).
- Ratification + Terms Index record: this commit.

**Notes:**
- "Commons Inversion Test" at first-use per chapter; "CIT" as acronym after. Framework convention per AIT precedent.
- Two sub-forms formalized as framework methodology contribution beyond rename — see Tech Appendix methodology section + Open Insight #16.
- Commute-story (Personal Stories Candidate #1) is the paradigm Commons-Consumption case; most resource-extraction cases are Commons-Absence; some (mining) exercise both.

---

### Abundance Inversion Test (AIT) — RETIRED

**Status:** `RETIRED` (ratified 2026-04-24 by Chris Winn — superseded by Commons Inversion Test (CIT) per commons-as-structural-identity reframing). Historical references in older docs preserved per Principle #4 Tier-2 discipline (retirement-note headers; no content sweep).

**Working definition (prior, retired):** Framework methodology for admitting candidate costs to RCV via abundance-inversion test ("invert the current abundance condition; does the cost become visible?").

**Term-spec version:** v1.0 final (retirement).

**Last reviewed:** 2026-04-24

**Why retired:** Author insight 2026-04-24: *"AiT is really CiT showing that a commons cost exists when you imagine the current abundance of that commons not existing."* The test operates on commons (concrete shared resources), not on abstract abundance-states. CIT's framing makes the operational instruction visualizable; AIT's framing required reader-side abstraction. Plus the two sub-forms (Commons-Absence + Commons-Consumption Inversion) became visible only after the commons-reframing — they were obscured under "invert the abundance state" language.

**Supersedes / superseded by:** Superseded by Commons Inversion Test (CIT). AIT's semantic content preserved + refined in CIT.

**Rigor provenance:** see CIT record + 3 ratified rigor passes (Commons-as-Structural-Identity + CIT rename + 10-list dissolution).

**Notes:**
- Phase A3 Stream A sweep target: ~100+ active AIT refs across framework (chapters + Tech Appendix + glossary + rigor passes + case studies + decision docs) — Tier-1 sweep per Principle #4.
- Historical docs (older rigor passes, session handoffs): Tier-2 retirement-note headers; no content sweep.

---

### Abundances → Commons Categories (10-element example record) — UPDATED 2026-04-24

**Working definition (v1.2 — supersedes v1.1 from earlier-this-session Abundances pass):** The 10 commons categories the framework has examined across the 18 cases of this book's research: Habitability · Spatial · Temporal · Institutional · Kindred · Ecosystem · Political · Cohesion · Epistemic · Autonomy. **These are EXAMPLES, not a canonical or exhaustive enumeration.** Each names a commons whose abundance state CIT can invert to reveal scarcity-grounded costs. "Abundance" is the STATE of each commons (abundant vs scarce), not the commons itself.

**Status:** `CURRENT` as **examples-record reference** at Ring 2 (ratified 2026-04-24 by Chris Winn — Option C' middle path with political-philosophical acknowledgment).

**Term-spec version:** v1.2 (supersedes v1.1 "scaffolding construct" framing → "examples-record reference" per Option C' refinement).

**Last reviewed:** 2026-04-24

**Key reframing (Option C' specific):**
- The 10 are NOT framework scaffolding (load-bearing architecture).
- The 10 ARE framework EXAMPLES — what CIT has surfaced across the 18 cases examined.
- Framework's UNIVERSALITY claim is about METHODOLOGY (CIT works wherever extraction operates on commons-like resources), NOT about enumeration canonicity.
- Different political traditions have different commitments about what IS a commons; the framework accommodates rather than settles this contestation.
- Reader application may surface different or additional commons categories in their context; framework is generative + politically-pluralistic.

**Rigor provenance:**
- Path F rigor pass — variables-not-dimensions reframing.
- Naming-cohort rigor passes 2026-04-22 (per-element rigor) preserved.
- Commons-as-Structural-Identity rigor pass (commit `c4b09dc`) — abundances → commons categories.
- 10-Commons-List Dissolution rigor pass (commit `e30087e`) — Option C' ratified: examples-not-canonical + political-philosophical acknowledgment.

**Political-philosophical acknowledgment (load-bearing for Ch 1 + Tech Appendix):**

What counts as a commons is politically-traditionally contested:
- **Classical liberalism** — autonomy as individual natural-right; supporting infrastructure enabling but not commons.
- **Civic republicanism** (Pettit/Skinner) — autonomy as non-domination; requires shared institutions; commons-like dependence.
- **Socialist/communitarian** — autonomy as enabled by shared infrastructure; the enabling conditions ARE commons.
- **Marxist** — autonomy material-conditions dependent.
- **Lived-oppression perspective** (slave, colonized, repressed worker) — autonomy as something denied/extracted, not shared commons.
- **Dominant-class perspective** — autonomy as individual privilege.

Framework doesn't argue universal ontology of what IS a commons. Argues: when any of these operate AS commons in a given society, extraction severs cost from that commons; CIT measures the severance. **Universality of method, examples of application, political-traditional-agnosticism on specific commons-ontology.**

Politically-contested commons especially: Autonomy (Anderson 2017 *Private Government* civic-republican framing); Political (rules of voice + representation contested); Kindred (Western nuclear vs collectivist kinship norms contested); Epistemic (knowledge-as-commons vs knowledge-as-property contested).

**Why Ring 2 (not Ring 1):** examples-record reference is framework-internal; not a public-adoption target.

**Recommended authorial-voice positioning** (for Ch 1 / Ch 6):
> *"This framework doesn't argue that autonomy is universally a commons, or that habitability is, or that time is. It argues that when any of these operate AS commons in a given society — shared, depended-on, collectively enabling — extraction can sever cost from that commons, and this methodology measures the severance. Different political traditions have different commitments about what is shared and what is individual. The framework works within any of those commitments. What it doesn't accept is extraction without accountability, regardless of which commons is being extracted from."*

**Depends on:**
- CIT methodology (operates on examples).
- Path F generative framework architecture.
- Per-commons rich profiles (preserved in methodology doc v1.4.0).
- Bibliography commons-governance lineage (Ostrom + Hess + Klinenberg + Anderson + Polanyi).

**Pairs with:**
- CIT (Ring 1) — examples illustrate methodology.
- Abundance Masking (Ring 2) — operates across commons examples.
- Cᵢ (Ring 1) — admitted via CIT operating on commons.

**Staleness triggers:**
- Commons-as-structural-identity reversed.
- New examples surfaced via CIT framework application.
- Political-philosophical positioning challenged in academic reception.

**Commit trail:**
- Commons-as-Structural-Identity pass: commit `c4b09dc`.
- 10-list dissolution pass: commit `e30087e`.
- Ratification + Terms Index update: this commit.

**Notes:**
- Phase A3 Stream A sweep targets: glossary v3 → "Commons categories (examples)" entry; methodology doc rename v1.3.0 → v1.4.0; chapter audit + case-study audit framed as reproducibility record (preserved); Ch 6 restructured methodology-forward.
- Per-commons rich profiles (v1.2.0 naming-cohort work) preserved in methodology doc — NOT chapter prose. Per Open Insight #13 (scope-creep monitoring), per-commons depth = Tech Appendix not chapters.
- Autonomy-as-commons specifically gets explicit political-philosophical acknowledgment in Ch 1 + Ch 6 + Tech Appendix per Open Insight #18.

---

### Cost Severance Damages (CSD)

**Working definition:** Backward-looking framework instrument measuring realized human harm from cost severance — health damages, intergenerational disadvantage, community-level suffering, foreclosed life-trajectories. Distinct from RCV (forward-looking resource permanent-foreclosure measurement). The framework's two-instrument architecture (per Three Ways + RCV Formal-Model rigor pass Block 1, ratified 2026-04-24): CSD measures damages-to-people; RCV measures damages-to-resource. Together they constitute Total Extraction Damages.

**Status:** `CURRENT` at Ring 2 (ratified 2026-04-24 by Chris Winn).

**Term-spec version:** v1.0 (first sanctioned spec; supersedes implicit-operation status across 7+ framework cases).

**Last reviewed:** 2026-04-24

**Rigor provenance:**
- Three Ways + RCV Formal-Model rigor pass Block 1 (commit `1c8e4dd`, 2026-04-24) — surfaced CSD as hidden Ring-2 element via two-instrument architecture.
- Three Ways + RCV Formal-Model ratification (commit `66becc5`, 2026-04-24) — promotion commissioned by Chris Winn directive.
- CSD individual rigor pass `tools/rigor-passes/commons_bonds_rigor_pass_2026-04-24_term_csd_v1.0.0.md` (commit `98fc8e6`, 2026-04-24) — Option A (Ring 2) ratified by Chris Winn 2026-04-24 with Principle-#3 distinctness check + M12 audit + 7-case implicit-operation evidence.

**M12 classification:** Independent specialization with established-methodology lineage. Adopts reparations-economics (Darity & Mullen 2020) wealth-gap-against-comparable-households methodology + VSL/DALY health-economics + intergenerational-mobility (Chetty et al.) + extends into extraction-community contexts via two-instrument architecture.

**M12 citations (LOAD-BEARING for Tech Appendix):**
- Darity, William A., Jr., & Mullen, A. Kirsten. *From Here to Equality* (UNC Press 2020) — already in bibliography §18.5.
- Bullard, Robert D. *Dumping in Dixie* (Westview 1990) — already in bibliography §7. Environmental-justice cross-reference.
- Chetty, Raj, et al. — already in bibliography §4. Intergenerational-mobility cross-reference.
- VSL/DALY methodology references — Tech Appendix v0.0.5.

**Why Ring 2 (not Ring 1):**
- Framework-internal architecture; readers learn it; non-readers don't adopt CSD as travel-ready vocabulary.
- Adoption-bet focus on Ring-1 flagships (Commons Bonds + Cost Severance + Severed Cost + Value Extraction + RCV + Cᵢ + CIT) preserved.

**Why Ring 2 (not subsumed under Cost Severance / Severed Cost):**
- Cost Severance = mechanism noun; Severed Cost = quantified result noun; CSD = specific measurement instrument for the human-harm component of result. Three different conceptual layers; instrument-layer warrants separate record.

**Implicit operation in framework cases (7 demonstrated; preserved in CSD rigor pass §2.2):**
- McDowell coal — life-expectancy gap, Black Lung, community-collapse mortality, intergenerational mobility loss
- Healthcare end-of-life — family-caregiver labor-time, patient-suffering, financial depletion
- Opioid Appalachia — overdose deaths, family destruction, multi-generational trauma, foster-care overload
- 2008 financial crisis — 10M foreclosures, retirement-cohort wealth destruction, racial wealth-gap effects
- Chesapeake watermen — multi-generational livelihood-loss, community-cohesion erosion
- Libby vermiculite — multi-decade asbestos health damages
- Tax-tradeoff (US-Sweden) — welfare-state-architecture-driven life-outcome disparities

**Pairs with:**
- RCV (Ring 1) — companion forward-looking instrument; orthogonal measurement (Block 1 Hole 5: full reparations leave the resource still gone).
- B1 (Restitution Bond, Ring-2 sub-instrument; ratified 2026-04-24 per B1 + B2 naming rigor pass commit `8e6a5b2`) — accountability instrument that closes CSD gap.
- Cost Severance (Ring 1) — mechanism CSD measures damages from.
- Severed Cost (Ring 1) — quantified result; CSD is the backward-looking measurement of its human-harm component.
- Total Extraction Damages = CSD + uncaptured RCV (Block 3 framework decomposition).

**Staleness triggers:**
- Two-instrument architecture (Block 1) reversed.
- CSD methodology displaced by superior measurement framework.
- Reparations-economics field develops a different framing that supersedes wealth-gap-against-comparable-households methodology.

**Commit trail:**
- Three Ways + RCV Formal-Model pass: commit `1c8e4dd`.
- Three Ways + RCV Formal-Model ratification + bibliography additions: commit `66becc5`.
- CSD individual rigor pass: commit `98fc8e6`.
- Ratification + Terms Index record: this commit.

**Open Insights:**
- **Open Insight #19** (CSD-RCV correlation hypothesis) — the framework's deepest empirical claim that CSD and uncaptured RCV correlate across extraction cases; remains hypothesis pending Block 4 validation execution.

**Notes:**
- CSD is the framework's most-empirically-validated measurement instrument — reparations-economics + environmental-justice + health-economics traditions have decades of methodology development.
- Norway's welfare-state architecture is approximately B1-for-Norwegian-citizens; framework's CSD measurement of climate-extraction damages on non-Norwegian populations remains uncompensated.
- Phase A3 sweep targets: Ch 5 prose; Tech Appendix v0.0.5 formalism; Glossary v3 entry.

---

### Hotelling Identity (framework's extension of Hotelling 1931)

**Working definition:** The framework's articulation that the gap between commons' true cost of extraction (RCV) and extractor's market-priced scarcity premium (Hotelling rent) IS, by definition, the per-unit Cost Severance: **RCV − Hotelling rent = Cost Severance per unit.** Bridge between framework vocabulary and standard resource-economics math.

**INTELLECTUAL HONESTY — clear attribution of components (per author M12 directive 2026-04-24):**

- **Hotelling's part** (Hotelling 1931): resource rent = market price − extraction cost (p − c); the rent rises over time at rate of interest; this rent represents the EXTRACTOR's scarcity premium accruing as the resource depletes. Standard resource-economics; foundational.
- **Framework's part:** (a) defining RCV as the COMMONS' true cost of extraction (forward-looking; integrand over substitutability + externality + abundance-grounded costs admitted via Four Gates); (b) recognizing that Hotelling rent under honest accounting represents commons' scarcity value being APPROPRIATED by extractor (rather than compensated to the commons); (c) articulating the identity: RCV − Hotelling rent = CS per unit. The identity is framework's articulation; Hotelling didn't write it (didn't have RCV; didn't have Cost Severance as named mechanism).

The framework EXTENDS Hotelling 1931 by adding a commons-side measurement to pair with Hotelling's extractor-side rent + naming the gap as the framework's central concept (Cost Severance).

**Status:** `CURRENT` at Ring 2 (ratified 2026-04-24 by Chris Winn with explicit extension-positioning discipline).

**Term-spec version:** v1.0.

**Last reviewed:** 2026-04-24

**Rigor provenance:**
- Three Ways + RCV Formal-Model rigor pass Block 3 (commit `1c8e4dd`) — Hotelling Identity surfaced.
- Three Ways + RCV Formal-Model ratification (commit `66becc5`) — promotion commissioned.
- Hotelling Identity individual rigor pass `tools/rigor-passes/commons_bonds_rigor_pass_2026-04-24_term_hotelling_identity_v1.0.0.md` (commit `5b8ff42`) — Option A (Ring 2 promote) with §3.2 Tech Appendix specification framing for the appropriated-commons-value interpretation.
- Author M12 challenge round 1 (2026-04-24): *"note 'Hotelling Identity' isn't my idea it's Hotelling, correct? we are just citing it and leveraging it within our formula."*
- Author M12 resolution round 2 (2026-04-24): *"ratify = Hotelling Identity Ring 2 promotion... but again, it's not my work so just cite it and then use it and call out how my work extends / adds to his work."*
- Ratification 2026-04-24 by Chris Winn — this commit. Ring 2 promotion ratified WITH extension-positioning discipline.

**M12 classification:** Independent specialization with foundational lineage extension. Hotelling 1931 is the foundation (clearly attributed); framework's identity-articulation + RCV-as-Hotelling-complementary-measurement is the extension (clearly attributed). NOT framework coinage of the underlying resource-rent concept.

**M12 citations (LOAD-BEARING):**
- **Hotelling, Harold. "The Economics of Exhaustible Resources." *Journal of Political Economy* 39, no. 2 (1931): 137–175.** — foundational; in bibliography §18.5.

**Optional Tech Appendix depth additions:**
- Solow 1974 — intergenerational equity and exhaustible resources.
- Hartwick 1977 — invest resource rents in reproducible capital (Norway sovereign-fund operationalization).
- Pearce-Atkinson 1993 — sustainability accounting / capital-theory extension.
- Daly's stock-flow accounting — already in bibliography §3.

**Why Ring 2 (not Ring 1):**
- Mathematical bridge, not adoption-target vocabulary.
- Lawyers + policymakers don't adopt mathematical identities directly; they adopt the framework concepts (Severed Cost; Cost Severance; Commons Bonds) the identity supports.

**Why Ring 2 with extension-positioning discipline:**
- Ring 2 placement honors the identity's M6 academic-positioning value (transforms M11 critic's *"isn't this rebranding externality theory?"* attack into structural identification).
- Extension-positioning honesty (Hotelling's part vs framework's part clearly attributed in this record + Tech Appendix passage) prevents the overclaim that the framework "coined" Hotelling's foundational work.
- Bibliography Hotelling 1931 entry is correct attribution at scholarly level.

**Pairs with:**
- RCV (Ring 1) — numerator in identity; framework's measurement.
- Hotelling rent (resource-economics term; Hotelling 1931) — subtractend; clearly Hotelling's contribution.
- Cost Severance equation CS = RCV − B (Ring 2) — Hotelling Identity is the per-unit specialization for standard-economics framing.
- Cost Severance mechanism (Ring 1) — what the identity ultimately characterizes per-unit.

**Tech Appendix v0.0.5 publication required:**
- Hotelling 1931 lineage citation + clear attribution.
- Per-unit per-period form: RCV(t) − Hotelling-rent(t) = CS(t).
- Integrated form: ∫RCV(t) dt − ∫Hotelling-rent(t) dt = ∫CS(t) dt.
- Hotelling-rent-as-appropriated-commons-value interpretive passage: under honest accounting, Hotelling rent represents commons' scarcity value being appropriated by extractor rather than compensated to commons.
- Framework-extends-Hotelling positioning (Hotelling's part + framework's part clearly attributed).

**Staleness triggers:**
- Hotelling 1931 framework displaced in resource economics (not expected; foundational status).
- Framework restructures CS equation in ways that change identity form.
- Tech Appendix specification reveals identity holds only under restricted assumptions.

**Commit trail:**
- Three Ways + RCV Formal-Model pass: commit `1c8e4dd`.
- Three Ways ratification + Hotelling 1931 added to bibliography: commit `66becc5`.
- Hotelling Identity individual rigor pass: commit `5b8ff42`.
- Ratification + Terms Index record: this commit.

**Notes:**
- The identity transforms M11 critic's "rebranding externality theory" attack into structural identification — framework asserts the algebraic complement to Hotelling 1931.
- M6 academic-positioning value is high; extension-positioning discipline preserves the value while honestly attributing components.
- Captured lesson (per Hotelling Identity rigor pass §8): when ratifying Ring placement for elements that EXTEND established work, Terms Index records must explicitly distinguish (a) foundational component cited and (b) framework's specific contribution. This protects against accidental over-claim while preserving framework's legitimate extension contribution.

---

### Triangulated RCV Estimation ("Three Ways of Counting" pedagogically)

**Working definition:** Three-method estimation methodology for RCV producing a defensible range rather than a single point estimate. Method 1 (Replacement Cost lower bound) + Method 2 (Norway Revealed Preference middle-anchor within triangulation) + Method 3 (Scarcity-Adjusted Option Value upper bound). Convergence reduces uncertainty; divergence reveals where real disagreements live (substitutability vs scarcity-rate vs option-value parameter dominance).

**Status:** `CURRENT` at Ring 2 (ratified 2026-04-24 by Chris Winn).

**Term-spec version:** v1.0.

**Last reviewed:** 2026-04-24

**Rigor provenance:**
- Three Ways + RCV Formal-Model rigor pass Block 2 (commit `1c8e4dd`) — methodology surfaced.
- Three Ways + RCV Formal-Model ratification (commit `66becc5`) — promotion commissioned.
- Triangulated RCV Estimation individual rigor pass `tools/rigor-passes/commons_bonds_rigor_pass_2026-04-24_term_triangulated_rcv_estimation_v1.0.0.md` (commit `4f48c48`) — Option A (Ring 2 promote) verified with three method sub-tests + triangulation-discipline check + integration check.
- Ratification 2026-04-24 by Chris Winn — this commit.

**M12 classification:** Independent specialization within established estimation methodology traditions. Each method adopts standard methodology; triangulation discipline is standard validation. Framework's contribution is the SPECIFIC THREE METHODS chosen + convergence/divergence diagnostic + integration with Two-Instrument Architecture (CSD ↔ B1; RCV ↔ B2).

**M12 citations:**
- Costanza, Robert, et al. *Nature* 1997 — Method 1 replacement-cost methodology lineage. (Optional Tech Appendix addition.)
- Hartwick 1977 + Solow 1974 — Method 2 Hartwick-rule + intergenerational-equity lineage. (Optional Tech Appendix addition.)
- Dixit & Pindyck 1994 — Method 3 real-options-theory foundation. Already in bibliography §16.
- Hotelling 1931 — used in Tech Appendix discussion of how RCV connects to standard resource economics; CITED not promoted as framework element. Already in bibliography §18.5.

**Sub-records (Methods 1, 2, 3) preserved within parent record below:**

#### Method 1 — Replacement Cost (Lower Bound)
- *Methodology:* RCV_min per unit ≥ replacement cost from nearest substitute − market price at extraction.
- *Boundary checks:* sand → low; helium → severe (correct directional differentiation).
- *M12 lineage:* Costanza 1997 ecosystem-services valuation + standard regulatory cost-benefit analysis + eminent-domain takings law.

#### Method 2 — Norway Revealed Preference (Middle-Anchor within Triangulation)
- *Methodology:* Norway fund value ÷ total barrels extracted = per-barrel captured value; for any comparison case, gap = Empirical measure of uncaptured RCV.
- *Sidesteps the discount-rate debate* (empirical not philosophical).
- *Per Open Insight #14 epistemic-humility ratification:* Norway didn't fully capture RCV either (climate damages externalized; future-uses option-value uncaptured). Method 2 functions as Norway-anchored MIDDLE within the triangulation (Method 1 ≤ Method 2 ≤ Method 3 ≤ true RCV); not absolute middle of true RCV.
- *M12 lineage:* Hartwick rule 1977 + Solow 1974 + revealed-preference economics tradition.

#### Method 3 — Scarcity-Adjusted Option Value (Theoretical Upper Bound)
- *Methodology:* Real-options theory (Dixit-Pindyck 1994) specialized for declining substitutability + future-use uncertainty. Parameters σ + α + V_option.
- *Tech Appendix v0.0.5 specification REQUIRED:* mathematical specification, parameter calibration approach, upper-bound rationale.
- *M12 lineage:* Dixit-Pindyck 1994 (already in bibliography); real-options applications in natural-resource extraction (Brennan-Schwartz 1985); option-pricing foundation (Black-Scholes 1973).

**Why Ring 2 (not Ring 1):**
- Mathematical methodology, not adoption-target vocabulary.
- Readers learn methodology; non-readers adopt framework concepts (Severed Cost; CS), not estimation methodologies.

**Pairs with:**
- RCV (Ring 1) — the quantity estimated.
- Four Gates (Ring 2) — admit costs first; estimate value second.
- CSD (Ring 2) — companion two-instrument-architecture estimation (different methodology — reparations economics rather than triangulated).
- Substitutability Function S (Ring 2) — appears in Method 3 formal model.

**Convergence-table pedagogy** (Ch 6 numerical center-of-gravity per IPG rigor pass): 4 approaches converge on IPG ≫ 1 across cases. Tech Appendix v0.0.5 should clarify whether 4-approaches reference is Methods 1+2+3 + Hotelling-citation cross-check OR Methods + CSD-RCV correlation cross-check (Block 1 cross-validation idea).

**Methodology naming decision (ratified 2026-04-24):**
- "Triangulated RCV Estimation" — formal name (Tech Appendix).
- "Three Ways of Counting" — pedagogical name (Ch 6 chapter title; preserves M5 dinner-table accessibility).
- Both forms ratified; different audiences.

**Open Insight #20** (sensitivity-analysis execution σ + α + V_option dominance) opened for Tech Appendix v0.0.5 publication.

**Staleness triggers:**
- Block 4 validation execution reveals methods don't converge on test cases.
- New estimation methodology emerges that displaces one of the three.
- Sensitivity-analysis reveals one parameter dominates such that triangulation provides no value.

**Commit trail:**
- Three Ways + RCV Formal-Model pass: commit `1c8e4dd`.
- Three Ways ratification + bibliography additions: commit `66becc5`.
- Triangulated RCV Estimation individual rigor pass: commit `4f48c48`.
- Ratification + Terms Index record: this commit.

---

### Accountability Bond — UPDATE: B = B1 + B2 decomposition (v1.2 — final sub-instrument names ratified)

**Working definition update (v1.2, supersedes v1.1 working-label sub-instrument names):** Aggregate framework instrument B = B1 + B2 closing the Cost Severance gap (CS = RCV − B at aggregate level; expanding via two-instrument architecture: total CS = (CSD − B1) + (RCV − B2)). Sub-decomposed into **B1 (Restitution Bond, backward-looking, pairs with CSD) and B2 (Foreclosure Bond, forward-looking, pairs with RCV)**. Final sub-instrument names ratified 2026-04-24 via dedicated B1 + B2 naming rigor pass.

**Status:** `CURRENT` at Ring 2 (aggregate ratified 2026-04-24 by Chris Winn; v1.1 update with B = B1 + B2 decomposition ratified 2026-04-24; v1.2 update with final sub-instrument names ratified 2026-04-24).

**Term-spec version:** v1.2 (aggregate v1.0 + B = B1 + B2 decomposition v1.1 + final sub-instrument names v1.2; Ring 2 status preserved).

**Last reviewed:** 2026-04-24.

**Rigor provenance update:**
- Original Accountability Bond rigor pass (commit `7fa1c1b`) — aggregate Ring-2 ratified.
- Three Ways + RCV Formal-Model pass §7.3 (commit `1c8e4dd`) — surfaced B = B1 + B2 decomposition via Block 1 two-instrument architecture.
- Three Ways + RCV Formal-Model ratification (commit `66becc5`) — decomposition rigor pass commissioned.
- B1/B2 decomposition individual rigor pass `tools/rigor-passes/commons_bonds_rigor_pass_2026-04-24_b1_b2_decomposition_v1.0.0.md` (commit `ab24a8e`) — Option A (decomposition ratified) verified with equational consistency check + per-sub-instrument M12 audit.
- B1 + B2 naming rigor pass `tools/rigor-passes/commons_bonds_rigor_pass_2026-04-24_b1_b2_naming_v1.0.0.md` (commit `8e6a5b2`) — Restitution Bond + Foreclosure Bond ratified over working labels (Reparations Bond + Resource-Foreclosure Bond).
- Aggregate decomposition ratification 2026-04-24 by Chris Winn (commit `56b5fd4`) — B = B1 + B2 + Open Insight #14 refinement.
- Final names ratification 2026-04-24 by Chris Winn — this commit.

**Equational consistency:** CS = RCV − B holds aggregately; decomposed: total CS = (CSD − B1) + (RCV − B2) = TED − B (Total Extraction Damages minus Total Accountability Bond). Boundary-case instruments (spanning both) decomposed by component.

#### B1 — Restitution Bond (Ring-2 sub-instrument)

**Working definition:** Backward-looking accountability-instrument cluster that closes the CSD gap. Mechanisms restoring (in monetary, legal, structural, or rights-based form) what was taken from people via cost severance — restitution payments, reparations programs, welfare-state instruments (universal healthcare, social-safety-net programs, public pensions), environmental-justice damages compensation, toxic-tort litigation, class-action damages, truth-and-reconciliation processes. Pairs with CSD in two-instrument architecture.

**Why "Restitution" over "Reparations" (per B1 + B2 naming rigor pass commit `8e6a5b2`):** legal-register-clear; cross-political-tradition adoption potential. "Reparations" carries political-loading that narrows framework adoption to politically-progressive audiences; "Restitution" preserves the same restoration-of-what-was-taken meaning while reaching center-right + libertarian + politically-cautious institutional audiences who'd disengage at "Reparations." Per Option C' political-philosophical-accommodation discipline (ratified 2026-04-24): framework accommodates political traditions rather than asserts politically-loaded commitments. Restitution-law scope is BROADER than damages-law (encompasses monetary + legal + structural + rights-based restoration); fits CSD's broader scope than narrow damages.

**M12 lineage:**
- Restitution-law tradition (general legal vocabulary; not citation-specific).
- Darity, William A., Jr., & Mullen, A. Kirsten. *From Here to Equality* (UNC Press 2020) — primary reparations economics methodology source. Already in bibliography §18.5.
- Bullard, Robert D. *Dumping in Dixie* (Westview 1990) — environmental-justice damages cross-reference. Already in bibliography §7.
- Toxic-tort + class-action damages tradition (legal-economics lineage).
- Truth and Reconciliation processes (South Africa post-apartheid + analogous infrastructures).
- Esping-Andersen, *The Three Worlds of Welfare Capitalism* (Princeton 1990) — welfare-state design lineage (optional Tech Appendix addition).

**Status of B1 globally:** UNDERDEVELOPED. Restitution-and-reparations is the active scholarly territory; less politically settled than B2; varies widely across welfare-state architectures; environmental-justice damages compensation is litigation-driven and incomplete.

**Pairs with:** CSD (Ring 2); aggregate Accountability Bond; Cost Severance mechanism (Ring 1).

#### B2 — Foreclosure Bond (Ring-2 sub-instrument)

**Working definition:** Forward-looking accountability-instrument cluster that closes the RCV gap. Mechanisms internalizing resource permanent-foreclosure value — Hartwick savings (sovereign wealth funds), reclamation bonds, Environmental Impact Bonds, Pigouvian carbon taxes, cap-and-trade schemes, decommissioning bonds. Pairs with RCV in two-instrument architecture.

**Why "Foreclosure Bond" over "Resource-Foreclosure Bond" (per B1 + B2 naming rigor pass commit `8e6a5b2`):** **term-pair coherence with Foreclosure Cost (C₁ in RCV integrand)** — *"Foreclosure Cost is what's lost; Foreclosure Bond is what would internalize it."* Shorter; preserves descriptive content via framework context; M5 dinner-table strong via mortgage-foreclosure analogy (in mortgage-foreclosure, ownership permanently severed from borrower; in resource-foreclosure, future-use permanently severed from future generations).

**Norway = canonical existing B2 exemplar** (specifically — operationalizes Hartwick rule 1977 via sovereign-wealth-fund). Refines Open Insight #14: Norway's GPFG is canonical B2, NOT canonical aggregate B; Norwegian welfare-state is approximately B1-for-Norwegian-citizens but doesn't extend to non-Norwegian populations affected by Norwegian oil's climate externalities.

**M12 lineage:**
- Hotelling, Harold. *Journal of Political Economy* 1931 — already in bibliography §18.5. Foundational resource-economics; Hotelling rent under honest accounting flows to B2 instrument.
- Hartwick rule 1977 — invest resource rents in reproducible capital. Norway sovereign-fund operationalizes (optional Tech Appendix addition).
- Solow 1974 — intergenerational equity and exhaustible resources (optional Tech Appendix addition).
- OSMRE Reclamation Bonds + GAO-17-207R + Yang & Davis 2021 — already in bibliography §15. Reclamation bond literature.
- Balboa 2016 *Accountability of Environmental Impact Bonds* — already in bibliography §15.
- Pigou 1920 *Economics of Welfare* — already in bibliography §17. Pigouvian-tax tradition.

**Pairs with:** RCV (Ring 1); Foreclosure Cost C₁ (term-pair coherence — what the bond internalizes); aggregate Accountability Bond; Hotelling 1931 framing; Norway case study.

**Aggregate B notes (v1.1 update):**
- Phrase-travel-monitoring flag (Open Insight #11) preserved at aggregate level.
- Scope-creep-monitoring flag (Open Insight #13) preserved + applies to both sub-instruments.
- Two-readership adoption opportunity surfaced: B2-conversation (resource-economics + sustainability-finance audiences); B1-conversation (justice-economics + political-philosophy audiences).
- Open Insight #14 refined: Norway = canonical existing B2 exemplar; B1 globally underdeveloped.

**Phase A3 sweep targets:**
- Ch 5 (accountability gap) — two-instrument architecture framing.
- Ch 9 (policy economy) — two distinct instrument-design conversations named.
- Tech Appendix v0.0.5 — B = B1 + B2 decomposition section + per-sub-instrument formalism.
- Glossary v3 — B1 + B2 sub-entries.
- Open Insight #14 update — Norway-as-B2-canonical refinement.

---

*End of Term Provenance Index v0.1.0. Skeleton established 2026-04-24. Populated progressively as Tier A rigor work produces records.*
