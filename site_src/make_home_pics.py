#!/usr/bin/env python3
"""Home v2.0.1 pictures (Earl + Claude.ai review 2026-11-27), from the real captures only. Run from the repo root.
- marlow-hero.jpg / marlow-hero-m.jpg: MARLOW's page cropped so it ends just under the line (no size row, no Add to cart).
  On the wide one the photo runs lower than the line, so the product column below the line is left white; nothing is drawn in.
- setup-plus.png / setup-added.png: the theme editor's panel only (no store preview): the + below Review stars, then the
  6thSTAR line block in place, each with the guides' thin gold outline.
- whole-story-poster.jpg: the film's own line capture, large, on white, with the film's caption: a still that reads at a glance."""
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont, ImageFilter

ROOT = Path(__file__).resolve().parent.parent
A = ROOT / "assets"
CAPS = ROOT / "site_src" / "caps"
GOLD = (255, 153, 0)

# ── hero ──
page = Image.open(A / "marlow.jpg").convert("RGB")            # 1250 x 700, 6thstar-sample, made data
h = page.crop((40, 90, 1240, 545))                             # the whole photo; the shoe's sole ends ~525
ImageDraw.Draw(h).rectangle((690, 345 - 90, h.width, h.height), fill=(255, 255, 255))   # the column under the stars: the line goes here
h.save(A / "marlow-hero.jpg", quality=90)
m = Image.open(A / "marlow-m.jpg").convert("RGB")             # 530 x 620, the phone crop
m.crop((0, 0, 530, 360)).save(A / "marlow-hero-m.jpg", quality=90)
print("hero", h.size)

# ── setup pair ──
def panel(cap, box, crop, out):
    im = Image.open(CAPS / cap).convert("RGB")
    d = ImageDraw.Draw(im)
    w = 2
    d.rounded_rectangle((box[0] - w, box[1] - w, box[2] + w, box[3] + w), radius=12, outline=GOLD, width=w)
    im = im.crop(crop)
    im = im.resize((im.width * 2, im.height * 2), Image.LANCZOS)    # shown about this size; keeps the panel's words readable
    im.save(A / out, optimize=True)
    print(out, im.size)

panel("w1_plus.png", (106, 382, 140, 413), (28, 352, 212, 452), "setup-plus.png")
panel("w1_added.png", (36, 399, 207, 421), (28, 352, 212, 452), "setup-added.png")

# ── the closing film's still ──
FONT = "/Users/tracyrosen/Library/Fonts/Roboto[wdth,wght].ttf"
film_raw = Path.home() / "Desktop/Downloads - Chrome/6thSTAR_Whole_Story_v1_1/source/raw/z_open.png"
line = Image.open(film_raw).convert("RGB").crop((88, 186, 790, 262))   # the line's row only, as in the film
W, H = 1280, 720
line = line.resize((1120, round(line.height * 1120 / line.width)), Image.LANCZOS)
poster = Image.new("RGB", (W, H), "white")
pad = 40
sh = Image.new("L", (line.width + 2 * pad, line.height + 2 * pad), 0)
ImageDraw.Draw(sh).rounded_rectangle((pad, pad + 10, pad + line.width, pad + 10 + line.height), 20, fill=70)
sh = sh.filter(ImageFilter.GaussianBlur(22))
x, y = (W - line.width) // 2, 250
poster.paste((0, 0, 0), (x - pad, y - pad), sh.point(lambda v: v // 2))
mask = Image.new("L", line.size, 0); ImageDraw.Draw(mask).rounded_rectangle((0, 0, line.width - 1, line.height - 1), 18, fill=255)
poster.paste(line, (x, y), mask)
f = ImageFont.truetype(FONT, 46); f.set_variation_by_axes([300, 100])
cap = "6thSTAR adds the one thing they don't expect."
ImageDraw.Draw(poster).text(((W - f.getlength(cap)) / 2, 470), cap, font=f, fill=(0, 0, 0))
poster.save(A / "whole-story-poster.jpg", quality=90)
print("poster", poster.size)
