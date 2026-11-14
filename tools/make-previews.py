"""Builds a personalised website preview for each prospect: p/<slug>/index.html.

Run from the repo root:  python3 tools/make-previews.py
Add a company to COMPANIES below, run the script, then commit and push.
"""
import json
import pathlib

ROOT = pathlib.Path(__file__).resolve().parent.parent
TEMPLATE = (ROOT / "tools" / "preview-template.html").read_text()

# slug, name, kind (dealer | rental | hire), WhatsApp number in international format, accent colour
COMPANIES = [
    ("acokocha", "A.C. Okocha Motors", "dealer", "2348036839121", "#E8B04B"),
    ("corporatecab", "Corporate Cab Services", "hire", "2348033279358", "#4F9DFF"),
    ("dreamafrica", "Dream Africa Motors", "dealer", "2347057382925", "#F2994A"),
    ("moscarrental", "Mos Car Rental", "rental", "2349061439923", "#22D3A6"),
    ("sommet", "Sommet Motors", "dealer", "2349090000438", "#C9A86A"),
    ("vehiclespot", "Vehiclespot", "dealer", "2348033971669", "#FF6B4A"),
    ("viperautos", "Viperautos", "dealer", "2347055343818", "#E5484D"),
    ("lamborghini", "Lamborghini Executive Car Hire", "hire", "2348095478699", "#F5C542"),
    ("mobilityng", "MobilityNG", "rental", "2348035880220", "#3DD68C"),
    ("plushdrives", "PlushDrives Rentals", "rental", "2349013281578", "#A78BFA"),
    ("patjeda", "Patjeda Executive Car Hire", "hire", "2348063318118", "#D4AF37"),
    ("rentacar", "Rent A Car Nigeria", "rental", "2348092927960", "#38BDF8"),
    ("fleetpartners", "FleetPartners Leasing", "hire", "2348066597211", "#60A5FA"),
    ("everything4hire", "Everything4hire", "rental", "2347036161153", "#FB923C"),
    ("metropolitan", "Metropolitan Motors", "dealer", "2348054477589", "#93C5FD"),
    ("xclusive", "Xclusive Rent A Car", "rental", "2348026434549", "#F472B6"),
]

CHECK = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2"><path d="M20 6 9 17l-5-5"/></svg>'
ICONS = {
    "shield": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10Z"/><path d="m9 12 2 2 4-4"/></svg>',
    "eye": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M2 12s3.5-7 10-7 10 7 10 7-3.5 7-10 7S2 12 2 12Z"/><circle cx="12" cy="12" r="3"/></svg>',
    "truck": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M3 6h11v10H3zM14 9h4l3 3v4h-7"/><circle cx="7" cy="17" r="2"/><circle cx="17" cy="17" r="2"/></svg>',
    "chat": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M21 11.5a8.4 8.4 0 0 1-12.6 7.3L3 21l2.2-5.4A8.4 8.4 0 1 1 21 11.5Z"/></svg>',
    "clock": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="9"/><path d="M12 7v5l3 2"/></svg>',
    "user": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="8" r="4"/><path d="M4 21a8 8 0 0 1 16 0"/></svg>',
    "spark": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M12 3v4M12 17v4M3 12h4M17 12h4M6 6l2.5 2.5M15.5 15.5 18 18M6 18l2.5-2.5M15.5 8.5 18 6"/></svg>',
    "card": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="2" y="5" width="20" height="14" rx="2"/><path d="M2 10h20"/></svg>',
}

CARS = [  # image, name, type, specs, dealer price, daily rate, tag
    ("car5", "Audi A6 S line 2020", "Sedan", ["Automatic", "Petrol", "44,100 km"], 38_750_000, 120_000, ""),
    ("car4", "BMW M5 Competition 2022", "Sedan", ["Automatic", "Petrol", "9,300 km"], 142_000_000, 250_000, "Low mileage"),
    ("car8", "Ford Mustang GT 2019", "Sports", ["Automatic", "Petrol", "38,900 km"], 44_800_000, 180_000, "Price drop"),
    ("car3", "Chevrolet Camaro SS 2020", "Sports", ["Manual", "Petrol", "31,750 km"], 52_900_000, 170_000, ""),
    ("car6", "BMW M4 2021", "Sports", ["Automatic", "Petrol", "21,600 km"], 96_750_000, 220_000, ""),
    ("car1", "Chevrolet Camaro ZL1 2021", "Sports", ["Automatic", "Petrol", "18,200 km"], 68_500_000, 200_000, "Just arrived"),
]


