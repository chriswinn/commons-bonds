---
name: Pipeline doctrine — single unified pipeline for publisher-facing prose (v3.1)
description: Six-stage pipeline (Stages 0-5) with five-pass Stage 3 (Amendment B 2026-05-18 added Pass 3.5 developmental-edit) + two-class cascade (Amendment A 2026-05-18 — automatic-on-edit vs explicit-gate) + continuous invariant-gate scans + change-cascade routing + cross-chapter workstream lifecycle. Extends v3.0 (2026-05-17) → v2.0 Amendment B. Canonical full doctrine at tools/pipeline-doctrine/commons_bonds_pipeline_doctrine_v1.0.0.md in commons-bonds repo.
type: feedback
originSessionId: 6a97b0f9-c18b-4992-8bf6-b2bbf9c60acf
---
**Canonical full content:** `tools/pipeline-doctrine/commons_bonds_pipeline_doctrine_v1.0.0.md`
**Layer:** scan-friendly summary; this file is the cross-session discipline pointer. Update the canonical artifact when content changes; sync this summary via `tools/memory-updates/` spec for substantive amendments.

# feedback_audience_aware_drafting_discipline (v3.0)

**Date:** 2026-05-17
**Supersedes:** v2.0 Amendment B (2026-05-10 + 2026-05-13)
**Canonical full doctrine:** `tools/pipeline-doctrine/commons_bonds_pipeline_doctrine_v1.0.0.md` in
the commons-bonds repo. This memory entry is the scan-friendly summary; the
doctrine artifact carries the full architecture.

## Summary

Publisher-facing prose moves through a single unified pipeline with six stages
and continuous invariant-gate scans:

- **Stage 0:** author conception / topic decision.
- **Stage 1:** ready-to-draft gate (three sub-steps).
  - **1a:** corpus-hygiene invariant gate (scaffolding scan + regressed-pattern
    scan via `tools/scripts/check-corpus-invariants.sh`).
  - **1b:** canonical fact-ground + audience-aware structure + render-safe
    convention (existing Stage 1 template).
  - **1c:** cross-artifact coherence check (bibliography + AuthorsNote +
    sibling-chapter + rigor-pass coherence).
- **Stage 2:** audience-blind drafting (existing).
- **Stage 3:** five-pass rigor audit.
  - **3.1:** fact-check (per v2.0).
  - **3.2:** voice-polish (per v2.0).
  - **3.3:** audience-load acceptance (target audiences; INCLUDE / EXCLUDE
    verdict per character).
  - **3.4:** audience-load robustness (adversarial / detractor characters;
    thread-pull synthesis verdict; NEW in v3.0).
  - **3.5:** developmental-edit (whole-chapter restoration-of-richness lens;
    catches emotional-arc continuity + scene-anchor density + sensory-detail
    restoration + voice-flow continuity + cumulative-LLM-cadence residue +
    reader-engagement at analytical pivots; restoration polarity, NOT cutting;
    NEW in v3.1 Amendment B 2026-05-18).
- **Stage 4:** render + character-integrity audit (NEW in v3.0).
- **Stage 5:** academic-rigor + prose-quality sign-off bookend + pre-publication
  review queue artifact (NEW in v3.0).

Per-prompt serial cadence enforced (each pass fires in its own prompt; author
ratifies + spot-fixes apply before next pass fires).

**Amendment A two-class cascade (ratified 2026-05-18 — load-bearing for
per-session pipeline routing):**

- **Automatic-on-edit cascade** (cheap; fires on every prose edit): Pass 3.1
  fact-check + Pass 3.2 voice-polish + Stage 1c-light cross-artifact coherence.
  ~10K-30K tokens per prose-edit event; justified by value-added prose rigor.
- **Explicit-gate cascade** (heavy; fires only on author trigger at specific
  gates — venue change, pre-publication, cross-chapter workstream close,
  author "build it now" / "developmental read-through"): Pass 3.3 acceptance +
  Pass 3.4 robustness + Pass 3.5 developmental-edit + Stage 4 render-audit +
  Stage 5 sign-off + pre-pub queue. 40K-160K tokens per pre-pub batch;
  amortized over many prose edits rather than paid per spot-fix.

