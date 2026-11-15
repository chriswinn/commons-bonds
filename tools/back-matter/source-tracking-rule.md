# Source tracking rule (author, 2026-11-15)

**Status:** internal; standing rule for every session that drafts, checks or researches. It applies to
chapters, the Technical Appendix, essays, op-eds and the proposal.

**The three lists.**
- **Tentative list:** `sources/bibliography.md` §19, "Supporting sources not yet integrated."
- **Working bibliography:** the numbered sections of `sources/bibliography.md`. The reader-facing
  bibliography is generated from these (`build.py`).
- **Decisions log:** `citation-decisions-log.md`.

## The rule

1. **Every potential source goes on the tentative list the day it is found.** That includes a source found
   on the web during a claims check, one named in a draft with no entry, and one a critic read says is
   missing. Write one entry: full citation as far as it is known; **Why here** (the claim or passage it would
   support, with chapter and line); **Standing** (read in full, read in part, or not read; where the
   description comes from). Never fill a field from memory; mark what is unknown.
2. **A source moves into the working bibliography only when a document cites it and the passage has been
   read.** The session that moves it writes the entry in its section with the reason it is included, and
   adds one dated line to §19's changes log: what moved, where to, and why. The reason stays on record in
   §19 after the entry has left it.
3. **A source that is ruled out stays out with its reason written down.** Add a dated line to §19's changes
   log and an entry in the decisions log (question, facts, reasoning, the author's ruling in his words where
   he gave them). The same goes for a source removed from the bibliography.
4. **Sessions recommend; the author rules.** Whether a work belongs in the bibliography or the appendix is
   his decision. Open questions go in the decisions log as OPEN with a recommendation.
5. **A named work with no entry is a finding.** If a draft names an author or title that is in neither list,
   add it to the tentative list and say so in the session's report.

## For drafting sessions

- Add entries to §19 under a dated heading of your own (for example "Candidates added 2026-11-16, Chapter 4
  drafting") so that sessions working in the same days do not edit the same lines. Fetch and rebase before
  pushing.
- The claims check (`tools/workstream-handoffs/claims-check-kickoff_2026-11-15.md`) is where most new
  sources turn up. Its "NO SOURCE IN THE PROJECT" rows that name a source found on the web each become a
  tentative entry. The check itself adds nothing to the working bibliography.
- A case-study file in `research/case-studies/` that copies an early draft is not a source.
