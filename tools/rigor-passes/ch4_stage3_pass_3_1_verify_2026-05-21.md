# Pass 3.1 Verify — Ch 4 (The Existence Proof)

**Date:** 2026-05-21
**Workstream:** Ch 4 pipeline-retrofit per [`tools/workstream-handoffs/ch4-pipeline-retrofit-handoff_2026-05-17.md`](../workstream-handoffs/ch4-pipeline-retrofit-handoff_2026-05-17.md)
**Chapter:** 4 — *The Existence Proof*
**File audited:** [`manuscript/chapters/Chapter__4_TheExistenceProof.md`](../../manuscript/chapters/Chapter__4_TheExistenceProof.md) — **141 lines**, post-rename (`a09e319`) + post-cosmetic-header-edit (`e1a533e`) state
**Branch:** `claude/unruffled-elbakyan-af5b16` (off `origin/main` at `de83dcb`)
**Status:** **PROPOSED** — awaits author ratification at retrofit-session close. No spot-fixes applied to chapter source.
**Mode:** Pass 3.1 verify (not fresh fact-check). Re-verifies the 5 MEDIUM + 2 LOW Pass-1 spot-fixes RATIFIED + APPLIED 2026-05-12 (commit `e67b8b8` MEDIUM-1 through MEDIUM-5; commit `8f792ee` LOW-1 + LOW-3 follow-up 2026-05-13) against current chapter state + flags the post-Pass-1 TA-verification-round-2026-05-14 canonical-anchor refresh as a Phase C update candidate extending the Pass-1 LOW-2 disposition.
**Parent artifact (RATIFIED + APPLIED):** [`commons_bonds_rigor_pass_2026-05-12_ch4_existence_proof_stage3_fact_check_v1.0.0.md`](commons_bonds_rigor_pass_2026-05-12_ch4_existence_proof_stage3_fact_check_v1.0.0.md)

---

## §0. Why this verify pass

Per pipeline-doctrine v1.0.0 retrofit-mode + per the Ch 4 retrofit handoff §1: Pass 1 fact-check was PROPOSED + RATIFIED + APPLIED 2026-05-12 (with LOW-1 + LOW-3 follow-up 2026-05-13). Two intervening events warrant a verify pass:

1. **Chapter rename + cosmetic header edit.** Commit `a09e319` (2026-05-17) renamed `Chapter__4_THEEXISTENCEPROOF__Draft.md` → `Chapter__4_TheExistenceProof.md`; commit `e1a533e` (2026-05-18) added `*By Chris Winn*` + horizontal-rule separator at the top (purely cosmetic per the commit message *"edited the first couple of lines of each chapter as they are giving me hell when it comes to rendering"*). Net effect: chapter is now 141 lines vs Pass-1-baseline 138 lines; line numbers shift +3 throughout the body. **No body-prose content change.** Verify pass confirms the 7 ratified spot-fixes survived the housekeeping.
2. **TA verification round 2026-05-14 canonical-anchor refresh.** Post-Pass-1-ratification, the Tech Appendix authoritative-source verification round (per [`tools/rigor-passes/tech_appendix_verification_round_2026-05-14.md`](tech_appendix_verification_round_2026-05-14.md)) refreshed Norway canonical anchors: cumulative production 8.7 → 8.9B Sm³ o.e.; GPFG end-2025 $2.0T (April 2025 peak $2.2T); per-citizen $356K–$391K (was $380K–$400K); population 5.62M. Ch 4 carries the pre-refresh figures ($1.9T + $340K per-citizen) per the Pass-1 LOW-2 disposition ("defer to pre-publication refresh"). Verify pass extends LOW-2 into an active Phase C update recommendation now that the canonical refresh has landed + Ch 6 line 207 has independently updated to "$2.2T (early 2025 NBIM)."

---

## §1. Source artifacts read

