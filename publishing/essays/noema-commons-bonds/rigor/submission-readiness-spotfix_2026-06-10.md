# Noema Essay — Submission-Readiness Spot-Fix Spec — 2026-06-10

**Status:** PROPOSED 2026-06-10 (verification sweep verdict SPOT-FIX-THEN-SUBMIT; deterministic greps run 2026-06-11)
**Verdict context:** submission-readiness verification returned SPOT-FIX-THEN-SUBMIT — 2 HIGH prose findings, 1 MEDIUM author-decision flag, 1 LOW no-action report, 2 material figure findings, 1 figure verified-consistent.
**Primary target artifacts:**
- `publishing/essays/noema-commons-bonds/essay.md` (locked cut; RATIFIED-AWAITING-SUBMIT 2026-05-24; deterministic body count 4,974w — `grep -v '^#' essay.md | wc -w`)
- `publishing/essays/noema-commons-bonds/cover-letter.md` (RATIFIED 2026-05-24)
- Mirror target if V-D-prime is promoted (see AC-4): `publishing/essays/noema-commons-bonds/_archive/parallel-drafts_2026-05-28/noema-essay_hybrid_best-of-both.md` (5,120w body)

**Figure canon (single source of truth):** `manuscript/ledgers/_CANONICAL_FIGURE_LEDGER.md` (RATIFIED 2026-06-04; amended 2026-06-09) + its provenance register `tools/audits/corpus-primary-source-register_2026-06-08.md`.

**Applying-session protocol (read before applying anything):**
1. Read `STATE.md` live at apply time — portfolio statuses in this spec are a 2026-06-11 snapshot and WILL go stale (BR/Public Books/Aeon all in motion).
2. Both target files are end-user-facing prose: every fix below is PROPOSED and requires author ratification; ratification = merge authorization per merge-on-ratification (CLAUDE.md).
3. Any essay.md prose edit fires the automatic-on-edit cascade (Pass 3.1 light + Pass 3.2 light + Stage 1c-light) per Amendment A. The figure fixes in §2 are small enough that the light re-fires should be quick; budget for them.
4. Update the `STATE.md` Commons Bonds/Noema line (line 22 as of 2026-06-11) in the same commit as any status-changing apply.
5. No invented facts: figure replacements below are ledger-cited; prose operations specify the operation, NOT drafted prose — the applying session drafts, the author ratifies.

---

## §1. Finding inventory (from verification sweep)

| ID | Finding | Severity | Class |
|---|---|---|---|
| SF-1 | GPFG AUM + per-capita stale ($1.9T/$340k → canon >$2T/~$390k) | HIGH (material figure) | Mechanical |
| SF-2 | Darity $14T figure coupled to wrong edition (2020 1st ed. vs canon 2nd ed./JEP 2022) | HIGH (material figure) | Mechanical |
| SF-3 | Word-count bookkeeping false across package (README, Stage 5, cover-letter header) | HIGH (feeds SF-4) | Mechanical |
| SF-4 | Cover letter ¶1 misstates essay length to gatekeeper ("~3,800-word"; actual 4,974w body) | HIGH | Gated on AC-1 |
| SF-5 | Cover letter ¶4 cascade-coordination claims factually false (BR rejected; Aeon window passed) | HIGH | Gated on AC-2 |
| AC-3 | Voice-register divergence vs redrafted Ch 1 (~60x em-dash density gap) | MEDIUM | Author call |
| AC-4 | Submission-candidate ambiguity (locked cut vs V-D-prime cascade not closed) | MEDIUM | Author call |
| NA-1 | Norway fiscal rule (2001@4% → 2017@3%) | — | Verified consistent; no action |
| NA-2 | Book-wide tic scan — essay substantially clean | LOW | No action; record only |

---

## §2. Mechanical fixes (canon-driven; author ratifies, no drafting judgment beyond style)

### SF-1 — Norway GPFG AUM + per-capita (HIGH, material)

Known flag F-FC-Noema-9 (`rigor/pass-3-1-fact-check.md` §F-FC-Noema-9: "verify at submission window") is now confirmed material.

**Canon:** `tools/audits/corpus-primary-source-register_2026-06-08.md` line 53 — "Norway GPFG NOK 21,268B (>$2T) end-2025; per-citizen ~$390k now. NBIM. HIGH." Echoed at `manuscript/ledgers/_CANONICAL_FIGURE_LEDGER.md` line 77 ("Norway per-capita ~$390k"). NB the register (line 146) flags GPFG stated three ways across the corpus ($1.9T/$2.0T/$2.2T) pending a single-vintage reconciliation — therefore phrase conservatively as "more than two trillion" (true under every vintage; conservative-anchoring per `tools/memory/feedback_quantitative_apparatus_peer_review_defense.md`), NOT a pinned $2.2T.

