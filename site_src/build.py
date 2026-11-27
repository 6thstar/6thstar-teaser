#!/usr/bin/env python3
"""6thSTAR site v1.1 (CC_MD_Website_And_Setup_Wizards_v1_2). Writes every page from one header and footer.
Run from the repo root: python3 site_src/build.py"""
from pathlib import Path
from html import escape

ROOT = Path(__file__).resolve().parent.parent
SUPPORT = "6thstarsupport@gmail.com"
VERSION = "v1.1"

def head(title, desc):
    return f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<meta name="description" content="{desc}">
<link rel="icon" href="/assets/6thstar-mark-96.png">
<link rel="apple-touch-icon" href="/assets/apple-touch-icon.png">
<link rel="preload" href="/assets/fonts/roboto-300-500.woff" as="font" type="font/woff" crossorigin>
<link rel="stylesheet" href="/assets/site.css">
</head>
<body>
<header class="top"><div class="in">
  <a class="brand" href="/" aria-label="6thSTAR home"><img src="/assets/6thstar-mark-96.png" alt="6thSTAR™" width="44" height="44"></a>
  <nav>
    <a class="txt" href="/setup/">Setup guides</a>
    <a class="txt" href="/demo/">Demo</a>
    <a class="btn sm" data-install href="/beta/">Install 6thSTAR</a>
  </nav>
</div></header>
<main>
"""

FOOT = f"""</main>
<footer class="foot"><div class="in">
  <nav><a href="/terms/">Terms</a><a href="/privacy/">Privacy</a><a href="mailto:{SUPPORT}">{SUPPORT}</a></nav>
  <img src="/assets/6thstar-mark.png" alt="6thSTAR™" width="120" height="120">
</div></footer>
<script src="/assets/site.js"></script>
</body>
</html>
"""

def install(cls="btn lg"):
    return f'<a class="{cls}" data-install href="/beta/">Install 6thSTAR</a>'

LINE = "Great trainer… runs a little narrow across the foot…"

# ── Home: the ten beats, words as written (MD v1.2 Part 2); images only the four named ──
HOME = head("6thSTAR — Reduce Returns and Build Trust",
            "One short phrase, at the moment shoppers decide. A Shopify app.") + f"""
<section class="beat hero" id="hook"><div class="in hero-grid">
  <div class="hero-words">
  <h1>Reduce Returns and Build Trust</h1>
  <p class="lead">One short phrase, at the moment shoppers decide.</p>
  <div class="cta">{install()}</div>
  </div>
  <div class="film" role="button" tabindex="0" aria-label="Watch the 30-second spot"
       data-src="/assets/spot-v2-8.mp4" data-poster="/assets/spot-v2-8.jpg" data-vtt="/assets/spot-v2-8.vtt">
    <img src="/assets/spot-v2-8.jpg" alt="The 30-second spot: the 6thSTAR mark, Reduce Returns and Build Trust" width="1280" height="720" loading="lazy">
    <span class="play">Watch the 30-second spot</span>
  </div>
</div></section>

<section class="beat narrow" id="surprise"><div class="in">
  <h2>Most returns start with a surprise.</h2>
  <p class="lead">The product was fine. The expectation wasn't. And by the time the box comes back, the margin is gone.</p>
</div></section>

<section class="beat narrow" id="seconds"><div class="in">
  <h2>Shoppers decide in seconds.</h2>
  <p class="lead">The photo, the stars and the price form an impression before a word is read. It happens fast and automatically, in every visit.</p>
  <p class="lead">That impression becomes the expectation. Whatever arrives is judged against it.</p>
</div></section>

<section class="beat" id="moment"><div class="in">
  <div class="center">
    <h2>There's one moment that matters.</h2>
    <p class="lead">It comes just before the shopper relies on that impression and decides. After it, the expectation has hardened. Before it, one true thing can still shape it.</p>
    <p class="speaks">That's when 6thSTAR speaks.</p>
  </div>
  <figure class="shot" aria-label="MARLOW's product page, everything dimmed except the space under the stars">
    <picture><source media="(max-width:700px)" srcset="/assets/marlow-m.jpg"><img src="/assets/marlow.jpg" alt="A product page for MARLOW SUEDE TRAINER TAN, dimmed except the space just under the review stars" width="1250" height="700" loading="lazy"></picture>
    <span class="spot-hole"></span>
    <span class="tag">Sample store, made data</span>
  </figure>
</div></section>

