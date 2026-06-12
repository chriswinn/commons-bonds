# §06 Sample Chapters — assembly protocol

**What ships:** the COMPLETE text of Chapter 1 (*The Quiet Math*) and Chapter 5
(*The Accountability Gap*) — entire chapters, not excerpts. "Sample chapters" in
a nonfiction proposal means whole chapters: they exist to prove the manuscript
is real and the prose holds at full length. (~6.2K + ~13.7K words as of
2026-06-11; together roughly 60–70 pp of the 75–100-pp package.)

**When to copy:** AFTER the author's redline pass on both chapters lands
(in flight 2026-06-11/12; the redline is the pipeline's final quality stage —
never copy before it, never edit after it). Pull from the then-current
canonicals:

- `manuscript/chapters/Chapter__1_TheQuietMath*.md`
- `manuscript/chapters/Chapter__5_TheAccountabilityGap*.md`

(Match by glob — the `__Draft` filename suffix is a consent marker that drops
when a chapter's named-subject questions resolve, as Ch 5's did.)

**Copy-time strip list (the ONLY permitted changes; prose verbatim otherwise):**

1. The `<!-- WORKING DRAFT ... -->` header comment (both files).
2. All inline `<!-- structure-note: ... -->` comments (Ch 5 carries several).
3. Nothing else. No silent edits; the author-redlined text is final.

**Copy-time checks:**

- `grep -c '<!--'` on each copy → must return 0.
- `bash tools/scripts/check-corpus-invariants.sh --scope publishing/book-proposal/06_sample-chapters/ --severity HIGH` → exit 0.
- Em-dash/glyph render check rides the package-level Stage-4 offline audit.

**File naming in this directory:** `sample-ch1_TheQuietMath.md`,
`sample-ch5_TheAccountabilityGap.md` (no `__Draft` markers, no dates — these
are package components, versioned by the assembly's git history).
