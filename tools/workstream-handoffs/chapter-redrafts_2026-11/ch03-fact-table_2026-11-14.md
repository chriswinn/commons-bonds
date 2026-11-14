# Ch 3, The Waterman: fact table for the pace and dinner-table drafts (2026-11-14)

**Status:** PROPOSED (internal scaffolding). Session 1 of the two-drafts process.
**Versions:** A = `manuscript/chapters/Chapter__3_TheWaterman.md` (untouched); B = `ch03-pace_2026-11-14.md`; C = `ch03-dinner-table_2026-11-14.md`.

**How it was checked.** `python3 tools/workstream-handoffs/chapter-redrafts_2026-11/ch03-compare-figures-quotes.py` compares the three files: every italic span in A (quotations, publication titles, case names), every number token, a hand list of spelled-out figures and proper names, and paragraph counts. Result on 2026-11-14: **PASS.** B and C carry the same quotations, figures and names as each other, and the same as A except the four differences listed at the bottom. Reef figures were read against the ledger as it stands today. Quotations were carried word for word from A; they were **not** re-verified against the outside sources in this session (no network check was run). Their sources of record are the files named in the last column.

**Source codes.** **LEDGER** = `manuscript/ledgers/_CANONICAL_FIGURE_LEDGER.md`, "Chesapeake reef / Restitution Bond" set, or its chapter-level corrections line. **NUM** = `research/story-drafts/ch3-restitution-bond-numbers_2026-06-05.md`. **CV** = `research/story-drafts/ch3-citable-voices-ledger_2026-06-05.md` (Colden and Moore, verbatim). **SPEC** = `tools/audits/chapter-citation-specs/ch03-citation-spec_2026-06-08.md`. **FC** = the Pass 3.1 fact-check, `tools/rigor-passes/commons_bonds_rigor_pass_2026-05-25_ch3_thewaterman_stage3_pass3.1_fact_check_v1.0.0.md`. **AUTH** = the author's own words, `research/story-drafts/ch3-author-edits_2026-06-06.md`, as corrected by `ch3-FACT-CORRECTION_father_boardwalk_2026-06-08.md`. **REG** = `tools/audits/corpus-primary-source-register_2026-06-08.md`.

## Reef column (ledger rows)

| Fact in B and C | Ledger row | Match |
|---|---|---|
| "about 2,700 acres" of high-quality reef bottom lost in the James, 1910 to 1981 | Foreclosed reef extent, ~2,738 ac (Schulte 2017) | Yes (rounded as in A) |
| The James "stands in here for the Hampton bars"; no Hampton Bar acreage | Geography discipline | Yes |
| Rebuilding cost "between about $7,300 and $13,500" an acre | Restoration unit-costs | Yes |
| Floor "roughly $20 million to $37 million", "for this one river" | Restitution Bond floor | Yes |
| "about $77,000 an acre" Bay-wide average; "roughly $211 million", "the center of the estimate" | Unit-costs; CSD central | Yes (stated as center, not floor) |
| Price "built from acres"; shell mountains give no price | Extent row: area basis only | Yes |
| Maryland "more than $92 million", "roughly 1,300 acres" | Realized B₁ | Yes |
| Bay-wide "roughly $115 million"; Maryland $93.52 million, Virginia $21.77 million; NOAA itemized, ten tributaries | Realized B₁ (primary) | Yes |
| Funders: NOAA, Army Corps of Engineers, Maryland and Virginia resource agencies | Industry contribution row (all funders public) | Yes |
| "The industry's line in this column is zero." | Industry contribution, $0 | Yes |
| "The damage figure is for one river, and the public spending is for the whole Bay, so one cannot be subtracted from the other." | TA decision 8 (map: "Depends on Session A") | Yes, stated plainly; no "seven cases" census anywhere |
| No dollar figure for the Navy installation | Geography discipline (NSA Hampton Roads qualitative only) | Yes |
| No foregone-fishery dollar figure; "left all of it out of the column on purpose" | CSD ceiling, open by design | Yes |
| 99 percent is used only for harvest decline, never multiplied by a per-acre cost | Measure hygiene | Yes |
| Dock: "around $35 a bushel", 200,000 bushels, "about $7 million", one peak year, today's prices | NUM | Yes |
| Table: "roughly two hundred oysters" a bushel, "a few dollars" an oyster, "on the order of $120 million a year" | NUM | Yes |

