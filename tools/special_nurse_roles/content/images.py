# -*- coding: utf-8 -*-
"""Image plan for the Special Dialysis Nurse Roles subtrack (Renal Care Academy, Nephrology Nursing, By Role).

HEROES: one circular-vignette hero per page (williamriveromd-hero-vignette v3), 15 in all (hub + 14 modules;
the end-of-course check reuses the hub hero).
FIGURES: in-body teaching figures. Scaffolds A (clinical algorithm, williamriveromd-algorithm-generator-skill),
B-E (williamriveromd-simple-figure), M (williamriveromd-biomedical-mechanism-figure layout, semi-photorealistic),
P (williamriveromd-infographic-skill procedural photo strip). A figure is placed at the end of its section only once
images/<stem>.webp (or .png) exists, so the pages never show a broken image.
Each figure records its teaching purpose: Understand (the mechanism), Apply (the action), Appreciate (why it matters).
tools/special_nurse_roles/build_image_prompts.py turns this file into docs/special-dialysis-nurse-roles/.
"""

P = "special-dialysis-nurse-roles"
HUB_ALT = "A Filipino dialysis nurse leading a short huddle with three colleagues beside a whiteboard of unit portfolio assignments."

# key: (file stem, archetype, camera, people, scene)
HEROES = {
    "hub": (f"{P}-vignette-hero", "J Environmental Storytelling", "wide-angle eye-level",
            "a Filipina nurse in her early 40s with a short layered bob and rimless glasses in navy scrubs, leading three colleagues: a tall Filipino nurse in his late 20s with a fade haircut in teal scrubs, a petite Filipina nurse in her 30s with a long braid in maroon scrubs, and a heavyset Filipino nurse in his 50s with gray temples in light-blue scrubs",
            "a morning huddle beside a whiteboard covered in colored sticky notes and simple icons (no readable words) at the nurses' station of a bright Philippine hemodialysis unit; dialysis chairs and machines in soft focus behind"),
    "01": (f"{P}-01-foundations-and-role-charter-vignette-hero", "H Clinical", "eye-level over-the-shoulder",
           "a Filipina head nurse in her late 50s with silver-streaked hair in a low bun and a cardigan over a white uniform, and a Filipina staff nurse in her late 20s with a pixie cut and wine-red scrubs",
           "they sit across a small desk reviewing a single printed page together; the younger nurse points to a section with a pen; a corkboard with a weekly roster grid (no readable text) behind them"),
    "02": (f"{P}-02-vascular-access-vignette-hero", "I Object Hero", "macro side view",
           "hands only",
           "a nurse's gloved fingertips resting lightly on a mature forearm arteriovenous fistula of a Filipino patient with a visible raised vein, a stethoscope diaphragm nearby on the armrest; soft clinical light"),
    "03": (f"{P}-03-infection-prevention-vignette-hero", "A Editorial Portrait", "three-quarter",
           "a lean Filipino nurse in his mid 30s with a neat side part and a thin mustache, in sky-blue scrubs, holding a clipboard against his chest",
           "he stands quietly at the edge of a dialysis station watching a colleague (out of focus) rub alcohol hand rub between her hands; a wall-mounted dispenser and a sharps container in the frame"),
    "04": (f"{P}-04-educator-and-preceptor-vignette-hero", "H Clinical", "eye-level close",
           "a Filipina preceptor in her late 40s with shoulder-length wavy hair and a lanyard, and a new Filipino nurse in his early 20s with curly hair in bright teal scrubs",
           "the new nurse practices a catheter connection on a training arm on a table while the preceptor watches his hands closely, one hand raised to pause him; a tray of sterile supplies"),
    "05": (f"{P}-05-patient-education-vignette-hero", "E Lifestyle", "eye-level seated",
           "a Filipina nurse in her early 30s with a high ponytail in lavender scrubs, an older Filipino man in his 60s with a weathered tanned face and a farmer's straw hat on his lap, and his daughter in her 30s with a ponytail and floral blouse",
           "they sit together at a dialysis chair; the nurse holds a bowl of soup and a small cup while the man explains with his hands; the daughter listens"),
    "06": (f"{P}-06-quality-improvement-audit-vignette-hero", "G Infographic", "straight-on",
           "a Filipino nurse in his early 40s with a crew cut and black-framed glasses in navy scrubs, pointing",
           "he points to a simple hand-drawn run chart on a whiteboard (a line with a dashed median, no readable numbers or words) while two colleagues look on from the side, out of focus"),
    "07": (f"{P}-07-safety-and-emergency-preparedness-vignette-hero", "J Environmental Storytelling", "low angle",
           "a Filipina nurse in her mid 40s with short curly hair and a small penlight in her scrubs pocket, in dark-green scrubs, and a Filipina patient in her 70s with white hair",
           "during a power interruption in a dim dialysis unit, the nurse gently folds back a blanket to keep the patient's taped forearm needle site visible; machines glow on battery; emergency lights"),
    "08": (f"{P}-08-care-coordination-transitions-vignette-hero", "I Object Hero", "three-quarter overhead",
           "hands only",
           "a desk with a hospital discharge folder, a dialysis treatment chart and a clear plastic bag of medicine boxes side by side; a nurse's hand places a small colored tab between two pages (no readable text)"),
    "09": (f"{P}-09-anemia-and-medication-safety-vignette-hero", "F Anatomy", "macro",
           "no people",
           "semi-photorealistic 3D render: red blood cells flowing out of a cross-section of bone marrow, with a kidney in soft focus in the background releasing small glowing signal particles toward the marrow; muted reds and teals; no labels"),
    "10": (f"{P}-10-transplant-and-options-liaison-vignette-hero", "B Journey", "wide-angle",
           "a Filipino nurse in his late 30s with a goatee and maroon scrubs, and a Filipino couple in their late 40s: a slim man with a cane and a woman with a short bob and reading glasses",
           "they walk together along a bright hospital corridor toward a sunlit doorway at the far end, the nurse half a step behind, gesturing forward; soft focus"),
    "11": (f"{P}-11-records-registry-philhealth-vignette-hero", "I Object Hero", "close three-quarter",
           "hands only",
           "a nurse's hand holding a pen over a paper treatment record beside a laptop showing an abstract form layout (no readable text) and a closed folder with a padlock sticker; a single line on the paper is neatly struck through and initialed"),
    "12": (f"{P}-12-water-dialysate-equipment-liaison-vignette-hero", "D Panorama", "wide low angle",
           "a Filipina nurse in her early 30s with a low ponytail and wire glasses in teal scrubs, and a stocky Filipino technician in his 40s with a cap and gray work uniform",
           "they stand together in a clean water treatment room in front of reverse osmosis membranes and blue filter housings, looking at a clipboard; stainless steel pipes in soft focus"),
    "13": (f"{P}-13-adequacy-volume-outcomes-vignette-hero", "I Object Hero", "macro side",
           "hands only",
           "a gloved hand holding two blood tubes (no readable text) beside the arterial sampling port of a dialysis blood line, the machine's blood pump in the background; precise and calm"),
    "14": (f"{P}-14-capstone-vignette-hero", "C Radial", "top-down",
           "four Filipino nurses of different ages and builds (a man in his 20s, a woman in her 40s wearing a hijab, a man in his 50s, a woman in her 30s with short dyed hair), seen from above, each holding a different colored clipboard",
           "the four stand around a central dialysis station table viewed from above, their clipboards pointing inward like spokes, a single patient chart in the middle"),
}

