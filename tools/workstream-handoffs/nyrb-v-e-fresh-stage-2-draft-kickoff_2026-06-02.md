# NYRB Multi-Book Review-Essay — V-E Fresh Stage 2 Audience-Blind Draft Kickoff — 2026-06-02

**Status:** PROPOSED 2026-06-02 by author per same-day directive following N=3 Pass 3.3 convergence audit (`e4cb25b`) + blind A/B/C comparison (`ab754b1`) findings.

**Workstream:** NYRB Multi-Book Review-Essay → **V-E (fifth variant)** — a SECOND independent Stage 2 audience-blind draft, fired by a fresh session with strict Path-B-preemptive policy against the existing V-D family + locked cut + alts + prior audits.

**Why this chip exists.** The current four-variant grid (locked cut, V-D, V-D', V-D'') all share massive architecture: coastline opener, Pistor-led arc, four-book sequential treatment, Polanyi-Harvey-Ostrom-Raworth-Daly-Sen cross-cutting lineage, mid-century-pivot rhyme to *General Theory* / *Great Transformation* / *Road to Serfdom*, ring-composition close to coastline. Only §VI lineage-density and §VIII closing-list rhetoric vary. The blind A/B/C comparison (`ab754b1`) falsified V-D's §VIII KEEP-ALL-5 recommendation but could not test whether the shared architecture itself is the right local maximum or the only sensible one — all three blind raters were comparing §VIII rhetoric within a single architecture. The architectural choices (opener, book sequencing, synthesis frame, lineage anchors, close type) were invariant across A/B/C and therefore invisible to the comparison.

V-E tests whether a fresh Stage 2 session, working only from the Stage 1 brief + bibliography + four reviewed books (NO exposure to existing V-D family prose), reaches the same architecture or a meaningfully different one. The $100 Barrel parallel-Stage-2-drafts comparative audit 2026-05-21 is the empirical anchor: parallel Stage 2 drafts of the same brief can produce structurally different essays where the differential is execution-choice rather than brief-compliance. v3.1 doctrine treats this as a load-bearing audit move when the brief is non-trivial and a strong iterated control is not available — both conditions hold here.

**Methodology anchor.** v3.1 audience-aware drafting discipline ([`tools/memory/feedback_audience_aware_drafting_discipline.md`](../memory/feedback_audience_aware_drafting_discipline.md)) Stage 2 audience-blind drafting protocol per [`tools/pipeline-doctrine/commons_bonds_pipeline_doctrine_v1.0.0.md`](../pipeline-doctrine/commons_bonds_pipeline_doctrine_v1.0.0.md) §2 + Path B preemptive policy verbatim.

---

## §0. Hard constraints (LOAD-BEARING; read before any other tool call)

### §0.1 Worktree isolation (per SessionStart hook + `feedback_worktree_isolation_for_parallel_sessions.md`)

```bash
HARNESS_ID="$(date +%y%m%d)-$(openssl rand -hex 3)"
WORKSTREAM="nyrb-v-e-fresh-stage-2"
BRANCH="claude/${WORKSTREAM}-${HARNESS_ID}"
WORKTREE_PATH="/Users/c17n/commons-bonds-${WORKSTREAM}-${HARNESS_ID}"
git -C /Users/c17n/commons-bonds fetch origin main
git -C /Users/c17n/commons-bonds worktree add -b "${BRANCH}" "${WORKTREE_PATH}" origin/main
```

All subsequent tool calls use absolute paths inside `${WORKTREE_PATH}`. No cd back to main cwd.

### §0.2 Path B preemptive policy — VERBATIM (Stage 1 brief §6)

**The fresh Stage 2 session must NOT open ANY of the following files at any point during drafting:**

- `manuscript/chapters/Chapter__5_TheAccountabilityGap.md` — Path B preemptive policy (Stage 1 brief §6)
- `manuscript/chapters/Chapter__9_PricingHonestly.md` — Path B preemptive policy (Stage 1 brief §6)
- `publishing/essays/nyrb-multi-book-review/essay.md` — locked cut (V-D family contamination prevention)
- `publishing/essays/nyrb-multi-book-review/_archive/parallel-drafts_2026-05-28/nyrb-multi-book-essay_hybrid_best-of-both.md` — V-D
- `publishing/essays/nyrb-multi-book-review/_archive/parallel-drafts_2026-05-28/nyrb-multi-book-essay_hybrid_drafters-self-audit.md`
- `publishing/essays/nyrb-multi-book-review/_archive/parallel-drafts_2026-05-28/nyrb-multi-book-essay_alt_no-emdashes_260528-26e6c3.md` — alt-no-emdashes
- `publishing/essays/nyrb-multi-book-review/_archive/parallel-drafts_2026-05-28/nyrb-multi-book-essay_alt_normal-punctuation_260528-759ccf.md` — alt-normal-punctuation
- `publishing/essays/nyrb-multi-book-review/_archive/parallel-drafts_2026-06-01/nyrb-multi-book-essay_VD-PRIME_trim-vIII-to-3-cases.md` — V-D'
- `publishing/essays/nyrb-multi-book-review/_archive/parallel-drafts_2026-06-01/nyrb-multi-book-essay_VD-DOUBLE-PRIME_revert-vIII-to-locked-cut.md` — V-D''
- ALL files under `publishing/essays/nyrb-multi-book-review/rigor/` EXCEPT `stage-1-brief.md` (the brief itself is canonical substrate; the audit artifacts are not — opening them would contaminate V-E with prior-audit verdict framings of the V-D family)
- ALL files under `publishing/essays/nyrb-multi-book-review/_archive/` other than the bibliography references already permitted at §0.3

**Any violation = Path B contamination = V-E session ABORTS + author surfaces a fresh-fresh-session retry.**

This is THE load-bearing methodological discipline of the V-E experiment. The whole point is to test whether a fresh session, with no exposure to existing V-D-family prose, reaches the same architecture or a meaningfully different one.

### §0.3 Permitted substrate (the V-E source-material allowlist)

| Source | Path | Purpose |
|---|---|---|
| Stage 1 brief (RATIFIED 2026-05-27 + Amendment-D weight-tag retrofit 2026-06-01) | `publishing/essays/nyrb-multi-book-review/rigor/stage-1-brief.md` | Audience set + structure recommendation + apparatus exclusion + Register A/B discipline + Conditions NR-1 + NR-2 + voice register lock + canonical fact-ground (§7) |
| Bibliography §13 + secondary entries near line 1000 | `research/literature/bibliography.md` | Mazzucato line 523+, Pistor line 531+, Christophers line 539+, Susskind line 547+, secondary entries near line 1009+ |
| The four reviewed books themselves | (physical/digital copies the drafter consults for verbatim quote integrity) | The OPPOSITE of Path B contamination — review-essay verbatim-quote integrity discipline requires source-text fidelity |
| CLAUDE.md | `CLAUDE.md` | Branch discipline + merge-on-ratification rule + voice register |
| v3.1 audience-aware drafting doctrine | `tools/memory/feedback_audience_aware_drafting_discipline.md` | Stage 2 protocol + Amendment D reception-chain weighting |
| No-invented-factual-claims hard rule | `tools/memory/feedback_no_invented_factual_claims_in_publisher_facing_prose.md` | Substrate-safety; no biographical/scene/quote invention |
| Em-dash discipline | `tools/memory/feedback_em_dash_overuse.md` | Em-dash calibration |
| Named-subject consent (public-record exception) | `tools/memory/feedback_named_subject_consent.md` | Public-record exception applies — all named subjects are published authors |
| Merge-on-ratification rule | `tools/memory/feedback_merge_on_ratification.md` | Push discipline |
| Cover letter (already-RATIFIED 2026-05-27) | `publishing/essays/nyrb-multi-book-review/cover-letter.md` | **REVIEW-ONLY** — V-E session may read for register-calibration awareness; cover-letter prose itself is not V-E body-prose source-material; cover-letter reconciles to V-E at post-comparison ratification |

**NB on cover letter.** Including the cover letter in the allowlist is a calibration call: the cover letter signals to NYRB editor what the essay is doing at thesis level. V-E session may read it for awareness of the editor-facing claim structure but should NOT use it as drafting substrate. If V-E's architecture diverges enough that the cover letter needs revision, that surfaces as a downstream chip post-comparison.

### §0.4 Apparatus exclusion list — VERBATIM (Stage 1 brief §8.2)

V-E body prose surfaces **NONE** of the following:

- ❌ CS = RCV − B (the framework's flagship equation)
- ❌ RCV / Residual Commons Value (formal name)
- ❌ CIT / Commons Inversion Test
- ❌ Four Gates
- ❌ Cᵢ vocabulary / cost-component proper-noun names (no "Time Cost" / "Energy Cost" / "Civic Cost" / "Future Cost" as proper-noun named cost-components)
- ❌ Three Ways of Counting
- ❌ ARR / Asymmetric Regret Rule
- ❌ Accountability Bond / B / B₁ + B₂
- ❌ Restitution Bond (proper noun including capitalization)
- ❌ Foreclosure Bond (proper noun including capitalization)
- ❌ Hartwick Identity (formal — distinguished from public-record "Hartwick rule" which IS permitted)
- ❌ Hotelling Identity (formal)
- ❌ Tech Appendix reference
- ❌ 10-dimension structure
- ❌ Commons Bonds (as the framework's name)
- ❌ "The framework" (as authorial-system-construction self-reference)

Concept-level surface ALLOWED (Stage 1 brief §8.1): "cost severance" (lowercase plain-prose; ~3% reveal), "value extraction" (Mazzucato-attributed; ~1%), "pricing-gap / mispricing" (~2%), "legal-architecture-of-accountability" (Pistor-territory; ~1%), "intergenerational pricing gap" (concept-only observation; ~1%), "accountability instruments" (concept-only; <1%). Effective reveal target: ≤8%.

### §0.5 Condition NR-1 verbatim — non-partisan framing discipline (Stage 1 brief §9)

Stern-Nordhaus engagement: **"the existing intellectual battleground"** posture, NOT side-taking. The framework's analytical posture is cross-battleground.

Foregrounded punchline (Stage 1 brief §9.2): *"the question is not whether extraction should have happened but whether cost-bearers should have been compensated"* — phrased as the observation the four-book cluster cumulatively raises, NOT as the framework's punchline.

Center-right policy reader (Tier 1 #3) is TIER 1 DISPOSITIVE per Condition NR-1 at Pass 3.3. INCLUDE verdict REQUIRED.

Hybrid Condition-1-disarming move at §VII close per F-4 ratification 2026-05-27: structural-not-partisan acknowledgment lands at observational distance — NOT first-person reviewer self-narration. NO "this essay's argument is..." / "this review is..." / "Note the move I have just made..." constructions. YES observational-distance phrasing naming the structural-not-partisan posture at the level of *the corrective the four diagnoses point toward*.

Recommended phrasing template (V-E drafter may adapt per voice register): *"The corrective the four diagnoses point toward is structural, not partisan; the construction holds whether the architecture is reached from regulatory caution, market discipline, or worker solidarity — the work this cluster collectively leaves unfinished."* (V-E drafter NOT bound to this phrasing; the discipline operates at the register-of-engagement level, not the verbatim level.)

### §0.6 Condition NR-2 verbatim — critique-register Register A signal-positioning (Stage 1 brief §10)

**Single most consequential brief specification.** Each paragraph engaging a reviewed author's argument MUST position the author's contribution as foundational + analytically necessary + extending in a direction the essay's synthesis names.

Required Register A phrase-patterns (verbatim or close paraphrase per V-E voice register):

- *"Mazzucato shows X — the question is then how to operationalize the corrective her diagnosis demands."*
- *"Pistor's legal-architecture diagnosis names the institutional location the accountability instruments would attach to."*
- *"Christophers' price-failure argument is the mechanism-level evidence the constructive move would correct."*
- *"Susskind's growth-redirection is the macro analog of the per-extraction-event redirection the synthesis names."*

BANNED Register B phrase-patterns (verbatim ban):

- ❌ *"Mazzucato shows X **but stops short of** Y"*
- ❌ *"Pistor names the modules **but** doesn't price"*
- ❌ *"Christophers names the failure **but** doesn't fix"*
- ❌ *"Susskind names the metric **but** doesn't operationalize"*
- ❌ Any "X **falls short of** Y" / "X **doesn't quite reach** Y" / "X **stops short of** Y" / "X **gestures at** Y **without** Z"
- ❌ Any "X but Y" construction across a reviewed-author's name + the essay's analytical move that codes as superior-judgment-of-the-reviewer

**EXCLUDE verdict from any of the four reviewed authors at Pass 3.3 = V-E ABORTS and returns to Stage 1c → Stage 2 re-draft.** Hard discipline gate. Blurb-network protection is the rationale (the four reviewed authors are blurb-network candidates #1+#2+#3+#4 for *Commons Bonds*).

### §0.7 Voice register lock (Stage 1 brief §5 F-5 RATIFIED 2026-05-27)

**Impersonal essayistic voice throughout; NO first-person reviewer presence.** Vendler-tradition NYRB literary-critical impersonal register. NO "I" / "the reviewer" / "this review" / "this essay's argument is..." presence at any point. The reviewer's intelligence is felt in choice-of-scene + sentence-craft + selection-of-passages + sequencing-of-the-four-books, NOT in self-narration.

V-E drafter does NOT have first-person discretion. The impersonal register is locked.

### §0.8 Em-dash discipline (per `feedback_em_dash_overuse.md` RATIFIED 2026-05-21)

Em-dashes require active justification; default to commas / periods / restructure for smoother prose. Long-form review-essays compound em-dash-as-tic-density visibly over 7,000+ words.

Target: 0 em-dashes in body prose (locked cut, V-D, V-D', V-D'' all achieved 0). If V-E reaches a site where em-dash is genuinely the right rhythm and commas/periods/restructure all fail the bar, use sparingly; flag at Pass 3.2 firing for justification.

### §0.9 No invented factual claims (per `feedback_no_invented_factual_claims_in_publisher_facing_prose.md` RATIFIED 2026-05-28)

**Hard rule.** No invented biographical specifics, scene-rendered encounters, period-typical infrastructure details, quoted speech, documentary-record specifics, or motivation attributions. Substrate-safe attributions only:

- Published-work citations from the four reviewed books (bibliography-anchored)
- Verbatim quotes from the four reviewed books (limited; V-E drafter selects per reading-judgment from substrate)
- Public-record on-record speech (e.g., Goldman Sachs CEO Vampire-squid / Doing-God's-work statement is public-record + already a Mazzucato anchor)
- Canonical-concept-attribution to bibliography-anchored intellectual traditions (Polanyi *Great Transformation*; Sen *Development as Freedom*; etc.)

V-E session may consult the four reviewed books directly for verbatim quote integrity. V-E session does NOT generate illustrative invented prose.

### §0.10 Length floor — 7,000w body; NO ceiling (NEW DISCIPLINE 2026-06-02)

**Author directive 2026-06-02:** word-count targets trigger compression pressure that produces clunky prose (the LLM-cadence signature Pass 3.2 voice-polish has to undo); a floor without a cap removes the compression pressure while preserving structural-minimum discipline.

**7,000w body floor.** Below 7,000w, four-book Register A discipline structurally cannot work (~1,400–1,700w per book for close-textual depth × 4 books = ~5,600–6,800w just for §II-§V book engagements; opener + cross-cutting synthesis + constructive close + final synthesis adds architectural overhead pushing structural minimum to ~7,000w). Below floor → at least one of the four reviewed authors gets compressed to catalogue-mention register → Register B drift risk → Condition NR-2 EXCLUDE risk.

**No ceiling.** Per `feedback_substance_drives_length.md`: NYRB venue band is 6,000–10,000w but the band is venue convention, not absolute. Tooze + Halpern review-essays have run 11,000–12,000w when substance justified. V-E lands at whatever length substance reaches; flag at Pass 3.3 if substance-driven length lands materially outside band for venue-fit assessment.

The honest discipline check: if V-E reaches a place where it's saying everything it needs to say at 7,400w, that's the right length for V-E. If it reaches that place at 10,500w with substance still pulling, that's also the right length. The floor protects against compression-from-below; the no-cap protects against compression-from-above.

---

## §1. What V-E session does (the core task)

Audience-blind draft a fresh NYRB multi-book review-essay reviewing Mazzucato + Pistor + Christophers + Susskind, working from:

- Stage 1 brief §1 audience set + §2 editorial-brain map + §5 structural decisions (recommendation only — V-E drafter has architectural discretion) + §7 canonical fact-ground + §8 apparatus exclusion + §9 Condition NR-1 + §10 Condition NR-2 + §14 render-safe convention
- Bibliography §13 + secondary entries
- The four reviewed books themselves for verbatim quote integrity

**V-E drafter has discretion over:**

- **Opener.** Coastline scene is the locked-cut + V-D family's choice; not Stage-1-brief-mandated. Any opener that earns the essay's length and avoids op-ed throat-clearing is permitted. Scene-anchor; close-textual engagement with a specific reviewed-book passage; institutional-architecture observation; etc.
- **Book sequencing.** Stage 1 brief §5 RECOMMENDED Pistor-lead but flagged it as drafter judgment — Mazzucato-lead / Christophers-lead / Susskind-lead all permitted per Stage 1 brief §F-2 ratification (Pistor-lead was the recommendation but the brief explicitly retained drafter discretion).
- **Cross-cutting synthesis architecture.** Negative-space cumulative-diagnosis-without-corrective is the locked-cut + V-D family's frame; not Stage-1-brief-mandated. Architecture-of-engineered-asymmetry; four-stage-pricing-failure; question-asking-architecture; cumulative-emergence — any synthesis frame that holds the apparatus-exclusion + Register A discipline + observational-distance close is permitted.
- **Cross-tradition lineage paragraph.** Polanyi-Harvey-Ostrom-Raworth-Daly-Sen is the locked-cut + V-D family's selection; V-E drafter may select different lineage anchors per reading-judgment. Veblen-Galbraith-Hirschman; Marx-Polanyi-Arrighi; Sen-Nussbaum-Anderson capabilities cluster; Doughnut-economics-and-Schumacher; whatever the synthesis-being-constructed makes natural.
- **Close type.** Ring-composition to opener is the locked-cut + V-D family's choice; not Stage-1-brief-mandated. Question-as-close (Tooze signature); return to a single book's case; forward-looking single-image close; etc.
- **Specific verbatim passages.** V-E drafter selects from the four reviewed books per reading-judgment.

**V-E drafter does NOT have discretion over:**

- Hard constraints §0 above (worktree isolation; Path B preemptive policy; apparatus exclusion list; Condition NR-1 + NR-2; voice register lock; em-dash discipline; no-invented-factual-claims hard rule; 7,000w body floor).
- Stage 1 brief §F-1 ratification (4-book primary set Mazzucato + Pistor + Christophers + Susskind; Patel & Moore NOT activated).
- Stage 1 brief §F-5 ratification (impersonal essayistic voice throughout; NO first-person reviewer presence).
- Register A signal-positioning discipline §0.6 (each reviewed author's contribution positioned as foundational + extension-positioning).

---

## §2. Output: where V-E lands

**Canonical path for V-E body prose:**

`publishing/essays/nyrb-multi-book-review/_archive/parallel-drafts_2026-06-02/nyrb-multi-book-essay_VE-fresh-stage-2.md`

(Create `parallel-drafts_2026-06-02/` directory as needed.)

**YAML frontmatter must include:**

- variant: V-E (fresh-stage-2)
- date: 2026-06-02
- session: claude/nyrb-v-e-fresh-stage-2-{HARNESS_ID}
- based_on: Stage 1 brief (RATIFIED 2026-05-27 + Amendment-D retrofit 2026-06-01) + bibliography §13 entries + four reviewed books themselves
- discipline: Path-B-preemptive (V-D / V-D' / V-D'' / locked cut / alts / prior audits NOT opened); audience-blind drafting per v3.1 Stage 2 protocol
- methodological_caveat: V-E was drafted with no exposure to existing V-D family prose; comparison vs V-D / V-D' / V-D'' is the load-bearing audit move
- word_count: (actual body wc)
- em_dashes_used: (count + per-site justification if non-zero)
- apparatus_discipline_compliance: (named_framework_terms_count: 0; effective_reveal_estimate: ~N%)
- path_b_compliance: (ch5_opened: false; ch9_opened: false; vd_family_opened: false; locked_cut_opened: false; alts_opened: false; prior_audits_opened: false; source_material_consulted: list per §0.3)
- voice_register_compliance: NYRB reviewer-not-architect impersonal essayistic per F-5; zero first-person presence
- verbatim_quotes_added: list (each bibliography-verifiable)

---

## §3. Sequencing after V-E lands

### §3.1 What V-E session ratifies in this kickoff

- V-E PROPOSED at canonical path with full YAML frontmatter disclosure.
- Drafter's self-audit (companion artifact) at `publishing/essays/nyrb-multi-book-review/_archive/parallel-drafts_2026-06-02/nyrb-multi-book-essay_VE-drafters-self-audit.md` — same protocol as V-D drafter's-self-audit (apparatus discipline + Path B compliance + voice register + em-dash discipline + per-character Pass 3.3 self-scoring with explicit drafter-bias acknowledgment).
- Internal scaffolding → auto-fast-forward merge to main per scaffolding cadence.

### §3.2 What V-E session does NOT do

- V-E session does NOT fire Pass 3.1 / 3.2 / 3.3 / 3.4 / 3.5 / Stage 4 / Stage 5. Those are downstream chips.
- V-E session does NOT promote V-E to canonical essay.md. Locked cut + V-D'' (current blind preference per `ab754b1`) remain in flight; V-E lands as parallel-draft for comparison-audit only.
- V-E session does NOT modify Stage 1 brief or any prior-audit artifact.

### §3.3 Downstream chips (post-V-E-PROPOSED; PM coordinates)

1. **Fresh-session Pass 3.1 + 3.2 + 3.3 + 3.4 + 3.5 cascade on V-E** (full 5-pass; not inherited from locked-cut cascade since V-E is architecturally independent).
2. **Blind 4-way A/B/C/D comparison** — V-D vs V-D' vs V-D'' vs V-E ranked by 3+ independent blind sub-agents for NYRB-editor preference. Anonymization protocol matches `ab754b1`: YAML frontmatter stripped before randomization; X/Y/Z/W → variant mapping session-private; sub-agents seeded with NYRB editorial register vocabulary (Silvers/Epstein founding DNA + Greenhouse/Mendelsohn co-editorship + Tooze/Halpern/Caldwell review-essay tradition); ranking + reasoning + confidence-flip condition per rater.
3. **Author selects highest-EV variant** at chip-cascade-completion gate. If V-E wins → V-E promotes to canonical essay.md (after fresh full-cascade ratification); V-D family archives as parallel-draft pedigree. If V-D family wins → V-D'' (or other variant) stays canonical; V-E archives as parallel-draft pedigree.
4. **Cover letter reconciliation** — if V-E architecture diverges materially from V-D family thesis-positioning, cover letter spawns a refresh chip. If not, cover letter inherits without revision.

### §3.4 Submission timeline

NYRB submission window Oct 8 – Nov 15, 2026. Today: 2026-06-02. **Five months of lead time.** V-E draft + full 5-pass cascade + 4-way blind comparison + author ratification cycle easily fits.

---

## §4. STATE marker

```
STATE: nyrb-v-e-fresh-stage-2-draft-kickoff PROPOSED 2026-06-02
NEXT: V-E session fires fresh-Stage-2 audience-blind draft per this kickoff
AWAITING: V-E PROPOSED at canonical path
SEQUENCING DISCIPLINE: V-E lands PROPOSED → downstream chips spawn (fresh 5-pass cascade on V-E + 4-way blind A/B/C/D comparison) → author selects highest-EV variant at chip-cascade-completion gate → selected variant promotes to canonical essay.md → cover-letter reconciles → submission Oct 8 – Nov 15, 2026
ARTIFACT-LINEAGE: locked cut (RATIFIED-AWAITING-SUBMIT 2026-05-27) → V-D / V-D' / V-D'' (parallel-drafts 2026-05-28 + 2026-06-01) → V-E (fresh-Stage-2 2026-06-02); blind A/B/C 2026-06-01 falsified V-D KEEP-ALL-5 §VIII; V-E tests whether the V-D-family shared architecture is the right local maximum
```

---

## §5. Cross-references

- Stage 1 brief: `publishing/essays/nyrb-multi-book-review/rigor/stage-1-brief.md` (RATIFIED 2026-05-27 + Amendment-D retrofit 2026-06-01)
- Locked cut: `publishing/essays/nyrb-multi-book-review/essay.md` (RATIFIED-AWAITING-SUBMIT 2026-05-27)
- N=3 Pass 3.3 convergence audit (this session): `publishing/essays/nyrb-multi-book-review/rigor/pass-3-3-convergence-N3_2026-06-01.md` (PROPOSED 2026-06-01)
- Blind A/B/C comparison (falsified V-D KEEP-ALL-5 §VIII): `publishing/essays/nyrb-multi-book-review/rigor/blind-ABC-comparison-N3_2026-06-01.md` (PROPOSED 2026-06-01)
- V2 audit + Amendment-D-aware addendum: `publishing/essays/nyrb-multi-book-review/rigor/pass-3-3-3-4-3-5-bundled-audience-load-developmental_VERSION-D_INDEPENDENT-AUDIT-V2_2026-05-28.md`
- Empirical anchor for parallel-Stage-2-drafts pattern: $100 Barrel parallel-Stage-2-drafts comparative audit 2026-05-21 (`publishing/essays/100-barrel/rigor/stage-3-comparative-draft-audit.md`)
- v3.1 audience-aware drafting doctrine: `tools/memory/feedback_audience_aware_drafting_discipline.md`
- Substance-drives-length doctrine: `tools/memory/feedback_substance_drives_length.md`
- Em-dash discipline: `tools/memory/feedback_em_dash_overuse.md`
- No-invented-factual-claims hard rule: `tools/memory/feedback_no_invented_factual_claims_in_publisher_facing_prose.md`
- Worktree isolation discipline: `tools/memory/feedback_worktree_isolation_for_parallel_sessions.md`
- Merge-on-ratification rule: `tools/memory/feedback_merge_on_ratification.md`

---

*End of NYRB V-E fresh Stage 2 draft kickoff 2026-06-02. Internal scaffolding (workstream-handoff artifact) → auto-fast-forward merge to main per CLAUDE.md merge-to-main policy + merge-on-ratification rule scaffolding cadence. V-E session fires as a separate worktree-isolated session per §0.1 above.*
