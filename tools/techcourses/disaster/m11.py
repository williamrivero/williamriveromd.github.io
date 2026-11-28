# -*- coding: utf-8 -*-
"""Disaster Preparedness and Response, Module 11: Reopening Safely and Recovering. DRAFT.
The five restart gates are repeated verbatim from Head Nurse Module 12 (the single source); any change goes into both."""

MODULE = {
    "image_alt": "A head nurse and a water treatment technician signing a checklist at the water room door of a clean, dry dialysis unit after a flood.",
    "objectives": [
        "Reopen only through the five signed restart gates: building, staff, water and machines, supplies and cart, records.",
        "Reconcile who was dialyzed where, who missed sessions, who needs an extra session and who needs laboratory tests.",
        "Recognize fatigue and distress in staff after a disaster, and what a unit can do.",
        "Recognize distress in patients after a disaster, and what the evidence shows about it.",
    ],
    "big": """
{{plain:Reopening a dialysis unit after a disaster is like a plane&rsquo;s pre-flight check after a storm. The pilot does not take off because the sky looks clear; every item on the list is checked and signed, and one unsigned item keeps the plane on the ground.}}
<p>The picture has a limit. A plane&rsquo;s checklist is the same every day; a unit&rsquo;s restart depends on what the disaster did. A flood may have reached the water room; an earthquake may have cracked a column; a long outage may have let bacteria grow in the water loop. The five gates are the same every time, but what each signer checks depends on the event. And unlike a plane, a unit carries the disaster forward in its people: patients who missed sessions, and staff who worked while their own homes flooded.</p>
<p>The gates come from <a href="dialysis-head-nurse-12-disaster-and-service-leadership.html">Head Nurse, Module 12</a>, which owns them; this module repeats them word for word. The Dialysis Clinical Head treats the restart as a signed decision (<a href="dialysis-clinical-head-07-disaster-and-continuity.html">Dialysis Clinical Head, Module 7</a>).</p>
{{cards:Key terms for this module|Restart gate::One of five signed checks before the unit treats patients again.|Water release::The water technician&rsquo;s and medical head&rsquo;s signed approval that the water is fit for dialysis.|Reconciliation::The record of who was dialyzed where and when, who missed sessions, and what each patient needs next.|Downtime record::A paper record kept while the electronic system was unavailable.|Posttraumatic stress::A lasting stress reaction after a frightening event.|Burnout::Exhaustion and detachment from work after long strain.}}
""",
    "case": {"title": "The gate that wasn't signed", "html": """
<p>A 14-station unit in Marikina was closed for four days after a flood reached its ground floor, including the water treatment room. On day five the building engineer has signed the building gate, the head nurse has a full roster with an ACLS-current nurse, the supply room is restocked, and the records officer has entered the paper downtime records.</p>
<p>The water treatment technician says on the phone, &ldquo;The system is running and the readings look fine, you can start.&rdquo; The water tests have been sent but the results are not back. Twenty patients are waiting, several of them overdue. The owner asks the head nurse to open &ldquo;since everything else is signed.&rdquo;</p>
""", "questions": ["Can the unit open? Which gate is not met?",
                  "What can the unit do for the twenty waiting patients meanwhile?",
                  "What goes on the reconciliation board when the unit opens?"]},
    "sections": [
        ("gates", "Five signed gates", "Restart only through five signed gates", """
<p>The unit restarts only when the five gates are signed.</p>
{{fig:dp11_five_restart_gates}}
<div class="table-wrap"><table>
<thead><tr><th>Gate</th><th>What it means</th><th>Who signs (typical)</th></tr></thead>
<tbody>
<tr><td>Building</td><td>Safe to occupy, power stable.</td><td>Building engineer or facilities officer; the hospital for a hospital-based unit</td></tr>
<tr><td>Staff</td><td>Qualified nurses and Advanced Cardiovascular Life Support (ACLS) cover.</td><td>Head nurse</td></tr>
<tr><td>Water and machines</td><td>Tested and released after the outage.</td><td>Water treatment technician and biomedical technician, with the medical head</td></tr>
<tr><td>Supplies and cart</td><td>Stock and emergency cart checked.</td><td>Head nurse or charge nurse</td></tr>
<tr><td>Records</td><td>Recovered, and paper downtime records entered.</td><td>Records officer</td></tr>
</tbody></table></div>
<p>A verbal &ldquo;it looks fine&rdquo; is not a signature. The water gate in particular depends on test results: when a test fails, the Department of Health&rsquo;s dialysis water order requires the facility to stop operations until a repeat test complies, disinfect the loop and notify its patients.[[dch_doh2013]] The water technician and the medical head decide when water is fit; the owner and the schedule do not.</p>
{{key:Restart only when all five gates are signed: building, staff, water and machines released, supplies and cart, records. One unsigned gate keeps the unit closed.}}
"""),
        ("reconcile", "Reconciliation", "Who was dialyzed where", """
<p>Reopening day starts with a list. For every patient on the unit&rsquo;s census, the reconciliation board records where they were dialyzed and when, how many sessions they missed, whether they need an extra session, and which laboratory tests they need.</p>
{{fig:dp11_reconciliation_board}}
<ul>
<li><strong>Dialyzed where:</strong> from the tracking board (Module 10) and the receiving units&rsquo; reports.</li>
<li><strong>Sessions missed:</strong> counted honestly; this is the measure of the plan.</li>
<li><strong>Needs an extra session:</strong> the attending nephrologist decides, usually for patients who missed sessions or had shortened ones.</li>
<li><strong>Needs laboratory tests:</strong> potassium and others as the nephrologist orders, and any hepatitis testing needed after treatment at another unit, per the unit&rsquo;s infection control protocol.</li>
</ul>
<p>Patients still not reached stay on the board until found. Any shortened sessions end and full prescriptions resume as capacity allows, with the date recorded (Module 10).</p>
"""),
        ("staff", "Caring for staff", "Staff fatigue and distress", """
<p>Staff often work through a disaster while their own homes are flooded or damaged. In the weeks after, fatigue and distress are common and easy to miss. There is little dialysis-specific research on staff after disasters, so this section gives practical steps rather than evidence-graded advice.</p>
{{fig:dp11_caring_for_staff}}
<ul>
<li><strong>Rest and recover:</strong> rotate shifts so nobody works for days without rest; send home staff who are exhausted.</li>
<li><strong>Look out for each other:</strong> ask how colleagues and their families are.</li>
<li><strong>Talk:</strong> a short, voluntary conversation after the event; refer staff who are struggling to the support the unit or hospital offers.</li>
<li><strong>Do not ignore signs of burnout:</strong> withdrawal, irritability, mistakes, and lasting exhaustion.</li>
</ul>
<p>The after-action report (Module 12) records what staff needed and did not have, so the next plan includes it. After Hurricane Maria, a Puerto Rico nephrology service listed attention to the staff&rsquo;s own needs among its lessons, so that staff could keep responding.[[dp_bonilla2019]]</p>
"""),
        ("patients", "Patients after", "Patients&rsquo; distress after disasters", """
<p>Patients carry the disaster too. About a year after Hurricane Katrina, 23.8% of 391 New Orleans hemodialysis patients reported symptoms consistent with posttraumatic stress disorder (PTSD). Symptoms were more common in those who missed three or more treatments, were evacuated fewer than two days before landfall, went first to a shelter, or stayed displaced for three months or more.[[dp_hyre2007]]</p>
<p>In the same group, 46% screened positive for depression. Depression was associated with a 33% higher risk of hospitalization or death over the following years (hazard ratio 1.33); PTSD was not significantly associated with those outcomes.[[dp_edmondson2013]] Both studies are observational. They support asking about mood and stress after a disaster, and referring patients who are struggling, as part of ordinary care.</p>
<p>Nurses and social workers can ask simple questions at the first sessions after reopening: how the patient and family are, where they are living, whether they are sleeping, and whether they feel low. The social worker coordinates support (<a href="social-worker-17-transfers-disasters-and-continuity.html">Social Worker, Module 17</a>).</p>
{{call:Any patient who expresses hopelessness or thoughts of self-harm after a disaster: stay with the patient, tell the physician-on-duty at once, and follow your unit&rsquo;s protocol for urgent mental health referral. Always ask the attending nephrologist for guidance.}}
"""),
    ],
    "debrief": ["""
<p><strong>Can the unit open?</strong> No. The water and machines gate is not signed: the water room was flooded, and test results are not back. A phone call saying the readings &ldquo;look fine&rdquo; is not a release. The owner&rsquo;s request does not change the gate; the water technician and the medical head decide when water is fit.</p>
<p><strong>The waiting patients.</strong> The attending nephrologist reviews them by priority (time since treatment, last potassium, fluid status, symptoms). The most urgent go to a receiving unit today, with a handoff; the others get diet and medicine reminders and a planned slot once the water is released.</p>
<p><strong>The reconciliation board.</strong> For each of the 52 patients: dialyzed where and when, sessions missed, need for an extra session, laboratory tests needed. The seven who missed three or more sessions are flagged for the nephrologist first.</p>
"""],
    "skills": {"title": "Restart and reconciliation",
               "intro": "In the restart checklist drill, or after a real closure.",
               "items": [
                   ("Names the five gates in order and who signs each.", True),
                   ("Refuses to open while any gate is unsigned, including a verbal water release.", True),
                   ("Builds the reconciliation board with dialyzed where, sessions missed, extra session needed, laboratory tests needed.", False),
                   ("Flags patients who missed sessions or had shortened sessions for the nephrologist.", False),
                   ("Asks at least one patient and one colleague how they are coping, and knows where to refer.", False),
               ],
               "placement": "Run the restart checklist drill with the head nurse: fill in each gate as if after a flood and note what was hard to confirm."},
    "terms": [("Restart gate", "One of five signed checks before treating patients again."),
              ("Water release", "Signed approval that the water is fit for dialysis."),
              ("Reconciliation", "The record of who was dialyzed where and what each patient needs next."),
              ("Downtime record", "A paper record kept while the electronic system was unavailable."),
              ("Burnout", "Exhaustion and detachment from work after long strain.")],
    "readings": [("typhoon-disaster-preparedness-dialysis.html", "The patient guide, including what happens after the storm.")],
    "calcs": [],
}


import importlib.util as _u
from pathlib import Path as _P
def _ld(n):
    s = _u.spec_from_file_location("dp_" + n, _P(__file__).resolve().parent / (n + ".py")); m = _u.module_from_spec(s); s.loader.exec_module(m); return m
MODULE["quiz"] = _ld("quizutil").balance(_ld("quizbank").QUIZ["11"])
