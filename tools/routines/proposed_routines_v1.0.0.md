# Commons Bonds — Routines (v2.0.0)

**Version:** 2.0.0
**Date:** 2026-05-09 (revised from v1.0.0 2026-04-28)
**Status:** RATIFIED 2026-05-09 + SCHEDULED 2026-05-09 — Routines 1', 2 (refined), 3', 4' live as remote agents on a unified 6:30am ET cadence (cron-time refresh 2026-05-09; v1.0.0 Routines 1, 3, 4 deprecated/deferred per author direction). DST-shift reminder one-shot scheduled for 2026-10-25.
**Author:** Chris Winn (drafting + review); routines run as scheduled remote agents

> **Filename note.** This file is named `proposed_routines_v1.0.0.md` because it was created at v1.0.0 on 2026-04-28. The v1.0.0 routine specs are recoverable from git history; the file has been rewritten in place at v2.0.0 to keep cross-references stable. Future major revisions will follow the same in-place pattern with a version bump in the header.

---

## Why v2.0.0 — what changed since v1.0.0

The v1.0.0 routines (drafted 2026-04-28) were calibrated for a project phase where:
- Vocabulary churn was active (8-tier scheme retired 2026-04-24, AIT→CIT, Reparations→Restitution Bond, etc.)
- Chapter drafts were partially-developed (Ch 1 in scaffolding; some chapters under-target)
- Single-thread-at-a-time work was the norm

By 2026-05-09 the project has shifted:
- 9 of 10 chapters drafted post-vocabulary-stabilization (vocabulary churn near-zero)
- Multi-branch parallel work (8+ feature branches active simultaneously)
- Cross-thread coordination friction is the dominant friction (rescue-from-frozen-sessions pattern emerged)
- Stale-reference accumulation across artifacts (~30 path updates in a single 2026-05-09 cleanup pass)

The v2.0.0 routine set replaces low-marginal-value vocabulary-churn-era routines with high-leverage coordination-era routines, lightens others, and defers ones whose surface area no longer warrants weekly attention.

---

## Per-routine status changes (v1.0.0 → v2.0.0)

