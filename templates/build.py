"""Build pipeline: content/{CC}.py -> output/{CC}/... (slides, pdf, captions, sources, post.json, reels).
usage: python3 templates/build.py ID [MY ...]   (or 'all')
"""
import sys, os, json, importlib.util, subprocess, datetime, shutil, csv
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import engine as E
import sources as SRC
import casing
E.CASE['lower'] = False  # headlines carry their own capitalisation (see casing.py)
from PIL import Image

ROOT = E.ROOT
OUT = os.path.join(ROOT, 'output')
TMP = os.environ.get('VR_TMP', '/tmp/vr_build')
START = datetime.date(2026, 11, 16)
SLOTS = {  # slot -> day offset from START
 'W1Mon': 0, 'W1Wed': 2, 'W1Fri': 4, 'W2Mon': 7, 'W2Wed': 9, 'W2Fri': 11,
 'W3Mon': 14, 'W3Wed': 16, 'W3Fri': 18, 'W4Mon': 21, 'W4Wed': 23, 'W4Fri': 25}
ORDER = list(SLOTS)
FMT = {'carousel': 'carousel', 'reel': 'reels', 'single': 'single'}

def load(cc):
    p = os.path.join(ROOT, 'content', f'{cc}.py')
    spec = importlib.util.spec_from_file_location(cc, p); m = importlib.util.module_from_spec(spec); spec.loader.exec_module(m)
    return m

def grid_variant(idx):
    """idx = chronological 0..11. Grid shows newest top-left -> position p = 11-idx.
    Diagonal checkerboard of 3 tile types a/b/c."""
    p = 11 - idx; r, c = divmod(p, 3)
    return 'abc'[(c - r) % 3]

def folder_name(cc, post, d):
    return f"{cc}_{d.isoformat()}_{d.strftime('%a')}_{post['pillar']}_{FMT[post['format']]}_{post['slug']}"

def post_id(cc, post, d):
    return f"{cc.lower()}_{d.strftime('%Y%m%d')}_{post['pillar'].lower()}"

def utm(cc, src, pid, d, path=''):
    return (f"https://www.vritimes.com/{cc.lower()}{path}?utm_source={src}&utm_medium=organic_social"
            f"&utm_campaign=sns_{cc.lower()}_{d.strftime('%Y%m')}&utm_content={pid}")

# ---------------- captions ----------------
CAPL = {
 'id': dict(src='Sumber', ig_cta='Simpan post ini & kirim ke tim marketing/PR kamu. Link di bio.', link='Selengkapnya',
            li_link='Pelajari VRITIMES', fb_cta='Simpan dan bagikan ke tim Anda 👇'),
 'en': dict(src='Sources', ig_cta='Save this and send it to your PR person. Link in bio.', link='Learn more',
            li_link='More on VRITIMES', fb_cta='Save it and share it with your team 👇'),
 'th': dict(src='แหล่งที่มา', ig_cta='กดบันทึกไว้ แล้วส่งต่อให้ทีมการตลาด/PR ของคุณ ลิงก์อยู่ในไบโอ', link='ดูเพิ่มเติม',
            li_link='ข้อมูลเพิ่มเติมเกี่ยวกับ VRITIMES', fb_cta='บันทึกไว้และแชร์ให้ทีมของคุณ 👇'),
 'vn': dict(src='Nguồn', ig_cta='Lưu bài này và gửi cho người phụ trách PR của bạn. Link ở bio.', link='Xem thêm',
            li_link='Tìm hiểu VRITIMES', fb_cta='Lưu lại và chia sẻ cho đội ngũ của bạn 👇'),
}

def src_lines(keys, cc, style='short'):
    out = []
    for k in keys:
        s = SRC.get(k, cc)
        out.append(f"{s['name']}, {s['title']} ({s['year']}) — {s['url']}" if style == 'full' else f"{s['short']} — {s['url']}")
    return out

