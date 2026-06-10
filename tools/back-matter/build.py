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
    c = re.sub(r"<[^>]+>", "", citation).strip().lstrip("*").strip()
    if "," in c.split(".")[0]:
        # 'Ostrom, Elinor' -> Ostrom ; 'Darity, William A., Jr., and ...' -> Darity
        return c.split(",")[0].strip()
    # institutional / no-comma: first 4 whitespace tokens (avoids the 'U.S.' period trap)
    return " ".join(c.split()[:4]).rstrip(".,;:").strip() or c[:24]


def md_to_text(s):
    s = s.replace("**", "")                         # flatten bold (handles nested *italic*)
    s = re.sub(r"`([^`]+)`", r"\1", s)
    s = re.sub(r"\[([^\]]+)\]\([^)]+\)", r"\1", s)   # md links -> link text
    return s.strip()                                # single-* italics preserved for the HTML gen


def truncate_at_scaffold(s):
    cut = len(s)
    for m in SCAFFOLD_MARKERS:
        i = s.find(m)
        if i != -1:
            cut = min(cut, i)
    return s[:cut].strip().rstrip("—–-").strip()


# ---------------------------------------------------------------- master bib --
# sub-section-number heading (e.g. "23.2 Candidate...", "§23.3 — ...", "24I. Indigenous", "23.1 In-repo")
SUBSECTION_NUM_HEADING = re.compile(r"^§?\d+(\.\d+)?[A-Z]?[.\s—-]")
# data-bullet sub-sections to EXCLUDE from reader-facing bib (claim-led / candidate / pending)
DATA_SUBSECTION_EXCLUDE = re.compile(
    r"(Candidate|23\.2|23\.3|Corpus-wide figure|From the outreach|Still pending|24K|Ch5 figure)", re.I)


