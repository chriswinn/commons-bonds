# Drafting-Session Templates

**Date drafted:** 2026-05-11
**Discipline reference:** v2.0 audience-aware drafting discipline (ratified 2026-05-10) at `/Users/c17n/.claude/projects/-Users-c17n-commons-bonds/memory/feedback_audience_aware_drafting_discipline.md`

**Purpose.** Reusable session-paste templates for any drafting task in the Commons Bonds project. Each template is a starting point: fill in the `[BRACKET PLACEHOLDERS]`, paste into a fresh session, the session executes.

Templates are organized by the v2.0 discipline's stages. Not every drafting task needs all stages — see the decision tree below.

---

## Files in this directory

| File | When to use |
|---|---|
| `stage-0-publishing-strategy-rigor-test.md` | Substantial publisher-facing derivative work that hasn't been ratified yet. Decides go/no-go + sequencing against book-success criteria BEFORE any drafting begins. |
| `stage-1-audience-aware-structure-pass.md` | Pre-draft brief building: audience pressure-test + canonical-facts inventory + structural decisions + voice register + carry-forward inventory. **Required for any publisher-facing drafting.** |
| `stage-2-audience-blind-flow-draft.md` | Fresh-session audience-blind drafting from the Stage 1 brief. **Required for any publisher-facing prose >~500w** that derives from chapter/source prose (Path B preemptive policy). |
| `stage-3-three-pass-rigor-audit.md` | Post-draft rigor — five distinct passes per v3.1 Amendment B (2026-05-18): fact-check + voice-polish + audience-load acceptance + audience-load robustness + developmental-edit. **Required for any publisher-facing prose >~500w** before submission. (Filename preserved across v2.0/v3.0/v3.1 evolution for cross-reference stability.) |
| `audience-pressure-test-construction.md` | Guide for building the 20-character pressure-test set adapted per venue. Reference from Stage 1 templates. |

---

## Decision tree — which stages to fire

```
What are you drafting?
│
├── Body paragraph / section inside an existing manuscript chapter (<~500w)
│   → Skip Stage 0. Use a "mini Stage 1" (10-min audience-load
│     + canonical-facts check in your head). Stage 2 + Stage 3 can be
│     bundled into a single session per the flagship-terms-defense
│     workstream model.
│   → Examples: flagship-term name-defense paragraphs (CIT / ARR /
│     Externality Tail / Abundance Masking insertions 2026-05-11).
│
├── New short-form publisher-facing piece (~700–1,200w op-ed, blurb,
│   short essay)
│   → Skip Stage 0 if the piece is already in cascade plan + the venue
│     is already cleared. Run Stage 0 if it's a new venue or a
│     potentially-thunder-stealing reveal.
│   → Run Stage 1 + Stage 2 + Stage 3 (all three are load-bearing
│     even at op-ed length).
│   → Example: op-ed pipeline drafts (Norway + McDowell, 2026-05-10).
│
├── New long-form publisher-facing essay (~3,000–5,000w magazine essay)
│   → Run Stage 0 if (a) it's a new venue OR (b) it would reveal
│     >15% of book apparatus OR (c) it could code Commons Bonds as
│     politically partisan.
│   → Always run Stage 1 + Stage 2 + Stage 3.
│   → Stage 2 MUST be a fresh session (audience-blind discipline).
│   → Example: $100 Barrel essay for Phenomenal World (workstream #16,
│     2026-05-11).
│
├── Book-proposal section (e.g., §00 overview, §01 market-and-audience,
│   §04 marketing plan)
│   → Skip Stage 0 (book proposal is already in pipeline; no go/no-go
│     question).
│   → Run a modified Stage 1 (audience = literary agents + acquiring
│     editors; structural conventions = trade-publishing-norm).
│   → Stage 2 can be bundled with Stage 1 if the section is
│     non-derivative (no chapter source to contaminate against).
│   → Stage 3 audience-load pass only; fact-check + voice-polish can
│     be inline.
│
├── Manuscript revision / polish (existing chapter prose)
│   → Skip Stage 0 + Stage 1 + Stage 2 entirely. This is a Stage-3-
│     style five-pass audit applied to existing prose.
│   → Use Stage 3 template only; specify "audit-existing-prose"
│     mode.
│
├── Internal-scaffolding artifact (handoff doc, audit doc, decisions
│   log entry, glossary entry)
│   → Skip all stages. Use the internal-scaffolding register; no
│     audience-load rigor needed.
│
└── Email / correspondence / cover letter / pitch (short, personal)
    → Skip all stages. Direct drafting with brief audience check at
      the top of the message ("am I writing to an agent? editor?
      interview subject?").
```

