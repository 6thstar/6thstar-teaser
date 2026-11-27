#!/usr/bin/env python3
"""6thSTAR site v2.0 (Home: 6thSTAR_Website_Script_v2_0; /setup, /beta, /terms, /privacy, /demo as CC_MD_Website_And_Setup_Wizards_v1_2). Writes every page from one header and footer.
Run from the repo root: python3 site_src/build.py"""
from pathlib import Path
from html import escape

ROOT = Path(__file__).resolve().parent.parent
CONTACT = "trosen@rosengroup.us"         # Script v2.0: the contact email, for now (everywhere, the setup guides too: Tracy 2026-11-27)
VERSION = "v2.0"

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
  <a class="brand" href="/" aria-label="6thSTAR home"><img src="/assets/6thstar-mark.png" alt="6thSTAR™" width="72" height="72"></a>
  <nav>
    <a class="txt" href="/#how">How it works</a>
    <a class="txt" href="/#ai">All channels</a>
    <a class="txt" href="/#questions">Questions</a>
  </nav>
</div></header>
<main>
"""

FOOT = f"""</main>
<footer class="foot"><div class="in">
  <img src="/assets/6thstar-mark.png" alt="6thSTAR™" width="72" height="72">
  <nav><a href="/terms/">Terms</a><a href="/privacy/">Privacy</a><a href="mailto:{CONTACT}">{CONTACT}</a></nav>
</div></footer>
<script src="/assets/site.js"></script>
</body>
</html>
"""

def install(cls="btn lg"):
    return f'<a class="{cls}" data-install href="/beta/">Request more information</a>'

LINE = "Great trainer… runs a little narrow across the foot…"

# ── Home v2.0: seven sections, dense, words as written (6thSTAR_Website_Script_v2_0). No install button until section 6. ──
SOURCES_SVG = """<svg class="draw" viewBox="0 0 320 200" role="img" aria-label="Three sources, your product page, reviews and returns, feeding one point">
  <g font-family="Roboto, sans-serif" font-size="15" fill="#333">
    <rect x="8" y="14" width="118" height="40" rx="10" fill="#fff" stroke="#cfcfcf"/><text x="67" y="39" text-anchor="middle">Product page</text>
    <rect x="8" y="80" width="118" height="40" rx="10" fill="#fff" stroke="#cfcfcf"/><text x="67" y="105" text-anchor="middle">Reviews</text>
    <rect x="8" y="146" width="118" height="40" rx="10" fill="#fff" stroke="#cfcfcf"/><text x="67" y="171" text-anchor="middle">Returns</text>
  </g>
  <g fill="none" stroke="#bdbdbd" stroke-width="1.5">
    <path d="M126 34 C 200 34, 210 100, 262 100"/><path d="M126 100 L 262 100"/><path d="M126 166 C 200 166, 210 100, 262 100"/>
  </g>
  <circle cx="274" cy="100" r="13" fill="#ff9900"/>
</svg>"""

POINT_SVG = """<svg class="draw" viewBox="0 0 320 200" role="img" aria-label="The one point: runs a little narrow across the foot">
  <circle cx="44" cy="100" r="13" fill="#ff9900"/>
  <path d="M57 100 L 88 100" stroke="#bdbdbd" stroke-width="1.5"/>
  <rect x="88" y="62" width="224" height="76" rx="12" fill="#fff8ec" stroke="#d9c39b"/>
  <g font-family="Roboto, sans-serif" fill="#1d1d1d"><text x="104" y="93" font-size="15">Runs a little narrow</text><text x="104" y="116" font-size="15">across the foot</text></g>
