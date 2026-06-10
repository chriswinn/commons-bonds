# PM Session Dashboard + Book-Completion Plan — 2026-06-10

**Session:** `claude/pm-book-completion-260610-07b75f`
**Supersedes:** `archive/pm-session-handoff_2026-06-04.md` (carries forward its open
items; re-verified against 06-06 → 06-09 artifacts).
**Session-freshness:** built 2026-06-10 from five parallel survey agents
reading current `origin/main` + held branches. Statuses re-verified against
`ta-closeout-summary_2026-06-09.md`, `redraft-campaign-scope-correction_2026-06-09.md`,
`post-audit-structural-todos_2026-06-06.md`, per-essay READMEs, and a full
prose read of all 10 chapters.

---

## 0. Top-of-mind action driver

**The Technical Appendix is the gate for everything in the back half of
June.** A live author-side Fable session is reviewing the TA for errors /
improvements (in flight 2026-06-10). The TA closeout branch
(`claude/ta-closeout-260607-92165f`, M3 Path-A rework + reserved fixes +
bibliography housekeeping) is COMPLETE and HELD awaiting author full-diff
review. Until BOTH land on main:

- the cross-corpus numeric sweep (coal $4.50→$4.70–4.85; IPG 33–122×→8.5–26×;
  Norway ~$48/BOE + ~16% captured; Ch 8/TA $510-vs-$524) CANNOT fire without
  risking double-churn;
- the whole-book prose-smoothing campaign (§4 below) SHOULD NOT fire, because
  smoothing prose around numbers that are about to change wastes a pass;
- the book-proposal figure refresh + TA-indexed essay refreshes (§5) are
  premature.

**Sequencing rule for all sessions this week: TA error-review closes → TA
merges → numeric sweep → prose-smoothing campaign → proposal/essay refresh.**
Everything NOT numerically coupled to the TA (submission critical path,
Ch 5/Ch 9 redrafts, author decisions) proceeds in parallel now.

---

## 1. Critical path (ordered)

1. 🔴 **TA error-review session close + author full-diff review + merge**
   (gate for phases 2–4 below). Branch `claude/ta-closeout-260607-92165f`
   HELD; review cmd: `git diff origin/main -- core/technical-appendix/ research/literature/bibliography.md`.
2. 🔴 **Foreign Affairs cover-letter ratification → submit.** Highest-tier
   venue, ship-ready since 2026-05-27; only gate is author ratification.
   Not TA-gated for submission BUT carries GPFG AUM figure — if submission
   slips past TA merge, refresh fund figure first.
3. 🔴 **Noema decision: submit ratified 2026-05-24 version vs close V-D-prime
   cascade first.** State ambiguity is itself the blocker. Noema carries a
   Norway fund AUM figure → prefer deciding AFTER TA merge if it lands this
   week, else submit with a submission-day fact-confirm.
4. 🟡 **Public Books cover letter** (BR-decline cascade) — target window
   Jun 9–13 is NOW.
5. 🟡 **Ch 5 whole-cloth redraft** — gates first-wave agent send (with Ch 1 +
   proposal). $108T recompute RATIFIED 2026-06-04; Phase C application to the
   chapter is pending and rides the redraft. Brief ~pre-written.
6. 🟡 **Book-proposal assembly sprint (~Jun 4–20)** — sections 00–05 ratified;
   Norway $1.9T figure re-verification is an explicit pre-agent gate (TA now
   carries GPFG ~$2.0T → refresh on TA merge). Gates agent Wave 1
   (compressed ~Jun 24–Jul 1).
7. 🟡 **Aeon portal spot-check** 1–2×/day; Jul 1–5 fallback window primary.
8. ⚪ **Berggruen Prize** — AI-free isolated track; submit by Aug 5 (hard
   deadline Aug 17).

---

## 2. Author decision queue (user actions)

| # | Decision | Context | Urgency |
|---|----------|---------|---------|
| 1 | TA full-diff review + merge authorization | Closeout branch HELD; error-review session output folds in first | 🔴 now |
| 2 | FA cover-letter ratification | Submission package otherwise complete | 🔴 now |
| 3 | Noema: submit-now vs close V-D-prime cascade | Ratified version ready since 05-24 | 🔴 now |
| 4 | Public Books cover-letter ratification | Window Jun 9–13 | 🟡 this week |
| 5 | Ch 8: spot-fix exception vs whole-cloth redraft | Survey recommendation: spot-fix (prose already 5-pass polished; open items are scoped) | 🟡 this week |
| 6 | Ch 4 decisions: D9 oyster-bridge beat; A0d macro-chapter landing depth; B-3 Valdez direction (depends on Ch 5) | Mostly agent-executable once decided | 🟡 with Ch 5 redraft |
| 7 | Ratify prose-smoothing campaign design (§4) incl. pipeline amendment | New explicit-gate pass; fires post-TA-merge | 🟡 this week |
| 8 | Atlantic Ideas closer fix (coherence flag §A): drop final sentence vs first-person rewrite | First-person-abstention discipline | 🟡 before submit |

