# -*- coding: utf-8 -*-
"""Build the Dialysis Team Resuscitation Lab / Emergency Readiness image plan blueprint and GPT prompt pack (one Markdown file).
Sources: course.py (pages, hero briefs), figs.py (file, alt, caption), PLAN below (figure type, teaching purpose, locks).
Skills applied: williamriveromd-hero-vignette v3 (heroes), williamriveromd-simple-figure and williamriveromd-algorithm-generator-skill
(house-style Mode C only: never the AHA chart look), williamriveromd-infographic-skill (tiles, OG share cards),
dialysis-circuit-schematic and tunneled-dialysis-catheter-path locks where a circuit or catheter is drawn.
Run:  python3 tools/techcourses/resus/build_image_prompts.py <output.md>"""
import html as _h
import importlib.util
import re
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent


def _load(name, f):
    s = importlib.util.spec_from_file_location(name, HERE / f); m = importlib.util.module_from_spec(s); s.loader.exec_module(m); return m


C = _load("rl_course", "course.py"); F = _load("rl_figs", "figs.py")
HUB = C.HUB
MODS = {m["id"]: m for m in C.MODULES}

# figure key -> (type, teaching purpose, extra lock keys)
ALG, CMP, SEQ, ONE, MECH, REF, SCN = ("Original decision layout", "Comparison", "Step sequence", "One-panel poster",
                                      "Mechanism poster", "Reference card", "Scene illustration")
PLAN = {
    "rl00_lab_map": (SEQ, "Appreciate", ""), "rl01_chain": (SEQ, "Understand", ""), "rl01_cart_check": (SCN, "Apply", "equip"),
    "rl01_unit_types": (CMP, "Appreciate", ""), "rl01_roster": (SCN, "Apply", ""),
    "rl02_frame": (SEQ, "Understand", ""), "rl02_five_questions": (ALG, "Apply", "orig"), "rl02_parallel": (ONE, "Understand", ""),
    "rl02_transitions": (ALG, "Understand", "orig"),
    "rl03_three_states": (CMP, "Apply", "dignity"), "rl03_rhythm_vs_pulse": (CMP, "Understand", "ecg"), "rl03_stability": (ONE, "Apply", ""),
    "rl03_k_ecg": (SEQ, "Understand", "ecg"),
    "rl04_flatten": (SEQ, "Apply", "cpr manikin"), "rl04_compression": (ONE, "Apply", "cpr manikin"), "rl04_bvm": (ONE, "Apply", "cpr manikin"),
    "rl04_choking": (SEQ, "Apply", ""),
    "rl05_two_paths": (ALG, "Apply", "orig"), "rl05_cycle": (ONE, "Apply", ""), "rl05_reversible": (REF, "Apply", ""),
    "rl05_etco2": (ONE, "Understand", "ecg"),
    "rl06_brady": (ALG, "Apply", "orig"), "rl06_brash": (MECH, "Understand", ""), "rl06_tachy": (ALG, "Apply", "orig"),
    "rl06_sync": (CMP, "Understand", "ecg"),
    "rl07_positions": (ONE, "Apply", "circuit"), "rl07_blood_decision": (ALG, "Apply", "orig"), "rl07_defib_safety": (SCN, "Apply", "circuit manikin"),
    "rl07_access": (SCN, "Apply", "cath"), "rl07_air": (SCN, "Apply", "circuit"),
    "rl08_membrane": (MECH, "Understand", ""), "rl08_blindspot": (CMP, "Understand", "ecg"), "rl08_protect_shift_remove": (REF, "Apply", ""),
    "rl08_aha_erc": (CMP, "Understand", "guide"),
    "rl09_dislodgement": (SCN, "Appreciate", "dignity"), "rl09_hemolysis": (SCN, "Understand", "circuit"), "rl09_anaphylaxis": (CMP, "Apply", "drug"),
    "rl09_other": (CMP, "Apply", ""),
    "rl10_age_bands": (REF, "Understand", ""), "rl10_infant_technique": (CMP, "Apply", "cpr manikin"), "rl10_resp_failure": (SEQ, "Understand", "child"),
    "rl10_ratios": (REF, "Apply", ""),
    "rl11_weight_dose": (SCN, "Apply", "child drug"), "rl11_concentrations": (CMP, "Apply", "drug"), "rl11_ecv": (ONE, "Understand", "circuit child"),
    "rl11_energies": (REF, "Apply", ""),
    "rl12_rosc_check": (SCN, "Apply", "ecg"), "rl12_first10": (REF, "Apply", ""), "rl12_handover": (SCN, "Apply", ""),
    "rl12_unit_limits": (CMP, "Apply", ""),
    "rl13_roles": (REF, "Apply", ""), "rl13_closed_loop": (SEQ, "Apply", ""), "rl13_debrief": (ONE, "Apply", "manikin"),
    "rl13_reports": (CMP, "Understand", ""),
}
SCAFFOLD = {ALG: "williamriveromd-algorithm-generator-skill, Style Mode C (renalcarematters.com house style), portrait, original layout",
            CMP: "williamriveromd-simple-figure scaffold B: two or three side-by-side panels with matched rows",
            SEQ: "williamriveromd-simple-figure scaffold C: numbered steps left-to-right (or a short vertical ribbon) with one picture each",
            ONE: "williamriveromd-simple-figure scaffold D: one strong central visual with up to five short callouts",
            MECH: "williamriveromd-simple-figure scaffold D (one-pathway mechanism), semi-photorealistic 3D components",
            REF: "williamriveromd-simple-figure scaffold E: compact reference card with short rows",
            SCN: "williamriveromd-infographic-skill archetype A/9: semi-photorealistic clinical scene with up to four short callouts"}
