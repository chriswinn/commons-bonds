# Reverse-CSD leftovers — kickoff paste-texts for parallel sessions (2026-06-10)

Four self-contained kickoff texts. Each assumes a FRESH session with no memory of
the originating conversation. The reverse-CSD/framework-core revision is MERGED to
main as of 2026-06-10 (architecture "three ways count the identity"; §5.5 reverse
method + §17.7 generativity applied; calc engine at
`manuscript/technical-appendix/calculations/`). Source session: `claude/ta-reverse-csd-260610-4fc8d1`.

---

## PASTE-TEXT 1 — §11.12 reef worked case (GATE-2-gated; launch WITH/AFTER the Ch3 restitution-section drafting)

You are drafting TA §11.12 — the Chesapeake oyster-reef restitution calibration, the
framework's first worked BACKWARD case — plus the small cross-TA reconciliation it
requires. FIRST ACTION: worktree-isolate per
`tools/drafting-templates/worktree-isolation-paste-text.md` with slug `ta-reef-11-12`.

GATE (hard): §11.12 may be DRAFTED but must NOT merge to main until a book chapter
(expected Ch 3) carries the priced restitution claim — the TA must never lead a number
into print ahead of the book. Verify the current `manuscript/chapters/Chapter__3_TheWaterman.md`
actually prices the reef before merging; commit with `MERGE-HOLD:` until it does.

READ FIRST (all on main):
1. `tools/audits/ta-reverse-csd-reef-calibration_proposal-record_2026-06-08.md` — full
   draft content (sections A–H) + verification addendum. Treat as WORKING DRAFT to
   re-render against the CURRENT TA: its line numbers and §5.5/M3 wording predate the
   2026-06-10 framework-core revision. Its §C (Daly) and §E (§5.6) are DONE; its §F
   authorial note is DECLINED-CLOSED; its A1–A3 are SUPERSEDED by the applied §5.5.
2. `tools/audits/ta-5-5-reverse-method-upgrade_PROPOSED_2026-06-10.md` — the applied
   §5.5 reverse method your §11.12 must exercise (RATIFIED+APPLIED status note).
3. `manuscript/technical-appendix/calculations/csd_rcv_calculations.py` Part 4 + its
   run-output — every reef number, derivation shown, 20/20 checks PASS.
4. `research/story-drafts/ch3-restitution-bond-numbers_2026-06-05.md` — sources +
   adversarial stress-tests.
5. Current TA §5.5 + §11 (`manuscript/technical-appendix/TechnicalAppendix_v2.0.0.html`).

RATIFIED CONTENT DECISIONS (do not re-litigate):
- Bond anchored at the M1 cure-cost floor ("bond only the unassailable floor"):
  2,738 ac (James River oyster-rock lost 1910→1981; Schulte 2017 Front. Mar. Sci.
  4:127) × $7,300/ac (Great Wicomico realized, NOAA per-tributary table) ≈ $20M;
  × $13,500/ac (Great Wicomico Tributary Plan §5) ≈ $37M headline floor;
  × $77,000/ac (bay-wide avg) ≈ $211M central. AREA basis only — the Darling
  shell-mountain stays narrative, never a number.
- M2 = realized-B₁ reading: >$92M MD (MD DNR/Gov. Moore Aug 26 2025); ~$115M bay-wide
  itemized (NOAA: MD $93.52M + VA $21.77M) as PRIMARY; $108M program-level is a
  rounding corroborator only. $0 industry. Unit-cost corroboration: $108M÷1,900ac ≈
  $57K/ac sits inside the M1 band. The finding is MIS-ASSIGNMENT, not just magnitude.
- M3 = NAMED, not priced — the §5.5 Open state. State explicitly it is a strategic
  decline (bond design), not methodological; the method is fully specified in §5.5;
  never show-then-flinch. Reef is restorable → low realized α → M3 adds little here.
- Renewable-with-extracted-renewal-structure note: the reef forecloses the
  REGENERATION FUNCTION (ρ; Def 1.1 + Thm 10.3) — distinct formal object from the
  non-renewable §11 cases; a feature.
