#!/usr/bin/env python3
"""
Commons Bonds Technical Appendix — calculation engine (2026-06-10)

Forward direction:  RCV via the Three Ways (M1 / M2 / M3 Path-A) + the §3.1
                    RCV integral (Def 1.6) under Weitzman declining discount.
Backward direction: CSD (Cost Severance Damages) via the same apparatus run in
                    reverse, with the Chesapeake oyster-reef restitution case
                    as the worked example.

Disciplines honored (per CLAUDE.md + session carry-forwards):
  * Every constant is sourced (TA line / external authority) or labeled
    ASSUMPTION. No posited number typeset to look sourced.
  * Reef backward-M3 is implemented as machinery but deliberately NOT
    evaluated for the reef ("bond only the unassailable floor",
    author decision 2026-06-08). The Open slot is a choice, not a gap.
  * M2 is computed as the realized-Bond reading in both directions
    (matches landed §11.5/§11.6; the §3.4/§3.6 relabel is pending the
    author's architecture decision — the NUMBERS are identical either way).

Outputs are grouped:
  [REPRODUCTION]   recomputes a landed TA number from its stated inputs;
                   any mismatch is flagged.
  [RECONSTRUCTION] computes a TA number whose full calibration is not
                   documented in the TA; assumptions are labeled.
  [REVERSE]        the CSD-side calculations (new work, for ratification).

Stdlib only. Run: python3 csd_rcv_calculations.py
"""

import math

PASS = "ok"
results = []


def check(label, computed, expected_lo, expected_hi, unit, kind="REPRODUCTION"):
    """Record a computed value against the landed TA band."""
    ok = expected_lo <= computed <= expected_hi
    results.append((kind, label, computed, expected_lo, expected_hi, unit, ok))
    flag = "PASS" if ok else "** MISMATCH **"
    print(f"[{kind}] {label}: {computed:,.1f} {unit} "
          f"(TA: {expected_lo:,.0f}-{expected_hi:,.0f}) {flag}")
    return ok


# =====================================================================
# PART 1 — FORWARD: Method 3 Path-A core (TA §3.5, L889-898)
#   RCV_M3 = V_market × scarcity_multiplier(ς) × irreversibility_premium(α)
#   scarcity_multiplier(ς)      = 1 + ln(1 + ς) × Hotelling_anchor
#   irreversibility_premium(α)  = 1 / (1 − α)
# =====================================================================

HOTELLING_ANCHOR = 0.05  # §3.5: posited 5%/yr calibration (Hotelling-rent
                         # tradition long-run-interest-rate proxy) — a
                         # calibration parameter, not an external datum.


def scarcity_multiplier(sigma_f: float) -> float:
    """ς-weight; ς is the R/P-grounded scarcity parameter (final sigma)."""
    return 1.0 + math.log(1.0 + sigma_f) * HOTELLING_ANCHOR


def irreversibility_premium(alpha: float) -> float:
    """1/(1−α); no free exponent (β retired, M3 rework 2026-06-08)."""
    if not 0.0 <= alpha < 1.0:
        raise ValueError("alpha in [0,1); α→1 is handed to §12 ARR, "
                         "not priced by this multiplier")
    return 1.0 / (1.0 - alpha)


def rcv_m3(v_market: float, sigma_f: float, alpha: float) -> float:
    """Forward Method 3 (Path A). v_market = resource's own intrinsic
    (market/extraction) value; the social premium emerges from the weights."""
    return v_market * scarcity_multiplier(sigma_f) * irreversibility_premium(alpha)


print("=" * 72)
print("PART 1 — FORWARD M3 PATH-A REPRODUCTIONS")
print("=" * 72)

# --- Norway petroleum (§11.5, landed values L4293-4333) ---
# central: ς=100, α=0.65, V_market=$80 market crude → ≈$281/BOE
check("Norway M3 central (ς=100, α=0.65, V=$80)",
      rcv_m3(80, 100, 0.65), 275, 285, "$/BOE")
