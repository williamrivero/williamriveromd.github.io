#!/usr/bin/env python3
"""Write docs/special-dialysis-nurse-roles/IMAGE-PLAN-BLUEPRINT.md, GPT-IMAGE-PROMPTS.md and image-manifest.json
from tools/special_nurse_roles/content/images.py.

Hero prompts follow williamriveromd-hero-vignette v3; algorithm prompts (A) follow williamriveromd-algorithm-generator-skill;
figure prompts B-E follow williamriveromd-simple-figure; mechanism posters (M) follow the williamriveromd-biomedical-mechanism-figure
layout rendered semi-photorealistically; photo strips (P) follow the williamriveromd-infographic-skill procedural style.
Paste each block into ChatGPT image generation, save the PNG under the FILE NAME shown, and drop the files in images/
(or hand them over for processing). Pages pick up figures automatically on the next generator run.
    python3 tools/special_nurse_roles/build_image_prompts.py [--copy-to "<folder>"]
"""
import collections, html, importlib.util, json, shutil, sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
spec = importlib.util.spec_from_file_location("sdnr_images", ROOT / "tools/special_nurse_roles/content/images.py")
I = importlib.util.module_from_spec(spec); spec.loader.exec_module(I)
OUT = ROOT / "docs" / "special-dialysis-nurse-roles"
AUDIENCE = "Philippine registered nurses who hold a portfolio in a hemodialysis unit (college-level readers), their preceptors and head nurses"
ATTR = ('Include a small professional footer reading "© renalcarematters.com" at the bottom-right corner, in a small sans-serif font '
        '(Inter), medium gray (#6b7280), opacity no lower than 70%, never inside a node or overlapping arrows, with a clear page-edge margin.')

NEG_HERO = """Avoid: busy layouts, collage overload, more than four supporting scenes, dozens of icons, tiny unreadable labels,
infographic clutter, duplicated people, repeated compositions, cropped circle, cropped objects, cropped anatomy, edge
clipping, objects touching the circular border, important content inside the title safe zone, baked-in text, titles,
captions, logos, watermarks, rectangular borders, frames, banners, dark / charcoal / black backgrounds, cartoon style,
neon, HDR, over-saturation, distorted hands or faces, implausible anatomy, real brand names on machines or supplies."""

NEG_FIG = """Avoid cartoon style, avoid clutter, avoid tiny unreadable labels, avoid AI gibberish text, avoid unrealistic anatomy,
avoid overprocessed HDR, avoid excessive saturation, avoid brand names and logos, avoid readable patient names or data.
NEVER use dark, navy, charcoal, or black backgrounds — light backgrounds only. Use ONLY the sans-serif font Inter — no other
fonts, no serif fonts, no decorative or handwritten typefaces. Never omit the © renalcarematters.com attribution."""

