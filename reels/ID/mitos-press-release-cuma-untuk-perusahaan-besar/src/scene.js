/* VRITIMES Reel scene renderer — motion-graphic POV of a VRITIMES PR specialist talking to camera.
   One file shared by the dashboard preview and the Remotion project (canvas 1080x1920).
   API: VRScene.loadAssets({logoWhite, logoColor, besideWhite}) -> Promise<assets>
        VRScene.timeline(reel) -> {durs, starts, total}
        VRScene.drawFrame(ctx, reel, durs, t, assets, opts)
        VRScene.drawScene(ctx, reel, i, lt, dur, assets, opts)
        VRScene.estimate(text, lang) -> seconds
   v2 (VRITIMES repo): 2D art library (illus.type 'art') + beats: a new illustration every reel.beatSec (default 4) seconds.
   A scene may list extra illustrations in scene.beats[]; beat k starts at k*beatSec inside the scene. */
(function (root) {
'use strict';
const W = 1080, H = 1920;
const C = {blue: '#0058F8', navy: '#071B6E', pale: '#E8F1FF', cyan: '#00C8F8', mid: '#0098F8', lime: '#D7F23C', ink: '#0A1440', white: '#FFFFFF'};
const clamp = (x, a, b) => Math.max(a, Math.min(b, x));
const easeOut = (x) => 1 - Math.pow(1 - clamp(x, 0, 1), 3);
const easeBack = (x) => { x = clamp(x, 0, 1); const c1 = 1.70158, c3 = c1 + 1; return 1 + c3 * Math.pow(x - 1, 3) + c1 * Math.pow(x - 1, 2); };
const lerp = (a, b, x) => a + (b - a) * x;
const noise = (t, s) => Math.sin(t * 1.7 + s) * 0.5 + Math.sin(t * 2.9 + s * 2.3) * 0.3 + Math.sin(t * 5.1 + s * 0.7) * 0.2;

const ICONS = {
 news: '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 100 100"><rect x="14" y="20" width="62" height="64" rx="8" fill="#0058F8"/><rect x="76" y="34" width="12" height="50" rx="6" fill="#071B6E"/><rect x="24" y="30" width="42" height="12" rx="3" fill="#fff"/><rect x="24" y="50" width="42" height="5" rx="2" fill="#E8F1FF"/><rect x="24" y="60" width="42" height="5" rx="2" fill="#E8F1FF"/><rect x="24" y="70" width="28" height="5" rx="2" fill="#E8F1FF"/></svg>',
 mega: '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 100 100"><path d="M18 42h14l34-18v52L32 58H18z" fill="#0058F8"/><rect x="24" y="58" width="12" height="22" rx="5" fill="#071B6E"/><path d="M74 38q10 12 0 24" stroke="#D7F23C" stroke-width="6" fill="none" stroke-linecap="round"/><path d="M80 30q18 20 0 40" stroke="#00C8F8" stroke-width="6" fill="none" stroke-linecap="round"/></svg>',
 chart: '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 100 100"><rect x="16" y="56" width="14" height="28" rx="4" fill="#00C8F8"/><rect x="38" y="42" width="14" height="42" rx="4" fill="#0098F8"/><rect x="60" y="24" width="14" height="60" rx="4" fill="#0058F8"/><path d="M14 40l24-14 18 10 28-20" stroke="#D7F23C" stroke-width="6" fill="none" stroke-linecap="round" stroke-linejoin="round"/></svg>',
 mail: '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 100 100"><rect x="12" y="24" width="76" height="54" rx="10" fill="#0058F8"/><path d="M14 30l36 26 36-26" stroke="#fff" stroke-width="6" fill="none" stroke-linejoin="round"/><circle cx="80" cy="26" r="12" fill="#D7F23C"/></svg>',
 link: '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 100 100"><rect x="10" y="38" width="46" height="26" rx="13" stroke="#0058F8" stroke-width="9" fill="none"/><rect x="44" y="38" width="46" height="26" rx="13" stroke="#00C8F8" stroke-width="9" fill="none"/></svg>',
 clock: '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 100 100"><circle cx="50" cy="52" r="34" fill="#0058F8"/><path d="M50 32v22l14 8" stroke="#fff" stroke-width="7" fill="none" stroke-linecap="round"/><circle cx="50" cy="52" r="5" fill="#D7F23C"/></svg>',
 cal: '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 100 100"><rect x="16" y="22" width="68" height="62" rx="10" fill="#0058F8"/><rect x="16" y="22" width="68" height="18" rx="9" fill="#071B6E"/><g fill="#fff"><rect x="26" y="50" width="10" height="10" rx="2"/><rect x="45" y="50" width="10" height="10" rx="2"/><rect x="64" y="50" width="10" height="10" rx="2" fill="#D7F23C"/><rect x="26" y="66" width="10" height="10" rx="2"/><rect x="45" y="66" width="10" height="10" rx="2"/></g></svg>',
 eye: '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 100 100"><path d="M8 50q42-44 84 0q-42 44-84 0z" fill="#0058F8"/><circle cx="50" cy="50" r="16" fill="#fff"/><circle cx="50" cy="50" r="8" fill="#071B6E"/></svg>',
 shield: '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 100 100"><path d="M50 12l32 12v24c0 20-14 34-32 40c-18-6-32-20-32-40V24z" fill="#0058F8"/><path d="M36 50l10 10 18-20" stroke="#D7F23C" stroke-width="7" fill="none" stroke-linecap="round" stroke-linejoin="round"/></svg>',
 quote: '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 100 100"><path d="M20 60c0-18 8-30 24-34v10c-8 3-12 9-12 16h12v22H20zM56 60c0-18 8-30 24-34v10c-8 3-12 9-12 16h12v22H56z" fill="#0058F8"/></svg>',
 pdf: '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 100 100"><path d="M24 10h36l18 18v62H24z" fill="#fff" stroke="#071B6E" stroke-width="5"/><path d="M60 10v18h18" fill="none" stroke="#071B6E" stroke-width="5"/><rect x="14" y="52" width="52" height="24" rx="5" fill="#0058F8"/><path d="M26 58h6a4 4 0 010 8h-6zM38 58v12M38 58h5a6 6 0 010 12h-5M52 58h8M52 58v12M52 64h6" stroke="#fff" stroke-width="2.5" fill="none"/></svg>',
 phone: '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 100 100"><rect x="30" y="10" width="40" height="80" rx="9" fill="#071B6E"/><rect x="34" y="18" width="32" height="58" rx="3" fill="#E8F1FF"/><rect x="38" y="24" width="24" height="6" rx="2" fill="#0058F8"/><rect x="38" y="34" width="24" height="4" rx="2" fill="#00C8F8"/><rect x="38" y="42" width="18" height="4" rx="2" fill="#00C8F8"/><circle cx="50" cy="83" r="3" fill="#D7F23C"/></svg>',
 search: '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 100 100"><circle cx="44" cy="44" r="24" stroke="#0058F8" stroke-width="10" fill="#E8F1FF"/><path d="M62 62l20 20" stroke="#071B6E" stroke-width="12" stroke-linecap="round"/></svg>',
 target: '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 100 100"><circle cx="50" cy="50" r="38" fill="#0058F8"/><circle cx="50" cy="50" r="26" fill="#fff"/><circle cx="50" cy="50" r="14" fill="#00C8F8"/><circle cx="50" cy="50" r="5" fill="#071B6E"/><path d="M50 50L84 16" stroke="#D7F23C" stroke-width="6" stroke-linecap="round"/></svg>',
 rocket: '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 100 100"><path d="M50 10c16 10 22 30 18 50H32c-4-20 2-40 18-50z" fill="#0058F8"/><circle cx="50" cy="38" r="8" fill="#fff"/><path d="M32 60l-10 14h16zM68 60l10 14H62z" fill="#071B6E"/><path d="M42 64q8 26 16 0" fill="#D7F23C"/></svg>',
};
const ICON_NAMES = Object.keys(ICONS);

function loadImg(src) {
  return new Promise((res) => { if (!src) return res(null); const im = new Image(); im.onload = () => res(im); im.onerror = () => res(null); im.src = src; });
}
async function loadAssets(src) {
  const a = {icons: {}};
  const [lw, lc, bw] = await Promise.all([loadImg(src.logoWhite), loadImg(src.logoColor), loadImg(src.besideWhite)]);
  a.logoWhite = lw; a.logoColor = lc; a.besideWhite = bw;
  await Promise.all(ICON_NAMES.map(async (k) => { a.icons[k] = await loadImg('data:image/svg+xml;charset=utf-8,' + encodeURIComponent(ICONS[k])); }));
  return a;
}
function estimate(text, lang) {
  text = String(text || '').replace(/[*[\]]/g, '');
  if (lang === 'th') return clamp(text.replace(/\s/g, '').length / 13 + 0.6, 2.2, 10);
  const words = text.split(/\s+/).filter(Boolean).length;
  const rate = {id: 2.35, vn: 2.9, en: 2.6}[lang] || 2.5;
  return clamp(words / rate + 0.6, 2.2, 10);
}
function timeline(reel) {
  const durs = (reel.scenes || []).map((s) => Number(s.dur) > 0 ? Number(s.dur) : estimate(s.vo, reel.lang));
  const starts = []; let acc = 0; durs.forEach((d) => { starts.push(acc); acc += d; });
  return {durs, starts, total: acc};
}

// ---------- drawing helpers ----------
function rr(ctx, x, y, w, h, r) { r = Math.min(r, w / 2, h / 2); ctx.beginPath(); ctx.moveTo(x + r, y); ctx.arcTo(x + w, y, x + w, y + h, r); ctx.arcTo(x + w, y + h, x, y + h, r); ctx.arcTo(x, y + h, x, y, r); ctx.arcTo(x, y, x + w, y, r); ctx.closePath(); }
function fillRR(ctx, x, y, w, h, r, fill) { rr(ctx, x, y, w, h, r); ctx.fillStyle = fill; ctx.fill(); }
function font(o, weight, size, kind) { return `${weight} ${size}px ${kind === 'body' ? o.fBody : kind === 'hand' ? o.fHand : o.fHead}`; }
/** rich text with *highlight* markup, wrapped; returns height. align: 'center'|'left' */
function richText(ctx, text, x, y, maxW, size, o, opt = {}) {
  const color = opt.color || C.navy, hl = opt.hl || C.blue, weight = opt.weight || 800, lh = opt.lh || 1.12, align = opt.align || 'center', kind = opt.kind || 'head';
  const raw = String(text || '').replace(/\*\*/g, '');
  const tokens = []; let on = false, alt = false;
  raw.split(/(\*|\[|\])/).forEach((part) => { if (part === '*') { on = !on; return; } if (part === '[') { alt = true; return; } if (part === ']') { alt = false; return; } part.split(/(\s+)/).forEach((w) => { if (w) tokens.push({w, hl: on || alt, alt}); }); });
  const lines = [];
  const fit = (sz) => {
    ctx.font = font(o, weight, sz, kind); lines.length = 0; let cur = [], cw = 0;
    tokens.forEach((tk) => {
      if (tk.w === '\n') return;
      const ww = ctx.measureText(tk.w).width;
      if (/^\s+$/.test(tk.w)) { if (cur.length) { cur.push(tk); cw += ww; } return; }
      if (cw + ww > maxW && cur.length) { while (cur.length && /^\s+$/.test(cur[cur.length - 1].w)) cur.pop(); lines.push(cur); cur = []; cw = 0; }
      cur.push(tk); cw += ww;
    });
    if (cur.length) lines.push(cur);
    return lines.length;
  };
  let sz = size; const maxLines = opt.maxLines || 4;
  while (fit(sz) > maxLines && sz > size * 0.55) sz -= 4;
  ctx.font = font(o, weight, sz, kind); ctx.textBaseline = 'alphabetic';
  lines.forEach((ln, i) => {
    const lw = ln.reduce((a, tk) => a + ctx.measureText(tk.w).width, 0);
    let cx = align === 'center' ? x - lw / 2 : x;
    const cy = y + sz * 0.9 + i * sz * lh;
    ln.forEach((tk) => {
      const tw = ctx.measureText(tk.w).width;
      const bx = tk.alt && opt.altBox ? opt.altBox : opt.box;
      if (tk.hl && bx && !/^\s+$/.test(tk.w)) { fillRR(ctx, cx - 6, cy - sz * 0.82, tw + 12, sz * 1.05, 10, bx); }
      ctx.fillStyle = tk.hl ? (bx ? (opt.boxText || C.navy) : (tk.alt && opt.alt ? opt.alt : hl)) : color; ctx.fillText(tk.w, cx, cy); cx += tw;
    });
  });
  return lines.length * sz * lh;
}

// ---------- background: office studio ----------
function drawStudio(ctx, t) {
  const g = ctx.createLinearGradient(0, 0, 0, H); g.addColorStop(0, '#E9EFF9'); g.addColorStop(0.55, '#DCE5F4'); g.addColorStop(1, '#C9D5EA');
  ctx.fillStyle = g; ctx.fillRect(0, 0, W, H);
  // window with blinds (left)
  ctx.save();
  fillRR(ctx, -40, 520, 360, 760, 18, '#F7FBFF');
  const lg = ctx.createLinearGradient(-40, 520, 320, 1280); lg.addColorStop(0, 'rgba(255,248,225,.95)'); lg.addColorStop(1, 'rgba(210,230,255,.9)');
  fillRR(ctx, -24, 536, 328, 728, 12, lg);
  ctx.fillStyle = 'rgba(160,178,210,.55)';
  for (let y = 556; y < 1260; y += 34) ctx.fillRect(-24, y, 328, 9);
  ctx.fillStyle = '#B7C4DC'; ctx.fillRect(132, 536, 8, 728);
  // light beam
  ctx.globalAlpha = 0.18; ctx.fillStyle = '#FFF6D8';
  ctx.beginPath(); ctx.moveTo(300, 560); ctx.lineTo(760, 1500); ctx.lineTo(560, 1600); ctx.lineTo(300, 1240); ctx.closePath(); ctx.fill();
  ctx.restore();
  // shelf (right)
  ctx.fillStyle = '#B98F64'; ctx.fillRect(790, 760, 300, 18); ctx.fillRect(790, 1010, 300, 18);
  const books = [[808, 640, 34, 120, C.blue], [846, 660, 26, 100, C.navy], [876, 630, 30, 130, '#7FA8FF'], [910, 670, 22, 90, C.lime], [936, 650, 34, 110, C.mid], [980, 700, 120, 60, '#E7EEFA']];
  books.forEach(([x, y, w, h, c]) => fillRR(ctx, x, y, w, h, 4, c));
  ctx.save(); ctx.translate(1010, 700); ctx.rotate(-0.25); fillRR(ctx, 0, 0, 30, 70, 4, C.navy); ctx.restore();
  // plant on shelf
  fillRR(ctx, 960, 930, 70, 80, 12, '#F1F4FA');
  ctx.fillStyle = '#3E9B6B';
  for (let k = 0; k < 7; k++) { ctx.save(); ctx.translate(995, 935); ctx.rotate(-1.2 + k * 0.4 + Math.sin(t * 0.8 + k) * 0.03); ctx.beginPath(); ctx.ellipse(0, -48, 13, 46, 0, 0, Math.PI * 2); ctx.fill(); ctx.restore(); }
  // award / frame
  fillRR(ctx, 830, 880, 96, 120, 8, '#FFFFFF'); fillRR(ctx, 842, 892, 72, 72, 4, C.pale);
  ctx.fillStyle = C.blue; ctx.beginPath(); ctx.arc(878, 928, 22, 0, Math.PI * 2); ctx.fill();
  // brand wall stripe + neon-ish sign
  const sg = ctx.createLinearGradient(0, 1090, W, 1090); sg.addColorStop(0, 'rgba(0,88,248,0)'); sg.addColorStop(0.5, 'rgba(0,88,248,.12)'); sg.addColorStop(1, 'rgba(0,88,248,0)');
  ctx.fillStyle = sg; ctx.fillRect(0, 1080, W, 40);
  // softbox glow
  const rg = ctx.createRadialGradient(540, 980, 60, 540, 980, 620); rg.addColorStop(0, 'rgba(255,255,255,.55)'); rg.addColorStop(1, 'rgba(255,255,255,0)');
  ctx.fillStyle = rg; ctx.fillRect(0, 300, W, 1400);
  // bokeh
  for (let k = 0; k < 9; k++) {
    const bx = (k * 137 + 60) % W, by = 360 + ((k * 211) % 900) + Math.sin(t * 0.4 + k) * 8;
    ctx.fillStyle = `rgba(${k % 2 ? '0,200,248' : '255,255,255'},${0.08 + (k % 3) * 0.03})`; ctx.beginPath(); ctx.arc(bx, by, 26 + (k % 4) * 10, 0, Math.PI * 2); ctx.fill();
  }
}

// ---------- character: male PR specialist, ~30 ----------
const SKIN = '#C98E6B', SKIN_D = '#B07656', HAIR = '#1F1A1D', SUIT = '#1C2B5E', SUIT_D = '#14204A', SHIRT = '#EAF2FF';
function drawPerson(ctx, t, talk, gesture, gt) {
  const bob = Math.sin(t * 2.2) * 5 + (talk ? Math.sin(t * 7.3) * 2.5 : 0);
  const sway = Math.sin(t * 0.9) * 6;
  const cx = 540 + sway * 0.4, headY = 1010 + bob;
  // torso
  ctx.save();
  ctx.translate(sway * 0.25, bob * 0.35);
  ctx.fillStyle = SUIT;
  ctx.beginPath(); ctx.moveTo(250, 1560); ctx.bezierCurveTo(250, 1330, 330, 1250, 460, 1225); ctx.lineTo(620, 1225); ctx.bezierCurveTo(750, 1250, 830, 1330, 830, 1560); ctx.closePath(); ctx.fill();
  // shirt V + collar
  ctx.fillStyle = SHIRT; ctx.beginPath(); ctx.moveTo(470, 1222); ctx.lineTo(610, 1222); ctx.lineTo(540, 1390); ctx.closePath(); ctx.fill();
  ctx.fillStyle = '#FFFFFF'; ctx.beginPath(); ctx.moveTo(478, 1218); ctx.lineTo(540, 1262); ctx.lineTo(510, 1300); ctx.closePath(); ctx.fill();
  ctx.beginPath(); ctx.moveTo(602, 1218); ctx.lineTo(540, 1262); ctx.lineTo(570, 1300); ctx.closePath(); ctx.fill();
  // lapels
  ctx.fillStyle = SUIT_D;
  ctx.beginPath(); ctx.moveTo(462, 1228); ctx.lineTo(518, 1330); ctx.lineTo(540, 1400); ctx.lineTo(450, 1300); ctx.closePath(); ctx.fill();
  ctx.beginPath(); ctx.moveTo(618, 1228); ctx.lineTo(562, 1330); ctx.lineTo(540, 1400); ctx.lineTo(630, 1300); ctx.closePath(); ctx.fill();
  // pin
  ctx.fillStyle = C.lime; ctx.beginPath(); ctx.arc(612, 1318, 9, 0, Math.PI * 2); ctx.fill();
  ctx.restore();
  // neck
  ctx.fillStyle = SKIN_D; fillRR(ctx, cx - 44, headY + 110, 88, 110, 30, SKIN_D);
  // head
  ctx.save();
  ctx.translate(cx, headY); ctx.rotate(Math.sin(t * 0.8) * 0.025 + (talk ? Math.sin(t * 3.1) * 0.012 : 0));
  // ears
  ctx.fillStyle = SKIN_D; ctx.beginPath(); ctx.ellipse(-112, 10, 20, 32, 0, 0, Math.PI * 2); ctx.ellipse(112, 10, 20, 32, 0, 0, Math.PI * 2); ctx.fill();
  // face
  ctx.fillStyle = SKIN; ctx.beginPath(); ctx.ellipse(0, 0, 112, 138, 0, 0, Math.PI * 2); ctx.fill();
  // stubble / jaw shade
  ctx.fillStyle = 'rgba(60,40,35,.16)'; ctx.beginPath(); ctx.ellipse(0, 70, 92, 66, 0, 0.05 * Math.PI, 0.95 * Math.PI); ctx.fill();
  // hair (short, side part, slight quiff)
  ctx.fillStyle = HAIR;
  ctx.beginPath(); ctx.moveTo(-116, -10); ctx.bezierCurveTo(-128, -120, -60, -170, 10, -166); ctx.bezierCurveTo(90, -166, 136, -110, 118, -6);
  ctx.bezierCurveTo(108, -60, 80, -92, 30, -98); ctx.bezierCurveTo(-10, -102, -40, -86, -60, -96); ctx.bezierCurveTo(-90, -80, -104, -50, -116, -10); ctx.fill();
  ctx.beginPath(); ctx.moveTo(-40, -150); ctx.quadraticCurveTo(40, -190, 100, -128); ctx.quadraticCurveTo(40, -150, -40, -150); ctx.fill();
  // eyebrows
  const raise = gesture === 'surprise' ? 10 : (talk ? Math.max(0, Math.sin(t * 2.6)) * 5 : 0);
  ctx.fillStyle = HAIR; fillRR(ctx, -78, -48 - raise, 52, 11, 6, HAIR); fillRR(ctx, 26, -48 - raise, 52, 11, 6, HAIR);
  // eyes + blink
  const bl = (t % 3.7) < 0.12 ? 0.12 : 1;
  ctx.fillStyle = '#FFFFFF'; ctx.beginPath(); ctx.ellipse(-50, -16, 17, 12 * bl, 0, 0, Math.PI * 2); ctx.ellipse(50, -16, 17, 12 * bl, 0, 0, Math.PI * 2); ctx.fill();
  if (bl > 0.5) { ctx.fillStyle = '#2B1D17'; const lx = Math.sin(t * 0.7) * 3; ctx.beginPath(); ctx.arc(-50 + lx, -15, 8, 0, Math.PI * 2); ctx.arc(50 + lx, -15, 8, 0, Math.PI * 2); ctx.fill(); }
  // glasses
  ctx.strokeStyle = '#1A1E2C'; ctx.lineWidth = 6; rr(ctx, -88, -42, 74, 52, 16); ctx.stroke(); rr(ctx, 14, -42, 74, 52, 16); ctx.stroke();
  ctx.beginPath(); ctx.moveTo(-14, -20); ctx.quadraticCurveTo(0, -28, 14, -20); ctx.stroke();
  ctx.beginPath(); ctx.moveTo(-88, -22); ctx.lineTo(-110, -14); ctx.moveTo(88, -22); ctx.lineTo(110, -14); ctx.stroke();
  // nose
  ctx.strokeStyle = SKIN_D; ctx.lineWidth = 6; ctx.lineCap = 'round'; ctx.beginPath(); ctx.moveTo(0, 0); ctx.quadraticCurveTo(-12, 34, 4, 38); ctx.stroke();
  // mouth
  const open = talk ? clamp(0.25 + 0.75 * Math.abs(Math.sin(t * 11.5)) * (0.55 + 0.45 * Math.abs(noise(t * 3, 1))), 0, 1) : 0;
  if (open > 0.12) {
    ctx.fillStyle = '#5B2324'; ctx.beginPath(); ctx.ellipse(0, 78, 34, 8 + open * 20, 0, 0, Math.PI * 2); ctx.fill();
    ctx.fillStyle = '#FFFFFF'; ctx.fillRect(-22, 70 - open * 10, 44, 7);
  } else {
    ctx.strokeStyle = '#7A3A33'; ctx.lineWidth = 7; ctx.beginPath(); ctx.moveTo(-30, 74); ctx.quadraticCurveTo(0, 96, 30, 74); ctx.stroke();
  }
  ctx.restore();
  return {cx, headY};
}
function drawArm(ctx, side, raise, t) {
  // side: -1 left, 1 right (viewer). raise 0..1 lifts hand to explain
  const sx = 540 + side * 250, sy = 1330;
  const hx = 540 + side * lerp(200, 300, raise), hy = lerp(1470, 1150, raise) + Math.sin(t * 6) * 10 * raise;
  ctx.strokeStyle = SUIT; ctx.lineWidth = 92; ctx.lineCap = 'round';
  ctx.beginPath(); ctx.moveTo(sx, sy); ctx.quadraticCurveTo(540 + side * 330, lerp(1480, 1360, raise), hx, hy + 40); ctx.stroke();
  ctx.fillStyle = '#FFFFFF'; ctx.beginPath(); ctx.ellipse(hx, hy + 34, 44, 18, side * 0.3, 0, Math.PI * 2); ctx.fill();
  ctx.fillStyle = SKIN; ctx.beginPath(); ctx.ellipse(hx, hy, 40, 46, side * 0.2, 0, Math.PI * 2); ctx.fill();
  if (raise > 0.6) { ctx.fillStyle = SKIN; fillRR(ctx, hx - 10 + side * 6, hy - 92, 20, 60, 10, SKIN); }
}
function drawLaptop(ctx, assets, t) {
  // desk
  const dg = ctx.createLinearGradient(0, 1760, 0, H); dg.addColorStop(0, '#F4F1EC'); dg.addColorStop(1, '#D9D2C7');
  ctx.fillStyle = dg; ctx.fillRect(0, 1770, W, 150);
  ctx.fillStyle = 'rgba(0,0,0,.08)'; ctx.fillRect(0, 1770, W, 6);
  // mug
  fillRR(ctx, 860, 1680, 100, 118, 16, '#FFFFFF'); ctx.strokeStyle = '#FFFFFF'; ctx.lineWidth = 16; ctx.beginPath(); ctx.arc(966, 1736, 26, -1.2, 1.2); ctx.stroke();
  fillRR(ctx, 872, 1712, 76, 30, 6, C.blue);
  ctx.globalAlpha = 0.35; ctx.strokeStyle = '#FFFFFF'; ctx.lineWidth = 6;
  for (let k = 0; k < 2; k++) { ctx.beginPath(); const ox = 890 + k * 30, of = Math.sin(t * 2 + k) * 6; ctx.moveTo(ox, 1666); ctx.quadraticCurveTo(ox + 14 + of, 1630, ox, 1596); ctx.stroke(); }
  ctx.globalAlpha = 1;
  // laptop lid (back side facing camera)
  const lx = 250, ly = 1440, lw = 580, lh = 380;
  ctx.fillStyle = 'rgba(7,27,110,.18)'; rr(ctx, lx - 10, ly + 20, lw + 20, lh, 30); ctx.fill();
  const g = ctx.createLinearGradient(lx, ly, lx + lw, ly + lh); g.addColorStop(0, '#3A4358'); g.addColorStop(0.5, '#2A3144'); g.addColorStop(1, '#1E2434');
  rr(ctx, lx, ly, lw, lh, 26); ctx.fillStyle = g; ctx.fill();
  ctx.strokeStyle = 'rgba(255,255,255,.18)'; ctx.lineWidth = 3; rr(ctx, lx + 3, ly + 3, lw - 6, lh - 6, 24); ctx.stroke();
  // sheen
  ctx.save(); rr(ctx, lx, ly, lw, lh, 26); ctx.clip();
  ctx.fillStyle = 'rgba(255,255,255,.06)'; ctx.beginPath(); ctx.moveTo(lx + lw * 0.55, ly); ctx.lineTo(lx + lw * 0.8, ly); ctx.lineTo(lx + lw * 0.45, ly + lh); ctx.lineTo(lx + lw * 0.2, ly + lh); ctx.closePath(); ctx.fill();
  ctx.restore();
  // logo centred on lid
  const logo = assets.logoWhite;
  if (logo) { const s = 230 / logo.width; const w = logo.width * s, h = logo.height * s; ctx.globalAlpha = 0.95; ctx.drawImage(logo, lx + lw / 2 - w / 2, ly + lh / 2 - h / 2 - 6, w, h); ctx.globalAlpha = 1; }
  else { ctx.fillStyle = '#FFFFFF'; ctx.font = '800 54px sans-serif'; ctx.textAlign = 'center'; ctx.fillText('VRITIMES', lx + lw / 2, ly + lh / 2); ctx.textAlign = 'left'; }
  // base edge
  fillRR(ctx, lx - 40, ly + lh - 6, lw + 80, 26, 12, '#9AA4B8');
}

// ---------- illustration panel ----------
function drawPanelIn(ctx, scene, lt, dur, assets, o, box) { return drawPanel(ctx, scene, lt, dur, assets, o, 0, 1, box); }
function drawPanel(ctx, scene, lt, dur, assets, o, idx, n, box) {
  const ill = scene.illus || {type: 'title', text: scene.onscreen || ''};
  const appear = easeBack(lt / 0.55), leave = lt > dur - 0.35 ? easeOut((lt - (dur - 0.35)) / 0.35) : 0;
  const sc = lerp(0.86, 1, appear) * (1 - leave * 0.06), al = clamp(appear, 0, 1) * (1 - leave);
  const px = box ? box.px : 70, py = box ? box.py : 170, pw = box ? box.pw : 940, ph = box ? box.ph : 640;
  ctx.save(); ctx.globalAlpha = al;
  ctx.translate(px + pw / 2, py + ph / 2 + (1 - appear) * 40 + Math.sin(lt * 1.6) * 6); ctx.scale(sc, sc); ctx.translate(-(px + pw / 2), -(py + ph / 2));
  ctx.fillStyle = 'rgba(7,27,110,.16)'; rr(ctx, px + 10, py + 22, pw, ph, 46); ctx.fill();
  fillRR(ctx, px, py, pw, ph, box ? 22 : 46, (box && box.bg) || '#FFFFFF');
  // header pill = on-screen text
  const head = scene.onscreen || '';
  let top = py + 46;
  if (head && ill.type !== 'title') { top += richText(ctx, head, px + pw / 2, top - 10, pw - 120, 56, o, {color: C.navy, hl: C.blue, maxLines: 2}) + 18; }
  const area = {x: px + 50, y: top, w: pw - 100, h: py + ph - 40 - top};
  const k = (d) => clamp((lt - 0.35 - d) / 0.45, 0, 1);
  const type = ill.type || 'title';
  if (type === 'title' || type === 'hook') {
    richText(ctx, ill.text || head, px + pw / 2, py + 120, pw - 120, 104, o, {color: C.navy, box: C.lime, boxText: C.navy, maxLines: 4});
  } else if (type === 'stat') {
    const raw = String(ill.big || ''); const num = parseFloat(raw.replace(/[^0-9.,]/g, '').replace(',', '.'));
    let shown = raw;
    if (!isNaN(num) && /\d/.test(raw)) { const p = easeOut((lt - 0.3) / 1.2); const v = num * p; const dec = (raw.split(/[.,]/)[1] || '').replace(/\D/g, '').length; shown = raw.replace(/[0-9]+([.,][0-9]+)?/, v.toFixed(Math.min(dec, 2)).replace('.', raw.includes(',') ? ',' : '.')); }
    ctx.font = font(o, 800, 230, 'head'); ctx.fillStyle = C.blue; ctx.textAlign = 'center'; ctx.fillText(shown, px + pw / 2, area.y + 210); ctx.textAlign = 'left';
    richText(ctx, ill.label || '', px + pw / 2, area.y + 250, pw - 140, 46, o, {color: C.navy, hl: C.blue, weight: 700, maxLines: 3});
  } else if (type === 'list' || type === 'steps') {
    const items = (ill.items || []).slice(0, 4); const rowH = Math.min(132, area.h / Math.max(items.length, 1));
    items.forEach((it, i) => {
      const a = easeBack(k(i * 0.35)); if (a <= 0) return;
      const y = area.y + i * rowH; ctx.save(); ctx.globalAlpha *= clamp(a, 0, 1); ctx.translate((1 - a) * -60, 0);
      fillRR(ctx, area.x, y, area.w, rowH - 18, 40, C.pale);
      ctx.fillStyle = type === 'steps' ? C.navy : C.blue; ctx.beginPath(); ctx.arc(area.x + 42, y + (rowH - 18) / 2, 28, 0, Math.PI * 2); ctx.fill();
      ctx.fillStyle = type === 'steps' ? C.lime : '#FFFFFF'; ctx.font = font(o, 800, 30, 'head'); ctx.textAlign = 'center'; ctx.fillText(type === 'steps' ? String(i + 1) : '✓', area.x + 42, y + (rowH - 18) / 2 + 11); ctx.textAlign = 'left';
      richText(ctx, it, area.x + 92, y + (rowH - 18) / 2 - (rowH > 110 ? 26 : 22), area.w - 124, rowH > 110 ? 42 : 36, o, {color: C.navy, hl: C.blue, weight: 600, kind: 'body', align: 'left', maxLines: 2});
      ctx.restore();
    });
  } else if (type === 'compare') {
    const cw = (area.w - 30) / 2;
    [['left', '✕', '#F2F5FB', C.navy], ['right', '✓', C.blue, '#FFFFFF']].forEach(([key, mk, bg, fg], j) => {
      const a = easeBack(k(j * 0.5)); if (a <= 0) return; const c = ill[key] || {};
      const x = area.x + j * (cw + 30);
      ctx.save(); ctx.globalAlpha *= clamp(a, 0, 1); ctx.translate(0, (1 - a) * 50);
      fillRR(ctx, x, area.y, cw, area.h, 34, bg);
      if (j === 0) { ctx.setLineDash([14, 10]); ctx.strokeStyle = 'rgba(7,27,110,.35)'; ctx.lineWidth = 4; rr(ctx, x, area.y, cw, area.h, 34); ctx.stroke(); ctx.setLineDash([]); }
      ctx.fillStyle = fg; ctx.font = font(o, 800, 40, 'head'); ctx.fillText(mk + ' ' + String(c.h || ''), x + 30, area.y + 64);
      (c.items || []).slice(0, 3).forEach((it, i) => { richText(ctx, '• ' + it, x + 30, area.y + 100 + i * 112, cw - 60, 36, o, {color: fg, hl: j ? C.lime : C.blue, weight: 500, kind: 'body', align: 'left', maxLines: 2}); });
      ctx.restore();
    });
  } else if (type === 'chart') {
    const bars = (ill.bars || []).slice(0, 5); const max = Math.max(1, ...bars.map((b) => Number(b.value) || 0));
    const bw = area.w / Math.max(bars.length, 1);
    bars.forEach((b, i) => {
      const p = easeOut(k(i * 0.2)); const bh = (area.h - 90) * (Number(b.value) || 0) / max * p; const x = area.x + i * bw + bw * 0.18, y = area.y + area.h - 50 - bh;
      fillRR(ctx, x, y, bw * 0.64, Math.max(bh, 2), 16, i === bars.length - 1 ? C.blue : [C.cyan, C.mid][i % 2]);
      ctx.fillStyle = C.navy; ctx.font = font(o, 800, 34, 'head'); ctx.textAlign = 'center';
      if (p > 0.6) ctx.fillText(String(b.value) + (ill.unit || ''), x + bw * 0.32, y - 14);
      ctx.font = font(o, 600, 26, 'body'); ctx.fillText(String(b.label || ''), x + bw * 0.32, area.y + area.h - 10); ctx.textAlign = 'left';
    });
  } else if (type === 'chat') {
    const msgs = (ill.messages || []).slice(0, 4); let y = area.y;
    msgs.forEach((m, i) => {
      const a = easeBack(k(i * 0.6)); if (a <= 0) return; const me = m.from !== 'them';
      ctx.font = font(o, 500, 32, 'body'); const tw = Math.min(area.w * 0.72, ctx.measureText(String(m.text || '')).width + 60); const bh = 84;
      const x = me ? area.x + area.w - tw : area.x;
      ctx.save(); ctx.globalAlpha *= clamp(a, 0, 1); ctx.translate(0, (1 - a) * 30);
      fillRR(ctx, x, y, tw, bh, 32, me ? C.blue : C.pale);
      richText(ctx, String(m.text || ''), x + 30, y + 8, tw - 60, 32, o, {color: me ? '#FFFFFF' : C.navy, hl: me ? C.lime : C.blue, weight: 500, kind: 'body', align: 'left', maxLines: 1});
      ctx.restore(); y += bh + 22;
    });
  } else if (type === 'quote') {
    const im = assets.icons.quote; if (im) ctx.drawImage(im, px + pw / 2 - 55, area.y, 110, 110);
    richText(ctx, '“' + String(ill.text || '').replace(/^["“]|["”]$/g, '') + '”', px + pw / 2, area.y + 110, pw - 160, 54, o, {color: C.navy, hl: C.blue, maxLines: 4});
    if (ill.by) { ctx.font = font(o, 700, 40, 'hand'); ctx.fillStyle = C.blue; ctx.textAlign = 'center'; ctx.fillText('— ' + ill.by, px + pw / 2, py + ph - 50); ctx.textAlign = 'left'; }
  } else if (type === 'cta') {
    if (assets.logoColor) { const s = 260 / assets.logoColor.width; ctx.drawImage(assets.logoColor, px + pw / 2 - 130, area.y - 10, 260, assets.logoColor.height * s); }
    const url = ill.url || ('vritimes.com/' + String(o.cc || 'id').toLowerCase());
    const a = easeBack(k(0.2));
    ctx.save(); ctx.globalAlpha *= clamp(a, 0, 1);
    ctx.font = font(o, 800, 46, 'head'); const tw = ctx.measureText(url).width + 80;
    fillRR(ctx, px + pw / 2 - tw / 2, area.y + 250, tw, 92, 46, C.navy); ctx.fillStyle = '#FFFFFF'; ctx.textAlign = 'center'; ctx.fillText(url, px + pw / 2, area.y + 312);
    ctx.font = font(o, 700, 44, 'hand'); ctx.fillStyle = C.blue; ctx.fillText('Raise It With Press Release', px + pw / 2, area.y + 410); ctx.textAlign = 'left';
    ctx.restore();
  } else { // icon
    const names = (ill.icons && ill.icons.length ? ill.icons : [ill.icon || 'news']).slice(0, 3);
    names.forEach((nm, i) => {
      const im = assets.icons[nm] || assets.icons.news; const a = easeBack(k(i * 0.3)); if (!im || a <= 0) return;
      const sz = names.length === 1 ? 260 : 190; const gap = names.length === 1 ? 0 : 250;
      const x = px + pw / 2 - sz / 2 + (i - (names.length - 1) / 2) * gap, y = area.y + 10 + Math.sin(lt * 2 + i) * 10;
      ctx.save(); ctx.globalAlpha *= clamp(a, 0, 1); ctx.translate(x + sz / 2, y + sz / 2); ctx.scale(a, a); ctx.rotate(Math.sin(lt * 1.5 + i) * 0.05);
      fillRR(ctx, -sz / 2 - 18, -sz / 2 - 18, sz + 36, sz + 36, 48, C.pale); ctx.drawImage(im, -sz / 2, -sz / 2, sz, sz); ctx.restore();
    });
    if (ill.label) richText(ctx, ill.label, px + pw / 2, area.y + (names.length === 1 ? 300 : 250), pw - 140, 46, o, {color: C.navy, hl: C.blue, weight: 700, maxLines: 2});
  }
  ctx.restore();
}

// ---------- overlays ----------
function drawTop(ctx, assets, idx, n, lt, dur) {
  // progress segments
  const x0 = 70, w = 940, gap = 10, sw = (w - gap * (n - 1)) / n;
  for (let i = 0; i < n; i++) {
    fillRR(ctx, x0 + i * (sw + gap), 70, sw, 10, 5, 'rgba(7,27,110,.18)');
    const f = i < idx ? 1 : i === idx ? clamp(lt / dur, 0, 1) : 0;
    if (f > 0) fillRR(ctx, x0 + i * (sw + gap), 70, sw * f, 10, 5, C.blue);
  }
  if (assets.logoColor) { const s = 0.55; const im = assets.logoColor; /* small mark top-left handled by panel */ }
}
function drawSubtitle(ctx, scene, lt, dur, o) {
  const words = String(scene.vo || '').replace(/[*[\]]/g, '').split(/\s+/).filter(Boolean);
  if (!words.length) return;
  const per = o.lang === 'th' ? 1 : 6;
  let chunks = [];
  if (o.lang === 'th') { const txt = words.join(' '); for (let i = 0; i < txt.length; i += 26) chunks.push(txt.slice(i, i + 26)); }
  else for (let i = 0; i < words.length; i += per) chunks.push(words.slice(i, i + per).join(' '));
  const speak = Math.max(0.5, dur - 0.4); const ci = clamp(Math.floor(lt / speak * chunks.length), 0, chunks.length - 1);
  const text = chunks[ci];
  ctx.font = font(o, 800, 50, 'head'); const tw = Math.min(980, ctx.measureText(text).width + 70);
  const y = 1300;
  fillRR(ctx, 540 - tw / 2, y, tw, 90, 30, 'rgba(7,27,110,.88)');
  ctx.fillStyle = '#FFFFFF'; ctx.textAlign = 'center'; ctx.fillText(text, 540, y + 63, 940); ctx.textAlign = 'left';
}
function drawLowerThird(ctx, lt, o) {
  if (lt > 3.4) return;
  const a = lt < 0.5 ? easeOut(lt / 0.5) : lt > 2.9 ? 1 - easeOut((lt - 2.9) / 0.5) : 1;
  const x = lerp(-520, 60, a), y = o.lowerY || 1170;
  fillRR(ctx, x, y, 480, 96, 22, '#FFFFFF');
  fillRR(ctx, x, y, 16, 96, 8, C.blue);
  ctx.fillStyle = C.navy; ctx.font = font(o, 800, 34, 'head'); ctx.fillText(o.roleTitle || 'PR Specialist', x + 40, y + 44);
  ctx.fillStyle = C.blue; ctx.font = font(o, 600, 26, 'body'); ctx.fillText('VRITIMES · ' + (o.countryName || ''), x + 40, y + 78);
}

// ======================= STAGE STYLE (default) =======================
// Navy stage with spotlights, 3D toon presenter, top label card, karaoke captions, badges, section pill, white cards.
// VRITIMES palette: navy #071B6E, blue #0058F8, mid #0098F8, cyan #00C8F8, lime #D7F23C, pale #E8F1FF
const S2 = {gold: '#D7F23C', goldD: '#9DB81A', red: '#E5484D', green: '#0058F8', cream: '#F4F8FF', navyBg: '#071B6E', navyD: '#040F45'};
function stageBg(ctx, t) {
  const g = ctx.createLinearGradient(0, 0, 0, H); g.addColorStop(0, '#0B3AB8'); g.addColorStop(0.3, '#0A2C93'); g.addColorStop(0.52, '#071B6E'); g.addColorStop(1, '#030B33');
  ctx.fillStyle = g; ctx.fillRect(0, 0, W, H);
  // spotlight rays from the top centre
  ctx.save(); ctx.globalCompositeOperation = 'lighter';
  const n = 14;
  for (let i = 0; i < n; i++) {
    const a = -Math.PI / 2 + (i - (n - 1) / 2) * 0.17 + Math.sin(t * 0.35 + i) * 0.01;
    const len = 1400; const w = 0.035;
    ctx.beginPath(); ctx.moveTo(540, -40);
    ctx.lineTo(540 + Math.cos(a - w) * -len * 0 + Math.sin(a - w + Math.PI / 2) * 0, -40);
    const x1 = 540 + Math.tan((i - (n - 1) / 2) * 0.17 - w) * len, x2 = 540 + Math.tan((i - (n - 1) / 2) * 0.17 + w) * len;
    ctx.lineTo(x2, len); ctx.lineTo(x1, len); ctx.closePath();
    const rg = ctx.createLinearGradient(0, 0, 0, len); rg.addColorStop(0, 'rgba(0,200,248,0.16)'); rg.addColorStop(1, 'rgba(0,200,248,0)');
    ctx.fillStyle = rg; ctx.fill();
  }
  ctx.restore();
  // faint screens row
  ctx.strokeStyle = 'rgba(0,200,248,0.20)'; ctx.lineWidth = 3;
  for (let i = -1; i < 7; i++) { rr(ctx, 30 + i * 175, 560, 140, 190, 14); ctx.stroke(); }
  // floor + gold edge
  const fl = ctx.createLinearGradient(0, 1020, 0, H); fl.addColorStop(0, '#081F7A'); fl.addColorStop(1, '#030B33');
  ctx.fillStyle = fl; ctx.fillRect(0, 1020, W, H - 1020);
  ctx.fillStyle = C.lime; ctx.fillRect(0, 1014, W, 9);
  const sh = ctx.createLinearGradient(0, 1023, 0, 1110); sh.addColorStop(0, 'rgba(0,0,0,.35)'); sh.addColorStop(1, 'rgba(0,0,0,0)'); ctx.fillStyle = sh; ctx.fillRect(0, 1023, W, 90);
  // vignette
  const vg = ctx.createRadialGradient(540, 900, 300, 540, 900, 1250); vg.addColorStop(0, 'rgba(0,0,0,0)'); vg.addColorStop(1, 'rgba(0,0,0,.45)'); ctx.fillStyle = vg; ctx.fillRect(0, 0, W, H);
}
function ball(ctx, x, y, r, base, light, dark) {
  const g = ctx.createRadialGradient(x - r * 0.35, y - r * 0.4, r * 0.1, x, y, r * 1.05);
  g.addColorStop(0, light); g.addColorStop(0.55, base); g.addColorStop(1, dark);
  ctx.fillStyle = g; ctx.beginPath(); ctx.arc(x, y, r, 0, Math.PI * 2); ctx.fill();
}
const TOON = {skin: '#E2A882', skinL: '#F6CCAE', skinD: '#B97A57', shirt: '#B9D3FF', stripe: '#E8F1FF', hair: '#2A1C17', hairL: '#4A3328'};
function toon(ctx, t, o) {
  // o: {x, y, s, talk, gesture, gt (gesture local time), fingers, female}
  const s = o.s || 1; ctx.save(); ctx.translate(o.x, o.y); ctx.scale(s, s);
  const bob = Math.sin(t * 2.3) * 6 + (o.talk ? Math.sin(t * 7.1) * 2 : 0);
  const sway = Math.sin(t * 0.8) * 0.02;
  // body (striped shirt)
  ctx.save(); ctx.translate(0, bob * 0.3);
  ctx.beginPath(); ctx.moveTo(-250, 1300); ctx.lineTo(-250, 360); ctx.quadraticCurveTo(-250, 250, -130, 235); ctx.lineTo(130, 235); ctx.quadraticCurveTo(250, 250, 250, 360); ctx.lineTo(250, 1700); ctx.closePath();
  const bg = ctx.createLinearGradient(-250, 0, 250, 0); bg.addColorStop(0, '#94B8F5'); bg.addColorStop(0.5, TOON.shirt); bg.addColorStop(1, '#88AEF0');
  ctx.fillStyle = bg; ctx.fill();
  ctx.save(); ctx.clip(); ctx.strokeStyle = 'rgba(255,255,255,.55)'; ctx.lineWidth = 7;
  for (let x = -240; x <= 240; x += 30) { ctx.beginPath(); ctx.moveTo(x, 240); ctx.lineTo(x, 1700); ctx.stroke(); }
  ctx.restore();
  // collar / neck
  ball(ctx, 0, 215, 58, TOON.skin, TOON.skinL, TOON.skinD);
  ctx.fillStyle = 'rgba(0,0,0,.12)'; ctx.beginPath(); ctx.ellipse(0, 248, 70, 16, 0, 0, Math.PI * 2); ctx.fill();
  if (!o.female) { ctx.fillStyle = '#FFFFFF'; ctx.beginPath(); ctx.moveTo(-70, 236); ctx.lineTo(0, 280); ctx.lineTo(-30, 300); ctx.closePath(); ctx.fill(); ctx.beginPath(); ctx.moveTo(70, 236); ctx.lineTo(0, 280); ctx.lineTo(30, 300); ctx.closePath(); ctx.fill(); }
  ctx.restore();
  // head
  ctx.save(); ctx.translate(0, bob); ctx.rotate(sway + (o.gesture === 'surprise' ? Math.sin(t * 9) * 0.01 : 0));
  if (o.female) { // long hair behind
    const hg = ctx.createLinearGradient(0, -260, 0, 160); hg.addColorStop(0, TOON.hairL); hg.addColorStop(1, TOON.hair);
    ctx.fillStyle = hg; rr(ctx, -205, -190, 410, 380, 120); ctx.fill();
  }
  ball(ctx, -178, 10, 40, TOON.skin, TOON.skinL, TOON.skinD); ball(ctx, 178, 10, 40, TOON.skin, TOON.skinL, TOON.skinD);
  ball(ctx, 0, 0, 180, TOON.skin, TOON.skinL, TOON.skinD);
  // hair cap
  const hg2 = ctx.createLinearGradient(-60, -200, 60, -40); hg2.addColorStop(0, TOON.hairL); hg2.addColorStop(1, TOON.hair);
  ctx.fillStyle = hg2; ctx.beginPath();
  if (o.female) { ctx.arc(0, -10, 188, Math.PI * 1.02, Math.PI * 1.98); ctx.quadraticCurveTo(120, -110, 10, -120); ctx.quadraticCurveTo(-120, -120, -186, -30); }
  else { ctx.arc(0, -4, 192, Math.PI * 1.0, Math.PI * 2.0); ctx.quadraticCurveTo(175, -60, 120, -88); ctx.quadraticCurveTo(40, -70, -20, -96); ctx.quadraticCurveTo(-110, -82, -150, -50); ctx.quadraticCurveTo(-175, -30, -192, -4); }
  ctx.closePath(); ctx.fill();
  ctx.fillStyle = 'rgba(255,255,255,.12)'; ctx.beginPath(); ctx.ellipse(-50, -150, 70, 22, -0.3, 0, Math.PI * 2); ctx.fill();
  // brows
  const raise = o.gesture === 'surprise' ? 14 : o.talk ? Math.max(0, Math.sin(t * 2.4)) * 6 : 0;
  ctx.strokeStyle = TOON.hair; ctx.lineWidth = 12; ctx.lineCap = 'round';
  ctx.beginPath(); ctx.moveTo(-95, -70 - raise); ctx.quadraticCurveTo(-65, -84 - raise, -35, -74 - raise); ctx.stroke();
  ctx.beginPath(); ctx.moveTo(35, -76 - raise * 0.6); ctx.quadraticCurveTo(65, -86 - raise * 0.6, 95, -72 - raise * 0.6); ctx.stroke();
  // eyes
  const bl = (t % 3.3) < 0.11 ? 0.15 : 1;
  const ey = o.gesture === 'surprise' ? 1.12 : 1;
  [-62, 62].forEach((ex) => {
    ctx.fillStyle = '#111'; ctx.beginPath(); ctx.ellipse(ex, -22, 19 * ey, 27 * bl * ey, 0, 0, Math.PI * 2); ctx.fill();
    if (bl > 0.5) { ctx.fillStyle = '#fff'; ctx.beginPath(); ctx.arc(ex - 6, -32, 6, 0, Math.PI * 2); ctx.fill(); }
  });
  // nose
  ball(ctx, 0, 36, 24, '#D9946D', '#F2B693', '#B57452');
  // cheeks
  ctx.fillStyle = 'rgba(240,120,110,.18)'; ctx.beginPath(); ctx.ellipse(-110, 50, 30, 18, 0, 0, Math.PI * 2); ctx.ellipse(110, 50, 30, 18, 0, 0, Math.PI * 2); ctx.fill();
  // mouth
  const open = o.talk ? clamp(0.2 + 0.8 * Math.abs(Math.sin(t * 11)) * (0.5 + 0.5 * Math.abs(noise(t * 3, 2))), 0, 1) : (o.gesture === 'surprise' ? 0.8 : 0);
  if (open > 0.15) {
    ctx.fillStyle = '#7A1E22'; ctx.beginPath(); ctx.ellipse(0, 102, 40, 12 + open * 30, 0, 0, Math.PI * 2); ctx.fill();
    ctx.fillStyle = '#E8616A'; ctx.beginPath(); ctx.ellipse(0, 112 + open * 12, 24, 8 + open * 7, 0, 0, Math.PI * 2); ctx.fill();
    ctx.fillStyle = '#fff'; rr(ctx, -22, 92 - open * 16, 44, 10, 4); ctx.fill();
  } else {
    ctx.strokeStyle = '#7A2A22'; ctx.lineWidth = 9; ctx.beginPath(); ctx.moveTo(-50, 96); ctx.quadraticCurveTo(0, 138, 50, 96); ctx.stroke();
  }
  ctx.restore();
  // arms / hands
  const g = o.gesture || 'explain', gt = o.gt || 0;
  const up = (g === 'count' || g === 'point') ? easeBack(gt / 0.5) : g === 'explain' ? 0.35 + Math.sin(t * 2.2) * 0.12 : 0;
  // left hand resting
  ball(ctx, -262, 640 + Math.sin(t * 2) * 4, 48, TOON.skin, TOON.skinL, TOON.skinD);
  // right arm
  if (up > 0.05) {
    const hx = 270, hy = lerp(640, 330, clamp(up, 0, 1.1));
    ctx.strokeStyle = TOON.shirt; ctx.lineWidth = 92; ctx.lineCap = 'round';
    ctx.beginPath(); ctx.moveTo(215, 420); ctx.quadraticCurveTo(300, 560, hx, hy + 60); ctx.stroke();
    ctx.strokeStyle = 'rgba(255,255,255,.4)'; ctx.lineWidth = 6; for (let k = -30; k <= 30; k += 30) { ctx.beginPath(); ctx.moveTo(215 + k, 420); ctx.quadraticCurveTo(300 + k, 560, hx + k, hy + 60); ctx.stroke(); }
    const fingers = g === 'count' ? clamp(o.fingers || 3, 1, 5) : g === 'point' ? 1 : 0;
    ctx.fillStyle = TOON.skin;
    for (let f = 0; f < fingers; f++) { const fx = hx - (fingers - 1) * 15 + f * 30; rr(ctx, fx - 13, hy - 120 + Math.abs(f - (fingers - 1) / 2) * 10, 26, 100, 13); ctx.fill(); }
    ball(ctx, hx, hy, 52, TOON.skin, TOON.skinL, TOON.skinD);
  } else ball(ctx, 262, 640 + Math.sin(t * 2 + 1) * 4, 48, TOON.skin, TOON.skinL, TOON.skinD);
  ctx.restore();
}
function topCard(ctx, card, lt, o) {
  if (!card || !(card.text || card.tag)) return;
  const a = easeBack(lt / 0.5); if (a <= 0) return;
  const x = 40, y = 255, w = 900;
  ctx.save(); ctx.globalAlpha = clamp(a, 0, 1); ctx.translate(0, (1 - a) * -40);
  ctx.save(); ctx.translate(x + w / 2, y); ctx.rotate(-0.012);
  const fake = document.createElement ? null : null;
  // measure height
  ctx.font = font(o, 800, 54, 'head');
  const h = 210;
  ctx.fillStyle = 'rgba(0,0,0,.28)'; rr(ctx, -w / 2 + 8, 14, w, h, 22); ctx.fill();
  fillRR(ctx, -w / 2, 0, w, h, 22, S2.cream);
  const tagC = {red: C.navy, green: C.blue, blue: C.blue, navy: C.navy, cyan: '#0098F8', gold: C.navy, lime: C.navy}[card.tagColor || 'blue'] || C.blue;
  if (card.tag) {
    ctx.font = font(o, 800, 34, 'head'); const tw = ctx.measureText(String(card.tag).toUpperCase()).width + 44;
    fillRR(ctx, -w / 2 + 26, -30, tw, 58, 12, tagC);
    ctx.fillStyle = '#fff'; ctx.fillText(String(card.tag).toUpperCase(), -w / 2 + 48, 10);
  }
  richText(ctx, card.text || '', -w / 2 + 34, 40, w - 70, 56, o, {align: 'left', color: C.navy, hl: C.blue, weight: 800, maxLines: 2, lh: 1.15, alt: '#0098F8', altBox: C.lime});
  ctx.restore(); ctx.restore();
}
function sectionPill(ctx, sec, lt, o) {
  if (!sec || !sec.text) return;
  const a = easeBack(lt / 0.45); if (a <= 0) return;
  ctx.save(); ctx.globalAlpha = clamp(a, 0, 1); ctx.translate(540, 300); ctx.scale(lerp(0.7, 1, a), lerp(0.7, 1, a));
  ctx.font = font(o, 800, 56, 'head'); const tw = ctx.measureText(String(sec.text).toUpperCase()).width;
  const w = tw + 220, h = 112;
  ctx.fillStyle = 'rgba(0,0,0,.3)'; rr(ctx, -w / 2 + 6, -h / 2 + 10, w, h, 56); ctx.fill();
  const g = ctx.createLinearGradient(0, -h / 2, 0, h / 2); g.addColorStop(0, '#2A7BFF'); g.addColorStop(1, '#0058F8');
  rr(ctx, -w / 2, -h / 2, w, h, 56); ctx.fillStyle = g; ctx.fill();
  ball(ctx, -w / 2 + 66, 0, 40, '#F2F4F8', '#FFFFFF', '#B8C2D6');
  ctx.fillStyle = C.navy; ctx.font = font(o, 800, 48, 'head'); ctx.textAlign = 'center'; ctx.fillText(String(sec.n || 1), -w / 2 + 66, 17);
  ctx.fillStyle = '#fff'; ctx.font = font(o, 800, 56, 'head'); ctx.fillText(String(sec.text).toUpperCase(), 50, 20); ctx.textAlign = 'left';
  ctx.restore();
}
function badge(ctx, b, lt, o) {
  if (!b || !(b.text || b.big)) return;
  const a = easeBack((lt - 0.35) / 0.5); if (a <= 0) return;
  ctx.save(); ctx.globalAlpha = clamp(a, 0, 1);
  if (b.type === 'coin' || (b.big && b.type !== 'pill')) {
    const x = o.badgeY ? 830 : 760, y = (o.badgeY ? o.badgeY + 40 : 560) + Math.sin(lt * 2) * 8, r = o.badgeY ? 110 : 128;
    ctx.translate(x, y); ctx.scale(a, a); ctx.rotate(Math.sin(lt * 1.5) * 0.05);
    ctx.fillStyle = 'rgba(0,0,0,.3)'; ctx.beginPath(); ctx.arc(8, 14, r, 0, Math.PI * 2); ctx.fill();
    ball(ctx, 0, 0, r, '#D7F23C', '#F1FFA3', '#9DB81A');
    ctx.strokeStyle = 'rgba(255,255,255,.35)'; ctx.lineWidth = 6; ctx.beginPath(); ctx.arc(0, 0, r - 14, 0, Math.PI * 2); ctx.stroke();
    ctx.fillStyle = C.navy; ctx.textAlign = 'center';
    ctx.font = font(o, 800, b.small ? 130 : 150, 'head'); ctx.fillText(String(b.big || b.text), 0, b.small ? 36 : 50);
    if (b.small) { ctx.font = font(o, 800, 30, 'head'); ctx.fillText(String(b.small).toUpperCase(), 0, 84); }
    ctx.textAlign = 'left';
  } else {
    const txt = String(b.text).toUpperCase(); ctx.font = font(o, 800, 62, 'head'); const tw = ctx.measureText(txt).width;
    const w = tw + 130, h = 116; const x = 940 - w, y = o.badgeY || 600;
    ctx.translate(x + w / 2, y + h / 2); ctx.rotate(-0.07); ctx.scale(a, a);
    const col = {red: C.lime, lime: C.lime, blue: C.blue, cyan: '#0098F8', navy: C.navy, green: C.blue, gold: C.lime}[b.color || 'lime'] || C.lime;
    const fg = col === C.lime ? C.navy : '#fff';
    ctx.fillStyle = 'rgba(0,0,0,.3)'; rr(ctx, -w / 2 + 8, -h / 2 + 12, w, h, 20); ctx.fill();
    fillRR(ctx, -w / 2, -h / 2, w, h, 20, col);
    const pulse = 0.6 + 0.4 * Math.abs(Math.sin(lt * 4));
    ctx.globalAlpha *= pulse; ctx.fillStyle = fg; ctx.beginPath(); ctx.arc(-w / 2 + 50, 0, 15, 0, Math.PI * 2); ctx.fill(); ctx.globalAlpha /= pulse;
    ctx.fillStyle = fg; ctx.fillText(txt, -w / 2 + 88, 22);
  }
  ctx.restore();
}
/** karaoke caption: chunk of words, spoken words bright, upcoming dim, keywords gold */
function karaoke(ctx, scene, lt, dur, o) {
  const raw = String(scene.vo || '').replace(/[*[\]]/g, '').trim(); if (!raw) return;
  const words = raw.split(/\s+/);
  const keys = new Set((scene.keywords || []).concat(((scene.onscreen || '') + ' ' + ((scene.card || {}).text || '')).match(/\*([^*]+)\*|\[([^\]]+)\]/g) || []).flatMap((k) => String(k).replace(/[*[\]]/g, '').split(/\s+/)).map((k) => k.toLowerCase().replace(/[^\p{L}\p{N}]/gu, '')).filter(Boolean));
  // word timings: real ones from TTS when present, else spread by length
  let times = scene._words && scene._words.length === words.length ? scene._words : null;
  if (!times) {
    const speak = Math.max(0.6, dur - 0.35); const tot = words.reduce((s, w) => s + w.length + 2, 0); let acc = 0.1;
    times = words.map((w) => { const d = speak * (w.length + 2) / tot; const r = {start: acc, end: acc + d}; acc += d; return r; });
  }
  let cur = 0; for (let i = 0; i < times.length; i++) if (lt >= times[i].start) cur = i;
  // chunks of max ~22 chars per line, 2 lines
  ctx.font = font(o, 800, 86, 'head');
  const chunks = []; let line = [], lines = [], width = 0; const maxW = 860;
  words.forEach((w, i) => {
    const ww = ctx.measureText(w.toUpperCase() + ' ').width;
    if (width + ww > maxW && line.length) { lines.push(line); line = []; width = 0; if (lines.length === 2) { chunks.push(lines); lines = []; } }
    line.push(i); width += ww;
  });
  if (line.length) lines.push(line); if (lines.length) chunks.push(lines);
  const ci = chunks.findIndex((c) => c.flat().includes(cur)); const chunk = chunks[Math.max(0, ci)];
  const y0 = o.capY || 1150;
  chunk.forEach((ln, li) => {
    const big = 86;
    ctx.font = font(o, 800, big, 'head');
    const lw = ln.reduce((s, i) => s + ctx.measureText(words[i].toUpperCase() + ' ').width, 0);
    let x = 540 - lw / 2; const y = y0 + li * 104;
    ln.forEach((i) => {
      const w = words[i].toUpperCase(); const ww = ctx.measureText(w + ' ').width;
      const spoken = i <= cur; const isKey = keys.has(words[i].toLowerCase().replace(/[^\p{L}\p{N}]/gu, ''));
      const pop = i === cur ? easeBack(clamp((lt - times[i].start) / 0.18, 0, 1)) : 1;
      ctx.save(); ctx.translate(x, y); if (i === cur) ctx.scale(1 + (1 - pop) * 0.08, 1 + (1 - pop) * 0.08);
      ctx.lineJoin = 'round'; ctx.lineWidth = 14; ctx.strokeStyle = 'rgba(0,0,0,.55)'; ctx.strokeText(w, 0, 0);
      ctx.fillStyle = isKey ? (spoken ? C.lime : 'rgba(215,242,60,.45)') : (spoken ? '#FFFFFF' : 'rgba(255,255,255,.45)');
      ctx.fillText(w, 0, 0); ctx.restore();
      x += ww;
    });
  });
}
function whiteCard(ctx, scene, lt, dur, assets, o) {
  const ill = scene.illus || {}; const T = ill.type;
  if (!T || T === 'none' || T === 'character') return false;
  const a = easeBack((lt - 0.1) / 0.5); const k = (d) => clamp((lt - 0.35 - d) / 0.4, 0, 1);
  const top = (scene.card && (scene.card.text || scene.card.tag)) ? 480 : (scene.section && scene.section.text) ? 390 : 300;
  const x = 90, w = 900;
  const nItems = (ill.items || ill.messages || ill.bars || []).length;
  const h0 = T === 'doc' ? 640 : T === 'grid' ? Math.min(640, 200 + Math.ceil(Math.max(nItems, 1) / (ill.cols || (nItems > 9 ? 4 : 3))) * 118) : ['list', 'steps'].includes(T) ? Math.min(640, 150 + nItems * 120) : ['chat'].includes(T) ? Math.min(640, 160 + nItems * 106) : 560;
  const h = o.maxBottom ? Math.max(260, Math.min(h0, o.maxBottom - top)) : h0;
  ctx.save(); ctx.globalAlpha = clamp(a, 0, 1); ctx.translate(540, top + h / 2); ctx.rotate(T === 'doc' ? -0.02 : 0); ctx.scale(lerp(0.85, 1, a), lerp(0.85, 1, a)); ctx.translate(-540, -(top + h / 2));
  if (T === 'doc') {
    if (h < 640) { const k2 = h / 640; ctx.translate(540, top); ctx.scale(k2, k2); ctx.translate(-540, -top); }
    ctx.fillStyle = 'rgba(0,0,0,.35)'; rr(ctx, x + 50 + 10, top + 18, w - 100, 640, 16); ctx.fill();
    fillRR(ctx, x + 50, top, w - 100, 640, 16, '#FFFFFF');
    ctx.save(); rr(ctx, x + 50, top, w - 100, 640, 16); ctx.clip(); ctx.fillStyle = C.navy; ctx.fillRect(x + 50, top, w - 100, 150); ctx.restore();
    ctx.textAlign = 'center'; ctx.fillStyle = '#fff'; ctx.font = font(o, 800, 48, 'head'); ctx.fillText(String(ill.header || 'DOKUMEN').toUpperCase(), 540, top + 72);
    ctx.fillStyle = C.lime; ctx.font = font(o, 700, 28, 'head'); ctx.fillText(String(ill.sub || '').toUpperCase(), 540, top + 118);
    ctx.fillStyle = C.navy; ctx.font = font(o, 800, 56, 'head'); ctx.fillText(String(ill.number || ''), 540, top + 240);
    ctx.fillStyle = '#6B7280'; ctx.font = font(o, 500, 30, 'body'); ctx.fillText(String(ill.about || 'tentang'), 540, top + 300);
    ctx.textAlign = 'left';
    richText(ctx, String(ill.title || ''), 540, top + 320, w - 220, 52, o, {color: C.navy, hl: C.blue, weight: 800, maxLines: 2});
    ctx.textAlign = 'left';
    for (let i = 0; i < 4; i++) { const p = easeOut(k(0.2 + i * 0.12)); fillRR(ctx, x + 150, top + 470 + i * 40, (w - 300) * (i === 3 ? 0.6 : 1) * p, 14, 7, '#D6E3FB'); }
  } else {
    ctx.fillStyle = 'rgba(0,0,0,.35)'; rr(ctx, x + 10, top + 18, w, h, 22); ctx.fill();
    fillRR(ctx, x, top, w, h, 22, S2.cream);
    let y = top + 30;
    if (ill.title) { ctx.textAlign = 'center'; ctx.fillStyle = C.navy; ctx.font = font(o, 800, 46, 'head'); ctx.fillText(String(ill.title).toUpperCase(), 540, y + 44); y += 60; if (ill.sub) { ctx.fillStyle = '#6B7280'; ctx.font = font(o, 600, 30, 'body'); ctx.fillText(String(ill.sub), 540, y + 30); y += 44; } ctx.textAlign = 'left'; y += 20; }
    const area = {x: x + 50, y, w: w - 100, h: top + h - 40 - y};
    if (T === 'grid') {
      const items = (ill.items || []).slice(0, 16); const cols = ill.cols || (items.length > 9 ? 4 : 3); const rows = Math.ceil(items.length / cols);
      const gw = area.w / cols, gh = Math.min(118, area.h / Math.max(rows, 1));
      const off = new Set((ill.off || []).map(Number));
      items.forEach((it, i) => {
        const p = easeBack(k(i * 0.06)); if (p <= 0) return;
        const cx = area.x + (i % cols) * gw + gw / 2, cy = area.y + Math.floor(i / cols) * gh + gh / 2;
        const isOff = off.has(i + 1) && lt > (ill.offAt || 1.6);
        ctx.save(); ctx.translate(cx, cy); ctx.scale(p, p);
        fillRR(ctx, -gw / 2 + 10, -gh / 2 + 8, gw - 20, gh - 16, 14, isOff ? '#FDE7E8' : C.pale);
        ctx.strokeStyle = isOff ? S2.red : C.blue; ctx.lineWidth = 5; rr(ctx, -gw / 2 + 10, -gh / 2 + 8, gw - 20, gh - 16, 14); ctx.stroke();
        ctx.fillStyle = isOff ? '#B4232A' : C.navy; ctx.font = font(o, 700, 32, 'head'); ctx.textAlign = 'center'; ctx.fillText(String(it), 0, 11);
        if (isOff) { ctx.strokeStyle = S2.red; ctx.lineWidth = 6; ctx.beginPath(); ctx.moveTo(-gw / 2 + 24, gh / 2 - 22); ctx.lineTo(gw / 2 - 24, -gh / 2 + 22); ctx.stroke(); }
        ctx.textAlign = 'left'; ctx.restore();
      });
    } else if (T === 'repost') {
      // handled separately
    } else {
      // reuse studio illustrations inside the cream card
      ctx.restore(); ctx.save(); ctx.globalAlpha = clamp(a, 0, 1);
      const sc = Object.assign({}, scene, {onscreen: ill.title ? '' : (scene.onscreen || '')});
      drawPanelIn(ctx, sc, lt, dur, assets, o, {px: x, py: top, pw: w, ph: h, bg: S2.cream});
    }
  }
  ctx.restore();
  return true;
}
function repostEnd(ctx, scene, lt, o) {
  const ill = scene.illus || {};
  topCard(ctx, {tag: ill.tag || 'BANTU SEBARKAN', tagColor: 'blue', text: ill.text || '*Repost* biar temanmu tahu'}, lt, o);
  const a = easeBack((lt - 0.25) / 0.6); if (a <= 0) return;
  ctx.save(); ctx.translate(540, 760); ctx.scale(a, a); ctx.rotate(Math.sin(lt * 2) * 0.03);
  ctx.fillStyle = 'rgba(0,0,0,.35)'; ctx.beginPath(); ctx.arc(10, 18, 190, 0, Math.PI * 2); ctx.fill();
  ball(ctx, 0, 0, 190, '#0058F8', '#3FA0FF', '#05329A');
  ctx.strokeStyle = '#fff'; ctx.lineWidth = 34; ctx.lineCap = 'round';
  const sp = lt * 1.2;
  ctx.beginPath(); ctx.arc(0, 0, 95, Math.PI * 1.05 + sp, Math.PI * 1.85 + sp); ctx.stroke();
  ctx.beginPath(); ctx.arc(0, 0, 95, Math.PI * 0.05 + sp, Math.PI * 0.85 + sp); ctx.stroke();
  const arrow = (ang) => { const ax = Math.cos(ang) * 95, ay = Math.sin(ang) * 95; ctx.save(); ctx.translate(ax, ay); ctx.rotate(ang + Math.PI / 2); ctx.fillStyle = '#fff'; ctx.beginPath(); ctx.moveTo(-40, -6); ctx.lineTo(30, 0); ctx.lineTo(-40, 6 + 50); ctx.closePath(); ctx.restore(); };
  [Math.PI * 1.85 + sp, Math.PI * 0.85 + sp].forEach((ang) => { const ax = Math.cos(ang) * 95, ay = Math.sin(ang) * 95; ctx.save(); ctx.translate(ax, ay); ctx.rotate(ang + Math.PI / 2); ctx.fillStyle = '#fff'; ctx.beginPath(); ctx.moveTo(-38, 10); ctx.lineTo(38, 10); ctx.lineTo(0, -40); ctx.closePath(); ctx.fill(); ctx.restore(); });
  ctx.restore();
  ctx.save(); ctx.globalAlpha = clamp(a, 0, 1); ctx.fillStyle = '#fff'; ctx.font = font(o, 800, 96, 'head'); ctx.textAlign = 'center';
  ctx.lineWidth = 12; ctx.strokeStyle = 'rgba(0,0,0,.5)'; ctx.strokeText(String(ill.label || 'REPOST'), 540, 1060); ctx.fillText(String(ill.label || 'REPOST'), 540, 1060); ctx.textAlign = 'left'; ctx.restore();
}
function stageWatermark(ctx, assets) {
  const im = assets.besideWhite || assets.logoWhite; if (!im) return;
  const w = 220, h = im.height * (w / im.width); ctx.save(); ctx.globalAlpha = 0.85; ctx.drawImage(im, 540 - w / 2, 1560, w, h); ctx.restore();
}
// ---------- cutaway scenes: full-screen visuals away from the studio, presenter stays in a corner bubble ----------
const CUTS = ['phone', 'inbox', 'newspaper', 'search', 'tv', 'timeline', 'network'];
function wrapText(ctx, text, maxW, maxLines) {
  const words = String(text || '').replace(/[*[\]]/g, '').split(/\s+/).filter(Boolean); const lines = []; let cur = '';
  words.forEach((w) => { const tr = cur ? cur + ' ' + w : w; if (ctx.measureText(tr).width > maxW && cur) { lines.push(cur); cur = w; } else cur = tr; });
  if (cur) lines.push(cur);
  if (lines.length > maxLines) { lines.length = maxLines; let l = lines[maxLines - 1]; while (ctx.measureText(l + '…').width > maxW && l.length > 1) l = l.slice(0, -1); lines[maxLines - 1] = l + '…'; }
  return lines;
}
function cutBg(ctx, t, dark) {
  const g = ctx.createLinearGradient(0, 0, W * 0.4, H);
  if (dark) { g.addColorStop(0, '#0B2A9A'); g.addColorStop(0.6, C.navy); g.addColorStop(1, '#040F45'); }
  else { g.addColorStop(0, '#EEF4FF'); g.addColorStop(1, '#CFDDF6'); }
  ctx.fillStyle = g; ctx.fillRect(0, 0, W, H);
  ctx.fillStyle = dark ? 'rgba(255,255,255,.07)' : 'rgba(0,88,248,.08)';
  for (let y = 40; y < H; y += 60) for (let x = 30 + ((y / 60) % 2) * 30; x < W; x += 60) { ctx.beginPath(); ctx.arc(x, y + Math.sin(t * 0.6 + x * 0.01) * 3, 3, 0, Math.PI * 2); ctx.fill(); }
  const rg = ctx.createRadialGradient(540, 860, 40, 540, 860, 760); rg.addColorStop(0, dark ? 'rgba(0,200,248,.22)' : 'rgba(255,255,255,.7)'); rg.addColorStop(1, 'rgba(0,0,0,0)');
  ctx.fillStyle = rg; ctx.fillRect(0, 0, W, H);
}
function presenterBubble(ctx, t, talk, gest, lt) {
  const a = easeBack((lt - 0.15) / 0.5); if (a <= 0) return;
  const cx = 920, cy = 1730, r = 118;
  ctx.save(); ctx.translate(cx, cy); ctx.scale(a, a); ctx.translate(-cx, -cy);
  ctx.fillStyle = 'rgba(0,0,0,.3)'; ctx.beginPath(); ctx.arc(cx + 6, cy + 10, r + 10, 0, Math.PI * 2); ctx.fill();
  ctx.fillStyle = C.lime; ctx.beginPath(); ctx.arc(cx, cy, r + 10, 0, Math.PI * 2); ctx.fill();
  ctx.save(); ctx.beginPath(); ctx.arc(cx, cy, r, 0, Math.PI * 2); ctx.clip();
  const s = (2 * r) / 560; ctx.translate(cx - 540 * s, cy - 1090 * s); ctx.scale(s, s);
  drawStudio(ctx, t); drawPerson(ctx, t, talk, gest, lt);
  ctx.restore(); ctx.restore();
}
function cutLogo(ctx, assets, dark) {
  const im = assets.besideWhite || assets.logoWhite; if (!im) return;
  const w = 200, h = im.height * (w / im.width);
  ctx.save(); ctx.globalAlpha = 0.92; if (!dark) fillRR(ctx, 44, 1730 - h / 2 - 18, w + 32, h + 36, (h + 36) / 2, C.navy);
  ctx.drawImage(im, 60, 1730 - h / 2, w, h); ctx.restore();
}
function cutDark(T) { return ['tv', 'network', 'timeline'].includes(T); }
function drawCutaway(ctx, scene, lt, dur, assets, o, t, talk) {
  const ill = scene.illus || {}; const T = ill.type; const dark = cutDark(T);
  cutBg(ctx, t, dark);
  const hasTop = (scene.card && (scene.card.text || scene.card.tag)) || (scene.section && scene.section.text);
  const top = hasTop ? 520 : 300, bottom = 1330;
  const k = (d) => clamp((lt - 0.3 - d) / 0.35, 0, 1);
  const enter = easeBack((lt - 0.05) / 0.5);
  ctx.save();
  ctx.textAlign = 'left'; ctx.textBaseline = 'alphabetic';
  if (T === 'phone') {
    const pw = 560, ph = Math.min(820, bottom - top + 40), px = 540 - pw / 2, py = top - 10;
    ctx.translate(0, (1 - enter) * 300); ctx.globalAlpha = clamp(enter, 0, 1);
    ctx.fillStyle = 'rgba(7,27,110,.25)'; rr(ctx, px + 14, py + 24, pw, ph, 70); ctx.fill();
    fillRR(ctx, px, py, pw, ph, 70, '#0E1430'); fillRR(ctx, px + 18, py + 18, pw - 36, ph - 36, 54, C.pale);
    fillRR(ctx, 540 - 70, py + 30, 140, 30, 15, '#0E1430');
    ctx.save(); rr(ctx, px + 18, py + 18, pw - 36, ph - 36, 54); ctx.clip();
    ctx.fillStyle = C.blue; ctx.fillRect(px + 18, py + 18, pw - 36, 150);
    ctx.fillStyle = '#fff'; ctx.font = font(o, 800, 38, 'head'); ctx.fillText(String(ill.title || 'Notifikasi').slice(0, 22), px + 56, py + 140);
    const items = (ill.items || []).slice(0, 5); const ih = Math.min(130, (ph - 230) / Math.max(items.length, 1) - 14);
    items.forEach((it, i) => {
      const p = easeBack(k(i * 0.35)); if (p <= 0) return;
      const y = py + 196 + i * (ih + 14);
      ctx.save(); ctx.translate(0, (1 - p) * -60); ctx.globalAlpha = clamp(p, 0, 1);
      ctx.fillStyle = 'rgba(7,27,110,.12)'; rr(ctx, px + 40, y + 6, pw - 80, ih, 24); ctx.fill();
      fillRR(ctx, px + 36, y, pw - 80, ih, 24, '#FFFFFF');
      ctx.fillStyle = i % 2 ? C.cyan : C.blue; ctx.beginPath(); ctx.arc(px + 88, y + ih / 2, 30, 0, Math.PI * 2); ctx.fill();
      ctx.fillStyle = '#fff'; ctx.font = font(o, 800, 30, 'head'); ctx.textAlign = 'center'; ctx.fillText(String(it).replace(/[*[\]]/g, '').trim().charAt(0).toUpperCase(), px + 88, y + ih / 2 + 11); ctx.textAlign = 'left';
      ctx.fillStyle = C.navy; ctx.font = font(o, 700, 29, 'body'); wrapText(ctx, it, pw - 200, 2).forEach((l, li, arr) => ctx.fillText(l, px + 136, y + ih / 2 + 10 - (arr.length - 1) * 18 + li * 36));
      ctx.restore();
    });
    ctx.restore();
    if (ill.counter) {
      const p = easeBack(k(items.length * 0.35 + 0.1)); if (p > 0) {
        ctx.save(); ctx.translate(px + pw - 10, py + 120); ctx.rotate(0.08); ctx.scale(p, p);
        ctx.font = font(o, 800, 46, 'head'); const tw = ctx.measureText(String(ill.counter)).width + 60;
        ctx.fillStyle = 'rgba(0,0,0,.25)'; rr(ctx, -tw / 2 + 6, -38, tw, 84, 42); ctx.fill();
        fillRR(ctx, -tw / 2, -46, tw, 84, 42, C.lime); ctx.fillStyle = C.navy; ctx.textAlign = 'center'; ctx.fillText(String(ill.counter), 0, 12); ctx.restore();
      }
    }
  } else if (T === 'inbox') {
    const x = 70, w = 940, h = Math.min(bottom - top, 780), y0 = top;
    ctx.translate(0, (1 - enter) * 200); ctx.globalAlpha = clamp(enter, 0, 1);
    ctx.fillStyle = 'rgba(7,27,110,.22)'; rr(ctx, x + 12, y0 + 20, w, h, 28); ctx.fill();
    fillRR(ctx, x, y0, w, h, 28, '#FFFFFF');
    ctx.save(); rr(ctx, x, y0, w, h, 28); ctx.clip(); ctx.fillStyle = C.navy; ctx.fillRect(x, y0, w, 120); ctx.restore();
    ctx.fillStyle = '#fff'; ctx.font = font(o, 800, 42, 'head'); ctx.fillText(String(ill.title || 'Inbox Redaksi').slice(0, 24), x + 40, y0 + 76);
    if (ill.count) {
      const n = parseInt(String(ill.count).replace(/\D/g, ''), 10); const shown = n ? Math.round(n * easeOut((lt - 0.3) / 1.2)) : ill.count;
      const txt = String(shown) + (ill.countLabel ? ' ' + ill.countLabel : ''); ctx.font = font(o, 800, 34, 'head'); const tw = ctx.measureText(txt).width + 44;
      fillRR(ctx, x + w - 40 - tw, y0 + 32, tw, 58, 29, C.lime); ctx.fillStyle = C.navy; ctx.fillText(txt, x + w - 40 - tw + 22, y0 + 73);
    }
    const items = (ill.items || []).slice(0, 6); const rh = Math.min(118, (h - 150) / Math.max(items.length, 1));
    const pick = Number(ill.pick) || 0; const pt = clamp((lt - 0.4 - items.length * 0.25 - 0.3) / 0.4, 0, 1);
    items.forEach((it, i) => {
      const p = easeOut(k(i * 0.25)); if (p <= 0) return;
      const y = y0 + 140 + i * rh; const isPick = pick === i + 1;
      ctx.save(); ctx.globalAlpha = clamp(p, 0, 1) * (pick && !isPick ? 1 - pt * 0.6 : 1); ctx.translate((1 - p) * 120, 0);
      if (isPick && pt > 0) { ctx.translate(540, y + rh / 2); ctx.scale(1 + pt * 0.04, 1 + pt * 0.04); ctx.translate(-540, -(y + rh / 2)); fillRR(ctx, x + 16, y + 4, w - 32, rh - 8, 18, `rgba(215,242,60,${pt})`); }
      ctx.fillStyle = ['#7FA8FF', C.cyan, C.blue, '#9AA4B8'][i % 4]; ctx.beginPath(); ctx.arc(x + 76, y + rh / 2, 30, 0, Math.PI * 2); ctx.fill();
      ctx.fillStyle = C.navy; ctx.font = font(o, isPick ? 800 : 600, 32, 'body'); ctx.fillText(wrapText(ctx, it, w - 260, 1)[0] || '', x + 130, y + rh / 2 - 4);
      fillRR(ctx, x + 130, y + rh / 2 + 16, (w - 300) * (0.5 + (i % 3) * 0.15), 12, 6, '#E3E9F5');
      if (isPick && pt > 0.5) { ctx.strokeStyle = C.blue; ctx.lineWidth = 9; ctx.lineCap = 'round'; ctx.beginPath(); ctx.moveTo(x + w - 96, y + rh / 2); ctx.lineTo(x + w - 78, y + rh / 2 + 18); ctx.lineTo(x + w - 46, y + rh / 2 - 18); ctx.stroke(); }
      ctx.strokeStyle = '#EEF2F9'; ctx.lineWidth = 2; ctx.beginPath(); ctx.moveTo(x + 30, y + rh); ctx.lineTo(x + w - 30, y + rh); ctx.stroke();
      ctx.restore();
    });
  } else if (T === 'newspaper') {
    const w = 860, h = Math.min(bottom - top + 20, 820), x = 540 - w / 2, y0 = top;
    const sp = easeOut((lt - 0.05) / 0.7);
    ctx.translate(540, y0 + h / 2); ctx.rotate(lerp(-0.9, -0.03, sp)); ctx.scale(lerp(0.2, 1, sp), lerp(0.2, 1, sp)); ctx.translate(-540, -(y0 + h / 2)); ctx.globalAlpha = clamp(sp * 1.5, 0, 1);
    ctx.fillStyle = 'rgba(7,27,110,.3)'; ctx.fillRect(x + 16, y0 + 24, w, h);
    ctx.fillStyle = '#FBF8F1'; ctx.fillRect(x, y0, w, h);
    ctx.fillStyle = '#1B1B1B'; ctx.textAlign = 'center'; ctx.font = font(o, 800, 64, 'head'); ctx.fillText(String(ill.name || 'HARIAN BISNIS').toUpperCase().slice(0, 20), 540, y0 + 92);
    ctx.fillRect(x + 40, y0 + 116, w - 80, 5); ctx.fillRect(x + 40, y0 + 166, w - 80, 2);
    ctx.font = font(o, 600, 24, 'body'); ctx.fillStyle = '#555'; ctx.fillText(String(ill.date || 'EDISI HARI INI').toUpperCase(), 540, y0 + 150);
    ctx.textAlign = 'left';
    ctx.fillStyle = '#111'; ctx.font = font(o, 800, 58, 'head');
    const hl = wrapText(ctx, ill.headline || scene.onscreen || '', w - 100, 3); hl.forEach((l, i) => ctx.fillText(l, x + 50, y0 + 250 + i * 66));
    let yy = y0 + 250 + hl.length * 66 - 20;
    if (ill.sub) { ctx.fillStyle = '#444'; ctx.font = font(o, 600, 30, 'body'); wrapText(ctx, ill.sub, w - 100, 2).forEach((l, i) => ctx.fillText(l, x + 50, yy + 30 + i * 40)); yy += 100; }
    const phH = Math.max(120, y0 + h - 40 - yy);
    const pg = ctx.createLinearGradient(0, yy, 0, yy + phH); pg.addColorStop(0, '#7FA8FF'); pg.addColorStop(1, C.blue);
    ctx.fillStyle = pg; ctx.fillRect(x + 50, yy, w * 0.55, phH);
    ctx.fillStyle = 'rgba(255,255,255,.35)'; ctx.beginPath(); ctx.moveTo(x + 50, yy + phH); ctx.lineTo(x + 50 + w * 0.2, yy + phH * 0.45); ctx.lineTo(x + 50 + w * 0.35, yy + phH * 0.7); ctx.lineTo(x + 50 + w * 0.45, yy + phH * 0.5); ctx.lineTo(x + 50 + w * 0.55, yy + phH); ctx.fill();
    ctx.fillStyle = '#CFCAC0'; for (let i = 0; yy + i * 30 < y0 + h - 50; i++) ctx.fillRect(x + 80 + w * 0.55, yy + 6 + i * 30, w * 0.45 - 130, 10);
  } else if (T === 'search') {
    const x = 70, w = 940, h = Math.min(bottom - top, 800), y0 = top;
    ctx.translate(0, (1 - enter) * 160); ctx.globalAlpha = clamp(enter, 0, 1);
    ctx.fillStyle = 'rgba(7,27,110,.22)'; rr(ctx, x + 12, y0 + 20, w, h, 28); ctx.fill();
    fillRR(ctx, x, y0, w, h, 28, '#FFFFFF');
    ctx.save(); rr(ctx, x, y0, w, h, 28); ctx.clip(); ctx.fillStyle = '#EEF2F9'; ctx.fillRect(x, y0, w, 70); ctx.restore();
    ['#E5484D', '#F5B83D', '#3FBF6F'].forEach((c, i) => { ctx.fillStyle = c; ctx.beginPath(); ctx.arc(x + 44 + i * 34, y0 + 35, 11, 0, Math.PI * 2); ctx.fill(); });
    const q = String(ill.query || '').replace(/[*[\]]/g, ''); const nType = Math.floor(clamp((lt - 0.35) * 22, 0, q.length)); const typed = q.slice(0, nType);
    fillRR(ctx, x + 40, y0 + 100, w - 80, 96, 48, '#FFFFFF'); ctx.strokeStyle = C.blue; ctx.lineWidth = 4; rr(ctx, x + 40, y0 + 100, w - 80, 96, 48); ctx.stroke();
    ctx.strokeStyle = C.blue; ctx.lineWidth = 7; ctx.beginPath(); ctx.arc(x + 100, y0 + 144, 18, 0, Math.PI * 2); ctx.stroke(); ctx.beginPath(); ctx.moveTo(x + 113, y0 + 158); ctx.lineTo(x + 128, y0 + 173); ctx.stroke();
    ctx.fillStyle = C.navy; ctx.font = font(o, 600, 36, 'body'); const qs = wrapText(ctx, typed, w - 260, 1)[0] || ''; ctx.fillText(qs, x + 150, y0 + 161);
    if (Math.floor(lt * 3) % 2 === 0 && nType < q.length + 1) { const cw = ctx.measureText(qs).width; ctx.fillRect(x + 154 + cw, y0 + 126, 4, 44); }
    const t0 = 0.35 + q.length / 22 + 0.2; const items = (ill.items || []).slice(0, 4); const pick = Number(ill.pick) || 0;
    const rh = Math.min(150, (h - 240) / Math.max(items.length, 1));
    items.forEach((it, i) => {
      const p = easeOut(clamp((lt - t0 - i * 0.25) / 0.35, 0, 1)); if (p <= 0) return;
      const y = y0 + 230 + i * rh; ctx.save(); ctx.globalAlpha = clamp(p, 0, 1); ctx.translate(0, (1 - p) * 30);
      if (pick === i + 1) { ctx.fillStyle = 'rgba(215,242,60,.55)'; rr(ctx, x + 26, y - 6, w - 52, rh - 12, 18); ctx.fill(); }
      fillRR(ctx, x + 50, y + 14, 180, 14, 7, '#9FDCC0');
      ctx.fillStyle = C.blue; ctx.font = font(o, 700, 34, 'head'); ctx.fillText(wrapText(ctx, it, w - 120, 1)[0] || '', x + 50, y + 70);
      fillRR(ctx, x + 50, y + 90, w - 160, 12, 6, '#E3E9F5'); fillRR(ctx, x + 50, y + 112, (w - 160) * 0.7, 12, 6, '#E3E9F5');
      ctx.restore();
    });
  } else if (T === 'tv') {
    const w = 920, h = 600, x = 540 - w / 2, y0 = top;
    ctx.translate(540, y0 + h / 2); ctx.scale(lerp(0.6, 1, enter), lerp(0.6, 1, enter)); ctx.translate(-540, -(y0 + h / 2)); ctx.globalAlpha = clamp(enter, 0, 1);
    ctx.fillStyle = '#1C2236'; ctx.fillRect(500, y0 + h, 80, 70); fillRR(ctx, 380, y0 + h + 60, 320, 22, 11, '#1C2236');
    fillRR(ctx, x - 20, y0 - 20, w + 40, h + 40, 30, '#141A2C');
    ctx.save(); rr(ctx, x, y0, w, h, 14); ctx.clip();
    const sg = ctx.createLinearGradient(0, y0, 0, y0 + h); sg.addColorStop(0, '#2A7BFF'); sg.addColorStop(1, '#0A2A8A'); ctx.fillStyle = sg; ctx.fillRect(x, y0, w, h);
    ctx.fillStyle = 'rgba(255,255,255,.12)'; [[60, 260], [150, 200], [230, 300], [330, 230], [430, 330], [540, 250], [640, 290], [740, 210], [820, 270]].forEach(([dx, hh]) => ctx.fillRect(x + dx, y0 + h - 120 - hh * 0.8, 70, hh));
    const ic = assets.icons && assets.icons[ill.icon] ; if (ic) { const s2 = 1 + Math.sin(lt * 2) * 0.03; ctx.drawImage(ic, 540 - 120 * s2, y0 + 60, 240 * s2, 240 * s2); }
    const lp = easeOut(k(0.1));
    ctx.fillStyle = C.lime; const lw2 = 210; ctx.fillRect(x, y0 + h - 210, lw2 * lp, 60);
    ctx.fillStyle = C.navy; ctx.font = font(o, 800, 34, 'head'); if (lp > 0.6) ctx.fillText(String(ill.label || 'BERITA').toUpperCase().slice(0, 10), x + 24, y0 + h - 168);
    ctx.fillStyle = '#FFFFFF'; ctx.fillRect(x, y0 + h - 150, w * lp, 150);
    if (lp > 0.6) { ctx.fillStyle = C.navy; ctx.font = font(o, 800, 40, 'head'); wrapText(ctx, ill.headline || '', w - 60, 2).forEach((l, i) => ctx.fillText(l, x + 26, y0 + h - 92 + i * 50)); }
    ctx.restore();
    if (ill.ticker) {
      const ty = y0 + h + 110; ctx.fillStyle = C.navy; ctx.fillRect(0, ty, W, 70); ctx.fillStyle = C.lime; ctx.fillRect(0, ty, 170, 70);
      ctx.fillStyle = C.navy; ctx.font = font(o, 800, 30, 'head'); ctx.fillText('TERKINI', 26, ty + 46);
      ctx.save(); ctx.beginPath(); ctx.rect(170, ty, W - 170, 70); ctx.clip(); ctx.fillStyle = '#fff'; ctx.font = font(o, 600, 32, 'body');
      const tx = String(ill.ticker).replace(/[*[\]]/g, '') + '   •   '; const tw = ctx.measureText(tx).width; const off = (lt * 160) % tw;
      for (let xx = 190 - off; xx < W; xx += tw) ctx.fillText(tx, xx, ty + 46); ctx.restore();
    }
  } else if (T === 'timeline') {
    const items = (ill.items || []).slice(0, 5); const n = Math.max(items.length, 1);
    const lx = 190, y1 = top + 100, y2 = bottom - 60, gap = (y2 - y1) / Math.max(n - 1, 1);
    const prog = clamp((lt - 0.3) / Math.max(0.8, dur * 0.75), 0, 1);
    ctx.strokeStyle = 'rgba(255,255,255,.25)'; ctx.lineWidth = 12; ctx.lineCap = 'round'; ctx.beginPath(); ctx.moveTo(lx, y1); ctx.lineTo(lx, y2); ctx.stroke();
    ctx.strokeStyle = C.lime; ctx.beginPath(); ctx.moveTo(lx, y1); ctx.lineTo(lx, lerp(y1, y2, prog)); ctx.stroke();
    items.forEach((it, i) => {
      const at = n === 1 ? 0 : i / (n - 1); const on = prog >= at - 0.001; const p = easeBack(clamp((prog - at) * 6 + (i === 0 ? 1 : 0), 0, 1));
      const y = y1 + i * gap; const lab = typeof it === 'object' ? String(it.t || '') : ''; const txt = typeof it === 'object' ? String(it.text || '') : String(it);
      ball(ctx, lx, y, on ? 30 : 22, on ? C.lime : '#3C4A86', on ? '#F1FFA3' : '#56649E', on ? '#9DB81A' : '#232F66');
      ctx.save(); ctx.globalAlpha = 0.35 + 0.65 * clamp(p, 0, 1); ctx.translate((1 - clamp(p, 0, 1)) * 40, 0);
      const cw = 720, chh = Math.min(150, gap - 20);
      fillRR(ctx, lx + 70, y - chh / 2, cw, chh, 22, on ? '#FFFFFF' : 'rgba(255,255,255,.14)');
      if (lab) { ctx.font = font(o, 800, 30, 'head'); const tw = ctx.measureText(lab.toUpperCase()).width + 34; fillRR(ctx, lx + 96, y - chh / 2 - 22, tw, 48, 24, C.blue); ctx.fillStyle = '#fff'; ctx.fillText(lab.toUpperCase(), lx + 113, y - chh / 2 + 12); }
      ctx.fillStyle = on ? C.navy : 'rgba(255,255,255,.75)'; ctx.font = font(o, 700, 34, 'body');
      const ls = wrapText(ctx, txt, cw - 60, 2); ls.forEach((l, li) => ctx.fillText(l, lx + 100, y + 14 - (ls.length - 1) * 20 + li * 42 + (lab ? 8 : 0)));
      ctx.restore();
    });
  } else if (T === 'network') {
    const items = (ill.items || []).slice(0, 6); const n = Math.max(items.length, 1);
    const cx = 540, cy = (top + bottom) / 2, R0 = Math.min(330, (bottom - top) / 2 - 70);
    const pts = items.map((_, i) => { const a = -Math.PI / 2 + (i + 0.5) * (Math.PI * 2 / n); return [cx + Math.cos(a) * R0 * 1.15, cy + Math.sin(a) * R0]; });
    pts.forEach(([px2, py2], i) => {
      const p = easeOut(k(0.2 + i * 0.18)); if (p <= 0) return;
      ctx.strokeStyle = 'rgba(0,200,248,.6)'; ctx.lineWidth = 6; ctx.setLineDash([14, 12]); ctx.lineDashOffset = -lt * 60;
      ctx.beginPath(); ctx.moveTo(cx, cy); ctx.lineTo(lerp(cx, px2, p), lerp(cy, py2, p)); ctx.stroke(); ctx.setLineDash([]);
      if (p >= 1) { const f = (lt * 0.8 + i * 0.17) % 1; ctx.fillStyle = C.lime; ctx.beginPath(); ctx.arc(lerp(cx, px2, f), lerp(cy, py2, f), 9, 0, Math.PI * 2); ctx.fill(); }
    });
    const cp = easeBack((lt - 0.05) / 0.5);
    ctx.save(); ctx.translate(cx, cy); ctx.scale(cp, cp); ball(ctx, 0, 0, 120, '#0058F8', '#3FA0FF', '#05329A');
    ctx.fillStyle = '#fff'; ctx.textAlign = 'center'; ctx.font = font(o, 800, 38, 'head'); wrapText(ctx, String(ill.center || 'RILIS').toUpperCase(), 200, 2).forEach((l, i, arr) => ctx.fillText(l, 0, 14 - (arr.length - 1) * 22 + i * 44)); ctx.restore();
    pts.forEach(([px2, py2], i) => {
      const p = easeBack(k(0.45 + i * 0.18)); if (p <= 0) return;
      ctx.save(); ctx.translate(px2, py2); ctx.scale(p, p); ctx.font = font(o, 800, 38, 'head');
      const ls = wrapText(ctx, items[i], 280, 2); const tw = Math.max(...ls.map((l) => ctx.measureText(l).width)) + 56; const th = 44 + ls.length * 46;
      ctx.fillStyle = 'rgba(0,0,0,.3)'; rr(ctx, -tw / 2 + 5, -th / 2 + 8, tw, th, 22); ctx.fill();
      fillRR(ctx, -tw / 2, -th / 2, tw, th, 22, '#FFFFFF'); ctx.fillStyle = C.navy; ctx.textAlign = 'center';
      ls.forEach((l, li) => ctx.fillText(l, 0, -th / 2 + 60 + li * 46)); ctx.restore();
    });
  }
  ctx.restore();
  if (scene.section && scene.section.text) sectionPill(ctx, scene.section, lt, o); else topCard(ctx, scene.card, lt, o);
  badge(ctx, scene.badge, lt, Object.assign({}, o, {badgeY: top + 60}));
  cutLogo(ctx, assets, dark);
  presenterBubble(ctx, t, talk, scene.gesture || 'explain', lt);
}
const BEAT_DEF = 4;
/** Beat layout: a scene shows ceil(dur / beatSec) illustrations (capped by how many it lists), split evenly,
    so no illustration stays on screen longer than beatSec and none flashes by too briefly. */
function beatPlan(reel, scene, dur) {
  const sec = Number(reel && reel.beatSec) > 0 ? Number(reel.beatSec) : BEAT_DEF;
  const list = [scene.illus || {type: 'none'}].concat(scene.beats || []);
  const n = Math.max(1, Math.min(list.length, Math.ceil(dur / sec - 0.001)));
  return {list, n, seg: dur / n};
}
function beatOf(reel, scene, lt, dur) {
  const {list, n, seg} = beatPlan(reel, scene, dur || 999);
  const b = Math.min(Math.floor(Math.max(lt, 0) / seg), n - 1);
  if (b === 0) return {scene, ilt: lt, b: 0};
  const ill = list[b];
  return {scene: Object.assign({}, scene, {illus: ill, card: ill.card || null, badge: ill.badge || null, section: null, onscreen: ill.onscreen || ''}), ilt: lt - b * seg, b};
}
function drawStageScene(ctx, reel, idx, lt0, dur, assets, o) {
  const sceneFull = (reel.scenes || [])[idx] || {};
  const bt = beatOf(reel, sceneFull, lt0, dur); const scene = bt.scene; const lt = bt.ilt; const ltv = lt0;
  const t = o.globalT != null ? o.globalT : lt;
  const studio = (reel.set || 'studio') === 'studio';
  ctx.save(); ctx.clearRect(0, 0, W, H);
  const ill = scene.illus || {};
  const talk = o.talking != null ? o.talking : (ltv > 0.12 && ltv < dur - 0.25);
  const hasTop = (scene.card && (scene.card.text || scene.card.tag)) || (scene.section && scene.section.text);
  const gest = scene.gesture || 'explain';
  const isCut = CUTS.includes(ill.type);
  if (isCut) {
    drawCutaway(ctx, scene, lt, dur, assets, o, t, talk);
  } else if (studio) {
    // camera: slow push-in on every studio shot; "close" = punch-in on the presenter for emphasis
    const close = scene.shot === 'close';
    const z = close ? lerp(1.12, 1.3, easeOut(ltv / 0.6)) : 1 + 0.025 * clamp(ltv / Math.max(dur, 1), 0, 1);
    ctx.save(); ctx.translate(540, close ? 760 : 1000); ctx.scale(z, z); ctx.translate(-540, close ? -760 : -1000);
    // office studio set (same as the posted reels): presenter + laptop always on screen
    drawStudio(ctx, t);
    drawPerson(ctx, t, talk, gest, ltv);
    const raiseR = gest === 'point' || gest === 'explain' || gest === 'count' ? easeOut((ltv - 0.2) / 0.6) * (gest === 'point' || gest === 'count' ? 1 : 0.65 + Math.sin(ltv * 2.4) * 0.2) * (1 - easeOut((ltv - dur + 0.5) / 0.5)) : 0;
    const raiseL = gest === 'shrug' ? 0.55 + Math.sin(lt * 3) * 0.1 : 0;
    drawArm(ctx, -1, raiseL, t); drawArm(ctx, 1, clamp(raiseR, 0, 1), t);
    drawLaptop(ctx, assets, t);
    ctx.restore();
    if (ill.type === 'art') {
      const hc = scene.card && (scene.card.text || scene.card.tag);
      if (hc) topCard(ctx, scene.card, lt, o);
      drawArt(ctx, ill, lt, {x: 70, y: hc ? 492 : 250, w: 940, h: hc ? 380 : 610}, o);
      badge(ctx, scene.badge, lt, Object.assign({}, o, {badgeY: hc ? 790 : 760}));
    } else if (ill.type === 'repost') {
      topCard(ctx, {tag: ill.tag || 'BANTU SEBARKAN', tagColor: 'blue', text: ill.text || '*Repost* biar temanmu tahu'}, lt, o);
      const a = easeBack((lt - 0.25) / 0.6);
      if (a > 0) {
        ctx.save(); ctx.translate(540, 650); ctx.scale(a * 0.8, a * 0.8); ctx.rotate(Math.sin(lt * 2) * 0.03);
        ctx.fillStyle = 'rgba(0,0,0,.25)'; ctx.beginPath(); ctx.arc(10, 18, 190, 0, Math.PI * 2); ctx.fill();
        ball(ctx, 0, 0, 190, '#0058F8', '#3FA0FF', '#05329A');
        ctx.strokeStyle = '#fff'; ctx.lineWidth = 34; ctx.lineCap = 'round'; const sp = lt * 1.2;
        ctx.beginPath(); ctx.arc(0, 0, 95, Math.PI * 1.05 + sp, Math.PI * 1.85 + sp); ctx.stroke();
        ctx.beginPath(); ctx.arc(0, 0, 95, Math.PI * 0.05 + sp, Math.PI * 0.85 + sp); ctx.stroke();
        [Math.PI * 1.85 + sp, Math.PI * 0.85 + sp].forEach((ang) => { ctx.save(); ctx.translate(Math.cos(ang) * 95, Math.sin(ang) * 95); ctx.rotate(ang + Math.PI / 2); ctx.fillStyle = '#fff'; ctx.beginPath(); ctx.moveTo(-38, 10); ctx.lineTo(38, 10); ctx.lineTo(0, -40); ctx.closePath(); ctx.fill(); ctx.restore(); });
        ctx.restore();
      }
    } else if (ill.type === 'cta') {
      topCard(ctx, scene.card || {tag: 'VRITIMES', tagColor: 'blue', text: scene.onscreen || 'Tulis, sebar, [pantau]'}, lt, o);
      drawPanelIn(ctx, Object.assign({}, scene, {onscreen: ''}), lt, dur, assets, o, {px: 90, py: 490, pw: 900, ph: 370, bg: S2.cream});
    } else {
      whiteCard(ctx, scene, lt, dur, assets, Object.assign({}, o, {maxBottom: 860}));
      if (scene.section && scene.section.text) sectionPill(ctx, scene.section, lt, o); else topCard(ctx, scene.card, lt, o);
      badge(ctx, scene.badge, lt, Object.assign({}, o, {badgeY: 760}));
    }
    if (idx === 0) drawLowerThird(ctx, ltv, Object.assign({}, o, {lowerY: 1095}));
  } else {
    stageBg(ctx, t);
    if (ill.type === 'art') {
      const hc = scene.card && (scene.card.text || scene.card.tag); if (hc) topCard(ctx, scene.card, lt, o);
      drawArt(ctx, ill, lt, {x: 70, y: hc ? 500 : 320, w: 940, h: 640}, o);
    } else if (ill.type === 'repost') {
      repostEnd(ctx, scene, lt, o);
    } else if (ill.type === 'cta') {
      topCard(ctx, scene.card || {tag: 'VRITIMES', tagColor: 'blue', text: scene.onscreen || 'Tulis, sebar, *pantau*'}, lt, o);
      drawPanelIn(ctx, Object.assign({}, scene, {onscreen: ''}), lt, dur, assets, o, {px: 90, py: 440, pw: 900, ph: 560, bg: S2.cream});
    } else {
      const hasCard = whiteCard(ctx, scene, lt, dur, assets, o);
      if (!hasCard) {
        const enter = easeOut(lt / 0.4);
        const fingers = scene.fingers || (scene.badge && /^\d+$/.test(String(scene.badge.big || '')) ? Number(scene.badge.big) : 3);
        toon(ctx, t, {x: scene.badge ? 430 : 540, y: lerp(hasTop ? 720 : 620, hasTop ? 670 : 570, enter), s: 0.95, talk, gesture: gest, gt: lt, fingers, female: reel.character === 'female'});
        badge(ctx, scene.badge, lt, o);
      }
      if (scene.section && scene.section.text) sectionPill(ctx, scene.section, lt, o); else topCard(ctx, scene.card, lt, o);
    }
    stageWatermark(ctx, assets);
  }
  if (o.subtitles !== false && !(ill.type === 'repost' && !studio)) karaoke(ctx, sceneFull, ltv, dur, Object.assign({}, o, {capY: isCut ? 1450 : studio ? 1310 : 1150}));
  if (lt < 0.1) { ctx.fillStyle = `rgba(255,255,255,${0.25 * (1 - lt / 0.1)})`; ctx.fillRect(0, 0, W, H); }
  ctx.restore();
}
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

const DEF_O = {fHead: 'Poppins, sans-serif', fBody: 'Inter, sans-serif', fHand: 'Caveat, cursive', lang: 'id', cc: 'ID', countryName: 'Indonesia', roleTitle: 'PR Specialist'};
function drawScene(ctx, reel, idx, lt, dur, assets, opts) {
  const o = Object.assign({}, DEF_O, opts || {});
  if ((reel.style || 'stage') === 'stage') return drawStageScene(ctx, reel, idx, lt, dur, assets, o);
  const scenes = reel.scenes || []; const scene = scenes[idx] || {};
  const t = (opts && opts.globalT != null ? opts.globalT : lt + idx * 3.3);
  ctx.save(); ctx.clearRect(0, 0, W, H);
  drawStudio(ctx, t);
  const talk = o.talking != null ? o.talking : (lt > 0.15 && lt < dur - 0.3);
  const g = scene.gesture || 'explain';
  drawPerson(ctx, t, talk, g, lt);
  const raiseR = g === 'point' || g === 'explain' ? easeOut((lt - 0.2) / 0.6) * (g === 'point' ? 1 : 0.65 + Math.sin(lt * 2.4) * 0.2) * (1 - easeOut((lt - dur + 0.5) / 0.5)) : g === 'count' ? 0.8 : 0;
  const raiseL = g === 'shrug' ? 0.55 + Math.sin(lt * 3) * 0.1 : 0;
  drawArm(ctx, -1, raiseL, t); drawArm(ctx, 1, clamp(raiseR, 0, 1), t);
  drawLaptop(ctx, assets, t);
  drawPanel(ctx, scene, lt, dur, assets, o, idx, scenes.length);
  if (idx === 0) drawLowerThird(ctx, lt, o);
  if (o.subtitles !== false) drawSubtitle(ctx, scene, lt, dur, o);
  drawTop(ctx, assets, idx, Math.max(scenes.length, 1), lt, dur);
  // scene cut flash
  if (lt < 0.12) { ctx.fillStyle = `rgba(255,255,255,${0.35 * (1 - lt / 0.12)})`; ctx.fillRect(0, 0, W, H); }
  ctx.restore();
}
function drawFrame(ctx, reel, durs, t, assets, opts) {
  let acc = 0, i = 0;
  while (i < durs.length - 1 && t >= acc + durs[i]) { acc += durs[i]; i++; }
  drawScene(ctx, reel, i, t - acc, durs[i] || 3, assets, Object.assign({}, opts, {globalT: t}));
  return i;
}
/** SFX cues for one scene, times relative to scene start (match the reveal timings in drawPanel). */
function sceneCues(scene, idx, dur) {
  const cues = []; const ill = (scene && scene.illus) || {}; const T = ill.type || 'title';
  if (idx > 0) cues.push({t: 0, name: 'whoosh', vol: 0.35});
  else cues.push({t: 0.05, name: 'whoosh', vol: 0.3});
  if (T === 'title' || T === 'hook') cues.push({t: 0.3, name: 'pop', vol: 0.35});
  if (T === 'stat') { cues.push({t: 0.3, name: 'pop', vol: 0.3}); cues.push({t: 1.5, name: 'ding', vol: 0.32}); }
  if (T === 'list' || T === 'steps') (ill.items || []).slice(0, 4).forEach((_, i) => cues.push({t: 0.38 + i * 0.35, name: 'pop', vol: 0.32}));
  if (T === 'compare') [0, 0.5].forEach((d) => cues.push({t: 0.38 + d, name: 'pop', vol: 0.32}));
  if (T === 'chart') (ill.bars || []).slice(0, 5).forEach((_, i) => cues.push({t: 0.4 + i * 0.2, name: 'click', vol: 0.4}));
  if (T === 'chat') (ill.messages || []).slice(0, 4).forEach((_, i) => { cues.push({t: 0.2 + i * 0.6, name: 'type', vol: 0.22}); cues.push({t: 0.38 + i * 0.6, name: 'pop', vol: 0.28}); });
  if (T === 'icon') ((ill.icons && ill.icons.length ? ill.icons : [ill.icon || 'news']).slice(0, 3)).forEach((_, i) => cues.push({t: 0.38 + i * 0.3, name: 'pop', vol: 0.32}));
  if (T === 'quote') cues.push({t: 0.35, name: 'click', vol: 0.35});
  if (T === 'cta') cues.push({t: 0.55, name: 'success', vol: 0.4});
  if (T === 'grid') (ill.items || []).slice(0, 16).forEach((_, i) => { if (i % 3 === 0) cues.push({t: 0.38 + i * 0.06, name: 'click', vol: 0.3}); });
  if (T === 'doc') cues.push({t: 0.3, name: 'pop', vol: 0.3});
  if (T === 'repost') cues.push({t: 0.3, name: 'success', vol: 0.4});
  if (T === 'phone' || T === 'inbox') (ill.items || []).slice(0, 6).forEach((_, i) => cues.push({t: 0.32 + i * (T === 'phone' ? 0.35 : 0.25), name: 'pop', vol: 0.28}));
  if (T === 'inbox' && ill.pick) cues.push({t: 0.4 + (ill.items || []).slice(0, 6).length * 0.25 + 0.4, name: 'ding', vol: 0.32});
  if (T === 'search') { const n = String(ill.query || '').length; for (let i = 0; i < Math.min(n, 30); i += 4) cues.push({t: 0.35 + i / 22, name: 'type', vol: 0.2}); }
  if (T === 'newspaper') cues.push({t: 0.55, name: 'pop', vol: 0.35});
  if (T === 'tv') cues.push({t: 0.4, name: 'ding', vol: 0.3});
  if (T === 'timeline') (ill.items || []).slice(0, 5).forEach((_, i, a) => cues.push({t: 0.3 + (a.length > 1 ? i / (a.length - 1) : 0) * Math.max(0.8, dur * 0.75), name: 'click', vol: 0.32}));
  if (T === 'network') (ill.items || []).slice(0, 6).forEach((_, i) => cues.push({t: 0.75 + i * 0.18, name: 'pop', vol: 0.26}));
  if (scene && scene.card && (scene.card.text || scene.card.tag)) cues.push({t: 0.12, name: 'pop', vol: 0.28});
  if (scene && scene.section && scene.section.text) cues.push({t: 0.1, name: 'pop', vol: 0.32});
  if (scene && scene.badge && (scene.badge.text || scene.badge.big)) cues.push({t: 0.45, name: scene.badge.big ? 'ding' : 'pop', vol: 0.32});
  return cues.filter((c) => c.t < Math.max(dur, 0.6));
}
function artCues(ill) {
  const c = [{t: 0.05, name: 'pop', vol: 0.3}];
  const A = ill.art;
  if (A === 'mythbust') { c.push({t: 0.7, name: 'click', vol: 0.35}); c.push({t: 1.25, name: 'ding', vol: 0.35}); }
  else if (A === 'docwrite') (ill.items || [0, 0, 0]).slice(0, 4).forEach((_, i) => c.push({t: 0.4 + i * 0.55 + 0.2, name: 'pop', vol: 0.28}));
  else if (A === 'rocket') c.push({t: 0.3, name: 'whoosh', vol: 0.4});
  else if (A === 'phonesearch') c.push({t: 0.6, name: 'type', vol: 0.22});
  else if (A === 'shop' || A === 'trust' || A === 'newspaper') c.push({t: 0.8, name: 'ding', vol: 0.25});
  return c;
}
function sfxCues(reel, durs) {
  const out = []; let acc = 0;
  (reel.scenes || []).forEach((sc, i) => {
    const {list, n, seg} = beatPlan(reel, sc, durs[i]);
    const first = list[0] && list[0].type === 'art' ? artCues(list[0]).concat(i > 0 ? [{t: 0, name: 'whoosh', vol: 0.35}] : []) : sceneCues(sc, i, seg);
    first.filter((c) => c.t < seg).forEach((c) => out.push({t: acc + c.t, name: c.name, vol: c.vol}));
    list.slice(1, n).forEach((ill, k) => {
      const b0 = (k + 1) * seg;
      const cs = [{t: 0, name: 'whoosh', vol: 0.35}].concat(ill.type === 'art' ? artCues(ill) : sceneCues(Object.assign({}, sc, {illus: ill, card: ill.card, badge: ill.badge, section: null}), 1, seg).filter((x) => x.name !== 'whoosh'));
      cs.filter((c) => c.t < seg).forEach((c) => out.push({t: acc + b0 + c.t, name: c.name, vol: c.vol}));
    });
    acc += durs[i];
  });
  return out;
}
const api = {W, H, ICON_NAMES, ART_NAMES, CUTS, BEAT_DEF, beatOf, beatPlan, drawArt, loadAssets, estimate, timeline, drawScene, drawFrame, sceneCues, sfxCues};
if (typeof module !== 'undefined' && module.exports) module.exports = api;
root.VRScene = api;
})(typeof window !== 'undefined' ? window : globalThis);
