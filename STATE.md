# STATE.md — live project status (single source for "where does X stand?")

**Discipline.** Any session that *changes* a status below updates that one line (with the date)
in the same commit. Status vocabulary: `tools/conventions/status-markers.md`. Orientation:
[MAP.md](MAP.md). Process + operating mode: see CLAUDE.md's **CURRENT OPERATING MODE** banner
(lean pipeline, one session at a time, RATIFIED 2026-10-25).

**▸ RECONCILED 2026-10-31** (Fall-plan W1 item 2) — this file was stale from late June; it is now
current as of today, built from the plan's verified chapter table + the 2026-10-31 session handoff
+ the author's W1 status answers. The governing plan is
[`tools/workstream-handoffs/commons_bonds_work-plan_2026-10_to_2027-08_v1.0.7.md`](tools/workstream-handoffs/commons_bonds_work-plan_2026-10_to_2027-08_v1.0.7.md).
For the detailed June snapshot (audit trail) see the 2026-06-10 PM dashboard + git history; this
file is the live surface and supersedes the June rows.

**Capacity:** ~1–2 hrs/week in semester; full-time over winter break (≈ Dec 14 – Jan 10, author-confirmed
2026-10-31) and summer 2027.

---

## ▸ TOP PRIORITY — the Darity package (Ch 1 + Ch 5 + corrected Technical Appendix)

Sandy Darity asked for the corrected TA plus any two chapters; the author chose **Ch 1 and Ch 5**.
**Author status (2026-10-31):** the relationship is warm — emails have been exchanged and Darity
knows about the author's accident, recovery, and nursing-school focus. **He is waiting on the
revised Ch 1, Ch 5, and corrected Technical Appendix.** He has **hinted at a possible path to
publish**, contingent on reading the sample chapters + TA ("to see if I can write"). His candor is
the asset; the foreword/publisher question waits until he raises it himself.

- **Agent queries (Wave 1): HELD for his read** (up to ~mid-February), then the route is chosen
  (his introduction → university-press path; or comments-only → fire Wave 1 ± Pipeline B).
- **Schedule:** TA + Ch 1 → early December (plan W6); **Ch 5 → Jan 4–5**.
- The handoff's "five-months-silence / personal note" watch item is **RESOLVED** by the author's
  answer: contact is active and he is aware of the circumstances; the next contact is the Dec send.

| Piece | State (2026-10-31) | Still needs before it goes |
|---|---|---|
| **Technical Appendix** | v2.0.0 on main; calc engines re-ran clean 2026-10-25 (21/21, 24/24) | Apply 06-24 positioning findings (none in it yet); 3 reef §11.12 calls; §6.3/§6.2 loose ends; render check; changelog vs his 05-15 copy; list of his call-material for approval |
| **Chapter 1** | Ready to ship since 06-11 (touched 06-17 by a mechanical fix) | Fact-check vs ledger + grammar polish + author final read |
| **Chapter 5** | **Rebuild brief APPROVED 2026-10-31** (`tools/workstream-handoffs/ch5-rebuild-brief_2026-10-31_v1.0.0.md`): A/B/C variants, 1972 SS anchor, grounding = diagnostic, 2008 first-person substrate captured | Draft Variant A (scale-narrative, out-and-back) + Variant B (grounded-scatter) + current as C → judge → fact-check winner → author picks (Dec) → hand redline → polish. Drafting background, **starts next session** (SSA-gated for the SS rung) |

---

## Book — chapters (verified against git 2026-10-25, per the plan's table)

Ch 1 ready; **Ch 2, 3, 4, 10 need only the author's redline**; **Ch 5–9 need a full rebuild first**
(Ch 5 is urgent — the second Wave-1 sample; Ch 6–9 rebuild through spring, redline in summer).

