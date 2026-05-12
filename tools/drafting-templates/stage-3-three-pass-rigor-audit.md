# Stage 3 — Three-Pass Rigor Audit (Template)

**Purpose.** Post-draft rigor on a Stage 2 audience-blind flow draft (or an existing piece of prose). Three distinct passes — fact-check + voice-polish + audience-load — each catching what the others miss.

**When to use.** Required for any publisher-facing prose >~500w before submission. Lighter version (single audience-load pass) acceptable for in-book defense paragraphs.

**Critical discipline (v2.0 Amendment B).** Three DISTINCT passes, not bundled. The op-ed pipeline workstream demonstrated empirically that the fact-check pass catches real factual drift that audience-load alone would miss.

**Canonical examples.**
- Stage 3 comparison verdict: [`tools/rigor-passes/commons_bonds_rigor_pass_2026-05-10_noema_stage3_comparison_v1.0.0.md`](../rigor-passes/commons_bonds_rigor_pass_2026-05-10_noema_stage3_comparison_v1.0.0.md)
- Audience-load pass: [`tools/rigor-passes/commons_bonds_rigor_pass_2026-05-11_why_bonds_paragraph_include_vs_exclude_audience_load_v1.0.0.md`](../rigor-passes/commons_bonds_rigor_pass_2026-05-11_why_bonds_paragraph_include_vs_exclude_audience_load_v1.0.0.md)
- Op-ed Stage 3 (self-applied): see op-ed pipeline session commit `5167edd` — the session's own Stage 3 caught real GPFG / Bondevik factual drift

---

## How to use this template

1. Confirm Stage 2 draft is committed to main + verified by PM session.
2. Fill in the `[BRACKET PLACEHOLDERS]` below.
3. Paste into a fresh session (or the same session that ran Stage 2 if bundled per the scale-down model).
4. Session produces three distinct rigor-pass artifacts (or one combined artifact with three sections).
5. STOP at verdict; author ratifies before applying any spot-fixes.

---

## Paste-text template

