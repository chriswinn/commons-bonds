---
artifact: Public Books "The Accountability Gap" — submission-readiness spot-fix spec
status: PROPOSED (awaiting author ratification; apply per-item, author-call items flagged)
date: 2026-06-10 (verification date; spec authored 2026-06-11)
verdict_remediated: UPDATE-FIGURES-THEN-SUBMIT (submission-readiness verification, 2026-06-10)
keyed_to: ../essay.md (97 lines; line anchors verified 2026-06-11 — re-verify with grep before applying if the file has moved)
figure_canon: manuscript/ledgers/_CANONICAL_FIGURE_LEDGER.md (RATIFIED 2026-06-04 + amendments through 2026-06-09) — single source of truth; derivative essays MUST match it
libby_canon: tools/audits/ta-provenance-libby-baotou-integral_2026-06-10_RATIFIED-APPLIED.md (Item 1) + tools/audits/corpus-primary-source-register_2026-06-08.md (§1 lines 39-40, §2 item 11)
chapter_reference: manuscript/chapters/Chapter__5_TheAccountabilityGap_Draft.md (redrafted 2026-06-09; the essay's source chapter — its landed formulations are the prose-register model for each figure fix)
deep_pass: publishing/essays/_pipeline/deep-pass/essay-public-books-deeppass_2026-06-04.md (sharpening item 6 = the venue tell)
state_line: STATE.md line ~20 ("Accountability Gap | ~~Boston Review~~ → Public Books | REJECTED 2026-06-03 → cascading to Public Books")
discipline: NO INVENTED FACTS — every replacement figure below traces to the ledger/audit/register entries cited per item; prose fixes specify the OPERATION, not invented prose. Per tools/memory/feedback_no_invented_factual_claims_in_publisher_facing_prose.md.
---

# Submission-readiness spot-fix spec — Public Books "The Accountability Gap"

**Context for a cold session.** This essay was submitted to Boston Review 2026-06-03 and
declined same day (boilerplate triage decline; transcript at
`_archive/boston-review-submission_2026-06-03/decline-letter.md`). Per STATE.md it is now
cascading to **Public Books**. A 2026-06-10 submission-readiness verification returned
**UPDATE-FIGURES-THEN-SUBMIT**: the essay's quantitative spine (Libby $4B / 40:1) was
**retired from the corpus canon on 2026-06-10**, several other figures drifted from the
ratified ledger, one venue tell and stale frontmatter remain, and a small set of register
edits are optional. This spec is the complete fix list. The essay is end-user-facing prose:
merge-on-ratification applies after Phase C; **submission itself remains author-controlled**.

**Important framing for the author:** the honest Libby figures are STRONGER than the retired
40:1 — the mortality-inclusive total is ≈$6.5–10.2B against ~$100M revenue (65–102×). This
is an upgrade, not a retreat.

---

## SEQUENCE GATES (apply in this order)

- **GATE 1 — Unfreeze first (item M1).** The current frontmatter declares the file
  `SUBMITTED ... frozen; further edits are for reprint/book only`. That instruction is now
  false (BR declined; PB cascade is live) and would direct any future session NOT to make
  the fixes below. M1 must land before any other edit.
- **GATE 2 — Figure fixes (F1–F7) before register/length edits (P2, P4).** The Libby spine
  rebuild (F1) changes four paragraphs; voice/length work before it is wasted motion.
- **GATE 3 — Source-manifest re-key travels with each figure fix.** `../source-manifest.md`
  is the fact-checker support sheet and currently certifies the retired figures (e.g. line 20
  "40:1 floor ✅"). Update the corresponding manifest row in the SAME commit as each fix
  (rows affected: Libby §I lines 19–24; finance line 40; SS line 53; Baotou line 55; black
  lung line 42). Also retitle the manifest's BR-keyed frontmatter when M1 lands.
- **GATE 4 — Venue norms before the length decision (P3 before P4-length).** No
  `publishing/venues/public-books/submission-norms.md` exists; the PB length band was never
  researched. Research it BEFORE deciding whether to take the ready-made ~300–400w cut.
- **GATE 5 — Post-apply cascade.** After Phase C: automatic-on-edit re-fire (Pass 3.1
  fact-check + Pass 3.2 voice + Stage 1c-light) per pipeline-doctrine Amendment A. Because
  the quantitative spine moved AND the venue changed, a fresh **Stage 5 sign-off for the PB
  package** is required before submission (the prior Stage 5 is keyed to the BR package and
  archived). The rigor/ dir already carries fresh 3.1/3.2/3.5 artifacts dated 2026-06-10 —
  reconcile with those sessions' findings rather than duplicating.
- **GATE 6 — STATE.md.** Any status change lands in STATE.md (line ~20) in the same commit,
  per CLAUDE.md orientation.

---

## M — Metadata fixes (mechanical; M1 is GATE 1)

### M1. Frontmatter is stale-by-venue and actively dangerous (verification finding, MEDIUM)

**Location:** `essay.md` lines 1–11 (YAML frontmatter).

**Defects:** (a) L2 `artifact: Boston Review essay ... canonical`; (b) L4 `status: SUBMITTED
2026-06-03 to Boston Review ... Submitted version frozen; further edits are for reprint/book
only` — false since the same-day decline, and it instructs future sessions not to edit;
(c) L8 `companions:` points to `../../venues/boston-review/submission-norms.md` (dead venue)
and `cover-letter.md` (does not exist in this dir — the BR one is archived; the PB cover
letter is "in flight" per STATE.md); (d) L9 `length_note` is calibrated to BR's bands.

**Operation (no new facts needed — all source material exists in-repo):**
1. Retitle artifact line to the Public Books target.
2. Replace status with the true lifecycle per `tools/conventions/status-markers.md`
   vocabulary, recording: BR SUBMITTED 2026-06-03 → REJECTED 2026-06-03 (same-day triage
   decline; package archived at `_archive/boston-review-submission_2026-06-03/`); now
   IN-REVISION for Public Books submission, pending this spec's fixes.
3. Delete the "frozen" sentence entirely.
4. Companions: drop the boston-review norms pointer and the dead `cover-letter.md`
   reference; point to `publishing/venues/public-books/submission-norms.md` once P3 creates
   it, and to the PB cover letter once it lands.
5. Rewrite `length_note` after P3 resolves the PB band.
6. Update STATE.md line ~20 in the same commit (GATE 6).

---

## F — Figure fixes (canon-anchored; replacement figures cite the ledger/audit per item)

### F1. Libby $4B / 40:1 spine — RETIRED; rebuild on the honest decomposition (verification finding, HIGH-equivalent; the essay's spine figure)

**Canon:** `tools/audits/ta-provenance-libby-baotou-integral_2026-06-10_RATIFIED-APPLIED.md`
Item 1 (RATIFIED + APPLIED to the TA 2026-06-10): "The 40:1 line dies." The $4B total is
class-4 (its own components sum to ≈$1.35B committed + ≈$1.25B accrued monitoring ≈ **$2.6B
documented-cash floor ≈ 26:1**). The defensible replacements, all derived in that audit:
- **Documented-cash floor:** ≈$2.6B ≈ **26:1** against ~$100M lifetime revenue. The revenue
  figure is itself an industry estimate no primary source has confirmed; sensitivity per the
  audit: if true revenue were twice as high, the floor ratio is still ≈13:1.
- **Mortality-inclusive total:** ≈**$6.5–10.2B** (= 694 documented asbestos-related-disease
  deaths through 2011, Naik et al. 2017, × EPA VSL $7.4–11.0M — labeled estimate; mortality
  ongoing, so a floor) → **65–102×** revenue.
- **Ch 5 register alternative** (the redrafted source chapter, `Chapter__5_TheAccountabilityGap_Draft.md`
  line 24): documented public spending ≈$0.9–1B → "a ratio of roughly nine or ten to one";
  with conservative valuation of deaths/disease the total "plausibly reaches into the low
  billions"; stated as "an order-of-magnitude estimate built from disclosed components rather
  than a single authoritative number ... costs at least an order of magnitude greater."

**Four sites in essay.md — all must move together and stay mutually consistent:**

1. **L21 (the ledger paragraph), final three sentences:** "...they exceed four billion
   dollars. Against one hundred million dollars in lifetime revenue, that is a ratio of
   forty to one. For every dollar the mine earned, the surrounding world absorbed at least
   forty in damage." → Rebuild on the chosen canon formulation (see AUTHOR-CALL A1). Do not
   keep any "$4B" or "40:1"/"forty" ratio language.
2. **L25:** "It did not mean the forty-to-one ratio was a fiction." → Replace the ratio
   reference with whatever quantity L21 now carries (operation: same referent, new figure;
   e.g. the ledger/the documented costs — wording at applier's discretion, figure from canon).
3. **L77 (Restitution Bond worked application):** "totaling the four billion dollars in
   documented costs, recognizing that this exceeds the mine's lifetime revenue forty times
   over" → retotal on the chosen canon (floor ≈$2.6B/26:1, or mortality-inclusive
   ≈$6.5–10.2B/65–102×, or Ch 5's order-of-magnitude register — must match L21's choice).
4. **L97 (closing paragraph):** "The four billion dollars in cost sits on a ledger that has
   been kept all along, against one hundred million dollars in revenue" → same rebuild. The
   closing argument ("no instrument existed to pay it") survives any of the canon
   formulations unchanged.

**Constraint:** figures only from the audit/Ch 5 formulations above; the prose around them
is the applier's normal voice work (Pass 3.2 re-fires per GATE 5).

### F2. Libby vermiculite share + homes (L17) — off-register

**Canon:** `tools/audits/corpus-primary-source-register_2026-06-08.md` line 39 + §2 item 11
(line 78); pointed to by the ledger's chapter-level-corrections note (ledger line 77,
"Libby >70%-of-US"). EPA Libby Superfund Site Profile says **">70% of US vermiculite"** —
the "~80% of world" claim does not trace. "35M homes" → register: cite as a range (~1M–35M);
Ch 5 (line 18) uses "tens of millions of American homes."

