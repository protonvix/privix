"""Builds the About and policy pages from one shared layout.

Run from the repo root:  python3 tools/make-pages.py
Edit the page text below, run the script, then commit and push.
"""
import pathlib

ROOT = pathlib.Path(__file__).resolve().parent.parent
UPDATED = "4 November 2026"
EMAIL = "vixautomations@gmail.com"

PAGES = {}

PAGES["about"] = dict(
    title="About us",
    desc="Vix Studio is the web design studio of Vix Assist, founded by Promise Felix, working with businesses in Lagos and London.",
    eyebrow="About Vix Studio",
    h1="We build websites that make businesses look as good as they are",
    intro="Vix Studio is the web design studio of Vix Assist, founded by Promise Felix. We work with businesses in Nigeria and the UK, especially car dealers, car rental companies, real estate agents, restaurants and service businesses.",
    body=f"""
<h2>Why we started</h2>
<p>Many good businesses lose customers online without knowing it. Their website is outdated, slow on phones, broken, or missing altogether, so buyers who search for them find nothing they can trust. We started Vix Studio to fix that: modern, fast websites that win trust at first glance and turn visitors into enquiries.</p>

<h2>What we do</h2>
<ul>
<li><b>New websites</b> designed from scratch for your business and your customers.</li>
<li><b>Redesigns</b> of outdated, slow or broken websites, including recovering sites whose domain has expired.</li>
<li><b>Interactive features</b> like 3D showcases, car and property listings, booking forms and WhatsApp enquiries.</li>
<li><b>Business automation</b> with GoHighLevel: lead capture, follow-ups, reminders and pipelines, through Vix Assist.</li>
<li><b>TikTok and social media marketing</b> to bring more people to your new website.</li>
</ul>

<h2>How we work</h2>
<ul>
<li><b>Fixed quote first.</b> You know the full price before any work starts.</li>
<li><b>You approve the design.</b> We don't build until you're happy with how it looks.</li>
<li><b>You own everything.</b> Your domain, website files and content belong to you, with no lock-in.</li>
<li><b>Clear communication.</b> One point of contact, on WhatsApp or email, from first message to launch.</li>
</ul>

<h2>Where we are</h2>
<p>We work remotely with clients from Lagos, Nigeria and London, United Kingdom. Meetings happen on WhatsApp, phone or video call at a time that suits you.</p>

<h2>Talk to us</h2>
<p>Email <a href="mailto:{EMAIL}">{EMAIL}</a>, message us on WhatsApp (<a href="https://wa.me/message/WV3WLO4FC656K">Nigeria</a> or <a href="https://wa.me/447723149573">UK +44 7723 149573</a>), or <a href="./#brief">send us your project brief</a>.</p>
""",
)

PAGES["privacy"] = dict(
    title="Privacy policy",
    desc="How Vix Studio collects, uses and protects your personal information.",
    eyebrow="Policies",
    h1="Privacy policy",
    intro="This policy explains what personal information Vix Studio (Vix Assist) collects, why we collect it, and the choices you have. We keep it simple: we only collect what we need to reply to you and deliver your project.",
    body=f"""
<h2>What we collect</h2>
<ul>
<li><b>Project briefs:</b> your name, business name, email address, WhatsApp or phone number, and the answers you give about your project.</li>
<li><b>Messages:</b> anything you send us by WhatsApp, email or phone.</li>
<li><b>Project materials:</b> logos, photos, text and logins you share so we can build your website.</li>
<li><b>Payment records:</b> invoices and payment confirmations. We never see or store your card details.</li>
</ul>

<h2>How we use it</h2>
<ul>
<li>To reply to your enquiry and prepare your quote.</li>
<li>To design, build, launch and support your website.</li>
<li>To send invoices and keep financial records required by law.</li>
</ul>
<p>We don't sell or rent your information, and we don't add you to marketing lists without your permission.</p>

<h2>Services we use</h2>
<p>Briefs and messages sent through our website forms are stored securely in our client portal (hosted on Cloudflare) and emailed to our inbox through Resend, an email delivery service. We also use Gmail, WhatsApp, Cloudflare (website hosting) and payment providers such as Payoneer, Cleva and Wise. Each of these processes data under its own privacy policy.</p>

<h2>Cookies</h2>
<p>This website doesn't use advertising or tracking cookies. Our hosting provider may keep basic technical logs, such as IP addresses, to keep the site secure and working.</p>

<h2>How long we keep it</h2>
<p>We keep enquiries for up to 12 months if no project goes ahead. For clients, we keep project and payment records for as long as the law requires, usually up to 6 years. Logins you share with us are deleted once your project is handed over.</p>

<h2>Your rights</h2>
<p>You can ask us to show, correct or delete the personal information we hold about you, or to stop contacting you. Email <a href="mailto:{EMAIL}">{EMAIL}</a> and we'll respond within 7 days. We follow the Nigeria Data Protection Act 2023 and UK data protection law (UK GDPR).</p>

<h2>Security</h2>
<p>We keep your information in secure, password-protected accounts and only use it for your project. If you share logins with us, we recommend changing the passwords after handover.</p>

<h2>Website previews</h2>
<p>We sometimes design a free preview of a new website for a business we'd like to work with. Previews use only public business information, such as the business name and contact number, are clearly labelled as previews and are hidden from search engines. To have a preview removed, message us and we'll take it down within 2 business days.</p>

<h2>Credits</h2>
<p>3D car model: Ferrari 458 Italia by vicent091036 on Sketchfab, used under its Creative Commons attribution licence via the three.js examples.</p>
""",
)

