# Reverse-CSD model + reef §11.12 — fresh-session kickoff paste-text (2026-06-08)

**How to use:** paste everything below the line into a FRESH session, started AFTER the TA
reconciliation + closeout session has merged the forward/correctness TA sessions (M3 rework,
internal-correctness, Deepwater, provenance, Darity-diff) to `origin/main`. Do not start this
before that merge — the reverse model must be built on the merged, corrected forward TA.

---

You are picking up the **reverse-CSD model + Chesapeake oyster-reef calibration** for the
Commons Bonds Technical Appendix. This is ADDITIVE downstream work, sequenced deliberately after
the TA forward-fix closeout. The prior session did the investigation, verification, and design
reconciliation; your job is to review the landed M3 rework, then draft the reverse model + reef
case against the corrected TA, and present it for author ratification before applying.

## FIRST ACTION — worktree isolation off CLEAN main

```bash
HARNESS_ID="$(date +%y%m%d)-$(openssl rand -hex 3)"
BRANCH="claude/ta-reverse-csd-${HARNESS_ID}"
WORKTREE="/Users/c17n/commons-bonds-ta-reverse-csd-${HARNESS_ID}"
git -C /Users/c17n/commons-bonds fetch origin main
git -C /Users/c17n/commons-bonds worktree add -b "${BRANCH}" "${WORKTREE}" origin/main
```
Work only in `${WORKTREE}`, absolute paths. Commit to the branch. **Do NOT merge to main** —
this is author-ratification-gated TA content; use `MERGE-HOLD:` on commits.

## READ FIRST (the prior session's output — all on the now-merged main or its history)

1. **`tools/audits/ta-reverse-csd-reef-calibration_proposal-record_2026-06-08.md`** — THE master.
   Read top to bottom. It has: a Path-A reconciliation block, a verification addendum (4 findings),
   the "bond only the unassailable floor" decision, and sections A–H with the full substantive
   draft content (the §5.5 reverse-model prose, the §11.12 reef HTML, §14.6/§5.6/§17.7 edits, the
   verified reef bibliography). Treat A–H as a WORKING DRAFT to re-render against the merged TA, not
   as final text to paste — line numbers and the exact §11.6/§3.5/M3 wording will have shifted in
   closeout.
2. The merged TA: `core/technical-appendix/TechnicalAppendix_v2.0.0.html`.
3. `research/story-drafts/ch3-restitution-bond-numbers_2026-06-05.md` — reef numbers + sources.
4. `manuscript/chapters/Chapter__3_TheWaterman.md` — the shipped reef chapter (see GATE 2 below).

## STEP 0 — gates (check before drafting)

- **GATE 1 (M3 in main):** confirm the M3 Path-A rework is merged. Your reverse-M3 prose must
  mirror it. If not merged, STOP and tell the author.
- **GATE 2 (Ch3 priced section):** the reef §11.12 puts a $20–37M figure in the TA. The shipped Ch3
  currently prices NO reef figure (verified 2026-06-08). The TA must not lead a number into print
  ahead of the book. So: §11.12 may be DRAFTED now, but it should not MERGE until Ch3 (or another
  chapter) carries the priced restitution claim it cohere with. Flag this to the author; coordinate
  with any Ch3 chapter-drafting session.

## STEP 1 — review the landed M3 rework (do this first; author previously held it for "once landed")

