# commons-bonds — project notes for Claude Code sessions

## Workflow defaults

### Branch discipline + merge-to-main

Each workstream operates on a dedicated feature branch
(`claude/<workstream>-<harness-id>`) branched from current
`origin/main`. See `tools/workstream-handoffs/README.md` for the
canonical branch-discipline reference.

**Merge-to-main default (established 2026-05-16 by author
direction; extended to rigor-pass artifacts 2026-05-16; extended
to all internal scaffolding 2026-05-24).**

The boundary that matters: **end-user-facing prose** vs.
**internal scaffolding**.

**End-user-facing prose** (changes require author ratification
BEFORE merge to main):

- `manuscript/chapters/` — book chapter prose
- `manuscript/essay/` — derivative-essay prose (Aeon, Noema, BR,
  PW, Atlantic Ideas, Wave 2 candidates, etc.)
- `publishing/op-eds/` — op-ed canonical drafts (news-peg
  activation variants in dated sibling files are derivatives)
- `publishing/book-proposal/` — proposal prose (agent/editor-
  facing)
- Outreach packet content that will be sent to subjects (Sandy,
  Colden, CBF, etc.)
- Cover letters / pitch emails attached to submissions
- Anything that goes out the door to anyone other than the author

Apply changes to these files via Phase C application sessions
where the author is present + ratifying. Until author ratifies,
these files DO NOT update on origin/main.

**Internal scaffolding** (all autonomously fast-forward merges
to main at session close):

- `tools/rigor-passes/` — rigor-pass artifacts at any stage
  (PROPOSED, RATIFIED, decision artifacts, audit findings)
- `tools/workstream-handoffs/` — PM dashboards, workstream
  handoffs, paste-text bundles, kick-off scaffolds
- `tools/memory/` — memory entries (feedback, reference,
  project)
- `tools/drafting-templates/` — templates, scaffolds, generic
  drafting-trigger paste-texts
- `tools/quality-gates/`, `tools/scripts/`, `tools/audits/` —
  pipeline infrastructure
- `publishing/strategy/` — cascade plans, decisions logs,
  cross-thread-todos, submission schedules
- `research/` — research notes, outreach packet DRAFTS (before
  send), background briefs, literature notes
- `alignment/` — working principles, framework positioning
  documents
- `archive/` — historical record
- README files, documentation, `CLAUDE.md` itself
- Anything that only the author will ever see

Rationale (extended 2026-05-24): the risk of losing work by
forgetting to push is bigger than the risk of pushing premature
internal scaffolding to main, since only the author sees
internal scaffolding and any issue can be iterated again. The
irreversibility (and reputational stake) lives at the end-user-
facing-prose boundary — once shipped, you cannot easily un-ship.
Internal scaffolding is iterable indefinitely; main is the
durable record of where the scaffolding currently sits.

**Per-session protocol:** at session close, the session
classifies its commits and auto-merges the internal-scaffolding
commits to main. End-user-facing prose commits stay on the
feature branch until the author ratifies and explicitly merges.

**Active-push expectation (from 2026-05-10).** As ratified
chunks complete, push them promptly — don't accumulate ratified
work on the feature branch waiting for explicit "push now."
Default behavior is push-on-chunk-completion.

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
