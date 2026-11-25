#!/usr/bin/env python3
"""Write docs/dialysis-nurse-assistant/IMAGE-PLAN-BLUEPRINT.md, GPT-IMAGE-PROMPTS.md and image-manifest.json from content/images.py.

Heroes follow williamriveromd-hero-vignette v3. Figures follow williamriveromd-simple-figure v1 (scaffolds B-E), the
williamriveromd-algorithm-generator-skill (A), williamriveromd-biomedical-mechanism-figure (M),
williamriveromd-organ-crosstalk-sigil-graphic (S) and the williamriveromd-infographic-skill procedural photo strip (P).
Share cards follow the infographic skill's OG rule (1200 x 630) and build_academy_og.py's art contract (text-free 1536 x 1024).

    python3 tools/dialysis_nurse_assistant/build_image_prompts.py [--copy "<folder>"]

--copy also writes both Markdown files into another folder (e.g. the blueprint folder on /Volumes/Storage).
"""
import argparse, collections, html, importlib.util, json, shutil
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
spec = importlib.util.spec_from_file_location("dna_images", ROOT / "tools/dialysis_nurse_assistant/content/images.py")
I = importlib.util.module_from_spec(spec); spec.loader.exec_module(I)
OUT = ROOT / "docs" / "dialysis-nurse-assistant"

AUD = "Dialysis Nurse Assistants / Patient Care Assistants (supervised support workers, plain-language readers) and their preceptors"
ATTR = 'Include a small professional footer reading "© renalcarematters.com" at the bottom-right corner in subtle medium-gray (#6b7280) Inter, at least 70% opacity, never inside a node, panel or arrow.'

NEG_HERO = """Avoid: busy layouts, collage overload, more than four supporting scenes, dozens of icons, tiny unreadable labels,
infographic clutter, duplicated people, repeated compositions, cropped circle, cropped objects, cropped anatomy, edge
clipping, objects touching the circular border, important content inside the title safe zone, baked-in text, titles,
captions, logos, watermarks, rectangular borders, frames, banners, dark / charcoal / black backgrounds, cartoon style,
neon, HDR, over-saturation, distorted hands or faces, implausible anatomy. Never show an assistant cannulating, touching
needles, catheter hubs, bloodlines or machine controls, giving medicine, or disconnecting a patient."""

NEG_FIG = """Avoid cartoon style, clutter, tiny unreadable labels, AI gibberish text, misspellings, unrealistic anatomy, overprocessed
HDR and excessive saturation. NEVER use dark, navy, charcoal or black backgrounds — white or soft light gray only. Use ONLY
the sans-serif font Inter — no serif, decorative or handwritten typefaces. Never show an assistant touching needles,
catheter hubs, bloodlines or machine controls, giving medicine or disconnecting a patient. No brands, logos, real
facility names or readable patient data. Never omit the © renalcarematters.com attribution."""

