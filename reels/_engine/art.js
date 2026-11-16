// ===================== VRITIMES 2D ART LIBRARY (spliced into scene.js) =====================
// Flat 2D illustrations with navy outlines, blue-dominant palette, lime accents. Each art is drawn on a
// canonical 900x560 stage and scaled into the target box. All motion is driven by `lt` (seconds since the beat began).
// Use in reel.json: "illus": {"type": "art", "art": "<name>", ...data}. Catalogue: ART_NAMES.
const OUT = '#0A1440', SK1 = '#C98E6B', SK2 = '#E2B48F', SK3 = '#8D5A3B';
function pop(lt, d, dur) { return easeBack(clamp((lt - d) / (dur || 0.45), 0, 1)); }
function fade(lt, d, dur) { return easeOut(clamp((lt - d) / (dur || 0.4), 0, 1)); }
function stroke(ctx, w, c) { ctx.lineWidth = w || 5; ctx.strokeStyle = c || OUT; ctx.lineJoin = 'round'; ctx.lineCap = 'round'; ctx.stroke(); }
function shape(ctx, fill, w) { ctx.fillStyle = fill; ctx.fill(); if (w !== 0) stroke(ctx, w || 5); }
function rrs(ctx, x, y, w, h, r, fill, sw) { rr(ctx, x, y, w, h, r); shape(ctx, fill, sw); }
function circ(ctx, x, y, r, fill, sw) { ctx.beginPath(); ctx.arc(x, y, r, 0, Math.PI * 2); shape(ctx, fill, sw); }
function shadow(ctx, x, y, rx, ry) { ctx.save(); ctx.fillStyle = 'rgba(7,27,110,.14)'; ctx.beginPath(); ctx.ellipse(x, y, rx, ry, 0, 0, Math.PI * 2); ctx.fill(); ctx.restore(); }
function star(ctx, x, y, r, fill, rot) {
  ctx.save(); ctx.translate(x, y); ctx.rotate(rot || 0); ctx.beginPath();
  for (let i = 0; i < 10; i++) { const a = -Math.PI / 2 + i * Math.PI / 5, rr2 = i % 2 ? r * 0.45 : r; ctx.lineTo(Math.cos(a) * rr2, Math.sin(a) * rr2); }
  ctx.closePath(); shape(ctx, fill, 4); ctx.restore();
}
function heart(ctx, x, y, s, fill) {
  ctx.save(); ctx.translate(x, y); ctx.scale(s, s); ctx.beginPath();
  ctx.moveTo(0, 12); ctx.bezierCurveTo(-26, -6, -14, -30, 0, -14); ctx.bezierCurveTo(14, -30, 26, -6, 0, 12); ctx.closePath();
  shape(ctx, fill, 4 / s); ctx.restore();
}
function sparkle(ctx, x, y, r, c) { ctx.save(); ctx.translate(x, y); ctx.fillStyle = c || C.lime; ctx.beginPath(); ctx.moveTo(0, -r); ctx.quadraticCurveTo(0, 0, r, 0); ctx.quadraticCurveTo(0, 0, 0, r); ctx.quadraticCurveTo(0, 0, -r, 0); ctx.quadraticCurveTo(0, 0, 0, -r); ctx.fill(); ctx.restore(); }
function plant(ctx, x, y, s, t) {
  ctx.save(); ctx.translate(x, y); ctx.scale(s, s);
  for (let k = 0; k < 5; k++) { ctx.save(); ctx.rotate(-0.9 + k * 0.45 + Math.sin(t * 1.3 + k) * 0.04); ctx.beginPath(); ctx.ellipse(0, -46, 13, 40, 0, 0, Math.PI * 2); shape(ctx, k % 2 ? '#2F8F63' : '#47B07A', 3); ctx.restore(); }
  ctx.beginPath(); ctx.moveTo(-26, -6); ctx.lineTo(26, -6); ctx.lineTo(20, 36); ctx.lineTo(-20, 36); ctx.closePath(); shape(ctx, '#FFFFFF', 4);
  ctx.fillStyle = C.blue; ctx.fillRect(-23, 4, 46, 8); ctx.restore();
}
function cloud(ctx, x, y, s, c) { ctx.save(); ctx.translate(x, y); ctx.scale(s, s); ctx.fillStyle = c || '#FFFFFF'; ctx.beginPath(); ctx.arc(-30, 0, 24, 0, Math.PI * 2); ctx.arc(0, -14, 32, 0, Math.PI * 2); ctx.arc(32, 0, 24, 0, Math.PI * 2); ctx.rect(-30, 0, 62, 24); ctx.fill(); ctx.restore(); }
function textC(ctx, o, s, x, y, size, color, weight, kind, maxW) {
  ctx.font = font(o, weight || 800, size, kind || 'head'); ctx.fillStyle = color || OUT; ctx.textAlign = 'center';
  let str = String(s || '').replace(/[*[\]]/g, ''); if (maxW) while (ctx.measureText(str).width > maxW && str.length > 3) str = str.slice(0, -2) + '…';
  ctx.fillText(str, x, y); ctx.textAlign = 'left';
}
/** flat half/whole-body character. opt: {skin, hair, shirt, hijab, glasses, wave, armR, armL, hold, t, mouth} */
function figure(ctx, x, y, s, opt) {
  const o2 = Object.assign({skin: SK1, hair: '#1F1A1D', shirt: C.blue, t: 0}, opt || {}); const t = o2.t;
  ctx.save(); ctx.translate(x, y + Math.sin(t * 2.2) * 3); ctx.scale(s, s);
  // body
  ctx.beginPath(); ctx.moveTo(-62, 150); ctx.quadraticCurveTo(-64, 40, -30, 28); ctx.lineTo(30, 28); ctx.quadraticCurveTo(64, 40, 62, 150); ctx.closePath(); shape(ctx, o2.shirt, 5);
  ctx.beginPath(); ctx.moveTo(-14, 28); ctx.lineTo(0, 52); ctx.lineTo(14, 28); shape(ctx, '#FFFFFF', 4);
  // arms
  const arm = (side, ang, hand) => {
    ctx.save(); ctx.translate(side * 50, 46); ctx.rotate(side * ang);
    ctx.beginPath(); ctx.moveTo(0, 0); ctx.lineTo(0, 78); ctx.lineWidth = 26; ctx.strokeStyle = OUT; ctx.lineCap = 'round'; ctx.stroke(); ctx.lineWidth = 18; ctx.strokeStyle = o2.shirt; ctx.stroke();
    circ(ctx, 0, 86, 13, o2.skin, 4); if (hand) hand(); ctx.restore();
  };
  const wave = o2.wave ? -2.5 + Math.sin(t * 7) * 0.35 : null;
  arm(-1, o2.armL != null ? o2.armL : 0.15);
  arm(1, wave != null ? wave : (o2.armR != null ? o2.armR : 0.15));
  // neck + head
  rrs(ctx, -11, 6, 22, 26, 8, o2.skin, 4);
  if (o2.hijab) { ctx.beginPath(); ctx.ellipse(0, -30, 46, 52, 0, 0, Math.PI * 2); shape(ctx, o2.hijab, 5); }
  circ(ctx, 0, -32, 36, o2.skin, 5);
  if (o2.hijab) { ctx.beginPath(); ctx.arc(0, -32, 40, Math.PI * 1.05, Math.PI * 1.95); ctx.lineTo(30, -40); ctx.quadraticCurveTo(0, -60, -30, -40); ctx.closePath(); shape(ctx, o2.hijab, 0); }
  else { ctx.beginPath(); ctx.arc(0, -36, 38, Math.PI * 1.02, Math.PI * 1.98); ctx.quadraticCurveTo(10, -48, -36, -40); ctx.closePath(); shape(ctx, o2.hair, 4); }
  // face
  const blink = (Math.floor(t * 0.7) % 4 === 0 && (t * 0.7) % 1 < 0.08) ? 0.15 : 1;
  ctx.fillStyle = OUT; ctx.save(); ctx.translate(-13, -30); ctx.scale(1, blink); ctx.beginPath(); ctx.arc(0, 0, 4.5, 0, Math.PI * 2); ctx.fill(); ctx.restore();
  ctx.save(); ctx.translate(13, -30); ctx.scale(1, blink); ctx.beginPath(); ctx.arc(0, 0, 4.5, 0, Math.PI * 2); ctx.fill(); ctx.restore();
  if (o2.glasses) { ctx.beginPath(); ctx.arc(-13, -30, 11, 0, Math.PI * 2); ctx.moveTo(24, -30); ctx.arc(13, -30, 11, 0, Math.PI * 2); ctx.moveTo(-2, -30); ctx.lineTo(2, -30); stroke(ctx, 3.5); }
  ctx.fillStyle = 'rgba(229,120,110,.35)'; ctx.beginPath(); ctx.arc(-22, -18, 6, 0, Math.PI * 2); ctx.arc(22, -18, 6, 0, Math.PI * 2); ctx.fill();
  ctx.beginPath(); if (o2.mouth === 'o') ctx.arc(0, -12, 5, 0, Math.PI * 2); else ctx.arc(0, -16, 10, 0.15 * Math.PI, 0.85 * Math.PI); stroke(ctx, 4);
  if (o2.hold) { ctx.save(); o2.hold(ctx); ctx.restore(); }
  ctx.restore();
}
function phoneShape(ctx, x, y, w, h, rot) { ctx.save(); ctx.translate(x, y); ctx.rotate(rot || 0); rrs(ctx, -w / 2, -h / 2, w, h, w * 0.16, '#0E1430', 5); fillRR(ctx, -w / 2 + 8, -h / 2 + 12, w - 16, h - 24, w * 0.1, '#FFFFFF'); return ctx; }
function miniShop(ctx, x, y, s, t, label, o) {
  ctx.save(); ctx.translate(x, y); ctx.scale(s, s);
  rrs(ctx, -110, -60, 220, 150, 10, '#F4F8FF', 5);
  for (let i = 0; i < 6; i++) { ctx.beginPath(); ctx.moveTo(-120 + i * 40, -90); ctx.lineTo(-80 + i * 40, -90); ctx.lineTo(-80 + i * 40, -50); ctx.arc(-100 + i * 40, -50, 20, 0, Math.PI); ctx.closePath(); shape(ctx, i % 2 ? '#FFFFFF' : C.blue, 4); }
  rrs(ctx, -90, -30, 90, 70, 6, '#CFE2FF', 4); rrs(ctx, 20, -20, 60, 110, 6, C.mid, 4);
  rrs(ctx, -80, -128, 160, 40, 10, C.navy, 4); if (label) textC(ctx, o, label, 0, -100, 22, C.lime, 800, 'head', 150);
  ctx.restore();
}
function newsPage(ctx, x, y, w, h, o, head, sub) {
  rrs(ctx, x, y, w, h, 8, '#FBF8F1', 5);
  textC(ctx, o, sub || 'HARIAN BISNIS', x + w / 2, y + h * 0.12, Math.max(16, h * 0.075), '#1B1B1B', 800);
  ctx.fillStyle = '#1B1B1B'; ctx.fillRect(x + w * 0.06, y + h * 0.16, w * 0.88, 4);
  ctx.font = font(o, 800, Math.max(16, h * 0.072), 'head'); ctx.fillStyle = '#111';
  wrapText(ctx, head || '', w * 0.86, 2).forEach((l, i) => ctx.fillText(l, x + w * 0.07, y + h * 0.27 + i * h * 0.085));
}

