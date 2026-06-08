# PROVENANCE — Technical Appendix source commits for the Darity packet

**Purpose:** pin the exact repository states from which the Technical Appendix
files delivered to William Darity Jr. were rendered, so no future (possibly
context-saturated) session re-derives them and gets it wrong. Created 2026-06-08
during the Session-B Darity-version diff (`tools/audits/ta-darity-version-diff_2026-06-07.md`);
revised same day after the author flagged that **two** TA files were sent.

## TWO files were sent — track the SECOND

| | File | Sent | Source commit |
|---|---|---|---|
| 1st (superseded) | `Technical_Appendix_Commons_Bonds_2026-05-14.docx` / `.pdf` | 2026-05-14 | **`71fb076`** |
| **2nd (PRIMARY — the latest Darity holds)** | `Technical_Appendix_Commons_Bonds_with-citations_2026-05-14.docx` / `.pdf` | **2026-05-15 02:31 ET** | **`e6ddf92`** (TA body == `cf24f57` state) |

The 2026-05-15 "proactive-Q0-citation" send (`post-citation-packet-email_2026-05-15.md`)
shipped the revised with-citations derivatives. Per that email the only changes
since the Thursday packet were citation form, two added paragraphs, and one
sentence rewrite — **"no changes to case-study computations or apparatus."** So
the two files are numerically identical; the second adds the author-date
"(Darity 2026)" citation form, the §18 interview bibliography entry, the §5.4
Parfit/Sen pairing, and the §5.1.1 Darity-Mullen sentence rewrite.

**Anchor analysis on the SECOND file (`e6ddf92` / `cf24f57` TA body).** It is the
latest TA Darity has.

## Why NOT `cf24f57`-as-the-only-story / NOT `71fb076`

- `71fb076` (2026-05-14) is the **first** file's source — superseded by the
  05-15 send. Retain as history only.
- `cf24f57` (2026-05-15) is a build-script/CSS commit; it did not change the TA
  body but its body state == the second file's. `e6ddf92` is the commit that
  actually regenerated the second file's derivatives. Either identifies the
  second file's TA state; `e6ddf92` is the precise committing commit.

## Verified (DOCX → source) three ways each

**Second file (with-citations DOCX) == `e6ddf92`/`cf24f57` state:**
1. `e6ddf92` heads the file's `git log --follow`.
2. Carries "(Darity 2026)" ×3 and zero "personal communication" — the post-05-15
   author-date form.
3. Contains the §18 "Interview by Christopher Winn" entry + §5.4 Sen pairing
   (×6); the "explicitly approved" sentence is absent (rewritten).

**First file (DOCX) == `71fb076`:** sole `--follow` commit; "(Darity, personal
communication, May 2026)" ×2; §5.4 Parfit-only; "explicitly approved" present.

Numeric markers (both files, identical): carbon $544/ton, total $552–566/ton,
2.32 mt CO₂/short ton basis, OSIRIS-REx→Bennu row, Keck commercial-mining table,
full §11.10 space-economics block.

## Consequence for corrections to Darity

The carbon figures Darity holds ($544 / $552–566, 2.32 basis) were **superseded
after both sends** by the Coal-CO₂ cascade (`914addc`, 2026-05-23 → 2.61 basis,
$510 / $518–532), itself being corrected by the held-branch rigor audit (→ $496
/ $504–518). Darity **never saw** the `$510` figure the audit ledger flags.
Every other confirmed audit error was already present in his copy. The new
substantive offer (backward-CSD / reworked Method-3) was in neither file.
Full mapping: `tools/audits/ta-darity-version-diff_2026-06-07.md`.

*(Git notes recording the same are attached to `e6ddf92` (primary) and
`71fb076` (superseded first send); git notes are not pushed by default, so this
tracked file is the durable record.)*
