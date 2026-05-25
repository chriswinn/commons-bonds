# Publishing-Pipeline Reorganization — Session 1: Comprehensive Audit + Move-List + Reference-Impact-Map

**Status:** PROPOSED. Ratification gates Session 2 (Phase C application).
**Date:** 2026-05-24
**Branch:** `claude/publishing-reorg-session1-audit-affectionate-wing-bb4bd8`
**Workstream:** Publishing-pipeline reorganization (essays + op-eds + literary-agent outreach scaling to ~10 essays/op-eds + 50-100 agent outreaches)
**Trigger:** Author direction 2026-05-24 ("step back and reorganize the essays and outreach folders" + "remove the token cost as a consideration; about to spin up another 4-5 essays + op-eds, and have 50-100 literary agent outreaches in flight").

---

## §0. Why this matters now

Three converging pressures argue for reorg-now-not-later:

1. **Submission-package fragmentation has reached editor-confusion threshold.** Current state requires 4-5 directories to find "everything about Noema submission" — `manuscript/essay/Noema/` (essay text + 14 historical drafts + reference PDFs + planning docs) + `publishing/essay-drafts/` (misnamed: holds cover letters not drafts) + `tools/quality-gates/sign-offs/` (Stage 5 sign-off) + `tools/rigor-passes/` (rigor-pass artifacts) + `publishing/strategy/` (cascade plan + decisions log + rights register). The author's "where is the essay?" question 2026-05-24 was a real-time symptom.
2. **Portfolio about to scale 2x in essays and ~50x in agents.** Current ~5 active essay pipelines → ~10 with 4-5 incoming. Current 1 agency identified → 50-100 typical for first-book trade-press placement. The reorg cost grows quadratically with portfolio size if deferred (more migrations against more in-flight work).
3. **A working architecture already exists at `research/outreach/subjects/`.** 8 per-subject directories (`colden/`, `darity/`, `phat/`, `dagan/`, `biggie/`, `cbf/`, `mazzucato/`, `moore/`) + cross-cutting `_pipeline/` + `_protocols/` + `_templates/` + `archive/` subdirs. Proven at scale; the reorg extends this pattern to essays + op-eds + agent-outreach instead of inventing a new one.

The reorg's principal design move is: **organize by what kind of artifact, then by status, then by venue/target — and let `research/outreach/subjects/` set the per-target-directory pattern across all three outbound pipelines.**

---

## §1. Source artifacts read + verification baseline

1. Current state verification: full recursive `find` across `manuscript/essay/`, `publishing/`, `tools/quality-gates/sign-offs/` (this session 2026-05-24).
2. Cross-reference grep across all `*.md` files for in-scope paths (this session 2026-05-24).
3. `CLAUDE.md` 2026-05-24 amendment ("end-user-facing prose vs. internal scaffolding" merge-to-main boundary).
4. `research/outreach/subjects/colden/` (sample per-subject directory; working pattern reference).
5. `research/outreach/_pipeline/` + `_protocols/` + `_templates/` + `archive/` (cross-cutting subdirs working pattern).
6. `publishing/essay-drafts/boston-review-essay-cover-letter_2026-05-23.md` (cover letter format model).
7. `tools/quality-gates/sign-offs/boston-review-essay_stage5_signoff_2026-05-23.md` (Stage 5 sign-off format model).
8. `publishing/agents/{personalization-snippets,post-darity-warm-intro-templates,query-letter-template,query-tracker,targets}.md` (current flat agent-pipeline state; 5 files).
9. `publishing/strategy/{cascade-plan,decisions-log,rights-register,june-2026-submission-schedule,cross-thread-todos}.md` (cross-essay strategy artifacts).

**No prior reorg artifact exists** — this is the first comprehensive audit + move-list session for the publishing pipeline.

---

## §2. Proposed architecture (codified from session conversation)

### §2.1 Core organizing principle

Three outbound publishing pipelines, all following the same per-target-directory pattern proven at `research/outreach/subjects/`:

1. **Essays** (`publishing/essays/`): one directory per essay submission
2. **Op-eds** (`publishing/op-eds/`): one directory per op-ed
3. **Literary agents** (`publishing/agents/`): one directory per agent (50-100 at scale)

Each follows the same structure:

```
<pipeline>/
├── _shared/              cross-target reusable resources (templates; snippets)
├── _pipeline/            cross-target strategy (tracker; targets; planning)
├── _protocols/           shared discipline (where applicable)
├── _archive/             retired / completed / rejected targets
└── <target-slug>/        per-target directory (essay; op-ed; agent)
    ├── README.md         state + status + checklist + cross-references
    ├── <core-artifact>   essay.md OR op-ed.md OR query-letter.md
    ├── <supporting-artifacts>
    └── _archive/         historical drafts of THIS target
```

### §2.2 Directory tree (target state)

```
publishing/
├── README.md                                  ← NEW — pipeline overview + conventions
├── essays/                                    ← RENAMED from publishing/essay-drafts/
│   ├── README.md
│   ├── _shared/
│   │   ├── templates/
│   │   │   ├── ai-disclosure-paragraph.md   ← MOVED from publishing/essay-drafts/templates/
│   │   │   └── cover-letter-template.md     ← NEW (extracted from BR cover letter pattern)
│   │   ├── personalization-snippets.md      ← NEW (essay-side; agent-side has its own at publishing/agents/_shared/)
│   │   └── README.md
│   ├── _pipeline/                             ← MOVED from publishing/strategy/ (essay-relevant subset)
│   │   ├── cascade-plan_2026-05-06.md
│   │   ├── cascade-plan_v2_2026-05-24.md
│   │   ├── june-2026-submission-schedule.md
│   │   ├── decisions-log.md
│   │   ├── rights-register.md
│   │   ├── cross-thread-todos.md
│   │   └── weekly-audits/
│   │       └── 2026-04-28.md                ← MOVED from publishing/weekly-audit-2026-04-28.md
│   ├── _archive/                              ← retired essay packages
│   ├── noema-commons-bonds/                   ← per-essay package
│   │   ├── README.md
│   │   ├── essay.md
│   │   ├── cover-letter.md
│   │   ├── stage-5-signoff.md               ← copy/symlink from tools/ (design Q1)
│   │   └── _archive/
│   │       ├── pre-pass1-drafts/
│   │       ├── session-handoffs/
│   │       ├── planning/
│   │       └── reference/                    ← venue PDFs (writing guidelines; model pitches)
│   ├── boston-review-accountability-gap/
│   ├── aeon-mask-of-abundance/
│   ├── 100-barrel/
│   ├── atlantic-ideas-<slug>/
│   └── berggruen-<slug>/
│
├── op-eds/                                    ← REORGED (currently flat)
│   ├── README.md
│   ├── _shared/
│   │   └── templates/
│   ├── _pipeline/
│   ├── _archive/
│   ├── mcdowell-county-true-cost/
│   │   ├── README.md
│   │   ├── op-ed.md
│   │   └── canonical-facts.md
│   └── norway-sovereign-wealth/
│       ├── README.md
│       ├── op-ed.md
│       └── canonical-facts.md
│
├── agents/                                    ← REORGED (currently flat; scaling to 50-100)
│   ├── README.md
│   ├── _shared/
│   │   ├── templates/
│   │   │   ├── query-letter-template.md      ← MOVED from publishing/agents/
│   │   │   └── follow-up-email-template.md   ← NEW (placeholder)
│   │   ├── personalization-snippets.md       ← MOVED from publishing/agents/
│   │   ├── post-darity-warm-intro-templates_2026-05-10.md  ← MOVED
│   │   └── README.md
│   ├── _pipeline/
│   │   ├── query-tracker.md                  ← MOVED from publishing/agents/
│   │   ├── targets.md                        ← MOVED from publishing/agents/
│   │   ├── outreach-strategy.md              ← NEW (placeholder; populated by agent-search PM session)
│   │   └── wave-1-plan.md                    ← NEW (placeholder)
│   ├── _protocols/                            ← NEW (analogous to research/outreach/_protocols/)
│   ├── _archive/                              ← passed / declined / closed agents
│   └── <agent-slug>/                          ← per-agent (50-100 at scale)
│       ├── README.md
│       ├── background-brief.md
│       ├── personalization.md
│       ├── query-letter.md
│       ├── correspondence/
│       └── _archive/
│
└── book-proposal/                             ← UNCHANGED
    ├── 00_overview.md
    ├── 01_market-and-audience.md
    ├── 02_comp-titles.md
    ├── 03_author-platform.md                  (cross-referenced from publishing/essays/_shared/ + publishing/agents/_shared/)
    ├── 04_marketing-plan.md
    ├── 05_chapter-summaries.md
    ├── 06_sample-chapters/
    └── proposal-master.md

manuscript/                                    ← collapse manuscript/essay/ into publishing/essays/
├── chapters/                                  ← UNCHANGED
└── (no more essay/ subdirectory; collapsed)

tools/                                         ← UNCHANGED structure (sign-offs decision Q1)
├── rigor-passes/                              ← STAYS HERE (pipeline-internal; naming convention disambiguates)
├── quality-gates/
│   └── sign-offs/                             ← Q1 design decision: stay here OR move into per-essay directory
└── (other tools/ subdirs unchanged)

research/outreach/                             ← UNCHANGED (already the working pattern this reorg extends)
```