SIZE = {ALG: ("1024 × 1536", "2:3 portrait"), REF: ("1536 × 1152", "4:3")}

LOCKS = {
    "orig": ("ORIGINAL LAYOUT LOCK: this is an original renalcarematters.com teaching layout. Do NOT imitate any published resuscitation "
             "algorithm chart: no AHA or ERC box arrangement, colors, numbering, logos or wording. House colors only: navy #0f1e2e text, "
             "teal #1a6b72 decision diamonds, green #1f7a4d actions, amber #b8860b cautions, red #b91c1c stop or emergency boxes. At most "
             "8 to 10 nodes, labels of five words or fewer."),
    "ecg": ("RHYTHM-STRIP TRUTH: draw every ECG on a pale pink or white grid with a thin dark trace. Sinus or organized rhythm = regular "
            "P-QRS-T complexes; ventricular fibrillation = chaotic irregular waves with no QRS complexes; peaked T waves are tall and narrow; "
            "a wide QRS is visibly broad; sine wave is smooth and rounded. Capnography = square plateaus. No numbers on the strip except "
            "those named in CONTENT."),
    "cpr": ("CPR TECHNIQUE TRUTH: adult compressions with the heel of one hand on the lower half of the breastbone, the other hand on top, "
            "arms straight, shoulders directly above the hands; patient flat on a firm surface; bag-mask with a two-handed seal; infant "
            "two-thumb encircling technique or heel of one hand on the lower half of the breastbone."),
    "manikin": ("DIGNITY: the person receiving CPR or a shock is a realistic adult training manikin (or child manikin where stated) in a "
                "dialysis recliner, never a real patient's distressed face or bare chest."),
    "dignity": ("DIGNITY: patients appear calm or with faces turned or softly out of focus; no graphic distress; a gown covers the chest; "
                "blood shown only as a small clean stain where the scene requires it."),
    "circuit": ("CIRCUIT LOCK (dialysis-circuit-schematic): blood leaves the patient on the RED arterial line, passes the blood pump, enters "
                "the dialyzer at an end port, leaves by the other end port, passes the venous drip chamber and air detector, and returns on the "
                "BLUE venous line. Dialysate tubing joins the dialyzer's SIDE ports only. Draw exactly one arterial and one venous line. "
                "No numeric pressures or settings."),
    "cath": ("CATHETER LOCK (tunneled-dialysis-catheter-path, external view only): exit site and small clean dressing on the patient's RIGHT "
             "upper chest below the collarbone; two short limbs ending in a RED (arterial) cap and a BLUE (venous) cap; clamps on each limb; "
             "nothing in the neck; no internal path drawn through the skin; never on the left or crossing the midline."),
    "drug": ("DRUG LABEL LOCK: labels read only the concentrations and routes given in CONTENT, in American English (\"epinephrine\", never "
             "a brand). No other numbers, no lot or expiry text, no logos."),
    "child": "CHILD: a school-age Filipino child, calm and cared for, family member nearby, equipment sized to the child.",
    "equip": ("EQUIPMENT: generic defibrillator (no brand), pads in a sealed pouch, bag-valve-mask, oxygen cylinder with a gauge, suction "
              "unit, oral and nasal airways, a sealed drug tray. No readable brand, dose or expiry text."),
    "guide": ("SOURCE WORDING: column headers \"AHA 2025\" and \"ERC 2025\" only; no society logos; each cell paraphrases the CONTENT in five "
              "words or fewer. Do not add drugs or doses that are not in CONTENT."),
}

