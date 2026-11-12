"""VRITIMES slide templates: JSON slide spec -> standalone HTML (rendered by shoot.js)."""
import html, re, os

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CSS = os.path.join(ROOT, 'templates', 'base.css')
LOGO = os.path.join(ROOT, 'brand', 'logo', 'web')
SLOGAN = 'Raise It With Press Release'
CASE = {'lower': True}  # False = keep authored capitalisation (EYD / sentence case)

L = {
 'id': {'src': 'Sumber', 'swipe': 'geser →', 'save': 'simpan', 'url_pre': 'vritimes.com/id'},
 'en': {'src': 'Source', 'swipe': 'swipe →', 'save': 'save this'},
 'th': {'src': 'แหล่งที่มา', 'swipe': 'ปัดดูต่อ →', 'save': 'บันทึกไว้'},
 'vn': {'src': 'Nguồn', 'swipe': 'lướt tiếp →', 'save': 'lưu lại'},
}

def md(s):
    """mini markup: *x* = highlight, [x] = box highlight, **x** = bold, \n = br"""
    s = html.escape(s or '')
    s = re.sub(r'\*\*(.+?)\*\*', r'<b>\1</b>', s)
    s = re.sub(r'\*(.+?)\*', r'<span class="hl">\1</span>', s)
    s = re.sub(r'\[(.+?)\]', r'<span class="box">\1</span>', s)
    return s.replace('\n', '<br>')

FIT_JS = """
<script>
window.__warn=[];
window.__fit=function(){
 document.querySelectorAll('[data-fit]').forEach(function(box){
   var t=box.querySelector('.fitt')||box; var min=parseFloat(box.dataset.min||28);
   var fs=parseFloat(getComputedStyle(t).fontSize);
   var guard=0;
   while((box.scrollHeight>box.clientHeight+1||box.scrollWidth>box.clientWidth+1)&&fs>min&&guard<200){fs-=2;t.style.fontSize=fs+'px';guard++;}
   if(box.scrollHeight>box.clientHeight+1||box.scrollWidth>box.clientWidth+1){window.__warn.push('overflow:'+(t.textContent||'').slice(0,40));}
 });
 document.querySelectorAll('.body,.check,.cmp li').forEach(function(e){
   var f=parseFloat(getComputedStyle(e).fontSize); if(f<27.5) window.__warn.push('small:'+f+':'+(e.textContent||'').slice(0,30));});
};
</script>"""

def page(inner, theme, lang, reel=False, extra_cls=''):
    h = 1920 if reel else 1350
    langcls = {'th': 'lang-th', 'vn': 'lang-vn'}.get(lang, 'lang-lat')
    return f"""<!doctype html><html><head><meta charset="utf-8">
<link rel="stylesheet" href="file://{CSS}">
<style>html,body{{height:{h}px}}</style></head>
<body class="{langcls} {'reel' if reel else ''} {'' if CASE['lower'] else 'nolc'}"><div class="c t-{theme} {extra_cls}">{inner}</div>{FIT_JS}</body></html>"""

def logo_img(kind):
    return f'file://{LOGO}/{kind}.png'

def stamp():
    return f'<div class="stamp"><img src="{logo_img("stack_color")}"></div>'

def corner_logo(theme, right=False):
    k = 'beside_color' if theme == 'pale' else 'beside_white'
    return f'<img class="logo-corner{" right" if right else ""}" src="{logo_img(k)}">'

def sticker():
    return f'<div class="sticker">{SLOGAN}</div>'

def src_line(lang, src):
    if not src: return ''
    return f'<div class="src">{L[lang]["src"]}: {html.escape(src)}</div>'

def footer(cc):
    return (f'<div class="footer"><span class="url">vritimes.com/{cc.lower()}</span>'
            f'<span class="tag">{SLOGAN}</span><img src="{logo_img("beside_color")}"></div>')

