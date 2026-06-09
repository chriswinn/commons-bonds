# TA Rigor-Audit CLOSEOUT — consolidation summary + pre-merge review queue (2026-06-09)

**Branch:** `claude/ta-closeout-260607-92165f` (HELD — nothing merged to main).
**Review surface:** `git diff origin/main -- core/technical-appendix/ research/literature/bibliography.md`
**TA net:** 1 file, +367/−399 lines. **Gate:** author full-diff review → then merge to main (pre-push reconciliation). Submission remains a separate, author-only gate.

---

## What this consolidation did

Assembled the five held branches onto `origin/main` + applied the reserved closeout fixes. Merge order + per-branch verification:

| # | Step | Source | Verified |
|---|------|--------|----------|
| 1 | M3 Path-A + 33–122× retire + scaffolding sweep | INTEGRITY (`ta-m3-resume`, =D base) | V_market=28/V_option=0; 33–122×=0; §6.4 CIT (main) kept |
| 2 | §16 renames + §10 framing + logic fixes + coal completion | C (`ta-internal-fixes`) | κ/ζ/ω/Ω entities; Empirical Obs 10.1b=6; coal $4.71 |
| 3 | provenance + §11.10 + bib §23.1 | A (`ta-provenance`) | §7.4 combine; 33–122× re-adds rejected |
| 4 | bib §24/§23.2/§23.3 + §11.6 relabels + DAC + Solow removal | PR (`ta-provenance-resume`) | Solow-1956=0 / 1974=6 (Item 8 done); auto-merge scrutinized clean |
| 5 | Darity-version-diff read-only docs | B (`ta-rigor-audit`) | zero TA edits |

**Reserved closeout fixes applied:**
- **Item 4 — Deepwater §11.2 reconciliation.** Revenue ~$1.1B (arithmetically impossible) → ~$4B (derived, ≈50M bbl × 2010 ~$80/BOE; labeled "not separately reported"). Dropped the self-contradictory "$20–30B total" (< its own component sum) → BP all-in ~$61.6B (June 2016; →$65B+ 2018, = Ch 5's ~$65B), bib-backed. IPG 15–17× now **reproduces** ($61.6B÷~$4B); RCV 16–19× reproduces ((61.6+8–12)÷4). Convergence-within-1.5× **unchanged** (verified false positive).
- **Item 8 — Solow-1956 orphan:** done by PR, verified (§18 = Solow 1974 only; 0 in-text 1956).
- **§3.4 Norway Method-2 summary** reconciled to §11.5 sourced detail (NOK-led $2.0T end-2025 / 55B BOE / $48).
- **Pre-publication NOK→USD note** added to the §11.5 GPFG citation (reader-facing; per author).
- **bib §23.1 stale bits** fixed (Brent V_option→V_market; coal "not yet applied"→applied).

## Defensibility class (per change)
- **Sourced (class 1):** BP $61.6B (BP disclosures); $18.7B/$20.8B (DOJ/BP); Macondo ≈50M bbl reserve; 2010 crude ~$80; GPFG NOK 21,268B (NBIM); 75% capture (Min. Fin.); 55B BOE (Offshore Dir.) — all bib- or inline-cited.
- **Derived, work shown (class 2):** Deepwater revenue ~$4B; IPG 15–17× & RCV 16–19×; Norway M2 $48/BOE.
- **Framework outputs / internal-consistency (class 2):** §9.5 / §16 IPG cells (107–110× / 67–134×), M3 band — re-derived by D/INTEGRITY.
- **No class-4 (unsupported) numbers introduced.** Revenue explicitly labeled a derivation, not a sourced figure.

## Internally verified
- Invariants scan (`check-corpus-invariants.sh`): **TA + bib = 0 HIGH**. (Repo-wide 649 HIGH are pre-existing in other workstreams — `publishing/op-eds` dominant — untouched by this closeout.)
- Render proxy: 0 replacement/tofu chars; new glyphs present as entities; UTF-8.
- Reproduction: every displayed Deepwater + McDowell multiple reproduces from its stated inputs.

## NOT externally verified / PENDING (review queue)
1. **Stage-4 PDF render audit** — confirm the literal `ς` + overall render (no tofu) in the containerized toolchain before external circulation.
2. **Notation-consolidation** (→ notation/registry owner) — re-sweep the *merged* TA, sync the PROPOSED registry to canonical, resolve residual collisions: **§10 A1–A4/P1–P4 vs A(t)/P** (C's warning note is interim), **τ §5.4** re-overload; confirm E→Ω / B-vs-"billion" completeness.
3. **Norway $48-vs-$50 + capture headline** (→ Norway owner) — §3-anchor-table / §11.5 inflation caveat / "~17% captured" (4931) still use round $50; decide canonical ($48 precise / $50 round / ~$48–50 range) and whether "~17%"→"~16%". Load-bearing; not touched.
4. **Bib housekeeping (internal .md)** — §23.1↔§24 cross-ref (Black Lung Trust Fund vs Benefits Program; EPA SCC vs IWG TSD — distinct sources, benign); add Offshore-Directorate production entry; full §18↔`bibliography.md` reconciliation.
5. **Chapter↔TA 33–122× inconsistency** (→ redraft campaign) — Ch 6 / Ch 8 still carry 33–122× (chapter-side was routed to the redraft campaign, not the TA sessions); now that the TA retired it, the chapters need reconciling.
6. **CSD reverse-model + reef worked case** (Session F) — additive, not built/merged (no `reverse-csd` branch on origin).
7. **Figure ledger** — no Deepwater entry exists (optional future add; nothing to reconcile).

## Merge readiness
TA is internally consistent, reproduces, and passes invariants at HIGH. Recommend: **author reviews the path-scoped diff → on approval, merge to main** via pre-push reconciliation (`fetch origin main` + rebase; never force-push main). Items 1–7 above are post-merge / other-owner follow-ups, not merge blockers, EXCEPT the author may wish to resolve #3 (Norway headline) before or after merge at their discretion.
