# Existing-Session Check-In Paste-Text (2026-05-24; updated 2026-05-26 with worktree-isolation step)

**Purpose.** Bring any existing parallel Claude Code session onto the new 2026-05-24 operating convention (one-finding-at-a-time presentation + standardized status markers + end-of-session one-liner) **AND the 2026-05-26 worktree-isolation discipline**. Paste the block below into each open session you want to upgrade. Sessions absorb the convention from the next prompt forward.

**Why this exists.** As of 2026-05-24 the canonical operating pattern for *Commons Bonds* rigor + drafting work is parallel-session-hop with one-finding-at-a-time presentation, captured in [`../memory/feedback_parallel_session_ratification_cadence.md`](../memory/feedback_parallel_session_ratification_cadence.md). The 2026-05-26 worktree-isolation discipline (per [`../memory/feedback_worktree_isolation_for_parallel_sessions.md`](../memory/feedback_worktree_isolation_for_parallel_sessions.md)) closes a branch-contamination failure mode that emerged under sustained 20-35+ parallel sessions in the same physical cwd. Existing sessions started before 2026-05-26 are at risk; this check-in upgrades them in-place.

**When to paste.** Any session that's mid-workstream and where you want clearer status communication going forward. Especially recommended for sessions you might leave open for hours/days and re-enter intermittently. **As of 2026-05-26, every existing session also needs the worktree-isolation upgrade — paste this check-in into every open session before continuing parallel-hop work.**

---

## Copy-paste block

```
SESSION CONVENTION UPDATE 2026-05-26 — worktree-isolation +
operating-cadence upgrade.

Going forward in this session, apply the following conventions:

0. WORKTREE-ISOLATION CHECK (FIRST ACTION — do this before
   anything else):

   Run: pwd && git rev-parse --show-toplevel

   If both report /Users/c17n/commons-bonds (the MAIN repo cwd),
   you are in a CONTAMINATION-PRONE state — multiple parallel
   sessions in this same cwd share .git/HEAD and corrupt each
   other's branches on every checkout/commit. Migrate this session
   to an isolated worktree before any further work:

     # Identify what workstream this session has been working on
     # (replace <workstream-slug> with a short descriptive slug)
     WORKSTREAM="<workstream-slug>"  # e.g. "ch4-stage5", "wave-2-ch4-fa"
     HARNESS_ID="$(date +%y%m%d)-$(openssl rand -hex 3)"
     BRANCH="claude/${WORKSTREAM}-${HARNESS_ID}"
     WORKTREE_PATH="/Users/c17n/commons-bonds-${WORKSTREAM}-${HARNESS_ID}"

     # If you have UNCOMMITTED WORK in the main cwd:
     # 1. git status --short to see what's modified
     # 2. EITHER commit what's clearly yours (only files you authored
     #    in this session) on the CURRENT branch first, THEN move;
     # 3. OR stash with a descriptive name, create the worktree, then
     #    re-apply the stash:
     #      git stash push -m "${WORKSTREAM} migration to worktree" -- <your files>
     #      git worktree add -b "${BRANCH}" "${WORKTREE_PATH}" origin/main
     #      cd "${WORKTREE_PATH}" && git stash pop

     # If you have NO uncommitted work in main cwd:
     git fetch origin main
     git worktree add -b "${BRANCH}" "${WORKTREE_PATH}" origin/main

   All subsequent tool calls in this session use absolute paths
   inside ${WORKTREE_PATH}. Do not cd back to
   /Users/c17n/commons-bonds for any operation.

   Canonical reference + paste-text:
   tools/drafting-templates/worktree-isolation-paste-text.md
   Memory entry: tools/memory/feedback_worktree_isolation_for_parallel_sessions.md

   If pwd already reports a path OTHER than /Users/c17n/commons-bonds
   (e.g., /Users/c17n/commons-bonds-<workstream>-<harness>, or
   .claude/worktrees/<name>), you are already isolated — skip step 0
   and proceed to step 1.

1. Read tools/memory/feedback_parallel_session_ratification_cadence.md
   AND tools/memory/feedback_worktree_isolation_for_parallel_sessions.md
   in full BEFORE your next response. Honor the canonical patterns.

2. Present findings/decisions ONE AT A TIME. Track the full inventory
   internally (HIGH → MED → LOW severity; never interleave). Show
   exactly ONE finding at a time in canonical format (Problem /
   Options / Recommendation / Reasoning). Wait for my disposition
   before showing the next. NEVER dump a full findings inventory in
   a single output — that breaks my parallel-session-hop cadence
   across 20+ concurrent sessions.

3. Use these STANDARDIZED STATUS MARKERS in any output where I need
   to act, decide, move stages, or fire a separate session:

     🔴 AUTHOR DECISION REQUIRED: [what specifically; brief]
     🟡 SUB-SESSION NEEDED: [what to fire; paste-text inline if short,
        or paste-text path if long]
     🟢 NEXT STAGE READY: [what stage; what to confirm to advance]
     🔵 ESCALATION: [structural issue worth discussion]

   These markers help me scan parallel sessions visually for action
   items without reading full session output.

4. When this session would otherwise close (end of pass / artifact
   ratified / sub-session needed / awaiting external), end with a
   single-line state summary in this format:

     STATE: [PROPOSED|APPLIED|RATIFIED]
     NEXT: [author-action-required|sub-session-fires|automatic]
     AWAITING: [author-ratification|sub-session-X|external-X]

   The PM session scrapes these lines for the parallel-session
   inventory dashboard.

5. CURRENT STATE CHECK: Before your next substantive response,
   briefly tell me:
     - What pass/stage/phase this session is working on
     - Where we left off (last finding ratified or decision pending)
     - Whether I have an immediate decision pending (use 🔴 marker)
     - Whether you're ready to advance to a next stage (🟢 marker)
     - Whether a sub-session is needed (🟡 marker)
     - Estimated remaining findings/decisions in current pass
     - Whether the worktree-isolation step in §0 fired or was skipped
       (and which path you are now operating in)

Format this current-state check as a tight bulleted summary, then
wait for me to direct the next action. Do not produce additional
work in this response until I respond.
```

