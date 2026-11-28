"""Right side rail (desktop / tablet >= 1024 px) on the Emergency Readiness pages (Dr. Rivero, Nov 28 2026). Idempotent.

The Emergency Readiness home, the Emergency quick cards and the two practice labs are built by apply_emergency_cards.py
and apply_resus_lab.py from the landing page's tail, which drops the share bar and the side rail. This patcher adds them
back on those pages: assets/share-buttons.js (hero share row + Share tab) and the current fingerprinted
assets/guide-rail.<hash>.js (References on the quick cards page, Share everywhere, Graphics where there are figures).
It also repoints every academy page's guide-rail tag to the current fingerprint, so a changed guide-rail.js never leaves
academy pages pointing at a pruned file. In the Resuscitation Lab's shared monitor display (?display=1) the rail and the
share row are hidden.

Run after apply_emergency_cards.py and apply_resus_lab.py and before patch_share_slot.py (publish_academy.py does);
the sitemap workflow runs it after patch_guide_rail.py.

    python3 tools/academy/apply_readiness_rail.py
"""
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
ACADEMY = ROOT / "academy"
PAGES = ["emergency-readiness.html", "emergency-cards.html",
         "resuscitation-lab-practice.html", "disaster-preparedness-practice.html"]
SHARE = '<script src="../assets/share-buttons.js" defer></script>'
RAIL_RE = re.compile(r'<script src="\.\./assets/guide-rail(?:\.[0-9a-f]{10})?\.js" defer></script>')
DISPLAY_CSS = ('<style id="rl-rail-display">body.rl-display-mode .rcm-rail,body.rl-display-mode .rcm-drawer,'
               'body.rl-display-mode .rcm-scrim,body.rl-display-mode .rcm-share{display:none!important;}</style>')


def rail_tag():
    files = sorted(ROOT.glob("assets/guide-rail.*.js"))
    files = [f for f in files if re.fullmatch(r"guide-rail\.[0-9a-f]{10}\.js", f.name)]
    if len(files) != 1:
        sys.exit(f"apply_readiness_rail: expected one assets/guide-rail.<hash>.js, found {len(files)}; run patch_guide_rail.py")
    return f'<script src="../assets/{files[0].name}" defer></script>'


def main(argv=None):
    tag = rail_tag()
    changed = 0
    for f in sorted(ACADEMY.glob("*.html")):
        old = f.read_text(encoding="utf-8")
        text = old
        if f.name in PAGES:
            text = text.replace("\n" + SHARE, "").replace(SHARE, "")
            text = RAIL_RE.sub("", text)
            text = text.replace(DISPLAY_CSS, "")
            i = text.rfind("</body>")
            text = text[:i] + SHARE + "\n" + tag + "\n" + text[i:]
            if f.name.endswith("-practice.html"):
                j = text.find("</head>")
                text = text[:j] + DISPLAY_CSS + "\n" + text[j:]
            text = re.sub(r"\n{3,}(?=<script src=\"\.\./assets/share-buttons)", "\n", text)
        elif RAIL_RE.search(text):
            text = RAIL_RE.sub(tag, text)
        if text != old:
            changed += 1
            f.write_text(text, encoding="utf-8")
    print(f"apply_readiness_rail: {changed} page(s) updated")


if __name__ == "__main__":
    main()
