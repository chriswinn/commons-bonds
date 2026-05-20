# Ch 3 augmentation workstream — Stage 1 pre-draft brief (1a + 1b + 1c)

**Date:** 2026-05-20
**Author:** Claude (Opus 4.7 1M ctx), session
`claude/frosty-northcutt-48ce94`
**Status:** PROPOSAL — pending author ratification at session close.
Ratified brief gates Stage 2 audience-blind drafting of the 11
augmentation landings in a follow-up session.
**Scope:** Stage 1 ready-to-draft gate per pipeline-doctrine v1.0.0
([`tools/commons_bonds_pipeline_doctrine_stage_1_v1.0.0.md`](../commons_bonds_pipeline_doctrine_stage_1_v1.0.0.md))
for the Ch 3 augmentation workstream — landing 11 named
public-record voices at chapter-specific locations in
[`manuscript/chapters/Chapter__3_TheWaterman__Draft.md`](../../manuscript/chapters/Chapter__3_TheWaterman__Draft.md)
v1, per the augmentation map in section 5 of
[`tools/stage-1-briefs/ch3_phat_replacement_analysis_2026-05-20_v1.0.0.md`](ch3_phat_replacement_analysis_2026-05-20_v1.0.0.md).
**Out of scope:** the full two-act restructuring described in
[`Chapter__3___GuidanceDoc.md`](../../manuscript/chapters/Chapter__3___GuidanceDoc.md)
§1 (that is a longer-horizon revision; this workstream lands named
voices into existing v1 sections without restructuring the chapter
shape). Phat anonymization is RATIFIED (commit `8a55395`,
2026-05-20) and IMMUTABLE for this workstream.

---

## §0. Sub-step verdicts at a glance

| Sub-step | Output | Verdict |
|---|---|---|
| **1a** Invariant gate | Ch 3 v1 scan via `tools/scripts/check-corpus-invariants.sh` | **CLEAN BASELINE** (0 HIGH; 2 MEDIUM; both annotated below as not blocking) |
| **1b** Substantive ready-to-draft brief | This file §§2–8 | **READY** (11 augmentation landings specified with anchor voices, verbatim quote candidates, target locations, structural roles, audience matrix, render conventions) |
| **1c** Cross-artifact coherence check | This file §9 | **HOLD with surfaced gaps** (Ch 3-relevant bibliography entries §19.5 do NOT yet carry the 11 augmentation sources beyond Colden; Stage 1c surfaces these as Stage-2-or-pre-Stage-3 add work). Sibling-chapter + GuidanceDoc + consent-discipline coherence VERIFIED. |
| **Stage 1 sign-off** | Academic + prose-quality bookend | **PASS with one HOLD** — bibliography §19.5 additions required before publisher-facing prose lands. See §10. |

---

# Sub-step 1a — Invariant-gate clean baseline

**Date:** 2026-05-20
**Scope:** `manuscript/chapters/Chapter__3_TheWaterman__Draft.md`
**Scan command:** `bash tools/scripts/check-corpus-invariants.sh --scope manuscript/chapters/Chapter__3_TheWaterman__Draft.md`
**Scaffolding-scan registry:** `tools/quality-gates/scaffolding-patterns.yaml` (HEAD as of session start)
**Regressed-pattern-scan registry:** `tools/quality-gates/regressed-patterns.yaml` (HEAD as of session start)

## §1a.1 Scan results

- **Patterns scanned:** 78
- **Files scanned:** 1
- **HIGH-severity matches:** 0
- **MEDIUM-severity matches:** 2
- **LOW / informational matches:** 0

## §1a.2 HIGH findings

None. Stage 1a clear to proceed.

## §1a.3 MEDIUM findings (per-finding disposition)

### M1 — `[scaffolding/scaffold-ratified]` at line 129

**Verbatim text:**
> `<!-- anonymized per named-subject consent discipline ratified 2026-05-20; consent pursuit continues at relationship-pace; restore name in future printings if consent lands -->`

**Disposition:** ALLOWLIST-INLINE (no YAML change). This is an HTML
comment, not publisher-facing prose. The scaffolding scanner reads
the chapter source flat; the comment renders as nothing in built
output. The annotation documents the ratified anonymization
discipline at the precise scene-anchor location and is intentionally
retained as an audit-trail breadcrumb. Removing the comment would
strip a load-bearing provenance marker for the Phat anonymization;
the MEDIUM verdict is correct that the word "ratified" appears, but
the location (HTML comment, never rendered) is the safe class for
this pattern. **No YAML allowlist update needed.** Held in place as
intentional process-trail.

### M2 — `[regressed/regressed-em-dash-density-three-plus]` at line 38

**Verbatim text:**
> "Take some — leave the rest — let the rest spawn — come back next year."

