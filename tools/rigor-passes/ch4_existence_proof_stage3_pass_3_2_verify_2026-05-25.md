# Stage-3 Pass 3.2 Verify — Ch 4 (The Existence Proof)

**Date:** 2026-05-25
**Workstream:** Ch 4 pipeline-retrofit (per [`tools/workstream-handoffs/ch4-pipeline-retrofit-handoff_2026-05-17.md`](../workstream-handoffs/ch4-pipeline-retrofit-handoff_2026-05-17.md))
**Chapter:** 4 — *The Existence Proof*
**File audited:** [`manuscript/chapters/Chapter__4_TheExistenceProof.md`](../../manuscript/chapters/Chapter__4_TheExistenceProof.md) — **140 lines** (post-Pass-1 spot-fix state; post-2026-05-24 publishing-pipeline reorg rename)
**Pass scope:** Pass 3.2 VERIFY of Pass 2 voice-polish findings PROPOSED 2026-05-15 at commit `3174cc8` (NOT YET RATIFIED + APPLIED), against current chapter state.
**Status:** PROPOSED — awaiting Phase C author ratification + application.
**Hard constraint observed:** No spot-fixes applied to the chapter file.

---

## §0. What this pass does

Pass 3.2 verify re-confirms each Pass 2 finding (F-V1 through F-V23) against the current 140-line chapter prose and refines recommendations where line-position drift or interim ratifications affect disposition.

Per pipeline doctrine §3.4 (Amendment A two-class cascade), Pass 3.2 fires in the automatic-on-edit cascade; this verify session fires because:

1. Pass 2 PROPOSED 2026-05-15 at commit `3174cc8`; NOT YET RATIFIED + APPLIED. The verify pass confirms each finding still maps to the current chapter prose at the updated line numbers (post-2026-05-24 publishing-pipeline reorg + Pass 1 spot-fix application together shifted the chapter from 138 lines to 140 lines; all flagged lines remap with a consistent +2 / +3 / +5 offset within the same prose).
2. Walkthrough author ratifications 2026-05-20 already locked F-V1 (Option B replacement text) and F-V2 (new Option D replacement text). These ratifications are carry-forward author input; this verify pass confirms the targeted prose still exists at the updated line numbers and records the locked replacements for Phase C application reference.
3. F-V3 through F-V15 (MEDIUM) and F-V16 through F-V23 (LOW) remain open for verify-pass refinement of recommendations against the current state.

---

## §1. Source artifacts read