### §2.3 What changes vs. what doesn't

| Pipeline area | Current location | New location | Change scope |
|---|---|---|---|
| Essay submission packages | scattered across 4-5 dirs | `publishing/essays/<venue>/` | **MAJOR** |
| Op-ed packages | flat in `publishing/op-eds/` | per-op-ed dirs in `publishing/op-eds/<slug>/` | **MODERATE** |
| Literary agent outreach | flat in `publishing/agents/` | per-agent dirs in `publishing/agents/<agent-slug>/` | **MAJOR** (anticipates 50-100 scale) |
| Cross-essay strategy | `publishing/strategy/` | `publishing/essays/_pipeline/` | **LIGHT** (rename + relocate) |
| Cover letters + templates | `publishing/essay-drafts/` (misnamed) | `publishing/essays/<venue>/cover-letter.md` + `publishing/essays/_shared/` | **MODERATE** |
| Stage 5 sign-offs | `tools/quality-gates/sign-offs/` | Decision Q1: stay OR move per-essay | **DECISION PENDING** |
| Rigor-pass artifacts | `tools/rigor-passes/` | UNCHANGED | (none) |
| Book proposal | `publishing/book-proposal/` | UNCHANGED | (none) |
| Source-subject outreach | `research/outreach/subjects/` | UNCHANGED | (none — already at target pattern) |
| Chapter prose | `manuscript/chapters/` | UNCHANGED | (none) |

---

## §3. Current state inventory (verified 2026-05-24)

### §3.1 manuscript/essay/ — 27 files across 6 venue subdirs

**`manuscript/essay/Noema/` (16 files):**
- `noema-essay-fresh-session-draft_2026-05-10.md` ← submission-ready (Stage 5 RATIFIED 2026-05-24)
- `noema-essay-pre-pass1_2026-05-09.md` ← historical pre-pass-1 snapshot
- `noema-essay-post-pass1_2026-05-09.md` ← historical post-pass-1 snapshot
- `noema-essay-fresh-draft_named_2026-05-09.md` ← historical pre-Stage-2 named variant
- `noema-essay-fresh-draft_anonymized_2026-05-09.md` ← historical pre-Stage-2 anon variant
- `noema-essay-draft_2026-05-09.md` ← Essay A early draft (Path-B-contaminated)
- `noema-commons-bonds-chriswinn_withdrawn_draft.md` ← withdrawn (per `withdrawal-note_2026-05-01.md`)
- `noema-essay-drafting-plan_2026-05-08.md` ← planning
- `rewrite-plan_2026-05-01.md` ← planning
- `withdrawal-note_2026-05-01.md` ← historical record
- `noema-session-handoff_2026-05-09.md` ← session handoff
- `noema-session-handoff_2026-05-10.md` ← session handoff
- `noema-writing-guidelines.pdf` ← venue reference
- `noema-model-pitch.pdf` ← venue reference
- `noema-pitch-commons-bonds-winn.docx` ← historical pitch

**`manuscript/essay/aeon/` (8 files):**
- `aeon-pitch-fresh-session_2026-05-10.md` ← submission-ready
- `aeon-pitch-commons-bonds-winn.md` ← prior pitch version
- `aeon-pitch-commons-bonds-winn_VERSION-C.md` ← prior pitch version
- `aeon-submission-day-package_2026-05-31.md` ← submission package (scheduled 2026-05-31)
- `aeon-essay-carry-forward-inventory.md` ← essay carry-forward inventory (post-acceptance plan)
- `aeon-essay-dunbar-aside-drafts_2026-05-08.md` ← exploratory drafts
- `aeon-session-handoff_2026-05-10.md` ← session handoff
- `aeon-submission-strategy_2026-05-08.md` ← strategy

**`manuscript/essay/boston-review/` (1 file):**
- `boston-review-essay-fresh-session-draft_2026-05-21.md` ← submission-ready (Stage 5 RATIFIED 2026-05-23)

**`manuscript/essay/atlantic-ideas/` (1 file):**
- `atlantic-ideas-essay-fresh-session-draft_2026-05-21.md` ← drafting state TBD

**`manuscript/essay/100-barrel/` (1 file):**
- `100-barrel-essay-draft_2026-05-19_v1.0.0.md` ← submission-ready (Stage 5 RATIFIED 2026-05-24)

**`manuscript/essay/berggruen/` (1 file):**
- `commons-bonds-berggruen-essay-draft.docx` ← binary; drafting state TBD

### §3.2 publishing/essay-drafts/ — 5 files (misnamed; contains cover letters + templates)

- `noema-essay-cover-letter_2026-05-24.md` ← RATIFIED 2026-05-24
- `boston-review-essay-cover-letter_2026-05-23.md` ← RATIFIED 2026-05-24
- `100-barrel-essay-cover-letter_2026-05-24.md` ← RATIFIED 2026-05-24
- `100-barrel-essay-passage.html` ← html rendering / passage artifact
- `templates/ai-disclosure-paragraph.md` ← cross-essay reusable template

### §3.3 publishing/op-eds/ — 3 substantive files + .gitkeep

- `mcdowell-county-true-cost-op-ed_2026-05-10.md` ← op-ed
- `norway-sovereign-wealth-op-ed_2026-05-10.md` ← op-ed
- `_inventory_norway-mcdowell-canonical-facts_2026-05-10.md` ← canonical-facts inventory (shared between the two op-eds)
- `.gitkeep`

### §3.4 publishing/agents/ — 5 files (flat; needs per-agent scale-up)

