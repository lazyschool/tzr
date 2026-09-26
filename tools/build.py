# -*- coding: utf-8 -*-
"""Generate the case-study and article pages.

    python tools/build.py          # from the repository root

The site itself has no build step: this writes plain HTML files that are
committed and served as-is. The generator exists only so that thirteen pages
share one header, one footer and one set of styles instead of drifting.

After running this, run tools/csp.py to refresh the inline-script hashes.
"""
import io
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from content import CASE_STUDIES, ARTICLES, PRIVACY, ARTICLE_TAGS  # noqa: E402
from mocks import mock_for  # noqa: E402
import nav  # noqa: E402

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SITE = "https://tavzuran.com"

# The line drawings reused from the home page's project cards.
THUMBS = {
    "a": '<rect x="72" y="16" width="56" height="118" rx="10"/><path d="M92 26h16"/>'
         '<rect x="82" y="40" width="36" height="20" rx="5"/>'
         '<path d="M82 70h36M82 80h24M82 90h30"/>'
         '<rect x="82" y="104" width="36" height="14" rx="7"/>',
    "b": '<rect x="26" y="24" width="148" height="102" rx="8"/><path d="M26 44h148"/>'
         '<path d="M40 60h40M40 72h56M40 84h32"/>'
         '<rect x="112" y="60" width="48" height="34" rx="6"/>'
         '<rect x="40" y="98" width="40" height="12" rx="6"/>',
    "c": '<rect x="34" y="30" width="132" height="90" rx="8"/><path d="M34 52h132"/>'
         '<circle cx="70" cy="86" r="18"/><path d="M70 68v18l12 8"/>'
         '<path d="M104 74h50M104 88h50M104 102h30"/>',
}

BRAND_SVG = (
    '<svg viewBox="0 0 196 174" fill="currentColor" aria-hidden="true"><path d="M76.69 164.78 L74.31 162.97 L72.28 161.30 L70.59 159.77 L69.25 158.38 L68.25 157.12 L67.19 155.61 L66.06 153.83 L64.88 151.78 L63.62 149.47 L62.61 147.34 L61.83 145.41 L61.28 143.66 L60.97 142.09 L60.80 139.25 L60.77 135.12 L60.88 129.72 L61.12 123.03 L61.97 114.31 L63.41 103.56 L65.44 90.78 L68.06 75.97 L69.94 64.78 L71.06 57.22 L71.44 53.28 L71.06 52.97 L70.55 52.72 L69.89 52.53 L69.09 52.41 L68.16 52.34 L63.44 52.30 L54.94 52.27 L42.66 52.25 L26.59 52.25 L14.45 52.06 L6.23 51.69 L1.94 51.12 L1.56 50.38 L1.34 49.14 L1.28 47.42 L1.38 45.22 L1.62 42.53 L1.98 40.00 L2.45 37.62 L3.03 35.41 L3.72 33.34 L4.55 31.20 L5.52 28.98 L6.62 26.69 L7.88 24.31 L9.16 22.09 L10.47 20.03 L11.81 18.12 L13.19 16.38 L14.61 14.75 L16.08 13.25 L17.59 11.88 L19.16 10.62 L20.72 9.48 L22.28 8.45 L23.84 7.53 L25.41 6.72 L27.27 5.91 L29.42 5.09 L31.88 4.28 L34.62 3.47 L40.27 2.81 L48.80 2.31 L60.22 1.97 L74.53 1.78 L85.42 1.69 L92.89 1.69 L96.94 1.78 L97.56 1.97 L98.02 2.20 L98.30 2.48 L98.41 2.81 L98.34 3.19 L97.88 3.80 L97.00 4.64 L95.72 5.72 L94.03 7.03 L92.38 8.48 L90.75 10.08 L89.16 11.81 L87.59 13.69 L86.22 15.47 L85.03 17.16 L84.03 18.75 L83.22 20.25 L82.53 21.88 L81.97 23.62 L81.53 25.50 L81.22 27.50 L81.39 28.48 L82.05 28.45 L83.19 27.41 L84.81 25.34 L86.62 23.28 L88.62 21.22 L90.81 19.16 L93.19 17.09 L95.64 15.16 L98.17 13.34 L100.78 11.66 L103.47 10.09 L106.31 8.64 L109.31 7.30 L112.47 6.06 L115.78 4.94 L118.94 4.00 L121.94 3.25 L124.78 2.69 L127.47 2.31 L133.23 2.03 L142.08 1.84 L154.00 1.75 L169.00 1.75 L180.45 1.89 L188.36 2.17 L192.72 2.59 L193.53 3.16 L194.03 4.34 L194.22 6.16 L194.09 8.59 L193.66 11.66 L193.00 14.81 L192.12 18.06 L191.03 21.41 L189.72 24.84 L188.33 28.02 L186.86 30.92 L185.31 33.56 L183.69 35.94 L181.94 38.17 L180.06 40.27 L178.06 42.22 L175.94 44.03 L173.31 45.73 L170.19 47.33 L166.56 48.81 L162.44 50.19 L158.00 51.25 L153.25 52.00 L148.19 52.44 L142.81 52.56 L138.25 52.73 L134.50 52.95 L131.56 53.22 L129.44 53.53 L127.73 53.86 L126.45 54.20 L125.59 54.56 L125.16 54.94 L123.55 62.44 L120.77 77.06 L116.81 98.81 L111.69 127.69 L107.67 149.48 L104.77 164.20 L102.97 171.84 L102.28 172.41 L101.31 172.81 L100.06 173.06 L98.53 173.16 L96.72 173.09 L94.50 172.72 L91.88 172.03 L88.84 171.03 L85.41 169.72 L82.83 168.72 L81.11 168.03 L80.25 167.66 L80.25 167.59 L79.66 167.09 L78.47 166.16 Z"/><path d="M109.09 126.38 L108.66 127.12 L108.25 128.19 L107.88 129.56 L107.53 131.25 L107.22 133.25 L106.88 134.81 L106.50 135.94 L106.09 136.62 L105.66 136.88 L105.23 136.91 L104.83 136.72 L104.44 136.31 L104.06 135.69 L103.66 135.36 L103.22 135.33 L102.75 135.59 L102.25 136.16 L101.80 136.52 L101.39 136.67 L101.03 136.62 L100.72 136.38 L100.28 136.31 L99.72 136.44 L99.03 136.75 L98.22 137.25 L97.52 137.59 L96.92 137.78 L96.44 137.81 L96.06 137.69 L95.77 137.69 L95.55 137.81 L95.41 138.06 L95.34 138.44 L95.19 138.69 L94.94 138.81 L94.59 138.81 L94.16 138.69 L93.70 138.91 L93.23 139.47 L92.75 140.38 L92.25 141.62 L91.75 142.62 L91.25 143.38 L90.75 143.88 L90.25 144.12 L89.83 144.55 L89.48 145.14 L89.22 145.91 L89.03 146.84 L88.75 147.56 L88.38 148.06 L87.91 148.34 L87.34 148.41 L86.80 148.58 L86.27 148.86 L85.75 149.25 L85.25 149.75 L84.72 150.09 L84.16 150.28 L83.56 150.31 L82.94 150.19 L82.44 150.38 L82.06 150.88 L81.81 151.69 L81.69 152.81 L81.58 153.53 L81.48 153.84 L81.41 153.75 L81.34 153.25 L81.27 152.95 L81.17 152.86 L81.06 152.97 L80.94 153.28 L80.84 153.42 L80.78 153.39 L80.75 153.19 L80.75 152.81 L80.62 152.52 L80.38 152.30 L80.00 152.16 L79.50 152.09 L79.00 151.83 L78.50 151.36 L78.00 150.69 L77.50 149.81 L76.97 149.20 L76.41 148.86 L75.81 148.78 L75.19 148.97 L74.80 149.19 L74.64 149.44 L74.72 149.72 L75.03 150.03 L75.11 150.30 L74.95 150.52 L74.56 150.69 L73.94 150.81 L73.44 151.06 L73.06 151.44 L72.81 151.94 L72.69 152.56 L72.28 152.81 L71.59 152.69 L70.62 152.19 L69.38 151.31 L68.30 150.36 L67.39 149.33 L66.66 148.22 L66.09 147.03 L65.55 145.53 L65.02 143.72 L64.50 141.59 L64.00 139.16 L63.64 136.78 L63.42 134.47 L63.34 132.22 L63.41 130.03 L63.52 128.00 L63.67 126.12 L63.88 124.41 L64.12 122.84 L64.41 121.52 L64.72 120.42 L65.06 119.56 L65.44 118.94 L65.78 117.67 L66.09 115.77 L66.38 113.22 L66.62 110.03 L67.03 107.34 L67.59 105.16 L68.31 103.47 L69.19 102.28 L70.00 100.98 L70.75 99.58 L71.44 98.06 L72.06 96.44 L72.77 94.95 L73.55 93.61 L74.41 92.41 L75.34 91.34 L76.23 90.08 L77.08 88.61 L77.88 86.94 L78.62 85.06 L79.34 83.55 L80.03 82.39 L80.69 81.59 L81.31 81.16 L81.84 80.59 L82.28 79.91 L82.62 79.09 L82.88 78.16 L83.33 77.33 L83.98 76.61 L84.84 76.00 L85.91 75.50 L86.73 74.88 L87.33 74.12 L87.69 73.25 L87.81 72.25 L88.44 71.19 L89.56 70.06 L91.19 68.88 L93.31 67.62 L95.02 66.45 L96.30 65.36 L97.16 64.34 L97.59 63.41 L98.19 62.67 L98.94 62.14 L99.84 61.81 L100.91 61.69 L101.77 61.52 L102.42 61.30 L102.88 61.03 L103.12 60.72 L103.33 60.31 L103.48 59.81 L103.59 59.22 L103.66 58.53 L103.38 58.14 L102.75 58.05 L101.78 58.25 L100.47 58.75 L99.52 58.72 L98.92 58.16 L98.69 57.06 L98.81 55.44 L99.03 54.16 L99.34 53.22 L99.75 52.62 L100.25 52.38 L100.81 52.19 L101.44 52.06 L102.12 52.00 L102.88 52.00 L103.56 52.19 L104.19 52.56 L104.75 53.12 L105.25 53.88 L105.80 54.48 L106.39 54.95 L107.03 55.28 L107.72 55.47 L108.88 55.42 L110.50 55.14 L112.59 54.62 L115.16 53.88 L117.30 53.36 L119.02 53.08 L120.31 53.03 L121.19 53.22 L121.05 57.83 L119.89 66.86 L117.72 80.31 L114.53 98.19 L112.14 111.61 L110.55 120.58 L109.75 125.09 L109.75 125.16 L109.64 125.39 L109.42 125.80 Z" opacity=".55"/></svg>'
)

