---
name: Em-dashes as Claude-prose crutch — calibrate critically when drafting + auditing
description: Author flagged 2026-05-21 that em-dashes are a Claude-prose crutch. AMENDED 2026-11-09 by the author's redline — the goal is one-pass readability, not a dash count. Never swap a dash for commas that can't carry the structure; restructure instead. At most one dash pair per paragraph.
type: feedback
---

# Em-dashes as Claude-prose crutch — calibrate critically (ratified 2026-05-21)

**The rule:** When drafting publisher-facing prose for Commons Bonds, treat em-dashes as a flagged punctuation choice rather than a default. Default toward smoother prose using commas, periods, or restructured syntax. When you DO use an em-dash, you should be able to articulate the specific work it's doing (parenthetical extension; deliberate breath-mark; punch-emphasis at a load-bearing pivot) that a comma or period would not do.

**Why:** Ratified 2026-05-21 during Ch 3 Stage-3 Pass 3.2 voice-polish interactive ratification (Phase C application session). When the author dispositioned F-V3 (Stage 1a M2 carry-forward em-dash density at Ch 3 line 38), the explicit feedback was: *"write smoother prose. Emdashes seem to be turning into a bit of a crutch for you. Try writing this without any of them."* The specific sentence was "Take some — leave the rest — let the rest spawn — come back next year." (three em-dashes in 13 words). The author's preferred resolution was full removal: "Take some, leave the rest to spawn, and come back next year."

This is broader feedback than the single sentence. It applies across all prose Claude generates for Commons Bonds — drafting (Stage 2 augmentation; new chapter prose; essay drafts) AND auditing (Pass 3.2 voice-polish recommendations should bias more aggressively toward em-dash-removal options when surfacing density findings).

**Compatible with existing rigor:**
- Ch 1 Pass 3.2 (v2.0 Amendment B canonical artifact) already flagged em-dash density at multiple locations (F-V4 line 29 + F-V8 line 69). The Ch 1 ratification applied em-dash reduction at both (F-V4 Option B compressed appositive; F-V8 Options A + C dropped em-dash count from 4 to 2). This feedback codifies what Ch 1 already enacted: em-dash reduction is the right Pass-3.2 default disposition, not just a per-instance call.
- Cumulative chapter-wide em-dash density is editor-visible across multiple chapters; the feedback applies cumulatively, not just per-sentence.

**How to apply:**

1. **In drafting (Stage 2 + new prose generation):** When a sentence wants an em-dash, first try comma or period. If those don't work, restructure the sentence rather than reaching for the em-dash. Em-dashes should appear when the specific work (sudden interruption; deliberate breath-mark; emphatic punch at chapter-spine pivot) is load-bearing AND a comma/period/restructure would actually lose meaning.

2. **In Pass 3.2 voice-polish audits:** When surfacing em-dash density findings, default Recommendation should bias toward removal/reduction options rather than PRESERVE-as-is, unless the cadence-enactive function is clearly load-bearing AND no alternative restructure preserves the function. Don't lean on Ch 1 F-V7 "cadence-enacts-content" precedent reflexively; the precedent supports holding only when the rhythm cannot be achieved through smoother prose.

3. **In ratification artifacts:** When proposing options on em-dash findings, include a "smoother prose / no em-dashes" Option as a named choice (not just as an implicit alternative), so the author can pick the smoother option without having to specify a custom rewrite.

4. **Cumulative-chapter em-dash audit:** When auditing a chapter for Pass 3.2, count em-dashes chapter-wide (not just per-sentence density). High cumulative chapter count is itself a voice-polish concern even when individual instances are defensible.

**Empirical anchor:**
- Ch 3 line 38 (2026-05-21 ratification): "Take some — leave the rest — let the rest spawn — come back next year." → "Take some, leave the rest to spawn, and come back next year." Pass 3.2 artifact had recommended PRESERVE-AS-IS based on Ch 1 F-V7 cadence-enactive precedent; author overrode toward smoother prose with em-dash removal. This is the canonical empirical example of the rule.

---

## AMENDED 2026-11-09 — the goal is one-pass readability, not a dash count (author)

**What went wrong.** The original rule said: try a comma or period, and if that doesn't work,
restructure. Drafting did the first half only. Em-dashes were swapped for commas even where commas
can't show where an insertion starts and ends. By 2026-11 every chapter had zero em-dashes, and the
Ch 5 rebuild drafts read badly. The author's anchor (redline of the Variant B printout, p. 1,
2026-11-09): "There is a pattern that, once you have seen it clearly, you cannot stop seeing" breaks
the reading thread, even though it is grammatical.

**The rule now (supersedes "default toward commas"):**

1. Every sentence must be readable in one pass.
2. Never split a clause at its joint with an insertion: not between subject and verb, and not between
   "that/which/who" and the rest of its clause. Put the insertion first or last, or give it its own
   sentence. The author's model fix: "Once you have seen a pattern, you start noticing it everywhere."
3. An insertion set off by commas must lift out cleanly and must not contain commas itself. A list
   inside an insertion gets parentheses or a colon, or becomes its own sentence.
4. Em-dashes are allowed when they are the clearest choice: at most one pair per paragraph, never
   three close together (the gate still flags that). The crutch warning stands.
5. Never fix a dash by swapping in commas. Restructure, and when in doubt, split the sentence.

**No sentence-length rule (corrected 2026-11-09, author).** An earlier draft of this amendment
added "prefer sentences under 35 words." The author never asked for that, and it was removed. Drafting
to it produced round-2 Ch 5 drafts averaging 14 words a sentence with zero sentences over 35 words,
clipped against the author's own Ch 1 (18 average, 44 over 35). This is the same failure Amendment E
names: a maximum that reaches the drafter manufactures compression. **Long sentences are fine. What
the rule forbids is splitting a clause with an insertion, or an insertion containing its own commas.**

**Checks.** `tools/scripts/check-prose-clarity.py` flags interrupted clauses (`intr`). Its
sentence-length and `stack` counts are after-the-fact editing aids for locating tangles, never a
drafting target. Do not draft toward zero on them.

---

## CLARIFIED 2026-11-11 (author): comma insertions are fine; there is no ban on splitting a clause

Items 2 and 3 of the 2026-11-09 amendment above overstated the author's mark. His words (2026-11-11):
"I'm perfectly happy with long sentences, which use comma insertions, being used. I only commented on it
the other day as a run on sentence I was reviewing from a prior draft had at least 3 different comma
insertions and that's just bad punctuation in clunky prose."

**What holds now.** One-pass readability is the test (item 1). Long sentences are fine, with or without
insertions. What to fix is a run-on that stacks several insertions so the reader loses the thread; fix it
by moving an insertion or splitting the sentence. Items 4 and 5 (dashes allowed when clearest; never repair
a dash by swapping in commas) stand. `check-prose-clarity.py`'s `intr` count is an editing aid like its
other counts, not a zero target. Current statement of the rule:
`tools/drafting-templates/commons_bonds_house-style-sheet_v1.0.1.md`, rule 1 and override 3.
