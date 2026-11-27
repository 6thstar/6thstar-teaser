#!/usr/bin/env python3
"""The link-preview picture (1200x630) for 6thstar.us (Tracy 2026-11-27: "push the website to the wild"): the promise, where,
and the real 6thSTAR line on MARLOW, from the film's own capture (6thstar-sample, made data). No mark (the site shows it at 72 px)."""
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont, ImageFilter
ROOT = Path(__file__).resolve().parent.parent
FONT = "/Users/tracyrosen/Library/Fonts/Roboto[wdth,wght].ttf"
raw = Path.home() / "Desktop/Downloads - Chrome/6thSTAR_Whole_Story_v1_1/source/raw/z_open.png"

def font(size, w=300):
    f = ImageFont.truetype(FONT, size); f.set_variation_by_axes([w, 100]); return f

W, H = 1200, 630
im = Image.new("RGB", (W, H), "white"); d = ImageDraw.Draw(im)
h1, sub = font(64), font(34)
t1, t2 = "Reduce Returns and Build Trust", "for Shopify stores"
d.text(((W - h1.getlength(t1)) / 2, 70), t1, font=h1, fill=(0, 0, 0))
d.text(((W - sub.getlength(t2)) / 2, 158), t2, font=sub, fill=(60, 60, 60))
line = Image.open(raw).convert("RGB").crop((88, 186, 790, 262))
line = line.resize((1000, round(line.height * 1000 / line.width)), Image.LANCZOS)
x, y = (W - line.width) // 2, 290
pad = 36
sh = Image.new("L", (line.width + 2 * pad, line.height + 2 * pad), 0)
ImageDraw.Draw(sh).rounded_rectangle((pad, pad + 8, pad + line.width, pad + 8 + line.height), 18, fill=60)
sh = sh.filter(ImageFilter.GaussianBlur(20))
im.paste((0, 0, 0), (x - pad, y - pad), sh.point(lambda v: v // 2))
m = Image.new("L", line.size, 0); ImageDraw.Draw(m).rounded_rectangle((0, 0, line.width - 1, line.height - 1), 16, fill=255)
im.paste(line, (x, y), m)
cap, url = font(30), font(26, 400)
c = "One short, true phrase under your review stars."
d.text(((W - cap.getlength(c)) / 2, y + line.height + 50), c, font=cap, fill=(30, 30, 30))
d.text(((W - url.getlength("6thstar.us")) / 2, H - 60), "6thstar.us", font=url, fill=(168, 98, 0))
im.save(ROOT / "assets" / "og-image.jpg", quality=90)
print("og-image", im.size)
