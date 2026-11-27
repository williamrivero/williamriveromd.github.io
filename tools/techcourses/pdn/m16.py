# -*- coding: utf-8 -*-
"""Pediatric Dialysis Nurse, Module 16: AKI, acute PD and continuous kidney replacement therapy. POD voice. Fictional cases."""

MODULE = {
    "image_alt": "",
    "objectives": [
        "Describe how common acute kidney injury (AKI) is in critically ill children and why urine output matters as much as creatinine.",
        "Calculate percent fluid overload and explain what the registry association does and does not show.",
        "Support acute PD for AKI in a ward with limited resources, using the 2020 ISPD pediatric grades.",
        "Recognize the limits of this module for continuous kidney replacement therapy (CKRT) and neonatal care.",
    ],
    "big": """
<p>AKI in a critically ill child develops over hours, often alongside sepsis, heart surgery, dehydration or infections such as leptospirosis. Fluid given to keep the child alive accumulates when the kidneys stop excreting it, and the extra water stiffens the lungs and swells the tissues.</p>
<p>Your work in this module is orientation, not authorization. You will learn to count fluid overload, to support acute PD where it is the available therapy, and to know when a child needs a team with intensive care and CKRT expertise.</p>
{{plain:Think of a critically ill child as a boat being bailed by the kidneys. Every infusion is water poured in to keep the boat afloat. When the bailing stops, the boat sits lower and lower, and soon it is the water itself that threatens to sink it.}}
<p>The picture has a limit. In the boat, more water is always worse. In a child in shock, fluid can be life-saving in the first hours; the problem is fluid that keeps accumulating after it has done its job. The timing and goal belong to the intensive care and nephrology team.</p>
{{cards:Key terms for this module|AKI::A rapid fall in kidney function over hours to days, defined by creatinine or urine output.|Percent fluid overload (%FO)::Net fluid gained as a share of admission weight.|Acute PD::PD used to treat AKI, often in unstable children.|CKRT::Continuous kidney replacement therapy: slow, round-the-clock blood purification in intensive care.|Oliguria::Low urine output, in children usually below 0.5 mL/kg/h for hours.}}
""",
    "case": {"title": "After the flood", "html": """
<p><strong>Nonoy Aguilar, 9</strong>, 25 kilograms, is admitted to a provincial hospital after floodwater exposure, with leptospirosis, oliguria and rising creatinine. Over 48 hours he has received 3.8 liters and passed 1.3 liters; he now has crackles in both lungs. The hospital has no CKRT and two adult hemodialysis machines, both in use. The pediatric nephrologist inserts an acute PD catheter. <strong>Nurse Hazel</strong>, from the outpatient PD unit, is called to help the ward nurses.</p>
""", "questions": ["What is Nonoy&rsquo;s percent fluid overload?",
                  "Is PD a reasonable choice here, and on what evidence?",
                  "What is Hazel&rsquo;s role, and what is not?"]},
    "sections": [
        ("aki-in-children", "AKI in children", "AKI in critically ill children", """
<p>The Assessment of Worldwide Acute Kidney Injury, Renal Angina, and Epidemiology (AWARE) study screened 4,683 children and young adults in 32 pediatric intensive care units. AKI developed in 26.9% and severe AKI in 11.6%. Death by day 28 occurred in 11.0% of those with severe AKI versus 2.5% without it, an adjusted odds ratio of 1.77. Creatinine alone missed AKI in 67.2% of the patients with low urine output.[[pdn_kaddourah2017]]</p>
<p>That last finding is a nursing finding. Hourly urine output, measured accurately and expressed in mL/kg/h, detects AKI that the laboratory misses. A Philippine series of children with leptospirosis found 62% oliguric at presentation, with PD started in 36% of them.[[pdn_anacleto2014]]</p>
{{key:Measure urine output by the hour and per kilogram. In AKI, the urine bag often speaks before the laboratory.}}
"""),
        ("fluid-overload", "Fluid overload", "Percent fluid overload", """
<p>In the prospective pediatric CRRT registry, fluid overload was defined as (fluid in minus fluid out, in liters) divided by the intensive care admission weight in kilograms, times 100. Among 297 children, mortality was 29.4% with less than 10% overload, 43.1% with 10% to 20%, and 65.6% with 20% or more; each 1% increase was associated with about 3% higher odds of death after adjustment.[[pdn_sutherland2010]]</p>
{{fig:pdn16_a}}
{{formula:%FO = (fluid in (L) &minus; fluid out (L)) &divide; admission weight (kg) &times; 100<br>Example: in 3.8 L, out 1.3 L, admission weight 25 kg &rarr; (3.8 &minus; 1.3) &divide; 25 &times; 100 = 10%}}
<p>The registry was observational. Sicker children receive more fluid and also die more often, so the association does not prove that removing fluid earlier saves lives; the authors say so. What it does show is that the percentage is worth tracking, and the nurse is the person who keeps the numbers honest: every infusion, flush, drug and feed in; every urine, drain and dialysis removal out.</p>
{{key:Track percent fluid overload from admission weight. Accurate counting is the nurse&rsquo;s contribution to the decision.}}
"""),
        ("acute-pd", "Acute PD", "Acute PD where machines are scarce", """
<p>The 2020 ISPD pediatric guideline on PD in AKI grades PD as suitable for AKI in children (1C), recommends prophylactic antibiotics before catheter insertion (1B) and a closed delivery system with a Y connection (1A), and notes that automated PD is suitable except in newborns, whose fill volumes are too small for current machines (1D).[[pd_nourse2021]] Acute PD matters most where hemodialysis and CKRT are scarce, which describes many Philippine provincial hospitals.</p>
{{fig:pdn16_b}}
<p>Acute PD in an unstable child changes fast. Fill volumes usually start small and rise as tolerated; dwells are short; potassium, glucose, sodium, acid&ndash;base status and blood pressure can change within hours. The nephrologist sets and revises the prescription. The PD nurse&rsquo;s contribution in a ward new to PD is to teach the closed-system exchange, set up an hourly balance sheet, make sure ordered laboratory tests happen on time, and agree with the ward on who calls whom for what.</p>
{{scene:Hazel on the ward|<p>Hazel calculates Nonoy&rsquo;s overload at 10%. She shows two ward nurses the closed-system exchange with a Y set, writes a one-page bedside guide, and sets up an hourly sheet: fill, drain, net balance, urine, intake, blood pressure, breathing rate. She agrees with the nephrologist on call thresholds and stays for the first two exchanges of each shift.</p><p class="tc-scene-take">In acute PD, communication and counting matter as much as technique.</p>}}
{{key:Acute PD is graded as suitable for pediatric AKI. The nurse brings technique, counting and clear escalation; the nephrologist brings the prescription.}}
"""),
        ("ckrt-orientation", "CKRT", "Orientation to CKRT and neonatal therapy", """
<p>CKRT runs slowly around the clock through a blood circuit and is used in intensive care for unstable children. The circuit-size problem of Module 13 is sharper still in infants. Machines designed for neonates have reduced it: the CARPEDIEM device, first used in a 2.9 kg newborn, has a circuit prime of under 30 mL.[[pdn_ronco2014]] That report described a single patient, so it shows feasibility, not general outcomes.</p>
<p>This module does not prepare you to run CKRT, prime neonatal circuits, manage citrate or heparin anticoagulation, or care for children on extracorporeal membrane oxygenation. Those need a separate pediatric intensive care pathway with device-specific training and authorization. What you can do now is understand the language, keep fluid records exact, and recognize when a child on your ward needs that team.</p>
{{key:Recognize the child who needs pediatric intensive care and CKRT. Running it is a separate qualification.}}
"""),
    ],
    "debrief": ["""
<p><strong>The percentage.</strong> (3.8 &minus; 1.3) L &divide; 25 kg &times; 100 = 10%, with crackles in both lungs.</p>
<p><strong>Is PD reasonable?</strong> Yes. The 2020 ISPD pediatric guideline grades PD as suitable for pediatric AKI (1C), and it is the available therapy here. A closed Y system (1A) and antibiotic prophylaxis before insertion (1B) are recommended.</p>
<p><strong>Hazel&rsquo;s role.</strong> Teach the exchange, set up hourly balances, make sure ordered tests and call thresholds are in place, and support the ward. She does not set or change the prescription, and she escalates to transfer if Nonoy deteriorates beyond what the ward can provide.</p>
"""],
    "skills": {"title": "AKI and acute PD support", "intro": "Use fictional PICU and ward charts.",
               "items": [("Calculates urine output in mL/kg/h from hourly measurements", False),
                         ("Calculates percent fluid overload from admission weight with an independent check", True),
                         ("Teaches a closed-system acute PD exchange to a ward nurse", False),
                         ("Sets up an hourly balance sheet and agreed call thresholds", True),
                         ("States the limits of own scope for CKRT and neonatal circuits", True)]},
    "quiz": [
        ('In AWARE, AKI developed in about what share of PICU patients?',
         ['27%', '5%', '60%', '90%'], 0,
         '26.9%; severe AKI 11.6%.'),
        ('28-day death with severe AKI versus without, in AWARE:',
         ['50% vs 5%', '11.0% vs 2.5%', '1% vs 1%', '30% vs 25%'], 1,
         'Adjusted odds ratio 1.77.'),
        ('In AWARE, creatinine alone missed AKI in what share of patients with low urine output?',
         ['10%', '33%', '67%', '100%'], 2,
         'Urine output matters.'),
        ('Percent fluid overload uses:',
         ['Current weight', 'Ideal weight', 'Target weight', 'Admission weight'], 3,
         '(in &minus; out) &divide; admission weight &times; 100.'),
        ('In 3.8 L, out 1.3 L, admission 25 kg:',
         ['10%', '5%', '15%', '25%'], 0,
         '2.5 &divide; 25 &times; 100.'),
        ('In the pCRRT registry, mortality with 20% or more overload was:',
         ['29.4%', '65.6%', '43.1%', '90%'], 1,
         'Versus 29.4% below 10%; observational.'),
        ('Does the registry prove that early fluid removal saves lives?',
         ['Yes', 'Only in adults', 'No; it is an observational association', 'Only for neonates'], 2,
         'Sicker children receive more fluid.'),
        ('ISPD 2020 pediatric grade for PD as suitable in AKI:',
         ['1A', '2D', 'Not graded', '1C'], 3,
         'Children: 1C.'),
        ('Closed delivery system with a Y connection in pediatric acute PD:',
         ['1A', '2C', 'Practice point', 'Not recommended'], 0,
         'A strong recommendation.'),
        ('Prophylactic antibiotics before acute PD catheter insertion in children:',
         ['2D', '1B', 'Not graded', 'Contraindicated'], 1,
         'Recommended.'),
        ('Automated PD in newborns, per ISPD 2020:',
         ['Suitable', 'Required', 'Not suitable; fills too small for machines (1D)', 'Not mentioned'], 2,
         'Manual acute PD is used.'),
        ('The PD nurse supporting a ward new to acute PD should:',
         ['Change the prescription as needed', 'Take over all exchanges for days', 'Avoid the ward', 'Teach technique, set up hourly balances and agree call thresholds'], 3,
         'The nephrologist owns the prescription.'),
        ('CARPEDIEM&rsquo;s circuit prime is:',
         ['Under 30 mL', 'About 300 mL', '1 L', 'Not stated'], 0,
         'Reported in a single neonate; feasibility only.'),
        ('Does this module authorize you to run CKRT?',
         ['Yes', 'No; that needs a separate PICU pathway and device training', 'Only at night', 'Only for teenagers'], 1,
         'Orientation only.'),
        ('Pediatric oliguria is usually defined as urine output below about:',
         ['5 mL/kg/h', '50 mL/h', '0.5 mL/kg/h for hours', '1 L/day'], 2,
         'As in the AWARE severe AKI definition (for 12 hours or more).'),
    ],
    "terms": [("AKI", "Acute kidney injury: a rapid fall in kidney function."),
              ("Percent fluid overload", "Net fluid gained as a percentage of admission weight."),
              ("Oliguria", "Low urine output."),
              ("Acute PD", "PD used to treat AKI."),
              ("CKRT", "Continuous kidney replacement therapy."),
              ("Y set", "A closed PD tubing system that allows flush before fill.")],
    "readings": [("leptospirosis-nephropathy.html", "Leptospirosis and the kidney."),
                 ("neonatal-acute-kidney-injury-clinician.html", "Neonatal acute kidney injury."),
                 ("crrt-continuous-renal-replacement-therapy.html", "Continuous kidney replacement therapy.")],
    "calcs": ["calc-pediatric-dialysis-nurse-toolkit.html", "calc-pediatric-aki.html", "calc-pediatric-uo.html", "calc-fluid-overload.html"],
}
