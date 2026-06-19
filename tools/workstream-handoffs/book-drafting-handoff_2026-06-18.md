# Book-Drafting Handoff — 2026-06-18

**From:** PM/book-drafting session `claude/pm-book-completion-260610-07b75f` (winding down).
**To:** the dedicated book-drafting session that runs the Ch 6/7/8/9 whole-cloth rebuilds.
**Branch state:** rebased onto `origin/main` @ `9f4b52a5` (2026-06-18); all this session's chapter work is already on main.

---

## 0. What this handoff is

The Ch 6/7/8/9 whole-cloth rebuilds were queued and a redraft run was in
flight (`wf_f33b8ef6-8e9`) when two parallel sessions landed ratified material
that the rebuild MUST carry. That run predates both inputs, so its output is
stale — **STOP it and re-fire 6/7/8/9 from the amended briefs** (the briefs now
carry the coordination context; see §3). This is the discipline-correct path:
the new material goes into the briefs, then a blind draft builds it in-register
(never grafted as a section afterward).

---

## 1. Chapter version map (so cross-session anchors resolve)

`e70ea0d0` (the H1-H5 anchor snapshot, 06-18) is AFTER this session's Ch
2/3/4/5/10 promotions (06-17), so those anchors already match the promoted
versions. Only Ch 6/7/8/9 are open.

| Ch | Status (current main) | Anchor situation |
|----|----------------------|------------------|
| 1 | redlined canonical | settled; place by content if anchored |
| 2 | PROMOTED redo2-B (06-17) | in e70ea0d0 — anchors match |
| 3 | full canonical + 4 ADDED beats (06-17) | base preserved — anchors match; H5 Ch3 = verify-at-redline only |
| 4 | PROMOTED redo-A (06-16) | in e70ea0d0 — anchors match; **owes the H5 Ch4 Zucman/Ndikumana insertion** (place by content) |
| 5 | canonical + fills (06-17) | in e70ea0d0 — anchors match; owes Insertions B/C/G (Ch5) |
| **6** | NOT promoted — **rebuild from amended brief** | whole-cloth; place all inserts by CONTENT |
| **7** | NOT promoted — **rebuild from amended brief** | whole-cloth; no H1-H5 inserts target it |
| **8** | NOT promoted — **rebuild from amended brief** | whole-cloth; owes Insertion K |
| **9** | NOT promoted — **rebuild from amended brief** | whole-cloth; owes Insertions E/F/H |
| 10 | PROMOTED redo2-B (06-17) | in e70ea0d0 — anchors match; owes statism cross-ref (Insertion E points at Ch10 L170-174) |

**Rule for all open chapters: place inserted material BY CONTENT, not line
number — the whole-cloth drafts will not match the canonical line anchors.**

---

## 2. The two coordination inputs (already folded into the briefs)

1. **Ch 6 L323-fix session** (commits `f1fd6801` + `5cd59a12` + `1034f3ac`):
   killed the false "neither addressed" positioning claim; ratified the
   corrected positioning (instrument FORM + LEVEL on the Pigou / Ostrom-
   asymmetry / Hartwick-Dasgupta axes) + a hard GUARD against any universal-
   negative. **This is a contribution claim — it belongs IN the Ch 6 brief
   (done, §3) so the blind draft builds it coherently, not as a bolt-on.**
2. **H1-H5 matrix-insertions session** (`matrix-h1-h5-ratified-insertions-handoff_2026-06-18.md`,
   commit `7364d69d`): PROPOSED, author-ratified prose blocks A-M, em-dash-
   free, substrate-safe (H1 credits the reparations field with NO coercion
   figure). The blocks targeting the open chapters: **Ch 6** = A (Broome),
   I (Solow/Dasgupta), J (Dasgupta-2021, coordinate w/ the L323 sentence);
   **Ch 8** = K (Hotelling/Costanza, respect the HELD-gate note); **Ch 9** =
   E (Nozick), F (Gardiner), H (Christophers fuller engagement); **Ch 7** =
   none.

---

## 3. The amended briefs (ready to draft from)

Each carries an `## ADDENDUM 2026-06-18` with its coordination context:
- `research/story-drafts/ch6-blind-brief-v3_2026-06-16.md` — positioning + guard (full) + Insertions A/I/J.
- `research/story-drafts/ch7-blind-brief-v3_2026-06-16.md` — no H1-H5 inserts; matrix-v2 fills only.
- `research/story-drafts/ch8-blind-brief-v3_2026-06-16.md` — Insertion K.
- `research/story-drafts/ch9-blind-brief-v3_2026-06-16.md` — Insertions E/F/H.
All briefs em-dash-free; all carry the matrix-v2 fills from the prior amend pass.

## 4. Run shape + gates (reuse the prior workflow design)

Per-chapter pipeline: draft 2 blind variants from the amended brief → judge
(positioning-first; fidelity; flatness; non-regression vs the prior redo
winner). Reuse/adapt the script at
`.../workflows/scripts/ch6789-matrix-redraft-wf_9b0960fa-29f.js` but point the
drafters at the v3 briefs (now amended) and the judges at: **Ch 6** must land
the corrected positioning + carry A/I/J + trip NO universal-negative;
**Ch 8** carry K + the just-rebranded-externality objection; **Ch 9** carry
E/F/H + Susskind restore + financialization answer. Zero em-dashes; no
invented facts; figures per `manuscript/ledgers/_CANONICAL_FIGURE_LEDGER.md`.

## 5. Settled this session (do not redo)

Ch 1 (redlined, ready), Ch 2/3/4/5/10 (promoted/filled, on main, each with
ADDED/ENHANCE marked beats awaiting the author redline). Ch 3 was kept FULL
(Option B) — do NOT promote the compressed `ch3-redo2-A`. The held TA §11.12
reef branch (`claude/ta-reef-migration-260611-ae0141`) is one-click mergeable,
MERGE-HELD on three author §11.12 calls; Ch 3 still prices the reef (GATE 2 ok).

## 6. Open author items (carry to the PM surface)

FA full redraft is unblocked (Ch 4 promoted). Essay-drafting session has its
own dashboard (`essay-drafting-dashboard_2026-06-15.md`). Author redline is the
final stage for every promoted chapter.
