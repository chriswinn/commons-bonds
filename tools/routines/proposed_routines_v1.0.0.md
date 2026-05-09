# Commons Bonds — Routines (v2.0.0)

**Version:** 2.0.0
**Date:** 2026-05-09 (revised from v1.0.0 2026-04-28)
**Status:** RATIFIED 2026-05-09 — Routine 1' + Routine 3' + Routine 4' new; Routine 2 ratified-with-refinement; v1.0.0 Routines 1, 3, 4 deprecated/deferred per author direction
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
| **1' — Cross-thread state-snapshot** | Every other day, 3pm ET | Survey branches; flag stale references + open cross-thread TODOs; replaces Routine 1's slot |
| **3' — Branch hygiene scan** | Weekly Friday 5pm ET | Surface branch-sprawl candidates for retirement; pre-empt the rescue-from-frozen-sessions pattern |
| **4' — Stale-reference scan** | Weekly Sunday 8pm ET | Punch-list of broken cross-references in publishing-strategy + manuscript-essay artifacts |

---

## Routine 1' — Cross-thread state-snapshot

**Purpose.** Every other day, surface what's changed across the project since the last snapshot — what landed on main, what's in flight on which feature branches, what stale references have accumulated, what cross-thread TODOs are open. Replaces v1.0.0 Routine 1 (daily terminology-regression sentinel) which has low marginal value post-vocabulary-stabilization.

**Cadence.** Every other day at 3pm ET. Cron: `0 15 */2 * *`

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
   - publishing/strategy/cascade-plan_2026-05-06.md
   - publishing/strategy/decisions-log.md
   - publishing/strategy/rights-register.md
   - publishing/strategy/cross-thread-todos.md
   - manuscript/essay/Noema/rewrite-plan_2026-05-01.md
   - manuscript/essay/Noema/noema-essay-drafting-plan_*.md
   - manuscript/essay/aeon/aeon-submission-strategy_*.md
   - For each markdown file path or commit hash referenced in those artifacts, verify the target exists / commit is reachable. Flag candidates whose target was renamed/moved/deleted.

4. Read publishing/strategy/cross-thread-todos.md
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
- (Pull from publishing/strategy/cross-thread-todos.md "Open" section; flag overdue items.)

### Recommended actions
- (1-3 highest-priority items to address based on the above.)

