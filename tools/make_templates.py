#!/usr/bin/env python3
"""Builds 30 website templates (10 real estate, 10 e-commerce, 10 home services)
into /t/<category>/<slug>/index.html, plus the three category pages.
Every brand is fictional and every page is labelled as a template preview.
Photos: assets/tpl/*.jpg (CC0 via Openverse, see assets/tpl/CREDITS.json) and assets/stores/*.jpg.
Run from the repo root: python3 tools/make_templates.py
"""
import os, html
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MAIN = "https://vixassist.com"

FONTS = {
 1: "family=Cormorant+Garamond:ital,wght@0,500;1,500&family=Jost:wght@400;500;600",
 2: "family=Playfair+Display:ital,wght@0,800;1,400&family=Libre+Franklin:wght@400;600;700",
 3: "family=Archivo:wght@400;600;900",
 4: "family=Sora:wght@600;700&family=Manrope:wght@400;600;700",
 5: "family=Fraunces:ital,wght@0,600;1,600&family=Nunito+Sans:wght@400;700",
 6: "family=Space+Grotesk:wght@400;700",
 7: "family=DM+Serif+Display&family=DM+Sans:wght@400;500;700",
 8: "family=Inter+Tight:wght@400;500&family=Inter:wght@400;500;700&family=JetBrains+Mono:wght@500",
 9: "family=Syne:wght@700;800&family=Manrope:wght@400;600;700",
 10: "family=Bebas+Neue&family=Inter:wght@400;600;700",
}
STYLE = {1: "Noir", 2: "Editorial", 3: "Swiss", 4: "Glass", 5: "Organic", 6: "Brutal", 7: "Split", 8: "Minimal", 9: "Bold colour", 10: "Cinematic"}
CATS = {
 "real-estate": ("Real estate websites", "re", "Listings, valuations and lead capture that turn visitors into buyers and sellers."),
 "ecommerce": ("E-commerce websites", "ec", "Online stores built to look premium and sell, on every screen."),
 "home-services": ("Home service websites", "hs", "Sites that make the phone ring and fill the calendar with booked jobs."),
}
im = lambda c, i: f"/assets/tpl/{c}-{i:02d}.jpg"
st = lambda k, i: f"/assets/stores/{k}-{i}.jpg"
E = html.escape