# ---------- inline icons (flat, own drawings) ----------
ICONS = {
 'news': '<svg viewBox="0 0 100 100"><rect x="14" y="20" width="62" height="64" rx="8" fill="#0058F8"/><rect x="76" y="34" width="12" height="50" rx="6" fill="#071B6E"/><rect x="24" y="30" width="42" height="12" rx="3" fill="#fff"/><rect x="24" y="50" width="42" height="5" rx="2" fill="#E8F1FF"/><rect x="24" y="60" width="42" height="5" rx="2" fill="#E8F1FF"/><rect x="24" y="70" width="28" height="5" rx="2" fill="#E8F1FF"/></svg>',
 'mega': '<svg viewBox="0 0 100 100"><path d="M18 42h14l34-18v52L32 58H18z" fill="#0058F8"/><rect x="24" y="58" width="12" height="22" rx="5" fill="#071B6E"/><path d="M74 38q10 12 0 24" stroke="#D7F23C" stroke-width="6" fill="none" stroke-linecap="round"/><path d="M80 30q18 20 0 40" stroke="#00C8F8" stroke-width="6" fill="none" stroke-linecap="round"/></svg>',
 'chart': '<svg viewBox="0 0 100 100"><rect x="16" y="56" width="14" height="28" rx="4" fill="#00C8F8"/><rect x="38" y="42" width="14" height="42" rx="4" fill="#0098F8"/><rect x="60" y="24" width="14" height="60" rx="4" fill="#0058F8"/><path d="M14 40l24-14 18 10 28-20" stroke="#D7F23C" stroke-width="6" fill="none" stroke-linecap="round" stroke-linejoin="round"/></svg>',
 'mail': '<svg viewBox="0 0 100 100"><rect x="12" y="24" width="76" height="54" rx="10" fill="#0058F8"/><path d="M14 30l36 26 36-26" stroke="#fff" stroke-width="6" fill="none" stroke-linejoin="round"/><circle cx="80" cy="26" r="12" fill="#D7F23C"/></svg>',
 'link': '<svg viewBox="0 0 100 100"><rect x="10" y="38" width="46" height="26" rx="13" stroke="#0058F8" stroke-width="9" fill="none"/><rect x="44" y="38" width="46" height="26" rx="13" stroke="#00C8F8" stroke-width="9" fill="none"/></svg>',
 'clock': '<svg viewBox="0 0 100 100"><circle cx="50" cy="52" r="34" fill="#0058F8"/><path d="M50 32v22l14 8" stroke="#fff" stroke-width="7" fill="none" stroke-linecap="round"/><circle cx="50" cy="52" r="5" fill="#D7F23C"/></svg>',
 'cal': '<svg viewBox="0 0 100 100"><rect x="16" y="22" width="68" height="62" rx="10" fill="#0058F8"/><rect x="16" y="22" width="68" height="18" rx="9" fill="#071B6E"/><g fill="#fff"><rect x="26" y="50" width="10" height="10" rx="2"/><rect x="45" y="50" width="10" height="10" rx="2"/><rect x="64" y="50" width="10" height="10" rx="2" fill="#D7F23C"/><rect x="26" y="66" width="10" height="10" rx="2"/><rect x="45" y="66" width="10" height="10" rx="2"/></g></svg>',
 'eye': '<svg viewBox="0 0 100 100"><path d="M8 50q42-44 84 0q-42 44-84 0z" fill="#0058F8"/><circle cx="50" cy="50" r="16" fill="#fff"/><circle cx="50" cy="50" r="8" fill="#071B6E"/></svg>',
 'shield': '<svg viewBox="0 0 100 100"><path d="M50 12l32 12v24c0 20-14 34-32 40c-18-6-32-20-32-40V24z" fill="#0058F8"/><path d="M36 50l10 10 18-20" stroke="#D7F23C" stroke-width="7" fill="none" stroke-linecap="round" stroke-linejoin="round"/></svg>',
 'quote': '<svg viewBox="0 0 100 100"><path d="M20 60c0-18 8-30 24-34v10c-8 3-12 9-12 16h12v22H20zM56 60c0-18 8-30 24-34v10c-8 3-12 9-12 16h12v22H56z" fill="#0058F8"/></svg>',
 'train': '<svg viewBox="0 0 100 100"><rect x="22" y="16" width="56" height="56" rx="12" fill="#0058F8"/><rect x="30" y="26" width="40" height="20" rx="4" fill="#E8F1FF"/><circle cx="36" cy="60" r="5" fill="#D7F23C"/><circle cx="64" cy="60" r="5" fill="#D7F23C"/><path d="M30 86l10-14M70 86L60 72" stroke="#071B6E" stroke-width="6" stroke-linecap="round"/></svg>',
 'pdf': '<svg viewBox="0 0 100 100"><path d="M24 10h36l18 18v62H24z" fill="#fff" stroke="#071B6E" stroke-width="5"/><path d="M60 10v18h18" fill="none" stroke="#071B6E" stroke-width="5"/><rect x="14" y="52" width="52" height="24" rx="5" fill="#0058F8"/><text x="40" y="70" font-family="Poppins" font-weight="800" font-size="17" fill="#fff" text-anchor="middle">PDF</text></svg>',
}
def icon(name, size=120):
    return f'<span style="display:inline-block;width:{size}px;height:{size}px">{ICONS.get(name, ICONS["news"])}</span>'

