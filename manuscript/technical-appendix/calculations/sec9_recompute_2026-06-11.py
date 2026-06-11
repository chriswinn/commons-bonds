#!/usr/bin/env python3
"""
§9.5 cross-check table recompute under the unified architecture (2026-06-11)

Context: author ratified (2026-06-11, book-proposal-tier1 session) that the
§9 "Three-Model Convergence" triple (Damage Function / Real Options / RCV)
and the §3 "Three Ways" triple (M1 / M2 / M3) are ONE apparatus at two
points in the framework's history — DF = M1's earlier name; Real Options =
pre-rework M3 (market-volatility calibration retired by the 2026-06-08
Path-A rework); M2 (realized bond) is not an estimator. This script settles
the §9.5 table numbers under the current architecture, per case.

Disciplines: every constant sourced (TA line / external authority) or
labeled; reproductions of landed numbers flagged on mismatch; retired
figures (RO 45-89x / 12-21x / 57-93x; RCV-col 72-111x; Deepwater "RCV
~17-18x" as a third model) are NOT reproduced — they are shown to be
either basis-unrecoverable or relabeled honestly below.

Run: python3 sec9_recompute_2026-06-11.py   (stdlib only)
"""

import math

results = []


def check(label, computed, lo, hi, unit, kind="REPRODUCTION"):
    ok = lo <= computed <= hi
    results.append(ok)
    print(f"[{kind}] {label}: {computed:,.1f} {unit} "
          f"(target {lo:,.1f}-{hi:,.1f}) {'PASS' if ok else '** MISMATCH **'}")
    return ok


# --- M3 Path-A core (mirrors csd_rcv_calculations.py; §3.5) ---
HOTELLING_ANCHOR = 0.05

def scarcity_multiplier(sigma_f):
    return 1.0 + math.log(1.0 + sigma_f) * HOTELLING_ANCHOR

def irreversibility_premium(alpha):
    return 1.0 / (1.0 - alpha)

def rcv_m3(v, s, a):
    return v * scarcity_multiplier(s) * irreversibility_premium(a)


print("=" * 72)
print("A. McDOWELL — the one case where every forward lens computes")
print("=" * 72)
# M1/Damage-Function lens IPG: 4-component Pigouvian floor $504-518 (ledger
# J1/J6-adjacent; TA §11.1) over $4.71 1960 mine-mouth (EIA Table 7.9).
check("McDowell M1/DF lens IPG low (504/4.71)", 504 / 4.71, 106.5, 107.5, "x")
check("McDowell M1/DF lens IPG high (518/4.71)", 518 / 4.71, 109.5, 110.5, "x")
# RCV-integral lens: adopted calibration $525-540/ton (2026-06-10) across
# the $8.66 contemporary / $4.71 1960 price bases -> 61-115x.
check("McDowell integral IPG low (525/8.66)", 525 / 8.66, 60.0, 61.5, "x")
check("McDowell integral IPG high (540/4.71)", 540 / 4.71, 114.0, 115.5, "x")
# M3 foreclosure-premium lens (price-independent multiple): 8.5-26x, ~15x.
m3_lo = 40 * 1.27 * irreversibility_premium(0.85) / 40
m3_hi = 140 * 1.31 * irreversibility_premium(0.95) / 140
check("McDowell M3-IPG low", m3_lo, 8.0, 9.0, "x")
check("McDowell M3-IPG high", m3_hi, 25.0, 27.0, "x")
check("McDowell M3-IPG geometric center", math.sqrt(m3_lo * m3_hi), 14.0, 16.0, "x")
# M2 realized: $50-88/ton societal, $8-15 industry (TA §11.6 landed) ->
# CS = M3-geo-center - M2 societal band = $1,025-1,065/ton (landed §11.6).
mcd_geo = math.sqrt((40 * 1.27 * irreversibility_premium(0.85)) *
                    (140 * 1.31 * irreversibility_premium(0.95)))
check("McDowell CS low (geo - 88)", mcd_geo - 88, 1020, 1045, "$/ton")
check("McDowell CS high (geo - 50)", mcd_geo - 50, 1045, 1070, "$/ton")

print()
print("=" * 72)
print("B. DEEPWATER — backward-dominant; M1 lens computes, integral does not")
print("=" * 72)
# Private-gain basis: ~$4B framework DERIVATION (Macondo ~50M bbl x ~$80;
# $3.2-4.8B across 40-60M bbl) — TA §11.2 line 4058, labeled in-file.
# Documented cost: $61.6B BP all-in (BP final est. June 2016; §11.2).
check("Deepwater M1/DF documented IPG central (61.6/4.0)", 61.6 / 4.0, 15.0, 16.0, "x")
check("Deepwater M1/DF reserve-band low (61.6/4.8)", 61.6 / 4.8, 12.5, 13.0, "x",
      kind="SENSITIVITY")