<section class="beat" id="phrase"><div class="in">
  <div class="center">
    <h2>One short phrase, right under your review stars.</h2>
  </div>
  <figure class="shot" data-line>
    <picture><source media="(max-width:700px)" srcset="/assets/marlow-m.jpg"><img src="/assets/marlow.jpg" alt="MARLOW SUEDE TRAINER TAN on 6thstar-sample, with the 6thSTAR under its review stars" width="1250" height="700" loading="lazy"></picture>
    <button class="star-hit" type="button" aria-expanded="false" aria-label="Open the 6thSTAR line"></button>
    <div class="line-pop" role="status">{LINE}</div>
    <span class="tag">Sample store, made data</span>
  </figure>
  <p class="hint">Point at the 6thSTAR under the stars (tap on a phone).</p>
  <div class="center">
    <p class="lead">It sits where every shopper's eye already goes.</p>
    <p class="lead">First it confirms the choice. Then it tells the truth, the way a friend would.</p>
  </div>
</div></section>

<section class="beat narrow" id="truth"><div class="in">
  <h2>Your product's own truth.</h2>
  <p class="lead">Over 100 signals compare everything shoppers are promised before they buy with what buyers experienced after.</p>
  <p class="lead">Stars tell what buyers said. Returns tell what they kept. 6thSTAR finds the one thing shoppers don't expect, and says it in a few words.</p>
</div></section>

<section class="beat narrow" id="every"><div class="in">
  <h2>Every shopper. Every AI shopper.</h2>
  <p class="lead">Shoppers see it on your product page.</p>
  <p class="lead">AI shoppers read the same truth in your product record: through Shopify, to ChatGPT and Copilot, and on the open web beside the star.</p>
  <p class="lead">Shared with every channel you choose.</p>
</div></section>

<section class="beat narrow" id="why"><div class="in">
  <h2>Close the gap, and trust follows.</h2>
  <p class="lead">Disappointment is the gap between what was expected and what arrived. Close the gap before the sale, and there's less to send back.</p>
  <p class="lead">Be right, product after product, and trust follows, from shoppers and from the AI shoppers that choose for them.</p>
</div></section>

<section class="beat narrow" id="get"><div class="in">
  <h2>Lower returns. More shopper trust. More AI-shopper trust.</h2>
  <p class="lead">See it in Live Results: your returns before, forecast and actual, down to each product.</p>
  <p class="speaks">About 20 minutes to install.*</p>
  <p class="lead">Seven steps, each with a guide.</p>
  <div class="links"><a href="/setup/#line">See how to place the line</a><a href="/setup/#ai">See the AI shoppers setup</a></div>
  <ul class="points">
    <li>It only adds; it never changes your words.</li>
    <li>Your praise words, in your brand's voice.</li>
    <li>You choose the channels.</li>
    <li>Uninstall from 6thSTAR's Settings clears everything it added.</li>
  </ul>
  <p class="lead">Try it first: <a href="/demo/">the hands-on demo</a>.</p>
  <p class="note">*Writing your lines depends on how many products you have.</p>
</div></section>

<section class="beat center" id="install"><div class="in">
  <div class="film" role="button" tabindex="0" aria-label="Watch The Whole Story, a 30-second film"
       data-src="/assets/whole-story-v1-1.mp4" data-poster="/assets/whole-story-v1-1.jpg" data-vtt="/assets/whole-story-v1-1.vtt">
    <img src="/assets/whole-story-v1-1.jpg" alt="The Whole Story: MARLOW's product page, with the 6thSTAR line open" width="1280" height="720" loading="lazy">
    <span class="play">Watch The Whole Story · 30 seconds</span>
  </div>
  <h2 style="margin-top:64px">Install 6thSTAR on your Shopify store.</h2>
  <div class="cta">{install()}</div>
  <div class="faq">
    <h3>Questions</h3>
    <details><summary>What appears on my page?</summary>
      <p>A small 6thSTAR, right under your review stars. A shopper points at it (or taps it on a phone) and one short line opens. Nothing else on your page changes.</p></details>
    <details><summary>Which themes work?</summary>
      <p>Themes with app blocks, such as Shopify's own Horizon: you place the 6thSTAR line under your review stars in the theme editor, and <a href="/setup/#line">the guide</a> shows each click. On a theme without app blocks there's nothing to place; your star still shows.</p></details>
    <details><summary>What data does it read?</summary>
      <p>Your products, photos and descriptions; your orders and returns, with return reasons and the notes buyers write; your return policy; your reviews; and your public website, to write your brief. It doesn't ask Shopify for a buyer's name, email, phone number or address. <a href="/privacy/">Privacy</a> has the detail.</p></details>
    <details><summary>How long until my lines are ready?</summary>
      <p>Installing takes about 20 minutes. Writing your lines then depends on how many products you have. You read them before anything goes live.</p></details>
    <details><summary>What happens if I uninstall?</summary>
      <p>Uninstall from 6thSTAR's Settings and it clears everything it added: the line, the description sentences, the AI shoppers field and its records. If you uninstall from Shopify's own screen instead, the description sentences stay until you remove them.</p></details>
    <details><summary>What does the beta involve?</summary>
      <p>A small group of Shopify stores install 6thSTAR before it's listed. We set it up with you on a call, you read your lines before anything goes live, and you tell us what you see.</p></details>
    <details><summary>Who do I contact?</summary>
      <p><a href="mailto:{SUPPORT}">{SUPPORT}</a></p></details>
  </div>