Token-economy rationale: render-toolchain containerization (Docker / remote-
container) drove Stage 4 Claude-token cost to ~0; the cascade reflects that
heavy passes should only fire when an artifact actually approaches a
distribution-readiness gate.

## Bookend sign-offs

Both academic-rigor AND prose-quality sign-offs at BOTH Stage 1 AND Stage 5.
Stage 1 verifies the ready-to-draft brief; Stage 5 verifies no drift through
the pipeline + generates the pre-publication review queue artifact.

## Change-cascade routing

Any change routes back to the appropriate prior stage. Specific rules:
- New fact → Stage 1b → re-fire Pass 3.1 + 3.2 + 3.3 (+ 3.4 if material).
- New audience character → Stage 1b → re-fire Pass 3.3 (+ 3.4 if adversarial).
- Bibliography commitment → Stage 1c → affected chapter's Pass 3.3 (light)
  re-fire.
- Spot-fix applied → Stage 1c (light) → Pass 3.3 (light) re-fire.
- Cross-chapter workstream → Stage 1c for all affected chapters → each
  chapter's Pass 3.3 (light) re-fire.
- Any source-file change → Stage 1a invariant scan (automatic via pre-commit
  hook).

## Single-pipeline architecture

Math + prose + tables + figures all go through the same pipeline. Content-type-
aware sub-protocols at each stage handle type-specific work. No parallel
pipelines for math vs prose.

## Cross-chapter workstream lifecycle

Workstreams touching multiple chapters get a first-class six-step lifecycle:
surfaces → PM ratifies + spins up → single feature branch applies cross-chapter
touches → each touched chapter auto-triggers Stage 1c + Pass 3.3 light re-fire
→ workstream closes only after all re-fires complete clean → cross-thread-todos
+ workstream-handoff archived.

## Pre-publication review queue

Mandatory hand-off artifact at Stage 5. Goes to publisher / agent / editor with
the manuscript-submission package. Contents: what has been internally verified
+ what has NOT been externally verified + recommended external reviewer types
+ highest-priority sections for external review if publisher budget is limited.
Transparent quality-control disclosure rather than overclaiming-verification
posture.

## Invariant-gate infrastructure

Two continuous scans (pre-commit + every stage transition + CI):
- **Scaffolding scan** — `tools/quality-gates/scaffolding-patterns.yaml` —
  placeholders (`TODO`, `TK`); drafting-template scaffolding; process-scaffolding
  vocabulary (`Option A`-`Z`, `ratified`, `Phase C-*`, `F-V*`, INCLUDE/EXCLUDE
  glyphs); meta-commentary tics.
- **Regressed-pattern scan** — `tools/quality-gates/regressed-patterns.yaml` —
  patterns previously fixed by rigor passes; deprecated terminology; gate-decision-
  banned patterns (vendor names per CEO-era NDA); render-failure patterns.

Both registries severity-tiered (HIGH = block; MEDIUM = flag; LOW =
informational) with per-file allowlist support.

Implementation: `tools/scripts/check-corpus-invariants.sh`.

## What v3.0 changes from v2.0 Amendment B

- Three passes → four passes (Pass 3 split into 3.3 acceptance + 3.4
  robustness).
- Stage 1 single-step → three sub-steps (1a invariant gate + 1b substantive
  + 1c cross-artifact coherence).
- New: Stage 4 render + character-integrity audit.
- New: Stage 5 bookend sign-off + pre-publication review queue artifact.
- New: change-cascade routing protocol codified.
- New: cross-chapter workstream lifecycle codified.
- New: continuous invariant-gate infrastructure (scaffolding + regressed-
  pattern scans).
- v2.0 Amendment B's three-pass discipline + per-prompt serial cadence is
  preserved as the core of Stage 3.

## What v3.1 adds beyond v3.0 (Amendments A + B, ratified 2026-05-18)

