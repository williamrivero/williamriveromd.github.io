# -*- coding: utf-8 -*-
"""Build the OT/PT image plan blueprint and GPT prompt pack (one Markdown file) from the plan below.
Heroes follow williamriveromd-hero-vignette v3; figures follow williamriveromd-simple-figure scaffolds (A-E) with
Constitution v1.0 anatomical-truth, negative-constraint and QA layers from williamriveromd-infographic-generator where
anatomy appears; tiles and OG art follow williamriveromd-infographic-skill (light backgrounds, Inter, renalcarematters.com).
Run:  python3 tools/techcourses/otpt/build_image_prompts.py  <output.md>"""
import importlib.util
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
_s = importlib.util.spec_from_file_location("otpt_figs", HERE / "figs.py"); F = importlib.util.module_from_spec(_s); _s.loader.exec_module(F)
_c = importlib.util.spec_from_file_location("otpt_course", HERE / "course.py"); C = importlib.util.module_from_spec(_c); _c.loader.exec_module(C)
HUB = C.HUB
MODS = {m["id"]: m for m in C.MODULES}

# ───────────── heroes: key -> (archetype, camera, people, scene, scaffold) ─────────────
HEROES = {
    "hub": ("E Lifestyle", "wide-angle environmental",
            "a Filipino physical therapist in his early 30s, tall and lean, with a side-parted undercut, rimless glasses and navy polo scrubs, and a Filipina occupational therapist in her mid 40s, petite, with a shoulder-length bob, small gold studs and a sage-green tunic; with them an older man in his late 60s on hemodialysis, stocky, balding with a white mustache, in a striped short-sleeve shirt",
            "a bright rehabilitation corner next to a hemodialysis unit; the PT guards the man as he rises from a reclining dialysis chair, the left forearm (fistula arm) free and uncovered; on a low table nearby the OT sets out a simple kitchen task (a bowl, a wooden spoon, a cutting board); machines on standby in soft focus", "A"),
    "01": ("H Clinical", "over-the-shoulder",
           "a Filipina occupational therapist in her late 20s with a high bun and freckles in a lavender tunic, and a broad-shouldered Filipino physical therapist in his 40s with a close beard and gray scrubs",
           "they read a blank referral sheet together at a rehabilitation desk near a dialysis unit doorway, one pointing to a line; a whiteboard behind them shows only colored sticky notes (no writing)", "A"),
    "02": ("D Panorama", "low-angle wide",
           "an older Filipino man in his mid 60s, slim, with gray crew-cut hair and a loose polo shirt, and a Filipina physical therapist in her 30s with a long braid and teal scrubs",
           "a long hospital staircase with soft daylight; he rests a hand on the rail at the landing halfway up while she stands one step below, calm and attentive; the staircase recedes upward", "A"),
    "03": ("H Clinical", "eye-level close",
           "a Filipino physical therapist in his mid 20s with a buzz cut and athletic build in white scrubs, kneeling, and a seated Filipino man in his early 70s with thick black-rimmed glasses and a cardigan",
           "the therapist kneels at eye level beside the patient in a dialysis waiting area, one hand lightly on the armrest, asking how he feels before a walk; a nurse in the soft-focus background checks a chart", "A"),
    "04": ("I Object Hero", "macro side view",
           "hands only: a patient's left forearm with a healed wrist fistula scar resting palm-up on a pillow, and an occupational therapist's gloved hand offering a soft green squeeze ball",
           "the forearm is uncovered and free of any cuff, band or watch; soft daylight; a folded clean towel and a disinfectant wipe canister (no readable label) in the background", "B"),
    "05": ("B Journey", "side profile",
           "a Filipina physical therapist in her early 40s with short wavy hair and a navy polo holding a stopwatch, and a Filipino man in his early 60s, medium build, salt-and-pepper hair, in a guayabera-style shirt",
           "a bright corridor with a four-meter course marked by two strips of colored tape on the floor; he walks the course while she times him from the side; a plain chair waits at the start", "A"),
    "06": ("E Lifestyle", "overhead three-quarter",
           "a Filipina occupational therapist in her mid 30s with a ponytail and a mustard cardigan, and a Filipina woman in her late 50s, plump, with curly shoulder-length hair and a floral house dress",
           "at a home kitchen table they plan a week on a large blank paper calendar with colored paper blocks (no writing); a thermos and two cups of tea; morning window light", "A"),
    "07": ("H Clinical", "eye-level",
           "an elderly Filipino man in his late 60s, tall and thin, with neatly combed white hair and a short-sleeved button shirt, his adult daughter in her 30s with a pixie cut and office blouse, and an occupational therapist in her 50s with reading glasses on a cord",
           "at a dining table he sorts tablets into a weekly pill organizer (no readable labels) while the therapist watches and the daughter looks on; a refrigerator in soft focus", "A"),
    "08": ("J Environmental Storytelling", "rear three-quarter",
           "a Filipina woman in her late 70s, small and slightly stooped, with silver hair in a low bun, using a front-wheeled walker, and a Filipino physical therapist in his mid 30s with a man-bun and maroon scrubs wearing a gait belt guard position",
           "she steps away from a reclining dialysis chair toward a bright exit; he walks at her side holding the gait belt, never her arm; clear dry floor; brakes visible on the chair", "A"),
    "09": ("A Editorial Portrait", "three-quarter",
           "a Filipino man in his early 50s, muscular but deconditioned, with a shaved head and a faded construction-company T-shirt (no logo), and a Filipina physical therapist in her late 20s with a sleek low ponytail counting on her fingers",
           "he sits on a firm chair doing a knee extension with a small ankle weight in a bright rehabilitation gym; resistance bands hang neatly on a rack behind", "A"),
    "10": ("I Object Hero", "wide-angle",
           "a Filipina woman in her early 60s with a gray pixie cut and a light blue blouse, reclining in a dialysis chair, and a physical therapist partly in frame",
           "a compact bed cycle is fixed at the foot of the reclining dialysis chair; she pedals with her legs; her fistula arm rests still on an armrest with taped needles and lines clear of the pedals; the dialysis machine stands in soft focus; a wall clock with no numbers readable", "A"),
    "11": ("H Clinical", "eye-level",
           "a Filipino man in his mid 40s, wiry, sun-tanned, with short spiky hair and a tank top under an open shirt, and a Filipina occupational therapist in her 30s with a headscarf",
           "in a clean storeroom they practice lifting a plain cardboard box of dialysis solution from a waist-high shelf, held close to the body; a second shelf at waist height holds more boxes (no brand or readable text)", "A"),
    "12": ("H Clinical", "high three-quarter",
           "a weak Filipino man in his late 40s with stubble and a hospital gown, and two therapists (a woman in her 30s in teal scrubs, a man in his 50s in navy scrubs)",
           "they help him sit at the edge of an intensive care bed; a continuous kidney replacement machine stands beside the bed with lines secured and a nurse watching the lines; monitors in soft focus with no readable numbers", "A"),
    "13": ("B Journey", "low side angle",
           "a Filipina woman in her early 60s, slender, with dyed auburn hair in a clip and athletic leggings, and a Filipino physical therapist in his early 30s with curly hair and a gray polo",
           "she steps up onto a low wooden platform in a rehabilitation gym, one hand on a rail, while he coaches beside her; a window with greenery behind", "A"),
    "14": ("H Clinical", "eye-level close",
           "a Filipino man in his late 60s, heavyset, with a gray goatee and a polo shirt, seated, wearing a below-knee prosthesis on the right leg, and a physical therapist in her 40s with a side braid",
           "she checks the fit of the socket at his knee while he watches; a pair of walking shoes and a folded prosthetic sock on the bench beside them", "A"),
    "15": ("J Environmental Storytelling", "wide-angle",
           "a Filipina occupational therapist in her mid 30s with a short undercut and a tape measure, and a Filipino family (a man in his 40s and a teenage girl) watching from a doorway",
           "inside a small, tidy Filipino home she measures a narrow bathroom doorway with a raised threshold; a plastic shower chair and a commode chair stand nearby", "A"),
    "16": ("A Editorial Portrait", "environmental portrait",
           "a Filipino man in his mid 40s with a neat side part and work shirt with rolled sleeves, and a Filipina occupational therapist in her 50s with short gray hair",
           "they review a blank weekly shift schedule printed as colored blocks beside a wall calendar with three days shaded, in a small electrical repair shop with tools neatly arranged", "A"),
    "17": ("E Lifestyle", "eye-level",
           "a Filipino boy about 12 years old with a mop of hair and a school P.E. shirt (no text), a pediatric physical therapist in her late 20s with a ponytail, and his mother in her 30s watching",
           "the boy balances on a foam beam holding a soft ball in a bright pediatric therapy room with colorful mats; his mother smiles from a chair", "A"),
    "18": ("I Object Hero", "top-down",
           "hands only: two pairs of hands (a therapist and a coordinator) at a desk",
           "printed circulars with colored tab dividers, a highlighter and a calendar on a desk; no readable words on any page", "B"),
    "19": ("I Object Hero", "over-the-shoulder",
           "two therapists seen from behind (a man in teal scrubs, a woman in a white coat over a blouse)",
           "they review a line chart on a monitor showing dots rising above a horizontal median line (no readable numbers or words), in a quiet office with a plant", "A"),
    "20": ("J Environmental Storytelling", "wide-angle",
           "an occupational therapist (a Filipina in her 30s with a high ponytail) and a physical therapist (a Filipino in his 40s with a buzz cut and glasses) presenting to a small seated team including a nurse and a physician",
           "a bright training room with a whiteboard covered in colored sticky notes arranged in two columns (no writing); a rehabilitation walker and a pedal cycle stand at the side", "A"),
}

