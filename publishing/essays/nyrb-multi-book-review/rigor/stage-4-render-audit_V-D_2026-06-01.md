# NYRB Multi-Book Review-Essay → *Mazzucato + Pistor + Christophers + Susskind* — Stage 4 Render + Character-Integrity Audit (V-D Hybrid; FRESH INDEPENDENT IN-SESSION) v1.0.0 — 2026-06-01

**Status:** **RATIFIED CLEAR 2026-06-01** via in-session containerized render-toolchain (Docker + Colima + `commons-bonds-render:latest` image, `tools/scripts/docker-render.sh` canonical path; cross-checked via host-pandoc HTML backend). All 7 Stage 1 brief §14 render-safe-convention axes PASS across 3 backends. Convergence verdict vs locked-cut Stage 4 (origin/main `b043b8d` 2026-05-27 author-offline-execution): **AGREE — no drift detected.**

**Workstream:** Wave 2 Candidate W2.5 — NYRB Multi-Book Review-Essay; V-D hybrid promotion chip (Amendment-D-aware reweighting V2 audit §13.5 spawn-chip #2 — fresh independent Stage 4 render audit on the V-D hybrid specifically).

**Audit target:** [`publishing/essays/nyrb-multi-book-review/_archive/parallel-drafts_2026-05-28/nyrb-multi-book-essay_hybrid_best-of-both.md`](../_archive/parallel-drafts_2026-05-28/nyrb-multi-book-essay_hybrid_best-of-both.md) — V-D hybrid; 8,421w body prose (lines 114–228 of the file; YAML frontmatter lines 1–112 + scaffold trailer lines 230–232 stripped before render).

**Companion artifacts:**
- Locked-cut Stage 4 baseline (target of convergence-check): [`stage-4-render-audit.md`](stage-4-render-audit.md) — locked-cut essay.md; RATIFIED CLEAR 2026-05-27 via author-offline-execution
- V-D Pass 3.3 + 3.4 + 3.5 V2 audit (Amendment-D-retrofit context): [`pass-3-3-3-4-3-5-bundled-audience-load-developmental_VERSION-D_INDEPENDENT-AUDIT-V2_2026-05-28.md`](pass-3-3-3-4-3-5-bundled-audience-load-developmental_VERSION-D_INDEPENDENT-AUDIT-V2_2026-05-28.md) §13.5 chip #2 (this artifact)
- Stage 1 brief §14 render-safe convention: [`stage-1-brief.md`](stage-1-brief.md) §14.1–§14.6
- V-D source frontmatter discipline disclosure: V-D YAML `em_dashes_used: 0`; `apparatus_discipline_compliance.named_framework_terms_count: 0`; bibliography-verified Polanyi + Sen additions

**Methodology anchor.** v3.1 audience-aware drafting discipline ([`tools/memory/feedback_audience_aware_drafting_discipline.md`](../../../../tools/memory/feedback_audience_aware_drafting_discipline.md)) Stage 4 + Stage 4 doctrine [`tools/pipeline-doctrine/commons_bonds_pipeline_doctrine_stage_4_v1.0.0.md`](../../../../tools/pipeline-doctrine/commons_bonds_pipeline_doctrine_stage_4_v1.0.0.md). Amendment A note: render-toolchain containerization (Docker / remote-container) drives Stage 4 Claude-token cost to ~0; this audit honors the mandatory-by-default firing under no-cost regime per author 2026-06-01 chip framing. Unlike the locked-cut audit (author-offline-execution), this V-D audit ran the render-toolchain in-session and inspected the rendered artifacts byte-for-byte.

---

## §1. Stage 4 scope (per v3.1 doctrine + Stage 1 brief §14)

The audit verifies seven axes per Stage 1 brief §14:

1. **Smart-quote convention** (§14.2) — NYRB house style requires curly quotes throughout body prose
2. **Em-dash render integrity** (§14.1) — V-D YAML claims 0 em-dashes; verify no Unicode hyphen / en-dash / em-dash drift
3. **Italicization integrity** (§14 implicit; brief §13 bibliography) — book titles (10 titles per cover-letter spec) + foreign-language phrases (*pari passu*) + Latin case names (*NML Capital v. Argentina*)
4. **Special-character render integrity** — non-ASCII chars (Ø in Ørsted; ć in Milanović; en-dash for year ranges); no tofu boxes; no font-substitution surprises
5. **Section-break convention** (§14.3 + §14.4 + F-8) — NO embedded section headers in body prose; only H1 title permitted
6. **Verbatim-quote integrity** (§14.6) — the 3 Pass-3.1-verified quotes (Pistor; Mazzucato; Christophers) render byte-for-byte intact across all backends
7. **Footnote / citation convention** (§14.5) — minimal footnoting; in-text citation only; no endnote infrastructure

---

## §2. Render toolchain inventory + execution

**Containerized canonical path (per Amendment A):**
- Docker (Engine 29.5.1) + Colima (macOS arm64 host) + `commons-bonds-render:latest` image (2.89 GB, built 2026-05-19)
- `tools/scripts/docker-render.sh` wrapper → `build-derivatives-alt.sh` → pandoc 3.x (in-container) → xelatex (.md → .pdf path; EB Garamond 12pt + DejaVu Serif fallback header for U+2014 + U+2248) + reference.docx style sheet (.md → .docx path)
- Letter paper; 1in margins; EB Garamond 12pt body

**Host fallback path (cross-check backend):**
- pandoc 3.9.0.2 (host) + `+smart` extension → standalone HTML5 with smartypants quote conversion

**Backends exercised (3 of 3 attempted):**

| Backend | Render path | Status | Output size | Pages/structure |
|---|---|---|---|---|
| **.pdf** | Docker → pandoc → xelatex → xdvipdfmx (Producer: xdvipdfmx 20220710; Creator: LaTeX via pandoc) | ✓ | 86,768 bytes | 14 pp × Letter (612×792 pt) |
| **.docx** | Docker → pandoc → reference.docx style → ECMA-376 Open XML | ✓ | 30,048 bytes | document.xml extracted + parsed |
| **.html** | Host pandoc → standalone HTML5 + smartypants | ✓ | 61,400 bytes | well-formed XHTML; 31 `<em>` spans preserved |

All three renders completed without warnings, tofu glyphs, or font-substitution flags. The Stage 4 friction anchors specifically noted in the chip framing — tofu-box em-dash / ≈ rendering issues (Ch 5 + Ch 6, commit `d238f2c`); Chrome-vs-wkhtmltopdf rendering divergence (commit `cf24f57`); EB Garamond font-family naming (commit `3208619`) — did **not** surface for this V-D hybrid because the body prose carries 0 em-dashes, 0 ≈ glyphs, and no figures / formulas that would exercise the divergent code paths.

---

## §3. Per-axis verification table

| Axis | Source (markdown) | PDF render | DOCX render | HTML render | Verdict |
|---|---|---|---|---|---|
| **§14.1 Em-dash discipline** — U+2014 count | **0** | 0 | 0 | 0 | ✅ **PASS** — V-D YAML `em_dashes_used: 0` claim verified at source + at all 3 backends |
| **§14.1 cont.** — U+2013 en-dash count | **1** (1936–1948 year range) | 1 (rendered as `–`) | 1 | 1 | ✅ **PASS** — appropriate convention for number range; not a violation |
| **§14.1 cont.** — em-dash substitute patterns (`--`, `---` mid-body, `space-hyphen-space`) | **0** | n/a (substrate-level) | n/a | n/a | ✅ **PASS** — no em-dash candidate-conversion sites |
| **§14.2 Smart-quote convention** — straight `'` count in body | 102 (markdown source) | **0** | **0** | **0** (residual 2 inside CSS `font-family:'Lucida Console'` attr only — not body prose) | ✅ **PASS** — smartypants quote conversion verified end-to-end across all 3 backends; body prose 100% smart-quoted at render |
| **§14.2 cont.** — straight `"` count in body | 14 (markdown source) | **0** | **0** | **0** (residual 20 inside DOCTYPE / `<meta>` / CSS attrs only — not body prose) | ✅ **PASS** — same |
| **§14.2 cont.** — smart-quote pair symmetry | n/a | 7 LDQ + 7 RDQ + 102 U+2019 right-single (apostrophes) | same | same | ✅ **PASS** — pair-count symmetric at all 3 backends; no unpaired quote drift |
| **§14.3 / §14.4 / F-8 Section-break convention** — embedded H2/H3 in body | **0** (only `# The Architecture and Its Residue` H1 title) | only title rendered as H1 heading; subsequent §-transitions via paragraph break + opening-sentence semantic shift | only title rendered; flow continuous | only title rendered; `<h1>` only | ✅ **PASS** — F-8 ratification holds; no NYRB-house-style violation |
| **§14.5 Footnote / citation convention** — `[^...]` footnote markers | **0** | 0 | 0 | 0 | ✅ **PASS** — in-text citation only; no endnote infrastructure |
| **§14.5 cont.** — inline `[text](url)` markdown links | **0** | 0 | 0 | 0 | ✅ **PASS** — review-essay carries no hyperlinks at this venue |
| **§14.6 Verbatim-quote integrity** — Pistor `"Capital," she writes, "is coded in law."` (split-quote) | present, straight-quoted | PRESENT, smart-quoted, normalized through line-break-tolerant check | PRESENT, smart-quoted | PRESENT, smart-quoted | ✅ **PASS** — Pass-3.1-verified quote survives 3-backend render |
| **§14.6 cont.** — Mazzucato value-extraction definition (`"activities focused on moving around existing resources and outputs, and gaining disproportionately from the ensuing trade."`) | present | PRESENT, smart-quoted, hyphenation-at-linebreak in PDF normalized | PRESENT, smart-quoted | PRESENT, smart-quoted | ✅ **PASS** — same |
| **§14.6 cont.** — Christophers (`"profit, not price, is what reshapes the world."`) | present | PRESENT, smart-quoted | PRESENT, smart-quoted | PRESENT, smart-quoted | ✅ **PASS** — same |
| **Italicization integrity** — book titles (10 expected) | 13 italic spans for the 10 titles (some multi-instance: *The Code of Capital* 2×, *The Value of Everything* 3×, *The Price Is Wrong* 3×, *Growth: A Reckoning* 2×, *The Great Transformation* 2×, *The General Theory* 1×, *The Road to Serfdom* 1×, *Development as Freedom* 1×, *Governing the Commons* 1×, *Doughnut Economics* 1×) | 31 italic runs preserved end-to-end (matches markdown source span count including the title-block author-publisher italic block) | 31 italic `<w:i/>` runs preserved at byte-XML level | 31 `<em>` spans preserved | ✅ **PASS** — all 10 expected book titles italicized in body prose + all bibliography-lineage titles italicized (Polanyi §VI addition; Susskind §V Sen attribution; Raworth + Daly ecological-economic frame); the title-block author/publisher italic group renders cleanly as 8 italic units |
| **Italicization integrity** — foreign-language phrases (*pari passu*) | 2 italic spans | rendered (italic flag dropped in pdftotext but text intact + visually italic in PDF) | 2 italic `<w:i/>` runs at byte level | 2 `<em>` spans | ✅ **PASS** |
| **Italicization integrity** — Latin case name (*NML Capital v. Argentina*) | 2 italic spans | rendered as above | 2 italic `<w:i/>` runs | 2 `<em>` spans | ✅ **PASS** |
| **Italicization integrity** — bold-span discipline (NYRB house-style: bold should NOT appear in body essay prose) | **0** `**...**` bold spans | n/a | n/a | n/a | ✅ **PASS** — V-D body prose carries no bold spans; reviewer-not-architect register honored |
| **Special-character integrity** — Ø (Ørsted) at U+00D8 | 1 instance (`Ørsted (formerly DONG Energy)`) | rendered as `Ørsted` in PDF text extraction; no tofu | rendered correctly in docx text run | rendered correctly in HTML | ✅ **PASS** — EB Garamond covers U+00D8; no fallback-font intervention needed |
| **Special-character integrity** — ć (Milanović) at U+0107 | 1 instance (`Branko Milanović`) | rendered as `Milanović`; no tofu | rendered correctly | rendered correctly | ✅ **PASS** — EB Garamond covers U+0107; no fallback-font intervention needed |
| **Special-character integrity** — tofu / replacement-char detection (U+FFFD, U+25A0, U+25A1) | 0 | 0 | 0 | 0 | ✅ **PASS** — no font-coverage gap surfaced |

**Summary axis count:** 18 sub-axes verified; **18/18 PASS**; **0 drift findings**; **0 spot-fixes required**.

---

## §4. Convergence-check vs locked-cut Stage 4

| Axis | Locked-cut Stage 4 (RATIFIED CLEAR 2026-05-27 via author-offline-execution) | V-D fresh in-session Stage 4 (this artifact) | Convergence |
|---|---|---|---|
| Smart-quote convention | ✅ CLEAN | ✅ PASS | **AGREE** |
| Verbatim-quote integrity | ✅ CLEAN | ✅ PASS | **AGREE** |
| Em-dash render integrity (0 em-dashes) | ✅ CLEAN | ✅ PASS (0 em-dashes + 1 expected en-dash for year range) | **AGREE** |
| Italicization integrity | ✅ CLEAN | ✅ PASS (31 italic spans preserved end-to-end) | **AGREE** |
| No embedded section-header break-markers | ✅ CLEAN (per F-8) | ✅ PASS (only H1 title) | **AGREE** |
| Footnote / citation convention | ✅ CLEAN (in-text only) | ✅ PASS (0 footnote markers; 0 inline links) | **AGREE** |
| Character-integrity at render | ✅ CLEAN | ✅ PASS (Ø + ć render-clean; 0 tofu) | **AGREE** |

**Aggregate convergence verdict:** **AGREE — no drift detected vs locked-cut Stage 4.** The V-D hybrid's marginal-improvement deltas vs the locked cut (§VI Polanyi `fictitious commodities of land, labor, and money` canonical-phrase expansion + Sen `Development as Freedom` capabilities-rather-than-income attribution; §VIII four-named-case closing list) introduce no new render risk: the deltas use commas, periods, semicolons, and italic book-title flags only — no new special characters, no new em-dash candidate sites, no new section-break candidates.

This independent fresh-session audit is methodologically distinct from the V-D drafter's-self-audit (filed alongside the V-D hybrid 2026-05-28 with the drafter-auditing-own-work bias caveat) — the locked-cut Stage 4 was executed by the author; this fresh audit was executed by a different in-session render-toolchain pass. Convergence at all 7 axes is independent corroboration that V-D is render-safe at NYRB submission gate.

---

## §5. Disposition

🟢 **STAGE 4 RATIFIED CLEAR 2026-06-01 via in-session containerized render-toolchain.**

The V-D hybrid passes all 7 Stage 1 brief §14 render-safe-convention axes across 3 backends (PDF via Docker xelatex; DOCX via Docker reference.docx; HTML via host pandoc smartypants). Convergence with the locked-cut Stage 4 verdict is AGREE; no drift detected; no spot-fixes required.

Per the chip framing (Amendment A note: render-toolchain containerization drives Stage 4 Claude-token cost to ~0; mandatory-by-default rather than inheritance-from-locked-cut), this fresh independent audit ratifies the V-D hybrid's render-safety on its own merits — not by inheritance from the locked-cut RATIFIED-CLEAR verdict. The V-D hybrid is render-safe for NYRB submission at the Oct 8 – Nov 15, 2026 window per cascade-plan v2 W2.5 schedule, conditional on V-D being selected as the canonical submission cut per author selection from the chip-cascade grid.

Per CLAUDE.md merge-to-main policy: Stage 4 RATIFIED CLEAR via in-session execution; no essay-prose changes; rigor-pass artifact only (internal scaffolding → fast-forward merge to main per merge-on-ratification cadence). No `MERGE-HOLD` or `MERGE-AFTER` escape-hatch markers required.

---

## §6. STATE marker

```
STATE: nyrb-vd-stage-4-render-audit RATIFIED (smart-quote: PASS; em-dash: 0-confirmed; italicization: PASS; verbatim-quote-integrity: PASS; section-break: PASS); CONVERGENCE-vs-locked-cut-Stage-4: AGREE; NEXT: aggregation; AWAITING: chip-cascade-completion
```

---

## §7. Cross-references

- V-D hybrid source: [`../_archive/parallel-drafts_2026-05-28/nyrb-multi-book-essay_hybrid_best-of-both.md`](../_archive/parallel-drafts_2026-05-28/nyrb-multi-book-essay_hybrid_best-of-both.md)
- Locked-cut Stage 4 baseline: [`stage-4-render-audit.md`](stage-4-render-audit.md)
- V-D Pass 3.3 + 3.4 + 3.5 V2 audit + Amendment-D retrofit: [`pass-3-3-3-4-3-5-bundled-audience-load-developmental_VERSION-D_INDEPENDENT-AUDIT-V2_2026-05-28.md`](pass-3-3-3-4-3-5-bundled-audience-load-developmental_VERSION-D_INDEPENDENT-AUDIT-V2_2026-05-28.md) §13.5 chip #2
- V-D drafter's-self-audit (methodologically suspect; corroborated by this independent audit on render axes): [`../_archive/parallel-drafts_2026-05-28/nyrb-multi-book-essay_hybrid_drafters-self-audit.md`](../_archive/parallel-drafts_2026-05-28/nyrb-multi-book-essay_hybrid_drafters-self-audit.md)
- Stage 1 brief §14 render-safe convention: [`stage-1-brief.md`](stage-1-brief.md)
- Stage 4 doctrine: [`../../../../tools/pipeline-doctrine/commons_bonds_pipeline_doctrine_stage_4_v1.0.0.md`](../../../../tools/pipeline-doctrine/commons_bonds_pipeline_doctrine_stage_4_v1.0.0.md)
- v3.1 audience-aware drafting discipline + Amendment A token-economy note: [`../../../../tools/memory/feedback_audience_aware_drafting_discipline.md`](../../../../tools/memory/feedback_audience_aware_drafting_discipline.md)
- Locked-cut canonical essay (safety-net baseline; not the V-D audit target): [`../essay.md`](../essay.md)

---

## §8. Methodology + reproducibility notes

**Render-input preparation.** YAML frontmatter (lines 1–112) + post-body italic scaffold trailer (line 232) stripped before render; body prose extraction = lines 114–228 = 8,421 words = 56,643 bytes UTF-8. The H1 title `# The Architecture and Its Residue` was preserved as render-input line 1 (it IS body prose at NYRB submission; the variant-disclosure YAML is not).

**Render-input scratch path:** `publishing/essays/nyrb-multi-book-review/rigor/.stage-4-scratch/vd-body.md` (in-repo under bind-mount for Docker; gitignored; ephemeral artifact removed at session close).

**Verification code path.** Character integrity verified via Python 3 + Unicode-name lookup over (a) the source markdown, (b) the pdftotext-extracted PDF body text (with `re.sub(r'-\s*\n\s*', '', ...)` line-break-hyphenation normalization before substring-verbatim checks), (c) the docx `word/document.xml` extracted via Python `zipfile` + `xml.etree.ElementTree` regex parse over `<w:t>` text runs and `<w:i/>` italic-property runs, and (d) the HTML standalone output with `<em>` span enumeration.

**Backend cross-check.** The three-backend convergence is the methodological safeguard against the Stage 4 friction anchors noted in the chip framing (Chrome-vs-wkhtmltopdf divergence per commit `cf24f57` — addressed here by running pandoc-xelatex (PDF) + pandoc-reference.docx (DOCX) + pandoc-smartypants (HTML) in parallel, all producing identical body-prose character profiles). Wkhtmltopdf was not exercised because the canonical Docker render path is .md → xelatex (per `build-derivatives-alt.sh` §"Style strategy" line 44–47), and HTML→PDF via wkhtmltopdf is only used for `.html` source inputs (e.g., TechAppendix); the V-D source is markdown, so wkhtmltopdf-vs-xelatex divergence is not in scope.

**Reproducibility.** Re-running this audit requires (a) Colima running on macOS host (or any docker-compatible daemon on Linux); (b) `commons-bonds-render:latest` image (built from `tools/scripts/Dockerfile.render`); (c) host pandoc ≥ 3.0 with `+smart` extension. The fresh worktree path for this session was `/Users/c17n/commons-bonds-nyrb-vd-stage-4-render-audit-260601-a8563f` (branch `claude/nyrb-vd-stage-4-render-audit-260601-a8563f`).

---

*End of NYRB multi-book review-essay V-D hybrid Stage 4 render + character-integrity audit v1.0.0 — FRESH INDEPENDENT IN-SESSION RATIFIED CLEAR 2026-06-01. Convergence with locked-cut Stage 4 (origin/main `b043b8d`): AGREE. Per CLAUDE.md merge-to-main policy: internal scaffolding (rigor-pass artifact) → fast-forward merge to main per merge-on-ratification cadence at session close.*
