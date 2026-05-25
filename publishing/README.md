# Publishing pipeline

Three outbound publishing pipelines, plus the book proposal:

- [`essays/`](essays/) — derivative essays going to magazine venues (Noema, Boston Review, Aeon, Atlantic Ideas, $100 Barrel / Phenomenal World, Berggruen, etc.). Per-essay submission packages.
- [`op-eds/`](op-eds/) — op-eds going to news venues. Per-op-ed packages.
- [`agents/`](agents/) — literary agent outreach. Per-agent directories.
- [`book-proposal/`](book-proposal/) — the book proposal itself.

Each outbound pipeline follows the same per-target-directory pattern (working model: [`research/outreach/subjects/`](../research/outreach/subjects/)):

```
<pipeline>/
├── _shared/         cross-target reusable resources (templates; snippets)
├── _pipeline/       cross-target strategy (tracker; targets; planning)
├── _protocols/      shared discipline (where applicable)
├── _archive/        retired / completed / rejected targets
└── <target-slug>/   per-target directory (essay; op-ed; agent)
```

Per-target directories carry a `README.md` with state + status + checklist + cross-references to rigor-pass artifacts (which stay centralized at [`tools/rigor-passes/`](../tools/rigor-passes/) and are referenced by canonical path; see follow-up rigor-pass reorg session, deferred 2026-05-24).

See per-pipeline READMEs for area-specific conventions:
- [`essays/README.md`](essays/README.md)
- [`op-eds/README.md`](op-eds/README.md)
- [`agents/README.md`](agents/README.md)

## Status-tag convention (per Publishing-Reorg Session 1 Q10 ratification 2026-05-24)

Directory-level state visibility via name-suffix:

- `<target-slug>/` — active / drafting / pre-submission
- `<target-slug>_SUBMITTED-<date>/` — post-submission, awaiting response
- `<target-slug>_PLACED-<date>/` — accepted / signed
- `_archive/<target-slug>_REJECTED-<date>/`
- `_archive/<target-slug>_WITHDRAWN-<date>/`
- `_archive/<target-slug>_PASSED-<date>/` (agents only)

Rename directory on state change via `git mv`. README.md state-field tracks fine-grained sub-state notes; directory-name suffix is the primary signal.

## Reorg origin

This architecture was ratified 2026-05-24 in [`tools/workstream-handoffs/publishing-reorg-session1-audit_2026-05-24.md`](../tools/workstream-handoffs/publishing-reorg-session1-audit_2026-05-24.md) and applied via Phase C application 2026-05-24 / 2026-05-25 (Session 2).

The architecture extends the proven per-target-directory pattern from [`research/outreach/subjects/`](../research/outreach/subjects/) (8 source-subject directories) to three outbound publishing pipelines anticipating ~10 essays/op-eds + 50-100 literary agent outreaches at scale.

## Deferred follow-up

- **Rigor-pass artifact relocation** (deferred 2026-05-24 per author direction): currently all rigor-pass artifacts remain centralized at [`tools/rigor-passes/`](../tools/rigor-passes/). A follow-up reorg session will revisit whether per-essay rigor-pass artifacts should move into per-essay directories.
