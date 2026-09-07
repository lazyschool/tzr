# -*- coding: utf-8 -*-
"""The site navigation, generated once for every page.

There are twenty pages now, and five flat links no longer reach most of them.
The primary nav is four items, three of which open a panel.

`prefix` is what it takes to get back to the site root from the page being
built: "" for index.html, "../" for anything in a subfolder. Links always name
index.html explicitly — a bare folder works on a web server but renders as a
directory listing when the site is opened from disk.
"""
from content import ARTICLES, ARTICLE_TAGS, CASE_STUDIES

CARET = ('<svg class="nd__caret" viewBox="0 0 24 24" fill="none" stroke="currentColor" '
         'stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round" '
         'aria-hidden="true"><path d="m6 9 6 6 6-6"/></svg>')

# The home-page sections behind the Services item.
SECTIONS = [
    ("Services", "#services"),
    ("Human + AI", "#human"),
    ("Industries", "#industries"),
    ("Process", "#process"),
]


def _grouped_studies():
    """Case studies by category, categories in first-appearance order."""
    order, groups = [], {}
    for cs in CASE_STUDIES:
        if cs["category"] not in groups:
            order.append(cs["category"])
            groups[cs["category"]] = []
        groups[cs["category"]].append(cs)
    return [(cat, groups[cat]) for cat in order]


def primary(prefix, active=""):
    """The desktop nav: four items, three of them with a panel."""
    p = prefix
    out = ['    <nav class="nav__links" aria-label="Primary">']

    # --- Services -----------------------------------------------------------
    links = "".join(
        '\n          <a href="%sindex.html%s">%s</a>' % (p, anchor, label)
        for label, anchor in SECTIONS)
    out.append('''      <div class="nd">
        <button class="nd__btn" type="button" aria-expanded="false" aria-controls="ndServices">Services{caret}</button>
        <div class="nd__panel" id="ndServices" hidden>
          <div class="nd__col">{links}
          </div>
        </div>
      </div>'''.format(caret=CARET, links=links))

    # --- Case Studies -------------------------------------------------------
    # split by row count, not by category count, or one column ends up
    # three times the height of the other
    groups = _grouped_studies()
    total = sum(len(items) + 1 for _, items in groups)
    left, right, run = [], [], 0
    for cat, items in groups:
        if run < (total + 1) // 2:
            left.append((cat, items))
            run += len(items) + 1
        else:
            right.append((cat, items))

    cols = []
    for chunk in (left, right):
        col = ['          <div class="nd__col">']
        for cat, items in chunk:
            col.append('            <p class="nd__head">%s</p>' % cat)
            for cs in items:
                col.append('            <a href="%scase-studies/%s.html">%s</a>'
                           % (p, cs["slug"], cs["title"]))
        col.append('          </div>')
        cols.append("\n".join(col))
    out.append('''      <div class="nd">
        <button class="nd__btn{on}" type="button" aria-expanded="false" aria-controls="ndWork">Case Studies{caret}</button>
        <div class="nd__panel nd__panel--wide" id="ndWork" hidden>
{cols}
          <a class="nd__all" href="{p}case-studies/index.html">All case studies <span aria-hidden="true">&#8594;</span></a>
        </div>
      </div>'''.format(on=" is-active" if active == "case-studies" else "",
                       caret=CARET, cols="\n".join(cols), p=p))

    # --- Articles -----------------------------------------------------------
    by_tag = [(tag, [a for a in ARTICLES if a["tag"] == tag]) for tag in ARTICLE_TAGS]
    total = sum(len(items) + 1 for _, items in by_tag)
    left, right, run = [], [], 0
    for tag, items in by_tag:
        if run < (total + 1) // 2:
            left.append((tag, items))
            run += len(items) + 1
        else:
            right.append((tag, items))

    cols = []
    for chunk in (left, right):
        col = ['          <div class="nd__col">']
        for tag, items in chunk:
            col.append('            <p class="nd__head">%s</p>' % tag)
            for a in items:
                col.append('            <a href="%sarticles/%s.html">%s</a>'
                           % (p, a["slug"], a["title"]))
        col.append('          </div>')
        cols.append("\n".join(col))

    out.append('''      <div class="nd">
        <button class="nd__btn{on}" type="button" aria-expanded="false" aria-controls="ndReads">Articles{caret}</button>
        <div class="nd__panel nd__panel--wide" id="ndReads" hidden>
{cols}
          <a class="nd__all" href="{p}articles/index.html">Read all articles <span aria-hidden="true">&#8594;</span></a>
        </div>
      </div>'''.format(on=" is-active" if active == "articles" else "",
                       caret=CARET, cols="\n".join(cols), p=p))

    out.append('      <a href="%sindex.html#about">About</a>' % p)
    out.append('    </nav>')
    return "\n".join(out)


def mobile(prefix):
    """The burger menu. Groups are <details>, so they open with no JavaScript."""
    p = prefix
    out = ['<div class="menu" id="mobileMenu" hidden>',
           '  <nav class="menu__inner" aria-label="Mobile">']

    sections = "".join(
        '\n      <a href="%sindex.html%s">%s</a>' % (p, anchor, label)
        for label, anchor in SECTIONS)
    out.append('''    <details class="mgroup">
      <summary><span>01</span> Services</summary>
      <div class="mgroup__body">{sections}
      </div>
    </details>'''.format(sections=sections))

    studies = []
    for cat, items in _grouped_studies():
        studies.append('\n      <p class="nd__head">%s</p>' % cat)
        for cs in items:
            studies.append('\n      <a href="%scase-studies/%s.html">%s</a>'
                           % (p, cs["slug"], cs["title"]))
    out.append('''    <details class="mgroup">
      <summary><span>02</span> Case Studies</summary>
      <div class="mgroup__body">{studies}
        <a class="nd__all" href="{p}case-studies/index.html">All case studies <span aria-hidden="true">&#8594;</span></a>
      </div>
    </details>'''.format(studies="".join(studies), p=p))

    reads = []
    for tag in ARTICLE_TAGS:
        reads.append('\n      <p class="nd__head">%s</p>' % tag)
        for a in [x for x in ARTICLES if x["tag"] == tag]:
            reads.append('\n      <a href="%sarticles/%s.html">%s</a>'
                         % (p, a["slug"], a["title"]))
    reads = "".join(reads)
    out.append('''    <details class="mgroup">
      <summary><span>03</span> Articles</summary>
      <div class="mgroup__body">{reads}
        <a class="nd__all" href="{p}articles/index.html">Read all articles <span aria-hidden="true">&#8594;</span></a>
      </div>
    </details>'''.format(reads=reads, p=p))

    out.append('    <a href="%sindex.html#about"><span>04</span> About Adil</a>' % p)
    out.append('    <a href="%sindex.html#contact"><span>05</span> Contact</a>' % p)
    return "\n".join(out)
