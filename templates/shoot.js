// Render a manifest of HTML files to PNG with headless Chromium.
// usage: node shoot.js manifest.json
const { chromium } = require('playwright');
const fs = require('fs');
(async () => {
  const jobs = JSON.parse(fs.readFileSync(process.argv[2], 'utf8'));
  const browser = await chromium.launch();
  const ctx = await browser.newContext({ deviceScaleFactor: 1 });
  const page = await ctx.newPage();
  let n = 0;
  for (const j of jobs) {
    await page.setViewportSize({ width: j.w, height: j.h });
    await page.goto('file://' + j.html, { waitUntil: 'load' });
    await page.evaluate(() => document.fonts.ready);
    await page.evaluate(() => window.__fit && window.__fit());
    const warn = await page.evaluate(() => window.__warn || []);
    if (warn.length) console.log('WARN', j.png, JSON.stringify(warn));
    await page.screenshot({ path: j.png, clip: { x: 0, y: 0, width: j.w, height: j.h } });
    n++;
  }
  await browser.close();
  console.log('rendered', n);
})();