# ───────────── figures: key -> (module, section, scaffold, size, purpose, audience, content) ─────────────
A_TRUTH_FISTULA = ("Anatomical truth: a radiocephalic fistula joins the radial artery to the cephalic vein at the wrist; the arterialized vein runs up the "
                   "forearm, wide and slightly raised; arteries are thick-walled with a circular lumen, the arterialized vein thinner-walled and larger; "
                   "blood flows from artery into vein and up toward the elbow. Never show a needle, cuff or band on the fistula as acceptable.")
FIGS = {
    "otpt00_capacity_gap": ("Hub, M02", "start / big picture", "D", "1792 × 1024", "Understand", "clinicians (OT, PT)",
        "Title: 'The capacity–demand gap'. Left: a tall teal bar labeled 'Healthy adult capacity'. Right: a shorter teal bar labeled 'Capacity on dialysis'. A dashed amber line across both labeled 'Demand of daily tasks' with small icons (stairs, bathing, walking to a jeepney stop). A green upward arrow under the short bar labeled 'PT raises capacity'; a green downward arrow on the dashed line labeled 'OT lowers demand'. Small gray causes beside the short bar: 'muscle loss', 'anemia', 'blood pressure swings', 'neuropathy', 'bone disease'. Bottom strip: 'Rehabilitation widens the gap from both sides.'"),
    "otpt01_who_owns": ("M01", "big picture", "D", "1792 × 1024", "Apply", "clinicians",
        "Title: 'Who owns which decision'. Center: a blank referral sheet icon. Four rounded cards with arrows: teal 'Physical therapist — movement, exercise, aids'; green 'Occupational therapist — daily tasks, routines, home'; navy 'Dialysis nurse — session, access, machine'; purple 'Nephrologist — prescription, fluid removal, medicines'. A red stop badge on the nurse and nephrologist cards: 'Route, never change'. Bottom strip: 'Read the referral, then route each request to its owner.'"),
    "otpt02_cascade": ("M02", "frailty", "A", "1024 × 1536", "Understand", "clinicians",
        "Title: 'From kidney failure to function'. Top node: a kidney icon 'Kidney failure'. Five branches downward, each mechanism to a bedside sign: 'Acidosis, inflammation → muscle breakdown → slow chair rise'; 'Low erythropoietin → anemia → breathless walking'; 'Fluid removal, weak reflexes → pressure drop → dizzy on standing'; 'Uremia, diabetes → neuropathy → unsteady turns'; 'Mineral and bone disorder → fragile bone → fractures'. All five converge at the bottom on an amber node 'Frailty: low reserve'."),
    "otpt02_muscle": ("M02", "muscle", "D", "1792 × 1024", "Understand", "clinicians",
        "Title: 'Why muscle shrinks in kidney failure'. Center: a semi-photorealistic cross-section of a thigh muscle bundle; left fiber labeled 'Healthy fiber', right smaller fiber labeled 'Fiber in kidney failure'. A balance scale above: left pan 'Building' (protein, exercise, insulin signal) and right pan 'Breakdown' (acidosis, inflammation, insulin resistance, inactivity) tipped toward breakdown. A green arrow: 'Exercise + adequate protein push back'. Bottom strip: 'Leg muscles fail first: test the legs, not just the grip.'"),
    "otpt03_orthostasis": ("M03", "why pressure falls", "D", "1792 × 1024", "Understand", "clinicians",
        "Title: 'Standing up after dialysis'. Center: a patient rising from a reclining dialysis chair (no anatomy visible through skin). Three teal callouts: 'Less plasma after fluid removal', 'Slow vessel reflex (neuropathy)', 'Heart rate blunted (beta-blocker)'. A small inset line graph (≤12% of the panel, labeled 'not to scale') of blood pressure falling on standing. A red badge: 'A normal pulse does not clear a bad symptom'."),
    "otpt03_decision": ("M03", "big picture", "C", "1792 × 1024", "Apply", "clinicians",
        "Title: 'Proceed, adapt, defer, stop'. Four horizontal cards with color bands: green 'Proceed — no new symptoms, within the unit sheet'; amber 'Adapt — stable but near a limit: shorter, seated, more help'; orange 'Defer — acute change or outside the sheet: tell the nurse, rebook'; red 'Stop — red flag: stop, call, stay, SBAR'. Small grey note under the cards: 'Limits come from the physician and the unit sheet.'"),
    "otpt04_fistula": ("M04", "big picture", "B", "1792 × 1024", "Apply", "mixed",
        "Title: 'Protect the fistula arm'. Left panel (green, 'Do'): an uncovered forearm with a radiocephalic fistula, a small buzz symbol over the vein, the arm resting free; checkmarks 'Visible', 'Free', 'Other arm for pressure'. Right panel (red, 'Never'): four small crossed-out icons on the same arm: 'cuff', 'tight sleeve', 'strapped weight', 'sleeping on it'. Bottom strip: 'Pressure slows flow, and slow flow clots.' " + A_TRUTH_FISTULA),
    "otpt04_hand_exercise": ("M04", "exercise evidence", "C", "1792 × 1024", "Apply", "mixed",
        "Title: 'Hand and forearm exercise before fistula surgery'. Three step cards: '1 Squeeze — soft ball, 5-second holds'; '2 Band — light wrist curls'; '3 Repeat — most days, 6 to 8 weeks, surgeon approved'. A fourth card with a simple ultrasound-style grayscale circle growing from smaller to larger, labeled 'Vein widened (surrogate)'. Amber footnote: 'In one trial vein size grew; early failure did not change.' " + A_TRUTH_FISTULA),
    "otpt05_battery": ("M05", "big picture", "C", "1792 × 1024", "Apply", "clinicians",
        "Title: 'A practical baseline battery'. Four cards with small line illustrations of a Filipino patient: '4-meter walk — gait speed'; 'Five chair rises — leg strength'; 'Balance stands — side-by-side, semi-tandem, tandem'; 'Six-minute walk — endurance'. Each card has a stopwatch icon. Bottom strip: 'Same chair, same course, same words, same dialysis day.'"),
    "otpt05_gait_speed": ("M05", "numbers", "E", "1536 × 1152", "Understand", "clinicians",
        "Title: 'Gait speed as a vital sign'. A horizontal ruler from 0.4 to 1.4 m/s with three bands: red 'below 0.6', amber '0.6 to 1.0', green 'above 1.0', each with a small walking-figure icon (walker, cane, independent). A marker at 0.68 m/s labeled 'Mr. V. (example)'. Footer: 'Each 0.1 m/s slower was associated with higher mortality in CKD (observational).' Do not present the bands as clinical cutoffs; label them 'illustrative bands'."),
    "otpt06_energy": ("M06", "big picture", "E", "1536 × 1152", "Apply", "mixed",
        "Title: 'An energy budget for a dialysis week'. A Monday-to-Sunday calendar grid; Monday, Wednesday and Friday mornings shaded navy 'Dialysis'; a small battery icon on each day dipping after dialysis and full on non-dialysis days. Colored blocks: green 'Valued activity' placed on Thursday evening, amber 'Chores' spread across Tuesday and Saturday, teal 'Planned rest' after each session. Footer: 'Put what matters most where the battery is fullest.'"),
    "otpt07_routine": ("M07", "observe", "D", "1792 × 1024", "Apply", "mixed",
        "Title: 'Routines that survive a tired day'. A bright kitchen counter: a weekly pill organizer with day-and-time compartments (no readable drug names), a single marked water bottle with a fill line labeled 'today', a large-print picture checklist on the refrigerator (icons only), a phone showing a bell icon. A caregiver and an older patient doing teach-back (speech bubbles with icons only). Callouts: 'Visible cue', 'One bottle', 'Tick sheet', 'Teach-back'."),
    "otpt08_falls": ("M08", "big picture", "D", "1792 × 1024", "Understand", "mixed",
        "Title: 'Why people fall after dialysis'. Center: an older patient with a cane walking out of a dialysis unit door. Six small cards around: 'Pressure drop after fluid removal', 'Numb feet', 'Poor vision', 'Sedating medicines', 'Weak legs', 'Wet floor'. A highlighted hip icon in red: 'Fragile bone: hip fracture risk about 4 times higher'. Bottom strip: 'Remove one block from the stack.'"),
    "otpt08_transfer": ("M08", "transfer", "C", "1792 × 1024", "Apply", "mixed",
        "Title: 'An access-safe sit-to-stand'. Five step cards: '1 Prepare — brakes on, arm free'; '2 Pause — sit a minute, ask about dizziness'; '3 Position — scoot forward, feet back'; '4 Rise — nose over toes, guard with a gait belt'; '5 Settle — stand still, then walk'. The therapist always holds the gait belt, never the fistula arm; the arm is uncovered."),
    "otpt09_fitt": ("M09", "prescription", "E", "1024 × 1024", "Apply", "clinicians",
        "Title: 'The exercise prescription on one card'. Six rows: 'Frequency — most days', 'Intensity — RPE 12 to 14, talk test', 'Time — start where they are', 'Type — walk, cycle, bands, sit-to-stand', 'Volume — toward 150 min/week as tolerated', 'Progression — time first, reps before load'. A small Borg scale strip 6 to 20 with 12–14 highlighted in teal. Footer: 'Effort, not heart rate, on beta-blockers.'"),
    "otpt09_adaptation": ("M09", "big picture", "C", "1792 × 1024", "Understand", "clinicians",
        "Title: 'What training changes, and when'. A 12-week timeline: weeks 1–4 card 'Nervous system learns to recruit fibers'; weeks 4–8 'Muscle fibers start to grow'; weeks 8–12 'More capillaries and mitochondria: endurance rises'. Small icons for neurons, muscle fiber and capillary. Amber note: 'Stop for 1 to 2 weeks and early gains fade first.'"),
    "otpt10_chairside": ("M10", "setup", "D", "1792 × 1024", "Apply", "mixed",
        "Title: 'Exercise in the chair, early in the session'. Center: a patient on a reclining dialysis chair with a bed cycle at the foot; the fistula arm still on the armrest, needles taped, lines routed away from the pedals; a nurse at the machine; a therapist coaching. Callouts: 'First half of session', 'Legs do the work', 'Arm still and visible', 'Nurse controls the machine', 'Stop for any symptom or alarm'. A clock icon showing the first half shaded."),
    "otpt10_trials": ("M10", "why they differ", "B", "1792 × 1024", "Understand", "clinicians",
        "Title: 'Why two trials disagreed'. Left panel green 'DiaTT (Germany)': '12 months', 'endurance + resistance', 'supervised', result 'STS60 +3.85 vs usual care'. Right panel amber 'PEDAL (UK)': '6 months', 'cycling only', 'adherence 18%', result 'no quality-of-life gain'. Bottom strip: 'Neither trial showed longer survival.'"),
    "otpt11_pd": ("M11", "pressure", "D", "1792 × 1024", "Understand", "mixed",
        "Title: 'Pressure in a full abdomen'. Side-view schematic of an adult abdomen filled with light blue dialysis fluid, a PD catheter exiting the lower abdominal wall with the exit site pointing downward, arrows pressing outward on the abdominal wall during lifting, with weak points marked (navel, groin, catheter tunnel). Two small cards: red 'Sit-ups, straining, breath-holding', green 'Exhale on effort, load close, gentle core'. Anatomical truth: the Tenckhoff catheter tip lies deep in the pelvis (rectouterine or rectovesical pouch), deep cuff preperitoneal, superficial cuff near the exit; the catheter is not in the bladder or bowel. Show anatomy only as a clean schematic panel, never through the skin of a photographed person."),
    "otpt12_icu": ("M12", "mobilize", "A", "1024 × 1536", "Apply", "clinicians",
        "Title: 'The early mobility ladder'. Six rungs from bottom to top: '1 Range of motion in bed', '2 Active bed exercises', '3 Sit at the edge', '4 Stand with help', '5 Chair transfer, march in place', '6 Walk with lines managed'. Beside the ladder: a small icon of a continuous kidney replacement machine with a navy note 'Nurse controls the circuit'. A red side bar: 'Stop for arrhythmia, falling pressure or saturation, bleeding, catheter movement'."),
    "otpt13_prehab": ("M13", "big picture", "C", "1792 × 1024", "Apply", "mixed",
        "Title: 'From waiting list to recovery'. A horizontal timeline: 'Waiting — prehabilitation habit' (strength, walking, breathing icons); 'Surgery'; 'Weeks after — protect the wound: surgeon's lifting limit' (a crossed-out heavy box); 'Months after — graded return to work and sport'. Amber note: 'Fitness helps recovery; it does not decide who gets a kidney.'"),
    "otpt14_frailty": ("M14", "big picture", "D", "1792 × 1024", "Understand", "clinicians",
        "Title: 'When problems stack up'. Center: an older seated man with a below-knee prosthesis (outside view, no anatomy through skin). Four stacked translucent layers behind him labeled 'Frailty', 'Fragile bone', 'Numb feet', 'Limb loss', each with a green action tag: 'Slower pace', 'No loaded bending', 'Daily foot check', 'Sock management'. Bottom strip: 'Treat the person, not the list.'"),
    "otpt15_home": ("M15", "solutions", "D", "1792 × 1024", "Apply", "mixed",
        "Title: 'Home changes that cost little'. A cutaway of a small Filipino home: three entrance steps with a rail and bright edge tape; a bathroom with a plastic shower chair, a nonslip mat and a commode chair over a squat toilet; a night light on the path to the bedroom. Green tags: 'Rail', 'Edge tape', 'Shower chair', 'Commode', 'Night light'. Amber note: 'Plan for the worst day of the dialysis week.'"),
    "otpt16_work": ("M16", "work", "E", "1536 × 1152", "Apply", "mixed",
        "Title: 'Work around dialysis'. A Monday-to-Saturday grid: dialysis mornings shaded navy on Monday, Wednesday, Friday; full work shifts in green on Tuesday, Thursday, Saturday; light tasks in amber on dialysis afternoons; a no-ladder icon on dialysis afternoons; a fistula-arm shield icon. Footer: 'Change when you work, not whether.'"),
    "otpt17_remote": ("M17", "remote", "C", "1792 × 1024", "Apply", "clinicians",
        "Title: 'Safe remote rehabilitation'. Four step cards: '1 In-person baseline and screen'; '2 Video session — family member guards balance work'; '3 Stop rule — red flags go to local emergency care'; '4 Next in-person review'. Small icons: clinic, phone with video, red stop sign, calendar."),
    "otpt18_authority": ("M18", "big picture", "E", "1536 × 1152", "Understand", "clinicians",
        "Title: 'Who decides what'. A 4-row table: 'PRC — who may practice (RA 5680 for PT, RA 11241 for OT)'; 'DOH — whether a facility is licensed'; 'PhilHealth — what is paid, through which contracted facility'; 'Academy — only that you studied'. A red footer badge: 'Never let one stamp stand in for another.' No agency logos or seals."),
    "otpt19_runchart": ("M19", "big picture", "D", "1792 × 1024", "Apply", "clinicians",
        "Title: 'Measure for improvement'. A clean run chart: x-axis 'Month', y-axis 'Median STS60'; three baseline points around a horizontal teal median line labeled 'baseline median'; an annotation 'Program starts'; six following points above the median shaded green with a bracket 'Shift: 6 points above'. A small gray balancing-measure line below: 'Stops for dizziness per 100 sessions'. Illustrative data only."),
    "otpt20_shared_plan": ("M20", "plan", "E", "1536 × 1152", "Apply", "clinicians",
        "Title: 'One goal, two leads'. Top banner: 'Goal: walk to the pier and sit with friends'. Two columns: teal 'PT leads — strength, walking, balance, walker'; green 'OT leads — energy budget, seated bathing, foot checks, rest stop'. A red row along the bottom: 'Safety first: near fall → nurse; heel blister → same-day review; low mood → physician'."),
}

