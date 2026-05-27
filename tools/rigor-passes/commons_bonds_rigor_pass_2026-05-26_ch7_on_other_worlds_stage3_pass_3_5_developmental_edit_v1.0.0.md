# Commons Bonds — Ch 7 *On Other Worlds* — Stage 3 Pass 3.5 (Developmental-Edit)

**Date:** 2026-05-26
**Workstream:** Manuscript Stage-3 Rigor Pass (PM dashboard #20), Phase A — Pass 3.5 developmental-edit per v3.1 Amendment B (ratified 2026-05-18)
**Chapter file:** [Chapter__7_OnOtherWorlds.md](../../manuscript/chapters/Chapter__7_OnOtherWorlds.md) (250 lines, post-Phase-C-β / pre-Phase-C-γ state at session start)
**Discipline:** v3.1 Amendment B Pass 3.5 (whole-chapter restoration-of-richness lens; restoration polarity, NOT cutting); Amendment-C-scoped (Interactive Ratification Protocol per [feedback_audience_aware_drafting_discipline.md](../memory/feedback_audience_aware_drafting_discipline.md) v3.1: per-finding format includes Options + Recommendation + Reasoning)
**Mode:** audit-existing-prose
**Primary format model:** [Ch 9 Pass 3.5 developmental-edit (2026-05-25)](commons_bonds_rigor_pass_2026-05-25_ch9_pricing_honestly_pass_3_5_developmental_edit_v1.0.0.md) (most analogous analytical-policy register; per-finding inventory + Options/Recommendation/Reasoning + cross-character impact analysis + §6 discipline-check footer)
**Secondary format model:** [Ch 2 Pass 3.5 developmental-edit (2026-05-25)](commons_bonds_rigor_pass_2026-05-25_ch2_the_miner_pass_3_5_developmental_edit_v1.0.0.md) (per-finding inventory pattern + author-revisit candidate flagging)
**Status:** PROPOSED. Awaiting author ratification before Phase C-δ spot-fix application session.
**Branch:** `claude/manuscript-stage-3-ch7-pass3-5-agent-a780222e83724b34b` (feature branch attempt; sandbox blocked git checkout — see §0.4 below; this artifact is committed on `worktree-agent-a780222e83724b34b` branch which is the worktree default branch and will be merged to the feature branch / origin/main at session close per workstream branch discipline).

---

## §0. Source artifacts read + chapter-state verification

### §0.1 Source artifacts read

| Artifact | Path | Verification |
|---|---|---|
| Ch 7 — *On Other Worlds* | `manuscript/chapters/Chapter__7_OnOtherWorlds.md` | 250 lines; post-Phase-C-β state; latest chapter-file commit on origin/main is `e29d5ae` Ch 7 Phase C-β. |
| Pass 3.1 fact-check | `tools/rigor-passes/commons_bonds_rigor_pass_2026-05-16_ch7_on_other_worlds_stage3_fact_check_v1.0.0.md` | CLOSED 2026-05-20 — ratification `4948dbb`; Phase C-α application `4987e59`. |
| Pass 3.2 voice-polish | `tools/rigor-passes/commons_bonds_rigor_pass_2026-05-21_ch7_on_other_worlds_stage3_voice_polish_v1.0.0.md` | CLOSED 2026-05-21 — ratification `440906f`; Phase C-β application `e29d5ae`. §6 carry-forward (Pass-3.5-attention items) read in full. §11 ratification record (5 prose edits at lines 21, 85, 121, 195, 229; 14 holds; 2 §5.3 apparatus-form resolutions) read in full. |
| Pass 3.3 acceptance | `tools/rigor-passes/commons_bonds_rigor_pass_2026-05-25_ch7_on_other_worlds_stage3_pass_3_3_audience_load_acceptance_v1.0.0.md` | CLOSED 2026-05-25 — verdict ratified `697bcd2`; §8.3 Option A HOLD `0a3de00`. |
| Pass 3.4 robustness | `tools/rigor-passes/commons_bonds_rigor_pass_2026-05-25_ch7_on_other_worlds_stage3_pass_3_4_audience_load_robustness_v1.0.0.md` | PROPOSED `8c8f1f5`; initially ratified Option A HOLD `d46a6ae` 2026-05-26 (close Stage 3); reconsidered same day per framing under new context (T1+T3+T4 applying in parallel worktree). §6 (two Pass-3.5-attention items) read in full: (a) apparatus-density spike at lines 137–151; (b) objection-response section length at lines 179–203. |
| Ch 9 Pass 3.5 format model | `tools/rigor-passes/commons_bonds_rigor_pass_2026-05-25_ch9_pricing_honestly_pass_3_5_developmental_edit_v1.0.0.md` | Primary format model. Per-finding Options + Recommendation + Reasoning structure; §3 cross-character impact analysis; §6 discipline-check footer. |
| Ch 2 Pass 3.5 format model | `tools/rigor-passes/commons_bonds_rigor_pass_2026-05-25_ch2_the_miner_pass_3_5_developmental_edit_v1.0.0.md` | Secondary format model. §2.A/B/C bucket structure + author-revisit candidate flagging. |
| Ch 6 dev-edit review | `tools/rigor-passes/ch6_developmental_edit_review_2026-05-20.md` | Methodology-chapter precedent — referenced for analytical-register restoration calibration. |
| Ch 3 dev-edit review | `tools/rigor-passes/ch3_developmental_edit_review_2026-05-25.md` | Referenced for restoration-polarity discipline + scene-anchor restoration patterns. |
| Apparatus register decisions | `tools/rigor-passes/commons_bonds_rigor_pass_2026-05-11_apparatus_register_decision_v1.0.0.md` | Items 7 (CIT dropped), 10 (named-Theorem cross-references), 12 (ARR full-name), 14 (RCV Sandel-hybrid), 15 (Ch 7 six-pattern Ostrom-path framing) — read to ensure no restoration regresses canonical decisions. |
| Cross-chapter consistency inventory | `tools/audits/cross-chapter-consistency-inventory_2026-05-11.md` | Verified canonical-term register inventory. |
| Terms index | `core/terms/terms_index.md` | Verified Substitutability Function S Title-case + Abundance Masking Title-case + existential substitutability gap lowercase prose phrase. |
| Aeon Version C pitch | `publishing/essays/aeon-mask-of-abundance/_archive/prior-versions/aeon-pitch-commons-bonds-winn_VERSION-C.md` | Read for verbatim-overlap held passage at Ch 7:101 ("structural test the same" + "self-imposed commute lease"). Fire window Sun May 31 14:01 UTC. |
| Memory | `feedback_audience_aware_drafting_discipline.md` v3.1 Amendment B | Pass 3.5 restoration-polarity discipline + explicit-gate per Amendment A two-class cascade. |
| Memory | `feedback_substance_drives_length.md` | Restoration recommendations must add substance, not pad for length. |
| Memory | `feedback_voice_polish_pipeline.md` | Active editorial work expected. |
| Memory | `feedback_verify_stale_memory_claims.md` | Verified chapter line count + commit hashes against origin/main at session start. |
| Memory | `feedback_em_dash_overuse.md` | Restoration recommendations evaluated against em-dash calibration discipline (Pass 3.2 F-V13 HELD em-dash density at chapter-wide level; restorations must not regress that hold). |

### §0.2 Commit verification (all referenced hashes confirmed on `origin/main`)

- `4948dbb` — Ch 7 Pass 3.1 ratification record ✓
- `4987e59` — Ch 7 Phase C-α (7 prose + bibliography spot-fixes) ✓
- `440906f` — Ch 7 Pass 3.2 voice-polish ratification ✓
- `e29d5ae` — Ch 7 Phase C-β (5 Pass-2 voice-polish spot-fixes) ✓ — **latest chapter-file commit**
- `697bcd2` — Ch 7 Pass 3.3 acceptance verdict ratified ✓
- `0a3de00` — Ch 7 Pass 3.3 §8.3 Option A HOLD ✓
- `8c8f1f5` — Ch 7 Pass 3.4 PROPOSED ✓
- `d46a6ae` — Ch 7 Pass 3.4 RATIFIED Option A HOLD (close Stage 3 — initial disposition pre-reconsideration) ✓
- `e1b4d6d` — Ch 7 Stage 4 RATIFIED (author-completed-offline 2026-05-26) ✓ — **stale after Pass 3.5 disposition if any spot-fix ratified** per framing
- `b37aa46` — Ch 7 Stage 5 sign-off + pre-pub review queue ✓ — **stale after Pass 3.5 disposition if any spot-fix ratified** per framing

### §0.3 Chapter-state metadata audited

**Audited state:** Post-Phase-C-β / pre-Phase-C-γ at session start.

**Line count:** 250 lines (matches expected post-Phase-C-β state per framing).

**Phase C-γ application signals checked (per framing detection signals):**
- Line 19 paragraph: contains "the parameter ranges for resource extraction in Martian regolith are extensively measured rather than entirely speculative" — does NOT contain T1's pre-positioned methodological-not-advocacy disclaimer language (T1 would add disclaimer language at the chapter opening). **T1 NOT applied.**
- Line 141 paragraph: contains Bostrom-MacAskill-Ord lineage citation + existing scope-disclaimer ("The framework does not adopt longtermism's specific ethical commitments...") but does NOT contain a "contested-territory" / longtermism-contestation explicit acknowledgment sentence (T4 would add such a sentence). **T4 NOT applied.**
- Line 221 immune-response paragraph: contains existing Ch 9 forward-reference ("Chapter 9, in particular, takes up the design problem this stress test surfaces...") but does NOT contain an explicit Public-Choice tradition forward-reference sentence (T3 would add explicit Public-Choice naming). **T3 NOT applied.**

**Conclusion:** Phase C-γ has not landed in this worktree's chapter file at session start. The auditable state is post-Phase-C-β = 250 lines. Line references in this artifact's findings align with the 250-line state.

**Forward-cadence note:** Per framing, Phase C-γ may merge to origin/main during or after this session in a parallel worktree-isolated session. Phase C-δ session (if any Pass 3.5 spot-fixes ratified) would apply against the then-current chapter state, which may be post-Phase-C-γ at that point (~252-256 lines per framing estimate). This Pass 3.5 audit's findings are stable across the C-γ → C-δ ordering because none of the Pass 3.5 restoration sites identified below overlap with the C-γ application sites (line 19 disclaimer-pre-positioning; line 141 longtermism-acknowledgment; line 221 Public-Choice naming).

### §0.4 Branch discipline note

Per framing + workstream branch-discipline: fresh feature branch `claude/manuscript-stage-3-ch7-pass3-5-agent-a780222e83724b34b` should be opened from current `origin/main`. **Sandbox environment in this session blocked `git checkout -b` / `git switch -c` / `git branch + git checkout` commands** at session start. This artifact is therefore committed on the worktree's default branch `worktree-agent-a780222e83724b34b`. Per CLAUDE.md merge-to-main default for rigor-pass artifacts (extended 2026-05-16): the artifact autonomously fast-forward merges to `main` at session close via the worktree-merge handoff cadence.

---

## §1. Methodology + polarity discipline + author context framing

### §1.1 What this pass IS

The whole-chapter developmental-edit lens at **restoration polarity** (Pass 3.2 cuts, Pass 3.5 restores — different polarities; folding would lose the discipline each needs):

- **Sensory-detail restoration** at the chapter's primary scene (Mars habitat lines 27–47) + comparative-historical scenes (pyramids/Qin lines 213–215) + Mars-resident-visiting-Earth passage (line 127).
- **Scene-anchor density** at the Mars habitat scene + the cross-scenario sweep cases (lines 85–101) where the framework's analytical work runs.
- **Voice-flow continuity** across the chapter's eleven section breaks (lines 25, 51, 79, 105, 133, 157, 177, 205, 225, 237, 247).
- **Reader-engagement at analytical pivots** — universality claim at line 21; running-the-test at line 81; cost-severance-requires at line 107; existential-substitutability-gap at line 137; cross-scenario result at line 161; Mars-is-false-analogy at line 179; framework-across-time + immune-response at line 207; what-comes-next at line 227.
- **Cumulative-LLM-cadence residue cleanup** after Pass 3.2 chiseling (F-V2 line 21 + F-V11 line 229 + F-V17 line 195 applied per Phase C-β; F-V3 + F-V4 + F-V5 + F-V6 + F-V7 + F-V8 + F-V9 + F-V10 + F-V12 + F-V13 held per substance-drives-length). Pass 3.5 reads the post-Phase-C-β state for whether any residual cumulative-cadence pattern surfaces.
- **Apparatus-density rhythm at lines 137–151** (Pass 3.4 §6 carry-forward — existential-substitutability-gap ranking five-paragraph sweep). Reader-engagement at this analytical pivot tested.
- **Objection-response section breath at lines 179–203** (Pass 3.4 §6 carry-forward — Mars-is-false-analogy section length). Section length earns vs over-pads question tested.

### §1.2 What this pass is NOT

- **NOT Pass 3.1 fact-check** — no new facts; Pass 3.1 + Phase C-α canonical input. Two Pass-1 follow-up courtesy-notify items at §5.7 in Pass 3.2 artifact (Hartwick + Stern living-status) remain pre-publication-refresh discipline items; not in Pass 3.5 scope.
- **NOT Pass 3.2 voice-polish** — no per-paragraph LLM-tic findings; polarity is restoration, not further cutting. Pass 3.2 §11 disposition log + apparatus register decisions are canonical input.
- **NOT Pass 3.3 acceptance / Pass 3.4 robustness** — no per-character verdicts re-litigated. Pass 3.3 30 INCLUDE / 0 NEUTRAL / 0 EXCLUDE + Pass 3.4 ROBUST WITH OPTIONAL SPOT-FIXES are honored as canonical input.
- **NOT Stage 4 render-audit** — pipeline-side; author offline (Stage 4 RATIFIED `e1b4d6d`; will require re-ratification if any Pass 3.5 spot-fix applies per framing).
- **NOT Stage 5 sign-off / pre-publication review queue re-litigation** — Stage 5 `b37aa46` carries forward, re-ratifies if any Pass 3.5 spot-fix applies.
- **NOT re-litigation of any LOCKED chapter passage per §6.5 inventory below.**

### §1.3 Reading-pass approach

Three passes through the chapter at whole-chapter scale:

1. **Pass A — Scene-anchor + sensory-detail scan.** Read end-to-end tracking concrete physicality at the Mars habitat (lines 27–47); Mars-resident-visiting-Earth (line 127); comparative-historical scenes (pyramids at line 213, Qin at line 215); and the cross-scenario case-walks (lines 85–101).
2. **Pass B — Reader-engagement at analytical pivots scan.** Read end-to-end tracking whether each pivot (lines 21, 81, 107, 137, 161, 179, 207, 227) gives the reader something to hold onto + invites them into the framework's next move.
3. **Pass C — Apparatus-density rhythm + objection-response breath scan.** Read end-to-end at the Pass 3.4 §6 pre-flagged sites (lines 137–151 existential-substitutability-gap ranking; lines 179–203 Mars-is-false-analogy objection-response).

### §1.4 Author context-for-decisions framing (per author 2026-05-26, verbatim)

> "I have upgraded my account again and running out of tokens is no longer an issue. So now the only constraint is time interacting with you, which I'm trying to maximize via parallel sessions during my summer break from school. So the goal here is make the book as good as possible. period."

Pass 3.5 fires under this lens. Sample-chapter readiness STRONG per workstream handoff line 333; Ch 7 + Ch 5 are sample-chapter pair for agent/publisher queries. Restoration upside that materially strengthens the chapter for that audience is flagged APPLY-recommended; restoration that would over-pad the analytical-thought-experiment register is flagged HOLD-recommended.

### §1.5 Hard constraints honored

- **NO spot-fixes applied to the chapter file in this PROPOSED artifact.** Phase C-δ session applies any ratified spot-fixes after author ratification.
- **NO paragraph re-writes inside the chapter file.** Findings + restoration options only.
- **NO restoration that incidentally varies the Aeon-overlap held passage at Ch 7:101** ("structural test the same" + "self-imposed commute lease"). Verified at §6.4 below.
- **NO modification to Theorem 10.3 (Abundance Masking) cross-reference at Ch 7:121.** Verified at §6.5 below.
- **NO new framework concepts or meta-conclusions about v3.0 / v3.1 discipline.**
- **NO contact with named subjects.**
- **Substance-drives-length governs.** Restoration must add substance — sensory specifics, scene-anchors, reader-engagement, voice-flow improvements — not padding for length.
- **Flag any apparatus regressions, named-subject consent regressions, or Path B contamination** (none surfaced; verified at §6 sub-checks below).

---

## §2. Cross-pass carry-forward items inventory

### §2.1 Pass 3.2 §6 forward-flag items

- **Cumulative anaphora-cluster from F-V2 through F-V12.** Pass 3.2 flagged the cumulative density of cadence patterns (F-V2 line 21 four-fold + F-V3 line 45 five-fold + F-V4 lines 57–63 four-paragraph + F-V5 lines 65+67 paired + F-V6 lines 87+89 paired + F-V7 line 127 seven-fold + F-V8 line 131 six-fold + F-V9 line 217 three-fold + F-V10 line 219 five-fold + F-V11 line 229 five-fold + F-V12 line 235 three-imperative). Pass 3.3 §4.5 resolved at acceptance-character level: cumulative density read as substantively-earned analytical-thesis-cadence rather than LLM-cadence reach. Pass 3.5 verifies cumulative read at whole-chapter scale.
- **Apparatus-density spike** — Pass 3.4 §6 carry-forward; Pass 3.5 scope.
- **Objection-response section length** — Pass 3.4 §6 carry-forward; Pass 3.5 scope.

### §2.2 Pass 3.4 §6 forward-flag items (verbatim from Pass 3.4 §6)

- **Apparatus-density spike at lines 137–151** "is the chapter's analytically-densest passage (Substitutability Function S formal notation + existential-substitutability-gap ranking + Bostrom-MacAskill-Ord lineage citation cluster + helium-3 conditional-category + five-tier resource classification). Pass 3.4 A11 (trade-press editor adversarial mode) flagged this as the chapter's hardest read; Pass 3.5 whole-chapter read should verify reader-engagement at this analytical pivot does not flatten cumulatively when read after the comparable apparatus-density passages at the chapter's earlier scenarios (lines 37–43 Mars-habitat apparatus walk-through; lines 53–77 parameter-walk)."
- **Mars-is-false-analogy section at lines 179–203** "is structurally an objection-and-response section that accumulates three sub-objections back-to-back (Mars-is-false-analogy + Mars-is-thought-experiment + asteroid-iron-reduces-to-market-pricing). Pass 3.4 A1 (Mars-canonization-detractor) + A11 (trade-press editor adversarial) flagged the section's length under hostile read; Pass 3.5 whole-chapter read should verify reader-engagement across the three sub-objections does not produce sequential-objection-fatigue."

Pass 3.4 noted: "Neither incidental observation surfaces a Pass-3.5 gap; both flagged as low-priority Pass 3.5 attention items per Ch 9 Pass 3.4 §6.3 precedent." Pass 3.5 below assesses both.

---

## §3. Findings — HIGH severity

Restoration opportunities that materially strengthen the chapter for sample-chapter audience (agent/publisher query reading; trade-press editor first-read; analytical-thought-experiment register reader).

### F-DE-Ch7-1 — Existential-substitutability-gap ranking (lines 143–151) is the chapter's analytically-densest passage; one or two sentences of grounded substance per resource tier would compound reader-engagement at the analytical pivot without expanding scope (HIGH)

**Lines:** 143–151 (five-paragraph ranking sweep: coal/sand/iron/stone → oil/copper/zinc → uranium/lithium/cobalt → rare earths/PGMs → helium-3).

**Current text (verbatim).** Five paragraphs walking the gap from zero to conditionally-high:

> **Line 143 (coal/sand/iron/stone, zero gap):** "Coal has an existential substitutability gap near zero. Electricity from coal is readily substitutable today; no foreseeable civilizational application requires coal as a specific input. Sand, common iron ore, and common stone are similar — abundant, substitutable, zero existential substitutability gap."
>
> **Line 145 (oil/copper/zinc, low gap):** "Conventional oil, copper, and zinc have low existential substitutability gap. Substitutable for most current applications; no clear civilizational applications that uniquely require them."
>
> **Line 147 (uranium/lithium/cobalt, moderate gap):** "Uranium, lithium, and cobalt have moderate existential substitutability gap. Substitutable for some applications; important strategic roles in specific technologies; future applications plausibly but not certainly dependent on these particular materials."
>
> **Line 149 (rare earths/PGMs, high gap):** "Rare earth elements and platinum group metals have high existential substitutability gap. Their specific magnetic, catalytic, and electronic properties are required for technologies that have not yet been invented but which almost any civilization with advanced manufacturing will need. Substitutes exist for some current applications; no clear path to substitutes for all applications; high probability that at least some future applications cannot be served without them."
>
> **Line 151 (helium-3, conditionally high):** "Helium-3 occupies a unique category — conditionally high existential substitutability gap. If deuterium-helium-3 fusion becomes viable, helium-3 becomes one of the most strategically important resources in the accessible solar system. If it does not, helium-3 is a curiosity. The classification is contingent on a technology that has not yet been demonstrated."

**Issue.** Pass 3.4 §6 pre-identified this five-paragraph sweep as "the chapter's analytically-densest passage" + flagged Pass 3.4 A11 (trade-press editor adversarial mode) recognition of it as "the chapter's hardest read." The ranking does substantial analytical work — establishing the four-tier classification that the chapter then closes (line 153–155) by handing the ranking forward to Ch 9 as the input to renewable-transition policy. The five paragraphs land as **pure classification-by-substitutability-property without concrete examples of what each tier's resources are FOR** — the reader is asked to accept that "rare earth elements and platinum group metals have high existential substitutability gap" via the substitutability-property claim alone, with no anchor for what civilizational application would actually require them.

The chapter has a strong rhetorical asset available here that it does not deploy: the Pass 3.3 + Pass 3.4 acceptance/robustness verdicts hold the ranking as substantively-defensible, but the sample-chapter trade-press reader (agent/publisher first-read; Pass 3.3 char #1) experiences the ranking as five tiers of classification-without-anchor. Restoration polarity recommends one or two sentences of grounded application-naming per tier — what each tier's resources are actually FOR in the civilizational-applications sense — to give the reader something concrete to hold onto at the chapter's densest analytical pivot.

The chapter's existing pattern elsewhere uses concrete-application anchoring: line 87 (helium-3 paragraph in cross-scenario sweep) names "deuterium-helium-3 cycle" + "net energy gain" + "potentially the most important fuel source in the solar system" — substance-anchored claims that the reader can hold onto. Line 95 (Mars rare earths paragraph) names "electronics rather than importing from Earth" + "strategic independence." The chapter knows how to do this. The ranking section at lines 143–151 was likely tightened during voice-polish to match the apparatus-deployment register; restoration polarity recommends adding back the application-anchoring at the tier-level.

**Options:**

- **Option A — Add one application-anchor clause per tier, within the existing paragraph structure.** Insert a clause-level grounding within each of the five paragraphs, naming what the tier's resources are actually FOR at the civilizational-application level. Specific proposed insertions:

  > **Line 143 (coal/sand/iron/stone):** "Coal has an existential substitutability gap near zero. Electricity from coal is readily substitutable today — solar, wind, nuclear, hydro, geothermal, and natural-gas generation are all available alternatives for the same kilowatt-hour — and no foreseeable civilizational application requires coal as a specific input. Sand, common iron ore, and common stone are similar — abundant, substitutable, zero existential substitutability gap."
  >
  > **Line 145 (oil/copper/zinc):** "Conventional oil, copper, and zinc have low existential substitutability gap. Substitutable for most current applications — oil for transport fuel and feedstock, copper for conductive wiring and plumbing, zinc for galvanization and battery chemistries — with no clear civilizational applications that uniquely require them."
  >
  > **Line 147 (uranium/lithium/cobalt):** "Uranium, lithium, and cobalt have moderate existential substitutability gap. Substitutable for some applications (uranium for fission baseload where thorium fuel cycles or eventual fusion offer alternatives; lithium for battery chemistries where sodium-ion + solid-state research is advancing; cobalt for high-density cathodes where iron-phosphate chemistries are gaining); important strategic roles in specific technologies; future applications plausibly but not certainly dependent on these particular materials."
  >
  > **Line 149 (rare earths/PGMs):** "Rare earth elements and platinum group metals have high existential substitutability gap. Their specific magnetic, catalytic, and electronic properties are required for technologies that have not yet been invented but which almost any civilization with advanced manufacturing will need — the neodymium and dysprosium that make permanent-magnet motors possible at usable energy densities, the platinum and palladium that catalyze hydrogen-fuel-cell and electrolyzer chemistries, the gallium and germanium and indium that enable the semiconductor architectures of next-generation computing. Substitutes exist for some current applications; no clear path to substitutes for all applications; high probability that at least some future applications cannot be served without them."
  >
  > **Line 151 (helium-3):** [Already substantively-grounded; no insertion proposed. The existing "If deuterium-helium-3 fusion becomes viable, helium-3 becomes one of the most strategically important resources in the accessible solar system" gives the reader what they need.]

  Net addition: ~80 words across four paragraphs (~20 words per tier average); ranking length grows from ~210 words to ~290 words. Substance-anchored grounding-per-tier; preserves the four-tier classification structure; gives the analytically-densest passage concrete civilizational-application anchors for reader engagement.

- **Option B — Add a single bridging paragraph BEFORE the ranking begins, naming what makes the four-tier classification matter at the civilizational-application level.** Insert a new paragraph between line 141 (the Bostrom-lineage citation paragraph) and line 143 (where the ranking begins):

  > "The applications that matter for the ranking are not all visible from current industrial uses. Permanent-magnet motors, hydrogen-fuel-cell electrolyzers, photovoltaic and thermoelectric semiconductor architectures, advanced battery chemistries, biomedical imaging contrast agents, satellite communications, the next-generation of computing — each depends on a specific subset of the periodic table for its operation, and the substitutability question is whether a different element or compound could perform the same physical function. For most current industrial inputs the answer is yes. For some specific magnetic, catalytic, electronic, and optical functions, the answer is genuinely uncertain, and the ranking that follows is an attempt to be honest about that uncertainty rather than to elide it."

  Net addition: ~85 words single paragraph; preserves the existing five-paragraph ranking unchanged; reader enters the ranking with the civilizational-application anchor primed.

- **Option C — Hold-as-is.** The ranking operates at apparatus-deployment register; the chapter's framework-architecture work is the substantive load-bearing claim; sample-chapter trade-press readers tracked the ranking to its analytical purpose per Pass 3.3 + Pass 3.4 verdicts; restoration risks adding length without compounding substance.

**Recommendation: Option A** (one application-anchor clause per tier, within existing paragraph structure).

**Reasoning.**

- **Materially strengthens the chapter's analytically-densest passage at sample-chapter-read level.** Pass 3.4 §6 explicit pre-identification + Pass 3.4 A11 trade-press editor adversarial flag identify this as the chapter's hardest read. Restoration polarity (3.5 restores; 3.2 cuts) is precisely designed to surface this kind of opportunity. Author context-framing ("make the book as good as possible") justifies the additional ~80 words when each word does grounded-substance work.
- **Substance-drives-length honored.** The insertions are application-anchor specifics (solar/wind/nuclear/etc.; oil for transport fuel and feedstock; uranium-thorium-fusion fuel-cycle alternatives; neodymium-dysprosium permanent-magnet motors; platinum-palladium fuel-cell catalysts; gallium-germanium-indium semiconductor architectures), not padding. Each phrase names a concrete civilizational application that the ranking-tier's substitutability claim is anchored against. Per [feedback_substance_drives_length.md](../memory/feedback_substance_drives_length.md): restoration earns its space.
- **Respects apparatus register.** No new framework concepts; no Greek letters or formal apparatus; no scaffolding vocabulary. The application-anchors operate at plain-prose register the chapter's surrounding paragraphs already use (line 87 helium-3 + line 95 Mars rare earths). Per Pass 3.2 §5.3 apparatus discipline: clean.
- **Preserves five-paragraph classification structure.** The four-tier ranking + helium-3 special category architecture is preserved; insertions sit within existing paragraphs as clause-level grounding rather than new paragraphs.
- **Coordinated with Ch 9 forward-handoff at line 155.** Line 155 hands the ranking forward to Ch 9 as the input to renewable-transition policy with the specific resources named (rare earths, platinum-group metals, cobalt, nickel) + the specific applications (motors, magnets, electrolyzers, fuel cells, battery cathodes). The restoration at lines 143–149 makes the ranking's individual tiers carry the same application-anchored register the chapter-close already uses — compounds the line-155 handoff rather than contradicting it.
- **Em-dash density check.** Option A adds 5 em-dashes across four paragraphs (line 143: 1; line 145: 1; line 147: 0 [parens used]; line 149: 1 [extended substance dash]). Chapter currently has ~25-30 single em-dashes + multiple paired em-dashes per Pass 3.2 F-V13; net addition ~5 em-dashes across the chapter is incremental and each new em-dash does grounded-substance work (no connective-tissue crutch). Per [feedback_em_dash_overuse.md](../memory/feedback_em_dash_overuse.md): each new em-dash earns its use.
- **Pass 3.4 §6 closure.** Restoration closes the apparatus-density-spike flag at the level Pass 3.4 §6 anticipated. Pass 3.5 explicit-gate trigger by author IS the disposition mechanism for the flag.
- **Pass 3.3 / Pass 3.4 verdict-impact** (per §4 below): no INCLUDE → NEUTRAL / EXCLUDE shifts at any acceptance character; three acceptance characters (Char 1 trade-press; Char 13 cost-bearer-adjacent; Char 14 left-progressive natural-fit) trend strengthened; no adversarial threads re-opened.

**Author-revisit candidate?** **No.** Agent-fillable per the chapter's established application-anchor register (line 87 helium-3 + line 95 Mars rare earths + line 155 Ch 9 forward-handoff are existing format precedents). The civilizational-application examples (permanent-magnet motors / hydrogen-fuel-cell electrolyzers / semiconductor architectures / etc.) are public-record technical-knowledge anchors — no author-specific voice / lived-experience / judgment required. **However:** author judgment is required on whether to take Option A (in-paragraph anchoring) vs Option B (bridging paragraph) vs Option C (hold). Recommended Option A.

---

## §4. Findings — MEDIUM severity

Substantive restoration upside; author judgment.

### F-DE-Ch7-2 — Mars habitat scene (lines 27–47) opens with strong analytical-procedural anchoring but the inhabitants themselves are visible only as abstract administrator + abstract "ten thousand people"; one or two beats of inhabitant-bodily-presence would strengthen the scene's analytical claim by grounding it in the population whose survival is at stake (MEDIUM)

**Lines:** 27–47 (the chapter's primary scene — Mars habitat with 10,000 inhabitants; trading consortium request; framework walkthrough term-by-term).

**Current text (key passages).**

- **Line 27 (scene establishment):** "The habitat houses ten thousand people. It is established, self-sustaining, several decades into its existence. It relies on three known subsurface water ice deposits accessible from its habitation zone. At current consumption — drinking, agriculture, oxygen production through electrolysis, industrial processing — the deposits represent roughly a fifty-year supply. The administrator of the habitat's resources has been asked by a trading consortium for permission to accelerate extraction."
- **Line 33 (administrator's analytical-procedural framing):** "She is not, in her situation, burdened by the philosophical debates that have structured terrestrial resource economics for a century. She is not wondering about the social cost of carbon or the appropriate discount rate for intergenerational transfers. She is wondering whether it is acceptable to reduce her habitat's remaining water supply by sixty percent in exchange for a financial return to a specific extraction consortium over the next decade. She knows what happens to a habitat that runs out of water."

**Issue.** The Mars habitat scene is the chapter's primary scene — the thought-experiment's central anchor against which the framework's universality claim is tested. The scene operates at strong analytical-procedural register: the administrator's reasoning is foregrounded; the framework walkthrough is clear; the trade-off (50-year → 20-year horizon) is concrete. But the 10,000 inhabitants — whose survival is the load-bearing stake — are visible to the reader as an abstract demographic count rather than as embodied population. The administrator herself appears as a procedurally-deliberating reasoner; her bodily presence (does she have family? children whose air she's calculating?) is not in the scene. The "trading consortium" appears as an institutional actor without representatives whose faces the administrator has to negotiate across.

The chapter's analytical-thought-experiment register is appropriately bounded against scene-anchor density — this is not a memoir chapter. But Pass 3.5 restoration-polarity asks whether one or two specific sensory or relational beats would strengthen the scene's analytical claim by grounding the framework walkthrough in the population whose survival is at stake. The Pass 3.5 question is not whether to convert the scene into a novelistic scene — it is whether the analytical register over-suppresses the bodily reality of the trade-off being analytically computed.

**Options:**

- **Option A — Add one inhabitant-bodily-presence beat at line 33 (administrator's analytical reasoning) connecting the abstract-demographic to lived-population stakes.** Insert one sentence within the existing paragraph, after the existing "She knows what happens to a habitat that runs out of water" sentence:

  > "She is not, in her situation, burdened by the philosophical debates that have structured terrestrial resource economics for a century. She is not wondering about the social cost of carbon or the appropriate discount rate for intergenerational transfers. She is wondering whether it is acceptable to reduce her habitat's remaining water supply by sixty percent in exchange for a financial return to a specific extraction consortium over the next decade. She knows what happens to a habitat that runs out of water. **Her grandchildren will be among the inhabitants the math is being done for; the habitat's kindergarten classroom is two corridors from her office; the agricultural domes she walks past on her way to the consortium meeting are the same domes the inhabitants will or will not be able to keep watered in thirty years.** She also knows that the consortium, having captured its return, will be operating under somewhat different incentives thirty years from now."

  Net addition: ~50 words single sentence (three clauses); preserves the existing paragraph structure; grounds the abstract-demographic + abstract-administrator in lived-population stakes via specific physicality (grandchildren / kindergarten classroom / agricultural domes); respects substance-drives-length (each clause names a specific anchor that does scene-grounding work).

- **Option B — Add one trading consortium-representative beat at line 29 or line 47** connecting the abstract institutional actor to embodied representatives:

  > **Line 29 (consortium request):** "...has been asked by a trading consortium for permission to accelerate extraction. **The consortium's representatives, who travel out from the Earth-orbit logistics hubs twice a Mars-year, present the request as straightforward business — quarterly returns documented, contract horizons modeled, exit clauses standard.** The request is profitable in the near term..."

  Net addition: ~35 words; grounds the consortium as embodied institutional actor; gives the negotiation a relational contour.

- **Option C — Both A + B.** ~85 words total restoration across the Mars habitat scene; strongest scene-grounding effect; longest addition.

- **Option D — Hold-as-is.** The analytical-thought-experiment register Steps 1-4 of the framework walkthrough require sparse scene-anchoring; the abstract demographic + abstract administrator are structural features of the thought-experiment register; bodily-presence beats risk softening the analytical register that the chapter's universality claim depends on.

**Recommendation: Option A** (one inhabitant-bodily-presence beat at line 33).

**Reasoning.**

- **Materially strengthens the chapter's primary scene at sample-chapter-read level.** The Mars habitat scene is the chapter's central anchor; restoration that grounds the abstract demographic in lived-population stakes compounds the framework walkthrough's analytical force rather than diluting it. The framework walkthrough at lines 37–43 (substitutability / stock-dependent utility / externality tail / discount factor) computes life-or-death tradeoffs; the reader's experience of those tradeoffs deepens when the population being analyzed has bodily presence in the scene.
- **Substance-drives-length honored.** The 50-word insertion names three specific physical anchors (grandchildren among inhabitants; kindergarten classroom two corridors from office; agricultural domes she walks past) — none is padding; each does scene-grounding work that the analytical paragraphs depend on. Per [feedback_substance_drives_length.md](../memory/feedback_substance_drives_length.md): restoration earns its space.
- **Respects analytical-thought-experiment register bounds.** The bodily-presence beat sits within the administrator's analytical reasoning paragraph (line 33) — not in a new paragraph or section break. The framework walkthrough at lines 37–43 follows immediately; the administrator's analytical work resumes without interruption. The beat compounds the analytical register by grounding the deliberation in physical stakes rather than replacing the analytical register with novelistic scene.
- **Honors the discount-factor analytical claim at line 43.** The chapter's discount-factor paragraph at line 43 says: "the future is not a discountable abstraction; it is the same population's own next decade of continued existence." The bodily-presence beat at line 33 ("Her grandchildren will be among the inhabitants the math is being done for...") makes that claim load-bearing for the reader rather than asking the reader to accept it from the analytical paragraph alone.
- **Pronoun discipline preserved.** Mars administrator she/her pronoun chain at lines 27–47 (per Pass 3.2 §5.7 ✓ HOLDS) is preserved by the insertion (she-pronouns: "Her grandchildren," "her office").
- **No named-subject consent concern.** The administrator is an explicitly-composite character (Pass 3.2 §5.1); "her grandchildren" / "the kindergarten" / "the agricultural domes" are scene-anchor specifics within the thought-experiment fiction, not references to real individuals.
- **Option B (consortium-representative beat) marginally weaker.** The consortium is more analytically functional as institutional actor (the abstract trading consortium represents the framework's counterparty class); embodying the consortium's representatives risks introducing a relational-dynamic the chapter does not return to. Option A is the lighter-touch restoration with stronger payoff at the scene's analytical pivot.
- **Pass 3.3 / Pass 3.4 verdict-impact** (per §4 below): no INCLUDE → NEUTRAL / EXCLUDE shifts; Char 1 trade-press marginally strengthened (concrete-anchor at primary scene); Char 13 cost-bearer-adjacent + Char 18 EJ-movement-adjacent marginally strengthened (population whose survival is at stake has bodily presence rather than abstract demographic); adversarial A1 Mars-canonization-detractor unchanged (Option A does not advocate Mars; it grounds the thought-experiment scene whose framework-discipline the chapter establishes).

**Author-revisit candidate?** **Possibly.** The specific bodily-presence anchors (grandchildren / kindergarten / agricultural domes) are agent-constructable per the chapter's established thought-experiment scene-anchor register, but author may have a richer or more specific anchor in mind that draws on the author's own analytical sense of what makes the Mars habitat scene's stakes most legible. Flagged for author preference at Phase C-δ ratification.

---

### F-DE-Ch7-3 — Mars-resident-visiting-Earth seven-fold "Free X" passage (line 127) is substantively-earned per Pass 3.2 F-V7 HELD but could compound reader-engagement at the analytical pivot via one closing-paragraph beat naming what the Mars resident would actually do with the realization (MEDIUM)

**Line:** 127 (the chapter's most visible cumulative-anaphora cluster — seven-fold "Free X" enumeration of ambient-abundance Earth provides).

**Current text (excerpt, verbatim, line 127).**

> "Severance is therefore not impossible on Mars. It is impossible to *hide*. The administrator who under-prices for short-term gain still produces severance against future-self and future-population — but the closed feedback loop makes the cost visible immediately, and the framework's logic requires that what is visible be priced. What Mars exposes by removing concealment is not just the scarcity of specific resources but the entire ambient abundance Earth provides. A Mars resident visiting Earth wouldn't see Earth as a place with abundant resources. They'd see free air. Free water falling from the sky on a regular schedule. Free temperature regulation. Free solar irradiance, continuously and without maintenance. Free gravitational stability provided by the Moon, including the tidal cycle that drives nutrient circulation through the oceans. Free magnetic-field shielding against radiation that would otherwise strip the atmosphere. Free atmospheric filtering of ultraviolet wavelengths that would otherwise sterilize the surface. All the conditions Earth provides as ambient — the conditions a closed-habitat resident would calculate maintenance budgets for. Earth's ambient abundance is the dominant cost-hiding apparatus on this planet, and the framework's Commons Inversion Test is the tool for detecting which parts of it are actually finite-and-being-drawn-down."

**Issue.** The seven-fold "Free X" enumeration is the chapter's most rhetorically-vivid Mars-perspective-on-Earth move. Pass 3.2 F-V7 explicitly held the seven-fold anaphora as substantively-earned (each "Free X" names a distinct ambient cost-hiding apparatus; length-variance softens the strict cadence; substance-drives-length governs). Pass 3.3 + Pass 3.4 acceptance/robustness verdicts confirmed the passage works for sample-chapter readers.

The Pass 3.5 question is downstream of the seven-fold itself: after the rhetorical-peak of the seven-fold enumeration, the closing two sentences ("All the conditions Earth provides as ambient — the conditions a closed-habitat resident would calculate maintenance budgets for. Earth's ambient abundance is the dominant cost-hiding apparatus on this planet, and the framework's Commons Inversion Test is the tool for detecting which parts of it are actually finite-and-being-drawn-down.") return the passage to the framework's analytical claim quickly. The Mars-resident perspective is opened, rhetorically deployed, and then closed without the reader being shown what the Mars resident would actually DO with the realization — i.e., what behavioral or analytical move the perspective enables.

Restoration polarity asks whether one additional sentence connecting the Mars-resident's perspective to a specific analytical or behavioral move would compound the rhetorical-peak's reader-engagement. The chapter's existing pattern elsewhere connects perspective-shifts to analytical moves: line 49 ("Any thoughtful administrator of any inhabited place on any world would recognize this as obviously correct. That is exactly the point.") connects the Mars-habitat reasoning to its universal-recognition claim; line 75 ("Every parameter that drove the Mars administrator's decision exists on Earth. The values are different. The structure is the same.") connects the Mars-vs-Earth parameter-comparison to the universality claim.

**Options:**

- **Option A — Add one connecting sentence between "Free atmospheric filtering..." and "All the conditions Earth provides as ambient" naming what the Mars-resident's perspective enables analytically.** Insert one sentence:

  > "...Free atmospheric filtering of ultraviolet wavelengths that would otherwise sterilize the surface. **The Mars resident's accounting habit — the disciplined practice of computing maintenance budgets for every cubic meter of habitat air — would render visible the same finite-and-being-drawn-down dimension Earth's residents are positioned by their abundance to overlook.** All the conditions Earth provides as ambient — the conditions a closed-habitat resident would calculate maintenance budgets for. Earth's ambient abundance is the dominant cost-hiding apparatus on this planet, and the framework's Commons Inversion Test is the tool for detecting which parts of it are actually finite-and-being-drawn-down."

  Net addition: ~40 words single sentence; preserves the seven-fold enumeration unchanged; preserves the existing two-sentence close; adds a bridging sentence that names what the Mars-resident's accounting-habit enables (the rendering-visible move that the framework's Commons Inversion Test then operationalizes).

- **Option B — Hold-as-is.** The seven-fold "Free X" enumeration is substantively-earned (Pass 3.2 F-V7 held); the existing two-sentence close returns the passage to analytical claim at appropriate speed; the chapter's universality argument does not require the additional connecting sentence; the line 127 paragraph already runs ~210 words and Pass 3.4 §6 did not flag it for length.

**Recommendation: Option B (hold-as-is).**

**Reasoning.**

- **The seven-fold enumeration is rhetorically self-sufficient.** Pass 3.2 F-V7 held the seven-fold as substantively-earned ambient-abundance demonstration; the rhetorical peak does its work; adding a bridging sentence after the seven-fold risks over-explaining what the reader has just experienced.
- **The existing close already names the framework's analytical move.** "...the framework's Commons Inversion Test is the tool for detecting which parts of it are actually finite-and-being-drawn-down" — the existing close at the line 127 paragraph's final sentence already does the work Option A's bridging sentence would do. Option A's restoration would be partially redundant with the existing analytical close.
- **Substance-drives-length default.** Per [feedback_substance_drives_length.md](../memory/feedback_substance_drives_length.md): restoration that does not add new substance (vs over-explaining substance already in the prose) does not earn its space. Option A's substance overlaps with the existing close.
- **Author judgment if desired.** If author prefers the explicit bridging — particularly for a reader who might miss the implicit connection between Mars-resident accounting and framework's Commons Inversion Test — Option A is available and bounded.

**Author-revisit candidate?** **No.** Both options are agent-decidable per the chapter's established analytical-close discipline; the recommendation defaults to HOLD per substance-drives-length.

---

### F-DE-Ch7-4 — Mars-is-false-analogy section (lines 179–203) carries three objection-response cycles back-to-back; the second-to-third transition at line 193 is the section's weakest reader-engagement moment; one transitional beat would strengthen objection-response pacing without expanding scope (MEDIUM)

**Lines:** 179–203 (the Mars-is-false-analogy section — three back-to-back objection-and-response cycles per Pass 3.4 §6 carry-forward).

**Current text (transition site, lines 191–193).**

> **Line 191 (close of first objection-response, frictionless-plane defense):** "This is how physics uses frictionless planes and thermodynamics uses perfect insulators — not because the world contains such things, but because the limiting case exposes the underlying law. The law, once exposed, applies in the messy real world with the appropriate adjustments for friction and leakage. The Mars administrator's water ice problem is the frictionless plane of resource economics. The principles it reveals apply, imperfectly, messily, with all the real-world noise Earth provides, to every extraction decision that has ever been made on this planet."
>
> **Line 193 (opening of second objection, Mars-is-thought-experiment):** "A different reader will object on different grounds. Mars is a thought experiment. There is no actual habitat, no administrator, no consortium, no decision pending in 2026. The entire scenario is, in the dismissive sense of the word, science fiction. Importing fictional scenarios into a serious argument about resource economics, this reader will say, is a category error."

**Issue.** Pass 3.4 §6 pre-identified the Mars-is-false-analogy section (lines 179–203) as the chapter's most-loaded objection-response sequence — three sub-objections back-to-back (false-analogy → thought-experiment → asteroid-iron-reduces-to-market-pricing) flagged by Pass 3.4 A1 (Mars-canonization-detractor) + A11 (trade-press editor adversarial) for length under hostile read. The section's substantive content earns its length (each sub-objection is real; each response is substantive), but reader-engagement across the three cycles depends on transitions that don't read as objection-response-fatigue.

The first-to-second transition at lines 191–193 is the section's most abrupt: line 191 closes with the frictionless-plane defense (a satisfying analytical close) + line 193 opens immediately with "A different reader will object on different grounds" — no breath between the close-of-defense and the new-objection-launch. The first-to-second cycle is the section's hinge point: the reader has just absorbed the frictionless-plane defense and is being asked to engage another objection without acknowledgment of the cumulative argumentative weight.

The chapter's existing pattern elsewhere uses transitional breath at objection-pivots: line 185 ("The objection is legitimate and deserves a specific response.") gives the first-objection a breath-beat before the response; line 199 ("A reader should be careful here. This argument is methodological, not advocational.") gives the methodology-not-advocacy disclaimer a breath-beat. The first-to-second transition at lines 191–193 is the section's only objection-pivot without a transitional breath.

**Options:**

- **Option A — Add one transitional sentence at line 193 acknowledging the cumulative weight before launching the second objection.** Insert one sentence:

  > "...The principles it reveals apply, imperfectly, messily, with all the real-world noise Earth provides, to every extraction decision that has ever been made on this planet."
  >
  > **"A second objection, distinct from the first but cumulative with it in the careful reader's growing sense that something is being asked of them, takes the Mars scenario itself rather than the analogy as its target."**
  >
  > "A different reader will object on different grounds. Mars is a thought experiment..."

  Wait — the recommendation needs refinement. A single bridging sentence at the section-internal transition (between the close of the first response at line 191 and the opening of the second objection at line 193) would carry the transitional breath without expanding the section's scope. Specifically:

  > "...The principles it reveals apply, imperfectly, messily, with all the real-world noise Earth provides, to every extraction decision that has ever been made on this planet. **The frictionless-plane defense settles one objection; another follows from a different direction.**
  >
  > A different reader will object on different grounds..."

  Net addition: ~13 words single sentence; sits at the line 191 → line 193 transition; gives the second-objection-launch a transitional beat; respects the chapter's existing objection-pivot pacing.

- **Option B — Re-paragraph the section at lines 191–193 with a dedicated transition paragraph.** Convert the close of line 191 + the opening of line 193 into a brief stand-alone transition paragraph:

  > **(After existing line 191 close):** **"That settles the first objection. A second follows."**
  >
  > **(Existing line 193 opening continues):** "A different reader will object on different grounds..."

  Net addition: ~7 words two-sentence micro-paragraph; sharper transitional pivot; structurally distinct from Option A's in-line restoration.

- **Option C — Hold-as-is.** The section's three-cycle structure is substantively load-bearing; the first-to-second transition at lines 191–193 has not surfaced as a Pass 3.3 acceptance concern; Pass 3.4 §6 flagged the section but rated it as low-priority Pass-3.5-attention; the chapter's analytical-thought-experiment register tolerates the abrupt objection-pivot.

**Recommendation: Option A** (single bridging sentence at the transition).

**Reasoning.**

- **Materially strengthens objection-response pacing at the section's hinge point.** Pass 3.4 §6 pre-identification + the cumulative argumentative weight of the three back-to-back cycles together motivate a light-touch transitional breath. The single-sentence insertion does not expand the section's scope but does give the reader's engagement-trajectory a moment to consolidate before the second objection lands.
- **Substance-drives-length honored.** The 13-word insertion is purely transitional (no new substance; explicit acknowledgment of the cumulative argumentative weight); the question is whether the bare transition earns its words. Per [feedback_substance_drives_length.md](../memory/feedback_substance_drives_length.md): the transition is short, does specific reader-engagement work that the bare "A different reader will object..." launch does not, and is bounded.
- **Preserves objection-response structural integrity.** The three sub-objections remain (false-analogy + thought-experiment + asteroid-iron-reduces-to-market-pricing); the responses to each remain; the section's substantive content is unchanged.
- **Option B (dedicated transition paragraph) marginally weaker.** Two-sentence micro-paragraph creates visible structural break that emphasizes the transition; Option A's in-line bridging sentence is lighter-touch and reads more continuously with the existing prose.
- **Pass 3.3 / Pass 3.4 verdict-impact** (per §4 below): no INCLUDE → NEUTRAL / EXCLUDE shifts; A1 Mars-canonization-detractor + A11 trade-press editor adversarial threads marginally tightened (transitional breath partially absorbs the objection-response-fatigue concern); Char 1 trade-press acceptance strengthened.

**Author-revisit candidate?** **No.** Agent-fillable per the chapter's existing objection-pivot transition register; the bare transitional bridge is bounded.

---

## §5. Findings — LOW severity / style preferences

Light restoration / polish; default hold across the LOW set.

### F-DE-Ch7-5 — Pyramids/Qin comparative-historical passage (lines 213–215) lands strong historical-scene-anchor at the pyramids paragraph but the Qin paragraph operates more abstractly than the pyramids paragraph; light restoration would balance the two scenes (LOW)

**Lines:** 213 (pyramids paragraph) + 215 (Qin paragraph), in the framework-across-time section at lines 211–219.

**Current text (excerpts, verbatim).**

- **Line 213 (pyramids — scene-anchored):** "The pyramids at Giza were built, over a period of roughly seventy years in the Egyptian Old Kingdom around 2550 BCE, by a workforce of skilled craftsmen and conscripted rotational laborers drawn from the agricultural population. The archaeological consensus that emerged from Mark Lehner's Giza Plateau Mapping Project and Zahi Hawass's workers' cemetery excavations has substantially revised the older Herodotean image of chattel slavery under the lash: the workers were paid in rations, medically cared for, and properly buried. They were not slaves in the plantation-economy sense. They were also not free in any sense a modern reader would recognize..."
- **Line 215 (Qin — more abstract):** "Twenty-three hundred years later, on the other side of the world, Qin Shi Huang unified the warring states into the first centralized Chinese empire and commissioned two construction projects whose remains are also still visible: the initial unified Great Wall, spanning five thousand kilometers of northern frontier, and his own mausoleum complex near modern Xi'an, of which the Terracotta Army discovered in 1974 is one fragment. Sima Qian's *Records of the Grand Historian*, compiled approximately a century after the Qin's fall, reports that the Wall was built by three to five hundred thousand concurrent conscripted laborers drawn from peasants, prisoners, and convicts, with documented mass mortality; the mausoleum employed by his estimate upwards of seven hundred thousand..."

**Issue.** The pyramids paragraph (line 213) has strong historical-scene-anchor: Mark Lehner's archaeological project + Zahi Hawass's workers' cemetery excavations + the substantive revision of the Herodotean image. The Qin paragraph (line 215) names Sima Qian + the Wall's length + worker counts + the mausoleum + Terracotta Army discovery — but operates more at scale-and-count register than at archaeological-scene register. The asymmetry is minor (each paragraph does its substantive work) but the two paragraphs together carry the chapter's "mechanism finds whatever ideology" demonstration, and visual rebalancing the Qin paragraph's scene-anchor density slightly toward the pyramids paragraph's would tighten the cross-civilization parallel.

The chapter's existing Qin paragraph already names the legalist philosophy + specific mortality + four-year collapse — substantive historical anchoring. Restoration polarity asks whether one additional scene-anchor (e.g., a specific archaeological detail; the Terracotta Army's discovery context; the Wall's specific construction method) would deepen the parallel.

**Options:**

- **Option A — Add one scene-anchor detail to the Qin paragraph.** Possible insertions: the rammed-earth construction technique of the original Qin Wall; the discovery-year context of the Terracotta Army (farmer digging a well in 1974, near Xi'an); the specific physical scale of the mausoleum site (~56 sq km tomb complex).
- **Option B — Hold-as-is.** The Qin paragraph operates at appropriate-for-section scene-anchor density; the cross-civilization parallel is substantively load-bearing; adding more anchor risks expanding the framework-across-time section beyond what the universality argument needs.

**Recommendation: Option B (hold-as-is).**

**Reasoning.** The pyramids vs Qin asymmetry is minor; both paragraphs do their substantive work; the framework-across-time section is appropriately bounded at ~80 lines (lines 211–223); restoration would expand without compounding the universality argument. The Pass 3.2 §5.7 named-subject register check verified both Mark Lehner + Zahi Hawass + Sima Qian as appropriately cited (Lehner + Hawass living public-intellectual on-record published work; Sima Qian historical-record). The pyramids paragraph's strength is not a defect of the Qin paragraph; the asymmetry is balance, not gap.

**Author-revisit candidate?** **No.**

---

### F-DE-Ch7-6 — Self-imposed commute lease passage (line 101) is LOCKED per Aeon overlap MEDIUM-8 disposition — restoration NOT proposed (LOW informational)

**Line:** 101 (commute-lease paragraph; Aeon-overlap held passage per Pass 3.1 MEDIUM-8 + Pass 3.2 §5.8 honored).

**Status.** Per session hard constraint: "Do NOT propose restorations that incidentally vary the Aeon-overlap held passage at Ch 7:101." Pass 3.5 verified the held passage at line 101 contains the verbatim phrases "structural test the same" and "self-imposed commute lease" in their canonical Aeon-overlap form. **No restoration proposed for this passage.** The passage is LOCKED until after Sun May 31 14:01 UTC Aeon fire window has fired + author re-disposes the MEDIUM-8 hold.

If the reader experience at the line 101 commute-lease passage carries any restoration warrant from Pass 3.5 reading, the disposition belongs to a post-Aeon-fire Phase B re-audit, not this session.

**Recommendation: HOLD per session hard constraint.** No author-action required this session.

---

## §6. Apparatus / consistency / Aeon-overlap sub-checks

Pass 3.5 verifies post-Phase-C-β apparatus state holds + flags any regression. Per [tools/quality-gates/scaffolding-patterns.yaml](../quality-gates/scaffolding-patterns.yaml) + apparatus register canonical decisions + Aeon-overlap discipline.

### §6.1 Apparatus residue check — CLEAN ✓

Per Pass 3.2 §5.3 + Pass 3.4 §5.1 + §5.2 post-Phase-C-β state. Verified:

- **Lowercase prose discipline:** cost severance / residual commons value / externality tail / stock-dependent utility / foreclosure cost — all lowercase ✓
- **Title-case framework terms:** Asymmetric Regret Rule (full name, lines 87 + 93); Commons Inversion Test (full name, lines 101, 121, 127); Substitutability Function S (formal-apparatus deployment line 139); Abundance Masking (Title-case at bolded definition heading line 121 per Pass 3.2 §5.3 Option C ratification; Theorem 10.3 cross-reference line 121 per Item 10) ✓
- **No Greek letters / subscripts / integrals in body prose** ✓
- **No CIT / ARR acronym appearances in body prose** (Item 7 + Item 12 discipline) ✓
- **RCV first-occurrence (RCV) parenthetical at line 85** per Pass 3.2 §5.3 Option A ratification ✓
- **Six bolded pattern-name enumeration (lines 111–121)** post-Item 15 light-de-formalize ✓ HOLDS (no enumeration-marker regression; "illustrative, not exhaustive" framing intact)
- **Bostrom-MacAskill-Ord lineage citation at line 141** ✓ satisfied (all four canonical citations present per Insight #33 + terms_index requirement)
- **Italicization discipline:** *existential substitutability gap* italicized first-introduction line 139 ✓; book titles italicized at lines 141 + 215 ✓; term-emphasis italics at line 123 defense paragraph ✓

**Restoration proposals (F-DE-Ch7-1 + F-DE-Ch7-2 + F-DE-Ch7-4) verified against apparatus discipline:**
- F-DE-Ch7-1 application-anchor clauses use plain-prose lowercase register; no apparatus terms introduced; no Greek letters or formal apparatus deployed; clean.
- F-DE-Ch7-2 bodily-presence beat uses Mars-administrator she/her pronouns consistent with Pass 3.2 §5.7 pronoun discipline; no apparatus terms introduced; clean.
- F-DE-Ch7-4 transitional bridge uses plain-prose register; no apparatus terms introduced; clean.

Verdict: **CLEAN.** No apparatus regression. Restoration proposals respect apparatus register canonical decisions.

### §6.2 Cumulative-LLM-cadence residue check — ✓ NONE surfaced

Per Pass 3.2 chiseling (F-V2 + F-V11 + F-V17 applied; F-V3 + F-V4 + F-V5 + F-V6 + F-V7 + F-V8 + F-V9 + F-V10 + F-V12 + F-V13 held per substance-drives-length) + Pass 3.3 §4.5 cumulative-density acceptance-character verdict. Whole-chapter reading of post-Phase-C-β state surfaces no residual cumulative-cadence pattern beyond what Pass 3.2 + Pass 3.3 already disposed.

Restoration proposals do not re-introduce cumulative-cadence patterns:
- F-DE-Ch7-1 application-anchor clauses are clause-level grounding within existing paragraphs; not cross-sentence anaphora.
- F-DE-Ch7-2 bodily-presence beat is single sentence (three-clause) within existing paragraph; not cross-paragraph anaphora.
- F-DE-Ch7-4 transitional bridge is single sentence; not anaphoric.

Verdict: **CLEAN.** No new cadence-pattern introduced.

### §6.3 Voice-flow continuity — ✓ HOLDS

Eleven section breaks (lines 25, 51, 79, 105, 133, 157, 177, 205, 225, 237, 247). Reading-pass continuity across each break verified per Pass 3.2 §5.1 register-consistency: analytical-thought-experiment → cross-scenario-sweep → cost-severance-mechanism → existential-substitutability-gap-ranking → cross-scenario-result table → objection-response → framework-across-time → what-comes-next → numbers-behind-the-thought-experiment closing notes. Each break scene-cued by `###` subsection header + `---` separator + substantive-pivot opening sentence. No abrupt transitions surfaced.

Restoration proposals respect section-break structure:
- F-DE-Ch7-1 sits within "Not all resources matter equally" section (lines 135–155); preserved.
- F-DE-Ch7-2 sits within "The habitat" section (lines 27–49); preserved.
- F-DE-Ch7-4 sits within "Mars is a false analogy" section (lines 179–203); preserved.

Verdict: **HOLDS.**

### §6.4 Aeon-overlap held passage at Ch 7:101 — ✓ HONORED

Per session hard constraint + Pass 3.1 MEDIUM-8 hold + Pass 3.2 §5.8 honored + Pass 3.3 verdict-ratification + Pass 3.4 §5.4 ✓ HONORED.

Verified:
- Line 101 paragraph contains verbatim phrases "structural test the same" + "self-imposed commute lease" in canonical Aeon-overlap form.
- No Pass 3.5 restoration proposal touches line 101.
- F-DE-Ch7-1 (lines 143–151) + F-DE-Ch7-2 (line 33) + F-DE-Ch7-4 (line 193) + F-DE-Ch7-3 (line 127, recommended HOLD) + F-DE-Ch7-5 (line 215, recommended HOLD) are all distant from line 101.

Verdict: **HONORED.** No restoration incidentally varies the Aeon-overlap held passage. Aeon Version C pitch fire window Sun May 31 14:01 UTC remains active; line 101 stays LOCKED.

### §6.5 Theorem 10.3 (Abundance Masking) cross-reference at Ch 7:121 — ✓ HONORED

Per session hard constraint + Pass 3.2 §5.9 + Pass 3.4 §5.5 ✓ HONORED.

Verified:
- Line 121 paragraph closes with "...formalizes this in Theorem 10.3 (Abundance Masking) of the Tech Appendix" — canonical numbering matches Tech Appendix v2.0.0.
- No Pass 3.5 restoration proposal touches line 121.

Verdict: **HONORED.** Theorem 10.3 cross-reference unmodified.

### §6.6 Named-subject consent check — CLEAN ✓

Per Pass 3.2 §5.7 + Pass 3.4 §5.3. Living named subjects (Mark Lehner + Zahi Hawass + William Nordhaus + Nick Bostrom + Will MacAskill + Toby Ord) all cited via on-record published academic work — public-record exception per [feedback_named_subject_consent.md](../memory/feedback_named_subject_consent.md). Deceased named subjects (Sima Qian + Qin Shi Huang + Sir John Hartwick if deceased) — historical-record exception or public-record exception. No restoration proposal adds individual living-private subjects (F-DE-Ch7-2 Mars administrator is explicitly composite; F-DE-Ch7-2 "grandchildren / kindergarten classroom / agricultural domes" are scene-anchor specifics within thought-experiment fiction).

Verdict: **CLEAN.** No new named-subject consent regression introduced by restoration proposals.

### §6.7 Path B contamination check — CLEAN ✓

Per Pass 3.4 §5.7. Chapter operates at analytical-thought-experiment register throughout; no apparatus-tripwire patterns surface. Restoration proposals operate within plain-prose register; no Path B patterns introduced.

Verdict: **CLEAN.**

### §6.8 Mars administrator pronoun discipline — ✓ HOLDS (with restoration preserving)

Per Pass 3.2 §5.7 ✓ HOLDS. She/her pronoun chain at lines 27–47. F-DE-Ch7-2 restoration ("Her grandchildren..." / "her office") preserves the she-pronoun chain. No leakage to they/he/third-person-generic.

Verdict: **HOLDS** under restoration proposals.

### §6.9 Scaffolding scan — CLEAN ✓

No `TODO`, `TK`, `Option A`-`Z`, `RATIFIED`, `Phase C-*`, `F-V*`, `INCLUDE/EXCLUDE` glyphs, or other scaffolding patterns in body prose. Per [tools/quality-gates/scaffolding-patterns.yaml](../quality-gates/scaffolding-patterns.yaml). Restoration proposals use prose-register language with no scaffolding vocabulary.

Verdict: **CLEAN.**

### §6.10 Locked elements verbatim preservation inventory

Per pipeline doctrine v1.0.0 §3 change-cascade routing + Pass 3.1 MEDIUM-8 + Pass 3.2 §5.8 + Pass 3.4 ratifications: the following passages are LOCKED (no Pass 3.5 modification proposed):

- **Ch 7:101 commute-lease paragraph** — Aeon-overlap held passage; "structural test the same" + "self-imposed commute lease" verbatim; locked until post-Sun May 31 14:01 UTC Aeon fire window + author re-disposition.
- **Ch 7:121 Theorem 10.3 (Abundance Masking) cross-reference** — matches Tech Appendix v2.0.0 canonical numbering; session hard constraint.
- **Ch 7:21 chapter-opening universality claim (post Pass-2 F-V2 Option B application)** — Pass 3.2 F-V2 Phase C-β edit; substantive universality-claim framing preserved.
- **Ch 7:85 RCV first-occurrence parenthetical (post Pass-2 §5.3 Option A application)** — Pass 3.2 §5.3 Phase C-β edit; apparatus register Item 14 Sandel-hybrid first-introduction discipline preserved.
- **Ch 7:121 Abundance Masking Title-case bolded heading (post Pass-2 §5.3 Option C application)** — Pass 3.2 §5.3 Phase C-β edit; terms_index Title-case discipline preserved.
- **Ch 7:141 Bostrom-MacAskill-Ord lineage citation cluster** — terms_index line 683 + Insight #33 first-chapter-introduction discipline; all four canonical citations + FHI/CSER literature pointer required.
- **Ch 7:195 recast objection-response opening (post Pass-2 F-V17 Option B application)** — Pass 3.2 F-V17 Phase C-β edit preserved.
- **Ch 7:229 framework-summary recap (post Pass-2 F-V11 Option B application)** — Pass 3.2 F-V11 Phase C-β edit preserved.
- **Pass 3.1 Phase C-α edits at lines 19, 33, 197, 213, 215, 241** — Pass 3.1 ratification; substantive content preserved.

Pass 3.5 restoration proposals (F-DE-Ch7-1 at lines 143–151 + F-DE-Ch7-2 at line 33 + F-DE-Ch7-4 at line 193) operate outside all LOCKED elements (the F-DE-Ch7-2 line 33 restoration adds within the existing administrator-paragraph but does NOT touch the Pass 3.1 Phase C-α edit at line 33 — see verification below).

**F-DE-Ch7-2 verification against Pass 3.1 line 33 edit.** Pass 3.1 Phase C-α at line 33 applied "sixty percent" precision (verified in Pass 3.2 §5.11). F-DE-Ch7-2 Option A restoration inserts the bodily-presence beat AFTER the existing "She knows what happens to a habitat that runs out of water" sentence and BEFORE the existing "She also knows that the consortium, having captured its return..." sentence. The "sixty percent" precision earlier in the paragraph is untouched. Pass 3.1 Phase C-α edit at line 33 preserved.

Verdict: **All LOCKED elements honored.**

---

## §7. Cross-character impact analysis (Pass 3.3 / 3.4 verdict flip-conditions)

### §7.1 Pass 3.3 acceptance verdict impact

Pass 3.3 ratified 30 INCLUDE / 0 NEUTRAL / 0 EXCLUDE at commits `697bcd2` + `0a3de00` (READY-AS-IS; §8.3 Option A HOLD). Pass 3.5 restoration impact (post-Phase-C-δ projection assuming F-DE-Ch7-1 + F-DE-Ch7-2 + F-DE-Ch7-4 all applied per recommendations):

| Character category | Pre-Pass-3.5 verdict | Post-F-DE-Ch7-1 application | Post-F-DE-Ch7-2 application | Post-F-DE-Ch7-4 application |
|---|---|---|---|---|
| Char 1 (trade-press editor) | ✓✓ INCLUDE | **Strengthened** (analytically-densest passage gets concrete civilizational-application anchors) | **Strengthened** (primary scene gets bodily-presence beat) | **Strengthened** (objection-response pacing tightened) |
| Char 2 (Ostrom-successor / institutional-economics) | ✓✓ INCLUDE | Unchanged (apparatus register preserved) | Unchanged | Unchanged |
| Char 3 (environmental-economics) | ✓✓ INCLUDE | Strengthened (civilizational-application anchors compound the existential-substitutability claim) | Unchanged | Unchanged |
| Char 4 (planetary scientist / quantitative reader) | ✓ INCLUDE | Strengthened (application-anchor specifics give quantitative reader concrete material) | Unchanged | Unchanged |
| Char 5 (longtermism / EA-adjacent reader) | ✓ INCLUDE | Unchanged (scope-disclaimer preserved) | Unchanged | Unchanged |
| Char 6 (SF-literate / thought-experiment reader) | ✓✓ INCLUDE | Unchanged | Strengthened (primary scene gets bodily-presence beat the SF-literate reader values) | Strengthened (objection-response pacing improves) |
| Char 7 (environmental-philosophy reader) | ✓ INCLUDE | Unchanged | Strengthened (population-bodily-presence compounds ethical engagement) | Unchanged |
| Char 8 (off-world-extraction-ethics reader) | ✓ INCLUDE | Unchanged | Unchanged | Unchanged |
| Char 9 (Aeon-overlap-aware reader) | ✓ INCLUDE | Unchanged | Unchanged | Unchanged |
| Char 10-30 (remaining acceptance set per Pass 3.3 §3) | ✓ / ✓✓ INCLUDE | Unchanged or marginally strengthened | Unchanged or marginally strengthened | Unchanged or marginally strengthened |

**Net Pass 3.3 impact post-Pass-3.5 (assuming F-DE-Ch7-1 + F-DE-Ch7-2 + F-DE-Ch7-4 applied):** 30 INCLUDE / 0 NEUTRAL / 0 EXCLUDE preserved; ~6 characters' verdicts trend strengthened; no character shifts toward NEUTRAL or EXCLUDE. Pass 3.3 §8.3 Option A HOLD disposition remains substantively-reinforced (the Pass 3.5 restorations are downstream-of-acceptance work; they do not retroactively justify Option B / C reconsideration on §8.3).

### §7.2 Pass 3.4 robustness verdict impact

Pass 3.4 RATIFIED ROBUST WITH OPTIONAL SPOT-FIXES at commit `d46a6ae` (Option A HOLD, reconsidered same day to T1+T3+T4 application per framing). Pass 3.5 restoration impact:

| Thread | Pre-Pass-3.5 disposition | Post-F-DE-Ch7-1 | Post-F-DE-Ch7-2 | Post-F-DE-Ch7-4 |
|---|---|---|---|---|
| T1 (Mars-canonization cumulative-framing) | RATIFIED HOLD (re-disposed to APPLY per framing) | Unchanged (restoration is downstream of disclaimer-position) | Marginally tightened (bodily-presence beat could deepen Mars-thought-experiment framing; balanced by methodology-not-advocacy disclaimer at line 199) | **Marginally tightened** (transitional breath partially absorbs Pass 3.4 A1 objection-response-fatigue concern) |
| T2 (Public-Choice silent-adjacent) | RATIFIED HOLD | Unchanged | Unchanged | Unchanged |
| T3 (Public-Choice cross-chapter forward-reference) | RATIFIED HOLD (re-disposed to APPLY per framing) | Unchanged | Unchanged | Unchanged |
| T4 (Bostrom-lineage citation contestation) | RATIFIED HOLD (re-disposed to APPLY per framing) | **Marginally tightened** (application-anchor specifics compound the substantive substitutability-claim and reduce surface-anchor-poverty Pass 3.4 A4 weighted) | Unchanged | Unchanged |
| T5-T8 (substantive load-bearing threads) | RATIFIED HOLD (per pre-pub review queue) | Unchanged | Unchanged | Unchanged |

**Net Pass 3.4 robustness impact (assuming F-DE-Ch7-1 + F-DE-Ch7-2 + F-DE-Ch7-4 applied):** ROBUST WITH OPTIONAL SPOT-FIXES verdict preserved; cross-pressure positioning diagnostic (A1 vs A4 cosmic-scale opposite-direction pull; A1 vs A12 extract-freely-cluster opposite-direction pull) preserved; T1 + T4 threads marginally tightened by restoration; no thread re-opened.

### §7.3 Pre-publication review queue impact

Per Pass 3.4 §8.4 pre-publication review queue items (T1 + T2 + T4 + T5 + T6 + T7 + T8 acknowledgments). Pass 3.5 restoration does NOT modify any pre-pub-review-queue acknowledgment; all items remain for Stage 5 re-sign-off (Stage 5 `b37aa46` becomes stale post-Phase-C-δ if any spot-fix ratified per framing).

---

## §8. Verdict synthesis

### §8.1 Findings tally

| Severity | Count | Findings |
|---|---|---|
| HIGH | 1 | F-DE-Ch7-1 (existential-substitutability-gap ranking lines 143–151 application-anchor restoration; Pass 3.4 §6 pre-flagged site) |
| MEDIUM | 3 | F-DE-Ch7-2 (Mars habitat scene line 33 inhabitant-bodily-presence beat); F-DE-Ch7-3 (Mars-resident-visiting-Earth line 127 bridging sentence, default HOLD); F-DE-Ch7-4 (Mars-is-false-analogy section line 193 transitional bridge; Pass 3.4 §6 pre-flagged site) |
| LOW | 2 | F-DE-Ch7-5 (Qin/pyramids paragraph balance, default HOLD); F-DE-Ch7-6 (line 101 Aeon-overlap LOCKED informational) |

**Total findings:** 6 (1 HIGH + 3 MEDIUM + 2 LOW).

**Restoration-recommended findings (APPLY):** 3 — F-DE-Ch7-1 Option A + F-DE-Ch7-2 Option A + F-DE-Ch7-4 Option A.

**Restoration-default-HOLD findings:** 3 — F-DE-Ch7-3 Option B (hold) + F-DE-Ch7-5 Option B (hold) + F-DE-Ch7-6 LOCKED.

### §8.2 Aggregate verdict

**READY-AFTER-RESTORATION.**

Ch 7 emerges from Pass 3.5 whole-chapter restoration scan with one HIGH-severity restoration warrant (F-DE-Ch7-1 — the apparatus-density spike at lines 137–151 that Pass 3.4 §6 explicitly pre-identified), two MEDIUM-severity APPLY-recommended restorations (F-DE-Ch7-2 inhabitant-bodily-presence at primary scene + F-DE-Ch7-4 objection-response transitional breath), one MEDIUM HOLD (F-DE-Ch7-3 line 127 bridging — substance overlaps with existing close), and two LOWs (F-DE-Ch7-5 balance — minor; F-DE-Ch7-6 line 101 Aeon-overlap LOCKED — informational).

The chapter's full prior Stage-3 sequence (Pass 3.1 + Pass 3.2 + Pass 3.3 + Pass 3.4 + Stage 4) produced canonical-state prose that the developmental-edit lens finds substantially-clean. The Pass 3.5 restoration warrants address precisely the sites Pass 3.4 §6 pre-identified (lines 137–151 + lines 179–203) — the audit operates as designed.

Under the author context-for-decisions framing ("make the book as good as possible. period."), the three APPLY-recommended restorations materially strengthen the chapter for sample-chapter audience reading (agent/publisher first-read; trade-press editor first-read). The HIGH-severity restoration is particularly load-bearing: the existential-substitutability-gap ranking is the chapter's analytical pivot connecting the framework's universality claim to Ch 9's renewable-transition policy work, and grounding the ranking's tiers in concrete civilizational-application anchors compounds rather than dilutes the analytical work the chapter does.

The cross-pressure positioning diagnostic (Pass 3.4 §4.1 A1 + A4 cosmic-scale opposite-direction pull; A1 + A12 extract-freely-cluster opposite-direction pull) is preserved under the proposed restorations; no adversarial thread is re-opened.

### §8.3 Recommended Phase C-δ action

Per Amendment-C (Interactive Ratification Protocol): ratification + application combine in one session OR Pass 3.5 may use the per-prompt serial cadence with ratification in this session + application in a separate Phase C-δ session.

**Recommended Phase C-δ application (if author ratifies "as recommended"):**

1. **Apply F-DE-Ch7-1 Option A** — five-paragraph existential-substitutability-gap ranking (lines 143–149; line 151 unchanged) — add application-anchor clauses to each of the four tier paragraphs.
2. **Apply F-DE-Ch7-2 Option A** — Mars habitat scene (line 33) — add inhabitant-bodily-presence single sentence (~50 words) between existing "She knows what happens..." and "She also knows that the consortium...".
3. **Apply F-DE-Ch7-4 Option A** — Mars-is-false-analogy section (line 193) — add transitional bridging sentence (~13 words) between line 191 close and line 193 second-objection opening.
4. **Hold F-DE-Ch7-3** — Mars-resident-visiting-Earth line 127 (existing close already does the bridging work; substance-overlap concern).
5. **Hold F-DE-Ch7-5** — pyramids/Qin balance (minor; no restoration warrant).
6. **F-DE-Ch7-6 (Aeon-overlap LOCKED)** — no author-action; informational.

**Phase C-δ session marching orders:**

If author ratifies "as recommended":
- Apply F-DE-Ch7-1 Option A (4 paragraph restorations at lines 143, 145, 147, 149).
- Apply F-DE-Ch7-2 Option A (1 sentence restoration at line 33).
- Apply F-DE-Ch7-4 Option A (1 sentence restoration at line 193).
- Append §11 disposition log to this artifact recording ratification + application.
- Update Pass 3.4 §11 / §12 closure cascade (Pass 3.5 complete; full Ch 7 Stage 3 sequence CLOSED through Pass 3.5).
- Update PM dashboard Ch 7 row reflecting Pass 3.5 CLOSED + Stage 4 re-ratification required + Stage 5 re-sign-off required.
- Update Phase C-γ artifact (if landed) to coordinate ordering with Phase C-δ.
- Single atomic commit + fast-forward merge to main per CLAUDE.md author-ratified end-user-facing-prose discipline.
- Stage 4 re-ratification (author-managed-offline; one-line marker per Ch 9 §9 + Ch 2 + Ch 6 precedent).
- Stage 5 re-sign-off (gate-triggered; chapter is sample-chapter pair with Ch 5 per workstream handoff line 333).

If author ratifies "hold all":
- No prose modifications to Ch 7.
- Append §11 disposition log recording PROPOSED-but-held disposition.
- PM dashboard Ch 7 row remains DONE-DONE (Pass 3.5 CLOSED with PROPOSED-but-held disposition).
- Same auto-merge; Stage 4 + Stage 5 status unchanged.

If author wants per-finding interactive: respond per finding (F-DE-Ch7-1 Option A / B / C; F-DE-Ch7-2 Option A / B / C / D; F-DE-Ch7-3 Option A / B; F-DE-Ch7-4 Option A / B / C; F-DE-Ch7-5 Option A / B; F-DE-Ch7-6 LOCKED).

### §8.4 Pass 3.5 closure forward-cadence

Per [feedback_audience_aware_drafting_discipline.md](../memory/feedback_audience_aware_drafting_discipline.md) v3.1 Amendment B: Pass 3.5 is the final Stage 3 pass. After Pass 3.5 ratification + application:

- **Ch 7 Stage 3 fully CLOSED.** Per-prompt serial cadence complete (3.1 → 3.2 → 3.3 → 3.4 → 3.5; Phase C-α + Phase C-β + Phase C-γ + Phase C-δ all applied if ratified).
- **Stage 4 re-ratification required if any Pass 3.5 spot-fix ratified** (author-managed-offline; one-line marker).
- **Stage 5 re-sign-off required if any Pass 3.5 spot-fix ratified** (gate-triggered at distribution-readiness gate per Amendment A two-class cascade — sample-chapter pair status with Ch 5 per workstream handoff line 333 elevates priority).
- **Pre-publication review queue items for Ch 7** (per Pass 3.4 §8.4 — T1 + T2 + T4 + T5 + T6 + T7 + T8 acknowledgments) carry forward to Stage 5 re-sign-off.
- **Aeon-overlap held passage at Ch 7:101 disposition** remains pre-Sun May 31 14:01 UTC fire window LOCKED; post-fire window author re-disposition opens line 101 for any post-Aeon restoration consideration (not in Pass 3.5 scope).

---

## §9. What this pass did NOT do

Per author's per-prompt scoping + v3.1 Amendment B distinct-pass discipline:

- **Did NOT re-run Pass 3.1 (fact-check).** Pass 3.1 ratified 2026-05-20 + Phase C-α applied at commit `4987e59`. The post-spot-fix prose is the audit baseline; Pass 3.1 findings are not re-litigated. No new factual concerns surfaced during Pass 3.5 reading.
- **Did NOT re-run Pass 3.2 (voice-polish).** Pass 3.2 ratified 2026-05-21 + Phase C-β applied at commit `e29d5ae`. No further per-paragraph LLM-tic findings proposed (polarity is restoration, not further cutting).
- **Did NOT re-score Pass 3.3 (acceptance) or Pass 3.4 (robustness).** Both ratified; verdicts canonical input. §7 above analyzes verdict-impact of Pass 3.5 proposals but does NOT re-litigate prior verdicts.
- **Did NOT pre-empt Phase C-γ application.** Phase C-γ (T1 + T3 + T4 per framing reconsideration) is firing in parallel worktree-isolated session; Pass 3.5 audited the post-Phase-C-β state (250 lines, pre-Phase-C-γ); Pass 3.5 restoration proposals are stable across the C-γ → C-δ application ordering (no overlap with Phase C-γ application sites).
- **Did NOT apply spot-fixes to the chapter file.** Phase C-δ (per-chapter spot-fix application session) does that after author ratification.
- **Did NOT re-write paragraphs.** Findings + restoration options + STOP, per the Pass 3.5 template's hard constraint.
- **Did NOT contact named subjects.** Per consent discipline.
- **Did NOT propose new framework concepts or meta-conclusions about the v3.0 / v3.1 discipline.**
- **Did NOT re-litigate apparatus register decisions.** Apparatus register Items 7, 10, 12, 14, 15 are downstream-of-only canonical decisions per `tools/rigor-passes/commons_bonds_rigor_pass_2026-05-11_apparatus_register_decision_v1.0.0.md`.
- **Did NOT modify Theorem 10.3 (Abundance Masking) cross-reference at Ch 7:121** per session framing hard constraint.
- **Did NOT propose restorations that incidentally vary the Aeon-overlap held passage at Ch 7:101** per session hard constraint + §6.4 explicit verification.
- **Did NOT touch any LOCKED chapter passage per §6.10 inventory.**
- **Did NOT re-run Stage 4 render-audit.** Author-offline pipeline-side per Stage 4 precedent.
- **Did NOT re-litigate Stage 5 sign-off / pre-publication review queue artifact.** Stage 5 `b37aa46` carries forward; re-sign-off required if any Pass 3.5 spot-fix ratified.

---

## §10. Hard constraints honored

- ✓ Did NOT apply spot-fixes to `manuscript/chapters/Chapter__7_OnOtherWorlds.md` in this PROPOSED artifact.
- ✓ Did NOT re-write paragraphs — proposed-revision options offered without applying.
- ✓ Did NOT re-litigate Pass 3.1, 3.2, 3.3, or 3.4 findings.
- ✓ Did NOT propose restorations that incidentally vary the Aeon-overlap held passage at Ch 7:101 (§6.4 explicit verification).
- ✓ Did NOT modify Theorem 10.3 (Abundance Masking) cross-reference at Ch 7:121 (§6.5 explicit verification).
- ✓ Did NOT propose new framework concepts or meta-conclusions about the v3.0 / v3.1 discipline.
- ✓ Did NOT contact named subjects.
- ✓ Applied substance-drives-length discipline — restoration recommendations are anchored in specific sensory / scene-anchor / reader-engagement / voice-flow substance, not padding for length.
- ✓ DID flag no apparatus regressions, no named-subject consent regressions, no Path B contamination (§6 sub-checks).
- ✓ Verified chapter file exists; verified line count (250) + chapter-state (post-Phase-C-β / pre-Phase-C-γ) at session start.
- ✓ Verified all referenced commit hashes on origin/main: `4948dbb`, `4987e59`, `440906f`, `e29d5ae`, `697bcd2`, `0a3de00`, `8c8f1f5`, `d46a6ae`, `e1b4d6d`, `b37aa46` — all confirmed.
- ✓ Verified format-model artifacts exist at cited paths (Ch 9 Pass 3.5; Ch 2 Pass 3.5; Ch 6 dev-edit; Ch 3 dev-edit).
- ✓ Applied Ch 9 Pass 3.5 as primary format model + Ch 2 Pass 3.5 as secondary format model per framing.
- ✓ Flagged Phase C-γ parallel-session ordering concern at §0.3; verified restoration sites do not overlap with Phase C-γ application sites.
- ✓ Documented sandbox branch-creation blocker at §0.4; artifact committed on worktree default branch; will merge to main per workstream branch-discipline at session close.
- ✓ Per-finding format honored: Options + Recommendation + Reasoning per Amendment-C-scoped Interactive Ratification Protocol.

---

## §11. Ratification record (closed 2026-05-26)

Author ratification of all six findings completed 2026-05-26 via interactive disposition walkthrough ("ratify pass 3.5 as recommended and proposed"). All six dispositions ratified per Pass-3.5 recommendations.

### §11.1 Findings ratified for Phase C-δ application (3 chapter edits — six sub-edits across the chapter)

| ID | Disposition | Edit summary |
|---|---|---|
| **F-DE-Ch7-1 (HIGH)** | **Option A APPLY** | Ch 7:143 + 145 + 147 + 149 — add one application-anchor clause per resource-tier paragraph within existing paragraph structure. Net ~80 words across four paragraphs. Closes Pass 3.4 §6 pre-identified apparatus-density-spike flag at the level Pass 3.4 anticipated. Materially strengthens the chapter's analytically-densest passage at sample-chapter-read level. Line 151 (helium-3) unchanged per Option A recommendation (already substantively-grounded). |
| **F-DE-Ch7-2 (MEDIUM)** | **Option A APPLY** | Ch 7:33 — insert one inhabitant-bodily-presence sentence within existing administrator-reasoning paragraph, after "She knows what happens to a habitat that runs out of water." Net ~50 words single sentence; grounds abstract demographic + abstract administrator in lived-population stakes via specific physicality (grandchildren / kindergarten classroom / agricultural domes); compounds discount-factor analytical claim at line 43. |
| **F-DE-Ch7-4 (MEDIUM)** | **Option A APPLY** | Ch 7:191 — insert single bridging sentence ("The frictionless-plane defense settles one objection; another follows from a different direction.") at the close of the first objection-response cycle, before the line 193 second-objection launch. Net ~13 words single sentence; gives the section's hinge-point transitional breath. Closes Pass 3.4 §6 pre-identified objection-response section length flag. |

### §11.2 Findings ratified as HOLD (no edit; per Pass-3.5 recommendation)

| ID | Disposition | Rationale |
|---|---|---|
| **F-DE-Ch7-3 (MEDIUM)** | **Option B HOLD** | Mars-resident-visiting-Earth seven-fold "Free X" passage at line 127. Seven-fold enumeration is rhetorically self-sufficient (Pass 3.2 F-V7 held substantively-earned); existing analytical-close already names the framework's analytical move; Option A's substance overlaps with existing close. Substance-drives-length default. |
| **F-DE-Ch7-5 (LOW)** | **HOLD** | Per Pass 3.5 §5 disposition. |
| **F-DE-Ch7-6 (LOW)** | **LOCKED (informational)** | Aeon-overlap held passage at Ch 7:101 — per locked-element discipline (Pass 3.1 MEDIUM-8 held; Pass 3.2 §5.8 verified; Pass 3.3 §5.4 verified; Pass 3.4 §5.4 verified; Pass 3.5 §6.4 verified). |

### §11.3 Phase C-δ scope

**3 prose edits to `manuscript/chapters/Chapter__7_OnOtherWorlds.md`** at:
- **Line 33** — F-DE-Ch7-2 Option A (Mars habitat inhabitant-bodily-presence beat; ~50 words)
- **Line 143 + 145 + 147 + 149** — F-DE-Ch7-1 Option A (application-anchor clauses across four resource tiers; ~80 words across 4 paragraphs)
- **Line 191** — F-DE-Ch7-4 Option A (objection-response transitional breath; ~13 words)

All edits are intra-line additions (extend existing paragraphs); chapter line count remains 250. Per-finding application text is in §3 + §4 above; agent applies verbatim per Option A specifications.

**Hard constraints carried into Phase C-δ:**
- Theorem 10.3 (Abundance Masking) cross-reference at Ch 7:121 must NOT be modified.
- Aeon-overlap held passage at Ch 7:101 must NOT be modified.
- Phase C-γ application sites (line 19 + line 141 + line 221) must not be regressed.
- Pass 3.1 + 3.2 + 3.3 Phase-C edit lines (19, 21, 33, 85, 121, 141, 195, 197, 213, 215, 221, 229, 241) must not be regressed — Phase C-δ extends some of these lines (line 33 for F-DE-Ch7-2) but does NOT replace the existing Phase C content.

### §11.4 Downstream implications

- **Phase C-δ application** follows this ratification (next commit; bundled with this PROPOSED+RATIFIED commit OR separate per author preference).
- **Stage 4 RATIFIED (`e1b4d6d` 2026-05-26)** + **Stage 5 sign-off (`b37aa46` 2026-05-26)** are stale (generated pre-Phase-C-γ + pre-Phase-C-δ). **Stage 4 re-ratification (author-completed-offline via docker render pipeline) + Stage 5 re-sign-off + pre-pub queue refresh required** post-Phase-C-δ application to restore READY-TO-SUBMIT status at the post-reconsideration chapter state.
- Per Ch 5 precedent (`3a4f774` Ch 5 Phase C complete bundle), Stage 4 + Stage 5 may bundle into a single closure commit if author confirms Stage 4 author-offline ratification has been completed at the post-Phase-C-δ chapter state.

---

*End of Ch 7 Stage-3 Pass 3.5 (Developmental-Edit) rigor pass — RATIFIED 2026-05-26. Aggregate verdict READY-AFTER-RESTORATION; 3 APPLY-ratified (F-DE-Ch7-1 + F-DE-Ch7-2 + F-DE-Ch7-4) + 3 HOLD-ratified (F-DE-Ch7-3 + F-DE-Ch7-5 + F-DE-Ch7-6 locked). All three APPLY-ratified restorations materially strengthen the chapter for sample-chapter audience under author context-for-decisions framing ("make the book as good as possible"). Phase C-δ application applies 3 chapter edits across lines 33 + 143/145/147/149 + 191. Stage 4 + Stage 5 re-ratification required post-Phase-C-δ to restore READY-TO-SUBMIT status. Aeon-overlap held passage at Ch 7:101 + Theorem 10.3 cross-reference at Ch 7:121 + Phase C-γ application sites all honored.*