- **Amendment A — Two-class cascade.** Original v3.0 cascade treated all
  stages as equally auto-firing on every relevant change. Amendment A splits
  the cascade into automatic-on-edit (Pass 3.1 + Pass 3.2 + Stage 1c-light;
  fires on every prose edit) vs explicit-gate (Pass 3.3 + Pass 3.4 + Pass 3.5
  + Stage 4 + Stage 5; fires only on author trigger at specific gates —
  venue change, pre-publication, cross-chapter workstream close, author
  "build it now" / "developmental read-through"). Token-economy rationale:
  render-toolchain containerization (Docker / remote-container) drove
  Stage 4 Claude-token cost to ~0, freeing the cascade to defer heavy passes
  until distribution-readiness gates rather than per-spot-fix.
- **Amendment B — Pass 3.5 developmental-edit codified.** Four passes → five
  passes. Pass 3.5 fires per-chapter AFTER Pass 3.1 + 3.2 + 3.3 + 3.4
  ratify-and-apply complete; restoration polarity (3.2 cuts, 3.5 restores —
  different polarities; folding would lose the discipline each needs);
  whole-chapter scale; ~50K-80K tokens per chapter; explicit-gate per §3.2.
  Empirically grounded by Ch 1 developmental-edit review 2026-05-18
  (3 HIGH + 7 MEDIUM + 3 LOW findings; HIGH findings clustered around
  recurring patterns — scene-anchor restoration, sensory-detail restoration,
  both/and reveal breath, framework-close breath, faithfulness-of-the-model
  lineage). Light Pass 3.3 re-fire recommended after Phase C application of
  ratified Pass 3.5 spot-fixes; Pass 3.4 re-fire NOT routinely warranted
  (restorations strengthen rather than weaken adversarial robustness).
- Per-prompt serial cadence extends: 3.1 → 3.2 → 3.3 → 3.4 → 3.5 (each pass
  in its own prompt; author ratifies + spot-fixes apply before next pass
  fires).
- Pass 3.5 is also Amendment-C-scoped (Interactive Ratification Protocol for
  prose-modifying passes, ratified 2026-05-19): per-finding format must
  include Options + Recommendation + Reasoning; ratification + application
  combine in one session.

## Empirical anchors

- v2.0 Amendment B empirical validation: op-ed pipeline session
  (commit 5167edd, 2026-05-10) ran its own three-pass Stage 3; fact-check
  pass caught two real factual drifts (GPFG founding-date conflation +
  Bondevik-coalition timing) that audience-load alone would have missed.
- v3.0 empirical validation: Ch 1 Pass 3 REAUDIT v3 (2026-05-17,
  `tools/rigor-passes/commons_bonds_ch1_stage_3_pass_3_audience_load_REAUDIT_2026-05-17_PROPOSED.md`)
  ran the 40-character full-rigor + adversarial set; adversarial test
  surfaced the Public Choice rent-seeking-engagement thread that became a
  cross-chapter workstream (would have been missed by acceptance-only).
- v3.0 Condition-1-execution-choice anchor: $100 Barrel parallel-Stage-2-drafts
  comparative audit (2026-05-21,
  `publishing/essays/100-barrel/rigor/stage-3-comparative-draft-audit.md`)
  ran the full 18-character acceptance + 5-character adversarial set across
  two parallel Stage 2 drafts of the same brief. Both drafts were
  Stage-1-brief-compliant. The differential was **execution choice**:
  Draft A's explicit-meta Condition-1-disarming moves ("Note the move I have
  just made... I am not endorsing his political program"; "I want to name
  what I am doing here"; "Readers who find Rawls unpersuasive should ask
  themselves whether they find Sandel and Parfit equally unpersuasive") vs
  Draft B's embedded-disarming-in-flowing-prose. The Tier 1 dispositive
  Condition 1 audience (center-right policy reader) + the adversarial A4
  reactionary intellectual reader both passed Draft A on skim-read with
  ✓✓✓ but passed Draft B only on close-read (⚠ skim-read risk). Discipline
  carry-forward: when a Stage 1 brief specifies a Condition-1-style
  non-partisan-framing-discipline dispositive audience, **explicit-meta
  disarming moves should be flagged as the recommended Stage 2 execution
  choice** rather than left to Stage 2 prose discretion. The discipline
  produced two parallel brief-compliant drafts (Draft B archived at
  `archive/_OneDayMaybe/100-barrel-essay-variants/100-barrel-essay-draft_2026-05-19_v1.0.0_variant-fbc623.md`)
  precisely because the Stage 1 brief did not flag this — useful evidence
  that Stage 1 brief templates should add this flag for future briefs with
  dispositive non-partisan audiences.
