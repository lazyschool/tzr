/* =====================================================================
   Tavzuran — script.js
   Vanilla JS only. No dependencies. Works from file:// or GitHub Pages.
   ===================================================================== */

/* =====================================================================
   >>>>>>>>>>>>>>>>>  EDIT YOUR BUSINESS INFO HERE  <<<<<<<<<<<<<<<<<<<<
   This is the ONLY place you need to change contact details.
   Every button, link and label on the site reads from this object.
   ===================================================================== */
const CONFIG = {
  // Instagram handle (without the @)
  instagram: "tavzuran",

  // Your email address
  email: "adil@tavzuran.com",
  emailSubject: "Project enquiry from tavzuran.com",

  // "Book a Free Call" opens the visitor's email app with this message already
  // written, addressed to the `email` above. Edit the wording freely - every
  // line break is kept. Keep it short: long forms scare people off.
  callSubject: "Free call request - Tavzuran",
  callBody: [
    "Hi Adil,",
    "",
    "I'd like to book a free call about something I want to build.",
    "",
    "Name:",
    "Business / idea:",
    "What I want to build:",
    "Rough budget:",
    "Best day and time to call:",
    "Call me on (keep one): Phone / WhatsApp / Zoom / Google Meet",
    "Number or email for the invite:",
    "",
    "Thanks!"
  ].join("\r\n"),

  // Optional: a scheduling link (Cal.com, Calendly, Topmate...).
  // Leave "" to use the pre-written email above. If you ever set this, every
  // "Book a Free Call" button switches to the scheduler instead.
  bookingUrl: ""
};
/* =====================================================================
   >>>>>>>>>>>>>>>>>>>>>  END OF EDITABLE SECTION  <<<<<<<<<<<<<<<<<<<<<
   ===================================================================== */

