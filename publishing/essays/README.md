# Essays pipeline

Per-essay submission packages. Each `<venue>-<short-title>/` directory holds the full submission package for one essay through its complete lifecycle (drafting → ratifying → submitting → archive after response).

## Active essay packages (as of 2026-05-25)

| Directory | Essay | Venue | State |
|---|---|---|---|
| [`noema-commons-bonds/`](noema-commons-bonds/) | *Commons Bonds* | Noema | RATIFIED-AWAITING-SUBMIT (Stage 5 ratified 2026-05-24) |
| [`boston-review-accountability-gap/`](boston-review-accountability-gap/) | *The Accountability Gap* | Boston Review | RATIFIED-AWAITING-SUBMIT (Stage 5 ratified 2026-05-23) |
| [`aeon-mask-of-abundance/`](aeon-mask-of-abundance/) | *The Mask of Abundance* | Aeon | Submission package scheduled 2026-05-31 |
| [`100-barrel/`](100-barrel/) | *$100 Barrel* | Phenomenal World (target) | RATIFIED-AWAITING-SUBMIT (Stage 5 ratified 2026-05-24) |
| [`atlantic-ideas-pricing-honestly/`](atlantic-ideas-pricing-honestly/) | *Pricing Honestly* | Atlantic Ideas | Stage 2 draft; Stage 3 cycle pending |
| [`berggruen-prize-2026/`](berggruen-prize-2026/) | (placeholder slug; offline AI-free drafting) | Berggruen Prize 2026 | Seed materials; hard deadline 2026-08-17 |

## Per-essay directory layout

**Updated 2026-05-28** with `rigor/` + `editor-iteration/` + `_archive/pre-submission/` subdirs per the per-essay-consolidation pattern ratified 2026-05-28. Per-essay rigor history co-locates with the essay package so editor-iteration loops (post-acceptance) can grep the full audit trail within one folder; also collapses the multi-location "what's the state of X?" lookup into one `ls`.

```
<venue>-<short-title>/
├── README.md                      submission state + checklist + cross-references
├── essay.md                       submission-ready essay text
├── cover-letter.md                submission cover note
├── stage-5-signoff.md             Stage 5 sign-off bookend
├── rigor/                         per-essay rigor history (NEW 2026-05-28)
│   ├── stage-1-brief.md           Stage 1 ready-to-draft brief (per-essay)
│   ├── pass-3-1-fact-check.md
│   ├── pass-3-2-voice-polish.md
│   ├── pass-3-3-audience-load.md
│   ├── pass-3-4-adversarial.md
│   ├── pass-3-5-developmental-edit.md
│   ├── stage-4-render-audit.md
│   ├── pre-pub-review-queue.md
│   └── light-refires/             post-Phase-C light re-fire records (if applicable)
├── editor-iteration/              post-acceptance editor-round artifacts (NEW 2026-05-28)
│   ├── round-1_<YYYY-MM-DD>/
│   │   ├── editor-questions.md    the letter / email from editor
│   │   ├── responses.md           author answers with rationale
│   │   ├── essay-revisions.md     what changed in essay.md + why (diff-style)
│   │   └── source-citations.md    new sourcing requests + responses
│   └── round-2_<YYYY-MM-DD>/
│       └── ...
└── _archive/                      historical drafts of THIS essay
    ├── pre-submission/            frozen essay state at moment of submit (NEW 2026-05-28)
    │   └── essay_pre-editor_<YYYY-MM-DD>.md
    ├── pre-pass1-drafts/
    ├── pre-stage-2-drafts/
    ├── withdrawn-<date>/          (if applicable)
    ├── session-handoffs/
    ├── planning/                  drafting plans; rewrite plans
    └── reference/                 venue PDFs (writing guidelines; model pitches)
```

### What goes in `rigor/` vs `tools/rigor-passes/`

After the per-essay rigor consolidation migration (queued; pilot session via spawned chip 2026-05-28):

- **`<venue>-<short-title>/rigor/`** — rigor-pass artifacts that pertain to ONE essay (the 5 passes, Stage 1 brief, Stage 4 render audit, Stage 5 pre-pub review queue, any light re-fires). Naming flattens from `commons_bonds_rigor_pass_<DATE>_<slug>_pass_3_1_v1.0.0.md` to `pass-3-1-fact-check.md` since the per-essay folder provides the disambiguation.
- **`tools/rigor-passes/`** — cross-essay or cross-chapter rigor artifacts that pertain to MULTIPLE essays / chapters (e.g., Wave 2 derivative-planning Stage 0 batch covering Ch 2 + Ch 3 + Ch 4 + Ch 8 in one file; cross-essay portfolio reviews; chapter-side rigor for `manuscript/chapters/Chapter__N_*` files).

