# -*- coding: utf-8 -*-
"""Dialyzer Reprocessing Technician, Module 08: Receiving, Rinsing and Cleaning. v0.1 RT08."""

MODULE = {
    "image_alt": "A reprocessing technician connecting a used dialyzer to an automated reprocessor, with a refrigerator of waiting dialyzers and a temperature log beside it.",
    "objectives": [
        "Receive a used dialyzer: check identity and eligibility, record the time, and decide whether it can be processed.",
        "Explain why time and temperature before processing matter, and follow the procedure for a dialyzer that waited too long.",
        "Explain rinsing, reverse ultrafiltration and header cleaning in terms of what they remove from the fibers.",
        "Describe what cleaning agents do to the membrane, and why only the approved agent and sequence are used.",
        "Follow the approved procedure step by step and document each step.",
    ],
    "big": """
{{plain:Washing a pot right after cooking is easy. Leave it overnight and the food dries on, and you scrub for twenty minutes and still miss some. Leave it in the sun and it starts to smell.}}
<p>The picture has a limit. Food on a pot is visible, and you can scrub it. Blood and protein left inside ten thousand fibers cannot be seen or scrubbed; they can only be rinsed and lifted out by water and cleaning agents moving through the right paths. Bacteria in that residue multiply with time and warmth. So the clock starts at the end of treatment, and the cleaning follows a method that has been shown to work on this dialyzer model.</p>
{{cards:Key terms for this module|Receiving::Accepting a used dialyzer into the reuse room, with identity, eligibility and time checked.|Header::The cap at each end of the dialyzer where blood enters or leaves the fibers.|Rinse::Flushing water through the blood compartment to remove blood.|Reverse ultrafiltration::Pushing water from the dialysate side into the fibers to lift deposits from the inner wall.|Cleaning agent::A chemical used before disinfection to remove protein and blood residue.|Validated procedure::A method shown, for this dialyzer and reprocessor, to achieve the result it claims.}}
<p>Your work is to start the cleaning in time, follow the validated steps exactly, and stop when a dialyzer cannot be cleaned within what the procedure allows.</p>
""",
    "case": {"title": "Three hours in the hallway", "html": """
<p>At 3:15 on a Wednesday afternoon, Ms. Nina Aquino finds a used dialyzer in a tray on a cart in the hallway outside the reuse room. Its label is clear, and the patient is eligible. The run sheet shows the treatment ended at 12:05. The hallway is warm. The refrigerator in the reuse room has space, and its temperature log was last signed at 7:00.</p>
<p>The dialyzer is on its third use. The patient is a 70-year-old woman whose new dialyzer would cost the unit another one from its yearly allowance.</p>
""", "questions": ["What is the problem with this dialyzer?",
                  "What does the procedure probably require, and who decides?",
                  "How can the unit stop it happening again?"]},
    "sections": [
        ("receiving", "Receiving", "Receiving a used dialyzer", """
{{fig:reuse_steps}}
<p>Receiving is the first gate inside the room. A dialyzer that fails it is not processed.</p>
<div class="table-wrap"><table>
<thead><tr><th>Check</th><th>Pass</th><th>Hold or reject</th></tr></thead>
<tbody>
<tr><td>Identity</td><td>Label readable, matches the receiving log</td><td>Missing, unreadable or mismatched label</td></tr>
<tr><td>Eligibility</td><td>Patient on the current eligibility list</td><td>Not listed, status changed, or unknown</td></tr>
<tr><td>Use count</td><td>Next use within the limit</td><td>Limit reached</td></tr>
<tr><td>Time since end of treatment</td><td>Within the limit your procedure sets, or refrigerated within it</td><td>Over the limit without refrigeration</td></tr>
<tr><td>Condition</td><td>Housing intact, ports capped</td><td>Cracks, leaks, gross clot, unusual color</td></tr>
</tbody></table></div>
{{key:Receiving is a gate, not a drop-off. Record the time the dialyzer arrived and what you checked.}}
"""),
        ("time", "Time and temperature", "Time and temperature before processing", """
{{fig:rt08_clock}}
<p>After treatment, the fibers hold blood, protein and whatever bacteria entered the circuit. At room temperature, bacteria multiply; dried protein sticks to the membrane. Both make cleaning less effective and raise endotoxin. That is why programs set a maximum time to processing and require refrigeration for dialyzers that will wait longer. The exact time and temperature come from your procedure, which follows the AAMI standard and the reprocessor maker.[[aami_reuse]]</p>
<p>The refrigerator is part of the system. A refrigerator for used dialyzers holds only used dialyzers, never food or medicines, and its temperature is logged. The United States Food and Drug Administration (FDA) advises that dialyzers should not be reused when reprocessing or required refrigeration facilities are not working.[[rt_fda_restart]]</p>
{{stop:A used dialyzer that has passed the time limit without refrigeration is not processed. Follow the procedure, usually discard, and report how it happened.}}
"""),
        ("cleaning", "Rinsing and cleaning", "Rinsing, reverse ultrafiltration and the headers", """
{{fig:rt08_cleaning}}
<p>Cleaning works from the outside in. First, water flushes the blood out of the blood compartment. Then reverse ultrafiltration pushes water backward through the membrane, from the dialysate side into the fibers, lifting protein and small clots off the inner wall. A cleaning agent, if the program uses one, dissolves what remains. Last, the headers are cleaned, because clot often collects there where blood enters the fibers.</p>
<div class="table-wrap"><table>
<thead><tr><th>Step</th><th>What it removes</th><th>Common error</th></tr></thead>
<tbody>
<tr><td>Initial rinse</td><td>Loose blood</td><td>Starting with a warm, dried dialyzer</td></tr>
<tr><td>Reverse ultrafiltration</td><td>Protein and small clots on the inner fiber wall</td><td>Pressure outside the reprocessor&rsquo;s set range</td></tr>
<tr><td>Cleaning agent</td><td>Remaining protein</td><td>Wrong agent, wrong strength, or skipped rinse afterward</td></tr>
<tr><td>Header cleaning</td><td>Clot at the fiber openings</td><td>Removing the header without authorization or damaging the O-ring; splash to the face</td></tr>
</tbody></table></div>
<p>Header removal and cleaning carry a splash risk, so the face shield stays down (Module 4). Some dialyzer models must not have their headers removed; the IFU says which.</p>
{{key:Rinse before the residue dries. Clean in the order the procedure sets. A step skipped is a step unproven.}}
"""),
        ("agents", "Cleaning agents and the membrane", "What cleaning agents do to the membrane", """
<p>Cleaning agents are chosen for a dialyzer model by the program. They can change the membrane itself. In the HEMO analysis, the clearance of beta-2-microglobulin with reuse depended on both the membrane material and the reprocessing technique; with some combinations it fell, and with others it rose substantially.[[rt_cheung1999]] A membrane that becomes more open can lose more albumin into the dialysis fluid. This is why a program cannot swap one agent for another, or add an extra cleaning step, without validation and the medical director&rsquo;s approval.</p>
<p>Agents must also be compatible with the germicide that follows. Some combinations react dangerously; Module 6 explains why bleach must never meet acid germicides outside a validated sequence.</p>
{{key:A stronger clean is not a better clean. Use only the agent, strength and sequence your validated procedure names.}}
"""),
        ("procedure", "The approved procedure", "Following the approved procedure", """
<p>This module describes the logic of cleaning. The steps you perform come from your unit&rsquo;s approved procedure, written for its own reprocessor, dialyzer models and agents. This track does not publish a recipe, because a recipe that works for one system can fail on another.</p>
{{cards:Before you start a processing run|Procedure::Current version at hand, signed by the medical director.|Reprocessor::Daily checks and calibration recorded (Module 11).|Water::Log reviewed, no unsigned failures (Module 5).|Agents and germicide::Correct products, in date, batch potency recorded (Module 6).|Dialyzer::Received, identified, eligible, within time (this module).}}
{{stop:If any start-of-run check is missing, do not start. A run that begins on an unproven system makes every dialyzer in it unproven.}}
"""),
    ],
    "debrief": ["""
<p><strong>What is the problem?</strong> The dialyzer has waited more than three hours at warm room temperature since the end of treatment. Bacteria may have multiplied and protein may have dried onto the membrane. Unless your procedure allows that time without refrigeration, it is outside the limit.</p>
<p><strong>What does the procedure require?</strong> Usually that such a dialyzer is not processed and is discarded, with a record. The decision follows the written procedure; if it is unclear, the head nurse or medical director&rsquo;s designate decides. The cost of one dialyzer and the yearly allowance do not change the safety decision; Module 3 explained that a payer allowance never justifies using a doubtful dialyzer.</p>
<p><strong>How can the unit prevent it?</strong> A rule that used dialyzers go straight to the reuse room or its refrigerator, a log of time received, a hallway cart that is never a parking place, and a shift hand-over that includes the reuse room. Ms. Aquino reports the event so the cause can be fixed without blame.</p>
"""],
    "skills": {"title": "Receiving and cleaning on a training dialyzer",
               "intro": "Practice receiving and the cleaning steps on training dialyzers and the unit&rsquo;s reprocessor under supervision.",
               "items": [
                   ("Checks identity, eligibility, use count, time since treatment and condition at receiving, and records the time.", True),
                   ("Rejects a dialyzer outside the time limit and follows the procedure.", True),
                   ("Confirms the start-of-run checks before starting the reprocessor.", True),
                   ("Performs the rinse and reverse ultrafiltration steps as the procedure sets.", True),
                   ("Cleans the header with the face shield down and without damaging seals, only if the IFU permits.", True),
                   ("Uses only the approved cleaning agent at the approved strength.", True),
                   ("Records each step as it is done, not afterward.", False),
                   ("Checks and records the used-dialyzer refrigerator temperature.", False),
               ],
               "placement": "For one week, record the time from end of treatment to receiving for every dialyzer. Show your preceptor the longest five and their causes."},
    "quiz": [
        ("Why does time before processing matter?",
         ["It does not matter if the dialyzer is refrigerated later", "Bacteria multiply and protein dries onto the membrane with time and warmth", "The label fades", "The patient may change shift"], 1,
         "Residue and bacteria make cleaning less effective and raise endotoxin."),
        ("Where do the maximum time to processing and the refrigeration rules come from?",
         ["The payer circular", "Your procedure, following the AAMI standard and the reprocessor maker", "The technician&rsquo;s judgment", "The patient"], 1,
         "No number on this page is a working limit."),
        ("What does reverse ultrafiltration do?",
         ["Pushes water from the dialysate side into the fibers to lift deposits from the inner wall", "Measures total cell volume", "Fills the dialyzer with germicide", "Tests for leaks"], 0,
         "It cleans the inside of the fibers by backflow."),
        ("Where does clot often collect in a used dialyzer?",
         ["In the dialysate ports", "In the headers, at the fiber openings", "In the label", "In the housing wall"], 1,
         "Blood enters the fibers at the headers."),
        ("A dialyzer has been in a warm hallway for three hours. Your procedure&rsquo;s limit is shorter. What do you do?",
         ["Process it with an extra rinse", "Follow the procedure, usually discard, and report how it happened", "Refrigerate it now and process tomorrow", "Ask the patient"], 1,
         "A dialyzer outside the time limit is not processed."),
        ("What may a different cleaning agent do to a membrane?",
         ["Nothing", "Change its pores, so middle-molecule clearance and albumin loss change", "Only change its color", "Make the label fade"], 1,
         "The HEMO data showed that technique changes membrane behavior."),
        ("A colleague suggests adding an extra bleach step to get dialyzers cleaner. What is the correct response?",
         ["Agree, cleaner is safer", "Decline; only validated agents and sequences approved by the medical director are used", "Try it on one patient", "Use it only on clotted dialyzers"], 1,
         "A stronger clean is not a better clean."),
        ("What may be stored in the used-dialyzer refrigerator?",
         ["Used dialyzers only", "Used dialyzers and staff lunches", "Medicines", "Clean dialyzers"], 0,
         "Mixing food, medicines or clean items invites contamination."),
        ("According to the FDA, what should happen when reprocessing or required refrigeration is not working?",
         ["Reuse continues as usual", "Dialyzers should not be reused", "Dialyzers are stored at room temperature", "Germicide strength is doubled"], 1,
         "Without functioning facilities, reuse stops."),
        ("Which check must be done before starting a processing run?",
         ["Only that the room is clean", "Procedure, reprocessor checks, water log, products and dialyzer receiving", "Only the water log", "Nothing; checks are done after"], 1,
         "A run on an unproven system makes every dialyzer in it unproven."),
        ("When should each cleaning step be recorded?",
         ["At the end of the day", "As it is done", "Only if it fails", "Weekly"], 1,
         "Records made later from memory are not evidence."),
        ("The IFU for a dialyzer model says the headers must not be removed. What do you do?",
         ["Remove them carefully", "Do not remove them; follow the IFU", "Remove only one", "Ask a colleague to remove them"], 1,
         "The IFU sets what is allowed for that model."),
    ],
    "terms": [("Receiving", "Accepting a used dialyzer into the reuse room after checks."),
              ("Header", "The cap at each end of the dialyzer where blood enters or leaves the fibers."),
              ("Reverse ultrafiltration", "Pushing water from the dialysate side into the fibers to clean them."),
              ("Cleaning agent", "A chemical that removes protein and blood residue before disinfection."),
              ("Validated procedure", "A method shown to achieve its claimed result on that system."),
              ("O-ring", "A rubber seal between the header and the dialyzer body.")],
    "readings": [("dialyzer-reprocessing-reuse.html", "The reprocessing steps in more detail.")],
    "calcs": [],
}


# Spread the keyed answers across positions A to D.
import importlib.util as _u
from pathlib import Path as _P
_s = _u.spec_from_file_location("rt_quizutil", _P(__file__).resolve().parent / "quizutil.py")
_q = _u.module_from_spec(_s); _s.loader.exec_module(_q)
MODULE["quiz"] = _q.balance(MODULE["quiz"])
