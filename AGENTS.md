# AGENTS.md — Internal collaborator orientation

**Layer:** internal scaffolding (per Working Principle #10).
**Audience:** author + AI collaborator + future-Claude.

This document is the canonical internal-scaffolding orientation for the Commons Bonds project — current canonical state, working discipline, repository structure, session workflow, and operating rules. Per WP#10, this content lives at the internal layer; the publisher-facing landing page is [`README.md`](README.md).

---

## Current canonical state

| Component | Status | File |
|---|---|---|
| Rigor protocol | **v2.2.0** canonical — Pre-Submission Peer Review Suite (11 modules) + Path Comparison Mode + 6 informational goals (personal/ethical satisfaction + family wellbeing + career safety + time/capacity preservation + movement utility + financial sustainability — produce per-path findings without driving primary recommendations) | [`tools/commons_bonds_rigor_protocol_v2.2.0.md`](tools/commons_bonds_rigor_protocol_v2.2.0.md) |
| Working principles | **v1.0.0 canonical — 10 principles**; WP#4 REFINED 2026-04-30 (tiered retirement-trace policy + canonical retirement-archive per Insight #59); WP#9 NEW 2026-04-29 (worktree-isolation git workflow); WP#10 NEW 2026-04-30 (two-layer content origination discipline per Insight #9 generalization) | [`alignment/commons_bonds_working_principles_v1.0.0.md`](alignment/commons_bonds_working_principles_v1.0.0.md) |
| Vocabulary strategy | **v1.0.1 canonical** — §3.1 Tier disambiguation note added 2026-04-30 (Insight #63 quick-fix). §6 + §13 light-trace migration to retirement archive applied 2026-04-30 (α-thread Phase α.1); §7 remains queued. | [`alignment/commons_bonds_vocabulary_strategy_v1.0.1.md`](alignment/commons_bonds_vocabulary_strategy_v1.0.1.md) |
| Terms index | **v1.0.0 canonical 2026-04-30** (α-thread Phase α.1 batched commit) — current-state registry; summary-level retirement traces per refined WP#4; full traces in retirement-archive index. UNBLOCKS Phase α.2 Tech Appendix v2.0.0 + Phase α.3 Glossary v4. | [`core/terms/terms_index.md`](core/terms/terms_index.md) |
| Decision-time application (internal) | **v1.0.0 canonical** — internal-scaffolding artifact preserving Pattern 1/2/3 literature analysis + two-layer framing rationale + worked-example seed material; per Insight #9 verdict (b) + WP#10. | [`core/methodology/decision_time_application_internal_v1.0.0.md`](core/methodology/decision_time_application_internal_v1.0.0.md) |
| Retirement archive | **canonical retirement-trace index** per refined WP#4 (Insight #59) — 16 vocabulary retirements + 2 methodology retirements + 3 file/artifact retirements + cross-references to ratifying rigor passes. | [`archive/retirements/index.md`](archive/retirements/index.md) |
| Open insights tracker | **6 OPEN** as of post-Thread-γ-commit: #13, #21, #36, #37, #39, #63. Closed 2026-04-30: #9 (Pattern 2 verdict + WP#10 generalization), #14 (Norway/Accountability Bond, by reference), #61 (README sweep + AGENTS.md split), #62 (archive hybrid ratified). Next free insight number: **#64**. | [`alignment/commons_bonds_open_insights_v1.0.0.md`](alignment/commons_bonds_open_insights_v1.0.0.md) |
| Routines | **v1.0.0 draft** — 4 sentinel-style scheduled-agent prompts: Routine 1 (daily terminology-regression sentinel) + Routine 2 (weekly pre-submission readiness audit) + Routine 3 (rigor pass status tracker) + Routine 4 (open insights status sync). | [`tools/routines/proposed_routines_v1.0.0.md`](tools/routines/proposed_routines_v1.0.0.md) |
| Abundance dimensions | **v1.3.0 — Path F reframing applied.** 10 abundances framed as organizational scaffolding over variables CIT has surfaced across 18 cases — illustrative, not ontological. Queued for absorption into Tech Appendix v2.0.0 §C.2 during Phase 3 rebuild; directory will archive at that point per Insight #55 hygiene pass. | [`core/dimensions/commons_bonds_abundance_dimensions_v1_3_0.md`](core/dimensions/commons_bonds_abundance_dimensions_v1_3_0.md) |
| Eight-tier decomposition | **RETIRED 2026-04-24** per tier-reframing rigor pass §11.2. Path F + Four Gates discipline supersedes. Archived 2026-04-30 per Insight #55 hygiene pass. | [`archive/decomposition/eight-tier-v10.html`](archive/decomposition/eight-tier-v10.html) |
| Chapter audit | **v1.0.6 canonical — Path F reframing applied** | [`core/chapters/commons_bonds_chapter_audit_v1.0.6.md`](core/chapters/commons_bonds_chapter_audit_v1.0.6.md) |
| Case-study audit | **v1.0.6 canonical — Path F reframing applied** | [`core/case-studies/commons_bonds_case_study_audit_v1.0.6.md`](core/case-studies/commons_bonds_case_study_audit_v1.0.6.md) |
| Technical appendix | **v1.0.0 canonical — Path F Section L (Four Gates discipline) + Section M (formula generalization) integrated.** Phase 3 v2.0.0 rebuild queued (~20–30 hrs; batches all Phase 2 + Group 1 ratifications: theorem restructures E.1a+E.1b / E.2 / E.3 / E.4 / E.5; §L methodological footnotes for Cost Severance + Foreclosure Bond + Intergenerational Option Value; notation discipline α→ξ + τ→u + C→𝒞; bibliography expansion; absorption of `core/dimensions/` content into §C.2). v0.0.3, v0.0.4, v0.0.5 superseded; supplements in `core/technical-appendix/archive/`. | [`core/technical-appendix/TechnicalAppendix_v1.0.0.html`](core/technical-appendix/TechnicalAppendix_v1.0.0.html) |
| Glossary | **v3 canonical** — Phase A3 framework structural-restructure ratifications integrated. Phase 4 v4 rebuild queued (~3–5 hrs; derives from terms_index v1.0.0+ per S1 schema; absorbs Phase 2 + Group 1 ratifications). | [`core/glossary/commons_bonds_updated_glossary_v3.html`](core/glossary/commons_bonds_updated_glossary_v3.html) |
| Book One scope | v1.0.3 canonical | [`tools/commons_bonds_book_scope_v1_0_3.md`](tools/commons_bonds_book_scope_v1_0_3.md) |
| Guiding constraints | v1.0.0 canonical | [`tools/commons_bonds_guiding_constraints_v1_0_0.md`](tools/commons_bonds_guiding_constraints_v1_0_0.md) |
| Framework-scope decision | **Path F selected** — variables-not-dimensions reframing. PCR v1.1.0 §8 confirmed 2026-04-24. Extreme-rigor pass PASSES-WITH-CONDITIONS; Phase A2 Conditions 1–4 materially implemented 2026-04-24. Rigor-pass rerun available per §11.7. | [`tools/pre-submission-reviews/commons_bonds_pcr_2026-04-23_v1.1.0.md`](tools/pre-submission-reviews/commons_bonds_pcr_2026-04-23_v1.1.0.md) · [`tools/rigor-passes/commons_bonds_rigor_pass_2026-04-24_path_f_variable_addability_v1.0.0.md`](tools/rigor-passes/commons_bonds_rigor_pass_2026-04-24_path_f_variable_addability_v1.0.0.md) |
| Tier reframing decision | **Reframing claim FAILS SC-1 on §5.3 duplication check (2026-04-24); dissolution ratified.** Variables replace tiers at framework-specification level. Conditions 1–4 APPROVED (2026-04-24); Condition 5 (Tier 6 / E overlap) deferred. | [`tools/rigor-passes/commons_bonds_rigor_pass_2026-04-24_tier_reframing_v1.0.0.md`](tools/rigor-passes/commons_bonds_rigor_pass_2026-04-24_tier_reframing_v1.0.0.md) |
| Macro-grouping decision | **Option A ratified (2026-04-24) — macro-groupings REJECTED at every level.** Pure variable enumeration with narrative pacing is the book's structural approach. | [`tools/rigor-passes/commons_bonds_rigor_pass_2026-04-24_macro_grouping_v1.0.0.md`](tools/rigor-passes/commons_bonds_rigor_pass_2026-04-24_macro_grouping_v1.0.0.md) |
| Current handoff | **v1.49.0** parallel-execution plan (4 threads + coordination discipline) layered on **v1.48.0** state-snapshot | [`v1.49.0`](alignment/sessions/commons-bonds-session-handoff-2026-04-30_v1.49.0.md) · [`v1.48.0`](alignment/sessions/commons-bonds-session-handoff-2026-04-30_v1.48.0.md) |

## Repository structure

- **[`tools/`](tools/)** — canonical working methodology (session upload set). See [`tools/README.md`](tools/README.md) for upload-set directory. Contains rigor protocol, book scope, guiding constraints, `routines/` (sentinel discipline draft), `rigor-passes/` (historical audit trail), `pre-submission-reviews/` (PSR + PCR records), `archive/` of superseded methodology versions.
- **[`manuscript/`](manuscript/)** — book content:
  - `chapters/` — 8 drafts + 10 guidance docs + dedication + author's note (`chapters/archive/` holds Ch 6 supplementary drafts pending structural placement per Insight #21)
  - `essay/Noema/` — submitted essay (do not touch)
  - `essay/berggruen/` — competition requires AI-free content (do not touch)
- **[`core/`](core/)** — canonical framework content:
  - `dimensions/` (v1.3.0; queued for Phase 3 absorption)
  - `glossary/` (HTML; v3 canonical, v4 rebuild queued)
  - `technical-appendix/` (math-heavy HTML; v1.0.0 canonical, v2.0.0 rebuild queued)
  - `terms/` (terms_index — single-source-of-truth pipeline for glossary derivation)
  - `methodology/` (internal-scaffolding methodology artifacts per WP#10; e.g. `decision_time_application_internal_v1.0.0.md`)
  - `chapters/` (chapter audit + supporting analysis)
  - `case-studies/` (per Insight #55: 8-tier `decomposition/` archived to [`archive/decomposition/`](archive/decomposition/))
- **[`alignment/`](alignment/)** — project-meta:
  - Top-level scaffolding files: working principles (v1.0.0), vocabulary strategy (v1.0.1), open insights tracker, personal-stories candidates
  - `decisions/` — ratified decisions + pending-review items (e.g. April 19 per-section captures, alternate 8-tier retired for tier-decision review)
  - `patches/pending-framework-review/` — C2/C3/C9 patches + 2 layer-era triage analyses, gated on tier-structure decision
  - `patches/archive/` — applied patches
  - `sessions/` — current handoff + `archive/` of prior handoffs
- **[`research/`](research/)** — `case-studies/` (17 files — see [README](research/case-studies/README.md)) + `literature/` (bibliography + economic-theory-reference)
- **[`publishing/`](publishing/)** — `essay-drafts/` (Noema/Berggruen source prose)
- **[`archive/`](archive/)** — deferred + retired material (see archive convention below):
  - `retirements/index.md` — canonical retirement-trace index per refined WP#4 (Insight #59)
  - `decomposition/` — retired 8-tier decomposition (per Insight #55 hygiene pass)
  - `_OneDayMaybe/book-two/` and `_OneDayMaybe/book-three/` — dumping grounds for Book Two / Book Three
  - `_OneDayMaybe/satellite-essays/` — framework-adjacent essays
  - `_OneDayMaybe/two-book-strategic-analysis.html` — strategic rationale for the books split

## Archive convention (Insight #62 ratified 2026-04-30)

The project uses a **hybrid archive structure**:

- **Top-level [`archive/`](archive/)** — cross-domain retirement material + multi-book seed material:
  - `archive/retirements/index.md` — single canonical retirement-trace index (refined WP#4)
  - `archive/decomposition/` — retired methodologies surfaced from any domain
  - `archive/_OneDayMaybe/` — Book 2 / Book 3 / satellite-essay seed material
- **Per-domain `<domain>/archive/`** — domain-specific historical predecessors kept adjacent to live work:
  - [`core/technical-appendix/archive/`](core/technical-appendix/archive/) — superseded TA versions + supplements
  - [`manuscript/chapters/archive/`](manuscript/chapters/archive/) — Ch 6 supplementary drafts pending integration
  - [`tools/archive/`](tools/archive/) — superseded methodology versions

**Rationale (per Insight #62 verdict (c)):** the actual cross-domain audit-trail need is solved by the canonical retirement-trace index. Per-domain archives encode origin context next to live work, which WP#10's "internal scaffolding can be rich" license endorses. Full consolidation (option (a)) was rejected for low marginal navigability gain vs. ~10–20 path-update cost + loss of domain-context proximity.

**Single search location for retirement provenance:** [`archive/retirements/index.md`](archive/retirements/index.md).

## Working discipline

10 working principles (v1.0.0 canonical). Selected:

- **WP#1** Vocabulary parsimony
- **WP#3** Two-path rigor — allocation symmetry + shield absence
- **WP#4** Retirement-trace discipline — REFINED 2026-04-30 (tiered policy by document type + canonical retirement-archive at [`archive/retirements/index.md`](archive/retirements/index.md))
- **WP#7** Earning-its-place + scaffolding-vs-book-worthy
- **WP#8** Publisher-facing artifacts scrubbed of scaffolding
- **WP#9** NEW 2026-04-29 — worktree-isolation git workflow with session-end fast-forward to `main`
- **WP#10** NEW 2026-04-30 — Two-layer content origination discipline (internal-scaffolding vs external-publisher-facing)

Full list + rationales: [`alignment/commons_bonds_working_principles_v1.0.0.md`](alignment/commons_bonds_working_principles_v1.0.0.md).

### WP#10 layer classification

| Layer | What lives here | Discipline |
|---|---|---|
| **Internal scaffolding** | `.claude/` · `tools/` · `core/methodology/` · `alignment/` · `research/` · `archive/` · this `AGENTS.md` | Rich; preserves methodology notes, worked examples, research-grade depth, literature audits, audit trail, decision-time-application drafts, Book 2 / Book 3 seed material, framework-supporting material that doesn't need publisher-facing exposure |
| **External publisher-facing** | `manuscript/chapters/*` · `core/glossary/*` · `core/technical-appendix/*` · `manuscript/essay/*` · `README.md` | Disciplined per WP#8 (scrubbed of audit-trail content) + Pattern 2 demonstration (threaded through cases rather than codified in dedicated how-to / methodology sections — the *Doughnut Economics* / *Mission Economy* / *Mine!* model) |

**Default behavior when uncertain:** classify new content as internal scaffolding. Easier to promote internal material to external (when it earns the slot via Pattern 2 demonstration) than to scrub publisher-facing artifacts of accumulated scaffolding.

## What's queued

- **Phase 3 — Tech Appendix v2.0.0 rebuild** (~20–30 hrs) — batches all Phase 2 + Group 1 ratifications (theorem restructures E.1a+E.1b / E.2 / E.3 / E.4 / E.5; §L methodological footnotes; notation discipline α→ξ + τ→u + C→𝒞; bibliography expansion; absorption of `core/dimensions/` content into §C.2). Currently unblocked.
- **Phase 4 — Glossary v4 rebuild** (~3–5 hrs) — derives from terms_index v1.0.0+ per S1 schema. Sequenced after Phase 3.
- **Drafting** — Ch 1 + Ch 3 conversational drafting (Insight #36, after Insight #37 separation pass); Ch 6 structural placement of supplementary §6.5–§6.10 passages (Insight #21).
- **Pre-publication external review** (Insight #39) — academic-rigor pass/fail gate; triggers entire-book citations audit + Tier word-level collision focused rigor pass (Insight #63) when the manuscript reaches submission-ready state.

Detailed priority order in [`v1.48.0`](alignment/sessions/commons-bonds-session-handoff-2026-04-30_v1.48.0.md) §5; parallel-execution plan in [`v1.49.0`](alignment/sessions/commons-bonds-session-handoff-2026-04-30_v1.49.0.md) §3.

## Session workflow

When starting a new Claude session:

1. Grab the current session handoff from `alignment/sessions/` (top level).
2. Grab the session-upload set from `tools/` per [`tools/README.md`](tools/README.md).
3. Include `tools/rigor-passes/` current pass record.
4. Paste the copy-paste snippet (at the top of the current handoff) into the first message.

For parallel-session work (multiple concurrent threads): see [`v1.49.0`](alignment/sessions/commons-bonds-session-handoff-2026-04-30_v1.49.0.md) §1 for thread-scoped copy-paste blocks (α architecture / β drafting / γ hygiene / δ discussion).

## Operating rules

- Never touch `manuscript/essay/Noema/` or `manuscript/essay/berggruen/` — Noema submitted; Berggruen requires AI-free content.
- Math files stay `.html` (Ch 6, Technical Appendix, glossary). The eight-tier decomposition is RETIRED 2026-04-24 + archived 2026-04-30 (Insight #55); replaced by Cᵢ admission via Four Gates per Path F.
- Privacy: scrub personal financial specifics from external-facing outputs.
- `.DS_Store`, `.claude/`, `.chriswinn/` are in `.gitignore` — never commit.
- Worktree-isolation git workflow per WP#9: harness-issued feature branches during a session; ratified-chunk fast-forward to `main` via `git push origin HEAD:main` after each closed-ratified insight or atomic patch.
- Retirement traces per refined WP#4 (Insight #59): tiered policy by document type; canonical retirement audit-trail at [`archive/retirements/index.md`](archive/retirements/index.md).
- Content origination per WP#10: classify at origination as internal-scaffolding or external-publisher-facing; default to internal when uncertain.

## Key conceptual foundations (internal vocabulary)

- **Two-path rigor** — allocation symmetry + shield absence. Both paths must confirm.
- **Merger gate + primitiveness gate** — applied to any new or renamed dimension.
- **Commons Inversion Test (CIT)** — epistemic core; scarcity-grounded cost claims survive counterfactual inversion (CAI / CCI). Operates as a thought-experiment discrimination gate within the Four Gates admission apparatus (Path F per Insight #21 + tier-reframing). Renamed from AIT; replaces 8-tier decomposition discipline.
- **Earning-its-place + Scaffolding-vs-book-worthy** — standing book-integrity tests (Tests 28 + 29) applied at every rigor depth.
- **Canonical cases are dimension-inherent** — not incidental illustrations.
- **Single-dimension cost severance** — one-dimension cases are full instances; framework doesn't require multi-dimension co-occurrence.

## Ten dimensions (locked)

Habitability · Spatial · Temporal · Institutional · Kindred · Ecosystem · Political · Cohesion · Epistemic · Autonomy.
