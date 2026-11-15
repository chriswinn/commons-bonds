# Citation decisions log

**Status:** internal. Started 2026-11-15 on the author's instruction.

**What this is for.** When someone asks whether a work should be in the bibliography or the Technical
Appendix, the question, the facts, the reasoning and the author's ruling are written here. A work that is
left out or taken out gets an entry saying why, so the decision is not made twice and its reason is not lost.

**How to use it.** Add an entry with status **OPEN** and a recommendation. The author rules. Then change the
status to **ADD**, **KEEP OUT**, **REMOVE** or **KEEP**, with the date and his reason in his words where he
gave one. Any change to the appendix or bibliography that follows from a ruling cites the entry number in its
commit message. Nothing here changes a source file by itself.

**Two lists, two tests.**
- The book's bibliography (`sources/bibliography.md`) lists works the book uses. A work belongs there if a
  chapter or the appendix cites it.
- The appendix's own §18 is the subset the appendix cites inline. A work belongs there only if the appendix
  cites it. Being a comp title is not a reason.

---

## Open entries

### 001. Pistor, *The Code of Capital* (2019): should the appendix cite it? **ADD (author, 2026-11-15: "as recommended")**

- **Facts (checked 2026-11-15).** In the bibliography (listed twice, see 006). Cited in Chapters 5, 9 and 10.
  Not cited anywhere in TA v2.0.1. A lead comp in the proposal, and the overview says "where Pistor diagnoses
  the legal modules that encode cost severance, the framework prices what they sever."
- **Why it might belong.** Chapter 5 does more than credit her. It uses her four attributes (priority,
  durability, universality, convertibility) as a test of whether an accountability bond is a real instrument.
  The appendix is where the bond is defined (Definition 1.7, §5). A reader who goes from Chapter 5 to the
  appendix finds the instrument without the test the chapter applied to it. The appendix already gives Harvey
  this kind of credit in §14.7 ("Harvey diagnoses the mechanism; RCV measures its size"), and Pistor is the
  closer neighbour.
- **Why it might not.** The appendix is the mathematics. Her argument is legal, and the chapter carries it.
- **Recommendation: ADD**, as one short entry in §14 and one row or clause where the bond is defined, at the
  next appendix version. Write it only after reading the passage of her book that Chapter 5 relies on. The
  appendix Darity has (v2.0.1) is not changed.
- **Claims-check evidence (2026-11-15), still OPEN.** Confirmed: the name does not occur in v2.0.1. The Chapter 5
  claims check found two faults in the chapter's own account of her (the list of modules; "lack the two
  attributes"), so the appendix cannot take its Pistor from the chapter. Recommendation narrowed: **ADD in §14
  only**, written from the book, after the author rules on the two Chapter 5 items; nothing at Definition 1.7
  yet. Report: `tools/audits/claims-check_technical-appendix_2026-11-15.md`, Part 6.
- **Second session (2026-11-15, §11 to §17), still OPEN.** No sentence in §11 to §17 needs her or contradicts her. §15.2.2, where the appendix says what kind of instrument the Foreclosure Bond is, is the only other place a clause could sit; §14 alone is still the recommendation. Unchanged: **ADD in §14 only, after reading.**

- **Update (2026-11-15, later).** Chapter 1 has now been read (open sample chapter at wid.world). Her modules:
  "contract law, property rights, collateral law, trust, corporate, and bankruptcy law." Her four attributes are
  as Chapter 5 gives them. The §14 entry can be written from her text; ready for the author's ruling.

### 002. Christophers, *The Price Is Wrong* (2024): should the appendix cite it? **KEEP OUT of the appendix (author, 2026-11-15: "as recommended")**

- **Facts.** In the bibliography (listed twice). Cited in Chapters 5, 9 and 10. Not in the appendix. Chapter 5
  calls his the most forceful living version of the worry that pricing turns a commons into a tradable asset,
  and says a later chapter answers it in full.
- **Why it might belong.** If the appendix had a section answering the objection that pricing commodifies, he
  would be its first citation. It has none: the words "commodify" and "financialize" do not appear in v2.0.1.
- **Why it might not.** His subject is investment and profit in the energy transition. The book's answer to
  him is an argument in Chapters 5 and 9, not a formal result.
- **Recommendation: KEEP OUT** of the appendix. Stay in the bibliography. Revisit only if the appendix gains a
  section on the commodification objection.
