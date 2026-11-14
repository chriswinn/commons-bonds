# Chapters 2–4 and 6–10: pace draft, dinner-table draft, compare, hand redline (kickoff, 2026-11-14)

**Status:** PROPOSED (internal scaffolding). Supersedes `chapter-redrafts-kickoff_2026-11-12.md`, whose method
line was never set. **Method, set by the author 2026-11-14: both.** Each chapter gets a pace draft and a
dinner-table draft, the author marks printed copies by hand, and a session assembles exactly what he marked.
This is the process that finished Chapters 1 and 5.

One session at a time. One chapter at a time. Three short sessions per chapter. Confirm the session is on Fable;
if not, say so first.

## Paste lines (put the chapter number in place of N)

**Session 1, write:**
```
Read CLAUDE.md, STATE.md, the newest house style sheet in tools/drafting-templates/ and tools/workstream-handoffs/chapter-two-drafts-kickoff_2026-11-14.md. Run Session 1 for Chapter N.
```
**Session 2, compare and print:**
```
Read CLAUDE.md, STATE.md, the newest house style sheet in tools/drafting-templates/ and tools/workstream-handoffs/chapter-two-drafts-kickoff_2026-11-14.md. Run Session 2 for Chapter N.
```
**Session 3, redline (attach photos of every marked page):**
```
Read CLAUDE.md, STATE.md, the newest house style sheet in tools/drafting-templates/ and tools/workstream-handoffs/chapter-two-drafts-kickoff_2026-11-14.md. Run Session 3 for Chapter N. My assembly copy is the [pace / dinner-table / current] draft. Photos attached.
```

## Order

Chapters that wait on nothing first: **2, 10, 4, 3.** Then **7, 9, 6, 8.** The author may change the order.

## The two kinds of chapter

- **Chapters 2, 3, 4, 10** are promoted drafts the author has not redlined. He compares **three versions**: A =
  the current chapter in `manuscript/chapters/`, B = pace draft, C = dinner-table draft (as with Chapter 1).
- **Chapters 6, 7, 8, 9** are old versions that fail their gate and need a rebuild. He compares **two versions**:
  B = pace draft built from the rebuild brief, C = dinner-table draft of B (as with Chapter 5). The old chapter is
  a source of content only and is not printed.

## Session 1: write both drafts

### Before drafting

1. Read the chapter's map, `tools/workstream-handoffs/chapter-maps_2026-11/chNN-map.md`, and the README beside
   it for calls that must be answered the same way in two chapters.
2. **Check the map's calls.** Where the author has answered, his answers govern. Where he has not, ask him once,
   in one short message, with the map's recommendation beside each call. "Yes to all" is a complete answer. Do
   not draft on unanswered structure calls unless he says to use the recommendations.
3. **Chapters 6–9:** read `research/story-drafts/chN-blind-brief-v4_2026-11.md`. Check its "Blocked on Session
   A" list against `origin/main`. If an item is still missing, stop and tell the author.
4. Every figure comes from `manuscript/ledgers/_CANONICAL_FIGURE_LEDGER.md` as it stands today. Do not load the
   Technical Appendix.
5. Read only this chapter, and only the short passages of other chapters the map or brief names. Chapters 1 and
   5 on main are the models for voice: read "The family" through Libby in Chapter 5 and the first two sections of
   Chapter 1, and the two redline records (`research/story-drafts/ch1-author-redline_2026-11.md`,
   `ch5-author-redline_2026-11.md`) to see what he kept, swapped and cut.

### Draft B, pace and pull (write this first)

- Chapters 2, 3, 4, 10: same content, facts and figures as the current chapter, with the map's answered calls
  applied. Chapters 6–9: built fresh from the brief and the map.
- Order for pull: a person or a place first, the pattern named after the reader has seen it, the reasoning in
  the joints, the strongest thing last (`tools/memory/feedback_engagement_lenses.md`). No length target.

### Draft C, dinner-table (write this second, from B as the content source)

- Same sections, order, facts and figures as B. A change of voice, not of structure.
- **Do not rewrite. Explain.** For each paragraph, answer "what is this saying?" as if the author had asked
  across a dinner table, one step per sentence, and use that answer as the text.
- **What his Chapter 5 marks showed about this draft** (style sheet rules 26–29 and pending row P4): he used it
  as his base and went back to the pace version for 22 of 123 paragraphs, mostly where the dinner-table draft
  had broken a thought into a run of short same-shaped sentences ("One is… One is… One is…") or set a definition
  inside a sentence that didn't need one. So: vary sentence shapes, don't split a sentence that already reads in
  one pass, and define a term inside a sentence only where a reader would be lost without it.

### Rules for both drafts

- **Protected, word for word:** quotations; the sayings of the author's family; facts and figures; any passage
  the author has named as his own or written by hand. List the protected passages in the change notes.
- **Nothing invented:** no fact, scene, quotation, feeling or memory. Where the map says only the author can
  supply something (Ch 3's three passages, Ch 10's hospital sentence and his standing toward the Black Hills),
  leave a hidden comment and write nothing.
