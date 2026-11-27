# -*- coding: utf-8 -*-
"""Pediatric Dialysis Nurse, Module 7: PD in children: physiology, readiness and the prescription. POD voice. Fictional cases."""

MODULE = {
    "image_alt": "",
    "objectives": [
        "Explain how the peritoneal membrane works in a child, and why fill volume is scaled to body surface area rather than weight alone.",
        "Calculate body surface area and express an ordered fill volume in mL/m&sup2; and mL/kg, and recognize a value outside the usual band.",
        "Describe intraperitoneal pressure, its signs at the bedside, and its link to leaks, hernias and breathing.",
        "Read a pediatric PD order element by element and verify it against today&rsquo;s weight and height.",
    ],
    "big": """
<p>The peritoneum is the same living membrane in a child and an adult: blood vessels on one side, dialysis fluid on the other, solutes moving down their gradients and water drawn by glucose. What changes is the surface available and how much fluid the abdomen tolerates. A child&rsquo;s peritoneal surface is large compared with body weight, but the abdomen is small, and an infant breathes mainly with the diaphragm that the fluid pushes against.</p>
<p>Your work in this module is to read a pediatric PD order with the eyes of someone who knows what each number does to the child.</p>
{{plain:Think of the peritoneum as a folded tablecloth inside the abdomen. Pour in a little fluid, and only part of the cloth gets wet. Pour in more, and more of the cloth unfolds and joins the exchange, until the cloth is fully spread. Pour in still more, and you do not wet more cloth; you only press on the table.}}
<p>The picture has a limit. The &ldquo;cloth&rdquo; is not passive: its blood flow, the number of working pores and the child&rsquo;s position all change how much of it works. Lying down recruits more surface than sitting. That is why the same fill feels different at night than during the day.</p>
{{cards:Key terms for this module|Body surface area (BSA)::Skin area in square meters, estimated from height and weight.|Fill volume::The volume of dialysate run into the abdomen per exchange.|Intraperitoneal pressure (IPP)::The pressure the fluid creates inside the abdomen, measured in cmH&#8322;O.|Dwell time::How long the fluid stays in before draining.|Recruitment::More membrane joining the exchange as fill volume rises.}}
""",
    "case": {"title": "A 900 that looked like a 300", "html": """
<p><strong>Rhea Aquino, 1 year</strong>, length 75 cm, weight 9 kilograms, is starting automated PD at home after training. The discharge order transcribed into the clinic record reads a fill volume of 900 mL per cycle. Her mother, <strong>Joy</strong>, mentions that in the hospital &ldquo;the bag looked much smaller&rdquo;. <strong>Nurse Lorna</strong> prepares the first home cycler program.</p>
""", "questions": ["What is the ordered fill volume in mL/m&sup2; and mL/kg?",
                  "Is it inside the usual band for Rhea&rsquo;s age?",
                  "What does Lorna do before programming the cycler?"]},
    "sections": [
        ("the-membrane-in-a-child", "The membrane", "The peritoneum in a child", """
<p>Three processes work across the membrane. Diffusion moves urea, creatinine, potassium and phosphate from blood to fluid. Osmosis, driven by glucose, pulls water into the abdomen (ultrafiltration). Convection drags solutes along with that water. The three-pore model describes the routes: tiny water-only channels (aquaporins), abundant small pores for solutes, and few large pores that leak protein.[[pdn_fischbach2009]]</p>
<p>Dwell time trades one goal against another. Short dwells favor water removal and urea clearance, because the glucose gradient is still strong. Long dwells favor creatinine and phosphate clearance; reaching a given dialysate-to-plasma ratio for phosphate takes three to four times longer than for urea.[[pdn_fischbach2009]] A child who needs phosphate removal may need some long dwells, at the cost of less ultrafiltration.</p>
<p>Children also lose protein into the dialysate, which is one reason their energy and protein needs are adjusted by the renal dietitian (Module 17).[[pdn_shaw2020]]</p>
{{key:Short dwells remove water and urea; long dwells remove phosphate. The order&rsquo;s dwell times are a deliberate trade.}}
"""),
        ("fill-volume-and-pressure", "Fill volume", "Fill volume and intraperitoneal pressure", """
<p>Pediatric fill volumes are scaled to body surface area. In children 2 years and older, the membrane keeps recruiting as fill volume rises toward about 1,400 mL/m&sup2;; above that, more fluid adds pressure without adding exchange. Under 2 years, fill volume is set more by tolerance, and about 800 mL/m&sup2; (or 30 to 50 mL/kg) is often suggested as an upper limit, with individual assessment most important.[[pdn_fischbach2009]]</p>
{{fig:pdn07_a}}
{{formula:BSA (m&sup2;) = &radic;(height in cm &times; weight in kg &divide; 3,600) &nbsp;(Mosteller)<br>Fill volume per BSA (mL/m&sup2;) = fill volume (mL) &divide; BSA (m&sup2;)<br>Example: 110 cm, 18 kg &rarr; BSA &radic;(110 &times; 18 &divide; 3,600) = 0.74 m&sup2;; a 1,000 mL fill = about 1,350 mL/m&sup2; and 56 mL/kg}}
<p>Intraperitoneal pressure (IPP) is the pressure the fill creates, measured at rest lying flat. In one published series of children over 2 years, IPP averaged about 5 cmH&#8322;O at 600 mL/m&sup2; and about 14 cmH&#8322;O at 1,400 mL/m&sup2;, similar to adults at their usual fills.[[pdn_fischbach2009]] High pressure is linked to discomfort, breathing difficulty, leaks and hernias. You see high IPP as a child who is breathless, grunting, refusing to lie down, vomiting, or complaining of fullness after the fill.</p>
{{key:A fill outside the usual band for the child&rsquo;s age is a question to ask, never a value to correct yourself.}}
"""),
        ("reading-the-order", "The order", "Reading a pediatric PD order", """
<p>Every element of the order connects to a physiological job. Check each one against today&rsquo;s weight and height.</p>
{{fig:pdn07_b}}
<div class="table-wrap"><table>
<thead><tr><th>Element</th><th>Its job</th><th>Your check</th></tr></thead>
<tbody>
<tr><td>Weight, height, BSA</td><td>Basis for scaling</td><td>Measured recently; BSA recalculated after growth</td></tr>
<tr><td>Fill volume (mL)</td><td>Membrane recruitment and comfort</td><td>Convert to mL/m&sup2; and mL/kg; compare with the age band</td></tr>
<tr><td>Dextrose strength</td><td>Ultrafiltration</td><td>Matches the order; stronger bags not substituted without an order</td></tr>
<tr><td>Dwell time and number of cycles</td><td>Clearance and water removal</td><td>Total therapy time fits the order and the family&rsquo;s night</td></tr>
<tr><td>Last fill (day dwell)</td><td>Daytime clearance</td><td>Volume and solution, or &ldquo;dry day&rdquo;, as ordered</td></tr>
<tr><td>Tidal or minimum drain settings, where used</td><td>Comfort and alarm reduction</td><td>Match the order and the device instructions</td></tr>
</tbody></table></div>
<p>Readiness for home PD includes more than the order: a trained caregiver who has shown the skills, a clean space, storage for supplies, reliable electricity or a backup plan for a cycler, and a way to reach the team at night (Module 18). The 2020 ISPD pediatric acute PD guideline notes that automated PD is not suitable for newborns because their fill volumes are too small for current machines (1D).[[pd_nourse2021]]</p>
{{scene:Lorna and the 900|<p>Lorna calculates. Rhea&rsquo;s BSA is &radic;(75 &times; 9 &divide; 3,600) = 0.43 m&sup2;. A 900 mL fill is about 2,080 mL/m&sup2; and 100 mL/kg, far above the usual band for a 1-year-old. She does not program the cycler. She checks the original hospital order, which reads 300 mL (about 690 mL/m&sup2;), and calls the pediatric nephrologist to confirm and correct the transcription.</p><p class="tc-scene-take">Converting the fill to mL/m&sup2; turned a plausible-looking number into an obvious stop.</p>}}
{{key:Convert every fill to mL/m&sup2; and mL/kg before you program it. The conversion is where transcription errors show themselves.}}
"""),
    ],
    "debrief": ["""
<p><strong>The arithmetic.</strong> BSA &radic;(75 &times; 9 &divide; 3,600) = 0.43 m&sup2;. 900 mL &divide; 0.43 m&sup2; &asymp; 2,080 mL/m&sup2;; 900 &divide; 9 = 100 mL/kg.</p>
<p><strong>The band.</strong> Under 2 years, about 800 mL/m&sup2; (30 to 50 mL/kg) is often the upper limit, by tolerance. 2,080 mL/m&sup2; is far outside it, and Joy&rsquo;s memory of a smaller bag fits a transcription error.</p>
<p><strong>Before programming.</strong> Lorna stops, compares with the source order, and has the nephrologist confirm the correct value. She documents the discrepancy and reports it as a near miss so the transcription step can be fixed.</p>
"""],
    "skills": {"title": "Reading a pediatric PD order", "intro": "Use fictional orders.",
               "items": [("Calculates BSA (Mosteller) with units and an independent check", True),
                         ("Converts a fill volume to mL/m&sup2; and mL/kg and compares with the age band", True),
                         ("Identifies each order element and its physiological job", False),
                         ("Recognizes signs of high intraperitoneal pressure in a child", False),
                         ("Stops and escalates when a fill volume is outside the usual band or differs from the source order", True)]},
    "quiz": [
        ('Pediatric PD fill volumes are usually scaled to:',
         ['Age only', 'Parent&rsquo;s weight', 'Bag size available', 'Body surface area'], 3,
         'Expressed in mL/m&sup2;.'),
        ('In children 2 years and older, recruitment rises with fill volume up to about:',
         ['1,400 mL/m&sup2;', '400 mL/m&sup2;', '800 mL/m&sup2;', '3,000 mL/m&sup2;'], 0,
         'Above that, more fluid adds pressure, not exchange.'),
        ('Under 2 years, a commonly suggested upper fill limit is about:',
         ['1,400 mL/m&sup2;', '800 mL/m&sup2; (30&ndash;50 mL/kg)', '2,000 mL/m&sup2;', 'None'], 1,
         'Tolerance and individual assessment come first.'),
        ('BSA for 110 cm and 18 kg (Mosteller) is about:',
         ['0.44 m&sup2;', '1.1 m&sup2;', '0.74 m&sup2;', '1.73 m&sup2;'], 2,
         '&radic;(110 &times; 18 &divide; 3,600) = 0.74.'),
        ('A 1,000 mL fill at BSA 0.74 m&sup2; is about:',
         ['740 mL/m&sup2;', '2,000 mL/m&sup2;', '550 mL/m&sup2;', '1,350 mL/m&sup2;'], 3,
         '1,000 &divide; 0.74 &asymp; 1,350.'),
        ('Short dwells favor:',
         ['Water removal and urea clearance', 'Phosphate removal', 'Protein retention', 'Nothing'], 0,
         'The glucose gradient is strongest early.'),
        ('Phosphate equilibration compared with urea takes:',
         ['The same time', 'About three to four times longer', 'Half the time', 'No time'], 1,
         'Long dwells help phosphate clearance.'),
        ('Which sign suggests high intraperitoneal pressure?',
         ['Sleeping comfortably', 'Good appetite', 'Breathlessness or grunting after the fill', 'Clear effluent'], 2,
         'High IPP also predisposes to leaks and hernias.'),
        ('IPP is measured with the child:',
         ['Sitting and eating', 'Running', 'Standing', 'At rest, lying flat'], 3,
         'Position changes pressure.'),
        ('A fill volume is outside the usual band. You:',
         ['Ask the prescriber; never correct it yourself', 'Correct it yourself', 'Program it anyway', 'Halve it'], 0,
         'The nurse verifies; the nephrologist decides.'),
        ('Why can automated PD be unsuitable for newborns (ISPD 2020, 1D)?',
         ['Newborns cannot have PD', 'Fill volumes are too small for current machines', 'Cyclers are noisy', 'Cost'], 1,
         'Manual PD may be used instead.'),
        ('Which pore type leaks protein?',
         ['Aquaporins', 'Small pores', 'Large pores', 'None'], 2,
         'Protein loss affects nutrition.'),
        ('Why is lying down different from sitting for PD?',
         ['It is not', 'Sitting removes more water', 'Gravity stops dialysis', 'Lying supine recruits more membrane'], 3,
         'Position changes the contact area.'),
        ('Height 75 cm, weight 9 kg: a 900 mL fill is about:',
         ['2,080 mL/m&sup2; and 100 mL/kg', '300 mL/m&sup2;', '690 mL/m&sup2;', '1,000 mL/m&sup2;'], 0,
         'BSA 0.43 m&sup2;; far above the band for a 1-year-old.'),
        ('Readiness for home PD includes:',
         ['Only the order', 'A trained caregiver, clean space, supplies, power plan and night contact', 'A big house', 'A car'], 1,
         'Order plus home plus people.'),
    ],
    "terms": [("Body surface area (BSA)", "Skin area in square meters estimated from height and weight."),
              ("Mosteller formula", "BSA = square root of (height in cm &times; weight in kg &divide; 3,600)."),
              ("Fill volume", "Dialysate volume run in per exchange."),
              ("Intraperitoneal pressure", "Pressure created inside the abdomen by the fill, in cmH&#8322;O."),
              ("Ultrafiltration", "Water removal across the membrane."),
              ("Three-pore model", "Description of the membrane&rsquo;s water channels, small pores and large pores.")],
    "readings": [("peritoneal-dialysis-ckd.html", "Peritoneal dialysis for families."),
                 ("dialysis-adequacy.html", "What dialysis adequacy measures and what it does not.")],
    "calcs": ["calc-pediatric-dialysis-nurse-toolkit.html", "calc-bsa.html", "calc-pd-adequacy.html"],
}
