#!/usr/bin/env python3
"""Build the technician-track blueprint and the GPT image prompt pack from the image_plan_*.py data files.

    python3 tools/techcourses/build_image_brief.py

Writes:
  blueprints/renal-care-academy-technician-tracks-blueprint.md   curriculum blueprint + image plan (handoff)
  docs/tech-courses/GPT-IMAGE-PROMPTS.md                          one Constitution v1.0 prompt per figure
  docs/tech-courses/image-prompts-manifest.json                   machine-readable list for installation
"""
import importlib.util, json, sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
sys.path.insert(0, str(HERE))
PREPARED = "November 23, 2026"
FOOTER = "© renalcarematters.com"
CANVAS = {"landscape": "1672 × 941, 16:9 landscape", "portrait": "1024 × 1536, 2:3 portrait", "hero": "2048 × 2048, 1:1"}
KIND = {
    "aid": ("Atlas visual aid", "A labeled teaching illustration. Realistic, softly shaded, illustrated atlas rendering of real equipment and people; not flat vector icons, not clip art."),
    "flow": ("Process or decision figure", "A sequence or decision figure. Each step is a small illustrated panel or tile with one short label, joined by clear arrows in reading order."),
    "card": ("Reference card", "A compact reference card with a few illustrated tiles. Large, legible type; generous spacing."),
}
BAR = "════════════════════════════════════"
UNIVERSAL_NEG = [
    "No mirrored anatomy or mirrored equipment",
    "No cartoon style, no flat clip-art icons",
    "No garbled or unreadable text; no text other than the verbatim labels and the footer",
    "No prompt text or production metadata visible in the image",
    f"No missing attribution footer — `{FOOTER}` appears on the image",
    "No altered attribution text — not \"Renal Care Matters\", not www.renalcarematters.com, not any other domain",
    "No attribution footer overlapping content, and none rendered large, centered, or in a color other than navy #1F3864",
    "No anatomy visible through opaque skin",
    "No manufacturer logos, brand names, or recognizable proprietary machine designs",
    "No identifiable real people, patient records, or readable screen values",
    "No dark background",
    "No numbers, limits, doses, or settings other than those written in the label list",
]


def load(name):
    spec = importlib.util.spec_from_file_location(name, HERE / f"{name}.py")
    m = importlib.util.module_from_spec(spec); spec.loader.exec_module(m); return m


def hd_slugs():
    spec = importlib.util.spec_from_file_location("hdc", HERE / "hd_technician" / "course.py")
    m = importlib.util.module_from_spec(spec); spec.loader.exec_module(m)
    return {r["id"]: f"hemodialysis-technician-{r['id']}-{r['slug']}" for r in m.MODULES}


def hero_prompt(scene, alt, where):
    return f"""Circular vignette hero · {CANVAS['hero']} · {where}

{BAR}
CONSTITUTION v1.0 — LAYER A: ANATOMICAL TRUTH BLOCK
Scene: {scene}
People are adult Filipino staff in plain scrubs or work uniform. Equipment is generic and plausible: correct proportions, tubing and pipes that connect to something, gauges with unreadable faces. No anatomy is shown; no needles, no blood, no patient unless the scene names one.

{BAR}
CONSTITUTION v1.0 — LAYER B: SPATIAL ORIENTATION
One circular picture centered on a pure white square canvas. The circle fills 85 to 90 percent of the canvas with an even white margin. The focal point (hands and the object being checked, or faces) sits in the middle third so it survives a small mobile crop.

{BAR}
CONSTITUTION v1.0 — LAYER C: RENDER SPECIFICATIONS
Realistic clinical editorial illustration with natural daylight, calm and competent mood, muted teal and navy with warm neutrals. Shallow depth of field. This hero carries NO text of any kind: no labels, no caption, no footer, no signage that can be read. (House rule for heroes: the page supplies the title and attribution.)

{BAR}
CONSTITUTION v1.0 — LAYER D: IMAGING PHYSICS
No clinical imaging modality depicted.

{BAR}
CONSTITUTION v1.0 — LAYER E: NEGATIVE CONSTRAINTS
✗ No text, letters, numbers, logos, or watermarks anywhere
✗ No cartoon style
✗ No manufacturer logos or recognizable proprietary equipment
✗ No identifiable real person; no readable badges, records, or screens
✗ No patient connected to a machine unless the scene says so
✗ No needles, blood, or open wounds
✗ No impossible equipment: pipes or tubing ending in mid-air, gauges without connections
✗ No extra fingers, distorted hands, or duplicated limbs
✗ No dark or colored background outside the circle
✗ No square or rectangular crop; the picture is a circle on white
✗ No prompt text or production metadata visible

{BAR}
CONSTITUTION v1.0 — LAYER F: STYLE REFERENCE
Existing Renal Care Matters course heroes (nephrology-nursing-NN-…-vignette-hero.png). Realistic documentary-style illustration of Philippine kidney care settings. Palette: NAVY #1F3864 · TEAL #1A6B72 with warm neutral skin and wood tones.

{BAR}
CONSTITUTION v1.0 — LAYER G: QA CHECKLIST
□ Output is 2048 × 2048 with a circular picture on pure white — confirmed
□ Circle fills 85 to 90 percent of the canvas — confirmed
□ Scene matches the description — confirmed
□ No text, numbers, or logos anywhere — confirmed
□ Hands and faces anatomically correct — confirmed
□ Equipment generic, plausible, and connected — confirmed
□ No patient, needle, or blood unless specified — confirmed
□ Focal point in the middle third — confirmed
□ Protective equipment shown where the scene requires it — confirmed
□ No readable screens, badges, or records — confirmed
□ No prompt text visible — confirmed
□ Suitable alt text: "{alt}" — confirmed"""


