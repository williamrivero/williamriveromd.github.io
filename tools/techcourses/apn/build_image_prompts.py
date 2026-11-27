# -*- coding: utf-8 -*-
"""Build the Attending Pediatric Nephrologist image plan blueprint and GPT prompt pack (one Markdown file).
Sources: course.py (pages), figs.py (file, alt, caption), parts/imgplan_NN.json (figure type, purpose, content, hero and card scenes).
Skills applied: williamriveromd-hero-vignette v3 (heroes), williamriveromd-simple-figure / algorithm-generator /
biomedical-mechanism-figure (figures), williamriveromd-infographic-skill (tiles, OG), dialysis-circuit-schematic (circuit
figures), tunneled-dialysis-catheter-path (catheter figures), Constitution v1.0 QA where anatomy appears.
Run:  python3 build_image_prompts.py <output.md>"""
import html as _h
import importlib.util
import json
import re
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent


def _load(name, f):
    s = importlib.util.spec_from_file_location(name, HERE / f); m = importlib.util.module_from_spec(s); s.loader.exec_module(m); return m


C = _load("apn_course", "course.py"); F = _load("apn_figs", "figs.py")
HUB = C.HUB
MODS = {m["id"]: m for m in C.MODULES}
PLANS = {}
for f in sorted((HERE / "parts").glob("imgplan_*.json")):
    PLANS[f.stem.split("_")[1]] = json.loads(f.read_text(encoding="utf-8"))

# Archetype and camera rotation (hero-vignette v3): no two consecutive pages share either.
ROT = [("J Environmental Storytelling", "wide-angle eye-level"), ("H Clinical", "over-the-shoulder"), ("F Anatomy", "three-quarter macro"),
       ("A Editorial Portrait", "three-quarter close"), ("I Object Hero", "macro side view"), ("B Journey", "low side angle"),
       ("E Lifestyle", "overhead three-quarter"), ("C Radial", "top-down"), ("D Panorama", "wide low angle"), ("G Infographic", "straight-on")]
PEOPLE_WORDS = ("boy", "girl", "mother", "father", "nurse", "physician", "doctor", "nephrologist", "infant", "baby", "newborn", "toddler",
                "child", "family", "woman", "man ", "parent", "grandmother", "teen", "adolescent", "resident", "surgeon", "aunt", "sister")
PEOPLE_ROT = [("J Environmental Storytelling", "wide-angle eye-level"), ("H Clinical", "over-the-shoulder"), ("A Editorial Portrait", "three-quarter close"),
              ("B Journey", "low side angle"), ("E Lifestyle", "overhead three-quarter"), ("D Panorama", "wide low angle"),
              ("C Radial", "top-down"), ("H Clinical", "eye-level close"), ("A Editorial Portrait", "profile"), ("J Environmental Storytelling", "rear three-quarter")]
OBJECT_ROT = [("I Object Hero", "macro side view"), ("F Anatomy", "three-quarter macro"), ("G Infographic", "straight-on")]
# Cast rotation: age band of the child and the adult present, so every hero has a new cast.
CAST = ["a newborn and a young mother", "a toddler and a grandmother", "a school-age girl and her father", "a teenage boy and an older sister",
        "an infant and both parents", "a preschool boy and his mother", "a pre-teen girl and a pediatric nurse", "an adolescent girl alone with a physician",
        "school-age twins and an aunt", "a teenage boy and a male pediatric nephrologist"]

NEG_HERO = ("Avoid: duplicated people, repeated compositions, cropped circle, objects touching the circular border, important content inside "
            "the title safe zone, baked-in text, titles, captions, logos, watermarks, rectangular borders, frames, dark / charcoal / black "
            "backgrounds, cartoon style, neon, HDR, over-saturation, distorted hands or faces, implausible anatomy, a child in distress or pain "
            "shown graphically, needles entering a child's skin in close-up, any exposure beyond what a clinical exam requires. Never show a "
            "blood pressure cuff, band or watch on a fistula arm, a PD catheter exiting at the beltline or in a diaper area, or adult-size "
            "equipment on a small child unless the scene is about that mismatch.")
