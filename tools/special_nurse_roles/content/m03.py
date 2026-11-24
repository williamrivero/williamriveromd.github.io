# -*- coding: utf-8 -*-
MODULE = {
    "sub": "How germs and blood travel around a dialysis station, why hepatitis B survives on surfaces, how to observe a task and feed back without blame, how to count infections with the right denominator, and what to do in the first hour of a suspected cluster.",
    "desc": "Special Dialysis Nurse Roles Module 3: the infection prevention and control nurse in a hemodialysis unit. Transmission routes, CDC core interventions, DART observation and feedback, surveillance per 100 patient-months, hepatitis precautions, cluster response and stewardship.",
    "keywords": "dialysis infection prevention nurse, hemodialysis bloodstream infection surveillance, CDC core interventions dialysis, DART audit tools, hand hygiene audit feedback, hepatitis B isolation dialysis, outbreak line list dialysis",
    "image_alt": "A Filipino infection prevention nurse with a clipboard quietly observing a colleague performing hand hygiene beside a dialysis station.",
    "objectives": [
        "Map the routes by which germs and blood travel through a dialysis session and name the barrier at each.",
        "Conduct structured observations and give corrective feedback that fixes systems rather than blames people.",
        "Keep surveillance with written definitions and denominators, stratified by access type.",
        "Recognize and escalate a suspected cluster, preserve the evidence, and support antimicrobial stewardship.",
    ],
    "sections": [
        {"id": "model", "nav": "Mental model", "tag": "Intuition", "h2": "A busy kitchen where blood is the raw ingredient",
         "html": """
<p>Picture a restaurant kitchen at lunch rush. Raw chicken is handled at one counter, salad at another. Food poisoning rarely comes from one dramatic mistake. It comes from a cloth that wiped the chicken board and then the salad bowl, a hand that touched the bin and then the plate, a tray carried from one counter to the next. A dialysis unit is that kitchen, with blood as the raw ingredient and twenty patients sharing one room, one sink, one supply cart and the same staff for four hours.</p>
<p>The picture has a limit. In a kitchen you can often see the raw chicken. In a dialysis unit, the dangerous material is usually invisible: a microscopic film of blood on a machine knob, bacteria on a catheter hub, a virus on a clamp. That is why infection prevention in dialysis is built on routines done the same way every time, whether or not anything looks dirty, and why the infection prevention nurse watches routines rather than waiting for infections.</p>
<div class="tc-plain"><span class="tc-lab">In plain words</span>Your job is to find the cloth that goes from the chicken to the salad before anyone gets sick, and to fix the kitchen, not to shame the cook.</div>
"""},
        {"id": "routes", "nav": "How germs travel", "tag": "Mechanism", "h2": "Follow the contamination pathway",
         "html": """
<p>Three kinds of infection dominate dialysis, and each travels differently.</p>
<div class="table-wrap"><table>
<thead><tr><th>Threat</th><th>How it travels</th><th>The barrier that matters most</th></tr></thead>
<tbody>
<tr><td>Bacteria into the bloodstream (often <em>Staphylococcus aureus</em>)</td><td>From skin and hands into the catheter hub or needle site; catheters bypass the skin barrier completely</td><td>Hand hygiene; aseptic catheter connection and disconnection; exit-site care; aseptic cannulation; fewer catheters</td></tr>
<tr><td>Bloodborne viruses (hepatitis B, hepatitis C)</td><td>Tiny amounts of blood on surfaces, gloves, shared vials, clamps, trays or carts, carried to another patient's access or injection</td><td>Clean and dirty zones; no shared supplies between stations; single-patient vials; disinfection of every surface between patients; hepatitis B vaccination and screening</td></tr>
<tr><td>Respiratory germs (influenza, COVID-19, tuberculosis)</td><td>Droplets and air in a crowded room for hours</td><td>Screening at the door, masks, spacing, ventilation, vaccination, early isolation</td></tr>
</tbody></table></div>
<p><strong>Why hepatitis B is the dialysis virus.</strong> Hepatitis B virus survived drying and storage for a week in a classic laboratory study, and remained able to infect.[[bond1981]] A patient can be highly infectious with no symptoms. Patients on dialysis are exposed to each other's blood environment three times a week. This combination explains why outbreaks in dialysis units have been traced again and again to everyday lapses: supplies carried from one station to another, medication vials used for more than one patient, and surfaces not disinfected between patients.[[thompson2009]] It also explains why the separate room, machine and staff for patients positive for hepatitis B surface antigen are kept, under current DOH and unit policy and long-standing CDC recommendations.[[cdc2001]] For hepatitis C, KDIGO advises strict standard precautions for every patient rather than relying on isolation; follow your unit's current policy.[[hcv2022]]</p>
<div class="tc-keyp"><span class="tc-lab">Remember</span>Nothing crosses from one station to another unless it has been cleaned and disinfected, or it is single-use. A tray, a clamp, a tape roll and a pen all count.</div>
"""},
        {"id": "evidence", "nav": "What works", "tag": "Evidence", "h2": "What the evidence shows",
         "html": """
<p><strong>Bundles with audit and feedback.</strong> In a CDC collaborative, 17 outpatient hemodialysis facilities adopted a package: chlorhexidine for catheter exit-site care, staff training and competency checks on catheter care and aseptic technique, hand hygiene and access-care audits, and feedback of infection and audit results to staff. Pooled bloodstream infection rates fell from 1.09 to 0.89 per 100 patient-months, and access-related bloodstream infections from 0.73 to 0.42. Modeled rates fell 32 percent and 54 percent at the start of the intervention.[[patel2013]] This was a quality improvement project without a control group in volunteer facilities, so the effect size may not transfer exactly. It is, however, the evidence base for the CDC Core Interventions that dialysis units now use.[[cdc_core]]</p>
<p><strong>Hand hygiene is a system property.</strong> In a landmark hospital-wide program in Geneva, observed hand hygiene compliance rose from 48 to 66 percent over three years with alcohol hand rub at the bedside, posters and feedback, while hospital-acquired infections fell from 16.9 to 9.9 percent.[[pittet2000]] This was an observational before-and-after study, and other changes may have contributed. The durable lesson is that compliance rises when rub is within arm's reach and feedback is regular, not when staff are scolded.</p>
<p><strong>Observation tools.</strong> The CDC Dialysis Audit and Reporting Tools (DART) are checklists for specific tasks: hand hygiene, catheter connection and disconnection, exit-site care, cannulation and decannulation, injectable medication preparation, and station disinfection.[[cdc_dart]] They make an observation reproducible: two nurses watching the same task should score the same steps.</p>
<div class="tc-plain"><span class="tc-lab">How certain are we?</span>Moderate: audits with feedback plus catheter-care training are followed by fewer bloodstream infections (before-and-after data, consistent across settings). Established: hepatitis B survives on dry surfaces. Practice point: no item moves between stations without disinfection.</div>
<p><strong>Your role and its limits.</strong> The WHO treats infection prevention and control as a profession with its own competencies, from surveillance to outbreak management.[[who_ipc]] A dialysis infection prevention nurse is usually a unit champion working with the hospital's infection control team, not a replacement for it. You do not prescribe antibiotics, decide public-health reporting alone, or run occupational health; you coordinate with the people who do.</p>
"""},
        {"id": "observe", "nav": "Observe and feed back", "tag": "Practice", "h2": "Observe a task, then improve the system",
         "html": """
<ol class="tc-flow">
<li><b>Choose the task</b>Start with the riskiest: catheter connection and disconnection.</li>
<li><b>Use a checklist</b>The DART tool or your unit's version, so every observer scores the same steps.</li>
<li><b>Observe openly</b>Staff know audits happen; you sample all shifts, including weekends.</li>
<li><b>Feed back at once</b>Privately for the individual, as unit data for the team.</li>
<li><b>Ask why</b>Was the rub empty? Were gloves out of reach? Was the step unclear?</li>
<li><b>Fix and remeasure</b>Change the system, then observe again.</li>
</ol>
<div class="tc-scene"><span class="tc-lab">Saturday afternoon &middot; fictional</span><p>Nurse Benjo's weekday hand hygiene audits average 88 percent. On a Saturday he observes 24 opportunities and counts 13 hand hygiene actions: 54 percent. Most misses are after touching the machine and before touching the catheter.</p><p>Instead of a memo telling staff to try harder, he walks the floor. Two of the three alcohol rub dispensers on the Saturday side are empty; the Saturday utility worker refills them only on weekdays. He arranges a refill checklist for every shift and mounts a small rub bottle on each machine. Four weekends later, Saturday compliance is 21 of 25, 84 percent.</p><p class="tc-scene-take"><b>What this shows.</b> The miss pattern pointed to a supply problem. The fix was a system change, and the result was remeasured, not assumed.</p></div>
<div class="sd-calc"><span class="tc-lab">Worked example &middot; Portfolio Toolkit, tool 1</span>13 of 24 is 54 percent, with a 95 percent range of about 35 to 72 percent. 21 of 25 is 84 percent, with a range of about 65 to 94 percent. The ranges barely overlap, which supports a real change, but four weekends is a short run; Benjo keeps plotting weekly on a run chart (Module 6).</div>
"""},
        {"id": "surveillance", "nav": "Surveillance", "tag": "Measurement", "h2": "Make surveillance reproducible",
         "html": """
<p>Surveillance means counting the same thing the same way every month so that a change in the number reflects a change in reality, not a change in counting. Three rules make it work.</p>
<p><strong>1. One written definition.</strong> Decide, with the physician and infection control team, what counts as a bloodstream infection event (for example, a positive blood culture in an outpatient or within the first day of admission, with rules for repeat cultures). Write it down. Apply it the same way every month, even when the result is embarrassing.</p>
<p><strong>2. The right denominator.</strong> Infection rates in dialysis are expressed per 100 patient-months: one patient dialyzing in the unit for a whole month contributes one patient-month. Count patient-months separately for fistulas, grafts and catheters, because catheter risk is many times higher.[[patel2013]] A unit that converts patients from catheters to fistulas may see its overall rate fall even if catheter care has not improved, and the opposite.</p>
<p><strong>3. Look at events, not only rates.</strong> With 50 patients, one infection moves the monthly rate a lot. Review each event as a case: access type, organism, last catheter-care observation, recent hospital stay, antibiotic given.</p>
<div class="tc-stop"><span class="tc-lab">Stop and check</span>Never change the definition or drop events to make a month look better. If the definition must change, mark the date on the chart so everyone knows the series has a break.</div>
"""},
        {"id": "cluster", "nav": "Clusters", "tag": "Response", "h2": "Respond promptly and preserve the evidence",
         "html": """
<p>A cluster is more cases than expected in a short time or place: two bloodstream infections on the same shift, a new hepatitis C conversion, three patients with fever on the same water loop. The first hour matters, and the order is always patient care first, then evidence, then investigation.</p>
<ol class="tc-flow">
<li><b>Treat</b>The charge nurse and physician manage the sick patients: vital signs, cultures before antibiotics as ordered, transfer if needed.</li>
<li><b>Contain</b>Take suspected shared items out of use; do not throw them away.</li>
<li><b>Preserve</b>Bag and label the tray, vials, lines or solutions; note lot numbers; keep the machine and station as they are if the physician or infection control asks.</li>
<li><b>List</b>Start a line list: patient code, station, shift, access, onset time, symptoms, cultures, staff assigned.</li>
<li><b>Notify</b>Head nurse, clinical head, hospital infection control; public-health reporting is decided by them under current rules.</li>
<li><b>Look for the common source</b>Shared supplies, medication preparation, water and machines (Module 12), a staff member's technique.</li>
</ol>
<div class="tc-scene"><span class="tc-lab">Second shift, 11:05 a.m. &middot; fictional</span><p>Two patients with tunneled catheters, at stations 9 and 10, develop rigors within 40 minutes of each other. One has a blood pressure of 82/50. The charge nurse and physician take the bedside. Nurse Benjo notices a supply tray with gauze, a shared tape roll and an open box of caps that has moved between the two stations all morning.</p><p>He takes the tray out of use, bags and labels it with the time, and writes down the lot numbers of the catheter caps and the heparin vials used. He starts a line list, informs the head nurse and the hospital infection control nurse, and asks the physician whether blood cultures were drawn before the first antibiotic dose. They were.</p><p class="tc-scene-take"><b>What this shows.</b> The infection nurse supports care, then preserves what an investigation will need. Throwing the tray away "to be safe" would have destroyed the evidence.</p></div>
<p><strong>Stewardship.</strong> Antibiotics in dialysis are often started empirically and continued by habit. The CDC core elements for hemodialysis stewardship ask for blood cultures before the first dose, a review when results return, and a stop or narrowing decision documented by the prescriber.[[cdc_steward]] Your part: make sure cultures are drawn as ordered before the dose, results reach the prescriber, and the review date is on the chart.</p>
"""},
    ],
    "case": {
        "title": "The shared tray",
        "html": """
<p><strong>Tuesday, second shift.</strong> At 11:00 a.m. Mrs. Dela Paz (station 9, tunneled catheter) has rigors and a temperature of 38.9 °C; her blood pressure is 82/50. At 11:40 Mr. Ocampo (station 10, tunneled catheter) has rigors too. Both were connected by the same nurse this morning, from a supply tray that has moved between stations 9, 10 and 11 since 7:00. Station 11's patient has a fistula and is well.</p>
<p>A nursing aide says, "I'll throw the tray out and clean everything so it doesn't spread." The unit had one catheter infection in the previous three months.</p>
""",
        "acte": {
            "Assess": "Two catheter patients, same shift, same nurse, shared tray: a possible common-source cluster. One patient is hemodynamically unstable and comes first. Station 11 may also have been exposed.",
            "Communicate": "Support the charge nurse and physician with immediate care. Stop the aide from discarding the tray; bag and label it. Notify the head nurse, clinical head and hospital infection control the same hour. Confirm that blood cultures were drawn before antibiotics.",
            "Teach": "Explain to the aide why the tray is evidence and why nothing moves between stations. Brief the shift without blaming the connecting nurse; ask her to describe her steps for the review.",
            "Escalate": "Start the line list; flag station 11's patient for monitoring. Ask infection control to decide on observation of catheter connections across shifts and any public-health notification.",
        },
        "outcome": """
<p>Both cultures grew the same organism. Infection control observed connection technique on all shifts within 48 hours and found that caps were being placed on the shared tray between uses. Single-station supply kits were introduced the next week. Over the following four months there were no further catheter bloodstream infections, which the team reported as "zero events over 72 catheter patient-months," not as proof of a cure.</p>
""",
        "task": "Draft the line list header and the first two rows, and a three-line note to the head nurse that states facts, actions taken and the decision you need, without naming the connecting nurse.",
    },
    "second_round": ("A month later, a routine screen shows a new hepatitis C antibody in a patient previously negative. He dialyzes at station 10.",
                     "A response plan that lists what you would check (recent exposures, station history, vial and supply practice, staff assignments, previous negative date) and whom you would notify, under current DOH and unit policy."),
    "evidence_out": "Ten DART-style observations with feedback, one month of stratified surveillance, and a simulated cluster response.",
    "critical": "Discarding suspected source items before review, or carrying any non-disinfected item between stations.",
    "reflect": "Name one object in your unit that travels between stations every day. Who disinfects it, when, and how would you know if they did not?",
    "practice": {
        "intro": "Observe openly, with staff aware that audits happen, and use synthetic data for exercises.",
        "items": [
            "Complete ten observations with a DART-style checklist across at least three shifts, including a weekend.",
            "Give private feedback after each observation and record one system cause for each miss.",
            "Calculate one month of bloodstream infection rates per 100 patient-months, separately for each access type.",
            "Walk the unit and map every object that moves between stations; propose one change.",
            "Run a tabletop cluster exercise with the charge nurse and infection control.",
        ],
    },
    "job_aid": ("Cluster line list (one row per patient)", [
        "Patient code, station, shift, date",
        "Access type; connecting nurse code",
        "Onset time and first symptom",
        "Vital signs at onset; transferred (yes/no)",
        "Blood culture drawn (time) before antibiotic (time)",
        "Organism (when known)",
        "Items preserved (description, lot numbers)",
        "Shared exposures (tray, vial, machine, water loop)",
        "Notified (name, time)",
        "Follow-up owner and date",
    ]),
    "metric": "Hand hygiene adherence (actions performed divided by observed opportunities), trended weekly; and bloodstream infections per 100 patient-months, stratified by access type, with a separate written definition. Never combine the two in one number.",
    "readings": [
        ("dialysis-access-infection.html", "Access infection from the patient's side."),
        ("antibiotic-stewardship-dialysis.html", "Stewardship in the dialysis unit."),
        ("viral-infections-vaccinations-ckd.html", "Hepatitis B and other vaccinations in kidney disease."),
    ],
    "academy": [("Dialysis Unit Support Staff Module 3: How germs travel", "dialysis-unit-support-staff-03-how-germs-travel.html")],
    "calcs": ["calc-dialysis-nurse-portfolio-toolkit.html", "calc-access-infection-rate.html"],
    "terms": [
        ("Patient-month", "One patient dialyzing in the unit for one month; the usual denominator for dialysis infection rates."),
        ("Line list", "A table with one row per affected patient, used to look for a common source in a suspected cluster."),
        ("Cluster", "More cases than expected in a short time or place, raising the possibility of a common source."),
        ("Stewardship", "Coordinated efforts to use antibiotics only when needed, at the right dose and duration."),
    ],
    "quiz": [
        {"stem": "Why is hepatitis B a particular concern in hemodialysis units?",
         "options": [["It survives drying on surfaces for days and infected patients may have no symptoms.", True, "Environmental survival plus silent infection allows transmission through shared surfaces and items."],
                     ["It spreads only by droplets.", False, "It is bloodborne."],
                     ["It cannot be prevented by vaccination.", False, "Vaccination is effective and recommended."],
                     ["It is only transmitted through dialyzer reuse.", False, "Shared items and surfaces are common routes."]], "sources": ["bond1981", "thompson2009"]},
        {"stem": "Which practice most directly breaks bloodborne transmission between stations?",
         "options": [["No item moves between stations unless single-use or disinfected.", True, "Shared supplies are a recurring cause of outbreaks."],
                     ["Wearing the same gloves between two quick tasks at different stations.", False, "This carries blood between stations."],
                     ["Using one multi-dose vial for the shift.", False, "Shared vials have caused outbreaks."],
                     ["Cleaning surfaces only when visibly dirty.", False, "Blood films are often invisible."]], "sources": ["thompson2009"], "critical": True},
        {"stem": "In the CDC collaborative of 17 facilities, what happened to access-related bloodstream infections?",
         "options": [["Modeled rates fell 54 percent at the start of the intervention, in a before-and-after design.", True, "Pooled rates fell from 0.73 to 0.42 per 100 patient-months; there was no control group."],
                     ["They rose because of more audits.", False, "They fell."],
                     ["They fell in a randomized trial.", False, "It was a quality improvement project."],
                     ["No change was seen.", False, "A significant reduction was seen."]], "sources": ["patel2013"]},
        {"stem": "What is the correct denominator for a dialysis bloodstream infection rate?",
         "options": [["Patient-months, counted separately by access type.", True, "Rates per 100 patient-months, stratified by access, are standard."],
                     ["Number of staff.", False, "Not a measure of exposure."],
                     ["Number of positive cultures.", False, "That is the numerator."],
                     ["Number of machines.", False, "Not a patient-exposure denominator."]], "sources": ["patel2013"]},
        {"stem": "Saturday hand hygiene is 54 percent while weekdays average 88 percent. Most misses follow touching the machine. Best next step?",
         "options": [["Look for the system cause on Saturdays, such as empty dispensers, then fix and remeasure.", True, "A miss pattern usually points to a system problem."],
                     ["Send a memo telling Saturday staff to try harder.", False, "Exhortation rarely fixes a supply problem."],
                     ["Stop auditing Saturdays.", False, "That hides the problem."],
                     ["Report each staff member to the head nurse.", False, "Blame discourages honest practice."]], "sources": ["pittet2000"]},
        {"stem": "Two catheter patients develop rigors on the same shift after a shared tray moved between their stations. An aide wants to throw the tray away. What do you do?",
         "options": [["Take the tray out of use, bag and label it, and keep it for review.", True, "It may be the common source; discarding destroys evidence."],
                     ["Let the aide discard it to prevent spread.", False, "Containment does not require destruction."],
                     ["Wash the tray and return it to use.", False, "This destroys evidence and risks further spread."],
                     ["Ignore the tray; focus only on the patients.", False, "Patient care comes first, but containment and preservation follow at once."]], "sources": [], "critical": True},
        {"stem": "In a suspected cluster, what comes first?",
         "options": [["Care of the sick patients.", True, "Treat first, then contain, preserve and investigate."],
                     ["Finding the nurse responsible.", False, "Blame is not the first step, nor a step."],
                     ["Completing the line list.", False, "Important, but after immediate care."],
                     ["Notifying the media.", False, "Not appropriate."]], "sources": []},
        {"stem": "What does the WHO competency framework imply about a dialysis infection prevention nurse?",
         "options": [["A unit champion supports, but does not replace, a professional infection control team.", True, "IPC is a profession with progressive competencies."],
                     ["The dialysis nurse becomes a full IPC professional after this module.", False, "This module is a subset."],
                     ["The nurse may prescribe antibiotics for infections.", False, "Prescribing is outside nursing scope."],
                     ["Public-health reporting is decided by the nurse alone.", False, "It is decided under current rules by designated people."]], "sources": ["who_ipc"]},
        {"stem": "What is the purpose of the DART checklists?",
         "options": [["To make task observations reproducible, so different observers score the same steps.", True, "Standard checklists reduce observer variation."],
                     ["To certify staff for promotion.", False, "They support feedback, not credentials."],
                     ["To count infections.", False, "That is surveillance."],
                     ["To replace training.", False, "They complement training."]], "sources": ["cdc_dart"]},
        {"stem": "The definition of a bloodstream infection event must change mid-year. What should the IPC nurse do?",
         "options": [["Mark the date of the change on the chart so the series break is visible.", True, "Otherwise a change in counting looks like a change in reality."],
                     ["Recalculate past months only if the new rate is lower.", False, "Selective recalculation misleads."],
                     ["Keep the change quiet.", False, "Hidden changes destroy trust in the data."],
                     ["Stop surveillance.", False, "Surveillance must continue."]], "sources": []},
        {"stem": "What does KDIGO advise about patients with hepatitis C in hemodialysis?",
         "options": [["Strict standard precautions for every patient, following unit policy, rather than relying on isolation.", True, "Transmission is prevented by consistent precautions at every station."],
                     ["No precautions are needed.", False, "Precautions are essential."],
                     ["They must never be dialyzed.", False, "Not acceptable or advised."],
                     ["Dialyzers must be reused only for them.", False, "Not the guidance."]], "sources": ["hcv2022"]},
        {"stem": "Which is a stewardship task within nursing scope?",
         "options": [["Ensure blood cultures are drawn as ordered before the first antibiotic dose and results reach the prescriber.", True, "Nurses support stewardship by sequence, follow-up and communication."],
                     ["Stop an antibiotic when the patient feels better.", False, "Stopping is the prescriber's decision."],
                     ["Choose a narrower antibiotic from the culture result.", False, "Prescribing decision."],
                     ["Extend antibiotics to be safe.", False, "Prescribing decision and poor stewardship."]], "sources": ["cdc_steward"]},
        {"stem": "In the Geneva hand hygiene program, what changed along with compliance?",
         "options": [["Hospital-acquired infections fell from 16.9 to 9.9 percent, in an observational before-and-after study.", True, "Bedside rub and feedback raised compliance from 48 to 66 percent."],
                     ["Infections rose because staff were distracted.", False, "They fell."],
                     ["A randomized trial proved the program caused the fall.", False, "It was observational."],
                     ["Compliance reached 100 percent.", False, "It reached 66 percent."]], "sources": ["pittet2000"]},
        {"stem": "A unit converts many catheter patients to fistulas and the overall infection rate falls. What does this tell you about catheter care?",
         "options": [["Nothing by itself; check the catheter-specific rate.", True, "Case mix changes can move the overall rate without any change in care quality."],
                     ["Catheter care has improved.", False, "Not necessarily."],
                     ["Catheter care has worsened.", False, "Not necessarily."],
                     ["Surveillance is no longer needed.", False, "It is still needed."]], "sources": ["patel2013"]},
        {"stem": "Which feedback approach best supports improvement after an observed lapse?",
         "options": [["Immediate private feedback to the person, unit-level data to the team, and a search for the system cause.", True, "This keeps trust while fixing the system."],
                     ["Naming the nurse at the staff meeting.", False, "Public blame discourages honest practice."],
                     ["Waiting for the annual review.", False, "Feedback works best when timely."],
                     ["No feedback, to avoid conflict.", False, "Without feedback, nothing changes."]], "sources": ["patel2013"]},
    ],
    "exam": [
        {"stem": "A supply tray has moved between three stations all morning, and two catheter patients develop rigors. What is the IPC nurse's priority after immediate patient care?",
         "options": [["Take the tray out of use and preserve it, start a line list and notify infection control.", True, "Contain, preserve and notify."],
                     ["Discard the tray and disinfect the stations.", False, "Destroys evidence."],
                     ["Ask the patients to sign a waiver.", False, "Not relevant."],
                     ["Wait for culture results before acting.", False, "Containment should not wait."]], "sources": [], "critical": True},
        {"stem": "How should a unit report bloodstream infections?",
         "options": [["Per 100 patient-months, stratified by access type, using one written definition.", True, "Consistent definitions and stratified denominators."],
                     ["As a total count per year.", False, "No denominator."],
                     ["As a percentage of staff.", False, "Wrong denominator."],
                     ["Only when an outbreak occurs.", False, "Surveillance is continuous."]], "sources": ["patel2013"]},
    ],
}