SCAFFOLD = {
    "A": ("Clinical algorithm (williamriveromd-algorithm-generator-skill)", "2:3 portrait",
          "Clinical algorithm flowchart in the style of an AHA resuscitation algorithm and a journal nephrology treatment algorithm, white (#ffffff) background, title at top in bold navy (#0f1e2e) Inter. Rounded rectangular nodes: start and decision nodes teal (#1a6b72), action nodes navy (#1f3864) with white text, caution nodes amber (#b8860b), escalation nodes red (#b91c1c), safe-outcome nodes renal green (#1f7a4d). Bold connecting arrows, at most 3–4 branching levels, generous whitespace, labels of at most eight words, mobile-readable."),
    "B": ("Side-by-side comparison (williamriveromd-simple-figure, Scaffold B)", "16:9 landscape",
          "Medical education comparison figure, AJKD/NEJM graphical-abstract style, white (#ffffff) background, title centered at top in bold navy (#0f1e2e) Inter, equal rounded panels separated by a soft dashed divider, green check (#1f7a4d) and red X (#b91c1c) markers where shown, ample negative space, mobile-readable labels."),
    "C": ("Horizontal step sequence (williamriveromd-simple-figure, Scaffold C)", "16:9 landscape",
          "Clean clinical education step figure, white (#ffffff) background, title at top center in bold navy (#0f1e2e) Inter. Rounded rectangular cards in a single row (or a gentle loop where stated) on a very soft gray panel (#f3f4f6), joined by bold navy arrows; each card has a colored top accent band, a small line icon or small semi-photorealistic vignette, a bold label and one short line. Generous whitespace, mobile-readable."),
    "D": ("One-panel teaching poster (williamriveromd-simple-figure, Scaffold D)", "16:9 landscape",
          "Medical teaching poster, AJKD/NEJM graphical-abstract style, white (#ffffff) background, title at top in bold navy (#0f1e2e) Inter, subtitle in clinical teal (#1a6b72). A central semi-photorealistic scene or chart with labeled callouts in modular rounded cards and color-coded arrows; a bottom strip in soft teal (#e6f2f2) with navy text carrying the practical rule. Ample negative space, no clutter."),
    "E": ("Reference card (williamriveromd-simple-figure, Scaffold E)", "1:1 square",
          "Clinical quick-reference card, publication-grade nephrology design, white (#ffffff) background, bold navy title at top in Inter, compact grid with headers in teal (#1a6b72) on soft gray (#f3f4f6), alternating row fills, green / amber / red accents only where stated, a short footer takeaway band."),
    "M": ("Biomedical mechanism figure (williamriveromd-biomedical-mechanism-figure)", "16:9 landscape",
          "Publication-grade review-article mechanism figure in the renalcarematters.com house style, white (#ffffff) background, title at top in bold navy (#0f1e2e) Inter, subtitle in clinical teal (#1a6b72). An organ-level or scene-level panel, a thin dashed magnified inset of the functional unit, and a bottom injury → intervention → benefit summary strip. Semi-photorealistic rendering with soft studio lighting, muted clinical palette (teal = normal or protective, red = harm, green = the fix), color-coded arrows, labels of at most four words. Anatomically and technically accurate."),
    "S": ("Organ crosstalk sigil (williamriveromd-organ-crosstalk-sigil-graphic)", "1:1 square",
          "Simple medical organ-crosstalk sigil: minimal clinical line-art, thin monoline strokes, soft teal-blue palette, white background, clean rounded organ shapes, balanced sigil-like composition, dotted curved arrows forming a calm loop, generous whitespace, no photorealism, no 3D. Short labels only where stated, in Inter."),
    "P": ("Instructional photo strip (williamriveromd-infographic-skill, procedural)", "16:9 landscape",
          "Clean instructional photo strip on a white (#ffffff) background, title at top in bold navy (#0f1e2e) Inter. Four or five equal photorealistic panels in a single row, each a tightly framed scene of Filipino staff and patients in a bright modern Philippine dialysis unit, consistent lighting, cast and color grade across panels, a small teal number badge in each panel corner and a one-line caption under each panel. Correct actions framed in green (#1f7a4d); prohibited actions marked with a clean red (#b91c1c) X. No readable text on labels, screens or papers inside the photos."),
}
NAMES = {"A": "Algorithm", "B": "Comparison", "C": "Step sequence", "D": "Teaching poster", "E": "Reference card",
         "M": "Mechanism figure", "S": "Crosstalk sigil", "P": "Photo strip"}


def hero_block(key, h):
    stem, arch, cam, people, scene, safe = h
    hands = people == "hands only"
    scaffold = "B still-life" if hands else "A people"
    who = "Hands only, no faces." if hands else (f"People: {people}. Filipino, with age, face shape, hairstyle, build, clothing color, "
                                                 "accessories and posture clearly different from the other heroes in this pack.")
    return f"""```
FILE NAME: {stem}.png
IMAGE TYPE: Circular vignette hero v3 — Scaffold {scaffold}
ASPECT RATIO: 1:1 (square — displayed inside an 85–90% inscribed circle with white margin)
PIXEL DIMENSIONS: 2048 × 2048
COMPOSITION ARCHETYPE: {arch}
CAMERA: {cam}
HUMAN VARIATION (vs. previous image): {'hands only' if hands else 'new cast; at least 12 traits differ (age, sex, face shape, jawline, hairstyle, hair length, build, skin tone within Filipino diversity, clothing style and color, accessories, posture, hand position, expression, setting)'}
AUDIENCE: {AUD}
VISUAL GOAL: One calm, dignified picture that tells a supervised assistant what this module is about at a glance and shows the work as skilled, careful and valued.

PROMPT:
Square 1:1 photorealistic editorial photograph on a 2048×2048 canvas, composed to be displayed inside a CIRCULAR vignette occupying 85–90% of the canvas diameter with a visible WHITE BORDER around the full circle (the circle never touches the canvas edges). Composition archetype: {arch}. Camera: {cam}.
{who}
Scene: {scene}. Clean, bright, modern Philippine dialysis unit or hospital setting, soft natural daylight, gentle shallow depth of field.
Visual hierarchy: hero subject 60–70% of the circle; 2–4 supporting elements 20–30%; reserve a 20–25% TITLE SAFE ZONE on the {safe} side of the circle as soft gradient, clean pale wall or blurred background (no faces, anatomy, icons, objects or callouts inside it).
Calm, reassuring, documentary-realistic color grade harmonizing with clinical teal #1a6b72 and navy #0f1e2e on a light background; soft falloff toward the rim. Full-bleed within the inscribed circle, no rectangular borders, frames or banners.
Clinical accuracy: any fistula arm stays uncovered and untouched; the assistant never handles needles, lines, catheter hubs or machine controls.
Absolutely NO text of any kind: no title, caption, label, readable writing on paper or screens, logo, or watermark.

NEGATIVE INSTRUCTIONS:
{NEG_HERO}

QUALITY CHECK:
Square 2048×2048; circle 85–90% with a visible white margin, never cropped; one dominant subject; 20–25% empty title-safe zone; Filipino context where people are shown; no text anywhere; nobody shown doing an excluded task; crops cleanly inside the circle and into a 16:9 tile from its center.
```"""