# ---------------------------------------------------------------- data
RE = [
 dict(slug="maison-noir", name="Maison Noir Estates", s=1, city="Beverly Hills", h1="Homes for the <em>extraordinary</em> few.", sub="Private listings, discreet representation and a concierge level of service for exceptional properties.", hero=1, cards=[11, 0, 12, 16, 2, 22], tiles=[13, 14, 10, 18], story=4, phone="(310) 555 0190"),
 dict(slug="hollis-group", name="The Hollis Group", s=2, city="Brooklyn", h1="Brownstones, lofts and <em>the stories behind them.</em>", sub="Brooklyn's neighbourhood specialists. We know every block, every school and every sunny kitchen.", hero=9, cards=[9, 25, 23, 19, 3, 26], tiles=[9, 17, 19, 15], story=25, phone="(718) 555 0144"),
 dict(slug="grid-realty", name="GRID Realty", s=3, city="Chicago", h1="Find. Tour. Own.", sub="Condos and lofts across Chicago, listed with real prices, real photos and same day tours.", hero=8, cards=[7, 8, 22, 27, 21, 6], tiles=[13, 8, 7, 14], story=7, phone="(312) 555 0177"),
 dict(slug="skyline-living", name="Skyline Living", s=4, city="Toronto", h1="New developments. <em>First access.</em>", sub="Pre construction condos and towns, with floor plans, incentives and VIP launch access before the public.", hero=14, cards=[8, 22, 27, 4, 11, 24], tiles=[14, 13, 15, 8], story=22, phone="(416) 555 0123"),
 dict(slug="willow-oak", name="Willow & Oak Homes", s=5, city="Austin", h1="Room to grow, <em>close to everything.</em>", sub="Family homes in Austin's best school districts, with a team that treats your move like our own.", hero=17, cards=[17, 2, 25, 5, 18, 26], tiles=[17, 18, 2, 19], story=5, phone="(512) 555 0168"),
 dict(slug="block-realty", name="BLOCK Realty", s=6, city="Atlanta", h1="Deals that <em>actually</em> pencil.", sub="Off market investment properties, cash flow numbers upfront and a team that answers in minutes.", hero=9, cards=[19, 17, 9, 18, 26, 7], tiles=[9, 19, 17, 7], story=26, phone="(404) 555 0109"),
 dict(slug="coastline", name="Coastline Properties", s=7, city="San Diego", h1="Wake up to the ocean.", sub="Beach houses, coastal condos and vacation homes from La Jolla to Encinitas.", hero=10, cards=[10, 0, 11, 21, 3, 22], tiles=[10, 0, 15, 12], story=0, phone="(619) 555 0136"),
 dict(slug="atelier", name="Atelier Residences", s=8, city="Los Angeles", h1="Architecture you can live in.", sub="A small collection of architect designed homes, presented with the care they were built with.", hero=6, cards=[6, 1, 11, 22, 27, 21], tiles=[6, 1, 2, 16], story=22, phone="(213) 555 0152"),
 dict(slug="keystone", name="Keystone Realty Co.", s=9, city="Denver", h1="Sold faster. <em>Sold for more.</em>", sub="A data driven team that prices right, markets hard and negotiates every dollar for Denver sellers.", hero=2, cards=[2, 17, 18, 25, 23, 1], tiles=[2, 17, 25, 13], story=16, phone="(720) 555 0181"),
 dict(slug="summit-estates", name="Summit Estates", s=10, city="Miami", h1="Live above it all.", sub="Waterfront estates and penthouses across Miami, shown the way they deserve to be seen.", hero=13, cards=[11, 12, 13, 20, 4, 15], tiles=[13, 15, 12, 10], story=12, phone="(305) 555 0118"),
]
EC = [
 dict(slug="obsidian", name="OBSIDIAN", s=1, h1="Time, <em>refined.</em>", sub="Swiss movements, sapphire crystal and a lifetime warranty. Watches made to be handed down.", hero=10, prods=[("ec", 10), ("ec", 8), ("ec", 17), ("ec", 9)], tiles=[10, 17, 8, 18], story=17, kind="Watches and jewellery"),
 dict(slug="the-edit", name="The Edit Store", s=2, h1="The pieces <em>worth keeping.</em>", sub="A small edit of womenswear, chosen each season for fabric, fit and how often you will actually wear it.", hero=0, prods=[("fashion", 0), ("fashion", 1), ("fashion", 2), ("fashion", 3)], tiles=[21, 23, 22, 1], story=1, kind="Fashion"),
 dict(slug="stride", name="STRIDE", s=3, h1="Made to move.", sub="Performance sneakers engineered in limited runs. Free returns, 30 day test runs.", hero=3, prods=[("ec", 3), ("ec", 2), ("ec", 4), ("fashion", 4)], tiles=[3, 4, 2, 12], story=4, kind="Sneakers"),
 dict(slug="aura-audio", name="Aura Audio", s=4, h1="Hear <em>everything.</em>", sub="Wireless headphones with adaptive noise cancelling and 40 hours of battery. Designed in London.", hero=11, prods=[("phones", 0), ("phones", 1), ("phones", 2), ("electrical", 0)], tiles=[11, 12, 9, 26], story=12, kind="Audio and tech"),
 dict(slug="bloom-skin", name="Bloom Skincare", s=5, h1="Skin that <em>glows</em> on its own.", sub="Clean, plant powered skincare with nothing to hide. Dermatologist tested, cruelty free, refillable.", hero=5, prods=[("beauty", 0), ("beauty", 1), ("beauty", 2), ("beauty", 3)], tiles=[5, 6, 7, 20], story=7, kind="Skincare"),
 dict(slug="loud-apparel", name="LOUD Apparel", s=6, h1="Wear it <em>loud.</em>", sub="Heavyweight streetwear in small drops. When it is gone, it is gone.", hero=1, prods=[("fashion", 5), ("fashion", 6), ("fashion", 7), ("ec", 4)], tiles=[23, 22, 2, 21], story=21, kind="Streetwear"),
 dict(slug="roast-co", name="Roast & Co.", s=7, h1="Coffee, roasted this week.", sub="Single origin beans roasted to order and delivered within days. Subscribe and never run out.", hero=13, prods=[("ec", 14), ("ec", 13), ("ec", 15), ("ec", 16)], tiles=[14, 13, 15, 16], story=16, kind="Coffee"),
 dict(slug="studio-form", name="Studio Form", s=8, h1="Furniture, reduced to what matters.", sub="Solid wood and steel pieces for modern homes. Made to order, delivered in four weeks.", hero=16, prods=[("furniture", 0), ("furniture", 1), ("furniture", 2), ("furniture", 3)], tiles=[16, 24, 25, 26], story=24, kind="Furniture"),
 dict(slug="volt-gadgets", name="Volt Gadgets", s=9, h1="The latest phones. <em>Tomorrow.</em>", sub="Unlocked phones, laptops and accessories with next day delivery and a two year warranty.", hero=9, prods=[("phones", 3), ("phones", 4), ("electrical", 1), ("electrical", 2)], tiles=[26, 9, 25, 11], story=26, kind="Electronics"),
 dict(slug="maison-parfum", name="Maison Parfum", s=10, h1="A scent for every story.", sub="Niche fragrances crafted in Grasse. Discovery sets, refills and engraving on every bottle.", hero=19, prods=[("ec", 19), ("ec", 20), ("beauty", 4), ("beauty", 5)], tiles=[19, 20, 0, 17], story=20, kind="Fragrance"),
]
HS = [
 dict(slug="apex-roofing", name="Apex Roofing", s=1, h1="Roofs built to <em>outlast</em> the storm.", sub="Premium roof replacements and repairs with a 25 year workmanship warranty and free drone inspections.", hero=7, svc=["Roof replacement", "Storm damage repair", "Drone inspections", "Gutters and fascia", "Skylights", "Insurance claims help"], ba=(9, 7), photos=[8, 9, 7, 5], phone="(214) 555 0144"),
 dict(slug="fairbank", name="Fairbank Renovations", s=2, h1="Kitchens and baths, <em>beautifully redone.</em>", sub="Design and build renovations with one team, one fixed price and a project manager who answers the phone.", hero=10, svc=["Kitchen remodels", "Bathroom remodels", "Basement finishing", "Custom carpentry", "Flooring", "Whole home renovations"], ba=(4, 28), photos=[10, 11, 12, 3], phone="(617) 555 0121"),
 dict(slug="volt-electric", name="VOLT Electric", s=3, h1="Power. Done right.", sub="Licensed electricians for panels, rewiring, EV chargers and emergencies, 24 hours a day.", hero=26, svc=["Panel upgrades", "EV chargers", "Rewiring", "Lighting design", "Emergency call outs", "Safety inspections"], ba=(20, 26), photos=[26, 20, 19, 12], phone="(602) 555 0177"),
 dict(slug="clearair", name="ClearAir HVAC", s=4, h1="Perfect air, <em>all year.</em>", sub="Heating and cooling installs, tune ups and same day repairs, with financing from $0 down.", hero=27, svc=["AC installation", "Furnace repair", "Heat pumps", "Duct cleaning", "Maintenance plans", "Air quality"], ba=(1, 27), photos=[27, 1, 0, 19], phone="(480) 555 0150"),
 dict(slug="green-acre", name="Green Acre Landscaping", s=5, h1="Gardens that <em>make people stop.</em>", sub="Landscape design, weekly lawn care and seasonal planting for homes that want to stand out on the street.", hero=18, svc=["Garden design", "Weekly lawn care", "Hedges and trees", "Planting", "Irrigation", "Seasonal clean ups"], ba=(17, 18), photos=[16, 14, 15, 17], phone="(503) 555 0163"),
 dict(slug="fixit", name="FIXIT Handyman", s=6, h1="Your to do list, <em>done.</em>", sub="One call fixes it all: repairs, installs, painting and assembly, booked online in 60 seconds.", hero=6, svc=["Repairs", "TV mounting", "Painting", "Furniture assembly", "Doors and locks", "Odd jobs"], ba=(4, 28), photos=[12, 21, 3, 6], phone="(206) 555 0188"),
 dict(slug="sparkle-clean", name="Sparkle Clean Co.", s=7, h1="Come home to clean.", sub="Vetted, insured cleaners for weekly, deep and move out cleans. Book online, satisfaction guaranteed.", hero=28, svc=["Weekly cleaning", "Deep cleaning", "Move out cleans", "Office cleaning", "Carpet cleaning", "Post build cleans"], ba=(4, 28), photos=[2, 28, 4, 13], phone="(702) 555 0131"),
 dict(slug="line-level", name="Line & Level Carpentry", s=8, h1="Built by hand. Built to last.", sub="Bespoke joinery, built ins and timber work, measured twice and made in our own workshop.", hero=10, svc=["Built in storage", "Staircases", "Doors and windows", "Decking", "Kitchens", "Restoration"], ba=(4, 3), photos=[10, 11, 13, 3], phone="(415) 555 0174"),
 dict(slug="flowright", name="FlowRight Plumbing", s=9, h1="Leak today. <em>Fixed today.</em>", sub="Licensed plumbers on call 24/7 for leaks, drains, water heaters and repipes. Upfront prices, no call out fee.", hero=1, svc=["Emergency leaks", "Drain unblocking", "Water heaters", "Repiping", "Bathroom installs", "Leak detection"], ba=(1, 27), photos=[1, 27, 0, 12], phone="(713) 555 0105"),
 dict(slug="sunpeak-solar", name="SunPeak Solar", s=10, h1="Make your own power.", sub="Solar and battery systems designed for your roof, installed in a day, with a 25 year performance guarantee.", hero=24, svc=["Solar panels", "Battery storage", "EV charging", "System monitoring", "Repairs", "Financing"], ba=(7, 23), photos=[23, 25, 24, 7], phone="(916) 555 0193"),
]
HS_ICONS = ["ph-wrench", "ph-lightning", "ph-shield-check", "ph-calendar-check", "ph-house-line", "ph-star"]

