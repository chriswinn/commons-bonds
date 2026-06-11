# PASTE-TEXT → Provenance + Bibliography session (Session A)

*(Copy everything below the line into the target session.)*

---

**Symbol-sweep findings that land in your domain — please verify INDEPENDENTLY (re-derive / re-grep; do not take these on faith).**

A notation/symbol-sweep ran on branch `claude/ta-internal-fixes-260607-208b7b` (off the held TA rigor-audit branch). It catalogued every symbol in `manuscript/technical-appendix/TechnicalAppendix_v2.0.0.html` (7-agent exhaustive pass + adversarial completeness check). Three items belong to your number-provenance + bibliography pass. Supporting artifact on the branch: `manuscript/technical-appendix/symbol-registry_2026-06-07.md` (Parts 1 & 3).

**1. Bare `B` (Accountability Bond) collides with the "billion" suffix in worked numbers.**
- The defined variable `B` (Accountability Bond) and the magnitude abbreviation "B" = billion (e.g. `55B BOE`, `$18.7B`, `$942B`) share the glyph, in exactly the quantitative passages a referee reads closely.
- ~50 occurrences. Verify with: `grep -noE '[0-9][0-9.,]*B\b' manuscript/technical-appendix/TechnicalAppendix_v2.0.0.html`. Sample lines: 859, 2265, 2340, 3892, 3904, 3911, 3914, 3917, 3920, 3958, 3974, 3993, 4118, 4150, 4160, 4170, 4184, 4241, 4245, 4432, 4533, 4543, 4603, 4605, 4617, 4619, 4631, 4633, 4651, 4666, 4693, 4696, 4699, 4702, 4706, 4712, 4719, 5935, 6040, 6100, 6136, 6155, 6196.
- The sweep session did **NOT** edit these — they are your sourced-number lines, and unilateral edits would collide with your pass. **Recommendation:** as part of your number pass, spell out "billion" ("55 billion BOE") so `B` reads only as the bond variable. The number values don't change. Verify the collision is real, then decide.

**2. Bibliography provenance gaps — cited inline, absent from §18.**
- **Brennan & Schwartz 1985** (commodity-investment real options) — cited at 6706, 6719, 6723; not in the bib.
- **Black–Scholes 1973** (option-pricing foundation) — cited at 6723; not in the bib.
- **Knight 1921** (risk vs uncertainty) — cited at 6895; not in the bib.
- Verify by grepping the §18 bibliography (~lines 7716–8037) for each; add the missing entries.

**3. Solow 1956 may become an orphan (coordinate with the correctness sweep).**
- The internal-correctness sweep proposes swapping §3.5 **line 917** "Solow 1956 *QJE*" → "Solow 1974 *Review of Economic Studies*" (line 917 makes an *intergenerational-equity* point; Solow 1956 is the *growth* paper — misattribution; Solow 1974 is the exhaustible-resources/intergenerational-equity paper, already in the bib).
- Line 917 is the **only** in-text use of Solow 1956. If the swap lands, the Solow 1956 bib entry (~line 7981) is orphaned. Verify whether Solow 1956 is cited anywhere else; if not, decide keep-vs-remove.

**Ask:** verify each independently against the file/sources, then fold #1 + #2 into your pass and coordinate #3 with the correctness sweep. Report what you confirm vs. dispute.
