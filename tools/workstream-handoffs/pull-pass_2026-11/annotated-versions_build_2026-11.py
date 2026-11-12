#!/usr/bin/env python3
"""Annotated print copies of the Ch 1 and Ch 5 versions (judging session, 2026-11-12).

Builds one HTML file per version: the text exactly as it stands, paragraph numbers, and
margin notes (SECTION verdict / BEST / ISSUE / QUESTION for the big edit). Nothing is edited.
Usage:  python3 annotated-versions_build_2026-11.py OUTDIR   (run from the repo root)
Then print each HTML to PDF with page numbers (Chromium; see the session's pdf step).
The notes are one reader's opinion for the author. PDFs are not committed.
"""
import re, html, sys
P = 'tools/workstream-handoffs/pull-pass_2026-11/'
S, B, I, Q = 'SECTION', 'BEST', 'ISSUE', 'QUESTION'

CH1A = [
("The first thing he did in any new city", [(S, "Section 1, the colleague. Your version is the best of the three here."), (B, "The opening line. All three versions keep it.")]),
("A rooftop, a tower, a hill on the edge", [(I, "One paragraph of about 330 words. The pace draft breaks it after “which it flowed past,” and the break helps."), (B, "The greetings, ending on “one word at a time.” The best thing in the section.")]),
("He made about half of what I made.", [(B, "The turn of the section. It lands in every version.")]),
("The most credentialed person in the building made", [(I, "I had to reread the sentence that ends “the other end of the cord.” The dinner-table draft says it plainly: “If the company decided it no longer wanted him, he could be sent out of the country, away from all of it.”"), (I, "“the country”: the style sheet says name it (the United States).")]),
("I had no word for what I was looking at.", [(B, "“a man who could not leave.” The line the section exists for.")]),
("What I felt standing near him", [(B, "“sat in my chest like a stone” is paid off later, in the three-generations paragraph. Keep.")]),
("I would learn to quantify it.", [(S, "Section 2, the lease. Yours is the best version. The other two smooth out the short fragments that give it speed."), (I, "“quantify”: “put a number on it” (dinner-table) is plainer. Small.")]),
("The first day I drove it", [(B, "The fragments (“Not the driving alone. The drive to the train, the parking…”) move fast. Both other drafts fill them in.")]),
("Run the arithmetic with me", [(B, "Best paragraph in the section. “going nowhere, generating nothing, becoming no one” is lost in the dinner-table draft.")]),
("I had saved three hundred dollars", [(B, "“The apartment was cheaper. It was also the most expensive place I have ever lived.” The chapter's idea in two sentences.")]),
("Seeing became a method.", [(I, "“Seeing became a method” arrives abruptly; slight reread. But the dinner-table fix (“It became a habit”) changes your meaning."), (Q, "This paragraph and the one before it make nearly the same point. Could one be shorter?")]),
("And then I saw it everywhere.", [(S, "Section 3. Yours is best. It is the most abstract section, and the shortest.")]),
("I saw it in the watermen", [(I, "The first sentence runs past 80 words and I lost the thread at “costs that settle.” Both other drafts split it well."), (B, "“They deserve a chapter, not a sentence.” The pace draft cut this.")]),
("I saw it in the worker, any worker", [(Q, "The only paragraph in the chapter with no person in it. Fold it into the next, or cut?")]),
("And I saw it in the deepest version", [(B, "Careful and necessary. “A commute and a stolen life do not belong on the same line.” Darity will read this paragraph closely; it should stay exactly yours.")]),
("Once the lens had formed", [(B, "The turn to the reader works, and “Now I can't unsee it” is your line."), (I, "“the lens” has not been set up as a word before this. Small.")]),
("I had been handed the feeling, it turns out", [(S, "Section 4, your family. Yours is best. The dinner-table draft is almost word for word the same; the pace draft rewrote most of your June redline here.")]),
("The man my own son would never meet", [(I, "Reread: your son has not been mentioned yet. Dinner-table: “My grandfather was a man my own son would never meet.”")]),
("Let me tell you what it means", [(I, "This sentence announces what the next paragraph does. The pace draft moves the “quiet center” thought to after the wind tunnel, which reads better.")]),
("A wind tunnel tells the truth", [(B, "One of the best paragraphs in the chapter. “Build it true enough that the truth can be seen while there is still time to act on it.”")]),
("I know the not-thinking-much-of-it", [(B, "The scene, in your words.")]),
("A week or two later my father came by", [(B, "“the way you mention the weather.”"), (I, "The last five sentences turn from scene to argument inside one paragraph. I had to reread “the fame and the fortune of the enterprise he served went, as it always does in the patient ordinary machinery of salaried invention, to the enterprise.” The pace draft starts a new paragraph at “That was the man”; the dinner-table sentence is plainer.")]),
("He taught it to me almost without", [(B, "The ditch. “no one had ever dug a better ditch.”")]),
("I remember an afternoon.", [(B, "The best scene in the chapter. The dinner-table draft did not touch a word.")]),
("There were the mornings he drove me", [(B, "Short, and it lands.")]),
("He had a way of holding a room", [(I, "“a person with a reputation for only speaking when they have something worth hearing begins to speak…” is a long subject; slight reread."), (Q, "Third anecdote about your father in a row. All three are good. Does the chapter need all three?")]),
("So three generations of men", [(B, "Ties the stone in the chest back to the colleague."), (I, "The last sentence repeats the section's first sentence. One of them can go.")]),
("There was one more handing-down", [(B, "The Pou story."), (I, "The last three sentences explain the gift three times (I did not know; I would not hear; he was too young). It could end one sentence sooner.")]),
("I started my own working life", [(S, "Section 5, the work. Your words, but take the pace draft's paragraph breaks. This is the longest section and the slowest.")]),
("That sounds simple and it was deceptively hard.", [(B, "The look on the child's face."), (I, "“And it needed enough information that the specialists…” puts three requirements in one sentence; slight reread. The pace draft gives each its own sentence.")]),
("The project I had been hired to look at", [(Q, "The aside about rounding the team down stops the story for four sentences. It is in your voice, and it sets up the “smallest honest number.” Does it belong here, or later?")]),
("What made me good at it", [(B, "Ties back to the drill bits.")]),
("Years later, a CEO by then", [(I, "The weakest passage for pace: about 330 words with no break, and the second sentence needed a reread. The pace draft breaks at “I asked each person” and at “The machine turned out.”"), (B, "“the little red light on that one had stopped blinking.” And the ending: “they declined.”")]),
("I tell you this not to praise the skill", [(B, "The hours, the unopened paychecks, shaving your head on mute. Specific and strong. “Sleep took me. I had stopped choosing it.” Keep that order.")]),
("That pattern, the one I learned at the NIH", [(I, "Two long insertions come before the verb. Both other drafts split it; either split works.")]),
("By the time I was deep into my best years", [(S, "Section 6, the plane and the hospital. Yours is best, and it is the strongest section in the chapter."), (Q, "This paragraph mixes story with argument (the free-market economist). The reader also does not yet know what “the leave” was for. Is that delay intended?")]),
("And I thought of him.", [(B, "The return to the rooftop. The best structural move in the chapter.")]),
("He had come early, and he was very small", [(B, "The best paragraph in the chapter."), (I, "One run-on only: “whichever I chose at the start held the same for the whole sitting.” Leave the rest alone.")]),
("The marriage did not make it through", [(B, "“But that is not my story to tell.”")]),
("I had bought a beautiful house", [(B, "Ties the house back to the lease. “keep feeding” is your image; the dinner-table draft flattens it to “keep paying for.”")]),
("And here is the harder number", [(B, "“Anyway, sure, the house was beautiful.”"), (I, "“Not at the peak. Not at the absolute top of what I could earn.” makes the point a third time.")]),
("The house is not the thing I miss.", [(B, "Plain, and enough.")]),
("What the years finally gave me", [(S, "The close. Yours, with one fix (next note).")]),
("The work of naming what hides behind a mask", [(I, "The weakest lines for a new reader: “The framework extends the move.” Neither “the framework” nor “the move” has been introduced. Dinner-table: “This book takes the same move and applies it to the pricing of commons.” Darity will read this closely.")]),
("The son I once held", [(B, "Four plain facts. The strongest lines in the close.")]),
("This is the ledger.", [(B, "The ending.")]),
]

