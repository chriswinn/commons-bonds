# TA §9 / §10.2 convergence-framing correction — PROPOSED 2026-06-11 (v2, Option-B-corrected)

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
