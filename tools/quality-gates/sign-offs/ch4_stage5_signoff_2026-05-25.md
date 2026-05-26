# Commons Bonds — Ch 4 *The Existence Proof* — Stage 5 Bookend Pre-Submission Sign-Off + Stage 4 Bundled Disposition

**Date drafted:** 2026-05-25
**Status:** **RATIFIED 2026-05-25** — Phase C application complete; chapter is READY-TO-SUBMIT. See §11 ratification record + Phase C application log.
**Stage:** Stage 5 bookend pre-submission sign-off per v3.1 (Amendment B 5-pass + Amendment A two-class cascade) doctrine. Stage 4 ratification bundled per Ch 6 (`533f4f6`) + Ch 2 (`cd2c76d`) + Ch 1 (`fb25c9c` adjacent) precedents.
**Workstream context:** Ch 4 is the **fifth book-chapter** to fire Stage 5 (after TA + Ch 6 + Ch 2 + Ch 1). Format precedents mirrored: Ch 6 / Ch 2 / Ch 1 chapter-class sign-offs at `tools/quality-gates/sign-offs/`.

**Artifact under sign-off:** [`manuscript/chapters/Chapter__4_TheExistenceProof.md`](../../../manuscript/chapters/Chapter__4_TheExistenceProof.md) — 140 lines / ~4,030 words (post-Pass-1 spot-fix state, commits `e67b8b8` + `8f792ee` 2026-05-12/13; pre-Pass-2 application — Pass 2 spot-fixes ratified in verify pass but not yet applied to chapter source).

**Pre-publication review queue companion:** [`tools/pre-submission-reviews/ch4_pre_pub_queue_2026-05-25.md`](../../pre-submission-reviews/ch4_pre_pub_queue_2026-05-25.md) (PROPOSED in parallel commit).

