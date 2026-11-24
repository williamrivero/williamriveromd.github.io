#!/usr/bin/env python3
"""
build_theme_dim.py — generate assets/theme-dim.css (the "Dim" theme).

The site has three appearance themes plus Auto (see assets/theme.js):

  Light  — default, no attribute
  Dim    — html[data-theme="dark"][data-shade="dim"]
  Dark   — html[data-theme="dark"]

Dim is an overlay on Dark: every existing dark-mode rule still applies, and
this stylesheet re-maps only the colors that need to change. That way the
thousands of per-guide dark-mode rules never have to be hand-duplicated.

How it works
  1. Scan every <style> block in every .html page plus every .css file.
  2. Collect each rule whose selector contains [data-theme="dark"].
  3. For each color literal in those rules:
       - dark SURFACES (backgrounds, borders, surface tokens; luminance
         < 0.05) are lifted to a soft charcoal gray, keeping their hue at
         reduced saturation (#0f1520 → #262b33-ish);
       - light TEXT colors are lightened, only as far as needed, to keep
         WCAG AA ≥ 4.5:1 against the lightest Dim card surface;
       - everything else (images, light cards, chips, shadows) is left alone.
  4. Emit the same selector with [data-shade="dim"] added — one attribute
     more specific, so it always wins over the Dark rule it shadows.
  5. Rules found on every dark-mode page are global. All others are scoped
     with [data-dimg~="<id>"] so a token defined on one page cannot leak into
     another. assets/theme-dim-groups.json maps each page to its ids;
     patch_theme_modes.py writes them into that page's bootstrap.

Re-run after adding guides that carry new dark-mode rules (idempotent):

  python3 build_theme_dim.py            # write assets/theme-dim.css
  python3 build_theme_dim.py --check    # report only, exit 1 if stale
"""

import argparse
import colorsys
import json
import re
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parent
OUT = REPO / "assets" / "theme-dim.css"
SKIP_DIRS = {".git", "node_modules", "tests", "scripts-qa", "blueprints", "docs"}

DARK_ATTR = re.compile(r"\[data-theme=(['\"]?)dark\1\]")
COLOR_RE = re.compile(
    r"#[0-9a-fA-F]{8}\b|#[0-9a-fA-F]{6}\b|#[0-9a-fA-F]{3,4}\b"
    r"|rgba?\(\s*[\d.]+%?\s*,?\s*[\d.]+%?\s*,?\s*[\d.]+%?\s*(?:[,/]\s*[\d.]+%?\s*)?\)"
)

# Lightest Dim card surface that text may sit on; text must clear 4.5:1 on it.
REF_SURFACE_LUM = 0.052          # ≈ #3a414c
MIN_TEXT_CONTRAST = 4.6           # a hair above 4.5 for rounding safety
TEXT_TOKENS = re.compile(r"^--(text|red|amber|green|purple|teal|gold|blue|orange|link|accent|muted|faint|ink|fg|slate|gray|grey|subtle|body|heading)(?!.*(soft|bg|surface|light|border|tint|wash))")
COLOR_PROPS = re.compile(r"^(color|background(-color|-image)?|border(-top|-right|-bottom|-left)?(-color)?|outline(-color)?|fill|stroke|-webkit-text-fill-color|caret-color|text-decoration-color|--.*)$", re.I)


# ── color helpers ────────────────────────────────────────────────────────────
def parse_color(tok):
    t = tok.strip()
    if t.startswith("#"):
        h = t[1:]
        if len(h) in (3, 4):
            h = "".join(c * 2 for c in h)
        r, g, b = (int(h[i:i + 2], 16) for i in (0, 2, 4))
        a = int(h[6:8], 16) / 255 if len(h) == 8 else 1.0
        return r, g, b, a
    nums = re.findall(r"[\d.]+%?", t)
    vals = []
    for i, n in enumerate(nums[:3]):
        vals.append(float(n[:-1]) * 2.55 if n.endswith("%") else float(n))
    a = 1.0
    if len(nums) > 3:
        n = nums[3]
        a = float(n[:-1]) / 100 if n.endswith("%") else float(n)
    return int(round(vals[0])), int(round(vals[1])), int(round(vals[2])), a