# ---------- illustrations for type-c tiles ----------
def art_frames(icons, top=880):
    xs = [90, 435, 780]; rots = [-7, 4, -3]
    out = f'<svg class="string" style="top:{top-40}px" viewBox="0 0 1120 300" preserveAspectRatio="none"><path d="M0 40 Q560 140 1120 30" stroke="#071B6E" stroke-width="5" fill="none"/></svg>'
    for i, ic in enumerate(icons[:3]):
        y = top + (36 if i == 1 else 4)
        out += (f'<div class="frame" style="left:{xs[i]}px;top:{y}px;transform:rotate({rots[i]}deg)"><div class="clip"></div>'
                f'<div class="ph">{icon(ic,150)}</div></div>')
    return out

def art_doc(top=640, rot=-8):
    lines = '<div class="ln b"></div>' + ''.join('<div class="ln{}"></div>'.format(' s' if i % 3 == 2 else '') for i in range(8))
    return (f'<div class="doc" style="left:300px;top:{top}px;width:560px;height:640px;transform:rotate({rot}deg)">{lines}'
            f'<div style="position:absolute;right:-40px;bottom:60px">{icon("mega",170)}</div></div>')

def ribbon(top=1040, color='#D7F23C'):
    return (f'<svg class="ribbon" style="top:{top}px" viewBox="0 0 1200 180" preserveAspectRatio="none">'
            f'<path d="M0 120 C200 20 380 170 600 90 S1000 10 1200 80" stroke="#071B6E" stroke-width="46" fill="none" stroke-linecap="round"/>'
            f'<path d="M0 120 C200 20 380 170 600 90 S1000 10 1200 80" stroke="{color}" stroke-width="30" fill="none" stroke-linecap="round" stroke-dasharray="70 40"/></svg>')