**Cross-references (full Stage 3 + Stage 1 cascade):**
- Stage 1a clean-baseline: [`tools/quality-gates/clean-baselines/ch4_stage1a_2026-05-25.md`](../clean-baselines/ch4_stage1a_2026-05-25.md) — CLEAN BASELINE (0 HIGH / 0 MEDIUM / 0 LOW; ~80 patterns scanned).
- Stage 1c cross-artifact coherence-check: [`tools/quality-gates/coherence-checks/ch4_stage1c_2026-05-25.md`](../coherence-checks/ch4_stage1c_2026-05-25.md) — COHERENCE VERIFIED with 5 MEDIUM flags (primary: GPFG anchor staleness vs. TA verification round 2026-05-14 canonical).
- Pass 3.1 fact-check baseline: [`tools/rigor-passes/commons_bonds_rigor_pass_2026-05-12_ch4_existence_proof_stage3_fact_check_v1.0.0.md`](../../rigor-passes/commons_bonds_rigor_pass_2026-05-12_ch4_existence_proof_stage3_fact_check_v1.0.0.md) RATIFIED + APPLIED (5 MEDIUM + 2 LOW spot-fixes applied via commits `e67b8b8` + `8f792ee`).
- Pass 3.1 verify (2026-05-25 retrofit): [`tools/rigor-passes/ch4_existence_proof_stage3_pass_3_1_verify_2026-05-25.md`](../../rigor-passes/ch4_existence_proof_stage3_pass_3_1_verify_2026-05-25.md) — RATIFIED-APPLIED prior findings verified realized; 0 HIGH + 2 MEDIUM newly routed (F-R-1 GPFG AUM line-26 refresh; F-R-2 per-citizen line-26 refresh) — both pending Phase C application.
- Pass 3.2 voice-polish baseline: [`tools/rigor-passes/commons_bonds_rigor_pass_2026-05-15_ch4_existence_proof_stage3_voice_polish_v1.0.0.md`](../../rigor-passes/commons_bonds_rigor_pass_2026-05-15_ch4_existence_proof_stage3_voice_polish_v1.0.0.md) PROPOSED at commit `3174cc8` (23 findings; 3 HIGH + 12 MEDIUM + 8 LOW).
- Pass 3.2 verify (2026-05-25 retrofit): [`tools/rigor-passes/ch4_existence_proof_stage3_pass_3_2_verify_2026-05-25.md`](../../rigor-passes/ch4_existence_proof_stage3_pass_3_2_verify_2026-05-25.md) — all 23 findings verified at remapped line offsets; F-V1 Option B + F-V2 Option D LOCKED as author-ratified pass-through per walkthrough 2026-05-20; F-V3 refined Option B; MEDIUM-cluster recommendations refined; LOW concur hold-as-is.
- Pass 3.3 acceptance: [`tools/rigor-passes/ch4_existence_proof_stage3_pass_3_3_acceptance_2026-05-25.md`](../../rigor-passes/ch4_existence_proof_stage3_pass_3_3_acceptance_2026-05-25.md) — **25/25 INCLUDE** (5 ✓✓✓ + 15 ✓✓ + 5 ✓; 0 NEUTRAL/EXCLUDE); Tier 1 0 ⚠⚠⚠ → **NO SHIP BLOCK**.
- Pass 3.4 robustness: [`tools/rigor-passes/ch4_existence_proof_stage3_pass_3_4_robustness_2026-05-25.md`](../../rigor-passes/ch4_existence_proof_stage3_pass_3_4_robustness_2026-05-25.md) — **ROBUST verdict**; thread-pull synthesis surfaces T1/T3/T4/T6/T7 load-bearing claims (chapter's structural disarms hold); T2 routes to Ch 6/TA Pass 3.4 (already RATIFIED); T4 flagged for Pass 3.5 developmental-edit candidate (lines 32-36 scene-anchor restoration).
- Cross-chapter consistency-inventory: [`tools/audits/cross-chapter-consistency-inventory_2026-05-11.md`](../../audits/cross-chapter-consistency-inventory_2026-05-11.md) (linter-modified intentionally; Norway / GPFG rows need refresh per Stage 1c §3-cross-corpus disposition).
- Pipeline doctrine v3.1: [`tools/commons_bonds_pipeline_doctrine_v1.0.0.md`](../../commons_bonds_pipeline_doctrine_v1.0.0.md).
- Stage 5 doctrine: [`tools/commons_bonds_pipeline_doctrine_stage_5_v1.0.0.md`](../../commons_bonds_pipeline_doctrine_stage_5_v1.0.0.md).
- Ch 4 pipeline-retrofit handoff: [`tools/workstream-handoffs/ch4-pipeline-retrofit-handoff_2026-05-17.md`](../../workstream-handoffs/ch4-pipeline-retrofit-handoff_2026-05-17.md).

---

## §0. Why this pass matters now

Stage 5 is the bookend pre-submission sign-off — the symmetric pair to the Stage 1 ratification gate. Stage 1 verified the ready-to-draft brief; Stage 5 verifies no drift occurred through the pipeline + generates the academic-rigor + prose-quality verification + pre-publication review queue artifact. Per pipeline doctrine v3.1 Amendment A two-class cascade, Stage 5 fires explicit-gate at pre-submission gates: pre-publication, cross-chapter workstream close, or author "build it now" trigger.

This sign-off fires after a full Ch 4 pipeline-retrofit (Stages 1a + 1c + Passes 3.1 verify + 3.2 verify + 3.3 acceptance + 3.4 robustness) and consolidates the cumulative verdict from all retrofit sub-steps. Per Ch 1 / Ch 6 / Ch 2 corpus precedent, Stage 4 render-audit disposition is bundled into this Stage 5 artifact at §8.

**Trigger for this firing:** Author 2026-05-25 instruction completing the Ch 4 pipeline-retrofit cycle ("ratify as recommended" closing on Option A: fresh Ch 4 pipeline-retrofit session). Two-agent parallel split delivered Stages 1a + 1c (recovered from dead first-agent worktree `agent-a26d044bd1e7bfa28`) + Pass 3.1 verify + Pass 3.2 verify + Pass 3.3 acceptance (recovered from agent #1 worktree `agent-afe3d6f29d7dc6eb9`) + Pass 3.4 robustness (recovered from agent #2 worktree `agent-ab6aebab9c2e9ff85`); Stage 4 + Stage 5 (this artifact + pre-pub queue) executed synchronously in the PM session given consistent agent-environment failures (sandbox-block on git operations + API socket errors).

---

## §1. Workstream context + Stage 5 scope

### §1.1 Cumulative state of Ch 4 retrofit cascade

| Stage / Pass | Date | Verdict | Disposition | Commit |
|---|---|---|---|---|
| Stage 1 (retrofit) | (pre-2026-05-12) | RATIFIED via retrofit | Existing chapter prose serves as canonical reference per Stage 1 doctrine §5 (audit-existing-prose retrofit mode) | (prior commits) |
| Stage 1a invariant-gate | 2026-05-25 | CLEAN BASELINE | 0 HIGH / 0 MEDIUM / 0 LOW; ~80 patterns scanned | `b278c1c` |
| Stage 1c coherence-check | 2026-05-25 | COHERENCE VERIFIED with 5 MEDIUM flags | Primary: GPFG anchor staleness (Ch 4 line 26 cites $1.9T / $340K; new TA canonical $2.0T / $356K-$391K). Sibling-side flagged for inventory + Ch 6 + op-ed refresh. | `b278c1c` |
| Pass 3.1 fact-check baseline | 2026-05-12 | RATIFIED + APPLIED | 5 MEDIUM + 2 LOW spot-fixes (GPFG 2006 rename; Bondevik II disambiguation; UNEP $1B rewrite; Alaska 1976 cross-corpus; Bismarck 1889 + 1920s; Equinor 2018 rename; canonical-facts-inventory footnote) | `e67b8b8` + `8f792ee` |
| Pass 3.1 verify (retrofit) | 2026-05-25 | RATIFIED + 2 MEDIUM newly routed | All prior fixes realized; F-R-1 (GPFG AUM line 26) + F-R-2 (per-citizen line 26) propose Phase C language for TA-canonical refresh | `7e390c8` |
| Pass 3.2 voice-polish baseline | 2026-05-15 | PROPOSED | 23 findings (3 HIGH + 12 MEDIUM + 8 LOW); F-V1 + F-V2 author-ratified via walkthrough 2026-05-20 (carry-forward) | `3174cc8` |
| Pass 3.2 verify (retrofit) | 2026-05-25 | RATIFIED with refined recommendations | All 23 findings verified at remapped line offsets; F-V1 Option B + F-V2 Option D LOCKED; F-V3 refined Option B; MEDIUM-cluster refined recommendations; LOW concur hold-as-is | `7e390c8` |
| Pass 3.3 acceptance | 2026-05-25 | INCLUDE — CHAPTER SHIPS | 25/25 INCLUDE (5 ✓✓✓ + 15 ✓✓ + 5 ✓); Tier 1 0 ⚠⚠⚠ NO SHIP BLOCK; Tier 2 + Tier 3 8/8 + 12/12 INCLUDE | `7e390c8` |
| Pass 3.4 robustness | 2026-05-25 | ROBUST | 8 adversarial characters EXCLUDE-as-expected per verdict-floor; thread-pull synthesis surfaces T1-T7 load-bearing claims (chapter's structural disarms hold); no chapter-disqualifying threads chapter-disarmable | `3a5c03f` |
| Pass 3.5 developmental-edit | NOT YET FIRED | DEFERRED | Pass 3.5 is explicit-gate per pipeline doctrine v3.1 Amendment B; flagged at Pass 3.4 T4 as candidate (lines 32-36 NBIM/transparency/ethics-council/Storting-consensus scene-anchor restoration); fires at author trigger via [developmental-edit workstream](../../workstream-handoffs/developmental-edit-workstream-handoff_2026-05-18.md) | (n/a) |
| Stage 4 render + character-integrity audit | 2026-05-25 | **RATIFIED as AUTHOR-COMPLETED-OFFLINE** per author 2026-05-25 direction; verdict CLEAN (matches Ch 1 + Ch 2 + Ch 6 patterns) | See §8 | (this artifact) |

**Retrofit cascade COMPLETE for the in-scope 8 sub-steps** (1a + 1c + 3.1 verify + 3.2 verify + 3.3 + 3.4 + 4 + 5). Pass 3.5 developmental-edit remains DEFERRED per explicit-gate cascade discipline (not in retrofit scope; author triggers separately).

### §1.2 Scope of this sign-off

In scope:
- Pipeline-drift verification across Stage 1 retrofit → Stage 2 → Stage 3 (4 passes via 3.1 + 3.2 + 3.3 + 3.4) → Stage 4 (audit-mode + author-offline flag).
- Academic-rigor sign-off (per-claim verification status across the chapter).
- Prose-quality sign-off (voice register + apparatus exclusion + scaffolding + Path B compliance + sentence-rhythm).
- Pre-publication review queue artifact ratification (companion file).
- Outstanding Phase C application items documentation (Pass 2 spot-fixes + GPFG anchor refresh — pending author ratification + application session).
- Cross-chapter coherence forward-flags (cross-chapter consistency inventory + Ch 6 + op-ed inventory anchor-refresh sibling routing).
- Aggregate Stage 5 verdict.
- Stage 4 render-audit bundled ratification marker.

Out of scope:
- Re-running prior retrofit sub-passes (all RATIFIED).
- Applying chapter-text edits (PROPOSED artifact only — Phase C is the application session).
- Pass 3.5 developmental-edit (DEFERRED per explicit-gate cascade).
- Contacting named subjects.
- Cover-letter / pitch-email assembly (chapter-class does not have cover-letter session).

---

## §2. Pipeline-drift verification

### §2.1 Stage 1 → Stage 2 → Stage 3 → Stage 4 drift verification

**Stage 1 (ready-to-draft brief):** Audit-existing-prose retrofit mode — existing chapter prose serves as canonical reference. No drift to verify (chapter pre-dates pipeline doctrine v3.1; Stage 1 retrofit-ratifies the existing prose's argumentative scope + audience-aware structure + fact-ground).

**Stage 2 (audience-blind drafting):** Pre-doctrine. Chapter exists as Stage-2-output. No drift verification applicable.

**Stage 3 (5-pass rigor cycle):** 4 of 5 passes complete (3.1 + 3.2 + 3.3 + 3.4); Pass 3.5 DEFERRED per explicit-gate cascade. No regression detected:
- Pass 3.1 baseline fixes (5 MEDIUM + 2 LOW) verified realized in current prose per Pass 3.1 verify §2.
- Pass 3.1 verify-newly-routed F-R-1 + F-R-2 (GPFG anchor refresh) consistent with Stage 1c F-1c-1 (anchor staleness flag); routed to Phase C.
- Pass 3.2 baseline (PROPOSED 23 findings) verified all present at remapped line offsets (+3/+5 chapter-wide offset post-Pass-1 application) per Pass 3.2 verify §2.
- Pass 3.2 walkthrough ratifications (F-V1 Option B + F-V2 Option D) verified locked + carry-forward.
- Pass 3.3 acceptance 25/25 INCLUDE result consistent with chapter's argumentative posture (Norway-as-existence-proof + non-prescriptive scope-discipline + comparative cases).
- Pass 3.4 robustness ROBUST verdict consistent with chapter's structural disarms (lines 62-72 institutional-foundations + line 100 architectural-contingency + line 106 non-prescriptive disclaimer + line 122 partial-not-universal + line 72 "build deliberately, against the resistance").

**Stage 4 (render + character-integrity audit):** AUDIT-MODE CLEAN per §8 detail. No render-side drift detected against the registered pattern set; author-offline render-pipeline verification flagged as pre-publication-gate item.

**Stage 5 (this artifact):** No drift detected in the cumulative verdict-aggregation pass.

**Verdict: NO DRIFT.** Pipeline cascade is internally consistent.

### §2.2 Pass-2 application gap

**Material outstanding:** Pass 3.2 verify identified spot-fixes that are NOT YET APPLIED to chapter source. This is the central Phase C-application item:

- **F-V1 (line 32; was line 29 pre-Pass-1):** Author-ratified Option B replacement: *"Through changes of government, oil-price downturns, populist spending pressure, and recurring industry argument for faster extraction, the rules have held."*
- **F-V2 (line ~84; was line 81 pre-Pass-1):** Author-ratified new Option D replacement: *"The oil, the market price, and the demand curve are all the same as Norway's. The outcomes for the communities whose commons the oil was drawn from are not."*
- **F-V3 (lines 118 + 120 + 122 + 124):** Pass 3.2 verify-refined Option B — break anaphora on lines 120 + 122; preserve "It does not…" openers on 118 + 124.
- **F-V6, F-V8, F-V9, F-V11, F-V12, F-V13, F-V14, F-V15 (8 MEDIUM):** Verify-pass-refined primary options proposed per Pass 3.2 verify §3.
- **F-V4, F-V5, F-V7, F-V10 (4 MEDIUM):** Verify-pass concur Pass 2 hold-as-is.
- **F-V16-V23 (8 LOW):** Verify-pass concur Pass 2 hold-as-is.
- **F-R-1 + F-R-2 (Pass 3.1 verify; line 26):** GPFG AUM refresh ("more than two trillion dollars") + per-citizen refresh (Option (a) "roughly three hundred and sixty thousand dollars" recommended; Option (b) range $356K-$391K available).

**Sibling-side outstanding (NOT Ch 4-side):**
- Cross-chapter consistency inventory line 95 + 96 anchor refresh (route to inventory revision session).
- Ch 6 line 537 anchor refresh ($1.8T → $2.0T) — route to Ch 6's next retrofit cycle if not addressed.
- Op-ed canonical-facts inventory refresh — PM disposition on whether op-ed is in active publication pipeline or historical-record.

**Phase C application session handles all Ch 4-side items.** Sign-off aggregate verdict (§9) is **conditional on Phase C application**.

---

## §3. Academic-rigor sign-off (Bookend #1)

Verifies the chapter's substantive claims against current canonical sources + framework consistency + apparatus discipline.

### §3.1 Per-claim verification status

**Named people:**
- Author (Chris Winn) — byline; consent default per author's authorial decision.
- Jens Stoltenberg (Stoltenberg I + Stoltenberg II) — Norwegian PM; named in official capacity. Public-record exception per `tools/memory/feedback_named_subject_consent.md`.
- Kjell Magne Bondevik (Bondevik II) — Norwegian PM; named in official capacity. Bondevik II disambiguation applied per Pass 3.1 MEDIUM-2.
- Erna Solberg — Norwegian PM; named in official capacity.
- Jonas Gahr Støre — Norwegian PM (current); named in official capacity.
- Ken Saro-Wiwa (deceased) — Nigerian writer/activist; named in historical-record context (1995 execution).

**Named places:** Norway, North Sea, Ekofisk (Block 2/4), Niger Delta, Bangladesh, Sahel, Pacific island states, Texas, Alberta, Alaska, Venezuela, Saudi Arabia, Germany (Bismarck) — all safe-to-name per place-name discipline.

**Named institutions:** Government Pension Fund Global (GPFG; established 1990 as Government Petroleum Fund; renamed 2006 per Pass 3.1 MEDIUM-1); Equinor (formerly Statoil; renamed 2018 per Pass 3.1 LOW-3); United Nations Environment Programme (UNEP); Commonwealth of Nations (Nigeria temporary-suspension reference 1995-1999); U.S. Social Security; Bismarck-era German 1889 Old Age and Disability Insurance (per Pass 3.1 MEDIUM-5).

**Statistics / numbers (canonical-source-verified status):**
- GPFG AUM "more than $1.9 trillion" (line 26) — **STALE per Stage 1c F-1c-1**; current TA canonical is $2.0T (end-2025). Phase C F-R-1 refresh.
- Per-citizen "roughly $340,000" (line 26) — **STALE per Stage 1c F-1c-1**; current TA canonical is $356K-$391K range at population 5.62M (Statistics Norway 2025). Phase C F-R-2 refresh.
- 70-80% state-capture share of net petroleum wealth (line 48) — within TA-verified canonical range.
- "expected real return... roughly three percent" fiscal rule (line 27) — verified per handlingsregelen 2017 revision.
- UNEP 2011 Ogoniland $1B + 25-30 years (line 82, post-Pass-1 rewrite) — verified per UNEP 2011 Environmental Assessment of Ogoniland §3.4 + §6.
- Ekofisk discovery December 1969 ("three days before Christmas") — verified per canonical-facts inventory; LOW-1 source-variation footnote acknowledges multiple-date-source ambiguity (Phillips Dec 22 / NPD Dec 23 / Equinor Dec 24).
- Alberta Heritage Trust Fund 1976 — verified.
- Alaska Permanent Fund 1976 (constitutional amendment) / operational 1977 — Pass 3.1 MEDIUM-4 cross-corpus lock at 1976 canonical (constitutional amendment date).
- Norway population 5.62M (current; per TA verification round 2026-05-14) — anchor for per-citizen calculation.

**Lineage / intellectual-history claims:**
- Hartwick rule operationalization framing — verified per bibliography §13 LOAD-BEARING Hartwick entry + §13 GPFG-as-Hartwick-operationalization designation.
- "Mazzucato-style value-capture" framing (Ring-1 flagship term) — verified per bibliography §13 STRONG SUPPORT.
- Pistor legal-architecture diagnosis — chapter does not directly cite; consistent with bibliography §13 Ch 5 home assignment.

**Verdict (academic-rigor):** **VERIFIED-CONDITIONAL on Phase C anchor refresh.** Once F-R-1 + F-R-2 apply, all per-claim verification is current against canonical sources. Until Phase C, chapter cites figures that are accurate-as-of-2026-04 but superseded by TA verification round 2026-05-14.

### §3.2 Framework consistency

- "Cost severance" lowercase prose usage — consistent with cross-chapter consistency inventory §1 Cost Severance row.
- "Accountability bond B" lowercase prose usage (Ch 5 apparatus-introduction home; Ch 4 uses for case-application illustration) — consistent with inventory §1 + apparatus register decisions 2026-05-11.
- "Residual commons value" lowercase prose usage — consistent.
- "Intergenerational Option Value" Title-case first-introduction (line 124, single canonical introduction site) — consistent with inventory §1 row 40 Ch 4 canonical-home assignment + Henry 1974 + Arrow-Fisher 1974 lineage.
- Apparatus exclusion (no formal-register apparatus terms in chapter prose beyond the lowercase-prose-phrases above + the single Title-case Intergenerational Option Value introduction): Pass 3.2 verify §4 + Stage 1a clean baseline + Pass 3.4 §4 apparatus sub-check all VERIFY-CLEAN.

**Verdict (framework consistency):** **VERIFIED.**

### §3.3 Academic-rigor sign-off verdict

**SIGN-OFF ✓ (CONDITIONAL on Phase C anchor refresh per F-R-1 + F-R-2).** Pre-Phase-C: chapter is academically defensible against canonical sources as of 2026-04; cites figures that the 2026-05-14 TA verification round has superseded. Post-Phase-C: chapter is academically current against all canonical sources.

---

## §4. Prose-quality sign-off (Bookend #2)

Verifies voice register + apparatus exclusion + scaffolding + Path B compliance + sentence-rhythm quality.

### §4.1 Voice register

Third-person-analytical throughout per Pass 3.2 baseline + verify pass. Tense consistency holds (past-tense for historical chronology; present-tense for current-state analytical claims; conditional for counterfactual scaffolding). No first-person breaks. No memoir-register intrusion. Trade-press analytical-comparative-policy prose register sound.

### §4.2 Apparatus exclusion

Verified clean per Pass 3.2 baseline §5 + Pass 3.4 §4 + Stage 1a (0 findings). One Title-case Intergenerational Option Value at line 124 is the canonical chapter-class introduction site per inventory.

### §4.3 Scaffolding compliance

Stage 1a CLEAN BASELINE — 0 HIGH / 0 MEDIUM / 0 LOW; ~80 patterns scanned. No `TODO` / `TK` / `INTERVIEW NEEDED` / `Option [A-Z]` / `Phase C-*` / `F-V[0-9]+` / include-glyph / exclude-glyph / meta-commentary scaffolding in chapter source.

### §4.4 Path B compliance

No verbatim-clone passages from other chapters detected. Norway op-ed at `publishing/op-eds/norway-sovereign-wealth/op-ed.md` is downstream of Ch 4 (derivative); not Path B contamination per Stage 1c §3-cross-references.

### §4.5 Sentence-rhythm quality

Pre-Phase-C: 3 HIGH (F-V1 + F-V2 + F-V3) + 12 MEDIUM (F-V4-V15) Pass 3.2 baseline findings flagged at specific lines. Walkthrough author ratifications + Pass 3.2 verify refined recommendations exist for all 15 findings. Post-Phase-C application: sentence-rhythm passes trade-press editorial standards.

### §4.6 Prose-quality sign-off verdict

**SIGN-OFF ✓ (CONDITIONAL on Phase C application of Pass 3.2 verify-refined spot-fixes).** Pre-Phase-C: chapter has flagged cadence patterns (declarative-three-in-a-row, four-anaphoric fragment block, four-paragraph "It does not…" anaphoric block, em-dash density, expository-frame patterns) that a trade-press editor would query. Post-Phase-C: all 3 HIGH cadence-flatness patterns dissolved + recommended MEDIUM refinements applied; chapter prose passes.

---

## §5. Cross-chapter coherence forward-flags

Per Stage 1c §3-cross-references + Pass 3.4 §5 cross-chapter sub-check:

- **Ch 4 ↔ Ch 5** (Restitution / Foreclosure Bonds apparatus): Pass 3.4 §5.4 confirms Ch 5 line 124 + 212+ cross-reference Ch 4 comparator correctly; $108T figure home is Ch 5 (clean division of labor with Ch 4's architectural-contingency framing).
- **Ch 4 ↔ Ch 6** (Three Methods + Four Gates + RCV apparatus): Pass 3.4 §5.1 confirms T2 orthodox-econ conceptual-precision routes to Ch 6 + TA Pass 3.4 (already RATIFIED). Ch 6 line 537 separately needs anchor refresh ($1.8T → $2.0T) — route to Ch 6's next retrofit cycle.
- **Ch 4 ↔ Ch 9** (policy economy + bond-instrument portability): Pass 3.4 §5.5 flags A5 Norway-exceptionalist + A1 industry-aligned + A6 postcolonial as adversarial characters that should pressure-test Ch 9's portability claims. Ch 9 Pass 3.4 already RATIFIED 2026-05-23 (CONDITIONALLY ROBUST); re-fire not warranted unless Ch 4 Phase C application surfaces structural change.
- **Cross-chapter rent-seeking workstream** (Public Choice cross-chapter handoff RATIFIED `bc02767`): Ch 4 T1 thread carries the Public Choice rent-seeking lens; substantive engagement at TA §1.10 + Ch 5 + Ch 8 + Ch 9 carries downstream load.

No new cross-chapter incoherence; cross-references are realized correctly.

---

## §6. Outstanding Phase C application items (carry-forward)

| Item | Location | Source | Disposition |
|---|---|---|---|
| F-R-1 GPFG AUM refresh | Ch 4 line 26 | Pass 3.1 verify | APPLY at Phase C: "more than $1.9 trillion" → "more than two trillion dollars" |
| F-R-2 per-citizen refresh | Ch 4 line 26 | Pass 3.1 verify | APPLY at Phase C: "roughly three hundred and forty thousand dollars" → "roughly three hundred and sixty thousand dollars" (Option (a) recommended; Option (b) range available) |
| F-V1 chronology cadence | Ch 4 line 32 | Pass 3.2 verify (walkthrough Option B locked) | APPLY at Phase C: replacement text per Pass 3.2 verify §2 |
| F-V2 fragment block | Ch 4 line ~84 | Pass 3.2 verify (walkthrough Option D locked) | APPLY at Phase C: replacement text per Pass 3.2 verify §2 |
| F-V3 four-paragraph anaphora | Ch 4 lines 118+120+122+124 | Pass 3.2 verify (refined Option B) | APPLY at Phase C: break anaphora on lines 120 + 122; preserve 118 + 124 openers |
| F-V6, V8, V9, V11, V12, V13, V14, V15 (8 MEDIUM) | Various | Pass 3.2 verify (refined primary options) | APPLY at Phase C per Pass 3.2 verify §3 recommendations |
| F-V4, V5, V7, V10 (4 MEDIUM) | Various | Pass 3.2 verify (concur hold) | HOLD per Pass 3.2 verify |
| F-V16-V23 (8 LOW) | Various | Pass 3.2 verify (concur hold) | HOLD per Pass 3.2 verify |

**Sibling-side (NOT Ch 4):**
- Cross-chapter consistency inventory line 95 + 96 anchor refresh — route to inventory revision session.
- Ch 6 line 537 anchor refresh — route to Ch 6's next retrofit cycle.
- Op-ed canonical-facts inventory refresh — PM disposition.

**Pass 3.5 developmental-edit DEFERRED** per explicit-gate cascade (not in this retrofit's scope; T4 flag from Pass 3.4 surfaces it as future-fire candidate — lines 32-36 scene-anchor restoration crediting NBIM/transparency/ethics-council/Storting-consensus operational architecture).

---

## §7. Pre-publication review queue companion artifact

Companion pre-pub queue at [`tools/pre-submission-reviews/ch4_pre_pub_queue_2026-05-25.md`](../../pre-submission-reviews/ch4_pre_pub_queue_2026-05-25.md). This sign-off ratifies the companion artifact. Key items in pre-pub queue:

- Recommended external reviewer types: Norwegian-petroleum-history reader; sovereign wealth fund academic / GPFG governance scholar (per handoff §1).
- Highest-priority sections for external review (budget-limited): Norway-as-existence-proof framing (lines 14-18 + 62-72); GPFG architecture description (lines 22-32; especially post-Phase-C anchor refresh); US Social Security comparator (lines 96-108).
- Pass 3.4 thread-pull synthesis items acknowledged for transparency: T1 Norway-as-existence-proof cross-pressure structure; T4 generalizability + replication-record gap; T6 SS comparator architectural-distinction; T7 framework apparatus conceptual-distinction.

---

## §8. Stage 4 render + character-integrity audit (RATIFIED 2026-05-25 — bundled per Ch 1/2/6 precedent)

### §8.1 Stage 4 disposition

**RATIFIED as AUTHOR-COMPLETED-OFFLINE 2026-05-25 per author direction.** Author render pipeline session executed offline; no agent involvement. Verdict: **CLEAN** (matches Ch 1 + Ch 2 + Ch 6 patterns). Bundled into this Stage 5 sign-off per Ch 1 (`fb25c9c` adjacent) + Ch 2 (`cd2c76d`) + Ch 6 (`533f4f6`) precedent — render-toolchain containerization (Docker / remote-container) drove Claude-token cost to ~0 per pipeline-doctrine reference, freeing Stage 4 execution to the author's offline workflow.

### §8.2 Audit-mode scan (PM-session pre-ratification baseline)

Prior to the author-offline render-pipeline ratification, the PM session performed an audit-mode scan against the registered character-integrity risk patterns as a pre-ratification baseline check. Findings consistent with the author-offline CLEAN verdict:

- **Em-dash density check:** Chapter has em-dashes flagged at Pass 3.2 F-V9 (78-word mega-parenthetical at line ~52) + F-V12 (4 em-dashes in US-SS comparator paragraph at ~98). Em-dashes are render-stable in EB Garamond + math-font fallback chain per existing render baseline; no tofu-box risk under current Docker render-toolchain (per pipeline-revision handoff §0 fix `d238f2c`).
- **Approximation-symbol check (≈):** Chapter does NOT contain `≈` symbol. No risk.
- **Greek-letter check:** Chapter does not use Cᵢ apparatus notation (apparatus is Ch 5 / Ch 6 home).
- **Currency-symbol check ($, NOK):** Chapter uses $ symbol multiple times (per-citizen, AUM, UNEP $1B); NOK appears in line 117 "rather than in krone" (prose word, not currency symbol). $ is render-stable.
- **Subscript / superscript check:** Chapter contains "8.9B Sm³ o.e." superscript-3 reference per F-1c-1 disposition (if Phase C applies F-R-1 with cumulative-production refresh) — superscript-3 (³) is render-stable per existing TA render baseline.
- **Typography (en-dash / hyphen-minus):** Random sampling shows correct em-dash usage (— not -- or --) throughout.
- **Cross-reference against `tools/quality-gates/regressed-patterns.yaml`:** All chapter-relevant patterns checked at Stage 1a; 0 findings.

**Audit-mode pre-ratification verdict:** RENDER-CLEAN against scanned-pattern set — consistent with author-offline CLEAN ratification.

### §8.3 Phase C re-fire trigger

Per change-cascade discipline: if Phase C application of F-R-1 + F-R-2 (GPFG anchor refresh) or Pass 2 spot-fixes introduces any new character-integrity risks (superscript-3 in F-R-1 cumulative-production refresh; em-dash density redistribution from Pass 2 spot-fixes), a light Stage 4 re-fire is warranted at the Phase C application session's close. The expected diff is small (anchor-refresh + sentence-rhythm spot-fixes) and the post-Phase-C render is the artifact that ships; author can re-run render-pipeline at the pre-publication gate to confirm.

**Stage 4 bundled ratification:** **RATIFIED 2026-05-25 — CLEAN — author-offline-completed.**

---

## §9. Aggregate Stage 5 verdict

**READY AFTER PHASE C APPLICATION.**

The chapter has passed all retrofit audit sub-steps (Stages 1a + 1c + Passes 3.1 verify + 3.2 verify + 3.3 + 3.4 + Stage 4 audit-mode) with verdicts ranging from CLEAN BASELINE (1a) to ROBUST (3.4) to INCLUDE — CHAPTER SHIPS (3.3). The retrofit work is complete.

**What's still needed before submission:** Phase C application session to:
1. Apply F-R-1 + F-R-2 (line 26 GPFG anchor refresh).
2. Apply F-V1 + F-V2 author-ratified Pass 2 spot-fixes (walkthrough Options B + D).
3. Apply F-V3 verify-refined Option B + the 8 MEDIUM Pass 3.2 verify-refined recommendations.
4. Hold F-V4 + F-V5 + F-V7 + F-V10 + all 8 LOW per Pass 3.2 verify concur.
5. Optionally fire Pass 3.5 developmental-edit (DEFERRED; T4 flag for scene-anchor restoration at lines 32-36).
6. Author-offline render-pipeline execution at pre-publication gate.

After Phase C: chapter is **READY-TO-SUBMIT** (matches Ch 1 + Ch 2 + Ch 6 + TA `2d01407` chapter-class READY-TO-SUBMIT precedent).

**Comparison to corpus precedents:**

| Artifact | Stage 5 verdict | Phase C status |
|---|---|---|
| TA (`2d01407`) | READY-TO-SUBMIT | Applied |
| Boston Review essay (`d34214d`) | READY-TO-SUBMIT | Applied |
| Noema essay (`8191004`) | READY-TO-SUBMIT | Applied |
| $100 Barrel essay (`0266525`) | READY-TO-SUBMIT | Applied |
| Ch 6 (`533f4f6`) | READY-TO-SUBMIT | Applied |
| Ch 2 (`cd2c76d`) | READY-TO-SUBMIT | Applied |
| Ch 1 (`fb25c9c` adjacent) | READY-TO-SUBMIT | Applied |
| **Ch 4 (this artifact)** | **READY AFTER PHASE C APPLICATION** | **PENDING** |

Ch 4 is the first chapter to reach Stage 5 with Phase C application still outstanding — the precedent prior chapters fired Stage 5 only after their Phase C applications had landed. Per pipeline doctrine v3.1 + Amendment C interactive ratification protocol, the combined Phase C ratification + application session is the natural next-step for Ch 4. PM session schedules.

---

## §10. Author ratification request

**Stage 4 bundled disposition (§8): RATIFIED 2026-05-25** as AUTHOR-COMPLETED-OFFLINE per author direction. CLEAN verdict.

Still pending:
1. **Stage 5 sign-off (this artifact):** PROPOSED → RATIFIED — confirms aggregate verdict + cross-references. Ratifies in same session as Phase C application per Amendment C interactive ratification protocol.
2. **Pre-publication review queue companion:** PROPOSED → RATIFIED at companion artifact. Ratifies in same session.

Phase C application session is the natural follow-on (combines ratification + application per pipeline doctrine §3.7 + v3.1 Amendment C interactive ratification protocol).

---

---

## §11. Ratification record + Phase C application log (closed 2026-05-25)

**Author ratification 2026-05-25:** All Phase C items ratified as recommended in a combined ratification + application session per pipeline doctrine v3.1 Amendment C interactive ratification protocol. The §9 aggregate verdict moves from "READY AFTER PHASE C APPLICATION" to **READY-TO-SUBMIT** — Ch 4 joins Ch 1 + Ch 2 + Ch 6 + TA in the chapter-class READY-TO-SUBMIT corpus.

### §11.1 Phase C edits applied to `Chapter__4_TheExistenceProof.md`

Single atomic chunk: 14 edits / 13 line changes (one line carries two collapsed edits — F-V14 + F-V15-line-108 are in the same paragraph).

| Finding | Line | Disposition | Applied |
|---|---|---|---|
| F-R-1 | 26 | GPFG AUM refresh: "one and nine-tenths trillion" → "two trillion" | ✓ |
| F-R-2 | 26 | Per-citizen refresh: "three hundred and forty thousand" → "three hundred and sixty thousand" (Option (a) recommended) | ✓ |
| F-V1 (HIGH) | 32 | Five-declarative chronology → Option B inventory-and-punch single sentence | ✓ |
| F-V2 (HIGH) | 84 | Four-fragment "The same X" block → Option D two-sentence comma-list (em-dash-free) | ✓ |
| F-V3 (HIGH) | 120 | Anaphora break: "It does not close the externality tail." → "The externality tail also remains open." | ✓ |
| F-V3 (HIGH) | 122 | Anaphora break: "It does not address the distributional problem at the global scale." → "The global-scale distributional problem is unresolved." | ✓ |
| F-V6 | 18 | Double-anaphoric pivot collapsed: "The variable is not geology. The variable is..." → "The variable is not geology — it is..." | ✓ |
| F-V8 | 42 | Soft-superlative hedge: "the best in the world" → "widely judged the best in the world" | ✓ |
| F-V9 | 52 | 78-word em-dash mega-parenthetical broken into two sentences (substantive claim + applications-list as separate sentence) | ✓ |
| F-V11 | 86 | Compress sentences 2+3: "It is large because B is small. It is not large because the oil is different." → "It is large because B is small, not because the oil is different." | ✓ |
| F-V12 (em-dash pair 1) | 98 | Em-dash pair (architectural-sources) → restructured to three sentences (drops both em-dashes; preserves substance) | ✓ |
| F-V12 (em-dash pair 2) | 98 | Em-dash pair (general-operations list) → parens | ✓ |
| F-V13 | 100 | Drop sentence 2: "Both are intergenerational instruments." removed; "Both are X" anaphora reduced from 3 to 2 | ✓ |
| F-V14 | 108 | Drop chiastic coda: "— and that what was constructed once can be reconstructed." removed | ✓ |
| F-V15 (line 88) | 88 | Drop expository frame: "This is what the framework needs to demonstrate to be credible: that it differentiates correctly." → "The framework needs to demonstrate that it differentiates correctly." | ✓ |
| F-V15 (line 108) | 108 | Drop expository frame: "What the comparison does add to the chapter's argument is this:" → "The comparison adds the following to the chapter's argument:" | ✓ |
| F-V15 (line 56) | 56 | HELD as deliberate §-conclusion cadence per Pass 3.2 verify recommendation | — |

### §11.2 Held findings (Pass 3.2 verify concur-hold)

| Finding | Line | Disposition |
|---|---|---|
| F-V4 | 12 | HELD — substantive survey-follow-through earns framing |
| F-V5 | 14 | HELD — sentence-length variance softens named pattern |
| F-V7 | 34 | HELD — three-element architecture-design substantively earned |
| F-V10 | 68 | HELD — selection-criterion claim earns cadence-build |
| F-V16-V23 (all 8 LOW) | 26 / 30 / 36 / 46 / 54 / 70 / 134 / 136 | HELD per Pass 3.2 verify concur-hold |

### §11.3 Stage 4 disposition

§8 RATIFIED 2026-05-25 as AUTHOR-COMPLETED-OFFLINE per author direction (separate `45323b1` commit; verdict CLEAN per Ch 1 + Ch 2 + Ch 6 corpus pattern). No re-fire warranted from this Phase C application chunk — the 13 line changes are anchor-refreshes + cadence-restructures within already-render-stable patterns (no new Greek letters, no new approximation symbols, no new currency-symbol patterns). Author-offline render-pipeline confirmation at pre-publication gate per Ch 1 precedent.

### §11.4 Stage 5 sign-off ratification

This sign-off artifact (§§0–§10) is RATIFIED 2026-05-25 in the same Phase C session per Amendment C interactive ratification protocol. The companion pre-pub queue artifact at [`tools/pre-submission-reviews/ch4_pre_pub_queue_2026-05-25.md`](../../pre-submission-reviews/ch4_pre_pub_queue_2026-05-25.md) is RATIFIED in tandem.

### §11.5 Aggregate verdict — UPDATED

§9 aggregate verdict **UPDATED FROM** "READY AFTER PHASE C APPLICATION" **TO** **READY-TO-SUBMIT**. Ch 4 joins corpus precedent:

| Artifact | Stage 5 verdict | Phase C status |
|---|---|---|
| TA (`2d01407`) | READY-TO-SUBMIT | Applied |
| Boston Review essay (`d34214d`) | READY-TO-SUBMIT | Applied |
| Noema essay (`8191004`) | READY-TO-SUBMIT | Applied |
| $100 Barrel essay (`0266525`) | READY-TO-SUBMIT | Applied |
| Ch 6 (`533f4f6`) | READY-TO-SUBMIT | Applied |
| Ch 2 (`cd2c76d`) | READY-TO-SUBMIT | Applied |
| Ch 1 (`fb25c9c` adj) | READY-TO-SUBMIT | Applied |
| Ch 9 (`0d67d62`) | READY-TO-SUBMIT | Applied |
| **Ch 4 (this artifact)** | **READY-TO-SUBMIT** | **Applied 2026-05-25** ✓ |

### §11.6 Outstanding items beyond this session

- **Sibling-side housekeeping** (NOT Ch 4-side; route via PM):
  - Cross-chapter consistency inventory line 95 + 96 anchor refresh (inventory revision session).
  - Ch 6 line 537 anchor refresh ($1.8T → $2.0T) — route to Ch 6's next retrofit cycle.
  - Op-ed canonical-facts inventory refresh — depends on op-ed active/archived status.
- **Optional Pass 3.5 developmental-edit** (DEFERRED per explicit-gate cascade; T4 thread flags lines 32-36 scene-anchor restoration crediting NBIM / transparency / ethics-council / Storting-consensus operational architecture). Author triggers separately via [developmental-edit workstream](../../workstream-handoffs/developmental-edit-workstream-handoff_2026-05-18.md) if warranted.
- **Pre-publication-gate render verification** at submission time.

---

---

## §12. Pass 3.5 developmental-edit application + Stage 4 re-ratification (closed 2026-05-26)

**Author ratification 2026-05-26:** Pass 3.5 developmental-edit (PROPOSED 2026-05-25 at `8920139`) ratified as recommended in a combined ratification + application session per Amendment C interactive ratification protocol.

### §12.1 Pass 3.5 application

Both HIGH findings applied via Option A as recommended:

| Finding | Line | Disposition | Applied |
|---|---|---|---|
| F-DE-Ch4-1 (HIGH; Option A) | 36 | ~50-word single-sentence scene-anchor restoration appended to §"The architecture" close: "The mechanisms that maintained it are specifiable: an operational arm — Norges Bank Investment Management — run at arms length from political direction, an ethics council whose divestment decisions are public, a fiscal rule coupled to quarterly reporting that makes any breach politically observable, and a Storting in which structural change to the fund requires a consensus supermajority no recent coalition has been able to assemble." Closes Pass 3.4 §6.2 T4 thread-pull flag. | ✓ |
| F-DE-Ch4-2 (HIGH; Option A) | 80 | ~75-word two-sentence international-architecture restoration inserted between corruption-prosecutions sentence and Niger-Delta-communities sentence: "The architecture that routed revenue outside Nigeria is itself part of the architecture the chapter is naming: international tax-treaty structures that legitimize commodity-trade transfer-pricing into low-disclosure jurisdictions, financial-secrecy intermediation in jurisdictions whose own home regulators have chosen not to impose extraterritorial liability on operating-company affiliates, and concession terms inherited from pre-independence arrangements made when the Nigerian state did not yet exist as a counterparty. The mechanism is not a Nigerian failure operating in isolation; it is an international architecture in which Nigerian institutional weakness is one component among others." Closes Pass 3.4 §6.2 T3 thread-pull flag. | ✓ |
| F-DE-Ch4-4 (LOW) | 52 | HELD per Pass 3.5 verify (Pass 3.4 §6.2 low-priority flag closed; enumeration appropriate to substantive-grounding register). | — |
| F-DE-Ch4-3, -5, -6 | — | NO FINDING logged — no restoration warranted. | — |
| C-DE-Ch4-1 through -7 | — | Whole-chapter confirmations — no restoration warranted. | — |

**Chapter state post-Pass-3.5:** ~143 lines / ~4,150 words (chapter grew by ~125 words / 2 lines from prior 141 lines / ~4,025 words at commit `97ba205`).

### §12.2 Cross-pass cascade confirmations

- **Pass 3.3 acceptance:** Pass 3.5 §3 cross-character impact analysis projected Tier 1 #3 (SWF-domain policy reader) verdict to STRENGTHEN from ✓✓ to ✓✓✓ + Tier 3 #14 (Mazzucato/Raworth cluster) to STRENGTHEN. **Light Pass 3.3 acceptance re-fire warranted** per Amendment B Pass-3.5 protocol; fires post-this-commit. No EXCLUDE shift projected at any character.
- **Pass 3.4 robustness:** Pass 3.4 §6.2 T3 + T4 thread-pull flags directly closed by F-DE-Ch4-1 + F-DE-Ch4-2. **Pass 3.4 re-fire NOT routinely warranted** per Amendment B Pass-3.5 protocol (restorations strengthen adversarial robustness; do not weaken). A3 + A5 + A6 adversarial reads partially defused.
- **Pass 3.1 fact-check + 3.2 voice-polish:** No re-litigation; all prior dispositions preserved.
- **Stage 1c coherence:** GPFG canonical anchors ($2.0T / $356K-$391K) unaffected; F-DE-Ch4-1 + F-DE-Ch4-2 add structural-feature content at the right register without touching anchor numerics.

### §12.3 Stage 4 re-ratification (post-Pass-3.5)

**RATIFIED 2026-05-26 as AUTHOR-COMPLETED-OFFLINE** per author 2026-05-26 direction. Author re-ran Docker render pipeline against the post-Pass-3.5 chapter state; verdict **CLEAN** (matches the prior Stage 4 ratification at `45323b1` against the post-Phase-C state).

Re-fire rationale per §8.3 Phase C re-fire trigger discipline: Pass 3.5 added one new em-dash pair (F-DE-Ch4-1 NBIM institutional-naming convention) within already-render-stable typography. F-DE-Ch4-2 added no new em-dashes. No new Greek letters, approximation symbols, or currency-symbol patterns. Author offline confirmation closes the re-fire flag.

### §12.4 Aggregate verdict — RE-CONFIRMED

**READY-TO-SUBMIT** (aggregate verdict unchanged from §11.5; Pass 3.5 application is optional-but-recommended polish that strengthens the chapter — does not change ship-readiness). Ch 4 remains in the chapter-class READY-TO-SUBMIT corpus alongside Ch 1 + Ch 2 + Ch 6 + Ch 9 + TA.

### §12.5 Outstanding items beyond this session

- **Light Pass 3.3 acceptance re-fire** — ✅ COMPLETE 2026-05-26. PROPOSED artifact at [`tools/rigor-passes/ch4_existence_proof_stage3_pass_3_3_light_refire_post_pass_3_5_2026-05-26.md`](../../rigor-passes/ch4_existence_proof_stage3_pass_3_3_light_refire_post_pass_3_5_2026-05-26.md). Aggregate verdict: **LIGHT-RE-FIRE CONFIRMS PRIOR + STRENGTHENS** — 25/25 INCLUDE preserved + 2 verdict-level uplifts (#14 Mazzucato/Raworth ✓✓→✓✓✓; #18 Niger Delta reader ✓→✓✓) + 12 confidence-level uplifts + 11 no-change + 0 DISCOUNT. 12 of 12 Pass 3.5 §3 projected STRENGTHEN candidates confirmed. NO SHIP BLOCK at any Tier 1 gating character. Verdict-tier distribution: ✓✓✓ 5→6, ✓✓ 15→15, ✓ 5→4. Awaiting author ratification (mobile-doable; one ratification call closes Ch 4 fully).
- **Pre-publication-gate render verification** — RE-CONFIRMED CLEAN per §12.3.
- **Cross-chapter cascade follow-up** — F-DE-Ch4-1 NBIM mechanism-credit pattern + F-DE-Ch4-2 international-architecture extension flagged for future cross-chapter developmental-coherence session.
- **Sibling-side housekeeping** (unchanged from §11.6) — cross-chapter consistency inventory + Ch 6 line 537 + op-ed canonical-facts inventory refresh.

---

*End of Stage 5 sign-off — Ch 4 The Existence Proof — **RATIFIED 2026-05-25 with Phase C application complete; Pass 3.5 RATIFIED + APPLIED 2026-05-26; Stage 4 RE-RATIFIED 2026-05-26 (post-Pass-3.5 author-offline Docker render CLEAN)**. Chapter is **READY-TO-SUBMIT**.*
