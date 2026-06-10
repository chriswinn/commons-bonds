# Stage-3 Pass 3.1 Verify — Ch 4 (The Existence Proof)

**Date:** 2026-05-25
**Workstream:** Ch 4 pipeline-retrofit (per [`tools/workstream-handoffs/archive/ch4-pipeline-retrofit-handoff_2026-05-17.md`](../workstream-handoffs/archive/ch4-pipeline-retrofit-handoff_2026-05-17.md))
**Chapter:** 4 — *The Existence Proof*
**File audited:** [`manuscript/chapters/Chapter__4_TheExistenceProof.md`](../../manuscript/chapters/Chapter__4_TheExistenceProof.md) — **140 lines** (post-Pass-1 spot-fix state; post-2026-05-24 publishing-pipeline reorg rename)
**Pass scope:** Pass 3.1 VERIFY of Pass 1 fact-check findings (PROPOSED 2026-05-12; RATIFIED + APPLIED via commits `e67b8b8` 2026-05-12 + `8f792ee` 2026-05-13) + Stage 1c MEDIUM coherence finding on GPFG anchor staleness against TA verification round 2026-05-14 canonical.
**Status:** PROPOSED — awaiting Phase C author ratification.
**Hard constraint observed:** No spot-fixes applied to the chapter file.

---

## §0. What this pass does

Pass 3.1 verify confirms which prior-cycle Pass 1 findings remain valid against the current chapter state, surfaces any items that have been superseded by other edits, and proposes spot-fix language for any newly-routed findings inherited from Stage 1c coherence checks.

Per pipeline doctrine §3.3 (Amendment A two-class cascade), Pass 3.1 fires in the automatic-on-edit cascade; this verify session in particular fires because:

1. Stages 1a + 1c were recovered to main 2026-05-25 (commit `b278c1c`) and Stage 1c routed a load-bearing GPFG-canonical-anchor staleness finding for Pass 3.1 verify spot-fix language.
2. Pass 1 PROPOSED 2026-05-12 had its 5 MEDIUM + 2 LOW spot-fixes ratified + applied 2026-05-12 / 2026-05-13. The verify pass confirms each spot-fix's correct realization in the current chapter prose.

---

## §1. Source artifacts read

1. [`manuscript/chapters/Chapter__4_TheExistenceProof.md`](../../manuscript/chapters/Chapter__4_TheExistenceProof.md) — 140 lines, current HEAD (post-Pass-1 spot-fix state, pre-Pass-2 application).
2. [`tools/rigor-passes/commons_bonds_rigor_pass_2026-05-12_ch4_existence_proof_stage3_fact_check_v1.0.0.md`](commons_bonds_rigor_pass_2026-05-12_ch4_existence_proof_stage3_fact_check_v1.0.0.md) — Pass 1 PROPOSED + Ratification record (RATIFIED 2026-05-12; LOW follow-up 2026-05-13).
3. [`tools/quality-gates/clean-baselines/ch4_stage1a_2026-05-25.md`](../quality-gates/clean-baselines/ch4_stage1a_2026-05-25.md) — Stage 1a clean baseline.
4. [`tools/quality-gates/coherence-checks/ch4_stage1c_2026-05-25.md`](../quality-gates/coherence-checks/ch4_stage1c_2026-05-25.md) — Stage 1c coherence findings + cross-session spot-fix recommendations §F-R-1 + §F-R-2 routed here.
5. [`tools/rigor-passes/tech_appendix_verification_round_2026-05-14.md`](tech_appendix_verification_round_2026-05-14.md) — TA verification round canonical anchors B-1 (cumulative production 8.9B Sm³ o.e.); B-2 (GPFG end-2025 $2.0T = 21,268 billion NOK); B-3 (per-citizen $356K-$391K at population 5.62M).
6. [`tools/audits/cross-chapter-consistency-inventory_2026-05-11.md`](../audits/cross-chapter-consistency-inventory_2026-05-11.md) — Norway SWF AUM + per-citizen rows (lines 95 + 96; pre-TA-verification-round canonical).
7. [`publishing/op-eds/_shared/canonical-facts/norway-mcdowell-inventory_2026-05-10.md`](../../publishing/op-eds/_shared/canonical-facts/norway-mcdowell-inventory_2026-05-10.md) — op-ed canonical-facts inventory + LOW-1 source-variation footnote applied 2026-05-13.

