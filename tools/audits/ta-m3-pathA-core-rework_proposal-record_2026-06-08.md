# Method-3 forward core — Path-A rework + triangulation reframe — Proposal Record (2026-06-08)

**Status: PROPOSAL — NO TA edits made.** Branch `claude/ta-m3-pathb-260607-6e6849`
(off held `claude/ta-rigor-audit-260606-f537b4`). **Do NOT merge to main.** Each
substantive change below is presented for author ratification before applying.

**Supersedes** the Path-B proposal record (`ta-m3-pathB-rework_proposal-record_2026-06-07.md`):
Path B (drop the multipliers, use the full Dixit–Pindyck premium `M×V_underlying`) was
**rejected** after independent verification. This record is the ratified-direction Path A.

## Provenance discipline (what this rests on)
Built only on (1) the TA file itself, (2) primary external sources, (3) math rederived
here. All prior saturated-session artifacts — the Path-B proposal, the CSD spec, the
audit ledger, their "author-ratified" provenance lines — are treated as **unverified
suggestions**. Findings independently corroborated by the reverse-CSD session's own
re-investigation (`ta-reverse-csd-reef-calibration_proposal-record_2026-06-08.md`,
verification addendum) are flagged ✔-corroborated.

---

## 0. Why Path A, not Path B (decision record)

Path B's headline (`RCV_M3 = M×V_underlying`, M=β/(β−1), β from the D–P quadratic) was
arithmetically correct (β≈1.341, M≈3.93, M×$496≈$1,950 — rederived) but rejected because:

1. **"Double-counts volatility + irreversibility" mischaracterizes the current formula.**
   Current `V_option` is a posited ~market-price base, not D–P-derived, so it embeds no σ/α
   to double-count. The real defect is *posited/mis-specified base + over-hot bespoke amplifier*.
2. **It relocates fragility from the best-grounded parameter to the worst.** The headline
   diverges to ∞ as δ→r; $1,950 hinges entirely on the assumed wedge (r−δ)=0.01, and δ
   (convenience yield of *unmined* coal) has no external anchor and no clear referent for a
   social-preservation option. Meanwhile α=0.85–0.95 is now *well*-corroborated (IPCC AR6
   SPM B.5; Solomon 2009; Bernhardt & Palmer 2011).
3. **It guts the CiT showcase + triangulation independence.** D–P `M×V` removes the
   context-dialing terms that make the asteroid (≈market) and Mars (→civilization-scale)
   demonstrations work, and ties M3's underlying to M1's ceiling.
4. **D–P investment-timing is the wrong tool** for valuing preserved/extinguished optionality
   (Arrow–Fisher/Henry quasi-option value is the apt lineage), and is **meaningless backward**
   (no live option to defer; δ undefined). The full D–P model already lives in the TA as the
   §9 / Empirical Observation 10.2 *Real Options cross-check* (which produces *systematically
   lower* estimates) — so M3 must stay distinct from it. ✔-corroborated (reverse session).

The original Path-B open question "report M×V vs (M−1)×V" is therefore **moot** under Path A.

---

## PART 1 — §3.5 forward core (the intellectual core), before/after

### 1.1 The reframed object
M3 prices the **(quasi-)option value of not foreclosing the commons** (Arrow–Fisher 1974 /
Henry 1974 lineage — preservation under uncertainty + irreversibility), built on the
**resource's own intrinsic/market value** and dialed by two context parameters that carry
the **Commons Inversion Test** into the pricing formula:

