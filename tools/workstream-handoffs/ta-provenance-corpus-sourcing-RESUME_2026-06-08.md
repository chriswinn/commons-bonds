# TA Provenance + Corpus-Sourcing — RESUME / HANDOFF (2026-06-08)

**Branch:** `claude/ta-provenance-260607-ad2dfc` — HEAD `381d998`, pushed, **HELD from main** (sub-branch of the held `ta-rigor-audit-260606`). Author reviews before any merge.
**Trigger to resume:** "resume the TA provenance + corpus-sourcing work."
**Why this handoff:** session crossed ~1M tokens. All substantive work is committed + pushed; the open items below are well-defined.

---

## ARTIFACTS BUILT THIS SESSION (all on the branch)
- `core/technical-appendix/TechnicalAppendix_v2.0.0.html` — applied: §11.10 space cluster, §11.9 DAC bands (source-confirmed + NAS fix), §18 bib gaps (7 entries), SCC attribution fix (§3.3+§11.9), B→billion spell-out, **self-citation wording kill (§11.6 IPG / §11.11 / §6.7 / §7.3 — "canonical/documented/terms_index" as justification removed, derivations shown, 0 numbers changed)**, + merged Session D's M3 Path-A rework.
- `research/literature/bibliography.md` — §23.3 corpus-wide figure sources + §18 DAC/SCC papers + Darity-packet recoveries (Bassett-Bell/Darity JAMA 2022; Colden 2017 MEPS; etc.).
- `tools/audits/ta-number-provenance-ledger_2026-06-07.md` — every TA number classified (sourced/derived/labeled-assumption/UNSUPPORTED) + value-verification sweep (Part 5b).
- `tools/audits/ta-number-provenance-DECISION-MEMO_2026-06-07.md` — judgment items + owners (Items 1–9; ownership table).
- `tools/audits/corpus-primary-source-register_2026-06-08.md` — **THE master register.** §1 ~40 load-bearing facts → primary source+URL; §2 ~14 CORRECTIONS (figures the sources contradict); §3 UNVERIFIABLE; §4 framework-outputs; §6 outreach-folder findings (Darity with-citations packet + Colden/Moore/CBF).
- `tools/audits/chapter-citation-specs/` — ch01–ch10 per-figure apply-specs + README rollup (reconciles the existing `_CITATION_EVIDENCE_LEDGER_2026-06-04` + my register).

## DISCIPLINE RATIFIED (carry forward)
- Cite the EXTERNAL primary source; **never our own ledger/audit/"canonical" status.** "It's so because we said so" = nothing. (Applied to TA; same wording fix pending in chapter prose.)
- Framework OUTPUTS (IPG/RCV/CS/per-ton tiers) are NOT externally sourced — label "framework-computed, derivation shown." Do NOT relabel them broadly; only kill external-authority *wording* + show the derivation.
- **Externally-sourced NUMBERS/FACTS belong in the bibliography — not just quotes.** (Author correction 2026-06-08: a prior session erroneously excluded non-quote facts from the bib. This is why the grandfather patents never got entered.)
- No invented sources; UNVERIFIABLE marked honestly.

---

## OPEN ITEMS (author's 2026-06-08 message + this session's investigation)

