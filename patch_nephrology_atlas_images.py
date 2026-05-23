#!/usr/bin/env python3
"""
Convert PNG → WebP and wire images into guides/nephrology-atlas.html.
Run from repo root after all PNG files are present in images/.

Usage:
  python3 patch_nephrology_atlas_images.py
  python3 patch_nephrology_atlas_images.py --dry-run
"""

import argparse
import re
import sys
from pathlib import Path

try:
    from PIL import Image
    HAS_PIL = True
except ImportError:
    HAS_PIL = False

REPO_ROOT = Path(__file__).parent
IMAGES_DIR = REPO_ROOT / "images"
GUIDE_PATH = REPO_ROOT / "guides" / "nephrology-atlas.html"

# Cards where loading="eager" should be used (first visible card in first tab)
EAGER_IDS = {"a1"}

# Alt text per image filename (derived from card titles)
ALT_TEXT = {
    "kidney-gross-anatomy-2d.png": "Kidney gross anatomy — 2D diagram with labeled cortex, medulla, pelvis and calyces",
    "kidney-gross-anatomy-3d.png": "Kidney gross anatomy — 3D rendering showing external surface and cut section",
    "kidney-vascular-supply-2d.png": "Kidney vascular supply — 2D diagram of renal artery segmental branches",
    "kidney-vascular-supply-3d.png": "Kidney vascular supply — 3D rendering of arcuate and interlobular vessels",
    "nephron-anatomy-functional-2d.png": "Nephron anatomy functional diagram — glomerulus through collecting duct with labeled segments",
    "glomerular-barrier-3d.png": "Glomerular filtration barrier — 3D cross-section of podocyte foot processes and GBM",
    "kidney-retroperitoneal-3d.png": "Kidney retroperitoneal position — 3D anatomy showing T12–L3 vertebral relationship",
    "kidney-collecting-system-hybrid-v2.png": "Kidney collecting system — hybrid diagram of calyces, renal pelvis and ureteropelvic junction",
    "kidney-cyst-simple-vs-complex-hybrid.png": "Simple vs complex renal cyst — Bosniak classification hybrid diagram",
    "horseshoe-kidney-3d.png": "Horseshoe kidney — 3D anatomy showing isthmus fusion and malrotation",
    "renal-agenesis-unilateral-hybrid.png": "Unilateral renal agenesis — hybrid illustration with compensatory hypertrophy",
    "adpkd-gross-architecture-3d.png": "ADPKD gross architecture — 3D bilateral polycystic kidneys with replacing cysts",
    "duplex-collecting-system-hybrid.png": "Duplex collecting system — hybrid diagram of bifid ureter and Weigert-Meyer rule",
    "renal-cell-carcinoma-cross-section-3d.png": "Renal cell carcinoma cross-section — 3D tumor architecture with vascular invasion",
    "bilateral-medical-renal-disease-hybrid.png": "Bilateral medical renal disease — hybrid comparison of common nephropathies",
    "kidney-systemic-disease-comparison-panel.png": "Systemic disease comparison panel — diabetic nephropathy, lupus nephritis, amyloidosis",
    "renal-artery-stenosis-anatomy-hybrid-v2.png": "Renal artery stenosis anatomy — hybrid diagram of atherosclerotic vs FMD lesions",
    "nephrocalcinosis-anatomy-hybrid.png": "Nephrocalcinosis anatomy — hybrid diagram of cortical and medullary calcium deposits",
    "hydronephrosis-anatomy-hybrid.png": "Hydronephrosis anatomy — hybrid cross-section showing calyceal dilation grades",
    "bph-upstream-obstructive-effects-hybrid.png": "BPH upstream obstructive cascade — hybrid diagram from prostate to bilateral hydronephrosis",
    "percutaneous-kidney-biopsy-v2.png": "Percutaneous kidney biopsy — US-guided technique with lower-pole targeting",
    "nephrostomy-pcn-insertion-v2.png": "Percutaneous nephrostomy insertion — Seldinger technique with pigtail in renal pelvis",
    "eswl-lithotripsy-v2.png": "ESWL lithotripsy — shock wave physics and patient positioning diagram",
    "dj-stent-insertion-v2.png": "Double-J stent insertion — retrograde cystoscopic technique step-by-step",
    "tenckhoff-catheter-insertion-v2.png": "Tenckhoff catheter insertion — surgical technique with dual-cuff positioning",
    "peritoneal-dialysis-fluid-exchange-v2.png": "Peritoneal dialysis fluid exchange — Fill–Dwell–Drain cycle with membrane transport",
    "ijcath-temporary-insertion-v2.png": "IJ temporary catheter insertion — US-guided Seldinger with CXR tip verification",
    "permcath-tunneled-insertion-v2.png": "Tunneled permcath insertion — subcutaneous tunnel and Dacron cuff positioning",
    "av-fistula-creation-maturation-v2.png": "AV fistula creation and maturation — radiocephalic anastomosis and Rule of 6s",
    "av-graft-placement-v2.png": "AV graft placement — PTFE loop configuration and venous anastomosis failure mode",
    "nephrectomy-procedure-v2.png": "Nephrectomy procedure — VAU ligation order, simple/radical/partial resection types",
    "embryo-stage1-pronephros.png": "Pronephros — Week 3–4 cervical intermediate mesoderm and Wolffian duct origin",
    "embryo-stage2-mesonephros.png": "Mesonephros — Week 4–6 Wolffian duct and male reproductive structure derivatives",
    "embryo-stage3-ureteric-bud-induction.png": "Ureteric bud induction — GDNF/RET signaling and metanephric mesenchyme Week 5–6",
    "embryo-stage4-branching-morphogenesis.png": "Branching morphogenesis — 15 rounds of dichotomous ureteric bud branching Week 6–10",
    "embryo-stage5-nephrogenesis-met.png": "Nephrogenesis MET sequence — cap mesenchyme to mature nephron Week 7–36",
    "embryo-stage6-renal-ascent-rotation.png": "Renal ascent and rotation — sacral to lumbar L1–L2 with 90° medial rotation Week 6–9",
    "embryo-stage7-fetal-kidney-mature.png": "Mature fetal kidney — fetal lobulation and urine production from Week 10",
    "embryo-stage8-anomaly-failure-map.png": "Congenital anomaly failure-point map — developmental timeline with branching defects",
}

