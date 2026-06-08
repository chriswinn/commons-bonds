# PROVENANCE — Technical Appendix source commit for the Darity packet

**Purpose:** pin the exact repository state from which the Technical Appendix
delivered to William Darity Jr. was rendered, so no future (possibly
context-saturated) session re-derives it and gets it wrong. Created 2026-06-08
during the Session-B Darity-version diff (`tools/audits/ta-darity-version-diff_2026-06-07.md`).

## The source commit

**`71fb076` (2026-05-14)** — "TA Sandy-packet — WP#10 regression cleanup: strip
version + status-block scaffolding from reviewer-facing artifacts."

This is the commit that committed `Technical_Appendix_Commons_Bonds_2026-05-14.docx`
(+ `.pdf`) into the repo. The TA HTML in this commit's tree
(`core/technical-appendix/TechnicalAppendix_v2.0.0.html`) is the exact body
text that was rendered into the deliverable Darity received.

- **In-scope artifact:** `Technical_Appendix_Commons_Bonds_2026-05-14.docx` / `.pdf`
  → source **`71fb076`** (sole commit in the file's `git log --follow`).
- **With-citations variant:** `Technical_Appendix_Commons_Bonds_with-citations_2026-05-14.docx`
  → regenerated later at **`e6ddf92`** (2026-05-15); it therefore includes the
  2026-05-15 prose/citation edits (author-date citation form; §5.4 Parfit/Sen
  pairing). Still pre-`914addc`, so its numeric content matches `71fb076`.

## Why NOT `cf24f57`

`cf24f57` (2026-05-15) is a day **after** the send and 7 TA commits downstream
of `71fb076`. An earlier draft of the Session-B report (and the rigor-audit
resume doc) mis-anchored on `cf24f57` and called it "the 6 commits." The 7
intervening commits (`6d28f4e`, `f6d6281`, `7599c41`, `769938a`, `b469079`,
`4cc49df`, `cf24f57`) are all prose / citation / CSS with **zero numeric
changes**, so the mis-anchor did not corrupt the error-provenance conclusions —
but the source ID and commit count were wrong. Anchor on `71fb076`.

## Verified three ways (DOCX == `71fb076`, not `cf24f57`)

1. **File history:** `71fb076` is the only commit in
   `git log --follow -- research/outreach/subjects/darity/Technical_Appendix_Commons_Bonds_2026-05-14.docx`.
2. **Citation form:** the DOCX carries "(Darity, personal communication, May
   2026)" ×2 and zero "(Darity 2026)" — matching `71fb076` (the 05-15 commits
   switched to author-date form).
3. **§5.4 + Darity-Mullen prose:** the DOCX lacks the Parfit/Sen-pairing
   expansion and retains the "explicitly approved the framework's use of
   'reparations' terminology" sentence — both `71fb076`-only.

Numeric markers also all match `71fb076`: carbon $544/ton, total-with-carbon
$552–566/ton, 2.32 mt CO₂/short ton basis, the OSIRIS-REx→Bennu row, the Keck
commercial-mining table, and the full §11.10 space-economics block.

## Consequence for corrections to Darity

The carbon figures Darity holds ($544 / $552–566, 2.32 basis) were **superseded
after the send** by the Coal-CO₂ cascade (`914addc`, 2026-05-23 → 2.61 basis,
$510 / $518–532) and are themselves being corrected by the held-branch rigor
audit (→ $496 / $504–518). Darity **never saw** the `$510` figure the audit
ledger flags. Every other confirmed audit error was already present in his copy.
Full mapping: `tools/audits/ta-darity-version-diff_2026-06-07.md`.

*(A git note recording the same is attached to `71fb076`; git notes are not
pushed by default, so this tracked file is the durable record.)*