NEG_FIG = ("Avoid flat vector clip art, cartoon style, clutter, tiny unreadable labels, AI gibberish text, unrealistic anatomy, overprocessed "
           "HDR, excessive saturation. NEVER dark, navy, charcoal or black backgrounds: light backgrounds only. Use ONLY Inter (sans-serif). "
           "No logos, brand names, society seals, real names or readable patient data. No doses, energies, rates or thresholds unless they "
           "appear word for word in CONTENT. Never omit the renalcarematters.com attribution, exactly lowercase (no www, no https://).")
NEG_HERO = ("Avoid: duplicated people, repeated compositions, cropped circle, objects touching the circular border, important content inside "
            "the title safe zone, baked-in text, titles, captions, logos, watermarks, readable monitor numbers, rectangular borders, frames, "
            "dark / charcoal / black backgrounds, cartoon style, neon, HDR, over-saturation, distorted hands or faces, implausible anatomy, "
            "panic, blood spray, a real patient's distressed face or bare chest during CPR (use a manikin), bent-elbow compressions, a "
            "blood pressure cuff on a fistula arm.")

PEOPLE_ROT = [("J Environmental Storytelling", "wide-angle eye-level"), ("H Clinical", "over-the-shoulder"), ("A Editorial Portrait", "three-quarter close"),
              ("B Journey", "low side angle"), ("D Panorama", "wide low angle"), ("C Radial", "top-down"), ("H Clinical", "eye-level close"),
              ("A Editorial Portrait", "side profile"), ("J Environmental Storytelling", "rear three-quarter"), ("E Lifestyle", "overhead three-quarter")]
CAST = ["a woman charge nurse in her fifties with short gray-streaked hair and a man technician in his twenties with a buzz cut",
        "a young woman physician with a long braid, a heavyset male nurse in his forties, and a slim woman nursing assistant",
        "a male nurse in his thirties with glasses and a goatee",
        "two women nurses, one tall and broad-shouldered with a bob cut, one petite and older with a low bun",
        "a male physician in his sixties with silver hair and a woman physician-on-duty in her thirties with a ponytail",
        "a young male physician-on-duty with curly hair and a woman nurse in her forties wearing a head scarf",
        "a stocky woman circuit nurse with cropped hair and three colleagues in different scrub colors",
        "a lean male physician in his forties with a shaved head and a woman nurse with shoulder-length wavy hair",
        "an older woman nurse with reading glasses on a cord and a young male nurse with a fade haircut",
        "a woman pediatric dialysis nurse in her late twenties with a high ponytail, a male colleague with a beard, and a quiet mother",
        "two pediatric nurses, one a young man with round glasses and one a woman in her fifties with short permed hair",
        "a woman nurse in her thirties with a side part and two ambulance crew members, a man and a woman",
        "a mixed team of six: technician, two nurses, nursing assistant, physician and a facilitator in her sixties"]
HUB_SCENE = ("A Filipino dialysis team in a drill around a realistic adult training manikin in a fully flattened dialysis recliner: one nurse "
             "compressing with straight arms, one sealing a bag-valve-mask with two hands, a circuit nurse at the hemodialysis machine, a "
             "physician watching a generic defibrillator, other chairs empty and softly blurred in morning light.")
HERO_FIX = {  # replace real-patient arrest scenes with manikin drills (dignity) and keep the brief's teaching point
    "04": "A nurse giving chest compressions with straight arms to a realistic adult training manikin in a fully flattened dialysis recliner while a second nurse seals a bag-valve-mask with both hands.",
    "05": "During a drill, a physician presses the shock button of a generic defibrillator while the team steps back from a manikin in a flattened dialysis recliner, every pair of hands visibly raised and clear of the chair and blood lines.",
    "07": "During a drill, a circuit nurse clamps blood lines at a hemodialysis machine while colleagues compress a training manikin in the flattened chair beside it; the machine, chair and team positions are the subject.",
    "09": "A nurse pressing folded gauze on a forearm fistula site after a needle dislodgement, a small clean stain on the blanket, a second nurse checking the pulse at the wrist; the patient calm, face turned away.",
}


