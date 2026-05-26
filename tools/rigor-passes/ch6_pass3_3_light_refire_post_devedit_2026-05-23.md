# Ch 6 — Stage-3 Pass 3.3 (Audience-Load Acceptance) light re-fire, post-Pass-3.5 developmental-edit application

**Status:** **RATIFIED 2026-05-25** — author ratified the 7-character delta verdict (4 ✓✓✓ + 3 ✓✓; 0 EXCLUDE; 6 LIGHTLY STRENGTHENED + 1 PRESERVED + 0 PERTURBED; READY TO SUBMIT AS-IS). **Stage 4 render-audit ratified as author-managed-offline** per author 2026-05-25 instruction (render pipeline session; no agent involvement) — see §8 below. Stage 5 fires next; see [`tools/quality-gates/sign-offs/ch6_stage5_signoff_2026-05-25.md`](../quality-gates/sign-offs/ch6_stage5_signoff_2026-05-25.md). (Originally PROPOSED 2026-05-23.)
**Date:** 2026-05-23 (PROPOSED) / 2026-05-25 (RATIFIED + Stage 4 author-offline marker).
**Branch:** `claude/ch6-pass-3-3-light-refire-1fae85` (branched from `origin/main` at `5f875a6`).
**Scope:** light Pass 3.3 acceptance re-fire across the canonical 7-character set, testing whether the Ch 6 dev-edit Phase C application (commit `713fbe1`, 2026-05-21) preserves, lightly strengthens, or perturbs the prior Pass 3.3 verdict (7 INCLUDE / 0 EXCLUDE; READY TO SUBMIT AS-IS; Phase C-ε CLOSED EMPTY 2026-05-15).
**Workstream rationale:** per pipeline doctrine v1.0.0 Amendment B + dev-edit workstream handoff §3.1 step 10, a light Pass 3.3 re-fire is recommended after Phase C application of dev-edit spot-fixes to confirm cumulative acceptance verdicts hold across the audience pressure-test character set. Pass 3.4 robustness re-fire NOT routinely warranted per the same step (restorations strengthen rather than weaken adversarial robustness; thread-pull surface unchanged).

---

## §0. Source artifacts read

- [tools/rigor-passes/ch6_developmental_edit_review_2026-05-20.md](tools/rigor-passes/ch6_developmental_edit_review_2026-05-20.md) §11 Disposition log + §11.2 Per-finding application detail + §11.4 Cross-pass impact confirmation (the canonical ground-truth for what changed at each restoration site).
- [tools/rigor-passes/commons_bonds_ch6_stage_3_pass_3_audience_load_2026-05-14_PROPOSED.md](tools/rigor-passes/commons_bonds_ch6_stage_3_pass_3_audience_load_2026-05-14_PROPOSED.md) §3 (Tier-1 + Tier-2 + Tier-3 character set construction) + §4 (per-character verdicts) + §7.1 (per-character tally) + the Phase C-ε disposition (2026-05-15 CLOSED EMPTY).
- [manuscript/chapters/Chapter__6_ThreeWaysofCounting.md](manuscript/chapters/Chapter__6_ThreeWaysofCounting.md) at `origin/main` head `5f875a6` (365 lines post-dev-edit, post-Phase-C-α/β/γ/δ/ε, post-cascade-followup `e927e74`, post-coal-CO₂-methodology-reconciliation `914addc`, post-line-21 Black Lung reframe `5569600`).
- [tools/rigor-passes/commons_bonds_ch6_stage3_pass_3_4_audience_load_robustness_2026-05-18.md](tools/rigor-passes/commons_bonds_ch6_stage3_pass_3_4_audience_load_robustness_2026-05-18.md) §0–§1 — verified CONDITIONALLY ROBUST verdict; thread-pull surface unchanged scope context for cascade-flag disposition.
- CLAUDE.md branch-discipline + merge-to-main + named-subject consent + three-pass-rigor discipline references.
- `tools/memory/feedback_audience_aware_drafting_discipline.md` v3.1 Amendment B + §3.2 explicit-gate cascade rule for Pass 3.5 + light Pass 3.3 re-fire-after-dev-edit framing.

---

## §1. What this pass IS (and what it is NOT)

**This pass IS** a light per-character delta re-application of the canonical 7-character Pass 3.3 set to the post-dev-edit chapter state. For each character: prior verdict cited, restoration-site impact identified, post-restoration verdict, delta classification (PRESERVED / LIGHTLY STRENGTHENED / PERTURBED).

**This pass is NOT** a re-construction of the Ch 6 audience pressure-test character set (use the prior Pass 3.3 §3 set as-built); a re-litigation of Pass 3.1 / 3.2 / 3.4 dispositions (all held per dev-edit §11.4); a re-litigation of the Phase C-ε Tier-B-optional disposition (held per 2026-05-15 affirmative author review); a verification of the "three percent" Norway spending-rule figure against the Technical Appendix (separate pre-publication verification cascade per dev-edit §11.6); a re-fire of Pass 3.4 robustness (NOT routinely warranted per workstream handoff §3.1 step 10); a propagation cascade beyond Ch 6 (no other chapter files touched); or a Stage 4 render audit (separate explicit-gate cascade).

---

## §2. Dev-edit restoration sites — quick reference

Per dev-edit §11.2 Phase C application detail, nine of twelve ratified findings applied to the chapter file in commit `713fbe1` (2026-05-21), producing +22 net lines (341 → 363) at application time; the chapter currently stands at 365 lines after the subsequent line-21 Black Lung reframe + coal-CO₂ methodology cascade landed (commits `5569600` + `914addc`).

