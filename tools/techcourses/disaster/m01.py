# -*- coding: utf-8 -*-
"""Disaster Preparedness and Response, Module 01: Why Disasters Hurt Dialysis Patients Twice.
Written for this series from published sources."""

MODULE = {
    "image_alt": "A freestanding dialysis clinic on a flooded street, its shutter half down, with an older man and his daughter on a dry step across the street.",
    "objectives": [
        "Explain why a disaster harms a dialysis patient twice: first through the event, then through missed treatment in the days after it.",
        "Trace the six links of the causal chain (warning, event, access, physiology, late presentation, restart) and name the place where the unit can act at each link.",
        "Describe what the disaster studies show about missed sessions, early dialysis, planning and patient self-disconnection, and state the limits of that evidence in the right words.",
        "Name the hazards a Philippine dialysis unit plans for and the agencies that warn about them.",
    ],
    "big": """
{{plain:Picture a dialysis unit as a bridge that patients must cross three times a week. A disaster can shake the bridge while people are on it, and it can also close the bridge for days. The shaking is frightening, but more people are hurt by the days the bridge stays closed, because the river of water, salt and potassium keeps rising on the far side.}}
<p>The picture has a limit. A closed bridge simply waits. A body without dialysis does not wait: every day without treatment adds a day of water, salt, potassium and acid to a patient who cannot remove them. And in a disaster the bridge does not close for everyone at once. Some patients are stranded, some reach another unit, and some arrive days later at a hospital that is itself running on a generator.</p>
<p>This module gives the whole course its logic. Each later module sits on one link of the chain below and teaches what the unit can do there.</p>
{{cards:Key terms for this module|Disaster::An event that harms many patients at once or stops the unit from treating them, such as a typhoon, flood, earthquake, fire, outage or outbreak.|Missed session::A scheduled hemodialysis treatment that does not happen.|Early dialysis::A session moved ahead of schedule because a disruption is expected.|Receiving unit::Another dialysis unit that agrees to treat your patients when yours cannot.|Restart::Reopening the unit after a disruption, only when it is safe to treat again.|Observational study::A study that watches what happened without assigning treatments; it shows associations, not proof.}}
""",
    "case": {"title": "Four days in Marikina", "html": """
<p>A freestanding 14-station unit in Marikina closes for four days after floodwater reaches its ground floor. It reopens on a Friday. By the end of the first shift, the head nurse has a list: of 52 patients, 31 dialyzed somewhere during the closure, 14 missed one or two sessions, and 7 missed three or more. Two of those seven are in the hospital with fluid overload and a potassium above 7 mmol/L.</p>
<p>The head nurse asks the safety nurse a simple question: &ldquo;Why these seven?&rdquo; The safety nurse checks the call log. Four had a wrong or old phone number. Two live in barangays where the roads flooded first. One said, &ldquo;Nobody told me the other unit would take me.&rdquo;</p>
""", "questions": ["At which link of the chain was each of the seven patients lost?",
                  "Which of those losses could the unit have changed before the flood?",
                  "What would you measure next season to know whether the plan worked?"]},
    "sections": [
        ("chain", "The causal chain", "Six links, and a place to act at each one", """
<p>Disasters harm dialysis patients through a chain that repeats from storm to storm and country to country.[[dp_sever2023]] Seeing it as a chain matters, because each link has a different owner and a different fix.</p>
{{fig:dp01_causal_chain}}
<div class="table-wrap"><table>
<thead><tr><th>Link</th><th>What happens</th><th>Where this course acts</th></tr></thead>
<tbody>
<tr><td>1. Warning</td><td>The storm is coming; staff and patients are not told what to do</td><td>Activation triggers, early dialysis, call-down (Modules 3 and 5)</td></tr>
<tr><td>2. Event</td><td>Patients are on machines when the ground shakes, the power fails or a fire starts</td><td>Protect in place, take-off and evacuation, quick cards (Modules 6 to 8)</td></tr>
<tr><td>3. Access</td><td>Roads flood, the unit closes, the patient cannot reach any unit</td><td>Receiving-unit agreements, patient tracking (Modules 3 and 10)</td></tr>
<tr><td>4. Physiology</td><td>Missed sessions; salty, potassium-rich relief food; no medicines</td><td>Emergency diet, emergency card, priority roster (Modules 4 and 10)</td></tr>
<tr><td>5. Late presentation</td><td>The patient arrives with high potassium and fluid overload, often at a hospital on a generator</td><td>Handoff to the Resuscitation Lab and the physician modules</td></tr>
<tr><td>6. Restart</td><td>The unit reopens before water, power or machines are safe</td><td>Five signed restart gates (Module 11)</td></tr>
</tbody></table></div>
<p>Link 4 is the reason a missed session is dangerous. A failed kidney no longer removes the water, salt, potassium and acid that enter the body each day. Dialysis opens the drain for a few hours, then closes it until the next session. Each missed session adds two or three more days of intake to a body that cannot clear it, and relief food (instant noodles, canned meat, dried fish) is often high in salt and potassium. Potassium can reach a level that disturbs the heart rhythm before the patient feels short of breath, so a patient who looks well can still be in danger.</p>
{{key:The event is the first harm; missed treatment is the second and usually the larger. Every link of the chain has a place where the unit can act before the disaster.}}
"""),
        ("evidence", "What the studies show", "What the evidence shows, and what it does not", """
<p>Most of the evidence comes from United States hurricanes and Japanese earthquakes, because those events were studied. None of it comes from randomized trials. That is not a reason to ignore it; it is a reason to use the right words.</p>
{{fig:dp01_what_the_studies_show}}
<ul>
<li><strong>Missed sessions follow storms.</strong> In 60,135 patients in the northeastern United States, exposure to a hurricane or tropical storm was associated with a 55% higher risk of missed appointments over the following week (rate ratio 1.55, 95% confidence interval 1.22 to 1.98).[[dp_remigio2023]]</li>
<li><strong>Missing three or more sessions is associated with hospitalization.</strong> Among 386 New Orleans patients after Hurricane Katrina, 44% missed at least one session and about 17% missed three or more. Patients who did not know their unit&rsquo;s emergency plan were among the more likely to miss three or more, and missing three or more was associated with hospitalization (adjusted odds ratio 2.16, 95% confidence interval 1.05 to 4.43).[[dp_anderson2009]]</li>
<li><strong>Early dialysis before landfall is associated with better outcomes.</strong> Of 13,836 patients in the areas hit by Hurricane Sandy, 60% were dialyzed ahead of schedule. Early dialysis was associated with lower odds of an emergency department visit (odds ratio 0.80), hospitalization (0.79) and death within 30 days (0.72, 95% confidence interval 0.52 to 0.997). The study could not tell who was offered early dialysis and declined, so healthier patients may have been the ones who came.[[dp_lurie2015]]</li>
<li><strong>A regional response can prevent excess deaths.</strong> In patients from 94 clinics hit by Katrina, the storm was not significantly associated with mortality in adjusted models.[[dp_kutner2009]] After Hurricane Maria, many patients were dialyzed outside Puerto Rico, and mortality did not change significantly; the authors suggest preparedness as one explanation.[[dp_rivera2022]] Both findings argue that planning works. Neither shows that disasters are harmless.</li>
<li><strong>Patients cannot be relied on to self-disconnect.</strong> In 626 hemodialysis patients in 10 centers across six countries, 20.0% had been trained in emergency self-disconnection and 22.4% said they knew how; on a checklist, 40.3% identified the first stage correctly and 38.3% the second.[[dp_ozen2026]] This course&rsquo;s position follows: patients are not taught to self-disconnect. They stay calm, stay connected, protect the access arm and wait for staff (Module 4).</li>
</ul>
<p>Reviews of disasters and kidney care describe the same failures again and again: no written plan, patients with no emergency instructions or diet advice, lost records, staff who cannot reach work, and no agreements with backup units.[[dp_sever2023]][[dp_sandal2025]][[dp_bonilla2019]] A 2026 scoping review of 30 studies from 10 countries found that, in 10 of 11 studies that measured it, 23% to 59% of patients had their dialysis disrupted, and it named lack of preparedness among the risk factors for worse outcomes.[[dp_sandal2026]]</p>
{{key:Say &ldquo;is associated with&rdquo; for these findings, never &ldquo;prevents death.&rdquo; The direction is consistent: units that plan, warn and move sessions early keep more patients dialyzed.}}
"""),
        ("hazards", "Philippine hazards", "The hazards a Philippine unit plans for", """
<p>The Philippines faces nearly every hazard on this list, often in the same year: typhoons and the floods that follow them, earthquakes, volcanic eruptions and ashfall, extreme heat, fires, long power interruptions, water supply failures, and infectious outbreaks. Each hazard reaches a dialysis unit through the same few dependencies: power, water, staff, supplies, transport, records and communications (Module 2).</p>
{{fig:dp01_philippine_hazards}}
<div class="table-wrap"><table>
<thead><tr><th>Hazard</th><th>Who warns</th><th>Warning time</th><th>Module</th></tr></thead>
<tbody>
<tr><td>Typhoon and flood</td><td>PAGASA (wind signals and rainfall warnings); the LDRRMO</td><td>Hours to days</td><td>5</td></tr>
<tr><td>Earthquake</td><td>PHIVOLCS (reports after the event; tsunami warnings)</td><td>None</td><td>6</td></tr>
<tr><td>Fire</td><td>The unit&rsquo;s own alarm; the Bureau of Fire Protection responds</td><td>None</td><td>7</td></tr>
<tr><td>Power and water failure</td><td>Utility notices for planned interruptions; none for faults</td><td>None to days</td><td>8</td></tr>
<tr><td>Heat, ashfall, outbreaks</td><td>PAGASA heat index; PHIVOLCS volcano alert levels; the Department of Health</td><td>Days to weeks</td><td>9</td></tr>
</tbody></table></div>
<p>Warning time changes the job. A typhoon gives a day or two to move sessions, warn patients and stock supplies; an earthquake gives seconds. That is why the plan has two halves: things done before any warning (the dependency map, the call list, the emergency cards, the drills) and things done when a warning or an event arrives.</p>
<p>The national framework is Republic Act No. 10121, the Philippine Disaster Risk Reduction and Management Act, which set up the national council and the local disaster offices.[[dp_ra10121]] The Department of Health applies it to health services through its policy on disaster risk reduction and management in health (DRRM-H).[[dp_doh2019]] A hospital-based unit works inside its hospital&rsquo;s plan; a freestanding unit coordinates with its city or municipal LDRRMO.</p>
{{key:Plan for every hazard through the same dependencies. Use the warning time a typhoon gives you; assume you will get none for an earthquake or a fire.}}
"""),
    ],
    "debrief": ["""
<p><strong>Where each patient was lost.</strong> The four with wrong phone numbers were lost at link 1 (warning): the call-down could not reach them. The two in flooded barangays were lost at link 3 (access). The patient who did not know another unit would take him was lost at links 1 and 3 together: no one told him the plan.</p>
<p><strong>What the unit could have changed.</strong> A call-list check before typhoon season would have found the wrong numbers (Module 3 and the call-down drill). Patients in flood-prone barangays could have been flagged for early dialysis with the nephrologist&rsquo;s approval before the water rose (Module 5). Every patient could have carried an emergency card naming the backup unit (Module 4).</p>
<p><strong>What to measure next season.</strong> The share of patients reached within 24 hours of activation, the number who missed three or more sessions, and the reasons. The call-down timer on the practice page gives the first number; the reconciliation in Module 11 gives the others.</p>
"""],
    "skills": {"title": "Reading your unit's last disruption",
               "intro": "With the safety nurse or head nurse, review the records of your unit&rsquo;s most recent disruption (a typhoon closure, a long outage, or a drill if there has been none).",
               "items": [
                   ("Lists every patient who missed at least one session, and the number of sessions missed.", True),
                   ("Places each loss on a link of the causal chain (warning, event, access, physiology, late presentation, restart).", False),
                   ("Names at least one action the unit could take before the next season for each link where patients were lost.", False),
                   ("Uses &ldquo;is associated with&rdquo; correctly when explaining the evidence to a colleague, without claiming a step prevents death.", False),
                   ("Names the local agency that warns for each hazard on the unit&rsquo;s list.", False),
               ],
               "placement": "Bring the list of lost patients and the links to the next staff meeting, and agree with the head nurse which two fixes come first."},
    "terms": [("Disaster", "An event that harms many patients at once or stops the unit from treating them."),
              ("Missed session", "A scheduled treatment that does not happen."),
              ("Early dialysis", "A session moved ahead of schedule before an expected disruption."),
              ("Receiving unit", "Another unit that agrees to treat your patients when yours cannot."),
              ("Causal chain", "The six links from warning to restart through which disasters harm dialysis patients."),
              ("Observational study", "A study that watches what happened without assigning treatments.")],
    "readings": [("typhoon-disaster-preparedness-dialysis.html", "The patient-facing guide to typhoon and disaster preparation."),
                 ("climate-extremes-kidney-care.html", "How climate extremes affect people with kidney disease.")],
    "calcs": [],
}


import importlib.util as _u
from pathlib import Path as _P
def _ld(n):
    s = _u.spec_from_file_location("dp_" + n, _P(__file__).resolve().parent / (n + ".py")); m = _u.module_from_spec(s); s.loader.exec_module(m); return m
MODULE["quiz"] = _ld("quizutil").balance(_ld("quizbank").QUIZ["01"])
