# -*- coding: utf-8 -*-
"""Dialyzer Reprocessing Technician, Module 04: Infection Prevention and Protecting Yourself. v0.1 RT04."""

MODULE = {
    "image_alt": "A reprocessing technician in a gown, gloves and face shield rinsing a used dialyzer at a deep sink, with an eye wash station on the wall beside her.",
    "objectives": [
        "Explain how hepatitis B, hepatitis C and HIV spread in dialysis units, and why the reuse room is a high-risk place for indirect spread.",
        "Describe one-way clean and dirty flow and why the reuse room must be separate from medicine preparation.",
        "Choose and use protective equipment for splash, vapor and sharps risks.",
        "Apply the academy eligibility default and the unit program to infection status.",
        "Respond correctly to a splash, a cut, or a spill, and report it.",
    ],
    "big": """
{{plain:Think of a kitchen where raw chicken is prepared. You keep the chopping board for raw meat away from the salad, you wash your hands between them, and you never let the juice drip onto the bread. Nobody can see the bacteria; the habits do the protecting.}}
<p>The picture has a limit. Chicken juice can be seen and smelled. A drop of blood carrying hepatitis B virus may be invisible, and the virus can survive on surfaces at room temperature for at least seven days.[[rt_cdc2001]] A reuse room handles blood-soiled devices from many patients every day. So the habits must be stricter than a kitchen&rsquo;s, and they must not depend on whether the contamination is visible.</p>
{{cards:Key terms for this module|Bloodborne virus::A virus carried in blood, such as hepatitis B, hepatitis C or HIV.|Indirect contact::Spread through hands, surfaces, equipment or supplies, not directly from person to person.|Clean area::Where processed dialyzers and clean supplies are kept.|Dirty area::Where used dialyzers are received and rinsed.|Personal protective equipment (PPE)::Gown, gloves, face shield, mask, eye protection and closed shoes.|Exposure::Contact of blood or chemical with broken skin, eyes, nose or mouth.}}
<p>Most of the time nothing goes wrong, because the habits hold. Your work is to keep the habits even when the room is busy and no one is watching.</p>
""",
    "case": {"title": "A splash at the header", "html": """
<p>Ms. Lorna Castillo, a reprocessing technician, is cleaning the blood-side header of a used dialyzer at 10:20 on a Saturday. She has her gown and gloves on. Her face shield is fogged, so she has pushed it up on her head for a moment. As she flushes the header, a jet of pink rinse water hits the side of her face and her left eye.</p>
<p>The dialyzer belongs to a patient whose program record shows him as eligible for reuse; his latest hepatitis results are filed in the nurses&rsquo; station. The reuse room is behind by eight dialyzers.</p>
""", "questions": ["What should Ms. Castillo do in the first minute?",
                  "What should happen in the next hour?",
                  "What should the unit change so it does not happen again?"]},
    "sections": [
        ("spread", "How viruses spread", "How bloodborne viruses spread in a dialysis unit", """
<p>Dialysis patients are exposed to blood every treatment, and many share stations, machines and staff. Outbreak investigations repeatedly find indirect contact: gloves not changed, surfaces not cleaned, clean supplies kept near dirty ones. The Centers for Disease Control and Prevention (CDC) recommendations for dialysis units rest on these findings.[[rt_cdc2001]][[cdc_dialysis]]</p>
<p>Two investigations show how the reuse room can be part of the chain. In a low-resourced unit in Vietnam, 11 patients acquired hepatitis C virus (HCV) over two months. All reused dialyzers on shared machines; the area for preparing injected medicines sat next to the area for handling blood samples and storing reused dialyzers. Investigators judged indirect contact through the environment as the likely route for 10 of the 11 cases and called for dedicated reprocessing systems and strict separation.[[rt_duong2016]] In the Netherlands, gene sequencing linked two new HCV infections to one patient, through a contaminated pressure port or lapses during two incidents in a single session.[[rt_heikens2019]] Both were investigations, not trials, but the mechanism is consistent: virus travels on hands, surfaces and equipment.</p>
<div class="table-wrap"><table>
<thead><tr><th>Virus</th><th>Why it matters in the reuse room</th></tr></thead>
<tbody>
<tr><td>Hepatitis B virus (HBV)</td><td>Very high amounts in blood; survives on surfaces for days; vaccination protects staff</td></tr>
<tr><td>Hepatitis C virus (HCV)</td><td>The most common bloodborne infection acquired in dialysis units; no vaccine</td></tr>
<tr><td>Human immunodeficiency virus (HIV)</td><td>Lower risk per exposure than HBV; PSN guidance excludes dialyzer reuse[[psn2024]]</td></tr>
</tbody></table></div>
{{key:Treat every used dialyzer as infectious, whatever its label says. The virus is invisible; the habit is not.}}
"""),
        ("flow", "Clean and dirty flow", "Clean and dirty flow", """
{{fig:rt04_flow}}
<p>A reuse room protects patients best when its layout makes mistakes hard. Used dialyzers enter at one end, move through rinsing and processing, and leave as clean, labeled dialyzers at the other end. Nothing travels backward. Malaysia&rsquo;s 2026 standards, a current regional comparison, require a dedicated reprocessing space with ventilation and labeled storage.[[rt_my2026]]</p>
<div class="table-wrap"><table>
<thead><tr><th>Feature</th><th>Why it matters</th></tr></thead>
<tbody>
<tr><td>Separate dirty receiving sink and clean storage</td><td>Prevents splash and drip from reaching processed dialyzers</td></tr>
<tr><td>No medicine preparation, food or drink in the room</td><td>The Vietnam outbreak placed medicine preparation next to reused dialyzers[[rt_duong2016]]</td></tr>
<tr><td>Hand hygiene station at the exit</td><td>Hands leaving the room are clean</td></tr>
<tr><td>Eye wash within reach</td><td>Splashes need water within seconds</td></tr>
<tr><td>Ventilation</td><td>Germicide vapor is removed (Module 6)</td></tr>
<tr><td>Dedicated area and reprocessor for any approved hepatitis program</td><td>Keeps one patient group&rsquo;s devices away from others&rsquo;[[psn2024]]</td></tr>
</tbody></table></div>
{{key:Dirty in, clean out, never crossing. If the layout forces a crossing, report it.}}
"""),
        ("ppe", "Protective equipment", "Protective equipment and how it fails", """
{{fig:rt04_ppe}}
<p>Header cleaning and rinsing produce splashes. Germicides give off vapor and can burn skin and eyes. Protective equipment works only when it is worn the whole time the risk exists.</p>
<div class="table-wrap"><table>
<thead><tr><th>Item</th><th>Protects against</th><th>How it fails</th></tr></thead>
<tbody>
<tr><td>Fluid-resistant gown</td><td>Splash to body and arms</td><td>Worn open at the back; worn outside the room</td></tr>
<tr><td>Gloves (chemical-compatible type)</td><td>Blood and germicide on hands</td><td>Not changed between dirty and clean tasks; torn; wrong material for the germicide</td></tr>
<tr><td>Face shield over a mask</td><td>Splash to eyes, nose and mouth</td><td>Pushed up because it fogs</td></tr>
<tr><td>Eye protection</td><td>Splash to eyes</td><td>Ordinary glasses with open sides</td></tr>
<tr><td>Closed, fluid-resistant shoes</td><td>Spills and dropped sharps</td><td>Sandals or cloth shoes</td></tr>
</tbody></table></div>
<p>Hepatitis B vaccination for staff is part of protection; the CDC recommends it for all susceptible dialysis staff, with a check of response.[[rt_cdc2001]] Ask occupational health for your own status.</p>
{{key:A fogged shield is a reason to fix the shield, not to lift it.}}
"""),
        ("eligibility", "Eligibility", "Infection status and eligibility", """
<p>The medical director&rsquo;s program decides which patients may reuse. The technician&rsquo;s job is to know the list and hold when it is unclear. Module 3 compared countries; the practical rules for the room are these.</p>
{{cards:Academy default for Philippine units (your program decides)|Hepatitis B positive::Single use.|HIV positive::Single use.|Hepatitis C positive::Hold unless the medical director has approved a documented pathway with a dedicated area and reprocessor.|Status unknown, out of date or conflicting::Hold and ask.}}
<p>A label on a dialyzer is not where infection status lives. It lives in the clinical record, and the nurse confirms it. Never write a diagnosis on a label that other patients can see unless your program requires a coded marker.</p>
{{stop:A change in a patient&rsquo;s infection status, such as a new positive result, stops reprocessing of that patient&rsquo;s dialyzer at once. Quarantine the dialyzer and tell the head nurse.}}
"""),
        ("exposure", "Exposure response", "When an exposure happens", """
{{flow:Splash, cut or needle injury|First seconds::Stop. Flush eyes at the eye wash for the time your procedure sets, holding the lids open; wash skin with soap and water; let a cut bleed freely, then wash. Do not scrub or apply bleach to skin.|First minutes::Tell the person in charge. Secure the dialyzer and the work area so no one else is exposed.|Within the hour::Report to occupational health or the designated physician, who assesses the need for testing and preventive treatment. Time matters for some preventive treatments.|Record::Date, time, what happened, which dialyzer, which patient (in the confidential report only), and what you did.|Review::The unit looks for the cause without blame: a fogged shield, a sink at the wrong height, a rushed schedule.}}
<p>Chemical splashes follow the same first steps: flush with water and follow the safety data sheet (SDS) for the product. Module 6 covers chemical exposure in detail.</p>
{{key:Flush first, report second, record third. A delayed report can close the window for preventive treatment.}}
"""),
    ],
    "debrief": ["""
<p><strong>In the first minute:</strong> Ms. Castillo stops work, goes to the eye wash and flushes her eye and face for the time the procedure sets, holding the lids open, then washes her face with water. She calls out so a colleague can secure the dialyzer and the sink.</p>
<p><strong>In the next hour:</strong> She reports to the person in charge and to occupational health or the designated physician. The source patient&rsquo;s infection results are retrieved through the nurse, confidentially, to guide her assessment. Her own hepatitis B vaccination status is checked. The incident is recorded. The backlog of eight dialyzers waits, or is processed by another authorized operator; patients receive new dialyzers if needed.</p>
<p><strong>What should change:</strong> The real cause was a fogging shield. The fix is anti-fog shields or a different model, a sink and spray height that point splashes away from the face, and a schedule that does not push staff to skip steps. The review asks why it happened, not who failed.</p>
"""],
    "skills": {"title": "Protective equipment and exposure drill",
               "intro": "Practice in the reuse room with your preceptor, using water in place of blood and germicide.",
               "items": [
                   ("Puts on gown, gloves, mask and face shield in the order the procedure sets, and removes them without contaminating hands or face.", True),
                   ("Keeps the face shield down for the whole splash-risk task.", True),
                   ("Changes gloves and performs hand hygiene between dirty and clean tasks.", True),
                   ("Identifies the clean and dirty areas and the one-way path in the room.", False),
                   ("Locates the eye wash, the spill kit and the SDS binder, and checks the eye wash flow.", True),
                   ("Demonstrates eye flushing with lids held open.", True),
                   ("States who to report an exposure to and how quickly.", True),
                   ("States what to do with a dialyzer when a patient&rsquo;s infection status changes.", True),
               ],
               "placement": "Audit the reuse room layout against the clean and dirty flow table. Report any crossing point to the head nurse with a suggested fix."},
    "quiz": [
        ("How long can hepatitis B virus survive on surfaces at room temperature?",
         ["A few minutes", "About an hour", "At least seven days", "It cannot survive outside the body"], 2,
         "The CDC notes survival for at least seven days, which is why surfaces matter."),
        ("In the Vietnam hepatitis C outbreak, what was the most likely route for most cases?",
         ["Shared needles", "Indirect contact through a contaminated environment", "Blood transfusion", "Airborne spread"], 1,
         "Investigators judged indirect contact likely for 10 of 11 cases."),
        ("Which arrangement in the Vietnam unit increased risk?",
         ["A separate reuse room", "Medicine preparation next to blood handling and reused dialyzer storage", "A dedicated reprocessor", "Daily surface cleaning"], 1,
         "Clean work beside dirty work invites contamination."),
        ("Your face shield fogs during header cleaning. What do you do?",
         ["Lift it for a moment", "Stop, and replace or fix the shield before continuing", "Continue with ordinary glasses", "Work faster"], 1,
         "A lifted shield protects nothing. Fix the equipment."),
        ("What is the first action after blood splashes into your eye?",
         ["Report to the head nurse", "Flush at the eye wash with lids held open", "Finish the dialyzer", "Rub the eye dry"], 1,
         "Flush first, report second, record third."),
        ("Under the academy default, a patient&rsquo;s hepatitis B surface antigen has turned positive. What happens to his dialyzer?",
         ["Continue reprocessing as usual", "Stop reprocessing it at once, quarantine it, and tell the head nurse", "Reprocess it once more", "Move it to clean storage"], 1,
         "A change in infection status stops reprocessing. The clinical team decides the plan."),
        ("Where should a patient&rsquo;s infection status be confirmed?",
         ["On the dialyzer label", "In the clinical record, through the nurse", "By asking the patient", "From memory"], 1,
         "Labels identify; the clinical record holds the diagnosis."),
        ("Which is the main reason the reuse room needs one-way flow?",
         ["To look tidy", "So that dirty items never travel back toward clean ones", "To save water", "To speed up processing"], 1,
         "Layout prevents contamination when people are busy."),
        ("What does the CDC recommend for susceptible dialysis staff?",
         ["Hepatitis B vaccination with a check of response", "Avoiding all blood contact", "Annual HIV testing only", "No vaccination"], 0,
         "Vaccination protects staff against hepatitis B."),
        ("A colleague cleans a cut on her hand with bleach after an injury. Is that correct?",
         ["Yes, bleach kills viruses", "No; let it bleed, wash with soap and water, and report", "Yes, if the bleach is diluted", "No; cover it and keep working"], 1,
         "Bleach damages skin. Washing and prompt reporting are the right steps."),
        ("Why should an exposure be reported within the hour?",
         ["To avoid paperwork later", "Some preventive treatments work best when started early", "Because the dialyzer must be discarded", "Because the patient must be told first"], 1,
         "Delay can close the window for preventive treatment."),
        ("Which item should never be in the reuse room?",
         ["An eye wash", "A spill kit", "Food and drink", "A hand hygiene station"], 2,
         "Eating and drinking where blood and chemicals are handled is a route of exposure."),
    ],
    "terms": [("Bloodborne virus", "A virus carried in blood, such as hepatitis B, hepatitis C or HIV."),
              ("Indirect contact", "Spread through hands, surfaces, equipment or supplies."),
              ("Clean area", "Where processed dialyzers and clean supplies are kept."),
              ("Dirty area", "Where used dialyzers are received and rinsed."),
              ("Exposure", "Contact of blood or chemical with broken skin, eyes, nose or mouth."),
              ("Occupational health", "The service that looks after the health of staff, including after an exposure."),
              ("Gene sequencing", "Reading a virus&rsquo;s genetic code to tell whether two infections are linked.")],
    "readings": [("viral-infections-vaccinations-ckd.html", "Viral infections and vaccines in kidney disease."),
                 ("dialysis-access-infection.html", "How infections start at the dialysis access.")],
    "calcs": [],
}


# Spread the keyed answers across positions A to D.
import importlib.util as _u
from pathlib import Path as _P
_s = _u.spec_from_file_location("rt_quizutil", _P(__file__).resolve().parent / "quizutil.py")
_q = _u.module_from_spec(_s); _s.loader.exec_module(_q)
MODULE["quiz"] = _q.balance(MODULE["quiz"])