```
RCV_M3 = V_option × scarcity_weight(ς) × irreversibility_weight(α)

  V_option            = the resource's own intrinsic value (market / extraction value).
                        In ABUNDANCE this is ~market price (both weights → 1, RCV ≈ market —
                        the asteroid-iron calibration); the SOCIAL premium EMERGES from the
                        two weights under scarcity + irreversibility. (NOT a posited $50–500
                        band; NOT a carbon-SCC anchor — see 1.2.)
  ς  (was σ)          = scarcity weight argument; dimensionless, grounded in the
                        reserves-to-production (R/P) ratio (EIA/EI-BP/USGS). RENAMED from σ
                        (finding A). [SCARCITY dial of the CiT]
  α                   = irreversibility probability ∈[0,1]; direction-grounded high
                        (IPCC AR6 SPM B.5; Solomon 2009; Bernhardt & Palmer 2011).
                        [IRREVERSIBILITY dial of the CiT]

  scarcity_weight(ς)        = 1 + ln(1 + ς) × Hotelling_anchor   (anchor ≈ 0.05)   ["log" → "ln", finding C]
  irreversibility_weight(α) = 1 / (1 − α)        [β fixed = 1; free exponent DROPPED, finding D]
```

### 1.2 The five changes vs. the current §3.5 (line 889ff)

