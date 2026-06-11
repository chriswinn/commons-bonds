# Ch 6 rebuild — settled cross-check numbers + architecture handoff (2026-06-11)

**To:** the book-drafting dashboard/plan session (PAUSED on weekly token limit as of
2026-06-11; resumes post-Wave-1 or on token reset — author direction). This file is
the durable hand-over; nothing else needs to be alive for the pickup.
**From:** book-proposal-tier1 session (`claude/book-proposal-tier1-260611-e0dbb7`),
single owner of the convergence-framing + Method-2 correction per author routing
2026-06-11.

## What is settled (do not re-derive)

1. **The unified-triple sunset is author-ratified (2026-06-11).** The §9
   "Three-Model Convergence" triple (Damage Function / Real Options / RCV) and the
   §3 "Three Ways" triple (M1/M2/M3) are ONE apparatus at two points in the
   framework's history. DF = M1's earlier name; Real Options = pre-rework M3
   (market-volatility calibration retired by the 2026-06-08 Path-A rework); M2 is
   the realized-bond reading, not an estimator. Convergence is NOT celebrated:
   "three estimates that always agree is a tell that inputs have been tuned to
   agree." The defensible claim is direction-never-flips, with the shared-SCC
   caveat stated. Canonical decision record + full TA edit set:
   `manuscript/technical-appendix/convergence-scope-correction_2026-06-11_PROPOSED.md`
   **§7** (v3).

2. **The §9.5 cross-check numbers are settled and engine-verified** —
   `manuscript/technical-appendix/calculations/sec9_recompute_2026-06-11.py`
   (24 checks, 0 mismatches; main engine 21/21 intact). The Ch 6 rebuild brief
   should draft against THIS table:

| Case | Damage lens (M1) IPG | Premium lens (M3) IPG (price-independent) | RCV-integral IPG | Realized bond (M2: who paid) |
|---|---|---|---|---|
| McDowell coal | 107–110× ($504–518 ÷ $4.71) | 8.5–26× (center ~15×) | 61–115× ($525–540 adopted calibration) | $50–88/ton societal vs $8–15/ton industry → CS ≈ $1,025–1,065/ton |
| Deepwater Horizon | ~15–16× documented ($61.6B ÷ ~$4B derived gain; 13–19× reserve band); ~17–18× w/ $8–12B ongoing = same lens extended, NOT a second model | 2.4–5.1× (oil-class register; class-level label) | not computable on documented inputs | $61.6B industry-paid (litigation-forced) — largest industry-paid B₁ in corpus; CSD−B₁ ≈ $8–12B |
| Libby vermiculite | ≈26× documented-cash floor (≈13× if revenue ×2); 65–102× mortality-inclusive (VSL-labeled) | n/a (extraction ended 1990) | not computable on documented inputs | ~$600M public + ~$250M industry (≈70/30) |
| Baotou rare earths | not computable — remediation-only floor $5–15B | high-ς register; level not case-computable | not computable | ≈$0 identified |

3. **Retired figures** (regression-gate candidates; do not let them re-enter any
   draft): McDowell RO 45–89×; Deepwater RO 12–21×; Libby RO 57–93×; Libby
   RCV-col 72–111×; "RCV model estimate ~17–18×" as an independent-model label;
   "All three models agree within a factor of 1.5"; "three independent
   methods/models converge"; "across six tested cases."

## What the rebuild brief must decide (open, NOT settled here)

- **Chapter title.** "Three Ways of Counting" survives at reader level only if the
  chapter's triad becomes: two estimates of what restoration requires (damage
  audit; foreclosure premium) + the record of what was actually paid. Otherwise
  retitle. Author voice call.
- **Exxon Valdez's role.** EV is in the old Ch 6 roster and Ch 5's block hands it
  to Ch 6 "for its full decomposition," but EV is NOT in the settled cross-check
  table. Decide EV's case-role (narrative case vs computed row); if the rebuild
  drops the full decomposition, fix Ch 5's hand-off line in the same pass
  (cross-chapter wiring).
- **M1 band reconciliation.** The Ch 6 ↔ TA Method-1 discrepancy flag is still
  open (Ch 6 table "$261–$2,412/ton" vs TA §11.6 "$290–$2,702"; pending §11.9 DAC
  refresh moves the conservative cap ~20%). Reconcile during the rebuild; the
  ledger flagged it "route to owner, do NOT fix blind."

## Status of the TA prose application (for orientation, not action)

The TA §9/§10.2/§11.2/§11.3 sunset edit set (spec §7.2, E1–E14) is in the
book-proposal-tier1 session's ratification queue. If it has not landed by the time
Ch 6 rebuild starts, check `git log origin/main -- manuscript/technical-appendix/`
for the apply commit before drafting; the settled numbers above are stable either
way. The book-proposal §00/§05 Ch 6 summary block is being aligned to the same
architecture in the same queue.
