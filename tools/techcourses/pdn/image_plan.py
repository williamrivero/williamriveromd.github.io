# -*- coding: utf-8 -*-
"""Pediatric Dialysis Nurse track: image plan blueprint and GPT prompt pack (Stage 1 of the two-stage image pipeline).

  python3 tools/techcourses/pdn/image_plan.py     # write the prompt book (repo docs copy + working folder copy)

Skills applied: williamriveromd-hero-vignette v3 (heroes), williamriveromd-infographic-skill v5 (teaching figures, tiles, OG cards),
williamriveromd-simple-figure (single-idea figures), williamriveromd-algorithm-generator-skill (decision paths), and the
tunneled-dialysis-catheter-path lock for every image that shows a tunneled hemodialysis catheter. Every figure is already wired
into the modules through figs.py, so the pages show each image as soon as prep_images.py places it. Every number on an image is in
the module text and verified against its source."""
import html, importlib.util, re
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]
HUB = "pediatric-dialysis-nurse"
WORKDIRS = [Path.home() / "mnt" / "Pedia Dialysis Nurse", Path("/Users/williamgregoryriveromd/Downloads/Pedia Dialysis Nurse")]


def _ld(n):
    s = importlib.util.spec_from_file_location("pdnplan_" + n, HERE / (n + ".py")); m = importlib.util.module_from_spec(s); s.loader.exec_module(m); return m


_C = _ld("course")
SLUGS = {m["id"]: m["slug"] for m in _C.MODULES}
TITLES = {m["id"]: html.unescape(m["title"]) for m in _C.MODULES}
FIGS = _ld("figs").FIGS
FB = {}

FONT = "Inter"
STYLE = (f"Clean renalcarematters.com house style: white (#ffffff) background, panels in soft gray (#f3f4f6) or light teal tint (#eef6f7); "
         f"navy #0f1e2e for titles and text, clinical teal #1a6b72 for headings and rules, renal green #1f7a4d for safe or done, amber "
         f"#b8860b for caution or check, clinical red #b91c1c for stop or danger, soft purple #6c3d8e for specialist or referral steps. "
         f"Typeface: {FONT} only, bold title, short labels (no paragraphs), minimum 11 pt equivalent. Semi-photoreal people and objects "
         f"where shown: Filipino children, families and nurses, children shown with dignity and fully clothed, calm expressions. Generous "
         f"whitespace. Bottom-right corner: \"© renalcarematters.com\" in small semi-transparent navy text (about 70% opacity).")
FIG_NEG = ("Avoid cartoon style, clutter, tiny unreadable labels, AI gibberish or misspelled text, overprocessed HDR, excessive saturation, "
           "generic stock-photo look. NEVER use dark, navy, charcoal, or black backgrounds; light backgrounds only. Use ONLY the sans-serif "
           "fonts Inter, Nunito Sans, IBM Plex Sans, Manrope, or DM Sans. No legible real names, ID numbers, PhilHealth numbers, or documents "
           "with readable personal data. Do not invent numbers, doses, volumes, rates or thresholds that are not written in this prompt. No "
           "drug names or doses. No visible blood spills, needles in a child&rsquo;s skin, crying or frightened close-ups, or partially "
           "dressed children. American English on every label. Never omit the renalcarematters.com attribution.")
FIG_QC = ("Mobile-readable at 360 px wide; every label spelled exactly as written in the prompt; one teaching idea only; calm, "
          "publication-grade, white or soft light-gray background; children shown with dignity; no legible personal data; "
          "© renalcarematters.com visible bottom-right.")
SIZES = {"land": ("16:9 landscape", "1672 × 941 (generate at 1536 × 1024 and keep content inside the 16:9 center)"),
         "port": ("2:3 portrait", "1024 × 1536")}
HERO_NEG = ("busy layouts, collage overload, more than four supporting scenes, dozens of icons, infographic clutter, duplicated people, "
            "repeated compositions, cropped circle, objects touching the circular border, important content inside the title safe zone, "
            "baked-in text, titles, captions, logos, watermarks, legible documents, ID cards or screens, rectangular borders, frames, banners, "
            "dark backgrounds, cartoon style, neon, HDR, over-saturation, distorted hands or faces, extra fingers, visible blood, needles in "
            "skin, crying, frightened or distressed children, partially dressed children, adult-sized equipment on a small child")
PH, ST = "photorealistic editorial photograph", "photorealistic still-life"

CATH_LOCK = ("ANATOMY LOCK — CATHETER PATH (follow exactly; overrides style): Anterior view, so the patient&rsquo;s RIGHT side is on the IMAGE "
             "LEFT. The whole catheter is on the patient&rsquo;s right (image left) and never crosses the midline. 1. EXIT SITE: right upper "
             "anterior chest wall, below the clavicle, a few finger-breadths lateral to the sternum, above the nipple line; below it a hub "
             "splits into two short external limbs hanging downward, RED clamp and cap (arterial) and BLUE clamp and cap (venous). 2. CUFF: a "
             "small textured cream-white Dacron cuff band INSIDE the subcutaneous tunnel just above the exit site, under the skin. 3. TUNNEL: "
             "from the cuff the catheter runs UPWARD beneath the skin of the anterior chest wall, passing OVER (in front of) the medial "
             "clavicle, never beneath it. 4. VENOTOMY AND LOOP: just above the clavicle it makes ONE smooth gentle U-shaped turn and enters the "
             "LOW right internal jugular vein, lateral to the common carotid artery. 5. INTRAVASCULAR COURSE: straight down the right internal "
             "jugular vein, right brachiocephalic vein, superior vena cava, RIGHT ATRIUM. 6. TIP: upper-to-mid right atrium. Child-sized "
             "proportions throughout. Never: mirrored anatomy, catheter under the clavicle or in the subclavian vein, crossing the midline, "
             "exit site in the neck or on the abdomen, external cuff, sharp kink or double loop, tip in the right ventricle or high superior "
             "vena cava, red/blue clamps swapped.")

