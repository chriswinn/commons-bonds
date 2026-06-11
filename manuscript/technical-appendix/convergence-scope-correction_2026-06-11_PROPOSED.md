# TA §9 / §10.2 convergence-framing correction — PROPOSED 2026-06-11 (v3 — unified-triple sunset; see §7)

> **v3 supersedes v2's two-triples premise (2026-06-11, book-proposal-tier1 session; author-directed).** v2 treated the §9 model triple (DF/RO/RCV) and the §3 method triple (M1/M2/M3) as two different triples needing a naming-collision firewall. Author challenge + file verification settled it the other way: **they are one apparatus at two points in the framework's history.** Evidence: (1) the calculation engine (`calculations/csd_rcv_calculations.py`, 21/21) computes M1/M2/M3 only — no Real-Options computation exists anywhere; (2) §9.1/§9.3's "Real Options calibrates volatility from market data" contradicts the ratified 2026-06-08 M3 Path-A rework (Arrow–Fisher/Henry quasi-option; β retired; Dixit–Pindyck reading disclaimed); (3) §9.3's "Avoided Externalities" term consumed the same SCC the Damage Function priced — the old triple shared the carbon input across **all three** columns on fossil cases; (4) §11.2's "RCV model estimate ~17–18×" reproduces as the damage lens + $8–12B ongoing — the same computation, not a second model — making "all three models agree within a factor of 1.5" a biased-to-converge exhibit; (5) the §9.5 RO column (45–89× / 12–21× / 57–93×) and Libby/Deepwater RCV-column figures (72–111× / 17–18×-as-model) have **no recoverable derivation** in the corpus. Disposition: **S-full sunset** (author-ratified direction 2026-06-11): §9 rewritten in the unified architecture; §9.5 table recomputed and reshaped (engine extension `calculations/sec9_recompute_2026-06-11.py`, 24/24, 0 mismatches); v2's §4 drafted prose is superseded where it presents DF/RO/RCV as three live approaches. Full v3 edit set + settled numbers: **§7 below**.

*(v2 header preserved below for the record:)*
(v2, Option-B-corrected)

**Status:** PROPOSED (author ratification required — end-user-facing TA prose; NOT auto-applied)
**Target file:** `manuscript/technical-appendix/TechnicalAppendix_v2.0.0.html`
**Base:** `origin/main` tip `0b83257`
**Gate baseline (unchanged worktree):** `check-corpus-invariants.sh --severity HIGH` → exit 0; `csd_rcv_calculations.py` → 0 FAIL (21 values, 0 mismatches)

> **v2 supersedes v1.** v1 (this morning) narrowed the convergence *scope* ("six → three") but **preserved the convergence-as-validation framing and treated Method 2 as a co-equal RCV estimator** — i.e. it regressed §9/§10.2 to the **Option-A** posture. Author corrections (2026-06-11):
>
> 1. The framework does **not require or celebrate convergence** — three "independent" estimates *always* agreeing is a finger-on-the-scale tell, not validation.
> 2. **Method 2 is a legitimate counting/valuation method** (bond, futures, options, and restitution valuation are established economics) — but it counts the **realized bond B: what has *actually been paid*** to repair the severance (reef rebuilt; reparations paid; McDowell restored), **not a third estimate of RCV** (what restoration actually requires). M1 + M3 estimate *what's needed*; M2 measures *what's been paid*; `CS = (M1∩M3, what's needed) − (M2, what's been paid)`, and that gap is the accountability story (reef: ~$110M paid, all public, $0 from the extractor). [Refines v2's earlier "not a counting method" shorthand — the symbol registry's exact word is "not an RCV **estimator**."]
>
> Both corrections are already **ratified canon** elsewhere in the TA; §9 and §10.2 are the laggards.

---

## 1. The correction is already canon — §9/§10.2 just never got it

The 2026-06-10 reverse-CSD merge migrated the TA to Option B almost everywhere. The laggards are the cross-**model** apparatus in §9 and §10.2.

**Already Option B (ratified, applied) — the model to bring §9/§10.2 into line with:**