```
You are running Stage 3 of the v2.0 audience-aware drafting discipline
for [ARTIFACT NAME] (PM dashboard workstream #[N]). Your job: three
distinct rigor passes — fact-check + voice-polish + audience-load —
against the Stage 2 draft. STOP at verdict + spot-fix recommendations;
do NOT apply spot-fixes to the draft.

== v2.0 Amendment B discipline ==

Three DISTINCT passes, not bundled. Each pass catches what the others
miss. Each pass produces its own list of findings; the audience-load
pass produces a final include-vs-exclude verdict.

The discipline is empirically validated. The op-ed pipeline session
(commit 5167edd, 2026-05-10) ran its own three-pass Stage 3 and the
fact-check pass caught two real factual drifts (GPFG founding-date
conflation + Bondevik-coalition timing) that audience-load alone
would have missed.

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
   - tools/rigor-passes/commons_bonds_rigor_pass_2026-05-10_noema_stage3_comparison_v1.0.0.md
   - tools/rigor-passes/commons_bonds_rigor_pass_2026-05-11_why_bonds_paragraph_include_vs_exclude_audience_load_v1.0.0.md

== Mission ==

Produce three distinct rigor-pass artifacts (or one combined artifact
with three labeled sections). For each pass, list findings + proposed
spot-fixes + severity. STOP at recommendations; author ratifies which
spot-fixes apply.

== Pass 1: Fact-check ==

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

== Pass 2: Voice-polish ==

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

== Pass 3: Audience-load ==

Apply the audience pressure-test character set from Stage 1 brief §1
to the full draft. For each character:

- What does this character read for?
- What lands for this character in the draft?
- What flags for this character in the draft?
- Does the draft hold this character's attention through the close?

Score per character on the standard include-vs-exclude scale:

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

Final verdict on include-vs-exclude basis:
- Total INCLUDE vs. NEUTRAL vs. EXCLUDE across all characters.
- Per-tier breakdown.

For each character returning EXCLUDE, propose specific spot-fixes
that would flip their verdict to INCLUDE without alienating other
characters.

[INSERT IF STAGE 0 CARRY-FORWARD CONDITIONS:] **Stage 0 carry-forward
conditions verification.** The piece must satisfy [LIST CONDITIONS
e.g., "non-partisan framing — center-right policy reader must read
the piece as scholarly inventory, not authorial commitment"]. Apply
these as additional pressure-test characters in the audience-load
pass. If any condition fails: flag as ⚠⚠⚠ and propose specific
remediation.

== Verdict synthesis ==

Three verdicts (one per pass):

- **Fact-check verdict** — total findings by severity; CRITICAL
  findings must be resolved before submission.
- **Voice-polish verdict** — total findings by severity; HIGH
  findings should be resolved.
- **Audience-load verdict** — total INCLUDE/EXCLUDE tally + final
  include-vs-exclude direction.

Aggregate verdict:
- **READY TO SUBMIT AS-IS** — fact-check returns 0 CRITICAL; voice-
  polish returns 0 HIGH; audience-load returns net INCLUDE with no
  Tier-1 EXCLUDE.
- **READY AFTER SPOT-FIXES** — specific spot-fixes itemized; piece
  flips to submit-ready once applied.
- **STRUCTURAL REVISION NEEDED** — findings cannot be addressed by
  spot-fixes; recommend re-firing Stage 2 with amended Stage 1
  brief.

== Output ==

Three artifacts (or one combined):
1. tools/rigor-passes/commons_bonds_rigor_pass_[DATE]_[SLUG]_stage3_fact_check_v1.0.0.md
2. tools/rigor-passes/commons_bonds_rigor_pass_[DATE]_[SLUG]_stage3_voice_polish_v1.0.0.md
3. tools/rigor-passes/commons_bonds_rigor_pass_[DATE]_[SLUG]_include_vs_exclude_audience_load_v1.0.0.md

Or, bundled:
- tools/rigor-passes/commons_bonds_rigor_pass_[DATE]_[SLUG]_stage3_three_pass_v1.0.0.md
  with three labeled sections.

== Hard constraints ==

- Do NOT apply spot-fixes to the draft. Author ratifies first.
- Do NOT re-write the draft. Three passes audit; remediation is
  separate.
- Do NOT propose meta-conclusions about the v2.0 discipline.
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
- Apply Pass 2 (voice-polish) + Pass 3 (audience-load) full strength.
- Apply Pass 1 (fact-check) only for time-sensitive claims (dates / counts / status / file paths) per verify-stale-memory-claims discipline.
- Add a Pass 4 (consistency check) — does the prose align with current canonical state of the framework (apparatus register decisions, flagship-term name-defenses, cross-chapter consistency canonical choices)?

---

## Bundled-Stage 1+2+3 mode (in-book defense paragraphs)

For ~200-400w in-book defense paragraphs (e.g., flagship-term name-defense paragraphs):

- Bundle Stage 1 inline (5-10 lines of audience-load brief + canonical-facts inventory).
- Run Stage 2 audience-blind drafting in the same session.
- Apply a single audience-load pass (Pass 3 only) — Pass 1 + Pass 2 can be inline during drafting since the piece is short enough that drift won't compound.
- Output: drafting artifact + audience-load rigor pass (the bond-defense / flagship-terms model).

---

## What Stage 3 does NOT do

- Does NOT apply spot-fixes to the draft. The author ratifies which fixes to apply; application is a separate session.
- Does NOT re-draft sections. Three passes audit; remediation is separate.
- Does NOT iterate / re-test after spot-fix application.
- Does NOT propose meta-conclusions about the discipline framework.
- Does NOT contact named subjects.

If Stage 3 surfaces a STRUCTURAL revision need (rather than spot-fixes), it should flag and STOP — the right move is to amend the Stage 1 brief + re-fire Stage 2, not to patch around structural issues at Stage 3.

---

*End of Stage 3 template.*
