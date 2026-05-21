# Pass 3.2 Verify — Ch 4 (The Existence Proof) Voice-Polish

**Date:** 2026-05-21
**Workstream:** Ch 4 pipeline-retrofit per [`tools/workstream-handoffs/ch4-pipeline-retrofit-handoff_2026-05-17.md`](../workstream-handoffs/ch4-pipeline-retrofit-handoff_2026-05-17.md)
**Chapter:** 4 — *The Existence Proof*
**File audited:** [`manuscript/chapters/Chapter__4_TheExistenceProof.md`](../../manuscript/chapters/Chapter__4_TheExistenceProof.md) — **141 lines**, post-rename + post-cosmetic-header state
**Branch:** `claude/unruffled-elbakyan-af5b16` (off `origin/main` at `de83dcb`)
**Status:** **PROPOSED** — awaits author ratification at Phase C session.
**Mode:** Pass 3.2 verify (not fresh voice-polish). Re-evaluates the 23 PROPOSED findings from [`commons_bonds_rigor_pass_2026-05-15_ch4_existence_proof_stage3_voice_polish_v1.0.0.md`](commons_bonds_rigor_pass_2026-05-15_ch4_existence_proof_stage3_voice_polish_v1.0.0.md) (commit `3174cc8`) against current chapter state; remaps line numbers; flags findings overtaken by intervening edits; carries remaining findings forward for Phase C author ratification.
**Parent artifact (PROPOSED, not yet ratified):** [`commons_bonds_rigor_pass_2026-05-15_ch4_existence_proof_stage3_voice_polish_v1.0.0.md`](commons_bonds_rigor_pass_2026-05-15_ch4_existence_proof_stage3_voice_polish_v1.0.0.md)

---

## §0. Why this verify pass

Per pipeline-doctrine v1.0.0 retrofit-mode + Ch 4 retrofit handoff §1: Pass 2 voice-polish was PROPOSED at commit `3174cc8` 2026-05-15 (23 findings: 3 HIGH + 12 MEDIUM + 8 LOW) but NOT YET RATIFIED + APPLIED. Two intervening events warrant a verify pass:

1. **Chapter rename + cosmetic header edit.** Commit `a09e319` (rename) + `e1a533e` (cosmetic-header) added `*By Chris Winn*` + horizontal-rule separator + blank lines at the top (purely cosmetic per the commit message). Net effect: chapter is 141 lines vs Pass-2-baseline 138 lines; line numbers shift +3 throughout the body. **No body-prose content change.**
2. **Stage 1c + Pass 3.1 verify completed earlier this session.** Stage 1c identified one Ch 4-side Phase C update candidate (F-1V-Ch4-1 — Norway canonical-anchor refresh at line 26). Pass 3.2 verify must check whether the F-1V-Ch4-1 prose-shape recommendation (Option A: end-2025 + peak; ~10 added words) would interact with any Pass-2 finding disposition at line 26 (current F-V16 LOW disposition: hold-as-is on per-citizen flourish).

Per Amendment C (pipeline doctrine §3.7): Pass 3.2 is an Amendment-C-scoped prose-modifying pass; any new findings beyond the existing PROPOSED Pass-2 inventory must include Options + Recommendation + Reasoning. This verify pass surfaces NO new HIGH or MEDIUM findings beyond what the 2026-05-15 Pass 2 PROPOSED + the 2026-05-21 Pass 3.1 verify already inventory; the existing 23 PROPOSED findings already carry their per-finding option sets in the parent Pass-2 artifact.

---

## §1. Source artifacts read