</div></section>
""" + FOOT

# ── /beta ──
BETA = head("Install 6thSTAR — beta request", "Ask to install 6thSTAR on your Shopify store.") + f"""
<div class="page">
  <h1>Install 6thSTAR on your Shopify store.</h1>
  <p class="lead">6thSTAR is in beta. Tell us about your store, and we'll set it up with you.</p>
  <form class="beta" novalidate>
    <label>Name<input name="name" autocomplete="name" required></label>
    <label>Email<input name="email" type="email" autocomplete="email" required></label>
    <label>Store URL<input name="store" type="text" inputmode="url" placeholder="yourstore.com or yourstore.myshopify.com" required></label>
    <label>Roughly how many orders a month?
      <select name="orders" required>
        <option value="">Choose one</option>
        <option>Under 100</option><option>100 to 500</option><option>500 to 2,000</option>
        <option>2,000 to 10,000</option><option>Over 10,000</option>
      </select></label>
    <label>How long has the store been selling?
      <select name="selling" required>
        <option value="">Choose one</option>
        <option>Under a year</option><option>1 to 3 years</option><option>Over 3 years</option>
      </select></label>
    <label class="trap" aria-hidden="true">Leave this empty<input name="website" tabindex="-1" autocomplete="off"></label>
    <div><button class="btn lg" type="submit">Send request</button></div>
    <p class="formerr" role="alert" hidden></p>
  </form>
  <div class="thanks" role="status">
    <h2 style="font-size:32px">Thank you. We'll write to you within two business days.</h2>
  </div>
</div>
""" + FOOT

# ── /setup: the two wizards (words as written, MD v1.2 Part 1); screenshots to come ──
def wizard(id_, title, steps, help_):
    t = "\n".join(
        f'    <template data-step data-say="{escape(say)}" data-img="{img}" data-alt="{escape(alt)}" data-ph="{escape(ph)}" data-label="{escape(label)}"></template>'
        for (say, img, alt, ph, label) in steps)
    h = "\n".join(f"    <p>{p}</p>" for p in help_)
    return f"""
  <section class="wiz" id="{id_}">
    <div class="wiz-head"><h2>{title}</h2><p class="wiz-count"></p></div>
{t}
    <div class="wiz-shot"></div>
    <p class="wiz-zoom">Click the picture to see it full size.</p>
    <p class="wiz-say" aria-live="polite"></p>
    <div class="wiz-nav"><button class="back" type="button">Back</button><button class="next" type="button">Next</button></div>
    <div class="wiz-help">
{h}
    </div>
  </section>"""

G = "/assets/guides/"
W1 = [
    ("In Shopify, click <b>Online Store</b>.", G + "line-1.png", "Shopify admin, left panel, Online Store outlined", "", ""),
    ("On your live theme, click <b>Edit theme</b>.", G + "line-2.png", "The live theme card, Edit theme outlined", "", ""),
    ("At the top, open the page menu and choose <b>Products › Default product</b>.", G + "line-3.png", "The theme editor's page menu, Products, Default product outlined", "", ""),
    ("In the left panel, find <b>Review stars</b>.", G + "line-4.png", "The theme editor's left panel, Review stars outlined", "", ""),
    ("Point just below <b>Review stars</b>. Click the <b>+</b> that appears.", G + "line-5.png", "The + just below Review stars, outlined", "", ""),
    ("Click <b>Apps</b>, then <b>6thSTAR line</b>.", G + "line-6.png", "The add-block panel, the Apps tab and 6thSTAR line outlined", "", ""),
    ("Check that the 6thSTAR line sits right under your stars. Click <b>Save</b>.", G + "line-7.png", "The preview with the 6thSTAR line under the stars, and Save, outlined", "", ""),
    ("Done. Back in 6thSTAR, this step shows ✓ and <b>Turn on</b> is ready.", G + "line-8.png", "The 6thSTAR Install step, Place the 6thSTAR line under your review stars, showing Done", "", ""),
]
W1_HELP = [
    f'Don\'t see Review stars? Your reviews app may need to add them first. Write to <a href="mailto:{SUPPORT}">{SUPPORT}</a>.',
    "Theme without app blocks? There's nothing to do. Your star still shows.",
    "Moved it later? 6thSTAR will tell you, and this guide will open again.",
]
W2 = [
    ("Before you start: your store must be open to shoppers (no password) and qualify for Shopify Catalog. "
     '<a href="https://help.shopify.com/en/manual/online-sales-channels/shopify-catalog" target="_blank" rel="noopener">Check in Shopify</a>',
     G + "ai-0.png", "Shopify Catalog's status in Shopify, here Ineligible, outlined", "", "Before you start"),
    ("In Shopify, click <b>Agentic</b>. Under Sources, click Shopify Catalog's status.", G + "ai-1.png", "Shopify admin, Agentic and Shopify Catalog's status outlined", "", ""),
    ("Click <b>Review your product data</b>. This opens Channel mapping.", G + "ai-2.png", "Shopify Catalog's status panel, Review your product data outlined", "", ""),
    ("Click into <b>Product description</b>, then <b>⊕</b>, to see its sources. <b>6thSTAR agent description</b> is under Product metafields.", G + "ai-3.png", "The Product description source list, 6thSTAR agent description outlined", "", ""),
    ("Take out <b>Product description</b> first, then add <b>6thSTAR agent description</b>. Click <b>Save</b>.", G + "ai-4.png", "Channel mapping with only 6thSTAR agent description left, and Save, outlined", "", ""),
    ("Done. Back in 6thSTAR, the AI shoppers card shows a green dot beside <b>Through Shopify</b>.", G + "ai-5.png", "The 6thSTAR AI shoppers card, Through Shopify with a green dot, outlined", "", ""),
]
W2_HELP = [
    "Shopify sends this to AI shoppers such as ChatGPT and Copilot. When each one reads it is up to them.",
    "To undo it, set Product description back to your own description.",
]
SETUP = head("6thSTAR setup guides", "Step-by-step guides: place the 6thSTAR line, and share with AI shoppers.") + f"""
<div class="page">
  <h1>Setup guides</h1>
  <p class="lead">Do each step in your own Shopify, then click Next.</p>
{wizard("line", "Place the 6thSTAR line under your review stars", W1, W1_HELP)}
{wizard("ai", "Share with AI shoppers", W2, W2_HELP)}
  <div class="cta" style="margin-top:64px">{install()}</div>
