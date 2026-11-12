"""Contact sheet of all rendered images for a country (QA aid). usage: contact.py CC out.png [filter]"""
import sys, os, glob
from PIL import Image, ImageDraw
cc, out = sys.argv[1], sys.argv[2]; flt = sys.argv[3] if len(sys.argv) > 3 else ''
base = f'/home/user/vritimes/output/{cc}'
files = []
for d in sorted(os.listdir(base)):
    p = os.path.join(base, d)
    if not os.path.isdir(p) or flt not in d: continue
    files += sorted(glob.glob(p + '/slides/*.png')) + glob.glob(p + '/image.png') + glob.glob(p + '/cover.png')
W = 216; H = 270; cols = 10
rows = (len(files) + cols - 1) // cols
sheet = Image.new('RGB', (cols * W, rows * H), 'white')
for i, f in enumerate(files):
    im = Image.open(f).convert('RGB'); im.thumbnail((W, H)); sheet.paste(im, ((i % cols) * W, (i // cols) * H))
sheet.save(out); print(len(files), 'images')
