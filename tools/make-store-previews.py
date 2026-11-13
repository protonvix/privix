"""Builds a personalised online-store preview for each retail prospect: p/<slug>/index.html.

Run from the repo root:  python3 tools/make-store-previews.py
Add a store to STORES below, run the script, then commit and push.
Photos live in assets/stores/<kind>-<n>.jpg (Unsplash licence, self-hosted).
"""
import html
import json
import pathlib

ROOT = pathlib.Path(__file__).resolve().parent.parent
BASE = "https://vixautomationsportfolio.pages.dev"

# slug, name, kind, area, social label, social url, phone (optional), accent
STORES = [
    ("phonespot", "Phone Spot", "phones", "St Mary Street, Weymouth", "@phonespot_weymouth", "https://www.instagram.com/phonespot_weymouth/", "", "#2F6BFF"),
    ("foneworld", "Fone World Fareham", "phones", "Fareham", "@foneworldfareham", "https://www.instagram.com/foneworldfareham/", "", "#7C3AED"),
    ("phoneaccessorieshud", "Phone Accessories Huddersfield", "phones", "Huddersfield", "@phoneaccessories_hud", "https://www.instagram.com/phoneaccessories_hud/", "", "#0EA5A4"),
    ("thephoneshopsheffield", "The Phone Shop Sheffield", "phones", "Sheffield", "@thephoneshop6", "https://www.instagram.com/thephoneshop6/", "", "#E11D48"),
    ("bargainsdelivered", "Bargains Delivered", "furniture", "Rotherham", "Facebook", "https://www.facebook.com/bargainsdelivered.woodmanfurniture/", "", "#B45309"),
    ("sofaandbedwarehouse", "The Sofa and Bed Warehouse", "furniture", "Meynell Road, Darlington", "Facebook", "https://www.facebook.com/Thesofaandbedwarehouse/", "", "#1F6F5C"),
    ("bluebelles", "Blue Belles Boutique", "fashion", "Delivered across the UK", "@blue_belles_boutique", "https://www.instagram.com/blue_belles_boutique/", "", "#3B6FD8"),
    ("pureladies", "Pure Ladies Boutique", "fashion", "UK ladies' boutique", "@pureladiesboutiques", "https://www.instagram.com/pureladiesboutiques/", "", "#B83280"),
    ("bristolboutique", "Bristol Boutique & Co.", "fashion", "Bristol", "@shopbristolboutique", "https://www.instagram.com/shopbristolboutique/", "", "#8B5E3C"),
    ("pinklemons", "Pink Lemons Studio", "fashion", "Essex · Worldwide shipping", "@pinklemonsstudio", "https://www.instagram.com/pinklemonsstudio/", "", "#EC4899"),
    ("bela", "Bela Boutique", "fashion", "UK family boutique", "@bela.uk", "https://www.instagram.com/bela.uk/", "", "#9F7AEA"),
    ("newlobo", "New Lobo Hair & Cosmetics", "beauty", "Enfield · Haringey", "@afro_hair_fashion", "https://www.instagram.com/afro_hair_fashion/", "", "#C2410C"),
    ("afroeuro", "Afroeuro Hair and Beauty", "beauty", "Hair & beauty store", "@afroeuro_hairandbeauty", "https://www.instagram.com/afroeuro_hairandbeauty/", "", "#A21CAF"),
    ("lordbros", "Lord Bros Electrical", "electrical", "Alford, Lincolnshire", "Facebook", "https://www.facebook.com/search/top?q=Lord%20Bros%20Electrical", "01507 472691", "#1D4ED8"),
]

