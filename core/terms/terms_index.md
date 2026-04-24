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

### Asymmetric Regret Principle (ARP)

**Working definition:** Framework-specific operational decision rule — when RCV tails cannot be precisely quantified, default to the reversible option. "We can always extract later. We can never un-extract." Specialization of Savage-style minimax-regret applied to resource-extraction decisions under quantification uncertainty. Bidirectional-flip-by-context — directs extract-aggressively (Comet flyby case: access window closes) OR preserve (Europa case: incommensurable externality) depending on which action is reversible.

**Status:** `CURRENT` at Ring 2 (ratified 2026-04-24 by Chris Winn — promoted from meta-pass §13.2.c DEFERRED status).

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

*End of Term Provenance Index v0.1.0. Skeleton established 2026-04-24. Populated progressively as Tier A rigor work produces records.*
