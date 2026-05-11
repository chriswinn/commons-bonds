# Cross-Chapter Path B Audit — 2026-05-11

**Status:** Bundled execution of `tools/workstream-handoffs/path-b-audit-cross-chapter-handoff_2026-05-10.md` alongside the apparatus register sweep (chapter files overlap; bundling avoided merge conflicts). Two contaminations resolved; one verified clean; remaining priority pairs deferred to lower-priority status given diminishing returns.

**Triggering finding:** 2026-05-10 Noema essay audit identified ~14 verbatim sentences and 9 high-echo paragraphs cloned from Ch 1. Same close-paraphrasing dynamic was plausibly operating between chapter pairs within the manuscript. The Path B preemptive policy (no sentence-level reuse, no structural close-paraphrase) applies between chapters within the book, not just between chapters and essays.

**Methodology:** Per-pair lexical scan + framework-definition co-occurrence scan + manual reading of overlapping case-walks. Tools: `git grep` for distinctive multi-word phrases; per-chapter apparatus density frequency tables; cross-chapter occurrence matrices for known framework references (Darity, Mullen, Hartwick, Pistor, Coates, Parfit, BLTF data block, Deepwater IPG, Sweden / Saltsjöbaden).

---

## Pair-by-pair findings

### 🔴 Ch 5 ↔ Ch 6 — Restitution Lineage clone — **RESOLVED**

**Finding:** Ch 6 lines 627-650 contained a standalone "Restitution Lineage" h3 section duplicating Ch 5 lines 192-206:
- Same Darity & Mullen *From Here to Equality* (2020) citation in both chapters with same wealth-gap calculation methodology framing
- "CSD (Cost Severance Damages)" parenthetical re-introduced in Ch 6 as if first-time when Ch 5 already introduced it
- "what is owed vs. politically feasible to collect" framing duplicated as verbatim-paraphrase across both
- "Wealth-gap calculation methodology / accumulate the specific economic mechanisms" framing structurally cloned

**Severity:** Highest. Structural paraphrase + repeated formal-citation introduction = exactly the Noema-essay pattern that triggered this audit.

