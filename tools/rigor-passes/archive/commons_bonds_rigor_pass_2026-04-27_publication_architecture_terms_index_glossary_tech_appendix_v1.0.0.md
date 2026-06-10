# Commons Bonds — Full Rigor Pass: Publication Architecture (terms_index + Glossary + Tech Appendix)

**Version:** 1.0.0
**Date:** 2026-04-27
**Protocol applied:** `tools/commons_bonds_rigor_protocol_v2.3.0.md` — full 12-module suite + §22 + §22.4 + all 6 Working Principles. Special focus on M3 (book content / artifact scope), M6 (academic), M8 (long-term / test-of-time), M10 (publishing), M11 (critic survival), M12 (intellectual honesty).
**Scope:** Tests the publication architecture for the framework's three primary term-bearing artifacts:
- `core/terms/terms_index.md` (1,796 lines, 147 KB) — internal source-of-truth carrying status indicators + rigor provenance + decision history + dependency graphs per framework term.
- `core/glossary/archive/commons_bonds_updated_glossary_v3.html` (406 lines, 39 KB) — reader-facing definitions.
- `core/technical-appendix/TechnicalAppendix_v1.0.0.html` (7,438 lines, 302 KB) — currently dual-purpose: math + worked examples + scaffolding/rigor-trail mixed.

Tests four interacting questions: (1) the architecture pattern (status quo vs upstream-source-of-truth vs merge); (2) per-term schema in terms_index; (3) synthesis-content boundary for Tech Appendix; (4) maintenance discipline (manual vs tooling). Per author directive 2026-04-27: *"It's probably time to make a task to merge the core/glossary and the core/terms/terms_index.md or perhaps the terms_index really needs to turn into the scaffolding for the technical appendix & the glossary?"* + ratified follow-up: *"the terms_index become the upstream source-of-truth that derives both Tech Appendix + glossary as downstream publication artifacts does seem to have a lot of merit if that's what you would suggest."*

**Status:** rigor pass executed 2026-04-27; **ratified 2026-04-27 by Chris Winn** — full ratification of A2 + S1 + B1 + M1 (upstream-source-of-truth hybrid; audience-specific rendering fields per term; Tech Appendix carries synthesis content not in terms_index; manual maintenance discipline initially).
**Author:** Chris Winn

---

## §1. Executive summary

**RECOMMENDED:** Option **A2 + S1 + B1 + M1** — adopt the **upstream-source-of-truth hybrid architecture** with terms_index driving definitional content for both downstream publication artifacts; manual maintenance discipline; phased implementation across Tech Appendix v2.0.0 rebuild + Glossary v4 rebuild + ongoing maintenance.

**Decisive findings:**

1. **The pattern is already half-documented in terms_index §2.** terms_index §2 already states: *"Glossary [...] is updated to short gloss entries that reference their full record in this index. Glossary becomes the user-facing lookup; this index is the provenance source-of-truth."* The architecture rigor pass extends this established discipline from Glossary-only to **Glossary + Tech Appendix**, with explicit per-term schema for audience-tailored renderings.

2. **Merging glossary + terms_index (rejected).** Different audiences (reader vs author/rigor-process) + different update cadences (reader-register polish vs rigor-pass ratification) + fundamentally different content depth (concise gloss vs full provenance). Single artifact cannot serve both registers without one losing its identity. **Reject merge; adopt upstream-source pattern instead.**

3. **Tech Appendix v1.0.0 currently violates separation-of-concerns at scale.** Earlier scope investigation (commit thread bcd0c51 + queued v2.0.0 rebuild) confirmed substantial issues:
   - **Retired-terminology residue** (e.g., §C.2 "Seven Abundance Dimensions" entire AIT-era enumeration; "v0.0.5 additions" framing block at line 331; theorem E.3 "Abundance Masking"; "v0.0.5 canonical-cohort note" at line 1350; line 6658 AIT/Abundance-Inversion archaeology)
   - **Rigor-scaffolding content pervasive throughout** (every major section carries "Backed by [X] rigor pass (commit XXX)" pattern; M11 character probes inline at lines 1600 + 1713; §18 + §19 entire sections are scaffolding; status-indicator definitions at lines 191-205; pre-v1.0.0 version-progression archaeology)
   - These are exactly the publisher / literary-agent readiness blockers the upstream-source pattern resolves: **scaffolding moves to terms_index (or to a dedicated internal-only `core/scaffolding/` doc); publication artifacts derive only the substantive terminological + synthesis content.**

4. **Hybrid model required for Tech Appendix.** Tech Appendix has substantial **synthesis content** (math, proofs, theorems, worked examples, convergence arguments, integration narrative) that doesn't decompose into per-term records. Per-term derivation gives the definitional sections; synthesis content stays manually maintained.

5. **Per-term schema extension.** terms_index entries currently carry working_definition + status + provenance + dependencies + commit_trail. Architecture rigor pass adds:
   - `glossary_definition` (~80 words; reader-register; one example)
   - `tech_appendix_definition` (~300 words; formal + lineage citations + math notation)
   - **Internal fields stay internal** (rigor_provenance, decision_history, M11_char_probes, rigor_pass_commit_refs).

