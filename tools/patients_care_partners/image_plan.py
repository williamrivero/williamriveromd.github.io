# -*- coding: utf-8 -*-
"""Renal Patients and Care Partners: image plan blueprint and GPT prompt pack (Stage 1 of the two-stage image pipeline).

    python3 tools/patients_care_partners/image_plan.py     # writes docs/tech-courses/patients-care-partners-image-prompts.md
                                                           # and the working-folder copy (RENAL-PATIENTS-CARE-PARTNERS-IMAGE-PROMPTS.md)

Same house style and file conventions as the other Academy tracks (see tools/techcourses/pdn/image_plan.py):
williamriveromd-hero-vignette v3 (one photorealistic circular hero per page), williamriveromd-infographic-skill v5 (teaching
figures, tiles, OG cards), williamriveromd-simple-figure (single-idea figures), williamriveromd-algorithm-generator-skill
(action paths), Constitution v1.0 anatomy locks (williamriveromd-infographic-generator) for every figure that shows anatomy, and
the tunneled-dialysis-catheter-path lock. Every hero shows its module's own "real situation"; every figure label comes from the
module's own lesson text (quoted in GROUNDED IN). Supersedes IMAGE_PLAN_AND_GPT_PROMPTS.md (November 28, 2026, morning)."""
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
HUB = "patients-care-partners"
CUR = json.loads((HERE / "content" / "curriculum.json").read_text(encoding="utf-8"))
MODS = {}
for i, m in enumerate(CUR["modules"], 1):
    m = dict(m); m["nn"] = f"{i:02d}"; m["page"] = f"{HUB}-{m['nn']}-{m['slug']}"; MODS[m["id"]] = m
ORDER = [m["id"] for m in CUR["modules"]]
WORKDIRS = [Path.home() / "mnt" / "Renal Patients & Care Partners", Path("/Users/williamgregoryriveromd/Downloads/Renal Patients & Care Partners")]

FONT = "Inter"
STYLE = (f"Clean renalcarematters.com house style: white (#ffffff) background, panels in soft gray (#f3f4f6) or light teal tint (#eef6f7); "
         f"navy #0f1e2e for titles and text, clinical teal #1a6b72 for headings and rules, renal green #1f7a4d for safe or done, amber "
         f"#b8860b for caution or check, clinical red #b91c1c for stop or emergency, soft purple #6c3d8e for referral or team steps. "
         f"Typeface: {FONT} only, bold title, short labels (no paragraphs), minimum 11 pt equivalent. Semi-photoreal people and objects "
         f"where shown: Filipino adults, older adults, care partners and nurses, fully clothed, calm and dignified. Generous whitespace. "
         f"Bottom-right corner: \"© renalcarematters.com\" in small semi-transparent navy text (about 70% opacity).")
FIG_NEG = ("Avoid cartoon style, painterly or watercolor illustration, warm sepia grading, clutter, tiny unreadable labels, AI gibberish or "
           "misspelled text, overprocessed HDR, excessive saturation, generic stock-photo look. NEVER use dark, navy, charcoal, or black "
           "backgrounds; light backgrounds only. Use ONLY the sans-serif fonts Inter, Nunito Sans, IBM Plex Sans, Manrope, or DM Sans. No "
           "legible real names, phone numbers, PhilHealth numbers or documents with readable personal data. Do not add numbers, doses, "
           "fluid amounts, potassium values, blood pressure targets or machine settings that are not written in this prompt. No drug "
           "brand names. No blood, wounds or needles in close-up. American English on every label. Never omit the renalcarematters.com "
           "attribution.")
FIG_QC = ("Mobile-readable at 360 px wide; every label spelled exactly as written in the prompt; one teaching idea only; calm, "
          "publication-grade, white or soft light-gray background; crisp semi-photoreal rendering matching the other Renal Care Academy "
          "figures (not painterly); no legible personal data; © renalcarematters.com visible bottom-right.")
HERO_NEG = ("busy layouts, collage overload, more than four supporting scenes, dozens of icons, infographic clutter, duplicated people, "
            "repeated compositions, cropped circle, objects touching the circular border, important content inside the title safe zone, "
            "baked-in text, titles, captions, logos, watermarks, legible documents, ID cards or screens, rectangular borders, frames, banners, "
            "dark backgrounds, painterly or watercolor illustration, cartoon style, neon, HDR, warm sepia grading, over-saturation, distorted "
            "hands or faces, extra fingers, visible blood, needles in skin, wounds, distressed or crying faces")
PH, ST = "photorealistic editorial photograph", "photorealistic still-life"

# ── Constitution v1.0 anatomy locks (williamriveromd-infographic-generator), pasted into every figure that shows anatomy ──
LOCK_KIDNEY = ("CONSTITUTION v1.0 ANATOMY LOCK (overrides style): any whole kidney is bean-shaped with the convex border LATERAL and the "
               "hilum MEDIAL; the renal pelvis exits at the medial hilum only; calyces drain INWARD toward the pelvis; renal vein anterior, "
               "artery middle, ureter posterior (VAU). A nephron is drawn as a standalone enlarged diagram, never inside a full-size kidney; the "
               "whole kidney appears only as a small orientation inset (12% of the panel or less) labeled \"NOT TO SCALE\". Glomerulus: a "
               "capillary tuft inside Bowman&rsquo;s capsule, afferent arteriole in, efferent arteriole out, filtrate into the proximal tubule. "
               "Arteries have a thick muscular wall and round lumen; veins are thin-walled. Anatomy is never drawn through clothing or skin "
               "except inside a labeled inset.")
LOCK_AVF = ("CONSTITUTION v1.0 ANATOMY LOCK — FISTULA (overrides style): left forearm radiocephalic fistula, the cephalic vein joined end-to-side "
            "to the radial artery near the wrist; the arterialized vein is visibly enlarged and runs up the forearm under the skin. When "
            "needles are shown, the arterial needle (red) sits nearer the joining point and the venous needle (blue) is further up the arm and "
            "points AWAY from the joining point, toward the heart. A graft, if shown, is a separate soft tube looping under the forearm skin.")
LOCK_PD = ("CONSTITUTION v1.0 ANATOMY LOCK — PD CATHETER (overrides style): soft silicone Tenckhoff catheter entering the LOWER abdominal wall off "
           "the midline; exit site points DOWNWARD; deep cuff preperitoneal, superficial cuff about 2 cm inside the exit site; the tip lies "
           "low in the pelvis, never in the bladder or bowel. The peritoneum is a thin glossy membrane lining the abdominal wall and covering "
           "the bowel, rich in tiny capillaries. Internal anatomy only inside a labeled cutaway inset marked \"NOT TO SCALE\".")
LOCK_TX = ("CONSTITUTION v1.0 ANATOMY LOCK — TRANSPLANT (overrides style): anterior view, patient&rsquo;s RIGHT on the IMAGE LEFT. Native kidneys "
           "stay in their usual place (right slightly lower than left). The donor kidney sits in the RIGHT iliac fossa (image left, lower "
           "abdomen): its renal artery joins the external iliac artery (red, thick-walled), its renal vein joins the external iliac vein (blue, "
           "thin-walled), and its ureter enters the bladder dome. Never in the native kidney position, never joined to bowel, never mirrored.")
LOCK_CATH = ("ANATOMY LOCK — CATHETER PATH (tunneled-dialysis-catheter-path skill; follow exactly; overrides style): Anterior view, so the "
             "patient&rsquo;s RIGHT side is on the IMAGE LEFT. The whole catheter is on the patient&rsquo;s right (image left) and never crosses "
             "the midline. 1. EXIT SITE: right upper anterior chest wall, below the clavicle, a few finger-breadths lateral to the sternum, above "
             "the nipple line; below it a hub splits into two short external limbs hanging downward, RED clamp and cap (arterial) and BLUE "
             "clamp and cap (venous). 2. CUFF: a small textured cream-white Dacron cuff INSIDE the subcutaneous tunnel just above the exit site, "
             "under the skin. 3. TUNNEL: upward beneath the skin, passing OVER (in front of) the medial clavicle, never beneath it. 4. VENOTOMY "
             "AND LOOP: just above the clavicle ONE smooth gentle U-shaped turn into the LOW right internal jugular vein, lateral to the common "
             "carotid artery. 5. COURSE: straight down the right internal jugular vein, right brachiocephalic vein, superior vena cava. 6. TIP: "
             "upper-to-mid right atrium. Internal path only inside an inset labeled \"NOT TO SCALE\". Never: catheter under the clavicle or in the "
             "subclavian vein, crossing the midline, exit site in the neck or on the abdomen, external cuff, sharp kink or double loop, tip in "
             "the right ventricle or high superior vena cava, red/blue clamps swapped.")
HERO_CATH = ("CATHETER LOCK FOR THIS HERO (tunneled-dialysis-catheter-path skill, vignette rules): the patient faces the camera, so her RIGHT "
             "side is on the IMAGE LEFT. Only the outside is visible: a clean white dressing on her right upper chest wall below the collarbone, "
             "a few finger-breadths from the breastbone and above the nipple line, with a hub and two short limbs hanging DOWNWARD below it, RED "
             "clamp and cap (arterial) and BLUE clamp and cap (venous). No tube in the neck, no catheter crossing the midline, no exit site on the "
             "neck or abdomen, no internal path, no inset, no labels; the body is never mirrored.")
