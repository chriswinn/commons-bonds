# McDowell op-ed — Post-audit triage on 2026-06-01 ratified bundle execution

**Date:** 2026-06-02
**Author:** parent session
**Status:** PROPOSED for author ratification on the spot-fix bundle in §6
**Supersedes-in-part:** Workstream A audit (stale-cwd false-negative); Workstream C audit foundational claim (stale-cwd false-negative); part of Workstream C M2 finding (Amendment D source doctrine claim false)
**Preserves:** Workstream A/B/C/D audit artifacts as historical record with correction overlays per §§1-5

---

## §0. Why this triage exists

The 2026-06-01 ratified bundle spawned four parallel verification audit chips (one per workstream) after the author flagged that the original ratification omitted audit-on-execution. The chips returned with verdicts that require careful triage because **three of four audit chips read STALE local working-tree state** at `/Users/c17n/commons-bonds/` rather than reflecting `origin/main` content.

### §0.1 The stale-cwd false-negative mechanism

Audit chips have Read access to `/Users/c17n/commons-bonds/` but not to parent-session worktrees. The canonical cwd at `/Users/c17n/commons-bonds/` is shared across all parallel sessions (per the SessionStart worktree-isolation warning) and accumulates stale local-HEAD state when sessions push to `origin/main` from their own worktrees without pulling-back into the canonical cwd. At audit time (2026-06-01 evening), canonical cwd local HEAD was at `851b368` (a "Git cleanup sweep — Round 2 Phase C" commit) whereas `origin/main` was at `c1ad8e8` (post-bundle state).

Audit chips reading from canonical cwd see whatever the canonical cwd's local working tree contains, NOT what's on `origin/main`. For artifacts that were committed + pushed by the parent session but not pulled into canonical cwd, the chips see absence-of-content where there should be content. Three of four chips reported "REVERT-AND-REWORK" verdicts on this basis. Re-verification against `origin/main` content (via `git show origin/main:...`) confirms the parent session's commits ARE on `origin/main` and the artifacts ARE present.

### §0.2 Three audit chips affected; one chip's findings are net-real

| Chip | Foundational verdict | Stale-state false-negative? | Substantive findings status |
|---|---|---|---|
| **A** (commit `189f42b` execution audit) | REVERT-AND-REWORK | **YES — false negative.** V-D content + LOCKED archive + README all correctly on `origin/main` per `git show origin/main:...` | No real findings beyond stale-state misread |
| **B** (commit `39eae8a` WVBLA inventory fact-check) | SPOT-FIX-AND-RATIFY | NO — chip used WebSearch independent of cwd state for fact-checking; chip verified Harper's essay.md content (unchanged by my workstreams) | **4 MEDIUM real findings + 2 LOW Harper's-side findings** — substantive web-verification work; spot-fix bundle proposed in §6 |
| **C** (commit `1f64da1` Amendment-D addendum audit) | REVERT-AND-REWORK | **YES — false negative on §9 absence claim.** §9 IS on `origin/main` at line 874+; Amendment D IS in source doctrine at `audience-pressure-test-construction.md` line 22 | **1 MEDIUM real finding** (artifact-class misclassification of Tier 2 + Tier 3 in §9) + 1 LOW (Aeon retroactive reclassification framing) |
| **D** (V-D-tight pre-draft + audit) | READY-TO-SHIP-AT-PRIMARY-BAND-WITH-EDITOR-ACKNOWLEDGED-OVERAGE | NO — chip wrote new artifact (didn't depend on cwd state being current for its own audit) | **Substantive finding:** V-D-tight = ~993w not 900w; substrate-density floor hit; per-venue routing strategy needed |

### §0.3 Systemic note

This is a discipline-relevant pattern. Parallel-session-volume reality (per `tools/memory/feedback_worktree_isolation_for_parallel_sessions.md`) means the canonical cwd is NEVER reliably current with `origin/main`. Future audit chips that read from canonical cwd must be instructed to either:
- (a) Verify their reads against `origin/main` via `git show origin/main:...` (requires Bash)
- (b) Skip reads that depend on current cwd state + use only commit-state-independent verifications
- (c) Be run from a freshly-isolated worktree where local HEAD matches `origin/main` (but sub-agents can't Read worktree paths)

**Recommendation:** treat audit-chip "REVERT-AND-REWORK" verdicts as flagged-for-cwd-staleness-verification by default. Parent session must verify the foundational claim against `origin/main` before treating chip findings as authoritative.

---

## §1. Workstream A — Canonical swap (commit `189f42b`)

### §1.1 Chip verdict (as-filed)

REVERT-AND-REWORK. Chip claimed body byte-equality FAIL + LOCKED archive missing + README not updated.

### §1.2 Triage finding

**FALSE NEGATIVE due to stale-cwd read.** Verified against `origin/main`:

```
$ git show origin/main:publishing/op-eds/mcdowell-county-true-cost/op-ed.md | head -25
# What a Ton of Coal Actually Cost
**Pipeline draft — opportunistic-submission readiness, not deadline-driven.**
**Created:** 2026-05-10 (LOCKED) → **2026-06-01 (V-D HYBRID promoted to canonical...)**
[full V-D body content follows]
```

LOCKED archive verified present at `_archive/prior-versions/mcdowell-op-ed_LOCKED-2026-05-10.md` on `origin/main`. README V-D-canonical-status text verified present.

### §1.3 Real findings

None. Workstream A execution is clean on `origin/main`.

### §1.4 Action

No action required. Chip artifact retained as historical record with this triage overlay documenting the stale-cwd false-negative. Future audit chips on similar internal-scaffolding execution should be instructed to verify against `origin/main` (not local cwd).

---

## §2. Workstream B — WVBLA inventory fix (commit `39eae8a`)

### §2.1 Chip verdict (as-filed)

SPOT-FIX-AND-RATIFY. Chip identified 4 MEDIUM hard-rule exposures + 2 LOW Harper's-side findings + verified the fix is net-positive (Harper's alignment + parenthetical nuance preservation + no portfolio regression risk).

### §2.2 Triage finding

**VALID** — chip's web-verification work is independent of cwd staleness. Chip verified:
- §1 Harper's lines 37 + 73 do contain "BLA led" framing (read Harper's essay.md which is unchanged by my workstreams)
- §2-§7 used WebSearch across 10+ authoritative sources (WV Encyclopedia, Clio, Zinn Education Project, Southern Spaces, Activist History Review, UMWA Journal, MSHA, Wikipedia, WV Public Broadcasting, Hamby book reviews)

