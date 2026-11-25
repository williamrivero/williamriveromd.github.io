# -*- coding: utf-8 -*-
"""Dialyzer Reprocessing Technician, Module 01: The Reuse Room and Your Place in It. Merges v0.1 RT01 and RT16."""

MODULE = {
    "image_alt": "A reprocessing technician at the door of a small reuse room, handing a labeled dialyzer to a dialysis nurse, with the dialysis floor visible behind.",
    "objectives": [
        "Describe reprocessing as one competency shared by the reprocessing operator, the dialysis technician and the biomedical technician, and what each may do with it.",
        "Name who decides patient eligibility, who decides use on the patient, who proves processing, and who restores equipment.",
        "State the tasks outside your scope, even when a lesson mentions them.",
        "Act correctly when two people disagree about a dialyzer: quarantine, then a written decision.",
        "Explain why a knowledge pass, an observed practical, and a facility authorization are three different things.",
    ],
    "big": """
{{plain:Think of a family that washes and reuses the same baby bottle for one child. It works because the bottle never goes to another child, it is washed the same way every time, and somebody checks it before the next feed. Dialyzer reuse runs on the same three ideas: one patient, one method, one check before use.}}
<p>The picture has a limit. A baby bottle is simple, and a mistake is usually small. A dialyzer holds about ten thousand hollow fibers, each thinner than a hair, and the next patient&rsquo;s blood flows through all of them. A mix-up can give a patient someone else&rsquo;s blood residue, a clotted filter that cleans poorly, or a dose of disinfectant. So reuse is safe only when every step is done, checked and written down.</p>
{{cards:Key terms for this module|Reprocessing::Cleaning, testing, disinfecting and storing a used dialyzer so the same patient can use it again. Also called reuse.|Reuse program::The unit&rsquo;s approved written system for reprocessing: who is eligible, which method, which tests, which records.|Operator::A person authorized by the facility to reprocess dialyzers.|Release::Making a reprocessed dialyzer available for the patient&rsquo;s next treatment.|Quarantine::Holding a dialyzer, a batch or a machine aside, labeled, until a decision is made.|Scope::The tasks your training and your facility&rsquo;s written authorization allow you to do.}}
<p>Most dialyzers in a well-run program pass through the room without incident. A few fail a test or arrive with a problem. Your work is to prove the first kind safe, step by step, and to stop the second kind before it reaches a patient.</p>
{{fig:rt01_lifecycle}}
""",
    "case": {"title": "A quiz is not a key", "html": """
<p>It is 6:10 on a Tuesday morning at a sixteen-station unit in Bulacan. Mr. Jun Soriano, a biomedical technician, has just finished the common knowledge module of the reprocessing track with a score of 5 of 5. The reuse room is behind schedule because the regular operator, Ms. Liza Dimaculangan, is on leave.</p>
<p>The charge nurse, Ms. Tess Lagman, asks Mr. Soriano to &ldquo;release the 6:30 dialyzers, since you passed the course.&rdquo; Three dialyzers have been processed overnight by a relief operator. One of them, labeled RU-0412, has a blank space where the integrity test result should be. The first patient is already on the weighing scale.</p>
""", "questions": ["Can Mr. Soriano release the dialyzers because he passed the quiz?",
                  "What should happen to dialyzer RU-0412?",
                  "Who should Ms. Lagman call, and what does the patient receive in the meantime?"]},
    "sections": [
        ("one-competency", "One competency", "One competency, three jobs", """
<p>Reprocessing is a technical patient-safety competency. It belongs to several jobs at once. The Department of Health (DOH) licensing order lists daily reprocessor calibration, collection, reprocessing, acceptance testing, labeling, records and storage among the duties of the dialysis technician.[[doh2012]] The Philippine Society of Nephrology (PSN) expects technicians to finish a structured training program of three months or longer.[[psn2024]] Some units hire a person only for the reuse room; others give the work to dialysis technicians; biomedical technicians service the reprocessor itself.</p>
<div class="table-wrap"><table>
<thead><tr><th>Job</th><th>What they do in the reuse room</th><th>What the job does not include</th></tr></thead>
<tbody>
<tr><td>Reprocessing operator</td><td>Receives, processes, tests, stores and documents each dialyzer under the approved program</td><td>Deciding who is eligible for reuse; using the dialyzer on a patient</td></tr>
<tr><td>Dialysis technician</td><td>The operator&rsquo;s work, plus machine preparation and other duties the facility assigns</td><td>Cannulation, medicines, or changing a prescription unless separately authorized by law and the facility</td></tr>
<tr><td>Biomedical technician</td><td>Installs, calibrates, maintains and repairs the reprocessor and water system within service authorization</td><td>Releasing a patient&rsquo;s dialyzer</td></tr>
</tbody></table></div>
<p>The track sits in the Renal Technicians track of the Academy, beside the Dialysis, Water Treatment and Biomedical Equipment Technician tracks. The reuse room still works under the medical director and alongside the nursing service, and completing a technician track gives no nursing or clinical scope.</p>
{{key:Knowing how to reprocess is shared. Being allowed to release a dialyzer is granted, one person at a time, by the facility.}}
"""),
        ("who-decides", "Who decides", "Who decides what", """
<p>Every safe decision in the reuse room has an owner. When ownership is clear, a technician can stop a dialyzer without arguing about who is in charge.</p>
{{fig:rt01_decisions}}
<div class="table-wrap"><table>
<thead><tr><th>Decision</th><th>Owner</th><th>Your part</th></tr></thead>
<tbody>
<tr><td>Whether the unit reuses at all, which method and germicide, and who is eligible</td><td>Medical director</td><td>Know the program and the eligibility list. Hold any dialyzer whose eligibility is unknown.</td></tr>
<tr><td>Whether a dialyzer is used on the patient today</td><td>Dialysis nurse</td><td>Give the nurse a dialyzer with complete evidence, and verify identity with the nurse.</td></tr>
<tr><td>Whether processing passed</td><td>Authorized operator</td><td>Prove each gate in the record. Report every failure.</td></tr>
<tr><td>Whether a reprocessor is fit for use after service</td><td>Biomedical technician, per the service procedure</td><td>Report faults and odd readings. Do not use equipment tagged out.</td></tr>
<tr><td>How to respond to contamination or a cluster of reactions</td><td>Infection prevention lead with the medical director</td><td>Quarantine, preserve evidence, and report.</td></tr>
</tbody></table></div>
<p>Disagreement happens. A nurse wants a dialyzer now; a technician sees a gap in its record. Production pressure is real, but it cannot settle a safety question. The rule is simple: the dialyzer goes to quarantine, the patient receives a new dialyzer, and the question is answered in writing by the person who owns it.</p>
{{stop:When two roles disagree about a dialyzer, quarantine it and give the patient a new one. Never settle the question by using it.}}
"""),
        ("scope", "Your scope", "The edges of your scope", """
<p>This track mentions many tasks that belong to other people: setting up a dialysis machine, connecting a patient, giving heparin, repairing an electrical board. A lesson that describes a task does not authorize you to do it.</p>
{{cards:Outside the reprocessing operator&rsquo;s scope unless separately authorized|Patient care::Cannulation, connecting or disconnecting a patient, giving any medicine.|Prescriptions::Choosing or changing a dialyzer type, a blood flow, or a dialysis order.|Eligibility::Deciding that a patient may or may not reuse.|Internal repair::Opening a reprocessor or water-system component beyond the user maintenance in its manual.|Overrides::Bypassing an alarm, a failed test, or an interlock.}}
<p>Before you accept a new duty, ask two questions: which written scope covers this, and who has watched me do it? If either answer is &ldquo;no one,&rdquo; the answer to the task is &ldquo;not yet.&rdquo;</p>
<p>Respect belongs to scope as well. The dialyzers you handle carry patients&rsquo; names and infection status. Speak about them only to the people who need to know, and never photograph a label on a personal phone.</p>
{{key:A lesson that describes a task is not permission to do it. Written scope plus observed practice is.}}
"""),
        ("completion", "What completion means", "Knowledge, practice, authorization: three different things", """
<p>The Academy can teach principles and record what you have learned. It cannot watch your hands. The track keeps five states apart, and they must never be merged.</p>
{{flow:From first lesson to facility authorization|Learning::Reading the modules and working through the cases.|Knowledge assessed::Self-assessments and the end-of-track examination.|Supervised practice::Workplace hours on the unit&rsquo;s own reprocessor, with an assessor.|Practical assessed::Observed full cycles with every critical item met.|Facility authorized::A written decision by the facility on what you may do. This happens outside the Academy.}}
<p>Each state proves something different. A quiz shows that you know the steps. An observed practical shows that you can do them on that equipment. A facility authorization says that the unit accepts responsibility for letting you do them. A person who passes a quiz has moved one step, not five.</p>
<p>The same logic applies to people moving between countries. A United States patient-care technician must be certified within 18 months of hire under federal rules, and the water-system technician role is addressed separately;[[rt_cfr494]] a Philippine certificate does not transfer automatically, and neither does a foreign one. Job titles vary as well: one 2025 Philippine job posting for reprocessing work used the title &ldquo;adding machine technician.&rdquo; Read the duties, not the title.</p>
{{key:A score shows knowledge. Only an assessor can show competence, and only the facility can grant authority.}}
"""),
        ("team", "Working with the team", "Working with the team", """
<p>The reuse room depends on the people upstream and downstream. A nurse who rinses the dialyzer well at the end of treatment and gives enough heparin during it sends you a cleaner dialyzer. In one United States unit, a team project that standardized heparin and end-of-treatment rinsing raised the average number of uses per dialyzer substantially without any fall in dialysis adequacy.[[rt_slyby2000]] It was a single-unit improvement report, not a trial, but the lesson holds: most failed dialyzers are made on the floor, not in the room.</p>
<p>Report what you see in a way the floor can use. &ldquo;Three dialyzers from station 5 failed volume this week, all with clotted headers&rdquo; is a fact a head nurse can act on. &ldquo;Station 5 is careless&rdquo; is not.</p>
{{cards:Good reports from the reuse room|What::The finding, with the dialyzer identifiers.|When::Date, time, and how many times it has happened.|Where it may come from::The station, the shift, or the step, without blame.|What you did::Quarantine, discard, report, and who you told.}}
"""),
    ],
    "debrief": ["""
<p><strong>Can Mr. Soriano release the dialyzers?</strong> No. He has passed a knowledge check. He has not been observed releasing dialyzers on this unit&rsquo;s reprocessor, and the facility has not authorized him as an operator. His biomedical role covers the reprocessor, not patient dialyzers. He can help in the room within his scope, for example by checking whether the reprocessor printout shows the integrity result.</p>
<p><strong>What happens to RU-0412?</strong> A blank integrity result means the gate is unproven. The dialyzer goes to quarantine with a hold label. It is not released on the assumption that the test was done. If the reprocessor memory shows a recorded pass, an authorized operator can complete the record later under the SOP; if not, the dialyzer is reprocessed or discarded as the program directs.</p>
<p><strong>Who does Ms. Lagman call?</strong> The head nurse or the person the unit designates for reuse-room questions, and, if no authorized operator is available, the medical director&rsquo;s designate. The patient receives a new dialyzer for today. That costs one dialyzer. Using an unproven one could cost far more.</p>
"""],
    "skills": {"title": "Responsibility map and escalation drill",
               "intro": "Complete this with your preceptor, using a training dialyzer with a deliberately incomplete record.",
               "items": [
                   ("Names the owner of each decision: eligibility, use on the patient, processing, equipment fitness, contamination response.", True),
                   ("Identifies the missing gate in the record and states that the dialyzer is unproven.", True),
                   ("Applies a quarantine label and moves the dialyzer to the quarantine shelf.", True),
                   ("States that the patient receives a new dialyzer while the question is answered.", True),
                   ("Refuses, politely and clearly, a request to release outside authorization.", True),
                   ("Names the person to call when no authorized operator is present.", False),
                   ("Writes a short factual report: what, when, where it may come from, what was done.", False),
                   ("States two tasks outside the operator&rsquo;s scope.", False),
               ],
               "placement": "During your first week in the reuse room, draw your unit&rsquo;s actual responsibility map with names and contact numbers, and have the head nurse confirm it."},
    "quiz": [
        ("A biomedical technician scores 5 of 5 on the common knowledge module. What may he now do?",
         ["Release patient dialyzers on any shift",
          "Continue to work within his biomedical scope; release requires an observed practical and a facility authorization",
          "Release dialyzers only when no operator is on duty",
          "Release dialyzers if the charge nurse agrees"], 1,
         "A knowledge pass is one of several states. Release authority is granted by the facility after an observed practical."),
        ("Who decides whether a patient is eligible for dialyzer reuse?",
         ["The reprocessing technician", "The charge nurse", "The medical director, through the approved program", "The patient&rsquo;s family"], 2,
         "Eligibility is a clinical program decision. The technician holds any dialyzer whose eligibility is unknown."),
        ("A nurse asks for a dialyzer whose record has a missing test result. What is the safest response?",
         ["Release it, since the test is usually passed",
          "Repeat the missing test without recording it",
          "Quarantine it, and give the patient a new dialyzer while the question is answered",
          "Ask the patient whether to use it"], 2,
         "An unproven gate is a failed gate until proven otherwise. A new dialyzer protects the patient today."),
        ("Which task is within a reprocessing operator&rsquo;s usual scope?",
         ["Cannulating the patient&rsquo;s fistula", "Labeling and storing a processed dialyzer", "Adjusting the heparin dose", "Opening the reprocessor to replace a circuit board"], 1,
         "Labeling and storage are core operator duties. The others belong to nurses, physicians or service staff."),
        ("Why must two disagreeing staff members not settle the question by using the dialyzer?",
         ["Because the nurse is always right",
          "Because production pressure cannot resolve a safety question; the owner of the decision must answer in writing",
          "Because the technician is always right",
          "Because the patient must decide"], 1,
         "Quarantine first, then a written decision by the person who owns it."),
        ("What does an observed practical assessment show that a quiz cannot?",
         ["That you know the steps", "That you can perform them correctly on that equipment", "That you are licensed", "That the facility accepts responsibility"], 1,
         "A quiz tests knowledge. Only observation shows performance on the unit&rsquo;s own reprocessor."),
        ("A job posting lists the title &ldquo;adding machine technician&rdquo; but describes dialyzer reprocessing. What should you rely on?",
         ["The title", "The duties described", "The salary", "The employer&rsquo;s size"], 1,
         "Titles vary between employers. The duties tell you what the job is."),
        ("According to the improvement report from a United States unit, where are most failed dialyzers made?",
         ["In the reuse room", "On the dialysis floor, through heparin and end-of-treatment rinsing", "In the factory", "In the storage rack"], 1,
         "Standardizing heparin and rinsing on the floor raised the average number of uses. It was a single-unit report, not a trial."),
        ("Which report from the reuse room is most useful to the head nurse?",
         ["&ldquo;Station 5 is careless.&rdquo;",
          "&ldquo;Three dialyzers from station 5 failed volume this week, all with clotted headers; quarantined and discarded.&rdquo;",
          "&ldquo;Too many failures lately.&rdquo;",
          "&ldquo;The night shift does not care.&rdquo;"], 1,
         "A useful report gives what, when, where it may come from, and what was done, without blame."),
        ("What does the DOH licensing order list among dialysis technician duties?",
         ["Prescribing dialyzer size", "Daily reprocessor calibration, reprocessing, acceptance testing, labeling, records and storage", "Cannulation", "Ordering laboratory tests"], 1,
         "AO 2012-0001 lists the reuse-room tasks among technician duties."),
        ("Which statement about this track&rsquo;s place in the Academy is correct?",
         ["Completing it confers nursing registration",
          "It allows the holder to release dialyzers anywhere",
          "It is a technician track; the reuse room works under the medical director and alongside the nursing service",
          "It replaces the Dialysis Technician track"], 2,
         "Placement tells learners where to find the track. It confers no nursing or clinical scope."),
        ("You are asked to photograph a dialyzer label to send to a colleague on a personal phone. What do you do?",
         ["Send it, since it is for work", "Decline; share patient information only through the unit&rsquo;s approved channels", "Crop the name and send it", "Send it to a group chat"], 1,
         "Labels carry patient identity and sometimes infection status. Use approved channels only."),
    ],
    "terms": [("Reprocessing", "Cleaning, testing, disinfecting and storing a used dialyzer for the same patient&rsquo;s next treatment."),
              ("Reuse program", "The unit&rsquo;s approved written system for reprocessing."),
              ("Operator", "A person authorized by the facility to reprocess dialyzers."),
              ("Release", "Making a reprocessed dialyzer available for the next treatment."),
              ("Quarantine", "Holding a dialyzer, batch or machine aside, labeled, until a decision is made."),
              ("Scope", "The tasks your training and written authorization allow."),
              ("Facility authorization", "A written decision by the facility on the tasks a person may perform.")],
    "readings": [("dialyzer-reprocessing-reuse.html", "The site&rsquo;s reference guide to dialyzer reuse, its history and its risks.")],
    "calcs": [],
}


# Spread the keyed answers across positions A to D.
import importlib.util as _u
from pathlib import Path as _P
_s = _u.spec_from_file_location("rt_quizutil", _P(__file__).resolve().parent / "quizutil.py")
_q = _u.module_from_spec(_s); _s.loader.exec_module(_q)
MODULE["quiz"] = _q.balance(MODULE["quiz"])