PAGES["payment"] = dict(
    title="Payment policy",
    desc="How quotes, deposits, invoices and payments work at Vix Studio.",
    eyebrow="Policies",
    h1="Payment policy",
    intro="We keep payments simple and transparent. You get a fixed quote before any work starts, and you never pay for anything you didn't agree to.",
    body=f"""
<h2>Quotes</h2>
<p>After you send your brief, we send a written fixed quote that lists exactly what's included: pages, features, revisions and timeline. Quotes are valid for 30 days. Work that isn't in the quote is only added after you approve a separate price.</p>

<h2>Free previews and consultations</h2>
<p>Consultations and website previews are free, with no obligation to buy.</p>

<h2>Payment schedule</h2>
<ul>
<li><b>50% deposit</b> to book your project and start the design.</li>
<li><b>50% balance</b> once you've approved the finished website, before it goes live on your domain.</li>
</ul>
<p>For larger projects we can agree payments in stages (milestones), written into your quote. Monthly services, such as maintenance or marketing, are paid at the start of each month.</p>

<h2>How to pay</h2>
<p>We accept bank transfer to accounts in Nigeria, the UK and the USA, and payment through Payoneer, Cleva and Wise. The payment details are on your invoice. Nigerian clients are invoiced in naira (₦); other clients in pounds (£) or US dollars ($). Please confirm payment details with us directly before sending money, and never pay into an account that isn't on your official invoice.</p>

<h2>Invoices</h2>
<p>Invoices are due within 7 days. If a payment is late, we pause work until it arrives, and the delivery date moves by the same amount of time.</p>

<h2>Third-party costs</h2>
<p>Your domain name, hosting, premium plugins, stock photos and other third-party services are listed separately in your quote. They're registered in your name wherever possible, so you own them. Most renew every year, and we remind you before renewal.</p>

<h2>Ownership</h2>
<p>Once the final payment is made, the website, its design and its files belong to you.</p>

<h2>Questions</h2>
<p>Email <a href="mailto:{EMAIL}">{EMAIL}</a> or message us on WhatsApp.</p>
""",
)

PAGES["delivery"] = dict(
    title="Delivery policy",
    desc="How and when Vix Studio delivers your website, from design to launch and handover.",
    eyebrow="Policies",
    h1="Delivery policy",
    intro="Our work is delivered digitally. Nothing is shipped. This page explains each step from your deposit to your website going live, and what happens after.",
    body=f"""
<h2>Timelines</h2>
<ul>
<li><b>Design:</b> your homepage design within 5 to 7 business days of receiving your deposit and content.</li>
<li><b>Business website:</b> usually 2 to 4 weeks from approved design to launch.</li>
<li><b>Larger websites</b> with bookings, payments, listings or 3D: we agree a date in your quote.</li>
</ul>
<p>Your exact delivery date is written in your quote.</p>

<h2>What we need from you</h2>
<p>Your logo, photos, text, prices and any logins we need (such as your domain account). Timelines start once we have these. If content arrives late, the delivery date moves by the same amount of time. If you don't have content ready, we can write text and source photos for you as an extra.</p>

<h2>Revisions</h2>
<p>Your quote includes 2 rounds of design changes before we build, and 1 round of changes on the finished website before launch. Further changes are welcome and are quoted separately.</p>

<h2>How you'll see your website</h2>
<p>We share a private preview link so you can check your website on your phone and computer before it goes live. Nothing is published on your domain until you approve it.</p>

<h2>Launch and handover</h2>
<p>After final payment, we publish your website on your domain, connect your email and WhatsApp buttons, and check everything works. You receive your logins, your website files on request, and a short video showing how to update your content.</p>

<h2>Support after launch</h2>
<p>For 14 days after launch, we fix any bugs or errors in our work for free. After that, we offer monthly maintenance, or we can help with one-off updates when you need them.</p>

<h2>Delays</h2>
<p>If we can't meet the agreed date, we'll tell you as early as possible and agree a new date with you. See our <a href="refund.html">refund policy</a> for what happens if we can't deliver.</p>
""",
)

