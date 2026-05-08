# Publishing Decisions Log

**Purpose.** Append-only record of publishing-strategy decisions — what was decided, when, and why. Mirrors the discipline in `alignment/decisions/`. Use for: venue choices, sequencing, rights questions, agent-query gating, deadline shifts.

**Discipline.** Newest at top. Each entry has date, decision, context, and (when relevant) what it supersedes.

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
