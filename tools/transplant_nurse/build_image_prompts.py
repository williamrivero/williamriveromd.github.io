#!/usr/bin/env python3
"""Write docs/transplant-nurse/GPT-IMAGE-PROMPTS.md and image-manifest.json from content/images.py.

Hero prompts follow williamriveromd-hero-vignette v3; figure prompts follow williamriveromd-simple-figure v1.
Paste each block into the ChatGPT Image Generator, save the PNG under the FILE NAME shown, and drop the files in
images/ (or hand them over for processing). Pages pick up figures automatically on the next generator run.
"""
import importlib.util, json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
spec = importlib.util.spec_from_file_location("tn_images", ROOT / "tools/transplant_nurse/content/images.py")
I = importlib.util.module_from_spec(spec); spec.loader.exec_module(I)
OUT = ROOT / "docs" / "transplant-nurse"

NEG_HERO = """Avoid: busy layouts, collage overload, more than four supporting scenes, dozens of icons, tiny unreadable labels,
infographic clutter, duplicated people, repeated compositions, cropped circle, cropped objects, cropped anatomy, edge
clipping, objects touching the circular border, important content inside the title safe zone, baked-in text, titles,
captions, logos, watermarks, rectangular borders, frames, banners, dark / charcoal / black backgrounds, cartoon style,
neon, HDR, over-saturation, distorted hands or faces, implausible anatomy."""

NEG_FIG = """Avoid cartoon style, avoid clutter, avoid tiny unreadable labels, avoid AI gibberish text, avoid unrealistic anatomy,
avoid overprocessed HDR, avoid excessive saturation. NEVER use dark, navy, charcoal, or black backgrounds — light
backgrounds only. Use ONLY the sans-serif font Inter — no other fonts, no serif fonts, no decorative or handwritten
typefaces. Never omit the renalcarematters.com attribution."""

SCAFFOLD = {
    "A": ("Scaffold A — Clinical algorithm / flowchart", "2:3 portrait",
          "Clinical nephrology algorithm, KDIGO guideline flowchart aesthetic, white (#ffffff) background, title at top in bold navy (#0f1e2e) Inter. Rounded rectangular nodes: decision nodes teal (#1a6b72), action nodes navy, caution nodes amber (#b8860b), escalation nodes red (#b91c1c), optimal-path nodes renal green (#1f7a4d). Bold connecting arrows, maximum 3–4 branching levels, generous whitespace, mobile-readable labels."),
    "B": ("Scaffold B — Side-by-side comparison", "16:9 landscape",
          "Medical education comparison infographic, AJKD/NEJM graphical abstract style, white (#ffffff) background, title centered at top in bold navy (#0f1e2e) Inter, soft dashed dividers between equal rounded panels, ample negative space, mobile-readable labels ≥11 pt."),
    "C": ("Scaffold C — Horizontal step sequence", "16:9 landscape",
          "Clean clinical education infographic, white (#ffffff) background, title at top center in bold navy (#0f1e2e) Inter. Rounded rectangular cards in a single row on a very soft gray panel (#f3f4f6), connected by bold navy arrows; each card has a colored top accent band, a small line icon, a bold label and 1–3 short details. Generous whitespace, mobile-readable."),
    "D": ("Scaffold D — Single mechanism / one-panel poster", "16:9 landscape",
          "Medical pathophysiology infographic, AJKD/NEJM graphical abstract style, white (#ffffff) background, title at top in bold navy (#0f1e2e) Inter, subtitle in clinical teal (#1a6b72). Central semi-photorealistic diagram with labeled callouts in modular rounded cards and color-coded arrows; bottom strip with the clinical implication in navy. Ample negative space, no clutter."),
    "E": ("Scaffold E — Reference table / quick-look card", "1:1 square",
          "Clinical reference card, publication-grade nephrology design, white (#ffffff) background, bold navy title at top in Inter, compact well-organized grid, headers in teal (#1a6b72) on soft gray (#f3f4f6), alternating row fills, key items highlighted in amber or red where clinically significant, short footer takeaway."),
}