# low corner: V=$40 crude, ς=50, α=0.50 → ≈$96/BOE
check("Norway M3 low corner (ς=50, α=0.50, V=$40)",
      rcv_m3(40, 50, 0.50), 92, 100, "$/BOE")
# high corner: V=$120 crude, ς=200, α=0.75 → ≈$610/BOE
check("Norway M3 high corner (ς=200, α=0.75, V=$120)",
      rcv_m3(120, 200, 0.75), 600, 615, "$/BOE")

# --- McDowell coal (§11.6, landed band $340–3,670, geo center ~$1,115) ---
# coal grade $40–140/ton contemporary (TA L2916 basis); α 0.85–0.95.
# The TA documents McDowell's scarcity_multiplier DIRECTLY as ≈1.27–1.31
# across the R/P register (L4733/L4749) — coal R/P is centuries, so the
# implied ς ≈ 220–490 (1 + ln(1+ς)×0.05 inverted). Use the documented
# multiplier band, not Norway's oil-register ς.
MCD_MULT_LO, MCD_MULT_HI = 1.27, 1.31
mcd_low = 40 * MCD_MULT_LO * irreversibility_premium(0.85)
mcd_high = 140 * MCD_MULT_HI * irreversibility_premium(0.95)
# cross-check the implied ς round-trips through the formula:
sigma_lo = math.exp((MCD_MULT_LO - 1) / HOTELLING_ANCHOR) - 1   # ≈ 220
sigma_hi = math.exp((MCD_MULT_HI - 1) / HOTELLING_ANCHOR) - 1   # ≈ 490
assert abs(scarcity_multiplier(sigma_lo) - MCD_MULT_LO) < 1e-9
assert abs(scarcity_multiplier(sigma_hi) - MCD_MULT_HI) < 1e-9
check("McDowell M3 low corner (V=$40, mult=1.27, α=0.85)", mcd_low, 330, 350, "$/ton")
check("McDowell M3 high corner (V=$140, mult=1.31, α=0.95)", mcd_high, 3500, 3700, "$/ton")
# geometric center (convexity-aware, per §11.6 decision record)
mcd_geo = math.sqrt(mcd_low * mcd_high)
check("McDowell M3 geometric center", mcd_geo, 1080, 1150, "$/ton")

# --- McDowell M3-IPG (premium-multiple basis: RCV_M3 / V_market) ---
check("McDowell M3-IPG low (340/40)", mcd_low / 40, 8.0, 9.0, "x")
check("McDowell M3-IPG high (3670/140)", mcd_high / 140, 25.0, 27.0, "x")
check("McDowell M3-IPG center (geometric)",
      math.sqrt((mcd_low / 40) * (mcd_high / 140)), 14.0, 16.0, "x")

# --- Norway M3-IPG ~2.4–5.1× (§11.5 L4215) ---
check("Norway M3-IPG low (96/40)", rcv_m3(40, 50, 0.50) / 40, 2.3, 2.5, "x")
check("Norway M3-IPG high (610/120)", rcv_m3(120, 200, 0.75) / 120, 4.9, 5.2, "x")


# =====================================================================
# PART 2 — FORWARD: M1 / M2 anchors (sourced constants, not computed here)
# =====================================================================

print()
print("=" * 72)
print("PART 2 — FORWARD M1 / M2 ANCHORS (sourced)")
print("=" * 72)

# M1 Norway: $161–422/BOE replacement-cost floor (§11.5 landed; DAC-anchored)
NORWAY_M1 = (161, 422)        # $/BOE — TA §11.5 (landed)
# M2 Norway: GPFG NOK 21,268B end-2025 (NBIM) ≈ $2.0T at ~75% capture
# → ~$2.67T petroleum wealth ÷ ~55B BOE ≈ $48/BOE (§3.4/§11.5)
GPFG_USD_T = 2.0              # NBIM Annual Report 2025 (FX-dependent)
CAPTURE_RATE = 0.75           # §3.4: ~70-80% state capture; midpoint
CUM_PRODUCTION_BBOE = 55      # Norwegian Offshore Directorate
norway_m2 = GPFG_USD_T * 1e12 / CAPTURE_RATE / (CUM_PRODUCTION_BBOE * 1e9)
check("Norway M2 realized-B reading (GPFG-derived)", norway_m2, 46, 50, "$/BOE")

