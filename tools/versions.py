#!/usr/bin/env python3
"""Rebuild the older design versions under /v/ from their branches.

    python tools/versions.py

Each version is the finished site from its branch, unpacked into v/<folder>/
with the design switcher added and search engines told to ignore it. Run again
whenever one of those branches changes. The default design at the site root is
not touched.
"""
import io, os, re, shutil, subprocess, sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
VERSIONS = [("blueprint", "redesign-rev-01"), ("honest-quote", "redesign-honest-quote"), ("original", "pre-redesign")]
KEEP_OUT = ("tools", "README.md", "LICENSES.md", "CNAME", "robots.txt", "sitemap.xml", ".gitignore", ".nojekyll")
SCRIPT = re.compile(r'<script src="((?:\.\./)*)script\.js" defer></script>')

def main():
    base = os.path.join(ROOT, "v")
    shutil.rmtree(base, ignore_errors=True)
    for folder, branch in VERSIONS:
        dest = os.path.join(base, folder)
        os.makedirs(dest)
        tar = subprocess.run(["git", "archive", branch], cwd=ROOT, check=True, capture_output=True).stdout
        subprocess.run(["tar", "-x", "-C", dest], input=tar, check=True)
        for n in KEEP_OUT:
            p = os.path.join(dest, n)
            if os.path.isdir(p): shutil.rmtree(p)
            elif os.path.exists(p): os.remove(p)
        shutil.copy(os.path.join(ROOT, "switcher.js"), dest)
        count = 0
        for dp, _, files in os.walk(dest):
            for f in files:
                if not f.endswith(".html"): continue
                p = os.path.join(dp, f)
                h = io.open(p, encoding="utf-8").read()
                h = SCRIPT.sub(lambda m: m.group(0) + '\n<script src="' + m.group(1) + 'switcher.js" defer></script>', h, 1)
                h = h.replace("<head>", '<head>\n<meta name="robots" content="noindex" />', 1)
                io.open(p, "w", encoding="utf-8", newline="\n").write(h)
                count += 1
        print(f"{folder}: {count} pages from {branch}")

if __name__ == "__main__":
    main()