# ───────────────────────── heroes (21) ─────────────────────────
# (id or "hub", style, archetype, camera, safe side, subject, audience, goal)
H = [
 ("hub", PH, "J Environmental Storytelling", "eye level, medium-wide", "upper-left",
  "a Filipina pediatric dialysis nurse in her late 30s with a round face, a low bun of black hair and teal scrubs with a small cartoon-free "
  "lanyard, kneeling at eye level beside a seven-year-old girl in a child-sized dialysis chair; the girl wears a yellow T-shirt and holds a "
  "picture book on her lap while her mother sits close holding her hand; a softly blurred child-sized hemodialysis machine and colorful "
  "but uncluttered wall in a bright pediatric dialysis room", "Mixed", "A child on dialysis is still a child; the nurse meets her at her level."),
 ("01", PH, "H Clinical", "over-the-shoulder, slightly high", "right",
  "a young Filipino nurse in his early 30s with short wavy hair, rimless glasses and navy scrubs speaking with a senior Filipina nurse "
  "educator in her 50s with short gray-streaked hair and a white cardigan, both looking at a closed binder at a nurses&rsquo; station "
  "outside a pediatric dialysis room; a child&rsquo;s drawing taped to the glass behind them (blurred)",
  "Nurses", "Know your authorization before your first shift."),
 ("02", PH, "A Editorial Portrait", "side profile, medium distance", "upper-right",
  "a Filipina mother in her late 20s with a ponytail and a floral blouse holding her three-year-old son on her lap in a clinic room while "
  "a nurse in light-blue scrubs shows them a simple model of a kidney; the toddler reaches for the model, curious",
  "Mixed", "Why this child&rsquo;s kidneys failed shapes everything that follows."),
 ("03", PH, "F Human Connection", "low angle at child&rsquo;s eye level", "upper-left",
  "a Filipina nurse in her 40s with a short bob and a lavender scrub top crouched beside a nine-year-old girl in a dialysis chair, both "
  "looking at a small picture card the girl holds; the girl&rsquo;s father stands slightly behind, one hand on the chair",
  "Mixed", "Speak to the child first, at her eye level, and ask for her agreement."),
 ("04", ST, "C Still-Life", "top-down flat lay", "upper-right",
  "a pediatric digital scale, a small blood pressure cuff in a child size beside a larger one, a measuring tape, a calculator and a "
  "clipboard with a blurred chart arranged neatly on a clean white treatment table",
  "Nurses", "Small bodies leave small margins; measure carefully."),
 ("05", PH, "H Clinical", "close-up of hands, slightly angled", "upper-left",
  "hands only: a nurse&rsquo;s gloved hands scrubbing a catheter hub with an antiseptic pad above a clean sterile field on a small tray, "
  "a child&rsquo;s sleeve and a stuffed toy just visible at the frame edge, blurred",
  "Nurses", "Hands and hubs are the main gates; keep them clean."),
 ("06", ST, "C Still-Life", "45-degree tabletop", "right",
  "two oral syringes of different sizes, a small amber medicine bottle without a readable label, a pill organizer and a pediatric "
  "dosing cup on a light counter, with soft daylight",
  "Nurses", "Every pediatric dose is a calculation; check it twice."),
 ("07", PH, "J Environmental Storytelling", "wide, eye level", "upper-right",
  "a Filipino father in his 30s with a crew cut and a gray polo sitting on a bed beside his five-year-old son, who is asleep under a "
  "light blanket next to a home PD cycler on a clean bedside table, warm lamp light in a tidy modest bedroom",
  "Mixed", "PD in children lets therapy happen at home while they sleep."),
 ("08", PH, "H Clinical", "close, slightly from above", "upper-left",
  "a nurse with dark brown skin tone and short natural hair, in white scrubs, gently checking a PD catheter exit site on the lower abdomen "
  "of a calm six-year-old boy lying on an exam couch in a T-shirt pulled up just enough, his mother holding a toy car nearby; the dressing "
  "area is clean and the image is respectful and modest",
  "Mixed", "Protect the exit site and you protect the catheter."),
 ("09", PH, "F Human Connection", "medium, eye level", "right",
  "a Filipina grandmother in her 60s with gray hair in a bun and reading glasses, wearing a mask, carefully connecting a PD bag on a clean "
  "table while a nurse in a teal scrub top watches with a checklist; a four-year-old grandson sits on a parent&rsquo;s lap nearby watching "
  "a tablet (screen blurred)", "Mixed", "Connection and disconnection deserve full attention."),
 ("10", ST, "C Still-Life", "low angle, soft night light", "upper-left",
  "a home PD cycler on a bedside table at night with neatly arranged tubing, a small night-light, a folded child&rsquo;s blanket with a "
  "simple star pattern and a closed notebook", "Mixed", "The cycler follows the order exactly; check the order first."),
 ("11", PH, "H Clinical", "over-the-shoulder at a phone", "upper-right",
  "a Filipina PD nurse in her 30s with shoulder-length hair and a headset at a quiet hotline desk, holding a clear empty effluent bag up to "
  "the light while speaking on the phone, a small clock on the wall (no readable time)",
  "Nurses", "A cloudy bag starts the clock; the first hour matters."),
 ("12", PH, "A Editorial Portrait", "three-quarter view", "upper-left",
  "a thirteen-year-old Filipino boy in a school uniform shirt sitting in a dialysis chair reading a book, with a tunneled catheter dressing "
  "visible as a neat white square on the right upper chest under an open collar; a nurse in navy scrubs adjusts the machine behind him, "
  "blurred", "Mixed", "Every vein a child keeps today is an access for tomorrow."),
 ("13", ST, "C Still-Life", "45-degree, studio-bright", "upper-right",
  "a small pediatric dialyzer and neatly coiled pediatric blood lines beside a larger adult dialyzer for comparison on a clean steel "
  "trolley, a sealed priming bag in the background", "Nurses", "The circuit must be small compared with the child."),
 ("14", PH, "J Environmental Storytelling", "wide, eye level", "upper-left",
  "an eleven-year-old Filipina girl lying back in a dialysis chair with a light blanket, holding a handheld game, as a male nurse in his "
  "40s with a goatee and blue scrubs checks her blood pressure with a child-sized cuff; her mother reads a magazine in a chair nearby",
  "Mixed", "Watch the child, not only the numbers."),
 ("15", PH, "H Clinical", "dynamic, slightly high", "right",
  "a small team of three Filipino nurses and a pediatrician gathered calmly around a dialysis chair with a pediatric emergency cart "
  "beside it, one nurse holding a clipboard, a teenage patient sitting up and being spoken to reassuringly; the scene is a drill, organized "
  "and calm", "Nurses", "Know your role before the emergency."),
 ("16", PH, "J Environmental Storytelling", "wide, eye level", "upper-left",
  "a provincial pediatric ward bed with a nine-year-old boy resting under a blanket, an acute PD setup with bags hanging on a stand, and a "
  "Filipina nurse in her 30s with a ponytail writing on a clipboard at the bedside; rain visible softly through a window",
  "Mixed", "Acute PD can save a child where machines are scarce."),
 ("17", PH, "A Editorial Portrait", "side view, eye level", "upper-right",
  "a seven-year-old Filipino boy standing straight against a wall stadiometer, shoes off, while a nurse with a short pixie cut in a green "
  "scrub top lowers the head piece gently; his mother watches smiling",
  "Mixed", "Growth is an outcome; measure it every time."),
 ("18", PH, "F Human Connection", "medium, eye level", "upper-left",
  "a Filipina nurse in her 50s with silver-streaked hair and a white blouse sitting at a kitchen table in a modest home with a Filipina "
  "grandmother in her late 60s, practicing on a PD training model while a six-year-old girl draws at the end of the table; picture cards "
  "spread on the table", "Mixed", "Readiness is shown, not counted."),
 ("19", PH, "A Editorial Portrait", "three-quarter, eye level", "right",
  "a sixteen-year-old Filipina with long straight hair and a denim jacket talking privately with a nurse in his late 20s in a quiet "
  "consultation room, both seated, the teen holding a phone face-down and a small notebook; a window with daylight behind",
  "Mixed", "Treat the adolescent as a partner; transition is a process."),
 ("20", ST, "C Still-Life", "top-down flat lay", "upper-right",
  "a neat portfolio folder, a printed run chart with dots and a dashed line (no numbers), a pen, a small calendar and a stethoscope on a "
  "light desk", "Nurses", "Know who governs what, count honestly, and improve one thing at a time."),
]