CH1B = [
("The first thing he did in any new city", [(S, "Section 1. Smooth, but less yours than your own version.")]),
("A rooftop, a tower, a hill at the edge", [(B, "The paragraph break after “flowed past.” Worth taking."), (I, "“between drags on his cigarette… a little wistful” rewrites your “between each cigarette puff he would look off… wistfully.”")]),
("He had done this in more countries", [(B, "Reads cleanly as its own paragraph.")]),
("There was nothing he could do about it", [(I, "Cuts your repeat (“The most credentialed person in the building made about half of what the least credentialed person… made”). The repeat was the emphasis."), (I, "“That difference went somewhere, but it did not go to him” undoes the break you made by hand (“But it did not go to him.”).")]),
("None of us had a word for it", [(B, "“The language was a lie. No one was lying, but the language had no room in it for a man who could not leave.” Clear.")]),
("What I felt standing near him", [(B, "Putting the list after “settled down onto him and stayed:” is easier to follow than your order.")]),
("What was being taken from him", [(I, "ADDED. This question, and “It would take me years to find the answer,” are not in your chapter. They replace “I would learn to quantify it.”")]),
("It had to do with a lease.", [(S, "Section 2. Tighter than yours, and it loses your rhythm.")]),
("I did not.", [(I, "Shortens your repeated line (“I did not understand what I was agreeing to.”).")]),
("The first time I drove it", [(I, "Drops a sentence from your hand redline: “Two and a half hours in the morning and two and a half hours at night…”")]),
("Run the arithmetic with me", [(I, "Merges your four short sentences into one with a colon. “generating nothing” became “making nothing.”")]),
("Without my deciding it, seeing became", [(B, "Clearer order than “Seeing became a method.” as an opener.")]),
("And then I saw it everywhere.", [(S, "Section 3. The split of the watermen sentence is good; the rest is weaker than yours.")]),
("I saw it in the watermen", [(B, "The long sentence is split in the right places."), (I, "Cuts “They deserve a chapter, not a sentence.”")]),
("And I saw it in the deepest version", [(I, "Rewrites a paragraph that should stay exactly as you wrote it (“What was done there” for “The wrongness there”; “Naming a shared shape…”).")]),
("Once the lens had formed", [(I, "Moves “Now I can't unsee it” to the very end, as a closing line. That is the short-closer habit you said is not yours.")]),
("I had been handed the feeling long before", [(S, "Section 4. The pace draft's weakest section: it rewrites most of your June hand redline.")]),
("My son would never meet my grandfather.", [(B, "A clearer opener than yours.")]),
("He built faithful models so the truth", [(B, "The “quiet center of this book” thought comes after the wind tunnel here. Better order than yours.")]),
("I know how little he thought of it", [(I, "Three of your redlined sentences about the workshop are folded into one.")]),
("That was the man.", [(B, "Starting a new paragraph here is right: the scene ends, the argument begins.")]),
("One weekend afternoon he gave my sister", [(I, "Your chore story, reordered and re-punctuated. Yours is better.")]),
("He held a room in a way", [(B, "“someone known for speaking only when it matters” is easier than your long subject.")]),
("So three generations of men", [(I, "Cuts “I had been given the feeling long before I was given the words.”")]),
("There was one more handing-down", [(I, "Rewrites four of your redlined sentences (“the sound of his own father's nickname”).")]),
("I started my own working life", [(S, "Section 5. The pace draft's best section. Take its paragraph breaks.")]),
("It sounds simple, and it was deceptively hard.", [(B, "The three requirements get a sentence each. Clearer than yours."), (I, "“One look, and I stopped sleeping well for years.” reorders your two sentences.")]),
("The project I had been hired to look at", [(B, "Your long last sentence is split into three.")]),
("Years later, by then a CEO", [(B, "Breaks here, at “I asked everyone,” and at “The machine turned out.” Take all three.")]),
("I asked everyone the most logical questions", [(I, "“A guy who” corrects your “A guy that.” You ruled that out in June."), (Q, "Your two questions now carry question marks. Your call.")]),
("I learned that pattern at the NIH", [(B, "Clearer than your one long sentence.")]),
("By the time I was deep into my best years", [(S, "Section 6. Close to yours, with small rewrites that do not help.")]),
("And I thought of him: my colleague", [(I, "Joins, with a colon, a fragment you wrote by hand.")]),
("He had come early, and he was very small.", [(I, "The nurses' request is turned into a direct question. Your indirect version is the one you wrote."), (B, "The breath-counting sentence is split, and it is clearer.")]),
("The marriage did not make it through that period, but", [(I, "Joins two sentences you separated by hand.")]),
("The apartment and the house both looked", [(I, "ADDED. You did not write this reflection. Leave it out.")]),
("The work of naming what hides behind a mask", [(B, "“It is Dunbar's mask and Du Bois's veil” is clearer than yours."), (I, "Still says “The framework.”")]),
]

