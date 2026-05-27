---
name: feedback-rigor-vs-bookkeeping-distinction
description: In portfolio-state and pipeline-state framing, distinguish rigor-work-pending (substantive 5-pass cascade work affecting publisher-facing prose) from post-rigor bookkeeping/handoff steps (Stage 5 sign-off filings, per-essay folder mirrors, cover-letter drafts, README refreshes, feature-branch merges to main). Conflating the two reads the portfolio as more in-flight than it actually is.
metadata:
  type: feedback
---

**Rule.** When framing pipeline/portfolio state for the author or in inventory artifacts, separate two categories explicitly:

1. **Rigor-work-pending** — substantive 5-pass cascade work (Pass 3.1 fact-check + 3.2 voice-polish + 3.3 acceptance + 3.4 adversarial + 3.5 developmental + Stage 4 render + Stage 5 sign-off content). Affects publisher-facing prose. This is real in-flight work.

2. **Post-rigor bookkeeping** — handoff/filing steps after rigor is done: per-essay `stage-5-signoff.md` folder mirrors, central rigor-pass artifact filing if a per-essay mirror exists or vice versa, cover-letter drafts, README refreshes, feature-branch merges to main, folder rename to `_SUBMITTED-<date>` status tag, pre-pub review queue extraction. These are filing/handoff actions, not in-flight rigor.

Both can be "pending" at the same time; what matters is calling them distinct categories so the reader can read the portfolio's true substantive-completion state at a glance.

**Why.** Surfaced by author 2026-05-27 after the cross-essay portfolio review session ([`tools/workstream-handoffs/cross-essay-portfolio-review_2026-05-27.md`](../workstream-handoffs/cross-essay-portfolio-review_2026-05-27.md)). I framed Atlantic Ideas as "Stage 5 close-out pending" and NYRB as "per-essay mirror missing" alongside Foreign Affairs (which truly is awaiting only a merge authorization), making the portfolio sound like 4 essays were mid-cycle when in fact only Harper's had any rigor pass still firing. The author corrected: "the only essay that isn't complete is harpers and that completion is coming any moment now." The framing failure under-credited the portfolio's actual completion state by treating filing-paperwork as equivalent to rigor work.

The cost of conflating these is: PM priorities get mis-set (post-rigor bookkeeping items get MED priority when they should be LOW); session-handoff state-markers read more alarming than warranted; the author has to re-read inventory artifacts to recover the true substantive-completion picture.

**How to apply.**

- In §0 / preamble framing of any portfolio-state or PM-dashboard artifact, lead with the substantive-completion state: how many essays are RATIFIED-AWAITING-SUBMIT or RATIFIED-READY-TO-SUBMIT or pitch-LOCKED, and how many have actual rigor work still firing. Bookkeeping items go in a separate sub-section, NOT the headline.
- In recommendations tables, add a "Class" column with values like {bookkeeping, rigor, tracking, PM, housekeeping} so the reader can sort by class before priority.
- When using terms like "pending," "in flight," "still open," or "incomplete," reserve them for *rigor*-pending items. For bookkeeping, prefer "filing", "mirror", "handoff", "scaffolding completion", "merge authorization needed."
- For Foreign Affairs-style cases where Stage 5 is RATIFIED but end-user-facing prose remains on a feature branch awaiting author merge authorization: this is bookkeeping (a merge step) but it has HIGH priority because the merge is the literal last gate before submission. Use the **Class** column to mark it bookkeeping AND HIGH; the two are not contradictory.

**Related memories.** [[project-book-complete-marketing-phase]] (book substantively complete since 2026-05-25; portfolio joined that state on 2026-05-27 with Harper's the trailing in-flight piece). [[feedback-pm-dashboard-structure]] (PM dashboard v2.0 — priority-labeled status buckets).