**Operation:** L17 "supplied roughly eighty percent of the world's vermiculite" → rescope to
the US-share claim (>70% of US, EPA). "an estimated thirty-five million American homes" →
soften to the register-approved range or Ch 5's "tens of millions" formulation.

### F3. Libby human toll (L21) — align to register

**Canon:** register line 40: deaths ">400 (early EPA) → ~694 by 2011 (Naik et al. 2017)";
diagnosed "~2,400+" (the essay's "roughly three thousand" does not match the register);
40–80× asbestosis mortality is SOURCED (ATSDR 2002) and may stand.

**Operation:** "More than four hundred Libby residents have died" → MAY stand as a floor
(true), but the stronger sourced figure (~694 documented deaths through 2011, Naik et al.
2017) is available and F1's mortality-inclusive option depends on it — if L21 adopts the
mortality-inclusive total, use 694 here for internal consistency (AUTHOR-CALL A1 decides).
"Roughly three thousand have been diagnosed" → align to the register's ~2,400+ (mechanical).

### F4. Foreclosure completions (L35; echoes L37, L61, L77) — 5M → ~4.1M completed

**Canon:** ledger line 77 chapter-level corrections: "foreclosures ~4.1M completed"; Ch 5
line 78 landed formulation: "roughly four million ended in completed foreclosures, about
4.1 million through 2012 by CoreLogic's count."

**Operation:** L35 "about five million lost their homes" → ~4.1M completed through 2012
(CoreLogic). The "ten million households received foreclosure filings" figure (L35, repeated
L37 and L61, "foreclosed households" L77): the ledger does not correct the filings number,
but the redrafted Ch 5 writes around it ("millions of foreclosure filings"); see
AUTHOR-CALL A2. Whatever is chosen, all four sites move together (the source-manifest line
40 row updates with them, GATE 3).

### F5. Social Security foregone return (L41) — "tens of trillions" off-canon

**Canon:** ledger line 69 ("$108T Social Security — DONE (Ch5 landed)"): honest foregone
return = investable base ~$2.7T surplus peak, compounded net of payouts → **"a few trillion,
not a hundred"**; the **~$22.6T 75-yr actuarial shortfall is a DIFFERENT quantity, kept
distinct**. Ch 5 lines 100–104 carry the full landed treatment.

**Defect:** L41 "The foregone return embedded in this arrangement ... runs into the tens of
trillions of dollars, an order of magnitude above the program's current trust-fund balance"
matches neither canonical quantity (the honest foregone return is single-digit trillions;
the $22.6T figure is the shortfall, not the foregone return).

**Operation:** restate the sentence on the canon: foregone return "into the trillions" (per
ledger line 69); if a larger magnitude is wanted in the same beat, name the ~$22.6T
seventy-five-year actuarial shortfall AS the distinct Trustees figure (never blended with
the foregone-return counterfactual). Drop the "order of magnitude above the trust-fund
balance" comparison unless recomputed from the canon quantities. Mechanical in substance;
wording discretion to the applier.

### F6. Baotou share (L43) — "this one place ≠ 60% of the world"

**Canon:** Ch 5 line 54 (landed 2026-06-09): China supplies ~60% of global production; the
Bayan Obo/Baotou complex accounts for roughly half of CHINA's output — "the correct way to
say it is not that this one place produces sixty percent of the world's rare earths."

**Defect:** L43 "the refining of roughly sixty percent of the world's rare-earth elements"
attributes the world share to Baotou itself — exactly the formulation the redraft corrects.

**Operation:** rescope to the two-step share (China ~60% of world; Baotou ≈ half of China's).
The "about ten tons of toxic and radioactive wastewater per ton of oxide" figure is retained
in Ch 5 (line 56, as the low end of published estimates) — keep. "farmland within a
ten-kilometer radius unusable": Ch 5 drops the point radius ("farmland within a radius of
the facilities has gone out of use") — soften to match (LOW).

### F7. Black-lung $44B (L55) — relabel with the honest date

**Canon:** ledger line 71: relabel as "≈$44 billion **through 2009** (GAO/CRS)" — a
conservative, honestly-dated floor (no authoritative post-2009 cumulative total exists).
Keep the trust-fund DEBT clause ($5.1B as of Sept 2024, DOL/GAO) distinct — the essay
already keeps it distinct; only the dating of the $44B changes.

**Operation:** L55 "has paid out about forty-four billion dollars over half a century" →
"through 2009" dating per the ledger label (Ch 5 line 194 model: "roughly forty-four billion
dollars through 2009, the most recent authoritative cumulative tally ... a conservative
floor for the program's full run").

### F8. Reclamation-bond gap (L55) — verify the single figure (LOW)

**Canon pointer:** ledger line 77 lists "reclamation-gap single figure" among chapter-level
corrections; Ch 5 line 194 now says "several billion dollars less"; the source manifest
(line 44) has "$4–6B" web-verified against 30 U.S.C. §1259.

**Operation:** verify which figure the per-chapter brief (`tools/audits/chapter-citation-specs/`)
ratified and harmonize L55 "routinely fall four to six billion dollars short" to it. If the
specs are silent, keep $4–6B (web-verified) and note it in the manifest.

### F9. Deepwater >$150B / "paid forty percent of its cost" (L31, echo L77) — verify register (LOW; author-call on motion)

**Canon pointer:** ledger line 77: 'Deepwater ">$150B" not NOAA' — an attribution fix the
essay already satisfies (L31 attributes to "academic, insurance-industry, and federal
sources," not NOAA). HOWEVER the redrafted Ch 5 (line 42) goes further and declines any
single total-loss aggregate ("no credible source that produces a single figure of total
economic loss to the Gulf"), building a defended component range instead.

**Operation:** see AUTHOR-CALL A3. No mechanical change is strictly required by the ledger;
the essay is attribution-compliant. If the author adopts Ch 5's stricter register, both L31
("above one hundred fifty billion ... the disaster paid forty percent of its cost") and the
L77 echo ("closing the gap between the sixty billion BP paid and the hundred fifty billion
the disaster cost") move together, using only Ch 5 line 42's documented components (NRDA
≈$17B; tourism several-B to >$20B multi-year; property ≈$4–5B; BP paid ≈$60–65B).

---

## P — Prose fixes

### P1. Dead-venue tell (L87) — MECHANICAL, HIGH

**Finding:** L87 "The philosophical grounding for why a society should do this comes from
two traditions **BR readers will recognize**." Flagged 2026-06-04 by the deep-pass
(`essay-public-books-deeppass_2026-06-04.md` line 128, sharpening item 6: "must change for
Public Books"); never fixed.

**Operation:** genericize — delete or recast the relative clause so no venue is named. Do
NOT substitute "Public Books readers" (same tell, new venue). The minimal motion is removing
"BR readers will recognize" and letting the two traditions stand on their own introduction
(Parfit; Pettit/Skinner — both named in the following sentences, so the clause is
load-free). Wording discretion to the applier; no facts involved.

### P2. FCIC quotation (L35) — MECHANICAL, MEDIUM

**Finding:** quotation marks wrap a paraphrase. Verbatim FCIC (2011): "the result of human
action and inaction, **not of Mother Nature or computer models gone haywire**." The essay's
quoted "not forces beyond human control" is gloss. The source manifest (line 40) already
flags "FCIC quote lightly paraphrased — verify wording." Checkable miss at a fact-checked
venue.

**Operation — choose one (both mechanical):**
- (a) RECOMMENDED (minimal motion, keeps the source's voice): trim the quote marks to the
  verbatim fragment — quote only "human action and inaction" and carry the rest as unquoted
  paraphrase; or
- (b) drop the quote marks entirely (Ch 5 line 78 model: "concluded that the crisis had
  resulted from human action and inaction, from choices, not from forces beyond anyone's
  control" — no quotation marks).
Update the manifest row's "verify wording" flag to resolved in the same commit.

### P3. Public Books venue-norms research + length (LOW; gates the length decision)

**Finding:** 4,446w was already above BR's published sweet spot per Stage 5; Public Books
typically runs shorter (≈2,000–3,500w per the verification's estimate — UNVERIFIED), and no
`publishing/venues/public-books/submission-norms.md` exists (`publishing/venues/` holds only
boston-review + phenomenal-world).

**Operation:** (1) research PB submission norms (length band, full-draft vs pitch, house
style, submission channel) and create `publishing/venues/public-books/submission-norms.md`
on the model of the boston-review file; (2) only then decide length (AUTHOR-CALL A4). The
ready-made cut, if needed, is Stage 5's identified optional ~300–400w tightening (the Social
Security beat + the GoFundMe/Baotou pair) — see
`_archive/boston-review-submission_2026-06-03/rigor/stage-5-signoff-new-pipeline_2026-06-02.md`
§3 carry-forwards.

### P4. Register: antithesis/epigram density (MEDIUM-optional) — see AUTHOR-CALL A5

**Finding (verification, honest count):** 10 strict "not X. It is Y."-family constructions
plus ~5 looser inversions; an aphorism closes 6 of 7 sections. Counter-evidence keeping this
optional: these passed Pass 3.2/3.5 ratification, and the 06-04 deep-pass harvested five of
them as book-grade articulations (deep-pass §e — e.g. L25 "not a moment. It was an
architecture", L49 "They are not flaws in the system. They are the system", L89
"Tractability is not the absence of severance...", L93 "not a fact of nature. It is
engineered."). **Do not touch the harvested lines.**

**The one true redundancy:** the near-identical semicolon pair —
- L55: "The design points one way; the financing drifts the other."
- L83: "The principle is sound; the execution is partial."

**Operation (if ratified):** rephrase ONE of the two as plain prose, preserving meaning
(operation, not prescribed prose); optionally flatten 2–3 of the WEAKER "It is" pivots (not
the five harvested lines). Apply AFTER the figure fixes (GATE 2) so the 3.2 re-fire sees
final text.

### P5. No-action findings — recorded so future sessions do not re-litigate

- **Self-narration (LOW):** 5 instances (L29 "Call it cost severance"; L65; L71 "A word on
  the term."; L75; L81; L97 "Return, at the end, to Libby.") — all functional; zero
  "this essay argues" / "the framework" chains / workshop vocabulary. **Leave as-is.**
- **Em-dash + tic hygiene: CLEAN.** 0 body em-dashes (the 3 grep hits are YAML frontmatter
  lines 2/4/9), 0 en-dashes, no fragment-emphasis tics; triads sparse and purposeful (the
  Coates "name the mechanism, name the harm, name the debt" echo is deliberate). **No action.**
  (NB: frontmatter em-dashes disappear anyway when M1 rewrites those lines.)

---

## AUTHOR-CALL ITEMS (separated; everything above not listed here is mechanical)

- **A1 — Libby spine register (F1/F3).** Which canon formulation does the essay adopt at all
  four sites? Options: (i) TA-style decomposed floor + mortality-inclusive total
  (≈$2.6B/26:1 floor; ≈$6.5–10.2B/65–102× with the 694-deaths × VSL line — strongest, most
  motion); (ii) Ch 5's order-of-magnitude prose register ("nine or ten to one" on documented
  public spending; "low billions"; "at least an order of magnitude greater" — most
  consistent with the source chapter, least number-laden for a general-readership venue);
  (iii) floor-only minimal motion (≈$2.6B/≈26:1 everywhere). Recommendation: (ii) for a
  Public Books register, with (i)'s mortality-inclusive sentence available if the author
  wants the "honest figures are stronger" beat explicit.
- **A2 — The 10M-filings figure (F4).** Keep (source-manifest-verified, ledger-uncorrected)
  or write around per Ch 5's "millions of foreclosure filings"? Keeping is defensible;
  conforming to Ch 5 is more conservative. Echoes at L35/L37/L61 move together either way.
- **A3 — Deepwater aggregate (F9).** Keep the attribution-compliant >$150B/40% spine, or
  adopt Ch 5's defended-component-range register (more motion, two sites)? No ledger
  violation either way.
- **A4 — Length (P3).** If PB norms require: take the Stage 5 ~300–400w cut. Author cuts
  prose; this spec only names the pre-identified candidates.
- **A5 — Epigram thinning (P4).** Thin one of the L55/L83 semicolon pair (+ optionally 2–3
  weak "It is" pivots)? Optional; the verification itself rated this MEDIUM-optional.

---

## CLOSE-OUT CHECKLIST (for the applying session)

1. M1 frontmatter unfreeze + STATE.md (GATE 1, GATE 6).
2. F1–F7 figure fixes (+ F8/F9 verifications), each with its source-manifest row (GATE 3).
3. P1 venue tell + P2 FCIC quotes.
4. P3 PB norms file → A4 length decision.
5. P4 register edit if A5 ratified.
6. Automatic-on-edit cascade (3.1 + 3.2 + 1c-light), then fresh PB Stage 5 sign-off
   (GATE 5). Reconcile with the 2026-06-10 rigor/ pass artifacts already in this dir.
7. PB cover letter (in flight per STATE.md) references the corrected figures — verify it
   carries no 40:1/$4B residue before submission.
8. Merge-on-ratification; submission click remains the author's.