The per-essay `README.md` links to any `tools/rigor-passes/` artifacts that include this essay (e.g., "Stage 0 verdict: see `tools/rigor-passes/wave-2-stage-0-batch_2026-05-24.md` §4.2 Candidate B").

### `editor-iteration/` workflow (post-acceptance)

When an editor accepts the essay and begins iteration, each round gets its own dated subdir under `editor-iteration/`. Pre-submission freeze (`_archive/pre-submission/essay_pre-editor_<DATE>.md`) captures the version sent to the editor so revisions are diff-able. Round-N response artifacts:

- `editor-questions.md` — the editor's letter / email verbatim (or anonymized if needed)
- `responses.md` — point-by-point answers; rationale for keeping or changing
- `essay-revisions.md` — what changed in essay.md, organized by editor question
- `source-citations.md` — sourcing answers; new citations added; supporting evidence

The `essay.md` itself is updated in place during each round (no `essay-v2.md`, `essay-v3.md` proliferation) — the rounds are the audit trail.

## Status tags (per Q3 + Q10 ratification 2026-05-24)

The directory name carries a status tag for at-a-glance state visibility:

- `<venue>-<short-title>/` — active (drafting / pre-submission / ratified-awaiting-submit)
- `<venue>-<short-title>_SUBMITTED-<date>/` — post-submission, awaiting editor response
- `<venue>-<short-title>_PLACED-<date>/` — accepted (could keep or move to `_archive/`)
- `_archive/<venue>-<short-title>_REJECTED-<date>/`
- `_archive/<venue>-<short-title>_WITHDRAWN-<date>/`

Rename directory on state change via `git mv`.

## Cross-references

- Rigor-pass artifacts: [`../tools/rigor-passes/`](../../tools/rigor-passes/) — centralized; naming convention disambiguates per-essay; cross-referenced from per-essay `README.md` by canonical path.
- Shared resources (AI disclosure paragraph; cover-letter template; personalization snippets): [`_shared/`](_shared/).
- Cross-essay strategy (cascade plan; decisions log; rights register; submission schedule): [`_pipeline/`](_pipeline/).

## Per-essay README.md contents

Each per-essay `README.md` carries:
- Essay title + venue + submission status
- Word count + ratification dates
- Cross-references to rigor-pass artifacts (Stage 1 brief; Pass 3.1 / 3.2 / 3.3 / 3.4 / 3.5; light re-fires; Stage 5 sign-off; cover letter)
- Submission checklist (Stage 4 render; consent-status checks; courtesy notifications; submission portal upload action)
- Named-subject inventory (per [`tools/memory/feedback_named_subject_consent.md`](../../tools/memory/feedback_named_subject_consent.md))
- Cross-essay coordination notes (cascade-plan position; rights-register status; soft-clip phrasing for cover letter)

## Pre-submission named-subject check

Before submitting any essay, execute the named-subject check gate against the canonical [`research/outreach/_pipeline/consent-tracker.md`](../../research/outreach/_pipeline/consent-tracker.md):

1. **Identify named-subject inventory** for the essay (per the essay's own README §"Named-subject inventory").
2. **For each subject, look up their row in the tracker** (§A living-pending-consent | §B deceased-courtesy-notify | §C public-record-on-record-speech | §D.1 interviewed | §D.2 published-work | §E deceased-public-record | §F author-family).
3. **Verify the subject's row shows OK-to-publish** per its class:
   - §A → signed consent landed (restore name) OR anonymization holds (submit anonymized).
   - §B → courtesy-notify executed OR 30-day good-faith effort completed.
   - §C → citation-accuracy notify packet fired pre-submission OR scheduled in submission window.
   - §D.1 → post-interview attribution-review materials sent AND written approval received for direct quotes + substantive paraphrases.
   - §D.2 → no per-submission check beyond standard fact-check (Pass 3.1 covers).
   - §E → no consent check; verify citation accuracy via Pass 3.1.
   - §F → author has confirmed naming for the essay.
4. **If any row shows a gate not satisfied** → the essay does NOT proceed to submission. Surface to author: complete the consent action OR anonymize the subject.
5. **Update the essay's submission checklist** with one line per named subject showing tracker-verified-OK-to-publish status, dated.

The check is a **gate**, not a guideline. See tracker §H for full discipline.
