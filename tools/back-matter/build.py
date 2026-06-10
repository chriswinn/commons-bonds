#!/usr/bin/env python3
"""Back-matter generator for Commons Bonds.

Parses the internal, scaffolding-laden source-of-truth files and emits CLEAN,
zero-scaffolding, per-entry-anchored reader-facing HTML into manuscript/back-matter/.

Source-of-truth (current homes; relocation deferred per 2026-06-09 plan):
  bibliography : research/literature/bibliography.md   (the SUPERSET master)
  TA §18 (in)  : core/technical-appendix/TechnicalAppendix_v2.0.0.html  (subset, for fold diff)
  glossary     : core/glossary/commons_bonds_updated_glossary_v4.html
  notation     : core/technical-appendix/symbol-registry_2026-06-07.md

Outputs (reader-facing, clean):
  manuscript/back-matter/bibliography.html
  manuscript/back-matter/glossary.html
  manuscript/back-matter/symbol-registry.html

Commands:
  fold-report   diff TA §18 vs master bib; list §18-only entries (review aid only)
  gen-bib       master bib  -> bibliography.html (alphabetical, anchored)
  gen-glossary  glossary v4 -> glossary.html (retired-terms section dropped)
  gen-notation  registry    -> symbol-registry.html ("Notation & Symbols")
  crossref      scan corpus for each bib entry's citations -> crossref index (md)

Discipline: cite the EXTERNAL source; strip every internal scaffolding field.
Stdlib only.
"""
import os, re, sys, html, unicodedata

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
BIB_MD   = os.path.join(ROOT, "research/literature/bibliography.md")
TA_HTML  = os.path.join(ROOT, "core/technical-appendix/TechnicalAppendix_v2.0.0.html")
GLOSS_V4 = os.path.join(ROOT, "core/glossary/commons_bonds_updated_glossary_v4.html")
REGISTRY = os.path.join(ROOT, "core/technical-appendix/symbol-registry_2026-06-07.md")
OUT_DIR  = os.path.join(ROOT, "manuscript/back-matter")

# ---- scaffolding markers: a citation ends where the first of these begins ----
SCAFFOLD_MARKERS = [
    "*Backs:*", "*Candidate", "*In-repo", "*Source:*", "*Sources:*",
    "**Backs", "— *Backs", "– *Backs", "*(Promoted", "*(Full entry",
    "Status:", "Confidence:", "**(verified", "*(verify", "*(end page",
]
SCAFFOLD_BULLET_FIELDS = re.compile(
    r"^\s*-\s+\*\*(Summary|Relevance|Relationship|Chapter relevance|Framework character|"
    r"Status|Rigor provenance|Path B note|Grounds|Available at|Nobel|2026-|Why|How to apply)"
    r"\b", re.I)

# sub-section headers that are NOT bibliographic entries
NON_ENTRY_HEADINGS = re.compile(
    r"^(Published journalism|Regulatory record|Books and book journalism|"
    r"Institutional / biographical context|Additional public-record items|"
    r"Allison Colden public record|Hampton historical record|From the outreach|"
    r"Statutes / regulations|Agency / IGO|Notes|Maintenance notes|Cross-references)",
    re.I)

# sections / sub-sections to EXCLUDE from the reader-facing bibliography
EXCLUDE_SECTION = re.compile(
    r"(Candidate sources|Still pending pin|Supporting sources not yet integrated|"
    r"Maintenance notes|Cross-references|Still-UNSOURCED)", re.I)

YEAR_RE = re.compile(r"\b(1[5-9]\d\d|20\d\d)\b")


def slugify(s):
    s = unicodedata.normalize("NFKD", s).encode("ascii", "ignore").decode()
    s = re.sub(r"[^a-zA-Z0-9]+", "-", s).strip("-").lower()
    return s or "x"


def first_author_surname(citation):
    """Heuristic surname of the first author/org from a citation string."""
    c = re.sub(r"<[^>]+>", "", citation).strip()
    # institutional authors (no comma-first-name pattern): take up to first period
    head = c.split(".")[0].strip()
    if "," in c.split(".")[0]:
        # 'Ostrom, Elinor' -> Ostrom ; 'Darity, William A., Jr., and ...' -> Darity
        return c.split(",")[0].strip()
    # 'U.S. Census Bureau' / 'Chesapeake Bay Foundation' -> whole head
    return head


def md_to_text(s):
    s = re.sub(r"\*\*([^*]+)\*\*", r"\1", s)   # bold
    s = re.sub(r"(?<!\*)\*(?!\*)([^*]+)\*", r"\1", s)  # italic -> plain (titles kept by html gen separately)
    s = re.sub(r"`([^`]+)`", r"\1", s)
    s = re.sub(r"\[([^\]]+)\]\([^)]+\)", r"\1", s)  # md links -> text
    return s.strip()


def truncate_at_scaffold(s):
    cut = len(s)
    for m in SCAFFOLD_MARKERS:
        i = s.find(m)
        if i != -1:
            cut = min(cut, i)
    return s[:cut].strip().rstrip("—–-").strip()