# ───────────────────────── teaching figures (41, keyed to figs.py) ─────────────────────────
# key: (skill, image type, title, body)
FG = {
 "pdn00_margins": ("simple-figure", "Comparison infographic", "Small body, small margins",
   "Two side-by-side panels. Left: a semi-photoreal Filipino adult silhouette labeled \"Adult 70 kg\" with a tall bar labeled \"Blood volume "
   "about 5,600 mL\" and a small teal slice labeled \"200 mL circuit = about 4%\". Right: a toddler silhouette labeled \"Child 10 kg\" with a "
   "short bar labeled \"Blood volume about 800 mL\" and a large amber slice labeled \"200 mL circuit = 25%\". Footer: \"Teaching estimate: "
   "80 mL/kg\"."),
 "pdn01_a": ("infographic-skill", "Stacked card infographic", "Four separate authorizations",
   "Four stacked rounded cards with icons, top to bottom: \"1 License — PRC\", \"2 Modality training\", \"3 Facility authorization — "
   "modality, device, age and size band\" (teal highlight), \"4 Clinical privileges\". An arrow leads to a nurse beside a child-sized dialysis "
   "chair. Footer chip in amber: \"No course certificate replaces any of them.\""),
 "pdn01_b": ("simple-figure", "Journey path illustration", "The child&rsquo;s kidney journey",
   "A gentle winding path left to right with five stops: \"CKD care\", \"Preparation\", \"PD or hemodialysis\", \"Transplant\", \"Transition "
   "to adult care\". The same child grows older along the path (toddler, school child, teen, young adult). A small nurse icon stands at every "
   "stop. A thin dashed loop from \"Transplant\" back to \"PD or hemodialysis\" labeled \"If a transplant fails\"."),
 "pdn02_a": ("simple-figure", "Age band chart", "Causes change with age and region",
   "A horizontal age band from \"Infant\" to \"Adolescent\". Above the young end, a large teal block \"CAKUT and hereditary disease\"; above "
   "the older end, a purple block rising \"Immune-mediated glomerular disease\". A small map chip of Southeast Asia: \"Southeast Asia: "
   "immune-mediated glomerular disease most common\". A gray chip: \"Cause unknown in 14% worldwide\"."),
 "pdn02_b": ("infographic-skill", "Decision illustration", "Choosing a modality with the family",
   "A Filipino family (mother, father, school-age child) at a round table with a nurse and a pediatric nephrologist. Three cards on the "
   "table: \"PD at home\", \"Hemodialysis in a center\", \"Transplant before dialysis\". Around them, five small icons with labels: \"Age and "
   "size\", \"Home and caregivers\", \"Distance\", \"Abdomen and access\", \"School\". Footer: \"The best modality is the one this family can do "
   "safely.\""),
 "pdn03_a": ("simple-figure", "Four-panel infographic", "Talking with a child at each age",
   "Four panels left to right, each with a semi-photoreal scene and one short tip: \"Infant — comfort and the parent close\"; \"Toddler — "
   "short honest words just before\"; \"School age — reasons and real choices\"; \"Adolescent — privacy and a say\". The nurse is at eye "
   "level in every panel."),
 "pdn03_b": ("algorithm-generator-skill", "Two-track flow", "Assent beside consent",
   "Two parallel lanes: top lane \"Parent or guardian: informed consent\"; bottom lane \"Child: assent in words that fit the age\". Both meet "
   "at \"Shared plan\". From the child lane, a branch \"Child says no\" leads to three steps: \"Pause if safe\", \"Find the fear\", \"Change "
   "what you can\". A small amber note: \"Urgent care: least restrictive approach, document\"."),
 "pdn04_a": ("simple-figure", "Fluid balance diagram", "Every route counts",
   "A child at the center of a balance scale. Left pan labeled \"In\" with icons: \"Feeds\", \"Drinks\", \"IV fluids\", \"Flushes\", "
   "\"Medicines\". Right pan labeled \"Out\": \"Urine\", \"Stool\", \"Drains\", \"Dialysis removal\". A teal callout on the flushes: \"10 flushes "
   "× 5 mL = 50 mL\"."),
 "pdn04_b": ("simple-figure", "Worked example card", "Arithmetic with units",
   "A clean card with three lines: \"300 mL ÷ 3 h = 100 mL/h\", \"100 mL/h ÷ 20 kg = 5 mL/kg/h\", and a crossed-out worksheet stub in red: "
   "\"300 mL/h ✗\". A green footer: \"Units at every step. A second person calculates without seeing your answer.\""),
 "pdn05_a": ("infographic-skill", "Annotated illustration", "How organisms reach the child",
   "A semi-photoreal clothed school-age child with a PD catheter (abdomen, dressing only) and a dressing on the right upper chest. Five "
   "labeled arrows toward the child: \"Hands\", \"Catheter hubs\", \"Exit site\", \"Diapers\", \"Gastrostomy\". Beside each arrow a green "
   "shield with the protection: \"Hand hygiene\", \"Scrub the hub\", \"Clean, dry dressing\", \"Exit away from the diaper\", \"Plan with the "
   "team\"."),
 "pdn05_b": ("simple-figure", "Before-and-after bar chart", "Bundles that lowered infection",
   "Two pairs of bars. Pair 1 labeled \"Hemodialysis catheter infections per 100 patient-months\": amber bar \"Before 3.3\", green bar "
   "\"After 48 months 0.8\". Pair 2 labeled \"PD peritonitis per patient-year\": amber \"Before 0.63\", green \"After 36 months 0.42\". "
   "Footnote: \"SCOPE collaborative; before-and-after comparisons\"."),
 "pdn06_a": ("simple-figure", "Single-idea illustration", "The ten-fold error",
   "Two oral syringes side by side: left filled to a small mark labeled \"0.5 mL\" (green check), right filled to a large mark labeled "
   "\"5 mL\" (red cross). Above, a large order card reading \".5 mL\" with the missing leading zero circled in red. Footer: \"Leading zero "
   "always. Trailing zero never.\""),
 "pdn06_b": ("algorithm-generator-skill", "Four-step flow", "The independent double check",
   "Four rounded steps left to right: \"1 Nurse A calculates\", \"2 Nurse B calculates separately\", \"3 Compare with the order and today&rsquo;s "
   "weight\", \"4 Match → give\". From step 3, a red branch: \"Mismatch → stop, ask the prescriber or pharmacist\"."),
 "pdn07_a": ("infographic-skill", "Annotated scale illustration", "Fill volume is scaled to body surface area",
   "Left: a child silhouette with a label \"Body surface area (m²) = √(height × weight ÷ 3,600)\". Right: a vertical scale in mL/m² with an "
   "amber band at \"about 800 mL/m² — often the upper limit under age 2\" and a teal band rising to \"about 1,400 mL/m² — recruitment plateau "
   "from age 2\". A note: \"Tolerance decides\"."),
 "pdn07_b": ("simple-figure", "Annotated order card", "Reading a pediatric PD order",
   "A mock PD order card with blurred handwriting and five highlighted fields, each with a check box and a label: \"Weight, height, BSA\", "
   "\"Fill volume in mL and mL/m²\", \"Dextrose strength\", \"Dwell time and cycles\", \"Last fill\". Footer: \"Check every field against "
   "today&rsquo;s size.\""),
 "pdn08_a": ("infographic-skill", "Cross-section illustration", "Catheter design and exit site",
   "A schematic cross-section of a child&rsquo;s abdominal wall showing a PD catheter with two cream-colored cuffs (labeled \"Deep cuff\" and "
   "\"Superficial cuff\") inside the tunnel and the exit site pointing downward. Small icons mark \"Diaper line\" and \"Gastrostomy\" with "
   "arrows showing the exit placed away from both. Footer chip: \"Double cuff, downward or lateral exit (ISPD 2024, 2D)\"."),
 "pdn08_b": ("algorithm-generator-skill", "Decision path", "When it will not drain",
   "A vertical path of five rounded steps: \"Clamps and kinks\", \"Bag below the abdomen\", \"Change position\", \"Bowels and bladder\", "
   "\"Fibrin strands\", ending in \"Still slow? Call the PD team\". A red stop box on the side: \"Pain, fever or cloudy fluid → call now\"."),
 "pdn09_a": ("simple-figure", "Step sequence", "The exchange in a small body",
   "Six numbered tiles with small semi-photoreal scenes: \"1 Prepare room and child\", \"2 Mask and hand hygiene\", \"3 Check bag and order\", "
   "\"4 Drain\", \"5 Flush before fill\", \"6 Fill the ordered volume\". Tiles 1 and 6 outlined in teal; a small amber label on tile 6: "
   "\"Small volume — measure carefully\"."),
 "pdn09_b": ("simple-figure", "Comparison panels", "Dry versus wet contamination",
   "Two panels. Left \"Dry\": a clamped transfer set, a touched connector, no fluid flowing; steps \"Clamp, cover, replace, report\". Right "
   "\"Wet\": an open transfer set with fluid flowing; steps \"Clamp now, cover, call the PD team\" and an amber chip \"Prophylaxis decision by "
   "the team\"."),
 "pdn10_a": ("simple-figure", "Scene with chart", "Cycling small volumes",
   "Left: a home cycler beside a child&rsquo;s bed at night. Right: a simple line chart across the night with repeated small fill and drain "
   "steps labeled \"Fill\", \"Dwell\", \"Drain\"; one drain step dips short and is marked with an amber alarm icon labeled \"Low drain\"."),
 "pdn10_b": ("infographic-skill", "Three-row reference card", "Alarms as clinical signals",
   "Three rows, each with an alarm icon, \"What it may mean\" and \"First response\": \"Low drain — position, constipation, catheter tip — "
   "check lines and position\"; \"Line occlusion — clamp closed or kinked line — check clamps and line path\"; \"Fill problem — bag clamp or "
   "empty bag — check bags\". Red footer: \"Pain, cloudy fluid or fever: stop and call\"."),
 "pdn11_a": ("simple-figure", "Four-tile criteria card", "Two of four",
   "Four tiles: \"Effluent white cells above 100/mm³\", \"50% or more neutrophils\", \"Pain or fever\", \"Positive culture\". A teal banner "
   "across: \"Any two = empiric diagnosis\". A small amber note: \"Dry day? Instill and wait at least 2 hours before sampling\"."),
 "pdn11_b": ("algorithm-generator-skill", "Timeline", "The first hour",
   "A horizontal timeline from a cloudy bag icon: \"0 min Sepsis screen\", \"Keep the bag\", \"Call the PD team (SBAR)\", \"Sample correctly\", "
   "\"Antibiotics as ordered, without delay\". A red branch at the start: \"Drowsy, fast breathing, cold hands → emergency now\"."),
 "pdn12_a": ("infographic-skill", "Anatomy and timeline illustration", "Access for a lifetime",
   "Left: a schematic child&rsquo;s upper body (glass-like translucent, no face) with a tunneled catheter on the right upper chest following "
   "the locked path, and the left forearm marked with a teal band labeled \"Protected for a fistula — no needles\". Right: a timeline \"Age "
   "8 → 18 → 40\" with a vein icon at each point. Footer: \"Every vein is a future access.\" " + CATH_LOCK),
 "pdn12_b": ("simple-figure", "Checklist board", "The catheter care bundle",
   "A clean checklist board with six icon rows and green check boxes: \"Hand hygiene\", \"Mask\", \"Scrub the hub\", \"Exit-site care\", "
   "\"Clean dry dressing\", \"Aseptic connect and disconnect\". Header chip: \"Every step, every time\"."),
 "pdn13_a": ("simple-figure", "Proportion illustration", "The 10% rule",
   "A child silhouette with a vertical bar labeled \"Estimated blood volume\" and a horizontal teal line at \"10%\". Beside it, a small "
   "dialyzer and lines with their combined volume shaded. Two examples: \"10 kg child: circuit 8.5% — below 10%\" (green) and \"3.5 kg "
   "newborn: circuit 23% — priming plan needed\" (amber)."),
 "pdn13_b": ("algorithm-generator-skill", "Decision path", "The priming decision",
   "Four steps: \"Estimate blood volume\", \"Add lines + dialyzer volume\", \"Compare with 10%\", then two branches: \"Below 10% → saline prime "
   "per order\" and \"Above 10% → albumin or blood prime per written order\". A purple chip: \"The prescriber decides the prime\". A small "
   "note: \"Plan whether the circuit is returned at the end\"."),
 "pdn14_a": ("simple-figure", "Single-scene illustration", "First sessions and disequilibrium",
   "A child in a dialysis chair at a first session with a slowly turning blood pump icon labeled \"Slow\" and a short clock labeled \"Short\". "
   "Three amber warning chips around: \"Headache\", \"Vomiting\", \"Restlessness or confusion\". Footer: \"Gentle start so urea falls "
   "slowly.\""),
 "pdn14_b": ("simple-figure", "Monitoring timeline", "Monitoring during the session",
   "A horizontal session timeline with check icons at intervals: \"Behavior\", \"Heart rate trend\", \"Blood pressure\", \"Color and "
   "comfort\", \"Access and pressures\", \"Fluid removed\". Near the end of the timeline an amber zone labeled \"Near target weight: watch "
   "closely\"."),
 "pdn15_a": ("infographic-skill", "Annotated illustration", "Early warning in children",
   "A calm semi-photoreal school-age child in a dialysis chair with six small labeled icons around: \"Quiet or irritable\", \"Heart rate "
   "rising\", \"Slow capillary refill\", \"Cool hands\", \"Fast breathing\", \"Yawning\". A small gray chip at the bottom: \"Low blood "
   "pressure comes late\"."),
 "pdn15_b": ("algorithm-generator-skill", "Three-step emergency card", "Air in the venous line",
   "Three large rounded steps in red outline with icons: \"1 Stop the pump\", \"2 Clamp the venous line\", \"3 Call and position as "
   "trained\". Above, an air detector alarm icon on a venous line with small bubbles. Footer: \"Then follow the unit emergency "
   "procedure.\""),
 "pdn16_a": ("simple-figure", "Formula card", "Percent fluid overload",
   "A formula card: \"%FO = (fluid in − fluid out) ÷ admission weight × 100\". Worked example: \"(3.8 L − 1.3 L) ÷ 25 kg × 100 = 10%\". Below, "
   "three small bars labeled \"Under 10%\", \"10–20%\", \"20% or more\" with a gray note: \"Registry: higher overload, higher mortality "
   "(association)\"."),
 "pdn16_b": ("simple-figure", "Scene illustration", "Acute PD where machines are scarce",
   "A bright provincial pediatric ward with a nine-year-old boy resting in bed, PD bags on a stand with a Y-shaped closed tubing set, and a "
   "nurse writing on an hourly fluid sheet. A teal chip: \"PD suitable for pediatric AKI (ISPD 2020, 1C)\"."),
 "pdn17_a": ("simple-figure", "Growth chart illustration", "Growth is an outcome",
   "A clean growth chart with percentile curves and a child&rsquo;s plotted height line flattening below the \"3rd percentile\" curve, an amber "
   "callout \"Height velocity below the 25th percentile\". Beside it, a nurse measuring a child on a stadiometer. Footer: \"Measure, plot, "
   "refer.\""),
 "pdn17_b": ("infographic-skill", "Team circle infographic", "The feeding team",
   "A child at the center with four people around: \"Renal dietitian — writes the plan\" (purple), \"Nurse — measures and reports\" (teal), "
   "\"Parents — feed and record\", \"Pediatric nephrologist — medical plan\". Small icons at the edge: \"Breast milk or formula\", \"Food\", "
   "\"Tube feeding\", \"Protein lost in PD fluid\"."),
 "pdn18_a": ("simple-figure", "Scene illustration", "Readiness by return demonstration",
   "A Filipina grandmother performing a PD exchange on a training model while a nurse watches with a checklist; two speech bubbles: nurse "
   "\"Tell me what you do if the bag is cloudy.\" and grandmother \"Keep the bag and call the team.\" A green chip: \"Shown, not "
   "counted\"."),
 "pdn18_b": ("infographic-skill", "Home plan board", "Typhoon and outage plan",
   "A home emergency plan board with five tiles and icons: \"Supplies above flood level\", \"Charged phone and power bank\", \"PD unit "
   "hotline\", \"Manual exchange backup if trained and ordered\", \"Route to a hospital that treats children\". A small rain-cloud icon in the "
   "corner. Footer: \"Make the plan before the storm.\""),
 "pdn19_a": ("simple-figure", "Stepped path", "Transition is a process",
   "Four rising steps with an adolescent climbing: \"Parent-led\", \"Shared\", \"Self-managed\", \"Adult clinic\". Under each step two short "
   "skills: \"Names condition and medicines\"; \"Books appointments, speaks alone\"; \"Decides with the team\"; \"First adult visit "
   "confirmed\". Footer: \"Skills, not birthdays.\""),
 "pdn19_b": ("simple-figure", "Checklist illustration", "Preparing for transplant",
   "An adolescent holding a clipboard with five checked items: \"Vaccinations\", \"Growth and nutrition\", \"Veins protected\", \"School and "
   "mental health\", \"Family and donor evaluation\". A small kidney icon at the end of a path. Footer: \"Built on dialysis, months before "
   "the call.\""),
 "pdn20_a": ("infographic-skill", "Card array", "Who governs what",
   "Five cards on a desk, each with a small calendar icon labeled \"Date\": \"PRC — the nurse\", \"DOH — the facility\", \"PSN — professional "
   "guidelines\", \"PhilHealth — benefits\", \"Hospital — privileges and procedures\". Footer: \"Read every rule for its issuer, scope and "
   "date.\""),
 "pdn20_b": ("simple-figure", "Worked example card", "Infection-rate arithmetic",
   "A card: \"3 episodes ÷ (96 patient-months ÷ 12) = 3 ÷ 8 = 0.375 per patient-year\". A small gauge beside it with a green zone \"0.4 or fewer "
   "(ISPD 2024 pediatric benchmark)\" and the needle just inside. Footer: \"Count, divide by time at risk, investigate every episode.\""),
}
FA = FG