### §2.3 Real findings

| ID | Severity | Issue |
|---|---|---|
| MED-1 | MEDIUM | Hamby attribution unverifiable. Hamby's *Soul Full of Coal Dust* is centrally about Gary Fox + John Cline (modern resurgence), not 1969 movement origins. Reviews don't confirm Hamby's specific framing on the BLA-led-vs-parallel-causal question. The parent session's "Hamby supports umbrella reading" claim cannot be verified from accessible sources. |
| MED-2 | MEDIUM | Founding date imprecision. The parent session's "early 1969" is partially defensible (formal Beckley-rally intro) but the dominant historical record cites **December 1968 in Montgomery, WV** as the founding event. |
| MED-3 | MEDIUM | HB1 designation unconfirmed. The bill signed by Gov. Arch Moore on March 11, 1969 is verified but the "HB1" bill-designation specifically is not independently confirmed in the chip's source pool. |
| MED-4 | MEDIUM | Physicians Committee (Donald Rasmussen / Isidore Buff / I.E. Buff / Hawey "Wells") is a notable omission from the parent session's founders list. The Physicians Committee was the parallel medical-side organization that gave the movement its medical-credibility anchor. |
| LOW-1 | LOW | Harper's line 73 says "1968 wildcat strike" but the strike was Feb-Mar 1969. **This is a Harper's-side issue, not Workstream B.** Forward-flag for separate Harper's spot-fix consideration. |
| LOW-2 | LOW | Harper's line 37 BLA-led simplification — minor framing concern; mostly defensible. |

### §2.4 Proposed spot-fix bundle (FOR AUTHOR RATIFICATION; substrate-safe per chip's verification)

Apply to `publishing/op-eds/_shared/canonical-facts/norway-mcdowell-inventory_2026-05-10.md` phrasing-precision note:

- **SF-B1 (MED-1 Hamby softening):** Change "Historically defensible per Hamby's *Soul Full of Coal Dust* + standard coal-history scholarship" → "Historically defensible per multi-source consensus across regional-labor-history scholarship (WV Encyclopedia; Activist History Review; UMWA Journal historical record; cf. Hamby's *Soul Full of Coal Dust* for 21st-century resurgence context — Hamby does not centrally address 1969 movement origins)."
- **SF-B2 (MED-2 founding date):** Change "WVBLA formed early 1969 — Brooks/Miller/Mullins" → "WVBLA formed **December 1968 in Montgomery, WV** (founders include Charles Brooks; Woodrow Mullins; physicians Donald Rasmussen / I.E. Buff / Hawey Wells via the parallel Physicians Committee; Arnold Miller joined as early organizer, elected WVBLA president 1970)."
- **SF-B3 (MED-3 HB1):** Change "WV HB1 signed by Gov. Moore March 1969" → "the WV black-lung compensation bill signed by Gov. Arch Moore on March 11, 1969" (drops the unverified HB1 designation; preserves date + signatory which ARE verified).
- **SF-B4 (MED-4 Physicians Committee):** Incorporated into SF-B2 above.

**LOW findings (LOW-1 + LOW-2):** Forward-flagged for separate Harper's spot-fix consideration; not Workstream B scope.

### §2.5 Action

**PROPOSE TO AUTHOR for ratification.** Spot-fix bundle SF-B1 through SF-B3 is substrate-safe per chip's web-verification + applies to internal-scaffolding inventory. Pending author ratification.

---

## §3. Workstream C — Amendment-D retroactive weighting addendum §9 (commit `1f64da1`)

### §3.1 Chip verdict (as-filed)

REVERT-AND-REWORK based on §9 absence + Amendment D content absence in source doctrine + 1 MEDIUM artifact-class misclassification finding + 1 LOW Aeon retroactive reclassification framing.

### §3.2 Triage finding (per chip claim)

| Chip claim | Triage verdict | Evidence |
|---|---|---|
| **§9 absent from canonical-path file** | **FALSE NEGATIVE — stale-cwd read.** §9 IS on `origin/main` at line 874+ | `git show origin/main:.../mcdowell-op-ed_VERSION-D_FRESH-THREE-PASS-INDEPENDENT-AUDIT_2026-05-28.md \| grep -nE "(## §9\|Reception-chain)"` returns: 874 §9 + 878 §9.1 + 888 §9.2 + 904 §9.3 + 918 §9.4 + 934 §9.5 |
| **§9.M1 Artifact-class misclassification of Tier 2 + Tier 3** | **VALID — real finding.** Worked-examples table at `tools/drafting-templates/audience-pressure-test-construction.md` line 36 specifies end-reader-facing op-ed prose has "All theoretical audiences per Stage 1 brief — they ARE the direct readers" with "(none; the buck stops here)" for consultants. My §9.3 classification of T2.1/T2.2/T2.3 as MEDIUM-to-LOW projected-downstream + T3.1/T3.2 as LOW projected-downstream does NOT match the worked-examples table | Direct cross-check against worked-examples table |
| **§9.M2 Source doctrine v3.0-labeled with 0 Amendment D content** | **FALSE — Amendment D IS in source doctrine.** v3.0 title label is stale (file title not updated to v3.1) but Amendment D section is at line 22 of `audience-pressure-test-construction.md` | `git show origin/main:tools/drafting-templates/audience-pressure-test-construction.md \| grep -nE "(Amendment D\|Reception-chain)"` returns: 22 + 70 |
| **§9.L1 Aeon empirical anchor retroactive reclassification** | **MINOR framing concern.** Aeon Option E.2 γ.1 audit at commit `73c5764` does not self-identify as "Amendment-D worked example" — the parent session retrofitted that framing. But Amendment D's source doctrine cites it as the empirical anchor (lines 68-70 of `audience-pressure-test-construction.md`), so the connection is real even if the "worked example" labeling is parent-session retrofit | Defensible-but-imprecise framing |

### §3.3 §9 supersession plan (§10 of fresh-chip audit; added by this triage)

Per §3.2 findings, §9 of the fresh-chip audit requires correction. Specifically:
1. Reclassify T2.1/T2.2/T2.3 specialists + T3.1/T3.2 cultural-resonance + T3.3 general-subscriber as HIGH-direct per worked-examples-table (end-reader-facing op-ed prose → all theoretical audiences ARE direct readers).
2. Refine the SHIP-strengthening claim: under correct weighting, Amendment-D weighting effectively COLLAPSES to unweighted aggregate for this artifact class (all 9 characters are direct), so the "Amendment-D weighting strengthens the SHIP recommendation" claim was over-stated. The SHIP recommendation holds independently of Amendment-D weighting.
3. Acknowledge §9's misclassification did not affect the substantive verdict (3 ✓✓✓ + 6 ✓✓ + 0 EXCLUDE under any weighting); only the rhetorical framing of "weighting strengthens" was wrong.
4. Preserve §9 in-place for audit-trail; add §10 superseding §9 with corrected analysis.

