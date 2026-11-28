#!/usr/bin/env python3
"""Write docs/dialysis-unit-support-staff/IMAGE-PLAN-BLUEPRINT.md, GPT-IMAGE-PROMPTS.md and image-manifest.json from content/images.py.

Hero prompts follow williamriveromd-hero-vignette v3; figure prompts follow williamriveromd-simple-figure v1 (scaffolds A-E),
the williamriveromd-biomedical-mechanism-figure layout (M) and the williamriveromd-infographic-skill procedural photo strip (P).
Paste each block into ChatGPT image generation (not the retired Image Generator GPT link), save the PNG under the FILE NAME shown, and drop the files in
images/ (or hand them over for processing). Pages pick up figures automatically on the next generator run.
"""
import html, importlib.util, json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
spec = importlib.util.spec_from_file_location("tn_images", ROOT / "tools/dialysis_support_staff/content/images.py")
I = importlib.util.module_from_spec(spec); spec.loader.exec_module(I)
OUT = ROOT / "docs" / "dialysis-unit-support-staff"

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
    "M": ("Mechanism poster (williamriveromd-biomedical-mechanism-figure layout, semi-photorealistic render)", "16:9 landscape",
          "Publication-grade mechanism poster in the renalcarematters.com house style, white (#ffffff) background, title at top in bold navy (#0f1e2e) Inter, subtitle in clinical teal (#1a6b72). Semi-photorealistic 3D-rendered anatomy and objects with soft studio lighting (NOT flat vector, NOT clip art), one dominant explanatory diagram, a thin dashed magnified inset where needed, color-coded arrows (teal for normal or protective, red for harm, green for the fix), and a bottom summary strip in navy with the practical rule. Muted clinical palette, generous whitespace, mobile-readable labels of at most four words each."),
    "P": ("Instructional photo strip (williamriveromd-infographic-skill procedural style)", "16:9 landscape",
          "Clean instructional photo strip on a white (#ffffff) background, title at top in bold navy (#0f1e2e) Inter. Four to six equal photorealistic panels in a single row, each a tightly framed close-up of Filipino hands or a Filipino worker in a bright modern Philippine dialysis unit or hospital corridor, consistent lighting and color grade across panels, a small teal number badge in each panel corner and a one-line caption under each panel. Correct actions framed in green (#1f7a4d), prohibited actions marked with a clean red (#b91c1c) X in the corner. No patient faces needed; no readable text on any labels, screens or papers inside the photos."),
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
AUDIENCE: dialysis unit orderlies and environmental service aides (plain-language readers) and their preceptors
VISUAL GOAL: One calm, dignified image that tells a support worker what this module is about at a glance and shows the work as skilled and valued.

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
    if f["size"] == "1024 × 1024":
        ratio = "1:1 square"
    elif f["size"] == "1536 × 1152":
        ratio = "4:3 landscape"
    return f"""```
FILE NAME: {f['stem']}.png
IMAGE TYPE: {name}
ASPECT RATIO: {ratio}
PIXEL DIMENSIONS: {f['size']}
AUDIENCE: dialysis unit orderlies and environmental service aides (plain-language readers) and their preceptors
VISUAL GOAL: {f['desc']}

PROMPT:
{base}
Title: "{f['title']}".
Content: {f['content']}
All text in American English, plain words a non-clinical worker understands, short labels only, spelled correctly. Use only the facts given here; add no other numbers, dilutions or color codes. {'Bottom-center' if f['scaffold'] == 'A' else 'Bottom-right'}: "renalcarematters.com" in small semi-transparent navy text.

NEGATIVE INSTRUCTIONS:
{NEG_FIG}

QUALITY CHECK:
Mobile-readable, clinically plausible, visually calm, publication-grade, consistent with renalcarematters.com house style. White or soft light-gray background, never dark. Attribution renalcarematters.com visible {'bottom-center' if f['scaffold'] == 'A' else 'bottom-right'}.
```"""


