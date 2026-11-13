# Third-party assets and their licences

This is the complete record of everything on tavzuran.com that was not made for
it. If an asset is not listed here, it is original to this project.

The live site makes **no requests to any other origin**. Every file below is
stored in this repository and served from tavzuran.com itself.

## Fonts

| Family | Used for | Made by | Licence | Files |
|---|---|---|---|---|
| IBM Plex Mono | Captions and small labels | IBM Corp. (USA) — Mike Abbink with Bold Monday (Netherlands) | SIL Open Font License 1.1 | `assets/fonts/ibm-plex-mono-*.woff2` |
| Caveat | The signature | Impallari Type (Argentina) | SIL Open Font License 1.1 | `assets/fonts/caveat-*.woff2` |

The full licence text for each family, including its copyright line, is in
`assets/fonts/licenses/`. The OFL permits commercial use, web embedding and
redistribution; it asks only that the licence travel with the fonts (it does,
in that folder) and that the fonts are not sold on their own. No attribution is
required on the pages.

### Where the files came from

| What | Source | Operator | Retrieved |
|---|---|---|---|
| IBM Plex Mono `.woff2` files (Latin and Latin Extended subsets) | `fonts.gstatic.com`, located through the stylesheet at `fonts.googleapis.com` | Google LLC, USA | 11 November 2026 |
| Caveat `.woff2` files | `fonts.gstatic.com` | Google LLC, USA | before this record began; carried over from the previous design |
| Licence texts and designer metadata | `github.com/google/fonts` (`ofl/ibmplexmono`, `ofl/caveat`) | GitHub, Inc. (Microsoft), USA | 11 November 2026 |

The files are used exactly as served: they are not renamed internally, edited
or re-subset. "Plex" is a Reserved Font Name of IBM Corp.

Upstream projects: <https://github.com/IBM/plex>, <https://github.com/googlefonts/caveat>.

Headlines and reading text use the visitor's own system font (`system-ui`: San Francisco on
Apple devices, Segoe UI on Windows, Roboto on Android). Nothing is downloaded
for it and no licence applies to the site.

## Everything else

| Asset | Origin |
|---|---|
| `assets/founder.jpg` | Photograph of Adil, supplied by him |
| `assets/icon.png`, the inline "T" mark | Tavzuran's own logo |
| `assets/og-image.png` | Made for this site from the fonts above and the logo |
| The sky (stars, planets, the light, the product drawing), icons and product mock-ups | Drawn in code for this site (canvas, inline SVG and CSS) |
| All copy, case studies and articles | Written for this site |

No stock photography, icon library, CSS framework, JavaScript library,
analytics script or embedded third-party content is used.

## Outbound links

The pages link to `instagram.com/tavzuran` (Meta Platforms, USA) and to
`humansofenglish.com`, a client site Tavzuran built. These are plain links a
visitor may choose to follow; nothing is loaded from either. The picture beside
the client project is one of this site's own drawn screens, not a screenshot
of the client's site.