# ───────────────────────── course tiles (no text) ─────────────────────────
T = {
 "card": "a small child-sized dialysis chair with a folded yellow blanket and a soft teddy bear sitting on it, in a bright clean room",
 "01": "a nurse&rsquo;s lanyard with a blank badge resting on a closed binder beside a child&rsquo;s crayon",
 "02": "a simple anatomical kidney model beside a toddler&rsquo;s wooden toy block",
 "03": "two chairs of different heights facing each other, one child-sized, with a picture card on the small one",
 "04": "a pediatric digital scale with a small blood pressure cuff resting on it",
 "05": "an antiseptic pad packet and a capped catheter hub on a sterile blue drape",
 "06": "two oral syringes of different sizes beside a small amber bottle with no label",
 "07": "a small PD solution bag beside a child&rsquo;s night-light on a bedside table",
 "08": "a coiled PD catheter with two cuffs on a white tray",
 "09": "a PD drainage bag and a mask on a clean table with a small stuffed animal",
 "10": "a home PD cycler with neat tubing on a child&rsquo;s bedside table",
 "11": "a clear PD effluent bag held up to window light",
 "12": "a dual-lumen tunneled catheter with red and blue clamps and a visible cuff on a sterile drape",
 "13": "a small pediatric dialyzer with neatly coiled blood lines",
 "14": "a child-sized blood pressure cuff draped over the arm of a dialysis chair",
 "15": "a pediatric emergency cart with closed drawers and a small bag-valve mask on top",
 "16": "PD bags on an IV stand beside a hospital bed window with rain",
 "17": "a wall stadiometer with a child&rsquo;s small shoes placed neatly below it",
 "18": "a PD training model and picture cards on a kitchen table",
 "19": "a school backpack leaning against a dialysis chair",
 "20": "a portfolio folder and a printed run chart (dots and a dashed line, no numbers) on a desk",
}


