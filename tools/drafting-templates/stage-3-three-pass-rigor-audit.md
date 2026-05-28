# Stage 3 — Five-Pass Rigor Audit (Template, v3.1 + Amendment C)

**FIRST ACTION (2026-05-26).** Before any other work, the session firing this template must execute the worktree-isolation step at [`worktree-isolation-paste-text.md`](worktree-isolation-paste-text.md). Branch-contamination root-cause + discipline: [`../memory/feedback_worktree_isolation_for_parallel_sessions.md`](../memory/feedback_worktree_isolation_for_parallel_sessions.md).

**Purpose.** Post-draft rigor on a Stage 2 audience-blind flow draft (or an existing piece of prose). Five distinct passes — fact-check + voice-polish + audience-load acceptance + audience-load robustness + developmental-edit — each catching what the others miss.

**v3.1 framing per pipeline-doctrine v1.0.0 Amendment B (ratified 2026-05-18):** Stage 3 extends from four-pass to five-pass with the addition of **Pass 3.5 developmental-edit** at whole-chapter scale. Pass 3.5 catches emotional-arc continuity + scene-anchor density + cumulative-LLM-cadence residue that per-paragraph Pass 3.2 cannot. Filename `stage-3-three-pass-rigor-audit.md` is canonical for cross-reference stability (historical: v2.0 was three-pass; v3.0 four-pass; v3.1 five-pass).

**Amendment C addendum (ratified 2026-05-19):** prose-modifying passes (Pass 3.1 / Pass 3.2 / Pass 3.5) MUST produce per-finding artifacts with the §3.7.2 required format (Options + Recommendation + Reasoning). Ratification is INTERACTIVE — a follow-up session walks author through each finding with options + recommendation + reasoning + applies ratified spot-fixes to chapter source in the same combined session. See pipeline-doctrine v1.0.0 §3.7 for the full codification.

**When to use.** Required for any publisher-facing prose >~500w before submission. Lighter version (single audience-load pass) acceptable for in-book defense paragraphs.

**Critical discipline (v3.0 framing, extending v2.0 Amendment B).** Four DISTINCT passes, not bundled. v2.0 Amendment B established the three-pass discipline (fact-check + voice-polish + audience-load); v3.0 splits Pass 3 into Pass 3.3 (audience-load acceptance) + Pass 3.4 (audience-load robustness against adversarial / detractor characters) per the 2026-05-17 Ch 1 Pass 3 REAUDIT v3 canonical example. Acceptance + robustness use different character sets, different verdict scales, and produce different diagnostic outputs.

**Parent doctrine:** [`tools/pipeline-doctrine/commons_bonds_pipeline_doctrine_v1.0.0.md`](../pipeline-doctrine/commons_bonds_pipeline_doctrine_v1.0.0.md) — see §1 for the full pipeline stage structure; §6 for the bookend sign-off discipline.

**Canonical examples.**
- Stage 3 comparison verdict: [`publishing/essays/noema-commons-bonds/rigor/stage-3-comparison_2026-05-10.md`](../../publishing/essays/noema-commons-bonds/rigor/stage-3-comparison_2026-05-10.md)
- Audience-load pass: [`tools/rigor-passes/commons_bonds_rigor_pass_2026-05-11_why_bonds_paragraph_include_vs_exclude_audience_load_v1.0.0.md`](../rigor-passes/commons_bonds_rigor_pass_2026-05-11_why_bonds_paragraph_include_vs_exclude_audience_load_v1.0.0.md)
- Op-ed Stage 3 (self-applied): see op-ed pipeline session commit `5167edd` — the session's own Stage 3 caught real GPFG / Bondevik factual drift
- Pass 2 voice-polish (canonical artifact format model — F-V1 through F-V21 named-tic inventory): [`tools/rigor-passes/commons_bonds_rigor_pass_2026-05-13_ch1_the_quiet_math_stage3_voice_polish_v1.0.0.md`](../rigor-passes/commons_bonds_rigor_pass_2026-05-13_ch1_the_quiet_math_stage3_voice_polish_v1.0.0.md)
- **Pass 3.3 + 3.4 split canonical example: [`tools/rigor-passes/commons_bonds_ch1_stage_3_pass_3_audience_load_REAUDIT_2026-05-17_PROPOSED.md`](../rigor-passes/commons_bonds_ch1_stage_3_pass_3_audience_load_REAUDIT_2026-05-17_PROPOSED.md)** — 40-character full-rigor + adversarial audit. §5.3 thread-pull synthesis is the canonical diagnostic format for the 3.4 pass.

