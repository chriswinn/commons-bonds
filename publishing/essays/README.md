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

```
<venue>-<short-title>/
├── README.md           submission state + checklist + cross-references
├── essay.md            submission-ready essay text
├── cover-letter.md     submission cover note (Decision #13 deliverable)
├── stage-5-signoff.md  Stage 5 sign-off bookend
└── _archive/           historical drafts of THIS essay
    ├── pre-pass1-drafts/
    ├── pre-stage-2-drafts/
    ├── withdrawn-<date>/   (if applicable)
    ├── session-handoffs/
    ├── planning/           drafting plans; rewrite plans
    └── reference/          venue PDFs (writing guidelines; model pitches)
```

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