QA = {
    "kidney": ["Nephron standalone; whole kidney only in a small NOT TO SCALE inset", "Afferent arteriole in, efferent out; filtrate into tubule",
               "Kidney convex border lateral, hilum medial, calyces drain inward"],
    "avf": ["Fistula on the left forearm near the wrist; vein enlarged up the forearm", "If needles shown: red nearer the joining point, blue further up pointing toward the heart"],
    "pd": ["PD exit site on the lower abdomen pointing downward", "Catheter tip low in the pelvis, not in bladder or bowel", "Anatomy only in a NOT TO SCALE inset"],
    "tx": ["Donor kidney in the right iliac fossa (image left)", "Artery to external iliac artery, vein to external iliac vein, ureter to bladder", "Native kidneys still present"],
    "cath": ["Path: chest-wall exit → cuff inside tunnel → over the clavicle → one loop into the low right internal jugular vein → superior vena cava → right atrium",
             "Entirely on the image left; never crosses the midline", "Red = arterial, blue = venous limbs below the hub"],
}
LOCKS = {"kidney": LOCK_KIDNEY, "avf": LOCK_AVF, "pd": LOCK_PD, "tx": LOCK_TX, "cath": LOCK_CATH}

# ───────────────────────── heroes: one per page, each showing the module's own "real situation" ─────────────────────────
# code: (style, archetype, camera, safe side, subject, goal)
H = {
 "hub": (PH, "J Environmental Storytelling", "eye level, medium-wide", "upper-right",
  "in a bright, modern Philippine dialysis unit lounge, a Filipino man in his early 60s with a round face, close-cropped gray hair and a "
  "striped polo sits with his adult daughter, who holds a small notebook, while a nurse educator in teal scrubs with a short bob shows them a "
  "printed booklet (pages blurred); other patients and chairs softly blurred behind",
  "Kidney care is learned together: the patient, the person they choose, and the team."),
 "C01": (PH, "H Clinical", "over-the-shoulder, slightly high", "upper-left",
  "Mang Ramon, a Filipino tricycle driver in his late 50s with a weathered tan face, short salt-and-pepper hair and a faded cap in his hand, "
  "sits beside his daughter Liza, late 20s, long straight hair, office lanyard, who holds a phone showing a course page (screen blurred); a "
  "barangay health worker in a white blouse hands them a blank care-team card at a simple community health station",
  "Find your stop: one goal, one supporter, one care team."),
 "C02": (PH, "A Editorial Portrait", "close portrait, three-quarter", "right",
  "Aling Cora, a Filipina in her early 50s with diabetes, shoulder-length wavy hair with a clip and reading glasses, sits at a clinic desk "
  "looking closely at a printed laboratory report (text blurred) while a woman doctor in a white coat points to a second line further down "
  "the page; soft window light",
  "Read both numbers: how much the kidneys clean, and whether they leak."),
 "C03": (PH, "J Environmental Storytelling", "wide, eye level", "upper-left",
  "a small barangay hall in late afternoon: Mang Tonio, mid-40s, security-guard uniform shirt, short hair, sits with his wife, a nurse in "
  "civilian clothes; across the room an 84-year-old grandfather, Lolo Pedring, in a cane chair with his grandchild leaning on his arm; a "
  "kidney doctor in a polo stands between them, talking warmly",
  "The same facts can lead to different, well-informed choices."),
 "C04": (PH, "I Object Hero", "45-degree tabletop", "upper-right",
  "a pharmacist&rsquo;s hands at a neighborhood pharmacy counter holding a blister pack and turning a small box so its side label (blurred) "
  "faces a Filipino man in his 60s, Tito Boy, whose hand rests on his lower back; a handwritten medicine list on the counter (unreadable)",
  "Ask before you take it: weak kidneys clear some medicines more slowly."),
 "C05": (PH, "F Human Connection", "three-quarter, eye level", "upper-left",
  "Aling Nena, 67, petite, short gray hair with a side part, cotton duster dress, at her kitchen table with a renal dietitian in a white "
  "polo who shows her a bowl of tinola with green papaya and malunggay and a small plate of fruit; a can of meat loaf and a plate of plain "
  "rice and egg pushed to the side; daylight from a jalousie window",
  "Do not cut out whole food groups on a rumor; build the plan with your dietitian."),
 "C06": (PH, "A Editorial Portrait", "side profile, medium", "upper-right",
  "Kuya Jun, early 40s, slim build, short spiky hair, birthday-party shirt, sits on the edge of a bed in the morning, gently pressing his "
  "swollen ankle with a thumb; a bathroom scale on the floor and a small glass of water on the side table",
  "With little urine, every glass stays until the next treatment."),
 "C07": (PH, "H Clinical", "close, slightly angled", "upper-left",
  "Ate Grace, 36, hair tied up, loose button-front blouse open at the collar, sitting on a dialysis unit bed on a rainy day while a "
  "dialysis nurse in navy scrubs and a mask examines the clean white dressing on her right upper chest below the collarbone (only the dressing "
  "and the red and blue capped limbs visible, no tube in the neck); a folded umbrella dripping by the chair, rain on the window",
  "Report redness the same day; do not wait for the next session."),
 "C08": (PH, "J Environmental Storytelling", "medium, low light", "upper-right",
  "a small home at night: Paolo, 19, lanky, messy hair, T-shirt, speaking urgently but calmly on his phone while his grandmother Lola Fe, "
  "70s, sits upright on the edge of her bed propped by pillows; a contact card and medicine list held by a magnet on the refrigerator in the "
  "background (unreadable)",
  "In an emergency, call: location, what happened, kidney treatment, bleeding."),
 "C09": (PH, "E Lifestyle", "environmental portrait, eye level", "upper-left",
  "Manong Ben, 66, a retired teacher with thick glasses, a cardigan and neatly combed white hair, walking slowly across a town plaza "
  "toward the parish church with his wife holding his arm and a choir folder under his other arm; morning light, church facade softly blurred",
  "Tiredness and low mood are information; several causes can be treated."),
 "C10": (PH, "H Clinical", "over-the-shoulder at a desk", "upper-right",
  "Mang Celso, 55, heavyset, basketball jersey, a bucket hat in his lap, at the reception desk of a dialysis unit while a benefits "
  "officer with short hair and a lanyard explains a form (unreadable) before he signs, the pen resting on the desk; a small transistor radio "
  "peeks out of his shoulder bag",
  "Ask what you are signing; a benefit is paid to the facility, not to you."),
 "C11": (PH, "D Panorama", "wide, eye level", "upper-left",
  "Aling Rosa, 59, slim, gray-streaked bun, rain jacket, leaving her house in Legazpi under heavy gray skies for the extra Tuesday session "
  "her unit added before the typhoon, holding a sealed waterproof folder and a power bank; a relative waits by a tricycle; wet road",
  "Plan while services are open: go early, keep a portable folder."),
 "C12": (PH, "H Clinical", "three-quarter, eye level", "upper-right",
  "Ate Mylene, late 40s, market vendor with a ponytail and an apron folded on her lap, explaining something back to a nurse in teal scrubs "
  "who listens and holds a pen over a printed medicine schedule (unreadable); a consultation room with a closed door",
  "Explain it back: teach-back catches mistakes before they happen."),
 "K01": (PH, "A Editorial Portrait", "medium, slightly low", "upper-left",
  "Sir Arnel, a public school teacher around 50 with a mustache and a barong-style polo, sits at his kitchen table pale and tired with a "
  "glass of oral rehydration fluid, reading a small written sick-day card from his clinic (text blurred); a stack of exam papers beside him",
  "A written sick-day plan turns an emergency into a phone call."),
 "K02": (PH, "B Journey", "wide, eye level", "upper-right",
  "Nanay Lourdes, early 60s, short permed hair, floral blouse, walking out of a modern dialysis unit entrance in daylight with her husband "
  "carrying her bag; she glances at the healed fistula on her left forearm",
  "Planning ahead gives you a ready access and a treatment you chose."),
 "K03": (PH, "H Clinical", "over-the-shoulder at a desk", "upper-left",
  "Ma&rsquo;am Lyn, an accountant in her late 50s with a short layered haircut, pearl earrings and a blazer, on a video call with her "
  "nephrologist on a laptop (screen softly blurred) while holding her printed laboratory results; a cup of coffee and a pill organizer nearby",
  "A small early dip can mean the medicine is working; ask before stopping."),
 "H01": (PH, "H Clinical", "eye level, medium", "upper-right",
  "Tatay Lito, about 70, thin, white mustache, in a dialysis chair with a light blanket, raising his hand to signal while a dialysis nurse "
  "with braided hair in teal scrubs turns toward him; the machine and lines softly blurred; his left forearm rests on a pillow",
  "Report cramps and dizziness early; it is part of the treatment."),
 "H02": (PH, "I Object Hero", "close, hands only", "upper-left",
  "hands only: Kuya Dodong&rsquo;s right fingertips resting lightly on the inside of his left forearm near the wrist, checking his fistula "
  "on a Sunday morning, his other hand reaching for a phone (screen blurred) on a wooden table beside a cup of coffee",
  "Feel the buzz morning and evening; if it weakens or stops, contact your unit promptly."),
 "H03": (PH, "H Clinical", "three-quarter", "upper-right",
  "Ate Joy, mid-40s, single mother with a short pixie cut and a school-pickup tote bag, talking with a head nurse at a small review table in "
  "a dialysis unit; a printed monthly results sheet between them (unreadable)",
  "Your review is numbers plus your experience; solve the barrier together."),
 "H04": (ST, "C Radial", "45-degree tabletop", "upper-left",
  "a Noche Buena table seen from the side: a sliced ham, a bowl of fruit salad, a young coconut with a straw and a soft drink, with a small "
  "medicine cup of phosphate binder tablets placed beside the plate and a wall calendar softly blurred behind",
  "Plan the food and fluid before the longest gap between sessions."),
 "P01": (PH, "F Human Connection", "medium, eye level", "upper-right",
  "Bong, late 30s, jeepney dispatcher with a buzz cut and a reflective vest folded on his chair, practicing a PD exchange on a training "
  "model at a clean table, masked, while a PD nurse in white scrubs watches with a checklist; his wife sits beside him taking notes",
  "Only supervised training makes you ready for home PD."),
 "P02": (PH, "J Environmental Storytelling", "medium, warm lamp light at night", "upper-left",
  "Aling Merly, early 60s, short curly gray hair, house dress, sits at her home exchange table at night holding up a drained PD bag to the "
  "lamp light while her daughter, mid-30s, dials a phone beside her; the bag looks faintly cloudy",
  "A cloudy bag is an urgent call, even at night."),
 "P03": (PH, "H Clinical", "medium, slightly high", "upper-right",
  "Tatay Nestor, early 70s, bald with a gray goatee, and his grandson Kevin, 22, with a fade haircut and glasses, both masked at a clean "
  "home table while a PD nurse watches Kevin practice a connection on a training set; boxes stored on a shelf off the floor",
  "A new helper or a long gap means a new skills check."),
 "T01": (PH, "H Clinical", "three-quarter", "upper-left",
  "Paolo, late 20s, Ana&rsquo;s brother, newly married, with a neat side part and a wedding ring, in a private consultation room with a transplant donor "
  "coordinator, a woman in her 40s with glasses; the door is closed, both seated, a water glass on the table",
  "A living donor has their own team and can say no at any time."),
 "T02": (ST, "I Object Hero", "close, 45-degree", "upper-right",
  "a weekly pill organizer with morning and evening compartments next to a phone alarm screen (blurred) and a travel pouch with a spare "
  "three-day supply, on a pine table in a Baguio guesthouse with a misty window",
  "Every anti-rejection dose matters; plan refills before you run out."),
 "T03": (PH, "H Clinical", "over-the-shoulder", "upper-left",
  "Mrs. Dela Cruz, mid-40s, with long hair in a low ponytail, and her adult son in a university shirt, sitting with a hospital benefits "
  "coordinator who holds a dated written estimate (unreadable) and a wall calendar softly blurred behind",
  "Coverage depends on which policy applies, and from what date."),
 "S01": (PH, "J Environmental Storytelling", "wide, eye level", "upper-right",
  "Lola Iska, 86, small and frail, white hair in a bun, wrapped in a shawl in a cane chair on a shaded porch, holding her daughter&rsquo;s "
  "hand while a home-visit nurse kneels beside her with a small medical bag; potted plants and afternoon light",
  "Conservative care is active care, focused on comfort and what matters."),
 "S02": (PH, "J Environmental Storytelling", "wide, eye level", "upper-left",
  "Manang Elsa, late 70s, silver hair cut short, glasses on a chain, speaking at a kitchen table to her three adult children while a "
  "nephrologist and a nurse listen; a rosary and a cup of tea on the table",
  "Talking about future care is a gift to the people who may decide for you."),
 "A01": (PH, "A Editorial Portrait", "side profile, eye level", "upper-right",
  "Mang Andoy, about 70, tall and lean with a cap, speaking to a doctor across a clinic desk while his daughter Marites, mid-40s, in a work "
  "blouse, sits slightly behind him taking notes and smiling",
  "Support without taking over: the patient speaks first."),
 "A02": (ST, "I Object Hero", "straight-on, eye level", "upper-left",
  "a refrigerator door with a hand-drawn weekly roster on paper (columns and small avatar stickers, no readable names), a clean magnet "
  "holding a folded contact card, and a phone on the counter showing a small private chat (blurred)",
  "A shared plan, a backup for every task, and private channels for medical details."),
 "A03": (PH, "A Editorial Portrait", "environmental portrait", "upper-right",
  "Ate Rowena, mid-40s, tired but smiling, hair loosely tied, sitting on a bench outside a parish hall with a cup of coffee, a support-group "
  "member in her 60s sitting beside her with a hand on her shoulder",
  "An empty cup cannot pour; ask for specific help."),
 "F01": (PH, "A Editorial Portrait", "three-quarter, eye level", "upper-left",
  "JM, 17, a Filipino teenager with a curtain haircut and a hoodie, filling his own weekly pill organizer at a clinic table while his mother "
  "watches from a chair behind him and a pediatric nurse in printed scrubs gives a thumbs-up",
  "Hand over responsibility step by step, with a safety net."),
 "F02": (ST, "C Radial", "top-down flat lay", "upper-right",
  "a hospital discharge folder, two printed medicine lists side by side with two lines circled (unreadable), a medicine box with blister "
  "packs and a highlighter on a dialysis unit counter",
  "After a hospital stay, reconcile one clear plan."),
}

