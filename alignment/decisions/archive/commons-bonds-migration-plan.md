# Commons Bonds Migration Plan: Google Drive → GitHub

## File Format Strategy (Hybrid Approach)

**Use `.html` for:**
- Mathematical formulas and equations
- Core decomposition (RCV formulas)
- Technical appendix (formal definitions A.1-A.9)
- Glossary (mathematical term definitions)
- Chapter 6 (calculation methods)

**Use `.md` for:**
- Workstream tracking and status
- Session handoffs and notes
- Alignment issue discussions
- Policy and narrative chapters
- README files and documentation
- GitHub Issues and project management

**Benefits:**
- `.md`: Lighter weight, better GitHub integration, easier collaboration
- `.html`: Proper math rendering, maintains your current formatting
- Hybrid approach: Use the right tool for the right job

## Current State Analysis (From Google Drive)

### **Root Commons Bonds Folder**
```
CANONICAL CONTENT (migrate to /core/):
├── commons-bonds-eight-tier-decomposition 9.html → /core/decomposition/eight-tier-v09.html
├── error-out-v10.html → /core/decomposition/eight-tier-v10.html (fix upload issues)
├── commons_bonds_updated_glossary.html → /core/glossary/terms-v2.html
├── Commons Bonds - Technical Appendix v0.0.1 → /core/technical-appendix/mathematical-framework.html

MANUSCRIPT CONTENT (migrate to /manuscript/):  
├── Commons Bonds - Chapter 6 (Draft) → /manuscript/chapters/06-three-ways-counting.html
├── Commons Bonds - Chapter 6 (Three Ways of Counting) - Draft v1 → /archive/chapters/06-v1.html

SESSION TRACKING (migrate to /alignment/):
├── commons-bonds-session-handoff-2026-04-19.html → /alignment/sessions/2026-04-19-handoff.md
├── Commons Bonds — Session Archive & Decision Log → /alignment/decisions/decision-log.md

CLEANUP (archive):
├── commons-bonds-multi-scale-revision-prototype.html → /archive/prototypes/
├── commons_bonds_full_economy_simulation.html → /research/methodology/
```

### **Workstreams Subfolder** 
```
ALIGNMENT TRACKING (migrate to GitHub Issues + /alignment/):
├── 00_alignment_companion.html → GitHub Issues + /alignment/scorecard.md

WORKSTREAM CONTENT (migrate to /workstreams/):
├── 08_technical_appendix.html → /workstreams/WS08-technical-appendix/status.md
├── 10_project_separation_folder_reorg.html → /workstreams/WS10-project-separation/status.md
├── 11_living_people_integration.html → /workstreams/WS11-living-people/status.md
├── 12_visualization_development.html → /workstreams/WS12-visualization/status.md  
├── 13_theory_of_change.html → /workstreams/WS13-theory-change/status.md
├── 14_counterargument_integration.html → /workstreams/WS14-counterarguments/status.md
├── 15_origin_story_development.html → /workstreams/WS15-origin-story/status.md
├── 16_international_dimension.html → /workstreams/WS16-international/status.md
├── 17_honest_concession_section.html → /workstreams/WS17-honest-concessions/status.md
```

## Phase 1: Foundation Setup (This Session)

### **1.1 Repository Initialization**
```bash
# Create repository structure
mkdir commons-bonds && cd commons-bonds
git init
git remote add origin https://github.com/[username]/commons-bonds.git

# Create directory structure  
mkdir -p {core/{decomposition,glossary,technical-appendix},manuscript/{chapters,essay,book},workstreams,alignment/{issues,decisions,sessions},research/{case-studies,methodology,literature},publishing/{targets},tools,archive}
```

### **1.2 Critical File Conversions**

**A. Convert Handoff Memo to Markdown Template**
```markdown
# Session Handoff: [Date]

## Session Summary
- **Decision Status**: [Any decisions made]
- **Workstreams Touched**: [List WS##]  
- **Alignment Issues**: [Closed/Opened]

## Key Accomplishments
[What was done this session]

## Architectural Refinements
[Any new refinements discovered]

## Next Session Priority
1. [First priority]
2. [Second priority] 
3. [Third priority]

## Files Modified
- [List with commit hashes]

## Technical Notes
[Any GitHub/workflow issues]
```

**B. Convert Alignment Companion to GitHub Issues**

From the alignment companion HTML, create GitHub Issues for:
```
Issue #1: Mechanism vs. Shield Split (Refinement 1)
- Label: architectural-refinement, project-wide
- Milestone: WS02/WS03 Execution  
- Files affected: [list from handoff memo]

Issue #2: Universal Claim, Scale-Dependent Salience (Refinement 2) 
- Label: architectural-refinement
- Milestone: WS02/WS03 Execution

Issue #3: Scale-Abstract Verbiage Revision (Refinement 3)
- Label: tier-revision
- Milestone: WS02/WS03 Execution

Issue #9: Three Architectural Refinements Bundle
- Label: meta-issue
- References: #1, #2, #3
```

