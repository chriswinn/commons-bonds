#!/usr/bin/env node
// render-html-pdf-paged.js — HTML → PDF with page numbers (Chromium via Playwright).
// Added 2026-11-12: the apt build of wkhtmltopdf (unpatched Qt) ignores footer
// switches, so build-derivatives*.sh cannot number pages. Use this for the
// Technical Appendix when page numbers are wanted.
//   node tools/scripts/render-html-pdf-paged.js <input.html> <output.pdf>
const path = require('path');
const { chromium } = require('playwright');
(async () => {
  const [input, output] = process.argv.slice(2);
  if (!input || !output) { console.error('usage: render-html-pdf-paged.js <input.html> <output.pdf>'); process.exit(2); }
  const browser = await chromium.launch();
  const page = await browser.newPage();
  await page.goto('file://' + path.resolve(input), { waitUntil: 'load' });
  await page.pdf({
    path: output, format: 'Letter', printBackground: true,
    margin: { top: '1in', bottom: '1in', left: '1in', right: '1in' },
    displayHeaderFooter: true, headerTemplate: '<span></span>',
    footerTemplate: '<div style="width:100%;text-align:center;font-family:Georgia,serif;font-size:9px;color:#555;"><span class="pageNumber"></span></div>',
  });
  await browser.close();
})();