def hero_prompt(i, style, arch, cam, safe, subj, aud, goal):
    slug = HUB if i == "hub" else f"{HUB}-{i}-{SLUGS[i]}"
    scaf = "Scaffold A people" if style == PH else "Scaffold B still-life"
    extra = (" Show the tunneled catheter only as a neat white dressing on the patient&rsquo;s right upper chest, below the clavicle, with a "
             "short capped dual limb (red and blue clamps) emerging below it; no tube in the neck." if i == "12" else "")
    p = (f"Square 1:1 {style} on a 2048×2048 canvas, composed to be displayed inside a CIRCULAR vignette occupying 85–90% of the canvas "
         f"diameter with a visible WHITE BORDER around the full circle (the circle never touches the canvas edges). Composition archetype: "
         f"{arch}. Camera: {cam}. Subject: {subj}, soft natural daylight, gentle shallow depth of field.{extra} Children appear calm, "
         f"comfortable, fully clothed and treated with dignity; equipment is child-sized. Visual hierarchy: hero subject 60–70% of the circle; "
         f"2–4 supporting context elements 20–30%; reserve a 20–25% TITLE SAFE ZONE on the {safe} side of soft gradient, clean wall or "
         f"blurred background with no faces, objects or callouts. Calm, reassuring, documentary-realistic grade harmonizing with clinical "
         f"teal #1a6b72 and navy #0f1e2e on a light background; soft edge falloff at the rim. Absolutely NO text of any kind: no title, "
         f"caption, label, logo, or watermark; papers, screens and ID cards show only blurred marks.")
    human = ("No people" if style == ST else "Hands only; skin tone and hand position differ from the previous image" if "hands only" in subj
             else "Changed from the previous hero in this track: ages of the child and adults, sex, face shape, hairstyle, hair length, "
                  "clothing style and colors, accessories, posture, hand position, expression, activity, setting, camera distance and angle")
    return slug, (f"FILE NAME: images/{slug}-vignette-hero.png\nSKILL: williamriveromd-hero-vignette v3\nIMAGE TYPE: Circular vignette hero v3 ({scaf})\n"
                  f"ASPECT RATIO: 1:1 (displayed inside an 85–90% inscribed circle with white margin)\nPIXEL DIMENSIONS: 2048 × 2048\n"
                  f"COMPOSITION ARCHETYPE: {arch}\nCAMERA: {cam}\nHUMAN VARIATION: {human}\nAUDIENCE: {aud}\nVISUAL GOAL: {goal}\n\n"
                  f"PROMPT:\n{p}\n\nNEGATIVE INSTRUCTIONS:\nAvoid {HERO_NEG}.\n\nQUALITY CHECK:\nSquare 2048×2048; circle 85–90% of canvas "
                  f"with white margin, never cropped; one dominant subject; 20–25% empty title-safe zone on the {safe} side; Filipino "
                  f"setting; children calm and dignified; no text or legible personal data; a different cast and camera from the previous hero.")


