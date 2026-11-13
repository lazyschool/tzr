# /assets

| File | What it is | Safe to replace? |
|------|------------|------------------|
| `icon.png` | Browser tab icon (192×192, the "T" mark in the default ink) | Yes — keep the same filename |
| `og-image.png` | Social preview card, 1200×630 (WhatsApp / Instagram / X link previews) | Yes — keep the same filename and size |
| `founder.jpg` | The photograph in the About section | Yes — keep it around 760×950 |
| `fonts/` | Self-hosted webfonts and their licence texts | See `LICENSES.md` in the repository root |

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

`og-image.png` is referenced by absolute URL from every page (`og:image` and
`twitter:image`), because social apps will not load a relative path. If the site
moves to another domain, update those URLs in `index.html` and in `head()` in
`tools/build.py`, then re-run `python tools/build.py && python tools/csp.py`.
