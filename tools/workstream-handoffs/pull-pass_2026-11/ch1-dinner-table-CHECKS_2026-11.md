# Ch 1 dinner-table draft: checks and change notes (2026-11-12)

**Status:** PROPOSED (internal). Draft: `ch1-dinner-table_2026-11.md`. Content source:
`manuscript/chapters/Chapter__1_TheQuietMath.md` (unchanged). `ch1-pace-redraft_2026-11-10.md` was not read.
This file reports what was done. It does not say which version is better.

## What changed in kind

Most of this chapter already sounds like a person talking, and much of it is the author's own hand redline, so
274 of the source's 359 sentences are carried over exactly. The changes are in the passages he did not rewrite:
sentence fragments were joined into full sentences, a few literary turns were said plainly ("the moment the
company decided it no longer wished to hold the other end of the cord", "As a flinch", "Seeing became a method",
"the patient ordinary machinery of salaried invention", "The bone-sense was inherited", "the skill and the price
are the same thing seen from two sides"), and long sentences with several insertions were split at their turns.
Nothing was added: no new detail, feeling, reaction or memory.

## Word counts (hidden comments excluded)

| | Words |
|---|---|
| Source | 6,460 |
| Draft | 6,577 |
| Change | +117 (+1.8%) |

## Check 2: protected words, string for string

All present and identical to the source (checked by script):

- The colleague: "you do not really see a city from inside it… and which it flowed past."
- The grandfather: the drill bits "were getting dull… not ready to use"; "the compressor's engine had given out on
  him"; "he had machined new pistons and new rings and rebuilt the engine"; "Those are good to go now, he said."
- The father: "my life was my own… the choice and the life were mine"; the ditch sentence, ending "no one had
  ever dug a better ditch"; "pride in your own work… they will never know it was you that did it"; "Before I get
  up, when I go to check the work, will you be proud of what I am about to see?"; "the best part of any trip is
  the journey"; "Pou it is, he said".
- The children: "Wait, we said. Wait, do not get up yet. Let us do a quick walk through."
- The nephew: "momma", "Uncle Chris", "Pou".
- The station worker's storm line; the Chicago worker's terms; the nurses' words; the economist's sentence.
- The author's own lines "Now I can't unsee it.", "But that is not my story to tell.", "Anyway, sure, the house
  was beautiful."
- The one quoted string in the source, and the hidden citation-pin comment, unchanged.
- The compressor, ditch, chore, hunting, room, nephew, hospital and marriage paragraphs are word for word.

## Check 3: corpus invariants

`bash tools/scripts/check-corpus-invariants.sh`: **HIGH = 0** (exit 0).
`check-prose-clarity.py` on the draft, for information only: HIGH 1, MEDIUM 9, LOW 1 (source: HIGH 3, MEDIUM 16,
LOW 1). The one HIGH is the hospital paragraph, which carries the nurses' words and the author's own redline and
was left exactly as it is.

## For the comparison session and the author

- **The road.** `<!-- THE ROAD: the author's section, to be written by him -->` sits after the work section
  ("…and it would cost me my marriage.") and before the section that begins "By the time I was deep into my best
  years". Nothing is written there.
- **The United States is named** once, in the colleague's paragraph ("His right to remain in the United States
  was tied to his job"), where the source has "the country".
- **The one sentence of his that was split:** the cable-station sentence that ran from the parking lot to the lost
  clients is now two sentences ("…lit from inside. The broadcast was running on a queue…"). His words are the
  same.
- **The former spouse:** the marriage paragraph is unchanged. Nothing was added anywhere.
- **Changed for the no-repeat rule (style sheet rule 11):** "I could not unsee the shape of it" in the lease
  section became "I could not stop noticing it", so that "Now I can't unsee it." is said once.
- **Carried over unchanged, worth a look at the redline:** "There was no villain in this. There almost never is."
  (see the author's 2026-11-12 note that sometimes there is one); "the decisions we made" in the close (an
  unnamed "we"); the Tubman paragraph, which is left in the source's words except that its first sentence is now
  three.

## Check 1: figures

Every figure in the source is in the draft, in the same written form, and the draft has no figure the source
lacks. Counts are occurrences.

| Figure (as written) | In source | In draft | Same? |
|---|---|---|---|
| 1 | 1 | 1 | yes |
| 1958 | 1 | 1 | yes |
| eight | 1 | 1 | yes |
| eleven | 1 | 1 | yes |
| eleven and | 1 | 1 | yes |
| fifteen | 3 | 3 | yes |
| fifty | 1 | 1 | yes |
| fifty-eight | 1 | 1 | yes |
| fifty-two | 1 | 1 | yes |
| five | 4 | 4 | yes |
| forty | 2 | 2 | yes |
| forty-eight | 1 | 1 | yes |
| hundred and sixty-eight | 1 | 1 | yes |
| hundred and thirty-eight | 1 | 1 | yes |
| hundred and twenty | 1 | 1 | yes |
| million | 1 | 1 | yes |
| million and | 1 | 1 | yes |
| million and a half and | 1 | 1 | yes |
| seven | 5 | 5 | yes |
| six | 1 | 1 | yes |
| thirteen hundred | 5 | 5 | yes |
| thirty-six | 1 | 1 | yes |
| thirty-six hundred | 2 | 2 | yes |
| three hundred | 2 | 2 | yes |
| twenty | 1 | 1 | yes |
| twenty-two | 1 | 1 | yes |
| two and a half | 3 | 3 | yes |
| about half of what | 2 | 2 | yes |
| two and a half hours | 3 | 3 | yes |
| three or four | 1 | 1 | yes |
| two or three mornings | 1 | 1 | yes |
| seven or eight years | 1 | 1 | yes |
| three generations | 2 | 2 | yes |
| mid-twenties | 1 | 1 | yes |
| top one to two percent | 1 | 1 | yes |
| a year past due | 1 | 1 | yes |
| another year and another million | 1 | 1 | yes |
| a year or so | 1 | 1 | yes |
| A week or two | 1 | 1 | yes |
| three hours and then half an hour | 1 | 1 | yes |
| three days | 1 | 1 | yes |
| three months | 3 | 3 | yes |
| two years | 2 | 2 | yes |
| about two years | 1 | 1 | yes |
| twenty-something | 1 | 1 | yes |
| decade-old | 1 | 1 | yes |
| over a century | 1 | 1 | yes |
| five days a week, six | 1 | 1 | yes |
| less than five days | 1 | 1 | yes |
| three weeks back to back | 1 | 1 | yes |
| one year, about a million | 1 | 1 | yes |

Distinct figures: 51 in source, 51 in draft; missing or new: 0.