# ---------- slide builders ----------
def s_cover(sp, lang, cc, variant='a', is_reel=False, counter=None):
    theme = {'a': 'blue', 'b': 'pale', 'c': 'blue'}[variant]
    if sp.get('theme'): theme = sp['theme']
    tag = f'<div style="margin-bottom:34px"><span class="pill">{html.escape(sp.get("tag",""))}</span></div>' if sp.get('tag') else ''
    sub = f'<div style="margin-top:38px"><span class="pill lime r">{html.escape(sp["sub"])}</span></div>' if sp.get('sub') else ''
    hsize = sp.get('size', 150 if not is_reel else 160)
    if variant == 'c' and not is_reel:
        art = art_frames(sp.get('icons', ['news', 'mega', 'chart'])) if sp.get('art', 'frames') == 'frames' else art_doc()
        inner = (f'<div class="safe" style="bottom:auto;height:640px;justify-content:center;align-items:center;text-align:center" data-fit data-min="70">'
                 f'<div class="fitt" style="font-size:{min(hsize,130)}px">{tag}<div class="h lc">{md(sp["title"])}</div>{sub}</div></div>' + art)
        extra = 'skyart'
    else:
        top, bottom = (300, 480) if is_reel else (150, 150)
        inner = (f'<div class="safe center" style="top:{top}px;bottom:{bottom}px" data-fit data-min="70">'
                 f'<div class="fitt" style="font-size:{hsize}px">{tag}<div class="h lc">{md(sp["title"])}</div>{sub}</div></div>')
        extra = ''
    inner += (stamp().replace('class="stamp"', 'class="stamp" style="top:255px"') if is_reel else stamp()) + sticker()
    if is_reel: inner += '<div class="reelicon" style="top:310px;right:auto;left:60px"></div>'
    elif sp.get('swipe', True): inner += f'<div class="swipe">{L[lang]["swipe"]}</div>'
    if sp.get('src'): inner += src_line(lang, sp['src'])
    style = ''
    if variant == 'c' and not is_reel:
        style = '<style>.skyart{background:linear-gradient(160deg,#00C8F8 0%,#0098F8 45%,#0058F8 100%)!important}.skyart::before{display:none}.skyart .h{color:#fff}.skyart .hl{color:var(--navy)!important}</style>'
    return page(style + inner, theme, lang, reel=is_reel, extra_cls=extra)

SERIES = {'v': ''}
def _count(i, n):
    ser = f'<span class="pill" style="position:absolute;left:190px;top:50px;font-size:30px;padding:9px 20px 11px;z-index:4">{html.escape(SERIES["v"])}</span>' if SERIES['v'] else ''
    return f'<div class="counter">{i:02d}/{n:02d}</div>' + ser

def s_point(sp, lang, cc, i, n, theme):
    note = f'<div class="note" style="margin-top:30px">{md(sp["note"])}</div>' if sp.get('note') else ''
    num = f'<div class="big-n" style="margin-bottom:26px">{html.escape(str(sp["n"]))}</div>' if sp.get('n') is not None else ''
    if sp.get('ex'):
        lab = sp.get('exlab', {'id':'contoh','th':'ตัวอย่าง','vn':'ví dụ'}.get(lang,'example'))
        note += (f'<div class="card" style="margin-top:34px;font-size:.9em"><div style="margin-bottom:12px"><span class="pill lime" style="transform:rotate(-2deg)">{html.escape(lab)}</span></div>'
                 f'<div class="body" style="font-size:inherit;color:var(--navy)">{md(sp["ex"])}</div></div>')
    icobg = 'background:#fff;border-radius:34px;padding:16px;display:inline-block;' if theme != 'pale' else ''
    ico = f'<div style="margin-bottom:24px"><span style="{icobg}">{icon(sp["icon"],130)}</span></div>' if sp.get('icon') else ''
    inner = (_count(i, n) + corner_logo(theme, right=True) +
             f'<div class="safe" style="justify-content:center" data-fit data-min="28"><div class="fitt" style="font-size:{sp.get("bsize",40)}px">'
             f'{ico}{num}<div class="h lc" style="font-size:{sp.get("tsize",84)}px;margin-bottom:34px">{md(sp["title"])}</div>'
             f'<div class="body" style="font-size:inherit">{md(sp.get("body",""))}</div>{note}</div></div>' +
             src_line(lang, sp.get('src')))
    return page(inner, theme, lang)

def s_stat(sp, lang, cc, i, n, theme):
    inner = (_count(i, n) + corner_logo(theme, right=True) +
             f'<div class="safe center" data-fit data-min="28"><div class="fitt" style="font-size:38px">'
             f'{f"<div style=margin-bottom:30px><span class=pill>{html.escape(sp[chr(116)+chr(97)+chr(103)])}</span></div>" if sp.get("tag") else ""}'
             f'<div class="h" style="font-size:{sp.get("bsize",260)}px;line-height:.9"><span class="hl">{html.escape(sp["big"])}</span></div>'
             f'<div class="h lc" style="font-size:{sp.get("lsize",64)}px;margin:28px 0 30px">{md(sp["label"])}</div>'
             f'<div class="body" style="font-size:inherit;max-width:860px;margin:0 auto">{md(sp.get("body",""))}</div></div></div>' +
             src_line(lang, sp.get('src')))
    return page(inner, theme, lang)

