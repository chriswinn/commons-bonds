# Ch 2 → Harper's Magazine — Stage 3 Pass 3.1 (fact-check) — kickoff paste-text

**Date staged:** 2026-05-27
**Predecessor:** Stage 2 audience-blind draft RATIFIED 2026-05-27 (Phase C ratification session at agent worktree `agent-a3390c00c9b9a4df0`); essay.md at commit `55842a3` on feature branch `worktree-agent-a3390c00c9b9a4df0`; Stage 1 brief RATIFIED at `origin/main` commit `be87926` with §18.4 ratification record + Stage 1a CLEAN BASELINE artifact at `tools/quality-gates/clean-baselines/ch2_harpers_stage1a_2026-05-27.md`; PC-4 ratification artifact + PC-5 forward-flag dispositions at `publishing/essays/harpers-the-miner/stage-2-ratification-2026-05-27.md` on feature branch.
**Status:** STAGED. Author fires Pass 3.1 in a fresh CC session by pasting the body block below.
**Internal scaffolding** per CLAUDE.md merge-to-main policy — this paste-text file fast-forwards to main at session close (lands via temp-worktree cherry-pick alongside other scaffolding commits per the worked pattern from Phase C 2026-05-27 cited in `tools/memory/feedback_worktree_isolation_for_parallel_sessions.md` v1.0.1 empirical anchor).

---

## Resume marker (for parent orchestration session at `worktree-ch2-harpers-pipeline-orchestration`)

- **Pass 3.1 artifact expected at:** `publishing/essays/harpers-the-miner/rigor/pass-3-1-fact-check.md` (PROPOSED at session start → RATIFIED + APPLIED at session close per Amendment C Interactive Ratification Protocol).
- **Essay artifact carrying Pass 3.1 spot-fixes:** `publishing/essays/harpers-the-miner/essay.md` (post-Pass-3.1 state lands on a fresh feature branch off `origin/main` per worktree-isolation discipline — typical naming `claude/ch2-harpers-pass3-1-factcheck-<harness-id>`; the essay.md spot-fixes commit stays on that feature branch per CLAUDE.md end-user-facing-prose discipline).
- **Status to look for:** `STATE: RATIFIED + APPLIED` at session close → ready for Stage 3 Pass 3.2 voice-polish session firing (Pass 3.2 kickoff paste-text expected to land at `tools/workstream-handoffs/ch2-harpers-stage-3-pass-3-2-voice-polish-kickoff_2026-05-27.md` produced by the Pass 3.1 session per Wave 1 + Ch 4 precedent).

## Cross-references

- **Input artifacts (Pass 3.1 reads but does NOT modify the inputs themselves):**
  - Stage 2 audience-blind draft: `publishing/essays/harpers-the-miner/essay.md` (feature branch `worktree-agent-a3390c00c9b9a4df0` commit `55842a3`; 7,216w body; 8 sections per brief §4)
  - Stage 1 brief §7 canonical-facts inventory: `publishing/essays/harpers-the-miner/rigor/stage-1-brief.md` §7 (Amendment A canonical fact-ground; §7.1 Kennedy + §7.2 McDowell demographics + §7.3 Bailey + §7.4 Latusek + §7.5 Lilly+Hamby + §7.6 Black Lung Trust Fund + §7.7 SMCRA + §7.8 Purdue/Sackler/Big Three + §7.9 Mazzucato+Harvey + §7.10 regional-scholarship + §7.11 out-of-scope inventory)
  - Source chapter for fact-verification only (NOT for paraphrase per brief §6 Path B preemptive policy): `manuscript/chapters/Chapter__2_TheMiner.md`
  - PC-4 ratification artifact (forward-flag inventory): `publishing/essays/harpers-the-miner/stage-2-ratification-2026-05-27.md` §3 + §3a (Pass-3.1-specific flags: §VI arithmetic-walk numerical anchors verification + §VII Purdue four-characteristic enumeration verification + Ch 10 RATIFIED-state §VIII coherence-awareness)