CH1C = [
("The first thing he did in any new city", [(S, "Section 1. Nearly your version. Two things worth taking (noted below).")]),
("It might be a rooftop", [(I, "“It might be” adds nothing. The long paragraph is still unbroken.")]),
("I was not. I was a junior developer, about two years into the work. I had", [(I, "Three short sentences where you had one. Flatter.")]),
("The most credentialed person in the building made", [(B, "The plain visa sentence: “If the company decided it no longer wanted him, he could be sent out of the country, away from all of it.” Take it. Also “the United States.”")]),
("I had no word for what I was looking at.", [(B, "“That language was a lie. Nobody was lying. It was a lie because it had no room in it for a man who could not leave.”")]),
("What I felt standing near him", [(B, "The list after “stayed:” is easier to follow.")]),
("I would learn to put a number on it.", [(S, "Section 2. The dinner-table draft's weakest section: filling in your fragments flattens it.")]),
("When I moved to the region", [(I, "“It had more room…” “It was late at night and the roads were empty…” Every step is there, and the speed is gone.")]),
("The first day I made the trip", [(I, "“That was not… It was… It was…” Alters a sentence from your hand redline.")]),
("Run the arithmetic with me", [(I, "Loses “going nowhere, generating nothing, becoming no one.” “nothing to show for” is an idiom.")]),
("Nobody did this to me.", [(I, "“could not stop noticing it” replaces “could not unsee the shape of it,” though you use “unsee” again later.")]),
("It became a habit.", [(I, "Meaning shift: you wrote “Seeing became a method.”")]),
("And then I saw it everywhere.", [(S, "Section 3. About even with yours.")]),
("I saw it in the watermen", [(B, "The long sentence is split well.")]),
("And I saw it in the deepest version", [(B, "Essentially yours. Only the opening is split.")]),
("I had been handed the feeling, it turns out", [(S, "Section 4. The same as yours except four sentences.")]),
("My grandfather was a man my own son", [(B, "Take this opener.")]),
("A wind tunnel tells you the truth", [(I, "Small smoothing; “a craft that lives nowhere yet” is lost.")]),
("A week or two later my father came by", [(B, "“The fame and the fortune that came from it went to the enterprise he worked for, which is where they always go when an inventor works on a salary.” Take it.")]),
("My father carried it forward.", [(I, "“He never passed on anything about the subject of his work, because I never heard any of it.” Clumsier than yours.")]),
("So three generations of men", [(I, "Meaning shift: “I recognized his situation on sight” for “I recognized him on sight.” Also “bone-sense” became “the sense of it in my bones.”")]),
("I started my own working life", [(S, "Section 5. Your words. Only one new break in the cable-station story.")]),
("Years later, a CEO by then", [(I, "Still one long paragraph. The split of the second sentence is good; it needs the pace draft's two other breaks.")]),
("I am not telling you this to praise", [(I, "“because the two came together” is weaker than “the same thing seen from two sides.”"), (I, "“By then I was not choosing when to sleep. Sleep took me.” reverses your order. Yours ends stronger.")]),
("I learned that pattern at the NIH", [(B, "A clear split of your long sentence."), (Q, "A marker follows this paragraph in the file: THE ROAD, your section, to be written by you.")]),
("By the time I was deep into my best years", [(S, "Section 6. The same as yours except three splits.")]),
("And I thought of him. I thought of the colleague", [(I, "Changes a fragment you wrote by hand.")]),
("He had come early, and he was very small", [(B, "Untouched.")]),
("I had bought a beautiful house", [(I, "“keep paying for” replaces your “keep feeding.”")]),
("The work of naming what hides behind a mask", [(B, "“This book takes the same move and applies it to the pricing of commons.” Take it.")]),
]

