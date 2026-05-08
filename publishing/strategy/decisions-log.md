# Publishing Decisions Log

**Purpose.** Append-only record of publishing-strategy decisions — what was decided, when, and why. Mirrors the discipline in `alignment/decisions/`. Use for: venue choices, sequencing, rights questions, agent-query gating, deadline shifts.

**Discipline.** Newest at top. Each entry has date, decision, context, and (when relevant) what it supersedes.

---

## 2026-05-08 (later) — Recalibrate green-light rule and Wave 1 timing; correct chapter-summaries source

**Decision.** Three corrections to `cascade-plan_2026-05-06.md` and `publishing/book-proposal/05_chapter-summaries.md`:

1. **Chapter-summaries source corrected.** GuidanceDocs are scaffolding artifacts (WP#10 layer-classification + staleness disclaimers), not content sources for publisher-facing artifacts. The book proposal's chapter summaries pull from the drafted chapters in `manuscript/chapters/Chapter__N__*__Draft.md` — *not* from `Chapter__N___GuidanceDoc.md`. Same logic applies to overview voice samples (use chapter prose) and sample chapters (use chapter drafts directly).

2. **"Two to four published derivative works at respected venues" framing dropped.** That was a generic-first-author rule of thumb, miscalibrated for this project's actual material strength: 9 of 10 chapters drafted, named-source interview pipeline already converting (Darity ACCEPTED), formal framework apparatus (RCV + Cost Severance), Pattern-2 implementation channel open (Amsterdam DEAL via Dagan). Replaced with the realistic floor: complete book proposal + ≥1 essay at editor-review stage at a top-tier venue + ≥1 substantive named-source interview recorded with quote-permission. "Under consideration at \_\_\_\_" is queryable in good faith if real and current.

3. **Wave 1 agent-query target shifted from November 2026 to late July / early August 2026.** The November target was driven by the higher-bar 2-4 placements assumption. Under the lower floor — and given this author's actual drafting pace (~12K words/week sustained during book writing) — the proposal can be assembled in a 3-week focused sprint targeting late June completion, with the comp-titles section already 80% drafted and chapter summaries pulling from already-drafted chapters. ~3-month acceleration. Wave 2 shifts from Jan to Sept-Oct 2026; Wave 3 shifts from Mar 2027 to Q4 2026 / Q1 2027. Strategic frame point 5 reframed: format mix (magazines + op-eds + academic/policy) builds platform breadth across waves rather than gating Wave 1.

**Context.** Author surfaced the 2-4 placements framing as miscalibrated against earlier-conversation guidance from other Claude sessions, which had suggested one placement (or one substantive submission under consideration) could suffice within the response window. Pressure-tested the math: drafting pace, comp-titles section already drafted, chapter drafts as sample-chapter source, Darity interview May 12 effectively banked — confirms the lower floor and faster timeline are realistic for this project specifically. Also clarified the source-of-truth pointer for chapter summaries (chapters, not GuidanceDocs) — the GuidanceDocs stay in place under WP#10 layer-classification with their staleness disclaimers; they are not consulted for publisher-facing content. Their archive moment is at pre-publication external review (Insight #39), not now.

**Supersedes.**
- `cascade-plan_2026-05-06.md` Context-section "two to four published derivative works at respected venues" framing.
- `cascade-plan_2026-05-06.md` Strategic frame point 5 (format mix as Wave 1 prerequisite → ongoing build); point 6 (green-light rule recalibrated).
- `cascade-plan_2026-05-06.md` 12-month sequence June through April 2027 (proposal sprint inserted in June; Wave 1 shifted to July-Aug; Wave 2 to Sept-Oct; Wave 3 to Q4-Q1).
- `cascade-plan_2026-05-06.md` Verification section (3-month checkpoint added; 6-month checkpoint reframed; green-light line updated; abort/pivot Wave-2 calendar context).
- `publishing/book-proposal/05_chapter-summaries.md` source-mapping table + drafting-rules section (GuidanceDocs → chapter drafts).

---

## 2026-05-08 — Cascade plan refresh: integrate v1.52.0 + post-handoff state; resolve two open decisions

**Decision.** Refresh `cascade-plan_2026-05-06.md` and `rights-register.md` to reflect canonical state per session-handoff v1.52.0 (2026-05-06) plus subsequent commits through 2026-05-08. Two `Decisions due in 2–4 weeks` items resolve out: the Aeon title and the `draft2.md` fate.

**Captures the following state changes:**

1. **Aeon pitch title ratified** — "The Mask of Abundance" (rigor pass v1.0.0, 2026-05-08); five candidates evaluated through full rigor pass (`tools/rigor-passes/commons_bonds_rigor_pass_2026-05-08_aeon_pitch_title_candidates_v1.0.0.md`); selected for "X of Y" pattern matching Sandel/Pistor/Mazzucato/Raworth + frame-agnosticism + threading to pitch's own signature phrasing. Cultural-engagement commitment to Dunbar/Du Bois/Ellison/Fanon lineage — explicit acknowledgment in Aeon essay + book Ch 8 + Ch 1; bibliography §21 added; mask-terminology pivot prepared for Darity May 12 call. Version B alternate-frame draft preserved on hand.
2. **Darity interview confirmed** — 2026-05-12 @ 14:00 ET, phone, 1 hr (author calls Sandy). Pre-read brief, background brief, internal interview-prep doc, live-call companion (HTML+MD), framework-decline contingency plan all drafted. Mullen warm-intro deferred to end-of-call.
3. **Outreach pipeline state per v1.52.0 + post-handoff:**
   - Mazzucato HOLDING via Adam Albrecht (UCL/IIPP).
   - Beth Ingledew → Dagan (Amsterdam DEAL implementation team) warm intro materialized 2026-05-08; response sent. Strongest Noema solutions-cluster-γ candidate now that channel is open.
   - Colden (CBF Maryland) via Val DiMarzio: SENT 2026-05-06; 7-question batch stashed.
   - Karen Moore (CBF Virginia) via David Sherfinski: SENT 2026-05-06; parallel CBF track to Colden, both feeding Ch 3.
   - Mullen held until end of Darity call.
   - 8 cold outreaches still awaiting reply within standard 2–3 wk academic window.
   - Interview attribution Q0 protocol now canonical for every interview.
4. **Withdrawn-Noema essay archived** — `draft2.md` moved to `archive/_OneDayMaybe/withdrawn-essays/draft2_withdrawn-noema_2026-05-01.md` 2026-05-08 with §I wife's-illness EXCISED per Candidate #4 discipline. **Resolves** the cascade-plan decision item "Decide whether `draft2.md` becomes Public Books or raw material" — *not* slated for any venue; held as historical record only.
5. **FPD v1.0.0 ratified 2026-05-06** — `alignment/commons_bonds_framework_positioning_disciplines_v1.0.0.md`; eight canonical positioning disciplines including "Why bonds vs. funds/accounts/trusts/reserves" rationale. Feeds book-proposal `00_overview.md` + `02_comp-titles.md` framing.
6. **Personal-story material relocations** — Candidates #2 (Neeraj) + #3 beats (Afghanistan war-zone, company buyout, CEO-setup/Roberts-rules) all moved from `research/story-drafts/` to `archive/_OneDayMaybe/personal-story-material/`. `ch1_aftermath-and-return-to-work_2026-05-01.md` deleted. Story-drafts substrate now 6 files (down from 8); leaner and explicitly curated.
7. **Two new outreach tracks in publishing scope** — Karen Moore (CBF VA) parallel to Colden (CBF MD); Amsterdam DEAL implementation team via Dagan.

**Context.** This branch (`claude/plan-publishing-strategy-9Yubv`) merged `origin/main` twice today (commits `747e47e` + `004c311`), bringing in 73 commits of work from concurrent threads. Refresh keeps cascade plan a living document rather than a 2026-05-06 morning snapshot. v1.52.0 remains the canonical state-snapshot file; the cascade plan is the publishing-strategy-specific projection of it.

**Supersedes.** Selected items in `cascade-plan_2026-05-06.md` Current state, 12-month sequence (May A/B/D + June A + August A), Risks, Decisions due, Verification, and Critical files sections — see commit diff for line-level changes.

---

## 2026-05-06 — Cascade plan ratified; Path B overridden in favor of parallel tracks

**Decision.** Adopt the parallel-tracks publishing strategy in `cascade-plan_2026-05-06.md`. Overrides the May 1 "Path B: book-first" decision: Aeon (Ch 7-derived) is no longer gated on Ch 1 stabilizing; book and essay tracks run concurrently.

**Scope expansion.** Derivative works for this strategy include literary/ideas magazines, op-eds in major newspapers, and academic/policy outlets. Excludes podcasts and owned channels (no Substack/newsletter).

**Load-bearing constraint preserved.** Non-partisan framework positioning remains in force. No specialized applications (abortion, reparations-specific, climate-specific) before the framework's universality is publicly established.

**Supersedes.** `manuscript/essay/Noema/rewrite-plan_2026-05-01.md` Path B sequencing constraint (only the sequencing — the Noema rewrite plan content itself remains in force).

---

## Template for future entries

```
## YYYY-MM-DD — Short title

**Decision.** What was decided.

**Context.** Why. What inputs led here.

**Supersedes.** What earlier decision (if any) this replaces. File path + date.
```