---

## 3. Per-chapter status + next action

Tiers per 2026-06-10 survey (rigor-pass artifacts + redraft-campaign scope).

| Ch | Title | Words | Tier | Done | Next action |
|----|-------|-------|------|------|-------------|
| 1 | The Quiet Math | 6,204 | A | 3.1, 3.2, 3.3(light), 3.5 | Author redline; Stage 4/5 at gate; prose pass P2 |
| 2 | The Miner | 6,486 | B | 3.1, 3.2, 3.3(×2), 3.4, 3.5 | Consent-status check (`__Draft`); Stage 4/5; prose pass P1 (expository flatness) |
| 3 | The Waterman | 10,580 | B | 3.1, 3.2, 3.3, 3.4, Stage 4 | 3.5 DE; Stage 5; prose pass P3 (lightest) |
| 4 | The Existence Proof | 4,168 | B | 3.1–3.5 | 3 author decisions (D9/A0d/B-3) → apply; Stage 4/5; prose pass P2 |
| 5 | The Accountability Gap | 13,369 | C | 3.1–3.3 (PROPOSED), 3.4 | **Whole-cloth redraft** (A1 Polanyi/Fraser/Sandel absent; $108T Phase C; em-dash 153; D1/D10) — fires NOW, brief pre-written |
| 6 | Three Ways of Counting | 13,425 | A | 3.1–3.4 | Mechanical redlines (coal figure, SCC attribution, Method-1 prose↔table, IPG 33–122× retire) ride numeric sweep; 3.5; prose pass P1 |
| 7 | On Other Worlds | 9,264 | A | 3.1–3.5, Stage 4 | Stage 5 only; coal-figure line rides sweep; prose pass P3 (lightest) |
| 8 | What Things Actually Cost | 6,495 | D | 3.1–3.5, Stage 4 | Author call #5 (recommend spot-fix); retract+re-issue stale Stage-5 arithmetic sign-off post-sweep; prose pass P1 |
| 9 | Pricing Honestly | 11,307 | C | 3.1–3.5 | **Whole-cloth redraft** (A3 cut to ~4,900–5,200w; D2/D3/D11/A2; 15 citation gaps) — brief pre-written, needs committing; fires NOW |
| 10 | Common Bonds | 5,384 | A | 3.1, 3.3(light), 3.5 | ~510w SAFE trims + line-94 fix; Stage 4/5; **register exemplar for prose campaign** |
| TA | Technical Appendix | 46,067 | — | M3 Path-A closeout COMPLETE (held) | Error-review session folds in → author diff review → merge → Stage-4 PDF render audit (ς glyphs) + notation consolidation |

Cross-cutting (do once, post-TA-merge, NOT per-chapter):
- Coal $4.50 → ~$4.70–4.85 (Ch 6, 7, 8, 9 + any essay carrying it).
- IPG 33–122× → M3 premium-multiple ~8.5–26× (Ch 6, Ch 8; TA already retired).
- Norway ~$48/BOE center + "~16% captured / 84% uncaptured" (essays may carry
  round "~17%").
- Ch 8 $496/$524 ↔ TA reconciliation + retract/re-issue stale "arithmetic
  verified" sign-offs (Ch 8 Stage 5; Ch 5 $108T-verified).

---

## 4. NEW WORKSTREAM — Whole-book prose-smoothing campaign (user request #1 + #3)

**Trigger:** fires immediately after TA merge + cross-corpus numeric sweep
land. **Goal:** smoothest prose the corpus can carry, book-wide, before
proposal assembly and agent Wave 1.

### 4.1 Findings (full-corpus prose read, 2026-06-10)

Chapter grades: Ch 10 **A** (register model) · Ch 3, 4, 7 **A−** · Ch 1, 5,
6, 9 **B+** · Ch 2, 8 **B**.

Eight cross-chapter patterns, ranked by impact:

