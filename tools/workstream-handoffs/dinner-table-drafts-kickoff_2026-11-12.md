# Dinner-table drafts of Ch 1 and Ch 5: the WRITING session (kickoff, 2026-11-12)

**Status:** PROPOSED (internal scaffolding). One fresh session. Confirm the session is on Fable; if not, say so first.
This session **writes and does not judge.** A separate session compares the versions
(`dinner-table-compare-kickoff_2026-11-12.md`).

## Paste line

```
Read CLAUDE.md, STATE.md, tools/drafting-templates/commons_bonds_house-style-sheet_v1.0.1.md and tools/workstream-handoffs/dinner-table-drafts-kickoff_2026-11-12.md. Run it.
```

## Why this session exists

The author wants to see Chapters 1 and 5 written in the voice he approved on 2026-11-12, the **dinner-table rule**
(style sheet, "The first rule"), so he can compare them with the versions that exist and decide which to send to
William Darity. Both chapters and the Technical Appendix v2.0.1 are the Darity package.

## The one thing to understand before you write a word

When you are asked to "write prose," you compress: you drop steps, pack three ideas into one sentence and reach
for a shape. When you are asked to explain something to the author, you write plainly, one step at a time. On
2026-11-12 he could not follow two compressed passages, and then pointed out that the chat explanation of what
they meant was clearer than the rewritten prose. **So do not rewrite. Explain.** For each paragraph, answer the
question "what is this saying?" as if he had asked you across a dinner table, and use that answer as the text.
If your explanation is clearer than the paragraph, the explanation is the paragraph.

He was trained at IBM to speak in a way that is not regional and has no jargon, so people anywhere feel included.
He speaks plainly by habit. He does not end paragraphs on clever verdicts ("It launders it."). A short sentence
that states a fact is fine ("I was one of them.").

## Rules for both chapters

- Same sections, same order, same facts, same figures as the content source. This is a change of voice, not of
  structure. Do not act on the chapter maps' open calls; the author has not answered them.
- No invented fact, scene, quotation, feeling or memory. Nothing new about the author. Darity is quoted only from
  published work.
- One vantage, the author's. "You" only for what any reader anywhere has. "We" only for author plus reader, or a
  group he names. Name the United States.
- Where the record shows a party seeking rent and shifting a cost, say so plainly from the record. Allege no
  intent the record does not show.
- Length follows substance: no minimum, no maximum. Long sentences and comma insertions are fine. Expect both
  drafts to come out longer than their sources, and report by how much.
- No labels ("what this means is"), no announcing what the next paragraph will do, no notes about sources inside
  the prose.
- Do not edit either chapter in `manuscript/chapters/`, the TA, the figure ledger, the gate files or STATE.md.
- Do Ch 5 first, then Ch 1. If context runs short, finish the chapter you are in, say where you stopped, and
  leave the other for a new session.

## Chapter 5

- **Content source:** `manuscript/chapters/Chapter__5_TheAccountabilityGap.md` (promoted 2026-11-12: the rings
  redraft with the author's twelve decisions and three later line edits applied).
- **Read also:** `tools/workstream-handoffs/pull-pass_2026-11/ch5-decision-answers_2026-11-11.md` (what he decided
  and why) and `tools/workstream-handoffs/pull-pass_2026-11/question-map.md` (what each section hands to the next).
- **Protected, word for word:**
  - In *The family*: from "Their own doctor still opposed the device." to the end of that paragraph, and the
    whole next paragraph ("This was not one family's bad luck…").
  - The author's 2008 account: from "I was doing well at the time." through "…and who stood on the far side of
    the transfer."
  - "The United States holds one more compact… would not mean being left with nothing."
  - In *Restitution and foreclosure*: "I should say plainly why. I am not a descendant… given their working lives
    to it."; "Applied to that debt, the Restitution Bond is a reparations bond… until it is paid."; "One question
    this book does not presume to close."; "An honest ledger can name a line… not this book's to enter."
  - His lines "did not produce," "cashed out," "left standing where it landed," "the bill comes due."
  - Every quotation, including the five from Butler and the two from Darity. Leave the two hidden page-number
    comments where they are.
- Everything else is explained afresh, paragraph by paragraph.
- **Write to:** `tools/workstream-handoffs/pull-pass_2026-11/ch5-dinner-table_2026-11.md`

## Chapter 1

- **Content source:** `manuscript/chapters/Chapter__1_TheQuietMath.md`. This is the only chapter the author has
  redlined by hand (commit `0fca4465`, 2026-06-12). **His redline is the best evidence there is of how he
  writes.** Read the diff of that commit before you start, and where a sentence is one he rewrote himself, keep
  his wording unless it is hard to follow.
- **Do not read** `ch1-pace-redraft_2026-11-10.md`. It was written in the compressed manner and would pull you
  toward it.
- **Protected, word for word:** every quotation; the father's, the grandfather's, the colleague's, the children's
  and the nephew's words; every fact and number. The list of eighteen sayings and twenty-five figures is in
  `tools/workstream-handoffs/pull-pass_2026-11/ch1-CHANGES.md` (read only its "Checks" section).
- This chapter is memory. You may put what is on the page in a plainer order and plainer words. You may not add
  to it: no new detail, no new feeling, no reaction he did not write. If a passage is already plain and already
  sounds like a person talking, leave it.
- The author's travel story is not written yet. Leave one hidden comment where the map places it (after the work
  section, before the plane): `<!-- THE ROAD: the author's section, to be written by him -->`. Write nothing there.
- The former spouse is a living person: nothing about her beyond what the chapter already says.
- **Write to:** `tools/workstream-handoffs/pull-pass_2026-11/ch1-dinner-table_2026-11.md`

## Checks, for each chapter

1. Every figure in the content source appears in the draft, unchanged, and no new one. Make the table.
2. Every protected passage and quotation is present, string for string.
3. `bash tools/scripts/check-corpus-invariants.sh`: HIGH = 0.
4. Three sentences on what you changed in kind, and the word counts of source and draft.

Commit, merge to main with pre-push reconciliation, and end with the three lines. Do not say which version is
better; that is the next session's job, and the author's decision.
