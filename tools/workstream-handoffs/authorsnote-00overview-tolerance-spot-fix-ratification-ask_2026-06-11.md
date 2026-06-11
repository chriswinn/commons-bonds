# Author's Note + 00_overview wind-tunnel tolerance spot-fix — ratification ask (2026-06-11)

**Status:** PROPOSED — prose edits applied on feature branch
`claude/tolerance-spot-fix-260611-2c3b1b`, held with `MERGE-HOLD: pending author
ratification` per the Interactive Ratification Protocol for end-user-facing
prose. One author yes/no merges both.

**Ruling being applied:** item G,
[`research/story-drafts/ch1-bone-sense-moments_2026-06-04.md:123`](../../research/story-drafts/ch1-bone-sense-moments_2026-06-04.md)
(author, RATIFIED 2026-06-04): *"Thousandth of an inch" — REMOVE (author does NOT
recall it). It drifted in and hardened across drafts; it is NOT author-grounded.
Describe the grandfather's wind-tunnel-model precision WITHOUT any specific
invented tolerance.* Ch 1 was corrected per this ruling; Ch 10's fix is PROPOSED
on `claude/ch10-tolerance-fix-260610-2ca75e` (its own MERGE-HOLD, separate
ratification — see
`tools/workstream-handoffs/ch10-tolerance-spot-fix-ratification-ask_2026-06-10.md`).
These two files were the last live publisher-facing instances.

## Edit 1 (`manuscript/chapters/_AUTHORSNOTE_ON_WINDTUNNELS_AND_AI.md:13`)

**Before:**
> Model-making at Langley meant building scale aircraft and spacecraft
> components — wood, metal, resin, accurate to a thousandth of an inch — so the
> wind tunnel would tell the truth about full-size designs that did not yet
> exist.

**After (Option A — pure deletion, applied):**
> Model-making at Langley meant building scale aircraft and spacecraft
> components — wood, metal, resin — so the wind tunnel would tell the truth
> about full-size designs that did not yet exist.

## Edit 2 (`publishing/book-proposal/00_overview.md:65`)

**Before:**
> Pooh, as the family called him, built scale aircraft and spacecraft
> components accurate to a thousandth of an inch, so the tunnel would tell the
> truth about a full-size design that did not yet exist.

**After (Option A — pure deletion, applied):**
> Pooh, as the family called him, built scale aircraft and spacecraft
> components, so the tunnel would tell the truth about a full-size design that
> did not yet exist.

**Time-sensitivity:** 00_overview was RATIFIED 06-09 (Stage 5); proposal
assembly targets ~Jun 14–20 before the Wave-1 agent-query gate. Without this
fix the invented tolerance ships to literary agents.

## Options considered (both edits)

- **Option A (applied; recommended):** delete the invented tolerance, change
  nothing else. Zero new unratified prose — the only variant that is purely the
  flagged fix. In the Author's Note, the faithfulness/precision register is
  already carried two paragraphs later ("building something faithful enough
  that the world will not lie about it") and in the book-is-a-model paragraph;
  in 00_overview it is carried by the truth-telling purpose clause, the two
  named patents, and the spaceflight close. Matches the Ch 10 precedent and
  corrected Ch 1.
- **Option B:** re-voice with Ch 1's "built true" faithfulness language — adds
  new unratified prose and over-rings the wind-tunnel bell (the Author's Note
  already rings it twice downstream).
- **Option C:** non-numeric precision word ("machined to exactness") —
  permitted by the ruling but introduces new unratified wording for no gain.

## Automatic-on-edit cascade (run 2026-06-11, edited-paragraph scope)

- **Pass 3.1 fact-check (light): clean.** Author's Note ¶13 remaining claims
  are all substrate-grounded (Langley model-making; wood/metal/resin; tool bit
  for resin-impregnated fiberglass laminates + zero-gravity liquid-waste feed
  system per the patent record; lunar program; spaceflight stakes).
  00_overview ¶65 remaining claims are pre-existing and Stage-5-ratified
  06-09; the edit is pure deletion. No invented specifics remain in either
  paragraph.
- **Pass 3.2 voice-polish (light): clean.** Author's Note: pre-existing
  em-dash pair now encloses the bare materials triad; no new em-dashes. The
  00_overview sentence keeps the comma + "so" purpose clause, matching the
  Ch 10 fixed register. No LLM-cadence tics introduced.
- **Stage 1c-light cross-artifact coherence:** with these edits plus the
  in-flight Ch 10 fix, all live publisher-facing wind-tunnel passages align
  with corrected Ch 1 (precision via faithfulness language, no number). NB:
  `publishing/book-proposal/rigor/00_overview-pass-3.5-developmental-edit_2026-06-09.md:36`
  cited the tolerance as defensible scene-anchor density — that finding
  predates the item-G application to this file; the ruling overrides, and the
  artifact stays untouched as audit trail.

## Coordination — book-proposal sprint session

Per STATE.md §Active workstreams, `claude/book-proposal-sprint-260603-e402b7`
is LIVE and owns `publishing/book-proposal/`. Checked before editing
(2026-06-11): the sprint branch is even with `origin/main` (`2c6d5e3`, nothing
unmerged) and its worktree is clean on `publishing/book-proposal/` — no
collision risk. On ratification this fix fast-forwards to `origin/main` and the
sprint session inherits it through its normal pre-push reconciliation
(`git rebase origin/main`). The STATE.md book-proposal row carries the pointer
so the sprint session sees the hold before assembly.

## Also fixed in this branch (internal scaffolding, no ratification needed)

`research/story-drafts/ch1-wholecloth-draft_2026-06-04.md:64` — same pure
deletion. Internal substrate; fixed so any whole-cloth redraft drafting from it
does not re-import the invented tolerance (the ruling's drift-hardening risk).
Archived/audit-trail copies (rigor-pass history, sign-offs, deep-pass
artifacts) intentionally left untouched per archival policy.

## Close-out

On author ratification of Option A for both edits: fast-forward the
feature-branch prose commit to `origin/main` per merge-on-ratification (the
hold clears), update the STATE.md chapters + book-proposal rows, and archive
this handoff. If the author instead prefers Option B/C wording for either
file, apply in this branch and re-run the light cascade before merging.
