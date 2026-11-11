# Parallel window, Session B: style sheet, chapter maps, Ch 6–9 briefs (kickoff, 2026-11-11)

**Status:** PROPOSED (internal scaffolding). Runs in parallel with Session A under the dated exception in
CLAUDE.md (expires 2026-11-17 02:30 local). **Model:** confirm the session is on Fable before starting; if it is
not, tell the author in your first reply.

## Paste line

```
Read CLAUDE.md (CURRENT OPERATING MODE banner and the DATED EXCEPTION), STATE.md, and tools/workstream-handoffs/parallel-window_2026-11-11_session-B_style-maps-briefs.md. Run it. You are Session B; Session A is running TA Phase 2 in parallel and owns the TA, ledger, gates and STATE.md.
```

## You own (only new files)

- `tools/drafting-templates/commons_bonds_house-style-sheet_v1.0.0.md`
- `tools/workstream-handoffs/chapter-maps_2026-11/` (new directory: one map per chapter, plus PDFs)
- `research/story-drafts/ch6-blind-brief-v4_2026-11.md` … `ch9-blind-brief-v4_2026-11.md`

**Do not edit:** the TA, the figure ledger, gate files, STATE.md, any chapter, any essay, the proposal. Do not
load the TA. Load one chapter at a time.

## Why this session exists

The book's chapters have their content but lack pace and pull, and the prose is clunky. The Ch 5 rings redraft
(`tools/workstream-handoffs/pull-pass_2026-11/ch5-rings-redraft_2026-11-10.md`) is the model of pace the author
approved. From Nov 17 every chapter is redrafted one per session, from a map, this style sheet and the amended
ledger, so the author can redline them all over winter break (Dec 14 – Jan 10). Those redrafts may run on a
less capable model; this session's job is to make the judgment calls now so the redrafts mostly execute them.

## Steps, in order

1. **House style sheet** (one to two pages, rules with a before-and-after example each). Sources:
   - The author's Ch 1 hand redline (applied about 2026-06-11). The clone is shallow: run
     `git fetch --unshallow origin` (or `--deepen`), then find the redline commit with
     `git log --oneline -- manuscript/chapters/Chapter__1_TheQuietMath.md` and diff it.
   - `tools/workstream-handoffs/ch5-rebuild-2026-10/ch5-author-redline-notes_2026-11-09.md`.
   - `tools/workstream-handoffs/pull-pass_2026-11/critic-read.md` and the review packet v1.0.2 Part 4 (the
     closing-line habit: too many paragraphs ending on a short turn; announcing sentences; stacked objections).
   - The author's Ch 5 redline of the rings redraft, if they supply it during the session; otherwise mark the
     sheet v1.0.0 and note that it updates from that redline.
   Record only patterns the author actually made or approved. Never invent the author's preferences.
2. **Chapter maps, one page each,** for Ch 1, 2, 3, 4, 6, 7, 8, 9, 10 (Ch 5 has `question-map.md`; use it as the
   format model). Each map: the chapter's one question; sections in order, each with what it must hand to the
   next; the opening person or place; the facts it carries (by ledger row, not by number); what to cut or move;
   open structure calls for the author (no more than five, each with a recommendation).
   - **Ch 1 is open** (not closed): the map must place the author's travel story (25 years as an IT consultant
     for IBM and startups, heavy business travel, a marriage that ended). The author writes the scenes; the map
     only places them. Supporting research: `research/citations/long-absence-high-risk-work_literature_2026-11-10.md`
     §6–7. The former spouse is a living person: unnamed, the author's own experience only.
   - Do not write figures into maps; Session A is changing the McDowell headline and the multiples.
3. **Ch 6–9 rebuild briefs v4,** updating the v3 briefs in `research/story-drafts/` with: the TA decisions log
   (`tools/rigor-passes/commons_bonds_rigor_pass_2026-11-10_technical_appendix_decisions-log.md`), the verified
   positioning (`tools/workstream-handoffs/verified-positioning-findings_2026-06-24.md`), the matrix insertions
   assigned to each chapter, and the style sheet. Ch 6 keeps the title "Three Ways of Counting" with the gloss
   (two ways count what is owed, one counts what was paid); no triangulation language. Remove the Ch 6 L285
   divided-community Ostrom passage (it paraphrases Darity's unpublished call; decision 6).
4. **PDFs** of the style sheet and every map for the author to print. One combined PDF is fine.

## Rules

- No invented facts, quotes, scenes or memories. Darity is quoted only from published work.
- One chapter in context at a time; summarize to the map, then drop it.
- If context runs short, finish the current map, write a handoff, and stop cleanly.

## Close

Internal scaffolding: merge to main at close with pre-push reconciliation. If a rebase touches a file you do not
own, stop and tell the author. End with the three lines.
