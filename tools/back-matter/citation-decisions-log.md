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

### 001. Pistor, *The Code of Capital* (2019): should the appendix cite it? **OPEN**

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

### 002. Christophers, *The Price Is Wrong* (2024): should the appendix cite it? **OPEN**

- **Facts.** In the bibliography (listed twice). Cited in Chapters 5, 9 and 10. Not in the appendix. Chapter 5
  calls his the most forceful living version of the worry that pricing turns a commons into a tradable asset,
  and says a later chapter answers it in full.
- **Why it might belong.** If the appendix had a section answering the objection that pricing commodifies, he
  would be its first citation. It has none: the words "commodify" and "financialize" do not appear in v2.0.1.
- **Why it might not.** His subject is investment and profit in the energy transition. The book's answer to
  him is an argument in Chapters 5 and 9, not a formal result.
- **Recommendation: KEEP OUT** of the appendix. Stay in the bibliography. Revisit only if the appendix gains a
  section on the commodification objection.

### 003. Susskind, *Growth: A Reckoning* (2024): should the appendix cite it? **OPEN**

- **Facts.** In the bibliography (listed twice). Cited in Chapter 9 only, in a list of neighbouring
  frameworks. Not in the appendix.
- **Reasoning.** The book names him as company, and uses none of his method or results. Nothing in the
  appendix depends on him.
- **Recommendation: KEEP OUT** of the appendix. Stay in the bibliography while Chapter 9 names him. When
  Chapter 9 is rebuilt, check that it still does; if not, this becomes a REMOVE question for the bibliography.

### 004. Daly: the appendix discusses him without a dated work or a §18 entry. **OPEN**

- **Facts.** TA v2.0.1 §14.6 is headed "Daly (1990s)" and attributes strong sustainability to him. §18 has no
  Daly entry. The book's bibliography has *Steady-State Economics* (1977; rev. 1991).
- **Reasoning.** The appendix cites inline, so by its own rule it needs the entry. "1990s" is not a citation.
  Which of his works says what §14.6 attributes to him has not been checked.
- **Recommendation: ADD** a §18 entry and a dated citation in §14.6 at the next appendix version, after the
  claims check of the appendix confirms the work and the wording.

### 005. Brian Barry: cited in the appendix with no year and no entry anywhere. **OPEN**

- **Facts.** TA v2.0.1 §14.4 says "Brian Barry (later) sharpened it: the overall range of opportunities open
  to successive generations should not be narrowed." No year. No entry in §18 or in the book's bibliography.
- **Reasoning.** As it stands the sentence has no source in the project.
- **Recommendation:** the claims check of the appendix finds the source and reads it. If found, **ADD** to
  both lists. If not, **REMOVE** the sentence. No source is named here from memory.

### 006. Housekeeping: three works are listed twice in the bibliography. **REMOVE (duplicates), done 2026-11-15 on the author's instruction**

- **Facts.** `sources/bibliography.md` has two full entries each for Pistor 2019, Christophers 2024 and
  Susskind 2024 (near lines 532 to 548 and 1081 to 1097), with different summaries.
- **Ruling and action (2026-11-15):** the author said to remove the duplicates. The three §19 copies were
  removed and the §13 entries kept, because §13 records that the engagement landed in the chapters and §19 is
  the list of sources not yet integrated. The reason is also written in §19's changes log. The rendered
  bibliography was regenerated and is unchanged (§19 is not rendered).

### 007. New comp titles that the book does not cite. **OPEN**

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

---

## Ruled entries

None yet.