_F = []


def fig(fid, mid, section, slug, scaffold, size, title, content, alt, desc, goal, why, abbrevs=()):
    _F.append({"id": fid, "mid": mid, "section": section, "stem": f"{P}-{mid}-{slug}", "scaffold": scaffold, "size": size,
               "title": title, "content": content, "alt": alt, "desc": desc, "goal": goal, "why": why,
               "abbrevs": [list(a) for a in abbrevs]})


L, W, S = "1536 × 1024", "1024 × 1536", "1024 × 1024"

# ── Module 1 ──
fig("SDNR01-F1", "01", "portfolios", "twelve-portfolios", "E", S, "Twelve portfolios, one unit",
    "A 4 × 3 grid of rounded cards, each with a simple line icon and a two-to-four word label: Vascular access (arm with fistula), Infection prevention (hands and droplet), Educator and preceptor (two people and a checklist), Patient education (speech bubble and cup), Quality and audit (run-chart line), Safety and emergencies (shield and lightning bolt), Care coordination (two arrows exchanging a folder), Anemia and medicines (red cell and vial), Transplant liaison (kidney and bridge), Records and PhilHealth (folder and padlock), Water and equipment (water drop and machine), Adequacy and volume (scale and blood tube). A thin teal band under the grid: 'Each portfolio looks across patients and across weeks.'",
    "Grid of twelve icons for the special dialysis nurse portfolios, from vascular access to adequacy and volume.",
    "The twelve special portfolios a hemodialysis nurse may hold, each answering a unit-level question.",
    "Understand", "Gives learners a single map of the subtrack and shows that each role is a slice of unit-wide work.")
fig("SDNR01-F2", "01", "authority", "levels-of-authority", "C", L, "Read the rule at its own level",
    "Five stacked horizontal steps from top to bottom, widest at top: 1 Law (RA 9173, RA 10173) navy; 2 License condition (DOH AO 2012-0001) teal; 3 Payer rule (PhilHealth circulars) amber; 4 Society guidance (PSN 2024) green; 5 Employer assignment (role charter) gray. At the right, a callout comparing two ratio statements side by side: 'DOH: no more than 1 nurse to 4 STATIONS' and 'PSN: 1 nurse to 4 PATIENTS, or 6 with a trained assistant', with STATIONS and PATIENTS highlighted and a small note 'Different denominators. Different authority.'",
    "Five levels of authority from law to employer assignment, with the DOH station ratio and PSN patient ratio shown side by side.",
    "Requirements carry different force: law, license condition, payer rule, society guidance and employer assignment. The DOH and PSN ratios use different denominators.",
    "Understand", "Prevents the most common misreading in Philippine units, merging the station-based and patient-based ratios.",
    (("DOH", "Department of Health"), ("PSN", "Philippine Society of Nephrology"), ("RA", "Republic Act"), ("AO", "Administrative Order")))