NEG_FIG = ("Avoid cartoon style, clutter, tiny unreadable labels, AI gibberish text, unrealistic anatomy, overprocessed HDR, excessive saturation. "
           "NEVER use dark, navy, charcoal or black backgrounds — light backgrounds only. Use ONLY Inter (sans-serif). No brand names, logos, "
           "agency seals, real names or readable patient data. NO DRUG DOSES, fill volumes, blood-flow settings or order values unless they "
           "appear word for word in CONTENT. Never omit the renalcarematters.com attribution, exactly lowercase (no www, no https://).")
TYPE_SCAFFOLD = {"Mechanism poster": "williamriveromd-biomedical-mechanism-figure: organ-level panel, dashed magnified inset, injury → intervention → benefit strip, semi-photorealistic",
                 "Clinical algorithm": "williamriveromd-algorithm-generator-skill: portrait clinical algorithm, rounded rectangles for actions, diamonds for decisions, red stop boxes, gray © renalcarematters.com footer bottom-right",
                 "Comparison": "williamriveromd-simple-figure scaffold B: two or three side-by-side panels with matched rows",
                 "Step sequence": "williamriveromd-simple-figure scaffold C: numbered left-to-right or top-to-bottom steps with one icon each",
                 "Reference card": "williamriveromd-simple-figure scaffold E: grid reference card with short rows",
                 "One-panel poster": "williamriveromd-simple-figure scaffold D: one strong visual with up to five callouts"}
SIZE = {"Clinical algorithm": ("1024 × 1536", "2:3 portrait"), "Reference card": ("1536 × 1152", "4:3")}
CIRCUIT_LOCK = """CIRCUIT LOCK (dialysis-circuit-schematic; overrides style): RED #C00000 = blood leaving the child (arterial limb), BLUE #1F6FC0 = blood returning (venous limb); blood pump on the RED line only; three pressure monitors in order access (negative) → pre-filter (inline between pump and filter) → venous; air detector INLINE on the BLUE line and the LAST component before the child's blue hub; filter END CAPS carry blood only (red bottom inlet, blue top outlet, blood ascends), SIDE PORTS carry fluid only; replacement fluid GREEN #2E6B3E joins the blood line as a short stub at a tee and never enters a side port; dialysate/effluent TEAL #1A6B72; one dual-lumen catheter with a red and a blue capped hub, hubs at the heights of the lines they join, lines meeting hub tips end to end (no arrowhead standing in for a connection). Pick ONE modality and make every panel agree with it. For a child: show the circuit and filter visibly SMALLER (pediatric lines and filter) and, where the content asks, a blood-prime bag on the arterial side labeled exactly as CONTENT states."""
CATH_LOCK = """ANATOMY LOCK — CATHETER PATH (tunneled-dialysis-catheter-path; follow exactly): anterior view, the child's RIGHT on the IMAGE LEFT; the whole catheter on the child's right, never crossing the midline. (1) Exit site on the right upper anterior chest wall below the clavicle, paramedian, above the nipple line; a hub splits into a RED-capped arterial limb and a BLUE-capped venous limb hanging downward. (2) Cream-white Dacron cuff INSIDE the subcutaneous tunnel just above the exit site. (3) Tunnel runs upward under the skin, passing OVER the medial clavicle, never beneath it. (4) One smooth shepherd's-crook loop just above the clavicle into the LOW right internal jugular vein, lateral to the carotid. (5) Down the right internal jugular → right brachiocephalic → superior vena cava → right atrium. (6) Tip in the upper-to-mid right atrium. Child-proportioned torso (shorter neck, proportionally larger head and heart). Never: subclavian route, exit in the neck, external cuff, kink or double loop, tip in the right ventricle or high SVC, swapped clamp colors, mirrored anatomy."""


