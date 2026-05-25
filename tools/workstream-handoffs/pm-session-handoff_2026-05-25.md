# PM Session Handoff — 2026-05-25

**Branch to create at session start:** `claude/pm-session-<harness-id>` from current `origin/main`.

**Session class:** PM dashboard + action-orchestration. Post-publishing-reorg state-recap + agent-search readiness + submission-window orchestration across 4 essays + 2 op-eds + 1 prize submission.

---

## 0. Mission of the PM session

Pick up where the publishing-pipeline reorganization left off (commit `52fde31` on `origin/main`; Session 2 RATIFIED + APPLIED 2026-05-25). All 6 essays + 2 op-eds + book-proposal + agent-pipeline now live under the new per-target-directory architecture at `publishing/essays/`, `publishing/op-eds/`, `publishing/agents/`. The reorg cleared the runway for two intersecting next-phase workstreams: (1) the June 2026 submission batch (4 essays ready to ship) and (2) the agent-search PM session (50-100 literary-agent outreaches incoming under the new `publishing/agents/<agent-slug>/` pattern).

Top-of-mind action drivers:

1. **Noema essay** — RATIFIED-AWAITING-SUBMIT (Stage 5 ratified 2026-05-24); rolling submission window (no fixed portal date); 7 submission-window author actions remaining
2. **Boston Review essay** — RATIFIED-AWAITING-SUBMIT (Stage 5 ratified 2026-05-23); cover-letter scaffolding-stripped 2026-05-24
3. **Aeon essay pitch** — Submission-day package staged for 2026-05-31 (June 1-7 portal window)
4. **$100 Barrel essay** — RATIFIED-AWAITING-SUBMIT (Stage 5 ratified 2026-05-24); Phenomenal World target
5. **Agent-search PM session** — pending fire; the new architecture is in place so per-agent directories land directly into `publishing/agents/<agent-slug>/` from day one
6. **Berggruen Prize submission** — hard deadline 2026-08-17; soft target 2026-08-05; AI-free drafting required (offline)

---

## 1. Read order

1. THIS handoff
2. [`tools/workstream-handoffs/publishing-reorg-session1-audit_2026-05-24.md`](publishing-reorg-session1-audit_2026-05-24.md) §14 ratification record (the 10 design decisions ratified for the reorg)
3. [`publishing/README.md`](../../publishing/README.md) — new architecture overview
4. [`publishing/essays/README.md`](../../publishing/essays/README.md) — per-essay package pattern
5. [`publishing/agents/README.md`](../../publishing/agents/README.md) — per-agent pattern (target: 50-100 at scale)
6. [`publishing/essays/_pipeline/cascade-plan_v2_2026-05-24.md`](../../publishing/essays/_pipeline/cascade-plan_v2_2026-05-24.md) — current cross-essay cascade
7. [`publishing/essays/_pipeline/june-2026-submission-schedule.md`](../../publishing/essays/_pipeline/june-2026-submission-schedule.md) — June batch schedule
8. [`publishing/essays/_pipeline/rights-register.md`](../../publishing/essays/_pipeline/rights-register.md) — rights / overlap verification per submission
9. [`tools/memory/feedback_named_subject_consent.md`](../memory/feedback_named_subject_consent.md) — named-subject consent discipline (Phat; Biggie; Colden + Moore)

---

## 2. Next 72 hours — TOP OF MIND

### 🔴 Submit Noema essay (rolling; can fire immediately)

All gates cleared. Remaining = author actions at submission-window:

1. **Stage 4 render audit** (Noema submission portal preview — author offline)
2. **F-FC-Noema-9 Norway fund value re-verification** (~$1.9T as of essay drafting 2026-05-10; check current at submission-window)
3. **Phat consent-status check** (anonymization ratified 2026-05-20 as working-draft baseline; verify if consent has landed since)
4. **Biggie courtesy-notification** (deceased 30+ years; good-faith family identification)
5. **Colden + Moore courtesy-notification** (CBF communications coordinator; citation-accuracy verification only — not consent gating)
6. **AI-disclosure re-verification against current Noema editorial guidelines**
7. **Submit via Noema submission portal** (rolling; no fixed portal window)