PAGES["refund"] = dict(
    title="Refund policy",
    desc="When and how Vix Studio refunds payments for website projects.",
    eyebrow="Policies",
    h1="Refund policy",
    intro="We want you to be confident paying us. That's why you approve your design before we build, and why our refund terms are clear from the start.",
    body=f"""
<h2>Before work starts</h2>
<p>If you cancel before we start designing, we refund your deposit in full.</p>

<h2>After design work has started</h2>
<p>Design takes real time, so once we've started working on your design, the deposit is not refundable. If you cancel at this stage, you don't owe the remaining balance, and you can keep any designs already delivered to you.</p>

<h2>After you approve the finished website</h2>
<p>Once you've approved the finished website and paid the balance, payments are not refundable. If something isn't working as agreed, we'll fix it. Bug fixes are free for 14 days after launch.</p>

<h2>If we can't deliver</h2>
<p>If we can't deliver what's in your quote, and we haven't fixed it within 14 days of you telling us, we refund everything you've paid for the work that wasn't delivered. If the delay is caused by missing content, late payments or approvals on your side, this doesn't apply.</p>

<h2>Third-party costs</h2>
<p>Domain names, hosting, plugins and other services bought for you from other companies can't be refunded by us, but they stay in your name and remain yours to use.</p>

<h2>Monthly services</h2>
<p>You can cancel monthly services at any time, and they stop at the end of the month you've paid for. Months already paid are not refunded.</p>

<h2>How to ask for a refund</h2>
<p>Email <a href="mailto:{EMAIL}">{EMAIL}</a> with your name, your invoice number and the reason. We reply within 2 business days. Approved refunds are paid within 7 business days, to the same account or method you paid with.</p>
""",
)

ORDER = [("about", "About us"), ("privacy", "Privacy"), ("payment", "Payment"), ("delivery", "Delivery"), ("refund", "Refunds")]

SHELL = """<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title} · Vix Studio</title>
<meta name="description" content="{desc}">
<link rel="canonical" href="https://vixautomationsportfolio.pages.dev/{slug}.html">
<meta property="og:title" content="{title} · Vix Studio">
<meta property="og:description" content="{desc}">
<meta property="og:image" content="https://vixautomationsportfolio.pages.dev/assets/og.jpg">
<link rel="icon" href="assets/favicon.svg" type="image/svg+xml">
<link rel="apple-touch-icon" href="assets/apple-touch-icon.png">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Geist:wght@400;500;600;700&display=swap" rel="stylesheet">
<link rel="stylesheet" href="https://unpkg.com/@phosphor-icons/web@2.1.1/src/regular/style.css">
<link rel="stylesheet" href="styles.css">
</head>
<body class="page">
<header class="page-top">
  <div class="wrap page-bar">
    <a class="brand" href="./"><img src="assets/logo.svg" alt="" width="28" height="28">Vix <span>Studio</span></a>
    <a class="btn btn-primary btn-sm" href="./#brief">Start your project</a>
  </div>
</header>
<main class="doc">
  <div class="wrap doc-wrap">
    <nav class="doc-tabs" aria-label="Pages">{tabs}</nav>
    <div class="eyebrow">{eyebrow}</div>
    <h1 class="doc-h1">{h1}</h1>
    <p class="doc-intro">{intro}</p>
    {updated}
    <div class="doc-body">{body}</div>
    <div class="doc-cta">
      <div><h2>Questions?</h2><p>We're happy to explain anything before you start.</p></div>
      <div class="cta-row"><a class="btn btn-primary" href="./#brief">Start your project</a><a class="btn btn-line" href="https://wa.me/message/WV3WLO4FC656K" target="_blank" rel="noopener"><i class="ph ph-whatsapp-logo" aria-hidden="true"></i>WhatsApp us</a></div>
    </div>
  </div>
</main>
<footer class="site">
  <div class="wrap legal"><span>© 2026 Vix Assist</span>{links}</div>
</footer>
</body>
</html>
"""

for slug, page in PAGES.items():
    current = ' aria-current="page"'
    tabs = "".join(f'<a href="{s}.html"{current if s == slug else ""}>{label}</a>' for s, label in ORDER)
    links = "".join(f'<a href="{s}.html">{label}</a>' for s, label in ORDER)
    updated = "" if slug == "about" else f'<p class="doc-date">Last updated {UPDATED}</p>'
    html = SHELL.format(slug=slug, tabs=tabs, links=links, updated=updated, **page)
    (ROOT / f"{slug}.html").write_text(html)
    print(f"{slug}.html")