def captions(meta, post, cc, pid, d):
    lang = meta.LANG; c = post['cap']; CL = CAPL[lang]
    tags = post.get('tags', [])
    ig_tags = (['#VRITIMES'] + tags + meta.TAGS)[:6]
    li_tags = (['#VRITIMES'] + tags + meta.TAGS)[:5]
    fb_tags = (['#VRITIMES'] + tags)[:3]
    srcs = src_lines(post['src'], cc)
    # Instagram
    ig = [c['hook'], ''] + c['lines'] + ['', c.get('ig_cta', CL['ig_cta']), '', ' '.join(ig_tags), '', f"{CL['src']}:"] + [f"• {s.split(' — ')[0]}" for s in srcs]
    # Facebook
    fb = [c.get('fb', c['hook']), ''] + c['lines'] + ['', c.get('fb_cta', CL['fb_cta']),
          f"{CL['link']}: {utm(cc,'facebook',pid,d)}", '', ' '.join(fb_tags), '', f"{CL['src']}:"] + [f"• {s}" for s in srcs]
    # LinkedIn
    pts = [f"{i+1}. {p}" for i, p in enumerate(c.get('li_points', []))]
    li = [c['li_hook'], ''] + c['li_body'] + ([''] + pts if pts else []) + ['', c['li_close'], '',
          f"{CL['li_link']}: {utm(cc,'linkedin',pid,d)}", '', ' '.join(li_tags), '', f"{CL['src']}:"] + [f"• {s}" for s in srcs]
    j = lambda xs: '\n'.join(xs).replace('\n\n\n', '\n\n').strip() + '\n'
    return j(ig), j(fb), j(li)

# ---------------- slides ----------------
def slide_html(sp, lang, cc, i, n, variant, kind):
    t = sp['t']; theme = sp.get('theme')
    if t == 'cover': return E.s_cover(sp, lang, cc, variant, is_reel=(kind == 'reelcover'))
    if t == 'point': return E.s_point(sp, lang, cc, i, n, theme or 'pale')
    if t == 'stat': return E.s_stat(sp, lang, cc, i, n, theme or 'blue')
    if t == 'list': return E.s_list(sp, lang, cc, i, n, theme or 'pale')
    if t == 'compare': return E.s_compare(sp, lang, cc, i, n, theme or 'blue')
    if t == 'quote': return E.s_quote(sp, lang, cc, i, n, theme or 'blue')
    if t == 'cta': return E.s_cta(sp, lang, cc, i, n, theme or 'navy')
    if t == 'promo': return E.s_promo(sp, lang, cc, theme or ('blue' if variant != 'b' else 'navy'))
    if t == 'single_stat': return E.s_single_stat(sp, lang, cc, theme or {'a': 'blue', 'b': 'pale', 'c': 'sky'}[variant])
    raise ValueError(t)

