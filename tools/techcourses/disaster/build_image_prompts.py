# -*- coding: utf-8 -*-
"""Disaster Preparedness and Response: image plan and GPT prompt pack (one Markdown file).
Built from DISASTER_PREPAREDNESS_BLUEPRINT.md v1.1 (November 28, 2026) before the course package exists, so the module
list and figure plan live here. When the package is built, figs.py must use these same file names.
Skills applied: williamriveromd-hero-vignette v3 (heroes), williamriveromd-simple-figure and
williamriveromd-algorithm-generator-skill Style Mode C (figures, never an official chart look), williamriveromd-infographic-skill
(tiles, OG share cards), dialysis-circuit-schematic lock where a circuit is drawn.
Run:  python3 tools/techcourses/disaster/build_image_prompts.py <output.md>"""
import sys
from pathlib import Path

HUB = "disaster-preparedness"
MODS = [  # id, slug, title, hero scene, OG art, OG chips
    ("01", "why-disasters-hurt-twice", "Why Disasters Hurt Dialysis Patients Twice",
     "A freestanding dialysis clinic on a flooded city street in light rain, its roll-up shutter half down; an older man with a cane and his adult daughter stand on a dry step across the street looking at it, worried but safe; muddy water reflects the clinic's sign (no readable words).",
     "a flooded street in front of a small clinic with its shutter half down, an older man and his daughter on a dry step", '"Missed sessions" · "The causal chain" · "Philippine hazards"'),
    ("02", "hazards-and-dependencies", "Know Your Unit's Hazards and Dependencies",
     "A safety nurse and a water treatment technician tracing pipes and cables behind a reverse osmosis unit with a clipboard and flashlight, labels on the equipment unreadable; bright utility room.",
     "a clipboard dependency map with icons for power, water, staff, supplies and transport beside a reverse osmosis unit", '"Hazard map" · "Dependencies" · "Single points of failure"'),
    ("03", "unit-plan-and-command", "The Unit Plan and Who Commands",
     "A small dialysis team around a table with a one-page plan (blank lines), a printed phone tree, a two-way radio and a wall clock; the charge nurse points at the plan while a physician listens.",
     "a one-page plan on a clipboard, a two-way radio and a phone tree on a table", '"One-page plan" · "Command roles" · "Triggers"'),
    ("04", "ready-patients", "Ready Patients: Card, Diet, Medicines, Contacts",
     "At home, an older Filipino man on hemodialysis and his adult daughter pack a waterproof go-bag on a wooden table: a laminated emergency card (blank), pill organizer, a folded diet sheet, a power bank, bottled water and a flashlight; warm afternoon light.",
     "a waterproof go-bag with a blank emergency card, pill organizer, diet sheet, power bank and flashlight", '"Emergency card" · "3-day kidney diet" · "Stay connected, wait for staff"'),
    ("05", "typhoons-and-floods", "Typhoons and Floods",
     "A dialysis unit at dusk under a heavy typhoon sky: through the glass front, staff move supply boxes onto high shelves; outside, a van waits to take staff home; rain streaks the windows; the mood is busy, calm, prepared.",
     "a dialysis unit window with rain streaks and supply boxes on high shelves, a staff van outside", '"Before the signal" · "Early dialysis" · "After the storm"'),
    ("06", "earthquake-on-the-machine", "Earthquake on the Machine",
     "A nurse crouches beside a patient who stays seated and connected in a dialysis recliner, one arm shielding the patient's head and the other steadying the access arm; the machine's wheels are locked; a ceiling light sways slightly; nobody is injured.",
     "a nurse crouching beside a connected patient in a recliner, shielding the head and access arm, machine wheels locked", '"Protect in place" · "After the shaking" · "Take off or stay"'),
    ("07", "fire-and-evacuation", "Fire and Evacuation",
     "Outside a building at an assembly point on a clear day, a nurse with a clipboard checks names while colleagues bring patients in wheelchairs and one on a stretcher; a faint haze from a window behind; calm and orderly.",
     "an assembly point with a nurse holding a census clipboard and patients in wheelchairs", '"RACE" · "Mobility categories" · "Account for everyone"'),
    ("08", "power-water-supplies", "Power, Water and Supplies",
     "At night, a biomedical technician with a headlamp checks the fuel gauge of a generator in a covered yard, while through a window behind him the unit glows with emergency lights and a nurse stands with patients.",
     "a generator with a fuel gauge, a headlamp and a battery icon, with the dialysis unit's emergency lights behind", '"First ten minutes" · "Blood return without power" · "Signed water release"'),
    ("09", "heat-ashfall-outbreaks", "Heat, Ashfall and Outbreaks",
     "Two staff in N95 masks close the windows of a dialysis unit while fine gray volcanic ash coats the parked cars and leaves outside; a distant hazy volcano silhouette; indoor light bright and clean.",
     "fine gray ash on a car windshield, a stack of N95 masks and a closed window", '"Heat days" · "Ashfall" · "Outbreaks"'),
    ("10", "keeping-everyone-dialyzed", "Keeping Everyone Dialyzed: Priority, Placement, Tracking",
     "A nurse on the phone in front of a whiteboard tracker with blank rows and colored magnets, while a physician reviews a laboratory sheet (unreadable) and a map with two pins marks receiving units.",
     "a whiteboard tracker with blank rows and colored magnets beside a map with two pins", '"Find every patient" · "Priority roster" · "Receiving units"'),
    ("11", "reopening-and-recovery", "Reopening Safely and Recovering",
     "Morning sun through the windows of a clean, dry dialysis unit after a flood; at the water room door, a head nurse and a water treatment technician sign a checklist on a clipboard (blank); chairs ready, floor mopped.",
     "a clipboard with five checkboxes at a water room door, sunlight in a clean dialysis unit", '"Five signed gates" · "Reconciliation" · "Caring for staff"'),
    ("12", "running-drills", "Running Drills That Change Practice",
     "A tabletop exercise: a dialysis team leans over a large printed floor plan of their unit with small tokens for chairs and people, a facilitator holding cards with injects, a timer on the table.",
     "a printed unit floor plan with tokens, a stack of inject cards and a timer", '"Tabletop exercise" · "Injects" · "After-action report"'),
]
HUB_SCENE = ("Before typhoon season in a bright Philippine dialysis unit: a nurse lifts supply boxes onto a high shelf, a technician "
             "checks a generator panel through an open door, and the head nurse holds a clipboard call list; chairs empty, rain clouds "
             "gathering outside the window.")

