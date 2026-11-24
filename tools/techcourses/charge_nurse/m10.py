# -*- coding: utf-8 -*-
"""Dialysis Charge Nurse, Module 10: Infection Prevention in Real Time. Written for this series from published sources."""

MODULE = {
    "image_alt": "A charge nurse observing hand hygiene at a dialysis station from a short distance.",
    "objectives": [
        "Explain why dialysis patients and units spread bloodborne and bloodstream infections.",
        "Keep clean and contaminated workflows apart on a busy floor.",
        "Observe practice honestly and give feedback the same shift.",
        "Recognize a possible cluster and escalate it the same day.",
        "Protect staff from sharps injuries and splashes, and know the post-exposure steps.",
    ],
    "big": """
{{plain:A kitchen that cuts raw chicken and salad on the same board, with the same knife, by the same hands, will make someone sick even if every cook is careful most of the time.}}
<p>A dialysis floor for people with chronic kidney disease (CKD) is a shared kitchen with blood. Many patients sit close together, surfaces and equipment are shared, every session opens the bloodstream, and staff move quickly between chairs. Hepatitis B can survive on surfaces for at least a week.[[cdc2001]] One lapse at a crowded moment can carry it from one patient to the next. The kitchen picture holds; the difference is that on a dialysis floor the &ldquo;food&rdquo; is the patient&rsquo;s own blood.</p>
{{cards:Key terms for this module|Hepatitis B virus (HBV)::A virus spread by blood that survives on surfaces for days.|Hepatitis C virus (HCV)::A virus spread by blood; dialysis units have had outbreaks.|Bloodstream infection::Infection in the blood, most often from a catheter.|Cluster::Two or more new infections of the same kind linked by time, place, or staff.|Single-dose vial::A vial meant for one patient, one time.|Post-exposure process::The steps after a needlestick or splash, done within hours.}}
""",
    "case": {"title": "Two positives in a month", "html": """
<p>At a 20-station unit, two patients with previously negative hepatitis C antibody tests turn positive within one month. Both dialyze on the Monday-Wednesday-Friday afternoon shift, at neighboring stations.</p>
<p>The charge nurse that afternoon, Nurse Divina Reyes, notices that medicines are prepared on one end of the same counter where used blood tubes are set down after sampling.</p>
""", "questions": ["Is this a cluster?",
                  "What does Divina do today?",
                  "What does she change at the counter?"]},
    "sections": [
        ("why", "Why dialysis spreads infection", "Why dialysis units spread infection", """
<p>From 2008 to 2011, hepatitis C outbreaks in several United States dialysis units caused at least 46 new infections. Investigators linked them to breaches in handling injectable medicines, in hand hygiene, and in disinfection.[[cn_mbaeyi2013]] In a Dutch unit, gene sequencing traced two new infections to incidents during a single session that the source patient and both new cases attended.[[cn_heikens2019]]</p>
{{fig:cn10_kitchen}}
<p>The reverse is also true. In a Belgian multicenter study, strict infection control, without isolating patients, reduced the yearly hepatitis C seroconversion rate from 1.4% to 0%.[[cn_fabrizi2008]] Practice, not luck, decides.</p>
"""),
        ("core", "Core interventions", "The core interventions", """
<p>The United States Centers for Disease Control and Prevention (CDC) core interventions for dialysis bloodstream infections include surveillance with feedback, hand hygiene audits, catheter and access care observations, staff competency checks, patient education, chlorhexidine skin antisepsis, catheter hub disinfection, and antimicrobial ointment where indicated.[[hn_cdc_core]] In a United States collaborative, facilities that adopted them together saw bloodstream infections fall from 1.09 to 0.89 per 100 patient-months and access-related infections from 0.73 to 0.42; the modeled decreases were 32% and 54%.[[patel2013]] The study had no randomized control group, but the size and consistency of the fall are hard to explain any other way.</p>
"""),
        ("clean", "Clean and dirty", "Clean and dirty never cross", """
<p>Prepare medicines in a clean area away from the stations and from anywhere blood is handled. Use single-dose vials once. Nothing taken to a station goes back to the clean cart, not even an unopened alcohol swab. Clean and disinfect machines and chairs between patients, after the patient has left the station.</p>
{{scene:The swab that went back|<p>Nurse Kat finishes a catheter connection and carries the unused swabs in her gloved hand back toward the clean cart. The charge nurse, walking past, says quietly, &ldquo;Those stay at the station. Bin them.&rdquo; Kat drops them in the bin. Two seconds, said privately, the same minute. That is what changes habits.</p>}}
"""),
        ("observe", "Observe and feed back", "Observe honestly, feed back the same shift", """
<p>A charge nurse who watches two hand hygiene opportunities per nurse per shift and speaks to each nurse right away changes practice more than a monthly poster. Count honestly. An audit that shows 100% every month is probably not looking closely.</p>
<p>Small numbers carry large uncertainty. Report the count with its confidence interval so nobody mistakes noise for improvement (Head Nurse toolkit #c5).</p>
"""),
        ("cluster", "A possible cluster", "A possible cluster: the same day", """
<p>Two new infections of the same kind in a short time, linked by shift, station, or staff, are a possible cluster. Do not wait for a third.</p>
{{fig:cn10_cluster}}
{{flow:The same day|Call::The head nurse, the infection prevention lead, and the attending nephrologist.|Preserve::Records, assignment sheets, and station lists for the period.|Wait::Do not move patients or reassign stations in ways that destroy the evidence before the infection lead decides.|Review::Walk through the shared steps: medicine preparation, sampling, cleaning, hand hygiene.}}
<p>Testing, isolation, and machine decisions belong to the infection lead and the physician under the unit protocol and the newest PSN guidance on bloodborne viruses. The charge nurse&rsquo;s job is to notice, call, and keep the evidence intact.</p>
"""),
        ("staff", "Protecting staff", "Protecting the staff", """
<p>Sharps go into the container at the chair, never recapped by hand. Wear eye protection for connection and disconnection. Know the post-exposure process and its phone number, because hepatitis B and HIV (human immunodeficiency virus) exposures need assessment within hours. A charge nurse who sees a needlestick sends the nurse for assessment now and covers her patients.</p>
"""),
    ],
    "debrief": ["""
<p><strong>Is it a cluster?</strong> Two new hepatitis C positives linked by shift and neighboring stations are a possible cluster. Divina does not wait for a third.</p>
<p><strong>Today.</strong> She calls the head nurse, the infection prevention lead, and the attending nephrologist. She preserves the assignment sheets and station lists. She does not move patients on her own; the infection lead decides testing and station changes.</p>
<p><strong>The counter.</strong> That afternoon she moves medicine preparation to a separate clean area away from where blood tubes are put down, and tells the next charge nurse why. She does a hand hygiene tally: 15 of 24 opportunities, 62.5%, with a 95% confidence interval of roughly 43% to 79% (Head Nurse toolkit #c5). The number is imprecise; its value is the conversation it starts. She gives feedback to each nurse the same day and repeats the tally next week.</p>
"""],
    "skills": {"title": "Infection prevention on the floor",
               "intro": "Observe a full shift for infection prevention and simulate the first steps for a possible cluster.",
               "items": [
                   ("Explains three ways infection spreads in a dialysis unit.", False),
                   ("Keeps medicine preparation in a clean area away from blood handling.", True),
                   ("Stops anything taken to a station from returning to the clean cart.", True),
                   ("Observes hand hygiene and gives feedback privately the same shift.", False),
                   ("Reports an observation rate with its uncertainty.", False),
                   ("Escalates a possible cluster the same day and preserves records.", True),
                   ("States the post-exposure steps and the phone number.", True),
               ],
               "placement": "For two weeks, tally two hand hygiene opportunities per nurse per shift and review the results with the infection lead."},
    "quiz": [
        ("In the CDC collaborative, access-related bloodstream infections fell by a modeled:",
         ["0%", "54%", "90%", "They rose"], 1,
         "From 0.73 to 0.42 per 100 patient-months."),
        ("Where should medicines be prepared?",
         ["Beside the stations", "In a clean area away from stations and blood handling", "On the machine", "Anywhere convenient"], 1,
         "Clean and dirty never cross."),
        ("Two new hepatitis C positives on one shift at neighboring stations are:",
         ["A coincidence", "A possible cluster to escalate today", "Nothing until a third", "A reason to move both patients now"], 1,
         "Call the same day and preserve records."),
        ("Who decides testing and station changes in a cluster?",
         ["The charge nurse", "The infection lead and the physician, per protocol", "The technician", "The patients"], 1,
         "The charge nurse notices, calls, and preserves evidence."),
        ("An audit that shows 100% every month suggests:",
         ["Perfection", "Possibly that nobody is looking closely", "A good poster", "Nothing"], 1,
         "Honest audits find gaps."),
        ("15 of 24 observations equals:",
         ["50%", "62.5%", "75%", "80%"], 1,
         "And the uncertainty is wide with only 24."),
        ("Recapping a used needle by hand is:",
         ["Allowed", "Never done", "Safer", "Optional"], 1,
         "Sharps go straight into the container."),
        ("Single-dose vials are:",
         ["Reused once", "Used once", "Kept for the shift", "Shared between two patients"], 1,
         "Shared vials have caused outbreaks."),
        ("What did the Belgian study show?",
         ["Isolation was essential", "Strict infection control without isolation reduced seroconversion from 1.4% to 0%", "No change", "More infections"], 1,
         "Practice decides."),
        ("How long can hepatitis B survive on surfaces?",
         ["Minutes", "At least seven days", "One hour", "It cannot"], 1,
         "Why cleaning between patients matters."),
        ("Unused swabs from a catheter connection should:",
         ["Go back to the clean cart", "Be discarded at the station", "Be saved for the next patient", "Go in the pocket"], 1,
         "Nothing taken to a station returns to clean supplies."),
        ("A nurse has a needlestick. What do you do?",
         ["Finish the shift first", "Send her for assessment now and cover her patients", "Tell her to wash and continue", "Report it next week"], 1,
         "Post-exposure assessment is needed within hours."),
        ("What were the 2008 to 2011 United States hepatitis C outbreaks linked to?",
         ["Water", "Injectable medicine handling, hand hygiene, and disinfection breaches", "Food", "Machines only"], 1,
         "Everyday practice failures."),
        ("When should feedback on a hand hygiene lapse be given?",
         ["At the annual review", "Privately, the same shift", "Publicly at the huddle", "Never"], 1,
         "Timely and private works best."),
        ("Why not move patients right away in a possible cluster?",
         ["It is not allowed", "It can destroy the evidence the infection lead needs", "Patients refuse", "It costs money"], 1,
         "Preserve, then let the lead decide."),
    ],
    "terms": [("Hepatitis B virus (HBV)", "A virus spread by blood that survives on surfaces for days."),
              ("Hepatitis C virus (HCV)", "A virus spread by blood; dialysis units have had outbreaks."),
              ("Human immunodeficiency virus (HIV)", "A virus spread by blood and body fluids."),
              ("Bloodstream infection", "Infection in the blood, most often from a catheter."),
              ("Cluster", "Two or more new infections linked by time, place, or staff."),
              ("Single-dose vial", "A vial for one patient, one time.")],
    "readings": [("dialysis-machine-assignment.html", "Machine allocation for hepatitis B, hepatitis C, and HIV."),
                 ("dialysis-access-infection.html", "Recognizing and preventing access infections."),
                 ("viral-infections-vaccinations-ckd.html", "Vaccinations, including hepatitis B, in kidney disease.")],
    "calcs": ["calc-dialysis-head-nurse-toolkit.html#c5", "calc-dialysis-head-nurse-toolkit.html#c6", "calc-access-infection-rate.html"],
}

import importlib.util as _u
from pathlib import Path as _P
_s = _u.spec_from_file_location("cn_quizutil", _P(__file__).resolve().parent / "quizutil.py")
_q = _u.module_from_spec(_s); _s.loader.exec_module(_q)
MODULE["quiz"] = _q.balance(MODULE["quiz"])
