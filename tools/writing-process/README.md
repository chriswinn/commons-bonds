# `tools/writing-process/` — Portable Writing & Audit Process Documents

**Date created:** 2026-05-19
**Status:** Living folder. These documents capture writing and audit disciplines developed during the *Commons Bonds* book project that are **portable** — designed to be lift-and-reused across other projects or extracted to their own standalone repositories with light editing.

---

## Why this folder exists

The *Commons Bonds* book project surfaced several writing / auditing disciplines that are general enough to be useful far beyond this one manuscript:

- A six-stage rigor pipeline for long-form publisher-facing writing.
- A 40-character audience-pressure-test set for predicting how target and adversarial audiences will read an artifact.
- (Future) An interview / sales-call / meeting-prep process derived from the same audience-aware discipline, adapted for live conversation rather than written artifacts.

These disciplines were developed iteratively, with empirical validation through parallel A/B drafting experiments, and they've become substantively load-bearing for the book's quality. They could be useful to other writers, researchers, journalists, and analysts working on long-form publisher-facing material — particularly when AI-assisted drafting is in the workflow.

Rather than leave these disciplines buried in project-internal canonical doctrine docs (which are necessarily project-specific with commit hashes, internal cross-references, and amendment trails), this folder holds the **portable overviews** — written to be readable on their own, generalized where project-specific examples didn't add value, and structured so they could be extracted to their own repositories when the time comes.

---

## What's in this folder

| Document | Purpose | Status |
|---|---|---|
| [`rigor-pipeline-overview_v1.0.0.md`](rigor-pipeline-overview_v1.0.0.md) | Six-stage rigor pipeline for long-form publisher-facing writing. Stages, sub-steps, invariant gates, change-cascade routing, token-economy table, adoption guidance. | v1.0.0 — current |
| [`audience-character-roster_v1.0.0.md`](audience-character-roster_v1.0.0.md) | The 40-character pressure-test set (30 acceptance + 10 adversarial) with tier structure, per-character descriptions, construction discipline for adapting to other projects. | v1.0.0 — current |
| `interview-prep-process_v1.0.0.md` | Interview / sales-call / meeting-prep process derived from the audience-aware discipline. | **Planned** — author flagged 2026-05-19 as a future extraction candidate |

---

## Relationship to project-internal canonical docs

The portable overviews here **derive from** project-internal canonical artifacts that live elsewhere in `tools/`. Those project-internal docs remain canonical for project-internal use; the overviews here are the externalized, generalized versions designed for portability.

| Portable overview (here) | Project-internal canonical (elsewhere) |
|---|---|
| `rigor-pipeline-overview_v1.0.0.md` | `tools/pipeline-doctrine/commons_bonds_pipeline_doctrine_v1.0.0.md` + Stage 1 / 4 / 5 sub-docs at `tools/pipeline-doctrine/commons_bonds_pipeline_doctrine_stage_{1,4,5}_v1.0.0.md` |
| `audience-character-roster_v1.0.0.md` | `tools/rigor-passes/commons_bonds_ch1_stage_3_pass_3_audience_load_REAUDIT_2026-05-17_PROPOSED.md` (lived 40-character full-rigor example) + `tools/drafting-templates/audience-pressure-test-construction.md` (construction discipline) |
| `interview-prep-process_v1.0.0.md` (planned) | `research/outreach/subjects/<subject>/` prep stacks; `alignment/commons_bonds_framework_positioning_disciplines_v1.0.0.md` |

---

## Future extraction path

These documents are written so they can be extracted to standalone repositories with relatively light editing — primarily removing project-specific cross-references and adjusting the license / acknowledgments. Plausible standalone repositories:

- **`rigor-pipeline`** — the six-stage pipeline as a writing/auditing process reference. Could include the YAML registries + invariant-gate shell scripts + CI workflow as a reusable infrastructure layer.
- **`audience-character-roster`** — the 40-character set + construction discipline as a pressure-testing reference.
- **`interview-prep-process`** — the interview / sales-call / meeting-prep process as a meeting-preparation discipline.

Extraction timing is at the author's discretion as these processes mature and their portability is further demonstrated through use beyond the *Commons Bonds* project.

---

## License

License terms TBD by the author when any document is extracted to a standalone repository. Within the *Commons Bonds* project, these documents are working artifacts under the project's overall arrangement.

---

*End of folder README. Update as new documents land or extraction paths formalize.*