def tick(text):
    return f"<div>{CHECK}<span>{text}</span></div>"


def trust(items):
    return "".join(f"<span>{CHECK}{t}</span>" for t in items)


def why(items):
    return "".join(f'<div class="tile rv"><div class="ic">{ICONS[i]}</div><h3>{h}</h3><p>{p}</p></div>' for i, h, p in items)


def field(label, inner):
    return f"<label>{label}{inner}</label>"


NAME_TEL = '<div class="two">' + field("Your name", '<input name="Name" required placeholder="Full name">') + field("Phone", '<input name="Phone" type="tel" required placeholder="080...">') + "</div>"

KINDS = {
    "dealer": dict(
        EYEBROW="Trusted car dealer in Lagos",
        H1="Quality cars. <span>Honest prices.</span>",
        LEAD="Browse our available cars with clear prices, inspect in person, and buy with confidence. Every enquiry comes straight to us on WhatsApp.",
        CTA1="View available cars", CTA2="Find me a car",
        TRUST=trust(["Verified cars", "Inspection welcome", "Nationwide delivery"]),
        CARS_LINK="Cars", BOOK_LINK="Find a car",
        CARS_H2="Available cars", CARS_SUB="Tap any car to ask about price, inspection or delivery on WhatsApp.",
        STOCK_WORD="stock", cardBtn="Enquire", unit="", ask="Is it still available?",
        BOOK_H2="Can't find the car you want?",
        BOOK_SUB="Tell us what you're looking for and your budget. We'll source it and send you options on WhatsApp.",
        TICKS=tick("Tokunbo and Nigerian-used options") + tick("Clean papers and documentation") + tick("Swap and payment plans available"),
        FORM=NAME_TEL
        + field("Car you want", '<input name="Car wanted" required placeholder="e.g. Toyota Camry 2018">')
        + '<div class="two">' + field("Budget", '<select name="Budget"><option>Under ₦10m</option><option>₦10m to ₦25m</option><option>₦25m to ₦50m</option><option>Above ₦50m</option></select>')
        + field("Swap my car?", '<select name="Swap"><option>No</option><option>Yes</option></select>') + "</div>",
        SUBMIT="Send request on WhatsApp",
        WHY=why([("shield", "Verified cars", "Every car is checked before it's listed, with clean documentation."),
                 ("eye", "Inspect first", "See the car in person and test drive it before you pay."),
                 ("truck", "Delivery", "We can deliver to you anywhere in Nigeria."),
                 ("chat", "Fast replies", "Message us on WhatsApp and get answers quickly.")]),
        CONTACT_H2="Ready to buy your next car?",
    ),
    "rental": dict(
        EYEBROW="Car rental in Lagos",
        H1="Rent a clean, reliable car <span>today.</span>",
        LEAD="Choose your car, pick your dates and book in minutes. Self-drive or with a driver, airport pickups and long-term rentals.",
        CTA1="See our cars", CTA2="Book now",
        TRUST=trust(["Clean, serviced cars", "Driver available", "Airport pickup"]),
        CARS_LINK="Our cars", BOOK_LINK="Book",
        CARS_H2="Choose your car", CARS_SUB="Daily rates shown. Tap a car to check availability on WhatsApp.",
        STOCK_WORD="fleet", cardBtn="Book", unit="/ day", ask="Is it available? I'd like to book.",
        BOOK_H2="Book your car in one minute",
        BOOK_SUB="Fill this in and your booking request goes straight to us on WhatsApp. We'll confirm availability quickly.",
        TICKS=tick("Self-drive or with a professional driver") + tick("Daily, weekly and monthly rates") + tick("Airport pickup and drop-off"),
        FORM=NAME_TEL
        + field("Car", '<select name="Car" id="car"><option>Any available car</option></select>')
        + '<div class="two">' + field("Pickup date", '<input name="Pickup date" type="date" required>')
        + field("Number of days", '<input name="Days" type="number" min="1" value="1">') + "</div>"
        + field("Driver", '<select name="Driver"><option>With driver</option><option>Self-drive</option></select>'),
        SUBMIT="Send booking on WhatsApp",
        WHY=why([("spark", "Clean cars", "Every car is cleaned and serviced before each rental."),
                 ("user", "Trained drivers", "Professional, courteous drivers who know Lagos."),
                 ("clock", "Always on time", "Pickups and drop-offs exactly when you need them."),
                 ("card", "Clear pricing", "Simple daily rates with no hidden charges.")]),
        CONTACT_H2="Need a car? We're ready.",
    ),
    "hire": dict(
        EYEBROW="Executive car hire in Lagos",
        H1="Executive car hire. <span>On time, every time.</span>",
        LEAD="Chauffeur-driven cars for executives, corporate clients, events and airport transfers across Lagos.",
        CTA1="View our fleet", CTA2="Book a car",
        TRUST=trust(["Professional chauffeurs", "Corporate accounts", "24/7 airport transfers"]),
        CARS_LINK="Fleet", BOOK_LINK="Book",
        CARS_H2="Our fleet", CARS_SUB="Rates per day with a chauffeur. Tap a car to book on WhatsApp.",
        STOCK_WORD="fleet", cardBtn="Book", unit="/ day", ask="I'd like to book it with a chauffeur.",
        BOOK_H2="Book a chauffeur-driven car",
        BOOK_SUB="Tell us when and where. Your request goes straight to us on WhatsApp and we'll confirm quickly.",
        TICKS=tick("Corporate accounts and monthly billing") + tick("Airport transfers, events and weddings") + tick("Vetted, uniformed chauffeurs"),
        FORM=NAME_TEL
        + field("Car", '<select name="Car" id="car"><option>Any available car</option></select>')
        + '<div class="two">' + field("Date", '<input name="Date" type="date" required>')
        + field("Service", '<select name="Service"><option>Airport transfer</option><option>Full day</option><option>Event or wedding</option><option>Corporate contract</option></select>') + "</div>"
        + field("Pickup location", '<input name="Pickup" placeholder="e.g. Victoria Island">'),
        SUBMIT="Send booking on WhatsApp",
        WHY=why([("user", "Professional chauffeurs", "Vetted, uniformed drivers who know every route in Lagos."),
                 ("clock", "Punctual", "We arrive before time, so you're never kept waiting."),
                 ("shield", "Safe and insured", "Well-maintained, fully insured cars."),
                 ("card", "Corporate billing", "Monthly accounts and invoices for companies.")]),
        CONTACT_H2="Book your next ride with us.",
    ),
}


