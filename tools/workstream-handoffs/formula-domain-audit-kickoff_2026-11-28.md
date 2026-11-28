# Kickoff: formula domain audit of the Technical Appendix

**Status:** internal; PROPOSED 2026-11-28, at the author's request in the decisions walk-through. Not started.
One session at a time: run it only when no other session is open.

## Why

In the walk-through the author was shown that one sentence places McDowell County at "A < τ" under Theorem
10.3, where the theorem's cost function is not defined. His question: are there other places where the
framework can be handed inputs that produce nonsense, which an economist could use to discredit the whole? The
claims check tested sentences against sources and the engines test the arithmetic (67/67, 28/28). **Nobody has
yet checked each formula's domain and its behaviour at the edges.** That is this audit.

## What to do

For every definition, formula, theorem and worked case in `manuscript/technical-appendix/TechnicalAppendix_v2.0.1.html`
(and the calc engines that implement them):

1. **Domain.** For which values of each input is the formula defined? Write it down in plain words.
2. **Edges.** What does it return at zero, at the threshold, at one, at infinity, and for a negative input?
   Division by zero, an infinite result, a negative price, a result that changes sign.
3. **Units.** Do both sides carry the same units?
4. **Cases against domains.** Is any case in §11 to §13 placed outside the domain of a formula it is said to
   illustrate, or given an input the formula cannot take?
5. **Meaning at the edge.** Where the formula does blow up or go negative, is that intended and said (as the
   appendix already says for a realized bond above RCV), or silent?

Report only. For each finding: the formula in plain words, the input that breaks it, what an economist would
say, and two or three ways to handle it (bound the domain and say so; define the edge; change the form). **No
change to the appendix, the engines or the ledger.** The author wants each finding taught to him step by step
before he rules; write for that.

## Seeds found in passing on 2026-11-27/28 (not yet examined)

- **Theorem 10.3, the threshold τ.** The cost function is defined only for A above τ. What τ *is* for a real
  resource is not stated: physical exhaustion, the point where extraction costs more than the price, or the
  point where the commons stops doing its work. McDowell still holds about 1.7 billion recoverable tons, so it
  is not near physical exhaustion. The author's suggestion: τ may be an economic or functional threshold (a
  mine no longer worth working; a fish stock below what can renew itself). Pindyck (1978, p. 844, read) has
  cost rising as reserves deplete. Wanted: a standard source on economic versus physical exhaustion.
  Candidate remark, **for his two-path test, not ratified:** above the threshold the framework prices forward
  (foreclosure); once a commons is past it, the case is read backward (damage done), as the reef is in §11.12.
- **The irreversibility premium.** The band 6.67 to 20 follows from 1/(1 − α) at α = 0.85 and 0.95. At α = 1
  (a loss that is fully irreversible) the premium is infinite. Intended? Said?
- **§15.1.7** says atmospheric stability "cannot be re-engineered at any finite cost" while Method 1 prices
  that re-engineering per ton. Infinite in one place, finite in another.
- **Method 3** cannot return a value below the market price (the appendix says so); check every place its
  result is read as evidence.
- **The Hotelling split.** (H − B₂) is negative for Norway. What does a negative term mean, and is it said?
- **Scarcity multipliers** that do not follow from the figures on file (claims check §1b item 16); the six
  prose figures the engines do not reproduce (report Part 3).
- **"Cost severance scales with distance"** (§11.4, §15): the author recalls the intended meaning as "distance
  makes the extraction and the severed cost easier to hide," not a numerical scaling. Check the history of the
  phrase and whether any formula uses distance as a quantity.
- **A realized bond larger than RCV** (CS negative): handled in the text; confirm it is handled everywhere.

## Read first

CLAUDE.md, STATE.md, `tools/workstream-handoffs/commons-bonds-session-handoff-2026-11-27_v1.0.3.html`, the
appendix rulings file (`tools/audits/claims-check_technical-appendix_rulings_2026-11-27.md`), and the symbol
registry.

## Paste line

"Read CLAUDE.md, STATE.md and tools/workstream-handoffs/formula-domain-audit-kickoff_2026-11-28.md. Run the
formula domain audit of the Technical Appendix. Report only; teach me each finding step by step; change nothing."
