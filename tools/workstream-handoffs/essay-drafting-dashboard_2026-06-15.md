# Essay & Op-Ed Drafting Dashboard — 2026-06-15

**Owner:** dedicated essay-drafting session (spawned 2026-06-15).
**Scope:** the derivative essay/op-ed portfolio ONLY. Chapter redrafts,
book proposal, and the matrix audit are other sessions — do not touch them.
**State source:** verified on disk 2026-06-15 (not from memory). The book
side is at STATE.md; this file is the essay-side operating surface.

---

## 0. Standing rules (author-ratified — apply to every piece)

1. **Lit-positioning is PRIMARY** (`feedback_lit_positioning_primacy.md`,
   2026-06-11): every piece must illustrate how the book supports /
   contradicts / adds to named adjacent literature; beat-capture is
   secondary. Judges score positioning FIRST, then flatness, then prose.
2. **Blind-draft-from-brief-only discipline** (the integrity rule the
   author re-affirmed 2026-06-15): fresh drafters read the brief + its
   ADDENDUM + named substrate ONLY — never the canonical essay or another
   venue's text. A missed beat is a BRIEF failure → amend the brief and
   re-draft; do NOT graft canonical prose (grafting is the seam-clunk the
   author rejected). Cross-variant A↔B fold-ins are fine (same brief register).
3. **Flatness watch:** an accurate-but-flat draft does not promote without a
   named remedy; the author's redline is the codified final stage.
4. **Standing drafting greenlight:** draft both variants the moment a brief
   is ready — no per-piece authorization. Author gates remain at PROMOTION
   and SUBMISSION only.
5. **Hard rules:** zero em-dashes in candidates; no invented facts
   (structure-notes for gaps); figures trace to `manuscript/ledgers/_CANONICAL_FIGURE_LEDGER.md`;
   TA canon per the brief (M2 = realized-Bond reader, lens-explicit IPG,
   Norway α-reduction not rent-capture, scope correction). Never a
   coercion/reparations dollar figure.

---

## 1. What the essay drafting process produced so far (verified 2026-06-15)

Two fleet runs fired and BOTH hit weekly session-token limits mid-run
(essay-redraft-fleet `wf_64743ae8-516`; noema-redraft `wf_9faefe26-a6c`).
What actually landed on disk:

- **6 redraft briefs built + lit-positioning ADDENDUM appended** (Harper's,
  NYRB, Atlantic main, Atlantic Ideas, Norway op-ed, McDowell op-ed) + the
  **Noema** brief (`redraft-brief_2026-06-11.md`, the new lit-positioning-first
  one, path-c full redraft).
- **Candidate drafts** (all blind-from-brief): see §2 table.
- **ZERO judges/compares have run** for ANY essay or op-ed. Nothing is
  "promoted." The chapter-side verdicts do NOT exist here yet.
- **Submission-readiness verdicts** (separate `wf_52e17340-1e0`, complete):
  Aeon SUBMIT-AS-IS · Atlantic Ideas + Noema SPOT-FIX · FA + Public Books
  UPDATE-FIGURES. FA spot-fixes already APPLIED to canonical (false
  supermajority + Støre + GPFG, commit `d1b5df2`). Atlantic Ideas §A closer
  ("theirs to enter" dropped) already APPLIED to canonical.

---

## 2. Per-piece state + what's left