def hero_block(key, i):
    if key == "hub":
        fname, title, brief = f"{HUB}-vignette-hero.png", "Course home (reused by the final exam and trainer pages)", C.COURSE["hero_alt"]
        scene = C.COURSE["hero_alt"]
    else:
        m = MODS[key]
        fname, title, brief = f"{HUB}-{key}-{m['slug']}-vignette-hero.png", f"Module {int(key)} · {m['title']}", m["sub"]
        scene = PLANS.get(key, {}).get("hero", m["hero_brief"])
    low = scene.lower()
    has_people = any(w in low for w in PEOPLE_WORDS)
    rot = PEOPLE_ROT if has_people else OBJECT_ROT
    arch, cam = rot[i % len(rot)]
    anatomy = not has_people
    people = ("as described in the scene; Filipino, with faces, ages, hairstyles, clothing and posture clearly different from every other "
              "Academy hero (a new cast)") if has_people else "no people, or hands only"
    lock = ""
    if "catheter" in low and "peritoneal" not in low and "pd catheter" not in low:
        lock = ("\nCATHETER (external view only, tunneled-dialysis-catheter-path): a small clean dressing on the child's RIGHT upper chest below the "
                "collarbone, with two short limbs ending in a RED cap and a BLUE cap hanging downward from a hub; nothing in the neck; no internal "
                "path drawn through the skin; never on the left or crossing the midline.")
    if "pd catheter" in low or ("peritoneal" in low and "catheter" in low):
        lock = ("\nPD CATHETER (external view only): exits the lower abdomen below and to the side of the navel, pointing DOWNWARD, away from the "
                "beltline and any diaper; covered by a small clean dressing; tubing coiled and secured.")
    return f"""### {title}

Teaching purpose: Appreciate. {brief}

```
FILE NAME: {fname}
IMAGE TYPE: Circular vignette hero v3 (williamriveromd-hero-vignette)
ASPECT RATIO: 1:1 (displayed inside an 85–90% inscribed circle with white margin)
PIXEL DIMENSIONS: 2048 × 2048
COMPOSITION ARCHETYPE: {arch}
CAMERA: {cam}
HUMAN VARIATION: {"hands only or no people" if anatomy else "new cast; at least 12 traits differ from the previous hero (age, sex, face shape, hairstyle, hair length and color, build, skin tone within Filipino diversity, clothing, accessories, posture, hand position, expression)"}
AUDIENCE: attending pediatric nephrologists and fellows; plain-language readable for families

PROMPT:
Square 1:1 semi-photorealistic editorial image on a 2048×2048 canvas, composed for a CIRCULAR vignette occupying 85–90% of the canvas diameter with a visible WHITE BORDER around the full circle (never touching the edges). Composition archetype: {arch}. Camera: {cam}.
People: {people}.
Scene: {scene} Clean, bright Philippine hospital, clinic or home setting, soft natural daylight, gentle shallow depth of field. Children look safe, cared for and dignified; families are present and involved.{lock}
Visual hierarchy: hero subject 60–70% of the circle; 2–4 supporting elements 20–30%; reserve a 20–25% TITLE SAFE ZONE of soft gradient, clean wall or blurred background on one side (no faces, anatomy, icons or objects inside it).
Calm, warm, documentary-realistic color grade harmonizing with teal #1a6b72 and navy #0f1e2e on a light background. No rectangular borders, frames or banners.
Absolutely NO text of any kind: no title, caption, label, readable writing on paper or screens, logo or watermark.

NEGATIVE INSTRUCTIONS:
{NEG_HERO}

QUALITY CHECK:
Square 2048×2048; circle 85–90% with a white margin, never cropped; one dominant subject; 20–25% empty title-safe zone; Filipino context; equipment sized to the child; no text anywhere.
```
"""