def fig_prompt(f, where):
    kname, kdesc = KIND[f["kind"]]
    labels = "\n".join(f"  • {x}" for x in f["labels"])
    negs = "\n".join(f"✗ {x}" for x in UNIVERSAL_NEG + f["negatives"] + [
        "No label spelled differently from the verbatim list",
        "No extra panels, steps, or tiles beyond those described",
        "No arrows pointing against the described direction of flow or sequence",
        "No crowded layout: every label has clear space around it"])
    qa = [f"Label \"{x}\" present and spelled exactly — confirmed" for x in f["labels"][:8]]
    qa += ["Number of panels, steps, or tiles matches the description — confirmed",
           "Flow and sequence arrows point the described way — confirmed",
           "No numbers other than those in the label list — confirmed",
           "No brand names, logos, or readable screens — confirmed",
           "Illustrated atlas rendering, not flat vector clip art — confirmed",
           "No anatomy visible through skin — confirmed",
           "No garbled labels — confirmed",
           "No prompt text visible in the generated image — confirmed",
           "Attribution footer present in the bottom-right corner — confirmed",
           f"Attribution reads exactly \"{FOOTER}\" (lowercase, no www, no https://) — confirmed",
           "Attribution footer legible, navy #1F3864, and not overlapping content — confirmed"]
    qa = "\n".join(f"□ {x}" for x in qa)
    return f"""{kname} · {CANVAS[f['canvas']]} · {f['title']} · {where}

{BAR}
CONSTITUTION v1.0 — LAYER A: ANATOMICAL TRUTH BLOCK
{f['truth']}
Where a person appears, anatomy is correct and skin is opaque. Where equipment appears, it is generic and technically plausible: every pipe, tube, and wire connects to something, and flow has one consistent direction.

{BAR}
CONSTITUTION v1.0 — LAYER B: SPATIAL ORIENTATION
{CANVAS[f['canvas']]}. {"Steps read top to bottom." if f['canvas'] == 'portrait' else "Reading order left to right, top to bottom."} White background. Nothing mirrored. Keep the main subject within the central 80 percent so labels are not cut off.

{BAR}
CONSTITUTION v1.0 — LAYER C: RENDER SPECIFICATIONS
{kdesc}
Learning purpose — {f['job']}
Render these labels verbatim, each once, in plain American English, with clean leader lines or inside their tiles. Render no other text:
{labels}
Attribution footer: `{FOOTER}` in the bottom-right corner — small, navy #1F3864, DM Sans, clear of all content.

{BAR}
CONSTITUTION v1.0 — LAYER D: IMAGING PHYSICS
No clinical imaging modality depicted.

{BAR}
CONSTITUTION v1.0 — LAYER E: NEGATIVE CONSTRAINTS
{negs}

{BAR}
CONSTITUTION v1.0 — LAYER F: STYLE REFERENCE
Existing Renal Care Matters atlas and guide figures (for example wts-treatment-train-flow.png, access-hd-blood-circuit.png, dialyzer-reprocessing-6-steps.png): realistic illustrated rendering with labeled callouts. White background. Palette: NAVY #1F3864 · TEAL #1A6B72 · ORANGE #C55A11 · GREEN #2E6B3E · RED #C00000 · PURPLE #4B3280 · AMBER #C9A84C. Blood-path colors where blood is shown: arterial red #C00000, venous blue #1F6FC0, dialysate teal #1A6B72. Typography: DM Sans for labels, DM Mono for technical terms. Attribution footer `{FOOTER}`, bottom right, small, navy, exact lowercase string.

{BAR}
CONSTITUTION v1.0 — LAYER G: QA CHECKLIST
{qa}"""