Give INDEPENDENT input on three things from the M3 session, reconciling against the priors already
recorded in the proposal record (don't rubber-stamp):
- **The M3 Path-A rework itself** (the formal crux). Check the multiplier architecture, ς, α,
  convergence, Norway cascade.
- **The unpriceability-theorem approach.** Prior independent verdict (in the proposal record): no
  formal unpriceability theorem ever existed in tracked history; don't author one; coercion is an
  *open slot*, not incommensurable; the framework already handles true incommensurability forward
  (Europa→ARR). Compare the M3 session's suggested approach against that.
- **The M2 reframe.** Ratified outcome: M2 is **(c)-uniform** — the realized-B reader in BOTH
  directions (forward Norway = B₂, backward reef = B₁), a **revealed lower bound on RCV**, NOT a
  third independent estimator. Reconcile your reverse-M2 prose to this.

## STEP 2 — draft the reverse-CSD model + reef §11.12 (present for ratification before applying)

Per-prompt serial cadence; one chunk at a time; author ratifies before you apply. Build:

**A. §5.5 reverse-model description** (the floor + moving-ceiling range method, three methods in
reverse, three states open≠zero≠unpriceable, CSD vs B₁).
- Backward-M3 = **Path A multiplier form**: `CSD_M3 = V_option × scarcity_weight(ς) × irreversibility_weight(1/(1−α))`
  (V_option = extinguished optionality / foregone service flow; ex-post vs ex-ante fork exposed not
  settled). ς is final-sigma (renamed from σ); irreversibility weight = 1/(1−α), **no β**; cite
  IPCC AR6 SPM B.5 + Bernhardt & Palmer 2011 for α.
- M2 = realized-B reader both directions; revealed lower bound; not a third estimator.
- **Convergence = bound-range, degree not kind.** Do NOT write "forward converges to a point /
  backward yields a range" — it contradicts the symmetry theorems (Thm 10.1b, §17.5). Both
  directions produce a range; the backward range is typically wider (more methodological-choice
  spread), not different in kind.

**B. New §11.12 reef calibration** (worked end-to-end). **Author decision: "bond only the
unassailable floor."**
- Bond anchored at **M1 cure-cost floor**: foreclosed reef extent **2,738 ac** (James River
  high-quality oyster-rock lost 1910→1981; Schulte 2017 *Front. Mar. Sci.* 4:127) × realized
  restoration **$7,300/ac** (Great Wicomico, NOAA per-tributary table) ≈ **$20M**; ×$13,500/ac
  (Great Wicomico Tributary Plan §5, natural-recruitment) ≈ **$37M**; ×$77,000/ac (bay-wide avg)
  ≈ **$200M central**. All numbers AREA-based (not shell volume — keep the Darling shell-mountain
  as narrative only).
- M2 corroboration: ~**$57K/ac** realized ($108M ÷ ~1,900 ac) sits between floor and average →
  corroborates M1 unit-cost. Realized B₁ (public, zero from industry): **>$92M MD** (MD DNR / Gov.
  Moore, Aug 26 2025) / **~$110M Bay-wide** (cite NOAA itemized ~$115M = MD $93.52M + VA $21.77M as
  primary; $108M program-level is the softest MEDIUM input, use as rounding corroborator only).
- **M3 = NAMED, not priced.** Do NOT put a foregone-fishery number on paper for the reef. Name it
  as the admitted *Open*-state ceiling (real and owed, a lower bound, NOT zero/unpriceable). State
  explicitly this is a **strategic** decline (bond design), not methodological — M3 is computable
  for the reef; its method is fully specified generically in §5.5 and is load-bearing in the
  forward cases (§11.8 α-dominance; IPG upper bound §11.11). The reef must never "show-then-flinch."
- Renewable-with-extracted-renewal-structure note: the reef exercises S_max / Thm 10.3 via
  destruction of the *regeneration function*, a distinct formal object from the non-renewable §11
  cases — a feature.
- **Do NOT** assert a Hampton-Bar-specific acreage (none exists); use the James figure as the
  stated lower-Bay/Hampton proxy. Do NOT invent the NSA Hampton Roads dollar figure (present
  qualitatively). No invented factual claims; cite EXTERNAL sources, never our own table/ledger.

**C. §5.5 blast-radius reconciliation (don't skip).** The TA currently says, in ~9 places, that the
backward direction is "not computed in this volume by design" (§1.7, §1.10, §5.5 ×several, §11.7,
Thm 10.1b, §17.5). Adding ONE computed backward case (the reef) requires reconciling those to
"computed for the reef demonstration; other backward cases still cited-not-computed" — leave NO
internal contradiction. **Prefer the light-touch "single worked demonstration / proof of reach"
framing** over a range-vs-convergence redesign that fights the symmetry theorems.

**D. §5.6 open-question resolution** (the L1447 "logged here without prescribing" marker): house the
B₁-direction moral grounding via the reparations-economics lineage (Darity, Mullen, Hamilton,
Coates) + the first-person authorial note — NOT a new theorem. Low priority.

**E. §17.7 generative strengthening** — optional polish; consistent with the ratified Ostrom-path
illustrative posture.

**F. Authorial note (coercion), if the author wants one in the TA.** First-person, visibly distinct
from the apparatus. Echo the SHIPPED voice — Atlantic essay :80 ("*What the framework offers is the
ledger. What belongs on it, looking backward, is **theirs** to enter*") and Ch1:56 ("*a commute and
a stolen life do not belong on the same line… Naming the rhyme is not the same as making them
equal*"). **Never use "standing"** (violates the no-standing discipline AND deviates from the shipped
voice). This material already exists in Ch1/Ch5/Atlantic — whether the formal TA needs a duplicate
is an author call, not a requirement.

## HARD DISCIPLINES (carry-forward; do not re-litigate)

- **No "standing" anywhere in the apparatus** — not even "open to anyone who has it." There is no
  standing primitive currently; don't add one. Coercion is an open slot, not incommensurable.
- **No unpriceability theorem.** None exists; don't author one. `S_max → 0` means "cost dominates"
  (Thm 10.4 knife-edge; Substitution Dominance Thm 10.5), not "unpriceable."
- **Every number sourced / derived-with-work-shown / labeled-assumption.** Cite the EXTERNAL
  authority, never our own table/ledger. Add each source to the bibliography the moment it's
  verified. Verify before applying any value-dependent fix.
- **No invented factual claims** in publisher-facing prose (per CLAUDE.md). The phrase "invites an
  argument I do not need to have" is NOT in Ch3 — do not put it (or any invented quote) in the TA.
- **Daly §14.6 fix is already applied** (prior commit `f9cef3f`): the inverted "Daly argues S_max
  must equal 1" was corrected to the complementarity / critical-natural-capital (S_max→0) statement.
  Confirm it's present in merged main (cherry-picked from the held branch, or applied by the
  internal-correctness session). DO NOT re-apply or double-apply.
- Per-prompt serial cadence; present substantive content for author ratification before applying;
  commit to branch with `MERGE-HOLD:`; never force-push main; never amend an origin/main commit;
  never `--no-verify` without author direction.

## CONTEXT FLAGS (history you should know)

- The original spec (`core/technical-appendix/CSD-computation-method-spec_2026-06-06.md`) and the
  session that produced it were context-saturated and contained errors (it said Path B — reversed to
  Path A; it framed "remove unpriceability theorem / remove standing" as needed surgery — both
  target things that don't exist in the TA). Treat the spec as a suggestion already superseded by the
  proposal record's Path-A reconciliation block + verification addendum.
- The reef-numbers file is dated "for author review BEFORE Ch3 drafting" — hence GATE 2.
