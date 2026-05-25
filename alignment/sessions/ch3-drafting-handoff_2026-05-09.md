# Ch 3 drafting — mini session handoff (2026-05-09)

**Purpose:** focused handoff for a fresh dedicated session to handle Ch 3 ("The Waterman") drafting. Self-contained — pick up cold without re-reading prior handoffs.

**Why a fresh session:** prior session (`claude/schedule-darity-interview-6RUlG`) ran long across multiple workstreams (Darity scheduling + outreach upgrades + AGENTS.md/README.md/v1.52.0 refresh + Ch 3 drafting) and hit context-depth limits. Better to give Ch 3 a dedicated session on a new branch.

---

## §1. What exists right now

A first-pass Ch 3 draft was produced in the prior session by a subagent under the substitution-hypothesis approach:

- **File:** `manuscript/chapters/Chapter__3_TheWaterman__Draft.md`
- **Length:** 7,167 words across 12 sections
- **Branch:** `claude/schedule-darity-interview-6RUlG` (pushed to remote; not on main — main push blocked, possibly by merge-via-PR policy shift evidenced by recent `d89dc38 Merge claude/respond-to-valerie-inquiry-mV3Na…` pattern)
- **Commit:** `3a8b096`

**The new session should decide one of two paths:**
- **Iterate** — use the existing 7K-word draft as v1 substrate; review, refine, integrate against the GuidanceDoc; commit refinements to the new branch.
- **Restart** — discard the existing draft and redraft from scratch with whatever structural/voice changes the author wants. The existing draft is preserved on `claude/schedule-darity-interview-6RUlG` regardless; nothing is lost.

Recommend looking at the existing draft before deciding — it took a subagent ~13 minutes and 140K tokens of internal work to produce, and the structural beats are reasonable. Strengths and weaknesses below.

### What the existing draft does well

- Opens with harbor-at-dawn at Old Point Comfort (Hampton-roots access-gate established).
- Generational-witness temporal spine (grandfather → father → daughter-to-nursing-school).
- Plants renewable-past-regeneration framing through specific stocks (oysters / blue crab / striped bass / menhaden) without theorizing it.
- Closing tie-back lands cleanly: *"Different resource. Different geography. Same mechanism."*
- Norway bridge to Ch 4 engineered explicitly: *"That is the question the next chapter takes up."*
- Final image circles back to harbor: *"It is not yet the day he could have had."*
- Two passages flagged with `<!-- v1 from public record; revisit post-Colden-interview -->` per substitution-hypothesis discipline.

### What the existing draft has issues with

- **Line 104 names "cost severance" with a self-aware "before that phrase is allowed to enter the chapter" device.** Pattern 2 violation per the GuidanceDoc which explicitly says framework vocabulary does not appear until the closing tie-back. Stylistically defensible but author-decision territory. Either remove or keep as deliberate meta-textual move.
- **Above 5K-6K target band** (7,167 words). GuidanceDoc says "5K-6K is reference, not target" — but worth a tightening pass to see what's load-bearing vs. what could compress.
- **No named watermen** — generic-archetypal observational register only (consistent with Hampton-specificity discipline since no consent gathered). Live Colden interview + waterman fieldwork would let one or two named voices anchor sections 3, 9, and the closing.
- **Colden quotes paraphrased not directly attributed** — preserves Pure Register 1 but means her voice is "a scientist with the Chesapeake Bay Foundation" / "the same Bay Foundation scientist." Named attribution can be added at integration time post-interview.
- **1985 striped-bass moratorium dates** rendered as "for five years on the Maryland side, beginning in 1985" — verify exact dates if a fact-check pass is run.

---

## §2. Operational approach (substitution hypothesis)

This is the discipline that unblocked Ch 3 in the first place. **Critical:** it is the same discipline that unblocked the Noema essay 2026-05-08/09 (proven on Section VI Chesapeake third-anchor + Section V Darity sub-portion). Not novel; canonical.

- Draft from public-record material + Chris's documented Hampton roots.
- The pending Colden interview becomes an **upgrade opportunity, not a precondition**.
- Mark passages that would benefit from live interview material with HTML comment flags:
  ```
  <!-- v1 from public record; revisit post-Colden-interview -->
  ```
- Post-interview (Colden if/when it lands; Darity already May 12), evaluate flagged passages for upgrade-vs-hold per the same two-position decision used in the Noema plan.

Source for full operational frame: `publishing/essays/noema-commons-bonds/_archive/planning/noema-essay-drafting-plan_2026-05-08.md` §HYBRID OPERATIONAL APPROACH.

---

## §3. Required reading (in order; lean — substitution-hypothesis-tested)

1. **`manuscript/chapters/Chapter__3___GuidanceDoc.md`** — full read. Canonical structural guidance. Pure Register 1; 2-4 watermen at depth; Hampton-specificity discipline; renewable-past-regeneration as Ch 3's distinctive framework contribution; closing tie-back; Norway bridge.
2. **`manuscript/chapters/Chapter__2_TheMiner.md`** — full read. Structural sibling; sets the register bar.
3. **`manuscript/chapters/Chapter__3_TheWaterman__Draft.md`** (the 7K-word v1 from prior session) — read end-to-end if iterating; skim if restarting.
4. **`research/outreach/subjects/colden/background-brief_2026-05-08.md`** — **skim, don't fully read** — pull what you need: oyster collapse statistics; striped bass + menhaden + crab regulatory battles; CBF positions; named watermen quotes (mine via grep); specific years and events.
5. **`alignment/commons_bonds_personal_stories_candidates_v1.0.0.md`** — grep for "Hampton" / "Bay" / "harbor" / "waterman" / "Old Point Comfort" / "Fort Monroe" / "dockmaster" / "sailboat" — Chris's documented first-person material.
6. **`manuscript/chapters/Chapter_10_CommonBonds__Draft.md`** — skim end of file only (harbor-dawn closing pages). Don't repeat scenes Ch 10 owns.

