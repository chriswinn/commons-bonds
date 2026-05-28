# Pipeline-Revision Session Close — 2026-05-17

**Date:** 2026-05-17
**Companion to:** [`pipeline-revision-handoff_2026-05-17.md`](pipeline-revision-handoff_2026-05-17.md) (the originating PROPOSED handoff this session worked from)
**Purpose:** Record what landed, what was deferred, what's next. Mirrors the pre-session handoff format for audit-trail symmetry.
**Status:** Session complete; all author-ratified deliverables on `origin/main`.

---

## §1. What landed (commits to `origin/main`)

Five doctrine-cluster commits + one infrastructure-expansion commit + one stubs commit + this close artifact:

| Commit | Scope |
|---|---|
| `3e31d9d` | Pipeline doctrine v1.0.0 cluster — doctrine docs (4) + template revisions (2) + memory-update spec + workstream README update |
| `935633e` | Invariant-gate infrastructure — YAML registries (scaffolding + regressed) + check-corpus-invariants.sh + install-pre-commit-hook.sh + GitHub Actions workflow + quality-gates/README.md + tools/scripts/README.md updates |
| `ed5f6cf` | AGENTS.md canonical-state index + registry commit-sha refresh |
| `85878d1` | Registry expansion — Ch 1 F-V7-V21 + Ch 5/6 Pass 2 + TA Pass 1 + verification round (registry 20 → 37 entries) |
| `aa3e448` | Self-audit fixes — missing build-environment.yaml + Stage 1 doctrine wording + change-cascade cross-reference |
| `d32c8bb` | Build-pipeline scan additions — INTERVIEW NEEDED bracket-placeholder + EB Garamond font-coverage gap documentation |
| `a7c38e2` | Retrofit handoff stubs — template + Ch 1-10 (11 files) |
| (this commit) | TA + AuthorsNote + Dedication stubs + README link update + this session-close artifact |

---

## §2. Decisions ratified (per pipeline-revision handoff §5)

| # | Decision | Disposition |
|---|---|---|
| 1 | Pipeline structure (Stage 0 → 1 [1a/1b/1c] → 2 → 3 [3.1/3.2/3.3/3.4] → 4 → 5) | **CONFIRMED as proposed.** |
| 2 | Single-pipeline architecture with content-type sub-protocols | **CONFIRMED as proposed.** |
| 3 | Invariant-gate scope: pre-commit + stage transitions + CI | **CONFIRMED: all three.** |
| 4 | Change-cascade routing protocol per handoff §3.3 table | **CONFIRMED as proposed.** |
| 5 | Pre-publication review queue mandatory at Stage 5 | **CONFIRMED.** |
| 6 | Bookend sign-offs (academic-rigor + prose-quality at Stage 1 + Stage 5) | **CONFIRMED: both at both.** |
| 7 | YAML registry format | RATIFIED at brainstorm. |
| 8 | Versioning approach | **CONFIRMED hybrid:** memory entry v3.0 summary + pointer; full doctrine in new canonical artifact at `tools/pipeline-doctrine/commons_bonds_pipeline_doctrine_v1.0.0.md`. |
| 9 | Retrofit-all-chapters | RATIFIED at brainstorm; 13 retrofit handoff stubs produced (Ch 1-10 + TA + AuthorsNote + Dedication). |
| 10 | External-reviewer policy | RATIFIED at brainstorm. |
| 11 | Cross-chapter workstream lifecycle | **CONFIRMED six-step lifecycle.** |

All 11 ratified.

---

## §3. Artifacts delivered (per pipeline-revision handoff §4)

### Doctrine cluster
- ✅ `tools/pipeline-doctrine/commons_bonds_pipeline_doctrine_v1.0.0.md` — canonical reference
- ✅ `tools/pipeline-doctrine/commons_bonds_pipeline_doctrine_stage_1_v1.0.0.md` — Stage 1 three-step
- ✅ `tools/pipeline-doctrine/commons_bonds_pipeline_doctrine_stage_4_v1.0.0.md` — render-integrity
- ✅ `tools/pipeline-doctrine/commons_bonds_pipeline_doctrine_stage_5_v1.0.0.md` — sign-off + pre-pub queue

