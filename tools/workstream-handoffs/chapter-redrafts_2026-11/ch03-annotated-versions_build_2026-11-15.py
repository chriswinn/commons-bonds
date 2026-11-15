#!/usr/bin/env python3
"""Annotated print copies of the three Ch 3 versions, and the paragraph-by-paragraph table (2026-11-15).

Pattern: tools/workstream-handoffs/pull-pass_2026-11/annotated-versions_build_2026-11.py (Ch 1 and Ch 5).
Builds one HTML per version: the text exactly as the file has it, a printed number beside every
paragraph, and a margin column with notes labeled SECTION / BEST / ISSUE / QUESTION, plus two labels
the author asked for on this chapter: ADDED (in a draft, not in the current chapter) and OMITTED
(in the current chapter, not in the drafts), each with a recommendation. Nothing is edited.

Usage, from the repo root:
  python3 tools/workstream-handoffs/chapter-redrafts_2026-11/ch03-annotated-versions_build_2026-11-15.py OUTDIR
It also rewrites the paragraph table inside ch03-comparison_2026-11-15.md (between the two markers).
Then print each HTML to PDF with page numbers (ch03-print-pdf.js). PDFs are not committed.

The notes are one reader's opinion for the author. That reader also wrote drafts B and C.
"""
import re, html, sys
D = 'tools/workstream-handoffs/chapter-redrafts_2026-11/'
S, B, I, Q, AD, OM = 'SECTION', 'BEST', 'ISSUE', 'QUESTION', 'ADDED', 'OMITTED'

