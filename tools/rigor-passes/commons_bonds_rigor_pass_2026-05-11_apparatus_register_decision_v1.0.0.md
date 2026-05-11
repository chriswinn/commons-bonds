# Apparatus Register Decision Sweep — Rigor Pass v1.0.0 — 2026-05-11

**Status:** Ratified across 15 apparatus items + 2 Path B fixes + 3 adjacent-issue follow-ups, applied to `manuscript/chapters/`, `core/glossary/`, and `core/technical-appendix/`. Standing reference for future essay extractions and chapter polish work.

**Methodology:** Bundled execution of the apparatus register sweep (`tools/workstream-handoffs/apparatus-register-sweep-handoff_2026-05-10.md`) and the cross-chapter Path B audit (`tools/workstream-handoffs/path-b-audit-cross-chapter-handoff_2026-05-10.md`) — the two workstreams overlap heavily in the chapter files they edit; bundling avoided merge conflicts.

**Audience-load discipline applied:** Each apparatus item was tested against the dual-audience layman+specialist test ratified mid-session (2026-05-11). The session caught a methodological failure mode in the original recommendations: defaulting to "shorter = trade-press-friendly" rather than asking what the substance actually requires. Substance-drives-length principle (per `feedback_substance_drives_length.md`) governs the final recommendations.