CH5B = [
("One October afternoon in 2007", [(S, "The family. Strong in both versions. The first two paragraphs here are tighter than the dinner-table draft and just as clear."), (B, "Opens on a person asking for something. The best opening this chapter has had.")]),
("His decline had begun", [(B, "Moves fast, and ends on her own words.")]),
("Nothing in the system had pushed", [(I, "Reread: “pushed the other way.” Other than what? The dinner-table opener is clearer."), (B, "“He was not consulted. He was notified by fax.”")]),
("This was not one family", [(B, "The numbers are attached to people (“a doctor like theirs”).")]),
("The surgeon and writer Atul Gawande", [(I, "“choose extraction over compassion” is the book's word, not a reader's. Dinner-table: “money over compassion.”")]),
("The device maker, the hospital", [(B, "Ends on two questions that carry the reader into the next section.")]),
("In Butler's family the bill came due", [(S, "The community. Even on fundraising. The dinner-table draft is clearer on Libby and the Gulf.")]),
("The platform's chief executive", [(I, "The last sentence tacks the citation on (“and the analysis by Saleh and colleagues… is one of them”).")]),
("The asking also works worst", [(I, "The last sentence is compressed. The dinner-table draft says why.")]),
("In some communities the cost reaches", [(B, "Libby opens on the miners and their kitchens before the company or the numbers.")]),
("That insulation did not stay", [(B, "Brings the case into the reader's own house."), (I, "“This case is not at arm's length. It is the distance between your chair and your ceiling.” A shaped closing line, and “arm's length” is an idiom.")]),
("The ore also carried", [(B, "“The mining went on.” A plain fact, and it is enough.")]),
("Hundreds of Libby residents", [(B, "Oxygen tanks beside the bread.")]),
("Over its life the mine", [(I, "Reread: “Built from disclosed parts, the order of magnitude is plain.”")]),
("The acquittal doesn't mean", [(Q, "The dinner-table draft carries the fuller explanation you approved (“A prosecutor has to prove one specific act…”).")]),
("The legal scholar Katharina Pistor explains", [(I, "Reread twice: “dissolve the responsible actor into a process”; “protects the cut… price what the law cuts loose.”"), (Q, "This is the first place the chapter stops for theory. Is Pistor needed here and again in “One kind of thing”?")]),
("Grace's shareholders and executives", [(B, "Two plain sentences, on people.")]),
("BP had drawn enormous value", [(I, "“the cost went looking for somewhere to land” is shaped writing. The dinner-table draft numbers the three ways.")]),
("Here, unusually, the polluter paid", [(B, "Clear, and fair to BP.")]),
("Some of what the coast lost", [(I, "“which is exactly why it could be lost for free.” A verdict closer.")]),
("The oil did not stop at the border.", [(B, "Mexico: new, concrete, and it makes the point without help. (Sources still to be verified.)")]),
("So the families went to court", [(I, "Lists the legal tools without saying what they are. “Pistor's modules are not abstract here.”")]),
("Twenty years earlier the same story", [(Q, "A third spill-and-courts case in a row, and it sends the reader to Chapter 6. Shrink or cut in the big edit?"), (I, "“the season has stayed gone.”")]),
("In 2008 the distance closed.", [(S, "The country. The longest section (about 3,700 words): your account, four objections, Sweden, then Social Security. The dinner-table draft is clearer throughout."), (Q, "Should Social Security be its own section? It starts a new subject two-thirds of the way in.")]),
("I was doing well at the time.", [(B, "Your account, here and the next four paragraphs. The best pages in the chapter. Identical in both versions.")]),
("I'm not telling this because", [(I, "Your own passage, and one reread in it: the sentence setting “I did everything I was told…” against “I was already struggling.” Also “This is the case in the chapter where…” talks about the chapter.")]),
("The 401(k) was one piece", [(I, "Two ideas and three sources in one paragraph; “the widening gap between those two curves.”")]),
("What was said less loudly", [(B, "“whose freedom it was.”")]),
("Leverage explains why.", [(B, "The two homeowners."), (I, "“The second has lost the whole down payment” skips the step that explains it. The dinner-table draft supplies it.")]),
("Now look at what the system", [(B, "The contrast in speed and size, in three numbers.")]),
("That contrast invites indignation", [(I, "A verdict line. Not how you talk.")]),
("Many of the borrowers who defaulted", [(I, "The biggest one-pass problem in this version. This paragraph and the next three each open by stating an objection as if it were the book's own claim. Nothing tells the reader it is an objection until “All four objections,” four paragraphs on.")]),
("The crisis was global", [(I, "Same problem. And “Its origin only matters more.”")]),
("The public got its money back.", [(I, "Same problem.")]),
("Reform closed the gap.", [(I, "Same problem. And “It is not a wall rebuilt.”")]),
("All four objections rest on one belief", [(B, "Your approved wording."), (Q, "Four objections in a row is a long stop. Answer the strongest in full and fold the rest?")]),
("Sweden faced banking pressure", [(I, "Dense: gold standard, krona, Saltsjöbaden, Kindleberger and Eichengreen in one paragraph.")]),
("The United States holds one more compact", [(B, "The bridge through parents and children.")]),
("In 1972 Congress passed", [(B, "The clearest paragraph in the Social Security passage.")]),
("The record is strong enough", [(I, "“strong enough without embellishment” is a note about method, in the prose.")]),
("It didn't have to be built this way.", [(I, "“selected, not fated.”")]),
("Two objections deserve a hearing.", [(I, "“The two pass each other.”"), (Q, "Two more objections, after four on 2008.")]),
("The second says the gap is tractable.", [(I, "“tractable.” And “A gap that can be closed is still a cost cut loose.”")]),
("In the villages near Baotou", [(S, "The world. Short, and it moves. The two versions are close; this one is quicker."), (B, "People first, in two sentences.")]),
("Here the cost is cut loose in every direction.", [(I, "Abstract. The dinner-table draft separates time, place and power.")]),
("The evidence from this far away", [(B, "Honest about what is not known, and about the $100 billion figure.")]),
("Rare earths also mark a limit.", [(Q, "Points to “a parameter in an appendix” the reader has not seen. Does this paragraph belong in this chapter?")]),
("Now think of the phone in your pocket", [(S, "In your pocket, and in mine. The strongest turn in the chapter's design.")]),
("That doesn't make you or me a villain", [(I, "“A saint could stand at the bright end of this arrangement.” “does that for a living.” Figures of speech.")]),
("With the phone in your hand", [(B, "The look back through the rings. The best structural paragraph in the chapter."), (Q, "Everything after this explains or names. How much of it does this chapter need?")]),
("Lay the cases side by side", [(S, "The pattern, named. Even with the dinner-table draft. Good pace.")]),
("The cost comes due later.", [(B, "Your lines: “cashed out,” “left standing,” “the bill comes due.”")]),
("What you have been watching in every ring", [(B, "The term arrives after the cases. The right order.")]),
("The word has a second meaning", [(Q, "Answers a worry few readers will have. Cut?")]),
("How does the party that gains slip", [(I, "Six covers in one fast paragraph, and the full set is deferred to Chapter 7.")]),
("Then call the roll", [(I, "“call the roll” is an idiom."), (B, "The list is of people.")]),
("None of this is a new insight.", [(B, "Credit given generously, and briefly.")]),
("Kapp and those who followed him", [(B, "The clearest statement anywhere of what the book adds.")]),
("Ask what each of these cases drew on.", [(S, "One kind of thing. The pull drops here in both versions. About 1,300 words: a definition, Sandel, Polanyi, Fraser, Christophers, Pistor.")]),
("Pricing any of these invites", [(I, "“launders the priceless into a transaction.”")]),
("The answer turns on what the alternative", [(B, "“These things already have a number, and the number is zero.” The best argument in the section.")]),
("The framework refuses that zero.", [(B, "Pricing to sell against pricing to reserve.")]),
("That refusal has an ancestor.", [(Q, "Lineage for three paragraphs (Polanyi, then Fraser twice). Credit in a sentence where the idea is used?")]),
("The reef, the community's knowledge", [(I, "“Chapter 2 left a thread loose…” A reader of this chapter as a sample has not read Chapter 2.")]),
("One caution answers", [(Q, "This paragraph and the next raise Christophers and then defer him to a later chapter.")]),
("In *The Code of Capital* Pistor names", [(B, "A concrete answer: the bond cannot be traded. Technical, but it earns its place.")]),
("The ledger shows where the cost landed", [(S, "Who shaped the system? The four paragraphs of cases are clear. The framing around them is defensive.")]),
("A rigorous toolkit for that question", [(I, "“it would be pride not to use it.”")]),
("At Libby, internal company documents", [(B, "Here and the next three paragraphs: named parties and named records. This is the “sometimes there is a villain” rule done right.")]),
("The use of this toolkit is easy to misread.", [(Q, "A paragraph defending the use of a tool. Shorten to two sentences?")]),
("Chapter 9 develops this pairing", [(Q, "Names four institutions as the intended audience. It reads as a note about readers, not as the chapter. Cut?")]),
("If all of this is one mechanism", [(S, "Restitution and foreclosure. About 2,700 words without a person in them, and the part Darity knows best. The dinner-table draft is clearer sentence by sentence; the content question is the same in both.")]),
("The gap has two faces in time.", [(I, "Reread: “two faces in time.”")]),
("So the framework proposes two instruments.", [(B, "The two bonds, defined. The core of the section."), (I, "“aggregate accountability bond”; the last sentence is technical.")]),
("Why bonds?", [(B, "Clear, and useful.")]),
("The backward instrument is called Restitution", [(B, "Darity's own published words, then a plain claim: “an instrument their framework already has room for.” Page numbers still needed.")]),
("Other names fail for their own reasons.", [(Q, "Names not chosen. Cut this and “The alternatives miss what matters”?")]),
("The forward instrument's name", [(B, "Ties “foreclosure” back to 2008.")]),
("Now the lineage behind the two instruments", [(Q, "The lineage tour starts here: four paragraphs, about ten names. The style sheet's rule is credit at the point of use.")]),
("The method belongs to them as well.", [(B, "The most important paragraph for Darity. Your plain statement of why you defer is the strongest thing in the section."), (I, "“an asteroid-mining colony” comes from nowhere for a reader of this chapter alone.")]),
("A current program in climate economics", [(I, "“adds only the grain.”")]),
("One question this book does not presume", [(B, "“An empty line is not a zero.”")]),
("Where does bond-posting actually stand", [(B, "Real numbers, and a real finding. Here and the next paragraph.")]),
("What is owed is a separate question", [(I, "“in any political weather.”")]),
("Come back, finally, to the room", [(S, "The family, again. A strong close in both versions."), (B, "The return to the room, and Butler's last sentence.")]),
("The rings end where they began", [(I, "Slight reread: “the one place from which no claim can ever be filed back.” The dinner-table draft is plainer.")]),
("So the question this chapter leaves", [(B, "Ends on the question the next chapters answer.")]),
]