# Norway implied CS: (RCV center − realized B) × cumulative production
# RCV center: M1∩M3 overlap region; M3 central $281 (above), M1 $161-422.
norway_cs_per_boe = rcv_m3(80, 100, 0.65) - norway_m2
norway_cs_total_T = norway_cs_per_boe * CUM_PRODUCTION_BBOE * 1e9 / 1e12
check("Norway implied CS per BOE (M3-central − M2)",
      norway_cs_per_boe, 225, 240, "$/BOE")
print(f"[RECONSTRUCTION] Norway cumulative CS: ${norway_cs_total_T:.1f}T "
      f"(§3.6 table says ~$12.5T; §11.6-region prose says $13-15T — "
      f"computed {norway_cs_per_boe:,.0f} × 55B BOE; the two TA spots "
      f"disagree with each other; flag for the §3.6 recompute)")

# McDowell M2: realized B $50-88/ton societally-paid; $8-15/ton industry-paid
# (§11.6 landed; Black Lung Trust Fund + reclamation bonds + settlements)
MCD_M2_SOCIETAL = (50, 88)    # $/ton — TA §11.6 (landed)
MCD_M2_INDUSTRY = (8, 15)     # $/ton — TA §11.6 (landed)
# McDowell CS at M3 geo center vs societal realized B:
mcd_cs_lo = mcd_geo - MCD_M2_SOCIETAL[1]
mcd_cs_hi = mcd_geo - MCD_M2_SOCIETAL[0]
check("McDowell CS (M3 geo-center − realized B band) low",
      mcd_cs_lo, 1020, 1045, "$/ton")
check("McDowell CS (M3 geo-center − realized B band) high",
      mcd_cs_hi, 1045, 1070, "$/ton")


# =====================================================================
# PART 3 — FORWARD: the §3.1 RCV integral (Def 1.6), numerically
#   RCV = ∫ {[1−S(t)]·U(R,t,Q) + E(R,t)} · D(t,t₀) dt
#   S(t) = S_max·(1−e^{−λ(t−t₀)})          (Def 1.2 tractable form)
#   D(t) = exp(−∫r(s)ds), r declining       (Def 1.5, Weitzman 2001)
# Status: RECONSTRUCTION. The TA reports the integral-lens results
# ($580-620/ton; IPG 67-134× across discount rates, §11.1/§16.4) but does
# not document the full U/E calibration. Assumptions below are labeled.
# =====================================================================

print()
print("=" * 72)
print("PART 3 — FORWARD RCV INTEGRAL (Def 1.6) — RECONSTRUCTION")
print("=" * 72)


def weitzman_r(t, r0, r_inf=0.02, half_life=50.0):
    """ASSUMPTION: r declines exponentially from r0 toward r_inf with a
    50-yr half-life (a standard declining-rate gamma-approx shape).
    The TA states the Weitzman framework but not the decline schedule."""
    return r_inf + (r0 - r_inf) * math.exp(-math.log(2) * t / half_life)


def rcv_integral(r0, s_max=0.85, lam=0.05, u_flow0=None, p=75.0,
                 e_pulse=496.0, e_other=15.0, tail_years=200.0,
                 horizon=600.0, dt=0.25):
    """Numerical RCV per ton.

    U calibration (ASSUMPTION, labeled): U(t) = r(t)·P — Def 1.3's lower
      bound taken as the operative flow (conservative: the bound, not more).
    E calibration: the $496/ton carbon term (EPA SCC $190 × 2.61 tCO2/ton,
      §11.1) is ALREADY a present value, so it enters as a t=0 pulse, not
      a flow to be discounted again. The non-carbon $8-22/ton (§11.1
      damage-floor components, central ~$15) is spread uniformly over the
      200-yr externality tail (§16.4 baseline) and discounted.
    """
    total = 0.0
    integral_r = 0.0
    t = 0.0
    while t < horizon:
        r_t = weitzman_r(t, r0)
        integral_r += r_t * dt
        d = math.exp(-integral_r)
        s = s_max * (1.0 - math.exp(-lam * t))
        u = r_t * p                       # Def 1.3 lower bound as flow
        e_flow = (e_other / tail_years) if t < tail_years else 0.0
        total += ((1.0 - s) * u + e_flow) * d * dt
        t += dt
    return total + e_pulse               # SCC pulse added undiscounted (PV)


