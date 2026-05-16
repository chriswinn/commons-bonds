# commons-bonds — project notes for Claude Code sessions

## Workflow defaults

### Branch discipline + merge-to-main

Each workstream operates on a dedicated feature branch
(`claude/<workstream>-<harness-id>`) branched from current
`origin/main`. See `tools/workstream-handoffs/README.md` for the
canonical branch-discipline reference.

**Merge-to-main default (established 2026-05-16 by author
direction; extended to rigor-pass artifacts 2026-05-16).**
Sessions that complete *author-ratified content changes* — Phase C
spot-fix application sessions, chapter-text edits ratified by the
author before the session begins, and similar work where the
author has explicitly approved the change set ahead of the
session — autonomously fast-forward merge their feature branch
into `main` and push `origin/main` at session close, instead of
stopping at the feature branch.

Rigor-pass artifacts (Stage-3 fact-check / voice-polish /
audience-load passes at any of the three passes; Stage-2
audience-blind drafts; audit findings prior to author
disposition) **also autonomously fast-forward merge to `main` at
session close.** Rationale: these artifacts are internal
scaffolding that propose spot-fixes rather than apply them; the
chapter file under audit is unchanged, so merging the rigor-pass
artifact to `main` does not commit any content change ahead of
author ratification. Author ratification still gates Phase C
spot-fix application (which is a separate session).

Sessions producing *direct content edits without prior author
ratification* continue to stop at feature branch and wait for
explicit author merge.

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
`feedback_named_subject_consent.md` memory. Named subjects with
historical-record status (deceased; matter of public record) do
not require consent gating. Living named subjects require
explicit author confirmation before naming in publisher-facing
prose.