TYPE_NAME = {"A": "Scaffold A — Algorithm / ladder (portrait)", "B": "Scaffold B — Side-by-side comparison", "C": "Scaffold C — Step sequence",
             "D": "Scaffold D — One-panel poster", "E": "Scaffold E — Reference card"}
NEG_HERO = ("Avoid: busy layouts, collage overload, more than four supporting scenes, dozens of icons, tiny unreadable labels, infographic clutter, "
            "duplicated people, repeated compositions, cropped circle, cropped objects, cropped anatomy, edge clipping, objects touching the circular "
            "border, important content inside the title safe zone, baked-in text, titles, captions, logos, watermarks, rectangular borders, frames, "
            "banners, dark / charcoal / black backgrounds, cartoon style, neon, HDR, over-saturation, distorted hands or faces, implausible anatomy. "
            "Never show a blood pressure cuff, band, strap, watch or weight on a fistula arm, a therapist touching a dialysis machine, needle, line or "
            "catheter, or a patient lifted by one person.")
NEG_FIG = ("Avoid cartoon style, clutter, tiny unreadable labels, AI gibberish text, unrealistic anatomy, overprocessed HDR, excessive saturation. "
           "NEVER use dark, navy, charcoal or black backgrounds — light backgrounds only. Use ONLY Inter (sans-serif) — no other fonts, no serif. "
           "No brand names, logos, agency seals, real names or readable patient data. Never show compression of a fistula arm, a therapist handling a "
           "dialysis machine, needle, line or catheter, or universal exercise-clearance numbers. Never omit the renalcarematters.com attribution, "
           "and render it exactly as lowercase renalcarematters.com (no www, no https://).")