rcv_4 = rcv_integral(r0=0.04)
print(f"[RECONSTRUCTION] RCV integral @ r0=4% (baseline): "
      f"${rcv_4:,.0f}/ton  (TA §11.1: $580-620/ton)")
rcv_14 = rcv_integral(r0=0.014)   # Stern
rcv_55 = rcv_integral(r0=0.055)   # Nordhaus
print(f"[RECONSTRUCTION] RCV integral @ r0=1.4% (Stern): ${rcv_14:,.0f}/ton")
print(f"[RECONSTRUCTION] RCV integral @ r0=5.5% (Nordhaus): ${rcv_55:,.0f}/ton")

# IPG under the integral lens, on the $4.71/ton 1960 mine-mouth basis
# (§16.4 row 1: 67× to 134× across r0 1.4%-5.5%; re-derived on $4.71
#  per commit c8080de)
P_1960 = 4.71
print(f"[RECONSTRUCTION] IPG integral-lens @ Stern: {rcv_14/P_1960:,.0f}x ; "
      f"@ Nordhaus: {rcv_55/P_1960:,.0f}x  (TA §16.4: 67-134x)")
print("  NOTE: the reconstruction brackets the TA band only under the")
print("  labeled assumptions (U = r·P bound; SCC-as-pulse; 200-yr tail).")
print("  The TA does not document its integral calibration — finding for")
print("  the provenance pass: §11.1's $580-620 and §16.4's 67-134x need")
print("  a documented parameterization to be reproducible.")

# Knife-edge demonstration (Thm 10.4 corollary): S_max<1, summable r → ∞
print()
print("[DEMO] Thm 10.4 knife-edge: with S_max<1 and r(s) summable")
print("  (∫r ds < ∞ → D_∞ > 0), the foreclosure integrand has a positive")
print("  floor forever → RCV diverges. Numerically: partial sums at")
for h in (100, 1000, 10000):
    # r(s) = 0.04·e^{-s/20} is summable (∫ = 0.8 → D_∞ = e^{-0.8} ≈ 0.45)
    total, integral_r, t, dt = 0.0, 0.0, 0.0, 1.0
    while t < h:
        r_t = 0.04 * math.exp(-t / 20.0)
        integral_r += r_t * dt
        d = math.exp(-integral_r)
        s = 0.85 * (1.0 - math.exp(-0.05 * t))   # S_max = 0.85 < 1
        total += (1.0 - s) * (0.02 * 75.0) * d * dt
        t += dt
    print(f"    horizon {h:>6,} yr → partial RCV ${total:,.0f}/ton (grows without bound)")


# =====================================================================
# PART 4 — REVERSE: the CSD model (backward direction)
#
#   CSD_M1 (remediation / cost-to-cure)  = foreclosed extent × realized
#                                          restoration unit-cost  → FLOOR
#   CSD_M2 (revealed restitution)        = reads realized B₁ (who paid,
#                                          how much) + corroborates M1's
#                                          unit cost. NOT a third estimator.
#   CSD_M3 (extinguished option value)   = V_market(extinguished optionality /
#                                          foregone service flow) ×
#                                          scarcity_multiplier(ς at extraction) ×
#                                          irreversibility_premium(α realized)
#                                          → admittable CEILING variable.
#   Identity: total CS = (CSD − B₁) + (RCV − B₂)     [§1.7 canonical form]
#   Three states of a slot: ZERO (CIT toggle) ≠ FILLED ≠ OPEN.
#   An OPEN admitted slot ⇒ computed CSD is a LOWER BOUND (sum missing a
#   non-negative term) — not zero, not unpriceable.
# =====================================================================

