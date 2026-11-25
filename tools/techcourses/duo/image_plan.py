#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Dialysis Unit Owner course: image plan data and GPT prompt pack.

    python3 tools/techcourses/duo/image_plan.py [--out "<folder>"]

Writes 10-image-plan-blueprint.md (plan + every copy-paste prompt) and image-plan-manifest.json.
Prompts follow the house graphic skills: williamriveromd-hero-vignette v3 (module and course heroes, text-free 2048x2048),
williamriveromd-infographic-skill v5 (tiles, OG art, calculator OG card), williamriveromd-simple-figure and
williamriveromd-algorithm-generator-skill (teaching figures), williamriveromd-organ-crosstalk-sigil-graphic (systems sigils).
Edit the data below and re-run; do not hand-edit the generated Markdown."""
import argparse, json
from pathlib import Path

HUB = "dialysis-unit-owner"
PREPARED = "November 25, 2026"
ATTR = "© renalcarematters.com"
FONT = "Inter"

ROWS = [  # id, slug suffix, title
    ("01", "role-and-governance", "The Owner Role and the Governance Charter"),
    ("02", "kidney-care-and-patient-journey", "Kidney Care and the Patient Journey"),
    ("03", "licensing-and-compliance", "Philippine Licensing and the Compliance Register"),
    ("04", "leadership-and-clinical-authority", "Leadership Appointments and Protected Clinical Authority"),
    ("05", "ethics-and-patient-rights", "Ethics and Patient Rights in an Owner-Led Service"),
    ("06", "feasibility-and-community-access", "Feasibility and Community Access"),
    ("07", "capital-and-financing", "Capital Planning and Financing"),
    ("08", "safe-capacity-and-operating-model", "Safe Capacity and the Operating Model"),
    ("09", "facility-design-and-commissioning", "Facility Design and Commissioning"),
    ("10", "workforce-and-employment", "Workforce Investment and Employment Oversight"),
    ("11", "water-equipment-and-utilities", "Water, Equipment, and Utilities Assurance"),
    ("12", "infection-prevention-investment", "Infection Prevention and Safety Investment"),
    ("13", "procurement-and-supply-chains", "Procurement, Supply Chains, and Conflicts"),
    ("14", "philhealth-benefit-stewardship", "PhilHealth Participation and Benefit Stewardship"),
    ("15", "claims-integrity-and-revenue", "Claims Integrity and Revenue Assurance"),
    ("16", "unit-economics-and-pricing", "Unit Economics and Transparent Pricing"),
    ("17", "cash-flow-and-controls", "Cash Flow, Working Capital, and Financial Controls"),
    ("18", "quality-dashboard-and-assurance", "Quality Dashboards and Board Assurance"),
    ("19", "patient-experience-and-growth", "Patient Experience, Access, and Ethical Growth"),
    ("20", "privacy-and-cybersecurity", "Privacy, Cybersecurity, and Information Governance"),
    ("21", "disaster-and-continuity", "Disasters, Emergency Coverage, and Continuity"),
    ("22", "serious-events-and-insurance", "Serious Events, Insurance, and External Scrutiny"),
    ("23", "expansion-and-responsible-exit", "Expansion, Acquisition, Succession, and Responsible Exit"),
    ("24", "integrated-owner-capstone", "Integrated Owner Capstone and the First 90 Days"),
]

# Module hero (vignette v3): archetype, camera, scaffold, subject, supporting elements, title-safe zone, cast.
# Casts rotate so no two adjacent heroes share age band, sex, setting, framing, or wardrobe.
HERO = {
 "01": ("A Editorial Portrait", "environmental portrait, slightly low angle", "A",
        "a Filipina owner in her early fifties, short silver-streaked bob, rectangular reading glasses pushed up, rust-colored blazer over a cream blouse, standing at the head of a small boardroom table with one hand resting on a closed binder",
        "through a glass wall behind her, a softly blurred dialysis floor with a nurse at a machine; on the table a printed one-page chart of boxes and arrows, unreadable",
        "upper-left: pale clean wall and soft daylight", "woman, 50s, standing, boardroom"),
 "02": ("F Anatomy", "three-quarter cross-section", "C",
        "a single semi-photoreal pair of human kidneys with the renal arteries and veins, one kidney cut to show cortex, medulla and pelvis, beside a translucent stylized hollow-fiber dialyzer cartridge at smaller scale",
        "a faint weekly ribbon of seven pale tiles curving under the kidneys (no letters), a soft droplet motif suggesting fluid",
        "right third: soft teal-tinted gradient", "no people"),
 "03": ("I Object Hero", "top-down", "B",
        "a neat stack of official-looking folders and a ring binder with colored tab dividers, a rubber stamp and an ink pad, a desk calendar with three days circled in teal, all on a light oak desk",
        "a small potted plant, a fountain pen, a magnifying glass resting on a sheet with unreadable lines",
        "bottom-right: empty desk surface in soft light", "no people"),
 "04": ("H Clinical", "over-the-shoulder", "A",
        "a Filipino nephrologist in his late thirties with a neat undercut and thin-rimmed round glasses, white coat over a navy polo, signing a contract at a desk while a woman administrator in her forties with a long braid and a maroon cardigan reviews a second copy",
        "a framed but unreadable certificate on the wall, a stethoscope coiled on the desk, a dialysis chair glimpsed through a doorway",
        "upper-right: soft blurred clinic wall", "man late 30s + woman 40s, desk"),
 "05": ("J Environmental Storytelling", "wide-angle, eye level", "A",
        "an older Filipino man on hemodialysis in his seventies, thin build, white hair combed back, checkered short-sleeve shirt, speaking calmly with a young social worker in her twenties with a ponytail and a lanyard who is kneeling at eye level beside his chair",
        "a family member in her forties standing behind holding an umbrella and a plastic folder; the dialysis machine softly out of focus",
        "upper-left: window with bright overcast sky", "elderly man + young woman + family"),
 "06": ("D Panorama", "high wide aerial-oblique", "A",
        "a Philippine provincial town of tin and tile roofs, rice fields and a highway, with one small modern single-story clinic building at a crossroads, a tricycle and a jeepney on the road",
        "distant hills, a winding road leading away toward a faint far city, a church bell tower",
        "top third: open pale sky", "no people (small distant figures only)"),
 "07": ("I Object Hero", "macro, three-quarter", "B",
        "a calculator, a printed loan amortization sheet with unreadable columns, a pen and a set of building keys on a blueprint of a small clinic floor plan",
        "a hard hat at the edge, a cup of coffee, a ceramic piggy bank in teal",
        "upper-right: soft blurred light surface", "no people"),
 "08": ("C Radial", "overhead, directly above", "B",
        "an architectural-model style overhead view of a twelve-station dialysis floor in miniature, nine stations softly lit and active with tiny figures, three stations dimmed and empty",
        "a nurse station at the center, a small clock, a water-room doorway",
        "lower-left: plain light floor area", "tiny figures only"),
 "09": ("J Environmental Storytelling", "rear three-quarter view", "A",
        "a Filipino site engineer in his twenties, slim, buzz cut, orange safety vest over a gray shirt, holding a tablet, walking a nearly finished dialysis room with a biomedical technician woman in her thirties in a hijab and coveralls checking a wall outlet panel",
        "plastic-wrapped dialysis chairs, a water pipe loop along the wall with valves, a ladder",
        "upper-left: freshly painted pale wall", "young man + woman in hijab"),
 "10": ("E Lifestyle", "side profile, medium", "A",
        "a team huddle at shift change: a stocky Filipino male nurse in his forties with a shaved head and teal scrubs, a petite nurse in her twenties with a short pixie cut and maroon scrubs, a patient care technician in his fifties with a gray mustache, standing in a loose circle",
        "a whiteboard roster with colored magnets, unreadable; a clock showing early morning",
        "right side: soft daylight window glow", "three staff, mixed ages"),
 "11": ("I Object Hero", "low angle, three-quarter", "B",
        "a gleaming reverse osmosis water treatment skid with blue pressure vessels, carbon tanks and a stainless distribution loop in a bright clean plant room",
        "a test-strip vial and a sample bottle on a steel shelf, a backup generator glimpsed through an open door",
        "upper-right: clean white ceiling and soft light", "no people"),
 "12": ("H Clinical", "close, hands-focused", "A",
        "gloved hands of a nurse performing a scrub-the-hub disinfection on a catheter connector with an alcohol swab, the patient's chest dressing clean and dry, a sharps container at the edge",
        "a hand-hygiene dispenser on a pillar, a clean supply cart",
        "upper-left: blurred bright window", "hands only"),
 "13": ("I Object Hero", "overhead, three-quarter", "B",
        "a tidy stockroom shelf of sealed dialyzer boxes and bloodline packs with color-coded bin labels (no readable text), one box pulled forward with a lot-number sticker shown as an unreadable barcode",
        "a handheld barcode scanner, a clipboard, a temperature and humidity monitor",
        "bottom-left: empty clean shelf space", "no people"),
 "14": ("H Clinical", "environmental portrait at a counter", "A",
        "a Filipina billing officer in her thirties, round face, curly shoulder-length hair, mustard blouse, explaining a printed form to a husband and wife in their sixties at a clinic front desk; the wife holds a small notebook",
        "a numbered queue display (no numbers), a pen holder, a bottle of alcohol gel",
        "upper-right: soft pale wall", "billing officer + older couple"),
 "15": ("I Object Hero", "macro", "B",
        "two neat stacks of paper forms side by side on a desk, one slightly shorter, connected by thin teal threads to a laptop showing an abstract table, with a magnifying glass over a gap between the stacks",
        "a red pen, a yellow sticky flag, a mug",
        "top third: soft blurred background", "no people"),
 "16": ("G Infographic", "straight-on", "C",
        "a single elegant 3D bar-and-line sculpture: rising translucent teal bars for sessions crossing a gently falling navy curve for cost per treatment, with one bar stepping abruptly higher at the right",
        "a small dialysis chair icon on the base, a coin stack beside it",
        "upper-left: plain soft gradient", "no people"),
 "17": ("A Editorial Portrait", "close portrait, eye level", "A",
        "a Filipino finance officer in his late forties, heavyset, salt-and-pepper beard, white barong-style shirt with rolled sleeves, studying a wall calendar of thirteen weeks with a calm, concentrated expression",
        "an open laptop, a payroll envelope bundle, a desk fan",
        "right third: blurred pale office wall", "man late 40s, close portrait"),
 "18": ("G Infographic", "straight-on", "C",
        "a single tablet on a stand showing an abstract run chart with a steady line that suddenly shifts upward, in teal and amber, on a clean boardroom table",
        "three printed indicator cards fanned beside it, unreadable",
        "upper-right: empty soft gradient", "no people"),
 "19": ("E Lifestyle", "wide, warm daylight", "A",
        "a young Filipina patient in her late twenties with a nose stud and a denim jacket arriving at a dialysis clinic entrance on a tricycle, greeted by a receptionist in his fifties with a cane and a bright smile",
        "a ramp with handrails, potted bougainvillea, a shaded waiting bench",
        "top-left: open sky over the clinic roofline", "young woman + older male receptionist"),
 "20": ("I Object Hero", "three-quarter", "B",
        "a padlock resting on a closed laptop beside a small external backup drive and a printed paper downtime binder, on a clean nurse-station counter",
        "a faint network of glowing teal dots in the blurred background, a key on a lanyard",
        "upper-left: soft blurred light", "no people"),
 "21": ("D Panorama", "wide, from a raised walkway", "A",
        "a dialysis clinic on a flooded street after a typhoon, water at knee height outside, a small rescue boat delivering two patients to a raised entrance while a generator hums in a covered bay",
        "dark-free bright overcast sky clearing, palm trees bending, a rescue worker in an orange vest",
        "top third: brightening sky", "small figures"),
 "22": ("H Clinical", "side profile, quiet room", "A",
        "a Filipino medical director in his sixties with a receding hairline and a gray cardigan sitting with a grieving daughter in her thirties in a quiet family room, both leaning slightly forward, a box of tissues between them",
        "a small window with a curtain, a glass of water",
        "upper-right: plain soft wall", "older man + woman 30s, seated"),
 "23": ("B Journey", "high three-quarter", "A",
        "a path of three small clinic buildings growing from left to right along a road, the third larger with a construction crane, and a fork in the road where one branch leads to a handshake at a table",
        "a signpost with blank arrows, a small family walking toward the first clinic",
        "upper-left: open pale sky", "small figures"),
 "24": ("J Environmental Storytelling", "wide, eye level", "A",
        "a full governance meeting around a long table: an owner, a clinical head, a head nurse, a technician and a manager of varied ages and builds, all Filipino, one presenting a single large printed board pack while others take notes",
        "a window onto the dialysis floor, a wall clock, water glasses",
        "upper-left: bright blurred window", "five people, varied"),
}

# Module tile (card) prompt: one-line visual metaphor, text-free, 16:9.
TILE = {
 "01": "a single key on a ring hanging beside a dialysis machine's front panel, the key's shadow forming a small org chart on the wall",
 "02": "a seven-day calendar strip of pale tiles where the tile after the weekend glows amber, beside a pair of kidneys",
 "03": "a ring binder with colored tabs and a rubber stamp on a light desk",
 "04": "a pen resting on a signed contract next to a stethoscope",
 "05": "a balance scale holding a coin stack on one side and a small dialysis chair on the other, perfectly level",
 "06": "a small modern clinic at a provincial crossroads seen from above",
 "07": "a blueprint, a calculator and a set of keys",
 "08": "a miniature dialysis floor with nine lit stations and three dimmed",
 "09": "a freshly finished dialysis room with chairs still wrapped in plastic",
 "10": "four pairs of hands in different scrub colors stacked on a clipboard roster",
 "11": "a reverse osmosis water skid with blue pressure vessels",
 "12": "gloved hands swabbing a catheter connector",
 "13": "sealed dialyzer boxes on a shelf and a barcode scanner",
 "14": "a printed benefit form and a pen on a clinic counter with a patient's hands",
 "15": "two stacks of forms joined by teal threads and a magnifying glass on the gap",
 "16": "rising teal bars crossing a falling navy curve, one bar stepping higher",
 "17": "a thirteen-week wall calendar with a payroll envelope bundle",
 "18": "a tablet showing a run chart with a sudden upward shift",
 "19": "a welcoming clinic entrance with a ramp and bougainvillea",
 "20": "a padlock on a closed laptop beside a backup drive and a paper binder",
 "21": "a clinic on a flooded street with a generator bay and a rescue boat",
 "22": "a quiet family room with two chairs and a box of tissues",
 "23": "three clinic buildings growing along a road toward a fork",
 "24": "a board pack on a long table surrounded by five note pads",
}

# Teaching figures: key, title, skill/kind, canvas, job (understanding it builds), layout, labels (verbatim), truth.
# kind: algo (algorithm skill, portrait) | compare | sequence | mechanism | card | sigil | scene
FIGS = {
 "01": [
  ("a", "decision-rights-map", "Who decides what: the owner's map of authority", "sigil", "1792x1024",
   "Shows at a glance that ownership supplies resources and assurance while clinical, nursing and technical decisions stay with qualified people; the owner's line to the patient runs through them, never around them.",
   "Five rounded role tiles arranged around a central patient icon: Owner / governing body (top), Clinical head (left), Nursing lead (bottom-left), Technical lead (bottom-right), Unit manager (right). Solid teal arrows from Owner to each role labeled with what flows down; dotted navy arrows from each role back up labeled 'Assurance'. Only the clinical, nursing and technical tiles connect to the patient.",
   ["Owner / governing body", "Clinical head", "Nursing lead", "Technical lead", "Unit manager", "Patient", "Resources · appointments · budget", "Assurance", "Prescriptions", "Assignments", "Water and machine release"],
   "No arrow from Owner directly to Patient. Owner tile is the same size as the others, not larger."),
  ("b", "assurance-ladder", "From promise to proof: the assurance ladder", "card", "1536x1152",
   "Teaches owners to rank the evidence they are given, so a verbal reassurance is never mistaken for a working control.",
   "A five-rung vertical ladder, bottom to top, each rung a rounded card with a small illustrated object: a speech bubble, a written policy page, a signed roster, a completed checklist with dates, a re-audit chart showing the problem stayed fixed. A side bar fills from amber (weak) at the bottom to green (strong) at the top.",
   ["Weak", "Strong", "\"The staff know what to do\"", "A written policy", "A current roster and competency record", "A signed record that the check was done", "A re-audit showing the fix worked"],
   "Exactly five rungs. No percentages or scores."),
 ],
 "02": [
  ("a", "week-sawtooth", "Why three sessions a week, and why the long gap matters", "mechanism", "1792x1024",
   "Makes the long interdialytic gap visible: wastes and fluid rise between sessions and fall during them, and the climb after the two-day weekend gap is the tallest.",
   "A clean horizontal timeline Monday to Sunday with three short teal 'Dialysis' bars (Mon, Wed, Fri). Above it a smooth sawtooth line labeled 'Fluid and wastes in the body' rising between sessions and dropping during each, with the Friday-to-Monday climb visibly highest and shaded amber. A small kidney icon at left labeled 'A healthy kidney works every hour'. A callout at the Monday peak.",
   ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun", "Dialysis", "Fluid and wastes in the body", "A healthy kidney works every hour", "Long gap: highest risk the day after"],
   "Sawtooth is schematic: no y-axis numbers. Three sessions only."),
  ("b", "patient-journey", "The patient journey an owner's service must serve", "sequence", "1792x1024",
   "Places the dialysis unit inside a longer journey, so owners see that referral for transplant, home dialysis or conservative care is part of good service, not lost revenue.",
   "A left-to-right journey path with six milestone cards: CKD clinic, Preparing for kidney failure, Starting hemodialysis, Living on dialysis, then a fork into three equal cards: Kidney transplant, Home or peritoneal dialysis, Supportive conservative care. A teal ribbon labeled 'Your unit' spans only the middle cards. A small Filipino patient figure walks the path.",
   ["CKD clinic", "Preparing for kidney failure", "Starting hemodialysis", "Living on dialysis", "Kidney transplant", "Home or peritoneal dialysis", "Supportive conservative care", "Your unit"],
   "The three branches are drawn the same size. No arrows back from transplant to the unit."),
 ],
 "03": [
  ("a", "compliance-layers", "Four layers that must all be current", "card", "1536x1152",
   "Separates the license, the payer accreditation, the society attestation and local permits, so owners stop treating one as proof of the others.",
   "Four stacked translucent rounded layers like floors of a building, each with an icon and short label: DOH license (building with a seal), PhilHealth accreditation (card), PSN attestation (certificate with ribbon), Local permits (fire extinguisher, business permit, waste). A small dialysis chair sits on the top floor. A note at the side: 'Each expires on its own date'.",
   ["DOH license", "PhilHealth accreditation", "PSN attestation", "Local permits: business, fire, sanitation, waste", "Each expires on its own date", "Owner checks all four"],
   "No dates or numbers. Equal visual weight for all four layers."),
  ("b", "register-lifecycle", "The compliance register: from requirement to proof", "sequence", "1792x1024",
   "Shows the life of one requirement through the register, so an owner can ask for the evidence, the owner and the expiry of each line.",
   "A circular workflow of five steps around a central ring binder: Requirement identified, Evidence filed, Named owner, Expiry alert set, Re-checked and signed. A small branch off the loop labeled 'Rule changed? Change-control log'.",
   ["Requirement identified", "Evidence filed", "Named owner", "Expiry alert set", "Re-checked and signed", "Rule changed? Change-control log"],
   "Exactly five steps in the loop."),
 ],
 "04": [
  ("a", "appointment-checklist", "Appointing leaders the right way", "card", "1536x1152",
   "Turns a leadership appointment into checkable items, including the clauses that protect clinical judgment from commercial pressure.",
   "A clipboard-style reference card with two columns of checkbox rows. Left column heading 'Before appointing': Credentials verified, Scope and sites written, Time commitment realistic, Conflicts declared. Right column heading 'In the contract': Clinical decisions protected, Authority to stop unsafe care, No penalty for reporting, Substitute named.",
   ["Before appointing", "Credentials verified", "Scope and sites written", "Time commitment realistic", "Conflicts declared", "In the contract", "Clinical decisions protected", "Authority to stop unsafe care", "No penalty for reporting", "Substitute named"],
   "Checkboxes empty. No signatures or names."),
  ("b", "protected-authority", "The protected line", "compare", "1792x1024",
   "Contrasts what an owner may decide with what an owner may not override, using one example on each side.",
   "Two panels split by a dashed line. Left panel (green header 'The owner may'): fund a second nurse, approve a repair, change opening hours with notice. Right panel (red header 'The owner may not'): restart a held machine, change a prescription, release water, end isolation. Small illustrated icon per item.",
   ["The owner may", "Fund staff and repairs", "Approve budgets and hours", "Appoint and evaluate leaders", "The owner may not", "Restart a held machine", "Change a prescription", "Release water", "End isolation precautions"],
   "Left header renal green, right header clinical red."),
 ],
 "05": [
  ("a", "incentive-chain", "How an incentive becomes a patient outcome", "mechanism", "1792x1024",
   "Gives owners the causal chain the evidence describes: a payment rule changes behavior, behavior changes care, care changes outcomes. Draws on observational studies of ownership and dosing.",
   "Left-to-right chain of four rounded cards joined by arrows: Payment or bonus rule, Staff and facility behavior, Care delivered, Patient outcome. Under each card a pair of small examples: 'Bonus per filled chair' -> 'Schedule full, no make-up slots' -> 'Missed sessions not rescheduled' -> 'More hospital stays'. A green alternative row below: 'Bonus for completed sessions and closed actions' -> 'Make-up slots kept' -> 'Sessions rescheduled' -> 'Fewer gaps'.",
   ["Payment or bonus rule", "Behavior", "Care delivered", "Patient outcome", "Bonus per filled chair", "No make-up slots", "Missed sessions not rescheduled", "More hospital stays", "Bonus for completed sessions", "Make-up slots kept", "Sessions rescheduled", "Fewer gaps"],
   "Label the bottom row in renal green and the top row in amber. No statistics."),
  ("b", "grievance-flow", "From complaint to fixed system", "algo", "1024x1536",
   "Shows the path every grievance takes to a named owner and a system fix, with the safety branch first.",
   "Top-to-bottom algorithm: Complaint received -> diamond 'Immediate safety risk?' yes -> 'Act now and inform clinical head' (red); no -> 'Acknowledge within the policy time' -> 'Investigate with the patient' -> 'Decision and reason in writing' -> 'System fix and re-check' (green) -> 'Report trend to the board'. Side note box: 'No retaliation; care continues during the complaint'.",
   ["Complaint received", "Immediate safety risk?", "Yes", "No", "Act now and inform clinical head", "Acknowledge within policy time", "Investigate with the patient", "Decision and reason in writing", "System fix and re-check", "Report trend to the board", "No retaliation; care continues"],
   "No numeric time limits."),
 ],
 "06": [
  ("a", "investment-gates", "Four gates before you build", "sequence", "1792x1024",
   "Teaches staged commitment: money is released only when each gate's evidence exists.",
   "Four gate arches along a path, each with a small icon and checklist: Gate 1 Need (map pin and people), Gate 2 Staff and water (nurse and water drop), Gate 3 Money under stress (calculator with a downward arrow), Gate 4 Permits (stamp). A coin bag moves only after each gate opens.",
   ["Gate 1: Need and travel time", "Gate 2: Staff and water you can secure", "Gate 3: Money under the bad case", "Gate 4: Permits and accreditation path", "Release funds only after each gate"],
   "Four gates exactly."),
  ("b", "sensitivity-tornado", "Which assumption can sink the plan?", "card", "1536x1152",
   "Introduces sensitivity analysis visually: the widest bar is the assumption to test first.",
   "A horizontal tornado chart with five bars centered on a vertical line labeled 'Base case'. Bars from widest to narrowest: Days to collect, Sessions per month, Staff cost, Supply prices, Rent. Left half amber 'Worse', right half green 'Better'. No numeric axis.",
   ["Base case", "Worse", "Better", "Days to collect", "Sessions per month", "Staff cost", "Supply prices", "Rent", "Test the widest bar first"],
   "Schematic only, no numbers."),
 ],
 "07": [
  ("a", "sources-and-uses", "Sources and uses: every peso accounted for", "compare", "1792x1024",
   "Shows that the money raised must equal the money spent, including the reserves owners forget.",
   "Two equal-height stacked columns side by side with a balance icon between. Left 'Sources': Owner equity, Bank loan, Supplier financing. Right 'Uses': Building fit-out, Water system, Machines and chairs, Opening stock, Working capital reserve, Contingency. The two reserve blocks are highlighted teal.",
   ["Sources", "Owner equity", "Bank loan", "Supplier financing", "Uses", "Fit-out", "Water system", "Machines and chairs", "Opening stock", "Working capital reserve", "Contingency", "Sources = Uses"],
   "No peso amounts."),
  ("b", "distribution-gate", "Before any dividend: the distribution gate", "algo", "1024x1536",
   "Makes conditional distributions concrete: safety and solvency tests come before owner payouts.",
   "Top-to-bottom algorithm of four diamonds, each with a 'No -> Hold distribution' exit to the right in amber: 'Payroll and statutory remittances current?', 'Safety actions funded and on time?', 'Cash reserve at target?', 'Loan covenants met?'. Final green node: 'Distribution may be approved by the board'.",
   ["Payroll and remittances current?", "Safety actions funded?", "Cash reserve at target?", "Loan covenants met?", "No: hold distribution", "Distribution may be approved"],
   "Four diamonds, one exit each."),
 ],
 "08": [
  ("a", "capacity-funnel", "Physical capacity is not safe capacity", "mechanism", "1792x1024",
   "Visualizes the narrowing from installed stations to safely staffed slots to patients supported, with make-up slots held back.",
   "A horizontal funnel of four bands narrowing left to right: Stations installed, Stations working, Stations staffed by cleared nurses, Patients you can safely accept. A small reserved slice peels off before the last band labeled 'Kept free for make-up sessions'. Tiny chair icons inside each band decrease in number.",
   ["Stations installed", "Stations working", "Stations safely staffed", "Patients you can safely accept", "Kept free for make-up sessions", "The narrowest gate sets capacity"],
   "No numbers on the funnel."),
  ("b", "dependency-web", "The services a unit cannot run without", "sigil", "1792x1024",
   "Shows the external dependencies an owner must secure by written agreement before accepting patients.",
   "A central dialysis chair icon with seven monoline icons around it joined by dotted lines: Hospital for emergencies, Laboratory, Ambulance, Vascular access surgeon, Water testing laboratory, Machine service, Power and water utilities. Each dotted line carries a small document icon.",
   ["Hospital", "Laboratory", "Ambulance", "Access surgeon", "Water testing", "Machine service", "Power and water", "Written agreement for each"],
   "Monoline sigil style, light background."),
 ],
 "09": [
  ("a", "zones-floorplan", "Clean, patient and support zones", "mechanism", "1792x1024",
   "Teaches why layout is an infection and safety control: separate flows, a visible isolation area, and a water room close to the floor.",
   "A simplified top-down floor plan in soft pastel zones: patient treatment floor with chairs (light teal), isolation room with its own sink (amber outline), clean supply room (green), soiled utility and waste (gray), water treatment room (blue), nurse station with clear sightlines to every chair (dotted sightline rays). Arrows show patient entry and waste exit on separate paths.",
   ["Treatment floor", "Isolation room", "Clean supply", "Soiled utility and waste", "Water treatment room", "Nurse station sightlines", "Patient entry", "Waste exit"],
   "No dimensions. Follow, do not quote, the DOH design guidelines."),
  ("b", "launch-gate", "Commissioning: the launch gate", "algo", "1024x1536",
   "Shows that opening day depends on tested systems, not finished construction.",
   "Top-to-bottom algorithm with five sequential checks, each with a red 'Not yet: do not open' exit: 'Water validated and released by technical lead?', 'Machines tested and logged?', 'Staff competencies signed?', 'Emergency drill done?', 'License and permits issued?'. Final green node 'Open with first patients'.",
   ["Water validated and released?", "Machines tested and logged?", "Staff competencies signed?", "Emergency drill done?", "License and permits issued?", "Not yet: do not open", "Open with first patients"],
   "Water release is the technical lead's, not the owner's."),
 ],
 "10": [
  ("a", "staffing-chain", "From staffing to outcomes", "mechanism", "1792x1024",
   "Traces how staffing level and skill mix act through care processes to outcomes, as observational studies associate them.",
   "Three linked columns: Staffing (patients per nurse, skill mix, fatigue), Care processes (assessments done, alarms answered, teaching given, care left undone), Patient outcomes (hospital stays, deaths, transplant referral). Arrows between columns, a dotted note 'Observational evidence: associations, not proof'.",
   ["Staffing", "Patients per nurse", "Skill mix", "Fatigue", "Care processes", "Assessments done", "Alarms answered", "Care left undone", "Patient outcomes", "Hospital stays", "Deaths", "Transplant referral", "Observational evidence: associations"],
   "No numbers."),
  ("b", "fte-relief", "Why one post needs more than one person", "card", "1536x1152",
   "Explains full-time equivalents and the relief factor with a simple visual of one chair-side post across a week.",
   "A week grid of shifts for one post, filled by colored person icons; extra icons labeled 'Leave', 'Training', 'Sick' fill gaps. A formula strip at the bottom in large type: 'FTE = posts × shifts × hours ÷ contracted hours, then add relief'.",
   ["One post, every shift", "Leave", "Training", "Sick", "FTE = posts × shifts × hours ÷ contracted hours", "then add relief"],
   "No numbers other than the formula words."),
 ],
 "11": [
  ("a", "water-pathway", "Dialysis water: pathway, tests and the hold", "mechanism", "1792x1024",
   "Shows why roughly a bathtub of water per session must be purer than drinking water, where it is tested, and that the technical lead, not the owner, releases it.",
   "Left-to-right water pathway as clean 3D-rendered components: city water, sediment filter, softener, two carbon tanks in series, reverse osmosis, storage or direct loop, dialysis machines. Test-tube markers at carbon outlet ('Chlorine'), loop ('Bacteria and endotoxin'), product water ('Chemical contaminants'). A red stop sign gate before the machines: 'Held until released by technical lead'.",
   ["City water", "Sediment filter", "Softener", "Carbon tanks", "Reverse osmosis", "Distribution loop", "Dialysis machines", "Chlorine", "Bacteria and endotoxin", "Chemical contaminants", "Held until released by technical lead"],
   "Two carbon tanks in series. No numeric limits."),
  ("b", "asset-lifecycle", "Every machine has a life cycle", "sequence", "1792x1024",
   "Teaches owners to budget for the whole life of equipment, not only the purchase.",
   "Circular cycle around a dialysis machine: Specify, Buy and receive, Commission and test, Preventive maintenance, Repair and recall, Retire and replace. A small budget coin beside the maintenance and replace steps labeled 'Budget every year'.",
   ["Specify", "Buy and receive", "Commission and test", "Preventive maintenance", "Repair and recall", "Retire and replace", "Budget every year"],
   "Generic machine, no brand."),
 ],
 "12": [
  ("a", "bsi-pathway", "How a bloodstream infection reaches a dialysis patient", "mechanism", "1792x1024",
   "Shows the routes of entry and the matching core interventions, so an owner sees what each funded control blocks.",
   "Center: a patient silhouette with a chest catheter and an arm fistula. Three entry routes drawn as amber arrows: hands, catheter hub, skin at the needle site. Each route blocked by a teal shield labeled with its control. Bottom strip: 'Catheters carry the highest risk: plan a fistula or graft'.",
   ["Hands", "Catheter hub", "Skin at the needle site", "Hand hygiene audits", "Scrub the hub", "Skin antisepsis", "Track infections monthly", "Catheters carry the highest risk"],
   "No blood or wounds shown graphically."),
  ("b", "outbreak-governance", "Two infections in a month: the governance response", "algo", "1024x1536",
   "Gives the owner's part of an outbreak response: resources and reporting, while clinicians lead the clinical work.",
   "Top-to-bottom algorithm: 'Cluster suspected' -> 'Clinical head leads investigation' -> 'Owner releases resources now' (staff, supplies, audits) -> 'Report as required' -> 'Audit hand hygiene, hub care, isolation' -> 'Re-check rates for three months' -> 'Close with evidence'. Side box: 'Do not hide or delay reporting'.",
   ["Cluster suspected", "Clinical head leads investigation", "Owner releases resources now", "Report as required", "Audit hands, hubs, isolation", "Re-check rates", "Close with evidence", "Do not delay reporting"],
   "Clinical steps belong to the clinical head."),
 ],
 "13": [
  ("a", "qualification-gates", "Qualifying a cheaper substitute", "sequence", "1792x1024",
   "Makes the five checks a new product must pass before patient use, whoever the supplier is.",
   "Five gates along a conveyor carrying a dialyzer box: FDA registration for this use, Technical compatibility, Clinical review, Staff training, Lot traceability. A side lane labeled 'Related supplier? Declare and recuse' with a person stepping aside.",
   ["FDA registration", "Technical fit", "Clinical review", "Staff training", "Lot traceability", "Related supplier? Declare and recuse"],
   "FDA means FDA Philippines; no brand names."),
  ("b", "recall-trace", "One-hour recall: from lot number to patient", "sequence", "1792x1024",
   "Shows why lot traceability is a safety system: a recall must find every affected patient fast.",
   "Left-to-right: a recall notice, the stock record with a highlighted lot, the treatment records listing which chairs used it, three patient chair icons highlighted, and a phone icon 'Physician informs patients'. A stopwatch icon labeled 'Within one hour'.",
   ["Recall notice", "Stock record by lot", "Treatment records", "Affected patients", "Physician informs patients", "Within one hour"],
   "No real lot numbers."),
 ],
 "14": [
  ("a", "benefit-chain", "From a session to a PhilHealth payment", "sequence", "1792x1024",
   "Shows the conditions that must all hold for a session to be paid, so owners stop treating the package as guaranteed revenue.",
   "Six linked tiles: Eligible member registered in the dialysis database, Accredited facility, Session delivered and documented, Agreement form signed, Claim filed on time, Payment received. A ribbon underneath: 'Package: 6,350 pesos per session, facility and professional fees included, up to 156 sessions a year'.",
   ["Eligible member in PDD", "Accredited facility", "Session delivered and documented", "Agreement form signed", "Claim filed on time", "Payment received", "6,350 pesos per session · facility and professional fees included · up to 156 sessions a year"],
   "Write the package line exactly as given."),
  ("b", "charge-matrix", "What the patient pays: tell them before the first session", "card", "1536x1152",
   "Helps owners present charges honestly: the package, any permitted co-payment, and sessions beyond the limit.",
   "A reference card with three rows and a patient-and-family illustration at the top. Rows: 'Covered session: no co-payment for covered services', 'Specified additional professional service: co-payment only as the circular allows, written on the form', 'Beyond the yearly limit: full charge unless other support'. Footer: 'Written estimate before the first session'.",
   ["Covered session", "No co-payment for covered services", "Additional professional service", "Only as the circular allows, on the form", "Beyond the yearly limit", "Full charge unless other support", "Written estimate before the first session"],
   "No peso amounts."),
 ],
 "15": [
  ("a", "reconciliation-funnel", "Session-to-cash reconciliation", "mechanism", "1792x1024",
   "Visualizes leakage: sessions delivered, documented, claimed, accepted, paid, with the gap at each step named.",
   "A horizontal funnel of five bands: Sessions delivered, Fully documented, Claimed, Accepted, Paid. Between bands small amber drops with labels of why sessions fall out: missing signature, late filing, eligibility, returned claim.",
   ["Sessions delivered", "Fully documented", "Claimed", "Accepted", "Paid", "Missing signature", "Filed late", "Eligibility", "Returned claim", "Fix the cause, not the number"],
   "No numbers."),
  ("b", "integrity-line", "The integrity line", "compare", "1792x1024",
   "Contrasts lawful correction of a claim with conduct that is never acceptable.",
   "Two panels. Left green 'Correct and resubmit': complete missing documentation that reflects what happened, refile within the period, log the exception. Right red 'Never': claim a session not delivered, change a date or diagnosis to fit the rules, charge a patient for what the package covers.",
   ["Correct and resubmit", "Complete true documentation", "Refile within the period", "Log the exception", "Never", "Claim an undelivered session", "Change dates or diagnoses", "Charge for what is covered"],
   ""),
 ],
 "16": [
  ("a", "cost-curve", "Cost per treatment falls with volume, then steps", "mechanism", "1792x1024",
   "Shows fixed, variable and step costs and why cost per treatment is a curve, not a constant.",
   "A clean chart: x-axis 'Sessions per month', y-axis 'Cost per treatment'. A smooth falling navy curve with a sudden upward jump at a step marked by a small nurse-team icon labeled 'New shift: step cost'. Under the chart three cost-type cards: Fixed, Variable, Step.",
   ["Sessions per month", "Cost per treatment", "New shift: step cost", "Fixed: rent, core salaries", "Variable: dialyzer, lines, drugs", "Step: a new team or shift"],
   "No numbers on axes."),
  ("b", "breakeven", "Contribution and break-even", "card", "1536x1152",
   "Gives the two formulas owners use most, with the rule that a negative contribution has no break-even.",
   "Reference card with two large formula strips and a small bar diagram: one session bar split into 'Variable cost' and 'Contribution'. Formulas: 'Contribution = net revenue − variable cost per session' and 'Break-even sessions = fixed cost ÷ contribution'. Red note: 'Contribution zero or negative: no volume breaks even'.",
   ["Variable cost", "Contribution", "Contribution = net revenue − variable cost", "Break-even = fixed cost ÷ contribution", "Contribution zero or negative: no volume breaks even"],
   ""),
 ],
 "17": [
  ("a", "cash-waterfall", "Profit is not cash", "mechanism", "1792x1024",
   "Shows the timing gap between a delivered session and cash in the bank, and the working capital that gap needs.",
   "A timeline from 'Session delivered' to 'Cash received' with a long bridge labeled 'Days to collect'. Under the bridge, stacked coin columns labeled 'Payroll', 'Suppliers', 'Loan' leave the bank before cash arrives. A water-tank metaphor at the right labeled 'Working capital' with a gauge.",
   ["Session delivered", "Claim filed", "Cash received", "Days to collect", "Payroll", "Suppliers", "Loan", "Working capital"],
   "Explain that the tank is a metaphor only by keeping it stylized."),
  ("b", "controls-quad", "Four controls that stop money going missing", "card", "1536x1152",
   "Introduces segregation of duties and the simplest bank controls owners can demand.",
   "Four equal tiles: 'Two signatures for payments', 'The person who orders does not pay', 'Monthly bank reconciliation by someone else', 'Payroll and remittances first'. Each tile with a small icon.",
   ["Two signatures for payments", "Orders and payments split", "Bank reconciliation by someone else", "Payroll and remittances first"],
   ""),
 ],
 "18": [
  ("a", "run-chart", "Read the trend, not the month", "mechanism", "1792x1024",
   "Teaches the run chart: a shift of several points on one side of the median is a signal; one bad month usually is not.",
   "A clean run chart with a gray median line, monthly dots, and a highlighted run of six consecutive dots above the median shaded amber labeled 'Shift: investigate'. A single high dot earlier labeled 'One point: watch'. Axis labels only.",
   ["Month", "Rate", "Median", "One point: watch", "Six in a row on one side: investigate"],
   "No numeric axis values."),
  ("b", "board-dashboard", "A board dashboard that drives action", "card", "1536x1152",
   "Shows the five columns every indicator row needs so a dashboard leads to a decision.",
   "A table-style reference card with five column headers and two illustrative rows using words only: Indicator with denominator, Trend, Interpretation, Action owner and date, Proof it worked. Example rows: 'Catheter infections per 1,000 catheter-days' and 'Missed sessions per 100 scheduled'.",
   ["Indicator and denominator", "Trend", "Interpretation", "Action, owner, date", "Proof it worked", "Catheter infections per 1,000 catheter-days", "Missed sessions per 100 scheduled"],
   "No values in cells; use short dashes."),
 ],
 "19": [
  ("a", "experience-loop", "Hearing every patient, not only the healthy ones", "sigil", "1792x1024",
   "Explains that surveys under-represent the sickest patients, so experience data need other channels.",
   "A circular loop of four monoline icons: Survey, Bedside conversation, Complaint and compliment log, Family meeting, around a central patient chair. A small dotted figure lying in a bed outside the loop labeled 'The sickest often do not answer surveys' with an arrow inviting them in.",
   ["Survey", "Bedside conversation", "Complaint and compliment log", "Family meeting", "The sickest often do not answer surveys"],
   ""),
  ("b", "marketing-check", "Marketing review: four questions", "card", "1536x1152",
   "Gives owners a quick test for any advertisement or referral arrangement.",
   "Four question cards in a 2x2 grid with a magnifying glass icon: 'Is every claim true and current?', 'Does it promise what the package covers as free?', 'Does it pay or reward referrals?', 'Can we serve the patients it attracts safely?'.",
   ["Every claim true and current?", "Covered care presented as free?", "Rewards for referrals?", "Capacity to serve them safely?"],
   ""),
 ],
 "20": [
  ("a", "ransomware-impact", "When the computers stop", "mechanism", "1792x1024",
   "Shows how one attack spreads from data to care, and which preparation breaks each link.",
   "Left-to-right chain: Phishing email, Systems encrypted, Records and schedules unavailable, Sessions delayed or cancelled. Under each link a teal shield: Training and two-step login, Offline backups tested, Paper downtime kit, Transfer agreements.",
   ["Phishing email", "Systems encrypted", "Records unavailable", "Sessions delayed", "Training and two-step login", "Offline backups tested", "Paper downtime kit", "Transfer agreements"],
   ""),
  ("b", "access-matrix", "Who may see what", "card", "1536x1152",
   "Turns the need-to-know rule into a simple access matrix the owner can approve.",
   "A grid with roles as rows (Owner, Manager, Nurse, Billing, Vendor) and data types as columns (Board reports, Patient charts, Claims, Payroll). Cells use three icons: green check 'Yes', amber half-circle 'Limited', red cross 'No'. The Owner row shows green only for Board reports.",
   ["Owner", "Manager", "Nurse", "Billing", "Vendor", "Board reports", "Patient charts", "Claims", "Payroll", "Yes", "Limited", "No"],
   "Owner: Board reports yes; Patient charts no."),
 ],
 "21": [
  ("a", "continuity-map", "Typhoon continuity: what must keep running", "sigil", "1792x1024",
   "Shows the dependencies a dialysis session needs during a disaster and the backup for each.",
   "Central dialysis chair with six dependency icons around it, each paired with its backup: Power -> Generator and fuel, Water -> Stored treated water plan, Staff -> Call tree and housing, Supplies -> Two weeks' stock, Patients -> Contact list and transport, Records -> Paper kit. Dotted lines.",
   ["Power", "Generator and fuel", "Water", "Treated water plan", "Staff", "Call tree", "Supplies", "Extra stock", "Patients", "Contact list and transport", "Records", "Paper kit"],
   ""),
  ("b", "restart-gate", "Before reopening after a disaster", "algo", "1024x1536",
   "Prevents an unsafe restart: the same release logic as opening day.",
   "Top-to-bottom algorithm: 'Building safe?' -> 'Power stable?' -> 'Water tested and released by technical lead?' -> 'Machines checked?' -> 'Enough staff?' -> green 'Reopen: physician-led triage'. Each 'No' exits to amber 'Keep transfers going'.",
   ["Building safe?", "Power stable?", "Water released by technical lead?", "Machines checked?", "Enough staff?", "No: keep transfers going", "Reopen: physician-led triage"],
   "Patient priority is set by physicians."),
 ],
 "22": [
  ("a", "first-hours", "The first hours after a serious event", "sequence", "1792x1024",
   "Orders the owner's actions: care and safety first, then evidence, disclosure and support, then reporting.",
   "Horizontal timeline with five blocks: 'Care for the patient', 'Make the unit safe', 'Preserve evidence', 'Tell the family honestly', 'Support staff', then 'Report as required'. A small clock above each block without times.",
   ["Care for the patient", "Make the unit safe", "Preserve evidence", "Tell the family honestly", "Support staff", "Report as required"],
   "No graphic injury."),
  ("b", "insurance-matrix", "What each policy covers", "card", "1536x1152",
   "Helps owners map risks to insurance and see uncovered gaps.",
   "A 2-column reference card: Risk on the left, Policy on the right, with icons: Patient injury -> Professional and facility liability; Fire and flood -> Property; Cyberattack -> Cyber policy, if any; Staff injury -> Employer obligations; Business stops -> Business interruption. A red tag 'Gap?' on rows without a match.",
   ["Patient injury", "Liability", "Fire and flood", "Property", "Cyberattack", "Cyber policy, if any", "Staff injury", "Employer obligations", "Business stops", "Business interruption", "Gap?"],
   ""),
 ],
 "23": [
  ("a", "acquisition-tradeoffs", "What changes after an acquisition", "compare", "1792x1024",
   "Presents what large studies observed after acquisitions, so owners ask the right questions before selling or buying.",
   "Two columns 'Before' and 'After acquisition (observed in US studies)'. Rows with icons: Drug doses, Nurse vs technician mix, Transplant waitlisting, Patient outcomes; arrows show the reported direction (up, shift to technicians, down, worse). A caption bar: 'Observational evidence; ask how the buyer will protect each'.",
   ["Before", "After acquisition (US studies)", "Highly reimbursed drug doses", "Nurses replaced by technicians", "Fewer transplant waitlistings", "Patients fared worse", "Observational evidence: ask how the buyer will protect each"],
   "Use arrows, not numbers."),
  ("b", "closure-continuity", "A responsible exit", "sequence", "1792x1024",
   "Shows that closing or selling is finished only when every patient is placed and records are safe.",
   "Left-to-right: Notice to regulators and payer, Find receiving units with confirmed slots, Individual transfer plans, Records transferred securely, Staff informed and paid, Final check: every patient accounted for.",
   ["Notify regulators and payer", "Confirmed receiving slots", "Individual transfer plans", "Records transferred securely", "Staff informed and paid", "Every patient accounted for"],
   ""),
 ],
 "24": [
  ("a", "board-pack", "The integrated board pack", "card", "1536x1152",
   "Shows how the module portfolio fits together into one decision document.",
   "An exploded view of a binder with seven tabbed sections fanned out: Governance and authority, Compliance register, Safe capacity and staffing, Water, equipment and infection, Claims and money, Quality and patient voice, Continuity and risk. A single cover sheet labeled 'Decisions needed'.",
   ["Decisions needed", "Governance", "Compliance", "Capacity and staffing", "Water, equipment, infection", "Claims and money", "Quality and patient voice", "Continuity and risk"],
   ""),
  ("b", "first-90-days", "The first 90 days", "sequence", "1792x1024",
   "Sequences a new owner's priorities: listen and secure, then fix, then build.",
   "Three wide panels on a timeline: Days 1–30 'Listen and secure' (walk-rounds, holds respected, cash and payroll checked), Days 31–60 'Fix the top risks' (funded corrective actions with owners), Days 61–90 'Build the system' (dashboard, charter, continuity drill).",
   ["Days 1–30: Listen and secure", "Days 31–60: Fix the top risks", "Days 61–90: Build the system", "Walk-rounds", "Respect every hold", "Cash and payroll", "Funded corrective actions", "Dashboard", "Charter", "Continuity drill"],
   ""),
 ],
}

KIND = {
    "algo": ("williamriveromd-algorithm-generator-skill", "Clinical/governance algorithm, AHA- and KDIGO-style flowchart"),
    "compare": ("williamriveromd-simple-figure (Scaffold B)", "Side-by-side comparison"),
    "sequence": ("williamriveromd-simple-figure (Scaffold C)", "Step sequence or cycle"),
    "mechanism": ("williamriveromd-simple-figure (Scaffold D)", "Single mechanism / causal-chain poster"),
    "card": ("williamriveromd-simple-figure (Scaffold E)", "Reference card / quick-look"),
    "sigil": ("williamriveromd-organ-crosstalk-sigil-graphic (adapted: service icons)", "Monoline systems sigil"),
}

NEG_HERO = """Avoid busy layouts, collage overload, more than four supporting scenes, dozens of icons, tiny unreadable labels, infographic clutter, duplicated people, repeated compositions, cropped circle, cropped objects, edge clipping, objects touching the circular border, important content inside the title safe zone, baked-in text, titles, captions, logos, watermarks, rectangular borders, frames, banners, dark / charcoal / black backgrounds, cartoon style, neon, HDR, over-saturation, distorted hands or faces, implausible anatomy, needles in skin, visible blood, readable screens, brand logos on machines."""

NEG_FIG = f"""Avoid cartoon style, clutter, tiny unreadable labels, AI gibberish text, misspelled labels, any text other than the verbatim labels and the footer, numbers or limits not in the label list, unrealistic anatomy or equipment, HDR, excessive saturation, brand names or logos, identifiable real people. NEVER use a dark, navy, charcoal or black background. Use ONLY {FONT} (approved sans-serif). Never omit the footer "{ATTR}"."""


def size(c):
    w, h = c.split("x")
    return f"{w} × {h}"


def ratio(c):
    return {"1792x1024": "16:9 landscape", "1024x1536": "2:3 portrait", "1536x1152": "4:3"}[c]


def hero_prompt(slug, title, h):
    arch, cam, sc, subj, supp, safe, cast = h
    kind = {"A": "photorealistic editorial photograph", "B": "photorealistic still-life", "C": "semi-photorealistic 3D medical illustration"}[sc]
    return f"""FILE NAME: {slug}-vignette-hero.png  (also export {slug}-vignette-hero.webp)
