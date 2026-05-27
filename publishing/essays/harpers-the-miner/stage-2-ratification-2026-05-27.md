# Ch 2 → Harper's Magazine Stage 2 audience-blind draft — RATIFIED 2026-05-27

**Date ratified:** 2026-05-27
**Ratification session:** Phase C ratification (agent-a3390c00c9b9a4df0 worktree)
**Draft state:** PROPOSED commit `55842a3` → RATIFIED 2026-05-27 (no prose changes applied; ratify-as-proposed disposition)
**Authority:** Author disposition 2026-05-27: *"ratify all as recommended and proposed; fire next phase/stage when ready"*
**Cadence reference:** Amendment C Interactive Ratification Protocol + [`tools/memory/feedback_parallel_session_ratification_cadence.md`](../../../tools/memory/feedback_parallel_session_ratification_cadence.md) (single-batch disposition pattern; precedent at Atlantic Ideas Pass 3.3 commit `20e4316` + Pass 3.4 commit `6224af0`)

---

## §1. PC-4 deferred 🔴 items dispositioned

### D-HIGH-1 — Commit handling — RESOLVED at PC-2

The agent return summary surfaced commit-handling as 🔴 because the autonomous-mode agent (task `a92185d216c1bddd6`) drafted the essay + README but did not commit/push (likely sandbox/worktree-isolation constraint). Phase C session PC-2 step staged + committed the Stage 2 draft on the feature branch as commit `55842a3` 2026-05-27 with descriptive message mirroring brief commit `3d1810b` format. Hard constraint preserved: commit lands on `worktree-agent-a3390c00c9b9a4df0` feature branch only; essay.md is end-user-facing prose per CLAUDE.md merge-to-main policy and does NOT auto-merge to main until author explicitly merges post-pre-submission ratification.

### D-HIGH-2 — Word count 7,216w vs brief §12 target band 8,000–11,000w — RATIFIED (defer to Pass 3.5)

**Verification:** `wc -w publishing/essays/harpers-the-miner/essay.md` returned 7,216w (whole file including dek + author bio; body-only = 7,176w when dek + bio excluded). The agent return summary's 7,216w figure is accurate. The per-essay README's prior claim of "~9,500w body" was a drafting-time estimate that diverged from the actual landed count by ~2,284w; corrected in this commit's README edit.