- **Methodology references:**
  - `tools/memory/feedback_audience_aware_drafting_discipline.md` v3.1 (Amendment A two-class cascade — Pass 3.1 is *automatic-on-edit* cascade; Amendment C Interactive Ratification Protocol — Pass 3.1 is prose-modifying so per-finding output uses Options + Recommendation + Reasoning, ratification + application combine in this same session)
  - `tools/memory/feedback_parallel_session_ratification_cadence.md` (one-finding-at-a-time presentation; status markers; end-of-session one-liner; ANTI-PATTERN A1 list-dump prohibition)
  - `tools/memory/feedback_worktree_isolation_for_parallel_sessions.md` v1.0.1 (worktree isolation + Edit/Write-tool-drift defense-in-depth)
- **Wave 1 Pass 3.1 format precedents (artifact-structure reference):**
  - `tools/rigor-passes/commons_bonds_rigor_pass_2026-05-22_boston_review_essay_stage3_pass_3_1_fact_check_v1.0.0.md` (BR institutional-measurement Pass 3.1 precedent)
  - `tools/rigor-passes/commons_bonds_rigor_pass_2026-05-22_100_barrel_essay_stage3_pass_3_1_fact_check_v1.0.0.md` ($100 Barrel Pass 3.1 sibling)
  - `tools/rigor-passes/commons_bonds_rigor_pass_2026-05-22_atlantic_ideas_essay_stage3_pass_3_1_fact_check_v1.0.0.md` (Atlantic Ideas Pass 3.1 sibling)
  - `publishing/essays/foreign-affairs-existence-proof/rigor/pass-3-1-fact-check.md` (Ch 4 → FA Pass 3.1 closest temporal sibling; same-day-as-this-staging precedent for cadence + commit pattern)

---

## Paste-text body (copy from "===" line below into fresh CC session)

```
===

You are running the Stage 3 Pass 3.1 fact-check session for the
Ch 2 *The Miner* → Harper's Magazine derivative essay. The Stage 2
audience-blind draft landed RATIFIED 2026-05-27 (Phase C ratification
session at agent worktree agent-a3390c00c9b9a4df0); essay.md at
commit 55842a3 on feature branch worktree-agent-a3390c00c9b9a4df0
(~7,216w body across 8 sections; first-person Option B frame; ring-1
concepts at plain-prose only; six brief-§6-permitted verbatim quotes
preserved). Your job is to audit the Stage 2 draft against the Stage
1 brief §7 canonical-facts inventory (Amendment A discipline) +
produce a per-finding fact-check artifact under v3.1 Amendment C
Interactive Ratification Protocol: per-finding output with Options
+ Recommendation + Reasoning; ratification + application combine
in this same session.

== Worktree-isolation FIRST ACTION ==

Create isolated worktree before any other tool call. Substitute
harness-id; the worktree path uses the WORKSTREAM slug
"ch2-harpers-pass3-1-factcheck":

```bash
HARNESS_ID="$(date +%y%m%d)-$(openssl rand -hex 3)"
WORKSTREAM="ch2-harpers-pass3-1-factcheck"
BRANCH="claude/${WORKSTREAM}-${HARNESS_ID}"
WORKTREE_PATH="/Users/c17n/commons-bonds-${WORKSTREAM}-${HARNESS_ID}"

git -C /Users/c17n/commons-bonds fetch origin main
git -C /Users/c17n/commons-bonds worktree add -b "${BRANCH}" "${WORKTREE_PATH}" origin/main