def convert_to_webp(png_path: Path) -> Path:
    """Convert PNG to WebP; return WebP path."""
    webp_path = png_path.with_suffix(".webp")
    if webp_path.exists():
        print(f"  [skip] {webp_path.name} already exists")
        return webp_path
    if not HAS_PIL:
        print("  [warn] Pillow not installed — skipping WebP conversion")
        return webp_path
    img = Image.open(png_path).convert("RGBA")
    img.save(webp_path, "WEBP", quality=88, method=6)
    size_kb = webp_path.stat().st_size // 1024
    print(f"  [webp] {png_path.name} → {webp_path.name} ({size_kb} KB)")
    return webp_path


def make_picture_tag(filename: str, loading: str = "lazy") -> str:
    stem = Path(filename).stem
    alt = ALT_TEXT.get(filename, stem.replace("-", " ").title())
    return (
        f'<picture>'
        f'<source srcset="../images/{stem}.webp" type="image/webp">'
        f'<img src="../images/{filename}" alt="{alt}" '
        f'loading="{loading}" style="width:100%;height:auto;display:block;">'
        f'</picture>'
    )


def wire_images(html: str, available: set, dry_run: bool) -> tuple[str, int, int]:
    """
    Replace .img-overlay placeholder blocks with <picture> tags.
    Returns (new_html, wired_count, skipped_count).
    """
    wired = 0
    skipped = 0

    # Pattern for card-img-zone placeholder
    # <div class="card-img-zone"><div class="img-overlay">...<div class="ph-filename">FILENAME.png</div></div></div>
    def replace_card_zone(m):
        nonlocal wired, skipped
        inner = m.group(0)
        fn_match = re.search(r'ph-filename">([^<]+)<', inner)
        if not fn_match:
            return inner
        filename = fn_match.group(1).strip()
        if filename not in available:
            skipped += 1
            return inner
        loading = "eager" if filename in {ALT_TEXT} else "lazy"
        pic = make_picture_tag(filename)
        wired += 1
        return f'<div class="card-img-zone">{pic}</div>'

    # Pattern for wide-card-img placeholder
    def replace_wide_zone(m):
        nonlocal wired, skipped
        inner = m.group(0)
        fn_match = re.search(r'ph-filename">([^<]+)<', inner)
        style_match = re.search(r'style="([^"]*)"', inner)
        style = f' style="{style_match.group(1)}"' if style_match else ''
        if not fn_match:
            return inner
        filename = fn_match.group(1).strip()
        if filename not in available:
            skipped += 1
            return inner
        pic = make_picture_tag(filename)
        wired += 1
        return f'<div class="wide-card-img"{style}>{pic}</div>'

    # Replace card-img-zone blocks that contain img-overlay
    html = re.sub(
        r'<div class="card-img-zone"><div class="img-overlay">.*?</div></div>',
        replace_card_zone,
        html,
        flags=re.DOTALL
    )

    # Replace wide-card-img blocks that contain img-overlay
    html = re.sub(
        r'<div class="wide-card-img"[^>]*><div class="img-overlay">.*?</div></div>',
        replace_wide_zone,
        html,
        flags=re.DOTALL
    )

    return html, wired, skipped


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--dry-run", action="store_true")
    args = parser.parse_args()

    if not GUIDE_PATH.exists():
        print(f"ERROR: {GUIDE_PATH} not found")
        sys.exit(1)

    # Find which of the target PNGs are present
    target_pngs = list(ALT_TEXT.keys())
    available_pngs = {f for f in target_pngs if (IMAGES_DIR / f).exists()}
    missing_pngs = set(target_pngs) - available_pngs

    print(f"\nNephrology Atlas Image Pipeline")
    print(f"{'='*50}")
    print(f"Images dir : {IMAGES_DIR}")
    print(f"Guide      : {GUIDE_PATH}")
    print(f"PNGs found : {len(available_pngs)} / {len(target_pngs)}")
    if missing_pngs:
        print(f"Missing    : {sorted(missing_pngs)}")
    print()

    if not available_pngs:
        print("No target PNGs found in images/ — push images first, then re-run.")
        sys.exit(0)

    # Convert PNGs → WebP
    if not args.dry_run:
        print("Converting PNG → WebP...")
        for fn in sorted(available_pngs):
            convert_to_webp(IMAGES_DIR / fn)
        print()

    # Wire images into HTML
    html = GUIDE_PATH.read_text(encoding="utf-8")
    new_html, wired, skipped = wire_images(html, available_pngs, args.dry_run)

    print(f"Images wired : {wired}")
    print(f"Skipped (missing PNG) : {skipped}")

    if args.dry_run:
        print("\n[dry-run] No files written.")
        return

    if wired > 0:
        GUIDE_PATH.write_text(new_html, encoding="utf-8")
        print(f"\nWritten: {GUIDE_PATH}")
    else:
        print("\nNo changes made.")


if __name__ == "__main__":
    main()
