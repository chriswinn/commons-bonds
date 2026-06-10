# Apparatus Register Decision Sweep — Workstream Handoff (2026-05-10)

**Date drafted:** 2026-05-10
**Branch to create at session start:** `claude/apparatus-register-sweep-<harness-id>` (branch from current `origin/main`)
**Status going in:** Issue surfaced 2026-05-09 in the Noema essay audience-load rigor pass — "cluster-γ" jargon flagged as ⚠⚠⚠ disqualifying for trade press; "RCV" three-component breakdown flagged as ⚠⚠⚠ academic-monograph register. Same apparatus is presumed to live throughout the chapters at higher density. **No project-wide register decision has been made about which apparatus stays in trade-press body, which migrates to tech appendix, which gets dropped entirely.**

---

## Workstream scope

Decide and apply a project-wide apparatus register policy across all 10 chapters of *Commons Bonds* + the Tech Appendix + paratextual material (AuthorsNote, Glossary, etc.).

**The decision question per apparatus item:** Stays in trade-press body / migrates to tech appendix / dropped entirely.

**The apparatus inventory (known partial list):**

- *Cost severance* — the framework's load-bearing concept. Trade-press body. Plain language.
- *Residual Commons Value (RCV)* — formal apparatus / acronym. Likely tech appendix only.
- *Cluster-α / cluster-β / cluster-γ* — the framework's typology of architectures (pure cost severance / partial accountability / full accountability). Likely tech appendix only; trade body uses plain language ("alternative architecture," "honest accounting," "different architecture in practice").
- *Asymmetric Regret Rule (ARR)* — formal apparatus. Likely tech appendix only; trade body could reference the Kantian / precautionary principle in plain language.
- *Intergenerational Pricing Gap (IPG)* — formal apparatus. Same.
- *Accountability bond (B)* — central concept; arguably stays in trade body in plain language ("the amount actually posted against the cost"); the formal symbol B stays in tech appendix.
- *Six patterns by which costs get hidden* (geographic distance, temporal asymmetry, informational asymmetry, power asymmetry, normative routinization, abundance masking) — framework analytical content; trade body should name them but not as a formal enumerated list. Treat as natural-language descriptors.
- *Two-layer content origination discipline (WP#10)* — internal scaffolding only. Never appears in publisher-facing prose.
- *Working principles (WP#1–WP#10)* — internal scaffolding. Same.
- Various Greek-letter / acronym-laden apparatus from the Tech Appendix.

For each item: ratify the register decision, then apply across all chapters.

---

## Why this matters

The Noema rigor pass demonstrated the audience-load cost of apparatus: "cluster-γ" was flagged as disqualifying for trade press; agents and acquisitions editors see internal-framework labels in a sample chapter and the manuscript goes to the no pile. Mazzucato's *The Value of Everything* names *value extraction* in plain English and saves the formal apparatus for academic papers. The book's trade-press version needs the same discipline.

Without a project-wide register decision, every essay extraction (Noema, Aeon, Boston Review, Berggruen, op-eds) will face the same apparatus-cleanup problem at the polish stage. Decide once, apply everywhere, and downstream essay extraction becomes much faster.

---

## Methodology

1. **Build the full apparatus inventory.** Walk every chapter, the Tech Appendix, and paratext. List every framework-specific term, acronym, Greek letter, formal definition, working principle, etc.
2. **Categorize each item:** trade-press body / tech appendix / dropped / paratext-only.
3. **Ratify with the user.** Each decision is content-strategic. The user is the author and decides.
4. **Apply.** Edit chapters to remove or rephrase apparatus per the ratified register. Move definitions to the tech appendix where appropriate. Keep the chapter prose readable in plain language; let the appendix carry formal precision for readers who want it.
5. **Cross-reference.** Where a chapter previously used apparatus X, leave a paratextual cross-reference ("see Tech Appendix §X.Y for the formal model") for the ~10% of readers who want it.

**Coordination with Path B audit:** This handoff and the cross-chapter Path B audit (`path-b-audit-cross-chapter-handoff_2026-05-10.md`) should run together where they overlap — apparatus duplication often appears as Path B duplication, and the same paragraph edits can address both.

---

## Current state

**Known sites of apparatus density:**
- Ch 5 *The Accountability Gap* — defines the framework's accountability concepts.
- Ch 6 *Three Ways of Counting* — naming clusters α/β/γ; introduces formal counting models.
- Ch 9 *Pricing Honestly* — RCV three-component breakdown likely lives here.
- Tech Appendix — full formal apparatus.

**Inventory not yet built.** A fresh session should grep across `manuscript/chapters/` and `manuscript/` for distinctive apparatus terms (cluster-γ, RCV, ARR, IPG, etc.) to map current density.

**Existing trade-press-friendly framings already established:**
- "what's left of a resource's worth after the obvious extraction value has been captured" (Noema essay framing of RCV without the acronym)
- "a different architecture in practice" (Noema essay framing of cluster-γ without the Greek letter)
- "the amount actually posted against the residual cost" (Noema essay framing of accountability bond)

---

## Deliverables

1. **`tools/rigor-passes/commons_bonds_rigor_pass_<DATE>_apparatus_register_decision_v1.0.0.md`** — the ratified register decisions per apparatus item. Becomes a standing reference for all future essay extractions and chapter polish work.
2. **Edits applied to chapter files** in `manuscript/chapters/` and the Tech Appendix. Each apparatus migration is its own commit.
3. **Updated `Glossary.md`** if affected — the Glossary should reflect the canonical register decisions.
4. **Cross-references inserted** in chapters where apparatus was removed but trade readers benefit from knowing the formal model exists in the appendix.

---

## First actions for fresh session

1. Read this handoff end-to-end.
2. Read the Noema rigor pass at `publishing/essays/noema-commons-bonds/rigor/early-audience-load_2026-05-09.md` — specifically the "Apparatus check" findings on cluster-γ, RCV, etc., for calibration on what trade-press editors flag.
3. Read the existing `feedback_two_layer_content_discipline.md` memory entry — apparatus is internal-scaffolding by default; trade body is external-publisher-facing. The two-layer discipline already has the conceptual scaffolding for this work.
4. Build the apparatus inventory: grep across chapters for known terms; produce a comprehensive list.
5. Confirm the inventory with the user before making decisions.
6. Walk decisions per item with the user — small batches, ratify each.
7. Apply edits in priority order: highest-density chapters first (Ch 5, Ch 6, Ch 9, Tech Appendix).

---

## What NOT to do

- Do not delete apparatus from the Tech Appendix without explicit user consent — the appendix is the home for formal apparatus, not the cut.
- Do not add new apparatus during this sweep. This is migration / consolidation work.
- Do not rewrite chapter prose beyond what apparatus removal requires — prose-flow polish is a separate concern.
- Do not make register decisions unilaterally — the user is the author and decides what's trade-body vs. appendix.

---

## Reference files

- `manuscript/chapters/Chapter__5_THEACCOUNTABILITYGAP__Draft.md`
- `manuscript/chapters/Chapter__6_ThreeWaysofCounting__Draft.html`
- `manuscript/chapters/Chapter__9_PricingHonestly__Draft.md`
- Tech Appendix (location varies; check `manuscript/` and `tools/`)
- Glossary (location varies; check `manuscript/`)
- `feedback_two_layer_content_discipline.md` (memory)
- `publishing/essays/noema-commons-bonds/rigor/early-audience-load_2026-05-09.md` (Noema apparatus findings)
- `publishing/essays/noema-commons-bonds/_archive/pre-stage-2-drafts/noema-essay-fresh-draft_named_2026-05-09.md` (working examples of plain-language framings of cost severance, RCV, cluster-γ that already passed audience-load rigor)

---

*End of handoff.*