def fig_block(f):
    name, ratio, base = SCAFFOLD[f["scaffold"]]
    ratio = {"1024 × 1024": "1:1 square", "1024 × 1536": "2:3 portrait"}.get(f["size"], ratio)
    abbr = ""
    if f["abbrevs"]:
        abbr = " Any acronym shown is spelled out once in small text on first appearance: " + "; ".join(f"{a} = {b}" for a, b in f["abbrevs"]) + "."
    return f"""```
FILE NAME: {f['stem']}.png
IMAGE TYPE: {name}
ASPECT RATIO: {ratio}
PIXEL DIMENSIONS: {f['size']}
AUDIENCE: {AUD}
TEACHING PURPOSE: {f['goal']}
VISUAL GOAL: {f['desc']}

PROMPT:
{base}
Title: "{f['title']}".
Content: {f['content']}
All text in American English, plain words a new assistant understands, short labels only, every word spelled correctly. Use only the facts and numbers given here; add no other numbers, doses, dilutions, contact times or color codes.{abbr}
{ATTR}

NEGATIVE INSTRUCTIONS:
{NEG_FIG}

QUALITY CHECK:
Mobile-readable at phone width; clinically and technically accurate (dialyzer ports, fistula, chair, machine); calm and uncluttered; light background; Inter only; numbers exactly as given; no one shown doing an excluded task; © renalcarematters.com visible bottom-right.
```"""


def og_track_block():
    o = I.OG_TRACK_ART
    return f"""```
FILE NAME: {o['file']}   (save into {o['folder']}/)
IMAGE TYPE: Academy share-card ART (text-free) for build_academy_og.py
ASPECT RATIO: 3:2 landscape (the script crops it to 1.91:1 and sets every word itself)
PIXEL DIMENSIONS: 1536 × 1024
AUDIENCE: people seeing the link on Facebook, Messenger, Viber or LinkedIn: assistants, nurses, unit managers
VISUAL GOAL: At thumbnail size, show a supervised assistant and a registered nurse working as one team at a dialysis chair.

PROMPT:
Landscape 3:2 photorealistic editorial photograph, 1536×1024. Keep the LEFT 42% of the frame a quiet field: soft, light, out-of-focus teal-and-cream wall with no faces, objects or detail (the title will be set there by script). Place the subject group in the RIGHT 58%.
Scene: {o['scene']}. Soft natural daylight, gentle shallow depth of field, calm and reassuring, color grade harmonizing with clinical teal #1a6b72 and navy #0f1e2e on a light background. The subject must stay recognizable at 300 px wide.
Clinical accuracy: the fistula arm is uncovered and untouched; the assistant does not touch lines, needles or machine controls.
Absolutely NO text, logos, watermarks, readable screens or papers.

NEGATIVE INSTRUCTIONS:
Dark or black backgrounds; clutter in the left field; text of any kind; cartoon style; neon or HDR; distorted hands or faces; an assistant doing an excluded task.

QUALITY CHECK:
Left 42% empty and light; subjects on the right and legible as a thumbnail; nothing important within 90 px of the top or bottom edge (the script trims about 110 px from each); Filipino context.
```"""


