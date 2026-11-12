# Ch 5: dinner-table-voice test redraft, for comparison (kickoff, 2026-11-12)

**Status:** PROPOSED (internal scaffolding). One fresh session. Confirm the session is on Fable; if not, say so first.

## Paste line

```
Read CLAUDE.md, STATE.md, tools/drafting-templates/commons_bonds_house-style-sheet_v1.0.1.md and tools/workstream-handoffs/ch5-dinner-table-test-kickoff_2026-11-12.md. Run it.
```

## What this is

A test. Chapter 5 was promoted on 2026-11-12 (`manuscript/chapters/Chapter__5_TheAccountabilityGap.md`): the rings
redraft with the author's twelve decisions applied. Its structure, order and facts are settled, but most of its
prose was written in a compressed manner the author does not speak in. He approved the **dinner-table rule**
(style sheet, "The first rule") and wants to see the whole chapter written that way, so he can put the two side
by side and decide which to keep. **Do not edit the promoted chapter.** Write the test to a new file.

## The one thing to understand before you start

When you are asked to "write prose," you compress: you drop steps, pack three ideas into a sentence and reach
for a shape. When you are asked to explain something to the author, you write plainly, one step at a time. He
could not follow two compressed passages on 2026-11-12, and then pointed out that the chat explanation of what
they meant was clearer than the rewritten prose. **So do not rewrite. Explain.** For each paragraph, answer the
question "what is this saying?" as if he had asked you across a dinner table, and use that answer as the text.
If your explanation is clearer than the paragraph, the explanation is the paragraph.

## Steps

1. Read the promoted chapter and `tools/workstream-handoffs/pull-pass_2026-11/ch5-decision-answers_2026-11-11.md`.
   Read `tools/workstream-handoffs/pull-pass_2026-11/question-map.md` for what each section hands to the next.
2. **Protected, word for word:** every wording the answers file marks confirmed or agreed (the Butler family
   paragraph, the profession paragraph with Epperly, the vantage line, the "reparations bond" sentence, the
   empty-line sentences, the 2008 "distance closes" sentence, the Social Security opening); the author's 2008
   account; his lines ("did not produce," "cashed out," "left standing," "the bill comes due"); every quotation.
3. **Everything else, paragraph by paragraph, in the dinner-table voice.** Same sections, same order, same facts,
   same figures. One step per sentence, in the order a person needs them. Plain words; no jargon; no idiom tied to
   one country. A short sentence is fine when it states a fact; a short verdict on what was just said comes out.
   No labels ("what this means is"), no announcing what the next paragraph will do. Apply the person-and-place
   rules: the author is "I"; "you" only for what any reader anywhere has; "we" only author plus reader or a
   group he names; name the United States. Where the record shows a party seeking rent and shifting a cost,
   say so plainly from the record; allege no intent the record does not show.
4. **Write it to** `tools/workstream-handoffs/pull-pass_2026-11/ch5-dinner-table-test_2026-11.md`.
5. **Checks.** Every figure in the promoted chapter appears in the test, unchanged, and no new one. Butler
   quotations: the same five. No new fact, scene, quotation or memory. `check-corpus-invariants.sh` HIGH = 0.
6. **Give the author what he needs to compare,** and keep it short for a one-to-two-hour week:
   - a PDF of the test chapter;
   - a PDF with three sections side by side, promoted on the left and test on the right: *The family*, the Libby
     paragraphs, and the Social Security passage;
   - five lines on what changed in kind (not a line-by-line list), and the word counts of both.
   Do not recommend one over the other unless he asks. He decides.

## Rules

- Length follows substance. No minimum and no maximum. Expect the test to be longer than the promoted chapter;
  say by how much.
- No invented facts, scenes, quotations or memories. Darity quoted only from published work.
- Do not edit the promoted chapter, the TA, the figure ledger, the gate files or STATE.md.
- If context runs short, finish the section you are in, say where you stopped, and write a handoff.
- End with the three lines.
