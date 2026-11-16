// Preview renderer for VRITIMES Remotion reel packages (no Remotion needed).
// Draws frames with the package's own src/scene.js in headless Chromium, writes JPEG frames,
// then (mode=video) encodes MP4 with the SFX cues mixed in (and VO if public/vo/ exists).
// usage: node reel_preview.js <reelDir> <outDir> [sheet|video] [fps]
const { chromium } = require('playwright');
const fs = require('fs'), path = require('path'), { execFileSync } = require('child_process');
const [reelDir, outDir, mode = 'sheet', fpsArg = '30'] = process.argv.slice(2);
const fps = Number(fpsArg);
const pub = path.join(reelDir, 'public');
const reel = JSON.parse(fs.readFileSync(path.join(pub, 'reel.json'), 'utf8'));
let timing = null; try { timing = JSON.parse(fs.readFileSync(path.join(pub, 'vo', 'timing.json'), 'utf8')); } catch (e) {}
const b64 = (p) => fs.readFileSync(p).toString('base64');
const fonts = fs.readdirSync(path.join(pub, 'fonts')).map((f) => { const m = f.match(/^(\w+)-(\d+)\.woff2?$/); return m && [m[1], m[2], 'data:font/woff;base64,' + b64(path.join(pub, 'fonts', f))]; }).filter(Boolean);
const logo = (n) => 'data:image/png;base64,' + b64(path.join(pub, 'logo', n));
fs.mkdirSync(outDir, { recursive: true });
(async () => {
  const browser = await chromium.launch();
  const page = await browser.newPage({ viewport: { width: 1080, height: 1920 } });
  await page.setContent('<html><body style="margin:0"><canvas id="c" width="1080" height="1920"></canvas></body></html>');
  await page.addScriptTag({ content: fs.readFileSync(path.join(reelDir, 'src', 'scene.js'), 'utf8') });
  const info = await page.evaluate(async ({ reel, timing, fonts, logos }) => {
    await Promise.all(fonts.map(([fam, w, url]) => new FontFace(fam, `url(${url})`, { weight: w }).load().then((f) => document.fonts.add(f))));
    window.A = await VRScene.loadAssets(logos);
    const est = VRScene.timeline(reel).durs;
    window.DURS = reel.scenes.map((s, i) => { const vo = timing && timing[i] && timing[i].duration ? timing[i].duration + 0.45 : 0; return Math.max(1.6, vo || est[i]); });
    window.REEL = reel; window.CTX = document.getElementById('c').getContext('2d');
    return { durs: window.DURS, cues: VRScene.sfxCues(reel, window.DURS) };
  }, { reel, timing, fonts, logos: { logoWhite: logo('stack_white.png'), logoColor: logo('stack_color.png'), besideWhite: logo('beside_white.png') } });
  const total = info.durs.reduce((a, b) => a + b, 0);
  // beat QA: no illustration may stay on screen longer than beatSec (default 4 s)
  const beatRep = await page.evaluate(() => REEL.scenes.map((sc, i) => { const p = VRScene.beatPlan ? VRScene.beatPlan(REEL, sc, DURS[i]) : { n: 1, seg: DURS[i], list: [sc.illus || {}] }; return { i: i + 1, n: p.n, seg: p.seg, none: p.list.slice(0, p.n).some((x) => !x || !x.type || x.type === 'none') }; }));
  const lim = Number(reel.beatSec) > 0 ? Number(reel.beatSec) : 4;
  const bad = beatRep.filter((b) => b.seg > lim + 0.01 || b.none);
  console.log('beat check: max hold ' + Math.max(...beatRep.map((b) => b.seg)).toFixed(2) + 's' + (bad.length ? '  ✗ FIX scenes ' + bad.map((b) => b.i + (b.none ? '(no illus)' : '(' + b.seg.toFixed(1) + 's)')).join(', ') : '  ✓ all ≤ ' + lim + 's'));
  const times = mode === 'sheet' ? Array.from({ length: Math.ceil(total) }, (_, i) => i + 0.9) : Array.from({ length: Math.ceil(total * fps) }, (_, i) => i / fps);
  const opts = { fHead: 'VRPoppins', fBody: 'VRInter', fHand: 'VRCaveat', lang: reel.lang, cc: reel.country, countryName: reel.countryName, roleTitle: reel.roleTitle || 'PR Specialist' };
  for (let i = 0; i < times.length; i++) {
    const data = await page.evaluate(({ t, opts }) => { VRScene.drawFrame(CTX, REEL, DURS, t, A, opts); return CTX.canvas.toDataURL('image/jpeg', 0.9); }, { t: Math.min(times[i], total - 0.01), opts });
    fs.writeFileSync(path.join(outDir, `f${String(i).padStart(5, '0')}.jpg`), Buffer.from(data.split(',')[1], 'base64'));
  }
  await browser.close();
  fs.writeFileSync(path.join(outDir, 'timeline.json'), JSON.stringify({ durs: info.durs, total, cues: info.cues }, null, 1));
  if (mode === 'video') {
    const out = path.join(outDir, 'preview.mp4');
    const args = ['-y', '-loglevel', 'error', '-framerate', String(fps), '-i', path.join(outDir, 'f%05d.jpg')];
    const filters = []; let n = 1;
    const sfx = reel.sfx === false ? [] : info.cues;
    sfx.forEach((c) => { args.push('-i', path.join(pub, 'sfx', c.name + '.wav')); filters.push(`[${n}:a]adelay=${Math.round(c.t * 1000)}|${Math.round(c.t * 1000)},volume=${c.vol}[a${n}]`); n++; });
    if (timing) { let acc = 0; reel.scenes.forEach((s, i) => { const f = path.join(pub, 'vo', 's' + String(i + 1).padStart(2, '0') + '.mp3'); if (fs.existsSync(f)) { args.push('-i', f); filters.push(`[${n}:a]adelay=${Math.round(acc * 1000)}|${Math.round(acc * 1000)}[a${n}]`); n++; } acc += info.durs[i]; }); }
    if (n > 1) {
      const labels = Array.from({ length: n - 1 }, (_, k) => `[a${k + 1}]`).join('');
      filters.push(`${labels}amix=inputs=${n - 1}:normalize=0,apad[aout]`);
      args.push('-filter_complex', filters.join(';'), '-map', '0:v', '-map', '[aout]', '-c:a', 'aac', '-b:a', '160k');
    }
    args.push('-c:v', 'libx264', '-pix_fmt', 'yuv420p', '-crf', '20', '-preset', 'veryfast', '-t', total.toFixed(2), out);
    execFileSync('ffmpeg', args, { stdio: 'inherit' });
    console.log('video', out, total.toFixed(1) + 's');
  } else console.log('sheet frames', times.length, 'total', total.toFixed(1) + 's', 'durs', info.durs.map((d) => d.toFixed(1)).join(','));
})();
