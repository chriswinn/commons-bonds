# Commons Bonds: house style sheet (v1.0.1, 2026-11-12)

**Status:** PROPOSED (internal). For every chapter redraft from 2026-11-17. Read it before drafting; check the draft against it after.
**What it is.** The changes the author has actually made or approved, turned into rules with one real before-and-after each. Nothing here is Claude's taste. Where a pattern is only Claude's observation, it sits in the last table, marked *pending*.
**Updates.** v1.0.1 (2026-11-12) adds the dinner-table rule (now the first rule), the person-and-place rules and the rule on villains, from the author's walk through the Ch 5 decision points. v1.0.0 was built without the author's redline of the Ch 5 rings redraft. When that redline arrives, add its patterns, settle the pending rows, and bump the version.

**Source codes.** **R1** = the author's Ch 1 hand redline (commit `0fca4465`, 2026-06-12) and his rulings on it (`aed2a7b1`). **R5** = his Ch 5 redline notes and directions (`ch5-author-redline-notes_2026-11-09.md`; `ch5-redraft-edits_2026-11-10_session-review.md`). **L** = the engagement lenses he set (`tools/memory/feedback_engagement_lenses.md`). **M** = an earlier ruling recorded in `tools/memory/`.

## The first rule: the dinner-table explanation (author, 2026-11-12)

**Write it the way you would explain it to the author across a dinner table.** That is the tone of the book.

- One step per sentence, in the order a person needs them. Nothing skipped because it seems obvious.
- **If your explanation of a passage is clearer than the passage, the explanation is the passage.** Method for every paragraph: first answer the question "what is this saying?" in plain sentences, as if the author had asked. Then use that.
- Do not compress to sound like prose. Tightness that costs the reader a step is not an improvement.
- Plain words. No jargon, and no idiom or figure of speech tied to one country or culture. The author was trained at IBM to speak in a way that is not regional and is free of jargon, so that people anywhere feel included, and he speaks plainly now by habit; it makes a complicated subject easier to follow.
- A short sentence is fine when it states a fact ("I was one of them."). A short verdict on what was just said comes out ("It launders it." "Instinct is wrong." "It didn't."). He does not talk like that.
- End a paragraph on a plain fact, a person, or the next question.

How this was found: asked to turn three Ch 5 passages into plain prose, Claude compressed them; the author pointed out that Claude's own explanation of what each passage meant was plainer and easier to follow than the "plain prose" version.

| Compressed (do not) | Explained (do) |
|---|---|
| "The law went looking for a moment, and there wasn't one. There was a process." | "The criminal case against the company failed. A prosecutor has to prove one specific act, done knowingly, by one specific person. Libby's harm didn't come from one act. It came from thousands of routine decisions over twenty-seven years, and no single one of them could be proven to be the crime." |
| "Underneath all four objections sits a quieter assumption: that the system did only what any system would have done. It didn't." | "All four objections rest on one belief: that in 2008 the government had no real choice, and any country would have rescued its banks and left households to manage alone. That belief is false. In the 1930s Sweden rescued its banks and its households together." |

## Three things that override everything below

1. **Redraft for pace, pull and flow. Do not match the existing chapters' prose.** The author's verdict on the first draft of the book (2026-11-11): the content is mostly there, the prose is clunky and slow, and nothing pulls the reader to the next sentence, paragraph or chapter. Treat each current chapter as a source of content only. The pace model is the Ch 5 rings redraft (`tools/workstream-handoffs/pull-pass_2026-11/ch5-rings-redraft_2026-11-10.md`). **Protected in every chapter:** quotations, the sayings of the author's father and family, facts and figures, and any passage the author names as his own (in Ch 5, the 2008 account and the lines "did not produce," "cashed out," "left standing," "the bill comes due"). Everything else is rewritten, and the change notes list what was protected. (R5; author 2026-11-10 and 2026-11-11)
2. **Add nothing that isn't in the record.** No invented fact, scene, quotation, feeling or memory. The author added "breathless and panting" to his own childhood; a drafter cannot. The aim is "less flat, not more vivid": fix order and presence, never add color. (R5, M)
3. **Length follows substance.** The map decides what is in the chapter, and the prose takes the room that needs. Long sentences are fine, including long sentences with comma insertions. There is no maximum and no minimum, for a chapter, a section or a sentence. No rhythm model either (don't imitate Ch 1's sentence shapes), and no counts used as targets. The author's reason (2026-11-11): "our worst prose was written trying to stay under a given word count." (R5; author 2026-11-11)

