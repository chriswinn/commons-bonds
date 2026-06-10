# Manuscript Stage-3 Rigor Pass — Workstream Handoff (2026-05-11)

**Date drafted:** 2026-05-11
**Branch prefix:** `claude/manuscript-stage-3-` (per phase: `claude/manuscript-stage-3-ch<N>-<harness-id>` for Phase A; `claude/manuscript-stage-3-whole-book-<harness-id>` for Phase B; `claude/manuscript-stage-3-spot-fix-ch<N>-<harness-id>` for Phase C)
**Status going in:** Not blocked. **Recommended pacing: spread 10-chapter Phase A across 2–3 weeks**, sequenced after Aeon Jun 1 submission, before late-June book-proposal sprint.

---

## Why this workstream exists

The recent verification workstreams (#8 Path B cross-chapter, #9 apparatus register, #10 cross-chapter consistency, #15 Tech Appendix numbering, #13 flagship-terms defense sweeps narrow+widened) cleaned up specific cross-cutting issues. None applied v2.0 Stage 3 three-pass rigor (fact-check + voice-polish + audience-load) systematically to **each chapter** or to the **manuscript as a whole**.

Empirical evidence the discipline catches things:
- Op-ed pipeline (commit `5167edd`) ran its own Stage 3 fact-check pass and caught two real factual drifts (GPFG founding-date conflation + Bondevik-coalition timing) that audience-load alone wouldn't have flagged.
- Noema Essay B Stage 3 (commit `a9b627c`) caught 5+ factual drift points + voice-polish issues that the audience-load pass alone hadn't surfaced.

The book is approaching submission-readiness. Per the cascade plan, Wave 1 agent queries fire late July / early August 2026 with the green-light rule requiring complete proposal + ≥1 essay at editor-review + ≥1 named-source interview recorded. Agents will request sample chapters; trade publishers will request the full manuscript. **Polished manuscript at request time = stronger placement signal than polished-after-request.**

---

## Workstream scope — phased

### Phase A — Per-chapter Stage-3 audits (10 parallel-safe sessions)

Each chapter gets a dedicated session running the three-pass audit:
1. **Fact-check pass** — every named person / date / number / quote / case-detail verified against canonical sources (bibliography §13, primary-source briefs, public-record briefs, recent ratification commits, prior pipeline artifacts).
2. **Voice-polish pass** — LLM tics + expository flatness + meta-commentary + rule-of-three + em-dash crutches + declarative-three-in-a-row + cadence repetition + apparatus residue.
3. **Audience-load pass** — apply the 20-character book-audience pressure-test set to the chapter; surface where each chapter loses each reader.

**Per-session deliverable:** rigor-pass artifact at `tools/rigor-passes/commons_bonds_rigor_pass_<DATE>_ch<N>_<chapter-slug>_stage3_three_pass_v1.0.0.md` with three labeled sections.

**Parallel-safety:** all 10 sessions write to different rigor-pass artifact files; no merge conflicts. Each session READS its chapter file but does NOT edit it (spot-fixes are Phase C, separate per-chapter sessions).

**Recommended pacing:** spread across 2–3 weeks. Suggested cadence — ~3–4 chapter sessions per week. User paces to spread token usage.

### Phase B — Whole-book Stage-3 audit (1–2 sessions)

Catches what per-chapter passes miss. Sessions fire AFTER all 10 Phase A audits land on main.

Audit dimensions:
- **Narrative arc** — does the framework build correctly Ch 1 → Ch 10? Sunrise-Ch 1 + sunset-Ch 10 bookend land?
- **Reader-load arc** — cumulative cognitive load progression; where does the reader get exhausted?
- **Cross-chapter prose-rhythm** — voice consistency under sustained reading (different from #10's sampling pass).
- **Apparatus-buildup sequence** — does each framework term land in plain language before formal apparatus appears? Cross-reference workstream #9's apparatus register decisions.
- **Comp-titles audience-load** — does the book hold the cumulative comp-cluster reader (Mazzucato + Pistor + Christophers + Darity-Mullen)?

**Deliverable:** rigor-pass artifact at `tools/rigor-passes/commons_bonds_rigor_pass_<DATE>_whole_book_stage3_audit_v1.0.0.md`.

### Phase C — Spot-fix application (per-chapter sessions)

Apply ratified findings per chapter. Author ratifies which fixes apply; sessions execute. Likely 1 session per chapter (parallel-safe for chapter edits; do NOT bundle multi-chapter spot-fixes in a single session).

**Per-session deliverable:** per-chapter edits committed to main per WP#9 (merge per ratified chunk).

---

## Per-chapter audit table

> **STALENESS NOTICE 2026-05-21:** This handoff was originally drafted 2026-05-11 and is now significantly outdated in three dimensions: (a) all 10 chapter filenames dropped `__Draft` suffix in commits `a09e319` (Ch 1, 4-10; 2026-05-18) + `7110865` (Ch 3; consent workstream closed) + `4d860e8` (Ch 2; 2026-05-21); (b) Stage 3 evolved from 3-pass to **5-pass** per Amendment B 2026-05-18 (commits `5812e5c` + `0be3a86`) — `Pass 1 fact-check + Pass 2 voice-polish + Pass 3 audience-load + Pass 3.2 voice-polish-re-fire + Pass 3.5 developmental-edit`; (c) most chapters have substantially advanced through Phase A + Phase C beyond the 2026-05-11 baseline. The per-chapter table below is **verified-updated 2026-05-21** to reflect actual current state. The §"Phase A — Per-chapter Stage-3 audits" scope description above retains its 3-pass framing for historical record but should be read with Amendment B 5-pass in mind for new sessions.

For Phase A sessions, use the table below to assemble each chapter's paste-text from the master template (§Master Phase A paste-text below). Before firing any new chapter session, **always verify current state against `git log`** rather than relying on this table alone — chapter workstream advances faster than this doc updates.

| Ch | Current file path | Lines / target words | Key named subjects | Key named cases | Verified Phase A status (2026-05-21) |
|---|---|---|---|---|---|
| 1 | `manuscript/chapters/Chapter__1_TheQuietMath.md` | 122 / ~3,400w (actual ~4,118w per substance-drives-length) | Author's son (anonymized); father (anonymized); sister + nephew (anonymized); grandfather LaVern E. Winn (deceased; named in AuthorsNote; intimate "Pooh"/"Pou" in Ch 1) | NICU scene; air-compressor scene; 120-hour workweek; DMV math; McDowell counter-objection | **DONE-DONE.** Pass 1 ✓ (`commons_bonds_rigor_pass_2026-05-11_ch1_the_quiet_math_stage3_fact_check_v1.0.0.md`; F-1+F-2+F-3 applied) + Pass 2 RATIFIED+APPLIED `7b4aa92` 2026-05-15 + Pass 3 multiple runs (PROPOSED `0ed8a68` + REAUDIT v3 40-char adversarial `76ca8a6` + Light Re-fire RATIFIED `eb14171` 2026-05-19) + Pass 3.5 developmental-edit RATIFIED+APPLIED `e69c61e` (9 spot-fixes) + §11.5 DMV-commute coda author-revisit `d36534f` 2026-05-19. `__Draft` dropped chapter-wide `a09e319` 2026-05-18. |
| 2 | `manuscript/chapters/Chapter__2_TheMiner.md` | 226 / ~5,000w (actual ~5,367w) | Robert Bailey (deceased, McDowell County, journalism-subject); Ted Latusek (journalism-subject); Mazzucato; Harvey; Keefe; Sacklers; JFK (deceased + public-record speech); Jessica Lilly + Chris Hamby (journalists) | McDowell County coal; black lung; SMCRA bonds; Black Lung Trust Fund; Purdue/Sackler second cycle; Chesapeake pivot (close) | **DONE-DONE.** Pass 1 ✓ + Pass 2 ✓ + Pass 3 ✓ + Phase C-α/β/γ/δ all applied (17 cumulative spot-fixes; latest `46080d8` 2026-05-21 named-voice substitutions). `__Draft` dropped `4d860e8` 2026-05-21. Outstanding non-blocking: MT-1 line 189 phrasing (LOW; held); courtesy-notify pipeline pre-publication (Bailey + Day + Fox families); endnote sweep. |
| 3 | `manuscript/chapters/Chapter__3_TheWaterman.md` | 244 / ~?w | Biggie (deceased, named, courtesy-notify pre-staged `164b9e2`); Phat (anonymized per `8a55395`); Fox Hill community; Allison Colden (CBF MD); Karen Moore (CBF VA); other named voices per `9a7cc7e` augmentation Stage 2 (11 voices across 9 chapter locations) | Chesapeake fisheries; Fox Hill mutual aid; oyster trajectory; VMRC | **Phase A advanced.** Phat anonymization applied `8a55395`; GuidanceDoc revised `e4d5daf`; Pass 1 retroactively filed `98bb299` then reverted `cfed2b1` (status: clarify); Pass 3.2 voice-polish RATIFIED+APPLIED `589ca05`; augmentation workstream Stage 1 brief RATIFIED `b8806fa` + Stage 2 11-voices `9a7cc7e`; bibliography G1–G10 scribe pass `134b888`; bay-cap chronology disambiguation `6785646`. `__Draft` dropped `7110865` 2026-05-21 ("consent workstream closed"). Outstanding: verify Pass 1 status post-revert; Pass 3 audience-load status; Biggie family courtesy-notify pre-publication. |
| 4 | `manuscript/chapters/Chapter__4_TheExistenceProof.md` | 141 / ~3,975w | Norway leadership (verify named figures); Petroleum Fund founders | Norway GPFG; Ekofisk 1969; petroleum-state counterfactuals | Pass 1 fact-check `commons_bonds_rigor_pass_2026-05-12_ch4_existence_proof_stage3_fact_check_v1.0.0.md` + Pass 2 voice-polish `commons_bonds_rigor_pass_2026-05-15_ch4_existence_proof_stage3_voice_polish_v1.0.0.md`. `__Draft` dropped `a09e319` 2026-05-18. **Verify Pass 3 status.** |
| 5 | `manuscript/chapters/Chapter__5_TheAccountabilityGap.md` | 257 / ~9,574w | Pistor; Christophers; Coates; Darity & Mullen; Hamilton; Conley; Sandel; Parfit; Pettit; Skinner; Buchanan; Tullock; MacLean (implicit via D-3a acknowledgment) | Libby asbestos; Deepwater Horizon; restitution + foreclosure bond lineages; "Architecture and rent-seeking" Public Choice complementarity section | Pass 1 + Pass 2 + Pass 3 all PROPOSED 2026-05-13/14 (different filename convention: `commons_bonds_ch5_stage_3_pass_*_PROPOSED.md`); **stuck at PROPOSED for ~week — author ratification needed**. `__Draft` dropped `a09e319` 2026-05-18. **2026-05-25 Stage 1c D-3 Phase C application:** Ch 5 line 202 closing paragraph of "Architecture and rent-seeking" section received D-3a MacLean acknowledgment (`8aa7dfb`) + D-3b substantive paragraph-level realignment to asymmetric framing matching Reading C v3 + Ch 8:122 Option A canonical (this commit). Ch 5 + Ch 8 + Ch 9 + TA §1.10 Public-Choice-engagement sites now uniformly asymmetric ✓ COHERENT. Pass 3.3 light re-fire ✓ ACCEPTANCE-TEST DEFENSIBLE (no shifts; verdicts trend strengthened for natural-fit + reparations-tradition + EJ-movement + libertarian-PC cross-pressure reduction). Original Pass 1/2/3 PROPOSED ratifications remain outstanding pending separate Ch 5 author-ratification session. |
| 6 | `manuscript/chapters/Chapter__6_ThreeWaysofCounting.md` | 343 / ~75KB-HTML-equivalent (converted MD per #18) | Hotelling; Ostrom; Mazzucato; Hartwick | CIT; ARR; Hotelling Identity; RCV three-component decomposition | Pass 2 + Pass 3 PROPOSED 2026-05-14; **IPG methodology reconciliation RATIFIED+APPLIED `dd825f2`** + IPG Pass 3.2 voice-polish RATIFIED+APPLIED `2d5d608`; **Pass 3.5 developmental-edit PROPOSED `838a3f2`**. `__Draft` dropped `a09e319` 2026-05-18. Outstanding: PROPOSED Pass 2 + Pass 3 + Pass 3.5 ratifications; cross-corpus IPG canonical-construction (`f3def8a`). |
| 7 | `manuscript/chapters/Chapter__7_OnOtherWorlds.md` | 250 / ~8,537w | Mars / thought-experiment characters; Devon Island; HI-SEAS | Mars colony; six cost-hiding patterns; Abundance Masking | **Pass 1 RATIFIED+CLOSED `4948dbb` 2026-05-20** (post-§4.1 cascade scan `3e54015`); Pass 2 voice-polish PROPOSED `6f54514`; Phase C-α 7 spot-fixes applied `4987e59`. Aeon-source-protection still relevant. `__Draft` dropped `a09e319` 2026-05-18. Outstanding: Pass 2 ratification; Pass 3 status. |
| 8 | `manuscript/chapters/Chapter__8_WhatThingsActuallyCost.md` | 243 / ~6,026w | (verify named subjects post-Dunbar/Du-Bois engagement 2026-05-08) | McDowell coal per-ton arithmetic; Cᵢ component examples; black-lung trust fund Ch 2↔Ch 6↔Ch 8 lineage | Pass 1 + Phase C **16 ratified Ch 8 edits + 1 Ch 2 + 1 Ch 6** + 5 inventory rows `5fe6af6`; **MED-3 + MED-6 cascade reconciliation RATIFIED `5e260a3`** + Phase C residuals PROPOSED `ec81197`; rent-seeking Stage 1c coherence check PROPOSED `7f7eef9` (STRUCTURAL DRIFT flag); cross-corpus IPG canonical-construction decision artifact `f3def8a`. `__Draft` dropped `a09e319` 2026-05-18. Outstanding: rent-seeking Stage 1c resolution; Pass 2/Pass 3 status. |
| 9 | `manuscript/chapters/Chapter__9_PricingHonestly.md` | 294 / ~10,178w | Susskind; Christophers; Pistor; Buchanan; Tullock; MacLean (implicit via Char 15 Option A acknowledgment) | Pricing mechanics; four-step framework; Reading C v3 Public Choice asymmetric framing | **DONE-DONE.** **Pass 1 RATIFIED + Phase C `4c8bc02`** (12 prose + 2 cross-corpus) → **Pass 2 RATIFIED + Phase C `78a26c2`** (13 prose + Reading C v3 substantive rewrite) → **Stage 1c Ch 8 cascade RATIFIED + Phase C `cbef9bd`** (Option A applied) → **Pass 3.3 acceptance RATIFIED `a6b7df5`** (READY TO SUBMIT AS-IS; 18 INCLUDE / 0 EXCLUDE) → **Pass 3.4 robustness RATIFIED `4a28275`** (CONDITIONALLY ROBUST; PROPOSED `f47dd1c`; T3 Char 15 Option A Phase C `8aa7dfb`) → **Stage 1c D-3 sibling-coherence-check FULLY CLOSED `06eb1ea`** (D-3a MacLean consolidation `8aa7dfb` + D-3b symmetric-vs-asymmetric framing realignment of Ch 5 + TA Option A applied + Pass 3.3 light re-fire ✓ ACCEPTANCE-TEST DEFENSIBLE; cross-chapter sibling-coherence ✓ COHERENT across Ch 5 + Ch 8 + Ch 9 + TA §1.10) → **Pass 3.5 developmental-edit RATIFIED + APPLIED `1fe06c2`** (PROPOSED `1fd32dd`; STRONG verdict; F-DE-Ch9-1 Option A em-dash interjection applied at line 202 medical-crowdfunding paragraph for representative-class human contour; F-DE-Ch9-2 held-as-is per default) → **Stage 4 (render + character-integrity audit) RATIFIED `bc9f52d` (author-managed-offline disposition)** per Ch 2 + Ch 6 + Ch 1 + TA precedent → **Stage 5 bookend pre-publication sign-off RATIFIED 2026-05-25 PASS** (this commit; academic-rigor PASS + prose-quality PASS + pre-pub review queue GENERATED + RATIFIED). `__Draft` dropped `a09e319` 2026-05-18. **All five Stage-3 passes + Stage 1c (Ch 8 cascade + D-3) + Stage 4 + Stage 5 RATIFIED + APPLIED + CLOSED.** **Ch 9 is the FIFTH chapter-artifact to reach Stage 5** (after TA `2d01407` 2026-05-20 + Ch 6 `533f4f6` 2026-05-25 + Ch 1 `906a204` 2026-05-25 + Ch 2 `cd2c76d` 2026-05-25). **PUBLISHER-SHIP-READY.** Pre-pub review queue at [`tools/pre-submission-reviews/ch9_pre_pub_review_queue_v1.0.0.md`](../../pre-submission-reviews/ch9_pre_pub_review_queue_v1.0.0.md) carries 11 external-verification items + 9 recommended external reviewer types + rank-ordered priority sections. T7 → Ch 10 Pass 3.4 forward-flag preserved. |
| 10 | `manuscript/chapters/Chapter_10_CommonBonds.md` (note SINGLE underscore before 10) | 152 / ~7,366w | (verify named subjects) | Sunset bookend with Ch 1 sunrise; framework synthesis | Pass 1 artifact v1.0.1 `e026d5f` (re-anchored against current state). `__Draft` dropped `a09e319` 2026-05-18. Outstanding: Pass 2 + Pass 3 + Pass 3.5 dev-edit. |

**Plus paratext (optional Phase A extensions):**

| Artifact | File path | Audit emphasis |
|---|---|---|
| AuthorsNote | `manuscript/chapters/_AUTHORSNOTE_ON_WINDTUNNELS_AND_AI.md` | NASA-grandfather-LaVern-E.-Winn naming; AI disclosure register; book-positioning |
| Tech Appendix | `core/technical-appendix/TechnicalAppendix_v2.0.0.html` | Numbering scheme post-#15 reconciliation; formal apparatus integrity; cross-references from chapters per Phase 4 |
| Glossary | (verify path) | v4 rebuild status (queued); coordinate with #9 apparatus register decisions |

---

## Master Phase A paste-text (per-chapter)

Use this for each Phase A chapter session. Fill in `[BRACKETS]` from the per-chapter table above.

```
You are running Phase A of the Manuscript Stage-3 Rigor Pass workstream
(PM dashboard #20) for Chapter [N] — [CHAPTER NAME]. Your job: apply
v2.0 three-pass rigor (fact-check + voice-polish + audience-load) to
the chapter file at [FILE PATH]. STOP at verdict + spot-fix
recommendations; do NOT apply spot-fixes to the chapter file. Phase C
sessions apply ratified spot-fixes per author.

== v2.0 Amendment B discipline ==

Three DISTINCT passes, not bundled. Each pass catches what the others
miss. Each pass produces its own list of findings; the audience-load
pass produces a final include-vs-exclude verdict against the 20-character
book-audience pressure-test set.

== Read in order before doing any work ==

1. THIS paste (the framing).
2. tools/workstream-handoffs/archive/manuscript-stage-3-rigor-pass-handoff_2026-05-11.md
   (the workstream handoff — overall scope + per-chapter table + Phase A
   methodology).
3. tools/drafting-templates/stage-3-three-pass-rigor-audit.md
   (the Stage 3 template + audit-existing-prose mode notes).
4. tools/drafting-templates/audience-pressure-test-construction.md
   (20-character book-audience pressure-test set construction).
5. /Users/c17n/.claude/projects/-Users-c17n-commons-bonds/memory/feedback_audience_aware_drafting_discipline.md
   (v2.0 discipline; ratified 2026-05-10).
6. /Users/c17n/.claude/projects/-Users-c17n-commons-bonds/memory/feedback_voice_polish_pipeline.md
   (dump → sift → polish).
7. /Users/c17n/.claude/projects/-Users-c17n-commons-bonds/memory/feedback_substance_drives_length.md
   (no padding; no cutting to fit).
8. /Users/c17n/.claude/projects/-Users-c17n-commons-bonds/memory/feedback_named_subject_consent.md
   (named-subject discipline).
9. /Users/c17n/.claude/projects/-Users-c17n-commons-bonds/memory/feedback_verify_stale_memory_claims.md
   (verification discipline).
10. [FILE PATH] — the chapter under audit. Read in full.
11. Canonical sources to verify against (fact-check pass):
   - research/literature/bibliography.md §13 (comp + framework-adjacent
     entries with engagement-state flags)
   - research/outreach/subjects/<subject>/background-brief_*.md (per
     named subject in the chapter — Darity / Colden / Moore / Dagan
     / Mazzucato as applicable)
   - tools/rigor-passes/commons_bonds_rigor_pass_2026-05-11_apparatus_register_decision_v1.0.0.md
     (apparatus register canonical decisions)
   - tools/audits/cross-chapter-consistency-inventory_2026-05-11.md
     (canonical-terms inventory + named-cases + recurring-stats)
   - research/audits/cross-chapter-path-b-audit_2026-05-11.md (cross-
     chapter Path B baseline)
   - Recent ratification commits relevant to this chapter (see per-chapter
     table in the workstream handoff §"Specific audit emphases")

== Per-chapter context ==

**Chapter:** [N] — [CHAPTER NAME]
**File path:** [FILE PATH]
**Word count target:** [WORD COUNT TARGET]
**Key named subjects:** [LIST]
**Key named cases:** [LIST]
**Specific audit emphases:** [PER-CHAPTER TABLE ROW — "Specific audit emphases" column]

== Mission ==

Three passes against the chapter. Each pass produces its own findings
list. Output one rigor-pass artifact with three labeled sections.

== Pass 1: Fact-check ==

For every factual claim in the chapter, verify against canonical sources
(see Read order item 11). Flag findings by severity:

- **CRITICAL** — claim is factually wrong; would be caught by a
  fact-checker; publisher pre-publication review would flag.
- **HIGH** — claim is misleading or imprecise; could be challenged
  by a knowledgeable reader.
- **MEDIUM** — claim is technically defensible but loose; acceptable
  in trade prose but worth tightening.
- **LOW** — claim is accurate but framing could be sharpened.

For each finding: cite chapter line number + chapter text + canonical
truth + recommended spot-fix.

Pay special attention to (per the chapter's specific audit emphases):
[LIST CHAPTER-SPECIFIC FACT-CHECK FOCUS — e.g., for Ch 4: "GPFG
founding date 1990 as Government Petroleum Fund, renamed 2006 — the
op-ed session caught this drift; verify Ch 4 doesn't carry same error;
Bondevik coalition timing"]

== Pass 2: Voice-polish ==

For every paragraph, check for the LLM tics + voice issues. Reference
tools/drafting-templates/stage-3-three-pass-rigor-audit.md §"Pass 2"
for the full LLM-tic inventory.

For each issue: cite chapter line number + chapter text + recommended
revision. Severity HIGH / MEDIUM / LOW.

Pay special attention to chapter-specific register concerns (per
per-chapter table). For memoir-register chapters (Ch 1, Ch 3, Ch 10):
sentence-length variance discipline; first-person consistency. For
analytical chapters (Ch 5, Ch 6, Ch 9): apparatus-register coherence
(apparatus is permitted but per #9 register decisions); jargon-tripwire
checking.

== Pass 3: Audience-load ==

Apply the 20-character book-audience pressure-test set (per
tools/drafting-templates/audience-pressure-test-construction.md). For
each character: include-vs-exclude scoring on the standard scale
(✓✓✓ INCLUDE through ⚠⚠⚠ EXCLUDE).

Per-tier aggregate:
- Tier 1 (gating): if any character is ⚠⚠⚠, the chapter cannot ship
  to publisher / agent without fix.
- Tier 2 + Tier 3: tally include-vs-exclude weight.

For each character returning EXCLUDE, propose specific spot-fixes
that would flip their verdict to INCLUDE without alienating other
characters.

Pay special attention to chapter-specific audience concerns (per
per-chapter table). For chapters with cultural-resonance cases (e.g.,
Ch 3 Fox Hill, Ch 8 Dunbar/Du Bois lineage): Tier 3 cultural-resonance
characters get extra weight. For chapters with policy content (Ch 4
Norway, Ch 9 Pricing Honestly): Tier 1 policy / agent characters get
extra weight.

== Verdict synthesis ==

Three verdicts (one per pass) + aggregate:

- **Fact-check verdict** — total findings by severity; CRITICAL
  findings must be resolved before submission.
- **Voice-polish verdict** — total findings by severity; HIGH findings
  should be resolved.
- **Audience-load verdict** — total INCLUDE/EXCLUDE tally + final
  include-vs-exclude direction.

Aggregate:
- **READY AS-IS** — 0 CRITICAL fact-check; 0 HIGH voice-polish; net
  INCLUDE on audience-load with no Tier-1 EXCLUDE.
- **READY AFTER SPOT-FIXES** — specific spot-fixes itemized.
- **STRUCTURAL REVISION NEEDED** — findings cannot be addressed by
  spot-fixes; flag scope-expansion to PM session.

== Output ==

Single atomic commit:
- tools/rigor-passes/commons_bonds_rigor_pass_[DATE]_ch[N]_[chapter-slug]_stage3_three_pass_v1.0.0.md

== Hard constraints ==

- Do NOT apply spot-fixes to the chapter file. Phase C sessions do that.
- Do NOT re-write sections. Three passes audit; remediation is separate.
- Do NOT propose meta-conclusions about the v2.0 discipline.
- Do NOT contact named subjects.
- DO flag ANY apparatus regressions (terms ratified to drop appearing
  in trade body prose), named-subject consent issues (unsigned-consent
  living subjects named), or Path B contamination (verbatim from another
  chapter — should be 0 post-#8 fixes).

== Branch discipline ==

Open fresh feature branch claude/manuscript-stage-3-ch[N]-<harness-id>
from current origin/main per tools/workstream-handoffs/README.md.

After commit lands on main: STOP. Report rigor-pass back to PM session +
author. Author ratifies which spot-fixes to apply; Phase C session
applies them.

== Verify-stale-memory-claims discipline ==

Before asserting any time-sensitive claim:
- Verify chapter file path exists; check current line count.
- Verify named-subject consent status against
  research/outreach/subjects/<subject>/ files (canonical).
- Verify lineage / intellectual-history claims against
  research/literature/bibliography.md §13.
- Verify apparatus register decisions against
  tools/rigor-passes/commons_bonds_rigor_pass_2026-05-11_apparatus_register_decision_v1.0.0.md.
- If any cited file does not exist where claimed, stop and ask before
  guessing.
```

---

## Master Phase B paste-text (whole-book)

Use after all 10 Phase A audits land on main.

```
You are running Phase B of the Manuscript Stage-3 Rigor Pass workstream
(PM dashboard #20). Your job: whole-book audit catching what
per-chapter passes miss. STOP at verdict + recommendations; do NOT
apply edits.

== Read in order before doing any work ==

1. THIS paste (the framing).
2. tools/workstream-handoffs/archive/manuscript-stage-3-rigor-pass-handoff_2026-05-11.md
   (workstream handoff — Phase B scope).
3. All 10 Phase A rigor-pass artifacts at
   tools/rigor-passes/commons_bonds_rigor_pass_*_ch*_stage3_three_pass_v1.0.0.md
   (per-chapter findings; Phase B treats these as input).
4. All 10 chapter files at manuscript/chapters/Chapter*Draft*
   (read in chapter order Ch 1 → Ch 10 to test reader-load arc).
5. AuthorsNote at manuscript/chapters/_AUTHORSNOTE_ON_WINDTUNNELS_AND_AI.md.
6. /Users/c17n/.claude/projects/-Users-c17n-commons-bonds/memory/feedback_audience_aware_drafting_discipline.md
7. tools/audits/cross-chapter-consistency-inventory_2026-05-11.md
   (canonical-terms / cases / stats inventory).
8. tools/rigor-passes/commons_bonds_rigor_pass_2026-05-11_apparatus_register_decision_v1.0.0.md
   (apparatus register decisions).
9. alignment/commons_bonds_framework_positioning_disciplines_v1.0.0.md
   (FPD locked positioning).

== Mission ==

Audit dimensions:

(a) **Narrative arc.** Does the framework build correctly Ch 1 → Ch 10?
Sunrise-Ch 1 + sunset-Ch 10 bookend land? Where does the arc accelerate /
flatten / stall?

(b) **Reader-load arc.** Cumulative cognitive load progression. Where
does the reader get exhausted? Where is the load too light (filler
risk)?

(c) **Cross-chapter prose-rhythm.** Voice consistency under sustained
reading. Different from #10 cross-chapter consistency's sampling pass
(#10 sampled; this reads continuously). Flag voice shifts that read as
unintended.

(d) **Apparatus-buildup sequence.** Does each framework term land in
plain language before formal apparatus appears? Cross-reference
workstream #9 apparatus register decisions. Specifically: does the
reader encounter "cost severance" in plain prose (Ch 2 Cost Severance
defense paragraph) before encountering the CS = RCV − B equation in
Ch 6? Same test for RCV, bonds, CIT, ARR, Externality Tail, Abundance
Masking.

(e) **Comp-titles audience-load.** Does the book hold the cumulative
comp-cluster reader (Mazzucato + Pistor + Christophers + Darity-Mullen
+ Susskind + Sandel)? Where would each comp-cluster reader engage /
disengage across the full arc?

(f) **Sample-chapter selection.** For agent / publisher sample-chapter
requests, which 2-3 chapters best represent the book? Defaults per
cascade plan: Ch 7 (Mars / thought-experiment) + Ch 5 (Accountability
Gap). Verify this still holds after Phase A audits land.

== Output ==

Single atomic commit:
- tools/rigor-passes/commons_bonds_rigor_pass_[DATE]_whole_book_stage3_audit_v1.0.0.md

== Hard constraints ==

- Do NOT apply edits.
- Do NOT propose new framework concepts.
- Do NOT re-litigate per-chapter findings (those live in Phase A
  artifacts).
- DO flag structural revisions (multi-chapter sequence changes; arc
  rebalancing) separately from per-chapter spot-fixes.

== Branch discipline ==

Open fresh feature branch claude/manuscript-stage-3-whole-book-<harness-id>
from current origin/main.

After commit lands on main: STOP. Report back to PM session + author.
```

---

## Master Phase C paste-text (per-chapter spot-fix application)

Fires only after author ratifies which Phase A + Phase B findings to apply. One session per chapter (parallel-safe).

```
You are running Phase C of the Manuscript Stage-3 Rigor Pass workstream
(PM dashboard #20) for Chapter [N]. Your job: apply the author-ratified
spot-fixes from the Phase A rigor-pass at [PHASE A ARTIFACT PATH] +
any whole-book-level fixes affecting Ch [N] from the Phase B artifact
at [PHASE B ARTIFACT PATH]. STOP at edited-chapter commit.

== Read in order before doing any work ==

1. THIS paste.
2. [PHASE A ARTIFACT PATH] (Ch [N]'s rigor-pass with author-ratified
   spot-fixes marked).
3. [PHASE B ARTIFACT PATH] (whole-book findings; filter for Ch [N]).
4. [FILE PATH] (chapter file under edit).
5. v2.0 discipline memory + verify-stale-memory-claims discipline.

== Mission ==

Apply ONLY the author-ratified spot-fixes. Do NOT apply non-ratified
findings even if they look correct. Do NOT introduce new findings
during application.

For each ratified fix:
1. Locate the chapter-line per the rigor-pass artifact.
2. Apply the spot-fix per the recommended revision.
3. Verify the fix doesn't introduce regressions (e.g., Path B
   contamination, apparatus regression, named-subject consent
   violations).

== Output ==

Single atomic commit:
- [FILE PATH] (edited)
Commit message references the Phase A artifact + Phase B artifact +
the list of fixes applied.

== Branch discipline ==

Open fresh feature branch claude/manuscript-stage-3-spot-fix-ch[N]-<harness-id>
from current origin/main per tools/workstream-handoffs/README.md.

After commit lands on main: STOP. PM session auto-verifies.
```

---

## Pacing guide

**Recommended cadence (post-Aeon-Jun-1):**

| Week | Activity | Token-budget estimate |
|---|---|---|
| Week of Mon Jun 2 | Phase A: fire 3–4 chapter sessions (Ch 1, 2, 3, 4 — easiest to fact-check) | ~moderate |
| Week of Mon Jun 9 | Phase A: fire 3–4 chapter sessions (Ch 5, 6, 7, 8 — apparatus-heavy) | ~heavy |
| Week of Mon Jun 16 | Phase A: fire 2 chapter sessions (Ch 9, 10) + Phase B whole-book audit | ~moderate-heavy |
| Week of Mon Jun 23 | Author ratifies Phase A + Phase B findings; Phase C spot-fix sessions fire | ~light per fire |

**Author bandwidth load:**
- Phase A: ratifying ~10 rigor-pass artifacts (one per chapter)
- Phase B: ratifying 1 whole-book audit
- Phase C: triggering spot-fix sessions per ratified findings

**Total estimated calendar window:** ~4 weeks (Phase A 3 weeks + Phase B 1 week + Phase C overlapping with Phase B last week + first half of next).

---

## Coordination — relationships with other workstreams

| Workstream | Relationship |
|---|---|
| **#5 Book proposal sprint** (late June 2026) | Phase A + B + C complete BEFORE sprint starts → sample chapters polished when sprint begins. Critical dependency. |
| **#7 Manuscript completion** (Tech Appendix v2.0.0 + Glossary v4 rebuilds) | Run in parallel with this workstream OR after. No hard dependency. |
| **#15 Tech Appendix numbering reconciliation** | COMPLETE 2026-05-11. This workstream operates downstream of #15's canonical scheme. |
| **#9 Apparatus register sweep** | COMPLETE 2026-05-11. This workstream operates downstream of #9's apparatus decisions. |
| **#10 Cross-chapter consistency audit** | COMPLETE 2026-05-11. This workstream operates downstream of #10's canonical-terms inventory. |
| **#19 Tech Appendix Scheme-4 cleanup** + **#18 Ch 6 HTML→MD conversion** | Independent. Can run before, during, or after this workstream. Ch 6 in HTML or MD is fine for Phase A audit. |
| **Wave 1 agent queries** (late July / early August 2026) | Phase C ratification complete BEFORE agent queries fire → polished manuscript ready when agents request full. |

---

## Hard constraints — what NOT to do

- Do NOT fire Phase A before Aeon Jun 1 submission. Author cognitive bandwidth competition.
- Do NOT bundle multiple chapters in one Phase A session. Each chapter is its own session for parallel-safety + clean per-chapter rigor-pass artifacts.
- Do NOT skip Phase B. Per-chapter passes miss cross-chapter sequencing + reader-load arc + apparatus-buildup issues.
- Do NOT apply spot-fixes during Phase A or Phase B. Phase C is the apply-spot-fixes phase; author must ratify findings first.
- Do NOT introduce new framework concepts during any phase.
- Do NOT propose meta-conclusions about the discipline framework.

---

## Reference files

- `tools/drafting-templates/stage-3-three-pass-rigor-audit.md` (Stage 3 template)
- `tools/drafting-templates/audience-pressure-test-construction.md` (audience set construction)
- `tools/audits/cross-chapter-consistency-inventory_2026-05-11.md` (canonical-terms inventory)
- `tools/rigor-passes/commons_bonds_rigor_pass_2026-05-11_apparatus_register_decision_v1.0.0.md` (apparatus decisions)
- `research/audits/cross-chapter-path-b-audit_2026-05-11.md` (cross-chapter Path B baseline)
- `research/literature/bibliography.md` §13 (engagement-flagged comp + framework-adjacent entries)
- `alignment/commons_bonds_framework_positioning_disciplines_v1.0.0.md` (FPD)

---

*End of workstream handoff. Per WP#9: merge per ratified chunk. Update in place if scope evolves; mark complete when Phase C application lands across all 10 chapters.*
