# Cross-Essay Portfolio Review — 2026-05-27

**Status:** **PROPOSED** at session start → **RATIFIED** at session close (per Amendment C interactive ratification protocol for portfolio inventory artifacts; auto-fast-forward to main per CLAUDE.md merge-to-main policy as internal scaffolding).
**Date:** 2026-05-27
**Scope:** Cross-essay portfolio inventory + feature-branch reconciliation + rigor-pass artifact coverage + pre-submission action items + cascade-plan position check + cross-essay coherence check + recommendations.
**Audit basis:** `origin/main` HEAD at session start = `18f47a1` (*Aeon essay file-org fix — cross-reference updates*); compared against all feature branches with commits ahead of main as of 2026-05-27.
**Worktree:** `/Users/c17n/commons-bonds-cross-essay-portfolio-review-260527-910102` (branch `claude/cross-essay-portfolio-review-260527-910102` off `origin/main`).
**Author state (per `publishing/essays/_pipeline/june-2026-submission-schedule.md` + cascade plan v2):** parallel-session-hop sprint mode through 2026-05-27; multiple essays moving through v3.1 five-pass cascade simultaneously; submission sprint window May 25–31 partway through.

---

## §0. Portfolio-state framing (author corrections 2026-05-27)

**The essay portfolio is functionally complete except Ch 2 → Harper's, which is imminent** (Pass 3.4 RATIFIED ROBUST during this audit session; Pass 3.5 kickoff STAGED; Stage 4 + Stage 5 expected to fire within hours). All other Wave 1 + Wave 2 + Wave 3 essays are either RATIFIED-AWAITING-SUBMIT, pitch-LOCKED, RATIFIED READY-TO-SUBMIT (FA awaiting merge authorization; Atlantic Ideas awaiting cover-letter drafting only — see §0.1 correction below), or in post-rigor bookkeeping (NYRB per-essay folder mirror). Berggruen runs on a separate AI-free track and is not gated by AI-collaborative pipeline state.

**What "post-rigor bookkeeping" means and does NOT mean:** rigor passes (3.1 fact-check + 3.2 voice-polish + 3.3 acceptance + 3.4 adversarial + 3.5 developmental) are SUBSTANTIVE work that affects publisher-facing prose. Stage 5 sign-off filings, per-essay folder mirrors, cover-letter drafts, README refreshes, and feature-branch merges to main are HANDOFF / FILING steps — necessary for submission but not gated by rigor-work-still-to-fire. The distinction matters because: a "still pending" framing that conflates the two reads the portfolio as more in-flight than it actually is, and risks miscalibrating PM-session priority.

This framing note was added per author correction post-session-close ("the only essay that isn't complete is harpers and that completion is coming any moment now"). The original §1–§8 inventory + recommendations are factually accurate but were framed without this distinction; §8.G recommendation-priority levels are corrected below to reflect the actual rigor-vs-bookkeeping split.

### §0.1 Audit correction (added 2026-05-27 post-resume per author second correction)

**Atlantic Ideas is substantively complete, not "Stage 5 sign-off close-out pending."** The original §1.3 + §3 + §5 + §7 + §8 entries claimed Atlantic Ideas had no Stage 5 sign-off filed; the original §8.B.2 recommendation said "Stage 5 close-out session needed (sign-off + cover-letter + README refresh)." **This was wrong.** The Stage 5 sign-off + pre-publication review queue artifacts DO exist under filing-convention paths this audit failed to scan:

- **Stage 5 sign-off:** [`publishing/essays/atlantic-ideas-pricing-honestly/rigor/stage-5-signoff.md`](../../publishing/essays/atlantic-ideas-pricing-honestly/rigor/stage-5-signoff.md) — **RATIFIED PASS 2026-05-27** post-Option-1-revert; verdict "READY-TO-SUBMIT"
- **Pre-publication review queue:** [`tools/pre-submission-reviews/atlantic_ideas_pre_pub_review_queue_v1.0.0.md`](../../publishing/essays/atlantic-ideas-pricing-honestly/rigor/pre-pub-review-queue.md) — **RATIFIED 2026-05-27**

**Three artifact-filing-conventions exist in the project, not two.** This audit identified Convention A (per-essay-only) and Convention B (per-essay + central at `tools/rigor-passes/`), but missed Convention C (central at `tools/quality-gates/sign-offs/` + separate pre-pub queue at `tools/pre-submission-reviews/`). Convention C is used for **chapters + Atlantic Ideas** specifically; it carries Stage 5 sign-offs for ch1, ch3, ch4, ch5, ch6, ch7, ch8, ch9, ch10, chapter-2, ta, and atlantic_ideas at `tools/quality-gates/sign-offs/`.

**Per the Atlantic Ideas Stage 5 sign-off §8 "What comes next" verdict, the only remaining items for Atlantic Ideas are:**
1. Pitch / cover-letter drafting per brief §11 (Atlantic Ideas pitch format — short cover note + tighter-than-essay register). Explicitly *not produced* in the Stage 5 session.
2. Submission to Atlantic Ideas section post-cover-letter ratification.
3. (Bookkeeping) README refresh at `publishing/essays/atlantic-ideas-pricing-honestly/README.md`; per-essay `stage-5-signoff.md` mirror creation (optional).

Atlantic Ideas is at the **same state Foreign Affairs was at audit start** — RATIFIED READY-TO-SUBMIT pending cover-letter drafting. §3 + §5 + §7 + §8 entries below are factually accurate at the substantive level *with this correction applied:* the canonical-completeness column for Atlantic Ideas should read complete-at-Convention-C-level (Stage 5 sign-off + pre-pub queue both on main), not "Stage 5 sign-off close-out pending."

**Future portfolio-review methodology fix:** scan all three conventions — `tools/rigor-passes/`, `tools/quality-gates/sign-offs/`, AND `tools/pre-submission-reviews/` — at audit start. See updated memory [`tools/memory/feedback_rigor_vs_bookkeeping_distinction.md`](../memory/feedback_rigor_vs_bookkeeping_distinction.md) for the three-convention scan discipline.

---

## §1. Per-essay portfolio inventory

Nine active essay folders on `origin/main` (excluding `_pipeline/`, `_shared/`, `_archive/` infrastructure).

### 1.1 `100-barrel/` → Phenomenal World

