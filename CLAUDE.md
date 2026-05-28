# commons-bonds — project notes for Claude Code sessions

## Workflow defaults

### Branch discipline + merge-to-main

Each workstream operates on a dedicated feature branch
(`claude/<workstream>-<harness-id>`) branched from current
`origin/main`. See `tools/workstream-handoffs/README.md` for the
canonical branch-discipline reference.

**Merge-to-main default (established 2026-05-16 by author
direction; extended to rigor-pass artifacts 2026-05-16; extended
to all internal scaffolding 2026-05-24; extended to end-user-facing
prose via merge-on-ratification 2026-05-28).**

The boundary that matters: **end-user-facing prose** vs.
**internal scaffolding**. Both auto-merge to main; the difference
is the trigger event (author-ratification for prose; session-close
for scaffolding) and the escape-hatch syntax.

**End-user-facing prose** (auto-merges on author ratification per
the merge-on-ratification rule 2026-05-28; supersedes the
2026-05-16 explicit-merge gate):

- `manuscript/chapters/` — book chapter prose
- `publishing/essays/<venue>/essay.md` + `cover-letter.md` —
  derivative-essay prose + cover notes (Aeon, Noema, BR, PW,
  Atlantic Ideas, $100 Barrel, Berggruen, Wave 2 candidates,
  etc.). Per-essay submission packages.
- `publishing/essays/<venue>/editor-iteration/` — post-acceptance
  editor-round artifacts (NEW class, 2026-05-28; subdir per round).
- `publishing/op-eds/<slug>/op-ed.md` — op-ed canonical drafts
  (news-peg activation variants in dated sibling files inside the
  per-op-ed directory are derivatives)
- `publishing/book-proposal/` — proposal prose (agent/editor-
  facing)
- `publishing/agents/<agent-slug>/query-letter.md` +
  `correspondence/` — outbound literary-agent communication
- Outreach packet content that will be sent to subjects (Sandy,
  Colden, CBF, etc.) under `research/outreach/subjects/<name>/`
- Anything that goes out the door to anyone other than the author

**Merge-on-ratification rule (2026-05-28 — supersedes the
2026-05-16 explicit-merge gate).** When the author ratifies an
end-user-facing prose change (Phase C application of a rigor-pass
spot-fix; Pass 3.5 developmental-edit; Stage 4 render audit apply;
Stage 5 sign-off; cover-letter ratification; editor-round response;
etc.), the ratification IS the merge authorization. The session
pushes the ratified commit to `origin/main` via the pre-push
reconciliation pattern immediately after the Phase C apply, same
mechanism as internal scaffolding.

Rationale: the prior 2026-05-16 "explicit author authorization
before merge" default interacted poorly with the 2026-05-10
active-push expectation and with the 2026-05-26 parallel-session-
volume reality (20-35+ concurrent sessions). Sessions had no clear
handoff between "ratified" and "merge-ready"; the practical result
was ratified prose stranded on feature branches indefinitely. The
2026-05-27 Foreign Affairs essay situation (6,065w essay + cover
letter + Stage 5 RATIFIED, sitting unmerged for ~6 hours until the
cross-essay portfolio review surfaced it, requiring an explicit
"merge end-user-facing prose to main per author authorization"
commit `3ae1777`) is the empirical anchor. See
[`tools/memory/feedback_merge_on_ratification.md`](tools/memory/feedback_merge_on_ratification.md)
for the full discipline + worked examples.

What still requires explicit author action (UNCHANGED): SUBMISSION
itself — sending the essay to the publisher / agent / editor;
pressing submit on the portal; emailing the editor. Landing on
`origin/main` is NOT shipping. It is syncing canonical repo state.
The actual ship gate is the submission portal click / email send,
entirely author-controlled regardless of merge-to-main policy.

**Escape hatches.** Two commit-message markers retain explicit-hold
behavior for the rare cases where merge-on-ratification is wrong:

- `MERGE-HOLD: <reason>` — session pushes to feature branch only;
  main is not touched. Use when you want to inspect the merged
  state before further sessions touch the file, or coordinate
  multiple parallel sessions on the same file. Author surfaces a
  follow-up merge authorization when the hold reason clears.
- `MERGE-AFTER: <gate-description>` — session waits for the named
  gate before merging. Use for "merge once X also ratifies" cross-
  session coordination.

Both markers go in the commit message body (not the subject line)
and the session's per-session-protocol scan inspects them before
the auto-merge step.

**Internal scaffolding** (all autonomously fast-forward merges
to main at session close — UNCHANGED):

