# PM Session Handoff / Project Dashboard — 2026-06-04

**Date:** 2026-06-04
**Session:** `pm-portfolio-ratification-and-aeon-submission-260529-b4ac02` (opened 2026-05-29; spanning 2026-05-29 → 2026-06-04)
**Supersedes (as CURRENT PM dashboard):** `pm-session-handoff_2026-05-28-portfolio-aeon-pattern-complete.md` (evening 2026-05-28) + `pm-session-handoff_2026-05-28.md` (morning 2026-05-28). Both retained as audit-trail.
**Status:** active dashboard
**Verification note:** all status claims below re-verified against `origin/main` HEAD `1e132cb` + per-essay READMEs on 2026-06-04 per `feedback_verify_stale_memory_claims.md`. Portfolio moved substantially since the 2026-05-28 handoffs — two essays submitted, one declined-and-cascading, major book-side Ch 1 v2 rewrite in parallel.

---

## §1 — Top-of-mind action driver

**The portfolio has started shipping.** Two essays submitted (first portfolio submissions); one already declined-and-cascading. The Aeon-pattern V-D ratification workload that defined the 2026-05-28 handoffs is effectively **closed** — essays advanced past V-D into submission or are RATIFIED-AWAITING-SUBMIT. The live work is now **submission cadence + cascade management + cover-letter rework + Aeon portal-watch**, not V-D dispositions.

**Next concrete author actions (highest-leverage first):**
1. **Foreign Affairs** — ratify the DRAFTED cover letter → submit (1 ratification from shipping; highest-tier venue ready now).
2. **Noema** — resolve the state ambiguity (submit the 2026-05-24 RATIFIED-AWAITING-SUBMIT version now, OR close the V-D-prime cascade first — see §4 🔵).
3. **Public Books** (Accountability Gap cascade) — cover-letter chip in flight; ratify when it surfaces → submit ~Jun 9-13.

---

## §2 — Critical path

1. **Foreign Affairs cover-letter ratification → submit.** Only gate is author final-ratification of the DRAFTED cover letter (`2026-05-27`). Foreign Affairs is a months-long editorial cycle; firing now starts the clock.
2. **Noema submission decision.** README says RATIFIED-AWAITING-SUBMIT (2026-05-24); but a V-D-prime Amendment-D-aware re-cascade filed PROPOSED artifacts 2026-06-01/02 (not visibly closed). Author decides: ship the ratified version, or close the cascade first.
3. **Public Books cascade.** Chip in flight (Option B directory restructure landed `6abf78e`; cover letter + Stage 1 brief + README pending). Target submission ~Jun 9-13.
4. **Aeon portal-watch.** V-E canonical; portal showed a maintenance page 2026-06-03 (first content-distinguishable signal); spot-check every 2-3h through ~Jun 5 then revert to baseline; July 1-5 fallback window planned.
5. **Agent-query Wave 1 window compressed to ~Jun 24 – Jul 1** (cascade plan v2 Amendment 6, ratified 2026-06-03; asset-decay framing — "under consideration at ___" assets peak mid-to-late June). Book-proposal sprint pulled forward to ~Jun 4-20 critical path.

---

## §3 — Author actions (compact list)

| # | Action | Priority | Est. time | Gate |
|---|---|---|---|---|
| 1 | Ratify Foreign Affairs cover letter → submit | 🔴 CRITICAL | ~20 min | None — ready now |
| 2 | Noema submit-now vs close-V-D-prime-cascade decision | 🔴 CRITICAL | ~15 min decide | None |
| 3 | Ratify Public Books cover letter (when chip surfaces) → submit | 🟡 HIGH | ~20 min | Chip completion |
| 4 | Aeon portal spot-check every 2-3h through ~Jun 5 | 🟡 HIGH | ~2 min × N | Portal opens |
| 5 | Atlantic Ideas + Atlantic main submission (author cadence) | 🟡 HIGH | varies | Author bandwidth |
| 6 | Revisit Sandy confirmation-email HELD decision (rationale changed — see §4 🔵) | 🟡 MED | ~10 min | None |
| 7 | NYRB cover-letter ratification (2 chips in flight) | 🟢 LOW | ~20 min | Oct 8-Nov 15 window; not urgent |
| 8 | Harper's R-2/R-3/R-4 author-substrate items | 🟢 LOW | author-substrate sessions | Q4 2026 window |
| 9 | Book-proposal sprint kickoff (~Jun 4-20 per Amendment 6) | 🟡 HIGH | multi-session | Gates agent Wave 1 |