MAILTO = ("mailto:adil@tavzuran.com"
          "?subject=Free%20call%20request%20-%20Tavzuran")
INSTAGRAM = "https://instagram.com/tavzuran"

# Both inline scripts are byte-identical to the ones in index.html, so the
# CSP hashes computed for that page cover these pages too.
HTTPS_SCRIPT = '''<script>
/* Send visitors to HTTPS. GitHub Pages' own "Enforce HTTPS" does this at the
   server level; this is the belt-and-braces version and is harmless once that
   setting is on (GitHub redirects first, so this never runs). Skipped for
   localhost and for opening the file directly from disk. */
(function () {
  var h = location.hostname;
  if (location.protocol === "http:" && h !== "localhost" && h !== "127.0.0.1") {
    location.replace("https://" + location.host + location.pathname + location.search + location.hash);
  }
})();
</script>'''

BOOT_SCRIPT = '''<script>
(function () {
  var d = document.documentElement, t = null, p = null;
  try {
    t = localStorage.getItem("tavz-theme");
    p = localStorage.getItem("tavz-palette");
  } catch (e) {}
  // never trust stored values verbatim
  if (t !== "dark" && t !== "light") t = null;
  if (["blue", "green", "slate", "ocean", "rainbow"].indexOf(p) === -1) p = "green";
  d.classList.add("js");
  d.setAttribute("data-theme", t || "light");
  d.setAttribute("data-palette", p);
})();
</script>'''

BEACON = ('<!-- Cloudflare Web Analytics. Privacy-friendly and cookie-free: the numbers go\n'
          '     to the Cloudflare dashboard, not onto this page. The token is public. -->\n'
          '<script type="module" src="https://static.cloudflareinsights.com/beacon.min.js" '
          'data-cf-beacon=\'{"token": "eeb96636c3c5427fbb1f63b306a78fee"}\'></script>')

CSP = ('<meta http-equiv="Content-Security-Policy" content="default-src \'self\'; '
       'base-uri \'self\'; object-src \'none\'; form-action \'none\'; '
       'script-src \'self\' https://static.cloudflareinsights.com {hashes}; '
       'style-src \'self\' \'unsafe-inline\'; font-src \'self\'; img-src \'self\' data:; '
       'connect-src \'self\' https://cloudflareinsights.com; upgrade-insecure-requests" />')