def og_calc_block():
    o = I.OG_CALC
    return f"""```
FILE NAME: {o['file']}   (save into images/)
IMAGE TYPE: OG / social share card (williamriveromd-infographic-skill)
ASPECT RATIO: 1.91:1
PIXEL DIMENSIONS: 1200 × 630
AUDIENCE: assistants and preceptors sharing the calculator link
VISUAL GOAL: Show at a glance that this is a practical bedside checking tool, not a treatment calculator.

PROMPT:
OG social share card, exactly 1200×630, white (#ffffff) background with a soft teal (#e6f2f2) diagonal band on the right. Left half: title "{o['title']}" in bold navy (#0f1e2e) Inter on two lines; subtitle "{o['subtitle']}" in teal (#1a6b72) Inter; small amber (#b8860b) pill "Report to the nurse". Right half: a clean semi-photorealistic still-life of three objects in a neat row on a light surface: a wheelchair-scale display reading "63.4 kg", a blood pressure cuff with a small display reading "104/62", and a small analog stopwatch; soft studio light. Generous whitespace, mobile-readable.
Small "© renalcarematters.com" bottom-right in subtle gray Inter.

NEGATIVE INSTRUCTIONS:
Dark backgrounds; any text other than the title, subtitle, pill, the two display readings and the attribution; serif fonts; clutter; cartoon style; misspellings.

QUALITY CHECK:
Exactly 1200×630; title readable at 600 px wide; words spelled exactly as given; light background; attribution present.
```"""


def tile_block():
    t = I.LANDING_TILE
    return f"""```
FILE NAME: {t['src']}   (processed to {t['file']}, 960 × 540)
IMAGE TYPE: Academy landing tile (By Role column card)
ASPECT RATIO: 3:2 generated, cropped to 16:9 from the center band
PIXEL DIMENSIONS: 1536 × 1024
AUDIENCE: visitors choosing a role on the Academy home page
VISUAL GOAL: In a small card, show what this role does all day: careful measurement and reporting beside the patient.

PROMPT:
Landscape photorealistic editorial photograph, 1536×1024, with all important content inside the central 1536×864 band (top and bottom 80 px will be cropped). Scene: {t['scene']}. Bright, airy, documentary-realistic, soft daylight, gentle depth of field, color grade harmonizing with clinical teal #1a6b72 and navy #0f1e2e. Clear single focal point readable at 320 px wide; distinct cast from the course heroes.
Absolutely NO text, logos, watermarks or readable displays.

NEGATIVE INSTRUCTIONS:
Dark scenes; clutter; text; cartoon style; neon or HDR; distorted hands or faces; an assistant touching lines, needles or machine controls.

QUALITY CHECK:
Focal point centered in the 16:9 band; readable as a small card; light and calm; no text.
```"""