U, A, P = "Understand", "Apply", "Appreciate"
SEQ, CMP, ONE, ALG, REF, SCN = ("Step sequence", "Comparison", "One-panel poster", "Original decision layout", "Reference card",
                                "Scene illustration")
# key: (module, file stem, type, purpose, content, caption, locks)
FIGS = [
    ("00", "act-learn-practice", SEQ, P, "Three connected panels labeled Act, Learn and Practice: a phone showing a disaster quick card, a tablet with an open lesson, and a team around a tabletop floor plan.", "Disaster readiness has three parts: act with the quick cards, learn with the modules, practice with drills.", ""),
    ("01", "causal-chain", SEQ, U, "Six linked steps left to right with one picture each: Warning (storm cloud), Event (ground crack or flame), Access cut (flooded road), Body builds up (potassium and fluid icons rising), Late arrival (hospital door), Unsafe restart (water drop with a question mark). A teal arrow under steps 1 to 6 labeled Where we act.", "Disasters hurt dialysis patients twice: through the event, then through missed treatment. Each link is a place to act.", ""),
    ("01", "philippine-hazards", ONE, P, "A simplified outline map of the Philippines on a light background with small icons spread across it: typhoon swirls from the east, flood droplets, earthquake jagged lines, three volcano icons, a sun icon for heat. No place names, no fault lines, no data.", "Typhoons, floods, earthquakes, volcanoes and heat: the hazards a Philippine dialysis unit plans for.", "map"),
    ("01", "what-the-studies-show", REF, U, "A four-row evidence card. Row 1: Storms and missed sessions, \"55% more missed sessions over the next week\". Row 2: Three or more missed sessions, \"more hospital admissions\". Row 3: Dialysis before landfall, \"fewer emergency visits and admissions\". Row 4: Planning, \"no excess deaths after a coordinated response\". Small gray tag on every row: Observational.", "What the studies show, and their limit: every finding is an association from observational data.", "nums"),
    ("02", "dependency-web", ONE, U, "A dialysis chair in the center with eight lines to icons around it: power, generator, water, reverse osmosis unit, staff, supplies, transport, records and phones. Two pairs are joined by red dashed lines labeled Fail together: power and water pump; roads and staff.", "Every chair depends on a web of services. Some fail together, so plan for both at once.", ""),
    ("02", "hazard-matrix", REF, A, "A three-by-three grid, Likelihood on one axis (low, medium, high) and Impact on the other (low, medium, high). Hazard icons placed as an example: typhoon and flood high-high, power failure high-medium, earthquake low-high, fire low-high, ashfall low-medium, water failure medium-high. Caption tag: Example, rate your own unit.", "A simple hazard grid. Plan first for what is likely and severe; rate your own unit, not this example.", ""),
    ("02", "single-point-of-failure", CMP, U, "Two panels. Left, red: one breaker feeding both the water booster pump and the generator transfer switch; when it trips, both stop. Right, green: separate breakers, with the pump on generator backup.", "A single point of failure: one breaker that stops both water and backup power. Find them before a disaster does.", ""),
    ("03", "one-page-plan", REF, A, "A one-page plan template with labeled blank sections: Triggers, Who leads, First calls, Patients on machines, Patients due today, Receiving units, Supplies and power, Restart. Lines are blank.", "The unit plan fits on one page: triggers, who leads, first calls, patients, receiving units, supplies and restart.", ""),
    ("03", "command-chart", ALG, U, "An original organization chart: top box Incident lead (charge nurse with the physician). Four boxes below: Patient care (nurses), Equipment and utilities (technicians), Tracking and records (records officer, social worker), Outside contacts (receiving units, hospital, local disaster office). A side box: Safety nurse or head nurse, plans and runs drills, not in command during the event.", "Who commands during the event, and who does what. The person who runs the drills is not the one in command.", "orig"),
    ("03", "trigger-ladder", ALG, A, "An original vertical ladder of five steps for rising typhoon signals, each with a unit action: Signal 1: review the plan and the call list. Signal 2: call-down; early dialysis decision with the nephrologist. Signal 3: staff transport; supplies up; last safe session time. Signal 4 and 5: unit closed; patients tracked. A gray footnote: Example actions, your plan sets them.", "Signals rise; so do the unit's actions. The actions shown are an example; your plan sets yours.", "orig"),
    ("03", "communication-tree", ONE, A, "A branching tree from the incident lead to staff and patients, with four channels shown as icons: text message, phone call, messaging app group, two-way radio, plus a runner on foot when everything else fails.", "When networks fail, have more than one way to reach staff and patients, down to a runner on foot.", ""),
    ("04", "emergency-card", REF, A, "A wallet-size patient emergency card shown front and back, with labeled blank fields: Name, Diagnosis, Dialysis days, Access type, Target weight, Last potassium, Medicines, Allergies, PhilHealth number, My unit, Backup unit, Family contact.", "The patient emergency card: everything a strange unit needs, carried at all times.", ""),
    ("04", "go-bag", ONE, A, "A waterproof bag open on a table with labeled items: emergency card, medicine list and pills, three-day diet sheet, power bank, flashlight, bottled water, copies of records, clean dressing for the access.", "The go-bag, packed before the season.", ""),
    ("04", "emergency-diet-principles", CMP, A, "Two columns of Filipino foods. Choose (green): white rice, unsalted crackers, drained canned fruit, eggs, fresh chicken. Limit (amber): dried fish, instant noodles, canned sardines, bananas, coconut water. A small cup icon labeled Measure your fluid. Footer tag: Your dietitian's three-day plan sets the amounts.", "The three-day emergency kidney diet in principle: choose lower-potassium, lower-salt foods and measure fluid. The dietitian's plan sets the amounts.", "diet"),
    ("04", "on-the-machine-when-disaster-strikes", SEQ, A, "Four steps for a patient on the machine: 1 Stay calm. 2 Stay connected. 3 Protect the access arm. 4 Wait for staff. A crossed-out icon of a hand pulling a needle: Do not disconnect yourself.", "If disaster strikes during your session: stay calm, stay connected, protect your access arm, and wait for staff.", ""),
    ("05", "typhoon-timeline", SEQ, A, "A horizontal timeline in four phases with unit actions: Before the season (plan, call list, supplies, agreements); Signal raised (call-down, early dialysis decision, staff transport); Landfall (unit closed, patients tracked); After (restart gates, reconciliation).", "A typhoon in four phases, each with the unit's actions.", ""),
    ("05", "early-dialysis-decision", ALG, A, "An original decision layout: Landfall expected before the next session? If yes: nephrologist reviews the schedule, patients moved earlier, transport arranged, diet and medicine reminders. If no: keep schedule, confirm contacts. A teal note: The nephrologist approves every change.", "Early dialysis before landfall: a schedule change the nephrologist approves, with transport and reminders.", "orig"),
    ("05", "flood-risks", ONE, U, "Three panels: wet floor and electrical equipment (unplug, do not touch wet machines); wading in flood water (avoid wading, cover wounds); after the flood (report fever, clean before reopening).", "Flood water brings electrical, infection and contamination risks for staff and patients.", ""),
    ("06", "protect-in-place", SCN, A, "Side view of a nurse crouched beside a patient seated and connected in a dialysis recliner, shielding the patient's head and steadying the access arm; machine wheel locks highlighted; a second staff member crouched by the next chair.", "During the shaking: protect in place. Patients stay connected; staff shield heads and access arms; machines stay locked.", "circuit"),
    ("06", "after-the-shaking", REF, A, "A checklist card with icons: needles and lines secure; no blood at connections; machine upright and running; no water leak; no gas smell; no new cracks; everyone accounted for.", "After the shaking: check people, lines, machines and the building before deciding what comes next.", ""),
    ("06", "take-off-or-stay", ALG, A, "An original decision layout: Evacuation ordered or building unsafe? If yes: emergency take-off by staff, then evacuate. Decision box: Air in the line, hemolysis or a severe reaction? If yes: do not return the blood. If no: return the blood if quick and safe, or clamp and disconnect. If no evacuation: continue or end each session per protocol.", "Take off or stay. Never return blood that may hold air, is hemolyzed or follows a severe reaction.", "orig"),
    ("06", "secure-equipment", ONE, A, "A dialysis machine with wheel locks engaged, a reverse osmosis unit strapped to the wall, shelves with lips and restraints, oxygen cylinders chained upright.", "Secure equipment before the earthquake: locks, straps, shelf lips and chained cylinders.", ""),
    ("07", "race-sequence", SEQ, A, "Four steps with icons: Rescue (move people from the danger), Alarm (raise the alarm and call), Contain (close doors), Extinguish or evacuate.", "RACE: rescue, alarm, contain, then extinguish a small fire or evacuate.", ""),
    ("07", "evacuation-floor-plan", ONE, A, "A top-down floor plan of a small dialysis unit with chairs color-coded by mobility: green walks alone, amber walks with help, blue wheelchair, purple stretcher; two exit routes with arrows to an assembly point outside.", "Mobility categories are set before the event, so everyone knows who needs help to leave.", ""),
    ("07", "census-at-the-assembly-point", SCN, P, "A nurse at an assembly point outside holding a census clipboard, checking off names; patients in wheelchairs and standing with staff; one patient on a stretcher with two staff.", "A named nurse holds the census and checks every patient at the assembly point. Missing patients are reported at once.", ""),
    ("07", "extinguisher-pass", SEQ, A, "Four steps on a red fire extinguisher: Pull the pin, Aim at the base, Squeeze the handle, Sweep side to side. A note: Only a small fire, with an exit behind you.", "PASS: pull, aim, squeeze, sweep, and only for a small fire with an exit behind you.", ""),
    ("07", "oxygen-and-fire", ONE, U, "An oxygen cylinder near a flame icon with a red warning: oxygen makes fire burn faster. Actions: turn off oxygen not in use, move cylinders away, never block exits with them.", "Oxygen makes fire burn faster. Turn off what is not in use and keep cylinders out of exits.", ""),
    ("08", "power-failure-first-ten-minutes", SEQ, A, "A timeline 0, 2, 5 and 10 minutes: stay with patients and uncover needle sites; machines on battery; check generator start; decide per patient to continue on battery or return blood; call the technician and the charge nurse.", "Power failure: the first ten minutes, in the order the Physician-on-Duty module teaches.", ""),
    ("08", "blood-return-without-power", SCN, A, "A gloved nurse turning the hand crank on a hemodialysis machine's blood pump to return blood, the venous line returning to the patient's access, the arterial line clamped, saline bag connected.", "Returning blood without power: the hand crank, as the manufacturer and your unit train it.", "circuit"),
    ("08", "generator-and-ups-checks", REF, A, "A check card with icons: fuel level, test run log, transfer switch test, battery-backed (UPS) outlets labeled, extension cords not used, contact for fuel delivery.", "Generator and backup power checks, logged before they are needed.", ""),
    ("08", "water-failure-decision", ALG, A, "An original decision layout: Water supply fails or a contamination alarm? Stop starting new treatments. End current treatments per protocol. Call the water technician. Resume only after a signed water release.", "When water fails or turns unsafe: stop new starts, end per protocol, and resume only after a signed release.", "orig"),
    ("08", "supply-buffer", ONE, A, "A storage shelf above a flood line with dialysis supplies, rotated first-in first-out, labeled by days of supply, with a red line marking past flood height.", "Keep a supply buffer above the flood line and rotate it.", ""),
    ("09", "heat-and-the-journey", ONE, U, "A patient's journey from home to the unit on a hot day: jeepney, waiting in the sun, then the unit; icons for water, shade, a fan, and a heat index thermometer without numbers.", "On heat-index days, the trip to the unit is part of the risk: shade, rest and timing matter.", ""),
    ("09", "ashfall-protections", ONE, A, "A dialysis unit during ashfall: windows and doors closed, air and water intakes covered, staff and patients in N95 masks at the entrance, an ash-cleaning station, the reverse osmosis room sealed.", "Ashfall: close the building, protect air and water intakes, mask people, clean ash before entry.", ""),
    ("09", "outbreak-as-a-disaster", CMP, U, "Three columns for an infectious outbreak: Cohorting (separate shifts or zones), Staff shortage (backup roster), Supply strain (masks, gowns, dialysis supplies).", "An outbreak is a slow disaster: cohort patients, protect the roster, and watch supplies.", ""),
    ("10", "find-every-patient", SCN, A, "A nurse on the phone at a whiteboard tracker with blank rows and colored magnets: reached, dialyzed elsewhere, not reached, in hospital; a clock showing time since the event.", "Find every patient: a tracker that shows who is reached, dialyzed elsewhere, missing or in hospital.", ""),
    ("10", "priority-roster", ALG, A, "An original layout: four inputs (time since last treatment, last potassium, fluid status, symptoms) feeding one box: Nephrologist sets the order. Output: First today, Next, Can wait with diet and review.", "Who dialyzes first is a medical decision. The nephrologist weighs time since dialysis, potassium, fluid and symptoms.", "orig"),
    ("10", "shortened-session-conditions", REF, U, "A card titled Shortened sessions: only when. Six checked rows: real shortage recorded; nephrologist's written order; time-limited with a review date; high-risk patients excluded; potassium and fluid watched; back to full sessions as soon as possible.", "Shortened sessions are a conditional option, never a routine: six conditions, all at once.", ""),
    ("10", "handoff-to-a-receiving-unit", SEQ, A, "Four steps: confirm the receiving unit and the accepting person; send the handoff (prescription, access, last labs, hepatitis status, medicines); arrange transport; tell the patient and record the placement.", "Placing a patient at a receiving unit: confirm, send the handoff, transport, record.", ""),
    ("11", "five-restart-gates", SEQ, A, "Five gates in a row, each with a signature line: Building safe; Qualified staff; Water and machines released; Supplies and emergency cart ready; Records recovered.", "Reopen through five signed gates. A verbal yes is not a gate.", ""),
    ("11", "reconciliation-board", REF, A, "A table with blank rows and four columns: Dialyzed where, Sessions missed, Needs extra session, Needs labs.", "Reconciliation after the event: who was dialyzed where, who missed sessions, who needs more.", ""),
    ("11", "caring-for-staff", SCN, P, "A small group of dialysis staff in a quiet break room after a disaster, sharing food, one listening to another; a notice board with blank cards; soft light.", "After the event, the people who kept the unit running need rest and support too.", ""),
    ("12", "exercise-ladder", SEQ, U, "Five rising steps: Orientation, Drill, Tabletop exercise, Functional exercise, Full-scale exercise, each with a small icon and a few words on what it tests.", "Exercises climb from talking through the plan to doing it for real.", ""),
    ("12", "anatomy-of-a-tabletop", ONE, A, "A table with a floor plan, three inject cards dealt in order, a timer, a recorder with a tablet, and a hot wash circle of chairs; labels: Scenario, Injects, Decisions, Hot wash.", "A tabletop exercise: a scenario, timed injects, decisions out loud, and a hot wash at the end.", ""),
    ("12", "after-action-report", REF, A, "A one-page report template with blank sections: Objectives met or not, What worked, What failed, Actions (owner and date), Next rehearsal.", "The after-action report: one page, with every action owned and dated.", ""),
    ("12", "the-watcher-rule", SCN, A, "During a drill at an empty station, a nurse wearing a colored vest labeled with an eye icon (no words) watches the patients still dialyzing at other chairs while colleagues practice.", "No drill on a working floor without a named watcher whose only job is the patients still dialyzing.", ""),
]