| Ch | Title | State on main | Still needs | Who |
|---|---|---|---|---|
| 1 | The Quiet Math | **Ready to ship** (redline applied 06-11; sample copied into proposal) | A quick reread at assembly | — |
| 2 | The Miner | **Promoted 06-17** (redo B); positioning check cleared its Fraser use | Author **redline**: 2 enhancement candidates + 1 fold-out | Author |
| 3 | The Waterman | **Promoted 06-11** (incl. priced reef section; 8 ADDED beats 06-17) | Author **redline** of the 8 beats + **3 calls** releasing the held TA §11.12 reef merge | Author |
| 4 | The Existence Proof | **Promoted 06-16** (redo A) | Author **redline**: 10 enhancements + 3 candidates; place **Insertion M** (Zucman/Ndikumana-Boyce); this also unblocks the FA redraft | Author, then a session |
| 5 | The Accountability Gap | Working draft + fills; **rebuild brief APPROVED 2026-10-31** (A/B/C variants; 1972 SS anchor; grounding = diagnostic; 2008 first-person substrate captured) | Drafting (Variant A scale-narrative out-and-back + Variant B grounded-scatter + current as candidate C) is background work, **starts next session** (SSA-gated for the 1972 SS rung); judged recommendation before winter break; **author picks in Dec**. **Wave-1 critical path.** | Session + author |
| 6 | Three Ways of Counting | Old version (method on the retired three-estimator frame; L323 positioning fixed 06-18) | **Full rebuild** from the amended v3 brief (needs 06-24 positioning folded in); Insertions A/I/J; numbers settled | Session + author |
| 7 | On Other Worlds | Old version (fails its gate) | **Full rebuild** from amended v3 brief; no insertions | Session + author |
| 8 | What Things Actually Cost | Old version (fails its gate) | **Full rebuild** from amended v3 brief; Insertion K | Session + author |
| 9 | Pricing Honestly | Old version (fails its gate) | **Full rebuild** from amended v3 brief; Insertions E/F/H | Session + author |
| 10 | Common Bonds | **Promoted 06-17** (redo B) | Author **redline**: 4 enhancements + 1 candidate; Ch 9 Nozick cross-ref once Ch 9 rebuilt | Author |

**Technical Appendix + back matter:** TA v2.0.0 on main, internally consistent, invariants HIGH=0,
glyphs tofu-free; engines re-ran clean 2026-10-25. Back matter is generated
(`tools/back-matter/build.py gen-all`). TA pre-Darity work is plan W4–W5 (see the Darity section).

**Redlined vs promoted — the distinction that matters:** "promoted" = a session's whole-cloth redraft
landed on main; "redlined" = the author's hand pass applied. **Only Ch 1 has been author-redlined.**
Ch 2/3/4/10 are promoted drafts **awaiting the author's redline**; Ch 5 is in rebuild (brief approved);
Ch 6–9 are old versions needing a rebuild before any redline.

### Book-wide consistency (the "change it everywhere, all at once" discipline)

The lists that track book-wide drift and enforce one-change-everywhere:

- **Canonical figure ledger** — [`manuscript/ledgers/_CANONICAL_FIGURE_LEDGER.md`](manuscript/ledgers/_CANONICAL_FIGURE_LEDGER.md).
  THE single source of truth for shared figures; every chapter, the TA, and every essay/op-ed must match
  it. It carries the per-figure **cascade-targets ("still needs editing") list**.
- **Automated gates** — `tools/quality-gates/regressed-patterns.yaml` + `scaffolding-patterns.yaml`, run
  by `tools/scripts/check-corpus-invariants.sh` on every commit (HIGH=0 blocks). **Every ratified ledger
  amendment gets a gate pattern in the same commit** so a retired figure can never silently return
  (e.g., the 2026-10 coal $4.71 fix + the 3b retired-figure gates).
- **Verified positioning findings** — [`tools/workstream-handoffs/verified-positioning-findings_2026-06-24.md`](tools/workstream-handoffs/verified-positioning-findings_2026-06-24.md).
  Book-wide positioning to apply across chapters/TA/essays as each is touched.
- **Matrix insertions H1–H5 / A–M** — [`tools/workstream-handoffs/matrix-h1-h5-ratified-insertions-handoff_2026-06-18.md`](tools/workstream-handoffs/matrix-h1-h5-ratified-insertions-handoff_2026-06-18.md).
  Ratified cross-chapter engagement additions, placed at each chapter's rebuild/redline (Ch 5 gets B/C/G).

---

## Portfolio — essays

Lean pipeline: essays run the loop **once**; no second round without a trigger (rejection-with-
feedback, a retired figure, or a venue change). The June per-essay session delegations are
**SUPERSEDED** (one-session mode) — see below.

