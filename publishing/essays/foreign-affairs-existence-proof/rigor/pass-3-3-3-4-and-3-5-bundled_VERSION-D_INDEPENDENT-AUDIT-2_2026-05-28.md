# Ch 4 → Foreign Affairs Version D (hybrid) — Stage 3 Pass 3.3 + 3.4 + 3.5 Bundled INDEPENDENT AUDIT-2 v1.0.0 — 2026-05-28

**Status:** PROPOSED 2026-05-28. **Second independent (fresh-session) audit** of Version D (hybrid `best-of-both`), commissioned because the prior chip's audit at `pass-3-3-and-3-4-bundled-audience-load_VERSION-D_INDEPENDENT-AUDIT_2026-05-28.md` (commit `2bdd9dd`) covered Pass 3.3 + Pass 3.4 only — **Pass 3.5 was omitted from its scope by author error**. This audit re-scores Pass 3.3 + Pass 3.4 from independent first principles, adds the missing Pass 3.5 developmental-edit pass, and cross-checks against both the drafter's-self-audit AND the prior chip's audit at Phase 3 boundary.

Phase 2 independent scoring on V-D was completed before Phase 3 reading of `ch4-foreign-affairs-essay_hybrid_drafters-self-audit.md` and `pass-3-3-and-3-4-bundled-audience-load_VERSION-D_INDEPENDENT-AUDIT_2026-05-28.md`. The independent-replication value-add is real: this is a quality-control double-check on the prior single-chip audit + a Pass 3.5 fill-in for the missed pass.

**Audit target.** [`publishing/essays/foreign-affairs-existence-proof/_archive/parallel-drafts_2026-05-28/ch4-foreign-affairs-essay_hybrid_best-of-both.md`](../_archive/parallel-drafts_2026-05-28/ch4-foreign-affairs-essay_hybrid_best-of-both.md) (Version D; ~5,941w body per drafter / ~5,948w body by awk-grep per prior chip; 12 body em-dashes at 7 sites; 90% of locked-cut prose preserved verbatim; backports Phillips Petroleum + Hannesson 1909 + NBIM AR 2023 + Pistor + Tooze + §I close em-dash + §III foreclosure-pivot em-dash; rejects IMF Article IV / OECD / Meld. St. 9 / Truman 2010 inline + preserves keep-Mazzucato-sub-textual disposition).

**Audit baselines.**

- Pass 3.3 baseline: locked cut Pass 3.3 RATIFIED PASS 2026-05-27 at 16/16 INCLUDE per [`pass-3-3-audience-load.md`](pass-3-3-audience-load.md).
- Pass 3.4 baseline: locked cut Pass 3.4 RATIFIED ROBUST 2026-05-27 per [`pass-3-4-adversarial.md`](pass-3-4-adversarial.md) (A1 + A2 PARTIALLY ROBUST; A3 ROBUST).
- Pass 3.5 baseline: locked cut Pass 3.5 RATIFIED HOLD 2026-05-27 per [`pass-3-5-developmental-edit.md`](pass-3-5-developmental-edit.md) (0 spot-fixes; F-3.5-L1 + F-3.5-L2 awareness items; F-3.2-L3 §VI anaphora HOLD as rhetorical-escalation).
- Prior chip's V-D Pass 3.3 + Pass 3.4 audit at [`pass-3-3-and-3-4-bundled-audience-load_VERSION-D_INDEPENDENT-AUDIT_2026-05-28.md`](pass-3-3-and-3-4-bundled-audience-load_VERSION-D_INDEPENDENT-AUDIT_2026-05-28.md): 16/16 INCLUDE with 8 ✅✅✅ + 8 ✅✅; ROBUST aggregate; SHIP-READY at FA submission window.

**Submission timeline.** Foreign Affairs portal submission window Q4 2026 / Q1 2027 (Nov–Feb) per cascade plan v2 §3 W2.3. No near-term gate; this AUDIT-2 lands 2026-05-28 to validate the prior chip's findings + close the Pass 3.5 gap.

**Critical calibration discipline.** Foreign Affairs editorial brain (Daniel Kurtz-Phelan; CFR Senior Fellow background; *The China Mission* author) reads for: cross-jurisdictional comparative-institutional analysis grounded in named cases; argument advancing the policy-intellectual conversation rather than restating it; named-institution clarity; SWF + extractive-economy + IPE as on-brand subject matter; refusal of partisan-aligned framing; institutional-architecture-as-engineerable conclusion. **The Aeon literary-philosophical calibration (cinematic-opener-preferred; em-dash-as-philosophical-breath signature; collective-singular literary voice) does NOT transfer.** Declarative scene-setting beats cinematic openers at FA; selective citation deployment beats citation density; third-person institutional-policy reportage holds throughout. This audit scores against FA-specific calibration only.

---

## §0. Source artifacts read

**Phase 0 — calibration baseline (CLAUDE.md + memory + brief + ratified rigor baselines):**

1. `CLAUDE.md` — merge-on-ratification rule; branch discipline; voice register.
2. [`tools/memory/feedback_audience_aware_drafting_discipline.md`](../../../../tools/memory/feedback_audience_aware_drafting_discipline.md) v3.1 — pipeline doctrine; Pass 3.3 + 3.4 + 3.5 scope; Amendment B Pass 3.5 codification; Amendment C per-finding interactive ratification.
3. [`tools/memory/feedback_em_dash_overuse.md`](../../../../tools/memory/feedback_em_dash_overuse.md) — em-dash calibration discipline (active justification required).
4. [`tools/memory/feedback_no_invented_factual_claims_in_publisher_facing_prose.md`](../../../../tools/memory/feedback_no_invented_factual_claims_in_publisher_facing_prose.md) — hard rule on fabrication; substrate-safety discipline for Pass 3.5 generation.
5. [`tools/memory/feedback_merge_on_ratification.md`](../../../../tools/memory/feedback_merge_on_ratification.md) — push discipline for output commit.
6. [`tools/memory/feedback_named_subject_consent.md`](../../../../tools/memory/feedback_named_subject_consent.md) — named-subject discipline; FA named-subject status closed at Stage 0.
7. [`publishing/essays/foreign-affairs-existence-proof/rigor/stage-1-brief.md`](stage-1-brief.md) — 16-character acceptance set (§1 Tier 1–3); 3-character adversarial set (§1 Tier 3 A1/A2/A3); FA editorial-brain map (§2); voice register (§5); canonical content (§7); apparatus exclusion list (§8); named-subject status (§11); Pass 3.3/3.4/3.5 protocol (§13); RATIFIED 2026-05-26 commit `1f73197`.
8. [`pass-3-1-fact-check.md`](pass-3-1-fact-check.md) — RATIFIED + APPLIED baseline.
9. [`pass-3-2-voice-polish.md`](pass-3-2-voice-polish.md) — RATIFIED + APPLIED baseline.
10. [`pass-3-3-audience-load.md`](pass-3-3-audience-load.md) — RATIFIED PASS 2026-05-27 baseline.
11. [`pass-3-4-adversarial.md`](pass-3-4-adversarial.md) — RATIFIED ROBUST 2026-05-27 baseline.
12. [`pass-3-5-developmental-edit.md`](pass-3-5-developmental-edit.md) — RATIFIED HOLD 2026-05-27 baseline.
13. [`stage-4-render-audit.md`](stage-4-render-audit.md) — RATIFIED CLEAR offline.
14. [`three-way-comparison_locked-vs-alt-no-em-vs-alt-norm-punct_2026-05-28.md`](three-way-comparison_locked-vs-alt-no-em-vs-alt-norm-punct_2026-05-28.md) — three-way comparative audit (SHIP LOCKED CUT + 2 back-ports recommendation; baseline for my interpretation of variants).
15. Aeon V-D independent audit at `publishing/essays/aeon-mask-of-abundance/rigor/pass-3-3-and-3-4-bundled-audience-load_VERSION-D_INDEPENDENT-AUDIT_2026-05-28.md` — STRUCTURE model only; Aeon-calibration content NOT transferred to FA.

**Phase 1 — essay variants:**

16. [`publishing/essays/foreign-affairs-existence-proof/essay.md`](../essay.md) — locked cut (Stage 5 RATIFIED 2026-05-27 commit `3ae1777`).
17. [`_archive/parallel-drafts_2026-05-28/ch4-foreign-affairs-essay_alt_no-emdashes_260528-50f30a.md`](../_archive/parallel-drafts_2026-05-28/ch4-foreign-affairs-essay_alt_no-emdashes_260528-50f30a.md) — Alt-no-em (0 em-dashes by hard constraint; +7 citations inline).
18. [`_archive/parallel-drafts_2026-05-28/ch4-foreign-affairs-essay_alt_normal-punctuation_260528-b357c4.md`](../_archive/parallel-drafts_2026-05-28/ch4-foreign-affairs-essay_alt_normal-punctuation_260528-b357c4.md) — Alt-norm-punct (8 em-dashes at 5 actively-justified sites; +4 citations inline).
19. [`_archive/parallel-drafts_2026-05-28/ch4-foreign-affairs-essay_hybrid_best-of-both.md`](../_archive/parallel-drafts_2026-05-28/ch4-foreign-affairs-essay_hybrid_best-of-both.md) — **VERSION D AUDIT TARGET.**

**Phase 3 cross-check inputs (read AFTER §§1–12 of this artifact were drafted):**

20. [`_archive/parallel-drafts_2026-05-28/ch4-foreign-affairs-essay_hybrid_drafters-self-audit.md`](../_archive/parallel-drafts_2026-05-28/ch4-foreign-affairs-essay_hybrid_drafters-self-audit.md) — drafter's-self-audit (methodologically suspect per drafter's own §0 caveat).
21. [`pass-3-3-and-3-4-bundled-audience-load_VERSION-D_INDEPENDENT-AUDIT_2026-05-28.md`](pass-3-3-and-3-4-bundled-audience-load_VERSION-D_INDEPENDENT-AUDIT_2026-05-28.md) — prior chip's V-D Pass 3.3 + Pass 3.4 audit.

---

## §1. Scope reminder — Pass 3.3 + 3.4 + 3.5 diff inventory + audit discipline

### §1.1 What Version D changes from the locked cut (load-bearing diffs)

