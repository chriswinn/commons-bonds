# Ch 5 rings redraft (Session 2): what changed from Out and back

Internal. **Base:** `tools/workstream-handoffs/ch5-rebuild-2026-10/round-3_2026-11-09/ch5-out-and-back_2026-11-09.md`.
**Draft:** `ch5-rings-redraft_2026-11-10.md` (11,620 words; base 12,594; no length target). **Map:**
`question-map.md`. **Critic read:** `critic-read.md`. Nothing in `round-3_2026-11-09/` or
`manuscript/chapters/` was edited.

**Superseded first attempt:** `ch5-rings_2026-11-10.md` (commit `2490a9c`) restructured the chapter into
rings but kept about 70 percent of the base's sentences word for word, including prose the author had
already called clunky and slow. The author stopped it. This redraft writes every section fresh. Word for
word from the base, it keeps only the author's own 2008 account (four paragraphs) and the author's lines
("did not produce," "cashed out," "left standing," "the bill comes due"). Outside those, about 17 percent of
words still match the base, mostly short factual sentences that state a figure, a title or a date.

Lens numbers refer to `tools/memory/feedback_engagement_lenses.md` (1 question first · 2 participant ·
3 strongest last · 4 people before abstraction · 5 lists build · 6 reasoning in the joints · 7 pull, then
polish · 8 one scene, earned scenes, relationship bridges).

## Structural moves

| # | Move | Serves |
|---|---|---|
| S1 | **Rings replace scale:** family → community (fundraising, Libby, the Gulf and Mexico, Valdez) → country (2008, Social Security) → world (Baotou) → the pocket → the pattern named → one kind of thing → who shaped the system → restitution and foreclosure → the family, again. | Pace; lens 8 |
| S2 | **Butler's room opens the chapter, told whole in her words.** It ends on a question, not a thesis: "So how did it get there? And is medicine the only place it lands?" | Lens 1, 4, 8 |
| S3 | **The author's pattern lines move to "The pattern, named,"** after the pocket. "Severed cost" is handed over there, with one example from each ring. | Pace (show, then name) |
| S4 | **The pocket is its own section and the only object bridge** ("your pocket, and the one in mine"). It answers the opening puzzle: the same arrangement runs through every ring, and through us. | Lens 8; climax |
| S5 | **Each case opens on people:** the asking family, the miners' children, the fishing families, the villages near Baotou. | Lens 4, 8 |
| S6 | **"Severance" is held back until it's named.** Before "The pattern, named," the prose says "cut loose." The only exception is the quoted $108T claim ("the largest cost severance in human history"). | Pace item 1 |
| S7 | **No section ends on a pointer to a later chapter.** Every pointer moved inside its paragraph (Ch 6 Valdez, Ch 9 Dodd-Frank and Sweden, Ch 7 covers, Christophers, Ch 9 Public Choice, Ch 6/9 restitution). | Lens 3 |
| S8 | **Section heads renamed where they announced:** "The same object, named honestly" became "One kind of thing." "Back to one body" became "The family, again." | Process notes out |

## Line changes, by section (all prose rewritten; the main moves)

| Section | What changed | Serves |
|---|---|---|
| Family | Session 1's Butler opening with the §6 facts; Gawande rewritten ("Decent people respond sensibly… and the incentives do the rest"); a two-sentence naming, then the question. Gone: the sourcing sentence, "wise," "nearly half," the malpractice claim. | Butler file; lens 1, 6 |
| Community: fundraising | Opens on the family asking; the outcomes are their own short paragraph as the punch; one sentence of countries and one of citations. | Lens 3, 4 |
| Community: Libby | Opens on the dust coming home; the mine, the ore, the dead, the ratio; then the law looking for a moment; Pistor; ends on the town. No attic. | Lens 3, 4, 8 |
| Community: the Gulf | Opens on the fishing families; three ways the cost landed; what BP paid and what it didn't; what never had a price. | Lens 4 |
| Community: Mexico | **New facts from the ledger:** the $25.5M settlement (Feb 2018; $15.3M to government costs, $10.2M to programs; nothing for the communities; BP released from damage in Mexican waters); 22 studies funded, withheld, 20 released after the deal, 2 still classified; about 25,000 fishermen's US class action (2015). Ends: "They decided whether a cost was counted at all." The funding-cut claim was **left out**: it rests on one researcher's account. | Author direction; Pistor point made concrete |
| Country: 2008 | "In your own country, the alibi fails." Author's account verbatim. Mishel–Bivens and Hacker bridge to the 401(k). The four objections each open in one sentence and end on their strongest line. Sweden closes on "The road it took was chosen, not forced." | Lens 3, 6 |
| Country: Social Security | Opens on the compact between parents and children. The $108T rejection, the honest build, the $22.6T kept apart, 1972, and the two objections are rewritten for joints and endings. Announced hedges are gone. | Lens 6, 8 |
| World | Villages first; then what the plants refine and where the ore comes from; the evidence paragraph states its limits without announcing them. | Lens 4; process notes out |
| Pocket | "Here it needs only to keep the cost out of sight…" Scoped to the case for Ch 7/10 consistency, under the license the author gave. | Consistency |
| The pattern, named | The author's lines; the handover of "severed cost"; the covers as a short build; the roll call as fragments that build; Kapp. New close: "Kapp and those who followed him showed who is left holding the bill. What this book adds is the amount written on it, posted as a reserve before the bill comes due." | Pace; author's rewrite request |
| One kind of thing | Sandel, the zero, Polanyi, Fraser and Christophers, then Pistor's test, with interrupting clauses removed. | Lens 6 |
| Who shaped | Opens on the chute line; the roster paragraphs tightened; the invitation to AEI and Cato ends the section. | Kickoff |
| Restitution | Opens on the question; the two faces, the instruments, "Why bonds?", the names, the lineage and the black-lung gap are all rewritten. Ends on "an answer in any political weather." | Lens 3, 6 |
| Close | Q3 return; the unborn as family ("farther away than Baotou, in time rather than space"); ends on the bond question asked as a question. | R outline |