1. [`commons_bonds_rigor_pass_2026-05-15_ch4_existence_proof_stage3_voice_polish_v1.0.0.md`](commons_bonds_rigor_pass_2026-05-15_ch4_existence_proof_stage3_voice_polish_v1.0.0.md) — PROPOSED Pass 2 voice-polish (23 findings).
2. [`manuscript/chapters/Chapter__4_TheExistenceProof.md`](../../manuscript/chapters/Chapter__4_TheExistenceProof.md) — current state (141 lines).
3. [`ch4_stage3_pass_3_1_verify_2026-05-21.md`](ch4_stage3_pass_3_1_verify_2026-05-21.md) — this session's Pass 3.1 verify (F-1V-Ch4-1 Phase C update candidate at line 26).
4. [`tools/quality-gates/coherence-checks/ch4_stage1c_2026-05-21.md`](../quality-gates/coherence-checks/ch4_stage1c_2026-05-21.md) — Stage 1c verdict CLEAN.
5. [`tools/rigor-passes/commons_bonds_rigor_pass_2026-05-11_apparatus_register_decision_v1.0.0.md`](commons_bonds_rigor_pass_2026-05-11_apparatus_register_decision_v1.0.0.md) — apparatus register canonical decisions.
6. Memory: [`feedback_em_dash_overuse.md`](/Users/c17n/.claude/projects/-Users-c17n-commons-bonds/memory/feedback_em_dash_overuse.md) — em-dash overuse discipline (ratified 2026-05-21 during Ch 3 Pass 3.2 F-V3 ratification; load-bearing for F-V9 + F-V12 re-evaluation in this verify pass).

---

## §2. Line-number remapping table (Pass-2 → current)

All 23 PROPOSED findings remap +3 lines uniformly (rename + cosmetic-header housekeeping commits did not touch body prose).

