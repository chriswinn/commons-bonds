# Ch 4 → Foreign Affairs — Stage 1 brief kickoff paste-text

**Date staged:** 2026-05-26
**Driven by:** Wave 2 Stage 0 Candidate C (Ch 4 → Foreign Affairs) ratification, RATIFIED 2026-05-25 on origin/main (`da67acf`; TA RCV publication-stability sign-off prerequisite at `d223a7f`)
**Scope:** Stage 1 pre-draft brief work (sub-steps 1a + 1b + 1c per v3.1 doctrine). Stop at Stage 1 brief artifact landed PROPOSED; do NOT pre-stage Stage 2 audience-blind drafting (that fires in its own session after this brief ratifies).
**Cadence:** Amendment C Interactive Ratification Protocol; one-finding-at-a-time discipline per `tools/memory/feedback_parallel_session_ratification_cadence.md`. Author present + ratifying interactively.

**Why fire now (not the rigor-pass-recommended ~Jul 13–19):** The Stage 0 verdict (§4.3 Q2) calibrated brief firing to expected Ch 4 Pass 2 ratification cadence (Pass 2 was 🔴 PROPOSED at `3174cc8` when Stage 0 drafted). Parallel-session work between 2026-05-24 and 2026-05-26 ran the entire Ch 4 chapter Stage 3 cascade ~6 weeks ahead of plan: Pass 2 RATIFIED + APPLIED (`97ba205`); Pass 3.1/3.2/3.3 + Pass 3.4 retrofitted (`7e390c8` + `3a5c03f`); Pass 3.5 RATIFIED + APPLIED + Stage 4 RE-RATIFIED (`8c64e7f`); Pass 3.3 light re-fire post-Pass-3.5 PROPOSED 2026-05-26 (`10f8c72`; confirmation-mode, non-blocking). **Both Finding 2 Option 1 gates from the Stage 0 ratification — Ch 4 Pass 2 ratification + Ch 4 Pass 3.4 closure — are CLEARED.** Brief can fire any time; earlier firing augments the Wave 1 platform paragraph + lets Stage 2 + Stage 3 derivative work proceed without waste-state.

---

## Paste-text — fire in fresh CC session

Paste everything between the `===` markers into a fresh Claude Code session.