IMAGE TYPE: Circular vignette hero v3 — Scaffold {sc}
ASPECT RATIO: 1:1 (square — displayed inside an 85–90% inscribed circle with white margin)
PIXEL DIMENSIONS: 2048 × 2048
COMPOSITION ARCHETYPE: {arch}
CAMERA: {cam}
CAST: {cast}
AUDIENCE: owners, governing boards, and unit leaders
VISUAL GOAL: one glance conveys "{title}".

PROMPT:
Square 1:1 {kind} on a 2048×2048 canvas, composed to be displayed inside a CIRCULAR vignette occupying 85–90% of the canvas diameter with a visible WHITE BORDER around the full circle (the circle never touches the canvas edges). Composition archetype: {arch}. Camera: {cam}.

Subject: {subj}, in a clean, bright, modern Philippine setting with soft natural daylight and gentle shallow depth of field. Supporting context: {supp}.

Visual hierarchy: hero subject 60–70% of the circle; supporting context 20–30%; reserve a 20–25% TITLE SAFE ZONE ({safe}) with no faces, objects, icons, or callouts inside it. Calm, reassuring, documentary-realistic color grade harmonizing with clinical teal #1a6b72 and navy #0f1e2e on a light background; soft falloff toward a slightly deeper neutral at the rim. People, where shown, are adult Filipinos with natural skin texture and realistic hands, visibly different from any other hero in this course.

