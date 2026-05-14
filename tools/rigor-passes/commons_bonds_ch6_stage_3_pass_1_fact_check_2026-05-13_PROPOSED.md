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
