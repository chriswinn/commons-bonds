# Ch 5 dinner-table draft: checks and change notes (2026-11-12)

**Status:** PROPOSED (internal). Draft: `ch5-dinner-table_2026-11.md`. Content source:
`manuscript/chapters/Chapter__5_TheAccountabilityGap.md` (unchanged). This file reports what was done. It does
not say which version is better; that is the comparison session's job and the author's decision.

## What changed in kind

Every paragraph outside the protected passages was written again as a plain answer to "what is this saying?",
one step per sentence, with the steps the source skipped put back in (for example how a tenth of a fall in price
removes a whole down payment, or why a sound defense of Treasury bonds does not answer a criticism about how
promises were timed). Short verdict lines and figures of speech were replaced by the plain statement they stood
for ("A door pushed partway open…", "The two pass each other.", "call the roll", "built the chute", "in any
political weather"), and terms of art got a short clause saying what they mean. Sections, order, cases, facts,
figures, quotations and the author's own passages are the same as the source.

## Word counts (hidden comments excluded)

| | Words |
|---|---|
| Source | 11,222 |
| Draft | 13,238 |
| Change | +2,016 (+18.0%) |

## Check 2: protected passages and quotations, string for string

All present and identical to the source (checked by script):

- *The family*: "Their own doctor still opposed the device." to the end of that paragraph, and the whole of
  "This was not one family's bad luck…".
- The 2008 account, "I was doing well at the time." through "…who stood on the far side of the transfer."
- "The United States holds one more compact… would not mean being left with nothing."
- "I should say plainly why. I am not a descendant… given their working lives to it."
- "Applied to that debt, the Restitution Bond is a reparations bond… until it is paid."
- "One question this book does not presume to close."
- "An honest ledger can name a line… not this book's to enter."
- "did not produce" · "cashed out" · "left standing where it landed" · "the bill comes due"
- All 18 quoted strings in the source (Butler's five, Darity's two, the titles and the quoted terms). One quoted
  term, "conservation", sits in a reordered sentence so that it keeps its lower-case form.
- Both hidden page-number comments, in place after the two Darity quotations.

## Check 3: corpus invariants

`bash tools/scripts/check-corpus-invariants.sh`: **HIGH = 0** (exit 0).
`check-prose-clarity.py` on the draft, for information only: HIGH 0, MEDIUM 2, LOW 7 (source: HIGH 0, MEDIUM 3,
LOW 8).

## For the comparison session and the author

**Explanatory steps added.** Each restates something the source says or plainly implies; none is a new fact.
Listed so they can be checked:
- "Jeff was Butler's father." (the source gives the name only inside the quotation)
- "The cases so far have moved outward in rings, from one family to whole communities." (the source uses "ring"
  here without having said what the rings are)
- The leverage paragraph spells out why the whole fall comes out of the down payment, and adds "When that many
  families cut their spending that sharply, businesses everywhere lose customers."
- The pocket section says what the opening question was before answering it, and adds "The people who gain are
  kept apart from the people who pay, and the cost goes to whoever cannot refuse it."
- "The black-lung program is paid for by an excise tax on coal." (the source says only "When the coal excise tax
  falls short")
- "the border between the United States and Mexico"; "in the Inner Mongolia region of China".
- The Sweden paragraph ends "It chose that path, and Sweden shows that another one was open."

**Terms given a short meaning in passing:** palliative care, joists, modules, tort law, securities, leverage,
equity, median wage, TARP, liquidity (said as "a form they could turn into cash quickly"), rents, remediation,
tailings ponds, third parties, bond, captured regulator, sinks, discharges. Left without a gloss because a gloss
would add content the source does not have: "non-domination" and "the non-identity problem".

**The United States is named** in the Grace prosecution ("the largest environmental criminal prosecution the
United States had attempted"), near the top of the 2008 section, and in the leverage paragraph.

**The 2008 objections** open as "One objection… Another objection… Another objection… The last objection…". The
word "four" appears only in the approved sentence that turns to Sweden.

**Carried over from the source unchanged, and worth a look at the redline:**
- The Pistor test names four attributes (priority, durability, universality, convertibility) and then says the
  bond lacks two of them, "convertible" and "transferable". Transferable is not one of the four named.
- "The complexity was no accident." is still a claim about intent that has not been checked against the
  Financial Crisis Inquiry Commission report (decision 7).
- Libby: the draft says the documents "show that the contamination was identified early, and that the exposure of
  the workers was measured for as long as the mine ran", and in the roster "show lobbying, and an effort to delay
  the regulation of asbestos". That is what the source says and no more.
- The open calls from the decision record are untouched: the section opener "In 2008 the distance closed." is in;
  the announcing line in *Restitution and foreclosure* is reduced to the two chapter pointers.

## Check 1: figures

Every figure in the source is in the draft, in the same written form, and the draft has no figure the source
lacks. Counts are occurrences. Where the draft count is higher, the same figure is repeated in an explanation.

| Figure (as written) | In source | In draft | Same? |
|---|---|---|---|
| $10 billion to $12 billion | 1 | 1 | yes |
| $10.2 million | 1 | 1 | yes |
| $100 billion | 1 | 1 | yes |
| $100 million | 2 | 2 | yes |
| $11 trillion | 1 | 1 | yes |
| $12,000 | 1 | 1 | yes |
| $15.3 million | 1 | 1 | yes |
| $16 trillion | 1 | 1 | yes |
| $173,000 | 1 | 1 | yes |
| $2 billion | 1 | 1 | yes |
| $22.6 trillion | 1 | 1 | yes |
| $25.5 million | 1 | 1 | yes |
| $250 million | 1 | 1 | yes |
| $4 billion | 1 | 1 | yes |
| $419,000 | 1 | 1 | yes |
| $44 billion | 1 | 1 | yes |
| $461 | 1 | 1 | yes |
| $5.1 billion | 1 | 1 | yes |
| $54 | 1 | 1 | yes |
| $545 million | 1 | 1 | yes |
| $600 million | 1 | 1 | yes |
| $61.6 billion | 1 | 1 | yes |
| $65 billion | 1 | 1 | yes |
| $7,500 | 1 | 1 | yes |
| $700 billion | 1 | 1 | yes |
| $8 billion to $12 billion | 1 | 1 | yes |
| 12 percent | 1 | 1 | yes |
| 16 percent | 1 | 1 | yes |
| 1929 to 1933 | 1 | 1 | yes |
| 1930 | 1 | 1 | yes |
| 1931 | 1 | 1 | yes |
| 1935 | 2 | 2 | yes |
| 1938 | 1 | 1 | yes |
| 1944 | 1 | 1 | yes |
| 1950 | 1 | 1 | yes |
| 1963 to 1990 | 1 | 1 | yes |
| 1965 | 1 | 1 | yes |
| 1970 | 1 | 1 | yes |
| 1972 | 5 | 5 | yes |
| 1977 | 4 | 4 | yes |
| 1978 | 1 | 1 | yes |
| 1980 | 1 | 1 | yes |
| 1983 | 1 | 1 | yes |
| 1984 | 1 | 1 | yes |
| 1989 | 1 | 1 | yes |
| 1990 | 2 | 2 | yes |
| 1997 | 1 | 1 | yes |
| 1998 | 1 | 1 | yes |
| 1999 | 2 | 2 | yes |
| 2 | 1 | 1 | yes |
| 20 | 1 | 1 | yes |
| 20 percent | 1 | 1 | yes |
| 2000 | 1 | 1 | yes |
| 2001 | 2 | 2 | yes |
| 2001 to 2008 | 1 | 1 | yes |
| 2005 | 1 | 1 | yes |
| 2006 | 1 | 1 | yes |
| 2007 | 1 | 1 | yes |
| 2008 | 16 | 16 | yes |
| 2009 | 4 | 4 | yes |
| 2010 | 4 | 4 | yes |
| 2011 | 2 | 2 | yes |
| 2012 | 2 | 2 | yes |
| 2014 | 1 | 1 | yes |
| 2015 | 3 | 3 | yes |
| 2016 | 2 | 2 | yes |
| 2018 | 2 | 2 | yes |
| 2020 | 6 | 6 | yes |
| 2021 | 1 | 1 | yes |
| 2022 | 3 | 3 | yes |
| 2024 | 2 | 2 | yes |
| 2030 | 2 | 2 | yes |
| 2033 | 1 | 1 | yes |
| 21 million | 1 | 1 | yes |
| 25,000 | 1 | 1 | yes |
| 4 | 1 | 1 | yes |
| 4.1 million | 1 | 1 | yes |
| 4.9 million | 1 | 1 | yes |
| 401(k) | 5 | 5 | yes |
| 438,000 | 1 | 1 | yes |
| 5 | 1 | 1 | yes |
| 6 | 3 | 3 | yes |
| 60 percent | 1 | 1 | yes |
| 7 | 1 | 1 | yes |
| 77 percent | 1 | 1 | yes |
| 8 | 2 | 2 | yes |
| 9 | 6 | 6 | yes |
| billion | 1 | 1 | yes |
| eighteen | 1 | 1 | yes |
| eighty | 3 | 3 | yes |
| eighty-five | 1 | 1 | yes |
| eighty-nine | 1 | 1 | yes |
| eighty-seven | 1 | 1 | yes |
| eleven | 1 | 1 | yes |
| fifteen | 1 | 1 | yes |
| five | 4 | 4 | yes |
| nine | 1 | 1 | yes |
| seventy-five | 1 | 1 | yes |
| seventy-seven | 2 | 2 | yes |
| six | 1 | 1 | yes |
| ten | 3 | 3 | yes |
| thirty | 2 | 2 | yes |
| thousand | 1 | 1 | yes |
| twenty | 2 | 2 | yes |
| twenty-seven | 2 | 2 | yes |
| twenty-two | 1 | 1 | yes |
| more than a third | 1 | 1 | yes |
| nearly nine in ten | 1 | 1 | yes |
| about six times | 1 | 1 | yes |
| a tenth of the price | 1 | 2 | yes |
| about three times as much | 1 | 1 | yes |
| three-quarters | 1 | 1 | yes |
| roughly half of China | 1 | 1 | yes |
| three ways at once | 1 | 1 | yes |
| three serious risks | 1 | 1 | yes |
| three main pieces | 1 | 1 | yes |
| four legal attributes | 1 | 1 | yes |
| All four objections | 1 | 1 | yes |
| Two objections | 1 | 1 | yes |
| two instruments | 2 | 1 | yes |
| a few thousand people | 1 | 1 | yes |
| Hundreds of | 1 | 1 | yes |
| Thousands more | 1 | 1 | yes |
| Millions of attics | 1 | 1 | yes |
| millions of gallons | 1 | 1 | yes |
| millions of foreclosure filings | 1 | 1 | yes |
| several billion dollars | 1 | 1 | yes |
| in the billions | 1 | 1 | yes |
| trillions of dollars | 1 | 1 | yes |
| two decades | 1 | 1 | yes |
| Twenty years earlier | 1 | 1 | yes |
| fifteen years after | 1 | 1 | yes |
| thirty-year | 1 | 1 | yes |
| eighteen months | 1 | 1 | yes |
| ten years | 1 | 1 | yes |
| five more | 1 | 1 | yes |
| five years | 3 | 4 | yes |

Distinct figures: 137 in source, 137 in draft; missing or new: 0.