- NO Hampton-Bar-specific acreage (none exists — James figure is the stated proxy);
  NO invented NSA Hampton Roads dollar figure (qualitative only); the phrase "invites
  an argument I do not need to have" is NOT in Ch3 — never quote it.
- Architecture: M1+M3 estimate CSD; M2 reads realized B₁ (§3.4/§3.6 as merged).

BLAST-RADIUS RECONCILIATION (required in the same package): the TA says in ~9 places
that the backward direction is cited-not-computed / "forward by design" (§1.7-region
L474, §1.10/Def 1.10 boundary, §5.5 backward-application header + empirical-scope
paragraph, §11.7, Thm 10.1b symmetric-application paragraph, §17.5 bidirectional
corollary). Reconcile each to "computed ONCE, for the reef demonstration (§11.12);
other backward cases remain cited-not-computed." Use the light-touch
"single worked demonstration / proof of reach" framing — do NOT introduce a
forward-converges/backward-ranges dichotomy (contradicts Thm 10.1b + §17.5; both
directions produce bound-ranges, backward typically wider, degree not kind).
Update §10.2's "six cases total" census to reflect the added backward case, and add
the reef row to the §3.6 worked-example table.

DISCIPLINES: no "standing" anywhere in the apparatus; no unpriceability theorem;
every number sourced/derived-with-work-shown/labeled (cite EXTERNAL authorities,
never our own ledger); bib entries (Schulte 2017; NOAA per-tributary table; Great
Wicomico Tributary Plan §5; MD DNR/Gov. Moore 2025) go to
`research/literature/bibliography.md` §25 AND re-run
`tools/back-matter/build.py gen-all` (TA §18 + reader bib regenerate from the master);
reconcile reef figures into `manuscript/ledgers/_CANONICAL_FIGURE_LEDGER.md` + coordinate
with the Ch3 session (figure-cascade discipline). Per-prompt cadence: present for
author ratification before applying. Never force-push main.

---

## PASTE-TEXT 2 — WS2 symbol-registry sync (B̂_M2 + CSD_M3 rows)

You are doing a small symbol-registry sync for the 2026-06-10 framework-core
revision (merged to main). FIRST ACTION: worktree-isolate per
`tools/drafting-templates/worktree-isolation-paste-text.md` with slug `ws2-registry-sync`.

CONTEXT: WS2 last synced `manuscript/technical-appendix/symbol-registry_2026-06-07.md` to
the TA at commit `fd12275`. The framework-core revision then landed: §3.4 now defines
**B̂_M2** (B-hat subscript M2 — the Method-2 realized-Bond reading; a strict lower
bound on RCV, NOT an RCV estimator), and §5.5 now carries **CSD_M3** (backward
Method-3 composite: `CSD_M3 = V_market × scarcity_multiplier(ς) ×
irreversibility_premium(α)` with V_market's backward reading = extinguished
optionality / foregone service flow).

TASK: (1) add registry rows for B̂_M2 and CSD_M3 (group them with the existing
CS/CSD/RCV/B family; note B̂_M2's hat = "reading/estimate of," distinguishing it from
the posted-instrument B of Def 1.7); (2) sweep the merged TA for any other symbol the
revision introduced that the registry lacks (the revision also touched §3.3/§3.6/
§15.1.3/§17.7 — expected: no other new symbols, verify); (3) re-run
`python3 tools/back-matter/build.py gen-all` and confirm symbol-registry.html
regenerates clean; (4) check ς (&sigmaf;) renders in the back-matter font path
(glyph gate: `tools/scripts/check-glyph-coverage.py`). Update the STATE.md
framework-core-revision row's "symbol registry" clause when done (same commit).
Internal scaffolding — merges to main at session close per CLAUDE.md.

---

## PASTE-TEXT 3 — Stage-4 TA markup sweep (technical-review window)

You are doing a markup-hygiene-only pass on
`manuscript/technical-appendix/TechnicalAppendix_v2.0.0.html` (NO prose changes). FIRST
ACTION: worktree-isolate per `tools/drafting-templates/worktree-isolation-paste-text.md`
with slug `ta-stage4-markup`.

