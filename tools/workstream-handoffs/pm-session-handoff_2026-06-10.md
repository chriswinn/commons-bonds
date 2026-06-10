# PM Session Dashboard + Book-Completion Plan — 2026-06-10 (v2)

**Session:** `claude/pm-book-completion-260610-07b75f`
**Supersedes:** `archive/pm-session-handoff_2026-06-04.md` (carries forward its open
items) **and v1 of this file (earlier 2026-06-10)** — see §0 correction record.
**Session-freshness:** v1 built from five parallel survey agents; v2 rebuilt
same-day after author challenge + deterministic verification (grep/git
counts) exposed three stale claims in v1. Per-chapter prose findings are
under adversarial re-verification (workflow `wf_9aa3bab2-187`, one
refute-by-default verifier per chapter, in flight); §4.1 carries only
deterministically verified data until it returns.

---

## 0. Top-of-mind action driver + v1 correction record

**v1 → v2 corrections (all author-caught or verification-caught, 2026-06-10):**

1. **TA closeout was reported HELD — it had already MERGED** to main
   (`fd12275`, 06-09). The 06-09 closeout-summary artifact predated the
   merge; the survey agent quoted it without checking the ref.
2. **Ch 5 whole-cloth redraft was reported "fires NOW" — it was promoted
   06-09** (`dbde2e6`, blind-draft verdict PROMOTE-NEW-AFTER-FOLDIN) with
   the $108T removal, Polanyi/Fraser/Sandel exposition, Butler fold-in,
   TA-provenance number corrections, and the first-person-abstention
   standing fix all landed the same day. The "153 em-dashes / $108T live"
   claims described the regressed pre-redraft file (verified: archived copy
   has exactly 153; current canonical has 0).
3. **The em-dash pattern was mislocated.** Verified counts, current
   canonical: Ch 1: **1**, Ch 2: **1**, Ch 3: **12**, Ch 4: **58**,
   Ch 5: **0**, Ch 6: **193**, Ch 7: **114**, Ch 8: **51**, Ch 9: **145**,
   Ch 10: **0**. The load lives in the chapters whose redrafts have NOT
   been promoted, exactly. v1's prose-read agents were primed to find
   em-dash overuse and confabulated it in clean chapters; all qualitative
   prose findings are being re-verified (workflow in flight).

**Gate status: CLEARED.** TA closeout merged 06-09; framework-core /
reverse-CSD revision merged 06-10 (branch `claude/ta-reverse-csd-260610-4fc8d1`:
§3.4 M2=realized-Bond reader + hedonic/VSL note; §3.6 logic/table recompute;
§15.1.3; calc engine `core/technical-appendix/calculations/` with 21/21
reproductions incl. reef + reparations-test + 11-case bidirectional
portfolio; Darity figure → $14T 2nd-ed/JEP-2022). **The cross-corpus numeric
sweep is UNBLOCKED and is now the first domino.**

**The prose engine is the redraft-compare campaign, not a new campaign.**
- Promoted: Ch 1 + Ch 2 (06-05, `342a89e`), Ch 5 (06-09, `dbde2e6`).
- Awaiting compare+promote (all 0 em-dashes): Ch 3 (v1/v2, 06-05),
  Ch 4 / 6 / 7 / 8 (v1, 06-06), Ch 9 (v1, 06-06 — 4,862w vs canonical
  11,307w, matches the planned A3 cut; **pre-dates the 06-09 scope
  correction — re-check against corrected framing before promote**).
- No redraft: Ch 10 (register model; already clean).
- **NEW — Fable prose bake-off, Ch 1–3, in flight this session** (workflow
  `wf_3dac3810-74d`): author wants to see whether Fable beats the
  pre-Fable redrafts. Two Fable variants per chapter (A scene-forward /
  B spare-lyric) + adversarial judge with factual-fidelity gate →
  `research/story-drafts/ch{1,2,3}-fable-redraft-{A,B}_2026-06-10.md` +
  `...-fable-compare_2026-06-10.md`. KEEP-CANONICAL is an allowed verdict.

**Sequencing:** numeric sweep (now) → compare+promote queue + Fable
bake-off verdicts (author-gated, per chapter) → smoothing/Pass 3.6 on the
promoted set → Stage 4/5 cascade → proposal assembly (~Jun 14–20) →
agent Wave 1 (~Jun 24–Jul 1).

---

## 1. Critical path (ordered)