Absolutely NO text of any kind: no title, caption, label, logo, or watermark; no readable screens or documents.

NEGATIVE INSTRUCTIONS:
{NEG_HERO}

QUALITY CHECK:
Square 2048×2048; full circle visible with white margin; one dominant subject; title-safe zone empty; no text; light, airy palette; Filipino context."""


def tile_prompt(slug, title, metaphor):
    return f"""FILE NAME: {slug}-card.png → export {slug}-card.webp at 640 × 360
IMAGE TYPE: Academy module tile (text-free editorial art)
ASPECT RATIO: 16:9 landscape
PIXEL DIMENSIONS: 1672 × 941 (downscale to 640 × 360 WebP, quality 82)
AUDIENCE: Academy visitors choosing a module
VISUAL GOAL: a single readable metaphor for "{title}" that still reads at 320 px wide.

PROMPT:
Photorealistic editorial still image, 16:9 landscape, 1672×941, for a training-course tile. One clear subject filling the central 60% of the frame: {metaphor}. Bright, airy Philippine clinical or office setting, soft natural daylight, shallow depth of field, light background (white, off-white, or light teal tint #eef6f7), accents in clinical teal #1a6b72 and navy #0f1e2e. Keep a 10% safe margin on all sides so the subject survives a center crop. Simple, uncluttered, premium medical-publication feel, consistent with the rest of this course's tiles.

No text, letters, numbers, logos, or watermark in the image (the tile title is set in HTML).

NEGATIVE INSTRUCTIONS:
Avoid clutter, more than one focal subject, dark or moody lighting, cartoon or clip-art style, HDR, neon, readable text, brand logos, identifiable real people, needles or blood.

QUALITY CHECK:
Reads at thumbnail size; one subject; light background; no text."""


def fig_prompt(slug, key, title, kind, canvas, job, layout, labels, truth):
    skill, ktype = KIND[kind]
    portrait = canvas == "1024x1536"
    foot = "bottom-center" if portrait else "bottom-right corner"
    style = {
        "algo": f"Clean clinical algorithm in AHA/KDIGO guideline style, top-to-bottom, white #ffffff background, rounded rectangle action nodes, diamond decision nodes, thin navy arrows, muted pastel fills: teal #1a6b72 for recommended steps, amber #b8860b for caution or hold exits, clinical red #b91c1c for stop exits, renal green #1f7a4d for the final safe node. Maximum 3–4 branching levels, generous whitespace, no photorealistic people, no decorative icons.",
        "compare": "Medical-education comparison figure, AJKD/NEJM graphical-abstract style, white #ffffff background, soft dashed vertical divider, two equal rounded panels, small clean semi-photoreal icons per item, mobile-readable labels.",
        "sequence": "Clean education figure on a white #ffffff background: rounded cards on a very soft gray band #f3f4f6, joined by bold navy arrows, each card with a colored top accent band and one small semi-photoreal icon, generous whitespace.",
        "mechanism": "Single-panel causal-chain poster, AJKD/NEJM graphical-abstract style, white #ffffff background, semi-photoreal 3D components where objects appear, color-coded arrows, modular rounded callout cards, a bottom strip carrying the take-home line in navy.",
        "card": "Clinical reference card, publication-grade design, white #ffffff background, teal #1a6b72 headers on soft gray #f3f4f6, alternating row fills, compact icons, large legible type.",
        "sigil": "Minimal monoline line-art sigil diagram on a white background, thin clean strokes in teal, slate and muted blue, simplified service icons joined by dotted curved arrows, no 3D, no shadows, short labels only.",
    }[kind]
    lab = "\n".join(f"- \"{x}\"" for x in labels)
    return f"""FILE NAME: {HUB}-{key}-{slug}.png  (also export .webp)
SKILL: {skill}
IMAGE TYPE: {ktype}
ASPECT RATIO: {ratio(canvas)}
PIXEL DIMENSIONS: {size(canvas)}
AUDIENCE: owners and governing boards (non-clinical), unit leaders
TEACHING JOB: {job}

PROMPT:
{style} Title at top in bold navy #0f1e2e, set in {FONT}: "{title}". Layout: {layout}
Use {FONT} for every word. Render ONLY these labels, spelled exactly:
{lab}
{('Accuracy constraints: ' + truth) if truth else 'Accuracy constraints: none beyond the label list.'}
Footer: small {FONT} text "{ATTR}" at the {foot}, gray-navy at 70% opacity, never overlapping content.

NEGATIVE INSTRUCTIONS:
{NEG_FIG}

QUALITY CHECK:
Every label spelled exactly; no extra words or numbers; light background; mobile-readable at 390 px wide; footer present at the {foot}."""


COURSE = [
    ("hub-hero", "Course home vignette hero", f"""FILE NAME: {HUB}-vignette-hero.png  (also .webp)
IMAGE TYPE: Circular vignette hero v3 — Scaffold A
ASPECT RATIO: 1:1 · PIXEL DIMENSIONS: 2048 × 2048
COMPOSITION ARCHETYPE: J Environmental Storytelling · CAMERA: wide, eye level from the doorway
CAST: a Filipina owner in her late forties (wavy shoulder-length hair, olive linen blazer) walking the dialysis floor with a male head nurse in his thirties (tall, wire glasses, teal scrubs); two patients at chairs in soft focus
VISUAL GOAL: ownership that walks the floor and listens.

PROMPT:
Square 1:1 photorealistic editorial photograph on a 2048×2048 canvas, composed for a CIRCULAR vignette occupying 85–90% of the canvas diameter with a visible WHITE BORDER around the full circle. Archetype J, wide eye-level view from a doorway: a Filipina owner in her late forties with wavy shoulder-length hair and an olive linen blazer walks a bright modern hemodialysis floor beside a tall male head nurse in his thirties in teal scrubs and wire glasses who is pointing toward a machine as he explains; two patients rest in reclining chairs in soft focus, machines generic and unbranded. Soft daylight through high windows. Hero pair 60–70%; context 20–30%; reserve a 20–25% TITLE SAFE ZONE of pale ceiling and window light in the upper-left. Teal #1a6b72 and navy #0f1e2e accents, light airy grade. Absolutely NO text, logos, readable screens, or watermark.

NEGATIVE INSTRUCTIONS:
{NEG_HERO}"""),
    ("course-card", "Academy landing card (track tile)", f"""FILE NAME: {HUB}-card.png → export {HUB}-card.webp at 640 × 360
IMAGE TYPE: Academy track card, text-free · 16:9 · 1672 × 941
PROMPT:
Photorealistic editorial image, 16:9, 1672×941: a bright boardroom table in the foreground with a closed teal binder, a calculator and a set of building keys, opening through a glass wall onto a softly blurred, sunlit hemodialysis floor with a nurse at a chair. One clear focal line from the keys to the floor. Light background, teal #1a6b72 and navy #0f1e2e accents, 10% safe margin all round. No text, numbers, logos, or watermark.

NEGATIVE INSTRUCTIONS:
Avoid clutter, dark or moody lighting, cartoon style, readable text, brand logos, identifiable real people."""),
    ("og-art", "Open Graph share-card art (text set by build_academy_og.py)", f"""FILE NAME: images/academy/og-art/{HUB}.webp  (generate PNG 1536 × 1024, save as WebP)
IMAGE TYPE: OG art, text-free, for build_academy_og.py (crops to 1200 × 630, sets every word itself)
GROUP: administrative (accent #4B3280) · TITLE (set by script): "Dialysis Unit Owner" · TAG: "GOVERNANCE AND STEWARDSHIP" · STATS: "24 modules · 8 owner calculators · capstone"

PROMPT:
Photorealistic editorial image, 1536×1024, landscape. The LEFT 42% of the frame is a quiet, nearly empty field of soft off-white wall and gentle daylight gradient (the script will set the title there) — no objects, faces, or texture detail in that area. The RIGHT 58%: a calm Filipino owner in his fifties (broad build, short gray hair, light-blue barong-style shirt) seated at the end of a bright meeting table, reviewing a single printed page with the unit's clinical head (a woman in her forties in a white coat, hair in a low bun) who points to it; behind them a glass wall onto a softly blurred hemodialysis floor. Teal #1a6b72 and soft violet #4B3280 accents in small objects only (a binder, a mug). Light, airy, premium medical-publication grade. No text, letters, numbers, logos, or watermark anywhere.

NEGATIVE INSTRUCTIONS:
Avoid any object or detail in the left 42%, dark backgrounds, readable documents or screens, brand logos, cartoon style, HDR.

AFTER GENERATION:
Add a TRACKS entry to build_academy_og.py: "{HUB}": ("academy/{HUB}.html", "administrative", "Dialysis Unit Owner", "GOVERNANCE AND STEWARDSHIP", "24 modules · 8 owner calculators · capstone"), then run
python3 build_academy_og.py --art images/academy/og-art --only {HUB} --patch"""),
    ("calc-og", "Owner toolkit calculator share card (with text)", f"""FILE NAME: images/og/calc-dialysis-owner-toolkit.png  (save ≤300 KB JPEG copy for og:image)
SKILL: williamriveromd-infographic-skill — OG card
IMAGE TYPE: OG / social share card · ASPECT RATIO 1.91:1 · PIXEL DIMENSIONS: 1200 × 630 (fixed)

PROMPT:
Social share card, exactly 1200×630, white #ffffff background. Left half: title in bold navy #0f1e2e {FONT}, two lines: "Dialysis Unit Owner" / "Toolkit"; under it in teal #1a6b72 {FONT}: "8 calculators: break-even · capacity · cash · DSCR · patient share". Right half: a clean semi-photoreal 3D arrangement on a light teal tint #eef6f7 panel — a calculator, a small dialysis chair model, a coin stack and a rising teal bar chart — with generous whitespace. Small {FONT} footer "{ATTR}" bottom-right in navy at 70% opacity. No other text.

NEGATIVE INSTRUCTIONS:
Avoid dark backgrounds, misspelled words, extra text, brand logos, clutter, cartoon style.

AFTER GENERATION:
Point og:image / twitter:image of guides/calc-dialysis-owner-toolkit.html at the JPEG (1200 × 630)."""),
    ("course-map", "Course path map (hub page figure)", f"""FILE NAME: {HUB}-00-course-map.png  (also .webp)
SKILL: williamriveromd-simple-figure (Scaffold C) · 16:9 · 1792 × 1024

PROMPT:
Clean education figure, white #ffffff background, title in bold navy {FONT}: "Six stages from authority to a responsible exit". Six rounded stage cards left to right on a soft gray band #f3f4f6, joined by navy arrows, each with a small semi-photoreal icon and its modules: "1 Authority and ethics · Modules 1–5" (key), "2 The service you build · 6–9" (blueprint), "3 People and safety systems · 10–13" (nurse and water drop), "4 Payer and money · 14–17" (coin and form), "5 Assurance · 18–20" (run chart and lock), "6 Resilience and transition · 21–23" (umbrella and handshake), and a final wide green card "Capstone · Module 24". Bottom strip in navy {FONT}: "The financial plan rests on safely supported service, never the reverse." Footer "{ATTR}" bottom-right at 70% opacity. Render only these words.

NEGATIVE INSTRUCTIONS:
{NEG_FIG}"""),
    ("calc-gallery", "Owner calculator gallery (hub page figure)", f"""FILE NAME: {HUB}-00-calculator-gallery.png  (also .webp)
SKILL: williamriveromd-simple-figure (Scaffold E) · 4:3 · 1536 × 1152

PROMPT:
Clinical reference card, white #ffffff background, title in bold navy {FONT}: "The owner's eight calculators". A 4 × 2 grid of rounded tiles, each with a small clean icon and one label: "Break-even", "Cost per treatment", "Safe capacity", "Staffing FTE", "Cash and runway", "Loan and DSCR", "Payback and NPV", "Patient's yearly share". Teal #1a6b72 tile headers on soft gray #f3f4f6. Bottom line in navy: "Arithmetic, not decisions: a number never overrides a hold." Footer "{ATTR}" bottom-right at 70% opacity. Render only these words.

NEGATIVE INSTRUCTIONS:
{NEG_FIG}"""),
]


def build(out_dir):
    out_dir = Path(out_dir)
    nfig = sum(len(v) for v in FIGS.values())
    total = len(COURSE) + 2 * len(ROWS) + nfig
    md, man = [], []
    md.append(f"""# Dialysis Unit Owner — Image Plan Blueprint and GPT Prompt Pack

Prepared {PREPARED} for the Renal Care Academy Dialysis Unit Owner course (package `tools/techcourses/duo/`). Generated by `image_plan.py`; edit that file and re-run instead of editing this document.

## 1. Purpose

Images in this course have one job: make an owner *understand*, *apply*, and *care about* a governance idea faster than words alone. Every teaching figure therefore carries a stated **teaching job**, uses the course's own words as verbatim labels, and turns a mechanism into something visible: money becoming staffing, staffing becoming care, care becoming outcomes. Heroes and tiles set the emotional register — calm, Filipino, real, respectful of patients — and never carry text.

## 2. Inventory ({total} images)

| Set | Count | Size | Skill | Saved as |
|---|---|---|---|---|
| Course hero, course card, OG art, calculator OG card, course map, calculator gallery | {len(COURSE)} | various | hero-vignette · infographic · simple-figure | see Section 4 |
| Module vignette heroes | {len(ROWS)} | 2048 × 2048 | williamriveromd-hero-vignette v3 | `images/<module-slug>-vignette-hero.png` + `.webp` |
| Module tiles (cards) | {len(ROWS)} | 1672 × 941 → 640 × 360 | infographic (editorial, text-free) | `images/<module-slug>-card.webp` |
| Teaching figures (A and B per module) | {nfig} | 1792 × 1024 · 1024 × 1536 · 1536 × 1152 | simple-figure · algorithm · sigil | `images/{HUB}-<mm><a/b>-<name>.png` + `.webp` |

## 3. House rules applied to every prompt

- **Light backgrounds only**; accents teal `#1a6b72`, navy `#0f1e2e`, green `#1f7a4d` (safe), amber `#b8860b` (caution), red `#b91c1c` (stop). OG art for the Administrative track uses the violet accent `#4B3280` sparingly.
- **Font:** {FONT} only (approved sans-serif). Labels verbatim, American English, no numbers that are not in the label list.
- **Attribution:** teaching figures and the calculator OG card carry `{ATTR}` (bottom-right; bottom-center on portrait). Heroes, tiles and OG art are text-free; the OG title and attribution are set by `build_academy_og.py`.
- **People:** adult Filipinos; casts rotate across age, sex, build, hair, wardrobe, setting and camera so no two heroes look alike. No needles in skin, no blood, no readable screens or records, no brand logos.
- **Accuracy:** the owner never appears releasing water, restarting a machine or prescribing; release gates name the technical lead; PhilHealth figures appear only as `6,350 pesos per session · facility and professional fees included · up to 156 sessions a year`. Observational evidence is captioned as association.

## 4. Course-level images
""")
    for key, title, prompt in COURSE:
        md.append(f"### {title}\n\n```\n{prompt}\n```\n")
        man.append({"set": "course", "key": key, "title": title})
    md.append("## 5. Module heroes, tiles, and teaching figures\n")
    md.append("| Module | Hero (cast · archetype) | Tile metaphor | Figure A | Figure B |\n|---|---|---|---|---|")
    for mid, suf, title in ROWS:
        h = HERO[mid]; fa, fb = FIGS[mid]
        md.append(f"| {int(mid)}. {title} | {h[6]} · {h[0]} | {TILE[mid]} | {fa[2]} | {fb[2]} |")
    md.append("")
    for mid, suf, title in ROWS:
        slug = f"{HUB}-{mid}-{suf}"
        md.append(f"### Module {int(mid)} · {title}\n\nPage: `academy/{slug}.html`\n")
        md.append(f"#### Hero\n\n```\n{hero_prompt(slug, title, HERO[mid])}\n```\n")
        md.append(f"#### Tile\n\n```\n{tile_prompt(slug, title, TILE[mid])}\n```\n")
        man += [{"set": "hero", "module": mid, "file": f"{slug}-vignette-hero.png", "size": "2048x2048"},
                {"set": "tile", "module": mid, "file": f"{slug}-card.webp", "size": "640x360"}]
        for letter, name, ftitle, kind, canvas, job, layout, labels, truth in FIGS[mid]:
            key = f"{mid}{letter}"
            md.append(f"#### Figure {letter.upper()} · {ftitle}\n\nPlacement: lesson part noted in the build spec (Blueprint v2, Section 4). Figure key `duo{key}`.\n\n```\n{fig_prompt(name, key, ftitle, kind, canvas, job, layout, labels, truth)}\n```\n")
            man.append({"set": "figure", "module": mid, "key": f"duo{key}", "file": f"{HUB}-{key}-{name}.png", "size": canvas, "title": ftitle, "kind": kind})
    md.append(f"""## 6. Production and installation

1. Generate in ChatGPT image generation (current GPT image model) one prompt at a time; paste the whole block.
2. Review each image against its QUALITY CHECK and the label list; regenerate any image with a misspelled or extra word, a mirrored or implausible object, or a dark background.
3. Save PNGs with the exact FILE NAME into `images/`; make WebP twins (`cwebp -q 82`); tiles at 640 × 360.
4. Figures: add each to `tools/techcourses/duo/figs.py` as `"duo<mm><a|b>": (file, alt, caption)` and place it with `{{{{fig:duo<mm><a|b>}}}}` in its lesson part; captions carry a plain-language description (lightbox rule 11) and the abbreviations used.
5. Heroes are picked up automatically by name (`<module-slug>-vignette-hero.png`); tiles by `card_img` in `course.py`.
6. OG: add the TRACKS entry and run `build_academy_og.py` as shown in Section 4; then `generate_rg_thumbs.py` and `patch_rg_card_thumbs.py`.
7. Re-run `python3 generate_tech_courses.py --course duo --patch` and `python3 tools/academy/publish_academy.py`. Nothing is deployed without Dr. Rivero's sign-off.
""")
    (out_dir / "10-image-plan-blueprint.md").write_text("\n".join(md), encoding="utf-8")
    (out_dir / "image-plan-manifest.json").write_text(json.dumps(man, indent=1, ensure_ascii=False), encoding="utf-8")
    print(f"wrote {out_dir / '10-image-plan-blueprint.md'} ({total} images) and image-plan-manifest.json")


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--out", default=str(Path(__file__).resolve().parent))
    build(ap.parse_args().out)
