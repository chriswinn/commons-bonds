# Tech Appendix Numbering Reconciliation + Chapter Cross-Reference Re-Validation — Workstream Handoff (2026-05-11)

**Date drafted:** 2026-05-11
**Branch to create at session start:** `claude/appendix-numbering-reconciliation-<harness-id>` (branch from current `origin/main` after `git fetch`)
**Status going in:** Issue surfaced 2026-05-11 during the Path B + apparatus register sweep — apparatus Item 9 (`cf682be`) + Item 10 (`16876a1`) + the §7-vs-§8 reconcile commit (`ede6d88`) all touched chapter cross-references to the Tech Appendix and exposed a dual-numbering pattern that confuses readers.

**Blocker — DO NOT START YET:** Apparatus register sweep (workstream #9) is still in flight on branch `claude/path-b-apparatus-bundle-flamboyant-feistel-97749b`. Items 11–15 are expected. Touching this workstream before that branch lands its remaining items will create rebase conflicts on chapter files. **Wait for #9 to declare itself done OR for the apparatus bundle branch to merge out** before opening this workstream.

---

## The substantive issue

The Tech Appendix at `core/technical-appendix/TechnicalAppendix_v2.0.0.html` (7,817 lines) runs **two parallel section-numbering systems for the same content**:

1. **Numeric sections** (§1, §2, …, §9) — used in the TOC (lines 144–204) + main section headers throughout.
2. **Letter sections** (Section A, B, C, …, L, M) — used in body subsection structure with lettered sub-IDs (L.1, L.2, L.3, L.4 etc.).

**Concrete example:** the Four Gates Admission Apparatus is labeled BOTH §7 (TOC line 194 + main heading line 2316) AND Section L (subsection structure at lines 2342–2730). Same content, two labels.

**Cascade effect on chapter cross-references:**

- Ch 6 line 714 references "Technical Appendix (Section L)" + "(Section M)" using the letter system.
- Ch 7 line 119 references "Theorem E.3" using letter-anchored theorem numbering.
- Ch 6 line 788 (Apparatus Item 9, commit `cf682be`) references "Section 8 — Asymmetric Regret Rule" using the numeric system.
- Ch 6 + Ch 7 (Apparatus Item 10, commit `16876a1`) added named-theorem content alongside Theorem E.3 references — surfaced the dual-numbering problem.

The mixed reference scheme actively confuses readers. Once the appendix canonicalizes to one system, all chapter cross-references should be re-validated against the canonical scheme.

---

## Specific known issues flagged but not auto-fixed

1. **Tech Appendix line 4868** — `"(§8 / supplement §7)"` — has §8 correct but "supplement §7" reference is unclear; §7 is Four Gates, not a supplement to ARR. **Needs author judgment.**
2. **Tech Appendix Section L** (Four Gates) duplicates §7 (Four Gates Admission Apparatus). Pick canonical, apply throughout.
3. Similar parallel-numbering patterns likely affect:
   - Section E (Theorems E.1–E.4) vs whichever numeric section those theorems live under
   - Section M (Formula Generalization) vs its numeric counterpart
   - Other sections — full appendix audit needed.

---

## Workstream scope

### Phase 1 — Audit (read-only)

Enumerate every top-level appendix section + identify which numbering systems it uses:
- Numeric only
- Letter only
- Both (the problematic case)

Produce inventory at `tools/workstream-handoffs/appendix-numbering-audit-inventory_2026-05-11.md` (or successor date) listing each section with its current dual labels (if any) + a recommended canonical label.

### Phase 2 — Decision (with author ratification)

Pick canonical scheme. **Recommend numeric §-system** since TOC + main headings already use it, and chapter cross-references that already use numeric (Ch 6 line 788 from Apparatus Item 9) align with that scheme.

Specifically resolve:
- The line 4868 "supplement §7" intent question — does the author mean a supplement to ARR (§8 + ARR-supplementary §X)? Or is "§7 / supplement" a misreading? Author judgment required before editing.
- Whether theorem numbering (Theorem E.1–E.4) folds under the numeric scheme as "Theorem 5.1" / "Theorem 5.2" etc., OR whether theorem numbering is a separate-but-aligned system (Theorem E.X with E corresponding to §5 explicitly).

### Phase 3 — Apply (in appendix)

Rename sections / cross-references in the Tech Appendix to the canonical scheme. Maintain backward-compatible HTML anchors during the transition (e.g., `id="section-L"` stays as a redirect anchor or is removed, depending on whether any prior published material has linked to it).

### Phase 4 — Validate (in chapters)

Scan all chapter files for appendix cross-references:
- `manuscript/chapters/Chapter__1_TheQuietMath__Draft.md`
- `manuscript/chapters/Chapter__2_TheMiner__Draft.md`
- `manuscript/chapters/Chapter__3_TheWaterman__Draft.md`
- `manuscript/chapters/Chapter__4_THEEXISTENCEPROOF__Draft.md`
- `manuscript/chapters/Chapter__5_THEACCOUNTABILITYGAP__Draft.md`
- `manuscript/chapters/Chapter__6_ThreeWaysofCounting__Draft.html`
- `manuscript/chapters/Chapter__7_OnOtherWorlds__Draft.md`
- `manuscript/chapters/Chapter__8_WhatThingsActuallyCost_Draft.md`
- `manuscript/chapters/Chapter__9_PricingHonestly__Draft.md` (verify exact filename)
- `manuscript/chapters/Chapter__10_CommonBonds__Draft.md` (verify exact filename)

Use `grep -niE "section [A-Z]|§[0-9]|theorem [A-Z]\.[0-9]|technical appendix|tech appendix"` against each chapter. Catalog every cross-reference. Update each to align with the canonical scheme.

### Phase 5 — Layman-lookup discipline (cross-cutting)

The lookup-by-layman discipline that surfaced this issue (named theorem content + precise reference; e.g., "(Abundance Masking) … Theorem E.3") should become the standard reference format throughout. Each chapter cross-reference should include:

- The named content (so layman knows what they'll find at that reference)
- The precise canonical-scheme address (so specialist can navigate directly)

Format candidate: `"… as the [Named Concept] (Technical Appendix §X.Y, Theorem X.Y) shows …"` or similar. Author ratifies the format; session applies it consistently.

---

## Methodology

- **Two-layer content origination (WP#10)** — Tech Appendix is internal-scaffolding; chapter cross-references that surface in body prose are external-publisher-facing. Apply the discipline accordingly.
- **Path B preemptive policy** — when rewriting chapter cross-references, do not re-introduce Ch 1 prose patterns (this is mostly mechanical / cross-reference-text-replacement, low Path B risk, but worth noting).
- **Verify-stale-memory-claims discipline** — verify line numbers via grep against the live files before citing them. The TOC line numbers + concrete examples above are point-in-time as of 2026-05-11 commit `16876a1`; re-verify before editing.

---

## Hard constraints — what NOT to do

- Do NOT start until apparatus register sweep (#9) Items 11–15 land OR the apparatus bundle branch merges out. Rebase conflict risk on chapter files.
- Do NOT introduce a third numbering scheme. Decision is binary (numeric vs. letter); apply consistently.
- Do NOT touch theorem statements or proofs in the appendix. Numbering reconciliation is metadata; theorem content is out of scope.
- Do NOT edit chapter cross-references without author ratification of the canonical scheme + reference format.
- Do NOT propose meta-conclusions about the Tech Appendix's design philosophy. Stay scoped to numbering hygiene.

---

## Coordination

- **Distinct from but related to:**
  - **Apparatus register sweep (#9)** — that workstream handles trade-press apparatus decisions (in body prose); this handles appendix-internal numbering + chapter cross-references. Different scope, hard dependency (this waits for #9 to land Items 11–15).
  - **Flagship-equation terminology defense sweep (#13)** — that workstream defends named terminology choices in body prose; this handles cross-reference accuracy + lookup affordance. Different scope, no dependency.
  - **Tech Appendix Phase 3 v2.0.0 rebuild (queued in #7)** — that workstream rebuilds appendix content; this handles its internal numbering. **Sequencing:** finish this numbering reconciliation BEFORE Phase 3 rebuild begins, so the rebuild operates on a single canonical-scheme appendix.
  - **Glossary v4 rebuild (queued in #7)** — coordinates with apparatus sweep #9; glossary entries should cite the canonical scheme established by this workstream.

---

## Estimated effort

**Medium.** Appendix is 7,817 lines, ~50+ headings. Audit + canonical-scheme application + chapter cross-reference re-validation likely 2–4 hours of focused session time.

**Could split into two sessions:**
- (a) Appendix-only reconciliation (Phases 1–3) as one session
- (b) Chapter cross-reference re-validation (Phase 4) + layman-lookup format application (Phase 5) as follow-up session once appendix is clean

Recommend single bundled session if the apparatus sweep #9 lands cleanly with no remaining chapter-prose conflicts. Split into two if there's overlap risk.

---

## Branch discipline (per `tools/workstream-handoffs/README.md`)

- Fresh feature branch `claude/appendix-numbering-reconciliation-<harness-id>` from current `origin/main` after `git fetch`.
- Author ratification required before any chapter edits land (Phase 4 onward).
- Per WP#9: merge per ratified chunk via `git push origin HEAD:main`.

---

## Reference files

- `core/technical-appendix/TechnicalAppendix_v2.0.0.html` (7,817 lines as of 2026-05-11)
- `manuscript/chapters/Chapter__6_ThreeWaysofCounting__Draft.html` (lines 714, 788)
- `manuscript/chapters/Chapter__7_OnOtherWorlds__Draft.md` (line 119)
- `tools/workstream-handoffs/README.md` (branch discipline)
- `tools/workstream-handoffs/apparatus-register-sweep-handoff_2026-05-10.md` (parent context; hard dependency)

**Surfacing commits:**
- `cf682be` Apparatus Item 9 — Ch 6 α-dominance replacement
- `16876a1` Apparatus Item 10 — Ch 6 + Ch 7 appendix cross-references with named content
- `ede6d88` Tech Appendix §7-vs-§8 ARR numbering reconcile

---

*End of workstream handoff. Hard-blocked on apparatus register sweep (#9) Items 11–15 landing. Update in place if scope evolves; mark complete via PM session auto-verify discipline.*