---

## How to use this template

1. Confirm Stage 2 draft is committed to main + verified by PM session.
2. Fill in the `[BRACKET PLACEHOLDERS]` below.
3. Paste into a fresh session (or the same session that ran Stage 2 if bundled per the scale-down model).
4. Session produces four distinct rigor-pass artifacts (or one combined artifact with four labeled sections).
5. STOP at verdict; author ratifies before applying any spot-fixes.

**Per-prompt serial cadence (v2.0 Amendment B carry-forward).** Each pass fires in its own prompt: Pass 3.1 → author ratifies + spot-fixes apply → Pass 3.2 → author ratifies + spot-fixes apply → Pass 3.3 → author ratifies + spot-fixes apply → Pass 3.4 → author ratifies + spot-fixes apply. Not bundled into one session.

---

## Paste-text template

```
You are running Stage 3 of the v3.0 audience-aware drafting discipline
for [ARTIFACT NAME] (PM dashboard workstream #[N]). Your job: four
distinct rigor passes — Pass 3.1 fact-check + Pass 3.2 voice-polish +
Pass 3.3 audience-load acceptance + Pass 3.4 audience-load robustness —
against the Stage 2 draft. STOP at verdict + spot-fix recommendations
after each pass; do NOT apply spot-fixes to the draft.

== v3.0 discipline (extends v2.0 Amendment B) ==

Four DISTINCT passes, not bundled. v2.0 Amendment B established the
three-pass discipline; v3.0 splits Pass 3 audience-load into Pass 3.3
acceptance (does the target-audience character set return INCLUDE?) +
Pass 3.4 robustness (does the adversarial / detractor character set
find threads that would let them unwind the artifact?). Acceptance +
robustness use different character sets, different verdict scales, and
produce different diagnostic outputs.

Each pass produces its own list of findings. Pass 3.3 produces a final
include-vs-exclude verdict on the acceptance set. Pass 3.4 produces a
thread-pull synthesis verdict (the diagnostic is which threads
adversarial readers find, NOT pass/fail per character — adversarial
characters are SELECTED for hostile read and verdict-floor is EXCLUDE).

The discipline is empirically validated. The op-ed pipeline session
(commit 5167edd, 2026-05-10) ran its own three-pass Stage 3 and the
fact-check pass caught two real factual drifts (GPFG founding-date
conflation + Bondevik-coalition timing) that audience-load alone
would have missed. The Ch 1 Pass 3 REAUDIT v3 (2026-05-17) ran the
40-character full-rigor + adversarial set; the adversarial test
surfaced the Public Choice rent-seeking-engagement thread that
became a cross-chapter workstream (would have been missed by
acceptance-only test).

== Read in order before doing any work ==

1. THIS paste (the framing).
2. [STAGE 2 DRAFT PATH] (the artifact under audit).
3. [STAGE 1 BRIEF PATH] (canonical facts in §6; voice register in §5;
   audience pressure-test set in §1).
4. /Users/c17n/.claude/projects/-Users-c17n-commons-bonds/memory/feedback_audience_aware_drafting_discipline.md
   (v2.0 discipline; ratified 2026-05-10).
5. /Users/c17n/.claude/projects/-Users-c17n-commons-bonds/memory/feedback_voice_polish_pipeline.md
   (dump → sift → polish).
6. /Users/c17n/.claude/projects/-Users-c17n-commons-bonds/memory/feedback_substance_drives_length.md
   (no padding; no cutting to fit).
7. /Users/c17n/.claude/projects/-Users-c17n-commons-bonds/memory/feedback_verify_stale_memory_claims.md
   (verification discipline).
8. Canonical examples to mirror:
   - publishing/essays/noema-commons-bonds/rigor/stage-3-comparison_2026-05-10.md
   - tools/rigor-passes/commons_bonds_rigor_pass_2026-05-11_why_bonds_paragraph_include_vs_exclude_audience_load_v1.0.0.md

== Mission ==

Produce four distinct rigor-pass artifacts (or one combined artifact
with four labeled sections). For each pass, list findings + proposed
spot-fixes + severity. STOP at recommendations; author ratifies which
spot-fixes apply.

Per-prompt serial cadence: each pass fires in its own session-prompt;
author ratifies + spot-fixes apply before next pass fires. Not bundled.

== Pass 3.1: Fact-check ==

For every factual claim in the draft, verify against Stage 1 brief
§6 canonical-facts inventory:

- Named people: spelling, full names, titles, institutional
  affiliations
- Named places: spelling, geographic specificity
- Dates: specific YYYY-MM-DD; verify against §6
- Statistics / numbers: verify against §6
- Quotes: verbatim where claimed; verify against §6
- Scene-anchor sequences: order of events; specific concrete details
- Fact-relationships: who is whose what; which institution did which
  thing when
- Lineage / intellectual-history claims: dates of published works;
  argument attributions

For each discrepancy: cite draft line number + draft text + canonical
truth + recommended spot-fix.

Severity:
- **CRITICAL** — claim is factually wrong (would be caught by a
  fact-checker; publisher pre-publication review would flag).
- **HIGH** — claim is misleading or imprecise (could be challenged
  by a knowledgeable reader).
- **MEDIUM** — claim is technically defensible but loose
  (acceptable in trade prose but worth tightening).
- **LOW** — claim is accurate but the framing could be sharpened.

Bonus: surface any claims the draft makes that AREN'T in §6's
canonical-facts inventory (i.e., the drafter improvised). These are
the highest-risk for factual drift even if they happen to be correct.

== Pass 3.2: Voice-polish ==

For every paragraph, check for the LLM tics + voice issues that
trade-press editors flag:

- **Rule of three** — "A. B. C." constructions; flag if >2 in draft.
- **Em-dash crutches** — em-dashes used as connective tissue rather
  than as deliberate parenthetical extension or punch.
- **Tidy parallels** — "He did X. She did Y. They did Z." structures.
- **Hedge phrases** — "I will argue that…" / "It seems likely
  that…" / "Perhaps…"
- **Connective-tissue clichés** — "in short" / "ultimately" /
  "moreover" / "furthermore" / "that being said"
- **Meta-commentary** — "That is the whole sentence." / "What I
  mean to say is…" / "Let me explain…"
- **Expository flatness** — "The plain definition is this:" /
  "Here is what I think:" / "The argument is simple:"
- **Declarative-three-in-a-row** — three short declaratives in
  succession with no sentence-length variance.
- **Nostalgia / sentimentality tics** — "There are not many people
  like that anymore" / "Back when…"
- **Cadence repetition** — "It changed me. It humbled me. It made…"
  patterns.
- **Apparatus residue** — Greek letters, subscripts, integrals,
  acronyms appearing in body prose where Stage 1 brief §8 prohibits.

For each issue: cite draft line number + draft text + recommended
revision.

Severity:
- **HIGH** — issue actively damages the prose (reader trips over it).
- **MEDIUM** — issue is a flag but not a stopper.
- **LOW** — issue is style preference (e.g., one em-dash usage that
  could be a comma).

== Pass 3.3: Audience-load (acceptance) ==

Apply the **acceptance-test character set** from Stage 1 brief §1
to the full draft. The acceptance set is the target-audience set:
characters whose No vote kills the piece (Tier 1 gating) + whose Yes
vote amplifies the piece (Tier 2 pipeline-strengthening) + whose
experience the piece engages (Tier 3 cultural-resonance / accessibility
/ practitioner). Typically 15-25 characters total.

For each character:

- What does this character read for?
- What lands for this character in the draft?
- What flags for this character in the draft?
- Does the draft hold this character's attention through the close?

Score per character on the acceptance-test include-vs-exclude scale:

- **✓✓✓ INCLUDE** — strong yes for this audience; piece lands
  decisively.
- **✓✓ INCLUDE** — yes for this audience; piece lands.
- **✓ INCLUDE** — yes for this audience; piece lands with minor
  reservations.
- **NEUTRAL** — this audience is neither alienated nor strongly
  engaged.
- **⚠ EXCLUDE** — this audience may disengage; flag specific reason.
- **⚠⚠ EXCLUDE** — this audience actively rejects; flag specific
  reason.
- **⚠⚠⚠ EXCLUDE** — disqualifying for this audience; cannot ship
  to venue with this character as Tier 1.

Aggregate the tally across tiers:

- Tier 1 (gating audiences): if any character is ⚠⚠⚠, the piece
  cannot ship as-is.
- Tier 2 + Tier 3: tally include-vs-exclude weight.

Final acceptance verdict on include-vs-exclude basis:
- Total INCLUDE vs. NEUTRAL vs. EXCLUDE across all acceptance-test
  characters.
- Per-tier breakdown.

For each character returning EXCLUDE, propose specific spot-fixes
that would flip their verdict to INCLUDE without alienating other
characters.

== Pass 3.4: Audience-load (robustness) ==

Apply the **adversarial / detractor character set** to the full
draft. The adversarial set tests robustness: do hostile readers find
threads that would let them unwind the artifact? Typically 5-10
characters; selected for hostile read (industry-funded; predisposed-
hostile-by-financial-incentive; ideologically-opposed; trade-press
hostile reviewer; etc.). See `tools/drafting-templates/audience-
pressure-test-construction.md` §3 for adversarial character types.

**Verdict scale for adversarial characters (different from
acceptance):**

- **⚠ EXCLUDE** — would push back but the chapter holds against the
  push-back; thread is acknowledged.
- **⚠⚠ EXCLUDE** — would actively reject; finds load-bearing thread;
  chapter's structural moves don't disarm.
- **⚠⚠⚠ EXCLUDE** — would weaponize the chapter against itself;
  finds chapter-disqualifying thread.

NEUTRAL and INCLUDE verdicts are **not in scope** for adversarial
characters — they are selected for hostile read; verdict-floor is
EXCLUDE.

**The diagnostic is NOT pass/fail per character.** All adversarial
characters return EXCLUDE — that is expected. The diagnostic is
**which threads they collectively find**, and whether those threads
are:

- (a) **Load-bearing chapter claims** — chapter must hold its ground;
  spot-fix would damage acceptance-test verdicts. Disposition:
  acknowledge the thread + verify the chapter's structural moves
  disarm it sufficiently + cross-chapter handoff if the thread
  warrants further engagement at another chapter.
- (b) **Procedural / cosmetic flags** — spot-fixes could disarm the
  attack without damaging acceptance verdicts. Disposition: apply
  spot-fixes.

Produce a **thread-pull synthesis** as the canonical diagnostic
output (see canonical Ch 1 REAUDIT v3 §5.3 for format model):

| Thread | Pulled by adversarial chars # | Type (load-bearing / procedural) | Recommendation |
|---|---|---|---|

Final robustness verdict:
- **ROBUST** — no common load-bearing threads found; isolated
  procedural flags only (chapter holds against adversarial set).
- **CONDITIONALLY ROBUST** — common load-bearing thread found that
  the chapter's structural moves do disarm; thread acknowledged in
  the pre-pub review queue.
- **REQUIRES STRUCTURAL ENGAGEMENT** — common load-bearing thread
  found that the chapter does NOT disarm; cross-chapter workstream
  or chapter-level structural revision needed.

Pass 3.4 robustness verdict gates Stage 5 sign-off; REQUIRES
STRUCTURAL ENGAGEMENT routes to a cross-chapter workstream (per
pipeline doctrine §5 cross-chapter workstream lifecycle).

[INSERT IF STAGE 0 CARRY-FORWARD CONDITIONS:] **Stage 0 carry-forward
conditions verification.** The piece must satisfy [LIST CONDITIONS
e.g., "non-partisan framing — center-right policy reader must read
the piece as scholarly inventory, not authorial commitment"]. Apply
these as additional pressure-test characters in the audience-load
pass. If any condition fails: flag as ⚠⚠⚠ and propose specific
remediation.

== Pass 3.5: Developmental-edit (whole-chapter restoration lens) ==

Per v1.0.0 Amendment B (ratified 2026-05-18). Fires AFTER Pass 3.1
+ 3.2 + 3.3 + 3.4 have ratified-and-applied. Operates at
whole-chapter scale; catches what per-paragraph + per-character
passes miss.

What Pass 3.5 catches:

- **Emotional-arc continuity** — does the chapter's emotional
  trajectory build + land, or does it flatten at structural pivots?
- **Scene-anchor density** — are scene-anchors (sensory detail,
  spatial grounding, temporal anchoring) dense enough to carry the
  analytical load without losing the reader?
- **Sensory-detail restoration** — what specific images / sounds /
  textures were cut during Pass 3.2 chiseling that the
  whole-chapter read shows as needed restoration?
- **Voice-flow continuity** — does the prose's memoir / essay /
  analytical register hold across the chapter without breaks?
- **Cumulative-LLM-cadence residue** — Pass 3.2 caught individual
  tics, but did the CUMULATIVE effect of multiple tic-fixes produce
  flatness even though each fix was individually justified?
- **Reader-engagement at analytical pivots** — at the chapter's
  most analytically-loaded passages, does the reader's attention
  plausibly slip? (Cross-reference with Pass 3.3 acceptance-character
  expectations.)

**Remediation polarity: RESTORATION, not cutting.** Pass 3.5
findings recommend ADDING prose (scene-anchors, sensory detail,
breath, restoration of cut richness, faithfulness-of-the-model
lineage paragraphs, both/and reveal breath at pivots) — NOT further
compression. This is the methodological-clarity argument for Pass
3.5's separation from Pass 3.2: opposite polarities; folding would
lose the discipline each polarity needs.

Per-finding format (mirrors Pass 3.2 voice-polish artifact structure):

- **Finding ID:** F-DE-Ch<N>-K
- **Severity:** HIGH (significant emotional-arc breakage; cumulative
  flatness reaches gate-level severity); MEDIUM (noticeable flatness
  at specific section); LOW (style preference / restoration option)
- **Location:** line number + verbatim current text
- **Diagnosis:** what specifically reads as flat / compressed /
  lost-richness
- **Proposed rewrite:** specific prose; same canonical-facts + same
  consent gates + same named-subject discipline
- **Cross-pass flag:** whether the rewrite affects any prior Pass 1
  / Pass 2 / Pass 3 finding's disposition (should be rare since this
  is whole-chapter scale; surfaces when a prior Pass 3.2
  ratified-as-applied cut over-corrected at the whole-chapter scale)

Whole-chapter synthesis at end of artifact:

- **Cumulative diagnosis** — what produced the flatness? Over-
  compression? Held findings that should have applied? Applied
  findings that over-corrected?
- **Cumulative recommendation** — apply N rewrites; restore K
  paragraphs of cut richness; structural pacing adjustment.
- **Token-economy note** per Amendment A: Pass 3.5 is heavy (~50K-80K
  tokens per chapter session); fires per-chapter pre-publication, not
  on every prose edit.
- **Cross-chapter cascade flag** — if any rewrite would affect
  cross-chapter pacing or callback resonance, flag for the
  cross-chapter-developmental-coherence workstream (separate;
  fires after all per-chapter developmental edits land).

**Output artifact:** `tools/rigor-passes/ch<N>_developmental_edit_review_<date>.md`.

**Phase C workflow:** PROPOSED at session close; author ratifies via
separate session; Phase C application applies ratified rewrites to
chapter source; light Pass 3.3 (acceptance) re-fire recommended
after Phase C application; Pass 3.4 re-fire not routinely warranted.

**Canonical example:** Ch 1 developmental-edit review at
`tools/rigor-passes/ch1_developmental_edit_review_2026-05-18.md`
(first session of the workstream class; 3 HIGH + 7 MEDIUM + 3 LOW
findings; §5.1 cumulative diagnosis is the canonical format for the
whole-chapter synthesis).

== Verdict synthesis ==

Five verdicts (one per pass):

- **Pass 3.1 fact-check verdict** — total findings by severity;
  CRITICAL findings must be resolved before submission.
- **Pass 3.2 voice-polish verdict** — total findings by severity;
  HIGH findings should be resolved.
- **Pass 3.3 audience-load acceptance verdict** — total
  INCLUDE/EXCLUDE tally + final include-vs-exclude direction across
  acceptance-test character set.
- **Pass 3.4 audience-load robustness verdict** — thread-pull
  synthesis + ROBUST / CONDITIONALLY ROBUST / REQUIRES STRUCTURAL
  ENGAGEMENT verdict.
- **Pass 3.5 developmental-edit verdict** — cumulative diagnosis
  (over-compression / held-findings-should-have-applied / applied-
  findings-over-corrected); minimum-restoration set + medium-
  priority set + author-discretionary set; cross-chapter cascade
  flag.

Aggregate verdict:
- **READY TO SUBMIT AS-IS** — Pass 3.1 returns 0 CRITICAL; Pass 3.2
  returns 0 HIGH; Pass 3.3 returns net INCLUDE with no Tier-1
  EXCLUDE; Pass 3.4 returns ROBUST or CONDITIONALLY ROBUST; Pass
  3.5 returns 0 HIGH (or HIGH findings ratified-and-applied).
- **READY AFTER SPOT-FIXES** — specific spot-fixes itemized; piece
  flips to submit-ready once applied (across all five passes).
- **STRUCTURAL REVISION NEEDED** — findings cannot be addressed by
  spot-fixes; recommend re-firing Stage 2 with amended Stage 1
  brief, OR (for Pass 3.4 REQUIRES STRUCTURAL ENGAGEMENT) spin up a
  cross-chapter workstream per pipeline doctrine §5, OR (for Pass
  3.5 cross-chapter cascade flags) queue the cross-chapter
  developmental-coherence workstream.

== Output ==

Five artifacts (or one combined):
1. tools/rigor-passes/commons_bonds_rigor_pass_[DATE]_[SLUG]_stage3_pass_3_1_fact_check_v1.0.0.md
2. tools/rigor-passes/commons_bonds_rigor_pass_[DATE]_[SLUG]_stage3_pass_3_2_voice_polish_v1.0.0.md
3. tools/rigor-passes/commons_bonds_rigor_pass_[DATE]_[SLUG]_stage3_pass_3_3_audience_load_acceptance_v1.0.0.md
4. tools/rigor-passes/commons_bonds_rigor_pass_[DATE]_[SLUG]_stage3_pass_3_4_audience_load_robustness_v1.0.0.md
5. tools/rigor-passes/[SLUG]_developmental_edit_review_[DATE].md

Or, bundled (only when scale + scope justify):
- tools/rigor-passes/commons_bonds_rigor_pass_[DATE]_[SLUG]_stage3_four_pass_v1.0.0.md
  with four labeled sections.

== Hard constraints ==

- Do NOT apply spot-fixes to the draft. Author ratifies first.
- Do NOT re-write the draft. Four passes audit; remediation is
  separate.
- Do NOT propose meta-conclusions about the v3.0 discipline.
- Do NOT contact named subjects.
- DO flag ANY apparatus residue, named-subject consent issues, or
  Path B contamination — these are gating issues separate from the
  three passes.

== Branch discipline ==

Open fresh feature branch claude/[SLUG]-stage-3-rigor-<harness-id>
from current origin/main per tools/workstream-handoffs/README.md.

After commit lands on main: STOP. Report verdicts back to PM session +
author. Author ratifies which spot-fixes to apply; spot-fix application
is a separate session.
```