fig("SDNR01-F3", "01", "loops", "closed-loop", "C", L, "A closed loop has four parts",
    "Four rounded cards in a circular flow connected by bold arrows: 1 Send (navy: SBAR to a named person), 2 Acknowledge (teal: receiver repeats back), 3 Act (green: decision with owner and due date), 4 Close (amber, with a small star: outcome confirmed, documented, patient told). A small red broken-arrow icon between 3 and 4 labeled 'Most often missed'.",
    "Four-step closed-loop communication cycle: send, acknowledge, act, close, with close marked as the most often missed step.",
    "A message is not finished when it is sent; the loop closes only when the outcome is confirmed and documented.",
    "Apply", "Turns the module's single most important habit into a picture a nurse can recall at the station.",
    (("SBAR", "Situation, Background, Assessment, Recommendation"),))

# ── Module 2 ──
fig("SDNR02-F1", "02", "physiology", "fistula-stenosis-steal", "M", L, "Reading the river: normal, narrowed, stolen",
    "Three side-by-side semi-photorealistic panels of a forearm fistula. Panel 1 'Healthy': smooth wide vein, gentle flow arrows, a small hand icon with a soft vibration symbol labeled 'Soft continuous thrill'. Panel 2 'Outflow stenosis': dashed magnified inset of the narrowed vein segment beyond the needles with turbulent arrows and backed-up flow; callouts 'Hammering pulse', 'Stays full when arm raised', 'Bleeds longer'. Panel 3 'Steal': a large arrow of blood diverted into the fistula, the hand beyond pale and cool with a red warning outline; callouts 'Cold, pale, painful hand', 'Act now'. Bottom navy strip: 'Look, listen, feel every session. A change from the patient's baseline matters most.'",
    "Three panels comparing a healthy fistula, an outflow stenosis with backed-up flow, and steal with a pale, cold hand.",
    "A healthy fistula has a soft continuous thrill; outflow narrowing causes a hammering pulse and prolonged bleeding; steal starves the hand and needs action now.",
    "Understand", "Links what the nurse feels at the bedside to what is happening inside the vessel.")
fig("SDNR02-F2", "02", "urgency", "access-urgency-algorithm", "A", W, "Access finding: act now, today or this week?",
    "Top node 'Before cannulation: look, listen, feel (compare with access map)'. Decision diamond 'No thrill or bruit? Cold, pale, painful hand? Uncontrolled bleeding? Spreading redness with fever?' YES (red) → 'Do not cannulate. Pressure if bleeding. Physician now. Same-day surgical or interventional decision.' NO → diamond 'Hammering pulse, stays full on arm raise, prolonged bleeding 2+ sessions, high venous pressure, new arm swelling?' YES (amber) → 'SBAR to physician this shift. Referral written. Owner and date on tracker.' NO → diamond 'Harder cannulation over weeks, slow maturation, catheter without dated plan?' YES (teal) → 'Tracker and access meeting this week.' NO (green) → 'Cannulate per access map; record attempts.'",
    "Algorithm sorting vascular access findings into act now, today and this week, before any cannulation.",
    "Findings are sorted before cannulation: emergencies to the physician now, developing patterns the same shift, slow changes to the weekly tracker.",
    "Apply", "Gives a bedside decision path so that urgent access problems never wait for the next clinic.",
    (("SBAR", "Situation, Background, Assessment, Recommendation"),))
fig("SDNR02-F3", "02", "tracker", "referral-tracker", "C", L, "The access referral, from finding to closed",
    "Six cards in a row connected by arrows: 1 Finding (dated, tier), 2 Request (physician decision, written referral), 3 Receipt (receiving service confirms), 4 Procedure (date or reason not done), 5 Returned plan (chart and access map updated), 6 Closed (patient told; first cannulation supervised). Under cards 3 and 5, small red markers 'Where referrals stall'.",
    "Six-step access referral tracker from finding to closure, with the receipt and returned-plan steps marked as common stall points.",
    "An access referral is closed only when the plan has come back, been acted on, and the patient has been told.",
    "Apply", "Shows exactly where to look when a family asks what happened to a referral.")

# ── Module 3 ──
fig("SDNR03-F1", "03", "routes", "contamination-pathways", "M", L, "How germs and blood travel around a dialysis station",
    "Semi-photorealistic overhead view of two neighboring dialysis stations with chairs, machines and a shared cart between them. Colored dotted paths: red path from a gloved hand on station A's machine knob to station B's catheter hub (label 'Hands'); amber path of a supply tray moving between stations (label 'Shared items'); purple path from a multi-dose vial to two syringes (label 'Shared vials'); light-blue droplet cloud near a coughing patient (label 'Droplets'). Dashed magnified inset of a machine knob showing an almost invisible dried blood film with small virus particles, caption 'Hepatitis B can survive on dry surfaces for about a week'. Bottom navy strip: 'Nothing crosses between stations unless single-use or disinfected.'",
    "Two dialysis stations with colored paths showing hands, shared items, shared vials and droplets carrying germs between patients.",
    "Germs and bloodborne viruses travel between stations on hands, shared supplies, shared vials and surfaces; hepatitis B can survive on dry surfaces for days.",
    "Understand", "Makes invisible transmission routes visible so the nurse knows where barriers belong.")