### Template revisions
- ✅ `tools/drafting-templates/stage-3-three-pass-rigor-audit.md` — v3.0 four-pass framing
- ✅ `tools/drafting-templates/audience-pressure-test-construction.md` — v3.0 acceptance + adversarial

### Infrastructure
- ✅ `tools/quality-gates/scaffolding-patterns.yaml` — ~35 patterns, severity-tiered, allowlist-supported
- ✅ `tools/quality-gates/regressed-patterns.yaml` — ~37 patterns (post-expansion); incrementally extensible
- ✅ `tools/scripts/check-corpus-invariants.sh` — bash + awk parser, allowlist filtering, severity modes
- ✅ `tools/scripts/install-pre-commit-hook.sh` — hook installer
- ✅ `.github/workflows/corpus-invariants.yml` — CI workflow (push + PR)
- ✅ `tools/quality-gates/render-baselines/build-environment.yaml` — placeholder for first Stage 4 audit
- ✅ `tools/quality-gates/README.md` — schema documentation

### Memory + index
- ✅ `tools/memory-updates/feedback_audience_aware_drafting_discipline_v3.0.md` — author applies locally
- ✅ `AGENTS.md` — canonical-state table updated with pipeline doctrine + invariant-gate registry rows
- ✅ `tools/workstream-handoffs/README.md` — workstream registry updated + retrofit table populated

### Retrofit handoff stubs (per ratified decision #9; 13 total)
- ✅ `pipeline-retrofit-template_2026-05-17.md` — canonical procedure
- ✅ Ch 1-10 stubs (10)
- ✅ TA stub
- ✅ AuthorsNote stub
- ✅ Dedication stub (conditional on text finalization)

### Audit-trail
- ✅ This session-close artifact

---

## §4. Verified registry state at session close

- HIGH-severity matches in corpus: **3** — all real signal (Ch 2 `[INTERVIEW NEEDED — …]` placeholders at lines 30 + 161 + 166). Block-on-Ch-2-stage; correct behavior.
- MEDIUM matches: 11. All real diagnostic signal for retrofit Pass 2 disposition (Ch 2 declarative-three cadence at L61 + L207; Ch 6 third "they answer different questions" occurrence at L244; Ch 10 closing cadence at L17; $44B canonical-framing flags; old Black Lung debt figure at Ch 2 L133; Ch 3 em-dash density at L38).
- LOW matches: 6. Op-ed metadata informal `~` approximation use; not blocking.

Allowlist exercised: Ch 5 L48 "settlement-ratified"; Ch 6 L158 table-headers; Ch 1 L67 "Time enough to" deliberate four-times; Ch 1 L101 framework-naming F-V14 held; one op-ed historical Black Lung debt snapshot.

---

## §5. What's deferred (open items captured for future sessions)

Per pipeline doctrine §10 + retrofit-handoff cross-references:

1. **Memory entry v2.0 → v3.0 application.** Author applies locally via memory-update spec at `tools/memory-updates/feedback_audience_aware_drafting_discipline_v3.0.md`. Cannot fire from mobile/web sessions (filesystem isolation).
2. **Memory-consolidation audit** (Option A from this session's mid-flight discussion). Paste-text provided to author for a laptop session.
3. **Per-chapter retrofit workstreams.** All 13 stubs produced. PM session sequences spinup. Parallelizable across chapters; some have explicit ordering preferences (Ch 5/6/8/9 prefer AFTER cross-chapter rent-seeking workstream lands; Dedication BLOCKED until text finalized; AuthorsNote prefer AFTER Ch 1 retrofit).
4. **Cross-chapter rent-seeking-engagement workstream.** Independent handoff already PROPOSED at [`cross-chapter-rent-seeking-engagement-handoff_2026-05-17.md`](cross-chapter-rent-seeking-engagement-handoff_2026-05-17.md). Sequence ahead of Ch 5/6/8/9/TA retrofits per cross-chapter lifecycle.
5. **TA pre-publication refresh.** F-7 cumulative oil/gas split exact-percentage (CSV download from sodir.no; ~15 min). Pass 2 typography sweep (F-11 + F-12 + F-14 + F-17; ~45 min). Per TA verification round §H + §I.
6. **HTML source scope for invariant-check.** Current registry scope is markdown-only; TA + Ch 6 HTML need explicit scope extension or per-retrofit `--scope` override. Decision in PM session at TA retrofit spinup.
7. **CI refinement.** Initial CI ships per ratified decision #3 scope; refinement (PR-block vs flag-only; per-push vs per-merge) deferred to first CI-iteration session.
8. **Build-environment.yaml population.** Placeholder shipped; first Stage 4 audit run populates with toolchain version stamps.
9. **Phase B whole-book audit.** Post-retrofit; absorbs Phase B work previously deferred.

---

## §6. Session-procedural notes

- **Branch discipline.** Original feature branch `claude/pipeline-doctrine-setup-r2uSJ` opened from `origin/main`; initial doctrine cluster commits landed (3e31d9d + 935633e + ed5f6cf); fast-forward merged to `main` at session-close-of-original-scope per CLAUDE.md doctrine-cluster autonomous-merge policy. Subsequent continuation commits (85878d1 + aa3e448 + d32c8bb + a7c38e2 + this commit) landed directly on `main` (which was the working branch by then) and pushed; feature branch resynced to match `main` for audit-trail symmetry.
- **No chapter content edits.** Hard constraint honored: this session is `tools/`-side scaffolding work only; no edits to `manuscript/chapters/*Draft*.md` files.
- **Author ratification flow.** All 11 doctrine decisions ratified at session start before drafting began (per the original handoff §5 + the paste-text §"Author ratification needed at session start" gating discipline). Mid-session decisions (continuing with options 1+3, then options 2+4, then Dedication 13th stub) were author-directed in real time.

---

## §7. PM-session pickup notes

For the next PM session that picks up sequencing of retrofit workstreams + the cross-chapter rent-seeking workstream:

1. **First reads:** this session-close artifact + `pipeline-revision-handoff_2026-05-17.md` + `cross-chapter-rent-seeking-engagement-handoff_2026-05-17.md` + retrofit-template + relevant per-chapter stubs.
2. **Sequencing priorities:**
   - Cross-chapter rent-seeking workstream FIRST (it touches Ch 5 + Ch 9 + TA + Ch 8 + bibliography; retrofit workstreams downstream of these chapters prefer to fire AFTER).
   - Ch 1 retrofit can fire any time (lightest; independent).
   - Ch 3 retrofit gated by Colden interview disposition.
   - Ch 2 retrofit gated by `[INTERVIEW NEEDED — …]` placeholder disposition.
   - Dedication retrofit gated by text finalization.
3. **Cross-thread-todos update.** Add post-pipeline-revision state + flag the 13 retrofit workstreams as pending PM-session-sequenced.

---

## §8. Cross-references

- Pre-session handoff: [`pipeline-revision-handoff_2026-05-17.md`](pipeline-revision-handoff_2026-05-17.md) (the source of the workstream)
- Canonical doctrine: [`tools/pipeline-doctrine/commons_bonds_pipeline_doctrine_v1.0.0.md`](../pipeline-doctrine/commons_bonds_pipeline_doctrine_v1.0.0.md)
- Cross-chapter rent-seeking workstream: [`cross-chapter-rent-seeking-engagement-handoff_2026-05-17.md`](cross-chapter-rent-seeking-engagement-handoff_2026-05-17.md)
- Retrofit template: [`pipeline-retrofit-template_2026-05-17.md`](pipeline-retrofit-template_2026-05-17.md)
- Memory-update spec: [`tools/memory-updates/feedback_audience_aware_drafting_discipline_v3.0.md`](../memory-updates/feedback_audience_aware_drafting_discipline_v3.0.md)

---

*End of pipeline-revision session close. 2026-05-17.*