**Optional reference:** `research/outreach/subjects/cbf/organizational-brief_2026-05-06.md` (CBF institutional context); `research/outreach/subjects/moore/background-brief_2026-05-08.md` (CBF VA additional substrate); `research/case-studies/chesapeake-fisheries.md` (32-line stub with 99% oyster collapse framing).

---

## §4. Disciplines (non-negotiable)

- **Pure Register 1.** No framework vocabulary in chapter prose until the closing tie-back. Even there, plain-language structural-mechanism phrasing only (not technical terms like "cost severance" / "RCV" / "Restitution Bond" / "Cᵢ" / "CIT" / "Foreclosure Bond").
- **Don't reuse retired vocabulary** per `archive/retirements/index.md` (Value Capture / AIT / Dynastic Labor Cost / Reparations Bond / Resource-Foreclosure Bond / etc.) — but none of these appear in Ch 3 prose anyway under Pure Register 1.
- **Consent-rejection plan applies.** No references to ex-wife or wife-medical material. Son-anchored at immediate end + parents-aging at longer-arc end.
- **Hampton-specificity discipline.** No specific operators (boat names, slip numbers, named watermen families) without consent. Generic observational register is the model.
- **Watermen-community dignity discipline.** Per Ch 2 baseline: skilled workers doing essential work; structural critique with respectful prose.
- **Cross-chapter coordination.** Ch 3 closes on Bay-as-commons → Ch 4 picks up with Norway as existence proof. Engineer the bridge. Ch 3 + Ch 10 share Hampton harbor — establish daily life in Ch 3; Ch 10 returns later. Don't repeat; earn the recurrence.
- **No HTML/math in prose.** Markdown only.

---

## §5. Recommended new-session workflow

1. **Generate fresh branch** per author direction. Suggested name: `claude/draft-chapter-3-watermen-<random-suffix>`.
2. **Cherry-pick or copy the existing draft** from `claude/schedule-darity-interview-6RUlG` if iterating, OR ignore it if restarting.
3. **Read in §3 order** (lean reading list — don't burn budget on 12K-word Colden brief end-to-end; grep + skim).
4. **Make the iterate-vs-restart call early.** Don't waffle — commit to one path.
5. **Resolve the line-104 "cost severance" device** if iterating: remove it, or keep it deliberately as a meta-textual move.
6. **Tightening pass** if iterating: 7K → 5.5K-ish if substance allows. Or accept the 7K length if all beats are load-bearing.
7. **Commit + push to the new branch.** Main push may still be blocked under the new merge-via-PR policy — open a PR if so.

---

## §6. Open loops downstream of Ch 3 drafting

These are NOT blocking Ch 3 itself but worth knowing about:

- **Darity interview Mon May 12 14:00 ET** — already on calendar. Live-call companion at `research/outreach/subjects/darity/live-call-companion_2026-05-06.md` is prepped. Outcome feeds Section V Darity sub-portion of Noema essay (upgrade-vs-hold decision) AND any McDowell-related passages in Ch 5/Ch 8 that the interview sharpens.
- **Colden interview** — pending Val DiMarzio response + Colden availability. Outcome feeds Ch 3 v1 → v2 upgrade decision per substitution-hypothesis flag pattern.
- **Aeon submission** — first week of June (Mon Jun 1 – Sun Jun 7); "The Mask of Abundance" (Version C) ratified.
- **Noema rewrite** — drafting plan ratified 2026-05-09; Phase 1-3 (~3,700 words) drafted-able now under hybrid; Phase 4 = Section V Darity upgrade-vs-hold post-May-12.

---

## §7. Branch + git state at handoff time

- **Feature branch:** `claude/schedule-darity-interview-6RUlG` at `3a8b096` (Ch 3 draft + AGENTS.md update committed; pushed to remote)
- **Main:** `d89dc38` (Ch 3 commit not on main — direct push rejected with 403; needs PR or alternate merge path)
- **Working tree:** clean
- **Files added by prior session:** `manuscript/chapters/Chapter__3_TheWaterman__Draft.md` + `AGENTS.md` (modified)

---

## §8. Cross-references

- `manuscript/chapters/Chapter__3___GuidanceDoc.md` — canonical structural guidance
- `publishing/essays/noema-commons-bonds/_archive/planning/noema-essay-drafting-plan_2026-05-08.md` §HYBRID OPERATIONAL APPROACH — the substitution-hypothesis discipline
- `alignment/sessions/commons-bonds-session-handoff-2026-05-06_v1.52.0.md` — broader v1.52.0 multi-thread state-snapshot
- `AGENTS.md` — current canonical state table (10-of-10-chapters-drafted reflected per prior session's commit)
- `archive/retirements/index.md` — retired vocabulary list