LOCKS = {
    "orig": ("ORIGINAL LAYOUT LOCK: an original renalcarematters.com teaching layout. Do not imitate any government, PAGASA, DOH, OCD or "
             "hospital chart, seal or form. House colors only: navy #0f1e2e text, teal #1a6b72 decisions, green #1f7a4d actions, amber "
             "#b8860b cautions, red #b91c1c stop boxes. At most 8 to 10 nodes, labels of six words or fewer."),
    "circuit": ("CIRCUIT LOCK (dialysis-circuit-schematic): blood leaves the patient on the RED arterial line, passes the blood pump, enters "
                "the dialyzer at an end port, leaves by the other end port, passes the venous drip chamber and air detector, and returns on "
                "the BLUE venous line. Dialysate tubing joins the dialyzer's SIDE ports only. One arterial and one venous line. No numbers."),
    "map": ("MAP LOCK: a simplified outline only. No place names, provinces, fault lines, volcano names, typhoon tracks or data; icons only "
            "show hazard types."),
    "nums": ("NUMBERS LOCK: the only number allowed is \"55%\" in row 1, exactly as written. No odds ratios, percentages or counts elsewhere."),
    "diet": ("DIET LOCK: no amounts, servings, milligrams or fluid volumes. Food photographs realistic and Filipino. The footer tag must read "
             "exactly as given."),
}
SCAFFOLD = {ALG: "williamriveromd-algorithm-generator-skill, Style Mode C (house style), portrait, original layout",
            CMP: "williamriveromd-simple-figure scaffold B: side-by-side panels",
            SEQ: "williamriveromd-simple-figure scaffold C: numbered steps with one picture each",
            ONE: "williamriveromd-simple-figure scaffold D: one strong central visual with up to five callouts",
            REF: "williamriveromd-simple-figure scaffold E: compact reference card",
            SCN: "williamriveromd-infographic-skill archetype A: semi-photorealistic scene with up to four short callouts"}