def head(title, description, canonical, jsonld):
    """The <head> for a page one directory below the site root."""
    return u'''<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8" />

<!--
  Content Security Policy. GitHub Pages cannot send real headers, so this is
  the meta form. The hashes cover the inline scripts below and are generated by
  tools/csp.py — regenerate them if you edit any inline script.
-->
{csp}
{https}
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover" />
<meta name="referrer" content="strict-origin-when-cross-origin" />
<meta name="theme-color" content="#f6fbf8" />

<title>{title}</title>
<meta name="description" content="{description}" />
<meta name="author" content="Adil — Tavzuran" />
<link rel="canonical" href="{canonical}" />

<meta property="og:type" content="article" />
<meta property="og:site_name" content="Tavzuran" />
<meta property="og:title" content="{title}" />
<meta property="og:description" content="{description}" />
<meta property="og:url" content="{canonical}" />
<meta property="og:image" content="{site}/assets/og-image.svg" />
<meta name="twitter:card" content="summary_large_image" />
<meta name="twitter:title" content="{title}" />
<meta name="twitter:description" content="{description}" />
<meta name="twitter:image" content="{site}/assets/og-image.svg" />

<link rel="icon" href="../assets/icon.png" type="image/png" sizes="192x192" />
<link rel="apple-touch-icon" href="../assets/icon.png" />

<link rel="preload" href="../assets/fonts/inter-latin.woff2" as="font" type="font/woff2" crossorigin />
<link rel="preload" href="../assets/fonts/bricolage-grotesque-latin.woff2" as="font" type="font/woff2" crossorigin />
<link rel="stylesheet" href="../style.css" />

<!-- Tiny bootstrap: marks that JS is on and applies the saved theme before the
     first paint, so dark-mode users never see a flash of light. -->
{boot}

<script type="application/ld+json">
{jsonld}
</script>
</head>
'''.format(csp=CSP.format(hashes="{hashes}"), https=HTTPS_SCRIPT, boot=BOOT_SCRIPT,
           title=title, description=description, canonical=canonical,
           site=SITE, jsonld=jsonld)


def chrome_open(active):
    """Header, translation notice and mobile menu. `active` marks the nav item."""
    return u'''<body>
<a class="skip-link" href="#main">Skip to content</a>
<div class="progress" aria-hidden="true"><span id="progressBar"></span></div>

<header class="nav" id="nav">
  <div class="container nav__inner">
    <a class="brand" href="../index.html" aria-label="Tavzuran home">
      <span class="brand__mark" aria-hidden="true">{brand}</span>
      <span class="brand__text">Tavzuran</span>
    </a>

{primary}

    <div class="nav__actions">
      <div class="lang">
        <svg class="lang__globe" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" aria-hidden="true"><circle cx="12" cy="12" r="9"/><path d="M3 12h18M12 3c2.6 2.7 4 5.8 4 9s-1.4 6.3-4 9c-2.6-2.7-4-5.8-4-9s1.4-6.3 4-9Z"/></svg>
        <select class="lang__select" id="langSelect" aria-label="Language"></select>
        <svg class="lang__caret" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="m6 9 6 6 6-6"/></svg>
      </div>
      <div class="appear">
        <button class="icon-btn" id="appearBtn" type="button" aria-label="Switch colour theme"
                aria-expanded="false" aria-haspopup="true" aria-controls="appearPanel">
          <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.9" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">
            <path d="M12 3a9 9 0 1 0 0 18c1 0 1.7-.8 1.7-1.7 0-.5-.2-.9-.5-1.2-.3-.3-.5-.7-.5-1.1 0-.9.8-1.7 1.7-1.7H16a5 5 0 0 0 5-5c0-4-4-7.3-9-7.3Z"/>
            <circle cx="7.6" cy="11.6" r="1.1" fill="currentColor" stroke="none"/>
            <circle cx="11" cy="7.4" r="1.1" fill="currentColor" stroke="none"/>
            <circle cx="16" cy="9" r="1.1" fill="currentColor" stroke="none"/>
          </svg>
        </button>

        <div class="appear__panel" id="appearPanel" hidden>
          <div class="appear__row" role="group" aria-label="Switch colour theme">
            <button type="button" class="appear__mode" data-mode="light" aria-label="Light">
              <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" aria-hidden="true"><circle cx="12" cy="12" r="4.2"/><path d="M12 2.6v2.2M12 19.2v2.2M2.6 12h2.2M19.2 12h2.2M5.3 5.3l1.6 1.6M17.1 17.1l1.6 1.6M18.7 5.3l-1.6 1.6M6.9 17.1l-1.6 1.6"/></svg>
            </button>
            <button type="button" class="appear__mode" data-mode="dark" aria-label="Dark">
              <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M20 14.2A8.4 8.4 0 0 1 9.8 4a8.6 8.6 0 1 0 10.2 10.2Z"/></svg>
            </button>
            <button type="button" class="appear__mode" data-mode="system" aria-label="System">
              <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><rect x="3" y="4.5" width="18" height="13" rx="2.5"/><path d="M9 21h6M12 17.5V21"/></svg>
            </button>
          </div>

          <div class="appear__row appear__row--swatches" role="group" aria-label="Colour">
            <button type="button" class="appear__sw" data-palette="blue" aria-label="Blue"><i style="background:#0f6ccc"></i></button>
            <button type="button" class="appear__sw" data-palette="green" aria-label="Green"><i style="background:#12784a"></i></button>
            <button type="button" class="appear__sw" data-palette="slate" aria-label="Slate"><i style="background:#445468"></i></button>
            <button type="button" class="appear__sw" data-palette="ocean" aria-label="Ocean"><i style="background:linear-gradient(135deg,#0b6a92,#38bdf8)"></i></button>
            <button type="button" class="appear__sw" data-palette="rainbow" aria-label="Rainbow"><i style="background:linear-gradient(100deg,#2563eb,#7028c8 34%,#c026d3 66%,#db2777)"></i></button>
          </div>
        </div>
      </div>
      <a class="btn btn--primary btn--sm nav__cta" data-link="call" href="{mailto}">Free Call</a>
      <button class="burger" id="burger" type="button" aria-label="Open menu" aria-expanded="false" aria-controls="mobileMenu">
        <span></span><span></span><span></span>
      </button>
    </div>
  </div>
</header>

<!-- Machine-translation notice (only shown when a translation is active) -->
<div class="tnote" id="transNote" hidden>
  <div class="container tnote__inner">
    <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M12 3.5 21 20H3l9-16.5Z"/><path d="M12 10v4M12 17h.01"/></svg>
    <p id="transNoteText"></p>
    <button type="button" id="transNoteLink" class="tnote__link"></button>
    <button type="button" id="transNoteOk" class="tnote__ok"></button>
  </div>
</div>

{mobilemenu}
    <div class="menu__cta">
      <a class="btn btn--primary btn--block" data-link="call" href="{mailto}">Book a Free Call</a>
      <a class="btn btn--ghost btn--block" data-link="instagram" href="{ig}">DM @tavzuran</a>
    </div>
  </nav>
</div>

<main id="main">
'''.format(brand=BRAND_SVG, mailto=MAILTO, ig=INSTAGRAM,
           primary=nav.primary("../", active),
           mobilemenu=nav.mobile("../"))


