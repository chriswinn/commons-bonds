# The remaining chapter redrafts: one chapter per session (kickoff, 2026-11-12)

**Status:** PROPOSED (internal scaffolding). Use this for Chapters 2, 3, 4, 6, 7, 8, 9 and 10, one chapter per
fresh session. Chapters 1 and 5 are handled by the comparison (`dinner-table-compare-kickoff_2026-11-12.md`).
Confirm the session is on Fable; if not, say so first.

## Paste line (put the chapter number in place of N)

```
Read CLAUDE.md, STATE.md, tools/drafting-templates/commons_bonds_house-style-sheet_v1.0.2.md and tools/workstream-handoffs/chapter-redrafts-kickoff_2026-11-12.md. Run it for Chapter N.
```

If a newer version of the style sheet exists, read that one instead.

## THE METHOD (the author sets this line after the Ch 1 and Ch 5 comparison)

> **METHOD: NOT YET CHOSEN.**

The author is choosing between two ways of redrafting. Both aim at the same thing: prose with pace and pull that
a reader can follow in one pass.

- **Method P, pace and pull.** Redraft fresh from the chapter map for order, people before abstractions,
  reasoning in the joints and the strongest thing last (the engagement lenses in
  `tools/memory/feedback_engagement_lenses.md`). The model is the Ch 5 rings redraft.
- **Method D, dinner-table voice with pace and pull.** Everything in Method P, written by explaining: for each
  paragraph, answer "what is this saying?" as if the author had asked across a dinner table, one step per
  sentence, and use that answer as the text. No compression, no verdict closers. The model is whichever
  dinner-table draft the author picked in the comparison.

**If the line above still says NOT YET CHOSEN, stop and ask the author which method to use. Do not guess.**
When he chooses, the session that hears it replaces that line with "METHOD: P" or "METHOD: D," the date and his
words, and names the model text. If he chooses P, the style sheet's "first rule" must be amended to match before
any chapter is drafted, in the same commit. If he chooses a mix (for example D for argument and P for scenes),
record exactly that.

## Order

Chapters that wait on nothing first: **2, 10, 4, 3.** Then **7, 9, 6, 8.** The author may change the order.

## Before you draft

1. **Read the chapter's map:** `tools/workstream-handoffs/chapter-maps_2026-11/chNN-map.md`, and the index beside
   it for calls that have to be answered the same way in two chapters.
2. **Check the map's calls.** Where the author has answered, his answers govern. Where he has not, ask him now,
   in one short message, with the map's recommendation beside each call. "Yes to all" is a complete answer. Do
   not draft on unanswered structure calls unless he tells you to use the recommendations.
3. **For Chapters 6 to 9, read the rebuild brief:** `research/story-drafts/chN-blind-brief-v4_2026-11.md`. Check
   its "Blocked on Session A" list against `origin/main`. TA v2.0.1 was ratified on 2026-11-12 and the ledger was
   amended, so most items should be there. If one is not, stop and tell the author.
4. **Every figure comes from** `manuscript/ledgers/_CANONICAL_FIGURE_LEDGER.md` as it stands today. Do not load
   the Technical Appendix.
5. **Read only this chapter** (`manuscript/chapters/`), and only the short passages of other chapters that the
   map or brief names. Use the current chapter for content, never for wording.

## Drafting

- Write the chapter fresh in the chosen method. Do not match the existing prose.
- **Protected everywhere:** quotations; the sayings of the author's family; facts and figures; any passage the
  author names as his own.
- **Nothing invented:** no fact, scene, quotation, feeling or memory. Where the map says only the author can
  supply something (Ch 3's three passages, Ch 10's hospital sentence and his standing toward the Black Hills),
  leave a hidden comment and write nothing.
- One vantage, the author's. "You" only for what any reader anywhere has; "we" only author plus reader or a
  group he names; countries named.
- Where the record shows a party seeking rent and shifting a cost, say so plainly from the record; allege no
  intent the record does not show.
- Length follows substance. No minimum and no maximum. Long sentences and comma insertions are fine.
- Living people named from on-record statements get a note for the consent tracker; living private people stay
  unnamed.

## What you hand back

1. The draft at `tools/workstream-handoffs/chapter-redrafts_2026-11/chNN-redraft_<date>.md`. **Do not overwrite
   the chapter in `manuscript/chapters/`.** It is promoted only on the author's word.
2. A fact table: every number, date, name and quotation in the draft against its ledger row or source.
3. Short change notes: which map calls you applied and how; what was protected; what you could not source and
   left as a marked gap; word counts of the old chapter and the draft.
4. One strongest-critic read, run once: the places a hostile but fair reader would stop, as questions for the
   author, seven at most.
5. A PDF of the draft for the author's line-by-line redline (PDFs are not committed; send it to him).
6. Checks: `bash tools/scripts/check-corpus-invariants.sh` HIGH = 0. Use `check-prose-clarity.py` only to find
   tangles; none of its counts is a target.

## After the author's redline

Apply his redline exactly. Then a grammar-and-punctuation polish, mechanical only, with every change listed.
Then promotion on his word, with the old chapter archived, STATE.md's line for the chapter updated in the same
commit, and any new or changed figure given a ledger row and a gate pattern in that commit.

## Rules

- One chapter per session. No delegated or parallel drafting sessions.
- If context runs short, finish the section you are in, say where you stopped, and write a handoff.
- Internal scaffolding merges to main at session close with pre-push reconciliation. End with the three lines.