echo "Worktree-isolated at: ${WORKTREE_PATH}"
echo "Branch: ${BRANCH}"
```

After worktree add, ALL subsequent tool calls use absolute paths
under ${WORKTREE_PATH}. Construct Edit/Write tool calls against
the worktree root; do NOT hand-construct paths against
/Users/c17n/commons-bonds (see feedback_worktree_isolation v1.0.1
empirical anchor 2026-05-27 — Edit/Write-tool drift is the
distinct failure mode the SessionStart hook does NOT prevent).

== Access the Stage 2 essay (which lives on a different feature branch) ==

The Stage 2 essay.md lives on feature branch
worktree-agent-a3390c00c9b9a4df0 (commit 55842a3) — NOT on
origin/main, because end-user-facing-prose per CLAUDE.md does NOT
auto-merge to main. Access pattern from this Pass 3.1 worktree:

```bash
# Fetch the feature branch from local refs (it's already in .git/)
git -C "${WORKTREE_PATH}" fetch . worktree-agent-a3390c00c9b9a4df0:refs/heads/_stage2_input_readonly 2>&1 | tail -3 || \
  git -C "${WORKTREE_PATH}" fetch . refs/heads/worktree-agent-a3390c00c9b9a4df0:refs/heads/_stage2_input_readonly

