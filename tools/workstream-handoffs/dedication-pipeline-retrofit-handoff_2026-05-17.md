# Dedication Pipeline-Retrofit Handoff

**Date drafted:** 2026-05-17
**Branch prefix:** `claude/dedication-pipeline-retrofit-`
**Artifact:** Dedication (`manuscript/chapters/_Dedication.md`)
**Status going in:** Currently in DRAFTING / PLANNING state — direction notes + family-name notes present; finalized dedication text NOT YET WRITTEN. Per 2026-05-04 author conversation: dedication will be three-generation arc (grandfather + father + son) mirroring the book's intergenerational thesis.
**Template:** [`pipeline-retrofit-template_2026-05-17.md`](pipeline-retrofit-template_2026-05-17.md)
**Parent doctrine:** [`tools/commons_bonds_pipeline_doctrine_v1.0.0.md`](../commons_bonds_pipeline_doctrine_v1.0.0.md)

---

## §0. Conditional firing

**This retrofit cannot fire until the dedication text is finalized.** The current `_Dedication.md` file holds direction notes + family-name notes only — no publisher-facing dedication prose to retrofit.

PM session sequencing: **block retrofit firing until** the dedication text is drafted + author-ratified. Likely deliverable: 1-3 sentences of dedication prose at the top of `_Dedication.md`, with the existing notes either deleted (retrofit-time cleanup) or retained as audit-trail below.

Once dedication text is finalized, retrofit proceeds per §1 below.

---

## §1. Retrofit scope (post-finalization)

The dedication is the smallest publisher-facing artifact in the manuscript. Retrofit is **maximally abbreviated**:

| Sub-step | Fire? | Notes |
|---|---|---|
| 1a invariant gate | YES | Quick scan. Expected CLEAN. Any direction-notes scaffolding from current draft state must be deleted before Stage 1a passes. |
| 1c coherence check | YES | Verify: grandfather + father + son three-generation framing aligns with Ch 1 grandfather-register-split (intimate-nickname-only in Ch 1; formal name LaVern E. Winn in AuthorsNote); verify son anonymization (no-contact status per Ch 1 disclosure); verify father naming-status (currently anonymized in Ch 1; check whether father gets named here vs anonymized per author preference). |
| 3.1 fact-check | YES — minimal | If any dedication names individuals or cites specific facts, verify against canonical-facts inventory (grandfather: LaVern Edwin Winn / NASA Langley model maker / patent inventor; father: anonymized in chapter prose; son: anonymized in chapter prose). |
| 3.2 voice-polish | YES — minimal | Single-pass voice-polish appropriate for the 1-3-sentence scale. Apply only HIGH-severity flags from Pass 2 inventory; LOW + MEDIUM defensibility is implicit at this scale. |
| 3.3 acceptance | NO | Acceptance test not warranted at dedication scale; the dedication is read by every reader of the book — its acceptance is implicit in the book-level acceptance test. |
| 3.4 robustness | NO | Adversarial test not warranted at dedication scale. |
| 4 render-integrity | YES | Verify dedication renders correctly across `.docx` + `.pdf` + HTML derivative paths. The dedication's typographic register (centered, italicized, perhaps multiple line breaks) is a render-stakes question more than a content question. |
| 5 sign-off + pre-pub queue | YES — abbreviated | Sign-off is the author's call (it is their dedication). Pre-pub review queue entry is one paragraph: who is dedicated to, whether any named subjects are living (son) vs deceased / historical-record (grandfather), and what venue / publisher considerations apply (some publishers have dedication-length conventions). |

---

## §2. Prior cycle status

- Pass 1 fact-check: NOT YET RUN.
- Pass 2 voice-polish: NOT YET RUN.
- Pass 3 audience-load: NOT YET RUN.
- Dedication text: NOT YET WRITTEN. Direction notes present in `_Dedication.md` lines 9-30 (per 2026-05-04 conversation: three-generation grandfather + father + son arc).

---

## §3. Chapter-specific notes

- **Named-subject consent.** Grandfather (LaVern E. Winn): deceased / matter of public record per NASA patent record; per CLAUDE.md named-subject discipline does NOT require consent gating. Father: anonymized in chapter prose; if dedication names father formally, author confirms naming-decision at retrofit time. Son: no-contact status per Ch 1 disclosure; if dedication references son, anonymization-vs-naming requires author confirmation (highly sensitive given Ch 1 line 101 "We have no contact" disclosure).
- **Three-generation framing.** The 2026-05-04 author direction notes: dedication mirrors the book's intergenerational thesis (Ch 10's closing on what one generation owes the next). The dedication is the first thing a reader sees; sets emotional register for everything that follows.
- **Render-stakes specifically.** Dedication typography matters disproportionately to its content size — placement on the page (often top-of-page, centered, italicized), font weight, leading, all matter to reader's first emotional cue. Stage 4 audit should verify both content AND typographic placement.
- **Sequencing.** This retrofit fires LAST among the 13 — after:
  1. Author finalizes dedication text (PM session blocker)
  2. Ch 1 retrofit (so grandfather register-split is fresh)
  3. AuthorsNote retrofit (so named-subject consent decisions surface)
  4. (Optional) After publisher / agent acquires the manuscript + their dedication-convention input is known

---

## §4. Cross-references

- Pipeline doctrine: [`tools/commons_bonds_pipeline_doctrine_v1.0.0.md`](../commons_bonds_pipeline_doctrine_v1.0.0.md)
- Retrofit template: [`pipeline-retrofit-template_2026-05-17.md`](pipeline-retrofit-template_2026-05-17.md)
- Ch 1 retrofit handoff: [`ch1-pipeline-retrofit-handoff_2026-05-17.md`](ch1-pipeline-retrofit-handoff_2026-05-17.md)
- AuthorsNote retrofit handoff: [`authorsnote-pipeline-retrofit-handoff_2026-05-17.md`](authorsnote-pipeline-retrofit-handoff_2026-05-17.md)
- CLAUDE.md named-subject discipline: see "Named-subject consent" section

---

*End of Dedication pipeline-retrofit handoff. PROPOSED 2026-05-17. Conditional on dedication finalization; last in retrofit sequence; minimal-scope retrofit appropriate to dedication scale.*
