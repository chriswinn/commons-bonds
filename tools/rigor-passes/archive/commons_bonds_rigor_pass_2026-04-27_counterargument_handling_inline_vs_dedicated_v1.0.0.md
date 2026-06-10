# Commons Bonds — Full Rigor Pass: Counterargument-Handling Structure (Inline-Woven vs Dedicated-Section)

**Version:** 1.0.0
**Date:** 2026-04-27
**Protocol applied:** `tools/commons_bonds_rigor_protocol_v2.3.0.md` — full 12-module suite + §22 + §22.4 + all 6 Working Principles. Special focus on M3 (book content + counterargument coverage), M4 (craft / momentum / register), M5 (dinner-table + reading flow), M6 (academic), M8 (long-term / test-of-time), M11 (critic survival), M12 (intellectual honesty).
**Scope:** Tests Ch 6's full defensive-content cluster — the just-inserted "Why These Choices" (Passage N, ~2,000 words, uncommitted) + existing "What the Critics Will Say" section (~1,400 words) + existing "The Carbon Concession" (~600 words) + existing "Reproducibility and the Range of Defensible Estimates" (~900 words) = ~4,900 words of consecutive dedicated defensive material in the chapter's back half. Tests whether this material should be (1) included as currently structured, (2) compressed, (3) restructured into inline-woven prose at natural arising points throughout the chapter, (4) removed, or (5) restructured per some hybrid. Per author directive 2026-04-27: *"run a full rigor test on the inclusion of the counter arguments as written or if the best way to handle counterarguments would be as we are walking through the framework and when that particular counterargument would naturally arise vs. in a dedicated session as that tends to read as defensive and breaks the natural momentum and flow of the prose. Include the entire counterargument section and how it sets within Chapter 6, and feel free to test alternate arrangements or some similar verbiage and investigate if including them as is or in some other verbiage and if including them would make the book stronger, expand, compress, remove, and ultimately will this make the book great? will this make the book stand the test of time?"*
**Status:** rigor pass executed 2026-04-27; **ratified 2026-04-27 by Chris Winn** — full ratification of A-1 + B-2 + per-element inline routing. Plus cross-chapter sweep scheduled for Ch 2 / Ch 4 / Ch 5 / Ch 7 / Ch 8 / Ch 9 / Ch 10 per same discipline. Implementation: multi-commit chapter restructure begins with revert of uncommitted Passage N body in working tree (revert to commit `04da48f`) + this rigor pass §11 ratification + per-element inline-weave commits + final dedicated-section removal commit.
**Author:** Chris Winn

---

## §1. Executive summary

**RECOMMENDED: Option B-2 + per-counterargument inline routing.** DISSOLVE the four dedicated defensive sections; WEAVE each defense / counterargument / concession at its natural arising point in the chapter's framework walk-through. Implement as a multi-commit chapter-restructure.

**Decisive findings:**

1. **The v1.0.3 book scope discipline is load-bearing on this question.** [tools/commons_bonds_book_scope_v1_0_3.md:63](../../commons_bonds_book_scope_v1_0_3.md): *"**Counterargument work** woven through every chapter; **no counterargument stitched in as a separate chapter**."* And [§124](../../commons_bonds_book_scope_v1_0_3.md): *"Every chapter has its specific counterarguments **woven in** (the existing counterargument work is preserved, not redone)."* The literal rule is at chapter-level (no whole-chapter dedicated to counterarguments); the principle ("woven through" + "woven in") extends to dedicated within-chapter sections.

2. **Ch 6 currently violates the discipline at scale.** Four consecutive dedicated defensive sections in the chapter's back half (~4,900 words = ~half the chapter's text). This is exactly the "stitched-in-as-dedicated-section" pattern the discipline was authored to prevent. The pattern reads as defensive, breaks momentum, and sequences the chapter as: framework-walk-through → defensive-cluster → closing. Trade-press editors + literary agents reading the chapter would see the defensive cluster as a structural weakness.

3. **Every current defense / counterargument / concession HAS a natural inline arising point** — verified per-element in §4 below. Per the discipline test ("would naturally arise vs. dedicated session"), zero of the current material genuinely requires dedicated treatment. Each can land where its objection or design choice naturally surfaces in the framework walk-through.