SIZE = {ALG: ("1024 × 1536", "2:3 portrait"), REF: ("1536 × 1152", "4:3")}
NEG_FIG = ("Avoid flat vector clip art, cartoon style, clutter, tiny unreadable labels, AI gibberish text, overprocessed HDR, excessive "
           "saturation. NEVER dark, navy, charcoal or black backgrounds: light backgrounds only. Use ONLY Inter. No logos, government seals, "
           "brand names, real names or readable patient data. No injured people, blood, bodies, burning people or panic. No numbers except "
           "those written in CONTENT. Never omit the renalcarematters.com attribution, exactly lowercase.")
NEG_HERO = ("Avoid: duplicated people, repeated compositions, cropped circle, objects touching the circular border, content inside the title "
            "safe zone, any text, captions, logos, watermarks, readable signs, rectangular borders, dark or black backgrounds, cartoon style, "
            "neon, HDR, over-saturation, distorted hands or faces, injured people, blood, bodies, flames on people, panic, disaster-porn "
            "devastation, a patient disconnecting their own lines.")
ROT = [("D Panorama", "wide-angle eye-level"), ("J Environmental Storytelling", "wide low angle"), ("A Editorial Portrait", "over-the-shoulder"),
       ("H Clinical", "three-quarter close"), ("E Lifestyle", "overhead three-quarter"), ("J Environmental Storytelling", "rear three-quarter"),
       ("A Editorial Portrait", "side profile"), ("D Panorama", "wide eye-level"), ("J Environmental Storytelling", "low side angle"),
       ("D Panorama", "wide-angle through a window"), ("H Clinical", "eye-level close"), ("J Environmental Storytelling", "straight-on"),
       ("C Radial", "top-down")]
