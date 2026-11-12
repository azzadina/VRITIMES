"""Headline capitalisation per language.
ID: EYD V judul — huruf kapital tiap kata kecuali kata tugas yang tidak di posisi awal.
EN (MY/PH/SG/AU): AP-style title case (short articles/conjunctions/prepositions lowercase).
VN: sentence case (Vietnamese headline convention) + proper nouns.
TH: Thai has no case; only Latin words are normalised (first letter + proper nouns/acronyms).
Markup (*x*, [x], \n) is preserved. Authored capitals are never lowered."""
import re, copy

SMALL = {
 'id': {'di', 'ke', 'dari', 'dan', 'yang', 'untuk', 'atau', 'pada', 'dengan', 'dalam', 'oleh', 'bagi', 'tentang', 'kepada',
        'sebagai', 'per', 'vs', 'x', 'demi', 'tapi', 'pun', 'sih', 'ya', 'aja', 'sampai', 'sebelum', 'setelah', 'agar', 'karena',
        'jika', 'kalau', 'bahwa', 'hingga', 'tanpa', 'seperti', 'antara', 'atas', 'lah', 'kah'},
 'en': {'a', 'an', 'the', 'and', 'but', 'or', 'nor', 'for', 'so', 'yet', 'as', 'at', 'by', 'in', 'of', 'on', 'to', 'via',
        'vs', 'per', 'x', 'if', 'na', 'daw', 'ng', 'po', 'pa'},
}
FIX = {  # lower-case core word -> correct form (applied in every mode)
 'google': 'Google', 'ivy': 'Ivy', 'lee': 'Lee', 'seo': 'SEO', 'pr': 'PR', 'umkm': 'UMKM', 'pdf': 'PDF', 'ave': 'AVE',
 'australia': 'Australia', 'australians': 'Australians', 'australian': 'Australian', 'filipinos': 'Filipinos',
 'indonesia': 'Indonesia', 'malaysia': 'Malaysia', "malaysia's": "Malaysia's", 'malaysians': 'Malaysians', 'philippine': 'Philippine',
 'philippines': 'Philippines', 'singapore': 'Singapore', 'thailand': 'Thailand', 'october': 'October', 'oktober': 'Oktober',
 'december': 'December', 'january': 'January', 'english': 'English', 'bahasa': 'Bahasa', 'tết': 'Tết', 'linkedin': 'LinkedIn',
 'tiktok': 'TikTok', 'jan–mar': 'Jan–Mar', 'apr–jun': 'Apr–Jun', 'jul–sep': 'Jul–Sep', 'oct–dec': 'Oct–Dec', 'okt–des': 'Okt–Des',
 'pov': 'POV', 'q1': 'Q1', 'q2': 'Q2', 'q3': 'Q3', 'q4': 'Q4',
}
PHRASES = [(re.compile(r'\bviệt nam\b'), 'Việt Nam'), (re.compile(r'\bnew york times\b'), 'New York Times')]
TOKEN = re.compile(r'[^\s]+')

def _up_first(tok):
    for i, ch in enumerate(tok):
        if ch.isalpha():
            return tok[:i] + ch.upper() + tok[i + 1:]
        if ch.isdigit():
            return tok
    return tok

def _core(tok):
    return re.sub(r'^[^\w]+|[^\w\'’–@=]+$', '', tok).lower()

def recase(text, lang, mode):
    """mode: 'title' | 'sentence' | 'keep' (proper nouns only, e.g. labels that continue a number)."""
    if not text:
        return text
    lines = text.split('\n'); out = []
    sentence_start = True
    for li, line in enumerate(lines):
        toks = []
        for m in TOKEN.finditer(line):
            tok = m.group(0); core = _core(tok); res = tok
            if '=' in tok or '@' in tok or not core:
                pass
            elif core in FIX:
                i = tok.lower().find(core); res = tok[:i] + FIX[core] + tok[i + len(core):] if i >= 0 else tok
            elif tok.startswith('…'):
                pass
            elif mode == 'title' and lang in ('id', 'en'):
                if sentence_start or core not in SMALL[lang]:
                    res = _up_first(tok)
                    if lang == 'en' and '-' in res:  # AP/Chicago: capitalise each part of a hyphenated compound
                        res = '-'.join(_up_first(x) if x.lower() not in SMALL['en'] else x for x in res.split('-'))
            elif mode in ('title', 'sentence') and sentence_start:
                res = _up_first(tok)
            toks.append((m.start(), m.end(), res))
            if core:
                sentence_start = bool(re.search(r'[.?!:]\**\]?["”]?$' if mode == 'title' else r'[.?!]\**\]?["”]?$', tok))
        # rebuild preserving spacing
        s, pos = '', 0
        for a, b, r in toks:
            s += line[pos:a] + r; pos = b
        s += line[pos:]
        out.append(s)
    res = '\n'.join(out)
    for rx, rep in PHRASES:
        res = rx.sub(rep, res)
    return res

def tag_mode(text):
    return 'title' if len((text or '').split()) <= 3 else 'sentence'

def apply(post, lang):
    """Return a deep copy of post with headline fields recased."""
    p = copy.deepcopy(post)
    L = 'id' if lang == 'id' else ('en' if lang == 'en' else lang)
    H = 'title' if L in ('id', 'en') else 'sentence'   # headline mode
    R = lambda t, m: recase(t, L, m)
    for s in p.get('slides', []):
        t = s['t']
        if s.get('tag'): s['tag'] = recase(s['tag'], 'en' if L == 'th' else L, tag_mode(s['tag']) if L in ('id', 'en', 'th') else 'sentence')
        if t in ('cover', 'point', 'list', 'compare', 'cta', 'promo') and s.get('title'): s['title'] = R(s['title'], H)
        if s.get('sub'): s['sub'] = R(s['sub'], 'sentence')
        if s.get('note'): s['note'] = R(s['note'], 'sentence')
        if s.get('price'): s['price'] = R(s['price'], 'sentence')
        if s.get('pre'): s['pre'] = R(s['pre'], 'sentence')
        if s.get('label'): s['label'] = R(s['label'], 'keep')
        if t == 'quote': s['text'] = R(s['text'], 'keep')
        if t == 'compare':
            for k in ('left', 'right'): s[k]['h'] = R(s[k]['h'], 'sentence')
    for f in (p.get('reel') or {}).get('frames', []):
        f['text'] = R(f['text'], 'sentence')
        if f.get('top'): f['top'] = recase(f['top'], 'en' if L == 'th' else L, tag_mode(f['top']) if L in ('id', 'en', 'th') else 'sentence')
        if f.get('sub'): f['sub'] = R(f['sub'], 'sentence')
    return p
