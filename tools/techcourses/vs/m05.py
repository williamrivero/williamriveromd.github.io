# -*- coding: utf-8 -*-
"""Vascular Surgeon, Module 5: Make the patient ready for surgery. Written for this track from published sources (v2.0 blueprint)."""

MODULE = {
    "image_alt": "In a pre-operative bay, an anesthesiologist, a surgeon and a nurse review a laboratory printout beside a patient on a trolley.",
    "objectives": [
        "Identify the physiologic threats that make elective access surgery unsafe on the day: potassium, volume, infection and bleeding.",
        "Coordinate dialysis timing, medicines and anesthesia with the nephrologist and anesthesiologist, with one owner for each abnormal result.",
        "Explain what the randomized evidence on regional versus local anesthesia shows, and its limits.",
        "Obtain consent that links the operation to the patient&rsquo;s goals and covers failure, further procedures and alternatives.",
    ],
    "big": """
{{plain:Getting a patient ready for access surgery is like checking a boat before leaving harbor. The trip is short and usually calm, but a boat with a leak or no fuel should not leave, however good the weather.}}
<p>The picture has a limit. A boat&rsquo;s faults stay put. A dialysis patient&rsquo;s physiology moves by the hour. Potassium climbs between sessions; fluid accumulates; a missed treatment turns a routine morning into a dangerous one. Readiness is a check made on the day, not a box ticked at the clinic visit weeks earlier.</p>
{{cards:Key terms for this module|Readiness::The patient, procedure, team and setting are all safe to proceed today.|Hyperkalemia::High blood potassium; it can stop the heart, and surgery and some anesthetic drugs can push it higher.|Brachial plexus block::Regional anesthesia of the arm; it dilates vessels as well as numbing them.|Informed consent::A conversation in which the patient understands the operation, its risks, its alternatives and what happens if it fails.|Decision owner::The clinician who acts on an abnormal result before surgery.}}
<p>Most access patients arrive ready. A few arrive after a missed session, with a high potassium, a fever, or a new anticoagulant. Your work is to catch them before the incision, and to make sure someone owns each abnormal result.</p>
""",
    "case": {"title": "Second on the list", "html": """
<p>Mr. Marcelino Dela Paz, 66, is second on your Thursday list for a left brachiocephalic fistula. He has CKD, is not yet on dialysis, and takes apixaban for atrial fibrillation. Admitted last night for &ldquo;weakness,&rdquo; he missed his nephrology clinic two weeks ago. This morning&rsquo;s potassium is 6.6 mmol/L; it was 5.4 at clinic last month. His electrocardiogram shows peaked T waves. He is short of breath lying flat and has gained 3 kilograms.</p>
<p>The ward resident says, &ldquo;The fistula is important, sir. Can we just do it under local and treat the potassium after?&rdquo;</p>
""", "questions": [
        "Can this operation proceed today?",
        "Who owns the potassium, the fluid and the apixaban decision?",
        "If surgery is postponed, what must the patient and the dialysis team be told?"]},
    "sections": [
        ("threats", "Threats on the day", "Why these four threats matter", """
<p>Potassium is the immediate danger. Kidneys normally excrete most of each day&rsquo;s potassium; without them it accumulates. Tissue injury releases potassium from cells, acidosis shifts it out of cells, and succinylcholine, if a general anesthetic uses it, raises it further. The heart&rsquo;s resting membrane potential depends on the ratio of potassium inside and outside cells; as outside potassium rises, the membrane partially depolarizes, conduction slows, and an arrhythmia can follow. Peaked T waves are a warning that this process has started.</p>
{{fig:vs05_a}}
<p>Volume is the second. A patient who cannot lie flat cannot lie still for a fistula operation, and sedation can tip borderline lungs into failure. Infection is the third: a fresh synthetic graft placed during bacteremia may become infected. Bleeding is the fourth: anticoagulants and uremic platelet dysfunction both raise hematoma risk, and a hematoma can compress a new anastomosis.</p>
<div class="table-wrap"><table>
<thead><tr><th>Threat</th><th>Mechanism</th><th>What you may see</th><th>Usual owner of the fix</th></tr></thead>
<tbody>
<tr><td>Hyperkalemia</td><td>No renal excretion; cell shifts from acidosis and tissue injury</td><td>Weakness, peaked T waves, a rising trend</td><td>Nephrologist, with anesthesia</td></tr>
<tr><td>Volume overload</td><td>No urine output; missed treatment</td><td>Orthopnea, weight gain, crackles</td><td>Nephrologist</td></tr>
<tr><td>Active infection</td><td>Bacteremia seeds new material</td><td>Fever, a red catheter exit, positive cultures</td><td>Treating team; surgeon decides on deferral</td></tr>
<tr><td>Bleeding risk</td><td>Anticoagulants, antiplatelets, uremic platelets</td><td>New drugs on the chart, prolonged bleeding</td><td>Prescriber, surgeon and anesthesia together</td></tr>
</tbody></table></div>
{{key:An elective access benefit never outweighs an immediate physiologic threat. Fix the threat, then operate.}}
"""),
        ("anesthesia", "Anesthesia evidence", "Regional, local or general: what the evidence shows", """
<p>Regional anesthesia does more than numb the arm. A brachial plexus block interrupts the sympathetic nerves that constrict arm vessels, so the artery and vein dilate and flow through a new anastomosis rises. Aitken and colleagues randomized 126 adults having radiocephalic or brachiocephalic fistulas in Glasgow to local anesthesia or a brachial plexus block. Primary patency at three months was 84% with the block and 62% with local anesthesia (odds ratio 3.3), and the difference was larger for radiocephalic fistulas (77% versus 48%). No serious procedure-related adverse events occurred.[[vs_aitken2016]]</p>
{{fig:vs05_b}}
<p>That is one three-center trial with a surrogate outcome at three months; it does not show longer-term functional use or effects on survival. Larger multicenter trials with longer follow-up are needed. The UK Kidney Association (UKKA) 2025 guideline suggests routinely favoring local or regional anesthesia for adult fistula formation (statement 3.5, grade 2B), and avoiding low blood pressure perioperatively and during maturation, with review of medicines and target weight (3.8, grade 2C).[[vs_ukka]] The mechanism is the same: low pressure means low flow, and low flow encourages thrombosis in a new fistula.</p>
{{flow:Coordinating the day of surgery|Night before::Dialysis timing agreed; potassium and weight checked; anticoagulant plan confirmed.|Morning check::Repeat potassium and vital signs; ask about breathlessness, fever, new drugs.|Huddle::Surgeon, anesthesiologist and nurse confirm readiness and the anesthesia plan.|Decide::Proceed, delay, or cancel, with a named owner for each abnormality.|Communicate::Tell the patient and the dialysis unit what happens next.}}
"""),
        ("consent", "Consent", "Consent that means something", """
<p>Consent is not the signature. It is the patient understanding what you propose, why, what can go wrong, what happens if the access does not work, and what the alternatives are, including not operating. For access surgery, the material facts include the chance of primary failure, the likely need for further procedures, the risk of hand ischemia and bleeding, and the time before the access can be used.</p>
<p>Connect the operation to the goals agreed in the Life-Plan. Medication interruptions, antibiotic prophylaxis and anesthetic plans are individual decisions under your institution&rsquo;s approved protocols; do not borrow another patient&rsquo;s plan. Give clear written instructions: when to stop and restart each drug, when to come, what to do if dialysis becomes urgent before the operation, and whom to call.</p>
{{scene:Pre-operative clinic, fictional|<p>Mrs. Teresita Manalo, 59, asks whether she can stop her clopidogrel. She had a coronary stent five months ago. You do not answer from memory; you call her cardiologist, who advises continuing it. You plan the fistula with meticulous hemostasis and document the discussion.</p><p class="tc-scene-take"><b>What this shows.</b> Bleeding decisions belong to the patient&rsquo;s whole risk, not to the surgeon&rsquo;s preference alone.</p>}}
{{call:Postpone elective access surgery and contact the nephrologist and anesthesiologist when the potassium is high with electrocardiographic changes, the patient cannot lie flat, there is fever or bacteremia, or an anticoagulant plan is missing.}}
"""),
    ],
    "debrief": [
        "<p><strong>Proceed today?</strong> No. A potassium of 6.6 mmol/L with peaked T waves, orthopnea and a 3 kilogram gain are immediate threats. Elective access surgery under any anesthetic would add stress, tissue injury and a supine position to an unstable patient.</p>",
        "<p><strong>Owners.</strong> The nephrologist owns the potassium and the fluid: this may mean urgent medical treatment and possibly urgent dialysis, which in turn may need a catheter. The prescriber and the anesthesiologist, with you, own the apixaban plan for the rescheduled date. You own the decision to postpone, the new date, and making sure the access plan survives the change.</p>",
        "<p><strong>Communication.</strong> Explain to Mr. Dela Paz, in plain words, why the operation is postponed and that it remains planned. Tell the nephrologist and, if a catheter is placed, the dialysis unit which side to protect and when the fistula is now expected. Record the reason for postponement and who owns each step.</p>",
    ],
    "skills": {"title": "Pre-operative readiness huddle",
               "intro": "Rehearse with a fictional case or observe a real list under supervision.",
               "items": [("Reviews the latest potassium, trend and electrocardiogram", True),
                         ("Assesses volume status and ability to lie flat", True),
                         ("Reconciles anticoagulants and antiplatelets with the responsible prescriber", False),
                         ("Checks for active infection before placing synthetic material", False),
                         ("Names the decision owner for each abnormal result", True),
                         ("Confirms consent covers failure, further procedures and alternatives", False)],
               "placement": "Pre-operative bay or simulation"},
    "quiz": [
        ("A patient who missed dialysis arrives for elective access surgery with a high potassium and electrocardiographic changes. What is the best action?",
         ["Resolve the immediate risk with nephrology and anesthesia before elective surgery", "Proceed because the access is beneficial",
          "Ask the patient whether the result matters", "Proceed under local anesthesia only"],
         0, "An elective benefit does not remove an immediate physiologic threat."),
        ("Which perioperative medication plan is appropriate?",
         ["Stop every medicine for every patient", "Individual reconciliation using approved protocols and the responsible teams",
          "Reuse another patient&rsquo;s plan", "Continue everything without review"],
         1, "Medication and bleeding decisions depend on the patient and the procedure."),
        ("In the Aitken randomized trial, what did brachial plexus block improve compared with local anesthesia?",
         ["One-year mortality", "Three-month primary patency (84% versus 62%)", "Infection rates", "Time to first cannulation"],
         1, "The surrogate outcome of three-month primary patency improved; longer-term outcomes were not tested."),
        ("Why does regional anesthesia plausibly help a new fistula?",
         ["It lowers potassium", "Sympathetic blockade dilates the artery and vein, increasing flow", "It prevents infection",
          "It shortens the operation"],
         1, "Vasodilation raises early flow, which may reduce early thrombosis."),
        ("UKKA 2025 statement 3.8 suggests avoiding what during the perioperative and maturation period?",
         ["Arm exercise", "Low blood pressure, with review of medicines and target weight", "Duplex ultrasound", "Early clinic review"],
         1, "Low pressure lowers fistula flow; the statement is graded 2C."),
    ],
    "terms": [("Peaked T waves", "Tall, narrow T waves on the electrocardiogram, an early sign of hyperkalemia."),
              ("Orthopnea", "Breathlessness when lying flat, often from fluid on the lungs.")],
    "readings": [("potassium-hyperkalemia-ckd.html", "Why potassium rises in kidney disease and how it is treated."),
                 ("heart-failure-ckd.html", "Volume and the heart in kidney disease.")],
    "calcs": ["calc-potassium-load.html", "calc-has-bled.html", "calc-af-anticoagulation.html"],
}

import importlib.util as _u
from pathlib import Path as _P
_s = _u.spec_from_file_location("vs_quizutil", _P(__file__).resolve().parent / "quizutil.py")
_q = _u.module_from_spec(_s); _s.loader.exec_module(_q)
MODULE["quiz"] = _q.balance(MODULE["quiz"])
