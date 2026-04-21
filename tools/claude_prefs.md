## File delivery rules
- Never write to Google Drive. Never use heredoc syntax. Always use the
  create_file tool and present_files so I can download and upload manually.
- I handle all Google Drive uploads and all GitHub add/commit/push manually.

## File format rules
- .html for: mathematical formulas, RCV decompositions, technical appendix,
  glossary definitions, chapter drafts with equations, session handoffs.
- .md for: workstream tracking, alignment notes, policy/narrative chapters,
  README files, patches, protocol documents, methodology docs.
- Naming convention (Commons Bonds):
    Chapters:     Chapter_#_Title_Draft.md / Chapter_#_Title_GuidanceDoc.md
    Patches:      c{N}_{topic}_patch.md
    Methodology:  commons_bonds_{topic}_{v#.#.#}.md or .html
    Handoffs:     commons-bonds-session-handoff-YYYY-MM-DD_{v#.#.#}.html
    Versioned files: add _{v#.#.#} suffix, increment rightmost digit per update.

## Session handoff rule
- When a session grows heavy, produce a handoff file before context runs out —
  don't wait to be asked. Handoff must include: session summary, top priority
  for next session with workflow steps, all open decisions and watch items,
  file inventory, and explicit resume instructions addressed to the next
  Claude instance.

## Commons Bonds operating core
**AIT positioning:** The Abundance Interference Taxonomy is the framework's
epistemic core. Layers are organizational scaffolding, not load-bearing
structure. Layer additions, mergers, or renames are organizational revisions,
not framework-integrity events.

**Two-path rigor test (apply before ratifying any architectural claim):**
Path 1 — Allocation symmetry: is the structural value-capture/cost-bearing
asymmetry present?
Path 2 — Shield absence: is the distance condition (the shielding mechanism)
absent?
Both paths must be confirmed. Structural allocation is the mechanism of cost
severance; distance is the shielding condition.

**Merger gate (apply before ratifying any new or renamed layer):**
Demonstrate bilateral independence with cases in both directions — a case
where Layer A costs occur without Layer B costs, and vice versa. If
independence fails in either direction, merger is indicated.

**Primitiveness gate (apply before ratifying any new layer):**
The layer's revealed costs must not decompose cleanly into compositions of
existing layers. If they do, the candidate is a cross-layer concept, not a
new layer.

**Operating discipline:** "Push harder so we only rewrite once." Apply to
layer set, protocol, AIT positioning, and chapter framing — not just wording.

## Privacy rules
- Exclude personal financial details (specific assets, income sources, dollar
  figures, budget tiers) from outputs intended for external or public use:
  GitHub repos, shared docs, templates, public examples, anything that will
  leave my private workspace. Private context (memory, methodology files,
  internal drafts, session handoffs) is fine — the rule applies to outputs
  intended to be seen by others.
- When producing an example or template that draws on a real project of mine,
  scrub financial specifics by default; ask if in doubt.

**Hard rules:**
- Never touch /Noema/ or /Berggruen Institute - Essay/ Drive folders. Ever.
- Never rename Drive files. Migration is read-only on the Drive side.
- Math files stay .html. Never convert to .md.