| Pass-2 ID | Severity | Pass-2 line | Current line | Verbatim-text verification (spot-check) |
|---|---|---|---|---|
| F-V1 | HIGH | 29 | **32** | ✓ HOLDS — *"Norwegian governments have changed. Economic crises have come and gone. Populist pressure to spend the money has surfaced repeatedly. Industry has argued for faster extraction. And the rules have held."* five-declarative cadence intact. |
| F-V2 | HIGH | 81 | **84** | ✓ HOLDS — *"The same oil. The same market price. The same global demand curve. Radically different outcomes for the communities whose commons the oil was drawn from."* four-fragment anaphoric block intact. |
| F-V3 | HIGH | 115/117/119/121 | **118 / 120 / 122 / 124** | ✓ HOLDS — all four paragraphs open with *"It does not [verb]…"* anaphoric pattern at remapped line numbers. |
| F-V4 | MEDIUM | 9 | **12** | ✓ HOLDS — *"Some of them do it quickly and badly — Venezuela, Nigeria, early-phase Saudi Arabia. Some do it more carefully, with more to show for it — Texas, Alberta, Alaska."* tidy-parallel framing intact. |
| F-V5 | MEDIUM | 11 | **14** | ✓ HOLDS — *"The decision was not obvious. It was not inevitable. It was deliberately argued for, debated, and then structurally enforced…"* negation-negation-affirmation cadence intact. |
| F-V6 | MEDIUM | 15 | **18** | ✓ HOLDS — *"Appalachia is one outcome. Norway is another. The variable is not geology. The variable is the institutional architecture…"* double-anaphoric pair intact. |
| F-V7 | MEDIUM | 31 | **34** | ✓ HOLDS — *"The revenue would be captured by the state. The capture would be placed in a structure that could not be looted by any single government. And the spending would be rate-limited to the income the capital itself generated."* three-declarative passive intact. |
| F-V8 | MEDIUM | 39 | **42** | ✓ HOLDS — *"The rents are captured. The community is compensated. The institutional architecture is the best in the world."* three-declarative *"best in the world"* intact. |
| F-V9 | MEDIUM | 49 | **52** | ✓ HOLDS — 78-word em-dash mega-parenthetical (*"— the specific chemistries, materials, and products for which no renewable alternative yet exists, including medical-grade plastics for surgical instruments and pharmaceutical packaging, aviation jet fuel for the present global commercial fleet, specialty petrochemistry for high-performance polymers and pharmaceutical synthesis, asphalt for road infrastructure, and the carbon-fiber and lubricant chemistries that underwrite both renewable-energy hardware and the manufacturing ecosystems that produce it —"*) intact. **NOTE — em-dash overuse memory addendum (ratified 2026-05-21):** the post-Pass-2 ratification of `feedback_em_dash_overuse.md` adds weight to F-V9's recommendation; the em-dash-as-default discipline applies to F-V9 + F-V12 disposition at Phase C. |
| F-V10 | MEDIUM | 63 | **66** | ✓ HOLDS — *"The mechanism preys on weakness. That is not a bug of the extraction economy. It is its selection criterion."* three-declarative selection-criterion punch intact. |
| F-V11 | MEDIUM | 83 | **86** | ✓ HOLDS — *"The cost severance, in the framework's terms, is very large. It is large because B is small. It is not large because the oil is different. The geology, the extraction technology, the product, the market — all comparable."* stacked-tic decomposition intact. |
| F-V12 | MEDIUM | 95 | **98** | ✓ HOLDS — 4-em-dash density paragraph (US Social Security comparator) intact. **NOTE — same em-dash overuse memory weight as F-V9.** |
| F-V13 | MEDIUM | 97 | **100** | ✓ HOLDS — *"Both are retirement-security architectures. Both are intergenerational instruments. Both are responses to the same problem: …"* three-anaphoric cadence intact. |
| F-V14 | MEDIUM | 105 | **108** | ✓ HOLDS — *"There are no naturally-occurring distributional outcomes. There are only the rules a generation builds, the rules it inherits, and the rules it agrees to maintain or replace. Norway's existence proof is, in this larger sense, an existence proof for the universal proposition that architecture is constructed, not given — and that what was constructed once can be reconstructed."* stacked-pattern + chiastic coda intact. |
| F-V15 | MEDIUM | 53 / 85 / 105 | **56 / 88 / 108** | ✓ HOLDS — *"[Setup-clause] is this:"* chapter-wide pattern at all three instances. Line 56: *"The framework's conclusion, applied to Norway, is this:"* Line 88: *"This is what the framework needs to demonstrate to be credible:"* Line 108: *"What the comparison does add to the chapter's argument is this:"* |
| F-V16 | LOW | 23 | **26** | ✓ HOLDS — *"…roughly three hundred and forty thousand dollars for every person in the country — man, woman, child, pensioner, newborn."* five-noun universality-of-coverage list intact. **CROSS-PASS NOTE — F-V16 may be touched by Pass 3.1 F-1V-Ch4-1 disposition; see §3 below.** |
| F-V17 | LOW | 27 | **30** | ✓ HOLDS — *"The oil will eventually be gone. The fund will remain."* two-declarative closer intact. |
| F-V18 | LOW | 33 | **36** | ✓ HOLDS — *"None of this is magic. It is institutional design, maintained across generations by people who understood what they were preventing."* meta-frame intact. |
| F-V19 | LOW | 43 | **46** | ✓ HOLDS — *"It says the cost severance has been dramatically reduced. It does not say the cost severance is zero."* standalone two-statement paragraph intact. |
| F-V20 | LOW | 51 | **54** | ✓ HOLDS — *"Similarly,"* paragraph-opener + *"No fund can."* two-word closer intact at line 54. |
| F-V21 | LOW | 67 | **70** | ✓ HOLDS — *"with a deliberately constructed accountability bond, with a political settlement that treats the commons as belonging to the commons, with rules designed to outlast the generation that writes them"* three-element within-sentence parallel intact. |
| F-V22 | LOW | 131 | **134** | ✓ HOLDS — *"Neither outcome was inevitable. Both were engineered."* chapter-spine punch intact. |
| F-V23 | LOW | 133 | **136** | ✓ HOLDS — *"Each one tells part of the answer. Each one tells part of the warning."* anaphoric bookend intact. |

**Verification result: 23 of 23 PROPOSED Pass-2 findings intact at line-shifted (+3) locations.** No body-prose content drift; all named-pattern cadences at original locations verbatim. Pass 2's §5 (Register / tense / apparatus / named-subject) verifications similarly unaffected by the housekeeping commits (apparatus register holds per this session's Stage 1c §1 + Pass 3.1 verify §5; named-subject consent discipline holds per Pass 3.1 verify §7).

---

## §3. Cross-pass coherence: Pass 3.1 F-1V-Ch4-1 ↔ Pass 3.2 F-V16

**Cross-pass flag.** This retrofit's Pass 3.1 verify surfaced F-1V-Ch4-1 (TA-canonical-anchor refresh at line 26; Recommended Option A: end-2025 + peak; ~10 added words to the sentence cluster). Pass 2 F-V16 is a LOW-disposition hold-as-is on the same sentence cluster (the universality-of-coverage flourish closing the per-citizen sentence).