CHROME_CLOSE = u'''</main>

<footer class="footer">
  <div class="container footer__inner">
    <div class="footer__brand">
      <a class="brand" href="../index.html" aria-label="Tavzuran home">
        <span class="brand__mark" aria-hidden="true">{brand}</span>
        <span class="brand__text">Tavzuran</span>
      </a>
      <p class="footer__tag">Apps • Websites • Software</p>
    </div>

    <nav class="footer__nav" aria-label="Footer">
      <a href="../index.html#services">Services</a>
      <a href="../index.html#build">Website &amp; App ₹20,000</a>
      <a href="../case-studies/index.html">Case Studies</a>
      <a href="../articles/index.html">Articles</a>
      <a href="../index.html#about">About</a>
      <a href="../index.html#contact">Contact</a>
      <a href="../privacy/index.html">Privacy</a>
    </nav>

    <div class="footer__social">
      <a class="footer__ig" data-link="instagram" href="{ig}">
        <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" aria-hidden="true"><rect x="3" y="3" width="18" height="18" rx="5.5"/><circle cx="12" cy="12" r="4.2"/><path d="M17.4 6.6h.01"/></svg>
        @tavzuran
      </a>
    </div>
  </div>
  <div class="container footer__bottom">
    <p>© 2026 Tavzuran. All rights reserved.</p>
    <p class="footer__made">Built by humans, in code. <span aria-hidden="true">✏️</span></p>
  </div>
</footer>

<div class="mobile-bar" id="mobileBar">
  <a class="btn btn--primary btn--block" data-link="call" href="{mailto}">Book a Free Call</a>
  <a class="mobile-bar__ig" data-link="instagram" href="{ig}" aria-label="DM us on Instagram">
    <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" aria-hidden="true"><rect x="3" y="3" width="18" height="18" rx="5.5"/><circle cx="12" cy="12" r="4.2"/><path d="M17.4 6.6h.01"/></svg>
  </a>
</div>

<script src="../i18n.js" defer></script>
<script src="../script.js" defer></script>

{beacon}
</body>
</html>
'''.format(brand=BRAND_SVG, mailto=MAILTO, ig=INSTAGRAM, beacon=BEACON)


def cta_block(title, sub):
    return u'''<section class="cta">
  <div class="container cta__inner">
    <h2 class="cta__title">{title}</h2>
    <p class="cta__sub">{sub}</p>
    <div class="cta__actions">
      <a class="btn btn--primary btn--lg" data-link="call" href="{mailto}">Book a FREE Call</a>
      <a class="btn btn--outline btn--lg" data-link="instagram" href="{ig}">DM @tavzuran</a>
    </div>
    <p class="cta__note">Free 20-min idea call · No obligation</p>
  </div>
</section>
'''.format(title=title, sub=sub, mailto=MAILTO, ig=INSTAGRAM)


def breadcrumb(section, section_url, current):
    return u'''  <nav class="crumb" aria-label="Breadcrumb">
    <a href="../index.html">Home</a>
    <span aria-hidden="true">/</span>
    <a href="{url}">{section}</a>
    <span aria-hidden="true">/</span>
    <span aria-current="page">{current}</span>
  </nav>
'''.format(section=section, url=section_url, current=current)


# --------------------------------------------------------------------------
# case studies
# --------------------------------------------------------------------------

def page_hero(eyebrow, title, lead, crumbs, chips="", meta="", actions="", aside=""):
    """The banner band every sub-page opens with.

    It carries the same grid-and-blob backdrop as the home page hero, so a
    sub-page reads as part of the same site rather than a bolted-on blog.
    """
    split = " phero--split" if aside else ""
    return u'''<section class="phero{split}">
  <div class="phero__bg" aria-hidden="true">
    <span class="grid-fade"></span>
    <span class="blob blob--1"></span>
    <span class="blob blob--2"></span>
  </div>
  <div class="container phero__inner">
{crumbs}
    <div class="phero__grid">
      <div>
        <p class="eyebrow reveal" data-reveal><span class="eyebrow__dot" aria-hidden="true"></span>{eyebrow}</p>
{chips}
        <h1 class="phero__title reveal" data-reveal style="--d:.05s">{title}</h1>
        <p class="phero__lead reveal" data-reveal style="--d:.1s">{lead}</p>
{meta}
{actions}
      </div>
{aside}
    </div>
  </div>
</section>
'''.format(split=split, crumbs=crumbs, eyebrow=eyebrow, chips=chips, title=title, lead=lead,
           meta=meta, actions=actions, aside=aside)


def band(inner, alt=False, extra="", ident=""):
    """One full-width section. Alternating backgrounds give the page its rhythm."""
    classes = "section section--alt" if alt else "section"
    if extra:
        classes += " " + extra
    return u'<section class="%s"%s>\n  <div class="container">\n%s  </div>\n</section>\n\n' % (
        classes, (' id="%s"' % ident) if ident else "", inner)


def band_head(eyebrow, title, sub=""):
    out = u'''    <div class="sec-head">
      <p class="eyebrow reveal" data-reveal><span class="eyebrow__dot" aria-hidden="true"></span>{eyebrow}</p>
      <h2 class="sec-title reveal" data-reveal style="--d:.05s">{title}</h2>
'''.format(eyebrow=eyebrow, title=title)
    if sub:
        out += u'      <p class="sec-sub reveal" data-reveal style="--d:.1s">%s</p>\n' % sub
    return out + u'    </div>\n\n'


# --------------------------------------------------------------------------
# case studies
# --------------------------------------------------------------------------

