#!/usr/bin/env python3
"""Ch 9 Session 1 check: do the pace draft (B) and the dinner-table draft (C) carry the same
figures, years, quotations and proper names? Prints anything found in one and not the other.
Usage: python3 ch09-compare-figures.py ch09-pace_2026-11-14.md ch09-dinner-table_2026-11-14.md"""
import re, sys
from collections import Counter
WORDS = ("one two three four five six seven eight nine ten eleven twelve thirteen seventeen thirty "
         "thirty-one thirty-four forty forty-four sixty hundred thousand million billion trillion "
         "fifth quarter").split()
def body(path):
    t = open(path, encoding="utf-8").read()
    t = re.sub(r"<!--.*?-->", "", t, flags=re.S)
    return t
def figures(t):
    nums = re.findall(r"\$?\d[\d,]*(?:\.\d+)?", t)
    words = [w.lower() for w in re.findall(r"[A-Za-z-]+", t) if w.lower() in WORDS]
    return Counter(n.rstrip(",.") for n in nums), set(words)
def quotes(t):
    return set(q.strip().rstrip(",.") for q in re.findall(r"[\"“]([^\"”]+)[\"”]", t))
def names(t):
    out = set()
    for m in re.finditer(r"(?<![.!?]\s)(?<!^)\b([A-Z][a-zé]+(?:[ -][A-Z][a-zé]+)*)", t, flags=re.M):
        out.add(m.group(1))
    return out
b, c = body(sys.argv[1]), body(sys.argv[2])
(nb, wb), (nc, wc) = figures(b), figures(c)
print("DIGIT FIGURES only in B:", sorted(set(nb) - set(nc)))
print("DIGIT FIGURES only in C:", sorted(set(nc) - set(nb)))
print("NUMBER WORDS only in B:", sorted(wb - wc))
print("NUMBER WORDS only in C:", sorted(wc - wb))
print("QUOTATIONS only in B:", sorted(quotes(b) - quotes(c)))
print("QUOTATIONS only in C:", sorted(quotes(c) - quotes(b)))
print("NAMES only in B:", sorted(names(b) - names(c)))
print("NAMES only in C:", sorted(names(c) - names(b)))
print("distinct digit figures:", len(set(nb)), "B /", len(set(nc)), "C; quotations:", len(quotes(b)), "B /", len(quotes(c)), "C")
pb = [x for x in b.split("\n\n") if x.strip() and not x.strip().startswith(("#", "*By"))]
pc = [x for x in c.split("\n\n") if x.strip() and not x.strip().startswith(("#", "*By"))]
print("paragraphs:", len(pb), "B /", len(pc), "C; words:", len(b.split()), "B /", len(c.split()), "C")
