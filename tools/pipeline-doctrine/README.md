# Pipeline doctrine

Canonical full doctrine for the Commons Bonds publishing pipeline (v1.0.0 ratified 2026-05-17, with Amendments A + B + C ratified 2026-05-18 / 19). Four files split by scope: an architecture-wide main doctrine plus three per-stage deep-dives. Promoted from `tools/` top-level into this subdir 2026-05-28 (S6 of the project-review structure-cleanup-followup session).

## When to read which

| File | Read when |
|---|---|
| [`commons_bonds_pipeline_doctrine_v1.0.0.md`](commons_bonds_pipeline_doctrine_v1.0.0.md) | Orienting to the full pipeline: six stages, change-cascade routing, two-class cascade (Amendment A), invariant-gate infrastructure, content-type sub-protocols, cross-chapter workstream lifecycle. **Start here** for any session that touches publisher-facing prose. |
| [`commons_bonds_pipeline_doctrine_stage_1_v1.0.0.md`](commons_bonds_pipeline_doctrine_stage_1_v1.0.0.md) | Drafting a Stage 1 ready-to-draft brief (chapter-side at `tools/stage-1-briefs/`, essay-side at `publishing/essays/<venue>/rigor/stage-1-brief.md`). Covers 1a invariant gate + 1b substantive brief + 1c cross-artifact coherence check + bookend academic-rigor + prose-quality sign-offs. |
| [`commons_bonds_pipeline_doctrine_stage_4_v1.0.0.md`](commons_bonds_pipeline_doctrine_stage_4_v1.0.0.md) | Stage 4 render + character-integrity audits. Canonical Docker container pipeline (apt-installed pandoc + xelatex + wkhtmltopdf on Ubuntu 24.04). Catches tofu-box glyph fallbacks, formula corruption, font-family naming drift, Chrome-vs-wkhtmltopdf rendering divergence. |
| [`commons_bonds_pipeline_doctrine_stage_5_v1.0.0.md`](commons_bonds_pipeline_doctrine_stage_5_v1.0.0.md) | Stage 5 bookend sign-off + pre-publication review queue artifact. The mandatory hand-off deliverable that goes to publisher / agent / editor with the manuscript-submission package. Symmetric pair to the Stage 1 ratification gate. |

## How they relate

The main doctrine (`v1.0.0`) is architecture-wide and load-bearing for anyone executing or modifying the pipeline. The three stage-specific files are deep-dives that the main doctrine cross-references — read them when working *on* that stage's artifacts, not as preflight for every session.

Stages 0 + 2 + 3 do not have dedicated subdoctrines (yet); their treatment lives in the main doctrine plus the v3.1 audience-aware drafting discipline memory entry ([`../memory/feedback_audience_aware_drafting_discipline.md`](../memory/feedback_audience_aware_drafting_discipline.md)) plus the Stage 3 rigor-audit template ([`../drafting-templates/stage-3-three-pass-rigor-audit.md`](../drafting-templates/stage-3-three-pass-rigor-audit.md)).

## Ratification audit trail

- 2026-05-17: v1.0.0 main doctrine ratified; per-stage Stage 1 + Stage 4 + Stage 5 deep-dives ratified.
- 2026-05-18: Amendment A (two-class cascade — automatic-on-edit vs explicit-gate).
- 2026-05-18: Amendment B (Pass 3.5 developmental-edit codified; four passes → five passes).
- 2026-05-19: Amendment C (interactive ratification protocol for prose-modifying passes).
- 2026-05-28: Files relocated from `tools/` top-level into `tools/pipeline-doctrine/` subdir; cross-references updated repo-wide.

## Cross-references

- Memory entry summary (always-loaded in CLAUDE.md): [`../memory/feedback_audience_aware_drafting_discipline.md`](../memory/feedback_audience_aware_drafting_discipline.md)
- Stage 3 audit template: [`../drafting-templates/stage-3-three-pass-rigor-audit.md`](../drafting-templates/stage-3-three-pass-rigor-audit.md)
- Audience pressure-test construction: [`../drafting-templates/audience-pressure-test-construction.md`](../drafting-templates/audience-pressure-test-construction.md)
- Invariant-gate registries: [`../quality-gates/scaffolding-patterns.yaml`](../quality-gates/scaffolding-patterns.yaml) + [`../quality-gates/regressed-patterns.yaml`](../quality-gates/regressed-patterns.yaml)
- Invariant-scan implementation: [`../scripts/check-corpus-invariants.sh`](../scripts/check-corpus-invariants.sh)
- Per-essay rigor consolidation pattern (2026-05-28): [`../../publishing/essays/README.md`](../../publishing/essays/README.md)