def case_study_page(cs, others):
    plain = cs["title"].replace("&amp;", "and")
    jsonld = u'''{{
  "@context": "https://schema.org",
  "@type": "CreativeWork",
  "name": "{title}",
  "abstract": "{summary}",
  "creator": {{ "@type": "Organization", "name": "Tavzuran" }},
  "url": "{site}/case-studies/{slug}.html",
  "isAccessibleForFree": true,
  "disambiguatingDescription": "Example build. Tavzuran is a new studio; this describes a project the studio is set up to deliver, not completed client work."
}}'''.format(title=plain, summary=cs["summary"], site=SITE, slug=cs["slug"])

    out = [head("%s — Case Study | Tavzuran" % cs["title"],
                cs["summary"],
                "%s/case-studies/%s.html" % (SITE, cs["slug"]),
                jsonld),
           chrome_open("case-studies")]

    # ---- banner -----------------------------------------------------------
    crumbs = breadcrumb("Case Studies", "../case-studies/index.html", cs["title"])
    chips = ('    <span class="chips reveal" data-reveal>'
             '<span class="proj__flag">Example build</span>'
             '<span class="proj__cat">%s</span></span>\n' % cs["category"])
    actions = u'''    <div class="phero__actions reveal" data-reveal style="--d:.16s">
      <a class="btn btn--primary btn--lg" data-link="call" href="{mailto}">Build something like this</a>
      <a class="btn btn--outline btn--lg" href="../case-studies/index.html">All case studies</a>
    </div>
'''.format(mailto=MAILTO)
    aside = ('      <div class="phero__art reveal" data-reveal style="--d:.2s">'
             '%s</div>\n' % mock_for(cs["slug"]))
    out.append(page_hero("CASE STUDY", cs["title"], cs["summary"],
                         crumbs, chips=chips, actions=actions, aside=aside))

    # ---- at a glance ------------------------------------------------------
    glance = ['    <dl class="glance">\n']
    for i, (label, value) in enumerate(cs["glance"]):
        glance.append(u'''      <div class="glance__item reveal" data-reveal style="--d:.{d}s">
        <dt>{label}</dt>
        <dd>{value}</dd>
      </div>
'''.format(d=(i * 6) + 4, label=label, value=value))
    glance.append('    </dl>\n\n')
    glance.append(u'''    <p class="note note--flag reveal" data-reveal><strong>This is an example build.</strong>
    Tavzuran is a new studio with no client work to show yet. This page describes
    how the project would be scoped and built — the same thinking you would get on a real
    one. Nothing here is a past client, and no number on this page is a result.</p>
''')
    glance.append(u"""    <p class="note note--price reveal" data-reveal><strong>The price follows
    the feature list.</strong> The number above buys everything scoped on this page. Take
    features out and it comes down \u2014 the shortest route to a smaller number is a shorter
    list, and deciding what to drop is what the free call is for.</p>
""")
    out.append(band("".join(glance), alt=True, extra="section--glance"))

    # ---- the situation ----------------------------------------------------
    inner = [band_head("THE SITUATION", "What's actually broken.")]
    inner.append('    <div class="split">\n      <div class="split__text">\n')
    for i, para in enumerate(cs["situation"]):
        inner.append('        <p class="reveal" data-reveal style="--d:.%ds">%s</p>\n'
                     % ((i * 6) + 4, para))
    # not .problem__list: the home page pins that class into grid column 1,
    # which would drop this list underneath the text instead of beside it
    inner.append('      </div>\n\n      <ul class="split__list">\n')
    for i, pain in enumerate(cs["pains"]):
        inner.append('        <li class="prob reveal" data-reveal style="--d:.%ds">'
                     '<span class="prob__x" aria-hidden="true">✕</span>'
                     '<h3>%s</h3></li>\n' % ((i * 6) + 6, pain))
    inner.append('      </ul>\n    </div>\n')
    out.append(band("".join(inner)))

    # ---- what we'd build --------------------------------------------------
    inner = [band_head("VERSION ONE", "What we'd build first.",
                       "Every item here earns its place by being something a real user "
                       "would miss on day one.")]
    inner.append('    <div class="cards cards--3">\n')
    for i, (name, body) in enumerate(cs["scope"]):
        inner.append(u'''      <article class="card card--service reveal" data-reveal style="--d:.{d}s">
        <span class="card__num" aria-hidden="true">{n:02d}</span>
        <h3>{name}</h3>
        <p>{body}</p>
        <span class="card__corner" aria-hidden="true"></span>
      </article>
'''.format(d=(i * 6) + 4, n=i + 1, name=name, body=body))
    inner.append('    </div>\n')
    out.append(band("".join(inner), alt=True))

    # ---- what we'd leave out ----------------------------------------------
    inner = [band_head("DELIBERATELY NOT IN V1", "What we'd leave out.",
                       "Not because these are bad ideas. Because each one is designed "
                       "better once the first version has told you something.")]
    inner.append('    <ul class="cutlist">\n')
    for i, item in enumerate(cs["excluded"]):
        inner.append('      <li class="reveal" data-reveal style="--d:.%ds">'
                     '<span class="cutlist__x" aria-hidden="true">✕</span>'
                     '<span>%s</span></li>\n' % ((i * 6) + 4, item))
    inner.append('    </ul>\n')
    out.append(band("".join(inner)))

    # ---- the stack --------------------------------------------------------
    inner = [band_head("UNDER THE HOOD", "How it's put together.")]
    inner.append('    <dl class="stack">\n')
    for i, (name, body) in enumerate(cs["stack"]):
        inner.append(u'''      <div class="stack__row reveal" data-reveal style="--d:.{d}s">
        <dt>{name}</dt>
        <dd>{body}</dd>
      </div>
'''.format(d=(i * 5) + 4, name=name, body=body))
    inner.append('    </dl>\n')
    out.append(band("".join(inner), alt=True))

    # ---- timeline ---------------------------------------------------------
    inner = [band_head("HOW IT RUNS", "Week by week.")]
    inner.append('    <ol class="timeline">\n'
                 '      <span class="tl__line" aria-hidden="true"><i></i></span>\n')
    for i, (when, what) in enumerate(cs["timeline"]):
        inner.append(u'''      <li class="tl reveal" data-reveal style="--d:.{d}s">
        <span class="tl__num">{n:02d}</span>
        <div class="tl__body">
          <h3>{when}</h3>
          <p>{what}</p>
        </div>
      </li>
'''.format(d=(i * 6) + 4, n=i + 1, when=when, what=what))
    inner.append('    </ol>\n')
    out.append(band("".join(inner)))

    # ---- the hardest part -------------------------------------------------
    hard_title, hard_paras = cs["hard"]
    inner = [band_head("THE HARD PART", hard_title,
                       "Every build has one problem that decides whether the rest "
                       "of it matters. This is that problem, written out.")]
    inner.append('    <div class="deep">\n')
    for i, para in enumerate(hard_paras):
        inner.append('      <p class="reveal" data-reveal style="--d:.%ds">%s</p>\n'
                     % ((i * 6) + 4, para))
    inner.append('    </div>\n')
    out.append(band("".join(inner)))

    # ---- what we'd ask before quoting -------------------------------------
    inner = [band_head("BEFORE A PRICE EXISTS", "What we'd ask you first.",
                       "A quote given without these answers is a guess. These are "
                       "the questions that actually move the number.")]
    inner.append('    <ol class="qlist">\n')
    for i, q in enumerate(cs["questions"]):
        inner.append('      <li class="reveal" data-reveal style="--d:.%ds">'
                     '<span class="qlist__n">%02d</span><span>%s</span></li>\n'
                     % ((i * 5) + 4, i + 1, q))
    inner.append('    </ol>\n')
    out.append(band("".join(inner), alt=True))

    # ---- how we'd know it worked ------------------------------------------
    inner = [band_head("AFTERWARDS", "How we'd know it worked.",
                       "Agreed before the build starts, so there is something to "
                       "judge it against other than whether it looks nice.")]
    inner.append('    <ul class="winlist">\n')
    for i, w in enumerate(cs["success"]):
        inner.append('      <li class="reveal" data-reveal style="--d:.%ds">'
                     '<span class="winlist__tick" aria-hidden="true">&#10003;</span>'
                     '<span>%s</span></li>\n' % ((i * 6) + 4, w))
    inner.append('    </ul>\n')
    out.append(band("".join(inner)))

    # ---- worth knowing + price -------------------------------------------
    inner = [band_head("BEFORE YOU START", "Worth knowing.")]
    inner.append(u'''    <div class="knowgrid">
      <p class="note reveal" data-reveal>{note}</p>
      <p class="note note--price reveal" data-reveal style="--d:.08s">Websites and apps start at
      <strong>₹20,000*</strong>. Final pricing depends on features and project scope.
      Third-party costs — cloud hosting, domains, external libraries, APIs, app-store
      fees and any other paid service — are billed separately and are not included.</p>
    </div>
'''.format(note=cs["note"]))
    out.append(band("".join(inner), alt=True))

    # ---- other builds -----------------------------------------------------
    inner = [band_head("KEEP LOOKING", "Other example builds.")]
    inner.append('    <div class="cards post-grid">\n')
    for i, other in enumerate(others):
        inner.append(u'''      <a class="card post-card reveal" data-reveal style="--d:.{d}s" href="{slug}.html">
        <span class="proj__cat">{cat}</span>
        <h3>{title}</h3>
        <p>{summary}</p>
        <span class="link-arrow">Read the case study <span aria-hidden="true">→</span></span>
      </a>
'''.format(d=(i * 6) + 4, slug=other["slug"], cat=other["category"],
           title=other["title"], summary=other["summary"]))
    inner.append('    </div>\n')
    out.append(band("".join(inner)))

    out.append(cta_block("Want this built for your business?",
                         "Tell us what you're thinking. We'll figure out the next step together."))
    out.append(CHROME_CLOSE)
    return "".join(out)