</svg>"""

CHANNELS_SVG = """<svg class="draw channels" viewBox="0 0 520 400" role="img" aria-label="The product record in the centre, with lines out to the product page, the description, AI shoppers through Shopify, the open web, Instagram and Gorgias">
  <g stroke="#bdbdbd" stroke-width="1.5" fill="none">
    <path d="M260 200 L 92 64"/><path d="M260 200 L 428 64"/><path d="M260 200 L 52 200"/><path d="M260 200 L 468 200"/><path d="M260 200 L 92 336"/><path d="M260 200 L 428 336"/>
  </g>
  <g font-family="Roboto, sans-serif" font-size="16" fill="#333" text-anchor="middle">
    <rect x="12" y="42" width="160" height="44" rx="22" fill="#fff" stroke="#cfcfcf"/><text x="92" y="69">Product page</text>
    <rect x="348" y="42" width="160" height="44" rx="22" fill="#fff" stroke="#cfcfcf"/><text x="428" y="69">Description</text>
    <rect x="2" y="178" width="140" height="44" rx="22" fill="#fff" stroke="#cfcfcf"/><text x="72" y="205">Open web</text>
    <rect x="378" y="166" width="140" height="68" rx="22" fill="#fff" stroke="#cfcfcf"/><text x="448" y="195">AI shoppers</text><text x="448" y="216" font-size="13" fill="#555">through Shopify</text>
    <rect x="12" y="314" width="160" height="44" rx="22" fill="#fff" stroke="#cfcfcf"/><text x="92" y="341">Instagram</text>
    <rect x="348" y="314" width="160" height="44" rx="22" fill="#fff" stroke="#cfcfcf"/><text x="428" y="341">Gorgias</text>
    <rect x="170" y="158" width="180" height="84" rx="14" fill="#fff8ec" stroke="#d9c39b"/>
    <text x="260" y="195" font-size="18" font-weight="500" fill="#1d1d1d">Product record</text><text x="260" y="220" font-size="14" fill="#555">your product's truth</text>
  </g>
</svg>"""

def tile(b, line):
    return f'<div class="tile"><h3>{b}</h3><p>{line}</p></div>'

def qa(q, a):
    return f'<details><summary>{q}</summary><p>{a}</p></details>'

QS = [
    qa("What appears on my page?", "A small 6thSTAR, right under your review stars. A shopper points at it (or taps it on a phone) and one short line opens. Nothing else on your page changes."),
    qa("Which themes work?", 'Themes with app blocks, such as Shopify\'s own Horizon: you place the 6thSTAR line under your review stars in the theme editor, and 6thSTAR\'s setup guide shows each click. On a theme without app blocks there\'s nothing to place; your star still shows.'),
    qa("What data does it read?", 'Your products, photos and descriptions; your orders and returns, with return reasons and the notes buyers write; your return policy; your reviews; and your public website, to write your brief. It doesn\'t ask Shopify for a buyer\'s name, email, phone number or address. <a href="/privacy/">Privacy</a> has the detail.'),
    qa("How long until my lines are ready?", "Installing takes about 20 minutes. Writing your lines then depends on how many products you have. You read them before anything goes live."),
    qa("Will it cost me sales?", "No. Each line first confirms the shopper's choice, then adds the one thing worth knowing, the way a friend would."),
    qa("What happens if I uninstall?", "Uninstall from 6thSTAR's Settings and it clears everything it added: the line, the description sentences, the AI shoppers field and its records. If you uninstall from Shopify's own screen instead, the description sentences stay until you remove them."),
    qa("Who do I contact?", f'<a href="mailto:{CONTACT}">{CONTACT}</a>'),
]


# ── The left column of section cards (v3.0, Tracy 2026-11-27), on every page so it stays put ("left nav should be persistent").
#    On Home a card shows its section in the panel; on other pages it opens Home at that section.
CARDS = [
    ("top", '<img src="/assets/marlow-hero.jpg" alt="">', "fth-shoe", "Reduce Returns and Build Trust"),
    ("why", "<i></i><i></i><i></i>", "fth-why", "Most returns start with a surprise"),
    ("how", "<em>1</em><em>2</em><em>3</em>", "fth-how", "One true phrase, at the moment shoppers decide"),
    ("ai", '<svg viewBox="0 0 96 60" aria-hidden="true"><g stroke="#9a9a9a" stroke-width="2"><path d="M48 30 L16 12"/><path d="M48 30 L80 12"/><path d="M48 30 L16 48"/><path d="M48 30 L80 48"/></g><g fill="#fff" stroke="#9a9a9a" stroke-width="2"><circle cx="16" cy="12" r="6"/><circle cx="80" cy="12" r="6"/><circle cx="16" cy="48" r="6"/><circle cx="80" cy="48" r="6"/></g><circle cx="48" cy="30" r="9" fill="#ff9900"/></svg>', "fth-ai", "Your product's truth, everywhere it's read"),
    ("get", "<i></i>" * 6, "fth-get", "Close the gap, and trust follows"),
    ("story", "<b></b>", "fth-film", "How to install · Request more information"),
    ("questions", "?", "fth-q", "Questions"),
    ("about", "&ldquo;", "fth-q fth-about", "About 6thSTAR"),
]

def fnav(home, active=""):
    pre = "#" if home else "/#"
    items = "\n".join(
        f'  <a class="fcard{" on" if k == active else ""}" href="{pre}{k}" data-for="{k}"><span class="fth {cls}">{th}</span><span class="fname">{name}</span></a>'
        for k, th, cls, name in CARDS)
    return f'<nav class="fnav" aria-label="Sections">\n{items}\n</nav>'

HOME = head("6thSTAR — Reduce returns. Build trust.",
            "6thSTAR is a Shopify app that adds one short, true phrase right under your review stars, so shoppers know what to expect before they buy.") + f"""
