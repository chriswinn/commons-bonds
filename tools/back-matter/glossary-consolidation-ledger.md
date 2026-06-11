# Glossary consolidation ledger — scaffolding companion

**Created 2026-06-09 (back-matter consolidation session).** This is the INTERNAL
scaffolding companion to the clean reader-facing `manuscript/back-matter/glossary.html`.
It records the v2→v3→v4 lineage, the canonicity decision, the retired/superseded
terms (kept OUT of the reader-facing file), the v3→v4 regression check, and the
open reconciliation items. The reader-facing glossary carries none of this.

## Canonicity decision (author-ratified 2026-06-09)

**Source of truth going forward: `tools/back-matter/sources/glossary/commons_bonds_updated_glossary_v4.html`.**
- v2 — SUPERSEDED 2026-04-29 (self-marked → v3). Archival.
- v3 — self-declared "Canonical Vocabulary Glossary — v3" (2026-04-24, 28 terms).
- v4 — latest (2026-05-02; +Ch2 severance term-choice note 2026-06-05), 39 terms, superset.

Author direction: **use v4 going forward, but dedupe/reconcile across v2+v3+v4 AND the
TA's inline term definitions** (consolidation, not a copy). v2/v3 are retained as archival
history; the clean reader-facing glossary is generated from v4 by `build.py gen-glossary`,
which **drops the "Retired and superseded terms" section** (scaffolding — those markers must
not appear reader-facing) and injects per-term anchors.

## Retired / superseded terms (moved here OUT of the reader-facing glossary)

These lived in v4's `retired-section`. They are framework history, not reader-facing
vocabulary. Kept here so the lineage is preserved without shipping "superseded" markers to
readers (per the corpus rule: retired/historical markers stay in internal working files only).

| Retired term | Disposition |
|---|---|
| Abundance Inversion Test (AIT) | → Commons Inversion Test (CIT) |
| Asymmetric Regret Principle (ARP) | → Asymmetric Regret Rule (ARR) |
| Civilizational Substitutability Gap (CSG) | retired → prose "existential substitutability gap" |
| Cost Bearing | demoted to prose-only |
| Dynastic Labor Cost | → Lineage Labor Cost |
| Eight-Tier FGC Decomposition | retired → Cᵢ via Four Gates |
| Full Generational Cost (FGC) | retired → RCV / Σᵢ Cᵢ |
| Industrial-existential substitutability gap | → "existential substitutability gap" |
| Knowledge and Culture Cost | → Knowledge and Cultural Cost |
| Reparations Bond (working label) | → Restitution Bond (B₁) |
| Resource-Foreclosure Bond (working label) | → Foreclosure Bond (B₂) |
| Reversibility Default (RD) | → Asymmetric Regret Rule (ARR) |
| Spatial Cost Severance (capitalized) | → lowercase prose "spatial cost severance" |
| Temporal Cost Severance | retired → "intergenerational cost severance" prose |
| Triangulated RCV Estimation | → Three Ways of Counting |
| Universality Test | retired → prose scope claim |
| Value Capture | retired → Value Extraction |

## v3 → v4 regression check (2026-06-09)

Term-name set diff (v3 = 28 names, v4 = 39). Nearly all v3 names absent from v4 are
**clean renames** that v4 carries under cleaned names (and lists in its retired-section):
- Externality Tail E(R, t) → **Externality Tail (E)**
- Substitutability Function S(t\|t₀) → **Substitutability Function (S)**
- Value Extraction → **value extraction (lowercase prose phrase)**
- Severed Cost → **severed cost (lowercase prose phrase)**
- Asymmetric Regret Principle → **Asymmetric Regret Rule** (ARP retired)
- CS = RCV − B (Cost Severance equation) → **CS = RCV − B equation**
- Eight-Tier FGC Decomposition (v10) → retired in v4
- Spatial Cost Severance (capitalized) → retired in v4 + lowercase prose phrase added

**⚠ ONE FLAG to verify (author): "Abundance Dimension"** is present in v3 but absent from v4
with no obvious rename. Confirm it was intentionally dropped (likely folded into the "Commons
categories — 10 examples" + abundance-state framing) rather than lost. Not a reader-facing
blocker — the reader-facing glossary follows v4 — but the lineage should record the disposition.

## Open reconciliation items (deferred — flagged for a follow-up pass)

1. **TA inline term definitions.** The Technical Appendix defines/uses framework terms inline
   (e.g. "Notational convention" notes; the RCV integrand prose; Four Gates). These are not yet
   reconciled against the v4 glossary term set. A future pass should confirm every TA-defined
   framework term has a matching glossary entry (and vice-versa) so the two agree. Low risk
   (the glossary is already curated reader prose); deferred for scope.
2. **terms_index.md.** `tools/back-matter/sources/terms_index.md` (1,915-line internal term-provenance source)
   is the deeper provenance layer behind the glossary. Not touched this session. If the glossary
   is ever regenerated from terms_index (rather than curated v4 prose), that is a separate workstream.
3. **v2/v3 retirement.** Once v4 is confirmed canonical and the reader-facing glossary ships,
   v2/v3 can be moved to `archive/` (deferred-move; not done this session per the build-new/defer-moves
   decision). v2 is already self-marked SUPERSEDED.

## How the reader-facing glossary is produced

`python3 tools/back-matter/build.py gen-glossary`
→ reads v4 → strips retired-section + version markers → injects `id="term-<slug>"` anchors
→ writes `manuscript/back-matter/glossary.html` (zero scaffolding).