---

## How to scale up or down

The v2.0 discipline is the **maximum-rigor** path. For lower-stakes work, scale down:

| Stakes | Stage 0 | Stage 1 | Stage 2 | Stage 3 |
|---|---|---|---|---|
| Major publisher-facing essay (new venue, potential book-impact) | ✓ Full | ✓ Full | ✓ Full fresh-session | ✓ Three distinct passes |
| Pipeline-already-cleared publisher-facing essay | Skip | ✓ Full | ✓ Full fresh-session | ✓ Three distinct passes |
| Op-ed / short publisher-facing piece | Skip | ✓ Light | ✓ Fresh-session OK | ✓ Three passes possibly bundled |
| In-book defense paragraph (~300w) | Skip | ✓ Inline mini-brief | ✓ Bundled with Stage 1 | ✓ Single audience-load pass |
| Book-proposal section | Skip | ✓ Modified for trade-publishing audience | ✓ Bundlable | ✓ Light audience-load |
| Revision of existing prose | Skip | Skip | Skip | ✓ Apply audit-existing-prose mode |
| Internal scaffolding | Skip | Skip | Skip | Skip |

---

## Picking the right rigor tests

Rigor tests beyond the v3.1 five-pass Stage 3:

| Test | When to apply |
|---|---|
| **Path B audit** | When draft derives from chapter prose. Test for verbatim sentences + structural close-paraphrase. Reference: `research/audits/cross-chapter-path-b-audit_2026-05-11.md`. |
| **Named-subject consent** | When draft uses real names of living subjects in publisher-facing prose. Reference: `feedback_named_subject_consent.md`. |
| **Framework-positioning** | When draft engages framework apparatus terms (CS, RCV, Bond, CIT, ARR, etc.). Check FPD v1.0.0 alignment. Reference: `alignment/commons_bonds_framework_positioning_disciplines_v1.0.0.md`. |
| **Apparatus register** | When draft uses framework symbols / Greek letters / acronyms. Trade-press body prose should be apparatus-light per `tools/rigor-passes/commons_bonds_rigor_pass_2026-05-11_apparatus_register_decision_v1.0.0.md`. |
| **Cross-chapter consistency** | When draft references named cases (Libby, McDowell, Mondragon, Norway, Chesapeake) or recurring statistics. Reference: `tools/audits/cross-chapter-consistency-inventory_2026-05-11.md`. |
| **Layman-lookup discipline** | When draft cross-references the Tech Appendix or theorem numbers. Format: "[Named Concept] (Technical Appendix §X.Y, Theorem X.Y)". Reference: workstream #15 outputs. |
| **Substance-drives-length** | Always. No padding to hit target; no cutting to fit. Reference: `feedback_substance_drives_length.md`. |
| **Verify-stale-memory-claims** | Always. Verify counts, dates, file paths, statuses against current ground truth before asserting. Reference: `feedback_verify_stale_memory_claims.md`. |
| **Two-layer content origination** | Always. Classify draft as internal-scaffolding vs. external-publisher-facing before drafting begins. Reference: `feedback_two_layer_content_discipline.md`. |

---

## Audience picking — quick reference

