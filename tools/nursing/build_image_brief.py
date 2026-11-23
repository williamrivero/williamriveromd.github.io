#!/usr/bin/env python3
"""Build docs/nursing-course/GPT-IMAGE-BRIEF.md from each module's `image` block.

    python3 tools/nursing/build_image_brief.py

The brief is self-contained: a GPT image session needs nothing but that file.
Prompts follow the house hero-vignette v3 scaffold (.claude/skills/williamriveromd-hero-vignette).
"""
import html, importlib.util
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]


def load(name):
    spec = importlib.util.spec_from_file_location(name, ROOT / "tools/nursing/content" / f"{name}.py")
    m = importlib.util.module_from_spec(spec); spec.loader.exec_module(m); return m


C = load("common")
u = lambda s: html.unescape(s)

CAMERA = {
    "01": "environmental portrait at seated eye level, subject group left of center",
    "02": "over-the-shoulder view from behind the patient, looking toward the nurse and the shared page",
    "03": "three-quarter overhead view of the table, faces partly in frame",
    "04": "wide-angle interior, sharp foreground figure, soft background action",
    "05": "eye-level side profile of the three seated people",
    "06": "rear three-quarter view of the nurse, machine in soft focus beyond",
    "07": "macro, hands-only composition; no faces",
    "08": "wide-angle interior from the doorway, single figure at one-third",
    "09": "wide environmental shot from slightly above, team arranged in an arc",
    "10": "environmental portrait from the doorway of the room",
    "11": "overhead, hands-and-table composition; faces out of frame or cropped at the chin",
    "12": "side profile of a standing group, speaker facing left",
}
CAST = {
    "01": "Nurse: woman, late 20s, short bob, light-brown skin, teal scrubs. Patient: man, 60s, gray crew cut, medium-brown skin, loose plaid shirt.",
    "02": "Nurse: woman, 40s, hair in a low bun, glasses, maroon scrub top. Patient: woman, late 50s, shoulder-length wavy hair, floral blouse.",
    "03": "Nurse: man, 30s, stocky, navy scrubs. Dietitian: woman, 30s, long ponytail, white coat over a green top. Patient: man, 60s, thin, balding, light polo shirt.",
    "04": "Foreground nurse: woman, 30s, tall, hair clipped up, light-blue scrubs. Background nurse: man, 40s, broad build. Patient: man, 70s, mostly out of focus.",
    "05": "Patient: woman, early 70s, silver hair in a bun, dark-brown skin, house dress and cardigan. Daughter: woman, 40s, market apron folded on her lap. Nurse: man, 30s, slim, gray scrubs.",
    "06": "Nurse: woman, 50s, short graying hair, navy scrubs, seen from behind and to the side.",
    "07": "Nurse's hands in light-blue nitrile gloves; patient's forearm, medium-brown skin, adult man. No faces.",
    "08": "Technician: man, 20s, lean, cap worn backward, dark-green scrub top, rubber shoes.",
    "09": "Three nurses: woman in her 20s with a braid, man in his 40s with glasses, woman in her 50s as trainer; mixed scrub colors.",
    "10": "Nurse: woman, 30s, curly hair tied back, white community-nurse uniform. Patient: man, mid-60s, heavyset, sleeveless undershirt under an open short-sleeved shirt.",
    "11": "Nurse's hands (woman, no gloves, plain watch) and patient's hands (man, 40s, wedding ring). Faces not shown.",
    "12": "Five staff: head nurse (woman, 50s), two staff nurses (man 20s, woman 30s), technician (man, 40s), physician (woman, 40s, white coat).",
}

PREAMBLE = """# GPT image production brief — Nephrology Nursing & Hemodialysis (12 module heroes)

**For:** a GPT image-generation session. This file is complete on its own; you do not need the website repository or any earlier conversation.
**Site:** Renal Care Matters (renalcarematters.com), a free kidney-health education library for Filipino patients and clinicians.
**What you are making:** one hero picture for each of 12 nursing-education modules. Each picture sits inside a circular frame beside the page title.
**What you are not making:** diagrams, infographics, labels, or anything with words. Two modules also need instructional diagrams; those are specified separately at the end and are **not** to be produced by free image generation.

## 1. Art direction (applies to every prompt)

Paste this block before each module prompt, or keep it as the session's standing instruction.

```
ART DIRECTION — RENAL CARE MATTERS NURSING SERIES

Format: square 1:1, 2048 x 2048 px. The scene is composed to be shown inside a CIRCLE that
fills 85-90% of the canvas, with a visible plain white margin all the way around. The circle
never touches the canvas edge and nothing important touches the circle's edge.

Style: realistic documentary-style editorial illustration with the look of a natural-light
photograph. Calm, warm, unstaged. Soft daylight, gentle depth of field. Bright and airy;
never dark, never high-contrast, never neon or HDR. Colors harmonize with clinical teal
#1a6b72, navy #1f3864, renal green #2e6b3e and warm neutrals. One consistent color grade
across all 12 images so they read as a set.

Setting and people: contemporary Philippine renal-care settings (ward, clinic, dialysis unit,
home). Filipino staff and patients with realistic, varied faces, ages, builds and skin tones.
Staff wear plain scrubs or uniforms with no logos; closed shoes; hair tied back; no jewelry on
hands except a plain watch or ring where stated. Patients are dressed modestly and shown with
dignity. Every image uses a different cast: no person may look like a person in another image.

Composition: one clear focal point that still reads when the picture is cropped to a small
circle on a phone. Hero subject 60-70% of the circle, supporting context 20-30%. Reserve
20-25% of the circle, on the LEFT side, as calm negative space (plain wall, soft blur, window
light) with no faces, hands or equipment in it.

Clinical accuracy: correct hands (five fingers), plausible anatomy, plausible equipment.
Equipment is generic and unbranded. If you are unsure how a device looks, keep it soft-focus
in the background rather than inventing detail.

Never include: any text, letters, numbers, labels, captions, watermarks, logos or brand names;
readable screens, monitors, charts, forms, name bands or medicine labels; needles entering
skin, blood, open wounds, or resuscitation maneuvers; real or recognizable individuals;
cartoon or flat-vector style; borders, frames or banners; a cropped circle.
```

## 2. Delivery

| Item | Specification |
|---|---|
| Master | 2048 x 2048 px PNG, sRGB, no transparency, white outside the circle |
| File name | exactly as given in each prompt (site convention `<page-slug>-vignette-hero.png`) |
| Where it goes | `images/` in the site repository |
| Derivatives | made by the site's own scripts after intake: WebP copy, 800 px phone copy, 1200 x 630 share card, 220 x 160 related-card thumbnail. Do not produce these. |
| Text in image | none (this differs from the atlas figures, which carry a footer; hero vignettes carry no text) |
| Language | any wording you write back to the team is in American English |

After intake, the site maintainer runs: `python3 generate_nursing_course.py --patch`, then `patch_responsive_images.py`, `patch_og_images.py` and `generate_rg_thumbs.py`. A module page shows no hero picture until its file exists, so images can arrive in any order.

## 3. Review before publication

Each image has a named reviewer type. Regenerate, do not retouch, if any of these appear: an impossible hand or limb; equipment that could not work or that implies a wrong technique (for example a blood-pressure cuff over clothing, a needle or tubing where the prompt forbids it, a catheter being handled without gloves or mask); readable or pseudo-readable text; a face that resembles a real public figure; a person repeated from another image; a patient shown in distress or undressed.

## 4. Module prompts
"""

