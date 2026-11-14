#!/usr/bin/env python3
"""Print copies of a chapter: a clean reader copy and a final-read copy for the author.

Usage (from the repo root):
  python3 tools/scripts/build-chapter-print-copies.py CHAPTER.md READER.pdf READCOPY.pdf
Reader copy: the text only, EB Garamond, page numbers. Read copy: the same text with
paragraph numbers and a blank margin column for hand marks. HTML comments are stripped,
quotes and apostrophes are curled, '---' becomes centered asterisks. Nothing else changes.
Needs the pre-installed Playwright Chromium (node) and the EB Garamond system font.
"""
import re, html, sys, subprocess, tempfile, os, json
src, reader_pdf, read_pdf = sys.argv[1:4]
raw = re.sub(r'<!--.*?-->', '', open(src).read(), flags=re.S)
lines = [x.strip() for x in raw.split('\n') if x.strip()]

def curl(s):
    s = re.sub(r'(^|[\s(\[])"', lambda m: m.group(1) + '“', s)
    s = s.replace('"', '”')
    s = re.sub(r"(^|[\s(\[“])'", lambda m: m.group(1) + '‘', s)
    return s.replace("'", '’')
def fmt(s):
    return re.sub(r'\*(.+?)\*', r'<i>\1</i>', html.escape(curl(s), quote=False))

book = chapter = byline = ''
rows = []  # (kind, text)
for x in lines:
    if x.startswith('# '): book = x[2:]
    elif x.startswith('*By '): byline = x.strip('*')
    elif x.startswith('## Chapter'): chapter = x[3:]
    elif x.startswith('## '): rows.append(('h', x[3:]))
    elif x == '---': rows.append(('r', ''))
    else: rows.append(('p', x))
words = sum(len(t.split()) for k, t in rows if k == 'p')
npar = sum(1 for k, _ in rows if k == 'p')

BASE = '''@page{size:Letter;margin:1in 1in 1in 1in}
body{font-family:"EB Garamond",Georgia,serif;font-size:12.5pt;line-height:1.5;color:#111}
h1{font-size:20pt;font-weight:normal;margin:0 0 .2em}.by{font-style:italic;margin:0 0 2.2em}
.book{font-variant:small-caps;letter-spacing:.06em;margin:0 0 .3em}
h2{font-size:14pt;font-weight:bold;margin:1.8em 0 .5em;break-after:avoid}
p{margin:0 0 .85em;orphans:2;widows:2}.r{text-align:center;margin:1.4em 0}'''
def head(extra=''):
    return (f'<!doctype html><meta charset="utf-8"><title>{html.escape(chapter)}</title><style>{BASE}{extra}</style>'
            f'<p class="book">{fmt(book)}</p><h1>{fmt(chapter)}</h1><p class="by">{fmt(byline)}</p>')

reader = head()
for k, t in rows:
    reader += {'h': f'<h2>{fmt(t)}</h2>', 'r': '<p class="r">* * *</p>', 'p': f'<p>{fmt(t)}</p>'}[k]

READ = '''@page{margin:.8in .6in .8in .6in}table{border-collapse:collapse;width:100%}
td{vertical-align:top;padding:0}td.n{width:.45in;font:8.5pt Helvetica,Arial,sans-serif;color:#777;padding-top:.35em}
td.t{width:4.6in}td.m{border-left:.5pt solid #999}tr.h td{padding-top:.6em}.note{font:9pt Helvetica,Arial,sans-serif;color:#444;margin:0 0 1.4em}'''
read = head(READ) + f'<p class="note">Final-read copy. {words:,} words, {npar} paragraphs. Small numbers count paragraphs. The right-hand column is for your marks.</p><table>'
n = 0
for k, t in rows:
    if k == 'h': read += f'<tr class="h"><td></td><td class="t"><h2>{fmt(t)}</h2></td><td class="m"></td></tr>'
    elif k == 'r': read += '<tr><td></td><td class="t"><p class="r">* * *</p></td><td class="m"></td></tr>'
    else:
        n += 1; read += f'<tr><td class="n">{n}</td><td class="t"><p>{fmt(t)}</p></td><td class="m"></td></tr>'
read += '</table>'

JS = '''const {chromium}=require('playwright');const jobs=JSON.parse(process.argv[2]);
(async()=>{const b=await chromium.launch();for(const [h,p,label] of jobs){const pg=await b.newPage();
await pg.goto('file://'+h);await pg.evaluate(()=>document.fonts.ready);
await pg.pdf({path:p,format:'Letter',preferCSSPageSize:true,printBackground:true,displayHeaderFooter:true,
headerTemplate:'<span></span>',
footerTemplate:'<div style="width:100%;padding:0 0.6in;font-family:Georgia,serif;font-size:8.5px;color:#555;display:flex;justify-content:space-between"><span>'+label+'</span><span><span class="pageNumber"></span> of <span class="totalPages"></span></span></div>'});
await pg.close()}await b.close()})();'''
with tempfile.TemporaryDirectory() as d:
    jobs = []
    for name, h, out, label in [('reader', reader, reader_pdf, chapter), ('read', read, read_pdf, chapter + ' · final-read copy')]:
        p = os.path.join(d, name + '.html'); open(p, 'w').write(h)
        jobs.append([p, os.path.abspath(out), html.escape(label)])
    js = os.path.join(d, 'r.js'); open(js, 'w').write(JS)
    subprocess.run(['node', js, json.dumps(jobs)], check=True, env={**os.environ, 'NODE_PATH': subprocess.run(['npm','root','-g'],capture_output=True,text=True).stdout.strip()})
print(f'{words:,} words, {npar} paragraphs ->', reader_pdf, read_pdf)
