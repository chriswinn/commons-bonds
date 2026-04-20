# Commons Bonds Repository Structure

## Directory Layout

```
commons-bonds/
├── README.md                          # Project overview
├── core/                              # Canonical framework documents
│   ├── decomposition/                 
│   │   ├── eight-tier-v10.md         # Canonical eight-tier decomposition
│   │   └── eight-tier-v10.html       # Math-heavy version with MathJax
│   ├── glossary/
│   │   ├── terms-v2.md               # Updated vocabulary glossary
│   │   └── terms-v2.html             # Display version
│   └── definitions/
│       └── formal-definitions.md     # Core RCV and CS definitions
├── manuscript/                        # Book and essay content
│   ├── chapters/
│   │   ├── chapter-01-the-plane.md
│   │   ├── chapter-02-mcDowell.md
│   │   ├── chapter-06-three-ways.md  
│   │   └── chapter-10-villain.md
│   ├── essays/
│   │   ├── noema-target-essay.md     # 5,000-8,000 word submission
│   │   └── boston-review-pitch.md
│   └── book/
│       ├── outline-ten-chapters.md
│       └── structure-notes.md
├── workstreams/                       # Active workstream tracking
│   ├── WS02-glossary-reconciliation.md
│   ├── WS03-chapter6-integration.md
│   ├── WS08-technical-appendix.md
│   ├── WS09-villain-analysis.md
│   └── [...WS10-WS17...]
├── alignment/                         # Decision tracking and alignment
│   ├── decisions/
│   │   ├── decision-A-ratified.md    # April 19 ratification
│   │   ├── decision-B-pending.md     # Option C architectural surfacing
│   │   ├── decision-C-pending.md     # Chapter 10 villain landing
│   │   └── decision-D-pending.md     # Two-book split
│   ├── sessions/
│   │   ├── session-handoff-2026-04-19.md
│   │   └── session-handoff-2026-04-20.md
│   └── issues/                       # GitHub Issues (replaces alignment companion)
├── research/                         # Case studies and methodology
│   ├── case-studies/
│   │   ├── appalachian-coal.md
│   │   ├── deepwater-horizon.md
│   │   ├── libby-vermiculite.md
│   │   └── norway-swf.md
│   ├── methodology/
│   │   ├── abundance-test.md
│   │   ├── universality-validation.md
│   │   └── rigor-testing-framework.md
│   └── validation/
│       ├── steelman-tests.md
│       └── counterargument-analysis.md
├── publishing/                       # Publication pipeline
│   ├── targets/
│   │   ├── noema-submission.md
│   │   ├── boston-review-plan.md
│   │   └── academic-journals.md
│   ├── submissions/
│   │   └── tracking.md
│   └── platform/
│       ├── substack-parallel.md
│       └── social-strategy.md
├── tools/                            # Automation and utilities
│   ├── migration/
│   │   ├── google-drive-export.md
│   │   └── html-to-markdown.py
│   ├── validation/
│   │   └── link-checker.py
│   └── deployment/
│       └── github-pages.md
└── archive/                          # Deprecated content
    ├── deprecated/
    │   ├── alignment-companion-v1.html
    │   └── decomposition-v9.html
    └── sessions/
        └── pre-migration-transcripts/
```

## File Naming Conventions

### Version Control
- **Major framework files:** `v10`, `v11` (e.g., `eight-tier-v10.md`)
- **Working documents:** `_v2`, `_v3` suffix (e.g., `alignment-companion_v2.md`)
- **Session handoffs:** Date format `YYYY-MM-DD` (e.g., `session-handoff-2026-04-19.md`)

### Content Types
- **`.md`** - Default for all text content, workstream tracking, session handoffs
- **`.html`** - Math-heavy content requiring MathJax (decomposition, technical appendix, Chapter 6)
- **`.py`** - Automation scripts and utilities

## Migration Strategy

### Phase 1: Foundation ✅
- Repository structure created
- Critical files converted (session handoff, decomposition v10)
- File format strategy implemented

### Phase 2: Content Migration 🎯
- Convert remaining HTML files to markdown where appropriate
- Preserve mathematical content in HTML format with MathJax
- Migrate workstream tracking from Google Drive

### Phase 3: Workflow Integration ⏳
- Replace alignment companion with GitHub Issues
- Set up GitHub Issues templates for:
  - Architectural refinements
  - Decision tracking
  - Workstream updates
  - Rigor test results

## GitHub Issues Integration

### Issue Labels
- `alignment` - Alignment companion replacement
- `architectural-refinement` - Framework structure changes  
- `decision-needed` - Requires formal decision (A, B, C, D structure)
- `ws02`, `ws03`, etc. - Workstream-specific issues
- `rigor-test` - Testing and validation
- `publishing` - Publication pipeline issues

### Milestones
- **Decision A** - Eight-tier decomposition ratification ✅
- **Decision B** - Option C architectural surfacing
- **Decision C** - Chapter 10 villain landing
- **Decision D** - Two-book split decision

## Best Practices

### Content Organization
- Keep canonical documents in `/core/`
- Working drafts in appropriate workstream folders
- Archive superseded versions in `/archive/deprecated/`

### Commit Messages
- Use conventional commit format: `feat:`, `fix:`, `docs:`, `refactor:`
- Reference workstream: `feat(WS02): add scale-abstract pattern`
- Reference decisions: `docs(Decision-A): ratify eight-tier decomposition`

### Branch Strategy
- `main` - Canonical framework content
- `ws02-glossary` - Workstream branches for major updates
- `publishing-noema` - Publication-specific branches

## Integration with Google Drive

During transition period:
- Google Drive remains source of truth for active writing
- GitHub stores canonical, version-controlled content
- Session handoffs bridge both systems
- Regular sync ensures consistency

Post-migration:
- GitHub becomes primary version control
- Google Drive used for collaborative drafting only
- Automated sync where possible