SCAFFOLD = {
    "A": ("Clinical algorithm (williamriveromd-algorithm-generator-skill)", "2:3 portrait",
          "Clean clinical algorithm in a KDIGO / AHA guideline-flowchart aesthetic, white (#ffffff) background, centered top-to-bottom logic, title at top in bold navy (#0f1e2e) Inter. Rounded rectangles for action nodes, diamonds for decision nodes, thin directional arrows, consistent node size and padding, muted pastel medical colors: decision teal (#1a6b72), action navy, caution amber (#b8860b), escalation red (#b91c1c), safe-path green (#1f7a4d). Maximum 3–4 branching levels, generous margins, no photorealistic people, no decorative icons, mobile-readable labels."),
    "B": ("Simple figure — side-by-side comparison (williamriveromd-simple-figure, scaffold B)", "3:2 landscape",
          "Medical education comparison infographic, AJKD/NEJM graphical-abstract style, white (#ffffff) background, title centered at top in bold navy (#0f1e2e) Inter, soft dashed dividers between equal rounded panels, ample negative space, mobile-readable labels of at least 11 pt."),
    "C": ("Simple figure — step sequence (williamriveromd-simple-figure, scaffold C)", "3:2 landscape",
          "Clean clinical education infographic, white (#ffffff) background, title at top center in bold navy (#0f1e2e) Inter. Rounded rectangular cards on a very soft gray panel (#f3f4f6), connected by bold navy arrows; each card has a colored top accent band, a small line icon, a bold label and 1–3 short details. Generous whitespace, mobile-readable."),
    "D": ("Simple figure — one-panel poster (williamriveromd-simple-figure, scaffold D)", "3:2 landscape",
          "Medical teaching poster, AJKD/NEJM graphical-abstract style, white (#ffffff) background, title at top in bold navy (#0f1e2e) Inter, subtitle in clinical teal (#1a6b72). One central diagram or chart with labeled callouts in modular rounded cards and color-coded arrows; bottom strip with the practical rule in navy. Ample negative space, no clutter."),
    "E": ("Simple figure — reference card (williamriveromd-simple-figure, scaffold E)", "1:1 square",
          "Clinical reference card, publication-grade nephrology design, white (#ffffff) background, bold navy title at top in Inter, compact well-organized grid, headers in teal (#1a6b72) on soft gray (#f3f4f6), alternating row fills, key items highlighted in amber or red where clinically significant, short footer takeaway."),
    "M": ("Mechanism poster (williamriveromd-biomedical-mechanism-figure layout, semi-photorealistic render)", "3:2 landscape",
          "Publication-grade biomedical mechanism poster in the renalcarematters.com house style: white (#ffffff) background, title at top in bold navy (#0f1e2e) Inter, subtitle in clinical teal (#1a6b72). An organ-level panel, a thin dashed magnified inset of the functional unit, and a bottom injury → intervention → benefit summary strip. Semi-photorealistic 3D-rendered anatomy and objects with soft studio lighting (NOT flat vector, NOT clip art), color-coded arrows (teal normal or protective, red harm, green the fix), muted clinical palette, labels of at most five words each, generous whitespace."),
    "P": ("Instructional photo strip (williamriveromd-infographic-skill procedural style)", "3:2 landscape",
          "Clean instructional photo strip on a white (#ffffff) background, title at top in bold navy (#0f1e2e) Inter. Four to six equal photorealistic panels in a single row, each a tightly framed close-up in a bright modern Philippine hemodialysis unit with Filipino staff and patients, consistent lighting and color grade, a small teal number badge in each panel corner and a one-line caption under each panel. Correct practice framed in green (#1f7a4d); unsafe practice marked with a clean red (#b91c1c) X in the corner. No readable text on labels, screens or papers inside the photos."),
}
RATIO = {"1536 × 1024": "3:2 landscape", "1024 × 1536": "2:3 portrait", "1024 × 1024": "1:1 square"}
NAMES = {"A": "Clinical algorithm", "B": "Comparison", "C": "Step sequence", "D": "One-panel poster", "E": "Reference card",
         "M": "Mechanism poster", "P": "Photo strip"}


def hero_block(key, h):
    stem, arch, cam, people, scene = h
    if people == "no people":
        who, scaffold = "No people.", ("C anatomy" if arch.startswith("F") else "B still-life")
    elif people == "hands only":
        who, scaffold = "Hands only, no faces.", "B still-life"
    else:
        who, scaffold = f"People: {people}; Filipino, with features, ages, hairstyles, clothing and posture clearly different from other Academy heroes.", "A people"
    render = "semi-photorealistic 3D medical illustration" if arch.startswith("F") else "photorealistic editorial photograph"
    variation = people if people in ("no people", "hands only") else "new cast; at least 12 traits differ from the previous Academy hero (age, sex, face shape, hairstyle, hair length, build, skin tone within Filipino diversity, clothing style and color, accessories, posture, hand position, expression, setting)"
    return f"""```
FILE NAME: {stem}.png
IMAGE TYPE: Circular vignette hero v3 — Scaffold {scaffold}
ASPECT RATIO: 1:1 (square — displayed inside an 85–90% inscribed circle with white margin)
PIXEL DIMENSIONS: 2048 × 2048
COMPOSITION ARCHETYPE: {arch}
CAMERA: {cam}
HUMAN VARIATION (vs. previous guide): {variation}
AUDIENCE: {AUDIENCE}
VISUAL GOAL: One calm, dignified image that tells a portfolio nurse what this module is about at a glance and shows the work as skilled, careful and valued.

PROMPT:
Square 1:1 {render} on a 2048×2048 canvas, composed to be displayed inside a CIRCULAR vignette occupying 85–90% of the canvas diameter with a visible WHITE BORDER around the full circle (the circle never touches the canvas edges). Composition archetype: {arch}. Camera: {cam}.
{who}
Scene: {scene}. Clean, bright, modern Philippine hemodialysis unit or hospital setting, soft natural daylight, gentle shallow depth of field. Machines and supplies are generic, with no brand names.
Visual hierarchy: hero subject 60–70% of the circle; 2–4 supporting elements 20–30%; reserve a 20–25% TITLE SAFE ZONE of soft gradient, clean wall or blurred background on the left side of the circle (no faces, anatomy, icons, objects or callouts inside it).
Calm, reassuring, documentary-realistic color grade harmonizing with clinical teal #1a6b72 and navy #0f1e2e on a light background; soft falloff toward the rim. Full-bleed within the inscribed circle, no rectangular borders, frames or banners.
Absolutely NO text of any kind: no title, caption, label, readable writing on paper or screens, logo, or watermark.

NEGATIVE INSTRUCTIONS:
{NEG_HERO}

QUALITY CHECK:
Square 2048×2048; circle 85–90% with a visible white margin, never cropped; one dominant subject; 20–25% empty title-safe zone; Filipino context where people are shown; correct dialysis anatomy (fistula on the forearm or upper arm, two needles, blood lines to the machine); no text anywhere; crops cleanly inside the circle.
```"""


