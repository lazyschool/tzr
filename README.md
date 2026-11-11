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

### c) Reviews → `index.html`

Search for `FAMILY REVIEWS`. While the studio is new, the reviews section carries three real
(and funny) quotes from Adil's mother, father and brother, under a heading that says plainly there
are no clients yet. Nothing on the page claims a customer you don't have.

When you land real client reviews, replace each `<blockquote>`, `.t__name` and `.t__role`, swap the
`Family` chip for something else (or delete it), and update the section heading from
"No clients yet. So I asked my family."

### d) Portfolio wording → `index.html`

The six project cards each carry an **Example build** chip, and the section says outright that these
are example builds rather than client work. As soon as you ship something real, replace that card's
content and delete its `<span class="proj__flag">Example build</span>` chip. Once every card is real,
drop the "Straight up: Tavzuran is new…" line from the section heading too.

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
- **Five marker colours × light/dark/system** — orange (default), blue, green, violet and slate,
  chosen from the palette button in the header. Nothing is stored, so the choice lasts for the visit.
- **Animations** — scroll reveals, the hero drawing tracing itself in, the timeline filling and the
  price count-up; all switched off under
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

### Design system: "Rev. 01"

The site is drawn as an architect's working drawing. A first version is,
literally, revision one. The pieces, all in `style.css`:

| Piece | What it is |
|---|---|
| Drafting film | Light mode: a pale green-grey sheet with a fine 22px grid and a heavier line every five cells |
| Blueprint | The hero, the Human + AI band and the final call to action are always blueprint; dark mode turns the whole site blueprint. One class, `.bp`, swaps the palette, so every component inside redraws itself |
| Sheet numbers | Each section heading opens with a boxed number (01, 02…) from a CSS counter, so adding a section renumbers the rest |
| Crop marks | The four corner marks on every section |
| Title blocks | Any `.cards` block is a ruled table with a frame and a rule between every cell; the hero, the case-study "at a glance" strip and the footer are title blocks |
| Dimension lines | Under the headline, around the hero drawing and along the about photo |
| Revision flags | `.proj__flag`, `.t__flag` — a tilted outline tag in marker colour |
| Revision cloud | The "what we'd leave out" list on each case study, drawn as a dashed outline |

Type: **IBM Plex Mono** for headlines, labels and buttons; the visitor's own **system sans-serif**
for reading text (nothing downloaded); **Caveat** for one hand-written note. Licences are in
`LICENSES.md`.

Labels on the drawing reuse wording that is already on the page (IDEA, BUILD, USERS, SCALE,
"Starting at"…), so the existing translations cover them; anything else is numerals and symbols.

### Colour themes

Two independent axes on `<html>`:

| Attribute | Values |
|---|---|
| `data-theme` | `light` (drafting film) \| `dark` (blueprint) |
| `data-palette` | `orange` \| `blue` \| `green` \| `violet` \| `slate` |

The defaults (`light`, `orange`) are written on `<html>` in the markup, so the first paint is already
correct. A palette changes one thing: the **marker colour** used for sheet labels, call-outs, flags,
the button shadow and the price. Each marker is two values in section 2 of `style.css` — `--a-l` for
film and `--a-d` for blueprint:

```css
:root[data-palette="blue"] { --a-l: #1c46c9; --a-d: #8fb4ff; }
```

**To add a marker:** add a line like the one above, add its two swatch colours beside the others in
section 6 (`.appear__sw[data-palette=…]`), add the name to `PALETTES` in `script.js`, and add a
swatch button in `index.html` and in `chrome_open()` in `tools/build.py`.

⚠️ **A marker carries text, so both values must reach 4.5:1** — `--a-l` against the darker film
(`#e3e8e0`) and `--a-d` against the lightest blueprint (`#143670`). The five shipped markers measure
between 4.6:1 and 7.8:1.

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
| Change the default marker colour | `style.css` → `:root { --a-l: #a83f12; --a-d: #ff8a52; }` (film and blueprint values). Both carry text, so keep each at 4.5:1 or better against its background. |
| Change the MVP price | `index.html` → search `20,000` (appears in the hero badge, MVP section, mobile menu, footer, meta description) |
| Add / remove a service or industry card | `index.html` → `#services` / `#industries` — copy an `<article class="card ...">` block |
| Edit the About text | `index.html` → `#about` (the credibility strip is `.about__stats`) |
| Edit the Human + AI section | `index.html` → `#human` |
| Change section order | `index.html` → move whole `<section>` blocks; nav links use the section `id`s |
| Rename a nav item | `index.html` → `.nav__links` **and** `.menu__inner` (desktop and mobile menus) |

---

© 2026 Tavzuran.
