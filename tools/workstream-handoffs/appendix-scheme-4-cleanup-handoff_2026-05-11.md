# Tech Appendix Scheme-4 Cleanup — Workstream Handoff (2026-05-11)

**Date drafted:** 2026-05-11
**Branch to create at session start:** `claude/appendix-scheme-4-cleanup-<harness-id>` (branch from current `origin/main` after `git fetch`)
**Status going in:** Not blocked. Surfaced in Phase 1 inventory of the appendix-numbering-reconciliation workstream (commits `7002003` / `b903f0f` / `8f5c416` / `4b53320` / `50ec90b`, landed 2026-05-11). Documented as deferred there + in Commit B message.

---

## The substantive issue

The Tech Appendix at `core/technical-appendix/TechnicalAppendix_v2.0.0.html` runs a **fourth numbering scheme** at the h4 and h5 level *inside* §6.6 (Worked Examples — Seven Walkthroughs) and inside §11.5–§11.11 (Empirical Validation Cases — deep calibrations). The scheme **locally restarts the §-symbol at the start of each h3 block**, so:

- Inside §11.5 (Norway petroleum calibration): h4 reads `§1. Norway calibration`; h5s read `§1.1 Empirical anchors`, `§1.2 Method 1`, `§1.3 Method 2`, etc.
- Inside §11.6 (Appalachian coal calibration): h4 reads `§2. Appalachian coal calibration`
- Inside §11.7 (CSD-RCV correlation): h4 reads `§3. CSD-RCV correlation hypothesis test`
- Inside §11.8 (Method 3 sensitivity analysis): h4 reads `§3. Sensitivity findings` — **collides with §11.7's §3**; the local-restart pattern means §3 means different things in different blocks
- Inside §11.9 (DAC three-horizon range): h4 reads `§1. Direct-air-capture (DAC) cost per ton CO₂`
- Inside §11.10 (Space-economics anchors): h4 reads `§2. Space-economics numerical anchors`
- Inside §6.6 (Worked Examples — Seven Walkthroughs): h4 sequence `§0. The Four Gates as a system`, `§1. McDowell County coal: Black Lung healthcare cost`, `§2. The commute trade`, `§3. Norwegian oil extraction`, `§4. 2008 financial crisis`, `§5. The asteroid miner`, `§6. Healthcare end-of-life (Butler pacemaker)`, `§7. Opioid Appalachia`, `§8. Cross-cutting findings`

The §-symbol falsely suggests top-level section reference (now §1–§18 in the canonical scheme); the local-restart pattern makes body references ambiguous about which §3 (or §1, or §2) they target.

---

## Cascade effects on body cross-references

Body refs like these become ambiguous or stale under the canonical scheme:

- **Line 4086** (current; verify via grep before editing): `Method 3 prices the scarcity-adjusted option value per supplement §3.3 + sensitivity analysis §3.2 (calibrated parameters for Norway).` — the `§3.3` and `§3.2` refer to the locally-restarted h5 inside §11.8 (Method 3 sensitivity)
- **Line 5003**: `Method 3 estimates for the framework's three named calibration anchors per supplement §3.3 worked-example` — same §3.3 reference
- **Line 5201**: `§1. Direct-air-capture (DAC) cost per ton CO₂ — Tech Appendix supplement §3.1 anchor` — the `§1` is the h4 inside §11.9; the `supplement §3.1` may target a stale pre-merger pointer
- **Line 5204**: `The supplement §3.1 (Method 1 Replacement Cost)` — same
- **Line 5496**: `§1.3 Recommended Method 1 anchor specification (for Tech Appendix supplement §3.1 + Ch 6 main-text integration)` — `§1.3` is h5 inside §11.9
- **Line 776**: `per Block 4 validation §1.3 numerical execution` — `§1.3` inside §11.5 (Norway)
- Several more — full catalog needed in Phase 1.

All line numbers above are point-in-time as of 2026-05-11 commit `50ec90b`; verify via grep before editing per `feedback_verify_stale_memory_claims.md`.

---

## Workstream scope

### Phase 1 — Audit (read-only)

Catalog every h4 / h5 header inside §6.6 and §11.5–§11.11 that uses local-restart §-notation. For each:
- Current label (e.g., `§3.2 Worked-example application`)
- Parent h3 (which §11.X or §6.6 sub-block)
- Content topic

Plus: catalog every body cross-reference to those headers (search for `supplement §X.Y` patterns + numbered `§X.Y` refs that resolve to local-restarted h4/h5 rather than top-level §X.Y).

Save to `tools/workstream-handoffs/appendix-scheme-4-audit-inventory_<date>.md`.

### Phase 2 — Decision (with author ratification)

Pick cleanup approach. Three options:

- **Option A — Strip §-prefix; headers become named-only.** `§1. Norway calibration` → `Norway calibration`; `§1.1 Empirical anchors` → `Empirical anchors (Norway petroleum extraction, 1971–present)`. Cleanest; eliminates ambiguity. Body refs rewritten descriptively.
- **Option B — Renumber to hierarchical (§X.Y.Z form).** `§1.1 Empirical anchors` → `§11.5.1 Empirical anchors`. Preserves enumeration but pushes notation to 4-deep numbering everywhere.
- **Option C — Letter prefix (Case A / Case B...).** `§0. The Four Gates as a system` → `Case A. The Four Gates as a system`. Distinct from §-notation but reintroduces letter scheme the canonical decision rejected.

**Recommended: Option A** for both §6.6 walkthroughs and §11.X sub-headers. Optionally use descriptive enumeration prefix for §6.6 walkthroughs ("Walkthrough 1. McDowell County coal..." — keeps the count-discipline without the false §-reference).

Plus: decide how to rewrite body refs (`supplement §3.3` → descriptive form like `the cross-case dominance pattern in §11.8` or similar).

### Phase 3 — Apply (after author ratification)

Rename headers + rewrite body refs to the canonical scheme. Maintain backward-compatibility on HTML anchors only if any external citation has been published referencing the locally-restarted §X.Y labels (verify; almost certainly none).

### Phase 4 — Validate

Re-grep for residual ambiguous §X.Y references that could still resolve to local-restart h4/h5 labels. Confirm cleanup is complete.

---

## Methodology / hard constraints

- **Two-layer content origination (WP#10)** — Tech Appendix is internal-scaffolding; cleanup is internal hygiene. No external-publisher-facing impact unless chapter cross-references touch local-restart h4/h5 labels (Phase 1 audit will confirm).
- **Verify-stale-memory-claims** — line numbers above are point-in-time; re-grep before editing.
- Do NOT touch theorem statements or proofs (no theorems in these blocks; constraint is a precaution).
- Do NOT reintroduce a parallel scheme. Cleanup is canonical-numeric only.
- Do NOT change content of h4 or h5 sections; only labels + body refs.

---

## Open questions for author ratification

1. **Option A / B / C for §11 sub-blocks** — recommend A (strip §-prefix). Author judgment.
2. **§6.6 walkthroughs handling** — recommend "Walkthrough N. <Case Name>" prefix (descriptive enumeration without §-symbol). Or pure named ("McDowell County coal: Black Lung healthcare cost"). Author judgment.
3. **Body ref rewrite style** — recommend descriptive form ("cross-case dominance pattern in §11.8") over preserving local-restart labels with disambiguation footnotes. Author judgment.

---

## Coordination

- **Distinct from but related to:**
  - **Tech Appendix numbering reconciliation (#X, complete 2026-05-11)** — this is the remaining cleanup from that workstream's deferred Scheme 4. Same file; different scope (h4/h5 + body refs, not h2/h3).
  - **Publishing pipeline (queued)** — this cleanup should land BEFORE the Tech Appendix PDF render is produced, so the published PDF doesn't carry confusing local-restart §-notation.
  - **Glossary v4 audit (queued in #7)** — likely no overlap; glossary doesn't reference h4/h5 labels.

- **No content dependencies.** Can run any time. Recommend running BEFORE publishing pipeline to avoid PDF rendering with confusing notation.

---

## Estimated effort

**Small to medium.** ~1–2 hours.

Breakdown:
- Phase 1 audit: ~30 min (grep-driven; targeted scope)
- Phase 2 decision (author ratification gate): ~10 min
- Phase 3 apply: ~30–60 min (mechanical renames + body-ref rewrites, ~30–50 edits)
- Phase 4 validate: ~15 min (re-grep + spot-check)

---

## Hard constraints — what NOT to do

- Do NOT introduce a third or fourth numbering scheme (canonical-numeric-only).
- Do NOT modify h4/h5 content; only labels.
- Do NOT touch theorem statements (precaution; no theorems in these blocks).
- Do NOT edit body refs without author ratification of the rewrite style.

---

## Branch discipline

Fresh feature branch `claude/appendix-scheme-4-cleanup-<harness-id>` from current `origin/main` after `git fetch`. Per WP#9: merge per ratified chunk via `git push origin HEAD:main`.

---

## Reference files

- `core/technical-appendix/TechnicalAppendix_v2.0.0.html` — target file
- `tools/workstream-handoffs/appendix-numbering-audit-inventory_2026-05-11.md` — parent inventory (Scheme 4 documented as deferred there)
- `tools/workstream-handoffs/appendix-numbering-reconciliation-handoff_2026-05-11.md` — parent workstream handoff
- Commits to reference: `b903f0f` (Phase 3A applied), `8f5c416` (Phase 3B Commit B with deferred-flag annotation)

---

*End of workstream handoff. No blocker. Recommend running before publishing pipeline so the rendered PDF doesn't carry confusing local-restart §-notation. ~1–2 hour focused session.*
