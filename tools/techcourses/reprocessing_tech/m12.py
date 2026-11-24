# -*- coding: utf-8 -*-
"""Dialyzer Reprocessing Technician, Module 12: Records, Quality and the Capstone. Merges v0.1 RT15 and RT17."""

MODULE = {
    "image_alt": "A head nurse and a reprocessing technician reviewing a monthly chart of dialyzer discards by reason on a laptop in a small office beside the reuse room.",
    "objectives": [
        "Explain what a complete processing record must prove, and audit a record against the acceptance gates.",
        "Calculate and interpret average uses per dialyzer, discard rates by reason and pyrogenic reactions per 1,000 treatments.",
        "Explain why a rising average use number is not a quality target, and how such targets can make reuse unsafe.",
        "Dispose of discarded dialyzers and chemical waste as the waste procedure and the safety data sheet direct.",
        "Integrate every module in a full capstone case, from receiving to handoff to incident.",
    ],
    "big": """
{{plain:A school report card does not prove a child learned; it proves that a teacher checked and wrote it down. If the teacher fills in grades without testing, the card looks the same but means nothing.}}
<p>The picture has a limit. A false report card misleads parents. A processing record is often the only evidence a patient will ever have that the dialyzer connected to their blood was the right one, cleaned, tested and rinsed. A record that is filled in afterward, or copied, looks exactly like a true one. So records are made at the time, by the person who did the step, and checked by someone else regularly.</p>
{{cards:Key terms for this module|Processing record::The written or electronic evidence that every gate passed for one dialyzer cycle.|Audit::A planned check of records and practice against the program.|Average uses per dialyzer::Total treatments divided by dialyzers used, over a period.|Discard rate::Discarded dialyzers as a share of those processed, by reason.|Perverse incentive::A target that rewards the wrong behavior.|Quality assessment and performance improvement (QAPI)::The unit&rsquo;s system for measuring and improving its own care.}}
<p>Your role in quality is to make honest records, to read the numbers of your own room, and to help the unit improve without ever trading safety for a better-looking number.</p>
""",
    "case": {"title": "A good-looking month", "html": """
<p>At a unit in Cebu, the October reuse report shows the average number of uses per dialyzer rising from 3.6 to 4.4. The operations manager praises the reuse room and suggests a bonus if the number reaches 4.8. The same report shows that discards for failed volume fell to almost zero, while two patients had chills during treatment, compared with none in September.</p>
<p>The head nurse, Ms. Rowena Del Rosario, asks the reprocessing technician, Mr. Mark Gonzales, to help her look at the records before the meeting.</p>
""", "questions": ["What could explain more uses, fewer volume failures and new reactions at the same time?",
                  "What should Mr. Gonzales look for in the records?",
                  "What would a safer target look like?"]},
    "sections": [
        ("records", "What a record proves", "What a complete record proves", """
{{fig:rt12_record}}
<p>A complete record lets someone who was not there prove that every gate passed for this dialyzer, this cycle. It links the dialyzer to its patient, to the water, germicide and reprocessor checks of that run, and to the people who did each step.</p>
<div class="table-wrap"><table>
<thead><tr><th>The record must show</th><th>Gate it proves</th></tr></thead>
<tbody>
<tr><td>Patient identity, second identifier, dialyzer identifier, use number</td><td>Identity, uses left</td></tr>
<tr><td>Eligibility confirmed for the current period</td><td>Eligibility</td></tr>
<tr><td>Time received and time processed</td><td>Time to processing</td></tr>
<tr><td>Run linked to the water log, germicide batch and reprocessor daily check</td><td>Water, germicide, equipment</td></tr>
<tr><td>Baseline and measured TCV; integrity result; inspection</td><td>Performance</td></tr>
<tr><td>Fill time, presence result, storage position</td><td>Disinfection, window</td></tr>
<tr><td>Rinse, residual result and read time, two-person verification</td><td>Safe to connect</td></tr>
<tr><td>Disposition and the person who decided</td><td>Accountability</td></tr>
</tbody></table></div>
<p>Correct an error by a single line through it, with the correction, date and initials, under the procedure. Never erase, overwrite or recopy a record. Electronic records follow the same rule through an audit trail.</p>
{{key:Record at the time, by the person who did it. A record made from memory is a guess written neatly.}}
"""),
        ("numbers", "Reading the numbers", "Reading the room&rsquo;s numbers", """
{{fig:rt12_audit}}
<div class="table-wrap"><table>
<thead><tr><th>Measure</th><th>How to calculate</th><th>What it can tell you</th></tr></thead>
<tbody>
<tr><td>Average uses per dialyzer</td><td>Treatments with reprocessed or new dialyzers &divide; dialyzers used, over the month</td><td>How long dialyzers last; affected by heparin, rinsing, patient factors and the use limit</td></tr>
<tr><td>Discard rate by reason</td><td>Discards for each reason (volume, integrity, clot, visual, expiry, other) &divide; dialyzers processed</td><td>Where failures come from: the floor, the room, or the machine</td></tr>
<tr><td>Pyrogenic reactions per 1,000 treatments</td><td>Reactions &divide; treatments &times; 1,000</td><td>A warning signal; any rise is investigated[[rt_roth2000]]</td></tr>
<tr><td>Records audited with a gap</td><td>Records with any missing gate &divide; records audited</td><td>Whether the evidence can be trusted</td></tr>
</tbody></table></div>
<p>Malaysia&rsquo;s 2026 standards require reuse audits as part of quality management.[[rt_my2026]] One United States unit raised its average uses substantially after standardizing heparin and end-of-treatment rinsing on the floor, with no fall in dialysis adequacy;[[rt_slyby2000]] the improvement came from upstream care, not from relaxing tests.</p>
{{key:Read the numbers together. A number that improves while another warning rises is a question, not a success.}}
"""),
        ("incentives", "Targets that harm", "Targets that make reuse unsafe", """
<p>The average number of uses is a result of good care, not a goal in itself. When staff are rewarded for raising it, the easiest way to raise it is to pass dialyzers that should fail: repeating volume tests until they pass, accepting doubtful integrity results, or stretching storage. The research gives a reason for caution even when tests are honest. In the HEMO analysis, the survival advantage of high-flux dialyzers seen with little reuse reversed with extensive reuse;[[rt_argyropoulos2015]] the finding is an association, but it means more uses is not automatically harmless.</p>
{{cards:Safer measures to praise|Complete records::Share of audited records with no gap.|Honest failures::Failures found and handled correctly, including trace-backs.|Upstream fixes::Fewer clot discards after floor improvements.|Zero tolerance::No sixth use, no release with a failed gate.|Reactions::No unexplained rise in reactions per 1,000 treatments.}}
{{stop:If you are rewarded or pressured for a higher reuse number, tell the head nurse or medical director. A bonus tied to uses can make a room unsafe.}}
"""),
        ("waste", "Waste", "Waste and disposal", """
<p>A discarded dialyzer contains blood residue and, often, germicide. It is infectious waste and, for some germicides, chemical waste. Follow the unit&rsquo;s waste procedure, which follows Philippine health-care waste rules and the SDS. Drain germicide as the SDS and procedure direct before disposal, never into a hand-washing sink. Cut or defaced labels protect privacy.</p>
<p>Reuse reduces plastic waste; one large provider estimated about 10,000 metric tons avoided over its study period.[[rt_bond2011]] Dialysis is among the most resource-intensive treatments in medicine, and the reuse room uses water and chemicals too.[[rt_barraclough2020]] A program that cares about the environment measures both sides.</p>
"""),
        ("capstone", "The capstone", "Capstone: one dialyzer, every gate", """
{{scene:Capstone case|Mrs. Teresita Lim, 66, dialyzes Monday, Wednesday and Friday at 7 a.m. Her dialyzer RU-1104 arrives in the reuse room at 11:20 on Friday after a treatment that ended at 11:05. It is on its fourth use. Its baseline TCV is 96 mL. The water log shows a passing weekly TDS. The germicide batch was tested at 6:30. After processing, measured TCV is 77 mL and the integrity test passes. On Monday at 6:50, the nurse primes a dialyzer for Mrs. Lim. That afternoon, a patient on the next shift has chills, and the biomedical technician reports that the reprocessor&rsquo;s volume sensor read low all last week.}}
<div class="table-wrap"><table>
<thead><tr><th>Step</th><th>What you should decide</th></tr></thead>
<tbody>
<tr><td>Receiving</td><td>Identity, eligibility, use count (next would be the fifth), time to receiving 15 minutes: accept</td></tr>
<tr><td>Volume</td><td>77 &divide; 96 &times; 100 = 80.2%: meets the 80% floor only</td></tr>
<tr><td>Integrity and inspection</td><td>Passed; all other gates recorded</td></tr>
<tr><td>Monday handoff</td><td>Contact time passed, within expiry; residual read at the correct time; two-person verification</td></tr>
<tr><td>The fault report</td><td>A low-reading volume sensor makes TCV results look worse, not better, but every result from the window is uncertain. Trace back all dialyzers processed since the last good check; quarantine stored ones; the medical director decides</td></tr>
<tr><td>The chills</td><td>Keep that patient&rsquo;s dialyzer and lines; check run, water and germicide records; report a possible cluster</td></tr>
<tr><td>After Monday</td><td>RU-1104 has had five uses. It is discarded at its next return, however good its tests look</td></tr>
</tbody></table></div>
{{key:The capstone question is always the same: which gate is proven, which is not, and who decides what is not?}}
"""),
    ],
    "debrief": ["""
<p><strong>What could explain the pattern?</strong> More uses and almost no volume failures can come from genuinely better care on the floor. It can also come from tests being repeated until they pass, a volume sensor drifting, or the use limit being stretched. Two new reactions in the same month make the second set of explanations worth checking before anyone celebrates.</p>
<p><strong>What should Mr. Gonzales look for?</strong> Repeated volume tests on the same dialyzer with only the pass recorded; dialyzers beyond the use limit; gaps in integrity results; reprocessor calibration dates; germicide batch and water results for the days of the reactions; and the processing records of the two dialyzers involved, if they were kept.</p>
<p><strong>A safer target?</strong> Praise complete records, honest failures, fewer clot discards after floor improvements, zero sixth uses and no unexplained reactions. Drop the bonus tied to average uses; Mr. Gonzales and Ms. Del Rosario should say so in the meeting.</p>
"""],
    "skills": {"title": "Record audit and capstone",
               "intro": "Audit twenty synthetic records, then work through the capstone case aloud with your assessor.",
               "items": [
                   ("Identifies every record with a missing or inconsistent gate.", True),
                   ("Corrects a sample record error by the single-line method, without erasing.", True),
                   ("Calculates average uses, discard rate by reason and reactions per 1,000 treatments from a monthly summary.", False),
                   ("Explains why a rising average use number is not a quality target.", True),
                   ("Disposes of a discarded training dialyzer and germicide as the procedure and SDS direct.", True),
                   ("Works the capstone from receiving to handoff, naming each gate and its proof.", True),
                   ("Recognizes the use limit in the capstone and the trace-back window after the fault.", True),
                   ("States who decides each unproven question in the capstone.", False),
               ],
               "placement": "Take part in one monthly reuse audit with the head nurse. Present one finding and one improvement to the unit&rsquo;s quality meeting."},
    "quiz": [
        ("When should a processing record be completed?",
         ["At the end of the week", "At the time, by the person who did the step", "By the head nurse", "Only when a test fails"], 1,
         "Records made later from memory are not evidence."),
        ("How do you correct an error in a paper record?",
         ["Erase it", "Use correction fluid", "A single line through it, with the correction, date and initials", "Recopy the page"], 2,
         "The original must stay readable."),
        ("In a month, 440 treatments used 100 dialyzers. What is the average number of uses?",
         ["0.23", "4.4", "44", "340"], 1,
         "440 &divide; 100 = 4.4."),
        ("2 pyrogenic reactions in 1,600 treatments is how many per 1,000 treatments?",
         ["0.8", "1.25", "2", "16"], 1,
         "2 &divide; 1,600 &times; 1,000 = 1.25."),
        ("Why is a rising average use number not a quality target?",
         ["It is hard to calculate", "Rewarding it can lead staff to pass dialyzers that should fail", "It always means poor care", "PhilHealth forbids counting"], 1,
         "A result of good care becomes dangerous as a goal."),
        ("Average uses rose and volume failures almost disappeared, while reactions appeared. What is the best response?",
         ["Celebrate", "Audit the records, the tests, the equipment and the reactions before drawing conclusions", "Raise the bonus", "Lower the TCV floor"], 1,
         "Read the numbers together."),
        ("What did the improvement report from a United States unit show raised average uses safely?",
         ["Relaxing the volume test", "Standardizing heparin and end-of-treatment rinsing on the floor", "Longer storage", "A stronger germicide"], 1,
         "Upstream care, not looser tests."),
        ("In the capstone, RU-1104 has baseline 96 mL and measured 77 mL. What is the retained TCV?",
         ["77%", "80.2%", "83%", "96%"], 1,
         "77 &divide; 96 &times; 100 = 80.2%, meeting the floor only."),
        ("In the capstone, after Monday&rsquo;s treatment RU-1104 has had five uses. What happens at its next return?",
         ["Process it if tests pass", "Discard it; the use limit is reached", "Reset its count", "Use it once more for the same patient"], 1,
         "No sixth use, whatever the tests."),
        ("How should germicide in a discarded dialyzer be handled?",
         ["Poured into a hand-washing sink", "Drained and disposed of as the SDS and waste procedure direct", "Left in the dialyzer in a general bin", "Mixed with bleach"], 1,
         "Follow the SDS and the waste procedure."),
        ("What did the HEMO secondary analysis suggest about extensive reuse?",
         ["It is proven harmless", "The high-flux survival advantage seen with little reuse reversed with extensive reuse", "It improves survival", "It was not studied"], 1,
         "An association that argues against treating more uses as better."),
        ("You are offered a bonus if the average uses reaches 4.8. What should you do?",
         ["Accept and work harder", "Raise the concern with the head nurse or medical director", "Repeat failed tests", "Extend storage limits"], 1,
         "Incentives tied to uses can make the room unsafe."),
    ],
    "terms": [("Processing record", "Evidence that every gate passed for one dialyzer cycle."),
              ("Audit", "A planned check of records and practice against the program."),
              ("Average uses per dialyzer", "Treatments divided by dialyzers used over a period."),
              ("Discard rate", "Discarded dialyzers as a share of those processed."),
              ("Perverse incentive", "A target that rewards the wrong behavior."),
              ("Audit trail", "An electronic record of who changed what, and when."),
              ("Infectious waste", "Waste contaminated with blood or body fluids.")],
    "readings": [("green-nephrology.html", "The environmental footprint of dialysis and ways to reduce it."),
                 ("dialyzer-reprocessing-reuse.html", "The reference guide to reuse.")],
    "calcs": ["calc-reprocessing-technician-toolkit.html#c6"],
}


# Spread the keyed answers across positions A to D.
import importlib.util as _u
from pathlib import Path as _P
_s = _u.spec_from_file_location("rt_quizutil", _P(__file__).resolve().parent / "quizutil.py")
_q = _u.module_from_spec(_s); _s.loader.exec_module(_q)
MODULE["quiz"] = _q.balance(MODULE["quiz"])