- **Claims-check evidence (2026-11-15), still OPEN.** Confirmed: not named in v2.0.1, and the words "commodify"
  and "financialize" do not occur. The Chapter 5 check found the chapter's summary of his book says more than
  the book. Recommendation unchanged: **KEEP OUT**. Report: `tools/audits/claims-check_technical-appendix_2026-11-15.md`, Part 6.
- **Second session (2026-11-15), still OPEN.** §14 and §15 answer eight neighbouring frameworks; none is the objection that pricing turns a commons into an asset. Unchanged: **KEEP OUT** unless the appendix gains that section, which is a question of scope for the author.

### 003. Susskind, *Growth: A Reckoning* (2024): should the appendix cite it? **KEEP OUT of the appendix (author, 2026-11-15: "as recommended")**

- **Facts.** In the bibliography (listed twice). Cited in Chapter 9 only, in a list of neighbouring
  frameworks. Not in the appendix.
- **Reasoning.** The book names him as company, and uses none of his method or results. Nothing in the
  appendix depends on him.
- **Recommendation: KEEP OUT** of the appendix. Stay in the bibliography while Chapter 9 names him. When
  Chapter 9 is rebuilt, check that it still does; if not, this becomes a REMOVE question for the bibliography.
- **Claims-check evidence (2026-11-15), still OPEN.** Confirmed: not named in v2.0.1; no definition, method or
  figure draws on him. Recommendation unchanged: **KEEP OUT**. Report: `tools/audits/claims-check_technical-appendix_2026-11-15.md`, Part 6.
- **Second session (2026-11-15), still OPEN.** Nothing in §11 to §17 concerns growth as such. Unchanged: **KEEP OUT.**

### 004. Daly: the appendix discusses him without a dated work or a §18 entry. **ADD after reading (author, 2026-11-15: "as recommended")**

- **Facts.** TA v2.0.1 §14.6 is headed "Daly (1990s)" and attributes strong sustainability to him. §18 has no
  Daly entry. The book's bibliography has *Steady-State Economics* (1977; rev. 1991).
- **Reasoning.** The appendix cites inline, so by its own rule it needs the entry. "1990s" is not a citation.
  Which of his works says what §14.6 attributes to him has not been checked.
- **Recommendation: ADD** a §18 entry and a dated citation in §14.6 at the next appendix version, after the
  claims check of the appendix confirms the work and the wording.
- **Claims-check evidence (2026-11-15), still OPEN.** Two works found by search, neither read (the host is
  outside the session's network): Daly, "Toward Some Operational Principles of Sustainable Development,"
  *Ecological Economics* 2(1) (1990): 1–6 (capital as complements); and his 1995 reply to Beckerman in
  *Environmental Values* 4(1) (weak and strong sustainability in his own words; title and pages to confirm).
  *Steady-State Economics* is not the source for §14.6. Not found: "critical natural capital" as his term; any
  source for the GDP sentence. Recommendation: **ADD both after reading**; head the section "Daly (1990,
  1995)"; drop or re-credit "critical"; source or cut the GDP sentence; "consistent with" for "confirming."
  Both are on the tentative list. Report: `tools/audits/claims-check_technical-appendix_2026-11-15.md`, Part 6.
- **Correction and update (2026-11-15, later).** The host was not blocked by the network; it did not resolve, and the
  session should have looked elsewhere or asked. Daly 1995 has now been **read in full**: "On Wilfred
  Beckerman's Critique of Sustainable Development," *Environmental Values* 4(1) (1995), within pp. 49–70. It
  supports §14.6 on weak and strong sustainability in his own words (substitutes against complements). It
  does not use "critical natural capital" and says nothing about GDP. Daly 1990 is still unread.
- **Second session (2026-11-15), still OPEN. The 1995 paper has now been read in full.** Daly, "On Wilfred Beckerman's Critique of Sustainable Development," *Environmental Values* 4(1) (1995): 49–55. It supports the definitions ("Strong sustainability assumes that manmade and natural capital are basically complements," p. 49; each "maintained intact separately," p. 53). It does not support "critical natural capital" (his words: "natural capital is the critical requirement," p. 50), the GDP sentence (absent), or "maintaining the physical stock itself" for the appendix's resources: for non-renewables his rule is that "the rate of depletion should be equal to the rate at which renewable substitutes can be developed" (p. 50), and he dismisses the no-extraction reading as "absurdly strong sustainability" (p. 49). Recommendation now: **ADD the 1995 paper**; head the section "Daly (1995)"; restate his non-renewable rule as he gives it; cut or source the GDP sentence; "consistent with" for "confirming." The 1990 paper has since been read in full by the other appendix session (report, Addendum 3); nothing is asked of the author.
- **Update (2026-11-15, later still).** Daly 1990 has now been **read in full**: natural and man-made capital are
  "basically complementary and only very marginally substitutable"; "Sustainable development requires that
  natural capital be maintained intact." No "strong sustainability," no "critical natural capital," nothing on
  GDP. Both papers are read; the recommendation is ready for the author's ruling.