def hero_block(key, i):
    if key == "hub":
        fname, title, scene, brief = f"{HUB}-vignette-hero.png", "Course home (the final exam, trainer and pre-test pages reuse it)", HUB_SCENE, C.COURSE["hero_alt"]
    else:
        m = MODS[key]
        fname, title, brief = f"{HUB}-{key}-{m['slug']}-vignette-hero.png", f"Module {int(key)} · {m['title']}", m["sub"]
        scene = HERO_FIX.get(key, m["hero_brief"].split("in image. ")[-1])
    arch, cam = PEOPLE_ROT[i % len(PEOPLE_ROT)]
    cast = CAST[i % len(CAST)]
    return f"""### {title}

Teaching purpose: Appreciate. {re.sub(r"<[^>]+>", "", brief)}

```
FILE NAME: {fname}   (convert to WebP; also export a 1200 × 1200 JPEG to images/og/ only if no text OG card is made)
IMAGE TYPE: Circular vignette hero v3 (williamriveromd-hero-vignette, Scaffold A people)
ASPECT RATIO: 1:1 (displayed inside an 85–90% inscribed circle with white margin)
PIXEL DIMENSIONS: 2048 × 2048
COMPOSITION ARCHETYPE: {arch}
CAMERA: {cam}
HUMAN VARIATION: new cast for this hero: {cast}; at least 12 traits differ from the previous hero (age, sex, face shape, jawline, hairstyle, hair length and color, build, height impression, skin tone within Filipino diversity, scrub color, accessories, posture, expression)
AUDIENCE: dialysis nurses, technicians, physicians-on-duty and unit leaders

PROMPT:
Square 1:1 semi-photorealistic editorial illustration on a 2048×2048 canvas (GPT-rendered, painterly-realistic, not flat vector), composed for a CIRCULAR vignette occupying 85–90% of the canvas diameter with a visible WHITE BORDER around the full circle (the circle never touches the canvas edges). Composition archetype: {arch}. Camera: {cam}.
People: Filipino, {cast}; calm, focused, competent expressions; correct scrubs, gloves and badges with no readable text.
Scene: {scene} A clean, bright modern Philippine hemodialysis unit with recliner dialysis chairs, hemodialysis machines with blank screens, a crash cart and a generic defibrillator; soft natural daylight, gentle shallow depth of field. The mood is urgent but controlled: a trained team doing the right thing.
Visual hierarchy: hero subject 60–70% of the circle; 2–4 supporting elements 20–30%; reserve a 20–25% TITLE SAFE ZONE of soft gradient, clean wall or blurred background on one side (no faces, equipment or hands in it).
Calm documentary-realistic color grade harmonizing with teal #1a6b72 and navy #0f1e2e on a light background. No rectangular borders, frames or banners.
Absolutely NO text of any kind: no title, caption, label, readable monitor numbers, writing on paper or screens, logo or watermark.

NEGATIVE INSTRUCTIONS:
{NEG_HERO}

QUALITY CHECK:
Square 2048×2048; circle 85–90% with a white margin, never cropped; one dominant subject; 20–25% empty title-safe zone; Filipino team; compressions with straight arms on the lower half of the breastbone where shown; manikin, not a real patient, during CPR or a shock; no text anywhere.
```
"""


def fig_block(key, idx):
    fname, alt, cap = F.FIGS[key]
    png = fname.replace(".webp", ".png")
    typ, purpose, locks = PLAN[key]
    mod = int(key[2:4])
    size, ratio = SIZE.get(typ, ("1792 × 1024", "16:9 landscape"))
    pos = "bottom-center" if "portrait" in ratio else "bottom-right"
    lock_txt = "".join("\n" + LOCKS[k] for k in locks.split() if k in LOCKS)
    qa = ["□ Light (white or #fafafa) background; semi-photorealistic, not flat vector", "□ Every label spelled exactly as written, American English, Inter font",
          "□ One concept; labels five words or fewer", "□ Numbers appear exactly as in CONTENT and nowhere else",
          "□ No logo, brand, real name or readable patient data", f"□ Attribution renalcarematters.com at the {pos}, small, navy, 70% opacity, exact lowercase"]
    if "orig" in locks:
        qa.append("□ Original layout: does not resemble an AHA or ERC algorithm chart")
    if "ecg" in locks:
        qa.append("□ Rhythm strips drawn correctly for the rhythm named")
    if "cpr" in locks:
        qa.append("□ Hands on the lower half of the breastbone, arms straight; infant technique as stated")
    if "circuit" in locks:
        qa.append("□ Circuit: red arterial line with the pump, blood at the dialyzer end ports, dialysate at the side ports, air detector before the blue return")
    if "cath" in locks:
        qa.append("□ Catheter exits the right upper chest, red and blue capped limbs, clamps, nothing in the neck")
    if "manikin" in locks or "dignity" in locks:
        qa.append("□ Dignity: manikin during CPR or shock; no distressed faces or bare chests")
    qa = "\n".join(qa)
    return f"""### RL-F{idx:02d} · {key}

Placement: {"Course home" if mod == 0 else f"Module {mod}"} · Teaching purpose: **{purpose}** · Teaches: {cap}

```
FILE NAME: {png}   (convert to {fname} for the site)
IMAGE TYPE: {typ} — {SCAFFOLD[typ]}
ASPECT RATIO: {ratio}
PIXEL DIMENSIONS: {size}
AUDIENCE: dialysis nurses, technicians and physicians-on-duty (plain enough for nursing assistants)
VISUAL GOAL: {cap}

PROMPT:
Clean clinical education figure in the renalcarematters.com house style, AJKD/NEJM graphical-abstract aesthetic, semi-photorealistic illustration with soft shading (not flat vector clip art, not cartoon). White (#ffffff) background with soft gray (#f3f4f6) or light teal (#eef6f7) cards. Title-free (the page caption carries the message); short labels only, in Inter, navy #0f1e2e, with teal #1a6b72 headings, green #1f7a4d for correct or safe actions, amber #b8860b for cautions and red #b91c1c for danger or stop. Generous whitespace, mobile-readable at 375 px wide.
CONTENT: {alt}{lock_txt}
Attribution: "renalcarematters.com" in small semi-transparent navy text (70% opacity) at the {pos}, exactly lowercase, clear of all content.

NEGATIVE INSTRUCTIONS:
{NEG_FIG}

QUALITY CHECK:
{qa}
```
"""


