"""Voice-over for every scene with Microsoft Edge neural voices (free, via edge-tts).
Writes public/vo/sNN.mp3 and public/vo/timing.json (seconds per scene) used by the Remotion composition.
usage: python3 scripts/tts.py [--voice id-ID-ArdiNeural] [--rate +0%]
"""
import asyncio, json, os, re, subprocess, sys
import edge_tts

# Corporate / proxy networks: also trust the CA bundle named in SSL_CERT_FILE or REQUESTS_CA_BUNDLE
try:
    import ssl, certifi
    _ca = os.environ.get('SSL_CERT_FILE') or os.environ.get('REQUESTS_CA_BUNDLE')
    if _ca and os.path.exists(_ca):
        _ctx = ssl.create_default_context(cafile=certifi.where()); _ctx.load_verify_locations(_ca)
        edge_tts.communicate._SSL_CTX = _ctx
except Exception:
    pass

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
REEL = json.load(open(os.path.join(ROOT, 'public', 'reel.json'), encoding='utf-8'))
VOICE = REEL.get('voice') or 'de-DE-FlorianMultilingualNeural'
RATE = REEL.get('rate') or '+0%'
args = sys.argv[1:]
if '--voice' in args: VOICE = args[args.index('--voice') + 1]
if '--rate' in args: RATE = args[args.index('--rate') + 1]
OUT = os.path.join(ROOT, 'public', 'vo'); os.makedirs(OUT, exist_ok=True)