<div class="frames">
@@FNAV@@
<div class="fpanel">
<section class="sec hero2" id="top"><div class="in intro">
  <h1>Reduce Returns and Build Trust</h1>
  <p class="for">for Shopify stores</p>
</div><div class="in two">
  <div class="words">
    <p class="sub">6thSTAR is a Shopify app that adds one short, true phrase right under your review stars, so shoppers know what to expect before they buy.</p>
    <div class="acts">
      <button class="playlink" type="button" data-film-open data-src="/assets/whole-story-v1-3.mp4" data-poster="/assets/whole-story-poster.jpg" data-vtt="/assets/whole-story-v1-3.vtt">Watch the 30-second film</button>
    </div>
  </div>
  <figure class="shot open hero-shot">
    <div class="frame"><picture><source media="(max-width:700px)" srcset="/assets/marlow-hero-m.jpg"><img src="/assets/marlow-hero.jpg" alt="MARLOW SUEDE TRAINER TAN on 6thstar-sample: the photo, the title, the review stars, and the 6thSTAR line open under them" width="1200" height="455"></picture>
    <div class="line-pop">{LINE}</div></div>
    <span class="tag">Sample store, made data</span>
  </figure>
</div></section>

<section class="sec" id="why"><div class="in">
  <h2>Most returns start with a surprise.</h2>
  <p class="sub">The product was fine. The expectation wasn't.</p>
  <div class="cols3">
    <div><h3>Shoppers decide in seconds</h3><p>The photo, the stars and the price form an impression before a word is read.</p></div>
    <div><h3>The impression becomes the yardstick</h3><p>Whatever arrives is judged against what the shopper expected.</p></div>
    <div><h3>A missed expectation comes back</h3><p>Not because it's faulty, just not what they pictured. The margin goes back with the box.</p></div>
  </div>
</div></section>

<section class="sec" id="how"><div class="in">
  <h2>One true phrase, at the moment shoppers decide.</h2>
  <p class="sub">There's one moment that matters: just before the shopper decides. After it, the expectation has hardened. Before it, one true thing can still shape it.</p>
  <ol class="steps">
    <li><div class="pic">{SOURCES_SVG}</div><h3><span>1</span>It reads your store.</h3><p>Over 100 signals compare everything shoppers are promised before they buy with what buyers experienced after: your product pages, reviews and returns.</p></li>
    <li><div class="pic">{POINT_SVG}</div><h3><span>2</span>It finds the one thing shoppers don't expect.</h3><p>Stars tell what buyers said. Returns tell what they kept.</p></li>
    <li><div class="pic"><figure class="shot open mini"><div class="frame"><img src="/assets/marlow-stars.jpg" alt="MARLOW's title, price and review stars, with the 6thSTAR line open under them" width="510" height="320" loading="lazy"><div class="line-pop">{LINE}</div></div><span class="tag">Sample store, made data</span></figure></div><h3><span>3</span>It says it, right under your stars.</h3><p>First it confirms the choice, then it tells the truth, the way a friend would: "{LINE}"</p></li>
  </ol>
</div></section>