| Finding | Where applied (post-app line refs) | Restoration polarity | Audience surfaces touched |
|---|---|---|---|
| F-DE-Ch6-3 (Option D = B+C) | Opening lines 10–20 | Re-paragraphation at natural beats + cut how-to-read directive | All Tier-2 + Tier-3; Tier-1 PRESERVES |
| F-DE-Ch6-5 (Option C = A+B) | Approach 1 community paragraph lines 32–36 + §-break line 41 | Darity-lineage standalone-paragraph treatment + carbon-pivot §-break | Tier-1 (Sandy) + Tier-2 (Sandel-trade-press) + Tier-3 (layman + reparations) |
| F-DE-Ch6-9 | Externality-tail name-defense line 121 (relocated from prior position) | Name-defense relocated to coda after term-by-term translation | Tier-2 (Sandel-trade-press) reads cumulative-load improvement; Tier-1 PRESERVES content |
| F-DE-Ch6-2 (Option C = A+B) | M2 paragraph line 141 lightening + Norway Backtest concrete-texture paragraph line 221 + per-citizen-accounting relocation line 225 | M2 limit-naming light + Norway concrete-texture restored (1990 / 1996 / spending rule / 1991 carbon tax / ethics council) | All Tier-1 + Tier-2 + Tier-3; LIGHTLY STRENGTHENS Berggruen + academic-econ + layman + Sandel-trade-press materially |
| F-DE-Ch6-7 | Norway Backtest closer split lines 227–229 | Norway differentiation / acknowledgment pivot paragraph-split | Tier-2 (Sandel-trade-press) + Tier-3 (layman) |
| F-DE-Ch6-1 | Convergence finding §-break line 197 | Central-finding paragraph + meta-naming paragraph paginated separately | Tier-1 (Berggruen) + Tier-2 (Sandel-trade-press) + Tier-3 (layman) |
| F-DE-Ch6-4 | Four-gates worked-example sentences lines 307 / 309 / 311 | DALY/WTP + infinite-intergenerational + Cohesion/Habitability double-count examples | Tier-2 (academic-econ + Sandel-trade-press) + Tier-3 (layman) materially |
| F-DE-Ch6-6 | Contribution section §-breaks lines 333 / 337 | Three-additions paragraph-rhythm matching structural claim | Tier-1 (Berggruen) + Tier-2 (Sandel-trade-press) + Tier-3 (layman) materially |
| F-DE-Ch6-8 | What Is Owed §-break line 271 + Sen-pairing standalone paragraph line 273 | Parfit-grounding cluster + Sen-pairing paginated separately | Tier-1 (Sandy + Berggruen) + Tier-3 (reparations) |

All restoration polarities are structural (paragraph-rhythm relief + §-break insertion + paragraph relocation) + one concrete-texture insertion (F-DE-Ch6-2 Norway 5-sentence paragraph) + three worked-example sentences (F-DE-Ch6-4 gates 2/3/4). No content was cut; one how-to-read directive was relocated from the opening to its natural home at the formula-introduction (line 94, where the plain-English-before-formula discipline now does the same orientation work in context).

---

## §3. Per-character delta verdicts

Per the §1 light-re-fire format: prior Pass 3.3 verdict cited, post-restoration delta identified at restoration sites this character reads for, post-restoration verdict on canonical scale, delta type.

### Tier 1 — gating audiences

#### 1. Sandy Darity — Tier 1 reader

**Prior Pass 3.3 verdict (2026-05-14):** ✓✓✓ INCLUDE — SI-1 framing intact at "deepest single-line case" surface; longevity-gap lineage at line 25 explicit; Method 2 backward-application list at line 132 substantively engages Darity-Mullen 2020 alongside four other restitution-tradition anchors; MI-3 stratification economics tie at line 262 names Sandy's analytical apparatus directly; counter-argument structure rigorous on falsifiability; Parfit+Sen pairing grounds the philosophical standing + valuation; Restitution Bond methodology specialization explicitly attributed to Darity-Mullen at line 248. The line 21 Black Lung Trust Fund attribution was the only Sandy-flag item (since resolved by commit `5569600` before Phase C-ε close).

**What lands post-restoration.**

