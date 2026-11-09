const { chromium } = require('playwright');
const [,, htmlPath, outPath, label] = process.argv;
(async () => {
  const browser = await chromium.launch();
  const page = await browser.newPage();
  await page.goto('file://' + htmlPath, { waitUntil: 'networkidle' });
  const header = `<div style="font-family:Georgia,serif;font-size:8px;color:#444;width:100%;padding:0 14mm 0 24mm;">${label}</div>`;
  const footer = `<div style="font-family:Georgia,serif;font-size:8px;color:#444;width:100%;text-align:right;padding:0 20mm 0 24mm;">Page <span class="pageNumber"></span> / <span class="totalPages"></span></div>`;
  await page.pdf({ path: outPath, format: 'Letter', printBackground: true,
    displayHeaderFooter: true, headerTemplate: header, footerTemplate: footer,
    margin: { top: '20mm', bottom: '18mm', left: '24mm', right: '52mm' } });
  await browser.close();
  console.log('wrote ' + outPath);
})().catch(e => { console.error(e); process.exit(1); });