1. 🔴 **Cross-corpus numeric sweep** (one coordinated session, fires now):
   coal $4.50 → ~$4.70–4.85 (Ch 6/7/8/9 + essays); IPG 33–122× and
   "fifty-to-five-hundred-fifty-five-times" → reconcile to TA's M3
   premium-multiple ~8.5–26× framing; Norway "approximately fifty dollars"
   → ~$48/BOE + "~16% captured" (Ch 6 line ~141 + essays carrying "~17%");
   Ch 8 ↔ TA $496/$510/$524 reconciliation + retract/re-issue stale
   "arithmetic verified" Stage-5 sign-offs; **NEW from 06-10 merge:**
   Darity reparations figure $14T (2nd-ed/JEP-2022) wherever a figure is
   cited (calc engine corrected; chapters cite lineage qualitatively —
   verify none carries a stale figure); Ch 6 Method-2 description vs new
   §3.4 M2=realized-Bond reader (coherence check, see §3 note).
2. 🔴 **Foreign Affairs cover-letter ratification → submit** (ship-ready
   since 05-27; GPFG AUM figure rides the sweep if submission slips).
3. 🔴 **Noema decision: submit ratified 05-24 version vs close V-D-prime
   cascade** (fund AUM figure: confirm at submission day).
4. 🟡 **Public Books cover letter** — window Jun 9–13 is NOW.
5. 🟡 **Compare+promote queue:** Ch 3 (incl. father/boardwalk
   FACT-CORRECTION status check), Ch 4, 6, 7, 8 (existing v1 drafts) +
   Ch 9 (v1 re-checked against 06-09 scope correction) + **Fable bake-off
   verdicts Ch 1–3**. Gates Wave-1 samples (Ch 1 + Ch 5) + smoothing pass.
6. 🟡 **Book-proposal assembly (~Jun 14–20)** — §00 + §05 already
   recascaded to TA-closeout figures 06-10 per STATE.md; remaining:
   assembly + offline render audit + strip status header. Gates agent
   Wave 1 (~Jun 24–Jul 1).
7. 🟡 **Aeon portal spot-check** 1–2×/day; Jul 1–5 fallback primary.
8. ⚪ **Berggruen** — submit by Aug 5 (hard deadline Aug 17).

---

## 2. Author decision queue (user actions)

| # | Decision | Context | Urgency |
|---|----------|---------|---------|
| 1 | ~~TA full-diff review + merge~~ **DONE 06-09/10** (closeout + framework-core both merged with author ratification) | — | ✅ |
| 2 | FA cover-letter ratification | Submission package otherwise complete | 🔴 now |
| 3 | Noema: submit-now vs close V-D-prime cascade | Ratified version ready since 05-24 | 🔴 now |
| 4 | Public Books cover-letter ratification | Window Jun 9–13 | 🟡 this week |
| 5 | Compare+promote verdicts: Ch 3 (v2 vs canonical vs Fable), Ch 4/6/7/8 (v1 vs canonical), Ch 9 (v1 + scope-correction recheck) | One chapter per session per ratification-cadence discipline | 🟡 rolling |
| 6 | Fable bake-off verdicts Ch 1–3 (KEEP-CANONICAL / PROMOTE-A / PROMOTE-B / WITH-FOLDIN) | Compare artifacts land this session | 🟡 when ready |
| 7 | Ch 4 decisions: D9 oyster-bridge; A0d macro-chapter depth; B-3 Valdez — **verify still-open against the 06-06 Ch 4 redraft draft before deciding** | May be absorbed by redraft | 🟡 with Ch 4 compare |
| 8 | Ratify smoothing/Pass 3.6 design (§4.2) — now scoped to post-promotion residue only | Cheaper than v1 framing | 🟡 after promotions |
| 9 | Atlantic Ideas closer fix (flag §A): drop final sentence vs first-person rewrite | First-person-abstention discipline | 🟡 before submit |

---

## 3. Per-chapter status + next action (v2 — verified)

