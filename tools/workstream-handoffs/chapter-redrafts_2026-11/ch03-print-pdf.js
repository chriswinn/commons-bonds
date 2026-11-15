// Print the three annotated Ch 3 HTML files to PDF with page numbers (pre-installed Playwright Chromium).
// Usage, from the repo root:  node tools/workstream-handoffs/chapter-redrafts_2026-11/ch03-print-pdf.js HTMLDIR OUTDIR
const { chromium } = require('playwright');
const fs = require('fs'), path = require('path');
(async () => {
  const [src, out] = process.argv.slice(2);
  const browser = await chromium.launch();
  for (const f of fs.readdirSync(src).filter(x => x.endsWith('.html'))) {
    const page = await browser.newPage();
    await page.goto('file://' + path.resolve(src, f));
    const title = await page.title();
    await page.pdf({
      path: path.join(out, f.replace('.html', '.pdf')), format: 'Letter', printBackground: true,
      displayHeaderFooter: true, headerTemplate: '<span></span>',
      footerTemplate: `<div style="font-family:DejaVu Sans,Arial,sans-serif;font-size:7pt;color:#666;width:100%;padding:0 0.5in;display:flex;justify-content:space-between"><span>${title}</span><span>page <span class="pageNumber"></span> of <span class="totalPages"></span></span></div>`,
      margin: { top: '0.6in', bottom: '0.7in', left: '0.5in', right: '0.5in' },
    });
    console.log('printed', f);
    await page.close();
  }
  await browser.close();
})();
