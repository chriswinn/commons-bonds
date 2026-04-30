# Commons Bonds — Proposed Claude Code Routines

**Version:** 1.0.0
**Date:** 2026-04-28
**Status:** DRAFT — pending author ratification before scheduling
**Author:** Chris Winn (drafting + review); routines run as scheduled remote agents

---

## Background

Per author directive 2026-04-28: explore Claude Code routines (scheduled remote agents) as a feature for the Commons Bonds project. Four routines drafted below for review. Each entry specifies: purpose, cron schedule, prompt text, and expected output format. Author ratifies (or counter-proposes) before scheduling.

Design discipline:
- Each routine is **self-contained** (the remote agent runs without context from a prior session — prompt must include all needed instructions)
- Each routine is **sentinel-style** (catches regressions / tracks state / flags drift; produces actionable findings, not decisions)
- Each routine has **clear output format** (brief; "all clean" when nothing to report; specific punch list when there are findings)
- Each routine respects the **scaffolding-vs-publication** discipline (rigor-pass files contain historical-record retired-vocabulary references; these are NOT regressions and should be excluded)

---

## Routine 1 — Daily terminology-regression sentinel

**Purpose:** Catch retired-vocabulary regressions in chapter manuscripts + framework docs as they're introduced (rather than accumulating until next sweep).

**Cadence:** Daily at 9am ET. Cron: `0 9 * * *`

**Prompt:**

```
You are running a daily terminology-regression sentinel for the Commons Bonds book project at /Users/c17n/Documents/___WorkingOn/commons-bonds.

Run grep -rnE for retired-vocabulary patterns across:
  - manuscript/chapters/
  - core/ (excluding core/terms/terms_index.md and core/scaffolding/)
  - research/

Patterns to check (each is a regex):
  1. "[Ee]ight[ -]?tier" — 8-tier scheme RETIRED 2026-04-24 per tier-reframing rigor pass §11
  2. "\\bAIT\\b" or "Abundance Inversion Test" — RETIRED 2026-04-24, superseded by Commons Inversion Test (CIT) per CIT rename rigor pass commit b294c79
  3. "[Rr]eparations [Bb]ond" — RETIRED 2026-04-24, superseded by Restitution Bond per b1_b2_naming rigor pass commit 8e6a5b2 (NOTE: "reparations economics" as academic-field reference is PRESERVED per b1_b2_naming pass §10; do not flag)
  4. "Reversibility Default" or "\\bRD\\b" (in framework context) — RETIRED 2026-04-24 (same-day flip), superseded by Asymmetric Regret Rule (ARR)
  5. "Asymmetric Regret Principle" or "\\bARP\\b" — RETIRED 2026-04-24, superseded by ARR per ARP rename rigor pass commit b8b62e3
  6. "industrial-existential substitutability gap" or "\\bESG\\b" (in framework context) — RETIRED 2026-04-24 on parsimony grounds; replaced by "industrial-existential substitutability gap" lowercase prose phrase
  7. "Spatial Cost Severance" (Title Case as proper noun) — RETIRED 2026-04-24, replaced with lowercase prose phrase per Spatial CS re-examination rigor pass v1.1
  8. "\\bFGC\\b" or "Full Generational Cost" — RETIRED 2026-04-24 per tier-reframing rigor pass
  9. NOTATION COLLISION — S used as scarcity threshold (collides with substitutability function S(t)) — RENAMED to τ (tau) per Insight #42 RATIFIED 2026-04-29 (Phase 2 Theorem E.3 audit + parallel-session integration §17). Detection patterns:
     - "[Ss]carcity threshold S\\b" (S used as scarcity threshold variable)
     - "\\bS = scarcity\\b" (S being defined as scarcity threshold)
     - "scarcity threshold .{0,30}\\bS\\b" (prose phrasing colliding S with scarcity threshold)
     - "abundance threshold .{0,30}\\bS\\b" (parallel — "abundance threshold" framing)
     Remediation hint: rename S → τ for scarcity/abundance threshold; reserve `S` and `S(t)` exclusively for substitutability function (per Insight #40 E.4 audit + framework's RCV integrand discipline).
  10. NOTATION COLLISION (general) — new single-letter Tech Appendix variable definition that collides with reserved letters. Reserved letter ledger (per current framework usage; cross-check before introducing new variables):
     - **S, S(t)** — substitutability function (Tech Appendix §B Definition A.2; load-bearing in RCV integrand + Theorems E.4 + E.5)
     - **S_max** — substitutability function limit (existential substitutability gap per Insight #33)
     - **τ (tau)** — scarcity threshold per Insight #42 (Phase 2 E.3)
     - **B, B₁, B₂** — Accountability Bond + sub-instruments (Restitution Bond + Foreclosure Bond)
     - **C, Cᵢ** — cost / i-th cost component
     - **CS** — Cost Severance (per equation CS = RCV − B)
     - **D, D(t, t₀)** — discount factor (Weitzman 2001 declining-rate)
     - **E, E(R, t)** — externality tail (function); also Theorem labels E.1–E.5 (context disambiguates)
     - **R** — resource
     - **Q, Q(t)** — quality-stock per Insight #52 (RCV integrand notation)
     - **U, U(R, t, Q(t))** — utility
     - **A** — abundance (Theorem E.3 domain)
     - **r(s), r_∞** — discount rate (per Insight #40 Theorem E.4)
     - **α** — scarcity-multiplier exponent / cost-function curvature parameter
     - **λ** — substitutability function exponential parameter (per Insight #40)
     Detection pattern: heuristic — grep for new variable-definition forms ("Let X = " or "where X is " or "X denotes ") and cross-check the X against reserved-letter ledger above. Flag any conflict.
     Remediation hint: choose a non-reserved letter or Greek letter not already in use (e.g., σ, μ, ν, ξ, π, ρ, φ, ψ, ω; or capital Greek like Γ, Δ, Θ, Λ, Π, Σ, Ψ, Ω).

Exclusions (do NOT flag):
  - core/terms/terms_index.md SUPERSEDED + RETIRED records (canonical record of retired terms)
  - tools/rigor-passes/* (historical-record files documenting the retirements)
  - core/scaffolding/* (internal-process scaffolding may reference retired vocabulary as historical context)
  - alignment/sessions/archive/* (archived session handoffs)
  - core/decomposition/eight-tier-v10.html (retired-archive file)
  - core/glossary/commons_bonds_updated_glossary_v3.html lines flagged with "RETIRED" status indicator

Output format:

If zero findings: report "All clean — no retired-vocabulary regressions detected in active framework artifacts."

If findings: report each as:
  filename:line — pattern matched: <pattern>
  context: <prose context, ~30 words around match>
  remediation hint: <suggested replacement per established cross-chapter precedent>

Limit: report up to 20 findings. If >20, summarize ("N findings; first 20 below; full report at /tmp/regression-report.txt").

Conclude with: "Sentinel run YYYY-MM-DD at HH:MM. Next run: tomorrow 9am ET."
```