- `query-letter-template.md` ← template
- `query-tracker.md` ← tracker
- `targets.md` ← target list
- `personalization-snippets.md` ← personalization templates
- `post-darity-warm-intro-templates_2026-05-10.md` ← Darity-interview-derived warm intro templates

### §3.5 publishing/strategy/ — 6 files (cross-essay strategy)

- `cascade-plan_2026-05-06.md` ← canonical cascade plan
- `cascade-plan_v2_2026-05-24.md` ← v2 cascade plan
- `june-2026-submission-schedule.md` ← June batch schedule
- `decisions-log.md` ← decisions log
- `rights-register.md` ← rights register
- `cross-thread-todos.md` ← cross-thread todos

### §3.6 publishing/ top level (1 file)

- `weekly-audit-2026-04-28.md` ← weekly audit

### §3.7 publishing/book-proposal/ — 8 files (UNCHANGED in reorg)

(No reorg changes; preserved as-is.)

### §3.8 tools/quality-gates/sign-offs/ — 3 files (Q1 decision pending)

- `noema-essay_stage5_signoff_2026-05-24.md` ← Stage 5 RATIFIED 2026-05-24
- `boston-review-essay_stage5_signoff_2026-05-23.md` ← Stage 5 RATIFIED 2026-05-24
- `100-barrel-essay_stage5_signoff_2026-05-24.md` ← Stage 5 RATIFIED 2026-05-24

**Total in-scope files: 58 substantive `.md`/`.pdf`/`.docx`/`.html` files across all directories above (excluding `book-proposal/` which is unchanged).**

---

## §4. Move-list (source → destination per file)

### §4.1 Noema essay package

| Source | Destination |
|---|---|
| `manuscript/essay/Noema/noema-essay-fresh-session-draft_2026-05-10.md` | `publishing/essays/noema-commons-bonds/essay.md` |
| `publishing/essay-drafts/noema-essay-cover-letter_2026-05-24.md` | `publishing/essays/noema-commons-bonds/cover-letter.md` |
| `tools/quality-gates/sign-offs/noema-essay_stage5_signoff_2026-05-24.md` | **Q1 decision:** `publishing/essays/noema-commons-bonds/stage-5-signoff.md` OR stay at current location |
| `manuscript/essay/Noema/noema-essay-pre-pass1_2026-05-09.md` | `publishing/essays/noema-commons-bonds/_archive/pre-pass1-drafts/noema-essay-pre-pass1_2026-05-09.md` |
| `manuscript/essay/Noema/noema-essay-post-pass1_2026-05-09.md` | `publishing/essays/noema-commons-bonds/_archive/pre-pass1-drafts/noema-essay-post-pass1_2026-05-09.md` |
| `manuscript/essay/Noema/noema-essay-fresh-draft_named_2026-05-09.md` | `publishing/essays/noema-commons-bonds/_archive/pre-stage-2-drafts/noema-essay-fresh-draft_named_2026-05-09.md` |
| `manuscript/essay/Noema/noema-essay-fresh-draft_anonymized_2026-05-09.md` | `publishing/essays/noema-commons-bonds/_archive/pre-stage-2-drafts/noema-essay-fresh-draft_anonymized_2026-05-09.md` |
| `manuscript/essay/Noema/noema-essay-draft_2026-05-09.md` | `publishing/essays/noema-commons-bonds/_archive/pre-stage-2-drafts/noema-essay-draft_2026-05-09.md` |
| `manuscript/essay/Noema/noema-commons-bonds-chriswinn_withdrawn_draft.md` | `publishing/essays/noema-commons-bonds/_archive/withdrawn-2026-05-01/noema-commons-bonds-chriswinn_withdrawn_draft.md` |
| `manuscript/essay/Noema/withdrawal-note_2026-05-01.md` | `publishing/essays/noema-commons-bonds/_archive/withdrawn-2026-05-01/withdrawal-note_2026-05-01.md` |
| `manuscript/essay/Noema/noema-essay-drafting-plan_2026-05-08.md` | `publishing/essays/noema-commons-bonds/_archive/planning/noema-essay-drafting-plan_2026-05-08.md` |
| `manuscript/essay/Noema/rewrite-plan_2026-05-01.md` | `publishing/essays/noema-commons-bonds/_archive/planning/rewrite-plan_2026-05-01.md` |
| `manuscript/essay/Noema/noema-session-handoff_2026-05-09.md` | `publishing/essays/noema-commons-bonds/_archive/session-handoffs/noema-session-handoff_2026-05-09.md` |
| `manuscript/essay/Noema/noema-session-handoff_2026-05-10.md` | `publishing/essays/noema-commons-bonds/_archive/session-handoffs/noema-session-handoff_2026-05-10.md` |
| `manuscript/essay/Noema/noema-writing-guidelines.pdf` | `publishing/essays/noema-commons-bonds/_archive/reference/noema-writing-guidelines.pdf` |
| `manuscript/essay/Noema/noema-model-pitch.pdf` | `publishing/essays/noema-commons-bonds/_archive/reference/noema-model-pitch.pdf` |
| `manuscript/essay/Noema/noema-pitch-commons-bonds-winn.docx` | `publishing/essays/noema-commons-bonds/_archive/reference/noema-pitch-commons-bonds-winn.docx` |

### §4.2 Boston Review essay package

| Source | Destination |
|---|---|
| `manuscript/essay/boston-review/boston-review-essay-fresh-session-draft_2026-05-21.md` | `publishing/essays/boston-review-accountability-gap/essay.md` |
| `publishing/essay-drafts/boston-review-essay-cover-letter_2026-05-23.md` | `publishing/essays/boston-review-accountability-gap/cover-letter.md` |
| `tools/quality-gates/sign-offs/boston-review-essay_stage5_signoff_2026-05-23.md` | **Q1 decision** |

### §4.3 Aeon essay package

| Source | Destination |
|---|---|
| `manuscript/essay/aeon/aeon-pitch-fresh-session_2026-05-10.md` | `publishing/essays/aeon-mask-of-abundance/essay.md` |
| `manuscript/essay/aeon/aeon-submission-day-package_2026-05-31.md` | `publishing/essays/aeon-mask-of-abundance/submission-day-package_2026-05-31.md` |
| `manuscript/essay/aeon/aeon-essay-carry-forward-inventory.md` | `publishing/essays/aeon-mask-of-abundance/carry-forward-inventory.md` |
| `manuscript/essay/aeon/aeon-pitch-commons-bonds-winn.md` | `publishing/essays/aeon-mask-of-abundance/_archive/prior-versions/aeon-pitch-commons-bonds-winn.md` |
| `manuscript/essay/aeon/aeon-pitch-commons-bonds-winn_VERSION-C.md` | `publishing/essays/aeon-mask-of-abundance/_archive/prior-versions/aeon-pitch-commons-bonds-winn_VERSION-C.md` |
| `manuscript/essay/aeon/aeon-essay-dunbar-aside-drafts_2026-05-08.md` | `publishing/essays/aeon-mask-of-abundance/_archive/planning/aeon-essay-dunbar-aside-drafts_2026-05-08.md` |
| `manuscript/essay/aeon/aeon-submission-strategy_2026-05-08.md` | `publishing/essays/aeon-mask-of-abundance/_archive/planning/aeon-submission-strategy_2026-05-08.md` |
| `manuscript/essay/aeon/aeon-session-handoff_2026-05-10.md` | `publishing/essays/aeon-mask-of-abundance/_archive/session-handoffs/aeon-session-handoff_2026-05-10.md` |
| (no Aeon cover letter in publishing/essay-drafts/) | (none) |
| (no Aeon Stage 5 sign-off in tools/quality-gates/sign-offs/) | (none — pitch model, not full-essay submission) |