<section class="sec" id="ai"><div class="in two">
  <div class="words">
    <p class="kicker">Every shopper. Every AI shopper.</p>
    <h2>Your product's truth, everywhere it's read.</h2>
    <ul class="ticks">
      <li>Shoppers see it on your product page and in your description.</li>
      <li>AI shoppers read the same truth in your product record, through Shopify to ChatGPT and Copilot, and on the open web beside the star.</li>
      <li>You choose the channels: AI shoppers, product pages, descriptions, Instagram, Gorgias.</li>
    </ul>
  </div>
  <div class="pic"><div class="chan-wide">{CHANNELS_SVG}</div>
    <div class="chan-list" aria-hidden="true"><p class="rec">Product record</p><ul><li>Product page</li><li>Description</li><li>AI shoppers <span>through Shopify</span></li><li>Open web</li><li>Instagram</li><li>Gorgias</li></ul></div></div>
</div></section>

<section class="sec" id="get"><div class="in">
  <h2>Close the gap, and trust follows.</h2>
  <p class="sub">Be right, product after product, and shoppers and the AI shoppers that choose for them learn to rely on you.</p>
  <div class="tiles">
    {tile("Lower returns.", "Fewer surprises, fewer boxes coming back.")}
    {tile("More shopper trust.", "What arrives is what they expected.")}
    {tile("More AI-shopper trust.", "Agents read what buyers kept, not only what they said.")}
    {tile("Your words, untouched.", "6thSTAR only adds. It never rewrites your copy.")}
    {tile("Your brand's voice.", "Your own praise words lead every line, and you can edit them.")}
    {tile("See it working.", "Live Results shows returns before, forecast and actual, down to each product.")}
  </div>
</div></section>

<section class="sec" id="story"><div class="in story-big">
  <div class="film" role="button" tabindex="0" aria-label="Watch How to install 6thSTAR, a 54-second film"
       data-src="/assets/how-to-install-v1-2.mp4" data-poster="/assets/how-to-install-poster-v1-1.jpg" data-vtt="/assets/how-to-install-v1-2.vtt">
    <div class="poster"><img class="film-mark" src="/assets/6thstar-mark.png" alt="6thSTAR™" width="72" height="72"><p>How to install 6thSTAR</p></div>
    <span class="play">Watch how to install · 54 seconds</span>
  </div>
  <div class="words cta-only">
    <h2>Request more information.</h2>
    <p class="sub">6thSTAR is in beta. Seven steps, right inside your Shopify admin. Join the first stores to use it.</p>
    <div class="acts">{install()}</div>
  </div>
</div></section>

<section class="sec" id="questions"><div class="in faq2">
  <h2 class="qh">Questions</h2>
  <div class="qcols"><div>{"".join(QS[:4])}</div><div>{"".join(QS[4:])}</div></div>
</div></section>

<section class="sec" id="about"><div class="in about">
  <h2>About 6thSTAR</h2>
  <p class="about-text">I've spent nearly fifty years in retail, and I've watched the same thing happen again and again: a good product comes back, not because anything was wrong with it, but because it wasn't what the shopper expected. Online, that gap has only grown. Shoppers decide in seconds, on a photo, the stars and a price. I built 6thSTAR to give every product one honest moment at that point of decision. I'm confident it will work because it rests on how people actually decide, and on a truth I've seen my whole career: when a store is right about its products, shoppers trust it, and keep what they buy.</p>
  <p class="about-sig">Tracy Rosen, founder</p>
</div></section>
</div></div>

<dialog class="filmbox" aria-label="The Whole Story, a 30-second film"><button class="x" type="button" aria-label="Close">×</button><div class="slot"></div></dialog>
""" + FOOT

# ── /beta ──
BETA = head("6thSTAR — Request more information", "Request more information about 6thSTAR for your Shopify store.") + f"""
<div class="page">
  <h1>Request more information.</h1>
  <p class="lead">6thSTAR is in beta. Tell us about your store, and we'll write to you.</p>
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
    <p class="lead">Questions in the meantime: <a href="mailto:{CONTACT}">{CONTACT}</a></p>
  </div>
