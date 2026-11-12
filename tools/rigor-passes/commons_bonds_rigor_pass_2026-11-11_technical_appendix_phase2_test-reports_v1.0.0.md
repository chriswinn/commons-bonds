# Technical Appendix Phase 2: test reports and items for the author (2026-11-11)

**Status:** PROPOSED (internal). Session A of the parallel window. The TA is now
`manuscript/technical-appendix/TechnicalAppendix_v2.0.1.html` on the session branch; v2.0.0 is archived.
**Merge to main waits on the author's OK.** Render: `commons_bonds_technical_appendix_v2.0.1_render_2026-11-11.pdf`
(this folder; 109 pages; no missing glyphs). Changelog against Darity's copy:
`tools/audits/ta-darity-version-changelog_2026-11-11.md`.

Checks at close: calc engines 67/67 and 28/28, 0 mismatches; invariants gate HIGH = 0; notation regenerated.

---

## 1. Hotelling-rent test (decision 3 condition)

Question per case: can rent per unit (price minus marginal extraction cost) be measured from a sourced figure?

| Case | Computes? | Why |
|---|---|---|
| Norway oil and gas | **Yes, as a proxy** | The state's net cash flow from petroleum is published year by year (Ministry of Finance / Statistics Norway, at norskpetroleum.no). I summed 1971–2025: about NOK 14,860 billion in constant 2027 kroner, about NOK 270 (about $25) per BOE. With the state's 70–80% share, rent is about $32–36 per BOE. |
| McDowell coal | **No. Bound only** | No sourced price-minus-cost figure for these tons. Rent cannot exceed price (H ≤ P), which gives a bound and nothing more. |
| Deepwater Horizon | No | Revenue is a reserve × price derivation; no sourced cost. |
| Libby | No | Revenue is an unconfirmed industry estimate; no cost record. |
| Baotou | No | Export revenue only. |
| Chesapeake reef | No, not applicable | Backward case on a renewable stock; the split is of the forward term. |

**Result.** §4 is written as the split RCV − B₂ = (RCV − H) + (H − B₂) with **Norway as the only worked
example**. No rent was invented. Norway's numbers: carbon floor about $70/BOE, rent about $32–36, fund about $36.
So (RCV − H) is at least $34–39 and (H − B₂) is about −$5 to $0. In words: Norway has bonded all of its rent;
the whole remaining gap is cost that no handling of the rent would pay. McDowell appears as one sentence with
the bound (RCV − H ≥ $385 per ton).

## 2. Decision-2 wording test ("priced with the cost in view")

Applied to every §11 case, §12 Scenarios 1 and 5, and Walkthrough 2.

| Case | What the wording gives | Right? |
|---|---|---|
| McDowell coal | Reclamation bonds count (instrument). Black lung was not visible to miners, so wages priced none of it. Carbon and community costs unpriced. CS > 0. | Yes |
| Deepwater | $61.6B was paid after the fact, forced by litigation. | **Wrong as first worded** (see finding A) |
| Libby | Hazard concealed; wages priced nothing; $250M repaid later. CS > 0. | Yes, with finding A |
| Baotou | No instrument; villagers made no choice. CS > 0. | Yes |
| Norway | Norwegians chose knowingly and hold the fund: domestic cost priced. Carbon falls on others: unpriced. | Yes, with finding B |
| Reef | Nothing priced at the time; public paid later. | Yes, with finding A |
| Scenario 1 (colony water) | Community chooses knowing the cost: CS = 0. | Yes |
| Scenario 5 (colony mines its own ore) | Knowing choice by the party that gains and bears: B = RCV, CS = 0. | Yes |
| Walkthrough 2 (commute) | A choice, but not one made knowing the cost: nothing priced, CS > 0. | Yes |

**Finding A. "When the deal was made" is too narrow.** Read literally it sets the bond to zero for every
backward case, because restitution is paid afterwards. Definition 1.7 now says the pricing can happen when the
deal is made **or afterwards, as payment actually made toward repair** (Definition 1.12).

**Finding B. A payment must count only against the cost it priced.** Without this, a crabber's danger premium
would offset the cost of absence, and Norway's fund would be credited against carbon. Definition 1.7 now carries
one sentence ("one payment, one cost") and asks for CS by component where costs are priced separately.

**Consequence the author should know:** the definition makes two facts part of every case: who bears each cost,
and what that party knew at signing. Each §11 case now has an attribution paragraph.

