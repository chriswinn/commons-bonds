# McDowell "33–122×" IPG — archaeology + RETIRE decision record (2026-06-09)

**Status: DIRECTION RATIFIED 2026-06-09 (author: "Ratify retire — I apply TA spots").**
3 of 5 TA spots applied (commit below, MERGE-HOLD). 2 spots (table cells that require a
*value*) flagged open — they cross the recompute boundary the author deferred. Chapter-side
(Ch6/Ch8) handed to the redraft campaign. Branch `claude/ta-m3-resume-260609-151562`.
**Do NOT merge to main.**

**Consolidated to this session** per cross-session handoff (ta-internal-fixes correctness sweep
+ provenance both confirmed non-reproduction and punted the recompute/retire to the M3/integrity
thread because it reaches into Ch6/Ch8 convergence). All claims below independently re-verified
against the TA + Ch6 + Ch8; prior-session conclusions treated as unverified suggestions until
confirmed (Discipline #4).

---

## The problem

A headline "33–122×" McDowell County IPG appears in the TA but reproduces from no consistent
input, and the TA retrofits **four mutually incompatible origin stories** onto it.

### Independent verification (arithmetic)
Current verified inputs: carbon ≈ $496/ton; carbon-inclusive damage floor $504–518/ton (§11.1);
RCV model estimate $580–620/ton (§11.1); 1960 mine-mouth price $4.71/ton (§11.6; still $4.50 in
several un-reconciled spots — cascade half-landed on this branch); contemporary $40–140/ton;
§11.1 also states a period price *range* $4.50–$18/ton.

- carbon $496 ÷ $4.71 = **105×**; ÷ $4.50 = 110×; ÷ $40 = 12×; ÷ $140 = 3.5×
- floor $504–518 ÷ $4.71 = **107–110×**; ÷ contemporary = 3.6–13×
- RCV $580–620 ÷ $4.71 = **123–132×**; ÷ $18 = 32–34×; ÷ $4.50 = 129–138×
- **33× needs a $155 numerator at $4.71** — no input is ~$155. **122× needs ~$575.**
- No single consistent basis yields a **33–122×** *range*. The "33" floor sits **below even the
  §9.5 Real-Options floor (45×)**, contradicting the §9.5 narrative (L3249: DF carbon-dominated;
  RCV highest).

### Where the endpoints actually come from
- **"122" (or "120" — Ch8 prints both, L172 vs L216)** = full carbon-inclusive RCV stack ÷
  1960-nominal price (~113–122×). Reproducible as a *point*, basis-specific.
- **"33"** is **definitional, not computed**: §3.2 (L762) defines "IPG = 33 means the market price
  covers approximately 3% of the true cost" (1/0.03 = 33.3). `block4_validation_2026-04-25.md`
  L115 records 33–122× as "case-file ratified canonical," sourced to "Case-study audit §2.1 +
  terms_index Severed Cost record" — **inherited as a fixed band, never re-derived.** L195 of that
  file already flagged the basis-mixing ("$2,500/$4.50 ≈ 555× mixes 2025 RCV with 1960 nominal").
- The §11.1 envelope (32–138×) only spans "33–122" by **swapping the denominator** between
  endpoints ($18 period-high for the floor, $4.50 1960 for the ceiling) — the mixed-basis artifact.

### Four incompatible origin stories (a range cannot be all four)
1. §14.3 / §16: a **discount-rate** sensitivity span.
2. §11.11: a **lens / price-basis** artifact (carbon ÷1960 inflates ~100×; the era-mixing to avoid).
3. Ch8 L172: "which **cost categories** + which **SCC anchor**."
4. Ch6 L187: "**Method 1 (Replacement Cost) alone**" — falsified by Ch6's own table (M1 $261–2,412
   ÷ $4.50 = 58–536×, ≠ 33–122).

## Decision: RETIRE the bare "33–122×"

Recompute is unavailable (no single consistent basis yields both endpoints). The reproducible,
lens-explicit replacement **already exists in §11.11** and is the model: three lenses on the same
gap, on a consistent basis —
- **M3 foreclosure-premium ~8.5–26× (center ~15×)** — price-independent, most conservative.
- **Carbon-externality lens** — single-to-low-double-digit ÷ contemporary price; ~100× only
  ÷1960-nominal (the era-mixing to avoid).
- **RCV-integral (Weitzman) 67–134×** — the cross-model integral (= §9.5 RCV column).

