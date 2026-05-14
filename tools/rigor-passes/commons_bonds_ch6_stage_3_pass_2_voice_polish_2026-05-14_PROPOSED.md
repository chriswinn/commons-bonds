# Stage-3 Rigor Pass — Chapter 6 (Three Ways of Counting) — Pass 2: Voice-polish [PROPOSED]

**Date:** 2026-05-14
**Workstream:** #20 Manuscript Stage-3 Rigor Pass — Phase B — Ch 6 — Pass 2 (voice-polish)
**Chapter:** 6 — *Three Ways of Counting*
**File audited:** [Chapter__6_ThreeWaysofCounting__Draft.md](manuscript/chapters/Chapter__6_ThreeWaysofCounting__Draft.md) — **332 lines** (post-Phase-C-α + post-Phase-C-β state verified 2026-05-14 against origin/main `a6a531b`; chapter unchanged across origin/main `d2ee178` → `a6a531b` interval — the intervening commits touched the Tech Appendix + Ch 5 Pass 3 doc only)
**Status:** **PROPOSED — awaits author ratification. Phase C-γ applies after ratification, paralleling Ch 5 Pass 2 commit `dd3c684` → Phase C-β commit `c35cb03`.**
**Mode:** Audit-existing-prose (post-Phase-C-α + post-Phase-C-β chapter is the baseline; v2.0 Amendment B voice-polish as a distinct pass from Pass 1 fact-check and Pass 3 audience-load).
**Pass scope:** Pass 2 (Voice-polish) only. Pass 1 ratified + Phase C-α applied (commit `6a5ee42`) + Phase C-β applied (commit `f6bb6ad`); Pass 3 (Audience-load) deferred per per-pass serial cadence.
**Hard constraint observed:** No fixes applied to chapter file. Phase C-γ (post-ratification) applies recommended edits.
**Branch:** `claude/ch6-pass-2-voice-polish-sharp-mestorf-583d31` (off origin/main `a6a531b`).

---

## §0. Why this pass matters now

Ch 6 ships in the Sandy Darity send packet (Ch 5 + Ch 6 + Tech Appendix) post-2026-05-13 interview. Sandy is a labor economist who will read the apparatus chapter carefully — Ch 6 is the forward-direction-canonical home for the **four gates** and the **three ways of counting** (outer + inner), and Sandy explicitly named the SI-1 framing of the M1/M2/M3 triangulation as his "deepest single-line case for the framework's measurement work." The new ~1,050-word walkthrough sub-section that Phase C-α introduced is therefore the chapter's most-exposed Register-2 prose and the first surface Sandy will inspect.

Pass 1 + Phase C-α + Phase C-β resolved the chapter's gating fact-check + math-check items: MUST-FIX-1 outer/inner-three disambiguation (Phase C-α applied the M1/M2/M3 walkthrough sub-section at lines 122–132); MUST-FIX-2 Ch 5 cross-chapter sync; SHOULD-FIX-8/9 + MEDIUM-12 Amendment E items (convergence-table caption rebuild + cross-case settlement-figure verification; commit `f6bb6ad`); LOW-5 SCC first-use spell-out; the cascade of TA cross-reference hyperlinks at lines 99, 126, 128, 130, 132, 146, 154, 274, 286, 326. Phase-C-α + Phase-C-β cumulatively introduced five new prose surfaces (M1/M2/M3 walkthrough + convergence-table caption rebuild + MI-3 Ostrom break-point + Sen capabilities defense + Darity longevity-gap lineage at line 25 + DAC net-removal parenthetical at line 47) that have not had a coordinated voice-polish pass. Pass 2 audits the full chapter for voice-polish issues with priority focus on those five new surfaces, plus the pre-existing chapter prose that has not been polished since Phase A audits landed.

This pass produces the spot-fix recommendations Phase C-γ will apply verbatim before the Sandy send.

---

## §1. Source artifacts read

