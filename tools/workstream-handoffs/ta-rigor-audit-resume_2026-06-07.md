# Technical Appendix Rigor Audit — RESUME / HANDOFF (2026-06-07)

**Trigger to resume:** "resume the TA rigor audit."
**Branch:** `claude/ta-rigor-audit-260606-f537b4` — worktree `/Users/c17n/commons-bonds-ta-rigor-audit-260606-f537b4`.
**HELD from main** (18+ commits ahead, NOTHING merged). Author reviews before merge. Path-scoped diff: `git diff origin/main -- core/technical-appendix/TechnicalAppendix_v2.0.0.html`.
**Why this handoff:** session length started degrading rigor (twice cited our own table/ledger as "the authoritative source" — the self-citation trap; nearly applied a fix on an unverified number that the §11.10 agent then proved wrong). A fresh session + this doc + the disciplines below avoids that.

---

## RATIFIED DISCIPLINES (carry forward — do NOT re-litigate)

1. **Defensibility class for EVERY number:** (1) **sourced** (cite the external authority) · (2) **derived** (show the work from cited inputs) · (3) **labeled assumption + sensitivity** · (4) **unsupported** = the defect to kill. "Canonical / we've-used-it" is NOT a justification. **Cite the EXTERNAL source, never our own ledger/table** (the repeated slip).
2. **Add the source to the bibliography the MOMENT it's verified** — stop the re-verify-then-lose cycle.
3. **Verify before applying** any value-dependent fix. (The §11.10 agent proved this: the "$50–500/kg" I almost ratified is unverifiable.)
4. **M3 = Path B** (full Dixit–Pindyck premium; drop the separate scarcity_multiplier + irreversibility_premium, which double-count). Supersedes item-14.
5. **CSD method** = bounded range (provable M1+M2 floor + Ostrom-path generative, gate-disciplined ceiling); NO "standing" anywhere in the apparatus; NO unpriceability theorem; coercion handled by a first-person authorial note (chapters + TA). Spec: `core/technical-appendix/CSD-computation-method-spec_2026-06-06.md`.
6. **M3 is a triangulation leg + the framework's core — make it SOLID (grounded), not hedged.** (Reverses an earlier wrong "demote M3 to qualitative" suggestion.)

---

## APPLIED + COMMITTED (on held branch; author reviews before merge)

**TA (`TechnicalAppendix_v2.0.0.html`, 14 line-changes):**
- §11.5 Norway CS-reduction **84%→16%** (item 1)
- §11.1 carbon **$510→$496**; total **$518–532→$504–518**; L3898 $496; §14.7 **$518→$504**; IPG label "(without carbon)" → carbon-inclusive 33–122×; population **18,000→~19,000** (ledger-covered cascade)
- §11.6 Method-1 combined anchor → **$1,595–2,702 / $812–1,658 / $290–875** + cascades L4827/4869/4871 (item 2)
- §11.8 scarcity_multiplier **6–7→1.27–1.31** (item 4)
- §11.10 Falcon 9 **$2,700→$3,245/kg** ($74M/22,800 kg, 2026) (item 5)
- §11.8 V_option **$500–2,000→$50–500** (item 14) — ⚠ **SUPERSEDED by Path B; interim only, will be reworked**

**Bibliography (`research/literature/bibliography.md`):** §23 figure-backing data sources (Census, Appalachian Voices 2021, BP/DOJ Deepwater, EPA AP-42, EPA-2023 SCC, Climeworks/IEA/IPCC/NAS, EIA coal price, SpaceX); §16 Arrow-Fisher 1974; §18.6 Weitzman 2001. §23.2 candidates to re-verify (Isle de Jean Charles, Pericak 2018, OSMRE/ARRI).

**Other committed:** durability beats cluster (`manuscript/_CANDIDATE-BEATS-AND-DEVICES.md`); `manuscript/technical-appendix/` symlink → canonical TA; CSD spec; audit ledger; M3 Path-B proposal record; 5 research-agent audit files; structural TODOs.

---

## PENDING — NOT DONE (the next session's work)