### §3.4 Action

**APPLY §10 correction to fresh-chip audit myself** (internal-scaffolding correction of my own §9 addendum; substrate-safe analytical work; no new prose generation about named subjects). See §10 of `mcdowell-op-ed_VERSION-D_FRESH-THREE-PASS-INDEPENDENT-AUDIT_2026-05-28.md` after this triage commits.

---

## §4. Workstream D — V-D-primary-band-tight pre-draft + audit

### §4.1 Chip verdict (as-filed)

READY-TO-SHIP-AT-PRIMARY-BAND-WITH-EDITOR-ACKNOWLEDGED-OVERAGE. V-D-tight = ~993w (from V-D HYBRID 1,029w; −36w). All four pass verdicts wash vs V-D HYBRID baseline. Substrate-safe trim floor reached at ~993w.

### §4.2 Triage finding

**VALID** — chip's audit is independent of cwd state; it audited prose it wrote itself. Key finding load-bearing:

> "V-D HYBRID's substantive-density floor at the audited Pass 3.3 / 3.4 / 3.5 verdict set is ~993w. The ~93w gap to 900w-band-ceiling cannot be closed substrate-safely without material content cuts that degrade Pass 3.3 Tier-1 gating verdicts."

### §4.3 Per-venue routing implications

| Venue | Word band | V-D HYBRID (1,029w) | V-D-tight (993w) | Recommended |
|---|---|---|---|---|
| Bloomberg Opinion | ~1,000w practical ceiling | borderline | fits cleanly | **V-D-tight** |
| Project Syndicate | ~700-900w preferred (with overage tolerated) | over | upper-band overage | **V-D-tight with editor-acknowledged overage** |
| FT Opinion | ~800-900w hard | over | over | **Neither fits substrate-safely.** Either pivot venue OR author-authorize deeper trim with Pass 3.3 verdict softening |
| NYT/WaPo/Guardian Long Read | 900-1,100w | preferred | acceptable | **V-D HYBRID preferred** |

### §4.4 Action

**PROPOSE TO AUTHOR for ratification** on:
- (D1) Ratify V-D-tight as ready-for-submission at Bloomberg + Project Syndicate band (993w; editor-acknowledged overage acceptable).
- (D2) Keep V-D HYBRID as canonical for NYT/WaPo/Guardian stretch.
- (D3) Defer FT Opinion path — requires separate decision: either drop FT from venue list OR author-authorize a deeper-trim variant with explicit verdict-softening + new audit.

Update README at-activation guidance to reflect the per-venue routing.

---

## §5. Stale-cwd discipline forward-flag

The systemic finding from §0 deserves codification. Recommend adding to `tools/memory/feedback_worktree_isolation_for_parallel_sessions.md` a new sub-section: **"Stale-cwd read risk for sub-agent audits."** Sub-agents reading from canonical cwd see stale-HEAD content; verdicts based on "content X is missing from file Y" should be flagged for parent-session verification against `origin/main` before being treated as authoritative.

**Action:** PROPOSE TO AUTHOR for memory-entry update.

---

## §6. Spot-fix bundle (FOR AUTHOR RATIFICATION)

Bundle for author ratification (substrate-safety verified per chip findings + cross-checks):