def tile_block(name, fname, size, scene):
    return f"""### {name}

```
FILE NAME: {fname}
IMAGE TYPE: Tile (illustrated scene, no text) — williamriveromd-infographic-skill
ASPECT RATIO: 16:9 landscape
PIXEL DIMENSIONS: {size}
PROMPT:
Semi-photorealistic illustrated editorial scene in the renalcarematters.com house style (GPT-rendered, painterly-realistic, not flat vector). Bright, airy, light background, soft natural daylight, gentle depth of field, colors harmonizing with teal #1a6b72 and navy #0f1e2e. One clear subject centered with a safe margin on all sides (tiles are cropped to 16:9 and to a 4:3 thumbnail). Filipino people where shown, a new cast for every tile. Scene: {scene} Absolutely no text, readable screens, logos or watermarks.
NEGATIVE: dark backgrounds, clutter, collage, readable text, a real patient's distressed face or bare chest during CPR (use a manikin), bent-elbow compressions, cartoon style, HDR, distorted hands or faces.
QUALITY CHECK: reads as one idea at 320 px wide; no text; light background; subject inside the safe margin.
```
"""


OG_CARD = """### {title}

```
FILE NAME: {png} → save as images/og/{slug}-og.jpg (JPEG, 1200 × 630, ≤ 300 KB; the generator picks it up automatically)
IMAGE TYPE: OG / social share card with text — williamriveromd-infographic-skill
ASPECT RATIO: 1.91:1
PIXEL DIMENSIONS: 1200 × 630
PROMPT:
Clean social share card, white (#ffffff) background, Inter font only, generous margins. LEFT 55%: a small teal (#1a6b72) uppercase eyebrow "{eyebrow}", a large bold navy (#0f1e2e) title on at most two lines "{head}", a navy subtitle in regular weight "{subtitle}", and a row of three small rounded chips with teal outlines reading {chips}. RIGHT 45%: {art}, semi-photorealistic, softly lit, on a light teal (#eef6f7) rounded panel that bleeds off the right edge. Small "renalcarematters.com" in semi-transparent navy (70% opacity) at the bottom-left under the chips, exactly lowercase.
NEGATIVE: dark backgrounds, misspelled words, any text beyond the words given, the words "AHA", "certified" or "certification", logos, seals, clutter, serif fonts, readable patient data, a real patient during CPR.
QUALITY CHECK: exactly 1200 × 630; every word spelled exactly as given; attribution present; readable at 600 px wide; important content inside the central 1100 × 560 (Messenger and X crop the edges).
```
"""

OG_MODS = {  # module -> (art for the right panel, three chips)
    "01": ("a top-down crash cart with a generic defibrillator, pads pouch, bag-valve-mask and oxygen cylinder", '"Morning cart check" · "Chain of survival" · "Shift roles"'),
    "02": ("a whiteboard with a branching path of blank rounded boxes and arrows beside a dialysis chair", '"Five questions" · "Parallel tasks" · "Transitions"'),
    "03": ("two dialysis chairs under one identical monitor rhythm strip, a nurse's fingers on a pulse", '"Pulse or no pulse" · "Stable or not" · "Potassium ECG"'),
    "04": ("hands with straight arms compressing a manikin in a flattened dialysis recliner", '"Flatten the recliner" · "100–120 a minute" · "Choking 2025"'),
    "05": ("a generic defibrillator beside a flattened dialysis chair with a manikin, hands raised clear", '"Shock first for VF" · "Epinephrine timing" · "Reversible causes"'),
    "06": ("a bedside monitor with a fast narrow rhythm and cardioversion pads on a conscious patient's chest under a gown", '"Stability first" · "Pacing" · "Synchronized shock"'),
    "07": ("a gloved hand clamping red and blue blood lines at a hemodialysis machine beside a flattened chair", '"Circuit nurse" · "Return or clamp" · "Defib near the machine"'),
    "08": ("an ECG strip with tall peaked T waves beside a laboratory tube and a calcium ampule (no readable labels)", '"Protect, shift, remove" · "AHA vs ERC" · "Dialysis after ROSC"'),
    "09": ("a dialysis venous line with dark translucent blood and folded gauze over a forearm fistula", '"Needle out" · "Hemolysis" · "Anaphylaxis"'),
    "10": ("two thumbs encircling a child manikin's chest beside a pediatric bag-valve-mask", '"Infant technique 2025" · "Breathing first" · "15:2"'),
    "11": ("a weight-based dose card, a syringe and three epinephrine ampules of different sizes (no readable labels)", '"Doses said aloud" · "Concentration traps" · "Circuit volume"'),
    "12": ("a clipboard handover sheet passed to an ambulance crew member beside a stretcher, a monitor showing a regular rhythm", '"Confirm ROSC" · "First ten minutes" · "Handover"'),
    "13": ("a small team in a standing circle around a manikin in a recliner, a facilitator with a clipboard", '"Closed-loop orders" · "Code status" · "Five-question debrief"'),
}


