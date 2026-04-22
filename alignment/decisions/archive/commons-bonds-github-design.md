# Commons Bonds GitHub Repository Structure & Migration Plan

## Repository Structure

```
commons-bonds/
├── README.md                              # Project overview, quick start
├── CHANGELOG.md                           # Decision log, major changes  
├── .github/
│   ├── ISSUE_TEMPLATE/
│   │   ├── alignment-issue.md             # Template for alignment tracking
│   │   └── refinement.md                  # Template for architectural refinements
│   └── workflows/                         # GitHub Actions for automation
│
├── core/                                  # Canonical framework documents
│   ├── decomposition/
│   │   ├── eight-tier-v10.html           # Current canonical version (HTML for RCV formulas)
│   │   ├── eight-tier-v09.html           # Previous version (archived)
│   │   └── archive/                       # Historical versions
│   ├── glossary/
│   │   └── terms-v2.html                  # Current vocabulary (HTML for math definitions)
│   └── technical-appendix/
│       └── mathematical-framework.html    # A.1-A.9 definitions, proofs (HTML for heavy math)
│
├── manuscript/                            # Book/essay content
│   ├── chapters/
│   │   ├── 01-introduction.md
│   │   ├── 02-cost-severance.md
│   │   ├── 06-three-ways-counting.html   # HTML for mathematical comparisons & formulas
│   │   ├── 10-policy-implications.md
│   │   └── README.md                      # Chapter status tracking
│   ├── essay/                             # 5-8k word essay version (Noema target)
│   │   └── commons-bonds-essay.md         # Markdown unless math needed
│   └── book/                              # Full book outline and structure
│       └── outline.md
│
├── workstreams/                           # WS02-WS17 tracking and content
│   ├── WS02-glossary/
│   │   ├── status.md                      # Current progress
│   │   ├── issues.md                      # Open alignment issues
│   │   └── deliverables/                  # Completed work
│   ├── WS03-tier-definitions/
│   ├── WS08-technical-appendix/
│   ├── WS10-project-separation/
│   ├── WS11-living-people/
│   ├── WS12-visualization/
│   ├── WS13-theory-change/
│   ├── WS14-counterarguments/
│   ├── WS15-origin-story/
│   ├── WS16-international/
│   ├── WS17-honest-concessions/
│   └── README.md                          # Workstream overview & status
│
├── alignment/                             # Project coordination (replaces companion)
│   ├── issues/                            # Alignment issue tracking
│   │   ├── 001-mechanism-shield-split.md # Issue #1: Refinement 1 
│   │   ├── 002-scale-dependent-salience.md # Issue #2: Refinement 2
│   │   └── 009-architectural-refinements.md # Issue #9 from handoff
│   ├── decisions/                         # Decision log
│   │   ├── decision-A-ratification.md     # April 19 Decision A
│   │   └── decision-log.md                # Running decision history
│   ├── sessions/                          # Session handoffs & notes
│   │   ├── 2026-04-19-handoff.md         # Converted from HTML
│   │   └── template.md                    # Template for future handoffs
│   └── scorecard.md                       # Current alignment status
│
├── research/                              # Supporting materials
│   ├── case-studies/
│   │   ├── appalachian-coal.md
│   │   ├── deepwater-horizon.md
│   │   └── libby-vermiculite.md
│   ├── methodology/
│   │   ├── abundance-test.md
│   │   ├── rigor-testing/                 # Ten-critic validation materials
│   │   └── falsifiability-defense.md
│   └── literature/
│       └── related-work.md                # Academic references
│
├── publishing/                            # Publication strategy & targets  
│   ├── strategy.md                        # Overall publication plan
│   ├── targets/
│   │   ├── noema-submission.md            # Noema-specific adaptation
│   │   ├── boston-review.md
│   │   └── academic-journals.md
│   └── success-criteria.md                # Measurable success metrics
│
├── tools/                                 # Automation and utilities
│   ├── version-bump.sh                    # Increment version numbers
│   ├── cross-ref-check.py                # Check internal references  
│   └── word-count.py                      # Track manuscript length
│
└── archive/                               # Deprecated content
    ├── google-drive-export/               # Initial migration content
    ├── superseded-versions/               # Old framework versions
    └── exploration/                       # Research dead-ends
```