- **SI-1 framing — verified intact at line 137** (post-app numbering; previously line 124). The three load-bearing sentences (*markets do have a mechanism... markets do not have an equivalent mechanism... the three estimation methods are the framework's substitute*) survive verbatim. Sandy's "deepest single-line case" surface unchanged. Per task brief hard constraint honored.
- **Longevity-gap legacy-effect lineage paragraph now stands alone at line 34** (F-DE-Ch6-5 Option C re-paragraphation). Previously embedded inside the community-paragraph substrate-enumeration; now sits as a discrete paragraph between the cost-enumeration close ("...thirteen years, in McDowell County, against the national average.") and the standalone $5–$15 cost-estimate closer at line 36. Sandy reads his methodology + "the methodology travels; the per-context calibration is what differs" framing with paragraph-rhythm matching the substantive engagement.
- **Method 2 backward-application list at line 145** — content unchanged (Holocaust reparations + 1988 Civil Liberties Act + Black Lung Trust Fund payouts + South African TRC + Darity-Mullen 2020). Position only.
- **MI-3 stratification economics tie at line 285** — content unchanged. Sandy's analytical apparatus (Darity + Hamilton + collaborators) named directly + framed as the apparatus the framework's commons-governance extension applies to heterogeneous-stakeholder commons.
- **Parfit-grounding cluster + Restitution-Bond cross-reference now closes at line 269** ("portable mechanism, per-context calibration"). §-break at line 271. Sen-pairing now stands alone at line 273. Sandy reads two discrete philosophical-grounding moves (Parfit-impersonal-outcomes + Sen-capability-valuation) with paragraph-rhythm matching the cross-tradition synthesis the framework operates within (F-DE-Ch6-8).
- **Line 28 Black Lung reframe** (commit `5569600` pre-Phase-C-ε): *"the federal Black Lung Benefits Program's approximately $44 billion in distributions through 2009 (GAO/CRS), allocated across the national tonnage of coal produced since the Program's 1969 establishment, runs between one and one and a half dollars per ton (Chapter 2 walks the program's Trust Fund — its funding gap, debt trajectory, and structural mechanics — in detail)."* Sandy's only flag from the prior Pass 3.3 verdict is resolved.

**What flags post-restoration.** None.

**Post-restoration verdict: ✓✓✓ INCLUDE — LIGHTLY STRENGTHENED.** The Darity-lineage paragraph's standalone treatment + the Sen-pairing's standalone treatment together give Sandy's two principal load-bearing surfaces dedicated paragraph-rhythm rather than embedded-in-cluster treatment. The SI-1 surface preserved verbatim. Line 28 Black Lung flag already resolved. No surface perturbed.

---

#### 2. Berggruen Prize judge — Tier 1 reader

**Prior Pass 3.3 verdict (2026-05-14):** ✓✓✓ INCLUDE — three-additions claim explicit + lineage-attributive; RCV name-defense engages Hartwick/Ostrom/Mazzucato substantively; Parfit+Sen pairing grounds the philosophical standing; Two Kinds of Commons locates the framework adjacent-to-Ostrom rather than competing; four-gates apparatus does scholarly admission-discipline; convergence-table figures TA-aligned post-cascade-followup; Asymmetric Regret Rule name-defense compressed but load-bearing. Cumulative name-defense + apparatus-density at the upper edge of trade-comp tolerance, but methodologically appropriate.

**What lands post-restoration.**

- **Contribution section §-breaks at lines 333 + 337** (F-DE-Ch6-6). The three additions the framework makes to its tradition — substitutability-weighting + Hotelling Identity bridge (line 329, closing at line 331 "...it formalizes what each leaves out."); integrated architecture (line 335, closing at "...how the components contribute."); Commons Inversion Test as discovery method (line 339, closing at "...each arriving with its own worked reasoning rather than by assertion.") — now stand as three distinct paragraphs separated by `---` rules. Berggruen reads "three additions, each consequential" with paragraph-rhythm matching the structural claim. The Hotelling/Pigou cross-tradition bridge passage at line 331 lands with breath. **Materially strengthens** the contribution-claim's structural register for this character.
- **Norway concrete-texture paragraph at line 221** (F-DE-Ch6-2 Option A). Five sentences of publicly-documented GPFG facts (fund established 1990 by statute, first deposit 1996, spending rule capped at expected real return ~3%, 1991 carbon tax as one of the world's earliest, ethics council with public divestment history). The convergence-claim empirical rigor for Norway-as-best-managed-extraction-case now lands with concrete institutional grounding the prior compressed thesis-paragraph lacked. Berggruen reads the differentiation move (Norway-as-Hartwick's-Rule-implemented) with empirical anchoring rather than as assertion. **Materially strengthens.**
- **Convergence finding §-break at line 197** (F-DE-Ch6-1). The central-finding paragraph ("The methods converge. Different assumptions, different foundations, same qualitative conclusion...") now stands as its own paragraph; the meta-naming paragraph ("This is the chapter's central finding, and it is worth sitting with for a moment...") sits after the `---`. Berggruen reads the convergence-claim as a paginated emphasis-moment rather than as continuation of the convergence-table validation paragraphs. **Lightly strengthens.**
- **Externality-tail name-defense relocation to line 121** (F-DE-Ch6-9). Content unchanged; position shifted from inside plain-English-orientation flow (between externality-tail component paragraph and synthesis paragraph) to coda position after the term-by-term translation. Berggruen reads the four-name-defense lineage-attribution pattern intact (lines 121 / 303 / 325 / 361) with the externality-tail defense now sitting parallel to the chapter's three other name-defense locations rather than interrupting the formula-explication flow. **Lightly strengthens** cumulative-pattern coherence; PRESERVES content.
- **What Is Owed §-break + Sen-pairing standalone paragraph** at lines 271 + 273 (F-DE-Ch6-8). Berggruen reads Parfit-grounding (impersonal-outcomes for forward-looking) and Sen-grounding (capability-valuation) as two discrete cross-tradition moves with paragraph-rhythm matching the cross-disciplinary synthesis claim. **Lightly strengthens.**

**What flags post-restoration.** None.

The "three percent" Norway spending-rule figure at line 221 carries the F-DE-Ch6-2 §11.6 pre-publication verification flag against TA Norway coverage + current Handlingsregelen rule formulation; this Pass 3.3 light re-fire reads the figure as currently stands per task brief. Berggruen Prize judge is a methodological-apparatus-rigor reader rather than a specific-figure-fact-checker; the flag is appropriately held for pre-publication verification (the actual external-send reviewer that would check Handlingsregelen specifics is closer to the academic econ reviewer character).

**Post-restoration verdict: ✓✓✓ INCLUDE — LIGHTLY STRENGTHENED (across multiple sites).** The Contribution-section §-breaks + Norway concrete-texture restoration are the two restoration sites that strengthen materially; convergence §-break + externality-tail name-defense relocation + What-Is-Owed §-break strengthen lightly. No surface perturbed.

---

### Tier 2 — pipeline-strengthening audiences

#### 3. Academic econ reviewer (AER/QJE/JPE comparable) — Tier 2 reader

**Prior Pass 3.3 verdict (2026-05-14):** ✓✓ INCLUDE — M1/M2/M3 method-specifications anchored to TA + established empirical-and-theoretical work; substitutability function honest about parameter uncertainty + sensitivity-trade-off; four-gates apparatus does formal admission-discipline; convergence-table figures TA-cascade-aligned; reproducibility counter-argument frames sensitivity-disclosure correctly. Convergence-table presentation density at the upper edge of trade-comp-convention but appropriate for the book's audience scope. No EXCLUDE concerns.

**What lands post-restoration.**

- **Four-gates worked-example sentences at lines 307 / 309 / 311** (F-DE-Ch6-4). Each gate now anchors its exclusion-discipline in a concrete health-economics or methodological-pathology example: gate 2 ("*A Disability-Adjusted Life Year, until paired with a published willingness-to-pay valuation, fails this gate.*"); gate 3 ("*A claim of infinite intergenerational damage — even one that survives Commons Inversion — fails this gate.*"); gate 4 ("*A community-disruption cost priced once as Cohesion commons-loss and again as Habitability commons-loss fails this gate until the overlap is resolved.*"). The DALY/WTP anchor signals health-economics literacy substantively; the infinite-intergenerational example anchors the boundedness gate against unbounded theoretical constructions; the double-count example anchors the independence gate against double-counting across overlapping commons categories. **Materially strengthens** the formal admission-apparatus rigor for this character — the gates now read as concrete-exclusion-discipline rather than as abstract specification.
- **Norway concrete-texture paragraph at line 221** (F-DE-Ch6-2 Option A). Method 2's revealed-preference anchor (Norway/GPFG) now grounded in five publicly-documented institutional facts (1990 statutory establishment + 1996 first deposit + spending rule ~3% expected real return + 1991 carbon tax + ethics council divestment). Academic econ reviewer reads Method 2's empirical anchor as concretely grounded rather than as compressed thesis. **Lightly strengthens** the Method 2 empirical-anchoring rigor.
- **M2 paragraph at line 141 limit-naming swap** (F-DE-Ch6-2 Option B). The previous M2-paragraph triple-claim about per-Norwegian-citizen accounting + atmospheric-externality-non-Norwegian-population + Norway-as-lower-bound is replaced with the lighter limit-naming *"The limit — what Norway's accounting does not capture — is worked through in the Norway Backtest section below."* The per-citizen-accounting + atmospheric-externality content moves to the Norway Backtest result paragraph at line 225 ("*And the fund's accounting is per-Norwegian-citizen accounting; the atmospheric externality non-Norwegian populations bear from Norwegian oil burned anywhere on Earth is not in the Government Pension Fund Global.*"). Academic econ reviewer reads the cross-reference to the section that does the work as appropriate sectional-architecture; the analytical content now lands where the Norway differentiation is being worked through rather than as M2 paragraph overhead. PRESERVES analytical content + paragraph-rhythm relief.
- **Convergence finding §-break at line 197** (F-DE-Ch6-1). The convergence claim ("*The methods converge. Different assumptions, different foundations, same qualitative conclusion and, in most cases, similar magnitudes. The direction never flips.*") now stands as its own paragraph. Academic econ reviewer reads the convergence-claim with structural emphasis matching the methodological-empirical claim. **Lightly strengthens.**

**What flags post-restoration.** The "three percent" Norway spending-rule figure at line 221 is the academic-econ-reviewer-relevant pre-publication verification flag per F-DE-Ch6-2 §11.6. Per task brief: this Pass 3.3 light re-fire reads the figure as currently stands; any TA-verification cascade is separate Phase-C-style scope. **Reads as currently stands.** Verification cascade against TA Norway coverage + current Handlingsregelen rule formulation is held for pre-publication; this Pass 3.3 verdict does not change on figure-verification grounds.

**Post-restoration verdict: ✓✓ INCLUDE — LIGHTLY STRENGTHENED.** Four-gates worked-example sentences are the materially-strengthening site; Norway concrete-texture + convergence §-break light-strengthen. No surface perturbed; pre-publication verification flag held appropriately.

---

#### 4. Sandel-tradition trade-press editor — Tier 2 reader

**Prior Pass 3.3 verdict (2026-05-14):** ✓✓ INCLUDE — plain-English-before-formula discipline at line 81; Pattern 2 register holds throughout; counter-argument structure rigorous + trade-press-editor-friendly; Norway Backtest demonstrates differentiation; section-break rhythm paces cumulative load; What the Chapter Leaves for Later scopes appropriately. The cumulative name-defense load at lines 280 + 302 was the chapter's strongest pull toward compression for this character (Tier-B-optional held in Phase C-ε).

**What lands post-restoration.** This character is the audience whose verdict gains the most across the dev-edit restoration sites — the restoration polarity (paragraph-rhythm restoration + §-break insertion + concrete-texture insertion) directly addresses the prior verdict's cumulative-load concerns.

- **Opening re-paragraphation (4 → 6 paragraphs at lines 10–20)** (F-DE-Ch6-3 Option D). Cost-severance claim → entitled-question / methodological pattern / chapter-structure / uncertainty-honest framing / three-approaches list. Each paragraph now lands on its own beat. Reads as Mazzucato/Sandel/Pistor cadence rather than dense thesis-paragraph stack. **Materially strengthens** — this is the trade-press editor's strongest gain from the dev-edit.
- **How-to-read directive cut from end of opening** (F-DE-Ch6-3 Option D part). The previous final two sentences of the opening ("*The reader who cares about the arithmetic can follow the arithmetic. The reader who cares about the argument can skip the formulas and follow the result.*") were cut from the opening; the directive's spirit lands instead naturally at line 94 ("*a plain-English version of what the formula computes, because the argument has to survive without the mathematics for readers who would rather not do integrals*"). Trade-press editor reads the orientation at the moment of need rather than as up-front meta-instruction. **Lightly strengthens** — the opening reads as opening rather than as opening-plus-reader-orientation.
- **Community paragraph re-paragraphation + §-break before carbon-addition at lines 32–41** (F-DE-Ch6-5 Option C). Substrate-enumeration ending at "...thirteen years, in McDowell County, against the national average."; Darity methodology lineage standalone paragraph at line 34; standalone $5–$15 cost-estimate closer at line 36; bottom-up synthesis closing at "Not a rounding error. A factor."; `---` break; "Then add the carbon. This is where the arithmetic stops being conservative and starts being contested." carbon-addition pivot at line 42. Trade-press editor reads carbon-cost as a separately-treated discussion. **Lightly strengthens.**
- **Convergence finding §-break at line 197** (F-DE-Ch6-1). Reads as paginated emphasis-moment matching the structural-claim register. **Lightly strengthens.**
- **Norway Backtest concrete-texture paragraph at line 221** (F-DE-Ch6-2 Option A). Trade-press editor reads concrete-institutional-detail (1990 / 1996 / spending rule / 1991 carbon tax / ethics council) as substantive Mazzucato/Sandel/Pistor-style grounding rather than as additional apparatus. **Lightly strengthens.**
- **Norway Backtest closer split at lines 227–229** (F-DE-Ch6-7). The differentiates-correctly claim ("*The model does what a good model should. It differentiates. It does not say 'extraction is always bad at the same rate.' It says 'extraction under these conditions produces this much cost severance, and extraction under those conditions produces that much.'*") now closes its own paragraph; the Norway acknowledgment ("*Norway is closer to honest pricing than anywhere else. It is still not all the way there.*") stands as its own paragraph. The differentiation demonstration + the acknowledgment land as two discrete moves rather than as compressed pair. **Lightly strengthens.**
- **What Is Owed §-break + Sen-pairing standalone paragraph at lines 271 + 273** (F-DE-Ch6-8). Parfit-Restitution-Bond cross-reference cluster + Sen-grounding-of-valuation now paginated separately. **Lightly strengthens.**
- **Four-gates worked-example sentences at lines 307 / 309 / 311** (F-DE-Ch6-4). Trade-press editor reads the worked-examples (DALY/WTP; infinite-intergenerational; Cohesion/Habitability double-count) as load-bearing illustration that breaks gate density into accessible-yet-rigorous units. **Lightly strengthens.**
- **Contribution section §-breaks at lines 333 + 337** (F-DE-Ch6-6). Three additions distinctly paginated. Trade-press editor reads "three additions, each consequential" with paragraph-rhythm matching the structural claim. **Materially strengthens** — the Contribution section was previously the trade-press editor's principal density concern in the chapter's third quarter.

**What flags post-restoration.** The four name-defense paragraphs (now at lines 121, 303, 325, 361) at ~1,125w cumulative load remain in place; this was the Phase C-ε Tier-B-optional held disposition. Dev-edit restoration polarity is *restoration* (paragraph-rhythm + concrete-texture + §-break + paragraph-relocation), not *cutting*; no further compression of name-defenses occurred. Trade-press editor's cumulative-name-defense-load read remains at the upper edge of trade-comp tolerance per the Phase C-ε disposition. Per the held Tier-B-optional disposition, this read does not warrant a new flag.

The chapter's section-break rhythm now reads more dispersed (15+ `---` rules across 365 lines, versus 13 section-headed sections + handful of section-internal `---` rules pre-dev-edit). Trade-press editor reads the §-break dispersion as appropriate paragraph-rhythm relief rather than as overuse — each restoration §-break does a specific paragraph-rhythm job at a structural pivot (carbon-pivot; convergence-finding; Norway differentiation-vs-acknowledgment; Parfit-vs-Sen; substitutability-vs-integrated-architecture; integrated-architecture-vs-CIT).

**Post-restoration verdict: ✓✓ INCLUDE — LIGHTLY STRENGTHENED (multiple sites materially).** The cumulative breath-restoration across opening + Approach 1 + convergence + Norway + What Is Owed + four-gates + Contribution is substantial; trade-press editor reads cumulative-load as net-better-managed post-dev-edit than pre-dev-edit. The verdict approaches but does not cross the ✓✓ → ✓✓✓ threshold because the four name-defense paragraphs at ~1,125w cumulative load remain in place per held Phase C-ε Tier-B-optional disposition; the third-order trade-press-editor compression-pull that prevented the ✓✓ → ✓✓✓ upgrade in the original Pass 3.3 is unchanged.

---

### Tier 3 — pipeline-strengthening audiences

#### 5. General-readership Mazzucato/Raworth-cluster reader (layman of economics) — Tier 3 reader

**Prior Pass 3.3 verdict (2026-05-14):** ✓✓ INCLUDE — three-approach plain-English orientation; formula + term-by-term-translation scaffolds the apparatus; counter-argument structure layman-readable + rhetorically-vivid; Ten Commons Categories section honors Ostrom-path illustrative register; knowledge-worker autonomy-commons paragraph universal-across-political-traditions. Cumulative apparatus-load through the chapter's second half was the principal load-bearing concern; scaffolding made it manageable.

**What lands post-restoration.** The dev-edit restoration polarity directly addresses the layman reader's prior principal concern (cumulative apparatus-load through the chapter's second half). The four-gates worked-example sentences + the Contribution section §-breaks + the Norway concrete-texture paragraph collectively relieve the cumulative-density flag while preserving the apparatus's substance.