def fig_prompt(stem, skill, scaf, title, body, aud="Pediatric dialysis nurses and families"):
    ratio, px = SIZES["land"]
    return (f"FILE NAME: images/{stem}.png\nSKILL: williamriveromd-{skill}\nIMAGE TYPE: {scaf}\n"
            f"ASPECT RATIO: {ratio}\nPIXEL DIMENSIONS: {px}\nAUDIENCE: {aud}\n\nPROMPT:\nTitle at top in bold navy: \"{title}\". {body} "
            f"{STYLE}\n\nNEGATIVE INSTRUCTIONS:\n{FIG_NEG}\n\nQUALITY CHECK:\n{FIG_QC}"
            + ("\n\nCATHETER QA:\n□ Chest-wall exit → cuff inside tunnel → tunnel over clavicle → one smooth loop into the low right internal "
               "jugular vein → superior vena cava → tip in right atrium □ Entirely on the image left; never crosses midline □ Red = arterial, "
               "blue = venous" if "ANATOMY LOCK" in body else ""))


def tile_prompt(i):
    name = f"images/{HUB}-card.png" if i == "card" else f"images/{HUB}-{i}-card.png"
    p = (f"16:9 landscape photorealistic editorial still-life for a course tile shown as small as 320 × 180 px. Subject: {T[i]}. One bold, "
         f"instantly readable subject filling the center 60% of the frame, simple uncluttered light background (white, off-white or pale "
         f"teal #eef6f7), soft daylight, gentle shadow, high-contrast silhouette so it reads at thumbnail size, colors harmonizing with teal "
         f"#1a6b72 and navy #0f1e2e. Keep a 10% clear margin on every edge. Absolutely NO text, letters, numbers, logos or watermark.")
    return (f"FILE NAME: {name} (generate at 1536 × 1024; prep script exports 640 × 360 WebP"
            f"{'; the course tile also writes images/academy/landing/' + HUB + '.webp 960 × 540' if i == 'card' else ''})\n"
            f"SKILL: williamriveromd-infographic-skill v5 (tile)\nIMAGE TYPE: Course tile (16:9, no text)\n"
            f"VISUAL GOAL: Recognizable at thumbnail size; signals the {'track' if i == 'card' else 'module'}&rsquo;s one idea.\n\n"
            f"PROMPT:\n{p}\n\nNEGATIVE INSTRUCTIONS:\nAvoid clutter, small details, faces, children&rsquo;s faces, text of any kind, dark "
            f"backgrounds, cartoon style, HDR.\n\nQUALITY CHECK:\nReadable at 320 px; one subject; light background; no text.")