check("Deepwater M1/DF reserve-band high (61.6/3.2)", 61.6 / 3.2, 19.0, 19.5, "x",
      kind="SENSITIVITY")
# The TA's "RCV model estimate ~17-18x" is the SAME lens + $8-12B ongoing:
check("Deepwater DF-extended low ((61.6+8)/4)", (61.6 + 8) / 4.0, 17.0, 17.5, "x",
      kind="RELABEL")
check("Deepwater DF-extended high ((61.6+12)/4)", (61.6 + 12) / 4.0, 18.0, 18.5, "x",
      kind="RELABEL")
print("  -> RELABEL finding: §11.2's 'RCV model estimate ~17-18x' reproduces as")
print("     the damage lens with ongoing costs added — NOT an independent model.")
print("     'All three models agree within a factor of 1.5' counted one")
print("     computation twice (and the §9.5 RO column 12-21x has no derivation")
print("     anywhere in the corpus). Convergence row: retired.")
# M3: oil-class register only (Norway §11.5 corners; class-level label):
check("Oil-class M3-IPG low (ς=50, α=0.50)", rcv_m3(40, 50, 0.50) / 40, 2.3, 2.5, "x",
      kind="CLASS-REGISTER")
check("Oil-class M3-IPG high (ς=200, α=0.75)", rcv_m3(120, 200, 0.75) / 120, 4.9, 5.2, "x",
      kind="CLASS-REGISTER")
print("  -> M3 for Deepwater: computable only at the oil-class register")
print("     (2.4-5.1x), labeled class-level. RCV-integral: NOT computable on")
print("     documented inputs (no case calibration exists).")
print("  -> M2/B1: $61.6B INDUSTRY-paid (litigation-forced) — largest realized")
print("     industry-paid B1 in the corpus. CSD - B1 ~= $8-12B ongoing.")

print()
print("=" * 72)
print("C. LIBBY — backward-dominant; M1 lens computes, others do not")
print("=" * 72)
# Documented-cash floor: $1.35B committed + $1.25B accrued monitoring
# (2000-2025 @ $50M+/yr) = $2.6B over ~$100M lifetime revenue (§11.3).
check("Libby documented-cash floor IPG (2.6/0.1)", 2.6 / 0.1, 25.5, 26.5, "x")
check("Libby revenue-doubling sensitivity (2.6/0.2)", 2.6 / 0.2, 12.5, 13.5, "x",
      kind="SENSITIVITY")
# Mortality-inclusive: 694 deaths (Naik et al. 2017) x EPA VSL $7.4-11.0M.
vsl_lo, vsl_hi = 694 * 7.4e6, 694 * 11.0e6
check("Libby VSL component low", vsl_lo / 1e9, 5.0, 5.2, "$B")
check("Libby VSL component high", vsl_hi / 1e9, 7.5, 7.7, "$B")
# §11.3 total "≈$6.5-10.2B": low = VSL-low + committed-only ($1.35B);
# high = VSL-high + full documented-cash ($2.6B). Reconstructs:
check("Libby mortality-inclusive total low ((5.14+1.35))", (vsl_lo + 1.35e9) / 1e9,
      6.4, 6.6, "$B", kind="RECONSTRUCTION")
check("Libby mortality-inclusive total high ((7.63+2.6))", (vsl_hi + 2.6e9) / 1e9,
      10.1, 10.3, "$B", kind="RECONSTRUCTION")
check("Libby mortality-inclusive IPG low (6.5/0.1)", 6.5 / 0.1, 64.5, 65.5, "x")
check("Libby mortality-inclusive IPG high (10.2/0.1)", 10.2 / 0.1, 101.5, 102.5, "x")
print("  -> Headline alignment: §11.3 prints '≈65-100x' but its own sub-bands")
print("     run to 102x; settle headline at 65-102x (or keep '~65-100x' as")
print("     a rounding — author call, micro).")
print("  -> M3 forward: n/a — extraction ended 1990, forward foreclosure ~0")
print("     (portfolio row, csd_rcv_calculations.py Part 7). RCV-integral:")
print("     NOT computable on documented inputs. Retired columns 57-93x (RO)")
print("     and 72-111x (RCV): no derivation survives anywhere in the corpus.")
print("  -> M2/B1: ~$600M Superfund (public) + ~$250M settlements (industry)")
print("     ~= 70/30 public/industry split (§11.3 + portfolio row).")

print()
n_fail = results.count(False)
print(f"SUMMARY: {len(results)} checked values, {n_fail} mismatches.")
raise SystemExit(1 if n_fail else 0)