### 🔴 Submit Boston Review essay (Submittable; ~6-8 week response)

All gates cleared. Cover letter scaffolding-stripped 2026-05-24 per author principle.

1. **Stage 4 render audit** (Submittable preview)
2. **Submit via `bostonreview.submittable.com/submit`** (Essays & Book Reviews stream)
3. **Update Placements / Soft Clips table post-submission** at [`publishing/book-proposal/03_author-platform.md`](../../publishing/book-proposal/03_author-platform.md)

### 🔴 Submit Aeon pitch (June 1-7 portal window)

Submission-day package staged at [`publishing/essays/aeon-mask-of-abundance/submission-day-package_2026-05-31.md`](../../publishing/essays/aeon-mask-of-abundance/submission-day-package_2026-05-31.md). Wait for June 1-7 portal window.

### 🟡 $100 Barrel submission (Phenomenal World target)

All gates cleared. Verify Phenomenal World submission process + venue selection final before submitting.

---

## 3. Critical path bottleneck

**Author-bandwidth for submission-window actions.** The pipeline has produced 4 submission-ready essays + 1 submission-day-staged pitch + 2 op-ed drafts. Pipeline output is now author-throughput-bounded:

- Each submission requires ~30-60 min of author actions (render verification + courtesy notifications + portal upload)
- 4 submissions × 30-60 min = 2-4 hours of author bandwidth needed
- Cascade-coordination considerations are minor; rights-register confirms no overlap

**Bandwidth bottleneck means TIMING strategy matters.** See §5 below for the "should you submit more than 2 in parallel?" question that previous PM handoff (2026-05-24) recommended YES on.

---

## 4. USER ACTIONS gating submissions

Per [`publishing/essays/noema-commons-bonds/stage-5-signoff.md`](../../publishing/essays/noema-commons-bonds/stage-5-signoff.md) §9 + Stage 5 sign-off equivalents for BR + 100-Barrel:

| Action | Noema | BR | Aeon | $100B | Owner |
|---|---|---|---|---|---|
| Stage 4 render audit | TBD | TBD | TBD | TBD | Author offline |
| Submission-window fact re-verification | Norway $1.9T | — | — | — | Author |
| Phat consent-status check | TBD | — | — | — | Author |
| Biggie courtesy-notify | TBD | — | — | — | Author |
| Colden + Moore courtesy-notify | TBD | — | — | — | Author |
| AI-disclosure phrasing verification | TBD | TBD | TBD | TBD | Author |
| Bio currency check | TBD | TBD | TBD | TBD | Author |
| Portal upload | TBD | TBD | June 1-7 | TBD | Author |
| Update Placements table post-submit | TBD | TBD | TBD | TBD | Author or PM session |

---

## 5. Cross-essay coordination

Per [`publishing/essays/_pipeline/rights-register.md`](../../publishing/essays/_pipeline/rights-register.md):

