# Stage-3 Rigor Pass — Chapter 8 (What Things Actually Cost) — Pass 3.3 (Audience-Load — Acceptance) [PROPOSED]

**Date:** 2026-05-25
**Workstream:** #20 Manuscript Stage-3 Rigor Pass — Phase A — Ch 8 — Pass 3.3 (audience-load acceptance)
**Chapter:** 8 — *What Things Actually Cost*
**File audited:** [`manuscript/chapters/Chapter__8_WhatThingsActuallyCost.md`](../../manuscript/chapters/Chapter__8_WhatThingsActuallyCost.md) — **243 lines** (post-Phase-C-β state at origin/main `16554fa`; verified 2026-05-25 via `wc -l`; em-dash count = 28 per `grep -c "—"`; word count = 6,421 per `wc -w`).
**Status:** PROPOSED — pending author ratification. Phase C-γ session applies any ratified spot-fixes after author disposition.
**Mode:** Audit-existing-prose (no Stage-1 brief; chapter file IS canonical reference).
**Pass discipline:** v3.0/v3.1 sub-pass split — Pass 3.3 (acceptance — INCLUDE / EXCLUDE per character). Pass 3.4 (robustness — adversarial / detractor with thread-pull synthesis) is the next session per per-prompt serial cadence. Pass 3.5 (developmental-edit) is explicit-gate per Amendment A two-class cascade.

**Prior-pass closure context.**
- Pass 3.1 (fact-check) — CLOSED 2026-05-16. Ratification + Phase C application via commit `5fe6af6` (16 Ch 8 spot-fixes + cross-chapter consequences) + commit `275b75a` (MED-6 Phase C-β follow-through — 2 residual hedge-alignment fixes); cross-corpus IPG canonical-construction Option D applied via commit `57575b1`; coal-CO₂ McDowell-specific cascade-reconciliation Phase C via commit `9befb92` (4 spot-fixes at lines 40, 52, 166, 238).
- Pass 3.2 (voice-polish) — CLOSED + RATIFIED 2026-05-25. Ratification at commit `138aa7e` (PROPOSED 2026-05-23 → RATIFIED 2026-05-25; all 20 dispositions = 8 RATIFY APPLY + 12 RATIFY HOLD); cascade-reconciliation `6589ca2` (9befb92 sync); Phase C-β application at commit `16554fa` (8 chapter spot-fixes at lines 12, 28, 60, 62, 96, 108, 124, 138, 166, 176, 222 + chapter-wide em-dash comprehensive sweep 80 → 28; net line-count delta 243 → 243 = neutral; word-count delta 6,375 → 6,421 = +46 net from F-V3 em-dash → comma/period restructure offsetting F-V1 + F-V2 + F-V4 compressions).
- Pass 3.3 (this session) audits the post-Phase-C-β chapter state.

**Branch:** `claude/ch8-pass3-3-audience-load-acceptance-aa04af5d` off origin/main `0615b9c`.

---

## §0. Source artifacts read