const ART = {};
// 1. UMKM storefront with owner waving
ART.shop = (ctx, lt, d, o) => {
  const t = lt; const b = pop(lt, 0, 0.5);
  circ(ctx, 450, 300, 250 * fade(lt, 0, 0.5), '#DCEBFF', 0);
  cloud(ctx, 150 + Math.sin(t * 0.5) * 10, 110, 0.9); cloud(ctx, 760 - Math.sin(t * 0.4) * 12, 150, 0.7);
  shadow(ctx, 450, 520, 330, 22);
  ctx.save(); ctx.translate(450, 520); ctx.scale(b, b); ctx.translate(-450, -520);
  rrs(ctx, 200, 200, 470, 310, 12, '#F4F8FF', 6);
  const aw = pop(lt, 0.25);
  ctx.save(); ctx.translate(0, (1 - aw) * -60); ctx.globalAlpha *= clamp(aw, 0, 1);
  for (let i = 0; i < 9; i++) { const x0 = 180 + i * 57; ctx.beginPath(); ctx.moveTo(x0, 160); ctx.lineTo(x0 + 57, 160); ctx.lineTo(x0 + 57, 220); ctx.arc(x0 + 28.5, 220, 28.5, 0, Math.PI); ctx.closePath(); shape(ctx, i % 2 ? '#FFFFFF' : C.blue, 5); }
  rrs(ctx, 290, 92, 290, 62, 14, C.navy, 5); textC(ctx, o, d.label || 'TOKO KITA', 435, 136, 34, C.lime, 800, 'head', 260);
  ctx.restore();
  // window with products
  rrs(ctx, 232, 270, 230, 190, 10, '#CFE2FF', 5);
  ctx.fillStyle = 'rgba(255,255,255,.55)'; ctx.beginPath(); ctx.moveTo(250, 450); ctx.lineTo(330, 280); ctx.lineTo(370, 280); ctx.lineTo(290, 450); ctx.fill();
  [[255, 340, C.mid], [300, 330, C.lime], [345, 345, C.blue], [390, 335, '#7FA8FF']].forEach(([px, py, c], i) => { const p = pop(lt, 0.45 + i * 0.1); if (p > 0) rrs(ctx, px, py + (1 - p) * 20, 34, 368 - py, 8, c, 4); });
  ctx.fillStyle = OUT; ctx.fillRect(240, 370, 214, 6); ctx.fillRect(240, 430, 214, 6);
  [[262, 400, '#FFFFFF'], [318, 396, C.cyan], [372, 404, C.lime]].forEach(([px, py, c]) => rrs(ctx, px, py, 40, 30, 6, c, 4));
  // door + swinging sign
  rrs(ctx, 500, 290, 140, 220, 8, C.mid, 5); circ(ctx, 620, 405, 7, C.lime, 3);
  ctx.save(); ctx.translate(570, 310); ctx.rotate(Math.sin(t * 2.4) * 0.12); ctx.beginPath(); ctx.moveTo(-30, 0); ctx.lineTo(0, -22); ctx.lineTo(30, 0); stroke(ctx, 3);
  rrs(ctx, -46, 0, 92, 40, 8, '#FFFFFF', 4); textC(ctx, o, d.open || 'BUKA', 0, 29, 24, C.blue, 800); ctx.restore();
  ctx.restore();
  plant(ctx, 175, 500, 1.1 * pop(lt, 0.5), t); plant(ctx, 700, 500, 1.0 * pop(lt, 0.6), t + 1);
  const ow = pop(lt, 0.7); if (ow > 0) figure(ctx, 790, 335 + (1 - ow) * 60, 0.95, {t, wave: true, shirt: C.blue, glasses: false, hijab: d.hijab ? C.navy : null});
  for (let i = 0; i < 4; i++) { const p = fade(lt, 1 + i * 0.2); if (p > 0) sparkle(ctx, [150, 720, 320, 610][i], [250, 80, 70, 250][i] + Math.sin(t * 3 + i) * 6, 16 * p * (0.8 + 0.2 * Math.sin(t * 5 + i))); }
};
// 2. big players are loud, the small shop's voice is faint
ART.quietvoice = (ctx, lt, d, o) => {
  const t = lt;
  [[90, 150, 130, 360, C.navy], [240, 80, 150, 430, '#123A9C'], [610, 110, 140, 400, C.navy], [770, 170, 110, 340, '#123A9C']].forEach(([x, y, w, h, c], i) => {
    const p = pop(lt, i * 0.12); if (p <= 0) return; const yy = y + (1 - p) * 120;
    rrs(ctx, x, yy, w, 510 - yy, 8, c, 5);
    for (let r = 0; r < 7; r++) for (let q = 0; q < 3; q++) { const on = (r * 3 + q + i) % 4 !== 0; fillRR(ctx, x + 16 + q * (w - 32) / 3, yy + 24 + r * 46, (w - 32) / 3 - 10, 26, 4, on ? 'rgba(215,242,60,.85)' : 'rgba(255,255,255,.2)'); }
    // loud waves from rooftops
    if (p >= 1) for (let k = 0; k < 3; k++) { const ph = ((t * 1.2 + k / 3 + i * 0.2) % 1); ctx.save(); ctx.globalAlpha = 1 - ph; ctx.beginPath(); ctx.arc(x + w / 2, yy, 20 + ph * 70, Math.PI * 1.15, Math.PI * 1.85); stroke(ctx, 6, C.cyan); ctx.restore(); }
  });
  ctx.fillStyle = '#E3ECFA'; ctx.fillRect(0, 505, 900, 55);
  const sp = pop(lt, 0.5); if (sp > 0) { ctx.save(); ctx.translate(450, 470); ctx.scale(sp, sp); miniShop(ctx, 0, 0, 0.9, t, d.label || 'UMKM', o); ctx.restore(); }
  // faint small bubble
  const bp = pop(lt, 0.9);
  if (bp > 0) {
    ctx.save(); ctx.translate(560, 300); ctx.scale(bp * (0.95 + Math.sin(t * 3) * 0.03), bp * (0.95 + Math.sin(t * 3) * 0.03)); ctx.globalAlpha = 0.9;
    rrs(ctx, -70, -44, 140, 80, 34, '#FFFFFF', 4); ctx.beginPath(); ctx.moveTo(-30, 34); ctx.lineTo(-50, 64); ctx.lineTo(-6, 36); shape(ctx, '#FFFFFF', 0);
    for (let k = 0; k < 3; k++) circ(ctx, -30 + k * 30, -4, 8, k <= Math.floor(t * 2) % 3 ? C.blue : '#C9D6EE', 0);
    ctx.restore();
    // volume-low badge
    ctx.save(); ctx.translate(660, 220); ctx.scale(bp, bp); circ(ctx, 0, 0, 34, C.lime, 4);
    ctx.beginPath(); ctx.moveTo(-16, -8); ctx.lineTo(-6, -8); ctx.lineTo(6, -18); ctx.lineTo(6, 18); ctx.lineTo(-6, 8); ctx.lineTo(-16, 8); ctx.closePath(); shape(ctx, C.navy, 0);
    ctx.beginPath(); ctx.arc(8, 0, 10, -0.7, 0.7); stroke(ctx, 4, C.navy); ctx.restore();
  }
};
// 3. myth stamped down, fact stamp lands
ART.mythbust = (ctx, lt, d, o) => {
  const t = lt; const cp = pop(lt, 0, 0.5);
  ctx.save(); ctx.translate(450, 290); ctx.scale(cp, cp); ctx.rotate(-0.03);
  rrs(ctx, -330, -200, 660, 400, 26, '#FFFFFF', 6);
  textC(ctx, o, d.mythTag || 'MITOS', 0, -110, 46, '#8A94B0', 800);
  ctx.font = font(o, 800, 46, 'head'); ctx.fillStyle = OUT; ctx.textAlign = 'center';
  wrapText(ctx, d.myth || 'Press release cuma untuk perusahaan besar', 560, 2).forEach((l, i) => ctx.fillText(l, 0, -30 + i * 58)); ctx.textAlign = 'left';
  const xs = fade(lt, 0.7, 0.35);
  if (xs > 0) { ctx.beginPath(); ctx.moveTo(-290, -150); ctx.lineTo(-290 + 580 * xs, -150 + 300 * xs); stroke(ctx, 16, C.navy); if (xs > 0.5) { const x2 = (xs - 0.5) * 2; ctx.beginPath(); ctx.moveTo(290, -150); ctx.lineTo(290 - 580 * x2, -150 + 300 * x2); stroke(ctx, 16, C.navy); } }
  ctx.restore();
  const sp = clamp((lt - 1.2) / 0.3, 0, 1);
  if (sp > 0) {
    const sc = lerp(2.2, 1, easeOut(sp)); ctx.save(); ctx.translate(610, 410); ctx.rotate(-0.14); ctx.scale(sc, sc); ctx.globalAlpha = clamp(sp * 1.4, 0, 1);
    rrs(ctx, -160, -62, 320, 124, 22, C.lime, 7); rr(ctx, -146, -48, 292, 96, 16); stroke(ctx, 4, C.navy);
    textC(ctx, o, d.factTag || 'FAKTA', 0, 18, 64, C.navy, 800); ctx.restore();
    if (sp >= 1) for (let i = 0; i < 6; i++) { const a = i * Math.PI / 3 + 0.3, r = 190 + ((t * 60) % 30); sparkle(ctx, 610 + Math.cos(a) * r, 410 + Math.sin(a) * r * 0.6, 14, i % 2 ? C.cyan : C.lime); }
  }
  if (d.fact) { const fp = fade(lt, 1.6); ctx.save(); ctx.globalAlpha = fp; textC(ctx, o, d.fact, 450, 545, 38, C.blue, 800, 'head', 820); ctx.restore(); }
};
// 4. journalist at desk, stories flying into the monitor
ART.newsroom = (ctx, lt, d, o) => {
  const t = lt;
  circ(ctx, 520, 280, 240 * fade(lt, 0, 0.5), '#DCEBFF', 0);
  rrs(ctx, 60, 440, 780, 34, 10, '#B98F64', 5); ctx.fillStyle = '#8E6A47'; ctx.fillRect(100, 474, 24, 80); ctx.fillRect(776, 474, 24, 80);
  const mp = pop(lt, 0.1);
  ctx.save(); ctx.translate(560, 440); ctx.scale(mp, mp); ctx.translate(-560, -440);
  rrs(ctx, 380, 150, 360, 250, 16, '#1C2236', 6); rrs(ctx, 398, 168, 324, 214, 8, '#FFFFFF', 0);
  fillRR(ctx, 398, 168, 324, 36, 0, C.blue); textC(ctx, o, d.screen || 'REDAKSI', 470, 194, 22, '#FFFFFF', 800);
  ctx.font = font(o, 800, 26, 'head'); ctx.fillStyle = OUT; wrapText(ctx, d.headline || 'UMKM lokal tembus pasar baru', 300, 2).forEach((l, i) => ctx.fillText(l, 412, 238 + i * 32));
  const ph = fade(lt, 0.6); fillRR(ctx, 412, 290, 150 * ph, 76, 6, '#7FA8FF'); miniShop(ctx, 487, 344, 0.28 * ph, t, '', o);
  for (let i = 0; i < 4; i++) fillRR(ctx, 576, 296 + i * 18, 130 * fade(lt, 0.7 + i * 0.08), 9, 4, '#D6E3FB');
  rrs(ctx, 540, 400, 40, 40, 4, '#1C2236', 5);
  ctx.restore();
  // journalist (seated, side)
  const jp = pop(lt, 0.25); if (jp > 0) figure(ctx, 250, 300 + (1 - jp) * 40, 0.95, {t, shirt: C.navy, glasses: true, armR: -1.1, hair: '#3A2A22', skin: SK2});
  // mug with steam + papers
  rrs(ctx, 770, 392, 46, 50, 8, '#FFFFFF', 4); ctx.beginPath(); ctx.arc(818, 414, 12, -1.4, 1.4); stroke(ctx, 4);
  for (let k = 0; k < 2; k++) { ctx.beginPath(); const sx = 784 + k * 18; ctx.moveTo(sx, 384); ctx.bezierCurveTo(sx - 10, 366 - Math.sin(t * 3 + k) * 6, sx + 10, 352, sx, 336); stroke(ctx, 4, 'rgba(10,20,64,.35)'); }
  [[110, 400, -0.1], [130, 388, 0.06]].forEach(([x, y, r]) => { ctx.save(); ctx.translate(x, y); ctx.rotate(r); rrs(ctx, 0, 0, 130, 40, 4, '#FFFFFF', 4); ctx.restore(); });
  // incoming envelopes
  for (let i = 0; i < 4; i++) {
    const ph2 = ((t * 0.55 + i / 4) % 1); const x = lerp(-30, 390, ph2), y = lerp(70 + i * 26, 175, ph2) - Math.sin(ph2 * Math.PI) * 50;
    ctx.save(); ctx.globalAlpha = ph2 < 0.7 ? 1 : Math.max(0, (0.9 - ph2) / 0.2); ctx.translate(x, y); ctx.rotate(-0.2 + ph2 * 0.3);
    rrs(ctx, -32, -22, 64, 44, 6, i % 2 ? '#FFFFFF' : C.lime, 4); ctx.beginPath(); ctx.moveTo(-32, -22); ctx.lineTo(0, 4); ctx.lineTo(32, -22); stroke(ctx, 4); ctx.restore();
  }
  if (d.count) { const cp2 = pop(lt, 0.8); ctx.save(); ctx.translate(735, 150); ctx.scale(cp2, cp2); rrs(ctx, -64, -30, 128, 60, 30, C.lime, 4); textC(ctx, o, d.count, 0, 12, 30, C.navy, 800); ctx.restore(); }
};
// 5. hands holding a newspaper with your story
ART.newspaper = (ctx, lt, d, o) => {
  const t = lt; const p = pop(lt, 0, 0.6);
  ctx.save(); ctx.translate(450, 300); ctx.rotate(lerp(-0.25, -0.02, p) + Math.sin(t * 1.5) * 0.01); ctx.scale(lerp(0.5, 1, p), lerp(0.5, 1, p)); ctx.globalAlpha = clamp(p * 1.4, 0, 1);
  ctx.fillStyle = 'rgba(7,27,110,.2)'; ctx.fillRect(-300, -215, 620, 450);
  newsPage(ctx, -310, -230, 620, 450, o, d.headline || 'Usaha lokal ini jadi sorotan', d.paper || 'HARIAN BISNIS');
  const ph = fade(lt, 0.5); fillRR(ctx, -280, 10, 320 * ph, 180, 6, '#BFD5FF'); if (ph > 0.6) miniShop(ctx, -120, 140, 0.62, t, d.label || '', o);
  for (let i = 0; i < 8; i++) fillRR(ctx, 60, 14 + i * 22, 210 * fade(lt, 0.6 + i * 0.05), 10, 4, '#CFCAC0');
  ctx.restore();
  // hands
  [[-1, 130], [1, 770]].forEach(([s, x]) => { ctx.save(); ctx.translate(x, 330 + Math.sin(t * 1.5) * 4); ctx.rotate(s * 0.2); rrs(ctx, -34, -20, 68, 110, 30, SK1, 5); rrs(ctx, -40, 70, 80, 120, 16, C.blue, 5); ctx.restore(); });
  for (let i = 0; i < 5; i++) { const f = fade(lt, 0.9 + i * 0.12); if (f > 0) star(ctx, 300 + i * 70, 525, 22 * f, C.lime, Math.sin(t * 2 + i) * 0.2); }
  if (d.badge) { const bp = pop(lt, 0.8); ctx.save(); ctx.translate(735, 90); ctx.rotate(0.12); ctx.scale(bp, bp); rrs(ctx, -100, -34, 200, 68, 34, C.lime, 5); textC(ctx, o, d.badge, 0, 12, 30, C.navy, 800); ctx.restore(); }
};
// 6. customer searches your name on a phone, your story shows up
ART.phonesearch = (ctx, lt, d, o) => {
  const t = lt;
  circ(ctx, 450, 290, 240 * fade(lt, 0, 0.5), '#DCEBFF', 0);
  const fp = pop(lt, 0.05); if (fp > 0) figure(ctx, 250, 270 + (1 - fp) * 50, 1.15, {t, shirt: C.mid, hijab: d.hijab === false ? null : '#0B2A9A', armR: -0.6, armL: 0.2, skin: SK2});
  const pp = pop(lt, 0.3);
  ctx.save(); ctx.translate(560, 300 + (1 - pp) * 80); ctx.rotate(0.06 + Math.sin(t * 1.4) * 0.015); ctx.scale(pp, pp);
  phoneShape(ctx, 0, 0, 260, 470, 0);
  rrs(ctx, -112, -200, 224, 46, 23, '#FFFFFF', 4); ctx.beginPath(); ctx.arc(-88, -177, 10, 0, Math.PI * 2); stroke(ctx, 4, C.blue);
  const q = String(d.query || 'nama usahamu'); const n = Math.floor(clamp((lt - 0.6) * 18, 0, q.length));
  ctx.font = font(o, 600, 20, 'body'); ctx.fillStyle = OUT; ctx.fillText(q.slice(0, n), -68, -170);
  const rp = fade(lt, 0.7 + q.length / 18);
  if (rp > 0) {
    ctx.globalAlpha = rp; rrs(ctx, -112, -136, 224, 170, 14, C.pale, 3);
    fillRR(ctx, -100, -124, 90, 66, 8, '#7FA8FF'); miniShop(ctx, -55, -76, 0.22, t, '', o);
    ctx.font = font(o, 800, 18, 'head'); ctx.fillStyle = C.blue; wrapText(ctx, d.result || 'Berita: usahamu masuk media', 100, 3).forEach((l, i) => ctx.fillText(l, -2, -110 + i * 22));
    for (let i = 0; i < 5; i++) star(ctx, -92 + i * 26, 4, 10, C.lime, 0);
    for (let i = 0; i < 3; i++) { rrs(ctx, -112, 48 + i * 52, 224, 42, 10, '#FFFFFF', 3); fillRR(ctx, -98, 62 + i * 52, 140 - i * 20, 12, 6, '#D6E3FB'); }
    ctx.globalAlpha = 1;
  }
  ctx.restore();
  const mg = pop(lt, 0.5); if (mg > 0) { ctx.save(); ctx.translate(770, 140 + Math.sin(t * 2) * 8); ctx.scale(mg, mg); circ(ctx, 0, 0, 46, '#FFFFFF', 6); ctx.beginPath(); ctx.moveTo(32, 32); ctx.lineTo(70, 70); stroke(ctx, 14, OUT); ctx.restore(); }
  if (rp >= 1) for (let i = 0; i < 3; i++) heart(ctx, 760 + i * 30, 420 - ((t * 50 + i * 40) % 160), 1.1, i % 2 ? C.lime : '#7FA8FF');
};
// 7. writing the press release: checklist ticks + pen
ART.docwrite = (ctx, lt, d, o) => {
  const t = lt; const p = pop(lt, 0, 0.5);
  ctx.save(); ctx.translate(430, 290); ctx.rotate(-0.04); ctx.scale(p, p);
  ctx.fillStyle = 'rgba(7,27,110,.18)'; rr(ctx, -250, -232, 520, 480, 18); ctx.fill();
  rrs(ctx, -260, -250, 520, 480, 18, '#FFFFFF', 6);
  ctx.save(); rr(ctx, -260, -250, 520, 480, 18); ctx.clip(); ctx.fillStyle = C.blue; ctx.fillRect(-260, -250, 520, 90); ctx.restore();
  textC(ctx, o, d.header || 'PRESS RELEASE', 0, -192, 38, '#FFFFFF', 800);
  const items = (d.items || ['Apa yang baru', 'Siapa kamu', 'Kenapa penting']).slice(0, 4);
  items.forEach((it, i) => {
    const y = -110 + i * 100; const ip = fade(lt, 0.4 + i * 0.55);
    rrs(ctx, -220, y, 56, 56, 14, ip >= 1 ? C.lime : C.pale, 4);
    if (ip > 0.3) { ctx.beginPath(); ctx.moveTo(-206, y + 28); ctx.lineTo(-194, y + 42); ctx.lineTo(-176, y + 14); stroke(ctx, 7, C.navy); }
    ctx.font = font(o, 800, 34, 'head'); ctx.fillStyle = OUT; ctx.globalAlpha = 0.25 + 0.75 * ip; ctx.fillText(String(it).replace(/[*[\]]/g, ''), -140, y + 40); ctx.globalAlpha = 1;
    fillRR(ctx, -140, y + 56, 300 * ip, 8, 4, '#D6E3FB');
  });
  ctx.restore();
  // pen follows the current line
  const cur = clamp(Math.floor((lt - 0.4) / 0.55), 0, items.length - 1); const lp = clamp(((lt - 0.4) / 0.55) % 1, 0, 1);
  const px = 300 + 290 * lp, py = 252 + cur * 100 + Math.sin(t * 18) * 2;
  ctx.save(); ctx.translate(px, py); ctx.rotate(0.7); rrs(ctx, -12, -120, 24, 130, 8, C.navy, 4); ctx.beginPath(); ctx.moveTo(-12, 10); ctx.lineTo(0, 34); ctx.lineTo(12, 10); shape(ctx, C.lime, 4); ctx.restore();
  ctx.save(); ctx.translate(760, 150); ctx.rotate(0.12); rrs(ctx, -60, -60, 120, 120, 6, C.lime, 4); textC(ctx, o, d.note || '3 hal', 0, 10, 30, C.navy, 800, 'hand'); ctx.restore();
};
// 8. trust: owner + customer handshake, stars rise
ART.trust = (ctx, lt, d, o) => {
  const t = lt;
  circ(ctx, 450, 300, 250 * fade(lt, 0, 0.5), '#DCEBFF', 0);
  miniShop(ctx, 450, 230, 0.7 * fade(lt, 0.1), t, '', o);
  const a = pop(lt, 0.2), b = pop(lt, 0.35);
  if (a > 0) figure(ctx, 300 - (1 - a) * 80, 330, 1.0, {t, shirt: C.blue, armR: -0.9});
  if (b > 0) figure(ctx, 600 + (1 - b) * 80, 330, 1.0, {t: t + 1, shirt: C.cyan, hijab: '#0B2A9A', armL: -0.9, skin: SK2});
  if (a >= 1 && b >= 1) { ctx.save(); ctx.translate(450, 420 + Math.sin(t * 6) * 4); rrs(ctx, -46, -22, 92, 44, 22, SK1, 5); ctx.restore(); }
  for (let i = 0; i < 5; i++) { const f = pop(lt, 0.8 + i * 0.15); if (f > 0) star(ctx, 290 + i * 80, 90, 30 * f, C.lime, 0); }
  for (let i = 0; i < 4; i++) { const ph = (t * 0.6 + i / 4) % 1; ctx.save(); ctx.globalAlpha = 1 - ph; heart(ctx, 450 + Math.sin(i * 2 + t) * 120, 360 - ph * 220, 1.3, i % 2 ? '#7FA8FF' : C.lime); ctx.restore(); }
  if (d.label) { const lp = fade(lt, 1.2); ctx.save(); ctx.globalAlpha = lp; rrs(ctx, 250, 500, 400, 52, 26, C.navy, 0); textC(ctx, o, d.label, 450, 536, 28, '#FFFFFF', 800, 'head', 380); ctx.restore(); }
};
// 9. rocket launching from a laptop
ART.rocket = (ctx, lt, d, o) => {
  const t = lt;
  shadow(ctx, 450, 540, 260, 18);
  rrs(ctx, 250, 330, 400, 200, 16, '#1C2236', 6); rrs(ctx, 268, 348, 364, 164, 8, '#2A7BFF', 0);
  ctx.beginPath(); ctx.moveTo(200, 530); ctx.lineTo(700, 530); ctx.lineTo(660, 556); ctx.lineTo(240, 556); ctx.closePath(); shape(ctx, '#AEB8CF', 5);
  const rp = clamp((lt - 0.3) / 1.6, 0, 1); const ry = lerp(430, 120, easeOut(rp)) + Math.sin(t * 20) * 2;
  for (let i = 0; i < 6; i++) { const ph = (t * 1.5 + i / 6) % 1; ctx.save(); ctx.globalAlpha = (1 - ph) * clamp(rp * 3, 0, 1); cloud(ctx, 450 + (i - 2.5) * 30 * ph, ry + 120 + ph * 120, 0.5 + ph * 0.6, '#FFFFFF'); ctx.restore(); }
  ctx.save(); ctx.translate(450, ry);
  ctx.beginPath(); ctx.moveTo(-26, 70); ctx.quadraticCurveTo(0, 130 + Math.sin(t * 30) * 12, 26, 70); shape(ctx, C.lime, 4);
  ctx.beginPath(); ctx.moveTo(0, -110); ctx.bezierCurveTo(60, -60, 60, 40, 40, 80); ctx.lineTo(-40, 80); ctx.bezierCurveTo(-60, 40, -60, -60, 0, -110); shape(ctx, '#FFFFFF', 6);
  ctx.beginPath(); ctx.moveTo(0, -110); ctx.bezierCurveTo(30, -90, 42, -60, 46, -40); ctx.lineTo(-46, -40); ctx.bezierCurveTo(-42, -60, -30, -90, 0, -110); shape(ctx, C.blue, 6);
  circ(ctx, 0, 0, 24, '#7FD3FF', 6);
  ctx.beginPath(); ctx.moveTo(-42, 30); ctx.lineTo(-74, 84); ctx.lineTo(-38, 76); shape(ctx, C.navy, 5); ctx.beginPath(); ctx.moveTo(42, 30); ctx.lineTo(74, 84); ctx.lineTo(38, 76); shape(ctx, C.navy, 5);
  ctx.restore();
  for (let i = 0; i < 10; i++) { const ph = (t * 0.7 + i / 10) % 1; const x = 450 + Math.cos(i * 2.4) * (120 + ph * 260), y = 300 + Math.sin(i * 2.4) * (80 + ph * 160); ctx.save(); ctx.globalAlpha = (1 - ph) * clamp(rp * 2, 0, 1); ctx.translate(x, y); ctx.rotate(t * 3 + i); ctx.fillStyle = [C.lime, C.cyan, '#FFFFFF'][i % 3]; ctx.fillRect(-8, -4, 16, 8); ctx.restore(); }
  if (d.label) textC(ctx, o, d.label, 450, 450, 34, '#FFFFFF', 800, 'head', 340);
};
// 10. share: phones connected by moving arrows
ART.share = (ctx, lt, d, o) => {
  const t = lt; const pts = [[180, 300], [450, 170], [720, 300]];
  for (let i = 0; i < 2; i++) { const [x1, y1] = pts[i], [x2, y2] = pts[i + 1]; const p = fade(lt, 0.5 + i * 0.3); ctx.setLineDash([16, 14]); ctx.lineDashOffset = -t * 50; ctx.beginPath(); ctx.moveTo(x1, y1); ctx.quadraticCurveTo((x1 + x2) / 2, Math.min(y1, y2) - 120, lerp(x1, x2, p), lerp(y1, y2, p)); stroke(ctx, 7, C.blue); ctx.setLineDash([]); }
  pts.forEach(([x, y], i) => {
    const p = pop(lt, i * 0.2); if (p <= 0) return;
    ctx.save(); ctx.translate(x, y); ctx.scale(p, p); phoneShape(ctx, 0, 0, 150, 270, (i - 1) * 0.1);
    circ(ctx, 0, -60, 30, [C.blue, C.cyan, C.mid][i], 4); fillRR(ctx, -50, -10, 100, 14, 7, '#D6E3FB'); fillRR(ctx, -50, 14, 70, 14, 7, '#D6E3FB');
    rrs(ctx, -50, 44, 100, 50, 10, i === 1 ? C.lime : C.pale, 3); ctx.restore(); ctx.restore();
  });
  const sp = pop(lt, 0.9); if (sp > 0) { ctx.save(); ctx.translate(450, 470); ctx.scale(sp, sp); ctx.rotate(Math.sin(t * 2) * 0.08); circ(ctx, 0, 0, 62, C.lime, 6);
    ctx.beginPath(); ctx.moveTo(-20, 20); ctx.quadraticCurveTo(-18, -14, 18, -14); stroke(ctx, 9, C.navy); ctx.beginPath(); ctx.moveTo(6, -30); ctx.lineTo(24, -14); ctx.lineTo(6, 2); stroke(ctx, 9, C.navy); ctx.restore(); }
  if (d.label) textC(ctx, o, d.label, 450, 550, 30, C.navy, 800, 'head', 700);
};
// 11. growth chart with coins
ART.growth = (ctx, lt, d, o) => {
  const t = lt; rrs(ctx, 120, 90, 660, 420, 22, '#FFFFFF', 6);
  ctx.beginPath(); ctx.moveTo(170, 120); ctx.lineTo(170, 460); ctx.lineTo(740, 460); stroke(ctx, 6);
  const vals = d.values || [30, 45, 62, 90];
  vals.forEach((v, i) => { const p = easeOut(fade(lt, 0.3 + i * 0.2, 0.6)); const h = 300 * v / Math.max(...vals) * p; rrs(ctx, 210 + i * 130, 460 - h, 86, h, 10, [C.cyan, C.mid, C.blue, C.navy][i % 4], 5); });
  const lp = fade(lt, 1.2, 0.6); ctx.beginPath(); vals.forEach((v, i) => { const x = 253 + i * 130, y = 440 - 300 * v / Math.max(...vals) - 30; if (i / (vals.length - 1) <= lp) i ? ctx.lineTo(x, y) : ctx.moveTo(x, y); }); stroke(ctx, 10, C.lime);
  [0, 1, 2].forEach((k) => { const p = pop(lt, 1.5 + k * 0.15); if (p > 0) { ctx.save(); ctx.translate(800, 470 - k * 34); ctx.scale(p, p); ctx.beginPath(); ctx.ellipse(0, 0, 54, 20, 0, 0, Math.PI * 2); shape(ctx, C.lime, 5); ctx.restore(); } });
  if (d.label) textC(ctx, o, d.label, 450, 70, 34, C.navy, 800, 'head', 700);
};
const ART_NAMES = Object.keys(ART);
/** draw an art illustration inside a box (scaled from the 900x560 stage), with a cream card behind */
function drawArt(ctx, ill, lt, box, o, card) {
  const fn = ART[ill.art] || ART.shop; const a = easeBack(lt / 0.45);
  ctx.save(); ctx.globalAlpha = clamp(a, 0, 1);
  const s = Math.min(box.w / 900, box.h / 560); const ox = box.x + (box.w - 900 * s) / 2, oy = box.y + (box.h - 560 * s) / 2;
  if (card !== false) { ctx.fillStyle = 'rgba(7,27,110,.18)'; rr(ctx, box.x + 10, box.y + 16, box.w, box.h, 34); ctx.fill(); fillRR(ctx, box.x, box.y, box.w, box.h, 34, S2.cream); }
  ctx.save(); rr(ctx, box.x, box.y, box.w, box.h, 34); ctx.clip();
  ctx.translate(ox, oy); ctx.scale(s, s); fn(ctx, lt, ill, o);
  ctx.restore(); ctx.restore();
}
// ===================== /ART LIBRARY =====================