def fig_block(key, idx, plan, modkey):
    fname, alt, cap = F.FIGS[key]
    png = fname.replace(".webp", ".png")
    typ = plan.get("type", "One-panel poster").split("|")[0].strip()
    size, ratio = SIZE.get(typ, ("1792 × 1024", "16:9 landscape"))
    pos = "bottom-center" if "portrait" in ratio else "bottom-right"
    content = plan.get("content", alt)
    low = (content + " " + cap).lower()
    locks = ""
    drawn = typ in ("Mechanism poster", "One-panel poster", "Comparison")  # schematic locks only where the circuit or catheter is drawn
    if drawn and any(w in low for w in ("circuit", "dialyzer", "hemofilter", "blood pump", "ckrt", "crrt", "extracorporeal")):
        locks += "\n" + CIRCUIT_LOCK
    if drawn and ("tunneled" in low or "permcath" in low or ("catheter" in low and ("jugular" in low or "central" in low or "hd catheter" in low))):
        locks += "\n" + CATH_LOCK
    anatomy = any(w in low for w in ("nephron", "glomerul", "podocyte", "kidney", "bladder", "peritone", "fistula", "vein", "heart", "brain", "membrane"))
    qa = ["□ Light (white or #fafafa) background", "□ Every label spelled exactly as written, American English, Inter font",
          "□ One concept; labels five words or fewer", "□ Numbers appear exactly as in CONTENT and nowhere else (no invented doses, volumes or limits)",
          "□ No readable brand, real name or patient data", f"□ Attribution renalcarematters.com at the {pos}, small, navy, 70% opacity, exact lowercase, not overlapping content"]
    if anatomy:
        qa += ["□ Anatomy plausible and child-proportioned where a child is shown (Constitution v1.0 anatomical truth); internal anatomy shown in a labeled inset, never drawn through a photographed child's skin"]
    if "CIRCUIT LOCK" in locks:
        qa += ["□ Circuit: pump on red line; access → pre-filter → venous gauges; air detector last before the blue hub; blood at end caps only; one modality throughout"]
    if "ANATOMY LOCK" in locks:
        qa += ["□ Catheter: chest exit → cuff in tunnel → over clavicle → one loop into low right IJV → SVC → tip in right atrium; on image left; red arterial, blue venous"]
    qa = "\n".join(qa)
    return f"""### APN-F{idx:02d} · {key}

Placement: Module {int(modkey)} · Teaching purpose: **{plan.get('purpose', 'Understand')}** · Teaches: {plan.get('teaches', cap)}

```
FILE NAME: {png}   (convert to {fname} for the site)
IMAGE TYPE: {typ} — {TYPE_SCAFFOLD.get(typ, TYPE_SCAFFOLD['One-panel poster'])}
ASPECT RATIO: {ratio}
PIXEL DIMENSIONS: {size}
AUDIENCE: attending pediatric nephrologists and fellows (plain-language glosses for families)
VISUAL GOAL: {cap}

PROMPT:
Clean clinical education figure in the renalcarematters.com house style, AJKD/NEJM graphical-abstract aesthetic, semi-photorealistic illustration (not flat vector clip art, not cartoon). White (#ffffff) background with soft gray (#f3f4f6) or light teal (#eef6f7) cards. Typography: Inter only; bold navy (#0f1e2e) title, teal (#1a6b72) subheadings; renal green (#1f7a4d) for safe or expected, amber (#b8860b) for caution, clinical red (#b91c1c) for stop or emergency, soft purple (#6c3d8e) for attending-owned decisions. Filipino children, families and clinicians where people appear. Generous whitespace, mobile-readable labels.
CONTENT: {content}{locks}
Alt-text intent (for checking): {alt}
Attribution: "renalcarematters.com" in small semi-transparent navy text (70% opacity) at the {pos}, exactly lowercase, clear of all content.

NEGATIVE INSTRUCTIONS:
{NEG_FIG}

QUALITY CHECK (Constitution v1.0 Layer G style):
{qa}
```
"""


def tile_block(name, fname, size, scene):
    return f"""### {name}

```
FILE NAME: {fname}
IMAGE TYPE: Track or module tile (illustrated scene, no text) — williamriveromd-infographic-skill
ASPECT RATIO: 16:9 landscape
PIXEL DIMENSIONS: {size}
PROMPT:
Semi-photorealistic illustrated editorial scene in the renalcarematters.com house style (GPT-rendered, not flat vector). Bright, airy, light background, soft natural daylight, gentle depth of field, colors harmonizing with teal #1a6b72, navy #0f1e2e and warm coral accents suited to pediatrics. Subject centered with a 15% safe margin on all sides so it crops cleanly to a card thumbnail. {scene} Filipino children, families and clinicians; Philippine setting. No text, letters, numbers, logos or watermark (the site sets titles in HTML).
NEGATIVE: dark backgrounds, clutter, collage, readable text, adult-size equipment on a small child (unless the scene is about it), a child shown in pain, cartoon style, HDR, distorted hands or faces.
QUALITY CHECK: reads as one idea at 320 px wide; no text; light background; subject inside the safe margin.
```
"""


