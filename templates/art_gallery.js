// Renders every 2D art in reels/_engine/scene.js at time lt into one PNG (QA / catalogue).
// usage: node art_gallery.js <out.png> [lt=2.5]
const { chromium } = require('playwright'); const fs = require('fs'), path = require('path');
const ROOT = path.join(__dirname, '..'); const out = process.argv[2]; const lt = Number(process.argv[3] || 2.5);
const FD = path.join(ROOT, 'reels/_engine/fonts');
(async () => {
  const b = await chromium.launch(); const p = await b.newPage({ viewport: { width: 1860, height: 2100 } });
  await p.setContent('<body style="margin:0"><canvas id="c" width="1860" height="2100"></canvas></body>');
  await p.addScriptTag({ content: fs.readFileSync(path.join(ROOT, 'reels/_engine/scene.js'), 'utf8') });
  const fonts = fs.readdirSync(FD).map((f) => { const m = f.match(/^(\w+)-(\d+)/); return [m[1], m[2], 'data:font/woff;base64,' + fs.readFileSync(path.join(FD, f)).toString('base64')]; });
  const data = await p.evaluate(async ({ fonts, lt }) => {
    await Promise.all(fonts.map(([f, w, u]) => new FontFace(f, `url(${u})`, { weight: w }).load().then((x) => document.fonts.add(x))));
    const ctx = document.getElementById('c').getContext('2d'); ctx.fillStyle = '#C9D5EA'; ctx.fillRect(0, 0, 1860, 2100);
    const o = { fHead: 'VRPoppins', fBody: 'VRInter', fHand: 'VRCaveat' };
    VRScene.ART_NAMES.forEach((n, i) => {
      const x = (i % 3) * 620 + 10, y = Math.floor(i / 3) * 420 + 10;
      VRScene.drawArt(ctx, { type: 'art', art: n, count: '214 baru', badge: 'TERBIT!', label: n === 'shop' ? 'TOKO KITA' : '' }, lt, { x, y, w: 600, h: 373 }, o);
      ctx.fillStyle = '#071B6E'; ctx.font = '800 26px VRPoppins'; ctx.fillText(n, x + 12, y + 405);
    });
    return ctx.canvas.toDataURL('image/png');
  }, { fonts, lt });
  fs.writeFileSync(out, Buffer.from(data.split(',')[1], 'base64')); await b.close(); console.log('ok', out);
})();