**Nothing load-bearing depends on the bare number.** CS > 0 and IPG > 1 hold under every lens and
price basis (the conservative without-carbon floor is already 1.8–4.9×; §16 robustness states
IPG ≥ 5×). Retiring removes a non-reproducing, internally-contradicted, internal-ledger-sourced
figure and substitutes the consistent lens framing.

---

## Per-spot disposition

| Spot | Loc | Disposition | Status |
|---|---|---|---|
| §11.1 case IPG | L3888 | Reframed → "~8.5–26× (conservative, price-independent foreclosure-premium), rising to 67–134× under the Weitzman RCV-integral lens; full lens decomposition in §11.11; without-carbon floor under ~5×" | ✅ APPLIED |
| §11.6 reconciliation table | L4493–4505 | **Row deleted.** "Documented IPG — canonical range / ~33–122× / Case-study audit §2.1 + terms_index Severed Cost record" was a non-reproducing *result* sourced to an **internal ledger** (Discipline #3 violation), misplaced in an externally-sourced physical/economic *anchors* table | ✅ APPLIED |
| §14.3 Nordhaus engagement | L6523 | Dropped "(as the McDowell County IPG range of 33–122× demonstrates)"; the true qualitative claim (output sensitive to discount rate) survives | ✅ APPLIED |
| §9.5 cross-model convergence table | L3147 | Damage-Function (IPG) **cell** — needs a *value* (carbon-dominated DF IPG on the table's basis). Retire-to-nothing impossible for a table cell; supplying one is a re-derivation (≈ carbon-inclusive floor $504–518 ÷ 1960 price ≈ 107–110×, which would also fix the table's own incoherence). **Crosses the recompute boundary + the unsettled $4.50/$4.71 denominator.** | ⏳ OPEN — author sub-decision |
| §16 sensitivity table | L7387 | Discount-rate row "IPG Range 33× to 122×" — needs the *actual* RCV-integral IPG at r=5.5% vs r=1.4% on one price basis (a recompute). | ⏳ OPEN — author sub-decision |

### Open sub-decision (§9.5 + §16)
Both are table cells; a cell cannot be retired to nothing. Options for each:
- **(A) Re-derive on a stated single basis** — §9.5 DF ≈ carbon-inclusive floor ÷ 1960 price
  (~107–110× @ $4.71; coheres the table: DF 107–110 between RO 45–89 and RCV 67–134, convergence
  ✓ holds). §16 discount-rate row ≈ recompute RCV-integral at the two rates (likely in the 67–134×
  neighborhood). *This is the recompute the author deferred — needs explicit go + the settled
  price basis from the closeout.*
- **(B) Restructure** — §9.5: replace the DF cell with the carbon-lens figure + an explicit
  basis footnote; §16: relabel the row to the RCV-integral discount-rate span.
- Recommendation: **(A)** once the $4.50→$4.71 cascade reconciliation lands (closeout), since (A)
  also repairs the §9.5 narrative-vs-table incoherence. Until then, leave the two cells flagged
  rather than mint a number on an unsettled denominator.

## Chapter-side (handed to the redraft campaign — NOT edited here)
- **Ch8**: L172 "120" vs L216 "122" internal inconsistency; "which cost categories + SCC anchor"
  origin story; the bare 33–122× headline → lens-explicit per §11.11.
- **Ch6**: L173 table row; L187 "Method 1 alone" claim (falsified by Ch6's own M1 $261–2,412 row).
- These are end-user-facing chapter prose; route through the redraft campaign + author ratification.

## Also noted (not retired here)
- §3.2 L762 "IPG = 33 means market covers ≈3%" is a **generic definitional illustration**, not a
  McDowell claim — left as-is (though the choice of "33" is the likely seed of the McDowell floor;
  flag for the redraft campaign if it wants a non-McDowell-colliding example).
- The §11.6 "1960 price $4.71/ton | Ch 6 convergence table" row sources the price to an internal
  table; the price itself is EIA-sourceable (bib §23.1). Minor; not in retire scope.

## Cross-references
- Whole-TA scaffolding findings (same session): `tools/audits/ta-whole-TA-internal-scaffolding-rescan_findings_2026-06-09.md`
- Session-D closeout handoff: `tools/workstream-handoffs/ta-m3-pathA-SESSION-D-closeout-handoff_2026-06-09.md`
- ta-internal-fixes provenance flag: `tools/workstream-handoffs/paste-to-IPG-owners_33-122x-provenance-flag_2026-06-09.md` (on the correctness-sweep held branch)
- §11.11 (the replacement model): TA L6196–6222.
