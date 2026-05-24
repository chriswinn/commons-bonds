# feedback_parallel_session_ratification_cadence

**Date ratified:** 2026-05-24
**Type:** feedback (operational empirics)
**Origin:** Author observation 2026-05-24 (PM-session conversation) correcting Claude's misframing of ratification as a serial-bandwidth-constrained step. Empirically grounded in the author's actual workflow under prior tier-limit constraints (2026-04 through 2026-05-23) and validated under max-tier capacity (2026-05-24 forward).
**Canonical reference:** This file is the canonical entry for the parallel-session-hop operating model. Pipeline Doctrine Amendment C (Interactive Ratification Protocol, ratified 2026-05-19) codifies the per-session pattern; this entry codifies the cross-session-cadence + presentation discipline + PM-as-meta-tracker implications that Amendment C alone doesn't capture.

## Summary

The highest-throughput operating mode for *Commons Bonds* rigor-pass + drafting work is **parallel-session hop with one-finding-at-a-time presentation per session**. Author opens 4–20+ parallel sessions simultaneously; each session at any moment has exactly one pending decision point; author hops between sessions ratifying interactively. The constraint that binds is cognitive switching ceiling + total token throughput, NOT serial author bandwidth (which was Claude's incorrect prior mental model).

This pattern emerged empirically under prior tier-limit constraints (where parallel sessions burned the 5-hour token budget in 1–2 hours, forcing 2–4 day waits for weekly reset). Under max-tier capacity, the prior token bottleneck removes; cognitive switching + sustainability become the binding constraints.

## The pattern

### Session-internal cadence (one finding at a time)

- Claude tracks the complete findings inventory INTERNALLY (organized HIGH → MED → LOW severity)
- Session presents exactly ONE finding at a time in canonical format:
  - **Problem** (what / where / why it matters)
  - **Options** (numbered alternatives)
  - **Recommendation** (Claude's pick + 1-line reason)
  - **Reasoning** (why this matters + why this option)
- Author ratifies / iterates / surfaces-bigger-issue on the single finding
- Spot-fix applies (or notes for batch); session advances to next finding
- Repeat until findings exhausted; commit + auto-merge per `CLAUDE.md`

### Cross-session cadence (parallel hop)

- Author opens N parallel sessions for related rigor work (chapter Stage 3 passes; essay Stage 3 passes; pipeline retrofits; bibliography passes; etc.)
- Each session at any moment has exactly one pending decision point
- Author hops between sessions; each hop is "respond to live finding in current tab"
- Cognitive switching ceiling (not tokens) is the operational constraint
- Empirically 4–6 parallel sessions is the sustainable maximum for sustained focus; 20+ is achievable in sprint mode but with PM-session-as-meta-tracker overhead

### Ratification-mix empirics

- **~70% accept-recommendation** (~5–10 min per finding)
- **~20% propose rewrite + iterate** (~20–30 min per finding)
- **~10% surface bigger issue + discuss** (~30–60+ min; sometimes spawns new workstream)

### Cross-session spawn lineage

- Sessions sometimes spawn sub-sessions. Typical reasons:
  - Minimize LLM cumulative-cadence tics (firing a fresh session for Stage 2 audience-blind drafting from a Stage 1 brief)
  - Isolate cross-chapter coherence work
  - Parallelize independent stages of the pipeline
- Parent session pauses + provides paste-text for sub-session
- Sub-session lands PROPOSED artifact + commit
- Parent session resumes; sub-session output is referenced
- PM session tracks the spawn lineage across all parallel work

## Standardized status markers (used in any session output)

Every session uses these markers in any output where author action is gated:

- 🔴 **AUTHOR DECISION REQUIRED** — author must ratify / decide / answer before session continues
- 🟡 **SUB-SESSION NEEDED** — current session paused; author must fire named sub-session (with paste-text)
- 🟢 **NEXT STAGE READY** — current pass/stage complete; author confirms to advance
- 🔵 **ESCALATION** — structural issue surfaced; needs author discussion
- ⏳ **CLAUDE-ACTION IN PROGRESS** — session working autonomously; no author action needed
- 🟣 **AWAITING EXTERNAL** — blocked on external response (editor reply; Sandy feedback; etc.)
- ✅ **SESSION COMPLETE** — closed; with standardized one-liner state summary

End-of-session one-liner format:

```
STATE: [PROPOSED|APPLIED|RATIFIED]; NEXT: [author-action-required|sub-session-fires|automatic]; AWAITING: [author-ratification|sub-session-X|external-X]
```

PM session scrapes these lines from session-output for the parallel-session inventory dashboard.

## Anti-patterns

### A1 — List-dump anti-pattern

**WRONG:** Session generates the full findings inventory ("Here are 14 findings, organized HIGH/MED/LOW...") and expects author to digest + react.

**WHY:** Triggers analysis paralysis. Author stops hopping between sessions to digest the whole list. Loses parallel-session throughput entirely. Documented empirically by author 2026-05-24 — this was a frequent prior failure mode.

**CORRECT:** Session presents findings one at a time. Author never sees the full inventory.

### A2 — "Propose-only batch then ratify later" anti-pattern

**WRONG:** Frame work as "Claude does heavy propose-only work; author ratifies later in batches." Treat ratification as a separable downstream step constrained by author bandwidth (~2 ratifications/day).

**WHY:** Treats author ratification as separable when it's actually integrated. Amendment C IS the operating mode; ratification happens inside each session. The "batch later" framing was Claude's mental model under the wrong assumption that serial bandwidth was the bottleneck. Documented by author 2026-05-24 as a Claude misframing.

**CORRECT:** Frame work as parallel-session firings with interactive ratification per session. Author bandwidth scales with parallel-session count, not serial throughput.

### A3 — Sub-session-without-paste-text anti-pattern

**WRONG:** Parent session says "fire a fresh session to do X" without providing the actual paste-text.

**WHY:** Author has to compose the paste-text from context. Adds friction. Easy to lose context across the spawn.

**CORRECT:** Parent session provides exact paste-text for the sub-session AND explicit resume-marker for when sub-session completes (artifact path + state to look for).

### A4 — Severity-interleaving anti-pattern

**WRONG:** Present findings in source-order (top-of-document → bottom) regardless of severity.

**WHY:** If author runs out of bandwidth mid-session, low-stakes findings may have been ratified ahead of high-stakes ones. Reverses the priority cost-benefit.

**CORRECT:** Present HIGH findings first, MED second, LOW last. Within severity, source-order is fine.

## Why the PM session matters in this mode

At parallel-session-hop velocity, **author has 20+ sessions open simultaneously** (worked example: 21 sessions reported by author 2026-05-24). Without a PM session tracking:
- Which artifacts are at which pipeline stage
- Which findings have been ratified vs. proposed
- Which sub-sessions are in flight from which parent sessions
- Which sessions are awaiting author action vs. Claude action
- Which sessions are blocked by external dependencies (Sandy reply; Aeon response; etc.)

...the author loses track quickly. The PM session is the meta-tracker that makes 20+ parallel sessions navigable rather than chaotic.

**PM session refresh cadence should scale with parallel-session count:**
- 4–6 parallel sessions: weekly refresh fine
- 10–15 parallel sessions: every 2–3 days
- 20+ parallel sessions: refresh after every major phase shift (often daily during sprint mode)

## Cognitive sustainability — sprint / sustained / blocked modes

Parallel-session-hop is high-throughput but high-cognitive-load. Three operating modes calibrate the tradeoff:

| Mode | Cadence | Per-day load | Per-week volume | Risk profile |
|---|---|---|---|---|
| **Sprint** | 5–6 days/wk @ 4–6 hr parallel-hop | Heavy | Maximum | Burnout risk after ~3 weeks; recovery week needed |
| **Sustained** | 4 days/wk @ 3–4 hr parallel-hop | Medium | High but durable | Sustainable for many weeks |
| **Blocked** | 2–3 day intense bursts + 1–2 day breaks | Variable | Medium | Best per-finding quality; lowest weekly volume |

Sprint mode is appropriate for time-boxed deliverable sprints (e.g., Wave 2 pre-staging across June 2026). Sustained mode is the default for steady-state rigor work. Blocked mode produces the highest-quality per-finding output and is appropriate when the work involves heavy "bigger issue" surfacing (the ~10% case in the ratification mix).

**Calibration check:** if accept-recommendation rate falls below ~60% (author iterating more than usual), that's a signal the author's cognitive bandwidth is saturated. Switch from sprint to sustained or blocked mode.

## Improvements (initial proposals 2026-05-24; ratify case-by-case as they prove out)

### I1 — Session-state breadcrumb on re-entry

When author returns to a parallel session after hopping away, the session immediately surfaces a breadcrumb:

`Finding 3 of 12 (HIGH); Findings 1-2 ratified; current finding shown above; remaining: 4 HIGH + 5 MED + 1 LOW.`

Makes re-entry instant rather than re-reading context.

### I2 — Severity-strict ordering enforced

Within a session, present HIGH findings before MED before LOW. Never interleave. (Already noted as anti-pattern A4 above; this is the positive form.)

### I3 — "Bigger issue" ESCALATION marker

When a finding surfaces a structural issue requiring discussion (the ~10% case), prefix the finding with explicit marker `🔵 ESCALATION:` (matching the standardized status markers above). Author can dive in or note for later without losing context.

### I4 — Sub-session spawn with paste-text + resume marker

Parent session that spawns a sub-session MUST:
- (a) Provide complete paste-text for the sub-session
- (b) Name an explicit resume marker (artifact path + state to look for)
- (c) Auto-pause until author returns and confirms sub-session output

### I5 — Standardized end-of-session one-liner (LOAD-BEARING; ratified into all kick-off paste-texts 2026-05-24)

Every session closes with the format above. PM session scrapes these lines for the parallel-session inventory dashboard.

### I6 — PM session §"Parallel session inventory" (LOAD-BEARING; ratified into PM dashboard 2026-05-24)

PM session adds a new section capturing open sessions + per-session pending decision + awaiting-on + parent-child lineage. Live at PM dashboard 2026-05-24 §10b (markdown) + §9b (HTML).

### I7 — Cognitive-bandwidth signal monitoring

If accept-recommendation rate falls below ~60% sustained over multiple sessions, that's a cognitive-saturation signal. PM session surfaces it; author considers mode-shift (sprint → sustained → blocked).

### I8 — Session-naming convention with parent-child surfacing

When a session spawns a sub-session, the sub-session's branch name encodes the parent. Example: parent `claude/ch6-pass-3-3-light-refire-1fae85` → child `claude/ch6-pass-3-3-light-refire-1fae85-child-stage2-<sub-harness-id>`. PM session scrapes the lineage from branch names.

## How to apply

### For every rigor-pass / Stage 3 / Phase C / Stage 5 / drafting session involving findings + author decisions

1. Track findings inventory internally; organize by severity
2. Present one finding at a time in canonical format
3. Wait for author disposition before presenting next
4. Apply spot-fix interactively (Amendment C cadence)
5. Honor severity-strict ordering (HIGH → MED → LOW; no interleaving)
6. Surface "bigger issue" ESCALATIONs explicitly
7. End with standardized one-line state summary

### For PM coordination across parallel sessions

1. Track session inventory + state per session (refresh as state evolves)
2. Surface dependencies between sessions (parent → sub-session lineage)
3. Surface ratification-queue + sub-session-queue separately
4. Refresh cadence scales with parallel-session count (daily during sprint mode)
5. Monitor cognitive-saturation signal (accept-recommendation rate < ~60% sustained)

### For paste-text scaffolds (kick-off prompts that drive fresh sessions)

Every kick-off paste-text MUST include in its DO list:
- "Present findings ONE AT A TIME. Track inventory internally. Wait for author disposition before next finding. NEVER dump full findings inventory."
- "Severity-strict ordering: HIGH → MED → LOW; no interleaving."
- "🔵 ESCALATION marker for findings surfacing structural issues."
- "End session with standardized one-line state summary."
- "Use status markers (🔴 🟡 🟢 🔵 ⏳ 🟣 ✅) for any author-action-gating output."

Canonical scaffold lives in `tools/drafting-templates/README.md` (refreshed 2026-05-24); worked example at `tools/workstream-handoffs/wave-2-derivative-kickoffs_2026-05-24.md`.

### For bringing existing sessions onto the convention

Paste-text at `tools/drafting-templates/existing-session-checkin-paste-text.md`. Drop into each open session to upgrade in place.

## Empirical anchors

- **Prior-tier constraint experience (2026-04 → 2026-05-23).** Author burned 5-hour token budget in 1–2 hours under parallel-session-hop mode; waited 2–4 days for weekly reset. Empirically demonstrated that parallel-session-hop is the throughput-maximizing mode AND that prior tier limits were the binding constraint, not author bandwidth.
- **Tier upgrade 2026-05-24.** Max-tier capacity removes prior token bottleneck. Cognitive switching ceiling now binds.
- **21-sessions-open observation 2026-05-24.** Author reported 21 parallel sessions open simultaneously at PM-session start. Demonstrates the PM-session-as-meta-tracker need + the I6 § "Parallel session inventory" improvement.
- **List-dump anti-pattern (A1) documented 2026-05-24.** Author explicitly noted that massive findings lists caused parallel-session hopping to stop while the list was digested. Codified as the load-bearing anti-pattern for this discipline.
- **Cross-session sub-session spawn lineage documented 2026-05-24.** Author noted that sessions often instruct firing sub-sessions to minimize LLM tics or parallelize. Codified as a first-class operational pattern.

## Where to read more

- `tools/commons_bonds_pipeline_doctrine_v1.0.0.md` — Amendment C Interactive Ratification Protocol (per-session pattern)
- `tools/memory/feedback_audience_aware_drafting_discipline.md` — v3.1 doctrine (the work this cadence operates on)
- `tools/memory/feedback_pm_dashboard_structure.md` — PM dashboard structure (canonical)
- `tools/memory/feedback_git_workflow.md` — merge-to-main policy (extended 2026-05-24)
- `tools/drafting-templates/README.md` — generic drafting-trigger paste-text scaffold (refreshed 2026-05-24)
- `tools/drafting-templates/existing-session-checkin-paste-text.md` — upgrade mechanism for existing sessions
- `tools/workstream-handoffs/wave-2-derivative-kickoffs_2026-05-24.md` — worked example of kick-off paste-texts that include the one-at-a-time discipline

## Update log

- **2026-05-24.** Initial entry. Codifies the empirical operating pattern + anti-patterns + improvements + sprint/sustained/blocked sustainability framing. Captured by author direction during 2026-05-24 PM-dashboard session.

---

*End of parallel-session-cadence feedback entry.*