## Who is speaking, and to whom (author, 2026-11-12)

The book is told from one vantage, the author's, from first page to last. He tells every case; he is not written into cases he did not witness, and no reaction or memory of his is invented. Where he has a real connection to a case, he supplies it.

| Word | What it may mean | Not this | Fix |
|---|---|---|---|
| **I** | The author, always. | "The framework" as the subject of sentence after sentence. | Put a person in the subject. |
| **you** | The reader, for what any reader anywhere has: parents, a phone, a home, a decision to sign. | A nationality, a class or a country assigned to the reader: "In your own country…" | Speak from the author: "In 2008…", "the country I live in." |
| **we** | The author and the reader doing the book's work together ("when we add it up"), or a group he belongs to and names ("we who grew up on this bay"). | An unnamed "we" that means Americans: "We paved with the thing that builds reefs." | Name the group, or say who did it. |
| **Countries** | Named: "the United States." | "This country," "your country," "here." | Name it. |

**Sometimes there is a villain.** The book's reading is that cost severance does not need one: decent people answering the incentives in front of them are enough. That is not a claim that there never is one. Sometimes a specific party seeks rent and works to shift a cost onto people who have no seat at the table and no ability to refuse it. Where the record shows that (internal documents, a plea, a judgment, a lobbying record), say so plainly, name the party, and cite the record. Do not soften a documented act into "the system," and do not allege intent the record does not show. (Author, 2026-11-12.)