- `tools/rigor-passes/` — rigor-pass artifacts at any stage
  (PROPOSED, RATIFIED, decision artifacts, audit findings).
  **NB:** per the per-essay rigor consolidation pattern established
  2026-05-28, per-essay rigor-pass artifacts are migrating into
  `publishing/essays/<venue>/rigor/` subdirs. After migration,
  `tools/rigor-passes/` will hold only chapter-side + cross-essay
  rigor; per-essay rigor history travels with the essay package.
- `tools/workstream-handoffs/` — PM dashboards, workstream
  handoffs, paste-text bundles, kick-off scaffolds
- `tools/memory/` — memory entries (feedback, reference,
  project)
- `tools/drafting-templates/` — templates, scaffolds, generic
  drafting-trigger paste-texts
- `tools/quality-gates/`, `tools/scripts/`, `tools/audits/` —
  pipeline infrastructure
- `publishing/essays/<venue>/rigor/` — per-essay rigor-pass
  history (migrated from `tools/rigor-passes/` per 2026-05-28
  consolidation pattern; co-located with the essay package for
  editor-iteration phase + dashboard lookup ease)
- `publishing/essays/_pipeline/` — cascade plans, decisions logs,
  cross-thread-todos, submission schedules
- `research/` — research notes, outreach packet DRAFTS (before
  send), background briefs, literature notes
- `alignment/` — working principles, framework positioning
  documents
- `archive/` — historical record
- README files, documentation, `CLAUDE.md` itself
- Anything that only the author will ever see

Rationale (extended 2026-05-24; reinforced 2026-05-28): the risk
of losing ratified work by forgetting to merge is bigger than the
risk of pushing prematurely, since (a) only the author sees
internal scaffolding and any issue can be iterated again, and (b)
landing on `origin/main` is not shipping — submission is. The
irreversibility (and reputational stake) lives at the SUBMISSION
boundary, not the merge-to-main boundary. Pre-2026-05-28 the
boundary was mis-located at merge-to-main; 2026-05-28 relocates
it to submission, where it always belonged.

**Per-session protocol:** at session close, the session
classifies its commits and auto-merges all ratified commits to
main per the merge-on-ratification rule. Commits flagged with
`MERGE-HOLD` or `MERGE-AFTER` remain on the feature branch until
the hold clears or the gate fires.

**Active-push expectation (from 2026-05-10; reinforced 2026-05-28).**
As ratified chunks complete, push them promptly — don't accumulate
ratified work on the feature branch waiting for explicit "push
now." With merge-on-ratification now applying to both prose and
scaffolding, there is no class of commits that "wait for explicit
merge"; the default is push-on-ratification-completion for both
classes.

**Pre-push reconciliation pattern.** Before fast-forwarding to
main, `git fetch origin main` and `git rebase origin/main` to
inherit any parallel-session work. If a parallel session
resolved or contradicts something in the chunk being pushed,
add a small reconciliation commit so what lands on main is
consistent. Then push.

Hard constraints (recurring): never force-push `main`; never
amend a commit already on `origin/main`; never skip hooks
(`--no-verify`) without explicit author direction.

### Three-pass rigor discipline

v2.0 Amendment B: fact-check + voice-polish + audience-load are
three DISTINCT passes, not bundled. Per-prompt serial cadence
(Pass-1 → spot-fix → Pass-2 → spot-fix → Pass-3 → spot-fix per
chapter). See `tools/drafting-templates/stage-3-three-pass-rigor-audit.md`
for the canonical template + `tools/rigor-passes/commons_bonds_rigor_pass_2026-05-13_ch1_the_quiet_math_stage3_voice_polish_v1.0.0.md`
for the canonical Pass-2 artifact format model.

### Named-subject consent

Confirmed individuals only; see
`tools/memory/feedback_named_subject_consent.md`. Named subjects
with historical-record status (deceased; matter of public record)
do not require consent gating. Living named subjects require
explicit author confirmation before naming in publisher-facing
prose.

## Project memory (cross-session discipline)

The project's cross-session discipline registry lives at
[`tools/memory/`](tools/memory/) (index at
[`tools/memory/README.md`](tools/memory/README.md)). Selective always-load
files:

@tools/memory/feedback_audience_aware_drafting_discipline.md
@tools/memory/feedback_named_subject_consent.md
@tools/memory/feedback_verify_stale_memory_claims.md

Remaining files in `tools/memory/` are situational; load when relevant via
the README index.

The local `~/.claude/projects/-Users-c17n-commons-bonds/memory/` directory
remains the default laptop-session memory layer. `tools/memory/` is the
in-repo mirror so mobile sessions + future collaborators can read the
discipline registry from the repo.