# Cherry-pick the Stage 2 essay.md + README into this branch
# (gives you essay.md to spot-fix against; commits land on THIS feature
# branch, NOT on main — same end-user-facing-prose discipline)
git -C "${WORKTREE_PATH}" cherry-pick 55842a3 537258f 189a847
```

The three commits being cherry-picked: 55842a3 (Stage 2 draft
PROPOSED) + 537258f (PC-4 ratification artifact + README word-count
fix) + 189a847 (PC-5 forward-flag dispositions + README state field).
Cherry-pick order matches the feature-branch history. After
cherry-pick, your worktree has:
- publishing/essays/harpers-the-miner/essay.md (Stage 2 draft;
  pre-spot-fix; you'll modify this during Pass 3.1)
- publishing/essays/harpers-the-miner/README.md (per-essay package
  status — update at session close with Pass 3.1 status)
- publishing/essays/harpers-the-miner/stage-2-ratification-2026-05-27.md
  (PC-4/PC-5 ratification artifact — read for Pass-3.1-specific
  forward-flag inventory + §VI arithmetic-anchor verification list)

== Read in order ==

1. THIS paste (framing)

2. CLAUDE.md (workflow doctrine; merge-to-main policy extended
   2026-05-24; end-user-facing-prose vs internal-scaffolding
   boundary; branch discipline; pre-push reconciliation pattern;
   hard constraints — never force-push main; never amend a commit
   on origin/main; never skip hooks without explicit author
   direction)

3. tools/memory/feedback_audience_aware_drafting_discipline.md
   (v3.1 doctrine — Amendment A two-class cascade where Pass 3.1
   is automatic-on-edit; Amendment C per-finding interactive
   ratification artifact format)

4. tools/memory/feedback_parallel_session_ratification_cadence.md
   (status markers; per-finding cadence; severity-strict ordering
   HIGH → MED → LOW; end-of-session one-liner; ANTI-PATTERN A1
   list-dump prohibition)

5. tools/memory/feedback_worktree_isolation_for_parallel_sessions.md
   v1.0.1 (worktree isolation + Edit/Write-tool-drift defense)

6. tools/memory/feedback_named_subject_consent.md (Bailey + Latusek
   deceased + courtesy-notify-family discipline; Lilly + Hamby
   living-journalist public-record exception + citation-accuracy
   courtesy-notify protocol; closed at Stage 0 + brief §11 — do
   NOT re-litigate)

7. tools/memory/feedback_verify_stale_memory_claims.md (verification
   discipline for counts/dates/status/figures sourced from memory
   ≥3 days old)

8. **publishing/essays/harpers-the-miner/essay.md** — **THE ARTIFACT
   BEING AUDITED.** Read in full (~7,216w body; 8 sections per brief
   §4). Note structural sections: §I opening scene → §II Kennedy
   1960 → §III place-before-collapse → §IV Bailey → §V vocabulary
   (cost severance / severed cost / value extraction + Mazzucato +
   Harvey lineage + UMWA/BLA/Miners for Democracy) → §VI four-cost-
   component arithmetic → §VII Purdue second cycle → §VIII spatial
   cost severance + closing return + explicit-meta disarming close.

9. **publishing/essays/harpers-the-miner/rigor/stage-1-brief.md**
   — **CANONICAL FACT-GROUND.** RATIFIED 2026-05-27 commit be87926
   on origin/main; §18.4 ratification record at end. Load-bearing
   sections for Pass 3.1:
   - **§7 canonical-facts inventory (LOAD-BEARING; Amendment A
     discipline):** §7.1 Kennedy + §7.2 McDowell demographics +
     §7.3 Bailey + §7.4 Latusek + §7.5 Lilly+Hamby + §7.6 Black
     Lung Trust Fund + §7.7 SMCRA + §7.8 Purdue + §7.9 Mazzucato+
     Harvey + §7.10 regional-scholarship + §7.11 out-of-scope
     inventory. **The essay must agree with §7 on every fact;
     Pass 3.1 audits this.**
   - §6 Path B preemptive policy + verbatim-quote exceptions (the
     six brief-§6-permitted verbatim quotes Pass 3.1 must preserve
     exactly; do NOT spot-fix the verbatim quotes)
   - §8 apparatus exclusion list (verify the essay's effective
     reveal stays ~18–22% concept-level; flag if any EXCLUDED
     apparatus surfaces)
   - §11 named-subject status (closed at Stage 0; cross-reference
     only; Pass 3.1 does NOT re-litigate)
   - §16 hard constraints

10. **publishing/essays/harpers-the-miner/stage-2-ratification-2026-05-27.md**
    — **PC-4 + PC-5 RATIFICATION + FORWARD-FLAG INVENTORY.** Load-
    bearing sections for Pass 3.1:
    - §3 Pass-3.1-flagged items: §VI four-cost-component arithmetic
      anchors verification (Trust Fund $4.6B/$15B-by-2050/45-year-
      deficit; SMCRA $4–6B gap / 633,000 acres / $7.5–9.8B cleanup /
      $3.8B bond / $865M 2014–2016 bankruptcy transfer; black lung
      20%-of-25+-year-Appalachian prevalence; 33× framework-multiple
      floor); §VII Purdue four-characteristic enumeration
      verification + Sackler $11B + Big Three $21B; Ch 10 RATIFIED-
      state §VIII closing-return coherence awareness
    - §3a flag 2: Ch 10 PROPOSED→RATIFIED ripple — light Stage 1c
      coherence touch-up may surface; Pass 3.1 handles inline if
      material

11. Wave 1 Pass 3.1 format precedents (artifact-structure reference):
    - tools/rigor-passes/commons_bonds_rigor_pass_2026-05-22_boston_review_essay_stage3_pass_3_1_fact_check_v1.0.0.md
    - tools/rigor-passes/commons_bonds_rigor_pass_2026-05-22_100_barrel_essay_stage3_pass_3_1_fact_check_v1.0.0.md
    - tools/rigor-passes/commons_bonds_rigor_pass_2026-05-22_atlantic_ideas_essay_stage3_pass_3_1_fact_check_v1.0.0.md
    - publishing/essays/foreign-affairs-existence-proof/rigor/pass-3-1-fact-check.md
      (closest temporal sibling; same-day-as-this-staging precedent
      for cadence + commit pattern)

12. **manuscript/chapters/Chapter__2_TheMiner.md** — source chapter
    for fact-verification ONLY. Per brief §6 Path B preemptive
    policy: the Pass 3.1 session may verify a fact against Ch 2 if
    needed, but spot-fix prose must be generated FRESH from §7
    anchors, NOT pasted from Ch 2. Treating Ch 2 as paraphrase
    source re-introduces Path B contamination.

== Your task — sequential ==

Produce the Pass 3.1 fact-check artifact for the Ch 2 → Harper's
Stage 2 essay. Output spec per Amendment C Interactive Ratification
Protocol:

**Sub-step 3.1-a — Mechanical fact-audit.** Walk the essay
section-by-section; for each substantive factual claim, verify
against §7 canonical-facts inventory. Build internal findings
inventory (do NOT dump to author). Track:

- Numerical anchors (dates; dollar amounts; percentages; counts;
  rates) — verify against §7
- Named-subject attribution (Bailey + Latusek + Lilly + Hamby +
  Kennedy + Sacklers + Mazzucato + Harvey + Keefe + Caudill / Catte
  / Stoll if named) — verify per brief §11 named-subject status
- Verbatim quotes (the six brief-§6-permitted) — verify EXACT match
  to §7 verbatim text; flag any drift in punctuation / wording
- Institutional names (W.R. Grace; Consol Energy; U.S. Steel Gary
  mine; UMWA; Black Lung Association; Miners for Democracy; Purdue;
  McKesson; Cardinal Health; AmerisourceBergen; WV Public
  Broadcasting; Inside Appalachia; Center for Public Integrity;
  Empire of Pain etc.) — verify against §7 + bibliography
- Dates + sequence (Kennedy May 1960; Black Lung Trust Fund 1969;
  SMCRA 1977; Yablonski murder 1969; Miners for Democracy
  post-1969; Bailey Feb 2019; Latusek Oct 19 2022; Hamby Pulitzer
  2014; Big Three settlement 2022) — verify against §7

**Sub-step 3.1-b — Per-finding artifact construction.** For each
finding (factual drift identified at sub-step 3.1-a), produce a
per-finding entry in the format:

- **ID + severity:** Fact-3.1-N + HIGH / MEDIUM / LOW
  - HIGH = material factual drift (wrong number / wrong date /
    wrong attribution / verbatim-quote drift)
  - MEDIUM = drift in framing that doesn't break the fact but
    departs from canonical inventory (e.g., "five words" vs
    "five-word self-description")
  - LOW = stylistic-adjacent fact-tagging (e.g., institutional-
    name shorthand vs full institutional name) — surface but
    don't necessarily spot-fix
- **Finding statement:** what the Stage 2 essay says + what §7
  says + where they diverge
- **Location anchor:** essay.md line + section
- **Options:** typically 2–4 spot-fix candidates; **at least one
  option must propose spot-fix prose GENERATED FRESH from §7
  anchors (not pasted from Ch 2)**
- **Recommendation:** sub-agent's recommended option + 1-line
  rationale
- **Reasoning:** load-bearing for author's ratification decision

**Sub-step 3.1-c — Interactive ratification + application.**
Per Amendment C Interactive Ratification Protocol + cadence memory
one-finding-at-a-time discipline:

1. Present finding #1 to author with Options + Recommendation +
   Reasoning. Severity-strict ordering: all HIGH first → all MEDIUM
   → all LOW.
2. Author selects / overrules / iterates per finding.
3. Apply ratified spot-fix to publishing/essays/harpers-the-miner/essay.md
   in this same session (Amendment C interactive — ratification +
   application combine).
4. Move to next finding.
5. At session close: essay.md state reflects all ratified Pass 3.1
   spot-fixes; the Pass 3.1 artifact records each finding + its
   ratification + APPLIED diff.

**Sub-step 3.1-d — Output artifact construction.** Output:

`publishing/essays/harpers-the-miner/rigor/pass-3-1-fact-check.md`

Required artifact structure:
- **Header:** Status (PROPOSED → RATIFIED + APPLIED at session
  close); Workstream; Methodology anchor; Scope; Predecessor
  artifacts (Stage 1 brief at be87926 + Stage 2 draft at 55842a3
  + PC-4 ratification at 537258f + PC-5 at 189a847).
- **§1 Per-finding entries** (per sub-step 3.1-b format)
- **§2 Severity-strict ordering** (all HIGH → all MEDIUM → all LOW)
- **§3 Ratification record** (per-finding ratification outcome +
  APPLIED diff verbatim against essay.md)
- **§4 Path B audit summary** (post-Pass-3.1: enumerate verbatim
  quotes — should be exactly the six brief-§6-permitted; flag any
  surviving non-permitted Ch 2 echoes; this is the Path B compliance
  verdict that PC-4 D-HIGH-3 deferred to Pass 3.1)
- **§5 Apparatus reveal audit summary** (post-Pass-3.1: verify
  effective reveal stays ~18–22% concept-level; confirm zero
  EXCLUDED apparatus per brief §8)
- **§6 Forward-flag inventory** for Pass 3.2 voice-polish session
  (any voice-register drift identified during fact-check that
  isn't a Pass 3.1 spot-fix target; e.g., §VIII elided-"that"
  sentence already queued in PC-4 §3 forward-flag #1)
- **§7 STATE + next-pass anchor + end-of-session one-liner**

== Commit + push discipline ==

**Per CLAUDE.md merge-to-main policy:**

- **The Pass 3.1 artifact** at `publishing/essays/harpers-the-miner/rigor/pass-3-1-fact-check.md`
  is internal scaffolding → at session close, auto-fast-forward
  merge to main per worked pattern at Phase C 2026-05-27 + memory
  entry feedback_worktree_isolation v1.0.1 (commit b8dc99e):
  cherry-pick the artifact-only commit onto a fresh branch from
  origin/main + push to main + remove temp branch.

- **The Pass 3.1 essay.md spot-fixes** are end-user-facing prose
  → commits stay on this feature branch
  (`claude/ch2-harpers-pass3-1-factcheck-<harness-id>`); do NOT
  push to main. The post-Pass-3.1 essay.md state is the input to
  Pass 3.2 voice-polish session.

- **The Pass 3.2 voice-polish kickoff paste-text** at
  `tools/workstream-handoffs/ch2-harpers-stage-3-pass-3-2-voice-polish-kickoff_2026-05-27.md`
  produced at session close per Wave 1 + Ch 4 → FA Pass 3.1 → 3.2
  precedent (1015a94) is internal scaffolding → auto-fast-forward
  merge to main same as the artifact.

- **Hard constraints (CLAUDE.md):** never force-push main; never
  amend a commit on origin/main; never skip hooks without explicit
  author direction; pre-push reconciliation (fetch origin main +
  rebase / cherry-pick onto fresh branch) for any main-bound commit.

== Hard constraints (Pass 3.1-specific) ==

- **Verbatim-quote preservation:** the six brief-§6-permitted
  verbatim quotes (Kennedy Canton + Bailey ×2 + Latusek ×3) must
  survive Pass 3.1 unchanged unless §7 canonical text differs from
  essay text (in which case Pass 3.1 conforms essay to §7 canonical
  per Amendment A discipline). Do NOT introduce alternate phrasings.
- **Path B preemptive policy (brief §6):** spot-fix prose generated
  FRESH from §7 anchors; do NOT paste from Ch 2 prose. The Pass 3.1
  agent may verify a fact against Ch 2 but must NOT lift sentences.
- **Named-subject discipline closed at Stage 0** (brief §11): do not
  re-litigate consent / public-record-exception decisions; do not
  contact named subjects beyond citation-accuracy courtesy-notify
  protocol (which is Stage 4 / pre-submission protocol, not Pass
  3.1 work).
- **Apparatus-reveal cap (brief §8):** verify the post-Pass-3.1
  essay stays ~18–22% effective reveal; flag any surfaced apparatus
  (CS = RCV − B equation; bond decomposition; Three Ways of
  Counting; CIT; Four Gates; Cᵢ vocabulary; ARR; named-instrument
  proper nouns) for immediate spot-fix.
- **Substance-drives-length** (`feedback_substance_drives_length.md`):
  Pass 3.1 polarity is precision (verify against §7 anchors), NOT
  cutting. Pass 3.2 is cutting polarity; Pass 3.5 is restoration
  polarity. Pass 3.1 should not alter section length budgets; it
  corrects factual drift in place.
- **Author substrate gets critical editorial input** per
  `feedback_substrate_critical_editorial_input.md`: when author
  ratifies / iterates, surface issues with the proposed spot-fix
  text actively rather than blindly applying.
- **One-finding-at-a-time per Amendment C + cadence memory.** NO
  list-dump anti-pattern A1. Severity-strict ordering: HIGH → MED
  → LOW; no interleaving.
- **Status markers:** 🔴 AUTHOR DECISION REQUIRED / 🔵 ESCALATION /
  🟢 NEXT STAGE READY / 🟡 SUB-SESSION NEEDED / ⏳ CLAUDE-ACTION
  IN PROGRESS / 🟣 AWAITING EXTERNAL / ✅ SESSION COMPLETE.

== Expected outputs ==

1. **Pass 3.1 artifact PROPOSED → RATIFIED + APPLIED** at
   `publishing/essays/harpers-the-miner/rigor/pass-3-1-fact-check.md`;
   internal scaffolding; pushed to origin/main via temp-worktree
   cherry-pick pattern at session close.
2. **Essay.md post-Pass-3.1 state** with ratified spot-fixes
   applied; stays on feature branch
   `claude/ch2-harpers-pass3-1-factcheck-<harness-id>`; NOT
   pushed to main.
3. **README.md** updated to reflect Pass 3.1 RATIFIED + APPLIED
   state on the feature branch (commit chain documented per Phase
   C 2026-05-27 precedent).
4. **Pass 3.2 voice-polish kickoff paste-text** staged at
   `tools/workstream-handoffs/ch2-harpers-stage-3-pass-3-2-voice-polish-kickoff_2026-05-27.md`;
   internal scaffolding; pushed to origin/main alongside the Pass
   3.1 artifact.
5. **End-of-session STATE one-liner** indicating Pass 3.2 voice-
   polish is the next session to fire.

== Parent session resume marker ==

When this Pass 3.1 session completes, the parent orchestration
session (currently in worktree
`/Users/c17n/commons-bonds/.claude/worktrees/ch2-harpers-pipeline-orchestration`)
can spawn the Stage 3 Pass 3.2 voice-polish agent from:
- the Pass 3.1 RATIFIED + APPLIED essay.md state on this feature
  branch
- the Pass 3.2 kickoff paste-text on origin/main
- the Stage 1 brief on origin/main (be87926)
- the Pass 3.1 artifact on origin/main (per artifact spec above)

===
```