---

## §4 — Priority-labeled status buckets

### 🔴 AUTHOR DECISION needed

- **Foreign Affairs cover-letter ratification** — DRAFTED 2026-05-27; awaits final author ratification → submit. Highest-tier venue ready now.
- **Noema submit-vs-close-cascade** — state ambiguity (see §4 🔵 below).

### 🟡 HIGH-priority queued

- **Public Books cover-letter chip** (Accountability Gap cascade) — IN FLIGHT; Option B directory restructure done; cover letter pending.
- **Atlantic Ideas + Atlantic main** — both RATIFIED-AWAITING-SUBMIT; fire on author cadence.
- **Book-proposal sprint** — pulled forward to ~Jun 4-20 per cascade plan v2 Amendment 6; gates agent Wave 1 query window (~Jun 24 – Jul 1).
- **Aeon portal-watch** — tightened cadence through ~Jun 5.

### 🟢 LOW-priority queued

- **NYRB cover-letter** — 2 chips in flight (ABC-variants-audits + amendment-d-reaudit); Oct 8-Nov 15 submission window, not urgent.
- **Harper's** — V-D HYBRID canonical; 4 author-substrate restoration items (R-2/R-3/R-4); Q4 2026 window.
- **Op-eds** (Norway + McDowell) — news-peg-activation pending; opportunistic.

### 🔵 ESCALATIONS surfaced

- **Boston Review DECLINED 2026-06-03** (same-day editorial-triage boilerplate). HANDLED — cascading to Public Books; bookkeeping landed (BR README state transition + cascade plan v2 W1.2 update + directory rename to `public-books-accountability-gap`). Decline read: information-poor venue-fit signal, not essay-quality signal; cascade plan absorbs it without strategy change.
- **Sandy confirmation-email HELD rationale CHANGED (2026-06-04).** The Darity interview-citation deletion (RATIFIED 2026-06-04, commit `389b773`) removed ALL unpublished-interview citations from the book + TA and relocated the thank-you to a new `_ACKNOWLEDGMENTS.md` seed. **This substantially weakens the HELD confirmation-email's gate-#2 rationale** ("documentation publishers' permissions teams will ask for") — there are no longer interview citations to document consent for. Published-grounding citations (Darity & Mullen 2020; Bassett-Bell/Darity JAMA 2022) are public-record, no consent needed. **Recommendation:** the confirmation email may now warrant decommission rather than hold-to-Day-45, since its load-bearing purpose (permissions documentation) is largely moot. The relationship-hygiene purpose remains but was already judged insufficient on its own (2026-05-31). Flag for author decision; not urgent.
- **Ch 5 $108T figure bug (book-side; RATIFIED recompute 2026-06-04).** Does NOT affect essays — verified the Accountability Gap / Public Books essay does not use the $108T figure. No essay-side cascade required. Book-side Ch 5 redraft queued.

### ✅ COMPLETED this session (2026-05-29 → 2026-06-04)

- **Aeon V-E + Option E.2 contingency** RATIFIED KEEP-AS-IS (`73c5764`); submission-package ship-ready; editor-facing-pitch lens insight surfaced.
- **Amendment D — reception-chain audience weighting** CODIFIED (3 files; `a1f88db` + `63e9f53` + `dac1e85`). Universal framing: prose weights audiences by actual reader chain (direct readers HIGHEST; consultants HIGH; projected downstream LOWER).
- **G1 DOC** — session-end branch-delete-default documentation pass (4 commits: `7878166` + `bbecf47` + `6ed5066` + `a05b209`). G1 RESOLVED (implementation `5313225` + this DOC pass).
- **G4 slug-collision guard** — `check-workstream-slug.sh` + paste-text + scripts README + workstream-handoffs README. G4 RESOLVED.
- **Cascade-v2 amendments** — chip landed; Amendment 1 (pre-warmed-cold framing, 2026-05-31) + Amendment 6 (asset-decay framing → compressed agent Wave 1 to ~Jun 24-Jul 1, 2026-06-03) ratified.
- **Aeon portal-timing investigation** — findings + maintenance-page observation (2026-06-03) logged; submission posture revised to opportunistic-spot-check + July fallback.
- **$100 Barrel SUBMITTED to Phenomenal World** (`bc5d77c` + `51cadd8`).
- **Boston Review SUBMITTED** (`bd9a20a` 🎉 first portfolio submission) → DECLINED → cascading to Public Books (bookkeeping complete).
- **Public Books cascade scaffolding** (Option B directory restructure `6abf78e`).