# ---------------------------------------------------------------------------------------------
# Paragraph by paragraph. B and C share one numbering (98 paragraphs). Each row:
# (B/C paragraph, the A paragraph(s) it comes from, which version is best, one-line reason).
# "best" is A, B, C, or two letters where they are even.
ROWS = [
(1, '1', 'B', "Almost the same as A. B names the Hampton Roads Bridge-Tunnel where A says “HRBT.” C adds words and loses “gray on gray.”"),
(2, '2', 'B', "“the men who come home empty are quieter than the others” is easier than A's “the men coming home the second way.”"),
(3, '3', 'BC', "The question pulls; A's “This chapter is about…” announces."),
(4, '4', 'B', "A puts “I grew up on this bay” after the oyster firm, which reads out of order."),
(5, '5', 'A', "A has the best line: “it was lost to the going price of gravel.” Neither rewrite matches it. Take A's sentence into B."),
(6, '6', 'B', "Fixes the unnamed “we” (“We paved…”) by naming the towns and the Navy."),
(7, '7', 'B', "Plainer than A's “The story of a renewable resource turning non-renewable has never needed explaining to me.” Close call."),
(8, '8', 'B', "A's “zero generations removed from the community” is an odd phrase. C's “has never been removed” is also fine."),
(9, '9', 'B', "Your chop passage. B is the easiest to follow. A keeps your word “wavelength”; B and C explain it without the word."),
(10, '10', 'AB', "Nearly identical. Your words about the slicks and the weight of the clothes are in all three."),
(11, '11', 'C', "“They are not describing a feeling. They are describing how the work is built.” The net-mending morning is clearest here."),
(12, '12', 'C', "The missing man. C says the hard sentence plainly: a waterman is always where he said he would be, unless something serious has happened."),
(13, '13', 'ABC', "The same in all three."),
(14, '14', 'B', "A spends two lines on what it is not starting from (prehistory, 1607). C's “a thinner one” is the drafter's word, not A's."),
(15, '15', 'B', "A's “Two orders of magnitude in a century, a 99 percent decline” says it twice."),
(16, '16', 'C', "The three causes, one at a time. The longest version and the clearest."),
(17, '17', 'B', "Ties back to Chapter 2. A's “an instrument that produces more oysters” uses “instrument” for a reef, and the book needs that word later for the bond."),
(18, '18', 'C', "The chapter's main idea. C walks it step by step. A's “visible and irreversible at the same time” is a good phrase that both drafts lose."),
(19, '19', 'C', "Ostrom on the verified wording, in three short sentences. A's version says her governing “gives way,” which overstates."),
(20, '20', 'ABC', "Your sunset line. The same in all three apart from the opening words."),
(21, '21', 'A', "Biggie. A is closest to the way the story was first set down. B and C change a few joins and nothing else."),
(22, '22', 'A', "The six-pack and the lunch in the water. Leave it as A has it."),
(23, '23', 'ABC', "The same."),
(24, '24', 'B', "A's subject runs 18 words before the verb (“The motion Biggie's body had worn down to a quarter turn of the wrist is not being shown…”). B splits it."),
(25, '25', 'B', "A's opening sentence is 46 words with two insertions; I had to reread it."),
(26, '26', 'AB', "The same. C's “Think of” adds nothing."),
(27, '27', 'B', "A's “the texture of generational witness” is a literary phrase."),
(28, '28', 'C', "“A good season used to carry a family through a year” is plainer than “Seasons that used to carry a year.” A ends on two short verdict lines (see OMITTED in the A copy)."),
(29, '29', 'ABC', "Hudgins. The same quotations."),
(30, 'none', 'BC', "ADDED: a question that hands the reader to the rockfish section."),
(31, '30', 'A', "Your boyhood memory. A is closest to what you wrote, including “we went on taking as much as we could carry.” B and C change “we” to “those of us who fished the Bay.”"),
(32, '31', 'B', "Clear and quick. C adds a definition of “moratorium.”"),
(33, '32', 'C', "Hardin. “The watermen did restrain themselves.” A opens with “It is worth naming what the moratorium disproves,” which announces."),
(34, '33', 'C', "Explains what the young-of-year count is before giving it."),
(35, '34', 'B', "Colden, three quotations. All three versions carry the same words."),
(36, '35', 'ABC', "Moore. The same."),
(37, '36', 'C', "A's last sentence is 70 words. C breaks it where the thought turns."),
(38, '37', 'B', "A ends “The asymmetry is the point.” and has the committees “discover an unfamiliar caution,” which is irony, not how you talk."),
(39, '38', 'C', "B has “how the two clocks differ,” a figure of speech the drafter added. C says it plainly."),
(40, '39', 'B', "The recast (call 3b). See QUESTION."),
(41, '40', 'B', "Shad. B gives the biology before the men, so the empty nets land harder."),
(42, '41–45', 'B', "Crab, folded into one paragraph by call 1. It is long in both drafts (273 and 290 words). A's four short paragraphs breathe more."),
(43, '46–47', 'A', "A's fragments have the rhythm: “The menhaden. Bunker, on the New Jersey side. Pogy, in New England. On the Bay, just menhaden.”"),
(44, '48', 'B', "“none of it goes to anyone's dinner table as fish.”"),
(45, '49', 'B', "A opens “Structurally, this is an interesting case,” which is flat."),
(46, '50', 'B', "The cap. Same facts; B and C split A's semicolon pairs."),
(47, '51', 'B', "“Meanwhile nobody knows how many menhaden are in the Bay” is a stronger opener than A's “The gap is no abstraction.”"),
(48, '52', 'A', "A is the tightest and the best: “Increases get adopted at the speed of the appetite for them, reductions at the speed of the resistance to them. The watermen know the asymmetry. The ospreys feel it.”"),
(49, '53', 'B', "B puts Reedville first, then the customers, then where the cost stays."),
(50, '54', 'C', "The petition. C explains “reduction fishery,” which A and B never do."),
(51, '56', 'B', "ADDED opening sentence links the watershed to the fishing sections."),
(52, '57', 'B', "Same content, shorter sentences."),
(53, '58', 'C', "“The reason is political weight.”"),
(54, '59', 'C', "Your sailboat observation is the same in all three. C explains the dead zones most clearly. A's “in a longer register” is literary."),
(55, '60', 'A', "A ends on the line the map names as this section's handoff: “The asymmetry is the geography, and the geography does the work the accounting will not.” Both drafts dropped it. Restore it."),
(56, '61', 'B', "The unnamed Fox Hill man. Small differences only."),
(57, '62', 'B', "“What is particular to him is how he has absorbed them.”"),
(58, '63', 'B', "“the man on the water” for A's “the presence on the water continuing.”"),
(59, '64', 'A', "“He did not quit the water. He could not.” is stronger as two sentences."),
(60, '65', 'C', "The guess is out (your call 3a). C's last two sentences are the clearest statement of what the book counts."),
(61, '66', 'B', "ADDED bridge in place of A's “There is a particular kind of community… a particular kind of decision.”"),
(62, '67', 'B', "Tangier. Same facts."),
(63, '68', 'A', "A keeps “The whole package, in his words.” The source file shows “the whole package” is part of Eskridge's quotation. Both drafts dropped it."),
(64, '69', 'B', "Smith Island. The saying is the same in all three."),
(65, '70', 'ABC', "Tilghman. The same. See QUESTION."),
(66, '71', 'B', "Hampton. C's “It used to be a place where… It is becoming a place where…” is also good. A's ending repeats “thins” five times."),
(67, '72', 'B', "C falls into a run of “They are asked… They are asked…” B reads in one pass."),
(68, '74', 'B', "The marina scene is out (your call 3c). What is left is what you have heard. See QUESTION on the daughter."),
(69, '75', 'C', "A has “a generation-scale withdrawal of the human capital.” C: “They will not teach a son into a trade when they cannot promise him it will support him.”"),
(70, '76', 'B', "Same thought; B is one sentence shorter than C."),
(71, '77', 'B', "The drafts drop one sentence from A (see OMITTED in the A copy)."),
(72, '78', 'ABC', "Evans and Harris. The same."),
(73, '79', 'BC', "ADDED: seven words in place of A's announcement (“A paradox has emerged… worth setting down carefully”)."),
(74, '80', 'B', "Same facts and quotations."),
(75, '81', 'ABC', "Tarnowski. The same."),
(76, '82', 'ABC', "The same."),
(77, '83', 'B', "All three say “in the same year.” The sources on file do not support that. See ISSUE."),
(78, '84', 'ABC', "Ruth. The same."),
(79, '85', 'B', "The paradox explained. A's last two sentences are good too: “They cannot pay for it. The price is not constructed to carry it.”"),
(80, '86', 'none', "None of the three is clear. What is “the same accounting” that recovers species and squeezes watermen? See ISSUE."),
(81, '87', 'B', "Ends on the question the column answers."),
(82, '88–89', 'B', "Names the Restitution Bond without the process talk (“a floor I can defend against anyone who wants to fight me about it”)."),
(83, '90', 'B', "States the one thing being priced, then asks what it would cost."),
(84, '91', 'C', "Says why the shell mountains cannot give the price."),
(85, '92–94', 'C', "The floor, step by step. A states the floor three times in three paragraphs."),
(86, '95–96', 'B', "But A has a line both drafts lost: “It was the fee Hampton charged to ship its own wealth away.” Restore it."),
(87, '97–98', 'C', "C's Mazzucato and Harvey sentences read best. A has “Value goes up and out. Cost stays and settles down,” which echoes your Chapter 1. Restore those two sentences."),
(88, '99–100', 'C', "The public is paying. C takes it in steps. It is 244 words and wants a paragraph break at “These two sets of numbers.”"),
(89, '101', 'B', "McDowell, once. A's version is one 63-word sentence followed by a 59-word one."),
(90, '102', 'B', "What the bond does. A repeats the figures and says “the modesty is its strength.”"),
(91, '103', 'C', "The credit to Darity, Mullen and Coates. “I did not invent this move.”"),
(92, '104', 'B', "A restates the floor a third time and argues with an imagined critic."),
(93, '105', 'B', "One sentence, by call 2."),
(94, '110–111', 'A', "A's two paragraphs repeat “He is paid for what comes up in the tongs,” and the repeat works. The drafts merged them into one long paragraph."),
(95, '112', 'B', "The room. B's last two sentences are clearer than A's (“The system has been extracting from them both…”)."),
(96, '113', 'A', "A says it in one flowing sentence. B and C use the short “is not X. It is Y.” shape you have cut elsewhere."),
(97, '114–118', 'B', "Norway in one paragraph, by call 2. A holds the country's name back for a paragraph, like a riddle."),
(98, '119', 'ABC', "The closing harbor paragraph. Word for word the same."),
]
BEST = {n: b for n, a, b, t in ROWS}