CH5C = [
("One October afternoon in 2007", [(S, "The family. Clearer than the rings version from the third paragraph on. The first two paragraphs are a little slower."), (I, "“asked her for help. ‘Please help me…’” says help twice.")]),
("His decline had begun", [(I, "A run of short sentences. “had turned it down. He turned it down on the advice…” repeats.")]),
("Nothing in the way that decision was set up", [(B, "A clearer opener than “Nothing in the system had pushed the other way.”")]),
("The surgeon and writer Atul Gawande", [(B, "Clearer on how the decision gets made."), (I, "First of about fifteen definitions set inside a sentence (“palliative care, which is the care that…”).")]),
("The company that made the device was paid.", [(B, "Each step is spelled out: who was paid, and how the rest was paid.")]),
("In Butler's family the cost was paid", [(S, "The community. Better than the rings version on Libby and the Gulf. Even on fundraising.")]),
("That is a great deal of money", [(B, "A good joint between the two sets of numbers.")]),
("Asking for help this way", [(B, "Says why the least help goes to those with the least.")]),
("That insulation did not stay", [(B, "“The same material may be a few feet above the chair you are sitting in.” A plain ending in place of the shaped one.")]),
("Hundreds of people in Libby", [(I, "CHECK: “In its grocery store” implies the town has one store. The rings version says “grocery carts.”")]),
("Over its life the mine", [(B, "“The figures that have been disclosed are enough to show the scale.”")]),
("The acquittal doesn't mean", [(B, "The explanation you approved: one specific act, and no single decision that could be proven to be the crime.")]),
("The legal scholar Katharina Pistor explains", [(B, "Much clearer than the rings version."), (Q, "It is now about 190 words, and still the first stop for theory.")]),
("BP had drawn enormous value", [(B, "The three ways the cost fell, numbered: place, time, the living system.")]),
("Some of what the coast lost", [(B, "“Because it was never on anyone's books, it could be lost without anyone owing anything for it.”")]),
("So the fishing families went to court", [(B, "The legal tools are explained. “The law was different.”")]),
("The same thing had happened twenty years", [(Q, "Same question as in the rings version: a third spill case in a row."), (B, "“there has been no herring season.”")]),
("In 2008 the distance closed.", [(S, "The country. Clearly better than the rings version. This is where the dinner-table approach helps most.")]),
("I was doing well at the time.", [(B, "Your account, identical in both versions.")]),
("The 401(k) was one part of a longer change.", [(B, "“So wages stayed flat while medical bills climbed.”"), (I, "“the median wage, which is the wage of the worker in the exact middle.” To an economist this reads as talking down.")]),
("It began quietly in 1978", [(B, "Pension against account, one step at a time.")]),
("What was said less loudly", [(I, "“One was… Another was… The third was…” Short sentences of one shape.")]),
("What finally showed it", [(I, "“securities, which are investments that can be bought and sold.”")]),
("The reason is leverage", [(B, "The two homeowners, step by step. The best explanation in the chapter."), (I, "About 250 words, with “which means” twice. Trim, do not cut.")]),
("It is easy to be angry about that contrast.", [(I, "CHECK: “Being angry is not the same as being right” is a new sentence in your voice. Keep it only if you would say it.")]),
("One objection is about the borrowers.", [(B, "Each objection is labeled as an objection. The clearest gain over the rings version, here and the next three paragraphs.")]),
("Another objection is that the public", [(B, "“That is also true, but it answers a different question.”")]),
("The last objection is that reform", [(Q, "Still four objections in a row.")]),
("Sweden's banks were under pressure", [(B, "The krona is explained. “Sweden shows that another one was open.”")]),
("In 1972 Congress passed", [(B, "Clear. The rings version is equally clear here.")]),
("The record makes the case", [(B, "Better than “strong enough without embellishment.”")]),
("Social Security did not have to be built", [(I, "The definition of rents inside the sentence. “It was not fated.”")]),
("Two objections deserve a hearing.", [(B, "“it defends something this argument does not criticize.” Clearer than “The two pass each other.”")]),
("The second objection says the gap can be closed.", [(B, "“can be closed” for “tractable.”")]),
("In the villages near Baotou", [(S, "The world. Clear, and a little slower than the rings version.")]),
("At Baotou the cost is separated", [(B, "Time, place and power, each in turn.")]),
("The evidence from Baotou is thinner", [(I, "“remediation, which means cleaning up the damage.”")]),
("Rare earths also show a limit", [(Q, "Still points to the appendix. Same content question as in the rings version.")]),
("Now think of the phone in your pocket", [(S, "In your pocket, and in mine. Better here: no figures of speech.")]),
("That doesn't make you or me a villain.", [(B, "“The most virtuous person alive could own one of these phones, and the ponds would be exactly the same.”")]),
("With the phone in your hand", [(B, "Answers the question from Butler's house outright.")]),
("Put these cases next to each other", [(S, "The pattern, named. Even with the rings version.")]),
("The word has a second meaning", [(B, "“I keep the word because the cut is the thing I am describing.” In your voice."), (Q, "Same question: is this paragraph needed?")]),
("How does the party that gains get away", [(I, "“One is…” six times.")]),
("Then consider who absorbed the cost", [(B, "No idiom.")]),
("None of this is a new insight.", [(I, "“third parties, meaning people who had no part in the transaction.”")]),
("Some existing tools come close", [(I, "“a bond, which is money set aside as a guarantee.”")]),
("Ask what each of these cases drew on.", [(S, "One kind of thing. Clearer sentence by sentence, and still where the pull drops."), (I, "The weakest sentence in this version: “They are alike in how they stand toward the people who use them…” The added explanation is harder than what it explains.")]),
("The answer depends on what really happens", [(B, "The reply to Sandel is easier to follow here: “If the choice were… That is not the choice.”")]),
("That refusal has an ancestor.", [(I, "“Labor is human life. Land is nature. Money is a token of trust among people.” Three short sentences of one shape.")]),
("The living thinker closest to this argument", [(I, "Eleven short sentences in a row. “sinks, which are the places that absorb waste.”")]),
("In *The Code of Capital* Pistor names", [(B, "The four attributes get a sentence each.")]),
("The ledger shows who ended up with the cost.", [(S, "Who shaped the system? Clearer than the rings version."), (B, "“who wrote the rules that sent the cost to them.”")]),
("A rigorous set of tools", [(B, "Olson is explained: the small group organizes, the large group does not.")]),
("At Libby, internal company documents", [(B, "“a captured regulator, which means a regulator that has come to serve the industry…” The one definition that clearly helps.")]),
("It is easy to misread how I am using", [(B, "“I” in place of “this book.” “A tool can be used by people who disagree about nearly everything else.”")]),
("Chapter 9 develops this pairing", [(Q, "Same question: the paragraph that names four institutions.")]),
("If all of this is one mechanism", [(S, "Restitution and foreclosure. Clearer sentences, the same content question, and longer than the rings version.")]),
("The gap looks different depending", [(B, "Clearer than “two faces in time.”")]),
("So the framework proposes two instruments.", [(I, "“discharges, meaning pays off.”")]),
("Why bonds, and not a tax", [(B, "The question now names the alternatives, and the answer comes in three plain steps.")]),
("Other possible names fail", [(Q, "Same question: names not chosen.")]),
("Pistor supplies the legal half", [(I, "CHECK: the explanation of Parfit (“meaning how well or badly things go for whoever ends up living”) is the drafter's wording, not Parfit's."), (Q, "The lineage tour, as in the rings version.")]),
("The method belongs to them as well.", [(B, "Unchanged in substance. “When this book measures McDowell County's own gap in life expectancy, it borrows their method…” is clearer.")]),
("A current program in climate economics", [(B, "“They were first, and this framework says so.”"), (I, "“a finer grain.”")]),
("How much has actually been posted", [(B, "The question is plainer than “Where does bond-posting actually stand.”")]),
("The more important finding", [(B, "Explains the coal excise tax before using it.")]),
("What is owed is a separate question", [(B, "The last sentence is plainer than “in any political weather.”")]),
("Come back, finally, to the room", [(S, "The family, again. Strong in both versions.")]),
("Nothing in that room has changed", [(B, "“The room is not a comparison for the other cases. It is the same mechanism at its smallest size.”")]),
("The rings end where they began", [(B, "“no one can file a claim from the future against the past.”")]),
]