fig("SDNR03-F2", "03", "observe", "observe-feedback-cycle", "C", L, "Observe a task, then fix the system",
    "Six cards in a loop with arrows: 1 Choose the riskiest task, 2 Use one checklist (clipboard icon), 3 Observe openly, all shifts, 4 Feed back at once (private to the person, data to the team), 5 Ask why (empty dispenser icon), 6 Fix and remeasure (small run chart). Center text: 'Fix the system, not the person.'",
    "Six-step cycle for infection prevention audits: choose a task, use a checklist, observe, give feedback, ask why, fix and remeasure.",
    "Audits improve care when feedback is quick and the misses lead to system fixes that are then remeasured.",
    "Apply", "Gives the observation routine a shape the nurse can follow and teach.")
fig("SDNR03-F3", "03", "cluster", "first-hour-cluster", "A", W, "The first hour of a suspected cluster",
    "Top node 'Two or more patients unwell together: same shift, loop, station or supplies'. Sequential nodes: 1 'Treat: charge nurse and physician at the bedside; cultures before antibiotics as ordered' (red), 2 'Contain: take suspected items out of use' (amber), 3 'Preserve: bag and label, keep lot numbers, do not discard' (amber), 4 'List: start a line list' (teal), 5 'Notify: head nurse, clinical head, infection control' (navy), 6 'Look for the common source: supplies, medicines, water, machines, technique' (green). Side warning box in red: 'Do not throw away the tray.'",
    "Six-step first-hour response to a suspected infection cluster, from treating patients to finding the common source.",
    "In a suspected cluster, patients come first, then containment, preservation of evidence, a line list, notification and the search for a common source.",
    "Apply", "Prevents the well-meaning error of discarding the very items an investigation needs.")

# ── Module 4 ──
fig("SDNR04-F1", "04", "stages", "teach-in-stages", "C", L, "From the head to the hands",
    "Six cards in a rising staircase: Explain, Demonstrate, Rehearse on a simulator, Supervised practice, Graded independence, Reassess on change. Above the staircase a thin gradient bar labeled from left to right 'Cognitive: every step thought through', 'Associative: steps link, errors fall', 'Autonomous: attention free for the patient'. A small amber note: 'A quiz score shows knowledge; only observation shows the hands.'",
    "Staircase of teaching stages from explanation to independence, aligned with the cognitive, associative and autonomous stages of skill learning.",
    "Skills move from conscious steps to automatic routines only through rehearsal and supervised practice.",
    "Understand", "Explains why a lecture or quiz cannot certify a procedure.")
fig("SDNR04-F2", "04", "gap", "training-vs-system-gap", "B", L, "Training gap or system gap?",
    "Two equal panels. Left 'Training gap' (teal): a nurse looking puzzled at a new catheter cap; bullets 'Never taught', 'New device', 'Not practiced'; fix 'Teach, rehearse, assess'. Right 'System gap' (amber): an empty hand-rub dispenser, a missing card at the station, a crowded roster board; bullets 'Knows how', 'Right action is hard', 'Under pressure'; fix 'Change supplies, layout, time'. Center question: 'Could she do it correctly if her life depended on it?'",
    "Comparison of training gaps and system gaps, with the test question and the matching fix for each.",
    "Before teaching, ask whether the problem is not knowing how, or a system that makes the right action hard.",
    "Understand", "Stops units from answering every incident with a lecture.")

# ── Module 5 ──
fig("SDNR05-F1", "05", "thirst", "salt-thirst-weight", "M", L, "Salt makes thirst, and thirst wins",
    "Left: semi-photorealistic Filipino meal elements (a bowl of instant noodles, dried fish, a small dish of soy sauce). Arrow to a blood vessel cross-section with rising sodium particles. Dashed magnified inset of the brain's hypothalamus with a small glowing sensor labeled 'Osmoreceptors'. Arrow to a person drinking from a glass. Arrow to a body silhouette with fluid shading at the ankles and lungs labeled 'No kidneys: water stays'. Arrow to a weighing scale with an upward arrow labeled 'Weight gain between sessions'. Bottom strip in three parts: red 'Injury: salty food drives thirst' → green 'Fix: less salt; count soup and sabaw as fluid' → navy 'Benefit: smaller weight gains, gentler fluid removal'.",
    "Mechanism poster from salty food to raised blood sodium, thirst, retained water and weight gain between dialysis sessions.",
    "Salt raises blood sodium, brain sensors switch on thirst, and without kidneys the water stays as weight gain; less salt reduces the drive to drink.",
    "Understand", "Explains why 'drink less' fails without salt teaching, in a way patients and nurses can redraw.")