# ---------------------------------------------------------------------------------------------
# Margin notes by paragraph number. A has its own numbering (119 paragraphs).
NA = {
1: [(S, "The harbor. All three versions are close to each other here. The pace draft is this text with small fixes.")],
3: [(OM, "The drafts turn this into a question (“So what are those books not allowed to record?”). Stronger as a question: it pulls, and this sentence announces. Recommend the question.")],
5: [(B, "“it was lost to the going price of gravel.” The best sentence in the section; neither draft matches it. One caution: your notes say you were told growing up that people did not know shell belonged back in the water. This sentence says they did. Which is right?")],
6: [(I, "“We paved… we are casting concrete”: an unnamed “we.” The drafts name the towns and the Navy.")],
8: [(S, "Fox Hill. The dinner-table draft is best on the net-mending morning and the missing man. Your own chop and clothing passages read well in all three.")],
9: [(OM, "The word “wavelength.” It is your word. The drafts explain the idea without it. Either works; keep it if you like the word.")],
14: [(S, "The oyster. The dinner-table draft is clearest on the three causes and on why the damage is permanent."), (OM, "“Not in some prehistoric sense, not before the Powhatan, not before the English came up the James in 1607.” Stronger without: it lists what the chapter is not doing. Recommend leaving it out.")],
18: [(B, "“visible and irreversible at the same time.” Both drafts lose this phrase. Worth keeping.")],
19: [(OM, "The longer Ostrom paragraph. Cut to the verified wording by your call 4. Stronger and more accurate short: this version says her governing “gives way,” and the checked position is narrower.")],
21: [(S, "Biggie. This version is the best. Leave it almost exactly as it is."), (B, "The oak, the one oar, the bars he worked his entire life.")],
22: [(B, "The best paragraph in the chapter. Your father's story, and “as fresh as it could be.”")],
25: [(S, "Witness. The pace draft is best: this version's first sentence needs a second read."), (I, "First sentence: 46 words, two insertions before the verb.")],
28: [(OM, "“The bodies are the instrument. The memory is the data.” The drafts say it in one plain sentence (“they keep it in their bodies and their memories”). These are two short verdict lines of the kind you cut from Chapter 5. I lean to leaving them out, but a reader remembers them. Your call.")],
30: [(S, "Rockfish. The drafts are clearer on the politics. This version is best on your own memory."), (B, "Your boyhood memory, closest to your own words. “we went on taking as much as we could carry to the shore.”")],
32: [(I, "“It is worth naming what the moratorium disproves” announces the point before making it.")],
37: [(OM, "“The asymmetry is the point.” Stronger without: a short verdict on what was just said. Recommend leaving it out.")],
39: [(OM, "The retired waterman. You said he is not one man, so the paragraph cannot stay as one man's account. The drafts recast it. Lost with it: “Nobody has told him what the political conditions for another collapse are,” the strongest line here. It depends on the claim that managers told him the conditions for a moratorium do not exist, and there is no source for that. Recommend leaving it out unless you have one.")],
40: [(S, "Shad and crab. Folded into the rockfish section by your call 1. Nothing was lost from the shad paragraph.")],
41: [(S, "The crab has its own section here, in four short paragraphs. The drafts make it one long paragraph. The content is the same except the two notes below.")],
44: [(OM, "“That sentence carries more than it appears to.” Stronger without: it tells the reader what to think of the quotation.")],
45: [(OM, "“We aren't catching what we used to catch.” The drafts keep the first three of these lines and drop this one. No strong view. It can go back.")],
46: [(S, "Menhaden. About even. This version has the best two short paragraphs (47 and 52); the pace draft has the better order.")],
47: [(B, "The fragments. Deliberate, and they work.")],
52: [(B, "Three sentences, and the best statement of the asymmetry in any version.")],
55: [(OM, "“The shape is familiar. Coal had it.” Stronger without. The map counted five McDowell comparisons in this version; this is a sixth.")],
56: [(S, "The watershed. The drafts are a little clearer. This version has the better ending.")],
60: [(B, "“The asymmetry is the geography, and the geography does the work the accounting will not.”"), (OM, "Both drafts dropped that sentence as a closing line. The chapter is weaker without it. It is the idea the section exists for, and the map names it as the handoff. Recommend restoring it.")],
61: [(S, "The unnamed Fox Hill man. All three are close. The drafts cut the guess (your call 3a).")],
64: [(B, "“He did not quit the water. He could not.”")],
65: [(OM, "“My guess… is that over a beer at the end of a long day he would say he is glad…” Cut by your call 3a. Stronger without: it puts words in a living man's mouth.")],
66: [(S, "The islands. Even. See the note at Eskridge."), (OM, "This opener is replaced in the drafts by “He has a second trade to fall back on. Whole communities on this Bay do not.” Stronger with the replacement: it ties the islands to the man you just met.")],
68: [(OM, "“The whole package, in his words.” Dropped from the drafts because I could not match it to a source. I have since found it: the citation spec gives the quotation as “…(a) way of life — the whole package.” So it is his. Recommend restoring it inside the quotation, after one check against the article.")],
70: [(Q, "Four names from photographs, and no one speaks. Does Tilghman earn its place, or is one sentence enough?")],
73: [(OM, "The McDowell line. Stronger without, by the map: once in the column and once in the room is enough.")],
74: [(S, "The children. The scene is gone from the drafts because you said it did not happen (call 3c)."), (OM, "The October marina scene: the question, the long pause, the glance at the water. Out, because it is not a real scene. The chapter loses a person here. If there is a real conversation you remember, this is the place for it, in your words.")],
77: [(OM, "“Most of them carry, somewhere, a respect for what their fathers did that they will not put into words.” The drafts drop it: it states a feeling the children have not expressed. Recommend leaving it out, unless you have heard one of them say it.")],
79: [(S, "The paradox. The pace draft is best."), (OM, "This announcement is replaced in the drafts by “And yet the oysters are coming back.” Stronger without the announcement. One real loss: this is the only place the current chapter says “cost-severance pattern,” and neither draft uses the book's word “severed” anywhere. See the QUESTION at paragraph 101.")],
83: [(I, "“In the same year.” The sources on file date the celebration of the five sanctuaries to August 2025 and the disaster request to February 2026. That is six months apart, not the same year. All three versions carry this. Suggested: “Six months after the program was celebrated…”")],
86: [(I, "“the same accounting that is… beginning to recover what was lost.” I could not tell what accounting is meant. The drafts did not fix it."), (OM, "“They are the same process, seen from the two sides of the ledger.” Left out of the drafts. No loss.")],
88: [(S, "The reef column. The drafts are much the better here: the floor is stated once, and the argument with an imagined critic is gone. Three lines from this version should go back (notes at 96, 97)."), (OM, "“So let me do… Let me add up the column.” Stronger without (the map's process-note list).")],
89: [(OM, "“a floor I can defend against anyone who wants to fight me about it.” Stronger without. So are “the first discipline of the floor,” “I would rather name my proxy than hide it,” “a floor nobody can knock over,” and “the part nobody can take away from me” in the paragraphs that follow. They make the reader an auditor.")],
96: [(B, "“It was the fee Hampton charged to ship its own wealth away.”"), (OM, "Both drafts lost that sentence. The chapter is weaker without it. Recommend restoring it.")],
97: [(B, "“Value goes up and out. Cost stays and settles down.” This echoes your Chapter 1 (“went up and out… settled down onto him and stayed”)."), (OM, "Both drafts lost those two sentences. Recommend restoring them. The third sentence (“the same sentence this book wrote about a county under coal”) is another McDowell repeat and can stay out.")],
98: [(OM, "The longer Mazzucato and Harvey paragraph. Cut to a sentence or two by your call 4. Stronger short.")],
100: [(OM, "“A rounder program-level figure of about $108 million… corroborates the magnitude, nothing more.” Out by your call 5. Stronger without: it is a sourcing note. Also out: “I am not going to invent a number to make a point.”"), (I, "“a world's-largest oyster operation.” Paragraph 4 says “one of the largest… in the country.” The drafts use the smaller claim in both places.")],
101: [(OM, "“the rhyme is the proof that this is a mechanism and not an accident.” Left out of the drafts. Two cases do not prove a mechanism, and a critic will say so. Stronger without."), (Q, "This paragraph says the cost “was severed loose.” The drafts say it “came loose from the value.” Neither draft uses “severed” or “cost severance” anywhere in the chapter. Should the book's own term appear here at least once?")],
102: [(OM, "The repeat of the figures, “the modesty is its strength,” and “a Navy crew in the Hampton Roads mud stacking concrete blocks.” Out with call 5. The Navy crew is a good picture; it could return in one clause.")],
104: [(OM, "The third statement of the floor and the “hand a critic the lever” line. Out by your call 5. Stronger without.")],
105: [(S, "The ending. Five sections here; the drafts have three paragraphs, the room, Norway, and the harbor (your call 2). The drafts are stronger. One sentence from this paragraph is worth a second look."), (OM, "“The thinning comes in stages, first in the margins, then in the center, then in the structure that produced the catch.” The drafts cut it with the list of fisheries. It sums up the whole chapter in one line. Recommend restoring that one sentence.")],
106: [(OM, "The fathers on “a Tuesday afternoon in early November” and “the thought they are not going to say out loud.” Stronger without: it writes a thought for men who have not said it, the same problem as calls 3a and 3c.")],
108: [(OM, "McDowell again. Stronger without.")],
109: [(OM, "“While I was finishing this chapter, I went back to McDowell County in my mind.” Cut by your call 2. Stronger without: the reader has just finished the column, where McDowell is already set beside the reef.")],
110: [(B, "This paragraph and the next. The repeat of “He is paid for what comes up in the tongs” works. The drafts merged the two into one long paragraph.")],
112: [(B, "The room. The new idea in the ending, and it is in all three.")],
113: [(B, "One sentence, and better than the drafts' three.")],
114: [(S, "Norway. Five paragraphs here; one in the drafts (call 2). Chapter 4 tells this story in full, so the short version is enough.")],
116: [(OM, "“existence proof.” Not in the drafts. It is the title of the next chapter, so the phrase can wait one page.")],
117: [(OM, "What the watermen would say if someone described Norway's fund to them. Stronger without: it is a guess at what living men would say.")],
119: [(B, "The return to the harbor. Word for word the same in all three.")],
}

