# Tech Appendix — Stage 3 Pass 3.4: Audience-Load Robustness (Adversarial Set)

**Date:** 2026-05-18
**Status:** PROPOSED — pending author ratification + Phase C cross-chapter rent-seeking workstream disposition
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
- **Verdict floor:** ⚠⚠⚠ EXCLUDE (finds chapter-disqualifying thread — Public Choice rent-seeking analysis is the load-bearing intellectual-serious critique TA does not engage; this is the SAME thread that surfaced as Ch 1 REAUDIT v3 #33 + drives the cross-chapter rent-seeking-engagement workstream).

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
| T4 | Public-Choice theorist | ⚠⚠⚠ EXCLUDE | **§5 Accountability Bond architecture — rent-seeking-blindness; §11.5 Norway-vs-American institutional-asymmetry without rent-seeking-explanation; §15.1 limitations section without Public-Choice critique engagement** |
| T5 | Libertarian / Rothbardian | ⚠⚠ EXCLUDE | §1.10 ten-commons-categories enumeration; §5 Accountability Bond; §6 CIT-admission as state-licensing; §15.1.6 Option C' rhetorical-vs-substantive |
| T6 | Reparations-economics methodological-skeptic | ⚠ EXCLUDE | §5.1.1 Darity-Mullen extension to broader case-class; §1.10 Darity-2026 single-source positioning; §5.5 backward-application empirically deferred |
| T7 | Tort-reform / corporate-fiduciary defense lawyer | ⚠⚠ EXCLUDE | §10.5 + §5.5 + §11 — combined produces litigation-architecture for corporate-extraction defendants |
| T8 | Technical-rigor skeptic / formal-math referee | ⚠ EXCLUDE | F-7 50/50 exact-percentage; Pass 2 typography items (F-11/12/14/17); notation-symbol density; §11.x sub-numbering convention |
| T9 | Reactionary intellectual technical-reader | ⚠⚠ EXCLUDE | §5.1.1 + §5.5 reparations-positioning; §1.10 ten-commons taxonomy; §14 lineage engagement; "non-partisan framing" claim test |
| T10 | WSJ editorial-board economics | ⚠⚠ EXCLUDE | §11.5 Norway existence-proof framing; §11.6 McDowell failure-case framing; §5 Accountability Bond as regulatory-state-expansion proposal |

**Aggregate verdicts:** 1 ⚠⚠⚠ + 7 ⚠⚠ + 2 ⚠ = 10/10 EXCLUDE (expected; adversarial-set verdict-floor is EXCLUDE per Stage 3 template §"Pass 3.4").

**Diagnostic value is in the threads collectively pulled, NOT the per-character verdicts.**

---

## §3. Thread-pull synthesis (canonical Pass 3.4 diagnostic format per Stage 3 template + Ch 1 REAUDIT v3 §5.3 model)

The thread-pull synthesis classifies each thread surfaced by ≥2 adversarial characters into:
- **(a) Load-bearing chapter claim** — TA must hold its ground; spot-fix would damage technical-rigor or scope. Cross-chapter handoff if thread warrants engagement in chapter-prose chapters.
- **(b) Procedural / cosmetic flag** — spot-fix could disarm without damaging the apparatus.

| # | Thread | Pulled by | Type | Recommendation |
|---|---|---|---|---|
| Σ1 | **§5 Accountability Bond architecture — rent-seeking-blindness.** The framework specifies what bonds do without engaging *who designs them* under what rent-seeking-incentives. §15.1 limitations section names alternatives but does not name Public Choice critique. | T4 (chapter-disqualifying); T1 + T5 + T10 partial-pull (regulatory-state-expansion frame) | **(a) Load-bearing — CROSS-CHAPTER HANDOFF ACTIVE** | **The cross-chapter rent-seeking-engagement workstream (in flight per [`cross-chapter-rent-seeking-engagement-handoff_2026-05-17.md`](../workstream-handoffs/cross-chapter-rent-seeking-engagement-handoff_2026-05-17.md)) is precisely the disposition for this thread.** Per retrofit handoff stub §3 "Cross-chapter rent-seeking handoff. TA is one of the touched artifacts; rent-seeking analysis material may land in TA §5.5 or new section." TA Pass 3.4 surfaces the SAME thread as Ch 1 REAUDIT v3 #33 — confirming the cross-chapter workstream's scope. Disposition: TA awaits the cross-chapter workstream's substantive material; pre-pub queue flag for external Public-Choice-tradition reviewer. **No retrofit-session spot-fix to TA**. |
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

**Justification:**
- Thread Σ1 (§5 Accountability Bond rent-seeking-blindness) is a **load-bearing common adversarial thread** pulled by T4 chapter-disqualifyingly + T1 + T5 + T10 partial-pull. **TA itself does not engage Public Choice rent-seeking analysis directly.** The cross-chapter rent-seeking-engagement workstream (in flight per [`cross-chapter-rent-seeking-engagement-handoff_2026-05-17.md`](../workstream-handoffs/cross-chapter-rent-seeking-engagement-handoff_2026-05-17.md)) is the structural disposition — Ch 5 / Ch 9 / TA are the cross-chapter targets where rent-seeking analysis lands. **The workstream's existence + active status disarms thread Σ1 from "REQUIRES STRUCTURAL ENGAGEMENT" down to CONDITIONALLY ROBUST.** TA awaits the workstream's substantive material to drop into §5.5 or a new TA section.
- Threads Σ2 + Σ3 + Σ4 + Σ5 + Σ6 (substitution-dominance premises; case-library framing; ten-commons taxonomy; reparations-positioning depth; litigation-architecture concern) are all **load-bearing chapter claims** where the framework holds its ground. The pre-pub review queue (Stage 5) flags each for the relevant external-reviewer engagement. Spot-fix would damage technical rigor or analytical scope.
- Thread Σ9 (§5.5 backward-application empirical deferral) is a **by-design scope-boundary**; the framework's explicit deference posture to the reparations-economics literature is the analytical claim. Pre-pub queue flag.
- Threads Σ7 + Σ8 (F-7 50/50 split exact-percentage hardening + Pass 2 typography items) are **procedural / cosmetic flags** already queued as I-1 + I-2 per 2026-05-14 verification round disposition; APPLY at pre-publication refresh.

**Net:** TA holds its ground against the 10-character adversarial set. The Public Choice rent-seeking-blindness thread (Σ1) is the diagnostic-significant finding — confirms the cross-chapter workstream's scope + locks TA as a downstream target for the workstream's substantive material. Pre-pub queue flags route every other thread to the appropriate external-reviewer engagement.

---

## §5. Cross-chapter routing

**Σ1 (Public Choice rent-seeking-blindness)** — confirms the cross-chapter rent-seeking-engagement workstream's scope. TA is one of the touched artifacts; rent-seeking analysis material may land in TA §5.5 (extending the bidirectional articulation to include rent-seeking-as-institutional-political-economy lens) OR a new TA section (e.g., §5.6 "Institutional-political-economy of bond architecture" OR §15.1.9 "Public Choice critique engagement"). Per handoff stub §3 + cross-chapter handoff §0 framing.

No new cross-chapter workstreams surface from this Pass 3.4 (the Σ1 thread is already routed to the active workstream).

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

- **Σ1 Public Choice rent-seeking-blindness:** cross-chapter workstream-routed; pre-pub queue flag for external Public-Choice-tradition reviewer (technical-economics + Virginia-School-tradition affiliation).
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

*End of TA Pass 3.4 audience-load robustness audit. PROPOSED 2026-05-18. CONDITIONALLY ROBUST verdict. No TA source-prose changes proposed in this session; all spot-fixes carry forward to pre-publication refresh or cross-chapter workstream completion per disposition table.*