### **1.3 Convert Core Documents**

**A. Eight-Tier Decomposition v10**
```bash
# Fix the failed upload content and convert to markdown
# Add frontmatter for metadata tracking
```

**B. Glossary Conversion**
```markdown
# Commons Bonds Glossary

<!-- Last Updated: [date] -->
<!-- Version: 2.0 -->

## Core Framework Terms

### Commons Bonds {#commons-bonds}
The obligations owed to shared resources and the communities that steward them...
[Full definition with cross-links]

### Cost Severance {#cost-severance}  
The act of cutting the cost of extraction loose from the profit...
[Cross-reference to technical definition: A.4]
```

## Phase 2: Content Migration (Next Session)

### **2.1 Workstream Conversion Strategy**

Each WS## HTML file becomes:
```
/workstreams/WS##-name/
├── README.md           # Overview from HTML file
├── status.md           # Current progress
├── issues.md           # Open alignment issues  
├── deliverables/       # Completed work
└── references.md       # Cross-references
```

### **2.2 Chapter 6 Migration**
```markdown
# Chapter 6: Three Ways of Counting

<!-- 
Source: Commons Bonds - Chapter 6 (Draft).docx
Migrated: [date]
Status: Draft v2
Word Count: ~[count]
-->

## Overview
If cost severance is real — if market prices systematically understate...
[Convert from Google Doc, preserve formatting]

## Cross-References
- [RCV Definition](../../core/glossary/terms-v2.md#rcv)
- [Technical Appendix A.6](../../core/technical-appendix/mathematical-framework.md#a6)
```

### **2.3 Version History Recovery**
```bash
# Create archive structure preserving Google Drive history
/archive/google-drive-export/
├── 2026-04-19-snapshot/    # Everything as-is from Drive
├── version-history/        # Document version progressions  
└── migration-log.md        # What went where and why
```

## Phase 3: Workflow Integration (Session After)

### **3.1 GitHub Issues Workflow**

Replace alignment companion sections with:
```
ISSUES BOARD:
├── Backlog → Open alignment issues
├── In Progress → Current session work
├── Review → Pending decisions  
├── Done → Resolved issues
```

### **3.2 Session Handoff Automation**
```bash
# Create tools/new-session.sh
#!/bin/bash
# Generate new handoff template
# Update scorecard.md
# Create branch for session work
```

### **3.3 Cross-Reference Validation**
```python
# tools/cross-ref-check.py
# Scan all .md files for broken internal links
# Report missing definitions
# Validate tier cross-references
```

## Migration Priority Order

### **Session 1 (Foundation):**
1. ✅ Repository structure
2. ✅ Handoff memo → markdown template  
3. ✅ Alignment companion → GitHub Issues
4. ✅ v10 decomposition fix and convert
5. ✅ Basic README and CHANGELOG

### **Session 2 (Core Content):**  
1. All WS## files → workstream structure
2. Chapter 6 → manuscript/chapters/
3. Technical appendix → core/technical-appendix/
4. Glossary → core/glossary/
5. Set up cross-reference checking

### **Session 3 (Workflow):**
1. GitHub Issues workflow training
2. Branching strategy setup  
3. Session handoff automation
4. Publishing pipeline basics

## Benefits Realization

### **Immediate** (After Phase 1):
- ✅ No more file size upload failures
- ✅ Proper version control with diff tracking  
- ✅ Backup redundancy (distributed git)
- ✅ Better search across all content

### **Short-term** (After Phase 2):  
- ✅ Cross-reference validation
- ✅ Parallel work on multiple workstreams
- ✅ Automated word counting and status tracking
- ✅ Markdown rendering for easier reading

### **Medium-term** (After Phase 3):
- ✅ GitHub Issues replace alignment companion
- ✅ Pull request workflow for changes
- ✅ Automated session handoff generation
- ✅ Integration with publishing targets

### **Long-term** (Future):
- ✅ GitHub Pages for public HTML versions
- ✅ Automated publishing to multiple targets  
- ✅ Collaboration workflow for peer review
- ✅ CI/CD pipeline for validation

## File Size & Performance Comparison

| Google Drive | GitHub |
|-------------|---------|
| 20KB upload limit | No practical limit |
| Manual version numbering | Automatic git versioning |
| Binary file storage | Text-based diffs |
| No change tracking | Line-by-line change history |
| Link rot on moves | Relative paths move with files |
| Manual backups | Automatic distributed backups |

Ready to start with Phase 1? I can create the repository structure and begin the critical file conversions right now.
