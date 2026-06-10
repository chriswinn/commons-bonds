---
name: project-repo-navigation-spine
description: "MAP.md + STATE.md are the repo's orientation/status spine (2026-06-10 reorg); update STATE.md when changing any status; archive sweep moved closed handoffs/April rigor to archive/ subdirs"
metadata: 
  node_type: memory
  type: project
  originSessionId: 0b52d800-7e03-4be4-8edd-35fcc10ac6b4
---

**Repo navigation spine (established 2026-06-10, repo-reorg session; branch `claude/refactor-bib-consolidation-260609-23c283`).** The repo had 933 files with no single map; sessions were losing track of what lived where (measured: 2,563 broken path references). The fix:

- **`MAP.md` (root)** — THE orientation document: top-level taxonomy (what each dir IS and is NOT), "where do I find X" routing table, lifecycle conventions, live-session ownership warnings.
- **`STATE.md` (root)** — THE live status surface: portfolio tables (essays/op-eds/proposal/agents/book/workstreams) with per-row verification dates. **Discipline: any session that changes a status updates its STATE.md line in the same commit; PM reconciles.** Supersedes the essays/README snapshot table.
- **Archive sweep:** closed handoffs → `tools/workstream-handoffs/archive/` (98 files; top level = live only); April-2026 rigor era → `tools/rigor-passes/archive/` (97); glossary v2/v3 → `core/glossary/archive/`; `core/chapters`+`core/case-studies` (held audits, not content) → `tools/audits/`; `_pipeline` one-shots → `_pipeline/archive/`. Policy: `tools/conventions/archival-policy.md`.
- **Link gate:** `python3 tools/scripts/check-repo-links.py --summary` before/after any file move; zero NEW breaks (compare normalized).

**Why:** 20–35 parallel sessions use the repo as shared memory; append-only sprawl buried live state under closed artifacts (112 handoffs / ~37 active).

**How to apply:** New sessions read MAP.md → STATE.md before searching. Never move live-session-owned files (check STATE.md §Active workstreams + `git worktree list`). Use the archival policy + link gate for any future moves.

**⚠ Shared-stash hazard (learned 2026-06-10):** `git stash` is repo-wide and shared across ALL worktrees. A bare `git stash` + `git stash pop` in any worktree can pop ANOTHER session's stash into your tree (it conflicted into Chapter 8 during this session; recovered via `git checkout HEAD -- <file>`, foreign stash preserved). Never use bare stash/pop in this multi-worktree repo. Related: [[feedback_worktree_isolation_for_parallel_sessions]].