def hero_block(key):
    arch, cam, people, scene, sc = HEROES[key]
    if key == "hub":
        fname, title, brief = f"{HUB}-vignette-hero.png", "Course home (also reused by the final exam and trainer pages)", C.COURSE["hero_alt"]
    else:
        m = MODS[key]
        fname, title, brief = f"{HUB}-{key}-{m['slug']}-vignette-hero.png", f"Module {int(key)} · {m['title']}", m["sub"]
    stype = {"A": "Scaffold A people", "B": "Scaffold B still-life"}[sc]
    if sc == "A":
        body = (f"Square 1:1 photorealistic editorial photograph on a 2048×2048 canvas, composed to be displayed inside a CIRCULAR vignette "
                f"occupying 85–90% of the canvas diameter with a visible WHITE BORDER around the full circle (the circle never touches the canvas "
                f"edges). Composition archetype: {arch}. Camera: {cam}.\nPeople: {people}; Filipino, with features, ages, hairstyles, clothing and "
                f"posture clearly different from other Academy heroes.\nScene: {scene}. Clean, bright modern Philippine hospital, rehabilitation or home "
                f"setting, soft natural daylight, gentle shallow depth of field.")
    else:
        body = (f"Square 1:1 photorealistic still-life on a 2048×2048 canvas, composed to be displayed inside a CIRCULAR vignette occupying 85–90% "
                f"of the canvas diameter with a visible WHITE BORDER around the full circle. Composition archetype: {arch}. Camera: {cam}.\n"
                f"Subject: {people}. Scene: {scene}. Soft, uncluttered light surface, gentle daylight, shallow depth of field.")
    body += ("\nVisual hierarchy: hero subject 60–70% of the circle; 2–4 supporting elements 20–30%; reserve a 20–25% TITLE SAFE ZONE of soft "
             "gradient, clean wall or blurred background on the left side of the circle (no faces, anatomy, icons, objects or callouts inside it).\n"
             "Calm, reassuring, documentary-realistic color grade harmonizing with clinical teal #1a6b72 and navy #0f1e2e on a light background; "
             "soft falloff toward the rim. Full-bleed within the inscribed circle, no rectangular borders, frames or banners.\n"
             "Absolutely NO text of any kind: no title, caption, label, readable writing on paper or screens, logo, or watermark.")
    return f"""### {title}

Teaching purpose: Appreciate. {brief}

```
FILE NAME: {fname}
IMAGE TYPE: Circular vignette hero v3 — {stype}
ASPECT RATIO: 1:1 (square — displayed inside an 85–90% inscribed circle with white margin)
PIXEL DIMENSIONS: 2048 × 2048
COMPOSITION ARCHETYPE: {arch}
CAMERA: {cam}
HUMAN VARIATION (vs. previous guide): {"new cast; at least 12 traits differ (age, sex, face shape, hairstyle, hair length and color, build, skin tone within Filipino diversity, clothing style and color, accessories, posture, hand position, expression, setting)" if sc == "A" else "hands only or no people"}
AUDIENCE: licensed occupational and physical therapists (and their preceptors); plain-language readable for patients
VISUAL GOAL: One calm, dignified image that says what this page is about at a glance and shows rehabilitation as safe, skilled teamwork inside the renal plan.

PROMPT:
{body}

NEGATIVE INSTRUCTIONS:
{NEG_HERO}

QUALITY CHECK:
Square 2048×2048; circle 85–90% with a visible white margin, never cropped; one dominant subject; 20–25% empty title-safe zone; Filipino context; any fistula arm uncovered and unloaded; no text anywhere; crops cleanly inside the circle.
```
"""


