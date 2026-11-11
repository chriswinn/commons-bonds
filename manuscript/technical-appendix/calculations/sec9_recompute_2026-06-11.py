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


# --- v2.0.1 (2026-11-11): inputs are DERIVED, not typed in. The integral
# and the realized bond come from csd_rcv_calculations.py (imported with its
# console output suppressed). Retired and no longer reproduced: 107-110x and
# 61-115x (2020-dollar costs over a 1960 nominal price), the unsourced $8.66
# price basis, and CS ~ $1,025-1,065/ton (Method-3 centre as headline). ---
import contextlib, importlib.util, io, os, sys
sys.dont_write_bytecode = True
_spec = importlib.util.spec_from_file_location(
    "engine", os.path.join(os.path.dirname(os.path.abspath(__file__)), "csd_rcv_calculations.py"))
engine = importlib.util.module_from_spec(_spec)
with contextlib.redirect_stdout(io.StringIO()):
    try:
        _spec.loader.exec_module(engine)
    except SystemExit as e:
        if e.code:
            raise

print("=" * 72)
print("A. McDOWELL — the integral is the headline; M1 and M3 are cross-checks")
print("=" * 72)
rcv_lo, rcv_hi = engine.rcv_lo, engine.rcv_hi
check("McDowell integral low (Stern)", rcv_lo, 524, 528, "$/ton")
check("McDowell integral high (Nordhaus)", rcv_hi, 539, 543, "$/ton")
# Consistent-basis multiples: 2020-dollar RCV over the contemporary price
# by grade ($40-140/ton, EIA; TA §11.6).
check("Integral multiple low (525/140)", 525 / 140, 3.7, 3.8, "x")
check("Integral multiple high (540/40)", 540 / 40, 13.4, 13.6, "x")
check("Damage-floor multiple low (504/140)", 504 / 140, 3.5, 3.7, "x")
check("Damage-floor multiple high (518/40)", 518 / 40, 12.9, 13.0, "x")
# M3 premium multiple (price-independent): 8.5-26x, ~15x.
m3_lo = 40 * 1.27 * irreversibility_premium(0.85) / 40
m3_hi = 140 * 1.31 * irreversibility_premium(0.95) / 140
check("McDowell M3 multiple low", m3_lo, 8.0, 9.0, "x")
check("McDowell M3 multiple high", m3_hi, 25.0, 27.0, "x")
check("McDowell M3 multiple geometric center", math.sqrt(m3_lo * m3_hi), 14.0, 16.0, "x")
# Realized bond (derived in the engine from the §11.6 components):
check("Bond per ton, all payers, low", engine.MCD_M2_ALL[0], 88.0, 88.5, "$/ton")
check("Bond per ton, all payers, high", engine.MCD_M2_ALL[1], 99.5, 100.5, "$/ton")
check("Bond per ton, extractor-paid, low", engine.MCD_M2_INDUSTRY[0], 8.0, 8.6, "$/ton")
check("Bond per ton, extractor-paid, high", engine.MCD_M2_INDUSTRY[1], 13.0, 13.6, "$/ton")
check("McDowell CS low (integral - all-payer bond)", engine.mcd_cs_lo, 424, 428, "$/ton")
check("McDowell CS high (integral - all-payer bond)", engine.mcd_cs_hi, 450, 454, "$/ton")

print()
print("=" * 72)
print("B. DEEPWATER — the realized industry-paid bond case (ratios conditional on the blowout)")
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
check("Oil-class M3 multiple low (ς=50, α=0.85)", rcv_m3(40, 50, 0.85) / 40, 7.8, 8.2, "x",
      kind="CLASS-REGISTER")
check("Oil-class M3 multiple high (ς=200, α=0.95)", rcv_m3(120, 200, 0.95) / 120, 25.0, 25.6, "x",
      kind="CLASS-REGISTER")
print("  -> M3 for Deepwater: computable only at the oil-class register")
print("     (8-25x, physical alpha), labeled class-level. RCV-integral: NOT computable on")
print("     documented inputs (no case calibration exists).")
print("  -> M2/B1: $61.6B INDUSTRY-paid (litigation-forced) — largest realized")
print("     industry-paid B1 in the corpus. CSD - B1 ~= $8-12B ongoing.")

print()
print("=" * 72)
print("C. LIBBY — backward case; rebuilt on sourced figures only (v2.0.1)")
print("=" * 72)
# >$600M federal cleanup (EPA); Grace's 2008 payment of $250M REIMBURSED
# cleanup cost (DOJ/EPA, March 11 2008) and is not an additional cost;
# revenue ~$100M is an unconfirmed industry estimate.
check("Libby cleanup / revenue (0.6/0.1)", 0.6 / 0.1, 5.9, 6.1, "x")
check("Libby extractor share of cleanup (250/600)", 100 * 250 / 600, 41.0, 42.5, "%")
vsl_lo, vsl_hi = 694 * 7.4e6, 694 * 11.0e6
check("Libby mortality head low (694 x $7.4M VSL)", vsl_lo / 1e9, 5.0, 5.2, "$B")
check("Libby mortality head high (694 x $11.0M VSL)", vsl_hi / 1e9, 7.5, 7.7, "$B")
check("Libby cleanup + mortality head low", (vsl_lo + 0.6e9) / 1e9, 5.6, 5.8, "$B")
check("Libby cleanup + mortality head high", (vsl_hi + 0.6e9) / 1e9, 8.1, 8.3, "$B")
print("  -> RETIRED: $2.6B documented-cash floor, 26x, 65-102x. The $50M/yr")
print("     monitoring stream and the $500M property estimate have no source")
print("     and are not entered (Open).")

print()
n_fail = results.count(False)
print(f"SUMMARY: {len(results)} checked values, {n_fail} mismatches.")
raise SystemExit(1 if n_fail else 0)
