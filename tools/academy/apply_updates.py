#!/usr/bin/env python3
"""Academy "Updated since you read it" flags (Dr. William Gregory Rivero, Nov 27 2026). Idempotent.

Source of truth: data/academy-updates.json, a list of dated notes, one per substantive module change:

    {"page": "attending-nephrologist-06-electrolyte-emergencies.html", "date": "2026-11-27",
     "note": "Added an interactive case: Sodium 109 at 2 a.m.", "anchor": "sim"}

Log only changes a learner who already finished the module should come back for (new or changed content, figures,
cases, corrected clinical facts), not typo or layout fixes: every entry re-flags the module for past finishers.
The page's own article:modified_time is a placeholder on most Academy pages, so it is NOT used to decide anything;
this patcher sets it (and JSON-LD dateModified) to the newest logged update on pages that have one.

This patcher:
  1. fingerprints assets/academy-updates.js as assets/academy-updates.<hash>.js (older copies pruned; _headers caches
     /assets/academy-updates.* immutable);
  2. on each module page with entries, writes <script type="application/json" id="rcm-updates"> with that page's
     notes and tags the script; on each track hub (<track>.html) with any updated module, writes the per-module dates
     and tags the script; removes both from pages that no longer need them;
  3. syncs article:modified_time / dateModified on updated module pages.
The learner side (assets/academy-updates.js) compares each date with the quiz result saved on the learner's device.
Nothing leaves the device.

Run after every publish (publish_academy.py does, before build_schola.py, so the script joins the offline list).

    python3 tools/academy/apply_updates.py                 # apply
    python3 tools/academy/apply_updates.py --dry-run       # report only
    python3 tools/academy/apply_updates.py --add attending-nephrologist-06-electrolyte-emergencies.html \\
        "Added a figure on the potassium shift" --anchor physiology [--date 2026-11-28]   # log an update, then apply
"""
import argparse, datetime, hashlib, json, re, sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
ACADEMY = ROOT / "academy"
ASSETS = ROOT / "assets"
DATA = ROOT / "data" / "academy-updates.json"
NAME = "academy-updates"

TAG_RE = re.compile(r'\n?<script src="[^"]*assets/' + NAME + r'\.[0-9a-f]{10}\.js"[^>]*></script>')
JSON_RE = re.compile(r'\n?<script type="application/json" id="rcm-updates">.*?</script>', re.S)
MOD_RE = re.compile(r"^(.+?)-(\d\d)-.+\.html$")
MT_RE = re.compile(r'(<meta property="article:modified_time" content=")[^"]*(")')
DM_RE = re.compile(r'("dateModified":\s*")[^"]*(")')
DATE_RE = re.compile(r"^\d{4}-\d\d-\d\d$")


def manila_today():
    return datetime.datetime.now(datetime.timezone(datetime.timedelta(hours=8))).date().isoformat()


def load():
    if not DATA.exists():
        return {"updates": []}
    return json.loads(DATA.read_text(encoding="utf-8"))


def check(updates):
    """Validate entries; return {page: [entries]} or exit with the problems listed."""
    bad, by_page, today = [], {}, manila_today()
    for i, u in enumerate(updates):
        page, date, note = u.get("page", ""), u.get("date", ""), (u.get("note") or "").strip()
        f = ACADEMY / page
        if not MOD_RE.match(page):
            bad.append(f"#{i}: {page!r} is not a module page (<track>-NN-<slug>.html)")
        elif not f.exists():
            bad.append(f"#{i}: {page} not found in academy/")
        if not DATE_RE.match(date):
            bad.append(f"#{i}: date {date!r} is not YYYY-MM-DD")
        elif date > today:
            bad.append(f"#{i}: date {date} is in the future (Manila today is {today})")
        if not note:
            bad.append(f"#{i}: empty note")
        a = u.get("anchor")
        if a and f.exists() and f'id="{a}"' not in f.read_text(encoding="utf-8"):
            bad.append(f"#{i}: anchor #{a} not found in {page}")
        by_page.setdefault(page, []).append({k: u[k] for k in ("date", "note", "anchor") if u.get(k)})
    if bad:
        sys.exit("academy updates: fix data/academy-updates.json:\n  " + "\n  ".join(bad))
    for v in by_page.values():
        v.sort(key=lambda e: e["date"])
    return by_page


def fingerprint(dry):
    data = (ASSETS / (NAME + ".js")).read_bytes()
    out = f"{NAME}.{hashlib.sha256(data).hexdigest()[:10]}.js"
    if not dry:
        (ASSETS / out).write_bytes(data)
        for old in ASSETS.glob(NAME + ".*.js"):
            if old.name != out and re.fullmatch(re.escape(NAME) + r"\.[0-9a-f]{10}\.js", old.name):
                old.unlink()
    return out


def blob(obj):
    return json.dumps(obj, ensure_ascii=False, separators=(",", ":")).replace("</", "<\\/")


def add(args):
    page = args.add[0] if args.add[0].endswith(".html") else args.add[0] + ".html"
    doc = load()
    entry = {"page": page, "date": args.date or manila_today(), "note": args.add[1].strip()}
    if args.anchor:
        entry["anchor"] = args.anchor
    doc.setdefault("updates", []).append(entry)
    check(doc["updates"])   # refuse to save a bad entry
    if not args.dry_run:
        DATA.write_text(json.dumps(doc, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print(f"logged: {entry['date']} {page}: {entry['note']}")


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("--dry-run", action="store_true")
    ap.add_argument("--add", nargs=2, metavar=("PAGE", "NOTE"))
    ap.add_argument("--anchor")
    ap.add_argument("--date")
    args, _ = ap.parse_known_args(argv if argv is not None else sys.argv[1:])   # tolerate publish_academy.py's own flags
    if args.add:
        add(args)

    by_page = check(load().get("updates", []))
    hubs = {}
    for page, entries in by_page.items():
        hubs.setdefault(MOD_RE.match(page).group(1) + ".html", {})[page] = sorted({e["date"] for e in entries})

    hashed = fingerprint(args.dry_run)
    changed = 0
    for f in sorted(ACADEMY.glob("*.html")):
        old = f.read_text(encoding="utf-8")
        if "</body>" not in old:
            continue
        text = TAG_RE.sub("", JSON_RE.sub("", old))
        payload = None
        if f.name in by_page:
            payload = {"page": f.name, "updates": by_page[f.name]}
            newest = by_page[f.name][-1]["date"]
            text = MT_RE.sub(lambda m: m.group(1) + newest + "T00:00:00+08:00" + m.group(2), text, count=1)
            text = DM_RE.sub(lambda m: m.group(1) + newest + m.group(2), text, count=1)
        elif f.name in hubs:
            payload = {"hub": True, "modules": hubs[f.name]}
        if payload:
            i = text.rfind("</body>")
            text = (text[:i] + f'<script type="application/json" id="rcm-updates">{blob(payload)}</script>\n'
                    f'<script src="../assets/{hashed}" defer></script>\n' + text[i:])
        if text != old:
            changed += 1
            if not args.dry_run:
                f.write_text(text, encoding="utf-8")
    print(f"academy updates ({hashed}): {len(by_page)} updated module(s) on {len(hubs)} track hub(s); "
          f"{changed} page(s) changed" + (" [dry run]" if args.dry_run else ""))


if __name__ == "__main__":
    main()