| v1.0.0 Routine | v2.0.0 Status | Reason |
|---|---|---|
| 1 — Daily terminology-regression sentinel | **DEPRECATED** | Vocabulary regressions are rare post-stabilization; daily scans yield mostly empty findings. Replaced by Routine 1' (cross-thread state-snapshot). |
| 2 — Weekly pre-submission readiness audit | **RATIFIED-with-refinement** | Lighter scope: only chapters in active polish + Ch 3; drop comprehensive notation-collision sweep (mostly stable per Insight #21 closure). See refined spec below. |
| 3 — Weekly rigor pass status tracker | **DEFERRED** | Rigor passes accumulating slowly at current stage. Reactivate when rigor-pass volume increases. |
| 4 — Weekly Open Insights status sync | **DEFERRED** | Insights file small enough to scan manually. Over-engineered for current state. Reactivate post-Phase 3 Tech Appendix rebuild. |

## NEW routines in v2.0.0

| Routine | Cadence | Purpose |
|---|---|---|
| **1' — Cross-thread state-snapshot** | Every other day, 6:30am ET | Survey branches; flag stale references + open cross-thread TODOs; replaces Routine 1's slot |
| **3' — Branch hygiene scan** | Weekly Friday 6:30am ET | Surface branch-sprawl candidates for retirement; pre-empt the rescue-from-frozen-sessions pattern |
| **4' — Stale-reference scan** | Weekly Sunday 6:30am ET | Punch-list of broken cross-references in publishing-strategy + manuscript-essay artifacts |

---

## Routine 1' — Cross-thread state-snapshot

**Purpose.** Every other day, surface what's changed across the project since the last snapshot — what landed on main, what's in flight on which feature branches, what stale references have accumulated, what cross-thread TODOs are open. Replaces v1.0.0 Routine 1 (daily terminology-regression sentinel) which has low marginal value post-vocabulary-stabilization.

**Cadence.** Every other day at 6:30am ET. Cron: `30 10 */2 * *` UTC (EDT-anchored; revisit at Nov 2026 DST shift). **Live as `trig_016fusGEFZV49uaWfRXNBPTT` since 2026-05-09; cron-time refreshed to 6:30am ET later same day.**

**Prompt:**

```
You are running a cross-thread state-snapshot for the Commons Bonds book project at /Users/c17n/commons-bonds.

Steps:

1. Run `git fetch --all --prune` then survey:
   - origin/main HEAD vs. previous snapshot HEAD (commits since last run, ~48h window)
   - All `claude/*` remote branches: commits ahead of main, last commit date
   - Identify branches stale > 7 days

2. For commits to main since last snapshot, summarize what changed in:
   - publishing/ (publishing-strategy artifacts)
   - manuscript/ (chapter drafts, GuidanceDocs, essays)
   - research/ (bibliography, outreach, story-drafts)
   - alignment/ (decisions, sessions, insights, working principles)
   - tools/ (rigor passes, audits, routines)

3. Scan for stale references in canonical living artifacts:
   - publishing/essays/_pipeline/cascade-plan_2026-05-06.md
   - publishing/essays/_pipeline/decisions-log.md
   - publishing/essays/_pipeline/rights-register.md
   - publishing/essays/_pipeline/cross-thread-todos.md
   - publishing/essays/noema-commons-bonds/_archive/planning/rewrite-plan_2026-05-01.md
   - publishing/essays/noema-commons-bonds/_archive/planning/noema-essay-drafting-plan_*.md
   - publishing/essays/aeon-mask-of-abundance/_archive/planning/aeon-submission-strategy_*.md
   - For each markdown file path or commit hash referenced in those artifacts, verify the target exists / commit is reachable. Flag candidates whose target was renamed/moved/deleted.

4. Read publishing/essays/_pipeline/cross-thread-todos.md
   - List items still in "Open" status
   - Flag items with target-resolution date in the past (if dated)
   - Flag items where the surfaced-by or for-thread session has been inactive > 14 days

Output format:

## Cross-thread state-snapshot — YYYY-MM-DD HH:MM ET

### What landed on main since last snapshot
- (List commits with brief descriptions; group by area: publishing/manuscript/research/alignment/tools.)
- (If zero commits: "No new commits on main since last snapshot.")

### Active feature branches
- branch-name | N commits ahead | last commit YYYY-MM-DD | scope (publishing/manuscript/etc.) | suggested fate
- (Stale > 7 days flagged with **STALE** marker.)

### Stale-reference findings
- file:line — referenced path: <path> — issue: <not found / renamed to X / etc.>
- (Limit 20 findings; report "all clean" if none.)

### Open cross-thread TODOs
- (Pull from publishing/essays/_pipeline/cross-thread-todos.md "Open" section; flag overdue items.)

### Recommended actions
- (1-3 highest-priority items to address based on the above.)

Snapshot run YYYY-MM-DD at HH:MM UTC. Next run: day-after-tomorrow 6:30am ET.
```

**Expected output:** ~½-page state-snapshot suitable for morning-coffee review. Picks up drift between branches before it accumulates into rescue-from-frozen-sessions territory.

---

## Routine 2 (refined) — Weekly pre-submission readiness audit (lighter scope)

**Purpose.** Catch publication-readiness blockers in chapters in active polish + Ch 3 (the only undrafted chapter as of 2026-05-09). Drops the comprehensive notation-collision sweep (mostly stable post-Insight #21 closure 2026-05-04).

**Cadence.** Weekly Monday 6:30am ET. Cron: `30 10 * * 1` UTC (EDT-anchored). **Live as `trig_018z7Dkcrw7R9Br25rvmCnTD` (re-purposed in-place from v1.0.0 Routine 2) since 2026-05-09; cron-time refreshed to 6:30am ET later same day.**

**Refinements from v1.0.0:**
- Scope reduced: only chapters in active polish + Ch 3 (previously: all 10 chapters every week). "Active polish" determined dynamically by `git log --since="14 days ago" --name-only -- 'manuscript/chapters/Chapter_*Draft.*'`.
- Drop the framework-wide notation-collision sweep (Insight #21 closed; stable until Phase 3 Tech Appendix rebuild lands).
- Length tracking softened: per "substance drives length" discipline (ratified 2026-05-02), don't flag for "under target" if substance is complete; only flag for "substantially over target" (>130% of upper bound) with magnitude.
- Add manuscript-completion-rate metric: % chapters READY for submission across the 10-chapter scope.

**Prompt (live):**

```
Cron: 30 10 * * 1 UTC (Monday 6:30am ET) — v2.0.0-refined weekly pre-submission readiness audit for the Commons Bonds book project.

The repo is checked out at the working directory. This is the v2.0.0-refined version of Routine 2 (lighter scope per author direction 2026-05-09; supersedes v1.0.0 Routine 2). See tools/routines/proposed_routines_v1.0.0.md for spec.

=== Scope (refined) ===

Audit only chapters in active polish + Chapter 3 (the only undrafted chapter as of 2026-05-09). Identify chapters in active polish by:
- `git log --since="14 days ago" --name-only -- 'manuscript/chapters/Chapter_*Draft.*'` — any chapter file with commits in the last 14 days is "in active polish"
- ALWAYS include Chapter 3 (Ch 3 audit covers the not-yet-drafted slot)

If no chapters meet these criteria, skip Group A/B audit and go directly to the Manuscript-completion-rate section.

=== Group A — Publication-blocker checks ===

A1. Model-output preamble residue: Pattern within first 30 lines: "Let me connect to" / "Let me pull" / "I have the full context" / "Before writing, a few notes". Flag files + line numbers.

A2. Strikethrough editing markup: Pattern ~~text~~. Flag files + line numbers.

A3. INTERVIEW NEEDED placeholders: Pattern "[INTERVIEW NEEDED" (case-insensitive). Count per chapter.

A4. Truncated paragraphs: Mid-paragraph truncations (heuristic: lines ending mid-word). Flag.

=== Group B — Scaffolding-content patterns (per Working Principle #8) ===

Per Working Principle #8 (RATIFIED 2026-04-28; alignment/commons_bonds_working_principles_v1.0.0.md), Tier 1 publisher-facing artifacts (chapter drafts, glossary, Tech Appendix) must not contain audit-trail / scaffolding content.

B1. "Backed by rigor pass" — exact phrase search (case-insensitive). Flag files + line numbers + 1-line context.
B2. "Per Insight #N" cross-references — pattern: `Per Insight #\d+`. Flag.
B3. "Per Working Principle #N" cross-references — pattern: `Per Working Principle #\d+`. Flag.
B4. Rigor-pass commit-hash references — pattern: backtick-wrapped 6-12 char hex hashes adjacent to "commit" / "ratified" / "rigor pass" tokens within ±10 chars. Flag.
B5. M11 probe markers — patterns: "M11 probe" / "M11 critic-survival probe" / "M11 critic prompt" / "M11 critic". Flag.
B6. "Per author direction" annotations — pattern: `Per author direction \d{4}-\d{2}-\d{2}`. Flag.
B7. Author-meta-notes (HEURISTIC — flag with `?`): bracketed annotations like `[Flag this when` / `[Note to self:` / `[TODO:` / `[Note to author` / `[ratify ` / `[author:`. Use `?` flag.
B8. Status-indicator residue (HEURISTIC — flag with `?`): `**Status:**` / `**Term-spec version:**` / `**Last reviewed:**` / `**Rigor provenance:**` patterns appearing in chapter prose.

=== Out of scope — do NOT flag ===

- Lineage citations on first-use (Brown Weiss 1989, Pigou 1920, Stern 2007, Nordhaus DICE, Hotelling 1931, etc.)
- Tier B framework-specialization footnotes
- Tech Appendix §L methodological footnotes
- Reader-facing cross-references between chapters
- Case-study sources / data citations
- Footnotes that aid reader comprehension
- Inline references to historical events / academic literature that are part of the prose
- DROPPED FROM v1.0.0: framework-wide notation-collision sweep (Insight #21 closed 2026-05-04; stable until Phase 3 Tech Appendix rebuild lands)

=== Length tracking (softened per substance-drives-length discipline) ===

Per Working Principle (substance drives length, ratified 2026-05-02): do NOT flag chapters as "under target" if substance is complete. Only flag for substantially over target — and report magnitude (% over upper bound).

Word count target ranges (Ch 1: 5K-6K; Ch 2: 5K-6K; Ch 4: 5K-6K; Ch 5: 5K-6K; Ch 6: 6K-8K; Ch 7: 5K-6K; Ch 8: 5K-6K; Ch 9: 5K-6K; Ch 10: 5K-7K).

Report length but only mark as a length issue if word count > 130% of upper bound.

=== Manuscript completion rate (NEW in v2.0.0) ===

Across the full 10-chapter scope (`manuscript/chapters/Chapter_*Draft.*`):
- Count of chapters: 10 expected
- Count of chapters that exist as files
- Count of chapters whose pre-submission status would be READY (no Group A/B findings; reasonable length)
- Manuscript-completion-rate = (READY count) / 10 expressed as percentage

Run a fast pre-submission status check on chapters NOT in active polish (just Group A blockers — A1, A2, A4 — skip Group B for non-active-polish chapters). This is just to compute the completion-rate metric.

=== Output format ===

## Refined pre-submission readiness audit — YYYY-MM-DD HH:MM UTC

### Scope this run
- Chapters in active polish: [list with last-commit dates]
- Plus Ch 3 (always audited)

### Audit findings (chapters in scope)

Per chapter:
## Chapter N — [name]
· Length: X,XXX words [— OK | OVER by Y% (only if > 130% upper bound)]
· A1 Model-output preamble: [CLEAN | findings]
· A2 Strikethrough markup: [CLEAN | findings]
· A3 INTERVIEW NEEDED: [N count]
· A4 Truncated paragraphs: [CLEAN | findings]
· B1 Backed by rigor pass: [CLEAN | findings]
· B2 Per Insight #: [CLEAN | findings]
· B3 Per Working Principle #: [CLEAN | findings]
· B4 Rigor-pass commit-hashes: [CLEAN | findings]
· B5 M11 probe markers: [CLEAN | findings]
· B6 Per author direction: [CLEAN | findings]
· B7 Author-meta-notes (heuristic): [CLEAN | findings flagged ?]
· B8 Status-indicator residue (heuristic): [CLEAN | findings flagged ?]
· Pre-submission status: [READY | NEEDS CLEANUP — Group A blocker | NEEDS CLEANUP — Group B scaffolding-scrub | NEEDS CLEANUP — both]

### Manuscript completion rate
- Chapters expected: 10
- Chapters present: N
- Chapters READY: K
- Manuscript-completion-rate: K/10 = X%

### Closing summary
- Active-polish chapters audited: A
- Ch 3 status: [READY | NEEDS CLEANUP — ...]
- Group A blockers (publication stoppers): X total findings across Y files
- Group B scaffolding-scrub items: X total findings across Y files
- Manuscript-completion-rate: X%

Audit run YYYY-MM-DD at HH:MM UTC. Next run: Monday next week 6:30am ET.

Context: this is v2.0.0-refined Routine 2. Scope reduced to chapters in active polish + Ch 3 (vs. all 10). Length-tracking softened per substance-drives-length discipline. Notation-collision sweep dropped per Insight #21 closure. Manuscript-completion-rate metric added.
```

---

## Routine 3' — Branch hygiene scan

**Purpose.** Weekly Friday afternoon scan of all `claude/*` remote branches; surface branch-sprawl candidates for retirement; pre-empt the rescue-from-frozen-sessions pattern that emerged when ~8 branches accumulated unmerged work.

**Cadence.** Weekly Friday 6:30am ET. Cron: `30 10 * * 5` UTC (EDT-anchored). **Live as `trig_01AcETfMQs2kD8vyvuKK5Arw` since 2026-05-09; cron-time refreshed to 6:30am ET later same day.**

**Prompt:**

```
You are running a weekly branch hygiene scan for the Commons Bonds book project at /Users/c17n/commons-bonds.

Steps:

1. `git fetch --all --prune`
2. List all `claude/*` remote branches.
3. For each branch:
   - Commits ahead of origin/main
   - Last commit date
   - Change scope (which top-level directories touched: publishing/manuscript/research/alignment/tools)
   - Most recent commit message subject (first line)
4. Categorize each branch by suggested fate:
   - **ACTIVE** — commits within last 3 days; active work in flight
   - **HIBERNATING** — last commit 4-7 days ago; in-flight but not currently active
   - **MERGE-AND-RETIRE** — single commit or small commit-set (≤3) ready to fast-forward to main
   - **ABANDONED** — last commit > 14 days ago; stale; consider deletion

Output format:

## Branch hygiene scan — YYYY-MM-DD HH:MM ET

| Branch | Commits ahead | Last commit | Scope | Subject (most recent) | Suggested fate |
|---|---|---|---|---|---|
| ... | ... | ... | ... | ... | ... |

### Closing summary
- Active branches: N
- Hibernating: M
- Merge-and-retire candidates: K (list by name)
- Abandoned candidates: J (list by name; recommend deletion review)

### Recommended actions
- (1-3 specific moves: e.g., "Fast-forward `claude/X` to main"; "Review `claude/Y` for abandonment"; etc.)

Scan run YYYY-MM-DD. Next run: Friday next week 6:30am ET.
```

**Expected output:** brief table + closing summary. Friday morning timing puts the digest in front of the author at start-of-day end-of-week (unified 6:30am ET cadence with the other routines).

---

## Routine 4' — Stale-reference scan

**Purpose.** Weekly scan for broken or outdated cross-references in publishing-strategy + manuscript-essay artifacts. Catches: file paths whose target was renamed/moved/deleted; references to versions/decisions superseded but not updated; "resolved" decisions not yet struck through; outdated Date-modified fields.

**Cadence.** Weekly Sunday 6:30am ET. Cron: `30 10 * * 0` UTC (EDT-anchored). **Live as `trig_01Puk9mHXTRUT8UWVUjptd1S` since 2026-05-09; cron-time refreshed to 6:30am ET later same day.**

**Prompt:**

```
You are running a weekly stale-reference scan for the Commons Bonds book project at /Users/c17n/commons-bonds.

Targets (canonical living artifacts):
- publishing/essays/_pipeline/*.md
- publishing/book-proposal/*.md
- publishing/agents/*.md
- publishing/essays/templates/*.md
- publishing/essays/noema-commons-bonds/_archive/planning/rewrite-plan_*.md
- publishing/essays/noema-commons-bonds/_archive/planning/noema-essay-drafting-plan_*.md
- publishing/essays/aeon-mask-of-abundance/_archive/planning/aeon-submission-strategy_*.md
- publishing/essays/aeon-mask-of-abundance/_archive/planning/aeon-essay-dunbar-aside-drafts_*.md
- alignment/sessions/commons-bonds-session-handoff-*.md (latest only)
- tools/routines/proposed_routines_*.md
- research/outreach/_pipeline/*.md
- research/outreach/_protocols/*.md

Checks:

1. **Broken file-path references.** Extract `[text](path/to/file)` markdown links and inline `` `path/to/file.md` `` patterns. Verify each target exists at the cited path. Flag missing.

2. **Stale path references after restructure.** Specific patterns to check:
   - `research/outreach/<subject>-<artifact>` (flat-path pattern; should now be `research/outreach/subjects/<subject>/<artifact>` post-2026-05-09 restructure)
   - `publishing/essays/draft2.md` (archived 2026-05-08; should now be at `archive/_OneDayMaybe/withdrawn-essays/draft2_withdrawn-noema_2026-05-01.md`)
   - `publishing/essays/aeon-mask-of-abundance/_archive/prior-versions/aeon-pitch-commons-bonds-winn_VERSION-B_alternate-frame.md` (deleted 2026-05-08; superseded by Version C)

3. **Stale version references.** Check for "Version A" / "Version B" references in Aeon-context artifacts (Version C is the locked submission cut as of 2026-05-08).

4. **Resolved-decision markers.** Items in "Decisions due" or "Open" sections that are actually resolved per decisions-log/git history. Cross-check against:
   - publishing/essays/_pipeline/decisions-log.md latest entries
   - publishing/essays/_pipeline/cross-thread-todos.md "Resolved" section

5. **Date-modified lint.** For files with `**Date modified:**` headers, verify Date modified ≥ most recent commit touching the file (per git log). Flag if file has been modified more recently than the stated Date modified.

Output format:

## Stale-reference scan — YYYY-MM-DD HH:MM ET

### Broken file-path references
- file:line — referenced path: <path> — issue: not found / suggested replacement: <path>

### Stale-path-after-restructure findings
- (Punch-list of flat-path or version-B references that should be updated.)

### Stale version references
- (Aeon Version A/B references that should be Version C.)

### Resolved-decision markers
- (Items still listed as open that are actually resolved.)

### Date-modified lint
- file — last commit YYYY-MM-DD — Date modified header YYYY-MM-DD — bump needed

### Closing summary
- Total findings: N
- High-priority (broken paths): K
- Medium-priority (stale references): M
- Low-priority (Date-modified lint): J

Scan run YYYY-MM-DD. Next run: Sunday next week 6:30am ET.
```

---

## Implementation order recommendation (v2.0.0) — historical, superseded 2026-05-09

The original phased-rollout recommendation (preserved below) was superseded by author choice on 2026-05-09 to schedule all four routines in parallel. First-week output across all four will validate cadences simultaneously rather than sequentially.

Original phased recommendation:

1. **Routine 1' first** (cross-thread state-snapshot, every other day) — highest expected leverage; replaces deprecated Routine 1 slot. Stand up immediately.
2. **Routine 4'** (stale-reference scan, weekly Sunday) — second-highest leverage; addresses path/reference drift. Stand up after 1 week of Routine 1' output validates the cadence.
3. **Routine 3'** (branch hygiene scan, weekly Friday) — useful if branch sprawl continues. Stand up if the rescue-from-frozen-sessions pattern recurs.
4. **Refine Routine 2** (lighter scope) — when convenient; full prompt rewrite needed before next Monday-morning run.
5. Re-evaluate v1.0.0 deferred Routines (3 + 4) after Phase 3 Tech Appendix rebuild lands.

Item 5 (re-evaluating deferred Routines 3 + 4 post-Phase-3) remains the open recommendation.

---

## Author ratification + scheduling status (updated 2026-05-09)

- [x] **Routine 1** (v1.0.0 daily terminology-regression sentinel) — **DEPRECATED** 2026-05-09
- [x] **Routine 1'** (cross-thread state-snapshot, every other day) — **RATIFIED + SCHEDULED** 2026-05-09 — `trig_016fusGEFZV49uaWfRXNBPTT`
- [x] **Routine 2** (weekly pre-submission readiness, refined) — **RATIFIED + SCHEDULED** 2026-05-09 — `trig_018z7Dkcrw7R9Br25rvmCnTD` (re-purposed in-place from v1.0.0 Routine 2 trigger)
- [x] **Routine 3** (v1.0.0 weekly rigor pass status tracker) — **DEFERRED** 2026-05-09
- [x] **Routine 3'** (weekly branch hygiene scan) — **RATIFIED + SCHEDULED** 2026-05-09 — `trig_01AcETfMQs2kD8vyvuKK5Arw`
- [x] **Routine 4** (v1.0.0 weekly Open Insights status sync) — **DEFERRED** 2026-05-09
- [x] **Routine 4'** (weekly stale-reference scan) — **RATIFIED + SCHEDULED** 2026-05-09 — `trig_01Puk9mHXTRUT8UWVUjptd1S`

All four live routines run as remote agents on Anthropic cloud (environment `env_01PoHTUjJ2qNQv7D6qLjzQU1`), model `claude-sonnet-4-6`, allowed_tools `["Bash","Read","Write","Edit","Glob","Grep"]`, MCP connections cleared. Cron expressions are EDT-anchored — revisit at the November 2026 DST shift. Routine output appears as completed remote-agent runs in the routines panel at https://claude.ai/code/routines.

**DST shift reminder.** A one-shot remote agent is scheduled for 2026-10-25 at 6:30am ET (`trig_01DZSC4uF8nZwLGVb2Bv3Nq5`, `run_once_at: 2026-10-25T10:30:00Z`) to compute the EST-anchored cron rebases for all four routines and write a reminder note to `tools/routines/dst-shift-reminder_2026-11.md`. The author then decides which crons (if any) to rebase before the Sunday 2026-11-01 DST shift. The reminder agent does NOT modify routines.

---

## Update log

- **2026-04-28.** v1.0.0 drafted — four routines (daily terminology sentinel + weekly pre-submission audit + weekly rigor pass tracker + weekly Open Insights sync). Pending author ratification.
- **2026-05-09.** v2.0.0 in-place rewrite per author direction. v1.0.0 Routine 1 deprecated; Routine 2 ratified-with-refinement; Routines 3 + 4 deferred. New routines added: 1' (cross-thread state-snapshot, every other day), 3' (weekly branch hygiene scan), 4' (weekly stale-reference scan). Companion file `publishing/essays/_pipeline/cross-thread-todos.md` stood up same date.
- **2026-05-09 (later same day).** All four ratified routines (1', 2-refined, 3', 4') scheduled as live remote agents. Routine 2's existing v1.0.0 trigger re-purposed in-place with the refined prompt + new cron + MCP connections cleared. Refined Routine 2 prompt (previously "rewrite pending") drafted and inlined into this spec for traceability. v1.0.0 Routine 2 prompt remains recoverable from git history.
- **2026-05-09 (third pass, same day).** All four routines unified to a 6:30am ET cadence (cron-time refresh per author direction): 1' every other day, 2 Mondays, 3' Fridays, 4' Sundays — all firing at 30 minutes past 10am UTC during EDT season. Auto-attached Gmail + Google Drive MCP connections stripped from Routines 1', 3', 4' (Routine 2 already cleared on initial scheduling). DST-shift reminder one-shot scheduled for 2026-10-25 6:30am ET (`trig_01DZSC4uF8nZwLGVb2Bv3Nq5`) to surface the EST-anchored cron rebase punch list one week ahead of the 2026-11-01 DST shift. Confirmed v1.0.0 Routines 3 + 4 disabled triggers are gone (HTTP 404 on get).

---

*v2.0.0 revised 2026-05-09. v1.0.0 (2026-04-28) recoverable from git history.*