def s_list(sp, lang, cc, i, n, theme):
    items = ''.join(f'<div class="check{" hot" if it.startswith("!") else ""}{" x" if it.startswith("~") else ""}"><i>{"✕" if it.startswith("~") else "✓"}</i><span>{md(it.lstrip("!~"))}</span></div>' for it in sp['items'])
    intro = f'<div class="body" style="font-size:32px;margin-bottom:30px">{md(sp["intro"])}</div>' if sp.get('intro') else ''
    inner = (_count(i, n) + corner_logo(theme, right=True) +
             f'<div class="safe" style="justify-content:center" data-fit data-min="28"><div class="fitt" style="font-size:{sp.get("bsize",34)}px">'
             f'<div class="h lc" style="font-size:{sp.get("tsize",80)}px;margin-bottom:30px">{md(sp["title"])}</div>{intro}'
             f'<div class="checks" style="font-size:inherit">{items}</div></div></div>' + src_line(lang, sp.get('src')))
    inner = inner.replace('class="check', 'style="font-size:inherit" class="check')
    return page(inner, theme, lang)

def s_compare(sp, lang, cc, i, n, theme):
    def col(c, k):
        return f'<div class="col {k}"><h4>{md(c["h"])}</h4><ul>' + ''.join(f'<li>{md(x)}</li>' for x in c['items']) + '</ul></div>'
    inner = (_count(i, n) + corner_logo(theme, right=True) +
             f'<div class="safe" style="justify-content:center" data-fit data-min="28"><div class="fitt">'
             f'<div class="h lc" style="font-size:{sp.get("tsize",80)}px;margin-bottom:36px">{md(sp["title"])}</div>'
             f'<div class="cmp">{col(sp["left"],"bad")}{col(sp["right"],"good")}</div></div></div>' + src_line(lang, sp.get('src')))
    return page(inner, theme, lang)

def s_quote(sp, lang, cc, i, n, theme):
    inner = (_count(i, n) + corner_logo(theme, right=True) +
             f'<div class="safe center" data-fit data-min="40"><div class="fitt" style="font-size:{sp.get("size",92)}px">'
             f'<div style="margin-bottom:20px">{icon("quote",110)}</div><div class="h">{md(sp["text"])}</div>'
             f'{f"<div class=note style=margin-top:40px>{md(sp[chr(98)+chr(121)])}</div>" if sp.get("by") else ""}</div></div>' + src_line(lang, sp.get('src')))
    return page(inner, theme, lang)

def s_cta(sp, lang, cc, i, n, theme='navy'):
    items = ''.join(f'<div class="check hot"><i>{k+1}</i><span>{md(it)}</span></div>' for k, it in enumerate(sp.get('items', [])))
    srcs = ''.join(f'<div>· {html.escape(s)}</div>' for s in sp.get('sources', []))
    srcblock = f'<div class="src" style="position:static;margin-top:34px">{L[lang]["src"]}:{srcs}</div>' if srcs else ''
    inner = (_count(i, n) + stamp() +
             f'<div class="safe" style="justify-content:center;bottom:150px" data-fit data-min="24"><div class="fitt" style="font-size:32px">'
             f'<div class="h lc" style="font-size:{sp.get("tsize",96)}px;margin-bottom:34px">{md(sp["title"])}</div>'
             f'<div class="checks">{items}</div>{srcblock}</div></div>' + footer(cc))
    inner = inner.replace('class="check hot"', 'style="font-size:inherit" class="check hot"')
    return page(inner, theme, lang)

