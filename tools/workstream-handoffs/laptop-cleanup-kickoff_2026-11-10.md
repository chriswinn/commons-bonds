# Laptop folder cleanup: kickoff for a local Claude Code session (2026-11-10)

**Status:** internal. Paste the block below into a Claude Code session started on the author's Mac, in
`/Users/c17n/commons-bonds`. Run it between the Ch 5 sessions, not alongside one.

```text
Commons Bonds laptop cleanup (local session, 2026-11-10). Goal: every piece of uncommitted work on this Mac is
saved to GitHub, the main checkout is back on main, and stale work folders are removed. Nothing gets lost.

Ignore the SessionStart worktree-isolation warning: CLAUDE.md's one-session banner makes it historical. Don't
create a new worktree for this session.

Safety rules (hard):
- Never delete, reset, clean or overwrite anything until its changes are committed to a rescue branch, pushed,
  and confirmed with git ls-remote.
- No force-push, no git reset --hard, no git clean, no worktree remove --force, no branch -D.
- Don't touch Google Drive. Don't edit or move any manuscript or publishing file's content; rescue as-is.
- Show me the list before each batch of removals and wait for my OK.

Steps:
1. Inventory. Run git fetch origin, git worktree list, and ls -d /Users/c17n/commons-bonds*. For each folder,
   report: branch (or detached HEAD), ahead/behind origin/main, count of modified and untracked files.
   Expected from the 2026-11-01 triage (verify; it may have changed): main checkout on
   claude/br-V-G-structural-choice-V-handoff-260601-7f8e9d with 17 dirty files; br-V-E 9; mcdowell-recs 7;
   ch5-rebuild-260625 5; tolerance-spot-fix 3 (detached); ta-bibconsol 2; noema-draft, noema-vd-cascade,
   public-books-cover-letter, redraft-campaign-resume, ta-stage4-markup and ta-reverse-csd 1 each; plus
   .claude/worktrees/agent-* folders.
2. Triage each dirty file: identical to origin/main (git diff --quiet origin/main -- <path>) → already safe;
   otherwise → rescue. Skip only obvious junk (.DS_Store, __pycache__, node_modules) and list what you skipped.
3. Rescue each folder with unsaved work: in that folder, git switch -c claude/rescue-<folder-slug>-20261110
   (from a detached HEAD too), git add the files to rescue, commit "Rescue uncommitted work from <folder>
   (laptop cleanup 2026-11-10)", git push -u origin <branch>, then confirm with git ls-remote. Don't merge
   rescue branches into main; I'll decide on each later.
4. Main checkout: once its work is rescued and pushed, git switch main and git pull --ff-only. Confirm clean.
5. Removals, after my OK: git worktree remove <path> (no --force) for folders that are clean and fully saved;
   git worktree prune; git branch -d (not -D) for local branches already on origin or merged.
6. Write a manifest (folder → what was rescued, branch name, what was removed, anything skipped) to
   tools/workstream-handoffs/laptop-cleanup-manifest_2026-11-10.md on branch claude/laptop-cleanup-20261110.
   Push it, and fast-forward main only if origin/main is an ancestor (no rebase, no force).
7. End with three lines: what got done · what's waiting on me · the exact next paste line.
```