</div>
""" + FOOT

# ── /setup: the two wizards (words as written, MD v1.2 Part 1); screenshots to come ──
def wizard(id_, title, steps, help_):
    """Tracy 2026-11-27: all tiles on one page, in order; pointing at a tile (tapping, on a phone) shows its detail, only while there."""
    tiles, n = [], 0
    for (say, img, alt, ph, label) in steps:
        if not label:
            n += 1
        num = escape(label) if label else str(n)
        tiles.append(f"""    <li class="tile-step" tabindex="0" aria-label="{escape(label) if label else f'Step {n}'}">
      <span class="tnum">{num}</span>
      <img src="{img}" alt="{escape(alt)}" loading="lazy">
      <div class="tsay" hidden>{say}</div>
    </li>""")
    h = "\n".join(f"    <p>{p}</p>" for p in help_)
    return f"""
  <section class="gtiles" id="{id_}">
    <h2>{title}</h2>
    <ol class="tgrid">
{chr(10).join(tiles)}
    </ol>
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
    f'Don\'t see Review stars? Your reviews app may need to add them first. Write to <a href="mailto:{CONTACT}">{CONTACT}</a>.',
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
<div class="page wide">
  <h1>Setup guides</h1>
  <p class="lead">Each step in order. <span class="hov">Point at a step to see it large.</span><span class="tap">Tap a step to see it large.</span></p>
{wizard("line", "Place the 6thSTAR line under your review stars", W1, W1_HELP)}
{wizard("ai", "Share with All Shoppers", W2, W2_HELP)}
  <div class="tzoom" aria-hidden="true"><figure><img alt=""><figcaption></figcaption></figure></div>
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
    f'<p class="lead">Questions: <a href="mailto:{CONTACT}">{CONTACT}</a></p>')
PRIVACY = placeholder("6thSTAR privacy", "The 6thSTAR privacy policy.", "Privacy",
    f'<p class="lead">The 6thSTAR privacy policy is being finalised. It will be published here, with its version and date, before 6thSTAR is listed.</p>'
    f'<p class="lead">This website sets no cookies and uses no analytics or tracking.</p>'
    f'<p class="lead">Questions: <a href="mailto:{CONTACT}">{CONTACT}</a></p>')
DEMO = placeholder("6thSTAR demo", "A hands-on 6thSTAR demo.", "The hands-on demo",
    '<p class="lead">Coming soon: try 6thSTAR yourself, on a sample store with made data. No login.</p>')

HOME = HOME.replace("@@FNAV@@", fnav(True))

def framed(html, active=""):
    """Every page but Home: the card column on the left, the page's own content in the panel."""
    return html.replace("<main>\n", f'<main>\n<div class="frames">{fnav(False, active)}\n<div class="fpanel fpage">\n', 1).replace("</main>", "</div></div>\n</main>", 1)

BETA, TERMS, PRIVACY, DEMO = framed(BETA), framed(TERMS), framed(PRIVACY), framed(DEMO)   # Tracy 2026-11-27: setup guides off the site for now ("not needed at this point"); guides.json still built for the app

PAGES = {"index.html": HOME, "beta/index.html": BETA,
         "terms/index.html": TERMS, "privacy/index.html": PRIVACY, "demo/index.html": DEMO}

for path, html in PAGES.items():
    p = ROOT / path
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(html)
    print("wrote", path, len(html))

# 404 page for the static site
(ROOT / "404.html").write_text(framed(placeholder("6thSTAR", "Page not found.", "Page not found",
    '<p class="lead">That page isn\'t here. <a href="/">Go to the home page</a>.</p>')))

# The same guides, for the 6thSTAR app (CC_MD v1.2: "Build them once, with the same screens and words in both places").
# The app copies assets/guides/guides.json and the shots into shopify_poc/mvp/guides/.
import json
def _g(steps, help_):
    return {"steps": [{"say": say, "img": img.rsplit("/", 1)[-1], "alt": alt, "label": label} for (say, img, alt, ph, label) in steps], "help": help_}
(ROOT / "assets" / "guides" / "guides.json").write_text(json.dumps({
    "version": "guides-v1-1",
    "line": dict(title="Place the 6thSTAR line under your review stars", **_g(W1, W1_HELP)),
    "ai": dict(title="Share with AI shoppers", **_g(W2, W2_HELP)),
}, ensure_ascii=False, indent=1))
print("wrote assets/guides/guides.json")
