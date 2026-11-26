#!/usr/bin/env python3
"""Crops the real captures in site_src/caps and marks the place to click with a thin gold outline.
Writes assets/guides/*.png. Run from the repo root."""
from pathlib import Path
from PIL import Image, ImageDraw
ROOT = Path(__file__).resolve().parent.parent
CAPS = ROOT / "site_src" / "caps"
OUT = ROOT / "assets" / "guides"; OUT.mkdir(parents=True, exist_ok=True)
GOLD = (255, 153, 0)
# name: (capture, crop box or None, [outline boxes in capture pixels])
SHOTS = {
  "line-1": ("w1_admin_themes.png", (0, 0, 720, 470), [(8, 313, 150, 339)]),
  "line-2": ("w1_admin_themes.png", (380, 40, 1120, 470), [(993, 401, 1061, 430)]),
  "line-3": ("w1_picker.png", None, [(652, 17, 919, 71), (546, 236, 1025, 318)]),
  "line-4": ("w1_review_stars.png", (0, 200, 760, 640), [(32, 373, 209, 398)]),
  "line-5": ("w1_plus.png", (0, 230, 480, 530), [(106, 382, 140, 413)]),
  "line-6": ("w1_apps.png", (0, 330, 700, 700), [(305, 427, 394, 451), (216, 454, 400, 492)]),
  "line-7": ("w1_added.png", (560, 0, 1363, 480), [(1298, 6, 1360, 34), (835, 250, 1111, 280)]),
  "line-8": ("w1_done.png", (0, 150, 1568, 476), [(12, 158, 1554, 304)]),
  "ai-0": ("w2_status.png", None, [(456, 116, 705, 184)]),
  "ai-1": ("w2_agentic.png", (0, 0, 1160, 480), [(8, 335, 150, 359), (938, 262, 1148, 285)]),
  "ai-2": ("w2_status.png", None, [(487, 635, 1069, 697)]),
  "ai-3": ("w2_pick.png", None, [(687, 238, 718, 268), (712, 492, 1294, 542)]),
  "ai-4": ("w2_save.png", (300, 0, 1110, 400), [(631, 323, 775, 355), (986, 15, 1050, 51)]),
  "ai-5": ("w2_card.png", None, [(28, 196, 1272, 306)]),
}
for name, (cap, crop, boxes) in SHOTS.items():
    im = Image.open(CAPS / cap).convert("RGB")
    d = ImageDraw.Draw(im)
    w = max(2, round(im.width / 520))          # thin, in proportion to the capture
    for (x0, y0, x1, y1) in boxes:
        d.rounded_rectangle((x0 - w, y0 - w, x1 + w, y1 + w), radius=6 * w, outline=GOLD, width=w)
    if crop: im = im.crop(crop)
    if im.width > 1400: im = im.resize((1400, round(im.height * 1400 / im.width)), Image.LANCZOS)
    im.save(OUT / f"{name}.png", optimize=True)
    print(name, im.size)
