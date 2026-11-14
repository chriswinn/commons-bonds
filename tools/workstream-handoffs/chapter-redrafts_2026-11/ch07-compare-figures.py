import re,sys
NUMW=r'(?:one|two|three|four|five|six|seven|eight|ten|twelve|twenty|thirty|forty|fifty|seventy|hundred|thousand|million|billion|forty-eight|twenty-three|thirteen)'
def load(p):
    t=open(p).read(); t=re.sub(r'<!--[\s\S]*?-->','',t)
    paras=[x for x in t.split('\n\n') if x.strip() and not x.startswith(('#','*By'))]
    return t,paras
def feats(t):
    digits=sorted(set(re.findall(r'\d[\d,.]*\d|\d',t)))
    words=sorted(set(w.lower() for w in re.findall(r'\b'+NUMW+r'(?:[ -]'+NUMW+r')*\b',t,flags=re.I)))
    quotes=sorted(set(re.findall(r'"([^"]+)"',t)))
    names=sorted(set(re.findall(r'\b(?:[A-Z][a-z]+(?:-\d)?(?: [A-Z][a-z]+)+|Giza|Khufu|Europa|Mars|Jupiter|Xi\'an|Stern|Nordhaus|Hartwick|Qin|McDowell|Wisconsin)\b',t)))
    return digits,words,quotes,names
b,bp=load(sys.argv[1]); c,cp=load(sys.argv[2])
print('paragraphs',len(bp),len(cp)); print('words',len(b.split()),len(c.split()))
for lab,x,y in zip(['digits','number-words','quotes','names'],feats(b),feats(c)):
    print(lab,'B only:',sorted(set(x)-set(y)),'| C only:',sorted(set(y)-set(x)))
    if lab in('digits','quotes'): print('   shared:',sorted(set(x)&set(y)))