def fmt(r, g, b, a):
    r, g, b = (max(0, min(255, int(round(v)))) for v in (r, g, b))
    if a >= 0.999:
        return f"#{r:02x}{g:02x}{b:02x}"
    return f"rgba({r},{g},{b},{a:.2f})".replace(".00)", ")")


def lum(r, g, b):
    def ch(c):
        c /= 255
        return c / 12.92 if c <= 0.03928 else ((c + 0.055) / 1.055) ** 2.4
    return 0.2126 * ch(r) + 0.7152 * ch(g) + 0.0722 * ch(b)


def lift_surface(r, g, b):
    """Map a near-black surface to soft charcoal, keeping hue."""
    h, l, s = colorsys.rgb_to_hls(r / 255, g / 255, b / 255)
    l2 = 0.112 + 0.68 * l
    s2 = s * 0.45
    rr, gg, bb = colorsys.hls_to_rgb(h, l2, s2)
    return rr * 255, gg * 255, bb * 255


def ensure_text(r, g, b):
    """Lighten toward white only as far as needed to pass on Dim cards."""
    need = MIN_TEXT_CONTRAST * (REF_SURFACE_LUM + 0.05) - 0.05
    if lum(r, g, b) >= need:
        return None
    for i in range(1, 101):
        t = i / 100
        rr, gg, bb = (c + (255 - c) * t for c in (r, g, b))
        if lum(rr, gg, bb) >= need:
            return rr, gg, bb
    return 255, 255, 255


def map_value(prop, value):
    """Return the Dim value for one declaration, or None if unchanged."""
    p = prop.lower()
    if p in ("box-shadow", "text-shadow", "filter", "backdrop-filter", "-webkit-filter"):
        return None
    is_text = p == "color" or p == "-webkit-text-fill-color" or (p.startswith("--") and TEXT_TOKENS.match(p))
    is_custom = p.startswith("--")
    changed = False

    def repl(m):
        nonlocal changed
        try:
            r, g, b, a = parse_color(m.group(0))
        except Exception:
            return m.group(0)
        L = lum(r, g, b)
        if is_text:
            if L >= 0.5 and a < 0.95 and not is_custom:
                changed = True
                return fmt(r, g, b, max(a, 0.8))
            if L >= 0.10:
                out = ensure_text(r, g, b)
                if out:
                    changed = True
                    return fmt(*out, a)
            elif is_custom and L < 0.05 and a >= 0.6:
                # surface-ish token mis-named as text (e.g. --teal-light)
                changed = True
                return fmt(*lift_surface(r, g, b), a)
            return m.group(0)
        if L < 0.05 and a >= 0.6:
            changed = True
            return fmt(*lift_surface(r, g, b), a)
        return m.group(0)

    new = COLOR_RE.sub(repl, value)
    return new if changed else None


# ── tiny CSS parser ──────────────────────────────────────────────────────────
def strip_comments(s):
    return re.sub(r"/\*.*?\*/", "", s, flags=re.S)


def parse(s):
    out, i, n = [], 0, len(s)
    while i < n:
        j = s.find("{", i)
        if j < 0:
            break
        prelude = s[i:j].strip()
        if ";" in prelude and not prelude.startswith("@"):
            prelude = prelude.split(";")[-1].strip()
        depth, k = 1, j + 1
        while k < n and depth:
            if s[k] == "{":
                depth += 1
            elif s[k] == "}":
                depth -= 1
            k += 1
        body = s[j + 1:k - 1]
        if prelude.startswith(("@media", "@supports", "@layer")):
            out.append((prelude, parse(body)))
        else:
            out.append((prelude, body.strip()))
        i = k
    return out


def split_decls(body):
    decls, buf, depth = [], "", 0
    for ch in body:
        if ch == "(":
            depth += 1
        elif ch == ")":
            depth -= 1
        if ch == ";" and depth == 0:
            decls.append(buf)
            buf = ""
        else:
            buf += ch
    if buf.strip():
        decls.append(buf)
    res = []
    for d in decls:
        if ":" not in d:
            continue
        prop, val = d.split(":", 1)
        res.append((prop.strip(), val.strip()))
    return res


def dimify_selector(sel):
    return DARK_ATTR.sub(lambda m: m.group(0) + '[data-shade="dim"]', sel, count=1)


