# -*- coding: utf-8 -*-
"""Recompute the Content-Security-Policy script hashes for every page.

    python tools/csp.py            # from the repository root

GitHub Pages cannot send real CSP headers, so the policy lives in a <meta> tag
and every inline script has to be listed by its sha256 hash. Edit an inline
script without re-running this and the browser refuses to run it.

Comments are stripped before scanning, because the explanatory comment above
the policy itself contains the word script in tag form and would otherwise be
mistaken for a real one.
"""
import base64
import glob
import hashlib
import io
import os
import re

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# an inline <script> is one with no src attribute; ld+json counts, browsers
# enforce script-src on it too
INLINE = re.compile(
    r'<script(?![^>]*\ssrc=)[^>]*>(.*?)</script>', re.S | re.I)
COMMENT = re.compile(r'<!--.*?-->', re.S)
POLICY = re.compile(
    r"(script-src 'self' https://static\.cloudflareinsights\.com)([^;]*);")


def hashes_for(html):
    body = COMMENT.sub('', html)
    out = []
    for code in INLINE.findall(body):
        digest = hashlib.sha256(code.encode('utf-8')).digest()
        token = "'sha256-%s'" % base64.b64encode(digest).decode('ascii')
        if token not in out:
            out.append(token)
    return out


def main():
    pages = ([os.path.join(ROOT, 'index.html')]
             + sorted(glob.glob(os.path.join(ROOT, 'case-studies', '*.html')))
             + sorted(glob.glob(os.path.join(ROOT, 'articles', '*.html'))))

    for page in pages:
        with io.open(page, encoding='utf-8') as fh:
            html = fh.read()
        tokens = hashes_for(html)
        if not tokens:
            print('  !! no inline scripts found in', page)
            continue
        replacement = r"\1 " + " ".join(tokens) + ";"
        new, count = POLICY.subn(replacement, html, count=1)
        if not count:
            print('  !! no policy matched in', os.path.relpath(page, ROOT))
            continue
        if new != html:
            with io.open(page, 'w', encoding='utf-8', newline='') as fh:
                fh.write(new)
        print('  %-46s %d hash(es)%s' % (
            os.path.relpath(page, ROOT).replace(os.sep, '/'),
            len(tokens), '' if new == html else '  (updated)'))


if __name__ == '__main__':
    main()