### 005. Brian Barry: cited in the appendix with no year and no entry anywhere. **ADD once the page is in hand, otherwise the sentence comes out (author, 2026-11-15: "as recommended"; library list L2 if no online source is found)**

- **Facts.** TA v2.0.1 §14.4 says "Brian Barry (later) sharpened it: the overall range of opportunities open
  to successive generations should not be narrowed." No year. No entry in §18 or in the book's bibliography.
- **Reasoning.** As it stands the sentence has no source in the project.
- **Recommendation:** the claims check of the appendix finds the source and reads it. If found, **ADD** to
  both lists. If not, **REMOVE** the sentence. No source is named here from memory.
- **Claims-check evidence (2026-11-15), still OPEN.** Two secondary sources, found by search, credit "the
  overall range of opportunities open to successor generations should not be narrowed" to Barry,
  "Circumstances of Justice and Future Generations," in Sikora and Barry (eds.), *Obligations to Future
  Generations* (Temple University Press, 1978), pp. 204–248, at p. 243. The appendix has "successive." The
  chapter was not read. Recommendation: **ADD once someone has the page in hand**, with the year and the
  exact words; **REMOVE the sentence** if the book cannot be obtained before the next version. On the
  tentative list. Report: `tools/audits/claims-check_technical-appendix_2026-11-15.md`, Part 6.