# ───────────────────────── teaching figures (40) ─────────────────────────
# (code, key, section, skill, image type, title, body, lock or None)
FG = [
 ("C01", "care-team-map", "lesson-2", "infographic-skill", "Role map infographic", "Who helps with what",
  "A center circle with a seated Filipino patient and the care partner they chose beside them. Around it six rounded cards, each with a "
  "small semi-photoreal portrait and one line: \"Kidney doctor (nephrologist): the medical plan\", \"Nurse: teaches and watches for problems\", "
  "\"Pharmacist: untangles medicine lists\", \"Dietitian: meals you actually eat\", \"Social worker or benefits officer: costs, PhilHealth, "
  "transport\", \"Care partner: the person you choose\". Right side: a blank card titled \"My care team card\" with four empty lines labeled "
  "\"Medicines\", \"Food\", \"Treatment\", \"Money\" and a fifth \"After hours\". Footer chip: \"You decide what your care partner helps with.\"", None),
 ("C02", "two-tests", "lesson-2", "simple-figure", "Two-panel comparison", "Two tests, two stories",
  "Left panel titled \"eGFR: how much your filters clean\": an enlarged single nephron (glomerulus and tubule) with blood entering and filtrate "
  "leaving, and a gauge. Right panel titled \"Urine albumin (uACR): is the filter leaking?\": a magnified filter wall with small gold albumin "
  "dots crossing into urine, and a strainer icon labeled \"holes stretching\". Bottom band: \"Normal eGFR can still leak albumin. Both together "
  "show risk.\" Small kidney orientation inset labeled \"NOT TO SCALE\".", "kidney"),
 ("C02", "trend", "lesson-3", "simple-figure", "Annotated line chart", "One result is a snapshot; the trend is the story",
  "A simple line chart with five dated dots (no numbers on the axes) and a gentle line through them. Three callouts: \"Same units every time\", "
  "\"One high dot after a big meat meal or dehydration\" pointing to a single outlier, and \"Ask: is the trend stable, improving or getting "
  "worse?\" A small clipboard icon labeled \"Keep a dated list\".", None),
 ("C03", "options", "lesson-1", "infographic-skill", "Option cards", "Options worth discussing",
  "Five equal cards in a row, each with a semi-photoreal scene and a short label: \"Protect the kidneys you have\", \"Hemodialysis in a unit, "
  "about three times a week\", \"Peritoneal dialysis at home\", \"Kidney transplant\", \"Conservative kidney management: comfort and quality of "
  "life\". Above the row two overlapping cards: \"What is medically suitable\" (held by a doctor) and \"What matters to me\" (held by a "
  "patient). A circular arrow under the row: \"A decision can be revisited\". All five cards the same size and brightness.", None),
 ("C04", "two-exits", "picture", "simple-figure", "Analogy diagram", "Why the same dose can build up",
  "A highway with capsule-shaped cars (medicines) and two exits: one to a liver icon, one to a kidney icon. Left half \"Healthy kidneys\": both "
  "exits flowing. Right half \"Weak kidneys\": the kidney exit narrowed to one lane and cars queuing, label \"Medicine builds up\". A thin dashed "
  "divider separates the analogy from a small real kidney icon. Footer: \"A dose that was right for healthy kidneys may need changing.\"", None),
 ("C04", "ask-first", "lesson-2", "infographic-skill", "Three-card action figure", "Ask before adding a product",
  "Three cards left to right with generic, unbranded products: \"Pain relievers called NSAIDs (ibuprofen, mefenamic acid, naproxen) reduce "
  "blood flow into the filters\"; \"Herbal &lsquo;kidney cleansers&rsquo; and detox teas are not tested for kidney disease\"; \"Imported "
  "supplements may hide potassium, metals or drugs\". Below, a pharmacist and patient at a counter with a speech bubble: \"I have kidney disease. "
  "Is this safe for me?\"", None),
 ("C05", "less-salt", "lesson-2", "infographic-skill", "Three-panel food figure", "Use the meals you already eat",
  "Panel 1 \"Same dish, less salt\": sinigang, tinola, rice and fried fish, with patis, toyo, bagoong and a seasoning cube fading out and "
  "calamansi, garlic, onion, ginger and pepper coming in. Panel 2 \"Read the label\": a generic nutrition label with \"Sodium per serving\" "
  "highlighted and the note \"1 pack of instant noodles is often 2 servings\". Panel 3 \"Ask your dietitian\": a dietitian and an older patient "
  "with a notebook \"My plan\". Footer: \"There is no single kidney food list that fits everyone.\"", None),
 ("C05", "too-strict", "lesson-3", "simple-figure", "Before-and-after comparison", "When a food list becomes too strict",
  "Left panel \"Three months on a rumor\": a plate of plain rice, egg and canned meat loaf; an older Filipina looking tired, with three amber "
  "chips \"Weak\", \"Constipated\", \"Blood pressure higher\". Right panel \"A plan made with a dietitian\": the same woman at the same table "
  "with tinola, vegetables, a small portion of fruit and rice, and green chips \"Salt cut first\", \"Other limits only if your results call "
  "for them\", \"Plan changes when treatment changes\". Footer: \"Report poor appetite, weight loss, or a diet so strict you stopped enjoying "
  "meals.\" No potassium or phosphorus numbers.", None),
 ("C06", "closing-drain", "picture", "simple-figure", "Three-step analogy", "The closing drain",
  "Three panels, each a sink above a seated person. \"Kidneys working\": drain open, water flowing out. \"Less urine\": drain half closed, water "
  "rising, light blue shading at the ankles labeled \"swelling\". \"Very little urine, on dialysis\": drain nearly closed, water high, a small "
  "inset of the lungs labeled \"fluid can reach the lungs\". Bottom band: a measuring cup labeled \"Your amount, if any, comes from your team\" "
  "and a red chip \"Can&rsquo;t breathe lying flat? Get help now.\" No numbers.", None),
 ("C07", "doorways", "lesson-2", "infographic-skill", "Four-column comparison with anatomy insets", "Know your doorway",
  "Four columns with a short label each: \"Fistula: your artery joined to a vein\" (left forearm), \"Graft: a soft tube joins artery and vein\" "
  "(forearm with looped tube), \"Hemodialysis catheter: a tube in a large vein\" (clothed upper right chest with dressing and red and blue "
  "clamps; internal path only in a NOT TO SCALE inset), \"PD catheter: a tube into the belly\" (lower abdomen with a dressing, tube pointing "
  "down). Under the first three columns a bar labeled \"Hemodialysis bloodstream infection risk (CDC)\" running from \"Lowest: fistula\" to "
  "\"Highest: catheter\". Footer: \"Never open a cap or remove a dressing yourself. Report redness, pus, fever or chills the same day.\"", "avf+cath+pd"),
 ("C07", "hands", "lesson-1", "simple-figure", "Four-moment icon strip", "Clean hands protect your doorway",
  "Four rounded tiles, each with a soap-and-water or alcohol hand-rub icon and a label: \"Before touching your access\", \"Before handling "
  "your dressing or supplies\", \"After the toilet\", \"After pets or garbage\". Below, two chips: \"Mask when you have a cough\" and \"Tell "
  "staff about fever, cough, diarrhea or a skin wound before your session\".", None),
 ("C08", "help-now", "lesson-1", "algorithm-generator-skill", "Action card", "Get emergency help now",
  "A red header \"Get emergency help now\". Seven rows with simple icons: \"Severe breathlessness or can&rsquo;t lie flat\", \"Chest pain or "
  "pressure\", \"Fainting or collapse\", \"New confusion or trouble speaking\", \"New weakness of face, arm or leg\", \"Heavy or spurting "
  "bleeding from an access\", \"Seizure\". Right side: two boxes \"In the dialysis unit: call staff at once\" and \"At home: local emergency "
  "service or nearest emergency department\". Footer in red: \"No website or chat is watched in real time.\" No phone numbers.", None),
 ("C08", "the-call", "lesson-2", "simple-figure", "Four-box script", "The 30-second call",
  "A phone at the center with four numbered speech boxes around it: \"1 Where you are, with a landmark\", \"2 What is happening and when it "
  "started\", \"3 Kidney treatment: hemodialysis, PD or transplant\", \"4 Is there bleeding?\". Below: a refrigerator magnet holding a contact "
  "card and medicine list, with the note \"Tell staff: no blood pressure or drips on the fistula arm.\" No phone numbers.", None),
 ("C09", "tired", "lesson-1", "infographic-skill", "Cause-and-action figure", "Tired is information",
  "Left: an older Filipino man on a porch with a thought bubble \"I can no longer climb the stairs without stopping.\" Center: four cards of "
  "causes the team can look for: \"Anemia (low red blood cells)\", \"Poor sleep\", \"Depression\", \"Dialysis that needs review\". Right: three "
  "action tiles: \"Describe how it affects your day\", \"Start small with walking, with your team&rsquo;s OK\", \"Ask for a counselor or social "
  "worker\". Footer chip: \"About one in four people with kidney disease has depression; it is treatable.\"", None),
 ("C10", "benefit-flow", "lesson-1", "simple-figure", "Flow diagram", "A benefit, not cash",
  "Left: a plain building icon labeled \"PhilHealth\" (text only, no logo). Arrow \"pays for covered services\" to the center: \"Accredited "
  "facility\". Arrow to the right: a patient receiving treatment and holding \"Itemized bill\" and \"Copies of documents\". A crossed-out dashed "
  "arrow from PhilHealth to a wallet: \"Not cash to you\". Bottom band: \"Up to 156 hemodialysis sessions per calendar year for eligible, "
  "registered members (PhilHealth Circular 2024-0023, checked November 28, 2026)\". No peso amounts.", None),
 ("C11", "spare-tire", "lesson-2", "infographic-skill", "Flat-lay plus timeline", "The spare tire plan",
  "Left: a top-down photo of a sealed waterproof folder holding \"Treatment summary\", \"Medicine and allergy list\", \"Latest results\", "
  "\"PhilHealth details\", \"Unit and backup unit card\", a few days of medicines and a charged power bank. Right: a four-step vertical timeline "
  "with rain icons: \"Storm signal raised\" → \"Unit announces schedule change\" → \"Go early, or to the backup unit\" → \"Can&rsquo;t reach "
  "anyone? Follow your written plan; emergency if severe symptoms\". A PD supply box on a shelf above a floodwater line. No logos.", None),
 ("C12", "teach-back", "lesson-1", "simple-figure", "Loop plus privacy card", "Ask until the plan is clear",
  "Left: a four-step loop with small scenes: \"Nurse explains\" → \"You explain it back\" → \"Nurse corrects one detail\" → \"Written plan\". "
  "Three speech chips: \"Please show me.\", \"Can you write that down?\", \"Let me explain it back.\" Right: a card \"Who may know about my "
  "health\" with three checkboxes (no names) and a padlock: \"Health information is sensitive personal information (Data Privacy Act).\"", None),
 ("K01", "drips", "picture", "simple-figure", "Analogy with real inset", "Many small drips",
  "A row of clay pots (palayok) labeled \"kidney filters\" under a nipa roof with five drips labeled \"High blood pressure\", \"High blood sugar\", "
  "\"Smoking\", \"Some pain relievers\", \"Dehydration\"; a person repairing the roof labeled \"Treatment and daily habits\". A dashed inset shows a "
  "real glomerulus with arrows \"pressure inside the filter\". Footer: \"Lost filters do not grow back; protect the ones you have.\"", "kidney"),
 ("K01", "sick-day", "lesson-3", "algorithm-generator-skill", "Simple decision path", "When you are sick",
  "Start box \"Vomiting, diarrhea, fever or not eating\" → \"Find your written sick-day card from your clinician\" → two branches: \"Medicines "
  "the card says to pause\" and \"Medicines the card says to keep\" → \"Call your clinic\" → \"Restart as the card says when you are eating and "
  "drinking\". Red side box: \"Do not use a generic online list.\" No medicine names.", None),
 ("K02", "two-starts", "picture", "simple-figure", "Two timelines", "Two ways to start dialysis",
  "Top timeline \"Planned start\": \"Clinic visits\" → \"Meets the PD nurse, visits a unit\" → \"Fistula made months before\" (forearm icon) → "
  "\"Planned first session, home the same day\". Bottom timeline \"Crisis start\": \"Skipped visits\" → \"Emergency department, breathless\" → "
  "\"Urgent catheter\" (clothed right upper chest with a dressing and red and blue capped limbs only) → \"Hospital stay\". Footer: \"People who plan ahead are more likely to start with a ready access and a treatment they chose.\"", "cath"),
 ("K03", "three-gears", "picture", "infographic-skill", "Mechanism analogy", "The heart, kidney and sugar connection",
  "Three interlocking gears labeled \"Heart\", \"Kidneys\", \"Sugar and fat handling\", with arrows showing strain passing between them. Four "
  "hands steady the gears, tagged \"ACE inhibitor or ARB\", \"SGLT2 inhibitor\", \"Finerenone\", \"GLP-1 medicine (for some)\". Caption chip: "
  "\"Ask: is one right for me?\" No doses, no brand names.", None),
 ("K03", "early-dip", "lesson-3", "simple-figure", "Annotated line chart with trial bars", "A small early dip, then slower decline",
  "Left: a schematic line chart (no axis numbers) with two lines: \"Without protection\" declining steadily and \"With protection\" dipping "
  "slightly at the start then declining more slowly; a callout on the dip: \"Expected early dip: lower pressure inside the filter. Your team "
  "checks it.\" Right: two small bar pairs from trials: \"DAPA-CKD: 14.5% → 9.2% over about 2.4 years\" and \"EMPA-KIDNEY: 16.9% → 13.1% over 2 "
  "years\", captioned \"Kidney decline, kidney failure or death from kidney or heart causes\".", None),
 ("H01", "dialyzer", "picture", "simple-figure", "Circuit and cutaway", "Inside the dialyzer",
  "Left: a seated, clothed patient with a left forearm fistula and two needles, red line to a blood pump, a vertical dialyzer, blue line back "
  "to the arm. Blood enters the dialyzer at the TOP and leaves at the BOTTOM; dialysate enters at the BOTTOM and leaves at the TOP (opposite "
  "directions). Right: a magnified cutaway of three hollow fibers: blood inside, dialysate outside, small waste dots crossing out, and a water "
  "drop labeled \"extra fluid removed\". Bottom: \"Cramps or dizziness? Tell the nurse early.\" No machine numbers or brand.", "avf"),
 ("H02", "daily-check", "lesson-1", "infographic-skill", "Three-panel access care", "Know and protect your access",
  "Panel 1 \"Feel the thrill\": fingertips on a left forearm fistula with soft vibration lines; ear icon \"listen if taught\". Panel 2 \"Protect "
  "this arm\": four crossed icons \"No blood pressure, blood draws or drips on this arm\", \"No tight sleeves, watches or bracelets\", \"Do not sleep on it\", \"No heavy bags hanging from it\". Panel "
  "3 \"Catheter\": clothed right upper chest with a clean dry dressing and red and blue capped limbs; \"Keep dry and covered\", \"Never open the "
  "caps\"; internal path only in a NOT TO SCALE inset. Red banner: \"Buzz weak, pulse-like or gone? Contact your unit promptly; clots are easier to clear early.\"", "avf+cath"),
 ("H02", "bleeding", "lesson-3", "algorithm-generator-skill", "Action path", "If a needle site bleeds at home",
  "Start \"Needle site bleeding\" → \"Press firmly with clean gauze, as your nurse showed you\" → \"Stopped?\" Yes → \"Keep watching; tell the "
  "unit at your next contact\". No, heavy or spurting → red box \"Keep pressing. Someone calls emergency help now.\" Side note: \"Keep clean "
  "gauze and your contact card where you can find them.\" No times or numbers.", None),
 ("H03", "review", "lesson-1", "infographic-skill", "Dashboard figure", "A review looks beyond one number",
  "Left: a clipboard with six unnumbered dials: \"Waste removal (Kt/V, URR)\", \"Hemoglobin\", \"Potassium\", \"Phosphorus and calcium\", "
  "\"Albumin\", \"Blood pressure and weight\". Right: three dials labeled \"Only you can tell us\": \"Recovery time after a session\", \"Sleep, "
  "appetite and itch\", \"Activities I miss\". Bottom: a session bar divided into four hours with waste removed steadily, the last part shaded "
  "with scissors: \"Leaving early removes less.\"", None),
 ("H04", "long-gap", "picture", "simple-figure", "Weekly sawtooth chart", "Rising behind the dam",
  "A week strip Monday to Sunday with dialysis on Monday, Wednesday and Friday. Above it a sawtooth line rising between sessions and dropping on "
  "dialysis days, highest before Monday, labeled \"Longest gap: plan ahead\". Two icons riding the line: \"Potassium\" and \"Fluid\". Footer: "
  "\"Never skip the session after a long gap.\" No values.", None),
 ("H04", "binders", "lesson-2", "simple-figure", "Mechanism figure", "Why binders go with meals",
  "Left: a plate with rice, fish and a soft drink, with small orange dots labeled \"phosphorus (also in processed foods and some soft "
  "drinks)\". Center: a schematic stomach and small intestine (dashed inset) where binder particles catch phosphorus dots so they leave in the "
  "stool. Right: two small panels \"Too much phosphorus pulls calcium from bones\" (bone icon) and \"and stiffens blood vessels\" (vessel "
  "icon). Footer: \"Take binders with meals, as your team instructs.\" No doses.", None),
 ("P01", "fill-dwell-drain", "picture", "simple-figure", "Three-step cutaway", "How peritoneal dialysis works",
  "Three steps, each a clothed person with a NOT TO SCALE abdominal cutaway inset: \"Fill\" (sterile fluid flows in through the catheter), "
  "\"Dwell\" (magnified circle: capillaries in the peritoneum with waste and water moving into the fluid; note \"sugar in the fluid draws out "
  "water\"), \"Drain\" (used fluid flows into a drain bag). Bottom: two icons \"CAPD: exchanges by day\" and \"APD: a cycler at night\", and a "
  "trainer watching a patient practice: \"Only supervised training makes you ready.\"", "pd"),
 ("P02", "cloudy", "picture", "infographic-skill", "Comparison plus actions", "Clear or cloudy",
  "Left: two drained PD bags held in front of a printed newspaper page (generic text): print readable through the clear bag, unreadable "
  "through the cloudy bag; a magnified circle of white blood cells. Right: three action steps \"Call your PD team now, day or night\", \"Keep "
  "the cloudy bag\", \"If you can&rsquo;t reach them, go to the emergency department with the bag\". A small exit-site close-up with labels "
  "\"redness\", \"swelling\", \"crust or pus\", \"pain\".", "pd"),
 ("P02", "contamination", "lesson-2", "algorithm-generator-skill", "Action path", "If a connection may be contaminated",
  "Start \"A tip touched something, a cap fell off, or a line cracked\" → \"Stop. Follow the step your trainer taught you\" → \"Call the PD team "
  "promptly\" → \"The team decides about preventive treatment\". Red side box: \"Never repair it yourself. Never add medicine to a bag.\"", None),
 ("P03", "home-station", "lesson-2", "infographic-skill", "Room illustration with ring of triggers", "A safe home routine",
  "A modest Filipino home corner: a clean, well-lit table with a mask and hand rub, PD boxes on a raised shelf in a dry, cool corner labeled "
  "\"Off the floor\" and \"Oldest first\", a hand checking a bag labeled \"Check for damage and expiry\", and a wall record sheet with blank "
  "columns labeled \"Records help the home team\". Around it six skills-review triggers: \"After an infection\", \"After a "
  "hospital stay\", \"New helper\", \"New equipment\", \"Eyesight, hands or memory changed\", \"Feeling unsure\".", None),
 ("T01", "where-it-goes", "picture", "simple-figure", "Anatomy schematic plus two cards", "Where a new kidney goes",
  "Left: an anterior translucent schematic of the abdomen and pelvis (cropped torso, no face): native kidneys in place; donor kidney in the "
  "right lower abdomen with labels \"New kidney\", \"Artery\", \"Vein\", \"Ureter to bladder\", \"Your own kidneys usually stay\". Right: two "
  "cards \"Anti-rejection medicines keep the immune system calm for as long as the kidney works\" and \"A living donor has their own team and "
  "can say no at any time\". A small gray chip: \"Buying or selling organs is illegal.\"", "tx"),
 ("T02", "steady-guard", "picture", "simple-figure", "Schematic level chart plus habits", "The steady guard",
  "Left: a line staying inside a soft green band labeled \"steady medicine level\" over seven days; on day 4 a missed dose dips below into a "
  "pale orange zone where small immune-cell icons approach a kidney icon: \"Rejection can start quietly\". Right: three habit tiles \"Alarms at "
  "the same times\", \"Weekly pill organizer\", \"Refill two weeks early\", and a card \"Ask before pomelo, grapefruit or herbal products\". No "
  "drug names or level numbers.", None),
 ("T03", "dates", "lesson-2", "simple-figure", "Timeline", "Published is not the same as effective",
  "Three chapter cards: \"Evaluation\", \"Surgery (recipient and donor)\", \"Life after transplant (follow-up and medicines)\". Below, a calendar "
  "strip: \"Published November 21, 2026\" and \"Expected effective December 6, 2026 (calculated, not yet confirmed)\" with a bracket \"fifteen days\". A chip: \"Pre-authorized under the earlier rules? Ask which policy applies.\" Right: "
  "a hand holding \"Dated written estimate\". No peso amounts, no logos.", None),
 ("S01", "active-care", "lesson-1", "infographic-skill", "Care wheel", "Conservative care is active care",
  "Center: an older Filipina at home in a garden chair with family near. A ring of six labeled care segments: \"Symptom relief (itch, "
  "breathlessness, sleep)\", \"Protect remaining kidney function\", \"Anemia and fluid care\", \"Emotional and spiritual support\", \"Family "
  "meetings\", \"Plan for the future\". A visiting nurse with a bag: \"Your team stays with you.\" Warm but clinical, light background.", None),
 ("S02", "future-care", "lesson-2", "infographic-skill", "Scene plus card", "Talking about future care",
  "A family around a kitchen table, the older woman speaking, a doctor and nurse listening. On the table a card \"What matters to me\" with "
  "icons \"Being at home\", \"Free of pain\", \"With family\", \"Trying every treatment\" and a line \"Who should speak for me if I cannot: "
  "________\". Footer ribbon: \"Ask your clinician how to record it; formal documents need your care team.\"", None),
 ("A01", "co-pilot", "picture", "simple-figure", "Analogy plus clinic inset", "A co-pilot, not the driver",
  "A jeepney with an older Filipino man driving and his adult daughter in the front seat holding a map, pointing. Three labels: \"He keeps the "
  "wheel\", \"She reads the map\", \"They agree on the route\". Inset: the same pair in a clinic, the father speaking first and the daughter "
  "taking notes. No plate numbers or operator names.", None),
 ("A02", "roster", "lesson-1", "infographic-skill", "Two-panel figure", "Make tasks visible, share carefully",
  "Left: a weekly roster on a refrigerator, columns Monday to Sunday, rows \"Transport\", \"Meals\", \"Refills\", \"Paperwork\", filled with "
  "avatar circles and a \"Backup\" badge on each row. Right: two phones: a large family group chat crossed out, labeled \"Not for records, "
  "prescriptions or PhilHealth numbers\", and a small private chat with four avatars labeled \"Helpers only\".", None),
 ("A03", "empty-cup", "picture", "simple-figure", "Analogy figure", "An empty cup cannot pour",
  "A Filipina care partner holding a cup being refilled by four labeled streams: \"Sleep\", \"Shared tasks\", \"Support group\", \"Time for "
  "myself\". Side card: \"&lsquo;Can you drive Tatay to dialysis every Wednesday this month?&rsquo; works better than &lsquo;Can someone "
  "help?&rsquo;\" Badge: \"Backup helpers need training for clinical tasks.\"", None),
 ("F01", "steps", "lesson-3", "simple-figure", "Staircase", "Growing independence, step by step",
  "A staircase of four steps, the same young person growing older on each: \"Learns the names of his medicines\", \"Speaks first in "
  "visits\", \"Books his own refill; parent checks\", \"First joint visit with adult services\". A pediatric "
  "nurse walks alongside. Caption: \"Children are not small adults.\"", None),
 ("F02", "reconcile", "lesson-1", "simple-figure", "Merge diagram", "Two lists, one plan",
  "Left: two lists \"Hospital discharge list\" and \"My home list\" with placeholder bars (no drug names), two lines highlighted: \"stopped in "
  "hospital\" and \"same medicine, different name\". Arrow to a single \"Reconciled list\" held by a pharmacist and a patient&rsquo;s daughter, "
  "with arrows to \"Dialysis unit\", \"Kidney doctor\", \"Primary care doctor\". Footer: \"Bring both lists and your medicine box.\"", None),
]