**Words that are not his.** "Alibi" (for the comfortable reader's sense that this happens elsewhere) is retired. The book's own word is **distance**: in the early cases the reader has it, and then it closes.

## Sentences

| # | Rule | Before | After | Source |
|---|---|---|---|---|
| 1 | **Readable in one pass.** A comma insertion is fine, and so is a long sentence that uses one. What reads as clunky is a run-on that stacks several insertions, so the reader loses the thread before the sentence lands. When that happens, move an insertion to the front or the end, or give it its own sentence. (Clarified by the author 2026-11-11: his mark of 2026-11-09 was about a run-on with several insertions, not a ban on insertions.) | "There is a pattern that, once you have seen it clearly, you cannot stop seeing." | "Once you have seen a pattern, you start noticing it everywhere." | R5 mark 1; author 2026-11-11 |
| 2 | **Lead with the setting when it helps the sentence land.** An example from his own redline, not a rule against the first form. | "He told me, when I was a boy, that even if I grew up to dig ditches…" | "When I was a boy he said that my life was my own… But he did suggest that even if I decided to dig ditches…" | R1 |
| 3 | **Break a comma chain at its turn.** Where a clause turns or trails off into an appositive, end the sentence and start a new one. He did this about ten times in Ch 1. | "…and that difference went somewhere, and it did not go to him." | "…and that difference went somewhere. But it did not go to him." | R1 |
| 4 | **Name the noun.** If the reader has to work out what "it," "he" or "the boy" is, say it. Give each person one name and keep it ("mother (or) wife?"). | "He carried it." · "The boy was too young to know what he had given my father back." | "He carried the full weight of it with his head held high." · "My nephew was too young to understand what gift he had just given to his Pappou." | R1; R5 |
| 5 | **Put the reason in the joint.** Say why a person does the next thing ("so," "because," "but") instead of setting two facts side by side. | "So he asked, casually, whether he might borrow a drill bit…" | "He didn't want to disturb his father's work, so he tried to ask, softly, casually, whether he might borrow a drill bit…" | R1; L6 |
| 6 | **Dashes.** Allowed when they are the clearest choice, at most one pair in a paragraph. Never repair a dash by swapping in commas; restructure or split. | "Take some — leave the rest — let the rest spawn — come back next year." | "Take some, leave the rest to spawn, and come back next year." | M (2026-05-21; amended 2026-11-09) |
| 6a | **Asides in commas must pass the deletion test.** He makes asides all the time when he talks, and he writes them between a pair of commas. Take out everything between the two commas: the sentence that is left has to read and flow well. If it doesn't, the commas are wrong and the sentence is not his voice. A sentence whose two commas are not a pair (an opening clause, then a tail) still fails if a reader can take them as a pair; give the tail its own sentence or join it with "and." (Added 2026-11-14, ahead of the version bump planned for his Ch 1 and Ch 5 redlines.) | "If he pressed for a raise, the company could send him back across that line, out of the country and away from his family." (delete the middle: "If he pressed for a raise out of the country and away from his family.") | His own: "I make comments as asides, all the time, while talking." (delete the middle: "I make comments as asides while talking.") | Author 2026-11-14, Ch 1 redline session |

## Words

| # | Rule | Before | After | Source |
|---|---|---|---|---|
| 7 | **The plain word over the literary one.** | "The lot was empty under the sodium lights" · "I stopped sleeping properly" | "The lot was fairly empty under the parking lot's lights" · "I stopped sleeping well" | R1 |
| 8 | **Say exactly what is true.** Trim an absolute you can't stand behind. Hedge only where accuracy needs it ("usually" was flagged). | "the finest minds alive" · "the only question I have ever really known how to ask" | "the finest minds I have ever had the pleasure of interacting with" · "the most logical questions I could think of" | R1; R5 mark 4 |
| 9 | **A concrete verb over a neutral one,** without implying bad faith. | "The executives have retired." | Author: "taken the cash." Settled as "cashed out." | R5 mark 5 |
| 10 | **Spell out what a term of art means.** | "had to be rigorous enough that the specialists in the field would take it seriously" | "had to be detailed enough for other research teams to independently replicate and verify" | R1 |
| 11 | **No image or signature word twice on a page.** | "standing where it landed" … "still standing in the place where it lands"; "twinkle" twice in Ch 1 | One of each ("same ↑ x2"; twinkle kept only in the Pou scene) | R5 mark 8; R1 ruling |
| 12 | **Contractions and plain register stay.** Never expand his contractions or "correct" plain usage ("a guy that had only been there a year"). Fix only real errors (its/it's, your/you're, stray apostrophes). | A mechanical pass expanded four of his contractions to "cannot / did not / would not." | He reversed all four: "can't / didn't / wouldn't." "Now I can't unsee it." | M (2026-06-11) |
| 13 | **The plain sourced figure over a shocking one that needs qualifying.** | "the figure that travels in the press, fifteen feet of shoreline a year, describes the worst of the exposed western shore; the peer-reviewed average is closer to two feet" | The paper's average, stated flatly. "We have chosen a different path than that throughout this entire book." | M (2026-06-11) |
| 14 | **Quote only what the source says.** Check every quoted or attributed word against the text ("does it say 'wise'?"). Anything not in the source stays out until its source is found. | "…a long conversation about whether an intervention was wise." | "…its standard office-visit rate of $54 for what would certainly have been a long meeting…" | R5 |

## Openings, cases and paragraphs

| # | Rule | Before | After | Source |
|---|---|---|---|---|
| 15 | **Show, then name.** Open on a person or a place. State the pattern after the reader has something to hold. | "There is a pattern that… you cannot stop seeing." (thesis, then a roadmap of seven cases) | "One October afternoon in 2007, the journalist Katy Butler was visiting her parents in Connecticut when her mother asked her for something." | R5 mark 2 |
| 16 | **One scene opens the chapter. Another only where it's earned.** Elsewhere, name who pays in a sentence or two before the mechanism or the numbers. Not every case is a scene. | Baotou: "the people who pay drop out of sight entirely," then a definition of rare earths; villagers arrive three paragraphs later. | Homes beside the waste ponds first; then what the plants refine; then the phone "in your pocket, and in mine." | R5; L8 |
| 17 | **Bridge a distant cost through people before objects.** Parents, children, whoever cares for us at the end, a community. Use an object only when it is the case's real link and is in the reader's life now. | "a quarterly statement in the mailbox" | The mother in the room; the cellphone in a pocket | L8 |
| 18 | **A list has to raise a question and build toward the personal.** An unframed catalogue lands flat. This is not a ban on lists. | "This one shows up in a Montana mining town, on an oil rig… and there is a good chance it is also in the house where you are reading this." | "Imagine one that shows up in seemingly unrelated places: a Montana mining town, … a hospital room where it sits beside your loved ones like an unannounced and uninvited guest." | R5; L5 |
| 19 | **Do it; don't announce it.** Cut the sentence that says what the next sentence will do, and the tail that explains what the last one did. | "It is worth pausing on where that insulation went, because it did not go somewhere else." | "That insulation did not stay in Montana." | R5 (edit 2); M (2026-06-24) |
| 20 | **No process notes in the prose.** No sourcing rules, no announced hedges ("honesty requires a word…"), no "as of this writing," no rebuttal of a claim the reader has never met. Keep the discipline and drop the announcement. | "Butler later published an account of those years, and it should be rendered strictly within what she wrote, with nothing added." · three paragraphs rebutting a $108 trillion figure | Cut. · "One figure does measure the bill honestly." | R5; R1 ruling |
| 21 | **End on the concrete thing, in plain words.** His own endings echo the image or speak plainly; they aren't aphorisms. | "…no one had ever done it better." · "…for everyone earning beneath it, which is to say almost everyone." | "…no one had ever dug a better ditch." · "…for everyone else. Anyway, sure, the house was beautiful." | R1 |
| 22 | **Other people's stories aren't his to tell.** One plain sentence closes the door. Living people stay unnamed. Don't dramatize the boundary. | "I will only tell you my side of that, because the rest is not mine to tell, and I am going to hold that boundary as carefully as I held the boundary around the weights of slavery…" | "But that is not my story to tell." | R1 |
| 23 | **His money appears as a rank, never a dollar figure.** | "…touched around [a dollar figure]." | "…put me in the top one to two percent of household incomes in the United States for those years." | R1 |
| 24 | **Credit a source in a sentence where its idea is used.** Lineage tours shrink or move. | Two paragraphs touring Pettit, Skinner and Hartwick | One paragraph; both titles, both years and Hartwick 1977 still cited | R5 (approved 2026-11-11) |
| 25 | **Retired frames.** "Scatter" as a word or a structure. | "…a deliberately scattered set of cases, and the scatter is the method." | Rings that close in on the reader | R5 mark 9 |

## Pending: Claude's observations, not yet the author's rulings

Apply these lightly in redrafts and list each use in the change notes, so the author can rule at the redline.

| # | Observation | Example | Provisional handling |
|---|---|---|---|
| P1 | *Settled 2026-11-12: the closing-line habit is not the author's voice. See "The first rule" above.* | | |
| P2 | **Stacked objections.** Several "state it, concede, turn" paragraphs back to back. (Part 4; decision point 7.) | Four objections on 2008, then two on Social Security | Answer the strongest in full. Fold or cut the rest, and say which in the change notes. |
| P3 | **Lineage in the middle of an argument** is the likeliest place a reader stops. (Critic read item 1; partly settled by rule 24.) | Five traditions credited inside "Restitution and foreclosure" | Credit at point of use; propose any move to another chapter in the map, not in the draft. |

## The reader's test

At the end of each paragraph, ask whether you want to know what comes next. Where the answer is no, that is usually where the problem is. (L)

## Where the checks live

`tools/scripts/check-prose-clarity.py` lists interrupted clauses, comma-stacked sentences and long sentences. Use all of its output to find tangles after drafting. None of it is a target, and a flagged sentence that reads cleanly in one pass stays as it is. `tools/scripts/check-corpus-invariants.sh` runs the figure and scaffolding gates.
