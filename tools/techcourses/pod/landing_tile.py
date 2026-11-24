#!/usr/bin/env python3
"""Keep the Physician-on-Duty card on the Academy landing page (academy/index.html) in step with the modules that are live.

Run from the repo root after building the course:  python3 tools/techcourses/pod/landing_tile.py
Idempotent. Rewrites only the POD card's count line and the POD quick-link count; touches nothing else on the page.
"""
import importlib.util
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
spec = importlib.util.spec_from_file_location("pod_course", Path(__file__).with_name("course.py"))
course = importlib.util.module_from_spec(spec)
spec.loader.exec_module(course)

mods = course.MODULES
live = [m for m in mods if m.get("status") != "planned"]
n, total = len(live), len(mods)
essentials = [m for m in mods if "Essentials" in str(m["tier"])]


def meta_line():
    if n >= total:
        return f"{total} modules &middot; three tiers &middot; end-of-course exam"
    if all("Essentials" in str(m["tier"]) for m in live) and n == len(essentials):
        return f"First-Shift Essentials: {n} modules open &middot; more in preparation"
    return f"{n} modules open &middot; more in preparation"


def main():
    p = ROOT / "academy" / "index.html"
    t = p.read_text(encoding="utf-8")
    line = meta_line()
    t2 = re.sub(r'(<b>Physician-on-Duty</b><span>.*?</span><span><strong>)(.*?)(</strong>)',
                lambda m: m.group(1) + line + m.group(3), t, count=1, flags=re.S)
    t2 = re.sub(r'(href="physician-on-duty\.html">.*?<strong>Physician-on-Duty</strong><small>)\d+ modules open(</small>)',
                lambda m: f"{m.group(1)}{n} modules open{m.group(2)}", t2, count=1, flags=re.S)
    if t2 != t:
        p.write_text(t2, encoding="utf-8")
    print(f"Physician-on-Duty landing card: {line.replace('&middot;', '·')}")


if __name__ == "__main__":
    main()
