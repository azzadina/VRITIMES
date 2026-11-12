"""Automated QA over output/ (§10). Prints issues; exit 0."""
import os, json, re, glob
OUT = '/home/user/vritimes/output'
issues = []; n = 0
for cc in ['ID','MY','PH','SG','AU','TH','VN']:
    for d in sorted(glob.glob(f'{OUT}/{cc}/{cc}_*')):
        n += 1; fn = os.path.basename(d); pj = json.load(open(f'{d}/post.json'))
        fmt = pj['format']
        need = ['caption_instagram.txt','caption_facebook.txt','caption_linkedin.txt','sources.md','post.json']
        need += {'carousel':['linkedin_carousel.pdf','slides/01.png'],'reel':['cover.png','reel_script.md','reel_draft.mp4'],'single':['image.png']}[fmt]
        for f in need:
            if not os.path.exists(f'{d}/{f}'): issues.append((fn,'missing '+f))
        if not re.match(rf'{cc}_\d{{4}}-\d\d-\d\d_(Mon|Wed|Fri)_(EDU|FUN|PROMO|VIRAL)_(carousel|reels|single)_[a-z0-9-]+$', fn): issues.append((fn,'bad name'))
        ig = open(f'{d}/caption_instagram.txt').read(); fb = open(f'{d}/caption_facebook.txt').read(); li = open(f'{d}/caption_linkedin.txt').read()
        hook = ig.split('\n')[0]
        if len(hook) > 125: issues.append((fn, f'IG hook {len(hook)} chars'))
        tags = lambda t: len(re.findall(r'(?:^|\s)#\w', t))
        if not 3 <= tags(ig) <= 6: issues.append((fn, f'IG tags {tags(ig)}'))
        if not 3 <= tags(li) <= 5: issues.append((fn, f'LI tags {tags(li)}'))
        if tags(fb) > 3: issues.append((fn, f'FB tags {tags(fb)}'))
        if not 900 <= len(li) <= 2000: issues.append((fn, f'LI length {len(li)}'))
        l2 = '\n'.join(li.split('\n')[:2])
        if len(l2) > 210: issues.append((fn, f'LI first 2 lines {len(l2)}'))
        for name, t, src in (('fb', fb, 'facebook'), ('li', li, 'linkedin')):
            if f'utm_source={src}&utm_medium=organic_social&utm_campaign=sns_{cc.lower()}_' not in t or f"utm_content={pj['post_id']}" not in t:
                issues.append((fn, f'UTM {name}'))
        for s in pj['sources']:
            if s['url'] not in fb or s['url'] not in li or s['url'] not in open(f'{d}/sources.md').read(): issues.append((fn,'source missing in caption '+s['name']))
            if s['name'].split(' ')[0] not in ig and s['short'].split(',')[0] not in ig: issues.append((fn, 'IG source '+s['name']))
        # banned
        allt = ig+fb+li+json.dumps(pj, ensure_ascii=False)
        for bad in ['PR Newswire','Business Wire','Media OutReach','SeaPRwire','990','1,490','1,790','THB 999','$99']:
            if bad in allt: issues.append((fn,'banned '+bad))
print(n, 'posts checked;', len(issues), 'issues')
for i in issues: print(' -', *i)