- One vantage, the author's. "You" only for what any reader anywhere has; "we" only author plus reader or a
  group he names; countries named. Everyday nouns ("company," "family"). State what the book does; no "tries to."
- Where the record shows a party seeking rent and shifting a cost, say so plainly from the record; allege no
  intent the record does not show.
- Credit a source in the sentence where its idea is used. Do not cut objections, lineage or a section on your
  own judgment: raise it as a QUESTION for him (he kept all six objections and the lineage in Chapter 5).
- No verdict closers, no announcing what the next paragraph will do, no process notes in the prose.
- Living people named from on-record statements get a note for the consent tracker; living private people stay
  unnamed.

### What Session 1 hands back

1. `tools/workstream-handoffs/chapter-redrafts_2026-11/chNN-pace_<date>.md` and `chNN-dinner-table_<date>.md`.
   **Do not touch the chapter in `manuscript/chapters/`.**
2. A fact table: every number, date, name and quotation in the drafts against its ledger row or source, and a
   script comparison showing B and C carry the same figures and quotations (and the same as A for 2, 3, 4, 10).
3. Short change notes: map calls applied; what was protected; marked gaps; word counts of each version.
4. One strongest-critic read of draft B, run once: where a hostile but fair reader would stop, as questions for
   the author, seven at most.
5. `bash tools/scripts/check-corpus-invariants.sh` HIGH = 0.
6. Commit and merge to main (scaffolding). **This session does not judge the drafts.**

## Session 2: compare and print (a fresh session that did not write the drafts)

1. Read every version straight through once, as a reader. Mark each place you had to reread.
2. Write `chNN-comparison_<date>.md` in the same folder: section by section, which version is clearest and which
   has the most pull, with real sentences quoted; what was added or changed against the author's own words; and
   the content questions (keep, cut, shrink or move) listed first, because he decides content before sentences.
   This is one reader's opinion. Do not pick a winner for him.
3. Build annotated print copies, one PDF per version, in the form he used for Chapters 1 and 5: the text exactly
   as the file has it, a small printed number beside every paragraph, page numbers, and a margin column with
   notes labeled **SECTION**, **BEST**, **ISSUE** and **QUESTION**. Use the pattern in
   `tools/workstream-handoffs/pull-pass_2026-11/annotated-versions_build_2026-11.py` (add the chapter's note
   lists) and print with the pre-installed Playwright Chromium in EB Garamond. Check that paragraph numbers line
   up across versions where the versions share a structure, and say so on the first page if they don't.
4. Send him the PDFs with a note of at most five lines: which copy to read first, about how many pages, and that
   he marks on paper.

## How the author marks (his convention; print it on page 1 of each copy)

- Pick one copy as the assembly copy. A paragraph with no mark stays.
- To take a paragraph from another version, cross the printed number and write the label: "#12 Pace," "#12
  Dinner," "#12 Current." "Except last sentence" and "swap 2 sentences" work the same way: circle what stays.
- Handwritten words go in at the arrow or caret. Printed words stay unless struck. A struck margin note means the
  note is rejected. "Cut" beside a crossed paragraph removes it.
- Photograph **every page of every copy he wrote on, in order**, and say in the message which pages are unmarked.

## Session 3: apply the hand redline

Follow section 2 of `tools/workstream-handoffs/commons-bonds-session-handoff-2026-11-14_v1.0.0.html` and the
two redline records as the model. In short:

1. Rebuild the printed paragraph numbers from the source files. If photos of some pages are missing, ask whether
   they are unmarked before treating them so.
2. Zoom into any mark you are unsure of. Save the transcription first, exactly as he wrote it, as
   `research/story-drafts/chN-author-redline_<date>.md`.
3. Ask once, in one batch, with the real sentences as the options: marks you cannot read; marks on a paragraph
   his labels replace; seams where two versions repeat or no longer connect. His questions written in the margin
   are questions to answer, not edits to make.
4. Apply exactly. Do not improve his wording. Decide nothing about content for him.
5. Check every number against the ledger and against the version already checked; run the gate.
6. Grammar-and-punctuation polish, mechanical only, every change listed for his veto. Rule 6a for commas.
   Contractions and deliberate fragments stay.
7. Commit on the feature branch with `MERGE-HOLD` until he ratifies. On his word: archive the old chapter,
   promote, update the chapter's STATE.md lines in the same commit, give any new or changed figure a ledger row
   and a gate pattern in that commit, and merge to main.
8. Update the house style sheet from his actual marks and bump its version. Build his final-read print copy with
   `tools/scripts/build-chapter-print-copies.py`.

## Rules for every session

- No delegated or parallel sessions. If context runs short, finish the section you are in, say where you
  stopped, and write a handoff.
- Never invent facts, scenes, quotations or the author's memories. Darity is quoted only from published work.
- Keep each ask to the author short. End with three lines: what got done, what is waiting on him, and the exact
  paste line for his next session.
