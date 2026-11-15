#!/usr/bin/env python3
"""Ch 4 annotated print copies and the paragraph-by-paragraph table (2026-11-15).

Same form as tools/workstream-handoffs/pull-pass_2026-11/annotated-versions_build_2026-11.py
(Chapters 1 and 5): the text exactly as each file has it, a small printed number beside every
paragraph, and a margin column. One label is added to that form at the author's request of
2026-11-14: PICK, on every paragraph, naming the version this reader would take.

Usage (from the repo root):
    python3 tools/workstream-handoffs/chapter-redrafts_2026-11/ch04-annotated_build_2026-11-15.py OUTDIR
writes three HTML files to OUTDIR and prints the paragraph table as markdown.
Print each HTML to PDF with page numbers (Chromium). PDFs are not committed.

The notes are one reader's opinion, and that reader wrote drafts B and C. Nothing is edited.
"""
import html
import re
import sys

D = 'tools/workstream-handoffs/chapter-redrafts_2026-11/'
FILES = {
    'A': 'manuscript/chapters/Chapter__4_TheExistenceProof.md',
    'B': D + 'ch04-pace_2026-11-14.md',
    'C': D + 'ch04-dinner-table_2026-11-14.md',
}
NAME = {'A': 'Current', 'B': 'Pace', 'C': 'Dinner'}
S, B_, I, Q = 'SECTION', 'BEST', 'ISSUE', 'QUESTION'