def fig_block(key, idx):
    mod, sec, sc, size, purpose, aud, content = FIGS[key]
    fname, alt, cap = F.FIGS[key]
    png = fname.replace(".webp", ".png")
    ratio = {"1792 × 1024": "16:9 landscape", "1024 × 1536": "2:3 portrait", "1536 × 1152": "4:3", "1024 × 1024": "1:1"}[size]
    attrib_pos = "bottom-center" if "portrait" in ratio else "bottom-right"
    anatomy = ("fistula" in content.lower()) or ("abdomen" in content.lower()) or ("muscle" in content.lower())
    qa = ["□ Light (white or #fafafa) background — confirmed", "□ Every label spelled exactly as written, American English, Inter font — confirmed",
          "□ One concept; labels four to eight words — confirmed", "□ No readable brand, real name or patient data — confirmed",
          f"□ Attribution renalcarematters.com present at the {attrib_pos}, small, navy, 70% opacity, exact lowercase string — confirmed",
          "□ Attribution does not overlap content — confirmed", "□ No prompt text or metadata visible — confirmed"]
    if anatomy:
        qa += ["□ Anatomy plausible; no anatomy shown through the skin of a photographed person — confirmed",
               "□ Any fistula arm uncovered, unloaded and free of cuffs or straps — confirmed"]
    qa = "\n".join(qa)
    return f"""### OTPT-F{idx:02d} · {key}

Placement: {mod} · section `{sec}` · Teaching purpose: **{purpose}** · Caption on page: {cap}

```
FILE NAME: {png}   (convert to {fname} for the site)
IMAGE TYPE: {TYPE_NAME[sc]}
ASPECT RATIO: {ratio}
PIXEL DIMENSIONS: {size}
AUDIENCE: {aud}
VISUAL GOAL: {cap}

PROMPT:
Clean clinical education figure in the renalcarematters.com house style, AJKD/NEJM graphical-abstract aesthetic, semi-photorealistic illustration (not flat vector clip art, not cartoon). White (#ffffff) background with soft gray (#f3f4f6) or light teal (#eef6f7) cards. Typography: Inter only; bold navy (#0f1e2e) title, teal (#1a6b72) subheadings; renal green (#1f7a4d) for safe or positive, amber (#b8860b) for caution, clinical red (#b91c1c) for stop; soft purple (#6c3d8e) for physician-owned decisions. Filipino people where people appear. Generous whitespace, mobile-readable labels (minimum 11 pt equivalent).
CONTENT: {content}
Alt-text intent (for checking): {alt}
Attribution: "renalcarematters.com" in small semi-transparent navy text (70% opacity, about 10–11 px) at the {attrib_pos}, exactly lowercase, clear of all content.

NEGATIVE INSTRUCTIONS:
{NEG_FIG}

QUALITY CHECK (Constitution-style QA):
{qa}
```
"""


