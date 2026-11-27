#!/usr/bin/env python3
"""Academy inline tools: Calculo calculators and Dosis lookups inside modules (Dr. William Gregory Rivero, Nov 27 2026).
Idempotent.

Placements live in data/academy-tools.json: {"page", "section", "tool": "ktv" | "sodium" | "dose", "opts"?}. Each tool
goes at the END of that module section, between <!-- RCM-TOOL-START <tool> --> / <!-- RCM-TOOL-END --> markers, as a
<form class="rcm-tool"> (Listen skips forms) whose static content is a link to the full Calculo / Dosis tool, so the
page still works without JavaScript.

This patcher:
  1. fingerprints assets/academy-tools.js as assets/academy-tools.<hash>.js (older copies pruned; _headers caches
     /assets/academy-tools.* and /assets/academy-kidney-doses.* immutable);
  2. builds assets/academy-kidney-doses.<hash>.js (window.RCM_KDOSE) from the Drug Index's published, APPROVED kidney
     tiles (drugs/interactions.json "k", the same data the interaction checker shows) plus each drug's display name and
     Philippine brands (drugs/search-index.json). No clinical text is written here: bands are copied as published;
  3. writes the markers, tags both scripts on pages that have a tool, and removes everything from pages that no longer do.
Run after every publish (publish_academy.py does, before build_schola.py, so the scripts join Schola's offline list),
and after the Drug Index is regenerated (so newly approved kidney dosing reaches the modules).

    python3 tools/academy/apply_tools.py             # apply
    python3 tools/academy/apply_tools.py --dry-run   # report only
"""
import hashlib, html, json, re, sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
ACADEMY = ROOT / "academy"
ASSETS = ROOT / "assets"
DATA = ROOT / "data" / "academy-tools.json"
NAME, KD = "academy-tools", "academy-kidney-doses"
TOOLS = {"ktv": ("Dialysis adequacy (Kt/V and URR) in Calculo", "/guides/calc-dialysis-adequacy-ktv"),
         "sodium": ("Sodium correction rate in Calculo", "/guides/calc-sodium-correction-rate"),
         "dose": ("Kidney dosing in the Dosis Drug Index", "/drugs/")}
BRANDS_MAX = 15

TAG_RE = re.compile(r'\n?<script src="[^"]*assets/(?:' + NAME + "|" + KD + r')\.[0-9a-f]{10}\.js"[^>]*></script>')
BLOCK_RE = re.compile(r"\n?<!-- RCM-TOOL-START [a-z]+ -->.*?<!-- RCM-TOOL-END -->", re.S)


def write_hashed(name, data, dry):
    out = f"{name}.{hashlib.sha256(data).hexdigest()[:10]}.js"
    if not dry:
        (ASSETS / out).write_bytes(data)
        for old in ASSETS.glob(name + ".*.js"):
            if old.name != out and re.fullmatch(re.escape(name) + r"\.[0-9a-f]{10}\.js", old.name):
                old.unlink()
    return out


def kidney_doses():
    k = json.loads((ROOT / "drugs" / "interactions.json").read_text(encoding="utf-8"))["k"]
    idx = {e["s"]: e for e in json.loads((ROOT / "drugs" / "search-index.json").read_text(encoding="utf-8"))}
    d = {}
    for slug in sorted(k):
        e = idx.get(slug, {})
        if not (ROOT / "drugs" / f"{slug}.html").exists():
            continue   # never link to a page that does not exist
        seen, brands = set(), []
        for b in e.get("b", []):
            if b.lower() not in seen and b.lower() != (e.get("n") or "").lower():
                seen.add(b.lower()); brands.append(b)
            if len(brands) >= BRANDS_MAX:
                break
        d[slug] = {"n": e.get("n") or slug.replace("-", " ").capitalize(), "b": brands, "k": k[slug]}
    body = json.dumps({"v": 1, "d": d}, ensure_ascii=False, separators=(",", ":"))
    return ("/* Renal Care Academy: reviewed kidney dosing from the Dosis Drug Index (drugs/interactions.json), "
            "built by tools/academy/apply_tools.py. Do not edit. */\nwindow.RCM_KDOSE=" + body + ";\n").encode("utf-8"), len(d)


def block(entry):
    tool, opts = entry["tool"], entry.get("opts") or {}
    label, href = TOOLS[tool]
    o = html.escape(json.dumps(opts, ensure_ascii=False, separators=(",", ":")), quote=True)
    return (f'\n<!-- RCM-TOOL-START {tool} --><form class="rcm-tool" data-tool="{tool}" data-opts="{o}" '
            f'aria-label="Interactive tool" onsubmit="return false"><p class="rt-sub">Try this in '
            f'<a href="{href}">{label}</a>.</p></form><!-- RCM-TOOL-END -->')


def insert(text, section, blk, page):
    m = re.search(r'<section\b[^>]*\bid="' + re.escape(section) + r'"[^>]*>', text)
    if not m:
        sys.exit(f"academy tools: section #{section} not found in {page}")
    end = text.find("</section>", m.end())
    if end < 0 or "<section" in text[m.end():end]:
        sys.exit(f"academy tools: section #{section} in {page} is nested or unclosed")
    return text[:end] + blk + "\n" + text[end:]


def main(argv=None):
    dry = "--dry-run" in (argv if argv is not None else sys.argv[1:])
    entries = json.loads(DATA.read_text(encoding="utf-8"))["tools"] if DATA.exists() else []
    by_page = {}
    for e in entries:
        if e.get("tool") not in TOOLS:
            sys.exit(f"academy tools: unknown tool {e.get('tool')!r} for {e.get('page')}")
        if not (ACADEMY / e["page"]).exists():
            sys.exit(f"academy tools: {e['page']} not found in academy/")
        by_page.setdefault(e["page"], []).append(e)

    hashed = write_hashed(NAME, (ASSETS / (NAME + ".js")).read_bytes(), dry)
    kd_bytes, n_drugs = kidney_doses()
    kd = write_hashed(KD, kd_bytes, dry)
    changed = 0
    for f in sorted(ACADEMY.glob("*.html")):
        old = f.read_text(encoding="utf-8")
        if "</body>" not in old:
            continue
        text = TAG_RE.sub("", BLOCK_RE.sub("", old))
        es = by_page.get(f.name)
        if es:
            for e in es:
                text = insert(text, e["section"], block(e), f.name)
            tags = ""
            if any(e["tool"] == "dose" for e in es):
                tags += f'<script src="../assets/{kd}" defer></script>\n'
            tags += f'<script src="../assets/{hashed}" defer></script>\n'
            i = text.rfind("</body>")
            text = text[:i] + tags + text[i:]
        if text != old:
            changed += 1
            if not dry:
                f.write_text(text, encoding="utf-8")
    print(f"academy tools ({hashed}, {kd}: {n_drugs} reviewed drugs): {len(entries)} tool(s) on {len(by_page)} module(s); "
          f"{changed} page(s) changed" + (" [dry run]" if dry else ""))


if __name__ == "__main__":
    main()
