"""Calendars (CSV/MD), grid previews, MASTER_calendar.csv and output/index.html."""
import os, json, glob, csv, html
from PIL import Image, ImageDraw

OUT = '/home/user/vritimes/output'
CCS = ['ID', 'MY', 'PH', 'SG', 'AU', 'TH', 'VN']
NAMES = {'ID': 'Indonesia', 'MY': 'Malaysia', 'PH': 'Philippines', 'SG': 'Singapore', 'AU': 'Australia', 'TH': 'Thailand', 'VN': 'Vietnam'}
COLS = ['date', 'day', 'local_time', 'platforms', 'pillar', 'format', 'title', 'hook', 'cta', 'post_id', 'folder', 'status']

def cover_of(d, fmt):
    return {'carousel': 'slides/01.png', 'single': 'image.png', 'reel': 'cover.png'}[fmt]

def load_posts(cc):
    ps = []
    for d in sorted(glob.glob(f'{OUT}/{cc}/{cc}_*')):
        pj = json.load(open(f'{d}/post.json')); pj['_dir'] = os.path.basename(d); ps.append(pj)
    return ps

def calendar(cc, posts):
    rows = []
    for p in posts:
        t = p['times']
        rows.append(dict(date=p['date'], day=p['day'], local_time=f"LinkedIn {t['linkedin']} | IG/FB {t['instagram_facebook']}",
                         platforms='Instagram; Facebook; LinkedIn', pillar=p['pillar'], format=p['format'], title=p['title'], hook=p['hook'],
                         cta=p['cta'], post_id=p['post_id'], folder=p['_dir'], status=p['status']))
    with open(f'{OUT}/{cc}/00_calendar_{cc}.csv', 'w', newline='', encoding='utf-8-sig') as f:
        w = csv.DictWriter(f, fieldnames=COLS); w.writeheader(); w.writerows(rows)
    md = [f'# {NAMES[cc]} — content calendar (16 Nov – 11 Dec 2026)', '', '| Date | Day | Time (local) | Pillar | Format | Title | Folder |', '|---|---|---|---|---|---|---|']
    for r in rows:
        md.append(f"| {r['date']} | {r['day']} | {r['local_time']} | {r['pillar']} | {r['format']} | {r['title']} | `{r['folder']}` |")
    open(f'{OUT}/{cc}/00_calendar_{cc}.md', 'w').write('\n'.join(md) + '\n')
    return [dict(country=cc, **r) for r in rows]

def grid(cc, posts):
    tw, th, gap = 360, 450, 6
    W = 3 * tw + 2 * gap; H = 4 * th + 3 * gap
    img = Image.new('RGB', (W, H), (255, 255, 255))
    for p_i, p in enumerate(reversed(posts)):  # newest top-left
        im = Image.open(f"{OUT}/{cc}/{p['_dir']}/{cover_of(p['_dir'], p['format'])}").convert('RGB')
        if im.height > 1350:  # reel cover: centre-crop to 4:5
            top = (im.height - 1350) // 2; im = im.crop((0, top, 1080, top + 1350))
        im = im.resize((tw, th))
        r, c = divmod(p_i, 3)
        img.paste(im, (c * (tw + gap), r * (th + gap)))
    img.save(f'{OUT}/{cc}/grid_preview_{cc}.png')

def index(allposts):
    data = {}
    for cc in CCS:
        items = []
        for p in allposts[cc]:
            d = f"{cc}/{p['_dir']}"
            if p['format'] == 'carousel':
                imgs = [f"{d}/slides/{f}" for f in sorted(os.listdir(f'{OUT}/{d}/slides'))]
            elif p['format'] == 'single':
                imgs = [f'{d}/image.png']
            else:
                imgs = [f'{d}/cover.png']
            cap = {k: open(f'{OUT}/{d}/caption_{k}.txt').read() for k in ('instagram', 'facebook', 'linkedin')}
            items.append(dict(id=p['post_id'], date=p['date'], day=p['day'], pillar=p['pillar'], format=p['format'], title=p['title'],
                              hook=p['hook'], cta=p['cta'], times=p['times'], dir=d, imgs=imgs, cap=cap,
                              sources=[dict(name=s['name'], title=s['title'], year=s['year'], url=s['url']) for s in p['sources']],
                              pdf=f'{d}/linkedin_carousel.pdf' if p['format'] == 'carousel' else None,
                              mp4=f'{d}/reel_draft.mp4' if p['format'] == 'reel' else None,
                              script=f'{d}/reel_script.md' if p['format'] == 'reel' else None,
                              price=p.get('price_status')))
        data[cc] = dict(name=NAMES[cc], grid=f'{cc}/grid_preview_{cc}.png', csv=f'{cc}/00_calendar_{cc}.csv', posts=items)
    tpl = open('/home/user/vritimes/templates/index_template.html').read()
    open(f'{OUT}/index.html', 'w').write(tpl.replace('/*__DATA__*/null', json.dumps(data, ensure_ascii=False)))

if __name__ == '__main__':
    master, allposts = [], {}
    for cc in CCS:
        ps = load_posts(cc); allposts[cc] = ps
        master += calendar(cc, ps); grid(cc, ps)
    with open(f'{OUT}/MASTER_calendar.csv', 'w', newline='', encoding='utf-8-sig') as f:
        w = csv.DictWriter(f, fieldnames=['country'] + COLS); w.writeheader(); w.writerows(master)
    index(allposts)
    print('posts:', len(master))