**Expected output (clean day):**
> All clean — no retired-vocabulary regressions detected in active framework artifacts. Sentinel run 2026-04-29 at 09:00. Next run: tomorrow 9am ET.

**Expected output (with findings):**
> 2 findings:
> - manuscript/chapters/Chapter__N_*.md:42 — pattern matched: `[Ee]ight[ -]?tier`
>   context: "...walks one extraction through the eight-tier accounting..."
>   remediation hint: per Ch 2/5/6/8 precedent, replace with "the framework's full cost-decomposition" or "cost-component by cost-component"
> - core/case-studies/some-file.md:108 — pattern matched: `\\bAIT\\b`
>   context: "...the AIT methodology has surfaced this cost..."
>   remediation hint: per CIT rename rigor pass, replace with "Commons Inversion Test" or "CIT"
>
> Sentinel run 2026-04-29 at 09:00. Next run: tomorrow 9am ET.

---

## Routine 2 — Weekly pre-submission readiness audit

**Purpose:** Catch publication-readiness blockers (model-output preamble; strikethrough editing markup; truncated paragraphs; INTERVIEW NEEDED placeholders; chapter-length tracking) before they propagate.

**Cadence:** Weekly Monday 8am ET. Cron: `0 8 * * 1`

**Prompt:**

```
You are running a weekly pre-submission readiness audit for the Commons Bonds book project at /Users/c17n/Documents/___WorkingOn/commons-bonds.

For each manuscript/chapters/Chapter_*Draft.* file, check:

1. Model-output preamble residue (publication-blocker):
   - Pattern: lines containing "Let me connect to" / "Let me pull" / "I have the full context" / "Before writing, a few notes" within the first 30 lines of file
   - Findings: flag specific files + line numbers

2. Strikethrough editing markup (publication-blocker):
   - Pattern: ~~text~~ markdown markup
   - Findings: flag files + line numbers (these are author/AI editing notes, should not be in publication artifact)

3. INTERVIEW NEEDED placeholders:
   - Pattern: "[INTERVIEW NEEDED" (case-insensitive)
   - Findings: count per chapter; ok if author-tracked but flagged as pre-submission gate

4. Truncated paragraphs:
   - Pattern: lines ending with "..." mid-paragraph (heuristic: "delivers the intergene" / "the full ext" / similar mid-word truncations)
   - Findings: flag files + line numbers

5. NOTATION COLLISION SWEEP (per Insight #55 framework-wide notation discipline, RATIFIED 2026-04-29):

   Comprehensive cross-document scan for notation collisions across:
   - core/technical-appendix/TechnicalAppendix_v*.html
   - core/terms/terms_index.md
   - manuscript/chapters/Chapter_*Draft.{md,html}
   - core/glossary/commons_bonds_updated_glossary_v*.html

   For each single-letter variable + multi-letter abbreviation in active use:
   (a) Identify all distinct semantic uses across the document set.
   (b) Flag any letter/abbreviation used for >1 distinct concept.
   (c) Cross-check against reserved-letter ledger (Routine 1 pattern #10).

   Specific patterns to scan:
   - Single-letter variables: A, B, C, D, E, P, Q, R, S, U, plus Greek letters α, β, γ, δ, ε, η, θ, λ, μ, ν, π, ρ, σ, τ, φ, ψ, ω
   - Multi-letter abbreviations: RCV, CIT, CSD, ARR, IPG, CS, AIT (retired), FGC (retired), ESG (retired)
   - Subscript patterns: B₁, B₂, Cᵢ, S_max, t₀, r_∞

   Output format:

   For each collision detected:
   - Letter/abbreviation: <symbol>
   - Distinct semantic uses: <list, with file:line examples>
   - Severity: HIGH (load-bearing in framework apparatus) / MEDIUM (used in prose only) / LOW (single-instance overlap)
   - Remediation suggestion: <which use stays + which gets renamed; cite Insight # if already addressed>

   This sweep is retrospective + cumulative; expect zero new collisions per week once Insight #55 audit is complete + Phase 3 v2.0.0 rebuild applied. Pre-completion: expect findings.

6. Chapter-length tracking (per memory rule on standing chapter-length tracking):
   - Word count per chapter file
   - Compare to standing target ranges:
     - Ch 1: 5,000-6,000 (currently partial draft)
     - Ch 2: 5,000-6,000
     - Ch 3: not yet drafted
     - Ch 4: 5,000-6,000
     - Ch 5: 5,000-6,000
     - Ch 6: 6,000-8,000
     - Ch 7: 5,000-6,000
     - Ch 8: 5,000-6,000
     - Ch 9: 5,000-6,000
     - Ch 10: 5,000-7,000
   - Flag chapters substantially above/below target with magnitude

Output format:

Per chapter:
  ## Chapter N — [name]
  - Length: X,XXX words ([STATUS] vs target Y-Z)
  - Model-output preamble: [CLEAN | N findings: ...]
  - Strikethrough markup: [CLEAN | N findings: ...]
  - INTERVIEW NEEDED placeholders: [N count, line refs]
  - Truncated paragraphs: [CLEAN | N findings: ...]
  - Notation-collision findings (in chapter prose): [CLEAN | N findings: ...]
  - Pre-submission status: [READY | NEEDS CLEANUP: ...]

Notation-collision sweep summary (cross-document; not per-chapter):
  - Letters/abbreviations checked: <count>
  - Collisions detected: <count>
  - HIGH severity: <count, list>
  - MEDIUM severity: <count, list>
  - LOW severity: <count, list>
  - All known collisions (Insights #42, #50, #52) addressed: [YES | NO with diff]

Closing summary:
  Total chapters READY for submission: N of 10
  Chapters with publication-blockers: M
  Chapters substantially over target: K
  Chapters substantially under target: J
  Notation-collision status: [CLEAN | N collisions outstanding]

Audit run YYYY-MM-DD. Next run: Monday next week 8am ET.
```

