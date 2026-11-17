# VRITIMES Reels (Remotion packages)

Packages downloaded from the VRITIMES SNS Dashboard live here, one folder per reel:
`reels/{CC}/{slug}/` (Remotion project: `src/scene.js`, `public/reel.json`, fonts, logos, SFX).

## House rules (apply to every reel package — no need to ask again)
1. **New illustration at least every 4 seconds.** `reel.json` gets `"beatSec": 4`. Every scene longer than 4 s lists
   extra illustrations in `scene.beats[]`; the engine splits the scene evenly
   (`ceil(duration / 4)` illustrations), so nothing stays on screen > 4 s and nothing flashes by too briefly.
2. **No empty scenes.** Scenes with `illus.type: "none"` get a 2D art illustration.
3. **2D illustrations with decent detail, easy to read:** flat style, navy outlines, blue-dominant, lime accents,
   one clear idea per illustration, large shapes, at most a few words of text inside.
4. **Numbers must match `research/`** (e.g. UMKM share of GDP = "lebih dari 60%", Kemenko Perekonomian 2025) and the
   caption lists the source with URL.
5. **Voice-over: native voice of the market.** ID → `id-ID-ArdiNeural` (Ardi, Bahasa Indonesia). Set `"voice"` in
   `reel.json` before running TTS; write VO text with the brand name as `VRITIMES` and let `pron` handle it
   (`VRITIMES = Fritaims`, `vritimes.com = Fritaims dot kom`). Other markets: ask once, then record the choice here.
6. Keep the dashboard's timing, subtitles and SFX; only `src/scene.js`, `scripts/tts.py` and `public/reel.json` change.

## Engine
`reels/_engine/scene.js` = dashboard renderer v1 (`reels/_original/scene_v1_dashboard.js`) + 2D art library
(`reels/_engine/art.js`) + beat system. Copy it over `src/scene.js` of each new package.
It is a drop-in replacement: the same file also works as the dashboard preview renderer.

### 2D art catalogue (`illus.type: "art"`) — see `reels/_engine/art_catalog.png`
| art | shows | data fields |
|---|---|---|
| `shop` | UMKM storefront, owner waving | `label`, `open`, `hijab` |
| `quietvoice` | loud big buildings vs small shop's faint voice | `label` |
| `mythbust` | myth crossed out, FAKTA stamp lands | `myth`, `fact`, `mythTag`, `factTag` |
| `newsroom` | journalist at desk, stories flying into the monitor | `headline`, `count`, `screen` |
| `newspaper` | hands holding a newspaper with your story | `headline`, `paper`, `badge`, `label` |
| `phonesearch` | customer searches your name, your news shows up | `query`, `result`, `hijab` |
| `docwrite` | press release checklist being ticked, pen writing | `items[]`, `header`, `note` |
| `trust` | owner + customer handshake, stars & hearts | `label` |
| `rocket` | rocket launching from a laptop | `label` |
| `share` | three phones passing a post along | `label` |
| `growth` | bar chart growing, coins | `values[]`, `label` |

Example scene: `{"vo": "...", "illus": {"type": "stat", "big": ">60%"}, "beats": [{"type": "art", "art": "quietvoice"}]}`

## Workflow for a new package
```bash
unzip <package>.zip -d reels/{CC}/            # then rename folder to the slug
cp reels/_engine/scene.js reels/{CC}/{slug}/src/scene.js
# edit public/reel.json: beatSec 4, beats for scenes > 4 s, art for "none" scenes, verify numbers/sources
node templates/reel_preview.js reels/{CC}/{slug} /tmp/prev sheet          # 1 frame per second (QA)
node templates/reel_preview.js reels/{CC}/{slug} /tmp/prev video          # silent+SFX preview mp4
node templates/art_gallery.js reels/_engine/art_catalog.png               # refresh catalogue after adding art
```
Voice-over + final video (works in this cloud session too):
```bash
cp reels/_engine/tts.py reels/{CC}/{slug}/scripts/tts.py          # proxy-aware edge-tts script
(cd reels/{CC}/{slug} && SSL_CERT_FILE=/root/.ccr/ca-bundle.crt python3 scripts/tts.py)   # -> public/vo/
node templates/reel_preview.js reels/{CC}/{slug} /tmp/prev video   # mixes VO + SFX; prints the 4-second beat check
ffmpeg -i /tmp/prev/preview.mp4 -c:v copy -af loudnorm=I=-14:TP=-1.5:LRA=11 -c:a aac -b:a 192k reels/{CC}/{slug}/preview/final_with_vo.mp4
```
Always re-check beats **after** VO is generated: real VO is usually longer than the estimate, so add beats until the check shows ✓.
Or with Remotion on your own machine: inside the package `npm install && npm run all`.
