# Tech Appendix — Stage 3 Pass 3.4: Audience-Load Robustness (Adversarial Set)

**Date:** 2026-05-18
**Status:** PROPOSED — pending author ratification. **Amendment 2026-05-18 (post-session correction):** original verdict treated the cross-chapter rent-seeking workstream as "in flight" based on stale-memory framing in the retrofit handoff stub. Verification on 2026-05-18 (post-session) confirms: workstream **RATIFIED 2026-05-18** (commit `bc02767`) + substantive material **APPLIED to TA §1.10 line 608+** ("Scope: complementarity with Public Choice / rent-seeking analysis") via commit `a1e54d9` + parallel applications to Ch 5 line 184 + Ch 9 line 133 + Ch 8 line 123. Σ1 disposition updated from "in flight; substantive material awaits" to "APPLIED; framework's structural-disposition articulated at §1.10." T4 per-character verdict updated from ⚠⚠⚠ to ⚠⚠ (chapter-disqualifying → load-bearing-with-disposition). Overall verdict remains **CONDITIONALLY ROBUST** under strict reading of Stage 3 template Pass 3.4 verdict scale (Σ2-Σ6 + Σ9 remain common load-bearing threads). See §A Amendment block at end of artifact for full detail.
**Scope:** `core/technical-appendix/TechnicalAppendix_v2.0.0.html` (v2.1.0 dated 2026-05-14; 8,044 lines)
**Base sha:** `3582823` (worktree branch `claude/ta-pipeline-retrofit-ecstatic-shannon-a17b5c`)
**Workstream:** TA pipeline-retrofit (fourth and final of 4 standardization-comparison-bed retrofits)
**Pass:** Stage 3 Pass 3.4 — Audience-Load Robustness (FIRST Pass 3.4 robustness test on TA under v3.0 framing per retrofit handoff stub §1)
**Pass 3.4 doctrine reference:** [`tools/drafting-templates/stage-3-three-pass-rigor-audit.md`](../drafting-templates/stage-3-three-pass-rigor-audit.md) §"Pass 3.4: Audience-load (robustness)" + [`tools/drafting-templates/audience-pressure-test-construction.md`](../drafting-templates/audience-pressure-test-construction.md) §3 (adversarial / detractor character types) + §3.4 (thread-pull synthesis canonical diagnostic format)
**Stage 1c verdict:** COHERENCE VERIFIED — see [`tools/quality-gates/coherence-checks/ta_stage1c_2026-05-18.md`](../quality-gates/coherence-checks/ta_stage1c_2026-05-18.md)

---

## §0. Framing

TA is the framework's formal-academic-register apparatus. Its primary audience is technical-rigor reviewer (Sandy-Darity + downstream math + framework-methodology reviewers per Stage 5 pre-pub queue). The acceptance test for TA's target audience is implicit in Pass 1 math/proof audit (RATIFIED + APPLIED via Phase C Tracks 1-5) + the 2026-05-14 verification round (RATIFIED) per handoff stub §1 row 3.3.

**Pass 3.4 robustness** is the new-to-v3.0 element: build the adversarial / detractor character set drawn from positions hostile-by-financial-incentive (industry-funded), ideologically-opposed (Public Choice / libertarian / Chicago-orthodox / reactionary-intellectual), legal-adversarial (tort-reform), and technical-rigor-adversarial (formal-math academic skeptic); diagnose which threads they collectively find in TA's central derivations (CS = RCV − B; the bidirectional decomposition; the substitution-dominance theorem; the four-gates apparatus; the Three Methods triangulation); produce thread-pull synthesis with ROBUST / CONDITIONALLY ROBUST / REQUIRES STRUCTURAL ENGAGEMENT verdict.