def write_blueprint():
    mods = collections.OrderedDict()
    for f in I.FIGURES:
        mods.setdefault(f["mid"], []).append(f)
    g = collections.Counter(f["goal"] for f in I.FIGURES)
    sc = collections.Counter(f["scaffold"] for f in I.FIGURES)
    out = ["# Dialysis Nurse Assistant / PCA · Image plan blueprint", "",
           "Renal Care Academy &rarr; Nephrology Nursing Track &rarr; By Role &rarr; Dialysis Nurse Assistant / Patient Care Assistant (PCA). Prepared 25 November 2026 to accompany Blueprint v2.", "",
           "## Aim", "",
           "Every image must help a supervised assistant do one of three things better:", "",
           "- **Understand** the reason behind a task: a mechanism the learner can redraw from memory (what the dialyzer does, how unseen blood travels, why the alarm may stay quiet, why standing after dialysis makes people dizzy, why the scale decides the fluid goal).",
           "- **Apply** the task correctly: a step sequence, an algorithm, a technique strip, a worked example with the same numbers as the text and the toolkit, or a one-glance reference card.",
           "- **Appreciate** why it matters: the evidence made visible (skill mix, staff CPR, label errors), and the dignity and skill of the work.", "",
           "Readers are new to clinical work, often on a phone, often between patients. So: one idea per image, short labels, real objects rather than abstractions, Filipino people in Philippine units, numbers only where the module text already states them, and the semi-photorealistic renalcarematters.com house style instead of flat clip art.", "",
           "## Skills used", "",
           "| Skill | Used for |", "|---|---|",
           "| williamriveromd-hero-vignette (v3) | 13 circular heroes (course home + 12 modules); module tiles and share images are cut from them |",
           "| williamriveromd-simple-figure (Scaffolds B–E) | comparisons, step sequences, teaching posters and reference cards |",
           "| williamriveromd-algorithm-generator-skill | exposure response, alarm or blood, and warning-sign algorithms |",
           "| williamriveromd-biomedical-mechanism-figure | dialyzer, blood transmission, needle dislodgement, weight as water, standing dizziness |",
           "| williamriveromd-organ-crosstalk-sigil-graphic | kidney, heart and lungs fluid loop |",
           "| williamriveromd-infographic-skill | instructional photo strips, the calculator OG card, the 1200 × 630 rule |",
           "| williamriveromd-local-image-generator (Stage 2) | optional: validate this pack and stage the folders |", "",
           "## Guardrails carried into every prompt", "",
           "- Nobody is shown cannulating, touching needles, catheter hubs, bloodlines or machine controls, giving medicine or disconnecting a patient. Machine parts appear only with a 'never' or 'not your role' marker.",
           "- The access arm is always uncovered and untouched in patient scenes (this is the Module 7 teaching point).",
           "- Numbers appear only as the module states them (63.4 kg worked example, 132/74 to 104/62, 81.4%, 1 in 3,046, 21% higher odds). No generic contact times, dilutions or waste colors: those come from the unit's own labels and charts.",
           "- The dialyzer follows the house reference anatomy: blood in and out at the end caps, dialysate in near the blood-out end and out near the blood-in end (countercurrent).",
           "- No real patients, readable patient data, brands, logos or facility names. Light backgrounds only, Inter typeface, American English, © renalcarematters.com bottom-right on every figure.",
           "- Heroes rotate archetype, camera and cast so no two pages share a model look; the OG art and landing tile use a third, distinct cast.", "",
           "## Inventory", "",
           f"- **{len(I.HEROES)} circular heroes** (2048 × 2048). The end-of-course check reuses the course-home hero.",
           f"- **{len(I.FIGURES)} in-body figures**: " + ", ".join(f"{NAMES[k]} {v}" for k, v in sorted(sc.items())) + ".",
           f"- Teaching purpose: Understand {g['Understand']}, Apply {g['Apply']}, Appreciate {g['Appreciate']}.",
           "- **Share (OG) cards**: (1) the track card art, text-free 1536 × 1024, which `build_academy_og.py` turns into a 1200 × 630 branded card for the course home and the knowledge check; (2) the calculator card, 1200 × 630 with its title; (3) every module's share image is made from its hero by `patch_og_images.py`, so no separate prompt is needed.",
           "- **Tiles**: (1) the Academy landing tile (By Role column), 960 × 540; (2) twelve module tiles (640 × 360) and the Related Guides thumbnails, cut automatically from the heroes; (3) the role card on the parent nursing course uses the course-home hero card (`dialysis-nurse-assistant-card.webp`).", "",
           "## Figure map", "",
           "| ID | Module · section | Type | Purpose | What it teaches | File |", "|---|---|---|---|---|---|"]
    for mid, fs in mods.items():
        for f in fs:
            out.append(f"| {f['id']} | M{int(mid)} · `{f['section']}` | {NAMES[f['scaffold']]} | {f['goal']} | {f['desc']} | `{f['stem']}.png` |")
    out += ["", "## Heroes", "", "| Page | Archetype | Camera | File |", "|---|---|---|---|"]
    for k, h in I.HEROES.items():
        out.append(f"| {'Course home' if k == 'hub' else 'Module ' + str(int(k))} | {h[1]} | {h[2]} | `{h[0]}.png` |")
    out += ["", "## Share cards and tiles", "", "| Asset | Size | Made from | Where it appears |", "|---|---|---|---|",
            f"| Track share card | 1200 × 630 | `{I.OG_TRACK_ART['folder']}/{I.OG_TRACK_ART['file']}` via `build_academy_og.py` | Course home and knowledge check links |",
            f"| Calculator share card | 1200 × 630 | `images/{I.OG_CALC['file']}` | Toolkit link previews, Latest calculators carousel |",
            "| Module share images | ≤ 1200 wide, ≤ 300 KB | each module hero via `patch_og_images.py` | Module link previews |",
            f"| Landing tile | 960 × 540 | `{I.LANDING_TILE['src']}` | Academy home, By Role column |",
            "| Module tiles | 640 × 360 | each hero via `prep_assets.card()` | Course-home module grid |",
            "| Related Guides thumbnails | auto | heroes via `generate_rg_thumbs.py` | Every Academy page's Related Guides block |", "",
            "## Production workflow", "",
            "1. Open GPT-IMAGE-PROMPTS.md and paste one block at a time into ChatGPT image generation.",
            "2. Save each PNG under its exact FILE NAME into one folder.",
            "3. Audit each image against its QUALITY CHECK and the guardrails: spelling, numbers exactly as given, no excluded task shown, the access arm visible, correct dialyzer and fistula anatomy, Filipino context, light background, attribution present. Failures go into a corrected-prompt list with the reason.",
            "4. Run `python3 tools/dialysis_nurse_assistant/process_images.py \"<folder>\"`. It copies heroes and figures into `images/` with WebP twins, cuts the 640 × 360 module tiles, places the OG art and builds the track card, places the calculator card, and makes the landing tile.",
            "5. Run `python3 generate_dialysis_nurse_assistant.py --calc --patch`, then `python3 generate_rg_thumbs.py`, `python3 patch_rg_card_thumbs.py` and `python3 patch_og_images.py`. Figures appear at the end of their sections automatically; alt text and plain-language captions are already written.", ""]
    return html.unescape("\n".join(out))


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--copy", help="also write the two Markdown files into this folder")
    args = ap.parse_args()
    OUT.mkdir(parents=True, exist_ok=True)
    lines = ["# Dialysis Nurse Assistant / PCA · GPT image prompt pack", "",
             "Generated from `tools/dialysis_nurse_assistant/content/images.py` by `tools/dialysis_nurse_assistant/build_image_prompts.py`. Read IMAGE-PLAN-BLUEPRINT.md first for the purpose of each image.", "",
             f"Contents: {len(I.HEROES)} circular heroes · {len(I.FIGURES)} in-body figures · 2 share-card prompts · 1 landing tile. Paste one block at a time into ChatGPT image generation and save each PNG under its FILE NAME.", "",
             "## Part 1 · Heroes (also the source of module tiles and module share images)", ""]
    for k, h in I.HEROES.items():
        lines += [f"### {'Course home' if k == 'hub' else 'Module ' + str(int(k))}", "", hero_block(k, h), ""]
    lines += ["## Part 2 · In-body figures", ""]
    for f in I.FIGURES:
        lines += [f"### {f['id']} · Module {int(f['mid'])} · section `{f['section']}` · {f['goal']}", "", f"_Why this image: {f['why']}_", "", fig_block(f), ""]
    lines += ["## Part 3 · Share (OG) cards", "", "### Track share-card art (course home and knowledge check)", "", og_track_block(), "",
              "### Calculator share card", "", og_calc_block(), "",
              "## Part 4 · Tiles", "", "### Academy landing tile", "", tile_block(), "",
              "Module tiles (640 × 360) are cut from each module hero by `process_images.py`; no separate prompt is needed.", ""]
    prompts = html.unescape("\n".join(lines))
    bp = write_blueprint()
    (OUT / "GPT-IMAGE-PROMPTS.md").write_text(prompts, encoding="utf-8")
    (OUT / "IMAGE-PLAN-BLUEPRINT.md").write_text(bp, encoding="utf-8")
    man = ([{"file": h[0] + ".png", "kind": "hero", "page": k} for k, h in I.HEROES.items()] +
           [{"file": f["stem"] + ".png", "kind": "figure", "id": f["id"], "module": f["mid"], "section": f["section"], "size": f["size"],
             "scaffold": f["scaffold"], "goal": f["goal"], "alt": html.unescape(f["alt"])} for f in I.FIGURES] +
           [{"file": I.OG_TRACK_ART["file"], "kind": "og-track-art"}, {"file": I.OG_CALC["file"], "kind": "og-calculator"},
            {"file": I.LANDING_TILE["src"], "kind": "landing-tile"}])
    (OUT / "image-manifest.json").write_text(json.dumps(man, indent=1, ensure_ascii=False), encoding="utf-8")
    if args.copy:
        dst = Path(args.copy)
        (dst / "IMAGE-PLAN-BLUEPRINT.md").write_text(bp, encoding="utf-8")
        (dst / "GPT-IMAGE-PROMPTS.md").write_text(prompts, encoding="utf-8")
    print(f"wrote {len(man)} prompts to {OUT.relative_to(ROOT)}/" + (f" and {args.copy}" if args.copy else ""))


if __name__ == "__main__":
    main()
