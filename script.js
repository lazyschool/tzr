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
     2. Theme (light / dark) with memory
  --------------------------------------------------------------- */
  const root = document.documentElement;
  const themeBtn = $("#themeToggle");

  function readStoredTheme() {
    try { return localStorage.getItem("hoc-theme"); } catch (e) { return null; }
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
     3. Mobile menu
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
     4. Reveal on scroll
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
     5. Hand-drawn SVG line "draw in" effect
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
     6. Scroll-driven UI: progress bar, sticky nav, active link,
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
     7. Price count-up (₹50,000)
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
