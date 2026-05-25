# Literary agent outreach

Per-agent directories. Mirrors the [`research/outreach/subjects/`](../../research/outreach/subjects/) pattern (8 active source-subject directories at last count).

**Target scale: 50-100 per-agent directories at full agent-outreach wave.**

## Current state (as of 2026-05-25)

- **Shared infrastructure:** templates, personalization snippets, post-Darity warm-intro templates → [`_shared/`](_shared/)
- **Pipeline strategy:** query-tracker, agent-targets → [`_pipeline/`](_pipeline/)
- **Per-agent directories:** none yet — agent-search PM session will populate these

## Per-agent directory layout

```
<agent-slug>/
├── README.md              state + status + notes
├── background-brief.md    agent research (deal-list; client-list; interests; mutual connections)
├── personalization.md     per-agent personalization sentences
├── query-letter.md        personalized query
├── correspondence/        email log (sent + received drafts)
└── _archive/              prior versions; declined / closed correspondence
```

## Agent directory naming (per Q4 ratification 2026-05-24)

**Flat `<agent-slug>/` (not two-level `<agency>/<agent>/`).** Most agencies have one relevant agent per book; cross-agent comparisons easier from a flat list. Agency name lives in per-agent `README.md` not in directory hierarchy.

## Status tags (per Q3 + Q10 ratification 2026-05-24)

- `<agent-slug>/` — active / pre-query (research phase)
- `<agent-slug>_QUERIED-<date>/` — query sent; awaiting response
- `<agent-slug>_REQUESTED-<date>/` — partial / full request received
- `<agent-slug>_OFFERED-<date>/` — representation offered
- `<agent-slug>_SIGNED-<date>/` — signed (rare; archive after signing)
- `_archive/<agent-slug>_PASSED-<date>/` — pass response received

## Shared resources

- [`_shared/templates/query-letter-template.md`](_shared/templates/query-letter-template.md)
- [`_shared/personalization-snippets.md`](_shared/personalization-snippets.md)
- [`_shared/post-darity-warm-intro-templates_2026-05-10.md`](_shared/post-darity-warm-intro-templates_2026-05-10.md)

## Pipeline strategy

- [`_pipeline/query-tracker.md`](_pipeline/query-tracker.md)
- [`_pipeline/targets.md`](_pipeline/targets.md) — agent target list (target: 50-100 entries at full scale; currently ~1)

## Cross-references

- Source-subject outreach (parallel inbound-outreach pipeline): [`../../research/outreach/subjects/`](../../research/outreach/subjects/)
- Author platform (bio variants; soft clips): [`../book-proposal/03_author-platform.md`](../book-proposal/03_author-platform.md)
- Essay placements that strengthen agent pitches: [`../essays/_pipeline/`](../essays/_pipeline/)