NB = {
1: [(S, "The harbor. My pick of the three, narrowly: the current chapter with small fixes.")],
3: [(AD, "The question replaces “This chapter is about what those books are not allowed to record.” Recommend keeping the question.")],
5: [(I, "“So anyone could see what shell did when it went back in the water.” Weaker than the current chapter's “it was lost to the going price of gravel.” Take that sentence.")],
8: [(S, "Fox Hill. Good on your chop passage. The dinner-table draft is better on the net-mending morning and the missing man.")],
14: [(S, "The oyster. Tighter than the dinner-table draft, and a little harder on the two paragraphs that carry the idea (16 and 18).")],
17: [(AD, "“The last chapter ended on the difference between two kinds of drawdown.” A link back to Chapter 2. Chapter 2 makes the point three paragraphs before its end, so “ended on” is loose, and Chapter 2 is about to be redrafted. Keep the link; fix the wording once Chapter 2 is settled.")],
19: [(I, "Ostrom, cut to two sentences by your call 4. The dinner-table version reads better.")],
21: [(S, "Biggie. Nearly the current chapter. Where they differ, the current chapter is better.")],
25: [(S, "Witness. My pick for this section.")],
30: [(AD, "A question to carry the reader into the rockfish section. This is the second of three such questions (3, 30, 81). Recommend keeping this one and 81; if three feels like a habit, this is the one to cut.")],
31: [(S, "Rockfish, with shad and crab folded in. Clearer than the current chapter on the politics."), (I, "“those of us who fished the Bay went on taking.” You wrote “we.” Changed because the style sheet asks for a named group. Your call.")],
33: [(AD, "Hardin's essay named by its title, “The Tragedy of the Commons.” Keep.")],
39: [(I, "“how the two clocks differ.” A figure of speech I added. The dinner-table version is plain.")],
40: [(Q, "Call 3b. The recast, with no one man in it. “and no second moratorium has been called” is ADDED and has no source on file. Keep, cut, or supply a source?")],
41: [(B, "Shad. The fish first, then the men and the empty nets.")],
42: [(I, "273 words in one paragraph. A break before “The 2025 winter dredge survey” would help."), (Q, "Call 1 folded the crab into this section. Read the current chapter's four short crab paragraphs beside this one and see which you prefer.")],
43: [(S, "Menhaden. Best order of the three versions. The current chapter has two short paragraphs that beat mine (its 47 and 52).")],
47: [(AD, "“Meanwhile nobody knows how many menhaden are in the Bay.” Replaces “The gap is no abstraction to the people working the science.” Keep.")],
48: [(I, "The current chapter says this better and shorter.")],
50: [(OM, "After the vote, the current chapter has “The shape is familiar. Coal had it.” Left out here. Stronger without.")],
51: [(S, "The watershed."), (AD, "“The fishing is only part of what reaches the watermen.” A link from the fishing sections. Keep.")],
55: [(OM, "The current chapter ends this section: “The asymmetry is the geography, and the geography does the work the accounting will not.” I cut it as a closing line. That was a mistake. Recommend restoring it.")],
56: [(S, "The unnamed Fox Hill man. Close to the current chapter.")],
60: [(OM, "The guess about what he would say over a beer is out here, by your call 3a.")],
61: [(S, "The islands and Hampton."), (AD, "Two sentences that tie the islands to the man you just met. Keep.")],
63: [(OM, "“The whole package, in his words.” Dropped here. It turns out to be part of Eskridge's quotation in the source file. Recommend restoring it inside the quotation.")],
65: [(Q, "Does Tilghman earn its place?")],
66: [(B, "Hampton and the marina tipping from working boats to recreational ones.")],
68: [(S, "The children. The marina scene is out (your call 3c), so the section opens on a question."), (Q, "“A daughter in nursing school in Norfolk…” Did a man on the waterfront tell you this? If not, it comes out here and in paragraph 94.")],
71: [(OM, "The current chapter adds: “Most of them carry, somewhere, a respect for what their fathers did that they will not put into words.” Left out: it states a feeling nobody is recorded as having.")],
73: [(S, "The paradox. My pick for this section."), (AD, "Seven words in place of “A paradox has emerged in the most recent years, and it is worth setting down carefully…” Keep.")],
77: [(I, "“In the same year.” The sources on file put the celebration in August 2025 and the disaster request in February 2026. Suggested: “Six months after the program was celebrated…”")],
80: [(I, "“the same accounting that is beginning, species by species, to recover what was lost.” Not clear in any version. What accounting?")],
81: [(AD, "The closing question (“So who did pay for the reef, and who should have?”). Keep: it is the question the column answers.")],
82: [(S, "The reef column. Tighter than the dinner-table draft; the dinner-table draft is easier on the arithmetic (85, 87, 88)."), (AD, "“The last chapter added up what was left unpaid for the miner.” Replaces “So let me do for the oyster what this book refused to leave undone for the miner.” Keep.")],
86: [(OM, "The current chapter has “It was the fee Hampton charged to ship its own wealth away.” Lost here. Recommend restoring it.")],
87: [(OM, "The current chapter has “Value goes up and out. Cost stays and settles down.” Lost here. Recommend restoring it. It echoes Chapter 1."), (I, "Mazzucato and Harvey in one sentence with a semicolon. The dinner-table version is easier.")],
88: [(AD, "“These two sets of numbers measure different things. The damage figure is for one river, and the public spending is for the whole Bay, so one cannot be subtracted from the other.” Required by the reef decision of November 10. Keep."), (Q, "Critic question 2: the public has already spent more than the floor. So what is unpaid? The answer here is “who has paid,” but paragraph 87 says the cost “went unpaid.”"), (OM, "The $108 million corroborating figure is out, by your call 5.")],
89: [(Q, "The current chapter says the cost “was severed loose.” This says it “came loose from the value.” The book's word “severed” appears nowhere in this draft. Should it appear here?")],
92: [(OM, "The current chapter restates the floor here a third time. Out by your call 5.")],
93: [(S, "The ending: three paragraphs, the room, and Norway (your call 2)."), (OM, "Cut with the list of fisheries: “The thinning comes in stages, first in the margins, then in the center, then in the structure that produced the catch.” Recommend restoring that one sentence here.")],
94: [(I, "170 words. The current chapter has this as two paragraphs with a repeated line, and that is better.")],
96: [(I, "“is not a resource. It is a position.” The short shape you have cut elsewhere. The current chapter's single sentence is better.")],
97: [(B, "Norway named in the first words, one paragraph, and straight to the next chapter.")],
98: [(B, "Word for word the current chapter.")],
}