# ---------------------------------------------------------------- master bib --
def parse_master_bib(path):
    """Return list of dicts: {citation(md), surname, year, section, kind, line}."""
    entries = []
    section = ""
    with open(path, encoding="utf-8") as f:
        lines = f.readlines()
    i = 0
    while i < len(lines):
        line = lines[i].rstrip("\n")
        m = re.match(r"^##\s+(.*)$", line)
        if m and not line.startswith("###"):
            section = m.group(1).strip()
            i += 1
            continue
        # heading-style entries (### or ####)
        mh = re.match(r"^(#{3,4})\s+(.*)$", line)
        if mh:
            text = mh.group(2).strip()
            if not NON_ENTRY_HEADINGS.match(text) and (YEAR_RE.search(text) or "*" in text or "<em>" in text):
                if not EXCLUDE_SECTION.search(section):
                    ym = YEAR_RE.search(text)
                    entries.append({
                        "citation": text,
                        "surname": first_author_surname(text),
                        "year": ym.group(1) if ym else "",
                        "section": section, "kind": "scholarly", "line": i + 1,
                    })
            i += 1
            continue
        # data bullets in §23 / §24 (only when inside those sections)
        if re.match(r"^##\s*2[34]\b", "## " + section) or section.startswith("23") or section.startswith("24"):
            mb = re.match(r"^-\s+\*\*(.+)$", line)
            if mb and not SCAFFOLD_BULLET_FIELDS.match(line) and not EXCLUDE_SECTION.search(section):
                raw = "- " + mb.group(1)
                raw = re.sub(r"^-\s+", "", raw)
                cite = truncate_at_scaffold(raw)
                cite = md_to_text(cite)
                if YEAR_RE.search(cite) or len(cite) > 25:
                    ym = YEAR_RE.search(cite)
                    entries.append({
                        "citation": cite,
                        "surname": first_author_surname(cite),
                        "year": ym.group(1) if ym else "",
                        "section": section, "kind": "data", "line": i + 1,
                    })
        i += 1
    return entries


# ----------------------------------------------------------------- TA §18 ------
def parse_ta_bib(path):
    """Return list of {citation_html, surname, year} from <section id=sec-18-bibliography>."""
    with open(path, encoding="utf-8") as f:
        txt = f.read()
    m = re.search(r'<section id="sec-18-bibliography">(.*?)</section>', txt, re.S)
    if not m:
        return []
    body = m.group(1)
    entries = []
    for li in re.findall(r"<li>\s*(.*?)\s*</li>", body, re.S):
        cite = re.sub(r"\s+", " ", li).strip()
        plain = re.sub(r"<[^>]+>", "", cite)
        plain = html.unescape(plain)
        ym = YEAR_RE.search(plain)
        entries.append({
            "citation_html": cite, "citation": plain,
            "surname": first_author_surname(plain),
            "year": ym.group(1) if ym else "",
        })
    return entries


def key_of(e):
    return (slugify(e["surname"]), e.get("year", ""))


# ----------------------------------------------------------------- commands ----
def cmd_fold_report():
    master = parse_master_bib(BIB_MD)
    ta = parse_ta_bib(TA_HTML)
    mkeys = {key_of(e) for e in master}
    only = [e for e in ta if key_of(e) not in mkeys]
    print(f"master entries parsed : {len(master)}")
    print(f"TA §18 entries parsed : {len(ta)}")
    print(f"TA-§18-ONLY (not in master by surname+year): {len(only)}\n")
    for e in sorted(only, key=lambda x: x["surname"].lower()):
        print(f"  [{e['surname']:<22}|{e['year']}] {e['citation']}")
    # also: master-only surnames count (informational)
    takeys = {key_of(e) for e in ta}
    monly = [e for e in master if key_of(e) not in takeys]
    print(f"\nmaster-only (not in TA §18): {len(monly)} (expected large — journalism/data)")


# entries that LOOK §18-only by surname+year but are duplicates already in master
FOLD_EXCLUDE_SURNAMES = {"bassett-bell"}  # garbled dup of Himmelstein 2022 (in master §18.5)


def html_citation_to_md(cite_html):
    s = cite_html.replace("<em>", "*").replace("</em>", "*")
    s = re.sub(r"<[^>]+>", "", s)
    s = html.unescape(s)
    return re.sub(r"\s+", " ", s).strip()


def cmd_fold_emit():
    master = parse_master_bib(BIB_MD)
    ta = parse_ta_bib(TA_HTML)
    mkeys = {key_of(e) for e in master}
    only = [e for e in ta if key_of(e) not in mkeys
            and slugify(e["surname"]) not in FOLD_EXCLUDE_SURNAMES]
    only.sort(key=lambda x: x["surname"].lower())
    print("## 25. Technical Appendix academic citations (folded from TA §18, 2026-06-09)\n")
    print("**Added 2026-06-09 (back-matter consolidation).** These are the academic works "
          "cited inline in the Technical Appendix that had no entry in this master. Folding "
          "them here makes this file the single bibliographic source of truth; the TA's §18 "
          "list is regenerated from it. Discipline: cite the external source. Where-cited is "
          "recorded for orphan-detection; titles/venues are carried verbatim from §18.\n")
    for e in only:
        print(f"### {html_citation_to_md(e['citation_html'])}\n")
        print("- **Where cited:** Technical Appendix §18 (academic citation referenced inline). "
              "Folded from §18 into the master 2026-06-09.\n")


def main():
    cmd = sys.argv[1] if len(sys.argv) > 1 else ""
    if cmd == "fold-report":
        cmd_fold_report()
    elif cmd == "fold-emit":
        cmd_fold_emit()
    else:
        print(__doc__)
        print("commands: fold-report | gen-bib | gen-glossary | gen-notation | crossref")


if __name__ == "__main__":
    main()