**Interaction analysis:** Option A's prose insertion (Pass 3.1 §3.3) preserves F-V16's flourish structure verbatim:

- Pre-refresh: *"…roughly three hundred and forty thousand dollars for every person in the country — man, woman, child, pensioner, newborn."*
- Post-refresh (Option A): *"…roughly three hundred and fifty-six thousand dollars for every person in the country — three hundred and ninety-one thousand at the 2025 peak — man, woman, child, pensioner, newborn."*

The five-noun universality-of-coverage tail (*"man, woman, child, pensioner, newborn"*) is preserved unchanged. The intervening em-dash-bracketed parenthetical (*"— three hundred and ninety-one thousand at the 2025 peak —"*) is a new em-dash pair, which interacts with the em-dash overuse memory addendum (`feedback_em_dash_overuse.md`, ratified 2026-05-21) — but it carries substantive content (the peak-figure anchor) that the prose needs.

**Disposition recommendation:** When F-1V-Ch4-1 Option A applies at Phase C, F-V16 disposition holds (hold-as-is on the flourish structure). If author prefers a non-em-dash form for the peak-figure parenthetical, Option B (single-point end-2025) per Pass 3.1 §3.3 is the cleaner alternative; it requires Ch 6 line 207 to specify "early 2025 peak" rather than "early 2025" to avoid cross-chapter temporal ambiguity. Author judgment which Option to apply at Phase C.

**No other Pass-2 findings interact with the Pass-3.1 F-1V-Ch4-1 recommendation.** Lines 28 (3% fiscal rule per Pass 3.1 §3.1 verified holds) + line 48 (70-80% capture per Pass 3.1 §3.1 verified holds) are not touched by F-1V-Ch4-1; their Pass-2 dispositions (no Pass-2 findings at lines 28 or 48 directly) stand unchanged.

---

## §4. Findings overtaken by intervening edits

**None.** The intervening commits (`a09e319` rename + `e1a533e` cosmetic-header) did not touch body prose; no Pass-2 finding was overtaken. All 23 PROPOSED findings remain valid against current chapter state.

---

## §5. Apparatus + named-subject + Path B re-verifications