NC = {
1: [(S, "The harbor. The wordiest of the three here, and it loses “gray on gray.”"), (I, "“the last dark before the sky turns gray” and “gray water under a gray sky” explain an image that did not need it.")],
3: [(AD, "The question replaces “This chapter is about…” Keep.")],
5: [(I, "Clear on the shell and the gravel, but the current chapter's “it was lost to the going price of gravel” is better than this.")],
8: [(S, "Fox Hill. My pick for the net-mending morning and the missing man (11, 12).")],
9: [(AD, "“so a five-foot wave lifts a boat slowly and sets it down slowly.” An explanation I added to your chop passage. It is not in your notes. Strike it if you don't want it.")],
11: [(B, "“They are not describing a feeling. They are describing how the work is built.”")],
12: [(B, "The missing man, said plainly.")],
14: [(S, "The oyster. My pick for this section."), (I, "“The grandfathers fished one Bay. The fathers fished a thinner one.” “Thinner” is my word. The current chapter says only that it was not the same Bay.")],
16: [(B, "The three causes, each given its own sentences.")],
17: [(AD, "The link back to Chapter 2. See the note in the pace copy: keep the link, fix “ended on” when Chapter 2 is settled.")],
18: [(B, "The chapter's main idea, step by step: the harvest was taking the reef along with the oysters.")],
19: [(B, "Ostrom in three sentences, on the checked wording.")],
21: [(S, "Biggie. Nearly the current chapter. Prefer the current chapter.")],
25: [(S, "Witness. About even with the pace draft.")],
26: [(I, "“Think of” adds nothing.")],
28: [(B, "“A good season used to carry a family through a year, and now it carries them through only part of one.”")],
30: [(AD, "The handoff question. See the note in the pace copy.")],
31: [(S, "Rockfish, shad and crab. My pick for the middle of this section (33, 34, 37, 39)."), (I, "Your memory is split into more sentences here than you wrote. The current chapter is closer to you.")],
32: [(AD, "“a moratorium, which is a complete stop to fishing for a set time.” A definition set inside the sentence. Keep or strike (style rule 29).")],
33: [(B, "“The watermen did restrain themselves.”"), (AD, "The essay's title. Keep.")],
34: [(B, "Says what the young-of-year count is before giving the number.")],
37: [(B, "The late admission, in short steps.")],
39: [(B, "“how differently time runs for the scientists and for the watermen.”")],
40: [(Q, "Call 3b. The recast. “no second moratorium has been called” is ADDED and has no source on file.")],
42: [(I, "290 words in one paragraph. It needs a break before “Then the numbers turned.”"), (AD, "“Then the numbers turned.” and “She is saying that…” are joins I added.")],
43: [(S, "Menhaden. Clear, but the current chapter's short paragraphs (its 47 and 52) are better than mine.")],
44: [(AD, "“what biologists call a forage fish, which means it sits at the base of the Bay's food web.” A definition. Keep or strike.")],
48: [(I, "The current chapter says this better in fewer words.")],
50: [(B, "Explains “reduction fishery.”"), (AD, "“The Reedville operation is called a reduction fishery, because it reduces the fish to meal and oil.” A definition. Recommend keeping this one: the term is in the petition and the reader has not met it.")],
51: [(S, "The watershed. My pick, narrowly."), (AD, "“The fishing is only part of what reaches the watermen. The rest comes down the rivers.” Keep.")],
53: [(B, "“The reason is political weight.”")],
54: [(B, "The dead zones explained in three sentences.")],
55: [(OM, "The current chapter's last sentence is missing: “The asymmetry is the geography, and the geography does the work the accounting will not.” Recommend restoring it.")],
56: [(S, "The unnamed Fox Hill man. Close to the other two.")],
60: [(B, "“This book counts what the surrounding economy has been accepting from him.”"), (OM, "The guess is out, by your call 3a.")],
61: [(S, "The islands and Hampton. The pace draft is a little better: this one falls into runs of same-shaped sentences in 67."), (AD, "The two-sentence bridge. Keep.")],
63: [(OM, "“The whole package, in his words.” Recommend restoring it inside the quotation.")],
65: [(Q, "Does Tilghman earn its place?")],
67: [(I, "“They are asked… They are asked… They are asked…” The pattern you went back to the tighter version for in Chapter 5.")],
68: [(S, "The children. The marina scene is out (call 3c)."), (Q, "The daughter in nursing school in Norfolk: did you hear this?")],
69: [(B, "“They will not teach a son into a trade when they cannot promise him it will support him.”")],
73: [(S, "The paradox. Even with the pace draft."), (AD, "Seven words in place of the announcement. Keep.")],
77: [(I, "“In that same year.” The sources on file say August 2025 and February 2026.")],
80: [(I, "“an accounting is beginning to recover what was lost.” Still not clear. What accounting?")],
81: [(AD, "The closing question. Keep.")],
82: [(S, "The reef column. My pick for the arithmetic (84, 85, 87, 88) and for the credit paragraph (91).")],
85: [(B, "The floor in steps: the acres, the cost per acre, the product, and then the higher figure.")],
86: [(OM, "“It was the fee Hampton charged to ship its own wealth away.” Recommend restoring it.")],
87: [(B, "Mazzucato and Harvey in short sentences."), (OM, "“Value goes up and out. Cost stays and settles down.” Recommend restoring it.")],
88: [(I, "244 words. Break at “These two sets of numbers measure different things.”"), (AD, "The one-river and whole-Bay sentences. Required. Keep."), (AD, "“One party is missing from that list.” A join I added.")],
89: [(Q, "“severed” appears nowhere in this draft. Should it appear here?")],
91: [(B, "“I did not invent this move.”")],
93: [(S, "The ending. Same as the pace draft, a little longer."), (OM, "“The thinning comes in stages…” Recommend restoring that one sentence here.")],
94: [(I, "176 words. Prefer the current chapter's two paragraphs.")],
96: [(I, "“is not a resource. It is a position.” Prefer the current chapter's one sentence.")],
98: [(B, "Word for word the current chapter.")],
}