fig("SDNR05-F2", "05", "teachback", "teach-back-loop", "C", L, "Teach-back: teach one thing, then check",
    "Five cards in a loop: 1 Ask (what worries you?), 2 Teach one thing (a real bowl and cup), 3 Check ('Tell me in your own words' or 'Show me'), 4 Reteach if any gap, 5 Record the patient's own words. A red crossed-out speech bubble beside the loop: 'Do you understand?'",
    "Five-step teach-back loop with a crossed-out 'Do you understand?' question.",
    "Understanding is confirmed when the patient explains or shows the action, not when they nod.",
    "Apply", "Replaces the ineffective yes-or-no question with a checkable routine.")

# ── Module 6 ──
fig("SDNR06-F1", "06", "define", "three-denominators", "B", L, "Same referrals, three answers",
    "Three equal panels with simple person icons. Panel 1 (red X in corner) '100%': 12 icons highlighted out of 12, caption 'Forms sent / forms sent'. Panel 2 (amber) '60%': 12 highlighted of 20, caption 'Forms sent / referrals due'. Panel 3 (green check) '40%': 8 highlighted of 20, caption 'Plans returned / referrals due'. Under all: 'Closure is what helps the patient. Define the measure before you count.'",
    "Three ways to count the same twenty referrals, giving 100, 60 and 40 percent; only the last measures closure.",
    "The same data give 100, 60 or 40 percent depending on the numerator and denominator; the honest closure rate here is 8 of 20.",
    "Appreciate", "Shows in one glance how a denominator can hide patients.")
fig("SDNR06-F2", "06", "runchart", "run-chart-rules", "D", L, "Signal or noise? Four run-chart rules",
    "A large clean run chart of monthly closure percentages (18 points) with a dashed median line; after a vertical dotted line labeled 'Change tested', seven consecutive points sit above the median and are shaded green with the label 'Shift: 6 or more on one side'. Small inset cards to the right: 'Trend: 5 or more rising or falling', 'Too few or too many crossings', 'Astronomical point: investigate'. Bottom strip: 'One good month is not evidence. Look for a rule.'",
    "Run chart with a median line and a highlighted shift after a change, with cards for the four run rules.",
    "Run charts separate real change from chance: six points on one side of the median is a shift; five rising or falling points is a trend.",
    "Understand", "Gives quality nurses the visual grammar to read their own data honestly.")

# ── Module 7 ──
fig("SDNR07-F1", "07", "vnd", "venous-needle-dislodgement", "M", L, "Why the alarm may stay quiet",
    "Semi-photorealistic forearm with a fistula and two needles, the venous needle slipped out of the skin and lying on a blanket, blood pooling. Dashed magnified inset of the venous line and pressure sensor with a gauge: 'Most pressure comes from the needle and tubing; it barely changes when the needle comes out'. Right side: a simple timer graphic 'At 300 mL/min: 1.5 liters in 5 minutes' with a blood-volume silhouette one-third shaded. Bottom strip: red 'Hidden site, silent alarm' → green 'Keep the access arm visible; secure lines' → navy 'Bleeding seen in seconds, not minutes'.",
    "Mechanism poster showing why venous needle dislodgement may not trigger the pressure alarm and how fast blood can be lost.",
    "When the venous needle slips out, the line still resists flow, so the pressure alarm may not sound; at 300 mL a minute about 1.5 liters can be lost in five minutes.",
    "Appreciate", "Makes the most dangerous silent failure in dialysis vivid enough to change the blanket habit.")
fig("SDNR07-F2", "07", "prepare", "disaster-readiness-grid", "E", S, "Ready for the events we actually face",
    "Reference card with five rows: Power interruption (keep alarms on, uncover needle sites, manual blood return per manufacturer); Water failure (no new starts, end per protocol, backup units); Earthquake (protect in place, disconnect only if evacuating); Typhoon and flood (reschedule early, contact list, missed-session diet); Fire (emergency disconnection, evacuate, account for every patient). Columns: 'First priorities' and 'Prepare ahead'. Each row has a small icon. Footer: 'Practice the likely event before it happens.'",
    "Reference card of first priorities and preparation for power failure, water failure, earthquake, typhoon and flood, and fire.",
    "Each likely emergency has first priorities at the bedside and preparation that must happen beforehand.",
    "Apply", "A quick-look card for drills and for the real event.")
fig("SDNR07-F3", "07", "hazards", "hazard-round-strip", "P", L, "A hazard round in five frames",
    "Five photorealistic panels: 1 green frame: an access arm uncovered with a blanket over the body; 2 green frame: venous line looped and taped; 3 green frame: a nurse checking an emergency cart with a checklist; 4 green frame: a laminated card and clamps in a small kit at a station; 5 red X: a blanket covering a needle site. One-line captions: 'Arm visible', 'Line secured', 'Cart checked', 'Disconnection kit here', 'Never cover the site'.",
    "Five-photo strip of safe and unsafe findings on a hazard round, ending with a covered needle site marked as unsafe.",
    "A hazard round looks for ordinary safeguards: visible access, secured lines, a checked cart, a disconnection kit at every station.",
    "Apply", "Shows correct and incorrect practice in the setting where nurses work.")

