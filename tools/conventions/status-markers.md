# Status-marker conventions

Codified 2026-05-28 per project-review S7 recommendation. Single reference for the status markers used across the commons-bonds repo — file-header status fields, rigor-pass filename conventions, directory-name tags, commit-message prefixes, PM dashboard emoji labels, and state-transition rules.

The conventions are descriptive (what we already do) more than prescriptive (what we should start doing). Where the convention diverges from current practice, the divergence is called out explicitly.

## File-header status field

Markdown artifacts in the rigor pipeline carry a `**Status:**` line near the top (typically line 2-5, after the `# Title` heading + Date line). Status values:

| Value | Meaning |
|---|---|
| `PROPOSED` | Artifact drafted; awaiting author ratification. Not yet load-bearing for downstream sessions. |
| `RATIFIED` | Author has ratified. Load-bearing. For prose passes, spot-fixes have been applied (or are queued in a follow-up apply session). |
| `RATIFIED-AWAITING-SUBMIT` | Specific to per-essay packages. All passes ratified, cover letter drafted, Stage 5 sign-off RATIFIED — waits only for the author submission action (portal upload / email send). |
| `SUBMITTED` | Sent to publisher / agent / editor. Awaiting their response. |
| `PLACED` | Accepted by venue. Editor-iteration may follow. |
| `REJECTED` | Declined by venue. Artifact archives. |
| `WITHDRAWN` | Pulled by author before decision. Artifact archives. |
| `SUPERSEDED` | Replaced by a newer version (different file). Original retained for lineage. |
| `HELD` | Pass-internal verdict: no spot-fixes needed; carry-forward only. Distinct from RATIFIED in that no Phase C application follows. |

Format precedent (verbatim copy-pasteable):

```markdown
**Status:** RATIFIED 2026-05-27 — READY-TO-SUBMIT. <free-text context>.
```

Multi-value composite is acceptable (e.g. `RATIFIED-AWAITING-SUBMIT`); separate two values with em-dash + space when both apply.

## Rigor-pass filename conventions

### Per-essay rigor (post-2026-05-28 consolidation)

Inside `publishing/essays/<venue>/rigor/`, filenames are flat:

| Pattern | Used for |
|---|---|
| `stage-1-brief.md` | Stage 1 ready-to-draft brief. |
| `pass-3-1-fact-check.md` | Stage 3 Pass 3.1 fact-check audit. |
| `pass-3-2-voice-polish.md` | Stage 3 Pass 3.2 voice-polish audit. |
| `pass-3-3-audience-load.md` | Stage 3 Pass 3.3 audience-load acceptance. |
| `pass-3-4-adversarial.md` | Stage 3 Pass 3.4 adversarial robustness. |
| `pass-3-5-developmental-edit.md` | Stage 3 Pass 3.5 developmental-edit. |
| `stage-4-render-audit.md` | Stage 4 render + character-integrity audit. |
| `pre-pub-review-queue.md` | Pre-publication external-review queue artifact. |
| `light-refires/pass-3-3-light-refire_<DATE>.md` | Post-Phase-C light re-fire records. |

Per-essay context disambiguates; no `commons_bonds_rigor_pass_<DATE>_<slug>_` prefix needed.

### Cross-essay + chapter-side rigor

`tools/rigor-passes/` retains the longer convention:

```
commons_bonds_rigor_pass_YYYY-MM-DD_<slug>_<stage>_v#_#_#.md
```

Examples:
- `commons_bonds_rigor_pass_2026-05-24_wave_2_derivative_planning_stage_0_v1.0.0.md`
- `commons_bonds_ch5_stage3_pass_3_4_audience_load_robustness_2026-05-18.md`

When a per-essay artifact would be ambiguous because multiple essays contribute, it stays in `tools/rigor-passes/` rather than a per-essay folder.

## Directory-name tags

Per `publishing/essays/README.md` §Status tags:

| Pattern | Meaning |
|---|---|
| `<venue>-<short-title>/` | Active package: drafting / pre-submission / RATIFIED-AWAITING-SUBMIT. |
| `<venue>-<short-title>_SUBMITTED-<YYYY-MM-DD>/` | Submitted; awaiting editor response. Rename on submission. |
| `<venue>-<short-title>_PLACED-<YYYY-MM-DD>/` | Accepted by venue. Editor-iteration may follow. |
| `_archive/<venue>-<short-title>_REJECTED-<YYYY-MM-DD>/` | Declined; moved to archive subdir. |
| `_archive/<venue>-<short-title>_WITHDRAWN-<YYYY-MM-DD>/` | Withdrawn by author; moved to archive subdir. |

Rename via `git mv` so history is preserved. The `<date>` is the day the state transition occurred, not the day the rename was performed.

**As-of 2026-05-28**: no essay packages currently carry the `_SUBMITTED-` / `_PLACED-` / etc. suffixes — they're convention-ready but not yet exercised. First use will set the rename pattern in stone.

## Commit-message prefixes

There is no enforced commit-prefix convention. Observed patterns in current `git log`:

- Bare imperative: `Per-essay rigor consolidation — boston-review Phase B file moves`
- Workstream-tagged: `Structure cleanup S6 — pipeline-doctrine subdir consolidation`
- Stage-tagged with status: `Ch 4 → Foreign Affairs Stage 5 sign-off — RATIFIED 2026-05-27`

Recommendation (NOT YET ENFORCED): for end-user-facing prose ratifications, include the venue + chapter + stage + status in the subject line so cross-essay portfolio reviews can grep `git log --oneline` cleanly. For internal scaffolding, the workstream name + sub-task identifier (e.g. `Structure cleanup S6`) is sufficient.

### Merge-on-ratification escape-hatch markers

Per `feedback_merge_on_ratification.md`, two commit-message **body** markers (not subject-line prefixes) retain explicit-hold behavior:

| Marker | Body-line format | Effect |
|---|---|---|
| `MERGE-HOLD` | `MERGE-HOLD: <reason>` | Session pushes to feature branch only; `origin/main` is not touched. |
| `MERGE-AFTER` | `MERGE-AFTER: <gate-description>` | Session waits for the named gate before merging. |

Default (no marker) is merge-on-ratification per `CLAUDE.md` §"Branch discipline + merge-to-main".

## PM dashboard emoji markers

Per `feedback_pm_dashboard_structure.md` §Priority labels + observed usage in `tools/workstream-handoffs/pm-session-handoff_*.md`:

| Emoji | Meaning |
|---|---|
| 🔴 | HIGH priority — time-pressured (hard deadline within ~30d) OR gates large downstream cascade. Also used for TODAY action drivers. |
| 🟡 | MEDIUM priority — important but not yet gating; no near-term hard deadline. Used for "this week" action drivers. |
| 🟢 | LOW priority — small / dormant / waiting on conditional trigger. Also used as "PIPELINE-READY" state indicator. |
| 🔵 | Parallel track — denotes workstream running concurrently with the primary thread. |
| 🟣 | Cross-cutting / cross-workstream — denotes work that touches multiple chapters or essays. |
| ⏳ | Waiting / blocked — external dependency or author-action gate. |
| ✅ | Completed — state transition closed; no further action expected. |

Section-header pattern: `### 🔴 TODAY <weekday> <month> <day>` for top-of-mind action driver; `### 🟡 <date>` for medium-priority forward-look.

## State-transition diagram

Allowed transitions:

```
PROPOSED ──ratify──> RATIFIED ──submit──> SUBMITTED ──┬─accept──> PLACED ──> (editor-iteration)
   │                    │                              ├─reject──> REJECTED
   │                    │                              └─withdraw> WITHDRAWN
   │                    │
   │                    ├──supersede──> SUPERSEDED (new version supersedes; old file retained)
   │                    └──no-changes──> HELD (pass-internal; no Phase C application)
   │
   └──discard──> (deleted; no terminal state)
```

**Specific rules:**

- `PROPOSED` may only transition to `RATIFIED` (after author ratification) or be discarded entirely. Direct `PROPOSED → SUBMITTED` is not permitted; submission requires ratification first.
- `RATIFIED → RATIFIED-AWAITING-SUBMIT` is a sub-state transition specific to per-essay packages, signaling that Stage 5 sign-off has fired and only the author submission action remains.
- `RATIFIED → SUBMITTED` requires the author to actually submit (portal click / email send). Sessions do not transition this state autonomously.
- `SUBMITTED → PLACED` / `REJECTED` / `WITHDRAWN` are terminal-ish; subsequent activity moves to the `editor-iteration/` workflow (PLACED) or the archive (REJECTED / WITHDRAWN).
- `RATIFIED → SUPERSEDED` is a documentation-only transition; the new version lives in a different file, and the old file's Status line updates from `RATIFIED` to `SUPERSEDED`.
- `HELD` is a pass-verdict terminal state — no further state transition for that pass. The pass record carries `HELD` permanently; the next pass in the cascade fires normally.

## Cross-references

- `CLAUDE.md` §"Branch discipline + merge-to-main" — full discipline for end-user-facing prose vs internal scaffolding + merge-on-ratification rule.
- [`../memory/feedback_merge_on_ratification.md`](../memory/feedback_merge_on_ratification.md) — full ratification of the merge-on-ratification rule with empirical anchors.
- [`../memory/feedback_pm_dashboard_structure.md`](../memory/feedback_pm_dashboard_structure.md) — PM dashboard structure v2.0 (priority labels, bucket order, section structure).
- [`../../publishing/essays/README.md`](../../publishing/essays/README.md) — per-essay directory layout + status tags (Q3 + Q10 ratification 2026-05-24).
- [`../pipeline-doctrine/`](../pipeline-doctrine/) — full pipeline doctrine (stages 0-5 + amendments).
- [`../memory/feedback_rigor_vs_bookkeeping_distinction.md`](../memory/feedback_rigor_vs_bookkeeping_distinction.md) — distinguishing rigor-cascade work from handoff/filing bookkeeping in PM recommendations.
