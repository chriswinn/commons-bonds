# Structure cleanup S8 — underused-subdir decide-or-archive sweep (2026-05-28)

**Workstream:** structure-cleanup-followup S8 (project review recommendation ratified 2026-05-28).
**Session:** `claude/structure-cleanup-followup-260528-*` (bundled with S1 + S6 + S7 + S9 in one session).
**Disposition:** decisions executed; this file is the record.

## Subdirs reviewed

| Subdir | File count | Decision | Rationale |
|---|---|---|---|
| `tools/audits/` | 2 | KEEP + document better | Strategic-snapshot inventory class distinct from `rigor-passes/` audit trail + live `quality-gates/` records. Contents: long-lived standing-reference cross-chapter-consistency inventory + one-shot 2026-05-01 pre-submission-readiness audit. The class is real even at low file count. Updated `tools/README.md` description. |
| `tools/writing-process/` | 3 (incl README) | KEEP + document better | Portable / lift-and-reuse process docs (rigor-pipeline-overview, audience-character-roster) designed to be extractable to standalone references. Distinct from `drafting-templates/` (project-specific) and `pipeline-doctrine/` (project doctrine). Class is intentional. Updated `tools/README.md` description. |
| `tools/drafts/` | 9 | ARCHIVE | Defense paragraphs from 2026-05-11 (flagship-terms-defense-sweep workstream). All ratified content has been merged into chapters (per `git log` "Ch 2 — insert ratified Cost Severance umbrella-mechanism defense paragraph" + similar). Drafts are historical work artifacts. Moved to `archive/_OneDayMaybe/tools-drafts-defense-paragraphs-2026-05-11/`. |
| `tools/routines/` | 1 | KEEP + document better | RATIFIED 2026-05-09 routines spec for cron-scheduled remote agents (Routines 1', 2 refined, 3', 4' on unified 6:30am ET cadence). Live operational doc; low file count reflects spec being one-document; not a stale class. Updated `tools/README.md` description. |
| `tools/memory-updates/` | 1 | KEEP | Active staging class for memory-discipline updates. Low file count reflects "stuff happens to land here briefly before flowing into `tools/memory/`" workflow, not a stale class. Already documented in `tools/README.md`; expanded description to call out keep-decision rationale. |
| `publishing/essays/_pipeline/weekly-audits/` | 1 | ARCHIVE | Single 2026-04-28 weekly pre-submission readiness audit; no subsequent weekly audits ran (cadence didn't take hold; superseded by ad-hoc cross-essay portfolio reviews). Moved to `archive/_OneDayMaybe/essays-pipeline-weekly-audits-2026-04-28/`. |

## Archive moves

```
git mv tools/drafts \
       archive/_OneDayMaybe/tools-drafts-defense-paragraphs-2026-05-11

git mv publishing/essays/_pipeline/weekly-audits \
       archive/_OneDayMaybe/essays-pipeline-weekly-audits-2026-04-28
```

Both moves preserve `git log --follow` history per the existing archive pattern.

## What did NOT get archived (and why)

The S8 prompt suggested considering archive for some of these subdirs. Decisions to keep are above. Net pattern: **low file count alone is not a stale-class signal**; the relevant question is whether the class is intentional + still receiving content. `tools/memory-updates/` has one file because staging is meant to be transient (files flow OUT to `tools/memory/` quickly). `tools/routines/` has one file because the spec consolidated into one document. `tools/audits/` has two files but both are still load-bearing (one is a standing reference; one is the canonical pre-submission readiness snapshot referenced from downstream artifacts).

## Verification

- `tools/README.md` entries updated for the keep-decided subdirs to clarify the class purpose at a glance.
- Corpus-invariant scan: scaffolding-patterns.yaml unchanged; archive paths are not in scan scope.
- No downstream references to break — `tools/drafts/*` and `publishing/essays/_pipeline/weekly-audits/*` had no incoming hyperlinks from current canonical docs (the defense paragraphs' content is what was load-bearing, and that landed in chapters via the merge commits 2026-05-12 / 13 / 19 / 20 / 21).

## Status

**EXECUTED 2026-05-28.** Two `git mv` operations performed; `tools/README.md` updated; this disposition log committed. No follow-up required.