4. **M8 test-of-time STRONGLY favors inline-woven.** Books that have stood the test of time in framework-introduction register (Adam Smith, Marx, Keynes, Ostrom, Mazzucato, Raworth) consistently use woven counterargument-handling. Dedicated counterargument sections are an academic-paper register pattern that doesn't transfer well to durable trade-press / academic-press book register. A book with woven counterargument-handling reads as confident; a book with dedicated counterargument sections reads as defensive — and the latter dates faster as the defensive postures themselves date.

5. **The Passage N "Why These Choices" structural problem is the most acute.** It's 2,000 words of dedicated alternative-tested-defense register sequenced immediately AFTER The Contribution section, BEFORE What the Critics Will Say. Reader trajectory: framework-walk-through → "but here's why we made each choice" → "but here's what critics will say" → "but here's the carbon concession" → "but here's the reproducibility caveat." Triple-decker defensive crouch; loses M4 craft + M5 dinner-table on momentum + M11 critic-survival on confident posture.

6. **The book gets STRONGER + STANDS THE TEST OF TIME with inline-woven structure.** The framework's intellectual content is unchanged; what changes is the surface structure. Inline-woven exposes the same counterarguments + defenses but at points where they advance the reader's understanding rather than retroactively defending it. Per M8 + M5 + M4 craft analysis: durable-book register; reads-as-confident; survives political-vocabulary regime shifts; matches successful adjacent-framework book patterns.

**Net verdict:** Restructure. Dissolve all four dedicated defensive sections. Weave each element at its natural arising point per §4 routing matrix. Multi-commit implementation.

---

## §2. The question under test

### §2.1 Author's question

> *"run a full rigor test on the inclusion of the counter arguments as written or if the best way to handle counterarguments would be as we are walking through the framework and when that particular counterargument would naturally arise vs. in a dedicated session as that tends to read as defensive and breaks the natural momentum and flow of the prose. Include the entire counterargument section and how it sets within Chapter 6, and feel free to test alternate arrangements or some similar verbiage and investigate if including them as is or in some other verbiage and if including them would make the book stronger, expand, compress, remove, and ultimately will this make the book great? will this make the book stand the test of time?"*

Four interacting sub-questions:

1. **Inclusion (axis A):** Include the defensive material at all? In what form?
2. **Structure (axis B):** Inline-woven / dedicated-section / hybrid?
3. **Per-element routing (axis C):** Where does each specific counterargument / defense / concession best land?
4. **Test-of-time (axis D):** Does the result stand the test of time + make the book great?

### §2.2 The defensive footprint under test

