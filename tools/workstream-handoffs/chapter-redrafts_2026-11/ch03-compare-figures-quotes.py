#!/usr/bin/env python3
"""Ch 3 two-drafts check (Session 1, 2026-11-14).
Compares A (current chapter), B (pace) and C (dinner-table):
  1. every italic span in A (quotations, titles, case names) must appear word for word in B and C;
  2. every number token (digits) in each version, set-compared;
  3. spelled-out figures and proper names from a hand list (the fact table's rows);
  4. paragraph counts of B and C (they must match so print numbers line up).
Run from the repo root:  python3 tools/workstream-handoffs/chapter-redrafts_2026-11/ch03-compare-figures-quotes.py
"""
import re, sys
D = "tools/workstream-handoffs/chapter-redrafts_2026-11/"
F = {"A": "manuscript/chapters/Chapter__3_TheWaterman.md",
     "B": D + "ch03-pace_2026-11-14.md",
     "C": D + "ch03-dinner-table_2026-11-14.md"}
def body(p):
    t = open(p, encoding="utf-8").read()
    t = re.sub(r"<!--.*?-->", "", t, flags=re.S)
    return t
T = {k: body(v) for k, v in F.items()}
def paras(t):
    return [p for p in re.split(r"\n\s*\n", t) if p.strip() and not p.startswith(("#", "---", "*By"))]
ALLOW_DROPPED_SPANS = set()
ok = True
print("== 1. Italic spans in A (quotations, titles, cases) ==")
spans = re.findall(r"(?<!\*)\*([^*\n]+)\*(?!\*)", T["A"])
for s in dict.fromkeys(spans):
    miss = [k for k in "BC" if s not in T[k]]
    if miss:
        if s not in ALLOW_DROPPED_SPANS: ok = False
        print(("  DROPPED (listed in change notes)" if s in ALLOW_DROPPED_SPANS else "  MISSING") + f" in {miss}: {s!r}")
print(f"  {len(set(spans))} distinct spans checked")

print("== 2. Number tokens ==")
num = lambda t: set(x.rstrip(",") for x in re.findall(r"\$?\d[\d,]*(?:\.\d+)?", t))
N = {k: num(v) for k, v in T.items()}
print("  in A, not in B:", sorted(N["A"] - N["B"]))
print("  in B, not in A:", sorted(N["B"] - N["A"]))
print("  B vs C differ :", sorted(N["B"] ^ N["C"]))
if N["B"] ^ N["C"]: ok = False

print("== 3. Spelled-out figures and names ==")
TERMS = """fifteen million bushels|under two hundred thousand|99 percent|two hundred thousand bushels|four stories|
more than thirty years|five years|sixth|six to two|forty percent|several hundred people|six states|forty years|
nearly two feet a year|a bit over a square mile|eight generations|twelve miles|more than fifty years|three years later|
roughly tripled|five |hundreds of acres|tens of millions|twelve words|two hundred oysters|
five-foot wave|thirty feet apart|one oar|six-pack of Coca-Cola|six bottles of Coca-Cola|quarter turn of the wrist|
late 1880s|late 1950s|late 1970s|late 1960s|1870s|1770s|early 2000s|
J.S. Darling and Son|Frank Darling|James McMenamin|Factory Point|Back River|Buckroe Beach|NASA Langley|Fox Hill|Old Point Comfort|
Newport News|Poquoson|Piankatank|Hudgins|Colden|Chris Moore|Goldsborough|Hardin|Ostrom|Reedville|Great Wicomico|Northumberland|
Nesslage|Latour|WHRO|Tonya O'Connor|Virginia Marine Resources Commission|Atlantic States Marine Fisheries Commission|
Chesapeake Bay Program|Mobjack Bay|Loudoun|Tangier|Eskridge|Cook Cannon|Thomson Reuters Foundation|Smith Island|Tilghman|
Pat Whewell|Lonnie Gowe|Broad Creek|Chumley Fisher|Chet Schwartz|Cameron Evans|Virginia Wesleyan|Andy Harris|Tarnowski|
Jason Ruth|Harris Seafood|Grasonville|James River|Restitution Bond|Mazzucato|Harvey|accumulation by dispossession|
Darity|Mullen|Coates|Army Corps of Engineers|National Oceanic and Atmospheric Administration|McDowell|Norway|Virginia General Assembly|
Gulf of Maine|Bristol Bay|West Africa|Mekong Delta|MSX|Dermo|Biggie|Indianapolis|Chile|Phoenix|Crabtown|oyster castles|deadrise|
Maryland Matters|Smithsonian Magazine|HRBT|Hampton Roads Bridge-Tunnel|Oslo|his lunch was waiting for him in the water, as fresh as it could be|
you get mud between your toes"""
for term in [x.strip() for x in TERMS.replace("\n","").split("|") if x.strip()]:
    c = {k: T[k].count(term) for k in "ABC"}
    flag = "" if (c["B"]>0)==(c["C"]>0) and ((c["A"]>0)==(c["B"]>0)) else "   <-- differs"
    if (c["B"]>0)!=(c["C"]>0): ok = False
    if flag: print(f"  {term!r}: A={c['A']} B={c['B']} C={c['C']}{flag}")
print("  (only rows that differ are printed)")

print("== 4. Paragraphs and words ==")
for k in "ABC":
    print(f"  {k}: {len(paras(T[k]))} paragraphs, {len(re.findall(r'\S+', T[k]))} words")
if len(paras(T["B"])) != len(paras(T["C"])): ok = False; print("  B and C paragraph counts differ")
print("RESULT:", "PASS (B and C carry the same quotations, figures and names)" if ok else "CHECK THE ROWS ABOVE")
sys.exit(0 if ok else 1)
