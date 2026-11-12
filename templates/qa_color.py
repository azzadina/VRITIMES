"""Blue-family coverage & lime share per rendered image (§4.2)."""
import glob, colorsys
from PIL import Image
rows = []
for f in sorted(glob.glob('/home/user/vritimes/output/*/*/slides/*.png') + glob.glob('/home/user/vritimes/output/*/*/image.png') + glob.glob('/home/user/vritimes/output/*/*/cover.png')):
    im = Image.open(f).convert('RGB').resize((108, 135 if 'cover' not in f else 192))
    px = list(im.getdata()); blue = lime = 0
    for r, g, b in px:
        h, s, v = colorsys.rgb_to_hsv(r/255, g/255, b/255)
        if (0.52 <= h <= 0.72 and s > 0.04) or (r > 225 and g > 235 and b > 245 and b >= r): blue += 1   # blue hues incl. pale blue
        elif (r > 240 and g > 240 and b > 240): pass
        if 0.17 <= h <= 0.22 and s > 0.5 and v > 0.7: lime += 1
    rows.append((blue/len(px), lime/len(px), f))
bad = [r for r in rows if r[0] < 0.70 or r[1] > 0.10]
print(len(rows), 'images; min blue %.0f%%; max lime %.1f%%' % (100*min(r[0] for r in rows), 100*max(r[1] for r in rows)))
for b in bad: print(' - blue %.0f%% lime %.1f%%' % (100*b[0], 100*b[1]), b[2].split('output/')[1])