# One row per paragraph of B and C (their numbers line up one for one).
# (n, [A paragraph numbers that carry the same content], pick, why)
# pick: 'A', 'B', 'C', or 'B/C' when the two drafts are as good as each other.
ROWS = [
 (1, [1], 'B/C', "Same sentence in both drafts. The current version puts two insertions between \"1969\" and \"found oil.\""),
 (2, [2], 'B', "Keeps every detail of the current scene in shorter sentences. Dinner explains why the waves are long, which the scene does not need."),
 (3, [3], 'B', "Ends on \"Not one of them had ever produced a barrel of oil.\" Close to the current version; Dinner is equal."),
 (4, [4], 'A', "\"…is settled by nothing in the rock\" is the best line in the opening, and only the current version has it whole. Pace turns it into two questions, which also works."),
 (5, [5], 'B', "\"uses up what the seabed took a hundred million years to store\" is plainer than \"one generation's consumption absorbs.\""),
 (6, [5], 'B', "Says Alberta is a Canadian province and keeps the two closing lines of the current version."),
 (7, [6, 8], 'B', "The current sentence stacks four insertions (\"enforced, structurally, across five decades, by rules…\"). Pace reads in one pass and ends on the inspection line."),
 (8, [9], 'B', "Unstacks the current $390,000 sentence and keeps \"born downstream of a decision.\" Dinner loses that phrase."),
 (9, [10], 'B', "Clear. \"The name on the door\" is a figure of speech; Dinner's \"that is still its name\" is the plain form if you want it."),
 (10, [10], 'C', "Dinner says what \"at the margin\" means (78 cents of each additional dollar of profit). A general reader needs that, and it is accurate."),
 (11, [11], 'B', "Drops the announcement (\"The revision is worth pausing on, because…\"). Take Dinner's \"the return the fund was expected to earn after inflation\" for \"expected real return.\""),
 (12, [12], 'B/C', "Same content. Dinner says what a barrel of oil equivalent is."),
 (13, [14], 'B', "Opens on the reason the machinery exists. The current version opens \"Then there is the machinery that keeps the machine honest.\""),
 (14, [15, 17], 'B', "Keeps the one long sentence about each generation handing the fortune on. Dinner breaks it into three and it loses force."),
 (15, [18], 'B', "Even with the current version. The commandments get three verbs in one sentence; Dinner gives each its own sentence, which is slower."),
 (16, [19], 'B', "The current paragraph minus its last sentence. The objects are the same in all three."),
 (17, [20], 'B', "Three short questions the section then answers in order."),
 (18, [21], 'C', "Dinner takes the fund-against-rent comparison one step at a time and says what rent is. Pace packs it into two sentences of figures."),
 (19, [27], 'B', "Hartwick at the point where his idea is used. Dinner is equal."),
 (20, [22, 23], 'C', "Narrowly. The objects read the same in both; Dinner's last three sentences say what cost severance is more plainly than \"people downstream in place and in time.\""),
 (21, [], 'C', "New paragraph. Dinner shows the arithmetic a step at a time and says what a floor is."),
 (22, [28], 'B', "\"But a fund compounds money. It does not rebuild a physical resource.\""),
 (23, [30, 31], 'B', "The plain statement of what Norway does and does not prove. Dinner is equal and a little longer."),
 (24, [32], 'B', "Even with the current version, and names West Virginia."),
 (25, [33], 'A', "\"Concede every word, because the concession is the argument\" pulls harder than either draft. One word to check: \"It preys on weakness\" (the drafts say \"finds\")."),
 (26, [34], 'B', "The current paragraph ends on three sentences the ledger retired. Pace ends on the plain fact that no reserve stands."),
 (27, [35], 'B', "Ends on the question the Delta answers. See the note on the current version's last line, which both drafts dropped."),
 (28, [36, 37], 'A', "The current sentence that carries the oil through the hangings, the suspension, the four years and every year since is one long breath. Both drafts cut it in two."),
 (29, [38], 'B', "Full sentences where the current version has a list of fragments."),
 (30, [39], 'B', "Splits the current 193-word paragraph and places the two economists. Dinner's step-by-step transfer pricing is as clear."),
 (31, [39], 'B', "\"The terms of the extraction were older than the country.\""),
 (32, [40], 'B', "Opens on the people. The current version opens \"the tail is the landscape,\" which a reader has to decode."),
 (33, [41], 'B/C', "Same content, equally clear."),
 (34, [42], 'B', "Short, and it ends on the finding."),
 (35, [7], 'B', "The thesis, after the reader has seen both countries."),
 (36, [43], 'B', "States what each country \"comes back with\" under the ledger's account."),
 (37, [44], 'B', "Without the label \"deserves its full voice.\""),
 (38, [45], 'B', "Opens on the voters. Dinner opens \"Consider Alaska first,\" which announces."),
 (39, [46], 'B', "Opens on the crews, as the current version does. Dinner numbers the cases (\"is the second case\"), which reads like a report."),
 (40, [47], 'B', "Same content; Dinner is equal apart from the numbering."),
 (41, [48], 'B', "Puts the city, not the courtyards, in the subject."),
 (42, [49], 'A', "\"Four cases, four scales\" and the last line (\"Architecture, built on purpose, defended over time…\") have a rhythm both drafts flattened."),
 (43, [50], 'B', "Dinner's last sentence is hard to follow (\"…outside the United States, and the United States is the economy…\")."),
 (44, [51, 52], 'B', "Pace's wording, but it is about 230 words in one paragraph. Break it at \"None of this says,\" as the current version does."),
 (45, [54], 'B/C', "The three family sentences are identical in all versions."),
 (46, [55], 'C', "Dinner gives \"a living commons makes more of itself…\" its own sentence. In Pace it sits inside the question as a long aside."),
 (47, [56], 'B/C', "Same in both."),
 (48, [57], 'B', "Even with Dinner. Ends \"It has not replaced the barrel.\""),
 (49, [58], 'B', "Dinner writes \"They are… They are… They are…,\" the run of same-shaped sentences you rejected in Chapter 5."),
 (50, [59], 'C', "\"A real solution for one country. The planet cannot adopt it by copying it.\" Pace joins the two awkwardly."),
 (51, [60], 'B/C', "Nearly the same sentences."),
 (52, [61], 'C', "Dinner's last sentence says why the second kind of place is harder. Pace's trails."),
 (53, [62], 'B', "Take the current version's opening fragments if you like them (\"Two strikes, eleven years apart. Oloibiri, 1958.\")."),
 (54, [63], 'C', "Dinner asks the question outright (\"What would it take to finish the job…?\") before handing off to Chapter 5."),
 (55, [64], 'B/C', "Word for word the same in all three."),
]