### ⏳ CLAUDE-ACTION in flight (chips)

- **Public Books cover-letter** (`public-books-cover-letter-accountability-gap-260604-ea56a9`) — Option B done; cover letter + Stage 1 brief + README pending.
- **NYRB cover-letter** (2 worktrees: `nyrb-cover-letter-ABC-variants-audits` + `nyrb-cover-letter-amendment-d-reaudit`).

### 🟣 AWAITING EXTERNAL

- **Phenomenal World** editorial decision ($100 Barrel; clock started ~2026-06-03; 4-8 week window).
- **Public Books** (Accountability Gap; after submission ~Jun 9-13).
- **Aeon** portal-open event (opportunistic; maintenance page observed 2026-06-03).
- **News-peg triggers** for Norway + McDowell op-eds.
- **Sandy Darity** reply (silent 20+ days on 2 prior asks; confirmation email HELD — see §4 🔵).

---

## §5 — Per-essay / per-unit next-action

| Unit | Venue | Current state (verified 2026-06-04) | Next author action |
|---|---|---|---|
| **$100 Barrel** | Phenomenal World | ✅ SUBMITTED ~2026-06-03 | Await decision (4-8wk) |
| **Accountability Gap** | ~~Boston Review~~ → Public Books | SUBMITTED→REJECTED 2026-06-03; cascading; chip in flight | Ratify Public Books cover letter → submit ~Jun 9-13 |
| **Foreign Affairs** (*Existence Proof*) | Foreign Affairs | RATIFIED READY-TO-SUBMIT; cover letter DRAFTED | **Ratify cover letter → submit (CRITICAL PATH)** |
| **Noema** (*Commons Bonds*) | Noema | RATIFIED-AWAITING-SUBMIT (2026-05-24) BUT V-D-prime cascade PROPOSED artifacts 2026-06-01/02 not visibly closed | Decide: submit ratified version OR close cascade first |
| **Aeon** (*Mask of Abundance*) | Aeon | V-E canonical; portal-watch (maintenance page 2026-06-03) | Spot-check portal; submit on open; July 1-5 fallback |
| **Atlantic Ideas** (*Pricing Honestly*) | Atlantic Ideas / Foreign Policy alt | RATIFIED-AWAITING-SUBMIT (Amendment D weighting applied 2026-06-01) | Submit on author cadence |
| **Atlantic main** (*What the Bay Knows*) | The Atlantic features | RATIFIED-AWAITING-SUBMIT; V-D HYBRID canonical 2026-06-01 | Submit on author cadence |
| **NYRB** (*Architecture and Its Residue*) | NYRB | RATIFIED-AWAITING-SUBMIT; cover-letter chips in flight | Oct 8-Nov 15 window; ratify cover letter when chips surface |
| **Harper's** (*What McDowell County Paid*) | Harper's | V-D HYBRID canonical 2026-06-01; R-2/R-3/R-4 author-substrate pending | Q4 2026 window; author-substrate sessions |
| **Norway op-ed** | FT / Bloomberg / Project Syndicate (primary) | V-D' canonical 2026-06-01; news-peg pending | Opportunistic peg activation |
| **McDowell op-ed** | TBD | V-D HYBRID canonical 2026-06-01; news-peg pending | Opportunistic peg activation |

---

## §6 — Date-anchored merged action list

### Now (Thu Jun 4 → Fri Jun 5)