VERSIONS = [
 ('Ch3_A_current_annotated', 'Chapter 3 · A · current chapter (promoted June 2026)', 'manuscript/chapters/Chapter__3_TheWaterman.md', NA, 'A',
  "Best on Biggie, on your own memories, and on a handful of single sentences that both drafts lost. It repeats the McDowell comparison six times, states the reef floor three times, and argues with an imagined critic through the reef column. OMITTED notes mark what the two drafts leave out, with a recommendation on each."),
 ('Ch3_B_pace_annotated', 'Chapter 3 · B · pace draft (Nov 14)', D + 'ch03-pace_2026-11-14.md', NB, 'B',
  "The quickest read. Best in more paragraphs than either of the others, mostly by small margins. Its weak spots: one very long crab paragraph, a few good lines from the current chapter lost, and three handoff questions that may read as a habit."),
 ('Ch3_C_dinner-table_annotated', 'Chapter 3 · C · dinner-table draft (Nov 14)', D + 'ch03-dinner-table_2026-11-14.md', NC, 'C',
  "The easiest to follow where the chapter explains something: the three causes of the oyster's collapse, why the damage is permanent, the rockfish politics, the reef arithmetic. Flatter than the others in the scenes, and it has five definitions set inside sentences."),
]

CSS = '''@page{size:letter;margin:0.6in 0.5in 0.7in}
body{font-family:"EB Garamond",Georgia,serif;font-size:11.3pt;line-height:1.42;color:#111;margin:0}
h1{font-size:16pt;margin:0 0 3pt} .sum{font-size:10.6pt;margin:0 0 6pt}
.legend{font-family:"DejaVu Sans",Arial,sans-serif;font-size:7.6pt;line-height:1.45;border:0.6pt solid #666;padding:5pt 7pt;margin:0 0 7pt}
table{width:100%;border-collapse:collapse;table-layout:fixed}
col.n{width:0.3in} col.t{width:4.45in} col.m{width:2.75in}
td{vertical-align:top;padding:0 0 7pt}
td.n{font-family:"DejaVu Sans",Arial,sans-serif;font-size:6.8pt;color:#777;padding-top:3pt}
td.t{padding-right:0.16in} td.t p{margin:0}
td.m{font-family:"DejaVu Sans",Arial,sans-serif;font-size:7.5pt;line-height:1.38;border-left:0.5pt solid #999;padding-left:0.11in}
.k{font-weight:bold;letter-spacing:0.03em;font-size:6.9pt}
.note{margin:0 0 4.5pt} .SECTION{border:0.9pt solid #111;padding:3pt 4pt;margin-bottom:5pt}
.BEST .k{color:#0a5d2a} .ISSUE .k{color:#9a1c1c} .QUESTION .k{color:#1d3f8a} .ADDED .k{color:#7a4a00} .OMITTED .k{color:#5a2d82}
.BEST{border-left:2.2pt solid #0a5d2a;padding-left:4pt} .ISSUE{border-left:2.2pt dashed #9a1c1c;padding-left:4pt} .QUESTION{border-left:2.2pt dotted #1d3f8a;padding-left:4pt}
.ADDED{border-left:2.2pt double #7a4a00;padding-left:4pt} .OMITTED{border-left:2.2pt solid #5a2d82;padding-left:4pt;background:#f4f0f8}
tr.r td{padding:2pt 0 9pt;text-align:center;color:#777}'''