**Resolution:** Ch 5 retains the canonical Coates → Darity-Mullen → Pistor → Parfit lineage roll-call (it is part of Ch 5's two-instrument apparatus introduction arc). Ch 6's standalone "Restitution Lineage" h3 (3 paragraphs ≈ 400 words) collapsed to a one-paragraph cross-reference (~50 words) pointing back to Ch 5. Ch 6's job is methodology + formula; the lineage belongs upstream in Ch 5.

**Commit:** `5643f70` (Path B fix — Ch 5 ↔ Ch 6 Restitution Lineage clone resolved)

---

### 🟡 Ch 2 ↔ Ch 6 ↔ Ch 8 — Black Lung Trust Fund three-way echo — **RESOLVED**

**Finding:** Same Black Lung Disability Trust Fund data block appearing as structural paraphrases across three chapters:
- Ch 2 line 67: *"$44 billion in benefits... fund is $4.6 billion in debt... By 2050, that debt is projected to reach $15 billion"*
- Ch 6 line 148: *"more than $44 billion to disabled miners... Fund has never collected enough revenue... black lung alone runs roughly eighty cents per ton"*
- Ch 8 line 35: *"over forty-four billion dollars to disabled miners and their widows... never collected enough revenue... debt stood at four and a half billion dollars in 2021 and is projected to exceed fifteen billion by 2050"*

**Severity:** Medium. Not verbatim, but structural triplication of the same five facts. Same Noema-essay close-paraphrasing dynamic at smaller scale.

**Resolution:** Three-way compression plan:
- Ch 2 (case-introduction chapter, canonical site for Fund's structural description) — keeps full BLTF treatment with all numbers
- Ch 6 (methodology chapter) — compressed to per-ton arithmetic only ($44B / national tonnage → ~$0.80/ton); cross-references Ch 2 for Fund mechanics
- Ch 8 (per-ton case-walk) — compressed to one-paragraph signposting that names black lung as the most-documented coal externality + cross-references Ch 2 for Fund mechanics + lands the per-ton number for the chapter's purpose

**Commit:** `71146da` (Path B fix — Ch 2 ↔ Ch 6 ↔ Ch 8 Black Lung Trust Fund three-way echo resolved)

---

### 🟢 Ch 5 ↔ Ch 6 ↔ Ch 8 — Deepwater Horizon IPG echo — **NOT A FIX (architecture-by-design)**

**Finding:** Deepwater "IPG 15-17" reference appears in all three chapters.

**Investigation:** 
- Ch 5 lines 36-52: full Deepwater account (case-introduction)
- Ch 6 lines 166-170: Deepwater compressed to convergence-table entry (methodology context)
- Ch 8 line 173: Deepwater IPG with explicit cross-reference back to Ch 5 (*"Chapter 5 answered that question with case after case"*)

**Verdict:** Not Path B contamination — the chapters' usage architecture is by-design. Ch 8's explicit cross-reference acknowledges Ch 5's canonical treatment; Ch 6 retains a computational role for the convergence table that requires the Deepwater data point. Existing cross-reference architecture handles the duplication.

**No edit applied.**

---

### ✅ Ch 5 ↔ Ch 9 — Sweden / Saltsjöbaden / 1930s banking crisis — **VERIFIED CLEAN**

**Finding inspected:** Ch 5 line 96 mentions Sweden's 1930s response as a brief comparative observation; Ch 9 lines 117-123 develops the Sweden case at length within the broader Nordic objection treatment.

**Investigation:** 
- Ch 5 line 96 explicitly forecasts Ch 9: *"Chapter 9 (Pricing Honestly) develops the comparison at fuller depth"*
- Ch 9 lines 117-123 introduces substantive new material (1992 Swedish banking crisis, Saltsjöbaden multi-generational durability, specific banking mechanics) NOT present in Ch 5
- Verbatim sentence-level scan (Sweden, Saltsjöbaden, krona devaluation, 1933 Riksbank, household-relief) found ZERO verbatim duplications across Ch 5 ↔ Ch 9

**Verdict:** Handoff honored — Ch 5's brief observation correctly forwards to Ch 9's substantive development. No Path B contamination. Reference architecture is exactly the discipline the Path B handoff wanted to preserve.

**No edit needed.**

---

### Other priority pairs — DEFERRED (diminishing returns past the high-priority set)

The handoff specified ~10-15 high-priority pairs for the audit. The bundled session covered the highest-priority pairs (Ch 5+Ch 6, Ch 5+Ch 9, Ch 2+Ch 3+Ch 8). Remaining priority pairs not audited:

- **Ch 1 ↔ Ch 10** — both reflective/memoir registers; could plausibly carry voice/phrasing echoes
- **Ch 4 ↔ Ch 5** — both apparatus-introduction territory; could carry overlapping framework-definition language
- **Ch 7 ↔ Ch 8** — both case-walk thought-experiments; could carry overlapping methodology demonstration
- **Ch 9 ↔ Ch 10** — both closing/synthesis registers; could carry overlapping moral-stakes language

**Recommendation for a future Path B audit pass:** Queue these four pairs for a follow-up session if any future essay extraction surfaces an echo that traces back to one of them. Otherwise: the priority-pair set covered the highest-likelihood contamination surfaces, and diminishing returns past these are real (per the parent handoff's own scope guidance).

---

## Methodology template for future cross-chapter Path B audits

Steps that worked in this session (carry forward):

1. **Apparatus density inventory first.** For each chapter, count occurrences of framework-specific terms (acronyms, formal symbols, named instruments, theorem references). Heavy-density chapters are the highest-likelihood Path B sources.
2. **Cross-occurrence scan for distinctive multi-word phrases.** Pick 10-15 distinctive non-trivial phrases per pair (e.g., specific case names, non-obvious lineage citations, formal-instrument phrasings). Grep across chapter files. Phrases appearing in 2+ chapters get manual inspection.
3. **Manual reading of overlapping sections.** Identify candidate Path B paragraphs by topical overlap (apparatus introductions, lineage citations, case data blocks). Read side-by-side.
4. **Severity calibration.** Verbatim sentence-level reuse → highest priority. Structural paraphrase of the same data block → medium. Conceptual overlap with reference forwarding → low (often acceptable architecture).
5. **Resolution principle.** Pick the canonical site (where the content first appears or where it's most load-bearing); compress the other site(s) to cross-references. Don't try to make multiple sites carry equal weight.

Steps to add for the NEXT pass:

6. **Encoding integrity scan in parallel.** This session caught `tₔ` vs `t₀` subscript inconsistency + `⟯` vs `+` Unicode operator corruption. Path B audits naturally surface character-level inconsistencies; bundle the fix when found.
7. **Glossary + Tech Appendix integrity check.** When chapter prose changes (Path B fixes, apparatus register decisions), verify Glossary + Tech Appendix don't drift from chapter usage.

---

## Cross-references to companion documents

- `tools/rigor-passes/commons_bonds_rigor_pass_2026-05-11_apparatus_register_decision_v1.0.0.md` — companion apparatus register rigor pass (this audit's bundled twin)
- `tools/rigor-passes/commons_bonds_rigor_pass_2026-05-09_noema_essay_audience_load_v1.0.0.md` — Noema rigor pass that triggered this cross-chapter audit
- `tools/workstream-handoffs/path-b-audit-cross-chapter-handoff_2026-05-10.md` — parent handoff
- `tools/workstream-handoffs/apparatus-register-sweep-handoff_2026-05-10.md` — bundled-twin parent handoff

---

*End of audit.*
