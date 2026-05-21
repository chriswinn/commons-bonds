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

For Phase A sessions, use the table below to assemble each chapter's paste-text from the master template (§Master Phase A paste-text below).

| Ch | File path | Word count target | Key named subjects | Key named cases | Specific audit emphases |
|---|---|---|---|---|---|
| 1 | `manuscript/chapters/Chapter__1_TheQuietMath__Draft.md` | ~3,400w | Author's son (anonymized); author's father; author's grandfather (deceased, NACA/NASA inventor LaVern E. Winn — name authorized per project_authors_grandfather_nasa_inventor memory) | NICU scene; air-compressor scene (Section II); 120-hour workweek; DMV math; McDowell counter-objection | Memoir-register consistency; named-subject consent (son/father). **PHASE A PASS 1 COMPLETE 2026-05-12** — see `tools/rigor-passes/commons_bonds_rigor_pass_2026-05-11_ch1_the_quiet_math_stage3_fact_check_v1.0.0.md`; F-1 + F-2 applied; F-3 + F-4 declined; Passes 2 + 3 pending. |
| 2 | `manuscript/chapters/Chapter__2_TheMiner.md` | ~5,000w | INTERVIEW NEEDED placeholders (3 flagged per weekly-audit-2026-04-28) | McDowell County coal; black lung; Appalachian community collapse | INTERVIEW NEEDED placeholders should be resolved or flagged; Ch 2 Cost Severance defense paragraph (commit `8e61cd1`) consistency with surrounding prose; pivot away from $100-barrel-passage (now resolved) |
| 3 | `manuscript/chapters/Chapter__3_TheWaterman__Draft.md` | ~?w (verify) | Biggie (deceased, named; Phat's (anonymized as "a crabber and a fisherman" pending consent); Fox Hill community; Allison Colden (CBF MD); Karen Moore (CBF VA) | Chesapeake fisheries restoration; Fox Hill mutual aid 3am scene; oyster trajectory; VMRC | Biggie courtesy-notify-family before publication; Phat's consent status; substitution-hypothesis CONFIRMED (commits `0e83dc5` + `c352d9a`); VMRC date correction landed (`b5692f1`) |
| 4 | `manuscript/chapters/Chapter__4_THEEXISTENCEPROOF__Draft.md` | ~3,975w | Norway leadership (verify named figures); Petroleum Fund founders | Norway GPFG; Ekofisk discovery 1969; petroleum-state counterfactuals (Venezuela, Nigeria, etc.) | GPFG founding-date precision (was 1990 as Government Petroleum Fund; renamed 2006 — the op-ed session caught this drift, verify Ch 4 doesn't carry same error); Bondevik-coalition timing |
| 5 | `manuscript/chapters/Chapter__5_THEACCOUNTABILITYGAP__Draft.md` | ~9,574w | Pistor (Code of Capital); Christophers (Price is Wrong); Coates; Darity & Mullen; Hamilton; Conley; Sandel; Parfit; Pettit; Skinner | Libby asbestos (W.R. Grace 2009 acquittal); Deepwater Horizon; restitution + foreclosure bond lineages | Why-bonds umbrella defense paragraph (commit `1c83753`) integration; Restitution Bond + Foreclosure Bond name-defense paragraphs (commit `caa987e`); Path B fix Ch 5↔Ch 6 Restitution Lineage clone resolved (commit `5643f70`) — verify no regression |
| 6 | `manuscript/chapters/Chapter__6_ThreeWaysofCounting__Draft.html` | ~75KB (HTML; verify word equivalent) | Hotelling; Ostrom; Mazzucato (Value of Everything); Hartwick | Three Ways of Counting; CIT (Commons Inversion Test); ARR (Asymmetric Regret Rule); Hotelling Identity; RCV three-component decomposition | RCV three-component name-defense (commit `1f3ad9c`); 4 widened-sweep defense paragraphs inserted (commit `2a7c336` — CIT, ARR, Externality Tail in Ch 6; Abundance Masking in Ch 7); Tech Appendix #15 Phase 5 layman-lookup hyperlinks (commit `50ec90b`); apparatus items 1–8 ratifications carried; methodology-chapter earns apparatus per #9 decisions |
| 7 | `manuscript/chapters/Chapter__7_OnOtherWorlds__Draft.md` | ~8,537w | Mars / closed-habitat thought-experiment characters; Devon Island; HI-SEAS contexts | Mars colony scenario; six cost-hiding patterns (Ostrom-path framing per Item 15 `b1c17d8`); Abundance Masking definitional surfacing | Aeon source material — protect against thunder-stealing with Aeon "Mask of Abundance" pitch (Version C, ready Mon Jun 1); Abundance Masking defense paragraph (`2a7c336`); Ostrom-path light-de-formalize per Item 15 |
| 8 | `manuscript/chapters/Chapter__8_WhatThingsActuallyCost_Draft.md` | ~6,026w | (verify named subjects) | McDowell coal per-ton arithmetic; Cᵢ component examples; black-lung trust fund (Ch 2↔Ch 6↔Ch 8 lineage) | Inline integral stripped Item 1 (`d1f6e2d`); Ch 8 line 71 stale "$100 barrel" reference (need to verify if patched by #10 or cross-thread #9 still pending); Dunbar/Du Bois/Ellison/Fanon engagement applied 2026-05-08 |
| 9 | `manuscript/chapters/Chapter__9_PricingHonestly__Draft.md` (verify exact filename) | ~10,178w | Susskind (Growth: A Reckoning); Christophers (Price is Wrong); Pistor cross-reference | Pricing mechanics; four-step framework (Classify → Reserve → Invest → Reassess); property-rights limits | Christophers + Susskind engagement applied 2026-05-08 (commit `d78872e`); secondary Pattern Made Visible cross-reference to Ch 5; cross-chapter consistency batches landed 2026-05-11 |
| 10 | `manuscript/chapters/Chapter__10_CommonBonds__Draft.md` (verify exact filename) | ~7,366w | (verify named subjects) | Sunset bookend with Ch 1 sunrise; framework synthesis | Sunrise/sunset bookend coherence with Ch 1; framework-positioning-disciplines summary land; cumulative-portfolio reader's experience |

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
2. tools/workstream-handoffs/manuscript-stage-3-rigor-pass-handoff_2026-05-11.md
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
2. tools/workstream-handoffs/manuscript-stage-3-rigor-pass-handoff_2026-05-11.md
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