1. [`manuscript/chapters/Chapter__4_TheExistenceProof.md`](../../manuscript/chapters/Chapter__4_TheExistenceProof.md) — current state (141 lines, post-rename + post-cosmetic-header).
2. [`commons_bonds_rigor_pass_2026-05-12_ch4_existence_proof_stage3_fact_check_v1.0.0.md`](commons_bonds_rigor_pass_2026-05-12_ch4_existence_proof_stage3_fact_check_v1.0.0.md) — Pass 1 fact-check artifact (RATIFIED + APPLIED).
3. [`tech_appendix_verification_round_2026-05-14.md`](tech_appendix_verification_round_2026-05-14.md) — TA authoritative-source verification round; canonical Norway anchors refresh.
4. [`tools/quality-gates/coherence-checks/ch4_stage1c_2026-05-21.md`](../quality-gates/coherence-checks/ch4_stage1c_2026-05-21.md) — this session's Stage 1c artifact (COHERENCE VERIFIED with §5 Phase C update recommendation).
5. [`publishing/op-eds/_inventory_norway-mcdowell-canonical-facts_2026-05-10.md`](../../publishing/op-eds/_inventory_norway-mcdowell-canonical-facts_2026-05-10.md) — op-ed canonical-facts inventory (gold standard for Pass 1).
6. [`tools/audits/cross-chapter-consistency-inventory_2026-05-11.md`](../audits/cross-chapter-consistency-inventory_2026-05-11.md) — cross-chapter consistency inventory (note: pre-TA-refresh; rows 95–96 stale per Stage 1c §5).
7. [`manuscript/chapters/Chapter__6_ThreeWaysofCounting.md`](../../manuscript/chapters/Chapter__6_ThreeWaysofCounting.md) — Ch 6 Norway Backtest line 207 (cross-chapter Norway-AUM reference).
8. Memory: [`feedback_verify_stale_memory_claims.md`](/Users/c17n/.claude/projects/-Users-c17n-commons-bonds/memory/feedback_verify_stale_memory_claims.md) — verification-of-time-sensitive-claims discipline.

---

## §2. Verification of Pass-1 ratified spot-fixes

Each fix verified by direct read of the current chapter at its (line-shifted) location.

| Finding | Pass-1 line | Current line (+3) | Status | Verification |
|---|---|---|---|---|
| **MEDIUM-1** — GPFG 2006 rename year added inside parenthetical | 21 | **24** | ✓ HOLDS | Current line 24: *"What Norway built, beginning with a White Paper in the early 1970s and culminating in the formal establishment of the Government Petroleum Fund in 1990 (later renamed the Government Pension Fund Global **in 2006**), is a sovereign wealth fund…"* Spot-fix intact verbatim. |
| **MEDIUM-2** — Bondevik II numeral disambiguator (Option A) | 29 | **32** | ✓ HOLDS | Current line 32: *"…has held through every administration since: **Bondevik II's** center-right coalition, Stoltenberg's second Labour government, Solberg's Conservative coalition, Støre's subsequent Labour-Centre coalition."* Numeral disambiguator intact. |
| **MEDIUM-3** — UNEP $1B sentence rewritten to scope-explicit *"initial capitalization of an Ogoniland Environmental Restoration Authority"* + *"twenty-five to thirty years"* duration | 79 | **82** | ✓ HOLDS | Current line 82: *"The UNEP report estimated that **initial capitalization of an Ogoniland Environmental Restoration Authority** would require on the order of one billion dollars, with full restoration projected to require **twenty-five to thirty years** of sustained remediation; subsequent monitoring suggests cleanup progress has remained well short of that timeline…"* Spot-fix intact verbatim with the additional "subsequent monitoring" qualifier (per Pass 2 §7 note: hedging language preserved). |
| **MEDIUM-4** — Cross-corpus Alaska 1976 canonical lock (Ch 4 unchanged per Pass 1 recommendation; case-study brief + cross-chapter consistency inventory updated 2026-05-12) | 9 | **12** | ✓ HOLDS | Current line 12: *"Alaska's Permanent Fund, **established the same year**, captured petroleum royalties for distribution as annual citizen dividends rather than long-term sovereign capitalization…"* The *"same year"* anchor resolves to Alberta's 1976 establishment (Ch 4:12 same line). Cross-corpus 1976 lock holds. |
| **MEDIUM-5** — Bismarck Germany 1889 + 1920s hyperinflation tightening (Option A) | 101 | **104** | ✓ HOLDS | Current line 104: *"Variations of the funded architecture had been proposed and partially implemented in other jurisdictions, including Bismarck's Germany, where **the partially-funded character of the 1889 Old Age and Disability Insurance system survived until the post-WWI hyperinflation of the early 1920s**."* Spot-fix intact verbatim. |
| **LOW-1** — Ekofisk Dec 22/23/24 source-variation footnote added to op-ed canonical-facts inventory (Ch 4 phrasing held per Pass 1 recommendation) | 7 | **10** | ✓ HOLDS | Current line 10: *"In 1969, **three days before Christmas**, a drill bit in the North Sea struck oil on a Norwegian concession called Block 2/4."* Ch 4 phrasing held; inventory footnote at `_inventory_norway-mcdowell-canonical-facts_2026-05-10.md:19` documents the Phillips Dec 22 / NPD Dec 23 / Equinor Dec 24 source split + locks corpus phrasing. |
| **LOW-3** — Equinor 2018 rename year (coupled to MEDIUM-1) | 23 | **26** | ✓ HOLDS | Current line 26: *"…direct ownership of Equinor (formerly Statoil, the national oil company, **renamed in 2018**) into the fund."* Spot-fix intact verbatim. |

