# Commons Bonds — Focused Rigor Pass: Gate 2 rename — "Units Consistency" → "Consistency"

**Version:** 1.0.0
**Date:** 2026-04-26
**Protocol applied:** `tools/commons_bonds_rigor_protocol_v2.4.0.md` — full 12-module suite + §22 Path Comparison Mode + §22.4 usefulness-vs-goals alignment + cluster-coherence sub-test + specificity-preservation sub-test + reader-inference sub-test.
**Scope:** Tests a sub-option not explicitly tested in `four_gates_cluster_v1.0.0.md`: rename **Gate 2 alone** from "Units Consistency" to "Consistency" — leaving CIT + Boundedness + Independence unchanged. Produces a 1-acronym-plus-3-property-nouns cohort pattern that is more uniform than the current 1-acronym-plus-1-compound-noun-plus-2-property-nouns pattern. Author direction 2026-04-26: *"do a full rigor test on the four gates if we were to change just the second gate to 'Consistency'."*
**Status:** rigor pass executed 2026-04-26; pending author ratification.
**Author:** Chris Winn

**Applies Working Principles:**
- **Principle #1** (effort-to-repair not a rigor argument) — sweep cost is downstream scheduling, not verdict input.
- **Principle #2** (audit concept not phrase) + option-space breadth — names variants tested as alternatives.
- **Principle #3** (misnaming is a rigor failure) — checks whether "Consistency" alone names the underlying gate condition correctly.
- **Principle #6** (M12 intellectual honesty) — prior-art collision check.

---

## §1. Executive summary

**RECOMMENDED: Option B — REJECT the proposed rename. Retain "Units Consistency."**

**Three rationales for rejection:**

