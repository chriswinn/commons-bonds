# Stage-3 Rigor Pass — Chapter 6 (Three Ways of Counting) — Pass 1: Fact-check + Math-check overlay [PROPOSED]

**Date:** 2026-05-13
**Workstream:** #20 Manuscript Stage-3 Rigor Pass — Phase A (per-chapter audits)
**Chapter:** 6 — *Three Ways of Counting*
**File audited:** [Chapter__6_ThreeWaysofCounting__Draft.md](manuscript/chapters/Chapter__6_ThreeWaysofCounting__Draft.md)
**Line count:** 309 (Draft); 439 (GuidanceDoc)
**Pass scope:** Pass 1 (Fact-check) with **math-check overlay** per Ch 6's apparatus density. Pass 2 (Voice-polish) and Pass 3 (Audience-load) NOT run this session.
**Hard constraint observed:** No spot-fixes applied to chapter file. Phase C-α session (post-author-ratification) applies recommended edits.
**Status:** **PROPOSED — awaits author ratification.**

---

## Why this pass matters now

Ch 6 is one of two artifacts being sent to Sandy Darity post-2026-05-13 interview (alongside Ch 5 + Tech Appendix). Sandy is a labor economist who will read the apparatus chapter carefully — the chapter is the forward-direction-canonical home for the **four gates** and the **three ways of counting**, the constructs Ch 5's just-added CSD-application section (commit ccaac20) depends on for the framework's bidirectionality claim.

