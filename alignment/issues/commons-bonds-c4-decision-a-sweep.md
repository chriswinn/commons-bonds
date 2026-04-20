# Commons Bonds — C4 Content Patch
## Decision A Ratification Ripple Sweep
### WS01–17 Update

**Status:** Canonical patch — apply to all 17 workstream files  
**Produced:** 2026-04-20 · v1.13.0 session  
**Event:** Decision A ratified 2026-04-19  

---

## What Decision A Establishes

**Decision A** formally ratifies the eight-tier RCV decomposition with v10 canonical naming as the authoritative taxonomy for Commons Bonds. This resolves prior ambiguity between legacy tier names (Immediate Survival, Lifetime Health, Community Stability, Environmental Remediation, etc.) and the v10 names. All prior naming conventions are retired. All documents, diagrams, and analysis using legacy names are superseded.

**Canonical eight tiers (v10, ratified 2026-04-19):**

| Tier | Canonical Name | Notes |
|---|---|---|
| 1 | Lifetime Survival | |
| 2a | Actuarial Risk Cost | Renamed from "Individual Risk Cost" (C1 complete) |
| 2b | Mission Failure Reserve | Sub-tier of 2a; catastrophic tail |
| 3 | Dynastic Labor | |
| 4 | Foreclosure | |
| 5 | Community Transition Reserve | |
| 6 | Ecological Carrying | |
| 7 | Knowledge and Culture | |
| 8 | Political Capture | |

---

## Standard Ratification Note — Insert in Every WS File

Place this block at the top of each WS file's **Status / Canonical Reference** section (or immediately after the file's header block if no such section exists). Use the exact Markdown below:

```markdown
> **Decision A — Ratified 2026-04-19**  
> The eight-tier RCV decomposition with v10 canonical naming is formally ratified as the
> authoritative taxonomy for Commons Bonds. All legacy tier names (Immediate Survival,
> Lifetime Health, Community Stability, Environmental Remediation, etc.) are retired.
> Tier 2a is "Actuarial Risk Cost" (renamed from "Individual Risk Cost," C1 complete).
> This workstream file reflects v10 canonical naming.
```

---

## Per-File Application Instructions

For each file below, confirm that:
1. The ratification note block is present (or add it).
2. The file body uses v10 canonical tier names exclusively.
3. Any legacy name found in the body is flagged and corrected.

### WS01 — `01_master_workstream.md`
- **Insert note:** Top of file after header.
- **Scan for:** Immediate Survival, Lifetime Health, Community Stability, Environmental Remediation, Individual Risk Cost.
- **Likely clean:** WS01 is the master tracker. Confirm tier table uses v10 names.

### WS02 — `02_glossary_reconciliation.md`
- **Insert note:** Top of file after header.
- **Body update:** Apply C1 rename (tier-2a-rename-changes.md) AND C2 scale-abstract patch before marking clean.
- **Note:** C2 patch adds scale-abstract core + manifestations to six tiers. Reconcile these as part of C2 application, not separately.

### WS03 — `03_chapter_6_integration.md`
- **Insert note:** Top of file after header.
- **Body update:** Apply C1 rename (tier-2a-rename-changes.md) AND C2 patch framing.
- **Note:** Same C2 dependency as WS02.

### WS04 — `04_chapter_alignment.md`
- **Insert note:** Top of file after header.
- **Scan for:** Legacy tier names in chapter-alignment references.

### WS05 — `05_evidence_integration.md`
- **Insert note:** Top of file after header.
- **Scan for:** Legacy tier names in evidence citations or tier-mapping tables.

### WS06 — `06_counterargument_framework.md`
- **Insert note:** Top of file after header.
- **Scan for:** Legacy tier names in counterargument framings.

### WS07 — `07_writing_style_voice.md`
- **Insert note:** Top of file after header.
- **Scan for:** Legacy tier names in example prose passages or style illustrations.

### WS08 — `08_technical_appendix.html`
- **Note:** This is an HTML file (math-keep). Ratification note format differs.
- **Insert:** Add the following HTML comment block immediately after the `<body>` tag:
  ```html
  <!-- Decision A ratified 2026-04-19: eight-tier v10 canonical naming authoritative.
       Tech Appendix is v0.0.2 — reflects v10 names throughout (C1 rename applied). -->
  ```
- **Body:** Tech Appendix v0.0.2 already reflects v10 names. Verify only the comment is needed; no body edits required.

### WS09 — `09_visualization_framework.md`
- **Insert note:** Top of file after header.
- **Scan for:** Legacy tier names in visualization specs or diagram labels.

### WS10 — `10_theory_of_change.md`
- **Insert note:** Top of file after header.
- **Scan for:** Legacy tier names in theory-of-change tier references.

### WS11 — `11_living_people_integration.md`
- **Insert note:** Top of file after header.
- **Scan for:** Legacy tier names in case study mappings.

### WS12 — `12_visualization_development.md`
- **Insert note:** Top of file after header.
- **Scan for:** Legacy tier names in chart labels, figure captions, or visualization specs.

### WS13 — `13_theory_of_change.md`
- **Insert note:** Top of file after header.
- **Scan for:** Legacy tier names.

### WS14 — `14_counterargument_integration.md`
- **Insert note:** Top of file after header.
- **Scan for:** Legacy tier names in counterargument text.

### WS15 — `15_origin_story_development.md`
- **Insert note:** Top of file after header.
- **Scan for:** Legacy tier names in origin narrative passages.

### WS16 — `16_international_dimension.md`
- **Insert note:** Top of file after header.
- **Scan for:** Legacy tier names in international case mappings.

### WS17 — `17_honest_concession_section.md`
- **Insert note:** Top of file after header.
- **Scan for:** Legacy tier names in concession framing.

---

## Legacy Name Reference Table

If any of the following appear in a WS file body, replace with the v10 canonical name:

| Legacy name (retire) | v10 canonical name |
|---|---|
| Immediate Survival | Lifetime Survival (Tier 1) |
| Lifetime Health | Actuarial Risk Cost (Tier 2a) |
| Individual Risk Cost | Actuarial Risk Cost (Tier 2a) |
| *(no prior name for 2b)* | Mission Failure Reserve (Tier 2b) |
| Community Stability | Dynastic Labor (Tier 3) OR Community Transition Reserve (Tier 5) — context determines which |
| Intergenerational Foreclosure | Foreclosure (Tier 4) |
| Environmental Remediation | Ecological Carrying (Tier 6) |
| Community and Social | Community Transition Reserve (Tier 5) |
| Political Capture | Political Capture (Tier 8) — name unchanged |
| Ecological Carrying | Ecological Carrying (Tier 6) — name unchanged |
| Temporal Displacement | *(Retired — absorbed into Foreclosure Tier 4 and Ecological Carrying Tier 6)* |
| Knowledge and Culture | Knowledge and Culture (Tier 7) — name unchanged |

---

## Completion Criteria

C4 is complete when:
- [ ] Decision A ratification note block is present in WS01–07, WS09–17
- [ ] HTML comment is present in WS08 (`08_technical_appendix.html`)  
- [ ] No legacy tier names remain in any WS01–17 body
- [ ] WS02 and WS03 have also received C2 patch (scale-abstract verbiage)

---

*End of C4 patch. The sweep is primarily mechanical — confirm note insertion and scan for legacy names. Most WS files were produced during the v1.0.0–v1.12.0 sessions and should already use v10 names, but Decision A ratification note is new and must be added universally.*
