# Existing-Session Check-In Paste-Text (2026-05-24)

**Purpose.** Bring any existing parallel Claude Code session onto the new 2026-05-24 operating convention (one-finding-at-a-time presentation + standardized status markers + end-of-session one-liner). Paste the block below into each open session you want to upgrade. Sessions absorb the convention from the next prompt forward.

**Why this exists.** As of 2026-05-24 the canonical operating pattern for *Commons Bonds* rigor + drafting work is parallel-session-hop with one-finding-at-a-time presentation, captured in [`../memory/feedback_parallel_session_ratification_cadence.md`](../memory/feedback_parallel_session_ratification_cadence.md). Existing sessions that started before 2026-05-24 don't know about the conventions yet. This check-in upgrades them in-place.

**When to paste.** Any session that's mid-workstream and where you want clearer status communication going forward. Especially recommended for sessions you might leave open for hours/days and re-enter intermittently.

---

## Copy-paste block

```
SESSION CONVENTION UPDATE 2026-05-24 — operating-cadence upgrade.

Going forward in this session, apply the following conventions
captured in tools/memory/feedback_parallel_session_ratification_cadence.md
(ratified 2026-05-24):

1. Read tools/memory/feedback_parallel_session_ratification_cadence.md
   in full BEFORE your next response. Honor the canonical pattern.

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

---

*End of existing-session check-in paste-text.*
