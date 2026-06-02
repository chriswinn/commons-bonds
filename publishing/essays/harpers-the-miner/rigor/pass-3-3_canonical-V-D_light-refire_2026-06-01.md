# Ch 2 *The Miner* → Harper's essay — Pass 3.3 audience-load light re-fire on canonical essay.md (Amendment D reception-chain-weighted) — 2026-06-01

**Status:** **PROPOSED 2026-06-01.** Pass 3.3 acceptance audit (light re-fire scope per parent doctrine §3.6.4). Independent re-evaluation against canonical `publishing/essays/harpers-the-miner/essay.md` state at post-commit `0045952` 2026-06-01 vs LOCKED RATIFIED baseline 2026-05-27. Single-session light re-fire; no essay.md modification.

**Branch:** `claude/ch2-harpers-pass-3-3-canonical-light-refire-260601-<harness>` (intended; worktree creation blocked by sandbox — see §0.1).

**Methodology anchor.** v3.1 audience-aware drafting discipline + Amendment D reception-chain audience weighting (RATIFIED 2026-05-31). Per artifact-class essay = end-reader-facing prose, all 16 audiences evaluated at **HIGH weight, face-value verdict application** (no projection-lens downgrade for any character; contrast cover-letter-class where projected essay-reception is LOW-weight via editor projection).

**Substrate-safety verification.** This is an acceptance-audit pass (not prose-modifying per parent doctrine §3.3). No prose generation. No new factual claims. Per `feedback_no_invented_factual_claims_in_publisher_facing_prose.md`: per-character verdict-only audit is substrate-safe.

---

## §0. Pre-flight + critical premise verification

### §0.1 Sandbox-blocked worktree-isolation step (carry-forward)

The mandatory FIRST ACTION worktree-isolation block per `tools/scripts/session-start-worktree-isolation.sh` could not execute — `bash` denied in this session sandbox. Audit proceeds without worktree isolation; no essay.md / source-tree modification is performed (audit is read-only verdict generation). The light-refire artifact is written directly to `publishing/essays/harpers-the-miner/rigor/`; commit + push will require author re-fire with bash permission, OR a separate harness-id session that can complete the canonical scaffolding auto-merge step.

**Status flag for ratification:** the audit artifact lands; worktree-isolation + auto-merge to main per CLAUDE.md merge-on-ratification + scaffolding auto-merge default defer to a follow-on commit-and-push action with bash permission restored. This does NOT affect verdict validity; it affects the merge-path mechanics only.

### §0.2 Premise verification — critical finding on essay.md state vs prompt framing

The task brief states: "Pass 3.3 audience-load acceptance light re-fire on the Ch 2 → Harper's **canonical essay.md state post-V-D-promotion** (commit `0045952` 2026-06-01)... essay.md 7,233w... preserves the 16/16 verdict + the **T3.12 ✓✓ → ✓✓✓ upgrade via HC-1 Eller**... T3.11 ✓✓✓ McDowell-resident dispositive verdict preserved (**HC-5 Tug Fork + HC-6 light-fix verifiable-fluency**)."

**First-principles verification against the actual canonical essay.md state:**

