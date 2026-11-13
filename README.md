# Tavzuran — Website

Static marketing site for **Tavzuran** — apps, websites, MVPs and custom software.
Plain HTML, CSS and vanilla JavaScript. No build step, no framework, no server, no paid services.

```
tavzuran/
├── index.html        all page content
├── style.css         all styling (mobile-first)
├── script.js         all behaviour + YOUR BUSINESS INFO at the top
├── i18n.js           language list + translation disclaimer (small, always loaded)
├── .well-known/
│   └── security.txt  how to report a problem with the site
├── assets/
│   ├── fonts/        self-hosted webfonts (no third-party requests) + licences
│   ├── icon.png      browser tab icon
│   ├── og-image.png  social share preview (1200×630)
│   ├── i18n/         20 dictionaries — loaded only when chosen
│   └── README.md     how to add project images
├── tools/            build.py regenerates the case studies, articles and nav
├── LICENSES.md       every third-party asset, its licence and where it came from
├── .nojekyll         tells GitHub Pages to serve files as-is
├── robots.txt
└── sitemap.xml
```

---

## 1. Run it locally

**Easiest way:** double-click `index.html`. It opens in your browser and everything works —
animations, menu, dark mode, all links.

**Optional (closer to the real thing):** run a tiny local server so the URL is `http://localhost`
instead of `file://`.

```bash
# Python (already installed on most machines)
python -m http.server 8000
# then open http://localhost:8000

# or Node
npx serve .
```

Any change to the files shows up on a browser refresh — there is nothing to build or compile.

---

## 2. Before you publish — what to edit

### a) Your contact details → `script.js`

Open `script.js`. The first block is the only place contact info lives — Instagram and email are
already filled in, so there is nothing you must change before publishing:

```js
const CONFIG = {
  instagram: "tavzuran",
  email:     "adil@tavzuran.com",
  emailSubject: "Project enquiry from tavzuran.com",
  callSubject: "Free call request - Tavzuran",
  callBody: [ ...the pre-written email, one line per array entry... ],
  bookingUrl: ""                          // ← optional Cal.com / Calendly link
};
```

Every **Book a Free Call**, **DM** and **Email** button on the page reads from this.
There are two contact channels: Instagram and email. WhatsApp was removed.

### How "Book a Free Call" works

All ten of those buttons open the visitor's email app with a message already written to
`adil@tavzuran.com`, asking for their name, what they want to build, rough budget, a good time
to call, and whether they want it on phone, WhatsApp, Zoom or Google Meet. Edit `callBody` to change
the wording — each array entry is one line.

If you later sign up for a scheduler (Cal.com, Calendly), put its link in `bookingUrl` and every one
of those buttons switches to the booking page instead. Nothing else needs touching.

The email template asks how they'd like the call to happen — phone, WhatsApp, Zoom or Google Meet —
so you can still take calls on WhatsApp without publishing your number on the site.

### b) Portfolio projects → `index.html`

Search the file for `PORTFOLIO DATA`. Six example projects sit between that marker and
`END PORTFOLIO DATA`. Each one is a self-contained block — edit the category, name and description,
duplicate or delete blocks freely:

```html
<span class="proj__cat">Mobile App</span>
<h3>Restaurant Ordering App</h3>
<p>Menu, cart, live order tracking and a simple kitchen dashboard.</p>
```

To use a real screenshot instead of the drawn thumbnail, see `assets/README.md`.

### c) Delivered client work → `tools/build.py`

Real, delivered projects live in `CLIENT_WORK` near the top of `tools/build.py`: name, live URL,
category, a one-line summary and which drawn screen to show beside it. Each one appears as a wide
"Delivered" panel ahead of the example builds, on the home page and on the case-studies index. Add an
entry and run `python tools/build.py && python tools/csp.py`. If you change a summary, add the new
wording to the four active dictionaries in `assets/i18n/`, or it shows in English.

### d) Reviews → `index.html`

Search for `FAMILY REVIEWS`. The section is headed "No client reviews yet. So I asked my family."
and carries three real (and funny) quotes from Adil's mother, father and brother. When the first
client review arrives, replace a `<blockquote>`, `.t__name` and `.t__role`, swap the `Family` chip,
and update the heading.

---

## 2b. Languages

The site ships in **21 languages**. English is the source and the authentic version; every other
language is translated by AI.

