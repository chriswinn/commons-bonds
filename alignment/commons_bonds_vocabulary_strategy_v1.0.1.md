# Commons Bonds — Vocabulary Strategy

**Version:** 1.0.1
**Established:** 2026-04-28
**Status:** **RATIFIED 2026-04-28 by Chris Winn** — v1.0.1 incorporates ratified refinements per `commons_bonds_rigor_pass_2026-04-28_vocabulary_decision_framework_shape_v1.0.0.md`: (a) §5 D-modulation guidance covers engineered-for-adoption-travel design intent; (b) §4 includes supplementary decision-tree representation; (c) §10 case-study selection deferred (audience for scaffolding doc is Chris + AI assistants — case studies serve future-AI pattern-matching but the per-term rigor passes themselves are the canonical examples; explicit selection deferred).
**Author:** Chris Winn

**Purpose:** Standing reference for vocabulary decisions on the *Commons Bonds* project. Codifies the discipline that flows from the ratified book-level audience (Option B + supplementary D, RATIFIED 2026-04-28). Future vocabulary decisions inherit this discipline without re-running the audience or methodology rigor passes.

This document sits alongside `commons_bonds_working_principles_v1.0.0.md` as a parallel discipline-record. Where Working Principles captures the *general project disciplines* (parsimony, retirement-traces, named-rule criterion, etc.), this document captures the *vocabulary-specific discipline* — when to coin, when to borrow, when to use prose, how to suffix, how to capitalize, how to record the decision.

---

## §0. Why this file exists

Per author articulation 2026-04-28: *"let's capture the resulting solution/approach that we decide on in a scaffolding document like core/terms/terms_index.md"* — i.e., not just produce a one-off rigor-pass verdict but a standing reference that future vocabulary decisions inherit from. The intent: future framework vocabulary decisions answer the question *"what tier? what suffix? what register?"* by consulting this document, not by re-running the rigor-pass methodology each time.

The discipline operates at two levels:

1. **Standing input.** The ratified book-audience (B + supplementary D) is the fixed input to every vocabulary decision. New terms, term renames, suffix questions, capitalization questions all evaluate against this single inherited audience profile.
2. **Standing output.** Once a vocabulary decision is made under this discipline, the decision is recorded in `core/terms/terms_index.md` per the architecture-rigor-pass S1 schema (rendering fields per term). This document specifies the format + cross-references.

Failure mode this prevents: per-term audience juggling. Earlier methodology drafts treated audience as a per-term variable, which produced inconsistent vocabulary register across the book. The book-level-audience-first discipline (codified here) prevents that drift.

---

## §1. Scope + cross-references

### §1.1 What this document governs

- New framework vocabulary coinage decisions (when to coin, when not to)
- Existing-term renaming decisions
- Suffix-convention questions (which ending; -Cost vs -Burden vs -Levy etc.)
- Capitalization decisions (proper-noun vs lowercase descriptive)
- Tier A/B/C/D classification decisions per term
- Per-occurrence usage decisions (load-bearing vs decorative; KEEP vs REPLACE)

### §1.2 What this document does NOT govern

- Book-level audience (governed by `tools/rigor-passes/commons_bonds_rigor_pass_2026-04-28_book_audience_choice_v1.0.0.md` — RATIFIED 2026-04-28)
- General-project disciplines (governed by `commons_bonds_working_principles_v1.0.0.md`)
- Term-record schema (governed by architecture rigor pass `commons_bonds_rigor_pass_2026-04-27_publication_architecture_terms_index_glossary_tech_appendix_v1.0.0.md`)
- Retirement-trace handling (governed by `commons_bonds_rigor_pass_2026-04-28_retirement_traces_scaffolding_vs_publisher_facing_v1.0.0.md` once ratified)
- Decision-rule rigor protocol (governed by `tools/commons_bonds_rigor_protocol_v2.3.0.md`)

### §1.3 Cross-references — load-bearing rigor passes

- `tools/rigor-passes/commons_bonds_rigor_pass_2026-04-28_book_audience_choice_v1.0.0.md` — ratified book-level audience (the fixed input to this document)
- `tools/rigor-passes/commons_bonds_rigor_pass_2026-04-28_intergenerational_cluster_vocabulary_consolidation_v1.0.0.md` — applied rigor pass producing the per-term verdicts that this document distills into standing discipline
- `tools/rigor-passes/commons_bonds_rigor_pass_2026-04-27_publication_architecture_terms_index_glossary_tech_appendix_v1.0.0.md` — S1 schema for per-term records in `core/terms/terms_index.md`
- `tools/rigor-passes/commons_bonds_rigor_pass_2026-04-24_term_value_capture_vs_extraction_v1.0.0.md` (and analogous per-term rigor passes) — historical record of past per-term decisions; cross-referenced from worked examples

---

## §2. Inherited fixed input — book-level audience

### §2.1 Ratified verdict

Per `commons_bonds_rigor_pass_2026-04-28_book_audience_choice_v1.0.0.md` (RATIFIED 2026-04-28 by Chris Winn):

> **Option B (academic-trade hybrid) primary register + Option D (policy-practitioner) supplementary register in adoption-travel chapters (Ch 9 *Pricing Honestly* canonical; Ch 7 instrument-design sections; Ch 10 regulatory-architecture sections).**

### §2.2 The B-register reader profile

The audience-of-record for every vocabulary decision in this document:

- **Reading background:** non-economics-degree, but engaged generalist. Reads Mazzucato (*Mission Economy*, *The Value of Everything*), Raworth (*Doughnut Economics*), Sen (*The Idea of Justice*), Anderson (*Private Government*), Acemoglu + Robinson (*Why Nations Fail*), Hickel (*Less Is More*), Stiglitz (*The Price of Inequality*).
- **Comfort with apparatus:** willing to track ~10-20 named framework objects across the book; willing to engage with equations when they're load-bearing on the chapter's argument; willing to follow lineage citations when they're non-distracting.
- **Discomfort triggers:** specialist gloss without payoff; jargon with no explanation; framework coinage that doesn't earn its keep; lineage citations that read as name-dropping; mathematical apparatus that reads as performance rather than work.
- **Approval signals:** clear naming that encodes what the term does; explicit lineage citations that situate the framework in established intellectual traditions; case studies that anchor abstract claims; emotional resonance that doesn't sacrifice rigor.

### §2.3 The D-modulation reader profile (for adoption-travel chapters)

In chapters where the success-criterion is severed-cost migrating into legal/policy text — Ch 9, Ch 7 instrument-design sections, Ch 10 regulatory-architecture sections — the audience-of-record extends to include:

- **Reading background:** policy-practitioner / regulatory-vocabulary-fluent reader. Reads Tooze (*Crashed*), Brookings policy briefs, Roosevelt Institute reports, Bernstein, Gabor + Ban, Hockett, Omarova.
- **Comfort with apparatus:** higher tolerance for instrument-design specificity; expects regulatory-text vocabulary; expects quantification of policy outcomes.
- **Discomfort triggers:** vague claims; conceptual framework without instrument-design specificity; missing quantification.
- **Approval signals:** instrument-design clarity; vocabulary that can migrate into regulatory text without translation; explicit success metrics.

### §2.4 What "inherited fixed input" means operationally

Every vocabulary decision in this document — the four moves (A/B/C/D), the suffix convention, the capitalization discipline, the per-occurrence usage rules — evaluates against the B-register reader as the primary audience-of-record, with D-modulation reader as the secondary audience-of-record in adoption-travel chapters.

