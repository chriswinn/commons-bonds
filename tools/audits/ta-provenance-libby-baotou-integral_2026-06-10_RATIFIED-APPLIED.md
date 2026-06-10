# TA provenance: §11.3 Libby + §11.4 Baotou + RCV-integral calibration — derivations (PROPOSED)

**Status: RATIFIED 2026-06-10 (author: "Apply 1, 2, 3 as recommended and proposed") + APPLIED same day.** Items 1, 2, and 3-Option-A applied to the TA incl. the §9.5 table cascade, §6.3/§11.11 ratio cascade, the §11.1 calibration note, and the calc-engine annotation sync (35/35 reproductions still PASS). Residual flagged, NOT in scope: §6.3's ~$1,025–1,065/ton cell level (same undocumented class; separate item) + `publishing/book-proposal/05_chapter-summaries.md` carries 67–134× (live-owned by the book-proposal sprint — routed there, not edited here).
**Session:** `claude/ta-provenance-11-3-11-4-integral-260610-d22bed` (2026-06-10). Lineage: successor
to `ta-number-provenance-ledger_2026-06-07.md` + `ta-method1-input-provenance_2026-06-06.md`; same
defensibility classes (1 SOURCED / 2 DERIVED / 3 LABELED ASSUMPTION / 4 UNSUPPORTED) and the
peer-review-defense discipline (`tools/memory/feedback_quantitative_apparatus_peer_review_defense.md`):
never a posited number typeset to look sourced; anchor conservatively; add sensitivity statements that
DEMONSTRATE robustness. Target standard: §11.5/§11.6.

---

## ITEM 1 — §11.3 Libby: the "$4 billion+ (40:1)" total and the 55–82× / 48–76× / 61–91× triplet

### Defect (confirmed)

The stated components do not reach the stated total:

| Component (as listed in §11.3) | Amount | Class |
|---|---|---|
| Federal Superfund cleanup committed | $600M+ | 1 (EPA Libby site profile; register §23.3 HIGH) |
| Legal settlements (wrongful death/injury) | $250M+ | 1 (DOJ/W.R. Grace 2008 settlement; register HIGH) |
| Medical monitoring + treatment | $50M+/yr ongoing | 3 (rate labeled; accrual not totaled in-text) |
| Lost property values / economic disruption | ~$500M | 3 (labeled estimate) |
| **Sum of listed components** | **≈$1.35B + accrual** | |

Accruing the monitoring rate over the CARD-clinic era (~2000→2025, 25 yr × $50M) adds ≈$1.25B →
**≈$2.6B total. The "$4 billion+" is not reachable from its own list** (gap ≈ $1.4B+), and "40:1"
divides the unreachable $4B by the ~$100M revenue figure that the corpus register already flags
UNVERIFIABLE. The IPG triplet implies an even larger total (55–82× × $100M = **$5.5–8.2B**) with no
stated derivation. As written: class 4.

### Reconstruction (labeled) — the missing mass is monetized mortality

The register carries **694 documented asbestos-related-disease deaths through 2011** (Naik et al.
2017, *J Expo Sci Environ Epidemiol* — class 1). Monetizing at EPA's Value of Statistical Life:

| VSL vintage | VSL | 694 deaths → | + cash components ($1.35B…$2.6B) → total | ÷ $100M revenue |
|---|---|---|---|---|
| EPA 2006$ (low) | $7.4M | $5.14B | $6.5B…$7.7B | 65–77× |
| EPA ~2023$ (updated) | $9.3–11.0M | $6.5–7.6B | $7.8B…$10.2B | 78–102× |

So a **mortality-inclusive total of ≈$6.5–10.2B (65–102×)** is derivable from class-1 inputs + one
labeled choice (VSL vintage). This is very likely the construction behind the current 55–82× band,
but the band as printed is not exactly recoverable (55× requires VSL-only with partial cash), and
deaths after 2011 (ARD mortality is ongoing) make even 65× conservative.

### Proposed replacement text (ratify → apply)

1. Add a mortality line to the components list:
   *"Asbestos-related-disease mortality, monetized: 694 documented deaths through 2011 (Naik et al.
   2017) × EPA VSL $7.4–11.0M ≈ $5.1–7.6B (labeled estimate; mortality is ongoing, so this is a
   floor)."*
2. Replace the total line:
   *"Documented-cash floor: ≈$1.35B committed + ≈$1.25B accrued monitoring (2000–2025 at $50M+/yr)
   ≈ $2.6B — ≈26:1 against the ~$100M lifetime revenue (itself an industry estimate no primary
   source has confirmed; if true revenue were twice as high, the floor ratio is still ≈13:1).
   Mortality-inclusive total: ≈$6.5–10.2B."*
3. Restate the triplet from the derivation: **Damage Function ≈65–100×** (sensitivity: VSL vintage
   dominates; 2006$ → 65–77×, updated → 78–102×); Real Options and RCV variants by the document's
   standard method scalars (×0.87–0.93 / ×1.11): **RO ≈57–93×, RCV ≈72–111×**. Alternative if the
   author prefers minimal motion: keep 55–82× and label it *"conservative band beneath the derived
   65–102×"* — defensible but weaker than restating.

