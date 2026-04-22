# Commons Bonds

*A framework for honest accounting of intergenerational commons-extraction costs*

**Author:** Chris Winn
**Status:** Framework development active — session v1.29.0 (2026-04-22)

---

## What this is

Commons Bonds is a book-in-progress developing a formal economic and philosophical framework for pricing the intergenerational costs of commons extraction. The framework introduces two core concepts:

- **Cost Severance** — the structural mechanism by which extraction separates value capture from cost bearing
- **Residual Commons Value (RCV)** — the mathematical framework for pricing previously unpriced intergenerational costs

The framework applies across extraction domains — coal mining, oil drilling, fisheries, rare-earth processing, financial instruments, pharmaceutical distribution, and (as a universality check) off-Earth mining — demonstrating that the same structural mechanism operates in all of them.

## Success criterion

If, thirteen or more years from now, a labor lawyer uses "severed cost" in a brief or in open court and the judge does not need it explained — and the author whose name is on the book never knows this happened — the book has succeeded. Vocabulary used by people solving real problems; not royalties, not prizes, not revolution.

## Three-book structure

- **Book One — *Commons Bonds*** (active, 2026–2027 target) — framework naming, non-partisan. Publication cascade: Noema (primary) → Boston Review (fallback) → The Atlantic Ideas → further venues. Parallel Berggruen Prize track, 2026-08-17 deadline (AI-free writing).
- **Book Two — *The Subsidy Economy*** (notes-only, 2029+ target) — applied / policy / advocacy. Requires coauthorship, institutional affiliation, and publisher legal backing. Seed material lives in `archive/_One Day Maybe/`.
- **Book Three — *Pricing the Final Frontier*** (notes-only) — off-Earth extraction framework extension. Post-Book-Two.

Strategic reasoning and content-assignment rules: [`alignment/decisions/sociology-paper-to-book-transition.md`](alignment/decisions/sociology-paper-to-book-transition.md) §4.

## Current canonical state (as of session v1.29.0)

| Component | Status | File |
|---|---|---|
| Rigor protocol | v1.2.1 canonical | [`tools/commons_bonds_rigor_protocol_v1.2.2.md`](tools/commons_bonds_rigor_protocol_v1.2.2.md) |
| Abundance dimensions | 10 canonical; Priority-1 naming cohort complete (Habitability, Kindred, Ecosystem locked 2026-04-22) | [`tools/commons_bonds_abundance_dimensions_v1_1_0.md`](tools/commons_bonds_abundance_dimensions_v1_1_0.md) |
| Book One scope | v1.0.3 canonical | [`tools/commons_bonds_book_scope_v1_0_3.md`](tools/commons_bonds_book_scope_v1_0_3.md) |
| Guiding constraints | v1.0.0 canonical | [`tools/commons_bonds_guiding_constraints_v1_0_0.md`](tools/commons_bonds_guiding_constraints_v1_0_0.md) |
| Current handoff | v1.29.0 | [`alignment/sessions/commons-bonds-session-handoff-2026-04-22_v1_29_0.html`](alignment/sessions/commons-bonds-session-handoff-2026-04-22_v1_29_0.html) |

**Naming cohort progress:** Habitability (was Atmospheric) and Ecosystem (was Ecological) locked. Demographic, Geographic, Informational, Agency, Cohesion naming pending Priority-2 cohort.

## Repository structure

- **`tools/`** — canonical working methodology (session upload set). See [`tools/README.md`](tools/README.md) for upload-set directory.
- **`manuscript/`** — book content:
  - `chapters/` — 8 drafts + 10 guidance docs
  - `essay/Noema/` — submitted essay (do not touch)
  - `essay/Berggruen Institute - Essay/` — competition requires AI-free content (do not touch)
- **`core/`** — canonical framework content (eight-tier decomposition, glossary, technical appendix — math-heavy HTML)
- **`alignment/`** — project-meta:
  - `decisions/` — ratified architectural decisions, housekeeping reviews, project-state docs
  - `patches/` — canonical architectural patches (c2, c3, c4, c5, c9, tier-2a)
  - `sessions/` — current session handoff + archived handoffs
- **`research/`** — scholarly apparatus:
  - `case-studies/` — 9 standalone case studies (see [README](research/case-studies/README.md))
  - `literature/` — consolidated bibliography + economic-theory reference
- **`publishing/`** — cascade strategy and path documents
- **`archive/`** — superseded material preserved for lineage:
  - `_One Day Maybe/` — Book Two + Book Three seed material
  - `Consider Including/` — staging-to-be-routed (reduced per workstream 10 plan)
  - `workstreams-old/` — 17 archived workstream planning docs
  - `prototypes/` — early framework prototypes

## Session workflow (for Claude sessions)

When starting a new Claude session:

1. Grab the current session handoff from `alignment/sessions/` (top level).
2. Grab the session-upload set from `tools/` per [`tools/README.md`](tools/README.md).
3. Include `tools/rigor-passes/` current pass record.
4. Paste the session-start snippet (at the top of the current handoff) into the first message.

## Key conceptual foundations

- **Two-path rigor** — allocation symmetry + shield absence. Both paths must confirm.
- **Merger gate + primitiveness gate** — applied to any new or renamed dimension.
- **Abundance Inversion Test (AIT)** — epistemic core; scarcity-grounded claims survive abundance stripping.
- **Canonical cases are dimension-inherent** — not incidental illustrations.
- **Single-dimension cost severance** — one-dimension cases are full instances; framework doesn't require multi-dimension co-occurrence.
- **Availability-absence is severity-marker** — not a primitive dimension (v1.28.0 finding).

## Hard rules

- Never touch `/Noema/` or `/Berggruen Institute - Essay/` Drive folders.
- Math files stay `.html` (Ch. 6, Technical Appendix, eight-tier decomposition, glossary).
- Privacy: scrub personal financial specifics from external-facing outputs.
- `.DS_Store`, `.claude/`, `.chriswinn/` are in `.gitignore` — never commit.
- Drive is read-only on the Drive side (no renames, no writes from Claude).

## Migration note

Repository migrated from Google Drive to GitHub on April 19–20, 2026. Migration-era planning documents (workflow guides, repository-structure proposals, GitHub-Issues-workflow designs) are archived in [`alignment/decisions/archive/`](alignment/decisions/archive/).

## Related

This project was preceded by a sociology-paper precursor thread that seeded its intellectual foundations. That thread's content, publishability assessment, and structured todo list is consolidated in [`alignment/decisions/sociology-paper-to-book-transition.md`](alignment/decisions/sociology-paper-to-book-transition.md). The consolidated bibliography across the project lives at [`research/literature/bibliography.md`](research/literature/bibliography.md).