KINDS = {
    "phones": dict(
        eyebrow="Phones · Repairs · Accessories",
        h1="Fixed today. <em>Like new tomorrow.</em>",
        lead="Same-day screen and battery repairs, quality accessories and great-value phones. Book online in a minute or walk straight in.",
        cta1="Book a repair", cta2="Shop accessories",
        trust=["Same-day repairs", "Warranty on every repair", "Free diagnostics"],
        cats=["All", "Phones", "Audio", "Wearables"],
        products=[
            (1, "iPhone 13 · Refurbished", "Phones", 379, "Graded A"),
            (2, "iPhone 12 · Refurbished", "Phones", 299, ""),
            (3, "Samsung Galaxy S22", "Phones", 329, "Unlocked"),
            (4, "iPhone 11 · 128GB", "Phones", 239, "Best value"),
            (5, "Wireless earbuds", "Audio", 39, ""),
            (6, "Over-ear headphones", "Audio", 89, "New in"),
            (7, "Smartwatch", "Wearables", 129, ""),
            (8, "Studio headphones", "Audio", 59, ""),
        ],
        service_h2="Book a repair in 60 seconds",
        service_sub="Pick your device and the problem. We'll confirm a time and an exact price before we start.",
        service_items=[("Screen replacement", "from £49"), ("Battery replacement", "from £39"), ("Charging port", "from £35"), ("Water damage", "Free check")],
        form=[("Device", "select", ["iPhone", "Samsung", "Google Pixel", "iPad / tablet", "Other"]), ("Problem", "select", ["Cracked screen", "Battery", "Charging port", "Camera", "Water damage", "Other"]), ("Preferred day", "date", None)],
        submit="Request my repair",
        why=[("Same-day fixes", "Most screens and batteries done while you wait."), ("Genuine-grade parts", "Quality parts with a warranty on every repair."), ("Clear prices", "You get the exact price before we touch your phone."), ("Trade-ins", "Swap your old phone for money off a new one.")],
    ),
    "furniture": dict(
        eyebrow="Sofas · Beds · Mattresses",
        h1="Beautiful furniture. <em>Bargain prices.</em>",
        lead="Sofas, beds and mattresses for every room and budget, delivered to your door and assembled for you. Visit the showroom or order online.",
        cta1="Shop the range", cta2="Visit the showroom",
        trust=["Free local delivery", "Assembly available", "Spread the cost"],
        cats=["All", "Sofas", "Beds", "Chairs"],
        products=[
            (2, "Velvet 3-seater sofa", "Sofas", 549, "Bestseller"),
            (3, "Upholstered king bed", "Beds", 449, ""),
            (4, "Ottoman double bed", "Beds", 399, "New in"),
            (5, "Low oak bed frame", "Beds", 329, ""),
            (6, "Accent armchair", "Chairs", 189, ""),
            (7, "Dining chair (set of 2)", "Chairs", 99, "Price drop"),
            (8, "Corner lounge suite", "Sofas", 899, ""),
            (9, "Scandi side chair", "Chairs", 59, ""),
        ],
        service_h2="Delivered, assembled, old one taken away",
        service_sub="Tell us what you're after and your postcode. We'll check stock and give you a delivery date.",
        service_items=[("Local delivery", "Free"), ("Assembly", "from £30"), ("Old furniture removal", "from £25"), ("Pay monthly", "Ask in store")],
        form=[("Looking for", "select", ["Sofa", "Bed", "Mattress", "Bedroom furniture", "Dining", "Other"]), ("Postcode", "text", "e.g. S60 1AA"), ("Budget", "select", ["Under £300", "£300 to £600", "£600 to £1,000", "Above £1,000"])],
        submit="Send my enquiry",
        why=[("Showroom prices", "Big-brand style without the big-brand price."), ("Delivered to your room", "Our own team delivers and assembles."), ("See it first", "Sit on it, lie on it, then decide."), ("Local and family-run", "Real people who answer the phone.")],
    ),
    "fashion": dict(
        eyebrow="New season · Just landed",
        h1="Pieces you'll <em>live in.</em>",
        lead="Hand-picked dresses, co-ords, bags and accessories. New drops every week, easy sizing help and fast UK delivery.",
        cta1="Shop new in", cta2="Get styling help",
        trust=["Fast UK delivery", "Easy returns", "Secure checkout"],
        cats=["All", "Dresses", "Bags", "Shoes", "Accessories"],
        products=[
            (2, "Wrap midi dress", "Dresses", 48, "New in"),
            (3, "Flowing maxi dress", "Dresses", 62, ""),
            (4, "Structured top-handle bag", "Bags", 45, "Bestseller"),
            (5, "Printed stiletto heels", "Shoes", 55, ""),
            (6, "Pearl necklace", "Accessories", 28, ""),
            (7, "Tailored joggers", "Dresses", 38, ""),
            (8, "Fringe knit poncho", "Accessories", 34, "Last few"),
            (9, "Belted trench coat", "Dresses", 79, ""),
        ],
        service_h2="Not sure about sizing or styling?",
        service_sub="Tell us the occasion and your size. We'll send outfit ideas and check stock for you.",
        service_items=[("Personal styling", "Free"), ("Size advice", "Free"), ("Gift wrapping", "£3"), ("Next-day delivery", "£4.95")],
        form=[("Occasion", "select", ["Everyday", "Wedding guest", "Night out", "Holiday", "Work", "Other"]), ("Dress size", "select", ["6", "8", "10", "12", "14", "16", "18", "20+"]), ("Budget", "select", ["Under £50", "£50 to £100", "£100+"])],
        submit="Get outfit ideas",
        why=[("New drops weekly", "Fresh pieces every week, never mass-market."), ("Sizes that fit", "Honest size guides and real advice."), ("Pay your way", "Card, Apple Pay and Klarna-ready checkout."), ("Loved by locals", "A boutique experience, online.")],
    ),
    "beauty": dict(
        eyebrow="Hair · Wigs · Beauty",
        h1="Everything for <em>your crown.</em>",
        lead="Braiding hair, wigs, extensions, hair care and beauty from the brands you trust. Shop online, click and collect, or visit us in store.",
        cta1="Shop hair & beauty", cta2="Click & collect",
        trust=["Click & collect", "Trusted brands", "Expert advice in store"],
        cats=["All", "Makeup", "Hair care", "Skin care"],
        products=[
            (2, "Pro makeup brush set", "Makeup", 24, "Bestseller"),
            (3, "Eyeshadow & bronzer kit", "Makeup", 19, ""),
            (4, "Everyday makeup bundle", "Makeup", 32, "New in"),
            (5, "Curl shampoo & conditioner", "Hair care", 16, ""),
            (6, "Repair hair mask", "Hair care", 12, ""),
            (7, "Daily moisturiser", "Skin care", 14, ""),
            (8, "Edge control & gels", "Hair care", 6, "Popular"),
            (9, "Wig & braid essentials", "Hair care", 22, ""),
        ],
        service_h2="Reserve it, collect it today",
        service_sub="Tell us what you need. We'll check stock and keep it aside for you at the counter.",
        service_items=[("Click & collect", "Free"), ("Wig fitting advice", "Free"), ("Local delivery", "from £3.95"), ("Bulk / salon orders", "Ask us")],
        form=[("Looking for", "select", ["Braiding hair", "Wig", "Extensions", "Hair care", "Makeup", "Skin care"]), ("Brand or colour", "text", "e.g. X-pression 1B"), ("Collect or deliver", "select", ["Collect in store", "Deliver to me"])],
        submit="Reserve my items",
        why=[("Huge range", "Hair, wigs, care and beauty under one roof."), ("Real advice", "Staff who know textures, lengths and brands."), ("Fair prices", "Everyday low prices and bundle deals."), ("Collect fast", "Reserve online, pick up the same day.")],
    ),
    "electrical": dict(
        eyebrow="TVs · Laundry · Kitchen appliances",
        h1="Local electricals. <em>Delivered and fitted.</em>",
        lead="TVs, washing machines, fridges and cookers from leading brands, with local delivery, installation and old-appliance removal by our own team.",
        cta1="Shop appliances", cta2="Call the store",
        trust=["Local delivery & install", "Old appliance removed", "Leading brands"],
        cats=["All", "TV", "Laundry", "Kitchen"],
        products=[
            (2, "55\" 4K Smart TV", "TV", 499, "Bestseller"),
            (3, "65\" 4K HDR TV", "TV", 799, ""),
            (4, "9kg washing machine", "Laundry", 379, "Free install"),
            (5, "8kg washer dryer", "Laundry", 549, ""),
            (6, "Retro fridge freezer", "Kitchen", 649, "New in"),
            (7, "Built-in single oven", "Kitchen", 399, ""),
            (8, "Countertop mini oven", "Kitchen", 89, ""),
            (9, "Coffee & kitchen bundle", "Kitchen", 149, ""),
        ],
        service_h2="Need it delivered and fitted?",
        service_sub="Tell us what you need. We'll confirm price, stock and a delivery slot, and take the old one away.",
        service_items=[("Local delivery", "Free"), ("Installation", "from £25"), ("Old appliance removal", "Free with install"), ("Repairs & servicing", "Call us")],
        form=[("Looking for", "select", ["TV", "Washing machine", "Tumble dryer", "Fridge freezer", "Cooker / oven", "Other"]), ("Postcode", "text", "e.g. LN13 9AA"), ("When", "select", ["As soon as possible", "This week", "Just browsing"])],
        submit="Send my request",
        why=[("Family-run", "Real local service you won't get online."), ("Fitted for you", "Our own engineers deliver and install."), ("Price match", "Ask us to match a fair online price."), ("After-sales care", "We're here when you need us.")],
    ),
}

