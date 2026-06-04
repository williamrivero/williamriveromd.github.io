#!/usr/bin/env python3
"""
patch_image_dblclick.py — williamriveromd.com

Lets readers open any guide image at full size in a new browser tab by
double-clicking (desktop) or double-tapping (touch) it.

Changes per guide:
  1. Injects a small, self-contained inline <script> right before </body>
     that delegates a `dblclick` listener (desktop) and a manual double-tap
     detector (touch) on every <img> in the page. On a double-activation it
     opens the image's current source (`currentSrc` || `src`) in a new tab.

Behaviour notes:
  - Images inside an <a> link are left alone, so existing linked images keep
    their normal single-click navigation.
  - Data-URI / inline SVG sources without a real URL are skipped.
  - The snippet is wrapped by a unique marker comment so the script is fully
    idempotent: a guide already patched is detected and skipped.

Skips: nothing — every guides/*.html gets the handler.

Usage:
    python3 patch_image_dblclick.py
    python3 patch_image_dblclick.py --dry-run
    python3 patch_image_dblclick.py --guide anemia-management.html
"""

import argparse
from pathlib import Path


MARKER = "img-dblclick-open"

# Self-contained IIFE. Kept terse and dependency-free; safe to ship in every
# guide regardless of which other scripts are present.
SNIPPET = (
    '<script>/* ' + MARKER + ': double-click / double-tap an image to open it '
    'full-size in a new tab */\n'
    '(function(){\n'
    '  function openImg(img){\n'
    '    var src=img.currentSrc||img.src;\n'
    '    if(!src||src.indexOf("data:")===0)return;\n'
    '    window.open(src,"_blank","noopener");\n'
    '  }\n'
    '  function imgFrom(e){\n'
    '    var t=e.target;\n'
    '    if(!t||!t.closest)return null;\n'
    '    var img=t.closest("img");\n'
    '    if(!img||img.closest("a"))return null;\n'
    '    return img;\n'
    '  }\n'
    '  document.addEventListener("dblclick",function(e){\n'
    '    var img=imgFrom(e);\n'
    '    if(img)openImg(img);\n'
    '  });\n'
    '  var lastTap=0,lastImg=null;\n'
    '  document.addEventListener("touchend",function(e){\n'
    '    var img=imgFrom(e);\n'
    '    if(!img){lastTap=0;lastImg=null;return;}\n'
    '    var now=Date.now();\n'
    '    if(now-lastTap<350&&lastImg===img){\n'
    '      e.preventDefault();\n'
    '      openImg(img);\n'
    '      lastTap=0;lastImg=null;\n'
    '    }else{lastTap=now;lastImg=img;}\n'
    '  },{passive:false});\n'
    '})();</script>\n'
)


def find_project_dir(script_path: Path) -> Path:
    for candidate in [script_path.parent, script_path.parent.parent]:
        if (candidate / "guides").is_dir() and (candidate / "index.html").exists():
            return candidate
    raise FileNotFoundError("Cannot find project root. Run from the repo directory.")


def patch_guide(path: Path, dry_run: bool = False) -> str:
    if not path.exists():
        return "missing"
    text = path.read_text(encoding="utf-8")

    if MARKER in text:
        return "unchanged"

    if "</body>" not in text:
        return "no </body>"

    # Insert just before the final </body>.
    idx = text.rfind("</body>")
    new_text = text[:idx] + SNIPPET + text[idx:]

    if not dry_run:
        path.write_text(new_text, encoding="utf-8")
    return "✓ dblclick handler added"


def main():
    parser = argparse.ArgumentParser(
        description=__doc__,
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    parser.add_argument("--dry-run", action="store_true", help="Preview changes without writing")
    parser.add_argument("--guide", metavar="FILENAME", help="Process one guide (e.g. anemia-management.html)")
    args = parser.parse_args()

    project_dir = find_project_dir(Path(__file__).resolve())
    guides_dir = project_dir / "guides"

    if args.guide:
        files = [guides_dir / args.guide]
    else:
        files = sorted(guides_dir.glob("*.html"))

    ok = skipped = 0
    for path in files:
        status = patch_guide(path, dry_run=args.dry_run)
        prefix = "DRY " if args.dry_run else ""
        print(f"{prefix}{path.name}: {status}")
        if status.startswith("✓"):
            ok += 1
        else:
            skipped += 1

    dry_label = "DRY RUN — " if args.dry_run else ""
    print(f"\n{dry_label}Done: {ok} patched, {skipped} skipped/unchanged")


if __name__ == "__main__":
    main()
