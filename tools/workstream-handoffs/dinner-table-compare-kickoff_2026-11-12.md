# Compare the versions of Ch 1 and Ch 5: the JUDGING session (kickoff, 2026-11-12)

**Status:** PROPOSED (internal scaffolding). One fresh session, started **after** the writing session has merged
its two drafts. It must be a different session from the one that wrote them. Confirm the session is on Fable.

## Paste line

```
Read CLAUDE.md, STATE.md, tools/drafting-templates/commons_bonds_house-style-sheet_v1.0.1.md and tools/workstream-handoffs/dinner-table-compare-kickoff_2026-11-12.md. Run it.
```

## What the author asked for

"Compare them with the pace and current versions and tell me which wins in your opinion and why." He decides.
Your job is an honest opinion with reasons, short enough to read in one sitting. The chapters go to William
Darity with the Technical Appendix, and he is reading partly to see whether the author can write.

## The versions

| | Chapter 1 | Chapter 5 |
|---|---|---|
| **A. Current** | `manuscript/chapters/Chapter__1_TheQuietMath.md` (the author's own hand redline, June 2026) | `manuscript/chapters/archive/Chapter__5_TheAccountabilityGap_SUPERSEDED_2026-11-12.md` (the old chapter; already replaced) |
| **B. Pace** | `tools/workstream-handoffs/pull-pass_2026-11/ch1-pace-redraft_2026-11-10.md` | `manuscript/chapters/Chapter__5_TheAccountabilityGap.md` (the rings redraft with the author's twelve decisions; promoted 2026-11-12) |
| **C. Dinner table** | `tools/workstream-handoffs/pull-pass_2026-11/ch1-dinner-table_2026-11.md` | `tools/workstream-handoffs/pull-pass_2026-11/ch5-dinner-table_2026-11.md` |

For Ch 5 the real contest is B against C. Read A's opening, its Libby section and its Social Security section
only, enough to say in a sentence whether anything in it was lost that should come back.

If either C file is missing, stop and tell the author; do not write it yourself.

## How to read

- Read each version straight through, as a reader would, **before** you read any change notes, the decision
  answers or the chapter maps. One chapter at a time.
- **Score the whole read, not the best lines.** This is a lesson the project has already paid for: on 2026-11-09
  Claude ranked three Ch 5 drafts by their best sentences and structural turns, and the author, reading for
  whether the pages kept turning, picked the one Claude had ranked last.
- You are not neutral about prose that sounds like you. Compressed, shapely sentences and short verdict closers
  are your habit, and the author has said he does not talk like that. Do not reward them.

## What to judge, in the author's terms

1. **Can it be followed in one pass?** Mark every place where you had to reread.
2. **Does it pull?** At the end of each paragraph, do you want the next one?
3. **Does it sound like him?** Plain, no jargon, no idiom tied to one country, one step at a time, like a person
   explaining across a dinner table. For Ch 1, his June redline (commit `0fca4465`) is the evidence of his voice.
4. **Did anything get lost or added?** Check mechanically that every figure and every quotation is identical
   across versions, and that C contains no fact, scene, feeling or memory that is not in its source. Anything
   added to the author's memories in Ch 1 is disqualifying for that passage; say exactly where.
5. **What does each version cost him?** Estimate how much hand redlining each would still need.

## What to give the author (keep it to about two pages, plus the PDFs)

1. **For each chapter, one line first:** which version you would send to Darity, or which you would redline from.
2. **Why,** in a short paragraph, in plain words.
3. **Where each version is strongest,** section by section, in a small table. Say so if the best text is a mix:
   for example C for the argument sections and B or A for the scenes.
4. **Say plainly if his own redlined Ch 1 (A) is still the best Ch 1.** That is a likely and acceptable result.
5. **The three weakest passages in the version you prefer,** quoted, so he knows what he would still have to fix.
6. **Two PDFs,** one per chapter, with three passages side by side across the versions. For Ch 5: *The family*,
   the Libby paragraphs, the Social Security passage. For Ch 1: the lease, the air-compressor story, the plane
   and the hospital mornings. PDFs are not committed (the repo ignores them); send them to him.
7. Word counts of every version.

## Rules

- Change no chapter and no draft. Do not write a fourth version or "fix" the one you prefer.
- No invented facts. Darity is quoted only from published work.
- Do not edit the TA, the figure ledger, the gate files or STATE.md.
- Write your opinion to `tools/workstream-handoffs/pull-pass_2026-11/dinner-table-comparison_2026-11.md`, commit,
  merge to main, and end with the three lines.
