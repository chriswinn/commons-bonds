# Noema §III FMLA paragraph — HARD CORRECTION CONSTRAINT (2026-06-18)

**Status: BINDING on any Noema version that ships.** A factual fabrication in the
paternity/FMLA/back-to-work paragraph (§III "The Quiet Math") was corrected on
`origin/main` 2026-06-18 (commit `cda9562b`, branch
`claude/noema-tautology-finding-260618-5f2f3a`). The current `essay.md` carries
the true account (verified L55, gate HIGH=0, 2026-06-18). **Any version I
select, draft, or promote MUST carry the true account below.** The fabrication
originated in the 2026-05-28 parallel-drafts lineage, so it WILL reappear in any
draft derived from that line unless actively replaced. If a selected version is a
V-D′ rewrite, PORT the corrected paragraph in — do not diff against the old
fabricated text.

## DO NOT SHIP (false fabrication — retired)
The version claiming the author "took two weeks of leave… I should have taken
twelve… **The architecture was the architecture.**" Two defects: (1) FACTUALLY
FALSE — the author did NOT take two weeks; it inverts the truth. (2)
"The architecture was the architecture." is a HIGH-severity tautological tic
(`regressed-tautological-x-was-x`; Ch 1 cut the identical line at F-V10).

## TRUE, AUTHOR-RATIFIED ACCOUNT (on main — port verbatim or re-voice faithfully)
> I was thirty-eight when my son was born. I took every day of paternity leave
> the company offered, and when that ran out I took the full leave the Family and
> Medical Leave Act allows. My boss let me work remotely and routed every piece
> of work he could to other people, and he kept doing it for as long as he was
> able. Then a few deals came back to life at huge clients where I had worked
> before and established myself, the kind a company calls must-win in a lean
> year. Word of them climbed high enough that even the chief executive was
> tracking them personally, and at that point there was no one my boss could hand
> them to. In the terms every company runs on, it was simply time for me to step
> up and add value. My employer was not cruel and my colleagues were not
> indifferent. The protocol did what it was built to do: paternity leave ends,
> family leave exhausts, the work only you can do is waiting. No one thing made
> me go back. Everything did.

Provenance: author's own correction + `research/story-drafts/_session-answers_2026-05-03.md`
(~L294-298, "paternity leave was over and FMLA leave had run out… no villain");
archived Ch 1 (`manuscript/chapters/archive/Chapter__1_TheQuietMath_REGRESSED_2026-06-05.md`)
carries the same true account.

## DISCIPLINE CONSTRAINTS (must hold in any version)
- **Anonymized per the CEO-era NDA:** employer is IBM, the chief executive is a
  real named person — keep BOTH out of prose. Use "the company" / "the chief
  executive" / "huge clients" only. No client names.
- **No invented facts:** do not embellish. No rendered scene of the personal
  cost (author described it only as "frankly just devastating" — stays
  understated), no quoted speech, no specific deal names or dollar figures.
- **No em-dashes** in this passage; **no X-was-X tautology.**

## GATE NOTE
The provisional line-55 allowlist for `regressed-tautological-x-was-x` was REMOVED
from `tools/quality-gates/regressed-patterns.yaml`. If a version reintroduces
"the architecture was the architecture," the corpus-invariant gate flags HIGH —
do NOT re-allowlist; fix the prose. Check:
`bash tools/scripts/check-corpus-invariants.sh --scope publishing/essays/noema-commons-bonds/essay.md`

Source: cross-session handoff from the noema-tautology-finding session, 2026-06-18.