- **§3.6 (lines 1129–1151) — the gold-standard statement.** "M1 prices *substitution* and M3 prices *option-bearing scarcity*: these are the two independent **RCV estimators**, and their convergence range is the well-supported RCV. M2 reads *revealed internalization*: the realized **Bond** term B … **not a third RCV estimator** — the same observable cannot serve as an estimate of RCV and as the B subtracted from it." Triangulation rule: "where they diverge widely, **the divergence itself is empirically informative** — surfacing what feature of the commons each method captures." Reporting discipline: report both estimators + range + the M2 realized-Bond reading + identified divergence sources.
- **Symbol registry (2026-06-07, upd. 2026-06-10), line 73:** `B̂_M2` is "**a strict lower bound on RCV (RCV ≥ B̂_M2), NOT an RCV estimator — the two value-estimators are M1 + M3.**"
- **§5.5 (line 1507):** "Methods 1 and 3 are the estimators and their convergence is a bound-range."
- **§14/Darity (line 1377):** "two independent RCV estimators (Methods 1 + 3) whose convergence range is reported alongside the Method 2 realized-Bond reading."
- **§11.5 Norway triangulation:** "M1 (full scope) and M3 mid-range estimates converge … M2 is the **OUTLIER LOWER-BOUND**."

**Still Option A (residue — what this proposal fixes):**

- **§9. "Three-Model Convergence Framework"** — frames model agreement as the result being demonstrated.
- **§9.1 (line 3212):** "correlated measurement error would not consistently produce IPG estimates within one order of magnitude **across six tested cases**" — overstates scope *and* leans on an independence claim the next point undercuts.
- **§9.5/§9.6 narrative** — convergence-ordering prose that contradicts the table (see audit B6).
- **§10.2 "Empirical Observation 10.2 (Cross-Model Convergence)"** census (line 3546): "produce IPG estimates within one order of magnitude **across the six forward cases**," with Norway in the "empirical four" but absent from the §9.5 table.
- **§11 intro (line 4002):** "**All four cases show IPG ≫ 1**" (Baotou's IPG isn't computable).

---

## 2. This terrain is already audited — reconcile, don't re-patch

The held **2026-06-06 TA rigor-audit ledger** (`TA-rigor-audit-ledger_2026-06-06.md`, PROPOSED, on branch `claude/ta-rigor-audit-260606-f537b4`, **not yet applied to main**) already catalogs every piece of this, in the Option-B direction:

| Audit ID | Finding | Maps to |
|---|---|---|
| **E12** (n36) | §11.6 "three independent methods" overclaim — M2 is the realized-B comparator, not a third RCV estimator | Author Point 2 |
| **E14** (n77/78) | §9.1 "six tested cases" overclaim — 4 empirical + 2 thought-experiments; **and all three models share the SCC input on fossil cases, qualifying the independence defense** | Author Point 1 (the shared-input artifact) |
| **C1** (n3) | §10.2 case-set mismatch — Norway named in the "empirical four"; §9.5 table rows are McDowell/Deepwater/Libby/**Baotou** | the tension I was asked to investigate |
| **B6** | §9.5/§9.6 convergence-ordering narrative contradicts the table | §9.5/§9.6 prose |
| **B7** | §3.5 α-dominance "finding" is a property of the chosen functional form, not empirical | same finger-on-scale class |

**E12 appears already applied** (current §11.6 has no "three independent methods" phrase; grep-clean) — consistent with the 2026-06-10 reverse-CSD merge having picked up the M2-is-bond reframe. The convergence-framing findings (E14, C1, B6) are **not** applied on main.

**Note — the reef migration outdated C1's prescribed fix.** C1 said "swap Norway→Baotou" in the empirical four. Post-reef-migration the census now reads "four forward **empirical**" — and Norway *is* a real empirical case, so the simple swap is now wrong. The correct fix is no longer a name-swap but the **Option-B reframe below** (scope the cross-model claim to where it computes; name each case's actual role). The Option-B reframe supersedes the mechanical C1 swap.

---

## 3. What the corrected prose must do (Option B, mirroring §3.6)

1. **Demote convergence from validation to modest, qualified corroboration.** The result being demonstrated is *independent construction*, not agreement. Agreement where it occurs is corroboration; **divergence is informative, not failure** (§3.6 language).
2. **State the independence limit honestly (E14 / Point 1).** On fossil cases the three models share the social-cost-of-carbon input, so agreement on the carbon-dominated term is a shared-input artifact, not independent confirmation. The genuine independence lives in the *non-overlapping* data sources (substitutability / market volatility / litigation-epidemiology). This is the framework naming its own finger-on-the-scale risk and refusing to lean on it.
3. **Scope the cross-model claim to where all three models actually compute** — McDowell, Deepwater Horizon, Libby (§9.5). Do not assert it across six.
4. **Name each other case's actual role (Point 2-aware):**
   - **Norway (§11.5):** *what's needed* estimated by its **two RCV estimators, M1 (~$161–422/BOE) and M3 (~$96–610/BOE)**, set against *what's been paid* — the **realized bond M2 (~$48/BOE)**, the canonical realized-B₂ exemplar; the gap is the residual CS (reduced via irreversibility-reduction, not eliminated). *(Not "Three Ways of Counting / Methods 1+2+3" — that phrasing re-imports M2 as a co-equal RCV estimator; M2 counts the paid side, M1+M3 estimate the needed side.)*
   - **Baotou (§11.4):** remediation-only floor, IPG not computable on documented inputs; floor alone implies CS > 0.
   - **Asteroid iron / lunar (§13):** RCV integral exercised in the abundance regime (correctly returns RCV ≈ market price) — boundary calibration, not a cross-model IPG comparison.
   - **Reef (§11.12):** the single backward CSD calibration (M1 floor / M2 corroboration; M3 Open).

---

## 4. Drafted replacement prose

HTML entities shown as in-file. These are the **Tier 1** core edits (see §5 for scope tiers).

### §10.2 census — replace the paragraph at line 3546

> `The framework's tested calibration landscape spans seven cases &mdash; four forward empirical (McDowell coal; Norway oil; Deepwater Horizon; Libby vermiculite), two forward thought-experiment scenarios (asteroid mining; lunar regolith &mdash; &sect;13), and one backward calibration (Chesapeake oyster reef &mdash; &sect;11.12) &mdash; but the framework does not treat agreement among the models as the result being demonstrated. The cross-model check proper runs three independent estimating approaches &mdash; the Damage Function (bottom-up cost audit), Real Options (market-referenced option value), and the RCV integral &mdash; and all three are computable only for three of the forward cases: McDowell coal, Deepwater Horizon, and Libby vermiculite (&sect;9.5). For those three the estimates land within one order of magnitude. That consistency is a modest corroboration, not a validation, and the framework states its limit rather than leaning on it: on fossil cases the three approaches share the social-cost-of-carbon input, so agreement on the carbon-dominated term is a shared-input artifact rather than independent confirmation; the load-bearing independence is in the data sources that do not overlap &mdash; materials-science substitutability (RCV), market volatility (Real Options), and litigation-plus-epidemiology (Damage Function) &mdash; and where the approaches diverge, the divergence is treated as informative about what each captures rather than suppressed (&sect;3.6). The remaining cases corroborate along other axes rather than entering the cross-model comparison: Norway's RCV is bounded by its two estimators (Methods 1 and 3) against a far-lower realized bond (Method 2, ~$48/BOE) &mdash; the canonical realized-B&#8322; exemplar, where institutional architecture has reduced but not eliminated CS (&sect;11.5); Baotou's documented inputs support a remediation-only floor rather than a full IPG, and that floor alone implies CS &gt; 0 (&sect;11.4); the asteroid-iron and lunar scenarios exercise the RCV integral in the abundance regime, where it correctly returns RCV &asymp; market price (&sect;13); and the reef exercises the &sect;5.5 Method-1-floor / Method-2-corroboration form with Method 3 deliberately Open, demonstrating the apparatus's backward reach (&sect;11.12).`

### §9.1 — replace the tail of line 3212 (from "correlated measurement error…")

> `correlated measurement error would not consistently produce IPG estimates within one order of magnitude across the three cases for which all three approaches are computable (McDowell, Deepwater Horizon, Libby; &sect;9.5). The independence is partial, and the framework states the limit rather than leaning on it: on fossil cases the three approaches share the social-cost-of-carbon input, so agreement on the carbon-dominated term is not independent confirmation; the genuine data-source independence is in the non-overlapping inputs &mdash; substitutability, market volatility, and litigation/epidemiology &mdash; and the cross-model claim rests on those.`

### §11 intro — replace the over-broad IPG clause at line 4002

> `The three cases with computable IPGs show IPG &gg; 1; all four &sect;9.5-table cases show the same structural pattern (value dispersed, costs concentrated) and B &asymp; 0 relative to RCV, with Baotou entering on its remediation-only floor (&sect;11.4) rather than a full IPG.`

### Do NOT change
§3.6 (1129–1151), symbol registry, §5.5 (1507), §11.5 triangulation, the §9.5 post-table paragraph ("the three cases with computable IPGs…", line 3398), the §11.2 row ("All three models agree within a factor of 1.5", line 4084) — all already Option-B-correct; they are the model.

---

## 5. Scope tiers — author decision

| Tier | Scope | Cascade / risk |
|---|---|---|
| **T1 (recommended floor)** | §10.2 census + §9.1 intro + §11-intro clause, in Option-B language (§4 above). Subsumes audit C1 + E14; adopts Point 1 + Point 2. | Low. Prose-only; no computed figure touched. Three localized paragraph edits. |
| **T2 (+ narrative coherence)** | T1 + reconcile §9.5/§9.6 convergence-ordering narrative to the table (audit **B6**). | Low–med. One more paragraph; keeps §9 internally consistent. |
| **T3 (+ structural reframe)** | T2 + retitle **§9 "Three-Model Convergence Framework"** and **Empirical Observation 10.2 "Cross-Model Convergence"** away from convergence-as-headline (e.g. "Three-Model Cross-Check" / "Cross-Model Consistency"), mirroring §3.6 throughout. | Med. Heading change cascades to TOC (line 237), the §10 theorem list (line 248), and any cross-refs ("Empirical Observation 10.2 (Cross-Model Convergence)" is cited by name). Author-voice-sensitive — naming call. |

**Recommendation: T2.** T1 is the minimum that discharges your two corrections and the two unapplied audit findings (C1, E14); T2 adds the one extra paragraph (B6) needed so §9 doesn't contradict itself line-to-line. **T3 is a genuine naming/structure call I'd rather you make** — the word "convergence" is load-bearing in the headings and cross-referenced; reframing it is right in spirit but is a voice decision, and can be a clean follow-up.

**Open question for you — home of the fix.** Because C1/E14/B6 belong to the held 2026-06-06 audit pass, do you want these applied (a) here, as a standalone Option-B convergence-reframe commit, or (b) folded into that audit pass when it lands, so the convergence findings travel with the rest of the forward-fix batch? Either is clean; (a) ships the reframe now, (b) avoids two passes touching §9/§10.2.

---

## 6. Application checklist (post-ratification — NOT done here)

1. Apply the ratified tier's edits.
2. `check-corpus-invariants.sh --scope … --severity HIGH` → exit 0.
3. `python3 …/csd_rcv_calculations.py` → 0 FAIL (no computed figure is touched; prose-scope/framing only).
4. Confirm no render-glyph regressions (&mdash; / &asymp; / B&#8322;) in edited paragraphs.
5. If T3: update TOC (line 237) + §10 list (line 248) + any "Cross-Model Convergence" name-cites; re-grep for the old heading text.
6. Merge-on-ratification per CLAUDE.md (end-user-facing TA prose).

**Until ratified, no change is applied to the TA HTML. This file is the proposal only.**

---

## 7. v3 (2026-06-11) — unified-triple sunset: settled numbers + S-full edit set

**Verification engine:** `calculations/sec9_recompute_2026-06-11.py` — 24 checked values, 0 mismatches; main engine baseline re-run, 21/21 intact. Every figure below is engine-reproduced from sourced/labeled inputs already in the TA, or explicitly marked retired-no-basis.

### 7.1 The settled §9.5 replacement table

| Case | Method 1 / damage lens (IPG) | Method 3 / premium lens (IPG; price-independent multiple) | RCV-integral lens (IPG) | Realized bond (M2 reading: who paid) |
|---|---|---|---|---|
| McDowell coal | **107–110×** ($504–518 4-component floor ÷ $4.71) | **8.5–26×** (center ~15×) | **61–115×** ($525–540 adopted calibration, across $8.66/$4.71 bases) | $50–88/ton societal vs $8–15/ton industry → **CS ≈ $1,025–1,065/ton** |
| Deepwater Horizon | **~15–16×** documented ($61.6B ÷ ~$4B derived gain; 13–19× across the 40–60M-bbl reserve band); **~17–18×** with the $8–12B ongoing added — *same lens extended, not a second model* | **2.4–5.1×** (oil-class register per §11.5; class-level, not case-derived) | not computable on documented inputs | **$61.6B industry-paid** (litigation-forced) — largest realized industry-paid B₁ in the corpus; CSD − B₁ ≈ $8–12B |
| Libby vermiculite | **≈26×** documented-cash floor ($2.6B ÷ ~$100M; ≈13× if true revenue were 2×); **65–102×** mortality-inclusive (694 deaths × EPA VSL $7.4–11.0M; vintage-labeled) | n/a — extraction ended 1990; forward foreclosure ≈ 0 | not computable on documented inputs | ~$600M Superfund (public) + ~$250M settlements (industry) ≈ 70/30 |
| Baotou rare earths | not computable — remediation-only floor $5–15B (§11.4) | high-ς REE register, ongoing (§11.8); level not case-computable | not computable | ≈ $0 identified |

**No "Convergence ✓" column.** The honest cross-check claims: (a) McDowell is the single case where every forward lens computes, and its lenses legitimately span an order of magnitude (8.5–26× premium vs 107–110× damage floor) because they measure different quantities; (b) no computed lens in any case returns IPG ≤ 1 — direction never flips; (c) Deepwater + Libby are backward-dominant (per the Part-7 bidirectional portfolio): the live quantities are realized damages and who paid; (d) the realized-bond column is the accountability story (industry-paid / 70-30 split / all-public / absent).

**Retired figures (add to `tools/quality-gates/regressed-patterns.yaml`):** McDowell RO "45–89×"; Deepwater RO "12–21×"; Libby RO "57–93×"; Libby RCV-col "72–111×"; Deepwater "RCV model estimate" label on 17–18×; "All three models agree within a factor of 1.5"; "Three-Model Convergence" (post-apply); "across six tested cases" / "across the six forward cases" (scope overclaim).

### 7.2 v3 TA edit set (supersedes v2 §4 where they conflict)

| # | Site | Edit |
|---|---|---|
| E1 | §9 title (3191) + TOC (237, 240) | Retitle away from "Three-Model Convergence Framework" — author voice options in §7.3. TOC description → "Estimator architecture (M1 damage audit + M3 foreclosure premium); the RCV integral; per-case cross-check table; the realized-bond (M2) reading." |
| E2 | §9.1 body (3198–3213) | Replace with the unified-architecture overview + the two-paragraph sunset note (history kept because the correction is instructive: DF = M1's earlier name; RO = pre-rework M3, market-volatility calibration superseded by Path-A, avoided-externalities term double-counted SCC; convergence demoted — "three estimates that always agree is a tell that inputs have been tuned to agree"; direction-never-flips is the claim; shared-SCC caveat (M1-carbon + integral share SCC; M3 contains no SCC and its multiple is price-basis-independent); divergence informative per §3.6; M2 outside the estimator set — RCV ≥ B̂_M2, same observable cannot be estimate and subtrahend). |
| E3 | §9.2 (3215–3228) | Retitle "Method 1: The Damage-Function Audit (bottom-up)"; body stands (floor framing + CIT complement already correct); add "(= Method 1, §3.3)" linkage. |
| E4 | §9.3 (3230–3246) | Retitle "From Real Options to Method 3: the Superseded Calibration"; body → short historical note (intuition survives in M3; volatility calibration + worked-example retired; SCC double-count named; cross-ref §3.5; Brennan & Schwartz kept as lineage). Structural-overlap defense paragraph (3245) deleted — it defends the retired calibration. |
| E5 | §9.4 (3248–3252) | Keep; "The Damage Function and Real Options can capture this cost only approximately" → "Methods 1 and 3 capture this cost only approximately"; add adopted-calibration cross-ref ($525–540; 61–115×; §11.1 note). |
| E6 | §9.5 (3254–3399) | Retitle "Per-Case Cross-Check Table"; replace table with §7.1; replace narrative paragraph (3398) with §7.1's claims (a)–(d). Discharges audit B6 fully (no ordering narrative remains). |
| E7 | §9.6 (3401–3408) | Retitle "The Realized-Bond Reading (Method 2) as Back-Check"; body: what this section called "implicit social pricing" is the §3.4 M2 reading — strict lower bound, not a fourth estimator; selection-bias caveat stands; consistency with the M1 floors says the estimators are not overestimating by orders of magnitude. |
| E8 | §10.2 census (3546) | v2 §4 draft, amended: full three-lens cross-check computes **only for McDowell**; Deepwater + Libby on the damage lens + realized-bond decomposition; Baotou floor-only; thought-experiments = boundary calibration; reef = backward calibration; shared-SCC + tuned-to-agree epistemics sentences retained from v2 draft. |
| E9 | §10.2 independence paragraph (3552) | "Real Options from market volatility data" → unified inputs (M1: litigation/epidemiology/remediation; M3: R/P scarcity + irreversibility record; integral: materials-science substitutability); Hong & Page + Mosteller & Tukey kept, re-scoped to the non-overlapping inputs under partial independence. |
| E10 | Empirical Observation 10.2 name (248 + in-section + any name-cites) | Rename away from "(Cross-Model Convergence)" — options in §7.3; grep all name-cites at apply. |
| E11 | §11.2 (4078–4085) | Relabel "RCV model estimate: ~17–18×" → "Damage-function lens, extended (adding the $8–12B ongoing): ~17–18× — the same lens with ongoing costs added, not an independent model." Replace "Convergence: ✓ All three models agree within a factor of 1.5." → realized-bond statement (industry-paid B₁ $61.6B; CSD − B₁ ≈ $8–12B; oil-class premium register 2.4–5.1×; no case integral). |
| E12 | §11.3 IPG line (4119) | → "≈26× on the documented-cash floor (≈13× if true revenue were twice the industry estimate); ≈65–102× mortality-inclusive (Damage Function; VSL vintage dominates: 2006$ → 65–77×, updated → 78–102×)." RO/RCV figures removed (no surviving derivation); headline aligned to its own sub-bands (65–102×). |
| E13 | Gate hardening | Add §7.1 retired patterns to regressed-patterns.yaml. |
| E14 | Exit gates | `check-corpus-invariants.sh --scope TA --severity HIGH` → 0; both calc scripts → 0 FAIL; glyph check on edited paragraphs; re-grep old heading text after retitles. |

### 7.3 Title options (author voice call — pick at ratification)

- **§9:** (a) "The Cross-Check Architecture" *(recommended)*; (b) "Cross-Checking the Estimate: Lenses and the Realized Bond"; (c) author phrasing.
- **Empirical Observation 10.2:** (a) "Cross-Lens Consistency" *(recommended)*; (b) "Direction Invariance"; (c) "Cross-Model Consistency".

### 7.4 Book-proposal side (Work Item B, unified architecture — final wording)

- **§00 argument clause:** "that what restoration requires can be estimated two independent ways — from the documented damage record, and from the foreclosure premium on the options extraction closes — and read against the bonds actually posted; that the gap between the needed and the paid is large enough, across enough domains, to constitute a material claim about how the economy actually works"
- **§00 Chapter-6 sentence:** "The book argues, and Chapter 6 demonstrates — estimating what restoration requires two independent ways and reading what has actually been paid off the record — that the gap between what extraction has cost and what has been paid runs an order of magnitude or more above the figures normally cited."
- **§00 paragraph close:** end at "Direction never flips across the lenses." (the convergence-celebration sentence deletes).
- **§05 Ch 6 block:** redraft on the same architecture (estimators + integral + realized bond; McDowell lens-explicit; no convergence celebration) — PROPOSED on the session branch.
- **Ch 6 chapter rebuild:** the settled §7.1 numbers + this architecture hand off to the dashboard/plan session that owns the Ch 6 drafting agents (handoff artifact follows ratification).

### 7.5 Downstream cascade (flag, not this session's scope unless routed)

Ch 6 chapter title "Three Ways of Counting" can survive at reader level only if the chapter's triad becomes (two estimates of what restoration requires) + (the record of what was paid) — a Ch-6-rebuild-brief decision, routed to the dashboard session with the numbers handoff.
