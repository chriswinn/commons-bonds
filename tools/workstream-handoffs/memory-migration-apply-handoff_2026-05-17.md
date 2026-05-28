# Memory migration application — Handoff 2026-05-17

**Status:** READY TO FIRE. All decisions ratified 2026-05-17 in the originating audit session (branch `claude/memory-consolidation-audit-0056b8`).
**Origin:** Audit proposal at [`tools/memory-migration-proposal_2026-05-17.md`](../memory-migration-proposal_2026-05-17.md) §7 ratification record.
**Branch:** `claude/memory-migration-apply-<harness-id>` from current `origin/main` per `tools/workstream-handoffs/README.md` branch discipline.
**Merge discipline:** Pre-ratified change set per audit proposal §7 ratifications. Per CLAUDE.md merge-to-main default, this session is "similar work where the author has explicitly approved the change set ahead of the session" — qualifies for autonomous fast-forward merge to `main` at session close.

---

## Mission

Apply the 14-file memory migration ratified per audit proposal §7. Single atomic commit; touches `tools/memory/` (new directory + 15 files + README + ARCHIVE log), `CLAUDE.md`, `alignment/commons_bonds_open_insights_v1.0.0.md` (insight #67 flag), and local `~/.claude/projects/-Users-c17n-commons-bonds/memory/MEMORY.md` (annotations only; not in repo).

## Read in order

1. This handoff.
2. [`tools/memory-migration-proposal_2026-05-17.md`](../memory-migration-proposal_2026-05-17.md) — §2 per-file table + §3 proposed CLAUDE.md block + §4 ARCHIVE log entry + §7 ratified decisions.
3. `CLAUDE.md` current state (target of step 5 edit).
4. `~/.claude/projects/-Users-c17n-commons-bonds/memory/MEMORY.md` + each MIGRATE-verdict source file (per §2 table).

## Ratified decisions (re-quote at session opening)

Per audit proposal §7:

1. Migration table approved (14 MIGRATE + 1 KEEP-LOCAL + 1 ARCHIVE + 1 EDGE-as-MIGRATE).
2. Selective `@import`: three always-load files (audience-aware + named-subject + verify-stale); rest discoverable via `tools/memory/README.md`.
3. `feedback_git_workflow.md` MIGRATE (operational nuance stays in `tools/memory/`).
4. `project_authors_grandfather_nasa_inventor.md` KEEP-LOCAL (SENSITIVE).
5. Canonical-pointer headers applied uniformly per v3.0 pattern.
6. Local `MEMORY.md` annotated (option c); structure unchanged.
7. No initial-migration specs under `tools/memory-updates/`.
8. Multi-machine-sync WP amendment deferred; flagged as insight #67.

---

## Branch setup

```
git fetch origin
git checkout -b claude/memory-migration-apply-<harness-id> origin/main
```

---

## Ordered task list (8 steps)

### Step 1 — Create `tools/memory/` and migrate 15 files

Source path: `~/.claude/projects/-Users-c17n-commons-bonds/memory/`
Target path: `tools/memory/`

Copy verbatim (preserving YAML frontmatter; canonical-pointer header insertion happens in step 2):

**14 standard MIGRATE files:**
- `feedback_audience_aware_drafting_discipline.md`
- `feedback_named_subject_consent.md`
- `feedback_substance_drives_length.md`
- `feedback_verify_stale_memory_claims.md`
- `feedback_voice_polish_pipeline.md`
- `feedback_two_layer_content_discipline.md`
- `reference_ostrom_illustrative_register.md`
- `feedback_dual_audience_test.md`
- `feedback_audit_open_illustrative_default.md`
- `feedback_audit_recent_active_review_default.md`
- `feedback_grammatical_role_cross_references.md`
- `reference_pattern_2_register.md`
- `feedback_pm_dashboard_structure.md`
- `reference_sandel_hybrid_pattern.md`

**1 EDGE-as-MIGRATE file:**
- `feedback_git_workflow.md`

**NOT copied (KEEP-LOCAL, SENSITIVE):** `project_authors_grandfather_nasa_inventor.md`
**NOT copied (ARCHIVE):** `project_book1_state_2026-05-10.md`

Verification: 15 files present in `tools/memory/`; each byte-identical to source except for the YAML frontmatter end position (step 2 will insert content after it).

### Step 2 — Add canonical-pointer headers (decision 5)

For each file where doctrine-side canonical exists, insert this block immediately after the closing `---` of the YAML frontmatter and before the H1 heading:

```
**Canonical full content:** `<path>`
**Layer:** scan-friendly summary; this file is the cross-session discipline pointer. Update the canonical artifact when content changes; sync this summary via `tools/memory-updates/` spec for substantive amendments.

```

**Canonical pointers (8 files):**

| File | Canonical pointer path |
|---|---|
| `feedback_audience_aware_drafting_discipline.md` | `tools/pipeline-doctrine/commons_bonds_pipeline_doctrine_v1.0.0.md` |
| `feedback_two_layer_content_discipline.md` | `alignment/commons_bonds_working_principles_v1.0.0.md` Principle #10 |
| `reference_pattern_2_register.md` | `core/methodology/decision_time_application_internal_v1.0.0.md` §3 |
| `reference_sandel_hybrid_pattern.md` | `tools/rigor-passes/commons_bonds_rigor_pass_2026-05-11_apparatus_register_decision_v1.0.0.md` Item 14 + §"Reusable principles" item 3 |
| `feedback_dual_audience_test.md` | `tools/rigor-passes/commons_bonds_rigor_pass_2026-05-11_apparatus_register_decision_v1.0.0.md` §"Reusable principles" items 1-2 |
| `feedback_grammatical_role_cross_references.md` | Apparatus Item 10 + Phase 5 of appendix-numbering-reconciliation workstream (see memory file's own footer for commit refs) |
| `feedback_pm_dashboard_structure.md` | `tools/workstream-handoffs/pm-session-handoff_2026-05-13.md` |
| `feedback_git_workflow.md` | `alignment/commons_bonds_working_principles_v1.0.0.md` Principle #9 + `CLAUDE.md` "Branch discipline + merge-to-main" section + `tools/workstream-handoffs/README.md` |

**Memory entry IS canonical (no header — 7 files):**
- `feedback_named_subject_consent.md`
- `feedback_substance_drives_length.md`
- `feedback_verify_stale_memory_claims.md`
- `feedback_voice_polish_pipeline.md`
- `reference_ostrom_illustrative_register.md`
- `feedback_audit_open_illustrative_default.md`
- `feedback_audit_recent_active_review_default.md`

### Step 3 — Create `tools/memory/README.md`

In-repo mirror of the local `MEMORY.md` index. Structure:

```
# tools/memory/ — cross-session discipline registry

Mirrors the project's local-machine memory at
`~/.claude/projects/-Users-c17n-commons-bonds/memory/`. Each file is a ratified
discipline (feedback / project / reference) that should hold consistently
across mobile + laptop sessions. Selective `@import` from `CLAUDE.md` covers
the three always-load files; the remaining files are situational — load when
relevant via this index.

**Always-loaded via CLAUDE.md `@import` (3):**

- [feedback_audience_aware_drafting_discipline.md](feedback_audience_aware_drafting_discipline.md) — v3.0 pipeline doctrine summary. Full architecture at `tools/pipeline-doctrine/commons_bonds_pipeline_doctrine_v1.0.0.md`.
- [feedback_named_subject_consent.md](feedback_named_subject_consent.md) — naming defaults for living / deceased / public-record subjects in publisher-facing prose.
- [feedback_verify_stale_memory_claims.md](feedback_verify_stale_memory_claims.md) — staleness discipline for time-sensitive claims in memory reads.

**Situational discipline files (12):**

[List remaining 12 files with one-line hooks per local MEMORY.md]

**Out of scope:**

- KEEP-LOCAL: `project_authors_grandfather_nasa_inventor.md` (SENSITIVE family material; lives in local memory only).
- ARCHIVED: `project_book1_state_2026-05-10.md` (superseded by `AGENTS.md` §"Current canonical state"; see [`ARCHIVE.md`](ARCHIVE.md) for retirement entry).
```

For each one-line hook, copy from local `MEMORY.md` verbatim.

### Step 4 — Create `tools/memory/ARCHIVE.md`

Use the §4 entry from the audit proposal verbatim. Single entry:

```
## Memory archive log

### 2026-05-17 — project_book1_state_2026-05-10.md

[paste §4 first entry from tools/memory-migration-proposal_2026-05-17.md]
```

### Step 5 — Edit `CLAUDE.md`

Insert a new section between the existing "## Workflow defaults" section and the "### Branch discipline + merge-to-main" subsection. Use this content:

```
## Project memory (cross-session discipline)

The project's cross-session discipline registry lives at
[`tools/memory/`](tools/memory/) (index at
[`tools/memory/README.md`](tools/memory/README.md)). Selective always-load
files:

@tools/memory/feedback_audience_aware_drafting_discipline.md
@tools/memory/feedback_named_subject_consent.md
@tools/memory/feedback_verify_stale_memory_claims.md

Remaining files in `tools/memory/` are situational; load when relevant via
the README index.

The local `~/.claude/projects/-Users-c17n-commons-bonds/memory/` directory
remains the default laptop-session memory layer. `tools/memory/` is the
in-repo mirror so mobile sessions + future collaborators can read the
discipline registry from the repo.
```

Wait — `## Workflow defaults` is a top-level heading and `### Branch discipline` is its first subsection. The new section should be a sibling of `## Workflow defaults` (not nested inside it). Insert AFTER the entire "## Workflow defaults" block. Place it AFTER `### Named-subject consent` (the last subsection of Workflow defaults).

Also update the existing line in `### Named-subject consent` from `feedback_named_subject_consent.md memory` to `tools/memory/feedback_named_subject_consent.md` (reflects the new canonical path).

Verification: `@import` directives reference existing files (grep `^@tools/memory/` in CLAUDE.md, check each path exists in working tree).

### Step 6 — Annotate local MEMORY.md (decision 6)

**This step modifies the local-only file `~/.claude/projects/-Users-c17n-commons-bonds/memory/MEMORY.md`, NOT the repo. Local-only edit; no git tracking.**

For each of the 15 migrated files' index entries, append ` — *mirrored at `tools/memory/<filename>`*` to the end of the one-line entry. Example:

```
- [Git workflow — worktree isolation + session-end fast-forward to main](feedback_git_workflow.md) — Working Principle #9 (2026-04-29). NOT push-every-commit-to-main; merge per ratified chunk via `git push origin HEAD:main`. — *mirrored at `tools/memory/feedback_git_workflow.md`*
```

KEEP-LOCAL entry (grandfather): unchanged.
ARCHIVE entry (project_book1_state_2026-05-10): **remove the line entirely** from the index. The memory file itself stays in the local directory (per audit proposal hard constraint "Do NOT delete any local memory files"); only the index entry is removed.

### Step 7 — Add insight #67 (decision 8)

Edit `alignment/commons_bonds_open_insights_v1.0.0.md`. Add a new OPEN insight #67 entry:

```
### Insight #67 — Multi-machine memory sync discipline candidate WP amendment — OPEN

**Surfaced:** 2026-05-17 (memory-migration audit proposal §5 OQ7).

**Question:** If author edits `tools/memory/<file>` locally during a session,
repo and local-memory can drift. Should the working-principles doc codify
"repo copy at `tools/memory/<file>` is canonical; local-memory edits ratified
into repo via `tools/memory-updates/` spec or direct edit at session close"
as an amendment to WP#9 + WP#10?

**Disposition pending:** defer codification until drift-incident data
accumulates. WP#9 + branch discipline handle 90% of the case (repo edits go
through feature branches); the residual gap is local-only memory writes the
author makes in flight, which is currently rare.

**Next action:** observe drift incidents over the next 30-60 days; revisit
codification decision when ≥1 concrete incident surfaces.
```

Also update AGENTS.md §"Current canonical state" → `Open insights tracker` row: increment "OPEN" count (was 6 OPEN as of 2026-05-06; verify current count from the open-insights file at apply time + bump by 1 if #67 is the first new open insight since that snapshot). Update "Next free insight number" to **#68**.

Verification: insight #67 entry parses; OPEN count + next-free-number consistent in AGENTS.md.

### Step 8 — Verification + commit

Pre-commit checks:
- 15 files present in `tools/memory/`.
- 8 of those files have canonical-pointer headers (step 2 list).
- `tools/memory/README.md` lists exactly 15 files.
- `tools/memory/ARCHIVE.md` has the `project_book1_state_2026-05-10.md` entry.
- `CLAUDE.md` has the new "## Project memory" section with 3 `@import` lines; existing line 53 named-subject reference updated.
- `alignment/commons_bonds_open_insights_v1.0.0.md` has insight #67.
- `AGENTS.md` open-insights count + next-free-number updated.
- Local `MEMORY.md` (not in repo) annotated; ARCHIVE entry removed.
- Pre-commit hook + `tools/scripts/check-corpus-invariants.sh` runs clean (per pipeline doctrine §2.4 placement).

Commit message:

```
Memory migration — apply ratified 2026-05-17 audit proposal

Migrates 14 standard MIGRATE files + 1 EDGE-as-MIGRATE file into tools/memory/
per audit proposal §7 ratifications. Adds tools/memory/README.md (index +
selective-@import discipline), tools/memory/ARCHIVE.md (project_book1_state
retirement). Adds selective @import block to CLAUDE.md for 3 always-load
files (audience-aware + named-subject + verify-stale). Adds open insight #67
flag for multi-machine memory sync discipline (deferred WP amendment). KEEP-
LOCAL file (grandfather) untouched per SENSITIVE flag.

Pre-ratified change set per
tools/memory-migration-proposal_2026-05-17.md §7. Autonomous fast-forward
merge to main per CLAUDE.md merge-to-main default.
```

Merge: `git push -u origin claude/memory-migration-apply-<harness-id>` + `git push origin HEAD:main` per WP#9 + CLAUDE.md autonomous-merge default.

---

## Hard constraints

- **Do NOT delete any local memory files.** Only modify the local `MEMORY.md` index per step 6 (annotate + remove ARCHIVE entry from the index; the underlying file stays in the local directory).
- **Do NOT touch `project_authors_grandfather_nasa_inventor.md`** (KEEP-LOCAL per decision 4).
- **Do NOT migrate any file not in the 15-file list.**
- **Do NOT skip pre-commit hooks** (`--no-verify`) without explicit author direction.
- **Do NOT force-push `main`** or amend any commit already on `origin/main`.
- If any step's verification fails, stop and report; do not proceed to commit.

---

## Session-close report

When session closes, report:
- 15 files migrated to `tools/memory/` (list verified).
- 3 selective-`@import` lines added to `CLAUDE.md` (line numbers for author quick-check).
- Insight #67 added (file + line range).
- Local `MEMORY.md` annotated (count of entries annotated).
- Commit SHA + merge-to-main confirmation.

---

*Apply-session handoff — READY TO FIRE 2026-05-17. Originating audit + ratifications at [`tools/memory-migration-proposal_2026-05-17.md`](../memory-migration-proposal_2026-05-17.md).*