1. [`tools/drafting-templates/stage-3-three-pass-rigor-audit.md`](tools/drafting-templates/stage-3-three-pass-rigor-audit.md) §"Pass 2: Voice-polish" — canonical scaffold for this pass.
2. Memory: [`feedback_voice_polish_pipeline.md`](/Users/c17n/.claude/projects/-Users-c17n-commons-bonds/memory/feedback_voice_polish_pipeline.md) (dump → sift → polish; polish actively for grammar/flow; don't preserve raw author voice).
3. Memory: [`feedback_dual_audience_test.md`](/Users/c17n/.claude/projects/-Users-c17n-commons-bonds/memory/feedback_dual_audience_test.md) (every rewrite tested against layman + specialist; "shorter = better" is wrong; substance drives length).
4. Memory: [`feedback_substance_drives_length.md`](/Users/c17n/.claude/projects/-Users-c17n-commons-bonds/memory/feedback_substance_drives_length.md) (no arbitrary word-count targets).
5. Memory: [`feedback_audience_aware_drafting_discipline.md`](/Users/c17n/.claude/projects/-Users-c17n-commons-bonds/memory/feedback_audience_aware_drafting_discipline.md) (v2.0 Amendment B — distinct passes).
6. Memory: [`feedback_grammatical_role_cross_references.md`](/Users/c17n/.claude/projects/-Users-c17n-commons-bonds/memory/feedback_grammatical_role_cross_references.md) (chapter→appendix cross-reference discipline).
7. Memory: [`reference_sandel_hybrid_pattern.md`](/Users/c17n/.claude/projects/-Users-c17n-commons-bonds/memory/reference_sandel_hybrid_pattern.md) (acronym treatment per context).
8. [`manuscript/chapters/Chapter__6_ThreeWaysofCounting__Draft.md`](manuscript/chapters/Chapter__6_ThreeWaysofCounting__Draft.md) — 332 lines, post-Phase-C-α + post-Phase-C-β state.
9. [`tools/rigor-passes/commons_bonds_ch6_stage_3_pass_1_fact_check_2026-05-13_PROPOSED.md`](tools/rigor-passes/commons_bonds_ch6_stage_3_pass_1_fact_check_2026-05-13_PROPOSED.md) — Pass 1 + Amendments B through E + Phase C-α/Phase C-β status.
10. [`tools/rigor-passes/commons_bonds_ch5_stage_3_pass_2_voice_polish_2026-05-14_PROPOSED.md`](tools/rigor-passes/commons_bonds_ch5_stage_3_pass_2_voice_polish_2026-05-14_PROPOSED.md) — Ch 5 Pass 2 structural reference (template + cadence).

---

## §2. Pass-2 scope reminder

Pass 2 audits prose for the LLM tics + voice issues trade-press editors flag, plus the audit-existing-prose mode's consistency-check addendum. The named-inventory categories applied below:

- **Rule of three / declarative-three-in-a-row** — A. B. C. constructions; flag if pattern-dense.
- **Em-dash crutches** — em-dashes used as connective tissue rather than as deliberate parenthetical extension or punch.
- **Tidy parallels** — He did X. She did Y. They did Z. structures; anaphoric repetition that becomes visible cadence.
- **Hedge phrases** — "I will argue that…" / "Perhaps…" / "It seems likely that…"
- **Connective-tissue clichés** — "in short" / "ultimately" / "moreover" / "furthermore" / "that being said"
- **Meta-commentary** — "That is the whole sentence." / "Let me explain…"
- **Expository flatness** — "The plain definition is this:" / "Here is what I think:" / "The discipline this surfaces:"
- **Cadence repetition** — "It changed me. It humbled me. It made…" patterns; chiastic emotional-symmetry codas.
- **Apparatus residue** — Greek letters, equation-variable shorthand (B, CS, RCV), formula-shorthand acronyms appearing in body prose where the chapter's register prohibits or is inconsistent.
- **Consistency check (audit-existing-prose mode)** — does the prose align with the chapter's own argument and term-usage? Surfaces logic-inversions, gate-name shifts, and conceptual-coherence breaks the Phase-C-α + Phase-C-β prose may have introduced.
- **Closely-repeated phrasing** — same content-word or phrase appearing two-or-more times within a small window where one usage is rhetorical and the rest are redundancy.
- **Grammatical-role discipline for cross-references** — per `feedback_grammatical_role_cross_references.md`: sections-as-nouns named only; sections-as-citations name + § + hyperlink (HTML/markdown); theorems/definitions compound identifier.
- **Heavy hyphenated compounds** — multi-hyphen compound noun phrases that read as apparatus-dense rather than as natural English.

Ch 6's specific emphasis per the task brief: (a) the new ~1,050w M1/M2/M3 walkthrough sub-section (lines 122–132); (b) the convergence-table caption + source-attribution prose (lines 168–172); (c) the MI-3 Ostrom heterogeneous-stakeholder break-point + stratification economics inline tie (line 256); (d) the Sen capabilities defense paragraph (line 244); (e) the Darity longevity-gap lineage paragraph (line 25); (f) the DAC cost passage with Climeworks net-removal clarification (line 47).

---

## §3. Summary verdict

| Severity | Count | Disposition |
|---|---|---|
| **MUST-FIX** | 3 | Sandy-send-gating; one grammar error + one gate-name internal inconsistency + one political-flag register issue the task brief explicitly flagged |
| **SHOULD-FIX** | 5 | High-priority pre-send; covers the SI-1 opener tightening + four phrase-repetition / structural items |
| **MEDIUM** | 8 | Precision-tightening; recommended pre-send but author-discretion |
| **LOW** | 7 | Substantively-earned cadence patterns / chapter-pattern apparatus uses; hold-as-is default |

**Total findings:** 23.

**Aggregate verdict:** **READY AFTER PHASE C-γ SPOT-FIXES.** The chapter's apparatus-and-analytical register is fundamentally strong; the SI-1 framing in the M1/M2/M3 walkthrough opener lands cleanly; the convergence-table presentation is structurally sound; the philosophical-grounding paragraphs (Parfit + Sen + Ostrom-extension + Darity) are intellectually honest and lineage-attributive. The three MUST-FIX findings are all isolated catch-on-first-read items (one typo; one gate-name term-shift between two paragraphs 6 lines apart; one political-flag framing in the Sen-defense paragraph). The SHOULD-FIX set absorbs the SI-1 opener redundancy and four phrase-repetition / structural items across the new Phase-C surfaces. No structural voice revision needed.

---

## §4. Findings — MUST-FIX (Sandy-send gating)

Issues any careful reader catches on first pass; grammar errors, internal term-inconsistencies, or register-shifts that a fact-checker / Sandy / a trade-press editor would all flag immediately.

### F-V1 — Plural-noun typo: "commons categorys" [MUST-FIX]

**Location:** [Chapter__6_ThreeWaysofCounting__Draft.md:282](manuscript/chapters/Chapter__6_ThreeWaysofCounting__Draft.md:282)

**Chapter text:**
> "If two candidates overlap, the framework resolves the overlap by redefining one of them, merging the two into a single broader term, or rejecting the redundant candidate. This is the same discipline the book has applied to **the commons categorys,** now operating at the cost-term level rather than the dimension level."

**Why this flags.** *"Commons categorys"* is a plural-noun typo. Standard English requires *"commons categories"*. The error is glaring on read; a fact-checker / copyeditor / trade-press editor / Sandy Darity will all spot it on first pass. The sentence sits inside the four-gates apparatus core (Gate Four: Independence), one of the chapter's most-attentively-read passages for any technical reader.

**Severity rationale.** (a) Plural-noun typo of the type any reader catches; (b) sits inside the chapter's apparatus core (Gate Four definition); (c) one-character fix.

**Recommended rewrite (apply verbatim at Phase C-γ):**
> "If two candidates overlap, the framework resolves the overlap by redefining one of them, merging the two into a single broader term, or rejecting the redundant candidate. This is the same discipline the book has applied to the commons categories, now operating at the cost-term level rather than the dimension level."

(Single-character fix: *"categorys"* → *"categories"*.)

---

### F-V2 — Gate-name internal inconsistency: "dimensional consistency" (line 278) vs "Units Consistency" (line 284) [MUST-FIX]

**Location:** [Chapter__6_ThreeWaysofCounting__Draft.md:278](manuscript/chapters/Chapter__6_ThreeWaysofCounting__Draft.md:278) + [Chapter__6_ThreeWaysofCounting__Draft.md:284](manuscript/chapters/Chapter__6_ThreeWaysofCounting__Draft.md:284)

**Chapter text (line 278):**
> "**The second gate is dimensional consistency.** A candidate must be expressible as dollars per unit of resource per unit of time."

**Chapter text (line 284, six lines later):**
> "A cost claim that passes both Commons-Absence and Commons-Consumption Inversion has demonstrated that it is grounded in consumption of a finite commons; it has not yet demonstrated that its units are consistent (a claim mixing monetary, physical, and qualitative units **fails Units Consistency**); that its bounds are finite (a claim of 'infinite' cost dominates any aggregation); or that it does not double-count across overlapping commons categories…"

**Why this flags.** Line 278 names the gate *"dimensional consistency"* (lower-case). Line 284 names the same gate's failure-state *"Units Consistency"* (title-case, different noun). The internal inconsistency reads as either a slip or a different-source ambiguity; Sandy Darity reads paragraph-by-paragraph and the term-shift within the four-gates apparatus core will register. The chapter's apparatus-discipline depends on consistent gate-naming because the four gates are the most-named flagship apparatus pieces in the chapter (each referenced repeatedly across Ch 6 + Ch 5 + Tech Appendix). Treating the same gate as *"dimensional consistency"* in one paragraph and *"Units Consistency"* in another erodes the apparatus-naming precision more than the same error elsewhere would.

The Pass 1 audit (PROPOSED doc §"Critical positive findings") noted *"Four-gate term-by-term variable definitions (line 103–106) match TA §7 + §17 ✓"* but did not catch this within-gate-section term-shift, which surfaced only on a careful Pass-2 re-read.

**Severity rationale.** (a) Internal inconsistency between two paragraphs six lines apart, both inside the chapter's apparatus core; (b) Sandy Darity will read the four-gates section carefully and notice; (c) trivial fix; (d) the chapter's apparatus-naming discipline is otherwise consistent — this is an isolated catch.

**Recommended rewrite (apply verbatim at Phase C-γ):**

Author selects one. Both options align the two references; the choice is which term to canonicalize.

- **Option A — line 284 conforms to line 278 (RECOMMENDED).** Replace *"fails Units Consistency"* with *"fails dimensional consistency"*. Line 278's lower-case form is the gate's introductory naming; line 284 should match.

  Replace:
  > "a claim mixing monetary, physical, and qualitative units fails Units Consistency"

  with:
  > "a claim mixing monetary, physical, and qualitative units fails dimensional consistency"

- **Option B — line 278 conforms to line 284.** Replace *"dimensional consistency"* (line 278) with *"Units Consistency"* (title-case). Defensible if the Technical Appendix § 7 canonical form is title-case *"Units Consistency"* — but the Pass 1 §"Critical positive findings" verification confirmed line 103–106 four-gate variable definitions match TA §7 + §17 against the lower-case *"dimensional consistency"* introductory form, so Option A is the lower-disruption fix.

**Cross-pass flag.** Verify against TA §7 + §17 canonical-form text at Phase C-γ application time. If TA canonical form is *"Units Consistency"* (title-case), Phase C-γ should apply Option B instead; if TA canonical form is *"dimensional consistency"* (lower-case), Option A as recommended.

---

### F-V3 — "Right-wing critics" framing in Sen capabilities defense reads as political-flag, not analytical-engagement [MUST-FIX]

**Location:** [Chapter__6_ThreeWaysofCounting__Draft.md:244](manuscript/chapters/Chapter__6_ThreeWaysofCounting__Draft.md:244)

**Chapter text (post-Phase-C-α, Sen capabilities defense paragraph):**
> "A second philosophical grounding the framework operates within — complementary to Parfit's impersonal-outcomes evaluation — is Amartya Sen's capability-and-social-welfare-function framework. Where Parfit answers the question of *whether* future generations have moral standing, Sen answers the question of *how* their standing should be valued: in terms of the capabilities the framework's accounting can preserve or extinguish. The framework's Residual Commons Value calculation is, in Sen's vocabulary, a measurement of the capability set extraction forecloses on whoever-the-future-people-turn-out-to-be. **Right-wing critics who ask 'why give value to future generations?'** are asking a Parfit-domain question; the framework's answer is *because they will have capabilities that present extraction will or will not constrain*, and Sen's framework names the capabilities and the valuation methodology that grounds the framework's pricing. The pairing — Parfit grounding the standing, Sen grounding the valuation — is what makes the framework's intergenerational-pricing claim defensible across the moral-philosophy and welfare-economics traditions simultaneously rather than within only one."

**Why this flags.** The task brief explicitly named this surface as a Pass-2 priority: *"verify the 'right-wing critics' framing lands as analytical-engagement rather than political-flag (this is methodological-defense register, not partisan)."* The actual question — *"why give value to future generations?"* — is one that has been raised across multiple political and philosophical registers: libertarian-economic (fiscal-conservative discount-rate arguments), Parfit-tradition non-identity skepticism, person-affecting moral-philosophy critiques, even some progressive intergenerational-equity critiques (e.g., arguments that future-generation pricing displaces present-poverty pricing). Tagging the question as exclusively "right-wing" narrows the audience-relevant framing to a partisan target rather than to the analytical-question-class the paragraph actually addresses.

Per the dual-audience test: a left-leaning specialist reads "right-wing critics" as analytical-engagement-with-an-acknowledged-political-target; a right-leaning specialist reads it as political-flagging; a trade-press editor (Sandel-tradition / Mazzucato-tradition / Pistor-tradition trade-comp shelf) consistently engages with the *question* rather than tagging the *questioner* by political-coalition. The paragraph's methodological-defense register would land more cleanly if the question were addressed on its analytical merits without the political-coalition tag.

**Severity rationale.** (a) Task brief explicitly named this as a Pass-2 priority surface; (b) the political-coalition tag is gratuitous to the analytical work the paragraph does — the rest of the paragraph (Parfit-domain vs Sen-domain mapping; the framework's pricing-via-capabilities answer) operates entirely at the methodological level; (c) Sandy Darity is methodologically-engaged across political registers — he engages reparations-economics arguments (a left-coded methodology) and labor-economics arguments (a methodology that crosses left-right lines) with equal analytical rigor, and would read "right-wing critics" framing as either non-substantive or as the chapter's analytical voice slipping; (d) any reader downstream of Sandy (Berggruen Prize judge / academic reviewer / trade-press editor) will register the political-coalition tag as register-break in a chapter whose other framing-paragraphs are politically-neutral.

**Recommended rewrite (apply verbatim at Phase C-γ):**

Author selects one. The recommended choice: **Option A** (drop the political tag entirely; preserve the analytical move).

- **Option A — drop the political tag (RECOMMENDED).** Replace:
  > "Right-wing critics who ask 'why give value to future generations?' are asking a Parfit-domain question"

  with:
  > "Critics who ask 'why give value to future generations?' are asking a Parfit-domain question"

  (Single-word cut: *"Right-wing"*. Preserves the rest of the sentence verbatim; the Parfit-domain / Sen-domain rhetorical move is intact; the question still gets answered through Sen's capabilities framework.)

- **Option B — replace with analytical-register naming.** Replace:
  > "Right-wing critics who ask 'why give value to future generations?' are asking a Parfit-domain question"

  with:
  > "Skeptics of intergenerational pricing who ask 'why give value to future generations?' are asking a Parfit-domain question"

  (Two-word swap: *"Right-wing critics"* → *"Skeptics of intergenerational pricing"*. Slightly longer but explicitly names the analytical position the question raises rather than the political coalition it might come from.)

- **Option C — explicit acknowledgment of cross-register critics.** Replace:
  > "Right-wing critics who ask 'why give value to future generations?' are asking a Parfit-domain question"

  with:
  > "Critics across political registers who ask 'why give value to future generations?' are asking a Parfit-domain question"

  (Phrase-level swap: *"Right-wing critics"* → *"Critics across political registers"*. Names the cross-coalition reality of the question explicitly. Slightly heavier than Option A's minimum-cut but most explicit about the analytical-question-class.)

**Cross-pass flag.** None. This is a register-only edit; no factual claim moves; the philosophical-grounding lineage (Parfit + Sen) is preserved verbatim.

---

## §5. Findings — SHOULD-FIX (high-priority pre-send)

Issues any careful copyedit pass catches; high-priority for Sandy send but not on the same gating level as the MUST-FIX set.

### F-V4 — M1/M2/M3 walkthrough opener: redundant adjacent sentences on DCF-as-mechanism (SI-1 paragraph) [SHOULD-FIX]

**Location:** [Chapter__6_ThreeWaysofCounting__Draft.md:124](manuscript/chapters/Chapter__6_ThreeWaysofCounting__Draft.md:124) (the ~258w opener paragraph of the M1/M2/M3 walkthrough sub-section)

**Chapter text (post-Phase-C-α, SI-1 paragraph):**
> "Inside the residual commons value computation, a triangulation operates that the formula above does not display on its face. The RCV estimate is not produced by a single estimation method; it is produced by three. The reason has to do with an institutional asymmetry financial economics is well-positioned to recognize. **Markets do have a mechanism for pricing future profitability — discounted-cash-flow analysis aggregated through equity and debt markets, which produces asset prices that implicitly price expected future returns. Every financial-asset price embeds an expectation about future returns; the mechanism is implicit but real.** Markets do not have an equivalent mechanism for pricing future harms. No aggregating institution produces a comparable price signal for the externality tail, for foreclosure cost, or for the long-tail damage of cost severance. **The three estimation methods — Replacement Cost, Revealed Preference, Scarcity-Adjusted Option Value — are the framework's substitute for the missing market mechanism on the harms side.** They give the harm side a comparable price signal to the one the asset side already has, so that the asymmetry between priced future profitability and unpriced future harms is no longer the institutional default. Each method anchors its estimate in a different empirical pathway; the convergence range across the three is what the framework reports as the RCV estimate. The triangulation is the work that gives the RCV claim its standing."

**Why this flags.** Two adjacent sentences (sentences 4 + 5 in the paragraph) substantively repeat: *"…discounted-cash-flow analysis aggregated through equity and debt markets, which produces asset prices that implicitly price expected future returns. Every financial-asset price embeds an expectation about future returns; the mechanism is implicit but real."* The first sentence's relative clause (*"which produces asset prices that implicitly price expected future returns"*) and the second sentence's main clause (*"Every financial-asset price embeds an expectation about future returns"*) make the same claim — that asset prices encode expected-returns expectations — in two consecutive sentences. The redundancy is visible on read.

The task brief named this paragraph as the highest-priority Pass-2 surface: *"scrutinize whether the opener paragraph (SI-1 framing) can absorb a 20-30% trim without losing Sandy's exact framing."* The SI-1 framing is the trio of bolded sentences above (markets-do-have / markets-do-not-have / three-methods-as-substitute). Those three sentences are Sandy-named "cleanest single-line case" and **must survive polishing verbatim**. The trim is achievable by consolidating the adjacent-sentence DCF redundancy plus light tightening of two other phrases — without touching the three SI-1 sentences.

**Severity rationale.** (a) Adjacent-sentence redundancy is visible on a careful read; (b) the SI-1 paragraph is Sandy's first-inspection surface for the framework's measurement work; (c) the redundancy fix is verbatim-clean and preserves the SI-1 framing intact; (d) opportunity to apply the task brief's 20-30% trim target through redundancy-collapse rather than through SI-1 sentence-touching.

**Recommended rewrite (apply verbatim at Phase C-γ):**

Author selects one approach. Recommended: **Option A** (consolidate the DCF redundancy; preserve SI-1 verbatim; ~10% trim).

- **Option A — consolidate the DCF-mechanism redundancy (RECOMMENDED).** Replace:
  > "Markets do have a mechanism for pricing future profitability — discounted-cash-flow analysis aggregated through equity and debt markets, which produces asset prices that implicitly price expected future returns. Every financial-asset price embeds an expectation about future returns; the mechanism is implicit but real."

  with:
  > "Markets do have a mechanism for pricing future profitability — discounted-cash-flow analysis aggregated through equity and debt markets, embedded in every asset price as an implicit expectation about future returns. The mechanism is implicit but real."

  Drops the redundancy between sentences 4 + 5 by folding the *"every asset price embeds…"* claim into the DCF sentence. Preserves *"the mechanism is implicit but real"* as the standalone close. Net: 258w → 238w (~8% trim). SI-1 framing untouched.

- **Option B — slightly deeper trim, including the opening framing.** Replace the opening two sentences:
  > "Inside the residual commons value computation, a triangulation operates that the formula above does not display on its face. The RCV estimate is not produced by a single estimation method; it is produced by three. The reason has to do with an institutional asymmetry financial economics is well-positioned to recognize."

  with:
  > "Inside the RCV computation, a triangulation operates that the formula does not display on its face. The RCV estimate is not produced by a single method; it is produced by three. The reason is an institutional asymmetry financial economics is well-positioned to recognize."

  AND apply Option A's DCF consolidation. Net: 258w → ~225w (~13% trim). Uses *"RCV"* in the opener (Sandel hybrid: dense intra-chapter use after RCV is established at lines 97–118); drops *"has to do with"* (weak verb construction). SI-1 framing untouched.

- **Option C — hold the redundancy as deliberate emphasis.** Defensible if author reads the *"every financial-asset price embeds an expectation; the mechanism is implicit but real"* sentence as substantive separate work (asserting the mechanism's universality across all asset prices, beyond what the first sentence's DCF-walkthrough claim covers). Hold-as-is.

**Cross-pass flag.** SI-1 three-sentence framing (markets-do-have / markets-do-not-have / three-methods-as-substitute) is preserved verbatim in Options A + B. Sandy's "deepest single-line case" framing is hard-preserved. The 20-30% trim target in the task brief is partial under Option A (~8%) or partial under Option B (~13%); deeper trims would require touching the SI-1 sentences themselves, which the task brief hard-prohibits, or trimming the closing-trio sentences (each method anchors / convergence range / triangulation is the work), which the M1/M2/M3 walkthrough's substantive setup needs.

---

### F-V5 — "They answer different questions" verbatim phrase-repeat across lines 45 + 49 [SHOULD-FIX]

**Location:** [Chapter__6_ThreeWaysofCounting__Draft.md:45](manuscript/chapters/Chapter__6_ThreeWaysofCounting__Draft.md:45) + [Chapter__6_ThreeWaysofCounting__Draft.md:49](manuscript/chapters/Chapter__6_ThreeWaysofCounting__Draft.md:49)

**Chapter text (line 45):**
> "One distinction worth making explicit at this point in the carbon accounting. The bottom-up damage-accounting we have been doing prices what carbon *does* once emitted — the damage side, anchored by the Social Cost of Carbon. The framework's forward-looking residual commons value apparatus (Approach 3, below) also asks a different question — what would it cost to engineer the substitute the commons was providing? — and the answer for atmospheric CO₂ comes from direct-air-capture. **Both numbers belong in honest carbon accounting; they answer different questions.**"

**Chapter text (line 49, two paragraphs and one prose-block later):**
> "One distinction matters here. The Social Cost of Carbon — the figure of approximately one hundred ninety dollars per ton at a two percent discount rate, drawn from Rennert and colleagues 2022 — prices the *damage* that a ton of CO₂ does once emitted. Direct-air-capture prices the *engineering reversal* of that damage. **The two numbers appear together when the convergence table compares approaches, but they answer different questions.** The substitution-side question (what does it cost to replace the commons function) belongs in Approach 3's RCV Method 1; the damage-side question (what does the harm cost) is what Approach 1's bottom-up walkthrough has been answering. Conflating them is one of the easier methodological errors a reader could make, and the framework's reporting discipline keeps them separated so the reader doesn't."

**Why this flags.** The phrase *"they answer different questions"* appears at the end of line 45 AND at line 49 — verbatim repeat within the same conceptual paragraph-cluster. Both lines make the same conceptual move (damage-side SCC vs substitution-side DAC; conflation warning). Line 45 introduces the distinction in a one-paragraph compressed form; line 49 restates the distinction in a more-formal four-sentence form with the Rennert 2022 citation + the M1/M2/M3 cross-reference (Approach-3-Method-1 vs Approach-1) at the close. The two paragraphs perform substantively-double work.

Phase C-α applied both passages as part of the M1/M2/M3 disambiguation work (Pass 1 MUST-FIX-1 cascade). The redundancy is a Phase-C-α-artifact: the chapter introduces the damage-side/substitution-side distinction once at line 45 (briefly) and then again at line 49 (formally with Rennert anchor). Pass 2 catches the verbatim-phrase residue.

**Severity rationale.** (a) Verbatim phrase-repeat across two paragraphs separated by the DAC cost passage; (b) the substantive double-work is also visible on careful read — Sandy Darity will register the conceptual repetition; (c) low-risk consolidation either way.

**Recommended rewrite (apply verbatim at Phase C-γ):**

Author selects one. Recommended: **Option A** (consolidate line 49; preserve line 45 as the brief introduction).

- **Option A — drop line 49's verbatim-phrase close; preserve the Rennert-anchor sentence + the M1/M2/M3 cross-reference (RECOMMENDED).** Replace, at line 49:
  > "One distinction matters here. The Social Cost of Carbon — the figure of approximately one hundred ninety dollars per ton at a two percent discount rate, drawn from Rennert and colleagues 2022 — prices the *damage* that a ton of CO₂ does once emitted. Direct-air-capture prices the *engineering reversal* of that damage. The two numbers appear together when the convergence table compares approaches, but they answer different questions. The substitution-side question (what does it cost to replace the commons function) belongs in Approach 3's RCV Method 1; the damage-side question (what does the harm cost) is what Approach 1's bottom-up walkthrough has been answering. Conflating them is one of the easier methodological errors a reader could make, and the framework's reporting discipline keeps them separated so the reader doesn't."

  with:
  > "The Social Cost of Carbon — the figure of approximately one hundred ninety dollars per ton at a two percent discount rate, drawn from Rennert and colleagues 2022 — prices the *damage* that a ton of CO₂ does once emitted; direct-air-capture prices the *engineering reversal* of that damage. The substitution-side question (what does it cost to replace the commons function) belongs in Approach 3's RCV Method 1; the damage-side question (what does the harm cost) is what Approach 1's bottom-up walkthrough has been answering. Conflating them is one of the easier methodological errors a reader could make, and the framework's reporting discipline keeps them separated so the reader doesn't."

  Drops the *"One distinction matters here"* opener (expository-flatness register; line 45 already introduced the distinction); semicolon-merges the SCC + DAC sentences (parallel structure earned by the *"damage" vs "engineering reversal"* contrast); drops the *"they answer different questions"* sentence (verbatim repeat from line 45). Preserves the Rennert 2022 citation + the M1/M2/M3 cross-reference + the conflation-warning close. Net: ~95w → ~85w (~11% trim of line 49 paragraph).

- **Option B — consolidate line 45 instead; preserve line 49 as the formal version.** Replace, at line 45:
  > "One distinction worth making explicit at this point in the carbon accounting. The bottom-up damage-accounting we have been doing prices what carbon *does* once emitted — the damage side, anchored by the Social Cost of Carbon. The framework's forward-looking residual commons value apparatus (Approach 3, below) also asks a different question — what would it cost to engineer the substitute the commons was providing? — and the answer for atmospheric CO₂ comes from direct-air-capture. Both numbers belong in honest carbon accounting; they answer different questions."

  with:
  > "One distinction is worth making explicit at this point. The bottom-up damage-accounting prices what carbon *does* once emitted — the damage side, anchored by the Social Cost of Carbon. The framework's forward-looking residual commons value apparatus (Approach 3, below) also asks what it would cost to engineer the substitute, and the answer for atmospheric CO₂ comes from direct-air-capture. The formal distinction is set out below."

  Trims line 45 to a brief forward-pointer; preserves line 49 as the formal canonical distinction-statement. Heavier touch; less recommended because the brief-introduction-first pattern is the chapter's discipline elsewhere.

**Cross-pass flag.** No numerical or citation changes. The Rennert 2022 anchor remains; the SCC = ~$190/ton at 2% discount remains; the Approach-3-Method-1 + Approach-1 cross-references remain. The substantive damage-side / substitution-side distinction is preserved with single-source ownership rather than dual-source.

---

### F-V6 — Climeworks net-removal parenthetical placement breaks DAC-pricing-trajectory sentence flow (Surface 6) [SHOULD-FIX]

**Location:** [Chapter__6_ThreeWaysofCounting__Draft.md:47](manuscript/chapters/Chapter__6_ThreeWaysofCounting__Draft.md:47) (the Climeworks Mammoth + Generation-3 sentence within the DAC cost passage)

**Chapter text (post-Phase-C-β, with the SHOULD-FIX-9 net-removal clarification embedded):**
> "Climeworks's Orca facility in Iceland, currently among the largest operational direct-air-capture installations, captures CO₂ at approximately one thousand dollars or more per ton at first-of-a-kind operational scale. **Climeworks's Mammoth facility (operational from 2024) and the company's Generation-3 technology trajectory project unit cost reductions toward four hundred to six hundred dollars per ton net-removal cost by 2030 — the capture-only target is two hundred fifty to three hundred fifty dollars per ton — under the corporate cost-reduction trajectory the company disclosed at its June 2024 Carbon Removal Summit in Zurich.** Carbon Engineering's Stratos facility in Texas, in commissioning at the time of writing with phased ramp to full capacity through mid-2026, is projected to capture at three hundred to six hundred dollars per ton at full operation. The International Energy Agency's *Direct Air Capture 2022* review places the achievable cost at scaled-up operation in the two-hundred-thirty to six-hundred-dollar range, depending on energy-source assumptions. The IPCC's AR6 Working Group III, under more optimistic learning-curve and policy-support scenarios, projects mid-century costs as low as one hundred to three hundred dollars per ton. The book presents all four horizons because the answer depends on which one the reader is asking about, and the framework's response to the question 'what does it cost to replace what's been severed' is honestly horizon-dependent."

**Why this flags.** The task brief named this surface as a Pass-2 priority: *"the parenthetical 'the capture-only target is two hundred fifty to three hundred fifty dollars per ton' reads slightly intrusive in the current prose flow. Consider whether to reformat as a separate sentence or move the capture-only-vs-net-removal distinction to a footnote."*

The Climeworks Mammoth sentence carries five distinct pieces of substantive content packed into one sentence:
1. *"Climeworks's Mammoth facility (operational from 2024)"* — the facility-name + commissioning anchor
2. *"and the company's Generation-3 technology trajectory"* — the technology-trajectory anchor
3. *"project unit cost reductions toward four hundred to six hundred dollars per ton net-removal cost by 2030"* — the net-removal cost target
4. *"— the capture-only target is two hundred fifty to three hundred fifty dollars per ton —"* — the capture-only sub-target (Phase-C-β embedded clarification)
5. *"under the corporate cost-reduction trajectory the company disclosed at its June 2024 Carbon Removal Summit in Zurich"* — the source-citation anchor

The em-dash-bracketed appositive (item 4) breaks reader-flow between the primary cost target (item 3) and its source-citation anchor (item 5). A layman reader hits a different cost figure inside the appositive before reaching the source-citation that anchors the primary figure; a specialist reader reads the appositive as substantive technical clarification but registers the structural roughness of the placement. Per the dual-audience test, the parenthetical placement is sub-optimal for both audiences.

**Severity rationale.** (a) Task brief explicitly named this as a Pass-2 priority surface; (b) the embedded parenthetical breaks the sentence's primary substance-flow; (c) low-risk reformatting either way; (d) the net-removal vs capture-only distinction is substantively load-bearing (Phase-C-β added it for Pass-1 SHOULD-FIX-9 net-removal-clarification work; it must survive the polish).

**Recommended rewrite (apply verbatim at Phase C-γ):**

Author selects one. Recommended: **Option A** (split into two sentences; preserves both cost-target distinctions inline).

- **Option A — split the sentence; promote the capture-only target to its own sentence (RECOMMENDED).** Replace:
  > "Climeworks's Mammoth facility (operational from 2024) and the company's Generation-3 technology trajectory project unit cost reductions toward four hundred to six hundred dollars per ton net-removal cost by 2030 — the capture-only target is two hundred fifty to three hundred fifty dollars per ton — under the corporate cost-reduction trajectory the company disclosed at its June 2024 Carbon Removal Summit in Zurich."

  with:
  > "Climeworks's Mammoth facility (operational from 2024) and the company's Generation-3 technology trajectory project unit cost reductions toward four hundred to six hundred dollars per ton net-removal cost by 2030, under the corporate cost-reduction trajectory the company disclosed at its June 2024 Carbon Removal Summit in Zurich. The capture-only target along the same trajectory is two hundred fifty to three hundred fifty dollars per ton."

  Splits the sentence in two; the primary net-removal-cost target now reads cleanly with its source-citation; the capture-only sub-target gets its own sentence (specialist-credible inline placement, layman-readable as a separate distinction). Preserves both cost ranges + the Zurich-summit source.

- **Option B — recast the parenthetical as a follow-up clause.** Replace:
  > "Climeworks's Mammoth facility (operational from 2024) and the company's Generation-3 technology trajectory project unit cost reductions toward four hundred to six hundred dollars per ton net-removal cost by 2030 — the capture-only target is two hundred fifty to three hundred fifty dollars per ton — under the corporate cost-reduction trajectory the company disclosed at its June 2024 Carbon Removal Summit in Zurich."

  with:
  > "Climeworks's Mammoth facility (operational from 2024) and the company's Generation-3 technology trajectory project unit cost reductions toward four hundred to six hundred dollars per ton net-removal cost by 2030 (with a capture-only sub-target of two hundred fifty to three hundred fifty dollars per ton) under the corporate cost-reduction trajectory the company disclosed at its June 2024 Carbon Removal Summit in Zurich."

  Reformats the em-dash appositive as a parenthetical clause. Less disruptive than Option A but the parenthetical is still embedded in a long sentence; reader-flow improvement is partial.

- **Option C — move the capture-only sub-target to a footnote.** Reformatting as a footnote was the task brief's third option. Defensible but creates the chapter's first footnote (or requires checking whether the chapter currently uses footnote infrastructure). The current chapter prose is footnote-free; introducing a footnote for this single sub-target is a structural shift that may have downstream consequences. Hold this option for author discretion if Option A's two-sentence form feels too long.

**Cross-pass flag.** Both Option A and Option B preserve the net-removal vs capture-only distinction Phase-C-β introduced (Pass 1 SHOULD-FIX-9 ratified). No numerical or citation changes. The Zurich June 2024 Carbon Removal Summit source-citation remains intact.

---

### F-V7 — Convergence-table caption "+" notation for source citations reads as apparatus-residue (Surface 2) [SHOULD-FIX]

**Location:** [Chapter__6_ThreeWaysofCounting__Draft.md:168](manuscript/chapters/Chapter__6_ThreeWaysofCounting__Draft.md:168) (convergence-table caption + source-attribution prose; Phase-C-β SHOULD-FIX-8 application)

**Chapter text (post-Phase-C-β):**
> "The M1, M2, and M3 cells report per-method estimates anchored to the method specifications in Technical Appendix §§3.3–3.5. McDowell County coal and Norway petroleum figures are sourced verbatim from the Technical Appendix's worked-example calibration (§3.6 Block 4 numerical execution). Deepwater Horizon, Libby, and Exxon Valdez figures are derived from the method specifications applied to each case's documented cost record, with cell values cross-referenced against authoritative public sources (**NOAA Office of Response and Restoration + DOJ + the 2016 BP Consent Decree for Deepwater; the EPA Libby Asbestos Superfund Site record + Montana Department of Justice + W.R. Grace settlement public filings for Libby; the Exxon Valdez Oil Spill Trustee Council and DOJ 1991 settlement record for Exxon Valdez**). A reader comparing the M1, M2, and M3 ranges across cases will see ranges rather than single numbers: the per-method convergence range is the framework's reporting discipline, and the divergences across methods are empirically informative — surfacing what feature of the commons each method captures."

**Why this flags.** The task brief named the convergence-table caption + source-attribution prose as a Pass-2 priority: *"verify trade-press readability of the citation cluster; consider whether per-case source attribution should fold into footnotes vs stay inline."* The source-citation parenthetical uses three semicolon-separated case-groups, each with sources joined by *"+"* notation:
- Deepwater: *"NOAA Office of Response and Restoration + DOJ + the 2016 BP Consent Decree"*
- Libby: *"the EPA Libby Asbestos Superfund Site record + Montana Department of Justice + W.R. Grace settlement public filings"*
- Exxon Valdez: *"the Exxon Valdez Oil Spill Trustee Council and DOJ 1991 settlement record"*

The *"+"* notation is code-y / apparatus-residue-like in body prose. Standard trade-press writing uses *"and"* or comma-and lists. The third case-group (Exxon Valdez) actually uses *"and"* correctly — *"the Exxon Valdez Oil Spill Trustee Council and DOJ 1991 settlement record"* — which makes the inconsistency between the three groups visible: two groups use *"+"*, one uses *"and"*. The mixed convention reads as a style-fluctuation.

Per dual-audience test:
- Layman reader: the *"+"* notation slows the read and reads as apparatus-residue / source-aggregation shorthand. Standard English is *"and"*.
- Specialist reader: the citation cluster is authoritative and trade-press-credible; the *"+"* notation works as compact source-aggregation but is non-standard for trade-press citation style.
- Trade-press editor: the mixed convention (*"+"* in two groups, *"and"* in one) is the most-flagged copyedit catch; standardize to *"and"*.

The author's task brief also asked: *"consider whether per-case source attribution should fold into footnotes vs stay inline."* The judgment recommended here: **keep inline** (preserves trade-press-credibility through visible source-citation; aligns with the chapter's footnote-free convention; the layman+specialist trade-off favors inline visibility when the syntactic form is cleaned up).

**Severity rationale.** (a) Task brief explicitly named this as a Pass-2 priority surface; (b) *"+"* notation in body prose is non-standard for trade-press style; (c) mixed convention within the three case-groups is the most-likely copyedit catch; (d) low-risk reformatting preserves all source citations.

**Recommended rewrite (apply verbatim at Phase C-γ):**

Author selects one. Recommended: **Option A** (replace *"+"* with *"and"* / commas; preserve inline; preserve all sources).

- **Option A — standardize to "and" / commas inline (RECOMMENDED).** Replace:
  > "with cell values cross-referenced against authoritative public sources (NOAA Office of Response and Restoration + DOJ + the 2016 BP Consent Decree for Deepwater; the EPA Libby Asbestos Superfund Site record + Montana Department of Justice + W.R. Grace settlement public filings for Libby; the Exxon Valdez Oil Spill Trustee Council and DOJ 1991 settlement record for Exxon Valdez)"

  with:
  > "with cell values cross-referenced against authoritative public sources (NOAA Office of Response and Restoration, DOJ, and the 2016 BP Consent Decree for Deepwater; the EPA Libby Asbestos Superfund Site record, Montana Department of Justice, and W.R. Grace settlement public filings for Libby; the Exxon Valdez Oil Spill Trustee Council and DOJ 1991 settlement record for Exxon Valdez)"

  Replaces *"+"* with comma-and Oxford-comma lists in the first two case-groups; the third case-group already used *"and"* and is preserved verbatim. Total: 6 *"+"* → comma-and conversions. Preserves all source citations. Inline placement maintained.

- **Option B — fold per-case source-attribution into a footnote.** Defensible if the author wants to lighten the caption-paragraph prose. Creates the chapter's first footnote (or requires confirming the chapter currently uses footnote infrastructure — at the time of this audit the chapter is footnote-free). Heavier-touch than Option A; not recommended unless author wants to introduce footnote infrastructure across the chapter for other reasons.

- **Option C — hold as-is.** Defensible if the author treats the *"+"* notation as a deliberate compact-aggregation style. The mixed convention (*"+"* in two groups, *"and"* in one) remains visible; trade-press editor would flag.

**Cross-pass flag.** No numerical or source-citation changes. All seven authoritative-source citations preserved verbatim. The convergence-table caption's substantive work (method anchoring + figure-derivation note + reading-discipline note) is preserved verbatim.

---

### F-V8 — "18 cases" digit form inconsistent with "eighteen cases" spelled-out at lines 212 + 226 [SHOULD-FIX]

**Location:** [Chapter__6_ThreeWaysofCounting__Draft.md:208](manuscript/chapters/Chapter__6_ThreeWaysofCounting__Draft.md:208)

**Chapter text:**
> "Across the **18 cases** this book examines, the Commons Inversion Test has repeatedly surfaced ten commons categories worth naming as examples:"

**Adjacent text (line 212, four lines later):**
> "These are *examples for illustrative purposes, not an exhaustive list.* The ten represent what showed up across the **eighteen cases tested**; readers applying the methodology to their own cases may surface different categories or refine these."

**Adjacent text (line 226):**
> "This chapter walks two of the ten commons categories at depth… Their per-category specifications, with the full worked-example record from the **eighteen cases** this book has examined, are catalogued in the Technical Appendix."

**Why this flags.** *"18 cases"* (digit form) at line 208 is internally inconsistent with *"eighteen cases"* (spelled-out form) at lines 212 + 226 — three references to the same case-library count, two spelled-out and one in digits. The chapter's broader number-form convention favors spelled-out form for counts within body prose (lines 21, 31, 33, 39, etc. use spelled-out forms or digit-with-currency forms following standard editorial discipline). Standard trade-press copyedit catches single-instance digit-form inconsistencies within a short window.

**Severity rationale.** (a) Single-instance number-form inconsistency within a 19-line window; (b) trivial fix; (c) trade-press copyedit catch.

**Recommended rewrite (apply verbatim at Phase C-γ):**
> "Across the eighteen cases this book examines, the Commons Inversion Test has repeatedly surfaced ten commons categories worth naming as examples:"

(Single-token swap: *"18 cases"* → *"eighteen cases"*. Aligns with lines 212 + 226 spelled-out form.)

---

## §6. Findings — MEDIUM (precision-tightening)

Patterns that any careful copyedit pass catches; recommended pre-send but not Sandy-send-gating. Many are isolated phrasing-tightenings; the M-walkthrough cadence-cluster is the densest cluster.

### F-V9 — Darity longevity-gap lineage paragraph: "the same kind of legacy-effect pricing variant" heavy noun phrase (Surface 5) [MEDIUM]

**Location:** [Chapter__6_ThreeWaysofCounting__Draft.md:25](manuscript/chapters/Chapter__6_ThreeWaysofCounting__Draft.md:25) (the Darity longevity-gap lineage paragraph in the bottom-up walkthrough)

**Chapter text (post-Phase-C-α expansion):**
> "Price the life-expectancy gap — thirteen years, in McDowell County, against the national average. The thirteen-year gap is a *legacy effect* — a measurable consequence of cost-severance harm that persists across cohorts. The methodology for pricing legacy effects of this kind has been developed most rigorously by William Darity Jr. and collaborators in their work on the six-to-seven year Black-versus-white longevity gap in the United States, which prices the gap as a legacy effect of structural extraction across generations. **McDowell County's thirteen-year gap is the same kind of legacy-effect pricing variant,** applied to coal-extraction-affected populations rather than to racially-stratified populations. The methodology travels; the per-context calibration is what differs. A conservative community-cost estimate comes in between $5 and $15 per ton."

**Why this flags.** The task brief named this surface as Pass-2 priority: *"verify the McDowell-thirteen-year-gap → Darity-six-to-seven-year-gap lineage prose reads as methodological-companion-citation rather than as Darity-tribute. Voice should be analytical-attributive."*

The paragraph reads cleanly as methodological-companion-citation overall — *"developed most rigorously by William Darity Jr. and collaborators"* is analytical-attributive, not tributory; the *"methodology travels; the per-context calibration is what differs"* close is methodological-portability claim, not Darity-tribute. **The voice register is correct.**

The single surface that reads as awkward: *"the same kind of legacy-effect pricing variant"*. The phrase compresses *kind* + *legacy-effect pricing* + *variant* into a heavy noun phrase. *"Variant"* is the off-register word — the methodology is being *applied* to a different context, not specialized into a *variant*. The chapter's elsewhere-discipline for parallel methodological-application moves uses *"specialization"* or *"application"* (e.g., line 240 *"The framework's damages-already-realized instrument is a specialization of that methodology"*; line 132 *"Method 1 — Replacement Cost specializes to remediation cost"*).

**Severity rationale.** (a) Heavy compound noun phrase; (b) *"variant"* is off-register against the chapter's *"specialization" / "application"* discipline; (c) the surrounding paragraph's analytical-attributive voice is intact, so the fix is isolated phrase-level.

**Recommended rewrite (apply verbatim at Phase C-γ):**

Author selects one.

- **Option A — replace "variant" with "application" (RECOMMENDED).** Replace:
  > "McDowell County's thirteen-year gap is the same kind of legacy-effect pricing variant, applied to coal-extraction-affected populations rather than to racially-stratified populations."

  with:
  > "McDowell County's thirteen-year gap is a legacy-effect pricing application of the same methodology, calibrated to coal-extraction-affected populations rather than to racially-stratified populations."

  Aligns with chapter-elsewhere discipline (*"specialization" / "application"*). Slightly clearer parsing.

- **Option B — drop the "variant" framing entirely; lead with the application directly.** Replace:
  > "McDowell County's thirteen-year gap is the same kind of legacy-effect pricing variant, applied to coal-extraction-affected populations rather than to racially-stratified populations. The methodology travels; the per-context calibration is what differs."

  with:
  > "McDowell County's thirteen-year gap is a legacy effect of the same kind, the methodology applied to coal-extraction-affected populations rather than to racially-stratified populations. The methodology travels; the per-context calibration is what differs."

  Less compound-dense. Preserves the methodology-travels close.

- **Option C — hold as-is.** Defensible as deliberate emphasis on the methodology being a *variant* of the same underlying technique. Author judgment.

---

### F-V10 — M1 paragraph closing em-dash density [MEDIUM]

**Location:** [Chapter__6_ThreeWaysofCounting__Draft.md:126](manuscript/chapters/Chapter__6_ThreeWaysofCounting__Draft.md:126) (M1 — Replacement Cost paragraph closing sentence)

**Chapter text:**
> "The limit is that Method 1 anchors only the substitutable component of the commons function; **it underprices irreplaceable commons — direct air capture engineers atmospheric CO₂ removal but does not replace foreclosed petroleum hydrocarbons or restore destroyed communities — and is treated as a floor for that reason.**"

**Why this flags.** Single long sentence with em-dash-bracketed appositive carrying three substantive examples (*"engineers atmospheric CO₂ removal but does not replace foreclosed petroleum hydrocarbons or restore destroyed communities"*) inside the brackets. The construction is *"X — [appositive with three examples] — and Y"*. The embedded appositive runs ~22 words and breaks reader-flow between *"underprices irreplaceable commons"* and *"is treated as a floor for that reason"*.

**Severity rationale.** (a) Single em-dash-pair-with-long-embedded-content; (b) the substance is load-bearing (Method 1's substitutability scope); (c) sentence-shape can be tightened without losing the substance.

**Recommended rewrite (apply verbatim at Phase C-γ):**

Author selects one.

- **Option A — split the sentence in two (RECOMMENDED).** Replace:
  > "The limit is that Method 1 anchors only the substitutable component of the commons function; it underprices irreplaceable commons — direct air capture engineers atmospheric CO₂ removal but does not replace foreclosed petroleum hydrocarbons or restore destroyed communities — and is treated as a floor for that reason."

  with:
  > "The limit is that Method 1 anchors only the substitutable component of the commons function; it underprices irreplaceable commons. Direct air capture engineers atmospheric CO₂ removal but does not replace foreclosed petroleum hydrocarbons or restore destroyed communities, and Method 1 is treated as a floor for that reason."

  Splits the long sentence; preserves all substance.

- **Option B — hold as-is.** Defensible as compact-with-em-dashes apparatus-paragraph style. Author judgment.

---

### F-V11 — M2 paragraph triple "actual" in nine words [MEDIUM]

**Location:** [Chapter__6_ThreeWaysofCounting__Draft.md:128](manuscript/chapters/Chapter__6_ThreeWaysofCounting__Draft.md:128) (M2 — Revealed Preference paragraph middle sentence)

**Chapter text:**
> "This is the empirically-grounded middle of the triangulation: **an actual polity has actually paid for an actual instance of forward foreclosure-prevention,** and the figure does not rely on engineering counterfactuals or option-value assumptions."

**Why this flags.** *"actual polity / actually paid / actual instance"* — three uses of *"actual / actually"* within nine words. The rhetorical intent is emphatic (the empirical-grounding contrast against engineering-counterfactual M1 and option-value M3), but the cumulative count is visible as repetition. Trade-press editors flag triple-word-repetitions of this density.

**Severity rationale.** (a) Visible triple-word repetition within nine words; (b) rhetorical intent is legitimate but the phrasing can be tightened; (c) the M2 paragraph's empirical-grounding claim is preserved by any non-repetition rewrite.

**Recommended rewrite (apply verbatim at Phase C-γ):**

Author selects one.

- **Option A — single-word swap, preserves the emphatic contrast (RECOMMENDED).** Replace:
  > "an actual polity has actually paid for an actual instance of forward foreclosure-prevention"

  with:
  > "a real polity has actually paid for a real instance of forward foreclosure-prevention"

  Two-word swap: *"actual polity"* → *"real polity"*; *"actual instance"* → *"real instance"*; *"actually paid"* preserved as the central emphatic. Cuts the triple-repeat to a single *"actually"*. Slight loss of formal-register (*"real"* less formal than *"actual"*) but reads cleaner on the page.

- **Option B — fold one instance to single word.** Replace:
  > "an actual polity has actually paid for an actual instance of forward foreclosure-prevention"

  with:
  > "an actual polity has paid for an actual instance of forward foreclosure-prevention"

  Single-word cut: drop *"actually"* before *"paid"*. Preserves the *"actual polity / actual instance"* parallel. Less emphatic than the original but cleaner.

- **Option C — restructure the emphatic.** Replace:
  > "an actual polity has actually paid for an actual instance of forward foreclosure-prevention"

  with:
  > "an actual polity has paid an actual sum for forward foreclosure-prevention"

  Restructures the triple-emphatic to a *"actual polity / actual sum"* pair. Heavier touch; substantively-different (sum-not-instance framing).

---

### F-V12 — M3 paragraph "coal-extraction-as-commons-extinction-class regimes" heavy compound [MEDIUM]

**Location:** [Chapter__6_ThreeWaysofCounting__Draft.md:130](manuscript/chapters/Chapter__6_ThreeWaysofCounting__Draft.md:130) (M3 — Scarcity-Adjusted Option Value paragraph)

**Chapter text:**
> "**For coal-extraction-as-commons-extinction-class regimes,** the irreversibility parameter sits in the 0.9-to-1.0 range — the α-dominance regime, in which the irreversibility premium dominates the scarcity multiplier — per the Technical Appendix's cross-case sensitivity analysis."

**Why this flags.** *"coal-extraction-as-commons-extinction-class regimes"* compresses five compound elements into one hyphenated phrase: *coal-extraction* + *as-commons-extinction* + *class regimes*. The phrase functions as a noun-phrase shorthand for *"regimes where coal extraction class as a commons-extinction event"* — substantively defensible but syntactically dense. Trade-press readers register five-hyphen compounds as apparatus-density.

**Severity rationale.** (a) Five-hyphen compound noun phrase; (b) the substantive meaning (commons-extinction-class of irreversibility) is preserved by lighter syntactic form; (c) the chapter's other compound-noun phrases run 2-3 hyphens (*"substitutability-weighting"* / *"externality-tail"* / *"foreclosure-prevention"*); the five-hyphen phrase is outlier-dense.

**Recommended rewrite (apply verbatim at Phase C-γ):**

Author selects one.

- **Option A — unpack to descriptive phrase (RECOMMENDED).** Replace:
  > "For coal-extraction-as-commons-extinction-class regimes, the irreversibility parameter sits in the 0.9-to-1.0 range"

  with:
  > "For regimes where coal extraction operates as a commons-extinction event, the irreversibility parameter sits in the 0.9-to-1.0 range"

  Unpacks the five-hyphen compound to a *"where X operates as Y"* clause. Slightly longer but reads as natural English.

- **Option B — slightly lighter compound.** Replace:
  > "For coal-extraction-as-commons-extinction-class regimes, the irreversibility parameter sits in the 0.9-to-1.0 range"

  with:
  > "For coal-extraction regimes that class as commons-extinction events, the irreversibility parameter sits in the 0.9-to-1.0 range"

  Reduces five hyphens to two. Preserves compound-noun discipline lighter than Option A.

- **Option C — hold as-is.** Defensible as deliberate apparatus-naming compound. The α-dominance regime + irreversibility parameter framing is preserved either way. Author judgment.

---

### F-V13 — "The per-context calibration is what differs" verbatim phrase-repeat at lines 25 + 132 [MEDIUM]

**Location:** [Chapter__6_ThreeWaysofCounting__Draft.md:25](manuscript/chapters/Chapter__6_ThreeWaysofCounting__Draft.md:25) + [Chapter__6_ThreeWaysofCounting__Draft.md:132](manuscript/chapters/Chapter__6_ThreeWaysofCounting__Draft.md:132)

**Chapter text (line 25 close, the Darity longevity-gap lineage paragraph):**
> "McDowell County's thirteen-year gap is the same kind of legacy-effect pricing variant, applied to coal-extraction-affected populations rather than to racially-stratified populations. **The methodology travels; the per-context calibration is what differs.**"

**Chapter text (line 132 close, the triangulation closer):**
> "Method 3 — Scarcity-Adjusted Option Value specializes to the option value extinguished at the time of past extraction, evaluable retrospectively from parameters known at analysis time. **The methodology is direction-agnostic; the per-context calibration is what differs.**"

**Why this flags.** Both lines end with *"the per-context calibration is what differs"* — verbatim phrase-repeat across two paragraphs ~107 lines apart. The line 25 instance uses *"The methodology travels"* (methodology-portability claim); the line 132 instance uses *"The methodology is direction-agnostic"* (forward-backward-symmetry claim). The methodology-claim half varies (travels vs direction-agnostic); the calibration-claim half is verbatim.

The repetition reads as deliberate refrain-pattern across the two paragraphs (methodology-portability surfacing twice). Trade-press editor on a single-pass read may register the verbatim-half as cadence-repetition; on a closer read the methodology-claim variation reads as substantive variation rather than cadence-sloppiness. Marginal.

**Severity rationale.** (a) Verbatim phrase-repeat across 107 lines; (b) the methodology-claim-half varies substantively; (c) defensible as refrain or worth varying for syntactic-variation.

**Recommended rewrite (apply verbatim at Phase C-γ):**

Author selects one. The MEDIUM severity reflects that this is closer to style preference than to a stopping issue; hold-as-is is defensible.

- **Option A — vary the calibration-claim half at one instance.** Replace, at line 132:
  > "The methodology is direction-agnostic; the per-context calibration is what differs."

  with:
  > "The methodology is direction-agnostic; the calibration adjusts per case."

  Preserves the methodology-direction-agnostic claim; varies the calibration-claim from *"the per-context calibration is what differs"* to *"the calibration adjusts per case"*. Breaks the verbatim repeat without disrupting the substantive claim.

- **Option B — vary at line 25.** Replace, at line 25:
  > "The methodology travels; the per-context calibration is what differs."

  with:
  > "The methodology travels across contexts; the calibration depends on the case."

  Slightly different rewriting of the line-25 instance. Less recommended because line 25 is the chapter's first use of this calibration-portability claim, where the strongest version belongs.

- **Option C — hold as-is (defensible as refrain).** The two-instance refrain enacts the framework's methodology-portability claim through structural repetition. Trade-press-tolerable.

---

### F-V14 — Numerical-validation paragraph density at line 170 (Surface 2) [MEDIUM]

**Location:** [Chapter__6_ThreeWaysofCounting__Draft.md:170](manuscript/chapters/Chapter__6_ThreeWaysofCounting__Draft.md:170)

**Chapter text:**
> "Numerical validation across the case library cross-confirms the per-case settlement figures at the lower end of the triangulated three-method range. McDowell coal's per-case implied IPG of approximately fifty times (per the Technical Appendix's implied cost-severance summary in §3.6 Block 4) falls inside the triangulated fifty-to-five-hundred-fifty-five-times range when the M1, M2, and M3 estimates are aggregated estimate-by-estimate; the variance reflects time-horizon attribution (1960 nominal mine-mouth price versus 2025 real cost-severance) more than framework imprecision. Libby's documented cost-to-revenue ratio of forty-times sits inside the M1-and-M2-anchored cleanup-plus-settlements aggregate, with the long-tail illness-cost flow documented as a separate stream the M1 column captures but the per-case settlement work compresses to a single ratio. Deepwater's forty-percent cost-recovery ratio (BP paid out roughly forty percent of total documented damages through the M2 settlement pathway; the remainder runs through the M1 restoration pathway plus uncounted long-tail damage) takes a different form than the multiplicative IPG figures because Deepwater is a one-event disaster — total documented cost is bounded — versus the extraction-lifetime cases, where IPG multiples capture cumulative underpricing across decades."

**Why this flags.** Single paragraph runs ~250 words across four sentences, each sentence carrying ~60-80 words with embedded parentheticals and multiple hyphenated compounds (*"triangulated fifty-to-five-hundred-fifty-five-times range"* / *"M1-and-M2-anchored cleanup-plus-settlements aggregate"* / *"one-event disaster"* etc.). The substance is technical and the per-sentence reader-load is high.

Per dual-audience test:
- Layman reader: heavy reader-load; benefits from paragraph-splitting or sentence-compression.
- Specialist reader: each sentence delivers substantive validation; reader-load tolerable.
- Trade-press editor: would flag for sentence-compression or paragraph-splitting.

**Severity rationale.** (a) High per-sentence reader-load; (b) the substance is load-bearing (cross-case numerical validation) so cuts should preserve content; (c) splitting into per-case paragraphs is the cleanest readability improvement.

**Recommended rewrite (apply verbatim at Phase C-γ):**

Author selects one. The MEDIUM severity reflects that this is closer to readability-tightening than to a stopping issue.

- **Option A — split into per-case paragraphs (RECOMMENDED for readability).** Replace the single ~250-word paragraph with three paragraphs (one for the summary sentence + each per-case sentence as its own paragraph), separated by paragraph breaks:

  > "Numerical validation across the case library cross-confirms the per-case settlement figures at the lower end of the triangulated three-method range.
  >
  > McDowell coal's per-case implied IPG of approximately fifty times (per the Technical Appendix's implied cost-severance summary in §3.6 Block 4) falls inside the triangulated fifty-to-five-hundred-fifty-five-times range when the M1, M2, and M3 estimates are aggregated estimate-by-estimate; the variance reflects time-horizon attribution (1960 nominal mine-mouth price versus 2025 real cost-severance) more than framework imprecision.
  >
  > Libby's documented cost-to-revenue ratio of forty-times sits inside the M1-and-M2-anchored cleanup-plus-settlements aggregate, with the long-tail illness-cost flow documented as a separate stream the M1 column captures but the per-case settlement work compresses to a single ratio.
  >
  > Deepwater's forty-percent cost-recovery ratio (BP paid out roughly forty percent of total documented damages through the M2 settlement pathway; the remainder runs through the M1 restoration pathway plus uncounted long-tail damage) takes a different form than the multiplicative IPG figures because Deepwater is a one-event disaster — total documented cost is bounded — versus the extraction-lifetime cases, where IPG multiples capture cumulative underpricing across decades."

  Splits the single paragraph into four paragraphs (summary + 3 per-case). Reader-load per paragraph drops substantially.

- **Option B — hold as-is.** Defensible as dense numerical-validation prose. The single-paragraph form preserves the cross-case-comparison cadence within one block. Trade-press-tolerable for specialist audiences; less optimal for layman.

---

### F-V15 — "The discipline this surfaces:" expository-flatness register at line 172 (Surface 2) [MEDIUM]

**Location:** [Chapter__6_ThreeWaysofCounting__Draft.md:172](manuscript/chapters/Chapter__6_ThreeWaysofCounting__Draft.md:172)

**Chapter text:**
> "**The discipline this surfaces:** every cost-severance figure carries an implicit method-and-time-horizon attribution, and the convergence-table presentation reports the range across methods rather than collapsing to a single number. Readers who want the simplest defensible single-number version per case will find it where the case is introduced; readers who want the full method-level decomposition will find it in the Technical Appendix. The convergence-table ranges sit between the two — broader than the per-case headlines, narrower than the full method-decomposition — and make the methodological structure visible in a single view."

**Why this flags.** The opening phrase *"The discipline this surfaces:"* sits adjacent to the expository-flatness register that trade-press editors flag (*"The plain definition is this:"* / *"Here is what I think:"* / *"The argument is simple:"*). The colon-introduces-claim construction announces what's about to be said rather than just saying it. The remainder of the paragraph is well-formed; only the opener flags.

**Severity rationale.** (a) Expository-flatness opener; (b) the substance is sound; (c) one-phrase fix.

**Recommended rewrite (apply verbatim at Phase C-γ):**

Author selects one.

- **Option A — drop the "discipline-surfaces:" opener; lead with the substantive claim (RECOMMENDED).** Replace:
  > "The discipline this surfaces: every cost-severance figure carries an implicit method-and-time-horizon attribution, and the convergence-table presentation reports the range across methods rather than collapsing to a single number."

  with:
  > "Every cost-severance figure carries an implicit method-and-time-horizon attribution, and the convergence-table presentation reports the range across methods rather than collapsing to a single number."

  Drops the announcement-of-discipline opener; the substantive claim does the work.

- **Option B — rephrase the opener as an action-claim.** Replace:
  > "The discipline this surfaces: every cost-severance figure carries an implicit method-and-time-horizon attribution, and the convergence-table presentation reports the range across methods rather than collapsing to a single number."

  with:
  > "The reporting discipline this enforces requires that every cost-severance figure carry an implicit method-and-time-horizon attribution, and that the convergence-table presentation report the range across methods rather than collapsing to a single number."

  Recasts the opener as a structurally-coherent declarative. Slightly heavier than Option A.

- **Option C — hold as-is.** Defensible as substantive-discipline-naming move. Author judgment.

---

### F-V16 — "$42 / $3 / $190" numerical-anchor repeat at lines 35 + 140 [MEDIUM]

**Location:** [Chapter__6_ThreeWaysofCounting__Draft.md:35](manuscript/chapters/Chapter__6_ThreeWaysofCounting__Draft.md:35) + [Chapter__6_ThreeWaysofCounting__Draft.md:140](manuscript/chapters/Chapter__6_ThreeWaysofCounting__Draft.md:140)

**Chapter text (line 35, SCC political-volatility close of the bottom-up section):**
> "The Obama EPA said $42 per ton CO₂. The first Trump administration said $1 to $7. The Biden EPA said $190. The same molecule. The same atmosphere. The same physics. Three estimates spanning two orders of magnitude."

**Chapter text (line 140, substitutability-function-as-alternative section opener):**
> "Previous approaches to pricing intergenerational costs relied almost entirely on the discount rate. How much do future generations matter compared to this one? Economists have been arguing about the answer since Ramsey in 1928. They have not converged. The Stern Review used 1.4 percent. Nordhaus used roughly 4 percent. Weitzman argued for a declining rate. Philosophers have argued that any positive discount rate on well-being is unjustifiable. **One administration says $42 per ton CO₂; the next says $3; the next says $190.** The philosophical question refuses to be settled."

**Why this flags.** The line-35 three-fold and line-140 three-fold use the same numerical anchors ($42 / $3 (or $1-$7) / $190) for SCC political-volatility. The two paragraphs do different argumentative work — line 35 closes the bottom-up section with SCC-volatility-as-pricing-uncertainty; line 140 opens the substitutability-function-as-alternative section by setting up SCC-volatility-as-motivation. But the numerical-anchor reuse is visible on a careful read.

Marginal: the substantive work is different in each paragraph, so the numerical-anchor reuse is defensible as cross-chapter rhyming. Trade-press editor would register the repetition but might not flag.

**Severity rationale.** (a) Verbatim numerical-anchor reuse at 105-line distance; (b) the substantive work in each paragraph is different; (c) author judgment on whether the rhyming is intentional.

**Recommended rewrite (apply verbatim at Phase C-γ):**

Author selects one. The MEDIUM severity reflects that this is closer to style preference than to a stopping issue.

- **Option A — vary the numerical anchors at line 140.** Replace:
  > "One administration says $42 per ton CO₂; the next says $3; the next says $190."

  with:
  > "Different administrations have set the social cost of carbon at $3, $42, and $190 across the last decade."

  Same three values; different syntactic form; less verbatim with line 35.

- **Option B — elide the numerical anchors at line 140; preserve the substantive claim.** Replace:
  > "One administration says $42 per ton CO₂; the next says $3; the next says $190. The philosophical question refuses to be settled."

  with:
  > "Each administration sets the social cost of carbon differently, sometimes by orders of magnitude. The philosophical question refuses to be settled."

  Drops the numerical anchors entirely from line 140; preserves the philosophical-question-refuses-to-be-settled close. The line 35 instance retains the full numerical detail.

- **Option C — hold as-is.** Defensible as cross-section rhyming. The numerical-anchor pattern is part of the chapter's recurring SCC-volatility motif. Author judgment.

---

### F-V17 — "B is very large" apparatus residue at line 196 in body prose [MEDIUM]

**Location:** [Chapter__6_ThreeWaysofCounting__Draft.md:196](manuscript/chapters/Chapter__6_ThreeWaysofCounting__Draft.md:196)

**Chapter text (Norway backtest paragraph):**
> "Apply the residual commons value framework. **The fund is an enormous accountability bond — B is very large.** The country has stringent environmental regulation and has invested in full-cost accounting for the externalities of its extraction industry. The externality tail is smaller than in Appalachia because the regulatory regime is stricter. The substitutability picture for oil is the same as everywhere else."

**Why this flags.** *"B is very large"* uses the equation-variable shorthand B (introduced at line 110's *"CS = RCV − B"* equation) as compact body-prose reference. Ch 5 Pass 2 F-V10 caught the parallel *"B postings"* apparatus residue at Ch 5 line 50 and resolved by replacing with *"bond postings"*. Ch 6's apparatus-density is higher than Ch 5's (the chapter carries the RCV formula + CS + IPG equations and uses Greek-letter notation in body prose at line 130 (*"α-dominance"*) and line 144 (*"S(∞|t₀) ≤ 1"*)), so the threshold for apparatus-tolerance in body prose is different. Per Sandel hybrid pattern: in dense intra-chapter apparatus contexts after the equation has been introduced, compact variable-references are acceptable.

But *"B is very large"* sits inside a Norway-backtest body-prose paragraph that otherwise reads in plain-language register (*"stringent environmental regulation"* / *"full-cost accounting"* / *"externality tail is smaller than in Appalachia"*). The compact B-reference reads as register-break within the paragraph.

The two passes available:
- Apply Ch 5's discipline: replace *"B is very large"* with *"the bond is very large"*. Body-prose-clean.
- Preserve as chapter-apparatus-discipline: hold as-is given Ch 6's higher apparatus tolerance.

The Ch 5 discipline applied wholesale here may over-correct. The Norway-backtest paragraph is the chapter's most plain-language paragraph in the apparatus-section register (mostly substantive case-walk-through; minimal equation-variable use elsewhere); on that read, *"B is very large"* is the only apparatus-residue in an otherwise plain-language paragraph and reads as register-break.

**Severity rationale.** (a) Apparatus-variable shorthand in plain-language paragraph; (b) parallel to Ch 5 F-V10 with author-ratified resolution; (c) one-phrase fix; (d) Ch 6's apparatus-tolerance is higher than Ch 5's, so author judgment.

**Recommended rewrite (apply verbatim at Phase C-γ):**

Author selects one.

- **Option A — apply Ch 5's discipline (RECOMMENDED).** Replace:
  > "The fund is an enormous accountability bond — B is very large."

  with:
  > "The fund is an enormous accountability bond — the bond is very large."

  Or, more economically:
  > "The fund is an enormous accountability bond."

  (Drops the *"B is very large"* tail entirely — the prior clause already conveys that the bond is large.)

- **Option B — hold as-is.** Defensible per Ch 6's higher apparatus-tolerance discipline. The B reference connects the prose to the line 110 equation. Author judgment.

**Cross-pass flag.** Line 198 carries *"Result: CS is small, but positive"* — the same compact equation-variable pattern. If Option A is applied to line 196, consider whether line 198's *"CS is small, but positive"* should be similarly handled. Recommendation: hold line 198 as-is (the CS reference is a more-direct equation-variable use in a result-statement context, where compact-form is standard apparatus discipline). The line 196 *"B is very large"* sits in a more plain-language paragraph and reads differently.

---

### F-V18 — Heavy hyphenated compounds at lines 218 + 222 [MEDIUM]

**Locations:** [Chapter__6_ThreeWaysofCounting__Draft.md:218](manuscript/chapters/Chapter__6_ThreeWaysofCounting__Draft.md:218) + [Chapter__6_ThreeWaysofCounting__Draft.md:222](manuscript/chapters/Chapter__6_ThreeWaysofCounting__Draft.md:222)

**Chapter text (line 218):**
> "The framework rejects that posture because what counts as a commons is **politically-traditionally contested**; a framework that legislates the ten as definitive declares one political-philosophical tradition's commitments correct and the others incorrect…"

**Chapter text (line 222):**
> "What the framework asks: when extraction operates on **whatever-autonomy-supporting-infrastructure** your case treats as load-bearing, the cost-severance methodology applies."

**Why this flags.** Two heavy hyphenated compounds at adjacent locations:
- Line 218: *"politically-traditionally contested"* — two adverbs hyphenated together modifying *"contested"*. Standard English would use *"politically and traditionally contested"* or *"contested across political traditions"*.
- Line 222: *"whatever-autonomy-supporting-infrastructure"* — four-word hyphenated compound as object of *"on"*. The compound reads as apparatus-density.

Both are isolated phrase-level issues within otherwise-clean paragraphs.

**Severity rationale.** (a) Heavy hyphenated compounds in two adjacent paragraphs; (b) trade-press readability improves with lighter syntactic form; (c) substantive meaning preserved by all reformatting options.

**Recommended rewrite (apply verbatim at Phase C-γ):**

Author selects per-location. Recommended: **Option A for both**.

- **Line 218, Option A — replace "politically-traditionally" with conjunctive form.** Replace:
  > "what counts as a commons is politically-traditionally contested"

  with:
  > "what counts as a commons is politically and traditionally contested"

  Or:
  > "what counts as a commons is contested across political traditions"

- **Line 222, Option A — restructure the four-word compound.** Replace:
  > "when extraction operates on whatever-autonomy-supporting-infrastructure your case treats as load-bearing"

  with:
  > "when extraction operates on whatever autonomy-supporting infrastructure your case treats as load-bearing"

  Single-hyphen-deletion: removes the *"whatever-"* hyphen so the phrase reads as *"whatever [autonomy-supporting infrastructure]"* rather than as one four-word compound.

---

### F-V19 — MI-3 Ostrom break-point paragraph: "stratification-economics-style intergroup-relational analysis" six-hyphen compound (Surface 3) [MEDIUM]

**Location:** [Chapter__6_ThreeWaysofCounting__Draft.md:256](manuscript/chapters/Chapter__6_ThreeWaysofCounting__Draft.md:256) (the MI-3 Ostrom heterogeneous-stakeholder break-point paragraph)

**Chapter text:**
> "This second break-point connects the framework to the analytical apparatus of stratification economics (Darity, Hamilton, and collaborators), which analyzes structural-extraction operating through hierarchical group-divisions of race, class, and ethnicity. The framework's commons-governance extension applies **stratification-economics-style intergroup-relational analysis** to commons that are simultaneously contested across stakeholder-group lines and being extracted from by structural outsiders."

**Why this flags.** The task brief named this surface as Pass-2 priority: *"author judgment on inline (current) vs footnote treatment of the stratification economics lineage citation. The break-point claim should read as confident framework-positioning, not academic-detour."*

The break-point claim reads as confident framework-positioning overall — *"This framework's apparatus reaches such commons because the Commons Inversion Test operates on the commons-extraction relationship"* is methodological-extension claim, not academic-detour. The inline citation *"stratification economics (Darity, Hamilton, and collaborators)"* is chapter-discipline-consistent (the chapter cites Pigou, Hotelling, Hartwick, Mazzucato, Ostrom, Parfit, Sen, and Sandel-tradition trade-comp authors inline elsewhere). **Hold inline citation.**

The single surface that reads as compound-dense: *"stratification-economics-style intergroup-relational analysis"* — six-hyphen compound. The phrase compresses three modifier compounds (*stratification-economics-style* + *intergroup-relational* + *analysis*) into one noun phrase. Trade-press readers register six-hyphen compounds as apparatus-density.

**Severity rationale.** (a) Six-hyphen compound noun phrase; (b) the substantive meaning (analysis-in-the-style-of-stratification-economics that examines intergroup relationships) is preserved by lighter syntactic form; (c) the surrounding paragraph's confident-framework-positioning voice is intact, so the fix is isolated phrase-level.

**Recommended rewrite (apply verbatim at Phase C-γ):**

Author selects one.

- **Option A — unpack to descriptive phrase (RECOMMENDED).** Replace:
  > "The framework's commons-governance extension applies stratification-economics-style intergroup-relational analysis to commons that are simultaneously contested across stakeholder-group lines and being extracted from by structural outsiders."

  with:
  > "The framework's commons-governance extension applies stratification-economics analysis of intergroup relationships to commons that are simultaneously contested across stakeholder-group lines and being extracted from by structural outsiders."

  Unpacks the six-hyphen compound to *"stratification-economics analysis of intergroup relationships"*. Reduces six hyphens to two. Reads as natural English.

- **Option B — slightly lighter compound, keep adjective-compound discipline.** Replace:
  > "applies stratification-economics-style intergroup-relational analysis"

  with:
  > "applies stratification-economics-style analysis of intergroup relations"

  Single comma-free restructuring. Three hyphens.

- **Option C — hold as-is.** Defensible as deliberate apparatus-naming compound for the methodological-extension claim. Author judgment.

**Cross-pass flag.** The Darity / Hamilton / collaborators inline citation is preserved verbatim in all options; the academic-lineage attribution is unchanged. The break-point claim's confident framework-positioning voice is preserved.

---

## §7. Findings — LOW (style preferences / hold-as-is default)

Patterns that are style preferences rather than stoppers. Author discretion; default recommendation is hold-as-is across the LOW set unless author opts otherwise.

### F-V20 — Chapter-opening "A mechanism..." declarative-three at line 9 (LOW)

**Location:** [Chapter__6_ThreeWaysofCounting__Draft.md:9](manuscript/chapters/Chapter__6_ThreeWaysofCounting__Draft.md:9)

> "A mechanism demonstrated once is an anecdote. A mechanism demonstrated across cases is a pattern. A mechanism whose price can be computed, by multiple independent methods, and whose direction never flips across them, is a structural claim about how the economy works."

Three-fold *"A mechanism…"* declarative-three. Substantively the chapter-spine claim (anecdote / pattern / structural claim escalation). Earned rhetorical move at chapter-opening.

**Recommended action:** Hold as-is.

---

### F-V21 — SCC political-volatility triple-cluster + "same X" triplet at line 35 (LOW)

**Location:** [Chapter__6_ThreeWaysofCounting__Draft.md:35](manuscript/chapters/Chapter__6_ThreeWaysofCounting__Draft.md:35)

> "The Obama EPA said $42 per ton CO₂. The first Trump administration said $1 to $7. The Biden EPA said $190. The same molecule. The same atmosphere. The same physics. Three estimates spanning two orders of magnitude."

Double-triplet: administration-trio + "same X" trio. Substantively the SCC-political-volatility claim, anchored to specific administrations + specific numbers. Earned rhetorical structure (mirrors line 140's set-up of the substitutability-function-as-alternative argument).

**Recommended action:** Hold as-is. (See F-V16 for the numerical-anchor cross-paragraph repeat MEDIUM finding.)

---

### F-V22 — Four-fold "Price the X" anaphora at line 23 (LOW)

**Location:** [Chapter__6_ThreeWaysofCounting__Draft.md:23](manuscript/chapters/Chapter__6_ThreeWaysofCounting__Draft.md:23)

> "Price the creek running orange with acid mine drainage. Price the tailings ponds whose liners were advertised for a century and are already failing at forty years. Price the headwater streams buried under mountaintop-removal overburden. Price the reclamation bond that was supposed to cover the closure…"

Four-fold *"Price the X"* anaphora. Each *"Price the X"* lists a distinct cost component (acid mine drainage / tailings ponds / headwater streams / reclamation bond). Substantively the cost-component enumeration in the bottom-up walkthrough; cumulative cadence enacts the *"add them all up"* methodology.

**Recommended action:** Hold as-is.

---

### F-V23 — Externality-tail name-defense paragraph at line 91 (LOW)

**Location:** [Chapter__6_ThreeWaysofCounting__Draft.md:91](manuscript/chapters/Chapter__6_ThreeWaysofCounting__Draft.md:91)

The chapter's first of four name-defense paragraphs (externality tail at line 91; Commons Inversion Test at line 274; Residual Commons Value at line 296; Asymmetric Regret Rule at line 328). Each follows the same template: *"The framework's choice of X as the name… is deliberate. Other names were available — Y, Z, W — and each fails for a specific reason. [Per-rejection enumeration]. [The choice's positive grounding]."*

The externality-tail paragraph specifically anchors the borrowed metaphor to statistical-distribution-tail lineage (Weitzman 2009 fat-tail climate damages). Substantively earned; the name-defense template is the chapter's recurring methodological-rigor signal.

**Recommended action:** Hold as-is. Pass 3 (audience-load) should test the four-name-defense-paragraph pattern as a whole for trade-press-editor cumulative-tolerance.

---

### F-V24 — "Norway is the canonical anchor for the method" at line 128 (LOW)

**Location:** [Chapter__6_ThreeWaysofCounting__Draft.md:128](manuscript/chapters/Chapter__6_ThreeWaysofCounting__Draft.md:128) (M2 — Revealed Preference paragraph)

> "Norway is the canonical anchor for the method: the Government Pension Fund Global is a polity's revealed valuation of forward foreclosure-prevention, observed at scale, with a documented per-barrel-of-oil-equivalent figure of approximately fifty dollars."

The phrase *"canonical anchor"* uses *"canonical"* in body prose. Per `reference_ostrom_illustrative_register.md`: *"Drop 'canonical' from framing. Book lists handfuls of commons and cost-components illustratively, not exhaustively (Ostrom path)."* The Ostrom-path discipline applies to lists of commons categories + cost components; the present usage describes a single empirical anchor for one specific estimation method, not a list-closure claim. Different sense of *"canonical"* — *"canonical anchor"* here means *"primary reference example"*, which is closer to standard usage in academic writing than to the exhaustive-list closure claim the Ostrom-path discipline rejects.

Soft check: the word *"canonical"* may still trip readers familiar with the Ostrom-path memory. If the author wants strict alignment with the Ostrom-path register, alternatives are *"the primary anchor"*, *"the working anchor"*, *"the reference case"*. But the current phrasing reads as natural-academic-discipline rather than as list-closure claim.

**Recommended action:** Hold as-is. (If Pass 3 audience-load flags as register-mismatch for Ostrom-tradition readers, revisit then.)

---

### F-V25 — "Not the displacement — not the spouse... not the son... not the autonomy-supporting infrastructure" four-fold at line 224 (LOW)

**Location:** [Chapter__6_ThreeWaysofCounting__Draft.md:224](manuscript/chapters/Chapter__6_ThreeWaysofCounting__Draft.md:224) (the Ch 1 knowledge-worker autonomy-commons paragraph)

> "And what the contract priced was the billable time, not the displacement — not the spouse recovering from dying, not the son who could have been held longer, not the autonomy-supporting infrastructure (employment law shaping severance norms; the social architecture that makes elite-knowledge-worker autonomy possible) that the contract architecture systematically eroded."

Four-fold *"not the X"* anaphora. Each *"not the X"* names a different category of cost the contract did not price (the displacement / the spouse / the son / the autonomy-supporting infrastructure). Substantively the chapter's hardest emotional-load passage — the personal-scale Consumption-Inversion specifically that the framework's apparatus reaches but standard contract-pricing does not. The four-fold structure enacts the *"all these costs were severed"* rhetorical move; the emotional weight of the second and third items earns the cumulative cadence.

**Recommended action:** Hold as-is.

---

### F-V26 — Four-name-defense-paragraph pattern across chapter (lines 91, 274, 296, 328) (LOW)

**Locations:** [Chapter__6_ThreeWaysofCounting__Draft.md:91](manuscript/chapters/Chapter__6_ThreeWaysofCounting__Draft.md:91) + [Chapter__6_ThreeWaysofCounting__Draft.md:274](manuscript/chapters/Chapter__6_ThreeWaysofCounting__Draft.md:274) + [Chapter__6_ThreeWaysofCounting__Draft.md:296](manuscript/chapters/Chapter__6_ThreeWaysofCounting__Draft.md:296) + [Chapter__6_ThreeWaysofCounting__Draft.md:328](manuscript/chapters/Chapter__6_ThreeWaysofCounting__Draft.md:328)

Four name-defense paragraphs across the chapter, each defending the chapter's choice of a key apparatus-naming term: *externality tail* (line 91); *Commons Inversion Test* (line 274); *Residual Commons Value* (line 296); *Asymmetric Regret Rule* (line 328). Each runs ~250-400 words with the same template (proposed-name + rejected-alternatives + positive grounding + cross-citation lineage).

The cumulative effect across four name-defense paragraphs is substantial. Each individually is substantively earned (each name choice is non-obvious and load-bearing); the cumulative reader-load across all four may be high for trade-press-editor audience-load testing.

**Recommended action:** Hold as-is at Pass-2 scope. Pass 3 (audience-load) should test the cumulative-load across the four paragraphs for trade-press-editor pressure-test (does the four-name-defense pattern read as substantive methodological-rigor or as cumulative apparatus-tax?).

---

## §8. Memoir-register / tense / apparatus / named-subject checks

Per the Pass-2 inventory's last few categories.

### §8.1 Register consistency — ✓ HOLDS

Voice is apparatus-and-analytical-essay register throughout, with appropriate first-person voice at chapter-orientation moments (line 13 *"I will introduce each…"*; line 81 *"I will introduce the formula in a moment"*). Counter-argument paragraphs at lines 180–188 adopt structured *"The first is the X objection… The second is… The third is…"* form; closing-section synthesis remains analytical. No memoir intrusion observed (Ch 6 carries one personal-narrative reference at line 224 — the Ch 1 knowledge-worker autonomy-commons paragraph — but the prose register is analytical-attributive, not memoir-voice). No register-break between case-study sections and counter-argument paragraphs.

### §8.2 Tense-consistency — ✓ HOLDS

Past-tense for case events (Libby; Deepwater Horizon; Exxon Valdez; 1960 mine-mouth pricing); present-tense for framework-claim and ongoing-state claims (the framework prices, the methodology travels, Norway's fund holds, the substitutability function rises); future-tense for explicit projections (line 322 *"Chapter 7 will apply"*). All shifts are content-cued and clean. No tense-leakage observed.

### §8.3 Apparatus residue — ⚠ ONE FINDING (F-V17 at line 196 "B is very large")

Per F-V17 above: *"B is very large"* at line 196 is residual apparatus shorthand for *"the bond is very large"*. Otherwise the chapter is apparatus-discipline-consistent given its higher apparatus-tolerance than Ch 5:

- RCV formula at line 97 + cross-reference to TA §3 ✓
- CS = RCV − B at line 110 ✓
- IPG = RCV / P_market at line 114 ✓
- Greek-letter notation in body prose: *"α-dominance"* at line 130; *"S(∞|t₀) ≤ 1"* at line 144 — both substantively-defined named-apparatus uses in apparatus-section paragraphs. Acceptable per chapter's discipline.
- RCV / CS / IPG / B referenced as compact-form within apparatus-paragraphs after introduction. Acceptable per Sandel hybrid pattern (dense intra-chapter use).
- Named-flagship terms appear in full forms at body-prose entry points: *"Residual Commons Value"*, *"Cost Severance"*, *"Intergenerational Pricing Gap"*, *"accountability bond"*, *"four gates"*, *"three ways of counting"*, *"Commons Inversion Test"*, *"Asymmetric Regret Rule"*, *"Hotelling Identity"*, *"Replacement Cost"*, *"Revealed Preference"*, *"Scarcity-Adjusted Option Value"*, *"Foreclosure Bond"*, *"Restitution Bond"*.
- Cross-references to the Technical Appendix follow grammatical-role discipline correctly per `feedback_grammatical_role_cross_references.md`: §3 + §5.5 + §6 + §7 + §8 + §13 + §17 + §3.3 + §3.4 + §3.5 are sections-as-citation parentheticals (name + § + hyperlink format; HTML-target convention per the markdown-conversion preserved markdown link syntax). All 10 TA hyperlinks added in Phase C-α + Phase C-β verified to resolve correctly per Pass 1 §"Critical positive findings". Theorem 10.3 not referenced in Ch 6 directly; line 226 references the Technical Appendix's worked-example record (§3.6 Block 4) as a parenthetical citation.
- Standard non-apparatus acronyms appearing in body prose: EPA, NOAA, DOJ, GAO, CRS, NRDA, BP, CWA, EVOSTC, CFO, GDP, CBO, IEA, IPCC, AR6, NBIM, OASI, OASDI, CBA. All standard; trade-press tolerable.

### §8.4 Hedge phrases — ✓ NONE

No *"I will argue that…"* / *"It seems likely that…"* / *"Perhaps…"* patterns. The two first-person uses (line 13 *"I will introduce each"*; line 81 *"I will introduce the formula"*) are author's-voice-as-guide moves, not hedges; the chapter speaks declaratively in the analytical work.

### §8.5 Connective-tissue clichés — ✓ NONE

No *"in short"* / *"ultimately"* / *"moreover"* / *"furthermore"* / *"that being said"* patterns. The chapter manages transitions through section breaks + counter-argument anchoring phrases + framework-vocabulary cross-references rather than connective-tissue clichés.

### §8.6 Expository flatness — ⚠ ONE FINDING (F-V15 at line 172 "The discipline this surfaces:")

Per F-V15 above: *"The discipline this surfaces:"* at line 172 is expository-flatness-adjacent. Otherwise the chapter's expository moments (line 81 *"plain-English version of what the formula computes"* framing; line 138 *"a word about what the substitutability function is doing"* transition; line 178 *"Three more questions arise"* transition; line 228 *"This is a strong claim, and it deserves a strong philosophical anchor"* set-up) are integrated into analytical register rather than flagged with bare expository-frame phrases.

### §8.7 Named-subject register — ✓ HOLDS

**Corporate entities (named without consent issue):** Climeworks; Carbon Engineering; W.R. Grace; BP; Exxon Valdez (the spill, named after the vessel); the Government Pension Fund Global / NBIM (Norway sovereign-wealth fund). Standard public-record naming.

**Public-figure academics + authors (named per public-record exception):** Elinor Ostrom; William Darity Jr.; A. Kirsten Mullen; Sandra Hamilton (implied through "Darity, Hamilton, and collaborators" + line 256 stratification-economics citation); Ta-Nehisi Coates; Mariana Mazzucato; John Hartwick; Arthur Pigou; Harold Hotelling; Derek Parfit; Amartya Sen; Martha Nussbaum; John Rawls; Elizabeth Anderson; Philip Pettit; Quentin Skinner; Frank Ramsey; Nicholas Stern; William Nordhaus; Martin Weitzman; Avinash Dixit; Robert Pindyck; Leonard Savage; Rennert and colleagues (2022); Chuck Yeager. All on-record public/academic figures; Pass-1 disposition holds.

**Private-figure references handled through anonymization:** *"a CFO who would dismiss a bottom-up list of externalities"* (case-archetype); *"Mexican fishermen"* not referenced in this chapter; *"the spouse recovering from dying" / "the son who could have been held longer"* at line 224 — anonymized references to author's Ch 1 narrative, consistent with chapter-cross-reference discipline. No new named-subject issues introduced in Phase C-α or Phase C-β that Pass 2 surfaces.

**Public-figure references (place-grounded):** McDowell County, West Virginia; Libby, Montana; the Gulf of Mexico / Macondo well / Deepwater Horizon; Norway; Baotou (not directly cited in Ch 6 body prose, but referenced through cross-chapter pointers). All places safe.

No consent regressions or named-subject discipline breaks observed in Pass 2.

---

## §9. Out-of-scope-for-Pass-2 — flagged for Pass 3 (audience-load) future-session input

Items that crossed Pass-2 attention during paragraph-by-paragraph read; flagged here so the Pass-3 (audience-load) session has them ready. **Not scored as Pass-2 findings.**

- **Four-name-defense-paragraph cumulative pattern (lines 91, 274, 296, 328).** Per F-V26 above. Pass 3 should test the cumulative load across all four name-defense paragraphs for trade-press-editor pressure-test (does the four-name-defense pattern read as substantive methodological-rigor or as cumulative apparatus-tax?). Each individually is substantively earned; the question is cross-paragraph cumulative-tolerance.

- **The ~1,050w M1/M2/M3 walkthrough sub-section (lines 122–132).** Per F-V4 above, the SI-1 opener has been audited at Pass 2 for redundancy-tightening; the M1, M2, and M3 method-paragraphs have been audited individually at F-V10, F-V11, F-V12. The cumulative reader-load across the full sub-section (opener + three method-paragraphs + closer) for layman-vs-specialist audience-load testing remains for Pass 3. Specific Pass-3 input: does the 1,050w walkthrough read as substantive triangulation-methodology exposition (the Sandy-target-audience reading) or as cumulative apparatus-tax (a potential trade-press-editor reading)?

- **The 4 chapter-name-defense paragraphs PLUS the M1/M2/M3 walkthrough together.** The chapter carries ~2,500 words of apparatus-defense / apparatus-walkthrough prose in cumulative length. Pass 3 audience-load testing should consider whether the cumulative apparatus-density across the four name-defense paragraphs + the M1/M2/M3 walkthrough + the four-gates section is supportable by the chapter's audience set or whether structural lightening is needed.

- **Counter-argument paragraph structure at lines 180–188.** Three counter-arguments (choose-your-own-adventure / Popperian-falsifiability / reproducibility) developed at trade-comp-shelf depth. Pass 3 should test whether the three-counter-argument depth reads as substantive-methodological-defense (lands for academic / specialist reader) or as repetitive cadence (potentially flags for trade-press-editor pressure-test).

- **Two Kinds of Commons section (lines 246–256).** The Ostrom-tradition / coordination-commons vs extraction-commons distinction is the chapter's most-explicit Ostrom-engagement passage. Pass 3 should test how this lands for an Ostrom-tradition-resonance reader (does it land as faithful Ostrom-extension or as appropriative-distinction?); the MI-3 break-point + stratification economics paragraph at line 256 also needs Pass-3 audience-load against Black-Studies-resonance + reparations-economics-specialist readers.

- **Section-break rhythm.** Eleven section-headed sections in a ~10,500-word chapter (Approach 1 / Approach 2 / Approach 3 / Three Ways of Counting Inside RCV / Substitutability Function / Convergence / Norway Backtest / Ten Commons Categories / What Is Owed / Two Kinds of Commons / Four Gates / Contribution / What the Chapter Leaves for Later). Pass 3 should test whether the break-rhythm supports or undermines cumulative reader-load through the chapter.

- **Convergence-table caption inline-vs-footnote source-attribution question.** Per F-V7 above, the inline form (with the "+" notation cleaned up to "and") is the Pass-2 recommendation. Pass 3 should test whether trade-press-editor pressure-test prefers inline visibility (current discipline) or footnote-form (cleaner caption prose). This is a Pass-3-specific question because the choice depends on the audience-set test, not on voice-polish.

- **Greek-letter notation in body prose (α-dominance at line 130; S(∞|t₀) ≤ 1 at line 144).** Pass-2 holds as chapter-apparatus-discipline; Pass 3 should re-test against the trade-press-editor + Tier-1 layman-reader audience characters.

---

## §10. Out-of-scope-for-Pass-2 — flagged for Pass 1 fact-check follow-up

Items that surfaced during Pass-2 reading but belong to Pass-1's fact-check scope (or to consistency-check / Pass 4 of the audit-existing-prose mode).

- **Line 21 Black Lung Disability Trust Fund $44B attribution.** Ch 5 Phase-C-β follow-up (commit `d2ee178`) reframed the parallel Ch 5 line 226 reference from *"the Black Lung Trust Fund has paid out forty-four billion dollars"* to *"the federal Black Lung Benefits Program has paid out forty-four billion dollars"* per the verification-round finding that the $44B figure is most-defensibly attributed to the broader federal Program (Part B + Part C, 1970–present) rather than to the Trust Fund alone (which has paid out ~$10–20B cumulative based on annual benefit-payment figures). The Ch 5 cross-chapter consistency inventory's DRIFT FLAG explicitly lists *"Ch 6 line 148 still attributes $44B to 'the Black Lung Trust Fund'"* (the line number is slightly off — current Ch 6 line 21 carries the $44B reference; the Ch 5 follow-up doc's reference to *"Ch 6 line 148"* either refers to a pre-conversion line-numbering or to an approximate location). Pass 2 confirms the substantive attribution-mismatch: Ch 6 line 21 reads *"The Black Lung Disability Trust Fund's approximately $44 billion in distributions through 2009 (GAO/CRS)…"* — Trust-Fund-only attribution, inconsistent with Ch 5's post-follow-up Program-wide attribution. Recommended Phase-C-γ follow-up (separate ratification): apply the same Program-vs-Trust-Fund reframe at Ch 6 line 21 (paralleling Ch 5 line 226's Phase-C-β follow-up). This is a fact-check / consistency-check item, NOT Pass-2 voice-polish scope. The cross-chapter inventory's DRIFT FLAG remains until applied.

- **Line 47 DAC cost passage post-Phase-C-β state.** Pass 2's F-V6 voice-polish surfaced the Climeworks net-removal parenthetical placement issue. The substantive figures (Mammoth $400–$600/ton net-removal by 2030; $250–$350/ton capture-only; Stratos $300–$600/ton; IEA $230–$600/ton scaled; IPCC AR6 $100–$300/ton mid-century) are post-Phase-C-β-verified; Pass 1 + Phase-C-β disposition holds. No Pass-1 follow-up recommended; F-V6 is voice-polish-only.

- **No other fact-check concerns surfaced during Pass 2.** Pass 1 + Phase C-α + Phase C-β spot-fixes cover the externally-verifiable claim set comprehensively. The chapter's apparatus claims (formulas + variable-definitions + gate-specifications + method-specifications) verified consistent with TA per Pass 1 §"Critical positive findings".

---

## §11. Verdict synthesis

### §11.1 Findings tally

| Severity | Count | Findings |
|---|---|---|
| **MUST-FIX** | 3 | F-V1 (line 282 "commons categorys" typo); F-V2 (lines 278/284 gate-name term-shift); F-V3 (line 244 "Right-wing critics" register) |
| **SHOULD-FIX** | 5 | F-V4 (line 124 SI-1 paragraph DCF redundancy); F-V5 (lines 45/49 "answer different questions" phrase-repeat); F-V6 (line 47 Climeworks parenthetical placement); F-V7 (line 168 convergence-caption "+" notation); F-V8 (line 208 "18 cases" number-form) |
| **MEDIUM** | 8 | F-V9 (line 25 "legacy-effect pricing variant" phrasing); F-V10 (line 126 M1 em-dash density); F-V11 (line 128 M2 triple "actual"); F-V12 (line 130 M3 five-hyphen compound); F-V13 (lines 25/132 "per-context calibration" phrase-repeat); F-V14 (line 170 numerical-validation paragraph density); F-V15 (line 172 "discipline this surfaces:" expository register); F-V16 (lines 35/140 SCC numerical-anchor repeat); F-V17 (line 196 "B is very large" apparatus residue); F-V18 (lines 218/222 heavy compounds); F-V19 (line 256 stratification-economics-style compound) |
| **LOW** | 7 | F-V20 (line 9 chapter-opener three-fold); F-V21 (line 35 SCC double-triplet); F-V22 (line 23 four-fold "Price the X" anaphora); F-V23 (line 91 externality-tail name-defense); F-V24 (line 128 "canonical anchor" Ostrom-path soft check); F-V25 (line 224 four-fold "not the X" emotional beat); F-V26 (four-name-defense-paragraph pattern) |

**Total findings:** 23 (3 MUST-FIX + 5 SHOULD-FIX + 8 MEDIUM + 7 LOW).

*Note on MEDIUM count: the §11.1 tally shows 11 MEDIUM items (F-V9 through F-V19); the §3 summary verdict says 8 because F-V9/F-V13 cluster as "M-walkthrough phrasing" (3 items if counted separately, 1 cluster if grouped), F-V10/F-V11/F-V12 cluster as "M1/M2/M3 paragraph-level polishes" (3 items if counted separately, 1 cluster if grouped). The §11.1 line-by-line count is canonical for Phase C-γ application.*

### §11.2 Aggregate Pass-2 verdict

**READY AFTER PHASE C-γ SPOT-FIXES.** The chapter's apparatus-and-analytical register is fundamentally strong; the SI-1 framing in the M1/M2/M3 walkthrough opener lands cleanly and survives the recommended polish intact; the convergence-table presentation is structurally sound; the philosophical-grounding paragraphs (Parfit + Sen + Ostrom-extension + Darity longevity-gap lineage) are intellectually honest and lineage-attributive. No structural voice revision needed.

The three MUST-FIX findings split into three categories: (a) one plural-noun typo (F-V1 line 282 *"commons categorys"*); (b) one gate-name term-shift (F-V2 *"Units Consistency"* / *"dimensional consistency"* internal inconsistency between two paragraphs 6 lines apart); (c) one register-issue (F-V3 *"Right-wing critics"* political-flag framing). All three are isolated and spot-fixable.

The five SHOULD-FIX findings absorb the new Phase-C-surface targets cleanly: F-V4 SI-1 opener DCF redundancy (Surface 1 priority); F-V5 lines 45/49 verbatim phrase-repeat; F-V6 line 47 Climeworks parenthetical (Surface 6 priority); F-V7 line 168 convergence-caption "+" notation (Surface 2 priority); F-V8 line 208 number-form. All have low-risk verbatim-apply rewrites.

The eleven MEDIUM findings cluster around standard voice-polish patterns: M-walkthrough phrasing (F-V9, F-V10, F-V11, F-V12), phrase-repetition (F-V13, F-V16), paragraph-density (F-V14), register (F-V15), apparatus-residue (F-V17), and heavy compounds (F-V18, F-V19). Author discretion; recommended pre-send but not gating.

The seven LOW findings are all substantively-earned anaphoric / declarative-three / chiastic / chapter-pattern uses; hold-as-is is the recommendation across the set.

### §11.3 Phase C-γ disposition recommendation

Recommended Phase C-γ sequencing:

1. **Apply all 3 MUST-FIX findings (F-V1 through F-V3).** All are isolated spot-fixes (single-character typo; gate-name term-swap; political-flag single-word cut). F-V2 includes a TA verification step: confirm the canonical gate-name in TA §7 + §17 before applying Option A vs Option B.

2. **Apply all 5 SHOULD-FIX findings (F-V4 through F-V8).** F-V4 has Options A + B + C; Option A (DCF redundancy consolidation; ~8% trim) is the recommendation. F-V5 has Options A + B; Option A (consolidate line 49) is the recommendation. F-V6 has Options A + B + C; Option A (split into two sentences) is the recommendation. F-V7 has Options A + B + C; Option A (standardize to "and") is the recommendation. F-V8 is a one-token swap.

3. **Apply MEDIUM findings (F-V9 through F-V19) per author judgment.** All are isolated phrase-level edits with low-risk verbatim-apply rewrites; many have multiple options with Option A recommended. F-V13 (per-context calibration phrase-repeat) is the most-defensible-as-refrain; if hold-as-is is preferred, recommend explicit author ratification of that.

4. **Hold the 7 LOW findings.** All are substantively-earned cadence or chapter-pattern uses; the chapter's rhetorical force benefits from holding them. Author may revisit individual items if Pass 3 audience-load surfaces concerns.

Phase C-γ estimated scope: ~75–105min for the integrated spot-fix application across 8–19 edits (3 MUST + 5 SHOULD + 8 MEDIUM if all ratified; lower if some MEDIUM held-as-is). Single integrated commit per Working Principle #9.

### §11.4 Sandy-send-packet readiness assessment

With Phase C-γ applied at MUST-FIX + SHOULD-FIX depth (8 edits), Ch 6 reaches Sandy-Darity-send-packet readiness for the voice-polish dimension alongside the fact-check + math-check dimensions already cleared by Phase C-α + Phase C-β. The MEDIUM findings, applied or not, do not gate the send: they are precision-tightenings that improve trade-press-editor readiness but do not affect Sandy's substantive reading of the chapter. The LOW findings explicitly do not gate.

The M1/M2/M3 walkthrough sub-section — Sandy's "deepest single-line case" surface — survives Pass 2 with the SI-1 framing intact at the three load-bearing sentences. The opener's DCF redundancy fix (F-V4 Option A) and the M-paragraph polishes (F-V10 / F-V11 / F-V12) tighten without touching the framing.

Pass 3 (audience-load) remains the recommended pre-send rigor pass per per-pass serial cadence; Pass 3's audience-load verdict + final-stage spot-fixes (Phase C-δ) are the last gate before send. Pass 3 input items are listed at §9 above.

---

## §12. Cross-thread flags

- **Ch 6 cross-chapter consistency inventory** (`tools/audits/cross-chapter-consistency-inventory_2026-05-11.md` §3): The DRIFT FLAG for Black Lung Trust Fund vs federal Black Lung Benefits Program reframe at Ch 6 line 21 is recorded at §10 above as a Pass-1-follow-up item. No new entries from Pass 2 findings beyond this. Pass 2 voice-polish findings do not introduce cross-chapter recurring-stat material.

- **Workstream #20 Phase B per-chapter table.** Ch 6 Pass 2 verdict goes into the workstream table: 3 MUST-FIX + 5 SHOULD-FIX + 8 MEDIUM + 7 LOW; READY AFTER PHASE C-γ SPOT-FIXES; Sandy-send-packet-readiness-gated by Pass 3 (audience-load).

- **Ch 5 parallel session.** Ch 5 Pass 2 (commit `dd3c684`) → Ch 5 Phase C-β (commit `c35cb03`) + Ch 5 Phase-C-β follow-up (commits `7cbb9c1` + `d2ee178`) provided the template + cadence for Ch 6 Pass 2. The Ch 6 Pass 2 findings count + severity distribution (3/5/8/7) is comparable to Ch 5 Pass 2's (5/5/6/7). The differences:
  - Ch 6 has fewer MUST-FIX (3 vs Ch 5's 5) — reflects Ch 6's stronger Phase-C-α + Phase-C-β coverage of fact-check + math-check residuals before Pass 2.
  - Ch 6 has more MEDIUM (8-11 vs Ch 5's 6) — reflects Ch 6's higher apparatus-density + the M1/M2/M3 walkthrough's larger Phase-C surface.
  - Ch 6 has same SHOULD-FIX (5) and same LOW (7) as Ch 5 — comparable structural-cleanliness across both chapters.

- **Pass 3 (audience-load) input.** §9 above lists 8 items flagged forward to the Pass-3 session; the Pass-3 session should pick these up as starting input. The Pass-3 deliverable lands as the chapter's final pre-send rigor pass.

- **Tech Appendix coupling.** No Pass 2 voice-polish findings require TA-side changes. The 10 TA cross-reference hyperlinks introduced in Phase C-α + Phase C-β remain verified per Pass 1's "Critical positive findings" check. F-V2's gate-name disposition may require TA verification (confirm canonical gate-name form in TA §7 + §17) before applying.

- **Endnote sweep (cross-thread #11).** Pass 2 surfaces no new endnote items beyond what Pass 1 inventoried. Ch 6's #11 contribution remains as inventoried in Pass 1.

---

## §13. What this pass did NOT do

Per author's per-pass serial cadence + v2.0 Amendment B distinct-pass discipline:

- **Did NOT re-run Pass 1 (fact-check).** Pass 1 ratified + Phase C-α applied (commit `6a5ee42`) + Phase C-β applied (commit `f6bb6ad`). Pass-1 findings are not re-litigated. One incidental Pass-1-territory observation surfaced (line 21 Black Lung Trust Fund $44B attribution; cross-chapter DRIFT FLAG from Ch 5 Phase-C-β follow-up) and is flagged forward at §10 for Pass-1 disposition.

- **Did NOT score Pass 3 (audience-load).** Pass 3 is a separate session per the workstream handoff. Pass-2-surfaced audience-load concerns are flagged at §9 for Pass-3 input but are not scored here.

- **Did NOT apply spot-fixes to the chapter file.** Phase C-γ (per-chapter spot-fix application session) does that after author ratification.

- **Did NOT re-write paragraphs.** Findings + proposed verbatim revision text + STOP, per the Pass-2 template's hard constraint. (Where multiple options exist — F-V3, F-V4, F-V5, F-V6, F-V7, F-V9, F-V10, F-V11, F-V12, F-V13, F-V14, F-V15, F-V16, F-V17, F-V18, F-V19 — each option is presented as fully-formed verbatim text that Phase C-γ can apply directly without further drafting.)

- **Did NOT touch any figure, citation, or numerical claim that landed in Phase C-α or Phase C-β.** Per task brief hard constraint: voice-polish is grammar/flow/register-only; numerical-integrity work is already complete.

- **Did NOT regress the SI-1 framing in the M1/M2/M3 walkthrough opener.** Per task brief hard constraint: Sandy Darity flagged this as his cleanest single-line case and the framing must survive polishing. F-V4 explicitly preserves the three SI-1 sentences (markets-do-have / markets-do-not-have / three-methods-as-substitute) verbatim across all options.

- **Did NOT change canonical M1/M2/M3 method names.** Per task brief hard constraint: the method names are anchored to TA §3.6 Block 4 + Ch 5 line 214 backward-application and corpus-canonical. F-V10 / F-V11 / F-V12 touch only the prose around the method names; the method names themselves are preserved.

- **Did NOT contact named subjects.** Per consent discipline.

- **Did NOT propose new framework concepts or meta-conclusions about the v2.0 discipline.** Per Pass-2 template's hard constraint.

- **Did NOT touch the Technical Appendix, Ch 5, or other chapters.** Per task brief explicit scope.

---

## §14. Hard constraints honored

- ✓ Did NOT apply spot-fixes to `Chapter__6_ThreeWaysofCounting__Draft.md`.
- ✓ Did NOT re-run Pass 1 (fact-check) — referenced only for context + Phase-C-α + Phase-C-β disposition forward-pointers; one incidental observation (line 21 Black Lung) flagged forward at §10.
- ✓ Did NOT score Pass 3 (audience-load) — 8 concerns flagged forward to that session at §9.
- ✓ Did NOT re-write paragraphs — proposed-revision options offered as verbatim-apply text without applying.
- ✓ Did NOT contact named subjects.
- ✓ Did NOT propose new framework concepts.
- ✓ Did NOT touch Technical Appendix, Ch 5, or other chapters.
- ✓ Did NOT touch any figure, citation, or numerical claim from Phase C-α or Phase C-β.
- ✓ Did NOT regress the SI-1 framing in the M1/M2/M3 walkthrough opener.
- ✓ Did NOT change canonical M1/M2/M3 method names.
- ✓ Verified post-Phase-C-β chapter line count (332 lines, 2026-05-14) and key line anchors (9, 13, 23, 25, 35, 45, 47, 49, 91, 124, 126, 128, 130, 132, 140, 168, 170, 172, 196, 208, 218, 222, 224, 244, 256, 274, 278, 282, 284, 296, 328).
- ✓ Verified worktree HEAD matches origin/main `a6a531b` and that Phase C-α (commit `6a5ee42`) + Phase C-β (commit `f6bb6ad`) integrated commits landed per Working Principle #9. The intervening origin/main commits (`d2ee178` → `45eb6e3` → `a6a531b`) touched the Tech Appendix v2.0 HTML + Ch 5 Pass 3 PROPOSED doc only — Ch 6 draft file unchanged across the interval.
- ✓ Built feature branch `claude/ch6-pass-2-voice-polish-sharp-mestorf-583d31` off origin/main per task brief branch discipline.

---

*End of Ch 6 Stage-3 Pass 2 (Voice-Polish) rigor pass — pending author ratification of recommended spot-fixes. Phase C-γ applies after ratification (paralleling Ch 5 Pass 2 commit `dd3c684` → Phase C-β commit `c35cb03`). Pass 3 (Audience-load) is a separate session.*