| # | Current | Path A | Drives |
|---|---|---|---|
| **σ-rename** | `σ = scarcity ratio` *inside an option-value product cited to Dixit–Pindyck* — read as VOLATILITY on sight; and stock÷flow is time-dimensioned (units bug) | rename **σ → ς**; define ς as dimensionless normalized R/P; cite EIA/EI-BP/USGS | **Finding A (dismissal-grade).** ✔ registry Part 4. Removes the volatility-collision + units bug. |
| **V_option anchor** | posited `$50–500/ton` (market-price-flavored, unsourced) | **the resource's own market/intrinsic value** (coal: $40–140/ton contemporary by grade, TA L2916; asteroid: ~iron market price). The CiT premium emerges from the weights, not from the base | Fixes the mis-specified/posited base **without** carbon-SCC anchoring (which would double-load scarcity, break the asteroid demo, and break backward CSD). Preserves M3's identity + triangulation independence. |
| **irreversibility form** | `1/(1−α)^β`, free β (β=2 → ×100, an order-of-magnitude swing, L5344) | `1/(1−α)`, **β fixed = 1**, given the *expected-loss-under-irreversibility-probability* interpretation | **Finding D.** Removes the single worst fragility (free β). |
| **dominance relocation** | "α-dominance *finding*": the formula diverges as α→1, presented as a discovered sensitivity result (header L922; implication L1029–1033) | reframe as **weighted, not discovered**: irreversibility is *weighted* heavily (direction grounded by IPCC/B&P); the *dominance* of irreplaceable harm is **theorem-grounded — Thm 10.4 knife-edge (L3677) + Thm 10.5 Substitution Dominance + §13** — not manufactured by the multiplier. The α→1 limit is routed to the existing **§12 incommensurability boundary + ARR** (L6355/6639) | **Finding D + CSD-spec §7 reconciliation.** ✔-corroborated (reverse session: 10.4 divergence is a *feature*; no unpriceability theorem exists). Honors §7's "prices high / divergence = dominates" while killing the tautology. |
| **construct citation** | "standard real-options option value (Dixit–Pindyck 1994)" — implies D–P calibration provenance it does not have | cite **Arrow–Fisher 1974 + Henry 1974** for the *construct* (quasi-option value of preservation; already in bib L7738); flag parameter magnitudes as posited-with-sensitivity (the framework's existing honest posture). Note full D–P lives in the §9 Real Options cross-check | Fixes the "cites D–P but isn't D–P" mismatch without adopting D–P. |

### 1.3 What the core thesis becomes (epistemic status changes; conclusion unchanged)
> Conventional accounting sees only the **market price** — the *abundance assumption baked in*
> (both weights ≈ 1). The Commons Inversion Test reveals that the **same resource**, under true
> scarcity and irreversibility, carries a cost that climbs from market price toward
> civilization-scale. That revealed premium — market price dialed up by scarcity and
> irreversibility — is exactly what is owed (forward as RCV; backward as CSD).

The thesis "irreversibility is the heart of the matter" is **unchanged**; it moves from a
*claimed discovery* (form-manufactured) to a *principled, sourced modeling commitment*
(IPCC/B&P + Thm 10.4/10.5). More defensible, less swagger.

---

## PART 2 — Notation fixes A–E (verified against file + sources)

| Finding | Fix | TA loc | Path-A status |
|---|---|---|---|
| **A — σ misused** | rename σ → ς (above); define units | §3.5 L892, §11.5/11.6/11.8 | core change 1.2 |
| **B — δ freed** | M3 uses **no δ** (Path A); §16.1 δ→κ rename (other branch) just must land on merge so no collision | coordination only | no M3 δ introduced |
| **C — log = ln** | write **ln** (or define "log ≡ ln" once) — `ln(101)=4.615` confirms natural log | L896, 4311, 4761, 5245 | folds into ς weight |
| **D — α-dominance overclaim** | reframe per 1.2 (dominance → Thm 10.4/10.5; drop free β) | §3.5 L922/1029, §11.8 L5063ff | core change 1.2 |
| **E — Solow misattribution** | L917 "Solow 1956 QJE" (growth paper) → **Solow 1974 *Rev. Econ. Stud.*** (intergen. equity; already bib L916/7984) | §3.5 L917 | clean correctness fix |
| β collision | β no longer an M3 free exponent (fixed=1); §16.2 innovation β→ω (other branch) | §3.5 L897 | resolved by 1.2 |

---

## PART 3 — Worked numbers (the dials must behave across the full CiT range)

`scarcity_weight ≈ 1 + ln(1+ς)×0.05 ≈ 1.27–1.31` across the documented R/P range
(insensitive — ≤13% swing, per σ-grounding audit). `irreversibility_weight = 1/(1−α)`.

| Case | V_option (market) | ς-weight | α | irrev-weight | RCV_M3 | Behaves? |
|---|---|---|---|---|---|---|
| **Asteroid iron** (abundance) | ~market iron price | ~1.0 (ς≈1–10) | 0.05–0.2 | ~1.05–1.25 | **≈ market price** | ✓ CiT: RCV≈market (matches L5295) |
| **Mars breathable air** | life-support cost | high | →1 (existential) | → diverges | **→ §12 incommensurability boundary + ARR** | ✓ routed to ARR, not a finite multiplier |
| **McDowell coal (forward)** | $40–140/ton (L2916) | ~1.30 | 0.85–0.95 | 6.67–20 | **$350–3,640/ton; central (≈$90, α=0.9) ≈ $1,170/ton** | ✓ inside M1 range, independently anchored |

**Convergence check (McDowell forward):** M1 replacement-cost = $1,595–2,702 (conservative DAC) /
$812–1,658 (at-scale) / $290–875 (optimistic). Path-A M3 central ~$1,170 lands inside M1's
at-scale band; the M3 band ($350–3,640) overlaps M1 across scenarios. **Convergence holds, and
M3 is now genuinely independent** (anchored to *market price*, not M1's DAC). Sensitivity: result
is driven by **α** (irreversibility weight; disclose the 0.85–0.95 band) and **coal grade**
($40–140) — both externally documented; **no unanchored δ.** Contrast Path B (rested on δ=0.04,
→∞ as δ→r).

---

## PART 4 — Triangulation/convergence reframe (your ratified "bound-range" understanding)

**Framing (ratified):** convergence is **not** proof of the true value; it is a **bound-range +
robustness** result. When the methods agree → robust (not an artifact of one method's bias).
When adversarial input-gaming forces divergence → min→floor, max→ceiling, still a useful bracket;
the floor-anchored **CS > 0** claim survives unless the floor is pushed below the current bond B.
This is the *more defensible* framing — it survives the shared-bias attack (TA already flags it,
L3407) that would sink a "convergence proves truth" claim.

**Forward vs backward = degree, not kind.** Both directions produce `[floor, ceiling]` brackets;
forward tighter (three estimators of one expected quantity), backward wider (more distinct realized
quantities). **Do NOT adopt the CSD spec's "forward point / backward range" dichotomy** — the
reverse session verified it contradicts the symmetry theorems (Thm 10.1b, §17.5) across ~9 sites.

**Overclaim language to soften (verified line cites; direction-neutral, theorem-safe):**

| Line | Current | → soften to |
|---|---|---|
| **3050** (strongest; §9 header) | "**validated through convergence**" | "cross-checked / corroborated by convergence with…" |
| **4877** | accountability gap "**triangulation-confirmed**" | "triangulation-supported" / "robust across all three methods" |
| **4907** | "**empirically grounded by triangulation** across three independent methods" | match the §3.6 "well-supported" register (+ see Part 5) |
| **3064** | "convergence **cannot be explained by shared error structure**" (contradicts L3407) | "cannot be explained by shared **data-source** error structure" + cross-ref the shared-assumption risk at L3407 |

---

## PART 5 — M2 / reframe (c): the Three Ways populate BOTH sides of CS = RCV − B

**E12 verdict (independently confirmed, here and by the reverse session): conceptually right.**
§11.6 literally plugs M2 in *as B* (L4883: "B ~$50–88/ton (M2)") then 24 lines later calls it one
of "three independent methods" estimating RCV (L4907) — it cannot be both.

**Reframe (c) — ratified:** the "Three Ways of Counting" independently populate the identity
**CS = RCV − B**: **M1 + M3 estimate RCV**; **M2 reveals the realized bond B** (forward: Norway's
GPFG = realized B₂, "B₁-for-Norwegians-only", L4218/4261; backward: NRDA/restoration spend =
realized B₁). The **gap is the contribution**. This *keeps* the "three ways" brand, *strengthens*
the accountability-gap claim, and matches your bound-range view (M1/M3 bound RCV; M2 is the bond).
The genuine multi-method robustness ALSO lives in §9's three *models* (Damage Function / Real
Options / RCV-integral) — untouched by E12.

**Forward §11.6 edit (~L4907):** replace "three independent methods [estimating RCV]" with the
(c) framing — two RCV estimators (M1, M3) + M2 as the realized-B reading. **Uniform across
directions.**

> **COORDINATION — RESOLVED by propagation (author-confirmed 2026-06-08):** the reverse-CSD
> session's draft edit **A3** keeps M2 as a *forward estimator / backward comparator* (direction-split)
> and targets the **same ~L4907**. Resolution: **propagate (c)-uniform into the reverse draft** — A3
> drops its forward-estimator half and reads M2 as the realized-B reader **both directions** (forward
> = realized B₂ / Norway; backward = realized B₁ / reef). The CSD draft is explicitly adjustable to
> make the book's parts agree, so this is a coordination edit, not a tension. **What is preserved:**
> M2's "**revealed lower bound on RCV**" role survives — a rational polity internalizes ≤ what it
> values, so realized B is a floor under RCV; (c) delivers that floor signal *as a realized-B reading*
> rather than as an independent RCV point-estimator. We drop the overclaim, not the usefulness. The
> principled-asymmetry note (revealed-preference *could* in principle estimate RCV forward) does not
> match how Norway is actually *computed* (realized capture). Reverse A3 is held → no live collision;
> the edit lands in the reverse draft when that session next touches it (not edited from here).

---

## PART 6 — Bidirectional readiness (foundation for the reverse-model session)

The Path-A formula is **bidirectional-capable by construction**, without hard-wiring the contested
reverse architecture:

- **V_option** — forward: resource's market/intrinsic value; **backward**: value of the
  optionality *extinguished* at extraction (non-renewable stock value) **or** the foregone
  *service flow* (renewable-regeneration cases, e.g. the reef — "the oysters the bar would have
  grown").
- **ς (scarcity)** — forward: current/future R/P; backward: scarcity at the extraction moment.
- **α (irreversibility)** — forward: will foreclosure be reversible; backward: *was* it (often
  better-grounded — observed).

**Deliberately NOT committed here** (left to the reverse-model session's own investigation, since
the CSD spec is itself an unverified suggestion): the point/range asymmetry (rejected — see Part 4),
the ex-post/ex-ante backward fork, the M2 direction-split, the reef numbers.

**Backward-M3 under Path A (symmetric with forward — corrects a Path-B residue):**
`CSD_M3 = V_option(extinguished optionality / foregone service flow) × scarcity_weight(ς at extraction)
× irreversibility_weight(1/(1−α), realized)`. **The multiplier architecture is KEPT in both
directions.** Retiring the multipliers ("a single option premium; no separate scarcity_multiplier ×
irreversibility_premium") was *Path B*, now rejected. Under Path A they do **not** double-count,
because V_option is the *market/intrinsic* base (not a D–P-derived value that already embeds σ/α).
The reverse §5.5 should commit to **no** forward M3 number.

> **⚠ Reconciliation (prose, not numbers):** the reverse draft's §0 flag 1 *and the earlier version
> of this record* described backward-M3 in **Path-B terms** ("single option premium; no separate
> multipliers"). That must be reconciled to the Path-A multiplier framing above when the reverse draft
> is next touched. **No reef numbers change** — the reef bond is M1 cure-cost + M2 realized-B with M3
> *declined* (Open ceiling slot), so it is unaffected by Decisions 1 & 2 regardless.

---

## PART 7 — Coordination flags
1. **Reverse A3 ↔ reframe (c): RESOLVED by propagation** (author-confirmed 2026-06-08) — propagate
   (c)-uniform into the reverse draft (drops A3's forward-estimator half; M2 = realized-B reader both
   directions; preserves M2's "revealed lower bound on RCV" role). Shared ~L4907 (held, no live
   collision); edit lands in the reverse draft when that session next touches it.
1a. **Backward-M3 description (Path-B residue):** the reverse draft's §0 flag 1 describes backward-M3
   as "a single option premium; no separate multipliers" (Path B). Reconcile to the **Path-A multiplier
   architecture** (V_option × ς-weight × irreversibility-weight, both directions; Part 6). Prose only —
   **no reef numbers change** (reef bond = M1 cure-cost + M2 realized-B; M3 declined / Open slot).
2. **Daly §14.6** is being applied by the reverse session (M3-independent; *strengthens* the
   dominance-relocation since corrected Daly = the S_max<1-critical-capital basis). Not edited here.
3. **§9 / Obs 10.2 Real Options cross-check = where full D–P lives.** Keep M3 distinct; do not
   collapse M3 into it.
4. **Bib additions** (M3-rigor: Palmer 2010, Bernhardt & Palmer 2011, Lindberg 2011, Solomon 2009,
   IPCC AR6 SPM B.5, Archer 2009; σ R/P: EIA/EI-BP/USGS; extend Arrow–Fisher/Henry + D–P use-notes):
   coordinate with the provenance-sweep + reverse sessions to avoid duplicate bib edits. Safe and
   path-independent — can land first.
5. **Do NOT merge to main;** commit to branch; sequential reconciliation with parallel TA branches.

## PART 8 — Open items for author
1. **Irreversibility form (the one genuine fork):** drop-β + reframe + relocate-dominance + route-α→1-to-ARR **(recommended)** vs hard-bounded saturating form. (Recommended chosen here.)
2. **Confirm (c)-uniform over reverse A3 direction-split** (Part 5).
3. **Headline presentation:** report McDowell M3 as a **band ($350–3,640) with central ~$1,170**,
   "within M1's replacement-cost range, independently anchored," + α/grade sensitivity. Confirm.
4. **Hand to Ch6/Ch8 drafting sessions** once §3.5 ratified.

## Cross-references
- Superseded: `tools/audits/ta-m3-pathB-rework_proposal-record_2026-06-07.md`
- M3-rigor groundings: `tools/audits/ta-m3-{sigma,alpha,voption}-*_2026-06-07.md`
- Symbol registry: `core/technical-appendix/symbol-registry_2026-06-07.md` (Parts 4–5)
- Reverse-CSD draft (coordinate): `tools/audits/ta-reverse-csd-reef-calibration_proposal-record_2026-06-08.md`
- TA: `core/technical-appendix/TechnicalAppendix_v2.0.0.html` (§3.5 L876, §11.6 L4733/4907, §11.8 L5063, §9/Obs10.2 L3041/3392, Thm 10.4 L3610/3677, §12 L6355)