</div>
""" + FOOT

def placeholder(title, desc, h1, body):
    return head(title, desc) + f"""
<div class="page">
  <h1>{h1}</h1>
  {body}
  <div class="cta">{install()}</div>
</div>
""" + FOOT

TERMS = placeholder("6thSTAR terms", "The 6thSTAR terms of service.", "Terms",
    f'<p class="lead">The 6thSTAR terms are being finalised. They will be published here, with their version and date, before 6thSTAR is listed.</p>'
    f'<p class="lead">Questions: <a href="mailto:{SUPPORT}">{SUPPORT}</a></p>')
PRIVACY = placeholder("6thSTAR privacy", "The 6thSTAR privacy policy.", "Privacy",
    f'<p class="lead">The 6thSTAR privacy policy is being finalised. It will be published here, with its version and date, before 6thSTAR is listed.</p>'
    f'<p class="lead">This website sets no cookies and uses no analytics or tracking.</p>'
    f'<p class="lead">Questions: <a href="mailto:{SUPPORT}">{SUPPORT}</a></p>')
DEMO = placeholder("6thSTAR demo", "A hands-on 6thSTAR demo.", "The hands-on demo",
    '<p class="lead">Coming soon: try 6thSTAR yourself, on a sample store with made data. No login.</p>')

PAGES = {"index.html": HOME, "beta/index.html": BETA, "setup/index.html": SETUP,
         "terms/index.html": TERMS, "privacy/index.html": PRIVACY, "demo/index.html": DEMO}

for path, html in PAGES.items():
    p = ROOT / path
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(html)
    print("wrote", path, len(html))

# 404 page for the static site
(ROOT / "404.html").write_text(placeholder("6thSTAR", "Page not found.", "Page not found",
    '<p class="lead">That page isn\'t here. <a href="/">Go to the home page</a>.</p>'))

# The same guides, for the 6thSTAR app (CC_MD v1.2: "Build them once, with the same screens and words in both places").
# The app copies assets/guides/guides.json and the shots into shopify_poc/mvp/guides/.
import json
def _g(steps, help_):
    return {"steps": [{"say": say, "img": img.rsplit("/", 1)[-1], "alt": alt, "label": label} for (say, img, alt, ph, label) in steps], "help": help_}
(ROOT / "assets" / "guides" / "guides.json").write_text(json.dumps({
    "version": "guides-v1-0",
    "line": dict(title="Place the 6thSTAR line under your review stars", **_g(W1, W1_HELP)),
    "ai": dict(title="Share with AI shoppers", **_g(W2, W2_HELP)),
}, ensure_ascii=False, indent=1))
print("wrote assets/guides/guides.json")