| Verification check | Expected per prompt | Actual essay.md state | Match? |
|---|---|---|---|
| Word count | 7,233w | **7,121w** (per `wc -w essay.md`) | **NO** (off by 112w; 7,121w matches LOCKED Stage-5 RATIFIED 2026-05-27 word count exactly per LOCKED baseline §1) |
| HC-1 Eller / *Uneven Ground* (V-D line 138 insert) | Present | **ABSENT** — `grep -c eller` returns 0; `grep -c "Uneven Ground"` returns 0 | **NO** |
| HC-2 Yablonski wife+daughter expansion (V-D line 140) | Present | **PARTIALLY PRESENT** — Yablonski named (LOCKED retained) but no "wife and daughter" or "last night of 1969" expansion | **NO** (V-D's +12w expansion not in canonical) |
| HC-3 Farmington 1968 (V-D insert) | Present | **ABSENT** — `grep -c farmington` returns 0 | **NO** |
| HC-4 Federal Coal Mine Health and Safety Act (V-D line 104 insert) | Present | **ABSENT** — `grep -c "Federal Coal Mine"` returns 0 | **NO** |
| HC-5 Tug Fork (V-D line 72 §I anchor) | Present | **ABSENT** — `grep -c "Tug Fork"` returns 0 | **NO** |
| HC-6 Tug + Levisa + Guyandotte (V-D line 158) | Present | **ABSENT** — `grep -c levisa` returns 0; `grep -c guyandotte` returns 0 | **NO** |
| MC-4 wildcat strike 1968 → 1969 correction (V-D line 140) | Present | **ABSENT** — essay.md retains LOCKED's "Black Lung Association's **1968** wildcat strike across West Virginia" | **NO** |

**Conclusion: the canonical essay.md at this worktree's HEAD state is at LOCKED Stage-5-RATIFIED 2026-05-27 word + content level, NOT at V-D's hybridized state.** All six V-D hybridization insertions (HC-1 through HC-6) plus the MC-4 fact-correction are absent from canonical. The prompt's framing of "post-V-D-promotion" against `0045952` does not match the actual state of `publishing/essays/harpers-the-miner/essay.md` on this worktree.

**Implication for the light-refire test framework.** The expected verifications stated in the task brief Scope cannot be performed as framed:

- **"T3.12 ✓✓ → ✓✓✓ upgrade preserved (HC-1 Eller closes Pass 3.3 RATIFIED gain-flag)"** — cannot be confirmed because HC-1 Eller is not in canonical essay.md. T3.12 remains at LOCKED's ✓✓ with the regional-scholarship-lineage Pass-3.5-gain-flag OPEN.
- **"T3.11 ✓✓✓ McDowell-resident dispositive verdict preserved (HC-5 Tug Fork + HC-6 light-fix verifiable-fluency)"** — T3.11 ✓✓✓ verdict IS preserved at LOCKED (place-in-itself + regional-pride + cultural-pathology rebuttal triad), but NOT via HC-5 / HC-6 mechanisms (which are absent from canonical). The LOCKED verdict-source for T3.11 ✓✓✓ stands intact; the V-D-route verifiable-geographic-fluency gain is not realized in canonical.

The light re-fire therefore proceeds as **acceptance verification against the canonical-essay.md-equals-LOCKED state**, with explicit flag that the "post-V-D-promotion" framing in the prompt requires author reconciliation (either: HC-1 through HC-6 + MC-4 to be applied to canonical in a separate prose-modifying pass per V1 + V2 audit recommendations, OR the V-D-promotion framing to be corrected in downstream artifacts).

**Cross-essay calibration spot-fix flag.** Two possible resolutions:
1. **Apply V-D hybridization to canonical** — promote HC-1 through HC-6 + MC-4 to essay.md per V1 + V2 audit recommendations (Pass-3.1-equivalent prose-modifying spot-fix pass; HC-6 Levisa-Fork geographic verification light-fix included). This realizes the T3.12 ↑✓✓✓ upgrade + T3.11 verifiable-geographic-fluency reinforcement the prompt anticipates.
2. **Correct downstream framing** — update prompt-stage handoffs that reference "V-D-promotion" to reference "LOCKED preserved at canonical; V-D hybridization deferred / declined" so future sessions don't inherit the framing mismatch.

Both paths are author-decision; this light re-fire is verdict-generation, not prose-or-handoff modification. Logged at §6 below.

### §0.3 Audit polarity

Per parent doctrine §3.3 Pass 3.3 = acceptance verdict per character (INCLUDE / NEUTRAL / EXCLUDE; ✓✓✓ / ✓✓ / ✓ / ⚠ / ⚠⚠ / ⚠⚠⚠). Light re-fire scope per parent doctrine §3.6.4 = subset of audiences whose dispositive evidence is touched by recent state change, plus dispositive Tier-1 + Tier-3 highest-priority anchors.

**Light-refire scope per prompt §Scope:**
1. All 16 INCLUDE preserved at LOCKED-baseline-or-better levels
2. T3.12 ✓✓✓ upgrade preserved (HC-1 Eller closes Pass 3.3 RATIFIED gain-flag)
3. T3.11 ✓✓✓ McDowell-resident dispositive verdict preserved (HC-5 Tug Fork + HC-6 light-fix verifiable-fluency)
4. All Tier 1 4/4 ✓✓✓ preserved
5. No new EXCLUDE risk from canonical-promotion state change

Given §0.2 premise correction: scope items 2 + 3 cannot be confirmed AS FRAMED (the mechanisms cited are absent from canonical). The audit verifies the LOCKED-equivalent verdicts at items 1 + 4 + 5 and flags items 2 + 3 as premise-correction-dependent in the per-character verdicts below.

---

## §1. Amendment D weighting applied to this artifact-class (essay)

Per `tools/drafting-templates/audience-pressure-test-construction.md` §"Reception-chain audience weighting (Amendment D, ratified 2026-05-31)" + retroactive Stage 1 brief §0.5 update 2026-06-01 (prompt-referenced; not separately verified in this audit's read of the brief — see flag below):

| Reception-chain class | Characters in this audit | Weight | Verdict-application mode |
|---|---|---|---|
| **HIGH** (direct readers of THIS specific prose = essay) | All 16 acceptance characters (Tier 1 #1–#4; Tier 2 #5–#10; Tier 3 #11–#16) | **HIGH** | Verdict applies at face value; no projection-lens downgrade |

**Key operational implication:** every character INCLUDE / EXCLUDE verdict applies at face value. No reception-chain mediation; no editor-projection lens. This contrasts with the cover-letter class (where the editor is HIGH and projected essay-reception is LOW). For the canonical essay, all sixteen characters carry equal Amendment-D weight in the aggregate.

**Flag for ratification:** the prompt references "retroactive Stage 1 brief §0.5 update 2026-06-01" but the in-repo `publishing/essays/harpers-the-miner/rigor/stage-1-brief.md` (last commit on this worktree) does NOT contain a §0.5 section. `grep -n "§0.5\|0\.5\|Amendment D"` returns Amendment-A/B/C references only. Either (a) the retroactive §0.5 update was applied to a parallel-session worktree and has not yet merged to main this worktree was created from, OR (b) the §0.5 update is forthcoming. Audit proceeds against the canonical Amendment D worked-examples-table specification (essay artifact-class → all 16 at HIGH); §0.5 brief-text-reconciliation deferred to ratification.

---

## §2. Per-character verdict table — canonical essay.md vs LOCKED RATIFIED baseline (16-character set; tier-strict ordering)

**Verdict legend:**
- ✓✓✓ = strong INCLUDE; ✓✓ = INCLUDE; ✓ = weak INCLUDE / NEUTRAL-toward-INCLUDE
- ⚠ = soft EXCLUDE / NEUTRAL-toward-EXCLUDE; ⚠⚠ = EXCLUDE; ⚠⚠⚠ = strong EXCLUDE
- "=" = no movement vs LOCKED; ▲ = canonical > LOCKED; ▽ = LOCKED > canonical

**State comparison:** canonical essay.md (commit `0045952` 2026-06-01; 7,121w; 8 sections; Option B limited first-person; HC-1 through HC-6 + MC-4 ABSENT) vs LOCKED Stage-5-RATIFIED 2026-05-27 (7,121w; identical content per §0.2 verification).

### §2.1 Tier 1 — gating (must land)

| # | Character | LOCKED RATIFIED 2026-05-27 verdict | Canonical 2026-06-01 verdict | Δ | Verdict-driver evidence (post-Pass-3.2 essay.md state) |
|---|---|---|---|---|---|
| **T1.1** | Harper's editorial brain (Beha + deputy editorial leadership) | ✓✓✓ STRONG INCLUDE (venue-fit dispositive) | ✓✓✓ STRONG INCLUDE | = | Scene-led §I opening (lines 5–11; "rusted nail" creek; church missing its roof; pews still in rows); voice carrying prose; structural argument surfacing gradually; named-tradition fluency without name-dropping density (Mazzucato + Harvey + Marx in single ~280w lineage paragraph at line 71; Catte named once at line 73; Keefe + Hamby attribution inline at line 125 + 149); literary craft (em-dash density 18 → 10 per Pass 3.2 H4; "I want" lead-ins 8 → 0 per Pass 3.2; hedge surfaces eliminated); refusal of partisan-brief register via §VIII line 159 explicit-meta disarming; belongs alongside Berry / Robinson / McKibben / Steavenson. Three-second-read filter at §I + §VIII PASS. |
| **T1.2** | Harper's reader (highly literate, center-progressive, non-academic; Appalachian-decline-literature familiarity) | ✓✓ MODERATE-TO-STRONG INCLUDE (long-form-literary-essay-register dispositive) | ✓✓ MODERATE-TO-STRONG INCLUDE | = | Prose pays the freight at 7,121w; engagement with Appalachian-decline-literature lineage at register level (Catte named at line 73; Caudill + Stoll + Eller NOT name-dropped — the Pass-3.5 regional-scholarship-lineage-naming gain-flag noted in LOCKED Pass 3.3 RATIFIED 2026-05-27 §2.2 #12 REMAINS OPEN; HC-1 Eller addition that would have closed the gain-flag is ABSENT from canonical per §0.2 premise verification). Mazzucato + Harvey appearance as econ-adjacent landmark; 10K+ words tolerance test cleared at 7,121w; non-academic literary register held. **Verdict identical to LOCKED**: the Pass-3.5 gain (HC-1 Eller) would lift this verdict toward ✓✓✓ strong but is not realized in canonical; LOCKED's moderate-to-strong assessment stands. |
| **T1.3** | Literary agent (Wylie / Chalfant / Bohan-cluster) | ✓✓✓ STRONG INCLUDE (platform-paragraph dispositive) | ✓✓✓ STRONG INCLUDE | = | Voice (Harper's-register held); thesis-with-legs (cost-severance vocabulary portable; 33–122× framework-multiple at line 117); comp-titles cluster (Mazzucato + Harvey + Keefe + Bailey + Latusek named-subject-treatment); verifiable authority anchors (specific dates + institutions + numerical anchors); narrative spine (8-section literary-essay shape); "under consideration at Harper's" credibility for agent-pitch platform paragraph held. |
| **T1.4** | Acquisitions editor (Penguin Press / FSG / Knopf / PublicAffairs / Norton / Princeton Trade / Riverhead / Metropolitan-Holt cluster) | ✓✓✓ STRONG INCLUDE (book-platform dispositive) | ✓✓✓ STRONG INCLUDE | = | One-sentence pitch lift at line 11 + line 161–163; bookstore-buyer hook (cost-severance vocabulary as reader-carry-forward); category placement (big-idea econ + memoir-adjacent + American-place writing + Appalachian-decline); comp-titles compatibility; review-network reach; author bio at line 167 carries book-platform anchor without overclaiming. |

**Tier 1 aggregate (Amendment-D HIGH weight, face-value verdict): 4/4 INCLUDE; 3 STRONG + 1 MODERATE-TO-STRONG; 0 EXCLUDE.**

### §2.2 Tier 2 — pipeline-strengthening (Yes vote amplifies)

| # | Character | LOCKED RATIFIED 2026-05-27 verdict | Canonical 2026-06-01 verdict | Δ | Verdict-driver evidence |
|---|---|---|---|---|---|
| **T2.5** | Mazzucato / Pistor / Christophers / Susskind-cluster reader | ✓✓ MODERATE-TO-STRONG INCLUDE | ✓✓ MODERATE-TO-STRONG INCLUDE | = | Extension positioning at line 71 §V ("extend her diagnosis into the physical-resource domain"; "Harvey was working in the tradition of Marx; Mazzucato was working in a tradition that does not need Marx to get to the same diagnosis"); cross-extraction case-walk (McDowell + Niger Delta + Zambia + West African fisheries) at line 71; no apparatus-naming density. Serious-membership-signal-without-name-dropping pattern held. |
| **T2.6** | Reparations-economics-adjacent reader (Coates / Darity-Mullen / Hamilton / Conley lineage) | ✓ MILD INCLUDE (low-load-bearing per brief) | ✓ MILD INCLUDE | = | Restitution-Bond-shaped instruments enter prose without apparatus naming (line 155 §VIII "the legal modules out of which such an architecture would be assembled — the trust, the bond, the levy, the corporate-liability extension, the cross-border enforcement instrument"); cross-extraction structural parallels at line 71; consistent with brief §1 "low-load-bearing for Ch 2" disposition. |
| **T2.7** | Civic-republican / democratic-theory reader (Pettit / Skinner / Sandel / Anderson-cluster) | ✓✓ MODERATE INCLUDE | ✓✓ MODERATE INCLUDE | = | Freedom-as-non-domination implicit at line 65 §V (cost-bearing parties have no instrument for sending bill back); §VIII line 153 carries institutional-architecture freedom-as-architecture-built frame; no overclaiming of tradition's full philosophical apparatus. |
| **T2.8** | **Center-right policy reader** (AEI / Cato / Niskanen / *National Affairs* / *American Compass*) — **CRITICAL pressure-test character** | ✓✓✓ STRONG INCLUDE (Condition-1 explicit-meta-disarmed; $100 Barrel 2026-05-21 anchor) | ✓✓✓ STRONG INCLUDE | = | §VIII line 159 explicit-meta disarming move LOAD-BEARING and PRESERVED VERBATIM in canonical ("The argument I have made here is not a partisan argument... The mechanism of cost severance operates regardless of whether the reader's political starting point is regulatory caution, market discipline, or worker solidarity... A center-right reader who values market efficiency should be at least as offended by cost severance as a center-left reader... A free-market system that does not price its costs is not a free-market system. It is a transfer mechanism."). §III pro-industrialization preemption at lines 27 + 29 preserved; §II Kennedy Mechanism-Not-Motive at line 19 preserved; §VII Purdue cultural-pathology rebuttal at lines 129–131 preserved. Condition-1-disarming PASS on skim-read. |
| **T2.9** | Coal-state Republican policy aide / Manchin-or-Justice-aligned reader | ✓✓ MODERATE-TO-STRONG INCLUDE | ✓✓ MODERATE-TO-STRONG INCLUDE | = | §III place-dignity preservation at lines 25 + 27 + 29; §V miner-agency + regional-organizing-tradition crediting at line 73 (UMWA + Black Lung Association 1968 wildcat strike + Miners for Democracy + Yablonski naming); §VII cultural-pathology rebuttal at lines 129–131; framework's regional-respect register held. **Note: MC-4 1968→1969 wildcat-strike date correction is absent from canonical; this is a Pass-3.1-equivalent fact-check finding NOT a Pass-3.3 acceptance finding; does not move this verdict.** |
| **T2.10** | Berggruen Prize / institutional-redesign reader | ✓✓ MODERATE INCLUDE | ✓✓ MODERATE INCLUDE | = | §V Mazzucato + Harvey lineage paragraph at line 71 positions framework within comp-cluster Berggruen ecosystem recognizes; §VIII line 155 architecture-not-yet-built closing (engineerable-architecture frame; diagnostic + actionable + structural-not-prescriptive); no prescriptive overreach per §VIII line 159 explicit disclaimer. |

**Tier 2 aggregate (Amendment-D HIGH weight): 6/6 INCLUDE; 1 STRONG + 3 MODERATE-TO-STRONG/MODERATE + 1 MILD + 0 EXCLUDE.**

### §2.3 Tier 3 — cultural-resonance + accessibility

| # | Character | LOCKED RATIFIED 2026-05-27 verdict | Canonical 2026-06-01 verdict | Δ | Verdict-driver evidence |
|---|---|---|---|---|---|
| **T3.11** | **McDowell County resident** — **HIGHEST-PRIORITY Tier 3 character** | ✓✓✓ STRONG INCLUDE (highest-priority Tier 3 dispositive; place-in-itself + regional-pride + cultural-pathology rebuttal triad) | ✓✓✓ STRONG INCLUDE | = | Place-in-itself before place-as-case-study at lines 25–29 §III preserved (town names; 1950 100,000-person peak; civic-life specifics; Golden Gate Bridge / Empire State Building / Pacific aircraft-carrier connection); regional-pride register at line 27 ("they had earned the wages and the respect they got") preserved; §V miner-agency + regional-organizing-tradition crediting at line 73 (UMWA + BLA + Miners for Democracy + Yablonski) preserved; §VII cultural-pathology rebuttal preserved; Bailey + Latusek named-subject treatment preserved; restrained Option B first-person at §I + §VIII preserved. **Verdict-source: LOCKED-internal triad mechanism; NOT HC-5 Tug Fork / HC-6 verifiable-geographic-fluency (which are absent from canonical per §0.2). LOCKED ✓✓✓ verdict source preserved fully; V-D's HC-5 reinforcement would have added verifiable-geographic-fluency gain but is not realized.** |
| **T3.12** | Skeptical Appalachian academic (Eller / Catte / Stoll / Caudill tradition) | ✓✓ MODERATE INCLUDE (with Pass 3.5 regional-scholarship-naming gain available) | ✓✓ MODERATE INCLUDE (with Pass 3.5 gain STILL OPEN) | = | Regional-organizing-tradition credit at line 73 §V preserved (UMWA + BLA 1968 wildcat strike + Miners for Democracy + Yablonski); regional-scholarship-lineage at register level via Catte named at line 73 ("Elizabeth Catte's *What You Are Getting Wrong About Appalachia*"); §VII cultural-pathology rebuttal preserved as Catte-tradition-consistent. **Pass 3.5 regional-scholarship-naming gain-flag (Caudill / Stoll / Eller naming) REMAINS OPEN: HC-1 Eller addition that would have lifted this verdict ✓✓ → ✓✓✓ per V1 + V2 audits is ABSENT from canonical per §0.2 premise correction. The verdict holds at LOCKED's ✓✓ — the upgrade path is identified but not realized.** |
| **T3.13** | Coates / Darity / Mullen / Hamilton lineage reader | ✓ MILD INCLUDE (low-load-bearing per brief) | ✓ MILD INCLUDE | = | Cross-extraction structural parallels at line 71 §V; §VIII line 155 architecture-not-yet-built closing; no explicit reparations-economics citation (consistent with brief disposition); cultural-engagement commitment implicit via cross-extraction case-walk + architecture-built register. |
| **T3.14** | General Harper's subscriber without policy expertise | ✓✓ MODERATE-TO-STRONG INCLUDE | ✓✓ MODERATE-TO-STRONG INCLUDE | = | Specialized terminology introduced with plain-prose definition (§V vocabulary section lines 59–69); concrete-dated-named institutional architecture throughout; no econ-domain jargon spikes; house-voice register held; Option B restrained first-person maintained. |
| **T3.15** | First-gen / working-class reader without prior framework knowledge | ✓✓ MODERATE-TO-STRONG INCLUDE | ✓✓ MODERATE-TO-STRONG INCLUDE | = | Bailey + Latusek named-miner voices at center of gravity (§IV lines 35–43; §VIII lines 149–151); no educated-elite register drift; §VIII line 159 explicit-meta disarming as honest-acknowledgment register; concrete numbers explained not just listed (line 47 "two-thirds of the total. In one year"). |
| **T3.16** | Environmental-justice movement reader (Cancer Alley / Bayou-Gulf / Appalachian-mining-advocacy / Just Transition register) | ✓✓ MODERATE-TO-STRONG INCLUDE (Yes-vote dispositive test PASS) | ✓✓ MODERATE-TO-STRONG INCLUDE | = | Extraction-affected communities as full agents (line 73 organized/struck/sued/lobbied/testified/died framing); §VII Purdue rebuttal as institutional-architecture-failure (lines 129–131; "structural pattern... wherever the conditions are available"); §I orange-creek imagery at line 5 + §VIII spatial-cost-severance framing at line 141. Yes-vote dispositive test PASS. |

**Tier 3 aggregate (Amendment-D HIGH weight): 6/6 INCLUDE; 1 STRONG + 4 MODERATE-TO-STRONG/MODERATE + 1 MILD + 0 EXCLUDE.**

---

## §3. Aggregate tally + canonical-vs-LOCKED comparison

### §3.1 Aggregate verdict

**Canonical essay.md 2026-06-01 Pass 3.3 light-refire verdict: 16/16 INCLUDE; 0 NEUTRAL; 0 EXCLUDE.**

| Verdict band | LOCKED 2026-05-27 | Canonical 2026-06-01 | Δ |
|---|---|---|---|
| ✓✓✓ STRONG INCLUDE | 5 (T1.1 + T1.3 + T1.4 + T2.8 + T3.11) | 5 (same) | = |
| ✓✓ MODERATE-TO-STRONG / MODERATE INCLUDE | 8 (T1.2 + T2.5 + T2.7 + T2.9 + T2.10 + T3.14 + T3.15 + T3.16) | 8 (same) | = |
| ✓✓ MODERATE INCLUDE (with open Pass 3.5 gain-flag) | 1 (T3.12) | 1 (same; gain-flag STILL OPEN) | = |
| ✓ MILD INCLUDE | 2 (T2.6 + T3.13) | 2 (same) | = |
| EXCLUDE / NEUTRAL | 0 | 0 | = |

**Total: 5 ✓✓✓ + 8 ✓✓ + 1 ✓✓-with-gain-flag + 2 ✓ + 0 EXCLUDE = 16/16 INCLUDE; 0 EXCLUDE.**

### §3.2 Prompt-scope verification

| Prompt-scope verification | Status |
|---|---|
| **(1) All 16 INCLUDE preserved at LOCKED-baseline-or-better levels** | ✅ **PASS.** 16/16 INCLUDE preserved at LOCKED levels exactly (canonical-equals-LOCKED state per §0.2 premise correction); zero downgrades; zero EXCLUDE; zero NEUTRAL. |
| **(2) T3.12 ✓✓✓ upgrade preserved (HC-1 Eller closes Pass 3.3 RATIFIED gain-flag)** | ⚠️ **CANNOT BE CONFIRMED AS FRAMED.** T3.12 remains at LOCKED's ✓✓ MODERATE INCLUDE with Pass-3.5 regional-scholarship-lineage-naming gain-flag STILL OPEN. The ✓✓ → ✓✓✓ upgrade pathway via HC-1 Eller addition (V-D parallel-draft mechanism per V1 audit 2026-05-28 §T3.12; V2 audit 2026-05-28 §T3.12) is NOT realized in canonical essay.md per §0.2 premise verification. **The verdict has not regressed** — LOCKED's ✓✓ verdict source is intact — but the prompt-anticipated upgrade is not present. |
| **(3) T3.11 ✓✓✓ McDowell-resident dispositive verdict preserved (HC-5 Tug Fork + HC-6 light-fix verifiable-fluency)** | ⚠️ **PARTIALLY CONFIRMED.** T3.11 ✓✓✓ STRONG INCLUDE verdict IS preserved — but via LOCKED's place-in-itself + regional-pride + cultural-pathology rebuttal triad mechanism, NOT via HC-5 Tug Fork or HC-6 three-rivers verifiable-geographic-fluency reinforcement (which are absent from canonical per §0.2). The LOCKED verdict-source is intact; the V-D-route verifiable-geographic-fluency gain is not realized. |
| **(4) All Tier 1 4/4 ✓✓✓ preserved** | ⚠️ **PARTIALLY CONFIRMED with terminology note.** Per the prompt's framing of "all Tier 1 4/4 ✓✓✓": at LOCKED RATIFIED 2026-05-27, T1.2 Harper's reader was recorded at **moderate-to-strong** (per LOCKED Pass 3.3 §2.1 #2 "Verdict: ✅ INCLUDE (moderate-to-strong)"), not at strong ✓✓✓. The LOCKED baseline Tier 1 was 3 ✓✓✓ + 1 ✓✓ (moderate-to-strong). This matches canonical exactly. **The "Tier 1 4/4 ✓✓✓" framing in the prompt over-states the LOCKED baseline by 1; canonical exactly matches LOCKED.** No regression at Tier 1; verdict preserved at LOCKED level. |
| **(5) No new EXCLUDE risk from canonical-promotion state change** | ✅ **PASS.** Zero EXCLUDE; zero NEUTRAL; no new EXCLUDE risk identified. Canonical state is identical to LOCKED state per §0.2 (no V-D promotion actually applied); no state-change-induced risk to verify. The HC-6 Levisa-Fork verification light-fix flag from V1 + V2 audits is not present as a risk in canonical (HC-6 itself is absent). |

### §3.3 Light-refire decision

**Verdict: PASS — canonical-equals-LOCKED state holds Pass 3.3 RATIFIED 2026-05-27 verdicts intact under Amendment D HIGH-weight face-value evaluation.**

The canonical essay.md preserves the LOCKED 16/16 INCLUDE pattern exactly. Under Amendment D's essay-artifact-class HIGH-weight face-value evaluation rule (all 16 audiences at HIGH weight; no projection-lens downgrade), no character verdict moves from its LOCKED state.

**Two prompt-anticipated verifications (T3.12 ↑✓✓✓; T3.11 HC-5/HC-6 reinforcement) cannot be confirmed because the underlying V-D hybridization mechanisms are absent from canonical** — see §0.2 premise verification. This does not affect the aggregate PASS (verdict-source mechanism for both characters preserved at LOCKED level), but it does flag a downstream-framing reconciliation need (§6 below).

---

## §4. Non-partisan-framing audit (CONDITION-1 dispositive carry-forward)

Per LOCKED Pass 3.3 RATIFIED §5 + brief §16 hard constraint: highest-risk passages re-verified in canonical state.

| Highest-risk passage | LOCKED verdict | Canonical verdict | State |
|---|---|---|---|
| §II Kennedy framing (line 19 "He had the wrong defendant") | PASS (Mechanism-Not-Motive preserved) | PASS | Preserved verbatim |
| §V Mazzucato + Harvey lineage paragraph (line 71) | PASS (no tribal-tradition coding; Marx-and-non-Marx-traditions-converging) | PASS | Preserved verbatim |
| §VII Purdue cultural-pathology rebuttal (lines 129–131) | PASS (substantive regional-dignity defense, not anti-pharmaceutical brief) | PASS | Preserved verbatim |
| §VIII line 159 explicit-meta Condition-1-disarming move | PASS ($100 Barrel 2026-05-21 anchor; skim-read PASS) | PASS | Preserved verbatim |

**Non-partisan-framing aggregate verdict: ✅ PASS** under Amendment D HIGH-weight face-value evaluation. All four load-bearing passages preserved.

---

## §5. Apparatus-reveal cap verification (~18–22% per brief §8 + Stage 0 ratified cap)

Per LOCKED Pass 3.3 RATIFIED §4. Canonical state-equals-LOCKED state per §0.2; apparatus-reveal counts unchanged.

| Named-OK term | LOCKED surface count | Canonical surface count | Δ |
|---|---|---|---|
| *cost severance* | 7 | 7 | = |
| *severed cost* | 1 | 1 | = |
| *value extraction* | 2 | 2 | = |
| *accumulation by dispossession* | 1 | 1 | = |
| *spatial cost severance* | 1 | 1 | = |
| EXCLUDED apparatus body-prose hits | 0 across all 16 EXCLUDED items | 0 | = |

**Effective-reveal essay-level: ~18–22% (at-cap; cap met).** ✅ PASS — canonical preserves LOCKED apparatus discipline exactly.

---

## §6. Forward-flag inventory (light re-fire output)

### §6.1 Critical premise-reconciliation flag (§0.2 carry-forward)

**HIGH-severity premise-reconciliation finding:** the prompt's "canonical V-D state post-V-D-promotion (commit `0045952`)" framing does not match the actual canonical essay.md state, which preserves LOCKED Stage-5-RATIFIED 2026-05-27 content (7,121w; HC-1 through HC-6 + MC-4 all absent). Two paths for resolution; author-decision required:

**Path A — Apply V-D hybridization to canonical** (realizes the T3.12 ↑✓✓✓ + T3.11 verifiable-geographic-fluency gains the prompt anticipates):
1. Pass-3.1-equivalent prose-modifying spot-fix pass applying HC-1 through HC-6 + MC-4 to canonical essay.md per V1 + V2 audit recommendations.
2. HC-6 Levisa-Fork geographic verification light-fix included (per V1 audit §T3.11 MEDIUM-severity flag — verify Levisa-Fork-feeding-tributaries claim against USGS hydrography / WV DNR watershed maps; clean-fix paths available if claim unsubstantiated: substitute "feed into the Tug and the upper Guyandotte" OR "drain southward toward the Tug Fork and the Big Sandy").
3. Light Pass 3.3 re-fire of T3.11 + T3.12 after spot-fixes applied to verify expected upgrades realize.

**Path B — Correct downstream framing** (acknowledges V-D was archived, not promoted):
1. Update downstream-session handoff artifacts that reference "V-D-promotion" / "post-V-D-promotion" to reference "LOCKED preserved at canonical; V-D hybridization deferred or declined" so future sessions don't inherit the framing mismatch.
2. T3.12 ✓✓ Pass-3.5 regional-scholarship-naming gain-flag explicitly remains OPEN as a known-defer item; submission proceeds at LOCKED ✓✓.

### §6.2 LOCKED Pass 3.3 RATIFIED forward-flags (re-affirmed)

Per LOCKED Pass 3.3 §6 inventory; status carry-forward:

1. **§V regional-scholarship-lineage naming (Caudill / Catte / Stoll) — Pass 3.5 restoration-polarity gain-flag** — REMAINS OPEN. Path A above would close via HC-1 Eller addition. Catte is named in canonical at line 73; Caudill / Stoll / Eller naming would lift T1.2 + T3.12 to strong.
2. **§I opening scene density possible restoration site** — Pass 3.5 forward-flag; status unchanged.
3. **§IV Bailey scene-anchor density possible Pass 3.5 restoration site** — Pass 3.5 forward-flag; status unchanged.
4. **§VII Purdue scene-anchor / Hamby acknowledgment expansion** — Pass 3.5 forward-flag; status unchanged.
5. **§VIII closing-sentence cadence (line 163 motif reprise)** — Pass 3.5 forward-flag; status unchanged.
6. **First-person frame balance at §I + §VIII** — Pass 3.5 forward-flag; status unchanged.

### §6.3 Amendment D §0.5 brief-text reconciliation flag

Per §1 above: the in-repo `stage-1-brief.md` (last commit on this worktree) does not contain a §0.5 Amendment-D-classification section. Either (a) the retroactive §0.5 update has been applied to a parallel-session worktree and has not yet merged to main this worktree was created from, OR (b) the §0.5 update is forthcoming. Audit proceeds against canonical Amendment D worked-examples-table specification (essay artifact-class → all 16 at HIGH); §0.5 brief-text-reconciliation deferred to ratification + reconciliation session.

### §6.4 Sandbox-blocked worktree-isolation + auto-merge action

Per §0.1: the mandatory worktree-isolation step and the merge-on-ratification scaffolding auto-merge action could not execute in this sandbox (bash denied). The artifact lands in `publishing/essays/harpers-the-miner/rigor/`; commit + push to canonical defer to a follow-on session with bash permission, OR author manual `git add + commit + push` per the CLAUDE.md merge-on-ratification scaffolding auto-merge default.

---

## §7. Status + next-pass anchor + end-of-session one-liner

### §7.1 Summary verdict

**Pass 3.3 canonical light re-fire: PASS — 0 spot-fixes required (acceptance polarity).** All 16 acceptance characters across Tier 1 + Tier 2 + Tier 3 INCLUDE under Amendment D HIGH-weight face-value evaluation; cumulative-portfolio effective-reveal at ~18–22% Stage 0 cap (preserved from LOCKED); non-partisan-framing audit PASS via §VIII line 159 explicit-meta disarming move preserved verbatim. No submission-blocking acceptance findings.

| Disposition | Count |
|---|---|
| ✓✓✓ STRONG INCLUDE | 5 (T1.1 + T1.3 + T1.4 + T2.8 + T3.11) |
| ✓✓ MODERATE-TO-STRONG / MODERATE INCLUDE | 8 |
| ✓✓ MODERATE INCLUDE (Pass 3.5 gain-flag open) | 1 (T3.12) |
| ✓ MILD INCLUDE | 2 (T2.6 + T3.13) |
| EXCLUDE / NEUTRAL | 0 |
| HIGH-severity premise-reconciliation findings | 1 (§6.1 — canonical-vs-V-D state mismatch) |
| MEDIUM-severity findings | 0 |
| LOW-severity / process flags | 2 (§6.3 §0.5 brief-text; §6.4 sandbox-blocked merge action) |

**Anchor commits:**
- Stage 1 brief RATIFIED: origin/main commit `be87926` (2026-05-27).
- LOCKED Stage-5-RATIFIED essay.md: 2026-05-27 (referenced as content-equivalent canonical state).
- Canonical essay.md HEAD (this worktree): per task brief commit `0045952` 2026-06-01 (content matches LOCKED per §0.2).
- V-D parallel draft (hybridized; NOT promoted to canonical per §0.2): `publishing/essays/harpers-the-miner/_archive/parallel-drafts_2026-05-28/ch2-harpers-essay_hybrid_best-of-both.md` 7,211w.
- V1 audit RATIFIED 2026-05-28: `pass-3-3-and-3-4-bundled-audience-load_VERSION-D_INDEPENDENT-AUDIT_2026-05-28.md`.
- V2 audit RATIFIED 2026-05-28: `pass-3-3-3-4-3-5-bundled_VERSION-D_INDEPENDENT-AUDIT-V2_2026-05-28.md`.

### §7.2 Next-pass anchor

After this light re-fire PROPOSED lands + parent session ratifies + author selects Path A (apply V-D) or Path B (correct framing) per §6.1:

- **Path A:** prose-modifying spot-fix pass applies HC-1 through HC-6 + MC-4 to canonical essay.md; HC-6 Levisa-Fork geographic verification light-fix included; light Pass 3.3 re-fire of T3.11 + T3.12 verifies the expected ✓✓✓ upgrades realize.
- **Path B:** downstream-handoff artifacts updated to reference LOCKED canonical state; T3.12 Pass-3.5 regional-scholarship-naming gain-flag explicitly remains OPEN; submission proceeds at LOCKED 16/16 INCLUDE at the LOCKED's verdict bands (3 STRONG + 1 MODERATE-TO-STRONG Tier 1; 1 STRONG + 5 MODERATE Tier 2; 1 STRONG + 4 MODERATE + 1 MILD Tier 3).

Either path preserves the LOCKED 16/16 INCLUDE submission-readiness; Path A realizes the V1 + V2 audits' anticipated T3.12 ✓✓ → ✓✓✓ + T3.11 verifiable-geographic-fluency gains. Harper's submission window target Q4 2026 (Oct–Nov per cascade plan v2 §3 Phase 2-β); either path is within window.

### §7.3 End-of-session one-liner

```
STATE: ch2-harpers-pass-3-3-canonical-V-D-light-refire PASS
(aggregate: 16 INCLUDE / 0 EXCLUDE / 0 NEUTRAL under Amendment D
HIGH-weight face-value evaluation; LOCKED 2026-05-27 RATIFIED
verdicts preserved exactly); CRITICAL FINDING: canonical
essay.md state at commit 0045952 2026-06-01 matches LOCKED
content exactly (7,121w; 0 HC-1/HC-3/HC-4/HC-5/HC-6 inserts;
1968 wildcat-strike not corrected to 1969 per MC-4) — the
prompt's "post-V-D-promotion" premise does NOT match the
actual file state; prompt-anticipated T3.12 ✓✓ → ✓✓✓
upgrade via HC-1 Eller + T3.11 HC-5 Tug Fork verifiable-
fluency reinforcement are NOT realized because the underlying
V-D hybridization is absent from canonical; NEXT: author
selects Path A (apply V-D hybridization to canonical per
V1 + V2 audit recommendations) OR Path B (correct downstream-
framing handoffs to reference LOCKED-preserved canonical
state); both paths preserve LOCKED 16/16 INCLUDE submission
readiness; AWAITING: (1) author ratification of light-refire
PASS verdict + premise-reconciliation path selection; (2)
sandbox-blocked worktree-isolation + auto-merge action
defer to follow-on session with bash permission OR author
manual git add + commit + push per merge-on-ratification
scaffolding default; (3) Stage 1 brief §0.5 Amendment-D-
classification text reconciliation (per §6.3 flag) if not
already applied parallel-session.
```

---

*End of Pass 3.3 light-refire artifact for Ch 2 *The Miner* → Harper's Magazine derivative essay — canonical essay.md state PROPOSED 2026-06-01.*