def hero_block(key, h):
    stem, arch, cam, people, scene = h
    who = "No people." if people in ("no people",) else ("Hands only, no faces." if people == "hands only" else f"People: {people}; Filipino, with features, ages, hairstyles, clothing and posture clearly different from other Academy heroes.")
    scaffold = "C anatomy" if arch.startswith("F") else ("B still-life" if people in ("no people", "hands only") else "A people")
    return f"""```
FILE NAME: {stem}.png
IMAGE TYPE: Circular vignette hero v3 — Scaffold {scaffold}
ASPECT RATIO: 1:1 (square — displayed inside an 85–90% inscribed circle with white margin)
PIXEL DIMENSIONS: 2048 × 2048
COMPOSITION ARCHETYPE: {arch}
CAMERA: {cam}
HUMAN VARIATION (vs. previous guide): {people if people in ('no people', 'hands only') else 'new cast; at least 12 traits differ (age, sex, face shape, hairstyle, hair length, build, skin tone within Filipino diversity, clothing style and color, accessories, posture, hand position, expression, setting)'}
AUDIENCE: clinicians (registered nurses)
VISUAL GOAL: One calm image that tells a nurse what this module is about at a glance.

PROMPT:
Square 1:1 {'semi-photorealistic 3D medical illustration' if arch.startswith('F') else 'photorealistic editorial photograph'} on a 2048×2048 canvas, composed to be displayed inside a CIRCULAR vignette occupying 85–90% of the canvas diameter with a visible WHITE BORDER around the full circle (the circle never touches the canvas edges). Composition archetype: {arch}. Camera: {cam}.
{who}
Scene: {scene}. Clean, bright modern Philippine hospital or home setting, soft natural daylight, gentle shallow depth of field.
Visual hierarchy: hero subject 60–70% of the circle; 2–4 supporting elements 20–30%; reserve a 20–25% TITLE SAFE ZONE of soft gradient, clean wall or blurred background on the left side of the circle (no faces, anatomy, icons, objects or callouts inside it).
Calm, reassuring, documentary-realistic color grade harmonizing with clinical teal #1a6b72 and navy #0f1e2e on a light background; soft falloff toward the rim. Full-bleed within the inscribed circle, no rectangular borders, frames or banners.
Absolutely NO text of any kind: no title, caption, label, readable writing on paper or screens, logo, or watermark.

NEGATIVE INSTRUCTIONS:
{NEG_HERO}

QUALITY CHECK:
Square 2048×2048; circle 85–90% with a visible white margin, never cropped; one dominant subject; 20–25% empty title-safe zone; Filipino context where people are shown; no text anywhere; crops cleanly inside the circle.
```"""


def fig_block(f):
    name, ratio, base = SCAFFOLD[f["scaffold"]]
    return f"""```
FILE NAME: {f['stem']}.png
IMAGE TYPE: {name}
ASPECT RATIO: {ratio}
PIXEL DIMENSIONS: {f['size']}
AUDIENCE: clinicians (registered nurses)
VISUAL GOAL: {f['desc']}

PROMPT:
{base}
Title: "{f['title']}".
Content: {f['content']}
All text in American English, short labels only, spelled correctly. {'Bottom-center' if f['scaffold'] == 'A' else 'Bottom-right'}: "renalcarematters.com" in small semi-transparent navy text.

NEGATIVE INSTRUCTIONS:
{NEG_FIG}

QUALITY CHECK:
Mobile-readable, clinically plausible, visually calm, publication-grade, consistent with renalcarematters.com house style. White or soft light-gray background, never dark. Attribution renalcarematters.com visible {'bottom-center' if f['scaffold'] == 'A' else 'bottom-right'}.
```"""


def main():
    OUT.mkdir(parents=True, exist_ok=True)
    lines = ["# Transplant Nurse subtrack · GPT image prompt pack", "",
             "Generated from `tools/transplant_nurse/content/images.py` by `tools/transplant_nurse/build_image_prompts.py`.",
             f"{len(I.HEROES)} circular-vignette heroes (williamriveromd-hero-vignette v3) and {len(I.FIGURES)} in-body figures (williamriveromd-simple-figure v1).",
             "Save each PNG under its FILE NAME. Figures appear on the pages automatically on the next `generate_transplant_nurse.py --patch` run once the image (and its .webp) is in `images/`. The end-of-course knowledge check reuses the hub hero.", "",
             "## Part 1 · Heroes", ""]
    for k, h in I.HEROES.items():
        lines += [f"### {'Hub' if k == 'hub' else 'Module ' + str(int(k))}", "", hero_block(k, h), ""]
    lines += ["## Part 2 · In-body figures", ""]
    for f in I.FIGURES:
        lines += [f"### {f['id']} · Module {int(f['mid'])} · section `{f['section']}`", "", fig_block(f), ""]
    (OUT / "GPT-IMAGE-PROMPTS.md").write_text("\n".join(lines), encoding="utf-8")
    man = [{"file": h[0] + ".png", "kind": "hero", "page": k} for k, h in I.HEROES.items()] + \
          [{"file": f["stem"] + ".png", "kind": "figure", "id": f["id"], "module": f["mid"], "section": f["section"], "size": f["size"], "alt": f["alt"]} for f in I.FIGURES]
    (OUT / "image-manifest.json").write_text(json.dumps(man, indent=1), encoding="utf-8")
    print(f"wrote {len(man)} prompts to {OUT.relative_to(ROOT)}/")


if __name__ == "__main__":
    main()
