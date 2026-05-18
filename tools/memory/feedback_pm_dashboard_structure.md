---
name: PM session dashboard structure (v2.0)
description: Standard structure for PM session handoff dashboards — top-of-mind action driver, priority-labeled status buckets, per-chapter detail with next-action column, date-anchored merged action list, PM session freshness section. Ratified 2026-05-13.
type: feedback
originSessionId: 52436a38-f724-4ccc-b29f-5fc316f7ef6a
---
**Canonical full content:** `tools/workstream-handoffs/pm-session-handoff_2026-05-13.md`
**Layer:** scan-friendly summary; this file is the cross-session discipline pointer. Update the canonical artifact when content changes; sync this summary via `tools/memory-updates/` spec for substantive amendments.

PM session handoff dashboards (`tools/workstream-handoffs/pm-session-handoff_<DATE>.md`) follow this structure, in order, top-of-page first. The structure is action-driving, not just reference-organized — the most-load-bearing question ("what do I do right now?") is answered without scrolling.

**Section order:**

1. **Header / meta / mission / read order** (boilerplate).
2. **Next 72 hours (TOP-OF-MIND)** — 3–5 line at-a-glance action driver. The dashboard's #1 job.
3. **Critical path bottleneck** — 2-line callout identifying the workstream(s) whose completion unblocks the largest fraction of downstream cascade.
4. **USER ACTIONS gating submissions** — elevated to top-level because these are uniquely user-action items (independent of any session firing) and gate near-term submissions.
5. **Workstream status by bucket** in order: IN FLIGHT → READY TO FIRE → WAITING/BLOCKED/DORMANT → COMPLETE (one-liner). Within each bucket, rows ordered by **priority** (HIGH/MED/LOW), not by workstream number. Priority column explicit.
6. **#20 Stage-3 per-chapter detail block** — include a "next action" column so the table doubles as a roadmap.
7. **Apparatus + front-and-back-matter section** — Bibliography, Tech Appendix, Glossary (multi-phase per-chapter + book-wide audit), plus AI Statement + Dedication (single-pass). Each row tagged with "fires when" condition.
8. **Decisions pending** — embed structural / unresolved-sequencing questions in-dashboard rather than as trailing chat text.
9. **Date-anchored action list** — single merged view of deadlines + todos, bucketed Today / This week / specific upcoming dates / Late June / Late July / Backlog / Dormant. Replaces the earlier separate calendar + todos.
10. **Cross-thread coordination** — preserve as before.
11. **PM session freshness** — when to wrap current PM session and start fresh.
12. **Disciplinary boilerplate** — common-prompt handling, auto-verify discipline, parallel-collision risk, reusable templates, v2.0 drafting discipline, outreach detail, updating instructions, reference inventory.

**Priority labels:**
- **HIGH** = time-pressured (hard deadline within ~30d) OR gates large downstream cascade.
- **MED** = important but not yet gating; no near-term hard deadline.
- **LOW** = small / dormant / waiting on conditional trigger.

Re-evaluate priority on each refresh — a workstream's priority shifts as deadlines approach or dependencies clear.

**Why:** Original dashboard structure (pre-2026-05-13) was reference-organized — workstream # order, single mega-status table, separate calendar, separate todos. User feedback 2026-05-13 was that it required too much scrolling and cross-referencing to answer "what should I do right now?" The v2.0 structure leads with action drivers (Next 72h, critical path, user actions) and treats reference detail as the second-tier scan.

**How to apply:**
- Every PM session that writes or refreshes a handoff inherits this structure.
- Successor handoffs (`pm-session-handoff_<NEW-DATE>.md`) preserve section ordering and headers — only content updates.
- Priority assignments re-evaluated each refresh.
- The PM-session-freshness section (§11) is mandatory — it tells the next session when to recommend wrapping.

**Codified in:** `tools/workstream-handoffs/pm-session-handoff_2026-05-13.md` (after 2026-05-13 v2.0 reorganization).
