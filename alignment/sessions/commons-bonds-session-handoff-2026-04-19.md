# Commons Bonds — Session Handoff Memo

**Date:** April 19, 2026  
**Created:** At session close due to context pressure  
**Next session:** Open with this memo plus the alignment companion

## ✅ Session Result

**Decision A ratified.** April 19 eight-tier decomposition is canonical. Multi-scale revision pattern (scale-abstract core + manifestations) validated against Tier 1 and Tier 8 via ten-critic rigor test. Cleared for WS02/WS03 execution across remaining four scale-locked tiers (2a, 3, 5, 7) plus Tier 2a rename ("Individual Risk Cost" → "Actuarial Risk Cost").

## Three Architectural Refinements Surfaced This Session

### Refinement 1 — Mechanism vs. Shield (project-wide standing refinement)

> ⚠️ **This is the big one.** Not a single-workstream edit — a project-wide vocabulary and structural adjustment that will resurface in every future rigor test.

"Distance" is carrying two different conceptual loads. As a taxonomy of separation types (spatial, temporal, legal, institutional, demographic, ecological, political) it works and stays. As a name for the mechanism of severance itself it strains. The mechanism is **structural allocation** — an arrangement assigning value-capture to one party and cost-bearing to another. Distance is the **shielding condition** preventing the allocation from being recognized, enforced, or corrected.

**Files affected (cross-file update scope):**

- **Chapter 2** — where cost severance is first articulated as a mechanism. Needs a revision pass to lead with allocation-as-mechanism and reposition distance as shielding.
- **Chapter 6** — mechanism integration with the eight-tier decomposition must match Chapter 2's reframe.
- **Chapter 10** — the villain-analysis landing ("institutional legibility infrastructure") is essentially shield-dismantling infrastructure; the reframe sharpens the prescription.
- **Glossary (WS02)** — new entries for *Structural Allocation* (mechanism) and *Shielding / Distance* (condition); revise *Cost Severance* entry to reflect the split.
- **Technical Appendix (WS08)** — formal definitions need to reflect the split; potentially two new A.x definitions.
- **Every future rigor/steelman/stress test** — default starting posture should use the two-path allocation/shield structure.

### Refinement 2 — Universal claim, scale-dependent salience

Framework is universal in claim (all eight tiers exist structurally in any extraction arrangement) but scale-dependent in salience (which tiers are visible, measurable, actionable depending on observer position — individual, community, firm, government). Scope: WS02, WS03, WS08 per the prototype pattern work.

### Refinement 3 — Scale-abstract verbiage revision

Direct consequence of Refinement 2. Six of eight canonical tiers are scale-locked in surface language (1, 2a, 3, 5, 7, 8). Revise each to scale-abstract core + manifestations paragraph.

## Tier 8 Rigor Test — Key Outcomes

**Verdict:** Pattern validated across ten critic perspectives (Academic Economist, Analytic Philosopher, AI Adversary, Writerly Editor, Future-Proofer, Novelty Critic, Falsifiability, Completeness, Libertarian, Leftist).

**Five refinement flags for WS02/WS03 execution:**

1. **Measurability split.** Make direct-expenditure / institutional-corrosion split explicit (per Academic Economist).
2. **Sub-division question.** Consider Tier 8a (Direct Capture Expenditure) vs. 8b (Institutional Corrosion), paralleling 2a/2b structure (per Analytic Philosopher). Do not resolve in WS01.
3. **Recursive structural role.** Tier 8 is uniquely both an allocation and a shield-maintenance expenditure; it's the cost of manufacturing invisibility of Tiers 1-7 (per AI Adversary).
4. **Individual-scale concretization.** Must reach for concrete examples (pneumoconiosis/state-medical-board is one; develop others) (per Writerly Editor).
5. **Framework-level falsifiability (NEW).** The allocation/shield reframe gives every tier (NOT just Tier 8) two independent paths to CS → 0: (a) allocation symmetry, (b) shield absence. Worth calling out in Chapter 6 or Technical Appendix as a framework-strengthening observation.

### Revised Tier 8 Falsifiability Defense (supersedes earlier draft)

The allocation/shield reframe gives Tier 8 two independent paths to CS → 0:

- **Allocation symmetry path.** An arrangement where those bearing political capture costs have equal influence over the system producing the capture. Theoretical asymptote; rarely realized; cleanly specifiable.
- **Shield absence path.** An arrangement where shielding conditions are dismantled through transparency, independent verification, distributed governance. Norway's sovereign wealth fund governance approximates this; EU disclosure regimes approximate on specific domains.

Framework predicts different CS values depending on which condition holds and to what degree. Two paths, independently testable, combinable. Falsifiability holds at the framework level, not just the tier level.

### Novelty Posture (Chapter 6 Tone Discipline)

Current framework delivers **narrow novelty** — integration that does new work — which is the signature of important frameworks (Darwin, Keynes, Piketty, Desmond, Rawls). The success metric (labor lawyer using "severed cost" in 10 years, judge doesn't need it explained) is a narrow-novelty success metric by design. Do not overclaim broad novelty in Chapter 6 prose; lean into integration claims which are defensible and strong.

## Execution List for Next Session

1. **Create v10 of eight-tier decomposition.** Content is largely ready; the failed upload attempt in the previous session contains the full draft. Two updates needed before upload: (a) replace the Tier 8 Falsifiability defense with the two-path version above; (b) add the Mechanism vs. Shield project-wide refinement note as a separate flagged section in the appended content. Upload as `commons-bonds-eight-tier-decomposition 10.html` to Commons Bonds root.

2. **Update alignment companion.** Create `00_alignment_companion_v2.html` (in Workstreams folder). Add Section 4 Issue #9 carrying the three architectural refinements, explicitly flagging Refinement 1 (mechanism/shield) as project-wide standing. Add Section 10 log entry for April 19 documenting Decision A ratification plus v10 creation.

3. **Manual cleanup (Chris does):** Delete `commons-bonds-eight-tier-decomposition 9.html`, `commons-bonds-multi-scale-revision-prototype.html`, original `00_alignment_companion.html` after v2 is acknowledged.

4. **Next decisions** (WS01 still open): Decision D (two-book split), then C (Chapter 10 villain landing), then B (Option C architectural surfacing).

## Technical Notes

- Drive `create_file` uploads are reliable below ~20KB but can error on larger payloads. The v10 draft is ~43KB base64 — consider splitting the appended section into its own sidecar if re-upload fails.
- Claude's tools can create but not update-in-place or delete. All "replacement" is create-new + manual-delete.
- Versioning convention: vN+1 for canonical framework files (e.g., decomposition); _v2 suffix for alignment companion and similar.
- Consider using `memory_user_edits` tool in next session to persist cross-session: "Decision A ratified; April 19 eight-tier decomposition is canonical" and "Mechanism/shield reframing is a standing project-wide architectural refinement."