def case_studies_index():
    jsonld = u'''{
  "@context": "https://schema.org",
  "@type": "CollectionPage",
  "name": "Case Studies — Tavzuran",
  "description": "Example builds showing how Tavzuran scopes and ships apps, websites and custom software.",
  "url": "%s/case-studies/"
}''' % SITE

    out = [head("Case Studies — Example Builds | Tavzuran",
                "How we scope and build apps, websites, dashboards and first versions — "
                "six example builds with the scope, the stack, the timeline and "
                "what we would deliberately leave out of version one.",
                "%s/case-studies/" % SITE, jsonld),
           chrome_open("case-studies")]

    crumbs = u'''    <nav class="crumb" aria-label="Breadcrumb">
      <a href="../index.html">Home</a>
      <span aria-hidden="true">/</span>
      <span aria-current="page">Case Studies</span>
    </nav>
'''
    out.append(page_hero("WHAT WE BUILD", "Case studies",
                         "Six builds, taken apart. What the business problem is, what "
                         "version one contains, what gets cut, how it's put together "
                         "and how long it runs.", crumbs))

    inner = [u'''    <p class="note note--flag reveal" data-reveal><strong>Straight up: these are example builds.</strong>
    Tavzuran is new, so none of these are past clients and nothing here is a
    results claim. They're the products the studio is set up to ship, written out in
    the same detail you'd get on a real project. Yours would be the first on this wall.</p>

    <div class="cards post-grid">
''']
    for i, cs in enumerate(CASE_STUDIES):
        inner.append(u'''      <a class="card post-card reveal" data-reveal style="--d:.{d}s" href="{slug}.html">
        <div class="post-card__mock">{mock}</div>
        <span class="chips"><span class="proj__flag">Example build</span><span class="proj__cat">{cat}</span></span>
        <h2>{title}</h2>
        <p>{summary}</p>
        <span class="link-arrow">Read the case study <span aria-hidden="true">→</span></span>
      </a>
'''.format(d=(i * 6) + 4, slug=cs["slug"], mock=mock_for(cs["slug"], bare=True),
           cat=cs["category"], title=cs["title"], summary=cs["summary"]))
    inner.append('    </div>\n')
    out.append(band("".join(inner), alt=True))

    inner = [band_head("HOW IT WORKS", "Every one of these starts the same way.")]
    inner.append(u'''    <ol class="timeline">
      <span class="tl__line" aria-hidden="true"><i></i></span>
      <li class="tl reveal" data-reveal><span class="tl__num">01</span>
        <div class="tl__body"><h3>Tell us your idea</h3>
        <p>Book a free call and tell us what you want to build.</p></div></li>
      <li class="tl reveal" data-reveal style="--d:.08s"><span class="tl__num">02</span>
        <div class="tl__body"><h3>Plan</h3>
        <p>We define the features, scope and best technical approach.</p></div></li>
      <li class="tl reveal" data-reveal style="--d:.16s"><span class="tl__num">03</span>
        <div class="tl__body"><h3>Build</h3>
        <p>We design and develop your product.</p></div></li>
      <li class="tl reveal" data-reveal style="--d:.24s"><span class="tl__num">04</span>
        <div class="tl__body"><h3>Launch</h3>
        <p>Get it in front of real users and start growing.</p></div></li>
    </ol>
''')
    out.append(band("".join(inner)))

    out.append(cta_block("Want to be project #001?",
                         "Tell us what you're thinking. We'll figure out the next step together."))
    out.append(CHROME_CLOSE)
    return "".join(out)


def render_blocks(blocks):
    out = []
    for kind, value in blocks:
        if kind == "h2":
            out.append(u"    <h2>%s</h2>\n" % value)
        elif kind == "h3":
            out.append(u"    <h3>%s</h3>\n" % value)
        elif kind == "p":
            out.append(u"    <p>%s</p>\n" % value)
        elif kind == "quote":
            out.append(u"    <blockquote><p>%s</p></blockquote>\n" % value)
        elif kind in ("ul", "ol"):
            out.append(u"    <%s>\n" % kind)
            for item in value:
                out.append(u"      <li>%s</li>\n" % item)
            out.append(u"    </%s>\n" % kind)
    return "".join(out)


