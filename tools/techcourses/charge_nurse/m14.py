# -*- coding: utf-8 -*-
"""Dialysis Charge Nurse, Module 14: Handoffs That Close the Loop. Written for this series from published sources."""

MODULE = {
    "image_alt": "Two charge nurses exchanging a handoff at the assignment board while a patient adds a comment.",
    "objectives": [
        "Give and receive a structured handoff using I-PASS.",
        "Include an action list with an owner and a time for every open item.",
        "Make a concise SBAR call to a physician and use read-back for orders.",
        "Use the bedside to check the handoff while protecting privacy.",
        "Close the board at the end of the shift so nothing is left unowned.",
    ],
    "big": """
{{plain:In a relay race, most races are lost not by slow runners but by dropped batons in the exchange zone. The outgoing runner does not let go until the incoming runner has a firm grip.}}
<p>A handoff moves responsibility, not just information. The outgoing charge nurse is still responsible until the incoming nurse has confirmed what she now owns. &ldquo;I told her&rdquo; is not the same as &ldquo;she took it.&rdquo;</p>
{{cards:Key terms for this module|I-PASS::A handoff structure: Illness severity, Patient summary, Action list, Situation awareness and contingency, Synthesis by receiver.|SBAR::A way to call for help: Situation, Background, Assessment, Recommendation.|Read-back::Repeating an order aloud to confirm it.|Synthesis::The receiver summarizing what she now owns.|Contingency::&ldquo;If this happens, do that.&rdquo;}}
""",
    "case": {"title": "&ldquo;I thought you&rsquo;d called&rdquo;", "html": """
<p>At the 11:00 change, the outgoing charge nurse, Benjie, tells the incoming charge nurse, Liza: &ldquo;Bed 3&rsquo;s potassium was high; the doctor knows.&rdquo;</p>
<p>The doctor had been told, and had asked for a repeat sample after the session. Nobody drew it. Mr. Santos in Bed 3 went home at 11:30.</p>
""", "questions": ["What was missing from the handoff?",
                  "How would a structured handoff have caught it?",
                  "What does Liza do now?"]},
    "sections": [
        ("why", "Why structure works", "Why structured handoffs work", """
<p>In a study across nine hospitals, introducing the I-PASS handoff program was associated with medical errors falling from 24.5 to 18.8 per 100 admissions, and preventable adverse events from 4.7 to 3.3.[[hn_starmer2014]] A later rollout across 32 programs was associated with a 47% fall in reported handoff-related adverse events.[[hn_starmer2023]]</p>
{{fig:cn14_baton}}
<p>These studies were of physicians in hospitals. Applying them to dialysis nursing shift changes is a reasonable inference, not a tested finding. The mechanism is the same: handoffs lose actions, not facts, and structure protects the actions.</p>
"""),
        ("ipass", "I-PASS", "I-PASS on the dialysis floor", """
{{fig:cn14_ipass}}
<div class="table-wrap"><table>
<thead><tr><th>Letter</th><th>What it means on a dialysis floor</th></tr></thead>
<tbody>
<tr><td><strong>I</strong>llness severity</td><td>Green, amber, or red, from the board</td></tr>
<tr><td><strong>P</strong>atient summary</td><td>Who, access, where the session is, the one key risk</td></tr>
<tr><td><strong>A</strong>ction list</td><td>What must be done, by whom, by when</td></tr>
<tr><td><strong>S</strong>ituation awareness and contingency</td><td>&ldquo;If the result is above 6.0 and she can&rsquo;t be reached, call the backup physician.&rdquo;</td></tr>
<tr><td><strong>S</strong>ynthesis by receiver</td><td>The incoming nurse repeats the actions and owners</td></tr>
</tbody></table></div>
<p>The action list and the synthesis are the two parts most often skipped, and the two that would have saved Mr. Santos&rsquo;s repeat potassium.</p>
"""),
        ("sbar", "SBAR calls", "SBAR for calling the physician", """
<p>SBAR is a four-part way to call: Situation, Background, Assessment, Recommendation or request. A systematic review found it associated with better communication and patient safety, with evidence of moderate quality.[[muller2018]] End every call with a read-back: &ldquo;So you want a repeat potassium after the session, and a call if it is above 6.0. I will do that.&rdquo;</p>
{{scene:The call that asked for nothing|<p>A staff nurse calls the physician on duty: &ldquo;Doc, Bed 5&rsquo;s pressure is a bit low.&rdquo; The physician asks three questions to find out what she wants. The charge nurse coaches her to call back with SBAR: &ldquo;Bed 5, Mrs. Ong, 72. Pressure fell from 140 to 96 at hour two; she&rsquo;s yawning. Fluid removal stopped, she&rsquo;s flat, saline given; now 104. I think the fluid goal is too high for today. I&rsquo;m asking whether to stop removal for the rest of the session.&rdquo; The physician answers in ten seconds.</p>}}
"""),
        ("bedside", "Bedside handover", "Bedside handover", """
<p>Handing over at the chair lets the patient correct errors and see the plan. Reviews report benefits for patient engagement and satisfaction, and concerns about privacy and time.[[cn_tobiano2018]][[cn_daicampi2025]] On an open dialysis floor, do the visual check at the chair (access, patient, machine) and keep sensitive details (results, diagnoses) for the station.</p>
"""),
        ("close", "Closing the board", "The end-of-shift close", """
<p>Walk the board with the incoming charge nurse. Every amber and red flag gets a new owner or is closed. Name unresolved results, pending orders, broken machines, and patient complaints. Do not leave until the receiver has confirmed what she owns. If the incoming nurse is late, stay and tell the head nurse.</p>
{{key:No release without a grip. Responsibility moves only when the receiver confirms.}}
"""),
    ],
    "debrief": ["""
<p><strong>What was missing.</strong> The handoff contained a fact (&ldquo;potassium high, doctor knows&rdquo;) but no action, no owner, no time, and no synthesis.</p>
<p><strong>The handoff done right.</strong> &ldquo;Bed 3, Mr. Santos, amber. Fistula, finishes at 11:20. Pre-dialysis potassium 6.3. Dr. Lim was told at 7:15; she wants a repeat sample at the end of the session and a call if it is above 6.0. Action: you draw the post-dialysis sample at 11:20 and call her with the result; Mr. Santos should not leave until it is drawn. If it is above 6.0 and she cannot be reached, call the backup physician.&rdquo; Liza: &ldquo;So I draw the sample at 11:20, he stays until it is drawn, and I call Dr. Lim with the result, or the backup.&rdquo; Benjie: &ldquo;Yes.&rdquo;</p>
<p><strong>What Liza does now.</strong> She calls Mr. Santos, arranges a repeat potassium today, tells Dr. Lim, and records a near miss. At the next huddle she proposes that every handoff at the unit include an action list.</p>
"""],
    "skills": {"title": "Handoffs and calls",
               "intro": "Give and receive two recorded I-PASS handoffs, and make two SBAR calls to a facilitator playing the physician.",
               "items": [
                   ("Gives an I-PASS handoff with an action list, owners, and times.", True),
                   ("Requires and gives a synthesis by the receiver.", True),
                   ("Includes at least one contingency statement.", False),
                   ("Makes an SBAR call that ends with a specific request.", True),
                   ("Reads back phone orders and records them.", True),
                   ("Checks the access, patient, and machine at the chair without disclosing private details.", False),
                   ("Does not leave until every open flag has a new owner.", True),
               ],
               "placement": "For one week, record each shift change: how many open items were handed over, and how many had an owner and a time."},
    "quiz": [
        ("Who does the synthesis in I-PASS?",
         ["The giver", "The receiver", "The physician", "The patient"], 1,
         "The receiver repeats what she now owns."),
        ("In the I-PASS study, errors per 100 admissions fell from:",
         ["50 to 10", "24.5 to 18.8", "5 to 4", "No change"], 1,
         "Preventable adverse events fell from 4.7 to 3.3."),
        ("Applying resident handoff data to nursing shift changes is:",
         ["Proven", "A reasonable inference", "Invalid", "Mandatory"], 1,
         "Same mechanism, untested setting."),
        ("How does an SBAR call end?",
         ["With a joke", "With a recommendation or request, then read-back", "With the patient&rsquo;s address", "In silence"], 1,
         "Ask for a decision."),
        ("What concerns do reviews of bedside handover raise?",
         ["Privacy and time", "The cost of chairs", "Dialysate", "None"], 0,
         "Do the check at the chair; keep private details for the station."),
        ("A handoff item without an owner is:",
         ["Fine", "An open loop", "Closed", "The head nurse&rsquo;s problem"], 1,
         "Owners close loops."),
        ("When is the outgoing nurse released?",
         ["When she says the words", "When the receiver confirms", "When the shift ends", "When the patient leaves"], 1,
         "No release without a grip."),
        ("What was missing in Benjie&rsquo;s handoff?",
         ["The patient&rsquo;s name", "An action, an owner, and a time", "The diagnosis", "The bed number"], 1,
         "A fact without an action."),
        ("What is a contingency statement?",
         ["A complaint", "&ldquo;If this happens, do that&rdquo;", "A billing code", "A greeting"], 1,
         "It tells the receiver what to do when things change."),
        ("A physician gives an order by phone. What do you do?",
         ["Remember it", "Read it back, write it, and have it countersigned", "Ask a colleague to remember", "Ignore it"], 1,
         "Read-back confirms the order."),
        ("The incoming charge nurse is 30 minutes late. What do you do?",
         ["Leave a note", "Stay until a handoff is complete and tell the head nurse", "Leave the keys", "Ask the assistant to hand over"], 1,
         "Responsibility does not drop to the floor."),
        ("&ldquo;Doc, the pressure is a bit low&rdquo; is weak because:",
         ["It is rude", "It gives no numbers and asks for nothing", "It is too long", "It uses SBAR"], 1,
         "SBAR makes the request clear."),
        ("Which parts of I-PASS are most often skipped?",
         ["Illness severity", "Action list and synthesis", "Patient summary", "None"], 1,
         "And they are the ones that protect actions."),
        ("A patient at the chair corrects the handoff. What do you do?",
         ["Ignore her", "Thank her and update the board", "Tell her to be quiet", "Report her"], 1,
         "Patients catch errors staff miss."),
        ("In the later rollout across 32 programs, reported handoff-related adverse events fell by about:",
         ["5%", "47%", "90%", "None"], 1,
         "Observed in a multicenter implementation study."),
    ],
    "terms": [("I-PASS", "Illness severity, Patient summary, Action list, Situation awareness and contingency, Synthesis by receiver."),
              ("SBAR", "Situation, Background, Assessment, Recommendation."),
              ("Read-back", "Repeating an order aloud to confirm it."),
              ("Synthesis", "The receiver summarizing what she now owns."),
              ("Contingency", "&ldquo;If this happens, do that.&rdquo;")],
    "readings": [("hemodialysis-transfer-guide.html", "What should travel with a patient between units and hospitals."),
                 ("dialysis-qapi-vs-cqi.html", "How units learn from near misses.")],
    "calcs": ["calc-dialysis-charge-nurse-toolkit.html#c7"],
}

import importlib.util as _u
from pathlib import Path as _P
_s = _u.spec_from_file_location("cn_quizutil", _P(__file__).resolve().parent / "quizutil.py")
_q = _u.module_from_spec(_s); _s.loader.exec_module(_q)
MODULE["quiz"] = _q.balance(MODULE["quiz"])