| Ch | Title | Words | Em— | Campaign state | Next action |
|----|-------|-------|-----|----------------|-------------|
| 1 | The Quiet Math | 6,204 | 1 | **Redrafted + PROMOTED 06-05**; author redlines 06-09 (Tubman "shape", Underground Railroad) | Fable bake-off verdict; light 3.3 re-fire; Stage 4/5 at gate; Wave-1 sample |
| 2 | The Miner | 6,486 | 1 | **Redrafted + PROMOTED 06-05** | Fable bake-off verdict; consent-status check (`__Draft`); Stage 4/5 |
| 3 | The Waterman | 10,580 | 12 | **NOT redrafted** — canonical = 05-25/26 rigor lineage; v1/v2 drafts (06-05) unpromoted; father/boardwalk FACT-CORRECTION (06-08) application status UNVERIFIED | Compare+promote (v2 + Fable candidates); verify FACT-CORRECTION applied |
| 4 | The Existence Proof | 4,168 | 58 | v1 redraft (06-06) awaiting compare | Compare+promote; D9/A0d/B-3 decisions ride compare |
| 5 | The Accountability Gap | 13,369 | 0 | **Redrafted + PROMOTED 06-09** (Polanyi/Fraser/Sandel in; $108T out; Butler + abstention fixes in) | Light 3.3 re-fire + Stage 1c-light vs reverse-CSD merge (see note); Stage 4/5; Wave-1 sample |
| 6 | Three Ways of Counting | 13,425 | 193 | v1 redraft (06-06) awaiting compare | **Most exposed to 06-10 framework-core merge**: M2 description (~line 141 "approximately fifty dollars"; §3.4 reader change), bidirectional triangulation passage (line ~145), IPG framings (lines ~185–191) — sweep + coherence check BEFORE compare+promote |
| 7 | On Other Worlds | 9,264 | 114 | v1 redraft (06-06) awaiting compare | Compare+promote; coal-figure line rides sweep |
| 8 | What Things Actually Cost | 6,495 | 51 | v1 redraft (06-06) awaiting compare | Compare+promote (supersedes v1's "spot-fix vs redraft" framing — a draft already exists); $496/$510/$524 reconciliation rides sweep |
| 9 | Pricing Honestly | 11,307 | 145 | v1 redraft (06-06, 4,862w) awaiting compare; **pre-dates 06-09 scope correction** | Re-check v1 vs corrected cost-severance framing → compare+promote |
| 10 | Common Bonds | 5,384 | 0 | No redraft needed (register model) | ~510w SAFE trims + line-94 fix; Stage 4/5 |
| TA | Technical Appendix | — | — | **Closeout MERGED 06-09 + framework-core/reverse-CSD MERGED 06-10**; calc engine 21/21; glyphs verified tofu-free 06-10 | Stage-4 PDF render audit before external circulation; deferred apparatus items parked post-Wave-1 |

**Reverse-CSD ↔ chapter coupling (verified by grep 06-10):** Ch 5 cites the
Darity/reparations lineage qualitatively (lines ~184/190/192) with NO dollar
figure and no M2/Himmelstein references — the 06-09 redraft already carries
the first-person-abstention deferral; the reverse-CSD merge VALIDATES Ch 5's
backward-instrument exposition computationally (reparations-test +
bidirectional portfolio PASS) rather than contradicting it. **No re-redraft
warranted; Stage 1c-light + Pass 3.1 spot-check suffice.** Ch 6 is the
exposed chapter (methods identity, M2 reader, bidirectional passage, IPG
framings) and gets the full coherence check inside the numeric sweep.

---

## 4. Prose-quality findings + smoothing pass (user requests #1 + #3)

### 4.1 Findings — VERIFICATION IN FLIGHT (v1 findings quarantined)

v1's eight-pattern findings list is **quarantined**: its authors confabulated
at least the em-dash pattern (claimed worst in Ch 1/3/5 — actually 1/12/0)
and graded then-already-redrafted chapters against stale claims. Workflow
`wf_9aa3bab2-187` is re-verifying every claim refute-by-default with line
numbers; this section will be replaced with verified findings when it
returns.

**Deterministically verified now (grep, current canonical):**
- Em-dashes: Ch 6 193 · Ch 9 145 · Ch 7 114 · Ch 4 58 · Ch 8 51 · Ch 3 12 ·
  Ch 1 1 · Ch 2 1 · Ch 5 0 · Ch 10 0. The un-promoted chapters carry
  essentially all of it; every waiting redraft draft greps to 0.
- "I want to say": Ch 10 ×3, Ch 3 ×1, elsewhere 0.
- "It is not X. It is Y." (narrow regex): Ch 3 ×4, Ch 9 ×2, Ch 2/5/6/8 ×1 —
  variant forms exist beyond the regex; verifier judgment pending.
- "Not from preference. From arithmetic." fragment emphasis: confirmed,
  Ch 8 line 12.
- "mechanism": 0–15 per chapter (Ch 10 highest at 15); "structure": 1–15.

### 4.2 Smoothing pass (PROPOSED — decision #8; re-scoped in v2)

With the redraft-compare campaign as the primary prose engine, the
smoothing pass shrinks to **post-promotion residue**: per-chapter Pass-3.2R
run on whatever the promoted set still carries (verified findings only),
Amendment-C interactive ratification, one chapter per session. Style
charter artifact still recommended (em-dash budget; section-close
variation; sensory anchor per technical slab; term rotation; banned tics)
— now ALSO feeds the compare+promote judging rubric and future Stage 2
briefs. Priority order set by verified findings, not v1 grades.

### 4.3 Pipeline suggestions (standing, unchanged from v1 except #6)

1. **Pass 3.6 (book-scale prose-smoothing)** codified as explicit-gate
   class, firing at whole-book gates (pre-proposal, pre-publication).
2. **Style telemetry in the invariant scanner** (`regressed-patterns.yaml`,
   LOW severity): em-dash density / "It is not X. It is Y." / meta-
   commentary phrases / pet-word counts — drift visible per-commit.
3. **Ch 10 named as register exemplar** in Stage 2 briefs.
4. **Figure sweeps before prose passes, always** (change-cascade routing
   amendment).
5. **Stage-5 sign-off retract+re-issue protocol** when upstream figures
   move.
6. **NEW (v2 lesson): deterministic-verification gate for survey claims.**
   Any countable claim (em-dash counts, figure presence, line numbers,
   "entirely absent") in a sub-agent survey or rigor artifact must be
   verified by grep/wc before landing on a dashboard; sub-agent prompts
   must not name expected findings ("look for em-dash overuse") without
   demanding line-number evidence — priming produces confabulated
   confirmations. Empirical anchor: this dashboard's v1 (2026-06-10).

---

## 5. Pitch/essay/proposal revision queue (user request #2) — gate CLEARED

TA closeout + framework-core both merged; the sweep session owns these.

| Artifact | Indexed content | Action |
|----------|-----------------|--------|
| Book proposal `00_overview.md` + `05_chapter-summaries.md` | TA-closeout figures | ✅ Recascaded 06-10 (per STATE.md); remaining: assembly ~Jun 14–20 + render audit + strip status header |
| Noema essay | Norway fund AUM | Submission-day fact-confirm |
| Foreign Affairs essay | GPFG AUM + Norway framing | Refresh in sweep if submit slips |
| Norway op-ed | Fund AUM + per-citizen + ~$48/BOE + capture % | Sweep + refresh at news-peg activation; trim ~26w |
| McDowell op-ed | Coal figures + Ch 6 multipliers | Sweep + refresh at peg activation |
| Atlantic Ideas essay | Ch 9-derived; closer flag §A | Fix closer (decision #9) + figure check before submit |
| No TA dependency | Aeon, Public Books, $100 Barrel, Harper's, Atlantic main, NYRB | None |

Also in sweep scope: "~17%" → "~16% captured" corpus-wide; Darity $14T
figure check; TA Stage-4 PDF render audit (ς glyphs — on-screen verified
tofu-free 06-10; print/PDF pending).

---

## 6. Merged date-anchored action list

| Date | Action | Owner |
|------|--------|-------|
| Now (Jun 10) | Numeric sweep session fires (§1.1 scope) | Session |
| Now | FA cover-letter ratify → submit; Noema decision | Author |
| Jun 9–13 | Public Books cover letter → submit | Author + session |
| Now (in flight) | Fable bake-off Ch 1–3 (this session, `wf_3dac3810-74d`); prose-findings verification (`wf_9aa3bab2-187`) | This session |
| Rolling | Compare+promote: Ch 3 → 4 → 6 (post-sweep) → 7 → 8 → 9 (post-recheck), one per session | Author + sessions |
| ~Jun 14–20 | Proposal assembly + offline render audit | Session + author |
| Jun 24–Jul 1 | Agent Wave 1 — gated on proposal + Ch 1/Ch 5 samples | Author |
| Jul 1–5 | Aeon fallback submission window | Author |
| Early–mid Jul | Comp-titles Phase 2 web verification | Session |
| Before Wave 1 | Endnote/citation sweep Phase 2 (todo #11, HIGH); lawyer consult (todo #7) | Session + author |
| Aug 5 | Berggruen submission target (hard Aug 17) | Author |
| Oct–Feb | Wave 2 windows: NYRB (Oct 8–Nov 15), Harper's (Q4), Atlantic main (Oct–Dec), FA (Nov–Feb if held) | Author |

---

## 7. Status buckets

**✅ DONE-DONE since 06-04:** TA closeout MERGED (06-09); framework-core /
reverse-CSD MERGED (06-10, calc engine 21/21); Ch 1 + Ch 2 redrafts
promoted (06-05); Ch 5 redraft promoted with fold-ins (06-09); Norway
$48/BOE precision edit; redraft-campaign scope correction; back-matter
clean set merged (06-10); proposal §00/§05 recascade (06-10).

**🔄 IN FLIGHT:** Fable bake-off Ch 1–3 + prose-findings verification (this
session); compare+promote queue (Ch 3/4/6/7/8/9 drafts waiting); Aeon
portal watch; consent tracker (11/12 §I gaps resolved).

**⏸ GATED:** smoothing pass (on promotions + verified findings); blurb
network (on agent/contract sign); Stage 5 sign-offs (explicit gates);
deferred TA apparatus items (post-Wave-1 per STATE.md).

**⚠️ WATCH:** Noema state ambiguity; Ch 6 framework-coupling (M2 reader +
IPG framings) before its compare+promote; Ch 9 redraft-v1 vs 06-09 scope
correction; Ch 3 FACT-CORRECTION application status; stale Ch 8 Stage-5
sign-off; Sandy Darity HELD email (decommission candidate); `__Draft`
suffixes Ch 1/2/5 (consent markers — verify tracker before Stage 5).