1. **Specificity loss is load-bearing (M6 + Principle #3 failure).** "Units Consistency" specifies *what kind* of consistency the gate enforces — units (dollar-magnitude × time-magnitude commensurability across all admitted Cᵢ). Dropping "Units" leaves "Consistency" alone, which is structurally ambiguous: consistency of what? Internal-logical-consistency? Cross-temporal consistency? Cross-case consistency? Notational consistency? Each of these is a defensible reading; none is the gate's actual function. "Consistency" alone fails Principle #3 (misnaming-is-rigor-failure) because it does not name the gate's specific operation.

2. **Cohort-uniformity gain is not load-bearing (the structural asymmetry remains).** The original `four_gates_cluster` finding holds: CIT is a methodological **test**; the other three are mathematical **conditions**. Renaming Gate 2 from "Units Consistency" to "Consistency" makes Gates 2/3/4 more parallel as single-word property-nouns, but does NOT eliminate the underlying CIT-vs-others asymmetry. The cohort goes from (acronym + compound-noun + property-noun + property-noun) to (acronym + property-noun + property-noun + property-noun) — mildly more uniform on the property-noun side, but the load-bearing asymmetry (CIT-as-test) is unchanged. The pass's structural-asymmetry argument applies regardless of whether Gate 2 is "Consistency" or "Units Consistency."

3. **M12 prior-art collision risk increases.** "Consistency" alone is a generic mathematical-and-philosophical term used across logic, set theory, ethics, axiomatic systems, and statistical methodology with non-overlapping meanings. As a framework-coined gate name, "Consistency" alone collides with all of these. "Units Consistency" carries enough modifier to disambiguate (the framework's gate is specifically about unit-commensurability, not logical-consistency or distributional-consistency). The prior-art collision profile worsens under the rename.

**Aggregate finding:** the cohort-uniformity gain is small (mildly more parallel reading of Gates 2/3/4 as single words) and the specificity + M12 + Principle #3 losses are substantial. Net: rename loses on every load-bearing axis. Status quo wins.

**The decisive test:** Reader-inference at first encounter. A reader meeting "Consistency" without prior context cannot reliably infer that the framework means *unit-commensurability* (dollars × time across all Cᵢ). A reader meeting "Units Consistency" can. The decisive criterion the original cluster pass used — naming should honor what the gate actually does — favors "Units Consistency."

**Falsifiers checked (§2.4):** None of the falsifiers for "Units Consistency" trip. None of the upside arguments for "Consistency" alone survive scrutiny.

---

## §2. The question under test

### §2.1 The change

| Gate | Current | Proposed | Function |
|---|---|---|---|
| 1 | CIT | CIT | content gate (commons-grounding test) |
| 2 | **Units Consistency** | **Consistency** | mathematical condition (unit-commensurability) |
| 3 | Boundedness | Boundedness | mathematical condition (integral convergence) |
| 4 | Independence | Independence | mathematical condition (no double-counting) |

### §2.2 The cohort comparison

**Current cohort:** CIT (acronym) + Units Consistency (compound noun) + Boundedness (single word) + Independence (single word).
- Naming pattern: 1 acronym + 1 compound noun + 2 single words.

**Proposed cohort:** CIT (acronym) + Consistency (single word) + Boundedness (single word) + Independence (single word).
- Naming pattern: 1 acronym + 3 single words.

**The structural asymmetry preserved in both cohorts:** CIT is a methodological test (action; methodology); the other three are mathematical conditions (property; state). Per `four_gates_cluster_v1.0.0.md` §3, this asymmetry is load-bearing and the rigor pass concluded the asymmetry should be preserved.

### §2.3 Options

- **A — RENAME.** Gate 2 becomes "Consistency." Cohort becomes more uniform (Gates 2/3/4 all single-word property-nouns).
- **B — RETAIN "Units Consistency."** Status quo per `four_gates_cluster_v1.0.0.md` ratification.
- **C — RENAME with a different single-word modifier preservation** (e.g., "Commensurability" — single word that retains the units-meaning). Consider if A is rejected on specificity grounds.
- **D — REVISIT the original four_gates_cluster verdict** in light of this question (e.g., consider whether the cohort should be reorganized differently entirely). Out of scope for this pass; flag if surfaced as needed.

### §2.4 Falsifiers

**Option B (retain) is falsified if:**
- "Consistency" alone is unambiguously interpretable in the framework's context (e.g., if no reader reasonably reads it as anything other than unit-commensurability).
- Cohort-uniformity gain is more load-bearing than specificity loss (e.g., if reader-experience evidence shows uniform property-noun cohort substantially improves comprehension).
- M12 prior-art audit clears "Consistency" alone as framework-term-distinctive.
- "Units Consistency" itself is found to be misnamed (e.g., if the gate actually enforces something broader than units).

**Option A (rename to "Consistency") is falsified if:**
- Specificity loss makes the gate's function unrecoverable from the name alone.
- M12 surfaces unacceptable prior-art collision.
- Principle #3 (misnaming-is-rigor-failure) check fails.
- The structural-asymmetry argument doesn't apply (i.e., if Gate 2 is somehow more like CIT than like Boundedness/Independence, requiring its own naming convention).

---

## §3. M1 — Framework CORE

**Test:** Does the rename affect the framework's mathematical apparatus?

**Finding:** No effect. CIT + Gates 2-4 + RCV integral mathematics are unchanged regardless of what Gate 2 is named. The mathematical condition the gate enforces (∫ Cᵢ dt with units consistent across all admitted Cᵢ) is invariant under renaming.

**Verdict on M1:** INDIFFERENT.

---

## §4. M2 — Case study

**Test:** Does the rename affect case-study application of the gates?

**Finding:** Marginal effect. Case applications (McDowell coal; Norway oil; Deepwater Horizon) walk candidate costs through the gates in sequence. The walkthrough prose currently reads: *"Black lung healthcare costs in dollars × years; passes Units Consistency (commensurable with other Cᵢ); passes Boundedness (finite over the case's century-scale horizon); passes Independence (not double-counted with environmental Cᵢ)."* Under "Consistency," the prose reads: *"...passes Consistency..."* — and the reader has to infer or recall what Consistency means.

The marginal effect is **weakly negative** — case prose is cleaner with the modifier intact because each gate's name reminds the reader what's being checked.

**Verdict on M2:** "Units Consistency" preferred (specificity supports prose readability).

---

## §5. M3 — Book content

**Test:** Does the rename improve or degrade chapter-level prose?

### §5.1 Ch 6 methodology section

Ch 6 introduces the Four Gates apparatus and walks readers through each gate's function. Current candidate prose for first-use of Gate 2 (per Tech Appendix supplement §6.2):

> *"...Units Consistency — claim's units match the underlying commons's units (avoids unit-conflation across heterogeneous commons categories)..."*

Under "Consistency," the prose would read:

> *"...Consistency — claim's units match the underlying commons's units (avoids unit-conflation across heterogeneous commons categories)..."*

The second version requires the reader to read the parenthetical to understand what kind of consistency is meant. Information that was front-loaded by the gate's name is now postponed.

### §5.2 Cross-chapter usage

Across Ch 6 + Tech Appendix + cit_examples + glossary v3, Gate 2 is referenced ~15-20 times. Each reference under "Consistency" requires either (a) prior context establishing the meaning, or (b) inline disambiguation. Under "Units Consistency," neither is needed at each reference.

### §5.3 Berggruen-essay relevance

The essay will likely introduce Four Gates compactly. Compact introduction with "Consistency" requires prose like *"the gates check that the claim is commons-grounded (CIT), unit-consistent, bounded, and independent."* Compact introduction with "Units Consistency" reads: *"the gates check that the claim is commons-grounded (CIT), units-consistent, bounded, and independent."* Marginal difference; both work, but the second carries the modifier without prose cost.

**Verdict on M3:** "Units Consistency" preferred. The modifier earns its place by front-loading information that would otherwise need parenthetical disambiguation at each use.

---

## §6. M4 — Craft

**Test:** Prose economy + register consistency + rhythm.

### §6.1 Prose economy

"Units Consistency" is two words; "Consistency" is one. Single-word naming is more compact. **Mild advantage to A (Consistency).**

### §6.2 Register consistency

The book's register is accounting-bookkeeping (per `four_gates_cluster` §1 finding that "Units" wins T2 over "Dimensional" on register grounds). "Units" is the register-aligned modifier. Dropping it surrenders register-alignment to gain compactness. **Mild disadvantage to A.**

### §6.3 Rhythm in cohort

Reading the cohort aloud:
- Current: *"CIT, Units Consistency, Boundedness, Independence."* — rhythm: **3-syllable acronym + 6-syllable phrase + 3-syllable word + 4-syllable word**. Mixed rhythm.
- Proposed: *"CIT, Consistency, Boundedness, Independence."* — rhythm: **3-syllable acronym + 4-syllable word + 3-syllable word + 4-syllable word**. More uniform rhythm.

**Mild advantage to A on rhythm.**

### §6.4 Aggregate craft verdict

A wins on prose economy (compactness) and rhythm; B wins on register-alignment. Net: roughly even on M4.

**Verdict on M4:** EVEN. Craft considerations alone do not decide.

---

## §7. M5 — Dinner-table

**Test:** Non-expert reader parsing.

### §7.1 First encounter

A reader encountering "Consistency" without prior context must guess what kind of consistency. Possible readings:
- Logical consistency (axiomatic; Gödelian register)
- Statistical consistency (estimator convergence)
- Internal consistency (no contradictions in the claim)
- Cross-time consistency (claim doesn't change across temporal scope)
- Cross-case consistency (same claim form across cases)
- Unit consistency (the actual framework meaning)

Each is a defensible reading. Only one is the framework's actual meaning.

A reader encountering "Units Consistency" has the modifier explicit. The reading is constrained by the modifier; reader correctly infers unit-commensurability.

### §7.2 Subsequent uses after introduction

Once the framework introduces "Consistency" and defines it, subsequent uses do not need re-disambiguation. The first-encounter cost is a one-time cost; subsequent prose carries the meaning.

But the framework's adoption-durability bet (per Goal-1 vocabulary portability) depends on terms that *travel* without their full chapter-introduction context. A labor lawyer in 2039 citing "Consistency" in a brief loses the framework's specific meaning unless the brief carries the disambiguating context. "Units Consistency" travels intact.

**Verdict on M5:** B (Units Consistency) preferred. First-encounter cost + travel-portability both favor specificity.

---

## §8. M6 — Academic rigor

**Test:** Connection to existing discourse + Principle #3 distinctness check + precision.

### §8.1 Established literature

"Units consistency" or "dimensional consistency" is established mathematical-and-engineering vocabulary for the requirement that quantities being added or compared must have commensurable units (the *units-must-match* discipline foundational to dimensional analysis since the 19th century — Buckingham π theorem; Bridgman 1922).

"Consistency" alone has multiple established uses:
- **Logic:** consistency of axiomatic systems (Hilbert; Gödel).
- **Statistics:** consistency of estimators (convergence in probability to the true parameter).
- **Ethics:** consistency of moral judgments (Rawls; Singer).
- **Decision theory:** consistency of preferences (von Neumann–Morgenstern).
- **Set theory + model theory:** various technical uses.

"Consistency" as the framework gate would collide with all of these in academic readers' priors.

### §8.2 Principle #3 (misnaming is a rigor failure) check

Principle #3 holds that misnaming a framework concept is itself a rigor failure. The test: does "Consistency" name the gate's actual operation correctly?

The gate enforces *unit-commensurability* — that all admitted Cᵢ have units of the form (dollars × time) so they can be summed in the RCV integral without category-error. Calling this "Consistency" omits the load-bearing modifier (units). The naming would be technically defensible if the framework explicitly pre-defines "Consistency" as "unit-consistency" — but this is exactly the kind of redefinition Principle #3 identifies as rigor-shifting (asking the reader to override their established prior on a generic word).

**Principle #3 check: FAILS for Option A.** "Consistency" misnames the gate's actual operation.

### §8.3 Precision

"Units Consistency" is precise about what's being checked.
"Consistency" is imprecise.

Academic-rigor commitment to precision: violated by Option A.

**Verdict on M6:** B (Units Consistency) strongly preferred. Established literature alignment + Principle #3 check + precision all favor B.

---

## §9. M7 — Originality

**Test:** Coinage status / framework-distinctive claim.

**Finding:** Neither option is novel coinage — "consistency" and "units consistency" are both established mathematical vocabulary used by the framework, not coined by it. The framework's distinctive contribution at Gate 2 is the *application* (gating commons-extraction-cost claims by unit-commensurability), not the term.

**Verdict on M7:** INDIFFERENT.

---

## §10. M8 — Long-term potential

**Test:** Adoption durability across decades + cross-discipline travel.

### §10.1 Adoption durability

A term that travels intact through chapter prose, academic citation, legal brief, policy paper, and ordinary reading is more durable than one that requires per-context disambiguation. "Units Consistency" carries its meaning intact. "Consistency" depends on context.

### §10.2 Cross-discipline

In a cross-discipline citation (e.g., environmental-law brief citing the framework), "Consistency" without modifier surfaces the M6 collision profile (logic vs statistics vs ethics readings all available). "Units Consistency" travels cleanly.

**Verdict on M8:** B (Units Consistency) preferred. Adoption-durability favors specificity.

---

## §11. M9 — Risk

**Test:** Collision / ambiguity / misuse risk.

**Finding:** Option A increases risk on all three axes. Collision (per M6 §8.1). Ambiguity (per M5 §7.1). Misuse (a reader who misreads "Consistency" as logical-consistency or statistical-consistency would apply the gate incorrectly to candidate costs that fail unit-commensurability but happen to be logically-consistent).

**Verdict on M9:** B preferred.

---

## §12. M10 — Publishing

**Test:** Production-pipeline implications + indexing.

**Finding:** "Units Consistency" indexes more cleanly (a reader looking up "Consistency" in the index would have to disambiguate from the multiple non-framework meanings). "Consistency" alone is harder to index without misleading.

**Verdict on M10:** B (Units Consistency) preferred (mild).

---

## §13. M11 — Critic pressure

### §13.1 Character 9 (tenured economics chair)

**Probe:** "What's 'Consistency' supposed to mean here? Logical? Statistical? Cross-temporal?"

**Framework response under Option A:** the framework explicitly defines "Consistency" as unit-consistency in the Tech Appendix. The reader is asked to override the generic prior with the framework's specific meaning.

**Critic response:** "Why ask me to override a generic word's established meaning when 'Units Consistency' would have prevented the override altogether? That's surrendering precision for compactness."

**Critic verdict under Option A:** A loses. Forced override of established meaning is a rigor cost.

**Critic response under Option B:** No probe. "Units Consistency" reads cleanly.

### §13.2 Character 12 (graduate student)

**Probe:** "Is 'Consistency' the same as the consistency requirement in real-options theory? Or in stochastic discounting? Or in...?"

**Framework response under Option A:** the framework distinguishes its Gate-2 consistency from those by context.

**Critic response:** "Each citation requires me to look up the framework's definition. 'Units Consistency' would have answered the question at first read."

**Critic verdict under Option A:** A loses on cross-citation cost.

### §13.3 Character 17 (Ostrom-successor scholar)

**Probe:** "Ostrom's eight design principles are named with specific compound modifiers (clear boundaries; congruence with local conditions; etc.). Why would a framework that extends commons-governance into extraction strip the modifier from one gate?"

**Framework response under Option A:** the framework's Gate 2 is structurally simpler than Ostrom's principles.

**Critic response:** "The structural simplicity is irrelevant; the naming convention should align with the adjacent literature your framework explicitly extends."

**Critic verdict under Option A:** A loses on adjacent-literature alignment.

### §13.4 Aggregate M11 verdict

Option A surfaces multiple critic-pressure points; Option B surfaces none on this naming question.

**Verdict on M11:** B preferred.

---

## §14. M12 — Intellectual honesty

### §14.1 Prior-art audit on "Consistency" as framework-coined term

If "Consistency" were adopted as the framework's Gate 2 name, the framework would be implicitly claiming ownership of a generic word. Under M12 Corollary D 7-level action ladder:

- **Level 1 (original coinage):** FAILS — the word is not a framework coinage.
- **Level 2 (independent rediscovery acknowledged):** N/A — there's no specific prior author the framework would credit.
- **Level 3 (lexical collision disambiguated):** REQUIRED — but disambiguation requires per-use context, defeating the compactness gain.
- **Level 4 (collision rename required):** ACTIVE — the collision risk argues for renaming back to "Units Consistency" (or to "Commensurability" — see Option C).
- **Level 5 (rhetorical bridge):** N/A — not a teaching-bridge case.
- **Level 6 (extension positioning):** N/A — the framework is not extending an established "Consistency" theory.
- **Level 7 (borrowed term acknowledged):** the framework would have to acknowledge borrowing "Consistency" from logic/statistics/ethics, which is awkward because there's no specific prior author to credit and the framework's meaning is none of those uses.

**M12 verdict under Option A:** PROBLEMATIC. The naming creates a Level-4 collision-rename pressure.

### §14.2 Prior-art audit on "Units Consistency"

"Units consistency" / "dimensional consistency" is established mathematical-engineering terminology (Buckingham π theorem 1914; Bridgman 1922 *Dimensional Analysis*). The framework using it as a gate name is normal-mathematical-vocabulary use, not coinage.

**M12 verdict under Option B:** CLEAN. No prior-art conflict.

### §14.3 Aggregate M12 verdict

**Verdict on M12:** B strongly preferred. A creates a Level-4 collision-rename pressure that B does not.

---

## §15. §22.4 alignment (usefulness vs goals)

| Goal | Option A (Consistency) | Option B (Units Consistency) |
|---|---|---|
| Goal-1: vocabulary portability (term travels intact) | Negative (modifier-loss reduces travel) | Positive (term travels intact) |
| Goal-2: first-encounter accessibility | Negative (ambiguous) | Positive (specific) |
| Goal-3: academic-credibility (M6) | Negative (collision profile) | Positive (clean) |
| Goal-4: book-craft register | Even (compactness vs register-alignment) | Even |
| Goal-5: long-term adoption durability | Negative | Positive |

**Aggregate alignment:** B wins on 4 of 5 goals; tie on Goal-4. A loses on the 4 load-bearing goals.

**Verdict on §22.4:** B strongly preferred.

---

## §16. Cluster-coherence sub-test

**Test:** Does the proposed rename improve cohort-internal coherence?

### §16.1 Cohort-uniformity gain measurement

Current: 1 acronym + 1 compound-noun + 2 single-words.
Proposed: 1 acronym + 3 single-words.

The gain is: Gates 2/3/4 read more parallel as single-word property-nouns. Reader-experience: marginal improvement in the visual / aural rhythm of the cohort.

### §16.2 Cohort-uniformity loss measurement

The original `four_gates_cluster` finding holds: CIT-vs-others is the load-bearing asymmetry, not Gate-2-vs-Gates-3-and-4. Renaming Gate 2 does not address the load-bearing asymmetry.

### §16.3 Net cluster-coherence finding

**Marginal gain on Gates-2/3/4 parallelism. No effect on the load-bearing CIT-vs-others asymmetry.** The cluster-coherence gain is real but small.

**Verdict on cluster-coherence:** A produces a marginal gain. Not enough to overcome M6 + M11 + M12 + §22.4 losses.

---

## §17. Specificity-preservation sub-test

**Test:** Does the rename preserve the gate's specificity?

**Finding:** No. The modifier "Units" is doing load-bearing work — it tells the reader the gate enforces unit-commensurability, not generic consistency. Dropping the modifier loses the specificity.

**Could specificity be recovered?** Three paths:

1. **In-text disambiguation at first use** — the framework defines "Consistency" as unit-consistency at first introduction. Cost: every first-encounter requires context.
2. **Glossary entry** — the glossary clarifies. Cost: the term doesn't travel without the glossary lookup.
3. **Tech Appendix definition** — formal spec carries the meaning. Cost: same as (2); the term doesn't travel.

**Specificity-preservation verdict:** Specificity LOST. None of the recovery paths is cost-free.

---

## §18. Reader-inference sub-test (decisive)

**Test:** Can a first-encounter reader correctly infer the gate's function from the name alone?

### §18.1 Test scenario

A reader encounters: *"The four gates: CIT, Consistency, Boundedness, Independence."*

What does "Consistency" mean? The reader's available inferences:
- (a) Logical consistency — non-contradictory claims.
- (b) Statistical consistency — convergence properties.
- (c) Ethical consistency — coherent moral judgments.
- (d) Cross-temporal consistency — claim doesn't change over time.
- (e) Cross-case consistency — same form across cases.
- (f) Unit consistency — units commensurable.

The framework's meaning is (f). The reader can only narrow to (f) by either (i) framework-prior context (already read the introduction), (ii) inferring from the gate-2-position's function, or (iii) parenthetical disambiguation at each use.

### §18.2 Comparison: "Units Consistency"

A reader encounters: *"The four gates: CIT, Units Consistency, Boundedness, Independence."*

The modifier "Units" constrains the reading to (f). Reader correctly infers gate function from name alone.

### §18.3 Decisive finding

**Reader-inference is decisive in favor of "Units Consistency."** This is the same kind of decisive finding that the original `four_gates_cluster` pass used to reject parallel-rename options — the asymmetric naming reflects asymmetric gate functions; the modifier reflects the gate's specific operation.

**Verdict on reader-inference:** B (Units Consistency) wins decisively.

---

## §19. Option C — alternative single-word modifier preservation

If Option A is rejected on specificity grounds (which §17 and §18 confirm), an alternative would be a different *single-word* term that retains the units-meaning.

**Candidate: "Commensurability."**

- Single word (matches cohort-uniformity goal of A)
- Carries the units-meaning (preserves specificity)
- Established mathematical-engineering vocabulary (M6 clean)
- Per Bridgman 1922 + Buckingham π theorem + standard dimensional-analysis literature

**Comparison to Option B (Units Consistency):**

| Test | A (Consistency) | C (Commensurability) | B (Units Consistency) |
|---|---|---|---|
| Cohort-uniformity (single-word) | Win | Win | Lose |
| Specificity | Lose | Win | Win |
| M6 academic | Lose | Even | Win (slight) |
| M5 first-encounter | Lose | Win | Win |
| M12 collision | Lose | Even (mild collision with separability literature) | Win |
| Prose rhythm | Win | Even | Lose (slight) |
| Reader-inference at first use | Lose | Win (if "commensurability" prior is held) or Lose (if not) | Win |

**Commensurability sub-finding:** mixed verdict. Better than "Consistency" but slightly weaker than "Units Consistency" on the reader-inference test for readers without strong priors on the dimensional-analysis vocabulary. Not decisively better than the status quo.

**Verdict on Option C:** Defensible alternative; not strongly preferred over Option B. If the cohort-uniformity gain becomes load-bearing for some downstream reason, Option C is the better single-word path than Option A.

---

## §20. Author-ratified resolutions

### §20.1 Path choice

**Options:**
- (A) Rename Gate 2 to "Consistency" — REJECTED in this pass on specificity + M6 + M12 + §22.4 grounds.
- (B) Retain "Units Consistency" — **RECOMMENDED.**
- (C) Rename Gate 2 to "Commensurability" — DEFENSIBLE alternative; not strongly preferred over B.
- (D) Revisit four_gates_cluster verdict more broadly — out of scope for this pass.

**Ratified decision (2026-04-26, Chris Winn): Option B — RETAIN "Units Consistency."** Status quo per `four_gates_cluster_v1.0.0.md` ratification stands. This pass's verdict (REJECT rename) preserves the original four_gates_cluster verdict (CONFIRM cohort + acknowledge naming asymmetry as load-bearing structural distinction). Author note: "this pass + four_gates_cluster together cover the option space exhaustively."

### §20.2 Implications

- **No sweep needed** — current chapter-prose + Tech Appendix supplement + glossary v3 + cit_examples references to "Units Consistency" intact and unchanged.
- **Open Insight #2 closed-ratified 2026-04-26.** Closure provenance: `four_gates_cluster_v1.0.0.md` (original cluster verdict) + this pass (Gate-2-rename-only sub-option exhaustively tested). Together they cover the option space:
  - Cohort-level renaming for parallelism (`four_gates_cluster` Option B; tested both all-test-suffix and all-property-noun sub-options) — REJECTED
  - Cohort-level restructuring (`four_gates_cluster` Options C + D) — REJECTED
  - Single-gate rename to single-word property-noun (this pass's Option A) — REJECTED
  - Single-gate rename with single-word units-meaning preservation (this pass's Option C — Commensurability) — DEFENSIBLE-but-not-preferred
  - Status quo (cohort with naming asymmetry honoring CIT-as-test vs others-as-conditions) — RATIFIED across both passes
- **Four_gates_cluster ratification carry-forward.** This ratification implicitly confirms the four_gates_cluster verdict (Option A — confirm cohort + ratify "Units Consistency" + acknowledge naming asymmetry); the four_gates_cluster pass's §9 Author-ratified-resolutions section can be updated to reflect formal ratification with cross-reference to this pass.

---

## §21. Rerun gate

Rerun if:
- A reader-experience study (Berggruen-essay reception, beta readers, academic reviewers) reports the cohort-naming asymmetry as a comprehension obstacle that "Consistency" alone (or a different alternative) would resolve.
- A new gate is added that changes the cohort-coherence calculation.
- The framework's underlying mathematical apparatus changes such that Gate 2's function changes (e.g., if Gate 2 starts enforcing more than unit-commensurability).
- "Units Consistency" develops a problematic prior-art collision that didn't exist when the four_gates_cluster pass ran.

Absent these triggers, verdict stands.

---

## §22. Cross-references

- `tools/rigor-passes/archive/commons_bonds_rigor_pass_2026-04-24_four_gates_cluster_v1.0.0.md` — original cluster pass that this pass extends with the previously-untested Gate-2-rename-only sub-option.
- `tools/rigor-passes/archive/commons_bonds_rigor_pass_2026-04-24_vocabulary_footprint_meta_v1.0.0.md` — meta-pass §12.2 + §12.3 T2 decision (Units vs Dimensional).
- `tools/back-matter/sources/terms_index.md` — Four Gates record + Units Consistency record.
- `manuscript/technical-appendix/TechnicalAppendix_v0.0.5_supplement.md` §6.2 — Four Gates admission apparatus operationalization.
- `tools/back-matter/sources/glossary/archive/commons_bonds_updated_glossary_v3.html` — glossary entries for Four Gates terms.
- `alignment/commons_bonds_open_insights_v1.0.0.md` Insight #2 — gate-naming-cohort consistency.

---

*End of focused rigor pass v1.0.0. Option B (RETAIN "Units Consistency") RECOMMENDED. Reader-inference + M6 + M12 + §22.4 alignment all favor retention; cohort-uniformity gain is real but small and non-load-bearing. Pending author ratification at §20.*