Adversarial-character set size: **10 characters** per `audience-pressure-test-construction.md` §3.3 "Chapter (book-internal artifact, full rigor)" default (Industry-funded 2 + Ideologically-opposed 3 + Trade-press 1 + Cultural 1-2 + Legal 1 + Technical-rigor-adversarial 1 = 10). The TA-specific weighting shifts toward technical-rigor + ideological-econ adversaries (vs Ch 1's trade-press + cultural weighting), reflecting TA's academic-reviewer-facing register.

---

## §1. Adversarial character set (10)

### #T1. Industry-funded energy economist (Heritage / AEI energy fellow / Manhattan Institute / API senior economist)

- **Background:** PhD economist with affiliation to industry-funded think tank or trade association. Reads TA for policy-implication threats to fossil-fuel-industry economics.
- **Expected register:** "Methodology is interesting but the policy framework implies aggressive bond instruments that would raise extraction costs by orders of magnitude. The §11.5 Norway figures are real but Norway is a special case; the §11.6 McDowell figures conflate distinct cost categories and double-count via §10.5 substitution dominance."
- **Likely concerns:** §10.5 substitution-dominance theorem reads as policy-prescription cloaked in academic apparatus; §11.6 McDowell triangulation as the framework's argumentative cudgel against coal; §11.5 Norway's "84% reduction" framing as cherry-picking the existence-proof while ignoring American institutional context.
- **Verdict floor:** ⚠⚠ EXCLUDE (would actively reject; finds load-bearing threads in §10.5 + §11).

### #T2. Pharma-industry-funded health economist (PhRMA-affiliated; AHIP cluster)

- **Background:** Health-economics PhD with pharma-industry-funded research portfolio. Reads TA for cost-shifting-accounting threats to pharma + medical-device industries.
- **Expected register:** "The McDowell Black Lung trust-fund framing (§11.6) extends naturally to opioid + asbestos + tobacco precedents — the framework's CSD methodology is the structural-extraction theory of mass-tort accounting, deployed pre-emptively against pharma."
- **Likely concerns:** §5.1.1 Restitution Bond + §5.5 backward-application reads as litigation-architecture for pharma-cost-shifting cases; §10.5 substitution-dominance theorem applied to legacy-health-cost cases threatens pharma's actuarial accounting; §1.10 Autonomy commons "addiction-induced choice-restriction" framing reads as opioid-industry liability theory.
- **Verdict floor:** ⚠⚠ EXCLUDE (finds load-bearing thread in §5.1.1 + §1.10 Autonomy commons + §10.5).

### #T3. Chicago-School orthodox-econ reader (Becker-Friedman fellow; freshwater-macro cluster)

- **Background:** PhD macro/applied micro economist at Chicago Booth / Stanford / Minnesota tradition. Reads TA for heterodox-econ-vs-orthodox boundary violations.
- **Expected register:** "Market-failure premises are doing more work than the formalism admits. Theorem 10.1b's 'structural CS > 0 under current institutions' presumes market-failure as the baseline, not as a result. CS = RCV − B is well-defined but the framework's policy implications follow only if RCV exceeds B, and RCV is the framework's-chosen-construct, not a market-revealed price. The substitution-dominance theorem is a normative claim dressed as a welfare result."
- **Likely concerns:** §10.1b "structural CS > 0" reads as assumption-not-result; §3 RCV-as-discounted-integral reads as constructed-not-revealed valuation; §10.5 substitution-dominance theorem's welfare-comparison algebra rests on RCV-as-social-opportunity-cost framing that orthodox-econ reads as contested; §6 CIT counterfactual reads as social-planner's view rather than market-discovery process.
- **Verdict floor:** ⚠⚠ EXCLUDE (finds load-bearing threads in §10.1b + §10.5 + §3 + §6).

### #T4. Public-Choice theorist (Buchanan/Tullock-tradition; Mercatus / GMU cluster)

- **Background:** PhD economist in Virginia-School Public Choice tradition. Reads TA for rent-seeking-blindness in institutional-design proposals.
- **Expected register:** "The §5 Accountability Bond architecture — B₁ + B₂ + the bond-administration entity that levies and disburses them — is the precise institutional structure Public Choice theory predicts will be captured by the highest-rent-seeking concentrated interest. The framework names institutions without naming the rent-seekers who will design them. §15.1.5 two-instrument architecture is an institutional-design proposal without an institutional-political-economy chapter."
- **Likely concerns:** §5.1 + §5.1.1 + §5.1.2 Accountability Bond definitions specify *what* the bond does without engaging *who designs it* (rent-seeking question); §11.5 Norway's GPFG is described as institutional-design existence-proof without engagement of the political-economy that produced GPFG vs the political-economy that produced American extraction regimes (the rent-seeking-explanation gap); §15.1 limitations section names alternatives but does not name Public Choice critique of bond-architecture rent-seeking-capture vulnerability.
- **Verdict floor (original 2026-05-18):** ⚠⚠⚠ EXCLUDE — claimed TA did not engage Public Choice. **Verdict floor (corrected per §A Amendment):** ⚠⚠ EXCLUDE — finds load-bearing thread but TA §1.10's "Scope: complementarity with Public Choice / rent-seeking analysis" paragraph (lines 606–611; landed via `a1e54d9` + RATIFIED `bc02767`) DOES carry the framework's methodological-complementarity engagement (cites Buchanan & Tullock 1962 + Tullock 1967 + Mueller 2003 + applicability conditions). T4 may still push on the more specific concern that §5 Accountability Bond architecture + §15.1 limitations do not carry the engagement at the bond-design-rent-seeking-vulnerability level; that's procedural / structural-extension, not chapter-disqualifying. This is the SAME thread that surfaced as Ch 1 REAUDIT v3 #33 + drove the cross-chapter rent-seeking-engagement workstream **which has since RATIFIED + APPLIED material to TA + Ch 5 + Ch 9 + Ch 8**.

### #T5. Pure-libertarian / Rothbardian / Mises-Institute reader

- **Background:** Libertarian economic-philosophy reader; Mises Institute / Cato-libertarian-wing / FEE register. Reads TA for state-coercion proposals cloaked in scholarly language.
- **Expected register:** "Accountability Bond architecture (§5) is regulatory-state expansion proposal. Ten-commons enumeration (§1.10) is metaphysical claim about what counts as commons — and the framework, having claimed Option C' (commons-as-examples) modesty, then proceeds to legislate ten commons categories with state-administered bond instruments levied against extraction from each. The §6 CIT 'admission process' is a state-licensing apparatus."
- **Likely concerns:** §1.10 ten-commons-categories + §6 CIT-admission + §7 Four Gates apparatus + §5 Accountability Bond — the configuration is state-administered cost-internalization regime; framework's "Option C' political-philosophical-accommodation" framing (§15.1.6) is rhetorically modest but the apparatus's policy implications are expansive.
- **Verdict floor:** ⚠⚠ EXCLUDE (finds threads at §1.10 + §5 + §6 + §15.1.6; reads framework as expanded-regulatory-state proposal).

### #T6. Reparations-economics methodological-skeptic (e.g., center-right reparations critic — Loury / McWhorter cluster on structural-claims side; or technically-rigorous reparations-economics reader who tests Darity-Mullen methodological extensions)

- **Background:** Economist or political-philosopher who engages reparations-economics literature critically. Reads TA for over-claiming-deference or methodological-borrowing without methodological-engagement-depth.
- **Expected register:** "§5.1.1 positions the Restitution Bond as 'operationalizing the restitution-as-redress component within Darity-Mullen's reparations framework, extended to the broader case-class.' The 'broader case-class' extension is doing significant analytical work — the framework extends a methodology developed for slavery's structural-racial-extraction to coal, asbestos, opioids, vermiculite, deepwater drilling. The structural similarity is asserted; the methodological transferability is presumed. §5.5 articulates bidirectional reach but the backward-direction empirical work is deferred to subsequent volumes."
- **Likely concerns:** §5.1.1 Darity-Mullen positioning — does Darity-Mullen's typology actually accommodate the framework's positioning, or does the framework speak for a tradition without that tradition's ratification? §1.10 coercion-vector scope-of-applicability boundary (Darity 2026) — single-source attribution for a methodologically-load-bearing positioning claim; needs broader reparations-economics-field engagement. §5.5 backward-application is structurally articulated but empirically untested; framework's claim "structurally identical methodology" needs case-empirical demonstration.
- **Verdict floor:** ⚠ EXCLUDE (would push back on Darity-Mullen extension claim; acknowledges the framework's deference posture; chapter holds against the push-back if Darity ratifies the positioning, which Pass 1 § Amendment 2026-05-13 records he did during the 2026-05-13 session).

### #T7. Tort-reform / corporate-fiduciary defense lawyer (Defense Research Institute cluster; ALI Restatement of Torts contributor)

- **Background:** Defense-bar litigator in corporate-counsel / tort-defense practice. Reads TA for litigation-amplification threats.
- **Expected register:** "§5.1.1 Restitution Bond + §5.5 backward-application + §10.5 substitution-dominance theorem combined produce the framework's litigation-architecture: CSD methodology (backward-pricing of legacy-effects) + RCV methodology (forward-pricing of foreclosure) + substitution-dominance dominance result (welfare-comparison favoring substitution under conditions described). Applied to corporate-extraction defendants, the apparatus produces priced-cost claims at orders of magnitude exceeding current tort recoveries."
- **Likely concerns:** §10.5 P1 specifies RCV > P (substitution-dominance condition); under industry-typical extraction RCV often >> P; theorem's application generalizes to industry-wide liability exposure. §11.6 McDowell Black Lung framing as priced-policy-instance (~$5.1B outstanding debt; "approximately 0% CS-reduction" for American extraction regimes) reads as policy-advocacy for trust-fund-instrument expansion. §5.5 backward-application combined with §11 case-libraries reads as priced-claim-architecture for class-action plaintiffs.
- **Verdict floor:** ⚠⚠ EXCLUDE (finds load-bearing thread at §10.5 + §5.5 + §11; verdict reflects litigation-stakes, not technical-rigor failure — the apparatus is technically rigorous, which is the precise concern).

### #T8. Technical-rigor skeptic / formal-math academic referee (JPE / QJE quantitative-economics reviewer)

- **Background:** Quantitative-economics PhD with formal-math expertise. Reads TA for proof-rigor + notation-consistency + over-precision-claims.
- **Expected register:** "The math is mostly sound. The framework's definitions are well-formed; the central theorems (10.1a, 10.3, 10.4) prove what they claim. Pass 1 audit caught the Theorem 10.5 P1 equivocation (F-2; applied per commit `0af3ff1`) and the §10.4 knife-edge corollary hypothesis gap (F-18; applied per `0f62704`). Residual concerns: the F-7 50/50 Norway oil/gas working assumption is defensibly bounded but lacks exact-percentage published source (§C of verification round); the §10.5 substitution-dominance theorem's welfare-comparison algebra is correct under stated premises but the premises themselves are non-trivial (RCV > P condition; Investment_cost ≤ P feasibility); the §16.3 SCS spatial formalization required restatement per F-19 and the restatement uses a notation choice (consumption-region letter K) flagged by R-2 for Pass 2 review."
- **Likely concerns:** F-7 exact-percentage hardening (~15 min CSV download deferred to pre-publication refresh per I-1); residual Pass 2 typography items (F-11 log-base + F-12 P-overload + F-14 seven-vs-ten + F-17 capitalization; ~45 min sweep deferred per I-2); the framework's notation-symbol density is high and a referee may push for consolidation (e.g., notation glossary at TA front-matter); §11.x sub-numbering convention is internal-restart-based (post-Scheme-4 cleanup) rather than outer-block-anchored — referees in some traditions will prefer the latter.
- **Verdict floor:** ⚠ EXCLUDE (would push back at the technical-detail level but the chapter holds against the push-back; most concerns are pre-publication-refresh items already queued).

### #T9. Reactionary intellectual technical-reader (Niall Ferguson cluster + Manhattan Institute technically-competent fellow; National Affairs / American Affairs reader)

- **Background:** Politically-conservative intellectual with technical-economics + history training. Reads TA for left-coded-scholarship cues + lineage-engagement positioning.
- **Expected register:** "The lineage engagement is conspicuous. §14 cites Mazzucato, Stern, Hartwick, Solow, Ostrom, Dixit-Pindyck, Coase, Pigou, Savage, Parfit — the lineage range is broad but tilts heterodox-econ-friendly. §5.1.1 + §5.5 + §1.10 + §10.5 engagement with Darity-Mullen reparations-economics is foregrounded; the framework's 'structural-extraction' diagnosis maps the corporate-extraction case-class onto the racial-extraction case-class. The political work the framework does is the universalization of the reparations-economics-grievance-architecture into market-wide policy."
- **Likely concerns:** §5.1.1 + §5.5 reparations-economics-positioning; §1.10 ten-commons-categories framing (including Political + Cohesion + Epistemic + Autonomy commons) reads as activist-policy taxonomy; §15.1.5 two-instrument architecture as policy-architecture more than as analytical apparatus. The framework's "non-partisan-framing" claim is tested by §5 + §1.10 + §14.
- **Verdict floor:** ⚠⚠ EXCLUDE (finds load-bearing thread at §1.10 + §5 + §14; chapter must hold its ground that the framework's apparatus is analytical-not-political — but the apparatus's policy-implications are real and the framework does not deny them, which gives the reactionary reader a thread to pull).

### #T10. WSJ editorial-board / business-press conservative reader

- **Background:** Editorial-board economist / business-press senior writer (WSJ / Bloomberg Opinion conservative wing / NRO economics page). Reads TA for business-blame regulation-preparation cues.
- **Expected register:** "Norway as poster-child existence-proof (§11.5 + 84%-CS-reduction framing) + McDowell as failure-case (§11.6 + ~0%-CS-reduction framing) tees up policy-architecture for US extraction regimes that emulates Norway. The Accountability Bond apparatus (§5) is the proposed regulation. The framework's intellectual modesty (Option C', illustrative-not-canonical) is dressing on what is in substance a regulatory-state-expansion proposal."
- **Likely concerns:** §11.5 Norway framing as existence-proof; §11.6 McDowell framing as policy-failure narrative; §5 Accountability Bond as the proposed instrument; §15.1.6 Option C' modesty framing as rhetorical-not-substantive. WSJ editorial-board reader's verdict largely reflects the regulatory-state-expansion implication, not technical rigor.
- **Verdict floor:** ⚠⚠ EXCLUDE (would weaponize the §11 case-juxtaposition + §5 Accountability Bond proposal as regulatory-state-expansion preparation).

---

## §2. Per-character verdict tally

| # | Character | Verdict | Primary threads pulled |
|---|---|---|---|
| T1 | Industry-funded energy economist | ⚠⚠ EXCLUDE | §10.5 substitution-dominance; §11.5 Norway "84%" framing; §11.6 McDowell triangulation |
| T2 | Pharma-industry health economist | ⚠⚠ EXCLUDE | §5.1.1 Restitution Bond + §5.5 backward-application + §1.10 Autonomy "addiction-induced choice-restriction"; §10.5 applied to legacy-health-cost |
| T3 | Chicago-School orthodox-econ | ⚠⚠ EXCLUDE | §10.1b "structural CS > 0"; §3 RCV-as-constructed; §10.5 welfare-comparison; §6 CIT counterfactual |
| T4 | Public-Choice theorist | ⚠⚠ EXCLUDE *(corrected per §A Amendment; was ⚠⚠⚠)* | **§5 Accountability Bond architecture bond-design-rent-seeking-vulnerability (procedural); §11.5 Norway-vs-American institutional-asymmetry not carrying rent-seeking explanation in §11 prose (procedural); §15.1 limitations section not naming Public-Choice critique** — note: TA §1.10 (line 608+) carries the framework-wide Public Choice complementarity engagement per RATIFIED cross-chapter workstream |
| T5 | Libertarian / Rothbardian | ⚠⚠ EXCLUDE | §1.10 ten-commons-categories enumeration; §5 Accountability Bond; §6 CIT-admission as state-licensing; §15.1.6 Option C' rhetorical-vs-substantive |
| T6 | Reparations-economics methodological-skeptic | ⚠ EXCLUDE | §5.1.1 Darity-Mullen extension to broader case-class; §1.10 Darity-2026 single-source positioning; §5.5 backward-application empirically deferred |
| T7 | Tort-reform / corporate-fiduciary defense lawyer | ⚠⚠ EXCLUDE | §10.5 + §5.5 + §11 — combined produces litigation-architecture for corporate-extraction defendants |
| T8 | Technical-rigor skeptic / formal-math referee | ⚠ EXCLUDE | F-7 50/50 exact-percentage; Pass 2 typography items (F-11/12/14/17); notation-symbol density; §11.x sub-numbering convention |
| T9 | Reactionary intellectual technical-reader | ⚠⚠ EXCLUDE | §5.1.1 + §5.5 reparations-positioning; §1.10 ten-commons taxonomy; §14 lineage engagement; "non-partisan framing" claim test |
| T10 | WSJ editorial-board economics | ⚠⚠ EXCLUDE | §11.5 Norway existence-proof framing; §11.6 McDowell failure-case framing; §5 Accountability Bond as regulatory-state-expansion proposal |

**Aggregate verdicts (corrected per §A Amendment):** 0 ⚠⚠⚠ + 8 ⚠⚠ + 2 ⚠ = 10/10 EXCLUDE (expected; adversarial-set verdict-floor is EXCLUDE per Stage 3 template §"Pass 3.4"). Original aggregate before correction: 1 ⚠⚠⚠ + 7 ⚠⚠ + 2 ⚠ (with T4 at ⚠⚠⚠ chapter-disqualifying).

**Diagnostic value is in the threads collectively pulled, NOT the per-character verdicts.**

---

## §3. Thread-pull synthesis (canonical Pass 3.4 diagnostic format per Stage 3 template + Ch 1 REAUDIT v3 §5.3 model)

The thread-pull synthesis classifies each thread surfaced by ≥2 adversarial characters into:
- **(a) Load-bearing chapter claim** — TA must hold its ground; spot-fix would damage technical-rigor or scope. Cross-chapter handoff if thread warrants engagement in chapter-prose chapters.
- **(b) Procedural / cosmetic flag** — spot-fix could disarm without damaging the apparatus.

| # | Thread | Pulled by | Type | Recommendation |
|---|---|---|---|---|
| Σ1 | **§5 Accountability Bond architecture — bond-design-rent-seeking-vulnerability (post-Amendment framing).** Original framing: "rent-seeking-blindness; framework specifies what bonds do without engaging who designs them." Amended framing per §A: TA §1.10 line 608+ now carries the methodological complementarity engagement (Buchanan & Tullock 1962 + Tullock 1967 + Mueller 2003); T4's residual concern narrows to §5 + §15.1 not carrying engagement at the bond-design level. | T4 (load-bearing-with-disposition; downgraded from chapter-disqualifying); T1 + T5 + T10 partial-pull (regulatory-state-expansion frame) | **(a) Load-bearing — CROSS-CHAPTER WORKSTREAM APPLIED** | **The cross-chapter rent-seeking-engagement workstream RATIFIED 2026-05-18 per [`cross-chapter-rent-seeking-engagement-handoff_2026-05-17.md`](../workstream-handoffs/cross-chapter-rent-seeking-engagement-handoff_2026-05-17.md) §9 ratification log; substantive content APPLIED to TA §1.10 (line 608+; commit `a1e54d9`), Ch 5 line 184, Ch 9 line 133, Ch 8 line 123 (all `a1e54d9` → ratified `bc02767`).** Disposition: thread acknowledged + framework's structural disposition articulated at scope level; T4 residual concern (§5 + §15.1 bond-design-rent-seeking-vulnerability engagement absence) routes to **pre-pub queue flag for external Public-Choice-tradition reviewer + future extension session if author wants §5/§15.1-side engagement** (not chapter-blocking). **No retrofit-session spot-fix to TA**. |
| Σ2 | **§10.5 substitution-dominance theorem — premises are non-trivial.** The welfare-comparison algebra is correct under stated premises (P1 RCV > P; P4 Investment_cost ≤ P) but readers from orthodox-econ, industry-funded, and tort-defense traditions read the theorem's *application* as policy-advocacy rather than analytical result. | T1 + T3 + T7 (Chicago + industry-energy + tort-defense) | **(a) Load-bearing** | TA's §10.5 already carries the cleaned-premises proof per Pass 1 F-2 + Phase C Track 2 (commit `0af3ff1`). The "premises-are-non-trivial" concern is **the framework holding its ground** — RCV > P is the framework's empirical claim per §11 case-libraries; the theorem's policy-implication strength follows from the empirical claim, which is the analytical work. Spot-fix not warranted. Pre-pub queue flag: external math + framework-methodology reviewers should engage the §10.5 premises empirically. |
| Σ3 | **§11 case-library framing — Norway as existence-proof, McDowell as failure-case.** The §11.5 Norway "84% CS-reduction" + §11.6 McDowell "~0% CS-reduction" juxtaposition reads as policy-architecture preparation. | T1 + T9 + T10 (industry + reactionary + WSJ) | **(a) Load-bearing** | The juxtaposition IS the framework's load-bearing empirical claim: institutional-architecture differences produce the CS-reduction gap. TA §11 is the documented case-library; the framing follows from the data, not vice versa. Spot-fix not warranted. Pre-pub queue: external policy-economics reviewer to verify the framing reads as analytical-finding rather than as policy-conclusion-presupposed. |
| Σ4 | **§1.10 ten-commons-categories — taxonomy is substantive policy claim.** The framework's Option C' modesty (commons-as-examples) is rhetorically present but the ten-commons enumeration is treated as substantive throughout TA. | T5 + T9 (libertarian + reactionary) | **(a) Load-bearing** | The ten-commons enumeration is the framework's empirical-record-of-what-surfaced across the 18 cases; the Option C' (examples-not-canonical) framing is the framework's structural-claim about its own scope. TA §15.1.6 explicitly articulates this — the framing is intentional. Spot-fix not warranted. Pre-pub queue: external framework-methodology reviewer in adjacent traditions (Ostrom-successor; Hartwick; heterodox-econ) to verify the Option C' framing is methodologically coherent. |
| Σ5 | **§5.1.1 + §5.5 + §1.10 reparations-economics-positioning depth.** The framework extends Darity-Mullen reparations methodology to a broader case-class; the extension's methodological transferability is asserted, not demonstrated. | T6 + T9 (reparations-methodological-skeptic + reactionary) | **(a) Load-bearing, with author-ratification disposition** | Sandy/Darity engagement (interview completed 2026-05-13 + Sandy-Darity packet sent + Sandy's 1-2 week commitment to read TA + Ch 6) is the structural disposition for this thread. The framework's deference posture is captured in §5.1.1's "operationalizing the restitution-as-redress component within Darity-Mullen's reparations framework, extended to the broader case-class" language. The author-ratified Approach B at Pass 1 Amendment 2026-05-13 sets the framework's positioning. Pre-pub queue: external reparations-economics reviewer (Darity-Mullen-tradition successor) for the "broader case-class" extension. |
| Σ6 | **§10.5 + §5.5 + §11 — litigation-architecture concern.** Combined apparatus produces priced-claim methodology applicable to corporate-extraction defendants at orders of magnitude exceeding current tort recoveries. | T7 (tort-defense); T2 + T6 partial-pull | **(a) Load-bearing — the apparatus IS what the apparatus is** | The apparatus is technically rigorous, which is the precise tort-defense concern. The framework does not claim to drive litigation; it claims to price what extraction costs. Whether the pricing translates into litigation is a downstream institutional-design question (per the §5 Accountability Bond architecture). Pre-pub queue: this concern is **expected** at publication time and is the framework's load-bearing analytical claim. Spot-fix would damage technical rigor. |
| Σ7 | **F-7 50/50 oil/gas working assumption (Norway cumulative split).** Defensibly bounded per 2026-05-14 verification round §C; exact-percentage not published in summary form by Norwegian Offshore Directorate. | T8 (technical-rigor skeptic) | **(b) Procedural / cosmetic flag — already queued as I-1** | Per 2026-05-14 verification round §I disposition: pre-publication refresh ~15 min CSV download from sodir.no; magnitude impact ~2% on cumulative emissions (well within M1/M2/M3 method-range resolution). Disposition: APPLY at pre-publication refresh (per I-1 carry-forward). Carried in Stage 5 pre-pub queue. |
| Σ8 | **Pass 2 typography items (F-11 log-base + F-12 P-overload + F-14 seven-vs-ten dimensions + F-17 capitalization).** All deferred per 2026-05-14 verification round I-2 (~45 min total). | T8 (technical-rigor skeptic) | **(b) Procedural / cosmetic flag — already queued as I-2** | Disposition: APPLY at pre-publication refresh (per I-2 carry-forward). Carried in Stage 5 pre-pub queue. |
| Σ9 | **§5.5 backward-application empirically deferred to subsequent volumes.** Framework's "structurally identical methodology" claim is asserted; backward case-empirical demonstration is outside Book 1's scope. | T6 (reparations-methodological-skeptic) | **(a) Load-bearing — by-design scope-boundary** | §5.5 explicitly scopes backward-direction empirical work to subsequent volumes ("Voices in the reparations-economics tradition have been doing this work for years; the framework recognizes and defers"). The "structurally identical methodology" claim is the framework's analytical claim; case-empirical validation lives in the reparations-economics literature the framework defers to. Spot-fix not warranted. Pre-pub queue: external reparations-economics reviewer for the deference-posture verification. |

---

## §4. Robustness verdict

**CONDITIONALLY ROBUST** (per Stage 3 template Pass 3.4 verdict scale).

Per Stage 3 template:
> "**CONDITIONALLY ROBUST** — common load-bearing thread found that the chapter's structural moves do disarm; thread acknowledged in the pre-pub review queue."

**Justification (corrected per §A Amendment):**
- Thread Σ1 (§5 Accountability Bond + bond-design-rent-seeking-vulnerability) — **original framing erroneously claimed TA does not engage Public Choice rent-seeking analysis**. Verification 2026-05-18 (post-session) confirms TA §1.10 line 608+ DOES carry "Scope: complementarity with Public Choice / rent-seeking analysis" paragraph (lines 606–611) — cites Buchanan & Tullock 1962, Tullock 1967, Mueller 2003; articulates framework's scope (cost-bearing-party identification) vs Public Choice's scope (rent-seeking-actor identification); specifies applicability conditions (sharpest / blurred / out-of-scope); tells Public Choice readers how to engage the framework. The cross-chapter rent-seeking-engagement workstream is **RATIFIED 2026-05-18** (commit `bc02767`) with substantive material APPLIED via commit `a1e54d9` to TA §1.10 + Ch 5 line 184 + Ch 9 line 133 + Ch 8 line 123. **T4's residual concern narrows to §5 Accountability Bond architecture + §15.1 limitations not carrying the engagement at the bond-design-rent-seeking-vulnerability level** — procedural / extension-opportunity, not chapter-disqualifying. Σ1 disposition shifts from "workstream in flight; awaits material" to "workstream APPLIED; framework's structural-disposition articulated at scope level; residual extension opportunity at §5 + §15.1."
- Threads Σ2 + Σ3 + Σ4 + Σ5 + Σ6 (substitution-dominance premises; case-library framing; ten-commons taxonomy; reparations-positioning depth; litigation-architecture concern) are all **load-bearing chapter claims** where the framework holds its ground. The pre-pub review queue (Stage 5) flags each for the relevant external-reviewer engagement. Spot-fix would damage technical rigor or analytical scope.
- Thread Σ9 (§5.5 backward-application empirical deferral) is a **by-design scope-boundary**; the framework's explicit deference posture to the reparations-economics literature is the analytical claim. Pre-pub queue flag.
- Threads Σ7 + Σ8 (F-7 50/50 split exact-percentage hardening + Pass 2 typography items) are **procedural / cosmetic flags** already queued as I-1 + I-2 per 2026-05-14 verification round disposition; APPLY at pre-publication refresh.

**Net:** TA holds its ground against the 10-character adversarial set. The Public Choice rent-seeking-blindness thread (Σ1) is the diagnostic-significant finding — confirms the cross-chapter workstream's scope + locks TA as a downstream target for the workstream's substantive material. Pre-pub queue flags route every other thread to the appropriate external-reviewer engagement.

---

## §5. Cross-chapter routing

**Σ1 (Public Choice rent-seeking complementarity)** — cross-chapter rent-seeking-engagement workstream **RATIFIED 2026-05-18** (commit `bc02767`); substantive material APPLIED via commit `a1e54d9` to TA §1.10 + Ch 5 line 184 + Ch 9 line 133 + Ch 8 line 123. TA's §1.10 paragraph (lines 606–611) carries the framework's scope-level complementarity engagement. Workstream is **COMPLETED** for TA's scope; residual extension opportunity at §5 + §15.1 (bond-design-rent-seeking-vulnerability engagement) is **NOT a cross-chapter workstream** but rather a potential future single-section spot-fix to TA at author discretion (handled via pre-pub queue flag + author judgment).

No new cross-chapter workstreams surface from this Pass 3.4. The Σ1 thread's cross-chapter workstream is RATIFIED + APPLIED.

---

## §6. Spot-fix recommendations (DO NOT APPLY in this session per retrofit hard constraints)

Per retrofit template §5: "Do NOT apply spot-fixes to chapter source during the retrofit session. Author ratifies first."

| ID | Spot-fix | Scope | Disposition |
|---|---|---|---|
| PF-Σ7 | F-7 Norway oil/gas exact-percentage hardening (CSV download from sodir.no + §11.5 anchor + F-7 weighted-factor calc + cumulative-emissions cell update) | TA §11.5 | DEFERRED to pre-publication refresh (~15 min effort; magnitude ~2% within method-range resolution). |
| PF-Σ8 | Pass 2 typography sweep (F-11 ln-specification + F-12 P-overload clarification + F-14 seven-vs-ten dimensions cohort + F-17 capitalization alignment) | TA §3.5 + §3.2 + §10.5 + §6.2 + §6.3 + §1.9 + §13 + §3.5 + §13.1 | DEFERRED to pre-publication refresh (~45 min total). |
| PF-Σ1 | Public Choice rent-seeking-blindness engagement section (e.g., §5.6 or §15.1.9) | TA §5 or §15.1 | DEFERRED to cross-chapter rent-seeking-engagement workstream completion. Material lands when the workstream produces it. |

---

## §7. Carry-forward to Stage 5 pre-publication review queue

Per Pass 3.4 doctrine + Stage 5 doctrine §3 pre-pub queue contents §2.3 "Adversarial threads NOT fully disarmed":

- **Σ1 Public Choice rent-seeking complementarity:** workstream RATIFIED + APPLIED at TA §1.10 (commit `a1e54d9` → ratified `bc02767`); pre-pub queue flag for external Public-Choice-tradition reviewer to verify the §1.10 complementarity engagement reads as substantive + verify whether §5 + §15.1 should be extended at a future session (author discretion).
- **Σ2 §10.5 substitution-dominance premises:** pre-pub queue flag for external math + framework-methodology reviewers.
- **Σ3 §11 case-library framing:** pre-pub queue flag for external policy-economics reviewer (framing-vs-finding verification).
- **Σ4 §1.10 ten-commons taxonomy:** pre-pub queue flag for external framework-methodology reviewer in adjacent tradition (Ostrom-successor / Hartwick / heterodox-econ).
- **Σ5 §5.1.1 reparations-positioning depth:** pre-pub queue flag for external reparations-economics reviewer (Darity-Mullen-tradition successor; Sandy/Darity engagement already in flight).
- **Σ6 §10.5 + §5.5 + §11 litigation-architecture concern:** expected at publication; flagged for legal-adversarial context-awareness in pre-pub queue.
- **Σ9 §5.5 backward-application deferral:** pre-pub queue flag for external reparations-economics reviewer (deference-posture verification).

Each of these populates the pre-pub queue §2.3 + §3 (recommended external reviewer types) per Stage 5 doctrine.

---

## §8. Cross-references

- Pass 3.4 doctrine: [`tools/drafting-templates/stage-3-three-pass-rigor-audit.md`](../drafting-templates/stage-3-three-pass-rigor-audit.md) §"Pass 3.4: Audience-load (robustness)"
- Adversarial character types + thread-pull synthesis format: [`tools/drafting-templates/audience-pressure-test-construction.md`](../drafting-templates/audience-pressure-test-construction.md) §3
- Canonical Ch 1 REAUDIT v3 §5.3 thread-pull synthesis (the diagnostic-format reference model): [`tools/rigor-passes/commons_bonds_ch1_stage_3_pass_3_audience_load_REAUDIT_2026-05-17_PROPOSED.md`](commons_bonds_ch1_stage_3_pass_3_audience_load_REAUDIT_2026-05-17_PROPOSED.md)
- TA Pass 1 math/proof audit: [`tools/rigor-passes/tech_appendix_rigor_pass_2026-05-13_pass_1_math_audit.md`](tech_appendix_rigor_pass_2026-05-13_pass_1_math_audit.md)
- TA 2026-05-14 verification round: [`tools/rigor-passes/tech_appendix_verification_round_2026-05-14.md`](tech_appendix_verification_round_2026-05-14.md)
- TA retrofit handoff: [`tools/workstream-handoffs/ta-pipeline-retrofit-handoff_2026-05-17.md`](../workstream-handoffs/ta-pipeline-retrofit-handoff_2026-05-17.md)
- Cross-chapter rent-seeking-engagement workstream: [`tools/workstream-handoffs/cross-chapter-rent-seeking-engagement-handoff_2026-05-17.md`](../workstream-handoffs/cross-chapter-rent-seeking-engagement-handoff_2026-05-17.md)
- TA Stage 1a clean-baseline: [`tools/quality-gates/clean-baselines/ta_stage1a_2026-05-18.md`](../quality-gates/clean-baselines/ta_stage1a_2026-05-18.md)
- TA Stage 1c coherence-check: [`tools/quality-gates/coherence-checks/ta_stage1c_2026-05-18.md`](../quality-gates/coherence-checks/ta_stage1c_2026-05-18.md)

---

*End of TA Pass 3.4 audience-load robustness audit. PROPOSED 2026-05-18. CONDITIONALLY ROBUST verdict (preserved post-Amendment under strict reading of verdict scale; Σ2-Σ6 + Σ9 remain common load-bearing threads). No TA source-prose changes proposed in this session; all spot-fixes carry forward to pre-publication refresh per disposition table. Σ1 cross-chapter workstream is RATIFIED + APPLIED per §A Amendment.*

---

## §A. Amendment 2026-05-18 (post-session verification correction)

**Trigger.** Author 2026-05-18 (post-session) flagged: *"I thought we already completed the rent-seeking thread? Is rent-seeking-blindness referring to something additional?"* The author's flag is correct — the cross-chapter rent-seeking-engagement workstream was RATIFIED 2026-05-18 (commit `bc02767`) with substantive material APPLIED via commit `a1e54d9` BEFORE this Pass 3.4 audit fired. The original audit's framing of the workstream as "in flight" was a verification failure (treating stale-memory framing from the retrofit handoff stub as current state rather than verifying TA's actual current §1.10 contents). Per `feedback_verify_stale_memory_claims.md`: workstream-status claims from memory require verification against current code before assertion as fact.

**Verified facts (post-session 2026-05-18):**

1. **TA §1.10 lines 606–611** carries a complete Public Choice complementarity paragraph titled "Scope: complementarity with Public Choice / rent-seeking analysis." Content: (a) names the framework's cost-severance-accounting-at-architecture-level scope; (b) names the complementary Public Choice analytical question (who shaped the architecture / political-economic process / rent-seeking expenditure); (c) cites Buchanan & Tullock 1962 *Calculus of Consent*, Tullock 1967, Mueller 2003 and successors; (d) articulates framework-vs-Public-Choice complementarity (framework's apparatus = cost-bearing-party identification + magnitude; Public Choice's apparatus = political-coalition-of-architecture-shapers); (e) specifies applicability conditions (sharpest complementarity application: heterogeneous extractor/cost-bearer populations; blurred application: overlapping populations + intergenerational temporal-distance; out-of-scope for the TA: rent-seeking-actor-identification methodology proper); (f) tells Public Choice readers how to engage the framework ("Readers in the Public Choice tradition should read the framework's cost-bearing-party identification as a foundation their apparatus can apply to, not as an alternative to their apparatus.").
2. **Cross-chapter workstream applications** all landed via commit `a1e54d9` (2026-05-17, author-direct-push):
   - Ch 5 line 184 — "Architecture and rent-seeking: who shaped the system?" section.
   - Ch 9 line 133 — Public Choice complementary accounting section.
   - Ch 8 line 123 — Political Capture Cost touch.
   - TA §1.10 line 608+ — Public Choice complementarity paragraph (above).
3. **Workstream handoff** [`cross-chapter-rent-seeking-engagement-handoff_2026-05-17.md`](../workstream-handoffs/cross-chapter-rent-seeking-engagement-handoff_2026-05-17.md) §0 status: **RATIFIED 2026-05-18** by PM session (commit `bc02767`).

**Corrections applied in this Amendment:**

- **T4 per-character verdict:** ⚠⚠⚠ EXCLUDE → **⚠⚠ EXCLUDE.** Chapter-disqualifying framing was based on stale "TA does not engage Public Choice" claim; corrected to load-bearing-with-disposition. T4's residual concern narrows to §5 Accountability Bond architecture + §15.1 limitations not carrying the engagement at the bond-design-rent-seeking-vulnerability level — procedural / extension-opportunity, not chapter-blocking.
- **Aggregate verdicts:** 1 ⚠⚠⚠ + 7 ⚠⚠ + 2 ⚠ → **0 ⚠⚠⚠ + 8 ⚠⚠ + 2 ⚠.**
- **Thread Σ1 framing + type-classification:** "rent-seeking-blindness" → "bond-design-rent-seeking-vulnerability"; "CROSS-CHAPTER HANDOFF ACTIVE" → "CROSS-CHAPTER WORKSTREAM APPLIED."
- **§4 robustness verdict justification:** explicitly notes TA §1.10's existing engagement; workstream APPLIED per §A above; verdict CONDITIONALLY ROBUST preserved because Σ2-Σ6 + Σ9 remain common load-bearing threads (Σ1 was not the only common thread; the verdict scale's "ROBUST = no common load-bearing threads" requires more than just Σ1's disposition).
- **§5 cross-chapter routing:** workstream RATIFIED + APPLIED; no new workstream needed from this Pass 3.4.
- **§7 pre-pub queue carry-forward:** Σ1 pre-pub queue flag reframed to "verify §1.10 engagement reads as substantive + verify whether §5 + §15.1 should be extended at a future session (author discretion)."

**Discipline lesson recorded.** The original 2026-05-18 audit relied on the retrofit handoff stub's §3 phrasing — *"Cross-chapter rent-seeking handoff. TA is one of the touched artifacts in the cross-chapter rent-seeking-engagement workstream. Sequencing: prefer AFTER rent-seeking workstream touches land (rent-seeking analysis material may land in TA §5.5 or new section)."* — without checking the workstream-handoff's current ratification status OR verifying TA's actual content at §1.10. The retrofit handoff stub was drafted before the workstream landed; its "Sequencing: prefer AFTER" phrasing predates `a1e54d9`. The discipline failure was treating the handoff stub's PROPOSED-state framing as current-state framing. Heeding the harness's automatic staleness reminder + `feedback_verify_stale_memory_claims.md` discipline rigorously: workstream-status claims from a >3-day-old artifact reference (the retrofit handoff stub is 2026-05-17; this session 2026-05-18; within the 3-day window but the handoff stub itself flagged "sequencing AFTER" which should have triggered verification).

**Amendment author-ratification path:** ratifies with Stage 4 verdict + Stage 5 sign-off batch ratification per CLAUDE.md merge-to-main default for rigor-pass artifacts. The Amendment-corrected verdicts replace the original where they differ; the original framings are preserved in the Amendment block as audit-trail.