6. **Manual maintenance discipline (M1) over generation tooling (M2).** Manual is simpler, more flexible for the prose-heavy Tech Appendix synthesis, and doesn't require toolchain investment. Generation tooling can be added later if discipline drift surfaces. Manual discipline: any term-related change touches terms_index FIRST; downstream derivation propagates manually; CI check optional.

7. **Versioning lockstep.** terms_index v1.X → Glossary v4.X → Tech Appendix v2.X derives from each terms_index version. When terms_index updates, downstream artifacts regenerate at next release point.

8. **M8 test-of-time STRONGLY favors this architecture.** Books and frameworks that have stood the test of time (Ostrom, Mazzucato, Sen-Nussbaum capabilities approach) consistently maintain a single source-of-truth for terminology; the framework's discipline matches that pattern. Status-quo (multiple sources, drift risk) is the durability risk.

**Net verdict:** Adopt upstream-source-of-truth hybrid architecture; manual discipline; phased implementation. Strengthens M3 + M6 + M8 + M10 + M11 + M12. Closes Tech Appendix publication-readiness blocker. Establishes durable maintenance pattern.

---

## §2. The question under test

### §2.1 Author's question (compound, surfaced 2026-04-27)

> *"It's probably time to make a task to merge the core/glossary and the core/terms/terms_index.md or perhaps the terms_index really needs to turn into the scaffolding for the technical appendix & the glossary?"*

> *(follow-up after my recommendation surface)* *"the terms_index become the upstream source-of-truth that derives both Tech Appendix + glossary as downstream publication artifacts does seem to have a lot of merit if that's what you would suggest."*

### §2.2 Four sub-questions

1. **Architecture (Axis A):** What is the relationship between terms_index, Glossary, and Tech Appendix?
2. **Per-term schema (Axis S):** What fields belong in terms_index? What renderings does each term carry for downstream artifacts?
3. **Synthesis-content boundary (Axis B):** What content stays in Tech Appendix that doesn't derive from terms_index?
4. **Maintenance discipline (Axis M):** Manual vs tooling-enforced derivation?

### §2.3 Options under test

**Architecture (Axis A):**
- **A1:** Status quo — three independent artifacts; ad-hoc consistency between them.
- **A2:** Upstream-source-of-truth hybrid — terms_index drives definitional content; Tech Appendix adds synthesis content. **RECOMMENDED.**
- **A3:** Full merge — collapse glossary + terms_index into one artifact.
- **A4:** Tooling-driven generation — terms_index has machine-derivable fields; Glossary + Tech Appendix sections auto-generated.

**Per-term schema (Axis S):**
- **S1:** Add audience-specific rendering fields (`glossary_definition`, `tech_appendix_definition`) to existing terms_index template. **RECOMMENDED.**
- **S2:** Single working_definition; downstream artifacts derive renderings via authorial judgment per artifact.
- **S3:** Per-audience structured fields (more granular: `concise_definition`, `formal_definition`, `lineage_citation`, `math_notation`, `worked_example_pointer`, etc.).