CSS = r"""
:root{--a:ACCENT;--ink:#14121f;--mute:#5b5870;--soft:#8a879c;--line:#e9e7f1;--bg:#fbfaf8;--card:#fff}
*{box-sizing:border-box}html{scroll-behavior:smooth}
body{margin:0;font-family:'DM Sans',system-ui,-apple-system,Segoe UI,Roboto,sans-serif;color:var(--ink);background:var(--bg);-webkit-font-smoothing:antialiased}
img{max-width:100%;display:block}a{color:inherit;text-decoration:none}
.wrap{width:min(1180px,100% - 32px);margin:0 auto}
.ribbon{background:#14121f;color:#fff;font-size:12.5px;text-align:center;padding:8px 14px;line-height:1.45}
.ribbon b{color:#fff}.ribbon a{color:#b9b4ff;text-decoration:underline}
header{position:sticky;top:0;z-index:30;background:rgba(251,250,248,.86);backdrop-filter:blur(14px);border-bottom:1px solid var(--line)}
.nav{display:flex;align-items:center;gap:18px;height:68px}
.logo{display:flex;align-items:center;gap:10px;font-weight:800;font-size:17px;letter-spacing:-.02em}
.logo i{width:38px;height:38px;border-radius:12px;background:var(--a);color:#fff;display:grid;place-items:center;font-style:normal;font-size:14px;letter-spacing:.02em}
.links{display:flex;gap:22px;margin-left:auto;font-size:14.5px;color:var(--mute)}
.links a:hover{color:var(--ink)}
.bag{position:relative;border:1px solid var(--line);background:#fff;border-radius:999px;padding:9px 14px;font:600 14px inherit;font-family:inherit;cursor:pointer;display:flex;gap:7px;align-items:center}
.bag b{background:var(--a);color:#fff;border-radius:999px;min-width:20px;height:20px;font-size:11px;display:grid;place-items:center;padding:0 6px}
.hero{display:grid;grid-template-columns:1.05fr 1fr;gap:44px;align-items:center;padding:56px 0 40px}
.eyebrow{display:inline-flex;gap:8px;align-items:center;font-size:12.5px;font-weight:700;letter-spacing:.08em;text-transform:uppercase;color:var(--a);background:color-mix(in srgb,var(--a) 10%,#fff);padding:7px 12px;border-radius:999px}
h1{font-family:'Fraunces',Georgia,serif;font-weight:600;font-size:clamp(40px,6vw,72px);line-height:1.02;letter-spacing:-.03em;margin:18px 0 16px}
h1 em{font-style:italic;color:var(--a)}
.lead{font-size:18px;line-height:1.6;color:var(--mute);max-width:520px;margin:0 0 26px}
.btns{display:flex;flex-wrap:wrap;gap:12px}
.btn{display:inline-flex;align-items:center;justify-content:center;gap:8px;padding:15px 24px;border-radius:999px;font-weight:700;font-size:15px;border:0;cursor:pointer;font-family:inherit;transition:transform .2s,box-shadow .2s}
.btn.p{background:var(--a);color:#fff;box-shadow:0 12px 30px -12px var(--a)}
.btn.p:hover{transform:translateY(-2px)}
.btn.g{background:#fff;border:1px solid var(--line);color:var(--ink)}
.trust{display:flex;flex-wrap:wrap;gap:10px 22px;margin-top:26px;font-size:14px;color:var(--mute)}
.trust span{display:flex;gap:7px;align-items:center}.trust svg{width:17px;height:17px;color:var(--a)}
.hero-art{position:relative;border-radius:28px;overflow:hidden;aspect-ratio:4/4.4;box-shadow:0 40px 80px -40px rgba(20,18,31,.45)}
.hero-art img{width:100%;height:100%;object-fit:cover;transform:scale(1.04);animation:zoom 14s ease-in-out infinite alternate}
@keyframes zoom{to{transform:scale(1.12)}}
.float{position:absolute;left:18px;bottom:18px;right:18px;display:flex;gap:12px;align-items:center;background:rgba(255,255,255,.92);backdrop-filter:blur(8px);border-radius:18px;padding:14px 16px;font-size:14px}
.float b{display:block;font-size:15px}.float small{color:var(--mute)}
.float i{width:42px;height:42px;border-radius:12px;background:var(--a);flex:none;display:grid;place-items:center;color:#fff;font-style:normal;font-size:20px}
.strip{border-block:1px solid var(--line);background:#fff;overflow:hidden}
.marq{display:flex;gap:46px;padding:16px 0;white-space:nowrap;animation:mq 26s linear infinite;font-weight:700;color:var(--mute);font-size:14px;letter-spacing:.04em;text-transform:uppercase}
.marq span::before{content:"✦";color:var(--a);margin-right:14px}
@keyframes mq{to{transform:translateX(-50%)}}
section{padding:72px 0}
.head{display:flex;justify-content:space-between;align-items:flex-end;gap:20px;flex-wrap:wrap;margin-bottom:26px}
h2{font-family:'Fraunces',Georgia,serif;font-weight:600;font-size:clamp(30px,4vw,44px);letter-spacing:-.025em;margin:0 0 8px;line-height:1.08}
.sub{color:var(--mute);margin:0;font-size:16px;line-height:1.6;max-width:560px}
.chips{display:flex;gap:8px;flex-wrap:wrap}
.chip{border:1px solid var(--line);background:#fff;border-radius:999px;padding:9px 16px;font:600 14px inherit;font-family:inherit;cursor:pointer;color:var(--mute)}
.chip.on{background:var(--ink);color:#fff;border-color:var(--ink)}
.grid{display:grid;grid-template-columns:repeat(4,1fr);gap:18px}
.card{background:var(--card);border:1px solid var(--line);border-radius:22px;overflow:hidden;display:flex;flex-direction:column;transition:transform .25s,box-shadow .25s}
.card:hover{transform:translateY(-4px);box-shadow:0 24px 50px -30px rgba(20,18,31,.35)}
.ph{position:relative;aspect-ratio:1/1.05;background:#f1eff6;overflow:hidden}
.ph img{width:100%;height:100%;object-fit:cover;transition:transform .5s}
.card:hover .ph img{transform:scale(1.06)}
.tag{position:absolute;top:12px;left:12px;background:#fff;color:var(--ink);font-size:11.5px;font-weight:700;padding:5px 10px;border-radius:999px}
.ci{padding:14px 16px 16px;display:grid;gap:6px;flex:1}
.ci small{color:var(--soft);font-size:12px;text-transform:uppercase;letter-spacing:.07em;font-weight:700}
.ci b{font-size:15.5px;line-height:1.3}
.row{display:flex;align-items:center;justify-content:space-between;margin-top:auto;padding-top:6px}
.price{font-weight:800;font-size:17px}
.add{border:0;background:color-mix(in srgb,var(--a) 12%,#fff);color:var(--a);font:700 13.5px inherit;font-family:inherit;padding:9px 14px;border-radius:999px;cursor:pointer}
.add:hover{background:var(--a);color:#fff}
.svc{background:#14121f;color:#fff;border-radius:32px;padding:46px;display:grid;grid-template-columns:1fr 1fr;gap:40px}
.svc .sub{color:#c9c6d8}
.items{display:grid;gap:10px;margin-top:22px}
.items div{display:flex;justify-content:space-between;padding:14px 16px;border-radius:14px;background:rgba(255,255,255,.06);border:1px solid rgba(255,255,255,.1);font-size:15px}
.items b{color:color-mix(in srgb,var(--a) 55%,#fff)}
form{background:#fff;color:var(--ink);border-radius:24px;padding:26px;display:grid;gap:14px;align-self:start}
label{display:grid;gap:6px;font-size:13px;font-weight:700;color:var(--mute)}
input,select{font:15px inherit;font-family:inherit;padding:13px 14px;border-radius:12px;border:1px solid var(--line);background:#fbfaf8;color:var(--ink);width:100%}
.two{display:grid;grid-template-columns:1fr 1fr;gap:12px}
.ok{display:none;background:color-mix(in srgb,var(--a) 10%,#fff);color:var(--ink);border-radius:14px;padding:14px;font-size:14px}
.why{display:grid;grid-template-columns:repeat(4,1fr);gap:16px}
.tile{background:#fff;border:1px solid var(--line);border-radius:22px;padding:22px}
.tile i{width:44px;height:44px;border-radius:14px;background:color-mix(in srgb,var(--a) 12%,#fff);color:var(--a);display:grid;place-items:center;font-style:normal;font-weight:800;margin-bottom:14px}
.tile h3{margin:0 0 6px;font-size:17px}.tile p{margin:0;color:var(--mute);font-size:14.5px;line-height:1.55}
.visit{display:grid;grid-template-columns:1fr 1fr;gap:20px;align-items:stretch}
.vimg{border-radius:26px;overflow:hidden;min-height:320px}.vimg img{width:100%;height:100%;object-fit:cover}
.vbox{background:#fff;border:1px solid var(--line);border-radius:26px;padding:34px;display:grid;gap:16px;align-content:center}
.vbox p{margin:0;display:flex;gap:10px;color:var(--mute);font-size:15.5px}
.vbox p b{color:var(--ink)}
footer{border-top:1px solid var(--line);padding:30px 0 40px;color:var(--soft);font-size:13.5px}
.foot{display:flex;justify-content:space-between;gap:16px;flex-wrap:wrap}
.drawer{position:fixed;inset:0;z-index:60;display:none}
.drawer.open{display:block}
.shade{position:absolute;inset:0;background:rgba(20,18,31,.45)}
.panel{position:absolute;right:0;top:0;bottom:0;width:min(400px,100%);background:#fff;padding:22px;display:flex;flex-direction:column;gap:14px;animation:slide .3s ease}
@keyframes slide{from{transform:translateX(100%)}}
.panel h3{margin:0;font-size:20px;display:flex;justify-content:space-between}
.panel h3 button{border:0;background:none;font-size:22px;cursor:pointer}
.lines{flex:1;overflow:auto;display:grid;gap:10px;align-content:start}
.line{display:grid;grid-template-columns:56px 1fr auto;gap:12px;align-items:center;font-size:14px}
.line img{width:56px;height:56px;border-radius:12px;object-fit:cover}
.tot{display:flex;justify-content:space-between;font-weight:800;font-size:18px;border-top:1px solid var(--line);padding-top:14px}
.note{font-size:12.5px;color:var(--soft);margin:0}
.toast{position:fixed;left:50%;bottom:22px;transform:translateX(-50%) translateY(120px);background:var(--ink);color:#fff;padding:12px 18px;border-radius:999px;font-size:14px;z-index:70;transition:transform .3s}
.toast.show{transform:translateX(-50%) translateY(0)}
.rv{opacity:0;transform:translateY(18px);transition:opacity .7s,transform .7s}.rv.in{opacity:1;transform:none}
@media (max-width:980px){.grid{grid-template-columns:repeat(2,1fr)}.why{grid-template-columns:repeat(2,1fr)}.svc{grid-template-columns:1fr;padding:30px 22px}}
@media (max-width:760px){.links{display:none}.hero{grid-template-columns:1fr;padding:30px 0 26px;gap:28px}.visit{grid-template-columns:1fr}section{padding:52px 0}.lead{font-size:16.5px}.logo span{max-width:180px;line-height:1.15}}
@media (max-width:440px){.grid{gap:12px}.ci{padding:12px}.ci b{font-size:14px}.price{font-size:15px}.add{padding:8px 11px;font-size:12.5px}.why{grid-template-columns:1fr}.two{grid-template-columns:1fr}.btn{flex:1}}
@media (prefers-reduced-motion:reduce){*{animation:none!important;transition:none!important}}
"""