def fig_block(f):
    name, ratio, base = SCAFFOLD[f["scaffold"]]
    ratio = RATIO.get(f["size"], ratio)
    abbr = "; ".join(f"{a} = {b}" for a, b in f["abbrevs"])
    return f"""```
FILE NAME: {f['stem']}.png
IMAGE TYPE: {name}
ASPECT RATIO: {ratio}
PIXEL DIMENSIONS: {f['size']}
AUDIENCE: {AUDIENCE}
TEACHING PURPOSE: {f['goal']} — {f['why']}
VISUAL GOAL: {f['desc']}

PROMPT:
{base}
Title: "{f['title']}".
Content: {f['content']}
All text in American English, short clinical labels a registered nurse reads at a glance, spelled correctly. Use only the facts and numbers given here; add no other numbers, doses, targets, alarm limits or brand names.{(' Abbreviations that may appear: ' + abbr + '.') if abbr else ''}
{ATTR}

NEGATIVE INSTRUCTIONS:
{NEG_FIG}

QUALITY CHECK:
Mobile-readable, clinically accurate, visually calm, publication-grade, consistent with the renalcarematters.com house style. White or very light background, never dark. Inter only. Every number matches the prompt exactly. Attribution © renalcarematters.com visible bottom-right in gray.
```"""


def blueprint():
    mods = collections.OrderedDict()
    for f in I.FIGURES:
        mods.setdefault(f["mid"], []).append(f)
    g = collections.Counter(f["goal"] for f in I.FIGURES)
    sc = collections.Counter(f["scaffold"] for f in I.FIGURES)
    out = ["# Special Dialysis Nurse Roles · Image plan blueprint", "",
           "Renal Care Academy → Nephrology Nursing Track → By Role → Special Dialysis Nurse Roles. Prepared 24 November 2026.", "",
           "## Aim", "",
           "Every image must help a portfolio nurse do one of three things better:", "",
           "- **Understand** the mechanism or the system behind the role: how a fistula narrows or steals, how germs travel between stations, how salt drives thirst, how erythropoietin and iron feed the marrow, what crosses a dialyzer membrane, why fast fluid removal stuns the heart.",
           "- **Apply** the role at the station: an algorithm, a tracker, a checklist, a loop or a priority ladder the nurse can follow under pressure.",
           "- **Appreciate** why it matters: a silent alarm and the blood it misses, a denominator that hides patients, the trials that set anemia targets, the cost of untreated water.", "",
           "The audience is registered nurses reading on a phone between tasks. So: one idea per figure, labels of five words or fewer, real objects and real Philippine settings, absolute numbers only where the module states them, and the illustrated (GPT-rendered, semi-photorealistic) house aesthetic rather than flat vector clip art.", "",
           "## Skills used", "",
           "- **williamriveromd-hero-vignette (v3)**: 15 circular heroes, 2048 × 2048, 85–90% circle with white margin, 20–25% title-safe zone, no text, rotating archetypes and casts.",
           "- **williamriveromd-algorithm-generator-skill**: portrait clinical algorithms (scaffold A) with diamonds for decisions and the mandatory gray bottom-right © renalcarematters.com footer.",
           "- **williamriveromd-simple-figure**: comparisons (B), step sequences (C), one-panel posters (D) and reference cards (E).",
           "- **williamriveromd-biomedical-mechanism-figure**: mechanism posters (M) with an organ-level panel, a dashed magnified inset and an injury → intervention → benefit strip, rendered semi-photorealistically (the owner dislikes flat vector figures).",
           "- **williamriveromd-infographic-skill**: one procedural photo strip (P) for the hazard round.", "",
           "## Guardrails carried into every prompt", "",
           "- No doses, targets, alarm limits or water limits beyond the numbers each module states and cites. Water quality is shown as a process (release, stop-use, restart), never as a universal number.",
           "- Scope is visible: physicians decide prescriptions, technicians release water and machines, the transplant center decides listing. No image shows a nurse prescribing, adjusting a water system, or signing a technical release.",
           "- No real patients, no readable patient data, no brands or logos, no real facility names. Sensitive topics (organ payment) are shown with neutral icons, never people exchanging money.",
           "- Light backgrounds only, Inter typeface, American English, © renalcarematters.com bottom-right (public Academy set).",
           "- Heroes rotate composition archetypes (A, B, C, D, E, F, G, H, I, J) and casts (age, sex, build, hairstyle, scrub color, headwear) so no two pages share a model look.", "",
           "## Inventory", "",
           f"- {len(I.HEROES)} circular-vignette heroes (hub plus 14 modules; the end-of-course check reuses the hub hero), 2048 × 2048.",
           f"- {len(I.FIGURES)} in-body figures: " + ", ".join(f"{NAMES[k]} {v}" for k, v in sorted(sc.items())) + ".",
           f"- Teaching purpose: Understand {g['Understand']}, Apply {g['Apply']}, Appreciate {g['Appreciate']}.",
           "- Every module has at least two figures; the clinically dense modules (access, infection, safety, anemia, adequacy) have three.", "",
           "## Figure map", "",
           "| ID | Module · section | Type | Purpose | What it teaches | File |",
           "|---|---|---|---|---|---|"]
    for mid, fs in mods.items():
        for f in fs:
            out.append(f"| {f['id']} | M{int(mid)} · `{f['section']}` | {NAMES[f['scaffold']]} | {f['goal']} | {f['desc']} | `{f['stem']}.png` |")
    out += ["", "## Heroes", "", "| Page | Archetype | Camera | Subject | File |", "|---|---|---|---|---|"]
    for k, h in I.HEROES.items():
        subj = h[3] if h[3] in ("no people", "hands only") else "people"
        out.append(f"| {'Hub' if k == 'hub' else 'Module ' + str(int(k))} | {h[1]} | {h[2]} | {subj} | `{h[0]}.png` |")
    out += ["", "## Production workflow", "",
            "1. Open `GPT-IMAGE-PROMPTS.md` and paste one block at a time into ChatGPT image generation.",
            "2. Save each PNG under its exact FILE NAME.",
            "3. Audit each image against its QUALITY CHECK and the guardrails above: spelling, numbers exactly as given, no invented limits or doses, scope boundaries respected, correct dialysis anatomy, Filipino context, light background, attribution present.",
            "4. Drop passing images in the repo's `images/` folder (or hand them over for processing to .webp). Failures go into a new corrected-prompt file with the reason for each.",
            "5. Re-run `python3 generate_special_dialysis_nurse_roles.py --patch`. Figures appear at the end of their sections automatically once the file exists; alt text and plain-language descriptions are already written in `content/images.py`.", ""]
    return "\n".join(out)


