# Tier-1 agent-submission package — gap list + send-ready path (2026-06-11)

**Session:** book-proposal update (`claude/book-proposal-tier1-260611-e0dbb7`), spawned 2026-06-11 per STATE.md Wave-1 critical path.
**Window in view:** proposal assembly ~Jun 14–20 → Pipeline A Wave-1 agent queries fire ~Jun 24 – Jul 1 (cascade-plan v2 Amendment 6).
**What this file is:** the complete inventory of what stands between today's repo state and a send-ready Tier-1 package, with owners and order. Companion decision queue (proposal-prose ratifications) lives in the session conversation + the MERGE-HOLD commit on this session's branch.

---

## A. Package inventory — component by component

| # | Component | State 2026-06-11 | Gap to send-ready | Owner |
|---|---|---|---|---|
| 1 | §00 Overview | RATIFIED 06-09 (Stage 5) + 06-10 recascade; **06-11:** tolerance defect removed (merged); Norway $2T / M2-architecture / food-stamps-scoping edits PROPOSED | Author ratifies the 4-item §00 edit set | This session (author ratification) |
| 2 | §01 Market & audience | Stable; staleness sweep clean | None found | — |
| 3 | §02 Comp titles | Drafted; carries `[verify]` tags + the **dormant Phase-2 web-verification gate** (review-outlet claims, §02 line ~471: gate "before §04 deployment") | Author decision: run the web-verification pass (~1 session) before assembly, or ship comps with the four HIGH-verified Darity rows and soften unverified review-outlet claims | Author decision → spawn session |
| 4 | §03 Author platform | Tables refreshed 06-11 (PW soft clip 06-03; Darity conducted 05-13, permission pending) — merged | Per-Wave refresh at send (Stage-5 gate 2): re-true the soft-clips table the day queries go out | Sending session |
| 5 | §04 Marketing plan | Stable; review-outlet target list inherits §02's verification gate | Rides component 3's decision | — |
| 6 | §05 Chapter summaries | 06-10 recascade in force; **06-11:** Ch 2 + Ch 3 promotion-aligned blocks + Ch 4/5/6 architecture fixes PROPOSED | Author ratifies (3 asks: Ch 2 block; Ch 3 block; Ch 4+5+6 set) | This session (author ratification) |
| 7 | §06 Sample chapters | **Directory EMPTY.** Wave-1 samples = Ch 1 + Ch 5 (proposal-master corrected 06-11 from the stale "Ch 7 + Ch 5") | Pull current canonicals AFTER the parallel Ch 1 + Ch 5 wrap-up stream closes; render per repo pipeline (author renders offline — no in-session PDF) | Assembly session, gated on Ch 1/Ch 5 stream |
| 8 | Query letter | `publishing/agents/` scaffolded; **0 queries sent**; targets at `publishing/agents/_pipeline/targets.md` | Draft query letter (it can be drafted NOW against the ratified §00 — standing ratification to draft on brief-ready applies); per-agent personalization at send | Next session after proposal ratifications land |
| 9 | Platform paragraph (in-query + §00 line) | §00's platform sentence true as of 06-11 (PW under consideration; ratified portfolio queued) | Re-true at send day (any decision/submission between now and Jun 24 changes it) | Sending session |
| 10 | Pre-publication review queue artifact | **MISSING for the proposal package** (pipeline Stage-5 mandatory hand-off; §00's Stage-5 sign-off exists but the rigor/ dir has no pre-pub queue file) | Generate from the Stage-5 sign-off + recascade record: internally-verified vs not-externally-verified inventory + recommended external-reviewer types. ~1 short session | Assembly session |
| 11 | Stage-4 render audit | Deferred to offline handling per author direction 06-09 (Stage-5 gate 1) | Author runs offline render check on assembled PDF | Author (offline) |
| 12 | proposal-master assembly | Skeleton corrected 06-11 (samples, timeline) — merged | Assemble + unifying voice pass after items 1, 6, 7 land | Assembly session ~Jun 14–20 |

## B. Cross-stream dependencies (not this package's files, but Wave-1-blocking or send-relevant)

1. **Ch 1 + Ch 5 wrap-up stream** — samples come from there. Do not snapshot early.
2. **Darity confirmation email** — consent tracker row: HELD-pending-trigger; trigger (2) "publisher-interest moment" fires when agent engagement begins, and trigger (1) Day-45 = **2026-06-29 falls inside the Wave-1 window**. Execute at or before first query send. Draft (needs revision first) at `research/outreach/subjects/darity/post-interview-confirmation-email_2026-05-31.md`.
3. **Moore citation-verification packet** (Ch 3 structure-note, P-6, route via Sherfinski) — pre-submission item for the manuscript, not the proposal; listed so the assembly session doesn't mistake it for closed.
4. **Flagged to manuscript streams (out of proposal scope):** (a) `_AUTHORSNOTE_ON_WINDTUNNELS_AND_AI.md:13` still carries the invented tolerance (chip already surfaced 06-10); (b) **NEW 06-11:** promoted Ch 3 lines 169 + 262 state Tangier shoreline loss "about fifteen feet a year" while the corpus-primary-source-register correction list pins "Tangier ~1.7 ft/yr exposed-max" — register-vs-promoted-chapter conflict; task chip surfaced this session; resolve before Ch 3 ships anywhere external.

## C. Ordered path to send-ready (author view)

1. **Now (this session):** ratify the 4 queued proposal-prose decisions (≈10 min total; one at a time per cadence). Each ratification merges per merge-on-ratification.
2. **Author decision:** comp-title web-verification pass — run (~1 session, needs web access) or soften-and-ship. Recommendation: run it; reviews-network claims are agent-facing factual claims and the gate was created for exactly this send.
3. **~Jun 12–14:** query-letter drafting session (can start before samples land).
4. **~Jun 14–18:** pre-pub review queue artifact (component 10) + any comp fixes.
5. **Gate:** Ch 1 + Ch 5 stream closes → copy samples into `06_sample-chapters/` → assemble proposal-master → strip status headers → author offline Stage-4 render check.
6. **At send (Jun 24 – Jul 1):** per-Wave platform refresh (components 4 + 9); execute the Darity confirmation email (dependency B-2); fire Wave-1 queries per `publishing/agents/_pipeline/targets.md`.

**Bottleneck read:** nothing in the proposal itself blocks the window. The two long poles are the Ch 1 + Ch 5 parallel stream (samples) and the comp-verification decision. Everything else is short, ordered work.