CHECK = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.4"><path d="M20 6 9 17l-5-5"/></svg>'


def esc(s):
    return html.escape(s, quote=True)


def initials(name):
    words = [w for w in name.replace("&", " ").replace(".", " ").split() if w[0].isalpha() and w.lower() not in ("the", "and", "co")]
    return (words[0][0] + (words[1][0] if len(words) > 1 else "")).upper()


def field(label, kind, opt):
    if kind == "select":
        inner = "<select name=\"%s\">%s</select>" % (esc(label), "".join(f"<option>{esc(o)}</option>" for o in opt))
    elif kind == "date":
        inner = f'<input type="date" name="{esc(label)}">'
    else:
        inner = f'<input name="{esc(label)}" placeholder="{esc(opt or "")}">'
    return f"<label>{esc(label)}{inner}</label>"


def build(slug, name, kind, area, social_label, social_url, phone, accent):
    k = KINDS[kind]
    img = lambda n: f"/assets/stores/{kind}-{n}.jpg"
    products = [dict(img=img(i), name=n, cat=c, price=p, tag=t) for i, n, c, p, t in k["products"]]
    contact_href = f"tel:{phone.replace(' ', '')}" if phone else social_url
    contact_label = f"Call {phone}" if phone else (f"Message us on {social_label}" if social_label == "Facebook" else f"Message {social_label}")
    social_line = f"<p>📱 <span><b>{'Facebook' if social_label == 'Facebook' else 'Instagram'}</b><br><a href=\"{esc(social_url)}\" target=\"_blank\" rel=\"noopener\">{esc(social_label if social_label != 'Facebook' else name + ' on Facebook')}</a></span></p>"
    phone_line = f"<p>📞 <span><b>Phone</b><br><a href=\"tel:{phone.replace(' ', '')}\">{esc(phone)}</a></span></p>" if phone else ""
    trust = "".join(f"<span>{CHECK}{esc(t)}</span>" for t in k["trust"])
    chips = "".join(f'<button class="chip{" on" if i == 0 else ""}" data-c="{esc(c)}">{esc(c)}</button>' for i, c in enumerate(k["cats"]))
    items = "".join(f"<div><span>{esc(a)}</span><b>{esc(b)}</b></div>" for a, b in k["service_items"])
    fields = k["form"]
    form = '<div class="two"><label>Your name<input name="Name" required placeholder="Full name"></label><label>Phone<input name="Phone" type="tel" required placeholder="07..."></label></div>'
    form += "".join(field(*f) for f in fields)
    why = "".join(f'<div class="tile rv"><i>{i + 1:02d}</i><h3>{esc(h)}</h3><p>{esc(p)}</p></div>' for i, (h, p) in enumerate(k["why"]))
    marq = " ".join(f"<span>{esc(t)}</span>" for t in (k["trust"] + [area, "Secure checkout"]) * 2)
    data = json.dumps(dict(products=products), ensure_ascii=False)
    title = f"{name} | {k['eyebrow'].split(' · ')[0]} – website preview"
    return f"""<!doctype html>
<html lang="en-GB"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>{esc(title)}</title>
<meta name="description" content="A website preview designed by Vix Assist for {esc(name)}.">
<meta name="robots" content="noindex">
<meta property="og:title" content="{esc(name)} – new website preview">
<meta property="og:image" content="{BASE}{img(0)}">
<link rel="icon" href="/assets/favicon.svg">
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=DM+Sans:wght@400;500;700;800&family=Fraunces:ital,opsz,wght@0,9..144,600;1,9..144,600&display=swap" rel="stylesheet">
<style>{CSS.replace('ACCENT', accent)}</style></head>
<body>
<div class="ribbon">✨ <b>Website preview designed for {esc(name)}</b> by <a href="https://vixautomations.pages.dev/free-design" target="_blank" rel="noopener">Vix Assist</a>. Sample products and photos. We'll swap in your real stock, prices and logo.</div>
<header><div class="wrap nav">
<a class="logo" href="#top"><i>{esc(initials(name))}</i><span>{esc(name)}</span></a>
<nav class="links"><a href="#shop">Shop</a><a href="#service">{'Repairs' if kind == 'phones' else 'Services'}</a><a href="#why">Why us</a><a href="#visit">Visit</a></nav>
<button class="bag" id="bagBtn" aria-label="Open bag">Bag <b id="count">0</b></button>
</div></header>
<main id="top">
<div class="wrap hero">
<div class="rv in">
<span class="eyebrow">{esc(k['eyebrow'])}</span>
<h1>{k['h1']}</h1>
<p class="lead">{esc(k['lead'])}</p>
<div class="btns"><a class="btn p" href="#{'service' if kind == 'phones' else 'shop'}">{esc(k['cta1'])}</a><a class="btn g" href="{'#shop' if kind == 'phones' else ('tel:' + phone.replace(' ', '') if phone else '#service')}">{esc(k['cta2'])}</a></div>
<div class="trust">{trust}</div>
</div>
<div class="hero-art rv in"><img src="{img(0)}" alt="{esc(name)}" fetchpriority="high">
<div class="float"><i>★</i><div><b>{esc(name)}</b><small>{esc(area)}</small></div></div></div>
</div>
<div class="strip"><div class="marq">{marq}</div></div>

<section id="shop"><div class="wrap">
<div class="head rv"><div><h2>Shop the range</h2><p class="sub">Tap "Add" to build your order. Checkout takes card, Apple Pay and Google Pay.</p></div><div class="chips">{chips}</div></div>
<div class="grid" id="grid"></div>
</div></section>

<section id="service" style="padding-top:0"><div class="wrap"><div class="svc rv">
<div><h2>{esc(k['service_h2'])}</h2><p class="sub">{esc(k['service_sub'])}</p><div class="items">{items}</div></div>
<form id="f">{form}<button class="btn p" type="submit">{esc(k['submit'])}</button><div class="ok" id="ok">✅ Thanks! In the live site this request goes straight to {esc(name)}'s inbox and phone, so you can reply in minutes.</div></form>
</div></div></section>

<section id="why" style="padding-top:0"><div class="wrap">
<div class="head rv"><div><h2>Why shop with {esc(name)}</h2></div></div>
<div class="why">{why}</div>
</div></section>

<section id="visit" style="padding-top:0"><div class="wrap visit">
<div class="vimg rv"><img src="{img(1)}" alt="" loading="lazy"></div>
<div class="vbox rv"><h2>Come and see us</h2>
<p>📍 <span><b>Where</b><br>{esc(area)}</span></p>
{phone_line}{social_line}
<div class="btns"><a class="btn p" href="{esc(contact_href)}" target="_blank" rel="noopener">{esc(contact_label)}</a></div>
</div></div></section>
</main>
<footer><div class="wrap foot"><span>© 2026 {esc(name)}. All rights reserved.</span><span>Website preview by <a href="https://vixautomations.pages.dev" target="_blank" rel="noopener"><b>Vix Assist</b></a></span></div></footer>

<div class="drawer" id="drawer"><div class="shade" data-x></div><div class="panel">
<h3>Your bag <button data-x aria-label="Close">×</button></h3>
<div class="lines" id="lines"></div>
<div class="tot"><span>Total</span><span id="tot">£0</span></div>
<button class="btn p" id="checkout">Secure checkout</button>
<p class="note">Preview only. No payment is taken. On the live site this opens a secure card / Apple Pay checkout.</p>
</div></div>
<div class="toast" id="toast"></div>
<script>
const D={data};
const g=document.getElementById('grid'),bag=[];const gbp=n=>'£'+n.toLocaleString('en-GB');
function render(c){{g.innerHTML=D.products.filter(p=>c==='All'||p.cat===c).map((p,i)=>`<article class="card rv in"><div class="ph"><img src="${{p.img}}" alt="${{p.name}}" loading="lazy">${{p.tag?`<span class="tag">${{p.tag}}</span>`:''}}</div><div class="ci"><small>${{p.cat}}</small><b>${{p.name}}</b><div class="row"><span class="price">${{gbp(p.price)}}</span><button class="add" data-n="${{p.name}}">Add</button></div></div></article>`).join('')}}
render('All');
document.querySelectorAll('.chip').forEach(b=>b.onclick=()=>{{document.querySelectorAll('.chip').forEach(x=>x.classList.remove('on'));b.classList.add('on');render(b.dataset.c)}});
const toast=t=>{{const e=document.getElementById('toast');e.textContent=t;e.classList.add('show');clearTimeout(e._t);e._t=setTimeout(()=>e.classList.remove('show'),1800)}};
function draw(){{document.getElementById('count').textContent=bag.length;document.getElementById('lines').innerHTML=bag.length?bag.map(p=>`<div class="line"><img src="${{p.img}}" alt=""><span>${{p.name}}</span><b>${{gbp(p.price)}}</b></div>`).join(''):'<p class="note">Your bag is empty.</p>';document.getElementById('tot').textContent=gbp(bag.reduce((s,p)=>s+p.price,0))}}
g.addEventListener('click',e=>{{const b=e.target.closest('.add');if(!b)return;bag.push(D.products.find(p=>p.name===b.dataset.n));draw();toast('Added to bag ✓')}});
const dr=document.getElementById('drawer');document.getElementById('bagBtn').onclick=()=>{{draw();dr.classList.add('open')}};
dr.addEventListener('click',e=>{{if(e.target.hasAttribute('data-x'))dr.classList.remove('open')}});
document.getElementById('checkout').onclick=()=>toast(bag.length?'Preview: secure checkout connects at launch':'Add something first');
document.getElementById('f').onsubmit=e=>{{e.preventDefault();document.getElementById('ok').style.display='block'}};
const io=new IntersectionObserver(es=>es.forEach(x=>{{if(x.isIntersecting){{x.target.classList.add('in');io.unobserve(x.target)}}}}),{{threshold:.12}});
document.querySelectorAll('.rv:not(.in)').forEach(el=>io.observe(el));
setTimeout(()=>document.querySelectorAll('.rv').forEach(el=>el.classList.add('in')),2500);
draw();
</script>
</body></html>
"""


for s in STORES:
    out = ROOT / "p" / s[0] / "index.html"
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(build(*s))
    print(f"{BASE}/p/{s[0]}/  {s[1]}")