- 🔴 Ratify Foreign Affairs cover letter → submit
- 🔴 Noema submit-vs-close-cascade decision
- 🟡 Aeon portal spot-check every 2-3h through ~Jun 5
- 🟡 Public Books cover-letter chip lands → ratify
- 🔵 Sandy confirmation-email HELD revisit (rationale changed)

### Near (Mon Jun 9 → Fri Jun 13)

- 🟡 Public Books (Accountability Gap) submission
- 🟡 Atlantic Ideas + Atlantic main submission (author cadence)
- 🟡 Book-proposal sprint underway (~Jun 4-20 per Amendment 6)

### Mid (Jun 24 → Jul 1)

- 🔴 Agent-query Wave 1 firing window (compressed per Amendment 6; asset-decay framing)
- 🟡 Aeon July portal window (Wed Jul 1 – Sun Jul 5 fallback)

### Later (Q3-Q4 2026)

- NYRB submission (Oct 8 – Nov 15)
- Harper's submission (Q4 2026; Oct-Nov)
- Wave 2 essay briefs + submissions per cascade plan v2

---

## §7 — Book-side parallel work (context; not portfolio-scope)

Significant manuscript work landed in parallel this session window (not driven by this PM session, but load-bearing context for the successor):

- **Ch 1 v2 whole-cloth rewrite** (`6387113`; 6,149w) — empirically BEAT a month of iteration (`bac8596`); colleague-open, four movements, framework-free; drafting-doctrine Rules 4 + 7 + Amendment A ratified.
- **Ch 5 $108T figure bug** — RATIFIED recompute-net-or-qualitative (`fe72992`); does NOT affect essays.
- **Darity interview-citation deletion** (`389b773`) — RATIFIED 2026-06-04; relocates thank-you to `_ACKNOWLEDGMENTS.md` seed; removes substantive-validation/consent risk; changes Sandy HELD-email calculus (§4 🔵).
- **Book deep-pass + canonical figure ledger + coal-figure cascade** — cross-chapter coherence work in flight.

---

## §8 — Standing items (preserved)

- **Cascade plan v2** — now operational; Amendments 1 + 6 ratified; remaining amendments folded into operational plan.
- **Cross-thread-todos** — Sandy (§4 🔵); publishing-lawyer consultation (late June); Tech Appendix RCV publication-stability.
- **Process changes ratified this window:** Amendment D (reception-chain audience weighting); G1 + G4 git-hygiene resolutions; merge-on-ratification (carried from 2026-05-28).

---

## §9 — Session-freshness for the successor PM session

The successor should:
1. Read CLAUDE.md + always-load memory files (per `@import`).
2. Read this dashboard.
3. **Update the branch first** (`git fetch origin main && git rebase origin/main`) — parallel-session volume is high (this session was 50 commits behind at one point); state moves fast.
4. Re-verify all countable/status claims per `feedback_verify_stale_memory_claims.md` — much of this dashboard is hours-old by the time it's read.
5. Drive the §1 top-of-mind action driver: Foreign Affairs submission + Noema decision + Public Books cascade + Aeon portal-watch.
6. Surface §4 🔵 ESCALATIONS (Sandy rationale change) for author decision.

Expected author interactive load: ~3-5 submission/decision dispositions + opportunistic Aeon portal-watch + chip ratifications as they surface.

---

## §10 — STATE marker

```
STATE: portfolio SHIPPING (2 submitted: $100 Barrel + BR; BR declined-and-cascading; Aeon-pattern V-D workload CLOSED)
NEXT: Foreign Affairs cover-letter ratification → submit; Noema submit-vs-close-cascade decision; Public Books cascade chip lands
AWAITING: author submission dispositions × ~3-5 + Aeon portal-open event + Phenomenal World/Public Books editorial decisions
SEQUENCING: Foreign Affairs is 1-ratification-from-ship (critical path); Aeon time-gated to portal-open (opportunistic + July fallback); agent Wave 1 compressed to ~Jun 24-Jul 1; book-proposal sprint ~Jun 4-20 gates agent wave
```

---

*End of PM dashboard 2026-06-04. Internal scaffolding; auto-merges to main per merge-on-ratification rule.*