VERSIONS = [
 ('Ch1_A_your-redline_annotated', 'Chapter 1 · A · your June redline (current chapter)', 'manuscript/chapters/Chapter__1_TheQuietMath.md', CH1A,
  "My pick for Chapter 1. The scenes are the chapter, and they are in your words. Its issues are a few long unbroken paragraphs, a handful of sentences that need a second read, and one line near the end a new reader cannot follow."),
 ('Ch1_B_pace-redraft_annotated', 'Chapter 1 · B · pace redraft (Nov 10)', P+'ch1-pace-redraft_2026-11-10.md', CH1B,
  "Smooth, and it reads like a different writer. It rewrote most of the sentences you redlined by hand in June, and it adds two things you did not write. Its best contribution is paragraph breaks, mainly in the work section."),
 ('Ch1_C_dinner-table_annotated', 'Chapter 1 · C · dinner-table draft (Nov 12)', P+'ch1-dinner-table_2026-11.md', CH1C,
  "Your chapter with about 85 sentences changed, mostly long sentences split into short ones. The scenes are untouched. A few changes are worth taking; the lease section is flatter than yours; three rewordings shift your meaning."),
 ('Ch5_B_rings-redraft_annotated', 'Chapter 5 · B · rings redraft (the chapter on main)', 'manuscript/chapters/Chapter__5_TheAccountabilityGap.md', CH5B,
  "The tighter piece of writing, and the better opening pages. I had to reread about twelve times, most of all at the four objections on 2008. It also carries shaped closing lines and figures of speech that are not how you talk."),
 ('Ch5_C_dinner-table_annotated', 'Chapter 5 · C · dinner-table draft (Nov 12)', P+'ch5-dinner-table_2026-11.md', CH5C,
  "My pick to work from for Chapter 5. Easier to follow in one pass (about five rereads). Its issues are its own: runs of short same-shaped sentences, and about fifteen definitions set inside sentences. In both versions the last third is a tour of names where the pull drops."),
]