```
===

You are running the Stage 1 brief (pre-draft audience + structure pass)
for the Ch 4 *The Existence Proof* → Foreign Affairs derivative essay
(Wave 2, Candidate C). The Wave 2 Stage 0 batch for this candidate
ratified 2026-05-25 (commit `da67acf` on origin/main; with TA RCV
publication-stability sign-off prerequisite at `d223a7f`); your job is
to produce the Stage 1 brief artifact that the subsequent Stage 2
audience-blind draft session will work from.

== Read in order ==

1. THIS paste (framing)
2. CLAUDE.md (workflow doctrine; merge-to-main policy extended
   2026-05-24)
3. tools/memory/feedback_audience_aware_drafting_discipline.md (v3.1
   pipeline doctrine — Amendments A + B + C; Condition-1 anchor 2026-05-21
   re explicit-meta disarming moves for non-partisan-framing-dispositive
   audiences)
4. tools/memory/project_book_complete_marketing_phase.md (book content-
   complete; essays are downstream marketing instruments; reframes
   Stage 0 dimension semantics and the Stage 1 brief that follows from
   them)
5. tools/memory/feedback_named_subject_consent.md (named-subject
   discipline; Ch 4 has minimal named subjects — Norwegian heads-of-
   government + Ken Saro-Wiwa as historical-public-record; no living-
   pending-consent subjects in Ch 4 scope)
6. tools/memory/feedback_parallel_session_ratification_cadence.md
   (one-at-a-time presentation; status markers; end-of-session
   one-liner)
7. tools/commons_bonds_pipeline_doctrine_stage_1_v1.0.0.md (Stage 1
   doctrine — sub-steps 1a/1b/1c)
8. tools/rigor-passes/commons_bonds_rigor_pass_2026-05-24_wave_2_derivative_planning_stage_0_v1.0.0.md
   — focus on §4.3 Candidate C verdict + §12 Candidate C ratification
   record (the latter captures the three ratified findings: TA RCV
   publication-stability gate closure via sign-off pass; Pass 2 +
   Pass 3.4 gate disposition; apparatus-reveal cap ≤22% with selective
   named-OK / EXCLUDED list per BR §8 pattern + Condition-1 disarming-
   moves conditional flag)
9. tools/rigor-passes/commons_bonds_rigor_pass_2026-05-24_ta_rcv_publication_stability_signoff_v1.0.0.md
   (TA RCV sign-off GREEN; load-bearing for the apparatus framing
   in the Foreign Affairs derivative; consult before naming RCV in
   the brief's apparatus-reveal cap section)
10. publishing/essays/_pipeline/cascade-plan_v2_2026-05-24.md (cascade
    plan v2; strategic frame; Wave 2 sequencing context)
11. manuscript/chapters/Chapter__4_TheExistenceProof.md (source chapter;
    current state: full Stage 3 cascade closed — Pass 2 RATIFIED +
    APPLIED `97ba205`; Pass 3.1/3.2/3.3 + Pass 3.4 retrofitted
    `7e390c8`/`3a5c03f`; Pass 3.5 RATIFIED + APPLIED + Stage 4
    RE-RATIFIED `8c64e7f`; Pass 3.3 light re-fire post-Pass-3.5
    PROPOSED 2026-05-26 `10f8c72` non-blocking; ~141 lines post-Pass-
    3.5 restorations adding ~125 words across NBIM-mechanism site at
    line 36 + international-architecture site at line 80)
12. publishing/op-eds/norway-sovereign-wealth/op-ed.md (sibling op-ed;
    differentiation strategy reference — op-ed is news-pegged + 0
    named framework terms confirmed-absent; the Foreign Affairs
    derivative occupies the durable concept-and-name lane and must
    differentiate from the op-ed by naming RCV + B + foreclosure +
    externality framework anchors)
13. Wave 1 brief examples for pattern reference (the $100 Barrel brief
    is the closest fit — institutional-policy register; non-partisan-
    framing-dispositive audience; Condition-1 disarming-moves anchor):
    - tools/rigor-passes/commons_bonds_rigor_pass_2026-05-19_100_barrel_essay_pre_draft_audience_structure_v1.0.0.md
    - publishing/essays/boston-review-accountability-gap/rigor/stage-1-brief.md
      (BR §8 apparatus-exclusion-list pattern is the load-bearing
      precedent for the named-OK / EXCLUDED cap in this brief)
    - tools/rigor-passes/commons_bonds_rigor_pass_2026-05-19_atlantic_ideas_essay_pre_draft_audience_structure_v1.0.0.md

== Your task ==

Produce the Stage 1 brief artifact for Ch 4 → Foreign Affairs
derivative. Walk three sub-steps per v3.1 doctrine:

**Sub-step 1a — Corpus-hygiene invariant gate.** Run
`tools/scripts/check-corpus-invariants.sh` on the Ch 4 source +
verify clean baseline. Surface any HIGH severity scaffolding /
regressed-pattern findings as ESCALATIONs to the author. (Ch 4 is
post-Pass-3.5 Phase C; expected clean; this is the procedural gate.)

**Sub-step 1b — Canonical fact-ground + audience-aware structure +
render-safe convention.** The substantive brief work. Produce:

- **Canonical fact-ground** — verbatim source-of-truth for facts the
  Stage 2 audience-blind draft will absorb (per Amendment A 2026-05-10
  anchor: Stage 1 must supply canonical factual ground truth, not
  just beats). Include: Ekofisk 1969 + Block 2/4 discovery; GPFG
  founding 1990 + renamed 2006 (NOT conflated — see Stage 3 fact-
  check pass at `tools/rigor-passes/commons_bonds_rigor_pass_2026-05-12_ch4_existence_proof_stage3_fact_check_v1.0.0.md`);
  $1.9T fund / $340k per-citizen scale; 70–80% state capture of net
  petroleum value; 2001 fiscal rule + ~3% real-return draw cap; the
  political-coalition list (Stoltenberg I Labour-led adopter →
  Bondevik II center-right → Stoltenberg II Labour → Solberg
  Conservative → Støre Labour-Centre — Bondevik order corrected per
  Stage 3 fact-check pass); Equinor / formerly Statoil + 2018
  rename; the NBIM operational-arm + ethics-council + Storting-
  supermajority architecture detail per Pass 3.5 line 36 restoration;
  the Nigeria contrast — Niger Delta + Ogoni + UNEP 2011 + $1B
  remediation estimate + 25–30 year timeline + Ken Saro-Wiwa
  1995 + post-execution diplomatic response; the international-
  architecture + colonial-era concession-inheritance detail per
  Pass 3.5 line 80 restoration; the Alberta Heritage Trust Fund
  1976 + repeated draw-downs / Alaska Permanent Fund 1976 + dividend-
  distribution contrast; the U.S. Social Security 1935 pay-as-you-go
  comparison + Bismarck Germany 1889 partial-funding + WWI
  hyperinflation breakdown.
- **Audience-aware structure** — Foreign Affairs editorial brain +
  reader profile. Foreign Affairs is **dispositively non-partisan-
  aligned by venue** (CFR-published; institutional-policy register);
  per the Stage 0 Candidate C ratification record, this means the
  Condition-1 explicit-meta disarming-moves discipline is LESS
  load-bearing here than at PW or Atlantic Ideas — flag it only if
  Stage 1 audience analysis surfaces center-right-policy-reader as
  Tier 1 dispositive (e.g., a Foreign Affairs subscriber who reads
  the framework's "cost severance" naming through a deregulatory-
  industrial-policy lens). Tier 1 dispositive audience candidates:
  Foreign Affairs subscriber / CFR member / international-economics
  policy elite; sovereign-wealth-fund domain practitioner (Truman,
  Cumming, NBIM-adjacent); Mazzucato/Tooze cluster comp-author
  reader. Tier 2 acceptance set: Brookings / PIIE / heterodox-econ
  policy reader; Christophers/Susskind cluster comp-author reader;
  Norway-cluster scholar (Norway-watching policy academic). Tier 3
  adversarial-load: Public Choice / industry-funded petroleum
  economist; reactionary intellectual reading "Norway has the rents,
  Norway is the model" through a sovereignty-skeptical lens;
  procedural-conservative who reads "residual commons value" as
  legal-framing entitling redistributive claims. Word-count target
  4,000–7,000w (Foreign Affairs band; let substance drive length
  per `tools/memory/feedback_substance_drives_length.md`).
  Structural beats with rhetorical anchors but NOT prose.
- **Render-safe convention** — em-dash / smart-quote / en-dash
  usage; scene-shift markers; section header convention; footnote /
  citation convention (Foreign Affairs house style if known + practical
  default per Wave 1 examples — $100 Barrel brief is the institutional-
  policy register precedent). Per the em-dash-overuse memory
  (`tools/memory/feedback_em_dash_overuse.md`): em-dashes require active
  justification; default to commas / periods / restructure for smoother
  prose.
- **Apparatus-reveal cap (load-bearing from Stage 0 §4.3 + §12
  Candidate C Finding 3):** ≤22% effective reveal. The named-OK +
  EXCLUDED inventory below is RATIFIED and load-bearing — do not
  re-litigate; embed verbatim in the brief's apparatus sub-section.
  - **NAMED-OK at brief time:** "residual commons value" (as a
    concept + named phrase); RCV acronym (in conjunction with the
    full phrase); "cost severance" (named); "accountability bond B"
    (named, with B as a variable); foreclosure component; externality
    tail; Norway full case; Nigeria full case.
  - **EXCLUDED at brief time:** CS = RCV − B equation (formal
    equation form); B₁ / B₂ bond decomposition (Restitution Bond /
    Foreclosure Bond names); Three Ways of Counting (Approach 1/2/3
    by name); Four Gates (named); CIT / Commons Inversion Test
    (named); Cᵢ component vocabulary (all 8 component names —
    Direct Health Cost, Environmental Degradation Cost, Community
    Disruption Cost, Foreclosure Cost, Lineage Labor Cost, Knowledge
    and Cultural Cost, Political Capture Cost, Temporal Displacement
    Cost); IPG / Intergenerational Pricing Gap (named); ARR /
    Asymmetric Regret Rule (named); Hartwick identity / rule (named);
    Pattern 2 register language.
  - **Verification cadence:** the cumulative effective reveal ≤22%
    target is verified at Stage 3 Pass 3.3 with cumulative-portfolio
    audit (per the BR pattern that landed Stage 5 RATIFIED clean
    at `d34214d`).
- **Named-subject status (no living-pending-consent gating):**
  - Norwegian heads-of-government (Stoltenberg, Bondevik, Solberg,
    Støre): historical-public-record / institutional-spokesperson;
    public-record exception applies for attribution; no consent
    issue. Names eligible.
  - Ken Saro-Wiwa: deceased 1995 (historical-record / executed); no
    consent issue. Name eligible.
  - Ogoni + Ijaw communities + Niger Delta communities: collective
    referents (not individual named subjects); no per-person consent
    issue.
  - UNEP report authors (institutional attribution): public-record;
    no consent issue.
  - Truman + Cumming (Foreign Affairs sovereign-wealth essayists):
    public-record (their FA essays are on-record publications);
    citation-accuracy courtesy-notify protocol available if directly
    quoted; not required for general reference.
  - No living-pending-consent gating remains for Ch 4 → Foreign
    Affairs derivative scope.
- **Differentiation from the Norway op-ed (load-bearing):** The
  Norway op-ed at `publishing/op-eds/norway-sovereign-wealth/op-ed.md`
  occupies the news-pegged + apparatus-free short-form lane (0 named
  framework terms; Path B audit verified). The Foreign Affairs
  derivative occupies the durable concept-and-name lane: names RCV
  + B + foreclosure + externality framework anchors. These two lanes
  must not collapse — the brief's structural beats should make clear
  that the FA derivative ADDS analytical bite (the RCV-frame Norway/
  Nigeria/Bismarck/Social-Security comparison) rather than retreading
  the op-ed's "Norway has a good fund, here's how it works" framing.
- **Marketing-phase reframing** (per
  `tools/memory/project_book_complete_marketing_phase.md` RATIFIED
  2026-05-25): framework is locked in the manuscript; the Stage 1
  brief does NOT need to stress-test apparatus framing (that work is
  done at the chapter Stage 3 + Tech Appendix level per the
  2026-05-24 TA RCV sign-off). Stage 1 brief work is marketing-pitch
  construction + audience calibration, not platform-development.

**Sub-step 1c — Cross-artifact coherence check.** Verify the brief
against:
- Ch 4 source chapter (current state on main; post-Pass-3.5 Phase C
  application; ~141 lines)
- Tech Appendix RCV definitions (Definitions 1.6 + 1.7 + CS = RCV − B
  at TA §1; verified GREEN at the 2026-05-24 sign-off pass; brief's
  named-OK use of RCV / B / foreclosure / externality must align
  with TA canonical form)
- Sibling-chapter bibliography (sovereign-wealth + UNEP 2011 + Saro-
  Wiwa citations; check consistency with bibliography file at
  `research/literature/bibliography.md`)
- AuthorsNote (if relevant facts from Ch 4 are also cited there)
- Ch 4 rigor-pass artifacts (full Stage 3 cascade artifacts in
  `tools/rigor-passes/`; especially the Pass 3.5 developmental-edit
  review for the NBIM + international-architecture restorations and
  the Pass 3.4 robustness for the adversarial-set baseline)
- Cascade plan v2 strategic-frame (trailing-Wave-1 by 30–90 days;
  marketing-phase reframing; agent target list considerations from
  Ch 3 + Ch 2 ratification-record surfaced amendments)
- The Norway op-ed (differentiation check; ensure brief's structural
  beats establish FA-derivative-distinct value vs op-ed)

== Hard constraints ==

- Stage 1 brief only. Do NOT begin Stage 2 audience-blind drafting
  in this session.
- Brief artifact lands PROPOSED at session close; author ratifies
  interactively per Amendment C; spot-fixes apply in this session.
- Brief is internal scaffolding → auto-fast-forward merge to main
  per CLAUDE.md merge-to-main policy at session close.
- Apparatus-reveal cap (NAMED-OK / EXCLUDED inventory above) is
  load-bearing — verify at sub-step 1b close + at 1c cross-check.
  The cap was ratified at Stage 0 Finding 3 Option 1; do NOT
  re-litigate the cap; embed it verbatim.
- Named-subject discipline is closed (no living-pending-consent
  gating); embed the closed-discipline language in the brief's
  named-subject sub-section.
- Differentiation from the Norway op-ed is load-bearing; the brief
  must articulate the FA-derivative-distinct value lane.
- Condition-1 disarming-moves: flag-as-conditional in the brief
  (depends on Stage 1 audience-analysis output); do NOT pre-commit
  to explicit-meta moves unless Tier 1 dispositive audience surfaces
  center-right-policy-reader.
- Per `feedback_parallel_session_ratification_cadence.md` cadence:
  one-finding-at-a-time presentation; track inventory internally;
  severity-strict ordering HIGH → MED → LOW; use status markers
  (🔴 🟡 🟢 🔵 ⏳ 🟣 ✅); end-of-session standardized one-liner:
  `STATE: PROPOSED|APPLIED|RATIFIED; NEXT: [next-action]; AWAITING:
  [next-gate]`.

== Resume marker for parent session ==

When this Stage 1 brief session closes, the brief artifact will
land at:
`tools/rigor-passes/commons_bonds_rigor_pass_2026-05-26_ch4_foreign_affairs_essay_pre_draft_audience_structure_v1.0.0.md`
(or similar dated filename per Wave 1 brief naming convention).

Parent session (the Stage 0 ratification session) is closed; resume
context for the next phase (Stage 2 audience-blind drafting) lives in
the brief artifact itself + the Stage 0 ratification record at
§12 Candidate C of the Wave 2 batch artifact.

When the Stage 1 brief ratifies, fire the Stage 2 audience-blind
drafting session in a fresh session spawned from the brief's paste-
text scaffold (the brief itself produces the Stage 2 kickoff per the
Wave 1 pattern).

===
```

