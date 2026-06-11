# Submission-readiness spot-fix spec — *The Existence Proof* (Foreign Affairs)

**Status:** PROPOSED
**Date:** 2026-06-10 (verification pass) / spec authored 2026-06-11
**Verdict being remediated:** UPDATE-FIGURES-THEN-SUBMIT (submission-readiness verification 2026-06-10)
**Targets:** `publishing/essays/foreign-affairs-existence-proof/essay.md` + `cover-letter.md` + `README.md` + `STATE.md` (repo root)
**Provenance inputs:**
- Submission-readiness verification findings 2026-06-10 (orchestrated; findings reproduced per-item below)
- `rigor/devils-advocate-adversarial_post-Phase-C_2026-06-02.md` (PROPOSED, never ratified/applied — F-DA-2 / F-DA-4 / F-DA-6 / F-DA-7 absorbed here)
- `rigor/pass-3-3-3-4-3-5-bundled_new-pipeline_2026-06-03.md` (independently ruled the supermajority claim false at the dispositive SWF-practitioner gate; fix exists only in `_archive/fresh-newpipe-draft_2026-06-03.md`, never backported)
- `manuscript/ledgers/_CANONICAL_FIGURE_LEDGER.md` (RATIFIED 2026-06-04; amended 2026-06-09) — cited per-figure below
- `tools/audits/corpus-primary-source-register_2026-06-08.md` §2 item 12 (Norway per-capita)

**Disciplines binding on the applying session:**
- **No invented factual claims** (`tools/memory/feedback_no_invented_factual_claims_in_publisher_facing_prose.md`): every fix below is structure-only or ledger/register-anchored. Where author substrate is required it is explicitly flagged AUTHOR-CALL; do not synthesize citations or facts to close those items.
- **Amendment C Interactive Ratification:** prose-modifying fixes are presented as Options + Recommendation + Reasoning; author ratifies before apply; ratification + application combine in one session.
- **Merge-on-ratification (2026-05-28):** author ratification of these prose fixes IS the merge authorization; push to `origin/main` via pre-push reconciliation immediately after Phase C apply.
- **Change-cascade routing:** after Phase C apply, run Stage 1c (light) + Pass 3.3 (light) re-fire. Pass 3.4 re-fire not warranted (fixes strengthen robustness).

---

## §0. Sequence gates (named; check before applying anything)

