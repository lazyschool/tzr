# HumansOfCoding — Website

Static marketing site for **HumansOfCoding** — apps, websites, MVPs and custom software.
Plain HTML, CSS and vanilla JavaScript. No build step, no framework, no server, no paid services.

```
humansofcoding/
├── index.html        all page content
├── style.css         all styling (mobile-first)
├── script.js         all behaviour + YOUR BUSINESS INFO at the top
├── assets/
│   ├── favicon.svg   browser tab icon
│   ├── og-image.svg  social share preview
│   └── README.md     how to add project images
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

Open `script.js`. The first block is the only place contact info lives. Instagram and email are
already filled in — the WhatsApp number is the one thing still to add:

```js
const CONFIG = {
  instagram: "humansofcoding",
  whatsapp:  "910000000000",             // ← your number: country code + number, digits only
  whatsappMessage: "Hi Adil! I have an idea I'd like to build. Can we talk?",
  email:     "adil@humansofcoding.com",   // already set
  emailSubject: "Project enquiry from humansofcoding.com",
  callSubject: "Free call request - HumansOfCoding",
  callBody: [ ...the pre-written email, one line per array entry... ],
  bookingUrl: ""                          // ← optional Cal.com / Calendly link
};
```

Every **Book a Free Call**, **WhatsApp**, **DM** and **Email** button on the page reads from this.

### How "Book a Free Call" works

All ten of those buttons open the visitor's email app with a message already written to
`adil@humansofcoding.com`, asking for their name, what they want to build, rough budget and a good
time to call. Edit `callBody` to change the wording — each array entry is one line.

If you later sign up for a scheduler (Cal.com, Calendly), put its link in `bookingUrl` and every one
of those buttons switches to the booking page instead. Nothing else needs touching.

WhatsApp buttons fall back to Instagram while `whatsapp` is still the `910000000000` placeholder, so
no button is ever dead.

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
drop the "Straight up: HumansOfCoding is new…" line from the section heading too.

---

## 3. Deploy to GitHub Pages

### Option A — Push from the command line

This repo is already wired up: remote `origin` points at
`git@github.com:lazyschool/humansofcoding.git` and the code lives on the `master` branch.

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
   **https://humansofcoding.com/**

`index.html` must stay in the repository root — Pages serves it as the home page.
`.nojekyll` is already included so GitHub serves every file untouched.

### Option B — Drag and drop (no command line)

On github.com → **Add file → Upload files** → drag `index.html`, `style.css`, `script.js`,
`robots.txt`, `sitemap.xml`, `.nojekyll` and the `assets` folder in → **Commit** → then follow
step 2 above.

### Site URL

The meta tags, `robots.txt` and `sitemap.xml` already point at
`https://humansofcoding.com/`. If you move the site to a different repo or a custom
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
- **Light + dark theme** with a toggle, remembered per visitor, no flash on load
- **Animations** — scroll reveals, floating doodles, drawn hand-made line art, animated timeline,
  price count-up; every one of them is switched off under `prefers-reduced-motion: reduce`
- **Works without JavaScript** — all content renders, all links still work
- **SEO** — title, meta description, Open Graph, Twitter card, canonical, JSON-LD business schema,
  semantic HTML, one `<h1>`, ordered heading levels
- **Honest by default** — no invented clients, no fake testimonials, no claimed case studies. The
  Human + AI section, the "Example build" chips and the family reviews all say what's true today.
- **Performance** — no libraries, no framework, one small CSS file, one small JS file, all
  illustrations are inline SVG (no image downloads). Only external request: Google Fonts.

### Want an even faster site?

Fonts are the only third-party request. To drop it, delete the three `fonts.g...` lines in
`index.html`; the CSS already falls back to system fonts.

---

## 5. Common edits

| I want to… | Where |
|-----------|-------|
| Change the accent colour | `style.css` → `:root { --accent: #0f6ccc; }` plus `--accent-hover`, `--accent-soft`, `--accent-light`, `--accent-glow`. `--accent` carries button and link text so keep it dark enough to read on white; `--accent-light` is decoration only (sketch strokes, doodles, sparks). |
| Change the MVP price | `index.html` → search `50,000` (appears in the hero badge, MVP section, mobile menu, footer, meta description) |
| Add / remove a service or industry card | `index.html` → `#services` / `#industries` — copy an `<article class="card ...">` block |
| Edit the About text | `index.html` → `#about` (the credibility strip is `.about__stats`) |
| Edit the Human + AI section | `index.html` → `#human` |
| Change section order | `index.html` → move whole `<section>` blocks; nav links use the section `id`s |
| Rename a nav item | `index.html` → `.nav__links` **and** `.menu__inner` (desktop and mobile menus) |

---

© 2026 HumansOfCoding.
