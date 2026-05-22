#!/usr/bin/env python3
"""
El Niño Hero Images — WebP Conversion + HTML Injection
Run this from the repo root after dropping JPGs into images/

Usage:
    python3 inject_el_nino_images.py
"""

import os, subprocess, re
from pathlib import Path

REPO   = Path(__file__).parent
IMAGES = REPO / "images"
GUIDE  = REPO / "guides" / "el-nino-heat-dialysis.html"

FILES = {
    "el-nino-heat-dialysis-hero":              "hero",
    "el-nino-eskd-thermoregulation-pathophys": "pathophys",
    "el-nino-four-heat-emergencies-patient":   "emergencies",
    "el-nino-clinician-rapid-heat-protocol":   "protocol",
    "el-nino-brownout-water-rationing-dialysis": "brownout",
    "el-nino-fluid-management-heat-paradox":   "fluid",
}

# ── 1. Convert all new JPGs to WebP ────────────────────────────────────────
print("=== WebP Conversion ===")
for stem in FILES:
    jpg = IMAGES / f"{stem}.jpg"
    webp = IMAGES / f"{stem}.webp"
    if jpg.exists() and not webp.exists():
        result = subprocess.run(
            ["cwebp", "-q", "85", str(jpg), "-o", str(webp)],
            capture_output=True, text=True
        )
        if result.returncode == 0:
            kb_jpg  = jpg.stat().st_size  // 1024
            kb_webp = webp.stat().st_size // 1024
            saving  = round((1 - kb_webp/kb_jpg) * 100)
            print(f"  ✓ {stem}.webp  ({kb_jpg}KB → {kb_webp}KB, -{saving}%)")
        else:
            print(f"  ✗ cwebp failed for {stem}: {result.stderr[:100]}")
    elif webp.exists():
        print(f"  · Already exists: {stem}.webp")
    else:
        print(f"  ! Missing source: {jpg.name} — skipping")

# ── 2. Patch HTML ──────────────────────────────────────────────────────────
print("\n=== HTML Injection ===")
html = GUIDE.read_text(encoding="utf-8")
original = html

# ── 2a. HERO — inject as CSS background-image overlay on .hero section ─────
hero_jpg  = IMAGES / "el-nino-heat-dialysis-hero.jpg"
hero_webp = IMAGES / "el-nino-heat-dialysis-hero.webp"

if (hero_jpg.exists() or hero_webp.exists()):
    # Check if hero image already injected
    if "el-nino-heat-dialysis-hero" not in html:
        # Find the opening <section class="hero"> and add background style
        old_hero_tag = '<section class="hero">'
        new_hero_tag = (
            '<section class="hero" style="'
            'background-image:url(../images/el-nino-heat-dialysis-hero.webp),'
            'linear-gradient(135deg,#1a2c4e 0%,#0f1e35 100%);'
            'background-size:cover;background-position:center top;'
            'background-blend-mode:multiply;">'
        )
        if old_hero_tag in html:
            html = html.replace(old_hero_tag, new_hero_tag, 1)
            print("  ✓ Hero: injected as background-image on .hero section")
        else:
            print("  ! Hero: could not find <section class=\"hero\"> — check markup")
    else:
        print("  · Hero: already injected")
else:
    print("  ! Hero image not found in images/ — skipping")

# ── 2b. PATHOPHYSIOLOGY — replace placeholder in #paradox section ──────────
PATHOPHYS_PLACEHOLDER = '<!-- PATHOPHYS_IMAGE_PLACEHOLDER -->'
PATHOPHYS_FIGURE = (
    '\n  <figure style="margin:24px 0;">\n'
    '    <picture>\n'
    '      <source srcset="../images/el-nino-eskd-thermoregulation-pathophys.webp" type="image/webp">\n'
    '      <img src="../images/el-nino-eskd-thermoregulation-pathophys.jpg"\n'
    '           loading="lazy" width="1344" height="1024"\n'
    '           alt="ESKD thermoregulation pathophysiology — why heat is dangerous in dialysis, fluid overload paradox, hyperkalemia risk"\n'
    '           style="border-radius:12px;display:block;width:100%;height:auto;">\n'
    '    </picture>\n'
    '    <figcaption class="illus-caption">Why dialysis patients cannot follow standard heat advice — impaired thermoregulation, anuria, and the overload-thirst paradox.</figcaption>\n'
    '  </figure>\n'
)

# ── 2c. EMERGENCIES — inject after #emergencies section heading ─────────────
EMERG_PLACEHOLDER = '<!-- EMERGENCIES_IMAGE_PLACEHOLDER -->'
EMERG_FIGURE = (
    '\n  <figure style="margin:24px 0;">\n'
    '    <picture>\n'
    '      <source srcset="../images/el-nino-four-heat-emergencies-patient.webp" type="image/webp">\n'
    '      <img src="../images/el-nino-four-heat-emergencies-patient.jpg"\n'
    '           loading="lazy" width="1792" height="1024"\n'
    '           alt="Four heat emergencies for dialysis patients — heat exhaustion, heat stroke, hyperkalemia, intradialytic hypotension"\n'
    '           style="border-radius:12px;display:block;width:100%;height:auto;">\n'
    '    </picture>\n'
    '    <figcaption class="illus-caption">Recognize and respond to the four heat emergencies: heat exhaustion, heat stroke, severe hyperkalemia, and intradialytic hypotension.</figcaption>\n'
    '  </figure>\n'
)

