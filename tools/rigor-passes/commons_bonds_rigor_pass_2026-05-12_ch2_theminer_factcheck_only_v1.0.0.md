# Commons Bonds — Rigor Pass: Chapter 2 (The Miner) — Stage-3 Phase A (fact-check pass only)

**Date:** 2026-05-12
**Workstream:** Manuscript Stage-3 Rigor Pass (PM dashboard #20)
**Phase:** A — per-chapter Stage-3 audit, Ch 2
**Scope of this artifact:** Pass 1 (fact-check) + Pass 2 (voice-polish), fired same session 2026-05-12. Pass 3 (audience-load) deferred to a follow-up session. Filename retains `_factcheck_only_` slug for git-history continuity; when Pass 3 lands, the artifact will be renamed to `..._stage3_three_pass_v1.0.0.md` per workstream convention.
**File audited:** `manuscript/chapters/Chapter__2_TheMiner__Draft.md` (217 lines, ~5,000w target)
**Canonical sources cross-referenced:**
- `research/literature/bibliography.md` §1, §2, §10, §13 (Harvey 2003, Mazzucato 2018, Keefe 2021, Case & Deaton 2020, Blackley et al. 2018, GAO reclamation reports)
- `research/case-studies/appalachian-coal.md` (Ch 2's case-study brief — verbatim source for much of the chapter prose)
- `research/case-studies/opioid-extraction-appalachia.md` (Ch 2's opioid-section brief)
- `manuscript/chapters/Chapter__2___GuidanceDoc.md` (internal-scaffolding guidance, per-section staleness audit 2026-05-08)
- Commit `8e61cd1` (Cost Severance defense paragraph inserted at line 141, ratified 2026-05-11)
- `tools/workstream-handoffs/manuscript-stage-3-rigor-pass-handoff_2026-05-11.md` (workstream spec)

---

## Pass 1: Fact-check — findings

### CRITICAL

#### C-1. Line 12 — "the first government food distribution program in American history"

**Chapter text (line 12):**
> Families eating surplus commodities — the first government food distribution program in American history, administered right there in the hollows of McDowell County, because there was nothing else.

**Canonical truth:** Surplus commodity distribution was *not* the first government food distribution program in American history. The Federal Surplus Relief Corporation (FSRC) began nationwide surplus food distribution in 1933, twenty-seven years before Kennedy's 1960 visit. The original Food Stamp Plan ran 1939–1943. By 1960, McDowell County families were receiving surplus commodities under a long-established federal program — *not* a first.

**What WAS first in McDowell County:** The pilot food-stamp program signed by JFK via Executive Order 10914 on January 21, 1961. The first recipients were the Muncy family of Paynesville, McDowell County, WV, on May 29, 1961 (even this is "first of the modern program," since the 1939–43 program preceded it).

**Recommended spot-fix:** Drop the false-first claim; keep the imagery.

> Families eating surplus commodities — distributed right there in the hollows of McDowell County, because there was nothing else.

**Propagation:** Same prose at `research/case-studies/appalachian-coal.md` line 20.

#### C-2. Line 41 — "The first food stamps in American history were issued in McDowell County"

**Canonical truth:** First food stamps under the *modern* program (JFK's 1961 pilot, which became SNAP) — yes, McDowell County. But the original Food Stamp Plan operated 1939–1943; McDowell was not first-in-American-history.

**Recommended spot-fix:** Three-word modifier.

> The first food stamps **under the modern program** were issued in McDowell County.

**Propagation:** Same claim at `research/case-studies/appalachian-coal.md` line 47.

#### C-3. Line 193 — "Purdue's 2007 misdemeanor plea on misbranding charges"

**Chapter text (line 193):**
> The litigation record now runs through Purdue's 2007 misdemeanor plea on misbranding charges and the company's 2020 felony plea on three federal counts; Patrick Radden Keefe's *Empire of Pain* (2021) traces the family's role through the documentary record.

**Canonical truth:** In 2007, *The Purdue Frederick Company* (corporate entity) pleaded guilty to a **felony** count of misbranding "with intent to defraud or mislead." Three Purdue executives (CEO Michael Friedman, GC Howard Udell, former CMO Paul Goldenheim) pleaded guilty to **misdemeanor** misbranding (strict-liability, no intent). The chapter inverts the corporate plea (felony) with the executives' pleas (misdemeanor).

**Recommended spot-fix:**

> The litigation record now runs through Purdue's 2007 felony misbranding plea (with three executives pleading guilty to misdemeanor counts) and the company's 2020 felony plea on three federal counts; Patrick Radden Keefe's *Empire of Pain* (2021) traces the family's role through the documentary record.

**Why CRITICAL severity:** This is the kind of named-litigation-record precision a trade-publisher fact-checker (Knopf, FSG, PublicAffairs imprint) will catch in pre-publication review. The chapter's Purdue/Sackler argument depends on the litigation record landing precisely — getting the corporate-vs-executive plea inversion wrong is a credibility wound on the most-load-bearing factual claim in the second-cycle extraction section.

**Propagation:** `research/case-studies/opioid-extraction-appalachia.md` does not mention 2007/2020 pleas — no propagation needed there.

#### C-4. Lines 10 + 14 — JFK September 1960 visit + Canton speech "month after"

**Chapter text (lines 10, 14):**
> In September of 1960, John F. Kennedy drove through McDowell County, West Virginia, and what he saw changed the direction of his campaign.
> [...]
> But in Canton, Ohio, the month after that West Virginia visit, he said something that has stayed with the historical record: *I do not believe any of us would like to live here.*

**Canonical concerns (three):**

1. **Date arithmetic conflict.** JFK's documented Canton, Ohio speech is September 27, 1960. "The month after" the WV visit would place the WV visit in August (or very early September) 1960 — not in September. As written, the chapter says the WV visit was September *and* Canton was the month after, which would put Canton in October. No documented JFK Canton speech in October 1960.

2. **Visit-date provenance.** JFK's most extensively documented McDowell County campaign visit was during the WV primary (April 1960; primary May 10, 1960) — the formative trip credited in mainstream historiography (Halberstam, Schlesinger, White's *The Making of the President 1960*). He did general-election campaigning in WV in late September 1960 (Charleston, Wheeling speeches), but a McDowell County visit in August or early September 1960 needs primary-source confirmation (JFK Presidential Library archives).

3. **Quote verification.** The exact phrasing "I do not believe any of us would like to live here" — verbatim attribution to the Canton speech needs primary-source confirmation against the JFK Library speech archive. Could be paraphrase or composite.

**Recommended action:** Verify against JFK Library before applying any fix. Three possible outcomes:
- (a) Confirms April-1960 primary visit + Canton paraphrase → rewrite lines 10+14 timeline to "during the 1960 primary campaign" + acknowledged paraphrase of the Canton-era impressions.
- (b) Confirms August/September 1960 general-election visit → tighten "month after" to specific date.
- (c) Quote is paraphrase → introduce as such ("...he said, in substance...").

**Status:** Held pending primary-source verification.

**Propagation:** Same prose at `research/case-studies/appalachian-coal.md` lines 18–22.

---

### HIGH

#### H-1. Line 22 — "the kind of coal that made steel hard enough to build the Brooklyn Bridge"

**Chapter text (line 22):**
> ...the kind of coal that made steel hard enough to build the Brooklyn Bridge, the Empire State Building, the aircraft carriers that turned the Pacific war.

**Canonical concern:** Brooklyn Bridge completed 1883; substantial commercial production from McDowell County's Pocahontas seams began in the 1890s–1900s. The attribution is romantic but historically loose. Empire State Building (1931) and WWII aircraft carriers are defensibly McDowell-era; Brooklyn Bridge is the stretch.

**Recommended spot-fix:** Swap for a verifiably post-1900, McDowell-era landmark that preserves the rule-of-three. The Golden Gate Bridge (1937) used 83,000 tons of structural steel from Bethlehem Steel and US Steel — both McDowell-Pocahontas-supplied during that era.

> ...the kind of coal that made steel hard enough to build the Golden Gate Bridge, the Empire State Building, the aircraft carriers that turned the Pacific war.

**Propagation:** Same prose at `research/case-studies/appalachian-coal.md` line 28.

#### H-2. Line 41 — "drug death rate in McDowell County runs at 141 per 100,000 — ten times the national average"

**Canonical concern:** The 10× ratio requires a national base of ~14/100k. National drug-overdose mortality was approximately 14/100k around 2014–2015; by 2020+ it reached ~28–30/100k. If the 141 figure is current (chapter uses present tense "runs at"), the current ratio is ~4.7×, not 10×. Figures need time-alignment.

**Recommended action:** Two options, author choice:
- (a) Keep ratio: anchor both figures to the same year (e.g., "ran at 141 per 100,000 in 2015 — ten times the national average").
- (b) Update to current: "runs at 141 per 100,000 — roughly five times the national average."

**Status:** Deferred to Pass 2 (voice-polish) — pairs naturally with prose-framing decisions.

#### H-3. Line 39 — "national average of 76.5"

**Chapter text (line 39):**
> What remained was this: a male life expectancy of 63.5 years, against a national average of 76.5.

**Canonical concern:** 76.5 is roughly correct for U.S. male life expectancy at birth (CDC 2019: 76.3 male; 78.8 all-sex). But the prose reads "male life expectancy of 63.5 years, against a national average of 76.5" — a knowledgeable reader could parse "national average" as all-sex (~78.8), creating an apparent apples/oranges comparison. The 13-year gap holds only if both figures are male-only.

**Recommended spot-fix:** Three-word disambiguation.

> ...a male life expectancy of 63.5 years, against a national male average of 76.5.

**Propagation:** Same comparison at `research/case-studies/appalachian-coal.md` line 12 + line 42.

---

### MEDIUM (primary-source citation tightening)

These are widely-reported figures that are not factually wrong but lack source-anchoring in the current prose. All belong in the endnote/citation-finalization sweep that runs against the whole manuscript closer to publisher submission — not piecemeal per chapter.

| # | Line | Claim | Citation needed |
|---|---|---|---|
| M-1 | 35 | "U.S. Steel Gary mine closed in the late 1980s — taking 1,200 jobs with it" | WV state labor archives; commonly quoted, rarely sourced |
| M-2 | 35 | "Personal income in McDowell County dropped by two-thirds in a single year" | BEA Regional Economic Accounts (CAINC1 county-level personal income, 1986–87) — striking enough that a fact-checker will chase it; verify before relying |
| M-3 | 63 | "Twenty percent of miners in Appalachia with twenty-five or more years of tenure have black lung" | NIOSH CWHSP surveillance; specify year |
| M-4 | 67 | "$44 billion in benefits / $4.6 billion in debt / $15 billion by 2050" (Black Lung Trust Fund) | GAO report (likely GAO-18-351 or GAO-20-489) |
| M-5 | 81 | "633,000 acres / $7.5–9.8 billion / $3.8 billion in bonds" | Appalachian Voices / OSMRE primary source |
| M-6 | 83 | "$865 million in liabilities" transferred 2014–2016 | OSMRE or Government Accountability Project report |
| M-7 | 123 | "33 to 122 times" — cross-chapter consistency with Ch 6 + Ch 8 | Belongs to Phase B whole-book audit, not Ch 2 spot-fix |
| M-8 | 155 | "400 miles away" | Pittsburgh ~230mi, NYC ~430mi, Norfolk ~330mi, Chicago ~600mi — consider "hundreds of miles" or pick one city |
| M-9 | 207 | "Two hundred and fifty miles" McDowell→Chesapeake | Welch, WV to Hampton Roads ~300mi by road; tolerable as straight-line approximation |

**Recommended action:** Hold for endnote/citation-finalization sweep. Exception: M-2 ("two-thirds in one year") warrants primary-source verification now since it's the most striking-and-checkable claim a knowledgeable reader will chase.

---

### LOW

| # | Line | Note |
|---|---|---|
| L-1 | 41 | "Median household income is $28,235" — accurate for some ACS years; date the figure when endnotes get built. |

---

## Structural audit emphases (per workstream Ch 2 row)

### A. INTERVIEW NEEDED placeholders — STATUS CORRECT ✓

All three publisher-facing pending-prose markers still present in Ch 2 prose, matching weekly-audit-2026-04-28 count:
- Line 30 — Opening person
- Line 163 — The miner's voice
- Line 168 — The extraction-side portrait

Outreach pipeline (Darity / Beth-Ingledew Amsterdam intro / Sherfinski / Colden) is active per `Chapter__2___GuidanceDoc.md` per-section staleness audit 2026-05-08 line 26, but no interviews have resolved into chapter prose yet. Markers are legitimate publisher-facing "TODO before publication" signals per WP#10 (internal-scaffolding discipline) — not audit-trail content to be scrubbed pre-submission.

**Action:** None in this audit. Resolution depends on outreach pipeline landing.

### B. Cost Severance defense paragraph (commit `8e61cd1`) — SOFT COHESION ASK (defer to Pass 2)

Inserted at line 141 between the vocabulary-subsection close ("...or fisheries in the Chesapeake Bay.") and the Mazzucato lineage paragraph open ("The phrase 'value extraction' carries an established lineage..."). Defense engages four alternative names (externality / displacement / transfer / appropriation), surfaces the employment-severance metaphor's missing-payment-architecture, names Mazzucato + Harvey lineage at close.

**Cohesion issue:** Soft duplication of Mazzucato + Harvey introduction.

- Line 141 closes: "Mariana Mazzucato names value-extraction's diagnosis; David Harvey names accumulation by dispossession; the framework adopts a third sister-term..."
- Line 143 opens: "The phrase 'value extraction' carries an established lineage worth naming once at the moment we adopt it. Mariana Mazzucato, in *The Value of Everything*..."

The reader meets Mazzucato as named ancestor in line 141, then encounters her again as freshly-introduced lineage in line 143 — a ~150-word whiplash. The "worth naming once at the moment we adopt it" framing in line 143 is slightly false given line 141 named her first.

**Recommended action:** Defer to Pass 2 (voice-polish). The fix is a connective-tissue adjustment to line 143 opening, not a factual correction. Pass 2 will likely surface 5–10 similar items in Ch 2 (rule-of-three patterns, em-dash crutches, declarative-three-in-a-row visible on skim) — better to fix in one cohesion-pass commit than to one-off it now.

### C. $100-barrel-passage pivot — COMPLETE ✓

Confirmed: no "$100", "barrel", or "$100/ton" references remain in Ch 2 draft. The pivot away from the $100-barrel framing (now living in Ch 8 per the case-study brief) is clean in Ch 2. The framing now lives as "what a ton of McDowell County coal actually cost" + the 33–122x IPG range — register-coherent with Ch 2's narrative voice.

**Caveat (M-7 above):** The cross-reference at line 123 to Ch 8 ("Chapter 8 walks the floor-estimate version of this calculation... lands at the upper end of this range") depends on Ch 8's per-ton arithmetic landing as described. Per workstream handoff Ch 8 line 71 has its own stale "$100 barrel" reference flagged separately. Cross-chapter consistency check belongs to Ch 8's Phase A audit or Phase B whole-book audit, not this Ch 2 audit.

---

## Fact-check verdict

**READY AFTER SPOT-FIXES.**

| Severity | Count | Disposition |
|---|---|---|
| CRITICAL | 4 | C-1, C-2, C-3, H-1 (typo — H-1 is HIGH not CRITICAL; corrected below) — 3 of 4 ratifiable now (C-1, C-2, C-3); C-4 (JFK) held for primary-source verification |
| HIGH | 3 | H-1, H-3 ratifiable now; H-2 deferred to Pass 2 |
| MEDIUM | 9 | Deferred to endnote/citation sweep; M-2 to be verified concurrently with C-4 |
| LOW | 1 | Deferred to endnote/citation sweep |

(Correction: C-4 is the only fact-check finding held for primary-source verification. C-1, C-2, C-3 are ratifiable now. H-1 and H-3 are ratifiable now. H-2 is deferred to Pass 2.)

The chapter's argument, structure, and apparatus are intact. Findings cluster in named-claim precision and primary-source citation tightening — not structural revision.

**Not yet run** (per scope of this session):
- Pass 2: Voice-polish — will surface Structural B (Mazzucato/Harvey duplication at lines 141/143) + likely 5–10 additional LLM-tic / cohesion items.
- Pass 3: Audience-load — 20-character book-audience pressure-test set.

---

## Phase C plan (this artifact's spot-fix scope)

**Ratified for immediate application** (5 spot-fixes):
- C-1 (line 12): drop false-first claim
- C-2 (line 41): "under the modern program" modifier
- C-3 (line 193): reverse felony/misdemeanor mapping for Purdue 2007 plea
- H-1 (line 22): Brooklyn Bridge → Golden Gate Bridge
- H-3 (line 39): "national average" → "national male average"

**Propagation to case-study brief** (`research/case-studies/appalachian-coal.md`):
- Line 12 (H-3) + line 20 (C-1) + line 28 (H-1) + line 42 (H-3 bullet) + line 47 (C-2)

**Held for primary-source verification** (2 items, separate research task):
- C-4 (JFK September 1960 visit + Canton quote)
- M-2 (two-thirds personal-income drop, BEA verification)

**Deferred to Pass 2 (voice-polish)**:
- Structural B (Mazzucato/Harvey duplication at lines 141 ↔ 143)
- H-2 (drug death rate 10× ratio time-alignment)

**Deferred to endnote/citation-finalization sweep**:
- M-1, M-3 through M-6, M-8, M-9, L-1

**Belongs to Phase B (whole-book audit)**:
- M-7 (33–122x cross-chapter consistency Ch 2 ↔ Ch 6 ↔ Ch 8)

---

## Cross-references

- `manuscript/chapters/Chapter__2_TheMiner__Draft.md` — chapter under audit
- `manuscript/chapters/Chapter__2___GuidanceDoc.md` — internal-scaffolding guidance (per-section staleness audit 2026-05-08)
- `research/case-studies/appalachian-coal.md` — verbatim-source case study (propagation target)
- `research/case-studies/opioid-extraction-appalachia.md` — opioid-section brief
- `research/literature/bibliography.md` §1, §2, §10, §13 — canonical-source verification
- Commit `8e61cd1` — Cost Severance defense paragraph (ratified 2026-05-11)
- `tools/workstream-handoffs/manuscript-stage-3-rigor-pass-handoff_2026-05-11.md` — Phase A spec + per-chapter table row for Ch 2
- `tools/drafting-templates/stage-3-three-pass-rigor-audit.md` — three-pass discipline template (Pass 2 + Pass 3 to follow)

---

*Phase C spot-fix application landed in commit `1130c67` on the same branch (`claude/reverent-noyce-15f90f`) — 5 ratified fixes to Ch 2 + propagation to case-study brief.*

---

## Verification addendum (2026-05-12) — C-4 + M-2

### C-4 (JFK September 1960 visit + Canton quote) — VERIFIED WRONG

Primary-source verification fired 2026-05-12 via JFK Library archive + American Presidency Project + WVU history materials. Findings:

**Date conflict — CONFIRMED.** JFK's documented McDowell County campaign visits were:
- **Saturday, May 9, 1959** — Welch Elementary School Truman birthday dinner (600 attendees).
- **Tuesday, May 3, 1960** — Welch courthouse rally before May 10 WV primary (700 inside courthouse + 300 outside via speaker system). Ted Kennedy took over speaking after JFK developed sore throat.

There is no documented JFK McDowell County visit in September 1960. The May 1960 primary-campaign visit is the formative trip the historiography references (Halberstam; Schlesinger; *Battleground West Virginia*; WV State Archives 1960 campaign timeline).

**Quote attribution — UNVERIFIED.** The actual JFK Canton, Ohio speech of September 27, 1960 (per JFK Library archive + American Presidency Project transcript) does reference McDowell County by name, but the verbatim passage is:

> "I ran in the primary in West Virginia. I spent some time in McDowell County in West Virginia. McDowell County mines more coal than it ever has in its history, probably more coal than any county in the United States and yet there are more people getting surplus food packages in McDowell County than any county in the United States."

The chapter's quoted line *"I do not believe any of us would like to live here"* **does not appear** in the documented Canton speech. WebSearch returned no canonical primary-source attribution of this line to JFK; one secondary search suggestion attributed a similar line to RFK in 1968, but no primary source confirms even that.

Other documented JFK 1960 WV-poverty quotes (any of which could replace the unverified line):

- **Welch, May 3, 1960** (referring to Eisenhower-administration neglect): *"He has seen the poor and hungry of foreign lands — but he has not seen the poor and hungry of McDowell County."*
- **General 1960 campaign framing:** West Virginia *"transformed into an island of poverty and distress in a vast sea of American plenty."*
- **Canton, September 27, 1960** (verbatim above) — the strongest McDowell-named option for direct quotation.

**Recommended spot-fix (pending author ratification):** rewrite lines 10 + 14 to align with documented record.

**Recommended replacement prose:**

> In May of 1960, John F. Kennedy drove through McDowell County, West Virginia, days before the primary that would carry the state. He had come to win an election he was expected to lose. What he found instead was something that didn't fit the story America was telling about itself that year — the story of postwar prosperity, of a country that had beaten the Depression and then the Axis and was now growing its way toward something permanent and good.
> 
> What Kennedy saw were children with distended bellies. Families eating surplus commodities — distributed right there in the hollows of McDowell County, because there was nothing else. Men who had mined the coal that powered the cities and built the ships that won the war, now sitting idle because the machines had come and the companies had no further use for them.
> 
> Kennedy was not given to sentiment in his public remarks. But four months later, in Canton, Ohio, he came back to what he had seen: *McDowell County mines more coal than it ever has in its history... and there are more people getting surplus food packages in McDowell County than any county in the United States.*
> 
> He meant it as an indictment of neglect. He was right that it was an indictment. He had the wrong defendant.

**Changes from current prose:**
- "September of 1960" → "May of 1960" (date corrected to documented primary visit)
- "He had come to win a primary in a state he was expected to lose" → "He had come to win an election he was expected to lose" (preserves the rhetorical beat; the primary itself, not "a primary" in the sense of any race)
- "in Canton, Ohio, the month after that West Virginia visit, he said something that has stayed with the historical record: *I do not believe any of us would like to live here.*" → "four months later, in Canton, Ohio, he came back to what he had seen: *McDowell County mines more coal than it ever has in its history... and there are more people getting surplus food packages in McDowell County than any county in the United States.*" (date arithmetic now matches Sept 27, 1960 Canton speech; verbatim quote from documented Canton speech text)

**Alternative replacement (Welch May 3 quote, if author prefers Eisenhower-neglect-indictment framing):**

> ...But four months later, in Canton, Ohio, he came back to what he had seen in McDowell County — the same indictment he had pressed in Welch days before the primary: *He has seen the poor and hungry of foreign lands — but he has not seen the poor and hungry of McDowell County.*

This preserves more of the original's emotional weight (it IS an indictment) at slight cost to the spatial setup (the quote was delivered IN McDowell, not in Canton; the "in Canton, Ohio" beat becomes "carried forward to Canton, Ohio").

**Propagation:** `research/case-studies/appalachian-coal.md` lines 16, 18, 22 carry the same prose verbatim and need the same fix.

**Status:** Pending author ratification of which replacement option (Canton-speech verbatim or Welch-speech verbatim or other) lands. Held from Phase C-α (commit `1130c67`) for verification; verification now complete; ready for Phase C-β application once ratified.

---

### M-2 (two-thirds personal income drop, 1986–87) — VERIFIED ACCURATE

Primary-source verification fired 2026-05-12. Findings:

**Claim CONFIRMED by secondary sources** anchored to BEA primary data. Wikipedia entry for McDowell County, WV + adjacent coal-history sources concur: the 1986 U.S. Steel Gary mine closure produced an immediate ~1,200-job loss; in the following year (1987), McDowell County's personal income decreased by approximately two-thirds. Canonical BEA series is **PCPI54047** (Per Capita Personal Income in McDowell County, WV), available via FRED — direct fetch returned 403 in this session, but the series is the established source.

**Recommended citation for endnote sweep:** "U.S. Bureau of Economic Analysis, *Per Capita Personal Income in McDowell County, WV* (PCPI54047), retrieved via FRED, Federal Reserve Bank of St. Louis. 1986–1987 county-level personal income series."

**Status:** Claim stands as written; verification successful; chapter prose requires no change. Endnote citation to be added during the endnote/citation-finalization sweep (cross-thread item — see PM session handoff + cross-thread-todos.md entry surfaced 2026-05-12).

---

### Verification disposition summary

| Item | Pre-verification status | Post-verification disposition |
|---|---|---|
| C-4 | Held for primary-source verification | **VERIFIED WRONG.** Date + quote both fail to match documented record. Spot-fix recommended; awaiting author ratification on which replacement option. |
| M-2 | Held for primary-source verification | **VERIFIED ACCURATE.** Claim stands. Endnote citation queued for endnote/citation-finalization sweep. |

---

*Phase C-β spot-fix application (C-4 Canton verbatim) landed in commit `3dcb15d` on the same branch.*

---

## Pass 2: Voice-polish — findings

**Pass 2 fired 2026-05-12 same session as Pass 1.** Applied the LLM-tic + voice-issue inventory from `tools/drafting-templates/stage-3-three-pass-rigor-audit.md` §Pass 2 + apparatus-residue check against `core/terms/terms_index.md` + apparatus register decisions (`tools/rigor-passes/commons_bonds_rigor_pass_2026-05-11_apparatus_register_decision_v1.0.0.md`).

### HIGH

#### V-1. Lines 141 → 143 → 147 — Mazzucato/Harvey introduction whiplash

**Chapter text (lines 141 close → 143 open → 147 open):**

Line 141 closes the Cost Severance defense paragraph:
> "Mariana Mazzucato names value-extraction's diagnosis; David Harvey names accumulation by dispossession; the framework adopts a third sister-term that points directly at the absent payment-instrument the other two leave the reader to imagine. Naming the missing architecture is what makes the bond proposing it possible."

Line 143 opens the Mazzucato lineage paragraph:
> "The phrase 'value extraction' carries an established lineage worth naming once at the moment we adopt it. Mariana Mazzucato, in *The Value of Everything: Making and Taking in the Global Economy* (2018), draws a sharp distinction..."

Line 147 opens the Harvey lineage paragraph:
> "The framing also echoes David Harvey, whose *The New Imperialism* (2003), Chapter 4, develops *accumulation by dispossession*..."

**Voice issue.** The reader meets Mazzucato + Harvey as named ancestors at the close of line 141, then encounters both freshly-introduced as if for the first time at lines 143 + 147. The "worth naming once at the moment we adopt it" framing in line 143 reads as slightly false once line 141 has just named her. The "framing also echoes David Harvey" at line 147 has the same issue. The two lineage paragraphs feel orphaned from the defense paragraph that introduced them.

This is the artifact of inserting the defense paragraph (commit `8e61cd1`, 2026-05-11) at line 141 between the vocabulary close (line 139) and the pre-existing Mazzucato + Harvey lineage paragraphs (143 + 147). The defense paragraph didn't update the connective tissue of the paragraphs that followed.

**Recommended spot-fix.** Light connective-tissue adjustment to lines 143 + 147. Two structurally-equivalent options:

**Option A — Tighten by reference.** Modify openings of lines 143 + 147 to acknowledge the prior introduction.

> [Line 143] Mazzucato's *The Value of Everything* (2018) bears developing in a paragraph. She draws a sharp distinction between *value creation*...
>
> [Line 147] Harvey's earlier *The New Imperialism* (2003), Chapter 4, develops *accumulation by dispossession* as the contemporary form of the older primitive-accumulation pattern Marx named...

**Option B — Restructure line 141 close.** Defer the named-ancestors line to lines 143 + 147, leaving line 141 to end on the "missing payment-architecture" thought.

> [Line 141 revised close] Severance names what the others do not. The word carries a borrowed payment-architecture... The framework's term applies the same logic to commons extraction — the same cut-tie structure — and surfaces what the prior names obscure: that the architecture of payment for cost severance is missing. Naming the missing architecture is what makes the bond proposing it possible.

Then line 143 + 147 stay as-is (lineage development reads as freshly-introduced because line 141 no longer pre-empts).

**Recommended:** Option B (restructure line 141 close). Reason: line 141's "third sister-term" / "ancestors" framing is novel rhetorical work that the defense paragraph was designed to do; trimming it to focus on the missing-architecture point keeps that work in line 141, and lets lines 143 + 147 own the lineage development they were drafted to handle. Option A bolts a hedge onto the existing lineage paragraphs, which works but feels patched.

---

### MEDIUM

#### V-2. Line 41 — Stat-dump paragraph

**Chapter text:**
> The drug death rate in McDowell County runs at 141 per 100,000 — ten times the national average. The poverty rate is 37.6 percent. Median household income is $28,235. The county ranks 55th of 55 West Virginia counties in health outcomes. The first food stamps under the modern program were issued in McDowell County. The latest data suggests the county may need them again.

**Voice issue.** Five back-to-back stat sentences with similar structure ("The X is Y. The X is Y. The X is Y..."). No sentence-length variance. Reader experiences the paragraph as a data dump rather than as part of the chapter's narrative voice.

Pairs with **H-2 fact-check finding** (drug death rate "10× ratio" needs time-alignment to circa-2015 national figure of ~14/100k, or update to current ~5× against current ~30/100k national).

**Recommended spot-fix.** Break the sequence with a varied-length sentence in the middle. Example pattern:

> The drug death rate in McDowell County runs at 141 per 100,000 — roughly five times the national average. The poverty rate is 37.6 percent. Median household income is $28,235, and the county ranks 55th of 55 in West Virginia health outcomes. The first food stamps under the modern program were issued here. The latest data suggests the county may need them again.

The combined sentence "Median household income is $28,235, and the county ranks 55th of 55 in West Virginia health outcomes." gives the sequence one longer beat, breaking the monotony.

#### V-3. Meta-commentary cluster (6 instances across chapter)

**Chapter text:**
- Line 24: "This matters."
- Line 49: "Here is a question that sounds simple but isn't:"
- Line 55: "Let's walk through it."
- Line 131: "At this point the book needs a word for what we've been describing, because we will use it in every chapter that follows."
- Line 153: "There is one more dimension of McDowell County's story that the numbers alone cannot convey."
- Line 205: "Before we leave McDowell County, there is something worth planting."

**Voice issue.** Six instances of author-voice signaling-what-comes-next. Each is acceptable in isolation as deliberate signposting. Cumulative effect is heavy author-presence — the reader is told what's about to happen rather than experiencing it.

**Recommended spot-fix.** Trim 2-3. The strongest candidates to cut:
- Line 55 "Let's walk through it." — removable; the next paragraph already walks through it. Cutting strengthens the lead-in.
- Line 24 "This matters." — telegraphs the importance the next sentence already enacts. Cut.
- Line 205 "Before we leave McDowell County, there is something worth planting." — could collapse into the next paragraph's open ("Two hundred and fifty miles from..."), making the spatial pivot do its own work without announcing it.

Keep lines 49 (sets up a question-answer rhetorical move), 131 (legitimately introduces vocabulary that will be used downstream), 153 (transitions to the Distance section by name).

#### V-4. Lines 179 + 181 — Two long counterargument paragraphs

**Chapter text:** Lines 179 and 181 are each single paragraphs of ~500-600 words handling, respectively, the "cheap energy lifted billions out of poverty" counterargument and the "miners chose that work" counterargument.

**Voice issue.** Visual weight + reader-load. Each paragraph is fact-dense and argumentatively complex with multiple sub-points; internal pacing is rhythmic but the unbroken text creates a wall-of-prose effect.

**Recommended spot-fix.** Break each into 2-3 paragraphs at natural argumentative joints. Example breaks:

Line 179 (cheap energy counterargument) — three natural breaks:
- Para 1: From "It does not prove that industrialization was a mistake." through "...stronger, not weaker:" (the framework's response to the cheap-energy claim).
- Para 2: From "the people of McDowell County subsidized..." through "...without any mechanism for declining." (the cost-bearing argument).
- Para 3: From "The miner who developed black lung did not agree..." through "...the structural mechanism by which the severance operated." (the consent argument).

Line 181 (agency counterargument) — similar three-break structure.

This is a structural recommendation rather than a sentence-level fix. The argument density and order are preserved; only paragraph breaks change.

#### V-5. Line 209 — Schematic Chesapeake-vs-coal parallel

**Chapter text:**
> The mechanism operating on them is different in its details. The resource is renewable rather than finite. The costs are ecological rather than occupational. The geography is water rather than tunnels.

**Voice issue.** Three "X is Y rather than Z" sentences in immediate succession — rigid parallel structure that reads schematic. The Chesapeake-vs-coal contrast is the chapter's pivot to the cross-chapter Common Bonds theme; the schematic compression undersells the move.

**Recommended spot-fix.** Vary one sentence or restructure to a single longer sentence with the three contrasts compressed. Example:

> The mechanism operating on them is different in its details — a renewable resource rather than a finite one, ecological costs rather than occupational, water rather than tunnels.

Single sentence; three contrasts as em-dash list; less monotone.

#### V-6. Line 65 — "astonishingly" hedge

**Chapter text:**
> The disease is also, astonishingly, resurgent.

**Voice issue.** "Astonishingly" is a soft hedge / author-emotion intrusion. The claim that follows (resurgent black lung among younger miners despite decades of regulation) is structurally astonishing on its own merits; the adverb tells the reader what to feel about it rather than letting the fact do the work.

**Recommended spot-fix.** Cut "astonishingly":

> The disease is also resurgent.

The shorter sentence makes the surprise the next sentence delivers ("rising fastest among younger miners") land harder.

#### V-7. Line 97 — "externality tail" apparatus residue without prior plain-prose grounding

**Chapter text:**
> The architecture that would have closed the gap — capturing the rents at extraction, routing them to the bearers, holding them across the full life cycle of the externality tail — was never built.

**Apparatus check.** "Externality Tail" is a canonical framework term (per `core/terms/terms_index.md` lines 120 + 360); the lowercase prose form is acceptable in body prose. Defense paragraph for the term lives in Ch 6 (per apparatus register decisions + commit `2a7c336`). However, Ch 2 line 97 is the term's *first appearance* in the manuscript reading order (Ch 1 → Ch 2 → ... → Ch 6), and the term appears without prior plain-prose grounding in Ch 2.

Per Phase B audit dimension (d) — "does each framework term land in plain language before formal apparatus appears?" — Ch 2 line 97 is the test. The phrase carries intuitively in context ("life cycle of the externality tail" reads as "extended-time tail of externalities"), but a careful reader might pause.

**Recommended spot-fix.** Either:
- (a) One-clause gloss at first mention: "holding them across the full life cycle of the externality tail — the long-tail downstream costs that persist after extraction ends — was never built." (Adds ~12 words.)
- (b) Accept that the term carries intuitively. The Ch 6 defense paragraph provides formal grounding when the reader encounters it again.

**Recommended:** Option (a). Reader-load benefit is real and the gloss costs nothing structurally.

---

### LOW

#### V-8. Line 137 — "It is" four-in-a-row

**Chapter text:**
> Value extraction is not theft. It is not fraud. In most cases, it is perfectly legal. It is what happens when the accounting system does not require honest pricing.

**Voice issue.** Four-in-a-row with "It is" anaphora ("Value extraction is not / It is not / It is perfectly legal / It is what happens"). Slightly heavy. Deliberate rhetorical climax but at the edge of cadence-repetition tic.

**Recommended action:** Leave as-is. Author may prefer to break the four-beat by combining two clauses, but the rhetorical climax earns the cadence.

#### V-9. Line 111 — Section-title meta-commentary

**Chapter text:** Subsection header `**The one sentence we will return to.**`

**Voice issue.** META-COMMENTARY in subsection header (signaling forward-reference rather than naming the content). Deliberate signposting per the GuidanceDoc — this header announces the carbon-footnote planted for Ch 6 ("None of these figures includes what happens when the coal is burned. We'll return to that.").

**Recommended action:** Leave as-is. The meta-framing is deliberate cross-chapter scaffolding.

#### V-10. Line 159 — "Chapter 7 walks through the full set" — Ostrom-path register fix

**Chapter text:**
> Distance is one of several arrangements that hide cost from honest accounting; Chapter 7 walks through **the full set**, by examining what happens when all of them collapse at once.

**Voice / register issue.** The phrase "the full set" leans toward closure — implies the patterns Ch 7 covers are exhaustive. Per the framework's ratified Ostrom-path register (`reference_ostrom_illustrative_register.md`, 2026-05-02), lists of patterns / cost components / commons are illustrative-with-room-to-grow, not exhaustive enumerations. "The full set" is the only phrase in the section that reads as closed-frame; the rest of lines 157-159 is properly open-frame ("one of several arrangements"; "Distance enabled ignorance"; etc.).

**Recommended spot-fix.** 4-5 word edit:

> ...Chapter 7 walks through **more of them**, by examining what happens when all of them collapse at once.

Or:

> ...Chapter 7 walks through **more of these arrangements**, by examining what happens when all of them collapse at once.

Either restores Ostrom-path register without rewriting the section's substance.

**Provenance note.** This finding surfaced after the author corrected two methodology lapses in the Pass 2 audit (in-session 2026-05-12): (a) an initial "false-flag" verdict on the broader spatial-cost-severance treatment that defaulted to trusting an older terms_index reference-file entry over a more recent active-review audit; (b) a subsequent attempt to reframe as "Phase B framing-consistency check against Ch 7's six patterns" that itself treated the six patterns as a closed reference frame. Both lapses captured to memory as `feedback_audit_recent_active_review_default.md` + `feedback_audit_open_illustrative_default.md`. The actual finding left after corrections is the narrow line-159 "full set" phrasing — what should have been flagged in the first place.

---

## Pass 2 verdict

**READY AFTER LIGHT SPOT-FIXES.** Chapter is in solid voice shape. Main issue is the Mazzucato/Harvey introduction whiplash (V-1, HIGH) — directly attributable to the recent insertion of the Cost Severance defense paragraph (commit `8e61cd1`, 2026-05-11). Other findings are MEDIUM/LOW polish work.

| Severity | Count | Disposition |
|---|---|---|
| HIGH | 1 | V-1 — Mazzucato/Harvey whiplash. Recommend Option B (restructure line 141 close). Apply during Phase C-γ. |
| MEDIUM | 6 | V-2 (stat-dump pacing) + V-3 (meta-commentary cluster) + V-4 (long counterargument paragraphs) + V-5 (schematic Chesapeake parallel) + V-6 ("astonishingly" hedge) + V-7 (externality tail gloss). All ratifiable as light spot-fixes; bundle into Phase C-γ. |
| LOW | 3 | V-8 (anaphora four-in-a-row — leave-as-is) + V-9 (section-title meta-commentary — leave-as-is) + V-10 (Ostrom-path register fix at line 159 "full set" phrasing — 4-5 word edit, apply during Phase C-γ). |

**Not yet run** (Pass 3 audience-load): 20-character book-audience pressure-test set. Ch 2's argumentative weight is heaviest on the long counterargument paragraphs (lines 179, 181) — those will be the chapter's primary audience-load test surface.

---

*Phase A artifact rev. 2026-05-12 (Pass 1 fact-check + verification addendum + Pass 2 voice-polish complete; Pass 3 audience-load pending). C-4 spot-fix Phase C-β landed in commit `3dcb15d` (original session SHA; rebased to `5bc6edb` after parallel-session reconciliation). Pass 2 spot-fix queue (V-1 through V-7) ready for author ratification before Phase C-γ session fires.*

---

## Phase C-γ — APPLIED 2026-05-13

Author ratified all proposed Pass 2 spot-fixes (V-1 through V-7 + V-10; V-8 + V-9 left-as-is per recommendation). Phase C-γ application landed same-session per WP#9 worktree workflow.

**Spot-fixes applied (8 total):**

| # | Line | Edit |
|---|---|---|
| V-1 (HIGH) | 141 | Removed the Mazzucato/Harvey sister-term trio sentence ("Mariana Mazzucato names value-extraction's diagnosis; David Harvey names accumulation by dispossession; the framework adopts a third sister-term...") from the Cost Severance defense paragraph close. Defense paragraph now ends at "Naming the missing architecture is what makes the bond proposing it possible." Lines 143 + 147 own the Mazzucato + Harvey lineage development they were drafted to handle (Option B per recommendation). |
| V-2 (MEDIUM) + H-2 (Pass 1 HIGH) | 41 | Stat-dump pacing fix + drug-death ratio time-alignment: "ten times the national average" → "roughly five times the national average"; combined "$28,235. The county ranks" → "$28,235, and the county ranks"; "in McDowell County. The latest" → "here. The latest". |
| V-3 (MEDIUM) | 24, 55, 205 | Three meta-commentary lines cut: "This matters." (line 24); "Let's walk through it." (line 55); "Before we leave McDowell County, there is something worth planting." (line 205). Lines 49, 131, 153 retained per recommendation (each does load-bearing work). |
| V-4 (MEDIUM) | 177, 179 | Two long counterargument paragraphs broken at natural argumentative joints. Line 177 (cheap-energy) broken into three paragraphs (concession + reframe / compensation argument / structural problem + consent + information asymmetry). Line 179 (agency) broken into four paragraphs (concede agency / constrained choice / information asymmetry / contemporary generalization). Argument density preserved; paragraph breaks at natural joints. |
| V-5 (MEDIUM) | 209 | Schematic Chesapeake-vs-coal parallel collapsed: three "X is Y rather than Z" sentences → single em-dash list ("a renewable resource rather than a finite one, ecological costs rather than occupational, water rather than tunnels"). |
| V-6 (MEDIUM) | 65 | "astonishingly" hedge cut: "The disease is also, astonishingly, resurgent." → "The disease is also resurgent." |
| V-7 (MEDIUM) | 97 | Externality tail gloss added: parenthetical "(the long-tail downstream costs that persist after extraction ends)" inserted at first manuscript-reading-order appearance of the term. |
| V-10 (LOW) | 159 | Ostrom-path register fix: "Chapter 7 walks through the full set" → "Chapter 7 walks through more of them". Restores open-illustrative framing per `feedback_audit_open_illustrative_default.md`. |

**Left as-is (per recommendation):**

- V-8 (LOW) Line 137 — "It is" four-in-a-row anaphora. Earned rhetorical climax.
- V-9 (LOW) Line 111 — section-title meta-commentary "The one sentence we will return to." Deliberate cross-chapter scaffolding (carbon footnote planted for Ch 6).

**Case-study propagation:**

`research/case-studies/appalachian-coal.md`:
- H-2 ratio update at lines 12 + 43 + 151 ("10× national" or "ten times the national" → "roughly 5×" / "roughly five times")
- V-3 partial: "This matters." cut from line 30
- V-6: "astonishingly" cut from line 57

`research/case-studies/opioid-extraction-appalachia.md`:
- H-2 ratio update at lines 15 + 50

Other voice-polish edits (V-1 + V-4 + V-5 + V-7 + V-10) are Ch 2-specific (case studies have different section structure / don't carry that prose).

**Phase C-γ verdict:** APPLIED. All ratified spot-fixes landed in Ch 2 + case-study propagations. Pass 3 (audience-load) remains the only outstanding Phase A work for Ch 2.

---

*Phase A artifact rev. 2026-05-13 (Pass 1 + Pass 2 complete + Phase C-α + Phase C-β + Phase C-γ all applied; Pass 3 audience-load remains pending). Ready for filename rename to `..._stage3_three_pass_v1.0.0.md` when Pass 3 lands and the full three-pass artifact is complete.*