# ---------------------------------------------------------------- page parts
def head(title, desc, s):
    return f'''<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">
<title>{E(title)}</title><meta name="description" content="{E(desc)}"><meta name="robots" content="noindex">
<link rel="icon" href="/assets/favicon.svg" type="image/svg+xml">
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?{FONTS[s]}&family=Inter:wght@500;700&display=swap" rel="stylesheet">
<link rel="stylesheet" href="https://unpkg.com/@phosphor-icons/web@2.1.1/src/regular/style.css">
<link rel="stylesheet" href="/assets/tpl/tpl.css?v=1"></head>'''

def demo(cat, name, n):
    return f'<div class="demo"><span><b>Template preview</b> · {E(name)} is a sample brand · Style: {STYLE[n]}</span><a href="/#brief">Use this design</a><a class="g" href="/{cat}/">All {CATS[cat][0].lower()}</a></div>'

def nav(name, links, cta, cart=False):
    l = "".join(f'<a href="#{h}">{t}</a>' for t, h in links)
    return f'<header class="nav"><div class="w"><a class="brand" href="#"><i></i>{E(name)}</a><nav class="links">{l}</nav>{"<span class=cart>Cart<b>0</b></span>" if cart else ""}<a class="btn" href="#{cta[1]}">{cta[0]}</a><button class="menu" aria-label="Menu">☰</button></div></header>'

