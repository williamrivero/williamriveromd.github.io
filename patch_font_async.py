#!/usr/bin/env python3
"""Load Google Fonts without blocking the first paint, on every page.

Lighthouse (Nov 17 2026) found the blocking fonts.googleapis.com stylesheet cost 0.8-2.3 s of first paint
on the homepage, guides and indexes. This rewrites each blocking

    <link href="https://fonts.googleapis.com/css2?..." rel="stylesheet">

into a marked block that preconnects to fonts.gstatic.com, preloads the stylesheet and applies it when it
arrives (text shows at once in the fallback font, then swaps; the URL already carries display=swap), with a
<noscript> fallback:

    <!-- FONTS-ASYNC --> ... <!-- /FONTS-ASYNC -->

Idempotent. patch_font_link.py calls strip_async()/make_async() so a font-link run keeps the async form.

  python3 patch_font_async.py                 # root pages, guides/, downloads/
  python3 patch_font_async.py --dry-run
  python3 patch_font_async.py --guide igan-guide.html
"""
import argparse, glob, html, re, sys

BLOCK_RE = re.compile(r"<!-- FONTS-ASYNC -->.*?<!-- /FONTS-ASYNC -->", re.S)
# Pages kept on blocking fonts: the guides index's long Lora/DM Sans intro text reflows when the font swaps in
# (Lighthouse CLS 0.36 with async fonts vs 0.06 blocking, Nov 17 2026).
EXCLUDE = {"guides/index.html"}
LINK_RE = re.compile(r'<link\b[^>]*href=["\'](https://fonts\.googleapis\.com/css2[^"\']*)["\'][^>]*>')


def block(url: str) -> str:
    u = url  # keep the URL exactly as written (it may already contain &amp;)
    return ('<!-- FONTS-ASYNC -->'
            '<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>'
            f'<link rel="preload" as="style" href="{u}" onload="this.onload=null;this.rel=\'stylesheet\'">'
            f'<noscript><link rel="stylesheet" href="{u}"></noscript>'
            '<!-- /FONTS-ASYNC -->')


def strip_async(text: str) -> str:
    """Turn a marked async block back into one plain blocking stylesheet link."""
    def back(m):
        u = re.search(r'rel="preload" as="style" href="([^"]+)"', m.group(0))
        return f'<link href="{u.group(1)}" rel="stylesheet"/>' if u else m.group(0)
    return BLOCK_RE.sub(back, text)


def make_async(text: str) -> str:
    text = strip_async(text)
    done = []

    def sub(m):
        tag = m.group(0)
        if "stylesheet" not in tag or "preload" in tag:
            return tag
        done.append(1)
        return block(m.group(1))
    # only the <head>: leave any font links inside templates/scripts in the body alone
    head_end = text.lower().find("</head>")
    if head_end < 0:
        return text
    return LINK_RE.sub(sub, text[:head_end]) + text[head_end:]


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--dry-run", action="store_true")
    ap.add_argument("--guide")
    a = ap.parse_args()
    files = ([f"guides/{a.guide}"] if a.guide else
             sorted(glob.glob("*.html") + glob.glob("guides/*.html") + glob.glob("downloads/*.html")))
    n = 0
    for f in files:
        if f in EXCLUDE:
            continue
        s = open(f, encoding="utf-8").read()
        t = make_async(s)
        if t != s:
            n += 1
            if not a.dry_run:
                open(f, "w", encoding="utf-8").write(t)
    print(f"{n} page(s) {'would be ' if a.dry_run else ''}updated")


if __name__ == "__main__":
    sys.exit(main())
