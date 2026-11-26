# -*- coding: utf-8 -*-
"""Dialysis Charge Nurse, Module 03: Building the Assignment. Written for this series from published sources."""

MODULE = {
    "image_alt": "Hands placing colored magnets on a dialysis assignment board while two nurses and an orientee look on.",
    "objectives": [
        "Weight each patient by what they need, not just count heads.",
        "Match each task to a nurse&rsquo;s verified competence, including orientees.",
        "Keep your own load light enough to stay free for the floor.",
        "Plan staggered breaks so that no nurse ever covers more running machines than is safe.",
        "Rebuild the assignment when the shift changes, and tell the team.",
    ],
    "big": """
{{plain:Loading a jeepney is not only counting passengers. A jeepney with twelve adults is not the same as one with eight adults, three sacks of rice, and a crate of chickens. The driver who counts only heads gets stuck on the first hill.}}
<p>An assignment that counts only patients makes the same mistake. Four patients with mature fistulas and steady pressures take less nursing than two patients with new catheters, one of whom drops her pressure every session. The work is in the needs, and the needs change during the shift.</p>
<p>The picture has a limit. A jeepney&rsquo;s load is fixed once it leaves the terminal; a patient&rsquo;s needs are not. Pressure falls in the second hour, a needle fails, a nurse is pulled to the ward, and the load on each nurse changes while the chairs stay the same. Your work in this module is to assign by need and competence at 6:00, plan the breaks, and rebuild the assignment when the needs change.</p>
{{cards:Key terms for this module|Acuity::How much nursing attention a patient is likely to need today.|Competence::A skill a nurse has performed correctly while a qualified person observed and signed.|Orientee::A nurse in orientation who works under a named resource nurse.|Resource nurse::The experienced nurse an orientee calls for help.|Break cover::The nurse who watches another nurse&rsquo;s patients during her break.|Load::The total nursing need assigned to one nurse.}}
""",
    "case": {"title": "&ldquo;Four each, like always&rdquo;", "html": """
<p>At a 12-station unit in Quezon City, Nurse Joy Bautista takes charge with three staff nurses: Arnel (eight years in dialysis), Kris (two years), and Mika (third week of orientation). Twelve patients are booked: two with new tunneled catheters, one with frequent low blood pressure during dialysis, one HBsAg-positive patient in the isolation room, one blind patient who needs help walking, and seven stable patients with fistulas.</p>
<p>The habit at this unit is &ldquo;four each, the charge nurse takes none.&rdquo; Breaks are decided at 8:00 by whoever is hungry first.</p>
""", "questions": ["Why does &ldquo;four each&rdquo; fail here?",
                  "Build a better assignment.",
                  "How will breaks work so that no nurse covers too many running machines?"]},
    "sections": [
        ("acuity", "Acuity, simply", "Acuity, simply", """
<p>Give each patient points for the things that take nursing time or need watching: a new or problem access, a catheter connection, a history of low pressure or arrhythmia during dialysis, isolation, limited mobility or confusion, a first session, a blood transfusion or intravenous (IV) medicine today. Add them up for each nurse.</p>
{{fig:cn03_jeepney}}
<div class="table-wrap"><table>
<thead><tr><th>Patient need (example scale; your unit sets its own)</th><th>Points</th></tr></thead>
<tbody>
<tr><td>Stable patient, mature fistula or graft</td><td>1</td></tr>
<tr><td>Add: new or problem access, needling help</td><td>+1</td></tr>
<tr><td>Catheter connection and disconnection</td><td>3 (instead of 1)</td></tr>
<tr><td>Add: frequent low pressure or arrhythmia during dialysis</td><td>+2</td></tr>
<tr><td>Add: isolation</td><td>+2</td></tr>
<tr><td>Add: needs help walking, confused, or new to dialysis</td><td>+1</td></tr>
<tr><td>Add: transfusion or IV medicine during the session</td><td>+1</td></tr>
</tbody></table></div>
<p>Be honest about what this is. Points are a tool for seeing the load, not a validated score. No acuity tool for outpatient hemodialysis has been shown in trials to improve patient outcomes. You use one because it makes invisible work visible on the board, so the whole team can see why an assignment is fair.</p>
"""),
        ("competence", "Competence", "Competence is specific", """
<p>&ldquo;Two years&rsquo; experience&rdquo; tells you little. Can she cannulate a new fistula? Connect a catheter alone with aseptic technique? Recognize air in the venous line? An orientee assigned four patients is a staff nurse on paper and a learner in fact.</p>
<p>The national guidelines for nursing delegation summarize the match as five rights: the right task, the right circumstance, the right person, the right communication, and the right supervision. Nursing judgment itself cannot be delegated.[[cn_ana_ncsbn2019]] These guidelines are from the United States, but the logic applies to any unit: you assign a task only to someone who can do it, in today&rsquo;s conditions, with clear instructions and someone watching.</p>
<p>Keep a simple competence list where the charge nurse can see it: each nurse, and which high-risk tasks are signed off (catheter connection, new fistula needling, isolation care, transfusion). An orientee always has a named resource nurse on the board.</p>
{{scene:&ldquo;I&rsquo;ve seen it done many times&rdquo;|<p>Mika, the orientee, tells the charge nurse she is comfortable connecting the catheter patient in Bed 7; she has watched it many times. Her competence record shows catheter connection not yet signed off.</p>
<p>The charge nurse pairs her with Arnel for that connection. Arnel watches, Mika does it, and Arnel signs the first of three observed connections in her record. Mika learns; the patient is safe; the record shows the truth.</p>}}
"""),
        ("ownload", "Your own load", "The charge nurse&rsquo;s own load", """
<p>A charge nurse with four patients of her own cannot leave her chairs when another nurse&rsquo;s patient collapses. On a heavy morning, keep two chairs or none, placed near the center of the floor where you can see the rest.</p>
<p>In a United States study that asked 427 emergency nurse leaders and educators what charge nurses must be able to do, the top five competencies were managing patient flow, communication, situational awareness, clinical decision-making, and the nurse-patient assignment.[[cn_wolf2024]] The setting was the emergency department, not dialysis, but every one of those five needs free attention, and a full assignment uses it up.</p>
{{key:The charge nurse needs free eyes. Every chair you take is attention you cannot give the floor.}}
"""),
        ("breaks", "Breaks", "Breaks are part of the assignment", """
<p>Breaks are when ratios quietly double. If two nurses on a four-nurse floor take their break together, the other two each cover six or eight running machines for half an hour.</p>
{{fig:cn03_breaks}}
<p>Plan breaks at 6:00, when you build the assignment, not at 8:00 when people are hungry. Three rules:</p>
<ul>
<li>One break at a time, and never two neighboring pods together.</li>
<li>No breaks in the first 30 minutes after connection or the last 30 before disconnection, when most low-pressure, needle, and bleeding problems happen.</li>
<li>Brief the covering nurse on each patient&rsquo;s one key risk: &ldquo;Bed 4 drops after the second hour.&rdquo;</li>
</ul>
<p>Breaks are not optional for the nurse either. In a study of hospital nurses&rsquo; logbooks, the odds of making an error were about three times higher on shifts lasting 12.5 hours or more.[[hn_rogers2004]] Tired nurses make the errors that charts record.</p>
"""),
        ("rebuild", "Rebuild", "Rebuild when things change", """
<p>The assignment you write at 6:00 is a plan, not a promise. A patient arrives breathless; a nurse is pulled to the ward; a machine fails; an emergency takes two nurses for twenty minutes. When that happens, re-score the affected pods and move one patient rather than leaving one nurse overloaded. Tell the whole team at the next huddle (Module 4), and update the board.</p>
{{scene:The ward pull at 7:30|<p>At 7:30 the hospital nursing supervisor asks for one dialysis nurse to help on the medical ward for an hour. The charge nurse checks the board: taking Kris would leave Arnel and Mika covering eleven running machines, with Mika unable to do catheter care. She tells the supervisor what she can release safely (no one until the 9:00 disconnections, then Kris for an hour) and writes the request and her answer in the shift log. The supervisor sends a ward nurse to cover a different task instead.</p>}}
"""),
    ],
    "debrief": ["""
<p><strong>Why &ldquo;four each&rdquo; fails.</strong> It gives Mika a catheter she cannot manage alone and leaves Joy with no free attention for the floor. It also ignores the isolation room, which needs a nurse who can be seen from the station.</p>
<p><strong>A better assignment, by points (Toolkit #c2).</strong> Two catheters (3 + 3 = 6), the low-pressure patient (1 + 2 = 3), isolation (1 + 2 = 3), the blind patient (1 + 1 = 2), and seven stable patients (7): 21 points. Arnel takes both catheters and one stable patient (7). Kris takes the low-pressure patient, the blind patient, and two stable patients (7). Mika takes four stable fistula patients (4), with Arnel as her named resource nurse. Joy takes the isolation patient (3), because the room is beside the station and she can see the floor through its window. Twelve patients, 21 points, and the charge nurse carries the lightest load.</p>
<p><strong>Breaks (Toolkit #c3).</strong> Written on the board at 6:00: Mika at 8:00 (Kris covers), Arnel at 8:30 (Joy covers), Kris at 9:00 (Arnel covers), Joy at 9:30 (Arnel covers). None in the first or last half hour of the sessions, and never two at once. Be honest about what a break does: for those thirty minutes the covering nurse watches her own pod and a second one. That is why only one break runs at a time, why it falls in the calmer middle of the session, why the covering nurse is told each patient&rsquo;s one key risk, and why the charge nurse keeps her own load light enough to step in. Toolkit #c1 shows the worst break window in numbers.</p>
"""],
    "skills": {"title": "Building an assignment",
               "intro": "Build assignments for two synthetic twelve-patient floors, one with an orientee, and explain each choice to a facilitator.",
               "items": [
                   ("Scores each patient and explains each point.", False),
                   ("Matches catheter care and new-access needling only to nurses signed off for them.", True),
                   ("Names a resource nurse for every orientee on the board.", True),
                   ("Keeps own load at two chairs or fewer on a heavy shift, near the center of the floor.", False),
                   ("Writes staggered breaks on the board at assignment time, avoiding the first and last half hour.", True),
                   ("Checks that no break window leaves a nurse above the unit&rsquo;s limit.", True),
                   ("Re-scores and moves one patient after a simulated change.", False),
                   ("Answers a request to release a nurse with what can be released safely, and records it.", False),
               ],
               "placement": "For one week, photograph each morning&rsquo;s board (no patient names) and review the points and breaks with the head nurse."},
    "quiz": [
        ("Why weight patients by need?",
         ["To rank nurses", "To make different nursing needs visible", "To satisfy PhilHealth", "To replace judgment"], 1,
         "Points show load; judgment still decides."),
        ("An orientee without catheter sign-off is assigned a catheter patient. Best fix?",
         ["Proceed", "Pair her with a signed-off nurse for that connection", "Cancel the patient", "Let the assistant do it"], 1,
         "She learns under observation; the patient stays safe."),
        ("Which of these cannot be delegated?",
         ["Taking a weight", "Nursing judgment", "Fetching supplies", "Preparing a chair"], 1,
         "The five rights of delegation exclude nursing judgment."),
        ("When should breaks be avoided?",
         ["The middle of the session", "The first and last 30 minutes of the sessions", "Any time after 8 a.m.", "Lunch time"], 1,
         "Most low-pressure, needle, and bleeding problems cluster then."),
        ("Shifts of 12.5 hours or more were associated with:",
         ["No change", "About three times the odds of an error", "Better outcomes", "Fewer interruptions"], 1,
         "Rest protects patients as well as nurses."),
        ("On a heavy morning, the charge nurse should carry:",
         ["Four chairs", "At most two, near the center of the floor", "Only the isolation room, always", "All the catheter patients"], 1,
         "Free attention is the charge nurse&rsquo;s main tool."),
        ("Which is one of the five rights of delegation?",
         ["The right price", "The right supervision", "The right uniform", "The right shift length"], 1,
         "Task, circumstance, person, communication, supervision."),
        ("What is true of acuity tools for outpatient hemodialysis?",
         ["They are proven in trials to reduce deaths", "They help make load visible but are not outcome-tested", "DOH mandates them", "They are useless"], 1,
         "Use them for visibility, and say so honestly."),
        ("Using the module&rsquo;s example scale, a stable fistula patient who is often hypotensive scores:",
         ["1", "2", "3", "5"], 2,
         "1 for the stable patient plus 2 for frequent low pressure."),
        ("Two nurses on a four-nurse floor take their break together. What happens?",
         ["Nothing", "The other two each cover twice as many running machines", "The breaks are shorter", "The charge nurse is relieved"], 1,
         "That is how ratios quietly double."),
        ("What should the covering nurse be told?",
         ["Nothing", "Each patient&rsquo;s one key risk", "The patients&rsquo; addresses", "The next week&rsquo;s schedule"], 1,
         "&ldquo;Bed 4 drops after the second hour.&rdquo;"),
        ("&ldquo;Two years&rsquo; experience&rdquo; tells you:",
         ["Exactly which tasks she can do alone", "Little; check which high-risk tasks are signed off", "That she can precept", "That she can take charge"], 1,
         "Competence is specific to a task."),
        ("The nursing supervisor asks to borrow a nurse at 7:30. What do you do?",
         ["Send anyone", "Say what you can release safely and when, and record it", "Refuse without explanation", "Send the orientee"], 1,
         "Answer with facts from the board."),
        ("Why might the charge nurse take the isolation patient?",
         ["It is the easiest", "The room is beside the station and she can see the floor from it", "Isolation patients need no care", "To avoid the floor"], 1,
         "Placement lets her keep the floor in view."),
        ("When should breaks be planned?",
         ["When people are hungry", "At assignment time, written on the board", "After the first emergency", "By the head nurse next week"], 1,
         "Planned breaks protect cover; improvised ones break it."),
    ],
    "terms": [("Acuity", "How much nursing attention a patient is likely to need today."),
              ("Competence", "A skill performed correctly under observation and signed off."),
              ("Orientee", "A nurse in orientation who works under a named resource nurse."),
              ("Resource nurse", "The experienced nurse an orientee calls for help."),
              ("Break cover", "The nurse who watches another nurse&rsquo;s patients during her break."),
              ("Delegation", "Assigning a task to another person while keeping accountability for the patient.")],
    "readings": [("hemodialysis-complications.html", "The complications that make some patients need more nursing than others."),
                 ("hemodialysis-elderly.html", "Why older patients on dialysis need more help and closer watching.")],
    "calcs": ["calc-dialysis-charge-nurse-toolkit.html#c2", "calc-dialysis-charge-nurse-toolkit.html#c3", "calc-dialysis-shift-coverage.html"],
}

import importlib.util as _u
from pathlib import Path as _P
_s = _u.spec_from_file_location("cn_quizutil", _P(__file__).resolve().parent / "quizutil.py")
_q = _u.module_from_spec(_s); _s.loader.exec_module(_q)
MODULE["quiz"] = _q.balance(MODULE["quiz"])
