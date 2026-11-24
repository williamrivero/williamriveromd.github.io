# -*- coding: utf-8 -*-
"""Peritoneal Dialysis Nurse, Module 11: Pediatric, acute and assisted PD.
Rewritten in the Renal Care Academy POD voice, with illustrative scenarios. Every patient and nurse is fictional. Edit here."""

MODULE = {
    "image_alt": "",
    "objectives": [
        "Distinguish chronic pediatric peritoneal dialysis (PD), acute PD for acute kidney injury (AKI), and assisted PD by who leads care, what changes clinically, and what the nurse may do.",
        "Summarize the 2020 International Society for Peritoneal Dialysis (ISPD) acute PD guidelines for adults and children, with their grades.",
        "Summarize the 2024 ISPD position paper on assisted PD and build an assistance plan.",
        "Route each context to the qualified team and recognize which tasks need additional training.",
    ],
    "big": """
<p>This course prepares you for adult chronic PD. You will still meet a child on PD, a critically ill adult on acute PD, or an older person who can no longer manage alone. This module gives you enough understanding to recognize what is different, to keep the person safe in the first hour, and to hand over to the right team.</p>
<p>It does not authorize independent practice in these areas. Pediatric PD and acute PD each need additional training and the authorization of your facility. Knowing where your competence ends is part of competence.</p>
{{plain:Think of three variations on one theme. The membrane, catheter and exchange are the same. What changes is who decides (pediatric nephrology, the acute-care team, the assisted-PD program), how small the margins are (a child&rsquo;s fill volume, an unstable patient&rsquo;s potassium), and who performs the tasks (a parent, an intensive care nurse, a paid caregiver).}}
<p>The picture has a limit. &ldquo;Same theme&rdquo; can tempt you to apply adult chronic routines everywhere. In each of these contexts the routine is different enough that applying adult defaults can cause harm: an adult fill volume in a toddler, an outpatient monitoring interval in an unstable patient, a family-training checklist for a paid caregiver who works only weekdays.</p>
{{cards:Key terms for this module|Pediatric PD::Chronic PD in children, led by pediatric nephrology.|Acute PD::PD used to treat acute kidney injury, often in unstable patients.|Assisted PD::PD in which another person performs some or all of the tasks.|Minimum standard::An option the 2020 guidelines accept where resources are limited.|Assistance plan::A written plan naming who does each task, who covers, and who supervises.}}
""",
    "case": {"title": "He can explain it, but not do it", "html": """
<p><strong>Mr. Romeo Santos, 69</strong>, a retired electrician from Cavite, has been on CAPD for three years with no peritonitis. Last week he had a stroke that weakened his right hand. He can still explain every step of the exchange, and correct the nurse when she skips one, but he cannot manage the connections.</p>
<p>His wife <strong>Nena</strong>, 66, has arthritis in both hands. Their only son works as a seafarer and is home for a few weeks a year. Romeo is in the hospital, and his discharge is being planned.</p>
""", "questions": ["What can Romeo still do, and what needs help?",
                  "Who could assist, and what must the plan specify?",
                  "Who supervises care while the team decides?"]},
    "sections": [
        ("pediatric-pd", "Pediatric PD", "Pediatric PD", """
<h3>Why PD is common in children</h3>
<p>PD avoids repeated needling, allows school attendance and can be done at home by parents. It is often the preferred modality in young children.</p>
{{fig:pd11_contexts}}
<h3>What is different</h3>
<ul>
<li>Prescriptions are scaled to body size, often body surface area, and fill volumes are small. The pediatric nephrology team sets all parameters.</li>
<li>Growth, nutrition, development, schooling and family function are central outcomes.</li>
<li>Caregiver competence and backup coverage are essential; parents may share or alternate tasks.</li>
<li>Infection assessment and treatment follow pediatric-specific ISPD guidance, not adult dosing.</li>
</ul>
<h3>In the Philippines</h3>
<p>PhilHealth Advisory 2026-0013 extended the pediatric automated PD pilot through 31 July 2026. Availability after that date and the eligible sites were not verified when this curriculum was written. Verify with PhilHealth before discussing coverage with a family.[[pd_ph_pa2026]]</p>
<h3>Your role</h3>
<p>Engage the child at a level that fits their age. Support the parents. Reinforce training. Recognize red flags: cloudy effluent, fever, poor drain, dehydration, poor feeding. Escalate to the pediatric PD team.</p>
<h3>Example: a seven-year-old in your adult clinic</h3>
<p>Bea, 7, on APD under a pediatric team in Manila, is visiting her grandmother in your province for the school break. Her mother calls your adult PD unit because the morning bag looks hazy and Bea has a stomachache.</p>
<p>You treat it exactly as you would an adult cloudy bag in urgency, and nothing like an adult in management. You screen for instability: fever, vomiting, drinking, how she looks. You ask the mother to keep the bag. Then you call Bea&rsquo;s pediatric PD team at once for direction, because the sampling, the antibiotics and their doses follow pediatric protocols. If she is unwell, she goes to the nearest emergency department that can manage children, with her pediatric team on the phone. You do not use adult antibiotic doses or adult fill volumes.</p>
{{key:With a child, be fast to recognize and quick to hand over. The pediatric team decides.}}
"""),
        ("acute-pd-for", "Acute PD", "Acute PD for acute kidney injury", """
<p>The 2020 ISPD guidelines on PD in AKI state that PD should be considered a suitable modality for AKI in all settings (adults, GRADE 1B; children, GRADE 1C). Acute PD matters most where hemodialysis or continuous therapies are scarce, and the guidelines include &ldquo;minimum standard&rdquo; options for resource-limited settings.[[pd_cullis2021]]</p>
<div class="table-wrap"><table>
<thead><tr><th>Recommendation (adults, 2020)</th><th>Grade</th></tr></thead>
<tbody>
<tr><td>PD is a suitable modality for AKI in all settings</td><td>1B</td></tr>
<tr><td>Flexible peritoneal catheters where resources and expertise exist</td><td>1B (optimal)</td></tr>
<tr><td>Rigid or improvised catheters may be used in resource-poor environments where they may be life-saving</td><td>1C (minimum standard)</td></tr>
<tr><td>Tunneled catheters to reduce peritonitis and leak</td><td>Practice point</td></tr>
<tr><td>Catheter insertion by trained nephrologists is safe, with results equivalent to surgical insertion in patients without contraindications</td><td>1B</td></tr>
<tr><td>Prophylactic antibiotics before catheter insertion</td><td>1B</td></tr>
<tr><td>Closed delivery system with a Y connection</td><td>1A (optimal)</td></tr>
<tr><td>Bicarbonate-containing solutions in critically ill patients, especially with significant liver dysfunction and marked lactate elevation</td><td>1B (optimal)</td></tr>
</tbody></table></div>
<p>For children (2020 pediatric update): PD is suitable for pediatric AKI (1C); prophylactic antibiotics before insertion (1B); a closed Y-connection system (1A); automated PD is suitable except in newborns, whose fill volumes are too small for current machines (1D).[[pd_cullis2021]][[pd_nourse2021]]</p>
<h3>What changes for nursing</h3>
<p>Acute PD patients are often unstable. Fluid removal, potassium, glucose, acid&ndash;base balance and blood pressure can change within hours. Monitoring is frequent, prescriptions change often, and exchanges may be done by intensive care unit (ICU) or ward nurses with variable PD experience. Know your facility&rsquo;s escalation, documentation and handoff procedures, and which tasks need additional training.</p>
<h3>Example: a provincial hospital with no continuous therapy</h3>
<p>After a flood, a 38-year-old farmer with leptospirosis is admitted to a provincial hospital with severe AKI. The hospital has two hemodialysis machines, both in use, and no continuous kidney replacement therapy. The nephrologist inserts an acute PD catheter at the bedside and starts acute PD.</p>
<p>The ward nurses have never done PD. The PD nurse from the outpatient unit is asked to help. Her job is not to run the prescription; the nephrologist sets that, and it may change several times a day. Her job is to teach the ward nurses the exchange technique for the closed system, set up an hourly fluid-balance sheet, make sure potassium and glucose are checked as ordered, and agree on who calls the nephrologist for what. She writes a one-page bedside guide and stays for the first two exchanges of each shift.</p>
{{key:In acute PD, the margins are hours, not weeks. Monitoring and communication matter more than technique alone.}}
"""),
        ("assisted-pd", "Assisted PD", "Assisted PD", """
<h3>Definition and scope</h3>
<p>The 2024 ISPD position paper on assisted PD notes that many people with kidney failure are older, frail, or have physical or cognitive disabilities that limit self-care PD, and may lack family support. Assistance can come from family members, paid caregivers, home-care nurses or health workers, and may be temporary, for example after a stroke or surgery, or long term. The paper states that PD should be offered to every eligible person considering maintenance dialysis, and aims to expand equitable access through assistance.[[pd_oliver2024]]</p>
<h3>Outcomes</h3>
<p>Observational comparisons, including a study of older patients, have found broadly similar survival and peritonitis-free survival between assisted and self-care PD after adjustment, even though assisted patients were older and had more illnesses.[[pd_oliver2024]] These are selected, observational groups. They support feasibility; they do not prove equivalence.</p>
{{key:An assistance plan must specify:}}
<div class="table-wrap"><table>
<thead><tr><th>Element</th><th>Content</th></tr></thead>
<tbody>
<tr><td>Task allocation</td><td>Exactly which steps the assistant performs and which the patient performs</td></tr>
<tr><td>Training</td><td>How the assistant was trained, by whom, and how competence was verified</td></tr>
<tr><td>Coverage</td><td>Days, times, and who covers absences</td></tr>
<tr><td>Escalation</td><td>Whom the assistant calls for each problem</td></tr>
<tr><td>Backup</td><td>What happens if the assistant is unavailable</td></tr>
<tr><td>Supervision</td><td>Which clinician keeps clinical oversight</td></tr>
<tr><td>Review</td><td>Reassessment date and triggers: change in function, living arrangement or caregiver</td></tr>
</tbody></table></div>
<h3>Example: the gap in a good plan</h3>
<p>Lola Felicidad&rsquo;s assistance plan looked complete: a trained paid caregiver for her APD setup, Monday to Saturday evenings. Nobody had written down Sundays. The caregiver went home to her family on Sunday nights, and for three weeks Lola Felicidad skipped therapy every Sunday, embarrassed to call. Her weight crept up.</p>
<p>At the review, Nurse Celia finds the gap in the treatment record, not in the plan. She arranges for a niece to be trained for Sunday setup, adds the niece and the hotline to the plan, and books a check after the first Sunday.</p>
{{key:Read the plan against the calendar. Every day and every absence needs a name.}}
"""),
    ],
    "debrief": ["""
<p><strong>What Romeo can still do.</strong> Nurse <strong>Celia</strong> obtains his consent and assesses his remaining abilities. He can verify supplies against the order, inspect the effluent, record volumes, recognize problems and call the hotline. His knowledge is intact; only his hands have changed. He keeps those tasks.</p>
<p><strong>Who could assist.</strong> Nena can manage some steps safely with adapted grips, but four manual exchanges a day would strain her hands. Celia raises two questions with the team: whether APD with Nena doing a single evening setup would be more feasible than four daily manual exchanges, and whether a home-care nurse or trained helper could support them for the first weeks while Romeo recovers. If assistance is arranged, the plan names each task, the trained person, coverage for every day, escalation, backup when the helper is absent, the supervising clinician and a review date. Their son can be trained as backup during his visits home, but cannot be the plan.</p>
<p><strong>Who supervises while the team decides.</strong> Romeo stays on hospital-based exchanges per order, under the inpatient team with the PD unit&rsquo;s support. Celia documents who performs each exchange, the interim supervision plan and the reassessment date. A stroke is a retraining trigger, so whoever takes over is trained and observed before discharge.</p>
"""],
    "skills": {"title": "Practice drill",
               "intro": "Complete both tasks and discuss them with your preceptor.",
               "items": [("Develop a one-page assistance plan for the stroke case.", False),
                         ("Write two sentences each on how the plan would differ for a 6-year-old on PD and for an unstable adult on acute PD in the ICU.", False)]},
    "quiz": [
        ("What must an assistance plan specify?",
         ["Task allocation, trained personnel, coverage, escalation, backup and supervision", "Only the caregiver&rsquo;s name", "Only the prescription", "The patient&rsquo;s income"], 0,
         "Each element closes a gap where therapy could be missed or done unsafely."),
        ("Which team verifies pediatric prescriptions and infection protocols?",
         ["The adult PD nurse", "The pharmacist alone", "The pediatric nephrology and PD team, using age-appropriate standards", "The parents"], 2,
         "Adult defaults can harm a child. The pediatric team decides."),
        ("According to the 2020 ISPD acute PD guideline for adults, PD is:",
         ["Unsuitable for AKI", "Only for children", "Only for high-income settings", "A suitable modality for AKI in all settings (1B)"], 3,
         "The guideline supports PD for AKI everywhere, with minimum-standard options for limited resources."),
        ("Which acute PD recommendation carries GRADE 1A?",
         ["Rigid catheters", "A closed delivery system with a Y connection", "Locally prepared fluids", "Tunneling"], 1,
         "The closed Y system is 1A (optimal) for adults and children."),
        ("Bicarbonate-containing solutions are recommended in acute PD particularly for:",
         ["Stable outpatients", "Critically ill patients with significant liver dysfunction and marked lactate elevation (1B)", "Children only", "No one"], 1,
         "A damaged liver handles lactate poorly, so bicarbonate solutions are preferred."),
        ("Why is automated PD not suitable for newborns in the 2020 pediatric guideline?",
         ["Newborns cannot have PD", "Cyclers are too loud", "Cost", "Fill volumes are too small for current machines"], 3,
         "The recommendation is graded 1D; it reflects machine limits, not unsuitability of PD itself."),
        ("How should the pediatric automated PD benefit be discussed with a family?",
         ["Verify current status with PhilHealth first, because the reviewed extension ended 31 July 2026", "State it is available nationwide", "Say it does not exist", "Avoid the topic"], 0,
         "Coverage after that date was not verified. Never promise a benefit you have not confirmed."),
        ("What does the 2024 ISPD position paper say about offering PD?",
         ["Only to young patients", "Only with family support", "PD should be offered to every eligible person considering maintenance dialysis", "Never to older adults"], 2,
         "Assistance is the tool for widening that access."),
        ("Observational studies comparing assisted and self-care PD in older patients found:",
         ["Assisted PD always worse", "Randomized proof of superiority", "Broadly similar adjusted survival and peritonitis-free survival", "No data"], 2,
         "They support feasibility but cannot prove equivalence."),
        ("Bea, 7, visiting from Manila, has a hazy bag and a stomachache. What is the adult PD nurse&rsquo;s role?",
         ["Screen for instability, keep the bag, and call her pediatric PD team at once", "Start adult antibiotic doses", "Wait until she returns to Manila", "Change her fill volume"], 0,
         "Recognize urgently, hand over quickly. Pediatric protocols govern sampling and treatment."),
        ("Why is acute PD monitoring more intense than chronic PD?",
         ["Catheters are different colors", "Fluid, potassium, glucose, acid&ndash;base balance and blood pressure can change within hours", "It is not", "Patients are always children"], 1,
         "Unstable patients need hourly attention, not monthly review."),
        ("A stroke patient can explain PD but cannot manage the connections. First step?",
         ["Transfer to hemodialysis immediately", "Ask him to try harder", "Stop dialysis", "With consent, assess his remaining abilities and the available caregivers, and coordinate evaluation for assisted PD"], 3,
         "He keeps the tasks he can do safely; the rest are reassigned and verified."),
        ("Lola Felicidad skipped therapy every Sunday because her caregiver was off. What was missing from the plan?",
         ["Task allocation", "Coverage for every day, with a named backup", "The prescription", "Exit-site care"], 1,
         "Read the plan against the calendar. Every absence needs a name."),
        ("Catheter insertion by trained nephrologists in acute PD is:",
         ["Unsafe", "Safe, with results equivalent to surgical insertion in patients without contraindications (1B)", "Banned", "Unstudied"], 1,
         "This is one reason acute PD can be started where surgical teams are scarce."),
        ("Which statement fits this module&rsquo;s level?",
         ["It authorizes independent pediatric and acute PD practice", "It replaces pediatric training", "It provides orientation; independent practice needs additional training and authorization", "It is optional reading for nephrologists only"], 2,
         "Recognize, keep safe, hand over. Independent practice needs more."),
    ],
    "terms": [("Peritoneal dialysis (PD)", "Dialysis that uses the lining of the abdomen as the filter, with fluid run in and out through a catheter."),
              ("CAPD", "Continuous ambulatory peritoneal dialysis: manual exchanges through the day."),
              ("APD", "Automated peritoneal dialysis: a cycler performs exchanges, usually overnight."),
              ("AKI", "Acute kidney injury: a rapid fall in kidney function over hours to days."),
              ("ICU", "Intensive care unit."),
              ("Tunnel", "The path of the catheter under the skin between the cuffs."),
              ("Peritonitis", "Infection or inflammation of the peritoneum, usually shown by cloudy effluent."),
              ("Effluent", "Fluid drained from the abdomen after a dwell."),
              ("Assisted PD", "PD in which a family member, paid caregiver or health worker performs some tasks."),
              ("Acute PD", "PD used to treat acute kidney injury, often in unstable patients."),
              ("Assistance plan", "A written plan naming who does each task, who covers absences and who supervises.")],
    "readings": [("adding-peritoneal-dialysis-program.html", "Building a PD program, including assisted PD.")],
    "calcs": ["calc-pediatric-egfr.html", "calc-aki-staging.html", "calc-frailty-assessment.html"],
}