def parse_master_bib(path, include_data=True):
    """Return list of dicts: {citation(md), surname, year, section, kind, line}."""
    entries = []
    section = ""
    subsection = ""   # tracks ### headings inside §23/§24 data sections
    with open(path, encoding="utf-8") as f:
        lines = f.readlines()
    i = 0
    while i < len(lines):
        line = lines[i].rstrip("\n")
        m = re.match(r"^##\s+(.*)$", line)
        if m and not line.startswith("###"):
            section = m.group(1).strip()
            subsection = ""
            i += 1
            continue
        # heading-style entries (### or ####)
        mh = re.match(r"^(#{3,4})\s+(.*)$", line)
        if mh:
            text = mh.group(2).strip()
            subsection = text  # remember even non-entry sub-headers for data-bullet routing
            is_subnum = bool(SUBSECTION_NUM_HEADING.match(text))
            if (not NON_ENTRY_HEADINGS.match(text) and not is_subnum
                    and (YEAR_RE.search(text) or "*" in text or "<em>" in text)
                    and not EXCLUDE_SECTION.search(section)):
                ym = YEAR_RE.search(text)
                entries.append({
                    "citation": text, "surname": first_author_surname(text),
                    "year": ym.group(1) if ym else "",
                    "section": section, "kind": "scholarly", "line": i + 1,
                })
            i += 1
            continue
        # data bullets in §23 / §24 (cleanly *Backs:*-delimited sub-sections only)
        if include_data and (section.startswith("23") or section.startswith("24")):
            mb = re.match(r"^-\s+(\*\*.+)$", line)   # keep the leading ** so md_to_text strips the pair
            if (mb and not SCAFFOLD_BULLET_FIELDS.match(line)
                    and not EXCLUDE_SECTION.search(section)
                    and not DATA_SUBSECTION_EXCLUDE.search(subsection)):
                raw = mb.group(1)
                cite = md_to_text(truncate_at_scaffold(raw)).strip()
                cite = re.sub(r"\s*(HIGH|MED(IUM)?|LOW)\b.*$", "", cite).strip()  # drop confidence tail
                cite = cite.rstrip(".") + "." if cite and not cite.endswith(".") else cite
                if len(cite) > 25:
                    ym = YEAR_RE.search(cite)
                    entries.append({
                        "citation": cite, "surname": first_author_surname(cite),
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


# ----------------------------------------------------------- shared HTML -------
HEAD_CSS = """    <style>
        body { font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', system-ui, sans-serif;
            line-height: 1.6; max-width: 820px; margin: 0 auto; padding: 40px 20px;
            color: #333; background-color: #fff; }
        .header { text-align: center; margin-bottom: 36px; border-bottom: 2px solid #eee; padding-bottom: 18px; }
        h1 { font-size: 28px; margin-bottom: 6px; color: #2c3e50; }
        .subtitle { font-size: 16px; color: #666; font-style: italic; }
        h2 { font-size: 20px; margin: 30px 0 12px 0; color: #34495e;
            border-bottom: 2px solid #3498db; padding-bottom: 6px; }
        ul.bib { list-style: none; padding-left: 0; }
        ul.bib li { margin: 0 0 14px 0; padding-left: 1.6em; text-indent: -1.6em; }
        ul.bib li:target { background: #fdf6e3; outline: 3px solid #fdf6e3; }
        table.notation { border-collapse: collapse; width: 100%; }
        table.notation th, table.notation td { border: 1px solid #ddd; padding: 7px 10px;
            text-align: left; vertical-align: top; }
        table.notation th { background: #f3f6f9; }
        table.notation td.sym { font-weight: bold; white-space: nowrap; }
        @media print { body { color: #000; background: #fff; } }
    </style>"""


def html_doc(title, body):
    return (f"<!DOCTYPE html>\n<html lang=\"en\">\n<head>\n    <meta charset=\"UTF-8\">\n"
            f"    <meta name=\"viewport\" content=\"width=device-width, initial-scale=1.0\">\n"
            f"    <title>{html.escape(title)}</title>\n{HEAD_CSS}\n</head>\n<body>\n{body}\n"
            f"</body>\n</html>\n")


def md_citation_to_html(cit):
    s = html.escape(cit, quote=False)
    s = s.replace("**", "")                               # flatten bold first
    s = re.sub(r"\*([^*]+)\*", r"<em>\1</em>", s)          # italics
    s = re.sub(r"\[([^\]]+)\]\((https?://[^)]+)\)", r'<a href="\2">\1</a>', s)
    s = s.replace("--", "&ndash;")
    return s.strip()


# ---------------------------------------------------------- gen-bibliography ---
def title_sig(citation):
    for pat in (r"\*([^*]+)\*", r"<em>(.*?)</em>", r'"([^"]+)"'):
        m = re.search(pat, citation)
        if m:
            return slugify(m.group(1))[:40]
    return slugify(citation)[:40]


def cmd_gen_bib():
    entries = parse_master_bib(BIB_MD)
    seen, uniq = {}, []
    for e in entries:
        k = (slugify(e["surname"]), e["year"], title_sig(e["citation"]))
        if k in seen:
            continue
        seen[k] = True
        uniq.append(e)
    uniq.sort(key=lambda e: (slugify(e["surname"]), e["year"], title_sig(e["citation"])))
    used, lis = {}, []
    for e in uniq:
        base = "bib-" + slugify(e["surname"]) + ("-" + e["year"] if e["year"] else "")
        slug = base
        n = used.get(base, 0)
        if n:
            slug = f"{base}-{n+1}"
        used[base] = n + 1
        lis.append(f'    <li id="{slug}">{md_citation_to_html(e["citation"])}</li>')
    body = ('  <div class="header">\n    <h1>Commons Bonds</h1>\n'
            '    <p class="subtitle">Bibliography</p>\n    <p class="subtitle">By Chris Winn</p>\n  </div>\n'
            '  <p>Works cited across the book, its essays, and the Technical Appendix, '
            'with primary data and agency sources, in a single alphabetical list. '
            'Each entry carries a stable anchor for cross-reference linking.</p>\n'
            '  <ul class="bib">\n' + "\n".join(lis) + "\n  </ul>")
    out = os.path.join(OUT_DIR, "bibliography.html")
    with open(out, "w", encoding="utf-8") as f:
        f.write(html_doc("Commons Bonds — Bibliography", body))
    print(f"wrote {out}  ({len(uniq)} unique entries from {len(entries)} parsed)")


# -------------------------------------------------------------- gen-glossary ---
def cmd_gen_glossary():
    with open(GLOSS_V4, encoding="utf-8") as f:
        txt = f.read()
    # drop the retired/superseded section (scaffolding; must not appear reader-facing).
    # retired-section is the last div before the centered footer paragraph; greedy to its last </div>.
    txt = re.sub(r'<div class="retired-section">.*</div>\s*(?=<p style="text-align: center)',
                 "", txt, flags=re.S)
    # also drop the now-unused .retired-section CSS rules from the <style> block
    txt = re.sub(r'\n\s*\.retired-section[^{]*\{[^}]*\}', "", txt)
    # strip version markers
    txt = txt.replace("Commons Bonds — Glossary v4", "Commons Bonds — Glossary")
    txt = re.sub(r'<p class="subtitle">Glossary — v4</p>', '<p class="subtitle">Glossary</p>', txt)
    txt = re.sub(r'<p class="subtitle" style="font-size:13px; color:#999;">[^<]*</p>', "", txt)
    txt = re.sub(r'<em>Commons Bonds Glossary v4 — [^<]*</em>', "<em>Commons Bonds — Glossary</em>", txt)
    # inject per-term anchors
    def anchor(m):
        name = re.sub(r"<[^>]+>", "", m.group(1))
        slug = "term-" + slugify(name)
        return f'<div class="term" id="{slug}">\n        <div class="term-name">{m.group(1)}</div>'
    txt = re.sub(r'<div class="term">\s*<div class="term-name">(.*?)</div>', anchor, txt, flags=re.S)
    out = os.path.join(OUT_DIR, "glossary.html")
    with open(out, "w", encoding="utf-8") as f:
        f.write(txt)
    n = txt.count('class="term-name"')
    assert "retired-section" not in txt and "uperseded" not in txt, "retired/superseded leaked!"
    print(f"wrote {out}  ({n} terms; retired-section dropped; anchors injected)")


# -------------------------------------------------------------- gen-notation ---
def parse_registry_part2():
    with open(REGISTRY, encoding="utf-8") as f:
        txt = f.read()
    m = re.search(r"## PART 2 .*?(?=\n## PART 3)", txt, re.S)
    region = m.group(0) if m else ""
    rows = []
    cur_hdr = None
    for line in region.splitlines():
        if not line.strip().startswith("|"):
            cur_hdr = None
            continue
        # split on UNescaped pipes ( \| is a literal pipe inside a cell, e.g. S(t|t0) )
        protected = line.strip().replace(r"\|", "\x00")
        cells = [c.strip().replace("\x00", "|") for c in protected.strip("|").split("|")]
        if re.match(r"^[\s:|-]+$", line.replace("|", "")):  # separator row
            continue
        low = [c.lower() for c in cells]
        if ("glyph" in low or "symbol" in low) and "meaning" in low:
            cur_hdr = low
            continue
        if cur_hdr:
            d = dict(zip(cur_hdr, cells))
            sym = d.get("glyph") or d.get("symbol") or ""
            meaning = d.get("meaning", "")
            units = d.get("units", "")
            if not sym or sym.startswith("~~"):   # skip dropped symbols
                continue
            sym = re.sub(r"\*\*|`", "", sym).strip()
            meaning = re.sub(r"\*\*|`|~~", "", meaning).strip()
            units = re.sub(r"\*\*|`", "", units).strip()
            if sym and meaning:
                rows.append((sym, meaning, units))
    return rows


def cmd_gen_notation():
    rows = parse_registry_part2()
    trs = []
    for sym, meaning, units in rows:
        u = "" if units in ("—", "") else units
        trs.append(f'    <tr><td class="sym">{html.escape(sym)}</td>'
                   f'<td>{html.escape(meaning)}</td><td>{html.escape(u)}</td></tr>')
    body = ('  <div class="header">\n    <h1>Commons Bonds</h1>\n'
            '    <p class="subtitle">Notation &amp; Symbols</p>\n    <p class="subtitle">By Chris Winn</p>\n  </div>\n'
            '  <p>Symbols used in the Technical Appendix and the book&rsquo;s quantitative passages. '
            'Standard conventions are preserved where the framework follows them; deliberate '
            'redefinitions are noted in the meaning.</p>\n'
            '  <table class="notation">\n    <tr><th>Symbol</th><th>Meaning</th><th>Units</th></tr>\n'
            + "\n".join(trs) + "\n  </table>")
    out = os.path.join(OUT_DIR, "symbol-registry.html")
    with open(out, "w", encoding="utf-8") as f:
        f.write(html_doc("Commons Bonds — Notation & Symbols", body))
    print(f"wrote {out}  ({len(rows)} symbols)")


def main():
    cmd = sys.argv[1] if len(sys.argv) > 1 else ""
    if cmd == "fold-report":
        cmd_fold_report()
    elif cmd == "fold-emit":
        cmd_fold_emit()
    elif cmd == "gen-bib":
        cmd_gen_bib()
    elif cmd == "gen-glossary":
        cmd_gen_glossary()
    elif cmd == "gen-notation":
        cmd_gen_notation()
    elif cmd == "gen-all":
        cmd_gen_bib(); cmd_gen_glossary(); cmd_gen_notation()
    else:
        print(__doc__)
        print("commands: fold-report | gen-bib | gen-glossary | gen-notation | crossref")


if __name__ == "__main__":
    main()