**Expected output:** structured punch list per chapter; can be reviewed with morning coffee.

---

## Routine 3 — Rigor pass status tracker

**Purpose:** Identify rigor passes pending ratification > 7 days; surface drift in rigor-process workflow.

**Cadence:** Weekly Friday 5pm ET. Cron: `0 17 * * 5`

**Prompt:**

```
You are running a weekly rigor pass status tracker for the Commons Bonds book project at /Users/c17n/Documents/___WorkingOn/commons-bonds.

For each file in tools/rigor-passes/:
  1. Read the **Status:** field (line near top of file)
  2. Categorize as:
     - RATIFIED: status field contains "ratified" + date
     - PROPOSED: status field contains "PROPOSED" or "pending author ratification"
     - REJECTED: status field contains "REJECTED" (less common)
     - UNCLEAR: status field absent or unparseable

For PROPOSED rigor passes:
  - Read the **Date:** field
  - Calculate days since proposal
  - Flag any PROPOSED > 7 days old as "AWAITING RATIFICATION"

Output format:

## Ratified rigor passes (count): N
- (list date + filename briefly; no detail required)

## PROPOSED, awaiting ratification:
  - filename — proposed YYYY-MM-DD (X days ago) — recommended verdict per file §1
  - filename — proposed YYYY-MM-DD (X days ago) — recommended verdict per file §1
  ...

## UNCLEAR status (manual review needed):
  - filename — status field unparseable

Closing summary:
  Total rigor passes: N
  Ratified: M
  Proposed > 7 days: K (action needed)
  Unclear: J

Tracker run YYYY-MM-DD. Next run: Friday next week 5pm ET.
```