1. [`manuscript/chapters/Chapter__8_WhatThingsActuallyCost.md`](../../manuscript/chapters/Chapter__8_WhatThingsActuallyCost.md) — chapter under audit, 243 lines post-Phase-C-β.
2. [`tools/rigor-passes/commons_bonds_rigor_pass_2026-05-16_ch8_what_things_actually_cost_stage3_fact_check_v1.0.0.md`](commons_bonds_rigor_pass_2026-05-16_ch8_what_things_actually_cost_stage3_fact_check_v1.0.0.md) — Pass 3.1 artifact + §10 audience-character set + §12 update note (rent-seeking paragraph fact-check coverage). All HIGH + MEDIUM dispositions APPLIED.
3. [`tools/rigor-passes/commons_bonds_rigor_pass_2026-05-23_ch8_what_things_actually_cost_stage3_voice_polish_v1.0.0.md`](commons_bonds_rigor_pass_2026-05-23_ch8_what_things_actually_cost_stage3_voice_polish_v1.0.0.md) — Pass 3.2 artifact + §7 Pass-3-forward-flagged audience-load future-session input + §10.1 ratification table (8 RATIFY APPLY + 12 RATIFY HOLD).
4. [`tools/drafting-templates/stage-3-three-pass-rigor-audit.md`](../drafting-templates/stage-3-three-pass-rigor-audit.md) — Pass 3 audience-load template (under v3.0/v3.1 sub-pass split: the acceptance portion = Pass 3.3).
5. [`tools/drafting-templates/audience-pressure-test-construction.md`](../drafting-templates/audience-pressure-test-construction.md) — character set construction guide.
6. [`tools/rigor-passes/commons_bonds_rigor_pass_2026-05-25_ch7_on_other_worlds_stage3_pass_3_3_audience_load_acceptance_v1.0.0.md`](commons_bonds_rigor_pass_2026-05-25_ch7_on_other_worlds_stage3_pass_3_3_audience_load_acceptance_v1.0.0.md) — most-recent analytical-register cousin Pass 3.3 (Ch 7); 30-character format model; RATIFIED 2026-05-25 (Option A hold).
7. [`tools/rigor-passes/commons_bonds_rigor_pass_2026-05-23_ch9_pricing_honestly_stage3_pass_3_3_audience_load_acceptance_v1.0.0.md`](commons_bonds_rigor_pass_2026-05-23_ch9_pricing_honestly_stage3_pass_3_3_audience_load_acceptance_v1.0.0.md) — directly-adjacent chapter Pass 3.3 (Ch 9); 18-character format model; READY TO SUBMIT AS-IS.
8. [`tools/rigor-passes/ch4_existence_proof_stage3_pass_3_3_acceptance_2026-05-25.md`](ch4_existence_proof_stage3_pass_3_3_acceptance_2026-05-25.md) — analytical-quantitative cousin Pass 3.3 (Ch 4); 25-character format model.
9. [`tools/rigor-passes/commons_bonds_ch1_stage_3_pass_3_audience_load_REAUDIT_2026-05-17_PROPOSED.md`](commons_bonds_ch1_stage_3_pass_3_audience_load_REAUDIT_2026-05-17_PROPOSED.md) — canonical 30-acceptance + 10-adversarial format model.
10. [`tools/rigor-passes/commons_bonds_rigor_pass_2026-05-21_cross_corpus_ipg_canonical_construction_v1.0.0.md`](commons_bonds_rigor_pass_2026-05-21_cross_corpus_ipg_canonical_construction_v1.0.0.md) — Option D ratified + applied; affects IPG construction at Ch 8:168.
11. [`tools/rigor-passes/commons_bonds_rigor_pass_2026-05-11_apparatus_register_decision_v1.0.0.md`](commons_bonds_rigor_pass_2026-05-11_apparatus_register_decision_v1.0.0.md) — apparatus register canonical decisions (Item 1 inline-integral strip from Ch 8 ✓ intact; Item 13 IPG full-name + acronym; Item 14 Cᵢ via Four Gates).
12. [`tools/audits/cross-chapter-consistency-inventory_2026-05-11.md`](../audits/cross-chapter-consistency-inventory_2026-05-11.md) — canonical-terms / named-cases / recurring-stats inventory.
13. [`tools/workstream-handoffs/manuscript-stage-3-rigor-pass-handoff_2026-05-11.md`](../workstream-handoffs/manuscript-stage-3-rigor-pass-handoff_2026-05-11.md) — Ch 8 row (analytical-quantitative register + arithmetic-load risk + framework's load-bearing analytical chapter).
14. Memory: [`feedback_audience_aware_drafting_discipline.md`](../memory/feedback_audience_aware_drafting_discipline.md) v3.1 (explicit-gate cascade for Pass 3.3/3.4/3.5); [`feedback_dual_audience_test.md`](../memory/feedback_dual_audience_test.md) (layman + specialist test); [`feedback_verify_stale_memory_claims.md`](../memory/feedback_verify_stale_memory_claims.md); [`feedback_named_subject_consent.md`](../memory/feedback_named_subject_consent.md) (public-record exception for cited scholars).

**Verifications performed at session start:**
- ✓ Chapter file exists at cited path; line count = 243 (matches commit `16554fa`).
- ✓ Em-dash count = 28 per `grep -c "—"` (matches Pass 3.2 §10.1 F-V3 Option B comprehensive sweep target band; was 80 pre-sweep).
- ✓ Word count = 6,421 per `wc -w` (within expected post-Phase-C-β band; +46 net vs pre-sweep 6,375 — F-V3 em-dash → comma/period restructure offsets F-V1 + F-V2 + F-V4 + F-V13 compressions).
- ✓ Commits `5fe6af6`, `275b75a`, `57575b1`, `9befb92`, `138aa7e`, `6589ca2`, `16554fa` all present on origin/main.
- ✓ Pass 3.1 artifact present with ratification record.
- ✓ Pass 3.2 artifact present with §10.1 ratification table (RATIFIED 2026-05-25; 8 APPLY + 12 HOLD).
- ✓ Audience pressure-test template present at cited path.
- ✓ Ch 7 + Ch 9 + Ch 4 cousin Pass 3.3 artifacts present (canonical format models).
- ✓ Rent-seeking paragraph at line 122 intact post-Phase-C-β (reparations-economics + Public Choice + framework-contribution structure).
- ✓ Item 1 inline-integral strip from Ch 8 ✓ intact (no Greek letters / integrals / Greek subscripts in body prose; verified via spot-check; only CO₂ + Cᵢ + EPA AP-42 §1.1 + 2.6 metric ton arithmetic at line 72 fall within permitted analytical-quantitative register).
- ✓ Cross-corpus IPG construction at line 168 ✓ intact (post-Phase-C-β state; "thirty-three and one hundred and twenty-two times" + "at least three" carbon-vs-today's-market ratio per Option D).

---

## §1. Pass-3.3 scope reminder

**In scope.**
- Per-character INCLUDE / EXCLUDE acceptance verdict against the audience-character pressure-test set.
- Per-character rationale anchored in specific chapter line citations.
- Aggregate verdict: READY AS-IS / READY AFTER SPOT-FIXES / STRUCTURAL REVISION NEEDED.
- Cross-character pattern observations.
- Apparatus / consistency / named-subject discipline audit sub-checks (verify post-Phase-C-β state holds).
- Out-of-scope-for-Pass-3.3 flagged forward to Pass 3.4 (robustness) future-session input (§7).
- Out-of-scope-for-Pass-3.3 flagged forward to Pass 3.1 fact-check / Pass 3.2 voice-polish follow-up if any surface (§8).

**Not in scope.**
- No Pass 3.1 (fact-check) re-litigation. Pass 3.1 CLOSED + APPLIED.
- No Pass 3.2 (voice-polish) re-litigation. Pass 3.2 RATIFIED 2026-05-25 + Phase C-β APPLIED at commit `16554fa`.
- No Pass 3.4 (robustness — adversarial / detractor) scoring. Separate subsequent session per per-prompt serial cadence; concerns flagged forward at §7.
- No Pass 3.5 (developmental-edit) scoring. Explicit-gate per Amendment A.
- No spot-fix application to chapter file. Phase C-γ session does that after author ratifies.
- No re-litigation of apparatus register canonical decisions (Item 1 inline-integral strip; Item 13 IPG; Item 14 Cᵢ-via-Four-Gates).
- No re-litigation of cross-corpus IPG canonical-construction (commit `57575b1` Option D applied at line 168).
- No modification proposals that touch the rent-seeking paragraph at line 122 without explicit §7 flag (cross-chapter rent-seeking-engagement workstream ratification already absorbed via F-V12 Pass 3.2 ✓ HOLDS).
- No new framework concepts. No contact with named subjects.

---

## §2. Audience-character pressure-test set construction

Per `audience-pressure-test-construction.md` §8 quick-start defaults, a chapter (book-internal artifact, full rigor) calls for 25–30 acceptance characters across Tier 1 (5) + Tier 2 (8) + Tier 3 (12–17). Per the Ch 7 + Ch 9 + Ch 4 cousin format models — and per Ch 8's distinctive role as the framework's load-bearing analytical-quantitative chapter (the IPG-arithmetic chapter that hands forward to Ch 9 policy + Ch 10 closing) — a 28-character acceptance set is constructed: 5 Tier-1 + 8 Tier-2 + 15 Tier-3.

**Ch-8-specific tilts vs the Ch 7 / Ch 9 / Ch 4 cousin baselines:**
- **Sharpen** Tier-1 quant-economist / SCC-attentive reader (chapter's $190/ton SCC anchor at line 72 + EPA AP-42 §1.1 + Rennert et al. 2022 *Nature* citation + IPG arithmetic at line 168 + $524 sum at line 164 = chapter's load-bearing arithmetic backbone). Distinct from Ch 7's planetary-scientist quant reader: Ch 8's quant reader is climate-economics / SCC literature literate.
- **Sharpen** Tier-1 trade-press editor as analytical-quantitative-chapter calibrator (chapter performs full eight-component cost-walkthrough; framework-arithmetic is the chapter's central rhetorical instrument).
- **Sharpen** Tier-1 layman-but-engaged reader as arithmetic-load reader (chapter's eight-component walk + IPG-arithmetic + $10-15T civilizational-scale extrapolation at line 214 = density-stress on the layman reader).
- **Add** Tier-2 housing-economics reader (chapter's YIMBY-engagement at lines 180–190 explicitly engages Glaeser + Gyourko + Schuetz tradition; the chapter takes the steelman seriously and offers a both/and synthesis; this audience deserves its own character).
- **Add** Tier-2 climate-policy / SCC-tradition reader (chapter's $190/ton SCC + Rennert et al. 2022 anchor + EPA 2023 update at line 72 + Political Capture section at line 118 walking the Obama / Trump / Biden SCC political-fight history = direct climate-policy territory).
- **Add** Tier-2 First-Nations / Indigenous-treaty reader (chapter's Athabasca Chipewyan + Mikisew Cree + Fort McKay First Nations naming at line 178 + Treaty 8 of 1899 + "consultation-and-consent failures" framing = explicit Indigenous-rights territory).
- **Sharpen** Tier-2 Public Choice reader (chapter's line 122 rent-seeking paragraph explicit naming of Public Choice tradition (Buchanan, Tullock) + reparations-economics tradition (Coates, Darity, Mullen, Hamilton, Conley) + framework's-different-in-kind framing; coordinates with Ch 9 §"Public Choice section" Reading C v3 asymmetric framing post-`cbef9bd` cascade resolution).
- **Sharpen** Tier-2 reparations-economics reader (line 122 explicit lineage-naming; line 92 Black-American-writing-tradition four-author parallel-citation Dunbar + Du Bois + Fanon + Ellison + framework-contribution closer).
- **Sharpen** Tier-3 McDowell County / Appalachian-resonant reader (chapter is THE McDowell-arithmetic chapter; all eight cost components computed against McDowell case; the Appalachian-resonant reader is reading their own community's accounting).
- **Add** Tier-3 environmental-justice / frontline-community reader (chapter centers McDowell County + Baotou + Niger Delta / W.R. Grace Libby Montana + Exxon Valdez + tar sands First Nations as frontline-community cost-bearers).
- **Hold** all other Ch 1 / Ch 7 REAUDIT v3 acceptance characters where they apply — chapter is Phase A in the same book, audited under the same pipeline doctrine; cross-chapter character-coverage discipline carries forward.

The 28-character set is documented in §3 with chapter-specific test surfaces.

---

## §3. Per-character acceptance findings

Format mirrors Ch 7 §3 + Ch 9 §2 per-character layout: tier + brief profile + what lands + what flags + INCLUDE / EXCLUDE final verdict.

### Tier 1 — gating characters

#### 1. Trade-press editor pressure-test character

**Profile.** Editor at a trade-press imprint at the Mazzucato/Sandel/Pistor comp-shelf level. Reads for chapter-architecture, framework-clarity at trade-press register, comp-shelf placement signal, reader-trust foundation across the chapter, and whether the chapter's central arithmetic earns the read forward to Ch 9.

**What lands.**
- **Chapter-architecture is clean.** Twelve section-breaks structure the eight-component walk + the sum + the cross-case pattern + the misreading-defenses + the brief extrapolation + the closing (lines 22, 32, 44, 56, 68, 84, 100, 112, 128, 142, 172, 196, 210, 226). The architecture reads as substantively earned (each section answers a distinct cost-component question or a distinct framework-defense question).
- **Chapter-opening claim site (line 10) is the strongest single-line opener in the analytical chapters.** *"What if everything cost what it actually costs?"* — single-sentence question at chapter-opening; the framework's load-bearing analytical promise compressed to nine words; trade-press editor reads as competent rhetorical-pivot opener.
- **Post-Phase-C-β F-V1 compression at line 12 lands cleanly** (eight-component cost-preview now reads as one analytical sentence with colon-list rather than five-fold imperative anaphora). Editor reads as the chapter doing its eight-component-preview work without the LLM-cadence drumbeat.
- **The $4-5 vs $524 IPG arithmetic** is the chapter's central rhetorical instrument and lands at line 164 ("Total: $524 per ton") + line 168 (IPG ratio "thirty-three and one hundred and twenty-two times"). The arithmetic is structured to be checkable (eight components priced individually at conservative-floor; summed transparently; ratio computed against verifiable historical market prices) — trade-press editor reads as analytical-rigor enacted.
- **The "conservative throughout" framing at line 28** ("Where estimates have a range I use the lower figure, and where an externality is contested I omit it. The goal is not a ceiling but a floor — the smallest honest number the framework can defend") is the chapter's central methodological-discipline move. Editor reads as the chapter pre-empting the "you're overcounting" objection through transparent floor-construction.
- **Chapter-closer at lines 230–240** (book-arc forward-pointer to Ch 9 + Ch 10 + "the invoice / the severed cost / what McDowell County bore" rhetorical pivot) earns the read into Ch 9 with restraint.

**What flags.**
- **Density.** 243 lines + ~6,421 words + eight cost-component walk + cross-case sweep + housing engagement + 2008 financial crisis engagement + YIMBY steelman + three misreadings + brief extrapolation + closing = substantial chapter. Trade-press editor will register that this chapter does extensive work. Hold — substance justifies density; Pass 3.2 voice-polish ratification confirmed cadence-as-content discipline; F-V1 + F-V2 + F-V3 + F-V4 compressions already absorbed the highest-density passages.
- **The line 178 single-paragraph tar-sands + First-Nations addition** is denser than the surrounding paragraphs (housing-pattern → tar sands → Athabasca Chipewyan + Mikisew Cree + Fort McKay First Nations + Treaty 8 of 1899 + canadian courts framing in a single paragraph). Editor reads as substantive-extension territory but may register the cumulative paragraph-load. Hold — paragraph does load-bearing work (extends housing pattern + extends tar-sands case + names Indigenous-treaty case; three substantive moves in one paragraph is appropriate at the chapter's "the pattern made legible" position).

**Verdict: ✓✓ INCLUDE.** Chapter delivers clean chapter-architecture + trade-press-register analytical-quantitative prose + comp-shelf placement signal + arithmetic backbone earning Ch-9 handoff. No structural concerns. Phase-C-β voice-polish work strengthened the cadence picture cleanly.

---

#### 2. Layman-but-engaged reader (book's primary intended reader)

**Profile.** Educated lay reader. No academic economics background. Reads framework-books at the Mazzucato/Sandel/Raworth/Doughnut-economics comp-shelf level. Wants to understand cost-severance arithmetic without apparatus-decoder-ring background.

**What lands.**
- **Chapter-opening question at line 10** is the most accessible single-line chapter-opener in the framework's analytical chapters. "What if everything cost what it actually costs?" — no apparatus; no jargon; direct rhetorical question. Layman reader reads as the framework's load-bearing promise compressed to nine words.
- **The McDowell County return at line 24** ("Return to McDowell County. Return to the county Kennedy visited in 1960") anchors the chapter in the book's established case-territory. Reader who has read Ch 2 + Ch 5 + Ch 6 + Ch 7 recognizes McDowell as the book's load-bearing case; reader fresh to Ch 8 gets enough context ("the county Kennedy visited in 1960... produced more coal than any other in the United States while its residents queued for surplus food") to follow.
- **Eight cost-component walk at lines 32–138** delivers each component in plain language. Direct Health → Environmental Degradation → Community Disruption → Foreclosure → Lineage Labor → Knowledge and Cultural → Political Capture → Temporal Displacement. Each section opens with concrete-anchor ("Begin with the lungs"; "Walk outside the mine"; "The county peaked near one hundred thousand residents in 1950"; etc.) and closes with per-ton numeric attribution. The layman reader can follow each section's arithmetic without prior framework familiarity.
- **The sum at lines 142–164** delivers the eight-component total in bullet-list form. Reader can verify the arithmetic by adding the bullets ($2 + $1 + $5 + $510 + $2 + $1 + $1 + $2 = $524). The bullet-list architecture is layman-reader-friendly (concrete; addable; transparent).
- **The IPG ratio at line 168** ("between thirty-three and one hundred and twenty-two times the 1960 sale price") + the today's-market comparison ("the carbon term alone exceeds the market price by a factor of at least three") gives the reader the chapter's central rhetorical-payoff in plain language. No formal apparatus; just a ratio.
- **Three misreading-defenses at lines 196–206** preempt the layman reader's most likely "but what about X" objections (extraction-should-never-have-happened; market-is-fake; rich-nations-pulling-up-the-ladder). Reader who has been hooked by the chapter's arithmetic but is now generating "wait, what about..." questions has them named and responded to in the same chapter.
- **GDP-not-degrowth response at line 220** ("GDP measures market transactions, not welfare. Every dollar spent cleaning up oil spills counts as economic production. Every medical bill from black lung treatment counts as medical output. GDP rises when the children of McDowell County develop addiction disorders and spend money on treatment. GDP does not fall when they die at fifty-eight") is the chapter's most accessible single-paragraph response to the standard "you're against growth" reflex. Layman reader registers as substantively right.

**What flags.**
- **Carbon arithmetic at line 72** is the chapter's heaviest single technical-passage (EPA AP-42 §1.1 bituminous-coal combustion factor + 93.28 kg CO₂ per mmBtu + 28 mmBtu per short ton + 2.61 metric tons CO₂ per short ton + Rennert et al. 2022 *Nature* + $190/metric ton SCC). For a strict-layman reader without prior climate-arithmetic exposure, this paragraph runs heavier than the rest of the chapter. **MITIGATION on page:** the paragraph closes with "The arithmetic is not subtle. The climate cost of burning one ton of McDowell County coal, at the currently published federal estimate, is approximately five hundred and ten dollars" — the load-bearing dollar figure lands in plain language at the end. Reader who skims the intermediate technical-passage but reads the closing sentence gets the framework's central arithmetic. Substance-drives-length governs; the technical-passage is the chapter's required defensible-anchor for its load-bearing dollar figure.
- **The line 178 single-paragraph density** (housing-pattern + tar sands + First Nations + Treaty 8) is the chapter's second-densest single paragraph. Layman reader will register the paragraph-load. Hold — paragraph does substantive cross-case extension work; the chapter's "the pattern made legible" position is where the cross-case sweep happens, and density at this position is content-justified.
- **Line 168 IPG construction** uses "the Intergenerational Pricing Gap — the ratio of honest price to market price" as the apparatus-name introduction. For a layman reader who has not encountered "Intergenerational Pricing Gap" before in the book, the Title-case apparatus name may register briefly. **MITIGATION on page:** the working definition ("the ratio of honest price to market price") immediately follows the term; reader gets the substantive content. Hold — apparatus-name introduction follows Sandel-hybrid discipline (working definition precedes formal naming) per apparatus register Item 13.

**Verdict: ✓✓ INCLUDE.** Chapter delivers framework-arithmetic at plain-language register; eight-component walk concrete and legible; IPG arithmetic + bullet-list-sum + misreading-defenses + GDP-not-degrowth all land; chapter's central rhetorical promise (the $524 vs $4-5 gap) lands in plain language. The technical-density flag at line 72 is absorbed by the chapter's closing-sentence translation discipline. Layman + specialist test per `feedback_dual_audience_test.md` holds at the layman pole.

---

#### 3. Free-market-economist / center-right policy reader

**Profile.** AEI / Cato / Reason / National Affairs / pure-policy-conservative register. Reads commons-pricing frameworks with default skepticism. Tests for left-coded framing tells, partisan tells, market-failure-overreach signals.

**What lands.**
- **The "conservative throughout" framing at line 28** is the chapter's strongest single audience-management move for this reader. The framework is shown to use lower-bound estimates throughout, omit contested externalities, and aim at a defensible floor rather than at a ceiling. The center-right reader reads as the framework's structural-discipline pre-empting the "you're overcounting" objection through transparent methodological choice.
- **The market-is-not-fake misreading-defense at lines 202–204** is the chapter's most explicit audience-management move for the market-skeptical-conservative subgroup. *"The market is not fake. The market is incomplete. The job of the framework is to name the part that got left out."* — frames the framework's critique as completing the market accounting rather than rejecting market mechanisms. Center-right reader reads as the framework operating within market-economics rather than as anti-market.
- **The pull-up-the-ladder misreading-defense at line 206** explicitly engages developing-nations concerns ("Solar electricity is now cheaper than coal in most of the developing world. The technology exists. The transition timeline should be asymmetric") — the center-right reader who carries development-economics skepticism about climate-policy-as-poverty-trap finds the chapter taking that concern seriously.
- **Extraction-was-real, the-money-was-real, the-coal-left framing at line 202** ("Prices cleared transactions. The money changed hands. Real coal left McDowell County on real rail cars") refuses cheap anti-market framing; substantive engagement with the market's actual function.
- **No-villain framing implicit in the chapter's structural architecture.** The chapter does not pin cost-severance on bad-actor capitalism specifically; the closing of the Lineage Labor section + the closing extrapolation + the GDP-not-degrowth paragraph all operate at structural-architecture level rather than at actor-blame level.
- **The chapter-opener at line 12** ("Ask the question without political coding, without ideology") explicitly disclaims partisan framing at the chapter's literal opening. Center-right reader who scans the first paragraph for political-coding finds the chapter explicitly disclaiming it.

**What flags.**
- **Political Capture section at lines 112–124** is the chapter's most likely friction point for the reflexively-skeptical center-right subgroup. The section names "documented lobbying, regulatory capture, and strategic suppression of research" + walks the SCC political fight (Obama $42 → Trump $1-7 → Biden $51 → EPA 2023 $190) + names "the fossil fuel industry alone" lobbying spend. **MITIGATION on page:** the section closes with the rent-seeking paragraph at line 122 explicitly engaging BOTH reparations-economics (Coates, Darity, Mullen, Hamilton, Conley) AND Public Choice (Buchanan, Tullock) traditions — the chapter explicitly cites the right-of-center analytical tradition (Public Choice) that names rent-seeking as the central political-economy mechanism. Center-right reader who reaches the rent-seeking paragraph reads the chapter as honoring the Public Choice tradition rather than as positioning against it. The asymmetric framing ("the ledger that counts what those traditions described has been costing, and to whom") matches the Ch 9 Reading C v3 framing per `cbef9bd` cross-chapter cascade resolution.
- **The Trump SCC framing at line 118** ("a methodological change academic commentary (Wagner, Anthoff, Cropper, et al. 2021) flagged as ungrounded in standard cost-benefit-analysis practice") names an academic-consensus critique of a Trump-administration methodological choice. The center-right reader will register this as substantively defensible (the global-vs-domestic-scope question is real CBA territory; the academic commentary is on-the-record published work) but politically-attentive readers may register the chapter's framing as one-sided. **MITIGATION on page:** the surrounding paragraph frames the SCC question as one where "one side of that fight has more resources than the other" — generic structural-asymmetry framing rather than partisan-targeted framing. Reader who reaches the structural framing absorbs the political-history walk as analytical rather than as partisan-targeted.
- **YIMBY engagement at lines 180–190** is the chapter's most extensive substantive engagement with a center-right-resonant policy position (zoning-supply-restriction-as-binding-constraint). The chapter takes the steelman seriously (Glaeser + Gyourko + Schuetz cited substantively) and offers a both/and synthesis ("Supply restriction is real and zoning reform is the appropriate response to it; rent-extraction is also real and a different accountability architecture is the appropriate response to it; the two are operating simultaneously"). Center-right reader recognizes the substantive engagement; reads as the chapter doing analytical-honesty work rather than dismissing the YIMBY position.
- **Rent-extractor cluster framing at line 188** ("Asset-class consolidation (the rise of institutional landlords; the financialization of single-family rental as an asset class; the documented pricing-coordination patterns that property-management software has enabled across markets, which the U.S. Department of Justice has been investigating since 2022)") may register as left-coded sector-targeting for some center-right subgroups. **MITIGATION on page:** the framing is empirical (DOJ investigation is on the record; pricing-coordination patterns are documented) rather than ideological; chapter operates at analytical-evidence-level rather than at policy-prescription-level.

**Skim-read risk assessment.**
- **Skim-read A (close-read holds; skim-read may not):** Political Capture section + YIMBY engagement + DOJ-investigation framing form a three-point cluster that, read in skim, could register as left-coded. Close-read of the rent-seeking paragraph (Public Choice citation balances the framework's framing) + the both/and YIMBY synthesis + the empirical-evidence framing of the DOJ point absorbs each into structural-analytical frame. Dual-audience test holds at close-read; skim-read carries a discount.
- **Skim-read B (arithmetic-anchor reader):** A reader who reads the chapter component-by-component (Direct Health → Environmental Degradation → Community Disruption → Foreclosure → ... → Sum → IPG) without close-reading the Political Capture section may encounter the $524 sum + the IPG ratio + the "conservative throughout" methodological discipline framing without ever engaging the political-coding cluster. This reader gets the framework's analytical-instrument frame without encountering the higher-friction Political Capture cluster.

**Net for subgroups:**
- *Literary-knowledgeable conservative reader* (George Will / Yuval Levin / National Review book-section calibrator): ✓✓ INCLUDE (reads the chapter as comp-shelf-standard analytical-quantitative work; Public Choice citation honored; methodology-not-policy disclaimer at line 16 + misreading-defenses at lines 196–206 land).
- *Pure-policy conservative reader* (Cato libertarian / AEI fellow / pure-free-market economist): ✓ INCLUDE (arithmetic-anchor reader + conservative-throughout methodological-discipline + market-is-not-fake misreading-defense earn through; Political Capture section + YIMBY rent-extractor framing register as left-resonant but the rent-seeking paragraph's Public Choice citation absorbs).
- *Reflexively-skeptical conservative reader* (the "left-coded" calibrator): ✓ INCLUDE (Political Capture cluster registers as positioning; chapter still earns through to close because eight-component arithmetic + conservative-throughout methodological discipline + market-is-not-fake misreading-defense + Public Choice citation in the rent-seeking paragraph do substantial offsetting work).

**Verdict: ✓✓ INCLUDE** (aggregate). Light discount for the reflexively-skeptical subgroup is real but bounded; chapter holds all three subgroups at INCLUDE through close. The conservative-throughout methodological discipline + market-is-not-fake misreading-defense + Public Choice citation in the rent-seeking paragraph do what no other chapter in the book can do for the center-right reader: they demonstrate the framework operating with explicit floor-not-ceiling discipline, refusing cheap anti-market framing, and honoring the right-of-center analytical tradition (Public Choice) that named rent-seeking. This is uniquely Ch 8's audience-management asset.

---

#### 4. Tier-1 quantitative reader / climate-economics + SCC-literature specialist [Ch-8-SHARPENED vs Ch 7 baseline]

**Profile.** Climate-economics specialist (Resources for the Future / RFF energy program; EPA Office of Air and Radiation; IAM-tradition climate-economics academic; Rennert / Anthoff / Cropper / Stern / Nordhaus / Wagner cluster). Reads for SCC-anchor precision; EPA-update chronology accuracy; Rennert et al. 2022 *Nature* citation accuracy; bituminous-coal combustion-factor accuracy; IPG arithmetic defensibility; cross-case order-of-magnitude defensibility (Deepwater / Libby / Baotou / Valdez).

**What lands.**
- **SCC anchor at line 72** ($190/metric ton; Rennert et al. 2022 *Nature*; EPA 2023 update): this is the canonical post-2023 federal SCC anchor; specialist reader recognizes the Rennert et al. 2022 paper as the load-bearing peer-reviewed grounding (Rennert, Errickson, Prest, Rennels et al., *Nature* 610, 2022). The chapter's citation discipline is correct.
- **Bituminous-coal combustion factor at line 72** (EPA AP-42 §1.1; 93.28 kg CO₂ per mmBtu; 28 mmBtu per short ton for Pocahontas seam; 2.61 metric tons CO₂ per short ton): this is the chapter's most precise quantitative claim. The EPA AP-42 §1.1 source is canonical (EPA Compilation of Air Pollutant Emissions Factors); the 93.28 kg CO₂ per mmBtu is the canonical bituminous default; the 28 mmBtu per short ton Pocahontas-seam heat content is on the high end of bituminous range but defensible for Pocahontas (which is high-quality metallurgical-grade bituminous). Specialist reader reads the cascade-reconciliation `9befb92` work as deliberate methodological care (chapter explicitly distinguishes McDowell-specific 2.61 from national-average 2.32 to avoid cross-chapter inconsistency with Ch 6's framework-level anchor).
- **SCC political-fight chronology at line 118** (Obama $42 via EO 12866; Trump $1-7 via geographic-scope limitation; Biden $51 via global-scope methodology return; EPA 2023 $190): all dates and dollar figures are correct against published academic + administrative record. Wagner, Anthoff, Cropper, et al. 2021 critique is a real published paper (Wagner et al. 2021 critique of Trump-era SCC methodology). Specialist reader reads as careful policy-chronology engagement.
- **Black Lung Benefits Program 1969 establishment at line 34** anchors the chapter's per-ton allocation arithmetic at the Program's legislative origin (Federal Coal Mine Health and Safety Act of 1969). Specialist reader who knows the historical record recognizes the 1969 anchor.
- **Reclamation bonds gap at line 48** ("between three and a half and six billion dollars short" + "available bonds total three point eight billion against cleanup costs estimated at seven and a half to nine point eight billion") + 1977 SMCRA: precise + defensible against current published estimates (Office of Surface Mining reclamation-bond-deficit data + GAO 2018 + WV Department of Environmental Protection reporting). Specialist reads as carefully-anchored.
- **2008 financial crisis architecture passage at line 192** (~$11T household wealth destruction; ~10M foreclosure filings; ~5M completed foreclosures; ~$700B TARP authorization; Mian & Sufi 2014 *House of Debt* citation): all figures are within published-academic-range; Mian & Sufi 2014 is the canonical academic citation for the welfare-cost-of-2008-architecture analysis. Specialist recognizes the citation discipline.
- **Cross-case IPG sweep at line 174** (Deepwater Horizon IPG 15-17 + Macondo well 40-60M barrels + 17-26M tons CO₂ at $190/ton = +$3-5B carbon-tail; W. R. Grace Libby IPG 40-80; Baotou rare-earth + Exxon Valdez): order-of-magnitude consistent with published-academic estimates. The framework-additionality framing (framework adds carbon-tail layer to documented-costs IPG; addition shifts the answer only slightly for Deepwater because documented costs already exceed market revenue by an order of magnitude) is the methodological-honesty move specialist reader values — chapter explicitly names where the framework's additional layer matters and where it doesn't.
- **IPG ratio construction at line 168** ("between thirty-three and one hundred and twenty-two times the 1960 sale price" + "at least three" carbon-vs-today's-market): post-Phase-C cross-corpus IPG canonical-construction Option D applied (per commit `57575b1`). Specialist reads the explicit-range construction + the today's-market carbon-alone-exceeds-by-3× framing as the chapter's most defensible single quantitative claim.

**What flags.**
- **Reclamation cancer-cases claim at line 50** ("the sixty thousand Appalachian cancer cases linked to mountaintop removal mining"): this is on the high end of published epidemiology range (Hendryx + colleagues at WVU have published cumulative cancer-mortality estimates in this band, though the specific 60,000 number requires Hendryx-specific citation that the chapter does not provide). Specialist reader may want explicit citation. **MITIGATION on page:** the figure is paragraph-internal and supports the broader environmental-degradation argument; chapter's "conservative throughout" framing at line 28 + the broader cost-component arithmetic at line 52 ("one to three dollars" per-ton allocation) absorbs any specialist friction about the specific epidemiology number — the per-ton allocation is the load-bearing quantitative claim, and it sits within published-academic-range. Hold per Pass 3.1 closure; pre-publication refresh may add explicit Hendryx citation if author opts.
- **Drug-induced death rate at line 58** ("In 2015, the county recorded the highest drug-induced death rate of any county in America: one hundred forty-one per hundred thousand"): McDowell County did rank highest nationally in 2015 (CDC NCHS county-level mortality data); the specific 141 per 100,000 figure is consistent with published reporting. Specialist reads as carefully-anchored.

**Verdict: ✓✓ INCLUDE.** All Pass-3.1 Phase-C precision spot-fixes integrated cleanly; chapter holds the climate-economics quantitative reader at INCLUDE on all major SCC + bituminous-combustion + IPG + cross-case + 2008-architecture tests. The cross-corpus IPG canonical-construction at line 168 (Option D applied) is exactly the methodological-construction discipline this reader values. The methodological-honesty framing for cross-case IPG (framework adds carbon-tail layer where it matters; explicit naming of where the layer doesn't matter for Deepwater) is the kind of analytical-care that specialist reader registers as deliberate.

---

#### 5. Literary agent (Wylie-cluster trade-press calibrator)

**Profile.** Wylie / Sarah Chalfant / Tracy Bohan-cluster literary agent. Reads for sustainable-book-author signals; commercial-arc evaluation; comp-titles fit; subsidiary-rights potential (excerpt-to-magazine value; foreign rights; audio); the question "can I sell this to an acquisitions editor?"

**What lands.**
- **Sample-chapter strength.** Per workstream handoff, Ch 8 is a strong sample-chapter candidate alongside Ch 5 + Ch 7 for agent / publisher queries. The chapter delivers the framework's central-arithmetic claim cleanly through 243 lines; chapter-architecture is legible; eight-component walk + cross-case sweep + brief extrapolation gives the agent a self-contained substantive chapter to send to acquisitions editors.
- **Comp-shelf placement.** The eight-component cost-walkthrough + the cross-case pattern sweep + the both/and YIMBY synthesis + the misreading-defenses + the brief extrapolation reads as Mazzucato/Sandel/Raworth/Pistor/Christophers comp-shelf-ready analytical-quantitative prose. The reparations-economics + Public Choice + Black-American-writing-tradition lineage citations at lines 92 + 122 expand comp-cluster reach across multiple intellectual-tradition reader-clusters.
- **Subsidiary-rights potential.** Multiple excerpt-able passages: the chapter-opening + eight-component walk through Direct Health (lines 32–40); the carbon arithmetic + SCC political fight (lines 68–124); the Black-American-writing-tradition passage at line 92; the cross-case pattern sweep (lines 174–178); the 2008 financial crisis passage (line 192); the three misreading-defenses (lines 196–206); the brief extrapolation + GDP-not-degrowth (lines 210–222); the chapter-closer (lines 230–240). Most strongly: the chapter as a whole functions as a "the framework applied" essay-length argument that magazine venues (Boston Review / Phenomenal World / Aeon / Noema / Harper's) would consider for excerpt or commission.
- **Chapter-closer at lines 230–240** (book-arc forward-pointer to Ch 9 + Ch 10 + "the invoice / the severed cost / what McDowell County bore" rhetorical pivot) is the kind of well-architected chapter-architecture that agents read as "this author can sustain a book."
- **Framework-promise honored at chapter close.** The chapter establishes the framework's central-arithmetic claim, computes the IPG, extrapolates to civilizational scale with explicit scope-discipline ("a gestured claim... that cannot honestly be compressed into the closing pages of a framework book"), and hands forward to Ch 9 with restraint. Agent reads as honest scope-discipline.

**What flags.**
- **Chapter density.** 243 lines + ~6,421 words is substantial for a single sample chapter; an agent reading the sample-chapter package will register the cognitive load. Hold — substance justifies the density; chapter-architecture distributes the load across twelve section-breaks.
- **The brief extrapolation at line 214** ($10-15T annual civilizational-scale severed cost; "largest continuous wealth transfer in human history") is the chapter's most aggressive claim. Agent reads as commercial-arc-strengthening (chapter delivers a quantitative civilizational-scale claim that magazine editors would commission to develop) but the chapter's own scope-discipline ("a gestured claim... cannot honestly be compressed") names the limit. Agent reads as marketable-without-overclaim.

**Verdict: ✓✓ INCLUDE.** Chapter delivers strong sample-chapter material + comp-shelf placement + subsidiary-rights potential + chapter-architecture signal. The eight-component arithmetic + cross-case sweep + brief extrapolation give the chapter a unique commercial-arc position in the book (the framework's load-bearing analytical-quantitative chapter; the chapter that delivers the framework's central rhetorical-arithmetic promise). Sample-chapter-ready for publisher / agent queries.

---

### Tier 2 — pipeline-strengthening characters

#### 6. Trade publisher acquisitions editor [book-deal-gating]

**Profile.** Acquiring editor at a trade-press imprint (Penguin Press, Public Affairs, Princeton-trade, Norton, or trade arm of a university press). Reads for commercial viability; comp-titles cluster placement; the question "can my marketing team find the audience for this book?"; whether the chapter-opener earns the read forward; bookstore-buyer hook.

**What lands.**
- **Reader-trust foundation across 243 lines.** Acquisitions editor reads chapter as sample of the author's analytical voice + reader-trust foundation. The chapter delivers — analytical-quantitative register holds throughout; apparatus residue clean (verified Pass 3.2 §5 + Item 1 inline-integral strip §5.1 below); named-subject discipline holds (Coates / Darity / Mullen / Hamilton / Conley + Buchanan / Tullock + Dunbar / Du Bois / Fanon / Ellison + Mian / Sufi + Glaeser / Gyourko / Schuetz all on-record published academic work; Kennedy + Dunbar historical-record; Rennert / Wagner / Anthoff / Cropper named via published-paper-citation; First Nations named at line 178 via Treaty 8 of 1899 public-record).
- **Sample-chapter candidacy strong.** Acquisitions editor reading the sample-chapter package gets a 243-line chapter that delivers the framework's central-arithmetic claim, walks through eight cost components for McDowell County coal, computes the IPG, extends to cross-case pattern (Deepwater / Libby / Baotou / Valdez + housing + tar sands + 2008 financial crisis), engages the YIMBY steelman with both/and synthesis, defends against three misreadings, extrapolates to civilizational scale, and hands forward to Ch 9. This is the chapter that demonstrates the framework's arithmetic-claim.
- **Comp-shelf placement.** Mazzucato / Sandel / Pistor / Raworth / Christophers / Susskind comp-shelf register that this acquisitions editor recognizes. The reparations-economics + Public Choice + Black-American-writing-tradition lineage citations expand comp-cluster reach.
- **Marketing team hook.** Multiple cover-copy / jacket-flap candidates: "a ton of coal that sold for $4 actually cost $524"; "the largest continuous wealth transfer in human history"; "what things actually cost"; the McDowell County eight-component arithmetic. The IPG ratio is the chapter's most-marketable single number.
- **Bookstore-buyer-pitch-ready compact statements.** "The market is not fake. The market is incomplete. The job of the framework is to name the part that got left out." (line 204); "GDP measures market transactions, not welfare" (line 220); "What if everything cost what it actually costs?" (line 10) — all comp-shelf-jacket-pull-quote candidates.

**What flags.**
- **Density question.** 243 lines is substantial. Acquisitions editor reads as depth-virtue (chapter earns its weight) rather than as pacing-flag — twelve section-breaks distribute the load + Pass 3.2 voice-polish work already tightened the highest-density cadence patterns.
- **Civilizational-scale extrapolation aggressiveness.** $10-15T annual figure is the chapter's most-aggressive claim. Editor reads as marketable-without-overclaim per chapter's own scope-discipline ("a gestured claim... cannot honestly be compressed").

**Verdict: ✓✓ INCLUDE.** Sample-chapter-ready; commercial-arc + comp-shelf + marketing-hook all deliver. Pass 3.2 already absorbed the cadence concerns. Acquisitions editor reads chapter as book-promising material.

---

#### 7. Venue editor for derivative works (Aeon / Noema / Boston Review / Phenomenal World composite)

**Profile.** Composite character spanning Boston Review (memoir-policy-essay venue commissioned for Ch 5; analytical-essay for Ch 8 candidate), Noema (three-register weave), Aeon (Sam Haselby; per Ch 7 Mask-of-Abundance pitch alignment), Phenomenal World (heterodox-econ methods-note). Reads chapter as sample of the author's voice + intellectual-tradition commitments when evaluating derivative-work pitches.

**What lands — venue-specific.**

- **For Boston Review.** Boston Review already commissioned/pitched on Ch 5 territory; Ch 8 sits in the BR analytical-policy-essay register at full strength. The chapter's central-arithmetic claim ($524 vs $4-5) + the IPG ratio + the cross-case pattern sweep + the YIMBY both/and synthesis + the 2008-financial-crisis policy-choice framing all sit in BR's analytical-policy register. Reparations-economics citation + Black-American-writing-tradition passage + Public Choice acknowledgment all match BR's intellectual-tradition reach. ✓✓✓ INCLUDE for BR (analytical-essay derivative track).
- **For Aeon (Sam Haselby).** Aeon Version C pitch fire window remains active (per Ch 7 cousin §0); Ch 7 carries the primary Aeon-derivative-pipeline alignment. Ch 8 is secondary for Aeon — analytical-quantitative register is not Aeon's primary memoir-history-theory weave, but the chapter's Black-American-writing-tradition passage at line 92 + the GDP-not-degrowth + civilizational-scale extrapolation paragraphs are Aeon-essay-derivable material. ✓✓ INCLUDE for Aeon (secondary derivative track).
- **For Noema.** Noema values three-register weave (memoir + history/theory + reportage). Ch 8 is NOT a three-register-weave chapter; it is analytical-quantitative. However, the Black-American-writing-tradition passage at line 92 + the McDowell County concrete-anchoring + the 2008-financial-crisis architecture engagement + the brief extrapolation gives Noema editor essay-derivable material at chapter-length. ✓✓ INCLUDE for Noema (analytical-essay derivative track).
- **For Phenomenal World.** Heterodox-econ academic-adjacent. The chapter's framework-arithmetic + IPG construction + cross-case sweep + Mian & Sufi 2014 *House of Debt* engagement + the both/and YIMBY synthesis + the asset-class-consolidation framing + the rent-seeking paragraph's framework-vs-Public-Choice + framework-vs-reparations-economics framing is exactly the kind of intellectual-history positioning PW publishes at depth. ✓✓✓ INCLUDE for PW (heterodox-econ methods-note derivative track).

**What flags.**
- **For more centrist or right-of-center venues (Project Syndicate; Bloomberg Opinion; National Affairs; American Affairs).** Political Capture section + asset-class-consolidation framing + 2008-financial-crisis policy-choice framing form a cluster that reads as scholarly-left-coded positioning for editors at these venues. Not disqualifying — the chapter's "conservative throughout" methodological discipline + market-is-not-fake misreading-defense + Public Choice citation in rent-seeking paragraph balance the cluster. ✓ INCLUDE for these venues.
- **For pure-trade outlets (NYT / WaPo Opinion).** Eight-component arithmetic + IPG ratio + cross-case pattern + civilizational-scale extrapolation all excerpt-able. ✓✓ INCLUDE.

**Verdict: ✓✓✓ INCLUDE for memoir-history-theory + analytical-policy venues** (BR ✓✓✓; PW ✓✓✓; Aeon ✓✓; Noema ✓✓). **✓ INCLUDE for more centrist or right-of-center venues.** Aggregate: **✓✓✓ INCLUDE** (BR + PW analytical-policy derivative pipelines strongly served; other venues at INCLUDE).

---

#### 8. Tier-1 left-policy reader

**Profile.** Reader at the Stone Center / Roosevelt Institute / Hewlett-Foundation-supported policy register. Reads for structural-critique framings + intergenerational-equity arguments + commons-pricing apparatus development.

**What lands.**
- **Universality claim implicit in the chapter-opener at line 10** establishes the framework's analytical scope: the question "What if everything cost what it actually costs?" is the structural-critique question this reader operates within.
- **Eight cost-component walk** delivers the framework's structural-cost-bearer-vs-value-capturer accounting at the per-ton arithmetic level. This reader reads as commitment to cost-bearing-and-accounting work at the analytical-quantitative register.
- **Lineage Labor section at lines 84–96** ("intergenerational wealth transmission... becomes impossible when the family's entire asset base consists of a house in a hollow that cannot be sold") is direct intergenerational-equity framing. Opportunity Insights citation at line 90 anchors the structural-mobility claim in canonical academic evidence (Chetty + Hendren + colleagues; Opportunity Insights project is the load-bearing intergenerational-mobility data source).
- **Black-American-writing-tradition passage at line 92** (Dunbar + Du Bois + Fanon + Ellison) + the framework's contribution closer ("The framework adds the cost-accounting mechanism by which the mask remains structurally necessary") sits in this reader's intellectual-tradition lineage at full strength.
- **Political Capture section** + rent-seeking paragraph at line 122 names the structural-architecture-as-shaped-by-specific-actors point that this reader carries as central analytical commitment. The reparations-economics citation (Coates, Darity, Mullen, Hamilton, Conley) explicitly honors this reader's tradition.
- **Housing-pattern section** + asset-class-consolidation framing at line 188 (institutional landlords; financialization of single-family rental; pricing-coordination patterns DOJ investigating since 2022) is direct structural-rent-extraction analysis at the analytical-quantitative register this reader works within.
- **2008-financial-crisis policy-choice framing at line 192** (Mian & Sufi 2014 *House of Debt*; recapitalizing bank balance sheets rather than restructuring household debt) is exactly the structural-policy-choice analysis this reader has been carrying for over a decade.
- **Closing-section "what honest pricing does not mean" misreading-defenses at lines 196–206** + GDP-not-degrowth at line 220 deliver the framework's structural-political-discipline at full strength — this reader reads as the framework refusing both right-of-center reflex-defense AND degrowth-coded over-claiming.

**What flags.**
- None substantive. Chapter delivers across this reader's full pressure-test surface at strong strength.

**Verdict: ✓✓✓ INCLUDE.** Chapter is a strong-INCLUDE for this reader; framework-arithmetic + intergenerational-equity (Opportunity Insights + Lineage Labor section) + Black-American-writing-tradition lineage + structural-rent-extraction analysis + 2008-architecture engagement + misreading-defenses all deliver at full strength.

---

#### 9. Tier-2 reparations-economics reader (Coates / Darity / Mullen / Hamilton / Conley)

**Profile.** Direct comp-team peer. Reads chapter for tradition-companionship signals + cross-chapter framework consistency + framework-contribution-vs-tradition-extension framing.

**What lands.**
- **Explicit lineage-naming at line 122** ("The reparations-economics tradition (Coates, Darity, Mullen, Hamilton, Conley) supplies the actor-and-coalition vocabulary for the racial wealth gap"): direct citation. Reader registers respect.
- **Framework's-different-in-kind framing at line 122** ("The framework's contribution is different in kind: the ledger that counts what those traditions described has been costing, and to whom — the cost-bearing magnitudes that name McDowell County's thirteen-year life-expectancy gap as a number rather than as an actor-attribution problem"): this is the asymmetric framing that matches the Ch 9 Reading C v3 framework-as-measurement-AND-decision-tool framing. Reparations-economics reader reads as the framework continuing the tradition with a different analytical instrument rather than as displacing the tradition. Cross-chapter cascade resolution at commit `cbef9bd` ensures consistent asymmetric framing across Ch 8 + Ch 9.
- **Black-American-writing-tradition passage at line 92** (Dunbar + Du Bois + Fanon + Ellison + framework-contribution closer): the four-author parallel-citation + framework-adds-cost-accounting-mechanism closer reads as honoring the tradition's intellectual-historical lineage. Reader recognizes the chapter's careful naming of the tradition's literary-philosophical anchors.
- **Lineage Labor section at lines 84–96** centers intergenerational-cost-bearing at the analytical-quantitative-arithmetic level. Reparations-economics reader recognizes the framework operating at the cost-bearer-and-accounting register the tradition has been pushing toward.
- **Opportunity Insights citation at line 90** (Chetty + Hendren + colleagues mobility data) anchors the intergenerational-mobility claim in the canonical academic source the tradition uses.

**What flags.**
- **Coates / Darity-Mullen not named at depth in Ch 8 body prose.** Named at line 122 + engaged at depth at Ch 5 (where the Restitution Bond + Foreclosure Bond + Pistor + Coates lineage lives). This is structurally correct — Ch 8 is the analytical-quantitative-arithmetic chapter; Ch 5 is the apparatus-chapter that carries the lineage roll-call. Reader who reads only Ch 8 (not the full book) gets the lineage-naming but not the depth-engagement; reader who reads the full book gets the full lineage at Ch 5 + Ch 8's analytical-quantitative complement.

**Verdict: ✓✓✓ INCLUDE.** Direct comp-team peer reads chapter as full-strength companion to reparations-economics work. The framework's-different-in-kind asymmetric framing at line 122 + Black-American-writing-tradition citation + Lineage Labor section + Opportunity Insights anchor all deliver at strong strength.

---

#### 10. Tier-2 Public Choice reader (center-left wing — Lindsey & Teles *The Captured Economy* tradition)

**Profile.** Reads rent-seeking analysis applied to specific community consequences (their political project); framework that bridges public-choice methodology with democratic-accountability + inequality-reduction work.

**What lands.**
- **Public Choice citation at line 122** ("The Public Choice tradition (Buchanan, Tullock) supplies the vocabulary for the extractor's reasoning that shaped the political-coalition record on the books"): explicit lineage-naming + asymmetric framing-alignment with Ch 9 Reading C v3. This reader registers as the framework taking the public-choice methodology seriously.
- **Framework's-different-in-kind framing at line 122** ("the ledger that counts what those traditions described has been costing, and to whom"): this is the move Lindsey & Teles also make in *The Captured Economy* — taking public-choice methodology and using it to document specific inequality-and-accountability consequences. Chapter reads as fellow-traveler.
- **Political Capture section at lines 112–124** centers documented lobbying + regulatory capture + strategic suppression of research at the analytical-quantitative-arithmetic level. The SCC political-fight history (Obama/Trump/Biden/EPA-2023) is exactly the kind of concrete rent-seeking-mechanism documentation Lindsey & Teles foreground in their work.
- **Asset-class-consolidation framing at line 188** (institutional landlords + financialization + DOJ-investigated pricing-coordination patterns) is the kind of empirical rent-seeking analysis this reader recognizes from *The Captured Economy*.
- **Coordination with Ch 9 Reading C v3.** Post-`cbef9bd` cross-chapter cascade resolution: Ch 8 + Ch 9 now read as consistent asymmetric framing of framework-vs-Public-Choice. Reader proceeding Ch 8 → Ch 9 experiences continuous asymmetric framing.

**What flags.**
- **Buchanan attribution.** Buchanan is on the *Democracy in Chains* (MacLean) controversy spectrum; this reader may want explicit acknowledgment that the framework draws on rent-seeking methodology while not endorsing Buchanan's broader political project. The framework's-different-in-kind framing at line 122 implicitly distances framework from B&T political project (the framework's analytical-instrument is on cost-bearing magnitudes; B&T political-project is on extractor-rationality + small-government); but the chapter doesn't explicitly engage the MacLean controversy. Hold — Ch 9 carries the asymmetric framing at depth; this reader reads Ch 8 + Ch 9 together.

**Verdict: ✓✓ INCLUDE.** Chapter delivers Public Choice citation + framework's-different-in-kind asymmetric framing + Political Capture concrete documentation + asset-class-consolidation empirical rent-seeking analysis. Cross-chapter cascade resolution at `cbef9bd` ensures Ch 8 + Ch 9 read consistently for this reader.

---

#### 11. Tier-2 housing-economics reader (Glaeser + Gyourko + Schuetz YIMBY-tradition) [NEW vs Ch 7 baseline; per Ch 8 chapter-specific tilt]

**Profile.** Housing-economics academic at Glaeser + Gyourko + Schuetz + Mast + Hsieh-Moretti cluster. YIMBY-aware (supply-restriction-as-binding-constraint scholar). Reads chapter's YIMBY engagement for accuracy of the steelman + substantive engagement with the empirical supply-economics literature + appropriate scope-discipline.

**What lands.**
- **YIMBY-steelman accuracy at lines 180–182.** Chapter names Edward Glaeser AND Joseph Gyourko AND Jenny Schuetz substantively (not just gesturing); cites "supply-constrained metropolitan areas" + "land-use regulation as the binding constraint" + "liberalizing zoning produces measurable rent moderation in the markets where it has been tried." This is the YIMBY-position-steelman at full strength. Housing-economics reader reads as the chapter taking the position seriously.
- **Both/and synthesis at lines 184–190.** Chapter does NOT dismiss YIMBY position; offers structural both/and synthesis ("supply-side analysis and rent-extraction analysis are operating at different levels of the same case, and that engaging only one of them produces incomplete diagnosis"). The supply-restricted vs supply-expanded metro-comparator empirical move at line 186 (San Francisco/NY/Boston/Seattle vs Atlanta/Phoenix/Houston/Charlotte; JCHS 2024 cost-burden share rising in BOTH) is the chapter's most empirically-grounded analytical move on the housing question. Housing-economics reader reads as analytically-disciplined work.
- **Across-supply-elasticity-spectrum cost-burden-rise framing at line 186** is the chapter's substantive empirical claim — supply restriction explains level-differences across markets; it does NOT explain the across-market rise in cost-burdened share. This is a falsifiable empirical claim grounded in JCHS data; reader recognizes the analytical-discipline.
- **Asset-class-consolidation framing at line 188.** Names institutional landlords + financialization of single-family rental + pricing-coordination patterns + DOJ investigation since 2022. This is the rent-extraction mechanism the chapter argues operates on top of supply elasticity. Housing-economics reader reads as substantive engagement with the post-2010 institutional-investor literature.
- **Closing both/and at line 190.** "Supply restriction is real and zoning reform is the appropriate response to it; rent-extraction is also real and a different accountability architecture is the appropriate response to it; the two are operating simultaneously and the policy response has to address both." This is the chapter's most explicit non-zero-sum framing of the housing question; housing-economics reader (especially the supply-restrictionist-but-not-monomaniacal subset) reads as analytical work that earns continued engagement.

**What flags.**
- **Mast / Hsieh-Moretti not named.** Recent housing-economics literature on filtering (Mast 2023) + on misallocation (Hsieh-Moretti) is not cited. Hold — chapter operates at the framework-engagement level; the depth-engagement with specific recent papers belongs at separate scholarly piece.
- **The framework's claim that supply restriction does NOT explain cost-burden rise across markets** is empirically defensible against current JCHS data but is the chapter's most-contested-by-YIMBY-orthodoxy claim. **MITIGATION on page:** the chapter does not deny supply-restriction effects on price LEVELS; it argues supply-restriction does not explain the across-market cost-burden SHARE rise. This is a precise empirical claim that survives YIMBY-orthodoxy pressure-testing because both effects can be true simultaneously (supply restriction raises price levels in restricted markets; asset-class consolidation raises cost-burden share across all markets).

**Verdict: ✓✓ INCLUDE.** Chapter delivers YIMBY-steelman at full strength + both/and synthesis + supply-restricted-vs-expanded empirical comparator + asset-class-consolidation framing + closing non-zero-sum framing. The chapter's analytical-honesty about the housing question (acknowledging supply-side empirics + naming asset-class-consolidation as additional mechanism) earns the housing-economics reader through close.

---

#### 12. Tier-2 climate-policy / SCC-tradition reader [NEW vs Ch 7 baseline; per Ch 8 chapter-specific tilt]

**Profile.** Climate-policy specialist (Resources for the Future / RFF energy program; EPA Office of Air and Radiation; Hewlett-Foundation climate-policy grantee; IPCC contributor cluster). Reads for SCC-anchor precision + EPA-update chronology + Rennert et al. 2022 citation accuracy + the chapter's framing of the climate-policy political fight.

**What lands.**
- **SCC anchor at line 72** ($190/metric ton; Rennert et al. 2022 *Nature*; EPA 2023 update): canonical post-2023 federal SCC anchor with peer-reviewed grounding. Climate-policy specialist recognizes the Rennert et al. 2022 paper as the load-bearing academic update that drove the EPA 2023 revision.
- **SCC political-fight chronology at line 118** (Obama $42 via EO 12866; Trump $1-7 via geographic-scope limitation; Biden $51 via global-scope methodology return; EPA 2023 $190 + the Wagner, Anthoff, Cropper, et al. 2021 critique citation): this is the most substantive single-paragraph engagement with the SCC political-fight history in the analytical-essay register. Reader reads as the chapter taking the SCC political-economy question seriously — including the methodological-critique work academic-climate-economists have done on the politically-driven scope-limitation move.
- **"The number is not uncertain because carbon physics is uncertain. The number is uncertain because the question of how much of the cost should be priced is a political fight" at line 118** is the chapter's clearest framing of the SCC question for this reader. Climate-policy specialist reads as substantive engagement with the political-economy of climate accounting.
- **Carbon-arithmetic at line 72** (2.6 metric tons CO₂ per ton coal × $190/ton SCC = $510 per-ton climate cost) is the chapter's load-bearing dollar-figure for the framework's central-arithmetic claim. Climate-policy specialist reads as carefully-anchored quantitative work.
- **Tar-sands + carbon-tail framing at line 178** ("the atmospheric carbon tail follows the combustion wherever the barrels are burned") extends the framework's climate-accounting to bitumen-extraction; specialist reads as cross-resource consistency.

**What flags.**
- **Externality-tail beyond SCC framing at line 78** ("before option value, before ecosystem service losses from atmospheric warming, before the climate-induced mortality and migration costs that the social cost of carbon understates"): specialist reader recognizes this as the active climate-economics debate (whether SCC fully captures non-market damages). Hold — chapter operates at the chapter-summary level; the depth-engagement with SCC-completeness debate belongs at separate scholarly piece. The framing is empirically defensible (current SCC estimates are widely-acknowledged-incomplete by climate-economists themselves).
- **Wagner et al. 2021 citation at line 118** is one named-paper citation; specialist may want broader citation-cluster for the academic-consensus claim. **MITIGATION on page:** the framing is "academic commentary... flagged" which signals that the cited paper represents a broader-academic-consensus position rather than a single-paper claim. Reader registers as appropriate-citation-discipline.

**Verdict: ✓✓✓ INCLUDE.** Chapter delivers SCC-anchor precision + EPA-update chronology + Rennert et al. 2022 grounding + SCC political-fight history engagement + tar-sands carbon-tail consistency + carbon-arithmetic that anchors the framework's central dollar-figure. Climate-policy specialist reads as substantive analytical-policy work at full strength.

---

#### 13. Tier-2 First-Nations / Indigenous-treaty reader [NEW vs Ch 7 baseline; per Ch 8 chapter-specific tilt]

**Profile.** Indigenous-rights scholar / treaty-rights attorney / First-Nations-governance researcher (Athabasca Chipewyan / Mikisew Cree / Fort McKay First Nations affiliated reader; First Nations Land Management Resource Centre reader; Treaty 8 First Nations reader). Reads chapter's First Nations naming at line 178 for accuracy + substantive treatment + appropriate scope-respect.

**What lands.**
- **Explicit naming at line 178.** "The Athabasca Chipewyan First Nation, Mikisew Cree First Nation, and Fort McKay First Nation, whose traditional territories under Treaty 8 of 1899 sit above and beside the bitumen deposits, have documented elevated cancer rates in downstream communities, contaminated traditional-food sources, and consultation-and-consent failures the Canadian courts have engaged repeatedly without resolving the structural arrangement." This is direct + substantive naming. Treaty 8 of 1899 is correctly anchored (Treaty 8 was signed June 21, 1899; encompasses northern Alberta + parts of British Columbia + Saskatchewan + Northwest Territories; the three named First Nations are among the Treaty 8 signatories whose traditional territories sit above/beside the Athabasca oil sands deposits).
- **"Consultation-and-consent failures the Canadian courts have engaged repeatedly without resolving the structural arrangement" framing.** This is substantively accurate against the documented record (Mikisew Cree v. Canada 2018 + Yahey v. British Columbia 2021 + multiple lower-court rulings on Treaty 8 cumulative-impacts + consultation-discipline failures). Reader recognizes the chapter taking the legal-procedural-failure history seriously.
- **"Documented elevated cancer rates in downstream communities" + "contaminated traditional-food sources" framing.** Substantively accurate against the documented epidemiology and community-monitoring record (Alberta Cancer Board 2009 + multiple Indigenous-led environmental-monitoring programs + downstream-community studies). Reader recognizes the chapter taking the documented harm seriously.
- **Framework-application-returns-same-order-of-magnitude framing.** "Framework application against tar sands returns the same order-of-magnitude gap that coal returns" extends the framework's analytical-quantitative apparatus to bitumen-extraction; reader reads as the framework's-instrument-applicability honoring the Indigenous cost-bearing dimension.
- **Cross-resource consistency.** The framework's structural-cost-severance accounting applies to bitumen the way it applies to coal; First Nations cost-bearing is treated as analytically-symmetric with McDowell County / Baotou / Niger Delta cost-bearing.

**What flags.**
- **First Nations not given voice in the chapter.** Chapter is third-person expository; First Nations are named but do not speak. Per cross-chapter inventory + Ch 9 Pass 3.3 character #13 disposition, the chapter's third-person register is structurally-correct for the analytical-quantitative chapter; first-person voice belongs in Ch 1 / Ch 3 / Ch 10 / other-chapter venues. Reader who knows the book's register-architecture will register the framework's depth of engagement (analytical-quantitative cost-bearing accounting) even without First Nations first-person voice.
- **Compressed treatment.** First Nations naming + Treaty 8 + cancer rates + consultation-and-consent failures + Canadian-courts framing all in a single paragraph (line 178). Reader may want depth-treatment in a dedicated section. Hold — chapter operates at the cross-case-pattern-extension level; the depth-treatment belongs at separate Indigenous-rights-focused work.
- **No engagement with specific First Nations governance positions or with Indigenous-led alternative-architecture proposals.** Chapter operates at the framework-applicability-acknowledgment level rather than at the alternative-architecture-development level. Reader may want broader engagement; chapter scope is appropriately bounded for an analytical-quantitative-arithmetic chapter.

**Verdict: ✓✓ INCLUDE.** Chapter delivers substantive First Nations naming + Treaty 8 of 1899 accuracy + documented-harm framing + cross-resource framework-applicability + structural-cost-bearing analytical-symmetric treatment. The chapter's third-person register + compressed single-paragraph treatment is structurally-appropriate for an analytical-quantitative chapter; reader recognizes cross-chapter scope-distribution honors the cost-bearing acknowledgment at the appropriate analytical-quantitative depth.

---

### Tier 3 — cultural-resonance + accessibility + practitioner characters

#### 14. Literary reader (analytical-prose calibrator)

**Profile.** Reads for analytical-prose discipline; chapter-architecture; voice register coherence; cumulative cadence; rhetorical-pivot quality.

**What lands.**
- **Voice register holds throughout** (analytical-quantitative dominant; brief deliberate first-person register-architecture at lines 96 + 138 + 222 per F-V4 Option B retain-one-strong-site disposition). Pass 3.2 voice-polish ratification confirmed register coherence at chapter-architecture scale.
- **Section-break rhythm.** Twelve section-breaks distribute the chapter's analytical-quantitative load across distinct argumentative moves; each section makes a substantive contribution. Reader reads as well-architected chapter-architecture.
- **Cumulative-cadence work post-Phase-C-β.** F-V1 (line 12 five-fold "Price the X" → colon-list) + F-V2 (line 176 six-fold "Different X / The same X" → one analytical sentence) + F-V3 (chapter-wide em-dash sweep 80 → 28; substantial cadence-density reduction) + F-V4 (five-fold "I'll" → retain one + convert four to third-person) + F-V13 (line 60 appositive-pair em-dashes → colons; preserve three-fold anaphora) all integrated cleanly. What remains reads as substantively-earned analytical-thesis-cadence; this reader recognizes the eight-component-walk + cross-case-pattern + misreading-defense + brief-extrapolation architecture as appropriate cadence-as-content discipline.
- **Chapter-closer at lines 230–240** (book-arc forward-pointer "Chapter 1 through Chapter 8 have done that. Chapter 9 sketches the direction... Chapter 10 closes with the miner, the waterman, and the off-world administrator recognizing each other across the distance the mechanism was designed to maintain") reads as earned rhetorical-pivot. F-V9 held per substance-drives-length.
- **Black-American-writing-tradition passage at line 92** (Dunbar + Du Bois + Fanon + Ellison + framework-contribution closer) delivers the chapter's most rhetorically-ambitious single passage with precision this reader values. The four-author parallel-citation + framework-contribution closer reads as lineage-honoring rather than lineage-appropriating.

**What flags.**
- **Em-dash count post-sweep = 28** (down from 80 pre-sweep). For an analytical-prose calibrator reading post-em-dash-discipline-ratified-2026-05-21, 28 em-dashes in 243 lines = roughly one em-dash per 8.7 lines, which is materially within disciplined-em-dash-density band. Reader reads as appropriate post-discipline cadence.
- **Cumulative anaphoric cadence at chapter-architecture level (F-V5 + F-V8 + F-V9 + F-V11 all held).** Section-header parallelism (8 of 14 in "[Adj] [Noun] Cost" pattern); YIMBY-engagement self-reference density; closing-section short-declarative cluster; three-misreading paragraph-opener anaphora. Reader registers cumulative pattern but reads as substantively-earned analytical-architecture rather than as LLM-cadence reach.

**Verdict: ✓✓ INCLUDE.** Chapter delivers analytical-prose discipline + chapter-architecture + voice register coherence + post-Phase-C-β cumulative cadence as content. Pass 3.2 voice-polish work strengthened the cadence picture cleanly; what remains reads as earned.

---

#### 15. Quantitative-policy reader (general)

**Profile.** Reads for quantitative-rigor signals across the chapter; per-ton arithmetic; cross-case parameter-range defensibility; IPG construction methodology.

**What lands.**
- All Pass-3.1 Phase-C precision spot-fixes integrated cleanly (see character #4 climate-economics quant reader for details). The eight-component arithmetic + IPG construction + cross-case parameter-ranges all read as quantitatively-careful.
- **The "conservative throughout" methodological framing at line 28** is the chapter's central methodological-discipline move. Reader reads as deliberate floor-construction discipline.
- **Cross-corpus IPG canonical-construction at line 168** (Option D applied per commit `57575b1`) delivers the chapter's most defensible single quantitative-construction claim — explicit-range IPG ("between thirty-three and one hundred and twenty-two times") + today's-market carbon-alone-exceeds-by-3× framing. Reader reads as appropriate-uncertainty discipline.
- **Cross-case IPG sweep at line 174** (Deepwater 15-17 + Macondo additional $3-5B carbon-tail + Libby 40-80 + Baotou + Valdez) is the chapter's cross-case quantitative-consistency claim. Reader reads as carefully-bounded.

**What flags.**
- None at chapter-level. The chapter's quantitative claims pass the post-Pass-3.1 quantitative-policy reader-engagement test.

**Verdict: ✓✓ INCLUDE.** Chapter holds the general quantitative-policy reader cleanly; Phase-C work resolved the precision concerns; IPG canonical-construction at line 168 is the chapter's quantitative-rigor anchor.

---

#### 16. Tier-3 environmental-justice / frontline-community reader [NEW vs Ch 7 baseline; per Ch 8 chapter-specific tilt]

**Profile.** Environmental-justice movement scholar / activist (Bullard / Pellow / EJ Atlas tradition; frontline-community organizing tradition). Reads for whether the framework centers frontline-community cost-bearing as analytically-load-bearing rather than as illustrative-anecdote.

**What lands.**
- **McDowell County as load-bearing case throughout chapter.** All eight cost components computed against McDowell case; the chapter is structurally the McDowell-arithmetic chapter. Frontline-community reader recognizes the chapter centering one specific extraction-community at full analytical-quantitative depth.
- **Cross-case extension to additional frontline communities.** Baotou rare-earth villagers (line 174); Libby Montana asbestos community (line 174 — "W. R. Grace vermiculite mine in Libby, Montana"); Niger Delta implicit via cross-case sweep; Athabasca Chipewyan + Mikisew Cree + Fort McKay First Nations (line 178); rent-burdened households (line 178) — all named as frontline cost-bearers.
- **Lineage Labor section at lines 84–96** delivers the framework's intergenerational-frontline-cost analysis at the analytical-quantitative-arithmetic level. The "extraction did not just take the coal. It took the children's probability of a different life" framing at line 90 + the framework's contribution-closer at line 92 sit in the EJ-tradition register at full strength.
- **Black-American-writing-tradition passage at line 92** (Dunbar + Du Bois + Fanon + Ellison + framework-contribution closer) honors the literary-intellectual lineage that EJ tradition draws on; reader recognizes the cross-tradition continuity.
- **Closing rhetorical-pivot at line 238** ("The invoice is what McDowell County was paid. The severed cost is what McDowell County bore") + line 240 ("for the waterman, for the reader's own life") — names McDowell + waterman cost-bearer characters at the chapter's rhetorical close.

**What flags.**
- **EJ-tradition literature not cited explicitly.** Bullard, Pellow, EJ Atlas not named in body prose. Chapter operates at the framework-summary level; the depth-positioning relative to EJ tradition lives at Ch 5. For an EJ-movement reader who wants explicit lineage-naming in Ch 8, the absence may register as gap. Verdict still ✓✓ INCLUDE because the framework's apparatus does the work without the explicit citation; reader who knows the EJ movement recognizes the chapter as movement-aligned via concrete frontline-community centering.
- **First-person frontline-community voice absent.** Chapter is third-person expository (per cross-chapter inventory §8; Ch 9 character #13 cost-bearer reader disposition). EJ reader who wants frontline-community voice in Ch 8 won't find it; they'll find their experience treated as the framework's central analytical concern. This is the structurally-correct chapter-register choice (Ch 8 is analytical-quantitative-arithmetic; first-person belongs in Ch 1 / Ch 3 / Ch 10).

**Verdict: ✓✓ INCLUDE.** Chapter centers McDowell County + cross-case extension to multiple frontline communities + Lineage Labor intergenerational-cost analysis + Black-American-writing-tradition lineage + chapter-closing cost-bearer rhetorical pivot. Framework reads as movement-aligned even without explicit EJ-literature citation; cross-chapter scope-distribution carries the EJ-lineage depth at Ch 5.

---

#### 17. McDowell County / Appalachian extraction-community-resonant reader [Ch-8-SHARPENED]

**Profile.** Rural-resource-extraction-community-resonant; reads whether the chapter's deep engagement with McDowell County lands as honest material-constraint-accounting or as appropriative-rhetorical-leverage. This is the chapter's most stakes-loaded Tier 3 character — Ch 8 is THE McDowell chapter; the framework's central-arithmetic claim is computed against McDowell.

**What lands.**
- **Kennedy 1960 anchor at line 24.** "Return to McDowell County. Return to the county Kennedy visited in 1960, the county that produced more coal than any other in the United States while its residents queued for surplus food." Kennedy's 1960 visit to McDowell County (April 1960, during the West Virginia primary) is historical-record. The "queued for surplus food" framing is substantively accurate against the historical record (the McDowell County food-distribution program was central to Kennedy's 1960 hunger-witness moment). Appalachian-resonant reader recognizes the framing as honest-historical-record rather than as poverty-tourism.
- **County-population collapse arithmetic at line 58.** Population peaked at ~100K in 1950; down to ~20K by 2020; mechanization cut workforce by more than half within a decade; U.S. Steel mine closure 1986 → personal income dropped by two-thirds in single year; 2016 last Walmart left; 2022 sixteenth-poorest county; median household income $28K vs national $67K; poverty rate ~38%; 2015 highest drug-induced death rate (141 per 100K). All figures are substantively accurate against published record (Census + ACS + BEA + CDC NCHS data). Reader recognizes the framing as honest-quantitative-record rather than as exploitative-statistics.
- **Lineage Labor section at lines 84–96** centers McDowell-specific intergenerational-cost dynamic ("the children who stay grow up in a food desert where the nearest grocery store is an hour away and the local school's graduation rate is among the lowest in the country"; Opportunity Insights mobility-data anchor). Reader recognizes the specific-place-grounded analysis.
- **Political Capture section at lines 112–122** centers McDowell-specific architecture-shaping by specific actors ("coal-industry political-economic actors (operators, absentee-mineral-rights holders, industry trade associations) whose lobbying expenditure at the West Virginia statehouse and at successive federal regulatory bodies is a multi-generational matter of public record"). Reader recognizes the chapter naming the specific political-economic actors who shaped McDowell's specific outcome.
- **Chapter-closer at lines 236–240** ("The invoice is what McDowell County was paid. The severed cost is what McDowell County bore. The next two chapters return to what that means, for McDowell County, for the waterman, for the reader's own life, and for the century ahead") names McDowell at the chapter's rhetorical peak as cost-bearer and forward-pointer to subsequent chapters. Reader reads as the chapter committing to continued McDowell engagement across the book.
- **Black-American-writing-tradition passage at line 92** + the Dunbar "We Wear the Mask" anchor connects McDowell to a broader American-extraction-community lineage. Reader recognizes the framing as solidarity-affirming rather than as universalist-effacing.

**What flags.**
- **McDowell as analytical-apparatus subject.** Chapter operates on McDowell case at analytical-quantitative depth; McDowell residents do not speak in the chapter. Per cross-chapter inventory + Ch 9 character #13 disposition, this is structurally-correct (Ch 8 is the analytical-quantitative-arithmetic chapter; Ch 3 + Ch 10 carry first-person voice). McDowell-resonant reader who wants Appalachian-voice in Ch 8 won't find it; they'll find their county centered at the framework's central-arithmetic claim. Reader who knows the book's register-architecture reads the framework's analytical-quantitative engagement as the appropriate Ch-8 register.

**Verdict: ✓✓✓ INCLUDE.** Chapter is the strongest single-chapter engagement with McDowell County in the book — Kennedy 1960 anchor + county-population collapse arithmetic + Lineage Labor section + Political Capture-shaped-by-specific-actors framing + chapter-closer naming-McDowell-at-rhetorical-peak + Black-American-writing-tradition solidarity-affirming framing all deliver at strong strength. Reference-mode use is honest material-constraint-accounting; not appropriative; chapter's analytical-quantitative depth honors McDowell as load-bearing case.

---

#### 18. Tier-3 sustainable-finance / ESG practitioner reader

**Profile.** Reads chapter for whether the framework will give them analytical tools for cost-severance accounting in portfolio construction (Larry-Fink-letter-era institutional investor; Bloomberg ESG analyst; Morningstar Sustainability rater).

**What lands.**
- **Carbon-arithmetic + SCC anchor + IPG construction.** Reader recognizes the framework as one that provides analytical tools for evaluating extractive-industry portfolio exposure at the cost-severance accounting level.
- **Asset-class-consolidation framing at line 188** (institutional landlords + financialization of single-family rental + pricing-coordination patterns + DOJ investigation since 2022) names ESG-screen-failure mode this reader tracks at depth. Reader reads as the chapter naming the simulated-reattachment dynamic that ESG screens often fail to address.
- **Chapter-handoff to Ch 9 at line 234** signals the policy-architecture work this reader needs for portfolio-construction discipline is forthcoming at the analytical chapters.
- **Cross-resource framework-applicability** (coal + oil + bitumen + rare earths + housing) gives ESG reader cross-portfolio analytical applicability.

**What flags.**
- Chapter doesn't develop sustainable-finance instrument design directly. Cross-chapter scope-distribution; held (Ch 9 carries the policy-instrument-design at depth).

**Verdict: ✓✓ INCLUDE.** Chapter delivers cost-severance accounting tools + asset-class-consolidation framing + cross-resource framework-applicability + Ch-9-handoff for sustainable-finance practitioner.

---

#### 19. Tier-3 fiscal-conservative budget-hawk reader

**Profile.** Tax-burden analyst that doesn't default to tax-and-spend; reader who is wary of agenda-laden policy framing; framework that takes fiscal-discipline questions seriously.

**What lands.**
- **The framework operates at structural-accounting level, not at policy-prescription level.** The chapter's misreading-defenses at lines 196–206 explicitly disclaim policy-prescription scope. Reader reads as appropriate analytical-scope-discipline.
- **The conservative-throughout methodological-discipline at line 28** is the chapter's central audience-management move for this reader as well. Floor-construction + lower-bound estimates + omit-contested-externalities discipline reads as appropriate fiscal-discipline approach.
- **The market-is-not-fake misreading-defense at lines 202–204** refuses cheap anti-market framing; reader recognizes the chapter operating within market-economics.
- **The 2008 financial crisis policy-choice framing at line 192** ("the choice produced a particular distribution of the crisis's costs between bank balance sheets and household balance sheets") reads as a structural-policy-choice analysis without explicit redistribution-advocacy.

**What flags.**
- **Political Capture section + lobbying expenditure framing** reads as left-resonant for some fiscal-conservative subgroups; balanced by the Public Choice citation at line 122 + rent-seeking-tradition acknowledgment.
- **Civilizational-scale extrapolation at line 214** ($10-15T annual) may register as scale-aggressive for some fiscal-conservative subgroups; the chapter's own scope-discipline ("a gestured claim") names the limit.

**Verdict: ✓ INCLUDE.** Chapter holds fiscal-conservative budget-hawk through close; conservative-throughout methodological-discipline + market-is-not-fake + Public Choice citation + structural-policy-choice framing earn the reader.

---

#### 20. Tier-3 mainstream / Coasean economist (devil's advocate)

**Profile.** Orthodox-econ / Coasean reader who'll push hardest on the externalities framing. Reads cost-severance as either alternative-to-Coasean (which they'll critique) or as Coasean-extension (which they may grant).

**What lands.**
- **Externality-tail framing throughout** is structurally Coasean territory (extraction-imposes-ongoing-damage-after-it-ends). The framework's treatment of externalities as priceable-via-Cost-Severance-accounting rather than as resolvable-via-bargaining is the central Coasean divergence; this reader reads as alternative-to-Coasean position rather than as endorsement.
- **The chapter's eight-component accounting** operates at the Pigouvian-externality cost-internalization register Coasean reader can translate from.
- **The methodology-not-policy framing at line 16** ("It is not, in this book, a policy recommendation. It is an accounting exercise") + the conservative-throughout floor-construction discipline at line 28 are the methodological-discipline moves this reader values.

**What flags.**
- **Chapter doesn't engage Coase by name.** Per cross-chapter scope-distribution (and per the rent-seeking-engagement workstream that closed for Ch 1 REAUDIT), this reader's full engagement-pressure-test is handled at the analytical chapters (Ch 5 + Ch 9 + Tech Appendix).
- **"Severely mispriced for a century" framing implicit in chapter's IPG arithmetic.** Coasean reader will push back ("if it were severely mispriced, why didn't Coase-style bargaining resolve it?"). The chapter's implicit response is the cost-severance structural-architecture framing at line 122 — extraction-and-cost-bearing has structural arrangements (geographic distance, informational asymmetry, power asymmetry per Ch 7's six-pattern enumeration) that prevent Coasean-bargaining from operating. Coasean reader at Ch 8 reads as wait-and-see for the analytical chapters' explicit Coase-engagement.

**Verdict: ✓ INCLUDE.** Chapter holds this reader at INCLUDE through close (externality-tail framing + eight-component accounting + methodology-not-policy framing + conservative-throughout discipline all land), but with reservations awaiting analytical-chapter Coase-engagement. Verdict mirrors Ch 7 REAUDIT v3 character #20 verdict; not chapter-flaw.

---

#### 21. Tier-3 ecological-economics reader (Herman Daly / Steady-State / Donella Meadows lineage)

**Profile.** Framework's commons-pricing engagement sits directly adjacent to ecological-economics tradition.

**What lands.**
- **Foreclosure component at lines 68–80** + Temporal Displacement component at lines 128–138 deliver the chapter's most ecological-economics-tradition-aligned single-section work. The "option-value foreclosure" framing at line 76 + "value of having extracted more slowly" framing at line 134 sit in Daly steady-state-economics + Meadows limits-to-growth territory at full strength.
- **GDP-not-degrowth at line 220** is the chapter's most explicit single-paragraph engagement with ecological-economics tradition's central distributional-vs-aggregate distinction. "GDP measures market transactions, not welfare... GDP rises when the children of McDowell County develop addiction disorders and spend money on treatment. GDP does not fall when they die at fifty-eight. Honest pricing reduces GDP in the narrow technical sense while increasing welfare in every sense the measurement was meant to proxy. It shifts the composition of economic activity, not the total." This reader reads as direct ecological-economics-tradition language.
- **Leaded gasoline pattern-analogue at line 220** ("Leaded gasoline was banned and refineries reformulated; the industry did not collapse; children's cognitive outcomes improved") delivers the ecological-economics-tradition empirical-historical anchor for the honest-pricing-pattern claim.
- **Civilizational-scale extrapolation at line 214** ($10-15T annual; larger than every government subsidy program combined; "largest continuous wealth transfer in human history") sits in ecological-economics-tradition civilizational-scale-accounting register.

**What flags.**
- Chapter doesn't engage Daly / Meadows by name. Per cross-chapter scope-distribution, that's appropriate.

**Verdict: ✓✓✓ INCLUDE.** Chapter delivers ecological-economics-tradition lineage continuation + Foreclosure + Temporal Displacement + GDP-not-degrowth + civilizational-scale-accounting all at strong strength.

---

#### 22. Tier-3 anti-capital / structural-critique reader

**Profile.** Marxist / political-economy-of-capital / structural-Left intellectual reader. Reads for whether the framework names architecture-not-blame in ways compatible with structural-critique commitments.

**What lands.**
- **Eight-component cost-severance accounting at chapter-arithmetic level** delivers the structural-extraction-and-cost-bearing analysis at full quantitative depth.
- **Political Capture section at lines 112–124** + rent-seeking paragraph at line 122 names structural-architecture-shaped-by-specific-actors point that this reader carries as central. The reparations-economics citation explicitly honors this reader's tradition.
- **Asset-class-consolidation framing at line 188** delivers the financialization analysis structural-Left tradition has been pushing for; the explicit naming of institutional landlords + financialization of single-family rental + pricing-coordination patterns is the kind of empirical financialization analysis this reader values.
- **2008-financial-crisis architecture engagement at line 192** delivers structural-Left tradition's central post-2008 analytical commitment (recapitalizing-banks-rather-than-restructuring-household-debt as the policy-choice that determined the crisis's distributional outcomes). Mian & Sufi 2014 *House of Debt* citation is the canonical structural-economics academic anchor.
- **Civilizational-scale extrapolation at line 214** ($10-15T annual; "largest continuous wealth transfer in human history") delivers the structural-Left tradition's civilizational-scale-accounting claim at the framework's arithmetic register.

**What flags.**
- **Framework's-different-in-kind framing at line 122** distinguishes framework from reparations-economics; some structural-Left readers may want framework as explicit-tradition-continuation rather than as different-in-kind-instrument. **MITIGATION on page:** the framework's-contribution closer at line 122 frames the framework's analytical-quantitative-arithmetic apparatus as supplementing rather than displacing the tradition's actor-and-coalition vocabulary — the more analytically-grounded structural-Left reader reads as productive instrumental-differentiation.

**Verdict: ✓✓ INCLUDE.** Chapter's eight-component accounting + Political Capture + asset-class-consolidation + 2008-architecture engagement + civilizational-scale extrapolation all land for this reader.

---

#### 23. Tier-3 Hayekian / Austrian-school economist (knowledge-problem reader)

**Profile.** Reads framework's structural-architecture analysis through Hayekian distributed-knowledge lens.

**What lands.**
- **Conservative-throughout methodological-discipline at line 28** is exactly the calibrated-instrument framing Hayekian reader values — the framework uses lower-bound estimates and omits contested externalities to construct a defensible floor.
- **The market-is-not-fake misreading-defense at lines 202–204** reads as the framework recognizing where market-discovery operates correctly; the framework's role is to identify structural-prevention of price-discovery (the eight cost-severance mechanisms), not to substitute centralized planning for market-discovery.
- **Six-pattern cost-severance mechanism framing (implicit via Ch 7 cross-chapter inventory; explicit in Ch 8's per-component walk)** reads as architecture-not-intention; this reader values structural-explanations over actor-intention-explanations.
- **Knowledge and Cultural Cost section at lines 100–108** ("Replacement cost for the civic infrastructure of a community of a hundred thousand people is not straightforwardly priced, but it is certainly not zero") sits in Hayekian distributed-knowledge-problem territory — the knowledge embedded in specific communities is non-fungible and not market-pricable when the communities disperse.

**What flags.**
- Some Hayekian readers will push on the cost-severance-architecture-naming as government-knows-better-than-market framing. **MITIGATION on page:** the chapter's parameter-sensitivity discipline + conservative-throughout methodology + market-is-not-fake misreading-defense + methodology-not-policy framing at line 16 all collectively earn the reader.

**Verdict: ✓✓ INCLUDE.** Chapter delivers calibrated-instrument framing + Knowledge and Cultural Cost distributed-knowledge analysis + market-is-not-fake + conservative-throughout + methodology-not-policy framing all land for Hayekian reader.

---

#### 24. Tier-3 civic-republican / political-philosophy reader (Pettit / Skinner / Pocock tradition)

**Profile.** Reads for compatibility between the framework's structural-architecture framing and civic-republican freedom-as-non-domination commitments.

**What lands.**
- **Cost-bearing-by-parties-who-had-no-say framing at line 16** ("What gets built from visibility is the work of policy-makers, communities, and political coalitions") is structurally civic-republican democratic-deliberation framing.
- **The "second transaction... unpriced, unwitnessed, and binding on parties who were never consulted" framing at line 202** is direct civic-republican non-domination concern in plain language. The "binding on parties who were never consulted" is the most explicit non-domination-vocabulary moment in the chapter.
- **Lineage Labor section** + the "children's probability of a different life" framing centers structural-non-domination-failure at the intergenerational scale.
- **Consultation-and-consent-failures framing at line 178** (First Nations + Treaty 8) names non-domination failure at the Indigenous-rights register explicitly.
- **The question-the-framework-asks framing at line 200** ("The question is who paid for it and whether they consented") is the chapter's most direct civic-republican consent-and-cost-bearing framing.

**What flags.**
- Chapter doesn't engage Pettit / Skinner by name. Per Ch 7 cousin disposition (Ch 5 develops civic-republican lineage explicitly), cross-chapter scope-distribution is appropriate.

**Verdict: ✓✓ INCLUDE.** Architecture-not-blame framing + "binding-on-parties-who-were-never-consulted" + "who paid for it and whether they consented" + consultation-and-consent-failures naming all land cleanly for civic-republican reader.

---

#### 25. Tier-3 corporate / regulatory / fiduciary-duty lawyer (CSR / ESG / corporate-governance lawyer cluster)

**Profile.** Reads framework's accountability-bond-instruments as potential legal architecture; reads chapter for signals about how the book will frame enforceability + relationship to existing fiduciary-duty doctrine.

**What lands.**
- **Cost-severance-as-structural-arrangement framing throughout** maps to legal-architecture territory.
- **Reclamation-bond example at line 48** (1977 SMCRA + 3.5-6 billion dollar gap) is direct legal-architecture territory (existing legal instrument that partially internalized cost; chapter explicitly names where the legal instrument's parameter-design left gap).
- **DOJ-investigation framing at line 188** (property-management-software pricing-coordination patterns; antitrust law territory) names current enforcement landscape this reader tracks.
- **Chapter-handoff to Ch 9 at line 234** signals legal-architecture work is handled at the analytical-chapter depth.

**What flags.**
- Chapter doesn't develop bond-instrument legal architecture in detail. Ch 9 carries the legal-architecture work at depth. Hold — cross-chapter scope-distribution is appropriate.

**Verdict: ✓✓ INCLUDE.** Cost-severance-architecture + reclamation-bond legal-example + DOJ-investigation enforcement framing + Ch-9-handoff all deliver for this reader.

---

#### 26. Tier-3 policy think-tank fellow (composite: Brookings / Urban / AEI / Cato / RFF / Manhattan Institute)

**Profile.** Reads chapter as work-product-sample for policy-paper-writer audience. Subgroups react differently to specific framings.

**What lands.**
- All subgroups: conservative-throughout methodological-discipline + eight-component arithmetic + IPG construction + methodology-not-policy disclaimer all land for the methodological-discipline signals these subgroups recognize.
- Center-left subgroups (Brookings; Urban; RFF; Hewlett-supported research): Political Capture section + reparations-economics citation + Black-American-writing-tradition + asset-class-consolidation + 2008-architecture engagement all land cleanly.
- Center-right subgroups (AEI; Manhattan Institute energy-fellow track; RFF energy track): conservative-throughout discipline + market-is-not-fake misreading-defense + Public Choice citation + both/and YIMBY synthesis earn good faith.
- Libertarian subgroups (Cato): conservative-throughout discipline + market-is-not-fake + Public Choice citation + asset-class-consolidation framing earn engagement (lighter than for center-left subgroups but still INCLUDE).

**What flags.**
- Some center-right and libertarian subgroups will read Political Capture cluster as left-resonant; held at INCLUDE per the broader audience-management work the chapter does.

**Verdict: ✓✓ INCLUDE** (aggregate across subgroups). Some subgroup variation but no EXCLUDE.

---

#### 27. Tier-3 foundation / philanthropy program officer (Ford / Hewlett / Robert Wood Johnson / Mott)

**Profile.** Reads chapter for whether the framework will be funder-adoptable + evidence-architecture credibility.

**What lands.**
- Chapter's methodological-discipline + conservative-throughout floor-construction + cross-case parameter-range defensibility + 2008-architecture academic-grounded engagement all read as evidence-architecture credible for grant-eligible work.
- Cost-severance-as-structural-arrangement framing is consonant with foundation-grant-priorities around structural-economic-research.
- Chapter's methodology-not-policy framing at line 16 + misreading-defenses at lines 196–206 read as the kind of disciplined-analytical-position foundations support.

**What flags.**
- None substantive at chapter level.

**Verdict: ✓✓ INCLUDE.** Chapter delivers funder-adoptable analytical-rigor + scope-discipline + evidence-architecture credibility.

---

#### 28. Tier-3 general working-class reader

**Profile.** No PhD; no journal-paper-reading habit; accessibility check. The book's commercial reach depends on this reader.

**What lands.**
- **Chapter-opening question at line 10** ("What if everything cost what it actually costs?") is direct + accessible.
- **McDowell County concrete anchoring** throughout chapter centers a specific working-class extraction-community at the framework's central case.
- **The $4-5 vs $524 ratio** is the chapter's central rhetorical-payoff in plain numerical terms.
- **GDP-not-degrowth at line 220** ("GDP rises when the children of McDowell County develop addiction disorders and spend money on treatment. GDP does not fall when they die at fifty-eight") is the chapter's most accessible single-paragraph response to the "you're against growth" reflex; working-class reader reads as substantively right.
- **Three misreading-defenses at lines 196–206** preempt the working-class reader's most likely "but what about X" objections in plain language.

**What flags.**
- **Carbon arithmetic at line 72** is the chapter's heaviest single technical-passage (EPA AP-42 §1.1 + 93.28 kg + mmBtu + Rennert et al. 2022). Working-class reader may skim this section. **MITIGATION on page:** the paragraph closes with the plain-language load-bearing dollar figure ("approximately five hundred and ten dollars"); even skimming, reader gets the framework's central arithmetic.
- **Density overall.** 243 lines is a substantial chapter; this reader may not read every section in detail. Chapter-architecture (twelve section-breaks; clear section-titles per F-V5 held parallel) helps with selective reading.

**Verdict: ✓✓ INCLUDE.** Chapter delivers plain-language opening + McDowell concrete anchoring + $4-5-vs-$524 ratio + GDP-not-degrowth + misreading-defenses. Density at line 72 is the principal accessibility-concern; chapter-architecture and closing-sentence translation discipline absorb the concern.

---

## §4. Cross-character pattern observations

### §4.1 Political Capture cluster as left-coded-vs-public-choice-honoring close-vs-skim divergence

The most substantive cross-character pattern observation parallel to Ch 7's Mars-canonization concern at character #17: Ch 8's Political Capture section + asset-class-consolidation framing + DOJ-investigation framing + 2008-architecture engagement form a cluster that, read in skim, could register as left-coded for reflexively-skeptical center-right reader (#3) + libertarian subgroups (#26 Cato) + fiscal-conservative budget-hawk reader (#19). Close-read of the rent-seeking paragraph at line 122 (Public Choice tradition explicitly cited; framework's-different-in-kind asymmetric framing) absorbs the political-coding into honoring-both-traditions frame. Dual-audience test holds at close-read; skim-read carries a bounded discount.

**This is the chapter's principal close-vs-skim divergence for acceptance-test characters.** The rent-seeking paragraph at line 122 is doing the work of honoring Public Choice while computing the cost-bearing-magnitudes; it sits structurally inside the Political Capture section as the chapter's central audience-management move for the cluster.

**Three options for author consideration at Phase C-γ:**
- **Option A — hold current state.** Substantively earned at the Political Capture section's analytical position; chapter's close-read holds the reader at INCLUDE; skim-read carries a bounded discount. This option keeps the chapter's current structure.
- **Option B — add a brief pre-position note in the chapter-opener (lines 14–18) that previews the Public Choice + reparations-economics + framework's-different-in-kind framing.** Light touch; could be one or two sentences signaling the cross-tradition-engagement disciplined-asymmetric framing the chapter operates within. Reduces skim-read risk for center-right reflexively-skeptical subgroup without disturbing the chapter's analytical architecture.
- **Option C — relocate the rent-seeking paragraph to a more prominent position (e.g., as a standalone section just after the §"The coal, again" anchor at line 22, before the eight-component walk begins).** Heavier touch; reorders the chapter's narrative architecture; would require care to preserve the chapter's existing arithmetic-cadence.

**Recommendation:** Author-judgment item. Option A is fully defensible (chapter holds at close-read; INCLUDE verdict holds; skim-read discount is bounded). Option B is the lightest available reduction in skim-read risk if the author wants to address the concern. Option C is heavier and would disrupt the chapter's arithmetic-cadence architecture. **Default recommendation: Option A (hold)** — the chapter's close-read holds; the skim-read discount is bounded; the chapter's analytical architecture (eight-component walk → cross-case pattern → misreading-defenses → brief-extrapolation → close) is well-earned and reordering it for skim-read accommodation would impose costs disproportionate to the benefit.

### §4.2 The both/and YIMBY synthesis as audience-management asset

The YIMBY-engagement passage at lines 180–190 is the chapter's most extensive substantive engagement with a non-natural-fit policy position. Across the 28-character acceptance set, the both/and synthesis lands as:

- **Strongly positive:** housing-economics reader (#11; explicit substantive engagement at full steelman strength); trade-press editor (#1; analytical-honesty signal); left-policy reader (#8; rent-extraction analysis at empirical-policy level); civic-republican reader (#24; non-domination architecture analysis); ecological-economics reader (#21; structural-economic-pattern analysis).
- **Neutral-positive:** center-right reader (#3; recognizes the substantive engagement with center-right-resonant position; reads as analytical-honesty); fiscal-conservative reader (#19; YIMBY-position-recognition).
- **No characters register as negative.** The both/and synthesis is the chapter's strongest single audience-management move across the acceptance set.

**Verdict: chapter's both/and YIMBY synthesis is doing substantial cross-character work; no spot-fix warranted.**

### §4.3 Black-American-writing-tradition passage as lineage-honoring asset

The passage at line 92 (Dunbar + Du Bois + Fanon + Ellison + framework-contribution closer) lands across the acceptance set as:

- **Strongly positive:** reparations-economics reader (#9; lineage-honoring); left-policy reader (#8; intellectual-tradition reach); EJ / frontline-community reader (#16; lineage-affirming); McDowell-resonant reader (#17; solidarity-affirming-cross-tradition); literary reader (#14; precision + rhetorical work); anti-capital reader (#22; tradition-continuity); civic-republican reader (#24; freedom-as-non-domination intellectual lineage).
- **Neutral-positive (no engagement concerns):** all other characters across the set.
- **No characters register as negative.**

**Verdict: chapter's Black-American-writing-tradition passage delivers lineage-honoring at strong strength across the acceptance set; no spot-fix warranted.**

### §4.4 Sample-chapter readiness

Per workstream handoff, Ch 8 is a sample-chapter candidate alongside Ch 5 + Ch 7 for agent / publisher queries. The sample-chapter readiness assessment:

- **Literary agent (#5):** ✓✓ INCLUDE — sample-chapter-ready; comp-shelf placement; subsidiary-rights potential.
- **Trade publisher acquisitions editor (#6):** ✓✓ INCLUDE — sample-chapter-ready; reader-trust foundation across 243 lines; commercial-arc signal.
- **Venue editor for derivative works (#7):** ✓✓✓ INCLUDE (BR + PW analytical-policy derivative pipelines strongly served).
- **Trade-press editor (#1):** ✓✓ INCLUDE — analytical-quantitative-prose register reads as comp-shelf-ready.

**Sample-chapter readiness: STRONG.** All four publishing-pipeline-relevant characters return INCLUDE. The chapter's load-bearing role as the framework's central-arithmetic chapter (the IPG-arithmetic chapter; the McDowell-case chapter; the chapter that delivers the framework's central rhetorical-arithmetic promise) makes Ch 8 distinctively valuable for sample-chapter packaging.

### §4.5 Cumulative-cadence-density (per Pass 3.2 §7 cumulative-anaphora-cluster diagnostic)

Per Pass 3.2 §7, the chapter's cumulative-anaphora-cluster (F-V5 + F-V8 + F-V9 + F-V11 + F-V18 all held-as-substantively-earned at Pass 3.2 ratification) was flagged for Pass 3.3 audience-load testing. The Pass 3.3 reading:

- **Trade-press editor (#1):** reads cumulative cadence as analytical-uniformity-enacted (the framework IS the same instrument across cost components; the cadence enacts the eight-component-walk discipline).
- **Literary reader (#14; analytical-prose calibrator):** reads cadence as substantively-earned analytical-thesis-cadence; Phase C-β work on F-V1 + F-V2 + F-V3 + F-V4 + F-V13 dropped the highest-density patterns; what remains reads as content-justified.
- **Climate-economics reader (#4 + #12):** reads cadence as apparatus-development-enacted; the parallel form makes the framework's arithmetic legible.
- **Layman-but-engaged reader (#2):** does not register cadence as crutch; reads as analytical-rhythm appropriate to the chapter's framework-arithmetic walkthrough.
- **All other acceptance characters:** no cadence-related concerns surface.

**Verdict: cumulative cadence reads as analytical-thesis-cadence at the acceptance-character level.** Pass 3.2 voice-polish ratification's substance-drives-length + cadence-as-content discipline holds at Pass 3.3 audience-load level. No further spot-fix warranted.

### §4.6 First-person register-architecture (per Pass 3.2 F-V4 + F-V10 dispositions)

Per Pass 3.2 §10.1, F-V4 Option B (retain one strong site at line 96 + convert four to third-person) + F-V10 Option C (retain first-person at line 222 + vary structure) were applied. The Pass 3.3 reading:

- **Trade-press editor (#1):** reads retained first-person sites (lines 96 + 138 + 222) as deliberate authorial-discipline-naming moments rather than as register-drift. The chapter's dominant analytical-third-person voice + deliberate first-person punctuation reads as authorial-architecture rather than as inconsistent-treatment.
- **Layman-but-engaged reader (#2):** experiences the first-person moments as scope-limit-statements that build trust (e.g., line 222 "So I am not going to compress it; I will name the figure and leave it there" is the chapter's most direct scope-discipline statement).
- **Literary reader (#14):** reads first-person retention as appropriate-cadence-variation; the four-fold-conversion-to-third-person + one-fold-retention pattern reads as deliberate authorial architecture.
- **All other acceptance characters:** no register-architecture concerns surface.

**Verdict: post-Phase-C-β first-person register-architecture is acceptance-test-clean.** Pass 3.2 F-V4 Option B + F-V10 Option C dispositions read as audience-load-clean.

### §4.7 Arithmetic backbone as central rhetorical instrument

The chapter's arithmetic backbone (eight cost components priced at conservative-floor; summed transparently; IPG ratio computed; cross-case extension; civilizational-scale extrapolation with explicit scope-discipline) is the chapter's central rhetorical instrument. Across the 28-character acceptance set, the arithmetic-backbone-as-central-instrument lands as:

- **Strongly positive:** climate-economics quant reader (#4; SCC anchor + EPA chronology + Rennert citation + cross-case IPG); general quantitative-policy reader (#15; conservative-throughout + cross-corpus IPG canonical-construction); layman-but-engaged reader (#2; bullet-list-sum + IPG ratio at plain-language register); McDowell-resonant reader (#17; county-collapse arithmetic + Lineage Labor + chapter-closer); left-policy reader (#8); reparations-economics reader (#9); housing-economics reader (#11); climate-policy reader (#12); First-Nations reader (#13); ecological-economics reader (#21); ESG practitioner (#18); foundation officer (#27).
- **Neutral-positive:** center-right reader (#3; conservative-throughout + market-is-not-fake earn the reader); fiscal-conservative reader (#19; conservative-throughout + structural-accounting); Coasean reader (#20; externality-tail framing); Hayekian reader (#23); civic-republican reader (#24); corporate-law reader (#25); think-tank fellow (#26); literary agent (#5); acquisitions editor (#6); venue editor (#7); trade-press editor (#1); literary reader (#14); EJ reader (#16); anti-capital reader (#22); Public Choice reader (#10); general working-class reader (#28).
- **No characters register the arithmetic-backbone as negative.**

**Verdict: arithmetic-backbone-as-central-rhetorical-instrument is the chapter's strongest cross-character asset; no spot-fix warranted.** The chapter's central rhetorical-arithmetic promise (the $4-5 vs $524 gap) lands across the full acceptance set.

---

## §5. Apparatus / consistency / named-subject sub-checks

### §5.1 Apparatus register canonical decisions — ✓ HOLDS

Verified post-Phase-C-β chapter state honors all canonical apparatus register decisions (per `tools/rigor-passes/commons_bonds_rigor_pass_2026-05-11_apparatus_register_decision_v1.0.0.md`):

- **Item 1 — inline-integral strip from Ch 8 body prose:** Chapter contains no Greek letters, no integrals, no formal-definitional integrals in body prose. The only quantitative-apparatus residue is at line 72 ("EPA AP-42 §1.1 bituminous-coal combustion factor of 93.28 kg CO₂ per mmBtu" + "2.61 metric tons CO₂ per short ton" + "$190 per metric ton" SCC) — all within permitted analytical-quantitative register (engineering / climate-economics arithmetic, not framework-formal-apparatus). ✓ Item 1 honored.
- **Item 13 — IPG full-name + acronym:** Chapter line 168 uses "The Intergenerational Pricing Gap — the ratio of honest price to market price — for McDowell County coal sits somewhere between thirty-three and one hundred and twenty-two times the 1960 sale price" + line 174 uses "IPG" (acronym after first-introduction). ✓ Item 13 honored (Sandel-hybrid: working definition precedes formal naming; acronym used in subsequent dense-context per Item 13 discipline).
- **Item 14 — Cᵢ via Four Gates:** Chapter line 18 uses "every Cᵢ that passes the discipline of the Commons Inversion Test, units consistency, boundedness, and independence" — Cᵢ subscript appears with full-name expansion + Four-Gates context. ✓ Item 14 honored.
- **Apparatus residue chapter-wide:** No additional Greek letters / formal subscripts / integrals beyond the Item 14 Cᵢ + the Item 1 permitted analytical-quantitative engineering arithmetic at line 72. ✓ Clean.

### §5.2 Cross-corpus IPG canonical-construction (commit `57575b1` Option D) — ✓ HOLDS

Verified post-Phase-C chapter state honors Option D disposition:
- **Line 168 IPG ratio:** "between thirty-three and one hundred and twenty-two times the 1960 sale price" + "even at today's higher market prices ($40 to $140 per ton depending on grade), the carbon term alone exceeds the market price by a factor of at least three." ✓ Option D explicit-range + today's-market carbon-alone-exceeds-by-3× framing intact.
- **Line 166 market-price band:** "$40 to $140 today depending on grade" + "Against a 1960 market price of four to five dollars" + "$40 to $140 today depending on grade, and against every price coal has ever sold for." ✓ Cross-chapter price-band canonical phrasing intact.
- **Cross-corpus consistency:** Ch 2 + Ch 6 + Ch 8 IPG construction uses Option D canonical phrasing per `57575b1` ratification.

### §5.3 Coal-CO₂ McDowell-specific cascade-reconciliation (commit `9befb92`) — ✓ HOLDS

Verified post-Phase-C chapter state honors `9befb92` cascade-reconciliation:
- **Line 72 McDowell-specific calibration intact:** "the McDowell-specific calibration of the framework figure Chapter 6 introduced under the national-bituminous-average heat content, which yields 2.32 metric tons CO₂ per short ton" — explicit reconciliation of McDowell-specific 2.61 figure with Ch 6 framework-level 2.32 national-average figure. ✓ Cross-chapter methodological-consistency intact.
- **Line 40 conservative-arithmetic framing intact** per cascade-reconciliation hedge-alignment.
- **Line 52 conservative-allocation framing intact** per cascade-reconciliation.
- **Line 166 market-price band intact** per cascade-reconciliation.
- **Line 238 chapter-closer "five hundred and twenty-four dollars" intact** per cascade-reconciliation.

### §5.4 Rent-seeking paragraph (line 122) — ✓ HONORED + ✓ ASYMMETRIC FRAMING CROSS-CHAPTER CONSISTENT

Verified per Pass 3.2 F-V12 ✓ HOLDS disposition + cross-chapter cascade resolution at `cbef9bd` (Ch 8 Stage 1c Phase C Option A):
- Chapter line 122 retains: reparations-economics tradition (Coates, Darity, Mullen, Hamilton, Conley) explicit citation ✓ + Public Choice tradition (Buchanan, Tullock) explicit citation ✓ + framework's-different-in-kind asymmetric framing ("the ledger that counts what those traditions described has been costing, and to whom") ✓ + cross-chapter forward-reference to Ch 9 ("Chapter 9 develops the framework-Public-Choice relationship at greater length") ✓.
- Asymmetric framing matches Ch 9 Reading C v3 framework-as-measurement-AND-decision-tool framing post-`cbef9bd` cascade resolution. Reader proceeding Ch 8 → Ch 9 experiences continuous asymmetric framing.
- No Pass 3.3 spot-fix recommendation would modify the rent-seeking paragraph at line 122.

### §5.5 Named-subject discipline — ✓ HOLDS

Chapter cites the following named individuals; all classified per `feedback_named_subject_consent.md`:

- **John F. Kennedy** (line 24, 58 — implicit via "Kennedy's visit"): Historical figure (1917–1963); historical-record discipline; not consent-gating. 1960 visit to McDowell County is public-record (April 1960 West Virginia primary; well-documented).
- **John L. Lewis** (line 116): Historical figure (1880–1969); historical-record discipline; not consent-gating. UMW leadership + black-lung-policy positions are public-record.
- **Paul Laurence Dunbar** (line 92): Historical figure (1872–1906); historical-record discipline; not consent-gating. *We Wear the Mask* (1896) is canonical published work.
- **W. E. B. Du Bois** (line 92): Historical figure (1868–1963); historical-record discipline; not consent-gating. *The Souls of Black Folk* (1903) is canonical published work.
- **Frantz Fanon** (line 92): Historical figure (1925–1961); historical-record discipline; not consent-gating. *Black Skin, White Masks* (1952) is canonical published work.
- **Ralph Ellison** (line 92): Historical figure (1914–1994); historical-record discipline; not consent-gating. *Invisible Man* (1952) is canonical published work.
- **Ta-Nehisi Coates** (line 122): Living scholar; public-record exception applies (citation is from on-record published work — *The Case for Reparations*, *Between the World and Me*). Courtesy notification pre-publication appropriate but not consent-gating.
- **William Darity Jr.** (line 122): Living scholar; public-record exception applies (citation is from on-record published academic work — *From Here to Equality* with Mullen). Courtesy notification pre-publication appropriate but not consent-gating.
- **A. Kirsten Mullen** (line 122): Living scholar; public-record exception applies (*From Here to Equality* with Darity). Courtesy notification pre-publication appropriate but not consent-gating.
- **Darrick Hamilton** (line 122): Living scholar; public-record exception applies (citation is from on-record published academic work — Stratification Economics). Courtesy notification pre-publication appropriate but not consent-gating.
- **Dalton Conley** (line 122): Living scholar; public-record exception applies (citation is from on-record published academic work — *Being Black, Living in the Red*). Courtesy notification pre-publication appropriate but not consent-gating.
- **James M. Buchanan** (line 122): Historical figure (1919–2013); historical-record discipline; not consent-gating. Public Choice scholarly tradition is public-record.
- **Gordon Tullock** (line 122): Historical figure (1922–2014); historical-record discipline; not consent-gating. Public Choice scholarly tradition is public-record.
- **Atif Mian + Amir Sufi** (line 192): Living scholars; public-record exception applies (citation is from on-record published academic work — *House of Debt* 2014). Courtesy notification pre-publication appropriate but not consent-gating.
- **Edward Glaeser + Joseph Gyourko + Jenny Schuetz** (line 182): Living scholars; public-record exception applies (citations are from on-record published academic work — Glaeser-Gyourko housing-supply literature; Schuetz land-use regulation literature). Courtesy notification pre-publication appropriate but not consent-gating.
- **Rennert + Errickson + Prest + Rennels et al.** (line 72 — "Rennert et al. 2022 *Nature*"): Living scholars; public-record exception applies (citation is from on-record published academic work — *Nature* 610, 2022 SCC paper). Courtesy notification pre-publication appropriate but not consent-gating.
- **Wagner + Anthoff + Cropper et al.** (line 118 — "Wagner, Anthoff, Cropper, et al. 2021"): Living scholars; public-record exception applies (citation is from on-record published academic work — 2021 SCC-methodology critique paper). Courtesy notification pre-publication appropriate but not consent-gating.

**First Nations** (line 178): Athabasca Chipewyan First Nation + Mikisew Cree First Nation + Fort McKay First Nation are institutional/governance entities (not individuals); Treaty 8 of 1899 + cancer-rate documentation + consultation-and-consent failures are public-record. Per `feedback_named_subject_consent.md` place-name + institutional-entity discipline: safe without per-person consent. Courtesy notification appropriate to relevant First Nations governance offices pre-publication.

All named-subject citations in Ch 8 fall under public-record exception (on-record published academic / cultural work + historical-record) or institutional/place-name discipline. No living-private-subject consent-gating items.

### §5.6 Voice register coherence — ✓ HOLDS

Voice register (analytical-quantitative-dominant; deliberate first-person punctuation at lines 96 + 138 + 222 per F-V4 Option B + F-V10 Option C ratification; comparative-historical brief moments at line 92 Black-American-writing-tradition passage) holds throughout per Pass 3.2 §5 verification. Pass 3.3 reading confirms register coherence at the acceptance-character level — no character flagged register-tonality concerns.

### §5.7 Path B contamination check — ✓ CLEAN

Spot-checked for verbatim from other chapters. No regression: chapter's prose is distinctively Ch 8 register (analytical-quantitative-arithmetic). No intentional cross-artifact verbatim overlaps (Ch 8 carries no Aeon-pitch-overlap-held-passage analogous to Ch 7:101).

---

## §6. Cadence / sentence-length / declarative-rhythm summary (post-Phase-C-β baseline)

Pass 3.3 reading confirms post-Phase-C-β cadence picture:

- **Sentence-length variance:** wide range (single-sentence questions at chapter-opener line 10 + line 200; multi-clause analytical-quantitative passages at line 72 + line 122 + line 178; bullet-list at lines 148–162). Reader experiences cadence-variation appropriate to the chapter's multiple registers (opening-question; eight-component-walk; cross-case-pattern; misreading-defense; brief-extrapolation; closing).
- **Anaphoric patterns:** all per-Pass-3.2-ratification held-as-substantively-earned (F-V5 section-header parallelism; F-V8 YIMBY-engagement self-reference density; F-V9 closing-section short-declarative cluster; F-V11 three-misreading paragraph-opener anaphora; F-V18 four-declarative cluster at line 200). Reader experiences as analytical-thesis-cadence rather than as LLM-cadence reach.
- **Em-dash density:** post-sweep 28 em-dashes in 243 lines (was 80 pre-sweep). Within disciplined-em-dash-density band per em-dash-discipline ratified 2026-05-21.
- **First-person register-architecture:** F-V4 Option B (retain one strong site at line 96 + convert four to third-person) + F-V10 Option C (retain first-person at line 222 + vary structure) applied; reader experiences deliberate authorial-discipline punctuation rather than register-drift.
- **Declarative-three-in-a-row patterns:** F-V18 four-declarative cluster at line 200 held; reader reads as appropriate misreading-defense cadence.

**Cadence verdict: post-Phase-C-β chapter is acceptance-test-clean at cadence level.** No further cadence-related spot-fix warranted from Pass 3.3 audience-load reading.

---

## §7. Out-of-scope-for-Pass-3.3 — flagged for Pass 3.4 (robustness) future-session input

Items observed during Pass 3.3 reading that belong to Pass 3.4 (robustness — adversarial / detractor characters) scope per per-prompt serial cadence + v3.0/v3.1 sub-pass split. NOT scored as Pass 3.3 findings. Flagged forward for Pass 3.4 session.

**Industry-funded adversarial characters to score at Pass 3.4:**

1. **Industry-funded fossil-fuel-industry economist** (Heritage / Manhattan Institute energy fellow / Texas Public Policy Foundation / American Petroleum Institute / National Mining Association). Predisposed-hostile to framework's commons-pricing application to coal/oil/gas. Will read $190/ton SCC anchor + 2.61 t-CO₂/ton coal + $510 carbon-tail per ton + IPG 33-122× + civilizational-scale $10-15T extrapolation as direct threat to fossil-industry economics. Will weaponize chapter's Political Capture section + asset-class-consolidation framing + 2008-architecture engagement against framework's policy-implications. Pass 3.4 should test thread-pull on the chapter's SCC arithmetic + IPG construction + civilizational-scale extrapolation.
2. **Industry-funded coal-industry economist** (National Mining Association; American Coal Council). Distinct adversarial position; reads chapter's McDowell-County eight-component arithmetic + Black Lung Benefits Program Trust Fund + reclamation-bond-gap + mountaintop-removal cancer-rate framing as direct threat. Pass 3.4 should test thread-pull on the chapter's component-by-component arithmetic for coal-industry defensibility.
3. **Industry-funded housing-economics economist** (American Enterprise Institute housing-policy fellow; Mercatus Center housing-policy program). Adversarial position on framework's asset-class-consolidation framing + DOJ-investigation framing + framework's claim that supply-restriction does not explain cost-burden-share-rise. Pass 3.4 should test thread-pull on the YIMBY both/and synthesis.
4. **Industry-funded financial-services economist** (American Bankers Association; Securities Industry and Financial Markets Association). Adversarial position on 2008-architecture engagement + Mian-Sufi citation + framework's policy-choice framing. Pass 3.4 should test thread-pull on the 2008-financial-crisis architecture engagement.

**Ideologically-opposed adversarial characters to score at Pass 3.4:**

5. **Public-choice theorist (Buchanan-tradition orthodox; hostile to redistributive policy implications)** (Cato / Mercatus / GMU). Cross-chapter rent-seeking-engagement workstream closed for Ch 1 REAUDIT + Ch 9 cascade-resolution at `cbef9bd`; Pass 3.4 should verify whether Ch 8's framework's-different-in-kind asymmetric framing + Political Capture cluster + asset-class-consolidation framing produces ⚠⚠ EXCLUDE in adversarial-direction read.
6. **MacLean-sympathetic Buchanan-critical adversarial reader.** Per Ch 9 character #15 carry-forward; Pass 3.4 should test whether Ch 8's Public Choice citation without explicit MacLean acknowledgment produces ⚠⚠ EXCLUDE.
7. **Pure-libertarian / Rothbardian reader** (Mises Institute / FEE / Cato-libertarian-wing). Reads framework's accountability-bond logic + Ch-9-handoff + civilizational-scale extrapolation as expanded-state-power proposal.
8. **Reactionary intellectual reader** (*National Review* / *National Affairs* / *American Affairs* reader; Niall Ferguson / Bret Stephens / Ross Douthat-cluster). Reads chapter's Political Capture cluster + Black-American-writing-tradition passage + reparations-economics citation + asset-class-consolidation framing as left-coded scholarship.
9. **Orthodox-econ reader (Chicago School; freshwater macro) — adversarial wing.** Adversarial to heterodox-econ framings + market-failure premises; reads the framework's structural-architecture analysis as displacement of property-rights-resolution-of-externalities framings.
10. **Climate-skeptical / SCC-questioning policy reader.** Adversarial to $190/ton SCC anchor as politically-driven rather than physics-driven. Reads SCC political-fight chronology + Wagner et al. 2021 critique citation as one-sided framing.

**Trade-press / commercial-adversarial characters to score at Pass 3.4:**

11. **Trade-press hostile reviewer** (NYT / WSJ / *The Atlantic* / *The New Republic* book-reviewer assigned with adversarial intent). Reads Ch 8 (if assigned as sample chapter for review) looking for threads to amplify; would weaponize Political Capture cluster + civilizational-scale extrapolation + 2008-architecture engagement against the book.
12. **Wall Street Journal editorial-board reader / business-press conservative.** Reads chapter for "this book is a threat to business interests" signals; framework-arithmetic + IPG + asset-class-consolidation + 2008-architecture engagement as preparation for business-regulation.

**Cultural-adversarial characters to score at Pass 3.4:**

13. **Tabloid / populist-skeptic reader** (NY Post / Daily Mail / Fox News op-ed-page reader). Reads chapter for populist character-attack ammunition; civilizational-scale extrapolation + GDP-not-degrowth + Political Capture cluster + asset-class-consolidation could be selectively framed as elite-academic-anti-business signaling.

**Legal-adversarial characters to score at Pass 3.4:**

14. **Tort-reform / fiduciary-protection lawyer** (defense-bar; corporate-counsel cluster). Reads framework's accountability-bond logic + Ch-9-handoff + asset-class-consolidation framing + DOJ-investigation framing as litigation-amplification threat.

**Cost-bearer-adversarial characters to score at Pass 3.4:**

15. **Adversarial-anti-pricing-as-instrumentalization cost-bearer reader.** Reads chapter's analytical-quantitative pricing of cost-bearer experience (McDowell County health + community + lineage + knowledge) as instrumentalizing cost-bearer experience for analytical purposes; adversarial to framework's "treating life-expectancy-gap as a number" framing. Pass 3.4 should test the framework's-different-in-kind asymmetric framing at line 122 against this adversarial direction.

**Pass 3.4 thread-pull synthesis (the central diagnostic):**
Pass 3.4 should produce the thread-pull synthesis table per `audience-pressure-test-construction.md` §3.4 and verify the chapter's robustness verdict (ROBUST / CONDITIONALLY ROBUST / REQUIRES STRUCTURAL ENGAGEMENT). Expected threads to track (from Pass 3.3 cross-character observations):
- Political Capture cluster as left-coded skim-read risk (already documented at §4.1).
- SCC anchor + EPA-update chronology defensibility against climate-skeptical adversarial wing.
- Asset-class-consolidation framing + DOJ-investigation framing defensibility against business-press / fiduciary-protection adversarial wings.
- YIMBY both/and synthesis defensibility against YIMBY-orthodoxy adversarial direction.
- Civilizational-scale extrapolation ($10-15T) defensibility against scale-aggressive adversarial direction.
- Black-American-writing-tradition passage + reparations-economics citation defensibility against reactionary intellectual + populist-skeptic adversarial directions.

The Pass 3.4 session should test whether these threads are (a) load-bearing chapter claims the chapter must hold its ground on or (b) procedural / cosmetic flags spot-fixable without damaging acceptance verdicts.

**Additional voice-polish concerns observed during Pass 3.3 reading (flagged for Pass 3.4 input rather than Pass 3.2 re-litigation):**
- None substantive. The cumulative cadence-cluster diagnostic from Pass 3.2 §7 resolved at the acceptance-character level (§4.5 above); Pass 3.4 should verify adversarial-character reads don't surface new cadence-related concerns.

---

## §8. Out-of-scope-for-Pass-3.3 — flagged for Pass 3.1 (fact-check) / Pass 3.2 (voice-polish) follow-up

Items observed during Pass 3.3 reading that belong to Pass 3.1 / Pass 3.2 scope.

**Pass 3.1 fact-check follow-up:** No new factual concerns surfaced during Pass 3.3 reading. Two pre-publication-refresh items previously flagged in Pass 3.1 + Pass 3.2 remain in-flight (not blocking Pass 3.3):

1. **DOJ RealPage investigation status at line 188** ("investigating since 2022"): Pass 1 LOW-6 (time-sensitive figures) flagged DOJ RealPage as moving from investigation (Nov 2022) → antitrust complaint (2024) → proposed settlement (Nov 2025). Pre-publication refresh checklist captures this; no Pass-3.3 action required.
2. **Hendryx-specific citation for 60,000 Appalachian cancer cases figure at line 50.** Optional pre-publication explicit-citation addition; not blocking; specialist-reader friction is bounded per character #4 disposition.

**Pass 3.2 voice-polish follow-up:** No new voice-polish concerns surfaced. Pass 3.2 RATIFIED 2026-05-25 + Phase C-β APPLIED at commit `16554fa`; the post-spot-fix prose is the audit baseline.

No new Pass 3.1 / Pass 3.2 concerns from Pass 3.3 reading.

---

## §9. Verdict synthesis

### §9.1 Per-character tally (acceptance set; 28 characters)

| Tier | # | Character | Pass 3.3 verdict |
|---|---|---|---|
| 1 | 1 | Trade-press editor pressure-test character | **✓✓ INCLUDE** |
| 1 | 2 | Layman-but-engaged reader | **✓✓ INCLUDE** |
| 1 | 3 | Free-market-economist / center-right policy reader | **✓✓ INCLUDE** (light discount for reflexively-skeptical subgroup; aggregate INCLUDE) |
| 1 | 4 | Tier-1 quantitative reader / climate-economics + SCC specialist [Ch-8-SHARPENED] | **✓✓ INCLUDE** |
| 1 | 5 | Literary agent (Wylie-cluster) | **✓✓ INCLUDE** |
| 2 | 6 | Trade publisher acquisitions editor | **✓✓ INCLUDE** |
| 2 | 7 | Venue editor for derivative works (Aeon / Noema / BR / PW composite) | **✓✓✓ INCLUDE** (BR + PW analytical-policy derivative pipelines strongly served) |
| 2 | 8 | Tier-1 left-policy reader | **✓✓✓ INCLUDE** |
| 2 | 9 | Reparations-economics reader (Coates/Darity/Mullen/Hamilton/Conley) | **✓✓✓ INCLUDE** |
| 2 | 10 | Public Choice reader (center-left wing — Lindsey & Teles tradition) | **✓✓ INCLUDE** |
| 2 | 11 | Housing-economics reader (Glaeser+Gyourko+Schuetz YIMBY-tradition) [Ch-8-NEW] | **✓✓ INCLUDE** |
| 2 | 12 | Climate-policy / SCC-tradition reader [Ch-8-NEW] | **✓✓✓ INCLUDE** |
| 2 | 13 | First-Nations / Indigenous-treaty reader [Ch-8-NEW] | **✓✓ INCLUDE** |
| 3 | 14 | Literary reader (analytical-prose calibrator) | **✓✓ INCLUDE** |
| 3 | 15 | Quantitative-policy reader (general) | **✓✓ INCLUDE** |
| 3 | 16 | Environmental-justice / frontline-community reader [Ch-8-NEW] | **✓✓ INCLUDE** |
| 3 | 17 | McDowell County / Appalachian extraction-community-resonant reader [Ch-8-SHARPENED] | **✓✓✓ INCLUDE** |
| 3 | 18 | ESG / sustainable-finance practitioner | **✓✓ INCLUDE** |
| 3 | 19 | Fiscal-conservative budget-hawk reader | **✓ INCLUDE** |
| 3 | 20 | Mainstream / Coasean economist (devil's advocate) | **✓ INCLUDE** |
| 3 | 21 | Ecological-economics reader (Daly/Meadows lineage) | **✓✓✓ INCLUDE** |
| 3 | 22 | Anti-capital / structural-critique reader | **✓✓ INCLUDE** |
| 3 | 23 | Hayekian / Austrian-school economist (knowledge-problem) | **✓✓ INCLUDE** |
| 3 | 24 | Civic-republican / political-philosophy reader (Pettit/Skinner-tradition) | **✓✓ INCLUDE** |
| 3 | 25 | Corporate / regulatory / fiduciary-duty lawyer | **✓✓ INCLUDE** |
| 3 | 26 | Policy think-tank fellow (composite across spectrum) | **✓✓ INCLUDE** |
| 3 | 27 | Foundation / philanthropy program officer | **✓✓ INCLUDE** |
| 3 | 28 | General working-class reader | **✓✓ INCLUDE** |

**Tally:** 28 INCLUDE / 0 NEUTRAL / 0 EXCLUDE.
**Distribution:** 6 ✓✓✓ INCLUDE; 20 ✓✓ INCLUDE; 2 ✓ INCLUDE.

**Tier-level breakdown:**
- Tier 1 (gating; 5 characters): 0 ✓✓✓ + 5 ✓✓; no EXCLUDE. All gating characters INCLUDE.
- Tier 2 (pipeline-strengthening; 8 characters): 4 ✓✓✓ + 4 ✓✓; no EXCLUDE.
- Tier 3 (cultural-resonance + accessibility + practitioner; 15 characters): 2 ✓✓✓ + 11 ✓✓ + 2 ✓; no EXCLUDE.

### §9.2 Aggregate Pass-3.3 verdict

**READY AS-IS (with one optional author-judgment item at §4.1 Option B if author wants to reduce Political-Capture-cluster skim-read risk).**

The post-Phase-C-β chapter state holds at **28 INCLUDE / 0 NEUTRAL / 0 EXCLUDE** across the full 28-character acceptance audience. All Tier-1 gating characters return INCLUDE (5/5); no Tier-1 EXCLUDE; book's commercial + policy + adoption success-criteria audiences all return INCLUDE.

The chapter delivers across:
- **Trade-press / publishing-pipeline characters** (#1, #5, #6, #7) all INCLUDE — sample-chapter-ready per §4.4.
- **Tier-1 climate-economics + SCC-literature quantitative reader** (#4) INCLUDE — all Pass 3.1 Phase-C precision spot-fixes integrated cleanly; quantitative-credibility holds; SCC anchor + EPA chronology + Rennert et al. 2022 + cross-corpus IPG canonical-construction all defensible.
- **Tier-1 center-right policy reader** (#3) INCLUDE at close-read; skim-read carries bounded ⚠ risk; rent-seeking paragraph at line 122 explicit Public Choice citation + framework's-different-in-kind asymmetric framing is the central audience-management asset.
- **Tier-1 layman-but-engaged reader** (#2) INCLUDE — chapter delivers $4-5-vs-$524 framework-arithmetic at plain-language register; misreading-defenses + GDP-not-degrowth all land.
- **Tier-2 reparations-economics + left-policy + climate-policy** readers (#8, #9, #12) all ✓✓✓ INCLUDE — chapter delivers at strong strength for the framework's natural-fit Tier-2 cluster.
- **Tier-2 housing-economics reader** (#11) INCLUDE — chapter's both/and YIMBY synthesis is the chapter's strongest single audience-management asset for a non-natural-fit policy position.
- **Tier-2 First-Nations / Indigenous-treaty reader** (#13) INCLUDE — explicit Treaty 8 of 1899 + Athabasca Chipewyan + Mikisew Cree + Fort McKay First Nations naming + documented-harm framing + cross-resource framework-applicability all deliver.
- **Tier-3 McDowell County resonant reader** (#17) ✓✓✓ INCLUDE — chapter is THE McDowell-arithmetic chapter; framework-arithmetic computed against McDowell case at strong depth.
- **Tier-3 ecological-economics + EJ + venue-editor + reparations + climate-policy** all ✓✓✓ INCLUDE.
- **All other characters across Tiers 1–3** INCLUDE without specific concern.

The two ✓ INCLUDE verdicts (fiscal-conservative budget-hawk #19; Coasean economist #20) are the lowest-confidence acceptance verdicts and reserve judgment for analytical-chapter deeper engagement; both verdicts mirror Ch 7 + Ch 9 cousin patterns for the same characters. Not chapter-flaws.

**Cross-chapter cascade resolution at commit `cbef9bd` (Ch 8 Stage 1c Phase C Option A — asymmetric rent-seeking framing alignment with Ch 9 Reading C v3)** continues to deliver value: the chapter's Ch 8:122 asymmetric framing matches Ch 9's Reading C v3 framing; reader proceeding Ch 8 → Ch 9 experiences continuous asymmetric framing across both chapters.

**Sample-chapter readiness: STRONG** (per §4.4). The chapter is publication-ready at trade-press-positioning level + at derivative-work-pipeline level (BR + PW ✓✓✓) + across the full acceptance-audience range tested. The chapter's load-bearing role as the framework's central-arithmetic chapter makes it distinctively valuable for sample-chapter packaging alongside Ch 5 + Ch 7.

### §9.3 Phase C-γ disposition recommendation

**Default recommendation: HOLD AS-IS.** Chapter holds at INCLUDE across all 28 acceptance characters; no spot-fixes required for Pass 3.3 acceptance verdict to be sustained.

**Author-judgment item for optional Phase C-γ disposition:**

| Item | Location | Disposition options | Recommendation |
|---|---|---|---|
| Political-Capture-cluster skim-read risk (§4.1) | Political Capture section + rent-seeking paragraph at line 122 | **Option A:** hold current position (substantively earned at Political Capture analytical position). **Option B:** add brief 1–2 sentence pre-positioning note in chapter-opener (lines 14–18) previewing Public Choice + reparations-economics cross-tradition engagement. **Option C:** relocate rent-seeking paragraph to a more prominent position (heavier touch; disrupts arithmetic-cadence architecture). | **Default Option A (hold)** — chapter's close-read holds; skim-read discount bounded; chapter's analytical architecture (eight-component walk → cross-case pattern → misreading-defenses → brief-extrapolation → close) well-earned. Author judgment if a lighter touch (Option B) is preferred to reduce skim-read risk for center-right reflexively-skeptical subgroup. |

**If author selects Option A:** no Phase C-γ session needed for Pass 3.3 acceptance. Chapter holds AS-IS. Pass 3.4 (robustness) is the next session for Ch 8.

**If author selects Option B:** Phase C-γ session applies a single 1–2 sentence addition in chapter's opener (lines 14–18). Minimal disturbance to chapter architecture; bounded scope. Pass 3.4 (robustness) follows Phase C-γ application.

**If author selects Option C:** Phase C-γ session is heavier (relocates the rent-seeking paragraph; reorders the chapter's narrative architecture); Pass 3.3 acceptance re-fire may be warranted before Pass 3.4 (robustness).

---

## §10. Ratification record

### §10.1 Author disposition placeholder (pending author ratification)

| Item | Severity | Disposition options | Recommendation | Author ratification |
|---|---|---|---|---|
| §9.3 Political-Capture-cluster skim-read disclaimer | Author-judgment | A / B / C | **A (HOLD)** | *(pending author ratification)* |

### §10.2 Phase C-γ application (downstream session — to be filled in post-application; only if author selects Option B or C)

- Application commit SHA: *(pending downstream Phase C-γ session, if any)*
- Chapter line-count post-application: *(pending; no change if Option A)*
- Cross-chapter cascade required: *(N if Option A; potentially Stage 1c-light if Option B touches rent-seeking-paragraph framing)*
- Pass 3.4 (robustness) session ready: **Y** (chapter holds at acceptance; Pass 3.4 may fire whether Option A held or Option B applied)

### §10.3 Next session for Ch 8

**Pass 3.4 (robustness — adversarial / detractor characters with thread-pull synthesis verdict)** is the next session for Ch 8 per per-prompt serial cadence + v3.0/v3.1 sub-pass split. 15 adversarial characters flagged forward at §7 with specific Ch-8-relevant thread expectations.

After Pass 3.4: if spot-fixes ratified (potentially combined with deferred §9.3 Option B / C disposition), Phase C-γ applies; otherwise Pass 3.5 (developmental-edit) is the explicit-gate next step if author triggers, OR Ch 8 closes Stage-3 audit and moves to Stage 4 (render + character-integrity audit) per v3.0 architecture.

---

## §11. Hard constraints honored

- ✓ Did NOT apply spot-fixes to `manuscript/chapters/Chapter__8_WhatThingsActuallyCost.md`.
- ✓ Did NOT re-run Pass 3.1 (fact-check) or Pass 3.2 (voice-polish) — both referenced only for context; no new findings re-litigated.
- ✓ Did NOT score Pass 3.4 (robustness — adversarial / detractor) — concerns flagged forward at §7 for Pass 3.4 session.
- ✓ Did NOT score Pass 3.5 (developmental-edit) — explicit-gate per Amendment A two-class cascade.
- ✓ Did NOT re-write paragraphs — verdicts + per-character analysis only.
- ✓ Did NOT contact named subjects.
- ✓ Did NOT propose new framework concepts or meta-conclusions about v3.0 / v3.1 discipline.
- ✓ Did NOT propose spot-fixes that touch the rent-seeking paragraph at line 122 (per session framing hard constraint; Pass 3.2 F-V12 ✓ HOLDS).
- ✓ Did NOT re-litigate apparatus register canonical decisions (Item 1 inline-integral strip; Item 13 IPG; Item 14 Cᵢ).
- ✓ Did NOT re-litigate cross-corpus IPG canonical-construction (commit `57575b1` Option D applied at line 168).
- ✓ Did NOT re-litigate coal-CO₂ McDowell-specific cascade-reconciliation (commit `9befb92`).
- ✓ Verified post-Phase-C-β chapter line count (243 lines, 2026-05-25) via `wc -l`.
- ✓ Verified post-Phase-C-β em-dash count (28 em-dashes) via `grep -c "—"` against current chapter file state — within disciplined post-F-V3-sweep band.
- ✓ Verified post-Phase-C-β word count (6,421 words) via `wc -w`.
- ✓ Verified commits `5fe6af6`, `275b75a`, `57575b1`, `9befb92`, `138aa7e`, `6589ca2`, `16554fa` all present on origin/main.
- ✓ Verified Pass 3.1 artifact present with ratification record.
- ✓ Verified Pass 3.2 artifact present with §10.1 ratification table (8 RATIFY APPLY + 12 RATIFY HOLD).
- ✓ Verified audience pressure-test template present at cited path.
- ✓ Verified Ch 7 + Ch 9 + Ch 4 cousin Pass 3.3 artifacts present (canonical format models).
- ✓ Verified named-subject consent discipline per §5.5 (all named individuals fall under public-record exception or historical-record; no living-private-subject consent-gating items).
- ✓ Verified apparatus register canonical decisions hold per §5.1 (Items 1, 13, 14 all honored).
- ✓ Verified cross-corpus IPG canonical-construction Option D holds per §5.2 (line 168 explicit-range + today's-market 3× framing intact).
- ✓ Verified coal-CO₂ McDowell-specific cascade-reconciliation holds per §5.3 (line 72 reconciliation + line 40 + line 52 + line 166 + line 238 all intact).
- ✓ Verified rent-seeking paragraph at line 122 + Ch 8 → Ch 9 asymmetric framing cross-chapter consistency holds per §5.4.
- ✓ Built feature branch `claude/ch8-pass3-3-audience-load-acceptance-aa04af5d` off current origin/main (`0615b9c`) per CLAUDE.md branch discipline.
- ✓ Flagged Political-Capture-cluster close-vs-skim divergence at §4.1 as principal cross-character pattern observation; offered three disposition options at §9.3 with Option A (hold) as default recommendation.
- ✓ Flagged both/and YIMBY synthesis as audience-management asset at §4.2 (strongest single audience-management move across acceptance set; no spot-fix warranted).
- ✓ Flagged Black-American-writing-tradition passage as lineage-honoring asset at §4.3 (no spot-fix warranted).
- ✓ Flagged sample-chapter readiness STRONG at §4.4.
- ✓ Flagged cumulative-cadence-density resolution at §4.5 (Pass 3.2 §7 cumulative-anaphora-cluster diagnostic resolved at acceptance-character level).
- ✓ Flagged first-person register-architecture acceptance-clean at §4.6 (Pass 3.2 F-V4 Option B + F-V10 Option C dispositions audience-load-clean).
- ✓ Flagged arithmetic-backbone-as-central-rhetorical-instrument at §4.7 (chapter's strongest cross-character asset; no spot-fix warranted).

---

*End of Ch 8 Stage-3 Pass 3.3 (Audience-Load — Acceptance) rigor pass — PROPOSED 2026-05-25. Aggregate verdict: READY AS-IS at §9.3 Option A (hold; default). Full 28-character acceptance set: 28 INCLUDE / 0 NEUTRAL / 0 EXCLUDE. No Phase C-γ session required for Pass 3.3 acceptance verdict to be sustained. Pass 3.4 (robustness — adversarial / detractor) is the next session for Ch 8 per per-prompt serial cadence + v3.0/v3.1 sub-pass split.*