### 1. $108T Social Security — recompute is NOT in the repo (highest-value find)
- **Decision + bug-diagnosis LANDED on main:** `fe72992` + `manuscript/_DEEP-SOURCE-REPORT_2026-06-04.md` §"The one genuine problem." Bug: $108T compounds all SS contributions at equity-index returns since 1937 **without netting benefits paid out** (gross "highest possible," ~100× the ~$1T Brookings counterfactual; mathematically unreachable; internally inconsistent with the "~$22.6T unfunded" line).
- **Recompute SPEC exists:** net out benefits paid; inputs = SSA Trustees contribution+benefit series since 1937 × a disclosed real equity-index return, compounded → honest NET figure as a labeled counterfactual; OR qualitative fallback; OR substitute Brookings/CRR ~$1T or Trustees ~$22.6T.
- **RECOMPUTE FOUND 2026-06-08 — it exists, just UNCOMMITTED.** Location: `/Users/c17n/commons-bonds-redraft-campaign-resume-260606-f8216d/research/story-drafts/ch5-blind-wholecloth-v1_2026-06-06.md` (the redraft campaign's own worktree; not committed/pushed → invisible to git branch greps; this matches the author's "a session computed it but the commit didn't land" theory). The draft: explicitly **disavows $108T as "dishonest"**; shows the honest build — cumulative contributions ~$26T ≈ cumulative benefits ~$26T (cancel by design), investable = running surplus peak ~$2.7T, compounded at a disclosed real equity return **net of payouts → "a few trillion dollars, not a hundred trillion"** (honest floor: "runs into the trillions"); keeps the **~$22.6T 75-yr actuarial shortfall distinct**; frames **$16T as cumulative** (correction handled). NOTE: it still attributes **$11T to Mian & Sufi** (register §2.2: $11T is Fed Z.1; House of Debt's number is $5.5T) — the one live correction in the redraft.
- **NEXT:** (a) the redraft campaign should **commit/push `ch5-blind-wholecloth-v1` so it stops being at-risk-uncommitted**; (b) promote it to the canonical `Chapter__5_TheAccountabilityGap.md` (which + the test-draft still carry $108T); (c) fix the residual $11T→Fed attribution. Chapter-prose → redraft campaign / author. **$108T is RESOLVED in content; only the commit + promotion remain.**

### 2. Darity private-interview quotes — ALREADY RESOLVED (don't re-do)
- `389b773` (RATIFIED 2026-06-04, on main + this branch) **deleted all Darity-interview citations** (TA §1.10 endorsement, 4 TA parentheticals, Ch5:240, orphan bib entry) and seeded `manuscript/chapters/_ACKNOWLEDGMENTS.md`. Published grounding kept (Darity & Mullen 2020; Bassett-Bell/Darity JAMA 2022). **The "Darity 2026 hazard" my chapter-agents flagged was off the historical `_CITATION_EVIDENCE_LEDGER`, not current prose — it is already fixed.** Mark resolved.

### 3. Grandfather USPTO patents — researched, NOT in bib (add them)
- Candidate files holding the research (found via cross-branch grep): `alignment/commons_bonds_personal_stories_candidates_v1.0.0.md`, `manuscript/chapters/_BookLevelGuidance.md`, `publishing/essays/atlantic-main-chesapeake-watermen/rigor/pass-3-1-fact-check.md` (a fact-check pass likely has the verified USPTO numbers). Memory: LaVern E. Winn — 2 patents (Liquid Waste Feed System 1972 + fiberglass-laminate lathe).
- **NEXT:** extract the actual patent numbers from those files, add to bibliography (per the "facts belong in the bib" correction), and pin them in-text (Ch1 §66/68/70 + Ch10 grandfather passage both promise "his name is in the patent record" with no number). **Was interrupted before extraction.**

### 4. $44B Black Lung — relabel pending source-search
- Traced to "$44B THROUGH 2009 (GAO/CRS)" (Darity with-citations Ch6). The test-draft + canonical Ch5 present it as current ("$44B across half a century / $5.1B debt as of Sept 2024"). Date-discrepant → likely a stale 2009 figure.
- **NEXT (author-authorized fallback):** run a focused agent to find any post-2009 cumulative-benefits figure (DOL OWCP annual reports / CRS R45261 mirror / GAO). **If none more current than 2009 → relabel to "≈$44B through 2009 (GAO/CRS)."** (Agent was about to launch when session paused.)

### 5. Black Hills escrow (Ch10) — soften
- Current "more than one and a half billion"; not publicly disclosable at exact balance (Oglala Sioux rejected a FOIA to unseal). **Soften to the academically-defensible ">$1B as of 2018 (BIA escrow)"** or whatever current authoritative anchor exists. Chapter prose → redraft/author.

### 6. Polanyi/Fraser anchor — in flight on the redraft campaign
- `389b773` logged **A1 = FIX RATIFIED**. Plan (per `_BOOK-REDRAFT-ACTION-LIST` A1b): add Polanyi (fictitious commodities) + Fraser (expropriation) to the **bibliography**; work the fictitious-commodity anchor into Ch1/Ch5/Ch6 + appendix §14; **full writeup in Ch5 (Ch8 for the mask-veil lineage)**; callbacks elsewhere. **Coordinate with the redraft campaign** (branch `redraft-campaign-resume-260606-f8216d`) for latest.

### 7. M3 Path-A rework — landed; reconcile my Ch6/register Method-3 figures
- Session D's M3 Path-A rework is **merged into this branch** (McDowell M3 central ~$1,115 geometric; M3-IPG = premium-multiple ~8.5–26×, NOT the old 50–555×; §9.5 67–134× is the cross-MODEL cell, unchanged). **My corpus-register / Ch6 spec Method-3 references may cite pre-rework values — reconcile against current TA §3.5/§11.6/§11.8/§11.11 before applying.**

---

## CROSS-CUTTING: ~14 reputational CORRECTIONS (register §2; mapped to chapter lines in the specs)
Norway 3%-rule=2017-not-2001 · $11T=Fed-not-Mian&Sufi ($5.5T) · $16T=cumulative-not-peak · Hendryx "60k cancer"=OR 2.03 · menhaden cap=Amendment 3 (2017/18) · Baotou >$100B→$5–15B · ">$150B" not-a-NOAA-figure · coal $4.50→$4.71 (EIA; cascades IPG) · GoFundMe=AJPH 2022 · Tangier 15ft/yr=exposed-shore · Libby 80%-world→>70%-US · per-capita Norway $390k · Ch2 "two-thirds income drop" (already softened to ~13–15%) · reclamation-gap stated inconsistently. **These + the A0 coal-$510→$496 cascade (still live in TA/Ch6/Ch9) are the highest-priority, lowest-judgment fixes.** Many overlap the deep-source report's CONTRADICTS list (Libby $4B/40:1; Deepwater $150B/$12B; Baotou $100B).

## OWNERSHIP / COORDINATION
- **Chapter prose application → redraft campaign (`redraft-campaign-resume-260606-f8216d`) + author ratification.** My specs are the apply-spec, NOT authorization to edit prose. Redraft status: ch1/ch2/ch3 v2 drafts (2026-06-05) + ch4-wholecloth-redraft (2026-06-06) in `research/story-drafts/`; Ch5 test-draft (2026-06-04) flags $108T/$44B/$150B as citation-gaps.
- **TA-side:** coal-price $4.50→$4.71 + framework-output relabels coordinate with Sessions C/D; Deepwater reconciliation → Session E (decision-memo Item 4). The §11.6 "$4.50 / Ch 6 convergence table" source-cell is deliberately left self-cited until the EIA $4.71 value lands (coupled).
- **§23.1 bib:** this branch + `ta-m3-pathb` both edited it — merge sequentially.