# ── main ─────────────────────────────────────────────────────────────────────
MAP_OUT = REPO / "assets" / "theme-dim-groups.json"
LINK_RE = re.compile(r"<link[^>]+href=[\"']([^\"'?#]+\.css)[^\"']*[\"'][^>]*>", re.I)


def page_key(path):
    return path.relative_to(REPO).as_posix()


def iter_pages():
    for path in sorted(REPO.rglob("*.html")):
        rel = path.relative_to(REPO)
        if any(part in SKIP_DIRS for part in rel.parts):
            continue
        yield path


def page_css(path, css_cache):
    """Inline <style> blocks plus local stylesheets the page links."""
    text = path.read_text(encoding="utf-8", errors="ignore")
    chunks = re.findall(r"<style[^>]*>(.*?)</style>", text, flags=re.S)
    for href in LINK_RE.findall(text):
        if href.startswith(("http:", "https:", "//")) or "theme-dim" in href:
            continue
        target = (REPO / href.lstrip("/")) if href.startswith("/") else (path.parent / href)
        try:
            target = target.resolve()
        except Exception:
            continue
        if target not in css_cache:
            css_cache[target] = target.read_text(encoding="utf-8", errors="ignore") if target.is_file() else ""
        chunks.append(css_cache[target])
    return "".join(chunks)



def split_selectors(pre):
    """Split a selector list on top-level commas only (respects :is(), [..], quotes)."""
    out, buf, depth, quote = [], "", 0, None
    for ch in pre:
        if quote:
            buf += ch
            if ch == quote:
                quote = None
            continue
        if ch in "\"'":
            quote = ch
        elif ch in "([":
            depth += 1
        elif ch in ")]":
            depth -= 1
        elif ch == "," and depth == 0:
            out.append(buf.strip())
            buf = ""
            continue
        buf += ch
    if buf.strip():
        out.append(buf.strip())
    return out


def base_text_rule(pre, body):
    """Light-mode rules whose text colour can only be meant for dark surfaces
    (mid/light grays that fail on white, or translucent white). On Dim's
    lighter charcoal they can slip under 4.5:1, so lift them for Dim only."""
    decls = []
    for prop, val in split_decls(body):
        if prop.lower() != "color":
            continue
        m = COLOR_RE.fullmatch(val.replace("!important", "").strip())
        if not m:
            continue
        r, g, b, a = parse_color(m.group(0))
        h, l, sat = colorsys.rgb_to_hls(r / 255, g / 255, b / 255)
        L = lum(r, g, b)
        imp = " !important" if "!important" in val else ""
        if L >= 0.8 and a < 0.8:
            decls.append(f"color:{fmt(r, g, b, 0.82)}{imp}")
        elif 0.2 <= L < 0.6 and sat < 0.3 and a >= 0.95:
            out = ensure_text(r, g, b)
            if out:
                decls.append(f"color:{fmt(*out, 1)}{imp}")
    if not decls:
        return None
    sels = []
    for sel in split_selectors(pre):
        if not sel or sel.startswith(("html", ":root", "body")) or ":root" in sel or "[data-theme" in sel:
            continue
        sels.append('html[data-theme="dark"] ' + sel)
    if not sels:
        return None
    return tuple(sels), ";".join(decls)


def dim_rules(css, memo):
    """Return the list of (media, rule) Dim overrides for one CSS string."""
    if css in memo:
        return memo[css]
    out = []

    def walk(items, media):
        for pre, body in items:
            if isinstance(body, list):
                walk(body, media + (pre,))
                continue
            if pre.startswith("@"):
                continue
            sels = [s for s in split_selectors(pre) if DARK_ATTR.search(s)]
            if not sels:
                base = base_text_rule(pre, body)
                if base:
                    out.append((media,) + base)
                continue
            # Re-emit every colour declaration (changed or not) so the Dark
            # cascade order survives the specificity boost; skip rules with
            # nothing changed AND no colour declarations at all.
            decls, any_changed = [], False
            for prop, val in split_decls(body):
                if not COLOR_PROPS.match(prop):
                    continue
                new = map_value(prop, val)
                if new is not None:
                    any_changed = True
                    decls.append(f"{prop}:{new}")
                elif COLOR_RE.search(val) or "var(" in val or val.lower().startswith(("transparent", "inherit", "currentcolor", "none", "#", "rgb", "white", "black")):
                    decls.append(f"{prop}:{val}")
            if decls:
                out.append((media, tuple(sels), ";".join(decls)))

    walk(parse(strip_comments(css)), ())
    memo[css] = out
    return out