def foot(name, cols):
    c = "".join(f'<div><h4>{h}</h4>' + "".join(f'<a href="#">{x}</a>' for x in xs) + "</div>" for h, xs in cols)
    return f'<footer><div class="w"><div><a class="brand" href="#"><i></i>{E(name)}</a><p style="margin-top:12px;max-width:300px">A sample brand created to show this template. Your business, your content, your photos.</p></div>{c}<div class="legal">© 2026 {E(name)} (sample) · Template designed by <a href="{MAIN}" style="display:inline">Vix Assist</a></div></div></footer>'

def hero(d, cat, img, extra):
    bg = f' style="background-image:url({img})"' if d["s"] == 10 else ""
    return f'''<section class="hero"{bg}><div class="w hero-in"><div class="rv in"><span class="kick">{E(d.get("kicker", ""))}</span><h1>{d["h1"]}</h1><p class="sub">{E(d["sub"])}</p>{extra}</div><div class="hero-img rv in"><img src="{img}" alt="" fetchpriority="high">{d.get("badge", "")}</div></div></section>'''

def stats(items):
    return '<div class="w"><div class="stats rv">' + "".join(f"<div><b>{a}</b><span>{b}</span></div>" for a, b in items) + "</div></div>"

def quotes(items, label):
    return '<div class="quotes">' + "".join(f'<div class="q rv"><span class="stars">★★★★★</span><p>“{E(t)}”</p><b>{E(n)}</b><small>{E(r)}</small></div>' for t, n, r in items) + f'</div><p class="sample">{label}</p>'

def page(cat, d, body):
    n = d["s"]
    out = head(f'{d["name"]} · {CATS[cat][0][:-1]} template by Vix Assist', d["sub"], n) + f'<body class="s{n}">' + demo(cat, d["name"], n) + body + '<script src="/assets/tpl/tpl.js?v=1" defer></script></body></html>'
    p = os.path.join(ROOT, "t", cat, d["slug"]); os.makedirs(p, exist_ok=True)
    open(os.path.join(p, "index.html"), "w", encoding="utf-8").write(out)