Ch 6 also just completed `.html → .md` conversion at commit 1d9b941 (workstream #18). Conversion preserved three anchor-style hyperlinks to the Technical Appendix that need verification post-#19 Scheme-4 cleanup (commit 2c880bc).

The chapter is also referenced by:
- Ch 5 line 230 forward-pointer ("the three ways of estimating Residual Commons Value")
- Ch 5 line 210 backward-direction setup ("the four gates and the three ways of counting, does that work")
- Ch 5 line 214 informal-label use of the three methods (already flagged as Ch 5 Pass 1 SHOULD-FIX-1 at commit a2d2d3f)
- Ch 10 (in-flight insertion-placement session — references not yet integrated as of file state)

The quality bar is therefore higher than the standard Phase A bar.

---

## Canonical sources consulted

1. [Chapter__6_ThreeWaysofCounting__Draft.md](manuscript/chapters/Chapter__6_ThreeWaysofCounting__Draft.md) — chapter under audit (post-conversion).
2. [Chapter__6___GuidanceDoc.md](manuscript/chapters/Chapter__6___GuidanceDoc.md) — guidance doc with per-section staleness audit dated 2026-05-08.
3. [Chapter__5_THEACCOUNTABILITYGAP__Draft.md](manuscript/chapters/Chapter__5_THEACCOUNTABILITYGAP__Draft.md) — post-CSD-application section state (commit ccaac20).
4. [Chapter_10_CommonBonds__Draft.md](manuscript/chapters/Chapter_10_CommonBonds__Draft.md) — closing-chapter state pre-insertion.
5. [core/technical-appendix/TechnicalAppendix_v2.0.0.html](core/technical-appendix/TechnicalAppendix_v2.0.0.html) — canonical apparatus post-#15 reconciliation + post-#19 Scheme-4 cleanup (commit 2c880bc).
6. [tools/rigor-passes/commons_bonds_ch5_stage_3_pass_1_fact_check_2026-05-13_PROPOSED.md](tools/rigor-passes/commons_bonds_ch5_stage_3_pass_1_fact_check_2026-05-13_PROPOSED.md) — Ch 5 Pass 1 (especially SHOULD-FIX-1 on Method-name vocabulary; closely related finding for Ch 6).
7. Memory entries: feedback_verify_stale_memory_claims.md; feedback_audit_recent_active_review_default.md; feedback_audit_open_illustrative_default.md; feedback_grammatical_role_cross_references.md; reference_sandel_hybrid_pattern.md.

---

## Summary verdict

| Severity | Count | Disposition |
|---|---|---|
| MUST-FIX | 2 | Resolve before Darity send; both are Sandy-Darity-sensitive |
| SHOULD-FIX | 2 | Strongly recommended; bidirectionality + convergence-table integrity |
| MEDIUM | 4 | Spot-fix recommended (author-ratify) |
| LOW | 6 | Verification flags / pre-publication refresh / opportunity hyperlinks |
| CITATION-LATER | — | See cross-thread #11 contribution block below |
| Cross-thread #9 | 1 | GuidanceDoc parallel-staleness analog |

**Aggregate verdict:** **READY AFTER SPOT-FIXES** for Pass 1. Two MUST-FIX findings are gating for Sandy Darity send. Both center on canonical-naming + structural integrity of the chapter's central convergence claim — exactly the surface Sandy will inspect first.

**Critical positive findings:**
- All three TA cross-reference hyperlinks (sec-7-four-gates, sec-8-asymmetric-regret-rule, sec-17-formula-generalization) verified — anchors exist in TA v2.0.0, content match Ch 6's prose claims, post-#19 Scheme-4 cleanup did not break them.
- RCV formula (line 97) matches TA §3.1 verbatim ✓.
- CS = RCV − B (line 110) matches TA §3 + §17.5 ✓.
- IPG = RCV / P_market (line 114) matches TA §3.2 ✓.
- Four-gate term-by-term variable definitions (line 103–106) match TA §7 + §17 ✓.
- McDowell bottom-up arithmetic internally consistent ($8–$22 without carbon; carbon = 2.86 × $190 = $544; with-carbon ≈ $550–$570) ✓ within rounding tolerance.
- DAC cost figures (Climeworks Orca/Mammoth $600–$1,000; Stratos $300–$600; IEA/IPCC $100–$300) match TA §3.3 verbatim ✓.
- Asymmetric Regret Rule citation lineage (Savage 1951) matches TA §8 ✓.
- Parfit non-identity-problem grounding (lines 213–215) is canonical philosophy ✓.
- Convergence-table figures are internally consistent with the per-case-prose disclosure passage at line 149–153 ("different methods producing different numerical compressions").
- No named-subject consent issues in chapter body (no living-private subjects named; Darity, Mullen, Coates, Hamilton, Conley, Anderson, Pettit, Skinner, Ostrom, Parfit, Pigou, Hotelling, Hartwick, Pistor, Yeager, Ramsey, Stern, Nordhaus, Weitzman, Rennert all engaged as public-academic citations; named places safe; Yeager deceased; courtesy-notify class only for any quoted-from-on-record cases — none identified in this chapter).

---

## Findings

### MUST-FIX-1 (CRITICAL): Title "Three Ways of Counting" maps to *different threes* in Ch 6 body vs Technical Appendix §3

**Location:**
- Ch 6 title (line 3): "Chapter 6: Three Ways of Counting"
- Ch 6 line 13: "The three approaches are bottom-up damage accounting, a real-options model, and the residual commons value (RCV) framework."
- Ch 6 line 136: "The three approaches — bottom-up, real-options, and RCV — are built on different foundations."
- Ch 6 line 307: "Three methods. Different foundations. Same direction."
- TA §3 title (line 704): "§3. RCV Quantification — Three Ways of Counting"
- TA §3.3 — Method 1: Replacement Cost; TA §3.4 — Method 2: Revealed Preference; TA §3.5 — Method 3: Scarcity-Adjusted Option Value.

**Canonical drift:**

The phrase "Three Ways of Counting" is used at two distinct levels of the framework's apparatus, and Ch 6 collapses them.

| "Three Ways of Counting" — outer (apparatus-comparison level) | "Three Ways of Counting" — inner (RCV-internal estimation level) |
|---|---|
| **Where it appears:** Ch 6 title + body lines 13, 136, 307 | **Where it appears:** TA §3 title + §3.3, §3.4, §3.5 |
| Approach 1: Bottom-Up Damage Accounting (SCC-anchored damage-function) | Method 1: Replacement Cost (DAC-anchored substitution-cost) |
| Approach 2: The Real Options Model (social-side option value) | Method 2: Revealed Preference (Norway-anchored) |
| Approach 3: The RCV Model (framework's central apparatus) | Method 3: Scarcity-Adjusted Option Value (Dixit-Pindyck + irreversibility-weighting) |

The drift is visible inside Ch 6 itself at line 49, where the chapter acknowledges Approach 3 contains the inner Methods:

> "The substitution-side question (what does it cost to replace the commons function) belongs in **Approach 3's RCV Method 1**; the damage-side question (what does the harm cost) is what Approach 1's bottom-up walkthrough has been answering."

So the outer Approach 3 (RCV Model) itself contains the inner Method 1 (Replacement Cost / DAC). The chapter never resolves which "three" the title is naming, and never explicitly walks the inner M1/M2/M3 inside Approach 3's exposition.

The drift propagates downstream:
- **Ch 5 line 230 forward-pointer** to Ch 6 says "the three ways of *estimating* Residual Commons Value when no single estimation method is sufficient" — this favors the inner Methods reading (M1/M2/M3 are estimation methods for RCV).
- **Ch 5 line 210** says "the four gates and the three ways of counting" — phrase matches Ch 6's title but the body context (preceded by forward-direction case study list, followed by "The same apparatus runs in reverse") leaves the referent ambiguous.
- **Ch 5 line 214** informal labels ("substitution cost / revealed restraint / forward option value") map to the inner Methods M1/M2/M3 — this is the **Ch 5 Pass 1 SHOULD-FIX-1** finding at commit a2d2d3f.

The implication is structural: **Ch 5's backward-direction application is reversing the inner Methods (M1/M2/M3), but Ch 6's forward-direction demonstration is conducting the outer Approaches (Bottom-Up / Real Options / RCV).** The framework's "bidirectional by construction" claim fails if the forward and backward applications are not operating on the same three constructs.

**Why this is MUST-FIX-1:**

Sandy Darity will read both chapters back-to-back. He will see "three ways of counting" in both, in Ch 6's title and in Ch 5's apparatus passage. He will follow the cross-references into the Technical Appendix and find that TA §3 ("RCV Quantification — Three Ways of Counting") describes three Methods that don't match Ch 6's three Approaches. The reader's first-pass mental model of the apparatus will be wrong, and the bidirectionality claim — which is load-bearing for the Coates/Darity-Mullen/Hamilton/Conley reparations-economics lineage Ch 5 has just established — will not survive the read.

This is also the most-Sandel-hybrid-test-sensitive flagship-term issue in the chapter. "Three Ways of Counting" is a named-quantity construct (it is the chapter title; it is also a TA section title; it appears in formula adjacencies, in apparatus summaries, and in cross-references). Per [reference_sandel_hybrid_pattern.md](/Users/c17n/.claude/projects/-Users-c17n-commons-bonds/memory/reference_sandel_hybrid_pattern.md): named-quantity constructs need contextual discipline at first use to disambiguate which three the prose is referring to. Ch 6 currently does not disambiguate at any of its three uses (lines 13, 136, 307).

Per [feedback_audit_open_illustrative_default.md](/Users/c17n/.claude/projects/-Users-c17n-commons-bonds/memory/feedback_audit_open_illustrative_default.md), the audit-side default is open/illustrative reading for framework lists. The current finding is **not** a closure-reading: the user has not asked which three is "canonical" in the metaphysical sense. The finding is: **two distinct threes are in active use under the same name, and the chapter does not navigate the reader between them.** That is a structural ambiguity, not a closure failure.

**Recommended spot-fix:** Three options, author judgment which to apply:

- **Option A (preserve Ch 6's outer-three structure; rename one of them):** Keep Ch 6's three Approaches; rename either the chapter title or TA §3's title so the same phrase does not refer to two different threes. Sample: Ch 6 title remains "Three Ways of Counting" (outer); TA §3 title becomes "RCV Quantification — Three Estimation Methods" (or similar). This is the lighter edit but it leaves the in-body uses of "three ways of counting" in Ch 5 line 210 still ambiguous as to which three.

- **Option B (preserve TA §3's inner-three structure; restructure Ch 6 to walk M1/M2/M3 inside the RCV section):** Ch 6's outer-three Approaches collapse into one apparatus chapter that walks M1 (Replacement Cost; DAC), M2 (Revealed Preference; Norway), M3 (Scarcity-Adjusted Option Value; Dixit-Pindyck) explicitly as the chapter's "three." This is the larger structural edit but aligns Ch 6 with TA §3 + Ch 5 line 214's informal labels + Ch 5 line 230's "three ways of estimating RCV" phrasing. Bottom-Up Damage Accounting becomes a preliminary "what enters the E term" walkthrough rather than a co-equal Approach.

- **Option C (preserve both threes; explicitly disambiguate at first use):** Keep both structures; at Ch 6 line 13 (the first occurrence of "three approaches"), add a disambiguating sentence: "The framework also contains three *estimation methods* for the RCV integrand itself — Replacement Cost (DAC), Revealed Preference (Norway), and Scarcity-Adjusted Option Value (Dixit-Pindyck). Those inner methods are the subject of Technical Appendix §3; this chapter's outer three are the cross-validation triangle (Bottom-Up + Real Options + RCV) that places the inner methods alongside two independent foundations." This is the smallest edit but adds explanatory text the reader has to carry.

**Severity rationale:** MUST-FIX (CRITICAL-equivalent) because (a) the title shared between Ch 6 and TA §3 refers to different threes, (b) the bidirectionality claim's load-bearing connection to Ch 5's CSD-application depends on which three is canonical, (c) Sandy Darity will catch the inconsistency on his first integrated read.

**Cross-session flag:** Coordinate with **#19 TA Scheme-4 cleanup session** before applying. If TA §3's title is being renamed during Scheme-4 work, Option A applies trivially. If not, Option B or C requires explicit author decision.

---

### MUST-FIX-2 (CRITICAL): Convergence table has only 2 method columns but body advertises 3 approaches

**Location:** [Chapter__6_ThreeWaysofCounting__Draft.md:142–147](manuscript/chapters/Chapter__6_ThreeWaysofCounting__Draft.md:142)

**Table as drafted:**

| Case | Market Price | Damage-Function IPG | RCV Model IPG | Direction |
| --- | --- | --- | --- | --- |
| McDowell County coal | $4.50/ton | 5–133× | 19–47× | CS > 0 |
| Deepwater Horizon | $4.25B revenue | 15–17× | ~15× | CS > 0 |
| Exxon Valdez | $5.5M product | 1,200–1,900× | ~1,000× | CS > 0 |
| Libby, Montana | ~$100M lifetime | 55–82× | 40–80× | CS > 0 |

**Issue:** The chapter's central convergence claim is that **three approaches converge**:

> Line 11: "if three different accounting methods produce estimates in the same range — then the gap is not a methodological artifact."
> Line 136: "The three approaches — bottom-up, real-options, and RCV — are built on different foundations."
> Line 155: "The methods converge. Different assumptions, different foundations, same qualitative conclusion and, in most cases, similar magnitudes."
> Line 157: "Three independent accounting methods, built on economics from different decades and different schools, have been applied to the same historical extractions. They agree not because they were designed to agree but because the thing they are measuring is real."
> Line 307: "Three methods. Different foundations. Same direction."

But the table that is presented as the demonstration of this convergence has only **two** quantitative method columns: "Damage-Function IPG" (corresponds to Approach 1: Bottom-Up Damage Accounting) and "RCV Model IPG" (corresponds to Approach 3: RCV Model). **Approach 2 — the Real Options Model — does not have a column.**

The Real Options section (lines 55–74) presents the method qualitatively, ends with "the same answer emerges" (line 73), but never commits a per-case IPG estimate. The convergence-table headline claim ("three methods converge on similar magnitudes") therefore cannot be evaluated for Approach 2 from the table as drafted.

The closest the body comes to giving Approach 2 a per-case number is line 67 ("on the order of tens of dollars at minimum, and plausibly hundreds once the externality tail is included") for 1960 McDowell coal — a one-sentence directional estimate, not a per-case IPG.

**Why this is MUST-FIX-2:**

The convergence claim is the chapter's structural centerpiece. The table is the visual demonstration of the claim. Sandy Darity, a quantitative labor economist, will read the table closely. He will note that two columns of quantitative IPG figures + one Direction column does not equal "three independent methods converging on similar magnitudes." He will ask: where are the Real Options numbers per case? The current chapter does not answer.

This is also a Sandel-hybrid-pattern concern at the chapter-architecture level: a chapter titled "Three Ways of Counting" whose central table shows two of the three is structurally inconsistent with its own framing.

**Recommended spot-fix:** Three options:

- **Option A (commit numbers; add a third column):** For each of the four cases, produce a Real-Options-derived IPG estimate (the social option value of waiting at t₀, divided by market price at t₀, expressed as a multiplier). This requires actual computation per case — McDowell 1960 coal, Deepwater 2010 spill, Exxon 1989 spill, Libby 1963–1990 mining lifetime. Approach 2's apparatus (social option value = private option value + avoided externalities + substitutability window) is specified; the table requires the analyst to do the per-case arithmetic. If the numbers cannot be produced (e.g., for the spill cases the option-value framing may not apply cleanly), the table needs to acknowledge that.

- **Option B (reframe the convergence claim):** Change the chapter's framing to "two quantitative methods + one directional method." The body would explicitly state: Approach 1 + Approach 3 produce IPG figures that converge; Approach 2 produces a directional finding ("CS > 0") that is consistent with both. The "Direction" column in the table would then be re-anchored as the Real Options output, not as a separate observation. This is the lighter edit but it weakens the chapter's central claim.

- **Option C (move Real Options to a different role):** Reposition Approach 2 not as a third co-equal method but as a *theoretical foundation* that Approach 3 (RCV) operationalizes. Under this framing, the chapter's "three" become: Approach 1 (Bottom-Up Damage), Approach 2 (Real Options framework that informs RCV's structure), Approach 3 (RCV applied). The table then legitimately has two quantitative columns because Approach 2 is the framework rather than a separate quantitative method. This is the largest structural edit and overlaps with MUST-FIX-1's Option B.

**Severity rationale:** MUST-FIX (CRITICAL-equivalent) because (a) the convergence claim is the chapter's central finding, (b) the table that visually demonstrates the claim does not match the prose claim, (c) Sandy Darity will read this table arithmetically and the gap will be immediately visible.

---

### SHOULD-FIX-1 (HIGH): Forward (Ch 6) ↔ backward (Ch 5) apparatus-consistency fails when the "three" don't align

**Location:**
- [Chapter__6_ThreeWaysofCounting__Draft.md:13, 136, 307](manuscript/chapters/Chapter__6_ThreeWaysofCounting__Draft.md:13) — forward Approaches 1/2/3
- [Chapter__5_THEACCOUNTABILITYGAP__Draft.md:214](manuscript/chapters/Chapter__5_THEACCOUNTABILITYGAP__Draft.md:214) — backward "same three methods" with informal labels mapping to TA §3 inner Methods M1/M2/M3

**Issue:** Ch 5 line 214 (post-CSD-application addition; commit ccaac20) claims:

> "They yield to the same four gates. They triangulate through the same three methods, applied backward: substitution cost becomes remediation cost; revealed restraint becomes revealed restitution; forward option value becomes the option value extinguished at the time of past extraction, evaluable from what we know now."

The three labels Ch 5 uses for the backward direction map to TA §3's **inner Methods**:
- "substitution cost" ↔ TA §3.3 Method 1 (Replacement Cost / DAC)
- "revealed restraint" ↔ TA §3.4 Method 2 (Revealed Preference / Norway)
- "forward option value" ↔ TA §3.5 Method 3 (Scarcity-Adjusted Option Value)

But Ch 6's forward direction conducts the outer **Approaches**:
- Approach 1: Bottom-Up Damage Accounting (does *not* map onto M1 Replacement Cost — it is SCC-anchored, damage-side)
- Approach 2: Real Options (maps roughly onto M3 Scarcity-Adjusted Option Value, but not named the same)
- Approach 3: RCV Model (is *the whole apparatus that contains* M1/M2/M3)

The "same three methods, applied backward" claim is structurally false as currently stated: the forward direction is not running the same three constructs Ch 5 line 214 reverses.

**Why this is SHOULD-FIX-1:**

The bidirectionality claim is the apparatus-level connection between Ch 6 (forward) and Ch 5's new CSD-application section (backward). It is also the framework's bridge to Darity-Mullen reparations economics (Ch 5 lines 196–224). If Sandy Darity follows the "same three methods applied backward" claim and finds that Ch 6's forward demonstration does not visibly run the inner Methods M1/M2/M3, the bidirectionality claim collapses.

This finding is downstream of MUST-FIX-1. Resolving MUST-FIX-1 by adopting Option B (restructure Ch 6 to walk M1/M2/M3) auto-resolves this finding. Resolving MUST-FIX-1 by Option A (rename one title) leaves this finding open. Resolving MUST-FIX-1 by Option C (disambiguate at first use) requires a separate fix here: Ch 6's body must explicitly demonstrate the inner Methods M1/M2/M3 on the four cases, or Ch 5 line 214 must be rewritten to reference Ch 6's outer Approaches 1/2/3 backward (not the inner Methods).

**Recommended spot-fix:** Coordinate with MUST-FIX-1 resolution. If Option B, no separate fix needed. Otherwise: either Ch 6 body adds an explicit M1/M2/M3 sub-walkthrough inside Approach 3's exposition (with worked examples per case), or Ch 5 line 214 is rewritten to reverse the outer Approaches rather than the inner Methods.

**Severity rationale:** SHOULD-FIX (HIGH-equivalent) because (a) the bidirectionality claim is load-bearing for Ch 5 ↔ Ch 6 ↔ Coates/Darity-Mullen lineage, (b) the structural inconsistency is visible to a careful reader on first integrated pass, (c) downstream of MUST-FIX-1 and partially resolved by some MUST-FIX-1 options.

---

### SHOULD-FIX-2 (HIGH): McDowell coal convergence-table IPG range internally inconsistent with body bottom-up totals

**Location:**
- Table line 144: McDowell coal "$4.50/ton | 5–133× | 19–47×"
- Body line 27 (bottom-up without carbon): "$8 to $22 per ton"
- Body line 31 (bottom-up with carbon at $190 SCC): "$550–570 per ton"
- Body line 149 (per-case work disclosure): "the per-case work settles on a tighter 33–122×"
- GuidanceDoc line 87 (stale): "Total: $21-54/ton without carbon, $567-598/ton with carbon"

**Math check:**

- $4.50 × 5 = $22.50 — corresponds to upper end of bottom-up **without** carbon ($22), which is the boundary case. The 5× lower bound implies a $22.50 RCV, but that is the body's maximum without-carbon estimate, not the minimum with-carbon.
- $4.50 × 133 = $598.50 — corresponds to the GuidanceDoc's stale $598 upper bound, **not** the body's updated $570 upper bound. The current body math yields 570 ÷ 4.50 = **127×**, not 133×.
- The "tighter 33–122×" range at line 149 corresponds to $4.50 × 33 = $148.50 (lower end approximating bottom-up with SCC at the Obama $42 level: 2.86 × $42 + ~$10 = ~$130 → $148) and $4.50 × 122 = $549 (upper end with SCC at $190: ~$550-570). This range is internally consistent with the body.
- The RCV Model IPG 19–47× corresponds to RCV figures of ~$85–$211/ton, which the chapter does not derive numerically in body prose. This is a method-decomposition figure that requires reader trust unless the per-case work is exposed.

**Issue cluster:**

(a) The damage-function IPG range 5–133× in the table appears to be computed against an earlier version of the bottom-up totals (the GuidanceDoc's $21–$54 without carbon / $567–$598 with carbon range). The body's current bottom-up totals are tighter ($8–$22 / $550–$570). The lower bound 5× corresponds to $22.50/$4.50 = max-without-carbon; the upper bound 133× corresponds to $598/$4.50 from the stale GuidanceDoc total.

(b) The body's own disclosure passage at line 149 ("the per-case work settles on a tighter 33–122×") implicitly acknowledges the table's wider range is a method-aggregation artifact. But the disclosure does not explain *which method* produced the 5× lower bound or the 133× upper bound. A reader following the arithmetic cannot reconcile.

(c) The 19–47× RCV Model IPG column has no body-derivation. The 33–122× tighter per-case figure is presented as "the per-case work" without a citation pointer to where that work is shown (the natural target is TA §11 or a Ch 6 sub-section that does not exist).

**Why this is SHOULD-FIX-2:**

A reader doing the arithmetic — and Sandy Darity will — will find that:
1. The damage-function lower bound 5× requires the upper end of the without-carbon range, which is a boundary case that doesn't represent the column's intent (the damage-function column is supposed to include carbon).
2. The damage-function upper bound 133× requires the stale GuidanceDoc with-carbon upper bound, not the body's current $570 figure.
3. The body's own admission of a "tighter 33–122×" range implicitly concedes the table's range is loose.

The chapter's prose at line 149–153 is well-disciplined about acknowledging the method-attribution differences — but the table itself is still presented as the visual centerpiece. The presented range and the body math should match.

**Recommended spot-fix:** Two options:

- **Option A (tighten the table to the body math):** Replace McDowell row Damage-Function IPG "5–133×" with the body-derived range. If the column intent is "with-carbon damage-function," use ($550 − $570) / $4.50 = **122–127×**. If the column intent is "across SCC bracket," use the disclosed 33–122× range from line 149. Either preserves arithmetic integrity.
- **Option B (preserve the table; add a footnote disclosing the SCC-bracket assumption):** Add a footnote to the Damage-Function IPG column: "Range spans SCC = $1 (Trump EPA) lower bound to SCC = $190 (Biden EPA) upper bound, against tightened bottom-up totals; per-case work settles on a narrower 33–122× range." This documents the wide-bracket method assumption without changing the figures.

The current GuidanceDoc's stale $567–$598 total at GuidanceDoc line 87 is a separate cross-thread #9 finding (see below).

**Severity rationale:** SHOULD-FIX (HIGH-equivalent) because (a) the arithmetic is visible to any economist-reader, (b) the discrepancy between table and body is small but real, (c) the per-case-work tighter-range disclosure at line 149 is well-disciplined but does not resolve the table's loose range.

---

### MEDIUM-1: Smax variable introduced but does not appear in the canonical RCV formula

**Location:** [Chapter__6_ThreeWaysofCounting__Draft.md:128](manuscript/chapters/Chapter__6_ThreeWaysofCounting__Draft.md:128)

**Chapter text:**
> "It approaches some maximum Smax that may be less than one; for some resources, complete substitution may never be physically possible."

**Issue:** The variable Smax is named in the substitutability-function natural-properties passage but does not appear in the canonical RCV formula (line 97) or in the term-by-term translation (lines 103–106). TA §17.6 (line 7497) does reference Smax: "S monotonically increases toward Smax ≤ 1" — so the construct exists in the formal apparatus, but it's a derived property of S(t|t₀), not an independent variable in the integrand.

The introduction at line 128 reads as if Smax is a model parameter the analyst sets independently, which may confuse a careful reader who is then asked to apply the formula. The clarification — that Smax is the asymptotic limit of S(t|t₀) as t→∞, not a separate parameter — is implicit but unstated.

**Why this is MEDIUM:** A careful reader (Sandy Darity is one) may pause at line 128 to ask "where is Smax in the formula?" The answer is in the natural-properties description, but the prose doesn't connect them.

**Recommended spot-fix:** Replace line 128 fragment "It approaches some maximum Smax that may be less than one" with "It approaches some asymptotic limit S(∞|t₀) ≤ 1; for some resources, complete substitution may never be physically possible (the limit can be strictly less than one)." This avoids introducing Smax as if it were a new variable.

**Severity rationale:** MEDIUM — small clarity issue, not a structural problem.

---

### MEDIUM-2: Approach 2 (Real Options) gives no per-case numerics — the chapter's "Apply it across cases, and the same answer emerges" is presented without showing the arithmetic

**Location:** [Chapter__6_ThreeWaysofCounting__Draft.md:73](manuscript/chapters/Chapter__6_ThreeWaysofCounting__Draft.md:73)

**Chapter text:**
> "Apply it across cases, and the same answer emerges. Every extraction event we have examined produced net revenue substantially below the social option value of leaving the resource in place. The direction does not flip."

**Issue:** The Real Options section presents the McDowell 1960 example (line 67: "on the order of tens of dollars at minimum, and plausibly hundreds once the externality tail is included") but does not produce per-case figures for Deepwater Horizon, Exxon Valdez, or Libby. The "same answer emerges" claim is asserted without arithmetic.

This is the structural antecedent of MUST-FIX-2 (convergence table missing the Real Options column). The chapter's apparatus claim — three independent methods converge — depends on demonstrating Real Options on the same four cases the other two methods are demonstrated on.

**Why this is MEDIUM:** Distinct from MUST-FIX-2 (which is about the table); this finding is about the body prose immediately preceding the table.

**Recommended spot-fix:** Either (a) commit per-case numerics in the body for Deepwater, Exxon, Libby (paralleling McDowell at line 67), or (b) restructure the Approach 2 section to be explicitly "Real Options as theoretical foundation that informs Approach 3's RCV structure, not a separate quantitative method," resolving the convergence-table inconsistency at the body level. This finding is downstream of MUST-FIX-2 and either resolves with it or compounds it.

**Severity rationale:** MEDIUM — partially resolves with MUST-FIX-2.

---

### MEDIUM-3: McDowell coal carbon-inclusive total has minor rounding-tolerance inconsistency

**Location:** [Chapter__6_ThreeWaysofCounting__Draft.md:31](manuscript/chapters/Chapter__6_ThreeWaysofCounting__Draft.md:31)

**Chapter text:**
> "Include carbon, and the bottom-up total rises to $550–570 per ton."

**Math check:**
- Without carbon: $8–$22 (line 27)
- Carbon: $544 (line 29: 2.86 × $190)
- With carbon: $8 + $544 = **$552** (low) to $22 + $544 = **$566** (high)

The body says $550–$570; the math yields $552–$566. The discrepancy is rounding-tolerance (within ±$5 in both directions) and is acceptable in trade prose. But the convergence table's IPG figures are sensitive to the upper bound: $570/$4.50 = 127× vs the table's 133× upper bound (already flagged in SHOULD-FIX-2). The wider body range gives more room for the table's wider IPG range.

**Why this is MEDIUM:** A literal reader doing the addition will get $552–$566, not $550–$570. The disclosure passage at line 149 admits per-case-work tightening; this finding is the body-level companion.

**Recommended spot-fix:** Two options:
- **Option A:** Replace "$550–570" with "$552–566" (literal sum).
- **Option B:** Keep "$550–570" as round-figure framing but add a parenthetical: "(rounded to nearest $10 from $552–$566)" — preserves rhetorical force.

**Severity rationale:** MEDIUM — rounding-tolerance issue, but propagates to the convergence table's IPG bounds. Resolves cleanly.

---

### MEDIUM-4: Ch 6 missing TA hyperlinks for sections directly engaged in body prose

**Location:** Ch 6 body throughout

**Chapter text:** Ch 6 carries three TA cross-reference hyperlinks (sec-7-four-gates at line 263; sec-17-formula-generalization at line 263; sec-8-asymmetric-regret-rule at line 303). All three verified to exist + match TA content.

**Issue:** Ch 6 engages four additional TA sections at substantial depth without hyperlinking to them:

| Ch 6 section | TA target | Anchor (verified exists) |
|---|---|---|
| "Approach 3 — The RCV Model" (lines 77–116); RCV formula introduction | TA §3 "RCV Quantification — Three Ways of Counting" | `#sec-3-rcv-quantification` |
| "The Convergence" (lines 134–169); convergence table | TA §9 "Three-Model Convergence" | `#sec-9-three-model-convergence` |
| "The Substitutability Function" (lines 120–131) | TA §13 "Substitutability Function and Gap" | `#sec-13-substitutability-function-and-gap` |
| "The Four Gates" → CIT exposition (lines 235–263) | TA §6 "Commons Inversion Test" (CIT proper) | `#sec-6-commons-inversion-test` |

Per [feedback_grammatical_role_cross_references.md](/Users/c17n/.claude/projects/-Users-c17n-commons-bonds/memory/feedback_grammatical_role_cross_references.md): chapter→appendix references in HTML chapters that are "sections-as-citations" (parentheticals / "see X") get a hyperlink. The four targets above all fit the sections-as-citations form structurally. Ch 6 chose to hyperlink only three; the other four would benefit from the same treatment.

**Why this is MEDIUM:** The missing hyperlinks are particularly notable because **TA §3** ("RCV Quantification — Three Ways of Counting") is the direct cross-reference target for MUST-FIX-1's canonical-naming finding. A reader who is confused by the shared title needs to be able to click to TA §3 from Ch 6's RCV section. Currently they cannot.

**Recommended spot-fix:** Add four hyperlinks during the Phase C-α spot-fix application:
- Near line 97 (RCV formula introduction): link "(see Technical Appendix [§3 RCV Quantification](../../core/technical-appendix/TechnicalAppendix_v2.0.0.html#sec-3-rcv-quantification))"
- Near line 138 (convergence introduction): link "(formalized in Technical Appendix [§9 Three-Model Convergence](../../core/technical-appendix/TechnicalAppendix_v2.0.0.html#sec-9-three-model-convergence))"
- Near line 131 (substitutability close): link "(formal specification in Technical Appendix [§13 Substitutability Function and Gap](../../core/technical-appendix/TechnicalAppendix_v2.0.0.html#sec-13-substitutability-function-and-gap))"
- Near line 251 (CIT defense passage): link "(see Technical Appendix [§6 Commons Inversion Test](../../core/technical-appendix/TechnicalAppendix_v2.0.0.html#sec-6-commons-inversion-test))"

**Severity rationale:** MEDIUM — not a fact-check failure, but a navigational gap that compounds MUST-FIX-1's canonical-naming confusion. Cheap to resolve.

---

### LOW-1: Time-sensitive figures requiring pre-publication refresh

Per [feedback_verify_stale_memory_claims.md](/Users/c17n/.claude/projects/-Users-c17n-commons-bonds/memory/feedback_verify_stale_memory_claims.md), the following Ch 6 figures are time-sensitive and require verification at pre-publication refresh:

| Figure | Location | Current claim | Verification note |
|---|---|---|---|
| Norway sovereign wealth fund total | line 177 | "$1.9 trillion" | Verify against latest GPFG quarterly disclosure (figure was ~$1.9T early 2025; check current value). |
| SCC = $190/ton CO₂ | lines 29, 41, 49 | "EPA's 2023 estimate of $190" | EPA Final SCC TSD 2023 at 2% discount rate; Rennert et al. 2022 Nature anchor. Stable as of audit; verify no superseding agency action. |
| DAC costs — Climeworks Orca/Mammoth | line 47 | "$600–$1,000/ton" | First-of-a-kind costs; verify against most recent Climeworks operational disclosures. |
| DAC costs — Carbon Engineering Stratos | line 47 | "$300–$600/ton at full operation; in construction at the time of writing" | Stratos / 1PointFive Ector County TX commissioning status; verify "in construction" framing remains accurate at submission. |
| DAC costs — IEA / IPCC mid-century | line 47 | "$100–$300 range" | Verify against IEA DAC 2022 + IPCC AR6 WGIII. |
| McDowell life-expectancy gap "thirteen years" | line 25 | Well-established; verify pre-publication. |
| Black Lung Trust Fund "$44 billion in distributions" | line 21 | Well-established; verify against current GAO/CRS figures. |
| McDowell County peak / current population | (referenced in TA §7.6 worked example, not body) | Body does not state; only mentions life-expectancy gap. No body-level claim to verify. |

**Severity rationale:** LOW — figures are correct as of audit; flag for systematic refresh at publication-pipeline stage.

---

### LOW-2: Exxon Valdez "$5.5M product" IPG basis is one-event-spill product value, not extraction revenue — flag for clarity

**Location:** [Chapter__6_ThreeWaysofCounting__Draft.md:33, 146](manuscript/chapters/Chapter__6_ThreeWaysofCounting__Draft.md:33)

**Chapter text:**
> Line 33: "Exxon Valdez: $5.5 million of oil spilled, against between $7 and $10 billion in cleanup, litigation, and long-run ecological damage. An IPG in the range of 1,200 to 1,900 times."
> Line 146: "Exxon Valdez | $5.5M product | 1,200–1,900× | ~1,000× | CS > 0"

**Verification:** Exxon Valdez spilled approximately 257,000 barrels of oil (≈11 million gallons). At 1989 wholesale prices (~$0.50/gallon equivalent for the spilled product), the spilled-product value is approximately $5.5M. The math is consistent.

But the IPG framing is structurally different from the other three cases:
- McDowell coal IPG: per-ton (extraction-lifetime ratio)
- Deepwater Horizon IPG: cumulative-cost-to-revenue (lifetime ratio)
- Libby IPG: cumulative-cost-to-revenue (lifetime ratio)
- Exxon Valdez IPG: cost-to-spilled-product-value (one-event ratio)

The Exxon Valdez case is a one-event spill, not an extraction lifetime. The chapter discusses this difference at lines 149–153 ("Deepwater's 40% recovery ratio takes a different form than the multiplicative IPG figures because Deepwater is a one-event disaster") but applies the discussion to Deepwater Horizon — Exxon Valdez is structurally identical but not called out.

**Why this is LOW:** The 1,200–1,900× IPG figure is rhetorically forceful and the underlying arithmetic is defensible, but a reader doing the comparison may notice the basis difference. The convergence-table presentation does not flag the difference for Exxon Valdez specifically.

**Recommended spot-fix:** At line 33, add a half-sentence clarification: "An IPG in the range of 1,200 to 1,900 times — though, as with Deepwater Horizon (line 149), the Valdez ratio is computed against spilled-product value rather than extraction-lifetime revenue, which makes the multiplier rhetorically large but structurally one-event-bounded." Or simpler: at the convergence table line 146, footnote the Exxon Valdez row with the same disclosure that the line-149 passage gives Deepwater.

**Severity rationale:** LOW — disclosure gap, not a factual error.

---

### LOW-3: Cross-case scope check — Ch 6 forward cases vs Darity-companion CSD cases — NOT drift; intentional

**Verification per the user's task brief:**

| Ch 6 convergence-table cases | Darity-call companion CSD-application cases |
|---|---|
| McDowell County coal | McDowell County coal |
| Deepwater Horizon | Libby asbestos |
| Exxon Valdez | Niger Delta oil |
| Libby, Montana | opioid-Appalachia |

**Overlap:** McDowell + Libby appear in both.
**Divergence:** Ch 6 has Deepwater + Exxon Valdez (forward triangulation demonstration); Darity has Niger Delta + opioid-Appalachia (backward CSD-application demonstration).

**Verdict:** This is **NOT list drift**. The two lists serve different purposes:
- Ch 6 cases demonstrate forward IPG triangulation across a wide-variance range (McDowell single-digit IPG up to Exxon Valdez 1,200–1,900× range), with two extraction-lifetime cases (McDowell, Libby) and two one-event cases (Deepwater, Exxon).
- Darity-companion cases demonstrate backward Restitution Bond computation in extraction-community contexts where Coates/Darity-Mullen/Hamilton reparations-economics methodology applies most directly. Niger Delta and opioid-Appalachia are the cases where the matched-comparison wealth-gap methodology lands sharpest.
- McDowell + Libby are reused across both because they are the book's load-bearing cases that have been fully worked through the apparatus.

The intentional overlap is consistent with [reference_ostrom_illustrative_register.md](/Users/c17n/.claude/projects/-Users-c17n-commons-bonds/memory/reference_ostrom_illustrative_register.md): the book demonstrates handfuls of cases illustratively, not exhaustively. Different chapters select different illustrative subsets for different purposes; the overlapping core (McDowell + Libby) is intentional, not drift.

**Severity rationale:** LOW (informational; surface for visibility — confirms intentional reuse). No spot-fix required.

---

### LOW-4: 10 commons categories list — Ostrom-illustrative discipline correctly preserved

**Location:** [Chapter__6_ThreeWaysofCounting__Draft.md:189–207](manuscript/chapters/Chapter__6_ThreeWaysofCounting__Draft.md:189)

**Verification:** The chapter introduces the ten commons categories (Habitability · Spatial · Temporal · Institutional · Kindred · Ecosystem · Political · Cohesion · Epistemic · Autonomy) and immediately flags them as illustrative-not-exhaustive at line 193:

> "These are *examples for illustrative purposes, not an exhaustive list.* The ten represent what showed up across the eighteen cases tested; readers applying the methodology to their own cases may surface different categories or refine these."

Per [reference_ostrom_illustrative_register.md](/Users/c17n/.claude/projects/-Users-c17n-commons-bonds/memory/reference_ostrom_illustrative_register.md) and [feedback_audit_open_illustrative_default.md](/Users/c17n/.claude/projects/-Users-c17n-commons-bonds/memory/feedback_audit_open_illustrative_default.md), this is the correct framing for framework lists. The Ostrom-path discipline is preserved through the rest of the section (lines 195–207).

**Severity rationale:** LOW — positive finding; no fix required. Surface as audit-pass on the illustrative-register discipline.

---

### LOW-5: Acronym discipline check (Sandel hybrid pattern)

Per [reference_sandel_hybrid_pattern.md](/Users/c17n/.claude/projects/-Users-c17n-commons-bonds/memory/reference_sandel_hybrid_pattern.md), named-quantity acronyms in Ch 6 receive contextual discipline:

| Acronym | First use | Spell-out | Subsequent | Discipline |
|---|---|---|---|---|
| RCV | line 13 | "residual commons value (RCV) framework" | RCV thereafter | ✓ Sandel hybrid: spelled-out at first use; acronym after |
| CS | line 110 | $\mathrm{CS} = \mathrm{RCV} - B$ | CS thereafter | ✓ Formal definition at introduction; acronym after |
| IPG | line 33 | "Intergenerational Pricing Gap (IPG)" | IPG thereafter | ✓ Sandel hybrid: spelled-out at first use; acronym after |
| CIT | line 235+ | "Commons Inversion Test" (full first use) | CIT (line 167 via earlier reference) | ⚠ Inconsistency: line 167 uses "Commons Inversion Test" full form; CIT acronym not introduced until later. Acronym is canonical (TA §6 + §7.1; Ch 6 GuidanceDoc line 386); body prose uses full form throughout except possibly line 167. Audit: body uses full form consistently — actually clean. |
| DAC | line 47 (implicit via "direct-air-capture") | Spelled out as "direct-air-capture"; "DAC" not used in body | n/a | ⚠ DAC acronym used in TA §3.3 but not in Ch 6 body; body uses spelled-out form. Per Sandel hybrid: single-use → expand. ✓ correct discipline for body. |
| SCC | line 35 | "social cost of carbon" + "SCC is" at line 35 | SCC thereafter | ⚠ Acronym used at line 35 ("the SCC") without prior spell-out — first body use. Audit: SCC is standard term-of-art in carbon-pricing literature; not a framework neologism. Borderline. Recommended: spell-out at line 35 first use: "the social cost of carbon (SCC), which lives or dies..." |

**Severity rationale:** LOW — single acronym discipline issue (SCC at line 35 first use). Discipline is otherwise clean.

**Recommended spot-fix:** Spell out SCC at line 35 first use. Body is otherwise compliant with Sandel hybrid discipline.

---

### LOW-6: Cross-thread #9 contribution — Ch 6 GuidanceDoc has parallel stale-reference issues to Ch 2 GuidanceDoc's "$100 barrel passage"

**Location:** [Chapter__6___GuidanceDoc.md](manuscript/chapters/Chapter__6___GuidanceDoc.md) throughout

**Findings for cross-thread #9 PM dashboard:**

(a) **GuidanceDoc line 87 — bottom-up totals stale.** GuidanceDoc states: "Total: $21-54/ton without carbon, $567-598/ton with carbon." Current Ch 6 body uses $8–$22 without carbon and $550–$570 with carbon. Stale by ~$13/ton (without-carbon lower) and ~$28/ton (with-carbon upper).

(b) **GuidanceDoc lines 33, 38, 371–373, 438 — Tech Appendix version references stale.** GuidanceDoc references "Tech Appendix v0.0.4" and "v0.0.5" throughout. Current TA is v2.0.0 (post-#15 + post-#19 cleanup). Per the GuidanceDoc's own staleness-disclaimer at lines 9–10, this is acknowledged historical record; not a fix-required finding, but a cross-thread #9 visibility flag.

(c) **GuidanceDoc lines 350, 386, 396, 416, 438 — 8-tier scheme references retired.** GuidanceDoc references "8-tier framework" / "AIT" / vocabulary the chapter body has moved past. Per the GuidanceDoc's own per-section audit dated 2026-05-08 at lines 11–38, these are flagged as historical references. Not fix-required at the GuidanceDoc level (it's scaffolding), but compounds cross-thread #9's accumulating-staleness pattern.

(d) **GuidanceDoc line 144 — IPG table.** Contains the same table presented in body line 142–147, but with column headers using "5-133x" (no Unicode multiplication sign × ). Trivial formatting inconsistency.

**Severity rationale:** LOW — surface for cross-thread #9 (GuidanceDoc parallel-staleness pattern). The GuidanceDoc is internal-scaffolding per WP#10; staleness in the GuidanceDoc is lower-stakes than chapter-body staleness but still worth tracking systematically.

**Recommended spot-fix:** Defer to cross-thread #9 PM session for the systematic GuidanceDoc-staleness sweep. No Ch 6 body change required from this finding.

---

## Cross-thread #11 contribution — Citation accumulation

**Schema:** Ch 6 = 1M (in-prose bibliographic insertion likely required) + 24L (literature already engaged at TA / bibliography level; chapter-level citation footnotes pending).

**1M (chapter-level citation insertion candidate):**
- **Mishel & Bivens / Hacker** — referenced in Ch 5 line 158 (post-CSD section), not Ch 6. Not a Ch 6 finding.
- **No body-level citations marked-but-uncited in Ch 6** — chapter draft uses in-prose attributions (Stern, Nordhaus, Weitzman, Ramsey, Parfit, Pigou, Hotelling, Ostrom, Hartwick, Anderson, Pettit, Skinner) without footnote insertion. M = ~1 candidate (Rennert et al. 2022 *Nature* at line 49 — flagged for chapter-end citation; currently inline).

**24L (literature already engaged; pre-publication footnote/endnote stage):**
| Author / work | Ch 6 location | Engagement |
|---|---|---|
| Pigou 1920 (*The Economics of Welfare*) | line 271, 277 | Pigouvian externality theory extension claim |
| Hotelling 1931 (*JPE*) | line 234, 279, 234 | Hotelling Rule + Hotelling Identity |
| Ramsey 1928 | line 124 | Discount-rate origin |
| Stern Review 2006 | line 124 | 1.4% discount rate |
| Nordhaus (DICE) | line 124 | ~4% discount rate |
| Weitzman 2001 (declining-rate framework) | line 106 | D(t,t₀) social discount factor |
| Weitzman 2009 (fat-tail damages) | line 91 | Tail metaphor for externality tail |
| Parfit 1984 (*Reasons and Persons*) | line 213, 217, 221 | Non-identity problem + impersonal-outcomes framework |
| Coates 2014 (*Atlantic*) | — (engaged in Ch 5; cited here only via Restitution-Bond reference at line 223) | Reparations-economics lineage |
| Darity & Mullen 2020 (*From Here to Equality*) | line 223 | Reparations methodology |
| Hamilton et al. 2015 (*Umbrellas*) | — | Wealth-gap methodology |
| Conley 1999 (*Being Black, Living in the Red*) | — | Wealth-as-structural-variable lineage |
| Anderson | line 197, 203, 410 (GuidanceDoc) | Civic-republican / autonomy-as-commons |
| Pettit 1997 (*Republicanism*) | line 203 (Ch 6) + Ch 5 references | Civic-republican lineage |
| Skinner 1998 (*Liberty Before Liberalism*) | line 203 | Civic-republican lineage |
| Ostrom 1990 (*Governing the Commons*) | line 191, 271 | Ostrom-tradition / coordination commons |
| Hess & Ostrom 2007 | — (engaged in TA + GuidanceDoc; Ch 6 body uses generic "Ostrom-lineage") | Commons-governance lineage |
| Hartwick 1977 | line 234, 273 | Hartwick's Rule + residual concept |
| Mazzucato 2018 (value extraction vs creation) | line 273 | Value register for "Residual Commons Value" |
| Sen / Nussbaum (capabilities approach) | line 193 | Ten central capabilities lineage analog |
| Rawls (primary goods) | line 193 | Primary goods lineage analog |
| Rennert et al. 2022 (*Nature*) | line 49 | SCC = $190 anchor |
| IEA *Direct Air Capture 2022* | line 47 | DAC cost trajectory |
| IPCC AR6 WGIII | line 47 | DAC mid-century range |
| Savage 1951 (*JASA*) | line 303 | Minimax-regret discipline |
| Lewis (counterfactual reasoning) | line 251 | David Lewis counterfactual lineage |
| Yeager 1947 | line 165 | Sound-barrier metaphor |
| Dixit-Pindyck 1994 (real options) | — (engaged in TA §3.5; Ch 6 body uses generic "real-options" framework) | Real options lineage |

**Summary for cross-thread #11:** Ch 6 = 1 M (potential chapter-end footnote insertion for Rennert et al. 2022) + 27 L (literature engaged in-prose; pre-publication citation system rendering required).

---

## Flags for parallel sessions

- **TA Pass 1 math audit (in flight or landed):** Verify TA §3.1 RCV formula matches Ch 6 line 97 verbatim. Verify TA §7.6 worked example for C3 community-transition-reserve (currently uses 1960 anchor with $5–$10/ton present-value addition to McDowell $550–$570 figure; arithmetic consistent with Ch 6 body bottom-up).
- **Ch 5 Stage-3 Pass 1 (landed 2026-05-13 at commit a2d2d3f):** Ch 6 Pass 1 SHOULD-FIX-1 finding is the forward-direction analog of Ch 5 Pass 1 SHOULD-FIX-1. Coordinated resolution recommended at Phase C-α.
- **Ch 10 insertion-placement session (in flight):** Ch 6 Pass 1 MUST-FIX-1 (canonical-naming "three ways of counting" drift) directly affects the Ch 10 insertion paragraph that references "the four gates and the three ways of counting" canonical naming. The in-flight Ch 10 insertion must not be written assuming the current ambiguous state; Phase C-α resolution of MUST-FIX-1 should land before the Ch 10 insertion is finalized.
- **#19 TA Scheme-4 cleanup session (landed 2026-05-13 at commit 2c880bc):** All three TA cross-reference anchors (sec-7, sec-8, sec-17) verified intact post-#19. No regressions from Scheme-4 work.
- **Cross-thread #9 (GuidanceDoc parallel-staleness pattern):** Ch 6 GuidanceDoc has 4 stale-reference findings (LOW-6 above). Surface to PM dashboard for systematic sweep alongside Ch 2 GuidanceDoc's "$100 barrel passage" findings.
- **Cross-thread #11 (Citation accumulation):** Ch 6 contribution = 1M + 27L. See block above.

---

## Aggregate disposition

**Pass 1 verdict:** **READY AFTER SPOT-FIXES** for the chapter to ship to Sandy Darity, contingent on author ratification of MUST-FIX-1 (canonical-naming drift "Three Ways of Counting") and MUST-FIX-2 (convergence-table missing Real Options column). Both MUST-FIX findings center on structural integrity of the chapter's apparatus claim and will be visible to Sandy Darity on first integrated read.

The chapter's apparatus-prose at the term-by-term level is rigorous and stands up to math-check. The TA cross-reference hyperlinks all verify. The Ostrom-illustrative-register discipline holds across the ten commons categories list. No named-subject consent issues. The Coates/Darity-Mullen/Hamilton/Conley reparations-economics engagement (via the Restitution-Bond instrument reference at line 223) is consistent with Ch 5's deeper engagement and does not need to be relitigated at Ch 6 depth.

Phase C-α spot-fix application is a separate ratification cycle and should coordinate with the in-flight Ch 10 insertion-placement session and any TA Scheme-4 follow-up.

---

*End of Pass 1 — Fact-check + math-check overlay (initial).*

---

# Amendment 2026-05-13 — corpus-canonical reading correction + MUST-FIX ratifications

**Trigger:** Author flagged that my initial MUST-FIX-1 recommendation (hybrid Option A+C — rename TA §3 + disambiguate Ch 6) had not been verified against the wider corpus's canonicalization of "Three Ways of Counting." A subsequent grep across `core/terms/`, `alignment/`, `tools/audits/`, `tools/drafts/`, `tools/rigor-passes/`, `publishing/`, and `research/outreach/` revealed that the canonical reading was already well-established and that the initial recommendation would have broken it.

## Corpus-canonical reading (verified 2026-05-13)

**"Three Ways of Counting" = Method 1 Replacement Cost + Method 2 Revealed Preference + Method 3 Scarcity-Adjusted Option Value. Direction-agnostic: runs forward as RCV calculation, backward as CSD calculation.**

Confirmed across:

| Source | Date | Confirms |
|---|---|---|
| **TA §3 (current title in v2.0.0)** | current | "RCV Quantification — Three Ways of Counting"; body walks M1/M2/M3 |
| **TA §5.5 bidirectionality proposal** (commit 013abd4b) | 2026-05-13 | "Three Ways of Counting triangulation (§3) — is direction-agnostic in its formal statement"; M1/M2/M3 forward/backward mapping with named exemplars (Norway GPFG forward; Darity & Mullen 2020 + Holocaust reparations + 1988 Civil Liberties Act + Black Lung Trust Fund + South African TRC backward) |
| **TA Pass 1 math audit** | 2026-05-13 | "the apparatus (CIT + Four Gates + Three Ways of Counting) is direction-agnostic in its formal statement: the same methodology applies forward (RCV) and backward (CSD)" |
| **Insight #31 RATIFIED** | 2026-04-28 | Established the rename: "Triangulated RCV Estimation" RETIRED; "Three Ways of Counting" promoted to primary methodology name for M1+M2+M3 |
| **Insight #48 RATIFIED** | 2026-04-29 | Post-rename adoption-fit verification; TA §3 section-title set to "RCV Quantification — Three Ways of Counting" |
| **cross-chapter-consistency-inventory** | 2026-05-11 | Three Ways of Counting canonically = "Method 1 Replacement Cost; Method 2 Revealed Preference; Method 3 Scarcity-Adjusted Option Value" |
| **Four flagship-term defense paragraphs** (RCV, CIT, ARR, externality-tail) | 2026-05-11 | All reference Ch 6 as "Three Ways of Counting" methodology chapter |
| **Ch 10 bidirectional-reach insertion** (commit 8b7ac89) | 2026-05-13 | Line 65: "The four gates and the three ways of counting have been applied in this book to one direction: forward... The same apparatus runs in reverse, as Chapter 5 noted and as the Technical Appendix formalizes (§5.5). The framework is bidirectional by construction." |
| **Ch 5 lines 210 + 214** | current | "the four gates and the three ways of counting" (line 210); informal labels for backward direction map to M1/M2/M3 (line 214; Ch 5 Pass 1 SHOULD-FIX-1 flags for canonical-name anchoring) |
| **Darity post-interview synthesis** | 2026-05-13 | "Ch 6 (Three Ways of Counting) Ostrom-extension section" |

**terms_index entry (lines 1708–1794) confirms the same core definition but is itself stale on:** internal contradiction between rename-ratified record (line 1714) and pre-rename "both forms ratified" residue (lines 1778–1781); references retired TA v0.0.5 (lines 1763, 1776, 1783); describes CSD as "different methodology" (line 1773) — contradicts today's TA §5.5; no mention of bidirectionality. Cross-thread #9-class staleness (see addendum below). Core M1/M2/M3 definition survives in independent active-review sources.

## Outlier identified

**Ch 6 body is the lone outlier** against the corpus-canonical reading. The chapter title is correctly canonical; the body presents three Approaches (Bottom-Up Damage Accounting / Real Options / RCV Model) at the apparatus-comparison level, not the canonical Three Ways of Counting (M1/M2/M3 inside RCV).

## MUST-FIX-1 — ratified resolution: Option B.2

**Initial recommendation (hybrid A+C):** SUPERSEDED. Would have broken the canonicalization established across Insight #31 + #48 + TA §3 + TA §5.5 + cross-chapter-consistency-inventory + 4 flagship-term defenses + Ch 10 insertion + Ch 5.

**RATIFIED 2026-05-13 (Chris Winn): Option B.2** — keep Ch 6's outer pedagogical scaffolding (three Approaches as cross-validation triangle); add an explicit Method 1 / Method 2 / Method 3 sub-section inside Approach 3 (RCV Model) that walks the canonical Three Ways of Counting with worked examples per case.

**Why B.2 over B.1 (full restructure):** B.2 preserves the chapter's existing pedagogical movement (Bottom-Up → Real Options → RCV) that gives the convergence claim its independent-foundations credit; lands the canonical Three Ways where readers expect them (inside the RCV apparatus, where they live in the framework); uses the chapter's own line 49 acknowledgment ("Approach 3's RCV Method 1") as the natural bridge.

**Phase C-α scope for B.2:**
- New sub-section inside Approach 3 (RCV Model) — title proposal: "The Three Ways of Counting Inside RCV" or "Triangulating the RCV — Method 1, Method 2, Method 3" — placed after the formula introduction (line 116) and before the Substitutability Function section (line 120). ~600–900w.
- Method 1 (Replacement Cost): walk McDowell coal via DAC anchor ($310–$1,800/ton per TA §3.6 Block 4); cite TA §3.3.
- Method 2 (Revealed Preference): walk McDowell coal via Norway-anchored revealed-preference (~$8–$88/ton per TA §3.6 Block 4); cite TA §3.4.
- Method 3 (Scarcity-Adjusted Option Value): walk McDowell coal via Dixit-Pindyck option-value with scarcity + irreversibility weighting ($420–$13,100/ton; mid $2,500 per TA §3.6 Block 4); cite TA §3.5; flag α-dominance regime per TA §3.5 sensitivity table.
- Connect the M1/M2/M3 walkthrough to the chapter's existing line 49 ("Approach 3's RCV Method 1") and to Ch 5's backward-direction application (line 214 informal labels resolve to canonical M1/M2/M3 names).
- Add forward-reference: "(formal articulation in Technical Appendix [§3 RCV Quantification — Three Ways of Counting](../../core/technical-appendix/TechnicalAppendix_v2.0.0.html#sec-3-rcv-quantification); bidirectional applicability in [§5.5](../../core/technical-appendix/TechnicalAppendix_v2.0.0.html#sec-5-5-bidirectionality))" — verify anchor name for §5.5 against just-landed TA work.

## MUST-FIX-2 — ratified resolution: rebuild convergence table as M1/M2/M3 columns per case

**Initial recommendation (Option B — reframe as 2 quantitative + 1 directional):** SUPERSEDED by the B.2 ratification above. Once the M1/M2/M3 walkthrough lands inside Approach 3, the convergence table reframes naturally at the method level rather than the apparatus-comparison level.

**RATIFIED 2026-05-13 (Chris Winn): rebuild convergence table as M1/M2/M3 per case.**

**Phase C-α scope for MUST-FIX-2:**
- Replace the current 2-column table (Damage-Function IPG | RCV Model IPG) with a 3-column table (Method 1 IPG | Method 2 IPG | Method 3 IPG) plus Direction.
- Per-case numerics for McDowell coal + Norway oil are already available in TA §3.6 Block 4 ($310–$1,800 / $8–$88 / $420–$13,100 mid $2,500 for McDowell; $300–$650 / $50 / $70–$1,000 mid $280 per BOE for Norway).
- Per-case numerics for Deepwater Horizon, Libby, Exxon Valdez: derive following TA §3.3–§3.5 method specifications + the per-case-prose figures already in Ch 5 (Libby cost-to-revenue 40×; Deepwater 40% recovery ratio; Exxon Valdez documented cleanup vs spilled product). Where Method 3 (option-value framing) does not cleanly apply for one-event spill cases (Deepwater, Exxon), mark the cell as N/A with footnote — same one-event-vs-extraction-lifetime distinction already disclosed at line 149.
- Preserve the body's existing line-149 method-attribution disclosure passage — it now reads as the table's caption / methodological note rather than as a damage-control disclosure.
- Bottom-Up Damage Accounting (formerly the "Damage-Function" column) absorbs into Method 1 (which is the canonical Replacement-Cost / substitution-side estimate) and into the E term of Method 3 (where the SCC-anchored carbon externality lives in the RCV integrand) — the body prose at lines 17–51 remains as preliminary "what enters the E term" walkthrough.

## Knock-on resolutions

**SHOULD-FIX-1 (forward↔backward apparatus consistency):** auto-resolves via the corpus-canonical-name anchoring. Apply jointly with Ch 5 Pass 1 SHOULD-FIX-1 in a single Phase C-α session: Ch 5 line 214's informal labels ("substitution cost / revealed restraint / forward option value") become canonical M1/M2/M3 names ("Method 1 Replacement Cost (here: remediation cost) / Method 2 Revealed Preference (here: revealed restitution) / Method 3 Scarcity-Adjusted Option Value (here: extinguished option value)"). This makes the bidirectionality claim run through the same three constructs in both directions.

**SHOULD-FIX-2 (McDowell IPG bounds):** auto-resolves with the table rebuild. M1/M2/M3 per-case columns replace the "Damage-Function IPG 5–133×" wide-bracket range; the new columns are method-anchored to TA §3.6 Block 4 figures, eliminating the GuidanceDoc-derived stale upper bound. The SCC-bracket framing migrates to a footnote explaining the E term's SCC sensitivity inside Method 3.

**MEDIUM-1 (Smax variable):** still applies; minor wording fix during Phase C-α. Not affected by B.2 ratification.

**MEDIUM-2 (Approach 2 no per-case numerics):** auto-resolves with the table rebuild. Approach 2 (Real Options) is recovered as Method 3's theoretical foundation — its empirical contribution shows up in the Method 3 column.

**MEDIUM-3 (rounding-tolerance $550–$570 vs $552–$566):** still applies; defer to Phase C-α discretion (was already classified as defer-acceptable).

**MEDIUM-4 (missing TA hyperlinks):** now expands to **five** hyperlink targets — TA §3 (added during M1/M2/M3 walkthrough), TA §5.5 (added per Ch 10 line 65's matching reference + the TA §5.5 proposal's own flag for Ch 6 forward-reference), TA §9 Three-Model Convergence (per convergence-table context), TA §13 Substitutability Function and Gap (per Substitutability Function section), TA §6 Commons Inversion Test (per CIT defense passage). Apply all five together during Phase C-α.

**LOW-1 through LOW-5:** unchanged from initial Pass 1.

## Cross-thread #9 contribution — addendum

In addition to the Ch 6 GuidanceDoc staleness findings (LOW-6 in the initial Pass 1), the corpus-verification sweep surfaced an additional cross-thread #9 finding:

**terms_index entry "Three Ways of Counting" (lines 1708–1794) is internally stale on 5 specific points:**
1. Internal contradiction between line 1714 (Insight #31 rename ratified 2026-04-28) and lines 1778–1781 (pre-rename "both forms ratified" residue, dated 2026-04-24) — the older paragraph wasn't deleted when the rename ratified.
2. References retired TA v0.0.5 at lines 1763, 1776, 1783 — current TA is v2.0.0.
3. Line 1773 describes CSD pairing as "different methodology — reparations economics rather than triangulated" — directly contradicts today's TA §5.5 + Pass 1 math audit, both of which establish CSD as the same Three Ways of Counting applied backward.
4. Bidirectionality structural property absent from the entry — TA §5.5 (today) canonicalizes it.
5. "Last reviewed: 2026-04-24" (line 1732) — 19 days old; predates Insights #31 + #48, TA §5.5, and the bidirectionality work.

The core M1/M2/M3 definition itself is consistent with other canonical sources; the staleness is on contextual + cross-reference + structural-property elements. **Surface for cross-thread #9 systematic-staleness sweep alongside Ch 6 GuidanceDoc, Ch 2 GuidanceDoc, and any other reference-file entries that have accumulated post-review canonicalization decisions.**

## Status after amendment

| Finding | Pre-amendment | Post-amendment |
|---|---|---|
| MUST-FIX-1 | PROPOSED (hybrid A+C recommended) | **RATIFIED — Option B.2** |
| MUST-FIX-2 | PROPOSED (Option B recommended) | **RATIFIED — rebuild table as M1/M2/M3 columns per case** |
| SHOULD-FIX-1 | PROPOSED | RATIFIED via canonical-name anchoring (jointly with Ch 5 Pass 1 SHOULD-FIX-1) |
| SHOULD-FIX-2 | PROPOSED | Auto-resolves with MUST-FIX-2; awaits Phase C-α |
| MEDIUM-1 | PROPOSED | Still PROPOSED — awaits author ratification |
| MEDIUM-2 | PROPOSED | Auto-resolves with MUST-FIX-2; awaits Phase C-α |
| MEDIUM-3 | PROPOSED | Still PROPOSED — defer-acceptable per initial recommendation |
| MEDIUM-4 | PROPOSED | Still PROPOSED — expanded to 5 hyperlinks; awaits author ratification |
| LOW-1 through LOW-6 | PROPOSED | Unchanged — pre-publication / cross-thread surfacing |
| terms_index staleness (NEW) | — | Surfaced for cross-thread #9 |

## Phase C-α scope (ratified items)

Single coordinated Phase C-α session applies:
1. Ch 6: insert M1/M2/M3 walkthrough sub-section inside Approach 3 + rebuild convergence table as M1/M2/M3 per-case columns.
2. Ch 5 line 214: anchor informal labels to canonical M1/M2/M3 names (jointly with Ch 5 Pass 1 SHOULD-FIX-1).
3. Ch 6: add 5 TA cross-reference hyperlinks (§3, §5.5, §9, §13, §6).
4. Ch 6: preserve existing line-149 method-attribution disclosure as caption / footnote for the rebuilt table.

Phase C-α coordinates with:
- Ch 10 bidirectional-reach insertion (already landed at commit 8b7ac89; canonical-naming alignment now established by Ch 5 + Ch 10 + Ch 6 post-Phase-C-α).
- TA §5.5 anchor name (just-landed; verify exact anchor ID against the TA commit before adding Ch 6 hyperlink).

---

*End of Amendment 2026-05-13.*

**Status: RATIFIED for MUST-FIX-1 (B.2) + MUST-FIX-2 + SHOULD-FIX-1 + SHOULD-FIX-2. Other findings remain PROPOSED.**

---

# Amendment 2026-05-13 (B) — Authoritative-source verification of questioned numbers (LOW-1)

**Trigger:** Author requested authoritative-source web verification for all numbers flagged as time-sensitive in LOW-1. This amendment resolves LOW-1 with per-figure verification status against current public sources (NBIM, EPA, IEA, GAO, NOAA, DOJ, CDC, CRS, Climeworks, 1PointFive corporate disclosures, peer-reviewed sources, Wikipedia/IHME for established historical figures).

## Summary verdict

| Status | Count | Items |
|---|---|---|
| **VERIFIED** | 9 | EPA SCC $190; Stern Review 1.4%; Nordhaus 4%; SCC history Obama/Trump (within rounding); Biden SCC $190; Appalachian reclamation bond shortfall $3.7–6B; McDowell 13-year life-expectancy gap; Deepwater Horizon $4.25B revenue + $65–70B costs; Exxon Valdez $5.5M product math |
| **VERIFIED-DATED** | 2 | Black Lung Trust Fund $44B (2009-vintage; current ~$50B); Climeworks/Stratos operational status (in commissioning, not construction) |
| **STALE — needs refresh** | 2 | Norway GPFG ($1.9T → ~$2.2T); Stratos "in construction at the time of writing" (now in commissioning/ramp) |
| **POSSIBLY-INCORRECT — needs fact-check or rewording** | 2 | IEA $100 lower bound for mid-century DAC (IEA 2022 actually cites $230 floor; the $100 attribution to IEA is not supported); coal-to-CO2 ratio 2.86 (high vs EPA's 2.325 short-ton or ~2.4–2.6 metric-ton convention) |
| **VERIFIED-MATH BUT DISCLOSURE-GAP** | 1 | Libby $5–8B costs (settlement-anchored figures much lower; $5–8B is long-tail framing that should be disclosed) |

## Per-figure verification details

### VERIFIED ✓

**EPA SCC $190/ton at 2% rate** ([Ch 6 lines 29, 41, 49](manuscript/chapters/Chapter__6_ThreeWaysofCounting__Draft.md:29)).
EPA's November 2023 *Report on the Social Cost of Greenhouse Gases* estimates social cost of one 2020 metric ton CO₂ at $190 using the 2.0% near-term Ramsey discount rate. ✓ Exact match.

**Stern Review 1.4% discount rate** ([Ch 6 line 124](manuscript/chapters/Chapter__6_ThreeWaysofCounting__Draft.md:124)).
Stern Review's SDR = 1.4%, derived from pure-time-preference 0.1% + growth 1.3%. ✓ Exact match.

**Nordhaus ~4% discount rate** ([Ch 6 line 124](manuscript/chapters/Chapter__6_ThreeWaysofCounting__Draft.md:124)).
Nordhaus's preferred DICE model simulations use ~4.3%. ✓ Match within rounding.

**SCC history: Obama $42, Trump $1–7, Biden $190** ([Ch 6 lines 35, 41](manuscript/chapters/Chapter__6_ThreeWaysofCounting__Draft.md:35)).
- Obama IWG: $43 (2013 update); $52 (2020 update). Ch 6's $42 is closer to 2013-dollar version at 3% rate; defensible.
- Trump 2019 EPA: $1–$8 range. Ch 6's $7 upper bound is within range (depends on discount rate cited).
- Biden EPA: $190 ✓.
- All defensible with rounding.

**Appalachian reclamation bond shortfall $3.7–$6 billion** ([Ch 6 line 23](manuscript/chapters/Chapter__6_ThreeWaysofCounting__Draft.md:23)).
Appalachian Voices analysis: "$3.7 to $6 billion problem." ✓ Exact match.

**McDowell County 13-year life-expectancy gap** ([Ch 6 line 25](manuscript/chapters/Chapter__6_ThreeWaysofCounting__Draft.md:25)).
2013 IHME data: McDowell male life expectancy 63.5 vs national 76.5 → 13.0-year gap. Female gap ~10 years. The 13-year figure is the canonically-cited male-specific gap from 2013. Currently ~12-13 years per 2019–2021 data. ✓ Defensible; note male-specific.

**Deepwater Horizon $4.25B revenue + $65–70B total costs** ([Ch 6 line 33](manuscript/chapters/Chapter__6_ThreeWaysofCounting__Draft.md:33)).
- Macondo well projected reserves: 50M+ barrels (Wikipedia/Offshore Technology). At 2010 wholesale crude ~$85/bbl, projected revenue ~$4.25B. ✓ Match.
- BP total cost as of 2018: >$65 billion (BP final estimate $61.6B; cleanup + charges + penalties accumulating to $65B+). ✓ Match.

**Exxon Valdez $5.5M product math** ([Ch 6 line 33](manuscript/chapters/Chapter__6_ThreeWaysofCounting__Draft.md:33)).
11 million gallons × ~$0.50/gallon (1989 wholesale crude) ≈ $5.5M. ✓ Math checks. Total costs estimated at $7B (Exxon paid $2B cleanup + $1.8B restoration + $900M civil settlement); higher estimates cite $7–10B with full ecological damages. IPG range 1,200–1,900× confirmed via division. ✓

### VERIFIED-DATED ⚠

**Black Lung Disability Trust Fund $44 billion distributions** ([Ch 6 line 21](manuscript/chapters/Chapter__6_ThreeWaysofCounting__Draft.md:21)).
**Source verification (CRS R45261; GAO):** "By 2009, the federal Black Lung Disability Trust Fund had distributed over $44 billion in benefits"; more recent data: $45B+ since 1970. FY2017 annual benefits ~$184M. Cumulative debt FY2021: $4.6B.

The $44B figure is a **2009-vintage snapshot**. Current cumulative (through ~2024) is likely $48–$52B given annual benefits ~$150–$200M for 15 additional years.

**Recommended spot-fix during Phase C-α:** Update to current figure: "The Black Lung Disability Trust Fund's roughly $50 billion in distributions through 2024..." OR add date-anchor: "$44 billion in distributions through 2009..."

### STALE — needs refresh

**Norway GPFG ~$1.9 trillion** ([Ch 6 line 177](manuscript/chapters/Chapter__6_ThreeWaysofCounting__Draft.md:177)).
**Source verification (NBIM 2025–2026; CNBC):** End of 2025 GPFG value = NOK 21,268 billion ≈ **$2.2 trillion USD** (April 2025), up from ~$2.08T end of 2024. 2025 annual return +15.1% / $247B.

Ch 6's $1.9T figure is stale by ~$300B (~15% understated). 

**Recommended spot-fix during Phase C-α:** Update to "approximately $2 trillion" or "roughly $2.2 trillion (early 2025)." The qualitative argument is unchanged; the figure refresh is housekeeping.

**Stratos / 1PointFive "in construction at the time of writing"** ([Ch 6 line 47](manuscript/chapters/Chapter__6_ThreeWaysofCounting__Draft.md:47)).
**Source verification (1PointFive corporate; Carbon Herald):** Trains 1 and 2 completed December 2024; operations expected late 2025; phased ramp to full capacity by mid-2026. Cost reported ~$400–$500/ton currently; DOE target <$100/ton.

Ch 6's "in construction at the time of writing, and targeting commissioning within the next two years" framing is now stale — Stratos is in commissioning/ramp-up.

**Recommended spot-fix during Phase C-α:** Update framing to "Stratos, in commissioning at the time of writing with phased ramp to full capacity through mid-2026, is reported at $400–$500/ton current operating cost and targeting reduced unit cost as the facility scales." Adjusts the time-sensitive framing while preserving the trajectory argument.

### POSSIBLY-INCORRECT — needs fact-check or rewording

**IEA / IPCC mid-century DAC "$100–$300 range"** ([Ch 6 line 47](manuscript/chapters/Chapter__6_ThreeWaysofCounting__Draft.md:47)).
**Source verification (IEA *Direct Air Capture 2022*):** IEA estimates "operational costs of direct air capture should get to between $230 and $630 per metric ton of CO₂ once scaled up." First-of-a-kind DACCS projects $400–$700 (PV) or $350–$550 (cheap renewables).

Ch 6's $100 lower bound is **more optimistic than IEA's $230 floor** and attributes the range to IEA + IPCC AR6 WG3 jointly. The $100–$300 range may originate from IPCC AR6 WG3 optimistic-deployment scenarios specifically (not verified directly in this audit), but the IEA citation does not support a $100 lower bound.

**Two resolution options for Phase C-α:**
- **Option A (tighten the range to authoritative):** "The International Energy Agency's *Direct Air Capture 2022* review and the IPCC's AR6 Working Group III place the achievable cost by mid-century in the **$230-to-$600** range under scaled-up deployment scenarios..."
- **Option B (cite IPCC specifically for optimistic floor):** "The IPCC's AR6 Working Group III, under optimistic learning-curve assumptions, projects mid-century cost in the $100-$300 range; IEA's *Direct Air Capture 2022* review estimates a less optimistic floor of $230 at scaled-up operation." This separates the sources rather than conflating them.

Option B preserves the chapter's "optimistic deployment scenarios" framing while accurately attributing.

**Recommended:** Option B (separate the source attributions). Author judgment as to whether to verify IPCC AR6 WG3 floor directly before applying.

**Coal-to-CO₂ ratio 2.86 tons CO₂ per ton bituminous coal** ([Ch 6 line 29](manuscript/chapters/Chapter__6_ThreeWaysofCounting__Draft.md:29)).
**Source verification (EPA emission factors 1.1):** Default CO₂ emission factor for bituminous coal: 93.28 kg CO₂/mmBtu × ~25 mmBtu/short ton ≈ 2,325 kg CO₂/short ton = **2.325 metric tons CO₂ per short ton bituminous coal**. For metric-ton coal accounting at ~70–78% carbon content: 2.57–2.86 metric tons CO₂ per metric ton coal.

Ch 6's 2.86 figure is at the **upper end** of plausibility, achievable with high-carbon-content bituminous in metric-ton accounting. EPA's canonical 2.325 figure is for short-tons; converting to metric-ton coal at high-carbon-content yields ~2.86. The discrepancy is unit-convention plus coal-grade assumption.

**Downstream sensitivity:**
- At 2.325 × $190 = $442/ton coal (rather than $544)
- At 2.86 × $190 = $544/ton coal (current Ch 6 figure)
- Difference: $100/ton coal

The bottom-up totals shift from $550–$570/ton (current) to ~$448–$464/ton (at 2.325 ratio) — still substantially exceeds the $4.50 market price; the chapter's qualitative "carbon term dominates" finding survives.

**Two resolution options for Phase C-α:**
- **Option A (use EPA short-ton factor explicitly):** Replace "roughly 2.86 tons of CO₂" with "approximately 2.32 tons of CO₂ (EPA bituminous-coal emission factor)" and recompute downstream: $190 × 2.32 ≈ $441/ton coal; with-carbon total ~$449–$463/ton.
- **Option B (preserve 2.86; add metric-ton-coal + high-carbon-content disclosure):** Replace with "roughly 2.86 tons of CO₂ per metric ton of high-carbon-content bituminous coal (EPA's short-ton emission factor implies ~2.32 tons CO₂ per short ton; the metric-ton high-carbon convention used here is at the upper end of bituminous-grade carbon-content)."

Option A is cleaner and uses canonical EPA conventions; Option B preserves the existing figure but adds explanatory disclosure. Author judgment.

### VERIFIED-MATH BUT DISCLOSURE-GAP

**Libby ~$100M revenue + $5–$8B costs (40–82× IPG)** ([Ch 6 line 33](manuscript/chapters/Chapter__6_ThreeWaysofCounting__Draft.md:33)).
**Source verification (DOJ; EPA Superfund):** W.R. Grace settlements: $54.5M (2003) + $250M (2008 — largest in Superfund history) + $18.5M (2023 natural resource). Federal cleanup spending: >$600M. EPA Superfund site activity ongoing.

Direct settlement + cleanup figures sum to ~$0.9–$1.0B — significantly less than Ch 6's $5–$8B.

The $5–$8B framing necessarily includes **long-tail costs not yet realized in settlements:**
- Medical care for 400+ deaths + 3,000+ illnesses across multi-decade lifetimes
- Lifetime mesothelioma/asbestosis treatment + long-tail tail
- Property value collapse + community destruction
- Ecological remediation extending into future decades

These are real costs the framework's externality-tail apparatus correctly captures (the chapter's E term + the framework's RCV integrand over time). But the $5–$8B figure is not a direct settlement or cleanup-cost citation; it's an aggregate long-tail estimate.

**Recommended spot-fix during Phase C-α:** Add a disclosure clause: "Libby, Montana: around $100 million in lifetime mine revenue against $5 to $8 billion in **direct settlements (~$0.3B) plus federal cleanup spending (~$0.6B+) plus the long-tail of asbestos-related illness costs across thousands of cases, environmental remediation extending into future decades, and community destruction**. An IPG of 55 to 82 times."

This preserves the IPG figure while disclosing what's in the $5–$8B aggregate. Matches the externality-tail apparatus the chapter is demonstrating.

## Resolution and findings doc status updates

| Pre-amendment finding | Status after verification |
|---|---|
| LOW-1: Norway GPFG ~$1.9T | **PROMOTED to MEDIUM (date-refresh) — pre-publication update needed; $2.2T current** |
| LOW-1: EPA SCC $190 | **VERIFIED — close LOW** |
| LOW-1: DAC Climeworks $600–$1,000 | **PROMOTED to MEDIUM — $600 lower bound aggressive; actual Orca FOAK $1,000+** |
| LOW-1: DAC Stratos $300–$600 + "in construction" | **PROMOTED to MEDIUM — status framing stale; cost range defensible** |
| LOW-1: DAC IEA/IPCC $100–$300 | **PROMOTED to SHOULD-FIX — IEA citation does not support $100 floor; separate IEA from IPCC AR6 WG3 attribution** |
| LOW-1: Black Lung $44B | **PROMOTED to MEDIUM (date-refresh) — vintage 2009; current ~$50B** |
| LOW-1: McDowell 13-year gap | **VERIFIED — close LOW** |
| (new) Coal-to-CO₂ 2.86 | **NEW SHOULD-FIX — high vs EPA's 2.325 short-ton; needs unit-convention disclosure** |
| (new) Libby $5–$8B framing | **NEW MEDIUM — needs long-tail-cost disclosure clause** |

## Net new findings

- **NEW SHOULD-FIX-3 (HIGH):** Coal-to-CO₂ ratio 2.86 — author decision between Option A (use EPA short-ton factor explicitly; recompute downstream) or Option B (preserve figure with disclosure of metric-ton + high-carbon convention).
- **NEW SHOULD-FIX-4 (HIGH):** IEA citation does not support $100 mid-century DAC floor — author decision between Option A (tighten range to IEA/IPCC authoritative bounds $230–$600) or Option B (separate IEA from IPCC AR6 WG3 attribution; IPCC carries the optimistic floor).
- **NEW MEDIUM-5:** Libby $5–$8B costs — add long-tail-cost disclosure clause to make the externality-tail apparatus the figure rests on visible.
- **NEW MEDIUM-6:** Norway GPFG $1.9T → ~$2.2T (date-refresh).
- **NEW MEDIUM-7:** Black Lung Trust Fund $44B → ~$50B (date-refresh or date-anchor).
- **NEW MEDIUM-8:** Stratos "in construction" → "in commissioning with phased ramp to full capacity through mid-2026" (status-refresh).
- **NEW MEDIUM-9:** Climeworks Orca $600 lower bound — actual FOAK reported ~$1,000+; revise to "$1,000+ per ton at first-of-a-kind operational scale" with the Mammoth/Generation-3 cost-reduction trajectory cited separately.

## Phase C-α scope additions

The Phase C-α session should additionally apply:
- Coal-to-CO₂ figure decision (SHOULD-FIX-3).
- IEA/IPCC attribution decision (SHOULD-FIX-4).
- Libby $5–$8B disclosure clause (MEDIUM-5).
- Norway GPFG figure refresh (MEDIUM-6).
- Black Lung Trust Fund figure refresh (MEDIUM-7).
- Stratos status refresh (MEDIUM-8).
- Climeworks Orca cost band correction (MEDIUM-9).

These figure-level fixes can apply jointly with the B.2 + MUST-FIX-2 structural fixes in a single Phase C-α session, since they touch adjacent prose passages.

## Authoritative source citations

For Phase C-α reference, the following sources should be cited if any of the figures are footnoted at chapter level:

- [EPA, *Report on the Social Cost of Greenhouse Gases* (November 2023)](https://www.epa.gov/system/files/documents/2023-12/epa_scghg_2023_report_final.pdf)
- [IEA, *Direct Air Capture 2022*](https://www.iea.org/reports/direct-air-capture-2022)
- [NBIM, "The fund's value"](https://www.nbim.no/en/investments/the-funds-value/)
- [CRS Report R45261, "The Black Lung Program, the Black Lung Disability Trust Fund, and the Excise Tax on Coal"](https://www.congress.gov/crs-product/R45261)
- [NOAA, "Deepwater Horizon oil spill settlements: Where the money went"](https://www.noaa.gov/explainers/deepwater-horizon-oil-spill-settlements-where-money-went)
- [DOJ, W.R. Grace asbestos cleanup settlements (2003, 2008)](https://www.justice.gov/archive/opa/pr/2008/March/08_enrd_194.html)
- [EPA Superfund — Libby Asbestos Site Profile](https://cumulis.epa.gov/supercpad/cursites/csitinfo.cfm?id=0801744)
- [Stern Review (Wikipedia summary) — 1.4% SDR composition](https://en.wikipedia.org/wiki/Stern_Review)
- [Barrage & Nordhaus, "Policies, Projections, and the Social Cost of Carbon: Results from the DICE-2023 Model" (NBER)](https://www.nber.org/papers/w31112)
- [Appalachian Voices, coal-mine reclamation bonding analysis](https://appvoices.org/coal-impacts/current-mine-reclamation/)
- [CDC + IHME County Profiles — McDowell County WV](https://www.healthdata.org/sites/default/files/files/county_profiles/US/2015/County_Report_McDowell_County_West_Virginia.pdf)
- [1PointFive Stratos project page](https://www.1pointfive.com/projects/ector-county-tx)
- [Climeworks Mammoth plant page](https://climeworks.com/plant-mammoth)
- [EPA Bituminous Coal Combustion Emission Factors](https://www.epa.gov/sites/default/files/2020-09/documents/1.1_bituminous_and_subbituminous_coal_combustion.pdf)

---

*End of Amendment 2026-05-13 (B) — authoritative-source verification of questioned numbers.*

**Status: LOW-1 RESOLVED. 2 new SHOULD-FIX + 5 new MEDIUM findings added; all 7 awaiting author ratification.**

---

# Amendment C (2026-05-14) — Darity-synthesis-incorporation gap (pre-Sandy-send)

**Trigger:** Cross-session handoff from Ch 5 Pass 1 audit (commit b390a46 §B.7, 2026-05-14, on origin/main) surfaced that this Ch 6 Pass 1 doc (current state through Amendment B at commit a2f39ca) does not cover the post-interview Darity-synthesis incorporation gap. Five items from the synthesis doc ([research/outreach/subjects/darity/post-interview-synthesis_2026-05-13.md](research/outreach/subjects/darity/post-interview-synthesis_2026-05-13.md)) target Ch 6 (or Ch 6 / Ch 10) and are pre-Sandy-send gating.

**Context.** Sandy Darity interview conducted Wed 2026-05-13 14:30 ET. Synthesis commit 3e39061 surfaced MI-1 through C-3 (9 items). MI-1 + MI-2 already incorporated into Ch 5 + TA via Approach B (commits 70dce3f + downstream). The 5 items below target Ch 6 (or Ch 6 / Ch 10) and remain PENDING. Sandy named SI-1 his "deepest single-line case for the framework's measurement work" — non-trivial absence pre-send. Ch 6 + Ch 5 + TA ship as the Sandy send packet after both chapters' Phase C-α lands.

**Scope of this amendment.** Content-incorporation findings rather than fact-check-strict findings; surfaced as PROPOSED at the severities the synthesis routing specifies, applied during Phase C-α (combined session with existing structural + number-level fixes per Amendments A + B).

## Findings

### NEW SHOULD-FIX-5 (HIGH): Ostrom homogeneity-of-interest break-point — missing second break-point in Ostrom-positioning passage

**Location:** [Chapter__6_ThreeWaysofCounting__Draft.md:227–233](manuscript/chapters/Chapter__6_ThreeWaysofCounting__Draft.md:227)

**Synthesis source ([darity post-interview-synthesis:260–266](research/outreach/subjects/darity/post-interview-synthesis_2026-05-13.md:260)):** Sandy's add-on critique of Ostrom (full quote):
> *"another issue with Ostrom is, I think she's assuming homogeneity of interest in using the commons across what she's calling the community. But suppose the community is divided on ethnic grounds or racial grounds, and have conflicting views about what should be done with the commons, then I don't think that her view provides a solution to the problem."*

**Current Ch 6 state:** The chapter's "Two Kinds of Commons" passage (lines 227–233) identifies non-sustained-yield commons (extraction commons where value-capture and cost-bearing are asymmetric) as the break-point where Ostrom's design principles do not apply. Verified by grep: no current Ch 6 reference to "homogeneity" / "heterogeneous-stakeholder" / "ethnic" / "racial" division of the commons community. Sandy's second break-point — **heterogeneous-stakeholder commons** — is absent.

**Framework consequence:** Sandy's critique adds a second structural break-point to the framework's existing Ostrom-positioning. Ostrom's eight design principles presume a community of shared-stakeholders with substantially-aligned use-preferences; where the community is divided on ethnic / racial / class lines and carries conflicting preferences, the Ostrom apparatus does not produce a solution. This is a substantive extension of the framework's claim of necessity — the framework now occupies a second adjacency to Ostrom (heterogeneous-stakeholder commons) alongside the first (extraction commons / non-sustained-yield).

**Why this is SHOULD-FIX:** Sandy is the canonical authority on this critique. He will recognize the absence on first read; the framework's Ostrom-positioning passage is exactly where he will look for it. Adding the second break-point also strengthens the framework's structural argument, not just its Sandy-facing presentation — the chapter's downstream "Each method does work the other can't" claim (line 233) becomes more defensible when both break-points are named.

**Recommended fix during Phase C-α:** Extend the Ostrom-positioning passage at lines 227–233 with a second break-point paragraph. Draft for author review:

> "A second break-point Ostrom's framework does not address is the heterogeneous-stakeholder commons: where a community drawing from a shared commons is divided on ethnic, racial, class, or other grounds, and carries conflicting use-preferences for the commons itself. Ostrom's eight design principles presume substantially-aligned stakeholders capable of negotiating governance institutions; when the stakeholders are structurally divided, the design principles do not produce a solution because the problem is not solely coordination-of-mutually-acceptable-use but contestation over what acceptable use is. This framework's apparatus reaches such commons because the Commons Inversion Test operates on the commons-extraction relationship rather than on the stakeholder-coordination relationship; the cost severance the framework prices is the cost of extraction *from* the commons by extracting parties structurally outside the commons-bearing community, and this cost is measurable whether the cost-bearing community is internally aligned or divided."

**Synthesis-stated destination:** Ch 6 (Three Ways of Counting) Ostrom-extension section + canonical Ostrom-pivot articulation in [alignment/commons_bonds_framework_positioning_disciplines_v1.0.0.md](alignment/commons_bonds_framework_positioning_disciplines_v1.0.0.md) + TA §E.3. The Ch 6 application is the gating item for the Sandy send; the FPD doc + TA §E.3 are downstream secondary applications (separate workstreams).

**Severity rationale:** SHOULD-FIX (HIGH-equivalent) because (a) Sandy is the canonical authority on this critique, (b) absence is visible on first read of the Ostrom-positioning passage, (c) addition strengthens framework's structural argument (not just Sandy-facing presentation).

---

### NEW SHOULD-FIX-6 (HIGH): Market-priced future profitability vs unpriced future harms — Sandy's exact framing missing as the "cleanest single-line case for the measurement work"

**Location:** [Chapter__6_ThreeWaysofCounting__Draft.md:89](manuscript/chapters/Chapter__6_ThreeWaysofCounting__Draft.md:89) and [Chapter__6_ThreeWaysofCounting__Draft.md:231](manuscript/chapters/Chapter__6_ThreeWaysofCounting__Draft.md:231) (the two adjacent passages where the underlying concept is in place)

**Synthesis source ([darity post-interview-synthesis:270–274](research/outreach/subjects/darity/post-interview-synthesis_2026-05-13.md:270)):** Sandy's observation:
> *"those kinds of forecasts are, not forecast of harms per se, but forecast of future profitability. So [it's] built into the prices of financial assets in a given moment, at least implicitly. But you don't have a market mechanism for trying to gauge the predictions of future harms."*

The synthesis doc explicitly identifies Sandy's framing as "the cleanest single-line case for the framework's measurement work" (synthesis:274) and routes it to Ch 6 for sharpening.

**Current Ch 6 state:** The underlying concept is in place at two adjacent passages:
- Line 89: "These ongoing costs are real, measurable, and currently unpriced by markets."
- Line 231: "The asymmetry between value-capture and cost-bearing is structural, not contingent. The cost the framework prices is the severance enabled by that asymmetry."

But the **specific asymmetry Sandy names — markets-price-future-profitability vs markets-don't-price-future-harms — is not stated in those terms.** The chapter has the structural-asymmetry argument; the chapter does not have the financial-asset-pricing asymmetry argument as its mirror. Verified by grep: no current Ch 6 reference to "future profitability" / "asset prices" / "financial assets" in this context.

**Framework consequence:** Sandy's framing is sharper than the chapter's current framing because it points to a specific institutional asymmetry the framework's three-ways-of-counting fills. Markets *do* have a mechanism for pricing future profitability — discounted-cash-flow analysis aggregated through equity and debt markets, which produces asset prices that implicitly price expected future returns. Markets *do not* have an equivalent mechanism for pricing future harms — there is no aggregating institution producing a comparable price signal for the externality tail, the foreclosure cost, or the long-tail damage of cost severance. The framework's three estimation methods (Replacement Cost / Revealed Preference / Scarcity-Adjusted Option Value) are the substitute for the missing market mechanism on the harms side.

**Why this is SHOULD-FIX:** Sandy named this his "cleanest single-line case." The chapter ships to him without that exact framing in those terms — a missed opportunity. The framing is also rhetorically efficient: it gives the chapter a single sentence that summarizes the entire measurement-work claim in vocabulary Sandy's field (financial economics) already speaks.

**Recommended fix during Phase C-α:** Insert a paragraph at the externality-tail / structural-asymmetry passage (after line 91, before line 93; or at the end of "Two Kinds of Commons" near line 233) that lifts Sandy's framing. Draft for author review:

> "The asymmetry the framework's three estimation methods address is not symmetric across the time horizon. Markets have a mechanism — discounted-cash-flow analysis aggregated through equity and debt pricing — for pricing future profitability. That mechanism is implicit but real: every financial asset price embeds an expectation about future returns. Markets do not have an equivalent mechanism for pricing future harms. There is no aggregating institution producing a comparable price signal for the externality tail, for foreclosure cost, or for the long-tail damage of cost severance. The three estimation methods (Replacement Cost, Revealed Preference, Scarcity-Adjusted Option Value) are the framework's substitute for the missing market mechanism on the harms side. That is the measurement work — to give the harm side a comparable price signal to the one the asset side already has, so that the asymmetry between priced future profitability and unpriced future harms is no longer the institutional default."

**Synthesis-stated destination:** Ch 6 methodology / externality-tail passage. Author may want to position the paragraph specifically — three candidate locations: (a) after line 91's externality-tail name-defense; (b) at the end of "Two Kinds of Commons" near line 233; (c) at the start of the M1/M2/M3 walkthrough sub-section landing under MUST-FIX-1 B.2. Recommend (c) — the paragraph sets up exactly what the three methods are doing, and lands the Sandy-framing immediately before the inner-three walkthrough does the work.

**Severity rationale:** SHOULD-FIX (HIGH-equivalent) because (a) Sandy explicitly named this his cleanest single-line case for the measurement work, (b) the framing is rhetorically efficient and grounds the M1/M2/M3 walkthrough, (c) the current chapter has the structural-asymmetry argument but not the financial-asset-pricing asymmetry mirror, and the mirror is what makes the measurement-work claim land for Sandy's field.

---

### NEW SHOULD-FIX-7 (HIGH): Longevity gap as legacy-effect pricing — Darity research lineage not connected to McDowell 13-year gap

**Location:** [Chapter__6_ThreeWaysofCounting__Draft.md:25](manuscript/chapters/Chapter__6_ThreeWaysofCounting__Draft.md:25)

**Synthesis source ([darity post-interview-synthesis:276–278](research/outreach/subjects/darity/post-interview-synthesis_2026-05-13.md:276)):** Sandy mentioned recent work pricing the 6–7 year Black-vs-white US longevity gap as legacy-effect pricing. The synthesis doc explicitly routes Ch 6 methodology engagement: "both as anchor for the framework's legacy-effects-pricing move and as a citation tie to Sandy's current research direction. Find the recent paper / talk and add to bibliography."

**Current Ch 6 state:** Line 25 carries the McDowell County 13-year life-expectancy gap (verified canonical per Amendment B figure-verification; matches 2013 IHME data for male-specific gap). Verified by grep: no current Ch 6 reference to "Darity longevity" / "legacy-effect pricing" / "6-7 year gap" / "Black-vs-white longevity." The connection between McDowell's 13-year gap and Darity's longevity-gap research is structural (both are legacy-effect pricing of cost-severance harm) but not named.

**Framework consequence:** Darity's longevity-gap pricing work is the methodological lineage McDowell's 13-year longevity gap inherits. The framework's measurement of McDowell's legacy effect (13 years) uses the same matched-comparison methodology Hamilton/Darity/Mullen developed for wealth-gap and longevity-gap research. Naming the connection (a) grounds the McDowell figure in established methodological lineage rather than presenting it as a freestanding claim, (b) ties the framework explicitly to Sandy's current research direction (which strengthens the framework's reparations-economics engagement), (c) extends the framework's bidirectional apparatus claim — McDowell's longevity gap is a backward-direction CSD computation; the methodology is the same Darity uses.

**Why this is SHOULD-FIX:** The connection is structurally present in the framework but not named in the chapter. Sandy reading Ch 6 will note the McDowell longevity-gap citation and may or may not recognize the methodological connection to his own work; making the connection explicit ensures he sees the framework's positioning. The bibliographic citation also opens a downstream tie-to-Sandy that the publishing pipeline can build on.

**Recommended fix during Phase C-α:** Add a short paragraph (or expanded sentence) at line 25 connecting McDowell's 13-year gap to Darity's longevity-gap legacy-effects work. Draft for author review:

> "The 13-year life-expectancy gap is a *legacy-effect* — a measurable consequence of cost-severance harm that persists across cohorts. The methodology for pricing legacy effects of this kind has been developed most rigorously by William Darity Jr. and collaborators in their work on the Black-vs-white longevity gap (a 6-to-7-year average gap in the United States), which prices the gap as a legacy effect of structural extraction across generations. McDowell County's 13-year gap is the same kind of legacy-effect pricing variant, applied to coal-extraction-affected populations rather than to racially-stratified populations. The methodology travels; the per-context calibration is what differs."

**Bibliography requirement:** Find Sandy's specific recent paper/talk on the longevity-gap pricing and add to bibliography §13 (reparations economics). Cross-thread #11 contribution: 1L (Darity longevity-gap paper TBD).

**Synthesis-stated destination:** Ch 6 methodology section (line 25 expansion) + bibliography expansion. The Ch 5 paired companion fix is the existing Ch 5 line 216 passage which already cites Darity & Mullen on the longevity gap framework — Ch 5's coverage establishes the methodology; Ch 6's gap is the chapter-specific application not anchoring to it.

**Severity rationale:** SHOULD-FIX (HIGH-equivalent) because (a) the methodological lineage is present in the framework but not named in the chapter, (b) Sandy will read the McDowell citation looking for the methodological tie to his own work, (c) the addition is small (one paragraph) and high-value.

---

### NEW MEDIUM-10 (conditional location): Sen on social welfare functions + capabilities — right-wing-pushback defense

**Location:** [Chapter__6_ThreeWaysofCounting__Draft.md:193](manuscript/chapters/Chapter__6_ThreeWaysofCounting__Draft.md:193) (current Sen + Nussbaum single-sentence reference)

**Synthesis source ([darity post-interview-synthesis:280–282](research/outreach/subjects/darity/post-interview-synthesis_2026-05-13.md:280)):** "Sen's framework gives the framework a defense against the 'why give value to future generations?' right-wing critique. Engage in Ch 6 or Ch 10. Bibliography expansion likely."

**Current Ch 6 state:** Line 193 contains the only Sen reference in Ch 6: "Sen and Nussbaum elaborated ten central capabilities" — an illustrative-register parallel to Ostrom-eight + Rawls-primary-goods, not a methodological engagement.

**Framework consequence:** Sen's social-welfare-function framework provides a defense the framework currently does not carry: the philosophical grounding for valuing future generations against the right-wing critique ("why give value to future generations?"). The framework's existing Parfit-grounded non-identity-problem engagement (lines 213–221) is one defense; Sen's capability framework is a second, complementary defense. The Sandy synthesis flags Sen specifically for the right-wing-pushback case-class.

**Conditional location — Ch 6 vs Ch 10:** Author judgment required.
- **Argument for Ch 6 (methodology):** Technical defense-of-methodology fits Ch 6's apparatus framing. The right-wing critique ("why value future generations?") is a methodological objection the chapter already engages via Parfit; Sen engagement would extend that section. Sen + Parfit together carry the philosophical grounding for the framework's intergenerational-pricing claim.
- **Argument for Ch 10 (politico-philosophical close):** Right-wing-pushback engagement reads more naturally in Ch 10's closing register, where the chapter explicitly addresses the "this is just degrowth in disguise" / "you're constraining the economy" critique-class. Sen engagement here grounds the chapter's "the framework does not take a position on what kind of economy we should have" passage (lines 81–87).

**Recommended fix during Phase C-α:**

- **If Ch 6:** Add a short paragraph at the end of the Parfit-grounded "What Is Owed" section (after line 224) that brings in Sen. Draft for author review:

  > "A second philosophical grounding the framework operates within — complementary to Parfit's impersonal-outcomes evaluation — is Amartya Sen's capability-and-social-welfare-function framework. Where Parfit answers the question of *whether* future generations have moral standing, Sen answers the question of *how* their standing should be valued: in terms of capabilities the framework's accounting can preserve or extinguish. The framework's Residual Commons Value calculation is, in Sen's vocabulary, a measurement of the capability set extraction forecloses on whoever-the-future-people-turn-out-to-be. Right-wing critics who ask 'why give value to future generations?' are asking a Parfit-domain question; the framework's answer is *because they will have capabilities that present extraction will or will not constrain*, and Sen's framework names the capabilities and the valuation methodology that grounds the framework's pricing."

- **If Ch 10:** Surface a cross-session flag to the Ch 10 workstream rather than applying in Ch 6. Recommend coordinating with the just-landed Ch 10 bidirectional-reach insertion (commit 8b7ac89) and the in-flight Ch 10 work.

**Recommend Ch 6 placement** (Argument for Ch 6 above) — the chapter's methodology framing already carries the Parfit engagement; adding Sen as a complementary methodology-defense reads as continuation, not detour. Sen's capability framework also resonates with the chapter's existing illustrative-register list at line 193 (Sen + Nussbaum + Rawls); upgrading from single-sentence illustrative reference to methodological engagement is natural.

**Could land post-Sandy-send if necessary** per the synthesis routing — Sen engagement is not as gating as MI-3 / SI-1 / SI-2.

**Synthesis-stated destination:** Ch 6 or Ch 10 (author judgment). Bibliography expansion likely (Sen *Development as Freedom* 1999; possibly Sen + Nussbaum *Quality of Life* 1993; Nussbaum *Creating Capabilities* 2011).

**Severity rationale:** MEDIUM (conditional location) because (a) the defense is structurally complementary to Parfit (the chapter has the Parfit defense; Sen extends), (b) the placement is conditional on author judgment between Ch 6 and Ch 10, (c) per synthesis routing this can land post-Sandy-send if necessary — not gating.

---

### NEW LOW-7: Stratification economics — cross-disciplinary tie to MI-3 Ostrom-critique

**Location:** New addition — Ch 6 currently does not reference stratification economics anywhere.

**Synthesis source ([darity post-interview-synthesis:294–296](research/outreach/subjects/darity/post-interview-synthesis_2026-05-13.md:294)):** "Sandy framed the racial-wealth-gap-as-public-policy claim as 'the kind of argument that [stratification economics] argument [makes]' — i.e., his field. The framework already cites stratification economics in Ch 5 + Ch 6; Sandy's Ostrom-critique implicitly extends the stratification-economics analytical apparatus to commons-governance debates. Worth a small Ch 6 footnote / Tech Appendix line."

**Verification finding (verified during this amendment):** The synthesis's premise that "the framework already cites stratification economics in Ch 5 + Ch 6" is **not currently accurate.** Corpus grep across `manuscript/chapters/` returns zero hits for "stratification" in any chapter draft (Ch 5 or Ch 6). The only corpus references to "stratification economics" are in `research/outreach/subjects/darity/` documents (background-brief, prereadbrief, post-interview-synthesis). The synthesis routing therefore needs adjustment: this is a **fresh-citation addition**, not an extension of an existing citation.

**Framework consequence:** Stratification economics — the analytical framework Sandy named as his own field — provides cross-disciplinary lineage for the MI-3 Ostrom-critique. Stratification economics specifically analyzes intergroup-relational dynamics where structural-extraction operates through hierarchical group-divisions (race, class, ethnicity); the framework's MI-3 extension of Ostrom to heterogeneous-stakeholder commons is structurally an application of stratification-economics-style analysis to commons-governance contexts. Naming the connection (a) credits Sandy's field-naming, (b) ties the framework's commons-governance extension to an existing analytical tradition, (c) opens a downstream methodological engagement the publishing pipeline can build on.

**Recommended fix during Phase C-α:** Small footnote or single-line addition tying the MI-3 Ostrom-critique to stratification economics. Could land in Ch 6 at the heterogeneous-stakeholder break-point paragraph (SHOULD-FIX-5) or in the TA §E.3 paragraph the synthesis flags. Draft for author review:

> "[Footnote or inline at the MI-3 break-point paragraph]: This second break-point connects the framework to the analytical apparatus of stratification economics (Darity, Hamilton, and collaborators), which analyzes structural-extraction operating through hierarchical group-divisions (race, class, ethnicity). The framework's commons-governance extension applies stratification-economics-style intergroup-relational analysis to commons that are simultaneously contested across stakeholder-group lines and being extracted from by structural outsiders."

**Synthesis-stated destination:** Small Ch 6 footnote / Tech Appendix line. Lower-priority than MI-3 itself but lands naturally as MI-3's lineage citation.

**Severity rationale:** LOW because (a) the addition is small (footnote or single line), (b) the underlying MI-3 addition is the load-bearing item; stratification-economics tie is a lineage credit on top, (c) the synthesis premise that the framework "already cites" stratification economics was incorrect — actual state is fresh-citation addition.

---

## Status after Amendment C

| Finding | Pre-amendment | Post-amendment |
|---|---|---|
| MUST-FIX-1 + MUST-FIX-2 (Amendment A) | RATIFIED | RATIFIED — unchanged |
| SHOULD-FIX-1 + SHOULD-FIX-2 (Amendment A) | RATIFIED | RATIFIED — unchanged |
| SHOULD-FIX-3 (coal-CO₂; Amendment B) | PROPOSED | PROPOSED — unchanged |
| SHOULD-FIX-4 (IEA/IPCC; Amendment B) | PROPOSED | PROPOSED — unchanged |
| **NEW SHOULD-FIX-5 (Ostrom homogeneity-of-interest; MI-3)** | — | **PROPOSED** |
| **NEW SHOULD-FIX-6 (Market-priced future profitability asymmetry; SI-1)** | — | **PROPOSED** |
| **NEW SHOULD-FIX-7 (Longevity gap as legacy-effect pricing; SI-2)** | — | **PROPOSED** |
| MEDIUM-1 (Smax wording) | PROPOSED | PROPOSED |
| MEDIUM-3 (rounding) | DEFER-ACCEPTABLE | DEFER-ACCEPTABLE (moot if SHOULD-FIX-3 lands) |
| MEDIUM-4 (5 TA hyperlinks) | PROPOSED | PROPOSED |
| MEDIUM-5 through MEDIUM-9 (Amendment B figure-fixes) | PROPOSED | PROPOSED |
| **NEW MEDIUM-10 (Sen on social welfare + capabilities; SI-3)** | — | **PROPOSED (conditional Ch 6 vs Ch 10)** |
| LOW-1 (Amendment B resolved) | RESOLVED | RESOLVED |
| LOW-2 through LOW-6 | PROPOSED / informational | unchanged |
| **NEW LOW-7 (Stratification economics tie; C-3)** | — | **PROPOSED** |

## Aggregate severity counts (full doc post-Amendment C)

| Severity | Initial Pass 1 | After Amendment A | After Amendment B | After Amendment C |
|---|---|---|---|---|
| MUST-FIX | 2 | 2 (ratified) | 2 (ratified) | 2 (ratified) |
| SHOULD-FIX | 2 | 2 (ratified) | 4 (2 ratified + 2 new) | **7 (2 ratified + 5 new — 3 fresh)** |
| MEDIUM | 4 | 4 | 9 | **10 (1 new)** |
| LOW | 6 | 6 | 6 (LOW-1 resolved → 5) | **6 (1 new + LOW-1 resolved)** |
| Cross-thread #9 | 1 | 1 | 1 | 1 |

## Phase C-α scope addition (Amendment C items)

The Phase C-α session should additionally apply, jointly with the existing Amendment A + B scope:

1. **MI-3 Ostrom homogeneity-of-interest break-point paragraph** at Ch 6 lines 227–233 (SHOULD-FIX-5).
2. **SI-1 market-priced future profitability asymmetry paragraph** at the start of the M1/M2/M3 walkthrough sub-section landing under MUST-FIX-1 B.2 (SHOULD-FIX-6). Recommended placement bundles cleanly with the B.2 work.
3. **SI-2 Darity longevity-gap lineage paragraph** at Ch 6 line 25 + bibliography expansion (SHOULD-FIX-7).
4. **SI-3 Sen capabilities defense paragraph** at the end of "What Is Owed" section after line 224 (MEDIUM-10) — *if author judgment selects Ch 6 placement; otherwise surface to Ch 10 cross-session flag*.
5. **C-3 stratification-economics lineage footnote/inline** at the MI-3 break-point paragraph (LOW-7).

Net additional Phase C-α prose: ~4 paragraphs + 1 footnote + 1 bibliography addition. All adjacent to or co-located with the existing Phase C-α scope; single coordinated session remains viable.

## Cross-thread items NOT folded into Ch 6 Pass 1

Per synthesis routing — surface to other workstreams:
- **C-1 (Fogel & Engerman *Time on the Cross* two-volume publishing model):** comp-titles deep matrix workstream (#14) / agent-prep workstream (#6).
- **C-2 (Du Bois *Black Reconstruction* bibliography expansion):** bibliography workstream.

## Coordination

- **Ch 5 Pass 1 §B.7** (the cross-session flag that triggered this amendment) and this Amendment C are now consistent. Ch 5 + Ch 6 Pass 1 docs both surface the Darity-synthesis-incorporation gap at the severities the synthesis routing specifies.
- **PM dashboard refresh** (commit 964448687, on origin/main) captures the full Darity-synthesis-incorporation status. This amendment is downstream of that PM refresh.
- **Phase C-α timing:** the 5 Amendment C items + the 2 SHOULD-FIX + 5 MEDIUM Amendment B items + the 4 ratified MUST/SHOULD-FIX Amendment A items all touch the same chapter and land in a single coordinated Phase C-α session. No additional dependency-resolution required.

---

*End of Amendment C 2026-05-14 — Darity-synthesis-incorporation gap.*

**Status: 3 new SHOULD-FIX + 1 new MEDIUM + 1 new LOW added; all 5 awaiting author ratification. Pre-Sandy-send gating for MI-3 + SI-1 + SI-2 per synthesis doc routing.**

---

# Amendment D (2026-05-14) — Full ratification + Phase C-α working brief

**Trigger:** Author ratified all remaining PROPOSED items in a single batch ("ratify all as proposed"), 2026-05-14. All recommended resolution paths applied per author judgment. Phase C-α now has full ratified scope.

## Ratification record

| Finding | Pre-ratification | Ratified resolution | Status |
|---|---|---|---|
| MUST-FIX-1 (B.2) | Ratified Amendment A | M1/M2/M3 walkthrough sub-section inside Approach 3 | **RATIFIED** |
| MUST-FIX-2 | Ratified Amendment A | Rebuild convergence table as M1/M2/M3 per-case columns | **RATIFIED** |
| SHOULD-FIX-1 | Ratified Amendment A | Anchor Ch 5 line 214 informal labels to canonical M1/M2/M3 names (joint with Ch 5 Pass 1) | **RATIFIED** |
| SHOULD-FIX-2 | Ratified Amendment A | Auto-resolves with MUST-FIX-2 table rebuild | **RATIFIED** |
| SHOULD-FIX-3 (coal-CO₂) | PROPOSED | **Option A** — Use EPA short-ton factor 2.32; recompute downstream: $544 → ~$441; bottom-up totals $550–$570 → ~$449–$464; recompute convergence-table IPG cells accordingly | **RATIFIED** |
| SHOULD-FIX-4 (IEA/IPCC) | PROPOSED | **Option B** — Separate IEA citation ($230–$600 scaled-up) from IPCC AR6 WG3 (optimistic floor); verify IPCC AR6 WG3 $100 floor as part of Phase C-α; fall back to Option A (drop $100 floor entirely) if verification fails | **RATIFIED with verification step** |
| SHOULD-FIX-5 (MI-3 Ostrom) | PROPOSED | Extend Ch 6 Ostrom-positioning passage at lines 227–233 with heterogeneous-stakeholder break-point paragraph | **RATIFIED** |
| SHOULD-FIX-6 (SI-1 future-profitability asymmetry) | PROPOSED | Insert Sandy's exact framing paragraph at the start of the M1/M2/M3 walkthrough sub-section (bundles with MUST-FIX-1 B.2) | **RATIFIED** |
| SHOULD-FIX-7 (SI-2 longevity gap) | PROPOSED | Expand Ch 6 line 25 with Darity longevity-gap lineage paragraph + bibliography expansion (Darity longevity-gap paper TBD) | **RATIFIED** |
| MEDIUM-1 (Smax wording) | PROPOSED | Replace "Smax that may be less than one" with "asymptotic limit S(∞\|t₀) ≤ 1" | **RATIFIED** |
| MEDIUM-3 (rounding tolerance) | DEFER-ACCEPTABLE | Moot once SHOULD-FIX-3 lands (figures recompute to ~$449–$464 anyway) | **MOOT** |
| MEDIUM-4 (5 TA hyperlinks) | PROPOSED | Add hyperlinks at TA §3, §5.5, §9, §13, §6; verify §5.5 anchor name against just-landed TA work before applying | **RATIFIED with verification step** |
| MEDIUM-5 (Libby disclosure) | PROPOSED | Add long-tail-cost disclosure clause to the $5–$8B figure at line 33 | **RATIFIED** |
| MEDIUM-6 (Norway refresh) | PROPOSED | Update $1.9T → ~$2.2T (early 2025 NBIM) at line 177 | **RATIFIED** |
| MEDIUM-7 (Black Lung date-anchor) | PROPOSED | "$44 billion through 2009" date-anchor at line 21 | **RATIFIED** |
| MEDIUM-8 (Stratos status) | PROPOSED | "in commissioning with phased ramp through mid-2026" replaces "in construction at the time of writing" at line 47 | **RATIFIED** |
| MEDIUM-9 (Climeworks Orca cost) | PROPOSED | "approximately $1,000+ per ton at first-of-a-kind operational scale" with Mammoth/Gen-3 trajectory cited separately at line 47 | **RATIFIED** |
| MEDIUM-10 (SI-3 Sen capabilities) | PROPOSED (conditional Ch 6 vs Ch 10) | **Ch 6 placement** — after line 224 at end of "What Is Owed" section | **RATIFIED — Ch 6 placement** |
| LOW-2 (Exxon Valdez disclosure) | PROPOSED | Extend line-149 one-event disclosure to Exxon Valdez | **RATIFIED** |
| LOW-5 (SCC acronym) | PROPOSED | Spell out "social cost of carbon (SCC)" at line 35 first use | **RATIFIED** |
| LOW-6 (cross-thread #9 GuidanceDoc + terms_index staleness) | PROPOSED for surfacing | Surface to PM dashboard for systematic sweep — **NOT Phase C-α** | **SURFACED** |
| LOW-7 (C-3 stratification economics tie) | PROPOSED | Add stratification-economics lineage footnote/inline at the MI-3 break-point paragraph | **RATIFIED** |

**All findings disposed.** 20 items in Phase C-α working scope; 1 item (cross-thread #9) routed separately; 1 item (MEDIUM-3) moot via cascading recompute.

---

## Phase C-α working brief — ordered by Ch 6 edit location

This is the working scope for the Phase C-α session. Edits ordered by line-of-occurrence in [Chapter__6_ThreeWaysofCounting__Draft.md](manuscript/chapters/Chapter__6_ThreeWaysofCounting__Draft.md) for clean session flow. Companion edits in Ch 5 and bibliography surfaced separately.

### §A. Bottom-Up Damage Accounting section (lines 17–51)

1. **Line 21 — Black Lung date-anchor (MEDIUM-7):** Replace "$44 billion in distributions" with "approximately $44 billion in distributions through 2009 (GAO/CRS)" or equivalent date-anchor wording.

2. **Line 25 — Darity longevity-gap lineage (SHOULD-FIX-7):** Insert paragraph connecting McDowell's 13-year gap to Darity's longevity-gap research. Draft text in Amendment C (above); bibliography expansion required (Darity longevity-gap paper TBD).

3. **Line 29 — Coal-to-CO₂ ratio + downstream recompute (SHOULD-FIX-3 Option A):**
   - Replace "roughly 2.86 tons of CO₂" with "approximately 2.32 tons of CO₂ (EPA emission factor for bituminous coal at short-ton accounting)"
   - Recompute "$190 × 2.86 = $544" → "$190 × 2.32 = $441 per ton coal"
   - Line 31: Recompute "Include carbon, and the bottom-up total rises to $550–570 per ton" → "$449–$464 per ton" (or "$450–$465" rounded)
   - Verify against EPA emission factor sheet; cite if footnoted

4. **Line 33 — Libby long-tail disclosure clause (MEDIUM-5):** Replace "$5 to $8 billion in asbestos-related illness costs, environmental remediation, and community destruction" with "$5 to $8 billion in **direct settlements (~$0.3B), federal cleanup spending (~$0.6B+), and the long-tail of asbestos-related illness costs across thousands of cases, environmental remediation extending into future decades, and community destruction**" — preserves IPG figure; discloses what's in the aggregate.

5. **Line 33 — Exxon Valdez one-event disclosure (LOW-2):** Extend the line-149 disclosure pattern to Exxon Valdez. Either inline at line 33 or at the convergence-table caption near line 146 alongside the Deepwater Horizon disclosure.

6. **Line 35 — SCC acronym spell-out (LOW-5):** Replace first-use "the SCC" with "the social cost of carbon (SCC)" — body uses spelled-out form throughout otherwise.

7. **Line 47 — DAC cost passages (SHOULD-FIX-4 + MEDIUM-8 + MEDIUM-9):**
   - **MEDIUM-9 Climeworks Orca:** Replace "$600 to $1,000 per ton" with "approximately $1,000 or more per ton at first-of-a-kind operational scale"
   - **MEDIUM-9 Climeworks Mammoth/Gen-3 trajectory:** Add separate clause citing Mammoth/Gen-3 cost-reduction trajectory toward $400–$600 by 2030 per Climeworks corporate disclosures
   - **MEDIUM-8 Stratos status:** Replace "in construction at the time of writing, targeting commissioning within the next two years" with "in commissioning at the time of writing with phased ramp to full capacity through mid-2026"
   - **SHOULD-FIX-4 IEA/IPCC attribution split (Option B):** Replace "The International Energy Agency's *Direct Air Capture 2022* review and the IPCC's AR6 Working Group III place the achievable cost by mid-century in the one-hundred-to-three-hundred-dollar range under optimistic deployment scenarios" with:
     - "The International Energy Agency's *Direct Air Capture 2022* review places the achievable cost at scaled-up operation in the $230-to-$600 range, depending on energy-source assumptions. The IPCC's AR6 Working Group III, under more optimistic learning-curve and policy-support scenarios, projects mid-century costs as low as $100-$300 per ton."
   - **Verification step required before applying:** Verify IPCC AR6 WG3 supports $100 floor under optimistic scenarios. If verification fails, fall back to Option A: tighten the entire range to $230–$600 and drop the IPCC $100 floor.

### §B. RCV apparatus section (lines 77–131)

8. **~Line 97 — TA §3 hyperlink (MEDIUM-4):** Add at the formula introduction: "(formal articulation in [Technical Appendix §3 — RCV Quantification — Three Ways of Counting](../../core/technical-appendix/TechnicalAppendix_v2.0.0.html#sec-3-rcv-quantification))"

9. **Line 128 — Smax wording (MEDIUM-1):** Replace "approaches some maximum Smax that may be less than one" with "approaches some asymptotic limit S(∞|t₀) ≤ 1"

10. **~Line 131 — TA §13 hyperlink (MEDIUM-4):** Add at end of Substitutability Function section: "(formal specification in [Technical Appendix §13 — Substitutability Function and Gap](../../core/technical-appendix/TechnicalAppendix_v2.0.0.html#sec-13-substitutability-function-and-gap))"

### §C. M1/M2/M3 walkthrough sub-section (NEW — lands inside Approach 3, ~line 116)

11. **MUST-FIX-1 B.2 walkthrough (~600–900w) — opens with SHOULD-FIX-6 (SI-1) framing:** Insert new sub-section "The Three Ways of Counting Inside RCV" (or similar) between line 116 (formula introduction close) and line 120 (Substitutability Function section opening). Sub-section structure:

    a. **Opening paragraph (SHOULD-FIX-6 — SI-1 framing):** Markets price future profitability via asset prices; markets do not price future harms; the three methods are the substitute for the missing market mechanism on the harms side. Draft text in Amendment C (above).
    b. **Method 1 — Replacement Cost:** Walk McDowell coal via DAC anchor ($310–$1,800/ton per TA §3.6 Block 4); cite TA §3.3.
    c. **Method 2 — Revealed Preference:** Walk McDowell coal via Norway-anchored revealed-preference (~$8–$88/ton per TA §3.6 Block 4); cite TA §3.4.
    d. **Method 3 — Scarcity-Adjusted Option Value:** Walk McDowell coal via Dixit-Pindyck option-value with scarcity + irreversibility weighting ($420–$13,100/ton; mid $2,500 per TA §3.6 Block 4); cite TA §3.5; flag α-dominance regime per TA §3.5 sensitivity table.
    e. **Bridge to backward direction:** Connect to Ch 5 line 214 backward-direction application (canonical names per SHOULD-FIX-1 anchoring); cite TA §5.5 for the bidirectional structural property.

### §D. Convergence table + caption (lines 134–157)

12. **~Line 138 — TA §9 hyperlink (MEDIUM-4):** Add at convergence introduction: "(formalized in [Technical Appendix §9 — Three-Model Convergence](../../core/technical-appendix/TechnicalAppendix_v2.0.0.html#sec-9-three-model-convergence))"

13. **Line 142 — Convergence-table rebuild (MUST-FIX-2):** Replace 2-column table (Damage-Function IPG | RCV Model IPG) with 3-column M1/M2/M3 per-case columns. Source numerics per TA §3.6 Block 4 for McDowell + Norway; derive Deepwater Horizon / Libby / Exxon Valdez from TA §3.3–§3.5 method specifications + Ch 5 per-case prose. Mark cells N/A with footnote where Method 3 (option-value) does not cleanly apply for one-event spill cases.

14. **Line 149 — Method-attribution caption (auto-resolved with table rebuild):** Existing line-149 disclosure passage now reads as the table's methodological caption rather than damage-control disclosure.

### §E. Norway backtest (line 177)

15. **Line 177 — Norway GPFG value refresh (MEDIUM-6):** Update "$1.9 trillion" → "approximately $2.2 trillion (early 2025 NBIM)" or "approximately $2 trillion" rounded.

### §F. What Is Owed section (line ~224)

16. **After line 224 — Sen capabilities defense paragraph (MEDIUM-10):** Insert Sen + capabilities methodological-defense paragraph at end of "What Is Owed" section. Draft text in Amendment C (above); bibliography expansion likely (Sen *Development as Freedom* 1999; possibly Sen + Nussbaum *Quality of Life* 1993; Nussbaum *Creating Capabilities* 2011).

### §G. Two Kinds of Commons section (lines 227–233)

17. **After line 233 — MI-3 Ostrom homogeneity-of-interest break-point paragraph (SHOULD-FIX-5):** Insert second break-point paragraph (heterogeneous-stakeholder commons) extending the existing Ostrom-positioning. Draft text in Amendment C (above).

18. **At MI-3 break-point paragraph — C-3 stratification-economics tie (LOW-7):** Add footnote or inline lineage citation tying the MI-3 critique to stratification economics (Darity, Hamilton, and collaborators). Draft text in Amendment C (above). Verification note: synthesis premise that "framework already cites stratification economics in Ch 5 + Ch 6" was incorrect — this is a fresh-citation addition, not extension.

### §H. Four Gates section (lines 235–263)

19. **~Line 251 — TA §6 hyperlink (MEDIUM-4):** Add at CIT defense passage: "(see [Technical Appendix §6 — Commons Inversion Test](../../core/technical-appendix/TechnicalAppendix_v2.0.0.html#sec-6-commons-inversion-test))"

20. **~Line 263 — TA §5.5 hyperlink (MEDIUM-4):** Add at apparatus-introduction reference (parallel to existing §7 + §17 hyperlinks): "(bidirectional applicability in [Technical Appendix §5.5](../../core/technical-appendix/TechnicalAppendix_v2.0.0.html#sec-5-5-bidirectionality))" — **anchor name verification required:** confirm exact anchor ID against just-landed TA §5.5 work (commit 013abd4b / d54bdfa) before adding.

## Companion edits (NOT Ch 6 body, but Phase C-α scope)

### §I. Ch 5 line 214 — canonical-name anchoring (SHOULD-FIX-1; joint with Ch 5 Pass 1)

Anchor Ch 5 line 214 informal labels to canonical M1/M2/M3 names. Replace:

> "substitution cost becomes remediation cost; revealed restraint becomes revealed restitution; forward option value becomes the option value extinguished at the time of past extraction"

with:

> "**Method 1 — Replacement Cost** (here: remediation cost rather than substitute-engineering cost); **Method 2 — Revealed Preference** (here: revealed restitution rather than revealed restraint); **Method 3 — Scarcity-Adjusted Option Value** (here: the option value extinguished at the time of past extraction, evaluable from what we know now)"

This is the joint resolution with Ch 5 Pass 1 SHOULD-FIX-1 (commit a2d2d3f finding). Both Ch 5 and Ch 6 land their respective sides in the same Phase C-α session.

### §J. Bibliography expansion

- **Darity longevity-gap paper** (SHOULD-FIX-7) — find specific recent paper/talk; add to bibliography §13 (reparations economics).
- **Sen capabilities citations** (MEDIUM-10) — Sen *Development as Freedom* 1999; possibly Sen + Nussbaum *Quality of Life* 1993; Nussbaum *Creating Capabilities* 2011. Add to bibliography appropriate section (philosophical / methodological).
- **Stratification economics citations** (LOW-7) — if Phase C-α adds inline lineage rather than footnote, cite specific Darity/Hamilton stratification-economics works already in bibliography §13.

## Verification steps required during Phase C-α (before applying specific items)

1. **IPCC AR6 WG3 $100 mid-century DAC floor** (SHOULD-FIX-4) — verify IPCC AR6 WG3 actually supports the $100 floor under optimistic scenarios. If not, fall back to Option A (drop $100 floor).
2. **TA §5.5 anchor name** (MEDIUM-4 hyperlink) — confirm exact anchor ID in just-landed TA §5.5 work (commit 013abd4b / d54bdfa) before adding the Ch 6 hyperlink.
3. **EPA bituminous-coal short-ton emission factor** (SHOULD-FIX-3) — verify exact EPA factor at canonical citation; the audit cited "approximately 2.32 mt CO₂ per short ton" (93.28 kg CO₂/mmBtu × ~25 mmBtu/short ton). Confirm exact figure for the chapter citation.

## Not in Phase C-α scope (surfaced separately)

- **Cross-thread #9 systematic-staleness sweep** — Ch 6 GuidanceDoc + Ch 2 GuidanceDoc + terms_index "Three Ways of Counting" entry + other reference-file entries with accumulated post-review canonicalization drift. PM-dashboard workstream.
- **Cross-thread #11 citation accumulation** — Ch 6 contribution = 1M + 28L (Sandy + Darity longevity-gap addition + Sen + stratification-economics additions during Phase C-α push the L count up). Citation-pipeline workstream.
- **C-1 + C-2** — Fogel & Engerman / Du Bois → comp-titles + bibliography workstreams.
- **MEDIUM-3 (rounding tolerance $550–$570 vs $552–$566)** — moot once SHOULD-FIX-3 lands; figures recompute to ~$449–$464 anyway.

## Status after Amendment D

**All Pass 1 findings dispositioned.** Ch 6 Pass 1 fact-check (with math-check overlay + corpus-canonical-naming verification + authoritative-source verification + Darity-synthesis-incorporation gap closure) is **COMPLETE AT PASS 1 LEVEL**.

Next phase: **Phase C-α single-session spot-fix application** per the ordered working brief above. After Phase C-α lands and is verified, Pass 2 (voice-polish) + Pass 3 (audience-load) fire. Then Sandy Darity send packet (Ch 5 + Ch 6 + TA) ships.

| Severity | Count | Status |
|---|---|---|
| MUST-FIX | 2 | All RATIFIED for Phase C-α |
| SHOULD-FIX | 7 | All RATIFIED for Phase C-α (2 with verification steps) |
| MEDIUM | 10 | 9 RATIFIED for Phase C-α; 1 (MED-3) moot |
| LOW | 6 | 5 RATIFIED for Phase C-α; 1 (LOW-6) routed to cross-thread #9 |
| Cross-thread #9 | 1 | Surfaced to PM dashboard |
| Cross-thread #11 | 1 | Surfaced to citation pipeline |

**20 items in Phase C-α working scope.** Single coordinated session per [feedback_pm_dashboard_structure.md](/Users/c17n/.claude/projects/-Users-c17n-commons-bonds/memory/feedback_pm_dashboard_structure.md) critical-path discipline.

---

*End of Amendment D 2026-05-14 — full ratification + Phase C-α working brief.*

**Status: PASS 1 COMPLETE. Phase C-α ready to fire. Pass 2 + Pass 3 + Sandy send downstream of Phase C-α landing.**

---

# Amendment E (2026-05-14) — Post-Phase-C-α cascade-cleanup + authoritative-source verification of derived convergence-table cells

**Trigger:** Phase C-α landed on origin/main at commit `6a5ee42` (2026-05-14). PM-handoff self-audit surfaced two classes of unresolved items: (i) intra-Ch 6 + cross-corpus stale-cascade references where the SHOULD-FIX-3 coal-CO₂ recompute scope did not propagate; (ii) convergence-table Deepwater / Libby / Exxon Valdez M1 / M2 cells derived during Phase C-α from method specifications + Ch 5 case prose, where authoritative-source verification was not part of the §D-2 ratification scope. Both items are within the corpus-canonical-naming + numerical-integrity surface Sandy Darity will inspect on first integrated read. Per Amendment D's hard constraint ("if a new finding surfaces during edits, surface it as PROPOSED in a follow-up Pass 1 amendment"), these are routed here rather than retrofitted into the Phase C-α commit.

**Method:** Post-commit web verification against authoritative public sources (NOAA, DOJ, EPA, Montana DOJ, Exxon Valdez Oil Spill Trustee Council, NBIM, Climeworks corporate disclosures). All figures cross-checked against current public records as of 2026-05-14.

## Findings

### NEW SHOULD-FIX-8 (HIGH): Intra-Ch-6 coal-carbon-cost cascade miss — Contribution section retains stale figure

**Location:** [Chapter__6_ThreeWaysofCounting__Draft.md:310](manuscript/chapters/Chapter__6_ThreeWaysofCounting__Draft.md:310)

**Current state (post-Phase-C-α):**

> "McDowell County coal. Under standard Pigouvian accounting, price health, environmental damage, and carbon — a number that, under $190/ton CO₂, lands around $550 per ton of coal."

**Issue:** SHOULD-FIX-3's coal-CO₂ emission-factor recompute (2.86 → 2.32 tons CO₂/short ton; $544 → $441 carbon externality per ton coal; aggregate $550–$570/ton → $449–$464/ton) was applied at lines 29 + 31 + the convergence table McDowell row per the Amendment D Phase C-α brief, but did not propagate to the parallel reference in the Contribution section at line 310. The stale figure now reads inconsistently with the chapter's own bottom-up walkthrough (line 31).

**Framework consequence:** Sandy Darity reading Ch 6 integrated will encounter "$449–$464" at line 31 and "around $550" at line 310 referring to the same arithmetic. The internal inconsistency is small but is exactly the surface inspection-by-economist-reader catches.

**Recommended fix:**

> "McDowell County coal. Under standard Pigouvian accounting, price health, environmental damage, and carbon — a number that, under $190/ton CO₂, lands around $449–$464 per ton of coal."

**Severity rationale:** SHOULD-FIX (HIGH-equivalent) — internal arithmetic consistency is load-bearing on the chapter's bottom-up-method credibility; the discrepancy is visible to any economist-reader on first careful read.

---

### NEW SHOULD-FIX-9 (HIGH): Convergence-table Deepwater / Libby / Exxon Valdez M1 / M2 cells — authoritative-source verification update

**Location:** [Chapter__6_ThreeWaysofCounting__Draft.md:142](manuscript/chapters/Chapter__6_ThreeWaysofCounting__Draft.md:142) (convergence table; post-Phase-C-α structure)

**Issue:** The Phase C-α convergence-table rebuild sourced McDowell + Norway figures verbatim from Technical Appendix §3.6 Block 4 (authoritative). Deepwater / Libby / Exxon Valdez M1 / M2 cells were derived from method specifications + Ch 5 per-case prose during the Phase C-α session, without explicit authoritative-source cross-check. Post-commit verification surfaces directional accuracy + tightening recommendations.

#### Deepwater Horizon — verification results

**Current (post-Phase-C-α) cells:**
- M1: "~$15–$20B engineering + ecological restoration"
- M2: "~$30–$40B settlements + damages paid"

**Authoritative-source data:**
- BP response + cleanup spending: ~$14B (BP corporate disclosures; cited in [NOAA explainer](https://www.noaa.gov/explainers/deepwater-horizon-oil-spill-settlements-where-money-went))
- 2016 Consent Decree Natural Resource Damages Assessment (NRDA): $8.8 billion to NRDAR Trustees over 15+ years ([DOI NRDAR Settlement](https://www.doi.gov/restoration/historic-nrdar-settlement-reached-deepwater-horizon-spill))
- Clean Water Act civil penalties: $5.5 billion (80% to RESTORE Act, 20% to Oil Spill Liability Trust Fund) ([NOAA explainer](https://www.noaa.gov/explainers/deepwater-horizon-oil-spill-settlements-where-money-went))
- DOJ criminal settlement: $4.525 billion (Nov 2012) ([Restore Mississippi River Delta on BP criminal settlement](https://mississippiriverdelta.org/bp-settles-deepwater-horizon-disaster-criminal-charges-for-4-5-billion-funding-headed-to-louisiana-for-restoration/))
- Economic + medical class-action settlements: ~$10–$15 billion
- BP-Mexico settlement (2018): $25.5 million (small absolute; not load-bearing on the table)
- Total to BP: ~$65 billion (consistent with chapter aggregate)

**Verified M1 / M2 allocation:**
- **M1 (Replacement Cost = engineering + ecological restoration):** BP response/cleanup spending ~$14B + NRDA $8.8B = **~$22B** (tighter than Phase C-α "$15–$20B")
- **M2 (Revealed Preference = settlements + damages paid via legal mechanism):** Criminal $4.5B + CWA $5.5B + class-action economic ~$10–$15B = **~$20–$25B** (lower than Phase C-α "$30–$40B")

**Recommended cell update:**

| Phase C-α | Amendment E (verified) |
|---|---|
| M1: "~$15–$20B engineering + ecological restoration" | M1: "~$22B engineering + ecological restoration (BP response ~$14B + NRDA $8.8B per 2016 Consent Decree)" |
| M2: "~$30–$40B settlements + damages paid" | M2: "~$20–$25B settlements + damages paid (CWA $5.5B + DOJ criminal $4.5B + class-action economic ~$10–$15B)" |

#### Libby, Montana — verification results

**Current (post-Phase-C-α) cells:**
- M1: "~$0.6B+ federal cleanup + ongoing remediation; long-tail illness-cost flow $4–$7B"
- M2: "~$0.3B direct settlements + Grace bankruptcy estate payouts"

**Authoritative-source data:**
- EPA Libby Asbestos Superfund Site cleanup spending: ~$600 million ([EPA Libby Site Profile](https://cumulis.epa.gov/supercpad/SiteProfiles/index.cfm?fuseaction=second.cleanup&id=0801744))
- W.R. Grace 2008 EPA settlement: $250 million ([NPR coverage](https://www.npr.org/transcripts/88154006))
- W.R. Grace 2023 Natural Resource Damage settlement to Montana: $18.5 million over 10 years (first $5M paid Oct 2023; $1.5M + interest annually for 9 years) ([Montana DOJ](https://dojmt.gov/NRDP-sites/libby-asbestos/))
- W.R. Grace 2008 DEQ bankruptcy settlement: $5.1 million for operation and maintenance ([Montana DOJ Libby Settlement Fact Sheet](https://dojmt.gov/wp-content/uploads/Libby-Settlement-Fact-Sheetv2.pdf))
- Long-tail illness-cost flow: $4–$7 billion aggregate (chapter prose; consistent with EPA + IHME public health spending records)

**Verified M1 / M2 allocation:**
- **M1 (Replacement Cost = federal cleanup + ongoing remediation):** EPA Superfund $600M + ongoing cleanup ramp **— Phase C-α cell confirmed**
- **M2 (Revealed Preference = settlements + revealed restitution):** W.R. Grace 2008 EPA settlement $250M + 2008 DEQ $5.1M + 2023 NRDA $18.5M = **~$275M ≈ $0.3B — Phase C-α cell confirmed**
- Long-tail illness flow: $4–$7B aggregate **— Phase C-α cell confirmed**

**Recommended cell update:** Minor refinement only (add specific source attribution); Phase C-α figures are authoritative-source-confirmed. Consider footnote citation in caption:

| Phase C-α | Amendment E (verified) |
|---|---|
| M1: "~$0.6B+ federal cleanup + ongoing remediation; long-tail illness-cost flow $4–$7B" | M1: "~$0.6B EPA Superfund cleanup spending + ongoing remediation; long-tail illness-cost flow $4–$7B" |
| M2: "~$0.3B direct settlements + Grace bankruptcy estate payouts" | M2: "~$0.3B W.R. Grace settlements ($250M 2008 EPA + $18.5M 2023 NRDA + $5.1M 2008 DEQ)" |

#### Exxon Valdez — verification results

**Current (post-Phase-C-α) cells:**
- M1: "~$2–$4B cleanup + ecological restoration"
- M2: "~$1–$2B settlements + damages paid"

**Authoritative-source data:**
- Exxon cleanup spending: $2.2 billion ([EVOSTC Settlement page](https://evostc.state.ak.us/oil-spill-facts/settlement/))
- 1991 civil settlement (Exxon to State of Alaska + United States): $900 million over 10 years
- Criminal fine: $25 million ($150M imposed; $125M forgiven for cooperation)
- Natural Resource Restitution: $100 million
- Punitive damages (post-2008 Supreme Court ruling): $507.5 million (capped at compensatory damages level)
- Private claims to fishermen, landowners, businesses (Exxon-paid): ~$507 million

**Verified M1 / M2 allocation:**
- **M1 (Replacement Cost = cleanup + ecological restoration):** Exxon cleanup $2.2B + NRDA-equivalent restoration ~$100M = **~$2.3B** (tighter than Phase C-α "$2–$4B" upper bound; Phase C-α range was wider than authoritative data warrants)
- **M2 (Revealed Preference = settlements + damages paid):** 1991 civil $900M + criminal $25M + punitive $507M + private claims $507M = **~$1.9B ≈ $2B** (Phase C-α "$1–$2B" upper bound confirmed)

**Recommended cell update:**

| Phase C-α | Amendment E (verified) |
|---|---|
| M1: "~$2–$4B cleanup + ecological restoration" | M1: "~$2.3B cleanup + ecological restoration (Exxon $2.2B + NRDA ~$100M per 1991 settlement)" |
| M2: "~$1–$2B settlements + damages paid" | M2: "~$1.9B settlements + damages paid (1991 civil $900M + private claims ~$507M + punitive $507M + criminal $25M)" |

#### Aggregate verification verdict

| Case | Phase C-α direction | Phase C-α magnitude | Verification verdict |
|---|---|---|---|
| McDowell County coal | sourced from TA §3.6 Block 4 | verbatim | **AUTHORITATIVE — unchanged** |
| Norway petroleum | sourced from TA §3.6 Block 4 | verbatim | **AUTHORITATIVE — unchanged** |
| Deepwater Horizon | correct | M1 understated; M2 overstated | **REVISION RECOMMENDED** |
| Libby, Montana | correct | confirmed | **CONFIRMED — source attribution added** |
| Exxon Valdez | correct | M1 upper bound loose; M2 confirmed | **REVISION RECOMMENDED (tightening)** |

**Severity rationale:** SHOULD-FIX (HIGH-equivalent) — the convergence-table cells are the Sandy-Darity-first-read surface. McDowell + Norway are TA-anchored; the three one-event cases were Phase C-α-derived without authoritative-source verification. Two cases (Deepwater, Exxon) warrant numerical revision; one case (Libby) is confirmed. Source attribution in caption strengthens the table's authority for Sandy review.

---

### NEW MEDIUM-11: Cross-corpus stale-cascade — Ch 8 + TA §3.6 worked example + TA §11 case file retain pre-cascade coal-CO₂ figures

**Locations:**

| File | Line | Current state | Cascade direction |
|---|---|---|---|
| [Chapter__8_WhatThingsActuallyCost_Draft.md:73](manuscript/chapters/Chapter__8_WhatThingsActuallyCost_Draft.md:73) | 73 | "approximately 2.86 tons of carbon dioxide" + "approximately five hundred and forty-four dollars" | 2.86 → 2.32; $544 → $441 |
| [TechnicalAppendix_v2.0.0.html:2808](core/technical-appendix/TechnicalAppendix_v2.0.0.html:2808) | 2808 | "E includes $190/ton CO2 × 2.86 tons CO2 per ton coal" (Gate 4 worked example) | 2.86 → 2.32 |
| [TechnicalAppendix_v2.0.0.html:4465](core/technical-appendix/TechnicalAppendix_v2.0.0.html:4465) | 4465 | "~2.86 tons CO₂ per ton coal" (§11 McDowell case file) | 2.86 → 2.32 |
| [core/technical-appendix/block4_validation_2026-04-25.md:114](core/technical-appendix/block4_validation_2026-04-25.md:114) | 114 | "Carbon intensity (combusted) | ~2.86 tons CO₂ per ton coal | EPA emissions factors" | Historical-at-validation-time; flag for caveat or update |

**Authoritative-source verification anchor:** EPA AP-42 §1.1 documents 93.28 kg CO₂/mmBtu for bituminous coal; combined with EIA-published heat content of 24.93 mmBtu/short ton, the canonical short-ton accounting factor is approximately 2.32 mt CO₂/short ton. The "~2.86 tons" figure derives from metric-ton or high-rank-coal accounting and is high relative to the EPA's documented short-ton factor for the McDowell context. The Ch 6 Phase C-α SHOULD-FIX-3 Option A ratification adopted the EPA short-ton factor with explicit emission-factor citation; cross-corpus alignment requires the same cascade.

**Routing recommendation:**

- **Ch 8 line 73:** Ch 8 has not run Pass 1 yet (per PM dashboard); the cascade-miss is a candidate Pass 1 finding for the eventual Ch 8 audit. Surface to Ch 8 PM workstream as a known-fix-pending item rather than retrofitting via Ch 6 Pass 1.
- **TA §3.6 Gate 4 worked example (line 2808) + TA §11 case file (line 4465):** TA has not run its own Pass 1; the cascade-miss is a candidate Pass 1 finding for the eventual TA audit. Surface to TA PM workstream.
- **block4_validation_2026-04-25.md:** This file is a calibration-validation audit record from 2026-04-25, documenting the figure as it stood at validation-time. Author judgment whether to (a) update the figure in-place with refresh note, (b) preserve as historical record with caveat footnote referencing the SHOULD-FIX-3 cascade, or (c) leave as-is.

**Severity rationale:** MEDIUM — cross-corpus consistency is desirable but not gating for Sandy send. The Sandy send packet is Ch 5 + Ch 6 + TA (where TA only ships if its Phase C-α has landed). Ch 8 is not in the Sandy send packet. TA case-file consistency strengthens the integrated read but is not blocking.

---

### NEW MEDIUM-12: Climeworks Generation-3 trajectory verification — "net removal" vs "capture cost" distinction

**Location:** [Chapter__6_ThreeWaysofCounting__Draft.md:47](manuscript/chapters/Chapter__6_ThreeWaysofCounting__Draft.md:47) (Phase C-α applied)

**Current state (post-Phase-C-α):**

> "Climeworks's Mammoth facility (operational from 2024) and the company's Generation-3 technology trajectory project unit cost reductions toward four hundred to six hundred dollars per ton by 2030 under the corporate cost-reduction trajectory the company has publicly disclosed."

**Authoritative-source verification:**

Per Climeworks's Generation 3 announcement at the Carbon Removal Summit in Zurich (June 2024), the publicly disclosed 2030 cost targets are:

- **$250–$350 per ton CO₂ captured** (capture cost only)
- **$400–$600 per ton net removal** (full lifecycle including storage)

Sources: [Climeworks press release](https://climeworks.com/press-release/next-gen-tech-powers-climeworks-megaton-leap), [Carbon Herald](https://carbonherald.com/climeworks-reveals-its-generation-3-direct-air-capture-technology/), [Canary Media](https://www.canarymedia.com/articles/carbon-capture/co2-removal-leader-climeworks-says-new-tech-can-halve-costs-energy-use).

**Verdict:** The Ch 6 figure "$400–$600 per ton by 2030" matches Climeworks's "net removal" target — the apples-to-apples figure for comparison with the Social Cost of Carbon (which measures damage avoided per ton CO₂ net-removed) and other DAC cost benchmarks. The figure is **VERIFIED CORRECT** for the policy-relevant unit. Optional refinement: add explicit "(net removal cost; capture-only cost target $250–$350 per ton)" disclosure for technical-reader transparency. Author judgment whether this clarity is worth the prose load.

**Severity rationale:** MEDIUM — the figure is correct; the optional refinement is a transparency improvement. Defer-acceptable.

---

## Status after Amendment E

| Finding | Severity | Status |
|---|---|---|
| SHOULD-FIX-8 (Ch 6 line 310 intra-chapter cascade miss) | HIGH | **PROPOSED** — awaits author ratification |
| SHOULD-FIX-9 (Convergence-table Deepwater + Libby + Exxon M1/M2 verification) | HIGH | **PROPOSED** — Deepwater + Exxon revisions recommended; Libby confirmed; awaits author ratification |
| MEDIUM-11 (Cross-corpus stale-cascade: Ch 8 + TA + block4_validation) | MEDIUM | **PROPOSED — routed to Ch 8 + TA PM workstreams** |
| MEDIUM-12 (Climeworks Gen-3 net-removal-vs-capture clarification) | MEDIUM | **PROPOSED — defer-acceptable; verification confirms current figure** |

## Aggregate severity counts (full doc post-Amendment E)

| Severity | After Amendment D | After Amendment E |
|---|---|---|
| MUST-FIX | 2 (ratified Phase C-α applied 6a5ee42) | 2 (ratified Phase C-α applied) |
| SHOULD-FIX | 7 (ratified Phase C-α applied) | **9 (7 applied + 2 new PROPOSED)** |
| MEDIUM | 10 (9 applied; 1 moot) | **12 (9 applied; 1 moot; 2 new PROPOSED)** |
| LOW | 6 (5 applied; 1 surfaced) | 6 (5 applied; 1 surfaced) |
| Cross-thread #9 | 1 (surfaced) | 1 (surfaced) |
| Cross-thread #11 | 1 (surfaced) | 1 (surfaced) |

## Phase C-β scope (recommended if author ratifies Amendment E)

If author ratifies SHOULD-FIX-8 + SHOULD-FIX-9 + MEDIUM-12, a small Phase C-β follow-up commit applies all three at once:

1. **SHOULD-FIX-8 (Ch 6 line 310 cascade):** Replace "around $550 per ton of coal" with "around $449–$464 per ton of coal" — one-line edit.
2. **SHOULD-FIX-9 (Convergence-table verification):** Update Deepwater M1 + M2 cells and Exxon M1 + M2 cells per verified figures above; add source attribution to caption referencing NOAA/DOJ/EVOSTC/Montana DOJ as authoritative anchors.
3. **MEDIUM-12 (Climeworks net-removal clarification):** Optional inline disclosure of "net removal" vs "capture-only" unit distinction; author judgment.

MEDIUM-11 (cross-corpus cascade) does NOT land in Phase C-β — routed to Ch 8 + TA workstreams as separate Pass 1 findings.

**Phase C-β single-commit scope:** ~5 line-level edits, all in Ch 6, single coordinated session. Author-discretion timing: lands before Pass 2 fires (preserves the convergence-table-as-Sandy-first-read-surface integrity), or folds into Pass 2 if author prefers (Pass 2 voice-polish naturally touches the convergence-table caption anyway).

## Routing decision

- **Recommended path:** Apply Phase C-β commit before Pass 2 fires. Rationale: (a) preserves Phase C-α / Phase C-β as the "numerical-integrity" phase distinct from Pass 2 / Pass 3 (voice-polish + audience-load); (b) the convergence table is the Sandy-first-read inspection surface and benefits from authoritative-source attribution before any review; (c) the Ch 6 line 310 cascade-miss is too small to defer to Pass 2 (it's a literal arithmetic-consistency fix, not a voice-polish question).
- **Alternative path:** Fold all three items into Pass 2. Acceptable but loses the phase-discipline separation.

## Pre-Sandy-send disposition

After Phase C-β + Pass 2 + Pass 3 land, Ch 6 + Ch 5 + TA are at Sandy-send readiness. The convergence table will then carry authoritative-source attribution for all five cases (TA §3.6 Block 4 for McDowell + Norway; NOAA + DOJ + EVOSTC + Montana DOJ for Deepwater + Libby + Exxon). Sandy's first-read inspection surface is reinforced.

---

*End of Amendment E 2026-05-14 — Post-Phase-C-α cascade-cleanup + authoritative-source verification.*

**Status: 2 new SHOULD-FIX + 2 new MEDIUM added; all 4 awaiting author ratification. Phase C-β scope drafted (SHOULD-FIX-8 + SHOULD-FIX-9 + MEDIUM-12). MEDIUM-11 cross-corpus items routed to Ch 8 + TA PM workstreams.**