**Fix locations + operations:**

1. **essay.md line 85** — current: "The fund is now valued at approximately one point nine trillion United States dollars. That works out to roughly three hundred and forty thousand dollars for every Norwegian citizen"
   - Replace "approximately one point nine trillion" → "more than two trillion" (keep "United States dollars" and the spelled-out-number register).
   - Replace "roughly three hundred and forty thousand dollars" → "roughly three hundred and ninety thousand dollars".
2. **cover-letter.md line 18** — current parenthetical: "(~$1.9 trillion / ~$340,000 per Norwegian citizen; principal inviolate since 1990)"
   - Replace "~$1.9 trillion" → "more than $2 trillion"; "~$340,000" → "~$390,000".
   - Optional LOW (remediation-author-verified, not in sweep findings): "principal inviolate since 1990" compresses fund-established-1990 with first-deposit-1996 (register line 53: "Fund est. 1990; first deposit 1996"). Tightening operation: rephrase so the inviolate-principal claim does not date from 1990 (e.g., drop the year from that clause, or anchor to the essay's own phrasing "the principal has never been spent"). Author call; do not block on it.
3. **cover-letter.md lines 40 + 86** (submission-checklist item 4 + carry-forward item 2) — both say "~$1.9 trillion as of essay drafting 2026-05-10"; both also cite "line 97 of essay," which is a stale anchor (the GPFG sentence is essay.md line 85). Update the figure reference to the post-fix value and correct the line anchor. These are internal checklist text; update in place.
4. **Mirror (if AC-4 promotes V-D-prime):** `_archive/parallel-drafts_2026-05-28/noema-essay_hybrid_best-of-both.md` line 156 carries the identical sentence — apply the same two replacements.

### SF-2 — Darity $14T figure-to-edition coupling (HIGH, material)

**Canon:** TA-state pins the $14T field figure to the 2nd edition / JEP 2022 — `manuscript/technical-appendix/calculations/csd_rcv_calculations.py` line 435 (`DM_TOTAL_2022 = 14.0e12  # 2nd ed / JEP 2022 (current)`) + `manuscript/technical-appendix/calculations/run-output_2026-06-10.txt` line 100 ("per-person x eligible (2nd ed/JEP 2022): 14.0 $T").

**Problem:** essay.md line 91 attributes the fourteen-trillion figure to "*From Here to Equality* (2020)" — the first edition. The figure-to-edition coupling is off.

**Fix location + operation:**

1. **essay.md line 91** — choose ONE operation (applying session drafts the sentence; author ratifies):
   - **Option A (recommended — preserves the 2020 landmark framing):** keep the book citation as the 2020 first edition but decouple the figure sentence so "on the order of fourteen trillion dollars" is attributed to Darity and Mullen's updated reckoning (second edition / their 2022 *Journal of Economic Perspectives* statement), not to the 2020 text.
   - **Option B:** re-date the citation itself to the second edition (2022) throughout the sentence.
   - Either way: the $14T stays field-credited (Darity/Mullen), no first-person dollar assignment — coercion-pricing first-person-abstention discipline (`tools/memory/feedback_coercion_pricing_first_person_abstention.md`) must survive the edit unchanged.
2. **cover-letter.md line 18** cites "*From Here to Equality* (2020)" but states NO figure — verified fine; no change required (if Option B is chosen for the essay, author may harmonize the cover-letter edition date for consistency, but it is not factually wrong as-is since the book did appear in 2020).
3. **Mirror (if AC-4 promotes V-D-prime):** hybrid file line 162 carries the identical sentence — same operation.

### SF-3 — Word-count bookkeeping corrections (HIGH; feeds SF-4)

**Deterministic ground truth:** essay.md body = **4,974 words** (`grep -v '^#' essay.md | wc -w`, run 2026-06-11); 4,924 after subtracting the 50 spaced em-dash tokens. The "~3,800w" figure fossilized from the Stage 1 brief TARGET (`rigor/stage-1-brief.md` line 165: "Target: ~3,800w body") and was NEVER true of any draft generation (2026-05-09 fresh draft 4,411w; post-pass-1 4,583w). None of the downstream artifacts counted.

**Fix locations + operations (internal scaffolding — no ratification gate, but commit honestly):**

1. **README.md line 10** — "**Word count:** ~3,800–4,000w (151 lines)" → state the deterministic count (~4,950–4,975w body) with the count method and date.
2. **stage-5-signoff.md line 6** — "151 lines / ~3,800–4,000w" — this is a RATIFIED historical artifact; do NOT silently edit the ratified line. Append a dated corrigendum block at the end of the file stating the deterministic recount (4,974w body, method, date) and noting the §1 word-count claim was never verified by counting.
3. **cover-letter.md line 5** (header metadata) — "(151 lines / ~3,800–4,000w; ...)" → correct alongside SF-4's body fix.
4. **cover-letter.md line 37** (submission-checklist item 1) — currently claims "this essay at ~3,800w is within the band." This is false twice over: the count is wrong AND the essay is ~950w OVER Noema's documented unsolicited ceiling (Stage 1 brief line 41: "2,500–4,000 words is the stated band. Pieces published over 4,000 are by editorial assignment, not unsolicited submission."). Rewrite the checklist item to state the true count and the over-band status, pointing at AC-1 for the decision.

---

## §3. Author-call items (decisions required; separated from mechanical applies)

### AC-1 — Length decision (BLOCKING for SF-4; HIGH)

The essay is 4,974w body against a documented 2,500–4,000w unsolicited band (~950w over). Options for the author:

- **Option A — submit at honest length.** State the true count in cover letter ¶1 (see SF-4) and accept the over-band risk. Cheapest; preserves the ratified cut; risk is a desk-pass on length grounds per the brief's own research ("over 4,000 are by editorial assignment").
- **Option B — trim toward ≤4,000w.** A ~950w trim is BEYOND spot-fix scope: it is a substantive prose edit that re-fires the automatic cascade (3.1 + 3.2 + 1c-light) and, given pre-submission state, warrants light 3.3 re-fire at minimum. If chosen, spin up as its own workstream; this spec's §2 figure fixes should still land first (they survive any trim).
- **Option C — query first.** Pitch/query Noema at the honest length before full submission, converting the over-band problem into an editorial-assignment conversation.

**Minimum bar regardless of option: the cover letter must never ship with "~3,800-word."**

### SF-4 — Cover letter ¶1 length statement (HIGH; gated on AC-1)

**cover-letter.md line 18** — "a ~3,800-word essay" → state the honest figure per AC-1 outcome: if Option A/C, "a ~4,950-word essay" (or equivalent honest rounding — "an essay of just under 5,000 words"); if Option B, the post-trim deterministic count. Do not round below the true count.

### AC-2 — Cover letter ¶4 rewrite (BLOCKING for SF-5; HIGH)

**cover-letter.md line 24** is factually false in both clauses as of 2026-06-11:

- "queued for Boston Review's Submittable portal" — BR REJECTED the Accountability Gap essay 2026-06-03; it is cascading to Public Books, cover letter in flight, NOT yet submitted (STATE.md line 20).
- "queued for the June 1-7 portal window" (Aeon) — window passed; Aeon is portal-watch (maintenance page seen 06-03) with Jul 1–5 fallback (STATE.md line 23).

**Operation (applying session drafts against LIVE STATE.md at apply time; author ratifies):**

- **Option A (recommended — safest under soft-clip discipline):** delete ¶4 entirely. The soft-clip rule (`publishing/book-proposal/03_author-platform.md`: "real and current submissions only, never speculative") means neither a not-yet-submitted Public Books cascade nor a portal-watch Aeon pitch qualifies for mention.
- **Option B:** replace ¶4 with a single rights-coordination sentence naming ONLY submissions that are live at apply time (verify each against STATE.md in the same session), retaining the no-overlap rights-register point if any venue is named.
- Cascade the same correction into the checklist/carry-forward text that repeats the dead claims: **cover-letter.md lines 44–45** (checklist items 8–9) and **lines 92–93** (carry-forward items 8–9) — rewrite to reference live venues/dates or generalize to "verify all cascade-coordination claims against STATE.md at submission window."

### AC-3 — Voice-register divergence vs redrafted Ch 1 (MEDIUM; author flag, not a defect)

Measured: essay 50 em-dashes / 4,974w (10.05/1,000w) vs new Ch 1 v2 redraft 1 em-dash / 6,195w (0.16/1,000w) — ~60x density gap. Both submission candidates (locked cut AND V-D-prime, 53 em-dashes/5,120w) carry the old register.

- The essay register was author-adjudicated 2026-05-28 (three-way comparison at `rigor/three-way-comparison_locked-vs-alt-no-em-vs-alt-norm-punct_2026-05-28.md` chose the locked cut over an alt_no-emdashes variant; F-DE-Noema-6 LOW HOLD ratified the density in-band).
- New Ch 1 is itself "REDLINE PENDING" (`manuscript/chapters/Chapter__1_TheQuietMath_Draft.md` header) — harmonizing now chases a moving target.
- **Recommendation: HOLD.** Author either (a) reaffirms the essay's adjudicated register for this submission (no action), or (b) queues a register-harmonization pass AFTER the Ch 1 redline settles — which would be redraft-grade work, not a spot-fix. Do not let this flag block submission; it is an informed-author acknowledgment item.

### AC-4 — Submission-candidate selection (MEDIUM; sequencing)

STATE.md line 22 flags the package AMBIGUOUS: locked cut is RATIFIED-AWAITING-SUBMIT (05-24) but the V-D-prime full re-cascade (`rigor/recascade_VERSION-D-PRIME_AMENDMENT-D-AWARE_2026-06-01.md`) is PROPOSED 06-01/02 and not visibly closed. Author decides: submit the ratified locked cut, or close the V-D-prime cascade first.

- **This spec's §2 figure fixes apply to essay.md regardless** (canon-driven; they are correct under either outcome).
- If V-D-prime is promoted to canonical, mirror SF-1/SF-2 to the hybrid file (line anchors given in §2) BEFORE promotion, and note V-D-prime's body is 5,120w — AC-1's over-band problem is WORSE there (~1,120w over).

---

## §4. Verified-consistent / no-action records

- **NA-1 — Norway fiscal rule.** essay.md line 87 ("adopted in 2001... initially set at four percent, lowered to three percent in 2017") MATCHES canon (`_CANONICAL_FIGURE_LEDGER.md` line 77: "Norway fiscal rule 2001@4%→2017@3%"; register line 53 same). The Pass 3.1 spot-fix (4%→3%, applied 2026-05-21) held. No action. (V-D-prime hybrid line 158 also consistent.)
- **NA-2 — Book-wide tic scan.** Essay substantially clean: antithesis/epigram ~5 instances mostly earned in memoir register (lines 43, 81, 89, 115, 137); self-narration low (2 "What I want" moves, lines 53 + 137; "the framework I am proposing" once, line 105 — the Mazzucato-positioning sentence, deliberate); workshop vocabulary ZERO; unattributed "economists say" ZERO (line-57 free-market economist is a dramatized interlocutor, adjudicated at Pass 3.4); fragments ~7, deliberate; rule-of-three low; en-dashes 0; em-dash density in-band per ratified F-DE-Noema-6 LOW HOLD. Recorded for honesty; NO fixes required from this finding.
- **Coercion-pricing discipline** confirmed clean in the sweep ($14T field-credited; no first-person dollar assignment; "theirs to enter" grep clean) — SF-2's edit must preserve this (see SF-2 operation note).

---

## §5. Sequence gates

| Gate | Rule |
|---|---|
| **G1** | AC-1 (length decision) BEFORE SF-4 (¶1 count value) and BEFORE the cover-letter.md line 37 checklist rewrite can be finalized. If AC-1 = Option B (trim), the trim is its OWN workstream with full automatic-cascade re-fire; SF-1/SF-2 land first and survive the trim. |
| **G2** | AC-2 (¶4 content decision) BEFORE SF-5 applies; the applying session MUST re-read STATE.md in the same session it drafts the replacement (statuses move daily). |
| **G3** | AC-4 (candidate selection) does NOT gate SF-1/SF-2 on essay.md, but DOES gate whether the hybrid-file mirrors are needed before any V-D-prime promotion. |
| **G4** | Any essay.md edit (SF-1, SF-2, any trim) fires the automatic-on-edit cascade: Pass 3.1 light + Pass 3.2 light + Stage 1c-light (Amendment A). Run these before re-asserting READY-TO-SUBMIT. |
| **G5** | Author ratification of each prose fix = merge authorization (merge-on-ratification); push via pre-push reconciliation pattern. Internal-scaffolding fixes (§2 SF-3 items 1–2) merge at session close. |
| **G6** | No sequence gate against Ch 1: the source chapter is STABLE post-redraft for figure purposes; AC-3 register harmonization (if ever chosen) waits for the Ch 1 REDLINE to clear — but that is explicitly out of spot-fix scope. |

## §6. Post-apply checklist for the applying session

1. Re-run the deterministic count (`grep -v '^#' essay.md | wc -w`) after all applies; verify every artifact that states a count (cover-letter ¶1 + line 5 + line 37; README line 10) states the same post-apply number.
2. Re-grep the package for `1.9 trillion|one point nine|three hundred and forty|340,000` — expect zero hits in essay.md + cover-letter.md body (checklist annotations updated per SF-1 item 3).
3. Verify `From Here to Equality` figure attribution matches the chosen SF-2 option in essay.md AND (if applicable) the hybrid file.
4. Update STATE.md Commons Bonds/Noema line (line 22 as of 2026-06-11) with the new package state in the same commit.
5. Confirm no scaffolding vocabulary leaked into essay.md/cover-letter.md body via `tools/scripts/check-corpus-invariants.sh`.
6. Stage 5 corrigendum appended (SF-3 item 2) — do not amend the ratified sign-off line in place.

---

*PROPOSED 2026-06-10. Internal scaffolding (rigor/ artifact) — auto-merges at session close per CLAUDE.md. The fixes it specifies are end-user-facing prose changes requiring author ratification before apply + merge.*