**Finding C (the author's, 2026-11-11). "In view" is wrong for instruments.** A bond can be posted against a
risk nobody can size. Knowledge matters only where the bearer's own consent does the pricing. Definition 1.7 now
has two routes: (a) an instrument, which counts whatever was known; (b) the bearer's informed consent, which
counts only as far as the bearer could see the cost. Cost severance is cost borne and neither bonded nor knowingly
accepted. Re-tested against the same nine cases: same answers. The phrase "priced with the cost in view" is retired.

Same day, at the author's direction: the borrowed/added section now ends with a list of what is the framework's
own, using its names (cost severance, the Cost Severance Decomposition, the Commons Inversion Test and Four Gates,
the three states, the per-unit reserve, the terms defined), with the size of each claim stated.

Please read Definition 1.7 in the PDF (page 9 or so) and confirm the final wording.

## 3. Number changes that need your OK before merge

| # | Item | Was | Now | Why |
|---|---|---|---|---|
| 1 | **McDowell cost severance** | packet said "about $440–490" | **at least about $425–450** per ton | The $50 low end of the bond had no derivation. Derived from the TA's own components the bond is $88–100 per ton, so the subtraction lands lower. Still a lower bound. |
| 2 | **Norway's bond** | $48/BOE | **about $36/BOE** (the fund) | $48 divided the fund by the capture rate and mixed investment returns into rent. Review item N4 said this needs your call. |
| 3 | **Norway Method 3** | $96–610, central $281 | **$320–3,040**, center about $985 | α is now physical (same as coal). A savings fund does not make a barrel restorable. Review item C2. |
| 4 | **Norway cost severance** | $13–15 trillion | **a floor: at least about $1.9 trillion** ($34/BOE) | Carbon term alone, minus the fund. Uses only sourced inputs. The replacement-cost cross-check gives a larger gap ($125–386/BOE) and is shown beside it. |
| 5 | **Libby** | $2.6B floor, 26 to 1 | **cleanup over $600M, about 6 × revenue**; Grace repaid $250M of it | The $250M was a reimbursement of cleanup, not settlements, and was being added to the cleanup it repaid. The $50M/yr monitoring and $500M property figures have no source and are now Open. |

Only Ch 6 (due for rebuild) carries any of the old Norway figures. Ch 5's redraft already says "about six times."

## 4. Things I could not source, left open in the TA

- The $8–12 billion of continuing Gulf damage (Deepwater). Labeled as an estimate with no primary source.
- A sourced end-use split for Pocahontas coal (coking against steam). The TA says so and shows the result barely
  moves (S_max = 0 gives $573).
- Libby medical monitoring and property losses; payments to Libby victims through Grace's bankruptcy trust.
- Naik et al. 2017: I have the journal and year from the repo's source register but not the article title.
- Ostrom's principle 3 is cited to chapter 3, Table 3.1. Please check the page in your copy before the send.
- Asare et al. 2023: first author's initials are from memory of the search record; check against the paper.

## 5. Call-derived material: status

Requirement: zero material from the May 2026 call. What I found and did:

| Item from the call | In v2.0.0 | In v2.0.1 |
|---|---|---|
| Ostrom and divided communities | Definition 1.10 paragraph | **Removed.** Rewritten on Ostrom's own principle 3. No Darity attribution. |
| "We declare in favor of restitution" typology | §5.1.1 | **Replaced** by two published quotations, both checked against the published text (Darity & Mullen 2020, 2–4, as quoted in Darity, Craemer, Berry & Francis 2024, *RSF* 10(2)). |
| Longevity gap, "6–7 years" | §5.5 | **Replaced** by Himmelstein et al. 2022 (published; Darity is a co-author), described by its title only. |
| "The field has not resolved pricing coercion" | Definition 1.10, §5.5 | **Claim about the field removed.** The TA now says only that this volume does not price coercion. |
| "(Darity 2026)" citations, interview entry | his 05-15 copy | Zero in v2.0.1. |

**One judgment call for you.** The scope boundary itself (the framework's main cases turn on not knowing;
coerced labor is a different thing, reached only through its legacy) first came up on the call. I kept it as the
framework's own scope statement, with no attribution and no claim about his field. If you want it held for his
approval too, say so and I will cut it to one sentence. Sen as the grounding for valuation (§5.4) was his reading
suggestion; it cites only Sen's published work and I left it.

**ANSWERED 2026-11-12 (from the author's Chapter 5 decisions, `tools/workstream-handoffs/pull-pass_2026-11/ch5-decision-answers_2026-11-11.md`, decision 1).**
The author kept the coerced-labor paragraph in Chapter 5, added "An empty line is not a zero…", and put the
passage on the list for Darity's review. The TA follows the chapter: **the coercion scope statement stays as
written (TA Definition 1.10 and §5.5) and goes on the same review list.** The TA's wording already matches the
chapter's (named, left Open, not this book's to price). One difference remains for the author: Chapter 5 line 254
says the question "remains open in the field itself"; the TA makes no claim about the field, because that claim
came from the call. The cover note now carries three questions: grounding of the Restitution Bond; carrying past
harm forward; and whether calling the instrument a reparations bond fits his and Mullen's program.

## 6. Owed outside the TA (not my files this session)

- Ch 6 rebuild: Norway row (L174), triangulation language (L137–187), Ostrom claim (L285).
- Ch 9 L202: "Ly & Soman" citation.
- NYRB essay ¶35: Ostrom claim (your decision before submit).
- Cover note to Darity: the two questions (what should ground the Restitution Bond; how past harm is carried
  forward in time).

The gate now flags each of these at MEDIUM so they cannot be forgotten.
