# Parallel window, Session A: TA Phase 2 (kickoff, 2026-11-11)

**Status:** PROPOSED (internal scaffolding). Runs in parallel with Session B under the dated exception in
CLAUDE.md (expires 2026-11-17 02:30 local). **Model:** confirm the session is on Fable before starting;
if it is not, tell the author in your first reply.

## Paste line

```
Read CLAUDE.md (CURRENT OPERATING MODE banner and the DATED EXCEPTION), STATE.md, and tools/workstream-handoffs/parallel-window_2026-11-11_session-A_ta-phase2.md. Run it. You are Session A; Session B is running in parallel and owns none of your files.
```

## You own (only you edit these)

`manuscript/technical-appendix/` (TA, calc engines, symbol registry), `manuscript/ledgers/_CANONICAL_FIGURE_LEDGER.md`,
`tools/quality-gates/`, `tools/back-matter/` generated notation output, `STATE.md`. Do not edit chapters, essays,
the proposal, or anything under `tools/drafting-templates/` or `tools/workstream-handoffs/chapter-maps_2026-11/`.

## Read first

1. `tools/rigor-passes/commons_bonds_rigor_pass_2026-11-10_technical_appendix_decisions-log.md` — the author's
   answers. **Governs.**
2. `tools/rigor-passes/commons_bonds_rigor_pass_2026-11-10_technical_appendix_review-packet_v1.0.2.md` (Part 1
   and the appendix table).
3. `tools/rigor-passes/commons_bonds_rigor_pass_2026-11-10_technical_appendix_independent_review_v1.0.0.md` —
   verbatim quotes and draft text per finding. Use it as a working reference; do not reload the whole TA twice.
4. `research/citations/long-absence-high-risk-work_literature_2026-11-10.md` (for the decision-7 passage).

## Steps, in order

1. **Hotelling-rent test** across every worked case (Norway, McDowell, Deepwater, Libby, Baotou, reef). For each:
   can rent per unit be measured from a sourced figure? Report a table. Then write §4 as the split of the forward
   term, RCV − B₂ = (RCV − H) + (H − B₂), with only the cases that compute as worked examples. No invented rents.
2. **Decision-2 wording test.** Apply "priced with the cost in view" to every §11 case and to §12 Scenarios 1 and
   5 and Walkthrough 2 (the commute). Report any case where it gives a wrong answer before writing Definition 1.7.
3. **Archive v2.0.0; write v2.0.1** (stays `.html`). Apply the ratified decisions and the no-decision batch
   (F2, F3, F6, F16, N4–N8, N10, N11, C3, C5). Name stays "Three Ways of Counting" with the one-line gloss;
   remove all triangulation and convergence language (decision 1).
4. **Decision 6 (revised):** rewrite the Definition 1.10 Ostrom paragraph on Ostrom's own published principles
   (those who bear the costs share the resource's fate and help make its rules; design principle 3, *Governing
   the Commons*, 1990). **No divided-community claim. No Darity attribution. Nothing from the May 2026 call.**
   Darity is quoted only from published work. Then confirm the TA contains zero call-derived material.
5. **Decision 7:** closest-prior-art subsection, borrowed/added table before §1, the two-party asteroid-colony
   reserve illustration (explicit thought-experiment register), the three-kinds-of-not-knowing passage. Write
   each prior-art entry from the source; Broome 2012 and Broome 1994 are unverified — verify or leave out.
6. **Fact items carried from Ch 5:** §11.3 relabel the $250M as Grace's 2008 reimbursement of federal cleanup
   (DOJ), not wrongful-death settlements; source or label the $50M/yr monitoring; adopt the chapter's sourced
   crowdfunding figures (Kenworthy & Igra 2022); frame Deepwater as the realized industry-paid bond case.
7. **Engines:** replace typed-in constants (McDowell bond, Norway bond, the $8.66 basis) with derivations; re-run
   both; 0 mismatches.
8. **Ledger + gates in the same commit:** amend the McDowell headline (integral $525–540; CS about $440–490),
   the consistent-basis multiples, Norway's bond label, the stale $580–620 / 67–134× rows; add a gate pattern
   for every retired figure or term.
9. **Notation:** sync `symbol-registry_2026-06-07.md` Part 7 and regenerate the TA notation section
   (`tools/back-matter/build.py gen-ta-notation`). The author reports it had drifted; check every symbol used.
10. Invariants HIGH = 0; render the TA PDF; one-page changelog against Darity's 05-15 copy
    (`tools/audits/ta-darity-version-diff_2026-06-07.md`).

## Close

Push to your branch with pre-push reconciliation (`git fetch origin main && git rebase origin/main`). If a rebase
touches a file you do not own, stop and tell the author. Give the author the TA PDF and changelog; **merge v2.0.1
to main on the author's OK** (publisher-facing). Update the STATE.md TA line. If context runs short before step
10, write a handoff (`commons-bonds-session-handoff-YYYY-MM-DD_v1.0.N.html`) and stop cleanly. End with the
three lines.
