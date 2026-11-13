(function () {
  "use strict";

  /* ===== Settings ===== */
  var EMAIL = "support@vixassist.com";
  var BRIEF_ENDPOINT = "https://vixassist.com/api/brief"; // saves the brief and emails it to the inbox
  var WA_UK = "447723149573";                                 // can carry the brief text
  var WA_NG = "https://wa.me/message/WV3WLO4FC656K";          // Nigeria line, no prefilled text

  var reduce = window.matchMedia("(prefers-reduced-motion: reduce)").matches;
  var $ = function (s, el) { return (el || document).querySelector(s); };
  var $$ = function (s, el) { return Array.prototype.slice.call((el || document).querySelectorAll(s)); };

  function inNigeria() {
    try { if (Intl.DateTimeFormat().resolvedOptions().timeZone === "Africa/Lagos") return true; } catch (e) {}
    return (navigator.languages || [navigator.language || ""]).some(function (l) { return /-NG$/i.test(l); });
  }
  function waText(text) { return "https://wa.me/" + WA_UK + "?text=" + encodeURIComponent(text); }
  var waPlain = inNigeria() ? WA_NG : waText("Hello Vix Assist, I visited your website and I'd like to discuss a website project.");
  $$("[data-wa-plain]").forEach(function (a) { a.href = waPlain; });
  $("#yr").textContent = new Date().getFullYear();

  /* ===== Designs ===== */
  var DESIGNS = [
    { id: 1, name: "Midnight Luxe", tags: ["auto"], desc: "Dark, cinematic and premium, with full-screen photography.", best: "Luxury car dealers, car rentals, jewellers" },
    { id: 2, name: "Clean Estate", tags: ["estate"], desc: "Bright and airy, with a large property search up front.", best: "Real estate agencies, brokers, shortlets" },
    { id: 3, name: "Bold Editorial", tags: ["food", "creative"], desc: "Huge headlines and a confident magazine feel.", best: "Restaurants, fashion brands, events" },
    { id: 4, name: "Glass Tech", tags: ["business"], desc: "Dark tech look with glowing glass panels.", best: "Startups, fintech, software, apps" },
    { id: 5, name: "Warm Organic", tags: ["food"], desc: "Soft warm tones, elegant type and arched imagery.", best: "Restaurants, cafés, bakeries, wellness" },
    { id: 6, name: "Corporate Trust", tags: ["business"], desc: "Structured, calm and confident in deep blue.", best: "Law, finance, consulting, logistics" },
    { id: 7, name: "Neo Brutal", tags: ["creative"], desc: "Loud colour, thick outlines and bold type.", best: "Agencies, streetwear, creators" },
    { id: 8, name: "Fresh Clinic", tags: ["business"], desc: "Calm mint, rounded shapes and a friendly feel.", best: "Clinics, dentists, pharmacies, salons" },
    { id: 9, name: "Photo Showcase", tags: ["creative", "estate", "auto"], desc: "Full-screen photography with minimal text.", best: "Photographers, hotels, venues, car showrooms" },
    { id: 10, name: "Playful Colour", tags: ["business", "creative"], desc: "Bright colour blocks and a cheerful layout.", best: "Schools, kids brands, churches, retail" }
  ];
  var gallery = $("#gallery");
  gallery.innerHTML = DESIGNS.map(function (d) {
    return '<article class="design rv' + (d.id < 3 ? ' feat' : '') + '" data-tags="' + d.tags.join(" ") + '">' +
      '<button class="thumb" type="button" data-preview="' + d.id + '" aria-label="Preview the ' + d.name + ' design"><img src="assets/designs/d' + d.id + (d.id < 3 ? '' : '-sm') + '.jpg" alt="' + d.name + ' website design preview" loading="lazy" width="600" height="400"><span class="num">Design ' + d.id + '</span></button>' +
      '<div class="body"><h3>' + d.name + '</h3><p>' + d.desc + '</p><p class="best">Best for: ' + d.best + '</p>' +
      '<div class="actions"><button class="icon-btn" type="button" data-preview="' + d.id + '" aria-label="Preview the ' + d.name + ' design"><i class="ph ph-eye" aria-hidden="true"></i></button>' +
      '<a class="btn btn-primary btn-sm grow" href="#brief" data-design="' + d.id + '">Choose this design</a></div></div></article>';
  }).join("");

  $$("[data-filter]").forEach(function (b) {
    b.addEventListener("click", function () {
      $$("[data-filter]").forEach(function (x) { x.setAttribute("aria-pressed", String(x === b)); });
      var f = b.dataset.filter;
      $$(".design").forEach(function (c) { c.hidden = f !== "all" && c.dataset.tags.split(" ").indexOf(f) < 0; });
    });
  });

  var dlg = document.createElement("dialog");
  dlg.setAttribute("aria-label", "Design preview");
  document.body.appendChild(dlg);
  gallery.addEventListener("click", function (e) {
    var p = e.target.closest("[data-preview]");
    if (!p) return;
    var d = DESIGNS[+p.dataset.preview - 1];
    dlg.innerHTML = '<div class="dlg-bar"><h3>Design ' + d.id + ': ' + d.name + '</h3><div class="cta-row" style="margin:0"><a class="btn btn-primary btn-sm" href="#brief" data-design="' + d.id + '">Choose this design</a><button class="btn btn-line btn-sm" type="button" data-close>Close</button></div></div>' +
      '<img src="assets/designs/d' + d.id + '.jpg" alt="' + d.name + ' full design preview" width="1200" height="800">';
    dlg.showModal();
  });
  dlg.addEventListener("click", function (e) { if (e.target === dlg || e.target.closest("[data-close]") || e.target.closest("[data-design]")) dlg.close(); });

  /* ===== Brief builder ===== */
  var OPTIONS = {
    industry: ["Car dealer", "Car rental", "Real estate", "Restaurant or café", "Clinic or health", "Salon or beauty", "School", "Church", "Logistics", "Online store", "Professional services", "Other"],
    project: ["New website", "Redesign my current website", "Fix my current website"],
    goals: ["Get more enquiries", "Take bookings online", "Show my stock or listings", "Sell products online", "Look more professional", "Rank on Google", "Build trust with new customers"],
    pages: ["Home", "About", "Services", "Stock or listings", "Gallery", "Pricing", "Testimonials", "Blog", "FAQ", "Contact"],
    features: ["WhatsApp chat button", "Booking or appointment form", "Online payments", "Interactive 3D showcase", "Search and filters", "Live chat", "Google Maps location", "Currency switcher", "Newsletter sign up", "Blog you can update"],
    style: ["Luxury", "Minimal", "Bold", "Warm", "Corporate", "Playful", "Modern tech"],
    budget: ["Under $500", "$500 to $1,000", "$1,000 to $2,500", "$2,500 and above", "Not sure yet"],
    timeline: ["As soon as possible", "Within 2 to 4 weeks", "Within 1 to 2 months", "Flexible"],
    content: ["Logo", "Photos", "Text for the pages", "Domain name", "Hosting", "None yet"]
  };
  var state = { industry: [], project: [], goals: [], pages: ["Home", "Contact"], features: ["WhatsApp chat button"], style: [], budget: [], timeline: [], content: [], design: null };

  $$(".chips").forEach(function (box) {
    var g = box.dataset.group, single = box.hasAttribute("data-single");
    box.setAttribute("role", "group");
    box.innerHTML = OPTIONS[g].map(function (o) {
      return '<button type="button" class="chip" aria-pressed="' + (state[g].indexOf(o) > -1) + '">' + o + "</button>";
    }).join("");
    box.addEventListener("click", function (e) {
      var c = e.target.closest(".chip"); if (!c) return;
      var v = c.textContent;
      if (single) { state[g] = [v]; $$(".chip", box).forEach(function (x) { x.setAttribute("aria-pressed", String(x === c)); }); }
      else {
        var i = state[g].indexOf(v);
        if (i > -1) state[g].splice(i, 1); else state[g].push(v);
        c.setAttribute("aria-pressed", String(i < 0));
      }
      box.classList.remove("invalid");
      render();
    });
  });

  var pick = $("#design-pick");
  pick.innerHTML = DESIGNS.map(function (d) {
    return '<button type="button" class="pick" data-pick="' + d.id + '" aria-pressed="false"><img src="assets/designs/d' + d.id + '-sm.jpg" alt="" loading="lazy" width="600" height="400"><span>' + d.id + ". " + d.name + "</span></button>";
  }).join("") + '<button type="button" class="pick custom" data-pick="custom" aria-pressed="false"><i class="ph ph-pencil-simple-line" aria-hidden="true"></i><span>Something else</span></button>';
  function setDesign(v) {
    state.design = v;
    $$(".pick").forEach(function (p) { p.setAttribute("aria-pressed", String(p.dataset.pick === String(v))); });
    render();
  }
  pick.addEventListener("click", function (e) { var p = e.target.closest(".pick"); if (p) setDesign(p.dataset.pick === "custom" ? "custom" : +p.dataset.pick); });
  document.addEventListener("click", function (e) {
    var a = e.target.closest("[data-design]"); if (!a) return;
    var v = a.dataset.design === "custom" ? "custom" : +a.dataset.design;
    setDesign(v);
    if (v === "custom") setTimeout(function () { var n = $("#f-notes"); n.placeholder = "Describe the website you want: the look, feel, colours and anything you've seen that you like."; }, 0);
  });

  // Turn rough notes into clear, professional sentences.
  var SHORT = { "pls": "please", "plz": "please", "u": "you", "ur": "your", "r": "are", "wanna": "want to", "gonna": "going to", "abt": "about", "asap": "as soon as possible", "msg": "message", "dm": "message", "info": "information", "thru": "through", "bcos": "because", "cos": "because", "coz": "because", "tho": "though", "wat": "what", "dey": "they", "wit": "with", "d": "the", "nd": "and", "n": "and", "im": "I am", "i'm": "I am", "dont": "do not", "cant": "cannot", "wont": "will not", "biz": "business", "pics": "photos", "pic": "photo", "whatsap": "WhatsApp", "whatsapp": "WhatsApp", "watsapp": "WhatsApp", "ig": "Instagram", "fb": "Facebook" };
  function polish(text) {
    var t = (text || "").replace(/\s+/g, " ").trim();
    if (!t) return "";
    t = t.replace(/[!?.]{2,}/g, ".").replace(/\s+([,.!?])/g, "$1");
    t = t.replace(/\b[\w']+\b/g, function (w) { var k = w.toLowerCase(); return SHORT.hasOwnProperty(k) ? SHORT[k] : w; });
    t = t.replace(/\bi\b/g, "I").replace(/\b(also|and|but|so)\s+(also|and)\b/gi, "$1");
    var parts = t.replace(/([.!?])\s+/g, "$1|").split(/\||\s+(?:and also|also)\s+/i).map(function (s) {
      s = s.trim().replace(/[,;]$/, ""); if (!s) return "";
      s = s.charAt(0).toUpperCase() + s.slice(1);
      s = s.replace(/^I want\b/, "We would like").replace(/^I need\b/, "We need").replace(/^I would like\b/, "We would like").replace(/\bmy\b/g, "our").replace(/\bme\b/g, "us").replace(/^I\b/, "We");
      return /[.!?]$/.test(s) ? s : s + ".";
    }).filter(Boolean);
    return parts.join(" ");
  }
  $("#polish").addEventListener("click", function () {
    var n = $("#f-notes"), before = n.value.trim(), m = $("#polish-msg");
    if (!before) { m.textContent = "Write a few words first, in any style. We'll tidy them up."; return; }
    var after = polish(before);
    n.value = after; m.textContent = after === before ? "Your notes already read well." : "Done. Edit anything you like before sending.";
    render();
  });

  function val(id) { return ($("#" + id).value || "").trim(); }
  function list(a, fallback) { return a.length ? a.join(", ") : (fallback || "Not specified"); }
  function bullets(a) { return a.length ? a.map(function (x) { return "• " + x; }).join("\n") : "• To be discussed"; }
  function buildBrief() {
    var d = state.design, design;
    if (d === "custom") design = "Custom design (described in the notes below)";
    else if (d) design = "Design " + d + ": " + DESIGNS[d - 1].name + " (" + DESIGNS[d - 1].desc.replace(/\.$/, "") + ")";
    else design = "Not chosen yet";
    var biz = val("f-business") || "Your business", ind = list(state.industry, "business").toLowerCase(), loc = val("f-location");
    var notes = val("f-notes");
    var date = new Date().toLocaleDateString("en-GB", { day: "numeric", month: "long", year: "numeric" });
    return [
      "PROJECT BRIEF: " + biz.toUpperCase(),
      "Prepared " + date + " via vixautomationsportfolio.pages.dev",
      "",
      "1. BUSINESS OVERVIEW",
      biz + " is a " + ind + (loc ? " based in " + loc : "") + "." + (val("f-current") ? " Current website: " + val("f-current") + "." : ""),
      "",
      "2. PROJECT TYPE",
      list(state.project, "To be confirmed"),
      "",
      "3. GOALS",
      bullets(state.goals),
      "",
      "4. PAGES",
      list(state.pages),
      "",
      "5. FEATURES",
      bullets(state.features),
      "",
      "6. DESIGN DIRECTION",
      "Chosen design: " + design,
      "Style: " + list(state.style),
      "Colours: " + (val("f-colours") || "Open to suggestions"),
      "Reference websites: " + (val("f-refs") || "None given"),
      "",
      "7. BUDGET AND TIMELINE",
      "Budget: " + list(state.budget),
      "Timeline: " + list(state.timeline),
      "Content ready: " + list(state.content),
      "",
      "8. CONTACT",
      "Name: " + (val("f-name") || "-"),
      "Email: " + (val("f-email") || "-"),
      "WhatsApp: " + (val("f-phone") || "-"),
      "",
      "9. ADDITIONAL NOTES",
      notes || "None"
    ].join("\n");
  }
  var pre = $("#brief-text");
  function render() { pre.textContent = buildBrief(); }
  $("#brief-form").addEventListener("input", function (e) { e.target.classList.remove("invalid"); render(); });

  // Step navigation
  var step = 1, TOTAL = 6;
  var form = $("#brief-form"), msg = $("#form-msg");
  function show(n) {
    step = n;
    $$(".step", form).forEach(function (f) { f.hidden = +f.dataset.step !== n; });
    $("#progress-bar").style.width = (n / TOTAL * 100) + "%";
    $("#step-count").textContent = "Step " + n + " of " + TOTAL;
    $("#back").hidden = n === 1; $("#next").hidden = n === TOTAL; $("#send").hidden = n !== TOTAL;
    msg.textContent = ""; msg.className = "msg";
  }
  function check(n) {
    var bad = [];
    $$(".step[data-step='" + n + "'] [required]", form).forEach(function (el) {
      var ok = el.value.trim() !== "";
      if (el.type === "email") ok = /^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(el.value.trim());
      if (el.name === "phone") ok = /^\+?[\d\s()-]{10,18}$/.test(el.value.trim());
      el.classList.toggle("invalid", !ok); if (!ok) bad.push(el);
    });
    if (n === 1 && !state.industry.length) { $(".chips[data-group='industry']").classList.add("invalid"); bad.push(null); }
    if (n === 2 && !state.project.length) { $(".chips[data-group='project']").classList.add("invalid"); bad.push(null); }
    if (bad.length) {
      msg.className = "msg err";
      msg.textContent = n === 6 ? "Please add a valid email and a WhatsApp number with at least 10 digits." : "Please fill in the highlighted fields to continue.";
      if (bad[0]) bad[0].focus();
      return false;
    }
    return true;
  }
  $("#next").addEventListener("click", function () { if (check(step)) { show(step + 1); form.scrollIntoView({ behavior: reduce ? "auto" : "smooth", block: "start" }); } });
  $("#back").addEventListener("click", function () { show(step - 1); });
  $("#copy").addEventListener("click", function () {
    navigator.clipboard && navigator.clipboard.writeText(pre.textContent).then(function () { $("#copy").setAttribute("aria-label", "Copied"); $("#copy").innerHTML = '<i class="ph ph-check" aria-hidden="true"></i>'; });
  });

  form.addEventListener("submit", function (e) {
    e.preventDefault();
    if (!check(6)) return;
    var brief = buildBrief(), biz = val("f-business");
    var mailUrl = "mailto:" + EMAIL + "?subject=" + encodeURIComponent("Website project brief: " + biz) + "&body=" + encodeURIComponent(brief);
    var send = $("#send"), label = send.innerHTML; send.disabled = true; send.textContent = "Sending…";
    var ctrl = window.AbortController ? new AbortController() : null;
    var timer = setTimeout(function () { if (ctrl) ctrl.abort(); }, 20000);
    fetch(BRIEF_ENDPOINT, {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ source: "Portfolio brief builder", subject: "New website brief: " + biz, name: val("f-name"), email: val("f-email"), whatsapp: val("f-phone"), business: biz, text: brief }),
      signal: ctrl ? ctrl.signal : undefined
    }).then(function (r) { return r.json().then(function (j) { if (!r.ok) throw new Error(j.error || "failed"); return j; }); })
      .then(function () {
        $("#done-title").textContent = "Your brief has been sent";
        $("#done-text").textContent = "Thank you! Your project brief is in our inbox. We'll review it and email you a fixed quote within one business day.";
        $("#done-mail").hidden = true;
      })
      .catch(function () {
        $("#done-title").textContent = "One more step";
        $("#done-text").textContent = "We couldn't send your brief automatically just now. Please tap the button below to send it by email, it's already written for you.";
        $("#done-mail").href = mailUrl; $("#done-mail").hidden = false;
      })
      .finally(function () {
        clearTimeout(timer); send.disabled = false; send.innerHTML = label;
        $(".builder").hidden = true; $("#done").hidden = false;
        $("#done").scrollIntoView({ behavior: reduce ? "auto" : "smooth", block: "center" });
      });
  });
  show(1); render();

  /* ===== Navigation ===== */
  var burger = $(".burger"), panel = $("#panel");
  function menu(open) {
    document.body.classList.toggle("menu-open", open);
    burger.setAttribute("aria-expanded", String(open)); burger.setAttribute("aria-label", open ? "Close menu" : "Open menu");
    panel.setAttribute("aria-hidden", String(!open));
    $$("a", panel).forEach(function (a, i) { a.style.transitionDelay = open ? Math.min(i * 60, 400) + "ms" : "0ms"; });
  }
  burger.addEventListener("click", function () { menu(burger.getAttribute("aria-expanded") !== "true"); });
  panel.addEventListener("click", function (e) { if (e.target.closest("a")) menu(false); });
  document.addEventListener("keydown", function (e) { if (e.key === "Escape") menu(false); });

  /* ===== Reveals ===== */
  var tag = $("#tagline");
  tag.innerHTML = tag.textContent.trim().split(/\s+/).map(function (w) { return '<span class="w">' + w + "</span>"; }).join(" ");
  if (!("IntersectionObserver" in window) || reduce) {
    $$(".rv").forEach(function (el) { el.classList.add("in"); }); $$(".w", tag).forEach(function (w) { w.classList.add("on"); });
  } else {
    var io = new IntersectionObserver(function (es) { es.forEach(function (x) { if (x.isIntersecting) { x.target.classList.add("in"); io.unobserve(x.target); } }); }, { threshold: 0.12 });
    $$(".rv").forEach(function (el) { io.observe(el); });
    var wo = new IntersectionObserver(function (es) { es.forEach(function (x) { if (x.isIntersecting) { x.target.classList.add("on"); wo.unobserve(x.target); } }); }, { rootMargin: "0px 0px -40% 0px" });
    $$(".w", tag).forEach(function (w) { wo.observe(w); });
    var links = $$(".nav-links a");
    var so = new IntersectionObserver(function (es) { es.forEach(function (x) { if (x.isIntersecting) links.forEach(function (a) { a.setAttribute("aria-current", String(a.getAttribute("href") === "#" + x.target.id)); }); }); }, { rootMargin: "-45% 0px -50% 0px" });
    ["top", "designs", "work", "process", "brief", "faq"].forEach(function (id) { var el = document.getElementById(id); if (el) so.observe(el); });
  }
})();