---

## Placeholders to fill

| Placeholder | What goes here |
|---|---|
| `[ARTIFACT NAME]` | Piece name |
| `[N]` | PM dashboard workstream number |
| `[STAGE 2 DRAFT PATH]` | Path to Stage 2 draft artifact |
| `[STAGE 1 BRIEF PATH]` | Path to Stage 1 brief |
| `[STAGE 0 CARRY-FORWARD CONDITIONS]` | If Stage 0 returned CONDITIONAL, list conditions to verify |
| `[DATE]` | Today's date in YYYY-MM-DD format |
| `[SLUG]` | Lowercase filename-friendly slug |

---

## Audit-existing-prose mode

For Stage 3 applied to existing prose (not Stage 2 fresh draft) — e.g., revising a chapter or applying a polish pass to a previously-ratified piece:

- Skip the §6-canonical-facts cross-check (no Stage 1 brief; treat the existing prose AS the canonical reference for §6-equivalent claims).
- Apply Pass 3.2 (voice-polish) + Pass 3.3 (acceptance) + Pass 3.4 (robustness) full strength.
- Apply Pass 3.1 (fact-check) only for time-sensitive claims (dates / counts / status / file paths) per verify-stale-memory-claims discipline.
- Cross-artifact coherence is the responsibility of Stage 1c (pipeline doctrine §3) — not a Pass 4 here. If Stage 1c was skipped (legacy artifact), run it before Pass 3.3 + 3.4 fire.