| Unit | Venue | State (2026-10-31) | Next action |
|---|---|---|---|
| $100 Barrel | American Prospect | **SUBMITTED 2026-06-17** (Submittable); **no reply as of 2026-10-31 → presumed pass** (author checked) | Cascade closed unless pursued (RWER was the noted tertiary). Low priority. |
| Architecture and Its Residue | **NYRB** | RATIFIED-AWAITING-SUBMIT on main (`publishing/essays/nyrb-multi-book-review/essay.md`, ~8,300w; cover letter ratified); carries the *Rentier Capitalism* H4 carry | **W2 SUBMIT — window closes Sun Nov 15.** Session preps the submit package (confirm NYRB's current method). |
| What McDowell County Paid | Harper's | V-D on main; June redraft-A promotion **SUPERSEDED** (no 2nd round w/o trigger) | **W3 submit the V-D version as-is** (~20 min). |
| Commons Bonds | Noema | V-D-prime on main (RATIFIED-AWAITING-SUBMIT); June path-c redraft delegation **SUPERSEDED** | Submit over winter break (plan Window 2 Week D). |
| Mask of Abundance | Aeon | V-E on main; portal-watch (aeon.co unreachable from this environment) | Author: one check of the pitch-guidelines page + set a stop date (Dec 31 suggested). |
| Pricing Honestly | Atlantic Ideas | On main; coal **$4.71** fix applied 2026-10-29 | Cover letter still says "$520–600" honest cost vs ledger floor **$510** (author OK open). May yield the Ideas slot to the data-center pitch (winter decision; Foreign Policy is the listed fallback). |
| What the Bay Knows | The Atlantic (features) | RATIFIED-AWAITING-SUBMIT (V-D hybrid on main) | Spring: decide when to send (after the Ideas pitch has an answer, so the Atlantic isn't sent two things at once). |
| Existence Proof | Foreign Affairs | Ch 4 promoted 06-16; FA whole-cloth redraft **HELD** on brief ratification + Ch 4 redline | Summer 2027 (window Nov 2027–Feb 2028): ratify brief → Ch 4 redline → draft. |
| Accountability Gap | Public Books | Cascading from BR reject (06-03); cover letter in flight (06-04) — **stale, verify at next essay slot** | Low priority; ratify PB cover letter → submit if pursued. |
| Berggruen Prize 2026 | Berggruen | **NOT submitted; 2026 window closed** (deadline Aug 17, during the pause; author confirmed 2026-10-31) | Berggruen **2027** scheduled for summer (verify deadline; drafting must be AI-free + offline) if the prize runs. |

---

## Portfolio — op-eds + proposal + agents

| Unit | State (2026-10-31) | Next action |
|---|---|---|
| Norway op-ed (FT/Bloomberg/PS) | V-D′ on main; June delegation **SUPERSEDED** | News-peg activation is the author's call; otherwise hold. |
| McDowell op-ed (**→ The Guardian**) | op-ed.md promoted 06-19 (body ~1,263w; canon figures $4.71/2.61/$496/$510; zero dashes); venue cascade Guardian→NYT→PS→Bloomberg→WaPo | Author redline + band-trim to ~1,000–1,100w (2 micro-calls open) → news-peg → submit (author-gated). |
| **Data-center** op-ed (Virginia) + Atlantic Ideas pitch | Drafts + lead-level fact base in `research/story-drafts/datacenter/` (PROPOSED 2026-10) | **NOT submittable:** [V1]–[V10] figures unverified (network blocked every source page). README has the checklist + author decisions. **Winter break;** op-ed pegged to the January General Assembly session. |
| **Book proposal** | §00 overview RATIFIED + merged 06-24; query letter + pre-pub review queue ratified; editor research done (UNC→Kinney, Duke→Wissoker/Berger, HUP→Tovbis) | **Winter break (Window 2 Week C):** author voice redline of §00 + open decisions (AI-disclosure placement; §02 comps refresh; Ch 7/9 no-overclaim; airlock-vs-coal-first); bio → nursing program; assembly (NOK→USD re-stamp, PDF render, Darity attribution placeholder). |
| Agent pipeline (Wave 1) | Scaffolded, **0 queries sent**; targets at `publishing/agents/_pipeline/targets.md` | **HELD for Darity's read** (up to ~mid-Feb), then route chosen. Proposal finished over break regardless (a press needs it too). |

---

## SUPERSEDED — do not resume (one-session mode + the plan)

These June artifacts are retired by the plan and the CURRENT OPERATING MODE banner. Do not resume them.

- Essay redraft fleet **`wf_64743ae8-516`**; Noema redraft **`wf_9faefe26-a6c`** (paused workflows).
- The per-essay session delegations (2026-06-19) and the "FULLY DELEGATED" essay posture.
- The 06-18/06-19 Ch 6–9 rebuild / book-drafting dashboard delegation.
- The 2026-06-11 token-conservation PAUSED hold — its live items are folded into the plan's windows
  (Ch 6 rebuild prerequisites remain valid as inputs to the spring rebuilds).

Chapter rebuilds (Ch 5–9) run **one session at a time** under the plan, not as a fleet.

---

## Author status answers captured (W1, 2026-10-31)

1. **American Prospect / $100 Barrel:** no reply on Submittable → treat as a pass.
2. **Berggruen Prize 2026:** not submitted; the 2026 window closed during the pause → skip to 2027.
3. **Darity:** in active email contact; he knows about the accident and the recovery/school focus;
   he is awaiting the revised Ch 1 + Ch 5 + corrected TA; he has hinted at a possible publishing path
   contingent on seeing the samples + TA. (Agent queries held for his read.)
4. **VPCC winter break:** ≈ Dec 14 – Jan 10 (the plan's assumption holds).

---
*Reconciled 2026-10-31 (Fall-plan W1 item 2) from the work plan v1.0.7 + the 2026-10-31 handoff +
the author's W1 answers. Next PM reconciliation: at the next status change, per the discipline above.*