- Stage 4 friction-anchors: tofu-box em-dash / ≈ rendering issues
  (Ch 5 + Ch 6, commit `d238f2c`); Chrome-vs-wkhtmltopdf rendering
  divergence (commit `cf24f57`); EB Garamond font-family naming
  (commit `3208619`); author's lived-experience math-formula corruption
  at NIH-era publications.

## Discipline carry-forward from v2.0 (unchanged in v3.0)

- Each pass produces its own findings list.
- Per-prompt serial cadence: each pass fires in its own prompt; author
  ratifies + spot-fixes apply before next pass fires.
- Pass 3.3 acceptance verdict is per-character INCLUDE / EXCLUDE.
- Pass 3.4 robustness verdict is thread-pull synthesis (NOT pass/fail per
  character).
- Stage 3 audit; remediation is separate.
- Hard constraints: never force-push main; never amend a commit on
  origin/main; never skip hooks without explicit author direction.

## Where to read more

- Full doctrine: `tools/pipeline-doctrine/commons_bonds_pipeline_doctrine_v1.0.0.md`
- Stage 1: `tools/pipeline-doctrine/commons_bonds_pipeline_doctrine_stage_1_v1.0.0.md`
- Stage 4: `tools/pipeline-doctrine/commons_bonds_pipeline_doctrine_stage_4_v1.0.0.md`
- Stage 5: `tools/pipeline-doctrine/commons_bonds_pipeline_doctrine_stage_5_v1.0.0.md`
- Stage 3 template (revised): `tools/drafting-templates/stage-3-three-pass-rigor-audit.md`
- Audience pressure-test construction (revised): `tools/drafting-templates/audience-pressure-test-construction.md`

### Three-home cross-reference (added 2026-05-31 per memory-process-review v2 B.6)

The v3.1 pipeline doctrine deliberately lives in three homes serving three distinct audiences:

| Home | Audience | Granularity |
|---|---|---|
| This memory file (`tools/memory/feedback_audience_aware_drafting_discipline.md`) | Every CC session (always-load via CLAUDE.md `@import`) | Scan-friendly summary (~18KB) |
| [`tools/pipeline-doctrine/`](../pipeline-doctrine/) (4 files: v1.0.0 main + Stage 1 / 4 / 5 deep-dives) | Sessions executing the pipeline | Full canonical doctrine + per-stage deep-dives (~90KB total) |
| [`tools/writing-process/`](../writing-process/) (rigor-pipeline-overview, audience-character-roster, planned interview-prep-process) | External readers + future projects | Portable extracts; project-specific examples generalized; lift-and-reuse-ready |

**Doctrine-amendment discipline.** Any future amendment to the v3.1 doctrine (Amendment D, Amendment E, etc.) MUST update all three homes — drift across them is the failure mode this cross-reference is here to prevent. The amendment session is responsible for cascading the change into all three; the sequenced update order is (1) `tools/pipeline-doctrine/` canonical full doctrine, (2) this memory file summary, (3) `tools/writing-process/` portable extracts. Step 1 establishes ground truth; steps 2 + 3 keep the summary + portable forms in sync.

---

## Historical record — v2.0 Amendment B empirical anchoring (preserved as audit-trail)

The detailed narrative below is preserved from the v2.0 Amendment B memory entry
(ratified 2026-05-10) as audit-trail. v3.0 extends rather than supersedes the
underlying three-pass discipline, so the empirical grounding remains live.

**v2.0 ratification context (2026-05-10).** v2.0 ratified after the parallel
Noema essay + Aeon pitch Stage 3 per-test verdicts (`publishing/essays/noema-commons-bonds/rigor/stage-3-comparison_2026-05-10.md`
and `..._aeon_pitch_stage3_comparison_v1.0.0.md`).