---

## What to expect after pasting

The session will:
1. Read the parallel-session-cadence memory file
2. Re-orient against current pass / state / pending decisions
3. Output a tight current-state check using the new markers
4. Pause for your next direction

This lets you re-enter each session with a clear sense of "where am I and what's next" — without re-reading the prior session output.

## Variant for sessions firing fresh (not yet started)

For sessions you haven't yet kicked off — i.e., paste-text scaffolds in `tools/drafting-templates/` or `tools/workstream-handoffs/*-kickoffs_*.md` — you don't need this check-in. The scaffolds already include the conventions in their DO blocks (as of 2026-05-24 refresh).

## Notes on coverage

The check-in only upgrades the LIVE conversation context of an existing session. It doesn't retroactively reformat prior session output. If a session generated a "massive findings list" earlier, that list stays in the prior turns — but the session will use one-at-a-time going forward from the next response.

**For sessions deep in a finding-by-finding ratification cadence already:** skip the check-in. They're already in the right mode; pasting the check-in would just disrupt their flow.

**For sessions that have produced a list and are awaiting your "react to all of these" response:** paste this check-in. The session will pivot to one-at-a-time going forward.

---

## Update log

- **2026-05-24.** Initial. Pre-stages the 21-sessions-open reality observed 2026-05-24.
- **2026-05-26.** Added §0 worktree-isolation check at top of paste-block. Under sustained 20-35+ parallel sessions, sessions running in the main `/Users/c17n/commons-bonds` cwd share `.git/HEAD` and contaminate each other's branches. The discipline is captured at [`../memory/feedback_worktree_isolation_for_parallel_sessions.md`](../memory/feedback_worktree_isolation_for_parallel_sessions.md); a SessionStart hook at [`../scripts/session-start-worktree-isolation.sh`](../scripts/session-start-worktree-isolation.sh) emits a context warning for fresh sessions; this paste-text upgrades existing sessions.

---

*End of existing-session check-in paste-text.*