def article_page(art, others):
    jsonld = u'''{{
  "@context": "https://schema.org",
  "@type": "BlogPosting",
  "headline": "{title}",
  "description": "{summary}",
  "datePublished": "{date}",
  "author": {{ "@type": "Person", "name": "Adil" }},
  "publisher": {{ "@type": "Organization", "name": "Tavzuran" }},
  "mainEntityOfPage": "{site}/articles/{slug}.html",
  "inLanguage": "en"
}}'''.format(title=art["title"], summary=art["summary"], date=art["date"],
             site=SITE, slug=art["slug"])

    out = [head("%s | Tavzuran" % art["title"], art["summary"],
                "%s/articles/%s.html" % (SITE, art["slug"]), jsonld),
           chrome_open("articles")]

    crumbs = breadcrumb("Articles", "../articles/index.html", art["title"])
    chips = ('    <span class="chips reveal" data-reveal>'
             '<span class="proj__cat">%s</span></span>\n' % art["tag"])
    meta = u'''    <p class="phero__meta reveal" data-reveal style="--d:.14s">
      <span>By Adil</span>
      <span aria-hidden="true">·</span>
      <time datetime="{date}">{date_label}</time>
      <span aria-hidden="true">·</span>
      <span>{read}</span>
    </p>
'''.format(date=art["date"], date_label=art["date_label"], read=art["read"])
    out.append(page_hero("ARTICLE", art["title"], art["summary"],
                         crumbs, chips=chips, meta=meta))

    # The body is the one place a narrow reading column is right, so it keeps
    # its own band rather than being broken into more of them.
    out.append(u'<section class="section section--read">\n  <div class="container prose">\n')
    if art.get("caveat"):
        # version-specific detail dates fast, so say so rather than let a reader
        # act on something that moved after this was written
        out.append(
            u'    <p class="note note--flag"><strong>Written {when}.</strong> This one '
            u'touches fast-moving tooling. The tradeoffs should hold; check anything '
            u'version-specific against current documentation before relying on '
            u'it.</p>\n'.format(when=art["date_label"]))
    out.append(render_blocks(art["body"]))
    out.append(u'''  </div>
</section>

''')

    inner = [band_head("KEEP READING", "More articles.")]
    inner.append('    <div class="cards post-grid">\n')
    for i, other in enumerate(others):
        inner.append(u'''      <a class="card post-card reveal" data-reveal style="--d:.{d}s" href="{slug}.html">
        <span class="proj__cat">{tag}</span>
        <h3>{title}</h3>
        <p>{summary}</p>
        <p class="post-card__meta"><time datetime="{date}">{date_label}</time> · {read}</p>
        <span class="link-arrow">Read it <span aria-hidden="true">→</span></span>
      </a>
'''.format(d=(i * 6) + 4, slug=other["slug"], tag=other["tag"], title=other["title"],
           summary=other["summary"], date=other["date"],
           date_label=other["date_label"], read=other["read"]))
    inner.append('    </div>\n')
    out.append(band("".join(inner), alt=True))

    out.append(cta_block("Got an idea you've been sitting on?",
                         "Book a free call. Worst case, you walk away with free advice on what to build first."))
    out.append(CHROME_CLOSE)
    return "".join(out)


def privacy_page():
    """A legal page still has to render, theme and work with JS off like the rest."""
    jsonld = u'''{{
  "@context": "https://schema.org",
  "@type": "WebPage",
  "name": "Privacy Policy",
  "description": "{summary}",
  "url": "{site}/privacy/index.html",
  "dateModified": "{updated}",
  "publisher": {{ "@type": "Organization", "name": "Tavzuran" }},
  "inLanguage": "en"
}}'''.format(summary=PRIVACY["summary"], site=SITE, updated=PRIVACY["updated"])

    out = [head("Privacy Policy | Tavzuran", PRIVACY["summary"],
                "%s/privacy/index.html" % SITE, jsonld),
           chrome_open("")]

    meta = (u'    <p class="phero__meta reveal" data-reveal style="--d:.14s">\n'
            u'      <span>Last updated</span>\n'
            u'      <span aria-hidden="true">&middot;</span>\n'
            u'      <time datetime="{d}">{label}</time>\n'
            u'    </p>\n').format(d=PRIVACY["updated"], label=PRIVACY["updated_label"])
    out.append(page_hero("LEGAL", "Privacy Policy", PRIVACY["summary"], "", meta=meta))

    out.append(u'<section class="section section--read">\n  <div class="container prose">\n')
    out.append(render_blocks(PRIVACY["body"]))
    out.append(u'  </div>\n</section>\n\n')

    out.append(cta_block("Still want to talk?",
                         "Email me. Nothing on this page makes that harder."))
    out.append(CHROME_CLOSE)
    return "".join(out)


def articles_index():
    jsonld = u'''{
  "@context": "https://schema.org",
  "@type": "Blog",
  "name": "Articles — Tavzuran",
  "description": "Plain-English writing about building software: first versions, pricing, apps versus websites, and how AI actually fits into the work.",
  "url": "%s/articles/"
}''' % SITE

    out = [head("Articles — Plain-English Writing on Building Software | Tavzuran",
                "First versions, what software actually costs, apps versus websites, and how "
                "AI fits into real engineering. Written by Adil, no jargon.",
                "%s/articles/" % SITE, jsonld),
           chrome_open("articles")]

    crumbs = u'''    <nav class="crumb" aria-label="Breadcrumb">
      <a href="../index.html">Home</a>
      <span aria-hidden="true">/</span>
      <span aria-current="page">Articles</span>
    </nav>
'''
    out.append(page_hero("WRITING", "Articles",
                         "What I've learned building software for eleven years, "
                         "written for the person paying for it rather than the person "
                         "writing it.", crumbs))

    # Topic filter. Eleven articles is past the point where a flat list works,
    # and the counts tell a reader what is actually here before they click.
    chips = ['      <button type="button" class="chip is-on" data-filter="all"'
             ' aria-pressed="true">All <span class="chip__n">%d</span></button>'
             % len(ARTICLES)]
    for tag in ARTICLE_TAGS:
        n = len([a for a in ARTICLES if a["tag"] == tag])
        chips.append('      <button type="button" class="chip" data-filter="%s"'
                     ' aria-pressed="false">%s <span class="chip__n">%d</span></button>'
                     % (tag, tag, n))

    inner = ['    <div class="chips-bar" role="group" aria-label="Filter articles by topic" id="artFilter">\n',
             "\n".join(chips),
             '\n    </div>\n\n',
             '    <div class="cards post-grid" id="artGrid">\n']
    for i, art in enumerate(ARTICLES):
        inner.append(u'''      <a class="card post-card reveal" data-reveal style="--d:.{d}s" href="{slug}.html" data-tag="{tag}">
        <span class="proj__cat">{tag}</span>
        <h2>{title}</h2>
        <p>{summary}</p>
        <p class="post-card__meta"><time datetime="{date}">{date_label}</time> · {read}</p>
        <span class="link-arrow">Read it <span aria-hidden="true">→</span></span>
      </a>
'''.format(d=(i * 6) + 4, slug=art["slug"], tag=art["tag"], title=art["title"],
           summary=art["summary"], date=art["date"], date_label=art["date_label"],
           read=art["read"]))
    inner.append('    </div>\n')
    out.append(band("".join(inner), alt=True))

    out.append(cta_block("Rather just ask a person?",
                         "Book a free 20-minute call and ask whatever you like. No obligation."))
    out.append(CHROME_CLOSE)
    return "".join(out)


def write(path, text):
    full = os.path.join(ROOT, path)
    folder = os.path.dirname(full)
    if not os.path.isdir(folder):
        os.makedirs(folder)
    with io.open(full, "w", encoding="utf-8", newline="\n") as fh:
        fh.write(text)
    print("  wrote %-52s %6d bytes" % (path, len(text.encode("utf-8"))))


def offered_languages():
    """The codes the switcher actually offers, read out of i18n.js.

    A language that is commented out there renders as English, so listing it
    as an alternate would claim a translation that does not exist.
    """
    src = io.open(os.path.join(ROOT, "i18n.js"), encoding="utf-8").read()
    block = src[src.index("window.TAVZ_I18N.languages = ["):]
    block = block[:block.index("];")]
    codes = []
    for line in block.split("\n"):
        stripped = line.strip()
        if stripped.startswith("//") or "code:" not in stripped:
            continue
        code = stripped.split("code:", 1)[1].split('"')[1]
        if code not in codes:
            codes.append(code)
    return codes