---

## End-of-staging notes

Per cadence-memory I4 (sub-session spawn discipline): this kickoff
paste-text + an explicit resume marker (artifact path + STATE-to-look-
for) constitute the complete handoff to the next pipeline stage. The
parent orchestration session at
`worktree-ch2-harpers-pipeline-orchestration` can spawn the Pass 3.1
agent immediately on receipt of this staged paste-text.

Per cadence-memory I8 (session-naming convention with parent-child
surfacing): the Pass 3.1 session's branch name `claude/ch2-harpers-pass3-1-factcheck-<harness-id>`
encodes the workstream + stage; downstream Pass 3.2 / 3.3 / 3.4 / 3.5
sessions follow the same naming pattern.

Per the worked Phase C 2026-05-27 commit-classification pattern:
- Pass 3.1 ARTIFACT (rigor-pass) → main as internal scaffolding via
  temp-worktree cherry-pick (lands cleanly without dragging essay.md)
- Pass 3.1 ESSAY.MD SPOT-FIXES → stay on feature branch per CLAUDE.md
  end-user-facing-prose discipline
- Pass 3.2 KICKOFF PASTE-TEXT → main as internal scaffolding (same
  temp-worktree pattern)

STATE: STAGED; NEXT: parent orchestration session spawns Pass 3.1
agent in fresh CC session by pasting the body block above; AWAITING:
Pass 3.1 RATIFIED + APPLIED → Pass 3.2 voice-polish session fires.