1. [`manuscript/chapters/Chapter__4_TheExistenceProof.md`](../../manuscript/chapters/Chapter__4_TheExistenceProof.md) — 140 lines, current HEAD.
2. [`tools/rigor-passes/commons_bonds_rigor_pass_2026-05-15_ch4_existence_proof_stage3_voice_polish_v1.0.0.md`](commons_bonds_rigor_pass_2026-05-15_ch4_existence_proof_stage3_voice_polish_v1.0.0.md) — Pass 2 PROPOSED artifact (23 findings: 3 HIGH + 12 MEDIUM + 8 LOW); full content reviewed.
3. [`tools/rigor-passes/ch4_existence_proof_stage3_pass_3_1_verify_2026-05-25.md`](ch4_existence_proof_stage3_pass_3_1_verify_2026-05-25.md) — Pass 3.1 verify (this retrofit session, sub-step 1); F-R-1 + F-R-2 spot-fixes at line 26 do not collide with any Pass 2 finding's flagged language.
4. [`tools/quality-gates/clean-baselines/ch4_stage1a_2026-05-25.md`](../quality-gates/clean-baselines/ch4_stage1a_2026-05-25.md) — Stage 1a clean baseline (zero regressed-pattern matches for any voice-polish pattern; confirms Pass 2's named-cadence findings are voice-polish-pass concerns rather than registry-tracked regressions).
5. Walkthrough author ratifications 2026-05-20 (carry-forward input per workstream handoff §"Walkthrough author ratifications"): F-V1 → Option B; F-V2 → new Option D.

---

## §2. Line-number remapping (Pass 2 138-line state → current 140-line state)

| Pass 2 finding | Pass 2 line | Current line | Remap-offset |
|---|---|---|---|
| F-V1 | 29 | 32 | +3 |
| F-V2 | 81 | 84 | +3 |
| F-V3 | 115/117/119/121 | 118/120/122/124 | +3 |
| F-V4 | 9 | 12 | +3 |
| F-V5 | 11 | 14 | +3 |
| F-V6 | 15 | 18 | +3 |
| F-V7 | 31 | 34 | +3 |
| F-V8 | 39 | 42 | +3 |
| F-V9 | 49 | 52 | +3 |
| F-V10 | 63 | 68 | +5 |
| F-V11 | 83 | 86 | +3 |
| F-V12 | 95 | 98 | +3 |
| F-V13 | 97 | 100 | +3 |
| F-V14 | 105 | 108 | +3 |
| F-V15 (line 53) | 53 | 56 | +3 |
| F-V15 (line 85) | 85 | 88 | +3 |
| F-V15 (line 105) | 105 | 108 | +3 |
| F-V16 | 23 | 26 | +3 |
| F-V17 | 27 | 30 | +3 |
| F-V18 | 33 | 36 | +3 |
| F-V19 | 43 | 46 | +3 |
| F-V20 | 51 | 54 | +3 |
| F-V21 | 67 | 70 | +3 |
| F-V22 | 131 | 134 | +3 |
| F-V23 | 133 | 136 | +3 |

All 23 findings remap cleanly with the chapter-wide +3 line offset (one finding, F-V10 at line 68, has a +5 offset due to a single intervening blank-line variance in the Pass 1 spot-fix application; the substantive paragraph and the flagged cadence-pattern remain unchanged). The flagged prose text matches verbatim at each remapped line for all 23 findings except where Pass 1 spot-fix application already addressed substantive content (none of the Pass 1 changes touched any Pass 2 flagged line — verified line-by-line below).

---

## §3. HIGH findings — verify dispositions

### F-V1 — Five-declarative chronology cadence-flatness at political-consensus paragraph (HIGH)

**Pass 2 line:** 29; **current line:** 32.

**Current chapter prose at line 32:**

> *"Behind the numbers sits an unusual political phenomenon, which is that none of this has been seriously undone. Norwegian governments have changed. Economic crises have come and gone. Populist pressure to spend the money has surfaced repeatedly. Industry has argued for faster extraction. And the rules have held. A broad political consensus — spanning the center-left and the center-right — has treated the fund's integrity as a non-negotiable element of the national settlement…"*

**Verify disposition.** ✓ Verified — flagged five-declarative cadence present verbatim at line 32. The Pass 1 MEDIUM-2 spot-fix ("Bondevik II's") sits later in the same line-32 paragraph but does NOT touch the five-declarative cadence block.

**Author ratification carry-forward (walkthrough 2026-05-20):** **Option B** selected.

**Locked Phase C replacement text:**

> *"Through changes of government, oil-price downturns, populist spending pressure, and recurring industry argument for faster extraction, the rules have held."*

Replaces the five-declarative block *"Norwegian governments have changed. Economic crises have come and gone. Populist pressure to spend the money has surfaced repeatedly. Industry has argued for faster extraction. And the rules have held."*

Phase C will apply this single-sentence collapse in place of the five sentences. The named declarative-three-extended-to-five cadence dissolves; the institutional-discipline-held-through-stresses claim lands as one sentence carrying four compound objects of "through" + a final-clause punch.

**Verify-pass refinement note.** Option B locks cleanly against current prose — no other prose changes intervened on this paragraph. The surrounding sentences (the topic-introduction "Behind the numbers…" and the immediately-following "A broad political consensus…") remain in place; Option B substitutes only the five-declarative chronology block.

---

### F-V2 — Four-anaphoric "The same X" fragment block at Niger-Delta-pivot paragraph (HIGH)

**Pass 2 line:** 81; **current line:** 84.

**Current chapter prose at line 84:**

> *"The same oil. The same market price. The same global demand curve. Radically different outcomes for the communities whose commons the oil was drawn from. The framework's residual commons value for the Niger Delta is not a small figure. It is enormous. And the accountability bond — the actual revenue captured on behalf of the affected communities, through instruments that reach those communities rather than flowing around them — is, in comparison with Norway's, near zero."*

**Verify disposition.** ✓ Verified — flagged four-fragment anaphoric block present verbatim at line 84.

**Author ratification carry-forward (walkthrough 2026-05-20):** **New Option D** selected (author-added; supersedes Pass 2's Options A/B/C).

**Locked Phase C replacement text:**

> *"The oil, the market price, and the demand curve are all the same as Norway's. The outcomes for the communities whose commons the oil was drawn from are not."*

Replaces the four-sentence block *"The same oil. The same market price. The same global demand curve. Radically different outcomes for the communities whose commons the oil was drawn from."* — i.e., the first four sentences of the line-84 paragraph.

The remainder of the line-84 paragraph (*"The framework's residual commons value for the Niger Delta is not a small figure. It is enormous. And the accountability bond — the actual revenue captured on behalf of the affected communities, through instruments that reach those communities rather than flowing around them — is, in comparison with Norway's, near zero."*) is preserved unchanged.

Phase C will substitute the author's Option D two-sentence pivot for the four-fragment-plus-closer block. The named tidy-parallel-extended-to-four cadence dissolves; the identical-inputs / different-outcomes pivot lands as two parallel-but-not-anaphoric sentences. Note Option D's serial comma + "and" before "the demand curve" forecloses the "The same X / The same Y / The same Z" cadence cleanly while preserving the sameness-and-difference contrast.

**Verify-pass refinement note.** Option D locks cleanly against current prose. The author's Option D is structurally closer to Pass 2's Option A (*"The oil, the market price, the demand curve — all the same as Norway's. The outcomes for the communities whose commons the oil was drawn from are not."*) than to B or C, but substitutes a serial-comma + "and" + "are all the same as Norway's" construction in place of Option A's em-dash construction. The em-dash-density chapter-wide pattern (Pass 2 §"Findings — MEDIUM severity" F-V12) is incrementally lighter under Option D than Option A. Recommended carry-forward.

---

### F-V3 — Four-paragraph anaphoric "It does not…" block at "The part Norway has not solved" §-section (HIGH)

**Pass 2 lines:** 115/117/119/121; **current lines:** 118/120/122/124.

**Current chapter prose at lines 118 / 120 / 122 / 124** — each paragraph opens with *"It does not [verb]…"*:

- Line 118: *"It does not price permanent foreclosure. The barrel is still gone. […]"*
- Line 120: *"It does not close the externality tail. North Sea ecosystems recover slowly where they recover at all. […]"*
- Line 122: *"It does not address the distributional problem at the global scale. Norway's fund compounds, in effect, on the productive output of the global economy. […]"*
- Line 124: *"It does not price the existence of the resource for its Intergenerational Option Value — the possibility that future generations will need the oil not for the applications we currently use it for, but for applications we have not yet imagined. […]"*

**Verify disposition.** ✓ Verified — flagged four-paragraph anaphoric structure present verbatim at lines 118/120/122/124. Pass 1 LOW-1 + LOW-3 spot-fixes did not touch this section; the section's prose is structurally unchanged from the Pass 2 audit baseline.

**Author ratification carry-forward.** NOT YET RATIFIED at walkthrough 2026-05-20. F-V3 remains open for Phase C author ratification across Pass 2's Options A/B/C.

**Verify-pass recommendation refinement.** Pass 2's recommendation set:
- Option A — break the anaphora on one paragraph (e.g., open line 122 differently).
- Option B — convert one or two paragraphs to embedded-thesis form (keep lines 118 + 124 as anaphoric openers; convert lines 120 + 122 to non-anaphoric openers).
- Option C — hold as-is (defensible enumerative cadence at the gap-naming inventory).

This verify pass recommends **Option B as the strongest reduce-pattern-while-preserving-architecture path**, refined as follows: the two openers that are most chapter-spine load-bearing are line 118 (foreclosure-pricing — Ch 5+ instrument-handoff) and line 124 (Intergenerational Option Value — canonical apparatus-introduction site per cross-chapter consistency inventory line 40). Holding the anaphoric "It does not…" at lines 118 + 124 preserves the rhythmic load-bearing positions while converting lines 120 + 122 to substantive non-anaphoric openers reduces the four-deep pattern to two-deep.

**Proposed Option B refined replacement openers (for line 120 + line 122 only; author selects whether to apply):**

- **Line 120 (externality tail).** Replace *"It does not close the externality tail. North Sea ecosystems recover slowly where they recover at all."* with: *"The externality tail also remains open. North Sea ecosystems recover slowly where they recover at all."* — two-sentence opener; first sentence carries the gap-thesis substantively rather than via "It does not" anaphora; second sentence preserves the ecosystem-recovery anchor.
- **Line 122 (global-scale distribution).** Replace *"It does not address the distributional problem at the global scale. Norway's fund compounds, in effect, on the productive output of the global economy."* with: *"The global-scale distributional problem is unresolved. Norway's fund compounds, in effect, on the productive output of the global economy."* — same approach; first sentence carries the gap-thesis substantively; second sentence preserves the compound-on-global-output anchor.

Lines 118 and 124 retain their "It does not [verb]…" openers, preserving the two most load-bearing anaphoric beats at the chapter's most structurally-anchored positions (foreclosure-pricing handoff to Ch 5+ instruments; Intergenerational Option Value introduction site).

Option A and Option C remain available; the refined Option B is what this verify pass recommends to author.

**Severity verify.** HIGH retained — paragraph-level anaphora repeated across four paragraphs is the chapter's highest-cadence-density named pattern outside F-V1 + F-V2. Pass 2's HIGH classification holds.

---

## §4. MEDIUM findings — verify dispositions

For each F-V4 through F-V15 finding, this verify pass confirms the flagged prose exists at the remapped line, summarizes verify-pass refinement of disposition (if any), and notes Phase C author ratification status. None of the MEDIUM findings are author-ratified yet; all remain open for Phase C disposition.

### F-V4 — Tidy-parallel "Some did X. Some did Y." petroleum-state survey (MEDIUM)

**Current line:** 12. **Verify:** ✓ Present verbatim. **Verify-pass disposition:** Pass 2 recommended hold-as-is (substantive survey-follow-through earns the framing) as primary; alternative "Most jurisdictions spend the money. Venezuela, Nigeria, and early-phase Saudi Arabia spent it quickly and badly. Texas, Alberta, and Alaska spent it more carefully…" as backup. **Verify pass concurs with hold-as-is recommendation.** The paragraph's subsequent Alberta + Alaska treatment (lines 12 still, mid-paragraph) substantively follows through; the "Some did X / Some did Y" framing reads as analytical-survey-setup rather than stylized.

### F-V5 — Declarative-three negation-negation-affirmation at decision-was-not-obvious paragraph (MEDIUM)

**Current line:** 14. **Verify:** ✓ Present verbatim. **Verify-pass disposition:** Pass 2 recommended hold-as-is; alternative "The decision was not obvious or inevitable. It was deliberately argued for…" as compound-negation. **Verify pass concurs with hold-as-is.** Sentence-3 length-variance softens the named pattern; the negation-negation-affirmation rhetorically tightens the chapter's existence-proof premise; cadence enacts the substance.

### F-V6 — Double-anaphoric "X is one outcome. Y is another. The variable is not Z. The variable is W." (MEDIUM)

**Current line:** 18. **Verify:** ✓ Present verbatim. **Verify-pass disposition:** Pass 2 recommended hold-as-is; alternative "Appalachia is one outcome. Norway is another. The variable is not geology — it is the institutional architecture that decides who captures the value and who bears the cost." as collapse-second-anaphoric-pair. **Verify pass refines toward the alternative as soft-recommendation** — the stacked anaphora is editor-detectable cadence-density; the alternative preserves the conceptually load-bearing Appalachia/Norway pivot while dissolving the second "The variable is" anaphora into a single em-dashed sentence. Author judgment which to apply.

### F-V7 — Three-declarative "The X would be Y" architecture-design paragraph (MEDIUM)

**Current line:** 34. **Verify:** ✓ Present verbatim. **Verify-pass disposition:** Pass 2 recommended hold-as-is (three-part architecture-design substantively earns three-part cadence); alternative breaks the named anaphora on sentence 3 via "Spending would be rate-limited…" opener-shift. **Verify pass concurs with hold-as-is.** The three-element architecture (revenue-capture / structural-protection / rate-limit) is real; cadence enacts the design-program substance.

### F-V8 — Three-declarative "The X is Y" framework-claim paragraph at §"What the framework says about Norway" opening (MEDIUM)

**Current line:** 42. **Verify:** ✓ Present verbatim. **Verify-pass disposition:** Pass 2 offered three options (hold; one-sentence compression; soften "best in the world" superlative). **Verify pass recommends the soft-superlative alternative as primary** — the named three-declarative pattern can hold (the cadence does setup-work for the §-section's central analytical question) but the "best in the world" unhedged superlative carries audience-load risk for the Pass 3.4 adversarial industry-funded-energy-economist read (where unhedged superlative reads as advocacy rather than analysis). Proposed: *"The rents are captured. The community is compensated. The institutional architecture is widely judged the best in the world."* Adds "widely judged" hedge; preserves three-declarative cadence; protects against adversarial-read framing concern.

### F-V9 — 78-word em-dash mega-parenthetical at petroleum-substitution paragraph (MEDIUM)

**Current line:** 52. **Verify:** ✓ Present verbatim. **Verify-pass disposition:** Pass 2 offered three options (break-into-own-sentence + summary; compress-list-to-3-or-4-elements; hold-as-is). **Verify pass recommends Option A (break-into-own-sentence + summary) as primary** — the 78-word interjection is the chapter's single longest em-dash-bracketed structure and the comparable Ch 1 F-V4 was ratified for unbinding via similar break-into-own-sentence treatment. Proposed two-sentence form: *"Future generations who have no viable substitute for petroleum in their particular application do not regain access to it because the revenue was well-managed. The applications for which no renewable alternative yet exists include medical-grade plastics for surgical instruments and pharmaceutical packaging, aviation jet fuel for the present global commercial fleet, specialty petrochemistry for high-performance polymers and pharmaceutical synthesis, asphalt for road infrastructure, and the carbon-fiber and lubricant chemistries that underwrite both renewable-energy hardware and the manufacturing ecosystems that produce it."*

### F-V10 — Three-declarative "The mechanism… That is not… It is…" cadence at selection-criterion punch paragraph (MEDIUM)

**Current line:** 68. **Verify:** ✓ Present verbatim (with +5 line-offset due to one blank-line drift; the substantive paragraph at line 68 contains the flagged "The mechanism preys on weakness. That is not a bug of the extraction economy. It is its selection criterion." three-declarative closer). **Verify-pass disposition:** Pass 2 recommended hold-as-is (cadence enacts selection-criterion claim); alternative "The mechanism preys on weakness — not as a bug of the extraction economy but as its selection criterion." as compound. **Verify pass concurs with hold-as-is.** The selection-criterion claim is the chapter's strongest mechanism-framing statement; the three-declarative cadence-build is rhetorically earned.

### F-V11 — Stacked-tic decomposition paragraph at Niger-Delta cost-severance section (MEDIUM)

**Current line:** 86. **Verify:** ✓ Present verbatim. **Verify-pass disposition:** Pass 2 offered four options (compress sentences 2+3; break list 4→3; combine A+B; hold-as-is). **Verify pass recommends Option A (compress sentences 2 + 3) as primary** — dropping the "It is large because X. It is not large because Y." anaphoric negation-pair into a single "It is large because B is small, not because the oil is different." sentence reduces the densest local cadence-stacking. The 4-element list at sentence 4 ("The geology, the extraction technology, the product, the market") substantively earns its space (each element is a distinct comparator dimension); holding to four-element rather than dropping to three preserves precision. Combined recommendation: apply A, hold the four-element list.

### F-V12 — Em-dash density (4 em-dashes / 2 parenthetical pairs) at US-Social-Security comparator paragraph (MEDIUM)

**Current line:** 98. **Verify:** ✓ Present verbatim. **Verify-pass disposition:** Pass 2 offered three options (convert sentence-4 pair to semicolon-comma; convert sentence-6 pair to parens; apply both). **Verify pass recommends Option C (apply both) as primary** — the paragraph carries the chapter's highest local em-dash density and reducing both pairs drops the chapter-wide em-dash habit most. Reference: the [em-dash overuse memory](../memory/feedback_em_dash_overuse.md) (ratified 2026-05-21 during Ch 3 Pass 3.2 F-V3 ratification): "treat em-dash use as a flag requiring active justification, not a default punctuation choice." Two paragraph-local em-dash-pair conversions align with that discipline. Author may select Option A or B individually if the cumulative-paragraph-cadence shift is too aggressive at the §"Architecture is a choice" introductory paragraph.

### F-V13 — Three-anaphoric "Both are X" cadence at US-Social-Security comparator (MEDIUM)

**Current line:** 100. **Verify:** ✓ Present verbatim. **Verify-pass disposition:** Pass 2 offered three options (one-sentence compression; drop sentence 2; hold). **Verify pass recommends Option B (drop sentence 2) as primary** — sentence 2 ("Both are intergenerational instruments.") is the most substantively-redundant of the three (architecture and instrument converge); dropping it reduces the three-anaphora to two-statement pivot while preserving the conceptual setup-work the third sentence ("Both are responses to the same problem:") does. Proposed: *"Both are retirement-security architectures. Both are responses to the same problem: how does a society provide for its members' final decades when those members' productive working years have ended?"*

### F-V14 — Stacked-pattern + chiastic constructed→reconstructed coda at architecture-is-engineered paragraph (MEDIUM)

**Current line:** 108. **Verify:** ✓ Present verbatim. **Verify-pass disposition:** Pass 2 offered four options (drop chiastic coda; replace with forward-pointer; compress three-rules tidy-parallel; hold). **Verify pass recommends Option A (drop chiastic coda) as primary** — the "and that what was constructed once can be reconstructed" chiasmus is the third chiastic-coda in the book (Ch 1 F-V9 + F-V11 + Ch 4 F-V14 — Pass 2 §6 flagged this as a possible book-wide cadence-habit). Dropping the Ch 4 chiastic coda preserves the constructed-not-given thesis at sentence-close without the chiastic flourish. The three-rules tidy-parallel inside the paragraph ("the rules a generation builds, the rules it inherits, and the rules it agrees to maintain or replace") is content-driven and substantively-earned; hold-as-is.

### F-V15 — Recurring "[Setup-clause] is this:" expository-frame pattern across three chapter-spine claims (MEDIUM)

**Current lines:** 56 / 88 / 108. **Verify:** ✓ Present at all three remapped lines:
- Line 56: *"The framework's conclusion, applied to Norway, is this:…"*
- Line 88: *"This is what the framework needs to demonstrate to be credible:…"*
- Line 108: *"What the comparison does add to the chapter's argument is this:…"*

**Verify-pass disposition:** Pass 2 offered three options (cut all three; cut one or two; hold all three). **Verify pass recommends Option B (cut two; hold the strongest as deliberate) as primary** — the §-conclusion at line 56 most earns the colon-introducer cadence (it explicitly closes a §-section's analytical claim); lines 88 and 105 are more vulnerable to the chapter-wide expository-flatness pattern. Proposed:
- **Line 56:** Hold as-is.
- **Line 88:** Replace *"This is what the framework needs to demonstrate to be credible: that it differentiates correctly."* with *"The framework needs to demonstrate that it differentiates correctly."* Drops expository frame; substance lands directly.
- **Line 108:** Replace *"What the comparison does add to the chapter's argument is this: when Norway proves…"* with *"The comparison adds the following to the chapter's argument: when Norway proves…"* Drops the cadence-introducer "is this" while preserving the colon-introduction of the broader-thesis-emergence claim.

Cuts two of the three instances; preserves the strongest at line 56 as deliberate §-conclusion cadence. Reduces chapter-wide pattern visibility from three-instance to one-instance.

---

## §5. LOW findings — verify dispositions (default hold-as-is)

Pass 2 recommended hold-as-is across F-V16 through F-V23. This verify pass concurs across the LOW set.

| Finding | Current line | Verify | Verify-pass disposition |
|---|---|---|---|
| F-V16 — five-noun list at per-citizen flourish | 26 | ✓ Present verbatim | Hold-as-is (universality-of-coverage flourish). NOTE: Pass 3.1 F-R-1 + F-R-2 modify the numeric anchors at line 26 but preserve the "— man, woman, child, pensioner, newborn" five-noun list. No collision. |
| F-V17 — "The oil will… The fund will…" two-declarative closer | 30 | ✓ Present verbatim | Hold-as-is (substantive temporal-substitution claim earns the rhythmic cadence). |
| F-V18 — "None of this is magic" meta-frame at §"The architecture" close | 36 | ✓ Present verbatim | Hold-as-is (defensible §-closer rhetorical move). |
| F-V19 — standalone two-statement "It says X. It does not say Y." paragraph | 46 | ✓ Present verbatim | Hold-as-is (deliberate-rhythmic-hinge between sections). |
| F-V20 — "Similarly," sentence-opener + "No fund can." two-word closer | 54 | ✓ Present verbatim | Hold-as-is (lone-instance connective-tissue cliché; not chapter-wide habit). Optional: drop "Similarly," at paragraph-opener. |
| F-V21 — "with X, with Y, with Z" three-element within-sentence tidy-parallel | 70 | ✓ Present verbatim | Hold-as-is (within-sentence enumeration softens the named-pattern visibility). |
| F-V22 — "Neither outcome was inevitable. Both were engineered." chapter-spine punch | 134 | ✓ Present verbatim | Hold-as-is (chapter-spine thesis-distillation moment). |
| F-V23 — "Each one tells…" anaphoric coda at chapter-handoff | 136 | ✓ Present verbatim | Hold-as-is (deliberate-bookend transition to Ch 5). |

---

## §6. Register / tense / apparatus / named-subject re-verification (carried forward from Pass 2 §5)

Pass 2 §5.1-§5.7 verified register-consistency-holds, tense-consistency-holds, no-apparatus-residue-beyond-Pass-1-baseline, hedge-phrases-clean, connective-tissue-clichés-mostly-clean, one chapter-wide expository-flatness pattern (F-V15), and named-subject-register-holds.

**Pass 3.2 verify re-confirms all §5 dispositions remain valid against current chapter prose.** The Stage 1a clean baseline (zero scaffolding leaks; zero regressed-pattern matches) anchors this independently. No new register / tense / apparatus / named-subject concerns surface.

---

## §7. Verdict

### §7.1 Findings tally (carry-forward from Pass 2)

| Severity | Count | Verify status |
|---|---|---|
| HIGH | 3 | F-V1 (RATIFIED Option B per walkthrough 2026-05-20); F-V2 (RATIFIED new Option D per walkthrough 2026-05-20); F-V3 (OPEN; verify-pass refines Option B with proposed line 120 + 122 specific opener-replacements) |
| MEDIUM | 12 | All 12 verified present at remapped lines; all OPEN for Phase C author ratification with verify-pass refinements as noted above |
| LOW | 8 | All 8 verified present at remapped lines; verify-pass concurs with Pass 2 hold-as-is recommendation across the set |

**Total findings:** 23 (3 HIGH + 12 MEDIUM + 8 LOW), all present at remapped current-state line numbers; 2 HIGH author-ratified at walkthrough 2026-05-20; 21 open for Phase C disposition.

### §7.2 Aggregate Pass-3.2-verify verdict

**VERIFIED + 2 HIGH AUTHOR-RATIFIED CARRY-FORWARD + 21 OPEN FOR PHASE C.**

The Pass 2 PROPOSED artifact (commit `3174cc8`, 2026-05-15) maps cleanly to current chapter state (140 lines; consistent +3 / +5 line offset; no Pass 1 spot-fix application touched any Pass 2 flagged line in a way that overrides the finding). All 23 findings remap; all 23 flagged cadence-patterns remain in current prose.

Two HIGH findings already author-ratified at walkthrough 2026-05-20:
- **F-V1: Option B locked.** Replacement text: *"Through changes of government, oil-price downturns, populist spending pressure, and recurring industry argument for faster extraction, the rules have held."*
- **F-V2: new Option D locked.** Replacement text: *"The oil, the market price, and the demand curve are all the same as Norway's. The outcomes for the communities whose commons the oil was drawn from are not."*

One HIGH finding remains open (F-V3 four-paragraph anaphoric "It does not…" block). Verify pass refines Pass 2's Option B with specific proposed opener-replacements for lines 120 + 122 (preserving anaphoric structure at the two most chapter-spine-load-bearing positions: line 118 foreclosure-pricing and line 124 Intergenerational Option Value introduction).

Twelve MEDIUM findings remain open; verify pass refines Pass 2 recommendations as follows:
- **F-V4, F-V5, F-V7, F-V10:** Concur with Pass 2 hold-as-is.
- **F-V6, F-V8, F-V9, F-V11, F-V12, F-V13, F-V14, F-V15:** Verify pass surfaces refined-recommendation primary options (per §4 above), prioritizing pattern-reduction at cadence-density hotspots and reducing the book-wide chiastic-coda pattern + the chapter-wide em-dash habit + the chapter-wide expository-frame pattern.

Eight LOW findings: verify pass concurs with Pass 2 hold-as-is across the set.

### §7.3 Recommended Phase C disposition (sequencing)

Apply at a single Phase C combined-ratification + application session:

1. **Apply F-V1 (Option B) and F-V2 (Option D)** — author-ratified pass-through; no further deliberation needed.
2. **Ratify F-V3 disposition** — verify-pass-refined Option B (opener-replacement at lines 120 + 122) vs Pass 2 Options A or C; apply selected option.
3. **Ratify-and-apply MEDIUM findings F-V6 + F-V8 + F-V9 + F-V11 + F-V12 + F-V13 + F-V14 + F-V15** — verify-pass refined primary options enumerated in §4 above; author selects per-finding.
4. **Hold-confirm MEDIUM findings F-V4 + F-V5 + F-V7 + F-V10** per verify-pass concurrence with Pass 2 hold-as-is.
5. **Hold-confirm all LOW findings F-V16 through F-V23** per verify-pass concurrence with Pass 2 hold-as-is.

Pass 3.1 verify F-R-1 + F-R-2 (line 26 GPFG anchor refresh) may apply in the same Phase C session as a parallel atomic chunk; the two F-R findings target line 26 (different paragraph from any Pass 2 flagged line) and do not collide.

---

## §8. What this pass did NOT do

- **Did NOT re-litigate Pass 2 finding catalog.** Pass 2 PROPOSED 23 findings (3 HIGH + 12 MEDIUM + 8 LOW); verify confirms remap + refines recommendations, does not re-score.
- **Did NOT apply spot-fixes to chapter source.** F-V findings are PROPOSED; Phase C combined ratification + application is a separate session.
- **Did NOT run Pass 3.3 acceptance.** That is sub-step 3 in this same retrofit-recovery session (lands as its own commit per session-protocol checkpoint discipline).
- **Did NOT propose any new findings.** Verify scope confines to existing Pass 2 finding-set + walkthrough 2026-05-20 ratifications.
- **Did NOT re-write paragraphs.** Verify pass surfaces proposed-revision refinements aligned to Pass 2's option-set; final selection is author-side.
- **Did NOT contact named subjects.**

---

## §9. Hard constraints honored

- ✓ Did NOT apply spot-fixes to `Chapter__4_TheExistenceProof.md`.
- ✓ Did NOT re-litigate Pass 2 findings (verify-disposition + recommendation-refinement only).
- ✓ Verified all 23 Pass 2 findings present at remapped line numbers via direct chapter read.
- ✓ Honored F-V1 Option B + F-V2 Option D walkthrough author ratifications as pass-through carry-forward.
- ✓ Branched within worktree per CLAUDE.md branch discipline.
- ✓ Surfaced Pass 3.1 F-R-1 + F-R-2 non-collision with Pass 2 findings at line 26.

---

*End of Ch 4 Stage-3 Pass 3.2 Verify. PROPOSED 2026-05-25 — awaiting Phase C author ratification + application.*
