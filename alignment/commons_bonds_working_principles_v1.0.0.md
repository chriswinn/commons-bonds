# Commons Bonds — Working Principles

**Version:** 1.0.0
**Established:** 2026-04-24
**Purpose:** captures ratified principles about *how* we work on this project — distinct from framework content (which lives in `core/` and `tools/`) and open insights awaiting resolution (which live in `alignment/commons_bonds_open_insights_v1.0.0.md`). Working principles are load-bearing operating rules that persist across sessions and constrain my reasoning about framework decisions, rigor passes, and option-space analysis.

---

## §0. Why this file exists

Unlike open insights (questions awaiting answers) or framework decisions (ratified framework state), working principles are about the *process* of working on the framework itself. They're articulated when a specific conversation surfaces a principle that should constrain future reasoning. Each principle has a ratification date, an originating context, and a scope.

Principles get added here when either party articulates a working rule that should persist. They can be revised or retired by explicit ratification.

---

## §1. Ratified working principles

### Principle #1 — Effort-to-repair is not a rigor argument

**Ratified:** 2026-04-24 by Chris Winn
**Originating context:** CSG (Civilizational Substitutability Gap) retirement decision. I had softened the meta-pass recommendation to retire CSG by citing the cost of rewriting Ch 7 and Ch 9 drafts. Chris corrected: *"chapter rewrite cost is nothing if skipping it causes us to fail to accomplish our success criteria. Additionally this isn't a project with a real deadline. I can complete this on my own timeline and as far as I can tell a month or two earlier or later don't really have any difference in results."*
**Scope:** applies to every rigor pass, option-space evaluation, and framework decision on this project.

**Principle statement:**

Rewrite cost, sweep cost, or any other effort-to-repair is not valid reasoning for or against a framework correctness decision. Correctness is tested on rigor grounds (M1–M11 + §22.4 alignment); effort-to-repair is a downstream scheduling question, not a rigor-level argument.

**What this changes about my reasoning:**

- When testing options, I evaluate each on rigor grounds alone. If Option X is more correct but requires 5 days of rewrite work and Option Y is less correct but costs no rewrite, the verdict is X unless rigor finds parity.
- I can *note* effort-to-repair in a downstream section of a rigor pass ("executing Condition N requires ~5 days") but this observation must not flow into the primary verdict.
- When presenting recommendations, I make the rigor case first, then separately note the downstream execution cost as a scheduling observation.
- If I catch myself softening a recommendation because the corrective work seems expensive, I stop and re-do the analysis on rigor-only grounds.

**Why this principle matters on this project specifically:**

Commons Bonds is an author-paced project with no publisher deadline or external clock forcing a decision point. A month or two of extra chapter work costs nothing the success criterion cares about. What costs the success criterion is publishing a framework whose vocabulary doesn't survive academic pressure — which is exactly what happens if weak recommendations survive because correcting them seems like too much work.

**Corollary A — scheduling notes are allowed; scheduling-as-rigor is not.**

A rigor pass may end with a *§N Downstream execution cost* section noting how many days / chapters / docs the ratified action implicates. That section informs sequencing (Phase A3 vs Phase B absorption vs deferral) but does not flip verdicts from §1 executive summary.

**Corollary B — usage frequency alone is not a rigor argument for retention** *(ratified 2026-04-24 by Chris Winn during CSG rigor pass findings review)*

Parallel to Corollary A: just as effort-to-repair cannot argue *against* retirement, raw usage frequency (chapter-ref counts, occurrences across docs) cannot argue *for* retention. High usage proves only that the term has been used — not that it earns its place on rigor grounds.

**What this changes about my reasoning:**

- A term with N chapter refs is not, for that reason alone, Ring-2 or Ring-1-worthy. The rigor verdict must rest on: (a) is it a distinct concept? (b) is it load-bearing for something? (c) does it pass Principle #3 / primitive-distinctness / derivation-from-primitive checks?
- When a retirement verdict is close-call, listing "but there are 66 refs to sweep" is a Principle #1 Corollary A concern (scheduling), not a reason to retain.
- When a retention verdict is made, usage frequency can be NOTED as evidence that the concept is active — but the verdict must cite the rigor-level distinctness/load-bearing claim, not the ref count.

**Why this matters on this project specifically:**

Frameworks that mature tend to prune. High-use terms can accumulate by inertia (author wrote them, found them useful, kept using them) without passing rigor tests for distinctness. CSG's 66 refs + active pedagogical use could have argued for retention on usage grounds; the rigor verdict retired anyway because CSG is a derived scalar from the primitive S. The corollary prevents usage inertia from protecting terms that don't earn their keep rigor-wise.

---

## §2. Operating discipline

### §2.1 When to add a principle

