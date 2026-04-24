# Commons Bonds

*A framework for honest accounting of intergenerational commons-extraction costs*

**Author:** Chris Winn
**Status:** Active framework development — session v1.33.0 (2026-04-23)

---

## What this is

Commons Bonds is a book-in-progress developing a formal economic and philosophical framework for pricing the intergenerational costs of commons extraction. The framework introduces two core concepts:

- **Cost Severance** — the structural mechanism by which extraction separates value capture from cost bearing
- **Residual Commons Value (RCV)** — the mathematical framework for pricing previously unpriced intergenerational costs

The framework applies across extraction domains — coal mining, oil drilling, fisheries, rare-earth processing, financial instruments, pharmaceutical distribution, and (as a universality check) off-Earth mining — demonstrating that the same structural mechanism operates in all of them.

## Success criterion

> If, ten-plus years from now, a labor lawyer uses "severed cost" in a brief or in open court and the judge does not need it explained — and the author whose name is on the book never knows this happened — the book has succeeded.

Vocabulary used by people solving real problems. Not royalties, not prizes, not revolution.

## Three-book structure

- **Book One — *Commons Bonds*** (active, 2026–2027 target) — framework naming, non-partisan. Publication cascade: Noema (primary) → Boston Review (fallback) → The Atlantic Ideas → further venues. Parallel Berggruen Prize track, 2026-08-17 deadline (AI-free writing).
- **Book Two — *The Subsidy Economy*** (notes-only, 2029+ target) — applied / policy / advocacy. Requires coauthorship, institutional affiliation, and publisher legal backing. Seed material in [`archive/_OneDayMaybe/book-two/`](archive/_OneDayMaybe/book-two/).
- **Book Three — *Pricing the Final Frontier*** (notes-only) — off-Earth extraction framework extension. Seed material in [`archive/_OneDayMaybe/book-three/`](archive/_OneDayMaybe/book-three/).

## Current canonical state

| Component | Status | File |
|---|---|---|
| Rigor protocol | **v2.2.0** canonical — Pre-Submission Peer Review Suite (11 modules) + Path Comparison Mode + **6 informational goals** (personal/ethical satisfaction + family wellbeing + career safety + time/capacity preservation + movement utility + financial sustainability — produce per-path findings without driving primary recommendations) | [`tools/commons_bonds_rigor_protocol_v2.2.0.md`](tools/commons_bonds_rigor_protocol_v2.2.0.md) |
| Abundance dimensions | **v1.3.0 canonical — Path F reframing applied.** 10 abundances framed as variables AIT has discovered across 18 cases — illustrative, not ontological. Naming-cohort preserved. | [`core/dimensions/commons_bonds_abundance_dimensions_v1_3_0.md`](core/dimensions/commons_bonds_abundance_dimensions_v1_3_0.md) |
| Eight-tier decomposition | v10 canonical + **Path F reframing preamble added 2026-04-24.** Eight tiers framed as one way to organize per-case accounting (not universal structure). Phase A2 methodology work will specify the four-gate discipline formally. | [`core/decomposition/eight-tier-v10.html`](core/decomposition/eight-tier-v10.html) |
| Chapter audit | **v1.0.6 canonical — Path F reframing applied** | [`core/chapters/commons_bonds_chapter_audit_v1.0.6.md`](core/chapters/commons_bonds_chapter_audit_v1.0.6.md) |
| Case-study audit | **v1.0.6 canonical — Path F reframing applied** | [`core/case-studies/commons_bonds_case_study_audit_v1.0.6.md`](core/case-studies/commons_bonds_case_study_audit_v1.0.6.md) |
| Technical appendix | v0.0.3 canonical; **Phase A2 Task 10 bumps to v0.0.4** with four-gate discipline + formula generalization | [`core/technical-appendix/TechnicalAppendix_v0.0.3.html`](core/technical-appendix/TechnicalAppendix_v0.0.3.html) |
| Glossary | v2 canonical | [`core/glossary/commons_bonds_updated_glossary_v2.html`](core/glossary/commons_bonds_updated_glossary_v2.html) |
| Book One scope | v1.0.3 canonical | [`tools/commons_bonds_book_scope_v1_0_3.md`](tools/commons_bonds_book_scope_v1_0_3.md) |
| Guiding constraints | v1.0.0 canonical | [`tools/commons_bonds_guiding_constraints_v1_0_0.md`](tools/commons_bonds_guiding_constraints_v1_0_0.md) |
| Framework-scope decision | **Path F selected** — variables-not-dimensions reframing. PCR v1.1.0 §8 confirmed 2026-04-24. Extreme-rigor pass PASSES-WITH-CONDITIONS. | [`tools/pre-submission-reviews/commons_bonds_pcr_2026-04-23_v1.1.0.md`](tools/pre-submission-reviews/commons_bonds_pcr_2026-04-23_v1.1.0.md) · [`tools/rigor-passes/commons_bonds_rigor_pass_2026-04-24_path_f_variable_addability_v1.0.0.md`](tools/rigor-passes/commons_bonds_rigor_pass_2026-04-24_path_f_variable_addability_v1.0.0.md) |
| Current handoff | **v1.38.0** | [`alignment/sessions/commons-bonds-session-handoff-2026-04-24_v1.38.0.html`](alignment/sessions/commons-bonds-session-handoff-2026-04-24_v1.38.0.html) |

