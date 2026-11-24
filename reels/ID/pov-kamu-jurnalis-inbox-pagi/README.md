# VRITIMES Reel — POV: Kamu Jurnalis, Ini Cara Rilismu Dibaca

Motion-graphic reel (1080×1920, 30 fps): POV of a VRITIMES PR specialist talking to camera in an office studio, laptop with the VRITIMES logo, animated illustrations per scene, subtitles. Voice-over: Microsoft Edge neural voice `de-DE-FlorianMultilingualNeural` (rate +0%) via edge-tts (free). Supporting SFX (whoosh, pop, ding, typing, chime) in `public/sfx/`, timed to each illustration reveal.

The frames are drawn by `src/scene.js`, the same file the VRITIMES SNS Dashboard uses for its preview, so the render matches what you saw there.

## Render (Claude Code or any machine with Node 18+, Python 3 and internet)

```bash
npm install
pip install -r requirements.txt
npm run tts      # voice-over per scene -> public/vo/*.mp3 + timing.json
npm run render   # -> out/id-pov-kamu-jurnalis-inbox-pagi.mp4
npm run master   # loudness -14 LUFS for Reels -> out/id-pov-kamu-jurnalis-inbox-pagi_final.mp4  (or: npm run all)
```

Preview and tweak: `npm run studio`. Another voice: `python3 scripts/tts.py --voice en-AU-WilliamNeural` (list: `edge-tts --list-voices`). Faster speech: `--rate +8%`.
Scene text, illustrations and gestures live in `public/reel.json` (edit there, or edit in the dashboard and download the package again).

Scene illustration types: title, stat, list, steps, compare, chart, chat, quote, icon, cta. Gestures: explain, point, count, shrug, smile, surprise.

## Revisi v2 (repo VRITIMES)
- `src/scene.js` = engine v2 (`reels/_engine/scene.js`), `scripts/tts.py` = versi proxy-aware.
- Voice-over Bahasa Indonesia, suara **Ardi** (`id-ID-ArdiNeural`), pelafalan `VRITIMES = Fritaims`.
- Ilustrasi baru maksimal tiap 4 detik (maks. 3,85 detik): 18 ilustrasi dalam 50,9 detik; adegan 1, 7, 8 yang kosong kini berilustrasi.
- Adegan 3: klaim "±5 detik" (tanpa sumber) diganti data Muck Rack 2025: 69% jurnalis lebih suka pitch di bawah 200 kata. Sumber ditambahkan ke caption.
- Video final (VO + SFX, −14 LUFS): `preview/final_with_vo.mp4`; key frames: `preview/keyframes.png`.