Per-term audience juggling is out of scope. The audience is a property of the book (and chapter-register), not a property of each term.

---

## §3. The four vocabulary moves — Tier A / B / C / D

### §3.1 Definitions

The framework's vocabulary discipline recognizes four moves:

**Tier A — Adopt established academic-literature term verbatim with citation.**
Use when an existing academic-literature term captures the framework's intended meaning exactly AND lands cleanly with the B-register reader without specialist gloss. Cite the source on first use. Do not re-coin.

*Examples (likely):* intergenerational equity (Brown Weiss 1989, Howarth + Norgaard 1990); intergenerational mobility (Becker 1979, Solon 1992, Chetty 2014); intergenerational wealth transmission (Piketty 2014, Saez + Zucman 2016); intergenerational transfers (Modigliani 1986, Kotlikoff 1992); intergenerational obligation (Rawls 1971, Parfit 1984, Gosseries + Meyer 2009); option value (Henry 1974, Arrow + Fisher 1974, Dixit + Pindyck 1994).

**Tier B — Adopt established academic-literature term with framework-specialization footnote.**
Use when an existing academic-literature term is close-but-not-identical, where the framework specializes one or two axes, AND the specialization is decodable to the B-register reader with a light footnote. Adopt the academic term as the base; mark the framework's specialization explicitly via Tech Appendix §L methodological footnote (or equivalent).

*Examples (existing):* Externality Tail (Pigou 1920 + framework specialization on four axes — post-extraction persistence, substitutability-independence, time-indexed function form, "runs on its own clock" rhetorical anchor); Substitutability Function S (econometric substitutability literature + framework specialization as time-indexed probability function); Hotelling Identity (Hotelling 1931 + framework extension); Triangulated RCV Estimation (econometric triangulation literature + framework synthesis).

**Tier C — Use descriptive prose adjective + noun (no proper-noun framework term).**
Use when existing English vocabulary suffices in B-register chapter usage, no academic-literature exact-fit term applies, and the phrase doesn't recur frequently enough or with enough specificity to warrant proper-noun status. Track in `core/terms/terms_index.md` as a "preserved compositional phrase" if recurring across chapters; do not promote to proper-noun.

*Examples (existing):* intergenerational cost severance (lowercase phrase composed from "intergenerational" adjective + Cost Severance Ring-1 term); temporal cost severance (lowercase); spatial cost severance (lowercase); the cost-bearer; the extractor; the framework's accounting.

**Tier D — Coin a new framework-specific term.**
Use when Tiers A+B+C all fail — the framework needs to make a distinction no existing vocabulary supports, and the distinction is load-bearing on the framework's argument. Full lineage and specialization required (per M12 honesty discipline). Coined term gets a full terms_index record with rigor-provenance, status, glossary_definition + tech_appendix_definition rendering fields per S1 schema, M12 lineage citations.

*Examples (existing):* Cost Severance (specialization of HR-severance concept); Severed Cost (result-noun pair); Accountability Bond (specialization of bond-as-financial-instrument); Restitution Bond + Foreclosure Bond (sub-instruments); Commons Inversion Test (CIT, supersedes AIT); Asymmetric Regret Rule (ARR, supersedes ARP); Intergenerational Pricing Gap (IPG); Abundance Masking; Residual Commons Value (RCV).

### §3.2 The decision-rule for which tier wins

**Default to lowest tier (A → B → C → D) that adequately serves the B-register reader.**

- Coinage (Tier D) is the last resort, not the first move.
- Existing academic vocabulary (Tier A or B) is preferred whenever it serves the B-register reader without specialist gloss.
- Descriptive prose (Tier C) is preferred whenever it carries the meaning without inflating vocabulary footprint.

For terms in D-modulation chapters where the success-criterion is legal/policy adoption-travel, the Tier verdict additionally tests whether the chosen tier supports regulatory-text migration. Failure on that test pushes the verdict to Tier D-with-policy-vocabulary-specialization — the coined term is engineered for legal/policy adoption (e.g., severed cost as Tier D specifically engineered for legal/policy migration; Restitution Bond as Tier D specifically engineered for policy-instrument adoption).

### §3.3 Strict-fit threshold for Tier A

Tier A adoption requires both:
1. The existing academic term captures *every* axis the framework cares about for the term's role.
2. The existing academic term requires no specialist gloss for the B-register reader.

Failure on either threshold pushes the verdict to Tier B (existing term + framework-specialization footnote) or further down the ladder. Tier A is the strictest move; most terms that look like Tier A candidates are actually Tier B once the strict-fit threshold is applied.

### §3.4 Strict-fit threshold for Tier D

Tier D coinage requires demonstrating that Tiers A+B+C all fail:
1. **Tier A fails** — no existing academic-literature term captures the framework's intended meaning exactly.
2. **Tier B fails** — no existing academic-literature term is close-but-not-identical with decodable specialization.
3. **Tier C fails** — descriptive prose adjective + noun does NOT carry the meaning for the B-register reader; the phrase recurs frequently enough or with enough specificity that proper-noun status is load-bearing.

If any of (1)/(2)/(3) is unclear, default to the lower tier and revisit. Coinage is reversible (rename via supersession) but creates audit-trail complexity.

---

## §4. The decision rule under the inherited audience

### §4.1 The single-question test (per term)

For any vocabulary decision, the single question is:

> **What's the lowest tier (A → B → C → D) that adequately serves the B-register reader for this term, with D-modulation reader supplementary in adoption-travel chapters?**

This question replaces all earlier per-term audience juggling. The answer is one verdict per term.

### §4.2 The four-tier ladder application

1. **Run Tier A check.** Does an established academic-literature term capture the framework's intended meaning exactly AND land cleanly with the B-register reader without specialist gloss? If YES → Tier A; document the source citation. If NO → proceed to Tier B.
2. **Run Tier B check.** Is there an academic-literature term that's close-but-not-identical, where the framework specializes one or two axes, AND the specialization is decodable to the B-register reader with a light footnote? If YES → Tier B; document the source citation + framework specialization footnote. If NO → proceed to Tier C.
3. **Run Tier C check.** Would descriptive prose adjective + noun (existing English vocabulary) suffice in B-register chapter usage? If YES → Tier C; track as preserved compositional phrase if recurring; do NOT promote to proper-noun. If NO → proceed to Tier D.
4. **Run Tier D check.** Coinage justified — proceed to draft full terms_index record per S1 schema; ensure suffix-convention discipline (§6) and capitalization-discipline (§7) hold.

### §4.3 Per-term verdict format

The verdict carries:
- **Tier verdict:** A / B / C / D
- **Audience-rationale:** one sentence explaining why this tier serves the B-register reader (and D-modulation reader where applicable)
- **Source citation** (Tiers A + B): explicit academic-literature reference
- **Framework specialization** (Tier B + D): what the framework adds beyond the academic term
- **Cross-tier-rejection rationale** (Tiers B/C/D): one sentence each explaining why higher tiers (A/B/C) failed

### §4.4 D-modulation override

In D-modulation chapters (Ch 9 + Ch 7 instrument-design + Ch 10 regulatory-architecture), the per-term Tier verdict additionally tests:
- Does this Tier choice support severed-cost migrating into legal/policy text?
- Does the term read naturally in regulatory-vocabulary register?