**Default audience pressure-test set** for publisher-facing work: 20 characters across three tiers (per `commons_bonds_rigor_pass_2026-05-11_why_bonds_paragraph_include_vs_exclude_audience_load_v1.0.0.md`).

**Venue-specific adaptations:**

| Venue | Audience adjustment from default |
|---|---|
| Aeon | Add literary-philosophical reader; weight thought-experiment toleration; lighter on policy-mechanism specificity |
| Noema | Three-register weave (memoir + history/theory + reportage); add internationalist scope; named-sources-with-cited-public-record |
| Boston Review | Institutional / policy-centrist; add policy-economics reader |
| Phenomenal World | Heterodox-econ / political-economy academic-adjacent; add center-right reader for non-partisan-framing test |
| Project Syndicate / Bloomberg | Financial / policy short-form; add international-reader |
| NYT / WaPo Opinion | General educated reader; lighter on jargon |
| Atlantic Ideas | Name-recognition prestige; expects established bylines |
| Real-World Economics Review | Heterodox-econ formalization; methods-note register |
| Trade-publisher acquiring editor | Add commercial-arc reader; emphasize bookstore-buyer hook |
| Literary agent | Add comp-titles-evaluator reader |

See `audience-pressure-test-construction.md` for the full construction guide.

---

## Giving context for what to draft

Every Stage 1 brief should specify:

1. **What** — the artifact (essay / paragraph / pitch / op-ed / etc.)
2. **Where** — the destination (specific venue / chapter / file path)
3. **Why** — strategic purpose (which book-success criterion does this serve?)
4. **Who** — audience (specific venue's editorial brain + reader)
5. **Length** — target band + ceiling (substance drives length within bounds)
6. **Voice** — register (memoir / literary-philosophical / op-ed / methods-note / academic)
7. **Source material** — what the draft draws on (chapter X, interview transcript, source essay, etc.)
8. **Constraints** — anything specific (no apparatus / no Path B / specific consent requirements / specific framing conditions)
9. **Locked elements** — what cannot change (title / opening line / closing paragraph / specific named subjects)

Stage 0 templates ask higher-level versions of these against book-success criteria.

---

## Canonical examples in the project

For each stage, recent worked examples:

| Stage | Worked example |
|---|---|
| Stage 0 | `tools/rigor-passes/commons_bonds_rigor_pass_2026-05-11_100_barrel_essay_q1_go_no_go_v1.0.0.md` |
| Stage 1 | `tools/rigor-passes/commons_bonds_rigor_pass_2026-05-10_noema_essay_pre_draft_audience_structure_v1.0.0.md` |
| Stage 1 (short-form) | `tools/rigor-passes/commons_bonds_rigor_pass_2026-05-10_aeon_pitch_pre_draft_audience_structure_v1.0.0.md` |
| Stage 2 | `manuscript/essay/Noema/noema-essay-fresh-session-draft_2026-05-10.md` |
| Stage 3 (verdict) | `tools/rigor-passes/commons_bonds_rigor_pass_2026-05-10_noema_stage3_comparison_v1.0.0.md` |
| Stage 3 (audience-load) | `tools/rigor-passes/commons_bonds_rigor_pass_2026-05-11_why_bonds_paragraph_include_vs_exclude_audience_load_v1.0.0.md` |
| Bundled mini-pipeline (in-book paragraph) | `tools/drafts/why-bonds-paragraph_2026-05-11_v1.0.0.md` + `tools/rigor-passes/commons_bonds_rigor_pass_2026-05-11_why_bonds_paragraph_include_vs_exclude_audience_load_v1.0.0.md` |

Mirror these when adapting templates.

---

## Maintenance

This directory grows as drafting patterns evolve. When a new pattern emerges from a workstream (e.g., the post-interview correspondence template-set from the interview-attribution v2 codification), add it here.

Updates to the v2.0 discipline (memory file `feedback_audience_aware_drafting_discipline.md`) should propagate here within a session.

---

*End of README.*