### §4.4 $100 Barrel essay package

| Source | Destination |
|---|---|
| `manuscript/essay/100-barrel/100-barrel-essay-draft_2026-05-19_v1.0.0.md` | `publishing/essays/100-barrel/essay.md` |
| `publishing/essay-drafts/100-barrel-essay-cover-letter_2026-05-24.md` | `publishing/essays/100-barrel/cover-letter.md` |
| `publishing/essay-drafts/100-barrel-essay-passage.html` | `publishing/essays/100-barrel/passage.html` |
| `tools/quality-gates/sign-offs/100-barrel-essay_stage5_signoff_2026-05-24.md` | **Q1 decision** |

### §4.5 Atlantic Ideas essay package

| Source | Destination |
|---|---|
| `manuscript/essay/atlantic-ideas/atlantic-ideas-essay-fresh-session-draft_2026-05-21.md` | `publishing/essays/atlantic-ideas-<slug>/essay.md` (slug determined at package creation) |

**Note:** Atlantic Ideas essay has no cover letter yet + no Stage 5 sign-off; the essay is mid-pipeline. New package directory created at move-time.

### §4.6 Berggruen essay package

| Source | Destination |
|---|---|
| `manuscript/essay/berggruen/commons-bonds-berggruen-essay-draft.docx` | `publishing/essays/berggruen-<slug>/_archive/reference/commons-bonds-berggruen-essay-draft.docx` (or essay.docx; slug determined at package creation) |

**Note:** Berggruen submission is a hard-deadline 2026-08-17 prize submission per cascade plan; format is `.docx` (binary); the file may be either a current draft or a reference, depending on Berggruen-essay-workstream state. To verify at Session 2 application.

### §4.7 Op-ed packages

| Source | Destination |
|---|---|
| `publishing/op-eds/mcdowell-county-true-cost-op-ed_2026-05-10.md` | `publishing/op-eds/mcdowell-county-true-cost/op-ed.md` |
| `publishing/op-eds/norway-sovereign-wealth-op-ed_2026-05-10.md` | `publishing/op-eds/norway-sovereign-wealth/op-ed.md` |
| `publishing/op-eds/_inventory_norway-mcdowell-canonical-facts_2026-05-10.md` | **DECISION:** stays at `publishing/op-eds/_shared/canonical-facts/norway-mcdowell-inventory_2026-05-10.md` (shared across both op-eds) OR duplicated into each op-ed dir. Recommend: shared (one source of truth). |

### §4.8 Cross-essay strategy moves

| Source | Destination |
|---|---|
| `publishing/strategy/cascade-plan_2026-05-06.md` | `publishing/essays/_pipeline/cascade-plan_2026-05-06.md` |
| `publishing/strategy/cascade-plan_v2_2026-05-24.md` | `publishing/essays/_pipeline/cascade-plan_v2_2026-05-24.md` |
| `publishing/strategy/june-2026-submission-schedule.md` | `publishing/essays/_pipeline/june-2026-submission-schedule.md` |
| `publishing/strategy/decisions-log.md` | `publishing/essays/_pipeline/decisions-log.md` |
| `publishing/strategy/rights-register.md` | `publishing/essays/_pipeline/rights-register.md` |
| `publishing/strategy/cross-thread-todos.md` | `publishing/essays/_pipeline/cross-thread-todos.md` |
| `publishing/weekly-audit-2026-04-28.md` | `publishing/essays/_pipeline/weekly-audits/2026-04-28.md` |

**Note:** `publishing/strategy/` directory is **deleted** after these moves complete.

### §4.9 Cover-letter template moves

| Source | Destination |
|---|---|
| `publishing/essay-drafts/templates/ai-disclosure-paragraph.md` | `publishing/essays/_shared/templates/ai-disclosure-paragraph.md` |

**Note:** `publishing/essay-drafts/` directory is **deleted** after all moves complete (cover letters move per §4.1-4.4; template moves per above; the misnamed directory is retired).

### §4.10 Agent-pipeline scale-up (current 5 files; target architecture for 50-100)

| Source | Destination |
|---|---|
| `publishing/agents/query-letter-template.md` | `publishing/agents/_shared/templates/query-letter-template.md` |
| `publishing/agents/personalization-snippets.md` | `publishing/agents/_shared/personalization-snippets.md` |
| `publishing/agents/post-darity-warm-intro-templates_2026-05-10.md` | `publishing/agents/_shared/post-darity-warm-intro-templates_2026-05-10.md` |
| `publishing/agents/query-tracker.md` | `publishing/agents/_pipeline/query-tracker.md` |
| `publishing/agents/targets.md` | `publishing/agents/_pipeline/targets.md` |

**Note:** No per-agent directories exist yet — those get created by the upcoming agent-search PM session under the new architecture.

### §4.11 Move-list summary

| Pipeline area | # moves | Net dir change |
|---|---|---|
| Noema essay | 17 moves | New: `publishing/essays/noema-commons-bonds/` + subdirs |
| Boston Review essay | 2 moves + Q1 | New: `publishing/essays/boston-review-accountability-gap/` |
| Aeon essay | 8 moves | New: `publishing/essays/aeon-mask-of-abundance/` + subdirs |
| $100 Barrel essay | 3 moves + Q1 | New: `publishing/essays/100-barrel/` |
| Atlantic Ideas essay | 1 move | New: `publishing/essays/atlantic-ideas-<slug>/` |
| Berggruen essay | 1 move | New: `publishing/essays/berggruen-<slug>/` |
| Op-eds | 3 moves | New: `publishing/op-eds/mcdowell-county-true-cost/` + `publishing/op-eds/norway-sovereign-wealth/` + `_shared/` |
| Cross-essay strategy | 7 moves | Delete: `publishing/strategy/`; Create: `publishing/essays/_pipeline/` |
| Cover-letter templates | 1 move | Delete: `publishing/essay-drafts/` |
| Agent-pipeline reorg | 5 moves | Create: `publishing/agents/_shared/` + `_pipeline/` + `_protocols/` + `_archive/` |
| Q1-pending (Stage 5 sign-offs) | 0-3 moves | DECISION PENDING |

**Total file moves: ~48 (excluding Q1-pending).** Plus directory creations + deletions.

---

## §5. Cross-reference impact map (grep results across all `*.md`)

### §5.1 Total impact

**128 unique `.md` files reference paths in the move-scope.** Substantial but tractable for a single Phase C application session with mechanical grep-and-replace.

### §5.2 Reference categories

| Reference pattern | # files affected | Replacement strategy |
|---|---|---|
| `manuscript/essay/Noema/` | 41 | `publishing/essays/noema-commons-bonds/` (essay → essay.md) or `_archive/...` (historical) |
| `manuscript/essay/aeon/` | 39 | `publishing/essays/aeon-mask-of-abundance/` |
| `manuscript/essay/100-barrel/` | 14 | `publishing/essays/100-barrel/` |
| `manuscript/essay/boston-review/` | 11 | `publishing/essays/boston-review-accountability-gap/` |
| `manuscript/essay/atlantic-ideas/` | 6 | `publishing/essays/atlantic-ideas-<slug>/` |
| `manuscript/essay/berggruen/` | 6 | `publishing/essays/berggruen-<slug>/` |
| `publishing/essay-drafts/` | ~20 | `publishing/essays/<venue>/cover-letter.md` OR `publishing/essays/_shared/` |
| `publishing/strategy/` | ~20 | `publishing/essays/_pipeline/` |
| `publishing/op-eds/<file>.md` | ~12 | `publishing/op-eds/<slug>/op-ed.md` |
| `publishing/agents/<file>` | ~15 | `publishing/agents/_shared/` OR `_pipeline/` per file |
| `tools/quality-gates/sign-offs/` | ~14 | (Q1 decision: stay or move per-essay) |

