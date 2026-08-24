/* =====================================================================
   HumansOfCoding — script.js
   Vanilla JS only. No dependencies. Works from file:// or GitHub Pages.
   ===================================================================== */

/* =====================================================================
   >>>>>>>>>>>>>>>>>  EDIT YOUR BUSINESS INFO HERE  <<<<<<<<<<<<<<<<<<<<
   This is the ONLY place you need to change contact details.
   Every button, link and label on the site reads from this object.
   ===================================================================== */
const CONFIG = {
  // Instagram handle (without the @)
  instagram: "humansofcoding",

  // Your email address
  email: "adil@humansofcoding.com",
  emailSubject: "Project enquiry from humansofcoding.com",

  // "Book a Free Call" opens the visitor's email app with this message already
  // written, addressed to the `email` above. Edit the wording freely - every
  // line break is kept. Keep it short: long forms scare people off.
  callSubject: "Free call request - HumansOfCoding",
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
  const I18N = window.HOC_I18N || null;
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
  function loadDict(code, done) {
    if (code === "en" || I18N[code]) return done();
    if (loading[code]) return loading[code].push(done);
    loading[code] = [done];
    const el = document.createElement("script");
    el.src = (I18N.path || "assets/i18n/") + code + ".js";
    el.onload = el.onerror = function () {
      const queue = loading[code] || [];
      loading[code] = null;
      queue.forEach(function (fn) { fn(); });
    };
    document.head.appendChild(el);
  }

  function dismissedNotes() {
    try {
      return (localStorage.getItem("hoc-note-ok") || "").split(",").filter(Boolean);
    } catch (e) { return []; }
  }
  function isNoteDismissed(code) {
    return dismissedNotes().indexOf(code) !== -1;
  }
  function dismissNote(code) {
    const list = dismissedNotes();
    if (list.indexOf(code) === -1) list.push(code);
    try { localStorage.setItem("hoc-note-ok", list.join(",")); } catch (e) { /* private mode */ }
  }

  function applyLang(code) {
    if (!I18N || SUPPORTED.indexOf(code) === -1) code = "en";
    if (code !== "en" && !I18N[code]) {
      // fetch the dictionary, then come back
      loadDict(code, function () { applyLang(code); });
      return;
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

    try { localStorage.setItem("hoc-lang", code); } catch (e) { /* private mode */ }

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
      I18N.languages.forEach(function (l) {
        const o = document.createElement("option");
        o.value = l.code;
        o.textContent = l.native;
        sel.appendChild(o);
      });
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

    // ?lang= wins, then a saved choice. English stays the default: it is the
    // authentic version, so we never guess from browser language.
    let start = "en";
    try {
      const q = new URLSearchParams(window.location.search).get("lang");
      const saved = localStorage.getItem("hoc-lang");
      if (q && SUPPORTED.indexOf(q) !== -1) start = q;
      else if (saved && SUPPORTED.indexOf(saved) !== -1) start = saved;
    } catch (e) { /* noop */ }
    if (start !== "en") applyLang(start);
    else if (sel) sel.value = "en";
  }

  /* ---------------------------------------------------------------
     3. Theme (light / dark) with memory
  --------------------------------------------------------------- */
  const root = document.documentElement;
  const themeBtn = $("#themeToggle");

  function readStoredTheme() {
    try {
      const t = localStorage.getItem("hoc-theme");
      return t === "dark" || t === "light" ? t : null;   // validate, never trust
    } catch (e) { return null; }
  }
  function applyTheme(theme) {
    root.setAttribute("data-theme", theme);
    if (themeBtn) themeBtn.setAttribute("aria-pressed", String(theme === "dark"));
  }

  const stored = readStoredTheme();
  applyTheme(stored || (window.matchMedia("(prefers-color-scheme: dark)").matches ? "dark" : "light"));

  if (themeBtn) {
    themeBtn.addEventListener("click", function () {
      const next = root.getAttribute("data-theme") === "dark" ? "light" : "dark";
      applyTheme(next);
      try { localStorage.setItem("hoc-theme", next); } catch (e) { /* private mode */ }
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
     6. Hand-drawn SVG line "draw in" effect
  --------------------------------------------------------------- */
  if (!reduceMotion) {
    $$(".char .draw").forEach(function (path, i) {
      let len = 500;
      try { if (path.getTotalLength) len = Math.ceil(path.getTotalLength()) || 500; } catch (e) { /* noop */ }
      path.style.setProperty("--len", len);
      path.style.animationDelay = (i * 0.07).toFixed(2) + "s";
    });
  }

  /* ---------------------------------------------------------------
     7. Scroll-driven UI: progress bar, sticky nav, active link,
        timeline fill, sticky mobile CTA
  --------------------------------------------------------------- */
  const nav = $("#nav");
  const progressBar = $("#progressBar");
  const timeline = $("#timeline");
  const mobileBar = $("#mobileBar");
  // pair each nav link with its section, ordered the way they appear in the
  // document (the nav order and the document order are not the same)
  const navTargets = $$(".nav__links a")
    .map(function (a) { return { link: a, el: document.querySelector(a.getAttribute("href")) }; })
    .filter(function (p) { return p.el; })
    .sort(function (a, b) { return a.el.offsetTop - b.el.offsetTop; });

  let ticking = false;

  function onScroll() {
    const y = window.pageYOffset || document.documentElement.scrollTop;
    const docH = document.documentElement.scrollHeight - window.innerHeight;

    if (progressBar) {
      progressBar.style.transform = "scaleX(" + (docH > 0 ? Math.min(y / docH, 1) : 0) + ")";
    }

    if (nav) nav.classList.toggle("is-stuck", y > 8);

    if (mobileBar) mobileBar.classList.toggle("is-visible", y > window.innerHeight * 0.55);

    if (timeline) {
      const r = timeline.getBoundingClientRect();
      const start = window.innerHeight * 0.85;
      const p = (start - r.top) / (r.height * 0.9);
      timeline.style.setProperty("--p", Math.max(0, Math.min(1, p)).toFixed(3));
    }

    // active nav link
    let activeIndex = -1;
    navTargets.forEach(function (pair, i) {
      if (pair.el.getBoundingClientRect().top <= window.innerHeight * 0.35) activeIndex = i;
    });
    navTargets.forEach(function (pair, i) { pair.link.classList.toggle("is-active", i === activeIndex); });

    ticking = false;
  }

  function requestScroll() {
    if (!ticking) {
      ticking = true;
      window.requestAnimationFrame(onScroll);
    }
  }

  window.addEventListener("scroll", requestScroll, { passive: true });
  window.addEventListener("resize", requestScroll);
  onScroll();

  /* ---------------------------------------------------------------
     8. Price count-up (₹50,000)
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
})();