## Chapter-level corrections that must not regress

| Fact | Source | Match |
|---|---|---|
| Tangier erosion "nearly two feet a year on the long-term average" (the paper average; no 15-feet figure) | LEDGER, chapter-level corrections line | Yes |
| Menhaden cap 51,000 metric tons, set by the Atlantic States Marine Fisheries Commission in 2017, "roughly forty percent" cut | LEDGER corrections line; REG §2.4 | Yes |
| Father poured concrete for the Buckroe Beach boardwalk; "concrete and rock with no shell in it"; the family driveway was shell | AUTH (boardwalk correction) | Yes |

## Other figures, dates and places

| Fact | Source |
|---|---|
| J.S. Darling and Son, name taken 1884 when Frank Darling joined; 160 shuckers; 200,000 bushels a year; iced tubs to Baltimore, New York and other cities; conveyor belts; piles more than four stories; shells crushed for roads and driveways or dumped in Back River, where oysters grew | AUTH msg 85 (Hampton historical marker text); FC |
| Menhaden factory at Factory Point, Fox Hill; Crabtown; James McMenamin's canning patent, 1870s | FC; SPEC |
| Company shut down 1979; author born 1980 | AUTH msg 85 |
| Oyster castles, summer 2020, Navy installation on the Hampton Roads shoreline; Bay Program supplied the young oysters | AUTH msg 83 (Navy Flagship article); LEDGER geography row |
| Grandfather at NASA Langley; Fox Hill; father's boyhood | A (author-ratified 2026-06-11); `research/story-drafts/ch3_fox-hill-watermen-biggie-phats_2026-05-09.md` |
| Five-foot wave, crests thirty feet apart or more; near-square Bay wave; deadrise; no superyachts; one oar; rain slicks and the weight of the clothes | AUTH msg 82 |
| Fifteen million bushels a year in the late 1880s; under two hundred thousand by the 1990s; 99 percent | `research/case-studies/chesapeake-fisheries.md`; FC |
| MSX late 1950s; Dermo after; overharvest, disease, sediment | FC |
| Biggie: six-pack of Coca-Cola in a wire carrier, no ice, cooler or lunch; quarter turn of the wrist; dead more than thirty years; died before the 1994 shad closure | AUTH msg 84; `ch3_fox-hill-watermen-biggie-phats_2026-05-09.md` |
| Rockfish: collapse by late 1970s; Maryland moratorium five years from 1985; declared restored 1995 | FC |
| 2024 Maryland young-of-year index 2.0 against long-term average 11.0; sixth such season in a row | FC; `research/outreach/subjects/colden/background-brief_2026-05-08.md` |
| Virginia shad fishery closed January 1994; no recovery | FC |
| 2025 winter dredge survey, about 238 million crabs; second-lowest since 1990; sixth consecutive below-average year | FC; Colden background brief |
| Reedville, mouth of the Great Wicomico River, Northumberland County; several hundred employees; largest single fishery on the East Coast | FC |
| 2023 VIMS proposal, $3 million; General Assembly declined to fund | FC; SPEC |
| O'Connor petition: filed last day of 2025; 349 pages; three cases with citations; hearing April 21, 2026; 1,266 comments; vote six to two against | SPEC; FC |
| Watershed: about 64,000 square miles, six states and the District of Columbia; Bay Program established 1983; advisory committee review: not on track | FC |
| Mobjack Bay; grass beds visible in the early 2000s (author's observation) | A |
| Tangier: a bit over a square mile; inhabited since the 1770s; eight generations; Smith Island twelve miles north | FC |
| Tilghman: Whewell on Gowe's boat, Broad Creek, 2023; Fisher and Schwartz three years later; *Maryland Matters* photographs | SPEC |
| Maryland restoration: five tributary-scale sanctuaries; hundreds of acres; tens of millions of oysters a year; population roughly tripled since 2005; federal disaster declaration request "in the same year" | FC; CV |
| Norway: fewer people than Virginia; late 1960s; fund kept more than thirty years | A; Ch 4 carries the detail |
| Gulf of Maine, Bristol Bay, West Africa, Mekong Delta | A |

## Quotations (all word for word from A; all present in B and C)

| Speaker and outlet | Words (opening) | Source of record |
|---|---|---|
| J.C. Hudgins, *Maryland Matters* | "You're lucky if you can put $150 in your pocket per day," / "And it ain't no easy job…" / "People aren't going to spend $20 for a pint of oysters…" | FC |
| Allison Colden, public statements | "Maryland's striped bass surveys have made it clear," / "we're facing a looming disaster…" | CV |
| Colden | "there are very few levers left to pull." | SPEC; Colden verification packet |
| Colden | "rely on striped bass for their food, their businesses, and their futures…" / "pummeling" | CV |
| Chris Moore, 2024 stock-assessment response | "Despite recent management actions, striped bass continue to struggle…" | CV |
| Bill Goldsborough, *Smithsonian Magazine* | "Our objective is to try to restore the health of bay and aquatic life…" / "We see that task taking place over a longer term [...]…" | SPEC; FC |
| Colden | "The red flags are flying for blue crabs," / "with more than five years of below average crab numbers…" | CV |
| (people who watch ospreys) | "a hollowing" | A |
| Colden | "Just as we were confident in increasing the total allowable catch…" / "we need to be as willing to take reductions…" | CV |
| Genny Nesslage, WHRO | "We don't know the abundance of menhaden in the bay at any given time relative to the coast." | SPEC; FC |
| Rob Latour, WHRO | "We have no data to really do this in a meaningful way, from a biological perspective." | SPEC |
| O'Connor petition | "did not have" / "still does not have" / "a Bay-wide estimate of menhaden biomass…" | SPEC |
| James "Ooker" Eskridge, Thomson Reuters Foundation | "We're talking about saving a culture, the people, (a) way of life." | SPEC |
| Cook Cannon, *Smithsonian Magazine* | "I could cry to think about what's going to happen to Tangier." | SPEC; FC |
| Cameron Evans, Thomson Reuters Foundation | "If you can't save an island a mile and a half long…" | SPEC; FC |
| Andy Harris, *Maryland Matters* | "Our watermen are pretty resilient," / "They're like our farmers…" | SPEC; FC |
| Colden | "Large-scale oyster restoration is working," / "Our effort to bring oysters back from the brink…" / "continued recovery is not guaranteed." | CV |
| Mitch Tarnowski, *Maryland Matters* | "There are plenty of oysters out there," / "They're just not being harvested." (twelve words: counted) | SPEC; FC |
| Colden | "Despite a growing oyster population," / "Maryland's watermen are feeling the pinch…" | CV |
| Jason Ruth, *Maryland Matters* | "While the demand for boutique aquaculture oysters has grown…" / "the shucked oyster sector," / "has seen a 60-year nationwide decline." | SPEC; FC |
| Colden | "One of the most important ways people connect with the Chesapeake Bay," / "is through eating seafood and fishing." / "there's certainly a lot fewer eyes on the water…" | CV |

Sayings carried as A has them (indirect speech, not in quotation marks): Biggie's "his lunch was waiting for him in the water, as fresh as it could be"; the Smith Island saying about mud between your toes.

## Where B and C differ from A in a figure, date or name (all four are deliberate)

| A has | B and C | Why |
|---|---|---|
| "A rounder program-level figure of about $108 million… corroborates the magnitude, nothing more." | Not carried | Call 5 (state what the public paid once) and style rule 20. The ledger keeps $108M as a rounding corroborator only. |
| "before the English came up the James in 1607" | Not carried | The sentence listed what the chapter was *not* starting from; cut with it (rule 19). |
| "HRBT expansion" | "the expansion of the Hampton Roads Bridge-Tunnel" | Rule 10, spell out a local term. Same fact. |
| "the instrument that was built in Oslo" | "what Norway built for its oil" | Call 2, Norway in one paragraph. Same fact. |

## New factual statements in B and C that A does not make (for the author's eye)

1. **"and no second moratorium has been called."** This replaces the unsourced claim in A's retired-waterman paragraph. It is true on the chapter's own account, but it has no citation on file. See QUESTION 1 in the change notes.
2. **Hardin's essay named by its title**, "The Tragedy of the Commons." A named the idea without the title.
3. **C only: three short definitions** set inside sentences, of *moratorium*, *forage fish* and *reduction fishery* ("because it reduces the fish to meal and oil"). Standard meanings; listed so he can strike any he doesn't want (style rule 29).
