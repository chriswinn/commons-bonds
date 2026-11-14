#!/usr/bin/env python3
"""Chapter 10: check that the current chapter (A), the pace draft (B) and the
dinner-table draft (C) carry the same figures, dates, names and quotations.
Run from the repo root. Each row lists the accepted spellings of one fact."""
import re, sys
A='manuscript/chapters/Chapter_10_CommonBonds.md'
B='tools/workstream-handoffs/chapter-redrafts_2026-11/ch10-pace_2026-11-14.md'
C='tools/workstream-handoffs/chapter-redrafts_2026-11/ch10-dinner-table_2026-11-14.md'
def load(p):
    t=open(p,encoding='utf-8').read()
    t=re.sub(r'<!--.*?-->','',t,flags=re.S)
    return re.sub(r'\s+',' ',t)
FACTS=[
 ('The sentence (verbatim)',['Value leaves the place it comes from, and the costs of its leaving stay behind.']),
 ('"The morning is what I came here to listen to." (verbatim)',['The morning is what I came here to listen to.']),
 ('Old Point Comfort',['Old Point Comfort']),('Newport News',['Newport News']),
 ('half a mile (author ruling)',['half a mile from where I am sitting']),
 ('Hampton',['Hampton']),
 ('waterman crabbing since twelve',['since he was twelve']),
 ('driver thirty nights',['thirty nights']),
 ('Baotou',['Baotou']),('Niger Delta',['Niger Delta']),('Texas Panhandle',['Texas Panhandle']),('Ogallala',['Ogallala']),
 ('Mars: ten thousand people',['ten thousand people']),
 ('"In a sealed dome there is no away." (verbatim)',['In a sealed dome there is no away.']),
 ('Mars lines (verbatim, author ruling)',['There is no downwind. There is no later generation in another country who will absorb the loss out of sight. Everyone who would bear the cost is in the room, breathing the same recycled air.']),
 ('Mars repeat sentence (verbatim, author ruling)',['Everyone breathes the same air; everyone drinks the same drawn-down water; the cost-bearer and the value-capturer are in the same room by physical necessity.']),
 ('McDowell County',['McDowell County']),('2008',['2008']),('pyramids',['pyramids']),
 ('"cost of doing business"',['cost of doing business']),
 ('two centuries of carbon',['two centuries of carbon']),
 ('NASA Langley, twelve miles',['twelve miles']),('NASA Langley',['NASA Langley']),
 ('patented work (verbatim)',['His patented work extended the discipline past the tunnel itself.']),
 ('Nordhaus',['Nordhaus']),('Stern',['Stern']),('Weitzman',['Weitzman']),('Norway',['Norway']),('Europa',['Europa']),
 ('years 1860 / 1960 / 1995 / 2027',['1860'],),('1960',['1960']),('1995',['1995']),('2027',['2027']),
 ('"no standing to price" (verbatim)',['There are harms I have no standing to price, and I leave the figure to those who do.']),
 ('Treaty of Fort Laramie 1868',['1868']),('Fort Laramie',['Fort Laramie']),('Ȟe Sápa',['Ȟe Sápa']),
 ('Great Sioux Reservation',['Great Sioux Reservation']),
 ('Custer expedition, six years later',['Six years later the Custer expedition']),
 ('February of 1877',['February of 1877']),
 ('1980 ruling',['1980']),('case name',['United States v. Sioux Nation of Indians']),
 ('award about 17.5 million',['seventeen and a half million dollars','$17.5 million']),
 ('five percent',['five percent']),
 ('about 106 million by 1980',['a hundred and six million dollars','$106 million']),
 ('trust more than 1.5 billion',['one and a half billion dollars','$1.5 billion']),
 ('more than four decades',['more than four decades']),
 ('"I do not say who else may" (verbatim)',['and I do not, and I do not say who else may.']),
 ('Kimmerer',['Robin Wall Kimmerer, of the Citizen Potawatomi']),
 ('Simpson',['Leanne Betasamosake Simpson, of the Michi Saagiig Nishnaabeg']),
 ('Coulthard',['Glen Coulthard, of the Yellowknives Dene']),
 ('Dunbar-Ortiz',['Roxanne Dunbar-Ortiz']),
 ('Deloria',['Vine Deloria Jr., of the Standing Rock Sioux']),
 ('Polanyi',['Polanyi']),('Pistor',['Pistor']),('Christophers',['Christophers']),('Sandel',['Michael Sandel']),
 ('Pistor friend lines (verbatim, author ruling)',['I met Pistor earlier in the book as a friend, a diagnostician on my side. The honest thing is to admit that the same diagnosis can be turned around and aimed at me.']),
 ('"already has a number, and that number is zero" (verbatim)',['the thing already has a number, and that number is zero']),
 ('pharaohs / Qin / feudal lords',['pharaohs']),('Qin',['Qin emperors']),('feudal',['Feudal lords']),
 ('Camus 1942',['1942']),('Camus title',['Le Mythe de Sisyphe']),
 ('Camus quotation (verbatim)',['Il faut imaginer Sisyphe heureux.']),('Camus translation',['One must imagine Sisyphus happy.']),
 ('closing lines (verbatim)',['The kettle is on. The dog is up. The day is made of small attentions, and they are waiting.']),
 ('"Let us begin."',['Let us begin.']),
 ('water my grandfather might have known',['water my grandfather might have known']),
]
MUST_BE_ABSENT=[('settler self-description',r'I am a settler|written by a settler|a settler author'),
 ('grandfather named (author ruling: Pooh only)',r'LaVern'),('universal floors (map cut)',r'[Uu]niversal floors'),
 ('wife / hospital weeks (author gap)',r'my wife|nearly died')]
txt={k:load(p) for k,p in (('A',A),('B',B),('C',C))}
bad=0
print('| Fact | A current | B pace | C dinner-table |\n|---|---|---|---|')
for row in FACTS:
    name,alts=row[0],row[1]
    r=[('yes' if any(a in txt[k] for a in alts) else 'NO') for k in 'ABC']
    if 'NO' in r: bad+=1
    print(f'| {name} | {r[0]} | {r[1]} | {r[2]} |')
print('\n| Must be absent from B and C | A current | B pace | C dinner-table |\n|---|---|---|---|')
for name,pat in MUST_BE_ABSENT:
    r=[('present' if re.search(pat,txt[k]) else 'absent') for k in 'ABC']
    if 'present' in r[1:]: bad+=1
    print(f'| {name} | {r[0]} | {r[1]} | {r[2]} |')
# every numeral and year in B must be in C and the reverse
nb=set(re.findall(r'\$?\d[\d,.]*\d|\d',txt['B'])); nc=set(re.findall(r'\$?\d[\d,.]*\d|\d',txt['C']))
print('\nNumerals only in B:',sorted(nb-nc) or 'none','| only in C:',sorted(nc-nb) or 'none')
if nb!=nc: bad+=1
def heads(p): return [l.strip() for l in open(p,encoding='utf-8') if l.startswith('#')]
print('Headings identical in B and C:', heads(B)==heads(C))
if heads(B)!=heads(C): bad+=1
for k,p in (('A',A),('B',B),('C',C)): print(f'Words {k}:',len(txt[k].split()))
print('\nRESULT:', 'all rows match' if bad==0 else f'{bad} row(s) need attention')
sys.exit(1 if bad else 0)