(function () {
  "use strict";

  const $ = (sel, root) => (root || document).querySelector(sel);
  const $$ = (sel, root) => Array.prototype.slice.call((root || document).querySelectorAll(sel));
  const reduceMotion = window.matchMedia("(prefers-reduced-motion: reduce)").matches;

  /* ---------------------------------------------------------------
     1. Contact links — fill every [data-link] and [data-text]
  --------------------------------------------------------------- */
  const PLACEHOLDER_MAIL = "your-email@example.com";
  const hasEmail = CONFIG.email && CONFIG.email !== PLACEHOLDER_MAIL;

  const links = {
    instagram: "https://instagram.com/" + CONFIG.instagram,
    email: "mailto:" + CONFIG.email + "?subject=" + encodeURIComponent(CONFIG.emailSubject || "")
  };

  // "Book a Free Call" opens a ready-to-send email, unless a scheduling link
  // is configured, in which case that wins.
  links.call = CONFIG.bookingUrl || (
    "mailto:" + CONFIG.email +
    "?subject=" + encodeURIComponent(CONFIG.callSubject || "") +
    "&body=" + encodeURIComponent(CONFIG.callBody || "")
  );

  $$("[data-link]").forEach(function (el) {
    const key = el.getAttribute("data-link");
    if (!links[key]) return;
    el.href = links[key];
    if (/^https?:/.test(links[key])) {
      el.target = "_blank";
      el.rel = "noopener noreferrer";
    }
  });

  $$("[data-text]").forEach(function (el) {
    if (el.getAttribute("data-text") === "email") {
      el.textContent = hasEmail ? CONFIG.email : PLACEHOLDER_MAIL;
    }
  });

  /* ---------------------------------------------------------------
     2. Language — swaps the page text against the dictionaries in
        i18n.js. English is the source, so switching back to English
        just restores the original DOM text.
  --------------------------------------------------------------- */
  const I18N = window.TAVZ_I18N || null;
  const SUPPORTED = I18N ? I18N.languages.map(function (l) { return l.code; }) : ["en"];
  const ATTRS = ["aria-label", "alt", "title"];

  // Snapshot the English page once, so any language can be applied from it.
  const textNodes = [];
  const attrNodes = [];

  function snapshot() {
    const walker = document.createTreeWalker(document.body, NodeFilter.SHOW_TEXT);
    let n;
    while ((n = walker.nextNode())) {
      const p = n.parentElement;
      if (!p || p.closest("script,style,noscript")) continue;
      const raw = n.nodeValue;
      const key = raw.replace(/\s+/g, " ").trim();
      if (!key || !/[A-Za-z]/.test(key)) continue;
      const lead = raw.match(/^\s*/)[0];
      const tail = raw.match(/\s*$/)[0];
      textNodes.push({ node: n, key: key, lead: lead, tail: tail });
    }
    document.querySelectorAll("[aria-label],[alt],[title]").forEach(function (el) {
      ATTRS.forEach(function (a) {
        const v = el.getAttribute(a);
        if (v && /[A-Za-z]/.test(v)) attrNodes.push({ el: el, attr: a, key: v.trim() });
      });
    });
  }

  // Dictionaries are separate files so an English visitor downloads none of
  // them. Injecting a <script> works from file:// too, where fetch() would be
  // blocked by the browser's local-file rules.
  const loading = {};
  const unavailable = {};
  function loadDict(code, done) {
    if (code === "en" || I18N[code] || unavailable[code]) return done();
    if (loading[code]) return loading[code].push(done);
    loading[code] = [done];
    const el = document.createElement("script");
    el.src = (I18N.path || "assets/i18n/") + code + ".js";
    el.onload = el.onerror = function () {
      // A dictionary that did not arrive is remembered as unavailable, so a
      // failed fetch falls back to English once instead of retrying forever.
      if (!I18N[code]) unavailable[code] = true;
      const queue = loading[code] || [];
      loading[code] = null;
      queue.forEach(function (fn) { fn(); });
    };
    document.head.appendChild(el);
  }

  // Nothing is written to the visitor's device, so a dismissal lasts as long as
  // the page does. The notice discloses that a machine translated this view;
  // disclosing it on every view is the honest end of that trade.
  const dismissed = [];
  function isNoteDismissed(code) {
    return dismissed.indexOf(code) !== -1;
  }
  function dismissNote(code) {
    if (dismissed.indexOf(code) === -1) dismissed.push(code);
  }

  function applyLang(code) {
    if (!I18N || SUPPORTED.indexOf(code) === -1) code = "en";
    if (code !== "en" && !I18N[code]) {
      if (unavailable[code]) {
        code = "en";                       // dictionary missing: show the source
      } else {
        loadDict(code, function () { applyLang(code); });
        return;
      }
    }
    const dict = code === "en" ? null : I18N[code];

    textNodes.forEach(function (t) {
      const out = dict && dict[t.key] ? dict[t.key] : t.key;
      t.node.nodeValue = t.lead + out + t.tail;
    });
    attrNodes.forEach(function (a) {
      const out = dict && dict[a.key] ? dict[a.key] : a.key;
      a.el.setAttribute(a.attr, out);
    });

    document.documentElement.lang = code;

    // Arabic reads right-to-left; everything else is left-to-right.
    const meta = I18N.languages.filter(function (l) { return l.code === code; })[0];
    document.documentElement.dir = meta && meta.rtl ? "rtl" : "ltr";

    // AI-translation notice. Dismissing it is remembered per language, so each
    // translation still discloses itself once rather than nagging every visit.
    const note = $("#transNote");
    if (note) {
      const d = I18N.disclaimer[code];
      if (d && !isNoteDismissed(code)) {
        $("#transNoteText").textContent = d.text;
        $("#transNoteLink").textContent = d.link;
        $("#transNoteOk").textContent = d.ok || "OK";
        note.hidden = false;
      } else {
        note.hidden = true;
      }
    }

    const sel = $("#langSelect");
    if (sel) {
      sel.value = code;
      sel.setAttribute("aria-label", I18N.selectorLabel[code] || "Language");
    }

    // keep the choice in the address bar instead of on the device, so a reload
    // or a shared link lands on the same language
    try {
      const url = new URL(window.location.href);
      if (code === "en") url.searchParams.delete("lang");
      else url.searchParams.set("lang", code);
      window.history.replaceState(null, "", url.toString());
    } catch (e) { /* older browser: the choice simply lasts this page */ }

    // keep the URL shareable without reloading
    try {
      const url = new URL(window.location.href);
      if (code === "en") url.searchParams.delete("lang");
      else url.searchParams.set("lang", code);
      history.replaceState(null, "", url.toString());
    } catch (e) { /* file:// */ }
  }

  if (I18N) {
    snapshot();

    const sel = $("#langSelect");
    if (sel) {
      // The option shows the native name first, then the English name, so the
      // ordering stays legible to someone who cannot read the script.
      function option(l) {
        const o = document.createElement("option");
        o.value = l.code;
        o.textContent = l.native === l.label ? l.label : l.native + " · " + l.label;
        return o;
      }

      // Region headings only earn their place once there are regions to head.
      // With a short list (or every entry left unregioned) a single "Other"
      // group is worse than a plain list, so fall back to one.
      const groups = {};
      I18N.languages.forEach(function (l) {
        if (!l.region) return;
        (groups[l.region] = groups[l.region] || []).push(l);
      });
      const regions = Object.keys(groups).sort();

      if (regions.length < 2) {
        I18N.languages.forEach(function (l) { sel.appendChild(option(l)); });
      } else {
        regions.forEach(function (region) {
          const g = document.createElement("optgroup");
          g.label = region;
          groups[region].forEach(function (l) { g.appendChild(option(l)); });
          sel.appendChild(g);
        });
      }

      sel.addEventListener("change", function () { applyLang(sel.value); });
    }

    const noteLink = $("#transNoteLink");
    if (noteLink) noteLink.addEventListener("click", function () { applyLang("en"); });

    const noteOk = $("#transNoteOk");
    if (noteOk) {
      noteOk.addEventListener("click", function () {
        dismissNote(document.documentElement.lang);
        $("#transNote").hidden = true;
      });
    }

    // ?lang= is the only source. English stays the default: it is the authentic
    // version, so we never guess from browser language and never store a choice.
    let start = "en";
    try {
      const q = new URLSearchParams(window.location.search).get("lang");
      if (q && SUPPORTED.indexOf(q) !== -1) start = q;
    } catch (e) { /* noop */ }
    if (start !== "en") applyLang(start);
    else if (sel) sel.value = "en";
  }

  /* ---------------------------------------------------------------
     3. Theme (light / dark) with memory
  --------------------------------------------------------------- */
  const root = document.documentElement;
  const PALETTES = ["green", "blue", "slate", "ocean", "violet"];
  const darkQuery = window.matchMedia("(prefers-color-scheme: dark)");

  // Preferences last as long as the page and are never written anywhere. The
  // defaults are night with a green light, set on <html> in the markup so the first paint
  // is already correct; "System" still follows the OS while it is selected.
  let currentMode = "dark";
  let currentPalette = "green";
  function storedMode() { return currentMode; }
  function storedPalette() { return currentPalette; }

  function applyMode(mode) {
    const resolved = mode === "system"
      ? (darkQuery.matches ? "dark" : "light")
      : mode;
    root.setAttribute("data-theme", resolved);
    $$(".appear__mode").forEach(function (b) {
      b.setAttribute("aria-pressed", String(b.getAttribute("data-mode") === mode));
    });
  }
  function applyPalette(name) {
    root.setAttribute("data-palette", name);
    $$(".appear__sw").forEach(function (b) {
      b.setAttribute("aria-pressed", String(b.getAttribute("data-palette") === name));
    });
  }

  applyMode(storedMode());
  applyPalette(storedPalette());

  // keep following the OS while the visitor is on "system"
  darkQuery.addEventListener("change", function () {
    if (storedMode() === "system") applyMode("system");
  });

  const appearBtn = $("#appearBtn");
  const appearPanel = $("#appearPanel");

  function setAppear(open) {
    if (!appearBtn || !appearPanel) return;
    appearPanel.hidden = !open;
    appearBtn.setAttribute("aria-expanded", String(open));
  }

  if (appearBtn && appearPanel) {
    appearBtn.addEventListener("click", function (e) {
      e.stopPropagation();
      setAppear(appearPanel.hidden);
    });
    appearPanel.addEventListener("click", function (e) { e.stopPropagation(); });

    $$(".appear__mode", appearPanel).forEach(function (b) {
      b.addEventListener("click", function () {
        const mode = b.getAttribute("data-mode");
        currentMode = mode;
        applyMode(mode);
      });
    });
    $$(".appear__sw", appearPanel).forEach(function (b) {
      b.addEventListener("click", function () {
        const name = b.getAttribute("data-palette");
        currentPalette = name;
        applyPalette(name);
      });
    });

    document.addEventListener("click", function () { setAppear(false); });
    document.addEventListener("keydown", function (e) {
      if (e.key === "Escape" && !appearPanel.hidden) { setAppear(false); appearBtn.focus(); }
    });
  }

  /* ---------------------------------------------------------------
     4. Mobile menu
  --------------------------------------------------------------- */
  const burger = $("#burger");
  const menu = $("#mobileMenu");

  function setMenu(open) {
    if (!burger || !menu) return;
    menu.hidden = !open;
    burger.classList.toggle("is-open", open);
    burger.setAttribute("aria-expanded", String(open));
    burger.setAttribute("aria-label", open ? "Close menu" : "Open menu");
    document.body.style.overflow = open ? "hidden" : "";
  }

  if (burger && menu) {
    burger.addEventListener("click", function () { setMenu(menu.hidden); });
    $$("a", menu).forEach(function (a) { a.addEventListener("click", function () { setMenu(false); }); });
    document.addEventListener("keydown", function (e) {
      if (e.key === "Escape" && !menu.hidden) { setMenu(false); burger.focus(); }
    });
    window.addEventListener("resize", function () {
      if (window.innerWidth >= 980 && !menu.hidden) setMenu(false);
    });
  }


  /* ---------------------------------------------------------------
     4b. Nav dropdowns
     Hover opens them on a pointer device; click and keyboard work
     everywhere, which is what a touch screen and a screen reader get.
  --------------------------------------------------------------- */
  const drops = $$(".nd").map(function (root) {
    return { root: root, btn: $(".nd__btn", root), panel: $(".nd__panel", root) };
  }).filter(function (d) { return d.btn && d.panel; });

  if (drops.length) {
    let hoverable = false;
    try {
      hoverable = window.matchMedia("(hover: hover) and (pointer: fine)").matches;
    } catch (e) { /* older browser: click only, which still works */ }

    function openDrop(d, open) {
      d.panel.hidden = !open;
      d.btn.setAttribute("aria-expanded", String(open));
    }

    function closeAll(except) {
      drops.forEach(function (d) { if (d !== except) openDrop(d, false); });
    }

    drops.forEach(function (d) {
      d.btn.addEventListener("click", function (e) {
        e.stopPropagation();
        const open = d.panel.hidden;
        closeAll(d);
        openDrop(d, open);
      });

      // arrow-down from the button moves into the panel
      d.btn.addEventListener("keydown", function (e) {
        if (e.key === "ArrowDown") {
          e.preventDefault();
          closeAll(d);
          openDrop(d, true);
          const first = $("a", d.panel);
          if (first) first.focus();
        }
      });

      if (hoverable) {
        d.root.addEventListener("mouseenter", function () { closeAll(d); openDrop(d, true); });
        d.root.addEventListener("mouseleave", function () { openDrop(d, false); });
      }

      // tabbing out of the last link should close the panel behind you
      d.root.addEventListener("focusout", function (e) {
        if (!d.root.contains(e.relatedTarget)) openDrop(d, false);
      });

      $$("a", d.panel).forEach(function (a) {
        a.addEventListener("click", function () { openDrop(d, false); });
      });
    });

    document.addEventListener("click", function (e) {
      if (!e.target.closest || !e.target.closest(".nd")) closeAll(null);
    });

    document.addEventListener("keydown", function (e) {
      if (e.key !== "Escape") return;
      drops.forEach(function (d) {
        if (!d.panel.hidden) { openDrop(d, false); d.btn.focus(); }
      });
    });
  }


  /* ---------------------------------------------------------------
     4c. Article topic filter
     Chips are generated in the page, so with scripting off they are
     simply absent and every article stays listed.
  --------------------------------------------------------------- */
  const artFilter = $("#artFilter");
  const artGrid = $("#artGrid");

  if (artFilter && artGrid) {
    const cards = $$(".post-card", artGrid);

    artFilter.addEventListener("click", function (e) {
      const chip = e.target.closest(".chip");
      if (!chip) return;

      const want = chip.getAttribute("data-filter");
      $$(".chip", artFilter).forEach(function (c) {
        const on = c === chip;
        c.classList.toggle("is-on", on);
        c.setAttribute("aria-pressed", String(on));
      });

      cards.forEach(function (card) {
        card.hidden = want !== "all" && card.getAttribute("data-tag") !== want;
      });

      // the URL should survive a reload and a share
      try {
        const url = new URL(window.location.href);
        if (want === "all") url.searchParams.delete("topic");
        else url.searchParams.set("topic", want);
        history.replaceState(null, "", url);
      } catch (err) { /* noop */ }
    });

    // honour ?topic= on arrival
    try {
      const topic = new URLSearchParams(window.location.search).get("topic");
      if (topic) {
        const chip = $('.chip[data-filter="' + CSS.escape(topic) + '"]', artFilter);
        if (chip) chip.click();
      }
    } catch (err) { /* noop */ }
  }

  /* ---------------------------------------------------------------
     5. Reveal on scroll
  --------------------------------------------------------------- */
  const revealables = $$("[data-reveal]");

  if (reduceMotion || !("IntersectionObserver" in window)) {
    revealables.forEach(function (el) { el.classList.add("is-in"); });
  } else {
    const io = new IntersectionObserver(function (entries) {
      entries.forEach(function (entry) {
        if (entry.isIntersecting) {
          entry.target.classList.add("is-in");
          io.unobserve(entry.target);
        }
      });
    }, { rootMargin: "0px 0px -8% 0px", threshold: 0.12 });
    revealables.forEach(function (el) { io.observe(el); });
  }

  /* ---------------------------------------------------------------
     6. Scroll-driven UI: progress bar, sticky nav, sticky mobile CTA,
        pinned chapters, the chapter rail, and the state of the voyage
  --------------------------------------------------------------- */
  const nav = $("#nav");
  const progressBar = $("#progressBar");
  const mobileBar = $("#mobileBar");
  const clamp01 = function (n) { return n < 0 ? 0 : n > 1 ? 1 : n; };

  // Pinned chapters hold still while their statements change. They need a
  // tall enough window and a visitor who has not asked for less motion;
  // otherwise the same markup is an ordinary list.
  const pins = $$("[data-pin]").map(function (el) {
    return { el: el, items: $$(".pin__item", el), q: 0, active: false };
  });
  function voyageWanted() { return !reduceMotion && window.innerHeight >= 560; }
  function setModes() {
    root.classList.toggle("pins-on", pins.length > 0 && voyageWanted());
    root.classList.toggle("fly", voyageWanted());
  }
  setModes();

  // The home page's chapters, top to bottom, and the rail links that point at them.
  const chapters = $$("main > section[id]");
  const heroInner = $(".hero__inner");
  const railLinks = $$("#rail a").map(function (a) {
    return { link: a, el: document.querySelector(a.getAttribute("href")) };
  }).filter(function (p) { return p.el; });

  // Where the light we are following sits in each chapter: x and y as
  // fractions of the window, k as its strength.
  const LIGHT = {
    hero: [0.5, 0.23, 1], problem: [0.5, 0.22, 0.5], services: [0.14, 0.2, 0.36],
    human: [0.5, 0.5, 0.6], industries: [0.86, 0.62, 0.3], build: [0.8, 0.4, 0.5],
    process: [0.72, 0.5, 0.72], about: [0.1, 0.28, 0.3], work: [0.9, 0.16, 0.34],
    testimonials: [0.5, 0.16, 0.36], articles: [0.12, 0.5, 0.28], cta: [0.5, 0.36, 1.25],
    contact: [0.5, 0.1, 0.4]
  };
  const sky = { x: 0.78, y: 0.2, k: 0.5, draw: 0, drawOn: 0, twin: 0, boost: 0, scrollY: 0, docH: 1 };

  let ticking = false;

  function onScroll() {
    const y = window.pageYOffset || document.documentElement.scrollTop;
    const vh = window.innerHeight;
    const docH = document.documentElement.scrollHeight - vh;
    const flying = root.classList.contains("fly");

    if (progressBar) progressBar.style.transform = "scaleX(" + (docH > 0 ? Math.min(y / docH, 1) : 0) + ")";
    if (nav) nav.classList.toggle("is-stuck", y > 8);
    if (mobileBar) mobileBar.classList.toggle("is-visible", y > vh * 0.55);

    // pinned chapters: how far through, and which statement is showing
    const pinned = root.classList.contains("pins-on");
    pins.forEach(function (p) {
      const r = p.el.getBoundingClientRect();
      const travel = r.height - vh;
      p.q = pinned && travel > 0 ? clamp01(-r.top / travel) : 0;
      p.active = pinned && r.top <= vh * 0.5 && r.bottom >= vh * 0.5;
      const n = p.items.length;
      const idx = Math.min(n - 1, Math.floor(p.q * n));
      p.items.forEach(function (it, i) {
        it.classList.toggle("is-on", pinned && i === idx);
        it.classList.toggle("is-past", pinned && i < idx);
      });
      p.el.style.setProperty("--q", p.q.toFixed(3));
    });

    // each chapter knows how far it has arrived (--e: 0 far away, 1 here),
    // so its heading can grow in from the distance; the first screen knows
    // how far behind us it is (--x), so we can fly through it
    let current = null;
    chapters.forEach(function (sec) {
      const r = sec.getBoundingClientRect();
      if (r.top <= vh * 0.5 && r.bottom > vh * 0.5) current = sec;
      if (flying && r.top < vh * 1.2 && r.bottom > -vh * 0.2) {
        sec.style.setProperty("--e", clamp01((vh - r.top) / (vh * 0.6)).toFixed(3));
      }
    });
    if (heroInner) heroInner.style.setProperty("--x", flying ? clamp01(y / (vh * 0.75)).toFixed(3) : "0");
    const id = current ? current.id : "";

    let lit = null;
    railLinks.forEach(function (p) {
      p.link.classList.remove("is-active");
      if (p.el.getBoundingClientRect().top <= vh * 0.5) lit = p;
    });
    if (lit) lit.link.classList.add("is-active");

    // tell the sky where we are
    const t = LIGHT[id];
    const narrow = window.innerWidth < 900;
    if (t) { sky.x = t[0]; sky.y = t[1]; sky.k = t[2]; }
    else if (chapters.length === 0) { sky.x = 0.78; sky.y = 0.2; sky.k = 0.5; }
    sky.twin = id === "human" ? 1 : 0;
    sky.boost = 0;
    const proc = pins.filter(function (p) { return p.el.id === "processPin"; })[0];
    if (id === "process" && proc && proc.active) {
      sky.drawOn = 1; sky.draw = proc.q;
      sky.boost = clamp01((proc.q - 0.86) / 0.1);
      if (narrow) { sky.x = 0.5; sky.y = 0.3; }
    } else {
      sky.drawOn = 0;
      if (id === "process") { sky.x = narrow ? 0.5 : 0.8; sky.y = 0.24; sky.k = 0.4; }
    }
    if (narrow && id === "human") sky.y = 0.4;
    sky.scrollY = y;
    sky.docH = Math.max(1, docH);

    ticking = false;
  }

  function requestScroll() {
    if (!ticking) { ticking = true; window.requestAnimationFrame(onScroll); }
  }

  window.addEventListener("scroll", requestScroll, { passive: true });
  window.addEventListener("resize", function () { setModes(); requestScroll(); });
  onScroll();

  /* ---------------------------------------------------------------
     6b. The voyage
     One fixed canvas behind the page. Scrolling flies the camera
     forward through a field of stars; planets drift past at the side;
     the light we follow (the idea) waits in each chapter, becomes a
     twin star for Human + AI, and in the process chapter draws itself
     into a product and launches. Colours come from the CSS tokens, so
     the theme and the palette apply here too. Under
     prefers-reduced-motion it repaints only when the page moves, and
     nothing streaks, orbits or pulses.
  --------------------------------------------------------------- */
  (function () {
    const canvas = $("#sky");
    if (!canvas || !canvas.getContext) return;
    const ctx = canvas.getContext("2d");
    if (!ctx) return;

    const SPEED = 0.00042;          // depth travelled per pixel scrolled
    let W = 0, H = 0, stars = [];
    const col = { glow: "84,224,160", star: "255,255,255", core: "255,255,255", ink: "238,243,240", bg: "4,8,6", body: "10,19,16", light: false };
    const cur = { x: sky.x, y: sky.y, k: sky.k, on: 0, q: 0, twin: 0, vel: 0, lastY: 0 };

    // Planets along the route: f is how far through the page they sit,
    // x and y how far off the flight path, r their size.
    const BODIES = [
      { f: 0.07, x: 0.9, y: -0.3, r: 0.07, ring: false },
      { f: 0.19, x: 0.96, y: 0.34, r: 0.1, ring: true },
      { f: 0.33, x: -0.98, y: -0.36, r: 0.06, ring: false },
      { f: 0.47, x: -0.94, y: 0.4, r: 0.11, ring: false },
      { f: 0.66, x: -0.98, y: -0.3, r: 0.09, ring: true },
      { f: 0.79, x: 0.96, y: 0.3, r: 0.07, ring: false },
      { f: 0.92, x: 0.92, y: -0.36, r: 0.05, ring: false }
    ];

    // Clouds of dust along the route: very large, very faint, some warm.
    const CLOUDS = [
      { f: 0.02, x: -0.5, y: 0.3, r: 0.9, warm: false }, { f: 0.14, x: 0.6, y: -0.1, r: 1.1, warm: true },
      { f: 0.28, x: -0.4, y: -0.3, r: 1.0, warm: false }, { f: 0.43, x: 0.5, y: 0.25, r: 1.2, warm: false },
      { f: 0.58, x: -0.6, y: 0.1, r: 1.0, warm: true }, { f: 0.73, x: 0.45, y: -0.25, r: 1.1, warm: false },
      { f: 0.88, x: -0.35, y: 0.3, r: 1.0, warm: false }, { f: 1.0, x: 0.3, y: -0.1, r: 1.2, warm: true }
    ];

    // a small seeded generator, so the sky is the same on every visit
    function rng(seed) {
      return function () {
        seed |= 0; seed = seed + 0x6D2B79F5 | 0;
        let t = Math.imul(seed ^ seed >>> 15, 1 | seed);
        t = t + Math.imul(t ^ t >>> 7, 61 | t) ^ t;
        return ((t ^ t >>> 14) >>> 0) / 4294967296;
      };
    }

    function hexRgb(hex, fallback) {
      const m = /^#?([0-9a-f]{2})([0-9a-f]{2})([0-9a-f]{2})$/i.exec((hex || "").trim());
      return m ? parseInt(m[1], 16) + "," + parseInt(m[2], 16) + "," + parseInt(m[3], 16) : fallback;
    }

    function readColours() {
      const cs = getComputedStyle(root);
      const get = function (n, d) { return (cs.getPropertyValue(n) || d).replace(/\s+/g, "") || d; };
      col.glow = get("--glow-rgb", col.glow);
      col.star = get("--star-rgb", col.star);
      col.ink = get("--ink-rgb", col.ink);
      col.bg = hexRgb(cs.getPropertyValue("--bg"), col.bg);
      col.body = hexRgb(cs.getPropertyValue("--bg-2"), col.body);
      col.light = root.getAttribute("data-theme") === "light";
      col.core = col.light ? col.glow : "255,255,255";
    }

    function resize() {
      const dpr = Math.min(window.devicePixelRatio || 1, 2);
      W = canvas.clientWidth; H = canvas.clientHeight;
      canvas.width = Math.round(W * dpr); canvas.height = Math.round(H * dpr);
      ctx.setTransform(dpr, 0, 0, dpr, 0, 0);
      const rand = rng(20261113);
      const n = Math.min(760, Math.round(W * H / 1900));
      stars = [];
      for (let i = 0; i < n; i++) {
        stars.push({ x: rand() * 2 - 1, y: rand() * 2 - 1, z: rand(), r: 0.5 + rand(), a: 0.35 + rand() * 0.65 });
      }
    }

    // Draw the first `t` (0..1) of a polyline given as [x0,y0,x1,y1,...].
    function trace(pts, t) {
      if (t <= 0) return;
      let total = 0;
      for (let i = 2; i < pts.length; i += 2) total += Math.hypot(pts[i] - pts[i - 2], pts[i + 1] - pts[i - 1]);
      let left = total * Math.min(t, 1);
      ctx.beginPath(); ctx.moveTo(pts[0], pts[1]);
      for (let i = 2; i < pts.length && left > 0; i += 2) {
        const dx = pts[i] - pts[i - 2], dy = pts[i + 1] - pts[i - 1];
        const len = Math.hypot(dx, dy);
        const f = len > 0 ? Math.min(1, left / len) : 1;
        ctx.lineTo(pts[i - 2] + dx * f, pts[i - 1] + dy * f);
        left -= len;
      }
      ctx.stroke();
    }
    const win = function (q, a, b) { return q <= a ? 0 : q >= b ? 1 : (q - a) / (b - a); };
    function roundRect(x, y, w, h, r) {
      const p = [x + r, y], steps = 6;
      const corner = function (cx, cy, a0) {
        for (let i = 1; i <= steps; i++) { const a = a0 + (Math.PI / 2) * i / steps; p.push(cx + Math.cos(a) * r, cy + Math.sin(a) * r); }
      };
      p.push(x + w - r, y); corner(x + w - r, y + r, -Math.PI / 2);
      p.push(x + w, y + h - r); corner(x + w - r, y + h - r, 0);
      p.push(x + r, y + h); corner(x + r, y + h - r, Math.PI / 2);
      p.push(x, y + r); corner(x + r, y + r, Math.PI);
      return p;
    }

    // The idea becomes a product: guides are marked out, a screen is drawn
    // around the light, its contents are filled in, and it goes live.
    function drawProduct(cx, cy, q, alpha, time) {
      const u = Math.max(70, Math.min(170, Math.min(W, H) * 0.17));
      const w = u * 1.25, h = u * 2.5, x = cx - w / 2, y = cy - h / 2;
      ctx.lineCap = "round"; ctx.lineJoin = "round";

      // 1. plan: guides and corner marks
      const plan = win(q, 0.2, 0.46);
      ctx.strokeStyle = "rgba(" + col.glow + "," + (0.55 * alpha) + ")";
      ctx.lineWidth = 1; ctx.setLineDash([3, 6]);
      trace([cx - u * 2.1, cy, cx + u * 2.1, cy], plan);
      trace([cx, cy - u * 1.9, cx, cy + u * 1.9], plan);
      ctx.setLineDash([]);
      const m = u * 0.22, cornerT = win(q, 0.3, 0.5);
      [[x, y, 1, 1], [x + w, y, -1, 1], [x, y + h, 1, -1], [x + w, y + h, -1, -1]].forEach(function (c) {
        trace([c[0] + c[2] * m, c[1], c[0], c[1], c[0], c[1] + c[3] * m], cornerT);
      });

      // 2. build: the screen and what is on it
      ctx.strokeStyle = "rgba(" + col.ink + "," + (0.9 * alpha) + ")";
      ctx.lineWidth = 1.4;
      trace(roundRect(x, y, w, h, u * 0.2), win(q, 0.44, 0.66));
      const pad = u * 0.16, ix = x + pad, iw = w - pad * 2;
      ctx.lineWidth = 3;
      trace([ix, y + u * 0.42, ix + iw * 0.62, y + u * 0.42], win(q, 0.58, 0.68));
      ctx.lineWidth = 1.2;
      for (let i = 0; i < 3; i++) {
        const ry = y + u * (0.74 + i * 0.36), t = win(q, 0.62 + i * 0.04, 0.74 + i * 0.04), s = u * 0.2;
        trace([ix, ry, ix + s, ry, ix + s, ry + s, ix, ry + s, ix, ry], t);
        trace([ix + s + u * 0.12, ry + s / 2, ix + iw * (0.9 - i * 0.14), ry + s / 2], t);
      }
      const by = y + h - u * 0.52, bh = u * 0.3, live = win(q, 0.8, 0.92);
      trace(roundRect(ix, by, iw, bh, bh / 2), win(q, 0.72, 0.82));
      if (live > 0) {
        ctx.fillStyle = "rgba(" + col.glow + "," + (0.85 * live * alpha) + ")";
        ctx.beginPath();
        const rr = roundRect(ix, by, iw, bh, bh / 2);
        ctx.moveTo(rr[0], rr[1]); for (let i = 2; i < rr.length; i += 2) ctx.lineTo(rr[i], rr[i + 1]);
        ctx.closePath(); ctx.fill();
      }

      // 3. launch: signal arcs rise from the screen
      const go = win(q, 0.84, 1);
      if (go > 0) {
        ctx.lineWidth = 1.3;
        for (let i = 0; i < 3; i++) {
          const ph = reduceMotion ? i / 3 : ((time * 0.00035 + i / 3) % 1);
          const r = u * (0.5 + ph * 1.5);
          ctx.strokeStyle = "rgba(" + col.glow + "," + ((1 - ph) * 0.75 * go * alpha) + ")";
          ctx.beginPath(); ctx.arc(cx, y - u * 0.1, r, Math.PI * 1.18, Math.PI * 1.82); ctx.stroke();
        }
      }
    }

    // one glowing point: a soft core with a coloured skirt
    function core(x, y, r, rgb, strength) {
      const c = ctx.createRadialGradient(x, y, 0, x, y, r);
      c.addColorStop(0, "rgba(" + rgb + "," + Math.min(1, 0.5 + strength) + ")");
      c.addColorStop(0.16, "rgba(" + rgb + "," + (0.85 * strength) + ")");
      c.addColorStop(0.4, "rgba(" + col.glow + "," + (0.5 * strength) + ")");
      c.addColorStop(1, "rgba(" + col.glow + ",0)");
      ctx.fillStyle = c; ctx.beginPath(); ctx.arc(x, y, r, 0, 6.2832); ctx.fill();
    }

    function paint(time) {
      ctx.clearRect(0, 0, W, H);
      const vx = W * 0.5, vy = H * 0.46, F = Math.max(W, H) * 0.5;
      const lx = cur.x * W, ly = cur.y * H, k = cur.k;

      // how fast we are going: scrolling, plus the launch
      const dy = Math.abs(sky.scrollY - cur.lastY); cur.lastY = sky.scrollY;
      cur.vel += ((reduceMotion ? 0 : dy) - cur.vel) * 0.18;
      const streak = Math.min(0.09, cur.vel * SPEED * 1.5 + sky.boost * 0.05);
      const cam = sky.scrollY * SPEED + (reduceMotion ? 0 : time * 0.000016);

      // the light's halo sits behind everything
      if (k > 0.01) {
        const R = Math.max(W, H) * 0.42 * (0.6 + 0.4 * Math.min(k, 1.4));
        const g = ctx.createRadialGradient(lx, ly, 0, lx, ly, R);
        const a = (col.light ? 0.26 : 0.4) * Math.min(k, 1.3);
        g.addColorStop(0, "rgba(" + col.glow + "," + a + ")");
        g.addColorStop(0.35, "rgba(" + col.glow + "," + (a * 0.3) + ")");
        g.addColorStop(1, "rgba(" + col.glow + ",0)");
        ctx.fillStyle = g; ctx.fillRect(0, 0, W, H);
      }

      // dust clouds we pass through
      const camMaxC = sky.docH * SPEED;
      for (let i = 0; i < CLOUDS.length; i++) {
        const c = CLOUDS[i];
        const d = c.f * camMaxC + 0.5 - sky.scrollY * SPEED;
        if (d < 0.08 || d > 1.8) continue;
        const sx = vx + c.x * F * 0.5 / d, sy = vy + c.y * F * 0.5 / d, R = c.r * F * 0.5 / d;
        const a = Math.min(1, (1.8 - d) * 1.6) * Math.min(1, (d - 0.08) * 6) * (col.light ? 0.1 : 0.16);
        const rgb = c.warm ? "255,150,96" : col.glow;
        const g = ctx.createRadialGradient(sx, sy, 0, sx, sy, R);
        g.addColorStop(0, "rgba(" + rgb + "," + a + ")");
        g.addColorStop(0.5, "rgba(" + rgb + "," + (a * 0.35) + ")");
        g.addColorStop(1, "rgba(" + rgb + ",0)");
        ctx.fillStyle = g; ctx.fillRect(sx - R, sy - R, R * 2, R * 2);
      }

      // stars: each has a depth; the camera moves through them, so they
      // come towards us and stretch into streaks when we travel fast
      ctx.lineCap = "round";
      const starA = col.light ? 0.42 : 1;
      for (let i = 0; i < stars.length; i++) {
        const s = stars[i];
        let d = ((s.z - cam) % 1 + 1) % 1;
        d = 0.02 + d * 0.98;
        const px = vx + s.x * F / d, py = vy + s.y * F / d;
        if (px < -40 || px > W + 40 || py < -40 || py > H + 40) continue;
        const near = 1 - d;
        const alpha = s.a * Math.min(1, 0.25 + near * 3) * Math.min(1, (d - 0.02) * 22) * starA;
        const r = 0.5 + near * near * 2.3 * s.r;
        if (streak > 0.0015) {
          const d2 = d + streak * (0.4 + near);
          ctx.strokeStyle = "rgba(" + col.star + "," + alpha + ")";
          ctx.lineWidth = Math.max(0.6, r * 1.3);
          ctx.beginPath(); ctx.moveTo(px, py); ctx.lineTo(vx + s.x * F / d2, vy + s.y * F / d2); ctx.stroke();
        } else {
          ctx.fillStyle = "rgba(" + col.star + "," + alpha + ")";
          ctx.beginPath(); ctx.arc(px, py, r, 0, 6.2832); ctx.fill();
        }
      }

      // planets along the route, lit from the side the light is on
      const camMax = sky.docH * SPEED;
      for (let i = 0; i < BODIES.length; i++) {
        const b = BODIES[i];
        const d = b.f * camMax + 0.42 - sky.scrollY * SPEED;
        if (d < 0.05 || d > 1.5) continue;
        const sx = vx + b.x * F * 0.56 / d, sy = vy + b.y * F * 0.56 / d, R = b.r * F * 0.62 / d;
        if (sx < -R * 3 || sx > W + R * 3 || sy < -R * 3 || sy > H + R * 3) continue;
        const alpha = Math.min(1, (1.5 - d) * 2.2) * Math.min(1, (d - 0.05) * 12);
        let ax = lx - sx, ay = ly - sy; const al = Math.hypot(ax, ay) || 1; ax /= al; ay /= al;
        if (b.ring) {
          ctx.strokeStyle = "rgba(" + col.glow + "," + (0.4 * alpha) + ")"; ctx.lineWidth = Math.max(1, R * 0.05);
          ctx.beginPath(); ctx.ellipse(sx, sy, R * 1.9, R * 0.46, -0.42, Math.PI, 6.2832); ctx.stroke();
        }
        ctx.fillStyle = "rgba(" + col.body + "," + alpha + ")";
        ctx.beginPath(); ctx.arc(sx, sy, R, 0, 6.2832); ctx.fill();
        const g = ctx.createRadialGradient(sx + ax * R * 0.6, sy + ay * R * 0.6, R * 0.05, sx, sy, R * 1.05);
        g.addColorStop(0, "rgba(" + col.glow + "," + ((col.light ? 0.5 : 0.62) * alpha) + ")");
        g.addColorStop(0.5, "rgba(" + col.glow + "," + (0.13 * alpha) + ")");
        g.addColorStop(1, "rgba(" + col.bg + "," + (0.55 * alpha) + ")");
        ctx.fillStyle = g; ctx.beginPath(); ctx.arc(sx, sy, R, 0, 6.2832); ctx.fill();
        ctx.strokeStyle = "rgba(" + col.glow + "," + (0.3 * alpha) + ")"; ctx.lineWidth = 1;
        ctx.beginPath(); ctx.arc(sx, sy, R, 0, 6.2832); ctx.stroke();
        if (b.ring) {
          ctx.strokeStyle = "rgba(" + col.glow + "," + (0.55 * alpha) + ")"; ctx.lineWidth = Math.max(1, R * 0.05);
          ctx.beginPath(); ctx.ellipse(sx, sy, R * 1.9, R * 0.46, -0.42, 0, Math.PI); ctx.stroke();
        }
      }

      // the light we follow
      if (k > 0.01) {
        const R = Math.max(W, H) * 0.42 * (0.6 + 0.4 * Math.min(k, 1.4));
        ctx.lineWidth = 1;
        for (let i = 0; i < 3; i++) {
          const ph = reduceMotion ? (i + 1) / 4 : ((time * 0.00009 + i / 3) % 1);
          ctx.strokeStyle = "rgba(" + col.glow + "," + ((1 - ph) * (col.light ? 0.5 : 0.34) * Math.min(k, 1)) + ")";
          ctx.beginPath(); ctx.arc(lx, ly, 14 + ph * R * 0.5, 0, 6.2832); ctx.stroke();
        }
        const cr = 26 + 30 * k, tw = cur.twin;
        if (tw > 0.02) {
          // a twin star: two lights circling each other
          const a = reduceMotion ? 0.6 : time * 0.0006, o = (34 + 26 * k) * tw;
          core(lx + Math.cos(a) * o, ly + Math.sin(a) * o * 0.42, cr * (1 - 0.25 * tw), col.core, k);
          core(lx - Math.cos(a) * o, ly - Math.sin(a) * o * 0.42, cr * (1 - 0.4 * tw), col.glow, k * 0.9);
        } else {
          core(lx, ly, cr, col.core, k);
        }
      }

      if (cur.on > 0.01) drawProduct(lx, ly, cur.q, cur.on, time);
    }

    let first = true, running = false;
    function frame(time) {
      running = false;
      if (document.hidden) return;
      const snap = first || reduceMotion;
      const e = snap ? 1 : 0.07;
      cur.x += (sky.x - cur.x) * e; cur.y += (sky.y - cur.y) * e; cur.k += (sky.k - cur.k) * e;
      cur.twin += (sky.twin - cur.twin) * (snap ? 1 : 0.06);
      cur.on += (sky.drawOn - cur.on) * (snap ? 1 : 0.1);
      cur.q += (sky.draw - cur.q) * (snap ? 1 : 0.18);
      if (first) cur.lastY = sky.scrollY;
      first = false;
      paint(time || 0);
      if (!reduceMotion) kick();
    }
    function kick() { if (!running) { running = true; window.requestAnimationFrame(frame); } }

    readColours();
    resize();
    kick();

    window.addEventListener("resize", function () { resize(); kick(); });
    document.addEventListener("visibilitychange", function () { if (!document.hidden) kick(); });
    // under reduced motion nothing animates, so repaint only when the page moves
    if (reduceMotion) window.addEventListener("scroll", function () { window.requestAnimationFrame(kick); }, { passive: true });
    // the theme and the palette are attributes on <html>; repaint in the new colours
    if ("MutationObserver" in window) {
      new MutationObserver(function () { readColours(); kick(); })
        .observe(root, { attributes: true, attributeFilter: ["data-theme", "data-palette"] });
    }
  })();

  /* ---------------------------------------------------------------
     7. Price count-up (₹20,000)
  --------------------------------------------------------------- */
  const priceEl = $("#priceCount");
  if (priceEl && !reduceMotion && "IntersectionObserver" in window) {
    const target = parseInt(priceEl.getAttribute("data-count"), 10) || 0;
    const fmt = function (n) { return n.toLocaleString("en-IN"); };

    const priceIO = new IntersectionObserver(function (entries) {
      entries.forEach(function (entry) {
        if (!entry.isIntersecting) return;
        priceIO.disconnect();
        const duration = 1100;
        const startTime = performance.now();
        (function step(now) {
          const t = Math.min((now - startTime) / duration, 1);
          const eased = 1 - Math.pow(1 - t, 3);
          priceEl.textContent = fmt(Math.round(target * eased / 100) * 100);
          if (t < 1) requestAnimationFrame(step);
          else priceEl.textContent = fmt(target);
        })(startTime);
      });
    }, { threshold: 0.4 });

    priceIO.observe(priceEl);
  }

  /* ---------------------------------------------------------------
     8. Pre-email notice
     Every route to my inbox passes through here first. The anchors stay
     real mailto links, so with JavaScript off they simply work; this only
     adds a step when it can, and never records that it was shown.
  --------------------------------------------------------------- */
  (function () {
    const dlg = document.getElementById("mailNotice");
    if (!dlg) return;
    const go = document.getElementById("mailNoticeGo");
    const box = dlg.querySelector(".cdlg__box");
    let opener = null;

    function focusables() {
      return Array.prototype.filter.call(
        dlg.querySelectorAll('a[href], button:not([disabled])'),
        function (el) { return el.offsetParent !== null; });
    }

    function close() {
      dlg.hidden = true;
      document.documentElement.style.overflow = "";
      if (opener && opener.focus) opener.focus();
      opener = null;
    }

    function open(href, from) {
      opener = from;
      go.href = href;
      dlg.hidden = false;
      document.documentElement.style.overflow = "hidden";
      const first = focusables()[0];
      if (first) first.focus();
    }

    // intercept only the links that open a mail client; a booking URL or an
    // Instagram profile hands nothing over and needs no warning
    document.addEventListener("click", function (e) {
      const a = e.target.closest ? e.target.closest("a[href^='mailto:']") : null;
      if (!a) return;
      if (e.metaKey || e.ctrlKey || e.shiftKey || e.button !== 0) return;
      e.preventDefault();
      open(a.getAttribute("href"), a);
    });

    dlg.addEventListener("click", function (e) {
      if (e.target.closest("[data-cdlg-close]")) { e.preventDefault(); close(); }
    });

    go.addEventListener("click", function () {
      // let the navigation happen, then put the page back as it was
      window.setTimeout(close, 0);
    });

    document.addEventListener("keydown", function (e) {
      if (dlg.hidden) return;
      if (e.key === "Escape") { e.preventDefault(); close(); return; }
      if (e.key !== "Tab") return;
      const items = focusables();
      if (!items.length) return;
      const first = items[0], last = items[items.length - 1];
      if (e.shiftKey && document.activeElement === first) { e.preventDefault(); last.focus(); }
      else if (!e.shiftKey && document.activeElement === last) { e.preventDefault(); first.focus(); }
    });

    if (box) box.addEventListener("click", function (e) { e.stopPropagation(); });
  })();

})();
