# Commons Bonds — Retirement Archive Index

**Established:** 2026-04-30 by Insight #59 (Working Principle #4 refinement; Tiered retirement-trace policy + retirement-archive index combined).

**Purpose:** Single canonical index for all retirement events across the Commons Bonds project — vocabulary renames; methodology retirements; file/artifact retirements. Other scaffolding documents reference this index rather than carrying full retirement traces inline (per refined Working Principle #4).

**Discipline (refined per Insight #59):** This index is the **canonical retirement-archive**. Per WP#4 refined tiered policy:
- **Active scaffolding** (open insights; pending rigor passes) preserves full traces (status quo).
- **Ratified rigor passes** preserve full traces (frozen + dated; canonical decision-record).
- **Working principles + vocabulary strategy** carry light traces with cross-reference here.
- **terms_index v1.0.0+** carries summary-level traces; full traces here.
- **Publisher-facing artifacts** carry no traces (status quo per WP#8).

Each entry links to the canonical rigor pass that ratified the retirement; that rigor pass remains the source-of-truth for the full audit trail.

---

## §0. Archive structure convention (Insight #62 ratified 2026-04-30)

The project uses a **hybrid archive structure**:

- **Top-level [`archive/`](../) — cross-domain retirement material + multi-book seed:**
  - `archive/retirements/index.md` (this file) — single canonical retirement-trace index per refined WP#4
  - `archive/decomposition/` — retired methodologies surfaced from any domain (e.g. 8-tier decomposition)
  - `archive/_OneDayMaybe/` — Book 2 / Book 3 / satellite-essay seed material
- **Per-domain `<domain>/archive/` — domain-specific historical predecessors kept adjacent to live work:**
  - [`core/technical-appendix/archive/`](../../core/technical-appendix/archive/) — superseded TA versions + supplements
  - [`manuscript/chapters/archive/`](../../manuscript/chapters/archive/) — Ch 6 supplementary drafts pending integration
  - [`tools/archive/`](../../tools/archive/) — superseded methodology versions

**Single search location for retirement provenance:** this index (§§1–3 below). Per-domain archives are *file predecessors*, not retirement records.

**Verdict (c) ratified per Insight #62:** the cross-domain audit-trail need is solved by this canonical index; per-domain archives encode origin context next to live work, which Working Principle #10's "internal scaffolding can be rich" license endorses. Full consolidation (option (a)) was rejected for low marginal navigability gain vs. ~10–20 path-update cost + loss of domain-context proximity.

---

## §1. Vocabulary retirements

| Date | Original term | Replacement / disposition | Insight # | Rigor pass |
|---|---|---|---|---|
| 2026-04-24 | Abundance Inversion Test (AIT) | Commons Inversion Test (CIT) | (pre-Insight tracking) | `tools/rigor-passes/commons_bonds_rigor_pass_2026-04-24_term_cit_rename_v1.0.0.md` |
| 2026-04-24 | Asymmetric Regret Principle (ARP) | Asymmetric Regret Rule (ARR) | (pre-Insight tracking) | `tools/rigor-passes/commons_bonds_rigor_pass_2026-04-24_term_asymmetric_regret_principle_v1.0.0.md` |
| 2026-04-24 | Reversibility Default (RD) | Asymmetric Regret Rule (ARR) — same-day flip | (pre-Insight tracking) | terms_index entry "Reversibility Default (RD) — RATIFICATION REVERSED 2026-04-24 (same-day flip)" |
| 2026-04-24 | Reparations Bond | Restitution Bond (B₁) | (pre-Insight tracking) | `tools/rigor-passes/commons_bonds_rigor_pass_2026-04-24_b1_b2_naming_v1.0.0.md` |
| 2026-04-24 | Resource-Foreclosure Bond | Foreclosure Bond (B₂) | (pre-Insight tracking) | `tools/rigor-passes/commons_bonds_rigor_pass_2026-04-24_b1_b2_naming_v1.0.0.md` |
| 2026-04-24 | Civilizational Substitutability Gap (CSG; Tier D coinage) | Tier C demotion → "industrial-vs-existential substitutability gap" descriptive prose | (pre-Insight tracking) | `tools/rigor-passes/commons_bonds_rigor_pass_2026-04-24_term_csg_v1.0.0.md` |
| 2026-04-24 | Universality Test (Tier D) | Tier C demotion → "the universality test" descriptive prose | (pre-Insight tracking) | `tools/rigor-passes/commons_bonds_rigor_pass_2026-04-24_term_universality_test_re_examination_v1.0.0.md` |
| 2026-04-24 | Spatial Cost Severance (proper-noun) | spatial cost severance (lowercase descriptive prose) | (pre-Insight tracking) | `tools/rigor-passes/commons_bonds_rigor_pass_2026-04-24_term_spatial_cost_severance_re_examination_v1.0.0.md` |
| 2026-04-24 | Temporal Cost Severance (proper-noun) | Demoted then RECONSIDERED — Tier C lowercase preserved | (pre-Insight tracking) | `tools/rigor-passes/commons_bonds_rigor_pass_2026-04-24_term_temporal_cost_severance_v1.0.0.md` + `..._reconsider_v1.0.0.md` |
| 2026-04-24 | Cost Bearing (proper-noun framework term) | Tier C demotion; descriptive prose only | (pre-Insight tracking) | terms_index entry §704 `Cost Bearing` |
| 2026-04-24 | Full Generational Cost (FGC) | RETIRED — replaced by Cᵢ admitted via Four Gates per Path F + tier-reframing | (pre-Insight tracking) | `tools/rigor-passes/commons_bonds_rigor_pass_2026-04-24_tier_reframing_v1.0.0.md` §11.2 |
| 2026-04-24 | Value Capture | Value Extraction (preferred reframing) | Insight #28 | `tools/rigor-passes/commons_bonds_rigor_pass_2026-04-24_term_value_capture_vs_extraction_v1.0.0.md` |
| 2026-04-28 | Triangulated RCV Estimation | Three Ways of Counting | Insight #31 | `tools/rigor-passes/commons_bonds_rigor_pass_2026-04-28_triangulated_rcv_estimation_naming_review_v1.0.0.md` |
| 2026-04-29 | industrial-existential substitutability gap | existential substitutability gap (per Bostrom + MacAskill + Ord disambiguation) | Insight #33 | `tools/rigor-passes/commons_bonds_rigor_pass_2026-04-28_csg_descriptive_prose_renaming_v1.0.0.md` |
| 2026-04-29 | Knowledge and Culture Cost | Knowledge and Cultural Cost (C1 form canonical) | Insight #34 | `tools/rigor-passes/commons_bonds_rigor_pass_2026-04-29_group2_knowledge_culture_cost_naming_v1.0.0.md` |
| 2026-04-30 | Dynastic Labor Cost | Lineage Labor Cost — class-connotation cleanup | Insight #56 | `tools/rigor-passes/commons_bonds_rigor_pass_2026-04-30_group1_1_labor_cost_naming_v1.0.0.md` |

---

## §2. Methodology retirements

| Date | Original methodology | Disposition | Insight # | Rigor pass |
|---|---|---|---|---|
| 2026-04-24 | 8-tier decomposition (Tiers 1–8 as canonical taxonomy) | RETIRED — replaced by Cᵢ indexed cost variables admitted via Four Gates per Path F | (pre-Insight tracking) | `tools/rigor-passes/commons_bonds_rigor_pass_2026-04-24_tier_reframing_v1.0.0.md` §11.2 + `..._path_f_variable_addability_v1.0.0.md` |
| 2026-04-24 | "Canonical taxonomy" framing for 10 abundances | REFRAMED — Path F: 10 abundances are *variables AIT has discovered across cases*, not closed ontological taxonomy | (pre-Insight tracking) | `tools/rigor-passes/commons_bonds_rigor_pass_2026-04-24_path_f_variable_addability_v1.0.0.md` |

---

## §3. File / artifact retirements

| Date | Original location | Disposition | Insight # | Rigor pass / commit |
|---|---|---|---|---|
| 2026-04-30 | `core/decomposition/eight-tier-v10.html` | Archived → `archive/decomposition/eight-tier-v10.html` (8-tier scheme retired 2026-04-24; directory archived per Insight #55 hygiene pass) | Insight #55 (hygiene pass authorization 2026-04-30) | This commit's `dac1ab3` archive operation |
| 2026-05-02 | `core/dimensions/commons_bonds_abundance_dimensions_v1_3_0.md` | Content absorbed into Tech Appendix §C.2 + new §C.2.1 (per-category profiles for all 10 commons categories: Habitability · Spatial · Temporal · Institutional · Kindred · Ecosystem · Political · Cohesion · Epistemic · Autonomy); source file archived to `archive/dimensions/` with Tier-2 header-note per WP#4; `core/dimensions/` directory removed | Insight #55 + Phase α.2.7c rebuild | Phase α.2.7c batched commit (Tech Appendix v2.0.0 absorption) |
| 2026-04-29 | `~/Documents/___WorkingOn/commons-bonds` | Project relocated to `~/commons-bonds` (escape iCloud Documents-sync corruption) | (Session handoff v1.47.0 §2.5) | Session handoff v1.47.0 |

---

## §4. Tier-2 archived files (reference)

Per Working Principle #4 + #8, Tier-2 archived files preserve a header-note retirement annotation but otherwise retain full content for provenance. Listed here for index completeness:

- `manuscript/chapters/archive/Chapter__6___SupplementaryDrafts_2026-04-24.md` — Ch 6 supplementary drafts archived per Insight #30 + Hotelling Identity §12 cleanup.
- `tools/archive/commons_bonds_rigor_protocol_v1.3.0.md` — superseded by v2.x.
- `tools/archive/commons_bonds_layer_tier_stress_test_1_0_0.md` — superseded by Path F + tier-reframing.
- `archive/decomposition/eight-tier-v10.html` — see §3 above.
- `archive/_OneDayMaybe/` — author meta-archive.

---

## §5. Cross-references

### §5.1 Working Principle anchors

- **Working Principle #4** (refined per Insight #59) — retirement-trace discipline; tiered policy points to this index.
- **Working Principle #8** (publisher-facing scrub) — complementary; publisher-facing artifacts carry no traces.
- **Working Principle #1** (effort-to-repair-not-rigor) — supports the refinement; we don't preserve traces because changing them is hard, we preserve them when load-bearing.

### §5.2 Routine cross-references

- **Routine 1 (daily terminology-regression sentinel)** — patterns reference this index for remediation hints. Each retired-vocabulary pattern (FGC; AIT; Reparations Bond; ARP; CSG; Spatial Cost Severance; Eight-tier; Dynastic Labor Cost; etc.) corresponds to an entry in §1 above.
- **Routine 2 (weekly pre-submission readiness audit)** — references this index for retirement-vocabulary status.

### §5.3 Vocabulary strategy + terms_index

- **Vocabulary strategy v1.0.1 §6 + §7 + §13** — light retirement traces in body; cross-reference this index.
- **terms_index v1.0.0+** — summary-level retirement traces; full traces here.

### §5.4 Original ratification rigor passes

Each retirement event's full audit trail is in the ratifying rigor pass (cited in the table rows above). Those rigor passes are the canonical decision-record; this index is the cross-reference catalog.

---

## §6. Maintenance discipline

**When a new retirement is ratified:**
1. Add row to appropriate section above (vocabulary; methodology; file/artifact).
2. Cite the ratifying rigor pass + Insight # (if applicable).
3. Apply Routine 1 retired-vocabulary pattern if vocabulary retirement.
4. Light retirement trace in active scaffolding docs (working principles; vocabulary strategy; terms_index v1.0.0+) cross-references this index.
5. Full retirement trace in the ratifying rigor pass (preserved as historical record).

**When considering reversibility (revisiting a retired decision):**
1. Check this index for the retirement date + Insight #.
2. Pull up the ratifying rigor pass (full audit trail preserved).
3. Per Working Principle #1 + #4: effort-to-repair is not the rigor argument; reversibility is preserved by the rigor pass record, not by inline scaffolding traces.

---

## §7. Index versioning

| Version | Date | Changes |
|---|---|---|
| v1.0 | 2026-04-30 | Initial creation per Insight #59 (Working Principle #4 refinement); populated with 16 vocabulary retirements + 2 methodology retirements + 3 file retirements. |
| v1.1 | 2026-04-30 | §0 archive structure convention added per Insight #62 verdict (c) — hybrid (top-level cross-domain + per-domain predecessors) ratified as canonical pattern. |

---

**End of Retirement Archive Index v1.1.**
