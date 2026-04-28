# Commons Bonds — Focused Rigor Pass: Ch 8 ("What Things Actually Cost") Restructure

**Version:** 1.0.0
**Date:** 2026-04-27
**Protocol applied:** `tools/commons_bonds_rigor_protocol_v2.3.0.md` — full 12-module suite + §22 + §22.4 + all 6 Working Principles. Special focus on M3 (book content; tier-vocabulary regression), M4 (craft / chapter-pacing), M6 (academic), M8 (long-term / test-of-time), M11 (critic survival), M12 (intellectual honesty).
**Scope:** Tests structural restructure for Ch 8 ("What Things Actually Cost"; 5,946 words; 14 h3 sections in current draft). Ch 8 is the framework's load-bearing worked-example chapter — *"one ton of McDowell County coal walked through the framework's full cost-decomposition"* — but its current draft is scaffolded on the 8-tier scheme that was RETIRED 2026-04-24 per [tier-reframing rigor pass §11](commons_bonds_rigor_pass_2026-04-24_tier_reframing_v1.0.0.md). Tests four interacting decisions:
1. **Section-organization approach** (Decision 1: tier-label rename / Cᵢ-indexed reframing / hybrid)
2. **Counterargument-handling approach** (Decision 2: full dissolution / lighter touch / no restructure)
3. **Abundance-test-vocabulary cleanup** (Decision 3: AIT references → CIT throughout)
4. **Scope-note + chapter-framing** (Decision 4: line 13 scope-note completion + tier-vocabulary sweep in chapter framing)

Per author directive 2026-04-27: *"Run a focused Ch 8 full rigor pass."*

**Status:** rigor pass executed 2026-04-27; pending author ratification.
**Author:** Chris Winn

---

## §1. Executive summary

**RECOMMENDED:** Option **D1-C + D2-A + D3-A + D4-A** — Hybrid structural reframing (Cᵢ-via-Four-Gates explicit framing while preserving 8-section worked-example pacing); full dissolution of "Two counterarguments, compressed" section; complete AIT → CIT vocabulary sweep; scope-note completion + tier-vocabulary cleanup in chapter framing.

**Decisive findings:**

1. **Ch 8 is the framework's load-bearing worked-example chapter.** The chapter's pedagogical role — *"price one ton honestly through every cost component"* — is essential for the framework's empirical anchor. The chapter's organizing principle (8-section walkthrough with arithmetic that sums to a floor estimate) is pedagogically strong and should be PRESERVED. What needs to change is the structural scaffolding's vocabulary and framing, not the worked-example structure itself.

2. **Three categories of issues identified, with different magnitudes:**
   - **Major (Decision 1 + 3 + 4):** Tier-vocabulary regressions throughout (8 h3 section labels; "the eight tiers" scope note; "tier by tier" prose; "abundance test" 3 references) — the chapter's surface vocabulary is RETIRED-vocabulary-saturated and requires comprehensive sweep.
   - **Medium (Decision 2):** "Two counterarguments, compressed" dedicated h3 section — discipline violation per ratified counterargument-handling rigor pass; smaller scope than Ch 6 (~470 words; chapter-close coda style; not a defense-walkthrough).
   - **Minor:** Scope-note truncation at line 13 ("delivers the intergene[ration...]" — looks like draft cutoff requiring completion).

