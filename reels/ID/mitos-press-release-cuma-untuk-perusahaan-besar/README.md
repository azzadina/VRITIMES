# VRITIMES Reel — Mitos: Press Release Cuma untuk Perusahaan Besar

Motion-graphic reel (1080×1920, 30 fps): POV of a VRITIMES PR specialist talking to camera in an office studio, laptop with the VRITIMES logo, animated illustrations per scene, subtitles. Voice-over: Microsoft Edge neural voice `de-DE-FlorianMultilingualNeural` (rate +0%) via edge-tts (free). Supporting SFX (whoosh, pop, ding, typing, chime) in `public/sfx/`, timed to each illustration reveal.

The frames are drawn by `src/scene.js`, the same file the VRITIMES SNS Dashboard uses for its preview, so the render matches what you saw there.

## Render (Claude Code or any machine with Node 18+, Python 3 and internet)

```bash
npm install
pip install -r requirements.txt
npm run tts      # voice-over per scene -> public/vo/*.mp3 + timing.json
npm run render   # -> out/id-mitos-press-release-cuma-untuk-perusahaan-besar.mp4
npm run master   # loudness -14 LUFS for Reels -> out/id-mitos-press-release-cuma-untuk-perusahaan-besar_final.mp4  (or: npm run all)
```

Preview and tweak: `npm run studio`. Another voice: `python3 scripts/tts.py --voice en-AU-WilliamNeural` (list: `edge-tts --list-voices`). Faster speech: `--rate +8%`.
Scene text, illustrations and gestures live in `public/reel.json` (edit there, or edit in the dashboard and download the package again).

Scene illustration types: title, stat, list, steps, compare, chart, chat, quote, icon, cta. Gestures: explain, point, count, shrug, smile, surprise.

## Revisi v2 (repo VRITIMES)
- `src/scene.js` diganti engine v2 (`reels/_engine/scene.js`): pustaka ilustrasi 2D + ilustrasi baru maksimal tiap 4 detik.
- `public/reel.json`: `beatSec: 4`, `beats` di setiap scene > 4 detik, scene 1 & 5 kini punya ilustrasi (toko UMKM, koran).
- Angka disesuaikan riset: UMKM "lebih dari 60%" PDB (Kemenko Perekonomian, 2025) — sebelumnya 61% (data 2021).
- Video final dengan voice-over Bahasa Indonesia (suara Ardi, `id-ID-ArdiNeural`) + SFX, loudness -14 LUFS: `preview/final_with_vo.mp4`. Voice-over: `public/vo/`. Pelafalan VRITIMES diatur di `pron` (`VRITIMES = Fritaims`).
- `scripts/tts.py` kini memakai proxy dari `HTTPS_PROXY` bila ada.
