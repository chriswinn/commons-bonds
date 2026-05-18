---
name: Verify time-sensitive claims in stale memories before asserting as fact
description: Memories are point-in-time. Before quoting any countable / time-sensitive / status claim from a memory more than a few days old, verify against current ground truth.
type: feedback
originSessionId: 6a97b0f9-c18b-4992-8bf6-b2bbf9c60acf
---
Memories are snapshots, not live state. The harness already issues a staleness reminder on every memory read ("Memories are point-in-time observations, not live state — claims about code behavior or file:line citations may be outdated. Verify against current code before asserting as fact."). Heed that reminder rigorously, especially for these categories of claims:

- **Counts** — chapter counts, drafted-essay counts, queries-sent counts, interviews-completed counts, populated-target-list counts.
- **Dates** — deadlines, scheduled events, "next steps," "as of."
- **Status** — workstream state ("in flight," "blocked," "pending," "complete"); the same workstream may have moved through multiple states since the memory was captured.
- **File paths** — files may have been renamed, moved, archived, or deleted.
- **Figures** — statistics, dollar amounts, percentages, sample sizes — these often update.

What's usually still safe to quote without verification:
- Names of people (rarely change).
- Conceptual definitions and ratified working principles.
- Historical events (the past doesn't get less true).
- Author preferences and consent decisions (sticky once ratified).

**Why:** Ratified 2026-05-10 after I quoted "7 chapters drafted" repeatedly in chat from a project-state memory dated 2026-05-02. By 2026-05-10 the actual count was 10. The harness's staleness reminder fires automatically; the failure mode was ignoring it. The cost of verification is small (one Bash listing); the cost of a wrong assertion is larger (user has to catch and correct, which erodes trust in the system's accuracy).

**How to apply:** Before asserting any time-sensitive claim sourced from a memory more than ~3 days old, run the relevant verification (`ls`, `git log`, `wc -l`, `grep -c`, etc.). For memories ≥7 days old, treat all countable/status claims as candidate-stale. Memories ≥30 days old get full verification on every relevant claim. The discipline applies to claims appearing in chat output and in newly-written files alike — both can mislead a user or a future session if quoted from stale ground truth.