Re-verified at Pass 3.1 verify §5 + §6 + §7 (this retrofit's prior sub-step); inherited here without re-litigation. Pass-2 §5.3 + §5.7 apparatus + named-subject checks hold.

---

## §6. Verdict synthesis

### §6.1 Findings tally

**No new findings beyond the 23 PROPOSED Pass-2 findings inventoried 2026-05-15 + the 1 cross-pass-coherence note at §3 above.**

| Severity | Count (Pass 2 PROPOSED + this verify pass) | Findings |
|---|---|---|
| HIGH | 3 (carried forward from Pass 2) | F-V1, F-V2, F-V3 |
| MEDIUM | 12 (carried forward from Pass 2) | F-V4 through F-V15 |
| LOW | 8 (carried forward from Pass 2) | F-V16 through F-V23 |

Total carry-forward findings: **23** (3 HIGH + 12 MEDIUM + 8 LOW).
Findings overtaken: **0.**
Cross-pass coherence notes: **1** (F-V16 ↔ F-1V-Ch4-1; see §3).

### §6.2 Aggregate Pass 3.2 verify verdict

**VERIFIED — 23/23 PASS-2 FINDINGS INTACT; 0 OVERTAKEN; 1 CROSS-PASS COHERENCE NOTE FLAGGED FOR PHASE C.**

The Pass-2 voice-polish PROPOSED state is preserved verbatim under the +3 line-shift; the rename + cosmetic-header housekeeping commits did not affect any Pass-2 finding's substrate. The em-dash overuse discipline ratified 2026-05-21 (post-Pass-2-PROPOSED) adds weight to F-V9 + F-V12 dispositions at Phase C without surfacing new findings — both findings already carry em-dash-density-reduction options in the parent artifact.

### §6.3 Phase-C disposition recommendation (extends Pass-2 §8.3)

The Phase-C sequencing recommendation from Pass-2 §8.3 carries forward unchanged + extends to incorporate the cross-pass coherence note + Pass 3.1 F-1V-Ch4-1:

1. **Apply F-V1 + F-V2 + F-V3 (all three HIGH).** Per Pass-2 §8.3 sequencing.
2. **Review F-V9 + F-V12 (em-dash-density pair).** Per Pass-2 §8.3 + reinforced by `feedback_em_dash_overuse.md` ratified 2026-05-21.
3. **Review F-V15 (chapter-wide "[Setup] is this:" expository-frame pattern).** Per Pass-2 §8.3.
4. **Apply F-1V-Ch4-1 (TA-canonical-anchor refresh; recommended Option A) at line 26.** Pass 3.1 verify recommendation; updates the GPFG AUM + per-citizen anchors to TA-canonical end-2025 + April 2025 peak. F-V16 disposition holds (universality-of-coverage flourish preserved).
5. **Review F-V8 + F-V11 + F-V13 + F-V14 (the four MEDIUM findings most likely to flag for a trade-press editor).** Per Pass-2 §8.3.
6. **Hold F-V4 + F-V5 + F-V6 + F-V7 + F-V10 (five substantively-earned MEDIUM findings).** Per Pass-2 §8.3.
7. **Hold F-V16 through F-V23 (all 8 LOW findings).** Per Pass-2 §8.3.

Per Amendment C interactive ratification protocol (pipeline doctrine §3.7): the Phase C application session is combined with author ratification — author walks through each finding with Options + Recommendation + Reasoning (the Pass-2 artifact's per-finding option sets carry forward verbatim; F-1V-Ch4-1 per Pass 3.1 §3.3 carries Options A/B/C/D + Recommendation A + Reasoning).

---

## §7. What this pass did NOT do

Per retrofit handoff §1 + pipeline-doctrine retrofit-template §3.4 + §5 hard constraints:

- **Did NOT re-fire fresh Pass-2 voice-polish.** Verify mode only: re-evaluates the PROPOSED findings against current chapter state; remaps line numbers; flags overtaken findings; does not re-litigate Pass-2 cadence calls.
- **Did NOT apply spot-fixes to the chapter file.** Phase C application session (combined with Pass 3.1 F-1V-Ch4-1 + Pass 3.3 / 3.4 dispositions) applies per author ratification.
- **Did NOT score Pass 3.3 / 3.4 (audience-load).** Those are this retrofit's subsequent sub-steps.
- **Did NOT propose new findings beyond the Pass-2 inventory + the 1 cross-pass coherence note.** The em-dash overuse memory addendum adds weight to existing findings; does not surface new ones.

---

## §8. Hard constraints honored

- ✓ Did NOT apply spot-fixes to `Chapter__4_TheExistenceProof.md`.
- ✓ Did NOT re-fire fresh Pass-2 voice-polish.
- ✓ Verified all 23 PROPOSED Pass-2 findings intact at line-shifted (+3) locations.
- ✓ Verified Pass-2 cited commit (`3174cc8`) exists on `origin/main` + the post-Pass-2 housekeeping commits (`a09e319` + `e1a533e`) exist on `origin/main`.
- ✓ Verified apparatus register holds (inherited Pass 3.1 verify §5).
- ✓ Verified named-subject consent + Path B contamination clean (inherited Pass 3.1 verify §6–7).
- ✓ Cross-pass coherence flagged for Phase C author disposition (F-V16 ↔ F-1V-Ch4-1).
- ✓ Branch discipline: working from `claude/unruffled-elbakyan-af5b16` (off `origin/main` `de83dcb`) per retrofit handoff.
- ✓ Amendment C compliance: this verify pass surfaces no new findings beyond the Pass-2 inventory + 1 cross-pass coherence note; the Pass-2 artifact's per-finding option sets carry forward as the Amendment-C-required Options + Recommendation + Reasoning per finding.

---

*End of Ch 4 Pass 3.2 verify. PROPOSED — awaits Phase C author ratification of the 23 Pass-2 findings + the cross-pass coherence flag (F-V16 ↔ F-1V-Ch4-1). Pass 3.3 audience-load acceptance is the next retrofit sub-step.*