# ── Module 8 ──
fig("SDNR08-F1", "08", "why", "what-changes-in-hospital", "B", L, "What can change while the patient is away",
    "Two columns joined by arrows: left 'Unit chart' (old target weight, old blood pressure medicine, fistula access, no antibiotic), right 'Discharge summary' (new target weight, medicine stopped, new catheter, antibiotic after dialysis, pending culture). Each difference marked with an amber triangle. Center banner: 'Every difference goes to the physician before the next session.'",
    "Side-by-side comparison of the unit chart and a discharge summary with five differences flagged.",
    "Hospitals change target weights, medicines, access and antibiotics; every difference must be decided before the next treatment.",
    "Understand", "Shows why reconciliation is a safety step, not paperwork.")
fig("SDNR08-F2", "08", "reconcile", "reconciliation-algorithm", "A", W, "Back from hospital: reconcile before you connect",
    "Top node 'Patient returns from hospital, emergency room or another unit'. Steps: 'Gather: discharge summary, medicine bag, new orders, pending results' → 'Compare side by side: prescription, target weight, access, heparin, medicines, labs' → diamond 'Any difference?' YES → 'SBAR to physician (pharmacist for medicines) before connection' → 'Record each decision, who decided, when' → 'Teach patient and caregiver; teach-back'. NO → 'Document reconciliation; proceed'. Red side box: 'The nurse finds and escalates; the physician decides.'",
    "Algorithm for reconciling a patient's orders after a hospital stay before the next dialysis session.",
    "After any hospital stay, gather documents, compare, escalate every difference and record the decisions before connecting.",
    "Apply", "Turns the module's practice into a portrait job aid for the dialysis station.",
    (("SBAR", "Situation, Background, Assessment, Recommendation"),))

# ── Module 9 ──
fig("SDNR09-F1", "09", "physiology", "renal-anemia-factory", "M", L, "The marrow factory: order slips, raw material, a calm floor",
    "Organ-level panel: a kidney sending small glowing particles labeled 'Erythropoietin (order slip)' toward a bone with marrow. Dashed magnified inset of the marrow making red cells. A transferrin 'truck' carrying iron from the gut and stores; a liver releasing 'Hepcidin' as a gate that blocks iron (red). An inflammation icon (flame) dimming the factory. Blood droplets leaving through a dialysis line labeled 'Losses'. Bottom strip: red 'Kidney failure: fewer order slips, iron locked away, blood lost' → green 'Treatment by prescription: ESA and iron within limits' → navy 'Aim: fewer transfusions and symptoms, not a normal number'.",
    "Mechanism poster of renal anemia: low erythropoietin, iron blocked by hepcidin, inflammation and blood loss.",
    "Kidney failure reduces erythropoietin, hepcidin and inflammation lock iron away, and blood is lost; treatment aims to reduce transfusions and symptoms, not to normalize hemoglobin.",
    "Understand", "Gives nurses a model for reading hemoglobin, ferritin and TSAT together.",
    (("ESA", "Erythropoiesis-stimulating agent"), ("TSAT", "Transferrin saturation")))
fig("SDNR09-F2", "09", "evidence", "treat-and-pivotal", "B", L, "Two trials that shaped anemia care",
    "Two equal cards. Left 'TREAT, 2009' (amber): 4,038 patients; darbepoetin to hemoglobin about 13 vs placebo; 'No fewer deaths or heart events'; 'Strokes: 101 vs 53'; 'About 1 extra stroke per 42 treated'. Right 'PIVOTAL, 2019' (green): 2,141 patients on hemodialysis; proactive vs reactive IV iron; 'Heart events or death: 29.3% vs 32.3%'; 'About 1 prevented per 33 over 2 years'; 'Less ESA, same infections'. Footer: 'Hemoglobin is a surrogate. Patients feel strokes, transfusions and symptoms.'",
    "Two trial cards: TREAT showed more strokes with a high hemoglobin target; PIVOTAL showed fewer cardiovascular events with proactive iron.",
    "TREAT showed that aiming for near-normal hemoglobin increased strokes; PIVOTAL showed proactive iron within limits reduced a cardiovascular composite and ESA use.",
    "Appreciate", "Shows with absolute numbers why the target sits below normal and why iron is given within limits.",
    (("ESA", "Erythropoiesis-stimulating agent"), ("IV", "Intravenous")))
fig("SDNR09-F3", "09", "authority", "falling-hemoglobin-algorithm", "A", W, "Hemoglobin changed: protocol step or physician now?",
    "Top node 'New hemoglobin result'. Diamond 'Bleeding signs, chest pain, neurological symptoms, fever, surgery, new anticoagulant?' YES (red) → 'Vital signs; physician now. Not a protocol step.' NO → diamond 'Change faster than expected (rise of more than 1 g/dL in 2 weeks, or a rapid fall)?' YES (amber) → 'Report before the next scheduled dose.' NO → diamond 'Patient covered by the signed protocol and no exclusion applies?' YES (green) → 'Give exactly what the protocol states; record.' NO (amber) → 'Prescriber review.'",
    "Algorithm deciding whether a hemoglobin change is a protocol step, a prescriber report, or an urgent physician call.",
    "Bleeding and other red flags go to the physician now; rapid changes are reported before the next dose; protocols apply only to covered patients with no exclusion.",
    "Apply", "Protects against treating a bleed as a dosing problem.")