**Synthesis boundary (Axis B):**
- **B1:** Tech Appendix carries substantial synthesis content (math, proofs, theorems, worked examples, convergence arguments) NOT in terms_index; per-term sections derive from terms_index. **RECOMMENDED.**
- **B2:** Maximally reduce Tech Appendix synthesis content (keep only what's strictly term-derivable; move math/proofs/worked-examples to separate `core/math/` doc).
- **B3:** Maximally expand terms_index to absorb math/proofs/worked-examples (single artifact carries all).

**Maintenance discipline (Axis M):**
- **M1:** Manual discipline (terms_index touched first; downstream regeneration manual). **RECOMMENDED.**
- **M2:** Generation tooling (script regenerates Glossary; partial regeneration of Tech Appendix definitional sections).
- **M3:** Hybrid (manual for synthesis; tooling for term-by-term sections).

### §2.4 Falsifiers

- **A2 falsified if:** Tech Appendix's synthesis content is so tightly coupled to per-term records that the boundary becomes impractical (would push toward A4 tooling).
- **A2 falsified if:** Manual discipline drift over 3-6 month period creates inconsistencies the upstream-source pattern was supposed to prevent (would push toward M2 tooling).
- **S1 falsified if:** Author finds the audience-specific rendering fields awkward to maintain; would push toward S2 (single definition + judgment) or S3 (more granular structure).
- **B1 falsified if:** Splitting math/proofs/worked-examples into a separate doc improves publication-readiness more than keeping them in Tech Appendix (would push toward B2).

---

## §3. Current state investigation

### §3.1 Three artifacts catalogued

| Artifact | Path | Size | Audience | Current status |
|---|---|---|---|---|
| `terms_index.md` | core/terms/ | 1,796 lines / 147 KB | author + framework rigor process | active source-of-truth; per-term records well-structured |
| `glossary_v3.html` | core/glossary/ | 406 lines / 39 KB | reader (general / pop) | current public-glossary; references terms_index implicitly |
| `TechnicalAppendix_v1.0.0.html` | core/technical-appendix/ | 7,438 lines / 302 KB | academic reviewer / serious researcher | dual-purpose: math + scaffolding mixed |

### §3.2 terms_index per-term template (current state)

Per terms_index §1 (lines 24-50):

```markdown
### <Term>

**Working definition:** <current definition — no claim of finality>

**Status:** [CURRENT / PENDING-RIGOR / UNDER-REVIEW / SUPERSEDED / RETIRED]

**Depends on (framework decisions this term rests on):**
- <Decision 1> — <brief description>

**Staleness triggers (what would require re-review):**
- <Upstream change 1>

**Commit trail:** <most relevant commit refs>

**Supersedes / superseded by:** <if applicable>

**Notes:** <optional>
```

Plus extended fields appearing on substantive entries: M12 lineage, Bibliography references, Cross-references.

**Finding:** template is rich on internal-process-state (status, dependencies, staleness, commits) but **lacks audience-specific rendering fields** (no separate glossary_definition or tech_appendix_definition). Currently each term has ONE working_definition that downstream artifacts paraphrase per their register.

### §3.3 terms_index already documents upstream-source pattern (partial)

Per terms_index §2 (Integration with other framework docs):

> *"Glossary (core/glossary/archive/commons_bonds_updated_glossary_v2.html) is updated to short gloss entries that reference their full record in this index. **Glossary becomes the user-facing lookup; this index is the provenance source-of-truth.**"*

**Finding:** the upstream-source-of-truth pattern is ALREADY ratified and documented for Glossary-vs-terms_index. The architecture rigor pass extends this established discipline to Tech Appendix.

Note: the §2 reference to `glossary_v2.html` is itself a reference-drift artifact (current Glossary is v3); minor maintenance issue but indicative of why explicit upstream-source discipline matters.

### §3.4 Tech Appendix v1.0.0 substance vs scaffolding inventory

From earlier scope investigation (commit thread leading to v2.0.0 rebuild queue):

**Substance (publication-ready):**
- §1 Foundations — Formal Definitions and Primitives
- §2 Two-Instrument Architecture
- §3 RCV Quantification — Triangulated Estimation
- §4 Hotelling Identity
- §5 Accountability Bond Decomposition
- §6 Commons Inversion Test
- §7 Four Gates Admission Apparatus
- §8 Asymmetric Regret Rule
- §9 Three-Model Convergence Framework
- §10 Theorems and Proofs
- §11 Empirical Validation Cases
- §12 Boundary-Awareness Scope Claim
- §13 Substitutability Function
- §14 Engagement with Existing Literature
- §15 Limitations and Boundary Conditions
- §16 Mathematical Extensions
- §17 Formula Generalization

**Scaffolding (NOT publication-ready):**
- §18 Working Principles + Open Insights Cross-Reference (entire section)
- §19 Provenance & Cross-References (entire section)
- Pervasive "Backed by [X] rigor pass (commit XXX)" footer pattern at every major section
- M11 character probes inline (Char 12 graduate student at line 1600; Char 17 Ostrom-successor at line 1713)
- Status-indicator definitions at lines 191-205 (CURRENT / PENDING-RIGOR / etc.)
- "Scope progress (Open Insight #21 Path B)" header block
- "v0.0.5 additions" framing block + version-progression archaeology

**Retired-vocabulary residue:**
- §C.2 "Seven Abundance Dimensions" entire AIT-era enumeration (~lines 1347-1405)
- Theorem E.3 "Abundance Masking" (line 3296)
- "v0.0.5 canonical-cohort note" (line 1350)
- "Eight-Tier" reference (line 1228)
- Long AIT/Abundance-Inversion archaeology (line 6658)
- Inline "AIT's pre-CIT framing obscured this" (line 1882)

### §3.5 Glossary v3 structure

Currently 406 lines; reader-facing HTML. Each term entry presumably carries a concise definition + example. Detailed verification deferred to implementation phase.

---

## §4. Axis A — Architecture pattern

### §4.1 A1 (status quo) analysis

Three independent artifacts; ad-hoc consistency:
- terms_index gets updated when rigor passes ratify changes
- Glossary gets updated when reader-register polish lands
- Tech Appendix gets updated... when? (currently unclear discipline)

Drift risk: HIGH. Term definitions can diverge between artifacts; status changes (e.g., RETIRED) may not propagate. Already evident: terms_index §2 references Glossary v2; current Glossary is v3 — internal-document drift on a documented integration point.

M3 / M6 / M11 weaknesses: a reviewer comparing Tech Appendix's definition to Glossary's may find inconsistencies; framework's vocabulary discipline appears compromised.

### §4.2 A2 (upstream-source hybrid) analysis — RECOMMENDED

terms_index = source-of-truth. Glossary derives definitional content. Tech Appendix derives definitional content + carries synthesis content not in terms_index.

```
terms_index.md  [UPSTREAM SOURCE-OF-TRUTH — internal]
  Per term:
    • working_definition  (canonical formal)
    • glossary_definition  (~80 words, reader-register)  [NEW FIELD]
    • tech_appendix_definition  (~300 words, formal + lineage)  [NEW FIELD]
    • status (CURRENT / PENDING-RIGOR / UNDER-REVIEW / SUPERSEDED / RETIRED)
    • rigor_provenance  [internal — never in publication artifacts]
    • decision_history  [internal]
    • downstream_dependencies  [internal — informs propagation]
    • commit_trail  [internal]
       │
       ▼ derives
   ┌───┴───────────────────────────────────────────┐
   │                                               │
   ▼                                               ▼
Glossary  [DOWNSTREAM PUBLICATION]               Tech Appendix  [DOWNSTREAM + SYNTHESIS]
  • CURRENT terms only                              • CURRENT terms' tech_appendix_definition
  • Reader-register                                 • PLUS synthesis content (NOT in terms_index):
  • Direct derivation                                    - Math, proofs, theorems
  • Periodic regeneration                                - Worked examples (Block 4, Method 3, etc.)
                                                         - Convergence arguments
                                                         - Integration narrative
                                                    • Internal-scaffolding REMOVED:
                                                         - Rigor-pass references
                                                         - "Backed by X" citations
                                                         - M11 character probes
                                                         - Status-indicator definitions
                                                         - Version-progression archaeology
```

### §4.3 A3 (merge) analysis — REJECTED

Merging Glossary + terms_index forces one of them to lose its identity:
- If merged-artifact retains terms_index's internal-scaffolding richness (status indicators, rigor provenance, decision history, dependency graphs), it becomes unreadable as a reader-facing glossary.
- If merged-artifact is reader-cleaned, terms_index loses its rigor-process-tracking value.
- Different audiences require different content depth + register; one artifact can't serve both well.
- Different update cadences couple artifacts that should update independently.

**REJECTED.**

### §4.4 A4 (tooling-driven generation) analysis

Per-term records have machine-readable fields; Glossary + Tech Appendix definitional sections regenerated by script.

Pros:
- Strict consistency enforcement
- Updates propagate automatically
- Versioning lockstep enforced

Cons:
- Toolchain investment (Python or similar; HTML rendering complexity)
- Tech Appendix synthesis content can't be auto-generated (still manual)
- Flexibility loss for prose-heavy passages

**Verdict:** A4 is a future-state to consider if A2 + manual discipline drifts. Don't start there. Start with A2 + manual; tool only when proven needed.

### §4.5 Verdict on Axis A

**A2 (upstream-source hybrid) is dominant.** Strong on M3 + M6 + M8 + M11 + M12. Aligned with terms_index §2 already-ratified Glossary discipline; extends to Tech Appendix.

---

## §5. Axis S — Per-term schema

### §5.1 Recommended schema extension (S1)

Add to existing terms_index template:

```markdown
### <Term>

**Working definition:** <canonical formal definition — basis for downstream renderings>

**Status:** [CURRENT / PENDING-RIGOR / UNDER-REVIEW / SUPERSEDED / RETIRED]

**Glossary definition (~80 words, reader-register):**
> <Concise reader-facing definition + brief example. Avoids math notation; uses everyday register; one concrete instance.>

**Tech Appendix definition (~300 words, formal + lineage):**
> <Formal definition + math notation if applicable + lineage citations + how it relates to adjacent traditions. May include sub-section structure if term has multiple operational forms.>

**Depends on:** [internal — staleness graph]
**Staleness triggers:** [internal]
**Commit trail:** [internal — provenance]
**Supersedes / superseded by:** <if applicable>
**M12 lineage:** [internal — adjacent academic traditions]
**Notes:** [internal]
```

### §5.2 Schema rationale

- `working_definition` = the author's canonical formal articulation; basis for all downstream renderings. Currently exists.
- `glossary_definition` (NEW) = pre-rendered reader-facing concise version. Avoids round-trip translation overhead per rebuild. ~80 words target.
- `tech_appendix_definition` (NEW) = pre-rendered formal academic-register version with lineage. ~300 words target.
- Internal fields (Depends on / Staleness / Commit / M12 lineage / Notes) stay as currently in terms_index. NEVER appear in publication artifacts.

### §5.3 S2 vs S1 evaluation

S2 (single working_definition; authorial paraphrase per artifact): introduces translation drift risk. Same definition rendered twice from one source can produce slightly different reader-facing versions; consistency depends on author memory of prior paraphrase.

S1 (pre-rendered audience-specific fields): explicit; consistent across rebuilds; lower author cognitive load (write once per audience; reuse forever until rigor change).

**S1 dominant.**

### §5.4 S3 (more granular structure) evaluation

S3 splits into many smaller fields: concise_definition, formal_definition, lineage_citation, math_notation, worked_example_pointer, etc.

Pros: maximally machine-readable; supports A4 tooling.
Cons: maintenance overhead; over-engineering for current scope; rigid structure may not fit all term types.

**S3 deferred — adopt S1 first; consider S3 if A4 tooling is later adopted.**

### §5.5 Verdict on Axis S

**S1 (audience-specific rendering fields) is dominant.** Pre-rendered concise + formal definitions per term; internal fields stay internal.

---

## §6. Axis B — Synthesis-content boundary

### §6.1 What goes in terms_index (per-term content)

- Definitions (working / glossary / tech_appendix)
- Status + provenance + dependencies + commit trail
- M12 lineage (adjacent traditions per term)
- Notes
- Cross-references TO other terms_index entries

### §6.2 What stays in Tech Appendix (synthesis content NOT in terms_index)

- Math (RCV integral; sum-of-costs general form; convergence proofs)
- Theorems and proofs (Theorem 1: Integral Convergence; Theorem 2: Renewable Imperative; etc.)
- Worked examples (McDowell coal walkthrough; Norway Backtest empirical; Block 4 validation; Method 3 sensitivity analysis; DAC three-horizon)
- Convergence arguments (three approaches converging on CS > 0)
- Integration narrative (how CIT + Four Gates + Three Ways + B = B₁ + B₂ work together)
- Empirical validation cases (per-case detailed analysis)
- Engagement with existing literature (essay-form; not per-term)
- Boundary-awareness scope claim (Mars/Europa illustrations)
- Limitations and Boundary Conditions

### §6.3 What goes to scaffolding (internal-only doc, NEVER in publication)

- Rigor-pass commit references
- M11 character probes
- Status-indicator definitions (these are in terms_index §1; internal context only)
- Version-progression archaeology
- "Backed by [X] rigor pass" footer pattern
- Open Insight cross-references
- Working Principle invocations

This scaffolding can live in:
- terms_index per-term records (for term-specific provenance)
- A new `core/scaffolding/tech_appendix_provenance.md` doc (for Tech-Appendix-specific synthesis-content provenance — which rigor passes ratified which proofs, etc.)

### §6.4 B2 (maximally reduce Tech Appendix synthesis) evaluation

Move math/proofs/worked-examples to separate `core/math/` doc. Tech Appendix becomes pure derived-from-terms_index document.

Pros: cleanest publication artifact.
Cons: math/proofs/worked-examples NEED to be in Tech Appendix for academic-reviewer audience; splitting forces reviewer to chase across docs.

**REJECTED.**

### §6.5 B3 (maximally expand terms_index) evaluation

Absorb math/proofs/worked-examples into terms_index per-term records.

Pros: single artifact carries everything.
Cons: terms_index becomes massive (already 1,796 lines); per-term records bloat; cross-term synthesis (theorems combining multiple terms) doesn't fit per-term structure.

**REJECTED.**

### §6.6 Verdict on Axis B

**B1 (Tech Appendix carries synthesis content not in terms_index) is dominant.** Per-term content derives from terms_index; synthesis content stays in Tech Appendix as section-level material.

---

## §7. Axis M — Maintenance discipline

### §7.1 M1 (manual discipline) — RECOMMENDED

Workflow:
1. Any term-related change touches terms_index FIRST.
2. Author updates `glossary_definition` + `tech_appendix_definition` fields per term.
3. At next Glossary release: regenerate Glossary v4.X by manually pulling glossary_definition fields from CURRENT terms.
4. At next Tech Appendix release: update term-derived sections by manually pulling tech_appendix_definition fields; preserve synthesis content; update version.
5. Versioning lockstep: terms_index v1.X → Glossary v4.X derives → Tech Appendix v2.X derives.

Pros: simple; flexible; no toolchain investment; supports prose-heavy synthesis content.
Cons: discipline drift risk (author forgets to update terms_index first); potential for inconsistency if discipline fails.

### §7.2 M2 (generation tooling) evaluation

Script regenerates Glossary (full); regenerates Tech Appendix per-term sections (partial — synthesis content untouched).

Pros: enforced consistency; updates propagate; versioning lockstep automated.
Cons: toolchain investment (Python + HTML rendering); brittleness for prose-heavy edge cases; debugging cost.

**Defer to future; start with M1.**

### §7.3 M3 (hybrid) evaluation

Manual for synthesis content; tooling for per-term sections.

**Same conclusion: defer to future state if M1 drifts; not initial recommendation.**

### §7.4 Verdict on Axis M

**M1 (manual discipline) is dominant for initial implementation.** Optional CI check or pre-commit hook can flag downstream-only changes for review (e.g., "this Glossary diff has no corresponding terms_index update — confirm intentional").

---

## §8. Per-artifact analysis (concrete implementation)

### §8.1 terms_index.md

**Current state:** 1,796 lines; each term has working_definition + status + provenance.

**Restructure (Phase 2):**
- Add `glossary_definition` field to each term (CURRENT-status terms first)
- Add `tech_appendix_definition` field to each term (CURRENT-status terms first)
- Update template in §1 to reflect new schema
- Update §2 (Integration with other framework docs) to add Tech Appendix discipline alongside Glossary
- Bump version: terms_index v0.1.0 (skeleton) → v1.0.0 (audience-specific renderings established)
- Estimated work: ~30 terms in CURRENT status; ~10-30 minutes per term to author both rendering fields = ~10-15 hours

**Maintenance going forward:** any rigor-pass ratification affecting a term updates the affected fields (working / glossary / tech_appendix definitions) in same commit as the rigor-pass ratification.

### §8.2 Glossary v4

**Current state:** Glossary v3.html exists; reader-facing.

**Rebuild (Phase 4):**
- Derive directly from terms_index CURRENT-status terms' glossary_definition fields
- Reader-register pretty-printed HTML (matches Tech Appendix Option A semantic HTML format)
- Alphabetical or topical organization (TBD; alphabetical is simpler)
- Version: v4.0 derived from terms_index v1.0.0
- Estimated work: ~3-5 hours assuming terms_index restructure (Phase 2) is complete

**Maintenance going forward:** at each Glossary release point, regenerate from current CURRENT terms.

### §8.3 Tech Appendix v2.0.0

**Current state:** v1.0.0 has substantial issues per §3.4 inventory.

**Rebuild (Phase 3):**

a. **Strip retired-vocabulary residue:**
   - Excise §C.2 "Seven Abundance Dimensions" entire section
   - Remove "v0.0.5 additions" framing block at line 331
   - Remove theorem E.3 "Abundance Masking"
   - Remove "v0.0.5 canonical-cohort note" at line 1350
   - Remove "Eight-Tier" reference at line 1228
   - Remove AIT/Abundance-Inversion archaeology at line 6658
   - Sweep all "AIT's pre-CIT" / "Abundance Inversion" prose

b. **Strip rigor-scaffolding content:**
   - Remove §18 "Working Principles + Open Insights Cross-Reference" entirely
   - Remove §19 "Provenance & Cross-References" entirely
   - Remove "Backed by [X] rigor pass (commit XXX)" footer pattern from every major section
   - Remove M11 character probes (Char 12 / Char 17 inline references)
   - Remove status-indicator definitions at lines 191-205
   - Remove "Scope progress (Open Insight #21 Path B)" header block
   - Remove version-progression archaeology

c. **Rebuild definitional content** as derived from terms_index `tech_appendix_definition` fields per term:
   - §1 Foundations: derives from terms_index Cost Severance + RCV + CSD + Cᵢ + B + S + IPG entries
   - §2 Two-Instrument Architecture: derives from terms_index B₁ + B₂ entries + B = B₁ + B₂ relational claim
   - §3 RCV Quantification: derives from terms_index Three Ways of Counting + Method 1 + Method 2 + Method 3 entries
   - §4 Hotelling Identity: derives from terms_index Hotelling Identity entry
   - §5 Accountability Bond Decomposition: derives from terms_index Accountability Bond + Restitution Bond + Foreclosure Bond
   - §6 CIT: derives from terms_index Commons Inversion Test + CAI + CCI entries
   - §7 Four Gates: derives from terms_index Four Gates + Units Consistency + Boundedness + Independence
   - §8 ARR: derives from terms_index Asymmetric Regret Rule entry
   - §13 Substitutability Function: derives from terms_index Substitutability Function entry

d. **Preserve synthesis content** (manual maintenance):
   - §9 Three-Model Convergence Framework
   - §10 Theorems and Proofs
   - §11 Empirical Validation Cases
   - §12 Boundary-Awareness Scope Claim
   - §14 Engagement with Existing Literature
   - §15 Limitations and Boundary Conditions
   - §16 Mathematical Extensions
   - §17 Formula Generalization

e. **Move scaffolding to internal doc:** new `core/scaffolding/tech_appendix_provenance.md` carries the rigor-pass commits, Working Principle invocations, M11 probe history, status-indicator decisions for synthesis content. NEVER in publication artifact.

f. **Version:** Tech Appendix v2.0.0 (clean rebuild from terms_index v1.0.0 + synthesis content)

g. **Estimated work:** ~20-30 hours (substantial rebuild). Could be split across 2-3 sessions.

### §8.4 New scaffolding doc

`core/scaffolding/` directory (new):
- `tech_appendix_provenance.md` — Tech Appendix synthesis content's rigor-pass provenance, M11 probe history, Working Principle invocations.
- `chapter_provenance.md` (potentially) — chapter-prose provenance for any inline-woven framework material that has rigor-trail (e.g., Ch 6's Restitution Lineage references Restitution Bond per b1_b2_naming pass).

Audience: author + future-rigor-pass workflows. NEVER reaches reader / publisher / literary agent.

---

## §9. M1–M11 abbreviated module results

| Module | A2 + S1 + B1 + M1 performance |
|---|---|
| **M1 CORE math** | PASS — math unchanged; preserved in Tech Appendix synthesis content |
| **M2 Case study** | PASS — cases unchanged; preserved in Tech Appendix §11 Empirical Validation |
| **M3 Book content** | **STRENGTHENS** — Tech Appendix becomes publication-ready; Glossary becomes derived-consistent; terms_index becomes upstream source-of-truth for vocabulary discipline |
| **M3.4 Counterargument coverage** | UNCHANGED — counterargument-handling is chapter-prose content (per 2026-04-27 ratified inline-woven discipline); not affected by this rigor pass |
| **M4 Craft** | **STRENGTHENS** — Tech Appendix's prose register stays consistent within publication-ready scope; scaffolding noise removed |
| **M5 Dinner-table** | UNCHANGED — Glossary serves dinner-table register; Tech Appendix serves academic register; appropriate to audience |
| **M6 Academic** | **STRENGTHENS** — academic reviewers see clean Tech Appendix without scaffolding noise; vocabulary consistency across artifacts; proper citation discipline |
| **M7 Originality** | UNCHANGED — framework's originality is in the substance; architectural cleanup doesn't affect |
| **M8 Long-term / test-of-time** | **STRONGLY STRENGTHENS** — single source-of-truth pattern is durable across decades; ensures vocabulary consistency as framework evolves; matches successful adjacent-framework maintenance patterns |
| **M9 Risk** | **REDUCES** — drift risk between artifacts (currently HIGH under A1 status quo) becomes LOW under A2 + M1 manual discipline; further reducible via M2 tooling if needed |
| **M10 Publishing** | **STRONGLY STRENGTHENS** — publication-ready Tech Appendix v2.0.0 is what gets sent to publisher / literary agent; scaffolding stays internal; matches publishing-industry expectations |
| **M11 Critic** | **STRENGTHENS** — academic reviewers comparing Glossary to Tech Appendix to chapter prose find consistent definitions across artifacts; framework's vocabulary discipline visible |

**§22 alignment:** A2 + S1 + B1 + M1 positive on Primary Goals — Publishing Path (clean publication artifacts); Academic Reception (consistency + scaffolding-free); Long-term Impact (durable maintenance pattern); Adoption-Bandwidth (single source-of-truth signals professional discipline).

**§22.4 stand-test-of-time alignment:** STRONGLY POSITIVE.

---

## §10. M12 — Intellectual honesty audit

### §10.1 A2 (upstream-source hybrid) M12

- **Rigor provenance separated from publication content** — terms_index keeps rigor-pass commit refs internally; publication artifacts get substantive content. Honest about what's reader-facing vs internal.
- **Status discipline visible upstream + filterable downstream** — RETIRED terms stay in terms_index (decision-history record) but never reach reader. Honest about which terms are current vs historical.
- **Per-term audience-specific renderings** — explicit pre-rendered fields, not on-the-fly paraphrase. Honest about what each audience sees.

**M12 PASSES at strongest register.**

### §10.2 A1 (status quo) M12

- Drift risk creates unintended inconsistencies. Reader sees one definition in Glossary; academic reviewer sees a different one in Tech Appendix; framework's vocabulary discipline appears compromised.
- **M12 ADEQUATE but vulnerable.**

### §10.3 A3 (merge) M12

- Forces one audience's content to dominate; either reader sees scaffolding (un-honest about audience-fitness) or rigor-process loses internal value (un-honest about provenance need).
- **M12 FAILS at audience-honesty register.**

### §10.4 M12 verdict

**A2 + S1 + B1 + M1 is M12-optimal.**

---

## §11. Cross-chapter implications

### §11.1 What this rigor pass affects beyond the three artifacts

- **Chapter prose** that references framework terms continues to use working_definition vocabulary; no chapter-restructure required.
- **Cross-chapter sweep** (counterargument-handling discipline, queued for Ch 2 / Ch 4 / Ch 5 / Ch 7 / Ch 8 / Ch 9 / Ch 10) is independent; can run in parallel with or after this architecture work.
- **Future rigor passes** end with terms_index impact assessment per terms_index §1 staleness-detection discipline; this discipline is reinforced by the architecture rigor pass.

### §11.2 What this rigor pass does NOT affect

- Framework intellectual content — unchanged.
- Math, proofs, theorems — preserved in Tech Appendix synthesis content.
- Empirical validation cases — preserved.
- Bibliography references — unchanged.

---

## §12. Verdict synthesis + recommendation

### §12.1 Recommended combination

**A2 + S1 + B1 + M1.**

- A2: Upstream-source-of-truth hybrid (terms_index drives definitional content; Tech Appendix adds synthesis)
- S1: Audience-specific rendering fields per term (glossary_definition + tech_appendix_definition)
- B1: Tech Appendix carries synthesis content not in terms_index (math, proofs, worked examples)
- M1: Manual maintenance discipline (initial; M2 tooling deferred)

### §12.2 Three rigor questions on the architecture

| Question | Verdict |
|---|---|
| **Earns place?** | **YES** — the upstream-source-of-truth pattern is already half-documented in terms_index §2 (for Glossary); this rigor pass extends it to Tech Appendix and formalizes the per-term schema. |
| **Would expansion strengthen?** | **PARTIALLY** — Phase 5 (M2 tooling) could automate derivation; defer until M1 manual discipline shows drift. |
| **Would compression strengthen?** | **NO** — A3 merge collapses audience-distinctions; B2/B3 force-fit content; S2 introduces translation drift. All collapsed alternatives are worse. |

### §12.3 Implementation phases

| Phase | Work | Estimated hours |
|---|---|---|
| **1. Architectural ratification** (this rigor pass) | Author ratifies A2 + S1 + B1 + M1 | <1 |
| **2. terms_index restructure** | Add glossary_definition + tech_appendix_definition fields per CURRENT term; update template; update §2; bump version | 10-15 |
| **3. Tech Appendix v2.0.0 rebuild** | Strip retired-vocabulary; strip scaffolding; rebuild definitional sections from terms_index; preserve synthesis; move scaffolding to internal-only doc | 20-30 |
| **4. Glossary v4 rebuild** | Derive from terms_index CURRENT terms' glossary_definition; reader-register HTML | 3-5 |
| **5. Maintenance discipline** | terms_index touched first for any term change; downstream derivation manual; versioning lockstep | ongoing |

Total Phase 2-4 implementation: **~33-50 hours**, splittable across 3-5 dedicated sessions.

### §12.4 Rejected alternatives + rationale

| Alternative | Rejected because |
|---|---|
| **A1 (status quo)** | Drift risk; inconsistency between artifacts; M3/M6/M11 weakness; current Tech Appendix v1.0.0 publication-readiness blocked |
| **A3 (merge glossary + terms_index)** | Forces audience-content to dominate; one artifact loses identity; M12 audience-honesty fails |
| **A4 (full tooling)** | Premature optimization; toolchain investment cost; flexibility loss for prose-heavy synthesis; defer to future state |
| **S2 (single working_definition + judgment)** | Translation drift risk; consistency depends on author memory |
| **S3 (granular structured fields)** | Over-engineering for current scope; rigid structure may not fit all terms; defer |
| **B2 (move math/proofs to separate doc)** | Splits academic-reviewer experience; chasing across docs |
| **B3 (absorb math/proofs into terms_index)** | terms_index bloat; cross-term synthesis doesn't fit per-term structure |
| **M2/M3 (tooling-driven)** | Premature; start with M1 manual; tool only when proven needed |

---

## §13. Author-ratified resolutions

**Ratified 2026-04-27 by Chris Winn — full ratification of A2 + S1 + B1 + M1.**

1. **A2 — UPSTREAM-SOURCE-OF-TRUTH HYBRID architecture.** terms_index becomes the upstream source-of-truth for both Glossary and Tech Appendix downstream artifacts. Tech Appendix carries synthesis content (math, proofs, theorems, worked examples) that doesn't decompose into per-term records.

2. **S1 — AUDIENCE-SPECIFIC RENDERING FIELDS** added to terms_index per-term schema:
   - `glossary_definition` (~80 words, reader-register, one example)
   - `tech_appendix_definition` (~300 words, formal + lineage citations)
   - Internal fields (rigor_provenance, decision_history, M11 character probes, rigor-pass commit refs) stay internal — NEVER appear in publication artifacts.

3. **B1 — TECH APPENDIX SYNTHESIS-CONTENT BOUNDARY.** Tech Appendix carries math, proofs, theorems, worked examples (Block 4, Method 3, DAC three-horizon), convergence arguments, integration narrative, empirical validation cases, engagement-with-existing-literature, boundary-awareness scope claim, limitations — all NOT in terms_index. Per-term sections derive from terms_index. Internal-scaffolding (rigor-pass references, M11 probes, status-indicator definitions, version-progression archaeology) MOVED to new `core/scaffolding/tech_appendix_provenance.md`.

4. **M1 — MANUAL MAINTENANCE DISCIPLINE** initially. Workflow: any term-related change touches terms_index FIRST; downstream regeneration manual; versioning lockstep (terms_index v1.X → Glossary v4.X → Tech Appendix v2.X). Optional CI check or pre-commit hook for downstream-only changes (deferred). M2 generation tooling reconsidered if M1 manual discipline drifts over 3-6 months.

**Implementation phases activated (per §12.3):**
- **Phase 1** (this rigor pass): architectural ratification — COMPLETE.
- **Phase 2** (~10-15 hrs): terms_index restructure — add glossary_definition + tech_appendix_definition fields per CURRENT term; bump terms_index v0.1.0 → v1.0.0. **NEXT.**
- **Phase 3** (~20-30 hrs): Tech Appendix v2.0.0 rebuild — strip retired-vocabulary; strip scaffolding; rebuild definitional sections from terms_index; preserve synthesis content; move scaffolding to core/scaffolding/. **AFTER Phase 2.**
- **Phase 4** (~3-5 hrs): Glossary v4 rebuild — derive from terms_index CURRENT terms' glossary_definition; reader-register HTML. **AFTER Phase 2; INDEPENDENT of Phase 3.**
- **Phase 5** (ongoing): maintenance discipline activated from Phase 2 onward; future rigor passes follow upstream-touched-first workflow.

**Ratifications activated:**
- Architecture pattern: terms_index as upstream source-of-truth ratified at framework-level (extends terms_index §2 already-documented Glossary-only integration discipline to Tech Appendix).
- Per-term schema discipline: audience-specific rendering fields ratified as part of terms_index template; future rigor-pass ratifications affecting terms include glossary_definition + tech_appendix_definition updates as part of the ratification commit.
- Synthesis-content boundary discipline: math, proofs, theorems, worked examples stay in Tech Appendix as section-level material; internal-scaffolding moves to core/scaffolding/.
- Versioning lockstep discipline: terms_index v1.X → Glossary v4.X → Tech Appendix v2.X derive at each release point; cross-artifact consistency enforced.
- Manual discipline: terms_index touched FIRST for any term-related change; future rigor passes end with terms_index impact assessment per terms_index §1 staleness-detection discipline.

**Cross-references to land:**
- terms_index §2 update: replace Glossary-only integration paragraph with full A2 + B1 architecture statement covering both downstream artifacts.
- b1_b2_naming pass + counterargument-handling pass + dissolution pass: cross-reference this architecture-rigor-pass as foundation for future propagation patterns.
- Architecture-rigor-pass cross-referenced from terms_index template §1 (audience-specific rendering fields are now part of canonical schema).

---

## §14. Rerun gate

Rerun if:
- Phase 2 terms_index restructure surfaces a term whose glossary + tech_appendix renderings can't be cleanly separated (would push toward S3 granular structure).
- Phase 3 Tech Appendix rebuild surfaces synthesis content that doesn't fit B1's category (would push toward B2 split into separate math doc).
- Phase 5 manual discipline shows drift over 3-6 months (would push toward M2 tooling).
- Adjacent-framework book authors adopt different architecture pattern with measurable adoption-bandwidth advantage.
- Future Tech Appendix audience (e.g., specific academic reviewer feedback) surfaces information needs not addressed by the recommended architecture.

---

*End of full rigor pass v1.0.0 on Publication Architecture (terms_index + Glossary + Tech Appendix). A2 + S1 + B1 + M1 recommended. All 12 modules examined; decision dominated by M3 + M8 + M10 + M12 publication-readiness + maintenance-durability + intellectual-honesty findings. Implementation phased across ~33-50 hours of work splittable into 3-5 dedicated sessions. Pending author ratification.*