- **Opening re-paragraphation at lines 10–20** (F-DE-Ch6-3 Option D). The layman reader reads the opening as six discrete paragraphs each landing on its own beat rather than as four dense thesis-paragraphs. The how-to-read directive's natural relocation to line 94 means the layman reader encounters the orientation at the moment of need (just before the formula appears) rather than as up-front meta-instruction the layman reader has not yet had reason to apply. **Lightly strengthens.**
- **Community paragraph re-paragraphation at lines 32–36** (F-DE-Ch6-5 Option C). The layman reader reads the substrate enumeration (health $2–4; environment $1–3; community $5–15) → Darity methodology lineage → standalone $5–$15 cost-estimate closer as three distinct beats. **Lightly strengthens.**
- **§-break before carbon-addition at line 41** (F-DE-Ch6-5 Option C). The layman reader recognizes the carbon-addition as a distinct analytical move ("*This is where the arithmetic stops being conservative and starts being contested.*") rather than as continuation of the bottom-up walkthrough. **Lightly strengthens.**
- **Norway concrete-texture paragraph at line 221** (F-DE-Ch6-2 Option A). The layman reader who was previously asked to take the Norway-as-best-managed-case claim at compressed thesis-paragraph level now reads concrete texture (1990 / 1996 / spending rule / 1991 carbon tax / ethics council). The Hartwick's-Rule-as-implemented-by-Norway framing lands with institutional grounding rather than as assertion. **Lightly strengthens.**
- **Norway Backtest closer split at lines 227–229** (F-DE-Ch6-7). The layman reader reads the differentiation demonstration + the acknowledgment as two discrete moves; the "*Norway is closer to honest pricing than anywhere else. It is still not all the way there.*" acknowledgment now sits as its own paragraph rather than as continuation. **Lightly strengthens.**
- **Convergence finding §-break at line 197** (F-DE-Ch6-1). The layman reader reads the central finding as a paginated emphasis-moment matching the structural claim. **Lightly strengthens.**
- **What Is Owed §-break + Sen-pairing standalone paragraph at lines 271 + 273** (F-DE-Ch6-8). The layman reader reads Parfit-grounding-of-standing and Sen-grounding-of-valuation as two distinct philosophical moves with paragraph-rhythm matching the cross-tradition pairing. **Lightly strengthens.**
- **Four-gates worked-example sentences at lines 307 / 309 / 311** (F-DE-Ch6-4). For the layman reader these are particularly load-bearing: the DALY/WTP example, the infinite-intergenerational-damage example, the Cohesion/Habitability double-count example make each gate concrete. The previous Pass 3.3 layman-reader principal concern (cumulative apparatus-load through the second half of the chapter) is materially addressed by the worked-example sentences. **Materially strengthens.**
- **Contribution section §-breaks at lines 333 + 337** (F-DE-Ch6-6). Three additions now distinctly paginated. The layman reader reads "three additions, each consequential" → substitutability-weighting paragraph → §-break → integrated architecture paragraph → §-break → Commons Inversion Test paragraph with paragraph-rhythm matching the three-addition structural claim. **Materially strengthens** — the Contribution section was a load-bearing site of the layman reader's prior cumulative-density concern.

