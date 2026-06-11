# PASTE-TEXT → Bibliography session — Solow 1956 orphan removal (CONTINGENT)

*(Copy below the line into the target session.)*

---

Solow 1956 bib-entry orphan removal — CONTINGENT on M3's §3.5 (verify on the tree you're editing first).

Context: The M3 Path-A rework swapped the §3.5 intergenerational-equity citation from "Solow 1956" (QJE — the growth paper; a misattribution) to "Solow 1974" (Review of Economic Studies — the actual intergenerational-equity / exhaustible-resources paper). On the M3 branch this is §3.5 ~line 920: "Solow 1974 Review of Economic Studies + Bergson 1938…". "Solow 1956" was the ONLY in-text use, so once M3's §3.5 is in the tree, the §18 Solow-1956 entry is orphaned.

VERIFY FIRST — do NOT remove blindly:
  grep -nE "Solow 1956" manuscript/technical-appendix/TechnicalAppendix_v2.0.0.html
If §3.5 still cites "Solow 1956" (i.e. M3's §3.5 swap is NOT yet in your tree — e.g. base/pre-merge), do NOT remove the entry; it's still a live citation. Only remove once §3.5 uses "Solow 1974" and "Solow 1956" appears SOLELY in the §18 bibliography. Also confirm it isn't cited in any other TA section (or shared chapters) before removing.

THEN remove this orphaned §18 entry:
  Solow, Robert M. "A Contribution to the Theory of Economic Growth." Quarterly Journal of Economics 70, no. 1 (1956): 65-94.

KEEP (do not touch - now used at §3.5 + 5 other places):
  Solow, Robert M. "Intergenerational Equity and Exhaustible Resources." Review of Economic Studies 41 (Symposium 1974): 29-45.