**Verification result: 7 of 7 Pass-1 ratified spot-fixes intact.** No regression introduced by the rename / cosmetic-header housekeeping commits. Line-number shifts (+3) are uniform; no body-prose content drift.

---

## §3. TA verification round 2026-05-14 canonical refresh — Phase C update candidate

Pass 1 LOW-2 disposition (held 2026-05-12, recommendation: *"defer to pre-publication refresh"*) is now ripe for Phase C application given the post-Pass-1 TA verification round's canonical-anchor refresh + the independent Ch 6 line 207 update to "$2.2T (early 2025 NBIM)."

### §3.1 Current Ch 4 anchors vs TA-canonical (post-2026-05-14)

| Anchor | Current Ch 4 (line 26) | TA-canonical (post-refresh) | Verdict |
|---|---|---|---|
| GPFG AUM | "more than one and nine-tenths trillion dollars" ($1.9T) | $2.0T end-2025; $2.2T April 2025 peak | **STALE** — Ch 4 carries the pre-2026-05-14 mid-range figure. |
| Per-citizen share | "roughly three hundred and forty thousand dollars" ($340K) | $356K–$391K range (at population 5.62M; end-2025 $356K + April 2025 peak $391K) | **STALE** — Ch 4 carries the pre-2026-05-14 single-point figure. |
| Norway population (1969 reference) | "fewer than four million people" (Ch 4 line 10; ~3.9M 1969 verified Pass 1) | Not a TA refresh target (1969 population unchanged) | ✓ HOLDS (1969 population is the chapter's intended scope at line 10; the TA refresh's 5.62M is the 2025 population, applicable at line 26 only). |
| Expected real return (fiscal rule) | "roughly three percent" (line 28) | 3% (verified per Pass 1 Items table; reflects 2017 downward revision from 4%) | ✓ HOLDS — no refresh; current canonical. |
| State capture rate | "seventy to eighty cents of every dollar of net petroleum wealth" (line 48) | 70–80% (structural figure; 78% effective petroleum tax + state ownership economics) | ✓ HOLDS — no refresh; current canonical per Pass 1. |
| Cumulative oil-and-gas production | Not in Ch 4 prose (cumulative BOE figures live at TA §11.5; Ch 4's prose is qualitative) | 8.9B Sm³ o.e. (refreshed from 8.7B) | N/A to Ch 4 prose. |
| Carbon intensity (oil + gas) | Not in Ch 4 prose | 0.43 t CO₂/barrel oil; 0.31 t CO₂/BOE-equivalent gas | N/A to Ch 4 prose. |

### §3.2 Cross-chapter Ch 6 reconciliation

Per Stage 1c §3 finding: Ch 6 line 207 (Norway Backtest) now reads *"approximately $2.2 trillion (early 2025 NBIM)"* — which is the April 2025 peak per TA refresh. Ch 4 line 26 currently reads $1.9T. **Cross-chapter inconsistency:** Ch 6 has updated to the peak figure; Ch 4 has not refreshed.

Cross-chapter consistency inventory (2026-05-11) line 95 records the pre-update state ("Ch 4 line 23: $1.9T canonical; Ch 6 line 537: $1.8T — Ch 4 canonical") + flags drift. The 2026-05-11 inventory is itself now stale — both chapters have updated independently of the inventory (Ch 6 to $2.2T; Ch 4 retains $1.9T per Pass-1 LOW-2 hold).

### §3.3 Phase C update recommendation (extends Pass-1 LOW-2)

**Severity: MEDIUM** (was LOW under Pass-1; promoted to MEDIUM at this verify pass because the TA-refresh has now landed + cross-chapter inconsistency has surfaced through Ch 6's independent update).

**Recommended Phase C touch (Ch 4 line 26 + the surrounding sentence cluster):**

Current line 26 sentence cluster:
> "The fund now holds more than one and nine-tenths trillion dollars in assets. On a per-citizen basis, that is roughly three hundred and forty thousand dollars for every person in the country — man, woman, child, pensioner, newborn."

**Options for refresh (author selects one; per Amendment C per-finding format with Options + Recommendation + Reasoning):**

- **Option A (end-2025 + peak; matches TA-refresh both anchors).** *"The fund now holds more than two trillion dollars in assets; at its April 2025 peak it held two-point-two trillion. On a per-citizen basis, that is roughly three hundred and fifty-six thousand dollars for every person in the country — three hundred and ninety-one thousand at the 2025 peak — man, woman, child, pensioner, newborn."* Preserves the universality-of-coverage flourish (Pass-2 F-V16 hold); adds the peak-figure breath that aligns with Ch 6's framing; gives the reader both end-of-year and peak anchors for trade-press accuracy.
- **Option B (single-point end-2025; simpler).** *"The fund now holds more than two trillion dollars in assets. On a per-citizen basis, that is roughly three hundred and fifty-six thousand dollars for every person in the country — man, woman, child, pensioner, newborn."* Cleaner prose; aligns with TA-canonical end-2025; cross-chapter requires Ch 6 line 207 to specify "early 2025 peak" rather than "early 2025" to avoid the now-vs-peak ambiguity.
- **Option C (range-framed; matches TA-refresh range).** *"The fund now holds in the range of two trillion dollars in assets, fluctuating in recent years through the two-to-two-point-two trillion band with market conditions. On a per-citizen basis, that is roughly three hundred and fifty-six to three hundred and ninety-one thousand dollars for every person in the country — man, woman, child, pensioner, newborn."* Most precise; highest-accuracy register; explicit range communicates the time-sensitivity of the figure.
- **Option D (hold-as-is + add inline pre-publication-refresh-flag comment).** Hold $1.9T + $340K; add a session-internal scaffolding note (NOT in body prose) at the pre-publication-refresh checklist to update when the manuscript moves to copyedit. Honors the Pass-1 LOW-2 disposition's "defer to pre-publication refresh" intent without changing prose now.

**Recommendation: Option A** (end-2025 + peak; matches TA-refresh both anchors).

**Reasoning:** Option A preserves the chapter's existing rhetorical structure (the universality-of-coverage flourish closing the sentence cluster); adds the precision that the TA verification round established as canonical; resolves the cross-chapter inconsistency with Ch 6 line 207 by giving Ch 4 both end-of-year + peak anchors (Ch 6 can keep "early 2025" framing); and the additional sentence-length (~10 added words) does not materially impact Pass-2 F-V16 / F-V12 voice-polish dispositions. Option B is simpler but creates cross-chapter ambiguity (Ch 6 says $2.2T early 2025; Ch 4 says $2.0T end-2025; reader scanning quickly may not parse the temporal distinction). Option C is most precise but breaks the prose's cadence (the "fluctuating" phrasing is too administrative-register for the chapter's voice). Option D defers to a pre-publication-refresh moment that may not happen on a schedule predictable to the current Phase C cadence; given the TA refresh has already landed + Ch 6 has updated, deferring further extends the cross-chapter inconsistency window.

**Cross-chapter cascade implications:** Option A application triggers (a) cross-chapter consistency inventory refresh at lines 95–96 (replace stale entries with TA-canonical anchors + cross-chapter reconciliation note); (b) op-ed `publishing/op-eds/norway-sovereign-wealth-op-ed_2026-05-10.md` line 26 refresh (currently *"more than $1.9 trillion in assets — roughly $340,000 for every Norwegian alive today"*) — held until op-ed reactivation moment per Stage 1c §3 op-ed-side disposition.

---

## §4. Items verified — no new findings (positive verifications)

Per `feedback_verify_stale_memory_claims.md` discipline applied to Pass-1 Items-verified table: re-verify time-sensitive claims at retrofit time. The following Pass-1 verified claims re-verified clean against current chapter state + canonical sources:

| Claim | Pass-1 line | Current line | Re-verify status |
|---|---|---|---|
| 1969 Ekofisk discovery, North Sea, Block 2/4, Norwegian concession | 7 | 10 | ✓ HOLDS |
| Norway "fewer than four million people" at the time | 7 | 10 | ✓ HOLDS (1969 population ~3.9M; figure refers to 1969 by chapter context) |
| Government Petroleum Fund formally established 1990 | 21 | 24 | ✓ HOLDS |
| Fund invests outside Norway, diversified equities/bonds/real estate | 23 | 26 | ✓ HOLDS |
| 2001 fiscal rule (handlingsregelen) adopted under Stoltenberg I | 29 | 32 | ✓ HOLDS |
| Government chronology sequence: Stoltenberg I → Bondevik II → Stoltenberg II → Solberg → Støre | 29 | 32 | ✓ HOLDS (Bondevik II disambiguator per MEDIUM-2 fix; sequence intact) |
| Investment returns now exceed extraction revenue | 27 | 30 | ✓ HOLDS (per multi-year GPFG annual reports; structurally stable claim) |
| Alberta Heritage Trust Fund established 1976 | 9 | 12 | ✓ HOLDS |
| Nigeria major oil producer since 1950s | 77 | 80 | ✓ HOLDS |
| Niger Delta operators: Shell, Chevron, ExxonMobil, Total | 77 | 80 | ✓ HOLDS (historical-claim accurate; some divestiture activity post-2020 is noted in research/case-studies/nigeria-oil-contrast.md but the historical operator claim holds) |
| UNEP 2011 report on Ogoniland (existence + non-contestation) | 79 | 82 | ✓ HOLDS |
| Ken Saro-Wiwa hanged 1995 | 79 | 82 | ✓ HOLDS (executed 10 November 1995; Ogoni Nine) |
| Nigeria temporarily suspended from Commonwealth post-1995 executions | 79 | 82 | ✓ HOLDS (suspended 11 November 1995; reinstated May 1999) |
| US Social Security designed 1935 | 99 | 102 | ✓ HOLDS |
| US Social Security pay-as-you-go architecture, trust-fund as intra-government accounting record | 95 | 98 | ✓ HOLDS (per research/case-studies/social-security.md; structural-historical claim stable) |
| Climate-vulnerable populations: Bangladesh, Sahel, Pacific island states | 117 | 120 | ✓ HOLDS (standard climate-vulnerability typology) |

**Re-verification result: all Pass-1-verified claims still hold against current chapter state + canonical sources.**

---

## §5. Apparatus regression check

Per Pass-1 §"Apparatus regression check" + Pass-2 §5.3 + Stage 1c §1 apparatus-register-decision reference: Ch 4 honors apparatus register (lowercase prose "cost severance" / "accountability bond B" with single-letter variable / "residual commons value" / "foreclosure component" / "externality tail" / single capitalized "Intergenerational Option Value" at line 124). The rename + cosmetic-header housekeeping commits did not touch apparatus terms. **No apparatus regression detected at Pass 3.1 verify.**

---

## §6. Path B contamination check

Per Pass-1 §"Path B contamination check": Ch 4 does NOT carry verbatim-clone passages from other chapters. The case-study brief at `research/case-studies/norway-swf.md` is copied from Ch 4 (per its 2026-04-22 housekeeping note), so identity-text overlap with that file is expected and correct (Ch 4 is the source). Op-ed `publishing/op-eds/norway-sovereign-wealth-op-ed_2026-05-10.md` per its own §"Path B audit" carries 0 verbatim Ch 4 sentences (verified via grep at op-ed drafting time). **No Path B contamination detected at Pass 3.1 verify.**

---

## §7. Named-subject consent check

Per Pass-1 §"Named-subject consent check": no living named subjects in Ch 4 require consent gating. Norwegian PMs (Stoltenberg, Bondevik II, Solberg, Støre) are named in official capacity (public-record exception per `feedback_named_subject_consent.md`). Ken Saro-Wiwa is deceased (historical-record status; executed 10 November 1995). Niger Delta peoples (Ogoni, Ijaw) named as peoples, not individuals. **No named-subject consent regression at Pass 3.1 verify.**

(Forward-pointer: BookLevelGuidance line 34 flags Norway-citizen interview as outreach priority. If a Norway-voice interview lands post-retrofit, the named-subject would route through the consent discipline. No Ch 4-side change required at this retrofit per Stage 1c §2 disposition.)

---

## §8. Verdict synthesis

### §8.1 Findings tally

| Severity | Count | Findings |
|---|---|---|
| HIGH | 0 | None — all Pass-1 ratified spot-fixes intact; no new fact-check concerns. |
| MEDIUM | 1 | **F-1V-Ch4-1** — TA-verification-round-2026-05-14 canonical-anchor refresh; recommend Phase C application of Option A per §3.3 (extends Pass-1 LOW-2). |
| LOW | 0 | None. |

Total findings: **1** (MEDIUM; promoted from Pass-1 LOW-2 disposition).

### §8.2 Aggregate Pass 3.1 verify verdict

**VERIFIED — 7/7 PASS-1 RATIFIED FIXES INTACT; 1 NEW MEDIUM (TA-CANONICAL REFRESH) ROUTES TO PHASE C.**

The rename + cosmetic-header housekeeping commits did not disturb any of the 5 MEDIUM + 2 LOW Pass-1 spot-fixes. Apparatus register holds; named-subject consent holds; Path B contamination check clean; tense-consistency / register-consistency unaffected by the housekeeping (verified via §5.1–§5.2 inheritance from Pass 2 voice-polish).

The single new MEDIUM finding (F-1V-Ch4-1) extends the Pass-1 LOW-2 disposition ("defer to pre-publication refresh") into an active Phase C update candidate now that the TA verification round 2026-05-14 has landed + Ch 6 line 207 has independently updated. Recommendation: Option A (Ch 4 line 26 updates to TA-canonical end-2025 + April 2025 peak anchors, with cross-chapter consistency inventory refresh + op-ed-side update at op-ed-reactivation moment).

### §8.3 Phase-C disposition recommendation

Author ratifies F-1V-Ch4-1 disposition (Option A / B / C / D / hold) at the eventual Phase C session. The Phase C session is naturally bundled with Pass 3.2 verify dispositions + Pass 3.3 acceptance dispositions + Pass 3.4 robustness dispositions for Ch 4 — author ratification + application combined per Amendment C interactive ratification protocol (pipeline doctrine §3.7).

---

## §9. What this pass did NOT do

Per retrofit handoff §1 + pipeline-doctrine retrofit-template §3.3 + §5 hard constraints:

- **Did NOT re-fire the Pass-1 fact-check.** Verify mode only: re-verifies the ratified-and-applied spot-fixes still hold; flags post-ratification canonical refreshes; does not re-litigate Pass-1 findings.
- **Did NOT apply spot-fixes to the chapter file.** Phase C application session (combined with Pass 3.2 / 3.3 / 3.4 dispositions) applies F-1V-Ch4-1 per author ratification.
- **Did NOT re-litigate Pass-2 PROPOSED findings.** Pass 3.2 verify (this retrofit's next sub-step) does that work.
- **Did NOT score Pass 3.3 / 3.4 (audience-load).** Those are this retrofit's subsequent sub-steps.
- **Did NOT contact named subjects.** Per consent discipline; no living named subjects in Ch 4 require contact.
- **Did NOT propose framework-conceptual edits.** Per Pass-1 + verify-mode template's hard constraint.

---

## §10. Hard constraints honored

- ✓ Did NOT apply spot-fixes to `Chapter__4_TheExistenceProof.md`.
- ✓ Did NOT re-fire Pass 1 fact-check.
- ✓ Verified all 7 Pass-1 ratified spot-fixes intact at line-shifted locations (+3 vs Pass-1 baseline).
- ✓ Verified Pass-1 Items-verified table claims still hold against current chapter state + canonical sources (TA verification round 2026-05-14 incorporated).
- ✓ Verified apparatus register holds (no regression from rename + cosmetic-header commits).
- ✓ Verified Path B contamination check still clean.
- ✓ Verified named-subject consent discipline still clean.
- ✓ Verified TA-verification-round-2026-05-14 canonical anchors against the cited artifact.
- ✓ Verified Pass-1 cited commits (`e67b8b8`, `8f792ee`) exist on `origin/main`.
- ✓ Verified Pass-2 cited commit (`3174cc8`) exists on `origin/main`.
- ✓ Verified chapter rename (`a09e319`) + cosmetic-header (`e1a533e`) commits exist on `origin/main`.
- ✓ Verified registry SHAs for Stage 1a + cross-artifact-coherence-check sources cited correctly.
- ✓ Branch discipline: working from `claude/unruffled-elbakyan-af5b16` (off `origin/main` `de83dcb`) per retrofit handoff branch-discipline.

---

*End of Ch 4 Pass 3.1 verify. PROPOSED — awaits Phase C author ratification of F-1V-Ch4-1 (TA-canonical-anchor refresh; recommended Option A end-2025 + peak). Pass 3.2 verify is the next retrofit sub-step.*