---

## Resume marker (for the parent ratification session if author returns)

- **Stage 1 brief artifact expected at:** `tools/rigor-passes/commons_bonds_rigor_pass_2026-05-26_ch4_foreign_affairs_essay_pre_draft_audience_structure_v1.0.0.md` (or similar dated filename).
- **Status to look for:** `STATE: PROPOSED` at session close → author interactive ratification → `STATE: RATIFIED` after spot-fixes apply.
- **Next phase after Stage 1 brief ratifies:** Stage 2 audience-blind drafting (fresh session; brief artifact produces Stage 2 kickoff).

## Cross-references

- Wave 2 Stage 0 Candidate C ratification record: `tools/rigor-passes/commons_bonds_rigor_pass_2026-05-24_wave_2_derivative_planning_stage_0_v1.0.0.md` §12 (commit `da67acf` 2026-05-25)
- TA RCV publication-stability sign-off (load-bearing prerequisite): `tools/rigor-passes/commons_bonds_rigor_pass_2026-05-24_ta_rcv_publication_stability_signoff_v1.0.0.md` (commit `d223a7f` 2026-05-24)
- Ch 4 source: `manuscript/chapters/Chapter__4_TheExistenceProof.md`
- Norway sibling op-ed (differentiation reference): `publishing/op-eds/norway-sovereign-wealth/op-ed.md`
- Stage 1 doctrine: `tools/commons_bonds_pipeline_doctrine_stage_1_v1.0.0.md`
- Marketing-phase memory: `tools/memory/project_book_complete_marketing_phase.md`
- Cascade plan v2: `publishing/essays/_pipeline/cascade-plan_v2_2026-05-24.md`
- Wave 1 brief examples: `tools/rigor-passes/commons_bonds_rigor_pass_2026-05-19_100_barrel_essay_pre_draft_audience_structure_v1.0.0.md` (closest fit — institutional-policy register) + Boston Review brief (BR §8 apparatus-exclusion-list pattern precedent) + Atlantic Ideas brief
- Ch 4 chapter-side Stage 3 cascade artifacts (full set in `tools/rigor-passes/`):
  - `ch4_existence_proof_stage3_pass_3_1_verify_2026-05-25.md`
  - `ch4_existence_proof_stage3_pass_3_2_verify_2026-05-25.md`
  - `ch4_existence_proof_stage3_pass_3_3_acceptance_2026-05-25.md`
  - `ch4_existence_proof_stage3_pass_3_4_robustness_2026-05-25.md`
  - `ch4_developmental_edit_review_2026-05-25.md`
  - `ch4_existence_proof_stage3_pass_3_3_light_refire_post_pass_3_5_2026-05-26.md`
- Sibling Ch 2 → Harper's Stage 1 brief kickoff (parallel-fired Wave 2 candidate; format precedent for this file): `tools/workstream-handoffs/ch2-harpers-stage-1-brief-kickoff_2026-05-26.md`

---

*End of Ch 4 → Foreign Affairs Stage 1 brief kickoff paste-text.*