def build(cc, only=None, render=True):
    meta = load(cc); lang = meta.LANG
    base = os.path.join(OUT, cc); os.makedirs(base, exist_ok=True)
    tmp = os.path.join(TMP, cc); shutil.rmtree(tmp, ignore_errors=True); os.makedirs(tmp)
    jobs, posts_out, post_jobs = [], [], []
    for idx, post in enumerate(meta.POSTS):
        post = casing.apply(post, lang)
        slot = ORDER[idx]; assert post['slot'] == slot, (cc, post['slot'], slot)
        d = START + datetime.timedelta(days=SLOTS[slot])
        fn = folder_name(cc, post, d); pid = post_id(cc, post, d); pdir = os.path.join(base, fn)
        if only and only not in fn: continue
        # remove stale folders of same slot
        for old in os.listdir(base):
            if old.startswith(f"{cc}_{d.isoformat()}_") and old != fn: shutil.rmtree(os.path.join(base, old))
        os.makedirs(pdir, exist_ok=True)
        variant = post.get('grid') or grid_variant(idx)
        # slides
        slides = post.get('slides', [])
        fmt = post['format']
        if fmt == 'carousel':
            sd = os.path.join(pdir, 'slides'); shutil.rmtree(sd, ignore_errors=True); os.makedirs(sd)
            n = len(slides)
            E.SERIES['v'] = slides[0].get('tag', '') if slides[0]['t'] == 'cover' else ''
            # alternate inner themes for rhythm
            for i, sp in enumerate(slides, 1):
                if i > 1 and sp['t'] in ('point', 'list') and not sp.get('theme'):
                    sp = dict(sp, theme='pale' if i % 2 == 0 else 'blue')
                h = slide_html(sp, lang, cc, i, n, variant, 'slide')
                hp = os.path.join(tmp, f'{fn}_{i:02d}.html'); open(hp, 'w').write(h)
                jobs.append(dict(html=hp, png=os.path.join(sd, f'{i:02d}.png'), w=1080, h=1350))
        elif fmt == 'single':
            h = slide_html(slides[0], lang, cc, 1, 1, variant, 'single')
            hp = os.path.join(tmp, f'{fn}_single.html'); open(hp, 'w').write(h)
            jobs.append(dict(html=hp, png=os.path.join(pdir, 'image.png'), w=1080, h=1350))
        elif fmt == 'reel':
            cov = dict(slides[0]); h = E.s_cover(cov, lang, cc, variant if variant != 'c' else 'a', is_reel=True)
            if variant == 'b': h = E.s_cover(cov, lang, cc, 'b', is_reel=True)
            hp = os.path.join(tmp, f'{fn}_cover.html'); open(hp, 'w').write(h)
            jobs.append(dict(html=hp, png=os.path.join(pdir, 'cover.png'), w=1080, h=1920))
            fd = os.path.join(tmp, f'{fn}_frames'); os.makedirs(fd, exist_ok=True)
            fr = post['reel']['frames']
            for k, f in enumerate(fr, 1):
                th = f.get('theme', ['blue', 'pale', 'navy'][k % 3])
                h = E.s_reel_frame(f, lang, cc, k, len(fr), th)
                hp = os.path.join(fd, f'{k:02d}.html'); open(hp, 'w').write(h)
                jobs.append(dict(html=hp, png=os.path.join(fd, f'{k:02d}.png'), w=1080, h=1920))
        post_jobs.append((post, pdir, fn, pid, d, variant))
    if render and jobs:
        mf = os.path.join(tmp, 'manifest.json'); json.dump(jobs, open(mf, 'w'))
        r = subprocess.run(['node', os.path.join(ROOT, 'templates', 'shoot.js'), mf], capture_output=True, text=True, cwd='/tmp')
        print(r.stdout.strip()[-3000:], r.stderr.strip()[-2000:])
    for post, pdir, fn, pid, d, variant in post_jobs:
        finish_post(meta, cc, post, pdir, fn, pid, d, variant, tmp)
        posts_out.append(fn)
    return posts_out

def finish_post(meta, cc, post, pdir, fn, pid, d, variant, tmp):
    lang = meta.LANG; fmt = post['format']
    if fmt == 'carousel':
        sd = os.path.join(pdir, 'slides'); imgs = [Image.open(os.path.join(sd, f)).convert('RGB') for f in sorted(os.listdir(sd))]
        imgs[0].save(os.path.join(pdir, 'linkedin_carousel.pdf'), save_all=True, append_images=imgs[1:], resolution=144, quality=92)
    if fmt == 'reel':
        make_reel(post, pdir, fn, tmp, lang)
    ig, fb, li = captions(meta, post, cc, pid, d)
    open(os.path.join(pdir, 'caption_instagram.txt'), 'w').write(ig)
    open(os.path.join(pdir, 'caption_facebook.txt'), 'w').write(fb)
    open(os.path.join(pdir, 'caption_linkedin.txt'), 'w').write(li)
    # sources.md
    lines = [f"# Sources — {fn}", '', f"Access date: {SRC.ACCESS}", '', '| Name | Title | Year | URL |', '|---|---|---|---|']
    for k in post['src']:
        s = SRC.get(k, cc); lines.append(f"| {s['name']} | {s['title']} | {s['year']} | {s['url']} |")
    if post.get('src_note'): lines += ['', post['src_note']]
    open(os.path.join(pdir, 'sources.md'), 'w').write('\n'.join(lines) + '\n')
    # post.json
    pj = dict(post_id=pid, country=cc, language=lang, date=d.isoformat(), day=d.strftime('%a'), slot=post['slot'],
              pillar=post['pillar'], format=fmt, grid_tile=variant, slug=post['slug'], title=post['title'],
              hook=post['cap']['hook'], cta=post['cta'], times=meta.times(post['pillar']),
              platforms=['instagram', 'facebook', 'linkedin'], status='ready_for_review',
              links={p: utm(cc, p, pid, d) for p in ('instagram', 'facebook', 'linkedin')},
              sources=[SRC.get(k, cc) for k in post['src']], slides=post.get('slides'), reel=post.get('reel'), captions_meta=post['cap'],
              tags=post.get('tags', []), price_status='PRICE_UNVERIFIED' if post['pillar'] == 'PROMO' else None)
    json.dump(pj, open(os.path.join(pdir, 'post.json'), 'w'), ensure_ascii=False, indent=2)