# ---------------------------------------------------------------- real estate
LIST = [("4 bd", "3.5 ba", "3,850 sqft"), ("3 bd", "2 ba", "2,140 sqft"), ("5 bd", "4 ba", "5,200 sqft"), ("2 bd", "2 ba", "1,280 sqft"), ("3 bd", "2.5 ba", "2,600 sqft"), ("1 bd", "1 ba", "860 sqft")]
STREETS = ["Oak Ridge Drive", "Linden Avenue", "Harbor View Road", "Maple Court", "Westlake Terrace", "Park Row"]
def re_page(d, i):
    c, s = "re", d["s"]
    mult = [4.2, 1.1, 2.6, .78, 1.6, .54] if s in (1, 10, 8) else [1.25, .68, 1.9, .49, .89, .36]
    cards = "".join(f'''<article class="card rv"><div class="im"><img src="{im(c, x)}" alt="" loading="lazy"><span class="tag">{["New", "Open house Sat", "Just listed", "Price drop", "Featured", "Coming soon"][k]}</span></div><div class="bd"><div class="price">${int(mult[k]*1000):,},000</div><h3>{100 + k*37 + i*11} {STREETS[k]}</h3><p>{d["city"]}</p><div class="specs"><span><b>{LIST[k][0]}</b></span><span><b>{LIST[k][1]}</b></span><span>{LIST[k][2]}</span></div></div></article>''' for k, x in enumerate(d["cards"]))
    areas = ["Downtown", "Waterfront", "Old Town", "The Heights"]
    tiles = "".join(f'<a class="tile rv" href="#listings"><img src="{im(c, x)}" alt="" loading="lazy"><div><b>{areas[k]}</b><span>{12 + k*7} homes for sale</span></div></a>' for k, x in enumerate(d["tiles"]))
    search = '<form class="search" onsubmit="return false"><label>Location<input placeholder="City, area or ZIP" value="' + E(d["city"]) + '"></label><label>Type<select><option>Any type</option><option>House</option><option>Condo</option><option>Townhouse</option></select></label><label>Price<select><option>Any price</option><option>Up to $750k</option><option>$750k to $1.5m</option><option>$1.5m+</option></select></label><button class="btn">Search</button></form><div class="trust"><span>Licensed brokerage</span><span>Replies in minutes</span><span>Free home valuation</span></div>'
    d.setdefault("kicker", f"{d['city']} real estate")
    d["badge"] = '<div class="badge"><b>98%</b>of list price, on average*</div>'
    body = nav(d["name"], [("Buy", "listings"), ("Sell", "value"), ("Neighbourhoods", "areas"), ("About", "about")], ("Book a showing", "value")) + hero(d, "real-estate", im(c, d["hero"]), search)
    body += stats([("$1.2B", "in homes sold*"), ("14", "days on market, median*"), ("2,400+", "happy clients*"), ("4.9★", "average review*")])
    body += f'<section id="listings"><div class="w"><div class="head rv"><span class="kick">Featured listings</span><h2 class="h2">Homes worth a closer look.</h2></div><div class="grid">{cards}</div></div></section>'
    body += f'<section id="about"><div class="w story"><div class="ph rv"><img src="{im(c, d["story"])}" alt="" loading="lazy"></div><div class="rv"><span class="kick">Why {E(d["name"])}</span><h2 class="h2">Local experts who answer the phone.</h2><p class="lead">Every buyer and seller gets one dedicated agent, a clear plan and updates without having to chase.</p><ul><li>Instant replies to every enquiry, day or night</li><li>Private showings booked around your schedule</li><li>Pricing backed by real local sales data</li><li>Professional photos, video and 3D tours for sellers</li></ul></div></div></section>'
    body += f'<section id="areas"><div class="w"><div class="head rv"><span class="kick">Neighbourhoods</span><h2 class="h2">Know the area before you move.</h2></div><div class="tiles">{tiles}</div></div></section>'
    body += '<section><div class="w"><div class="head rv"><span class="kick">How it works</span><h2 class="h2">From first viewing to keys in hand.</h2></div><div class="steps"><div class="st rv"><h3>Tell us what you want</h3><p>Area, budget and must haves. We send matching homes the moment they list.</p></div><div class="st rv"><h3>Tour on your schedule</h3><p>Book showings online, in person or by video.</p></div><div class="st rv"><h3>Win the right home</h3><p>We price your offer with local data and negotiate hard.</p></div><div class="st rv"><h3>Close with confidence</h3><p>Inspections, lenders and paperwork handled, start to finish.</p></div></div></div></section>'
    body += '<section><div class="w"><div class="head c rv"><span class="kick">Clients</span><h2 class="h2">What our clients say.</h2></div>' + quotes([("They answered our enquiry at 10pm and had us viewing the next morning. We had an accepted offer within the week.", "Daniel and Priya", "Bought in " + d["city"]), ("Priced perfectly, marketed beautifully and sold over asking in nine days.", "Margaret L.", "Sold her family home"), ("Every question answered, every step explained. Moving felt easy for the first time.", "Chris T.", "First time buyer")], "Sample reviews and figures (*) for template preview.") + "</div></section>"
    body += f'<section id="value"><div class="w"><div class="cta rv"><div><span class="kick" style="color:inherit;opacity:.7">Thinking of selling?</span><h2 class="h2">What is your home worth today?</h2><p class="lead">Get a free, no obligation valuation from a local expert within 24 hours.</p></div><div><form class="form"><input placeholder="Property address" required><input placeholder="Your name" required><input type="email" placeholder="Email" required><button class="btn">Get my free valuation</button></form><div class="ok">Thanks. In a live site, this request goes straight to your CRM and your phone.</div></div></div></div></section>'
    body += foot(d["name"], [("Buy", ["Homes for sale", "New listings", "Open houses"]), ("Sell", ["Home valuation", "Seller guide", "Sold homes"]), ("Contact", [d["phone"], "hello@" + d["slug"] + ".com", d["city"]])])
    page("real-estate", d, body)

