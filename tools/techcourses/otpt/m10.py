# -*- coding: utf-8 -*-
"""OT/PT track, Module 10: Rehabilitation During Hemodialysis. Written for this series from published sources."""

MODULE = {
    "image_alt": "A patient pedaling a small bed cycle attached to a reclining dialysis chair, the machine in soft focus.",
    "objectives": [
        "Explain why exercise during dialysis is attractive and what hemodynamic risks it must respect.",
        "Summarize the three largest trials of exercise during hemodialysis (HD), DiaTT, PEDAL and CYCLE-HD, including what each did and did not show.",
        "Explain why the trials disagreed, and use that to design a program patients will keep.",
        "Set up intradialytic exercise safely with the nurse: timing, position, access protection and stop rules.",
        "Measure the program with a sit-to-stand test and track adherence.",
    ],
    "big": """
{{plain:Twelve hours a week in a dialysis chair is like a long bus ride three times a week. You cannot get off, but you can stretch your legs. Intradialytic exercise turns dead time into training time, without asking the patient for an extra trip or an extra hour.}}
<p>The picture has a limit. On a bus, nothing is being taken out of your blood. During hemodialysis, two to three liters of fluid may be removed, the blood is outside the body in the circuit, and blood pressure can fall. Exercise also sends blood to working muscles. So timing and position matter: most programs exercise in the first half of the session, before much fluid has been removed and before pressure is likely to fall, with the legs doing the work and the access arm still.</p>
{{fig:otpt10_chairside}}
<p>This module is shared between OT and PT, with the PT leading the exercise prescription. The nurse controls the session and the machine; nothing you do changes either.</p>
{{cards:Key terms for this module|Intradialytic exercise::Exercise performed during the dialysis session.|Bed or pedal cycle::A small cycle ergometer fixed to the foot of the chair.|Adherence::Doing the prescribed amount; not the same as attending.|STS60::Full chair rises in 60 seconds; the main outcome of the DiaTT trial.|Surrogate outcome::A measurement (such as heart mass) used in place of an outcome patients feel.}}
""",
    "case": {"title": "Twelve chairs and one bike", "html": """
<p><strong>Monday, 7:30 a.m.</strong> The Santa Maria Kidney Center has received two donated pedal cycles. Dr. Ramon Uy asks PT Carlo Dizon to &ldquo;start an exercise program on the morning shift: 12 chairs.&rdquo; The head nurse is supportive but worried: &ldquo;Last time a patient fainted on a bike. And who will set them up? My nurses have their hands full at the start of the shift.&rdquo;</p>
<p>Carlo has read about a British trial in which patients cycled during dialysis for six months and quality of life did not improve, and a German trial in which a year of exercise during dialysis improved function. A patient, Mrs. Carmen Velasco, 61, asks him: &ldquo;Will this make me live longer?&rdquo;</p>
""", "questions": ["What did each trial show, and why might they disagree?",
                  "How would you design the program so patients keep doing it?",
                  "What do you say to Mrs. Velasco?"]},
    "sections": [
        ("trials", "The trials", "What the major trials showed", """
<p><strong>DiaTT (Germany).</strong> In a cluster-randomized trial across dialysis units, 1,211 patients were randomized and 917 analyzed (mean age 66). The intervention was 12 months of combined endurance and resistance training during dialysis, supervised by trained staff. The STS60 improved from 16.2 to 19.2 repetitions with exercise and fell from 16.2 to 14.7 with usual care: a difference of 3.85 repetitions (95 percent confidence interval 2.22 to 5.48). The Timed Up and Go improved by 1.1 seconds and the six-minute walk by 37.5 meters, and the physical summary and vitality scores of a quality-of-life questionnaire improved. Adverse events during sessions were similar in both groups. Median hospital days per year were 2 with exercise and 5 with usual care, a secondary outcome. Mortality was not affected.[[otpt_andingrost2023]]</p>
<p><strong>PEDAL (United Kingdom).</strong> In a randomized trial of 379 patients on hemodialysis for more than a year, six months of intradialytic cycling did not significantly improve the physical component of a kidney-specific quality-of-life questionnaire (difference 2.4 units, 95 percent confidence interval &minus;0.1 to 4.8; P = 0.055), and peak oxygen uptake and other secondary outcomes did not improve. Compliance was 47 percent and adherence to the prescription only 18 percent. Harms were similar between groups.[[otpt_greenwood2021]]</p>
<p><strong>CYCLE-HD (United Kingdom).</strong> In a cluster-randomized trial (130 recruited, 101 completed), six months of intradialytic cycling reduced left ventricular mass on cardiac MRI by 11.1 grams versus control and reduced measures of myocardial fibrosis and aortic stiffness, without increasing arrhythmias. Physical function and quality of life did not change.[[otpt_grahambrown2021]] Heart mass is a surrogate: a plausible marker of cardiac risk, not a demonstrated reduction in heart attacks or deaths.</p>
{{fig:otpt10_trials}}
{{key:Supervised, combined, year-long training improved function. Short, cycling-only programs with poor adherence did not. Neither has shown longer survival.}}
"""),
        ("why-differ", "Why they differ", "Why the trials disagreed, and what that means for your program", """
<p>When good trials disagree, the differences between them teach more than either result alone.</p>
<div class="table-wrap"><table>
<thead><tr><th>Feature</th><th>DiaTT (positive for function)</th><th>PEDAL (null for quality of life)</th></tr></thead>
<tbody>
<tr><td>Duration</td><td>12 months</td><td>6 months</td></tr>
<tr><td>Type</td><td>Endurance plus resistance</td><td>Cycling (aerobic) only</td></tr>
<tr><td>Primary outcome</td><td>STS60 (physical function)</td><td>Kidney quality-of-life physical score</td></tr>
<tr><td>Delivery</td><td>Supervised by trained exercise staff</td><td>Prescribed; adherence 18 percent</td></tr>
</tbody></table></div>
<p>The lessons for your unit follow directly. Include resistance work, not only cycling. Plan for a year, not a few weeks. Supervise and coach: an exercise that nobody sets up does not happen. Measure what exercise most directly changes (function) as well as what patients value most (how they feel), and do not promise more than the evidence shows.</p>
{{key:Design for adherence. A perfect prescription done 18 percent of the time is a weak prescription.}}
"""),
        ("setup", "Setting it up", "Setting up intradialytic exercise safely", """
{{flow:Chairside set-up with the nurse|Select::With the nephrologist and head nurse, agree who is eligible (stable sessions, no recent hypotension in the chair) and who is not, per unit protocol.|Screen::Before each session, the nurse confirms stability; you run your screen (Module 3).|Time::Start after the nurse has connected and the session is running smoothly; exercise in the first half; stop well before the end.|Position::Legs do the work; the access arm stays still and visible, needles taped, lines free of the pedals.|Dose::Warm up 2 to 5 minutes; cycle at RPE 11 to 13 progressing toward 30 minutes; add leg resistance (ankle weights, bands, straight-leg raises) on alternate sessions.|Stop::Any symptom, alarm, needle movement, or the nurse&rsquo;s request; nurse checks pressure.|Clean::Wipe the cycle and bands with the approved disinfectant between patients (Module 4).}}
<p>Nurses are busiest at connection and disconnection. A program that relies on nurses to set up bikes during those minutes will fail. Agree a time slot (for example, 30 to 90 minutes into the session) and who does the set-up: you, a trained exercise assistant, or the patient themselves after training.</p>
{{stop:Stop pedaling and call the nurse at once for dizziness, yawning, nausea, cramps, chest discomfort, breathlessness, a machine alarm, any movement of a needle or blood on the dressing, or if the nurse asks. You never silence an alarm or touch the machine or lines.}}
"""),
        ("measure", "Measuring the program", "Measuring the program and keeping it going", """
<p>Use the STS60 or the five-times sit-to-stand at baseline and every three months, on a non-dialysis day or before a session, under standard conditions. The <a href="calc-renal-rehabilitation-toolkit.html#tool-4">sit-to-stand change tracker</a> shows each patient&rsquo;s change, with the DiaTT between-group difference (3.85 repetitions over 12 months) as context, not as an individual target. Track adherence too: sessions offered, sessions done, minutes done. A unit run chart (Module 19) shows whether the program is working at scale.</p>
{{formula:<strong>Illustrative 3-month report, morning shift (12 eligible patients).</strong> Sessions offered 432; sessions with any exercise 302 (70 percent); median minutes per session 18. Median STS60 13 at baseline, 15 at 3 months. Two sessions stopped for dizziness, both resolved with the nurse. Plan: add resistance on alternate days; patient champions for the afternoon shift.}}
{{key:Report adherence beside outcomes. Low adherence explains a weak result better than any other variable.}}
"""),
    ],
    "debrief": ["""
<p><strong>The trials.</strong> DiaTT (12 months, supervised, endurance plus resistance) improved STS60 by 3.85 repetitions versus usual care, with fewer hospital days as a secondary finding and no effect on mortality. PEDAL (6 months, cycling only, 18 percent adherence) did not improve quality of life. CYCLE-HD reduced heart mass, a surrogate, without changing function. They differ in duration, exercise type, supervision and outcome.</p>
<p><strong>Designing for adherence.</strong> Carlo proposes a fixed time slot after connection, set-up by him or a trained assistant rather than the nurses, a combined cycling and leg-resistance program, patient champions, and a plan for at least a year. He agrees eligibility and stop rules with Dr. Uy and the head nurse, and adds cleaning of the cycles between patients.</p>
<p><strong>Mrs. Velasco&rsquo;s question.</strong> &ldquo;The best studies show that exercise during dialysis helps people get stronger, stand up more easily and walk further, and in one large study people spent fewer days in hospital. We don&rsquo;t yet have proof that it makes people live longer. Most people who stay with it say they feel better.&rdquo;</p>
"""],
    "skills": {"title": "Intradialytic exercise set-up",
               "intro": "Set up and supervise simulated intradialytic exercise with a dialysis nurse playing the nurse role.",
               "items": [
                   ("Confirms eligibility and the nurse&rsquo;s go-ahead for this session.", True),
                   ("Positions the cycle so pedals and lines do not touch, and the access arm stays still and visible.", True),
                   ("Times the exercise in the first half of the session and states why.", False),
                   ("Delivers warm-up and dose by RPE, and adds leg resistance work.", False),
                   ("States and applies the stop rules; never touches the machine, alarms or lines.", True),
                   ("Cleans the equipment between patients.", True),
                   ("Records minutes, RPE, any stop and the reason.", False),
               ],
               "placement": "Run or observe a two-week pilot on one shift; report sessions offered, sessions done, minutes, stops and reasons."},
    "terms": [("Intradialytic", "During the dialysis session."), ("Adherence", "Doing the prescribed amount."),
              ("Cluster randomization", "Randomizing whole units, not individual patients."), ("Surrogate outcome", "A measurement standing in for an outcome patients feel.")],
    "readings": [("exercise-guide-ckd.html", "What patients read about exercise and dialysis."),
                 ("post-dialysis-fatigue.html", "Fatigue after dialysis and why activity helps.")],
    "calcs": ["calc-renal-rehabilitation-toolkit.html#tool-4"],
}


import importlib.util as _u
from pathlib import Path as _P
def _ld(n):
    s = _u.spec_from_file_location("otpt_" + n, _P(__file__).resolve().parent / (n + ".py")); m = _u.module_from_spec(s); s.loader.exec_module(m); return m
MODULE["quiz"] = _ld("quizutil").balance(_ld("quizbank").QUIZ["10"])