UNITS = ['', 'satu', 'dua', 'tiga', 'empat', 'lima', 'enam', 'tujuh', 'delapan', 'sembilan', 'sepuluh', 'sebelas']
def id_num(n):
    n = int(abs(n))
    if n < 12: return 'nol' if n == 0 else UNITS[n]
    if n < 20: return UNITS[n - 10] + ' belas'
    if n < 100: return UNITS[n // 10] + ' puluh' + (' ' + UNITS[n % 10] if n % 10 else '')
    if n < 200: return 'seratus' + (' ' + id_num(n % 100) if n % 100 else '')
    if n < 1000: return UNITS[n // 100] + ' ratus' + (' ' + id_num(n % 100) if n % 100 else '')
    if n < 2000: return 'seribu' + (' ' + id_num(n % 1000) if n % 1000 else '')
    if n < 10**6: return id_num(n // 1000) + ' ribu' + (' ' + id_num(n % 1000) if n % 1000 else '')
    if n < 10**9: return id_num(n // 10**6) + ' juta' + (' ' + id_num(n % 10**6) if n % 10**6 else '')
    return id_num(n // 10**9) + ' miliar' + (' ' + id_num(n % 10**9) if n % 10**9 else '')

PRON = []
for line in (REEL.get('pron') or '').split('\n'):
    if '=' in line:
        a, b = line.split('=', 1)
        if a.strip(): PRON.append((a.strip(), b.strip()))
PRON.sort(key=lambda x: -len(x[0]))

def clean(t):
    t = re.sub(r'[*\[\]]', '', t or '')
    for a, b in PRON:
        if re.fullmatch(r'[\w.-]+', a):
            t = re.sub(r'(^|[^\w])' + re.escape(a) + r'(?!\w)', lambda m, b=b: m.group(1) + b, t, flags=re.I)
        else:
            t = t.replace(a, b)
    if REEL.get('lang') == 'id':
        dig = lambda s: ' '.join(id_num(int(d)) for d in s)
        t = re.sub(r'(\d+)[.,](\d+)\s?%', lambda m: id_num(int(m.group(1))) + ' koma ' + dig(m.group(2)) + ' persen', t)
        t = re.sub(r'(\d+)\s?%', lambda m: id_num(int(m.group(1))) + ' persen', t)
        t = re.sub(r'Rp\s?([\d.]+)', lambda m: id_num(int(m.group(1).replace('.', ''))) + ' rupiah', t)
        t = re.sub(r'(\d+)[.,](\d+)', lambda m: id_num(int(m.group(1) + m.group(2))) if len(m.group(2)) == 3 else id_num(int(m.group(1))) + ' koma ' + dig(m.group(2)), t)
        t = re.sub(r'\d+', lambda m: id_num(int(m.group(0))), t)
        t = re.sub(r'\s*[–—]\s*', ', ', t); t = re.sub(r'\s*/\s*(?=(bulan|tahun|hari|minggu|jam|orang|post|posting|rilis)\b)', ' per ', t, flags=re.I); t = re.sub(r'\s*/\s*', ' atau ', t)
    return re.sub(r'\s+', ' ', t).strip()

def probe(path):
    try:
        r = subprocess.run(['ffprobe', '-v', 'error', '-show_entries', 'format=duration', '-of', 'default=nw=1:nk=1', path], capture_output=True, text=True)
        return float(r.stdout.strip())
    except Exception:
        return None

def pct(x):
    return int(re.sub(r'[^\d-]', '', str(x)) or 0)

def chunks(text, scene_idx, n_scenes):
    """Split a line into spoken phrases and give each its own pitch/rate/pause for a livelier rise and fall."""
    parts = []
    for sent in re.findall(r'[^.!?]+[.!?]*', text):
        sent = sent.strip()
        if not sent: continue
        words = len(sent.split())
        kind = 'question' if sent.endswith('?') else 'exclaim' if sent.endswith('!') else 'punch' if words <= 3 else 'statement'
        parts.append((sent, kind))
    # very short phrases lose their language context (a multilingual voice may switch accent): merge them
    merged = []
    for t, kind in parts:
        if merged and (len(merged[-1][0].split()) < 5 or len(t.split()) < 4):
            pt, pk = merged[-1]
            nk = kind if kind in ('question', 'exclaim') else pk if pk in ('question', 'exclaim') else 'statement'
            merged[-1] = (pt + ' ' + t, nk)
        else:
            merged.append((t, kind))
    parts = merged
    out = []
    base = pct(RATE)
    for k, (t, kind) in enumerate(parts):
        first = scene_idx == 0 and k == 0
        last = k == len(parts) - 1
        if kind == 'question': pitch, rate, pause = 4, 4, 0.32
        elif kind == 'exclaim': pitch, rate, pause = 3, 4, 0.30
        elif kind == 'punch': pitch, rate, pause = 4, -4, 0.34
        elif kind == 'label': pitch, rate, pause = 3, 2, 0.20
        else:
            pitch, rate, pause = (2, 2, 0.24) if k % 2 == 0 else (-1, 4, 0.24)
            if last: pitch, pause = -2, 0.0
        if first: pitch = min(pitch + 1, 4)
        if last and kind != 'statement': pause = 0.0
        vol = {'exclaim': 8, 'question': 5, 'punch': 6, 'label': 4}.get(kind, 0 if not last else -3)
        if 'Multilingual' in VOICE:
            # pitch shifts change how multilingual voices pronounce Indonesian words: keep pitch, vary tempo/volume/pauses
            pitch = 0
            rate = 0
        out.append({'text': t, 'pitch': f'{pitch:+d}Hz', 'rate': f'{base + rate:+d}%', 'volume': f'{vol:+d}%', 'pause': pause})
    return out

async def say(text, pitch, rate, path, volume='+0%'):
    kw = dict(rate=rate, pitch=pitch, volume=volume)
    try:
        comm = edge_tts.Communicate(text, VOICE, boundary='WordBoundary', **kw)
    except TypeError:
        comm = edge_tts.Communicate(text, VOICE, **kw)
    end = 0.0
    with open(path, 'wb') as f:
        async for chunk in comm.stream():
            if chunk['type'] == 'audio':
                f.write(chunk['data'])
            elif chunk['type'] == 'WordBoundary':
                end = max(end, (chunk['offset'] + chunk['duration']) / 1e7)
    return end or (probe(path) or 1.0)

async def one(i, text):
    path = os.path.join(OUT, f's{i + 1:02d}.mp3')
    tmp = os.path.join(OUT, f'_s{i + 1:02d}'); os.makedirs(tmp, exist_ok=True)
    parts = chunks(text, i, len(REEL['scenes']))
    inputs, filt, total = [], [], 0.0
    for k, c in enumerate(parts):
        cp = os.path.join(tmp, f'{k:02d}.mp3')
        end = await say(c['text'], c['pitch'], c['rate'], cp, c.get('volume', '+0%'))
        keep = min(end + 0.3, probe(cp) or end + 0.3)
        inputs += ['-i', cp]
        filt.append(f'[{k}:a]atrim=0:{keep:.3f},asetpts=PTS-STARTPTS,apad=pad_dur={c["pause"]:.3f}[a{k}]')
        total += keep + c['pause']
    filt.append(''.join(f'[a{k}]' for k in range(len(parts))) + f'concat=n={len(parts)}:v=0:a=1[out]')
    r = subprocess.run(['ffmpeg', '-y', '-v', 'error'] + inputs + ['-filter_complex', ';'.join(filt), '-map', '[out]', '-ar', '24000', '-ac', '1', '-c:a', 'libmp3lame', '-b:a', '96k', path], capture_output=True, text=True)
    if r.returncode:
        raise SystemExit('ffmpeg failed: ' + r.stderr[-400:])
    for f in os.listdir(tmp): os.remove(os.path.join(tmp, f))
    os.rmdir(tmp)
    return {'file': os.path.basename(path), 'duration': round(total, 3), 'text': text, 'phrases': parts}

async def main():
    timing = []
    for i, s in enumerate(REEL['scenes']):
        text = clean(s.get('vo'))
        if not text:
            timing.append({'file': None, 'duration': 0}); continue
        res = await one(i, text); timing.append(res)
        print(f"scene {i + 1}: {res['duration']:.2f}s  {text[:60]}")
    json.dump(timing, open(os.path.join(OUT, 'timing.json'), 'w'), ensure_ascii=False, indent=2)
    print('voice:', VOICE, '| total VO', round(sum(t['duration'] for t in timing), 1), 's | phrases with own pitch/rate for natural intonation')

asyncio.run(main())
