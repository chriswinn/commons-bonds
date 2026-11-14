#!/usr/bin/env python3
"""Compare the figures, years and quotations carried by two or three drafts of a chapter.
Usage: compare-figures.py A.md B.md [C.md]
Prints every number token and every quoted string with its count per file, and lists any that differ.
A difference is a prompt to look, not an error: the dinner-table draft may repeat a figure when it explains it."""
import re, sys, collections
def load(p):
    t = open(p, encoding='utf-8').read()
    t = re.sub(r'<!--.*?-->', '', t, flags=re.S)
    return t
NUM = re.compile(r'\$?\d[\d,]*(?:\.\d+)?(?:[–-]\d[\d,]*(?:\.\d+)?)?(?:\s?(?:percent|billion|million|trillion))?')
QUO = re.compile(r'[“"]([^”"]{4,})[”"]')
def toks(t):
    return collections.Counter(m.group(0).strip().rstrip(',.') for m in NUM.finditer(t)), collections.Counter(m.group(1).strip().rstrip('.,') for m in QUO.finditer(t))
files = sys.argv[1:]
data = [toks(load(f)) for f in files]
def sec_paras(t):
    out, cur = collections.OrderedDict(), None
    for block in re.split(r'\n\s*\n', t):
        b = block.strip()
        if b.startswith('## '): cur = b[3:]; out[cur] = 0
        elif cur and b and not b.startswith('#'): out[cur] += 1
    return out
for kind, i in (('NUMBERS', 0), ('QUOTATIONS', 1)):
    keys = sorted(set().union(*[d[i].keys() for d in data]))
    present_diff = [k for k in keys if len({bool(d[i][k]) for d in data}) > 1]
    count_diff = [k for k in keys if k not in present_diff and len({d[i][k] for d in data}) > 1]
    print(f'== {kind}: {len(keys)} distinct; in some files but not all: {len(present_diff)}; same set, different counts: {len(count_diff)}')
    for k in present_diff: print('   MISSING SOMEWHERE:', repr(k), [d[i][k] for d in data])
    for k in count_diff: print('   count differs:', repr(k), [d[i][k] for d in data])
print('== PARAGRAPHS PER SECTION')
sp = [sec_paras(load(f)) for f in files]
for s in sp[0]:
    row = [x.get(s) for x in sp]
    print('  ', 'OK ' if len(set(row)) == 1 else 'DIFF', row, s)
print('   totals', [sum(x.values()) for x in sp], ' words', [len(load(f).split()) for f in files])