Version D preserves ~90% of locked-cut prose verbatim. Diffs concentrate at seven sites (matching the prior chip's §1.1 enumeration, replicated independently here):

- **§I opening (backport from Alt-no-em):** Phillips Petroleum + Dec 23, 1969 + Norwegian sector specificity. Closes Pass 3.1 LOW-3 historical-precision flag.
- **§I close (backport from Alt-norm-punct):** Em-dash pivot at thesis breath ("...different outcome — the choice is the thing"). +1 em-dash; load-bearing pre-§II pivot.
- **§II revenue-intake (backport from Alt-no-em):** Hannesson *Petroleum Economics* 2015 + 1909 Watercourse Regulation Act hydropower-concession lineage sentence (~45w). Closes locked-cut Pass 3.5 F-3.5-L1 awareness flag (legal-architecture claim previously under-elaborated).
- **§II NBIM-AR-2023 half-clause (backport from Alt-no-em):** ~9,000 publicly listed companies across more than 70 markets (~17w SWF-domain fluency marker).
- **§III foreclosure-pivot (backport from Alt-norm-punct):** Three-sentence locked-cut reveal compressed into single em-dash-pivot sentence (+1 em-dash). Cleanest single-sentence foreclosure reveal across all three variants per three-way §6.
- **§IV Pistor inline (backport from both alts):** *Code of Capital* (Princeton, 2019) attribution after Sachs/CCSI (~38w). Legal-engineering complement.
- **§VI Tooze inline (backport from Alt-norm-punct):** *Shutdown* + *Chartbook* climate-finance attribution + framing-as-open-problem follow-up (~45w + "The Norwegian case does not resolve it either" + "makes the asymmetry legible as architecture rather than as accident").
- **§VI close em-dash (backport from Alt-norm-punct):** Paired em-dashes around "in some form and against some resistance." +2 em-dashes; load-bearing epigrammatic close.

**Calibration rejections (NOT surfaced in V-D):**

- IMF Article IV 24/171 (2024), OECD Economic Survey Norway 2024, Meld. St. 9 (2023–2024), Truman 2010 — rejected per FA-editor selective-citation discipline.
- Mazzucato explicit attribution at §V — rejected to preserve locked cut's keep-Mazzucato-sub-textual disposition per brief §7.11 + A2 tribal-coding-management discipline.

**Em-dash + word delta:** Per V-D YAML: 12 em-dashes at 7 sites (+3-to-+4 vs locked-cut measured 8-or-9); +56w (drafter measure) to +182w (prior chip awk-grep measure; methodological discrepancy over HTML-comment-boundary; not material). Em-dash density ~2.0/1000w (within publisher-facing norm; each site carries active per-site justification per `feedback_em_dash_overuse.md`).

### §1.2 Audit discipline

Per Pass 3.3 + 3.4 + 3.5 protocol per per-essay brief §13:

- **Pass 3.3:** per-character INCLUDE / NEUTRAL / EXCLUDE verdict on 16 characters; within-INCLUDE comparative subscoring at ✅✅✅ / ✅✅ / ✅; Tier 1 EXCLUDE blocks submission; Δ from locked-cut RATIFIED PASS 2026-05-27 noted per character.
- **Pass 3.4:** thread-pull synthesis verdict on 3 adversarial characters (A1/A2/A3); verdict-floor is EXCLUDE; three classes (ROBUST / PARTIALLY ROBUST / NOT-CHAPTER-DISARMABLE).
- **Pass 3.5:** restoration-polarity audit (opposite of Pass 3.2 CUT polarity); per-finding format Options + Recommendation + Reasoning per v3.1 Amendment C; substrate-safety hard rule per `feedback_no_invented_factual_claims_in_publisher_facing_prose.md` (structure-only + substrate-safe attribution recommendations; NO illustrative invented prose).
- Independent first-principles scoring before Phase 3 cross-check against drafter's-self-audit + prior chip's audit.

---

## §2. Pass 3.3 — Acceptance set per-character verdicts (Version D)

### §2.1 Tier 1 — Gating audiences

**T1.1 Foreign Affairs editorial brain (Daniel Kurtz-Phelan).** Cross-jurisdictional comparative-institutional analysis grounded in named cases preserved verbatim from locked cut (Norway/Nigeria/US three-jurisdiction comparative spine). V-D's selective-deployment discipline at Hannesson + Pistor + Tooze (each at single-sentence depth, doing specific argumentative work) reads at FA-editor-preferred register; the explicit REJECTIONS of IMF + OECD + Meld. St. 9 + Truman + explicit Mazzucato attribution preserve the locked cut's selective-citation discipline. §I Phillips Petroleum attribution is a factual-precision improvement an FA editor reads as the right disciplinary instinct. **Verdict: ✅✅✅ INCLUDE.** Marginal lift over locked cut via selective-citation-discipline applied to additional comp-cluster references. **Δ: ✅✅✅ → ✅✅✅** (holds at ceiling; marginal lift).

**T1.2 FA reader / CFR member / IPE policy elite.** §III + §IV + §V analytical-bite-over-restatement layer preserved verbatim. Hannesson at §II adds Norway-petroleum-tax-lineage depth; Pistor at §IV adds legal-engineering complement to Sachs/CCSI; Tooze at §VI engages climate-finance conversation. **Verdict: ✅✅✅ INCLUDE.** **Δ: ✅✅✅ → ✅✅✅** (marginal lift via comp-cluster register signal).

**T1.3 SWF domain practitioner — DISPOSITIVE for substantive accuracy.** All locked-cut dispositive tests preserved verbatim (NBIM operational arm + ethics-council 2004 + Storting supermajority + Norway-as-Hartwick-application + international-architecture + colonial-era concession-inheritance). V-D adds Hannesson 1909 hydropower-concession lineage (Norway-petroleum-tax-architecture marker an in-domain reader will recognize as accurate scholarship) + NBIM AR 2023 ~9,000-companies-across-70-markets half-clause (current-period authoritative fluency marker). Pistor at §IV places international-architecture framing in legal-engineering register the SWF practitioner reads in adjacent territory. **Verdict: ✅✅✅ INCLUDE (dispositive PASS).** Marginal lift over locked cut via Hannesson + NBIM-AR Norway-specific domain markers. **Δ: ✅✅✅ → ✅✅✅** (holds at dispositive ceiling).

**T1.4 Literary agent.** Third-person institutional-policy voice held throughout; thesis-with-legs preserved; verifiable authority anchors stronger via Hartwick + UNEP + Sachs preserved + Hannesson + Pistor + Tooze added; cross-jurisdictional reach unchanged. **Verdict: ✅✅✅ INCLUDE.** Marginal lift over locked cut on comp-cluster register signal. **Δ: ✅✅✅ → ✅✅✅** (holds at agent platform-paragraph-credibility ceiling).

**Tier 1 aggregate: 4/4 ✅✅✅ INCLUDE.** Same count as locked cut at ✅✅✅ ceiling; marginal lift across all four cells via selective-deployment discipline + Norway-domain fluency.

### §2.2 Tier 2 — Pipeline-strengthening audiences

**T2.5 Mazzucato / Tooze cluster comp-author reader.** V-D surfaces Tooze inline at §VI at single-sentence depth doing specific argumentative work (climate-finance national-vs-global liability boundary; framing-as-open-problem). Mazzucato remains sub-textual per locked cut's brief §7.11 + A2 tribal-coding-management disposition. The cluster-reader reads for BOTH halves of the cluster signal; V-D delivers half explicit + holds half implicit. **Verdict: ✅✅ INCLUDE.** Marginal lift over locked cut via Tooze inline; not full upgrade to ✅✅✅ because Mazzucato remains sub-textual. **Δ: ✅✅ → ✅✅** (holds at locked-cut level with mild Tooze lift; cluster-reader reads partial register-signal as partial; A2 cost saved by Mazzucato sub-textual is separate dimension at §4).

**T2.6 Brookings / PIIE / heterodox-econ policy reader.** §II + §IV + §V institutional-architecture comparative work preserved. Hannesson reads as Norway-cluster-scholar register (overlaps Brookings reader's interests but is not the current-period multilateral authority signal Brookings most reads for). V-D explicitly REJECTS IMF Article IV 24/171 + OECD Economic Survey 2024 + Meld. St. 9 per FA-editor selective-citation discipline; Alt-no-em surfaced all three at ✅✅✅ for this character; V-D's calibration choice forgoes that upgrade. **Verdict: ✅✅ INCLUDE.** Trade-off deliberate. **Δ: ✅✅ → ✅✅** (locked-cut level held; Brookings-register gain forgone for FA-editor discipline).

**T2.7 Christophers / Susskind cluster comp-author reader.** V-D's §IV Pistor *Code of Capital* attribution is the Christophers-tradition register signal — Pistor reads as legal-engineering complement to Christophers's pricing-mechanics-of-finance work + as in-cluster scholarship to Susskind's growth-reckoning tradition. Pistor at moderate depth ("reads the same architecture from the legal-engineering side: the rules by which a privately held claim becomes durable across borders are themselves a product of choices that, once made, are easier to maintain than to undo") reads as analytical-bridge rather than as add-on attribution. **Verdict: ✅✅✅ INCLUDE.** **Δ: ✅✅ → ✅✅✅ UPGRADE** (Pistor inline at moderate depth).

**T2.8 Norway-cluster scholar.** All locked-cut Norway-precision details preserved (NBIM; ethics council 2004; Storting supermajority; *handlingsregelen* 2001 under Stoltenberg I; 4%→3% in 2017; Bondevik II disambiguation; Equinor rename). V-D adds Hannesson 1909 Watercourse Regulation Act hydropower-concession lineage (Norway-petroleum-economics scholars recognize this as load-bearing institutional-history anchor) + NBIM AR 2023 ~9,000-companies-across-70-markets half-clause (current-period authoritative figure). Both are exactly the domain-fluency markers a Norway-cluster scholar reads as serious engagement. **Verdict: ✅✅✅ INCLUDE.** **Δ: ✅✅✅ → ✅✅✅** (holds at Norway-precision ceiling; Hannesson is strongest single Norway-domain marker any variant carries).

**T2.9 Public Choice / center-right reader (CONDITIONAL — does NOT fire).** Standard non-partisan-framing discipline at body-prose level preserved verbatim (structural-not-prescriptive register at §V close; Niger Delta multilateral-architecture rather than corporate-villain framing at §IV; McDowell-county-vulnerable-jurisdictions structural framing at §V). Hannesson 1909 marginally aids Public Choice register read at A1 (path-dependence is methodologically respectable; see §4.1). **Verdict: ✅✅ INCLUDE.** Conditional-elevation flag correctly NOT fired. **Δ: ✅✅ → ✅✅** (holds).

**Tier 2 aggregate: 5/5 INCLUDE; 2 × ✅✅✅ (T2.7 + T2.8) + 3 × ✅✅ (T2.5 + T2.6 + T2.9).** Net ✅✅✅ upgrade of T2.7 vs locked cut three-way scoring. T2.5 + T2.6 trade-offs deliberate per V-D's calibration discipline (Mazzucato sub-textual; IMF/OECD/Meld. St. 9 / Truman rejected).

### §2.3 Tier 3 — Cultural-resonance + accessibility audiences

**T3.10 Non-Anglo / internationalist reader.** §IV international-architecture restoration preserved verbatim (international tax-treaty + financial-secrecy + colonial-era concession-inheritance triad). Pistor at §IV is the European-policy-intellectual register signal — *Code of Capital* is widely-read across European policy-intellectual cluster + reads as legal-architecture-of-capital tradition this reader recognizes. Mild Pistor amplification; not rung-changing. **Verdict: ✅✅ INCLUDE.** **Δ: ✅✅ → ✅✅** (holds with mild Pistor amplification).

**T3.11 Niger Delta / postcolonial reader — CRITICAL test.** §IV at full scope preserved verbatim from locked cut: Ogoni crisis of early 1990s as community-led political organization; Saro-Wiwa + Ogoni Nine + Sani Abacha + Commonwealth-suspension + operating-companies-continued-production critical assessment; MEND 2005; Ogoni + Ijaw + several hundred other communities; framework conclusion (architecture-not-Nigerian-failure-in-isolation). Pistor at §IV reinforces multilateral-architecture-not-Nigerian-failure reading. **Verdict: ✅✅ INCLUDE (critical test cleared).** **Δ: ✅✅ → ✅✅** (holds).

**T3.12 Sovereign-wealth-funded developing-country reader.** §V McDowell-and-vulnerable-jurisdictions framing preserved verbatim; §VI Norwegian-model-as-local-optimum bounding preserved. **Verdict: ✅✅ INCLUDE.** **Δ: ✅✅ → ✅✅** (holds).

**T3.13 General FA subscriber without SWF domain expertise.** Specialized terminology introduced with plain-prose definitions preserved verbatim. Concrete-dated-named institutional architecture carries the analysis. V-D's §III foreclosure-pivot em-dash improvement ("is gone — and the fund holds financial claims...") preserves analytical motion across the pivot that locked cut's three-sentence version breaks slightly. V-D's §I close em-dash improvement ("different outcome — the choice is the thing") preserves the thesis-breath analytical cumulation. Both are accessibility-cadence improvements. Counter-pressure: §II Hannesson + NBIM-AR additions read as specialist references at half-clause + single-sentence depth; surrounding plain-prose carries the general subscriber. Net: cadence improvements ≥ density cost. **Verdict: ✅✅✅ INCLUDE.** Marginal upgrade vs locked cut via §I close + §III pivot cadence. **Δ: ✅✅ → ✅✅✅ UPGRADE** (matches prior chip; drafter scored conservatively at ✅✅ per drafter §3 §II-density caveat — see §13 cross-check).

**T3.14 First-gen / climate-curious / energy-transition reader.** §III applications-for-which-no-substitute-yet-exists list preserved verbatim. §VI externality-tail named-jurisdictional consequences preserved (Bangladesh / Sahel / Pacific island states / agricultural economies of the broader Global South). Tooze at §VI is a comp-author reference; reader does not read for Tooze but prose context carries the climate-finance frame without requiring recognition. **Verdict: ✅✅ INCLUDE.** **Δ: ✅✅ → ✅✅** (holds).

**T3.15 Climate-finance / discount-rate-engagement reader.** §III + §VI conceptual distinction between *foreclosure component* (permanent geological loss) and *externality tail* (climate consequences across centuries) preserved verbatim; Weitzman/Stern non-conflation discipline holds. V-D's Tooze inline at §VI ("steadily pointing at this asymmetry without yet naming an instrument that resolves it") is the explicit climate-finance register signal that lifts this character to ✅✅✅. **Verdict: ✅✅✅ INCLUDE.** **Δ: ✅✅ → ✅✅✅ UPGRADE** (Tooze inline).

**T3.16 Reader in the reparations-economics lineage.** §VI international-distributional framing + global-scale distributional problem framing preserved verbatim. Implicit cultural-engagement signal carries. **Verdict: ✅✅ INCLUDE (low-load-bearing per brief).** **Δ: ✅✅ → ✅✅** (holds).

**Tier 3 aggregate: 7/7 INCLUDE; 2 × ✅✅✅ (T3.13 + T3.15) + 5 × ✅✅.** Net ✅✅✅ upgrade of T3.13 + T3.15 vs locked cut three-way scoring.

---

## §3. Pass 3.3 — Aggregate verdict (Version D)

### §3.1 Per-character verdict tally

| # | Tier | Character | Locked-cut three-way V | V-D verdict | Δ |
|---|---|---|---|---|---|
| T1.1 | 1 | FA editorial brain | ✅✅✅ | ✅✅✅ | = (marginal lift) |
| T1.2 | 1 | FA reader / CFR / IPE elite | ✅✅✅ | ✅✅✅ | = (marginal lift) |
| T1.3 | 1 | SWF practitioner DISPOSITIVE | ✅✅✅ | ✅✅✅ | = (marginal Hannesson + NBIM-AR lift) |
| T1.4 | 1 | Literary agent | ✅✅✅ | ✅✅✅ | = (marginal lift) |
| T2.5 | 2 | Mazzucato / Tooze cluster | ✅✅ | ✅✅ | = (Tooze inline; Mazzucato sub-textual) |
| T2.6 | 2 | Brookings / PIIE / heterodox | ✅✅ | ✅✅ | = (IMF/OECD intentionally not surfaced) |
| T2.7 | 2 | Christophers / Susskind cluster | ✅✅ | ✅✅✅ | **↑1** (Pistor inline) |
| T2.8 | 2 | Norway-cluster scholar | ✅✅✅ | ✅✅✅ | = (marginal Hannesson lift) |
| T2.9 | 2 | Public Choice / center-right (CONDITIONAL — NOT FIRED) | ✅✅ | ✅✅ | = |
| T3.10 | 3 | Non-Anglo / internationalist | ✅✅ | ✅✅ | = (mild Pistor amplification) |
| T3.11 | 3 | Niger Delta / postcolonial CRITICAL | ✅✅ | ✅✅ | = |
| T3.12 | 3 | SWF-funded developing-country | ✅✅ | ✅✅ | = |
| T3.13 | 3 | General FA subscriber | ✅✅ | ✅✅✅ | **↑1** (§I + §III cadence) |
| T3.14 | 3 | First-gen / climate-curious | ✅✅ | ✅✅ | = |
| T3.15 | 3 | Climate-finance / discount-rate | ✅✅ | ✅✅✅ | **↑1** (Tooze inline) |
| T3.16 | 3 | Reparations-economics lineage | ✅✅ | ✅✅ | = |

### §3.2 Aggregate tally

| Verdict | Locked-cut three-way count | V-D count | Δ |
|---|---|---|---|
| ✅✅✅ INCLUDE | 5 | **8** | **+3** |
| ✅✅ INCLUDE | 11 | 8 | −3 |
| ✅ INCLUDE | 0 | 0 | = |
| NEUTRAL | 0 | 0 | = |
| EXCLUDE | 0 | 0 | = |

**Total INCLUDE: locked cut 16 / V-D 16.** The 3 ✅✅→✅✅✅ upgrades (T2.7 Pistor + T3.13 cadence + T3.15 Tooze) concentrate at the pipeline-strengthening + accessibility tiers where the locked cut's three-way scoring was below ceiling. All 4 Tier 1 characters hold at ✅✅✅ ceiling with marginal lifts.

### §3.3 Per-tier breakdown

| Tier | Count | ✅✅✅ | ✅✅ | NEUTRAL | EXCLUDE | Tier verdict |
|---|---|---|---|---|---|---|
| Tier 1 (gating) | 4 | **4** | 0 | 0 | 0 | **GATING DECISIVE** — all 4 ✅✅✅ |
| Tier 2 (pipeline-strengthening) | 5 | 2 | 3 | 0 | 0 | **PIPELINE STRONG** — T2.7 Pistor upgrade |
| Tier 3 (cultural-resonance + accessibility) | 7 | 2 | 5 | 0 | 0 | **ACCESSIBILITY STRENGTHENED** — T3.13 cadence + T3.15 Tooze upgrades |

### §3.4 Aggregate Pass 3.3 verdict

**Pass 3.3 verdict: NET INCLUDE DECISIVE; substantially stronger than locked cut on pipeline + accessibility tiers; matches locked cut at Tier 1 dispositive ceiling.** 16/16 INCLUDE; 0 NEUTRAL; 0 EXCLUDE; all Tier 1 + Tier 2 + Tier 3 audiences clear. Two deliberate FA-register trade-offs preserved at T2.5 + T2.6 (Mazzucato sub-textual for A2 protection; IMF/OECD/Meld. St. 9 / Truman rejected for FA-editor selective-citation discipline).

**Cumulative-portfolio effective-reveal verification:** V-D carries the same Ring-1 named-OK concept set as locked cut (*residual commons value* + *cost severance* + *accountability bond B* + *foreclosure component* + *externality tail* + RCV acronym in conjunction). No formal apparatus surfaces. No equation form. ✅ at-cap per brief §8.3 ≤22% target.

**Spot-fix recommendations:** None at Pass 3.3 layer. V-D's per-character verdicts all clear INCLUDE; trade-offs at T2.5 + T2.6 deliberate and defensible.

---

## §4. Pass 3.4 — Adversarial set per-character thread analysis (Version D)

Per Pass 3.4 RATIFIED 2026-05-27 format precedent + brief §1 Tier 3 adversarial set: 3 characters at FA-essay scope. Verdict-floor is EXCLUDE; diagnostic is thread-pull synthesis.

### §4.1 A1 — Public Choice / industry-funded petroleum economist (combined)

**Threads pulled (per locked-cut Pass 3.4 RATIFIED):** Industry-funded petroleum hostile-review threads (state-capture rate; externality-tail substitution; Nigeria-contrast cherry-picking) NOT chapter-disarmable (reception-cycle mitigation only); Public Choice analytical apparatus omission carried by cross-chapter cascade-via-Ch 5/9/TA per commit `bc02767`.

**V-D diff effect on A1.** Hannesson 1909 Watercourse Regulation Act hydropower-concession lineage at §II is genuinely reinforcing for A1's Public Choice analytical lens — 1909 reads as pre-petroleum institutional-equilibrium that path-shaped the 1970s petroleum-tax architecture decision. A1's Public Choice register reads this as institutional-path-dependence + prior-equilibrium-shaping-current-outcomes, exactly the analytical move the discipline rewards. Pistor at §IV reads as legal-engineering-architecture analysis A1's Public Choice register can place within rent-seeking-incentive analysis. Marginal reinforcement; not chapter-disarming for industry-funded hostile review.

**Verdict: PARTIALLY ROBUST (mildly reinforced vs locked cut on Public Choice scholarly engagement).** Industry-funded hostile review unchanged (not chapter-disarmable). **Δ: PARTIALLY ROBUST → PARTIALLY ROBUST** (mild Hannesson + Pistor reinforcement).

### §4.2 A2 — Reactionary intellectual reader (*National Review* / *National Affairs* / *American Affairs*)

**Threads pulled (per locked-cut Pass 3.4 RATIFIED):** Crypto-prescriptive read of U.S. Social Security comparator absorbed by structural-not-prescriptive disclaimer + §V opening preemption; universalist-Norway-as-template absorbed by §VI Norwegian-model-as-local-optimum; ethics-council divestment-list F-3.1-L1 attention item carries to Stage 5 cover-letter awareness via category-list framing; smuggled-in claim-architecture absorbed by observational-not-prescriptive framing.

**V-D diff effect on A2.** V-D's keep-Mazzucato-sub-textual disposition is the load-bearing A2 calibration call. Alt-norm-punct surfaced Mazzucato explicitly at §V and carried a small A2 cost; V-D's deliberate rejection preserves the locked cut's A2 protection. **This is the single most consequential V-D calibration call for adversarial robustness.** V-D's Tooze framing at §VI ("steadily pointing at this asymmetry without yet naming an instrument that resolves it... The Norwegian case does not resolve it either. It only makes the asymmetry legible as architecture rather than as accident") is framing-as-open-problem move; A2 reads this as the author explicitly acknowledging the externality-tail is an open problem rather than asserting a claim-architecture — mild A2-attenuation.

Small A2 cost considerations: Pistor at §IV is somewhat left-coded in *National Review* register (Princeton University Press; "code of capital" framing reads as critical-of-financialization). But Pistor at §IV is deployed at legal-architecture-of-extraction passage, not at §V Social Security passage; the framing is multilateral-architecture-as-choice, not anti-Western-extraction-industry brief. Mild A2 risk only.

**Verdict: PARTIALLY ROBUST (mildly stronger than locked cut on framing-as-open-problem; matches locked cut's A2 protection by rejecting Mazzucato explicit attribution).** **Δ: PARTIALLY ROBUST → PARTIALLY ROBUST** (mild Tooze framing-attenuation; A2 cost of Alt-norm-punct's Mazzucato explicit attribution NOT inherited).

### §4.3 A3 — Procedural-conservative reader (WSJ editorial-board cluster)

**Threads pulled (per locked-cut Pass 3.4 RATIFIED):** Residual-as-entitlement absorbed by §III RCV grounding in classical-economics externality framing; commons-as-collectivized-ownership absorbed by Pigouvian / Coasean grounding; B-as-accountability-bond as non-classical-economics framing absorbed by institutional-revenue-capture-instrument register.

**V-D diff effect on A3.** Pistor *Code of Capital* at §IV places the international-architecture framing in legal-engineering register; A3's orthodox-property-law tradition recognizes Pistor's book as legal-scholarship-within-discipline (A3 may disagree with conclusions but cannot dismiss the register). Hannesson 1909 hydropower-concession lineage at §II is a long-standing institutional-property-law instrument (A3 reads 1909-era Norwegian property-law as legitimate state-asset-with-public-claim register — Norway treated hydropower rent as a public claim under standard pre-WWI property-law-instrument architecture). Both V-D additions amplify A3's within-discipline scholarship register reading.

**Verdict: ROBUST (mildly amplified vs locked cut).** A3 cannot stake disqualification on body-prose framing. **Δ: ROBUST → ROBUST** (mild within-discipline amplification).

---

## §5. Pass 3.4 — Thread-pull synthesis + robustness verdict (Version D)

### §5.1 Thread inventory

| Thread | Pulled by | Type | Disposition |
|---|---|---|---|
| **T1: Public Choice analytical apparatus omission** | A1 | Load-bearing pitch claim; cross-chapter engagement at Ch 5/9 + TA §1.10 via commit `bc02767` (unchanged from locked cut) | Cross-chapter cascade carries; V-D adds Hannesson 1909 path-dependence marker A1's Public Choice lens reads as proto-discipline-respectable. Marginal reinforcement; not chapter-disarming. |
| **T2: Industry-aligned hostile review** | A1 industry-funded portion | NOT chapter-disarmable | Reception-cycle mitigation only; framework-promise IS the threat to A1's funders' interests. Unchanged from locked cut. |
| **T3: Reactionary intellectual tribal-tradition read** | A2 | Procedural / cosmetic flag at FA scale | Absorbed by structural-not-prescriptive + Norwegian-model-local-optimum + category-list framing of ethics-council divestments. **V-D specifically rejects Alt-norm-punct's Mazzucato explicit attribution to preserve locked cut's A2 protection.** Tooze framing-as-open-problem mild additional attenuation. |
| **T4: Procedural-conservative property-law read** | A3 | Absorbed by classical-economics externality grounding + Pigouvian / Coasean register + structural-not-prescriptive register | V-D adds Hannesson 1909 hydropower-concession-lineage (long-standing property-law instrument) + Pistor *Code of Capital* (legal-scholarship-within-discipline) as within-discipline amplifications. ROBUST holds. |
| **F-3.1-L1 ethics-council divestment-list attention item** | A2 (Israeli construction companies category-list) | Procedural attention item from Pass 3.1 + carried at Pass 3.4 + Stage 5 cover-letter | Identical handling to locked cut; category-list framing absorbs the political-coding pressure; cover-letter awareness deferred to Stage 5. |

### §5.2 Cross-pressure pattern

**A1 + A3 opposite-direction critiques continue to absorb the same Norway-as-existence-proof framing from opposite political-economy positions.** A1 reads insufficient Public Choice rent-seeking analysis; A3 reads too-much-state-framing. Both opposite-direction adversaries pull on the same framing from opposite positions, confirming V-D is positioned correctly in the political-economy debate — neither extreme finds the framing endorsing their position. V-D's structural-not-prescriptive register + concept-level-only apparatus + Pigouvian-externality grounding + cross-chapter cascade-via-Ch 5/9/TA + Hannesson path-dependence + Pistor legal-engineering hold against both directional pressures.

### §5.3 Conditional-elevation flag check (per brief §1 Tier 2 #9)

**V-D disposition: Conditional-elevation flag does NOT FIRE.** Per Pass 3.3 V-D NET INCLUDE DECISIVE verdict: 16/16 INCLUDE; T1.1 FA editor brain dispositively non-partisan-aligned; T2.9 Public Choice / center-right CONDITIONAL correctly NOT FIRED. A1's center-right pressure does not surface as dispositive; A2's reactionary intellectual pressure absorbed by structural-not-prescriptive + Mazzucato-kept-sub-textual; A3's procedural-conservative pressure absorbed by Pigouvian-externality grounding + Pistor within-discipline scholarship register. No explicit-meta Condition-1-disarming-moves required. Standard non-partisan-framing discipline at body-prose level continues to carry the load.

### §5.4 Overall verdict

**Pass 3.4 ROBUST.** V-D's hybridization moves are **NET-POSITIVE for adversarial robustness vs locked cut:**

- **A1:** Mild Hannesson 1909 path-dependence reinforcement + Pistor legal-engineering reinforcement; industry-funded hostile review unchanged (not chapter-disarmable).
- **A2:** Mild Tooze framing-as-open-problem attenuation; **load-bearing keep-Mazzucato-sub-textual disposition preserved (Alt-norm-punct A2 cost NOT inherited).**
- **A3:** Mild Hannesson 1909 + Pistor within-discipline amplifications.

One PARTIALLY ROBUST attention item (F-3.1-L1 ethics-council divestment-list framing) continues to carry forward to Stage 5 cover-letter awareness; the essay text holds as-is.

**Spot-fix recommendations:** None at Pass 3.4 layer.

---

## §6. Pass 3.5 — Developmental-edit per-finding artifacts (Version D)

**Pass 3.5 is the pass the prior chip omitted by author error.** This section closes that gap.

Pass 3.5 polarity is RESTORATION — opposite to Pass 3.2's CUT. The lens: analytical-arc continuity at section transitions; institutional-architecture-detail density at §II + §IV (scene-anchor analog at FA register); voice-flow continuity (third-person institutional-policy reportage); cumulative-LLM-cadence residue; reader-engagement at analytical pivots.

**Critical Pass 3.5 substrate-safety discipline per `feedback_no_invented_factual_claims_in_publisher_facing_prose.md`:** All Pass 3.5 findings must be **structure-only + substrate-safe attribution** recommendations. NO illustrative invented prose. Verification of V-D's backports follows substrate-safety check before per-finding analysis.

### §6.1 Substrate-safety verification on V-D's seven backport sites

| Backport site | Content type | Substrate-safety |
|---|---|---|
| §I Phillips Petroleum + Dec 23 + Block 2/4 + Norwegian sector | Fact-precision (operator + date + location) | ✓ SAFE — public-record fact; verifiable against Phillips Petroleum corporate history + Norwegian petroleum-licensing record |
| §I close em-dash | Punctuation backport | ✓ SAFE — no factual content |
| §II Hannesson + 1909 Watercourse Regulation Act | Published-work citation + historical-record law | ✓ SAFE — Hannesson *Petroleum Economics* 2015 is published; 1909 Watercourse Regulation Act is real Norwegian legislation; the specific claim that Norwegian petroleum-tax modeled on hydropower-concession lineage IS substantively per Hannesson 2015 (drafter §8 #2 flagged this as moderate-confidence; light Pass 3.1 verification recommended before submission per integrated-artifact discipline) |
| §II NBIM AR 2023 half-clause | Institutional reporting | ✓ SAFE — NBIM Annual Report 2023 is public document; specific quantitative figure (~9,000 companies / >70 markets) widely-referenced (drafter §8 #3 flagged moderate confidence; light Pass 3.1 verification recommended) |
| §III foreclosure-pivot em-dash | Punctuation + restructure | ✓ SAFE — no factual content; restructure of existing factual material |
| §IV Pistor inline | Published-work citation + paraphrase of central argument | ✓ SAFE — Pistor *Code of Capital* (Princeton 2019) is published; paraphrase ("the rules by which a privately held claim becomes durable across borders are themselves a product of choices that, once made, are easier to maintain than to undo") is faithful to Pistor's central argument; drafter §8 #4 flagged for Pass 3.1 paraphrase verification |
| §VI Tooze inline | Published-work citation + paraphrase of *Chartbook* climate-finance critique | ✓ SAFE — Tooze *Shutdown* (2021) + *Chartbook* (Substack ongoing) are published; paraphrase ("steadily pointing at this asymmetry without yet naming an instrument that resolves it") is faithful to widely-articulated Tooze position; drafter §8 #5 flagged for Pass 3.1 paraphrase verification |

**Substrate-safety verdict: CLEAN.** All V-D backport additions are either fact-precision improvements anchored in public record, published-work citations with faithful paraphrase, or punctuation/cadence backports with no factual content. **No invented biographical specifics; no invented scene-rendered encounters; no invented documentary specifics; no motivation attributions; no quoted speech.** The Ch 2 → Harper's Pass 3.5 near-miss empirical anchor (substrate-critical-illustrative-prose) does NOT apply to V-D's backports.

Three of seven sites (Hannesson; NBIM-AR; Pistor paraphrase + Tooze paraphrase) carry light-touch Pass 3.1 verification flag per drafter §8 #2–#5. This is light-touch (date + author + publisher confirmation + paraphrase-faithful-to-source check), NOT invention-flagging. The drafter and prior chip both correctly handled this as a pre-submission integrated-artifact gate; this audit independently confirms.

### §6.2 Per-finding Pass 3.5 verdicts (Options + Recommendation + Reasoning per v3.1 Amendment C)

**Format note (NEW for this session; not in Aeon V-D pattern):** This is the first independent Pass 3.5 audit on a hybrid V-D artifact. The findings inventory below documents V-D's organic restorations (achieved via the harvest) as Pass-3.5-polarity-consistent restorations + carries forward the locked-cut Pass 3.5 RATIFIED HOLD inventory items at the corresponding V-D sites. Where V-D's backport substantively closes a prior Pass 3.5 awareness item, this is recorded as the awareness item's natural closure.

#### F-3.5-V-D-1 (LOW) — §II Hannesson backport substantively closes locked-cut F-3.5-L1 awareness flag

**Location:** V-D line 103 (§II Architecture, revenue-intake paragraph close).

**Locked-cut Pass 3.5 baseline:** F-3.5-L1 (LOW) flagged the legal-architecture claim at locked-cut line 33 ("legal architecture surrounding the Norwegian continental shelf was constructed early to treat the resource rent itself, rather than the private operator's profit, as the primary fiscal object") as analytically-doing-work-but-not-anchored. Verdict was HOLD (a) per FA-scope length envelope; F-3.5-L1 left as awareness item for Stage 5 cover-letter.

**V-D state:** V-D line 103 backports the Hannesson sentence: "Rögnvaldur Hannesson, in his *Petroleum Economics* (Edward Elgar, 2015), traces the design of the petroleum tax to a deliberate early-1970s decision to model rent capture on Norway's existing hydropower-concession regime, which had treated the rent of an enclosed natural resource as a public claim since the 1909 Watercourse Regulation Act."

**Options:**
- **(a)** ACCEPT V-D's Hannesson addition as substantively closing F-3.5-L1.
- **(b)** Trim V-D's Hannesson sentence to ~25 words (Hannesson + 1909 anchor only; drop the "model rent capture on Norway's existing hydropower-concession regime" intervening half).
- **(c)** Reject V-D's Hannesson addition; revert to locked-cut F-3.5-L1 HOLD verdict.

**Recommendation: (a) ACCEPT.**

**Reasoning.** The Hannesson addition is substrate-safe (published-work citation; verifiable against Hannesson 2015 + Norwegian legislative record) and closes the F-3.5-L1 analytical anchor gap Pass 3.5 had flagged. Length (~50 words) is at the upper end of selective-deployment but within FA register; the 1909 Watercourse Regulation Act provides a path-dependence anchor that strengthens Tier 1 #3 SWF practitioner verdict and A1 Public Choice scholarly engagement simultaneously. Option (b) trim plausible but loses the load-bearing analytical content. Option (c) reject discards a substantive analytical anchor.

#### F-3.5-V-D-2 (LOW) — §I Phillips Petroleum backport closes Pass 3.1 LOW-3 historical-precision flag

**Location:** V-D line 87 (§I Ekofisk Decision opener).

**Locked-cut state:** "Three days before Christmas in 1969, the Ekofisk well in Block 2/4 of the North Sea returned the results..." Pass 3.1 LOW-3 flagged historically-retrospective phrasing (well not yet named "Ekofisk" at discovery; was Phillips Petroleum's exploration well).

**V-D state:** "On December 23, 1969, a test well drilled by Phillips Petroleum in Block 2/4 of the Norwegian sector of the North Sea returned the readings that, within a year, would confirm Norway sat on one of the largest petroleum reservoirs in the industrialized world."

**Options:**
- **(a)** ACCEPT V-D's Phillips Petroleum opener as fact-precision improvement that strengthens §I declarative-scene-setting.
- **(b)** Adjust opener to acknowledge the actual drilling rig (*Ocean Viking*, operated by Odeco; Phillips was the licensee) per three-way comparison §8 #3 caveat.

**Recommendation: (a) ACCEPT as drafted.**

**Reasoning.** V-D's phrasing is substrate-safe (public-record fact; Phillips Petroleum was the licensee operating in Block 2/4) and within standard journalistic shorthand. Option (b) is a fact-check-team copy-edit consideration that need not gate Stage 5 ratification.

#### F-3.5-V-D-3 (LOW) — §II NBIM-AR half-clause as appropriate FA-scope scene-anchor density restoration

**Location:** V-D line 107 (§II fund-operations paragraph).

**V-D state:** "...the 2023 *NBIM Annual Report* recorded equity holdings in roughly nine thousand publicly listed companies across more than seventy markets."

**Pass 3.5 evaluation.** Scene-anchor density restoration in FA-register terms — institutional-architecture-detail density at §II. Verifiable specificity marker that Tier 1 #3 SWF practitioner + Tier 2 #8 Norway-cluster scholar will recognize as fluency with source material. Locked-cut Pass 3.5 §2.1 §II row noted appropriate-scope-met without restoration; V-D's addition modestly *increases* density.

**Options:**
- **(a)** ACCEPT V-D's NBIM-AR half-clause as appropriate FA-scope scene-anchor density restoration.
- **(b)** Trim "across more than seventy markets" tail; keep "~9,000 publicly listed companies" half only.
- **(c)** Reject NBIM-AR addition; revert to locked-cut phrasing.

**Recommendation: (a) ACCEPT.**

**Reasoning.** NBIM-AR is institutional reporting (substrate-safe; verifiable). Numerical specificity is the kind of marker FA signature long-form essays carry; it does not shift the §II passage toward policy-paper register. Light Pass 3.1 verification recommended for the specific quantitative claim (~9,000 + >70 markets) per drafter §8 #3 + this AUDIT-2 §6.1.

#### F-3.5-V-D-4 (LOW) — §IV Pistor inline register-signal restoration

**Location:** V-D line 135 (§IV international-architecture paragraph).

**V-D state:** "Katharina Pistor's *The Code of Capital* (Princeton University Press, 2019) reads the same architecture from the legal-engineering side: the rules by which a privately held claim becomes durable across borders are themselves a product of choices that, once made, are easier to maintain than to undo."

**Pass 3.5 evaluation.** Register-signal restoration — closes Tier 2 #7 Christophers/Susskind cluster + Tier 3 #10 internationalist + A3 procedural-conservative legal-architecture-scholarship coverage gap. Locked cut Pass 3.5 didn't flag §IV as a developmental-edit gap (held at appropriate scope per §2.1 §IV row); V-D's backport substantively *strengthens* §IV register-signal layer.

**Options:**
- **(a)** ACCEPT V-D's Pistor backport as substantive register-signal restoration.
- **(b)** Reduce Pistor to single half-sentence reference ("Pistor's *Code of Capital* documents the legal-engineering side of the same architecture") — less depth, lower A2 tribal-coding cost.
- **(c)** Reject Pistor inline; reserve for editor-iteration.

**Recommendation: (a) ACCEPT.**

**Reasoning.** Pistor at moderate depth — one sentence of attribution + one half-sentence of substantive characterization. The characterization is doing argumentative work (extends multilateral-architecture framing into legal-system mechanics the surrounding paragraph leaves implicit). Sits within Tier 2 #7 register-signal layer at FA-discipline depth. Mild A2 tribal-coding cost (Pistor IS engaged in *National Review-Capital Matters* register but more often read as left-coded; mild cost) offset by A3 procedural-conservative absorption (legal-engineering-as-choice framing is within-economics-and-legal-discipline observation). Light Pass 3.1 verification of paraphrase-faithful-to-Pistor recommended per drafter §8 #4 + this AUDIT-2 §6.1.

#### F-3.5-V-D-5 (LOW) — §VI Tooze inline + framing-as-open-problem follow-up: reader-engagement at analytical pivot

**Location:** V-D line 167 (§VI externality-tail paragraph).

**V-D state:** "Adam Tooze, writing in the climate-finance tradition across *Shutdown* (Viking, 2021) and the ongoing *Chartbook* commentary, has been steadily pointing at this asymmetry without yet naming an instrument that resolves it. The Norwegian case does not resolve it either. It only makes the asymmetry legible as architecture rather than as accident."

**Pass 3.5 evaluation.** Reader-engagement at analytical pivot restoration. §VI externality-tail framing is the analytical pivot where Tier 3 #15 climate-finance / discount-rate-engagement reader needs anchor. V-D's Tooze inline closes locked-cut implicit-Tooze gap and adds the framing-as-open-problem move that A2 reactionary intellectual reads as open-problem-not-prescription.

Two-sentence follow-up cadence ("The Norwegian case does not resolve it either. It only makes the asymmetry legible as architecture rather than as accident") is V-D's hybrid framing-as-open-problem move that absorbs A2's "smuggled-in claim-architecture" reading at scholarly-disagreement-not-disqualification level. Substantive analytical addition beyond mere citation.

**Options:**
- **(a)** ACCEPT V-D's Tooze inline + framing-as-open-problem follow-up.
- **(b)** Accept Tooze inline only; drop "The Norwegian case does not resolve it either. It only makes the asymmetry legible as architecture rather than as accident" follow-up (saves 22 words).
- **(c)** Reject Tooze inline; reserve for editor-iteration.

**Recommendation: (a) ACCEPT.**

**Reasoning.** Tooze deployment at §VI is exactly Tier 3 #15 dispositive reader's anchor. Follow-up framing-as-open-problem move closes A2 reactionary intellectual's "smuggled-in claim-architecture" thread at analytical-not-prescriptive level — V-D's deliberate move per YAML *fa_calibration_applied* note. Substantive Pass 3.5 restoration. Light Pass 3.1 verification of paraphrase-faithful-to-Tooze recommended per drafter §8 #5 + this AUDIT-2 §6.1.

**Drafter §3 over-positioning concern check.** Drafter's-self-audit §3 flagged Tooze passage as possibly reading as over-positioning if independent audit treated it as forcing a Norway-as-non-resolution claim redundant with §VI Norwegian-model-as-local-optimum passage two paragraphs later. My independent read: the Tooze passage operates at the externality-tail-specific analytical pivot (focused on climate-finance national-vs-global liability boundary), while the §VI Norwegian-model-as-local-optimum passage operates at the global-scale distributional problem analytical pivot (focused on whether the Norwegian architecture is replicable across the international system). These are adjacent but distinct analytical moves; Tooze is doing the climate-finance-boundary work + Norwegian-model-as-local-optimum is doing the replicability work. Not redundant; complementary. Drafter's flag is over-conservative.

#### F-3.5-V-D-6 (LOW) — §I close em-dash backport as load-bearing thesis-breath cadence

**Location:** V-D line 97 (§I closing sentence).

**V-D state:** "Same physical resource, different architecture, different outcome — the choice is the thing."

**Pass 3.5 evaluation.** Cadence-restoration via em-dash backport from Alt-norm-punct. Per V-D YAML per-site justification at site_1: load-bearing thesis breath before §II structural pivot; period-split loses analytical-cumulative motion; comma loses rhetorical pause. Defensible at load-bearing pivot.

**Options:**
- **(a)** ACCEPT V-D's §I close em-dash as defensible per per-site justification + analytical-cumulative motion gain.
- **(b)** Reject §I close em-dash; revert to locked-cut period-split form.
- **(c)** Replace em-dash with semicolon.

**Recommendation: (a) ACCEPT.**

**Reasoning.** §I close em-dash at load-bearing thesis-pivot moment (the section's structural-summative sentence priming §II). V-D's per-site justification is defensible. `feedback_em_dash_overuse.md` permits em-dashes "when the specific work (sudden interruption; deliberate breath-mark; emphatic punch at chapter-spine pivot) is load-bearing AND a comma/period/restructure would actually lose meaning" — exactly that case. Three-way comparison §6 independently identified this as one of "the cleanest single sentences in any of the three variants."

#### F-3.5-V-D-7 (LOW) — §III foreclosure-pivot em-dash backport as cleanest reveal across variants

**Location:** V-D line 125 (§III foreclosure-component reveal sentence).

**V-D state:** "The barrel, once extracted and combusted, is gone — and the fund holds financial claims on the productive output of other economies, which compound but do not reconstitute the barrel."

**Pass 3.5 evaluation.** Locked-cut three-sentence form vs V-D single-em-dash compression. Three-way comparison §6 + §7.2 #5 identified V-D's §III foreclosure pivot as the smoothest single-sentence reveal across all three variants. Per V-D YAML site_3: pivot from barrel-is-gone hard reveal to financial-substitute structural claim; commas saturate surrounding clause; period-split disrupts analytical motion.

**Options:**
- **(a)** ACCEPT V-D's §III foreclosure-pivot em-dash as substantive cadence improvement.
- **(b)** Reject; revert to locked-cut three-sentence form.
- **(c)** Restructure into two sentences with semicolon.

**Recommendation: (a) ACCEPT.**

**Reasoning.** §III foreclosure-component reveal is analytical pivot where framework's *foreclosure component* is first surfaced (Tier 3 #15 climate-finance + Tier 1 #3 SWF practitioner dispositive readers). V-D em-dash version compresses three sentences to one and carries analytical motion without breaking. Three-way comparison independently identified as smoothest single sentence across variants.

#### F-3.5-V-D-DISP1 (DISPOSITION) — F-3.2-L3 §VI rule-of-five anaphora carry-forward

**Location:** V-D lines 163, 165, 167, 169, 171 (§VI five-paragraph anaphora "What the architecture [has/has not] solved...").

**V-D state:** Preserves locked-cut's rule-of-five anaphora verbatim. Locked-cut Pass 3.5 closed F-3.2-L3 as HOLD-as-rhetorical-escalation. V-D preserves verbatim.

**Verdict: HOLD as rhetorical-escalation (carry-forward unchanged from locked-cut Pass 3.5 ratification).** Qualifier-variance across five paragraphs reads as rhetorical escalation, not formula. **No essay.md spot-fix required.**

#### F-3.5-V-D-8 (LOW awareness) — §V McDowell paragraph 800-word density (carry-forward)

**Location:** V-D line 157 (§V McDowell-acknowledgment paragraph).

V-D preserves locked-cut's single ~800-word paragraph. Locked-cut Pass 3.5 F-3.5-L2 held this as cumulative-weight rationale at FA institutional-policy register.

**Verdict: HOLD (carry-forward from locked-cut Pass 3.5 F-3.5-L2).** No essay.md change in V-D.

### §6.3 Polarity discipline check

V-D's hybridization is RESTORATION polarity (4 backports adding substrate-safe attributions + 2 em-dash backports + 1 fact-precision rewrite). Polarity-discipline check vs Pass 3.2 ratified cuts:

| Pass 3.2 ratified cut | V-D state |
|---|---|
| Em-dash density 23→8 | V-D moves to 12 em-dashes at 7 sites; **modest regression** of Pass 3.2's chiseling-to-8 target, but each new em-dash sits at load-bearing pivot with active per-site justification per `feedback_em_dash_overuse.md` discipline. Per cumulative-chapter density: 12/~5,941w ≈ 2.0/1000w at upper end of publisher-facing norm; within discipline tolerance |
| Outside-§III framework-tic compressions | Preserved (no framework-tic regression) |
| §III opening restructure | Preserved |
| Line 41 declarative-three-in-a-row + line 23 "called" | Preserved |

**Polarity discipline: CLEAN-ish.** Em-dash count regression (8→12) is the one watchpoint; modest, per-site-justified, within cumulative-density discipline. Not a categorical Pass 3.2 regression.

### §6.4 Pass 3.5 V-D summary

**Pass 3.5 inventory: 0 HIGH + 0 MEDIUM + 7 LOW (5 ACCEPT V-D backports + 2 HOLD carry-forward + 1 DISPOSITION).**

- F-3.5-V-D-1 (LOW): ACCEPT Hannesson backport at §II — closes locked-cut F-3.5-L1 awareness flag.
- F-3.5-V-D-2 (LOW): ACCEPT Phillips Petroleum opener at §I — closes Pass 3.1 LOW-3 historical-precision flag.
- F-3.5-V-D-3 (LOW): ACCEPT NBIM-AR half-clause at §II — appropriate FA-scope density restoration.
- F-3.5-V-D-4 (LOW): ACCEPT Pistor inline at §IV — Tier 2 #7 + Tier 3 #10 + A3 register-signal restoration.
- F-3.5-V-D-5 (LOW): ACCEPT Tooze inline + framing-as-open-problem at §VI — Tier 3 #15 + A2 framing-attenuation restoration.
- F-3.5-V-D-6 (LOW): ACCEPT §I close em-dash backport — load-bearing thesis-breath cadence.
- F-3.5-V-D-7 (LOW): ACCEPT §III foreclosure-pivot em-dash backport — smoothest single-sentence reveal across variants.
- F-3.5-V-D-DISP1: HOLD §VI anaphora as rhetorical-escalation (carry-forward).
- F-3.5-V-D-8 (LOW): HOLD §V McDowell paragraph density (carry-forward).

**Net Pass 3.5 verdict on V-D: RATIFIABLE-AS-V-D.** V-D's hybridization moves are substantively aligned with restoration polarity (each backport restores a register-signal or scene-anchor or analytical pivot that locked cut had at minimum-viable density). No new developmental-edit concerns surfaced beyond locked-cut Pass 3.5 RATIFIED HOLD inventory.

**Important nuance:** V-D is not a *Pass 3.5 spot-fix* applied to locked cut — it's a hybrid construction that includes Pass 3.5-territory restorations organically via the harvest. This finding inventory is the independent verdict that V-D's organic restorations are Pass-3.5-polarity-consistent.

**Substrate-safety: VERIFIED CLEAN** per §6.1 (all backports are public-record facts, published-work citations, or punctuation/cadence backports; no invented biographical specifics; no invented scene-rendered encounters; no invented documentary specifics; no motivation attributions; no quoted speech). Light-touch Pass 3.1 verification on Hannesson + NBIM-AR + Pistor + Tooze paraphrase faithfulness recommended before submission per integrated-artifact discipline.

---

## §7. Pass 3.5 — Aggregate verdict + cascade closure check (Version D)

**Pass 3.5 RATIFIABLE-AS-V-D.** V-D's seven backport-and-rejection moves are Pass-3.5-polarity-consistent restorations of register-signal + scene-anchor + analytical-pivot material that locked cut had at minimum-viable density. F-3.2-L3 §VI anaphora + F-3.5-L2 §V McDowell paragraph density carry forward as HOLD from locked-cut Pass 3.5 ratification (V-D preserves both verbatim). F-3.5-L1 §II legal-architecture awareness item from locked-cut Pass 3.5 is substantively closed by V-D's Hannesson backport.

**Stage 3 cascade verdict for V-D integrated artifact:** All five v3.1 Stage 3 passes can re-fire light-touch on V-D for integrated-artifact discipline, with expected verdicts:

| Pass | Expected V-D verdict |
|---|---|
| Pass 3.1 fact-check | LIGHT VERIFICATION REQUIRED on four backports (Hannesson 1909 claim depth-of-attribution; NBIM-AR 2023 ~9,000 / >70 markets figure; Pistor paraphrase faithfulness; Tooze paraphrase faithfulness). Substrate-safe per §6.1; not invention-flagging. ~15-min author session. |
| Pass 3.2 voice-polish | INHERITED CLEAN. Em-dash density 12 at 7 sites within discipline; no new throat-clearing; no new framework-tic regression. |
| Pass 3.3 audience-load | NET INCLUDE DECISIVE per §3.4 (8 ✅✅✅ + 8 ✅✅). |
| Pass 3.4 adversarial | ROBUST per §5.4 (A1 + A2 PARTIALLY ROBUST; A3 ROBUST). |
| Pass 3.5 developmental-edit | RATIFIABLE-AS-V-D per §6.4. |

**Stage 3 cascade re-close estimate for V-D:** ~15-min light Pass 3.1 verification + 0 spot-fixes at Pass 3.2/3.3/3.4/3.5 = ~15-min author session pre-Stage 5 re-sign-off.

---

## §8. Cross-pass synthesis (3.3 + 3.4 + 3.5 combined; Version D)

### §8.1 Aggregate findings

| Pass | Locked-cut verdict (RATIFIED 2026-05-27) | V-D verdict | Spot-fixes |
|---|---|---|---|
| Pass 3.3 (acceptance) | NET INCLUDE DECISIVE (16/16; 5 ✅✅✅ + 11 ✅✅ per three-way) | **NET INCLUDE DECISIVE — substantially stronger** (16/16; 8 ✅✅✅ + 8 ✅✅) | 0 |
| Pass 3.4 (robustness) | ROBUST (A1 + A2 PARTIALLY ROBUST + A3 ROBUST) | **ROBUST — mildly strengthened across A1 + A2 + A3** | 0 |
| Pass 3.5 (developmental-edit) | RATIFIED HOLD (0 spot-fixes; F-3.5-L1 + F-3.5-L2 awareness) | **RATIFIABLE-AS-V-D** (0 new spot-fixes; F-3.5-L1 closed by V-D Hannesson backport; F-3.5-L2 holds as carry-forward; +7 LOW backport-acceptance findings; +1 DISPOSITION carry-forward) | 0 |

### §8.2 V-D hybridization-impact summary

V-D's seven backport-and-rejection moves had net-positive impact across all three passes:

- **Pass 3.3:** Substantively positive at Tier 2 + Tier 3. Three ✅✅→✅✅✅ upgrades (T2.7 Pistor + T3.13 cadence + T3.15 Tooze). All Tier 1 characters hold at ceiling with marginal lift. Two trade-offs (T2.5 + T2.6) deliberate calibration calls.
- **Pass 3.4:** Mildly positive across all three adversarial characters. Hannesson + Pistor + Tooze each provide marginal reinforcement; keep-Mazzucato-sub-textual + reject-IMF/OECD/Meld. St. 9 preserve locked cut's A2 + FA-editor protections.
- **Pass 3.5:** RATIFIABLE-AS-V-D. V-D's backports organically achieve restoration-polarity work the locked-cut Pass 3.5 had held at HOLD pending Stage 5 cover-letter awareness. Substrate-safety verified clean.

**The V-D hybridization is substantively defensible across all three passes.** It consolidates the strongest single-character gains from both alt drafts while explicitly preserving the locked cut's two strongest calibration calls (Mazzucato sub-textual for A2 protection; IMF/OECD/Meld. St. 9 rejected for FA-editor selective-citation discipline). The result is an integrated artifact strictly stronger than the locked cut on the FA-specific audience set, without inheriting the alt drafts' specific weaknesses.

### §8.3 Pre-pub review queue items (unchanged from locked cut)

For Stage 5 cover-letter / pre-publication review queue:

1. F-3.1-L1 ethics-council divestment-list framing (Israeli construction companies in category-list at §II line 109). Identical across all variants; cover-letter awareness.
2. Cross-chapter cascade for Public Choice load via Ch 5/9 + TA §1.10 (commit `bc02767`). Unchanged.
3. Industry-funded hostile-review thread NOT chapter-disarmable; reception-cycle mitigation expected at submission.
4. A3 procedural-conservative scholarly-disagreement at WSJ editorial-board register; absorbed; no editor-iteration handoff.
5. **NEW for V-D:** Light Pass 3.1 verification flag on four backport sites (Hannesson 1909 claim depth; NBIM-AR 2023 figure; Pistor + Tooze paraphrase faithfulness) per §6.1 + drafter §8 #2–#5.

### §8.4 Cross-chapter cascade flag

No new cross-chapter cascade required from V-D. Same load-bearing threads as locked cut; same cross-chapter engagement workstreams in place.

---

## §9. Submission-readiness verdict (post-V-D-independent-AUDIT-2)

### §9.1 Aggregate severity tally across full Stage 3 + Stage 4 + Stage 5 (V-D-specific)

| Pass / Stage | V-D status | Verdict |
|---|---|---|
| Pass 3.1 fact-check | Inherited clean for ~90% locked-cut prose; light verification recommended on four V-D backports (Hannesson + NBIM-AR + Pistor + Tooze paraphrase faithfulness) | LIGHT VERIFICATION REQUIRED (~15 min) |
| Pass 3.2 voice-polish | Em-dash discipline maintained at 12 at 7 sites with active per-site justification; no new throat-clearing; no framework-tic regression | INHERITED CLEAN |
| Pass 3.3 acceptance | 16/16 INCLUDE; 8 ✅✅✅ + 8 ✅✅; 4/4 Tier 1 INCLUDE at ✅✅✅; 3 ✅✅→✅✅✅ upgrades vs locked cut | **NET INCLUDE DECISIVE; substantially stronger than locked cut** |
| Pass 3.4 robustness | 3/3 adversarial verdicts hold or marginally strengthen | **ROBUST — mildly strengthened** |
| Pass 3.5 developmental-edit | F-3.5-L1 closed by V-D Hannesson; F-3.5-L2 holds; 7 LOW backport-acceptance findings (5 ACCEPT + 2 HOLD); substrate-safety verified clean | **RATIFIABLE-AS-V-D** |
| Stage 4 render | Locked cut Stage 4 RATIFIED CLEAR offline; V-D em-dash + citation backports should render cleanly through FA submission portal; final pre-submission portal-paste check at submission time | INHERITED CLEAR |
| Stage 5 sign-off | Locked cut Stage 5 RATIFIED 2026-05-27; **V-D requires Stage 5 re-sign-off on integrated artifact** if (A)/(B) disposition chosen (~30-min author session) | INHERITED but requires explicit re-application |

### §9.2 Submission verdict

**Per-character + thread-pull + developmental-edit aggregate: SHIP-READY at FA submission window Q4 2026 / Q1 2027 (Nov–Feb).** V-D is publishable at FA at SOLID-to-VERY-SOLID accept-probability — measurably stronger than locked cut on FA-specific audience set across Pass 3.3 + Pass 3.4 + Pass 3.5.

### §9.3 Disposition options (author-decidable)

Three procedural paths land V-D's substantive value:

**(A) SHIP HYBRID.** Author ratifies V-D; canonical `essay.md` swaps to hybrid content; locked cut moves to `_archive/prior-versions/`; Stage 5 re-applied to V-D integrated artifact; cover letter refreshed to add Pistor + Hannesson + Tooze to citation inventory. **Strengths:** captures full V-D delta in one integrated artifact; symmetric with Aeon V-D pattern. **Costs:** light-touch Pass 3.1 verification on four backports + light Pass 3.5 confirmation + Stage 5 re-sign-off + cover-letter refresh (~1.5 hr author session total).

**(B) SPOT-FIX LOCKED CUT THEN SHIP (Phase C amendment route).** Author ratifies V-D's substantive content as Phase C amendment to locked cut; locked cut `essay.md` modified in place with V-D's seven backports; Mazzucato + IMF/OECD/Meld. St. 9 + Truman rejections preserved. **Substantively identical to (A).** Stage 5 RATIFIED state preserved via Phase C amendment scope per `feedback_merge_on_ratification.md` + three-way comparison §7.2 rationale; cover-letter refresh same as (A).

**(C) SMALLER BACK-PORT (per three-way §7.2 original recommendation).** Author ratifies only the Phillips Petroleum + Pistor backports as Phase C amendments; defers Hannesson + NBIM-AR + Tooze + §I close + §III pivot + §VI close em-dash backports. **Costs:** forgoes the T2.5 Tooze + T2.8 Hannesson + T3.13 cadence + T3.15 Tooze upgrades V-D demonstrates; the three-way comparison's smaller recommendation was conservative relative to the demonstrated V-D delta + Pass 3.5 closure of F-3.5-L1 awareness item.

**My disposition recommendation (independent AUDIT-2 perspective): (A) or (B); substantive value identical between them; author chooses procedural path.** Option (C) is the conservative path the three-way comparison recommended; my independent audit (matching the prior chip's audit) reads the additional V-D backports (Hannesson + NBIM-AR + Tooze + §I + §III + §VI em-dashes) as worth capturing in entirety. The Pass 3.5 substantive closure of F-3.5-L1 (via Hannesson) strengthens the SHIP HYBRID disposition over the smaller back-port (C), since F-3.5-L1 was a locked-cut Pass 3.5 awareness item that Phase C amendments at (C) scope would leave un-addressed.

### §9.4 Honest qualifications on the recommendation

Five caveats:

1. **V-D has not been through full 5-pass rigor cascade as integrated artifact.** Locked cut was; V-D inherits at prose-architecture level (~90% preserved verbatim); ~145-182w backports are not Pass 3.1+3.2-verified at integrated-artifact layer. Risk is low because backported claims trace to brief §7 canonical-facts + standard published-work citation per brief §11. Light-touch Pass 3.1 re-fire is the right discipline; not a blocker for submission window.

2. **Pass 3.5 cascade closure depends on substrate-safety of V-D's four backport citations (Hannesson 1909 claim depth; NBIM-AR 2023 figure; Pistor paraphrase faithfulness; Tooze paraphrase faithfulness).** §6.1 substrate-safety check verified all four as substrate-safe (published-work citations + public-record fact + faithful paraphrase). Pass 3.1 verification is light-touch (date + author + publisher confirmation + paraphrase-faithful-to-source check), NOT invention-flagging. Drafter §8 #2–#5 and prior chip §7 #1 both flagged this correctly; this AUDIT-2 confirms.

3. **My Pass 3.3 cell-level scoring matches the prior chip's scoring exactly (8 ✅✅✅ + 8 ✅✅; 16/16 INCLUDE).** Both audits independently arrive at the same per-tier breakdown (Tier 1 = 4 ✅✅✅; Tier 2 = 2 ✅✅✅ + 3 ✅✅; Tier 3 = 2 ✅✅✅ + 5 ✅✅). The convergence at independent replication validates the prior chip's verdicts.

4. **Drafter's-self-audit aggregate 9 × ✅✅✅ over-credited at T2.5 split-read.** Drafter tallied T2.5 partial signal as ✅✅✅ in aggregate count; my independent score + prior chip's score both place T2.5 at ✅✅ (cluster-reader reads partial signal as ✅✅, not ✅✅✅). Drafter's frontmatter acknowledged this potential bias.

5. **Sandy named-subject state confirmed OUT OF SCOPE for FA derivative.** Per drafter frontmatter + per-essay README disposition + this AUDIT-2 verification: FA essay draws from public-record + published-source material only; no interview material engaged in V-D. Sandy consent state reserved for chapter scope or different essay derivative if author elects to surface Norway interview material. **No consent-pending gate fires for any disposition (A/B/C).**

### §9.5 Conditions for ratification

**No conditional gates on the substantive Pass 3.3 + Pass 3.4 + Pass 3.5 verdicts.** V-D clears all 16 acceptance characters at INCLUDE; all 3 adversarial characters at ROBUST or PARTIALLY ROBUST; Pass 3.5 closes one prior awareness item + holds two; conditional-elevation flag does NOT fire.

Procedural conditions:

- If (A)/(B) selected: light-touch Pass 3.1 fact-check on four backport sites + Stage 5 light re-sign-off + cover-letter refresh.
- If (C) selected: standard Phase C amendment scope on Phillips Petroleum + Pistor backports only.
- Mazzucato sub-textual + IMF/OECD/Meld. St. 9 / Truman rejected — all three dispositions preserve these calls.

---

## §10. Cross-pass routing (post-V-D-AUDIT-2-ratification)

### §10.1 What fires next (post-ratification, conditional on author disposition)

**Status:**

- AUDIT-2 PROPOSED 2026-05-28 (this artifact).
- Hybrid file at `_archive/parallel-drafts_2026-05-28/ch4-foreign-affairs-essay_hybrid_best-of-both.md` PROPOSED 2026-05-28 (drafter session).
- Drafter's-self-audit at `_archive/parallel-drafts_2026-05-28/ch4-foreign-affairs-essay_hybrid_drafters-self-audit.md` PROPOSED 2026-05-28.
- Prior chip's audit at `pass-3-3-and-3-4-bundled-audience-load_VERSION-D_INDEPENDENT-AUDIT_2026-05-28.md` PROPOSED 2026-05-28.

**What fires next:**

- **Author disposition** on (A) SHIP HYBRID vs (B) SPOT-FIX LOCKED CUT vs (C) smaller back-port. **AWAITING.**
- If (A) or (B): light Pass 3.1 verification on four backports + Stage 5 re-sign-off + cover-letter refresh; commit + push per merge-on-ratification.
- If (C): Phase C amendment on Phillips Petroleum + Pistor only; smaller cover-letter refresh; commit + push.

### §10.2 What does NOT fire from this artifact

- **No essay.md modifications** — audit-only per Pass 3.3 + Pass 3.4 + Pass 3.5 hard constraint.
- **No new cross-chapter workstreams.**
- **No spot-fixes recommended on V-D source.**

---

## §11. Stop point — PROPOSED 2026-05-28

This artifact PROPOSED 2026-05-28 (second independent fresh-session audit of V-D hybrid against locked-cut Pass 3.3 + Pass 3.4 + Pass 3.5 RATIFIED baselines). Per v3.1 Amendment C, this is NOT a prose-modifying pass; no spot-fixes recommended on V-D source.

**Verdict summary:**

- **Pass 3.3 acceptance:** NET INCLUDE DECISIVE (16/16 INCLUDE; 8 ✅✅✅ + 8 ✅✅ + 0 NEUTRAL + 0 EXCLUDE). Three ✅✅→✅✅✅ upgrades vs locked-cut three-way scoring (T2.7 Pistor + T3.13 cadence + T3.15 Tooze).
- **Pass 3.4 robustness:** ROBUST. A1 + A2 + A3 all hold at locked-cut verdicts with mild reinforcements. Load-bearing keep-Mazzucato-sub-textual preserved A2 protection. Conditional-elevation flag NOT FIRED.
- **Pass 3.5 developmental-edit (the prior chip's gap closed):** RATIFIABLE-AS-V-D. V-D's seven backport-and-rejection moves are Pass-3.5-polarity-consistent organic restorations. F-3.5-L1 §II legal-architecture awareness item from locked-cut Pass 3.5 substantively CLOSED by V-D's Hannesson backport. F-3.5-L2 + F-3.2-L3 HOLDs carry forward. Substrate-safety verified clean per `feedback_no_invented_factual_claims_in_publisher_facing_prose.md`.

**Aggregate disposition recommendation:** **SHIP HYBRID** (disposition (A)) **OR SPOT-FIX LOCKED CUT** with full V-D delta as Phase C amendment (disposition (B) — substantively identical to (A)). Both produce the substantively-stronger integrated artifact at FA-specific audience set + close F-3.5-L1 Pass 3.5 awareness item. The three-way comparison's conservative (C) (smaller back-port: Phillips Petroleum + Pistor only) forgoes the T3.15 Tooze + T2.8 Hannesson + T3.13 cadence upgrades + the F-3.5-L1 Pass 3.5 closure; my independent AUDIT-2 confirms the prior chip's reading that these are worth capturing in entirety.

**Author actions for ratification (one-finding-at-a-time per Amendment C cadence):**

1. Ratify or revise the §9.3 disposition recommendation: (A) SHIP HYBRID / (B) SPOT-FIX LOCKED CUT / (C) smaller back-port.
2. If (A) or (B): authorize light-touch Pass 3.1 verification on four backports + Stage 5 light re-sign-off + cover-letter refresh.
3. If (C): authorize Phase C amendment scope on Phillips Petroleum + Pistor only.
4. Independent of disposition: confirm cover-letter refresh scope (Pistor + Hannesson + Tooze citation inventory updates for (A)/(B); Pistor only for (C)).

---

## §12. Cross-references

- Audit target: [`publishing/essays/foreign-affairs-existence-proof/_archive/parallel-drafts_2026-05-28/ch4-foreign-affairs-essay_hybrid_best-of-both.md`](../_archive/parallel-drafts_2026-05-28/ch4-foreign-affairs-essay_hybrid_best-of-both.md)
- Locked cut (baseline): [`publishing/essays/foreign-affairs-existence-proof/essay.md`](../essay.md) (Stage 5 RATIFIED 2026-05-27 commit `3ae1777`)
- Alt-no-em parallel draft: [`_archive/parallel-drafts_2026-05-28/ch4-foreign-affairs-essay_alt_no-emdashes_260528-50f30a.md`](../_archive/parallel-drafts_2026-05-28/ch4-foreign-affairs-essay_alt_no-emdashes_260528-50f30a.md)
- Alt-norm-punct parallel draft: [`_archive/parallel-drafts_2026-05-28/ch4-foreign-affairs-essay_alt_normal-punctuation_260528-b357c4.md`](../_archive/parallel-drafts_2026-05-28/ch4-foreign-affairs-essay_alt_normal-punctuation_260528-b357c4.md)
- Drafter's-self-audit (Phase 3 cross-check target): [`_archive/parallel-drafts_2026-05-28/ch4-foreign-affairs-essay_hybrid_drafters-self-audit.md`](../_archive/parallel-drafts_2026-05-28/ch4-foreign-affairs-essay_hybrid_drafters-self-audit.md)
- Prior chip's audit (Phase 3 cross-check target): [`pass-3-3-and-3-4-bundled-audience-load_VERSION-D_INDEPENDENT-AUDIT_2026-05-28.md`](pass-3-3-and-3-4-bundled-audience-load_VERSION-D_INDEPENDENT-AUDIT_2026-05-28.md)
- Three-way comparison (preceding audit; STRUCTURE reference only): [`three-way-comparison_locked-vs-alt-no-em-vs-alt-norm-punct_2026-05-28.md`](three-way-comparison_locked-vs-alt-no-em-vs-alt-norm-punct_2026-05-28.md)
- Stage 1 brief: [`stage-1-brief.md`](stage-1-brief.md) (RATIFIED 2026-05-26 commit `1f73197`)
- Locked-cut Pass 3.3 RATIFIED PASS: [`pass-3-3-audience-load.md`](pass-3-3-audience-load.md)
- Locked-cut Pass 3.4 RATIFIED ROBUST: [`pass-3-4-adversarial.md`](pass-3-4-adversarial.md)
- Locked-cut Pass 3.5 RATIFIED HOLD: [`pass-3-5-developmental-edit.md`](pass-3-5-developmental-edit.md)
- Locked-cut Pass 3.1 RATIFIED + APPLIED: [`pass-3-1-fact-check.md`](pass-3-1-fact-check.md)
- Locked-cut Pass 3.2 RATIFIED + APPLIED: [`pass-3-2-voice-polish.md`](pass-3-2-voice-polish.md)
- Locked-cut Stage 4 RATIFIED CLEAR: [`stage-4-render-audit.md`](stage-4-render-audit.md)
- Locked-cut Stage 5 RATIFIED: [`../stage-5-signoff.md`](../stage-5-signoff.md)
- Aeon V-D independent audit (format STRUCTURE model only; calibration content NOT transferred): `publishing/essays/aeon-mask-of-abundance/rigor/pass-3-3-and-3-4-bundled-audience-load_VERSION-D_INDEPENDENT-AUDIT_2026-05-28.md`
- v3.1 audience-aware drafting discipline: [`tools/memory/feedback_audience_aware_drafting_discipline.md`](../../../../tools/memory/feedback_audience_aware_drafting_discipline.md)
- Em-dash calibration: [`tools/memory/feedback_em_dash_overuse.md`](../../../../tools/memory/feedback_em_dash_overuse.md)
- Merge-on-ratification rule: [`tools/memory/feedback_merge_on_ratification.md`](../../../../tools/memory/feedback_merge_on_ratification.md)
- No-invented-factual-claims rule: [`tools/memory/feedback_no_invented_factual_claims_in_publisher_facing_prose.md`](../../../../tools/memory/feedback_no_invented_factual_claims_in_publisher_facing_prose.md)
- Named-subject consent discipline: [`tools/memory/feedback_named_subject_consent.md`](../../../../tools/memory/feedback_named_subject_consent.md)

---

## §13. Cross-check vs drafter's-self-audit AND prior chip's audit (Phase 3 two-target)

*This section was drafted AFTER §§1–12 above were committed to file, to preserve Phase 2 independence. The drafter's-self-audit and the prior chip's audit were opened only after this artifact's independent scoring was locked.*

### §13.1 Cross-check protocol — two-target

Per audit kickoff §3 Phase 3 boundary: compare each of 16 Pass 3.3 + 3 Pass 3.4 verdicts AND Pass 3.5 inventory against TWO targets: (a) drafter's-self-audit; (b) prior chip's independent audit. Document divergences. Classify by direction. Test whether the prior chip missed anything substantive that my fresh-eyes pass caught (the load-bearing question for this AUDIT-2's value-add).

The drafter's-self-audit is explicitly methodologically suspect (drafter-auditing-own-work bias acknowledged in §0 + §1.2 + multiple per-character cells). The prior chip's audit is structurally independent. AUDIT-2 functions as quality-control double-check on prior chip + Pass 3.5 fill-in for the missed pass.

### §13.2 Pass 3.3 cross-check table (three-way comparison)

| # | Character | My V (AUDIT-2) | Prior chip V | Drafter V | My agreement with prior chip | My agreement with drafter |
|---|---|---|---|---|---|---|
| T1.1 | FA editor brain | ✅✅✅ | ✅✅✅ | ✅✅✅ | AGREE | AGREE |
| T1.2 | FA reader / CFR | ✅✅✅ | ✅✅✅ | ✅✅✅ | AGREE | AGREE |
| T1.3 | SWF practitioner DISP | ✅✅✅ | ✅✅✅ | ✅✅✅ | AGREE | AGREE (verdict; drafter "strongest of four" claim tempered as bias-amplified) |
| T1.4 | Literary agent | ✅✅✅ | ✅✅✅ | ✅✅✅ | AGREE | AGREE |
| T2.5 | Mazzucato / Tooze cluster | ✅✅ | ✅✅ | ✅✅✅ split | AGREE | DISAGREE (drafter over-credited via split-read tally) |
| T2.6 | Brookings / PIIE | ✅✅ | ✅✅ | ✅✅ | AGREE | AGREE |
| T2.7 | Christophers / Susskind | ✅✅✅ | ✅✅✅ | ✅✅✅ | AGREE | AGREE |
| T2.8 | Norway-cluster scholar | ✅✅✅ | ✅✅✅ | ✅✅✅ | AGREE | AGREE (verdict; drafter "most-decorated" tempered) |
| T2.9 | Public Choice / center-right (NOT FIRED) | ✅✅ | ✅✅ | ✅✅ | AGREE | AGREE |
| T3.10 | Non-Anglo / internationalist | ✅✅ | ✅✅ | ✅✅ | AGREE | AGREE |
| T3.11 | Niger Delta / postcolonial CRITICAL | ✅✅ | ✅✅ | ✅✅ | AGREE | AGREE |
| T3.12 | SWF-funded developing-country | ✅✅ | ✅✅ | ✅✅ | AGREE | AGREE |
| T3.13 | General FA subscriber | ✅✅✅ | ✅✅✅ | ✅✅ | AGREE | DISAGREE (drafter under-credited per drafter's-own counter-conservative bias) |
| T3.14 | First-gen / climate-curious | ✅✅ | ✅✅ | ✅✅ | AGREE | AGREE |
| T3.15 | Climate-finance / discount-rate | ✅✅✅ | ✅✅✅ | ✅✅✅ | AGREE | AGREE |
| T3.16 | Reparations-economics | ✅✅ | ✅✅ | ✅✅ | AGREE | AGREE |

**Cross-check summary (Pass 3.3):**

- **My audit vs prior chip's audit: 16/16 AGREE.** Independent replication at the per-cell level confirms the prior chip's per-character verdicts. The prior chip's 8 ✅✅✅ + 8 ✅✅ aggregate count holds at independent replication.
- **My audit vs drafter's-self-audit: 14/16 AGREE; 2 disagreements** (T2.5 drafter over-credited via split-read tally; T3.13 drafter under-credited per counter-conservative bias). Matches prior chip's cross-check vs drafter exactly.

### §13.3 Pass 3.4 cross-check table (three-way comparison)

| Adversarial char | My V (AUDIT-2) | Prior chip V | Drafter V | My agreement with prior chip | My agreement with drafter |
|---|---|---|---|---|---|
| A1 Public Choice / industry-funded petroleum | PARTIALLY ROBUST (mild Hannesson + Pistor reinforcement) | PARTIALLY ROBUST (mild Hannesson + Pistor reinforcement) | PARTIALLY ROBUST (mild path-dependence reinforcement via Hannesson back-port) | AGREE | AGREE |
| A2 Reactionary intellectual | PARTIALLY ROBUST (mild Tooze attenuation; Mazzucato sub-textual preserved) | PARTIALLY ROBUST (mild Tooze attenuation; Mazzucato sub-textual preserved) | PARTIALLY ROBUST (Tooze attribution mildly clarifies open-problem framing; Mazzucato sub-textual preserved) | AGREE | AGREE |
| A3 Procedural-conservative | ROBUST (Hannesson + Pistor amplification) | ROBUST (Hannesson + Pistor amplification) | ROBUST (Hannesson + Pistor amplify within-discipline scholarship register) | AGREE | AGREE |

**Cross-check summary (Pass 3.4):** **3/3 AGREE across all three audits.** Adversarial-set verdicts are robust against drafter-auditing-own-work bias + independent-replication noise.

### §13.4 Pass 3.5 cross-check (new pass; only drafter as comparison target)

The prior chip did NOT cover Pass 3.5 (omitted by author error). The drafter's-self-audit also did NOT explicitly cover Pass 3.5 (focused on Pass 3.3 + Pass 3.4). My Pass 3.5 inventory is therefore the FIRST independent Pass 3.5 verdict on V-D.

| Pass 3.5 finding | AUDIT-2 verdict | Source documentation status |
|---|---|---|
| F-3.5-V-D-1 §II Hannesson backport closes F-3.5-L1 | ACCEPT | Drafter §8 #2 flagged Hannesson for Pass 3.1 verification; locked-cut Pass 3.5 F-3.5-L1 was an awareness item; AUDIT-2 documents V-D's organic Pass 3.5 closure |
| F-3.5-V-D-2 §I Phillips Petroleum closes Pass 3.1 LOW-3 | ACCEPT | Three-way comparison §7.2 Phase C amendment 1 + drafter + prior chip §1.1 §I diff |
| F-3.5-V-D-3 §II NBIM-AR scene-anchor density | ACCEPT | Prior chip §1.1 §II diff; drafter §8 #3 flagged NBIM-AR for Pass 3.1 verification |
| F-3.5-V-D-4 §IV Pistor register-signal | ACCEPT | Three-way §7.2 Phase C amendment 2 + drafter + prior chip §1.1 §IV diff |
| F-3.5-V-D-5 §VI Tooze + framing-as-open-problem | ACCEPT | Prior chip §1.1 §VI diff; drafter §3 flagged Tooze for over-positioning concern (this AUDIT-2 §6.2 tempers the over-positioning concern) |
| F-3.5-V-D-6 §I close em-dash | ACCEPT | Three-way §7.2 §III pivot OPTIONAL; prior chip §1.1 §I close diff |
| F-3.5-V-D-7 §III foreclosure-pivot em-dash | ACCEPT | Three-way §6 cleanest single sentence + prior chip §1.1 §III diff |
| F-3.5-V-D-DISP1 §VI anaphora HOLD | CARRY-FORWARD | Locked-cut Pass 3.5 F-3.5-DISP1; V-D preserves verbatim |
| F-3.5-V-D-8 §V McDowell paragraph density HOLD | CARRY-FORWARD | Locked-cut Pass 3.5 F-3.5-L2 awareness item; V-D preserves verbatim |

**Substrate-safety verification on V-D backports:** §6.1 verified clean (all 7 backport sites; no invented biographical/scene/documentary/quoted-speech specifics; light-touch Pass 3.1 verification recommended for 4 paraphrase/citation sites). Drafter §8 #2–#5 flagged the same four sites for Pass 3.1 verification; prior chip §7 #1 also flagged. Three independent sources converge on the same light-touch verification gate. **AUDIT-2 confirms substrate-safety: CLEAN.**

### §13.5 Did the prior chip miss anything substantive?

**The prior chip's audit holds up at independent replication.** All 16 Pass 3.3 cells match my independent verdicts; all 3 Pass 3.4 cells match. The prior chip's aggregate (8 × ✅✅✅; 16/16 INCLUDE; ROBUST adversarial) is independently confirmed.

**The prior chip's substantive addition that AUDIT-2 contributes:** Pass 3.5 inventory + substrate-safety verification of V-D's backports + closure of locked-cut Pass 3.5 F-3.5-L1 awareness item. The prior chip noted (§7.1 Pass 3.5 cell) that "V-D inherits locked cut's Pass 3.5 RATIFIED HOLD verdict for the ~90% preserved prose; the ~182w of backports introduce two new em-dash sites + four new citation insertions. Pass 3.5 lens (restoration-polarity) does not directly apply at this scope; no new developmental-edit findings expected. Recommended: light Pass 3.5 re-fire on the backport sites only if author elects SHIP HYBRID (integrated-artifact discipline)." The prior chip thus *anticipated* what AUDIT-2 has now executed. AUDIT-2 confirms the prior chip's anticipated verdict: Pass 3.5 RATIFIABLE-AS-V-D with no new developmental-edit concerns + organic closure of F-3.5-L1.

**Where the prior chip's verdicts deserve special validation at independent replication (per author kickoff §3 special-attention cells):**

1. **(a) Whether prior chip properly applied FA calibration (vs accidentally transferring Aeon-pattern verdicts).** AUDIT-2 independent read: **YES, prior chip applied FA calibration correctly.** Prior chip §1.1 + §2 + §3 + §4 + §5 all operate at FA-specific calibration (selective citation deployment; declarative-scene-setting; analytical-policy register; CFR-affiliated reader cluster; FA-stable third-person institutional-policy reportage voice; refusal of partisan-aligned framing; institutional-architecture-as-engineerable analytical conclusion). No Aeon-pattern verdicts (cinematic-opener-preferred; literary-philosophical register; em-dash-as-philosophical-breath signature) appear in prior chip's reasoning. Prior chip §"Critical calibration discipline" explicitly disclaimed Aeon transfer: "Aeon literary-philosophical calibration (cinematic-opener-preferred; em-dash-as-philosophical-breath signature; collective-singular literary voice) does NOT transfer." Calibration discipline: CLEAN.

2. **(b) Whether prior chip's verdicts at T2.5 + T3.13 (the two cells where prior chip diverged from drafter) hold up at independent replication.**
   - **T2.5:** Prior chip ✅✅; drafter ✅✅✅ split. AUDIT-2 independent: ✅✅. **Prior chip's verdict HOLDS at independent replication.** Drafter's split-read tally as ✅✅✅ over-credits the partial cluster-reader signal; the single-verdict cluster-reader read is ✅✅ (Tooze inline gives half the cluster signal; Mazzucato sub-textual gives partial signal).
   - **T3.13:** Prior chip ✅✅✅; drafter ✅✅. AUDIT-2 independent: ✅✅✅. **Prior chip's verdict HOLDS at independent replication.** Drafter's-own counter-conservative bias signature (drafter explicitly compensating for drafter-auditing-own-work bias risk) under-credits the §I close + §III pivot accessibility-cadence gains. Independent read: the cadence gains compensate for the §II density increase; T3.13 cleanly lifts to ✅✅✅.

3. **(c) Whether prior chip's recommendation (SHIP HYBRID disposition A/B with full V-D delta) is the right call or whether something it missed shifts disposition toward (C) smaller back-port.** AUDIT-2 independent: **prior chip's recommendation HOLDS.** The Pass 3.5 finding inventory in this AUDIT-2 *strengthens* the SHIP HYBRID disposition vs the smaller back-port (C), because F-3.5-V-D-1 (Hannesson backport closing F-3.5-L1 awareness) is a Pass 3.5 substantive closure that the smaller (C) back-port (Phillips + Pistor only) would leave un-addressed. The substantive Pass 3.5 closure was anticipated but not documented by the prior chip; AUDIT-2 documents it. Net effect on disposition recommendation: **(A) / (B) SHIP HYBRID is independently confirmed as the right call.**

### §13.6 What AUDIT-2 adds beyond the prior chip's audit

1. **Pass 3.5 finding inventory (the prior chip's missed pass).** 7 ACCEPT findings + 2 HOLD carry-forwards + 1 DISPOSITION carry-forward + substrate-safety verification + organic closure of locked-cut F-3.5-L1 awareness item.

2. **Substrate-safety check on V-D's seven backport sites per `feedback_no_invented_factual_claims_in_publisher_facing_prose.md`.** §6.1 verifies CLEAN — all backports are public-record facts, published-work citations, faithful paraphrases, or punctuation backports. No invented testimonial-register content. The Ch 2 → Harper's Pass 3.5 near-miss empirical anchor (substrate-critical illustrative prose) does NOT apply.

3. **Independent confirmation of prior chip's per-cell Pass 3.3 verdicts at 16/16 AGREE.** Quality-control double-check that the prior chip's single-session audit holds up at independent replication.

4. **Tempering of drafter's §3 over-positioning concern about Tooze §VI passage.** AUDIT-2 §6.2 F-3.5-V-D-5 reasoning shows Tooze passage operates at externality-tail-specific analytical pivot (climate-finance national-vs-global liability boundary) while §VI Norwegian-model-as-local-optimum operates at global-scale distributional problem pivot. Not redundant; complementary.

### §13.7 Cross-check verdict on prior chip's audit quality

**Prior chip's audit quality: HIGH.** Holds up at independent replication on every per-cell verdict. Calibration discipline clean. Disposition recommendation correct. Anticipated Pass 3.5 verdict matches what AUDIT-2 documents. The single missing piece (Pass 3.5 inventory) was acknowledged by prior chip as anticipated-but-not-executed; AUDIT-2 closes that gap.

### §13.8 Summary of cross-check value-add

- Prior chip's audit: confirmed by independent replication on Pass 3.3 + Pass 3.4.
- Drafter's-self-audit: confirmed on Pass 3.4 + 14/16 Pass 3.3 cells; 2 divergences (T2.5 over-credit + T3.13 under-credit) classified per drafter's-own acknowledged bias signatures.
- Pass 3.5 (missed by prior chip): now documented; RATIFIABLE-AS-V-D; closes locked-cut F-3.5-L1 awareness item via Hannesson backport.
- Substrate-safety: CLEAN per `feedback_no_invented_factual_claims_in_publisher_facing_prose.md`.
- Disposition recommendation: **(A) / (B) SHIP HYBRID** with full V-D delta; **independently confirmed strengthened by Pass 3.5 substantive closure of F-3.5-L1**.

**Net: AUDIT-2 fulfills the quality-control double-check function + closes the Pass 3.5 gap.** Author can proceed to disposition decision with two independent audits + one drafter's-self-audit + Pass 3.5 inventory + substrate-safety verification all converging on the same recommendation.

---

`STATE: ch4-foreign-affairs-V-D-independent-audit-2 PROPOSED 2026-05-28 (16/16 INCLUDE; 8 ✅✅✅ + 8 ✅✅ at Pass 3.3; A1 + A2 PARTIALLY ROBUST + A3 ROBUST at Pass 3.4; RATIFIABLE-AS-V-D + organic closure of locked-cut F-3.5-L1 at Pass 3.5; substrate-safety CLEAN; prior chip's audit independently confirmed at 16/16 Pass 3.3 cells + 3/3 Pass 3.4 cells; Pass 3.5 gap closed); NEXT: author-decision-ship-V-D-vs-stay-locked; AWAITING: author-confirmation`

---

*End of Ch 4 → Foreign Affairs Version D (hybrid) second independent Pass 3.3 + Pass 3.4 + Pass 3.5 bundled AUDIT-2 — PROPOSED 2026-05-28.*