THREE ITEMS (flagged by the 2026-06-10 whole-TA review; queued to the
technical-review window alongside the cb2d2f8-deferred in-TA Notation + Part 7 items):
1. **Invalid table markup, file-wide:** many tables have an EMPTY `<tbody></tbody>`
   with the data rows OUTSIDE it (between `</tbody>` and `</table>`), and several use
   `<td>` inside `<thead>` where `<th>` belongs (§6.3, §7.2, §7.3, §9.5, §16.4 are
   known instances — sweep all). Re-parent rows into tbody; convert header cells to th.
   Browsers auto-recover so RENDERED output should be IDENTICAL — verify with the
   render pipeline before/after (wkhtmltopdf + Chrome divergence history: commit
   cf24f57).
2. **Integral typesetting:** bounds are plain run-on text (`∫t₀∞`) with no
   `<sub>/<sup>` in §3.1 (Def 1.6), §7.3, §17.2/§17.6 formula blocks. Typeset as
   sub/superscript. Do not alter formula CONTENT.
3. **ς glyph check:** confirm `&sigmaf;` (final sigma, U+03C2) coverage in the
   EB Garamond render path (`tools/scripts/check-glyph-coverage.py`); known tofu-risk
   flagged at the M3 rework. Also spot-check �?-class artifacts in §10 theorem blocks.
Constraint: every diff hunk must be tag-only/whitespace-only. If any hunk would touch
prose, STOP and queue it instead. Internal-quality pass on reader-facing artifact:
commit with `MERGE-HOLD:` and present the before/after render check for author
sign-off (Stage 4 discipline).

---

## PASTE-TEXT 4 — TA provenance pass (Libby + Baotou + RCV-integral calibration)

You are closing the three remaining shown-work gaps in the TA's empirical sections,
flagged by the 2026-06-10 whole-TA review. FIRST ACTION: worktree-isolate per
`tools/drafting-templates/worktree-isolation-paste-text.md` with slug
`ta-provenance-11-3-11-4-integral`. Lineage: successor to the
`ta-number-provenance-ledger_2026-06-07` / `ta-method1-input-provenance_2026-06-06`
sessions (read both first for format + standards).

TARGET STANDARD: §11.5/§11.6's level — every figure sourced, derived-with-work-shown,
or labeled a framework estimate with sensitivity. Discipline per
`tools/memory/feedback_quantitative_apparatus_peer_review_defense.md`: never a posited
number typeset to look sourced; argue conservatively; add sensitivity statements
DEMONSTRATING results don't depend on contested inputs.

THREE ITEMS:
1. **§11.3 Libby:** the stated "Total documented: $4 billion+ (40:1...)" is not
   reachable from its own listed components ($600M Superfund + $250M settlements +
   $50M/yr ongoing + $500M property ≈ $1.35B + accrual). Source the $4B+ (or re-derive
   and restate honestly); show the derivation for the IPG triplet (55–82× / 48–76× /
   61–91×) or re-derive it from sourced inputs.
2. **§11.4 Baotou:** the IPG triplet (12–35× / 18–48× / 22–41×) has no stated
   denominator or derivation. Establish the value-captured basis ($2–4B/yr export
   revenue vs downstream framing), show the arithmetic, or re-derive.
3. **§11.1 + §16.4 RCV-integral lens:** the $580–620/ton RCV-model estimate and the
   67–134× IPG range have NO documented calibration (U(R,t,Q) flow form, E(R,t)
   schedule, Weitzman decline path). A labeled-assumption reconstruction
   (`manuscript/technical-appendix/calculations/csd_rcv_calculations.py` Part 3 — read it)
   reaches $526–541/ton, close but not matching. Either recover/document the original
   parameterization in the TA (a short "integral calibration" note), or re-derive the
   numbers from a documented one and cascade (§3.6 table + §9.5 + §16.4 + §11.11
   integral-lens references).
Cross-model note: §9.5's 67–134× cell is the cross-MODEL (integral) check and was
deliberately left during the M3-method reframe — your item 3 owns it now.
Per-prompt cadence; commit `MERGE-HOLD:`; present derivations for ratification
before applying; update `tools/audits/ta-number-provenance-ledger_2026-06-07.md`
(or successor) with dispositions.