def main():
    tracks = [load(n).TRACK for n in ("image_plan_hd", "image_plan_water", "image_plan_biomed")]
    hd = hd_slugs()
    manifest, prompts, plan_rows = [], [], []
    bp = []
    for T in tracks:
        pre = T["prefix"]
        expanded = isinstance(T["modules"][0], dict)
        prompts.append(f"\n# {T['title']}\n")
        if T["hub_hero"]:
            scene, alt = T["hub_hero"]
            fid = f"{T['key'].upper()}-H0"
            file = f"images/{pre}-vignette-hero.png"
            where = f"hub page academy/{pre}.html, hero"
            manifest.append({"id": fid, "track": T["key"], "module": None, "kind": "hero", "core": True, "title": f"{T['title']} hub hero", "file": file,
                             "canvas": CANVAS["hero"], "placement": where, "alt": alt, "review": "Dr. Rivero"})
            prompts.append(f"## {fid} — Hub hero\n\n**File:** `{file}` · **Alt:** {alt}\n\n```text\n{hero_prompt(scene, alt, where)}\n```\n")
            plan_rows.append((fid, "★", "Hub hero", file, "hero"))
        for mod in T["modules"]:
            if expanded:
                mid, title, figs = mod["id"], mod["title"], mod["figs"]
                page = f"{pre}-{mid}-{mod['slug']}"
            else:
                mid, title, figs = mod
                page = hd[mid]
            prompts.append(f"\n## Module {int(mid)} — {title}\n")
            if expanded:
                fid = f"{T['key'].upper()}-{mid}-H"
                file = f"images/{page}-vignette-hero.png"
                alt = mod["hero"].rstrip(".") + "."
                where = f"module page academy/{page}.html, hero"
                manifest.append({"id": fid, "track": T["key"], "module": mid, "kind": "hero", "core": True, "title": f"Module {int(mid)} hero", "file": file,
                                 "canvas": CANVAS["hero"], "placement": where, "alt": alt, "review": "Dr. Rivero"})
                prompts.append(f"### {fid} — Module hero\n\n**File:** `{file}` · **Alt:** {alt}\n\n```text\n{hero_prompt(mod['hero'], alt, where)}\n```\n")
                plan_rows.append((fid, "★", f"M{int(mid)} hero", file, "hero"))
            for f in figs:
                fid = f"{T['key'].upper()}-{mid}-{f['letter']}"
                slot = "teaching-diagram" if (not expanded and f["letter"] == "A" and mid != "01") else f["slug"]
                file = f"images/{page}-{slot}.png" if slot == "teaching-diagram" else f"images/{pre}-{mid}-{f['slug']}.png"
                where = f"academy/{page}.html, section `{f['section']}`"
                star = "★" if f["core"] else "○"
                entry = {"id": fid, "track": T["key"], "module": mid, "kind": f["kind"], "core": f["core"], "title": f["title"], "file": file,
                         "canvas": CANVAS[f["canvas"]], "placement": where, "job": f["job"], "alt": f["alt"],
                         "replaces": "existing flat teaching diagram (same filename)" if slot == "teaching-diagram" else "",
                         "review": "Dr. Rivero" + ("; chief technician" if T["key"] != "hd" else "; head nurse")}
                manifest.append(entry)
                plan_rows.append((fid, star, f["title"], file, f["kind"]))
                head = f"### {fid} {star} — {f['title']}\n\n**File:** `{file}` · **Canvas:** {CANVAS[f['canvas']]} · **Placement:** {where}\n\n**Job:** {f['job']}\n\n**Alt:** {f['alt']}\n"
                if entry["replaces"]:
                    head += "\n**Replaces** the current flat teaching diagram; saving under this filename swaps it in with no code change.\n"
                if f["kind"] == "circuit":
                    prompts.append(head + f"\n> **Circuit figure.** Do not write a new layout. Generate this prompt with the `dialysis-circuit-schematic` skill (modality: intermittent hemodialysis), which locks the port colors, flow directions, and pressure points. Emphasis for this figure: {f['truth']}\n")
                else:
                    prompts.append(head + f"\n```text\n{fig_prompt(f, where)}\n```\n")
        # blueprint section per track
        bp.append(f"\n## {T['title']}\n")
        if expanded:
            bp.append("| No. | Module | Origin | Opening case | Skills checklist |\n|---|---|---|---|---|")
            for m in T["modules"]:
                bp.append(f"| {int(m['id'])} | {m['title']} | {m['origin']} | {m['case']} | {m['skills']} |")
            bp.append("")
            for m in T["modules"]:
                bp.append(f"**Module {int(m['id'])}. {m['title']}** (`{pre}-{m['id']}-{m['slug']}`) — Teach: {m['teach']} Figures: " +
                          "; ".join(f"{x['letter']}{'' if x['core'] else ' ○'} {x['title']}" for x in m["figs"]) + ".\n")
        else:
            bp.append("Twelve modules are kept as built. The image plan replaces each flat teaching diagram with an illustrated figure (A) and adds two more per module.\n")
            bp.append("| No. | Module | Figures (○ = optional) |\n|---|---|---|")
            for mid, title, figs in T["modules"]:
                bp.append(f"| {int(mid)} | {title} | " + "; ".join(f"{x['letter']}{'' if x['core'] else ' ○'} {x['title']}" for x in figs) + " |")
    n = len(manifest)
    core = sum(1 for m in manifest if m["core"])
    heroes = sum(1 for m in manifest if m["kind"] == "hero")
    circ = sum(1 for m in manifest if m["kind"] == "circuit")
    table = "\n".join(f"| {i} | {a} {b} | {c} | `{d}` | {e} |" for i, (a, b, c, d, e) in enumerate(plan_rows, 1))
    head = f"""# GPT image prompts — Renal Care Academy technician tracks

**Site:** renalcarematters.com · **Prepared:** {PREPARED} · **Images:** {n} ({core} core ★, {n - core} optional ○; {heroes} heroes, {circ} circuit figures)

This file is self-contained. Each gray block is one complete Constitution v1.0 prompt: paste it into a fresh ChatGPT image chat, generate, then run its Layer G checklist before saving under the filename on the entry.

## How to produce

1. One figure per chat. Ask for the canvas size on the entry.
2. Check text first: compare every label with the verbatim list. If one word is wrong, ask for that word to be fixed, not for a new image.
3. Reject an image with an invented number, a brand, a dark background, flat clip-art rendering, or a missing or altered footer (`{FOOTER}`). Heroes are the exception: they carry no text at all.
4. Circuit figures (marked in the list) are generated with the `dialysis-circuit-schematic` skill, not from a prompt in this file.
5. Save as PNG under the exact filename into `images/`, then run `python3 tools/techcourses/prep_assets.py` and `python3 generate_tech_courses.py --patch`. Hemodialysis Technician figure A of each module replaces the flat teaching diagram automatically; other figures appear once they are added to `tools/techcourses/figs.py` and placed with a `{{{{fig:key}}}}` macro in the module.
6. Production order: core figures first, track by track; optional figures last.
7. Every figure needs Dr. Rivero's review before publication. Numbers appear only where the lesson states them.

## Production list

| # | ID | Figure | File | Type |
|---|---|---|---|---|
{table}
"""
    docs = ROOT / "docs" / "tech-courses"
    docs.mkdir(parents=True, exist_ok=True)
    (docs / "GPT-IMAGE-PROMPTS.md").write_text(head + "\n".join(prompts), encoding="utf-8")
    (docs / "image-prompts-manifest.json").write_text(json.dumps(manifest, indent=1, ensure_ascii=False), encoding="utf-8")
    blueprint = (HERE / "blueprint_head.md").read_text(encoding="utf-8").replace("{{COUNTS}}", f"{n} images: {core} core and {n - core} optional, including {heroes} heroes and {circ} circuit figures") \
        + "\n".join(bp) + "\n" + (HERE / "blueprint_tail.md").read_text(encoding="utf-8")
    (ROOT / "blueprints").mkdir(exist_ok=True)
    (ROOT / "blueprints" / "renal-care-academy-technician-tracks-blueprint.md").write_text(blueprint, encoding="utf-8")
    print(f"{n} images ({core} core, {n - core} optional; {heroes} heroes, {circ} circuit). Wrote blueprint, prompt pack, and manifest.")


if __name__ == "__main__":
    main()
