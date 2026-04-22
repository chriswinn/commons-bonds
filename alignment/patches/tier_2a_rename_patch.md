# Tier 2a Rename: "Individual Risk Cost" → "Actuarial Risk Cost"
## Change Summary — WS02 and WS03

---

## WS02 — 02_glossary_reconciliation.md

### Change 1: Eight-tier canonical list table (§ "The eight tiers — canonical list")

**FIND:**
```
| 2a | Individual Risk Cost | Institutional | Partially |
```

**REPLACE WITH:**
```
| 2a | Actuarial Risk Cost | Institutional | Partially |
```

---

### Change 2: "New terms proposed in vocabulary-additions 13" table — Mission Failure Reserve verdict

**FIND:**
```
| Mission Failure Reserve | PROMOTE from provisional | Passes as sub-tier (2b) under Individual Risk. Belongs in glossary for clarity. Rare in existing frameworks — "Mission Failure Reserve is structurally absent from most extraction contracts" is a strong line. |
```

**REPLACE WITH:**
```
| Mission Failure Reserve | PROMOTE from provisional | Passes as sub-tier (2b) under Actuarial Risk Cost. Belongs in glossary for clarity. Rare in existing frameworks — "Mission Failure Reserve is structurally absent from most extraction contracts" is a strong line. |
```

---

### Rationale note to add (append to § "Term-by-term decisions" intro or as a footnote to Tier 2a row):

> **Tier 2a naming:** "Individual Risk Cost" replaced by "Actuarial Risk Cost" (Decision A ratification, April 19, 2026). The actuarial framing is more precise: the tier prices a *population-level statistical distribution* of occupational and environmental health outcomes, not an individual harm. This aligns with how insurance, public health, and regulatory systems actually measure and absorb these costs. "Individual" was descriptively inaccurate — the tier is not priced per individual, it is priced per exposed population using actuarial methods.

---

## WS03 — 03_chapter_6_integration.md

### Change 1: "The new fourth section: RCV Decomposed" → "What the section covers" → item 4

**FIND:**
```
4. **The eight tiers, each as a paragraph:** Lifetime Survival, Individual Risk (with Mission Failure Reserve as sub-tier), Dynastic Labor, Foreclosure, Community Transition Reserve, Ecological Carrying, Knowledge and Culture, Political Capture.
```

**REPLACE WITH:**
```
4. **The eight tiers, each as a paragraph:** Lifetime Survival, Actuarial Risk Cost (with Mission Failure Reserve as sub-tier 2b), Dynastic Labor, Foreclosure, Community Transition Reserve, Ecological Carrying, Knowledge and Culture, Political Capture.
```

---

### No other occurrences of "Individual Risk" found in WS03.

---

## Summary of occurrences across all uploaded files

| File | Occurrences | Status |
|------|-------------|--------|
| 02_glossary_reconciliation.md | 2 (tier table + Mission Failure verdict) | Changes above |
| 03_chapter_6_integration.md | 1 (tier paragraph in section 4) | Change above |
| commons-bonds-vocabulary-additions_13.html | 1 ("Sub-tier within Individual Risk Cost" in Mission Failure Reserve entry) | ARCHIVE — this file is source-only, not canonical; no edit needed |
| commons_bonds_updated_glossary.html | 0 direct occurrences (uses old taxonomy: "Immediate Survival," "Lifetime Health" etc.) | Full eight-tier section replacement needed — see companion glossary file |
| CommonsBondsTechnicalAppendixv0_0_1.html | 0 direct occurrences (uses yet another taxonomy) | C.4 section replacement needed — see companion HTML block file |

---

## Broader context flag

The Tech Appendix Section C.4 and the Glossary both use **pre-v10 eight-tier taxonomies** that are entirely different from the canonical v10 list. The Tier 2a rename is technically a no-op in those files (the term doesn't appear) but both files need their tier sections updated to canonical v10 — which is where "Actuarial Risk Cost" gets introduced as the canonical Tier 2a label. Those updates are in the companion files delivered with this change summary.

Also note: Definition A.8 in the Tech Appendix lists **only 6 abundance layers** (missing "political"). The canonical v10 has 7. This is a separate fix needed in A.8 and C.2 — flagged for a future pass.
