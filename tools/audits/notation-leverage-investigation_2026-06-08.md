# Notation-leverage investigation — result (2026-06-08)

**Status: PROPOSED for author consideration. NOT applied.** Read-only investigation (per author request during the M3 Path-A work): *which spelled-out constructs would benefit from citable notation, and which should stay descriptive?* Sources: symbol registry, TA, chapters.

## Core finding — two notation layers with opposite needs
1. **Quantities that enter equations** — RCV, CSD, CS, B/B₁/B₂, IPG — **already symbolized correctly** and heavily used; a citing paper lifts them verbatim. No change needed; the only open issue is collision-hygiene (owned by the registry).
2. **Methodological apparatus / procedures** — CiT, the Four Gates, the Three Ways of Counting (M1/M2/M3), CAI/CCI — are **tests/protocols, not quantities.** The TA itself states this layer distinction (§6.7, L1868: *"CIT is a TEST… the others are CONDITIONS… naming asymmetry honors the layer distinction"*). External citers reference these **by name**, not by symbol. **Symbolizing procedures = over-formalization that hurts the lay+specialist dual audience.**

## Recommendations

**① HIGHEST VALUE — name the master identity (a NAME, not a symbol).**
`total CS = (CSD − B₁) + (RCV − B₂)` (TA L1212, L1409) is the object most likely to be cited and built on (Darity-style reparations economics), but it currently has **no compact name** and lives in §5 prose. Give it a citable label — **"Cost Severance Decomposition"** (the phrase already appears descriptively at TOC L184) or **"Two-Instrument Identity"** — exactly parallel to the framework's already-named **Hotelling Identity** (L1171). Zero readability cost, zero collision risk, pure citability gain. *This is the single change most likely to help external citers.*

**② OPTIONAL, low value — `G1–G4` gate shorthand** for the few cross-reference-dense TA passages only (e.g. §5.5 L1394 enumerates "Gate 1… Gate 2… Gate 3… Gate 4" in one paragraph). Collision-free (registry Part 2 uses `A1–A4` Assumptions + `P1–P4` Premises as label families; `G` is unused). Keep the full self-documenting gate **names** (CiT / Units / Boundedness / Independence) everywhere else. Do only if the spelled-out enumerations read clunky.

## Explicit "leave alone" (symbolizing these would HURT)
- **RCV, CSD, CS, B/B₁/B₂, IPG** — already optimal.
- **CiT, CAI, CCI** — abbrev-only is correct; do NOT create a gate-pass predicate / test-operator (the test is a verbal counterfactual; a symbol reads as apparatus-theater).
- **Three Ways / M1·M2·M3** — named-methods + M-abbrev already optimal; do NOT add a triangulation operator (triangulation is a report-all-three *discipline*, not a function).
- **Four Gate *names*** — self-documenting; must stay descriptive for the dual audience.
- **Method-3 internals (ς, α, δ→κ)** — owned by the M3 Path-A decision + registry Batches; not a greenfield notation question.

## Adjacency flag (existing-symbol hygiene, not new-notation)
Registry Batch I-5 (deferred): **bare `B` vs the "billion" suffix** in §11 worked numbers (~50 occurrences) is the one place an *existing* symbol is genuinely reader-confusing in the quantitative passages a referee reads closely. Owned by the provenance session; worth closing before external circulation.

## Confidence
High on the layer distinction (TA-stated), notation status (line-cited), and `G1–G4` being collision-free. Frequency counts grep-based (order-of-magnitude). Could not verify Darity's specific citation preferences (no external correspondence in scope).