def og_prompt(i):
    if i == "hub":
        slug, title, sub, bg = HUB, "Pediatric Dialysis Nurse", "20 modules · PD and hemodialysis for infants, children and teens", T["card"]
    elif i == "toolkit":
        slug, title, sub, bg = f"{HUB}-toolkit", "Pediatric Dialysis Nurse Toolkit", "6 tools · fill volume · circuit volume · fluid · infection rates", \
            "a calculator, a pediatric scale, a small PD bag and a clipboard with a blurred grid"
    else:
        slug, title, sub, bg = f"{HUB}-{i}-{SLUGS[i]}", TITLES[i], f"Pediatric Dialysis Nurse · Module {int(i)} of 20", T[i]
    out = f"images/og/{slug}.jpg" if i == "toolkit" else f"images/og/{slug}-og.jpg"
    p = (f"Social share card, final size exactly 1200 × 630 px (1.91:1). Design on a white (#ffffff) to pale teal (#eef6f7) background; "
         f"generate at 1536 × 1024 and keep every element inside the central 1536 × 804 band so the prep script can crop to 1.91:1. "
         f"Left 55%: text block in {FONT}. Small chip at top in clinical teal #1a6b72 with white text \"RENAL CARE ACADEMY · NEPHROLOGY "
         f"NURSING TRACK\". Title in bold navy #0f1e2e, three lines at most: \"{title}\". Subtitle in teal #1a6b72: \"{sub}\". A thin teal rule "
         f"under the title. Right 45%: a clean photorealistic still-life on a light surface: {bg}, softly lit, no faces. Bottom-right: "
         f"\"© renalcarematters.com\" in small semi-transparent navy text. Spell every word exactly as given, American English.")
    return out, (f"FILE NAME: {out.replace('.jpg', '.png')} (prep script exports {out} 1200 × 630 JPEG ≤ 300 KB)\n"
                 f"SKILL: williamriveromd-infographic-skill v5 (OG card)\nIMAGE TYPE: OG / social share card\n"
                 f"ASPECT RATIO: 1.91:1\nPIXEL DIMENSIONS: 1200 × 630 (final)\nAUDIENCE: Pediatric dialysis nurses and kidney care teams\n"
                 f"VISUAL GOAL: A share preview that names the page and shows its one idea.\n\nPROMPT:\n{p}\n\nNEGATIVE INSTRUCTIONS:\n"
                 f"Avoid extra words, misspellings, text outside the central band, dark backgrounds, cluttered collage, faces, serif or "
                 f"decorative fonts, more than one subject. Never omit renalcarematters.com.\n\nQUALITY CHECK:\nTitle readable at 600 px "
                 f"wide; text only in the left 55%; spelling exact; light background.")


def fb_file(k):
    return FIGS[k][0]


def _mod_of(k):
    m = re.match(HUB + r"-(\d\d)-", FIGS[k][0]); return m.group(1)


def placement():
    """Which module section holds each figure macro."""
    where = {}
    for i in SLUGS:
        src = (HERE / f"m{i}.py").read_text(encoding="utf-8")
        for mm in re.finditer(r'\(\s*"([a-z0-9-]+)",\s*"[^"]*",\s*"[^"]*",\s*"""(.*?)"""', src, re.S):
            for k in re.findall(r"\{\{fig:([a-z0-9_]+)", mm.group(2)):
                where[k] = (i, mm.group(1))
        big = re.search(r'"big":\s*"""(.*?)"""', src, re.S)
        if big:
            for k in re.findall(r"\{\{fig:([a-z0-9_]+)", big.group(1)):
                where.setdefault(k, (i, "bigpicture"))
    return where