def main():
    OUT.mkdir(parents=True, exist_ok=True)
    lines = ["# Special Dialysis Nurse Roles · GPT image prompt pack", "",
             "Generated from `tools/special_nurse_roles/content/images.py` by `tools/special_nurse_roles/build_image_prompts.py`. Read `IMAGE-PLAN-BLUEPRINT.md` first for the purpose of each image.",
             f"{len(I.HEROES)} circular-vignette heroes (williamriveromd-hero-vignette v3) and {len(I.FIGURES)} in-body figures (algorithms A, simple figures B–E, mechanism posters M, photo strip P).",
             "Save each PNG under its FILE NAME. Figures appear on the pages automatically on the next generator run once the image (and its .webp) is in `images/`. The end-of-course knowledge check reuses the hub hero.", "",
             "## Part 1 · Heroes", ""]
    for k, h in I.HEROES.items():
        lines += [f"### {'Hub' if k == 'hub' else 'Module ' + str(int(k))}", "", hero_block(k, h), ""]
    lines += ["## Part 2 · In-body figures", ""]
    for f in I.FIGURES:
        lines += [f"### {f['id']} · Module {int(f['mid'])} · section `{f['section']}` · {f['goal']}", "", f"_Why this image: {f['why']}_", "", fig_block(f), ""]
    (OUT / "GPT-IMAGE-PROMPTS.md").write_text(html.unescape("\n".join(lines)), encoding="utf-8")
    (OUT / "IMAGE-PLAN-BLUEPRINT.md").write_text(html.unescape(blueprint()), encoding="utf-8")
    man = [{"file": h[0] + ".png", "kind": "hero", "page": k, "archetype": h[1]} for k, h in I.HEROES.items()] + \
          [{"file": f["stem"] + ".png", "kind": "figure", "id": f["id"], "module": f["mid"], "section": f["section"], "size": f["size"],
            "scaffold": f["scaffold"], "goal": f["goal"], "alt": f["alt"]} for f in I.FIGURES]
    (OUT / "image-manifest.json").write_text(json.dumps(man, indent=1, ensure_ascii=False), encoding="utf-8")
    print(f"wrote {len(man)} prompts to {OUT.relative_to(ROOT)}/")
    if "--copy-to" in sys.argv:
        dest = Path(sys.argv[sys.argv.index("--copy-to") + 1])
        dest.mkdir(parents=True, exist_ok=True)
        for n in ("GPT-IMAGE-PROMPTS.md", "IMAGE-PLAN-BLUEPRINT.md", "image-manifest.json"):
            shutil.copy(OUT / n, dest / n)
        print(f"copied to {dest}")


if __name__ == "__main__":
    main()
