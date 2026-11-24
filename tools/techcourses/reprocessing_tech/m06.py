# -*- coding: utf-8 -*-
"""Dialyzer Reprocessing Technician, Module 06: Germicides and Chemical Safety. v0.1 RT06."""

MODULE = {
    "image_alt": "A reprocessing technician in goggles and chemical-resistant gloves dipping a potency test strip into a freshly mixed germicide container under a ventilation hood.",
    "objectives": [
        "Explain how oxidizing and aldehyde germicides and heat kill microorganisms in a dialyzer.",
        "Explain why a germicide must be mixed evenly and tested for potency, using the CDC outbreak of 1988 as the example.",
        "Calculate a dilution with C1V1 = C2V2 and state why the result must still be verified.",
        "Read a safety data sheet (SDS) for hazards, protective equipment and first aid.",
        "Describe the respiratory and skin risks to staff and the controls that reduce them.",
    ],
    "big": """
{{plain:Think of making juice from a concentrate. If you pour the syrup into the jug and do not stir, the first glass is pale and the last glass is thick and sweet. Same jug, different strength, depending on where you pour from.}}
<p>The picture has a limit. A weak glass of juice is only disappointing. A weak dose of germicide leaves bacteria alive inside the fibers, where they multiply and release endotoxin into the next patient&rsquo;s blood. A strong dose that is not rinsed away reaches the patient as a chemical. The strength must be right, the same everywhere in the batch, proven by a test, and then removed.</p>
{{cards:Key terms for this module|Germicide::A chemical or physical agent that kills microorganisms. In reprocessing it must reach high-level disinfection.|Peracetic acid (PAA) mixture::An oxidizing germicide supplied with hydrogen peroxide and acetic acid.|Aldehyde::A class of germicide that includes formaldehyde and glutaraldehyde.|Potency test::A check, usually a test strip, that the germicide in the dialyzer is at least the required strength.|Contact time::The minimum time the germicide must stay in the dialyzer to work.|Safety data sheet (SDS)::The supplier&rsquo;s document on a chemical&rsquo;s hazards, handling and first aid.}}
<p>You will never choose the germicide or set its strength; the program and the instructions for use (IFU) do that. Your work is to prepare it exactly, prove it, use it safely, and remove it completely.</p>
""",
    "case": {"title": "The bottom of the container", "html": """
<p>This case is retold from a CDC investigation.[[rt_beck1990]] In April 1988, a United States hemodialysis center saw nine pyrogenic reactions and five gram-negative bacteremias in 11 patients over about two weeks. Every affected session used a reprocessed dialyzer; none occurred with new dialyzers.</p>
<p>The center reprocessed manually with a 2.5% peracetic acid mixture. Investigators measured germicide strength in stored dialyzers and found it ranged from 0.9% to 4.2%. Dialyzers with strength at or below 1.0% had higher endotoxin. When investigators repeated the technician&rsquo;s own dilution method, the solution measured 1.4% at the surface of the mixing container and 3.5% at the bottom.</p>
""", "questions": ["Why did some dialyzers hold less than half the intended strength?",
                  "Which single check would have caught the problem before patients were affected?",
                  "What would you change in the mixing procedure?"]},
    "sections": [
        ("how-they-kill", "How germicides kill", "How germicides kill", """
{{fig:rt06_chemicals}}
<div class="table-wrap"><table>
<thead><tr><th>Method</th><th>How it kills</th><th>Main hazard to staff</th><th>Before the next treatment</th></tr></thead>
<tbody>
<tr><td>Peracetic acid mixture</td><td>Oxidizes proteins and cell membranes of microorganisms</td><td>Irritates eyes, nose and airways; corrosive to skin</td><td>Residual test for the peroxide or acid after rinsing</td></tr>
<tr><td>Formaldehyde</td><td>Binds and cross-links proteins</td><td>Irritant; classified as a human carcinogen; skin sensitizer</td><td>Residual formaldehyde test after rinsing</td></tr>
<tr><td>Glutaraldehyde</td><td>Cross-links proteins</td><td>Strong sensitizer; occupational asthma and dermatitis</td><td>Residual test after rinsing</td></tr>
<tr><td>Heat with citric acid</td><td>Heat denatures proteins; citric acid assists</td><td>Burns from hot equipment</td><td>Cooling and checks set by the method</td></tr>
</tbody></table></div>
<p>The HEMO Study used several of these methods, including heated citric acid, and found that the method changed how well middle molecules were cleared.[[rt_cheung1999]] The 2012 systematic review found that outcome differences, where seen, varied by germicide.[[rt_galvao2012]] So the germicide is a clinical choice, made by the program. Concentrations and contact times differ between products and are taken only from the product IFU and the validated procedure.</p>
{{key:Each germicide kills differently, harms staff differently, and needs its own residual test. None is universal.}}
"""),
        ("mixing", "Mixing and potency", "Mixing, potency and the 1988 outbreak", """
{{fig:rt06_mixing}}
<p>A concentrated germicide is often denser than water. Poured in without enough mixing, it sinks. The top of the container is weak and the bottom is strong. Dialyzers filled from different parts of the batch get different doses. That is what the 1988 investigators found, and weak germicide allowed bacteria and endotoxin to persist in stored dialyzers.[[rt_beck1990]]</p>
<p>Automated reprocessors dilute germicide in-line, which reduces but does not remove the risk: a kinked line, an empty concentrate container or a failing pump gives weak germicide too. The defense in every system is the same.</p>
{{flow:Preparing and proving the germicide|Check the product::Correct product, within its expiry date, container intact.|Prepare::Exactly as the IFU and SOP direct, including the order of adding concentrate and water and the mixing method.|Prove the batch::Potency test on the prepared solution before use, recorded.|Prove each dialyzer::Presence or potency test on each filled dialyzer as the program directs, recorded.|Label::Batch preparation time and expiry, if the solution is stored.}}
{{formula:C1 &times; V1 = C2 &times; V2 &nbsp;&middot;&nbsp; volume of concentrate V1 = (target strength C2 &times; final volume V2) &divide; stock strength C1. Example for practice only: to make 10 L at 2.5% from a 50% stock, V1 = (2.5 &times; 10) &divide; 50 = 0.5 L of concentrate, made up to 10 L.}}
<p>The formula tells you how much to measure. It cannot tell you whether the batch is mixed or whether the stock has lost strength in storage. Only the potency test does.</p>
{{key:Arithmetic predicts the strength. Only the potency test proves it.}}
"""),
        ("sds", "Reading an SDS", "Reading a safety data sheet", """
<p>Every chemical in the room has an SDS. You do not need to read all of it every day. You need to know where it is and four sections by heart.</p>
<div class="table-wrap"><table>
<thead><tr><th>SDS section</th><th>What to look for</th></tr></thead>
<tbody>
<tr><td>Hazards identification</td><td>Pictograms and warnings: corrosive, toxic, sensitizer, carcinogen</td></tr>
<tr><td>First-aid measures</td><td>What to do for eyes, skin, inhalation and swallowing</td></tr>
<tr><td>Exposure controls and personal protection</td><td>Ventilation, glove material, eye and face protection, respirator if any</td></tr>
<tr><td>Handling and storage; stability and reactivity</td><td>Temperature, light, incompatible chemicals</td></tr>
</tbody></table></div>
{{stop:Never mix germicides or cleaners unless the SOP gives the exact sequence. Bleach mixed with acids releases chlorine gas.}}
"""),
        ("staff", "Protecting your lungs and skin", "Protecting your lungs, eyes and skin", """
<p>Germicide vapor is a staff health problem. The best data come from hospitals using products that contain hydrogen peroxide, peracetic acid and acetic acid for cleaning. In a study of 163 staff, users reported more work-related wheeze and watery eyes than non-users, and workers in the department with the highest air levels had a higher prevalence of watery eyes and more than three times the expected rate of current asthma.[[rt_casey2017]] In a companion study of cleaning staff, eye and airway symptoms were associated with exposure even though measured air levels were below established limits; no full-shift limit for peracetic acid had been set in the United States, and a limit of 0.2 ppm had been proposed by researchers.[[rt_hawley2017]] Both were observational studies of cleaning staff, not reuse rooms, but the chemicals are the same.</p>
<div class="table-wrap"><table>
<thead><tr><th>Control</th><th>How it protects you</th></tr></thead>
<tbody>
<tr><td>Closed systems and automated filling</td><td>Less open liquid, less vapor</td></tr>
<tr><td>Local exhaust ventilation at the work point</td><td>Removes vapor before you breathe it</td></tr>
<tr><td>Capped containers; spills cleaned promptly with the spill kit</td><td>Less evaporation</td></tr>
<tr><td>Chemical-compatible gloves, goggles or face shield, gown</td><td>Prevents skin and eye contact</td></tr>
<tr><td>Reporting symptoms early</td><td>Wheeze, cough, eye or skin irritation at work are signals, not inconveniences</td></tr>
</tbody></table></div>
{{key:If you smell the germicide all day, the ventilation is not working. Report it before your lungs report it.}}
"""),
        ("spill", "Spills and splashes", "Spills and splashes", """
{{flow:Germicide spill|Protect::Warn others; keep people away; open ventilation if safe.|Protective equipment::Gloves, goggles and gown before you approach; respirator only if the SDS calls for it and you are fitted.|Contain::Use the spill kit absorbent; never wipe concentrate with a bare cloth.|Dispose::As the SDS and the waste procedure direct.|Report::Record the spill and any exposure.}}
<p>A splash to the eye is flushed at once at the eye wash, as in Module 4, and followed by the first-aid section of the SDS and a report to occupational health.</p>
"""),
    ],
    "debrief": ["""
<p><strong>Why was the strength uneven?</strong> The concentrate was not mixed thoroughly into the water. It layered: 1.4% at the surface and 3.5% at the bottom of the same container.[[rt_beck1990]] Dialyzers filled from the weak layer held as little as 0.9%, not enough to stop bacteria growing during storage.</p>
<p><strong>Which check would have caught it?</strong> A potency test on the prepared batch, and a presence or potency check on each filled dialyzer. Either would have shown the weak solution before the dialyzers were stored.</p>
<p><strong>What would you change?</strong> Follow the IFU&rsquo;s mixing method exactly, including the order of adding concentrate and water and the mixing time; test the batch every time it is prepared; test each dialyzer as the program directs; and record both. Better still, use a validated automated system and keep the same tests, because machines can dilute badly too.</p>
"""],
    "skills": {"title": "Germicide preparation and spill drill",
               "intro": "Practice with water and a dye in place of germicide, then with the real product under supervision.",
               "items": [
                   ("Checks product name, expiry and container integrity before use.", True),
                   ("Calculates the volume of concentrate with C1V1 = C2V2 and has the arithmetic checked.", False),
                   ("Prepares the solution in the order and with the mixing method the IFU sets.", True),
                   ("Performs and records a potency test on the batch before use.", True),
                   ("Wears chemical-compatible gloves, eye and face protection and a gown.", True),
                   ("Locates the SDS and reads the first-aid and protection sections aloud.", False),
                   ("Contains and cleans a simulated spill with the spill kit.", True),
                   ("States why bleach must never be mixed with acid germicides.", True),
               ],
               "placement": "Review your unit&rsquo;s germicide records for one week: check that every batch has a recorded potency result. Report any gap."},
    "quiz": [
        ("In the 1988 CDC investigation, what caused the uneven germicide strength?",
         ["Expired product", "Inadequate mixing during dilution", "Contaminated water only", "A faulty dialyzer"], 1,
         "The concentrate layered: weak on top, strong at the bottom."),
        ("Which check would have caught the weak germicide before storage?",
         ["Total cell volume", "A potency test on the batch and on filled dialyzers", "The integrity test", "A visual inspection"], 1,
         "Only a potency or presence test proves strength."),
        ("To make 10 L at 2.5% from a 50% stock, how much concentrate is needed?",
         ["0.05 L", "0.5 L", "2.5 L", "5 L"], 1,
         "V1 = (2.5 &times; 10) &divide; 50 = 0.5 L."),
        ("What does the dilution formula not tell you?",
         ["How much concentrate to measure", "Whether the batch is mixed evenly and the stock is still at full strength", "The final volume", "The target strength"], 1,
         "Arithmetic predicts; testing proves."),
        ("Where do the germicide concentration and contact time come from?",
         ["This module", "The product IFU and the validated SOP", "The technician&rsquo;s judgment", "A colleague"], 1,
         "No concentration on this page is a working value."),
        ("Which germicide is a strong sensitizer associated with occupational asthma?",
         ["Glutaraldehyde", "Sodium chloride", "Citric acid alone", "Water"], 0,
         "Glutaraldehyde sensitizes skin and airways."),
        ("Mixing bleach with an acid germicide releases:",
         ["Oxygen only", "Chlorine gas", "Nothing harmful", "Water vapor"], 1,
         "Never mix chemicals outside the SOP&rsquo;s exact sequence."),
        ("What did the NIOSH studies of hospital staff using peroxide and peracetic acid products find?",
         ["No symptoms", "More wheeze and eye and airway symptoms, even at low measured levels", "Improved lung function", "Only skin rashes"], 1,
         "Observational, but consistent: these vapors irritate airways."),
        ("You can smell germicide strongly throughout your shift. What does that suggest?",
         ["Normal operation", "Ventilation or containment is not working; report it", "The germicide is extra strong, which is good", "You should work faster"], 1,
         "Persistent odor means exposure."),
        ("Which SDS section tells you what glove material to wear?",
         ["Hazards identification", "Exposure controls and personal protection", "Transport information", "Ecological information"], 1,
         "Exposure controls lists protective equipment."),
        ("An automated reprocessor dilutes germicide in-line. Do you still need potency or presence checks?",
         ["No, machines are always accurate", "Yes; lines kink, containers empty and pumps fail", "Only monthly", "Only if a patient has a reaction"], 1,
         "The same proof is needed whatever the system."),
        ("Why can a weak germicide cause fever in the next patient?",
         ["It cools the blood", "Bacteria survive and multiply during storage and release endotoxin", "It raises potassium", "It blocks fibers"], 1,
         "Weak disinfection lets bacteria grow; endotoxin causes pyrogenic reactions."),
    ],
    "terms": [("Germicide", "A chemical or physical agent that kills microorganisms."),
              ("High-level disinfection", "Killing all microorganisms except large numbers of bacterial spores."),
              ("Peracetic acid mixture", "An oxidizing germicide supplied with hydrogen peroxide and acetic acid."),
              ("Aldehyde", "A germicide class that includes formaldehyde and glutaraldehyde."),
              ("Potency test", "A check that a germicide is at least the required strength."),
              ("Sensitizer", "A chemical that can cause allergy after repeated exposure."),
              ("Local exhaust ventilation", "A system that draws vapor away at the point where it is released.")],
    "readings": [("dialyzer-reprocessing-reuse.html", "Germicides used in reprocessing and their risks.")],
    "calcs": ["calc-reprocessing-technician-toolkit.html#c3"],
}


# Spread the keyed answers across positions A to D.
import importlib.util as _u
from pathlib import Path as _P
_s = _u.spec_from_file_location("rt_quizutil", _P(__file__).resolve().parent / "quizutil.py")
_q = _u.module_from_spec(_s); _s.loader.exec_module(_q)
MODULE["quiz"] = _q.balance(MODULE["quiz"])