## Key Design Principles

### 1. **Version Control Strategy**
- **Semantic versioning**: v10.0.0, v10.1.0, v10.1.1
- **Branch strategy**: 
  - `main`: Always deployable/publishable content
  - `develop`: Integration branch for ongoing work  
  - `ws##-feature-name`: Feature branches for each workstream
  - `refinement/#`: Branches for architectural refinements

### 2. **File Naming Convention**  
- **Markdown over HTML**: Better diff tracking, GitHub native rendering
- **Semantic names**: `eight-tier-decomposition-v10.md` not `commons-bonds-eight-tier-decomposition 10.html`
- **No spaces**: Use hyphens for readability
- **Consistent prefixes**: WS##, chapter-##, etc.

### 3. **Issue Tracking Replaces Alignment Companion**
- **GitHub Issues**: Each alignment issue becomes a GitHub Issue
- **Labels**: `alignment`, `architectural-refinement`, `decision-needed`, `ws##`
- **Milestones**: Map to your Decision A, B, C, D structure
- **Project Boards**: Kanban view of work in progress

### 4. **Cross-Reference Management**
- **Relative links**: `[RCV definition](../core/glossary/terms-v2.md#rcv)`
- **Automated checking**: Tools to verify internal links
- **Reference tracking**: Know what breaks when you change something

### 5. **Collaboration Ready**
- **Pull Request workflow**: Review before merging to main
- **Issue discussion**: Threaded conversations on alignment problems  
- **Branching**: Parallel work on different workstreams
- **Blame tracking**: See who changed what and why

## Migration Benefits Over Google Drive

### **Eliminated Problems:**
1. **File size limits**: No more 20KB upload failures
2. **Version confusion**: Clear git history replaces manual numbering
3. **Link rot**: Relative paths that move with files
4. **Collaboration friction**: Proper merge conflict resolution
5. **Backup anxiety**: Git is distributed; every clone is a backup
6. **Search limitations**: Full-text search across entire repository
7. **Change tracking**: See exactly what changed between any two versions

### **New Capabilities:**
1. **Branching**: Work on multiple refinements simultaneously
2. **Pull requests**: Review changes before they become canonical  
3. **Issue linking**: Connect discussions to specific problems
4. **Automated checks**: Scripts to validate references, word counts
5. **GitHub Pages**: Publish HTML versions directly from markdown
6. **Integration**: Connect to other tools (CI/CD, publishing workflows)

## Migration Strategy

### **Phase 1: Foundation** (Session 1)
1. Create repository structure
2. Convert current v9 decomposition to markdown
3. Migrate alignment companion to GitHub Issues
4. Convert handoff memo to markdown template
5. Set up basic README and CHANGELOG

### **Phase 2: Content Migration** (Session 2)  
1. Convert all WS## files from HTML to markdown
2. Migrate Google Docs (Chapter 6, Technical Appendix) to markdown
3. Set up automated cross-reference checking
4. Create branching strategy for ongoing work

### **Phase 3: Workflow Integration** (Session 3)
1. GitHub Issues for alignment tracking
2. Project boards for workstream visibility  
3. Automated builds for HTML output (if needed)
4. Integration with your session handoff workflow

### **Phase 4: Advanced Features** (Later)
1. GitHub Pages for public HTML versions
2. Continuous integration for validation
3. Automated publishing pipelines
4. Collaboration workflows for peer review

Would you like me to start with Phase 1 and create the initial repository structure with your current content migrated to markdown? I can also set up the GitHub Issues system to replace your alignment companion tracking.