Failure on either override pushes the verdict to Tier D-with-policy-vocabulary-specialization. The coined term is then engineered with explicit attention to regulatory-text adoption-travel.

### §4.5 Decision-tree representation (supplementary)

The four-tier-ladder above is mathematically equivalent to a decision-tree of sequential yes/no questions. For readers who decode algorithmic walks more easily than tier-lists, the same discipline can be expressed:

```
For any candidate vocabulary decision:

  1. Does an established academic-literature term capture the framework's
     intended meaning EXACTLY?
     |
     +-- Question 1a: AND would a B-register reader (Mazzucato/Raworth/Sen
     |   profile) decode it without specialist gloss?
     |   |
     |   +-- YES → ★ TIER A (adopt verbatim with citation)
     |   |
     |   +-- NO → proceed to question 2
     |
     +-- NO → proceed to question 2

  2. Is there an academic-literature term that's close-but-not-identical,
     where the framework specializes one or two axes?
     |
     +-- Question 2a: AND is the specialization decodable to a B-register
     |   reader with a light footnote?
     |   |
     |   +-- YES → ★ TIER B (adopt with framework-specialization footnote)
     |   |
     |   +-- NO → proceed to question 3
     |
     +-- NO → proceed to question 3

  3. Would descriptive prose adjective + noun (existing English vocabulary)
     suffice in B-register chapter usage WITHOUT proper-noun status?
     |
     +-- YES → ★ TIER C (descriptive prose; track as preserved compositional
     |          phrase if recurring; do NOT promote to proper-noun)
     |
     +-- NO → proceed to question 4

  4. The framework needs a distinction no existing vocabulary supports.
     |
     +-- ★ TIER D (coinage justified — proceed to draft full terms_index
                   record per S1 schema with audience-rationale narrative)

  D-modulation override (in Ch 9, Ch 7 instrument-design, Ch 10
  regulatory-architecture sections):
     After the tier verdict, additionally test:
     - Does this tier choice support severed-cost migrating into
       legal/policy text?
     - Does the term read naturally in regulatory-vocabulary register?
     If failure on either, push verdict to Tier D-with-policy-vocabulary-
     specialization (term engineered for regulatory-text adoption-travel).
```

This decision-tree is operationally equivalent to the tier-ladder framing in §4.2; it is included as a supplementary representation per the framework-shape rigor pass `commons_bonds_rigor_pass_2026-04-28_vocabulary_decision_framework_shape_v1.0.0.md` ratification.

---

## §5. D-modulation guidance for adoption-travel chapters

### §5.1 Where D-modulation applies

Per the ratified book-audience verdict:

- **Ch 9 *Pricing Honestly*** — canonical D chapter. Already drafted in policy-practitioner register (Norway sovereign-wealth-fund + accountability-instrument design + regulatory-text vocabulary). Continues in D-modulation.
- **Ch 7 *Guidance Doc / framework operating manual*** — partial D-modulation in instrument-design sections; B primary in framework-introduction sections.
- **Ch 10 *Common Bonds*** — primarily B; D-flavored regulatory-architecture discussion in late sections.

### §5.2 What D-modulation changes vocabulary-wise

- **Higher tolerance for instrument-design specificity.** Restitution Bond, Foreclosure Bond, Asymmetric Regret Rule, Cost Severance Damages get more concrete operational treatment.
- **Regulatory-text vocabulary preferred** where the framework's success-criterion is migration of severed-cost into legal/policy text. Names like *Restitution Bond* (engineered for legal/policy adoption), *Cost Severance Damages* (legal-tort-vocabulary), *severed cost* (becoming legal/policy vocabulary).
- **More citation density on policy-economics lineage.** Tooze, Brookings, Roosevelt-Institute, Hockett, Omarova references where load-bearing.
- **Less narrative-personal voice.** Author voice still present but disciplined.

### §5.3 What D-modulation does NOT change

- **The Tier A→D ladder framework.** Same four tiers; same decision rule. Just additional override for adoption-travel.
- **The book's primary register.** B is primary across the book; D-modulation is register-modulation within specific chapters, not audience-change.
- **The framework's mathematical apparatus.** CS = RCV − B, the integrand, the Substitutability Function, the Hotelling Identity all carry across chapters.

### §5.4 What "register-modulation" means concretely

A B-primary chapter (e.g., Ch 4 *Existence Proof*) might introduce *Cost Severance* with: *"Cost Severance is the framework's name for the structural mechanism by which extraction separates value capture from cost bearing — the central phenomenon this book examines."*

A D-modulation chapter (e.g., Ch 9 *Pricing Honestly*) might introduce the same term with: *"The accountability gap measures the dollar amount of cost severance — RCV minus the Accountability Bond. When B = RCV, severance is zero (honest accounting); when B is below RCV, the gap is what gets passed forward."* — same framework term, more instrument-design-vocabulary register.

### §5.5 Engineered-for-adoption-travel design intent

Per the four-move-framework-shape rigor pass (RATIFIED 2026-04-28), the framework recognizes a distinction between two flavors of Tier D coinage that operate within the four-tier shape rather than splitting D into separate tiers:

**Tier D (general framework coinage)** — coined to support the framework's internal apparatus or pedagogy. Examples: Substitutability Function (S), Asymmetric Regret Rule (ARR), Abundance Masking, Triangulated RCV Estimation. These terms exist primarily to make the framework's internal logic legible; their adoption travel beyond the book is a side benefit, not the design intent.

**Tier D engineered for legal/policy adoption-travel** — coined with explicit design intent that the term migrates into regulatory text + legal opinions + policy briefs. Examples: Cost Severance, Severed Cost, Restitution Bond, Foreclosure Bond, Cost Severance Damages (CSD). The term's success criterion is migration into regulatory vocabulary; the design choice (suffix, semantic loading, lineage hooks) optimizes for that travel.

Both flavors are Tier D under the four-move framework — the distinction is a *design intent annotation*, not a separate tier. The decision rule (default to lowest tier serving B-register reader) applies identically; the design-intent annotation determines additional engineering-for-adoption-travel constraints in D-modulation chapters.

**When to flag a Tier D coinage as engineered-for-adoption-travel:**
1. The term appears in D-modulation chapters (Ch 9; Ch 7 instrument-design sections; Ch 10 regulatory-architecture sections) as a load-bearing instrument-name.
2. The framework's success criterion is the term's migration into legal/policy text.
3. The suffix (e.g., -Bond, -Damages, Severed Cost) pattern-matches existing regulatory-vocabulary conventions to ease adoption.
4. The lineage hooks (e.g., Restitution-tradition cross-political-readability for Restitution Bond) explicitly support adoption across political traditions.

**When NOT to flag Tier D as engineered-for-adoption-travel:**
1. The term exists primarily to make framework's internal logic legible (e.g., Triangulated RCV Estimation — pedagogical-internal).
2. The term appears mostly in B-primary chapters as conceptual apparatus.
3. The term's design intent is reader-comprehension, not regulatory-vocabulary migration.

**Decision-record annotation:** when a Tier D coinage carries engineered-for-adoption-travel design intent, the terms_index Rigor-provenance section explicitly notes: *"Tier D engineered for legal/policy adoption-travel per vocabulary strategy §5.5 — design intent: [specific success-criterion]; suffix-convention: [pattern]; lineage hooks: [traditions]."*

---