CAST = ["a woman nurse in her forties with a short bob, a lean young male technician with a buzz cut, and a head nurse in her fifties with reading glasses",
        "an older man in his late sixties with a cane and thinning gray hair, and his daughter in her thirties with a ponytail and a raincoat",
        "a woman safety nurse in her thirties with a high bun, and a stocky male water technician in his fifties with a mustache",
        "a charge nurse in her late twenties with shoulder-length wavy hair, and a male physician in his forties with glasses and a shaved head",
        "a man in his sixties with a round face and short white hair, and his adult daughter with a side braid",
        "four staff: a tall male nurse, a petite older woman nurse, a young woman nursing assistant, a heavyset male driver",
        "a woman nurse in her fifties with short permed hair and a male patient in his forties with a beard",
        "a male nurse in his thirties with round glasses, a woman nurse with a head scarf, and patients of mixed ages",
        "a slim male biomedical technician in his twenties with curly hair and a headlamp, and a woman nurse seen through a window",
        "two staff: a woman with cropped hair and a young man with a fade haircut, both in N95 masks",
        "a woman nurse in her forties with a low ponytail on the phone, and an older male physician with silver hair",
        "a head nurse in her fifties with a gray-streaked bob, and a young water technician with a goatee",
        "a mixed team of six around a table: technician, two nurses, nursing assistant, physician and a facilitator in her sixties"]