| # | Section | Status | Words | Content |
|---|---|---|---|---|
| 1 | Why These Choices | **JUST INSERTED, UNCOMMITTED** (Passage N body in working tree) | ~2,000 | 8 methodology defenses (CIT vs revealed-preference; two-instrument vs single; triangulation vs single-method; Hotelling Identity vs Pigou-only / Hotelling-only; Four Gates vs CIT alone; Option C' commons-as-examples vs legislative; ARR vs CBA; CIT two sub-forms vs single-form) |
| 2 | What the Critics Will Say | Existing | ~1,400 | 2 counterargument rebuttals (Objection 1: pricing-the-unpriceable / parameter-sensitivity / "choose-your-own-adventure"; Objection 2: Popperian falsifiability / "always-underpriced means unfalsifiable") |
| 3 | The Carbon Concession | Existing | ~600 | Concession that carbon term dominates SCC-dependency; chapter's "honesty clause" |
| 4 | Reproducibility and the Range of Defensible Estimates | Existing | ~900 | Inter-analyst-variation rebuttal (range-not-failure; analogous to SCC; framework guarantees transparent disagreement) |
| **TOTAL** | | | **~4,900** | ~half the chapter's prose; ~46% of post-Phase-B Ch 6 word count |

### §2.3 Options under test

**Axis A — Inclusion:**
- **A-1:** Include all current defensive material (4 sections + Passage N)
- **A-2:** Drop Passage N (methodology defenses); keep existing 3 dedicated counterargument-rebuttal/concession sections
- **A-3:** Drop existing 3 sections; keep Passage N
- **A-4:** Drop all dedicated defensive material; rely on inline-woven only

**Axis B — Structural arrangement:**
- **B-1:** All dedicated sections (current state + Passage N as inserted)
- **B-2:** All inline-woven (zero dedicated counterargument/defense sections; each element lands at natural arising point) — **RECOMMENDED**
- **B-3:** Hybrid — some dedicated for genuinely cross-cutting cases; others inline
- **B-4:** Compressed dedicated sections (keep dedicated structure but reduce each to ~500 words)

**Axis C — Per-counterargument routing:** detailed in §4 below.

**Axis D — Test-of-time:** evaluated against M8 in §6 below.

### §2.4 Falsifiers

- **B-2 falsified if:** a counterargument exists that has no natural inline arising point in the framework walk-through — would justify dedicated treatment.
- **B-2 falsified if:** weaving the material inline produces longer chapter total than dedicated structure (since inline weaving requires light surrounding-context expansion).
- **B-2 falsified if:** academic reviewers genuinely require dedicated counterargument-section as a discoverability convention.

---

## §3. Axis A — The inclusion question

### §3.1 Should the defensive material exist at all?

For each element, what does removal cost?

| Element | Removal cost |
|---|---|
| Methodology defenses (Passage N) | M11 Char 9 / Char 12 / Char 14 / Char 19 closure on "why these methodological choices?" — academic reviewer audiences expect alternative-tested justification. Closes M6.1 finding. |
| Pricing-the-unpriceable rebuttal (Objection 1) | M11 Char 14 (libertarian economist) + Char 8 (mainstream economist) closure on "this is a choose-your-own-adventure" attack. |
| Popperian falsifiability rebuttal (Objection 2) | M11 Char 12 (philosopher of science / methodological-rigor reader) closure. Critical for academic reception. |
| Carbon Concession | M3.4 + M12 honesty about parameter-dependency; the concession itself is intellectually-required given the chapter's quantitative claims. |
| Reproducibility-Range rebuttal | M11 + M3.4 closure on inter-analyst-variation attack; addresses range-not-failure misread. |

**Verdict on Axis A:** All five elements EARN inclusion. The substantive content closes load-bearing M11 audiences and supports M12 intellectual-honesty discipline. Removal is rejected. The question is structural, not inclusion.

---

## §4. Axis C — Per-element routing analysis (the natural-arising-point test)

### §4.1 Methodology defenses (Passage N's 8 sub-defenses)

| # | Defense | Natural inline arising point | Fit | Length cost |
|---|---|---|---|---|
| 1 | CIT vs revealed preference | At The Four Gates section opening, where CIT is first formally introduced as the discrimination gate. Or earlier, at Ten Commons section where commons-grounding is discussed. | **Strong fit** | ~150 words inline |
| 2 | Two-instrument architecture (CSD + RCV) vs single | At What Is Owed (Parfit grounding) section, where B = B₁ + B₂ is first introduced. | **Strong fit** (Parfit grounding already implies this defense; making it explicit is one paragraph) | ~150 words inline |
| 3 | Triangulation (Three Ways) vs single-method | At Approach 1 / Approach 2 / Approach 3 transitions, OR at "The Convergence" section opening (where the three methods are integrated). | **Strong fit** | ~200 words inline (could split across sections) |
| 4 | Hotelling Identity vs Pigou-only or Hotelling-only | At The Contribution section, where Pigou + Ostrom traditions are discussed as adjacent fields. | **Strong fit** (already partially there; one paragraph addition) | ~200 words inline |
| 5 | Four Gates vs CIT alone | At The Four Gates section, where each gate is introduced. The current section already structures this implicitly; making the alternative-tested rationale explicit is one paragraph. | **Strong fit** | ~150 words inline |
| 6 | Option C' (commons-as-examples) vs legislative | At Ten Commons Categories — Examples From the Cases This Book Examines section. **Already partially there** — the section's prose ("These are examples drawn from cases this book examines... The framework's universality is about the method, not about whether ten is the right number"). One paragraph elaborates the alternative-tested defense. | **Already partially inline; light expansion** | ~100 words inline |
| 7 | ARR vs CBA | At a TBD inline arising point — ARR isn't currently introduced explicitly in the chapter body. Could be introduced briefly at What the Chapter Leaves for Later (forward-pointer) OR worked into Method 3 / α-dominance discussion in Approach 3. | **Mid fit** — requires choosing where ARR enters the chapter | ~200 words inline |
| 8 | CIT two sub-forms (CAI + CCI) vs single-form | At The Four Gates section where CIT is introduced; the CAI + CCI framing is already there ("Commons-Absence Inversion asks... Commons-Consumption Inversion asks..."). One paragraph elaborates the alternative-tested defense. | **Already partially inline; light expansion** | ~150 words inline |

**§4.1 verdict:** All 8 methodology defenses have natural inline arising points. Total inline expansion ~1,300 words distributed across 6-7 existing sections (vs Passage N's 2,000 dedicated words). Net length reduction: ~700 words.

### §4.2 Counterargument rebuttals (What the Critics Will Say)

| # | Objection | Natural inline arising point | Fit |
|---|---|---|---|
| 1 | "Pricing the unpriceable / parameter-sensitivity / choose-your-own-adventure" | At Approach 1's carbon discussion (line 215-227 area), where the SCC range $3 / $42 / $190 first surfaces and "the bottom-up total rises to $550-570 per ton... carbon dominates" is established. The four-part response (structures-uncertainty / market-pricing-isn't-neutral / convergence-is-evidence / parameters-becoming-more-estimable) lands as a continuation of the carbon discussion. | **Strong fit** — already half there at lines 215-227 |
| 2 | "Popperian falsifiability / always-underpriced means unfalsifiable" | At The Convergence section (line 723-744 area), where "CS > 0 for case X under existing accountability regimes" prediction is established. The two-layer falsifiability response (CIT as thought-experiment filter; CS / RCV as empirical predictions) lands as a continuation of the convergence discussion. The Yeager-1947 analogy fits naturally there as the testability-when-instruments-don't-yet-exist illustration. | **Strong fit** |

**§4.2 verdict:** Both objections have strong natural inline arising points. Inline expansion ~800 words distributed across 2 existing sections (vs current dedicated ~1,400 words). Net length reduction: ~600 words.

### §4.3 The Carbon Concession

| Element | Natural inline arising point | Fit |
|---|---|---|
| Carbon-term-dominates concession + SCC-as-political-statement honesty | At Approach 1's carbon discussion (line 215-227 area). The chapter already half-treats this ("Three estimates spanning two orders of magnitude" — line 224; "the fight over the SCC is itself a proxy war over acceptable cost severance levels" — line 227). Folding the dedicated section's content into the carbon discussion completes the integration. | **Strong fit** — chapter already establishes the framing; the dedicated section duplicates work already partially done at line 215-227 |

**§4.3 verdict:** Carbon Concession integrates cleanly into the existing carbon discussion. Net length reduction: ~400 words (some content already exists at line 215-227).

### §4.4 Reproducibility and the Range of Defensible Estimates

| Element | Natural inline arising point | Fit |
|---|---|---|
| Range-not-failure rebuttal + transparent-disagreement framing | At The Convergence section (where the IPG ranges 5-133 etc. are first reported), OR after the Three Ways triangulation introduction (where range-output is established as a feature not a bug). Could also appear at the carbon discussion (Approach 1) given the SCC range is the chapter's most-prominent example. | **Strong fit** — fits at any of three natural points |

**§4.4 verdict:** Range-rebuttal integrates at any of three points. ~600 words inline (vs current dedicated ~900 words). Net length reduction: ~300 words.

### §4.5 Aggregate routing summary

| Source | Current dedicated words | Inline-woven words | Net reduction |
|---|---|---|---|
| Passage N (Why These Choices) | ~2,000 | ~1,300 | ~700 |
| What the Critics Will Say | ~1,400 | ~800 | ~600 |
| The Carbon Concession | ~600 | ~200 (already partially in line 215-227) | ~400 |
| Reproducibility and the Range | ~900 | ~600 | ~300 |
| **TOTAL** | **~4,900** | **~2,900** | **~2,000** |

Inline-woven approach: ~2,000-word net reduction in chapter length AND woven discipline AND defensive-structure dissolution. Triple win on M3 + M4 + M5 + M11.

---

## §5. Axis B — Structural arrangement (the load-bearing question)

### §5.1 What B-1 (current dedicated structure) optimizes for

- Discoverability for skim-reading critics (counterarguments at known location)
- Q-A register familiarity for academic-paper-trained readers
- Author-explicit signaling that counterarguments are taken seriously
- Each counterargument gets dedicated paragraph-level depth

### §5.2 What B-2 (inline-woven) optimizes for

- M4 craft / momentum (chapter reads as confident framework introduction, not framework-then-defense)
- M5 dinner-table (no defensive crouch register; reader stays in framework register)
- M8 test-of-time (matches successful long-running adjacent-framework books)
- M3 chapter length (~2,000-word net reduction)
- M12 woven-discipline (per book_scope v1.0.3 §63 + §124)
- Each counterargument addressed where reader's mind would naturally raise it (more pedagogically effective)

### §5.3 What B-3 (hybrid) would require

A criterion for which counterarguments belong dedicated vs inline. Per the natural-arising-point test in §4, every current defensive piece has a natural inline arising point. So no counterarguments meet the criterion-for-dedicated. B-3 collapses into B-2 in practice.

### §5.4 What B-4 (compressed dedicated) would optimize for

A halfway position — keep dedicated structure but reduce each section to ~500 words. Cost-benefit:
- Pro: less length cost
- Con: still violates woven discipline; still reads as defensive cluster; doesn't solve M4/M5/M8 issues

B-4 is a non-improvement.

### §5.5 The successful-adjacent-framework-books test (M8 + M10)

| Book | Counterargument structure | Outcome |
|---|---|---|
| Smith, *Wealth of Nations* | Inline-woven through prose | Stood test of time |
| Marx, *Capital* | Inline-woven; counterarguments in argument-progression | Stood test of time |
| Keynes, *General Theory* | Inline-woven within argument-flow | Stood test of time |
| Ostrom, *Governing the Commons* | Inline-woven through case walks; some critique-engagement at chapter ends but not as dedicated counterargument-rebuttal section | Stood test of time |
| Mazzucato, *Value of Everything* | Inline-woven at category-transitions | Bestseller; sustained influence |
| Raworth, *Doughnut Economics* | Inline-woven through framework-walk | Bestseller; viral adoption |
| Klinenberg, *Palaces for the People* | Inline-woven through case studies | Bestseller |
| Piketty, *Capital in 21st Century* | Inline-woven; light footnoted counterargument-engagement | Bestseller; lasting influence |

**Pattern: 8 of 8 successful framework-introduction books use inline-woven counterargument structure.** The dedicated-counterargument-section pattern appears more in academic-paper register and in less-durable framework-introduction books.

This is the M8 + M10 evidence. A book targeted at the publishing-path Commons Bonds aspires to (academic-press / serious-trade-press, multi-decade reception) should match the structural pattern of successful adjacent books.

### §5.6 Verdict on Axis B

**B-2 (inline-woven) is dominant.** Strong on M4 + M5 + M8 + M10 + M11 + M12. Matches successful adjacent-framework-book patterns. Net chapter-length reduction. Closes book_scope v1.0.3 discipline violation.

---

## §6. Axis D — Test-of-time / book-greatness analysis

### §6.1 Will the chapter stand the test of time under B-1 (current dedicated)?

The intellectual content is durable; the structural pattern dates. The "Why These Choices" + "What the Critics Will Say" + "Carbon Concession" + "Reproducibility Range" sequence reads as defensive even on first encounter. Over time, defensive postures date faster than confident postures because:

- The specific objections being rebutted may stop being load-bearing as the field evolves (the 2020s "is this a model?" attack may not be the 2050s attack).
- Dedicated counterargument sections fix the chapter's anxieties at a specific moment in academic-discourse time.
- Future readers may find the dedicated-defense register quaint or tone-deaf.

### §6.2 Will the chapter stand the test of time under B-2 (inline-woven)?

The intellectual content stays. The structural pattern is durable: confident framework-introduction with counterarguments addressed where they advance reader understanding rather than at retrospective-defense register. This is the pattern of canonical framework-introduction books across two centuries (Smith → Marx → Keynes → Ostrom → Mazzucato → Raworth).

Over time:
- The framework's claims continue to be addressed at points that match how readers' minds naturally engage them.
- Specific objections that arise inline are pedagogically integrated rather than retroactively defended.
- The chapter's structural pattern matches the canonical-framework-book pattern.

### §6.3 Will the book be GREAT under B-2?

Three book-greatness contributions from B-2:

1. **Confident posture.** The framework reads as confident because it doesn't need a dedicated defensive section to legitimate its choices. Each choice is justified at the moment it's introduced.
2. **Reader trust.** The chapter respects the reader's intelligence by addressing objections at the moment those objections naturally arise — not by deferring them to a back-half cluster the reader has to wait for.
3. **Cross-political-tradition adoption-bandwidth.** Defensive posture register signals "this framework is in trouble"; confident posture register signals "this framework is doing the work." Inline-woven structure widens the adoption-bandwidth across reader political traditions.

Under B-1, the chapter's defensive register narrows greatness; the framework's intellectual content carries the work despite the structural pattern. Under B-2, the structural pattern amplifies the intellectual content's authority.

### §6.4 Verdict on Axis D

**B-2 makes the book GREATER + STANDS THE TEST OF TIME more reliably than B-1.** The structural pattern of B-2 matches successful framework-introduction books across two centuries; B-1 matches academic-paper register that doesn't transfer well to durable book register.

---

## §7. M1–M11 abbreviated module results

| Module | B-1 (current dedicated) | B-2 (inline-woven) |
|---|---|---|
| **M1 CORE math** | PASS | PASS — math unchanged |
| **M2 Case study** | PASS | PASS — cases unchanged |
| **M3 Book content** | Adequate; chapter-length-bloat from defensive cluster | **STRONGER** — counterarguments addressed where they advance reader understanding; net ~2,000-word reduction |
| **M3.4 Counterargument coverage** | COVERED via dedicated sections | COVERED via inline-woven distribution across natural arising points; **MORE pedagogically effective** |
| **M4 Craft** | Weakens — defensive cluster register breaks momentum + flow | **STRONGER** — confident framework-introduction register throughout; momentum preserved |
| **M5 Dinner-table** | Weakens — chapter ends with defensive-crouch sequence | **STRONGER** — chapter's framework-introduction register is sustained to chapter close |
| **M6 Academic** | Adequate — academic readers tolerate dedicated counterargument sections | **STRONGER OR EQUAL** — modern academic discourse increasingly weaves; matches Ostrom + Mazzucato + Raworth pattern |
| **M7 Originality** | Adequate | **STRONGER** — framework's confidence signals originality without needing to defend it |
| **M8 Long-term / test-of-time** | **WEAKENS** — defensive register dates; matches academic-paper pattern not durable-book pattern | **STRONGLY STRENGTHENS** — matches 8/8 canonical successful framework-introduction books |
| **M9 Risk** | Risk: chapter reads as defensive; readers may infer framework is in trouble | LOW — confident posture matches mature-framework register |
| **M10 Publishing** | Trade press editor flags defensive cluster as structural weakness | **STRENGTHENS** — matches successful trade-press / academic-press patterns |
| **M11 Critic** | Critic finds counterarguments at known location | **EQUAL OR STRONGER** — engaged critic finds counterarguments at natural-arising points (more pedagogically integrated); skim-reader sees no defensive cluster (better impression) |

**§22 alignment:** B-2 positive on Primary Goals — Publishing Path (matches successful-book patterns); Academic Reception (modern discourse uses woven counterarguments); Long-term Impact (M8 durability); Adoption-Bandwidth (confident register reaches broader political traditions).

**§22.4 stand-test-of-time alignment:** STRONGLY POSITIVE for B-2.

---

## §8. M12 — Intellectual honesty audit

### §8.1 B-1 (current dedicated) M12

- M3.4 counterargument-coverage requirement met via dedicated sections.
- BUT: Honest acknowledgment that the chapter has TWO consecutive defensive-section clusters (Why These Choices + What the Critics Will Say + Carbon Concession + Reproducibility Range) is structurally distinct from intellectual-honesty about counterarguments. The latter requires the counterarguments be addressed; the former requires the structure not signal defensiveness.
- M12 PASSES on substance (counterarguments addressed); FAILS on structure (defensive cluster signals retroactive-defense register).

### §8.2 B-2 (inline-woven) M12

- M3.4 counterargument-coverage requirement met via inline-woven distribution.
- Each counterargument addressed at the point its objection naturally arises in the framework walk-through. This is MORE intellectually honest because it surfaces the objection at the moment the reader is most likely to be holding it, rather than batching objections into a back-half cluster.
- M12 PASSES on both substance + structure.

### §8.3 The book_scope v1.0.3 §63 + §124 discipline check

B-1 violates the explicit discipline ("counterargument work woven through every chapter; no counterargument stitched in as a separate chapter"). B-2 honors it.

While the literal rule is at chapter-level (no whole-chapter dedicated to counterarguments), the principle ("woven through" + "woven in") extends naturally to dedicated within-chapter sections. B-1's four-section defensive cluster is exactly the "stitched-in" pattern the discipline opposes.

### §8.4 M12 verdict

**B-2 is M12-optimal.** Honors substance + structure + book_scope v1.0.3 discipline.

---

## §9. Cross-chapter sweep implications

If B-2 is ratified for Ch 6, the same discipline should be applied chapter-by-chapter to other drafted chapters (Ch 2, 4, 5, 7, 8, 9, 10) which may carry similar dedicated defensive sections. Sweep candidates:

- **Ch 5** — has "Restitution and Foreclosure: Two Directions of Accountability" section (per v1.45.0 handoff) which is methodology-engagement (companion to Ch 6 Restitution Lineage). Currently a dedicated section; question is whether it's woven or stitched.
- **Ch 7** — On Other Worlds; the universality test framing may carry counterargument-handling around space-economics-is-far-fetched and Mars-as-arbitrary objections.
- **Ch 8** — What Things Actually Cost; counterarguments around bottom-up-accounting vs externalities-only objections.
- **Ch 9** — Pricing Honestly; the policy economy chapter likely has the highest counterargument-handling load.
- **Ch 10** — Common Bonds; closing chapter; counterargument handling at the meditative-closing register.

This rigor pass scopes Ch 6 only. Cross-chapter sweep is a follow-up scope question. If the woven discipline is applied chapter-by-chapter under Insight #22 sweep discipline + this rigor pass's verdict, ~5-7 additional chapter-restructure passes would land over the next few sessions.

---

## §10. Verdict synthesis + recommendation

### §10.1 Recommended combination

**Axis A:** A-1 (include all defensive material in some form — substantive content is load-bearing for M11 audiences).

**Axis B:** **B-2 (all inline-woven; dissolve all four dedicated defensive sections).**

**Axis C:** Per-element routing per §4 routing matrix:
- 8 Why These Choices defenses → distributed across 6-7 existing sections (Ten Commons; What Is Owed; Restitution Lineage; Two Kinds of Commons; Four Gates; The Convergence / Approach 1-2-3 transitions; Contribution)
- Pricing-the-unpriceable rebuttal → inline at Approach 1 carbon discussion (line 215-227 area)
- Popperian falsifiability rebuttal → inline at The Convergence section
- Carbon Concession → inline at Approach 1 carbon discussion (consolidates with parameter-sensitivity rebuttal; chapter already half-treats this at line 215-227)
- Reproducibility-Range rebuttal → inline at The Convergence section (consolidates with falsifiability rebuttal) OR after Three Ways triangulation introduction

**Axis D:** B-2 makes the book GREATER + STANDS THE TEST OF TIME relative to B-1.

### §10.2 Implementation approach

Multi-commit chapter-restructure:

1. **Commit R-1**: Discard uncommitted Passage N body insertion (working tree → match HEAD); restart Passage N as inline-woven distribution.
2. **Commit R-2 through R-N (~6-8 commits)**: One per inline-weave operation, distributing the methodology defenses + counterargument rebuttals + concessions across natural arising points.
3. **Final commit**: Remove the now-empty dedicated sections (Why These Choices new placement; What the Critics Will Say; The Carbon Concession; Reproducibility and the Range of Defensible Estimates).
4. **Marker block + line 169 cleanup commit** (already-queued task) handles remaining marker block content.

### §10.3 What this strengthens

- **M3 Book content:** ~2,000-word net chapter reduction; counterarguments addressed pedagogically.
- **M4 Craft:** confident framework-introduction register sustained through chapter.
- **M5 Dinner-table:** no defensive crouch; chapter reads as confident exposition.
- **M6 Academic:** matches modern academic discourse pattern.
- **M8 Long-term:** matches successful adjacent-framework book patterns; durable structural pattern.
- **M10 Publishing:** trade press + academic press both prefer confident structural pattern.
- **M11 Critic:** counterarguments addressed where critics' objections naturally arise — more pedagogically effective + still discoverable.
- **M12 Intellectual honesty:** honors both substance + structure; closes book_scope v1.0.3 discipline violation.

### §10.4 What this doesn't change

- Framework intellectual content — unchanged.
- Counterargument coverage — fully preserved (per §4 routing matrix).
- Methodology defenses — fully preserved.
- Bibliography references — unchanged.
- Tech Appendix integration — unchanged.
- Ch 5 / Ch 9 cross-references — unchanged (Ch 5 Restitution-and-Foreclosure section continues as methodology-engagement companion; Ch 9 policy economy continues as political-action chapter).

### §10.5 Rejected alternatives + rationale

| Alternative | Rejected because |
|---|---|
| **A-2 (drop Passage N only; keep existing 3 dedicated sections)** | Doesn't solve the structural problem. The remaining 3 sections still form a defensive cluster. Half-measure. |
| **A-3 (drop existing 3; keep Passage N)** | Removes load-bearing M11 closure (parameter-sensitivity + falsifiability) without solving Passage N's structural problem. |
| **A-4 (drop all defensive material entirely)** | Removes load-bearing M11 closures; M3.4 counterargument-coverage gap; methodologically dishonest. |
| **B-1 (keep current dedicated structure + commit Passage N)** | Violates book_scope v1.0.3 discipline; defensive cluster register; M4 + M5 + M8 weaknesses; doesn't match successful-adjacent-book patterns. |
| **B-3 (hybrid)** | Per §4 routing analysis, every element has a natural inline arising point, so no element meets the criterion-for-dedicated. B-3 collapses to B-2. |
| **B-4 (compressed dedicated)** | Doesn't solve woven-discipline violation; doesn't solve M4 + M5 + M8 weaknesses; halfway non-improvement. |

### §10.6 Three rigor questions on whole counterargument-handling structure

| Question | Verdict |
|---|---|
| **Earns place?** | **YES** for substantive content (M11 closures load-bearing); **NO** for dedicated-section structural pattern (woven-discipline violation). |
| **Would expansion strengthen?** | **NO** — current dedicated sections already at full length; expansion compounds the structural problem. |
| **Would compression strengthen?** | **YES** — and the maximum compression is full dissolution-into-inline-woven (~2,000-word net reduction + structural improvement). B-4 (compressed dedicated) is a halfway compression that doesn't capture the full benefit. |

---

## §11. Author-ratified resolutions

**Ratified 2026-04-27 by Chris Winn — full ratification of A-1 + B-2 + per-element inline routing.**

1. **A-1 — INCLUDE all current defensive substance.** Counterargument coverage + methodology defenses + concessions all preserved (closes load-bearing M11 audiences; M3.4 coverage maintained).

2. **B-2 — ALL INLINE-WOVEN.** Dissolve all four dedicated defensive sections (Why These Choices [Passage N]; What the Critics Will Say; The Carbon Concession; Reproducibility and the Range of Defensible Estimates). Counterargument-handling becomes woven prose throughout the chapter at points where each objection / defense / concession naturally arises.

3. **Per-element inline routing per §4 routing matrix.** Each defensive piece lands at its identified natural arising point.

4. **Cross-chapter sweep scheduled.** Same discipline (book_scope v1.0.3 §63 + §124 + this rigor pass's verdict) to be applied to Ch 2 / Ch 4 / Ch 5 / Ch 7 / Ch 8 / Ch 9 / Ch 10 — per-chapter rigor checks. Estimated 5-7 follow-up chapter-restructure passes if the discipline is applied across all drafted chapters.

**Implementation cadence:**
- Revert uncommitted Passage N body insertion in working tree (revert Chapter__6_ThreeWaysofCounting__Draft.html to post-Passage-M-ratification state, commit `04da48f`).
- Multi-commit chapter restructure across ~7-9 inline-weave operations.
- Final commit removes now-empty dedicated section wrappers + any closing-section content that remains non-defensive.
- Marker block + line 169 cleanup commit (already-queued task) handles remaining marker block content separately.

**Ratifications activated:**
- B-2 inline-woven discipline confirmed at chapter-level structural register (extends book_scope v1.0.3 §63 + §124 from chapter-level to within-chapter-section-level).
- Cross-chapter sweep scheduled per Insight #22 sweep discipline + this rigor pass's verdict.
- Successful-adjacent-framework-book pattern (8/8 of Smith / Marx / Keynes / Ostrom / Mazzucato / Raworth / Klinenberg / Piketty) adopted as durable structural model for Commons Bonds.
- Test-of-time discipline reaffirmed (confident framework-introduction register; counterarguments addressed at natural arising points, not in retrospective-defense register).

---

## §12. Rerun gate

Rerun if:
- book_scope v1.0.3 woven-discipline (§63 + §124) is reversed or modified.
- Adoption evidence shows skim-reading critics fail to find inline-woven counterargument-handling (would push toward B-3 hybrid for some specific objections).
- Cross-chapter sweep reveals a counterargument that genuinely has no natural inline arising point (would surface a new dedicated-section-justified case).
- Future Ch 6 holistic review (per Insight #22 sweep discipline) reconsiders the chapter's structural register.

---

*End of full rigor pass v1.0.0 on counterargument-handling structure (inline-woven vs dedicated-section). I-A + B-2 + per-element inline routing recommended. All 12 modules examined; decision dominated by M4 craft + M5 momentum + M8 test-of-time + M12 woven-discipline + 8/8 successful adjacent-framework-book pattern match. Pending author ratification.*