# ── 2d. CLINICIAN PROTOCOL ─────────────────────────────────────────────────
PROTOCOL_FIGURE = (
    '\n  <figure style="margin:24px 0;">\n'
    '    <picture>\n'
    '      <source srcset="../images/el-nino-clinician-rapid-heat-protocol.webp" type="image/webp">\n'
    '      <img src="../images/el-nino-clinician-rapid-heat-protocol.jpg"\n'
    '           loading="lazy" width="1024" height="1536"\n'
    '           alt="Clinician rapid heat protocol — pre-dialysis screen, dialysate 35°C, UF cap, heat emergency triage"\n'
    '           style="border-radius:12px;display:block;max-width:600px;margin:0 auto;height:auto;">\n'
    '    </picture>\n'
    '    <figcaption class="illus-caption" style="text-align:center;">Rapid heat protocol reference card — pre-session screen, intradialytic adjustments, and emergency triage for El Niño season.</figcaption>\n'
    '  </figure>\n'
)

# ── 2e. BROWNOUT ───────────────────────────────────────────────────────────
BROWNOUT_FIGURE = (
    '\n  <figure style="margin:24px 0;">\n'
    '    <picture>\n'
    '      <source srcset="../images/el-nino-brownout-water-rationing-dialysis.webp" type="image/webp">\n'
    '      <img src="../images/el-nino-brownout-water-rationing-dialysis.jpg"\n'
    '           loading="lazy" width="1792" height="1024"\n'
    '           alt="Brownout and water rationing survival guide for dialysis patients — power outage SOP, medication cold chain, water priorities"\n'
    '           style="border-radius:12px;display:block;width:100%;height:auto;">\n'
    '    </picture>\n'
    '    <figcaption class="illus-caption">Brownout and water rationing survival: power outage protocols for HD and PD patients, medication cold chain, and water priority hierarchy.</figcaption>\n'
    '  </figure>\n'
)

# ── 2f. FLUID PARADOX ──────────────────────────────────────────────────────
FLUID_FIGURE = (
    '\n  <figure style="margin:24px 0;">\n'
    '    <picture>\n'
    '      <source srcset="../images/el-nino-fluid-management-heat-paradox.webp" type="image/webp">\n'
    '      <img src="../images/el-nino-fluid-management-heat-paradox.jpg"\n'
    '           loading="lazy" width="1792" height="1024"\n'
    '           alt="Dialysis fluid management in heat — the thirsty AND fluid-overloaded paradox, cooling without drinking strategies"\n'
    '           style="border-radius:12px;display:block;width:100%;height:auto;">\n'
    '    </picture>\n'
    '    <figcaption class="illus-caption">The dialysis heat paradox — thirsty and fluid-overloaded simultaneously — and practical cooling strategies that require no extra fluid intake.</figcaption>\n'
    '  </figure>\n'
)

# ── Inject section images by finding their section IDs ─────────────────────
INJECTIONS = [
    # (section_id, image_stem, figure_html, anchor_pattern)
    ("paradox",    "el-nino-eskd-thermoregulation-pathophys",   PATHOPHYS_FIGURE,  '</h2>\n'),
    ("emergencies","el-nino-four-heat-emergencies-patient",     EMERG_FIGURE,      '</h2>\n'),
    ("md-quickprotocol","el-nino-clinician-rapid-heat-protocol", PROTOCOL_FIGURE,  '</h2>\n'),
    ("power",      "el-nino-brownout-water-rationing-dialysis", BROWNOUT_FIGURE,   '</h2>\n'),
    ("fluid",      "el-nino-fluid-management-heat-paradox",     FLUID_FIGURE,      '</h2>\n'),
]

for section_id, stem, figure_html, anchor in INJECTIONS:
    img_file = IMAGES / f"{stem}.jpg"
    if not img_file.exists():
        print(f"  ! {stem}.jpg not found — skipping #{section_id}")
        continue
    if stem in html:
        print(f"  · Already injected: #{section_id}")
        continue

    # Find section and inject after the first </h2> within it
    section_marker = f'id="{section_id}"'
    idx = html.find(section_marker)
    if idx == -1:
        print(f"  ! Section #{section_id} not found in HTML")
        continue
    h2_end = html.find('</h2>', idx)
    if h2_end == -1:
        print(f"  ! No </h2> found in #{section_id}")
        continue
    insert_at = h2_end + len('</h2>')
    html = html[:insert_at] + figure_html + html[insert_at:]
    print(f"  ✓ Injected: {stem} into #{section_id}")

# ── 3. Write patched HTML ──────────────────────────────────────────────────
if html != original:
    GUIDE.write_text(html, encoding="utf-8")
    print(f"\n  ✓ Guide updated: {GUIDE.name}")
else:
    print("\n  · No changes needed — guide already up to date")

print("\nDone. Run: git add -A && git commit -m 'feat: add El Niño heat guide images' && git push")