- **Noema essay** ← derives from Ch 1 (cost severance / commons bond) — different chapter from BR + Aeon + $100-Barrel
- **Boston Review essay** ← derives from Ch 5 (accountability gap / reparations-economics-civic-republican)
- **Aeon pitch** ← derives from Ch 7 + Ch 8 + Ch 1 (mask of abundance / Mars / universality)
- **$100 Barrel essay** ← derives from withdrawn-Noema §III material (per cross-thread-todos #4 resolution)
- **Atlantic Ideas essay** ← derives from Ch 9 (pricing honestly; rare earths + carbon + cost-severance)
- **Berggruen Prize submission** ← AI-free; separate workflow; hard deadline 2026-08-17

**Soft-clip phrasing:** once any one essay reaches "under consideration at X" state, the cover letters for subsequent submissions update with that soft-clip per [`publishing/book-proposal/03_author-platform.md`](../../publishing/book-proposal/03_author-platform.md) discipline ("real and current submissions only, never speculative").

---

## 6. Dashboard A — Derivative essays + op-eds (2026-05-25)

### Essays (6 active packages)

| Pipeline | State | Path | Next action |
|---|---|---|---|
| Noema *Commons Bonds* | RATIFIED-AWAITING-SUBMIT | [`publishing/essays/noema-commons-bonds/`](../../publishing/essays/noema-commons-bonds/) | Submission-window author actions (7 items per §2) |
| Boston Review *The Accountability Gap* | RATIFIED-AWAITING-SUBMIT | [`publishing/essays/boston-review-accountability-gap/`](../../publishing/essays/boston-review-accountability-gap/) | Submit via Submittable (cover letter scaffolding-stripped 2026-05-24) |
| Aeon *The Mask of Abundance* | Submission-day package staged | [`publishing/essays/aeon-mask-of-abundance/`](../../publishing/essays/aeon-mask-of-abundance/) | Wait for June 1-7 portal window; package ready |
| Phenomenal World *$100 Barrel* | RATIFIED-AWAITING-SUBMIT | [`publishing/essays/100-barrel/`](../../publishing/essays/100-barrel/) | Confirm PW submission process; submit |
| Atlantic Ideas *Pricing Honestly* | Stage 3 cycle in progress | [`publishing/essays/atlantic-ideas-pricing-honestly/`](../../publishing/essays/atlantic-ideas-pricing-honestly/) | Continue Stage 3 cycle (Pass 3.1 PROPOSED 2026-05-23) |
| Berggruen Prize 2026 | Seed materials (AI-free drafting offline) | [`publishing/essays/berggruen-prize-2026/`](../../publishing/essays/berggruen-prize-2026/) | Author offline drafting; hard deadline 2026-08-17 |

### Op-eds (2 active packages)

| Pipeline | State | Path | Next action |
|---|---|---|---|
| McDowell County True Cost | Draft (news-peg activation pending) | [`publishing/op-eds/mcdowell-county-true-cost/`](../../publishing/op-eds/mcdowell-county-true-cost/) | News-peg activation watch |
| Norway Sovereign Wealth | Draft (news-peg activation pending) | [`publishing/op-eds/norway-sovereign-wealth/`](../../publishing/op-eds/norway-sovereign-wealth/) | News-peg activation watch |

Shared canonical-facts inventory: [`publishing/op-eds/_shared/canonical-facts/norway-mcdowell-inventory_2026-05-10.md`](../../publishing/op-eds/_shared/canonical-facts/norway-mcdowell-inventory_2026-05-10.md).

### Skipped / parked venues

Per previous PM handoff 2026-05-24 — see existing handoff at `tools/workstream-handoffs/pm-session-handoff_2026-05-24.md` for the skipped/parked-venues list (Christophers deep review parked 2026-05-25; etc.).

---

## 7. Dashboard B — Book chapters + other manuscript artifacts (2026-05-25)

Out of scope for this PM session pickup — see existing PM handoff 2026-05-24 for chapter Stage-3 + Stage-4 + Stage-5 matrix + Ch 2 Pass 3.3 LIGHT RE-FIRE state (commit `b4dc755`) + Ch 2 Phase C-ζ confirmation 2026-05-25 (commit `9bddbd2`).

---

## 8. Other workstreams + standing capabilities

### Agent-search PM session — READY TO FIRE

The new `publishing/agents/<agent-slug>/` directory architecture is in place. Per-agent directories will be created by the agent-search PM session and inherit the architecture from day one. No reorg-migration overhead.

**Pre-conditions for agent-search PM session:**
- ✓ `publishing/agents/_shared/templates/query-letter-template.md` — template available
- ✓ `publishing/agents/_shared/personalization-snippets.md` — snippets available
- ✓ `publishing/agents/_shared/post-darity-warm-intro-templates_2026-05-10.md` — warm-intro templates available
- ✓ `publishing/agents/_pipeline/query-tracker.md` — tracker available
- ✓ `publishing/agents/_pipeline/targets.md` — current target list (1 agency identified: Wylie / Sarah Chalfant; scale-up target 50-100)
- ✓ Author platform: [`publishing/book-proposal/03_author-platform.md`](../../publishing/book-proposal/03_author-platform.md)
- ✓ Architecture documented: [`publishing/agents/README.md`](../../publishing/agents/README.md)

**Status-tag convention per Q3 ratification:** `<agent-slug>_QUERIED-<date>` / `_REQUESTED-<date>` / `_OFFERED-<date>` / `_SIGNED-<date>` / `_PASSED-<date>` (archive).

**Author has text ready to paste** to spin up the agent-search PM session per author direction 2026-05-24.

### Publishing-reorg follow-up sessions

Two follow-up workstreams deferred per author direction 2026-05-24:

1. **Rigor-pass artifact relocation** — currently all rigor-pass artifacts remain centralized at `tools/rigor-passes/`. Author initially ratified ("ratify rigor-passes also move") then reversed within same ratification turn ("nevermind rigor passes for now. Let's look closer at that after we are done with this.") — defer until after current submissions land + agent-search PM session output settles.
2. **Essay-file audit-trail-vs-prose separation** — current essay.md files (especially 100-barrel; also Noema/Aeon/BR/Atlantic Ideas) mix audit-trail frontmatter with prose body. Refactor essay.md → split into clean `essay.md` (prose only) + sibling `audit-trail.md` (or similar) so essay.md is clean prose. After separation, re-enable `publishing/essays/*/essay.md` in scaffolding-scan scope (currently commented out in `tools/quality-gates/scaffolding-patterns.yaml` + `regressed-patterns.yaml` + `tools/scripts/check-corpus-invariants.sh`).

---

## 9. Decisions pending

### Submission-timing strategy

Previous PM handoff (2026-05-24) recommended YES on submitting all four ready essays in parallel within 7 days. That recommendation stands; the publishing reorg completion doesn't change it. Author bandwidth is the only constraint.

### Atlantic Ideas Stage 3 cycle continuation

Atlantic Ideas essay has Pass 3.1 PROPOSED 2026-05-23. Stage 3 cycle (3.2 voice-polish + 3.3 + 3.4 + 3.5) pending. Compare cadence to other essays' Stage 3 cycles (avg ~5-7 days end-to-end). Fire Stage 3 continuation when author has bandwidth — not on critical path for June batch.

### Foreign Policy alternate venue (for Atlantic Ideas or other content)

Per [`tools/workstream-handoffs/foreign-policy-alternate-outline_2026-05-21.md`](foreign-policy-alternate-outline_2026-05-21.md) — outline for FP-as-alternate-target exists. Worth revisiting if Atlantic Ideas Stage 3 cycle surfaces fit concerns.

---

## 10. Date-anchored action list (2026-05-25)

| Date | Action | Owner |
|---|---|---|
| Now | Submit Noema (rolling; 7 author actions) | Author |
| Now | Submit Boston Review via Submittable | Author |
| 2026-05-31 | Aeon pitch ready (submission-day package staged) | Author |
| 2026-06-01–07 | Aeon portal window (submit during this window) | Author |
| Now or after | Submit $100 Barrel to Phenomenal World | Author |
| 2026-05-25+ | Agent-search PM session fires (per-agent dirs populate new architecture) | Author + Claude PM session |
| 2026-05-25+ | Atlantic Ideas Stage 3 cycle continues (Pass 3.2 → 3.5) | Claude per-pass sessions |
| 2026-08-05 | Berggruen Prize soft target (12-day buffer) | Author offline AI-free |
| 2026-08-17 | Berggruen Prize hard deadline | Author |

---

## 11. Session freshness

This handoff is dated 2026-05-25 — fresh as of publishing-pipeline reorg Session 2 commit `52fde31` on `origin/main`. Should be picked up by next PM session no later than 2026-05-28; if not, stale-memory verification needed per [`tools/memory/feedback_verify_stale_memory_claims.md`](../memory/feedback_verify_stale_memory_claims.md) (counts, dates, statuses, file paths likely-stale after ~3 days).

Particularly time-sensitive items to verify on next PM session pickup:
- Submission status of each essay (whether any have landed at editor-review)
- F-FC-Noema-9 Norway fund value (re-verify at submission-window)
- Phat consent status (per relationship-pace pursuit)
- Berggruen Prize hard deadline distance (currently ~84 days as of 2026-05-25; check current)

---

*End of PM session handoff 2026-05-25. Per CLAUDE.md internal-scaffolding boundary: this PM handoff artifact autonomously fast-forwards to main at session close. Next PM session picks up here.*
