# Commons Bonds: GitHub Workflow Integration Guide

## Replacing the Alignment Companion with GitHub Issues

### **Current System Problems:**
- Alignment companion is a monolithic HTML file
- No threading of discussions  
- Hard to track issue status across sessions
- Cross-references break when files move
- No automated status tracking

### **GitHub Issues Solution:**

#### **Issue Templates**
```yaml
# .github/ISSUE_TEMPLATE/alignment-issue.md
name: Alignment Issue
about: Track project alignment problems
title: '[ALIGNMENT] Brief description'
labels: alignment
assignees: ''

body:
  - type: markdown
    value: |
      ## Alignment Issue Description
      Describe the specific alignment problem or drift

  - type: dropdown  
    id: category
    attributes:
      label: Category
      options:
        - Cross-reference error
        - Architectural refinement
        - Terminology inconsistency  
        - Workstream conflict
        - Decision dependency

  - type: textarea
    id: affected-files
    attributes:
      label: Affected Files
      description: List files that need changes

  - type: textarea
    id: resolution
    attributes:
      label: Proposed Resolution
      description: How should this be fixed?
```

#### **Issue Labels System**
```
PRIORITY:
├── critical          # Blocks other work
├── high              # Needs attention this session
├── medium            # Address when convenient
└── low               # Future consideration

CATEGORY:  
├── alignment         # Companion issues
├── architectural     # Framework refinements  
├── tier-revision     # Scale-abstract updates
├── cross-reference   # Link maintenance
├── decision-needed   # Requires explicit choice
└── project-wide      # Affects multiple workstreams

WORKSTREAMS:
├── ws02-glossary
├── ws03-tiers
├── ws08-technical
└── [etc.]

STATUS:
├── in-progress       # Currently being worked
├── blocked           # Waiting on dependency
├── needs-review      # Ready for decision
└── verified          # Confirmed resolved
```

#### **Milestones as Decision Points**
```
Decision A (DONE) ✅
├── Issue #1: Eight-tier canonicalization
├── Issue #2: Multi-scale validation
└── Issue #3: April 19 ratification

Decision B (WS01)
├── Issue #4: Option C architectural surfacing  
├── Issue #5: Framework positioning
└── Issue #6: Novelty claims scope

Decision C (WS01)  
├── Issue #7: Chapter 10 villain landing
├── Issue #8: Policy prescription tone
└── Issue #9: Implementation pathway

Decision D (WS01)
├── Issue #10: Two-book split decision
├── Issue #11: Scope boundary definition
└── Issue #12: Publication strategy split
```

## Session Handoff Workflow Integration

### **Old Process:**
1. Create handoff HTML file manually
2. Upload to Google Drive (often fails)
3. Reference in next session  
4. Manually track decisions and progress

### **New GitHub Process:**

#### **1. Session Start**
```bash
# Auto-generated branch for session work
git checkout -b session-2026-04-19
git checkout -b ws03-tier-revision  # If working on specific workstream

# Review open issues
gh issue list --label="high,critical" --state=open

# Check milestone progress  
gh issue list --milestone="Decision B" --state=open
```

#### **2. During Session**
```bash
# Create issues as problems are discovered
gh issue create --title="Tier 2a rename affects cross-references" \
                --label="tier-revision,high" \
                --body="Renaming Individual Risk Cost to Actuarial Risk Cost breaks links in Ch.6"

# Link commits to issues
git commit -m "Fix tier 2a cross-references (closes #23)"

# Update progress  
gh issue comment 15 --body="Completed scale-abstract revision for Tier 1. Ready for WS03 execution."
```

#### **3. Session End**
```bash
# Automated handoff generation
tools/generate-handoff.sh 2026-04-19

# Creates:
/alignment/sessions/2026-04-19-handoff.md:
```