def book():
    where = placement()
    nF = len(FG)
    total = 21 + nF + 21 + 21 + 1 + 1
    o = ["# Pediatric Dialysis Nurse track: image plan blueprint and GPT prompt pack", "",
         "Renal Care Academy → Nephrology Nursing Track → By Specialization → Pediatric Dialysis Nurse. Prepared November 27, 2026. American "
         "English throughout. Stage 1 of the two-stage image pipeline: generate in ChatGPT image generation, then run the prep script (Stage 2).", "",
         "## 1. Why these images", "",
         "Every image has one job: make a pediatric dialysis decision easier to understand, apply, or appreciate. This track turns on size: small "
         "bodies, small volumes, small margins. So the teaching figures show proportions (circuit to blood volume, fill volume to body surface "
         "area), worked arithmetic, and decision paths, while the heroes show children and families as people first, cared for at eye level.", "",
         "| Image | Learning purpose | Where it appears | Count |", "| --- | --- | --- | --- |",
         "| **Circular vignette hero** | Appreciation: who is involved, where, and what is at stake | Top of the course home and each module | 21 |",
         f"| **Teaching figure** | Understanding (the central idea) and application (a check, flow or card to use on shift) | Already wired into the module text through `figs.py`; each image appears as soon as it is placed | {nF} |",
         "| **Course tile** | Navigation: recognition on the syllabus cards and module tiles | Course home module cards; Related Guides thumbnails | 21 |",
         "| **OG share card** | Reach: a share preview that names the page | `og:image` for the course home and each module (`images/og/<slug>-og.jpg`) | 21 |",
         "| **Toolkit OG card** | Reach for the calculator page | `og:image` of `guides/calc-pediatric-dialysis-nurse-toolkit.html` | 1 |",
         "| **Track share-card art** | Background for the Academy composited track card (text set by `build_academy_og.py`) | `images/academy/og-art/pediatric-dialysis-nurse.webp` | 1 |",
         "| **Landing tile** | The Pediatric Dialysis Nurse card on `academy/index.html` | `images/academy/landing/pediatric-dialysis-nurse.webp` | made from the course tile |", "",
         f"**Total: {total} prompts.**", "",
         "## 2. Rules for every image", "",
         "- **Light backgrounds only** (white, off-white, soft gray, pale teal). Palette: navy #0f1e2e, teal #1a6b72, green #1f7a4d, amber #b8860b, red #b91c1c, purple #6c3d8e; the Nephrology Nursing track accent is teal #1a6b72.",
         "- **Fonts on images:** Inter (or Nunito Sans, IBM Plex Sans, Manrope, DM Sans). American English spelling on every label.",
         "- **Attribution:** teaching figures and OG cards carry `© renalcarematters.com` bottom-right (public Academy pages, not patient documents). Heroes and tiles carry no text.",
         "- **Children:** fictional Filipino children only, calm, fully clothed, treated with dignity; no crying or frightened close-ups; no needles in a child&rsquo;s skin; child-sized equipment; a PD exit site shown only with the shirt raised just enough.",
         "- **Numbers:** an image carries only the numbers written in its prompt, each already in the module and verified (10% rule; 800 and 1,400 mL/m²; 3.3 → 0.8; 0.63 → 0.42; 0.4 benchmark; 300 mL ÷ 3 h ÷ 20 kg; 3.8 − 1.3 L ÷ 25 kg). No drug names or doses on any image.",
         "- **Tunneled catheters:** every image that shows one follows the tunneled-dialysis-catheter-path lock (right internal jugular route, exit on the right upper chest, cuff inside the tunnel, red arterial and blue venous clamps). Heroes show only the chest dressing.",
         "- **People:** a different cast, camera and setting in each hero (hero-vignette v3 human-variation rule).",
         "- **Skills used:** `williamriveromd-hero-vignette` v3 (heroes), `williamriveromd-infographic-skill` v5 (figures, tiles, OG cards), `williamriveromd-simple-figure` (single-idea figures), `williamriveromd-algorithm-generator-skill` (decision paths), `tunneled-dialysis-catheter-path` (catheter anatomy).", "",
         "## 3. Production workflow", "",
         "1. Generate each prompt in ChatGPT image generation. Save each PNG with the exact FILE NAME stem into `images/incoming/pediatric-dialysis-nurse/` in the repo (track art in a subfolder `og-art/`), or first into the working folder `~/Downloads/Pedia Dialysis Nurse/images/` for audit.",
         "2. Run `python3 tools/techcourses/pdn/prep_images.py` (`--report` lists what is still missing). It writes heroes to `images/<slug>-vignette-hero.png` + `.webp`, figures to `images/<stem>.webp` + `.png`, tiles to 640 × 360 WebP (the course tile also to `images/academy/landing/pediatric-dialysis-nurse.webp` 960 × 540), OG cards to 1200 × 630 JPEG ≤ 300 KB in `images/og/`, and the track art to `images/academy/og-art/pediatric-dialysis-nurse.webp`.",
         "3. Rebuild: `python3 generate_tech_courses.py --course pdn --patch`; `python3 tools/techcourses/pdn/expand_acronyms.py`; `python3 build_academy_og.py --art images/academy/og-art --only pediatric-dialysis-nurse --patch` and `--only academy-index`; `python3 generate_rg_thumbs.py`; `python3 patch_rg_card_thumbs.py`.",
         "4. Audit each image against its QUALITY CHECK, check one module in light and dark mode, and paste one module URL into the Facebook Sharing Debugger. Write corrected prompts for any failures in a new MD file in the working folder.", "",
         "## 4. Image map by module", "", "| Module | Hero idea | Teaching figures (section) |", "| --- | --- | --- |"]
    figs_by_mod = {}
    for k in FG:
        figs_by_mod.setdefault(_mod_of(k), []).append(k)
    o.append(f"| Course home | {H[0][7]} | {html.unescape(FG['pdn00_margins'][2])} (Module 1, big picture) |")
    for h in H[1:]:
        i = h[0]
        items = [f"{html.unescape(FG[k][2])} (`{where.get(k, ('', '?'))[1]}`)" for k in figs_by_mod.get(i, [])]
        o.append(f"| {int(i)}. {TITLES[i]} | {html.unescape(h[7])} | {'; '.join(items) or '—'} |")
    o += ["", "## 5. Track-level images", ""]
    _, txt = hero_prompt(*H[0])
    o += ["### Course home hero", "", "```", txt, "```", ""]
    f, alt, cap = FIGS["pdn00_margins"]
    o += ["### Track figure: Small body, small margins (Module 1 big picture)", "", "```", fig_prompt(f[:-5], *FG["pdn00_margins"]), "```", "",
          f"*On-page caption:* {cap}", f"*Alt text:* {alt}", ""]
    o += ["### Course tile and Academy landing tile", "", "```", tile_prompt("card"), "```", ""]
    o += ["### Course home OG card", "", "```", og_prompt("hub")[1], "```", ""]
    o += ["### Toolkit OG card", "", "```", og_prompt("toolkit")[1], "```", ""]
    o += ["### Track share-card art (Academy composited card)", "", "```",
          f"FILE NAME: images/incoming/{HUB}/og-art/{HUB}.png (prep script writes images/academy/og-art/{HUB}.webp)\n"
          "SKILL: williamriveromd-infographic-skill v5 (background art)\n"
          "IMAGE TYPE: Background art for build_academy_og.py (the script sets every word)\nPIXEL DIMENSIONS: 1536 × 1024\n\nPROMPT:\n"
          "3:2 landscape photorealistic editorial photograph on a light background: in a bright Philippine pediatric dialysis room, a Filipina "
          "nurse in her late 30s with a low bun and teal scrubs kneels at eye level beside a seven-year-old girl in a child-sized dialysis "
          "chair; the girl holds a picture book and her mother sits close. Place the people in the RIGHT 55%; keep the LEFT 45% as clean, "
          "light, empty negative space (soft wall and window light) where the builder sets the track title, group label and stats. Soft "
          "daylight, gentle depth of field, colors harmonizing with teal #1a6b72 and navy #0f1e2e. Absolutely NO text, logos or watermark; no "
          "legible screens or papers.\n\nNEGATIVE INSTRUCTIONS:\nAvoid text, clutter, dark backgrounds, distressed or crying children, "
          "needles in skin, legible documents, people in the left 45%.\n\nQUALITY CHECK:\nLeft 45% empty and light; subjects on the right; "
          "child calm; no text.", "```", ""]
    o += ["## 6. Module prompts", ""]
    for h in H[1:]:
        i = h[0]
        o += [f"### Module {int(i)}: {TITLES[i]}", ""]
        _, txt = hero_prompt(*h)
        o += ["**Hero (circular vignette)**", "", "```", txt, "```", ""]
        for n, k in enumerate(figs_by_mod.get(i, []), 1):
            skill, scaf, title, body = FG[k]
            f, alt, cap = FIGS[k]
            sec = where.get(k, ("", "?"))[1]
            o += [f"**Figure {'AB'[n - 1] if n <= 2 else n}: {html.unescape(title)}**  ·  skill `{skill}`  ·  placed in section `{sec}`  ·  key `{k}`", "",
                  "```", fig_prompt(f[:-5], skill, scaf, title, body), "```", "", f"*On-page caption:* {cap}", f"*Alt text:* {alt}", ""]
        o += ["**Course tile**", "", "```", tile_prompt(i), "```", ""]
        o += ["**OG share card**", "", "```", og_prompt(i)[1], "```", ""]
    o += ["## 7. Audit checklist before publishing", "",
          "- [ ] Every label spelled exactly as in the prompt (compare letter by letter; GPT often misspells).",
          "- [ ] No number on an image that is not in its prompt; no drug names or doses anywhere.",
          "- [ ] Children calm, clothed and dignified; no needles in skin; no crying close-ups; child-sized equipment.",
          "- [ ] Tunneled catheter images follow the path lock (right upper chest exit, cuff inside, over the clavicle, right internal jugular, right atrium; red arterial, blue venous).",
          "- [ ] Heroes: circle with white margin, title-safe zone empty, a different cast from the previous hero, no text.",
          "- [ ] Figures and OG cards: light background, Inter, © renalcarematters.com bottom-right.",
          "- [ ] OG cards: text only in the left 55%, nothing important outside the 1.91:1 band.",
          "- [ ] Any image that fails: note why, and write a corrected prompt in a new MD file in the working folder.", ""]
    return html.unescape("\n".join(o))


def main():
    md = book()
    out = ROOT / "docs" / "tech-courses" / f"{HUB}-image-prompts.md"
    out.write_text(md, encoding="utf-8"); print("wrote", out)
    for w in WORKDIRS:
        if w.exists():
            (w / "PEDIATRIC-DIALYSIS-NURSE-IMAGE-PROMPTS.md").write_text(md, encoding="utf-8"); print("wrote", w / "PEDIATRIC-DIALYSIS-NURSE-IMAGE-PROMPTS.md"); break


if __name__ == "__main__":
    main()
