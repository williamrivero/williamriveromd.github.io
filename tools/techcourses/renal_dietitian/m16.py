# -*- coding: utf-8 -*-
"""Renal Dietitian, Module 16: Transitions of Care, Quality Improvement, and Capstone. Written for this series from published sources."""

MODULE = {
    "image_alt": "A dietitian presenting a simple run chart on a wall board to a nurse and a nephrologist in a unit meeting room.",
    "objectives": [
        "Write a nutrition handoff that survives a move between clinic, hospital, dialysis unit, and home.",
        "Define a nutrition quality measure with a numerator, denominator, period, and data source.",
        "Add a balancing measure that shows whether the change caused harm elsewhere.",
        "Plot and read a simple run chart.",
        "Combine assessment, prescription, counseling, monitoring, and escalation in one case.",
        "Stop routine work and escalate when a critical result arrives.",
    ],
    "big": """
{{plain:Each time a patient moves, from clinic to hospital, hospital to dialysis, or dialysis to home, the nutrition plan is carried across a river. Some plans arrive intact. Many are dropped halfway, and the patient lands with an old restriction or no plan at all. A good handoff is a bridge. A quality measure is a count of how many plans make it across.}}
<p>The picture has a limit. A plan does not simply arrive or sink. It can arrive changed, such as an old protein target copied forward from a discharge note, or arrive complete with no one owning it. And a count of plans that crossed says nothing about whether patients ate better unless you measure that too. Your work in this module is to hand off each nutrition plan with confirmation, and to measure handoffs in a way that shows whether care actually improved.</p>
{{cards:Key terms for this module|Transition of care::A move between settings or teams.|Handoff::Passing responsibility and information to the next person, with confirmation.|Quality measure::A defined count that shows how often care meets a standard.|Numerator and denominator::The patients who met the standard, out of all the patients who should have.|Balancing measure::A count that checks whether improving one thing made another worse.|Run chart::A graph of a measure over time, used to see whether a change made a difference.|Plan-Do-Study-Act (PDSA)::A small test of change: plan it, try it, study the result, and act on what you learned.}}
{{flow:A small improvement cycle|Measure now::Baseline for several weeks.|Plan::One change, one owner.|Do::Test it on a small scale.|Study::Plot the result on a run chart.|Act::Keep, adapt, or drop it.}}
""",
    "case": {"title": "Capstone: Ramon", "html": """
<p>Ramon, 63, moved from CKD G5 to maintenance hemodialysis three weeks ago. His agreed calculation weight today is 60 kg after dialysis. At his first outpatient session it was 63 kg after dialysis. He estimates he eats about 45 g of protein a day, about half his usual meals, and he avoids food until he gets home after treatment. His potassium is stable. His phosphorus is above the unit&rsquo;s range for the second month in a row, and he is unsure when to take his binder. He likes rice, fish, and vegetables.</p>
<p>The unit is testing a change: every new patient should have a dietitian assessment within 14 days of starting HD. The log shows 9 of 12 eligible new patients were assessed in time last quarter.</p>
<p><em>During the exercise, after you describe routine follow-up, the examiner will hand you a new result.</em></p>
""", "questions": ["Write the assessment, a PES statement, and the protein calculation.",
                  "Give a patient-chosen change, a monitoring plan, and a handoff line about the phosphorus.",
                  "Calculate the quality measure and propose a balancing measure."]},
    "sections": [
        ("handoff", "Handoffs", "A handoff that survives the move", """
<p>Plans are lost at transitions. A low-protein order from the clinic follows the patient into the ICU. A hospital tube-feeding plan ends at discharge with nobody watching intake at home. A new dialysis patient keeps a pre-dialysis diet for months. The fix is a short, structured nutrition handoff every time a patient moves.</p>
{{cards:What a nutrition handoff carries|The question::Why the patient was referred and what is still open.|Kidney status::Cause, stage or treatment type, and any recent change.|Weights::Comparable weights with dates and timing.|Intake::What the patient eats now, and the main barrier.|Prescription::Energy and protein targets, the guideline used, and why they changed.|Open issues::Results awaiting review, binder questions, supplements.|Owner and date::Who follows up and when.|Acceptance::Who received the handoff and confirmed it.}}
<p>Give the patient the next step too, in plain words: what to eat this week and when the next check is. Follow your facility&rsquo;s documentation and privacy rules. Academy exercises use only fictional patients.</p>
<p><strong>Example from practice.</strong> Mr. Lopez, 67, goes home after an admission for AKI on G3b CKD. His handoff to the clinic reads: &ldquo;Question: rewrite the nutrition plan after discharge. Kidney: AKI on CKD G3b, recovering; eGFR 38 at discharge, 52 before admission. Weights: usual 64 kg, discharge 61 kg (no edema). Intake: about two-thirds of meals; main barrier is fatigue. Prescription: 1.0 g/kg in hospital (ESPEN) must be reviewed against KDIGO 0.8 g/kg once recovered. Open: phosphate 2.6 mg/dL at discharge. Owner: clinic dietitian, visit within 7 days. Accepted by: Ms. Abella, clinic dietitian, 14:20.&rdquo; Each line answers a question the next person would otherwise have to ask.</p>
{{fig:rd16_fig_nutrition_handoff_eight_items}}
"""),
        ("measure", "Measuring quality", "Define a measure, then add its balance", """
<p>Quality improvement starts with a clear count. A vague aim, such as &ldquo;better nutrition care for new patients,&rdquo; cannot be measured. A defined measure can.</p>
<div class="table-wrap"><table>
<thead><tr><th>Part</th><th>Example</th></tr></thead>
<tbody>
<tr><td>Denominator</td><td>Adults who started outpatient HD in the unit during the month, with transfers in counted by a written rule</td></tr>
<tr><td>Numerator</td><td>Those in the denominator with a documented dietitian assessment within 14 days of the first session</td></tr>
<tr><td>Period</td><td>Each calendar month, reported quarterly</td></tr>
<tr><td>Data source</td><td>The unit&rsquo;s admission log and the nutrition notes</td></tr>
<tr><td>Target</td><td>Set locally from the baseline; the 14-day window is an illustrative local standard, not a guideline</td></tr>
</tbody></table></div>
<p>Then add a <strong>balancing measure</strong>. If the dietitian rushes every new patient to meet the 14-day window, other work may suffer. Count something that would reveal that: assessment time per patient, the share of assessments with a complete monitoring plan, or the number of follow-up visits missed for existing patients.</p>
{{formula:Measure (%) = numerator &divide; denominator &times; 100. Example: 9 &divide; 12 &times; 100 = 75%.}}
<p>Plot the measure month by month on a run chart, mark when the change began, and look for a sustained shift rather than reacting to one good or bad month. Small numbers swing widely; 9 of 12 and 10 of 12 differ by one patient.</p>
{{fig:rd16_runchart}}
<p><strong>Example from practice.</strong> A unit raised its 14-day assessment measure from 9 of 12 (75%) to 12 of 12 (100%) in one quarter. The balancing measure told the rest of the story. Missed follow-up visits for existing patients rose from 2 to 9 in the same quarter. The new patients were seen on time because the dietitian dropped visits for patients already on the roster. The change worked, and it had a cost. The next step is to change the work, perhaps with group sessions for routine follow-up, and keep both measures on the same run chart.</p>
"""),
        ("capstone", "The capstone", "Putting it all together", """
<p>A safe capstone answer connects everything in this series: comparable weights, the right protein range for the treatment, laboratory trends read with their causes, the patient&rsquo;s own priorities, and a clear path for escalation. It also shows judgment: the plan changes when the patient&rsquo;s condition changes, and routine work stops when a critical result arrives.</p>
{{flow:Capstone checklist|Assess::Comparable weights, intake, barriers, results.|Diagnose::A PES statement with a cause you can act on.|Prescribe::Targets with the weight and guideline named.|Counsel::One change the patient chooses; teach-back.|Monitor::Measure, date, owner.|Hand off::Open issues to the right person.|Escalate::Stop and call when the situation changes.}}
{{stop:If a critical result with new symptoms arrives at any point, stop the routine work. Activate the urgent pathway, give a structured handoff, obtain a read-back, and document who accepted responsibility.}}
<p>Scoring is described on the trainer page. The capstone passes at 8 of 10, with the escalation criterion scored as complete and independent.</p>
<p><strong>Example from practice.</strong> Two trainees answer the same item for a different patient, Mrs. Yap, whose phosphorus has been high for two months. One writes: &ldquo;Low-phosphorus diet; avoid dairy and meat.&rdquo; The other writes: &ldquo;Phosphorus 6.8 and 7.0 mg/dL. Takes her binder after meals, not with them. Lunch includes two colas and processed meat. Plan: binder with the first bites, as written; replace the colas and processed meat; keep protein at 1.0 to 1.2 g/kg; recheck next month; binder-timing finding sent to the prescriber.&rdquo; The second answer names a cause, keeps protein, and sends the dose question to the right person. That is what the examiner is looking for.</p>
"""),
    ],
    "debrief": ["""
<p><strong>Assessment and calculation.</strong> Comparable post-dialysis weights: (63 &minus; 60) &divide; 63 &times; 100 = 4.8% in three weeks. Confirm with the nurse that this is tissue loss and not a change in dry weight. Stable HD protein at 60 kg: 1.0 to 1.2 &times; 60 = 60 to 72 g a day. He eats about 45 g, so he is 15 to 27 g short. Before finalizing, check for acute illness or other reasons he may not be metabolically stable.</p>
<p><strong>PES.</strong> &ldquo;Inadequate oral intake related to missed meals around dialysis, as evidenced by about half his usual intake, an estimated 45 g of protein a day, and a 4.8% loss on comparable post-dialysis weights over three weeks.&rdquo;</p>
<p><strong>Change and monitoring.</strong> Ask what he could manage on dialysis days. He likes fish and rice: perhaps a small rice-and-fish packed meal or a fish sandwich to eat early in the session or right after, if the unit allows. Use teach-back. Recheck intake and same-timing weights in one week.</p>
<p><strong>Phosphorus handoff.</strong> &ldquo;Ramon&rsquo;s phosphorus is above range for the second month. He is unsure of his binder timing. I have checked his diet for additives and found [result]. Could pharmacy confirm the prescribed binder instructions with him? His protein intake is low, so please do not restrict protein.&rdquo;</p>
<p><strong>Quality measure.</strong> 9 &divide; 12 = 75%. A balancing measure: assessment time per new patient, or the share of assessments with a complete monitoring plan, reported each quarter.</p>
<p><strong>The new result.</strong> When the examiner reports a critical potassium with new weakness, stop the routine work at once. Activate the urgent pathway, give the structured handoff, obtain a read-back, and document who accepted it. Everything else can wait. Knowing when to stop the diet plan is the last skill in this series, and the most important.</p>
"""],
    "skills": {"title": "Capstone integration and quality measure",
               "intro": "Allow 25 minutes for the written plan and 5 minutes for the oral handoff. The examiner introduces a critical result after routine follow-up is described.",
               "items": [
                   ("Calculates comparable weight loss and the stable HD protein range, with the stability caveat.", False),
                   ("Writes a PES statement with an actionable cause and a patient-chosen change with teach-back.", False),
                   ("Protects protein intake while addressing persistent high phosphorus and binder timing.", False),
                   ("Sets a monitoring measure, an interval, and an owner.", False),
                   ("On the critical result with weakness, stops routine work, activates the urgent pathway, and confirms an accepted handoff.", True),
                   ("Calculates the quality measure and defines a balancing measure with a reporting period.", False),
               ],
               "placement": "With your preceptor, choose one nutrition measure your unit could track, define its numerator and denominator, and collect three months of baseline data."},
    "quiz": [
        ("Comparable post-dialysis weights were 63 kg and now 60 kg. The loss is about:",
         ["3.0%", "4.8%", "5.0%", "6.3%"], 1,
         "(63 − 60) ÷ 63 × 100 = 4.8%."),
        ("At 60 kg on stable HD, protein should be about:",
         ["45 g/day", "48 g/day", "60 to 72 g/day", "90 g/day"], 2,
         "1.0 to 1.2 × 60."),
        ("9 of 12 eligible new patients were assessed in time. The measure is:",
         ["67%", "75%", "80%", "90%"], 1,
         "9 ÷ 12 = 75%."),
        ("Which is a balancing measure for faster new-patient assessments?",
         ["Number of new patients", "Assessment time per patient or completeness of monitoring plans", "Weight of new patients", "Number of dialysis machines"], 1,
         "It shows whether speed came at a cost."),
        ("The denominator in the example is:",
         ["Assessed patients", "All adults who started outpatient HD in the period, by the written rule", "All patients in the unit", "Dietitians on staff"], 1,
         "The patients who should have met the standard."),
        ("A run chart is used to:",
         ["Calculate protein", "See whether a measure changes over time after a change", "Store laboratory results", "Assign blame"], 1,
         "Look for sustained shifts."),
        ("With small numbers, a change from 9 of 12 to 10 of 12:",
         ["Proves the change worked", "Is one patient and may be chance", "Is a decline", "Cannot be calculated"], 1,
         "Small samples swing widely."),
        ("Which item belongs in every nutrition handoff?",
         ["The dietitian&rsquo;s opinion of the physician", "Who follows up and when", "The patient&rsquo;s religion", "The unit&rsquo;s budget"], 1,
         "Ownership and timing make a handoff work."),
        ("A low-protein order from the clinic is still active after a new HD start. This is an example of:",
         ["Good continuity", "A plan lost or mis-carried at a transition", "A quality measure", "A balancing measure"], 1,
         "Transitions are where plans fail."),
        ("In the capstone, the binder question should be:",
         ["Solved by doubling the dose", "Handed to pharmacy to confirm prescribed timing", "Ignored", "Solved by stopping fish"], 1,
         "Timing is clarified by the prescriber or pharmacist."),
        ("What should happen first when a critical potassium with weakness is reported mid-session?",
         ["Finish the food recall", "Give a potassium handout", "Activate the urgent pathway and confirm the handoff", "Schedule a follow-up"], 2,
         "Routine work gives way to urgent care."),
        ("PDSA stands for:",
         ["Plan, Do, Study, Act", "Prescribe, Dose, Supply, Audit", "Plan, Document, Sign, Archive", "Patient, Doctor, Staff, Admin"], 0,
         "A small test-of-change cycle."),
        ("A vague aim becomes a measure when it has:",
         ["A slogan", "A numerator, denominator, period, and data source", "A poster", "A meeting"], 1,
         "Definition makes it countable."),
        ("Why add a stability check before finalizing the HD protein range?",
         ["Stable patients need less", "Acute illness changes needs and the meaning of urea-based estimates", "It is optional", "Protein is fixed"], 1,
         "The stable range assumes metabolic stability."),
        ("The patient-facing part of a handoff should include:",
         ["Only codes", "The next step in plain words and the next check date", "The guideline grade", "Nothing"], 1,
         "Patients need to know what to do next."),
    ],
    "terms": [("Transfer rule", "A written rule on whether patients arriving from another unit are counted."),
              ("Baseline", "Measurements taken before a change is tested."),
              ("Sustained shift", "A change on a run chart that lasts over several points, not one month."),
              ("Closed loop", "A handoff confirmed by read-back and acceptance."),
              ("Capstone", "A final case that combines all the skills of the course.")],
    "readings": [("dialysis-qapi-vs-cqi.html", "Quality programs in dialysis units.")],
    "calcs": ["calc-qapi-run-chart-spc.html", "calc-qapi-cqi-toolkit.html", "calc-dialysis-qapi-scorecard.html"],
}

# Spread the keyed answers across positions A to D.
import importlib.util as _u
from pathlib import Path as _P
_s = _u.spec_from_file_location("rd_quizutil", _P(__file__).resolve().parent / "quizutil.py")
_q = _u.module_from_spec(_s); _s.loader.exec_module(_q)
MODULE["quiz"] = _q.balance(MODULE["quiz"])