# Extra margin notes, by copy and paragraph number in that copy.
XB = {  # notes shown on BOTH the Pace and the Dinner copy (same paragraph numbers)
 1: [(S, "Section 1, Block 2/4. Pace is the best of the three; the current version has the better last paragraph.")],
 5: [(S, "Section 2, what usually happens. Pace.")],
 7: [(I, "MOVED. The current chapter states the thesis here (\"Cost severance is a policy choice…\"). It is now paragraph 35, after the Delta. Recommendation: leave it moved. The reader has seen both countries by then.")],
 8: [(S, "Section 3, the fund. Pace, with Dinner's paragraph 10.")],
 13: [(I, "OMITTED: \"The withdrawal rule is the keel. Around the keel, the rest of the rigging.\" Recommendation: leave out. It sets up a comparison the chapter never uses again."),
      (I, "CHANGED: the current chapter says a change needs \"a supermajority of the Storting.\" No source was found in June. The drafts say \"broad agreement across the parties.\" Yours to rule.")],
 14: [(S, "Section 4, why it held. Pace."),
      (I, "OMITTED: \"A Norwegian born the year of the first deposit turned 30 this year.\" Recommendation: leave out. It dates the book to 2026. It was the only person in the paragraph, so the cost is real but small."),
      (I, "ADDED: the paragraph now ends on \"Why?\"")],
 16: [(S, "Section 5, one barrel. This is the section the ledger changed. Dinner is clearer in the three paragraphs with figures (18, 20, 21); Pace elsewhere."),
      (I, "OMITTED: \"Those objects mark the honest edge of what the fund can and cannot do.\" Recommendation: leave out; the three questions do that job.")],
 18: [(I, "ADDED: about $36 a barrel held, against rent of about $32 to $36. Both from the ledger rows you ratified Nov 12. Recommendation: keep. It is what makes \"Norway kept the rent\" a measured statement."),
      (Q, "An economist will ask whether a 2025 fund balance and fifty years of rent are in the same year's money. Keep as is, or add a clause?")],
 19: [(I, "MOVED: Hartwick came after the honest-pricing passage. It now comes first, because under the ledger the fund is Hartwick's rule and the reader needs that before the unpaid part."),
      (I, "OMITTED: \"Norway's answer is the reserve itself: hold the wealth permanently, and the question of substitution stays open.\" Retired by the ledger. In its place: the fund \"gives Norway the means to pay for repair… It does not make a burned barrel come back.\"")],
 20: [(I, "OMITTED: the flat three-part list (the current chapter carries both versions). Recommendation: leave out; it says the same thing without the objects."),
      (B_, "The only mention of the Technical Appendix in the chapter. The current version names it eight times.")],
 21: [(I, "ADDED, whole paragraph: the carbon cost ($70 a barrel), what is unpaid ($34 a barrel, $1.9 trillion). Recommendation: keep. Without it the chapter claims more for Norway than the ledger allows."),
      (Q, "The floor counts every barrel as burned, and paragraph 16 has just said some become plastics and asphalt. Say \"if burned\"?"),
      (Q, "$190 a ton is one agency's figure. At the older $51 the carbon comes to about $19 a barrel, under the $36 fund. Say so in a clause?")],
 22: [(I, "ADDED: \"The fund does not pay that bill… The fund is rent saved for later generations of Norwegians… no handling of the rent would have paid them.\" From the ledger's account."),
      (I, "OMITTED: the sentence about the word \"yet\" (\"'yet' is doing real work in that sentence\"). Recommendation: leave out; it talks about the prose.")],
 23: [(I, "OMITTED, and they cannot come back as written: \"The loss is made less final,\" \"forecloses once,\" \"buys back optionality,\" \"by orders of magnitude against the Appalachian baseline.\" The ledger retired them. The chapter is less elegant without them and it is true."),
      (I, "ADDED: \"What Norway proves is narrower, and nobody had shown it before: the rent from a commons can be kept whole…\" This sentence now carries the chapter's claim. Check that it says what you mean."),
      (I, "SHORTENED: the scope note. Gone: \"nothing here says all extraction everywhere severs costs, or that renewable harvests are innocent by nature.\" Recommendation: leave shortened.")],
 24: [(S, "Section 6, \"Norway was special.\" Pace, with the current version's paragraph 33 for paragraph 25."),
      (I, "CHANGED: \"arrives on schedule\" is now \"is a fair one.\" That is a judgment the current chapter does not make.")],
 26: [(I, "OMITTED: \"Nothing buys back any part of the finality. The loss arrives final and stays final, and honest pricing charges the full premium for forever.\" Retired with the Norway account.")],
 27: [(I, "OMITTED: \"The building is the part that travels.\" Recommendation: put it back, before the question. It is plain, and it is the idea the four cases later prove."),
      (I, "ADDED: the closing question.")],
 28: [(S, "Section 7, the Delta. The current version for the first paragraph; Pace for the rest.")],
 30: [(I, "ADDED: two sentences naming Zucman and Ndikumana and Boyce (Insertion M, ratified in June). Recommendation: keep. A book about measurement should say who measured this. Not yet fact-checked: see the ledger list.")],
 34: [(I, "OMITTED: \"that could buy back any part of the finality, so the foreclosure arrived total and stayed total.\" Retired.")],
 35: [(I, "ADDED: three sentences that set the two countries side by side before the thesis. The thesis words are yours, from the current paragraph 7.")],
 36: [(I, "CHANGED: the current chapter says Norway \"comes back with a small severed cost.\" The ledger's floor is about $1.9 trillion, so the drafts say \"its rent kept and a carbon bill unpaid.\"")],
 37: [(S, "Section 8, \"It could never work here.\" Pace for the four cases; the current version for the summing-up (paragraph 42)."),
      (I, "ADDED: \"wherever here happens to be,\" so that \"here\" is not a country."),
      (Q, "Only Alaska is about a resource. Do all four cases stay at full length here, or does Alaska stay and the others shrink or wait for Chapter 9?")],
 38: [(I, "CHANGED: \"roughly three votes to one\" is now \"roughly two votes to one\" (66 percent yes). Yours to rule."),
      (I, "OMITTED: \"The objection now has to explain Alaska first,\" and \"The objection now has to explain Tennessee\" in the next paragraph. Recommendation: leave out. Paragraph 42 makes the point once for all four.")],
 39: [(I, "CHANGED: \"three years before Google Fiber\" is now \"ahead of\"; the chapter's own dates are 2010 and 2012.")],
 40: [(I, "CHANGED: \"roughly 80,000 worker-owners across some 95 cooperatives\" is now \"about 70,500 people working in 92 cooperatives\" (the federation's 2023 report). Yours to rule.")],
 43: [(S, "Section 9, Social Security. Pace, broken into three paragraphs.")],
 44: [(I, "OMITTED: \"depleted around 2034… roughly 81 percent.\" Recommendation: leave out. Chapter 5, which you have ratified, says 2033 and 77 percent; two different pairs in one book would look like an error."),
      (I, "OMITTED: the paragraph on what an American worker already pays (\"less a new bill than an honest reprinting of one that already arrives\"). Recommendation: leave out. It has no sourced figure behind it. The last image is good; it could return if a figure is found.")],
 45: [(S, "Section 10, the oyster. Even; Dinner for paragraph 46."),
      (Q, "The three sentences about your father and Fox Hill came from the June redraft. Are they yours as written?")],
 47: [(S, "Section 11, four gaps. Pace, with Dinner's paragraphs 50 and 52."),
      (I, "OMITTED: \"Each one is a debt the later chapters owe.\" Recommendation: leave out; paragraph 52 says what remains.")],
 48: [(I, "REWRITTEN: the current paragraph says the fund \"attacks the finality of the loss.\" Retired. The gap itself (the barrel is not replaced) is kept.")],
 49: [(I, "REORDERED: the people come first, then the carbon, then the North Sea.")],
 51: [(I, "REWRITTEN: gone are \"preserves restoration optionality as a side effect,\" \"bought insurance on part of the future,\" and the term Intergenerational Option Value.")],
 53: [(S, "Section 12, two strikes. Pace, with Dinner's paragraph 54.")],
 54: [(I, "ADDED: \"Norway did not finish the job. Its carbon bill is unpaid, and the people it falls on live a long way from Oslo.\""),
      (I, "CHANGED: the hand-off. The current chapter promises Libby, the Deepwater Horizon, the Exxon Valdez and Baotou. Chapter 5 now opens with a family in Connecticut, so the drafts point there."),
      (I, "OMITTED: the second statement of \"Cost severance is a policy choice.\" It is said once, at paragraph 35.")],
}
XC = {  # Dinner copy only
 7: [(I, "ADDED in this draft only: \"Because all of it was done in the open.\" A reason the current chapter does not give.")],
 8: [(I, "\"The child was simply born after a decision that other people made\" loses \"downstream.\"")],
 10: [(B_, "The definition of the marginal rate.")],
 14: [(I, "Three short sentences where the other versions have one.")],
 20: [(B_, "\"In plain terms, take the full value that was used up and subtract what was actually set aside.\"")],
 21: [(B_, "\"Multiply the two…\" Each step of the arithmetic has its own sentence.")],
 38: [(I, "\"Consider Alaska first… is the second case… The third case… The fourth case.\" The numbering is this draft's and can come out.")],
 43: [(I, "The last sentence needs a second read.")],
 49: [(I, "\"They are… They are… They are…\"")],
}
XP = {  # Pace copy only
 4: [(I, "\"settled by nothing in the rock\" became \"Nothing in the rock answers either question.\"")],
 9: [(I, "\"the name on the door\" is a figure of speech.")],
 28: [(I, "The oil sentence is split in two here.")],
 42: [(I, "Flatter than the current version's \"Four cases, four scales.\"")],
 44: [(I, "About 230 words in one paragraph.")],
 46: [(I, "The question carries a long aside (\"one that makes more of itself as long as…\").")],
 49: [(B_, "One sentence, three peoples, the Pacific islands last.")],
}
XA = {  # Current copy only, by A paragraph number
 1: [(S, "Section 1. Two insertions slow the first sentence; the fourth paragraph is the best of any version.")],
 4: [(B_, "\"…is settled by nothing in the rock.\"")],
 5: [(S, "Section 2. One paragraph here; the drafts break it before Alberta.")],
 6: [(I, "Four insertions in one sentence (\"enforced, structurally, across five decades, by rules…\").")],
 7: [(Q, "The thesis, before the reader has seen either country. Both drafts hold it until after the Delta (their paragraph 35). Recommendation: move it.")],
 9: [(S, "Section 3."), (I, "The $390,000 sentence has five commas and two sources inside it.")],
 11: [(I, "\"The revision is worth pausing on, because…\" announces.")],
 13: [(Q, "June's keel-and-rigging line. OMITTED from both drafts on your answer. Recommendation: leave out.")],
 14: [(I, "\"a supermajority of the Storting\": no source found in June.")],
 15: [(S, "Section 4.")],
 16: [(Q, "\"turned 30 this year.\" OMITTED from both drafts. Recommendation: leave out; it dates the book.")],
 17: [(I, "\"cannot agree on the time of day\" is an idiom.")],
 19: [(S, "Section 5. From paragraph 24 on, this section rests on an account of Norway the ledger retired on Nov 11. It cannot be taken as it stands.")],
 22: [(Q, "The flat list. OMITTED from both drafts in favor of the objects (next paragraph). Recommendation: leave out.")],
 24: [(I, "RETIRED by the ledger: \"The loss is made less final.\" A fund does not make a burned barrel restorable.")],
 25: [(I, "RETIRED: \"Norway's forecloses once.\"")],
 26: [(I, "RETIRED: \"lowers the effective irreversibility,\" \"buys back optionality,\" and \"the deeper reason Norway's severed cost runs so far below Appalachia's.\"")],
 27: [(I, "\"There is a lineage worth naming here, briefly\" announces. The last three sentences rest on the retired account.")],
 28: [(B_, "\"But compound interest does not reconstitute a physical resource.\" Kept in substance in both drafts."), (I, "\"'yet' is doing real work in that sentence\" talks about the prose.")],
 29: [(Q, "OMITTED from both drafts. \"What Norway internalized per barrel… is a floor\" used the old $48 reading. The drafts' floor is the unpaid carbon (their paragraph 21).")],
 30: [(I, "RETIRED: \"by orders of magnitude against the Appalachian baseline.\" The ledger puts Norway's unpaid cost at a floor of about $1.9 trillion.")],
 31: [(I, "\"One scope note, so the claim stays the right size\" is a label. Both drafts fold the note into two sentences.")],
 32: [(S, "Section 6.")],
 33: [(B_, "\"Concede every word, because the concession is the argument.\" Better than either draft.")],
 34: [(I, "The last four sentences are RETIRED (\"buys back any part of the finality\"; \"the premium for forever\").")],
 35: [(B_, "\"The building is the part that travels.\" Both drafts dropped it. Recommendation: keep it.")],
 36: [(S, "Section 7."), (B_, "\"Through the day of the hangings, and the day of the suspension, and the four years between, and every year since, the oil kept moving.\"")],
 39: [(I, "193 words in one paragraph. The drafts split it and add two sentences naming the economists who measured the leakage.")],
 40: [(I, "\"the tail is the landscape\" has to be decoded.")],
 42: [(I, "RETIRED wording: \"buy back any part of the finality.\"")],
 43: [(I, "\"Norway comes back with a small severed cost\" no longer matches the ledger.")],
 44: [(S, "Section 8."), (I, "\"deserves its full voice\" is a label.")],
 45: [(I, "\"roughly three votes to one\": the certified result was about two to one (66 percent)."), (Q, "\"The objection now has to explain Alaska first.\" OMITTED from both drafts. Recommendation: leave out.")],
 46: [(I, "\"three years before Google Fiber… 2012\": the launch date given is about 2010.")],
 47: [(I, "\"roughly 80,000 worker-owners across some 95 cooperatives\": the 2023 report says 70,500 people and 92.")],
 49: [(B_, "\"Four cases, four scales…\" and the last line. Better than either draft.")],
 50: [(S, "Section 9.")],
 51: [(Q, "\"depleted around 2034… roughly 81 percent.\" OMITTED from both drafts. Chapter 5 says 2033 and 77 percent. Recommendation: leave out here.")],
 53: [(Q, "OMITTED from both drafts: no sourced figure behind \"a substantial share of every paycheck.\" Recommendation: leave out unless a figure is found.")],
 54: [(S, "Section 10.")],
 55: [(I, "209 words; \"only, and crucially\" is an aside that fails your deletion test.")],
 56: [(S, "Section 11.")],
 57: [(I, "RETIRED wording: \"The architecture attacks the finality of the loss.\"")],
 58: [(I, "\"The second is the tail\": the people arrive four sentences in. Both drafts put them first.")],
 60: [(I, "RETIRED wording: \"preserves restoration optionality as a side effect,\" \"bought insurance on part of the future.\"")],
 62: [(S, "Section 12."), (B_, "The opening fragments."), (I, "RETIRED wording: \"keeps repair and substitution open,\" \"driven down toward the honest floor.\"")],
 63: [(I, "The hand-off promises Libby, the Deepwater Horizon, the Exxon Valdez and Baotou. Chapter 5 now opens with a family."), (I, "RETIRED wording: \"blunts the finality of the loss itself.\"")],
}

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
.BEST .k{color:#0a5d2a} .ISSUE .k{color:#9a1c1c} .QUESTION .k{color:#1d3f8a}
.BEST{border-left:2.2pt solid #0a5d2a;padding-left:4pt} .ISSUE{border-left:2.2pt dashed #9a1c1c;padding-left:4pt} .QUESTION{border-left:2.2pt dotted #1d3f8a;padding-left:4pt}
.PICK{background:#eee;padding:2pt 4pt}
tr.r td{padding:2pt 0 9pt;text-align:center;color:#777}'''

SUMMARY = {
 'A': "The chapter on main, promoted in June and not yet redlined by you. Its paragraph numbers do NOT line up with the two drafts: this copy has 64, the drafts have 55 each, and three passages sit in a different place. Each PICK note gives the matching draft number. From paragraph 24 on, the \"One barrel\" section rests on an account of Norway that the ledger retired on Nov 11; those sentences are marked RETIRED.",
 'B': "My suggestion for the assembly copy. Paragraph numbers match the Dinner copy one for one, and do not match the Current copy (each PICK note gives the Current number). I would take 8 paragraphs from Dinner (10, 18, 20, 21, 46, 50, 52, 54) and 4 from Current (its 4, 33, 36–37 and 49).",
 'C': "Paragraph numbers match the Pace copy one for one, and do not match the Current copy. Clearer than Pace where the chapter does arithmetic or introduces a term (10, 18, 20, 21). Elsewhere it is longer without being clearer, and in a few places it breaks a good sentence into short ones.",
}
LEGEND = '''<div class="legend"><b>How to read the margin.</b> Small numbers count paragraphs.
<b>PICK</b> (grey, on every paragraph): the version I would take for this paragraph, and why.
<b>SECTION</b> (boxed): how the section compares across versions.
<b style="color:#0a5d2a">BEST</b> (solid bar): a line worth keeping.
<b style="color:#9a1c1c">ISSUE</b> (dashed bar): where I had to reread, or where something was ADDED, OMITTED, MOVED or CHANGED against the current chapter, with a recommendation.
<b style="color:#1d3f8a">QUESTION</b> (dotted bar): a content question for you.
These are one reader's opinions, and that reader wrote the Pace and Dinner drafts, so weigh its preference for them accordingly. Nothing in the text has been edited.</div>
<div class="legend"><b>How to mark (your convention).</b> Pick one copy as the assembly copy. A paragraph with no mark stays.
To take a paragraph from another version, cross the printed number and write the label: "#12 Pace," "#12 Dinner," "#12 Current." "Except last sentence" and "swap 2 sentences" work the same way: circle what stays.
Handwritten words go in at the arrow or caret. Printed words stay unless struck. A struck margin note means the note is rejected. "Cut" beside a crossed paragraph removes it.
Photograph every page of every copy you wrote on, in order, and say which pages are unmarked.</div>'''


def fmt(s):
    s = html.escape(s, quote=False)
    return re.sub(r'\*(.+?)\*', r'<i>\1</i>', s)


def paras(path):
    raw = re.sub(r'<!--.*?-->', '', open(path, encoding='utf-8').read(), flags=re.S)
    out = []
    for x in [l.strip() for l in raw.split('\n') if l.strip()]:
        if x.startswith('#') or x.startswith('*By '):
            continue
        out.append(x)
    return out


def a_to_bc():
    m = {}
    for n, a, pick, why in ROWS:
        for k in a:
            m.setdefault(k, []).append(n)
    return m


def pick_text(copy, n):
    """The PICK line for paragraph n of the given copy."""
    def lab(pick, bc, a):
        if pick == 'A':
            return 'Current #' + ', #'.join(str(k) for k in a)
        if pick == 'B/C':
            return f'Pace or Dinner #{bc} (equal)'
        return f'{NAME[pick]} #{bc}'
    if copy in 'BC':
        _, a, pick, why = ROWS[n - 1]
        where = ('Current #' + ', #'.join(str(k) for k in a)) if a else 'not in Current'
        return f'{lab(pick, n, a)}. {why} [{where}]'
    rows = [r for r in ROWS if n in r[1]]
    if not rows:
        return None
    return ' / '.join(f'{lab(p, bn, a)}. {why}' for bn, a, p, why in rows)


def build(copy, outdir):
    body = paras(FILES[copy])
    extra = {'A': [XA], 'B': [XB, XP], 'C': [XB, XC]}[copy]
    rows = ''
    n = 0
    for x in body:
        if x == '---':
            if n:
                rows += '<tr class="r"><td></td><td>* * *</td><td></td></tr>'
            continue
        n += 1
        notes = []
        for d in extra:
            notes += [t for t in d.get(n, []) if t[0] == S]
        p = pick_text(copy, n)
        if p:
            notes.append(('PICK', p))
        elif copy == 'A':
            notes.append(('PICK', 'Not in either draft. See the note below.'))
        for d in extra:
            notes += [t for t in d.get(n, []) if t[0] != S]
        m = ''.join(f'<div class="note {k}"><span class="k">{k}</span> {fmt(t)}</div>' for k, t in notes)
        rows += f'<tr><td class="n">{n}</td><td class="t"><p>{fmt(x)}</p></td><td class="m">{m}</td></tr>'
    expect = {'A': 64, 'B': 55, 'C': 55}[copy]
    assert n == expect, (copy, n)
    words = len(' '.join(y for y in body if y != '---').split())
    label = {'A': 'Chapter 4 · CURRENT · the chapter on main (promoted June 16)',
             'B': 'Chapter 4 · PACE · pace-and-pull draft (Nov 14)',
             'C': 'Chapter 4 · DINNER · dinner-table draft (Nov 14)'}[copy]
    h = f'''<!doctype html><meta charset="utf-8"><title>{label}</title><style>{CSS}</style>
<h1>{label}</h1><p class="sum">{words:,} words, {n} paragraphs. The text is exactly as the file has it. {SUMMARY[copy]}</p>
{LEGEND}
<table><colgroup><col class="n"><col class="t"><col class="m"></colgroup>{rows}</table>'''
    slug = {'A': 'Ch4_CURRENT_annotated', 'B': 'Ch4_PACE_annotated', 'C': 'Ch4_DINNER_annotated'}[copy]
    open(f'{outdir}/{slug}.html', 'w', encoding='utf-8').write(h)
    return slug, words, n


def table_md():
    out = ['| # (Pace and Dinner) | Current # | Pick | Why |', '|---|---|---|---|']
    for n, a, pick, why in ROWS:
        cur = ', '.join(str(k) for k in a) if a else 'new'
        p = {'A': '**Current**', 'B': 'Pace', 'C': '**Dinner**', 'B/C': 'Pace or Dinner'}[pick]
        out.append(f'| {n} | {cur} | {p} | {why} |')
    return '\n'.join(out)


if __name__ == '__main__':
    assert [r[0] for r in ROWS] == list(range(1, 56))
    if len(sys.argv) > 1 and sys.argv[1] == '--table':
        print(table_md())
    else:
        for c in 'ABC':
            print(*build(c, sys.argv[1]))
        tally = {}
        for r in ROWS:
            tally[r[2]] = tally.get(r[2], 0) + 1
        print(tally)