- **Second session (2026-11-15), still OPEN.** The 1978 volume and chapter are confirmed to exist (publisher's page for the reprint). The sentence was not found in anything that could be opened. The Stanford Encyclopedia entry does not contain it; for the nearby idea (options reduced to "an inadequate range") it cites a different essay of his, "Sustainability and Intergenerational Justice" (1999). Unchanged: **ADD once someone has p. 243 of the 1978 book in hand; otherwise REMOVE the sentence.** This needs a library copy; nothing online was blocked.

### 006. Housekeeping: three works are listed twice in the bibliography. **REMOVE (duplicates), done 2026-11-15 on the author's instruction**

- **Facts.** `sources/bibliography.md` has two full entries each for Pistor 2019, Christophers 2024 and
  Susskind 2024 (near lines 532 to 548 and 1081 to 1097), with different summaries.
- **Ruling and action (2026-11-15):** the author said to remove the duplicates. The three §19 copies were
  removed and the §13 entries kept, because §13 records that the engagement landed in the chapters and §19 is
  the list of sources not yet integrated. The reason is also written in §19's changes log. The rendered
  bibliography was regenerated and is unchanged (§19 is not rendered).

### 007. New comp titles that the book does not cite. **KEEP OUT of the reader-facing bibliography (author, 2026-11-15: "as recommended")**

- **Facts.** The comps the author ratified on 2026-11-15 include three works the book does not cite and the
  bibliography does not list: Davies, *The Unaccountability Machine*; Dasgupta, *On Natural Capital*;
  Riofrancos, *Extraction*. The comps file's own rule is that comps should be works the book engages, with at
  most one or two exceptions framed as shared readership.
- **Reasoning.** A comp does not have to be cited in the book, and none of these should be added to the
  bibliography merely for being a comp. The proposal has to describe them truthfully: as recent books in the
  same conversation, not as works the book builds on.
- **Action (2026-11-15, author's instruction):** all candidates from the comps research are now listed as
  tentative in `sources/bibliography.md` §19 (not rendered for readers), each with the reason it is there.
- **Recommendation: KEEP OUT** of the reader-facing bibliography now. In the proposal, frame all three as neighbours. If a
  chapter that is open for rebuild comes to use one (Davies on accountability is the likeliest), add it then
  and record it here. No signed-off chapter is reopened for this.

### 008. Tertiary web pages used to date the 1969 black lung strike. **OPEN**

- **Facts.** The Chapter 2 claims check (row 33) found the chapter's "wildcat strike in 1968" contradicted by
  outside accounts that give February 18, 1969. Those accounts were a Clio history page, a Wikipedia entry on
  Arnold Miller, and two political newspapers' pages, seen through a search summary.
- **Reasoning.** They were enough to raise the flag. None is a source a reader should be sent to, and none
  was read in full.
- **Recommendation: KEEP OUT** all four. Settle the date from Derickson (§24A, already held) or the
  encyclopedia's "Black Lung Movement" entry, both on the tentative list as not read.

### 009. News accounts of the Purdue pleas and the Sackler withdrawals. **OPEN**

- **Facts.** The Justice Department's pages could not be reached from the session. The claims check (row 79)
  compared the draft with news and trade-press accounts (insurance and legal trade sites, a local ABC page).
- **Reasoning.** The pleas and amounts are matters of federal record, and the primary releases exist. A
  trade-press rewrite adds nothing and gave two different totals for 2007 ($600 million; $634.5 million).
- **Recommendation: KEEP OUT** the news accounts. Cite the Justice Department releases (tentative list, not
  read) once someone has read them, and Keefe (§9) for narrative.

### 010. Alpert and colleagues (2022) as support for where OxyContin went. **OPEN**

- **Facts.** §24E says the paper "Backs: the geographic-distress half of the Ch2 Purdue 'four-characteristic
  target map' attribution." The abstract, read 2026-11-15, explains the geography by state prescription
  rules: states with triplicate programs got less marketing, and distribution there "was about 50% lower."
  It says nothing in the abstract about collapsed wage economies.
- **Reasoning.** The paper is sound and belongs in the bibliography. What does not hold is the note saying
  what it backs. As written, it would lead a later session to cite the paper for a claim it does not make,
  and for one it partly cuts against (Chapter 2 claims check, row 77).
- **Recommendation: KEEP the work; REMOVE the "Backs" note** and replace it after the article itself is read.
  Until then it is **kept out as support for the sentence** "The drug found its largest markets where the wage
  economy had already collapsed."

### 011. Sources that turned up in the scrip search and should not be cited. **OPEN**

- **Facts.** The search for coal-camp scrip returned Wikipedia's "Company scrip" (which gives 1967 as the year
  Congress outlawed coal scrip), a coin collectors' newsletter, coal-camp hobby sites, and a trade-press
  summary of the Blackley prevalence paper.
- **Reasoning.** The encyclopedia entries by Athey and McGehee cover the same ground with named authors and
  source lists. The Wikipedia date has no primary record behind it in anything read, and Athey says scrip
  "disappeared with the collapse of the coal industry in the 1950s."
- **Recommendation: KEEP OUT** all of them. In particular, do not use the 1967 date.

### 012. Secondary pages used to locate the Barry and Daly works. **OPEN**

- **Facts.** The appendix claims check (2026-11-15) found the Barry quotation in a Springer article and an
  IntechOpen chapter on the ethics of nuclear power, and found Daly's two papers through a course page, a
  review article and Beckerman's reply. A set of lecture notes on Barry's 1997 essay was also opened.
- **Reasoning.** They were enough to identify the works. None is the source, and the two that quote Barry
  disagree with the appendix by one word, which only the 1978 chapter can settle.
- **Recommendation: KEEP OUT** all of them. Cite Barry 1978 and Daly 1990 and 1995 once read (entries 004, 005).

### 013. Web reproductions of Ostrom's Table 3.1. **OPEN**

- **Facts.** The appendix claims check (2026-11-15) marked the wording of Ostrom's third design principle
  (TA Definition 1.10) SUPPORTED on two web reproductions and a library record that gives "Table 3.1, p. 90."
  None was opened, and the book was not opened.
- **Reasoning.** The book is already in the bibliography and is the only thing to cite. The reproductions agree
  with each other, which is why the row was marked supported, but other summaries found in the same search
  paraphrase the principle more loosely. The 2026-11-11 session also asked for the page to be checked in the
  author's copy.
- **Recommendation: KEEP OUT** all three. Confirm the wording and page 90 in the book, and treat the row as
  resting on secondary copies until then.

### 014. Encyclopedia, blog and report pages used for Barry, Rawls and the discount rates. **OPEN**

- **Facts.** The check opened the Stanford Encyclopedia's entry on intergenerational justice, and saw through
  search a blog reading of Rawls's §44 to §45, a Global Priorities Institute talk, a Boston University report
  on the Stern Review debate, an NBER working paper and a Resources for the Future commentary.
- **Reasoning.** Each summarizes a primary text the appendix already names: Rawls 1971, the Stern Review,
  Nordhaus. They raised three flags (which edition of Rawls the just-savings wording comes from; Stern's 1.4
  percent; no source for Nordhaus at 5.5 percent). None settles one.
- **Recommendation: KEEP OUT** all of them. Settle each point from the primary text. The one secondary work
  worth reading for the Rawls point is Picchio 2024 (tentative list), and only as a guide to the editions.

### 015. Secondary accounts of the black-lung total and the trust fund's debt. **OPEN**

- **Facts.** For TA §11.6 the check saw, through search: ethosrisk.com and the National Academy of Social
  Insurance ("over $47 billion" since 1970); an NPR report ("more than $6 billion in debt"); an Appalachian
  Voices report (February 2024); and, from the Chapter 5 check, Wyoming Public Media ("about $6.5 billion").
- **Reasoning.** The total has a primary source now: the Labor Department's chart for fiscal 1970 to 2009
  ($44.2 billion). The debt has one too, the Treasury's statement for the trust fund, which no session has
  yet read. The secondary accounts give three different debt figures for nearly the same date.
- **Recommendation: KEEP OUT** ethosrisk.com, the NPR report, the Appalachian Voices report and Wyoming Public
  Media as sources for these two figures. **Hold** the National Academy of Social Insurance paper (Boden) on the
  tentative list: it may be the best citable later total. Read in part later the same day; it also
  records that Congress forgave much of the fund's debt in 2009. Cite the Labor
  Department chart and, once read, the Treasury statement.
- **Correction (2026-11-15, later).** The claims check first set Wyoming Public Media's "about $6.5 billion"
  against the appendix's $5.1 billion and called the latter contradicted. Withdrawn: the Labor Department's
  FY 2026 budget document shows $6.5 billion was the sum refinanced in 2008, and a trade article gives $5.1
  billion for September 2024. Neither secondary figure is sourced, which is the reason to keep both out. Add
  the trade article (Insurance Business, April 28, 2026) to the keep-out list.

### 016. Pages used only to locate sources in the appendix check, second session. **OPEN**

- **Facts.** The second session of the appendix claims check (2026-11-15) used these to find or date things: the
  Stanford Encyclopedia entry on intergenerational justice (read); the publisher's page for the reprint of
  Sikora and Barry; an encyclopedia page and a human-rights group's page on the Baogang tailings dam; two
  commercial summaries of Ostrom's book; trade-press reports on the Stratos plant; news rewrites of BP's 2012
  plea; a Colorado legislative handbook quoting the National Conference of State Legislatures.
- **Reasoning.** Each pointed to a primary source that can be cited instead: Rawls's own books; Barry's
  chapter; a journal study and one named article on Baotou; Ostrom's book; the company's own statements; the
  Justice Department's release; the Conference's page. Two of them disagree with each other on Baotou's
  yearly tailings (7 to 8 million tons against "millions").
- **Recommendation: KEEP OUT** all of them. The primaries are on the tentative list as not read. (Entry 014 already covers the encyclopedia entry; this adds the rest.)

### 017. Rawls's later books: the appendix quotes them under "Rawls (1971)." **OPEN**

- **Facts.** TA v2.0.1 §14.4 gives the just-savings principle as "principles we would wish all preceding and
  succeeding generations to have followed," under the heading "Rawls (1971)." The Stanford Encyclopedia
  (read 2026-11-15) places that wording in *Political Liberalism* (1993: 274) and *Justice as Fairness*
  (2001: 160), and says the 1971 argument used "a motivational assumption" that he "withdraws" in 1993.
  Neither later book is in §18 or the bibliography. The bibliography has no Rawls entry at all.
- **Reasoning.** The appendix cites inline, so the sentence needs the book it comes from. Citing 1971 for
  the later wording is the kind of slip a philosopher reading §14.4 will catch.
- **Recommendation: ADD** *A Theory of Justice* (already in §18) to the bibliography, and **ADD** whichever
  later book the author reads the wording in, cited at that sentence. Until one is read, reword §14.4 so it
  quotes nothing: the claims check offers a sentence (report, section 1b, item 2).

### 018. State overdose figures as support for "the highest … in the United States." **OPEN**

- **Facts.** TA §11.1 says McDowell County has "the highest per-capita opioid death rate in the United
  States." The check found a West Virginia health department slide deck (2020–2022: 186.3 drug-overdose
  deaths per 100,000, highest in the state) and a USAFacts page (2022, highest in the state), both via search.
- **Reasoning.** Both are about one state's counties and about all drugs, not opioids. Neither ranks the
  country's counties. Cited beside the sentence as it stands, they would appear to support a claim they do
  not make (the same trap as entry 010).
- **Recommendation: KEEP the state deck on the tentative list** as a source for a narrower sentence ("the
  highest rate of any county in West Virginia in 2020–2022"), once read. **KEEP OUT both as support for the
  national superlative**, and keep USAFacts out altogether (it restates the federal data).

---

## Ruled entries

None yet.