DIAGRAMS = """
## 5. Instructional diagrams (separate track — do not generate freely)

These are teaching diagrams whose labels, directions and numbers must be correct. They are built as reviewed vector graphics or site-native HTML, with every label authored as real text on the page. An image generator must not be asked to render machine settings, numeric values, labels or procedural steps.

| Module | Diagram | How it is produced | Must be verified by |
|---|---|---|---|
| 6 | Dialyzer transport: blood and dialysate in countercurrent flow; diffusion of urea and potassium out and bicarbonate in; ultrafiltration of water by pressure | The house `dialysis-circuit-schematic` skill, which fixes port colors, flow directions and pressure points; labels in HTML beside the figure | Hemodialysis nurse educator and nephrologist |
| 6 | Extracorporeal circuit overview: arterial needle, blood pump, dialyzer, venous chamber and air detector, venous needle | Same skill; no numeric settings in the image | Hemodialysis nurse educator and biomedical technician |
| 8 | Water treatment train: feed water, sediment filter, softener, two carbon tanks in series, reverse osmosis, distribution loop, machine; with the total-chlorine sampling point after the carbon tanks | Site-native markup (an ordered flow built in HTML and CSS) or a verified vector; topology and sampling points must match the unit being taught, and the caption must say it is an example layout | Dialysis water technician or biomedical engineer, and nephrologist |

The tables of limits, schedules and first actions in Modules 2, 4, 6, 8 and 9 already exist as accessible HTML on the pages and must stay as HTML.
"""


def main():
    out = [PREAMBLE]
    manifest_rows = ["| Module | Final file name | Alt text | Reviewer |", "|---|---|---|---|"]
    for mid, slug, title, short, _n, _h in C.MODULES:
        m = load(f"m{mid}").MODULE
        im = m["image"]
        final = f"{C.COURSE['hub_slug']}-{mid}-{slug}-vignette-hero.png"
        out.append(f"""### Module {int(mid)} — {title}

- **Module ID:** {mid} (work ID `{im['file']}`)
- **Final file name:** `{final}`
- **Placement:** hero circular vignette on `/guides/{C.COURSE['hub_slug']}-{mid}-{slug}`, to the right of the title on desktop, above it on phones
- **Learning purpose:** {u(im['purpose'])}
- **Alt text (already set on the page):** {u(im['alt'])}
- **Review:** {u(im['reviewer'])}

```
[Paste the ART DIRECTION block first.]

Square 1:1 documentary-style editorial image on a 2048x2048 canvas, composed for a CIRCULAR
vignette occupying 85-90% of the canvas with a white margin all around.
Composition archetype: {u(im['archetype'])}. Camera: {CAMERA[mid]}.

Scene: {u(im['scene'])}

Cast (unique to this image): {CAST[mid]}

Framing and focal point: {u(im['focal'])} The focal point sits right of center so the left
20-25% of the circle stays calm and empty.

Setting: {u(im['setting'])}

Clinically significant details to get right: {u(im['details'])}

Do not show: {u(im['exclusions'])} Also no text, numbers, labels, logos, watermarks, readable
screens or documents anywhere in the image.

Output file name: {final}
```
""")
        if im.get("diagram_note"):
            out.append(f"> Diagram note for this module: {u(im['diagram_note'])}\n")
        manifest_rows.append(f"| {int(mid)} | `{final}` | {u(im['alt'])} | {u(im['reviewer'])} |")
    out.append("## Asset manifest (summary)\n\nThe machine-readable version is `image-manifest.json` beside this file.\n\n" + "\n".join(manifest_rows) + "\n")
    out.append(DIAGRAMS)
    p = ROOT / "docs/nursing-course/GPT-IMAGE-BRIEF.md"
    p.write_text("\n".join(out), encoding="utf-8")
    print("wrote", p.relative_to(ROOT))


if __name__ == "__main__":
    main()