## §6. Suffix-convention discipline

### §6.1 The framework's existing suffix convention

The framework already operates under an implicit role-bearing-suffix discipline. Each suffix encodes the term's mathematical role for the reader:

| Mathematical role | Suffix | Examples |
|---|---|---|
| Input variable / Cᵢ | `-Cost` | Foreclosure Cost, Externality Tail (variant), Dynastic Labor Cost (when ratified), Lifetime Survival Cost (when ratified), Community Disruption Cost, Knowledge and Cultural Cost, Political Capture Cost |
| Function inside RCV integrand | `-Function` | Substitutability Function (S), Discount Function (D) |
| Primitive on equation's other side | `-Bond` | Accountability Bond (B), Restitution Bond (B₁), Foreclosure Bond (B₂) |
| Output mechanism | `-Severance` | Cost Severance |
| Output dollar amount | `Severed Cost` | Severed Cost |
| Output ratio | `-Gap` | Intergenerational Pricing Gap (IPG) |
| Damages instrument | `-Damages` | Cost Severance Damages (CSD) |
| Decision rule | `-Rule` | Asymmetric Regret Rule (ARR) |
| Methodology / test | `-Test` | Commons Inversion Test (CIT) |
| Methodology / apparatus | `-Gates` | Four Gates |
| Identity (math equation by definition) | `-Identity` | Hotelling Identity |
| Estimation methodology | `-Estimation` | (slot retired per Insight #31 RATIFIED 2026-04-28; Triangulated RCV Estimation → Three Ways of Counting) |

### §6.2 The discipline going forward

When coining a new framework term (Tier D move), choose the suffix that:
1. Encodes the term's mathematical role transparently for the B-register reader.
2. Matches the existing convention table where applicable.
3. Pattern-matches academic conventions for that role (e.g., `-Function` for math functions matches econometric convention; `-Bond` for B-side primitives matches financial-instrument convention).
4. Survives the cross-political-tradition robustness check (§8).

### §6.3 When to extend the convention

If a new mathematical role surfaces that doesn't match any existing slot, the suffix-convention may be extended via focused rigor pass. Don't add new suffix slots casually — each slot adds reader-cognitive-overhead. Default to compressing into existing slots when possible.

### §6.4 Aggressive-scope suffix coherence verdicts

Per the cluster vocabulary rigor pass (`commons_bonds_rigor_pass_2026-04-28_intergenerational_cluster_vocabulary_consolidation_v1.0.0.md`), each suffix slot is evaluated against 2-5 alternatives under the inherited B-register audience. The per-slot verdicts are:

*[Cluster pass §10.4 (RATIFIED 2026-04-28) defers the formal suffix-convention coherence rigor pass: "most suffix slots passed audience-fit per inventory data; one-off slots (`-Identity` for Hotelling Identity; `-Estimation` for Triangulated RCV Estimation) flagged as RECONSIDER candidates but not load-bearing audience-fit failures. Defer formal suffix-convention coherence rigor pass until adoption-travel evidence surfaces a specific issue." The table below remains as preliminary forecasts; ratified verdicts will land here when the deferred coherence pass executes.]*

The preliminary forecast pattern (subject to the deferred coherence pass):

| Suffix slot | Current | Likely verdict |
|---|---|---|
| Cᵢ inputs | `-Cost` | Likely RATIFIED — universal reader comprehension; mathematical-role implicit; alternative -Burden / -Levy / -Damage tested under B-register audience and likely rejected for primary-vocabulary. -Damage retained as parallel for legal-vocabulary contexts (e.g., CSD). |
| B-side primitives | `-Bond` | Likely RATIFIED — financial-instrument convention; legal-adoption-travel strong; -Account / -Reserve / -Fund / -Trust tested and likely rejected as less precisely role-encoding. |
| Output ratios | `-Gap` | Likely RATIFIED — strong gap-form lineage in econ literature; -Deficit / -Shortfall / -Differential tested and likely rejected. |
| Output mechanism | `-Severance` | Likely RATIFIED — Ch 1 Option-C HR-severance bridge already ratified; legal-property-law lineage strong. |
| Decision rules | `-Rule` | Likely RATIFIED — ARP→ARR rename rigor pass already ratified this slot. |
| Methodologies | `-Test` | Likely RATIFIED — methodological-procedure convention; flagged for re-test under B-register audience due to mild statistical-test connotation. |
| Functions | `-Function` | Likely RATIFIED — math-specialist convention; B-register reader decodes with light context. |
| Identity (one-off) | `-Identity` | RECONSIDER possible — Hotelling Identity is one-off; B-register reader may misread as "personal identity"; alternative -Equation / -Relation possible. |
| Estimation (one-off) | `-Estimation` | RETIRED per Insight #31 RATIFIED 2026-04-28 — Triangulated RCV Estimation renamed to "Three Ways of Counting"; slot now empty in active vocabulary. |

---

## §7. Capitalization-discipline guidance

### §7.1 The discipline

Two rules govern capitalization choice:

**Rule 1 — Proper-noun (capitalized) for framework-technical terms; lowercase for descriptive prose phrases.**

Framework-technical terms (Ring-1 + Ring-2 ratified per terms_index) get proper-noun capitalization. Descriptive prose phrases composed from existing words (lowercase compositional phrases) stay lowercase.

*Examples:*
- *Cost Severance* (proper-noun) = the Ring-1 framework term
- *cost severance* (lowercase) = descriptive prose phrase composing "cost" + "severance"
- *Intergenerational Pricing Gap* (proper-noun) = Ring-2 framework term
- *intergenerational cost severance* (lowercase) = descriptive prose phrase
- *Restitution Bond* (proper-noun) = Ring-2 sub-instrument
- *bonds of restitution* (lowercase) = descriptive prose phrase

**Rule 2 — Capitalization is content, not formatting.** Authorial capitalization choice carries meaning the typesetting must preserve. Editorial capitalization-homogenization sweeps must not flatten the proper-noun-vs-lowercase distinction for framework terms.

### §7.2 Edge cases

**First-word-of-sentence capitalization.** When a lowercase-compositional-phrase appears as the first word of a sentence, the rule still holds — the capitalization is sentence-mechanical, not framework-technical. Reader context disambiguates.

**Section-header capitalization.** Section headers may use title-case or sentence-case per editorial style; the framework-vs-prose distinction holds within sentences regardless.

**Equations + math notation.** Symbols are always proper-noun-capitalized (CS, RCV, B, S, E, IPG). Subscripts (B₁, B₂, Cᵢ) follow math conventions.

### §7.3 When in doubt

Default to lowercase descriptive prose unless the term meets all three criteria:
1. The term is in `core/terms/terms_index.md` as a CURRENT Ring-1 or Ring-2 entry.
2. The term has explicit framework specialization (Tier B or Tier D).
3. The capitalized form is the form ratified in that terms_index entry.

If any criterion fails, use lowercase descriptive prose.

---

## §8. Cross-political-tradition robustness check

### §8.1 The check

For any new coined term (Tier D) or borrowed academic term (Tier A or B), test the term's connotations against four political-tradition reading-positions:

1. **Classical-liberal reading** — does the term work for a reader who frames the framework's claims through individual-rights / property-rights / market-mechanism vocabulary?
2. **Civic-republican reading** — does the term work for a reader who frames through non-domination / shared-institutions / public-goods vocabulary (Pettit, Skinner, Anderson)?
3. **Socialist / communitarian reading** — does the term work for a reader who frames through collective-provisioning / shared-infrastructure / common-stewardship vocabulary?
4. **Lived-oppression reading** — does the term work for a reader who reads from positions where extraction has been done TO their community (Indigenous, descendant of historically-extracted communities, currently-extracted communities)?

A term passes the check if it's load-bearing across all four reading-positions without unintended connotations that would distort the framework's claims for any one position.

### §8.2 Examples of past terms that passed (or were renamed to pass)

- **Restitution Bond** (renamed from Reparations Bond per b1_b2_naming pass §10) — *Reparations* read narrowly as US-Black-reparations specifically, distorting the framework's broader cross-tradition claim. *Restitution* reads more neutrally across all four positions.
- **Cost Severance** (Option C ratification 2026-04-24) — HR-severance bridge in Ch 1 establishes the term across reading positions; the term works for classical-liberal (severance-of-property), civic-republican (severance-of-civic-bond), socialist (severance-of-collective-stewardship), and lived-oppression (severance-of-lineage) readings.
- **Commons Inversion Test (CIT)** (renamed from Abundance Inversion Test per CIT supersession 2026-04-24) — *Abundance* specifically risked Marxist-orthodoxy connotations that distorted the framework's cross-tradition reach; *Commons* anchors in Ostrom-tradition cross-political-readable language.

### §8.3 What failure looks like

A term fails the check if any one reading-position would read the term in a way that distorts the framework's claim for that position. Failure pushes the verdict to:
- Renaming the term (different word; preserve framework meaning)
- Demoting the term (Tier C descriptive prose instead of Tier D coinage)
- Adding explicit clarifying footnote (Tier D + cross-tradition footnote)

### §8.4 What the check does NOT require

The check does not require the term to be *neutral* across all positions — every term carries some lineage and some connotational weight. The check requires that the term's connotations not *distort* the framework's claims for any one reading-position. *Cost Severance* connotes labor-rights vocabulary (workers' severance pay) — that connotation is fine; it doesn't distort the framework's claim under any reading-position.

---

## §9. Decision-record format for future vocabulary decisions

### §9.1 Where decisions get recorded

Every framework vocabulary decision lands in `core/terms/terms_index.md` per the architecture-rigor-pass S1 schema:

- **For Tier D (coinage)** — new entry with full record per S1 schema, including `glossary_definition` (~80 words, reader-register, one example) + `tech_appendix_definition` (~300 words, formal + lineage citations).
- **For Tier B (academic + specialization)** — new entry with S1 fields; lineage citations cite the academic source + framework-specialization footnote.
- **For Tier A (academic adopt verbatim)** — typically does NOT need a terms_index entry; the academic source citation lives in the chapter prose's first-use footnote.
- **For Tier C (descriptive prose)** — terms_index entry as "preserved compositional phrase" record; no rendering fields per S1 schema (descriptive prose doesn't produce publisher-facing entries).

### §9.2 Decision-record narrative format

Every Tier D or Tier B decision carries a brief decision-narrative in the terms_index entry's `Rigor provenance` section:

```
Audience-rationale (per vocabulary strategy v1.0.1): Tier {A/B/C/D} chosen because [reason serving B-register reader]. {If D-modulation applicable: D-modulation override applied because [reason supporting legal/policy adoption-travel].} Cross-tier-rejection: Tier {one-down-from-chosen} rejected because [reason]. Cross-political-tradition check: PASSES (or describe specific accommodation).
```

This narrative becomes part of the standing audit trail. Future readers (academic reviewers, editors, future-self) can trace why a given term landed at a given tier.

### §9.3 Suffix-convention decision record

When a new term is coined (Tier D), the suffix choice is documented:

```
Suffix-convention: {-Cost / -Bond / -Function / -Rule / -Test / -Gates / -Severance / -Damages / -Gap} per §6 of vocabulary strategy v1.0.1. Encodes mathematical role: {role}. Pattern-matches academic convention: {convention}.
```

If the new term extends the suffix-convention with a new slot, that requires its own focused rigor pass before coinage.

### §9.4 Rename / supersession record

When an existing term is renamed (e.g., AIT → CIT, ARP → ARR, Reparations Bond → Restitution Bond), the supersession record cites this strategy doc:

```
Renamed per {rigor pass file} ratified {date} by {Chris Winn / collaborative}. New name chosen per vocabulary strategy v1.0.1 §{section} discipline: {one-sentence rationale}.
```

### §9.5 Publisher-facing-scrubbing discipline (per Working Principle #8)

The decision-record narrative formats above (§9.2 + §9.3 + §9.4) live in `core/terms/terms_index.md` Rigor-provenance sections (Tier 3 scaffolding per Working Principle #8). They DO NOT appear in publisher-facing artifacts — chapter drafts, glossary entries, Tech Appendix sections.

**Specifically:**

- **In chapter prose:** terms appear as named objects with reader-facing context — first-introduction definitions, lineage citations on first use, framework-specialization footnotes if Tier B. NO audience-rationale narratives, cross-tier-rejection notes, or "Tier D per §X" annotations.
- **In glossary entries:** rendering fields derived from terms_index `glossary_definition` field (~75-85 words, reader-register, one concrete example). NO Rigor-provenance / Audience-rationale / Cross-tier-rejection / Tier-suffix-convention metadata.
- **In Tech Appendix:** rendering fields derived from terms_index `tech_appendix_definition` field (~280-340 words, formal + lineage citations + math notation). NO "Backed by rigor pass X (commit Y)" annotations, M11 critic-survival probes inline, status indicators.

**The decision-record narratives are author-facing scaffolding** (Tier 3 per Working Principle #8) — they let future-author + AI assistants + reviewers trace why each term landed at its ratified tier without having to re-run the discipline. They are NOT intended for the B-register reader (Mazzucato/Raworth/Sen profile) of the published book.

This discipline holds for ALL framework vocabulary decisions going forward and for the Phase 3 Tech Appendix v2.0.0 rebuild + Phase 4 Glossary v4 rebuild deliverables.

---

## §10. Worked examples

**Status: case-study selection deferred (per author direction 2026-04-28).** Audience for this scaffolding doc is Chris + AI assistants applying the discipline to future vocabulary decisions; case studies serve future-AI pattern-matching, but the per-term rigor passes themselves are the canonical examples. Explicit selection of "the right 8" is deferred — when a future vocabulary decision needs a worked-example anchor, the relevant past per-term rigor pass gets cross-referenced inline rather than promoted into a curated §10 list.

The original draft enumerated 8 worked examples (Cost Severance / Externality Tail / Restitution Bond / intergenerational equity / intergenerational cost severance / ARR / CSG demotion / Cost Bearing demotion). Those drafts are preserved below as illustrative — not curated as canonical.

### §10.1 Cost Severance (Tier D, targets B-register first; survives D-modulation)

**Decision:** Tier D coinage. Specialization of HR-severance + property-law-severance lineage; framework-specific specialization on the value-extractor-vs-commons relationship.

**Audience rationale:** Tier A failed (no academic-literature exact-fit term existed for the framework's intended meaning); Tier B failed (no close-fit academic term that could carry framework specialization with light footnote); Tier C failed (descriptive prose like "the cost-severance phenomenon" recurs frequently enough across chapters that proper-noun status is load-bearing); Tier D justified.

**B-register reception:** strong. HR-severance + property-law-severance are accessible to non-economics-degree readers; framework specialization decodes via Ch 1 Option-C bridge.

**D-modulation reception:** strong. *Severed cost* engineered for legal/policy adoption-travel; success-criterion specifically targets this term's migration into regulatory text.

**Cross-political-tradition check:** PASSES (per §8.2 example).

**Suffix-convention:** `-Severance` is the canonical suffix for the framework's output-mechanism slot.

### §10.2 Externality Tail (E) (Tier B, targets B-register first)

**Decision:** Tier B — Pigouvian externality (Pigou 1920) base + framework specialization on four axes (post-extraction persistence, substitutability-independence, time-indexed function form, "runs on its own clock").

**Audience rationale:** Tier A failed strict-fit (Pigouvian externality doesn't capture the four specialization axes); Tier B fits — academic lineage (Pigou) + framework specialization decodable via Tech Appendix §L footnote.

**B-register reception:** adequate. Reader doesn't need to know Pigou to follow the framework; Pigou citation provides academic-defensibility for those who do.

**Suffix-convention:** `-Tail` is a one-off in the framework's suffix vocabulary; flagged for §6.4 RECONSIDER review (could potentially be `-Function` per the Function slot, but `-Tail` carries stronger time-extending connotation).

### §10.3 Restitution Bond (Tier D, engineered for D-modulation adoption-travel)

**Decision:** Tier D coinage; renamed from *Reparations Bond* per b1_b2_naming pass §10 ratified 2026-04-24.

**Audience rationale:** Tier A failed; Tier B failed (financial-instrument *bond* + restitution-tradition specialization is non-trivial framework specialization); Tier C failed (the term is a load-bearing instrument-name across multiple chapters); Tier D justified.

**B-register reception:** strong. *Restitution* is reader-accessible; *Bond* pattern-matches financial-instrument convention; the combination signals the framework's instrument-architecture clearly.

**D-modulation reception:** strong. Engineered specifically for legal/policy adoption-travel; *Restitution Bond* reads naturally in regulatory-text register where the policy-instrument is being discussed.

**Cross-political-tradition check:** PASSES (per §8.2 example) — *Reparations* failed because of US-specific connotations; *Restitution* passes across all four reading-positions.

**Suffix-convention:** `-Bond` per the B-side-primitive slot.

### §10.4 intergenerational equity (Tier A, descriptive academic adoption)

**Decision:** Tier A — adopt Brown Weiss 1989 + Howarth + Norgaard 1990 academic concept verbatim with citation. No coinage; no specialization footnote required.

**Audience rationale:** Tier A passes — established academic concept reads cleanly with B-register reader (intergenerational ethics is well-established literature; Brown Weiss is canonical); no framework specialization required for the term to do its work in chapter prose.

**B-register reception:** strong. Reader recognizes academic concept; framework cites it as load-bearing on intergenerational-ethics tradition without claiming to extend it.

**Capitalization:** lowercase per §7 — *intergenerational equity* (lowercase) = the established academic concept; the framework does not promote it to proper-noun.

### §10.5 intergenerational cost severance (Tier C, preserved compositional phrase)

**Decision:** Tier C — preserved compositional phrase. Composes from existing Ring-1 term (Cost Severance) + descriptive adjective (intergenerational); no proper-noun status; no rendering fields per S1 schema.

**Audience rationale:** Tier A failed (no academic-literature exact-fit); Tier B failed (no close-fit academic term); Tier C succeeds — descriptive prose carries the meaning for the B-register reader because Cost Severance is already a Ring-1 framework term and "intergenerational" is a descriptive adjective the reader recognizes.

**B-register reception:** strong. Reader follows the compositional logic without needing the phrase elevated to proper-noun.

**Capitalization:** lowercase per §7.

### §10.6 Asymmetric Regret Rule (Tier D, renamed from Asymmetric Regret Principle)

**Decision:** Tier D — renamed from Asymmetric Regret Principle (ARP) to Asymmetric Regret Rule (ARR) per ARP-rename rigor pass `commons_bonds_rigor_pass_2026-04-24_arp_rename_v1.0.0.md` ratified 2026-04-24.

**Audience rationale:** Original Tier-D ARP coinage was correct under previous discipline. Rename to ARR was triggered by Working Principle #5 (context-flipping rules earn named-rule status) + M6 audit (Loomes & Sugden 1982 regret-theory direct lineage in name without Tech-Appendix-footnote dependency) + Principle-overclaim concern. *Rule* downgrades *Principle* overclaim while preserving regret-theory framing.

**B-register reception:** strong. *Asymmetric Regret* signals the regret-theory tradition; *Rule* signals operational-decision-rule status (matches Loomes-Sugden convention).

**D-modulation reception:** strong. Operational-rule register reads naturally in instrument-design discussion (Ch 7 + Ch 9 + Ch 10).

**Suffix-convention:** `-Rule` per the decision-rule slot.

### §10.7 Civilizational Substitutability Gap (CSG) (Tier C demotion from Tier D)

**Decision:** Originally Tier D coinage; demoted to Tier C (preserved as descriptive prose phrase only) per CSG-rigor-pass `commons_bonds_rigor_pass_2026-04-24_term_csg_v1.0.0.md` ratified 2026-04-24.

**Audience rationale:** Tier D coinage failed parsimony (CSG is a derived scalar — difference between two Substitutability Function S evaluations — and the framework doesn't name derived scalars per Principle #1 + Corollary B). Tier C suffices — descriptive prose *"industrial-vs-existential substitutability gap"* carries the meaning without proper-noun status.

**B-register reception (under demotion):** adequate. Concept persists in prose; reader follows compositional logic.

**Reading lesson:** ratified Principle #1 Corollary B *"usage frequency alone is not a rigor argument for retention"* originated here. CSG had 66 active references but the rigor verdict was demotion despite usage; this discipline holds for future similar cases.

### §10.8 Cost Bearing (Tier C demotion from Tier D)

**Decision:** Tier C — demoted from glossary entry to prose-only usage per Cost-Bearing-rigor-pass 2026-04-24.

**Audience rationale:** Tier D coinage was incorrect — *Cost Bearing* describes a ROLE (someone is bearing cost), not a framework-specific mechanism or event. Role-descriptions don't need technical vocabulary. Tier C suffices — descriptive prose ("the cost-bearer", "the community bears", "future generations bear the cost") carries the role-description without proper-noun status.

**Reading lesson:** distinguishing ROLE descriptions from MECHANISM / EVENT terms. Mechanisms + Events earn Tier D coinage when load-bearing; Roles default to Tier C prose.

---

## §11. Versioning + ratification + revision triggers

### §11.1 Version

Document version: **v1.0.1** as of 2026-04-28.

### §11.2 Ratification

Initial document ratification: **RATIFIED 2026-04-28 by Chris Winn** (v1.0.0 → v1.0.1 with refinements per `commons_bonds_rigor_pass_2026-04-28_vocabulary_decision_framework_shape_v1.0.0.md`: §4.5 decision-tree representation; §5.5 engineered-for-adoption-travel design intent; §10 case-study selection deferred). Document is the standing reference for framework vocabulary decisions; cited from terms_index entries + chapter audit + rigor passes.

### §11.3 Revision triggers

The document is revised when:

1. **Book-level audience changes.** If a future rigor pass overturns the ratified Option B + supplementary D verdict, this document inherits the new audience and §2 + §4 update accordingly.
2. **Substantial Tier-A/B/C/D verdict pattern emerges.** If a series of vocabulary decisions surface a pattern not anticipated by the §3 + §4 framework, the framework gets updated.
3. **Suffix-convention extends.** If a new mathematical role surfaces requiring a new suffix slot, the §6 convention table is updated (after focused rigor pass).
4. **Cross-political-tradition test surfaces a missed reading-position.** If a new political-tradition reading-position emerges as load-bearing for the framework's reach, §8 reading-positions are updated.
5. **Capitalization-discipline edge case surfaces.** If a new edge case in §7 emerges, the discipline is updated.

### §11.4 Cross-reference maintenance

Whenever this document is revised:
- Update `MEMORY.md` (project memory index) to reflect any change in vocabulary discipline that affects future sessions.
- Update `core/terms/terms_index.md` §1 (template + integration notes) to reflect the current version.
- Update `tools/commons_bonds_rigor_protocol_v2.X.0.md` cross-reference if the protocol references vocabulary discipline.
- Update Working Principles file if a new Principle emerges (e.g., possible Principle #7 codifying audience-discipline as standing commitment).

---

## §12. Cross-references — load-bearing files

### §12.1 Upstream rigor passes (this document inherits from)

- `tools/rigor-passes/commons_bonds_rigor_pass_2026-04-28_book_audience_choice_v1.0.0.md` — RATIFIED 2026-04-28; ratified book-level audience (B + supplementary D)
- `tools/rigor-passes/commons_bonds_rigor_pass_2026-04-27_publication_architecture_terms_index_glossary_tech_appendix_v1.0.0.md` — RATIFIED 2026-04-27; S1 schema for terms_index per-term records

### §12.2 Sibling discipline files

- `alignment/commons_bonds_working_principles_v1.0.0.md` — general-project disciplines
- `alignment/commons_bonds_open_insights_v1.0.0.md` — Insight #25 captures the closed-ratified book-audience verdict that feeds this document

### §12.3 Applied rigor passes (this document distills)

- `tools/rigor-passes/commons_bonds_rigor_pass_2026-04-28_intergenerational_cluster_vocabulary_consolidation_v1.0.0.md` — applied rigor pass producing per-term verdicts that this document captures as standing discipline
- `tools/rigor-passes/commons_bonds_rigor_pass_2026-04-24_term_value_capture_vs_extraction_v1.0.0.md` — historical per-term decision (Value Capture retired; Value Extraction adopted)
- `tools/rigor-passes/commons_bonds_rigor_pass_2026-04-24_term_csg_v1.0.0.md` — historical per-term decision (CSG demoted to Tier C)
- `tools/rigor-passes/commons_bonds_rigor_pass_2026-04-24_term_universality_test_re_examination_v1.0.0.md` — historical per-term decision (Universality Test demoted)
- `tools/rigor-passes/commons_bonds_rigor_pass_2026-04-24_arp_rename_v1.0.0.md` — historical per-term decision (ARP → ARR)
- `tools/rigor-passes/commons_bonds_rigor_pass_2026-04-24_b1_b2_naming_v1.0.0.md` — historical per-term decision (B = B₁ + B₂; Reparations Bond → Restitution Bond)

### §12.4 Standing artifacts (this document feeds into)

- `core/terms/terms_index.md` — every per-term record cites this discipline doc in its Rigor-provenance section
- `core/glossary/commons_bonds_updated_glossary_v4.html` (when Phase 4 rebuild lands) — derived from terms_index per S1 schema
- `core/technical-appendix/TechnicalAppendix_v2.0.0.html` (when Phase 3 rebuild lands) — derived from terms_index per S1 schema

---

## §13. Notation-discipline (added 2026-04-29 per Insight #55)

### §13.1 Why this section exists

Per Insight #42 (Phase 2 E.3 audit) + Insight #50 (Phase 2 RCV acronym collision) + Insight #52 (Phase 2 RCV integrand Q(t) convention divergence) + Insight #55 (framework-wide notation collision audit OPEN): notation collisions are a parallel discipline to vocabulary collisions. The same letter or abbreviation used for distinct concepts across the framework's apparatus produces the same M12 attribution-honesty + readability issue that the vocabulary-discipline framework is designed to prevent. This §13 codifies notation-discipline as standing reference parallel to §6 (suffix-convention discipline) + §7 (capitalization-discipline) + §8 (cross-political-tradition robustness check).

### §13.2 The reserved-letter ledger (per current framework usage)

Before introducing any new single-letter variable, multi-letter abbreviation, or Greek letter to the framework, cross-check against the reserved-letter ledger below. If the chosen letter/symbol collides with reserved usage, choose a non-reserved alternative.

**Single-letter variables (Latin):**

| Letter | Reserved use | Source / authority |
|---|---|---|
| **A** | Abundance (cost-tier domain in Theorem E.3) | Tech Appendix §10 E.3 |
| **B** | Aggregate Accountability Bond (CS = RCV − B) | Tech Appendix §B + terms_index entry |
| **B₁** | Restitution Bond (sub-instrument) | terms_index Restitution Bond entry |
| **B₂** | Foreclosure Bond (sub-instrument) | terms_index Foreclosure Bond entry |
| **C, Cᵢ** | Cost / i-th cost component | Tech Appendix §B Definition A.4 |
| **CS** | Cost Severance (per equation CS = RCV − B) | Tech Appendix §B + terms_index Cost Severance entry |
| **D, D(t, t₀)** | Discount factor (Weitzman 2001 declining-rate) | Tech Appendix §B Definition A.5 |
| **E, E(R, t)** | Externality tail (function); also Theorem labels E.1–E.5 (context disambiguates) | terms_index Externality Tail entry; Tech Appendix §10 |
| **P** | Market price | Tech Appendix §10 E.1 |
| **Q, Q(t)** | Quality-stock | Insight #52 (P2#8) |
| **R** | Resource (in RCV integrand) | Tech Appendix §B Definition A.1 |
| **S, S(t)** | Substitutability function (probability function in [0, 1]) | Tech Appendix §B Definition A.2 |
| **U, U(R, t, Q(t))** | Utility | Tech Appendix §B Definition A.6 |

**Subscript + superscript patterns:**

| Pattern | Reserved use | Source |
|---|---|---|
| **S_max** | Substitutability function limit (existential substitutability gap) | Insight #33 |
| **S_threshold** | Critical value of S_max below which a resource is existentially critical (per §F existential substitutability gap definition) | §F Tech Appendix; codified per Insight #55 (2026-04-30) |
| **t₀** | Initial time (extraction time) | Tech Appendix §B |
| **r_∞** | Long-run discount rate | Insight #40 (Theorem E.4) |

**Greek letters:**

| Letter | Reserved use | Source |
|---|---|---|
| **α** | Irreversibility parameter (§M scarcity multiplier; α ∈ [0, 1]; probability commons cannot be restored once extracted) | §M Tech Appendix; codified per Insight #55 (2026-04-30) |
| **β** | Risk-posture calibrator (§M scarcity multiplier; irreversibility_premium exponent; β = 1 default; β = 2 precaution-regime) | §M Tech Appendix; codified per Insight #55 (2026-04-30) |
| **ξ (xi)** | Cost-function curvature parameter (Insight #42 Theorem E.3 functional form: c(A) = c₀ · (τ/(A−ξ)... with ξ ≥ 1; renamed from α per Insight #55 to disambiguate from §M α irreversibility parameter) | Insight #42 + Insight #55 (2026-04-30 rename α → ξ) |
| **λ** | Substitutability function exponential parameter (S(t) = S_max(1 − e^{−λt})) | Insight #40 (Theorem E.4) |
| **ρ** | Commons regeneration rate (§B Definition A.1; ρ ≥ 0; non-renewable when ρ = 0) | §B Tech Appendix; codified per Insight #55 (2026-04-30) |
| **σ** | Scarcity parameter (§M scarcity multiplier; commons-stock / sustainable-flow ratio; scarcity_multiplier(σ) = 1 + log(1 + σ) × Hotelling_anchor) | §M Tech Appendix; codified per Insight #55 (2026-04-30) |
| **τ (tau)** | Scarcity threshold (Insight #42 Theorem E.3 — renamed from S to τ to disambiguate from substitutability function S(t)). NOTE: also commonly appears as integration dummy variable in math conventions (per Insight #55 audit, integration variable usage at line 6720 of Tech Appendix v1.0.0 will be renamed to u during Phase 3 v2.0.0 rebuild to avoid local-vs-global-scope conflict) | Insight #42 + Insight #55 (Phase 3 rename clarification) |

**Multi-letter abbreviations:**

| Abbreviation | Reserved use | Source |
|---|---|---|
| **RCV** | Residual Commons Value | Tech Appendix §B Definition A.1 + terms_index entry |
| **CIT** | Commons Inversion Test | terms_index entry; supersedes AIT |
| **CSD** | Cost Severance Damages | terms_index entry |
| **ARR** | Asymmetric Regret Rule | terms_index entry; supersedes ARP |
| **IPG** | Intergenerational Pricing Gap | terms_index entry |
| **CS** | Cost Severance (also single-letter-pair convention) | terms_index entry |
| **AIT** | RETIRED — superseded by CIT | terms_index retired-records |
| **FGC** | RETIRED | terms_index retired-records |
| **ESG** | RETIRED in framework context (industrial-existential substitutability gap) | terms_index retired-records |

### §13.2.1 Section-namespace overlap with single-letter variables (informational)

Per Insight #55 audit (2026-04-30): Tech Appendix section labels (§A through §M) overlap alphabetically with single-letter variable namespace (A, B, C, D, E). This is **standard academic-economics convention** — section labels use letters; variable letters chosen for mnemonic value; context disambiguates in practice.

Specifically:
- §A. Definitions ↔ A = abundance variable (Theorem E.3)
- §B. RCV Model ↔ B = Accountability Bond
- §C. Commons Inversion Test Protocol ↔ C = cost variable (Cᵢ); also 𝒞 = commons-territory set (per §13.2.2)
- §E. Theorems & Proofs ↔ E = externality tail function E(R, t); also Theorem labels E.1–E.5

**This overlap is documented for completeness; no rename required.** Reader-context disambiguation is reliable: §B (section reference) vs B (variable in equation) is unambiguous in any sentence; "Section E" vs "the externality tail E" likewise.

When introducing new section labels in Phase 3 Tech Appendix v2.0.0 rebuild, consult the reserved-letter ledger §13.2 for any new collisions; document any new overlap in this §13.2.1 note.

### §13.2.2 Set-valued objects use script/calligraphic typography (typography discipline)

Per Insight #55 audit (2026-04-30): when introducing set-valued mathematical objects (vs scalar variables), use **script/calligraphic typography** to disambiguate from variable namespace.

Standard mathematical convention:
- **𝒞 (script C)** — commons-territory set (resource units R ∈ 𝒞). Disambiguates from C = cost variable (Cᵢ).
- **𝒟, 𝒮, 𝒰, etc.** — available script forms for future set-valued objects if needed.

This convention applies to any new set-valued object introduced to the framework. Phase 3 Tech Appendix v2.0.0 rebuild applies this discipline to existing line 398 (commons-territory set rename C → 𝒞 per Insight #55 §11.4).

**Pattern-match academic-economics convention:** standard textbooks (Mas-Colell-Whinston-Green; Varian; Friedman) use script typography for set-valued objects (consumption sets ℒ; choice sets 𝒞; outcome spaces 𝛺). Framework discipline aligns.

### §13.3 The discipline going forward

When coining a new framework variable, abbreviation, or Greek letter (Tier D move per §3), the notation choice must:

1. **Cross-check the reserved-letter ledger** (§13.2) before introduction. If the letter is reserved, choose a non-reserved alternative.
2. **Pattern-match academic conventions** for the role (e.g., σ commonly denotes standard deviation in econometrics; if the framework introduces σ for something else, justify the divergence with M12 attribution-honesty footnote per §6.4).
3. **Survive the cross-political-tradition robustness check** parallel to §8 — for symbols (e.g., subscripted letters or composite notation), verify the choice doesn't have unintended connotations in adjacent academic fields.
4. **Document the reservation** — when a new letter/abbreviation is ratified, this §13.2 ledger is updated in the same commit.

### §13.4 Failure mode this prevents

Per Insight #42 Phase 2 E.3 audit: the S → τ collision (E.3 scarcity threshold colliding with E.4 substitutability function S(t) and Insight #33 S_max) was caught only because the cross-theorem viewing angle surfaced it; single-theorem audits would not have flagged it. Without standing notation-discipline, future framework decisions risk introducing similar collisions.

The four-layer notation discipline (Routine 1 prospective + Routine 2 retrospective + Insight #55 one-time retroactive + this §13 preventive) provides comprehensive coverage:

- **Prospective (Routine 1)** — daily sentinel catches new collisions as introduced.
- **Retrospective (Routine 2)** — weekly pre-submission sweep catches anything routine 1 misses.
- **One-time retroactive (Insight #55)** — surfaces existing collisions before Phase 3 Tech Appendix v2.0.0 rebuild.
- **Preventive (this §13)** — guides new framework decisions; reserved-letter ledger consulted before any new notation introduction.

### §13.5 Cross-references

- **Insight #42** — Phase 2 E.3 audit; origin of NOTATION COLLISION finding; established S → τ rename.
- **Insight #50** — Phase 2 RCV acronym collision; resolved.
- **Insight #52** — Phase 2 RCV integrand Q(t) convention divergence; resolved via §B Definition A.3 expansion.
- **Insight #33** — existential substitutability gap rename; established S_max notation.
- **Insight #40** — Theorem E.4 audit; established S(t) substitutability-function notation discipline.
- **Insight #55 OPEN** — Framework-wide notation collision audit (one-time retroactive sweep); informs Phase 3 v2.0.0 rebuild.
- **Insight #39 OPEN** — Pre-publication external review; notation-discipline reviewer is one of the multi-perspective reviewers warranted.
- **Routine 1** — daily terminology-regression sentinel extended with notation-collision patterns (#9 specific S → τ; #10 reserved-letter ledger general).
- **Routine 2** — weekly pre-submission readiness audit extended with comprehensive notation-collision sweep (check #5).
- **Phase 3 Tech Appendix v2.0.0 rebuild** — downstream implementation venue for any collision-resolution renames identified by Insight #55 audit.

---

**End of vocabulary strategy v1.0.1 [RATIFIED 2026-04-28 by Chris Winn; §13 notation-discipline added 2026-04-29 per Insight #55].**