def s_promo(sp, lang, cc, theme='blue'):
    items = ''.join(f'<div class="check hot" style="font-size:inherit"><i>✓</i><span>{md(it)}</span></div>' for it in sp.get('items', []))
    price = f'<div style="margin-top:34px"><span class="pill lime" style="font-family:var(--head);font-weight:800;font-size:44px;transform:rotate(-2deg)">{html.escape(sp["price"])}</span></div>' if sp.get('price') else ''
    tag = f'<div style="margin-bottom:28px"><span class="pill white">{html.escape(sp["tag"])}</span></div>' if sp.get('tag') else ''
    inner = (stamp() +
             f'<div class="safe" style="justify-content:center;top:170px;bottom:170px" data-fit data-min="28"><div class="fitt" style="font-size:32px">{tag}'
             f'<div class="h lc" style="font-size:{sp.get("tsize",112)}px;margin-bottom:36px">{md(sp["title"])}</div>'
             f'<div class="checks">{items}</div>{price}'
             f'<div class="src" style="position:static;margin-top:30px">{L[lang]["src"]}: {html.escape(sp.get("src",""))}</div></div></div>' +
             (ribbon(sp.get('ribbon_top', 1075)) if sp.get('ribbon') else '') + footer(cc))
    return page(inner, theme, lang)

def s_single_stat(sp, lang, cc, theme='pale'):
    tag = f'<div style="margin-bottom:30px"><span class="pill">{html.escape(sp["tag"])}</span></div>' if sp.get('tag') else ''
    inner = (stamp() + sticker() +
             f'<div class="safe center" data-fit data-min="28"><div class="fitt" style="font-size:34px">{tag}'
             f'<div class="h lc" style="font-size:{sp.get("tsize",70)}px;margin-bottom:10px">{md(sp.get("pre",""))}</div>'
             f'<div class="h" style="font-size:{sp.get("bsize",280)}px;line-height:.92"><span class="hl">{html.escape(sp["big"])}</span></div>'
             f'<div class="h lc" style="font-size:{sp.get("lsize",70)}px;margin:22px 0 34px">{md(sp["label"])}</div>'
             f'<div class="body" style="font-size:inherit;max-width:840px;margin:0 auto">{md(sp.get("body",""))}</div>'
             f'{f"<div style=margin-top:30px><span class=pill lime r>{html.escape(sp[chr(115)+chr(117)+chr(98)])}</span></div>" if sp.get("sub") else ""}</div></div>' +
             src_line(lang, sp.get('src')))
    return page(inner, theme, lang)

def s_reel_frame(sp, lang, cc, k, n, theme):
    prog = f'<div style="position:absolute;left:84px;right:84px;top:200px;height:10px;border-radius:5px;background:rgba(255,255,255,.25)"><div style="width:{int(100*k/n)}%;height:100%;border-radius:5px;background:var(--lime)"></div></div>'
    if theme == 'pale': prog = prog.replace('rgba(255,255,255,.25)', 'rgba(0,88,248,.15)').replace('var(--lime)', 'var(--blue)')
    top = f'<div style="margin-bottom:40px"><span class="pill{" lime" if theme!="pale" else ""}">{html.escape(sp["top"])}</span></div>' if sp.get('top') else ''
    icobg = 'background:#fff;border-radius:44px;padding:20px;display:inline-block;' if theme != 'pale' else ''
    ico = f'<div style="margin-bottom:30px"><span style="{icobg}">{icon(sp["icon"],200)}</span></div>' if sp.get('icon') else ''
    sub = f'<div class="note" style="margin-top:44px;font-size:52px">{md(sp["sub"])}</div>' if sp.get('sub') else ''
    inner = (prog + corner_logo(theme) +
             f'<div class="safe center" style="top:300px;bottom:460px" data-fit data-min="44"><div class="fitt" style="font-size:{sp.get("size",112)}px">'
             f'{top}{ico}<div class="h lc">{md(sp["text"])}</div>{sub}</div></div>' + (src_line(lang, sp.get('src')).replace('class="src"', 'class="src" style="bottom:420px"') if sp.get('src') else ''))
    return page(inner, theme, lang, reel=True)