**Brief §12 framework:**
- Target band: 8,000–11,000w body (middle-of-band Harper's literary-essay convention).
- Stage-3-flag triggers: ≥12,000w (re-evaluate compression) or ≤6,500w (re-evaluate substance).
- No-auto-flag band: 6,500–12,000w (substance-drives-length disposition; Harper's editor will read short if prose earns it).

**Disposition:** 7,216w sits 784w below the target band floor (8,000w) but 716w above the ≤6,500w Stage-3-flag trigger. **Sits squarely in brief §12 no-auto-flag band** (6,500–12,000w). Per `feedback_substance_drives_length.md` 2026-05-02 + Amendment B Pass 3.5 codification 2026-05-18 (restoration polarity, NOT cutting polarity), the appropriate disposition is to **defer to Pass 3.5 developmental-edit** for restoration-polarity identification of any genuine restoration sites. The brief §4 structural table suggested per-section word targets summing to ~7,900w; the draft's 7,216w body sits within ~10% of that brief-estimated target, indicating substance-driven length rather than under-developed structure. Pass 3.5 will identify any genuine restoration sites (scene-anchor density at §I + §III + §VIII; arithmetic-walk depth at §VI; voice-flow continuity across sections); if Pass 3.5 finds no warranting restoration sites, the draft accepts as-is.

**Forward-flag:** Pass 3.5 session, when fired, evaluates the 784w gap against the brief §4 per-section word targets; reports either (a) restoration sites identified with proposed additions, or (b) accept-as-is verdict if substance is genuinely shorter than the band floor. Restoration polarity (3.5) cannot be combined with cutting polarity (3.2) — see Amendment B 2026-05-18.

### D-HIGH-3 — Path B carry-over: 6 verbatim sentences/phrases — DISSOLVED on inspection

**Verification:** Brief §6 *Verbatim carry-forward exceptions* explicitly enumerates **exactly six** load-bearing public-record verbatim quotes as permitted Path B exceptions:

1. Kennedy 1960 Canton, Ohio formulation (Ch 2 line 14).
2. Bailey *"It's almost like drowning."* (Ch 2 line 30).
3. Bailey *"Most laws across the nation, most laws have been written with blood..."* (Ch 2 line 34).
4. Latusek *"A lot of times, you couldn't see your hand in front of your face..."* (Ch 2 line 168).
5. Latusek *"My goal in life was to outlive Consol..."* (Ch 2 line 170).
6. Latusek *"I was loyal to the company, but the loyalty wasn't there for me..."* (Ch 2 line 172).

**Stage 2 draft inventory:** all six brief-§6-permitted verbatim quotes appear in the draft (Kennedy at §II ¶7; Bailey ×2 at §IV ¶17 + ¶19; Latusek ×3 at §VIII ¶71). No additional verbatim quotes beyond the six permitted exceptions surface in the draft via direct identification.

**Dissolution:** the agent return summary's framing as *"6 verbatim sentences/phrases vs brief target ≤4 (all brief-anchored load-bearing carry-forwards; iterate via Pass 3.2 voice-polish or accept as intentional structural anchors)"* misread the Path B discipline. The "~3–4 verbatim Ch 1 sentences" figure surfaces in `feedback_audience_aware_drafting_discipline.md` Noema empirical anchor as a **measured residue** in Essay B's audience-blind draft (down from ~17–22 in Path-B-contaminated Essay A), NOT as a target ceiling. The brief §6 explicit-permission for the six load-bearing public-record quotes is independent of and prior to the Noema residue measurement. The draft is brief-§6-compliant on this metric.

**Forward-flag for Pass 3.1 fact-check session:** Pass 3.1 will run the full Ch 2 diff for any UNINTENDED Ch 2 echoes beyond the six permitted brief-§6 quotes. That's where the actual Path B compliance verdict lands (per Wave 1 BR Pass 3.1 + Atlantic Ideas Pass 3.1 precedent). The current dissolution does not pre-empt Pass 3.1 — it simply corrects the agent return summary's misread of the brief.

---

## §2. Structural execution dispositions (draft choices ratified)

These execution choices were carried forward into the Stage 2 draft from the Stage 1 brief and are recorded here as PC-4 dispositions for cross-artifact traceability. All ratified per the single-batch "ratify all as recommended" disposition; cross-referenced to the relevant Stage 1 brief §18.4 ratification finding:

- **Frame: Option B limited first-person frame** — first-person §I opening (Route 52 arrival; "I had come because of a question..."; "What I want to do in what follows is to try, in plain English, to add up what was actually paid for the coal..."); first-person §VIII closing return ("I drove back out of McDowell County on the same road I had come in on"; "I think about Latusek's last sentence often..."); occasional structural-inflection first-person elsewhere (§III "I do not want, in anything that follows, to write a sentence that makes them sound like victims"; §IV "five words that I have not been able to get out of my head since I first heard them on the radio"; §V "The word I have come, after a long time of trying other words, to use for it is *cost severance*"); third-person reportage spine §II + §III (post-first-person-aside) + §IV (post-first-person-aside) + §VI + §VII. Cross-reference: Stage 1 brief §18.4 HIGH-2 ratification.

- **Scene-shift marker: `* * *` (three-asterisk ornament)** between major sections; no marker within sections. Eight major-section breaks rendered cleanly. Cross-reference: Stage 1 brief §18.4 HIGH-3 ratification.

- **Eight-section structure** §I opening scene → §II Kennedy 1960 historical anchor → §III place-before-collapse + dignity-of-labor preemption → §IV Bailey body-keeps-account + Trust Fund mechanism → §V vocabulary section (cost severance / severed cost / value extraction + Mazzucato + Harvey lineage + UMWA / BLA 1968 / Miners for Democracy regional-organizing credit) → §VI four-cost-component arithmetic → §VII Purdue second cycle + cultural-pathology rebuttal → §VIII spatial cost severance + first-person closing return + explicit-meta Condition-1 disarming close. Per brief §4 structural table; substantively delivers all eight section functions. Cross-reference: Stage 1 brief §18.4 MED-3 ratification.

- **Apparatus reveal concept-level only ~18–22% effective** — cost severance + severed cost + value extraction surface as plain-prose concepts; Mazzucato + Harvey lineage attribution at §V; brief mention of *accumulation by dispossession* (Harvey) + Mazzucato's *value creation* / *value extraction* distinction. No formal apparatus surfaces (no equation, no bond decomposition, no Three Ways of Counting, no CIT, no Four Gates, no Cᵢ vocabulary, no ARR, no named-instrument proper nouns). The 33× framework-multiple floor lands at §VI in a single sentence with route-to-book attribution per brief §7.11. Cross-reference: Stage 1 brief §18.4 MED-4 ratification.

- **Regional-organizing-tradition crediting at §V** — UMWA + Black Lung Association 1968 wildcat strike + Miners for Democracy + Yablonski named in plain prose at §V miner-agency paragraph. Pre-empts cultural-pathology framing by surfacing miners-built-the-architecture-themselves. Cross-reference: Stage 1 brief §18.4 MED-5 ratification.

- **Explicit-meta Condition-1 disarming move at §VIII close** — *"I want to close with a sentence that I have, by this point in the essay, perhaps earned. The argument I have made here is not a partisan argument. I am not making the case for any particular legislative program. I am not asking the reader to agree with any specific policy I am not, on these pages, proposing. The mechanism of cost severance operates regardless of whether the reader's political starting point is regulatory caution, market discipline, or worker solidarity, because the mechanism does not turn on any of those things..."* Per $100 Barrel 2026-05-21 anchor; Tier 2 #8 center-right reader + Tier 2 #9 Manchin-aligned reader gating-adjacent. Cross-reference: Stage 1 brief §18.4 MED-6 ratification.

---

## §3. Auxiliary forward-flags queued for Stage 3 sessions

Surfaced during PC-4 review; NOT ratification-blocking; queued for relevant Stage 3 pass:

1. **§VIII close — elided-"that" sentence flagged for Pass 3.2 voice-polish.** Sentence: *"I am not asking the reader to agree with any specific policy I am not, on these pages, proposing."* The elided "that" clause ("any specific policy [that] I am not, on these pages, proposing") reads stilted on first pass and may warrant rephrasing. Pass 3.2 voice-polish should evaluate whether to restore the explicit "that" or restructure the sentence; the rhetorical work (explicit-meta non-partisan disarming) is load-bearing and must survive any rephrasing.

2. **§V Mazzucato + Harvey lineage paragraph — verify single-prose-mention discipline per brief §7.9.** The draft's §V renders Mazzucato + Harvey lineage attribution across two paragraphs (¶33–34): *"The economist Mariana Mazzucato, in her 2018 book The Value of Everything: Making and Taking in the Global Economy, drew the line between value creation and value extraction..."* + *"The geographer David Harvey, in The New Imperialism (2003), gave the longer lineage a different name (accumulation by dispossession)..."* Brief §7.9 specifies "one prose mention" each. Pass 3.2 voice-polish should verify the two-paragraph treatment doesn't crowd the section's argumentative motion; if compression warranted, fold to single-paragraph treatment.

3. **§V regional-scholarship reference compression.** The draft's §V does not name Caudill / Catte / Stoll explicitly (the brief §7.10 specified one prose mention at §V or §III for the regional-scholarship lineage). The UMWA / Black Lung Association / Miners for Democracy regional-organizing-tradition credit DID land at §V (per MED-5 ratification). Forward-flag for Pass 3.5 developmental-edit: evaluate whether one-sentence Caudill / Catte / Stoll credit warrants restoration; the regional-scholarship and regional-organizing traditions are distinct (scholarship = Caudill 1962 *Night Comes to the Cumberlands* + Stoll 2017 *Ramp Hollow* + Catte 2018 *What You Are Getting Wrong About Appalachia*; organizing = UMWA + BLA + MFD). Pass 3.5 restoration-polarity is the appropriate session to evaluate.

4. **§VI arithmetic-walk depth.** Brief §4 specified ~1,200w for §VI; draft §VI lands at approximately the brief target. The 33× framework-multiple range (33–122×) is mentioned at §VI ¶46 with the floor (33×) only and route-to-book attribution per brief §7.11. Pass 3.1 fact-check should verify the 33–122× range, the $4.6B / $15B-by-2050 Trust Fund debt anchors, the 633,000 acres / $7.5–$9.8B / $3.8B reclamation-bonding anchors, the $865M 2014–2016 bankruptcy transfer anchor, and the 20%-of-25+-year-Appalachian-miners-with-black-lung prevalence figure against brief §7 canonical-facts inventory.

5. **§VII Purdue framing.** Draft §VII renders the four-characteristic target map + Sackler $11B + Big Three $21B settlement + cultural-pathology rebuttal per brief §7.8. Pass 3.1 should verify the four-characteristic enumeration (high rates of physical labor injury / limited healthcare infrastructure / concentrations of high-prescribing physicians / economic precarity) against brief canonical-facts; Pass 3.4 adversarial robustness should evaluate the cultural-pathology rebuttal against the Tier 1 #2 Harper's reader + Tier 3 #12 Appalachian academic + Tier 3 #16 environmental-justice reader pressure tests.

6. **README word-count drift fixed inline.** The per-essay README at `publishing/essays/harpers-the-miner/README.md` initially claimed *"~9,500w body"* — a drafting-time estimate. Corrected to actual 7,216w body in this commit; the corrected README references the substance-drives-length disposition + defer-to-Pass-3.5 forward-flag.

---

## §3a. PC-5 forward-flag dispositions (§18.3 Stage-2-fire-time verification items)

Status check of the five Stage 1 brief §18.3 forward-flags performed at Phase C session 2026-05-27:

1. **Ch 2 Pass 3.5 RATIFIED/APPLIED ripple — CLEARED.** Ch 2 chapter Pass 3.5 RATIFIED + Phase C-ζ minimum-restoration set applied at origin/main commit `c1d9ae3` (lines 184/186 analytical-pivot restorations; per Stage 0 record 2026-05-25). Pass 3.5 closure preceded Stage 2 draft generation; no ripple needed. Brief §7 canonical-facts inventory remains coherent with chapter source.

2. **Ch 10 PROPOSED → RATIFIED ripple — REQUIRES PASS-3.1-LIGHT-COHERENCE-AWARENESS.** Ch 10 (`manuscript/chapters/Chapter_10_CommonBonds.md`) has advanced through Pass 3.5 developmental-edit RATIFIED + APPLIED at origin/main commit `dd997ad` 2026-05-25 + Pass 3.1 parallel-workstream consolidation at commit `0615b9c` 2026-05-25. The brief §4 §VIII row references "Ch 10 ALT Stage 2 PROPOSED" — the chapter's current RATIFIED state postdates that reference. **Forward-flag to Pass 3.1 fact-check session:** verify Harper's §VIII closing-return framing remains coherent with Ch 10's RATIFIED state; specifically the architecture-that-would-have-closed-the-gap-was-never-built register (Harper's §VIII ¶78 final block) should align with Ch 10's RATIFIED closing-book-chapter handling. Light Stage 1c coherence touch-up may surface; Pass 3.1 session handles inline if material.

3. **Rights-register no-overlap verification — PRE-FIRE CLEAR; APPEND-AT-SUBMISSION-REQUIRED.** Rights-register at `publishing/essays/_pipeline/rights-register.md` (drafted 2026-05-06; modified 2026-05-09) verified at Stage 2 fire-time per brief §6 source-material list. No current pipeline overlap with Aeon Ch 7 / Noema Ch 1+10 / BR Ch 5 / Atlantic Ideas Ch 9 / $100 Barrel Ch 9-adj scopes. **Forward-flag to Stage 4/5 cover-letter + submission-package session:** append Harper's row to rights-register per the file's "append-only. One row per submission." discipline; row should record: Piece = "Harper's — *What McDowell County Paid*"; Source chapter = Ch 2; Venue (status) = "Harper's Magazine (Stage 2 draft RATIFIED; Stage 3 cascade firing)"; Submitted = TBD Q4 2026; Exclusivity terms = TBD per Harper's contract on acceptance; Conflicting passages / do-not-reuse = TBD post-Stage-3.

4. **Atlantic Ideas + Harper's McDowell numerical-anchor coherence — STAGE-5-TIMING-FLAG.** Atlantic Ideas Ch 9 essay has advanced through Pass 3.5 PROPOSED at origin/main commit `f04f821` + Pass 3.5 Phase C applied at `2581277` + Stage 4 render audit RATIFIED at `b54822b`. The Atlantic Ideas essay carries McDowell per-ton arithmetic ($4.50/ton 1960 mine-mouth → $520–600/ton honest cost; 33–122× framework-multiple range full development per cascade plan v2 + Ch 9 derivative scope); the Harper's essay carries only the 33× floor at §VI with route-to-book attribution per brief §7.11. **Forward-flag to Stage 5 sign-off + pre-submission package session:** verify numerical-anchor consistency (33× floor + Bay Lung Trust Fund $4.6B / $15B by 2050 anchor + reclamation-bonding $4–6B gap anchor) against Atlantic Ideas essay's RATIFIED-state numerical anchors. Routine cross-essay coherence verification; not Stage 3 territory.

5. **AI-disclosure paragraph template — VERIFIED PRESENT.** `publishing/essays/_shared/templates/ai-disclosure-paragraph.md` exists in agent worktree per Stage 2 fire-time verification. **Forward-flag to Stage 4 cover-letter draft session:** integrate AI-disclosure paragraph per Wave 1 BR + Aeon + Atlantic Ideas precedent (bottom of cover letter; generic-variant from template; per `feedback_named_subject_consent.md` + brief §16 hard constraints).

## §3b. Phase C session-housekeeping notes (NOT material to draft state)

1. **Worktree-isolation self-incident — bounded; no parallel-session collision.** Phase C session initially attempted to apply brief §18.4 ratification record edits against the MAIN repo path (`/Users/c17n/commons-bonds/tools/rigor-passes/...`) instead of the agent worktree path (`/Users/c17n/commons-bonds/.claude/worktrees/agent-a3390c00c9b9a4df0/tools/rigor-passes/...`). The main repo was on branch `claude/atlantic-ideas-essay-pass-3-5-ratify-and-phase-c-61cef166-5c1` (an unrelated parallel Atlantic Ideas Pass 3.5 ratification session). The Atlantic Ideas session's active modifications (`publishing/essays/atlantic-ideas-pricing-honestly/essay.md` + Pass 3.5 rigor-pass artifact + sign-off files) do not touch the Ch 2 → Harper's brief; contamination was bounded. Reconciliation: copied modified brief from main repo to agent worktree; restored main repo brief via `git checkout`. No parallel-session collision realized. Logged for `feedback_worktree_isolation_for_parallel_sessions.md` empirical-anchors update consideration.

2. **Temp-worktree push pattern for scaffolding-only commit.** Phase C session used a fresh worktree off origin/main (`/Users/c17n/commons-bonds-ch2-harpers-scaffolding-push-260527-6dc170`) to cherry-pick the brief-ratification + clean-baseline commit `ea867f1` onto a branch from origin/main + push as commit `be87926` to main, isolating the scaffolding push from the essay.md commit `55842a3` on the agent feature branch. This pattern works cleanly for mixed-classification commit handling (scaffolding-only commits push to main; end-user-facing-prose commits stay on feature branch). May warrant codification as a CLAUDE.md merge-to-main-policy supplementary pattern; flagged for next PM session.

## §4. State + next-action summary

- **Stage 2 draft state:** RATIFIED 2026-05-27 (no prose changes applied; ratify-as-proposed disposition).
- **Stage 1 brief state:** RATIFIED 2026-05-27 at sibling §18.4 (cross-reference: `tools/rigor-passes/commons_bonds_rigor_pass_2026-05-26_ch2_harpers_essay_pre_draft_audience_structure_v1.0.0.md` §18.4 + clean-baseline at `tools/quality-gates/clean-baselines/ch2_harpers_stage1a_2026-05-27.md`).
- **Stage 1a invariant gate:** CLEAN BASELINE per-scope for Ch 2 → Harper's artifacts.
- **Stage 3 cascade state:** NOT STARTED — fires sequentially after Phase C session close per brief §13 + v3.1 doctrine + Amendment A two-class cascade discipline + per-prompt serial cadence.
- **Stage 4 + Stage 5 state:** NOT STARTED — fires post-Stage 3 per brief §14.

**Next session to fire:** Stage 3 Pass 3.1 fact-check (per brief §13). The parent orchestration session at worktree `/Users/c17n/commons-bonds/.claude/worktrees/ch2-harpers-pipeline-orchestration` resumes after Phase C close and spawns the Pass 3.1 agent from the ratified Stage 2 essay draft (`publishing/essays/harpers-the-miner/essay.md` at commit `55842a3` on this branch) + the RATIFIED Stage 1 brief (now on origin/main per scaffolding push at commit `be87926`).

**Per CLAUDE.md merge-to-main policy:** This PC-4 ratification artifact + the inline README correction commit on the feature branch (`worktree-agent-a3390c00c9b9a4df0`) does NOT auto-merge to main. The essay.md commit (`55842a3`) + this PC-4 commit both stay on the feature branch until author ratifies the full Stage 3 cascade + pre-submission package and explicitly merges to main pre-Submittable-submit.

---

## §5. STATE one-liner

```
STATE: RATIFIED; NEXT: Stage 3 Pass 3.1 fact-check fires in separate session
(parent orchestration session at worktree-ch2-harpers-pipeline-orchestration
resumes + spawns Pass 3.1 agent from this ratified Stage 2 draft); AWAITING:
Phase C session close → Stage 3 cascade begins (per-prompt serial cadence
3.1 → 3.2 → 3.3 → 3.4 → 3.5 → light 3.3 re-fire)
```