def main(out):
    keys = list(F.FIGS)
    missing = [k for k in keys if k not in PLAN]
    if missing:
        sys.exit(f"no PLAN entry for {missing}")
    types, purposes = {}, {}
    for k in keys:
        t, p, _ = PLAN[k]; types[t] = types.get(t, 0) + 1; purposes[p] = purposes.get(p, 0) + 1
    n_tiles = 4 + len(MODS)
    n_og = 1 + len(MODS) + 6
    L = [f"""# Dialysis Team Resuscitation Lab and Emergency Readiness · Image Plan Blueprint and GPT Prompt Pack

Renal Care Academy → Emergency Readiness → Dialysis Team Resuscitation Lab (`academy/{HUB}.html`), with the section hub (`academy/emergency-readiness.html`), the Practice Lab (`academy/{HUB}-practice.html`) and the toolkit (`guides/calc-resuscitation-lab-toolkit.html`). Prepared November 28, 2026 from `RESUSCITATION_LAB_BLUEPRINT_v2.md`. Generated by `tools/techcourses/resus/build_image_prompts.py` from the course's own figure list, so file names match the pages exactly.

**Status: the course is a DRAFT pending Dr. Rivero's clinical sign-off.** Images can be produced now; none of them carries the word "draft", so nothing needs remaking after sign-off.

## 1. Aim

Every image should help a dialysis team member do one of three things better:

- **Understand** what a decision rests on: why the same rhythm strip can be a living circulation or pulseless electrical activity, why potassium moves the membrane toward threshold, why a child's circuit holds so much of the blood.
- **Apply** it at the chair: flatten the recliner, compress well, return or clamp the blood, aspirate the catheter lock, say the pediatric dose aloud, hand over what the ambulance needs.
- **Appreciate** what a trained team looks like in the first minutes, so the drills feel worth doing.

## 2. Guardrails carried into every prompt

- **Original layouts only.** No American Heart Association or European Resuscitation Council algorithm chart is reproduced or imitated: no box arrangement, color code, numbering, logo or wording. Decision figures use the renalcarematters.com house style (algorithm-generator Style Mode C), not Mode A.
- **Numbers only where the module states them.** Doses, energies, rates and targets appear only when the figure's CONTENT gives them; each was checked against the 2025 AHA and ERC guidelines while writing the modules.
- **Dignity.** Anyone receiving CPR or a shock is a training manikin. No distressed faces, bare chests, blood spray or panic. Compressions always with straight arms on the lower half of the breastbone.
- **Dialysis truth.** Every drawn circuit follows the dialysis-circuit-schematic lock; every tunneled catheter follows the tunneled-dialysis-catheter-path lock (right upper chest, red and blue capped limbs).
- **House style.** Light backgrounds, Inter, American English, short labels, mobile-readable; attribution `renalcarematters.com` on every figure and share card (heroes and tiles carry no text by design). Semi-photorealistic illustration, never flat vector clip art.
- **People.** A new Filipino cast for every hero and tile (at least 12 visible traits differ); archetypes and camera angles rotate. No real names, brands or readable screens.
- **Share cards** never say "certified", "certification" or "AHA": the course is a BLS-, ALS- and PALS-aligned review, not a certification course.

## 3. Inventory

| Set | Count | Size | Where it lands |
|---|---|---|---|
| Circular-vignette heroes | {1 + len(MODS)} (course home + 13 modules; exam, trainer and pre-test reuse the home hero) | 2048 × 2048 | `images/{HUB}[-NN-slug]-vignette-hero.webp` |
| Teaching figures | {len(keys)} | 1792 × 1024, 1024 × 1536, 1536 × 1152 | `images/{HUB}-NN-*.webp` (placed automatically once the file exists) |
| Tiles | {n_tiles} (Academy landing tile, course-home card, 13 module cards, Emergency Readiness tile, Practice Lab tile) | 1536 × 864 (export 960 × 540 / 640 × 360) | `images/academy/landing/{HUB}.webp`, `images/{HUB}-card.webp`, `images/{HUB}-NN-card.webp`, `images/emergency-readiness-card.webp`, `images/{HUB}-practice-card.webp` |
| OG share cards with text | {n_og} (course home art + 13 modules + Practice Lab, Emergency Readiness, final exam, trainer, pre-test, toolkit) | 1536 × 1024 art / 1200 × 630 cards | `images/academy/og-art/{HUB}.png`; `images/og/<page>-og.jpg` |

Figure types: {", ".join(f"{k} {v}" for k, v in sorted(types.items()))}. Teaching purpose: {", ".join(f"{k} {v}" for k, v in sorted(purposes.items()))}; heroes and tiles carry Appreciate.

## 4. Figure map

| ID | Module | Type | Purpose | What it teaches | File |
|---|---|---|---|---|---|"""]
    for i, k in enumerate(keys):
        t, p, _ = PLAN[k]
        mod = int(k[2:4])
        L.append(f"| RL-F{i:02d} | {'Home' if mod == 0 else mod} | {t} | {p} | {F.FIGS[k][2]} | `{F.FIGS[k][0].replace('.webp', '.png')}` |")
    L.append(f"""
## 5. Production workflow

1. Paste one fenced block at a time into ChatGPT image generation. Save each PNG under its FILE NAME. Produce the figures for Modules 4, 5 and 7 first: they carry the most practical weight.
2. Drop the files in `~/Downloads/Emergency Readiness/images/` (regenerated replacements in `images/Corrected/`). Claude audits each image against its QUALITY CHECK, converts to WebP and places heroes, figures and tiles.
3. Figures and heroes appear on the pages at the next `python3 generate_tech_courses.py --course resus --patch` and `python3 tools/academy/publish_academy.py`.
4. OG: put the course-home art (`{HUB}.png`) in `images/academy/og-art/`, then `python3 build_academy_og.py --art images/academy/og-art --only {HUB} --patch` (the script sets the words). Save the other share cards as `images/og/<page>-og.jpg`; the generator and `tools/academy/apply_resus_lab.py` pick them up.
5. After tiles land: `python3 generate_rg_thumbs.py` and `python3 patch_rg_card_thumbs.py`.

---

## Part 1 · Heroes ({1 + len(MODS)})
""")
    L.append(hero_block("hub", 0))
    for i, k in enumerate(sorted(MODS), 1):
        L.append(hero_block(k, i))
    L.append(f"\n---\n\n## Part 2 · Teaching figures ({len(keys)})\n")
    for i, k in enumerate(keys):
        L.append(fig_block(k, i))
    L.append(f"\n---\n\n## Part 3 · Tiles ({n_tiles}; no text, the site sets titles in HTML)\n")
    L.append(tile_block("Academy landing tile", f"academy-landing-{HUB}.png → images/academy/landing/{HUB}.webp (960 × 540)", "1536 × 864",
                        "Wide view of a bright dialysis unit at the start of a shift: a nurse wheels a crash cart with a generic defibrillator past a row of recliner chairs while a technician and a physician talk at a whiteboard with blank role boxes; morning light; nobody in distress."))
    L.append(tile_block("Course-home card", f"{HUB}-card.png → images/{HUB}-card.webp", "1536 × 864",
                        "Close, warm drill scene: four pairs of gloved hands around a manikin in a flattened dialysis recliner (one pair compressing with straight arms, one holding a bag-valve-mask seal, one on the blood lines, one holding a clipboard)."))
    L.append(tile_block("Emergency Readiness section tile", "emergency-readiness-card.png → images/emergency-readiness-card.webp", "1536 × 864",
                        "Three objects in a row on a light teal counter, evenly spaced: a phone showing a red-bordered card with blank lines, a tablet showing an open lesson page with a blank figure, and a small adult CPR manikin torso. One idea: act, learn, practice."))
    L.append(tile_block("Practice Lab tile", f"{HUB}-practice-card.png → images/{HUB}-practice-card.webp", "1536 × 864",
                        "A tablet on a stand beside a manikin in a dialysis recliner shows a monitor display with a green rhythm trace (no numbers); a facilitator's hand taps a second tablet with a grid of blank buttons; a stopwatch on the armrest."))
    for k in sorted(MODS):
        m = MODS[k]
        card = HERO_FIX.get(k, m["hero_brief"].split("in image. ")[-1])
        L.append(tile_block(f"Module {int(k)} card · {m['title']}", f"{HUB}-{k}-card.png → images/{HUB}-{k}-card.webp (640 × 360)", "1536 × 864",
                            card + " Wider framing than the module hero, a different camera angle and a different cast."))
    L.append(f"\n---\n\n## Part 4 · OG share cards ({n_og})\n")
    L.append(f"""### Course-home share card art (text added by build_academy_og.py)

```
FILE NAME: {HUB}.png  (save to images/academy/og-art/)
IMAGE TYPE: OG card art, text-free (build_academy_og.py crops to 1200 × 630 and sets the title, track label and stats)
ASPECT RATIO: 3:2
PIXEL DIMENSIONS: 1536 × 1024
PROMPT:
Semi-photorealistic editorial illustration, bright and airy, light background. Keep the LEFT 42% of the canvas a quiet, soft off-white to light-teal gradient field with no objects (the script places text there). In the RIGHT 58%: a Filipino dialysis team in a drill around a training manikin in a flattened recliner, one nurse compressing with straight arms, one with a bag-valve-mask, a circuit nurse at the hemodialysis machine, a generic defibrillator on a cart; morning daylight; calm and focused.
NEGATIVE: dark backgrounds, clutter, any text, objects in the left 42%, a real patient during CPR, bent-elbow compressions.
QUALITY CHECK: left 42% empty and light; subject fully inside the right side; no text.
```
""")
    for k in sorted(MODS):
        m = MODS[k]
        art, chips = OG_MODS[k]
        slug = f"{HUB}-{k}-{m['slug']}"
        L.append(OG_CARD.format(title=f"Module {int(k)} · {m['title']}", png=f"{slug}-og.png", slug=slug,
                                eyebrow=f"RESUSCITATION LAB · MODULE {int(k)}", head=_h.unescape(m["title"]), subtitle="Dialysis Team Resuscitation Lab · Renal Care Academy",
                                chips=chips, art=art))
    extra = [
        ("Practice Lab", f"{HUB}-practice", "EMERGENCY READINESS", "Practice Lab", "Algorithm recognition · timed megacodes · unit drills",
         '"46 recognition items" · "17 megacodes" · "Shared display"', "a tablet showing a bedside monitor with a green rhythm trace (no numbers) beside a manikin in a dialysis recliner and a stopwatch"),
        ("Emergency Readiness section", "emergency-readiness", "RENAL CARE ACADEMY", "Emergency Readiness", "Act, learn and practice the first minutes on the dialysis floor",
         '"Quick cards" · "13 modules" · "Practice Lab"', "a phone with a red-bordered card (blank lines), a tablet with a lesson page, and a small CPR manikin torso on a light counter"),
        ("Final exam", f"{HUB}-final-exam", "RESUSCITATION LAB", "End-of-Course Examination", "Dialysis Team Resuscitation Lab · timed",
         '"13 modules" · "Timed" · "Certificate of completion"', "a tablet with a multiple-choice card of four blank answer bars beside a stopwatch and a folded pocket mask"),
        ("Trainer and facilitator kit", f"{HUB}-trainer", "RESUSCITATION LAB", "Facilitator Kit", "Scripts · role cards · observation checklist · debrief",
         '"Role cards" · "Megacode scripts" · "Five-question debrief"', "a clipboard with a blank checklist, a fan of colored role cards and a stopwatch beside a manikin's shoulder"),
        ("Placement pre-test", f"{HUB}-pretest", "RESUSCITATION LAB", "Placement Pre-test", "Find the modules you need",
         '"Five questions a module" · "80% mastery" · "On this device"', "a tablet showing a short quiz card with blank answer bars beside a pen and a dialysis unit badge without text"),
        ("Toolkit (calculator)", "calc-resuscitation-lab-toolkit", "RESUSCITATION LAB · TOOLKIT", "Resuscitation Lab Toolkit", "Compression fraction · megacode timeline · pediatric dose trainer",
         '"Compression fraction" · "Oxygen duration" · "Role rotation"', "a stopwatch, an oxygen cylinder gauge and a syringe beside a tablet with a blank timeline chart"),
    ]
    for title, slug, eyebrow, head, sub, chips, art in extra:
        L.append(OG_CARD.format(title=title, png=f"{slug}-og.png", slug=slug, eyebrow=eyebrow, head=head, subtitle=sub, chips=chips, art=art))
    Path(out).write_text(_h.unescape("\n".join(L)), encoding="utf-8")
    print("wrote", out, len(keys), "figures")


if __name__ == "__main__":
    main(sys.argv[1] if len(sys.argv) > 1 else "RESUSCITATION_LAB_IMAGE_PROMPTS.md")