**What flags post-restoration.** None new. The Greek-letter notation at line 130 (α-dominance) flagged at the prior verdict's edge-of-tolerance level remains in place per Phase C-ε Item (viii) held-with-publisher-signal-flag disposition; not Pass 3.3 light re-fire scope. Cumulative apparatus-load through the chapter's second half remains substantively the chapter's job but is now better-scaffolded with concrete anchors + paragraph-breath relief.

**Post-restoration verdict: ✓✓ INCLUDE — LIGHTLY STRENGTHENED (multiple sites materially).** The four-gates worked-example sentences + Contribution section §-breaks are the materially-strengthening sites; opening re-paragraphation + Approach 1 community re-paragraphation + Norway concrete-texture + convergence §-break + What-Is-Owed §-break light-strengthen. Cumulative apparatus-load concern is materially better-managed post-dev-edit; the verdict approaches but does not cross the ✓✓ → ✓✓✓ threshold because the cumulative density itself (~28% apparatus-bearing prose) is substantively the chapter's job and the restoration polarity relieves rhythm rather than reducing substance.

---

#### 6. Ostrom-tradition resonance reader — Tier 3 reader

**Prior Pass 3.3 verdict (2026-05-14):** ✓✓✓ INCLUDE — Two Kinds of Commons section is the chapter's strongest single section for this character; framework joins Ostrom tradition at adjacent-domain-specification level rather than appropriating vocabulary; Commons-Absence + Commons-Consumption Inversion two-sub-form distinguishes the framework's scope from Ostrom's appropriately; MI-3 heterogeneous-stakeholder break-point names where Ostrom's framework doesn't reach accurately; ten commons categories presented in open/illustrative Ostrom-path register with explicit reference to Ostrom's eight design principles; RCV name-defense names Ostrom directly as the *Commons* sub-choice grounding; Phase C-δ swap at line 128 resolved the Ostrom-path-memory soft tripwire.

**What lands post-restoration.**

- **Two Kinds of Commons section (lines 275–285)** — content untouched by dev-edit. The coordination-vs-extraction structural distinction + the MI-3 stratification economics tie at the heterogeneous-stakeholder break-point land verbatim. PRESERVES.
- **Ten Commons Categories section (lines 233–253)** — content untouched. The Ostrom-path illustrative register (lines 237 + 239 + 245 + 247) with explicit Ostrom-Sen-Nussbaum-Rawls comparison lands verbatim. PRESERVES.
- **RCV name-defense at line 325** — content untouched. The triple-lineage (Hartwick + Ostrom + Mazzucato) defense of *Residual Commons Value* sub-choices lands verbatim, with Ostrom named as the *Commons* sub-choice grounding. PRESERVES.
- **MI-3 stratification economics tie at line 285** — content unchanged. PRESERVES.
- **Line 141 "Norway is the primary anchor for the method"** (post-Phase-C-δ swap from *"canonical anchor"*) — preserved verbatim. The Ostrom-path-memory tripwire resolution holds. PRESERVES.
- **No restoration site touches the Ostrom-tradition reader's load-bearing surfaces.** The dev-edit restoration polarity (paragraph-rhythm + §-break + concrete-texture + paragraph-relocation) operates at sites outside this character's principal reading surfaces.

