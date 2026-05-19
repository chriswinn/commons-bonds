# Memory Update Spec — `feedback_audience_aware_drafting_discipline.md` v2.0 → v3.0 → **v3.1.0** (Amendment B Pass 3.5)

**Date drafted:** 2026-05-17 (v3.0 base); 2026-05-18 Amendment A (selective stage-firing) + Amendment B (Pass 3.5 developmental-edit ratification) added.
**Status:** v3.0 base PROPOSED + author-applied 2026-05-17; Amendment A + Amendment B BOTH ratified 2026-05-18. **Memory entry version: v3.1.0.**

**Amendment A in one line:** the v3.0 cascade is now two-class — automatic-on-edit (Pass 3.1 + Pass 3.2 + Stage 1c-light; fires on every prose edit) vs explicit-gate (Pass 3.3 + Pass 3.4 + Stage 4 + Stage 5; fires only on author trigger at pre-external-review send + pre-publication + venue-change). Rationale: token-economy — heavy passes only fire when value justifies the cost.

**Amendment B in one line:** Stage 3 extends from four-pass to **five-pass** with the addition of **Pass 3.5 developmental-edit** at whole-chapter scale. Pass 3.5 catches emotional-arc continuity + scene-anchor density + sensory-detail restoration + voice-flow continuity + cumulative-LLM-cadence residue + reader-engagement at analytical pivots — all of which per-paragraph Pass 3.2 + per-character Pass 3.3/3.4 cannot catch by design. Remediation polarity is RESTORATION, not cutting (Pass 3.2 cuts; Pass 3.5 restores; the polarity-difference is the methodological-clarity argument for separation). Pass 3.5 is explicit-gate per Amendment A — fires per-chapter after Pass 3.1-3.4 ratify-and-apply; pre-publication; not on every prose edit. Empirically grounded by Ch 1 developmental-edit review (`tools/rigor-passes/ch1_developmental_edit_review_2026-05-18.md`); cross-chapter empirical grounding via the developmental-edit workstream continues for Ch 2 → Ch 10 + AuthorsNote.

**Amendment C in one line (ratified 2026-05-19):** prose-modifying passes (Pass 3.1 / Pass 3.2 / Pass 3.5) + Phase C application sessions follow an **interactive ratification protocol** — each finding gets Options + Recommendation + Reasoning, walked through interactively in a follow-up session, with author dispositioning each before chapter-source changes apply. Two-session workflow: (1) discovery session produces PROPOSED artifact + auto-merges to main; (2) interactive ratification + application session walks through findings + applies ratified spot-fixes to chapter source in the same combined session. Replaces the prior three-step pattern (discovery + external author-review + Phase C application).

**Apply Amendments A + B + C to local memory:** v3.1.0 memory entry should append "Amendment A" + "Amendment B" + "Amendment C" blocks from `tools/commons_bonds_pipeline_doctrine_v1.0.0.md` §3.1-3.4 + §3.6 + §3.7 respectively, OR replace the v3.0-original cascade section with the new two-class five-pass interactive-ratification framework. Memory file remains a scan-friendly summary; canonical doctrine carries the full architecture.

---
**Origin:** Pipeline-revision workstream (handoff at [`tools/workstream-handoffs/pipeline-revision-handoff_2026-05-17.md`](../workstream-handoffs/pipeline-revision-handoff_2026-05-17.md)).
**Versioning approach:** hybrid per ratified decision #8 — this memory entry stays scan-friendly (summary + pointer); the full doctrine lives in `tools/commons_bonds_pipeline_doctrine_v1.0.0.md`.
**Applies to local memory file:** `/Users/c17n/.claude/projects/-Users-c17n-commons-bonds/memory/feedback_audience_aware_drafting_discipline.md`

---

## §0. Context for this spec

The author's memory file is on the local Claude Code machine, not in the repo. This spec captures the proposed v3.0 update for the author to apply locally after this session's doctrine cluster lands on `main`. Once applied, future sessions reading the memory entry will see the v3.0 summary + the pointer to the canonical doctrine artifact in the repo.

---

## §1. Proposed v3.0 memory-entry content (replaces v2.0 Amendment B entry verbatim)

```markdown
# feedback_audience_aware_drafting_discipline (v3.0)

**Date:** 2026-05-17
**Supersedes:** v2.0 Amendment B (2026-05-10 + 2026-05-13)
**Canonical full doctrine:** `tools/commons_bonds_pipeline_doctrine_v1.0.0.md` in
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
- **Stage 3:** four-pass rigor audit.
  - **3.1:** fact-check (per v2.0).
  - **3.2:** voice-polish (per v2.0).
  - **3.3:** audience-load acceptance (target audiences; INCLUDE / EXCLUDE
    verdict per character).
  - **3.4:** audience-load robustness (adversarial / detractor characters;
    thread-pull synthesis verdict; NEW in v3.0).
- **Stage 4:** render + character-integrity audit (NEW in v3.0).
- **Stage 5:** academic-rigor + prose-quality sign-off bookend + pre-publication
  review queue artifact (NEW in v3.0).

Per-prompt serial cadence enforced (each pass fires in its own prompt; author
ratifies + spot-fixes apply before next pass fires).

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

- Full doctrine: `tools/commons_bonds_pipeline_doctrine_v1.0.0.md`
- Stage 1: `tools/commons_bonds_pipeline_doctrine_stage_1_v1.0.0.md`
- Stage 4: `tools/commons_bonds_pipeline_doctrine_stage_4_v1.0.0.md`
- Stage 5: `tools/commons_bonds_pipeline_doctrine_stage_5_v1.0.0.md`
- Stage 3 template (revised): `tools/drafting-templates/stage-3-three-pass-rigor-audit.md`
- Audience pressure-test construction (revised): `tools/drafting-templates/audience-pressure-test-construction.md`
```

---

## §2. Application instructions for author

1. Open the local memory file: `/Users/c17n/.claude/projects/-Users-c17n-commons-bonds/memory/feedback_audience_aware_drafting_discipline.md`.
2. Replace the v2.0 Amendment B content with the §1 proposed v3.0 content above.
3. Keep any historical-record sections (the empirical anchors should be retained as audit-trail).
4. Save + commit (the memory file is on the local Claude Code machine; commit-tracking depends on the local memory-versioning setup if any).
5. Future sessions reading the memory entry will see the v3.0 summary + the pointer to the canonical doctrine artifact in the repo.

---

## §3. Rollback procedure

If v3.0 needs to be rolled back to v2.0 Amendment B:
1. The v2.0 Amendment B content is preserved in this repo at the git commit prior to this spec landing (use `git log` to find).
2. Restore the v2.0 Amendment B content to the local memory file.
3. The doctrine cluster artifacts in the repo stay in place (they don't conflict with v2.0 Amendment B at the memory-entry level; they describe the architecture v2.0 Amendment B implied but didn't fully codify).

---

*End of memory update spec.*
