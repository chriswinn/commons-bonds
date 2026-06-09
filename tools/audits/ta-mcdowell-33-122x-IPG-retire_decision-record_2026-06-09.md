# McDowell "33–122×" IPG — archaeology + RETIRE decision record (2026-06-09)

**Status: RATIFIED + APPLIED 2026-06-09.** All 5 TA spots resolved (3 retired + 2 table cells
re-derived on $4.71 per author "Re-derive now"). Zero bare "33–122×" remain in the TA.
Chapter-side (Ch6/Ch8) handed to the redraft campaign. MERGE-HOLD. Branch
`claude/ta-m3-resume-260609-151562`. **Do NOT merge to main.**

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
| §9.5 cross-model convergence table | L3147 | DF (IPG) cell re-derived → **107–110×** = carbon-inclusive damage floor $504–518 (§11.1) ÷ 1960 price $4.71. Coheres the table (RO 45–89 < DF 107–110 ⊂ RCV 67–134; RCV retains the highest ceiling, matching the L3249 narrative; convergence ✓ holds). | ✅ APPLIED |
| §16 sensitivity table | L7387 | Discount-rate row "IPG Range" re-derived → **67× to 134×** = the §11.11-verified RCV-integral range (the Weitzman declining rate is the integral's discount mechanism, so the RCV-integral IPG span is the appropriate discount-sensitivity figure). §16 robustness floor "IPG ≥ 5×" unchanged. | ✅ APPLIED |

### §9.5 + §16 re-derivation note (author: "Re-derive now on $4.71", 2026-06-09)
Both are table cells (a cell cannot be retired to nothing); both re-derived on reproducible,
§11.11-consistent, verified numbers — neither minted:
- **§9.5 DF = 107–110×** is a direct computation ($504–518 ÷ $4.71 = 107.0–110.0×). It also repairs
  the table's prior incoherence (the retired "33" floor sat *below* the Real-Options floor of 45).
- **§16 discount-rate row = 67–134×** reuses the verified §11.11 RCV-integral range rather than a
  freshly-computed r=5.5%/1.4% pair (the underlying RCV-integral model is not re-run here); this is
  the RCV-based IPG whose primary driver is the Weitzman discount rate. The other §16 rows (S_max,
  SCC, externality tail) are untouched; the multi-parameter-conservative envelope (IPG ≥ 5×) is
  unaffected. **NB for the closeout:** these two cells now sit on $4.71; if the closeout settles the
  global price differently, re-check §9.5 (the only basis-sensitive one — §16 is price-independent
  via the RCV-integral).

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