def tile_block(name, fname, size, scene):
    return f"""### {name}

```
FILE NAME: {fname}
IMAGE TYPE: Track or module tile (illustrated scene, no text)
ASPECT RATIO: 16:9 landscape
PIXEL DIMENSIONS: {size}
PROMPT:
Semi-photorealistic illustrated editorial scene in the renalcarematters.com house style (GPT-rendered, not flat vector). Bright, airy, light background, soft natural daylight, gentle depth of field, colors harmonizing with teal #1a6b72, navy #0f1e2e and renal green #1f7a4d. Subject centered with 15% safe margin on all sides so the image crops cleanly to a card thumbnail. {scene} Filipino people and Philippine setting. No text, no letters, no numbers, no logos, no watermark (the site places titles in HTML).
NEGATIVE: dark backgrounds, clutter, collage, readable text, cuffs or straps on a fistula arm, a therapist touching a dialysis machine or lines, cartoon style, HDR, distorted hands or faces.
QUALITY CHECK: reads as one idea at thumbnail size (320 px wide); no text anywhere; light background; subject inside the safe margin.
```
"""


def main(out):
    L = []
    L.append(f"""# Occupational and Physical Therapist Track · Image Plan Blueprint and GPT Prompt Pack

Renal Care Academy → Ancillary Staff Track → Occupational and Physical Therapist (`academy/{HUB}.html`). Prepared November 25, 2026 from blueprint v2 (`OT-PT-BLUEPRINT-v2.md`). Generated by `tools/techcourses/otpt/build_image_prompts.py`; edit the plan there, not here.

## 1. Aim

Every image must help a therapist do one of three things better:

- **Understand** a mechanism they can redraw from memory: the capacity–demand gap, why muscle shrinks in uremia, why pressure falls on standing after dialysis, why a fistula clots under pressure, why a full abdomen strains the wall, why two exercise trials disagreed.
- **Apply** a decision or technique: proceed/adapt/defer/stop, an access-safe transfer, a baseline battery, an exercise prescription card, an energy budget, a home plan, a run chart.
- **Appreciate** why the work matters: heroes that show rehabilitation as skilled, safe teamwork with Filipino patients and families, and tiles that make each module recognizable.

## 2. Guardrails carried into every prompt

- **Light backgrounds only**, Inter typeface, American English, short labels, mobile-readable.
- **Attribution `renalcarematters.com`** on every figure, tile-free heroes excepted (heroes carry no text by design; the vignette is masked by CSS). This is the public Academy set, so the renalcarematters.com attribution applies, not williamriveromd.com.
- **Safety in the picture:** a fistula arm is always uncovered and unloaded; therapists never touch a dialysis machine, needle, line or catheter; nobody lifts a patient alone; no universal exercise-clearance numbers appear (the handoff forbids inventing them; the unit sheet holds them).
- **Evidence honesty:** surrogate outcomes are labeled as surrogates (vein size, heart mass); observational associations say "associated with"; bands on rulers are labeled illustrative.
- **People:** Filipino cast, every hero a new cast (at least 12 visible traits differ), composition archetypes and camera angles rotated across the 21 heroes. No real names, brands, logos or readable patient data.
- **Anatomy:** where a fistula, PD catheter or muscle appears, Constitution v1.0 anatomical-truth notes are embedded (radiocephalic anatomy; Tenckhoff tip deep in the pelvic pouch with downward exit; no anatomy through photographed skin).

## 3. Inventory

| Set | Count | Size | Where it lands |
|---|---|---|---|
| Circular-vignette heroes | 21 (hub + 20 modules; exam and trainer reuse the hub hero) | 2048 × 2048 | `images/{HUB}[-NN-slug]-vignette-hero.webp` |
| Teaching figures | {len(FIGS)} | 1792 × 1024, 1024 × 1536, 1536 × 1152, 1024 × 1024 | `images/{HUB}-NN-*.webp` (placed automatically once the file exists) |
| Tiles | 22 (landing tile, course-home card, 20 module cards) | 1536 × 864 (export 960 × 540 / 640 × 360) | `images/academy/landing/{HUB}.webp`, `images/{HUB}-card.webp`, `images/{HUB}-NN-card.webp` |
| OG share cards | 4 (track card art + toolkit, exam, trainer cards) | 1536 × 1024 art / 1200 × 630 cards | `images/og/academy/…`, `images/og/renal-rehabilitation-toolkit.jpg` |

Teaching purpose of the figures: Understand {sum(1 for v in FIGS.values() if v[4] == 'Understand')}, Apply {sum(1 for v in FIGS.values() if v[4] == 'Apply')}; heroes and tiles carry Appreciate.

## 4. Figure map

| ID | Placement | Type | Purpose | What it teaches | File |
|---|---|---|---|---|---|""")
    for i, k in enumerate(FIGS, 0):
        mod, sec, sc, size, pur, aud, content = FIGS[k]
        L.append(f"| OTPT-F{i:02d} | {mod} · `{sec}` | {TYPE_NAME[sc].split('— ')[1]} | {pur} | {F.FIGS[k][2]} | `{F.FIGS[k][0].replace('.webp', '.png')}` |")
    L.append(f"""
## 5. Production workflow

1. Generate each image in the ChatGPT Image Generator from the blocks below (copy the fenced block whole). Save the PNG under its FILE NAME.
2. Drop the files in `/Volumes/Storage/Renal Care Academy/OT-PT/images/` (corrected regenerations in `images/Corrected/`). Claude audits each image against its QUALITY CHECK, converts to WebP, places heroes, figures and tiles in the repo `images/` folder, and writes a new MD prompt file for any image that fails audit.
3. Figures appear on the pages automatically on the next `python3 generate_tech_courses.py --course otpt --patch` (then `python3 tools/techcourses/otpt/expand_acronyms.py`).
4. OG: put the track art (`{HUB}.png`) in `images/academy/og-art/`, then `python3 build_academy_og.py --art images/academy/og-art --only {HUB} --patch`; the script sets every word on the card. The toolkit, exam and trainer cards are complete 1200 × 630 images with text.
5. After tiles land: `python3 generate_rg_thumbs.py` and `python3 patch_rg_card_thumbs.py`.

---

## Part 1 · Heroes (21)
""")
    L.append(hero_block("hub"))
    for k in sorted(MODS):
        L.append(hero_block(k))
    L.append("\n---\n\n## Part 2 · Teaching figures\n")
    for i, k in enumerate(FIGS, 0):
        L.append(fig_block(k, i))
    L.append("\n---\n\n## Part 3 · Tiles (no text; the site sets titles in HTML)\n")
    L.append(tile_block("Academy landing tile", f"academy-landing-{HUB}.png → images/academy/landing/{HUB}.webp (960 × 540)", "1536 × 864",
                        "A physical therapist and an occupational therapist with an older patient in a bright rehabilitation corner beside a dialysis unit: the patient rises from a chair with a gait belt while the OT sets a simple household task on a table; a pedal cycle and a walker nearby."))
    L.append(tile_block("Course-home card", f"{HUB}-card.png → images/{HUB}-card.webp", "1536 × 864",
                        "A close, warm scene of a therapist's hands steadying an older patient's hands on a walker, a dialysis chair softly blurred behind."))
    for k in sorted(MODS):
        m = MODS[k]
        L.append(tile_block(f"Module {int(k)} card · {m['title']}", f"{HUB}-{k}-card.png → images/{HUB}-{k}-card.webp (640 × 360)", "1536 × 864",
                            m["hero_brief"].split("no legible names or numbers in image. ")[-1] + " Wider framing than the module hero, different camera angle and a different cast."))
    L.append("\n---\n\n## Part 4 · OG share cards\n")
    L.append(f"""### Track share card art (text added by build_academy_og.py)

```
FILE NAME: {HUB}.png  (save to images/academy/og-art/)
IMAGE TYPE: OG card art, text-free (build_academy_og.py crops to 1200 × 630 and sets the title, track label and stats)
ASPECT RATIO: 3:2
PIXEL DIMENSIONS: 1536 × 1024
PROMPT:
Semi-photorealistic editorial illustration, bright and airy, light background. Keep the LEFT 42% of the canvas a quiet, soft off-white to light-teal gradient field with no objects (the script places text there). In the RIGHT 58%: a Filipino physical therapist guarding an older man as he rises from a reclining dialysis chair with a gait belt (his fistula forearm uncovered and free), and a Filipina occupational therapist at a low table setting out a simple kitchen task; a pedal cycle at the chair's foot; dialysis machines softly blurred. Soft daylight, teal #1a6b72 and renal green #2E6B3E accents. No text, letters, numbers, logos or watermark anywhere.
NEGATIVE: dark backgrounds, clutter, any text, objects in the left 42%, cuffs or straps on the fistula arm, therapists touching machines or lines.
QUALITY CHECK: left 42% empty and light; subject fully inside the right side; no text.
```

### Toolkit share card

```
FILE NAME: renal-rehabilitation-toolkit-og.png → images/og/renal-rehabilitation-toolkit.jpg
IMAGE TYPE: OG / social share card with text
ASPECT RATIO: 1.91:1
PIXEL DIMENSIONS: 1200 × 630
PROMPT:
Clean social share card, white (#ffffff) background, Inter font only. Left half: small teal (#1a6b72) eyebrow "RENAL CARE ACADEMY · OT AND PT", large bold navy (#0f1e2e) title in two lines "Renal Rehabilitation Toolkit", a teal subtitle "6 measurement tools for kidney care", and a row of three small rounded chips "6-minute walk" · "SPPB" · "Sit-to-stand". Right half: a semi-photorealistic illustration of a stopwatch, a strip of colored floor tape marking a 4-meter course and a firm chair, on a light teal (#eef6f7) rounded panel. Bottom-right: "renalcarematters.com" small, navy, 70% opacity.
NEGATIVE: dark backgrounds, misspelled words, extra text, logos, people's faces, clutter, serif fonts.
QUALITY CHECK: exactly 1200 × 630; every word spelled as given; attribution present; readable at 600 px wide.
```

### Final exam share card

```
FILE NAME: {HUB}-final-exam-og.png → images/og/academy/{HUB}-final-exam.jpg
IMAGE TYPE: OG / social share card with text
ASPECT RATIO: 1.91:1
PIXEL DIMENSIONS: 1200 × 630
PROMPT:
Clean social share card, white background, Inter font only. Left: green (#2E6B3E) eyebrow "ANCILLARY STAFF TRACK", bold navy title "Occupational and Physical Therapist", teal subtitle "End-of-course examination · 20 questions · pass 16". Right: a semi-photorealistic illustration of a phone showing a multiple-choice card with four blank answer bars (no readable text) beside a stopwatch and a gait belt on a light teal panel. Bottom-right: "renalcarematters.com" small, navy, 70% opacity.
NEGATIVE: dark backgrounds, misspellings, extra text, logos, clutter.
QUALITY CHECK: exactly 1200 × 630; words spelled exactly; attribution present.
```

### Trainer page share card

```
FILE NAME: {HUB}-trainer-og.png → images/og/academy/{HUB}-trainer.jpg
IMAGE TYPE: OG / social share card with text
ASPECT RATIO: 1.91:1
PIXEL DIMENSIONS: 1200 × 630
PROMPT:
Clean social share card, white background, Inter font only. Left: green (#2E6B3E) eyebrow "ANCILLARY STAFF TRACK", bold navy title "Trainer and Preceptor Resource", teal subtitle "Occupational and Physical Therapist · 8 practical stations · 10 templates". Right: a semi-photorealistic illustration of a clipboard with a blank scoring grid (no readable text), a pen and a gait belt on a light teal panel. Bottom-right: "renalcarematters.com" small, navy, 70% opacity.
NEGATIVE: dark backgrounds, misspellings, extra text, logos, clutter.
QUALITY CHECK: exactly 1200 × 630; words spelled exactly; attribution present.
```
""")
    import html as _h
    Path(out).write_text(_h.unescape("\n".join(L)), encoding="utf-8")
    print("wrote", out)


if __name__ == "__main__":
    main(sys.argv[1] if len(sys.argv) > 1 else "OT-PT-IMAGE-PLAN-AND-PROMPTS.md")
