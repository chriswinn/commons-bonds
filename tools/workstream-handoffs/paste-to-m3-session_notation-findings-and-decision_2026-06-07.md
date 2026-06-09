# PASTE-TEXT → Method-3 Path-A/B session (Session D)

*(Copy everything below the line into the target session.)*

---

**Notation findings that bear on the Method-3 formula + your Path-A/B decision — verify INDEPENDENTLY (against the cited sources + the file; do not take these on faith), then the direction call can be made.**

A notation/symbol-sweep ran on branch `claude/ta-internal-fixes-260607-208b7b` (off the held TA rigor-audit branch). It verified items that touch your section. Supporting artifact: `core/technical-appendix/symbol-registry_2026-06-07.md` (Parts 4 & 5). Method-3 formula as it stands:
`RCV_M3 = V_option × scarcity_multiplier(σ) × irreversibility_premium(α)`, with `scarcity_multiplier(σ) = 1 + log(1+σ) × Hotelling_anchor` and `irreversibility_premium(α) = 1/(1−α)^β`.

**A. The σ choice is dismissal-grade (verified against YOUR cited sources).**
- σ is defined as a "scarcity parameter = commons-stock / sustainable-flow ratio" and sits inside the option-value product. But in **Black–Scholes and Dixit–Pindyck — the works cited for V_option — σ is universally the VOLATILITY of the underlying.** A finance-literate referee reads "σ in an option-value product" as volatility on sight and concludes the author doesn't know the cited literature.
- Verified against: Columbia/Haugh Black–Scholes notes; NBER w12486; MIT Pindyck real-options lectures; Princeton UP. **Re-verify independently.**
- Latent units bug too: stock ÷ flow-rate is time-dimensioned, yet σ is used as the dimensionless argument of `log(1+σ)`.
- **Decision impact:** under **Path A** (keep `scarcity_multiplier(σ)`), σ MUST be renamed (e.g. ς / a descriptive token). Under **Path B** (adopt proper Dixit–Pindyck machinery), σ is *vindicated* as real volatility and the scarcity-σ disappears. Either way the current σ is a defect; its fix depends on your direction.

**B. δ is now free for proper DP use.** The sweep renamed §16.1's discount-rate decay `δ → κ` (it collided with the §10.3 ε–δ proof variable and with the DP convenience-yield δ). So if Path B adopts DP machinery using δ for the convenience/payout yield, that glyph is now available and won't collide.

**C. `log` is entirely M3-coupled (yours).** Every `log()` usage (896, 904, 4311, 4761, 5245) is inside `scarcity_multiplier`. "log" is never defined as ln, but the worked `log(101)≈4.6` is natural log (ln 101≈4.615; log₁₀≈2.004 would change the multiplier ~2.3×). The sweep did NOT touch it. If Path A keeps the log form → define "log ≡ ln" once; if Path B drops `scarcity_multiplier` → log disappears. Verify and handle with the direction.

**D. "α-dominance sensitivity finding" is a property of the chosen functional form, not an empirical finding.** `irreversibility_premium(α) = 1/(1−α)^β` diverges as α→1 by construction, so high-α cases are α-dominated *by construction*. The §3.5 header (~line 922) "Sensitivity finding" + implication (1029–1033, "the real debate is irreversibility") overclaim empirical content. A reframe is drafted but **HELD** pending your direction (the spine itself may change under Path B). Verify the math; settle the framing with the direction.

**E. §3.5 Solow citation (#8).** §3.5 line 917 cites "Solow 1956 *QJE*" for an intergenerational-equity point — that's the growth paper. The intergenerational-equity paper is Solow 1974 *Review of Economic Studies* (already in bib). Pending citation swap, in your section. Verify.

**F. Three workstreams are queued behind your Path-A/B call:**
- Batch II notation renames (σ; Method-3 β; Method-3 α framing) + the `log≡ln` fix.
- Correctness items #3 (§9.5 convergence-ordering cascade), #6 (α-dominance reframe = item D above), #8 (Solow = item E above) — all in your section or its cascade.

---

## THE DECISION (for the author — your prior M3-memo framing + the new σ input)

- **Path A** (the V_option-audit's "Option A"): correct the V_option base + tame the irreversibility premium; **keep** the σ/α architecture and the α-dominance/ARR spine. *Requires renaming σ* (volatility conflict). Less destructive; preserves the "methodological contribution" narrative.
- **Path B** (full Dixit–Pindyck premium): drop the separate `scarcity_multiplier` + `irreversibility_premium`. Your memo's stated cautions: (1) the ratified "double-counts" justification doesn't describe the *current* formula; (2) it swaps the framework's **best-grounded** parameter (α — IPCC/Bernhardt & Palmer) for its **worst-grounded** (δ, headline diverging to ∞ as δ→r); (3) it demolishes a narrative the TA itself calls "a methodological contribution." Your memo's lean was: do the safe bib additions now, put Path-A-vs-B back to the author as a decision rather than executing Path B.
- **New input from the σ finding:** Path A must rename σ; Path B may *vindicate* σ as proper volatility. So the notation problem is now a fresh consideration in the choice, not just a cleanup.

**Ask:** verify A–E independently, then the author makes the Path-A/B call. Whatever lands, the held Batch II + correctness #3/#6/#8 apply against the *final* §3.5/§11.8.