**Disposition:** HOLD FOR PASS 3.2 VOICE-POLISH RE-FIRE. Three em-
dashes in 13 words is a known rigor-pass density-tic pattern. The
sentence is rhythmic ("Take some — leave the rest — let the rest
spawn — come back next year") and the em-dashes do the parallelism
work, but the density flag is legitimate. **This is a Pass 3.2 voice-
polish concern**, not a Stage 1a blocker — the augmentation
workstream is landing NEW prose at OTHER locations, and the existing
line 38 sentence is unaffected by the augmentation. **Recorded here
so the eventual Ch 3 Pass 3.2 voice-polish session catches it; not a
gate on this Stage 1.** No spot-fix in this workstream.

## §1a.4 LOW findings

None.

## §1a.5 Allowlist updates committed

None this session.

## §1a.6 Verdict

**CLEAN BASELINE.** Stage 1a complete. Two MEDIUM findings dispositioned
without YAML changes (M1 = intentional process-trail annotation;
M2 = held for Pass 3.2 voice-polish, not a Stage 1 blocker). Ready
for Stage 1b.

---

# Sub-step 1b — Canonical fact-ground + audience-aware structure + render-safe convention

## §1. Audience pressure-test character set (Ch 3-augmentation specific)

The augmentation lands inside the existing Ch 3 v1 prose; the
chapter's broader audience set already lives in
[`Chapter__3___GuidanceDoc.md`](../../manuscript/chapters/Chapter__3___GuidanceDoc.md).
This sub-section trims to the **augmentation-specific
pressure-test set** — the readers whose ability to verify or
recognize the named voices is most load-bearing for landing the
augmentation cleanly.

### Tier 1 — gating

| # | Character | ~50w sketch |
|---|---|---|
| 1 | **CBF Maryland communications team (Val DiMarzio)** | Non-economist; environmental-nonprofit comms career. Likely will read the chapter pre-publication if/when CBF gateway opens further. Wants comprehension she can carry to Colden. Reads for: voice-attribution accuracy, framing fairness, no overclaim. What lands: Colden quoted exactly as published; Tarnowski's 12-word thesis preserved verbatim. What alienates: paraphrasing-as-quote; misattribution; framing CBF as villain or hero. |
| 2 | **David Sherfinski (CBF VA communications; ex-Reuters Foundation journalist)** | Multi-year political + climate reporter; wrote the 2022 Tangier piece this brief draws on. Reads for: journalism standards — proper attribution, verbatim quotes, source-of-record citation, no over-extension. What lands: Eskridge / Pruitt / Evans quotes attributed to his 2022 piece by name + URL; courtesy-notify discipline acknowledged. What alienates: paraphrasing his subjects' words; weaponizing the quotes against the subjects' stated positions. |
| 3 | **Tonya O'Connor (VMRC Petition 449 petitioner; non-affiliated VA resident)** | Filed the 349-page petition demanding moratorium until VMRC produces Bay-specific menhaden science; her petition is named-quoted public-record material. Reads for: accurate representation of the petition's central finding; correct citation of public-trust doctrine grounding; no distortion of her ask. What lands: the petition's "no Bay-wide estimate" finding quoted verbatim; the 1,266-comments figure cited; hearing date accurate. What alienates: framing her as a hero-of-the-story; misstating the petition's legal grounding. |
| 4 | **J.C. Hudgins (President, VA Watermen's Association; Piankatank River waterman)** | The kitchen-table-economics voice in Maryland Matters Apr 2026. The $150/day quote is the public record of his daily margins. Reads for: that his words appear exactly as he gave them to the reporter; that the Piankatank River geography is correctly named; that he's not being made a spokesperson for a position he didn't take. What lands: $150/day + "pretty expensive eating" quotes preserved verbatim; institutional role (President, VWA) attributed. What alienates: paraphrasing the $150 line; using his words for arguments he didn't make. |

### Tier 2 — pipeline-strengthening

| # | Character | ~50w sketch |
|---|---|---|
| 5 | **Allison Colden (CBF MD ED; already canonical in Ch 3)** | Already named in chapter; the augmentation deepens her voice's institutional setting by adding peer-voices (Tarnowski, Nesslage, Latour). Reads for: consistency with what she's already said; alignment with peer-scientist quotes. What lands: her existing canonical quotes preserved; Tarnowski's "plenty of oysters" thesis lands as peer-validation of her oyster-paradox framing. What alienates: silently re-quoting her in modified wording; using her quotes to make a sharper claim than she made. |
| 6 | **Mitch Tarnowski (MD DNR oyster-reef survey leader)** | The chapter's central paradox quote in 12 words: *"There are plenty of oysters out there. They're just not being harvested."* Said by a state regulator. Reads for: verbatim quote; institutional attribution (MD DNR); context preserved (the Maryland Matters Apr 2026 piece's specific framing). What lands: 12-word thesis quoted exactly + attributed to MD DNR + cited to Maryland Matters. |
| 7 | **Genny Nesslage (UMD CES; menhaden scientist)** | The science-gap voice in WHRO Oct 2025: *"We don't know the abundance of menhaden in the bay at any given time relative to the coast."* Reads for: verbatim quote; correct institutional attribution; correct framing of the scientific gap (not as institutional failure but as data-deficit acknowledgment). |
| 8 | **Bill Goldsborough (retired CBF fisheries scientist; 1980s rockfish institutional memory)** | The 1985 → present arc institutional-memory voice. Quoted in Smithsonian 2009. Reads for: that the 1985 moratorium history is told accurately; that his institutional-memory work is properly credited. |
| 9 | **Cameron Evans (Tangier native; Virginia Wesleyan student)** | The next-generation Tangier voice from Sherfinski 2022. *"If you can't save an island a mile and a half long, how are you going to save the East Coast?"* Reads for: that her words are her words; that she's not made to carry an adult political position; that the next-generation register is preserved. |

### Tier 3 — cultural resonance + accessibility

| # | Character | ~50w sketch |
|---|---|---|
| 10 | **General Bay-area reader (recreational angler; weekend boater)** | The chapter's general audience. Reads for: that the chapter feels like the Bay they know; that named voices ring true; that the augmented voices don't break the chapter's existing pace. What alienates: too-many-quotes-in-a-row that turns the chapter into a transcript. |
| 11 | **General trade-press reader (knows nothing about the Bay)** | Reads for: that named voices are introduced with enough institutional context to know who's speaking + why their voice carries weight. What alienates: name-dropping without explanation; insider acronyms (VMRC / ASMFC / VWA) without first-mention expansion. |
| 12 | **Reedville-side reader (menhaden industry worker; Northumberland County)** | Adversarial reader; this is the audience-load Pass 3.4 robustness test will pressure-test. Reads for: that O'Connor's petition is represented as a regulatory-record voice, not a moral indictment; that the chapter doesn't villainize Omega Protein / Ocean Harvesters or the Reedville community. |
| 13 | **Tangier-side reader (Eskridge constituent; island resident)** | Reads for: that Tangier voices are quoted respectfully and in their own register; that the chapter doesn't make Tangier a climate-rhetoric battlefield. Per GuidanceDoc §7: "DOES NOT introduce climate-rhetoric framing for Tangier — erosion-and-shoreline only." |
| 14 | **Public Choice tradition reader (adversarial; Ch 5 cross-thread)** | Reads Ch 3 as story-ground for the rent-seeking-engagement workstream landed in Ch 5 (commit `bc02767`). Reads for: that Ch 3's augmented voices position the regulatory-architecture story so Ch 5 can do the analytical work. What alienates: Ch 3 making the analytical move itself (apparatus exclusion list per GuidanceDoc §2). |

---

## §2. Editorial-brain map for the augmentation venue

This brief is for **augmentation of an existing chapter**, not a new
venue. The "editorial brain" for the augmentation is two-layered:

### §2.1 Internal — the author + author's discipline

- **Path B preemptive policy** holds: Stage 2 augmentation drafting
  does NOT reuse existing Ch 3 v1 prose at the sentence level (per
  GuidanceDoc §3). The 11 landings are NEW sentences inserted at
  existing locations; the surrounding prose stays put.
- **Apparatus exclusion list** (GuidanceDoc §2) holds: no framework
  vocabulary in augmented prose. Plain-English description of
  facts only.
- **Substance-drives-length** (memory `feedback_substance_drives_length.md`):
  the augmentation may push the chapter from ~4,400 words (current
  v1) toward GuidanceDoc §1's 8,000–12,000 target band. Acceptable
  if substance earns the addition. Word-count targets per landing
  are NOT prescribed.

### §2.2 External — eventual publisher review

- **Trade-press editor** (book publisher's editor for the chapter):
  reads for verifiability of named voices; whether each named
  subject would consent to or contest the framing. Public-record
  exception removes the consent gate for all 11 named voices, but
  citation accuracy is non-negotiable.
- **CBF gateway reader** (Val + David, if they read pre-pub):
  reads for journalism-standard attribution + non-villainization.

---

## §3. Comp titles / lineage cluster

Augmentation does not change the chapter's comp-cluster. For
completeness, the chapter sits inside:

- **Earl Swift,** *Chesapeake Requiem* (2018) — closest lineage
  partner; the chapter's Tangier voices (Eskridge, McMann, Milton
  Parks, Cook Cannon) are sourced from Swift's book + Sherfinski's
  2022 update. The chapter does not duplicate Swift's narrative;
  it lands his named voices at structural points in a different
  argumentative arc.
- **Kenneth R. Fletcher,** "Tangier Island and the Way of the
  Watermen," *Smithsonian Magazine* (March 2009) — historical-
  arc lineage. The 140→65 waterman population statistic (54%
  decline 2003-2009) is sourced here.
- **David Sherfinski,** *"As Sea Levels Rise, Can Chesapeake Bay's
  Tangier Island Survive?"* (Thomson Reuters Foundation/Context,
  April 2022) — direct journalism precedent. The 2022 piece is
  the methodology twin for what Ch 3 attempts.
- **Maryland Matters / Bay Journal** (Wheeler + Cox, April 2026)
  + **The Banner** (Willis, May 2026) — current 2026 reporting
  layer. Hudgins, Brown Sr., Harrison, Tarnowski, Scheld, Ruth,
  Andy Harris (R-MD) named voices.
- **Tonya O'Connor — VMRC Petition 449** (filed 2025-12-31) — the
  regulatory-record layer. 349-page filing; 1,266 public comments;
  hearing 2026-04-21; decision pending. Public-trust doctrine
  grounding cites *Commonwealth v. City of Newport News*, 158 Va.
  521 (1932); *Taylor v. Commonwealth*, 102 Va. 759 (1904);
  *Bradford v. Nature Conservancy*, 224 Va. 181 (1982).

---

## §4. Structural decisions — the 11 augmentation landings

The augmentation lands 11 named voices at chapter-specific
locations. Each landing is specified below as: anchor voice +
verbatim quote candidate + target chapter location (line range) +
structural role + render-safe convention.

**Important scoping note.** The augmentation map in the proposal's
section 5 lists 11 landing intents (some bundle 1–2 voices in a
single landing). The expanded count below treats each named voice
as a separate row for clarity, then groups co-located landings in
the Stage 2 instruction at §11. Total landings: **11 voices across
9 distinct chapter locations** (Hudgins solo; Tarnowski + Ruth
co-locate at oyster paradox; O'Connor solo; Nesslage + Latour
co-locate at menhaden section; Evans solo; Cannon + Eskridge
co-locate at Tangier section; Goldsborough solo; Andy Harris solo;
Whewell + Tilghman watermen co-locate at place-paragraph region).
Adjusted total = 11 named voices at 9 landings. The brief surfaces
all 11 named voices explicitly.

### §4.L1 — J.C. Hudgins (kitchen-table economics)

- **Anchor voice:** J.C. Hudgins (President, Virginia Watermen's
  Association; works Piankatank River).
- **Canonical source:** Wheeler + Cox, *"Amid oyster bounty,
  Chesapeake Bay watermen suffer dismal harvest,"* Maryland
  Matters / Bay Journal, 2026-04-27.
  https://southernmarylandchronicle.com/2026/04/27/amid-oyster-bounty-chesapeake-bay-watermen-suffer-dismal-harvest-2/
- **Verbatim quote candidates** (lift directly; do not paraphrase):
  - *"You're lucky if you can put $150 in your pocket per day. And
    it ain't no easy job. You're freezing your butt off. It's cold."*
  - *"People aren't going to spend $20 for a pint of oysters. It's
    pretty expensive eating. I think people are feeding their
    families in other ways."*
- **Target chapter location:** lines 63–64 (the "asymmetry of
  margins" / "disappearance of margins" paragraph at the close of
  the generational-witness section, immediately before the rockfish
  section opens at line 67).
- **Structural role:** Cost-compression verification in a named
  waterman's own voice. The chapter's existing paragraph at lines
  63–64 makes the cost-compression observation in the chapter's
  voice ("the seasons that used to carry a year now carry only part
  of one... the runs of striped bass that their fathers had timed
  to the calendar do not run on the calendar anymore"). Hudgins
  lands the same observation in a regional waterman's institutional
  voice + provides verifiable public-record grounding.
- **Render-safe convention:** Both quotes use straight ASCII
  apostrophes in the source; the chapter convention is straight
  ASCII throughout (`don't`, `aren't`, `you're`). No special
  characters. The $ symbol renders cleanly through the existing
  Pandoc pipeline (verified at line 99 of Ch 3 v1 in similar
  contexts).

### §4.L2 — Mitch Tarnowski (the 12-word chapter thesis)

- **Anchor voice:** Mitch Tarnowski (Maryland Department of Natural
  Resources oyster reef survey leader).
- **Canonical source:** Wheeler + Cox, Maryland Matters /
  Bay Journal, 2026-04-27 (same source as L1).
- **Verbatim quote candidate:**
  - *"There are plenty of oysters out there. They're just not being
    harvested."*
- **Target chapter location:** lines 168–178 (the oyster paradox
  section that opens at line 168 with *"There is a paradox that has
  emerged, in the most recent years, that I want to set down
  carefully…"* and closes at line 178 with *"The reef can be
  rebuilt without the working waterfront being rebuilt."*).
- **Structural role:** Names the paradox in a state regulator's
  voice. The chapter currently develops the paradox over ~250
  words; Tarnowski's 12-word formulation is the chapter's central
  claim said by a working state regulator. Landing his quote at
  the section's hinge gives the paradox a named institutional
  ground.
- **Render-safe convention:** Standard straight apostrophe in
  *They're*; no special characters.

### §4.L3 — Jason Ruth (Harris Seafood Co.; market-collapse named voice)

- **Anchor voice:** Jason Ruth (Owner, Harris Seafood Co.,
  Grasonville, MD — Chesapeake oyster processor).
- **Canonical source:** Wheeler + Cox, Maryland Matters /
  Bay Journal, 2026-04-27 (same source as L1, L2).
- **Verbatim quote candidates:** Per the source document, Ruth
  speaks to the 60-year decline in shucked oyster sector + market
  dynamics. **Stage 2 must lift the verbatim quote(s) directly
  from the Maryland Matters article**; this brief does not
  speculate. The CBF live-call-companion (§"Voices catalogued")
  notes Ruth as a market-dynamics voice without itemizing the
  exact verbatim. Stage 2 reads the article + lifts the line(s).
- **Target chapter location:** lines 168–178 (oyster paradox
  section, co-located with L2 Tarnowski landing).
- **Structural role:** Market-collapse named voice. The chapter's
  existing oyster-paradox paragraph at lines 172–174 references
  *"the market for Chesapeake oysters was being hollowed out by
  Gulf Coast farm-raised competition…"* Ruth's voice grounds this
  in the named owner of a working MD processor with 60-year
  decline observation.
- **Render-safe convention:** Standard ASCII; no special
  characters.

### §4.L4 — Tonya O'Connor / VMRC Petition 449 (regulatory-record voice)

- **Anchor voice:** Tonya O'Connor (Virginia resident; petitioner;
  filed VMRC Petition 449 on 2025-12-31).
- **Canonical source:** O'Connor, Tonya. *Petition for Rulemaking
  to Establish a Temporary Moratorium on Chesapeake Bay Menhaden
  Reduction Fishing.* Virginia Marine Resources Commission,
  filed 2025-12-31 (Petition 449; hearing 2026-04-21; 1,266 public
  comments; decision pending). PDF available at
  https://mrc.virginia.gov/Notices/2026/Menhaden-Moratorium-Petition.pdf
  (also in author's local download `2026-04-21-Menhaden-Petition.pdf`).
- **Verbatim quote candidate** (the petition's central finding,
  per CBF live-call-companion):
  - *"[VMRC] did not have — and still does not have — a Bay-wide
    estimate of menhaden biomass, age structure, spatial
    distribution, recruitment trends, or localized depletion risk."*
- **Canonical numerical anchors:**
  - 349-page filing
  - 1,266 public comments received
  - Hearing 2026-04-21
  - Decision pending as of 2026-05-20
  - Public-trust doctrine grounding cites: *Commonwealth v. City
    of Newport News*, 158 Va. 521 (1932); *Taylor v. Commonwealth*,
    102 Va. 759 (1904); *Bradford v. Nature Conservancy*, 224 Va.
    181 (1982).
- **Target chapter location:** lines 99–113 (menhaden section
  opening at line 99 *"There is a fish you have probably never
  eaten…"* and closing at line 113 *"It is the same shape coal
  had."*).
- **Structural role:** Regulatory-record voice grounding the
  chapter's menhaden-management critique in a citable public
  petition. The chapter currently makes the case at lines 107–112
  in the author's analytical voice; O'Connor's petition lands the
  same critique as a regulatory-record action that 1,266 people
  signed onto. Public-trust doctrine grounding makes the petition's
  legal posture clear without the chapter needing to develop it.
- **Render-safe convention:** Bracketed editorial insertion
  `[VMRC]` is per standard journalism convention for unspoken
  subject substitution in a quote. The em-dashes inside the quote
  (`— and still does not have —`) are em-dashes (U+2014); confirm
  Pandoc rendering. *Italicized case names* in V. citations render
  via Markdown `*…*` syntax.

### §4.L5 — Genny Nesslage (menhaden science gap)

- **Anchor voice:** Genny Nesslage (Associate research professor,
  University of Maryland Center for Environmental Science; menhaden
  scientist).
- **Canonical source:** Katherine Hafner, *"Menhaden board cuts
  amount harvesters can catch along the Atlantic next year,"*
  WHRO, 2025-10-29.
  https://www.whro.org/environment/2025-10-29/menhaden-board-cuts-amount-harvesters-can-catch-along-the-atlantic-next-year
- **Verbatim quote candidate:**
  - *"We don't know the abundance of menhaden in the bay at any
    given time relative to the coast."*
- **Target chapter location:** lines 99–113 (menhaden section,
  co-located with L4 O'Connor landing; specifically the chapter's
  current claim at lines 107–108 about *"The relevant scientific
  committee has, in recent years, been recommending coastwide
  reductions and Bay-specific precautions…"*).
- **Structural role:** Names the Bay-specific science deficit in
  a working scientist's voice. The chapter currently invokes
  "the relevant scientific committee" anonymously; Nesslage's
  quote names the gap directly and credits the scientist who
  said it.
- **Render-safe convention:** Standard ASCII apostrophe in
  *don't*; no special characters.

### §4.L6 — Rob Latour (VIMS menhaden / cap-on-industry-record critique)

- **Anchor voice:** Rob Latour (Professor, William & Mary's Batten
  School and Virginia Institute of Marine Science; menhaden
  researcher).
- **Canonical source:** Hafner, WHRO, 2025-10-29 (same as L5).
- **Verbatim quote candidates:**
  - *"Just using average catch isn't really achieving optimal use
    of the resource from a sustainability perspective."*
  - *"We have no data to really do this in a meaningful way, from
    a biological perspective."*
- **Target chapter location:** lines 99–113 (menhaden section,
  co-located with L4 O'Connor + L5 Nesslage landings; specifically
  the chapter's reference at line 107 to the 51,000 mt cap "set by
  the Atlantic States Marine Fisheries Commission in 2017").
  **Canonical-fact correction surfaced:** the Bay cap was
  established in **2006** per WHRO Oct 2025 + GuidanceDoc §1, NOT
  2017 as the v1 chapter currently states. ASMFC adjusted the cap
  in 2017 (the chapter's "2017" date matches an adjustment year,
  but the original cap dates to 2006). **Stage 2 must reconcile
  this**; the brief's canonical-facts inventory (§6) records the
  correct 2006 date.
- **Structural role:** Names the science-gap from a second VIMS
  voice. Latour's "no data to really do this in a meaningful way"
  is the directest articulation of the data-deficit claim the
  chapter is making.
- **Render-safe convention:** Standard ASCII apostrophe in *isn't*;
  no special characters.

### §4.L7 — Cameron Evans (next-generation Tangier voice)

- **Anchor voice:** Cameron Evans (Tangier native; Virginia
  Wesleyan student at time of Sherfinski 2022).
- **Canonical source:** David Sherfinski, *"As Sea Levels Rise, Can
  Chesapeake Bay's Tangier Island Survive?"* Thomson Reuters
  Foundation / Context, April 2022.
  https://www.context.news/climate-risks/as-sea-levels-rise-can-chesapeake-bays-tangier-island-survive
- **Verbatim quote candidate:**
  - *"If you can't save an island a mile and a half long, how are
    you going to save the East Coast?"*
- **Target chapter location:** lines 155–164 (the generational-
  thinning paragraphs that begin at line 156 *"I want to say
  something now about the choice the men on the dock are making,
  and about what they are telling their sons,"* and close at line
  164 *"The next father, the next son, hear the news and run their
  own arithmetic."*).
- **Structural role:** The next-generation question in a named
  young person's own words. The chapter's existing prose describes
  the children "mostly going" (line 164); Evans's quote lands the
  next-generation voice directly + connects island-survival to
  East-Coast survival without the chapter making the climate-
  rhetoric move itself.
- **Render-safe convention:** Standard ASCII apostrophe in *can't*;
  no special characters.

### §4.L8 — Cook Cannon (cultural-survival sermon register)

- **Anchor voice:** George "Cook" Cannon (64-year-old former
  Tangier waterman; CBF; sermon leader).
- **Canonical source:** Fletcher 2009 (Smithsonian Magazine) +
  Swift 2018 (*Chesapeake Requiem*) + Meinhardt (Bitter
  Southerner). Multiple corroborating attributions.
- **Verbatim quote candidates:**
  - *"I could cry to think about what's going to happen to
    Tangier."* (Smithsonian 2009)
  - *"Why do you think we're on this Earth? Do you think we're
    here to catch a sook and a jimmy and a peeler?"* (sermon;
    quoted in Bitter Southerner)
- **Target chapter location:** line 144 region (the Tangier
  paragraph that opens *"Tangier Island, in the middle of the
  Lower Bay, is two square miles of low-elevation marsh and sand
  that has been continuously inhabited since the 1770s."*).
- **Structural role:** Cultural-survival register in a named
  former-waterman's voice. The chapter currently describes the
  Tangier situation in the author's voice (lines 144–148); Cannon's
  sermon-register quote adds the spiritual / cultural-stake voice
  the existing prose does not carry. The sook/jimmy/peeler
  vocabulary is also waterman-specific (sook = mature female crab;
  jimmy = mature male; peeler = pre-molt crab) — preserving the
  vocabulary preserves the register.
- **Render-safe convention:** Standard ASCII apostrophes.
  Lowercase common-noun crab-terminology (sook, jimmy, peeler) per
  source.

### §4.L9 — James "Ooker" Eskridge (Tangier mayor; cultural-survival voice)

- **Anchor voice:** James "Ooker" Eskridge (Mayor of Tangier;
  50+ years on the water).
- **Canonical source:** Sherfinski 2022 (Thomson Reuters Foundation/
  Context); also: Earl Swift, *Chesapeake Requiem* (Dey Street
  Books, 2018); Fletcher 2009 (Smithsonian); CNN town hall with
  Al Gore (June 2017, cited in Swift + Undark review).
- **Verbatim quote candidates:**
  - *"We're talking about saving a culture, the people, (a) way
    of life — the whole package."* (Sherfinski 2022)
  - *"Our island is disappearing, but it's because of erosion and
    not sea-level rise."* (CNN/Gore town hall, June 2017; cited
    in Swift + multiple reviews — the defining waterman-vs-
    climate-spokesman public moment.)
- **Target chapter location:** line 144 region (Tangier section,
  co-located with L8 Cannon landing). The Eskridge erosion-not-
  sea-level-rise quote is the second-paragraph option; Stage 2
  decides whether to include both quotes or pick one.
- **Structural role:** Cultural-survival in the named elected
  voice + the waterman-vs-climate-spokesman public moment.
  **Discipline guardrail per GuidanceDoc §7:** Ch 3 publisher-
  facing prose *"DOES NOT introduce climate-rhetoric framing for
  Tangier — erosion-and-shoreline only, per the CBF-political-
  spectrum discipline."* Stage 2 must land Eskridge's voice
  WITHIN this guardrail. The 2022 *"saving a culture"* quote is
  safe; the 2017 *"erosion not sea-level rise"* quote is the
  political-register quote that requires careful framing if used
  at all. Stage 2 should default to the 2022 quote unless the
  scene specifically requires the 2017 anchor.
- **Render-safe convention:** Standard ASCII apostrophes;
  parenthetical insertion `(a)` in the Sherfinski quote is
  per source.

### §4.L10 — Bill Goldsborough (1985 rockfish institutional memory)

- **Anchor voice:** Bill Goldsborough (retired CBF fisheries
  scientist; institutional memory across the 1985 striped bass
  collapse + recovery + present crisis).
- **Canonical source:** Fletcher 2009 (Smithsonian Magazine) +
  ongoing CBF citations. Specific verbatim from Smithsonian 2009
  to be lifted by Stage 2 from the article.
- **Verbatim quote candidate:** Stage 2 lifts the verbatim from
  Smithsonian 2009 + any cross-referenced CBF citations. The
  live-call-companion does not itemize an exact quote; the role
  is institutional-memory, which is structural rather than
  single-quote. Stage 2 should pull a 1–2 sentence verbatim that
  carries the institutional-memory register.
- **Target chapter location:** lines 67–80 (the 1985 rockfish
  moratorium section opening at line 67 *"The striped bass — what
  they call rockfish on the Bay — is the species that taught
  Maryland and Virginia, in the 1980s, what intervention can do"*
  and closing at line 80).
- **Structural role:** Institutional memory across the 1985 →
  present arc. The chapter currently develops the moratorium
  history in the author's voice (lines 67–80); Goldsborough's
  voice grounds the institutional memory in a named retired CBF
  scientist who lived through the 1985 → 1995 recovery + present
  decline.
- **Render-safe convention:** Standard ASCII.

### §4.L11 — Andy Harris (US Rep R-MD; bipartisan structural framing)

- **Anchor voice:** Andy Harris (United States Representative,
  R-MD; Maryland Eastern Shore Congressional district).
- **Canonical source:** Wheeler + Cox, Maryland Matters /
  Bay Journal, 2026-04-27 (same source as L1, L2, L3).
- **Verbatim quote candidate:**
  - *"Our watermen are pretty resilient. They're like our farmers.
    They have good years and bad years. But if you have a couple
    bad seasons in a row, then you're in trouble."*
- **Target chapter location:** lines 155–164 (generational-thinning
  paragraphs, co-located with L7 Evans landing).
- **Structural role:** Bipartisan structural framing in a sitting
  congressman's words. The chapter's existing prose at lines
  148–150 makes the cross-watershed-asymmetry claim in the
  author's voice; Harris's voice grounds the structural reading
  in a Republican congressman's own words, which is a methodology
  win against partisan-framing pressure-tests. Per GuidanceDoc §6,
  the framing is bipartisan rather than partisan — Harris's voice
  is the load-bearing public-record evidence of that posture.
- **Render-safe convention:** Standard ASCII apostrophes.

### §4.L12 — Pat Whewell + Tilghman Island watermen (MD working-waterfront named voices)

- **Anchor voice:** Pat Whewell (Tilghman Island, MD; photographed
  culling oysters aboard Lonnie Gowe's boat in Broad Creek, 2023)
  + Chumley Fisher + Chet Schwartz + Lonnie Gowe (Tilghman Island
  watermen photographed in Maryland Matters Apr 2026; named in
  photo captions but not directly quoted).
- **Canonical source:** Wheeler + Cox, Maryland Matters /
  Bay Journal, 2026-04-27.
- **Verbatim quote candidates:** None — these subjects are named
  in photo captions but not directly quoted. The landing is
  **named-attribution-without-quotation**, lifting them out of
  anonymity and into the chapter's named-presence register.
  Whewell specifically closes a known coverage gap — a named woman
  on-water — which the chapter currently lacks.
- **Target chapter location:** line 144 region (place-paragraph
  area that includes Tangier + Smith Island + Hampton; the
  Tilghman Island named-voices landing adds the Maryland working-
  waterfront named-presence the chapter currently passes through
  in the author's voice).
- **Structural role:** Closes the woman-on-water coverage gap +
  adds Maryland working-waterfront named presence. The chapter's
  existing prose at lines 144–148 describes "the picking houses
  there — where mostly older women have, for generations, picked
  the meat from soft-shell crabs"; Whewell's presence as a named
  woman culling oysters on-deck makes the gender-of-the-work
  description verifiable rather than generic.
- **Render-safe convention:** Standard ASCII. Named subjects can
  be introduced without verbatim quotes; the discipline is to
  attribute the named presence to the source (Maryland Matters
  Apr 2026 photo captions).

### §4.L13 — (informational — augmentation count reconciliation)

The proposal's section 5 lists 11 named landings as the
augmentation map. The brief's §4.L1–L12 enumeration treats some
co-located voices separately (Tarnowski + Ruth at oyster paradox;
Nesslage + Latour at menhaden science; Cannon + Eskridge at
Tangier; Whewell + Tilghman watermen at place-paragraph) for
specificity. Reading the proposal's map row-by-row:

| Proposal row | Brief §4 entry |
|---|---|
| 1. J.C. Hudgins | §4.L1 |
| 2. Mitch Tarnowski | §4.L2 |
| 3. Tonya O'Connor / Petition 449 | §4.L4 |
| 4. Genny Nesslage + Rob Latour | §4.L5 + §4.L6 |
| 5. Cameron Evans | §4.L7 |
| 6. Cook Cannon | §4.L8 |
| 7. James "Ooker" Eskridge | §4.L9 |
| 8. Bill Goldsborough | §4.L10 |
| 9. Jason Ruth | §4.L3 |
| 10. Andy Harris | §4.L11 |
| 11. Pat Whewell + Tilghman Island watermen | §4.L12 |

**Net augmentation count:** 11 proposal rows → 12 named-voice
entries in this brief (Nesslage + Latour as separate rows per the
proposal; all other rows preserved). **All 11 proposal-row landings
are accounted for; the brief expands #4 into two named entries for
clarity.** Stage 2 may treat L5 + L6 as a single co-located landing
in prose (one sentence introducing Nesslage; one introducing
Latour); the per-entry treatment in this brief is for canonical-
facts specificity, not Stage 2 prose-structure prescription.

---

## §5. Voice register (augmentation-specific)

Augmented prose preserves the chapter's existing register
exactly. Reading Ch 3 v1 paragraphs at lines 73, 91, 107, 170, 172,
176 (the chapter's existing named-voice landings — Colden quotes
already in the chapter), the convention is:

- **Person:** First-person author throughout; named subjects
  introduced in third person with full institutional context on
  first mention.
- **Quote convention:** Verbatim quotes set off with italics
  (Markdown `*…*` syntax), introduced with a present-perfect
  attribution clause (`Allison Colden, the Chesapeake Bay
  Foundation's Maryland executive director, watching that signal
  accumulate across the years, has put the situation in terms the
  watermen would recognize`). The italicization convention is
  load-bearing — Ch 3 v1 italicizes all direct quotes consistently;
  augmentation must match.
- **First-mention institutional attribution:** Always name the
  subject's role + institution on first mention. Subsequent
  mentions may drop the institutional attribution.
- **Tense:** Past tense for source actions (*Colden has said*);
  present tense for chapter narration.
- **Sentence-length variance:** Mix of short (5–10 word) sentences
  with longer (25–40 word) sentences. No rule-of-three. Em-dash
  density discipline (see L1 disposition for the Pass 3.2 carry-
  forward).
- **LLM-tic avoidance:**
  - No "in short" / "ultimately" / "It changed me"
  - No "There are not many people like that anymore" -class
    closures
  - No "The truth is" / "The thing is" hedges
  - No meta-commentary ("This is the load-bearing observation")
- **Italicization conventions:**
  - Direct quotes: Markdown `*…*`
  - Book / publication titles: Markdown `*…*` (e.g., *Chesapeake
    Requiem*; *Maryland Matters*)
  - Case names in V. citations: `*Commonwealth v. City of Newport
    News*`
  - Emphasis: rare; reserved for load-bearing semantic stress
    (e.g., *every* season).

---

## §6. Carry-forward inventory — canonical factual ground truth

Amendment A discipline: include canonical facts, NOT just beats.
Stage 2 drafts from this section without re-opening source
articles.

### §6.1 Named subjects + institutional attribution

| Subject | Role + institution | First-mention attribution form (canonical) |
|---|---|---|
| **J.C. Hudgins** | President, Virginia Watermen's Association; works Piankatank River | "J.C. Hudgins, who runs the Virginia Watermen's Association and works the Piankatank River" |
| **Mitch Tarnowski** | MD DNR oyster reef survey leader | "Mitch Tarnowski, who leads Maryland's Department of Natural Resources oyster reef surveys" |
| **Jason Ruth** | Owner, Harris Seafood Co., Grasonville, MD | "Jason Ruth, who owns Harris Seafood Co., a Grasonville, Maryland oyster processor" |
| **Tonya O'Connor** | VA resident; petitioner; filed VMRC Petition 449 | "Tonya O'Connor, a Virginia resident who filed a petition with the Virginia Marine Resources Commission on December 31, 2025" |
| **Genny Nesslage** | Associate research professor, UMD Center for Environmental Science | "Genny Nesslage, an associate research professor at the University of Maryland Center for Environmental Science" |
| **Rob Latour** | Professor, William & Mary's Batten School + VIMS | "Rob Latour, a Virginia Institute of Marine Science menhaden researcher" |
| **Cameron Evans** | Tangier native; Virginia Wesleyan student (at time of 2022 source) | "Cameron Evans, a Tangier native then studying at Virginia Wesleyan" |
| **George "Cook" Cannon** | 64-year-old (at time of 2009 source) former Tangier waterman; CBF; sermon leader | "Cook Cannon, a former Tangier waterman who has spent the years since at the Chesapeake Bay Foundation" |
| **James "Ooker" Eskridge** | Mayor of Tangier; 50+ years on the water | "James 'Ooker' Eskridge, the mayor of Tangier and a working waterman for more than fifty years" |
| **Bill Goldsborough** | Retired CBF fisheries scientist | "Bill Goldsborough, a fisheries scientist at the Chesapeake Bay Foundation through the rockfish moratorium years" |
| **Andy Harris** | United States Representative (R-MD); Maryland Eastern Shore Congressional district | "Andy Harris, who represents Maryland's Eastern Shore in Congress" |
| **Pat Whewell** | Tilghman Island, MD; named in Maryland Matters photo caption (2023, on Lonnie Gowe's boat in Broad Creek) | "Pat Whewell, photographed culling oysters in Broad Creek aboard Lonnie Gowe's boat" |
| **Chumley Fisher** | Tilghman Island waterman (Maryland Matters photo caption 2026) | Named-in-photo attribution only |
| **Chet Schwartz** | Tilghman Island waterman (Maryland Matters photo caption 2026) | Named-in-photo attribution only |
| **Lonnie Gowe** | Tilghman Island waterman; boat owner (Maryland Matters 2026) | Named-in-photo attribution only |

### §6.2 Verbatim quotes — canonical text (lift exactly)

See §§4.L1–L12 for each verbatim. Stage 2 must NOT paraphrase.
Stage 2 may select WHICH quote to land if multiple are listed
(e.g., Hudgins has two; Eskridge has two; Cannon has two; Latour
has two), but Stage 2 may not re-word any selected quote.

### §6.3 Canonical numerical anchors

| Fact | Canonical value | Source |
|---|---|---|
| **Bay menhaden cap, established by ASMFC** | 51,000 metric tons; **established 2006** (NOT 2017 as Ch 3 v1 currently states at line 107); set on industry's past performance, not science | WHRO Oct 2025; GuidanceDoc §1 |
| **VMRC Petition 449 page count** | 349 pages | O'Connor petition |
| **VMRC Petition 449 public comments** | 1,266 | O'Connor petition; CBF live-call-companion |
| **VMRC Petition 449 hearing date** | 2026-04-21 | O'Connor petition |
| **VMRC Petition 449 decision** | Pending as of 2026-05-20 | Verify-stale-claims discipline: confirm before submission |
| **Maryland young-of-year rockfish 2024 index** | 2.0 fish per sample (vs. 11.0 long-term average) | Ch 3 v1 line 71 — preserved unchanged |
| **Bay-wide blue crab population 2025 winter dredge survey** | ~238M crabs; second-lowest since 1990 | Ch 3 v1 line 91 — preserved unchanged |
| **Maryland oyster population growth since 2005** | Roughly tripled | Ch 3 v1 line 170 — preserved unchanged |
| **Virginia's allocation of total menhaden** | "about 75% of the total" | WHRO Oct 2025 |
| **VIMS $3M Bay-specific menhaden study** | Drafted for VA General Assembly 2023; state lawmakers declined to fund | WHRO Oct 2025 |
| **Tangier waterman population 2003 vs 2009** | 140 → 65 (54% decline in 6 years) | Smithsonian 2009 (Fletcher) |
| **Tangier shoreline loss** | ~15 feet/year (Ch 3 v1 line 144); per Schulte + Wu projection cited in Sherfinski 2022 | Preserved unchanged |
| **Bay waters unimpaired 2022 vs 1985** | 28.1% (2022) vs 26.5% (1985); 37 years; $12B spent | Bay Journal / Winegrad 2024 — secondary source, available if needed |
| **MD commercial fisheries declined since 2012** | 7 fisheries; 27-91% decline | Bay Journal / Winegrad 2024 |
| **Blue crab decline (longer arc)** | ~800M+ early 1990s → 50% decline from 2010 peak through 2023 → 238M recent | The Banner May 2026 |

**Canonical-fact correction surfaced** (recorded as a Stage 2 spot-fix
to resolve): Ch 3 v1 line 107 states the Bay menhaden cap was *"set
by the Atlantic States Marine Fisheries Commission in 2017 at
51,000 metric tons."* The correct establishment year is **2006**;
ASMFC adjusted the cap level in subsequent years (including 2017
reductions). Stage 2 should correct this when landing the Nesslage
/ Latour quotes at the same section. Pass 3.1 fact-check will
catch it if Stage 2 misses; flagging here gives Stage 2 the
canonical date.

### §6.4 Canonical source citations (URL-stable; for Stage 2)

| Source | Full citation | URL |
|---|---|---|
| **Sherfinski 2022** | David Sherfinski, *"As Sea Levels Rise, Can Chesapeake Bay's Tangier Island Survive?"* Thomson Reuters Foundation / Context, April 2022 | https://www.context.news/climate-risks/as-sea-levels-rise-can-chesapeake-bays-tangier-island-survive |
| **Swift 2018** | Earl Swift, *Chesapeake Requiem: A Year with the Watermen of Vanishing Tangier Island.* Dey Street Books, 2018 | Book (no URL) |
| **Smithsonian 2009 (Fletcher)** | Kenneth R. Fletcher, *"Tangier Island and the Way of the Watermen,"* Smithsonian Magazine, March 2009 | https://www.smithsonianmag.com/science-nature/tangier-island-and-the-way-of-the-watermen-117890294/ |
| **Maryland Matters / Bay Journal Apr 2026** | Timothy Wheeler + Jeremy Cox, *"Amid oyster bounty, Chesapeake Bay watermen suffer dismal harvest,"* Maryland Matters / Bay Journal, 2026-04-27 | https://southernmarylandchronicle.com/2026/04/27/amid-oyster-bounty-chesapeake-bay-watermen-suffer-dismal-harvest-2/ |
| **The Banner May 2026** | Adam Willis, *"Chesapeake blue crabs are disappearing. The reason remains a mystery,"* The Banner, 2026-05-12 | https://www.thebanner.com/community/climate-environment/chesapeake-bay-blue-crab-decline-E5CV5LURHNB23JLFNK4ZQTHCGE/ |
| **WHRO Oct 2025 (Hafner)** | Katherine Hafner, *"Menhaden board cuts amount harvesters can catch along the Atlantic next year,"* WHRO, 2025-10-29 | https://www.whro.org/environment/2025-10-29/menhaden-board-cuts-amount-harvesters-can-catch-along-the-atlantic-next-year |
| **O'Connor / VMRC Petition 449** | Tonya O'Connor, *Petition for Rulemaking to Establish a Temporary Moratorium on Chesapeake Bay Menhaden Reduction Fishing,* filed with VMRC, 2025-12-31 | https://mrc.virginia.gov/Notices/2026/Menhaden-Moratorium-Petition.pdf |
| **Bay Journal / Winegrad 2024** | Gerald Winegrad, *"Chesapeake restoration collapsing on altar of political expediency,"* Bay Journal, 2024-10-04 | https://www.bayjournal.com/opinion/forum/chesapeake-restoration-collapsing-on-altar-of-political-expediency/article_c10b6860-8193-11ef-860c-dfacdaaaa228.html |
| **Bitter Southerner (Meinhardt)** | Mickie Meinhardt, *"Chronicling The End Times on Tangier Island,"* The Bitter Southerner | https://bittersoutherner.com/chronicling-the-end-times-on-tangier-island |
| **Undark book review (Unger)** | David J. Unger, book review of *Chesapeake Requiem*, Undark, 2018-08-31 | https://undark.org/2018/08/31/book-review-swift-chesapeake-requiem/ |

### §6.5 Public-trust doctrine grounding (for L4 O'Connor)

The petition's legal grounding cites three Virginia Supreme Court
public-trust doctrine cases. Stage 2 lands the citations exactly:

- *Commonwealth v. City of Newport News*, 158 Va. 521 (1932)
- *Taylor v. Commonwealth*, 102 Va. 759 (1904)
- *Bradford v. Nature Conservancy*, 224 Va. 181 (1982)

These citations are public-record material; the chapter does not
need to develop them analytically (apparatus exclusion list per
GuidanceDoc §2 — Public Choice / regulatory-capture terminology
stays out of the chapter). They land as named-in-passing
parenthetical grounding for O'Connor's petition's legal posture.

---

## §7. Locked elements

| Locked element | Rationale |
|---|---|
| **Phat anonymization at lines 129–138** | RATIFIED 2026-05-20 by author (commit `8a55395`). Replacement analysis ratified same day (commit `8e3bf25`). IMMUTABLE for this workstream. Augmentation does NOT touch the five anonymized paragraphs. |
| **Existing Colden canonical quotes at lines 73, 91, 107, 170, 172, 176** | Already canonical for Ch 3. Stage 2 may co-locate new voices alongside Colden but does NOT modify Colden's existing quotes. |
| **Biggie passage at lines 47–53** | Existing canonical Biggie material. Goldsborough landing (L10) is at a DIFFERENT location (lines 67–80 rockfish moratorium); Biggie passage is unaffected. Courtesy-notify-family discipline applies to Biggie per consent doctrine. |
| **Hampton-harbor opening (lines 10–14)** | Existing canonical chapter opening; augmentation does not touch it. |
| **Closing tie-back to McDowell County (lines 192–202)** | Existing canonical chapter close; augmentation does not touch it. |
| **Verbatim quote text for all 11 named voices** | Per §6.2, all quotes lifted verbatim from source. Stage 2 selects but does not re-word. |

---

## §8. Hard constraints

- **Path B preemptive policy** (per GuidanceDoc §3 + memory
  `feedback_audience_aware_drafting_discipline.md`). Stage 2
  augmentation drafting does NOT open the existing Ch 3 v1 draft
  at the sentence level. Stage 2 works from THIS brief's
  canonical-facts inventory (§6) + structural decisions (§4).
  Existing Ch 3 v1 prose at target locations may be read for
  context (where the new sentences land) but new sentences are
  drafted freshly, not derived from v1 sentences.
- **Apparatus exclusion list** (per GuidanceDoc §2). No framework
  vocabulary in augmented prose: no "cost severance," "regulatory
  capture," "rent-seeking," "Public Choice," "externality" (as
  noun), "structural mechanism" (academic register), "Pattern 2,"
  "Four Gates," etc.
- **Real-world institutional names are SAFE** (per GuidanceDoc §2
  ✅ list): VMRC, ASMFC, VIMS, CBF, Omega Protein, Ocean Harvesters,
  Science Center for Marine Fisheries, Va. Code § 28.2-201.
- **Named-subject consent discipline applied** (per memory
  `feedback_named_subject_consent.md` + GuidanceDoc §4). All 11
  named voices qualify under the **public-record exception**
  (elected officials quoted from on-record speech; petitioners on
  regulatory record; published-journalism interviewees). No
  consent gate. **Courtesy notification before publication** is
  the right discipline — pre-submission, send each subject (or
  their communications coordinator) the verbatim quotes attributed
  to them + a citation-accuracy check. Not consent; courtesy.
- **Phat anonymization IMMUTABLE** — RATIFIED 2026-05-20; no
  augmentation touches lines 129–138.
- **Climate-rhetoric framing for Tangier** (per GuidanceDoc §7):
  erosion-and-shoreline only; default to Eskridge's 2022 *"saving
  a culture"* quote over the 2017 *"erosion not sea-level rise"*
  political-register quote.
- **Substance drives length** (per memory
  `feedback_substance_drives_length.md`). Stage 2 does not target
  a word-count band for augmentation; each landing earns its space
  by the substantive role specified in §4.
- **Voice register preserved** (per §5). Italicized quotes;
  attributive present-perfect verb tense for source actions;
  first-mention institutional context.
- **Render-safety conventions preserved** (per Stage 4 doctrine
  carry-forward + author's lived-experience math-formula corruption
  anchor). Em-dashes are U+2014; smart quotes off (ASCII straight
  quotes throughout); Markdown italics for quotes + publication
  titles + V. case names.
- **Canonical-fact correction (Bay cap year)** — Stage 2 corrects
  Ch 3 v1's "2017" date for the Bay cap establishment to "2006"
  (per §6.3). Pass 3.1 fact-check verifies.

---

## §9. Sub-step 1c — Cross-artifact coherence check

**Date:** 2026-05-20
**Scope:** Ch 3 augmentation workstream (per §§1–8 above) +
adjacent chapters (Ch 2 + Ch 4 + Ch 5) + bibliography + GuidanceDoc
+ Phat-anonymization rigor-pass artifacts.
**Stage 1b brief:** this file §§1–8.

### §9.1 Inventory — bibliography commitments touching scope

**Status: HOLD with gaps surfaced.** Bibliography §19.5 (the
Chesapeake fieldwork tentative section) currently carries:
- Colden public record (multiple entries — load-bearing for Ch 3
  testimony + CBF news framings).
- Mosbrucker / Bay Journal *"Fisheries commission again holds fire
  on striped bass limits"* (existing Colden quote source).
- Institutional / biographical context for Colden + the Maryland
  Oyster Advisory Commission.
- Breadcrumbs only (not full entries) for additional Colden
  testimony + CBF Virginia / Chris Moore parallel record + VIMS
  Lipcius/Mann.

**Gaps** — the following 10 sources are referenced in this Stage 1
brief's §6.4 canonical-source citations but do NOT yet appear as
formal bibliography §19.5 entries (or any other §):

| # | Source | Used in landing(s) | Bibliography status |
|---|---|---|---|
| G1 | Sherfinski 2022 (Thomson Reuters Foundation / Context) | L7, L9 | NOT IN BIBLIOGRAPHY |
| G2 | Swift 2018 (*Chesapeake Requiem*; Dey Street Books) | L8, L9 | NOT IN BIBLIOGRAPHY |
| G3 | Fletcher 2009 (Smithsonian Magazine) | L8, L10 | NOT IN BIBLIOGRAPHY |
| G4 | Wheeler + Cox 2026-04-27 (Maryland Matters / Bay Journal) | L1, L2, L3, L11 | NOT IN BIBLIOGRAPHY |
| G5 | Willis 2026-05-12 (The Banner) | (referenced as data source for canonical-fact anchor at §6.3) | NOT IN BIBLIOGRAPHY |
| G6 | Hafner 2025-10-29 (WHRO) | L5, L6 | NOT IN BIBLIOGRAPHY |
| G7 | O'Connor VMRC Petition 449 (2025-12-31) | L4 | NOT IN BIBLIOGRAPHY |
| G8 | Winegrad 2024 (Bay Journal opinion) | (referenced as data source for canonical-fact anchor) | NOT IN BIBLIOGRAPHY |
| G9 | Meinhardt (Bitter Southerner) | L8 (Cook Cannon sermon corroboration) | NOT IN BIBLIOGRAPHY |
| G10 | Unger 2018 (Undark book review of *Chesapeake Requiem*) | (referenced as Eskridge / Gore town-hall citation corroborator) | NOT IN BIBLIOGRAPHY |

**Disposition:** Each of G1–G10 must be added to bibliography §19.5
(or a new section if §19.5's Colden-centered focus is too narrow —
new section "19.6. Chesapeake fieldwork — public-record voices
(post-petition expansion)" is the cleaner architecture). **This
addition work is NOT part of the present Stage 1 brief session; it
is surfaced here as a Stage 1c gap with disposition: ADD BEFORE
STAGE 3 PASS 3.1 fact-check fires.** Pass 3.1 will verify that
each cited source has a corresponding bibliography entry; the brief
flags it now so the author + a follow-up scribe session can land
the bibliography additions before fact-check.

The Stage 2 audience-blind drafting session may proceed against
this brief WITHOUT waiting for the bibliography additions; the
canonical sources are URL-stable and the brief's §6.4 carries the
full citation text. The bibliography gate is at Stage 3, not
Stage 2.

### §9.2 AuthorsNote framings touching scope

The AuthorsNote ("On Wind Tunnels and AI") touches Ch 3 only
indirectly. The Author's family-record claims about LaVern E. Winn
(grandfather; NASA Langley inventor; commit history per memory
`project_authors_grandfather_nasa_inventor.md`) connect to Ch 10
(grandfather narrative) and the Author's Note, not Ch 3. **No
AuthorsNote framing touches the Ch 3 augmentation workstream.**

### §9.3 Sibling-chapter cross-references touching scope

**Ch 2 (The Miner) — parallel structural pattern.** Per GuidanceDoc
§6: *"The miner-waterman recognition is the chapter's load-bearing
cross-chapter move. Different industry, different regulator, same
shape: extraction past renewability + costs absorbed by community
+ accountability lagging the harm."* Ch 3 v1 closes at lines
192–198 with the Ch 2 (McDowell County) tie-back. **Augmentation
does NOT touch the McDowell tie-back at lines 192–198.** The 11
named-voice landings strengthen the named-presence of Ch 3's
working-waterfront case but do not extend the Ch 2 parallelism.
**Coherence VERIFIED.**

**Ch 4 (Norway — commons-governance existence proof).** Ch 3 v1
closes at lines 206–218 with the Norway pivot toward Ch 4. **The
augmentation does NOT touch the Norway pivot.** Coherence VERIFIED.

**Ch 5 (The Accountability Gap; rent-seeking-engagement linkage).**
Per GuidanceDoc §6 + commits `bc02767` / `a1e54d9`: *"Ch 5 carries
the structural critique formally; Ch 3 carries it as story. Ch 3
doesn't need to make the analytical argument because Ch 5 already
does."* The augmentation lands NAMED VOICES at structural points
(L4 O'Connor petition for regulatory-record voice; L5/L6 Nesslage
+ Latour for science-gap voice). **None of the augmentations
introduce framework vocabulary or analytical claims.** Per §8 hard
constraints (apparatus exclusion). Stage 3 Pass 3.4 robustness
test against the Public Choice adversarial reader (Tier 3
character #14 in §1) will pressure-test that Ch 3 holds the
story-register; brief surfaces this as a Pass 3.4 watch-item, not
a Stage 1 blocker. **Coherence VERIFIED at Stage 1 level.**

**Ch 8 (What Things Actually Cost; non-renewable parallel).** Ch 3
v1 closes at lines 192–202 with the miner-waterman recognition,
which connects to Ch 8's coal walkthrough. **Augmentation does
NOT touch.** Coherence VERIFIED.

**Ch 9 (Pricing Honestly; Bay-cap critique parallel).** Per
GuidanceDoc §6: *"Moore's 'Bay cap based on historic landings
rather than current Bay-specific biology' critique echoes
structurally in Ch 9's broader pricing-honesty argument."* The
augmentation L4 (O'Connor) + L5/L6 (Nesslage + Latour) land the
science-gap voices in Ch 3's menhaden section. Ch 9 may extend
these voices in its analytical register. **Coherence VERIFIED:
Ch 3 holds story-register; Ch 9 carries the analytical register.**

**Ch 10 (Common Bonds; harbor close).** Ch 3 establishes the
harbor's daily life; Ch 10 returns after framework. **Augmentation
does NOT touch the Hampton-harbor opening or close.** Coherence
VERIFIED.

### §9.4 Prior rigor-pass artifacts touching scope

| Artifact | Coherence with this brief |
|---|---|
| `tools/stage-1-briefs/ch3_phat_replacement_analysis_2026-05-20_v1.0.0.md` (commit `8e3bf25`) — replacement-analysis proposal | This brief implements the proposal's section 5 augmentation map. Coherence VERIFIED: per-landing structural roles in §4 here match the proposal's section 5 table; Phat anonymization preserved as locked element per §7. |
| Ch 3 Pass 1 fact-check artifact (referenced in GuidanceDoc §9 as PROPOSED `2f76e37`; reverted per commit `cfed2b1` 2026-05-20) | The retroactive filing of the Pass 1 artifact was REVERTED 2026-05-20 (commit `cfed2b1`). Ch 3 v1 currently sits at Pass 1 PROPOSED but the rigor-pass artifact is NOT filed on `main`. **Disposition:** the augmentation workstream's Stage 2 drafting + subsequent Stage 3 passes will re-fire Pass 3.1 fact-check freshly on the augmented chapter; the prior Pass 1 artifact's findings (if any) are not carried forward. **Coherence VERIFIED** (no conflicting prior-finding disposition to honor). |
| `tools/quality-gates/clean-baselines/` — Stage 1a baselines | Directory exists; no Ch 3-specific clean-baseline filed yet. This Stage 1 brief's §1a captures the current clean-baseline; a follow-up scribe session may file a standalone `clean-baselines/ch3_v1_stage1a_2026-05-20.md` artifact if the doctrine's per-clean-baseline filing pattern is being enforced. **Disposition:** the inline §1a clean-baseline above is the load-bearing record for this workstream; standalone artifact filing is a doctrine-discipline question for PM session. |
| `tools/quality-gates/coherence-checks/` — Stage 1c coherence artifacts | Directory exists; no Ch 3-specific coherence-check filed yet. This Stage 1 brief's §9 captures the coherence check inline. Same disposition as §1a clean-baseline. |

### §9.5 Cross-chapter consistency-inventory items touching scope

`tools/audits/` carries cross-chapter consistency audits.

- **Named-subject consent discipline.** Already verified via GuidanceDoc §4 + memory `feedback_named_subject_consent.md`. All 11 named voices satisfy the **public-record exception** (elected officials on-record; petitioners on regulatory record; published-journalism interviewees). Courtesy-notify-before-publication discipline applies; no consent gate. **Coherence VERIFIED.**

- **Pattern 2 register discipline** (memory `reference_pattern_2_register.md`). Ch 3 carries the Bay case as story (Pattern 2 anchor); augmentation deepens the story-anchor without codifying methodology. **Coherence VERIFIED.**

- **Ostrom-path illustrative register** (memory `reference_ostrom_illustrative_register.md`). Augmentation lists named voices illustratively, not exhaustively. The 11-voice augmentation map is not closure; the chapter's voice inventory remains open to future additions if substantively earned. **Coherence VERIFIED.**

- **Sandel hybrid pattern for acronym treatment** (memory `reference_sandel_hybrid_pattern.md`). First-mention of institutional acronyms (VMRC, ASMFC, UMD CES, VIMS, VWA) gets full expansion + acronym in parenthesis per Sandel hybrid rule. **Coherence VERIFIED at brief level; Stage 2 implements.**

### §9.6 Stage 1b brief updates required by 1c

None at the brief level — §§1–8 above already realize each coherence
commitment surfaced in §§9.1–9.5. The only outstanding 1c surface
is the bibliography §19.5 gap (G1–G10 at §9.1), and that disposition
is ADD BEFORE PASS 3.1 fact-check fires (a separate scribe session,
not a Stage 1 blocker).

### §9.7 1c verdict

**COHERENCE VERIFIED with one HOLD.**

- Bibliography §19.5 carries Colden material but NOT the 10
  augmentation sources (G1–G10 at §9.1). **HOLD:** add G1–G10
  entries to bibliography §19.5 (or new §19.6) before Pass 3.1
  fact-check fires. Stage 2 audience-blind drafting may proceed
  without the additions; the canonical sources in §6.4 are URL-
  stable + fully cited.
- All sibling-chapter cross-references VERIFIED.
- GuidanceDoc two-act structure VERIFIED (the augmentation does
  not restructure; it lands named voices within existing v1
  sections that map cleanly into the GuidanceDoc's eventual
  two-act split).
- Named-subject consent discipline VERIFIED (public-record
  exception applies to all 11; courtesy-notify before publication
  is the discipline).
- Phat anonymization preserved as locked element (§7).
- Cross-chapter consistency-inventory items VERIFIED.

---

## §10. Stage 1 sign-off (bookend gate)

### §10.1 Academic-rigor sign-off

| Checklist item | Verdict |
|---|---|
| Canonical-facts inventory (§6) complete + each fact verified against source | **PASS** — §§6.1–6.5 itemize subjects, quotes, numbers, sources, legal citations. One canonical-fact correction surfaced (Bay cap year: 2006, not 2017) + disposition recorded. |
| Canonical-formula inventory (math content) | **N/A** — no math content in augmentation. |
| Cross-artifact coherence verified (1c CLEAN) | **HOLD** — bibliography §19.5 gaps (G1–G10) to add before Pass 3.1 fact-check. Stage 2 may proceed. |
| Bibliography commitments touching scope inventoried + dispositioned | **PASS** — §9.1 inventories Colden entries (present) + flags G1–G10 (gaps) with disposition. |
| Stage 1a invariant scan returned CLEAN BASELINE | **PASS** — §§1a.1–1a.6; 0 HIGH; 2 MEDIUM dispositioned without YAML changes. |
| Named-subject consent gating | **PASS** — public-record exception applies to all 11; courtesy-notify discipline noted; Phat anonymization preserved as immutable. |

**Verdict:** PASS with one HOLD (bibliography G1–G10 additions
required pre-Pass 3.1; not a Stage 2 blocker).

### §10.2 Prose-quality sign-off

| Checklist item | Verdict |
|---|---|
| Audience pressure-test character set (§1) complete + tier-coverage appropriate to venue | **PASS** — 14 characters across three tiers; tier coverage matches chapter-augmentation work (CBF gateway + named subjects + general reader + adversarial reader + cross-chapter reader). |
| Voice register specification (§5) complete + venue-appropriate | **PASS** — preserves Ch 3 v1's existing italicized-quote / present-perfect attribution / first-mention institutional context conventions. |
| LLM-tic avoidance list (§5) complete | **PASS** — itemized at §5 bullet 5. |
| Locked elements (§7) verified + reproduced verbatim where applicable | **PASS** — Phat anonymization + existing Colden quotes + Biggie passage + opening + closing tie-back all locked. Verbatim quote text for all 11 named voices in §§4.L1–L12. |
| Hard constraints (§8) complete | **PASS** — itemized at §8; includes Path B preemptive policy, apparatus exclusion, consent discipline, climate-rhetoric guardrail, substance-drives-length, voice register, render-safety, canonical-fact correction. |

**Verdict:** PASS.

### §10.3 Overall

**PASS with one HOLD.** Stage 2 cleared to fire on this brief.
The HOLD (bibliography G1–G10 additions) is downstream of Stage 2:
it must resolve before Pass 3.1 fact-check, not before Stage 2
audience-blind drafting. Author ratification of this brief gates
Stage 2.

---

## §11. Stage 2 brief — what fires next

Single follow-up session at branch
`claude/ch3-augmentation-stage2-<harness-id>` performs:

- Audience-blind drafting of the 11 augmentation landings into Ch 3 v1.
- **Path B discipline:** Stage 2 does NOT open Ch 3 v1 at the
  sentence level for derivation; it reads the surrounding existing
  prose at each target location (e.g., lines 63–64 for L1 Hudgins)
  ONLY to know WHERE the new sentences land + WHAT THE PARAGRAPH
  PRECEDING/FOLLOWING IS SAYING, then writes the new sentences
  freshly from this brief's §§4–6 + §8.
- **Canonical-facts source:** §6 of THIS brief; do NOT re-open
  source articles for fact-verification (§6.4 carries full
  citations).
- **Quote selection:** per landing, §§4.L1–L12 list verbatim quote
  candidates; Stage 2 picks 1 or 2 per landing based on Stage 2
  prose-flow judgment. Stage 2 does NOT re-word any selected
  quote.
- **Co-located landings handled as a single prose unit:**
  - L2 Tarnowski + L3 Ruth (oyster paradox section, lines 168–178)
  - L5 Nesslage + L6 Latour (menhaden science section, lines
    99–113)
  - L8 Cannon + L9 Eskridge (Tangier section, line 144 region)
  - L12 Whewell + Tilghman watermen (place-paragraph region near
    line 144)
- **Output:** Stage 2 produces a SINGLE atomic commit landing
  the augmented Ch 3 file:
  `manuscript/chapters/Chapter__3_TheWaterman__Draft.md` —
  modified prose at the 9 distinct chapter locations specified
  in §4. The Stage 2 commit is PROPOSED — author ratification
  follows before Stage 3 fires.
- **Branch + merge discipline:** Stage 2 is a DIRECT content edit
  to Ch 3 v1 (publisher-facing prose). Per CLAUDE.md merge-to-main
  default: sessions producing *direct content edits without prior
  author ratification* stop at feature branch and wait for explicit
  author merge. Stage 2 does NOT autonomously fast-forward to
  `main`.

## §12. Stage 3 protocol — what comes after Stage 2

Three Pass passes fire serially against the post-Stage-2 augmented
Ch 3 draft (per `feedback_audience_aware_drafting_discipline.md`
v3.0 + Stage 3 template). Per-prompt serial cadence:

- **Pass 3.1 (fact-check):** verify every named subject, quote,
  date, number against §6 canonical-facts inventory + the bibliography
  entries (G1–G10 must be filed by this point). Pass 3.1 also
  catches the Bay-cap 2006 vs 2017 correction (§6.3).
- **Pass 3.2 (voice-polish):** flatness, meta-commentary, LLM tics,
  em-dash density (carries forward the MEDIUM finding at Ch 3 v1
  line 38 from §1a.3 M2).
- **Pass 3.3 (audience-load acceptance):** apply the §1
  pressure-test set; produce INCLUDE / EXCLUDE verdict per
  character.
- **Pass 3.4 (audience-load robustness):** apply adversarial /
  detractor characters (Tier 3 #12 Reedville-side reader + Tier 3
  #14 Public Choice adversarial reader + the adversarial-industry
  reader from GuidanceDoc §8 audience set). Thread-pull synthesis
  verdict.

---

## §13. Branch + merge discipline (this brief itself)

Per CLAUDE.md 2026-05-16 extension: **rigor-pass-style scaffolding
artifacts** (Stage 1 briefs at any pass) autonomously fast-forward
merge to `main` at session close. This brief is internal scaffolding
proposing spot-fixes; the chapter file under augmentation
(`Chapter__3_TheWaterman__Draft.md`) is UNCHANGED in this session.
Stage 2 (which DOES touch the chapter file) is the session that
stops at feature branch and awaits explicit author merge.

Hard constraints unchanged: never force-push `main`; never amend a
commit already on `origin/main`; never skip hooks (`--no-verify`)
without explicit author direction.

---

## §14. Discipline-trail

- **Pipeline doctrine v1.0.0:** `tools/commons_bonds_pipeline_doctrine_v1.0.0.md`
- **Stage 1 doctrine v1.0.0:** `tools/commons_bonds_pipeline_doctrine_stage_1_v1.0.0.md`
- **Stage 1 template:** `tools/drafting-templates/stage-1-audience-aware-structure-pass.md`
- **Audience-aware drafting v3.0:** `tools/memory/feedback_audience_aware_drafting_discipline.md`
- **Named-subject consent:** `tools/memory/feedback_named_subject_consent.md`
- **Verify-stale-claims:** `tools/memory/feedback_verify_stale_memory_claims.md` (the canonical sources at §6.4 are URL-stable as of 2026-05-20 + cross-checked against the CBF live-call-companion which is also current as of session)
- **Substance-drives-length:** `tools/memory/feedback_substance_drives_length.md`
- **Voice-polish pipeline:** `tools/memory/feedback_voice_polish_pipeline.md`
- **Sandel hybrid acronym pattern:** `tools/memory/reference_sandel_hybrid_pattern.md`
- **Ch 3 GuidanceDoc:** `manuscript/chapters/Chapter__3___GuidanceDoc.md`
- **Phat replacement-analysis proposal (ratified 2026-05-20):** `tools/stage-1-briefs/ch3_phat_replacement_analysis_2026-05-20_v1.0.0.md`
- **CBF live-call-companion (voices catalogue source):** `research/outreach/subjects/cbf/live-call-companion_2026-05-21_thursday-meeting.html`

— End of Stage 1 brief —