# ---------------------------------------------------------------- e-commerce
PNAMES = {"Watches and jewellery": ["Meridian Automatic", "Noir Chronograph", "Aurora Pendant", "Heritage Field"], "Fashion": ["Linen Wrap Dress", "Tailored Blazer", "Silk Midi Skirt", "Cashmere Knit"], "Sneakers": ["Aero Runner", "Court Classic", "Flux Trainer", "Street Low"],
          "Audio and tech": ["Aura One", "Aura Studio", "Aura Buds", "Aura Speaker"], "Skincare": ["Glow Serum", "Daily Cleanser", "Night Repair Oil", "Barrier Cream"], "Streetwear": ["Heavy Hoodie", "Boxy Tee", "Cargo Pant", "Drop 07 Jacket"],
          "Coffee": ["Ethiopia Yirgacheffe", "House Espresso", "Colombia Huila", "Decaf Swiss Water"], "Furniture": ["Oak Lounge Chair", "Steel Side Table", "Linen Sofa", "Walnut Shelf"], "Electronics": ["Volt X Pro", "Volt Lite", "Volt Book 14", "Volt Charge Pad"], "Fragrance": ["Nuit Ambrée", "Fleur de Sel", "Bois Sacré", "Discovery Set"]}
PRICES = [189, 249, 129, 319]
def ec_page(d, i):
    c, s = "ec", d["s"]
    names = PNAMES[d["kind"]]
    pimg = lambda p: im(c, p[1]) if p[0] == "ec" else st(p[0], p[1])
    scale = 6 if d["kind"] in ("Watches and jewellery",) else (3 if d["kind"] in ("Furniture", "Electronics") else (.12 if d["kind"] == "Coffee" else 1))
    prods = "".join(f'''<article class="card rv"><div class="im"><img src="{pimg(p)}" alt="" loading="lazy">{'<span class="tag">Bestseller</span>' if k == 0 else ('<span class="tag">New</span>' if k == 2 else '')}</div><div class="bd"><span class="stars">★★★★★</span> <small style="color:var(--mute)">({48 + k*31})</small><h3>{names[k]}</h3><div class="price" style="font-size:22px">${max(12, int(PRICES[k]*scale)):,}</div><button class="add">Add to cart</button></div></article>''' for k, p in enumerate(d["prods"]))
    cats = ["New in", "Bestsellers", "Gift sets", "Last chance"]
    tiles = "".join(f'<a class="tile rv" href="#shop"><img src="{im(c, x)}" alt="" loading="lazy"><div><b>{cats[k]}</b><span>Shop now →</span></div></a>' for k, x in enumerate(d["tiles"]))
    d.setdefault("kicker", d["kind"])
    d["badge"] = '<div class="badge"><b>4.9★</b>from 2,300+ reviews*</div>'
    extra = '<div class="ctas"><a class="btn" href="#shop">Shop the collection</a><a class="btn o" href="#story">Our story</a></div><div class="trust"><span>Free shipping over $75</span><span>30 day returns</span><span>Secure checkout</span></div>'
    body = nav(d["name"], [("Shop", "shop"), ("Collections", "cats"), ("Story", "story"), ("Reviews", "reviews")], ("Shop now", "shop"), cart=True) + hero(d, "ecommerce", im(c, d["hero"]), extra)
    claims = ["Free shipping over $75", "30 day returns", "Secure checkout", "Gift wrapping", "Klarna and Afterpay", "Ships in 24 hours"]
    mq = "".join(f"<span>✦ {x}</span>" for x in claims)
    body += f'<div class="mq" aria-hidden="true"><div>{mq}{mq}</div></div>'
    body += f'<section id="cats"><div class="w"><div class="head rv"><span class="kick">Collections</span><h2 class="h2">Find your next favourite.</h2></div><div class="tiles">{tiles}</div></div></section>'
    body += f'<section id="shop"><div class="w"><div class="head rv"><span class="kick">Bestsellers</span><h2 class="h2">Loved by thousands.</h2></div><div class="grid g4">{prods}</div></div></section>'
    body += f'<section id="story"><div class="w story"><div class="ph rv"><img src="{im(c, d["story"])}" alt="" loading="lazy"></div><div class="rv"><span class="kick">Our story</span><h2 class="h2">Made with care, built to last.</h2><p class="lead">We started {E(d["name"])} because we could not find {E(d["kind"].lower())} that looked this good and lasted this long. So we made it ourselves.</p><ul><li>Small batches, carefully finished</li><li>Responsibly sourced materials</li><li>Every order checked by hand</li><li>Real people answering every message</li></ul></div></div></section>'
    body += '<section><div class="w"><div class="feat"><div class="f rv"><div class="ic"><i class="ph ph-truck"></i></div><h3>Fast, free shipping</h3><p>Orders over $75 ship free and arrive in 2 to 4 days.</p></div><div class="f rv"><div class="ic"><i class="ph ph-arrow-counter-clockwise"></i></div><h3>30 day returns</h3><p>Not right? Send it back free. No questions asked.</p></div><div class="f rv"><div class="ic"><i class="ph ph-lock-key"></i></div><h3>Secure checkout</h3><p>Pay by card, Apple Pay, Google Pay or in instalments.</p></div></div></div></section>'
    body += '<section id="reviews"><div class="w"><div class="head c rv"><span class="kick">Reviews</span><h2 class="h2">Don\'t take our word for it.</h2></div>' + quotes([("Arrived in two days, beautifully packed, and even better in person.", "Amara O.", "Verified buyer"), ("The quality is unreal for the price. Already ordered my second.", "Jordan P.", "Verified buyer"), ("Customer service replied in minutes when I needed to change my size.", "Lucy W.", "Verified buyer")], "Sample reviews and figures (*) for template preview.") + "</div></section>"
    body += '<section><div class="w"><div class="cta rv"><div><span class="kick" style="color:inherit;opacity:.7">Join the list</span><h2 class="h2">Get 10% off your first order.</h2><p class="lead">New drops, restocks and members only offers. No spam, ever.</p></div><div><form class="form"><input type="email" placeholder="Your email" required><button class="btn">Get my 10% code</button></form><div class="ok">Thanks. In a live store, this adds the subscriber to your email marketing automatically.</div></div></div></div></section>'
    body += foot(d["name"], [("Shop", ["New in", "Bestsellers", "Gift cards"]), ("Help", ["Shipping", "Returns", "Contact us"]), ("Follow", ["Instagram", "TikTok", "Pinterest"])])
    page("ecommerce", d, body)

