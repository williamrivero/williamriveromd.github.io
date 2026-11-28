# -*- coding: utf-8 -*-
"""Disaster Preparedness and Response, Module 05: Typhoons and Floods."""

MODULE = {
    "image_alt": "A dialysis unit at dusk under a heavy typhoon sky, staff moving supply boxes onto high shelves while a van waits outside.",
    "objectives": [
        "List what a unit does before typhoon season, when a signal is raised, during the storm and after it.",
        "Explain early dialysis before landfall: who decides, how patients are chosen, and what the evidence shows.",
        "Plan staff transport and minimum staffing for a storm, and decide when staff should not travel.",
        "Recognize the hazards of flood water for staff and patients (electrical equipment, wounds, leptospirosis) and the precautions for each.",
    ],
    "big": """
{{plain:A typhoon is the one disaster that knocks before it comes in. The knock is the wind signal. A unit that hears it and acts can move sessions earlier, stock up and send people home safely before the roads close.}}
<p>The knock has a limit. The signal warns about wind; the flood often comes from rain, can rise in hours, and can outlast the wind by days. A unit can be dry on the day of landfall and unreachable for a week after. So the plan has four phases, and the most important work happens in the first two.</p>
<p>The person who decides any change to a patient&rsquo;s schedule, session length or fluid goal is the attending nephrologist. The head nurse turns those decisions into a roster (<a href="dialysis-head-nurse-12-disaster-and-service-leadership.html">Head Nurse, Module 12</a>); the physician-on-duty handles the shift (<a href="physician-on-duty-30-when-the-power-or-water-fails.html">Physician-on-Duty, Module 30</a>).</p>
{{cards:Key terms for this module|Wind signal::PAGASA&rsquo;s Tropical Cyclone Wind Signal, Nos. 1 to 5, each with a wind threat and a lead time.|Landfall::When the center of the typhoon crosses the coast.|Early dialysis::A session moved ahead of schedule before an expected disruption.|Last safe session::The latest time the unit can finish treatments and still send patients and staff home safely.|Leptospirosis::A bacterial infection from water or soil contaminated by animal urine, often after wading in flood water.|Minimum staffing::The smallest team that can run a shift safely.}}
""",
    "case": {"title": "Signal No. 3 by Thursday", "html": """
<p>On Tuesday evening PAGASA forecasts that a typhoon will make landfall over Luzon on Thursday morning, with Signal No. 3 expected for Quezon City by Wednesday night. A 24-station unit in Quezon City dialyzes a Tuesday&ndash;Thursday&ndash;Saturday group of 40 patients. Thursday&rsquo;s sessions would fall during landfall.</p>
<p>The unit can add a Wednesday evening shift if staff can stay late. Eight staff live in Marikina and Rizal, where floods often close the roads. Three of Thursday&rsquo;s patients use tricycles; one is a 74-year-old woman with heart failure who gained 3.5 kg before her last session.</p>
""", "questions": ["Who decides whether Thursday&rsquo;s patients dialyze early, and which of them first?",
                  "How do you staff a Wednesday evening shift and get staff home safely?",
                  "What do you tell the patients who will dialyze early about the days after?"]},
    "sections": [
        ("phases", "Four phases", "Before the season, when the signal is raised, during, after", """
<p>A typhoon plan is a timeline. What the unit does in each phase depends on what it did in the phase before.</p>
{{fig:dp05_typhoon_timeline}}
<div class="table-wrap"><table>
<thead><tr><th>Phase</th><th>What the unit does</th></tr></thead>
<tbody>
<tr><td>Before the season</td><td>Review the plan and dependency map; call-down drill to fix phone numbers; emergency cards updated; supply buffer stocked above the flood line; receiving-unit agreements checked; tabletop exercise (Modules 2, 3, 4, 12)</td></tr>
<tr><td>When the signal is raised</td><td>Activate the plan at the trigger; call-down; the attending nephrologist decides on early dialysis; staff transport; reminders to patients about diet, medicines and the go-bag; generator fuel and water checked</td></tr>
<tr><td>During</td><td>Unit closed when travel is unsafe; nobody sent onto flooded roads; patients tracked by phone; the incident lead keeps a log</td></tr>
<tr><td>After</td><td>Find every patient within 24 hours (Module 10); reopen only through the five signed gates (Module 11); reconcile who was dialyzed where</td></tr>
</tbody></table></div>
<p>PAGASA&rsquo;s signals give the lead time: Signal No. 3 means storm-force winds within 18 hours, and No. 4 within 12.[[pagasa_tcws]] At No. 4 and No. 5, PAGASA&rsquo;s impact statements expect widespread loss of power and communications, the two things a unit needs to reach its patients.[[pagasa_tcws]] Use the earlier signals to do the work that needs roads and phones.</p>
"""),
        ("early", "Early dialysis", "Early dialysis before landfall", """
<p>If landfall will fall on a patient&rsquo;s session day, or the roads are likely to close for days, moving the session earlier shortens the longest gap the patient will face. Before Hurricane Sandy, 60% of 13,836 patients in the affected areas were dialyzed early; early dialysis was associated with lower odds of an emergency department visit, hospitalization and death within 30 days.[[dp_lurie2015]] The study was observational and could not see who was offered early dialysis and declined, so it supports the practice without proving it.</p>
{{fig:dp05_early_dialysis_decision}}
<p><strong>Who decides.</strong> The attending nephrologist decides which patients dialyze early, and whether any session length or fluid goal changes. The Dialysis Clinical Head and the head nurse turn the decision into a roster; the charge nurse calls the patients.</p>
<p><strong>Who goes first.</strong> The nephrologist usually puts first the patients with the most to lose from a long gap: recent high potassium, large weight gains or fluid overload, heart failure, missed sessions, and those whose transport fails first in a flood. The same medical priority logic is taught in Module 10.</p>
<p><strong>What to tell patients.</strong> That the next session may be later than usual, so the emergency diet starts after this session; where the backup unit is; and to keep the go-bag ready. The interdialytic weight gain calculator on the site shows how a longer gap raises the fluid to be removed next time.</p>
{{key:Early dialysis shortens the longest gap. The nephrologist decides who and when; the unit makes it happen before the roads close.}}
"""),
        ("staff", "Staff", "Staff who cannot come in, and staff who must get home", """
<p>Staff live where patients live; the same flood that strands patients strands nurses. The call-down starts with staff because the unit cannot promise what it cannot staff (Module 3).</p>
<ul>
<li><strong>Know who can come.</strong> Map where staff live against the roads that flood first.</li>
<li><strong>Set minimum staffing</strong> for an emergency shift with the head nurse, including at least one nurse with current Advanced Cardiovascular Life Support (ACLS), as the unit&rsquo;s licensing requires.[[doh2012]][[psn2024]]</li>
<li><strong>Arrange transport</strong> (the unit van, shared rides) and, if the shift ends late, somewhere safe to stay.</li>
<li><strong>Set the last safe session time</strong> so the last patient and the last staff member are home before travel becomes unsafe. Nobody is sent onto a flooded road to keep a schedule.</li>
</ul>
"""),
        ("flood", "Flood water", "Flood water, wet equipment and leptospirosis", """
<p>Flood water brings three hazards to a dialysis unit.</p>
{{fig:dp05_flood_risks}}
<ul>
<li><strong>Electricity.</strong> Do not touch machines, plugs or panels that are wet or standing in water. Switch off at the main breaker only if it is dry and safe to reach; otherwise leave it to the electrician or technician. Unplug equipment before water arrives.</li>
<li><strong>Wounds and the access.</strong> Avoid wading. If a patient or staff member must cross water, cover wounds and the access site with a waterproof dressing, and wash and dry the skin afterward.</li>
<li><strong>Leptospirosis.</strong> Flood water contaminated by animal urine can carry leptospirosis, which can damage the kidneys (acute kidney injury, AKI). Anyone who waded and develops fever, muscle pain or red eyes in the weeks after should report it and see a physician; preventive treatment after exposure is a physician&rsquo;s decision, following Department of Health guidance. The site&rsquo;s <a href="../guides/leptospirosis-nephropathy.html">leptospirosis guide</a> explains why it matters for the kidneys.</li>
</ul>
<p>After the water recedes, the unit is cleaned and disinfected before reopening, and nothing that stood in flood water is used until the technicians have checked it. The restart gates (Module 11) make that a signed decision.</p>
{{call:Any staff member or patient with fever after wading, any machine or panel that has been wet, or any flood water in the water treatment room: report to the incident lead and the technicians at once. Follow your unit protocol, and always ask the attending nephrologist for guidance.}}
"""),
    ],
    "debrief": ["""
<p><strong>Who decides.</strong> The attending nephrologist decides on early dialysis for the Thursday group and which patients go first. The 74-year-old woman with heart failure and a 3.5 kg gain is a likely first choice; so are patients with a recent high potassium or missed sessions, and the three who depend on tricycles. The head nurse turns the list into a Wednesday roster.</p>
<p><strong>Staffing.</strong> Call staff first. Build the Wednesday evening shift from staff who live closest or can stay overnight, with at least one ACLS-current nurse. Arrange the unit van for the Marikina and Rizal staff and set a last safe session time so everyone is home before Signal No. 3 takes effect. Nobody travels onto flooded roads.</p>
<p><strong>What patients are told.</strong> Their next session may be later than usual, so the emergency diet starts tonight; their backup unit and contacts are on their emergency card; keep the go-bag and medicines ready; and do not wade through flood water.</p>
"""],
    "skills": {"title": "Running the typhoon activation",
               "intro": "In a tabletop or on a real signal, run the unit&rsquo;s typhoon activation with the head nurse.",
               "items": [
                   ("Activates the plan at the unit&rsquo;s trigger and records the time.", True),
                   ("Calls staff first, then patients due within 24 hours.", False),
                   ("Obtains the attending nephrologist&rsquo;s decision on early dialysis before changing any schedule.", True),
                   ("Plans staff transport, minimum staffing with an ACLS-current nurse, and a last safe session time.", False),
                   ("Reminds patients about the emergency diet, medicines, go-bag and backup unit.", False),
                   ("Gives the flood water precautions, including reporting fever after wading.", False),
               ],
               "placement": "Use the tabletop simulator on the practice page with the typhoon scenario and record your decisions."},
    "terms": [("Wind signal", "PAGASA&rsquo;s Tropical Cyclone Wind Signal, Nos. 1 to 5."),
              ("Landfall", "When the center of the typhoon crosses the coast."),
              ("Early dialysis", "A session moved ahead of schedule before an expected disruption."),
              ("Last safe session", "The latest time to finish treatments and still send people home safely."),
              ("Leptospirosis", "An infection from water or soil contaminated by animal urine."),
              ("Minimum staffing", "The smallest team that can run a shift safely.")],
    "readings": [("typhoon-disaster-preparedness-dialysis.html", "The patient guide to typhoon preparation."),
                 ("leptospirosis-nephropathy.html", "Leptospirosis and the kidney.")],
    "calcs": ["calc-dialysis-continuity-planner.html", "calc-leptospirosis-aki-risk.html"],
}


import importlib.util as _u
from pathlib import Path as _P
def _ld(n):
    s = _u.spec_from_file_location("dp_" + n, _P(__file__).resolve().parent / (n + ".py")); m = _u.module_from_spec(s); s.loader.exec_module(m); return m
MODULE["quiz"] = _ld("quizutil").balance(_ld("quizbank").QUIZ["05"])