- **§11.10 space-economics cluster** (sourcing agent done; `tools/audits/ta-11.10-space-economics-sourcing_2026-06-07.md`): **(a) NEW HARD error — Keck "7-ton" is a mis-transcribed DIAMETER; the asteroid is ~500 tons → "$370,000/kg" should be ~$5,200/kg (~2 orders off).** (b) Planetary Resources **"$50–500/kg" is UNVERIFIABLE** — substitute the academic ~$2,000–3,000/kg (Colvin/Crane/Lal 2020, *Acta Astronautica*) or downgrade to POSITED + drop the "Source: PR" attribution. (c) Bennu $9.5M/g = derivation (NASA 121.6 g ÷ ~$1.16B) — present as derived. (d) the per-gram→per-kg unit fix + orders-of-magnitude recompute (now against the corrected anchors, NOT $50–500/kg). (e) Falcon Heavy config/year-stamp. (f) add all 6 to bib.
- **§16.1 declining-rate fix** — PRESENTED, not ratified: `r(t)=r₀·e^−δt+r_min` → `(r₀−r_min)·e^−δt+r_min` (gives r(0)=r₀ per the prose). Clean internal-correctness; apply on ratification.
- **M3 Path-B rework** — proposal at `tools/audits/ta-m3-pathB-rework_proposal-record_2026-06-07.md`. Reworked McDowell M3 ≈ $1,950/ton; convergence holds + tightens. **5 OPEN QUESTIONS for author** (Norway cascade is HIGHEST-RISK — Path B has no α dial; Norway's GPFG-restoration-optionality / canonical-B₂ story must be re-expressed). Then apply: §3.5/§11.6/§11.8 + cascades §9.5/§11.11/§11.5-Norway + add bib sources.
- **Item 3 Deepwater reconciliation cluster** — DECIDED: cost **$61.6B** (BP final, in bib); revenue **~$3–4B** (the $1.1B is arithmetically impossible); **KEEP IPG 15–17×** (the audit's "→18–27×" was WRONG — verified against $61.6B/$3-4B). Cross-corpus: §11.2 + §9.5 + Ch5 + figure ledger. **KNOWN FALSE POSITIVE: do NOT change the "convergence within 1.5×".** Not yet applied.
- **SOFT batch (relabels, no number changes):** §11.6 Eco/Cohesion inputs → estimate-labels + anchors (Appalachian Voices reclamation aggregate; Isle de Jean Charles for relocation); §14.6 **Daly inversion** fix; §3.5 **Solow 1956→1974** misattribution; σ-register reconciliation; add the M3-rigor + §11.10 bib sources. (Method-3 parameter-labeling is absorbed into the Path-B rework.)
- **Remaining HARD walkthrough items (~9):** §11.5 M1 table $300–650→$161–422; §11.6 M2 industry-paid $8–15→$8–13 + societally-paid $50–88→$88–100; §3.6 McDowell M1 $310–1,800→$261–2,412; §3.4/3.6 Norway vintage 50B/$50→55B/$48; §16.2 stock-dependent-S sign vs prose; §9.5 convergence-ordering vs table; §3.1 Def 1.3 `U≥P(t)` dimensional; §10.1b proof restates premise (relabel to Empirical Observation) + statement-scope; §3.5 α-dominance "finding"→property-of-functional-form. **Each NUMERIC item needs the defensibility check first** (several will need sourcing verification, like §11.10 did). Proof/dimensional items (§16.1/§16.2/§9.5/§3.1/§10.1b/§3.5-α) are internal-correctness — no sourcing, fast ratifies.

---

## MASTER FILES
- Finding list: `core/technical-appendix/TA-rigor-audit-ledger_2026-06-06.md` (81 confirmed → ~45 distinct)
- CSD method spec: `core/technical-appendix/CSD-computation-method-spec_2026-06-06.md`
- M3 Path-B proposal: `tools/audits/ta-m3-pathB-rework_proposal-record_2026-06-07.md`
- M3-rigor research: `tools/audits/ta-m3-{sigma,alpha,voption}-*_2026-06-07.md`, `ta-method3-parameter-provenance_2026-06-06.md`
- §11.6 input provenance: `tools/audits/ta-method1-input-provenance_2026-06-06.md`
- §11.10 sourcing: `tools/audits/ta-11.10-space-economics-sourcing_2026-06-07.md`
- Single-source-of-truth figures: `manuscript/_CANONICAL_FIGURE_LEDGER.md`
- Structural TODOs (deferred): `tools/workstream-handoffs/post-audit-structural-todos_2026-06-06.md`

## NEXT-SESSION ORDER
1. §11.10 cluster (Keck error + PR substitution + Bennu-as-derived + unit fix + Falcon Heavy + bib).
2. M3 Path-B: resolve the 5 open questions → apply the rework.
3. Item 3 Deepwater reconciliation (cross-corpus).
4. Remaining HARD items (defensibility-check each).
5. SOFT batch (relabels + bib sources).
6. Final confirmation burst (re-audit fixed file clean).
7. Author reviews path-scoped diff → approve → merge.