print()
print("=" * 72)
print("PART 4 — REVERSE CSD MODEL + CHESAPEAKE REEF WORKED CASE")
print("=" * 72)


def csd_m1_floor(foreclosed_units: float, cure_cost_per_unit: float) -> float:
    """Backward Method 1: cost-to-cure floor. Mirrors forward M1
    (replacement cost) with the temporal direction reversed: forward
    prices engineering a substitute; backward prices repairing the
    realized loss. Every input must be documented+realized."""
    return foreclosed_units * cure_cost_per_unit


def csd_m3(v_extinguished: float, sigma_f_at_extraction: float,
           alpha_realized: float) -> float:
    """Backward Method 3 (Path-A multiplier form, mirrored).
    v_extinguished = extinguished optionality / foregone service flow
    (the backward reading of V_market — §3.5 base, M3-rework Part 6).
    Exposes — does not settle — the ex-post (realized value;
    strict-liability reading) vs ex-ante (correct-value-at-t₀;
    negligence reading) fork: the caller chooses which v to enter.
    IMPLEMENTED BUT NOT EVALUATED for the reef (author decision
    2026-06-08: 'bond only the unassailable floor')."""
    return rcv_m3(v_extinguished, sigma_f_at_extraction, alpha_realized)


# --- Reef worked case (all inputs external-sourced; see provenance) ---
# Foreclosed extent: James River high-quality oyster-rock, 1910→1981:
#   7,047 ac → 4,309 ac = 2,738 ac lost (Schulte 2017, Front. Mar. Sci.
#   4:127, citing Moore 1910 / Haven et al. 1981). AREA basis, not shell
#   volume (Darling shell-mountain stays narrative).
REEF_FORECLOSED_AC = 2738

# Restoration unit costs (NOAA Fisheries per-tributary table, Dec 31 2024;
# Great Wicomico Tributary Plan §5):
UNIT_REALIZED = 907_000 / 124          # Great Wicomico realized $/ac
UNIT_FORWARD_ENG = 13_500              # construction-only, natural recruitment
UNIT_BAYWIDE_AVG = 77_000              # completed-program avg (constr+seed)

check("Reef unit-cost: Great Wicomico realized ($907K/124ac)",
      UNIT_REALIZED, 7250, 7350, "$/ac", kind="REVERSE")

floor_realized = csd_m1_floor(REEF_FORECLOSED_AC, UNIT_REALIZED)
floor_headline = csd_m1_floor(REEF_FORECLOSED_AC, UNIT_FORWARD_ENG)
central_robust = csd_m1_floor(REEF_FORECLOSED_AC, UNIT_BAYWIDE_AVG)

check("Reef CSD_M1 floor (realized basis)", floor_realized / 1e6,
      19.9, 20.1, "$M", kind="REVERSE")
check("Reef CSD_M1 floor (forward-engineering headline)", floor_headline / 1e6,
      36.9, 37.1, "$M", kind="REVERSE")
check("Reef CSD central (bay-wide average; robust, not the floor)",
      central_robust / 1e6, 210, 212, "$M", kind="REVERSE")

# --- M2: revealed restitution (realized B₁ reading + corroboration) ---
# Realized public spend: >$92M MD (MD DNR / Gov. Moore, Aug 26 2025);
# ~$115.29M itemized bay-wide (NOAA: MD $93.52M + VA $21.77M); $108M
# program-level (MEDIUM confidence; rounding corroborator only).
B1_REALIZED_MD = 92e6
B1_ITEMIZED_BAYWIDE = 93.52e6 + 21.77e6
B1_INDUSTRY = 0.0          # all funders public (NOAA, USACE, MD DNR, VMRC)