def scope(sel, group):
    m = DARK_ATTR.search(sel)
    tag = '[data-shade="dim"]' + (f'[data-dimg~="{group}"]' if group else "[data-dimg]")
    return sel[:m.end()] + tag + sel[m.end():]


def build():
    """Rules shared by every dark-mode page are emitted globally; all others are
    scoped to a group tag (data-dimg on <html>) so one page's tokens never leak
    into another page that does not define them."""
    css_cache, memo = {}, {}
    rule_pages, order, dark_pages = {}, [], []
    for path in iter_pages():
        css = page_css(path, css_cache)
        if not DARK_ATTR.search(css):
            continue
        key = page_key(path)
        dark_pages.append(key)
        seen = set()
        for r in dim_rules(css, memo):
            if r in seen:
                continue
            seen.add(r)
            if r not in rule_pages:
                rule_pages[r] = []
                order.append(r)
            rule_pages[r].append(key)

    n_all = len(dark_pages)
    sets = {}
    for r in order:
        pages = rule_pages[r]
        if len(pages) == n_all:
            continue
        sets.setdefault(frozenset(pages), None)
    # biggest groups get the shortest ids
    ranked = sorted(sets, key=lambda s: (-len(s), sorted(s)[0]))
    def b36(n):
        a = "0123456789abcdefghijklmnopqrstuvwxyz"
        o = ""
        while True:
            n, r = divmod(n, 36)
            o = a[r] + o
            if n == 0:
                return o
    gid = {s: b36(i) for i, s in enumerate(ranked)}
    page_groups = {k: [] for k in dark_pages}
    for s, g in gid.items():
        for k in s:
            page_groups[k].append(g)

    blocks, morder = {}, []
    for r in order:
        media, sels, decls = r
        pages = rule_pages[r]
        g = None if len(pages) == n_all else gid[frozenset(pages)]
        rule = ",".join(scope(s, g) for s in sels) + "{" + decls + "}"
        if media not in blocks:
            blocks[media] = []
            morder.append(media)
        if rule not in blocks[media]:
            blocks[media].append(rule)

    lines = [
        "/* theme-dim.css — GENERATED by build_theme_dim.py. Do not edit by hand.",
        "   Dim = html[data-theme=\"dark\"][data-shade=\"dim\"]: soft charcoal surfaces,",
        "   text re-checked to WCAG AA. Page-specific rules are scoped with",
        "   [data-dimg~=\"id\"] (set per page by the theme bootstrap). */",
        'html[data-theme="dark"][data-shade="dim"]{color-scheme:dark}',
    ]
    count = 0
    for media in morder:
        rules = blocks[media]
        count += len(rules)
        body = "\n".join(rules)
        for m in reversed(media):
            body = f"{m}{{\n{body}\n}}"
        lines.append(body)
    groups = {k: " ".join(v) for k, v in sorted(page_groups.items()) if v}
    return "\n".join(lines) + "\n", count, groups


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--check", action="store_true")
    args = ap.parse_args()
    css, count, groups = build()
    gjson = json.dumps(groups, indent=0, sort_keys=True) + "\n"
    if args.check:
        cur = OUT.read_text(encoding="utf-8") if OUT.exists() else ""
        curg = MAP_OUT.read_text(encoding="utf-8") if MAP_OUT.exists() else ""
        if cur != css or curg != gjson:
            print(f"theme-dim.css is stale ({count} rules) — run build_theme_dim.py")
            sys.exit(1)
        print(f"theme-dim.css up to date ({count} rules)")
        return
    OUT.write_text(css, encoding="utf-8")
    MAP_OUT.write_text(gjson, encoding="utf-8")
    longest = max((len(v) for v in groups.values()), default=0)
    print(f"wrote {OUT.relative_to(REPO)} — {count} rules, {len(css)/1024:.1f} KB; "
          f"{len(groups)} pages tagged, longest tag {longest} chars")


if __name__ == "__main__":
    main()
