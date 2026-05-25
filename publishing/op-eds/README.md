# Op-eds pipeline

Per-op-ed packages. Each `<slug>/` directory holds the op-ed text + canonical-facts inventory + cover letter (if applicable to venue).

## Active op-ed packages

| Directory | Op-ed | Target venues | State |
|---|---|---|---|
| [`mcdowell-county-true-cost/`](mcdowell-county-true-cost/) | McDowell County True Cost | TBD | Draft (2026-05-10) |
| [`norway-sovereign-wealth/`](norway-sovereign-wealth/) | Norway Sovereign Wealth | TBD | Draft (2026-05-10) |

## Per-op-ed directory layout

```
<slug>/
├── README.md
├── op-ed.md
├── canonical-facts.md       per-op-ed canonical-facts inventory (or symlink to _shared/canonical-facts/ if shared)
├── cover-letter.md          (if venue requires)
└── _archive/                historical drafts / variants
```

## Shared canonical-facts inventories (per Q5 ratification 2026-05-24)

Some op-eds share a canonical-facts inventory — preserve at `_shared/canonical-facts/` as a single source of truth rather than duplicating into each per-op-ed directory:

- [`_shared/canonical-facts/norway-mcdowell-inventory_2026-05-10.md`](_shared/canonical-facts/norway-mcdowell-inventory_2026-05-10.md) — shared between McDowell + Norway op-eds

## Status tags

Same convention as essays. See [`../essays/README.md`](../essays/README.md).

## Shared resources

- Cross-op-ed canonical facts: [`_shared/canonical-facts/`](_shared/canonical-facts/)
- Cross-op-ed templates: [`_shared/templates/`](_shared/templates/) (placeholder)
- Cross-op-ed pipeline: [`_pipeline/`](_pipeline/) (placeholder)