def initials(name):
    words = [w for w in name.replace(".", " ").split() if w[0].isalpha()]
    return (words[0][0] + (words[1][0] if len(words) > 1 else "")).upper()


def local(num):
    n = "0" + num[3:]
    return f"{n[:4]} {n[4:7]} {n[7:]}"


for slug, name, kind, num, accent in COMPANIES:
    k = KINDS[kind]
    cars = [dict(img=i, name=n, type=t, specs=s, price=(p if kind == "dealer" else d), tag=tag) for i, n, t, s, p, d, tag in CARS]
    data = dict(name=name, wa=num, unit=k["unit"], cardBtn=k["cardBtn"], ask=k["ask"], cars=cars)
    html = TEMPLATE
    for key, val in k.items():
        html = html.replace("{{" + key + "}}", str(val))
    html = (html.replace("{{DATA}}", json.dumps(data, ensure_ascii=False))
                .replace("{{NAME}}", name).replace("{{INITIALS}}", initials(name))
                .replace("{{ACCENT}}", accent).replace("{{PHONE}}", local(num)).replace("{{TEL}}", "+" + num))
    assert "{{" not in html, slug
    out = ROOT / "p" / slug / "index.html"
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(html)
    print(f"https://design.vixassist.com/p/{slug}/  {name}")