## Ledger and gate (same commit)

- `manuscript/ledgers/_CANONICAL_FIGURE_LEDGER.md`: new section "Ch 5 case figures (Butler; BP–Mexico)."
- `tools/quality-gates/regressed-patterns.yaml`: three MEDIUM patterns ("nearly half of which went/flowed to
  the company," the Butler malpractice sentence, "comparable lengths of damaged coastline"). All three fire
  on the current `Chapter__5` and none on the redraft. MEDIUM, so they don't block commits. They were
  first placed below a column-0 comment the parser treats as end-of-list and never loaded; they were moved
  above it.
- `manuscript/ledgers/_RESEARCH-RESULTS-LEDGER_2026-06-04.md:135`: the coastline framing is now
  attributed to an earlier Claude session, not the author.

## Checks

- **Figures vs base:** new = Butler corrections + Mexico ledger entries ($25.5M, $15.3M, $10.2M, 22/20/2
  studies, 25,000, 2015, 2018). "About $25 million" is now "$25.5 million." Every other base figure is
  present.
- **Fact list:** all 46 rows of the round-3 fact-check table are present. README's "35" is a count, not a
  list.
- **check-prose-clarity.py:** HIGH 0; **interrupted 0; comma-stacked 0**; em-dashes 0. One false positive
  was reworded anyway ("hasn't settled that, and…").
- **check-corpus-invariants.sh:** only the three known items.
- **Quotations:** Q1–Q4, 39 words.

## What this pass taught about drafting for pull

1. **Restructuring is not redrafting.** Moving clunky paragraphs into a better order left them clunky.
   Pull lives in the sentences' joints and endings as well as in the order. Both have to be rewritten.
2. **A figures rule protects numbers, not prose.** "Figures identical to the base" was read as "keep the
   base's sentences." Next time, a brief should say outright which prose is protected (here: the author's
   2008 account and four lines) and that everything else is rewritten.
3. **Write each paragraph toward its last line.** The quickest fixes came from deciding the last sentence
   first ("There was a process." "It is not a wall rebuilt." "They decided whether a cost was counted at
   all.") and cutting whatever came after it.
4. **Hedges cluster at joints and before numbers.** Nearly every announced hedge sat where the writer was
   nervous about the next step. State the narrow claim and move on.
5. **Next pace problem: the back half.** Rings put the climax at about 57 percent, and the argument sections
   follow it. Moving the lineage paragraphs out is the likely fix (critic read, item 1).

## Addendum (2026-11-10, later): the Darity passage, revised on the author's direction

The author's stance: defer the method to Darity, show that the framework's two-way pricing fits it, and say
plainly that it isn't the author's place, as someone who presents as a white man, to put a dollar figure on
what is owed for slavery. Grounded in MI-1 and MI-2 from the 2026-05-13 call (Option 1: the Restitution
Bond carries out the restitution part of Darity–Mullen redress) and in Darity's published wording, now
quoted (see `research/citations/darity-mullen-arc-quotes_2026-11-10.md`).

- **Replaced:** "older and broader term" and "Calling the instrument the Reparations Bond would narrow it…".
  Both put Restitution beside reparations as the bigger idea, which is the flattening Darity corrected. The
  replacement places the bond inside their ARC, quoting the definition and "Redress is the act of
  restitution…".
- **Cut:** "So the framework joins the reparations tradition instead of rebranding it." Also the old ARC
  paragraph, now folded into the first paragraph.
- **New paragraph, after the lineage:** "The method belongs to them as well…", with the author's first-person
  line on where he stands and the fit ("on their terms").
- **Coerced labor:** now "this book does not presume to close it" and "belongs to the people already
  carrying that question forward."
- **Gate:** "Reparations Bond" no longer appears, so the regressed-term HIGH item is cleared. Only the two
  MEDIUM known items remain.