# ── Module 10 ──
fig("SDNR10-F1", "10", "pathway", "referral-to-decision", "C", L, "Referral is not listing",
    "Four cards connected by arrows, each with an owner chip: 1 Referral (dialysis unit; sent and acknowledged), 2 Evaluation (transplant team; tests, donor assessed separately), 3 Decision (transplant team; suitable, not suitable, not yet), 4 Waiting or scheduled (transplant center; listing is its decision). A speech bubble at card 1 from a family icon: 'We're on the list!' with a gentle correction arrow to card 4.",
    "Four steps from referral to evaluation, decision and waiting, each with its owner, correcting the belief that referral means listing.",
    "Referral starts evaluation; listing and scheduling are later decisions by the transplant center.",
    "Understand", "Corrects the most common family misunderstanding about transplant.")
fig("SDNR10-F2", "10", "ethics", "permitted-routes", "B", L, "Free and informed: which routes are permitted",
    "Two panels. Left green 'Permitted': living donor evaluated privately by a separate team, free to stop at any time; deceased donation through the authorized program. Right red 'Not permitted': payment for an organ; pressure on a family member; transplant tourism. Small icons only (a crossed-out handshake, a balance scale, a hospital). Footer: 'Refuse involvement, offer legal routes, report.' No people shown exchanging money.",
    "Comparison of permitted donation routes with practices that are not permitted, such as paying for an organ.",
    "Organs are donated freely; living donors are assessed separately and may stop at any time; buying or brokering organs is not permitted.",
    "Appreciate", "States the ethical boundary plainly for a sensitive conversation.")

# ── Module 11 ──
fig("SDNR11-F1", "11", "three", "one-session-three-records", "D", L, "One session, three records, one truth",
    "Center: a dialysis session icon (chair and machine) labeled 'What happened'. Three arrows outward to: 'Clinical record' (teal: care and continuity), 'Registry' (green: national kidney data), 'PhilHealth claim' (amber: payment). A red crossed-out arrow from the claim back to the clinical record labeled 'Never change the chart to fit the claim'. Bottom strip: 'Derived records follow the clinical truth.'",
    "Diagram of one dialysis session feeding the clinical record, the registry and the PhilHealth claim, with a crossed-out arrow from claim back to chart.",
    "The chart records what happened; the registry and claim follow it, never the reverse.",
    "Understand", "Fixes the direction of truth in the learner's mind.")
fig("SDNR11-F2", "11", "amend", "correct-vs-conceal", "B", L, "Correct openly, never conceal",
    "Two paper-record close-ups side by side. Left green check 'Correct': a single neat line through an entry, still readable, with the correction, date, time, initials and reason beside it. Right red X 'Wrong': correction fluid, overwritten numbers, a torn page edge. Footer: 'Late entries are labeled late. Never back-date or sign for someone else.'",
    "Comparison of a correct visible amendment with concealing corrections on a paper record.",
    "A correction leaves the original readable and records who changed it, when and why.",
    "Apply", "Shows the exact look of a defensible amendment.")

# ── Module 12 ──
fig("SDNR12-F1", "12", "hazards", "membrane-hazards", "M", L, "What crosses the membrane",
    "Organ-level: a dialyzer cut-away with blood flowing one way and dialysate the other (countercurrent arrows), labeled 'About 120 liters per session at 500 mL/min (illustrative)'. Dashed magnified inset of one hollow fiber wall: small particles labeled 'Chloramine, metals' passing through (red arrows); intact bacteria blocked (gray, stopped); small fragments labeled 'Endotoxin' passing or triggering inflammation (amber). A small sidebar 'Caruaru 1996: untreated water, microcystins; 101 liver failure, 50 deaths'. Bottom strip: red 'Hazard in water or dialysate' → green 'Technical release before use' → navy 'Patients protected'.",
    "Mechanism poster of a dialyzer membrane showing chemicals and endotoxin crossing while intact bacteria are blocked, with the Caruaru outbreak noted.",
    "Small chemicals cross the membrane and bacterial fragments can trigger reactions; the Caruaru outbreak showed the cost of untreated water.",
    "Understand", "Explains why water and machine release are clinical safeguards.")
fig("SDNR12-F2", "12", "restart", "stop-use-to-restart", "A", W, "From stop-use to restart",
    "Top node 'Missing release, failed test, or patient reactions on a loop or machine'. Steps: 'Stop exposure: no new starts; stop affected treatments as directed' (red) → 'Care for patients; samples as ordered' (red) → 'Preserve: do not flush until the technical team samples' (amber) → 'Record exposures: patients, stations, machines, lots' (teal) → 'Notify technicians, head nurse, clinical head, infection prevention' (navy). Two parallel boxes at the bottom, both required: 'Technical release (technician)' and 'Clinical approval (physician)' → green 'Restart; tell every shift'.",
    "Algorithm from stopping use of a water loop or machine to restart, requiring both technical release and clinical approval.",
    "After a failure, exposure stops, evidence is preserved, and treatment restarts only with both technical release and clinical approval.",
    "Apply", "Makes the two-key restart rule unforgettable.")

