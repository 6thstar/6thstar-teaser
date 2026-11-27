#!/usr/bin/env python3
"""Hero picture v3.11 (Tracy 2026-11-27: the line "clear of the shoe"). From the real MARLOW capture (6thstar-sample, made data):
the shoe is set smaller at the left and the title, price and stars beside it, so the one-line 6thSTAR line has room under the
stars without touching the shoe. Pieces of the capture only; nothing drawn in."""
from pathlib import Path
from PIL import Image
ROOT = Path(__file__).resolve().parent.parent
page = Image.open(ROOT / "assets" / "marlow.jpg").convert("RGB")      # 1250 x 700
shoe = page.crop((50, 225, 685, 552))                                  # the whole shoe and its shadow
info = page.crop((740, 95, 1220, 335))                                 # title, price, stars and the 6thSTAR star
W, H = 1200, 420
out = Image.new("RGB", (W, H), "white")
s = 0.62
shoe = shoe.resize((round(shoe.width * s), round(shoe.height * s)), Image.LANCZOS)
out.paste(shoe, (24, 150))
k = 0.9
info = info.resize((round(info.width * k), round(info.height * k)), Image.LANCZOS)
ix = 24 + shoe.width + 36
out.paste(info, (ix, 30))
out.save(ROOT / "assets" / "marlow-hero-v2.jpg", quality=92)
print("hero v2", out.size, "shoe right", 24 + shoe.width, "info x", ix, "star y ~", 30 + round((318 - 95) * k))