---

## Bundled-Stage 1+2+3 mode (in-book defense paragraphs)

For ~200-400w in-book defense paragraphs (e.g., flagship-term name-defense paragraphs):

- Bundle Stage 1 inline (5-10 lines of audience-load brief + canonical-facts inventory).
- Run Stage 2 audience-blind drafting in the same session.
- Apply a single audience-load pass (Pass 3.3 acceptance only) — Pass 3.1 + Pass 3.2 can be inline during drafting since the piece is short enough that drift won't compound. Pass 3.4 (robustness) typically not required for defense paragraphs unless the paragraph is itself the audience-pressure-test focal point.
- Output: drafting artifact + audience-load rigor pass (the bond-defense / flagship-terms model).

---

## What Stage 3 does NOT do

- Does NOT apply spot-fixes to the draft. The author ratifies which fixes to apply; application is a separate session.
- Does NOT re-draft sections. Four passes audit; remediation is separate.
- Does NOT iterate / re-test after spot-fix application (light re-fires per change-cascade routing are separate sessions).
- Does NOT propose meta-conclusions about the discipline framework.
- Does NOT contact named subjects.

If Stage 3 surfaces a STRUCTURAL revision need (rather than spot-fixes), it should flag and STOP — the right move is to amend the Stage 1 brief + re-fire Stage 2, not to patch around structural issues at Stage 3.

If Pass 3.4 surfaces a load-bearing thread that crosses chapters (per Ch 1 REAUDIT v3 Public-Choice example), spin up a cross-chapter workstream per pipeline doctrine §5.

---

*End of Stage 3 template (v3.0).*
