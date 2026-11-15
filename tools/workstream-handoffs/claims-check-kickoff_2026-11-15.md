# Claims check: every factual statement against what the project has already found (kickoff, 2026-11-15)

**Status:** PROPOSED (internal scaffolding). One document per session. Report only: this session changes no
chapter, appendix or ledger text. Confirm the session is on Fable; if not, say so first.

## Why this exists

The figure ledger checks **numbers**. Nothing has checked the **sentences around the numbers**, or the factual
statements that carry no number at all. On 2026-11-15 the BP–Mexico figures in Chapter 5 all matched their
source, and the sentence introducing them ("The oil did not stop at the border…") stated as fact something the
same source reports as contested. The ledger row even recorded the contrary evidence. No step compared the
prose with it.

## Paste line (name the document)

```
Read CLAUDE.md, STATE.md and tools/workstream-handoffs/claims-check-kickoff_2026-11-15.md. Run it for [Chapter 5 / the Technical Appendix / Chapter 1 / Chapter N draft at <path>].
```

Order for the documents already with Darity: **Chapter 5, then the Technical Appendix, then Chapter 1.**
The appendix may need two sessions (§1–§10, then §11–§18); say where you stopped.

## Step 1. List every claim

Go through the document sentence by sentence and write one row for every statement a reader could check:

- numbers, dates, names, titles, places;
- quotations and anything attributed to a person or a source ("Pistor argues…", "the chief executive has said…");
- events and what happened in them;
- superlatives and firsts ("the largest," "the first," "most of," "never");
- cause and effect ("because," "which is why," "led to");
- descriptions of a scene or a place that the author did not witness;
- statements about what the evidence shows or does not show.

Leave out the author's own life (first-person memory is his to supply), the book's own argument and definitions,
and openly marked thought experiments. When unsure whether something is a claim, list it.

## Step 2. Look for each claim in what the project already has

Search all of these, not only the cited ones:

- `manuscript/ledgers/_CANONICAL_FIGURE_LEDGER.md`
- `tools/back-matter/sources/bibliography.md` (the full list of sources found, cited or not) and
  `tools/back-matter/citation-crossref-index.md`
- `research/case-studies/`, `research/citations/`, `research/literature/`
- the consent tracker for any named living person

**The Technical Appendix and the chapters cannot support each other.** A claim in Chapter 5 is not sourced
because the appendix says the same thing.

## Step 3. Read the source, and compare the whole sentence

For each claim, read what the source note actually says. Where the repo holds only a citation and the claim
matters, read the source itself on the web. Then compare **the full sentence in the document** with the source,
not just the figure. Ask each time:

- Does the source state this as a **fact, an estimate, an allegation, or one party's position**? Does the prose
  keep that status?
- Does the prose **say more** than the source: a wider scope, a stronger verb, a cause the source does not give,
  "never" or "first" where the source is narrower?
- Is the claim attributed to the **right source**, and is the year right?
- Does anything else the project has found **contradict or qualify** it?

## Step 4. Give every claim one status

| Status | Meaning |
|---|---|
| **SUPPORTED** | The source says it. Quote the source's words beside the claim. |
| **SAYS MORE THAN THE SOURCE** | The source supports a weaker statement. Quote both, and say what the difference is. |
| **CONTESTED** | Sources the project holds disagree, or the source reports a dispute. Say who says what. |
| **SOURCE FOUND, NOT CITED** | Supported by something in the repo that the document does not credit. Name it. |
| **NO SOURCE IN THE PROJECT** | Nothing found. Say whether a quick web check finds one, and name it; do not add it. |
| **CONTRADICTED** | A source the project holds says otherwise. Quote it. |
| **NOT CHECKED** | Could not reach the source. Say why. Never mark a claim supported on memory or likelihood. |

## Step 5. What you hand back

1. `tools/audits/claims-check_<document>_<date>.md`: the full table (location, the claim in the document's words,
   status, the source's words, the source).
2. **At the top, a short list for the author: only the rows that are not SUPPORTED,** worst first. For each: the
   sentence as it stands; what the source supports; and one or two plainer sentences the source would support,
   offered as options. He rules on each: revise, find a source, or cut.
3. A second short list: **sources the project has found that bear on this document and are not used**, where one
   would strengthen a claim or should qualify it.
4. Counts: claims listed, and how many in each status.
5. Every source found on the web that the project does not hold goes on the tentative list, with the claim it
   would support, per `tools/back-matter/source-tracking-rule.md`. (The check still adds nothing to the working
   bibliography.)
6. Do not edit the document. After the author rules, a later session applies his rulings exactly, and every
   ruling that retires or changes a figure or a factual wording gets a ledger row and a gate pattern in the same
   commit.

## Rules

- Never invent a source, a quotation or a page number. An honest NOT CHECKED is a correct result.
- A keyword match in a source file is not support. Read the passage.
- Keep the report for the author short; the full table is the record.
- One session at a time. End with three lines: what got done, what is waiting on him, the next paste line.