### §5.3 High-priority cross-reference impact files (most-likely-to-break)

These files reference moved paths heavily + are themselves load-bearing artifacts:

1. **`CLAUDE.md`** — references at least 4 directory paths to be moved (lines 23, 25, 27, 51 per grep). Critical: needs amendment as part of Session 2 (see §10).
2. **All Stage 5 sign-offs** — cross-reference essay paths, cover letter paths, Stage 1 brief paths, rigor-pass artifact paths. The 3 Stage 5 sign-offs (Noema, BR, $100 Barrel) all need internal cross-reference updates after their own location (and the locations they reference) move.
3. **All cover letters** — frontmatter cross-references essay path + Stage 5 sign-off path + Stage 1 brief path + bio source + AI-disclosure source. 3 RATIFIED cover letters (Noema, BR, $100 Barrel) need internal cross-reference updates.
4. **All rigor-pass artifacts** referencing essay paths — likely 30+ files across the rigor-pass directory.
5. **Strategy artifacts** (cascade plan, decisions log, rights register, cross-thread-todos, June schedule) — reference essay paths + each other; their own move location changes.
6. **Workstream handoffs** at `tools/workstream-handoffs/` — reference essay paths + strategy paths.
7. **Research outreach artifacts** at `research/outreach/subjects/` — some reference essay paths (e.g., Phat consent / mentions inventory references the Noema essay).

### §5.4 Reference-update mechanical approach (Session 2)

For each path-pattern in §5.2, run grep-and-replace across the repo. Verify post-replace by re-running the grep to confirm no occurrences of old paths remain. Files that fail post-replace verification get individual review.

Estimated reference-update operations: ~200-300 individual string replacements across ~128 files.

---

## §6. Proposed README content (per new directory)

### §6.1 `publishing/README.md` (top-level)

```markdown
# Publishing pipeline

Three outbound publishing pipelines, plus the book proposal:

- `essays/` — derivative essays going to magazine venues (Noema, Boston Review, Aeon, Atlantic Ideas, $100 Barrel / Phenomenal World, Berggruen, etc.). Per-essay submission packages.
- `op-eds/` — op-eds going to news venues. Per-op-ed packages.
- `agents/` — literary agent outreach. Per-agent directories.
- `book-proposal/` — the book proposal itself.

Each pipeline follows the same per-target-directory pattern (working model:
`research/outreach/subjects/`):

```
<pipeline>/
├── _shared/         cross-target reusable resources (templates; snippets)
├── _pipeline/       cross-target strategy (tracker; targets; planning)
├── _protocols/      shared discipline (where applicable)
├── _archive/        retired / completed / rejected targets
└── <target-slug>/   per-target directory (essay; op-ed; agent)
```

Per-target directories carry a `README.md` with state + status + checklist
+ cross-references to rigor-pass artifacts (which stay at `tools/rigor-passes/`).

See per-pipeline READMEs for area-specific conventions:
- `publishing/essays/README.md`
- `publishing/op-eds/README.md`
- `publishing/agents/README.md`
```

### §6.2 `publishing/essays/README.md`