m2_unit_read = 108e6 / 1900   # program-level ÷ actively-restored acres
check("Reef M2 unit-cost corroboration ($108M/1,900ac)",
      m2_unit_read, 56_000, 58_000, "$/ac", kind="REVERSE")
corroborates = UNIT_FORWARD_ENG < m2_unit_read < UNIT_BAYWIDE_AVG
print(f"[REVERSE] M2 corroboration: ${m2_unit_read:,.0f}/ac sits between the "
      f"$13,500 floor and the $77,000 average → "
      f"{'CORROBORATES the M1 unit-cost band' if corroborates else '** FAILS **'}")
print(f"[REVERSE] Realized B₁: >${B1_REALIZED_MD/1e6:.0f}M (MD) / "
      f"~${B1_ITEMIZED_BAYWIDE/1e6:.0f}M (bay-wide itemized) — "
      f"industry contribution ${B1_INDUSTRY:.0f}. The bond exists, is large, "
      f"and is mis-assigned to the public.")

# --- M3: named, not priced (the Open slot, by design) ---
print("[REVERSE] Reef CSD_M3 (foregone-fishery option value): OPEN slot —")
print("  admittable ceiling variable, deliberately not entered (author")
print("  decision 2026-06-08). The machinery above (csd_m3) is fully")
print("  specified; a party with reason to enter the slot can compute it.")
print("  Consequence (pure arithmetic): the computed CSD is a LOWER BOUND.")
print("  NOTE: the reef is restorable → low realized α → modest 1/(1−α);")
print("  backward-M3 does its real work on high-irreversibility legacy")
print("  cases, not here. Declining the figure costs the reef case little")
print("  and buys floor-anchored unassailability.")

# --- The reef CSD range summary ---
print()
print("[REVERSE] Reef CSD structured range (the §5.5 floor/ceiling form):")
print(f"    CSD_floor   = ${floor_realized/1e6:.0f}M-${floor_headline/1e6:.0f}M "
      f"(M1 cure-cost, basis-dependent)")
print(f"    CSD_central = ~${central_robust/1e6:.0f}M (bay-wide avg basis)")
print("    CSD_ceiling = floor + Σ(gate-admitted Cᵢ, incl. M3 option value)")
print("                  — moving ceiling; M3 slot OPEN by design")
print(f"    Realized B₁ = ~${B1_ITEMIZED_BAYWIDE/1e6:.0f}M, 100% public / $0 industry")
print("    The finding is MIS-ASSIGNMENT, not just magnitude: the public")
print("    has already posted more than the floor; the extractive industry")
print("    has posted nothing.")


# =====================================================================
# PART 5 — THE IDENTITY ASSEMBLED (both directions, per §1.7)
# =====================================================================

print()
print("=" * 72)
print("PART 5 — COST SEVERANCE DECOMPOSITION (both directions)")
print("=" * 72)
print("""
  total CS = (CSD − B₁) + (RCV − B₂)

  Forward worked case (McDowell, per-ton):
    RCV  = M1 ∩ M3 convergence (M3 geo-center ~$1,115/ton)
    B₂   = realized forward instruments — M2 reads $50-88/ton societal
    CS_forward ≈ $1,025-1,065/ton             [matches landed §11.6]

  Backward worked case (Chesapeake reef, total):
    CSD  = $20M-37M floor … ~$211M central … ceiling OPEN (M3 slot)
    B₁   = ~$115M realized — public-paid; industry $0
    CSD − B₁: vs the FLOOR, B₁ already exceeds it (restoration is
    happening); vs the CENTRAL figure, ~$96M of severance remains
    unrestituted even crediting every public dollar; and the
    INSTRUMENT-ASSIGNMENT is inverted — B₁ should be industry-posted.

  Same equation, same Three Ways, run in both temporal directions;
  the backward range is wider (methodological-choice spread), the
  convergence logic identical in kind (Thm 10.1b; §17.5).
""")

n_fail = sum(1 for r in results if not r[6])
print(f"SUMMARY: {len(results)} checked values, {n_fail} mismatches.")
