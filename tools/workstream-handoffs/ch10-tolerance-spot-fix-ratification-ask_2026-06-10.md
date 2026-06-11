# Ch 10 wind-tunnel tolerance spot-fix — ratification ask (2026-06-10)

**Status:** PROPOSED — prose edit applied on feature branch
`claude/ch10-tolerance-fix-260610-2ca75e`, held with `MERGE-HOLD: pending author
ratification` per the task direction to present end-user-facing prose edits for
ratification. One author yes/no merges it.

**Ruling being applied:** item G,
[`research/story-drafts/ch1-bone-sense-moments_2026-06-04.md:123`](../../research/story-drafts/ch1-bone-sense-moments_2026-06-04.md)
(author, RATIFIED 2026-06-04): *"Thousandth of an inch" — REMOVE (author does NOT
recall it). It drifted in and hardened across drafts; it is NOT author-grounded.
Describe the grandfather's wind-tunnel-model precision WITHOUT any specific
invented tolerance.* Ch 1 was corrected per this ruling (current
`Chapter__1_TheQuietMath_Draft.md` carries no tolerance); Ch 10 had not been.

## The edit (Chapter_10_CommonBonds.md, grandfather/wind-tunnel section)

**Before:**
> He built scale aircraft and spacecraft components out of wood and metal and
> resin, accurate to a thousandth of an inch, so that the tunnel would tell the
> truth about a full-size design that did not yet exist.

**After (Option A — pure deletion, applied):**
> He built scale aircraft and spacecraft components out of wood and metal and
> resin, so that the tunnel would tell the truth about a full-size design that
> did not yet exist.

**Options considered:**
- **Option A (applied; recommended):** delete the appositive, change nothing
  else. Zero new unratified prose. Precision/faithfulness is already carried two
  sentences later ("Build it faithfully enough that reality will not lie when it
  is run against your work") and again in the framework-as-model paragraph
  ("built faithfully enough that the world will not lie"). Adding a third
  faithfulness phrase at this sentence would over-ring the wind-tunnel bell
  (cf. item E's ~twice ceiling for Ch 1).
- **Option B:** re-voice as "…wood and metal and resin, built true, so that the
  tunnel would tell the truth…" — echoes Ch 1's "Build it true" register but
  adds new prose and a third bell-ring.
- **Option C:** re-voice with a non-numeric precision word ("exact enough
  that…") — permitted by the ruling but introduces new unratified wording.

**Recommendation + reasoning:** Option A. It is the only variant that is purely
the flagged fix (deletion of the non-author-grounded claim) with no new prose to
ratify; the paragraph's rhythm survives (materials triad → purpose clause →
spaceflight-stakes close) and the faithfulness register is supplied by the two
adjacent paragraphs, matching corrected Ch 1.

## Automatic-on-edit cascade (run 2026-06-10, edited paragraph scope)

- **Pass 3.1 fact-check (light):** clean. Remaining claims in the paragraph are
  all substrate-grounded (NASA Langley; model maker in the wind tunnels;
  wood/metal/resin; scale aircraft + spacecraft components; patented work;
  spaceflight stakes). No invented specifics remain.
- **Pass 3.2 voice-polish (light):** clean. No em-dashes introduced; single
  comma before the "so that" purpose clause reads naturally; no LLM-cadence
  tics introduced.
- **Stage 1c-light cross-artifact coherence:** the edit ALIGNS Ch 10 with
  corrected Ch 1. It DIVERGES from three sibling artifacts that still carry the
  invented tolerance — see below.

## Sibling occurrences of the invented tolerance (out of scope here; flagged)

Live, publisher-facing — need the same item-G application by their owning
sessions:

1. `manuscript/chapters/_AUTHORSNOTE_ON_WINDTUNNELS_AND_AI.md:13` — "accurate
   to a thousandth of an inch". (Per STATE.md 06-10 the redraft-compare campaign
   is SUPERSEDED-CLOSED — author direction: chapters get whole-cloth redo. Any
   whole-cloth redo drafts from current canon, which makes removing the invented
   tolerance from canon MORE urgent, not less: the ruling's drift-hardening risk
   is exactly re-drafting from contaminated substrate.)
2. `publishing/book-proposal/00_overview.md:65` — "accurate to a thousandth of
   an inch" in the grandfather paragraph. **Time-sensitive:** 00_overview was
   RATIFIED 06-09 (Stage 5) and proposal assembly targets ~Jun 14–20 before the
   Wave-1 agent gate; the invented tolerance would otherwise ship to agents.
   (Book-proposal sprint owns this file.)

Internal substrate (lower priority): `research/story-drafts/ch1-wholecloth-draft_2026-06-04.md:64`.
Archived/audit-trail copies (Ch 1 REGRESSED archive, Atlantic parallel-draft
archive, rigor-pass history) intentionally left untouched per archival policy.

A background-task chip was also surfaced to the author for items 1–2.

## Close-out

On author ratification of Option A: merge the feature-branch prose commit to
`origin/main` per merge-on-ratification (the hold clears), update the STATE.md
chapters-row note, and archive this handoff.
