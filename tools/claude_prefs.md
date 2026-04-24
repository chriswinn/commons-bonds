## File delivery and collaboration
- **Preferred: direct work in the local git worktree.** Claude writes, edits,
  commits, merges, and pushes to the GitHub remote (origin). Everything is
  recoverable via git. Validated 2026-04-22 (session v1.28.0: worktree-write,
  merge to main, and push to origin/main all succeeded end-to-end with no
  truncation).
- **Branch discipline:** Claude works on its assigned worktree branch
  (e.g., claude/epic-bose-9f88b3). Merges to main and pushes to origin happen
  only on explicit request — authorization doesn't carry across requests, and
  pushing to main is a visible-to-others action that needs a fresh go-ahead.
- **Never force-push to main.** Warn if requested; don't do it without explicit
  acknowledgment of the destructive implication.
- **Deprecated but still functional: mobile file uploads.** Clunky for larger
  workflows; still fine for reviewing one or two files at a time. Prefer
  GitHub-based collaboration going forward for anything multi-file.
- **Never write to Google Drive.** Heredoc truncation risk is Drive-specific
  and still real. Drive uploads remain manual-only on my side.
- **Never skip hooks** (--no-verify) or bypass signing on commits.

## File format rules
- .html for: mathematical formulas, RCV decompositions, technical appendix,
  glossary definitions, chapter drafts with equations, session handoffs.
- .md for: workstream tracking, alignment notes, policy/narrative chapters,
  README files, patches, protocol documents, methodology docs.
- Naming convention (Commons Bonds): **Version suffixes use dots, not underscores.**
  Canonical format is `_v{major}.{minor}.{patch}` (example: `_v1.2.1`), not `_v1_2_1`.
  Patterns:
    Chapters:     Chapter_#_Title_Draft.md  /  Chapter_#_Title_GuidanceDoc.md
    Patches:      c{N}_{topic}_patch.md  (in alignment/patches/)
    Methodology:  commons_bonds_{topic}_v{major}.{minor}.{patch}.md  (or .html)
                  example: commons_bonds_rigor_protocol_v2.1.0.md
    Handoffs:     commons-bonds-session-handoff-YYYY-MM-DD_v{major}.{minor}.{patch}.html
                  example: commons-bonds-session-handoff-2026-04-22_v1.29.0.html
    Rigor pass:   commons_bonds_rigor_pass_YYYY-MM-DD_v{major}.{minor}.{patch}.md
                  (in tools/rigor-passes/)
    Triage:       commons_bonds_{topic}_triage_v{major}.{minor}.{patch}.md
                  (in tools/triage/)
  Versioned files: add `_v{major}.{minor}.{patch}` suffix; increment rightmost digit
  per minor update (patch). Middle digit for material additions. Leading digit for
  fundamental revisions.
  Historical note: files created pre-2026-04-22 (session v1.29.0) use underscored
  version suffixes (e.g., `_v1_2_1.md`). New files use dot-separated. A mass rename
  sweep to normalize existing files is queued as an optional future task; in the
  meantime, reference existing files by their current on-disk names.

## Session handoff rule
- When a session grows heavy, produce a handoff file before context runs out —
  don't wait to be asked. Handoff must include: session summary, top priority
  for next session with workflow steps, all open decisions and watch items,
  file inventory, and explicit resume instructions addressed to the next
  Claude instance.

## Commons Bonds operating core
**AIT positioning:** The Abundance Interference Taxonomy is the framework's
epistemic core. Dimensions are organizational scaffolding, not load-bearing
structure. Dimension additions, mergers, or renames are organizational
revisions, not framework-integrity events.

**Two-path rigor test (apply before ratifying any architectural claim):**
Path 1 — Allocation symmetry: is the structural value-capture/cost-bearing
asymmetry present?
Path 2 — Shield absence: is the distance condition (the shielding mechanism)
absent?
Both paths must be confirmed. Structural allocation is the mechanism of cost
severance; distance is the shielding condition.

**Merger gate (apply before ratifying any new or renamed dimension):**
Demonstrate bilateral independence with cases in both directions — a case
where Dimension A costs occur without Dimension B costs, and vice versa. If
independence fails in either direction, merger is indicated.

**Primitiveness gate (apply before ratifying any new dimension):**
The dimension's revealed costs must not decompose cleanly into compositions
of existing dimensions. If they do, the candidate is a cross-dimension
concept, not a new dimension.

**Operating discipline:** "Push harder so we only rewrite once." Apply to
dimension set, protocol, AIT positioning, and chapter framing — not just
wording.

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

## Guiding constraints (publication path + success criteria)
**Canonical capture:** commons_bonds_guiding_constraints_v1_0_0.md. Upload
at session start for scope, architectural, or stakeholder-facing decisions.
Carries the operational form of success criteria and publishing-path
constraints for rigor-pass application.

**Success criteria anchor:** 13+-year labor-lawyer sentence (scope v1.0.3
§7.1). Goal 1 — future generations compensated more fairly (framework-level,
upstream, routed through vocabulary adoption). Goal 2 — people accept work
with open eyes and honest accounting (direct, reader-by-reader). "When in
doubt, trim."

**Publishing path is integral to success, not orthogonal** (scope v1.0.3
§8). Cascade: Noema → Boston Review → The Atlantic Ideas → further;
Berggruen Prize (Aug 17 2026) is parallel independent track. Specific agent
and publisher detail lives in the Publishing Strategy document (Apr 18 2026).

**Rigor-pass implication:** Group D (Tests 14–19) and Group E (Tests 20–23)
in rigor protocol v1.2.1 operationalize these constraints. Absence of
upload ≠ absence of constraint — if the standing doc is not in session
context, flag the drift rather than proceeding on implicit values.