# ---------------------------------------------------------------- home services
def hs_page(d, i):
    c = "hs"
    svc = "".join(f'<div class="f rv"><div class="ic"><i class="ph {HS_ICONS[k % 6]}"></i></div><h3>{x}</h3><p>Upfront pricing, tidy work and a written guarantee on every job.</p></div>' for k, x in enumerate(d["svc"]))
    d.setdefault("kicker", "Licensed · Insured · Local")
    d["badge"] = '<div class="badge"><b>4.9★</b>from 800+ local reviews*</div>'
    extra = f'<div class="ctas"><a class="btn" href="#quote">Get a free quote</a><a class="btn o" href="#quote">Call {d["phone"]}</a></div><div class="trust"><span>Licensed and insured</span><span>Same week appointments</span><span>Workmanship guarantee</span></div>'
    areas = ["North side", "Downtown", "East county", "Suburbs"]
    tiles = "".join(f'<a class="tile rv" href="#quote"><img src="{im(c, x)}" alt="" loading="lazy"><div><b>{areas[k]}</b><span>Same week availability</span></div></a>' for k, x in enumerate(d["photos"]))
    body = nav(d["name"], [("Services", "services"), ("Our work", "work"), ("Reviews", "reviews"), ("Areas", "areas")], ("Free quote", "quote")) + hero(d, "home-services", im(c, d["hero"]), extra)
    body += stats([("25+", "years of experience*"), ("12,000", "jobs completed*"), ("60 min", "average response*"), ("100%", "satisfaction guarantee")])
    body += f'<section id="services"><div class="w"><div class="head rv"><span class="kick">Services</span><h2 class="h2">Everything your home needs, done properly.</h2></div><div class="feat">{svc}</div></div></section>'
    body += f'<section id="work"><div class="w"><div class="head rv"><span class="kick">Our work</span><h2 class="h2">See the difference.</h2></div><div class="ba"><figure class="rv"><img src="{im(c, d["ba"][0])}" alt="" loading="lazy"><figcaption>Before</figcaption></figure><figure class="rv"><img src="{im(c, d["ba"][1])}" alt="" loading="lazy"><figcaption>After</figcaption></figure></div></div></section>'
    body += '<section><div class="w"><div class="head rv"><span class="kick">How it works</span><h2 class="h2">Booked in a minute. Done right the first time.</h2></div><div class="steps"><div class="st rv"><h3>Book online</h3><p>Pick a time that suits you. We confirm by text instantly.</p></div><div class="st rv"><h3>Fixed quote</h3><p>We inspect and give you a clear, fixed price before any work.</p></div><div class="st rv"><h3>Expert work</h3><p>Licensed pros, tidy sites and updates as we go.</p></div><div class="st rv"><h3>Guaranteed</h3><p>Not happy? We come back and make it right, free.</p></div></div></div></section>'
    body += f'<section id="areas"><div class="w"><div class="head rv"><span class="kick">Service areas</span><h2 class="h2">Local, and proud of it.</h2></div><div class="tiles">{tiles}</div></div></section>'
    body += '<section id="reviews"><div class="w"><div class="head c rv"><span class="kick">Reviews</span><h2 class="h2">Neighbours who recommend us.</h2></div>' + quotes([("Called in the morning, fixed by the afternoon. Clear price, no surprises.", "Robert H.", "Homeowner"), ("Tidy, polite and genuinely skilled. The best trades team we have used.", "Angela M.", "Homeowner"), ("They texted when they were on the way and finished ahead of schedule.", "Kevin S.", "Property manager")], "Sample reviews and figures (*) for template preview.") + "</div></section>"
    body += f'<section id="quote"><div class="w"><div class="cta rv"><div><span class="kick" style="color:inherit;opacity:.7">Free quote</span><h2 class="h2">Tell us what you need.</h2><p class="lead">We reply within minutes during business hours, and book you in the same week.</p></div><div><form class="form"><select><option>{d["svc"][0]}</option>' + "".join(f"<option>{x}</option>" for x in d["svc"][1:]) + f'</select><input placeholder="Your name" required><input placeholder="Phone or email" required><button class="btn">Get my free quote</button></form><div class="ok">Thanks. In a live site, this lead is texted back instantly and lands in your CRM.</div></div></div></div></section>'
    body += foot(d["name"], [("Services", d["svc"][:3]), ("Company", ["About us", "Reviews", "Careers"]), ("Contact", [d["phone"], "Mon to Sat, 7am to 7pm", "Emergency line 24/7"])])
    page("home-services", d, body)