CSS = '''@page{size:letter;margin:0.6in 0.5in 0.7in}
body{font-family:"EB Garamond",Georgia,serif;font-size:11.3pt;line-height:1.42;color:#111;margin:0}
h1{font-size:16pt;margin:0 0 3pt} .sum{font-size:10.6pt;margin:0 0 6pt}
.legend{font-family:"DejaVu Sans",Arial,sans-serif;font-size:7.6pt;line-height:1.45;border:0.6pt solid #666;padding:5pt 7pt;margin:0 0 10pt}
table{width:100%;border-collapse:collapse;table-layout:fixed}
col.n{width:0.3in} col.t{width:4.45in} col.m{width:2.75in}
td{vertical-align:top;padding:0 0 7pt}
td.n{font-family:"DejaVu Sans",Arial,sans-serif;font-size:6.8pt;color:#777;padding-top:3pt}
td.t{padding-right:0.16in} td.t p{margin:0}
td.m{font-family:"DejaVu Sans",Arial,sans-serif;font-size:7.5pt;line-height:1.38;border-left:0.5pt solid #999;padding-left:0.11in}
.k{font-weight:bold;letter-spacing:0.03em;font-size:6.9pt}
.note{margin:0 0 4.5pt} .SECTION{border:0.9pt solid #111;padding:3pt 4pt;margin-bottom:5pt}
.BEST .k{color:#0a5d2a} .ISSUE .k{color:#9a1c1c} .QUESTION .k{color:#1d3f8a}
.BEST{border-left:2.2pt solid #0a5d2a;padding-left:4pt} .ISSUE{border-left:2.2pt dashed #9a1c1c;padding-left:4pt} .QUESTION{border-left:2.2pt dotted #1d3f8a;padding-left:4pt}
tr.h td{padding:9pt 0 5pt;font-size:13.5pt;font-weight:bold;break-after:avoid}
tr.r td{padding:2pt 0 9pt;text-align:center;color:#777}'''

