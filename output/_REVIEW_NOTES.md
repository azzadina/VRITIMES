# Review notes — batch 16 Nov – 11 Dec 2026 (run of 2026-11-12)

## 🔴 Must check before posting
1. **Pricing = PRICE_UNVERIFIED for all 7 countries.** Every vritimes.com / vritimes.info page (pricing, service, About, newsroom) returns a *Vercel Security Checkpoint* (HTTP 429) to automated clients; it was not bypassed. The 14 PROMO posts therefore show "starts from — see link" (localized) and no numbers or media counts.
   → To add prices: create `research/promo.md` with live prices/promo + end date per country, update the PROMO `slides`/captions in `content/{CC}.py`, then run `python3 templates/build.py {CC} --only=PROMO && python3 templates/finalize.py`.
   Figures seen only in search snippets (NOT used): SG S$50 / 20 media, AU AU$50 / 20 media, ID Rp499k / 100 media, VN 15 media — please confirm or discard.
2. **Guaranteed media counts** differ across VRITIMES pages (PH 50, TH 20+, SG/AU 20, VN 15, ID 100, MY 10 in 2023). Posts say "count depends on plan". Confirm wording is acceptable.
3. **VRITIMES company facts** (5,000+ companies, 2025 market entries, media partnerships) could not be verified live → not used in posts.
4. **Reference image** was supplied in chat only (not as a file); style notes are in `brand/reference/README.md`. If you want it archived, add it as `brand/reference/grid-reference.png`.

## 🟡 Assumptions & items to verify
- **Dates estimated:** Ramadan/Hari Raya/Lebaran 2027, Chinese New Year 2027 (6–7 Feb), Tết 2027 (~6 Feb), PH National Heroes Day 2027 (30 Aug, last-Monday rule), AU Federal Budget 2027 (usually May). Marked "est./perkiraan/dự kiến" on slides; confirm with official calendars.
- **PH "MSME Development Month (July)"** used in the PH 2027 calendar — confirm still current.
- **Harbolnas Rp36,4 T (2025)** comes from media reports (ANTARA/VOI); no official Komdigi/idEA release found. Slide says "dilaporkan".
- **TH MSME GDP 2568** (6,606,631 ล้านบาท, +2.4%) is from Thansettakij citing OSMEP; OSMEP PDF could not be downloaded (connection reset).
- **Cision 72%** verified via Cision's own press release (search index), not the full PDF.
- **DNR country figures** read from the Reuters Institute DNR 2025 PDF (downloaded directly). Australian avoidance 69% from University of Canberra release.
- **Illustrative examples** (e.g. "Penang logistics start-up", "Chuỗi cà phê X", headline/subject-line samples) are fictional teaching examples, never presented as clients or results.
- **Posting times** are research-based defaults; TH 7 Dec (substitution holiday) and PH 30 Nov (Bonifacio Day) may warrant later LinkedIn slots.

## 🟢 Production notes
- Tools: python3, node + Playwright/Chromium, ffmpeg, pdfunite available; `img2pdf` not installed → PDFs built with Pillow.
- Fonts downloaded from Google Fonts into `brand/fonts/` (Poppins, Inter, Prompt, Noto Sans Thai, Be Vietnam Pro, Caveat — all OFL). Thai & Vietnamese render-tested.
- Logo: `brand/logo.zip` → `brand/logo/`; color stacked logo used in the white circular stamp on every cover/single/reel cover; white/color "beside" logo on inner slides by background.
- Palette extracted from logo → `brand/palette.json` (brand blue #0058F8). Automated check: blue family ≥ 91% on every image, lime ≤ 6.4%.
- Automated QA (`templates/qa.py`): 84/84 posts pass file structure, naming, IG hook ≤125 chars, hashtags (IG 3–6, LI 3–5, FB ≤3), LinkedIn 900–2,000 chars, first two LI lines ≤210 chars, UTM links, sources in all captions + sources.md, no competitor names/outdated prices.
- Reels: `reel_draft.mp4` are silent kinetic-text drafts (1080×1920, 18–26 s). Audio is a *type* suggestion only; pick a licensed track in-app. B-roll lists call for internal talent/own footage only.
- Photo tiles use own flat illustrations (no stock, no real people). Swap in authentic team photos anytime.
- Re-render anything: edit `content/{CC}.py` → `python3 templates/build.py {CC}` → `python3 templates/qa.py` → `python3 templates/finalize.py`.

## Revisi kapitalisasi (12 Nov 2026)
- Judul cover/slide **ID** mengikuti EYD V (kapital tiap kata kecuali kata tugas seperti di, ke, dari, dan, yang, untuk, sebagai, dalam, demi, sebelum, sampai bila tidak di awal).
- **MY/PH/SG/AU**: AP-style title case (a, the, of, to, in, for, and, vs … lowercase; hyphenated compounds capitalised per part).
- **VN**: sentence case + nama diri (Việt Nam, Ngày Báo chí Việt Nam, Ivy Lee, Google).
- **TH**: no case in Thai script; only Latin words normalised (SEO, PR, Ivy Lee, Pitch).
- Pill tags ≤3 words use title case; sub-texts, handwritten notes, reel frame text use sentence case; stat labels that continue a number stay lowercase.
- Rules live in `templates/casing.py` and are applied automatically at build time.