# ───────────────────────── tiles (16:9, no text): one object from each module ─────────────────────────
T = {
 "card": "a teal notebook and a pen resting on a small printed booklet (pages blurred) beside a folded light blanket on the armrest of a dialysis chair, bright clinic window light",
 "C01": "a blank care-team contact card and a pen on a clinic counter beside a tricycle key on a keychain",
 "C02": "a printed laboratory report (text blurred) under a pair of reading glasses, with a urine sample cup with a blank label",
 "C03": "five small blank cards fanned out on a table beside a clinician&rsquo;s stethoscope",
 "C04": "an unbranded blister pack, a small box and a handwritten medicine list (unreadable) on a pharmacy counter",
 "C05": "a bowl of sinigang with calamansi halves and garlic beside it on a woven placemat",
 "C06": "a bathroom scale on a tiled floor beside a small glass of water",
 "C07": "a hand-rub bottle and a sealed sterile dressing packet on a clean blue tray",
 "C08": "a refrigerator door with a magnet holding a folded contact card and a medicine list (unreadable)",
 "C09": "a pair of walking shoes beside a park bench in a town plaza in morning light",
 "C10": "a clear document folder with an itemized statement (unreadable) and a pen on a hospital counter",
 "C11": "a sealed waterproof pouch with folded papers and a power bank on a windowsill with rain outside",
 "C12": "a printed medicine schedule (unreadable) with a pen and a small padlock on a desk",
 "K01": "a home blood pressure monitor and a small written card (unreadable) on a kitchen table",
 "K02": "a calendar page with an appointment circled (no readable text) beside a walking cane",
 "K03": "three interlocking brass gears on a clean white surface",
 "H01": "an empty reclining dialysis chair with a folded blanket and a pillow, softly lit",
 "H02": "a left forearm resting on a pillow with two fingers gently on the inner wrist (hands only), clean and bright",
 "H03": "a clipboard with a blurred results sheet beside a dialysis chair armrest",
 "H04": "a young coconut with a straw beside a small medicine cup of tablets and a plate",
 "P01": "a PD training model and a mask on a clean table",
 "P02": "a clear PD drainage bag held up to window light",
 "P03": "stacked PD supply boxes on a raised shelf, off the floor, in a tidy room",
 "T01": "two chairs facing each other in a quiet consultation room with a closed door and a glass of water",
 "T02": "a weekly pill organizer with morning and evening compartments beside a phone",
 "T03": "a wall calendar with two days circled (no readable text) beside a folder",
 "S01": "a cane chair with a shawl on a shaded porch beside potted plants",
 "S02": "a kitchen table with a cup of tea, a rosary and a blank card",
 "A01": "two pairs of hands on a clinic desk, an older man&rsquo;s hand resting near a notebook held by a younger woman&rsquo;s hand",
 "A02": "a refrigerator door with a hand-drawn weekly roster made of colored stickers, no readable names",
 "A03": "a ceramic mug being filled with coffee on a bench outside a church hall",
 "F01": "a school backpack beside a weekly pill organizer on a clinic table",
 "F02": "two printed lists side by side with a highlighter and a medicine box",
 "toolkit": "a clipboard with blank lined worksheet pages, a pencil and a calculator on a light wooden table",
}