1. **Em-dash as default repair tool** (all chapters; worst Ch 1, 3, 5, 6;
   Ch 5 carries 153). Doing work a period, comma, or restructure should do.
   Existing em-dash memory discipline confirmed at book scale.
2. **Aphorism-at-section-close habit.** Nearly every section in Ch 1–5 ends
   with a settled quotable verdict; metronomic/didactic at book length.
   Vary: end some sections mid-argument or on a question.
3. **"It is not X. It is Y." inversion + fragment emphasis** ("Not from
   preference. From arithmetic.") ~1 per 3,000 words in Ch 8–9; LLM-cadence
   tell.
4. **Expository flatness in framework-heavy stretches** — tell-before-show.
   Acute: Ch 2 five-column ledger (categories without bodies), Ch 8 cost
   components (name → explain → figure ×8), Ch 9 policy steps, Ch 5 Baotou +
   healthcare. Fix polarity = Pass 3.5 restoration: one sensory-specific or
   person-specific sentence opening every technical slab.
5. **Repeated structural templates** — Ch 4 comparison blocks ("Norway did X.
   [Country] did Y. The difference is Z."), Ch 7 scenario template, Ch 6 RCV
   bullet predicates, Ch 8 component template. Break each template once or
   twice per run.
6. **Pet-word clustering** — "cost/severance/framework" (load-bearing but
   clustering), "real" (40+), "visible" (30+), "mechanism" (50+),
   "structure" (60+). Rotate grammatical role, bury mid-sentence.
7. **Meta-commentary tics** — "Here is what X proves," "I want to say,
   plainly" (4× in Ch 10), "sounds strange on first hearing." Trust the
   reader.
8. **Rule-of-three density** — effective individually, audible in aggregate.

**Register model:** Ch 10 opens and closes in the same grounded register and
carries framework weight through sensory arc — the campaign's target voice.
Strongest existing prose: Ch 3, Ch 7 Mars sequence, Ch 10 harbor frame.

### 4.2 Campaign design (PROPOSED — author ratification = decision #7)

- **Form:** per-chapter "Pass 3.2R smoothing" run (voice-polish polarity for
  patterns 1/2/3/5/6/7/8 + targeted 3.5-style restoration for pattern 4),
  Amendment-C interactive ratification (Options + Recommendation per
  finding), one chapter per session per parallel-session cadence.
- **Style charter (new artifact, drafted at campaign kickoff):** em-dash
  budget per 1,000 words; section-close variation quota; one
  sensory/person anchor per technical slab; term-rotation list; template-
  break rule; banned meta-commentary phrases. Lives in
  `tools/drafting-templates/`; cited by every smoothing brief AND by future
  Stage 2 briefs.
- **Priority order:** P1 = Ch 8, Ch 2, Ch 6 (framework-heavy, grades B/B+,
  worst flatness). P2 = Ch 1, Ch 4 (+ Ch 5, Ch 9 AFTER their redrafts land —
  do not smooth prose that is about to be redrafted). P3 = Ch 3, Ch 7,
  Ch 10 (light touch only).
- **Cascade compliance:** each smoothing run triggers automatic-on-edit
  cascade (3.1 + 3.2 + Stage 1c-light); light 3.3 re-fire after Phase C
  apply; 3.4 re-fire not routinely warranted (per Amendment B precedent).

### 4.3 Pipeline suggestions (user request #1)

1. **Add a book-scale cadence pass to the doctrine.** Pass 3.2 is
   per-chapter; Pass 3.5 is per-chapter restoration. Nothing in the pipeline
   catches patterns that only show at book scale (aphorism-close metronome,
   template repetition across chapters, pet-word totals). Propose
   codifying the §4.2 campaign as **Pass 3.6 (book-scale prose-smoothing)**,
   explicit-gate class, firing once per whole-book gate (pre-proposal,
   pre-publication).
2. **Instrument the invariant scanner with style telemetry.** Add
   informational/MEDIUM counters to `tools/quality-gates/regressed-patterns.yaml`:
   em-dash density per 1,000 words; "It is not X. It is Y." regex;
   "I want to say" / "Here is what" meta-commentary phrases; flagged
   pet-word counts. LOW severity — telemetry, not blocking — so drift is
   visible at every commit instead of rediscovered at the next read-through.
3. **Name Ch 10 as register exemplar in Stage 2 briefs.** Stage 1b template
   gains a "register model" line pointing at the Ch 10 harbor frame for any
   framework-carrying prose.
4. **Sequence numeric sweeps before prose passes, always.** This session's
   TA situation generalizes: any corpus-wide figure change invalidates
   line-level prose work in flight. Add to change-cascade routing: figure
   sweep → THEN smoothing/3.2/3.5.
5. **Stage-5 sign-off retraction protocol.** Ch 8's stale "arithmetic
   verified" sign-off shows sign-offs need a retract+re-issue step wired
   into the change-cascade when an upstream figure moves. One-line doctrine
   amendment.

---

## 5. TA-gated pitch/essay/proposal revision queue (user request #2)

Fires AFTER TA error-review session closes + TA merges. Owner: one
dedicated "post-TA refresh" session.

| Artifact | TA-indexed content | Action |
|----------|--------------------|--------|
| Book proposal `00_overview.md` + `05_chapter-summaries.md` | Norway $1.9T (TA now ~$2.0T GPFG); coal $4.50; $558 floor; McDowell/Libby multipliers | 🔴 Refresh before assembly (~Jun 14–20); explicit pre-agent gate |
| Noema essay | Norway fund AUM | Refresh at submit (or submission-day fact-confirm if submitted first) |
| Foreign Affairs essay | GPFG AUM + Norway framing | Refresh if submit slips past merge |
| Norway op-ed | Fund AUM + per-citizen + ~$48/BOE + capture % | Refresh at news-peg activation; trim ~26w over band |
| McDowell op-ed | Coal figures + Ch 6 multipliers | Refresh at news-peg activation |
| Atlantic Ideas essay | Ch 9-derived; coherence flag §A (closer standing-assignment) | Fix closer (decision #8) + figure check before submit |
| No TA dependency | Aeon, Public Books, $100 Barrel, Harper's, Atlantic main, NYRB | No refresh needed |

Also riding this gate: cross-corpus "~17%" → "~16% captured" sweep; chapter
Stage-4 render audit for TA (ς glyph/tofu check in containerized toolchain).

---

## 6. Merged date-anchored action list

| Date | Action | Owner |
|------|--------|-------|
| Now (Jun 10) | TA error-review session continues; author diff-review queued behind it | Author + TA session |
| Now | FA cover-letter ratify → submit; Noema decision | Author |
| Jun 9–13 | Public Books cover letter → submit | Author + session |
| Now (parallel) | Ch 5 redraft session fires (brief pre-written); Ch 9 redraft brief committed + fires | Sessions |
| On TA merge | Cross-corpus numeric sweep (one coordinated session) | Session |
| Sweep + ~1 day | Prose-smoothing campaign kickoff: style charter + P1 chapters (Ch 8, 2, 6) | Sessions |
| ~Jun 14–20 | Proposal figure refresh → assembly + offline render audit | Session + author |
| Jun 24–Jul 1 | Agent Wave 1 (compressed) — gated on proposal + Ch 5 | Author |
| Jul 1–5 | Aeon fallback submission window | Author |
| Early–mid Jul | Comp-titles Phase 2 web verification | Session |
| Before Wave 1 | Endnote/citation sweep Phase 2 (todo #11, HIGH); lawyer consult (todo #7) | Session + author |
| Aug 5 | Berggruen submission target (hard Aug 17) | Author |
| Oct–Feb | Wave 2 windows: NYRB (Oct 8–Nov 15), Harper's (Q4), Atlantic main (Oct–Dec), FA window if held (Nov–Feb) | Author |

---

## 7. Status buckets

**✅ DONE-DONE since 06-04:** TA M3 Path-A closeout (held); Norway $48/BOE
precision edit; Ch 5 $108T recompute ratified; redraft-campaign scope
correction ratified; Ch 9 five-pass Stage 3 closed (2026-05-25).

**🔄 IN FLIGHT:** TA error-review (author's parallel Fable session); Ch 5 +
Ch 9 redraft briefs (pre-written, unfired); Aeon portal watch; consent
tracker (11/12 §I gaps resolved).

**⏸ GATED:** numeric sweep, prose campaign, proposal refresh, TA-indexed
essay refreshes (all on TA merge); blurb network (on agent/contract sign);
Stage 5 sign-offs (on explicit gates, none complete corpus-wide).

**⚠️ WATCH:** Noema state ambiguity; chapters carrying retired 33–122×;
stale Ch 8 Stage-5 sign-off; Sandy Darity HELD email (decommission
candidate); `__Draft` suffixes Ch 1/2/5 (consent markers — verify tracker
before Stage 5).
