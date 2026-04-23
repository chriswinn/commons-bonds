# RCV Block 2 — Triangulated RCV Estimation Framework — April 19, 2026

**Status:** Pending review

**Source:** April 19, 2026 session, File 2 (`archive/Consider Including/commons_bonds_new_material_april_19_2026 - Placeholder to consider for inclusion 2.html`), Block 2. Captured 2026-04-23 as a per-section pending-review item in `alignment/decisions/`.

**Integration target (if accepted):** Ch. 6 (Three Ways of Counting) + Technical Appendix RCV formal-model section. Companion to `april-19-rcv-two-instrument-distinction.md` (Block 1), `april-19-rcv-hotelling-identity.md` (Block 3), `april-19-rcv-validation-strategy.md` (Block 4).

**Priority:** High — this is the RCV formal-model session's formal-model proposal.

---

**Core problem restated:** RCV is the permanent foreclosure cost — what's lost forever when a non-renewable resource unit is extracted, beyond what the market price captures. Pricing permanent foreclosure naively requires summing value across infinite future generations, making the answer almost entirely dependent on the discount rate — a moral parameter masquerading as a mathematical one. The goal is to build something that either sidesteps the discount rate problem or makes its role explicit and bounded rather than determinative.

**Strategy:** Three independent methods approaching the same quantity from different directions. If they converge, the number is robust. If they diverge, the divergence reveals exactly where the real disagreements live.

## Method 1: Replacement Cost (Lower Bound)

What would it cost to provide the same service from the next-best source?

```
RCV_min per unit = Replacement cost from nearest substitute − Market price at extraction
```

If a barrel of oil sold for $80 and the equivalent energy from synthetic or renewable sources would cost $200, then RCV_min is at least $120/barrel. Calculable today with existing data for most major resources.

Why it's a *lower* bound: it only captures substitutable value. If the resource has non-substitutable properties (unique chemical compounds, irreplaceable geological functions, uses not yet invented), replacement cost understates the loss. It prices what we know we're losing, not what we don't yet know we'll need.

**Boundary check:** Sand (highly substitutable, abundant) → replacement cost gap near zero → correct, low RCV. Helium (essentially non-substitutable for cryogenics and superconductor applications, finite, no synthetic production) → replacement cost effectively infinite for those uses → correct, severe and poorly priced permanent foreclosure. The method differentiates appropriately.

## Method 2: Revealed Preference via Norway Calibration (Middle Estimate)

Norway's sovereign fund is the closest real-world attempt at capturing residual commons value. Rather than arguing about what the number should be, look at what one country actually captured when it behaved as if permanent foreclosure mattered.

```
Norway's fund value attributable to petroleum ÷ Total barrels extracted to date = Per-barrel captured value

For any comparison case:
Value retained in community per unit extracted = Per-unit retained value

Gap = Per-barrel Norway capture − Per-unit comparison retention = Empirical measure of uncaptured RCV
```

**Why this is powerful:** It completely sidesteps the discount rate debate. You're pointing at a real country, real money, real outcomes. The difference is a number, not a philosophy argument.

**Why it's a middle estimate rather than an upper bound:** Even Norway didn't fully capture RCV. They still extracted the oil. The fund converts financial proceeds into a durable instrument, but it doesn't price the permanent environmental loss or the option value of unknown future uses. The fund's value represents what Norway captured — more than almost anyone else — but still a subset of total RCV.

**Envelope calculation:** Norway has extracted roughly 10–11 billion barrels of oil equivalent since production began. The fund is worth roughly $1.9 trillion (though not all attributable directly to oil revenue — a significant portion is investment returns). Rough envelope: $170–190 per barrel equivalent in accumulated fund value. Compare to what an Appalachian coal community retained per ton extracted — essentially nothing, or in many cases negative value (Superfund liability, health costs, economic collapse). The gap is enormous and directionally correct.

## Method 3: Scarcity-Adjusted Option Value (Theoretical Upper Bound)

A barrel of oil has value beyond its current use because (a) it might be needed for something we can't yet predict (option value), and (b) as the total stock depletes, each remaining unit becomes more valuable (scarcity rent). Neither is fully captured by market price.

```
rcv(t) = [C_replace(t) − p(t)] + V_option(t) × (1 − σ) × (R / S(t))^α

Where:
- C_replace(t) = cost of nearest substitute at time t
- p(t)        = market price
- V_option(t) = estimated option value for unknown future uses
- σ ∈ [0,1]   = substitutability parameter (1 = perfect substitute exists, 0 = nothing can replace it)
- R           = total original recoverable stock
- S(t)        = remaining stock at time t
- α > 0       = governs how steeply RCV rises as depletion progresses
- R/S(t)      = inverse depletion ratio (equals 1 when nothing extracted, approaches infinity as resource runs out)
```

Two components: the first term is the replacement cost gap from Method 1 (the floor). The second term adds scarcity-adjusted option value, increasing with depletion and decreasing as substitutability improves.

**Boundary checks:**

*Early-stage oil extraction (~1920):* S(t)/R ≈ 1, so R/S(t) ≈ 1, scarcity term small. No real substitutes (σ low), but depletion negligible. RCV moderate — mainly option value and replacement cost gap. Sensible.

*Present-day oil:* Conventional reserves roughly half depleted, R/S(t) ≈ 2. Substitutes exist but aren't perfect (σ moderate, 0.4–0.6). RCV meaningfully higher than in 1920. Sensible.

*Near-depletion:* S(t) → 0, R/S(t) → very large. Even with moderate σ, scarcity term dominates. RCV per barrel extremely high. Sensible — the last barrels of oil on Earth should have enormous residual commons value.

*Highly substitutable resource (commodity sand):* σ → 1. The (1−σ) term zeroes out. RCV ≈ replacement cost gap, which is small. Correct.

*Non-substitutable resource (helium):* σ → 0. Full scarcity term applies. Even at moderate depletion, RCV is high. Matches reality — physicists have warned about helium depletion for decades because no substitute exists for many applications.

**Problems with Method 3:** Requires estimating σ (substitutability) and V_option (option value for unknown future uses), both fundamentally about predicting future technology. However, you don't need point estimates — calculate RCV across a plausible range and present as a confidence interval. The spread of the interval is itself informative. V_option can be bounded by historical analogy (oil was initially valued for lamp fuel; its value as petrochemical feedstock, transportation fuel, and plastics precursor was unanticipated option value).
