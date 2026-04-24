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

---

## §4. Established records

*(Records below are populated as rigor passes land. Each record's body summarizes the pass's verdict; full pass documents live at `tools/rigor-passes/`.)*

*(None yet. First records land with the Variable-vs-Cost rigor pass.)*

---

*End of Term Provenance Index v0.1.0. Skeleton established 2026-04-24. Populated progressively as Tier A rigor work produces records.*
