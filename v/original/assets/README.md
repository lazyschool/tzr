# /assets

| File | What it is | Safe to replace? |
|------|------------|------------------|
| `favicon.svg` | Browser tab icon | Yes — keep the same filename |
| `og-image.svg` | Social preview card (WhatsApp / Instagram / X link previews) | Yes — see note below |

## Adding project images

Drop project screenshots here (`assets/restaurant-app.jpg`, etc.) and swap the
inline SVG thumbnail inside a portfolio card in `index.html` for:

```html
<img class="proj__img" src="assets/restaurant-app.jpg"
     alt="Screens from the restaurant ordering app"
     loading="lazy" decoding="async" width="800" height="600">
```

Keep images under ~200 KB and around 800×600 px so the site stays fast on mobile.

## Social preview note

`og-image.svg` works, but a few social apps only render **PNG/JPG** previews.
For the best result, export it once to a 1200×630 PNG:

1. Open `assets/og-image.svg` in a browser, or use any SVG → PNG converter.
2. Save the result as `assets/og-image.png`.
3. In `index.html`, change the two lines containing `og-image.svg` to `og-image.png`
   (`<meta property="og:image">` and `<meta name="twitter:image">`).

Also update the domain in those tags (and in `og:url` / `<link rel="canonical">`)
to your real GitHub Pages URL — social previews need absolute URLs.