def fmt(s):
    s = html.escape(s, quote=False)
    return re.sub(r'\*(.+?)\*', r'<i>\1</i>', s)

def build(slug, label, path, notes, summary, outdir):
    raw = re.sub(r'<!--.*?-->', '', open(path).read(), flags=re.S)
    lines = [x.strip() for x in raw.split('\n') if x.strip()]
    body = [x for x in lines if not x.startswith('#') and x != '---' and not x.startswith('*By ')]
    used = set(); rows = ''; n = 0
    for x in lines:
        if x.startswith('# ') or x.startswith('*By ') or x.startswith('## Chapter'): continue
        if x.startswith('## '): rows += f'<tr class="h"><td></td><td colspan="2">{fmt(x[3:])}</td></tr>'; continue
        if x == '---':
            if n: rows += '<tr class="r"><td></td><td>* * *</td><td></td></tr>'
            continue
        n += 1; m = ''
        for i, (pref, ns) in enumerate(notes):
            if x.startswith(pref):
                assert sum(y.startswith(pref) for y in body) == 1, (slug, pref)
                used.add(i)
                m += ''.join(f'<div class="note {k}"><span class="k">{k}</span> {fmt(t)}</div>' for k, t in ns)
        rows += f'<tr><td class="n">{n}</td><td class="t"><p>{fmt(x)}</p></td><td class="m">{m}</td></tr>'
    missing = [notes[i][0] for i in range(len(notes)) if i not in used]
    assert not missing, (slug, missing)
    words = len(' '.join(body).split())
    h = f'''<!doctype html><meta charset="utf-8"><title>{label}</title><style>{CSS}</style>
<h1>{label}</h1><p class="sum">{words:,} words, {n} paragraphs. The text is exactly as the file has it; nothing is edited. {summary}</p>
<div class="legend"><b>How to read the margin.</b> Small numbers count paragraphs, so you can point to one.
<b>SECTION</b> (boxed): how this section compares with the other versions.
<b style="color:#0a5d2a">BEST</b> (solid bar): what is strongest here, or worth carrying into a combined version.
<b style="color:#9a1c1c">ISSUE</b> (dashed bar): where I had to reread, where the voice is not yours, or where something was added or changed.
<b style="color:#1d3f8a">QUESTION</b> (dotted bar): a content, flow or pacing question for the big edit.
A paragraph with no note read fine and is not remarkable either way. These are one reader's opinions.</div>
<table><colgroup><col class="n"><col class="t"><col class="m"></colgroup>{rows}</table>'''
    open(f'{outdir}/{slug}.html', 'w').write(h)
    print(slug, words, 'words', n, 'paras', len(notes), 'annotated paras')

if __name__ == '__main__':
    for v in VERSIONS: build(*v, sys.argv[1])