LEGEND = '''<div class="legend"><b>How to read the margin.</b> Small numbers count paragraphs, so you can point to one.
<b>SECTION</b> (boxed): how this section compares with the other versions.
<b style="color:#0a5d2a">BEST</b> (solid green bar): this paragraph, or the line quoted, is the best of the three versions.
<b style="color:#9a1c1c">ISSUE</b> (dashed bar): where I had to reread, where the voice is not yours, or where a fact needs a look.
<b style="color:#1d3f8a">QUESTION</b> (dotted bar): a content question for you.
<b style="color:#7a4a00">ADDED</b> (double bar): in this draft and not in the current chapter, with a recommendation.
<b style="color:#5a2d82">OMITTED</b> (shaded): in the current chapter and not in the drafts, with a recommendation on whether the chapter is stronger without it.
A paragraph with no note read fine and is not remarkable either way. These are one reader's opinions, and that reader wrote drafts B and C.</div>
<div class="legend"><b>How to mark.</b> Pick one copy as your assembly copy. A paragraph with no mark stays.
To take a paragraph from another version, cross the printed number and write the label: “#12 Pace,” “#12 Dinner,” “#12 Current.” “Except last sentence” and “swap 2 sentences” work the same way: circle what stays.
Handwritten words go in at the arrow or caret. Printed words stay unless struck. A struck margin note means the note is rejected. “Cut” beside a crossed paragraph removes it.
Photograph every page you wrote on, in order, and say which pages are unmarked.
<b>Numbers.</b> The pace and dinner-table copies have the same 98 paragraphs, and their numbers line up one for one. The current chapter has 119 paragraphs and its numbers do <b>not</b> line up with the other two; the table in the comparison file gives the match.</div>'''