| | | | |
|---|---|---|---|
| English (source) | العربية | Български | Deutsch |
| Ελληνικά | Español | Français | हिन्दी |
| Bahasa Indonesia | Italiano | 日本語 | Қазақша |
| 한국어 | Bahasa Melayu | Norsk | Português |
| Русский | Svenska | தமிழ் | ไทย |
| Tiếng Việt | | | |

Whenever a translation is active, a notice under the header says — in that language — that the page
was translated by AI, apologises for any mistakes, and points to English as the authentic version.
It carries two buttons: **view in English**, and an **Okay** button that dismisses it.

Dismissal is remembered *per language* (`tavz-note-ok` in `localStorage`), so a reader who accepts the
Japanese notice never sees it again in Japanese, but still gets the disclosure once if they switch to
another translation. Each language's wording lives in the `disclaimer` map in `i18n.js` as
`text` / `link` / `ok`.

**How it works.** There is only one `index.html`. On load, `script.js` snapshots every text node and
translatable attribute on the page, then swaps them against the chosen language's dictionary.
Switching back to English restores the original text, so English can never drift.

Dictionaries live in `assets/i18n/<code>.js` and are **downloaded only when that language is
selected** — an English visitor fetches none of them. Only the small `i18n.js` (language list plus
the disclaimer wording) loads up front.

**Choosing a language:** the globe control in the header (a dropdown on desktop, a compact globe
button on phones). The choice is remembered per visitor and reflected in the URL as `?lang=de`, so a
translated page can be shared or linked directly. English stays the default — the browser's language
is deliberately *not* auto-detected, because the English version is the authoritative one.

**Arabic runs right-to-left.** Setting `rtl: true` on a language in `i18n.js` flips
`document.dir`; the `9b. RIGHT-TO-LEFT` block in `style.css` mirrors the pieces that are pinned with
physical left/right values and flips the arrows.

### Editing or adding a translation

Open `assets/i18n/<code>.js` (e.g. `assets/i18n/de.js`). Each is a plain map of
`"English text": "translation"`:

```js
window.TAVZ_I18N["de"] = {
  "Have an idea?": "Sie haben eine Idee?",
  ...
};
```

The key must match the English on the page **exactly** — same punctuation, same dashes. Anything
without an entry simply stays in English, which is why brand names, `MVP`, `SaaS`, `AWS`, the
Instagram handle and the email address are deliberately absent.

**If you change English wording on the page, update the matching key in all 20 files**, or that line
quietly falls back to English. To add a language: add it to `languages` in `i18n.js`, add a
`disclaimer` and a `selectorLabel` entry there, drop a new `assets/i18n/<code>.js` beside the others,
and add an `hreflang` tag in `index.html` plus an entry in `sitemap.xml`.

**Always re-check the layout after adding a language.** Translated strings run much longer than the
English they replace, and that is where the breakage happens — German broke the header nav, Tamil's
headline word is wider than a phone screen (it gets a smaller heading size), and Tamil's CTA label is
long enough that the duplicate header button is hidden for that language. Run:

```bash
node ~/.claude/skills/static-site-ship/scripts/page-audit.js "http://localhost:8000/index.html" 375,390,1280 ./shots "?lang=xx"
```

---

## 3. Deploy to GitHub Pages

### Option A — Push from the command line

This repo is already wired up: the code lives at
`git@github.com:lazyschool/tzr.git` on the `master` branch.
(The older `lazyschool/humansofcoding` repo still holds the pre-rename history and is
what serves humansofcoding.com until the domain move is finished.)

1. Push:

```bash
git add .
git commit -m "Your message"
git push
```

2. On GitHub: **Settings → Pages → Build and deployment**
   - Source: **Deploy from a branch**
   - Branch: **master**, folder: **/ (root)** → **Save**

3. Wait ~1 minute. The site goes live at:
   **https://tavzuran.com/**

`index.html` must stay in the repository root — Pages serves it as the home page.
`.nojekyll` is already included so GitHub serves every file untouched.

### Option B — Drag and drop (no command line)

On github.com → **Add file → Upload files** → drag `index.html`, `style.css`, `script.js`,
`i18n.js`, `robots.txt`, `sitemap.xml`, `.nojekyll`, `CNAME` and the `assets` folder (with its
`i18n` subfolder) in →
**Commit** → then follow step 2 above.