def page(code):
    return HUB if code == "hub" else MODS[code]["page"]


def hero_prompt(code):
    style, arch, cam, safe, subj, goal = H[code]
    slug = page(code)
    scaf = "Scaffold A people" if style == PH else "Scaffold B still-life"
    grounded = ("Course home: the track serves patients, care partners and educators together." if code == "hub" else
                f"Module {code} real situation \"{MODS[code]['realSituation']['title']}\": {MODS[code]['realSituation']['body']}")
    p = (f"Square 1:1 {style} on a 2048×2048 canvas, composed to be displayed inside a CIRCULAR vignette occupying 85–90% of the canvas "
         f"diameter with a visible WHITE BORDER around the full circle (the circle never touches the canvas edges). Composition archetype: "
         f"{arch}. Camera: {cam}. Subject: {subj}, soft natural daylight, gentle shallow depth of field, bright and airy modern Philippine "
         f"setting. People are fictional Filipinos, calm, fully clothed and treated with dignity. Visual hierarchy: hero subject 60–70% of the "
         f"circle; 2–4 supporting context elements 20–30%; reserve a 20–25% TITLE SAFE ZONE on the {safe} side of soft gradient, clean wall or "
         f"blurred background with no faces, objects or callouts. Calm, reassuring, documentary-realistic grade harmonizing with clinical teal "
         f"#1a6b72 and navy #0f1e2e on a light background; soft edge falloff at the rim. Match the photographic look of the other Renal Care "
         f"Academy module heroes (real photograph, not illustration). Absolutely NO text of any kind: no title, caption, label, logo or "
         f"watermark; papers, screens and cards show only blurred marks.")
    human = ("No people" if style == ST else "Hands only" if "hands only" in subj else
             "Different from the previous hero: age, sex, face shape, hairstyle, hair length, clothing style and colors, accessories, posture, "
             "hand position, expression, activity, setting, camera distance and angle")
    return (f"FILE NAME: images/{slug}-vignette-hero.png\nSKILL: williamriveromd-hero-vignette v3\nIMAGE TYPE: Circular vignette hero v3 ({scaf})\n"
            f"ASPECT RATIO: 1:1 (displayed inside an 85–90% inscribed circle with white margin)\nPIXEL DIMENSIONS: 2048 × 2048\n"
            f"COMPOSITION ARCHETYPE: {arch}\nCAMERA: {cam}\nHUMAN VARIATION: {human}\nAUDIENCE: Patients and care partners\n"
            f"VISUAL GOAL: {goal}\nGROUNDED IN: {grounded}\n\nPROMPT:\n{p}" + (f"\n\n{HERO_CATH}" if code == "C07" else "") +
            f"\n\nNEGATIVE INSTRUCTIONS:\nAvoid {HERO_NEG}.\n\nQUALITY CHECK:\nSquare 2048×2048; circle 85–90% of canvas with white margin, never "
            f"cropped; real-photograph look like the other Academy heroes; one dominant subject; 20–25% empty title-safe zone on the {safe} side; "
            f"Filipino setting; people calm and dignified; no text or legible personal data; a different cast and camera from the previous hero.")


