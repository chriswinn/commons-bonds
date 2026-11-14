#!/usr/bin/env python3
"""Ch 8 Session 1 check: do draft B (pace) and draft C (dinner-table) carry the same
figures, quotations, names and section headings? Run from this folder: python3 ch08-figure-compare.py"""
import re, sys
B_FILE, C_FILE = 'ch08-pace_2026-11-14.md', 'ch08-dinner-table_2026-11-14.md'
def body(f):
    return re.sub(r'<!--.*?-->', '', open(f, encoding='utf-8').read(), flags=re.S)
def figures(t):
    # every numeral, with a leading $ and a trailing unit word; trailing punctuation dropped
    return set(m.rstrip(',.') for m in re.findall(r'\$?\d[\d,]*(?:\.\d+)?(?: (?:billion|million|percent))?', t))
WORD_FIGS = ['hundred thousand', 'nineteen thousand', 'twelve hundred', 'thirteen years', 'eight and thirteen',
             'sixteenth', 'a fifth', 'twice', 'two decades', 'six times', 'three times', 'a century']
NAMES = ['Bailey', 'Hendryx', 'Rennert', 'Hotelling', 'Costanza', 'Dunbar', 'Du Bois', 'Fanon', 'Ellison',
         'Derickson', 'Wagner', 'Obama', 'Trump', 'Biden', 'Darity', 'Mullen', 'Hamilton', 'Conley', 'Coates',
         'Buchanan', 'Tullock', 'Pigou', 'Appalachian Voices', 'OpenSecrets', 'U.S. Steel', 'BP', 'Libby',
         'Baotou', 'Norway', 'Welch', 'Farmington', 'Black Lung Association', 'Pocahontas',
         'Government Accountability Office', 'Congressional Research Service', 'Energy Information Administration',
         'Geological Survey', 'Environmental Protection Agency']
B, C = body(B_FILE), body(C_FILE)
ok = True
fb, fc = figures(B), figures(C)
print(f'figures: B has {len(fb)} distinct, C has {len(fc)} distinct')
print('  only in B:', sorted(fb - fc) or 'none'); print('  only in C:', sorted(fc - fb) or 'none')
ok &= fb == fc
for w in WORD_FIGS:
    b, c = w in B, w in C
    if b != c or not b: ok = False; print(f'  WORD FIGURE MISMATCH {w!r}: B={b} C={c}')
qb, qc = (sorted(set(re.findall(r'"([^"]{12,})"', t))) for t in (B, C))
print('quotations identical:', qb == qc, f'({len(qb)})'); ok &= qb == qc
bad = [n for n in NAMES if not (n in B and n in C)]
print('names in both:', not bad, bad or ''); ok &= not bad
hb, hc = (re.findall(r'^## .*', t, flags=re.M) for t in (B, C))
print('section headings identical:', hb == hc, f'({len(hb)})'); ok &= hb == hc
pb, pc = (len([x for x in t.split('\n\n') if x.strip() and not x.lstrip().startswith('#')]) for t in (B, C))
print(f'paragraph blocks: B={pb} C={pc}'); print(f'words: B={len(B.split())} C={len(C.split())}')
print('RESULT:', 'PASS' if ok else 'FAIL'); sys.exit(0 if ok else 1)