**Class after fix:** total = 2 (derived, shown); mortality term = 3 (labeled, sensitivity given);
revenue = 3 (labeled unverified, sensitivity given). The 40:1 line dies.

---

## ITEM 2 — §11.4 Baotou: the 12–35× / 18–48× / 22–41× triplet has no recoverable basis

### Defect (confirmed)

No denominator or derivation is stated. The available documented pieces cannot produce it:
remediation $5–15B (register: MIIT/Jiangxi $5.5B anchor; ">$100B" rejected as unverifiable) against
annual export revenue $2–4B/yr gives **1.2–7.5** (a stock-vs-flow ratio, not an IPG); against any
cumulative-revenue basis the ratio falls below 1. The health, agricultural, groundwater, and
relocation costs that would carry the triplet are listed but unquantified, and prior provenance
passes located no credible external dollar estimates for them. **As written: class 4, and not
honestly reconstructible.** (This is the same defect class as the retired 33–122×.)

### Proposed replacement text (ratify → apply)

Replace the IPG line with a derived, conservative, honestly-typed statement:

*"IPG: not computable to the document's IPG form on documented inputs — the dominant local costs
(cancer incidence, agricultural foreclosure, Yellow-River-basin groundwater, village relocation)
have no credible external dollar estimates. What the documented inputs do support: the tailings-lake
remediation liability alone ($5–15B; MIIT/Jiangxi cleanup-program anchor ≈$5.5B) equals
**1.2–7.5 years of the entire export revenue stream** ($2–4B/yr) — a lower bound on the severance,
since it excludes every unquantified cost category above."*

**Class after fix:** 2 (derived from class-1/3 inputs, arithmetic shown). The case's narrative force
(spatial severance at 10,000 km) is untouched; the only change is refusing to print a triplet nothing
supports. If the author wants an IPG retained here, the honest path is commissioning per-category
cost estimates first (research task, not a restatement).

---

## ITEM 3 — §11.1 + §16.4 RCV-integral lens: $580–620/ton and 67–134× lack a documented calibration

### Findings

1. The **67–134× spread is reconstructible arithmetic given the level band** — it is the $580–620
   level across the two price denominators the section names: ÷ current price ~$8.66 → **67–72×**;
   ÷ 1960 mine-mouth $4.71 → **123–132×** (printed as 67–134×). So the only genuinely undocumented
   number is the **level band $580–620/ton**.
2. The labeled reconstruction (`calculations/csd_rcv_calculations.py` Part 3; run-output 2026-06-10)
   reaches **$526 (Stern r₀=1.4%) / $537 (4%) / $541 (Nordhaus 5.5%)** under fully-documented
   assumptions: U = r(t)·P (Def 1.3's lower bound, conservative), the $496 carbon term entering as a
   present-value pulse (not re-discounted), the non-carbon $8–22/ton spread over the 200-yr §16.4
   tail, Weitzman decline with 50-yr half-life toward r_∞ = 2%. That is **−9% from the printed band**
   — close, but the original parameterization is not recorded anywhere and could not be recovered.

### Options

- **(A) RECOMMENDED — adopt the documented calibration.** Restate the level to **≈$525–540/ton**
  (citing the Part-3 parameterization in a short "integral calibration" note in §11.1), and cascade
  the ratio: ÷$8.66 → ≈61×; ÷$4.71 → ≈111–115× ⇒ **IPG ≈61–115× (integral lens)**. Conservative
  (lower band), fully reproducible, and the calibration note doubles as the referee's audit trail.
  Cascade sites: §3.6 table · §9.5 (67–134 cell — this item owns it) · §11.1 · §11.11 · §16.4 row 1
  · the §6.3 summary line (L1132). Chapter-side echoes route to the numeric sweep.
- **(B) Keep $580–620 + add the calibration note as a robustness demonstration** ("a conservative
  labeled reconstruction reaches $526–541, within 9%"). Less motion, but leaves the headline number
  resting on an unrecorded parameterization — exactly what the peer-review-defense memo says not to
  do for load-bearing figures.

**Sensitivity (either option):** the result is dominated by the $496 carbon pulse (≈92% of the
total); the U-flow and tail terms move the band by <$30 across Stern↔Nordhaus — i.e., the IPG
conclusion (a double-digit-to-triple-digit multiple) survives any defensible discount schedule.

---

## Ratification asks (per-prompt cadence)

1. **Item 1:** apply the Libby restatement (mortality line + honest floor + derived triplet), or the
   minimal-motion variant?
2. **Item 2:** apply the Baotou IPG-retirement + remediation-floor restatement?
3. **Item 3:** Option A (adopt $525–540 + cascade) or Option B (keep + note)?

On ratification this session applies the chosen text, updates
`tools/audits/ta-number-provenance-ledger_2026-06-07.md` dispositions, re-runs the invariants gate,
and re-verifies every changed multiple reproduces from its stated inputs.
