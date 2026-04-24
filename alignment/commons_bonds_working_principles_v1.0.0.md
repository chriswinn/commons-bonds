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

### Principle #5 — Context-flipping rules earn named-rule status

**Ratified:** 2026-04-24 by Chris Winn
**Originating context:** Asymmetric Regret Principle (ARP) rigor pass 2026-04-24. Ch 7 GuidanceDoc shows ARP directing *extract-aggressively* on Comet flyby (access window closes permanently → extraction is the reversible choice) AND *preserve* on Europa (incommensurable biosphere externality → preservation is the reversible choice). Same rule, opposite operational verdicts. Precautionary Principle can't do this — it's unidirectional. The bidirectional flip was decisive for ARP's Ring-2 promotion.
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
- **Asymmetric Regret Principle** (ARP) — bidirectional (flips on which action is reversible). PASSES.
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