| ID | Source | Description | Substrate-safety | Cost |
|---|---|---|---|---|
| **SF-B1** | B audit MED-1 | Hamby softening to multi-source consensus | substrate-safe (multi-source verified) | ~25w |
| **SF-B2** | B audit MED-2 + MED-4 | Founding date to Dec 1968 Montgomery WV + Physicians Committee addition | substrate-safe (web-verified across 10+ sources) | ~20w |
| **SF-B3** | B audit MED-3 | Drop unverified HB1 bill designation; keep verified date + signatory | substrate-safe (subtraction only) | −3w |
| **§10** | C audit M1 | §9 supersession with corrected reception-chain classification | substrate-safe (analytical correction of own §9; no new biographical/scene/quote/motivation/etc.) | new section added; original §9 preserved |
| **D1** | D audit | Ratify V-D-tight for Bloomberg + Project Syndicate band | already audited clean | shipping decision |
| **D2** | D audit | Keep V-D HYBRID for NYT/WaPo/Guardian | no change | shipping decision |
| **D3** | D audit | Defer FT Opinion path (separate decision needed) | no change | shipping decision |
| **README-update** | D triage | Update README at-activation guidance for per-venue routing | substrate-safe | ~30w added |
| **Memory entry** | §5 triage | Codify stale-cwd discipline forward-flag in `feedback_worktree_isolation_for_parallel_sessions.md` | substrate-safe | new sub-section ~100w |

§10 + audit-artifact filing are applied by this triage commit (internal-scaffolding corrections of my own work; substrate-safe). SF-B1/B2/B3 + D1/D2/D3 + README-update + memory-entry-update are PROPOSED for author ratification.

---

## §7. State one-liner

```
STATE: mcdowell-op-ed-2026-06-01-bundle-post-audit-triage PROPOSED 2026-06-02
(3-of-4 chips stale-cwd-false-negative on foundational verdicts;
chip B's web-verification findings real → 3 MED inventory spot-fixes proposed;
chip C M1 finding real → §9 reclassification applied as §10 supersession;
chip D substrate-density-floor finding real → per-venue routing proposed);
NEXT: author-ratification on spot-fix bundle §6 (SF-B1/B2/B3 + D1/D2/D3 + README + memory);
AWAITING: author-ratification
```

---

## §8. Cross-references

- A audit artifact (as-filed; foundational verdict stale-cwd-false-negative): [`mcdowell-op-ed_WORKSTREAM-A-EXECUTION-AUDIT_2026-06-01.md`](mcdowell-op-ed_WORKSTREAM-A-EXECUTION-AUDIT_2026-06-01.md)
- B audit artifact (as-filed; substantive web-verification findings real): [`../../../_shared/canonical-facts/_audit/wvbla-inventory-fix-fact-check_2026-06-01.md`](../../../_shared/canonical-facts/_audit/wvbla-inventory-fix-fact-check_2026-06-01.md)
- C audit artifact (as-filed; foundational verdict stale-cwd-false-negative; M1 finding real): [`mcdowell-op-ed_WORKSTREAM-C-AMENDMENT-D-ADDENDUM-AUDIT_2026-06-01.md`](mcdowell-op-ed_WORKSTREAM-C-AMENDMENT-D-ADDENDUM-AUDIT_2026-06-01.md)
- D V-D-tight draft: [`../news-peg-activation-pre-draft/mcdowell-op-ed_V-D-primary-band-tight_750-900w_2026-06-01.md`](../news-peg-activation-pre-draft/mcdowell-op-ed_V-D-primary-band-tight_750-900w_2026-06-01.md)
- D V-D-tight audit: [`mcdowell-op-ed_VERSION-D-TIGHT_FRESH-AUDIT_2026-06-01.md`](mcdowell-op-ed_VERSION-D-TIGHT_FRESH-AUDIT_2026-06-01.md)
- Fresh-chip V-D audit (will receive §10 supersession at next commit): [`mcdowell-op-ed_VERSION-D_FRESH-THREE-PASS-INDEPENDENT-AUDIT_2026-05-28.md`](mcdowell-op-ed_VERSION-D_FRESH-THREE-PASS-INDEPENDENT-AUDIT_2026-05-28.md)
- 2026-06-01 ratified bundle commits: `189f42b` (A) + `39eae8a` (B) + `1f64da1` (C); D chip artifacts pending commit
- Amendment D source doctrine: `tools/drafting-templates/audience-pressure-test-construction.md` §"Reception-chain audience weighting" (line 22)
- Worked-examples table reference (load-bearing for C M1 finding): `tools/drafting-templates/audience-pressure-test-construction.md` §"Artifact-class worked examples" (line 32+)
- Worktree-isolation discipline: `tools/memory/feedback_worktree_isolation_for_parallel_sessions.md`

---

*End of post-audit triage on 2026-06-01 McDowell op-ed ratified bundle. Per merge-on-ratification, this internal-scaffolding artifact auto-merges to main. Spot-fix bundle §6 awaits author ratification.*
