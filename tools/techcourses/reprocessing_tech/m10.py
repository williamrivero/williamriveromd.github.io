# -*- coding: utf-8 -*-
"""Dialyzer Reprocessing Technician, Module 10: Disinfect, Store, Rinse and Hand Off. Merges v0.1 RT10 and RT11."""

MODULE = {
    "image_alt": "A dialysis nurse and a reprocessing technician at a patient&rsquo;s chair, reading a dialyzer label aloud against the patient&rsquo;s wristband, with a residual test strip and a timer on the tray.",
    "objectives": [
        "Explain why germicide must fill every space, stay for a minimum contact time, and be proven present.",
        "Calculate the usable window from fill time, minimum contact time and maximum storage time, all taken from the instructions for use (IFU).",
        "Store processed dialyzers so they stay identified, capped, filled and separate.",
        "Explain why rinsing and a residual test protect the patient, and read the test exactly as its instructions require.",
        "Hand off a dialyzer with two-person verification of identity, use number and test results.",
    ],
    "big": """
{{plain:Pickling vegetables needs three things: the jar must be full of brine, it must sit long enough to work, and you eat it before it goes bad. And if the brine is too salty to eat, you rinse the vegetables first and taste before serving.}}
<p>The picture has a limit. Too much salt on a vegetable only spoils the taste. Germicide left in a dialyzer goes straight into the patient&rsquo;s blood. Germicide that did not reach every corner leaves bacteria alive. So each part of the pickling idea becomes a gate with a proof: full, long enough, not too long, rinsed, and tested before the blood touches it.</p>
{{cards:Key terms for this module|Fill::Filling the blood and dialysate compartments with germicide so no air pockets remain.|Contact time::The minimum time the germicide must stay in the dialyzer to disinfect it.|Expiry::The latest time the dialyzer may be used after processing, set by the IFU and the program.|Presence test::A check that germicide is present in the filled dialyzer.|Residual test::A check after rinsing that germicide has fallen below the safe threshold.|Two-person verification::Two people independently reading the label against the patient record and confirming the results.}}
<p>The technician owns the fill, the storage and the record. The rinse and the residual test at the chair are done by whoever your program assigns, often the nurse. Either way, the patient is protected only if every gate is proven before the blood pump starts.</p>
""",
    "case": {"title": "The strip at the wrong minute", "html": """
<p>At 6:55 on a Tuesday, the nurse, Mr. Joel Ramos, is priming Mrs. Felicidad Navarro&rsquo;s reprocessed dialyzer for her 7:00 start. He finishes the rinse and dips the residual test strip. The strip instructions say to read the color at a fixed number of seconds after dipping. Busy with another alarm, he reads it after about two minutes. It shows a faint color he judges &ldquo;close enough to negative.&rdquo;</p>
<p>The reprocessing technician, Ms. Mylene Torres, brings the next dialyzer and notices the strip on the tray. The dialyzer label shows it was filled with germicide 30 hours ago; the program&rsquo;s minimum contact time is shorter than that, and its maximum storage time is longer.</p>
""", "questions": ["Is this dialyzer proven safe to connect?",
                  "What should Ms. Torres say, and to whom?",
                  "What does the storage time on the label tell you?"]},
    "sections": [
        ("fill", "Fill and contact", "Fill, contact time and proof of presence", """
<p>Germicide works only where it touches. An air pocket in a header or a partly filled dialysate compartment is a place where bacteria survive. The reprocessor or the manual procedure fills both compartments until no air remains, then caps all four ports.</p>
<p>Germicides also need time. Each product has a minimum contact time at a stated temperature, printed in its IFU and confirmed in your validated procedure. Before that time has passed, the dialyzer is not yet disinfected, even if it looks ready.</p>
<p>A presence test on each filled dialyzer, where the program requires it, proves that germicide actually went in at adequate strength. The 1988 outbreak in Module 6 is the reason: stored dialyzers held from 0.9% to 4.2% of a germicide meant to be 2.5%.[[rt_beck1990]]</p>
{{key:Full, capped, proven present, and left for at least the contact time. Until then, it is not disinfected.}}
"""),
        ("window", "The usable window", "Contact time, storage and expiry", """
{{fig:rt10_timeline}}
<p>Each processed dialyzer has a usable window. It opens when the minimum contact time has passed and closes at the maximum storage time. Both come from the germicide IFU, the dialyzer IFU and the program. Outside the window, the dialyzer is reprocessed or discarded as the procedure directs.</p>
{{formula:Earliest use = fill time + minimum contact time &nbsp;&middot;&nbsp; Expiry = fill time + maximum storage time &nbsp;&middot;&nbsp; Example for training only, with made-up IFU values: filled Monday 14:00, contact 11 h, storage 30 days &rarr; earliest use Tuesday 01:00; expiry 30 days after Monday 14:00.}}
<p>Record the fill time on the label and in the log, to the minute. A dialyzer whose fill time is missing has no window, and is held.</p>
{{stop:A dialyzer used before its contact time or after its expiry is outside the proven window. Do not release it.}}
"""),
        ("storage", "Storage", "Storage that keeps it proven", """
<div class="table-wrap"><table>
<thead><tr><th>Storage rule</th><th>Why</th></tr></thead>
<tbody>
<tr><td>Individual labeled position for each patient</td><td>Picks by label, not by location; Malaysian standards require individually labeled storage[[rt_my2026]]</td></tr>
<tr><td>Ports capped; dialyzer upright or as the procedure sets</td><td>Germicide stays in; contaminants stay out</td></tr>
<tr><td>Within the temperature range the IFU sets, away from sunlight and heat</td><td>Some germicides break down with heat and light</td></tr>
<tr><td>Separate from used dialyzers and from any dedicated hepatitis program&rsquo;s dialyzers</td><td>Clean and dirty never mix (Module 4)</td></tr>
<tr><td>Daily check for leaks, missing caps, and expiry</td><td>A leaking dialyzer has lost its germicide and its proof</td></tr>
</tbody></table></div>
"""),
        ("rinse", "Rinse and residual test", "Rinse and residual test", """
<p>Before the dialyzer meets blood, the germicide is rinsed out with the volume and method the procedure sets, usually during priming of the circuit. Then a residual test confirms that germicide has fallen below the safe threshold printed on the test kit and in the procedure. Germicide entering a patient&rsquo;s bloodstream is a chemical injury that the rinse and the residual test exist to prevent.</p>
<div class="table-wrap"><table>
<thead><tr><th>Common error</th><th>Why it matters</th></tr></thead>
<tbody>
<tr><td>Reading the strip later or earlier than its instructions say</td><td>Colors keep changing; the result no longer means anything</td></tr>
<tr><td>Using a strip for a different germicide</td><td>Each germicide needs its own test</td></tr>
<tr><td>Using expired strips or strips stored open</td><td>They may not change color</td></tr>
<tr><td>Testing at the wrong port or before the rinse is complete</td><td>The sample does not represent what reaches the blood</td></tr>
<tr><td>Judging a faint color as &ldquo;close enough&rdquo;</td><td>A doubtful result is a failed result: rinse again as the procedure allows and retest</td></tr>
</tbody></table></div>
{{key:Read the residual test at the time its instructions set. A doubtful color is not a negative.}}
"""),
        ("handoff", "Two-person handoff", "Two-person verification at the chair", """
{{fig:rt10_handoff}}
{{flow:Two-person verification|Identity::Both read the label aloud: full name and second identifier, matched to the patient&rsquo;s record and wristband or verbal confirmation.|History::Use number within the limit; processing date within the window.|Results::Volume, integrity and presence results recorded as passed.|Residual::Rinse complete; residual test read at the correct time and below threshold.|Sign::Both sign or initial the treatment record.}}
<p>Two people catch errors that one person, rushed and sure, will miss. Each must check independently; a second person who only watches the first is not a second check.</p>
{{key:If either person is unsure, the dialyzer does not connect. A new dialyzer is always an option.}}
"""),
    ],
    "debrief": ["""
<p><strong>Is the dialyzer proven safe?</strong> No. The residual strip was read at about two minutes instead of the time its instructions set, so the color means nothing, and a faint color is a doubtful result in any case. The fill time is inside the window: the contact time has passed and storage has not expired. That gate is proven. The residual gate is not.</p>
<p><strong>What should Ms. Torres say?</strong> Politely and directly, to Mr. Ramos before connection: &ldquo;The strip was read late. Can we rinse again as the procedure allows and retest at the right time?&rdquo; If he disagrees, the charge nurse decides; the dialyzer is not connected while the result is doubtful. Speaking up across roles is part of the job (Module 1).</p>
<p><strong>What does the storage time tell you?</strong> Thirty hours is after the minimum contact time and before the maximum storage, so the germicide has had time to work and the dialyzer is within its window. Had it been filled only two hours earlier, it would not yet be disinfected.</p>
"""],
    "skills": {"title": "Storage, residual testing and handoff",
               "intro": "Practice on training dialyzers filled with water, then observe and perform under supervision.",
               "items": [
                   ("Checks that both compartments are full, without air, and all four ports are capped.", True),
                   ("Records the fill time to the minute on the label and in the log.", True),
                   ("Calculates the earliest-use time and expiry from IFU values.", True),
                   ("Places the dialyzer in the patient&rsquo;s labeled position and performs the daily storage check.", False),
                   ("Uses the correct, in-date residual strip for the germicide.", True),
                   ("Reads the residual test at the exact time its instructions set.", True),
                   ("Treats a doubtful color as a failed result.", True),
                   ("Completes a two-person verification, each person checking independently.", True),
               ],
               "placement": "Take part in at least two observed two-person handoffs at the chair, and log each with your assessor."},
    "quiz": [
        ("Why must there be no air pockets after filling with germicide?",
         ["Air makes the dialyzer heavier", "Germicide works only where it touches; air pockets shelter bacteria", "Air damages the label", "Air raises the TCV"], 1,
         "Contact is required for disinfection."),
        ("A dialyzer was filled two hours ago. The IFU minimum contact time is longer than that. May it be used now?",
         ["Yes, if it looks clean", "No; it is not yet disinfected", "Yes, if the residual test is negative", "Yes, if the nurse agrees"], 1,
         "The window opens only after the contact time."),
        ("Filled Monday 14:00, minimum contact 11 h (training values). What is the earliest use?",
         ["Monday 22:00", "Tuesday 01:00", "Tuesday 14:00", "Wednesday 01:00"], 1,
         "14:00 + 11 h = 01:00 the next day."),
        ("A dialyzer&rsquo;s fill time is missing from its label and log. What do you do?",
         ["Estimate it", "Hold it; without a fill time it has no proven window", "Release it after a long rinse", "Assume it was filled yesterday"], 1,
         "No fill time, no window."),
        ("The residual strip is read two minutes late. What does the result mean?",
         ["It is still valid", "Nothing; colors keep changing, so rinse as allowed and retest at the right time", "It is positive", "It is more accurate"], 1,
         "Timing is part of the test."),
        ("A residual strip shows a faint color. What is the correct interpretation?",
         ["Negative", "Doubtful, treated as failed: rinse again as allowed and retest", "Positive but acceptable", "Ignore it"], 1,
         "Doubt is not a negative."),
        ("Which strip should be used for a dialyzer disinfected with a peracetic acid mixture?",
         ["Any residual strip", "The strip validated for that germicide", "A pH strip", "A water hardness strip"], 1,
         "Each germicide needs its own test."),
        ("What makes a second person a real second check?",
         ["Watching the first person", "Checking independently, reading the label and results themselves", "Signing without looking", "Being senior"], 1,
         "Independent verification catches what one person misses."),
        ("A stored dialyzer is found with a missing cap and a damp shelf. What do you do?",
         ["Replace the cap and release it", "Treat it as having lost its germicide and proof; reprocess or discard per procedure", "Add more germicide by hand", "Release it after rinsing"], 1,
         "Leakage breaks the proof of disinfection."),
        ("Why are processed dialyzers stored in individual labeled positions?",
         ["To look neat", "So they are picked by label, not location, and stay identified", "To save space", "Because of the germicide"], 1,
         "Storage protects identity."),
        ("What is the purpose of the rinse before treatment?",
         ["To cool the dialyzer", "To remove germicide before blood touches the membrane", "To raise the TCV", "To test integrity"], 1,
         "Germicide in the blood is a chemical injury."),
        ("During handoff, the nurse and technician disagree about whether a result is acceptable. What happens?",
         ["The senior person decides alone", "The dialyzer is not connected; the charge nurse decides, and a new dialyzer is an option", "They flip a coin", "The patient decides"], 1,
         "Doubt stops connection."),
    ],
    "terms": [("Fill", "Filling both compartments with germicide so no air remains."),
              ("Contact time", "The minimum time germicide must remain to disinfect."),
              ("Expiry", "The latest time a processed dialyzer may be used."),
              ("Presence test", "A check that germicide is present after filling."),
              ("Residual test", "A check after rinsing that germicide is below the safe threshold."),
              ("Priming", "Filling the blood circuit with saline before connecting the patient."),
              ("Two-person verification", "Two people independently confirming identity and results.")],
    "readings": [("dialyzer-reprocessing-reuse.html", "Storage, rinsing and residual testing.")],
    "calcs": ["calc-reprocessing-technician-toolkit.html#c4"],
}


# Spread the keyed answers across positions A to D.
import importlib.util as _u
from pathlib import Path as _P
_s = _u.spec_from_file_location("rt_quizutil", _P(__file__).resolve().parent / "quizutil.py")
_q = _u.module_from_spec(_s); _s.loader.exec_module(_q)
MODULE["quiz"] = _q.balance(MODULE["quiz"])