**Expected output:** brief status summary; only "PROPOSED > 7 days" requires action.

---

## Routine 4 — Open Insights status sync

**Purpose:** Catch drift between Open Insights file (status records) and commit log / chapter prose (referenced insights). Flag any insight referenced in commits but not status-updated.

**Cadence:** Weekly Friday 5pm ET (parallel to Routine 3). Cron: `5 17 * * 5` (offset 5 min from Routine 3)

**Prompt:**

```
You are running a weekly Open Insights status sync for the Commons Bonds book project at /Users/c17n/Documents/___WorkingOn/commons-bonds.

Steps:

1. Read alignment/commons_bonds_open_insights_v1.0.0.md
   - Extract each Insight # + current status (closed-ratified / open / etc.)

2. For each Insight # found:
   a. grep recent commits (last 30 days) for "Insight #N" references
   b. grep chapter prose / framework docs for "Insight #N" references
   c. Compare commit/prose status implications to Open Insights file status

3. Flag drift cases:
   - Insight referenced as "closed" in commits/prose but Open Insights file shows "open"
   - Insight referenced as "open" in commits/prose but Open Insights file shows "closed"
   - Insight with substantive new commits but Open Insights file unchanged > 14 days

Output format:

## Open Insights file status summary:
  - Total insights: N
  - Closed-ratified: M
  - Open: K
  - Other status: J

## Drift flags:
  - Insight #X — [drift description]
    Open Insights file: [status]
    Recent commit/prose evidence: [evidence]
    Action: [suggest update / verify]

(If no drift: "No drift detected — Open Insights file is in sync with commit/prose evidence.")

Sync run YYYY-MM-DD. Next run: Friday next week 5pm ET (5 min after rigor pass tracker).
```

**Expected output:** drift findings or "in sync."

---

## Implementation order recommendation

If implementing all four:

1. **Start with Routine 1 (terminology-regression sentinel)** — highest signal-to-noise; aligns with existing memory rule; catches the bug class we hit ~6 times this restructure cycle.

2. **Then Routine 2 (pre-submission readiness audit)** — catches publication-blocker pattern (Ch 9 preamble; Ch 8 scope-note truncation). Critical before submission to literary agent / publisher.

3. **Routine 3 + 4 (rigor pass tracker + Open Insights sync)** — process-discipline; nice-to-have; lower priority. Can implement together when scheduling Routine 3.

Phased ratification approach (run for 1-2 weeks each before adding the next) lets us see whether the cadence + output format work before building up routine surface area.

---

## Author ratification options

For each routine, author can:
- **Ratify as proposed** — schedule with prompt + cron as drafted
- **Ratify with modifications** — adjust prompt language, cron timing, or output format
- **Reject** — don't schedule (and possibly remove the routine from this list)
- **Defer** — keep in this draft; revisit later

Ratification request:
- [ ] Routine 1 (daily terminology-regression sentinel) — `0 9 * * *`
- [ ] Routine 2 (weekly pre-submission readiness audit) — `0 8 * * 1`
- [ ] Routine 3 (weekly rigor pass status tracker) — `0 17 * * 5`
- [ ] Routine 4 (weekly Open Insights status sync) — `5 17 * * 5`

Once ratified, schedule via Claude Code's scheduled-tasks tooling. Routine output appears as completed remote-agent runs in the routines panel; reviewable when ready.

---

*End of proposed routines v1.0.0. Draft 2026-04-28 by Claude Opus 4.7 at Chris Winn's direction. Pending author ratification before scheduling.*