**What flags post-restoration.** None.

**Post-restoration verdict: ✓✓✓ INCLUDE — PRESERVED.** The chapter's strongest sections for this character (Two Kinds of Commons + Ten Commons Categories + RCV name-defense + MI-3 tie + Norway-anchor phrasing) are all content-unchanged by the dev-edit; the surrounding-prose breath-restoration around them is structural rather than substantive. The Ostrom-tradition reader's verdict holds at full strength.

---

#### 7. Reparations-economics specialist + Black-Studies-resonance reader (combined) — Tier 3 reader

**Prior Pass 3.3 verdict (2026-05-14):** ✓✓✓ INCLUDE — Darity longevity-gap lineage paragraph at line 25 substantively-engaged + portability claim grounded in methodology-travels-calibration-adjusts framing; Method 2 backward-application list at line 132 is five-element-cross-three-tradition substantive engagement; MI-3 stratification economics tie at line 262 explicitly locates the framework within Darity-Hamilton-and-collaborators tradition; What Is Owed section uses Parfit+Sen as philosophical grounding + cross-references Ch 5's Restitution Bond methodology; universality claim at line 230 accommodates lived-oppression reading alongside civic-republican + classical-liberal readings. The line 21 Black Lung Trust Fund attribution was the only flag and was separate cross-chapter follow-up scope (since resolved by commit `5569600` before Phase C-ε close).

**What lands post-restoration.**

- **Darity longevity-gap lineage paragraph now standalone at line 34** (F-DE-Ch6-5 Option C re-paragraphation). This is the materially-strengthening site for this character: the methodology-travels-per-context-calibration-differs framing previously sat embedded inside the community-paragraph substrate-enumeration; now it stands as its own paragraph between the cost-enumeration close ("...thirteen years, in McDowell County, against the national average.") and the standalone $5–$15 cost-estimate closer. The reparations-economics reader reads Darity's named-attribution + the "the methodology travels; the per-context calibration is what differs" lineage-attributive register with paragraph-rhythm matching the substantive engagement. **Materially strengthens** — this is the chapter's most-load-bearing single sentence for this character's authentic-engagement-vs-decorative-name-checking test, and it now stands at paragraph-level emphasis rather than at substrate-clause level.
- **Method 2 backward-application list at line 145** — content unchanged. Five-element list (Holocaust reparations + 1988 Civil Liberties Act + Black Lung Trust Fund payouts + South African TRC + Darity-Mullen 2020) preserved verbatim. PRESERVES.
- **MI-3 stratification economics tie at line 285** — content unchanged. Sandy's stratification-economics tradition named directly + framed as the analytical apparatus the framework's commons-governance extension applies to heterogeneous-stakeholder commons. PRESERVES.
- **What Is Owed §-break + Sen-pairing standalone paragraph at lines 271 + 273** (F-DE-Ch6-8). The Parfit-grounding cluster closes at line 269 with the explicit Ch 5 cross-reference: *"The methodology applied to the Restitution Bond builds on Darity and Mullen's reparations-economics wealth-gap framework, engaged at depth in Chapter 5's introduction of the two-instrument apparatus; Chapter 6's role here is methodological. The framework's damages-already-realized instrument is a specialization of that methodology to extraction-community contexts — portable mechanism, per-context calibration."* Then `---` break; Sen-pairing standalone at line 273. The reparations-economics reader reads the Parfit-Restitution-Bond-Ch-5-cross-reference cluster and the Sen-grounding-of-valuation as two discrete philosophical-grounding moves rather than as compressed pair. The "portable mechanism, per-context calibration" closer at line 269 echoes the line 34 "methodology travels; per-context calibration is what differs" framing — same lineage-attributive register at two locations in the chapter, now both at paragraph-rhythm-emphasis level. **Lightly strengthens.**
- **Universality claim at line 251** ("*Whether you read that as a Commons-Consumption Inversion against an autonomy commons (the civic-republican reading), as a market mechanism functioning as designed (the classical-liberal reading), or as evidence of structural domination (the lived-oppression reading), the framework's measurement applies.*") — content unchanged. The lived-oppression reading is named directly + framed as one of the three political-tradition readings the framework's measurement applies across. PRESERVES.
- **Line 28 Black Lung Trust Fund → federal Program reframe** (commit `5569600` pre-Phase-C-ε): preserved at *"the federal Black Lung Benefits Program's approximately $44 billion in distributions through 2009 (GAO/CRS), allocated across the national tonnage of coal produced since the Program's 1969 establishment..."* The reparations-economics reader's only flag from prior verdict is resolved.

**What flags post-restoration.** None.

**Post-restoration verdict: ✓✓✓ INCLUDE — LIGHTLY STRENGTHENED.** The Darity-lineage paragraph's standalone treatment + the Parfit-Restitution-Bond-Ch-5-cross-reference closer's "portable mechanism, per-context calibration" framing at line 269 (echoing the line 34 "methodology travels" framing) + the Sen-pairing's standalone treatment together give this character's three principal load-bearing surfaces dedicated paragraph-rhythm. The methodology-travels-per-context-calibration-differs framing now sits twice in the chapter at paragraph-rhythm-emphasis level (lines 34 + 269), and the cross-tradition synthesis discipline reads as substantively-paginated.

---

## §4. Aggregate light-re-fire verdict

### §4.1 Per-character tally — before-and-after

| Tier | # | Audience | Prior verdict (2026-05-14) | Post-restoration verdict (2026-05-23) | Delta |
|---|---|---|---|---|---|
| 1 | 1 | Sandy Darity | ✓✓✓ INCLUDE | ✓✓✓ INCLUDE | LIGHTLY STRENGTHENED |
| 1 | 2 | Berggruen Prize judge | ✓✓✓ INCLUDE | ✓✓✓ INCLUDE | LIGHTLY STRENGTHENED |
| 2 | 3 | Academic econ reviewer (AER/QJE/JPE comparable) | ✓✓ INCLUDE | ✓✓ INCLUDE | LIGHTLY STRENGTHENED |
| 2 | 4 | Sandel-tradition trade-press editor | ✓✓ INCLUDE | ✓✓ INCLUDE | LIGHTLY STRENGTHENED |
| 3 | 5 | General-readership Mazzucato/Raworth-cluster reader (layman of economics) | ✓✓ INCLUDE | ✓✓ INCLUDE | LIGHTLY STRENGTHENED |
| 3 | 6 | Ostrom-tradition resonance reader | ✓✓✓ INCLUDE | ✓✓✓ INCLUDE | PRESERVED |
| 3 | 7 | Reparations-economics specialist + Black-Studies-resonance reader | ✓✓✓ INCLUDE | ✓✓✓ INCLUDE | LIGHTLY STRENGTHENED |