# ── Module 13 ──
fig("SDNR13-F1", "13", "kinetics", "urea-curve-sampling", "D", L, "What the urea numbers really measure",
    "A smooth curve of blood urea falling during a four-hour session and rising slightly after (rebound). Markers: 'Pre sample: before saline or heparin' at the start; 'Post sample: unit method (slow-flow or stop-pump), fixed time' at the end. Dashed inset of the access with cleaned blood looping from the venous to the arterial needle labeled 'Recirculation makes post urea falsely low'. Worked example box: 'Pre 150, post 50 → URR 66.7%'. Bottom strip: 'Validate the sample before trusting the number.'",
    "Urea curve during dialysis with correct sampling points, a recirculation inset and a worked urea reduction ratio.",
    "URR depends on correctly timed samples; recirculation or a late sample distorts the result.",
    "Understand", "Shows why the same blood test can tell two different stories.",
    (("URR", "Urea reduction ratio"),))
fig("SDNR13-F2", "13", "volume", "plasma-refill-stunning", "M", L, "When fluid comes off faster than it can refill",
    "Organ-level: a body silhouette with fluid in tissues (light blue) and in blood vessels (red). Arrows: ultrafiltration pulling fluid out of the blood into the dialyzer (large arrow), plasma refill from tissues into vessels (smaller arrows). Dashed magnified inset of the heart with a patch of muscle dimmed labeled 'Stunning with repeated low flow'. Callouts: 'Cramps', 'Low blood pressure', 'Early ending'. Side card: 'Above 13 mL/kg/h: associated with higher mortality'. Bottom strip: red 'Removal faster than refill' → green 'Team review: weight gain, time, target, medicines, salt' → navy 'Gentler sessions'.",
    "Mechanism poster of ultrafiltration outpacing plasma refill, causing cramps, hypotension and heart muscle stunning.",
    "When fluid is removed faster than tissues can refill the blood vessels, blood pressure falls and the heart can be stunned; the fix is a team review, not faster removal.",
    "Understand", "Explains why the nurse never raises the ultrafiltration rate to finish on time.")
fig("SDNR13-F3", "13", "evidence", "adequacy-floor-not-dial", "E", S, "Adequacy is a floor, not a dial",
    "Reference card with five rows: 'Owen 1993 (13,473 patients): URR below 60% associated with higher death risk; albumin a stronger predictor'; 'HEMO 2002 (1,846, randomized): spKt/V 1.71 vs 1.32, no mortality difference'; 'KDOQI 2015: target spKt/V 1.4; minimum 1.2'; 'DOPPS 2006 (22,000): longer than 240 minutes associated with lower mortality'; 'Flythe 2011: UFR above 13 mL/kg/h associated with higher mortality'. Each row tagged 'Randomized' (green), 'Observational' (amber) or 'Guideline' (navy). Footer: 'URR and Kt/V are surrogates.'",
    "Reference card of adequacy evidence with each study tagged as randomized, observational or guideline.",
    "Too little dialysis is associated with harm, more than the standard did not help, and treatment time and fluid removal rate matter beyond urea.",
    "Appreciate", "Shows at a glance how certain each adequacy claim is.",
    (("URR", "Urea reduction ratio"), ("UFR", "Ultrafiltration rate"), ("KDOQI", "Kidney Disease Outcomes Quality Initiative"), ("DOPPS", "Dialysis Outcomes and Practice Patterns Study"), ("HEMO", "Hemodialysis Study")))

# ── Module 14 ──
fig("SDNR14-F1", "14", "integrated", "priority-ladder", "C", L, "Everything at once: the order of priorities",
    "Six numbered cards descending like a ladder: 1 Patient safety now (red), 2 Stop further exposure (amber), 3 Notify the decision-makers (navy), 4 Reconcile unclear orders (teal), 5 Coordinate tomorrow's appointments (green), 6 Document facts, times, owners (gray). Small portfolio icons beside each card show which portfolio nurse helps. Footer: 'The charge nurse and physician decide; each portfolio brings its part.'",
    "Ladder of six priorities in a multi-problem shift, from patient safety to documentation.",
    "When problems arrive together, patient safety comes first, then stopping exposure, notification, reconciliation, coordination and documentation.",
    "Apply", "Gives the capstone case a memorable structure.")
fig("SDNR14-F2", "14", "marking", "osce-four-stations", "E", S, "Four stations, one standard",
    "Reference card: four quadrants, each a station: 1 Immediate safety and escalation, 2 Infection and water stop-use, 3 Reconciliation and handoff, 4 Portfolio presentation; each with two key criteria and one critical error in red. Center circle: 'Pass: 32 of 40, at least 7 per station, no critical error'.",
    "Four-quadrant card of the capstone OSCE stations with criteria, critical errors and the pass standard.",
    "The capstone OSCE has four stations; passing needs 32 of 40, at least 7 per station and no critical error.",
    "Apply", "Lets learners and assessors see the whole standard in one place.",
    (("OSCE", "Objective structured clinical examination"),))

FIGURES = _F