def alternates(indent, close):
    codes = offered_languages()
    rows = ['%s<%s hreflang="en" href="%s/"%s' % (indent, TAG, SITE, close)]
    for code in sorted(c for c in codes if c != "en"):
        rows.append('%s<%s hreflang="%s" href="%s/?lang=%s"%s'
                    % (indent, TAG, code, SITE, code, close))
    rows.append('%s<%s hreflang="x-default" href="%s/"%s' % (indent, TAG, SITE, close))
    return rows, codes


def build_sitemap():
    global TAG
    TAG = 'xhtml:link rel="alternate"'
    alts, codes = alternates("    ", "/>")

    out = ['<?xml version="1.0" encoding="UTF-8"?>',
           '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9" '
           'xmlns:xhtml="http://www.w3.org/1999/xhtml">',
           '  <url>',
           '    <loc>%s/</loc>' % SITE,
           '    <changefreq>monthly</changefreq>',
           '    <priority>1.0</priority>']
    out += alts
    out.append('  </url>')

    for path in ("case-studies/", "articles/"):
        out += ['  <url>',
                '    <loc>%s/%s</loc>' % (SITE, path),
                '    <changefreq>monthly</changefreq>',
                '    <priority>0.8</priority>',
                '  </url>']
    out += ['  <url>',
            '    <loc>%s/privacy/index.html</loc>' % SITE,
            '    <changefreq>yearly</changefreq>',
            '    <priority>0.3</priority>',
            '  </url>']

    for cs in CASE_STUDIES:
        out += ['  <url>',
                '    <loc>%s/case-studies/%s.html</loc>' % (SITE, cs["slug"]),
                '    <priority>0.7</priority>',
                '  </url>']
    for art in ARTICLES:
        out += ['  <url>',
                '    <loc>%s/articles/%s.html</loc>' % (SITE, art["slug"]),
                '    <lastmod>%s</lastmod>' % art["date"],
                '    <priority>0.7</priority>',
                '  </url>']
    out.append('</urlset>')
    write("sitemap.xml", "\n".join(out) + "\n")
    write("robots.txt", "User-agent: *\nAllow: /\n\nSitemap: %s/sitemap.xml\n" % SITE)


def build_nav():
    """Rewrite index.html's nav from nav.py, so the home page and the generated
    pages can never drift apart."""
    path = os.path.join(ROOT, "index.html")
    html = io.open(path, encoding="utf-8").read()

    start = html.index('    <nav class="nav__links" aria-label="Primary">')
    end = html.index("</nav>", start) + len("</nav>")
    html = html[:start] + nav.primary("") + html[end:]

    start = html.index('<div class="menu" id="mobileMenu" hidden>')
    end = html.index('    <div class="menu__cta">', start)
    html = html[:start] + nav.mobile("") + "\n" + html[end:]

    io.open(path, "w", encoding="utf-8", newline="").write(html)
    print("  index.html nav rebuilt")


PORTFOLIO_BANNER = u"""    <!--
      ========================= PORTFOLIO DATA =========================
      GENERATED by tools/build.py from CASE_STUDIES in tools/content.py.
      Hand edits here are overwritten on the next build.

      Every card is one case study: the link, the category chip, the title,
      the one-line summary and the stylised screen all come from the same
      entry, so a card can never point at the wrong page or show a stale
      category. To change a card, edit tools/content.py and re-run:

          python tools/build.py && python tools/csp.py

      These are EXAMPLE builds, not client projects. When one becomes real
      client work, drop the "Example build" chip by removing it below in
      portfolio_cards(), and update the honest note in the section heading
      above (which is still hand-written).
      ==================================================================
    -->
"""


def portfolio_cards():
    """One card per case study, in content.py order."""
    out = []
    for i, cs in enumerate(CASE_STUDIES):
        out.append(u'''      <a class="card proj reveal" data-reveal style="--d:.{d}s" href="case-studies/{slug}.html">
        <div class="proj__thumb" aria-hidden="true">{mock}</div>
        <div class="proj__body">
          <span class="chips"><span class="proj__flag">Example build</span><span class="proj__cat">{cat}</span></span>
          <h3>{title}</h3>
          <p>{summary}</p>
          <span class="link-arrow">Read the case study <span aria-hidden="true">\u2192</span></span>
        </div>
      </a>
'''.format(d=("04", "10", "16")[i % 3], slug=cs["slug"],
           mock=mock_for(cs["slug"], bare=True), cat=cs["category"],
           title=cs["title"], summary=cs["summary"]))
    return "".join(out)


def build_portfolio():
    """Rewrite the home page's portfolio grid from content.py."""
    path = os.path.join(ROOT, "index.html")
    html = io.open(path, encoding="utf-8").read()

    start = html.index("    <!--\n      ========================= PORTFOLIO DATA")
    end = html.index("    <!-- ======================= END PORTFOLIO DATA")
    grid = (u'    <div class="cards cards--3 work__grid">\n'
            + portfolio_cards() + u'    </div>\n')

    io.open(path, "w", encoding="utf-8", newline="").write(
        html[:start] + PORTFOLIO_BANNER + grid + html[end:])
    print("  index.html portfolio %d card(s)" % len(CASE_STUDIES))


def build_hreflang():
    """Keep index.html's alternate-language links to the languages on offer."""
    global TAG
    TAG = 'link rel="alternate"'
    rows, codes = alternates("", " />")

    path = os.path.join(ROOT, "index.html")
    html = io.open(path, encoding="utf-8").read()
    start = html.index('<link rel="alternate" hreflang="en"')
    end = html.index("/>", html.index('hreflang="x-default"')) + 2
    io.open(path, "w", encoding="utf-8", newline="").write(
        html[:start] + "\n".join(rows) + html[end:])
    print("  index.html hreflang %d language(s)" % len(codes))


def main():
    write("case-studies/index.html", case_studies_index())
    for i, cs in enumerate(CASE_STUDIES):
        others = CASE_STUDIES[i + 1:] + CASE_STUDIES[:i]
        write("case-studies/%s.html" % cs["slug"], case_study_page(cs, others[:3]))

    write("articles/index.html", articles_index())
    for i, art in enumerate(ARTICLES):
        others = ARTICLES[i + 1:] + ARTICLES[:i]
        write("articles/%s.html" % art["slug"], article_page(art, others[:3]))

    write("privacy/index.html", privacy_page())

    build_sitemap()
    build_hreflang()
    build_nav()
    build_portfolio()
    print("\n%d pages generated. Now run: python tools/csp.py" %
          (2 + len(CASE_STUDIES) + len(ARTICLES)))


if __name__ == "__main__":
    main()