```markdown
# Essays pipeline

Per-essay submission packages. Each `<venue>-<short-title>/` directory holds
the full submission package for one essay through its complete lifecycle
(drafting → ratifying → submitting → archive after response).

## Per-essay directory layout

```
<venue>-<short-title>/
├── README.md           submission state + checklist + cross-references
├── essay.md            submission-ready essay text
├── cover-letter.md     submission cover note (Decision #13 deliverable)
├── stage-5-signoff.md  Stage 5 sign-off bookend [or referenced from tools/]
└── _archive/           historical drafts of THIS essay
    ├── pre-pass1-drafts/
    ├── pre-stage-2-drafts/
    ├── withdrawn-<date>/   (if applicable)
    ├── session-handoffs/
    ├── planning/           drafting plans; rewrite plans
    └── reference/          venue PDFs (writing guidelines; model pitches)
```

## Status tags

The directory name carries a status tag for at-a-glance state visibility:

- `<venue>-<short-title>/` — active (drafting / pre-submission / ratified-awaiting-submit)
- `<venue>-<short-title>_SUBMITTED-<date>/` — post-submission, awaiting editor response
- `<venue>-<short-title>_PLACED-<date>/` — accepted (could keep or move to `_archive/`)
- `_archive/<venue>-<short-title>_REJECTED-<date>/`
- `_archive/<venue>-<short-title>_WITHDRAWN-<date>/`

Rename directory on state change via `git mv`.

## Cross-references

- Rigor-pass artifacts live at `tools/rigor-passes/` (centralized; naming
  convention disambiguates per-essay; cross-referenced from per-essay
  `README.md`).
- Stage 5 sign-offs: [DECISION Q1 — either centralized at
  `tools/quality-gates/sign-offs/` or co-located at
  `<venue>-<short-title>/stage-5-signoff.md`].
- Shared resources (AI disclosure paragraph; cover-letter template;
  personalization snippets): `_shared/`.
- Cross-essay strategy (cascade plan; decisions log; rights register):
  `_pipeline/`.

## Per-essay README.md contents

Each per-essay `README.md` carries:
- Essay title + venue + submission status (RATIFIED-AWAITING-SUBMIT /
  SUBMITTED / PLACED / etc.)
- Word count + ratification dates
- Cross-references to rigor-pass artifacts (Stage 1 brief; Pass 3.1 / 3.2 /
  3.3 / 3.4 / 3.5; light re-fires; Stage 5 sign-off; cover letter)
- Submission checklist (Stage 4 render; consent-status checks; courtesy
  notifications; submission portal upload action)
- Named-subject inventory (per `tools/memory/feedback_named_subject_consent.md`)
- Cross-essay coordination notes (cascade-plan position; rights-register
  status; rights-clip phrasing for cover letter)
```

### §6.3 `publishing/op-eds/README.md`

```markdown
# Op-eds pipeline

Per-op-ed packages. Each `<slug>/` directory holds the op-ed text +
canonical-facts inventory + cover letter (if applicable to venue).

## Per-op-ed directory layout

```
<slug>/
├── README.md
├── op-ed.md
├── canonical-facts.md       per-op-ed canonical-facts inventory
├── cover-letter.md          (if venue requires)
└── _archive/                historical drafts / variants
```

## Status tags

Same convention as essays. See `publishing/essays/README.md`.

## Shared resources

- Cross-op-ed canonical facts (e.g., facts shared across two related op-eds):
  `_shared/canonical-facts/`
- Templates: `_shared/templates/`
- Cross-op-ed pipeline: `_pipeline/`
```

### §6.4 `publishing/agents/README.md`

```markdown
# Literary agent outreach

Per-agent directories. Mirrors the `research/outreach/subjects/` pattern
(8 active per-subject directories at last count).

Target scale: 50-100 per-agent directories at full agent-outreach wave.

## Per-agent directory layout

```
<agent-slug>/
├── README.md              state + status + notes
├── background-brief.md    agent research (deal-list; client-list; interests; mutual connections)
├── personalization.md     per-agent personalization sentences
├── query-letter.md        personalized query
├── correspondence/        email log (sent + received drafts)
└── _archive/              prior versions; declined / closed correspondence
```

## Status tags

- `<agent-slug>/` — active / pre-query
- `<agent-slug>_QUERIED-<date>/` — query sent; awaiting response
- `<agent-slug>_REQUESTED-<date>/` — partial / full request (advance state)
- `<agent-slug>_PASSED-<date>/` — pass response; move to `_archive/`
- `<agent-slug>_SIGNED-<date>/` — signed (rare; archive after signing)

## Shared resources

- `_shared/templates/query-letter-template.md`
- `_shared/templates/follow-up-email-template.md`
- `_shared/personalization-snippets.md`
- `_shared/post-darity-warm-intro-templates_2026-05-10.md`

## Pipeline strategy

- `_pipeline/query-tracker.md`
- `_pipeline/targets.md` — agent target list (50-100 entries at scale)
- `_pipeline/outreach-strategy.md`
- `_pipeline/wave-1-plan.md`

## Cross-references

- Source-subject outreach (e.g., Darity, Colden): `research/outreach/subjects/`
  (parallel inbound-outreach pipeline; cross-references where warm intros emerge)
- Author platform (bio variants; soft clips): `publishing/book-proposal/03_author-platform.md`
- Essay placements that strengthen agent pitches: `publishing/essays/_pipeline/`
```

### §6.5 Per-essay/per-op-ed/per-agent README.md templates

See §8 below.

---

## §7. Status-tag convention spec

### §7.1 Why status tags

At 10+ active essays + 50-100 agent outreaches, directory-level state visibility is high-value. `ls publishing/agents/ | grep _QUERIED` is faster than grepping README.md state-fields across 100 directories.

### §7.2 Status tag suffix pattern

`<target-slug>_<STATE>-<DATE>/` where:

- `<target-slug>` = base directory name (e.g., `noema-commons-bonds`)
- `<STATE>` = uppercase state tag (see below)
- `<DATE>` = YYYY-MM-DD date of state transition

### §7.3 Essay state tags

| State tag | Meaning | Directory location |
|---|---|---|
| (no suffix) | Active: drafting / pre-submission / ratified-awaiting-submit | `publishing/essays/<slug>/` |
| `_SUBMITTED-<date>` | Submitted; awaiting editor response | `publishing/essays/<slug>_SUBMITTED-<date>/` |
| `_PLACED-<date>` | Accepted; published | `publishing/essays/<slug>_PLACED-<date>/` (or move to `_archive/` after publication) |
| `_REJECTED-<date>` | Rejected | `publishing/essays/_archive/<slug>_REJECTED-<date>/` |
| `_WITHDRAWN-<date>` | Withdrawn | `publishing/essays/_archive/<slug>_WITHDRAWN-<date>/` |

### §7.4 Op-ed state tags

Same as essays (op-eds use the same lifecycle).

### §7.5 Agent state tags

| State tag | Meaning |
|---|---|
| (no suffix) | Active: research / pre-query |
| `_QUERIED-<date>` | Query sent; awaiting response |
| `_REQUESTED-<date>` | Partial / full request received (advance state) |
| `_OFFERED-<date>` | Representation offered (advance state) |
| `_SIGNED-<date>` | Signed with agent |
| `_PASSED-<date>` | Pass response received |

### §7.6 State transitions

Rename directory via `git mv` on state change. Update README.md state field correspondingly.

Example workflow for essay:
```
# Initial state (active / drafting)
publishing/essays/noema-commons-bonds/

# Post-submission
git mv publishing/essays/noema-commons-bonds publishing/essays/noema-commons-bonds_SUBMITTED-2026-05-25

# Post-acceptance
git mv publishing/essays/noema-commons-bonds_SUBMITTED-2026-05-25 publishing/essays/noema-commons-bonds_PLACED-2026-08-15
```

State transitions update all cross-references in the same commit (the README.md state field + the cover letter status + any rigor-pass artifacts that should note the state change).

---

## §8. Template READMEs (per-essay; per-op-ed; per-agent)

### §8.1 Per-essay README.md template

```markdown
# <Essay Title> — <Venue> submission package

**Slug:** `<venue>-<short-title>`
**Venue:** <Noema / Boston Review / Aeon / etc.>
**State:** <DRAFTING / RATIFIED-AWAITING-SUBMIT / SUBMITTED-<date> / PLACED-<date> / REJECTED-<date> / WITHDRAWN-<date>>
**Last updated:** <YYYY-MM-DD>

## Essay status

- **Word count:** ~<N>w (Stage 5 cite)
- **Stage 1 brief:** <ratification date>; located at `tools/rigor-passes/`
- **Stage 3 cycle:** <complete / in progress at Pass N>
  - Pass 3.1 fact-check: <RATIFIED + APPLIED date>; commit `<sha>`
  - Pass 3.2 voice-polish: <RATIFIED + APPLIED date>; commit `<sha>`
  - Pass 3.3 acceptance: <RATIFIED date>; commit `<sha>`
  - Pass 3.4 robustness: <RATIFIED date>; commit `<sha>`
  - Pass 3.5 developmental-edit: <RATIFIED + APPLIED date>; commit `<sha>`
  - Pass 3.3 light re-fire (if applicable): <RATIFIED date>; commit `<sha>`
- **Stage 5 sign-off:** <RATIFIED date>; located at `<path>`
- **Cover letter:** <RATIFIED date>; located at `cover-letter.md`

## Submission checklist

- [ ] Stage 4 render audit (author offline)
- [ ] Venue-specific fact re-verifications (list)
- [ ] Named-subject consent-status checks (list)
- [ ] Courtesy notifications (list)
- [ ] Cover letter venue-personalization re-verification
- [ ] Submit via <venue> portal

## Named-subject inventory

Per `tools/memory/feedback_named_subject_consent.md`:

- **<Subject>** (<status>): <citation locations in essay>

## Cross-essay coordination

- Cascade-plan position: <reference>
- Rights-register status: <reference>
- Soft-clip phrasing carry: <reference>

## Cross-references

- Essay text: `essay.md`
- Cover letter: `cover-letter.md`
- Stage 5 sign-off: `stage-5-signoff.md` OR `tools/quality-gates/sign-offs/...`
- Stage 1 brief: `tools/rigor-passes/<brief-slug>.md`
- All rigor-pass artifacts: `tools/rigor-passes/` (filter by `<venue>` slug)
- Historical drafts: `_archive/`
```

### §8.2 Per-op-ed README.md template

```markdown
# <Op-Ed Title>

**Slug:** `<slug>`
**Target venues:** <list>
**State:** <DRAFTING / RATIFIED-AWAITING-SUBMIT / SUBMITTED-<date> / PLACED-<date>>
**Last updated:** <YYYY-MM-DD>

## Op-ed status

- **Word count:** ~<N>w
- **Stage cycle:** <complete / in progress>
- **Canonical-facts inventory:** `canonical-facts.md` (or `_shared/canonical-facts/<inventory>.md` if shared)

## Submission checklist

- [ ] Final fact re-verification
- [ ] Venue-specific format check
- [ ] News-peg activation timing (per `_pipeline/op-ed-news-peg-strategy.md` if available)
- [ ] Submit to <venue>

## Cross-references

- Op-ed text: `op-ed.md`
- Canonical facts: `canonical-facts.md`
- Cover letter (if venue requires): `cover-letter.md`
- Historical drafts: `_archive/`
```

### §8.3 Per-agent README.md template

```markdown
# <Agent Name> — <Agency>

**Slug:** `<agent-slug>`
**Agency:** <Agency Name>
**State:** <RESEARCHING / READY-TO-QUERY / QUERIED-<date> / REQUESTED-<date> / OFFERED-<date> / SIGNED-<date> / PASSED-<date>>
**Last updated:** <YYYY-MM-DD>

## Agent profile (summary)

- **Recent deals:** <list>
- **Client list:** <list>
- **Interests / specialties:** <relevant matches to *Commons Bonds*>
- **Mutual connections:** <if any>
- **Submission preferences:** <query letter only / sample chapters / full proposal>

## Outreach state

- **Query sent:** <date> via <method>
- **Response received:** <date / status>
- **Follow-up cadence:** <next-action date if applicable>

## Cross-references

- Background research: `background-brief.md`
- Per-agent personalization: `personalization.md`
- Query letter: `query-letter.md`
- Correspondence log: `correspondence/`
- Bio source: `publishing/book-proposal/03_author-platform.md`
- Shared resources: `publishing/agents/_shared/`
- Soft-clip status: `publishing/essays/_pipeline/rights-register.md`
```

---

## §9. Open design decisions requiring author ratification before Session 2

These decisions were surfaced in the session conversation 2026-05-24 but not finalized. Ratification gates Session 2.

### §9.1 Q1 — Stage 5 sign-off location

**Option Q1-A: Keep in `tools/quality-gates/sign-offs/`.**
- Sign-off pattern consistency across essays
- Single canonical location for sign-off-template editing
- Mirrors `tools/rigor-passes/` discipline
- "Find everything about Noema" still requires 2 locations (per-essay dir + tools/)

**Option Q1-B: Move into per-essay directory at `publishing/essays/<venue>/stage-5-signoff.md`.**
- Self-contained submission package; portable
- "Find everything about Noema" → one directory
- Sign-off discipline distributes across essays (slightly harder template maintenance)

**Claude recommendation:** **Q1-A.** Keep centralized. The per-essay README.md cross-references the sign-off by canonical path. Consistent with rigor-pass-artifact discipline.

### §9.2 Q2 — `manuscript/essay/` collapse vs. keep separate authoring workspace

**Option Q2-A: Collapse `manuscript/essay/` into `publishing/essays/<venue>/`.**
- One directory per essay through full lifecycle
- Drafting in progress + submission-ready + archived historical drafts all in one place
- Simpler mental model
- `_archive/` captures historical drafts within per-essay directory

**Option Q2-B: Keep `manuscript/essay-drafts/<venue>/` as separate authoring workspace.**
- Clear separation between drafting-in-progress and submission-ready package
- Drafts "graduate" from `manuscript/essay-drafts/` to `publishing/essays/` when submission-ready
- Two locations per essay; graduation step adds friction

**Claude recommendation:** **Q2-A.** Collapse. At portfolio scale, simpler is better; status-tag convention handles the drafting-vs-submission-ready visibility.

### §9.3 Q3 — Status-tag convention for agents

**Option Q3-A: Directory-name suffix** (e.g., `<agent-slug>_QUERIED-<date>/`)
- Visible at directory level
- Single `ls | grep` finds all queried-but-not-responded agents
- Cheap to maintain (single `git mv` per state change)

**Option Q3-B: README state field only** (stable directory names)
- No directory renames on state change
- Less visible at-a-glance
- Easier maintenance (no need to remember to rename)

**Claude recommendation:** **Q3-A.** Visibility wins at 50-100 scale. Same convention for essays + op-eds + agents.

### §9.4 Q4 — Agency-vs-agent disambiguation for agent directories

**Option Q4-A: Two-level — `<agency-slug>/<agent-slug>/`.**
- Accurate hierarchy (agents work at agencies)
- Supports parallel-queries-at-same-agency scenarios
- Heavier directory structure

**Option Q4-B: Flat — `<agent-slug>/` with agency-name in README.md.**
- Simpler structure
- Cross-agent comparisons easier (flat list)
- Slightly less hierarchical clarity

**Claude recommendation:** **Q4-B.** Flat. Most agencies have one relevant agent per book; 2-level structure adds complexity that doesn't pay off at first-book scale. Cross-references in README handle the agency dimension.

### §9.5 Q5 — Op-ed canonical-facts inventory location

**Option Q5-A: Shared at `publishing/op-eds/_shared/canonical-facts/<inventory>.md`** when facts span multiple op-eds.
- One source of truth
- Easier to maintain (fact-updates propagate to both op-eds)
- Per-op-ed README cross-references the shared inventory

**Option Q5-B: Duplicated into each per-op-ed directory.**
- Self-contained per-op-ed package (portability)
- Drift risk (facts can drift between duplicates)

**Claude recommendation:** **Q5-A.** Shared. The Norway + McDowell canonical-facts inventory currently at `publishing/op-eds/_inventory_*` is shared by design (two op-eds derive from one inventory); preserving that pattern is correct.

### §9.6 Q6 — Aeon essay slug naming

The Aeon essay's working title (per `aeon-pitch-commons-bonds-winn_VERSION-C.md`) is "The Mask of Abundance" — proposed slug `aeon-mask-of-abundance`.

**Open:** is this the right slug? Author confirms or revises.

### §9.7 Q7 — Atlantic Ideas + Berggruen essay slug naming

Both essays have no explicit working title yet in the file frontmatters I sampled. Slugs need author input:
- Atlantic Ideas: `atlantic-ideas-<slug>` — proposal needed
- Berggruen: `berggruen-<slug>` — proposal needed

### §9.8 Q8 — Boston Review essay slug

The Boston Review essay's working title is "The Accountability Gap" per the cover letter — proposed slug `boston-review-accountability-gap`.

**Open:** confirm or revise.

### §9.9 Q9 — Stage 5 sign-off filename in per-essay dirs (if Q1-B)

If Q1-B is ratified (move sign-offs into per-essay dirs), proposed filename is `stage-5-signoff.md` (drops the venue-name redundancy since the directory already names the venue).

### §9.10 Q10 — README.md state-tag convention update vs. directory-name update

Two ways to track state changes:
- Update directory name (per §7) — visible at `ls`
- Update README.md state field — cleaner; no directory churn

**Hybrid recommendation:** use directory-name suffix for major state transitions (SUBMITTED, PLACED, REJECTED, WITHDRAWN, QUERIED, SIGNED) + README.md state field for fine-grained sub-state notes. The directory-name suffix is the primary signal; README.md carries the detail.

---

## §10. CLAUDE.md amendments needed

CLAUDE.md (lines 23-51 grep results) references several paths that move:

### §10.1 Current CLAUDE.md text (excerpts)

> - `manuscript/essay/` — derivative-essay prose (Aeon, Noema, BR,
>   PW, Atlantic Ideas, Wave 2 candidates, etc.)
> - `publishing/op-eds/` — op-ed canonical drafts (news-peg
>   activation variants in dated sibling files are derivatives)
> - `publishing/book-proposal/` — proposal prose (agent/editor-
>   facing)
> - `publishing/strategy/` — cascade plans, decisions logs, ...

### §10.2 Proposed CLAUDE.md amendments

Replace the path references with the new architecture:

**End-user-facing prose (author ratification BEFORE merge to main):**

- `manuscript/chapters/` — book chapter prose
- `publishing/essays/<venue>/essay.md` + `cover-letter.md` — derivative essays + cover notes
- `publishing/op-eds/<slug>/op-ed.md` — op-ed prose
- `publishing/book-proposal/` — proposal prose (agent/editor-facing)
- `publishing/agents/<agent-slug>/query-letter.md` + `correspondence/` — outbound agent communication
- Outreach packet content at `research/outreach/subjects/<subject>/` (subject-facing material)

**Internal scaffolding (auto-merge to main at session close):**

- `tools/rigor-passes/`
- `tools/workstream-handoffs/`
- `tools/quality-gates/`
- `publishing/essays/_shared/`, `_pipeline/`, `_archive/`, README.md, per-essay README.md
- `publishing/op-eds/_shared/`, `_pipeline/`, `_archive/`, README.md, per-op-ed README.md
- `publishing/agents/_shared/`, `_pipeline/`, `_protocols/`, `_archive/`, README.md, per-agent README.md
- `publishing/essays/<venue>/_archive/` (historical drafts; internal record)

**Note:** Stage 5 sign-offs (Q1 decision pending) — if Q1-A, stay at `tools/quality-gates/sign-offs/` (internal scaffolding). If Q1-B, sign-offs move to per-essay directory but remain internal scaffolding (publisher doesn't see them; they're pipeline-discipline artifacts).

### §10.3 Other CLAUDE.md references to verify post-Session-2

- Per-essay file paths cited as examples in `tools/memory/` files
- Per-essay file paths cited in `tools/drafting-templates/` files
- Per-essay file paths cited in `tools/commons_bonds_pipeline_doctrine_*` files

Session 2 needs to grep these explicitly.

---

## §11. Session 2 sequencing + checklist

Session 2 (Phase C application) executes the move-list + cross-reference updates + README population in a single comprehensive session. Per author "remove the token cost as a consideration," this can be a heavy session.

### §11.1 Session 2 sequence

1. **Pre-session verification.**
   - Verify origin/main has not advanced since Session 1 PROPOSED commit (rebase if needed)
   - Verify no in-flight work on essays / cover letters / sign-offs that would conflict
   - Verify no parallel agent-search PM session is mid-fire (which would generate new files under old architecture)

2. **Author ratification of §9 design decisions.**
   - Q1 (Stage 5 sign-off location)
   - Q2 (manuscript/essay/ collapse)
   - Q3 (status-tag convention)
   - Q4 (agency-vs-agent disambiguation)
   - Q5 (op-ed canonical-facts inventory location)
   - Q6-Q8 (essay slug naming)
   - Q9 (sign-off filename if Q1-B)
   - Q10 (state-tag tracking)

3. **Phase A — Directory structure creation.**
   - Create all new `_shared/`, `_pipeline/`, `_protocols/`, `_archive/` directories
   - Create all new per-essay / per-op-ed directories
   - Create directory placeholders with `.gitkeep` where needed

4. **Phase B — File moves.**
   - Execute all `git mv` operations per §4 move-list
   - One commit per pipeline (essays / op-eds / agents) for cleaner blame history

5. **Phase C — Cross-reference updates.**
   - Run grep-and-replace per §5.2 reference patterns
   - Update CLAUDE.md per §10.2 amendments
   - Update all Stage 5 sign-offs (3 files) internal cross-references
   - Update all cover letters (3 files) internal cross-references
   - Update all strategy artifacts internal cross-references
   - Update all rigor-pass artifacts that reference essay paths

6. **Phase D — README population.**
   - Top-level `publishing/README.md`
   - Per-pipeline `publishing/<pipeline>/README.md`
   - Per-essay `README.md` (6 active essays)
   - Per-op-ed `README.md` (2 op-eds)
   - Per-agent template `README.md` (placeholder; populated by future agent-search session per-agent)

7. **Phase E — Verification.**
   - Re-run grep for old paths; verify no occurrences remain
   - Verify all in-flight essays / cover letters / sign-offs render correctly at new locations
   - Verify CLAUDE.md updates are syntactically + semantically clean
   - Verify `tools/scripts/check-corpus-invariants.sh` still passes (scaffolding patterns may reference moved paths)
   - Verify `tools/scripts/docker-render.sh` still renders correctly (if it references moved paths)

8. **Phase F — Commit + push.**
   - Single comprehensive commit or one-commit-per-phase
   - Push to origin/main per CLAUDE.md author-ratified content-change merge default
   - (Session 2 is author-ratified per §11.1 step 2)

### §11.2 Session 2 estimated scope

- ~48 file moves
- ~200-300 string replacements across ~128 files
- ~10 new README files
- ~5-10 CLAUDE.md amendments + memory file updates

Conservative session-token estimate: 40-60K tokens. Per author "remove the token cost as a consideration," budget allowed.

### §11.3 Session 3 (optional)

After Session 2 completes, optional Session 3 fills out the per-essay / per-op-ed / per-agent README.md content for in-flight items with state details (current state; commit SHAs; cross-references; submission checklists). Lighter — ~15-20K tokens.

---

## §12. What this session did NOT do

- **Did NOT execute any file moves.** Session 1 is audit + planning only. Session 2 (Phase C application) executes moves.
- **Did NOT modify CLAUDE.md.** Session 2 applies CLAUDE.md amendments.
- **Did NOT update any existing essay / cover letter / sign-off cross-references.** Session 2 applies cross-reference updates.
- **Did NOT contact named subjects.**
- **Did NOT propose Session 2 fire automatically.** Author ratification of §9 design decisions gates Session 2.
- **Did NOT propose changes to `research/outreach/subjects/` architecture** — that pattern is the working model the reorg extends, not the target of the reorg.
- **Did NOT propose changes to `manuscript/chapters/` architecture.**
- **Did NOT propose changes to `tools/rigor-passes/` or `tools/workstream-handoffs/` architecture.**
- **Did NOT propose changes to `publishing/book-proposal/` architecture.**

---

## §13. Hard constraints honored

- ✓ Did NOT apply file moves (Session 1 is audit-only).
- ✓ Verified current state via `find` + grep on 2026-05-24.
- ✓ Built feature branch `claude/publishing-reorg-session1-audit-affectionate-wing-bb4bd8` from current origin/main per CLAUDE.md branch-discipline.
- ✓ Per CLAUDE.md rigor-pass-artifact / workstream-handoff merge-to-main default, this audit artifact autonomously fast-forwards to main at session close.
- ✓ Session 1 is planning artifact (workstream-handoff classification per `tools/workstream-handoffs/README.md`); auto-merges per CLAUDE.md internal-scaffolding boundary.
- ✓ Per author "remove the token cost as a consideration," scope is comprehensive across all in-scope directories.
- ✓ Surfaced 10 open design decisions explicitly for author ratification before Session 2 fires.

---

*End of Publishing-Pipeline Reorganization Session 1 audit + move-list + reference-impact-map artifact (PROPOSED). Auto-merges to main per CLAUDE.md internal-scaffolding boundary. Author ratification of §9 design decisions gates Session 2 (Phase C application). Session 2 estimated scope: ~48 file moves + ~200-300 string replacements across ~128 files + ~10 new READMEs + CLAUDE.md amendments + verification. After Session 2: per-essay/per-op-ed/per-agent README.md content population (Session 3, optional) + agent-search PM session inherits new architecture from day one.*