**10 locked dimensions:** Habitability · Spatial · Temporal · Institutional · Kindred · Ecosystem · Political · Cohesion · Epistemic · Autonomy

## Repository structure

- **[`tools/`](tools/)** — canonical working methodology (session upload set). See [`tools/README.md`](tools/README.md) for upload-set directory. Contains rigor protocol, book scope, guiding constraints, `rigor-passes/` record, `archive/` of superseded methodology versions.
- **[`manuscript/`](manuscript/)** — book content:
  - `chapters/` — 8 drafts + 10 guidance docs + dedication + author's note
  - `essay/Noema/` — submitted essay (do not touch)
  - `essay/berggruen/` — competition requires AI-free content (do not touch)
- **[`core/`](core/)** — canonical framework content: `dimensions/`, `decomposition/`, `glossary/`, `technical-appendix/` (math-heavy HTML)
- **[`alignment/`](alignment/)** — project-meta:
  - `decisions/` — ratified decisions + pending-review items (e.g. April 19 per-section captures, alternate 8-tier retired for tier-decision review)
  - `patches/pending-framework-review/` — C2/C3/C9 patches + 2 layer-era triage analyses, gated on tier-structure decision
  - `patches/archive/` — applied patches
  - `sessions/` — current handoff + `archive/` of prior handoffs
- **[`research/`](research/)** — `case-studies/` (17 files — see [README](research/case-studies/README.md)) + `literature/` (bibliography + economic-theory-reference)
- **[`publishing/`](publishing/)** — `essay-drafts/` (Noema/Berggruen source prose)
- **[`archive/`](archive/)** — deferred material:
  - `_OneDayMaybe/book-two/` and `book-three/` — dumping grounds for Book Two / Book Three
  - `_OneDayMaybe/satellite-essays/` — framework-adjacent essays
  - `_OneDayMaybe/two-book-strategic-analysis.html` — strategic rationale for the books split

## Session workflow

When starting a new Claude session:

1. Grab the current session handoff from `alignment/sessions/` (top level).
2. Grab the session-upload set from `tools/` per [`tools/README.md`](tools/README.md).
3. Include `tools/rigor-passes/` current pass record.
4. Paste the copy-paste snippet (at the top of the current handoff) into the first message.

## Key conceptual foundations

- **Two-path rigor** — allocation symmetry + shield absence. Both paths must confirm.
- **Merger gate + primitiveness gate** — applied to any new or renamed dimension.
- **Abundance Inversion Test (AIT)** — epistemic core; scarcity-grounded claims survive abundance stripping. Dimensions are organizational scaffolding around AIT.
- **Earning-its-place + Scaffolding-vs-book-worthy** — standing book-integrity tests (Tests 28 + 29) applied at every rigor depth.
- **Canonical cases are dimension-inherent** — not incidental illustrations.
- **Single-dimension cost severance** — one-dimension cases are full instances; framework doesn't require multi-dimension co-occurrence.

## Hard rules

- Never touch `manuscript/essay/Noema/` or `manuscript/essay/berggruen/` — Noema submitted; Berggruen requires AI-free content.
- Math files stay `.html` (Ch. 6, Technical Appendix, eight-tier decomposition, glossary).
- Privacy: scrub personal financial specifics from external-facing outputs.
- `.DS_Store`, `.claude/`, `.chriswinn/` are in `.gitignore` — never commit.
- Direct-to-main git workflow with smaller focused commits; push each to origin after commit.

## Migration note

Repository migrated from Google Drive to GitHub on April 19–20, 2026.