---

## §2. Pass 1 RATIFIED-APPLIED findings — verify dispositions

| Finding | Prior status | Current chapter location | Verify disposition |
|---|---|---|---|
| **MEDIUM-1 — GPFG rename year (2006) anchor** | RATIFIED + APPLIED 2026-05-12 via commit `e67b8b8` | Line 24: *"…culminating in the formal establishment of the Government Petroleum Fund in 1990 (later renamed the Government Pension Fund Global in 2006)…"* | **✓ VERIFIED REALIZED.** The "in 2006" addition to the parenthetical sits cleanly in the current prose; parallel structure with the 1990 founding date holds; no drift. |
| **MEDIUM-2 — Bondevik II disambiguation (Option A numeral)** | RATIFIED + APPLIED 2026-05-12 via commit `e67b8b8` | Line 32: *"Bondevik II's center-right coalition, Stoltenberg's second Labour government, Solberg's Conservative coalition, Støre's subsequent Labour-Centre coalition."* | **✓ VERIFIED REALIZED.** "Bondevik II's" present in current prose; the prior op-ed-pipeline coalition-timing drift remains foreclosed; no regression. |
| **MEDIUM-3 — UNEP $1B scope-explicit rewrite** | RATIFIED + APPLIED 2026-05-12 via commit `e67b8b8` | Line 82: *"The UNEP report estimated that initial capitalization of an Ogoniland Environmental Restoration Authority would require on the order of one billion dollars, with full restoration projected to require twenty-five to thirty years of sustained remediation; subsequent monitoring suggests cleanup progress has remained well short of that timeline, and mangrove-ecosystem recovery, where it occurs, runs on multi-decade timescales independent of the cleanup itself."* | **✓ VERIFIED REALIZED.** The scope-explicit "initial capitalization of an Ogoniland Environmental Restoration Authority" phrasing replaces the prior "comprehensive cleanup… on the order of one billion dollars" framing. Twenty-five to thirty years duration anchored; mangrove-ecosystem-recovery hedge present. No drift. |
| **MEDIUM-4 — Alaska 1976/1977 cross-corpus resolution** | RATIFIED + APPLIED 2026-05-12 via commit `e67b8b8` (cross-corpus only — Ch 4 unchanged per recommendation) | Ch 4 line 12: *"Alaska's Permanent Fund, established the same year…"* (1976 implicit) | **✓ VERIFIED REALIZED.** Per Pass 1 ratification: Ch 4 prose deliberately held unchanged; cross-corpus canonical lock to 1976 (constitutional amendment) applied to case-study brief + cross-chapter consistency inventory. Ch 4 prose still reads correctly per locked canonical. No drift. |
| **MEDIUM-5 — Bismarck 1889 + 1920s hyperinflation date-tightened (Option A)** | RATIFIED + APPLIED 2026-05-12 via commit `e67b8b8` | Line 104: *"…Bismarck's Germany, where the partially-funded character of the 1889 Old Age and Disability Insurance system survived until the post-WWI hyperinflation of the early 1920s."* | **✓ VERIFIED REALIZED.** Date-tightened phrasing present; "1889 Old Age and Disability Insurance" + "post-WWI hyperinflation of the early 1920s" both anchored as recommended. No drift. |
| **LOW-1 — Ekofisk Dec 22/23/24 source-variation footnote** | RATIFIED + APPLIED 2026-05-13 via commit `8f792ee` (canonical-facts-inventory footnote; NOT a chapter change) | Ch 4 line 10: *"In 1969, three days before Christmas…"* (unchanged) | **✓ VERIFIED REALIZED.** Ch 4 prose preserves the locked "three days before Christmas" phrasing; the source-variation disclosure lives in the canonical-facts inventory per the LOW-1 ratification, foreclosing future Stage-3 sessions from re-litigating the Dec 22/23/24 date variance. No drift. |
| **LOW-3 — Equinor 2018 rename year anchor** | RATIFIED + APPLIED 2026-05-13 via commit `8f792ee` | Line 26: *"…direct ownership of Equinor (formerly Statoil, the national oil company, renamed in 2018)…"* | **✓ VERIFIED REALIZED.** The "renamed in 2018" addition completes the corporate/institutional-rename anchoring symmetry alongside MEDIUM-1's GPFG 2006 anchor. No drift. |
| **LOW-2 — Time-sensitive figures (deferred to pre-publication refresh)** | HELD per Pass 1 recommendation (deferred to pre-pub) | Line 26 GPFG AUM + per-citizen figures; line 28 ~3% real-return; line 48 ~70–80% state-capture | **⚠ PARTIALLY OVERTAKEN.** The "$1.9T AUM + $340K per-citizen" component of LOW-2's deferred list has been superseded by the TA verification round 2026-05-14 canonical refresh. The deferred-to-pre-pub posture stood when LOW-2 was held; the TA round happened in the interim and set new canonical anchors. **Routed here as F-R-1 + F-R-2 below.** The 3% real-return + 70–80% state-capture components of LOW-2 remain in their original deferred-to-pre-pub posture (TA round did not surface drift on these). |