def hero(i, fname, title, scene, purpose):
    arch, cam = ROT[i % len(ROT)]
    cast = CAST[i % len(CAST)]
    return f"""### {title}

Teaching purpose: Appreciate. {purpose}

```
FILE NAME: {fname}
IMAGE TYPE: Circular vignette hero v3 (williamriveromd-hero-vignette, Scaffold A people)
ASPECT RATIO: 1:1 (displayed inside an 85–90% inscribed circle with white margin)
PIXEL DIMENSIONS: 2048 × 2048
COMPOSITION ARCHETYPE: {arch}
CAMERA: {cam}
HUMAN VARIATION: new cast: {cast}; at least 12 traits differ from the previous hero
AUDIENCE: the whole dialysis unit team, from nursing assistants to owners

PROMPT:
Square 1:1 semi-photorealistic editorial illustration on a 2048×2048 canvas (painterly-realistic, not flat vector), composed for a CIRCULAR vignette occupying 85–90% of the canvas diameter with a visible WHITE BORDER around the full circle (the circle never touches the canvas edges). Composition archetype: {arch}. Camera: {cam}.
People: Filipino, {cast}; calm, capable, prepared expressions.
Scene: {scene} Philippine setting, believable details, bright enough to read the scene even under storm or night light. The mood is readiness, not catastrophe.
Visual hierarchy: hero subject 60–70% of the circle; 2–4 supporting elements 20–30%; reserve a 20–25% TITLE SAFE ZONE of soft sky, wall or blurred background on one side.
Color grade harmonizing with teal #1a6b72 and navy #0f1e2e. No rectangular borders, frames or banners.
Absolutely NO text of any kind: no title, caption, label, readable sign, screen text, logo or watermark.

NEGATIVE INSTRUCTIONS:
{NEG_HERO}

QUALITY CHECK:
Square 2048×2048; circle 85–90% with white margin, never cropped; one dominant subject; 20–25% empty title-safe zone; Filipino people and setting; nobody injured; no text anywhere.
```
"""


def fig(idx, f):
    mod, stem, typ, purpose, content, cap, locks = f
    png = f"{HUB}-{mod}-{stem}.png"
    size, ratio = SIZE.get(typ, ("1792 × 1024", "16:9 landscape"))
    pos = "bottom-center" if "portrait" in ratio else "bottom-right"
    lock_txt = "".join("\n" + LOCKS[k] for k in locks.split() if k in LOCKS)
    qa = ["□ Light background; semi-photorealistic, not flat vector", "□ Every label spelled exactly as written, American English, Inter",
          "□ No numbers except those in CONTENT", "□ No seals, logos, real names or readable patient data", "□ Nobody injured; no blood, bodies or panic",
          f"□ Attribution renalcarematters.com at the {pos}, small, navy, 70% opacity, exact lowercase"]
    if "orig" in locks:
        qa.append("□ Original layout: does not look like any official chart or form")
    if "circuit" in locks:
        qa.append("□ Circuit: red arterial line with the pump, blood at the dialyzer end ports, dialysate at the side ports, blue venous return")
    qa = "\n".join(qa)
    return f"""### DP-F{idx:02d} · {stem}

Placement: {"Course home" if mod == "00" else f"Module {int(mod)}"} · Teaching purpose: **{purpose}** · Teaches: {cap}

```
FILE NAME: {png}   (convert to {png[:-4]}.webp for the site)
IMAGE TYPE: {typ} — {SCAFFOLD[typ]}
ASPECT RATIO: {ratio}
PIXEL DIMENSIONS: {size}
AUDIENCE: the whole dialysis unit team (plain enough for nursing assistants and support staff)
VISUAL GOAL: {cap}

PROMPT:
Clean education figure in the renalcarematters.com house style, semi-photorealistic illustration with soft shading (not flat vector clip art, not cartoon). White (#ffffff) background with soft gray (#f3f4f6) or light teal (#eef6f7) cards. Title-free (the page caption carries the message); short labels only, in Inter, navy #0f1e2e, with teal #1a6b72 headings, green #1f7a4d for safe actions, amber #b8860b for cautions and red #b91c1c for danger. Filipino people and settings where people appear. Generous whitespace, readable on a phone.
CONTENT: {content}{lock_txt}
Attribution: "renalcarematters.com" in small semi-transparent navy text (70% opacity) at the {pos}, exactly lowercase, clear of all content.

NEGATIVE INSTRUCTIONS:
{NEG_FIG}

QUALITY CHECK:
{qa}
```
"""


def tile(name, fname, scene):
    return f"""### {name}

```
FILE NAME: {fname}
IMAGE TYPE: Tile (illustrated scene, no text) — williamriveromd-infographic-skill
ASPECT RATIO: 16:9 landscape
PIXEL DIMENSIONS: 1536 × 864
PROMPT:
Semi-photorealistic illustrated editorial scene in the renalcarematters.com house style (painterly-realistic, not flat vector). Bright, airy, light overall; colors harmonizing with teal #1a6b72 and navy #0f1e2e. One clear subject centered with a safe margin on all sides (tiles are cropped to 16:9 and to a 4:3 thumbnail). Filipino people where shown, a new cast for every tile. Scene: {scene} Absolutely no text, readable signs, logos or watermarks.
NEGATIVE: dark backgrounds, clutter, collage, readable text, injured people, blood, panic, devastation, cartoon style, HDR, distorted hands or faces.
QUALITY CHECK: reads as one idea at 320 px wide; no text; light enough to read; subject inside the safe margin.
```
"""


