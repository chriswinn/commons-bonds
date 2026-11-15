# Book proposal refresh (kickoff, 2026-11-15)

**Status:** PROPOSED (internal scaffolding). One session at a time. Confirm the session is on Fable; if not,
say so first. The proposal is publisher-facing prose: nothing in it is ratified until the author says so, and
nothing merges to main as ratified before then.

## Paste line

```
Read CLAUDE.md, STATE.md, the newest house style sheet in tools/drafting-templates/ and tools/workstream-handoffs/proposal-refresh-kickoff_2026-11-15.md. Run Part 1 and stop.
```

## Why now

The author sent Chapters 1 and 5 and the Technical Appendix to William Darity on 2026-11-15 and is using the
wait to redraft chapters and refresh the proposal (his decision, 2026-11-15). A press needs the proposal whether
the book goes through Darity's introduction, a university press directly, or an agent. Agent queries and press
submissions stay **held** until Darity answers or mid-February, per the work plan.

## Part 1. Readiness report (do this first, change nothing, then stop)

Read every file in `publishing/book-proposal/` and report to the author, in one short message, **what has to
happen before the proposal can be refreshed.** Sort it into three lists:

**A. Only the author can decide or supply.** Check each of these and say where it stands today:
1. The four open decisions recorded in STATE.md: where the AI disclosure goes; the comp-titles refresh (§02);
   the no-overclaim wording for Chapters 7 and 9; airlock first or coal first.
2. His bio and platform (§03): the facts for the nursing program and anything else that has changed. Never
   draft these from inference.
3. Which form to build: a university-press proposal, a trade proposal for agents, or one master with both
   variants. Recommend one, with the reason.
4. How the proposal describes Chapters 6 to 9, which are not yet rebuilt: from the chapter maps and v4 briefs as
   planned content, or held until each chapter is redlined.
5. His ruling on the BP–Mexico sentence (Chapter 5 and TA §11.2), if still open.

**B. Should be finished first by another session.** Say for each whether it is done:
1. The claims check on Chapter 5, the Technical Appendix and Chapter 1
   (`tools/workstream-handoffs/claims-check-kickoff_2026-11-15.md`). The proposal quotes all three, so any
   wording they retire must not be copied into it.
2. The author's final straight read of Chapter 1 and Chapter 5.
3. The as-sent Darity email archived in `research/outreach/subjects/darity/`.

**C. This session can do without him.** List what Part 2 would change, file by file, with the size of each job:
stale figures, the Chapter 1 sample (still the June version), the Chapter 5 summary (still the old chapter,
including the retired $108 trillion passage), superseded candidate files, and anything the gate flags.

End Part 1 with a recommendation: start Part 2 now on list C, or wait for specific items on A and B. Then stop
and wait for his answer.

## Part 2. Refresh (only on the author's go-ahead, and only what he has cleared)

1. **Figures.** Check every number and factual statement in the proposal against
   `manuscript/ledgers/_CANONICAL_FIGURE_LEDGER.md` as amended for TA v2.0.1, and run Steps 1 to 4 of the claims
   check on the proposal itself. The overview was ratified in June, before the appendix corrections; expect
   retired figures. List every change with old and new values. Do not load the Technical Appendix.
2. **Samples.** Replace the Chapter 1 sample with the ratified November chapter, copied exactly, and add
   Chapter 5 the same way. No edits to either.
3. **Chapter summaries (§05).** Rewrite the Chapter 1 and Chapter 5 summaries from the ratified chapters.
   Summaries for 2, 3, 4 and 10 from the promoted chapters. Summaries for 6 to 9 as the author ruled in A4.
   Claim nothing a chapter does not yet do.
4. **Overview (§00).** Do not redraft it. Fix figures and retired frames only, list each change, and build a
   print copy with paragraph numbers and a margin for his hand redline (`tools/scripts/build-chapter-print-copies.py`).
   His redline of the overview is the voice pass.
5. **Darity.** Quote and cite only his published work. Nothing from the May 2026 call. Leave any endorsement or
   attribution line as a marked placeholder until he answers.
6. **Dinner-table voice** for anything newly written: explain, one step per sentence; everyday nouns; no "tries
   to"; no verdict closers. Never invent facts, scenes, quotations or the author's memories.
7. **Housekeeping.** Mark superseded candidate files as superseded; update `proposal-master.md`; note the
   NOK-to-USD re-stamp date; render the proposal PDF.

## What Part 2 hands back

- A change list, file by file, with every figure change shown old to new.
- The rows of the claims check that are not SUPPORTED, for his ruling.
- The overview print copy for his redline, and the questions only he can answer, in one batch.
- Gate: `bash tools/scripts/check-corpus-invariants.sh` HIGH = 0. Every retired figure gets a gate pattern in the
  same commit.
- Commit on the feature branch with `MERGE-HOLD` until he ratifies. Update the proposal line in STATE.md.
- Three closing lines: what got done, what is waiting on him, the exact next paste line.