```markdown
# Session Handoff: April 19, 2026

## Issues Closed This Session
- #15: Tier 1 scale-abstract revision ✅  
- #23: Tier 2a cross-reference fixes ✅
- #24: Multi-scale validation completion ✅

## Issues Opened This Session  
- #25: Mechanism/shield split implementation
- #26: WS02 glossary integration requirements

## Decisions Made
- **Decision A**: RATIFIED - April 19 eight-tier decomposition is canonical

## Files Modified
- `core/decomposition/eight-tier-v10.md` - Added two-path falsifiability defense
- `workstreams/WS03-tier-definitions/status.md` - Updated with refinement flags
- `alignment/decisions/decision-A-ratification.md` - Documented ratification

## Next Session Priorities
1. **Create v10 decomposition** (addresses #25) - HIGH
2. **Update alignment companion** (addresses #26) - MEDIUM  
3. **Manual cleanup** (Chris does) - LOW

## Technical Notes
- No upload failures - all content saved successfully
- Cross-reference checker passed ✅
- Word count: Essay at 6,247 words (target: 5-8k) ✅

## Milestone Progress
- **Decision A**: COMPLETE ✅
- **Decision B**: 2/6 issues complete (33%)
- **WS02/WS03 Execution**: 1/12 workstreams ready (8%)
```

#### **4. Cross-Session Continuity**
```bash
# Next session starts with:
git checkout develop  
git pull origin develop

# Review handoff
cat alignment/sessions/2026-04-19-handoff.md

# Check issue status
gh issue list --milestone="Decision B" --state=open

# Auto-generate session branch
tools/new-session.sh 2026-04-20
```

## Project Board Integration

### **Kanban View of All Work:**

**🏗️ Backlog**
- [ ] Issue #15: Tier 3 scale-abstract revision  
- [ ] Issue #16: Tier 5 scale-abstract revision
- [ ] Issue #17: WS08 technical appendix update

**⚡ In Progress**  
- [ ] Issue #25: Mechanism/shield split implementation
- [ ] Issue #26: WS02 glossary integration

**👀 Review**
- [ ] Issue #24: Multi-scale validation (awaiting decision)
- [ ] Issue #27: Chapter 6 tone adjustment (needs approval)

**✅ Done**
- [x] Issue #1: Eight-tier canonicalization (Decision A)
- [x] Issue #23: Tier 2a cross-reference fixes
- [x] Issue #24: Multi-scale validation completion

### **Workstream View:**
```
WS02 (Glossary) - 3 open, 2 in progress
WS03 (Tier Definitions) - 6 open, 1 in progress  
WS08 (Technical Appendix) - 2 open, 0 in progress
[etc.]
```

## Automated Quality Checks

### **Pre-commit Hooks:**
```bash
#!/bin/bash
# .git/hooks/pre-commit

# Check cross-references
python tools/cross-ref-check.py

# Validate markdown formatting
markdownlint *.md **/*.md

# Check word count targets
python tools/word-count.py --target manuscript/essay/

# Verify no TODO comments in core files
grep -r "TODO" core/ && exit 1
```

### **CI/CD Pipeline:**
```yaml
# .github/workflows/validate.yml  
name: Validate Content
on: [push, pull_request]

jobs:
  validate:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      - name: Check Cross-References
        run: python tools/cross-ref-check.py
      - name: Build HTML Preview  
        run: pandoc manuscript/essay/*.md -o preview.html
      - name: Upload Artifacts
        uses: actions/upload-artifact@v3
        with:
          name: preview
          path: preview.html
```

## Benefits Summary

| Aspect | Google Drive | GitHub Issues |
|--------|-------------|---------------|
| **Issue Threading** | Linear HTML file | Threaded discussions |
| **Status Tracking** | Manual updates | Automatic labels/milestones |
| **Cross-References** | Break on file moves | Relative paths + validation |
| **Search** | Basic text search | Full metadata search |
| **Collaboration** | Comment-only | Full workflow integration |
| **Automation** | None | Hooks, CI/CD, templates |
| **History** | Manual snapshots | Complete git history |
| **Integration** | Siloed | Links to commits/PRs/files |

## Training Requirements

### **For You (Chris):**
- ✅ Basic git commands (commit, push, pull, branch)
- ✅ GitHub Issues workflow (create, label, close, reference)  
- ✅ Markdown syntax (headers, links, references)
- ✅ Repository navigation (finding files, checking status)

### **For Future Collaborators:**
- ✅ Pull request workflow
- ✅ Code review process
- ✅ Branching strategy
- ✅ Issue assignment and tracking

### **Learning Curve:**  
- **Week 1**: Basic workflow (git + issues)
- **Week 2**: Advanced features (branches, PRs)  
- **Month 1**: Full automation utilization
- **Month 2**: Collaboration and review workflows

The GitHub workflow will initially require learning new tools, but within a month you'll have capabilities that Google Drive simply cannot provide for a project of this complexity and scope.

Ready to proceed with the migration? I recommend starting with Phase 1 (foundation setup) this session.