| Piece | Brief | Candidates on disk | Judge | Next action |
|---|---|---|---|---|
| **Harper's** (Ch 2) | ✅ +addendum | A (8,015w, 0 em) + B (6,557w, 0 em) | ❌ none | **JUDGE A vs B vs current** (positioning-first) |
| **Atlantic Ideas** (Ch 9) | ✅ +addendum | A (4,998w, 0 em) + B (4,806w, 0 em) | ❌ none | **JUDGE.** Note: canonical §A closer already fixed; spotfix spec in rigor/ for figure items |
| **Atlantic main** (Ch 3) | ✅ +addendum | A (7,830w, **5 em**) + B (9,437w, **5 em**) | ❌ none | **Em-dash scrub BOTH candidates first** (rule violation), then JUDGE. Ruth-quote fidelity per brief |
| **NYRB** | ✅ +addendum | **B only** (4,508w, 0 em) — A failed at limit | ❌ none | **Re-draft variant A** from brief, then judge. §VIII anchor author-call carried in brief |
| **Norway op-ed** | ✅ +addendum | **A only** (1,026w, 0 em) — B failed; **A is OVER the 750–900 band** | ❌ none | **Re-draft B + trim A into band**, then judge. α-reduction reframe |
| **McDowell op-ed** | ✅ +addendum | **none** — both failed at limit | ❌ none | **Draft A + B** from brief, then judge. Pinned $496/$510/2.61 + lens-explicit IPG |
| **Noema** (Ch 1/book-wide) | ✅ 06-11 (path-c) | **none** — drafts never fired | ❌ none | **Draft A + B** from brief, then judge. Historical-drift anchors (Pou/Pooh, hunting, cussing-at-self) MUST survive |
| **Public Books** (Ch 5) | — (spotfix spec) | n/a (fix-apply, not redraft) | n/a | **Apply the fix bundle** F1–F7 + P1/P2 + draft the (nonexistent) PB cover letter + research venue norms. No external deadline — do it right |
| **Foreign Affairs** (Ch 4) | spotfix applied | n/a | n/a | **GATED:** full redraft fires when Ch 4 promotes (fork option c). Canonical already has false-claim fixes. Window Nov–Feb, no rush |
| **Aeon** (pitch) | — | n/a | n/a | **SUBMIT-AS-IS** — portal-gated only. Courtesy email ready at `courtesy-email-READY_2026-06-11.md`. No drafting work |

---

## 3. Work queue (ordered; each is one workflow phase)

**A. Judge what's already drafted (no new drafting needed):**
1. Harper's A vs B — both clean, ready now.
2. Atlantic Ideas A vs B — both clean, ready now.
3. Atlantic main — scrub 5 em-dashes from each candidate, THEN judge.

**B. Finish partial drafting, then judge:**
4. NYRB — draft variant A (B exists), then judge A vs B.
5. Norway op-ed — draft variant B + trim A into the 750–900 band, then judge.

**C. Draft from ready briefs (greenlit), then judge:**
6. McDowell op-ed — draft A + B, then judge.
7. Noema — draft A + B, then judge (flagship; protect the drift anchors).

**D. Non-redraft tracks:**
8. Public Books — apply the spotfix bundle + cover letter + venue norms.
9. Foreign Affairs — hold until Ch 4 promotes, then fire the redraft.
10. Aeon — no work; portal watch is the author's.

Every judge writes `rigor/redraft-compare_2026-06-15.md` (PROPOSED) with the
positioning + aliveness rows and an A↔B fold-in list. Promotion is
author-gated; bring verdicts back, do not self-promote.

---

## 4. Token discipline

Both prior fleets died at weekly limits. Run in SMALL batches (judge the
3 ready pairs first — cheapest, highest value — before any new drafting).
Every workflow that fans out is resumable: on a limit hit, re-invoke with
`{scriptPath, resumeFromRunId}` — completed agents return from cache. Bank
landed artifacts with a commit before any risky next batch.

---

## 5. Cross-session coordination

- **Atlantic main + Noema + Atlantic Ideas + FA** derive from chapters
  (Ch 3 / Ch 1 / Ch 9 / Ch 4). Ch 2 + Ch 3 are PROMOTED; Ch 1 redlined;
  Ch 4/9 winning drafts chosen but NOT promoted. If a chapter's promoted
  text shifts under an essay, re-verify the essay's borrowed facts.
- The book-proposal session + matrix-audit session are separate; do not
  edit `publishing/book-proposal/` or `manuscript/`.
- Update this file's §2 table on every state change; STATE.md owns the
  one-line portfolio status.