Snapshot run YYYY-MM-DD at HH:MM. Next run: day-after-tomorrow 3pm ET.
```

**Expected output:** ~½-page state-snapshot suitable for morning-coffee review. Picks up drift between branches before it accumulates into rescue-from-frozen-sessions territory.

---

## Routine 2 (refined) — Weekly pre-submission readiness audit (lighter scope)

**Purpose.** Catch publication-readiness blockers in chapters in active polish + Ch 3 (the only undrafted chapter as of 2026-05-09). Drops the comprehensive notation-collision sweep (mostly stable post-Insight #21 closure 2026-05-04).

**Cadence.** Weekly Monday 8am ET. Cron: `0 8 * * 1`

**Refinements from v1.0.0:**
- Scope reduced: only chapters in active polish + Ch 3 (previously: all 10 chapters every week).
- Drop the framework-wide notation-collision sweep (Insight #21 closed; stable until Phase 3 Tech Appendix rebuild lands).
- Length tracking softened: per "substance drives length" discipline (per session-handoff v1.51.0+), don't flag for "under target" if substance is complete; only flag for "substantially over target" with magnitude.
- Add manuscript-completion-rate metric: % chapters READY for submission across the 10-chapter scope.

**Full prompt rewrite pending** — to be drafted on first ratified scheduling. Target: similar structure to v1.0.0 spec but with reduced scope per refinements above.

---

## Routine 3' — Branch hygiene scan

**Purpose.** Weekly Friday afternoon scan of all `claude/*` remote branches; surface branch-sprawl candidates for retirement; pre-empt the rescue-from-frozen-sessions pattern that emerged when ~8 branches accumulated unmerged work.

**Cadence.** Weekly Friday 5pm ET. Cron: `0 17 * * 5`

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

Scan run YYYY-MM-DD. Next run: Friday next week 5pm ET.
```

**Expected output:** brief table + closing summary. Friday afternoon timing aligns with end-of-week project rhythm; gives author a digest before weekend.

---

## Routine 4' — Stale-reference scan

**Purpose.** Weekly scan for broken or outdated cross-references in publishing-strategy + manuscript-essay artifacts. Catches: file paths whose target was renamed/moved/deleted; references to versions/decisions superseded but not updated; "resolved" decisions not yet struck through; outdated Date-modified fields.

**Cadence.** Weekly Sunday 8pm ET. Cron: `0 20 * * 0`

**Prompt:**

```
You are running a weekly stale-reference scan for the Commons Bonds book project at /Users/c17n/commons-bonds.

Targets (canonical living artifacts):
- publishing/strategy/*.md
- publishing/book-proposal/*.md
- publishing/agents/*.md
- publishing/essay-drafts/templates/*.md
- manuscript/essay/Noema/rewrite-plan_*.md
- manuscript/essay/Noema/noema-essay-drafting-plan_*.md
- manuscript/essay/aeon/aeon-submission-strategy_*.md
- manuscript/essay/aeon/aeon-essay-dunbar-aside-drafts_*.md
- alignment/sessions/commons-bonds-session-handoff-*.md (latest only)
- tools/routines/proposed_routines_*.md
- research/outreach/_pipeline/*.md
- research/outreach/_protocols/*.md

Checks:

1. **Broken file-path references.** Extract `[text](path/to/file)` markdown links and inline `` `path/to/file.md` `` patterns. Verify each target exists at the cited path. Flag missing.

2. **Stale path references after restructure.** Specific patterns to check:
   - `research/outreach/<subject>-<artifact>` (flat-path pattern; should now be `research/outreach/subjects/<subject>/<artifact>` post-2026-05-09 restructure)
   - `publishing/essay-drafts/draft2.md` (archived 2026-05-08; should now be at `archive/_OneDayMaybe/withdrawn-essays/draft2_withdrawn-noema_2026-05-01.md`)
   - `manuscript/essay/aeon/aeon-pitch-commons-bonds-winn_VERSION-B_alternate-frame.md` (deleted 2026-05-08; superseded by Version C)

3. **Stale version references.** Check for "Version A" / "Version B" references in Aeon-context artifacts (Version C is the locked submission cut as of 2026-05-08).

4. **Resolved-decision markers.** Items in "Decisions due" or "Open" sections that are actually resolved per decisions-log/git history. Cross-check against:
   - publishing/strategy/decisions-log.md latest entries
   - publishing/strategy/cross-thread-todos.md "Resolved" section

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

Scan run YYYY-MM-DD. Next run: Sunday next week 8pm ET.
```

---

## Implementation order recommendation (v2.0.0)

If implementing all three new routines + refining Routine 2:

1. **Routine 1' first** (cross-thread state-snapshot, every other day) — highest expected leverage; replaces deprecated Routine 1 slot. Stand up immediately.
2. **Routine 4'** (stale-reference scan, weekly Sunday) — second-highest leverage; addresses path/reference drift. Stand up after 1 week of Routine 1' output validates the cadence.
3. **Routine 3'** (branch hygiene scan, weekly Friday) — useful if branch sprawl continues. Stand up if the rescue-from-frozen-sessions pattern recurs.
4. **Refine Routine 2** (lighter scope) — when convenient; full prompt rewrite needed before next Monday-morning run.
5. Re-evaluate v1.0.0 deferred Routines (3 + 4) after Phase 3 Tech Appendix rebuild lands.

---

## Author ratification status (updated 2026-05-09)

- [x] **Routine 1** (v1.0.0 daily terminology-regression sentinel) — **DEPRECATED** 2026-05-09
- [x] **Routine 1'** (cross-thread state-snapshot, every other day) — **RATIFIED** 2026-05-09; scheduling pending
- [x] **Routine 2** (weekly pre-submission readiness, refined) — **RATIFIED with refinement** 2026-05-09; full prompt rewrite pending before next scheduled run
- [x] **Routine 3** (v1.0.0 weekly rigor pass status tracker) — **DEFERRED** 2026-05-09
- [x] **Routine 3'** (weekly branch hygiene scan) — **RATIFIED** 2026-05-09; scheduling pending
- [x] **Routine 4** (v1.0.0 weekly Open Insights status sync) — **DEFERRED** 2026-05-09
- [x] **Routine 4'** (weekly stale-reference scan) — **RATIFIED** 2026-05-09; scheduling pending

Once scheduling tooling is configured, routine output appears as completed remote-agent runs in the routines panel; reviewable when ready.

---

## Update log

- **2026-04-28.** v1.0.0 drafted — four routines (daily terminology sentinel + weekly pre-submission audit + weekly rigor pass tracker + weekly Open Insights sync). Pending author ratification.
- **2026-05-09.** v2.0.0 in-place rewrite per author direction. v1.0.0 Routine 1 deprecated; Routine 2 ratified-with-refinement; Routines 3 + 4 deferred. New routines added: 1' (cross-thread state-snapshot, every other day), 3' (weekly branch hygiene scan), 4' (weekly stale-reference scan). Companion file `publishing/strategy/cross-thread-todos.md` stood up same date.

---

*v2.0.0 revised 2026-05-09. v1.0.0 (2026-04-28) recoverable from git history.*