**Tally:** 7 INCLUDE; 0 NEUTRAL; 0 EXCLUDE. Distribution: 4 ✓✓✓ + 3 ✓✓ + 0 ✓ — **identical aggregate distribution** to prior Pass 3.3 verdict (2026-05-14).

**Delta distribution:** 6 LIGHTLY STRENGTHENED + 1 PRESERVED + 0 PERTURBED. No character returns NEUTRAL or EXCLUDE post-restoration. No character drops a tier (no ✓✓✓ → ✓✓ regression; no ✓✓ → ✓ regression). No character crosses the ✓✓ → ✓✓✓ threshold (the two ✓✓ characters whose verdicts gained most materially — Sandel-tradition trade-press editor + layman reader — approach the threshold but the third-order concerns that prevented the ✓✓ → ✓✓✓ upgrade in the original Pass 3.3 are unchanged by the dev-edit restoration polarity).

**Tier 1 (gating): 2 ✓✓✓ — both LIGHTLY STRENGTHENED.** Methodology-chapter standing threshold met + reinforced.
**Tier 2: 2 ✓✓ — both LIGHTLY STRENGTHENED.**
**Tier 3: 1 ✓✓ + 2 ✓✓✓ — 1 LIGHTLY STRENGTHENED + 1 PRESERVED + 1 LIGHTLY STRENGTHENED.**

### §4.2 Aggregate light-re-fire verdict

**READY TO SUBMIT AS-IS (verdict preserved + lightly strengthened across the audience pressure-test character set).**

The Ch 6 dev-edit Phase C application (commit `713fbe1`, 2026-05-21) preserves the prior Pass 3.3 verdict (7 INCLUDE / 0 EXCLUDE; READY TO SUBMIT AS-IS) across all seven characters and lightly strengthens six of seven. The restoration polarity — paragraph-rhythm restoration + §-break insertion + concrete-texture paragraph + worked-example sentences + paragraph-relocation — operates at sites that either lightly-strengthen the relevant audience character's load-bearing surfaces or pass through without touching them. No site perturbs any prior verdict.

The two materially-strengthening restoration sites — F-DE-Ch6-2's Norway concrete-texture paragraph + F-DE-Ch6-4's four-gates worked-example sentences + F-DE-Ch6-6's Contribution section §-breaks — relieve the cumulative-apparatus-load concern that surfaced as the principal third-order pull in the prior Pass 3.3 verdict for the Sandel-tradition trade-press editor + the layman reader. Cumulative density at the substance level is unchanged; cumulative breath is restored across opening + Approach 1 + convergence + Norway + What Is Owed + four-gates + Contribution.

### §4.3 Spot-fix recommendations

**None.** No character returns EXCLUDE post-restoration. No PERTURBED verdict surfaces. Per the Stage-3 template's Pass-3 hard constraint — per-character spot-fixes are proposed only for EXCLUDE verdicts — this light re-fire produces no spot-fix recommendations.

The pre-publication verification flag on the "three percent" Norway spending-rule figure at line 221 (per dev-edit §11.6) is **carried forward as held**, not converted to a Pass-3.3-light-re-fire spot-fix recommendation. Per task brief out-of-scope, this Pass 3.3 light re-fire reads the figure as currently stands; the TA-Norway-coverage + Handlingsregelen-rule verification cascade fires separately at pre-publication.

The Phase C-ε Tier-B-optional held items (Item (i) name-defense compression at lines 280 + 302 [now lines 303 + 325 post-app]; Item (vii) convergence-table caption inline-vs-footnote; Item (viii) α-dominance plain-English unpacking at line 130 [now line 143 post-app]) are **all held unchanged**. Per task brief, no re-litigation of Phase C-ε disposition. The dev-edit restoration polarity does not touch any of these held items; the held dispositions remain.

### §4.4 Cross-pass cascade flag

**Pass 3.4 robustness re-fire: NOT WARRANTED.** Per dev-edit workstream handoff §3.1 step 10 + dev-edit §11.4 cross-pass impact confirmation: restorations strengthen rather than weaken adversarial robustness; thread-pull surface unchanged. The Norway concrete-texture paragraph at line 221 strengthens the chapter's response to parameter-rigging (adversarial Chicago #5) + business-blame (WSJ #7) + universal-CS>0 (adversarial #4/#5/#7/#10) threads — the differentiates-correctly demonstration now carries concrete-texture grounding the prior rendering lacked. The convergence-finding §-break does not change the finding's substance; thread-pull surface unchanged. No new adversarial thread surfaced by the restorations.

**Other cross-pass cascades:** none warranted. Pass 3.1 fact-check + Pass 3.2 voice-polish dispositions are preserved per dev-edit §11.4 (no new facts contradict canonical-facts inventory; no per-paragraph tic-fix re-litigated; F-V5 verbatim phrase repeat at lines 58 + 263 [now ~63 + ~287] continues to flag as Pass-2-held; F-V11 M2-paragraph triple "actual" verified clean post-F-DE-Ch6-2 Option B M2 limit-naming swap). Stage 4 render-integrity (closed via pipeline retrofit `5e08642`) unaffected — applied edits use existing paragraph-break + §-break + inline-text patterns consistent with the chapter's already-rendered state.

Named-subject consent discipline preserved (no new named subjects; no anonymized subjects in Ch 6; named figures remain public-record academics + authors).

---

## §5. What this pass did NOT do

Per task brief hard constraints:

- **Did NOT apply spot-fixes to the chapter file.** No EXCLUDE characters; no PERTURBED verdicts; no required spot-fixes surfaced. Chapter file unchanged.
- **Did NOT re-run Pass 3.1 (fact-check) or Pass 3.2 (voice-polish) or Pass 3.4 (robustness).** All held per dev-edit §11.4 cross-pass impact confirmation.
- **Did NOT re-litigate Phase C-ε Tier-B-optional disposition** (CIT name-defense compression at line 280 [now 303]; RCV name-defense compression at line 302 [now 325]; convergence-table caption inline-vs-footnote; α-dominance plain-English unpacking at line 130 [now 143]).
- **Did NOT re-construct the Ch 6 audience pressure-test character set.** Used the canonical 7-character set as built in the prior Pass 3.3 §3.
- **Did NOT verify the "three percent" Norway spending-rule figure** at line 221 against TA Norway coverage + current Handlingsregelen rule formulation. That verification cascade is held for pre-publication per dev-edit §11.6; this Pass 3.3 light re-fire reads the figure as currently stands per task brief.
- **Did NOT incorporate Sandy's not-yet-arrived reply** for lines 124 [now ~137] + 262 [now ~285] (Q0 tier-S citation outreach sent 2026-05-15). Lines read as they currently stand.
- **Did NOT regress the SI-1 framing** in the M1/M2/M3 walkthrough opener. Per task brief hard constraint: verified intact at line 137 (the three load-bearing sentences survive verbatim).
- **Did NOT contact named subjects.** Per consent discipline.
- **Did NOT propose new framework concepts.** Per task brief hard constraint.
- **Did NOT touch the Technical Appendix, Ch 5, or other chapters.** Per task brief explicit scope.
- **Did NOT cascade beyond Ch 6.** Per task brief.