When either party articulates a working rule that should persist across future sessions — not a specific decision about a specific term or framework element, but a *how-we-reason* or *how-we-work* statement. Examples that would qualify:
- "Effort-to-repair is not a rigor argument." (Principle #1 above)
- "When testing options, always explicitly consider option-space breadth before committing to a test." (Articulated earlier 2026-04-24; candidate for Principle #2 — see below.)
- "Rigor-pass output produces provenance records as deliverables." (Articulated in TPS design 2026-04-24; candidate for Principle #3.)

### §2.2 Principle format

Each principle follows the template: ratified-by-whom-and-when · originating-context · scope · principle-statement · what-it-changes · corollaries-and-notes.

### §2.3 Interaction with other docs

- **Open Insights Log** holds open questions. Principles are ratified rules.
- **Rigor passes** reference principles where they constrain reasoning (e.g., "per Principle #1, effort-to-repair is noted in §16 but does not affect §15 verdict").
- **Session handoffs** reference the current principle list when relevant to next-session work.

---

### Principle #2 — Audit the concept, not the exact phrase

**Ratified:** 2026-04-24 by me (self-ratified; candidate for author confirmation)
**Originating context:** while auditing Ring-3 vocabulary-retirement candidates, I used case-sensitive exact-phrase grep patterns (e.g., `\bValue Capture\b`) which returned 0 matches for Value Capture, Cost Bearing, and Asymmetric Regret. A better-methodology re-audit (case-insensitive + concept-level patterns matching proper-noun, compound, phrasal, adjective forms) revealed 16, 46, and 24+ occurrences respectively — flipping the retirement recommendations to *promote*.
**Scope:** every audit that informs a rigor-pass verdict or a Ring-classification decision.

**Principle statement:**

When auditing chapter drafts / case studies / guidance docs for the presence of a concept, search for all forms in which the concept can be expressed — not just the proper-noun or capitalized-phrase form. Concepts appear as:
- Proper-noun forms ("Value Capture")
- Lowercase forms ("value capture")
- Compound / hyphenated forms ("cost-bearing," "value-extraction")
- Phrasal forms ("capturing the value," "bearing the cost")
- Adjectival / derivative forms ("asymmetric regret," "cost-severing mechanism")

**What this changes about my audit methodology:**

- Default to case-insensitive matching (`re.IGNORECASE`) unless there's a specific reason to case-sensitive.
- When auditing a concept, write 2–4 patterns covering the expected surface forms, not one pattern for the proper-noun form.
- When an audit returns 0 results, treat that as a candidate for methodology failure before treating it as a substantive finding.
- When audit results will inform a retirement/demotion recommendation, sanity-check by reading a sample of the candidate-term's chapter prose.

**Why this principle matters on this project specifically:**

The Ring-3 retirement decisions have real consequences — retiring a load-bearing term because the audit missed its occurrences would create chapter-rewrite work that the meta-pass was supposed to prevent. The audit methodology IS part of the rigor.

**Corollary — audit verification:**

When the audit output is decisive for a verdict (not just descriptive), verify by (a) running the audit with alternative patterns, (b) sampling one or two hit files to confirm the pattern catches what it should, and (c) checking a plausible non-hit to confirm the pattern's scope is right.

---

### Principle #3 — Misnaming is a rigor failure

**Ratified:** 2026-04-24 by Chris Winn
**Originating context:** Spatial Cost Severance was labeled as a Cost Severance variant for months. The variant-subtype check (when finally applied) revealed the phenomenon (spatial-distance-dependent costs that vanish when distance collapses) was actually abundance-cost mechanics, not severance. The name *pollutes* the Cost Severance concept's precision every time a reader encounters "Spatial Cost Severance" and tries to map it onto the Cost Severance definition.
**Scope:** every variant-term, subtype-term, or compound-term introduced into the framework vocabulary. Applies retroactively (audit existing vocabulary) and prospectively (verify before introducing new terms).

**Principle statement:**

When a variant-term is introduced for a core concept (e.g., "Spatial X," "Temporal X," "Intergenerational X"), verify that the variant actually describes a genuine subtype of X — *not* a distinct phenomenon being accidentally absorbed into X. A misnamed term is worse than no term, because it pollutes the parent concept's precision every time a reader encounters it.

**What this changes about my reasoning:**

- When proposing or evaluating a variant-term, run the variant-subtype check explicitly: "under the parent concept's definition, is this variant still an instance? Or is it describing a different mechanism?"
- The check: imagine the variant's distinguishing condition (spatial distance, temporal gap, whatever) is removed. Does the variant's phenomenon remain or vanish? If it vanishes because it depended on that condition, confirm the condition produces a *subtype* of the parent concept — not an adjacent-but-distinct mechanism.
- If a variant fails the check, either (a) rename it (the phenomenon is real but not a subtype of the parent), (b) retire it entirely (the phenomenon is already captured elsewhere), or (c) redefine the parent concept to genuinely include the variant (with all the rigor-pass work that implies).
- This principle is stricter than the merger/primitiveness gate (Section L.4 independence gate) — it operates at the *naming* level before the variable-admission level.

**Why this principle matters on this project specifically:**

Cost Severance is the framework's flagship mechanism. Its precision is load-bearing for the success criterion (*"severed cost"* adopted as legal/policy vocabulary). Every misnamed variant dilutes the precision. Spatial Cost Severance and the Temporal-Cost-Severance-renaming question (tested in the 2026-04-24 focused rigor pass) both show the risk: variants can accumulate that weaken the parent concept. Principle #3 is the discipline that prevents this.

**Corollaries:**

- Principle #3 applies to *all* variant-terms, not just Cost-Severance-variants. If a future rigor pass proposes "Spatial Abundance Masking" or "Temporal Gate," the variant-subtype check must run.
- A variant passing Principle #3 does not automatically earn a dedicated named term. Passing only confirms the variant is a genuine subtype; whether it needs a name is a separate vocabulary-footprint question (see meta-pass + Variable-vs-Cost rigor pass + Temporal-Cost-Severance rigor pass for examples of this two-step analysis).

---

### Principle #4 — Retirements preserve their history in-document

> **REFINED 2026-04-30 per Insight #59 — see refinement section below for current discipline.** The original 2026-04-24 ratification body (immediately following) is preserved as historical record per WP#4 itself; the **REFINEMENT 2026-04-30** section partway down this principle supersedes the per-document-type table for current operating discipline. Canonical retirement-archive at `archive/retirements/index.md` carries full retirement traces; this principle's body lays out what summary form is preserved where.

**Ratified:** 2026-04-24 by Chris Winn. Confirmed 2026-04-24 with extension per second directive: *"Additionally include a pointer to the associated document that captures the reason(s) why it's used in the then current document."* Originating articulation: *"When we update/retire words it probably makes sense to update the current documents it's used in, and for all older files maybe simply add a note that the word was retired as of version #.#.# of the document, and perhaps a pointer to the associated document that captures the reason(s) why."*

**Originating context:** as the project retires vocabulary items (FGC, 8 tier labels, Spatial Cost Severance, Abundance Masking, Universality Test, Value Capture pending, Temporal Cost Severance pending, etc.), silently sweeping each retired term out of the documents where it appears creates a readability gain but destroys the audit trail. A future reader encountering a reference to a retired term — or noticing a retired term's absence — has no in-document signal explaining what happened. Making retirement traces visible preserves the reasoning chain.

**Scope:** all framework-vocabulary retirements going forward. Applies retroactively to the retirements already ratified 2026-04-24 (Spatial Cost Severance, FGC, 8 tier labels, etc.) when those retirements propagate into the affected documents during Phase A3 sweep.

**Principle statement (per author clarification 2026-04-24):**

Retirements are handled in two tiers depending on the document's status:

**(Tier 1) Current / active documents** — sweep the retired term out (replace with new term where applicable, or remove where no replacement exists). Bump the document's version to reflect the change. The sweep is the update.

**(Tier 2) Older / historical / archived / versioned-predecessor documents** — **do NOT sweep or rewrite.** Instead add a single *retirement-note header* near the top of the document with three components:
1. Which term(s) were retired.
2. The document version (or framework-state version) at which retirement occurred.
3. A pointer to the rigor pass, Terms Index record, or decision doc that captures the reasoning.

The older document's historical content remains intact. Only the header note is added. Readers encountering the document see the retirement-state up front and can follow the pointer if they want the reasoning. This respects the live-vs-archive policy (point 2 of 2026-04-24 ratified policy: older docs stay intact except for minimal annotation).

**Per-document-type format guidance:**

| Document type | Tier | Retirement treatment |
|---|---|---|
| **Terms Index** (`core/terms/terms_index.md` §4) | Tier 1 | Full RETIRED record with rigor-pass link + full reasoning (this is the authoritative retirement record — template established by Spatial Cost Severance entry 2026-04-24). |
| **Glossary** (currently v2, bumping to v3) | Tier 1 | Sweep retired terms out in v3. The v3 → v2 supersession is the audit trail; v2 is preserved as an older doc. |
| **Active chapter drafts** | Tier 1 | Sweep retired term to replacement where natural; where sweep would distort authorial voice, add footnote. |
| **Active audit docs** (chapter audit v1.0.6, case-study audit v1.0.6) | Tier 1 | Sweep retired terms; bump to v1.0.7 at sweep-time. |
| **Active Technical Appendix** (v0.0.4) | Tier 1 | Sweep retired terms; document gets a "Changes from v0.0.3 → v0.0.4" section (already has this for the dimension renames). |
| **Archived session handoffs** | Tier 2 | Add single retirement-note header: *"Note: this handoff references terms subsequently retired (e.g., 'Spatial Cost Severance'). See `core/terms/terms_index.md` §4 for the retirement record and rigor-pass reasoning."* No sweep. |
| **Archived rigor protocol versions** (`tools/archive/*.md`) | Tier 2 | Single retirement-note header; no sweep. |
| **Archived rigor passes** (e.g., `tools/rigor-passes/*2026-04-22*.md`) | Tier 2 | Single retirement-note header; no sweep. Rigor passes from 2026-04-24 (Path F, tier-reframing, macro-grouping) get the existing `§ Subsequent developments` annotation pattern per prior ratification. |
| **Superseded Technical Appendix versions** (v0.0.3) | Tier 2 | Single retirement-note header pointing to v0.0.4 + Terms Index. |
| **Archived chapter audits / case-study audits** (v1.0.5 etc.) | Tier 2 | Single retirement-note header; no sweep. |
| **PCR v1.1.0** (historical pre-submission review) | Tier 2 | Single retirement-note header; body intact per earlier ratified policy. |

**Extension per author 2026-04-24: active-term traceability.**

The principle covers two symmetric cases:

**(Retirement case) — traceable why a term is GONE** — per the Tier 1 / Tier 2 discipline above.

**(Active-use case) — traceable why a term is THERE** — active documents using current framework vocabulary should include a reasoning-pointer so readers can trace why each term is the one being used. Author direction: *"include a pointer to the associated document that captures the reason(s) why it's used in the then current document."*

**Format for active-use traceability:**

Active documents (chapter drafts, current audits, Technical Appendix, glossary, guidance docs) include a *provenance pointer* — a short header note near the top of the document that points readers to the Terms Index for vocabulary provenance:

> *"Framework vocabulary used in this document: provenance (rigor-pass support, ratification history, definition) tracked in `core/terms/terms_index.md`. See individual entries for reasoning chain."*

This one-line note provides a single entry-point to the full audit trail without requiring per-term inline footnotes (which would clutter prose). The Terms Index records carry the detailed reasoning; the document's header note points to the Index.

**For documents that are PRIMARILY about vocabulary** (Terms Index itself, glossary, rigor passes, provenance records) — no header note needed; they're already the reasoning-chain docs.

**For OLDER / archived documents (Tier 2)** — the retirement-note header already provides a backward-pointer; active-term traceability is preserved implicitly because the older doc's content is intact (readers can follow its references to whatever was current at the time).

**Combined Tier structure:**

| Document state | Active-term pointer | Retirement note |
|---|---|---|
| Current / active | Header-note pointing to Terms Index | Tier-1 sweep at retirement time |
| Older / archived / superseded | N/A (older doc's self-references are preserved) | Tier-2 retirement-note header |
| Vocabulary-authoritative (Terms Index, glossary, rigor passes) | — (is itself the reasoning chain) | Embedded in the authoritative record |

**What this changes about my execution:**

- When a retirement is ratified, downstream sweep-plus-note work runs in two modes: Tier-1 (update/sweep) + Tier-2 (header-note-only). Both land in Phase A3.
- Active docs get version-bumped with each retirement batch.
- Archived/older docs get a header note once per retirement batch (not per term; one consolidated note listing all terms retired in that batch).
- **Current documents gain a provenance-pointer header** (one-line Terms Index pointer) during Phase A3 sweep. Low-effort addition per doc; enables reader-facing traceability.
- Phase A3 audit sweep scope includes: (i) Tier-1 retirement sweeps, (ii) Tier-2 retirement-note-header additions, (iii) active-use provenance-pointer headers on current docs.

**Why this principle matters on this project specifically:**

Commons Bonds's rigor-pass infrastructure is part of the book's credibility infrastructure. A reviewer encountering a retired term + finding a clean audit trail through retirement notes + Terms Index + rigor passes will trust the framework more than one encountering silent sweeps. The audit trail IS the credibility.

**Corollary:**

Retirements during today's session (2026-04-24) that have Terms Index records but haven't yet propagated into their affected documents (Spatial Cost Severance; when Value Capture retirement ratifies; etc.) will need Phase A3 sweep to apply this principle. The Terms Index record exists; the in-document retirement notes don't yet. Phase A3 adds them.

---

**REFINEMENT 2026-04-30 per Insight #59 — Tiered retirement-trace policy + retirement-archive index:**

The original 2026-04-24 discipline (sweep current docs; header-note older docs; full retirement record in Terms Index) was correct for the rapid-development phase. As the framework matured into the publisher-prep phase (2026-04-29 onward), the discipline's costs began to outweigh benefits in some places — specifically, terms_index approaching v1.0.0 with substantial retirement-trace metadata; navigability declining; Phase 3 + Phase 4 rebuilds inheriting noise; pre-publication external review friction.

Per `tools/rigor-passes/commons_bonds_rigor_pass_2026-04-30_working_principle_4_refinement_v1.0.0.md` (RATIFIED 2026-04-30 by Chris Winn): refine the discipline to a **tiered retirement-trace policy + dedicated retirement-archive index** (Options B + C combined per rigor pass §4-§5).

**Refined per-document-type policy:**

| Document type | Retirement-trace policy (refined) |
|---|---|
| **Open insights** (insights with OPEN status) | Full traces (active discipline; status quo) |
| **Pending rigor passes** ([PROPOSED] status) | Full traces (active audit trails; status quo) |
| **Ratified rigor passes** (frozen by date in filename) | Full traces preserved as historical record (status quo; canonical decision-record) |
| **Working principles** | Light traces in body; cross-reference retirement archive index |
| **Vocabulary strategy v1.0.1** | Light traces in §6 + §7 + §13; cross-reference retirement archive index |
| **terms_index v1.0.0+** | **Summary-level traces** (1-line "renamed YYYY-MM-DD per Insight #N; full trace at archive/retirements/index.md"); full traces moved to retirement archive index |
| **Publisher-facing artifacts** (chapter drafts; glossary; Tech Appendix) | NO traces (status quo per WP#8) |
| **Tier 2 archived/superseded files** | Header-note only (status quo) |

**New canonical retirement-archive index:** `archive/retirements/index.md` — single canonical index for all retirement events across the project. Other scaffolding documents reference this index rather than carrying full retirement traces inline. Each entry links to the canonical rigor pass that ratified the retirement; that rigor pass remains the source-of-truth for the full audit trail.

**What the refinement preserves:**

- **Provenance** — preserved via retirement archive index + ratified rigor passes (canonical decision-record).
- **Reversibility** — preserved (rigor passes that ratified retirements remain canonical; revisits cite the rigor pass).
- **M12 attribution-honesty** — preserved (academic lineage stays in rigor passes + vocabulary strategy).
- **Routine 1 + 2 sentinel** — preserved (still catches retired-vocabulary regression; remediation hints reference archive).
- **Working Principle #8** publisher-facing scrub — unchanged; complementary.

**What the refinement changes:**

- terms_index v1.0.0+ reads as current-state document, not retirement-trace catalog.
- Working principles + vocabulary strategy less cluttered with retirement annotations.
- Single canonical retirement-archive (instead of distributed retirement traces).
- Phase 3 Tech Appendix v2.0.0 + Phase 4 Glossary v4 rebuilds derive from cleaner sources.
- Pre-publication external reviewer sees current state cleanly; full audit trail accessible via archive.

**Implementation pending:**

- terms_index v1.0.0 version bump applies summary-level retirement traces (full traces moved to archive/retirements/index.md).
- Working principles body cleanup (this principle's table above) — done in this commit.
- Vocabulary strategy v1.0.1 §6 + §7 + §13 retirement-trace cleanup — queued (could absorb into Insight #37 scaffolding-vs-publisher-facing separation pass).
- Phase 3 Tech Appendix v2.0.0 rebuild derives from cleaner terms_index.
- Phase 4 Glossary v4 rebuild derives from cleaner terms_index.

**Cross-references:**

- `archive/retirements/index.md` — new canonical retirement-archive index; populated 2026-04-30 with 16 vocabulary retirements + 2 methodology retirements + 3 file/artifact retirements.
- `tools/rigor-passes/commons_bonds_rigor_pass_2026-04-30_working_principle_4_refinement_v1.0.0.md` — full audit trail for this refinement.
- Insight #59 (closed-ratified 2026-04-30) — open_insights record.

---

### Principle #5 — Context-flipping rules earn named-rule status

**Ratified:** 2026-04-24 by Chris Winn
**Originating context:** Asymmetric Regret Principle (ARP) rigor pass 2026-04-24, subsequently renamed to **Asymmetric Regret Rule (ARR)** per ARP rename rigor pass commit `b8b62e3` ratified 2026-04-24 (final ratification after same-day flip from preliminary Reversibility Default ratification — M6 academic-rigor question surfaced post-preliminary-ratification; ARR has regret-theory direct lineage in the name without Tech-Appendix-footnote dependency). Ch 7 GuidanceDoc shows the rule directing *extract-aggressively* on Comet flyby (access window closes permanently → extraction is the reversible choice) AND *preserve* on Europa (incommensurable biosphere externality → preservation is the reversible choice). Same rule, opposite operational verdicts. Precautionary Principle can't do this — it's unidirectional. The bidirectional flip was decisive for the rule's Ring-2 promotion.
**Scope:** every rigor pass evaluating a decision-rule / heuristic / principle candidate for named-term status.

**Principle statement:**

When a candidate decision rule produces opposite operational verdicts under different contexts (extract-here vs preserve-there) while remaining the *same underlying rule*, that bidirectional flip is a positive test for named-rule status. Describing such a rule in generic prose ("sometimes do X, sometimes do Y") loses the unifying principle that generates the flip. Naming the rule makes the unification visible.

Conversely, unidirectional rules (rules that always point in the same operational direction) are less name-earning — they can be stated as prose imperatives without losing structure.

**What this changes about my reasoning:**

- When a rigor pass evaluates a decision-rule candidate (e.g., "should we name this reasoning pattern?"), I check: does the rule's operational output flip by context while the rule itself stays constant? If YES → strong name-earning signal. If NO → weaker; test parsimony + other load-bearing criteria harder.
- When testing Principle #3 (misnaming) against a decision rule, I ask separately: is this rule bidirectional? A bidirectional rule survives Principle #3 misnaming tests that a unidirectional rule might fail, because the bidirectional structure IS the distinguishing feature.
- When presenting rigor-pass findings, bidirectional-flip rules get explicit context-comparison tables (e.g., "Comet flyby → extract; Europa → preserve") to show the unification visible.

**Why this principle matters on this project specifically:**

The framework has multiple decision rules in its vocabulary (ARP; Four Gates admit-or-reject; Abundance Inversion's pass-or-fail). Not all are bidirectional. ARP is (flips based on which action is reversible). Four Gates aren't in the same sense (they either admit or reject a cost; they don't flip). AIT isn't (it confirms or denies scarcity-grounding). ARP's bidirectionality is what earns named-rule Ring-2 status where other decision rules may not.

**Corollary — the diagnostic question:**

For any candidate decision rule, ask: *"under different contexts, does this rule direct OPPOSITE actions while remaining the same rule?"* If yes, the rule earns named-rule status (subject to other rigor tests). If no, the rule may still earn a name via other criteria but doesn't earn it via bidirectionality.

**Examples in the framework:**
- **Asymmetric Regret Rule (ARR)** (formerly Asymmetric Regret Principle; renamed 2026-04-24 — last-word "Principle" → "Rule" to downgrade overclaim) — bidirectional (flips on which action is reversible). PASSES.
- **Precautionary Principle** (established literature) — unidirectional (always toward prevention). Framework doesn't name it; cites it.
- **Abundance Inversion Test** (AIT) — not a direction-rule; a test. N/A.
- **Option-Preservation** (candidate framing for ARP rename) — bidirectional (preserve optionality either by acting or by not acting). PASSES; candidate rename for ARP captures the same bidirectional structure.

---

### Principle #6 — Intellectual-honesty (prior-art) audit is part of rigor

**Ratified:** 2026-04-24 by Chris Winn
**Originating context:** Framework-wide literature audit 2026-04-24 (Open Insight #10). Chris raised concern that some framework terms may collide with or unknowingly appropriate established economics / political-economy terminology: *"I honestly thought you said you pulled that from existing literature. Could you do a search to confirm if you/we came up with that term? Additionally for all terms to the same search. I really don't want to claim anyone else's work as my own."* Audit revealed:
- Mazzucato 2018 as prior published usage of "value extraction" (Chris independently rediscovered).
- HR/accounting "severance costs" as semantic collision with "Cost Severance" (Ring-1 flagship).
- Reclamation-bond / financial-assurance literature as prior art for Accountability Bond.
Chris directive: *"Please capture the intellectual-honesty check as one of the tests to run in the full test suite."* Formalized as rigor protocol Module M12 (v2.3.0) and this working principle.
**Scope:** every term, concept, decision rule, and named mathematical primitive introduced into the framework's vocabulary. Applies both prospectively (before term ratification) and retrospectively (for terms introduced before this principle existed).

**Principle statement:**

Intellectual honesty about prior art is part of rigor. Every framework term must pass a literature audit that classifies its relationship to prior published work — (a) original coinage, (b) independent rediscovery of established terminology, (c) lexical collision with a different established concept, (d) adoption of an established term, or (e) adjacent to established terminology. The classification determines the required action: cite + extension-positioning for independent rediscovery; disambiguation or rename for lexical collision; citation-only for adoption; due-diligence footnote for adjacent; no action for original coinage.

Usage-inertia protection is NOT a defense against an M12 finding: a framework term that has 100 chapter refs but is revealed to be independent rediscovery of Mazzucato-style established terminology does NOT get to dodge the citation requirement by claiming "too expensive to change" (Principle #1) or "too widely used to alter" (Principle #1 Corollary B). The citation requirement is a rigor-level obligation.

**What this changes about my reasoning:**

- When proposing, evaluating, or ratifying any framework term, I run M12 (literature audit) before the ratification decision.
- For terms already ratified before this principle existed, I run retrospective M12 audits during Phase A3 or on explicit author request.
- When a rigor pass recommends or ratifies a term, the pass's verdict includes an M12 finding as part of the rigor basis.
- When I draft citation / positioning / disambiguation language, I default to explicit and visible (main-text Ch 1 positioning) rather than buried (Tech Appendix footnote only) for load-bearing terms.
- When M12 finds a lexical-collision of High severity (target audience for the framework overlaps heavily with audience for the established different-concept term), I flag as a dedicated-rigor-pass requirement rather than a single-footnote fix.

**Why this principle matters on this project specifically:**

Commons Bonds's adoption-durability bet rests on framework vocabulary traveling into policy / legal / academic discourse. If a reader in those audiences encounters a framework term and their first reflex is "wait — that's Mazzucato's term, is this author appropriating it?" or "wait — 'cost severance' in accounting means something else, is this author being sloppy?" — the framework loses the credibility its adoption-durability depends on. Intellectual-honesty audit is what prevents this. Additionally, Chris's commitment to not claim others' work as his own is a load-bearing authorial value that the framework's infrastructure must support.

**Corollaries:**

- **Corollary A — Citation beats rename for independent rediscovery.** When the framework and an established term describe the same concept arrived at independently, the stronger move is usually to cite + position-as-extension rather than rename. Rename signals the framework couldn't stand next to its intellectual ancestors; citation signals it can. (Rename remains appropriate for High-severity lexical collisions where the term means a DIFFERENT concept in established use.)

- **Corollary B — "Original coinage" requires evidence, not claim.** A term cannot be called "original coinage" without an M12 audit that specifically checked for prior published usage. Prior-to-M12 terms that were called "original coinage" (including Value Extraction, labeled as such in earlier Terms Index records before the 2026-04-24 audit) require retrospective audits and may need their claim revised to "independent rediscovery."

- **Corollary C — Retrospective M12 updates add value, not obligation.** When M12 finds prior art for an already-ratified term, the finding ADDS provenance information; it does NOT usually flip the rigor verdict. The Value Extraction 2026-04-24 audit is the template — Mazzucato finding → citation requirement → positioning statement → bibliography update, but Option A (Ring 1) verdict unchanged.

- **Corollary D — M12 action ladder (ratified 2026-04-24 via Cost Severance collision pass).** When M12 finds prior art requiring action, the following 7-level ladder governs the response — lighter at top, heavier at bottom:

  1. **Tech Appendix footnote** (for low-severity or due-diligence-only findings)
  2. **Glossary entry citation** (prior art noted in term's formal definition)
  3. **Ch 1 prose citation** (load-bearing positioning in main text at first use)
  4. **Terms Index extension-positioning statement** (formal framework-relation statement)
  5. **Rhetorical bridge in load-bearing main text** (for High-severity lexical collisions where the collision can be converted into a teaching on-ramp; ratified via Cost Severance collision pass 2026-04-24; see that pass §5 for canonical bridge structure)
  6. **Dedicated rigor pass** (for close calls between cite-and-extend vs. rename)
  7. **Rename** (when lexical-collision severity is High and no bridge / disambiguation reaches the target audience's first-encounter reflex)

  Level 5 (rhetorical bridge) is the highest-integrity move for High-severity collisions where bridge framing is authorially tractable — it honors the prior meaning AND extends it, recruiting the reader's existing schema as on-ramp rather than fighting it. Level 7 (rename) is reserved for cases where bridge framing fails.

---

### Principle #7 — Pre-publication-state discipline

Articulated and ratified 2026-04-26 by Chris Winn, after a methodology critique on the Gate-2-rename rigor pass surfaced that external-reception modules (M6 prior-art audit; M11 critic-pressure; M12 collision check) had been implicitly given weight on retired placeholder terms that no external reader has ever encountered or will encounter.

**Statement:** External-reception modules (M6 prior-art audit; M11 critic-pressure; M12 collision check) apply at full weight only to **candidate-publication terms** — the vocabulary the framework will ship with in published outputs (book; essays; papers). **Placeholder terms used and retired during pre-publication drafting carry zero external-reception weight**; rigor on their retirement is internal-coherence-only. Internal-doc-update cost (sweeping references; updating glossary entries; refreshing chapter prose) is real and material, but per Working Principle #1 it is **not a rigor argument** — it is downstream scheduling.

**Operational consequences:**

1. **Rigor on candidate-publication terms operates at full M6/M11/M12 depth.** A naming choice that will appear in the published book or essay must be tested against established academic priors, future critic reception, and prior-art collision because future readers will encounter it.

2. **Rigor on retired-term retirement is lightweight.** A rigor pass on retiring a placeholder that's never been published doesn't need M6/M11/M12 at full depth. It needs internal-coherence checks (does the framework still cohere after the retirement?) + Tier-1-update-header documentation (per Principle #4) so internal provenance preserves the lineage.

3. **The pre-publication state is a window of cheap correction.** Until publication, rename / retire / restructure costs are purely internal — measured in commit-time and doc-update-time, not in published-reader-migration-time. The framework can self-correct freely. Working Principle #1 (effort-to-repair-not-a-rigor-argument) reinforces this: internal repair effort is real but doesn't count as rigor input.

4. **For terms that have been published and are later retired (post-publication retirement),** the discipline shifts: external-reception modules apply because the retired term has reached external readers. This is a different regime than pre-publication retirement. The framework is currently entirely in the pre-publication regime.

**Why this matters for the framework's adoption-durability bet:** the framework's success criterion (vocabulary that travels — the labor lawyer in 2039 citing "severed cost" in a brief) is about *future* reception of the *published* vocabulary. Forward-simulation of that reception is what M6/M11/M12 are for. Wasting forward-simulation effort on retired terms that will never reach future readers is a methodology error that obscures what the rigor work is actually accomplishing.

**Concrete example (from the supplemental Gate-2-rename pass 2026-04-26):** the prior pass mentioned "Dimensional Consistency" (T2-retired predecessor of "Units Consistency") in its alignment table at full per-test weight. The supplemental pass applied Principle #7 and treated the retired term as zero-weight — appears only for provenance, not for current rigor evaluation. The analysis is therefore lighter on retired-predecessor mentions and heavier on candidate-publication-term comparisons (Units Consistency vs Consistency vs Commensurability vs Commensurate vs Comparability vs Homogeneity — all six being candidate-publication terms get full M6/M11/M12 weight).

**Interaction with other principles:**
- **Principle #1** (effort-to-repair-not-a-rigor-argument) — Principle #7 reinforces this: internal repair effort doesn't count as rigor input regardless of how the term changes.
- **Principle #4** (retirements-preserve-history) — Principle #7 specifies that retirement provenance is documented per #4's Tier-1 header pattern; the *content* of retirement-pass rigor focuses on internal-coherence rather than on the external-reception modules.
- **Principle #6** (M12 intellectual honesty) — Principle #7 specifies that the M12 Corollary D 7-level action ladder (original-coinage / independent-rediscovery / lexical-collision-disambiguated / collision-rename-required / rhetorical-bridge / extension-positioning / borrowed-term-acknowledged) applies to candidate-publication terms; retired terms don't need M12 ladder evaluation at full weight.

**Triggering rigor-protocol update:** the rigor protocol (`tools/commons_bonds_rigor_protocol_v2.4.0.md`) should reference Principle #7 in its description of M6/M11/M12 modules so future rigor passes apply the discipline by default. Effort: small protocol update (separate commit).

**Triggering retroactive scan recommended:** past rigor passes may contain places where retired-term external-reception worries were inappropriately weighted. A retroactive scan would identify and revise. Effort: ~1 audit commit. Likely produces a small set of revisions (the principle has been implicitly held in many places; explicit violations are likely few).

**Provenance:** articulated by Claude after author flagged retired-vocabulary worry in supplemental Gate-2 rigor pass 2026-04-26; ratified 2026-04-26 by Chris Winn ("My recommendation: All three, because they reinforce each other"). Implemented by adding to working principles doc + updating rigor protocol + executing retroactive scan.

---

### Principle #8 — Publisher-facing artifacts are scrubbed of scaffolding/audit-trail content

**Ratified:** 2026-04-28 by Chris Winn. Originating articulation: *"regarding the Tier 3 / scaffolding-vs-publisher-facing principle in the still-PROPOSED retirement-traces rigor pass — scaffolding is internal; reasoning chains preserved in the rigor passes themselves; don't over-engineer for external readability. Let's expand that to every external facing document. So all chapter drafts, glossary items, and technical appendix."*

**Originating context:** the retirement-traces rigor pass `tools/rigor-passes/commons_bonds_rigor_pass_2026-04-28_retirement_traces_scaffolding_vs_publisher_facing_v1.0.0.md` (RATIFIED 2026-04-28; Insight #28) established the Tier 1 / Tier 2 / Tier 3 trichotomy for retirement-trace handling specifically. Tier 1 (publisher-facing live documents) gets retired terms swept; Tier 3 (scaffolding/decision-record) preserves traces. Author surfaced 2026-04-28 that the principle generalizes beyond retirement-traces: ALL scaffolding/audit-trail content should be scrubbed from publisher-facing artifacts (chapter drafts, glossary, Tech Appendix), with reasoning chains preserved exclusively in scaffolding documents (terms_index, rigor passes, working principles, vocabulary strategy, sessions, open insights, alignment patches).

**Scope:**

*Tier 1 publisher-facing artifacts subject to scrub:*
- Chapter drafts (`manuscript/chapters/Chapter_*Draft.{md,html}`) at submission-readiness state
- Current + future glossary (`core/glossary/commons_bonds_updated_glossary_v3.html` + future v4 derived from terms_index)
- Current + future Tech Appendix (`core/technical-appendix/TechnicalAppendix_v1.0.0.html` + future v2.0.0 derived from terms_index)
- Research case-study writeups (`research/case-studies/*.md`) where they feed chapter prose

*Tier 3 scaffolding documents preserving all traces:*
- `core/terms/terms_index.md` (source-of-truth)
- `tools/rigor-passes/*.md` (decision history)
- `alignment/commons_bonds_working_principles_v*.md` + `commons_bonds_vocabulary_strategy_v*.md` + `commons_bonds_open_insights_v*.md` (standing disciplines)
- `alignment/sessions/*.md` + `alignment/patches/*.md` (project state)

**Principle statement:**

Publisher-facing artifacts (Tier 1) carry only content directly serving the reader — prose, equations, lineage citations, examples, footnotes that aid reader comprehension. They DO NOT carry scaffolding/audit-trail content:

- "Backed by rigor pass X (commit Y)" annotations
- M11 critic-survival probes inline
- "Per Insight #N" / "Per Working Principle #M" cross-references
- Decision-record narratives ("the verdict here was X because Y...")
- Status indicators (CURRENT / RETIRED / SUPERSEDED markers in inline prose)
- Version-progression archaeology
- Author-meta-notes ("Flag this when you get to the glossary pass…")
- Rigor-pass commit references

Reasoning chains for ALL framework decisions (vocabulary, methodology, structural) are preserved exclusively in scaffolding documents.

**Explicitly OUT of scope for scrub** (these stay in publisher-facing artifacts because they serve the reader, not the audit trail):

- Lineage citations on first-use (e.g., Brown Weiss 1989 for intergenerational equity; Pigou 1920 for externality lineage)
- Tier B framework-specialization footnotes (e.g., Externality Tail's "Pigou + 4-axis specialization" footnote)
- Tech Appendix §L methodological footnotes that situate the framework in established traditions
- Reader-facing cross-references between chapters that aid navigation
- Case-study sources / data citations

**What this changes about my execution:**

- **During chapter drafting:** sweep author-meta-notes, status indicators, rigor-pass commit references before submitting to publisher. Pre-submission readiness audit (routine 2) catches these patterns.
- **During Tech Appendix v2.0.0 rebuild:** explicitly scrub all scaffolding content — "Backed by rigor pass X (commit Y)" patterns, M11 probes, version archaeology, status-indicator definitions, pre-v1.0.0 version-progression sections.
- **During Glossary v4 rebuild:** derive entries from terms_index rendering fields (per S1 schema); no rigor-pass references in glossary entries; no Insight / Working-Principle cross-references in entries.
- **Pre-submission readiness audit (routine 2):** expand pattern checks to include scaffolding-content patterns.

**Why this principle matters on this project specifically:** the book's credibility infrastructure includes both academic-trade-hybrid-publisher reach (Princeton/Yale/Harvard/MIT/U-Chicago) and legal/policy-adoption-travel reach (regulatory text + policy briefs). Both audiences expect publisher-facing artifacts to be clean of internal-process content. Audit trail in scaffolding documents is exactly where reviewers, future-author, future-collaborator look for reasoning; it should NOT appear in the published book itself. Mixing tiers undermines reader experience + signals process-rather-than-content focus.

**Application discipline:**

- **Prospective application** (default per author 2026-04-28): going forward, no new scaffolding content lands in Tier 1 artifacts. Pre-submission readiness audit catches violations naturally.
- **Retroactive sweep is NOT triggered automatically:** current chapter drafts may contain residual author-meta-notes etc. that get cleaned during normal pre-submission readiness audit (routine 2), not via dedicated retroactive sweep. Reason: retroactive sweep risks losing author intent (some "meta-notes" might be legitimate footnote-content in disguise).

**Corollaries:**

- **Tier 3 scaffolding documents preserve all traces, decisions, rigor-pass references, and reasoning chains** — generalizes the corollary from the retirement-traces rigor pass.
- **Tier 2 archived versions get header-note-only annotations** for retirements (per Principle #4).
- **Tier 1 publisher-facing artifacts contain only content serving the reader** — Principle #8's distinctive contribution.

**Interaction with other principles:**

- **Principle #4 (retirements preserve their history in-document)** — Principle #8 generalizes: it's not just retirement-traces that go to Tier 3; ALL audit-trail content does. Principle #4 covers the special case of retired-term traces; Principle #8 covers the broader category.
- **Principle #7 (pre-publication-state discipline)** — Principle #8 reinforces: pre-publication artifacts that get scrubbed before publication don't carry the audit trail forward into publication.

**Cross-references:**

- Retirement-traces rigor pass `tools/rigor-passes/commons_bonds_rigor_pass_2026-04-28_retirement_traces_scaffolding_vs_publisher_facing_v1.0.0.md` (Insight #28 closed-ratified 2026-04-28)
- Vocabulary strategy scaffolding doc `alignment/commons_bonds_vocabulary_strategy_v1.0.1.md` §9 (decision-record format references this principle)
- Architecture rigor pass `tools/rigor-passes/commons_bonds_rigor_pass_2026-04-27_publication_architecture_terms_index_glossary_tech_appendix_v1.0.0.md` (Phase 3 Tech Appendix v2.0.0 + Phase 4 Glossary v4 rebuilds inherit Principle #8 as standing input)
- Routine 2 (pre-submission readiness audit) — pattern checks extended to include scaffolding-content patterns

---

### Principle #9 — Worktree isolation with session-end fast-forward to main

**Ratified:** 2026-04-29 by Chris Winn. Originating articulation: *"Hmm, is there a better workflow for us to use? Like should we create .claude & .chriswinn directories in the git folder and checkout the project to those and push to the main branch from those folders instead of working on the main branch?"* followed by *"Let's go ahead and implement your suggested working process and document it as our standard workflow going forward."*

**Originating context:** the iCloud incident 2026-04-29 (project relocated from `~/Documents/___WorkingOn/commons-bonds` to `~/commons-bonds` after iCloud sync corruption deleted ~70 working-tree files mid-session) plus the harness-managed worktree pattern (Claude's session worktrees auto-created at `.claude/worktrees/<branch-name>/` on a separate branch) made evident that single-checkout direct-to-main is fragile when author and Claude operate concurrently. The earlier project rule "Direct-to-main git workflow; push each commit as it lands" is supplemented — direct-to-main is preserved at the ratified-chunk level, but with worktree isolation during the session itself.

**Principle statement:**

The project operates two concurrent working trees from a single `.git` directory:

| Working tree | Branch | Operator | Purpose |
|---|---|---|---|
| `/Users/c17n/commons-bonds` | `main` | Chris Winn | Author checkout; reading state; manual edits |
| `/Users/c17n/commons-bonds/.claude/worktrees/<session-name>` | `claude/<session-name>` | Claude (harness-issued) | Claude's session work |

**During-session discipline:**

- Claude commits to the harness-issued branch within its worktree.
- Chris's primary checkout is never touched by Claude.
- Object database is shared (single `.git`); refs are tracked per worktree.

**Session-end ritual** (executed when a chunk of Claude's work is ratified by Chris):

1. Claude pushes the feature branch to origin: `git push -u origin claude/<session-name>` (preserves session as a remote record).
2. Claude fast-forwards `origin/main` to the branch HEAD: `git push origin HEAD:main`. Fast-forward only — direct-to-main linear history is preserved (no merge commits).
3. Chris runs `git pull` in the primary checkout to absorb changes locally.
4. The feature branch may be deleted post-merge or kept indefinitely as a session-record.

**Cadence:** the merge happens per ratified chunk, not per commit. A chunk may be one commit (e.g., the v1.0.1 cleanup) or many (a multi-commit rigor pass). Ratification by Chris is the gate.

**What this changes about Claude's execution:**

- Claude no longer pushes directly to `main` on each commit. Claude pushes to the harness-issued branch, then surfaces a "ready to merge?" signal when a chunk is ratified.
- After Chris ratifies, Claude executes the merge ritual (steps 1–3 above) and confirms `origin/main` is at the new HEAD.
- `git fetch origin main:main` from Claude's worktree fails by design (git refuses to fetch into a branch checked out in another worktree). Claude treats `origin/main` as the source of truth and trusts Chris's primary checkout will pull when convenient.
- If the harness places Claude on a session branch but no commits land that session, the branch can be discarded without ritual — nothing to merge.

**Why this principle matters on this project specifically:** the iCloud incident demonstrated that single-checkout discipline is fragile. Worktree isolation prevents author-Claude collisions during long sessions (the iCloud-deleted-while-editing scenario could not occur because Chris's working tree is independent of Claude's). Direct-to-main linear history (no merge commits, no PR ceremony) is preserved at the ratified-chunk level. The trade-off is one merge-step per ratified chunk, which surfaces a natural "is this ready?" gate that the previous push-each-commit-immediately pattern lacked.

**Interaction with other principles:**

- This supersedes the project rule "Direct-to-main git workflow; push each commit as it lands" as articulated in earlier session handoffs. Direct-to-main is preserved at the ratified-chunk level (via fast-forward push), not at the commit level.
- **Principle #7 (pre-publication-state discipline)** — orthogonal; pre-publication discipline operates on content, this principle operates on git workflow.

**Cross-references:**

- Session handoff `alignment/sessions/commons-bonds-session-handoff-2026-04-29_v1.47.0.md` §2.5 — iCloud incident motivating context
- First execution: commit `b8db72d` (Vocabulary strategy v1.0.1 file rename + version-marker sweep) merged via this ritual on 2026-04-29

---

### Principle #10 — Two-layer content origination discipline (internal scaffolding vs external publisher-facing)

**Ratified:** 2026-04-30 by Chris Winn during Insight #9 Thread δ surfacing. Originating reframe: *"hmm, I think perhaps I should have asked the question differently as what we are archiving isn't necessarily going to end up as end reader, publisher, literary agent facing. So I guess a better question is what should be internal vs external, then apply the earlier question to the external facing material."*

**Originating context:** Insight #9 (Framework as decision-time severance-detection tool) initially framed as a single-layer book-scope question (a/b/c/d options for the publisher-facing book). The reframe surfaced that the question is actually two-layer: (Step 1) what lives in internal scaffolding vs external publisher-facing artifacts; (Step 2) for whatever lands external, apply book-scope / literature-pattern reasoning. The reframe is general — it applies to *any* framework decision where rich research / methodology / worked examples / literature audits exist alongside a publisher-facing chapter / glossary / Tech Appendix decision.

**Principle statement:**

All new framework content is classified at origination as **internal-scaffolding** or **external-publisher-facing**. The two layers operate under different disciplines:

| Layer | What lives here | Discipline |
|---|---|---|
| **Internal scaffolding** | `.claude/` · `tools/` · `core/methodology/` · `alignment/` · `research/` · `archive/` | Rich; preserves methodology notes, worked examples, research-grade depth, literature audits, audit trail, decision-time-application drafts, Book 2 / Book 3 seed material, framework-supporting material that doesn't need publisher-facing exposure |
| **External publisher-facing** | `manuscript/chapters/*` · `core/glossary/*` · `core/technical-appendix/*` · `manuscript/essay/*` | Disciplined per WP#8 (scrubbed of audit-trail content) + Pattern 2 demonstration (threaded through cases rather than codified in dedicated how-to / methodology sections — the *Doughnut Economics* / *Mission Economy* / *Mine!* model) |

**Cross-layer flow:**

- **Internal can FEED external** — worked examples can become chapter prose; literature audits can inform chapter framing; methodology drafts can demonstrate as case treatment.
- **External must NOT carry internal contamination** — no scaffolding bleed into publisher-facing artifacts. WP#8 enforces this directly.
- **Internal serves as bridge to Book 2 / Book 3** — research that doesn't land in Book 1 publisher-facing accumulates in internal scaffolding, where it becomes seed material for future books per Insight #13 book-scope-creep discipline.

**Application discipline at content origination:**

Before creating new content, classify it:

1. *Is this directly supporting the reader-facing argument in a way that earns its publisher-facing slot?* → External.
2. *Is this methodology / research / worked example / audit material that supports framework decisions but doesn't need to land in chapters / glossary / Tech Appendix?* → Internal.
3. *Is this material that future books (Book 2 / Book 3) might absorb?* → Internal (as seed).
4. *Is this audit trail / decision record / rigor-pass content?* → Internal (per WP#4 + WP#8).

When in doubt, default to internal — it's easier to promote internal material to external (when it earns the slot) than to scrub publisher-facing artifacts of accumulated scaffolding.

**Pattern 2 demonstration discipline (for external layer):**

External-facing material that touches applied / decision-time / how-to registers should follow the **Pattern 2 / threaded** model documented in [`core/methodology/decision_time_application_internal_v1.0.0.md`](../core/methodology/decision_time_application_internal_v1.0.0.md):

- Demonstrate the framework's affordance through case treatment (chapters; personal stories; cross-references)
- Do NOT codify a methodology in publisher-facing prose (no "How to Apply" chapters; no prescribed two-step procedures)
- Trust the reader to extract the methodology by observing the framework get used
- Mirror the Insight #14 epistemic-humility discipline: "demonstrate the affordance; don't codify it"

**Why this principle matters:**

1. **Preserves all research without scope-creep cost.** Rich internal scaffolding doesn't bleed into publisher-facing register. Insight #13 (book-scope creep monitoring) is reinforced.
2. **Names where new content originates.** WP#4 (refined retirement-trace policy) tells us where retirement traces go. WP#8 tells us what's scrubbed from publisher-facing. Insight #28 classifies retirement tiers. Insight #37 is the after-the-fact separation operation. WP#10 fills the gap: it tells us where new content *originates* and the discipline that follows from that classification.
3. **Creates a clean handoff to Book 2 / Book 3.** Material that exceeds Book 1 publisher-facing scope accumulates in internal scaffolding as seed for future books — rather than being lost or forced into Book 1 inappropriately.
4. **Coordinates parallel threads.** Threads α (architecture), β (drafting), γ (hygiene), δ (discussion) per session handoff v1.49.0 each operate across both layers; explicit two-layer discipline keeps thread outputs disciplined regardless of which thread lands them.

**Interaction with other principles:**

- **WP#4 (refined retirement-trace policy)** — operates on the same internal/external axis; WP#10 generalizes the discipline to all content origination, not just retirement traces.
- **WP#8 (publisher-facing scrubbed of scaffolding)** — WP#10 is the origination-time companion to WP#8's scrubbing-time discipline.
- **Insight #13 (book-scope creep monitoring)** — WP#10 provides the structural answer to scope-creep pressure: rich material lives internal; external stays disciplined.
- **Insight #14 (Norway treatment + epistemic-humility discipline)** — WP#10 generalizes the "demonstrate the affordance; don't codify it" register from Norway/Accountability Bond specifically to all framework affordances at the publisher-facing layer.
- **Insight #28 (three-tier retirement-trace classification)** — WP#10 operates at content-origination; Insight #28 operates at retirement-time. Compatible; complementary.
- **Insight #37 (scaffolding-vs-publisher-facing separation pass)** — Insight #37 is the after-the-fact separation operation; WP#10 prevents the contamination at origination, reducing #37's scope going forward.

**Cross-references:**

- Insight #9 closed-ratified 2026-04-30 (verdict (b) at external layer + rich-internal-scaffolding discipline) — WP#10 is generalized from this verdict
- [`core/methodology/decision_time_application_internal_v1.0.0.md`](../core/methodology/decision_time_application_internal_v1.0.0.md) — internal scaffolding artifact preserving the literature-pattern analysis (Pattern 1 / 2 / 3) + two-layer framing rationale
- WP#4 (refined per Insight #59); WP#8; Insight #13; Insight #14; Insight #28; Insight #37
- Session handoff v1.49.0 §4 — parallel-thread coordination discipline

---

## §3. Candidate principles (articulated but not yet ratified as such)

### Candidate — Option-space breadth is load-bearing

Articulated 2026-04-24 after Variable-vs-Cost rigor pass incident where I tested only A/B/C despite D and E being real candidates. Pattern: when framing a rigor question, explicitly enumerate candidate options that the initial question didn't raise. I shouldn't assume the initial framing exhausts the option space.

**Why candidate rather than ratified:** this is a recurring behavior pattern I'm working to internalize. May warrant formal ratification as Principle #3 if it proves to benefit from the explicit statement.

### Candidate — Proactive insight capture

Articulated 2026-04-24 per Chris's direction that I should "always feel you have the freedom to think & express [my] ideas so we can work more collaboratively vs. [Chris] asking the right questions." The Open Insights Log implements the capture mechanism. The principle is: don't sit on observations; log them and surface them.

**Why candidate rather than ratified:** already being acted on via the Open Insights Log. Formalizing as a principle here is redundant unless Chris wants it explicit.

---

*End of Working Principles v1.0.0. Established 2026-04-24. Principle #1 ratified; candidates tracked in §3 for potential future ratification.*
