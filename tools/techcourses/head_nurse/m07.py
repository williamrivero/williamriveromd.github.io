# -*- coding: utf-8 -*-
"""Dialysis Head Nurse, Module 07: Leading the First Minutes of an Emergency. Written for this series from published sources."""

MODULE = {
    "image_alt": "A head nurse directing a small team at one dialysis chair during an emergency while another nurse watches the other patients.",
    "objectives": [
        "Decide whether the circuit is the cause of an emergency or a bystander.",
        "State the events in which blood in the circuit must not be returned.",
        "Explain why some dialysis patients cannot hold their blood pressure, and what that means at the chair.",
        "Assign five named roles in the first thirty seconds and close each loop.",
        "Summarize what is known about cardiac arrest in dialysis clinics, and why compressions matter more than the shock.",
        "Deliver a structured transfer handoff and a short debrief.",
    ],
    "big": """
{{plain:An emergency in a dialysis unit involves two patients at once: the person, and the circuit holding about a quarter liter of their blood. Every dialysis emergency starts with the same question. Is the circuit the cause, or is it a bystander?}}
<p>The picture has a limit. Sometimes you cannot tell at first. When you are unsure, treat the circuit as a possible cause: stop the pump and clamp. Returning blood can wait a minute. Undoing a return cannot.</p>
{{fig:hn07_fork}}
{{cards:Key terms for this module|Cause or bystander::Whether the circuit produced the emergency (air, hemolysis, a reaction) or the patient did (low pressure, a heart problem).|Blood return::Rinsing the blood in the circuit back to the patient at the end of treatment.|Closed-loop communication::A named instruction, repeated back, and reported when done.|Nonshockable rhythm::A cardiac arrest rhythm that a defibrillator will not shock. Compressions are the treatment.|Dialyzer reaction::An allergic-type reaction to the dialyzer or tubing, usually in the first minutes.|SBAR::Situation, Background, Assessment, Recommendation.}}
""",
    "case": {"title": "Station 7 goes quiet", "html": """
<p>At 9:40, during the morning shift, Mr. Benjamin Torres, 71, stops responding at station 7. He is in his third hour. His nurse, Ms. Rhea Castillo, shouts, and four nurses and the technician run to the chair. Eleven other patients are connected. At station 2, a machine begins to alarm.</p>
<p>The physician on duty, Dr. Paolo Lim, is at the far end of the unit examining a new patient.</p>
""", "questions": ["What do you say in the first thirty seconds?",
                  "What happens to the blood in Mr. Torres&rsquo;s circuit?",
                  "What do you hand over when the transfer team arrives, and what happens afterward?"]},
    "sections": [
        ("physiology", "Why patients fall", "Why some patients fall further", """
<p>Module 2 explained that fluid removal can outrun refilling. A healthy body compensates by tightening its vessels and speeding the heart. Many dialysis patients cannot. Diabetic nerve damage stops the vessels tightening. A thick, stiff heart needs full filling to pump. Blood pressure tablets taken that morning blunt both responses.</p>
{{fig:hn07_compensate}}
<p>A nadir systolic below 90 mm Hg is the level most strongly linked to mortality in observational data.[[hn_flythe2015]] A low pressure that does not improve after stopping fluid removal and laying the patient flat is something else until proven otherwise: a heart attack, an arrhythmia, bleeding, infection, or fluid around the heart.</p>
<p>Cardiac arrest is the most common cause of death in patients on hemodialysis.[[hn_pun2007]] Risk peaks after the long gap.[[hn_foley2011]] In a case-control study of in-clinic arrests, low-potassium dialysis fluid was among the factors associated with arrest.[[hn_pun2011]]</p>
{{scene:The low pressure that did not come back|<p>Mrs. Corazon Medina, 64, has diabetes and dialyzes on the morning shift. At two and a half hours, her systolic pressure is 82 mm Hg. Her nurse stops fluid removal, lays her flat, and raises her legs. Ten minutes later the pressure is still 80. Mrs. Medina is sweating, and when asked, she says her jaw aches.</p>
<p>A drop caused by fluid removal usually improves when removal stops and the patient lies flat, because refilling catches up. This one did not. That is the signal to think beyond fluid. Her nurse calls the physician on duty at once and says, &ldquo;Low pressure not responding to stopping UF, sweating, and jaw pain. I am worried about her heart.&rdquo; The physician orders an electrocardiogram under the unit&rsquo;s protocol. The nurse&rsquo;s job was not to diagnose a heart attack. It was to notice that the usual explanation no longer fit, and to say so in words that got the physician to the chair.</p>}}
"""),
        ("table", "The fork", "Cause or bystander, event by event", """
<p>Actions follow your unit&rsquo;s algorithm and the physician&rsquo;s direction. This table teaches the reasoning behind them.[[hn_greenberg2021]]</p>
<div class="table-wrap"><table>
<thead><tr><th>Event</th><th>Clues</th><th>Return blood?</th><th>First actions</th></tr></thead>
<tbody>
<tr><td>Low pressure from fluid removal</td><td>Gradual fall, cramps, yawning, nausea, late in the session</td><td>Yes, if stopping, on order</td><td>Stop UF. Lay flat, legs raised. Fluid as the protocol allows. Reassess in minutes</td></tr>
<tr><td>Cardiac arrest</td><td>Unresponsive, not breathing normally</td><td>Per protocol. Never delay compressions for it</td><td>Call for help, start compressions, defibrillator pads on</td></tr>
<tr><td>Chest pain</td><td>Pressure, sweating, breathlessness</td><td>Usually, on order</td><td>Stop UF, slow the pump, ECG, call the physician</td></tr>
<tr><td>Air embolism</td><td>Air in the venous line, sudden cough, chest pain, collapse</td><td><strong>No</strong></td><td>Clamp the venous line, stop the pump. Left side down, head down. Oxygen</td></tr>
<tr><td>Hemolysis</td><td>Dark or cherry-red venous blood, chest or back pain, often several patients</td><td><strong>No</strong></td><td>Stop, clamp. Call the water lead (Module 6)</td></tr>
<tr><td>Severe dialyzer reaction</td><td>First minutes: itching, wheeze, swelling, low pressure</td><td><strong>No</strong></td><td>Stop, clamp. Treat as anaphylaxis on order</td></tr>
<tr><td>Needle out or access bleeding</td><td>Blood, pallor</td><td>Not through a contaminated needle</td><td>Stop, clamp, press (Module 4)</td></tr>
<tr><td>Seizure or sudden confusion</td><td>New patient with very high urea suggests disequilibrium. Otherwise think of sugar, stroke, pressure</td><td>On order</td><td>Protect the airway, check glucose, stop or slow, call</td></tr>
</tbody></table></div>
<p>The left-side-down position in air embolism is meant to hold the air in the right side of the heart, away from the outflow to the lungs. It comes from physiology and expert advice, not trials.</p>
{{scene:Two patients and the color of the line|<p>Twenty minutes into the second shift, the patient at station 5 says his chest feels tight and his back hurts. At station 6, a patient complains of the same thing a minute later. The nurse looks at the venous line on both machines. The blood in the lines looks darker and clearer than usual, like red wine.</p>
<p>Two patients on the same water system, with the same symptoms at the same time, and blood that looks hemolyzed, point to the fluid, not the patients. The nurses stop both blood pumps and clamp the lines. They do not return the blood, because returning hemolyzed blood would deliver the potassium released from the broken red cells straight into the patient. The physician is called, every other connection on that water system is held, and the water lead is called to test the system (Module 6).</p>}}
{{call:Stop the blood pump, clamp the lines, and do not return the blood when air, hemolysis, or a severe dialyzer reaction is suspected. Call the physician on duty and the attending nephrologist at once. Follow your unit&rsquo;s protocol while you call.}}
"""),
        ("arrest", "Cardiac arrest", "What the evidence shows about arrests in dialysis clinics", """
<div class="table-wrap"><table>
<thead><tr><th>Study</th><th>Finding</th><th>Strength and limits</th></tr></thead>
<tbody>
<tr><td>398 arrests in United States clinics</td><td>Staff started CPR in 81.4% and applied a defibrillator before the ambulance came in 52.3%. Staff-started CPR was associated with three times the odds of leaving hospital alive. The first rhythm was nonshockable in 66%[[hn_pun2019]]</td><td>Observational. Arrests where staff acted may differ from those where they did not</td></tr>
<tr><td>729 arrests in an earlier series</td><td>42.5% were alive at 24 hours, 11% at six months[[hn_pun2007]]</td><td>Observational</td></tr>
<tr><td>Clinics with and without a defibrillator</td><td>The early cohort did not find better survival in clinics that had one on site[[hn_lehrich2007]]</td><td>Observational. Result consistent with mostly nonshockable rhythms</td></tr>
<tr><td>102 arrests attended by paramedics</td><td>10 happened before, 72 during, and 20 after dialysis[[hn_davis2008]]</td><td>Observational, older series</td></tr>
</tbody></table></div>
<p>Two lessons follow. Staff compressions are the intervention that matters most. And a defibrillator will often advise no shock, so the team must keep compressing. The device does not replace the hands.</p>
<p>Use the survival figures to motivate prevention and honest conversations about goals of care with the nephrologist and family, not to discourage resuscitation.</p>
"""),
        ("voices", "Five voices", "Five voices in the first thirty seconds", """
<p>In the first thirty seconds, say the emergency aloud and give five jobs to five named people.</p>
{{fig:hn07_voices}}
{{cards:Five voices|Patient::Airway, breathing, compressions.|Circuit::Pump, clamps, and the return-or-not decision under protocol.|Caller::Physician and emergency response, then reports back: &ldquo;Called. Team in four minutes.&rdquo;|Recorder::Times, rhythms, drugs, who did what.|Floor::One nurse watches every other connected patient. Other alarms do not stop.}}
<p>&ldquo;Somebody call the doctor&rdquo; is not an assignment. &ldquo;Ana, call Dr. Lim and tell me when you have reached him&rdquo; is. A name and a report back are what closed-loop communication means.</p>
<p>Structured handoff programs were associated with 23% fewer medical errors and 30% fewer preventable adverse events among hospital residents.[[hn_starmer2014]] Applying that to dialysis transfers is a reasonable inference, not a tested finding.</p>
{{flow:Transfer handoff|Identity::Name, age, unit, attending nephrologist.|Event::What happened and when.|Treatment::Time on dialysis, fluid removed, whether blood was returned, estimated blood loss.|Status::Observations, rhythm, drugs given, access.|Results::Last potassium and other recent results.|Accepted by::The name of the person who accepted the patient, and who will call the family.}}
"""),
        ("after", "Afterward", "After the emergency", """
<p>Spend ten minutes on a debrief: what happened, what went well, what to change, and how everyone is. Restock and reseal the emergency cart before the station is used again. Deeper review goes to Module 11.</p>
<p>Time every drill: seconds from collapse to first compression, to the call made, and to pads on. Plot the drills on a run chart (Module 11) so the team can see whether practice is making them faster.</p>
{{scene:From 74 seconds to 31|<p>In January, the unit&rsquo;s first timed drill shows 74 seconds from the call &ldquo;No response at station 3&rdquo; to the first chest compression. The nurses spent the time lowering the chair, finding the backboard, and deciding who would start.</p>
<p>After the debrief, the backboard is clipped to the side of the emergency cart, the chair&rsquo;s flat button is marked in red, and the first nurse at the chair is told that her job is compressions, not the circuit. The drills are repeated monthly with different nurses and plotted on a run chart. By April, the time is 31 seconds. No single change did it. The team did, by practicing and measuring.</p>}}
{{key:In an emergency, the head nurse&rsquo;s first job is often not at the chest. It is making sure that every job has a name and that the other eleven patients are watched.}}
"""),
    ],
    "debrief": ["""
<p><strong>The first thirty seconds.</strong> Seven people at one chair and no one watching eleven circuits is the danger here. Say it: &ldquo;Station 7, unresponsive. Rhea, check breathing and start compressions if he is not breathing normally. Leo, circuit: stop the pump and clamp. Ana, call Dr. Lim and the emergency team and tell me when they are coming. Joy, record. Mark, the floor: go to station 2 now and watch everyone else.&rdquo; The defibrillator goes on. If it advises no shock, compressions continue.</p>
<p><strong>The blood.</strong> Mr. Torres&rsquo;s circuit is a bystander unless something suggests otherwise: there is no air in the line, no dark blood, and he is three hours in, not three minutes. Whether to return the blood follows your protocol and Dr. Lim&rsquo;s direction. It never delays compressions. If anything suggests air or hemolysis, do not return it.</p>
<p><strong>Handoff and afterward.</strong> Give the transfer team his identity, the time he collapsed, time on dialysis, fluid removed, whether blood was returned, rhythms, drugs, and his last potassium. Write down the name of the person who accepted him and who will call his family. Then debrief for ten minutes, restock the cart, and check on Ms. Castillo, who found him.</p>
"""],
    "skills": {"title": "Emergency team leadership",
               "intro": "Lead a simulated emergency at a dialysis chair while your facilitator observes. Repeat with two patients deteriorating at once.",
               "items": [
                   ("Names the emergency aloud within the first few seconds.", True),
                   ("Assigns patient, circuit, caller, recorder, and floor roles to named people.", True),
                   ("Asks for and receives a report back from the caller.", True),
                   ("Ensures compressions start without delay when indicated.", True),
                   ("States whether the circuit is a cause or a bystander, and the blood-return rule.", True),
                   ("Keeps one nurse on the rest of the floor throughout.", True),
                   ("Continues compressions after a no-shock advisory.", True),
                   ("Gives a structured transfer handoff, including blood return and estimated loss.", False),
                   ("Records the name of the person who accepted the patient.", False),
                   ("Leads a ten-minute debrief and arranges cart restocking.", False),
               ],
               "placement": "Run one emergency drill a month for three months. Time collapse to compressions, to call, and to pads on. Plot the results and review them with the team."},
    "quiz": [
        ("What is the first question in any dialysis emergency?",
         ["Who is the attending nephrologist?", "Is the circuit the cause or a bystander?", "What is the potassium?", "Has the family been called?"], 1,
         "The answer decides whether blood may be returned."),
        ("In which events is blood not returned?",
         ["Low pressure from fluid removal", "Air embolism, hemolysis, and severe dialyzer reaction", "Chest pain", "Cramps"], 1,
         "In these, the circuit is the cause."),
        ("A defibrillator advises &ldquo;no shock&rdquo; during an in-clinic arrest. What next?",
         ["Stop resuscitation", "Continue compressions per algorithm", "Return blood and wait", "Remove the pads"], 1,
         "Two thirds of in-clinic arrests were nonshockable."),
        ("What was staff-started CPR associated with?",
         ["No change in survival", "About three times the odds of leaving hospital alive", "Worse neurological outcome", "More bleeding"], 1,
         "The study was observational, but no stronger evidence is likely."),
        ("Air is seen in the venous line and the patient coughs. What position is taught?",
         ["Sitting upright", "Left side down, head down", "Right side down, head up", "Prone"], 1,
         "It keeps air in the right heart away from the lung outflow."),
        ("Why does &ldquo;somebody call the doctor&rdquo; fail?",
         ["It is rude", "No one owns the task, so no one confirms it was done", "Doctors dislike it", "It is too long"], 1,
         "A name plus a report back closes the loop."),
        ("Why must one nurse watch the rest of the floor during an emergency?",
         ["To keep visitors away", "Other connected patients still need monitoring and alarms continue", "To answer the phone", "To prepare the transfer form"], 1,
         "An emergency at one chair does not stop the risks at the others."),
        ("Pressure stays low five minutes after stopping UF, lying flat, and giving fluid. What has changed?",
         ["Nothing", "The working diagnosis. Look for a heart, bleeding, infection, or pericardial cause", "The patient needs more UF", "The dry weight is too high"], 1,
         "Failure to recover is a warning sign in itself."),
        ("Why can some dialysis patients not hold their pressure during fluid removal?",
         ["They drink too little", "Nerve damage, a stiff heart, and morning blood pressure tablets blunt their defenses", "The machine is faulty", "Their potassium is low"], 1,
         "Compensation depends on vessel tightening and the heart&rsquo;s response."),
        ("A patient becomes itchy and wheezy ten minutes into a session, and pressure falls. What happens to the blood?",
         ["Return it quickly", "Do not return it. Stop and clamp", "Return it slowly", "Continue dialysis"], 1,
         "Early onset with itching and wheeze suggests a dialyzer reaction."),
        ("Which dialysis fluid factor was associated with in-clinic arrest in a case-control study?",
         ["High sodium", "Low potassium", "Warm temperature", "High calcium"], 1,
         "Low-potassium fluid was among the associated factors."),
        ("What must the transfer handoff include that is specific to dialysis?",
         ["The patient&rsquo;s religion", "Whether blood was returned, fluid removed, and estimated blood loss", "The machine brand", "The PhilHealth number"], 1,
         "The receiving team needs to know the volume state."),
        ("Does a defibrillator on site guarantee better survival?",
         ["Yes, always", "Not by itself. The early cohort found no survival advantage, consistent with mostly nonshockable rhythms", "It doubles survival", "It replaces compressions"], 1,
         "Compressions remain the core intervention."),
        ("What did the structured handoff program show in hospital residents?",
         ["No change", "23% fewer medical errors", "More delays", "Higher costs only"], 1,
         "Applying this to dialysis transfers is an inference."),
        ("What should happen after the emergency?",
         ["Return to work immediately", "A short debrief, cart restocking, and checking on staff", "Only an incident report", "Nothing until the next day"], 1,
         "The station is not ready until the cart is restocked."),
    ],
    "terms": [("Blood return", "Rinsing the blood in the circuit back to the patient."),
              ("Air embolism", "Air entering the bloodstream through the circuit."),
              ("Hemolysis", "Breakdown of red blood cells."),
              ("Dialyzer reaction", "An allergic-type reaction to the dialyzer or tubing."),
              ("Disequilibrium", "Brain swelling from a fast fall in urea, usually in early sessions."),
              ("Closed-loop communication", "A named instruction, repeated back, and reported when done."),
              ("Nonshockable rhythm", "A cardiac arrest rhythm that a defibrillator will not shock."),
              ("Debrief", "A short team review after an event.")],
    "readings": [("code-blue-acls-dialysis-unit.html", "Cardiac arrest response in a dialysis unit."),
                 ("hemodialysis-complications.html", "The main complications of a session."),
                 ("dialysis-qapi-vs-cqi.html", "Using drills and events to improve.")],
    "calcs": ["calc-dialysis-head-nurse-toolkit.html#c10"],
}


# Spread the keyed answers across positions A to D.
import importlib.util as _u
from pathlib import Path as _P
_s = _u.spec_from_file_location("hn_quizutil", _P(__file__).resolve().parent / "quizutil.py")
_q = _u.module_from_spec(_s); _s.loader.exec_module(_q)
MODULE["quiz"] = _q.balance(MODULE["quiz"])