**Pass 1 verify summary.** All 7 RATIFIED-APPLIED findings (5 MEDIUM + 2 LOW) verified realized in current chapter prose with no drift. LOW-2's deferred-to-pre-pub posture remains valid for two of its three components (3% real-return; 70–80% state-capture) and has been partially overtaken by the TA round for the third (AUM + per-citizen anchors) — the overtaken portion is routed forward as F-R-1 + F-R-2 below.

---

## §3. Newly-routed findings from Stage 1c — proposed spot-fix language

These two findings are routed from Stage 1c [`ch4_stage1c_2026-05-25.md`](../quality-gates/coherence-checks/ch4_stage1c_2026-05-25.md) §"Cross-session spot-fix recommendations" with spot-fix language to be authored here. Both are factual-currency anchor refreshes within already-correct prose architecture (no structural change to chapter); both stay within the trade-prose cadence Ch 4 already established at line 26.

### F-R-1 — GPFG AUM anchor refresh at line 26 (MEDIUM)

**Location:** Line 26 (currently in the §"The architecture" §-section, paragraph beginning *"Petroleum revenue flows from the state's production licenses…"*).

**Current chapter text (line 26):**

> "The fund now holds more than one and nine-tenths trillion dollars in assets. On a per-citizen basis, that is roughly three hundred and forty thousand dollars for every person in the country — man, woman, child, pensioner, newborn."

**Canonical truth (per TA verification round 2026-05-14, anchor B-2):**

GPFG end-2025: **$2.0T = 21,268 billion NOK** (Norges Bank Investment Management 2025 end-year reporting via Statistics Norway harmonization; per the TA verification round 2026-05-14 calibration commit `aec033c`).

**Why this is the F-R-1 finding.** Ch 4's "more than one and nine-tenths trillion dollars" represents the corpus state at original Ch 4 drafting (2026-04). The figure crossed $1.9T in mid-2025 and has continued through the $1.9T-$2.2T range with market conditions; the TA verification round 2026-05-14 set canonical end-2025 at $2.0T. The chapter prose can absorb the refresh with a single-word change ("one and nine-tenths" → "two") that preserves the cadence and the "more than X trillion" register. The cross-chapter consistency inventory line 95 also needs parallel refresh (sibling-side disposition routed to inventory-side revision session per Stage 1c §"Sibling-side spot-fix candidates").

**Recommended spot-fix language.** Replace *"more than one and nine-tenths trillion dollars in assets"* with:

```
more than two trillion dollars in assets
```

Single-word substitution; preserves the "more than X trillion" cadence + the trade-prose-friendly spell-out-the-numeral register Ch 4 has used consistently; aligns Ch 4 to the TA verification round canonical anchor at $2.0T (rounded down to "two trillion" for the trade-prose register, with the precise canonical figure carried by the TA + cross-chapter consistency inventory).