- **GATE-1 (LIVE-WEB VERIFY — blocks M-3):** the Norwegian-government-composition fix rests on events that postdate every rigor artifact in this package (Centre Party exit from the Støre government, early Feb 2025, EU energy-directives dispute; Labour-only minority government since; Sept 2025 Storting election). The applying session MUST verify current Norwegian government composition against live reporting (WebSearch: Norwegian government composition + Støre status as of application date) before applying M-3. The recommended replacement wording is deliberately robust to post-election detail, but verify it is still true.
- **GATE-2 (AUTHOR SUBSTRATE — blocks A-1):** the 70–80% intake-share anchor requires an author-supplied primary source (Norwegian Ministry of Finance state-take statistics / Norwegian Offshore Directorate (formerly NPD) / IMF working paper) with methodology + time-window. Do NOT invent the citation. All other fixes can apply without this gate; do not hold M-items on GATE-2.
- **GATE-3 (POST-APPLY CASCADE):** after Phase C apply of ratified items — Stage 1c light + Pass 3.3 light re-fire, then Stage 4 portal-preview re-check + Stage 5 light re-sign-off remain owed before submission (both already in the pre-pub queue; see §4).
- **GATE-4 (CH 4 REDRAFT COORDINATION — non-blocking for this verdict, blocks final pre-submit sign-off):** source chapter Ch 4 is being whole-cloth redone around the **α-reduction mechanism** (ledger 2026-06-09 amendment: Norway's CS-reduction is **irreversibility-reduction** — GPFG restoration optionality moves α from ~1 toward ~0.50–0.75 — **NOT rent-capture**; the old "16% / $48/BOE rent captured" framing is dropped). The essay's §III reads Norway's bond through the 70–80% rent-capture-compounded frame. The FA submission window is Q4 2026 / Q1 2027 (README checklist), so the Ch 4 promotion will likely land first. Before portal submission: re-check §III (essay.md:60) + §VI (essay.md:100) against the promoted Ch 4. If the promoted framing materially changes the bond/cost-severance reading of Norway, route per change-cascade (new fact → Stage 1b → re-fire 3.1 + 3.2 + 3.3); do NOT silently patch.

---

## §1. Mechanical fixes (fully specified; author ratifies, no substrate needed)

### M-1 — FALSE Storting-supermajority claim in essay (HIGH)

- **Location:** `essay.md:46` — "Structural change to the fund's underlying architecture requires a Storting supermajority that no recent coalition has come close to assembling: a relaxation of the budgetary rule, a redirection of the principal toward domestic investment, a repeal of the ethics council's mandate."
- **Why false:** the fund act and the *handlingsregelen* are ordinary statute. The essay contradicts itself: `essay.md:42` already says the rule "is statutory rather than constitutional; it could be repealed by a future Storting majority." Independently ruled false by the 2026-06-03 new-pipeline audit (dispositive SWF-practitioner gate: "the 'Storting supermajority' claim is false and this reader would catch it") and flagged HIGH as F-DA-4 (devils-advocate 2026-06-02, option (b) recommended). The corrected framing exists only in `_archive/fresh-newpipe-draft_2026-06-03.md` (cross-party-consensus framing, its ¶ "A rule of this kind is only as strong as…") and was never backported to essay.md.
- **Operation:** drop "supermajority"; reframe the constraint as a *political-coalition* threshold, consistent with line 42.
- **Options:**
  - **(a) RECOMMENDED:** replace "requires a Storting supermajority that no recent coalition has come close to assembling" with "would require a Storting coalition that no recent government has come close to assembling" (keep the colon list unchanged). Minimal diff; restores internal consistency with line 42; matches the verification finding's suggested reframe and F-DA-4 option (b).
  - **(b):** fuller cross-party-consensus recast on the model of the archived fresh draft ("less a single legal lock than an unusually settled cross-party consensus… no government has been willing to pay the political price of breaking it"). Stronger prose but larger diff into a Stage-5-signed paragraph; only if author wants the recompose.
- **Reasoning:** the claim is the single highest credibility risk in the package — false at the venue's dispositive specialist gate, and self-contradicting within four paragraphs.

### M-2 — Same false supermajority claim in cover letter (HIGH)

- **Location:** `cover-letter.md:5` — "…the ethics council established in 2004, and the Storting supermajority required for structural change to the fund's underlying rules…"
- **Why worse than M-1:** framed to the editor-in-chief as one of the three load-bearing institutional features.
- **Operation:** replace the third operational-architecture clause with the political-threshold / cross-party-consensus formulation. Must stay consistent with whatever M-1 option is ratified.
- **Options:**
  - **(a) RECOMMENDED:** "…the ethics council established in 2004, and a cross-party political consensus that has put structural change to the fund's underlying rules beyond the reach of any recent governing coalition…"
  - **(b):** "…the ethics council established in 2004, and the breadth of Storting coalition that structural change to the fund's underlying rules would require — one no recent government has come close to assembling…"
- **Reasoning:** the cover letter must not assert what the essay (post-M-1) no longer asserts.

### M-3 — Stale current-government fact: "Støre's current Labour-Centre coalition" (HIGH; GATE-1 applies)

- **Locations:**
  - `essay.md:50` — "It has been preserved through Jonas Gahr Støre's current Labour-Centre coalition, which has been in office since 2021."
  - `cover-letter.md:5` — "…and the current Støre Labour-Centre government."
- **Why stale:** the Centre Party left the Støre government in early February 2025 (EU energy-directives dispute); Støre has led a Labour-only minority government since, through the September 2025 election. FA fact-checkers will catch it. Not recorded in any rigor artifact in this package — hence GATE-1 live verification before apply.
- **Operation (after GATE-1 verification passes):**
  - `essay.md:50` → "It has been preserved through Jonas Gahr Støre's Labour-led government, in office since 2021." (One clause; the durability argument is unaffected — if anything the rule surviving a coalition rupture strengthens it.)
  - `cover-letter.md:5` → "…and Støre's current Labour-led government."
- **No-change note:** `essay.md:32` ("across coalitions of Labour, center-right, Conservative, and Labour-Centre composition") is a *historical* list and remains accurate (the Labour-Centre coalition existed 2021 – early 2025); leave unless author prefers harmonizing to "Labour-led."
- **If GATE-1 verification contradicts the above** (e.g., government changed again post-knowledge-cutoff): adapt the clause to verified current fact, preferring composition-neutral phrasing ("the Labour-led governments in office since 2021" / "every government since"), and record the source in the apply commit.

### M-4 — Cover-letter word-count self-contradiction (MEDIUM)

- **Location:** `cover-letter.md:3` — "a 5,941-word essay" vs `cover-letter.md:11` — "(~6,065 words; well inside the magazine's 4,000–7,000-word convention)".
- **Why:** ¶1 was updated 2026-06-01 to the post-Phase-C 5,941; ¶5 still carries the pre-Phase-C 6,065. Either alone is fine; both together look careless.
- **Operation:** re-run the body word count on the final post-spot-fix essay.md (the M/A fixes below shift it by a handful of words), then harmonize BOTH instances to the recount. Recommended ¶5 form: "(~5,9xx words; well inside the magazine's 4,000–7,000-word convention)" or "(just under 6,000 words; …)". Update the essay.md header/footer comment word-count lines (essay.md:10, essay.md:115) in the same commit.

### M-5 — §V Social Security "has not been revisited" overstatement (MEDIUM; = F-DA-6, MEDIUM-HIGH at the author-bona-fides intersection)

- **Location:** `essay.md:90` — "The structural choice it embedded, that the surplus would be invested in intra-governmental debt rather than in a sovereign-wealth-style external capital pool, has not been revisited."
- **Why:** Clinton-era USA Accounts proposals and the Bush 2005 partial-privatization debate seriously revisited external-pool capitalization; the structural choice *survived* rather than went unexamined. The essay itself concedes "several subsequent reform moments" two sentences later (internal tension). F-DA-6 proposed a one-clause fix, never applied.
- **Operation (structure-only, per F-DA-6 recommended response):** convert "has not been revisited" into "was seriously contested at several reform moments — and survived each one." Recommended form: replace "…has not been revisited." with "…has been seriously debated at several reform moments — the Clinton-era USA Accounts proposals, the partial-privatization debate of 2005 — and has survived each one." (Both debate clusters are public record and already named in the F-DA-6 artifact; if the applying session adds any specifics beyond these two named clusters, fact-verify first.) Then check the following two sentences (same line) for redundancy with the new clause; the "or at any of several subsequent reform moments" phrase may now read as harmonized rather than contradictory — prefer leaving it.
- **Reasoning:** converts the most credentials-vulnerable sentence in the essay from "outsider misses the debate" to "informed outsider notes the debate happened and the choice survived."

### M-6 — Stale per-capita figure (FIGURE FIX; ledger-mandated)

- **Location:** `essay.md:48` — "assets in excess of two trillion U.S. dollars, or roughly three hundred and sixty thousand dollars for each Norwegian citizen alive."
- **Canonical figure:** **per-capita ~$390,000** — `manuscript/ledgers/_CANONICAL_FIGURE_LEDGER.md` (final per-chapter-corrections paragraph: "Norway per-capita ~$390k"), sourced at `tools/audits/corpus-primary-source-register_2026-06-08.md` §2 item 12 ("Per-capita Norway '$360,000' is now ~$390,000 — time-sensitive; NBIM end-2025") and carried in `tools/audits/_TA-redraft-reconciliation_2026-06-09.md` ("Per-capita ~$390k (NBIM end-2025; time-sensitive)"). The archived fresh draft already uses "more than 390,000 dollars."
- **Operation:** replace "roughly three hundred and sixty thousand dollars" with "roughly three hundred and ninety thousand dollars". The "in excess of two trillion U.S. dollars" clause is consistent with the ledger ("well over two trillion") — leave. The sentence's own hedge ("the figure moves with global equity-market valuations") stays.
- **Time-sensitivity:** this figure is flagged time-sensitive in the register; the existing README checklist item "GPFG AUM figure refresh against current NBIM figure at submission-window" covers the final refresh — keep that item open (§4).

---

## §2. Author-call items (need author substrate or author decision; do not apply mechanically)

### A-1 — Anchor the 70–80% intake-share figure (MEDIUM; = F-DA-2, rated HIGH by the devils-advocate audit; GATE-2 applies)

- **Locations:** `essay.md:40` (primary statement — "The state captures, by recent estimates, somewhere between seventy and eighty percent of the net economic value of Norwegian petroleum production…"); repeated `essay.md:60`, `essay.md:100`; cover letter `cover-letter.md:5` ("70 to 80 percent of net petroleum value").
- **Issue:** the single most-cited number in §II is unanchored — no source, no methodology definition of "net economic value," no time-window. Different methodologies yield ~55%–85%. F-DA-2 (PROPOSED 2026-06-02) recommended a structure-only spot-fix with an author-supplied primary source; never ratified or applied.
- **Operation (once author supplies the source):** add a single-clause attribution at the FIRST instance only (essay.md:40) naming the source + methodology + time-window (e.g., the share of net cash flow / resource rent per <source>, <period>). Lines 60 and 100 inherit by back-reference; no edits there under this item. Cover letter: no citation needed in a cover letter; optionally soften to "roughly three-quarters" if the author prefers symmetric hedging.
- **Candidate primary sources (per F-DA-2; author selects/verifies — do not invent):** Norwegian Ministry of Finance state-take statistics; Norwegian Offshore Directorate (formerly NPD); IMF working-paper estimates.
- **If the source does not land by submission:** the essay remains submission-eligible (the existing "by recent estimates" hedge stands) but carries the credibility risk the devils-advocate audit names; author decides whether to submit unanchored. Record the decision in the apply commit either way.

### A-2 — White-paper register leak in §III ¶1 (LOW; = F-DA-7 locus)

- **Locations:**
  - `essay.md:56` — "…what the framework calls *residual commons value*, abbreviated RCV in technical writing."
  - `essay.md:58` — "In the framework's plain-prose summary, cost severance for any given extraction is…"
- **Issue:** a terminology defense + internal-pipeline vocabulary inside a definition-by-naming cluster; the cover letter's AI-disclosure paragraph primes exactly this reading (F-DA-7). Otherwise the self-narration scan is clean; "the framework does not say the United States should adopt" (essay.md:92) is a brief-§16-authorized verbatim preservation — DO NOT touch it.
- **Mechanical micro-fixes (recommended; can ratify with §1 batch):**
  - essay.md:56 — delete ", abbreviated RCV in technical writing" (verified: "RCV" appears nowhere else in the essay body, so the abbreviation is dead weight).
  - essay.md:58 — replace "In the framework's plain-prose summary, cost severance for any given extraction is" with "Stated plainly, cost severance for any given extraction is" (operation: remove pipeline vocabulary; preserve the definition that follows verbatim).
- **Author-call portion:** F-DA-7's fuller recommendation — a single-paragraph recompose of §III ¶1 to soften the definition-by-naming cadence (4 sentence-initial "The framework" constructions body-wide) — is a register choice; offer it to the author as optional, severity LOW, not submission-blocking. The framework's terms are load-bearing and cannot be renamed or omitted.

### A-3 — Epigram density + 70–80% triad repetition (LOW; not submission-blocking — HOLD-WITH-FLAG)

- **Inventory (for the author's read, no default change):** ~6 "is not X. It is Y." constructions in 5,9xx words (essay.md:30, 52, 72 [brief-authorized verbatim — do not touch], 94, 102, 108) + aphoristic closes at §I/§IV/§VI; 12 body em-dashes (~2.0/1000w) — ratified, defensible. The 70–80% triad (licenses + taxation + dividends) repeats near-verbatim 3× (essay.md:38, 40, 100), paralleling the 2026-06-03 audit's §III↔§VI dedup note.
- **Optional operation if author wants the dedup:** lighten the THIRD restatement (essay.md:100) to a back-reference ("the seventy-to-eighty-percent capture described above" or similar compression) rather than re-listing the three channels. Leave 38/40 (first statement + anchored figure) intact.

---

## §3. Bookkeeping fixes (internal scaffolding; mechanical; same session)

### B-1 — README.md refresh (stale and hiding the real state)

- **Location:** `publishing/essays/foreign-affairs-existence-proof/README.md` — header says "RATIFIED READY-TO-SUBMIT" / "~6,065w" / "Last updated 2026-05-27"; records none of: the devils-advocate audit (PROPOSED 2026-06-02; 2 HIGH spot-fixes that were unapplied until this spec), the 2026-06-03 new-pipeline audit + fresh draft, the 2026-06-01 Phase C amendment (5,941w), or the 2026-06-10 UPDATE-FIGURES-THEN-SUBMIT verdict.
- **Operation:** update State line (e.g., "SPOT-FIX IN FLIGHT per rigor/submission-readiness-spotfix_2026-06-10.md → returns to RATIFIED READY-TO-SUBMIT on Phase C apply + light re-fires"), word count (post-fix recount), Last-updated date; add rigor cross-reference entries for: `devils-advocate-adversarial_post-Phase-C_2026-06-02.md`, `pass-3-3-3-4-3-5-bundled_new-pipeline_2026-06-03.md` (+ its archived fresh draft), `audit-5-second-triangulation_integrated-essay-post-Phase-C_2026-06-02.md` if absent, and this spec. Keep the submission-checklist items; add the A-1 source-supply item and the GATE-4 Ch 4 re-check item to the checklist.

### B-2 — STATE.md line update (same commit as any status change, per repo orientation rule)

- **Location:** `STATE.md:21` — "| Existence Proof | Foreign Affairs | **RATIFIED READY-TO-SUBMIT**; cover letter DRAFTED 05-27 | 06-04 (PM) | **Ratify cover letter → submit (critical path)** |"
- **Operation:** update State to reflect the 2026-06-10 verdict + this spec (e.g., "UPDATE-FIGURES-THEN-SUBMIT 06-10; spot-fix spec PROPOSED"), Verified column to the apply date, Next action to "Ratify + apply spot-fix spec → light re-fires → submit". On Phase C completion, update again to the post-fix state in the same commit as the apply.

### B-3 — essay.md header/footer comment blocks

- **Location:** `essay.md:1-18` (header) + `essay.md:114-122` (footer).
- **Operation:** in the apply commit, append to the Stage 3 status line: devils-advocate audit (2026-06-02, absorbed into this spec), new-pipeline bundled audit (2026-06-03), this spec (2026-06-10) + its Phase C apply date; refresh the word-count lines (with M-4). Note the footer line 115 says "~6,078w" while the header says "5,941w (verified via awk recount)" — harmonize both to the post-fix recount.

---

## §4. Carried-forward pre-pub queue (unchanged; not this spec's scope, listed so the applying session doesn't drop them)

1. **NBIM AR precise-figure verification** at nbim.no (~9,000 companies / 70+ markets, essay.md:44; per essay header Option A hedge) — author manual lookup before portal submission.
2. **GPFG AUM + per-capita refresh** against current NBIM figure at submission window (README checklist; M-6 makes the working figure ~$390k per ledger, final refresh still owed).
3. **Stage 4 FA portal preview** on the integrated post-spot-fix content (em-dash + italics + curly-quote rendering).
4. **Stage 5 light re-sign-off** on the post-spot-fix package.
5. **F-DA-5 Tooze engagement question** (HOLD-WITH-FLAG per devils-advocate audit) — editor-iteration candidate if the essay places; no pre-submit change.
6. **F-DA-7 §III ¶1 recompose** beyond the A-2 micro-fixes (HOLD-WITH-FLAG).
7. **Cover-letter sub-editor identification** + courtesy-notify discipline items (README checklist).
8. **Submission window:** Q4 2026 / Q1 2027 (Nov–Feb) per cascade plan v2 §3 W2.3. SUBMISSION itself remains an explicit author action regardless of merge state.

---

## §5. Recommended apply order

1. GATE-1 live verification (Norwegian government composition).
2. Present §1 M-1…M-6 + §2 A-2 micro-fixes to author per Amendment C (Options + Recommendation + Reasoning, one batch); ratify; Phase C apply; recount words (M-4); B-1/B-2/B-3 in the same session.
3. Stage 1c light + Pass 3.3 light re-fire (GATE-3).
4. Merge-on-ratification push to `origin/main` (pre-push reconciliation pattern; never force-push main).
5. A-1 lands whenever the author supplies the source (independent ratification cycle; do not block 1–4 on it).
6. Before portal submission: GATE-4 Ch 4 α-reduction re-check + §4 items 1–4.