- **Essay title:** *The $100 Barrel*
- **Venue:** Phenomenal World (target; per cross-thread-todos #4 resolution)
- **Stage state:** **RATIFIED-AWAITING-SUBMIT** (Stage 5 sign-off RATIFIED 2026-05-24; cover letter RATIFIED 2026-05-24).
- **Canonical layout on main:** ✓ `README.md` · ✓ `essay.md` · ✓ `cover-letter.md` · ✓ `stage-5-signoff.md` · ✓ extra: `passage.html` (HTML rendering) · ✗ no `_archive/` on main (Draft B archived under `archive/_OneDayMaybe/100-barrel-essay-variants/` per Q3 reorg discipline).
- **Word count (essay.md body):** ~4,248w (per Stage 5 sign-off frontmatter).
- **Last activity on main:** `52fde31` (Publishing-pipeline reorg Session 2 APPLIED — 50 file moves + 10 READMEs) — pre-2026-05-25; per the Stage 5 sign-off frontmatter the essay.md HEAD itself is at `b853f42` from the parallel-session apply.
- **Discipline note:** essay.md last *content* commit predates the reorg session (Pass 3.5 + light Pass 3.3 re-fire 2026-05-23 → 2026-05-24); reorg session re-touched paths only.

### 1.2 `aeon-mask-of-abundance/` → Aeon

- **Essay title:** *The Mask of Abundance* (Version C pitch body; 297w)
- **Venue:** Aeon (pitch-first model; full essay developed post-acceptance via editor collaboration).
- **Stage state:** **Pitch-ready (LOCKED 2026-05-08)**; submission target **Sun May 31 14:01 UTC** (hard deadline per Aeon portal window).
- **Canonical layout on main:** ✓ `README.md` · ✓ `essay.md` (Version C; 297w pitch body) · ✗ no `cover-letter.md` (by design — pitch IS the submission) · ✗ no `stage-5-signoff.md` (replaced by `submission-day-package_2026-05-31.md` per Aeon-specific workflow) · ✓ `carry-forward-inventory.md` · ✓ `submission-day-package_2026-05-31.md` · ✓ `_archive/`.
- **Word count (essay.md):** ~300w pitch body (Version C; LOCKED).
- **Last activity on main:** `18f47a1` (Aeon essay file-org fix — cross-reference updates; HEAD of `origin/main`) — most recently touched essay folder of all nine.
- **Discipline note:** layout is non-standard by design — Aeon is the only pitch-first venue in the portfolio.

### 1.3 `atlantic-ideas-pricing-honestly/` → Atlantic Ideas (primary) / Foreign Policy (alt)

- **Essay title:** *Pricing Honestly*
- **Venue:** Atlantic Ideas (TBD; Foreign Policy alternate reframe outline available per `tools/workstream-handoffs/foreign-policy-alternate-outline_2026-05-21.md`).
- **Stage state on main (per README — STALE):** "Stage 2 audience-blind flow draft complete (2026-05-21); Stage 3 cycle in progress; Pass 3.1 PROPOSED 2026-05-23." **Actual state on main per recent commits:** Pass 3.5 RATIFIED + APPLIED 2026-05-27 (`2581277`); Stage 4 render audit RATIFIED (rigor-pass artifact on main, *_stage_4_render_audit_author_offline_v1.0.0.md*); Stage 5 surfacing **F-DE-Atlantic-1 book-architecture drift** — Option 1 REVERT RATIFIED + APPLIED 2026-05-27 (`82c6da6`). **Stage 5 sign-off rigor-pass artifact NOT YET on main.**
- **Canonical layout on main:** ✓ `README.md` (STALE; needs refresh) · ✓ `essay.md` · ✗ no `cover-letter.md` · ✗ no `stage-5-signoff.md` (per-essay mirror) · ✗ no `_archive/`.
- **Word count (essay.md body):** ~4,272w (per current essay.md; brief target band 4,200; substance-drives-length).
- **Last activity on main:** `82c6da6` (Stage 5 F-DE-Atlantic-1 REVERT RATIFIED + APPLIED 2026-05-27).
- **Discipline note:** the README badly trails the actual essay state — recommend refresh in a per-essay session as part of Stage 5 close-out.

### 1.4 `atlantic-main-chesapeake-watermen/` → The Atlantic main magazine (Wave 2 W2.1)

- **Essay title:** *What the Bay Knows About Us*
- **Venue:** The Atlantic main magazine — features (print; National desk or environmental long-form sub-editor pool).
- **Stage state:** **RATIFIED-AWAITING-SUBMIT** (Stage 5 sign-off RATIFIED 2026-05-27; Stage 4 render audit RATIFIED offline 2026-05-27 commit `b54822b`; cover letter DRAFTED 2026-05-27 — awaits author final-ratification).
- **Canonical layout on main:** ✓ `README.md` · ✓ `essay.md` · ✓ `cover-letter.md` (DRAFTED; awaits author final-ratification per README) · ✓ `stage-5-signoff.md`.
- **Word count (essay.md body):** ~6,590w (per Stage 5 sign-off; brief band 7,000w lower target; within Atlantic features editorial band 6,000–10,000w; substance-drives-length preserved).
- **Last activity on main:** `6e330e8` (canonical per-essay README.md + stage-5-signoff.md added — completed the canonical-layout discipline).
- **Discipline note:** **most rigor-thoroughly-completed essay in the portfolio** — only essay with both central Stage 5 sign-off rigor-pass artifact AND per-essay stage-5-signoff.md mirror AND **separate pre-publication review queue artifact** ([`publishing/essays/atlantic-main-chesapeake-watermen/rigor/pre-pub-review-queue.md`](../../publishing/essays/atlantic-main-chesapeake-watermen/rigor/pre-pub-review-queue.md); consolidated 2026-05-28 from `tools/rigor-passes/commons_bonds_rigor_pass_2026-05-27_ch3_atlantic_main_essay_stage5_pre_publication_review_queue_v1.0.0.md`). This is the v3.1 Stage 5 mandatory hand-off requirement met in full.

### 1.5 `berggruen-prize-2026/` → Berggruen Prize 2026

- **Essay title:** (placeholder; renamable when working title emerges)
- **Venue:** Berggruen Prize 2026 (AI-free physically-isolated parallel track).
- **Stage state:** **Seed materials (offline AI-free drafting per prize rules)**; first-draft work in progress per cascade plan v2 §4; soft target 2026-08-05; hard deadline 2026-08-17.
- **Canonical layout on main:** ✓ `README.md` · ✓ `_archive/` (seed materials) · ✗ no `essay.md` on main (by design — AI-free isolated workflow) · ✗ no `cover-letter.md` · ✗ no `stage-5-signoff.md`.
- **Word count:** N/A on main (essay drafted offline AI-free).
- **Last activity on main:** `52fde31` (pipeline reorg).
- **Discipline note:** canonical layout incomplete *by design* — the AI-collaborative pipeline does not touch Berggruen essay prose. No rigor-pass artifacts on main and no rigor-pass cadence applies.

### 1.6 `boston-review-accountability-gap/` → Boston Review

- **Essay title:** *The Accountability Gap*
- **Venue:** Boston Review (Essays & Book Reviews stream; Submittable portal).
- **Stage state:** **RATIFIED-AWAITING-SUBMIT** (Stage 5 sign-off RATIFIED 2026-05-23; cover letter RATIFIED 2026-05-24).
- **Canonical layout on main:** ✓ `README.md` · ✓ `essay.md` · ✓ `cover-letter.md` · ✓ `stage-5-signoff.md`.
- **Word count (essay.md body):** ~4,853w (per Stage 5 sign-off).
- **Last activity on main:** `52fde31` (Publishing-pipeline reorg Session 2 APPLIED).
- **Discipline note:** per cascade plan v2 §2, submission target was **Mon May 25** — TODAY is **2026-05-27** and the essay state on main is unchanged from RATIFIED-AWAITING-SUBMIT. Either author has already submitted offline (status tag should flip to `_SUBMITTED-<date>` directory rename per `publishing/essays/README.md` convention) OR submission slipped 2+ days — flag for author awareness.

### 1.7 `foreign-affairs-existence-proof/` → Foreign Affairs (Wave 2 W2.3) ⚠️

- **Essay title:** *The Existence Proof* (per feature-branch README) — essay title in feature-branch essay.md frontmatter.
- **Venue:** Foreign Affairs (target; Wave 2 Candidate C per cascade plan v2 §3).
- **Stage state on main:** Per `stage-5-signoff.md` (on main, commit `33da821`) — **RATIFIED READY-TO-SUBMIT 2026-05-27**. But **only `stage-5-signoff.md` is on main**: ✗ no `README.md` · ✗ no `essay.md` · ✗ no `cover-letter.md`.
- **Stage state on feature branch `claude/ch4-fa-pass3-1-factcheck-260527-c7af4e`:** essay.md (6,065w body, 5,938w body per brief band 5,500–6,500) · README.md · cover-letter.md · stage-5-signoff.md — all four files present.
- **Word count (essay.md on feature branch):** ~6,065w body.
- **Last activity on main:** `33da821` (Ch 4 → Foreign Affairs Stage 5 pre-submission sign-off — RATIFIED READY-TO-SUBMIT 2026-05-27) — internal-scaffolding sign-off committed alone; end-user-facing prose remains on feature branch.
- **Last activity on feature branch:** `713c02a` (mirrors `33da821`) — full pipeline through Stage 5 completed 2026-05-27 in 16 commits on the feature branch.
- **Discipline note:** ⚠️ **MAJOR canonical-layout gap on main.** This is the most consequential feature-branch-only situation in the portfolio. See §2 for full reconciliation detail.

### 1.8 `noema-commons-bonds/` → Noema

- **Essay title:** *Commons Bonds*
- **Venue:** Noema.
- **Stage state:** **RATIFIED-AWAITING-SUBMIT** (Stage 5 sign-off RATIFIED 2026-05-24; submission portal upload gated only on §9 author-action submission-window items).
- **Canonical layout on main:** ✓ `README.md` · ✓ `essay.md` · ✓ `cover-letter.md` · ✓ `stage-5-signoff.md` · ✓ `_archive/`.
- **Word count (essay.md body):** ~3,800–4,000w (151 lines per Stage 5 sign-off; within Noema 2,500–4,000 band).
- **Last activity on main:** `cf56858` (scaffolding cleanup — first 15-20 lines of essay; "Essay prose has been untouched.") — recent, post-`52fde31` reorg.
- **Discipline note:** per cascade plan v2 §2, submission target was **Wed May 27 / Thu May 28** — TODAY is **2026-05-27**, hitting the front of the submission window. Submission gate is at author Stage 4 portal-preview rendering + portal upload action.

### 1.9 `nyrb-multi-book-review/` → NYRB (Wave 2 — new entry)

- **Essay title:** *The Architecture and Its Residue* (review of Pistor + Mazzucato + Christophers + Susskind)
- **Venue:** The New York Review of Books (Wave 2 multi-book review-essay; new addition not in cascade plan v2 §3 — cascade plan slotted Ch 8 → NYRB at PM-recommended DEFER; this multi-book review-essay surfaces as a different NYRB shot).
- **Stage state:** Central rigor-pass artifacts on main show **Stage 5 sign-off RATIFIED 2026-05-27** (rigor-pass `publishing/essays/nyrb-multi-book-review/rigor/stage-5-signoff.md` on main); Stage 4 render audit on main; cover letter DRAFTED + RATIFIED 2026-05-27 (commit `52ad24d`).
- **Canonical layout on main:** ✗ **no `README.md`** · ✓ `essay.md` (8,301w; longest in portfolio) · ✓ `cover-letter.md` (618w) · ✗ **no `stage-5-signoff.md`** (per-essay mirror missing — central rigor-pass artifact present at `tools/rigor-passes/`).
- **Word count (essay.md):** ~8,301w (review-essay scale — NYRB review-essay band is ~5,000–10,000w; sits within band).
- **Last activity on main:** `52ad24d` (cover letter DRAFTED + RATIFIED 2026-05-27).
- **Discipline note:** ⚠️ The entire 5-pass cascade + Stage 4 + Stage 5 sign-off was driven through the central rigor-pass artifacts directly on main without producing the per-essay folder's `README.md` or `stage-5-signoff.md` mirror. Canonical layout per `publishing/essays/README.md` is not yet complete. The end-user-facing prose IS on main; the *internal scaffolding* (per-essay README + per-essay stage-5-signoff.md mirror) is missing.

---

## §2. Feature-branch-only check

Branches with commits ahead of `origin/main` (per `git rev-list --count origin/main..<branch>`):

| Branch | Commits ahead | End-user-facing-prose? | Ratified? | Action |
|---|---|---|---|---|
| `claude/ch4-fa-pass3-1-factcheck-260527-c7af4e` | **16** | **YES** (essay.md + cover-letter.md content edits) + internal-scaffolding (README + paste-texts) | **YES — RATIFIED READY-TO-SUBMIT 2026-05-27 per stage-5-signoff.md on main** | See §2.1 below |
| `claude/pm-commons-bonds-handoff-jBIGy` | 2 | Unknown (likely PM dashboard scaffolding) | Unknown | Out of scope (PM workstream; not an essay) |
| `claude/quirky-ardinghelli-f59e63` | 1 | Unknown | Unknown | Out of scope (not an essay branch) |
| `claude/atlantic-ideas-essay-pass-3-1-phase-c-application-a9e5554f-302` | 1 | YES (older Pass 3.1 work) | Superseded — Pass 3.5 RATIFIED + APPLIED on main supersedes; branch is **stale** | See §2.2 below |

All other essay-prefixed feature branches show **0 commits ahead of main** — already merged.

### 2.1 Foreign Affairs feature branch — `claude/ch4-fa-pass3-1-factcheck-260527-c7af4e`

**Full commit list ahead of main (newest to oldest):**

1. `713c02a` Stage 5 pre-submission sign-off — RATIFIED READY-TO-SUBMIT 2026-05-27 *(mirrors `33da821` on main)*
2. `1a44f03` Cover letter — DRAFTED 2026-05-27 *(end-user-facing prose)*
3. `f3842c6` Stage 5 sign-off + cover-letter draft kickoff paste-text — STAGED 2026-05-27 *(internal scaffolding)*
4. `ad18aa5` Stage 4 (render + character-integrity audit) — RATIFIED CLEAR 2026-05-27 (author-offline-execution) *(rigor-pass artifact is on main)*
5. `ce10e26` Pass 3.5 (developmental-edit) — RATIFIED HOLD 2026-05-27 *(no essay edits; held)*
6. `cc76138` Pass 3.5 developmental-edit kickoff paste-text — STAGED 2026-05-27
7. `ac9bf02` Pass 3.4 (adversarial robustness) — RATIFIED ROBUST 2026-05-27 *(no essay edits)*
8. `3cabd6b` Pass 3.4 adversarial robustness kickoff paste-text — STAGED 2026-05-27
9. `e246067` Pass 3.3 (audience-load acceptance) — RATIFIED PASS 2026-05-27 *(no essay edits)*
10. `c83d742` Pass 3.3 audience-load acceptance kickoff paste-text — STAGED 2026-05-27
11. `797582c` Pass 3.2 (voice-polish) — RATIFIED + APPLIED 2026-05-27 *(end-user-facing essay.md edits)*
12. `8d80736` Pass 3.2 spot-fixes — RATIFIED + APPLIED 2026-05-27 *(end-user-facing essay.md edits)*
13. `3fadbe1` Pass 3.2 voice-polish kickoff paste-text — STAGED 2026-05-27
14. `bdf8726` Pass 3.1 (fact-check) — RATIFIED + APPLIED 2026-05-27 *(end-user-facing essay.md edits)*
15. `c4bd4d6` Pass 3.1 spot-fixes — RATIFIED + APPLIED 2026-05-27 *(end-user-facing essay.md edits)*
16. `50c37b7` Stage 2 audience-blind draft — PROPOSED 2026-05-27 *(end-user-facing essay.md baseline)*

**Files left on feature branch, NOT on main:**
- `publishing/essays/foreign-affairs-existence-proof/essay.md` (6,065w body) — **end-user-facing prose**
- `publishing/essays/foreign-affairs-existence-proof/cover-letter.md` — **end-user-facing prose**
- `publishing/essays/foreign-affairs-existence-proof/README.md` — internal scaffolding
- Various kickoff paste-texts under `tools/workstream-handoffs/` — internal scaffolding (rigor-pass artifacts themselves are already on main)

**Ratification status:** **stage-5-signoff.md on main verdict reads RATIFIED 2026-05-27 — READY-TO-SUBMIT.** All five Stage 3 passes ratified per artifact frontmatter; Stage 4 RATIFIED CLEAR (author-offline-execution); cover letter DRAFTED.

**Active-push-on-chunk-completion lapse:** Per CLAUDE.md "Active-push expectation (from 2026-05-10) — push them promptly — don't accumulate ratified work on the feature branch." The 16 commits date-stamped 2026-05-27 represent a single-day full-cascade execution; the *stage-5-signoff.md* alone made it across to main while the essay + cover letter + README — all of which are ratified for submission — remained on the feature branch. End-user-facing prose requires explicit author authorization to merge per CLAUDE.md; per Stage 5 sign-off RATIFIED verdict, the author has effectively ratified the content. **PM recommendation:** author authorizes merge of essay.md + cover-letter.md + README.md to main in a per-essay merge session (FA branch rebase against `origin/main` → fast-forward).

### 2.2 Atlantic Ideas feature branch — `claude/atlantic-ideas-essay-pass-3-1-phase-c-application-a9e5554f-302`

**Single commit ahead of main:** `57b62ec Atlantic Ideas essay Pass 3.1 Phase C — spot-fixes APPLIED + brief v1.1.4 + bibliography Marx entry`.

**Status:** **STALE.** Pass 3.1 work has been superseded — Pass 3.2 + 3.3 + 3.4 + 3.5 all subsequently RATIFIED + APPLIED on main (commits `0e8810d`, `2581277`, `82c6da6`); Stage 4 render audit RATIFIED. The single feature-branch commit predates and is subsumed by the on-main cascade.

**PM recommendation:** branch can be archived / pruned at author discretion; no merge action needed (content was either re-applied in main-line commits or superseded by later passes).

---

## §3. Rigor-pass artifact coverage check

For each essay with Stage 5 status, the canonical artifact chain is verified at `tools/rigor-passes/` on `origin/main`:

| Essay | Stage 1 brief | Pass 3.1 | Pass 3.2 | Pass 3.3 | Pass 3.4 | Pass 3.5 | Stage 4 render | Stage 5 sign-off (central) | Per-essay `stage-5-signoff.md` | Pre-pub review queue |
|---|---|---|---|---|---|---|---|---|---|---|
| 100-barrel | ✓ + Q1 go/no-go | ✓ | ✓ | ✓ (light) | ✓ (light) | ✓ | (offline; no central artifact) | ✗ no central | ✓ | (not separately filed) |
| aeon-mask-of-abundance | ✓ + title cands | ✓ | ✓ | ✓ (bundled 3.3+3.4) | (bundled) | N/A (297w pitch) | (offline) | (replaced by `submission-day-package`) | ✗ (n/a — pitch model) | (n/a) |
| atlantic-ideas-pricing-honestly | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✗ **no central Stage 5 sign-off rigor-pass artifact YET** | ✗ no per-essay mirror | (not yet) |
| atlantic-main-chesapeake-watermen | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | (offline; ratified per README b54822b) | ✓ | ✓ | ✓ **(separate central artifact)** |
| boston-review-accountability-gap | ✓ + Stage 0 | ✓ | ✓ | ✓ full + light re-fire | (opt-out per Pass 3.3 C-12 ≥ NEUTRAL) | ✓ | (offline) | ✗ no central | ✓ | (not separately filed) |
| foreign-affairs-existence-proof | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✗ **no central Stage 5 sign-off rigor-pass artifact** (per-essay mirror IS on main) | ✓ | (not separately filed) |
| noema-commons-bonds | ✓ | ✓ | ✓ | ✓ + light re-fire | ✓ | ✓ | (offline) | ✗ no central | ✓ | (not separately filed) |
| nyrb-multi-book-review | ✓ + Stage 0 | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✗ **no per-essay mirror** | (not separately filed) |
| berggruen-prize-2026 | — | — | — | — | — | — | — | — | — | (n/a — AI-free track) |

**Cross-essay coherence observations:**

1. **Two emerging Stage-5-artifact conventions in the portfolio:**
   - **Older (per-essay-only):** 100-barrel, boston-review, noema — per-essay `stage-5-signoff.md` mirror only; **no central** `tools/rigor-passes/..._stage_5_sign_off_v1.0.0.md` artifact.
   - **Newer (dual):** atlantic-main + foreign-affairs — both per-essay mirror AND central rigor-pass artifact. atlantic-main also produced separate central pre-publication review queue artifact.
   - **Inverted (central-only):** nyrb-multi-book-review — central artifact on main but per-essay mirror missing.
   - **In-progress:** atlantic-ideas — Pass 3.5 + Stage 4 done; Stage 5 not yet filed at either layer.

2. **Pre-publication review queue artifact** is mandatory per v3.1 Amendment B Stage 5 doctrine (`tools/memory/feedback_audience_aware_drafting_discipline.md` §"Pre-publication review queue"). **Only atlantic-main has the separate filed artifact;** for the other Stage-5-ratified essays the pre-pub review queue content is either embedded inside the stage-5-signoff or not surfaced. Cross-essay coherence flag: the pre-pub review queue is the publisher-facing hand-off artifact; an essay can submit without it, but the editor will not have the "what has been internally verified vs. what has not been externally verified" disclosure that v3.1 doctrine requires. Recommend: pre-pub review queue extraction sweep across 100-barrel + boston-review + foreign-affairs + noema + nyrb as a portfolio-coherence catch-up.

3. **Aeon Stage 5 anchor:** Aeon's pitch-first workflow does not generate a Stage 5 sign-off in the magazine-essay shape; the equivalent artifact is `submission-day-package_2026-05-31.md`. Audit-passes-by-design. No catch-up needed.

---

## §4. Pre-submission action items inventory (per Stage-5-RATIFIED essay)

Per each RATIFIED-AWAITING-SUBMIT essay's README + stage-5-signoff: the pending pre-submission action items the author holds.

### 4.1 100-barrel → Phenomenal World

Per `100-barrel/README.md` + sign-off §9 (Submission checklist; abbreviated; full list in sign-off):
- ☐ Stage 4 render audit (author offline; pre-submission)
- ☐ Submit via PW pitch + essay (e-mail to *[email protected]* per cover-letter discipline)
- ☐ Update Soft Clips table (`publishing/book-proposal/03_author-platform.md`) post-submission

### 4.2 boston-review-accountability-gap → Boston Review

Per `boston-review-accountability-gap/README.md` Submission checklist §:
- ☐ Stage 4 render audit (Submittable preview — author offline)
- ☐ Submit via `bostonreview.submittable.com/submit` (Essays & Book Reviews stream)
- ☐ Update Soft Clips table post-submission
- **Note:** cascade plan v2 submission target was **Mon May 25**; TODAY is 2026-05-27 — flag for author whether submission has already happened (folder rename to `_SUBMITTED-<date>` per status-tag convention).

### 4.3 noema-commons-bonds → Noema

Per `noema-commons-bonds/README.md` submission-window author actions:
- ☐ Stage 4 render audit (Noema portal preview — author offline)
- ☐ Norway fund value re-verification (~$1.9T as of essay drafting 2026-05-10; check at submission-window)
- ☐ Phat consent-status check (anonymization ratified 2026-05-20 as working-draft baseline)
- ☐ Biggie courtesy-notification (deceased 30+ years; good-faith family identification)
- ☐ Allison Colden + Chris Moore courtesy-notification (CBF communications coordinator; citation-accuracy verification only)
- ☐ AI-disclosure Noema-guidelines re-verification at submission-window
- ☐ Medium bio current-status re-verification
- ☐ Submit via Noema submission portal (rolling)
- **Note:** cascade plan v2 submission target was **Wed May 27 / Thu May 28** — TODAY is 2026-05-27, front of window.

### 4.4 atlantic-main-chesapeake-watermen → The Atlantic main magazine

Per Wave 2 W2.1 cascade + Stage 5 sign-off + per-essay README:
- ☐ Author final-ratification of cover-letter DRAFTED 2026-05-27 (~709w) — only blocking pre-submission item per README
- ☐ Sub-editor identification (Atlantic features pool — National desk OR environmental long-form)
- ☐ Pre-pub citation-verification packet hand-off (artifact ready: central pre-pub review queue rigor-pass)
- ☐ Courtesy-notify discipline:
  - Biggie surviving family (deceased oysterman; courtesy-notify if reachable; per named-subject discipline)
  - Anonymized waterman portrait verification (anonymization carries from Phat ratification 2026-05-20)
  - Public-record-quoted CBF + scientist + waterman subjects: courtesy-notification (per `feedback_named_subject_consent.md` public-record exception)
- ☐ Submission target window per cascade plan v2: **Oct – Dec 2026** (Wave 2 cadence; not part of May/June sprint)

### 4.5 foreign-affairs-existence-proof → Foreign Affairs (Wave 2 W2.3) ⚠️

**Pre-submission blockers:**
- ☐ **Author authorization to merge feature-branch essay.md + cover-letter.md + README.md to `origin/main`** (per CLAUDE.md merge-to-main policy for end-user-facing prose — see §2.1 + §8.B)
- ☐ Sub-editor identification (FA features editorial pool)
- ☐ Pre-pub citation-verification packet hand-off (artifact extraction needed — see §3 cross-essay coherence)
- ☐ Author final-ratification of cover-letter DRAFTED on feature branch
- ☐ Submission target window per cascade plan v2: **Q4 2026 / Q1 2027 (Nov – Feb)** — not in the May–Jun sprint window.

### 4.6 nyrb-multi-book-review → NYRB

**Pre-submission blockers:**
- ☐ **Per-essay README.md creation** (canonical layout completion) — internal scaffolding
- ☐ **Per-essay `stage-5-signoff.md` mirror creation** (canonical layout completion) — internal scaffolding; mirror central rigor-pass artifact
- ☐ Sub-editor identification (NYRB review-essays editorial pool)
- ☐ Pre-pub citation-verification packet hand-off (artifact extraction needed)
- ☐ Submission target: cascade plan v2 §3 originally slotted Ch 8 → NYRB at Path D-α DEFER; **this multi-book review-essay is a different NYRB shot not in cascade plan v2 §3** — flag for author whether to fold into Wave 2 or treat as opportunistic NYRB cascade addition.

---

## §5. Cascade-plan position check (cross-reference against `cascade-plan_v2_2026-05-24.md` + `june-2026-submission-schedule.md`)

Per cascade plan v2 §2 (Wave 1 active pipeline) and June 2026 submission schedule:

| Cascade slot | Plan stage | Actual state on main 2026-05-27 | Drift? |
|---|---|---|---|
| W1.1 Aeon Pitch | Stage 3 COMPLETE; LOCKED; submit **Sat May 31 14:01 UTC** | Pitch LOCKED (Version C 297w) on main; submission-day package on main | ✓ on plan |
| W1.2 Boston Review | Stage 5 RATIFIED + cover letter RATIFIED; submit **Mon May 25** | RATIFIED-AWAITING-SUBMIT on main; **2-day slip from May 25 target** (or already submitted offline) | ⚠ Slip OR offline-submit untracked |
| W1.3 $100 Barrel → PW | Stage 5 RATIFIED + cover letter RATIFIED; submit **Tue May 26** | RATIFIED-AWAITING-SUBMIT on main; **1-day slip from May 26 target** (or already submitted offline) | ⚠ Slip OR offline-submit untracked |
| W1.4 Noema | Pass 3.5 APPLIED; Stage 5 + cover letter PROPOSED; submit **Wed May 27 / Thu May 28** | RATIFIED-AWAITING-SUBMIT on main (Stage 5 + cover letter both RATIFIED 2026-05-24, ahead of cascade plan v2's "PROPOSED" snapshot) | ✓ ahead of plan |
| W1.5 Atlantic Ideas | Pass 3.1 RATIFIED + APPLIED 2026-05-24; Pass 3.2 + 3.3 + 3.4 + 3.5 + Stage 5 pending; submit **late June / early July 2026** | Pass 3.2 + 3.3 + 3.4 + 3.5 + Stage 4 + Stage 5 F-DE-Atlantic-1 REVERT all complete on main; Stage 5 sign-off rigor-pass artifact + per-essay stage-5-signoff.md + cover-letter not yet filed | ✓✓ significantly ahead of plan |
| W2.1 Ch 3 → Atlantic main | Wave 2 candidate; Stage 1 brief fire ~Jun 29 – Jul 5 | **Wave 2 W2.1 has fully completed through Stage 5 RATIFIED 2026-05-27** — entire Stage 1 → Stage 5 cycle ran on the day **2026-05-27** | ✓✓✓ **massively** ahead of plan (Wave 2 W2.1 originally planned to fire Jun–Aug; ran completely in one day five weeks early) |
| W2.2 Ch 2 → Harper's | Wave 2 candidate; Stage 1 brief fire ~Jun 22 – Jul 28 | **Parallel session in flight 2026-05-27**: Stage 1 brief RATIFIED 2026-05-26 + Pass 3.1 + 3.2 + 3.3 + **Pass 3.4 RATIFIED ROBUST 2026-05-27** (rigor-pass artifacts on main; commits `a9fe7be` + `7c16abc` landed during this audit session); Pass 3.5 kickoff STAGED. **No `publishing/essays/harpers-*` folder on main yet** — running through rigor-pass artifacts only (same pattern as NYRB intra-session). | ✓✓✓ **massively** ahead of plan (Stage 1 brief planned ~Jun 22–28; fired May 26; full Stage 3.1–3.4 cascade in two days) |
| W2.3 Ch 4 → Foreign Affairs | Wave 2 candidate CONDITIONAL; Stage 1 brief fire ~Jul 13 – Jul 19 (gated on Ch 4 Pass 2 + apparatus-stability) | **Wave 2 W2.3 has fully completed Stage 1 → Stage 5 RATIFIED 2026-05-27 on feature branch (essay/cover-letter not yet on main)** | ✓✓✓ **massively** ahead of plan (Stage 1 brief planned mid-July; ran complete one-day cascade May 27, seven weeks early) |
| W2.4 Ch 8 → NYRB | Wave 2 candidate PM-recommend DEFER (Path D-α) or rescope D-β | **NYRB multi-book review-essay (different shot) Stage 5 RATIFIED 2026-05-27** — not the Ch 8 NYRB cascade slot; this is a four-book review-essay using Pistor + Mazzucato + Christophers + Susskind | ⚠ off-plan slot fired — NYRB shot taken but via different framing than cascade plan v2 §3 W2.4 contemplates |
| C Berggruen | first-draft work in progress; submit by Aug 5 | Seed materials only on main (AI-free track) | ✓ on plan |
| Op-eds | Pipeline-ready; opportunistic on news-peg | (out of scope this audit) | — |

**Net cascade-plan-position summary:**
- Wave 1 essays: **0/5 ratified-not-yet-submitted** are firmly past the cascade plan v2 submission target — Boston Review + $100 Barrel are 1–2 days slipped (or possibly submitted offline; tracking-discipline question); Noema + Aeon are on or ahead of plan; Atlantic Ideas is ahead of plan but Stage 5 close-out artifacts are unfiled.
- Wave 2 essays: **Three of four Wave 2 slots were driven through full or near-full cascade in one or two days (2026-05-26 → 2026-05-27)** — W2.1 (Atlantic Main; Stage 5 RATIFIED), W2.2 (Ch 2 → Harper's; Pass 3.4 RATIFIED ROBUST 2026-05-27 — parallel-session in flight; landed *during* this audit), and W2.3 (Foreign Affairs; Stage 5 RATIFIED on feature branch). This is wildly ahead of cascade plan v2's "Wave 2 Stage 1 briefs fire ~Jun 22 – Jul 19" timing. **Off-plan velocity**, not off-plan content — all three executing clean.
- A **fifth NYRB shot** (multi-book review-essay) executed start-to-finish 2026-05-27 outside the cascade plan v2 §3 frame. PM-relevant flag for cascade plan v3 refresh.
- **Reconciliation note (added during this session's pre-push reconciliation pattern):** while this audit was being written, the Ch 2 → Harper's parallel session landed Pass 3.4 RATIFIED ROBUST commits (`a9fe7be` + `7c16abc`) on `origin/main`. §1 inventory shows 9 essay folders + the Harper's-in-flight workstream running through rigor-pass artifacts at `tools/rigor-passes/ch2_harpers_*` only (no `publishing/essays/harpers-*` folder yet) — same pattern as NYRB intra-session. **The portfolio is effectively a 10-essay portfolio** (9 with folders on main + 1 Harper's in flight at near-Stage-5). Cascade plan v3 refresh recommendation (§8.C.2) covers this.

**Cumulative apparatus-portfolio reveal monitoring** (per cascade plan v2 §8 item 7): Wave 1 alone ~40–45%; Wave 1 + Wave 2 (PM-recommended W2.1 + W2.2 + W2.3) ~48–55%. With NYRB multi-book review-essay added (which by README/title is observational-distance / negative-space construction; engages all four comp authors at chapter length per cover letter §3) the cumulative may push to ~55–60% effective. **Recommend:** cumulative apparatus-portfolio reveal re-measurement before next Wave 2 fires (W2.2 Ch 2 → Harper's).

---

## §6. Cross-essay portfolio coherence check

Per Stage 1 brief §9.3 / Pass 3.3 §4 patterns + named-subject discipline + rights register §:

### 6.1 Norway content allocation
- **Foreign Affairs (W2.3)** — primary Norway long-form treatment (GPFG architecture, fiscal rule, 3% spending cap, $2T AUM); confirmed per Stage 1 brief §7.5 + essay §IV/§V on feature branch.
- **Op-ed `publishing/op-eds/norway-sovereign-wealth/`** — short-form news-peg-fire op-ed.
- **Boston Review (W1.2)** — Norway two-event diagnostic (per Pass 3.1 fact-check §5 spot-fix; supportive register, not load-bearing).
- **100 Barrel (W1.3)** — Norway fiscal-rule history (3% revised from 4%; supporting cluster).
- **NYRB multi-book review-essay** — Norway as "institutional templates" in cover letter §3; presumed light treatment given review-essay frame.
- **Atlantic Ideas (W1.5)** — GPFG cited in §"What works already" (~$2T AUM, 3% fiscal cap; 1969 Ekofisk find; renamed 2006).
- **Coherence verdict:** ✓ Norway content surfaces at varying depth in **5 essays + 1 op-ed**. Cascade plan v2 §2 + rights register §"one source-chapter → one venue → one frame" — Norway is permitted multi-cite at supportive register; FA is the single-frame allocation. **Recommend cross-essay verification** that the FA Norway treatment does not verbatim/near-verbatim with the Atlantic Ideas Norway paragraph (~340w in Atlantic Ideas §"What works already"). FA essay rigor-pass artifacts on main include Path B audit (3 brief-authorized verbatim preservations from Ch 4 source); but cross-essay verbatim audit may not have fired against Atlantic Ideas essay state. Light cross-check recommended.

### 6.2 McDowell long-arc allocation
- **Ch 8 → NYRB cascade slot (W2.4)** — PM-recommended Path D-α DEFER per cascade plan v2.
- **Op-ed `publishing/op-eds/mcdowell-county-true-cost/`** — news-peg short-form.
- **Atlantic Ideas (W1.5)** — McDowell ton-of-coal opener (one paragraph, 1960 sale price + true cost $520–600/ton).
- **The Atlantic main (W2.1) §VIII** — explicit McDowell County watershed-of-coal parallel close (per README essay-architecture §VIII).
- **NYRB multi-book review-essay** — McDowell not visible in cover letter §; presumably absent (review-essay frame stays on four books' material).
- **Coherence verdict:** ✓ McDowell long-arc currently allocated to op-ed + Atlantic Ideas + Atlantic main §VIII parallel. Ch 8 → NYRB DEFER per cascade plan; consistent. **Caution:** Atlantic Ideas + Atlantic Main both touch McDowell; given both are Atlantic-imprint targets (Ideas vertical vs main magazine), if both submit and one accepts the other should be withdrawn. Cascade plan v2 §2 W1.5 + cascade plan v2 §3 W2.1 do not explicitly state this dual-Atlantic-imprint risk — flag for cascade plan v3.

### 6.3 Named-subject discipline consistency
- **Phat** — anonymized per ratification 2026-05-20 (Noema essay README §; Atlantic main essay README §VII confirms anonymized waterman portrait). **Cross-essay consistency:** ✓ both essays carry Phat anonymization.
- **Biggie** — named at Noema essay line 135 (oysterman; deceased 30+ years; courtesy-notify-surviving-family); Atlantic main §III scene-anchor (oak-build; six-pack-of-Coca-Cola; wrist-motion economy; courtesy-notify-surviving-family pre-submission per README). **Cross-essay consistency:** ✓ Biggie named in both with consistent discipline; courtesy-notify gate applies to both essays' submission timing.
- **Allison Colden** — named at Noema line 131 (public-record exception; courtesy-notify); Atlantic main §IV named scientific voice. **Cross-essay consistency:** ✓.
- **Chris Moore** — named at Noema line 131 (CBF Virginia); Atlantic main not visible in README §IV listing (Goldsborough + Hudgins listed); **possibly inconsistent — verify in Atlantic main essay body.**
- **Darity (Sandy)** — referenced in Noema §V and BR pre-pub citation discipline; possibly referenced in FA (cascade plan v2 §8 item 5).
- **Verdict:** named-subject discipline appears consistent for Phat + Biggie + Colden. Moore allocation needs spot-check. **No portfolio-wide named-subject inconsistency surfaced.**

### 6.4 Apparatus-reveal differentiation across venues
Per cascade plan v2 §8 item 7 + Stage 1 brief §10 (cumulative apparatus-reveal cap ≤22% per essay for trade-press; tighter caps for Atlantic features at <10%):
- **Atlantic main (W2.1):** cumulative-portfolio effective-reveal at <10% sentence-level per Pass 3.3 §; **well below cap.**
- **Foreign Affairs (W2.3):** cumulative effective reveal target ≤22%; per feature-branch essay.md frontmatter, apparatus-check passes ("named-OK terms surface at concept-level only").
- **Atlantic Ideas (W1.5):** mechanism vocabulary at policy-explanation register; apparatus-density not surfaced in current README — verify at Stage 5 sign-off close-out.
- **Boston Review (W1.2):** institutional-measurement vocabulary at center-right policy reader pressure-test level; Stage 5 sign-off RATIFIED.
- **Noema (W1.4):** Path B Chris-as-vignette + cluster γ register; per Stage 5 sign-off + brief §7 CTG repairs.
- **100 Barrel (W1.3):** explicit Condition-1-disarming moves register per `feedback_audience_aware_drafting_discipline.md` $100 Barrel anchor; Stage 5 RATIFIED.
- **NYRB multi-book review-essay:** "observational-distance register rather than manifesto" per cover letter §3; **review-essay frame allows higher comp-cluster-engagement-depth without apparatus reveal.**
- **Verdict:** ✓ apparatus-reveal differentiation appears intact across the portfolio. Stage 5 sign-off-time monitor the cumulative reveal across all-soon-to-submit pieces (per cascade plan v2 §8 item 7).

---

## §7. Status summary table

| Essay | Venue | Stage | On main? | Feature-branch commits? | Pre-submission action items pending? |
|---|---|---|---|---|---|
| 100-barrel | Phenomenal World | **RATIFIED-AWAITING-SUBMIT** (Stage 5 RATIFIED 2026-05-24) | ✓ full layout | 0 ahead | Stage 4 author offline + submit |
| aeon-mask-of-abundance | Aeon (pitch-first) | **Pitch-LOCKED**; submit Sat May 31 14:01 UTC | ✓ pitch-model layout | 0 ahead | Pre-submission verify (May 29) + submit |
| atlantic-ideas-pricing-honestly | Atlantic Ideas / FP alt | **RATIFIED PASS / READY-TO-SUBMIT 2026-05-27** (per §0.1 correction — Stage 5 sign-off at `publishing/essays/atlantic-ideas-pricing-honestly/rigor/stage-5-signoff.md` + pre-pub queue at `tools/pre-submission-reviews/atlantic_ideas_pre_pub_review_queue_v1.0.0.md`; Convention C filing) | ✓ at Convention-C level (essay.md on main; sign-off + pre-pub queue at central paths; README stale + no per-essay mirror — both bookkeeping) | 0 ahead | **Cover-letter / pitch drafting** (Stage 5 §8 next-step) + README refresh + optional per-essay mirror; submission window late-Jun / early-Jul 2026 |
| atlantic-main-chesapeake-watermen | The Atlantic main | **RATIFIED-AWAITING-SUBMIT** (Stage 5 RATIFIED 2026-05-27) | ✓ full layout (with central pre-pub review queue) | 0 ahead | Cover-letter author final-ratification + sub-editor + courtesy-notify; submission window Oct–Dec 2026 |
| berggruen-prize-2026 | Berggruen Prize | **Seed-materials (AI-free track)** | ✓ by-design partial layout | 0 ahead (n/a) | (offline workflow; not Claude scope) |
| boston-review-accountability-gap | Boston Review | **RATIFIED-AWAITING-SUBMIT** (Stage 5 RATIFIED 2026-05-23); cascade-plan submit target May 25 | ✓ full layout | 0 ahead | Stage 4 author offline + submit (slip-or-submitted-offline?) |
| foreign-affairs-existence-proof | Foreign Affairs | **RATIFIED READY-TO-SUBMIT** per stage-5-signoff.md (only file on main); essay+README+cover-letter NOT on main | partial (only stage-5-signoff.md) | **16 ahead on `claude/ch4-fa-pass3-1-factcheck-260527-c7af4e`** (ratified essay.md + cover-letter.md + README.md) | ⚠ **Author authorize merge to main**; cover-letter author final-ratification; submission window Q4 2026/Q1 2027 |
| noema-commons-bonds | Noema | **RATIFIED-AWAITING-SUBMIT** (Stage 5 RATIFIED 2026-05-24); cascade-plan submit window May 27/28 | ✓ full layout | 0 ahead | 8 submission-window checks per README §; submit |
| nyrb-multi-book-review | NYRB | Stage 5 RATIFIED 2026-05-27 (central artifact); per-essay README + stage-5-signoff.md mirror MISSING | partial (essay + cover-letter; no README; no stage-5-signoff.md) | 0 ahead | ⚠ Create per-essay README + stage-5-signoff.md mirror; sub-editor; pre-pub queue; cascade-plan slot decision |

---

## §8. Recommendations

### A. Auto-merge already complete (no further action)
The vast majority of internal-scaffolding work has already auto-merged to `origin/main` per CLAUDE.md merge-to-main policy. No backlog to clear here.

### B. End-user-facing prose awaiting author authorization to merge

**B.1 (HIGHEST PRIORITY) — Foreign Affairs feature branch.** Author authorizes merge of `claude/ch4-fa-pass3-1-factcheck-260527-c7af4e` to `origin/main`. The 16-commit cascade is fully RATIFIED per stage-5-signoff.md (already on main); essay.md (6,065w) + cover-letter.md + README.md are end-user-facing prose and need explicit author OK. Recommended sequence:
- Author session opens feature branch worktree (or hops into existing FA worktree)
- `git fetch origin main && git rebase origin/main` (likely clean — minimal recent main-line touches to FA folder)
- `git push origin HEAD:main`
- Verify all four canonical files now match on main + feature branch
- Folder slug renames per status-tag convention deferred until actual submission

**B.2 — Atlantic Ideas cover-letter / pitch drafting session.** *(Corrected per §0.1 audit-correction 2026-05-27 post-resume.)* Atlantic Ideas Stage 5 sign-off + pre-pub review queue are **already filed** (Convention C: `publishing/essays/atlantic-ideas-pricing-honestly/rigor/stage-5-signoff.md` + `tools/pre-submission-reviews/atlantic_ideas_pre_pub_review_queue_v1.0.0.md`; both RATIFIED 2026-05-27). The remaining items are the **cover-letter / pitch drafting** (per Atlantic Ideas brief §11 — short cover note, tighter-than-essay register) + (optional bookkeeping) README refresh at `publishing/essays/atlantic-ideas-pricing-honestly/README.md` + (optional bookkeeping) per-essay `stage-5-signoff.md` mirror creation. Cover letter is end-user-facing prose; needs author session. Submission window per cascade plan v2 is late-June / early-July, so this is not on the May–Jun sprint.

### C. Canonical-layout completion gaps

**C.1 — NYRB per-essay folder canonical-layout completion.** Create `publishing/essays/nyrb-multi-book-review/README.md` + `publishing/essays/nyrb-multi-book-review/stage-5-signoff.md` per `publishing/essays/README.md` §"Per-essay README.md contents" spec, mirroring the atlantic-main pattern. Internal scaffolding; auto-fast-forwards to main.

**C.2 — Cascade plan v3 refresh (cascade plan v2 stale as of 2026-05-27).** Per cascade plan v2 §13 update-log + §3 Wave 2 timing: Wave 2 W2.1 (Atlantic Main) and W2.3 (Foreign Affairs) both completed full cascade on 2026-05-27 — **seven weeks ahead of cascade plan v2's Jun 22 – Jul 19 Stage 1 brief firing window.** The author's parallel-session-hop sprint velocity ratified 2026-05-24 has produced execution far exceeding plan timing. Additionally, the NYRB multi-book review-essay (Pistor + Mazzucato + Christophers + Susskind) is a new shot outside cascade plan v2 §3 W2.4's Ch 8 → NYRB slot. **PM session recommend cascade plan v3 refresh that incorporates:**
- W2.1 + W2.3 already-completed status
- NYRB multi-book review-essay as new Wave 2 slot (W2.5? or rename slot semantics)
- Cumulative apparatus-portfolio reveal re-measurement across now-7 essays + 2 op-eds
- Wave 2 W2.2 Ch 2 → Harper's still-pending status
- Cascade plan v2 §3 W2.4 Ch 8 → NYRB path decision (D-α vs D-β) — possibly affected by NYRB multi-book review-essay submission timing

### D. Tracking-discipline + status-tag sync

**D.1 — Boston Review + $100 Barrel submission-status tracking.** Cascade plan v2 §2 dates were Mon May 25 + Tue May 26. Today is 2026-05-27. Either both essays have been submitted offline (in which case folder rename `boston-review-accountability-gap_SUBMITTED-2026-05-25/` + `100-barrel_SUBMITTED-2026-05-26/` per `publishing/essays/README.md` status-tag convention is overdue) **OR** submission has slipped 1–2 days (in which case the slip is small but warrants flagging). Author confirms which.

### E. Pre-publication review queue artifact extraction sweep (low-priority backfill)

**E.1 — Pre-pub review queue artifacts for 100-barrel + boston-review + foreign-affairs + noema + nyrb.** Per v3.1 Amendment B Stage 5 doctrine, the pre-publication review queue is mandatory hand-off artifact at Stage 5 (going to publisher/agent/editor with manuscript-submission package). atlantic-main filed its as a separate rigor-pass artifact at [`publishing/essays/atlantic-main-chesapeake-watermen/rigor/pre-pub-review-queue.md`](../../publishing/essays/atlantic-main-chesapeake-watermen/rigor/pre-pub-review-queue.md) (consolidated 2026-05-28 from `tools/rigor-passes/commons_bonds_rigor_pass_2026-05-27_ch3_atlantic_main_essay_stage5_pre_publication_review_queue_v1.0.0.md`); the other five Stage-5-ratified essays embed the content inside the stage-5-signoff (per-essay or central). For cross-essay coherence + publisher hand-off discipline, recommend an extraction sweep that produces the separate pre-pub-queue artifact for each. Low priority; not blocking submission; can run after Wave 1 sprint clears.

### F. Stale-branch pruning (low-priority housekeeping)

**F.1 — `claude/atlantic-ideas-essay-pass-3-1-phase-c-application-a9e5554f-302`** stale 1-commit branch superseded by later main-line work; can be archived/deleted at author discretion.

**F.2 — Multiple older branches** (`claude/aeon-pitch-stage2-flamboyant-clarke-359516`, `claude/aeon-pitch-stage3-comparison-f38496`, `claude/boston-review-essay-pass-3-1-fact-check-clever-sinoussi-440b42` and 4 siblings, `claude/atlantic-ideas-essay-stage-2-determined-payne-8b61ec`, `claude/atlantic-ideas-essay-pensive-mendeleev-7e04b6`, `claude/noema-essay-stage3-polish-great-shirley-ba0e08`, `claude/100-barrel-essay-stage-2-fbc623`) all show 0 commits ahead of main = fully merged. Branch hygiene sweep at author discretion.

### G. Recommendations Summary (TL;DR) — priorities corrected per §0 rigor-vs-bookkeeping distinction

| # | Priority | Class | Action | Who | When |
|---|---|---|---|---|---|
| 1 | **HIGH** | bookkeeping (FA-merge gating) | Merge FA `claude/ch4-fa-pass3-1-factcheck-260527-c7af4e` to `origin/main` (end-user-facing essay.md + cover-letter.md + README.md). Stage 5 already RATIFIED READY-TO-SUBMIT — merge is the last gate before FA is submission-portal-ready. | Author authorize; per-essay session | Next session |
| 2 | MED | tracking | Confirm/track BR + $100 Barrel submission status; rename folders to `_SUBMITTED-<date>` if submitted | Author confirm | When status known |
| 3 | LOW (was MED) | bookkeeping | Atlantic Ideas Stage 5 close-out (sign-off rigor-pass + per-essay mirror + cover letter + README refresh). Rigor work already complete (Pass 3.5 + Stage 4 + F-DE-Atlantic-1 REVERT all ratified-and-applied); this is just filing the handoff artifacts. Submission window is late-June anyway. | Per-essay session | Within 1–2 wk |
| 4 | LOW (was MED) | bookkeeping | NYRB per-essay canonical-layout completion (README + stage-5-signoff.md mirror). Central Stage 5 sign-off rigor-pass artifact already on main; this is mirroring it into the per-essay folder. | Internal scaffolding session | Auto-bundle into next NYRB-touching session |
| 5 | MED | PM | Cascade plan v3 refresh (Wave 2 W2.1 + W2.2 + W2.3 essentially complete; NYRB new slot; cumulative apparatus-reveal re-measurement). High value because it shapes the next PM session's resource-allocation decisions across Berggruen / agent-queries / Ch 2 → Harper's close-out / Wave 3 surfacing. | PM session | Within 1 wk |
| 6 | LOW | bookkeeping | Pre-pub review queue extraction sweep for 100-barrel + BR + FA + Noema + NYRB. Content is embedded in stage-5-signoff; extraction produces a separately-filed publisher-handoff artifact. | Bundled session | Post-sprint |
| 7 | LOW | housekeeping | Stale-branch pruning | Branch-hygiene sweep | Author discretion |
| 8 | LATCHED | rigor (HARPERS) | **Ch 2 → Harper's** — Pass 3.5 + Stage 4 + Stage 5 imminent in parallel session. This is the only rigor-still-firing piece in the entire portfolio. **No PM action needed** — already in flight per `a9fe7be` Pass 3.5 kickoff STAGED. Per-essay folder `publishing/essays/harpers-<slug>/` to be created at canonical-layout discipline step at or after Stage 5. | Parallel session in flight | Hours |

---

## §9. STATE marker (for next-session resumption)

```
STATE: cross-essay portfolio review RATIFIED (10-essay portfolio
substantively complete except Ch 2 → Harper's, which is firing
Pass 3.5 + Stage 4 + Stage 5 imminently in parallel session; 16
feature-branch-only commits flagged on Foreign Affairs branch;
8 recommendations ranked HIGH/MED/LOW/LATCHED in §8.G per §0
rigor-vs-bookkeeping distinction); NEXT: author authorizes FA
merge (Recommendation #1; the only HIGH); author confirms BR +
$100 Barrel submission status (Recommendation #2); other items
are post-rigor bookkeeping at LOW priority. AWAITING: Ch 2 →
Harper's Stage 5 ratification (imminent; parallel session).
```

---

*End of cross-essay portfolio review 2026-05-27.*