def grounded_fig(code, section):
    m = MODS[code]
    if section == "picture":
        return f"Module {code}, The everyday picture: {m['everydayPicture']}"
    li = int(section.split("-")[1]) - 1
    les = m["lessons"][li]
    return f"Module {code}, Lesson {li + 1} \"{les['title']}\": {les['body']}"


def fig_stem(code, key):
    return f"{HUB}-{MODS[code]['nn']}-{key}"


def fig_prompt(row):
    code, key, section, skill, scaf, title, body, lock = row
    locks = [LOCKS[x] for x in (lock or "").split("+") if x]
    qa = [q for x in (lock or "").split("+") if x for q in QA[x]]
    out = (f"FILE NAME: images/{fig_stem(code, key)}.png\nSKILL: williamriveromd-{skill}" + (" + williamriveromd-infographic-generator (Constitution v1.0 anatomy lock)" if locks else "")
           + f"\nIMAGE TYPE: {scaf}\nASPECT RATIO: 16:9 landscape\nPIXEL DIMENSIONS: 1672 × 941 (generate at 1536 × 1024 and keep content inside the 16:9 center)\n"
           f"AUDIENCE: Patients and care partners (plain words), and the nurses who teach them\nPLACED IN: Module {code}, section \"{section}\"\n"
           f"GROUNDED IN: {grounded_fig(code, section)}\n\nPROMPT:\nTitle at top in bold navy: \"{title}\". {body} {STYLE}")
    if locks:
        out += "\n\n" + "\n\n".join(locks)
    out += f"\n\nNEGATIVE INSTRUCTIONS:\n{FIG_NEG}\n\nQUALITY CHECK:\n{FIG_QC}"
    if qa:
        out += "\n\nANATOMY QA (Constitution v1.0, Layer G):\n" + "\n".join(f"□ {q} — confirmed" for q in qa)
    return out