def make_reel(post, pdir, fn, tmp, lang):
    r = post['reel']; fd = os.path.join(tmp, f'{fn}_frames'); fr = r['frames']
    # script
    t = 0.0; rows = []
    for k, f in enumerate(fr, 1):
        dur = f.get('dur', 3.0)
        rows.append(f"| {t:04.1f}–{t+dur:04.1f}s | {f.get('shot','Kinetic text card')} | {f['text'].replace(chr(10),' ').replace('*','').replace('[','').replace(']','')} | {r['vo'][k-1] if k-1 < len(r['vo']) else ''} |")
        t += dur
    md = [f"# Reel script — {fn}", '', f"**Length:** ~{t:.0f}s · **Format:** 1080×1920 · **Safe zone:** text between y=250 and y=1520",
          f"**Audio type suggestion:** {r['audio']} (pick from the platform's licensed library; no copyrighted track is embedded in the draft)", '',
          '| Time | Shot | On-screen text | Voice-over (optional) |', '|---|---|---|---|'] + rows + ['', '## B-roll / footage list'] + [f"- {b}" for b in r['broll']] + \
         ['', '## Notes', '- `reel_draft.mp4` is a silent kinetic-text draft built from the on-screen text cards; replace cards with real footage where listed.',
          '- Cover: `cover.png` (key text stays inside the 4:5 grid crop).']
    open(os.path.join(pdir, 'reel_script.md'), 'w').write('\n'.join(md) + '\n')
    # mp4 via ffmpeg xfade
    durs = [f.get('dur', 3.0) for f in fr]; xf = 0.35
    inputs = []
    for k, dur in enumerate(durs, 1):
        inputs += ['-loop', '1', '-t', f'{dur + xf:.2f}', '-i', os.path.join(fd, f'{k:02d}.png')]
    fc = []; last = '0:v'; off = 0.0
    for k in range(1, len(durs)):
        off += durs[k - 1]
        out = f'v{k}'
        fc.append(f'[{last}][{k}:v]xfade=transition=slideleft:duration={xf}:offset={off - xf*0:.2f}[{out}]')
        last = out
    fc.append(f'[{last}]format=yuv420p,scale=1080:1920[vout]')
    cmd = ['ffmpeg', '-y', '-loglevel', 'error'] + inputs + ['-filter_complex', ';'.join(fc), '-map', '[vout]', '-r', '30',
           '-c:v', 'libx264', '-preset', 'veryfast', '-crf', '22', '-t', f'{sum(durs):.2f}', os.path.join(pdir, 'reel_draft.mp4')]
    p = subprocess.run(cmd, capture_output=True, text=True)
    if p.returncode: print('FFMPEG ERR', fn, p.stderr[-800:])

if __name__ == '__main__':
    args = sys.argv[1:]
    ccs = ['ID', 'MY', 'PH', 'SG', 'AU', 'TH', 'VN'] if args and args[0] == 'all' else [a for a in args if not a.startswith('--')]
    only = next((a[7:] for a in args if a.startswith('--only=')), None)
    for cc in ccs:
        print('==', cc, build(cc, only=only))