OG = """### {title}

```
FILE NAME: {slug}-og.png → save as images/og/{slug}-og.jpg (JPEG, 1200 × 630, ≤ 300 KB)
IMAGE TYPE: OG / social share card with text — williamriveromd-infographic-skill
ASPECT RATIO: 1.91:1
PIXEL DIMENSIONS: 1200 × 630
PROMPT:
Clean social share card, white (#ffffff) background, Inter font only, generous margins. LEFT 55%: a small teal (#1a6b72) uppercase eyebrow "{eyebrow}", a large bold navy (#0f1e2e) title on at most two lines "{head}", a navy subtitle "{sub}", and three small rounded chips with teal outlines reading {chips}. RIGHT 45%: {art}, semi-photorealistic, softly lit, on a light teal (#eef6f7) rounded panel that bleeds off the right edge. Small "renalcarematters.com" in semi-transparent navy (70% opacity) at the bottom-left under the chips, exactly lowercase.
NEGATIVE: dark backgrounds, misspelled words, any text beyond the words given, government seals, logos, clutter, serif fonts, injured people, devastation.
QUALITY CHECK: exactly 1200 × 630; every word spelled exactly as given; attribution present; readable at 600 px wide; key content inside the central 1100 × 560.
```
"""


def main(out):
    L = [f"""# Disaster Preparedness and Response · Image Plan Blueprint and GPT Prompt Pack

Renal Care Academy → Emergency Readiness → Disaster Preparedness and Response (`academy/{HUB}.html`). Prepared November 28, 2026 from `DISASTER_PREPAREDNESS_BLUEPRINT.md` v1.1. Generated by `tools/techcourses/disaster/build_image_prompts.py`; when the course package is built, its figure list uses these exact file names. **The course is a DRAFT pending clinical sign-off; nothing in these images says "draft", so nothing needs remaking afterward.**

## 1. Aim

Every image should help the unit team do one of three things better:

- **Understand** why a disaster harms dialysis patients twice, how one failure drags others with it, and why the order of actions matters.
- **Apply** the plan: protect in place, take off or stay, RACE, the census, blood return without power, the signed water release, the priority roster, the five restart gates, the tabletop exercise.
- **Appreciate** what a prepared Filipino dialysis team looks like before, during and after a typhoon, an earthquake, a fire or ashfall.

## 2. Guardrails carried into every prompt

- **Readiness, not catastrophe.** No injured people, blood, bodies, flames on people, panic or devastation. Storm, flood and ash scenes stay bright enough to read.
- **Patients never disconnect themselves** (Dr. Rivero's decision): every image shows patients staying connected and staff doing take-off.
- **Original layouts only.** No government, PAGASA, DOH, OCD or hospital chart, seal or form is imitated. Decision figures use algorithm-generator Style Mode C.
- **Numbers only where the module states them.** The diet figure carries no amounts (the dietitian's plan sets them); the evidence card carries one number.
- **Dialysis truth.** Any drawn circuit follows the dialysis-circuit-schematic lock.
- **House style.** Light backgrounds, Inter, American English, short labels; attribution `renalcarematters.com` on every figure and share card (heroes and tiles carry no text by design). Semi-photorealistic, never flat vector.
- **People.** A new Filipino cast for every hero and tile.

## 3. Inventory

| Set | Count | Size | Where it lands |
|---|---|---|---|
| Circular-vignette heroes | 13 (course home + 12 modules) | 2048 × 2048 | `images/{HUB}[-NN-slug]-vignette-hero.webp` |
| Teaching figures | {len(FIGS)} | 1792 × 1024, 1024 × 1536, 1536 × 1152 | `images/{HUB}-NN-*.webp` |
| Tiles | 15 (Academy landing tile, course-home card, 12 module cards, Practice tools tile) | 1536 × 864 | `images/academy/landing/{HUB}.webp`, `images/{HUB}-card.webp`, `images/{HUB}-NN-card.webp`, `images/{HUB}-practice-card.webp` |
| OG share cards with text | 17 (course-home art + 12 modules + final exam, trainer, pre-test, practice tools) | 1536 × 1024 art / 1200 × 630 cards | `images/academy/og-art/{HUB}.png`; `images/og/<page>-og.jpg` |

## 4. Figure map

| ID | Module | Type | Purpose | What it teaches | File |
|---|---|---|---|---|---|"""]
    for i, f in enumerate(FIGS):
        L.append(f"| DP-F{i:02d} | {'Home' if f[0] == '00' else int(f[0])} | {f[2]} | {f[3]} | {f[5]} | `{HUB}-{f[0]}-{f[1]}.png` |")
    L.append(f"""
## 5. Production workflow

1. Paste one fenced block at a time into ChatGPT image generation and save each PNG under its FILE NAME, into `~/Downloads/Disaster Preparedness/images/` (regenerated replacements in `images/Corrected/`).
2. Suggested order: the heroes and tiles first, then Modules 6, 7 and 8 (earthquake, fire, power), which carry the most practical weight.
3. Claude audits each image against its QUALITY CHECK, converts it to WebP and places it when the course is built.

---

## Part 1 · Heroes (13)
""")
    L.append(hero(0, f"{HUB}-vignette-hero.png", "Course home (the final exam, trainer and pre-test pages reuse it)", HUB_SCENE,
                  "Before the season: a unit getting ready, not a unit in ruins."))
    for i, m in enumerate(MODS, 1):
        L.append(hero(i, f"{HUB}-{m[0]}-{m[1]}-vignette-hero.png", f"Module {int(m[0])} · {m[2]}", m[3], m[2] + "."))
    L.append(f"\n---\n\n## Part 2 · Teaching figures ({len(FIGS)})\n")
    for i, f in enumerate(FIGS):
        L.append(fig(i, f))
    L.append("\n---\n\n## Part 3 · Tiles (15; no text, the site sets titles in HTML)\n")
    L.append(tile("Academy landing tile", f"academy-landing-{HUB}.png → images/academy/landing/{HUB}.webp (960 × 540)",
                  "A Philippine dialysis unit seen from the street on a gray pre-typhoon afternoon, lights on, staff visible through the glass moving supplies to high shelves; a staff van parked outside; calm and ready."))
    L.append(tile("Course-home card", f"{HUB}-card.png → images/{HUB}-card.webp",
                  "Close, warm scene: hands placing a laminated emergency card, a flashlight, a power bank and a folded plan into a waterproof go-bag on a clinic counter."))
    L.append(tile("Practice tools tile", f"{HUB}-practice-card.png → images/{HUB}-practice-card.webp",
                  "A tablet on a table showing a timeline with blank inject cards beside a stopwatch, a printed unit floor plan with tokens, and a phone with a call list."))
    for m in MODS:
        L.append(tile(f"Module {int(m[0])} card · {m[2]}", f"{HUB}-{m[0]}-card.png → images/{HUB}-{m[0]}-card.webp (640 × 360)",
                      m[3] + " Wider framing than the module hero, a different camera angle and a different cast."))
    L.append("\n---\n\n## Part 4 · OG share cards (17)\n")
    L.append(f"""### Course-home share card art (text added by build_academy_og.py)

```
FILE NAME: {HUB}.png  (save to images/academy/og-art/)
IMAGE TYPE: OG card art, text-free (build_academy_og.py crops to 1200 × 630 and sets the title, track label and stats)
ASPECT RATIO: 3:2
PIXEL DIMENSIONS: 1536 × 1024
PROMPT:
Semi-photorealistic editorial illustration, bright and airy, light background. Keep the LEFT 42% of the canvas a quiet, soft off-white to light-teal gradient field with no objects (the script places text there). In the RIGHT 58%: a Filipino dialysis team preparing before a typhoon, one nurse lifting supply boxes to a high shelf, a technician at a generator panel, the head nurse with a clipboard; storm clouds through the window; calm and ready.
NEGATIVE: dark backgrounds, clutter, any text, objects in the left 42%, injured people, devastation.
QUALITY CHECK: left 42% empty and light; subject fully inside the right side; no text.
```
""")
    for m in MODS:
        slug = f"{HUB}-{m[0]}-{m[1]}"
        L.append(OG.format(title=f"Module {int(m[0])} · {m[2]}", slug=slug, eyebrow=f"DISASTER PREPAREDNESS · MODULE {int(m[0])}",
                           head=m[2], sub="Disaster Preparedness and Response · Renal Care Academy", chips=m[5], art=m[4]))
    for title, slug, eyebrow, head, sub, chips, art in [
        ("Final exam", f"{HUB}-final-exam", "DISASTER PREPAREDNESS", "End-of-Course Examination", "Disaster Preparedness and Response · timed",
         '"12 modules" · "Timed" · "Certificate of completion"', "a tablet with a multiple-choice card of four blank answer bars beside a flashlight and a folded plan"),
        ("Trainer and facilitator kit", f"{HUB}-trainer", "DISASTER PREPAREDNESS", "Facilitator Kit", "Tabletop scripts · injects · drill records",
         '"Tabletop scripts" · "Inject cards" · "After-action report"', "a stack of inject cards, a printed floor plan with tokens and a timer"),
        ("Placement pre-test", f"{HUB}-pretest", "DISASTER PREPAREDNESS", "Placement Pre-test", "Find the modules you need",
         '"Five questions a module" · "80% mastery" · "On this device"', "a tablet with a short quiz card of blank answer bars beside a pen"),
        ("Practice tools", f"{HUB}-practice", "EMERGENCY READINESS", "Disaster Drill Tools", "Tabletop simulator · call-down timer · evacuation sheet",
         '"Tabletop simulator" · "Call-down timer" · "Evacuation sheet"', "a tablet with a timeline and blank inject cards, a phone with a call list, and a stopwatch"),
    ]:
        L.append(OG.format(title=title, slug=slug, eyebrow=eyebrow, head=head, sub=sub, chips=chips, art=art))
    Path(out).write_text("\n".join(L), encoding="utf-8")
    n = sum(1 for x in L if "FILE NAME:" in x)
    print("wrote", out, len(FIGS), "figures,", n, "prompts")


if __name__ == "__main__":
    main(sys.argv[1] if len(sys.argv) > 1 else "DISASTER_PREPAREDNESS_IMAGE_PROMPTS.md")