OG_CARD = """### {title}

```
FILE NAME: {fname}
IMAGE TYPE: OG / social share card with text — williamriveromd-infographic-skill
ASPECT RATIO: 1.91:1
PIXEL DIMENSIONS: 1200 × 630
PROMPT:
Clean social share card, white (#ffffff) background, Inter font only. Left half: small navy-blue (#1F3864) eyebrow "{eyebrow}", large bold navy (#0f1e2e) title "{head}", a teal (#1a6b72) subtitle "{subtitle}", and a row of three small rounded chips {chips}. Right half: {art} on a light teal (#eef6f7) rounded panel. Bottom-right: "renalcarematters.com" small, navy, 70% opacity.
NEGATIVE: dark backgrounds, misspelled words, any text beyond the words given, logos, clutter, serif fonts, readable patient data.
QUALITY CHECK: exactly 1200 × 630; every word spelled exactly as given; attribution present; readable at 600 px wide.
```
"""


def main(out):
    fig_keys = [k for k in F.FIGS]
    plans_by_key = {}
    for mk, p in PLANS.items():
        for fg in p.get("figures", []):
            plans_by_key[fg["key"]] = (mk, fg)
    types, purposes = {}, {}
    for k in fig_keys:
        mk, p = plans_by_key.get(k, (k[3:5], {}))
        t = p.get("type", "One-panel poster").split("|")[0].strip(); types[t] = types.get(t, 0) + 1
        pu = p.get("purpose", "Understand"); purposes[pu] = purposes.get(pu, 0) + 1
    L = [f"""# Attending Pediatric Nephrologist · Image Plan Blueprint and GPT Prompt Pack

Renal Care Academy → Renal Care Physicians → Attending Pediatric Nephrologist (`academy/{HUB}.html`). Prepared November 27, 2026 from Blueprint v2 (`APN_BLUEPRINT_v2.md`). Generated by `tools/techcourses/apn/build_image_prompts.py`; edit the plan there (and in `parts/imgplan_NN.json`), not here.

## 1. Aim

Every image must help a pediatric attending do one of three things better:

- **Understand** a mechanism he or she can redraw from memory: why creatinine rises with height, why hypotonic fluid swells the brain, why the podocyte leaks, why a valve bladder destroys kidneys after the valves are gone, why a small child's circuit volume matters, how a peritoneal membrane in an infant differs from an adult's.
- **Apply** a decision at the bedside or by phone: an algorithm, a monthly PD review, a peritonitis first hour, a circuit-volume check, a catheter-fever pathway, a transition checklist.
- **Appreciate** why the work matters: heroes and tiles that show children with kidney disease as children first, cared for by skilled teams and involved families in real Philippine settings.

## 2. Guardrails carried into every prompt

- **Light backgrounds, Inter, American English, short labels, mobile-readable; attribution `renalcarematters.com`** on every figure and card (heroes and tiles carry no text by design).
- **No doses, fill volumes, blood-flow settings or order values** in any image unless the module states them word for word; thresholds appear exactly as the cited guideline gives them.
- **Children with dignity:** no graphic distress, no close-up needles in a child's skin, no unnecessary exposure; families present; equipment sized to the child.
- **Dialysis truth:** every extracorporeal circuit follows the dialysis-circuit-schematic lock; every tunneled catheter follows the tunneled-dialysis-catheter-path lock; PD catheters exit downward, away from the beltline and diaper area.
- **People:** a new Filipino cast for every hero (at least 12 visible traits differ); archetypes and cameras rotate across the 30 heroes (ten archetypes, ten cameras, ten family groupings). No real names, brands, logos or readable patient data.
- **The house dislikes flat vector images:** every figure is semi-photorealistic illustration.

## 3. Inventory

| Set | Count | Size | Where it lands |
|---|---|---|---|
| Circular-vignette heroes | 30 (hub + 29 modules; exam and trainer reuse the hub hero) | 2048 × 2048 | `images/{HUB}[-NN-slug]-vignette-hero.webp` |
| Teaching figures | {len(fig_keys)} | 1792 × 1024, 1024 × 1536, 1536 × 1152 | `images/{HUB}-NN-*.webp` (placed automatically once the file exists) |
| Tiles | 31 (landing tile, course-home card, 29 module cards) | 1536 × 864 (export 960 × 540 / 640 × 360) | `images/academy/landing/{HUB}.webp`, `images/{HUB}-card.webp`, `images/{HUB}-NN-card.webp` |
| OG share cards | 4 (track card art, final exam, trainer, nephrotic calculator) | 1536 × 1024 art / 1200 × 630 cards | `images/academy/og-art/`, `images/og/academy/…`, `images/calc-pediatric-nephrotic-course-og.png` |

Figure types: {", ".join(f"{k} {v}" for k, v in sorted(types.items()))}. Teaching purpose: {", ".join(f"{k} {v}" for k, v in sorted(purposes.items()))}; heroes and tiles carry Appreciate. The seven dialysis modules (16, 20–25) carry three figures each.

## 4. Figure map

| ID | Module | Type | Purpose | What it teaches | File |
|---|---|---|---|---|---|"""]
    for i, k in enumerate(fig_keys):
        mk, p = plans_by_key.get(k, (k[3:5], {}))
        L.append(f"| APN-F{i:02d} | {int(mk)} | {p.get('type', 'One-panel poster').split('|')[0].strip()} | {p.get('purpose', 'Understand')} | {p.get('teaches', F.FIGS[k][2])} | `{F.FIGS[k][0].replace('.webp', '.png')}` |")
    L.append(f"""
## 5. Production workflow

1. Paste one fenced block at a time into the ChatGPT Image Generator. Save each PNG under its FILE NAME. For circuit figures, attach the catheter-hub reference image from the dialysis-circuit-schematic skill alongside the prompt.
2. Drop the files in `~/Downloads/Attending Pedia Nephro/images/` (regenerated replacements in `images/Corrected/`). Claude audits each image against its QUALITY CHECK, converts to WebP, places heroes, figures and tiles in the repo `images/` folder, and writes a new MD prompt file for any image that fails audit.
3. Figures appear on the pages automatically at the next `python3 generate_tech_courses.py --course apn --patch` and `python3 tools/academy/publish_academy.py`.
4. OG: put the track art (`{HUB}.png`) in `images/academy/og-art/`, then `python3 build_academy_og.py --art images/academy/og-art --only {HUB} --patch` (the script sets the words). The exam, trainer and calculator cards are complete 1200 × 630 images with text.
5. After tiles land: `python3 generate_rg_thumbs.py` and `python3 patch_rg_card_thumbs.py`.

---

## Part 1 · Heroes (30)
""")
    L.append(hero_block("hub", 0))
    for i, k in enumerate(sorted(MODS), 1):
        L.append(hero_block(k, i))
    L.append("\n---\n\n## Part 2 · Teaching figures\n")
    for i, k in enumerate(fig_keys):
        mk, p = plans_by_key.get(k, (k[3:5], {}))
        L.append(fig_block(k, i, p, mk))
    L.append("\n---\n\n## Part 3 · Tiles (no text; the site sets titles in HTML)\n")
    L.append(tile_block("Academy landing tile", f"academy-landing-{HUB}.png → images/academy/landing/{HUB}.webp (960 × 540)", "1536 × 864",
                        "A pediatric nephrologist crouches at eye level with a seven-year-old girl in a bright pediatric ward playroom, her mother beside them; behind, softly blurred, a nurse sets up a home peritoneal dialysis cycler on a low table and a small window shows a hospital courtyard."))
    L.append(tile_block("Course-home card", f"{HUB}-card.png → images/{HUB}-card.webp", "1536 × 864",
                        "Close, warm scene: a physician's hand and a small child's hand together on a stethoscope chest piece, a parent's hand resting on the child's shoulder, a growth chart softly blurred on the wall behind."))
    for k in sorted(MODS):
        m = MODS[k]
        card = PLANS.get(k, {}).get("card") or m["hero_brief"].split("no text in image. ")[-1]
        L.append(tile_block(f"Module {int(k)} card · {m['title']}", f"{HUB}-{k}-card.png → images/{HUB}-{k}-card.webp (640 × 360)", "1536 × 864",
                            card + " Wider framing than the module hero, a different camera angle and a different cast."))
    L.append("\n---\n\n## Part 4 · OG share cards\n")
    L.append(f"""### Track share card art (text added by build_academy_og.py)

```
FILE NAME: {HUB}.png  (save to images/academy/og-art/)
IMAGE TYPE: OG card art, text-free (build_academy_og.py crops to 1200 × 630 and sets the title, track label and stats)
ASPECT RATIO: 3:2
PIXEL DIMENSIONS: 1536 × 1024
PROMPT:
Semi-photorealistic editorial illustration, bright and airy, light background. Keep the LEFT 42% of the canvas a quiet, soft off-white to light-teal gradient field with no objects (the script places text there). In the RIGHT 58%: a Filipina pediatric nephrologist in her forties, sleeves rolled, kneeling to listen to the chest of a six-year-old boy who sits on his father's lap in a bright pediatric clinic; on a side table a small home peritoneal dialysis cycler and a child-size blood pressure cuff; a colorful growth chart on the wall, softly blurred. Soft daylight, navy #1F3864 and teal #1a6b72 accents with a warm coral highlight. No text, letters, numbers, logos or watermark anywhere.
NEGATIVE: dark backgrounds, clutter, any text, objects in the left 42%, adult-size equipment on the child, a child in distress.
QUALITY CHECK: left 42% empty and light; subject fully inside the right side; no text.
```
""")
    L.append(OG_CARD.format(title="Final exam share card", fname=f"{HUB}-final-exam-og.png → images/og/academy/{HUB}-final-exam.jpg",
                            eyebrow="RENAL CARE PHYSICIANS", head="Attending Pediatric Nephrologist", subtitle="End-of-course examination · 40 questions · timed",
                            chips='"29 modules" · "7 on dialysis" · "Certificate"',
                            art="a semi-photorealistic illustration of a tablet showing a multiple-choice card with four blank answer bars (no readable text) beside a stopwatch and a child-size stethoscope"))
    L.append(OG_CARD.format(title="Trainer page share card", fname=f"{HUB}-trainer-og.png → images/og/academy/{HUB}-trainer.jpg",
                            eyebrow="RENAL CARE PHYSICIANS", head="Trainer and Preceptor Resource", subtitle="Attending Pediatric Nephrologist · stations · capstone",
                            chips='"Work samples" · "Scenario stations" · "Capstone"',
                            art="a semi-photorealistic illustration of a clipboard with a blank scoring grid (no readable text), a pen, a small toy kidney model and a pediatric blood pressure cuff"))
    L.append(OG_CARD.format(title="Nephrotic syndrome calculator share card", fname="calc-pediatric-nephrotic-course-og.png → images/calc-pediatric-nephrotic-course-og.png",
                            eyebrow="PEDIATRIC NEPHROLOGY · CALCULATOR", head="Nephrotic Syndrome Course Classifier", subtitle="KDIGO 2025 definitions · no doses",
                            chips='"Steroid-sensitive" · "Frequent relapses" · "Steroid-resistant"',
                            art="a semi-photorealistic illustration of a family's urine dipstick diary (a calendar grid of blank colored squares, no readable text) beside a dipstick and a color chart bottle without labels"))
    Path(out).write_text(_h.unescape("\n".join(L)), encoding="utf-8")
    print("wrote", out, len(fig_keys), "figures")


if __name__ == "__main__":
    main(sys.argv[1] if len(sys.argv) > 1 else "APN-IMAGE-PLAN-AND-PROMPTS.md")