### Site URL

The meta tags, `robots.txt` and `sitemap.xml` already point at
`https://tavzuran.com/`. If you move the site to a different repo or a custom
domain, update it in these places:

| File | What to change |
|------|----------------|
| `index.html` | `og:url`, `og:image`, `twitter:image`, `<link rel="canonical">`, and the `url` in the JSON-LD block |
| `robots.txt` | the `Sitemap:` line |
| `sitemap.xml` | the `<loc>` line |

Social previews (WhatsApp, Instagram, X) need absolute URLs — relative paths will not show an image.

### Custom domain (optional)

Point your domain's DNS at GitHub Pages, then **Settings → Pages → Custom domain**. GitHub commits a
`CNAME` file for you. Update the URLs above to the new domain and tick **Enforce HTTPS**.

---

## 4. What's already handled

- **Mobile-first** and checked with no horizontal scroll at 375 / 390 / 430 px, tablet and desktop
- **Sticky bottom CTA bar** on phones (Instagram traffic lands on a visible "Book a Free Call")
- **Five colours × dark/light/system** — green (default), blue, slate, ocean and violet, chosen
  from the palette button in the header. Dark is the default. Nothing is stored, so the choice lasts for the visit.
- **Animations** — the flight through the sky, pinned chapters, scroll reveals and the price
  count-up; all switched off under
  `prefers-reduced-motion: reduce`
- **Works without JavaScript** — all content renders, all links still work
- **SEO** — title, meta description, Open Graph, Twitter card, canonical, JSON-LD business schema,
  semantic HTML, one `<h1>`, ordered heading levels
- **Honest by default** — no invented clients, no fake testimonials, no claimed case studies. The
  Human + AI section, the "Example build" chips and the family reviews all say what's true today.
- **21 languages** — English is authentic, the other 20 are AI-translated, each with a visible
  notice in that language, `hreflang` tags, and right-to-left support for Arabic
- **Performance** — no libraries, no framework, one small CSS file, one small JS file, all
  illustrations are inline SVG (no image downloads). No external requests at all.

### Design system: "First Light"

The site is a voyage through space. One fixed `<canvas id="sky">` sits behind every page and is
painted by section `6b` of `script.js`; scrolling flies the camera forward.

| Piece | What it is |
|---|---|
| Stars | Each has a depth. Scrolling moves the camera through them, so they come towards you and stretch into streaks when you scroll fast |
| The light | "The idea": a glowing point with pulse rings that waits in each chapter. Its position per chapter is the `LIGHT` table in section 6 of `script.js` |
| Planets and dust | Drawn in depth along the route (`BODIES`, `CLOUDS`), so you pass them as you travel |
| Twin star | In the Human + AI chapter the light splits into two lights circling each other |
| The drawing | In the process chapter the light draws itself into a product screen, then launches: the stars streak |
| Pinned chapters | Problem, Human + AI and Process hold still while their statements change one at a time (`data-pin` in `index.html`, section 14 of `style.css`) |
| Fly-through | The first screen grows and blurs away as you leave it; chapter headings grow in from the distance |
| Chapter rail | The column of dots on the right edge of the home page (desktop only) |
| Colour band | The price chapter, in the palette's saturated colour |

Everything is hand-written canvas and CSS: no animation library, nothing loaded from another origin.

**Fallbacks.** With `prefers-reduced-motion`, or in a window under 560px tall, nothing is pinned and
nothing streaks, orbits or pulses: the sky is a still picture and the pinned chapters are ordinary
lists. Without JavaScript the canvas stays empty, a CSS gradient stands in for the light, and all the
content is still there.

Type: the visitor's own **system sans-serif** for headlines and text (nothing downloaded), **IBM Plex
Mono** for captions, **Caveat** for the signature. Licences are in `LICENSES.md`.

New labels reuse wording that is already on the page, so the existing translations cover them.

### Colour themes

Two independent axes on `<html>`:

| Attribute | Values |
|---|---|
| `data-theme` | `dark` (night, the default) \| `light` (daylight) |
| `data-palette` | `green` \| `blue` \| `slate` \| `ocean` \| `violet` |

The defaults (`dark`, `green`) are written on `<html>` in the markup, so the first paint is already
correct. A palette sets the tint of the sky, the colour of the light (and so the logo, links and
highlights) and the colour band. Each is one block in section 2 of `style.css`:

```css
:root[data-palette="blue"] {
  --bg: #03050b; --bg-2: #0a0f1e; --card: #0b1122;
  --hue: #8fb0ff; --hue-l: #2450c8; --glow-rgb: 96, 140, 255; --band: #1838b0; --band-2: #102780;
}
```

`--hue` is the light as a text colour on night, `--hue-l` its readable twin for daylight, and
`--glow-rgb` the same light for the canvas.

**To add a palette:** add a block like the one above, add its two swatch colours in section 6
(`.appear__sw[data-palette=…]`), add the name to `PALETTES` in `script.js`, and add a swatch button in
`index.html` and in `chrome_open()` in `tools/build.py`.

⚠️ **Check contrast.** `--hue` must reach 4.5:1 on `--card`, `--hue-l` 4.5:1 on `#f2f5f2`, and the
band's light text 4.5:1 on `--band`. The five shipped palettes measure 4.7:1 or better.

### Security

The site is static — no server code, no database, no forms, no user accounts — so most web
vulnerabilities simply do not apply. What is in place:

- **No third-party requests at all.** Fonts are self-hosted in `assets/fonts/`, so nothing about
  your visitors is sent to any other company, and there is no external script that could ever be
  compromised. This also keeps you clear of the EU complaints about Google Fonts logging visitor IPs.
- **Content Security Policy** (`<meta http-equiv="Content-Security-Policy">` near the top of
  `index.html`). Everything must come from this origin: no external scripts, no plugins, no forms
  posting anywhere. If someone ever managed to inject a `<script>` tag, the browser would refuse
  to run it.
- **Referrer policy** — `strict-origin-when-cross-origin`, so outbound clicks don't leak full URLs.
- **Values read from `localStorage` are validated**, never applied to the DOM verbatim.
- **No dependencies** — no npm packages, so no supply-chain risk and nothing to keep patched.

⚠️ **If you edit either inline `<script>` in `index.html`, the CSP hashes must be regenerated**, or
the browser will refuse to run that script. The page still works without them (it just loses the
pre-paint theme), but regenerate them properly:

```bash
# prints the sha256-... value for a given inline script body
python -c "import hashlib,base64,re,sys; h=open('index.html',encoding='utf-8').read(); print([('sha256-'+base64.b64encode(hashlib.sha256(b.encode()).digest()).decode()) for b in re.findall(r'<script(?![^>]*src=)[^>]*>(.*?)</script>', h, re.S)])"
```

Or simply run `python tools/csp.py`, which rewrites the hashes on every page.

What CSP **cannot** do here: GitHub Pages can't send real HTTP headers, so `frame-ancestors`
(clickjacking protection) and HSTS are unavailable. Neither matters much for a brochure site.

The real risks are your **accounts**, not this code: GitHub, GoDaddy and the email behind them.
Keep 2FA on all three and the domain auto-renewing.

### Fonts and local preview

Fonts live in `assets/fonts/` and are loaded by `@font-face` rules at the top of `style.css`.

When you open `index.html` **directly from disk**, the browser blocks the two `<link rel="preload">`
font hints as cross-origin (a `file://` rule, not a bug) and logs two console errors. The fonts
still load and the page looks correct. For an exact preview, run the local server from section 1.

---

## 5. Common edits

| I want to… | Where |
|-----------|-------|
| Change the default colour of the light | `style.css` → `:root { --hue: #5fe0a6; --hue-l: #14734b; --glow-rgb: 84, 224, 160; }`. Keep `--hue` at 4.5:1 on `--card` and `--hue-l` at 4.5:1 on the daylight background. |
| Change the MVP price | `index.html` → search `20,000` (appears in the hero badge, MVP section, mobile menu, footer, meta description) |
| Add / remove a service or industry card | `index.html` → `#services` / `#industries` — copy an `<article class="card ...">` block |
| Edit the About text | `index.html` → `#about` (the credibility strip is `.about__stats`) |
| Edit the Human + AI section | `index.html` → `#human` |
| Change section order | `index.html` → move whole `<section>` blocks; nav links use the section `id`s |
| Rename a nav item | `index.html` → `.nav__links` **and** `.menu__inner` (desktop and mobile menus) |

---

© 2026 Tavzuran.