def fmt(s):
    s = html.escape(s, quote=False)
    return re.sub(r'\*(.+?)\*', r'<i>\1</i>', s)

def build(slug, label, path, notes, letter, summary, outdir):
    raw = re.sub(r'<!--.*?-->', '', open(path).read(), flags=re.S)
    lines = [x.strip() for x in raw.split('\n') if x.strip()]
    rows = ''; n = 0; body = []
    rowmap = {r[0]: r for r in ROWS}
    for x in lines:
        if x.startswith('#') or x.startswith('*By '): continue
        if x == '---':
            if n: rows += '<tr class="r"><td></td><td>* * *</td><td></td></tr>'
            continue
        n += 1; body.append(x)
        ns = list(notes.get(n, []))
        if letter in 'BC' and n in rowmap:
            best = rowmap[n][2]
            has_best = any(k == B for k, _ in ns)
            if best == letter and not has_best:
                ns.append((B, rowmap[n][3]))
            elif best not in ('none',) and letter not in best and len(best) == 1:
                who = {'A': 'the current chapter', 'B': 'the pace draft', 'C': 'the dinner-table draft'}[best]
                ns.append(('PICK', f"Best here: {who}" + (f" (its ¶{rowmap[n][1]})" if best == 'A' else '') + "."))
        m = ''.join(f'<div class="note {k}"><span class="k">{k}</span> {fmt(t)}</div>' if k != 'PICK'
                    else f'<div class="note" style="color:#555">{fmt(t)}</div>' for k, t in ns)
        rows += f'<tr><td class="n">{n}</td><td class="t"><p>{fmt(x)}</p></td><td class="m">{m}</td></tr>'
    bad = [k for k in notes if k > n]
    assert not bad, (slug, bad)
    words = len(' '.join(body).split())
    h = f'''<!doctype html><meta charset="utf-8"><title>{label}</title><style>{CSS}</style>
<h1>{label}</h1><p class="sum">{words:,} words, {n} paragraphs. The text is exactly as the file has it; nothing is edited. {summary}</p>
{LEGEND}
<table><colgroup><col class="n"><col class="t"><col class="m"></colgroup>{rows}</table>'''
    open(f'{outdir}/{slug}.html', 'w').write(h)
    print(slug, words, 'words', n, 'paras', len(notes), 'annotated paras')

def table_md():
    name = {'A': 'Current', 'B': 'Pace', 'C': 'Dinner', 'AB': 'Current or Pace', 'BC': 'Pace or Dinner (same)',
            'ABC': 'Same in all', 'none': 'None'}
    out = ['| Pace / Dinner ¶ | Current ¶ | Best | Why |', '|---|---|---|---|']
    for n, a, b, t in ROWS:
        out.append(f"| {n} | {a} | **{name[b]}** | {t} |")
    tally = {}
    for n, a, b, t in ROWS: tally[b] = tally.get(b, 0) + 1
    order = ['B', 'C', 'A', 'BC', 'AB', 'ABC', 'none']
    out.append('')
    out.append('**Tally of the 98 paragraphs:** ' + '; '.join(f"{name[k]} {tally[k]}" for k in order if k in tally) + '.')
    return '\n'.join(out)

if __name__ == '__main__':
    assert [r[0] for r in ROWS] == list(range(1, 99))
    for v in VERSIONS: build(*v, sys.argv[1])
    p = D + 'ch03-comparison_2026-11-15.md'
    try:
        s = open(p).read()
        s2 = re.sub(r'(<!-- PARA-TABLE-START -->).*?(<!-- PARA-TABLE-END -->)', lambda m: m.group(1) + '\n' + table_md() + '\n' + m.group(2), s, flags=re.S)
        open(p, 'w').write(s2); print('paragraph table written into', p)
    except FileNotFoundError:
        print(table_md())