3. **Decision 1: Hybrid (1C) is dominant.** Light-rename (1A: drop "Tier N —" prefixes only) under-corrects (chapter still feels implicitly tier-organized; reader doesn't see the connection to current Cᵢ-via-Four-Gates framework). Cᵢ-indexed reframing (1B: structural restructure to "C₁ Direct Health Cost / C₂ Environmental Degradation Cost / ..." or similar) over-corrects and may distance reader through subscript-notation register. Hybrid (1C) keeps the chapter's strong 8-section walkthrough pacing while reframing the structural scaffolding via explicit "Cᵢ admitted through Four Gates" framing in chapter intro + scope note + closing recap. Reader-flow preserved; framework-vocabulary alignment achieved.

4. **Decision 2: Full dissolution (2A) is proportional.** The "Two counterarguments, compressed" section is ~470 words; both counterarguments have natural inline arising points elsewhere in the chapter:
   - **"Degrowth" charge** → folds into "The brief extrapolation" (line 207-217) where the $10-15T/year figure invites the degrowth association.
   - **"Pulling up the ladder" charge** → folds into "The brief extrapolation" or into "What honest pricing does NOT mean" section (line 195+) which already does similar coda work with two misreadings.
   The chapter-close section can become a clean closing without the "Two counterarguments" coda; the substance is preserved at natural arising points. Lighter-touch (2B) leaves the dedicated h3 wrapper which is the load-bearing structural issue. No-restructure (2C) under-applies discipline.

5. **Decision 3: Comprehensive AIT → CIT sweep.** The chapter has 3 "abundance test" references (lines 91, 111, 131) that all should become "Commons Inversion Test" or "CIT" per the CIT rename rigor pass. Plus the surrounding prose may need light adjustment to match CIT's two-sub-form architecture (CAI + CCI) where the original AIT framing was single-form.

6. **Decision 4: Scope-note completion + tier-vocabulary cleanup.** Line 13 has truncated "delivers the intergene[ration...]" — needs completion. Line 21 has "tier by tier" — needs reframing. Line 13 also has "through the eight tiers" — needs reframing.

7. **M8 test-of-time analysis:** The 8-tier scheme was a 2025-era framework artifact dissolved within months of its formal articulation. A book published with 8-tier scaffolding ages quickly as the framework's vocabulary moves on. The Cᵢ-via-Four-Gates framing is the framework's CURRENT ratified architecture and is durable across the publication horizon. Restructure now or ship a chapter whose vocabulary is already retired.

8. **Implementation cost-benefit:** Option D1-C + D2-A + D3-A + D4-A requires ~3-5 commits across decisions; ~2-4 hours of careful prose work. The benefit is strong: closes major chapter-level vocabulary regression; honors counterargument-handling discipline; preserves chapter pedagogical strength.

**Net verdict:** Hybrid structural reframing (D1-C) + full counterargument-section dissolution (D2-A) + comprehensive AIT → CIT sweep (D3-A) + scope-note completion (D4-A). Multi-commit restructure preserving the chapter's load-bearing worked-example pedagogy while bringing surface vocabulary + structural framing into alignment with current framework architecture.

---

## §2. The question under test

### §2.1 Author's directive

> *"Run a focused Ch 8 full rigor pass."*

Surfaced after Ch 8 cross-chapter sweep scope assessment found:
- 8 dedicated h3 sections labeled "Tier 1 — Direct Health Cost" through "Tier 8 — Temporal Displacement Cost"
- "The sum" recap with 8 line items
- Scope note (line 13): *"It walks one extraction — one ton of McDowell County coal — through the eight tiers..."* (truncated mid-sentence)
- "Two counterarguments, compressed" dedicated h3 section at line 221+
- 3 references to "abundance test" (retired AIT vocabulary)

### §2.2 Four interacting decisions

**Decision 1 — Section-organization approach:**
- **1A:** Light-rename only — drop "Tier N —" prefixes; keep 8 sections + arithmetic + sum recap
- **1B:** Cᵢ-indexed reframing — restructure as "C₁ ... C₈" or similar; explicit Four Gates apparatus throughout
- **1C:** Hybrid — keep 8-section walkthrough pacing + arithmetic + sum recap; rename without "Tier N" prefix; add explicit Cᵢ-via-Four-Gates framing in chapter intro + scope note + closing recap **— RECOMMENDED**

**Decision 2 — Counterargument-handling approach:**
- **2A:** Full dissolution — distribute both counterarguments to natural arising points; remove dedicated "Two counterarguments, compressed" h3 **— RECOMMENDED**
- **2B:** Lighter touch — remove dedicated h3 wrapper + meta-framing only; keep substance in adjacent prose
- **2C:** No restructure — accept the dedicated section as is

**Decision 3 — Abundance-test vocabulary cleanup:**
- **3A:** Comprehensive AIT → CIT sweep — replace all 3 "abundance test" references; adjust surrounding prose for CIT two-sub-form architecture **— RECOMMENDED**
- **3B:** Light fix — replace "abundance test" → "Commons Inversion Test" with no surrounding adjustment

**Decision 4 — Scope-note + chapter-framing:**
- **4A:** Complete scope-note (line 13) + sweep tier-vocabulary in chapter framing (line 13, 21, etc.) **— RECOMMENDED**
- **4B:** Complete scope-note only; preserve "tier by tier" prose

### §2.3 Falsifiers

- **D1-C falsified if:** the "Cᵢ via Four Gates" framing in chapter intro reads as math-jargon that distances readers; would push toward 1A (lighter rename + plain-prose framing).
- **D2-A falsified if:** the two counterarguments don't have natural inline arising points without disrupting chapter flow; would push toward 2B.
- **D3-A falsified if:** replacing "abundance test" with "CIT" requires substantive prose-rewriting beyond simple substitution; might push toward Ch 8 scope-expansion in restructure work.
- **D4-A falsified if:** scope-note completion reveals deeper chapter-framing issues that warrant reconsidering chapter scope entirely.

---

## §3. Findings inventory

### §3.1 Tier-vocabulary regressions (8-tier scheme dissolved 2026-04-24)

| Location | Current text | Issue |
|---|---|---|
| Line 13 (scope note) | "It walks one extraction — one ton of McDowell County coal — through the eight tiers, delivers the intergene[ration..." | Retired vocabulary + truncation |
| Line 21 (chapter framing) | "tier by tier, against the extraction we've been following" | Retired vocabulary |
| Lines 37, 49, 61, 73, 89, 103, 115, 129 (h3 section labels) | "Tier 1 — Direct Health Cost" through "Tier 8 — Temporal Displacement Cost" | Retired vocabulary at structural-organization level |
| Line 45 | "Tier 1 alone — the most documented tier — returns roughly as much as the coal sold for" | Retired vocabulary |
| Line 57 | "added to tier one, already places the national severed cost..." | Retired vocabulary |
| Line 69 | "Running total across the first three tiers" | Retired vocabulary |
| Lines 75 | "This is the tier Chapter 2 named through the $100 barrel passage..." | Retired vocabulary |
| Line 91 | "tier five is the one the abundance test reveals" | Retired vocabulary (tier + abundance-test double regression) |
| Line 105 | "The sixth tier is the one that is hardest to see..." | Retired vocabulary |
| Line 131 | "The final tier is the one revealed by the abundance test most starkly. It is the cost of *when*." | Retired vocabulary (tier + abundance-test double regression) |
| Line 145 | "Running the total at the low end of every tier" | Retired vocabulary |
| Lines 147-161 (sum recap) | "Tier 1 (Direct Health): $2 · Tier 2 (Environmental Degradation): $1 · ... · Tier 8 (Temporal Displacement): $2" | Retired vocabulary in sum recap |

**Aggregate:** 18+ "tier" references across the chapter; 3 "abundance test" references. Comprehensive sweep required.

### §3.2 Counterargument-section discipline check

**"Two counterarguments, compressed"** (line 221, ~470 words):
- Charge 1: "this is degrowth in a different vocabulary"
- Charge 2: "honest pricing is a tool by which already-industrialized nations pull up the ladder behind them"

Per ratified [counterargument-handling rigor pass](commons_bonds_rigor_pass_2026-04-27_counterargument_handling_inline_vs_dedicated_v1.0.0.md) §10, dedicated counterargument h3 sections should be dissolved (B-2 inline-woven discipline). Ch 8's section is smaller-scope than Ch 6's was (~470 words vs ~4,900 words; chapter-close coda style vs full back-half defensive cluster) but structurally the same kind of violation.

### §3.3 Inline-woven counterargument-handling (already canonical)

Lines 179-189 contain the YIMBY-objection rebuttal **inline within "The pattern made legible" section** — no dedicated h3 wrapper. This is canonical inline-woven pattern; matches Ch 4 + Ch 7 + successful adjacent-framework books. **Already compliant; no changes needed at this section.**

### §3.4 Chapter pedagogical strength preserved across all options

The chapter's worked-example structure (8-section walkthrough + arithmetic + sum recap producing $558/ton floor) is the framework's load-bearing empirical anchor. All options preserve this structure; differences are in surface vocabulary + structural framing only.

---

## §4. Decision 1 — Section-organization approach

### §4.1 Option 1A (light rename) analysis

Drop "Tier N —" prefixes; section h3s become "Direct Health Cost / Environmental Degradation Cost / ..." Keep arithmetic + sum recap with cost-component names instead of tier numbers.

**Pros:** Minimal restructure (~10 minutes; pure surface-edit). Preserves chapter pacing exactly. Reader flow unchanged.

**Cons:** Implicit-8-organization remains. Reader doesn't see connection to current Cᵢ-via-Four-Gates framework. The "tier" mental model may persist in reader memory even without label. Doesn't anchor the chapter's worked-example to the framework's current architecture.

### §4.2 Option 1B (Cᵢ-indexed reframing) analysis

Restructure as "C₁ Direct Health Cost / C₂ Environmental Degradation Cost / ..." with explicit Four Gates apparatus integrated throughout. Possibly fold cost components into Cᵢ-categories rather than 8 sections.

**Pros:** Maximally aligned with current framework architecture. Reader sees explicit Cᵢ-via-Four-Gates connection. Tech Appendix audience finds chapter's arithmetic directly traceable to framework formalism.

**Cons:** Significant restructure. Subscript notation (C₁, C₂, ...) may distance reader through math-register; chapter's strength has been concrete narrative-arithmetic register. May feel like math-textbook in the middle of trade-press / academic-press long-form.

### §4.3 Option 1C (hybrid) analysis — RECOMMENDED

Keep 8-section walkthrough pacing + arithmetic + sum recap. Rename without "Tier N" prefix (h3s become "Direct Health Cost" etc., as 1A). ADD explicit Cᵢ-via-Four-Gates framing in three load-bearing positions:

- **Chapter intro** (post-scope-note paragraph): Brief framing — "This chapter walks each cost component the framework's Four Gates admit — every Cᵢ that passes the discipline of the Commons Inversion Test, units consistency, boundedness, and independence — through one specific extraction."
- **Scope note** (line 13): Replace "through the eight tiers" with "through the framework's full cost-decomposition" or similar.
- **Closing recap** (around "The sum" section): Brief sentence connecting the 8 component sums to the framework's Cᵢ-summation discipline.

The 8 h3 sections remain as illustrative cost-component walkthrough at narrative register; the Cᵢ-via-Four-Gates framing anchors the structure to current architecture without forcing subscript notation through the chapter prose.

**Pros:**
- Preserves chapter's strong worked-example pacing
- Reader-flow narrative-arithmetic register preserved
- Framework-vocabulary alignment achieved at three load-bearing positions
- Tech Appendix audience finds the connection at chapter intro + closing
- Trade-press audience finds the chapter's narrative register intact

**Cons:**
- Slightly more work than 1A (adds ~3 framing paragraphs/sentences)
- Doesn't maximally restructure to subscript-Cᵢ register

### §4.4 Verdict on Decision 1

**1C dominant.** Strong on M3 + M4 + M6 + M8 + M11 + M12. Preserves pedagogical strength while closing vocabulary regression.

---

## §5. Decision 2 — Counterargument-handling approach

### §5.1 Natural-arising-point analysis for the two counterarguments

**Charge 1: "Degrowth in a different vocabulary"**
- Naturally arises in "The brief extrapolation" (line 207-217) where the $10-15T/year global aggregate is asserted. Reader's mind: "Is this degrowth?" Could be addressed at line ~215 as continuation prose.

**Charge 2: "Pulling up the ladder behind already-industrialized nations"**
- Naturally arises in "The brief extrapolation" too — the global figure invites the global-justice question. Or could fold into "What honest pricing does NOT mean" section which already does similar coda work.

### §5.2 Option 2A (full dissolution) analysis — RECOMMENDED

Distribute both counterarguments inline:
- Degrowth rebuttal → fold into "The brief extrapolation" closing paragraphs
- Pulling-up-the-ladder rebuttal → fold into "What honest pricing does NOT mean" (expand from two-misreadings to three-misreadings) OR also into "The brief extrapolation" extension

Remove "Two counterarguments, compressed" h3 section entirely. Closing flow becomes: "The brief extrapolation" → expanded "What honest pricing does NOT mean" (or kept as is if rebuttals fold elsewhere) → "The closing line."

### §5.3 Option 2B (lighter touch) analysis

Remove dedicated h3 wrapper + meta-framing language ("Two objections will meet this chapter on its way to the next, and the book has made implicit promises about honoring them. The first is the charge..." → "...The first charge meets the chapter on its way to the next..."). Keep counterargument substance in adjacent prose without h3.

**Cons:** Leaves the structural pattern (dedicated counterargument-coda) intact. Half-measure.

### §5.4 Option 2C (no restructure) analysis

Accept dedicated section as is. Under-applies discipline.

### §5.5 Verdict on Decision 2

**2A dominant.** Both counterarguments have natural inline arising points; dissolution preserves substance while removing structural pattern violation.

---

## §6. Decision 3 — Abundance-test vocabulary cleanup

### §6.1 References to clean

- **Line 91:** "Tier five is the one the abundance test reveals" — fold into "the cost the Commons Inversion Test surfaces when the underlying community-cohesion commons is imagined absent" or similar (CAI sub-form framing)
- **Line 111:** "the abundance test surfaces it" — replace with "the Commons Inversion Test surfaces it" or similar
- **Line 131:** "The final tier is the one revealed by the abundance test most starkly" — replace + adjust to CIT framing

### §6.2 CIT two-sub-form considerations

Where AIT was a single-form thought experiment, CIT has two sub-forms (CAI + CCI). The Ch 8 references should be reviewed to identify which sub-form is operative for each cost component:

- **Tier 5 (Dynastic Labor)** → likely CAI (imagine community-cohesion commons absent — what dispersal cost surfaces?)
- **Tier 6 (Knowledge and Cultural)** → likely CAI (imagine knowledge-commons absent — what replacement-cost surfaces?)
- **Tier 8 (Temporal Displacement)** → likely CCI (imagine temporal commons not consumed — what foregone-optionality surfaces?)

Light prose adjustment may be warranted to match CIT's sub-form architecture; not all "abundance test" → "CIT" replacements are pure substitutions.

### §6.3 Verdict on Decision 3

**3A (comprehensive sweep) dominant.** Pure substitutions where possible; light prose adjustment where sub-form framing improves clarity.

---

## §7. Decision 4 — Scope-note + chapter-framing

### §7.1 Scope-note completion (line 13)

Current truncation: *"It walks one extraction — one ton of McDowell County coal — through the eight tiers, delivers the intergene[ration..."*

Reasonable completion: *"It walks one extraction — one ton of McDowell County coal — through the framework's full cost-decomposition, delivers the intergenerational pricing gap as a specific number, and gestures at the civilizational-scale implication without attempting to simulate it. Subsequent chapters develop what the simulation would require; this chapter performs the worked example that makes those subsequent simulations meaningful."*

### §7.2 Chapter-framing tier-vocabulary cleanup (line 21)

Current: *"This chapter does that exercise for one ton of Appalachian coal — and lets the reader see what the gap looks like when it isn't aggregated, abstracted, or dissolved in policy language, but priced, tier by tier, against the extraction we've been following from the book's opening."*

Replacement: *"...but priced, cost-component by cost-component, against the extraction we've been following from the book's opening."*

### §7.3 Verdict on Decision 4

**4A dominant.** Scope-note completion + chapter-framing cleanup are both load-bearing for chapter-vocabulary consistency post-restructure.

---

## §8. M1–M11 abbreviated module results

| Module | D1-C + D2-A + D3-A + D4-A performance |
|---|---|
| **M1 CORE math** | PASS — math unchanged; arithmetic preserved; sum recap preserved |
| **M2 Case study** | PASS — McDowell County case-walkthrough preserved |
| **M3 Book content** | **STRONGLY STRENGTHENS** — closes major chapter-level vocabulary regression; aligns with current framework architecture |
| **M3.4 Counterargument coverage** | PRESERVED — degrowth + pulling-up-the-ladder rebuttals retained as inline-woven content |
| **M4 Craft** | STRENGTHENS — chapter pacing preserved; surface vocabulary cleaned |
| **M5 Dinner-table** | STRENGTHENS — "Cᵢ admitted via Four Gates" framing in chapter intro + closing connects to broader framework without forcing math notation through narrative |
| **M6 Academic** | **STRONGLY STRENGTHENS** — academic reviewer sees current-architecture alignment; no AIT/eight-tier retired vocabulary |
| **M7 Originality** | UNCHANGED — chapter's contribution (worked-example walkthrough; $558/ton floor) preserved |
| **M8 Long-term / test-of-time** | **STRONGLY STRENGTHENS** — vocabulary aligned with current ratified framework; chapter ages with the framework rather than carrying retired-vocabulary tracks |
| **M9 Risk** | LOW — restructure scope is contained; arithmetic + load-bearing pedagogy preserved |
| **M10 Publishing** | STRENGTHENS — publisher / literary-agent reader sees current-framework chapter without retired-vocabulary regression |
| **M11 Critic** | STRENGTHENS — academic reviewer surveying chapter for current-framework alignment finds it; counterargument coverage preserved |

**§22 alignment:** D1-C + D2-A + D3-A + D4-A positive on Primary Goals — Publishing Path; Academic Reception; Long-term Impact; Adoption-Bandwidth.

**§22.4 stand-test-of-time alignment:** STRONGLY POSITIVE.

---

## §9. M12 — Intellectual honesty audit

### §9.1 Per-decision M12

**D1-C (hybrid):** Honest about chapter's load-bearing role + framework's current architecture. Preserves narrative-arithmetic register without forcing math-textbook register that would obscure pedagogy. **PASSES.**

**D2-A (full dissolution):** Honors counterargument-handling discipline; preserves substance at natural arising points. **PASSES.**

**D3-A (comprehensive AIT → CIT sweep):** Closes retired-vocabulary regression. Honest about framework's evolution from AIT (2025) to CIT (2026-04-24). **PASSES.**

**D4-A (scope-note + chapter-framing cleanup):** Closes truncation + retired vocabulary in chapter framing positions. **PASSES.**

### §9.2 M12 verdict

**D1-C + D2-A + D3-A + D4-A is M12-optimal.** All four decisions honor framework-evolution honesty + counterargument-handling discipline + chapter-vocabulary consistency.

---

## §10. Cross-chapter precedent

| Chapter | Restructure scope | Outcome | Magnitude vs Ch 8 |
|---|---|---|---|
| Ch 2 | Two dedicated counterargument h3s + 1 retired-vocabulary line | Full restructure | Smaller |
| Ch 4 | Already inline-woven canonical | No restructure | N/A |
| Ch 5 | Inline-but-meta-framed walkthroughs | Lighter touch | Smaller |
| Ch 6 | Four dedicated h3 counterargument sections (~half chapter) | Full multi-commit restructure | Larger (defensive cluster); smaller (tier-vocabulary scope) |
| Ch 7 | Already inline-woven canonical | No restructure | N/A |
| **Ch 8** | **Tier-vocabulary scaffolding (18+ refs) + dedicated counterargument coda + AIT references + scope-note truncation** | **Multi-decision restructure** | Largest cross-chapter sweep target due to tier-vocabulary saturation |

**Verdict on Axis precedent:** Ch 8 is structurally similar to Ch 6 (multi-decision multi-commit restructure) but the scope is different — Ch 6 was about counterargument-handling discipline; Ch 8 is about tier-vocabulary regression + counterargument-handling + scope-note completion. The recommended restructure depth (D1-C + D2-A + D3-A + D4-A) is proportional to the magnitude of issues.

---

## §11. Verdict synthesis + recommendation

### §11.1 Recommended combination

**D1-C + D2-A + D3-A + D4-A.**

- **D1-C:** Hybrid section-organization — drop "Tier N —" prefixes; preserve 8-section walkthrough pacing + arithmetic + sum recap; add Cᵢ-via-Four-Gates framing at chapter intro + scope note + closing
- **D2-A:** Full dissolution of "Two counterarguments, compressed" — distribute degrowth + pulling-up-the-ladder rebuttals to natural arising points (likely "The brief extrapolation" + "What honest pricing does NOT mean")
- **D3-A:** Comprehensive AIT → CIT sweep — replace 3 "abundance test" references; light prose adjustment for CIT two-sub-form architecture where applicable
- **D4-A:** Scope-note completion + chapter-framing tier-vocabulary cleanup

### §11.2 Three rigor questions on Ch 8 restructure

| Question | Verdict |
|---|---|
| **Earns place?** | Substance YES (worked-example pedagogy is load-bearing). Tier-vocabulary scaffolding does NOT earn its place (retired). Counterargument-coda dedicated h3 does NOT earn its place (discipline violation). |
| **Would expansion strengthen?** | NO — current chapter length is appropriate for worked-example pedagogy; expansion would dilute the arithmetic punch. |
| **Would compression strengthen?** | YES — the tier-vocabulary sweep + counterargument-section dissolution compress the chapter's surface-vocabulary surface area without losing substance. |

### §11.3 Implementation phases

**Phase 1 (1 commit):** Decision 4 — scope-note completion + chapter-framing tier-vocabulary cleanup (line 13, 21).

**Phase 2 (1 commit):** Decision 1 — section h3 renames (drop "Tier N —" prefixes); update sum recap; add Cᵢ-via-Four-Gates framing at chapter intro + closing.

**Phase 3 (1 commit):** Decision 3 — comprehensive AIT → CIT sweep; light prose adjustment for sub-form architecture where applicable.

**Phase 4 (1-2 commits):** Decision 2 — distribute counterargument substance to natural arising points; remove "Two counterarguments, compressed" h3 section.

**Phase 5 (1 commit):** Final pass — chapter-end-to-end read; vocabulary regression scan; commit any small follow-on cleanups.

Total: ~5-6 commits / ~2-4 hours of careful prose work.

### §11.4 Rejected alternatives + rationale

| Alternative | Rejected because |
|---|---|
| **D1-A (light rename only)** | Implicit-8-organization remains; chapter doesn't anchor to current Cᵢ-via-Four-Gates framework; M3 + M6 + M8 alignment incomplete |
| **D1-B (full Cᵢ-indexed reframing)** | Subscript notation register may distance reader; chapter pedagogical strength is narrative-arithmetic, not math-textbook |
| **D2-B (lighter touch)** | Leaves dedicated counterargument-coda h3 wrapper; structural pattern violation persists |
| **D2-C (no restructure)** | Under-applies discipline; defensive register at chapter close |
| **D3-B (light AIT → CIT only)** | Doesn't address sub-form architecture mismatch; potential for prose/concept inconsistency |
| **D4-B (scope-note only)** | Leaves "tier by tier" prose intact; chapter-framing vocabulary regression persists |

---

## §12. Author-ratified resolutions

**[PENDING — author ratification 2026-04-27.]**

Once ratified:
- Apply D1-C + D2-A + D3-A + D4-A in 5-6 sequential commits per Phase 1-5 plan
- Mark Track B Ch 8 sweep complete (cross-chapter sweep todo)
- Cross-reference this rigor pass from terms_index entries that reference Ch 8 (none currently; eventual updates may add cross-references when terms_index Phase 2 restructure reaches sub-instrument terms)

---

## §13. Rerun gate

Rerun if:
- D1-C "Cᵢ via Four Gates" framing in chapter intro tested and reads as math-jargon distancing readers; would push toward D1-A (lighter rename + plain-prose framing).
- D2-A distribution of counterarguments surfaces that natural arising points produce awkward chapter-flow; would push toward D2-B.
- D3-A AIT → CIT sweep surfaces that the chapter requires substantial prose-rewrite beyond simple substitution; might push toward Ch 8 scope-expansion as separate restructure scope.
- Future Ch 8 holistic review (per Insight #22 sweep discipline) reconsiders chapter scope or pedagogy.

---

*End of focused rigor pass v1.0.0 on Ch 8 ("What Things Actually Cost") restructure. D1-C + D2-A + D3-A + D4-A recommended (hybrid section-organization + full counterargument-section dissolution + comprehensive AIT → CIT sweep + scope-note completion). All 12 modules examined; decision dominated by M3 + M6 + M8 + M12 finding that tier-vocabulary regression + counterargument-discipline violation require multi-decision restructure proportional to the magnitude of issues. Pending author ratification.*
