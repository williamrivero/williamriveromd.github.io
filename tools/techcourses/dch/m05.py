# -*- coding: utf-8 -*-
"""Dialysis Clinical Head, Module 05: Infection, Water, and Machines: The Invisible Barriers. Written for this series from published sources."""

MODULE = {
    "image_alt": "A physician and a water technician examining a sample port and test log in a dialysis water room, carbon tanks behind them.",
    "objectives": [
        "Explain why patients on hemodialysis are unusually vulnerable to bloodstream infection and to contaminants in water.",
        "Name the core interventions for preventing bloodstream infection, and audit one with an honest denominator.",
        "Read a water treatment diagram and log: what each stage removes, where samples come from, and which limits apply.",
        "Hold affected operations when a critical check fails or is unknown, and bound the exposure by station and shift.",
        "Separate technical verification from clinical authorization, and require both before restart.",
        "Plan placement and timely dialysis for a patient with possible tuberculosis or a reactive hepatitis B result.",
    ],
    "big": """
{{plain:Think of the water room as part of every patient&rsquo;s bloodstream. Whatever gets past the filters gets to the blood.}}
<p>The picture is closer to the truth than it sounds, with one limit. Most bacteria cannot cross an intact dialyzer membrane, but bacterial fragments such as endotoxin can, and small dissolved chemicals cross freely. That is why dialysis water is held to standards stricter than drinking water, and why a chlorine test matters more than a clean-looking tank.</p>
{{cards:Key terms for this module|Bloodstream infection (BSI)::Bacteria or fungi growing in the blood. In dialysis, most start at the vascular access.|Core interventions::The Centers for Disease Control and Prevention (CDC) set of practices proven together to reduce dialysis bloodstream infections.|Chloramine::A disinfectant added to city water. It passes through reverse osmosis and destroys red cells if not removed by carbon.|Endotoxin::Fragments of bacterial cell walls that can cross a dialyzer membrane and cause fever and inflammation.|CFU/mL::Colony-forming units per milliliter, the count of live bacteria in a sample.|EU/mL::Endotoxin units per milliliter.|Action level::A result below the maximum that triggers investigation before the maximum is reached.|Technical release::The signed statement by the technical lead that a system is within limits.}}
""",
    "case": {"title": "Two patients have rigors", "html": """
<p>At 10:15 on a Wednesday at a sixteen-station hospital-based unit in Pampanga, two patients on the second shift, Mr. Domingo Reyes at station 4 and Mrs. Luz Mercado at station 11, develop shaking chills an hour into treatment. Both have fistulas. Both were well before they connected.</p>
<p>The water technician, Mr. Allan Pineda, reports that this morning&rsquo;s total chlorine test was not logged; the night technician says he did it but forgot to write it. A product-water culture from last week came back this morning at 70 CFU/mL from a port labeled only &ldquo;RO room&rdquo; (reverse osmosis room). The vendor&rsquo;s representative tells you by phone that &ldquo;yesterday everything was normal.&rdquo;</p>
""", "questions": ["Who do you call first, and what do you stop?",
                  "Which stations and shifts are potentially affected, and how do you find out?",
                  "What evidence do you need before anyone restarts, and who signs it?"]},
    "sections": [
        ("why", "Why it matters", "Why dialysis is an infection-prone setting", """
<p>Patients on hemodialysis have their bloodstream accessed three times a week, often through a catheter, in a room shared with other patients, while their immune response is blunted by uremia. In United States surveillance from 2017 to 2020, the <em>Staphylococcus aureus</em> bloodstream infection rate among patients on hemodialysis was about 100 times that of other adults (4,248 versus 42 per 100,000 person-years). Central venous catheters carried about six times the risk of fistulas.[[dch_rha2023]]</p>
<p>Philippine data point the same way. In a retrospective cohort at the Philippine General Hospital, where temporary catheters were still being used for maintenance dialysis, catheter-related bloodstream infection occurred at 6.72 episodes per 1,000 catheter-days. Gram-negative organisms, including <em>Burkholderia cepacia</em> complex, were the most common, and nearly half of isolates were multidrug-resistant.[[dch_pasilan2024]] Gram-negative organisms in dialysis infections should make you look at water and environmental sources, not only skin.</p>
{{key:The catheter is the single biggest modifiable infection risk in your unit. Every catheter-day you remove is a risk you remove.}}
"""),
        ("core", "Core interventions", "The core interventions, and an honest audit", """
<p>The CDC core interventions combine surveillance with feedback, hand hygiene observation, catheter and vascular access care observation, staff competency, patient education, catheter reduction, chlorhexidine skin antisepsis, catheter hub disinfection, and antimicrobial ointment at catheter exit sites.[[dch_cdc_core]] In a United States collaborative of 17 facilities that adopted them, bloodstream infection rates fell 32% and access-related bloodstream infection rates fell 54% at the start of the intervention period, and the decline was sustained.[[dch_patel2013]] There was no control group, so some of the effect may reflect secular trends, but the direction is consistent with the mechanism.</p>
<p>An audit is useful only with a denominator. &ldquo;Hand hygiene is good&rdquo; is a feeling. &ldquo;We observed 120 opportunities this month and 96 were correct, 80%, down from 88%&rdquo; is a measurement you can act on.</p>
{{flow:An actionable audit|Observe::A set number of opportunities, on different shifts and staff.|Count::Correct over observed, with the definition written down.|Feed back::To the person, on the day, privately.|Re-observe::After correction, to see whether it held.}}
<p>Review hepatitis B screening, vaccination, and isolation arrangements against your facility&rsquo;s pathway. Hemodialysis-linked hepatitis B transmission fell sharply where vaccination, serologic screening, and dedicated machines and staff for infected patients were used together.[[dch_winston2020]]</p>
"""),
        ("water", "Water", "What water can do to a patient", """
{{fig:dch05_volume}}
<p>A person drinks about two liters a day, filtered by the gut and liver. A patient on hemodialysis meets roughly 120 liters of dialysis fluid across a membrane a few micrometers thick, every session. Contaminants that are harmless to drink can be harmful at that volume and route.</p>
<div class="table-wrap"><table>
<thead><tr><th>Event</th><th>What happened</th><th>Lesson</th></tr></thead>
<tbody>
<tr><td>Caruaru, Brazil, 1996</td><td>Water from a reservoir with cyanobacteria reached a dialysis center without adequate treatment. 101 patients met the case definition for acute liver injury and 50 died; microcystin toxins were found in the water and in patients&rsquo; tissue[[dch_jochimsen1998]]</td><td>Source water and treatment failures can kill a unit&rsquo;s patients within days</td></tr>
<tr><td>S&atilde;o Paulo, Brazil, 2000</td><td>Chlorine and chloramine residuals above limits in dialysis water and reprocessed dialyzers were associated with an outbreak of hemolytic reactions[[dch_calderaro2001]]</td><td>Chlorine tests must be done, logged, and acted on every shift</td></tr>
</tbody></table></div>
{{fig:dch05_train}}
<p>Chloramine is not removed by reverse osmosis. It depends on activated carbon, and carbon can be exhausted without warning when the incoming level rises. Placing two carbon tanks in series, with a test port between them, lets a breakthrough be caught after the first tank, before the second fails.[[dch_ward1996]]</p>
<p>The International Organization for Standardization (ISO) water standard, ISO 23500-3 (2024), sets maximum limits for dialysis water of fewer than 100 CFU/mL of bacteria and less than 0.25 EU/mL of endotoxin, and calls for lower action levels so that problems are investigated before the maximum is reached.[[dch_iso2024]] Action levels are commonly set at half the maximums. In the Philippines, the Department of Health (DOH) water order governs sampling, analysis, and records; use the limits your unit adopted under it, and check whether they match the current ISO edition.[[dch_doh2013]] Calculator 8 compares a result with the limits you enter.</p>
{{call:Stop dialysis on the affected loop when a critical water check fails, is missing, or cannot be traced to a named port. Call the technical lead and the attending nephrologists. Restart only on a documented technical release followed by your clinical authorization.}}
"""),
        ("release", "Release", "Two signatures, two questions", """
{{fig:dch05_release}}
<p>Technical verification asks whether the system is within its limits: the result, the port, the sample identity, the laboratory, the date, and the corrective action. The technical lead signs it. Clinical authorization asks whether it is safe to treat patients again: whether affected patients have been assessed, exposure bounded, and staff told. The clinical head signs it. Neither signature can stand in for the other.</p>
<p>Apply the same discipline to machines. A machine returns after repair, recall, or a failed disinfection only with a documented technical release. If your unit reprocesses dialyzers, trace one through patient assignment, reprocessing, testing for integrity and fiber bundle volume, and release, against the rules and the manufacturer&rsquo;s instructions. A systematic review of reuse and mortality found mostly very low-quality evidence and no consistent difference from single use; the safety of reuse depends on how well it is done.[[dch_galvao2012]]</p>
{{formula:<strong>Bounding exposure, illustration only.</strong> One water loop serves stations 1 to 16. A chlorine breakthrough sometime between the 06:00 and 10:00 checks could have reached every patient treated on the loop in that window: two shifts &times; 16 stations = up to 32 patients. List them by station and shift.}}
{{fig:dch05_exposure}}
"""),
        ("placement", "Placement", "Admitting a patient with an infection concern", """
<p>Patients on dialysis have a much higher risk of tuberculosis than the general population. In Singapore, incidence among patients with chronic kidney disease stage 5 ranged from 279 to 630 per 100,000, against 33 to 41 per 100,000 in the general population.[[dch_metussin2026]] The World Health Organization recommends systematic testing and treatment of latent tuberculosis infection in patients receiving dialysis.[[dch_getahun2015]]</p>
<p>If a patient arrives with possible infectious pulmonary tuberculosis, arrange prompt clinical assessment and activate your respiratory infection pathway with infection prevention and the tuberculosis team. Time on treatment alone does not settle which precautions are needed. If a transfer record shows a reactive hepatitis B surface antigen, confirm the result and apply your hepatitis B pathway, including whether a dedicated room, machine, and staff are available, while arranging dialysis without unsafe delay. Make the exposure decision and the placement decision separately for each case.</p>
"""),
    ],
    "debrief": ["""
<p><strong>Who first, and what stops?</strong> Call the attending nephrologists and the physician on duty for the two patients, and the technical lead for the water. Stop new connections on the loop now. For patients already connected, the physicians decide, patient by patient, whether to end treatment early; do not return blood from a circuit suspected of a dialyzer reaction without a physician&rsquo;s decision. Draw blood cultures and, if hemolysis is possible, check for it.</p>
<p><strong>Who is affected?</strong> Everyone treated on that loop since the last documented normal chlorine test, by station and shift. Ask the technical lead to test chlorine before and after each carbon tank now, and to repeat the culture from named ports. The &ldquo;RO room&rdquo; result cannot support any decision until it can be traced to a port; 70 CFU/mL is below a 100 CFU/mL maximum but above a common action level, so it requires investigation in any case.</p>
<p><strong>What evidence before restart?</strong> A documented within-limit chlorine result after the carbon, the corrective action recorded, the culture repeated from identified ports, and the technical lead&rsquo;s signed release. Then your clinical authorization, after the affected patients are assessed and followed up by named owners. The vendor&rsquo;s reassurance is not evidence. Report through your incident system, and check your reporting obligations.</p>
"""],
    "skills": {"title": "Infection prevention audit, water-log review, and two-signature release",
               "intro": "Run a short infection prevention audit, review a water log with an ambiguous port and a missing chlorine entry, and lead a release decision with a preceptor playing the technical lead.",
               "items": [
                   ("Audits a core intervention with a written definition and an observed denominator.", False),
                   ("Gives same-day feedback and schedules re-observation.", False),
                   ("Identifies a missing or untraceable water result as a failed check.", True),
                   ("Holds dialysis on the affected loop until a technical release is documented.", True),
                   ("Bounds exposure by station and shift and names a follow-up owner for each patient.", True),
                   ("Requires technical release before signing clinical authorization.", True),
                   ("Rejects verbal reassurance in place of a documented result.", True),
                   ("Plans timely dialysis and placement for a patient with a reactive hepatitis B or tuberculosis concern.", False),
                   ("Reports the event through the incident system and checks reporting obligations.", False),
               ],
               "placement": "Review your unit&rsquo;s water log every week for a month. Check that every result names a port, a time, and a signature, and that every result above an action level has a recorded action."},
    "quiz": [
        ("How did the <em>S. aureus</em> bloodstream infection rate in hemodialysis patients compare with other adults in United States surveillance?",
         ["About the same", "About 10 times higher", "About 100 times higher", "Lower"], 2,
         "4,248 versus 42 per 100,000 person-years."),
        ("What was the catheter-related bloodstream infection rate in the Philippine cohort?",
         ["0.5 per 1,000 catheter-days", "6.72 per 1,000 catheter-days", "20 per 1,000 catheter-days", "Not measured"], 1,
         "Gram-negatives predominated, and nearly half were multidrug-resistant."),
        ("Which vascular access carries the highest bloodstream infection risk?",
         ["Fistula", "Graft", "Central venous catheter", "All equal"], 2,
         "About six times the fistula risk in national surveillance."),
        ("What makes an infection prevention audit actionable?",
         ["A general impression", "A written definition, an observed denominator, feedback, and re-observation", "A signed policy", "A poster"], 1,
         "Measure, feed back, and check again."),
        ("What happened when facilities adopted the CDC core interventions in a collaborative?",
         ["Infection rates rose", "Bloodstream infection fell 32% and access-related infection 54%", "No change", "Only costs changed"], 1,
         "No control arm, so interpret with care."),
        ("Why must chlorine be tested every shift?",
         ["Reverse osmosis removes it anyway", "Chloramine passes reverse osmosis and can break through carbon within hours, causing hemolysis", "It is a PhilHealth rule", "To protect the pipes"], 1,
         "Carbon is the only reliable barrier."),
        ("Why place two carbon tanks in series?",
         ["To double the cost", "So a breakthrough is caught after the first tank before the second fails", "To soften water", "To remove bacteria"], 1,
         "Test between the tanks."),
        ("What maximums does ISO 23500-3 (2024) set for dialysis water?",
         ["Below 1,000 CFU/mL and 2 EU/mL", "Below 100 CFU/mL and 0.25 EU/mL", "Below 10 CFU/mL and 0.01 EU/mL", "None"], 1,
         "Action levels are set lower so problems are found earlier."),
        ("A culture result is labeled only &ldquo;RO room.&rdquo; What is it worth for a release decision?",
         ["Enough", "Nothing until it is traced to a named port; repeat it", "Half", "It overrides other results"], 1,
         "A result you cannot place cannot support a release."),
        ("The vendor says yesterday was normal; today&rsquo;s test is not logged. What do you do?",
         ["Accept the reassurance", "Treat it as a failed check: test now and hold the loop", "Wait until tomorrow", "Ask patients if they feel well"], 1,
         "Reassurance is not evidence."),
        ("Who signs technical verification, and who signs clinical authorization?",
         ["Both the clinical head", "The technical lead, then the clinical head", "The owner, then the vendor", "The head nurse, then the owner"], 1,
         "Two signatures, two questions."),
        ("What happened at Caruaru in 1996?",
         ["A machine recall", "Microcystins in inadequately treated water caused liver failure; 50 patients died", "A hepatitis B outbreak", "A fire"], 1,
         "Water treatment is life support."),
        ("What did a systematic review conclude about dialyzer reuse and mortality?",
         ["Reuse clearly raises mortality", "Mostly very low-quality evidence and no consistent difference", "Reuse lowers mortality", "No studies exist"], 1,
         "Safety depends on how reuse is done."),
        ("How much higher was tuberculosis incidence among CKD stage 5 patients in Singapore than in the general population?",
         ["About the same", "Roughly 7 to 15 times higher", "Lower", "100 times higher"], 1,
         "279 to 630 versus 33 to 41 per 100,000."),
        ("A transfer record shows a reactive hepatitis B surface antigen (HBsAg). What is the right sequence?",
         ["Refuse the patient", "Confirm the result, apply the hepatitis B pathway, and arrange timely dialysis", "Dialyze at any open station", "Wait two weeks"], 1,
         "Delaying dialysis is a risk too."),
    ],
    "terms": [("Bloodstream infection (BSI)", "Microbes growing in the blood."),
              ("Core interventions", "The CDC bundle for preventing dialysis bloodstream infections."),
              ("Chloramine", "A water disinfectant that causes hemolysis if not removed by carbon."),
              ("Endotoxin", "Bacterial fragments that can cross a dialyzer membrane."),
              ("Action level", "A result below the maximum that triggers investigation."),
              ("Technical release", "The technical lead&rsquo;s signed statement that a system is within limits."),
              ("Clinical authorization", "The clinical head&rsquo;s signed decision that patients may be treated again."),
              ("Exposure window", "The period and stations during which patients could have been affected.")],
    "readings": [("hemodialysis-access-lifeline.html", "Making vascular access last, and reducing catheter use.")],
    "calcs": ["calc-dialysis-clinical-head-toolkit.html"],
}


import importlib.util as _u
from pathlib import Path as _P
_s = _u.spec_from_file_location("dch_quizutil", _P(__file__).resolve().parent / "quizutil.py")
_q = _u.module_from_spec(_s); _s.loader.exec_module(_q)
MODULE["quiz"] = _q.balance(MODULE["quiz"])