def write_blueprint():
    import collections
    mods = {}
    for f in I.FIGURES:
        mods.setdefault(f["mid"], []).append(f)
    g = collections.Counter(f["goal"] for f in I.FIGURES)
    sc = collections.Counter(f["scaffold"] for f in I.FIGURES)
    names = {"A": "Algorithm (portrait)", "B": "Two-panel comparison", "C": "Step sequence", "D": "One-panel poster",
             "E": "Reference card", "M": "Mechanism poster", "P": "Instructional photo strip"}
    out = ["# Housekeeping & Support Staff · Image plan blueprint", "",
           "Renal Care Academy &rarr; Nephrology Nursing &rarr; Housekeeping & Support Staff (orderlies and environmental service aides). Prepared 24 November 2026.", "",
           "## Aim", "",
           "Every image must help a support worker do one of three things better:", "",
           "- **Understand** the reason behind a task (a mechanism the learner can redraw from memory: the chain of infection, why soil shields germs, why patients faint after dialysis, why distance loads the spine).",
           "- **Apply** the task correctly (a technique strip, a checklist, a decision card or a map of the object being cleaned).",
           "- **Appreciate** why it matters (invisible risk made visible, a schedule that has no slack, a lift that becomes safe when the shelf moves, the dignity of the work).", "",
           "The audience reads plain language, often on a phone, often between tasks. So: one idea per image, labels of four words or fewer, real objects instead of abstractions, Filipino people and Philippine settings, and the illustrated (GPT-rendered, semi-photorealistic) house aesthetic rather than flat vector clip art.", "",
           "## Guardrails carried into every prompt", "",
           "- No generic dilutions, contact times or imported waste colors: label and task-card values are shown as blanks; the DOH color grid carries a 'facility chart governs' note.",
           "- Excluded tasks are never shown being done by support staff (no aide touching a machine screen, needle, line or catheter). Machine parts appear only with 'never' or 'only if assigned' markers.",
           "- No real patients, no readable patient data, no brands or logos, no real facility names. Patient faces are optional and never in distress close-ups.",
           "- Light backgrounds only, Inter typeface, American English, renalcarematters.com attribution (public Academy set).",
           "- Heroes rotate composition archetypes and cast (age, sex, build, hairstyle, uniform color) so no two pages share a model look.", "",
           "## Inventory", "",
           f"- {len(I.HEROES)} circular-vignette heroes (hub plus 15 modules; the end-of-course check reuses the hub hero), 2048 &times; 2048.",
           f"- {len(I.FIGURES)} in-body figures: " + ", ".join(f"{names[k]} {v}" for k, v in sorted(sc.items())) + ".",
           f"- Teaching purpose: Understand {g['Understand']}, Apply {g['Apply']}, Appreciate {g['Appreciate']}.", "",
           "Emphasis follows the owner's request: aseptic technique (Modules 3 to 5: 9 figures), health care waste (Module 10: 3 figures plus spill and sharps in Module 9), and patient transport and transfers (Modules 11 and 12: 7 figures).", "",
           "## Figure map", "",
           "| ID | Module and section | Type | Purpose | What it teaches | File |",
           "|---|---|---|---|---|---|"]
    for mid in sorted(mods):
        for f in mods[mid]:
            out.append(f"| {f['id']} | M{int(mid)} &middot; `{f['section']}` | {names[f['scaffold']]} | {f['goal']} | {f['desc']} | `{f['stem']}.png` |")
    out += ["", "## Heroes", "", "| Page | Archetype | Camera | File |", "|---|---|---|---|"]
    for k, h in I.HEROES.items():
        out.append(f"| {'Hub' if k == 'hub' else 'Module ' + str(int(k))} | {h[1]} | {h[2]} | `{h[0]}.png` |")
    out += ["", "## Production workflow", "",
            "1. Open GPT-IMAGE-PROMPTS.md and paste one block at a time into ChatGPT image generation.",
            "2. Save each PNG under its exact FILE NAME.",
            "3. Audit each image against its QUALITY CHECK and the guardrails above: spelling, no invented numbers, no excluded task shown, correct object anatomy (dialysis chair, machine, fistula arm), Filipino context, light background, attribution present.",
            "4. Drop passing images in `images/` (or hand them over for processing to .webp). Failures go into a new corrected-prompt file with the reason for each.",
            "5. Re-run `python3 generate_dialysis_support_staff.py --patch`. Figures appear at the end of their sections automatically once the file exists; alt text and plain-language descriptions are already written.", ""]
    (OUT / "IMAGE-PLAN-BLUEPRINT.md").write_text(html.unescape("\n".join(out)), encoding="utf-8")


def main():
    OUT.mkdir(parents=True, exist_ok=True)
    lines = ["# Housekeeping & Support Staff subtrack · GPT image prompt pack", "",
             "Generated from `tools/dialysis_support_staff/content/images.py` by `tools/dialysis_support_staff/build_image_prompts.py`. Read IMAGE-PLAN-BLUEPRINT.md first for the purpose of each image.",
             f"{len(I.HEROES)} circular-vignette heroes (williamriveromd-hero-vignette v3) and {len(I.FIGURES)} in-body figures (simple-figure scaffolds A-E, mechanism posters M, instructional photo strips P).",
             "Save each PNG under its FILE NAME. Figures appear on the pages automatically on the next `generate_dialysis_support_staff.py --patch` run once the image (and its .webp) is in `images/`. The end-of-course knowledge check reuses the hub hero.", "",
             "## Part 1 · Heroes", ""]
    for k, h in I.HEROES.items():
        lines += [f"### {'Hub' if k == 'hub' else 'Module ' + str(int(k))}", "", hero_block(k, h), ""]
    lines += ["## Part 2 · In-body figures", ""]
    for f in I.FIGURES:
        lines += [f"### {f['id']} · Module {int(f['mid'])} · section `{f['section']}` · {f['goal']}", "", f"_Why this image: {f['why']}_", "", fig_block(f), ""]
    (OUT / "GPT-IMAGE-PROMPTS.md").write_text(html.unescape("\n".join(lines)), encoding="utf-8")
    write_blueprint()
    man = [{"file": h[0] + ".png", "kind": "hero", "page": k} for k, h in I.HEROES.items()] + \
          [{"file": f["stem"] + ".png", "kind": "figure", "id": f["id"], "module": f["mid"], "section": f["section"], "size": f["size"], "scaffold": f["scaffold"], "goal": f["goal"], "alt": f["alt"]} for f in I.FIGURES]
    (OUT / "image-manifest.json").write_text(json.dumps(man, indent=1), encoding="utf-8")
    print(f"wrote {len(man)} prompts to {OUT.relative_to(ROOT)}/")


if __name__ == "__main__":
    main()