def tile_prompt(code):
    name = f"images/{HUB}-card.png" if code == "card" else f"images/{HUB}-toolkit-card.png" if code == "toolkit" else f"images/{HUB}-{MODS[code]['nn']}-card.png"
    p = (f"16:9 landscape photorealistic editorial still-life for a course tile shown as small as 320 × 180 px. Subject: {T[code]}. One bold, "
         f"instantly readable subject filling the center 60% of the frame, simple uncluttered light background (white, off-white or pale teal "
         f"#eef6f7), soft daylight, gentle shadow, high-contrast silhouette so it reads at thumbnail size, colors harmonizing with teal #1a6b72 "
         f"and navy #0f1e2e. Keep a 10% clear margin on every edge. Absolutely NO text, letters, numbers, logos or watermark.")
    extra = "; the course tile also writes images/academy/landing/patients-care-partners.webp 960 × 540" if code == "card" else ""
    return (f"FILE NAME: {name} (generate at 1536 × 1024; prep exports 640 × 360 WebP{extra})\n"
            f"SKILL: williamriveromd-infographic-skill v5 (tile)\nIMAGE TYPE: Course tile (16:9, no text)\n"
            f"VISUAL GOAL: Recognizable at thumbnail size; signals the {'track' if code == 'card' else 'page'}&rsquo;s one idea.\n\n"
            f"PROMPT:\n{p}\n\nNEGATIVE INSTRUCTIONS:\nAvoid clutter, small details, faces, text of any kind, dark backgrounds, painterly or "
            f"watercolor style, cartoon style, HDR.\n\nQUALITY CHECK:\nReadable at 320 px; one subject; light background; photographic; no text.")


OG_EXTRA = {
    "hub": (HUB, "Renal Patients and Care Partners", "32 short modules · 9 pathways · free, no account", T["card"]),
    "toolkit": ("calc-patient-care-partner-toolkit", "Patient and Care Partner Toolkit", "6 tools · results trend · label sodium · fluid · weight gain · sessions · medicine clock", T["toolkit"]),
    "urgent": (f"{HUB}-urgent-help", "When to Get Urgent Help", "Know the signs. Make the call.", T["C08"]),
    "worksheets": (f"{HUB}-worksheets", "Printable Patient Worksheets", "23 blank forms for your visits", T["toolkit"]),
    "final": (f"{HUB}-final-check", "Final Knowledge Check", "Built from the modules on your path", T["C12"]),
}


def og_prompt(code):
    if code in OG_EXTRA:
        slug, title, sub, bg = OG_EXTRA[code]
    else:
        m = MODS[code]
        slug, title, sub, bg = m["page"], m["title"], f"Patients &amp; Care Partners · Module {code} · {int(m['nn'])} of 32", T[code]
    out = f"images/og/{slug}-og.jpg"
    p = (f"Social share card, final size exactly 1200 × 630 px (1.91:1). Design on a white (#ffffff) to pale teal (#eef6f7) background; "
         f"generate at 1536 × 1024 and keep every element inside the central 1536 × 804 band so the prep script can crop to 1.91:1. Left 55%: "
         f"text block in {FONT}. Small chip at top in clinical teal #1a6b72 with white text \"RENAL CARE ACADEMY · PATIENTS &amp; CARE "
         f"PARTNERS\". Title in bold navy #0f1e2e, three lines at most: \"{title}\". Subtitle in teal #1a6b72: \"{sub}\". A thin teal rule under "
         f"the title. Right 45%: a clean photorealistic still-life on a light surface: {bg}, softly lit, no faces. Bottom-right: "
         f"\"© renalcarematters.com\" in small semi-transparent navy text. Spell every word exactly as given, American English.")
    return (f"FILE NAME: {out.replace('.jpg', '.png')} (prep exports {out} 1200 × 630 JPEG ≤ 300 KB)\n"
            f"SKILL: williamriveromd-infographic-skill v5 (OG card)\nIMAGE TYPE: OG / social share card\nASPECT RATIO: 1.91:1\n"
            f"PIXEL DIMENSIONS: 1200 × 630 (final)\nAUDIENCE: Patients, care partners and kidney care teams\n"
            f"VISUAL GOAL: A share preview that names the page and shows its one idea.\n\nPROMPT:\n{p}\n\nNEGATIVE INSTRUCTIONS:\n"
            f"Avoid dark or saturated color backgrounds, extra words, misspellings, text outside the central band, cluttered collage, faces, "
            f"painterly style, serif or decorative fonts, more than one subject. Never omit renalcarematters.com.\n\nQUALITY CHECK:\nLight "
            f"background like the other Academy share cards; title readable at 600 px wide; text only in the left 55%; spelling exact.")


ART = ("FILE NAME: images/incoming/patients-care-partners/og-art/patients-care-partners.png (prep writes images/academy/og-art/patients-care-partners.webp)\n"
       "SKILL: williamriveromd-infographic-skill v5 (background art)\nIMAGE TYPE: Background art for build_academy_og.py (the script sets every word)\n"
       "PIXEL DIMENSIONS: 1536 × 1024\n\nPROMPT:\n3:2 landscape photorealistic editorial photograph on a light background: in a bright, modern "
       "Philippine dialysis unit lounge, a Filipino man in his early 60s and his adult daughter sit with a nurse educator in teal scrubs who shows "
       "them a printed booklet (pages blurred). Place the people in the RIGHT 55%; keep the LEFT 45% as clean, light, empty negative space (soft "
       "wall and window light) where the builder sets the track title and stats. Soft daylight, gentle depth of field, colors harmonizing with "
       "teal #1a6b72 and navy #0f1e2e. Absolutely NO text, logos or watermark; no legible screens or papers.\n\nNEGATIVE INSTRUCTIONS:\nAvoid "
       "text, clutter, dark backgrounds, painterly style, people in the left 45%.\n\nQUALITY CHECK:\nLeft 45% empty and light; subjects on the "
       "right; photographic; no text.")

OLD = {  # the 62 images made this morning from IMAGE_PLAN_AND_GPT_PROMPTS.md: what happens to each group
    "Heroes (9, rpcp-hero-*)": "Replace. Landscape 1536 × 1024 painted illustrations, one per pathway; the Academy uses a square 2048 × 2048 photographic hero for every page.",
    "Share cards (11, rpcp-og-*)": "Replace. Dark, saturated color backgrounds break the Academy light-background rule; Academy cards are white to pale teal with a teal chip.",
    "Tiles (10, rpcp-tile-*)": "Replace. Square painted illustrations; Academy tiles are 16:9 photographic still-lifes, one per module.",
    "Figures (32, rpcp-<code>-*)": "Interim only. Content was checked and they read well, but the painted look differs from the crisp white Academy figures and several illustrate the analogy rather than the lesson. The pages use them until the new figure for that module is placed, then drop them.",
}