**Trade-comp shelf:** Mazzucato (*The Value of Everything*), Raworth (*Doughnut Economics*), Pistor (*The Code of Capital*), Sandel (*What Money Can't Buy*), Sen-in-trade-mode (*Development as Freedom*), Piketty (*Capital in the Twenty-First Century*).

---

## Headline finding (changed scope at session start)

**`cluster-α / β / γ` typology does not exist in any chapter** (zero occurrences across all 10 chapter drafts + AuthorsNote). The Noema-essay disqualifying flag (`cluster-γ` ⚠⚠⚠ at Section VI.1) was an essay-drafting artifact — the essay introduced apparatus the chapters do not use. The chapters' actual apparatus problems were different and concrete (catalogued below).

---

## Per-item ratified decisions

### Trade-body apparatus (chapter prose) — ratified register

| Apparatus | Decision | Rationale |
|---|---|---|
| Inline integral `RCV = ∫ (Σ Cᵢ) · D dt` mid-paragraph | **Strip from Ch 8 trade prose; appendix cross-reference only** | Ch 8 does concrete per-ton arithmetic; integral notation collapses register mid-paragraph. Item 1 (commit `d1f6e2d`). |
| Full integral formula `RCV(R, t₀) = ∫…dt` in Ch 6 | **Keep** (Ch 6 is the methodology chapter; earns the formula via the explicit "skip the formulas" affordance at line 138) | Item 2 (commit `baf3776`). |
| Shorthand identities `CS = RCV − B` and `IPG = RCV / Pmarket` in Ch 6 | **Keep, strip function arguments `(R, t₀)`** | Glossary + appendix carry full functional form for symbol-curious. Item 3 (commit `39a8416`). |
| `B / RCV ≈ 0.40` symbol-arithmetic mid-Deepwater-case-walk in Ch 5 | **Rewrite without symbols** (*"The framework's accountability target is one hundred percent — extractors paying the full residual cost. Deepwater paid forty."*) | Item 4 (commit `4d012fb`). |
| Restitution Bond / Foreclosure Bond names in Ch 5 | **Keep named instruments; drop B₁/B₂ subscripts in body** | Mazzucato-discipline: keep memorable named concepts; drop subscript apparatus tax. Items 5, 6 (commits `19e91d1`, `547346a`). |
| CSD acronym | **Introduce once in Ch 5 (apparatus chapter); drop in Ch 6+ in favor of "Restitution Bond's accounting"** | Cross-chapter consistency with named-instrument discipline. Item 6 (commit `547346a`). |
| CIT acronym | **Drop everywhere in chapter prose; expand to "Commons Inversion Test"** (11 expansions across Ch 6) | Sub-form acronyms CAI/CCI never appeared in chapter prose; full names already in Ch 7/Ch 8. Item 7 (commit `4f32743`). |
| Hotelling Identity passage | **Polish-not-compress (Option C)** — addressed Pigou circularity, jargon compounds, and redundant identity-restatement | Caught session methodology failure: compression ≠ accessibility. Item 8 (commit `067f5a1`). |
| `Method 3's α-dominance finding` | **Replace with named navigation aid** (*"Section 8 — Asymmetric Regret Rule, with empirical evidence from Method 3 (Scarcity-Adjusted Option Value)"*) | Greek-letter Unicode breaks search on multiple e-readers; named sections work for paper-scanner + digital-searcher + layman + specialist. Item 9 (commit `cf682be`). |
| `Section L`, `Section M` letter labels in Ch 6 | **Replace with named content** (*"Four Gates Admission Apparatus section"*, *"Formula Generalization section"*) | Same wayfinding logic as Item 9. Item 10 (commit `16876a1`). |
| `Theorem E.3` in Ch 7 | **Add named content** (*"Theorem E.3 (Abundance Masking)"*) | Specialist still gets precise reference; layman now knows what they'll find. Item 10 (commit `16876a1`). |
| `primitive equation` terminology | **Standardize manuscript-wide to `central equation`** (3 trade-body edits + 4 appendix edits) | One-name-for-one-thing principle. Cross-chapter inconsistency: Ch 5 used "central equation" while Ch 6 used "primitive equation" for the same equation. Item 11 (commits `76cb0e4`, `cfde88c`). |
| ARR / Asymmetric Regret Rule | **No-op** — discipline already in place. All chapter prose uses full name; appendix uses ARR after parenthetical introduction (academic register). Item 12. |
| IPG acronym | **No-op** — discipline already in place. Both chapters introduce full name with plain-English gloss before deploying acronym; table headers + formulas use compact form for layout. Item 13. |
| RCV acronym | **Sandel-style hybrid (Option B)** — full-name expansion for single-use occurrences (8 expansions in Ch 6 + 1 in Ch 8); acronym retained in formulas, dense intra-paragraph repeat-references, parallel-structure case-walks, table headers, named methods. Plus add introduction parenthetical at Ch 6 line 138 (was deploying acronym before introduction — actual audience-load gap). | Item 14 (commit `214af4a`). |
| Six-pattern enumerated bolded list in Ch 7 | **Strengthen Ostrom-path framing + light de-formalize** — explicit "illustrative, not exhaustive" + Ostrom/Sen/Rawls lineage citation; drop "The first / The second / …" enumeration markers but keep bolded pattern names for back-reference navigation | Item 15 (commit `b1c17d8`). |

### Tech Appendix (formal register) — register decisions

| Apparatus | Decision | Rationale |
|---|---|---|
| Formal symbols (B, B₁, B₂, RCV, Cᵢ, integrals) | **Keep** — academic register appropriate for appendix audience |
| ARR acronym in appendix body prose | **Keep** — standard academic-paper discipline (parenthetical introduction at section header, then acronym for compactness) |
| `central equation` terminology | **Standardize to match trade body** (4 edits at appendix lines 554, 1122, 3482, 6498) — one-name-for-one-thing across whole manuscript |
| `B₁ / B₂` subscripts | **Keep** — academic register appropriate; Glossary line 115 + Tech Appendix line 1130 carry the canonical decomposition |

---

## Path B fixes (cross-chapter contamination resolved)

Two contaminations found and resolved during the bundled sweep:

1. **Restitution Lineage clone (Ch 5 ↔ Ch 6)** — Ch 6 lines 627-650 had a standalone "Restitution Lineage" h3 section duplicating Ch 5 lines 192-206 (same Darity/Mullen citation, "what is owed vs. politically feasible" framing, CSD parenthetical re-introduction). **Fix:** Ch 5 retains canonical lineage roll-call (Coates/Darity-Mullen/Pistor/Parfit); Ch 6 collapsed to one-paragraph cross-reference (~400 words → ~50 words). Commit `5643f70`.

2. **Black Lung Trust Fund three-way echo (Ch 2 ↔ Ch 6 ↔ Ch 8)** — Same data block ($44B distributed, $4.6B debt, $15B by 2050) appearing as structural paraphrases across three chapters. **Fix:** Ch 2 retains full BLTF treatment with all numbers (case-introduction site); Ch 6 compressed to per-ton arithmetic; Ch 8 compressed to one-paragraph cross-reference + per-ton number. Commit `71146da`.

3. **Verified clean — Ch 5 ↔ Ch 9 Sweden / Saltsjöbaden:** Ch 5 line 96 is brief observation pointing forward; Ch 9 lines 117-123 develops at length with substantive new material (1992 Swedish banking crisis, Saltsjöbaden multi-generational durability). Handoff honored — no Path B contamination.

---

## Adjacent issues handled in-session

1. **Encoding bugs (Item 3 + Item 14 follow-up):** Ch 6 had `tₔ` subscript inconsistency (8 instances total: line 275 + lines 278/285/294 + line 736) instead of canonical `t₀` used by appendix + glossary. Plus `⟯` Mathematical Right White Tortoise Shell Bracket character (U+27EF) at lines 275 and 736 where canonical formula has `+`. Both fixed — zero encoding residuals across all chapter drafts. Commits `39a8416`, `214af4a`, `5f143b0`.

2. **Tech Appendix §7-vs-§8 ARR section-numbering discrepancy:** TOC + main heading placed Asymmetric Regret Rule at §8; body cross-reference at line 950 said §7; subsections at 2784/2790 mislabeled §7.1/§7.2 instead of §8.1/§8.2. **Fixed.** Commit `ede6d88`. Wayfinding integrity prerequisite for Item 9's Ch 6 cross-reference.

3. **`why bonds` apparatus-defense paragraph** — substantive gap surfaced (book's choice of "bond" as umbrella instrument was asserted, never defended in body prose). Spawned as separate task; auto-completed during session and integrated into Ch 5 (commits `f5f905e`, `47bd6d4`, `2c8138f` — ran on parallel session).

---

## Adjacent issues flagged for separate workstream

**Tech Appendix dual-numbering reconciliation** (handed to PM session 2026-05-11): Tech Appendix runs TWO parallel section-numbering systems for the same content (numeric §1-§9 in TOC + main headers; letter A-M in body subsection structure). Example: Four Gates Admission Apparatus is BOTH §7 (TOC line 194 + main heading line 2316) AND Section L (subsection structure at lines 2342-2730 with L.1, L.2, L.3, L.4 sub-gates). Same pattern likely affects multiple sections. Cascade effect: chapter cross-references to the appendix use mixed numbering systems (Ch 6 line 788 uses "Section 8"; Ch 7 line 119 uses "Theorem E.3"). Once appendix canonicalizes to one scheme, all chapter cross-references should be re-validated.

Specific items flagged:
- Tech Appendix line 4868: `(§8 / supplement §7)` — has §8 correct but "supplement §7" reference is unclear (§7 is Four Gates, not a supplement to ARR). Needs author judgment.
- Section L (Four Gates) duplicates §7 (Four Gates Admission Apparatus). Pick canonical.
- Likely similar parallel-numbering patterns affect Section E (Theorems E.1-E.4), Section M (Formula Generalization), and others.

---

## Reusable principles surfaced by this sweep

1. **Dual-audience layman+specialist test (ratified 2026-05-11):** Every register decision gets tested against BOTH audiences. Specialist-only optimization fails layman; layman-only optimization fails specialist. Most apparatus has a third option that serves both (e.g., named navigation aid instead of Greek-letter shortcut).

2. **Compression ≠ accessibility (caught mid-session):** Default tendency is "shorter = trade-press-friendly." Honest tendency is "what does the substance require?" Sometimes substance requires MORE prose (Mazzucato-style plain-English foothold) not LESS. The Hotelling Identity polish (Item 8) was the canonical example — the original semicolon-dense compression was wrong; Sandel-style polish-not-compress was right.

3. **Sandel hybrid pattern (Item 14):** For hybrid acronyms (named-quantity that's also descriptive phrase), apply contextual discipline rather than blanket rule. Single-use occurrences → expand to full name; dense intra-paragraph repeat → keep acronym; formulas/headers/named methods → keep acronym. Sandel does this naturally with "moral limits" in *What Money Can't Buy*.

4. **Ostrom-path discipline (ratified 2026-05-02 in `reference_ostrom_illustrative_register.md`; applied in Item 15):** Lists are illustrative not exhaustive. Cite Ostrom/Sen/Rawls lineage. Open-list affordance ("readers may surface additional patterns"). Preserves framework defensibility against the "name a seventh thing and the framework has a hole" attack.

5. **Wayfinding > shorthand for cross-references (Items 9, 10):** Chapter cross-references to the appendix should use named content (e.g., "Section 8 — Asymmetric Regret Rule") rather than opaque labels (e.g., "Method 3's α-dominance finding"). Greek-letter Unicode breaks search on multiple e-readers; named sections work for paper-scanner + digital-searcher + layman + specialist simultaneously.

6. **Cross-chapter consistency check** (caught Items 11, 14): Same concept named differently across chapters (Ch 5 "central equation" vs Ch 6 "primitive equation") creates reader friction. Standardize.

7. **Encoding integrity** (caught Items 3, 14 follow-up): Subscript characters (`tₔ` vs `t₀`) and Unicode operator characters (`⟯` vs `+`) silently diverge from canonical appendix/glossary forms. Worth a project-wide encoding-integrity scan as a separate audit pass.

---

## Reference files for future sessions

- `manuscript/chapters/Chapter*Draft*` — all 10 chapters (post-sweep state)
- `core/glossary/commons_bonds_updated_glossary_v4.html` — canonical glossary (updated for "central equation" standardization)
- `core/technical-appendix/TechnicalAppendix_v2.0.0.html` — formal apparatus (updated for §7→§8 ARR reconciliation + "central equation" standardization; pending: parallel-numbering audit)
- `tools/rigor-passes/commons_bonds_rigor_pass_2026-05-09_noema_essay_audience_load_v1.0.0.md` — Noema rigor pass (severity calibration framework + 14-character audience set)
- `tools/workstream-handoffs/apparatus-register-sweep-handoff_2026-05-10.md` — parent handoff
- `tools/workstream-handoffs/path-b-audit-cross-chapter-handoff_2026-05-10.md` — Path B parent handoff
- `research/audits/cross-chapter-path-b-audit_2026-05-11.md` — companion audit document

---

## Scope of NEXT apparatus pass (when warranted)

This sweep was bundled execution of the apparatus + Path B handoffs. A future apparatus-pass session might address:

1. **Tech Appendix dual-numbering reconciliation** (handed to PM session 2026-05-11; will get its own workstream branch)
2. **Cross-chapter Path B audit on additional pairs** — this session covered Ch 5+Ch 6, Ch 5+Ch 9, Ch 2+Ch 3+Ch 8 priority pairs. Lower-priority pairs (Ch 1+Ch 10, Ch 4+anything, Ch 7+Ch 8) not yet audited; diminishing returns expected past the priority set.
3. **Project-wide encoding-integrity scan** — surfaced in this session (`tₔ` vs `t₀`; `⟯` vs `+`); broader scan likely surfaces additional Unicode inconsistencies across the manuscript.
4. **Glossary consistency audit** against Tech Appendix — both have been independently maintained; subscript notation, equation references, and section cross-references may have drift.

---

*End of rigor pass.*