**Noema test — audience-blind validation + drift-discovery anchoring Amendment A
+ Amendment B fact-check pass.** Validated audience-blind Stage 2 decisively on
Path B compliance: verbatim Ch 1 sentences dropped from ~17–22 (Essay A, drafted
from Ch 1) to ~3–4 (Essay B, drafted audience-blind from a Stage 1 brief), and
structural close-paraphrase paragraphs dropped from ~14 to 0. The Stage 1
apparatus prohibition held through audience-blind drafting (the "cluster-γ"
tripwire never reached Essay B). BUT Stage 2 introduced 5+ factual drift points
and 1 structural omission in Essay B — Pou/Pooh nickname etymology rewritten
with an invented Tidewater-accent provenance; predawn-Appalachian drives
reframed as a Navy commute rather than hunting trips; "fifteen audiences"
reframed from reader-audiences to meeting-audiences; "responsible for 45
people" misframed as direct management rather than original-scope-before-cutback;
cussing scene direction inverted from cursing-at-self to cursing-at-recipient;
air-compressor anecdote compressed to a one-sentence summary rather than
reconstructed as a scene. These drove Amendment A (Stage 1 must supply
canonical factual ground truth, not just beats) and Amendment B's fact-check
pass at Stage 3. The voice-polish pass (Amendment B) is empirically grounded
in Essay B's expository flatness and meta-commentary patterns ("The plain
definition is this:" / "That is the whole sentence.") that pass-1 drafting
with Ch 1 prose in front of the drafter had previously caught.

**Aeon test — short-form-with-strong-iterated-control inverse anchoring
Amendment C (domain-of-applicability rule).** Produced the inverse result: the
carefully-iterated A→B→C control (Version C) decisively beat the
audience-blind Pitch B across substantive criteria including editor 3-second
read, ¶1 hook, ¶3 universalizability close, voice register / LLM-tic
avoidance, and the audience-load matrix (A wins 7 of 14 audiences; B wins 1
slightly). Pitch B passed Path B audit cleanly (a methodology win for the
discipline regardless of aesthetic outcome), but its substantive losses —
salutation hedge, manifest-scene diffusion of the airlock device, "stolen
hours" diction contradicting the no-villain example, three rule-of-three
LLM-tic exposures — outweighed its strengths against a strong iterated
control on short-form material. This drove Amendment C: the discipline's
payoff is concentrated on long-form publisher-facing material derived from
source prose with apparatus tripwire risk and without a strong iterated
control. Short-form material with a strong iterated control is a regime
where careful iteration may suffice.

**Net validation framing.** The Noema verdict showed the discipline produced
a submittable draft on the first try where the prior approach (Path-B-contaminated
Essay A) did not — net validation for the regime where domain-of-applicability
clauses (a)/(b)/(c) all fire. v2.0 codified the regime where the discipline
was the default and the regime where it was untested. v3.0 extends this
discipline with the additional stages described above; the v2.0 regime
specification remains live within Stage 3's five-pass architecture.

**v2.0 application targets (carry-forward).** Boston Review essay (long-form
derived from Ch 5; clauses a + b + c all fire — see
`tools/workstream-handoffs/boston-review-essay-handoff_2026-05-09.md`); Aeon
post-acceptance essay (long-form derived from Ch 7 + Ch 8 + Ch 1; clauses a
+ b + c all fire — see
`tools/workstream-handoffs/aeon-essay-post-acceptance-two-stage-handoff_2026-05-10.md`);
future long-form publisher-facing essays drafted without a strong iterated
control (Atlantic, Harper's, NYRB, Phenomenal World).

**v2.0 exclusions (carry-forward).** Short-form material with a strong
iterated control (the Aeon pitch Version C is the empirical reference — the
discipline did not beat careful iteration there). Treat short-form material
with no iterated control as untested; default to careful iteration and switch
to the discipline if iteration isn't converging. Internal scaffolding
documents (CLAUDE.md additions, session handoffs, source-material dumps in
`research/story-drafts/`) remain out of scope per the two-layer content
origination discipline (WP#10) — Stage 1 audience analysis is overhead for
internal-content work.