def book():
    figs_by = {}
    for r in FG:
        figs_by.setdefault(r[0], []).append(r)
    n_h, n_f, n_t, n_o = len(H), len(FG), len(T), 32 + len(OG_EXTRA)
    total = n_h + n_f + n_t + n_o + 1
    o = ["# Renal Patients and Care Partners: image plan blueprint and GPT prompt pack (version 2)", "",
         "Renal Care Academy → Renal Patients and Care Partners. Prepared November 28, 2026 (evening). American English throughout. Stage 1 of the "
         "two-stage image pipeline: generate in ChatGPT image generation, then run the prep step (Stage 2). **This pack replaces "
         "`IMAGE_PLAN_AND_GPT_PROMPTS.md`.**", "",
         "## 1. What changed, and why", "",
         "The first plan gave the course one hero per pathway, in a painted style, with dark share cards and square tiles. It did not match the "
         "other Academy tracks, and most figures illustrated an analogy rather than the module&rsquo;s own lesson. This version uses the same house "
         "style and file conventions as the Social Worker, Pediatric Dialysis Nurse and other tracks, and it is built from the modules themselves:", "",
         "- **Every hero shows that module&rsquo;s own real situation** (Mang Ramon&rsquo;s tricycle and his daughter&rsquo;s phone, Aling Cora&rsquo;s report, Kuya Jun&rsquo;s swollen ankle, Ate Grace&rsquo;s dressing in the rain, Paolo&rsquo;s 2 a.m. call, Rosa in the Bicol storm, and so on). Each prompt quotes the situation it is built from (GROUNDED IN).",
         "- **Every figure label comes from the lesson text**, and each prompt names the module section it is placed in and quotes that lesson. Numbers on figures are only the ones the module states (156 sessions; 14.5% → 9.2% and 16.9% → 13.1%; published November 21, effective December 6, 2026 expected; one in four with depression).",
         "- **House style:** square photographic circular heroes, crisp white-background figures in Inter with the Academy palette, 16:9 photographic still-life tiles, and light share cards with the teal Academy chip.",
         "- **Anatomy:** Constitution v1.0 anatomy locks and anatomy QA (from `williamriveromd-infographic-generator`) on every figure that shows a kidney, nephron, fistula, PD catheter, transplant or tunneled catheter; the catheter path lock on both catheter images.", "",
         "### The 62 images made this morning", "", "| Group | Decision |", "| --- | --- |"]
    o += [f"| {k} | {v} |" for k, v in OLD.items()]
    o += ["", "## 2. Inventory", "",
          "| Image | Learning purpose | Where it appears | Count |", "| --- | --- | --- | --- |",
          f"| **Circular vignette hero** | Appreciation: the module&rsquo;s own person and moment | Top of the course home and every module | {n_h} |",
          f"| **Teaching figure** | Understanding (the mechanism) and application (an action path, card or checklist) | In the named lesson section of its module | {n_f} |",
          f"| **Course and module tiles** | Navigation: recognition on the module cards and Related Guides thumbnails | Course home cards; landing page tile | {n_t} |",
          f"| **OG share card** | Reach: a share preview naming the page | `images/og/<page>-og.jpg` for the course home, 32 modules, urgent help, worksheets, final check and toolkit | {n_o} |",
          "| **Track share-card art** | Background for the Academy composite card | `images/academy/og-art/patients-care-partners.webp` | 1 |", "",
          f"**Total: {total} prompts.** Suggested order: heroes and figures for the shared foundations (C01–C12) first, then the pathways, then tiles and share cards.", "",
          "## 3. Rules for every image", "",
          "- **Light backgrounds only** (white, off-white, soft gray, pale teal). Palette: navy #0f1e2e, teal #1a6b72, green #1f7a4d, amber #b8860b, red #b91c1c (emergency only), purple #6c3d8e.",
          "- **Photographic, not painted:** heroes and tiles are real-photograph style; figures are crisp semi-photoreal infographics like the other Academy figures. No watercolor, no warm sepia.",
          "- **Fonts on images:** Inter (or Nunito Sans, IBM Plex Sans, Manrope, DM Sans). American English spelling on every label.",
          "- **Attribution:** figures and share cards carry `© renalcarematters.com` bottom-right; heroes and tiles carry no text.",
          "- **No individual clinical targets on any image:** no fluid amounts, potassium or phosphorus values, blood pressure targets, doses, machine settings or phone numbers.",
          "- **People:** fictional Filipinos, calm, fully clothed, dignified; a different cast, camera and setting in each hero; no needles in skin, blood or wounds.",
          "- **Skills used:** `williamriveromd-hero-vignette` v3, `williamriveromd-infographic-skill` v5, `williamriveromd-simple-figure`, `williamriveromd-algorithm-generator-skill`, `williamriveromd-infographic-generator` (Constitution v1.0 anatomy locks), `tunneled-dialysis-catheter-path`.", "",
          "## 4. Production workflow", "",
          "1. Generate each prompt in ChatGPT image generation. Save each PNG with the exact FILE NAME stem into `~/Downloads/Renal Patients & Care Partners/images-v2/` (track art in `images-v2/og-art/`).",
          "2. Tell me when a batch is ready. I audit each image against its QUALITY CHECK and anatomy QA, place it (heroes `images/<page>-vignette-hero.png` + `.webp`; figures `images/<stem>.webp` + `.png`; tiles 640 × 360 WebP, the course tile also `images/academy/landing/patients-care-partners.webp`; share cards 1200 × 630 JPEG ≤ 300 KB in `images/og/`), rebuild with `python3 generate_patients_care_partners.py --patch`, and write corrected prompts for any failures in a new MD file.",
          "3. Nothing is pushed until you say so.", "",
          "## 5. Image map by module", "", "| Module | Hero (the module&rsquo;s situation) | Figures (section) |", "| --- | --- | --- |",
          f"| Course home | {H['hub'][5]} | — |"]
    for c in ORDER:
        figs = "; ".join(f"{r[5]} (`{r[2]}`)" for r in figs_by.get(c, []))
        o.append(f"| {c}. {MODS[c]['title']} | {MODS[c]['realSituation']['title']}: {H[c][5]} | {figs} |")
    o += ["", "## 6. Track-level images", "", "### Course home hero", "", "```", hero_prompt("hub"), "```", "",
          "### Course tile and Academy landing tile", "", "```", tile_prompt("card"), "```", "",
          "### Course home OG card", "", "```", og_prompt("hub"), "```", "",
          "### Track share-card art (Academy composite card)", "", "```", ART, "```", ""]
    for k, lab in (("urgent", "Urgent help page"), ("worksheets", "Worksheets page"), ("final", "Final knowledge check page"), ("toolkit", "Toolkit page")):
        o += [f"### {lab} OG card", "", "```", og_prompt(k), "```", ""]
    o += ["### Toolkit tile", "", "```", tile_prompt("toolkit"), "```", "", "## 7. Module prompts", ""]
    for c in ORDER:
        m = MODS[c]
        o += [f"### Module {c} ({int(m['nn'])} of 32): {m['title']}", "", "**Hero (circular vignette)**", "", "```", hero_prompt(c), "```", ""]
        for n, r in enumerate(figs_by.get(c, []), 1):
            o += [f"**Figure {'AB'[n - 1]}: {r[5]}**  ·  skill `{r[3]}`  ·  placed in `{r[2]}`", "", "```", fig_prompt(r), "```", ""]
        o += ["**Module tile**", "", "```", tile_prompt(c), "```", "", "**OG share card**", "", "```", og_prompt(c), "```", ""]
    o += ["## 8. Audit checklist before publishing", "",
          "- [ ] Every label spelled exactly as in the prompt (compare letter by letter).",
          "- [ ] No number on an image that is not in its prompt; no doses, fluid amounts, targets or phone numbers.",
          "- [ ] Heroes: square photograph, circle with white margin, empty title-safe zone, the module&rsquo;s own situation, a different cast from the previous hero, no text.",
          "- [ ] Figures: white background, Inter, crisp (not painted), © renalcarematters.com bottom-right; anatomy QA ticked where present.",
          "- [ ] Catheter images follow the path lock (right upper chest exit, cuff inside, over the clavicle, low right internal jugular, right atrium; red arterial, blue venous).",
          "- [ ] Tiles: 16:9 photographic still-life, readable at 320 px, no text.",
          "- [ ] Share cards: light background, teal chip, text only in the left 55%, nothing important outside the 1.91:1 band.",
          "- [ ] Any image that fails: note why, and write a corrected prompt in a new MD file in the working folder.", ""]
    return "\n".join(o).replace("&rsquo;", "’").replace("&lsquo;", "‘").replace("&amp;", "&")


def main():
    md = book()
    out = ROOT / "docs" / "tech-courses" / f"{HUB}-image-prompts.md"
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(md, encoding="utf-8"); print("wrote", out)
    for w in WORKDIRS:
        if w.exists():
            (w / "RENAL-PATIENTS-CARE-PARTNERS-IMAGE-PROMPTS.md").write_text(md, encoding="utf-8"); print("wrote", w / "RENAL-PATIENTS-CARE-PARTNERS-IMAGE-PROMPTS.md"); break


if __name__ == "__main__":
    main()