---

## §6. Hard constraints honored

- ✓ Did NOT apply spot-fixes to `Chapter__6_ThreeWaysofCounting.md` (chapter file unchanged).
- ✓ Used the canonical 7-character Pass 3.3 set as-built (no re-construction).
- ✓ Per-character delta format honored: prior verdict + post-restoration delta + post-restoration verdict + delta type (PRESERVED / LIGHTLY STRENGTHENED / PERTURBED).
- ✓ SI-1 framing preserved verbatim at line 137 (verified against the three load-bearing sentences from the prior Pass 3.3 §4 character #1 "What lands" bullet).
- ✓ M1/M2/M3 canonical method names preserved.
- ✓ Did NOT re-run Pass 3.1 / 3.2 / 3.4.
- ✓ Did NOT re-litigate Phase C-ε Tier-B-optional disposition.
- ✓ Did NOT incorporate Sandy's not-yet-arrived reply.
- ✓ Did NOT verify the "three percent" Norway figure (held for pre-publication per dev-edit §11.6).
- ✓ Did NOT contact named subjects.
- ✓ Did NOT propose new framework concepts.
- ✓ Did NOT touch the Technical Appendix, Ch 5, or other chapters.
- ✓ Built feature branch `claude/ch6-pass-3-3-light-refire-1fae85` off `origin/main` per task brief branch discipline + CLAUDE.md rigor-pass artifact branch discipline.
- ✓ Per CLAUDE.md merge-to-main default for rigor-pass artifacts: this artifact autonomously fast-forward merges to `main` at session close (internal scaffolding; chapter file unchanged; proposes no spot-fixes).

---

## §7. Session-close disposition

**Verdict (light re-fire):** READY TO SUBMIT AS-IS (verdict preserved + lightly strengthened across the audience pressure-test character set).

**Per-character delta tally:** 6 LIGHTLY STRENGTHENED + 1 PRESERVED + 0 PERTURBED across 7 characters.

**Pass 3.4 cascade flag:** NOT WARRANTED. Restorations strengthen adversarial robustness; thread-pull surface unchanged.

**Held items carried forward** (none added by this re-fire; held from prior dispositions):
1. Pre-publication verification flag on the "three percent" Norway spending-rule figure at line 221 against TA Norway coverage + current Handlingsregelen rule formulation (per dev-edit §11.6).
2. Phase C-ε Tier-B-optional held items (Item (i) name-defense compression at lines 303 + 325; Item (vii) convergence-table caption inline-vs-footnote; Item (viii) α-dominance plain-English unpacking at line 143).
3. Pass 2 F-V5 verbatim phrase repeat at lines ~63 + ~287 (held as Pass-2 disposition; not Pass 3.3 scope; regressed-pattern scanner correctly flags as pre-existing pattern).

**Chapter rigor-pass cycle status:** Ch 6 Pass 3.3 light re-fire post-dev-edit closes clean. Per pipeline doctrine v3.1 Amendment B, Pass 3.5 (developmental-edit) → Phase C application → light Pass 3.3 re-fire is the canonical post-developmental-edit cascade; this artifact closes that cascade for Ch 6. The chapter's three-pass-plus-dev-edit rigor cycle (Pass 1 + Amendments + Phase C-α + Phase C-β + Pass 2 + Phase C-γ + Phase-C-γ-follow-up + Phase C-δ + cascade-followup + Pass 3 + Phase C-ε + Pass 3.4 + Pass 3.5 + Phase C dev-edit application + Pass 3.3 light re-fire) is fully closed at the post-dev-edit chapter state.

---

*End of Ch 6 Stage-3 Pass 3.3 light re-fire post-Pass-3.5-developmental-edit-application — PROPOSED 2026-05-23 / RATIFIED 2026-05-25. Per CLAUDE.md merge-to-main default for rigor-pass artifacts, this artifact autonomously fast-forward merges to `main` at session close (rigor-pass artifact; internal scaffolding; chapter file unchanged; proposes no spot-fixes; verdict preserved + lightly strengthened across the audience pressure-test character set).*

---

## §8. Stage 4 ratification — author-managed-offline disposition (2026-05-25)

**Stage 4 render + character-integrity audit: RATIFIED as author-managed-offline.** Per author 2026-05-25 instruction matching the 2026-05-24 Ch 2 precedent (commit `9bddbd2` "Stage 4 render-audit ratified as author-managed-offline per author 2026-05-24 instruction"): Ch 6's post-dev-edit Stage 4 render audit is owned by the author offline (render pipeline session; no agent involvement). The author has rendered the chapter at the post-dev-edit + post-coal-CO₂-methodology-cascade state and ratifies Stage 4 by confirmation.

**Pre-dev-edit Stage 4 baseline** remains the prior triple-render comparison data at [`tools/rigor-passes/render_pipeline_comparison_ch6_2026-05-18.md`](render_pipeline_comparison_ch6_2026-05-18.md) (verdict CLEAN modulo canonical-pipeline ratification; SI-1 preservation verified at render level; all key Ch 6 render-fidelity tests passing) + the canonical-pipeline-decision retrofit (commit `5e08642`) that closed Stage 4 at the corpus level.

**Post-dev-edit delta from the Stage 4 baseline:**
- +22 lines structural restoration (paragraph-rhythm + §-break + concrete-texture + worked-example sentences + paragraph-relocation per dev-edit §11.2);
- 1 concrete-texture paragraph added at Norway Backtest (5 sentences);
- 3 four-gates worked-example sentences (gates 2/3/4);
- 6 new `---` §-breaks (carbon-pivot; convergence-finding; Norway differentiation/acknowledgment; Parfit/Sen; substitutability/integrated-architecture; integrated-architecture/CIT);
- 1 paragraph relocation (externality-tail name-defense).

All restoration polarities use existing paragraph-break + §-break + inline-text patterns consistent with the chapter's already-rendered state per dev-edit §11.4. No new Plane-1 characters, no new math display blocks, no new tables, no new figure references. Stage 4 author-offline ratification confirms no rendering anomalies were surfaced in the post-dev-edit render.

**Stage 4 verdict for the pre-publication review queue artifact §1.5:** CLEAN (author-managed-offline ratification 2026-05-25). MEDIUM HOLD items from the pre-dev-edit Stage 4 baseline (the documented-not-canonical laptop wkhtmltopdf Qt 4.8.7 disposition per F-RP-TA-02 pattern; canonical Docker pipeline at Qt 5.15.13 renders cleanly) carry forward unchanged.
