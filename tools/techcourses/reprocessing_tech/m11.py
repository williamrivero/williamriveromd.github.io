# -*- coding: utf-8 -*-
"""Dialyzer Reprocessing Technician, Module 11: Machines, Faults and When Things Go Wrong. Merges v0.1 RT12, RT13 and RT14."""

MODULE = {
    "image_alt": "A biomedical technician and a reprocessing technician at an automated reprocessor with its side panel closed, comparing a calibration log with a reference gauge.",
    "objectives": [
        "Explain what daily reprocessor checks and periodic calibration prove, and what a failed check means for dialyzers already processed.",
        "Separate the operator&rsquo;s user checks from the biomedical technician&rsquo;s service work, and equipment return to service from dialyzer release.",
        "Trace every dialyzer processed since the last good check after an equipment fault.",
        "Recognize a cluster of fever and chills during dialysis as a possible reprocessing or water event, and respond.",
        "Act in the first hour of a power, water or reprocessor failure, and know when reuse must stop.",
    ],
    "big": """
{{plain:A weighing scale at the market that reads half a kilo heavy cheats every customer from the moment it went wrong, not only the one who noticed. Fixing the scale today does not refund yesterday&rsquo;s customers.}}
<p>The picture has a limit. A market scale cheats people of money. A reprocessor that measures volume wrongly, or holds pressure falsely, passes dialyzers that should have failed, and those dialyzers have gone to patients. So a fault raises two questions: how to fix the machine, and which dialyzers were processed while it was wrong.</p>
{{cards:Key terms for this module|Daily check::The user check of the reprocessor at the start of each day, as its manual and the program set.|Calibration::Comparing the machine&rsquo;s readings with a reference and correcting them, by trained service staff.|Tag-out::Labeling equipment as out of service so nobody uses it.|Return to service::The service technician&rsquo;s documented decision that equipment works correctly after repair.|Trace-back::Identifying every dialyzer processed between the last good check and a fault.|Pyrogenic reaction::Fever, chills or rigors during dialysis, caused by bacterial products reaching the blood.}}
<p>Most days the machine works and the checks pass. Your job is to prove that it worked, every day, and to stop and trace when it did not.</p>
""",
    "case": {"title": "A week out of calibration", "html": """
<p>On a Thursday at a unit in Iloilo, the biomedical technician, Mr. Ernesto Villanueva, performs the scheduled calibration of the reprocessor. He finds that its pressure sensor has been reading high. He compares it with his reference gauge and estimates that the error began after a power fluctuation the previous Thursday. In the past week, 84 dialyzers were processed on that reprocessor.</p>
<p>Meanwhile, the head nurse mentions that two patients had chills in the first hour of treatment on Tuesday, both with reprocessed dialyzers. The daily checks in the log were all marked &ldquo;OK.&rdquo;</p>
""", "questions": ["What does a high-reading pressure sensor mean for the integrity tests done this week?",
                  "Which dialyzers are affected, and what should happen to them?",
                  "How are the Tuesday chills connected, and who must be told?"]},
    "sections": [
        ("checks", "Daily checks and calibration", "Daily checks and calibration", """
<p>The DOH licensing order lists daily reprocessor calibration among technician duties.[[doh2012]] In practice, the operator performs the user checks the reprocessor manual sets each day, and trained service staff perform periodic calibration against reference instruments.</p>
<div class="table-wrap"><table>
<thead><tr><th>What is checked</th><th>Why it matters</th><th>Who</th></tr></thead>
<tbody>
<tr><td>Self-test passed; alarms work</td><td>The machine can detect its own faults</td><td>Operator, daily</td></tr>
<tr><td>Germicide and cleaning agent supply and lines</td><td>Prevents weak or missing chemicals</td><td>Operator, daily</td></tr>
<tr><td>Volume and pressure measurement against a reference</td><td>TCV and integrity results are only as good as these sensors</td><td>Service technician, at the interval the manual sets</td></tr>
<tr><td>Water supply pressure and quality at the reprocessor</td><td>Rinsing and dilution depend on it</td><td>Operator and water technician</td></tr>
</tbody></table></div>
<p>A check written as &ldquo;OK&rdquo; proves nothing unless it records what was checked and the reading. A daily check that would not detect the fault you care about is not a check of that fault.</p>
{{key:Every TCV and integrity result depends on the sensors that measured it. Prove the sensors, or the results prove nothing.}}
"""),
        ("boundaries", "Service boundaries", "Who fixes, who releases", """
<div class="table-wrap"><table>
<thead><tr><th>Task</th><th>Operator</th><th>Biomedical technician</th></tr></thead>
<tbody>
<tr><td>User checks in the manual</td><td>Yes</td><td>Trains and audits</td></tr>
<tr><td>Opening panels, replacing sensors or boards</td><td>No</td><td>Yes, within service authorization</td></tr>
<tr><td>Calibration</td><td>No</td><td>Yes, with traceable reference instruments</td></tr>
<tr><td>Returning the reprocessor to service</td><td>No</td><td>Yes, after a documented performance check</td></tr>
<tr><td>Releasing a patient&rsquo;s dialyzer</td><td>Yes, if authorized</td><td>No</td></tr>
</tbody></table></div>
<p>Two decisions are easy to confuse. &ldquo;The reprocessor works again&rdquo; is the biomedical technician&rsquo;s return to service. &ldquo;This dialyzer may be used&rdquo; is the operator&rsquo;s release under the program. A repaired machine does not release the dialyzers that passed through it while broken.</p>
{{stop:Equipment tagged out is not used, by anyone, until it is returned to service in writing.}}
"""),
        ("traceback", "Tracing back", "Tracing back after a fault", """
{{fig:rt11_traceback}}
<p>When a fault is found, find the last time the equipment was proven good: the last passed calibration or the last check that would have detected this fault. Every dialyzer processed between then and now is in question.</p>
{{flow:Trace-back|Fix the window::Last proven-good check to the time of discovery.|List::Every dialyzer processed on that equipment in the window, with patient, date and use.|Quarantine::Stored dialyzers from the window are held.|Assess::The medical director decides, with the biomedical and infection prevention leads, whether to reprocess, retest, or discard, and whether patients need review.|Notify::Nurses caring for affected patients; the medical director informs patients as the program and ethics require.|Record::The fault, the window, the list, the decisions.}}
{{key:After a fault, ask which dialyzers, not only what broke.}}
"""),
        ("reactions", "Reactions in patients", "When patients react", """
<p>Fever, chills or rigors during dialysis, especially in the first hour and in more than one patient, may be a pyrogenic reaction from bacterial products in the water, the dialysis fluid or the dialyzer. Outbreak investigations have traced such clusters to reprocessing and water failures many times.[[rt_beck1990]][[rt_archibald2006]][[rt_roth2000]] Bloodstream infection can look the same at first.</p>
{{fig:rt11_quarantine}}
{{cards:What the reuse room does when patients react|Tell::The nurse and head nurse are told at once; the physician treats the patient.|Keep::The dialyzer and blood lines from the reacting patient are kept, capped and labeled, not discarded, for possible testing.|Look::Check the processing records of the dialyzers involved, the germicide batch, the water log and the reprocessor checks for the same period.|Hold::If a common cause is plausible, stored dialyzers from the same run or batch are held.|Report::The infection prevention lead looks for a cluster; the CDC advises tracking pyrogenic reactions and investigating any rise.[[rt_roth2000]]}}
{{stop:Two or more patients with fever or chills on the same day is a possible cluster. Keep the dialyzers, check the run, and report before the next shift is processed.}}
"""),
        ("continuity", "Power and water failure", "When the power, water or reprocessor fails", """
<p>Typhoons, floods and power interruptions are part of Philippine practice. The FDA advises that dialyzers should not be reused when reprocessing or required refrigeration facilities are not functioning.[[rt_fda_restart]]</p>
<div class="table-wrap"><table>
<thead><tr><th>Failure</th><th>First actions in the reuse room</th><th>Before restarting</th></tr></thead>
<tbody>
<tr><td>Power interruption during a run</td><td>Note the time; dialyzers in an interrupted cycle are unproven and held</td><td>Reprocessor self-test and the checks the manual requires; consider whether the event could have shifted calibration</td></tr>
<tr><td>Water treatment failure or a failed water result</td><td>Stop processing; refrigerate used dialyzers within their limit, or discard per procedure</td><td>Water cleared in writing by the person responsible (Module 5)</td></tr>
<tr><td>Refrigeration failure</td><td>Note the time and temperature; used dialyzers past their limit are not processed</td><td>Refrigerator repaired and logging again</td></tr>
<tr><td>Reprocessor failure</td><td>Tag it out; patients receive new dialyzers</td><td>Return to service in writing; trace-back if the fault may predate discovery</td></tr>
</tbody></table></div>
<p>A unit continues to dialyze patients through these events, with new dialyzers. The continuity plan should say where extra dialyzers come from and who decides when reuse resumes.</p>
{{key:When the system that proves a dialyzer is broken, reuse stops. Patients still get treatment, with new dialyzers.}}
"""),
    ],
    "debrief": ["""
<p><strong>What does a high-reading pressure sensor mean?</strong> In a pressure-hold test, a leak shows as pressure falling. A sensor that reads high may make a leaking dialyzer appear to hold pressure. Integrity results from the past week cannot be trusted. The daily &ldquo;OK&rdquo; entries did not test the sensor against a reference, so they could not catch this fault.</p>
<p><strong>Which dialyzers?</strong> All 84 processed since the last proven-good check, from the previous Thursday&rsquo;s power event, or from the last calibration if the start is uncertain. Stored ones are quarantined. The medical director decides, with the biomedical and infection prevention leads, whether to retest on a verified machine or discard, and whether patients treated with them need review.</p>
<p><strong>The Tuesday chills?</strong> Two patients with chills in the first hour, both with reprocessed dialyzers, during a week when integrity results were unreliable, is a possible link. If their dialyzers were kept, they can be examined. The head nurse, the medical director and the infection prevention lead must know today, and the water and germicide records for the same days are checked. The reprocessor returns to service only after Mr. Villanueva documents its repair and performance.</p>
"""],
    "skills": {"title": "Fault, trace-back and continuity drill",
               "intro": "A tabletop exercise with synthetic logs, then a walk-through at the reprocessor with the biomedical technician.",
               "items": [
                   ("Performs and records the reprocessor&rsquo;s daily user checks with actual readings.", True),
                   ("Tags out a faulty reprocessor and refuses to use it until written return to service.", True),
                   ("Identifies the trace-back window from a set of logs.", True),
                   ("Lists and quarantines the dialyzers processed in the window.", True),
                   ("Keeps the dialyzer and lines from a patient with a pyrogenic reaction.", True),
                   ("Checks the processing, germicide, water and reprocessor records for a cluster.", False),
                   ("States the first actions for power, water, refrigeration and reprocessor failures.", True),
                   ("Distinguishes equipment return to service from dialyzer release.", True),
               ],
               "placement": "Read your unit&rsquo;s continuity plan for the reuse room. Find where extra dialyzers come from in a failure, and who decides when reuse resumes."},
    "quiz": [
        ("A reprocessor&rsquo;s pressure sensor is found reading high. What does that mean for recent integrity tests?",
         ["Nothing", "A leaking dialyzer may have appeared to pass; recent results cannot be trusted", "All dialyzers failed", "Only volume results are affected"], 1,
         "Integrity depends on accurate pressure measurement."),
        ("After a fault is found, which dialyzers are in question?",
         ["Only today&rsquo;s", "Every dialyzer processed since the last proven-good check", "None, once the machine is fixed", "Only those that failed"], 1,
         "The trace-back window starts at the last proof that the equipment was good."),
        ("Who returns a repaired reprocessor to service?",
         ["The operator", "The biomedical technician, after a documented performance check", "The charge nurse", "The patient"], 1,
         "Return to service is a service decision."),
        ("Does returning the reprocessor to service release the dialyzers processed while it was faulty?",
         ["Yes", "No; those dialyzers need their own decision", "Only if they passed", "Only for eligible patients"], 1,
         "Repairing the machine does not prove past results."),
        ("Two patients have chills in the first hour of treatment on the same day, both with reprocessed dialyzers. What does the reuse room do?",
         ["Discard both dialyzers to keep the room clean", "Keep the dialyzers and lines, check the run records, hold related stored dialyzers, and report", "Nothing; the physician handles it", "Increase germicide strength"], 1,
         "A possible cluster needs evidence kept and records checked."),
        ("A daily check written only as &ldquo;OK&rdquo; is weak because:",
         ["It is too short", "It does not record what was checked or the reading", "It uses English", "It was done daily"], 1,
         "Evidence needs the reading."),
        ("Which task is outside the reprocessing operator&rsquo;s scope?",
         ["Daily user checks", "Replacing a pressure sensor", "Tagging out a faulty machine", "Keeping dialyzers after a reaction"], 1,
         "Internal repair belongs to authorized service staff."),
        ("What does the FDA advise when reprocessing or required refrigeration is not working?",
         ["Reuse as usual", "Do not reuse dialyzers", "Double the germicide", "Store at room temperature"], 1,
         "Reuse stops when the proving system is broken."),
        ("Power fails in the middle of a reprocessing cycle. What happens to the dialyzers in that cycle?",
         ["They are released", "They are unproven and held", "They are discarded without a record", "They are counted as passed"], 1,
         "An interrupted cycle proves nothing."),
        ("During a water treatment failure, patients:",
         ["Are sent home", "Continue treatment with new dialyzers while reuse stops", "Use unprocessed dialyzers", "Skip a week"], 1,
         "Treatment continues; reuse waits for proof."),
        ("Why does the CDC advise tracking pyrogenic reactions over time?",
         ["For billing", "So a rise can be noticed and investigated", "Because they are rare", "To rank nurses"], 1,
         "Surveillance finds clusters early."),
        ("What should a continuity plan for the reuse room say?",
         ["Nothing; reuse never stops", "Where extra dialyzers come from and who decides when reuse resumes", "Only the phone number of the supplier", "Which patients to skip"], 1,
         "Planning prevents unsafe improvisation."),
    ],
    "terms": [("Daily check", "The operator&rsquo;s start-of-day check of the reprocessor."),
              ("Calibration", "Comparing readings with a reference and correcting them."),
              ("Tag-out", "Labeling equipment as out of service."),
              ("Return to service", "The documented decision that repaired equipment works correctly."),
              ("Trace-back", "Identifying every dialyzer processed between the last good check and a fault."),
              ("Pyrogenic reaction", "Fever, chills or rigors during dialysis caused by bacterial products."),
              ("Cluster", "More cases than expected in a short time or one place.")],
    "readings": [("hemodialysis-complications.html", "Problems during dialysis, including fever and chills."),
                 ("typhoon-disaster-preparedness-dialysis.html", "Keeping dialysis going through typhoons and floods.")],
    "calcs": [],
}


# Spread the keyed answers across positions A to D.
import importlib.util as _u
from pathlib import Path as _P
_s = _u.spec_from_file_location("rt_quizutil", _P(__file__).resolve().parent / "quizutil.py")
_q = _u.module_from_spec(_s); _s.loader.exec_module(_q)
MODULE["quiz"] = _q.balance(MODULE["quiz"])