**Severity rationale.** MEDIUM (factual-currency anchor refresh within correct prose architecture). Not HIGH because the underlying claim (Norway's fund holds a substantially-greater-than-prior-decade sum) is correct + holds across any plausible market-movement of the canonical figure; not LOW because the inventory + TA round have both flagged this as a known coherence-drift line that should refresh at the next chapter touch.

---

### F-R-2 — Per-citizen GPFG share anchor refresh at line 26 (MEDIUM)

**Location:** Line 26 (same sentence-pair as F-R-1, the "On a per-citizen basis…" closer).

**Current chapter text (line 26 continuation):**

> "On a per-citizen basis, that is roughly three hundred and forty thousand dollars for every person in the country — man, woman, child, pensioner, newborn."

**Canonical truth (per TA verification round 2026-05-14, anchor B-3):**

Per-citizen GPFG share: **$356K-$391K range at population 5.62M** (Statistics Norway 2025 population; year-end 2025 $2.0T → $356K floor; April 2025 $2.2T peak → $391K ceiling).

**Why this is the F-R-2 finding.** Ch 4's "roughly three hundred and forty thousand dollars" derives directly from the prior $1.9T AUM ÷ ~5.55M population calculation that anchored the original chapter prose. Both inputs have refreshed: AUM to $2.0T (F-R-1 above) and population to 5.62M (per Statistics Norway 2025 release per TA round B-3). The refreshed per-citizen figure sits in the $356K-$391K range depending on which AUM snapshot anchors it.

**Recommended spot-fix language (two options, author selects):**

- **Option (a) — single-figure year-end-anchor preservation of cadence (recommended).** Replace *"roughly three hundred and forty thousand dollars"* with *"roughly three hundred and sixty thousand dollars"*. Anchors to year-end 2025 $2.0T → ~$356K rounded to "three hundred and sixty thousand." Preserves the chapter's single-figure prose-flow at line 26 and the spell-out-the-numeral cadence; matches Pass 1 LOW-2's defer-to-pre-pub-refresh recommendation in lightweight-substitution form. Aligns conservatively to the year-end floor of the canonical range; the chapter prose can refresh upward at next anchor cycle if the canonical moves further. This is the **recommended option** for trade-prose-cadence preservation.

- **Option (b) — range-form precision match to TA canonical.** Replace *"roughly three hundred and forty thousand dollars"* with *"roughly three hundred and fifty to three hundred and ninety thousand dollars"*. Carries the full canonical range explicitly; matches TA precision exactly; slightly lengthens the sentence cadence at line 26 (8 → 13 words in the per-citizen phrase). Defensible if the author prefers explicit-range form over single-figure-with-rounding.

Author selects between (a) and (b) at Phase C; both options align to TA canonical; (a) preserves cadence + (b) preserves precision.

**Severity rationale.** MEDIUM (same as F-R-1 — factual-currency anchor refresh within correct prose architecture). Population anchor (5.62M) is locked per Statistics Norway; AUM anchor varies through the year so the per-citizen figure inherits range uncertainty that Option (b) makes visible and Option (a) absorbs via single-figure-rounded-conservatively register.

---

## §4. Items verified — no findings (positive verifications carried forward from Pass 1)

The Pass 1 Items-verified table (§"Items verified — no findings") contains 22 positively-verified claims spanning Ekofisk discovery + Norwegian-population at the time + Government Petroleum Fund 1990 + fund-investment scope + 2001 fiscal rule + government-chronology sequencing + Alberta-Alaska contrasts + Nigeria oil-history + UNEP 2011 report + Saro-Wiwa hanging + Commonwealth suspension + US Social Security 1935 + US Social Security pay-as-you-go architecture + climate-vulnerability typology. **All 22 carry forward as verified; Pass 3.1 re-verifies none individually** (per pipeline doctrine §3.3 verify discipline — confirm Pass 1's positively-verified items remain in-place rather than re-litigate the underlying facts).

Two of the 22 items receive incidental anchor-refresh notes from F-R-1 + F-R-2 above:

- *"GPFG AUM 'more than $1.9 trillion'"* (Pass 1 verified Ch 4:23) — Ch 4 line 26 in current numbering. Refreshes to "$2.0T" canonical via F-R-1.
- *"~$340K per citizen"* (Pass 1 verified Ch 4:23) — Ch 4 line 26 in current numbering. Refreshes to ~$356K-$391K canonical range via F-R-2.

The Pass 1 verification *"~$340K per citizen … ($1.9T ÷ ~5.55M population ≈ $342K)"* parenthetical-arithmetic note remains accurate as a historical-arithmetic record of the pre-TA-round anchor. The TA round updated both the numerator (AUM) and the denominator (population, 5.55M → 5.62M); the post-refresh arithmetic is $2.0T ÷ 5.62M ≈ $356K.

---

## §5. Apparatus regression check (carried forward from Pass 1)

Pass 1 verified zero apparatus regression. Pass 3.1 re-verifies via Stage 1a clean baseline ([`ch4_stage1a_2026-05-25.md`](../quality-gates/clean-baselines/ch4_stage1a_2026-05-25.md)): zero scaffolding-vocabulary leaks; zero regressed-pattern matches; single Title-case *"Intergenerational Option Value"* at line 124 is the canonical Ch 4 introduction site per cross-chapter consistency inventory line 40. **No apparatus regression confirmed.**

---

## §6. Named-subject consent check (carried forward from Pass 1)

Pass 1 verified zero living-named-subject consent issues. Pass 3.1 re-verifies:

- Norwegian PMs (Stoltenberg, Bondevik II, Solberg, Støre) named in their official capacity as office-holders — standard journalistic practice per [`feedback_named_subject_consent.md`](../memory/feedback_named_subject_consent.md) public-record exception.
- Ken Saro-Wiwa is deceased (executed 10 November 1995); historical-record status; named with courtesy-notify-family-if-reachable default. No follow-up required for Pass 3.1.
- No private living subjects named.
- Ogoni and Ijaw named as peoples not as individuals (line 80).
- International oil-companies (Shell, Chevron, ExxonMobil, Total) named in official capacity as historical operators (line 80).

**No named-subject consent issues confirmed.**

---

## §7. Verdict

### §7.1 Findings tally

| Severity | Count | Findings |
|---|---|---|
| HIGH | 0 | — |
| MEDIUM | 2 | F-R-1 (line 26 GPFG AUM anchor refresh to "more than two trillion dollars"); F-R-2 (line 26 per-citizen anchor refresh to ~$360K Option (a) or $350K-$390K Option (b)) |
| LOW | 0 | — |

**Total newly-routed findings:** 2 (both MEDIUM; both from Stage 1c routing; both factual-currency anchor refreshes within already-correct prose architecture).

**Pass 1 RATIFIED-APPLIED findings:** 7 (5 MEDIUM + 2 LOW); **all verified realized in current chapter prose with no drift**.

**Pass 1 HELD (LOW-2) findings:** 3 components; 2 components remain in original deferred-to-pre-pub posture (3% real-return; 70–80% state-capture); 1 component (AUM + per-citizen) has been partially overtaken by the TA verification round 2026-05-14 → routed forward as F-R-1 + F-R-2.

### §7.2 Aggregate Pass-3.1-verify verdict

**VERIFIED + 2 NEW MEDIUM SPOT-FIXES PROPOSED.**

The Pass 1 spot-fix application (commits `e67b8b8` + `8f792ee` 2026-05-12 / 2026-05-13) holds cleanly in the current chapter prose. No drift; no regression; no overtaken-by-subsequent-edits findings. The 5 MEDIUM + 2 LOW Pass-1 spot-fixes verify realized at the line locations specified by the Pass 1 Phase C ratification record.

Two new MEDIUM findings (F-R-1 + F-R-2) are routed forward from Stage 1c §"Cross-session spot-fix recommendations" with proposed spot-fix language for Phase C author ratification:

- **F-R-1 (GPFG AUM line 26).** Recommended substitution: "one and nine-tenths trillion" → "two trillion." Single-word change; preserves cadence; aligns to TA round 2026-05-14 canonical $2.0T.
- **F-R-2 (per-citizen line 26).** Recommended Option (a): "three hundred and forty thousand" → "three hundred and sixty thousand." Single-figure substitution; preserves cadence; aligns to TA round 2026-05-14 canonical year-end floor (~$356K). Option (b) range-form preserves TA precision exactly at slight cadence cost.

Both F-R-1 + F-R-2 are factual-currency refreshes within already-correct prose architecture; both are MEDIUM severity (inventoried + TA-round-canonical-aligned); no chapter structural change. The pair should be applied as a single coupled Phase C atomic-chunk because both modify the same sentence at line 26.

Sibling-side spot-fix candidates (cross-chapter consistency inventory line 95 + 96 row updates; Ch 6 line 537 anchor refresh; op-ed canonical-facts inventory status check) are routed to separate-session disposition per Stage 1c §"Sibling-side spot-fix candidates" and are NOT in scope for this Pass 3.1 verify artifact.

### §7.3 Recommended Phase C disposition

1. **Apply F-R-1 + F-R-2 together at Phase C as a single atomic-chunk commit** at line 26 of `manuscript/chapters/Chapter__4_TheExistenceProof.md`. Recommended chunk text:

   > *"The fund now holds more than two trillion dollars in assets. On a per-citizen basis, that is roughly three hundred and sixty thousand dollars for every person in the country — man, woman, child, pensioner, newborn."*

   (Assumes F-R-2 Option (a) selection; if author selects Option (b), substitute the range-form per-citizen phrase.)

2. **Update Pass 1 Ratification record** to note F-R-1 + F-R-2 supersede the AUM + per-citizen component of LOW-2 (the 3% real-return + 70–80% state-capture components of LOW-2 remain in deferred-to-pre-pub posture for next refresh cycle).

3. **PM session schedules sibling-side spot-fixes** (cross-chapter consistency inventory line 95 + 96; Ch 6 line 537; op-ed canonical-facts inventory status check) per Stage 1c §"Sibling-side spot-fix candidates."

---

## §8. What this pass did NOT do

- **Did NOT re-litigate Pass 1 findings.** Pass 1 RATIFIED + APPLIED via commits `e67b8b8` + `8f792ee`; verify confirms realization, does not re-score.
- **Did NOT apply spot-fixes to chapter source.** F-R-1 + F-R-2 are PROPOSED; Phase C application is a separate combined ratification + application session.
- **Did NOT run Pass 3.2 verify or Pass 3.3 acceptance.** Those are separate sub-steps in this same retrofit-recovery session (each lands as its own commit per session-protocol checkpoint discipline).
- **Did NOT propose any structural chapter change.** Both newly-routed findings are factual-currency anchor refreshes within already-correct prose architecture.
- **Did NOT contact named subjects.** Per consent discipline + per hard constraints in the workstream handoff.

---

## §9. Hard constraints honored

- ✓ Did NOT apply spot-fixes to `Chapter__4_TheExistenceProof.md` (chapter source unchanged in this session).
- ✓ Did NOT re-litigate Pass 1 findings (verify-disposition only).
- ✓ Verified Pass 1 spot-fix application by direct reading against current chapter prose at line locations (24, 26, 32, 82, 104, 10, 26).
- ✓ Verified TA verification round 2026-05-14 canonical anchors (B-1 + B-2 + B-3) via direct read of the verification artifact.
- ✓ Surfaced F-R-1 + F-R-2 with explicit recommended spot-fix language per workstream handoff direction.
- ✓ Honored Pass 1 + Stage 1c routing dispositions (sibling-side findings routed to separate sessions).
- ✓ Branched within worktree per CLAUDE.md branch discipline.

---

*End of Ch 4 Stage-3 Pass 3.1 Verify. PROPOSED 2026-05-25 — awaiting Phase C author ratification + application of F-R-1 + F-R-2 at line 26.*