# ---------------------------------------------------------------- category index pages
def cat_page(cat, items):
    title, c, sub = CATS[cat]
    cards = "".join(f'''<a class="tcard" href="/t/{cat}/{d["slug"]}/"><div class="shot"><img src="/assets/tpl/shots/{cat}-{d["slug"]}.jpg" alt="{E(d["name"])} template preview" loading="lazy"></div><div class="meta"><span>{k:02d} · {STYLE[d["s"]]}</span><b>{E(d["name"])}</b><em>Live preview →</em></div></a>''' for k, d in enumerate(items, 1))
    others = "".join(f'<a href="/{k}/"{" aria-current=page" if k == cat else ""}>{v[0]}</a>' for k, v in CATS.items())
    out = f'''<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title} · 10 templates · Vix Assist</title><meta name="description" content="{E(sub)} Ten premium templates, each built to convert and connected to GoHighLevel.">
<link rel="icon" href="/assets/favicon.svg" type="image/svg+xml"><link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&family=Instrument+Serif:ital@0;1&display=swap" rel="stylesheet">
<link rel="stylesheet" href="/assets/tpl/gallery.css?v=1"></head><body>
<header class="gnav"><div class="gw"><a class="glogo" href="/"><img src="/assets/logo.svg" alt="" width="28" height="28">Vix <span>Assist</span> <small>Websites</small></a><nav>{others}</nav><a class="gbtn" href="/#brief">Start your website</a></div></header>
<main><section class="ghero"><div class="gw"><span class="gk">10 templates</span><h1>{title.replace(" websites", "")} websites that <em>sell for you.</em></h1><p>{E(sub)} Pick a style, open the live preview, and I'll build it for your brand, connected to GoHighLevel so every enquiry is answered in seconds.</p></div></section>
<section class="ggrid"><div class="gw">{cards}</div></section>
<section class="gcta"><div class="gw"><h2>Like one? <em>It can be yours in days.</em></h2><p>Every template is adapted to your brand, your photos and your words, then connected to your CRM.</p><div><a class="gbtn" href="/#brief">Start your website</a> <a class="gbtn o" href="{MAIN}/book.html">Book a call</a></div></div></section></main>
<footer class="gfoot"><div class="gw">© 2026 Vix Assist · <a href="{MAIN}">vixassist.com</a> · Templates use sample brands and royalty free photos.</div></footer></body></html>'''
    p = os.path.join(ROOT, cat); os.makedirs(p, exist_ok=True)
    open(os.path.join(p, "index.html"), "w", encoding="utf-8").write(out)

if __name__ == "__main__":
    for i, d in enumerate(RE): re_page(dict(d), i)
    for i, d in enumerate(EC): ec_page(dict(d), i)
    for i, d in enumerate(HS): hs_page(dict(d), i)
    cat_page("real-estate", RE); cat_page("ecommerce", EC); cat_page("home-services", HS)
    print("built 30 templates + 3 category pages")
