# -*- coding: utf-8 -*-
"""Vascular Surgeon, Module 1: The surgeon in the kidney care team. Written for this track from published sources (v2.0 blueprint)."""

MODULE = {
    "image_alt": "A surgeon on a hospital corridor phone call, writing a referral note, with a dialysis unit visible through the window.",
    "objectives": [
        "Distinguish the surgeon&rsquo;s clinical responsibility from the dialysis unit&rsquo;s governance and the attending nephrologist&rsquo;s prescription.",
        "Triage an access referral into emergency, urgent and elective work from a few targeted questions.",
        "Close a referral with a named owner, a next action, and a contingency the dialysis unit can use.",
        "Write a coverage arrangement that answers when you are in the operating room, on leave, or asleep.",
    ],
    "big": """
{{plain:Think of a relay race. The nephrologist runs the first leg, the surgeon runs the second, the dialysis nurse runs the third. Races are rarely lost on the straight. They are lost at the handoff, when one runner thinks the baton has been passed and the other has not yet closed a hand around it.}}
<p>The picture has a limit. In a relay, the runners know the order and the baton is visible. In access care the order changes with each problem, the baton is a decision, and nobody can see it unless it is written down and acknowledged. A referral that has been sent but not accepted is a baton lying on the track.</p>
{{cards:Key terms for this module|Access referral::A request for a surgical decision: creation, revision, rescue, or removal.|Decision owner::The named clinician who will act next, and by when.|Closed loop::A handoff the receiver has acknowledged and read back, with a fallback if the action does not happen.|Privileges::Permission from the hospital where you operate to perform named procedures. A course cannot grant it.|Coverage arrangement::The written answer to who responds when the usual surgeon cannot.}}
<p>Most referrals are elective and can wait for a clinic slot. A few hide a threatened hand, active bleeding, sepsis, or a patient who has not dialyzed. Your work is to find those few within minutes, and to make sure every other referral has an owner before you put the phone down.</p>
""",
    "case": {"title": "Friday, 4:40 p.m.", "html": """
<p>Your clinic secretary hands you a message from a hemodialysis center (HDC) in Valenzuela: &ldquo;Poor fistula. Please see.&rdquo; The patient is Mr. Rogelio Santiago, 61, with diabetes, on hemodialysis three times a week through a left radiocephalic fistula you did not create. There is no callback number, no mention of whether today&rsquo;s session was completed, and no name for the attending nephrologist.</p>
<p>You are about to leave for a weekend conference in Cebu. Your colleague, Dr. Teodoro Ilagan, covers your patients but has never heard of this one. The unit&rsquo;s charge nurse, Ms. Liza Dimaculangan, answers when you call the main line.</p>
""", "questions": [
        "What three or four questions do you ask Ms. Dimaculangan before deciding where this referral goes?",
        "Who owns which decision tonight: you, the attending nephrologist, the physician on duty, or the nurse?",
        "What must be true before you can call this referral &ldquo;handled&rdquo; and leave for Cebu?"]},
    "sections": [
        ("roles", "Who owns what", "Three authorities, one patient", """
<p>An access patient sits inside three separate systems. The dialysis facility is licensed by the Department of Health (DOH) under Administrative Order 2012-0001, which sets its personnel, records and referral arrangements.[[an01_2]] The attending nephrologist owns the patient&rsquo;s kidney plan and dialysis prescription; the Philippine Society of Nephrology (PSN) 2024 guidelines ask the attending to coordinate access provision and care with a vascular surgeon or a trained general surgeon (Section 1.2, b3).[[an01_1]] Your authority comes from a third place: the credentialing committee of the hospital where you operate.</p>
{{fig:vs01_a}}
<p>None of these documents makes the surgeon the unit&rsquo;s medical director or physician on duty (POD), and none of them makes the nephrologist responsible for operative decisions. The overlap is the access itself. That is where responsibility blurs, and where patients wait.</p>
<div class="table-wrap"><table>
<thead><tr><th>Decision</th><th>Usual owner</th><th>What you contribute</th></tr></thead>
<tbody>
<tr><td>Whether and when to dialyze, and the prescription</td><td>Attending nephrologist</td><td>Whether the access can be used today, and with what restrictions</td></tr>
<tr><td>Bedside response during a session</td><td>POD and dialysis nurse</td><td>Clear instructions for bleeding, a cold hand, or a failed cannulation</td></tr>
<tr><td>Cannulation technique and site</td><td>Dialysis nurse, within the unit&rsquo;s authorization</td><td>The usable segment, segments to avoid, and the first-use plan</td></tr>
<tr><td>Creation, revision, salvage, ligation</td><td>Surgeon, within privileges</td><td>The operative decision and its follow-up owner</td></tr>
<tr><td>Endovascular treatment</td><td>The credentialed operator (surgeon, interventional radiologist, or nephrologist)</td><td>Whether the treatment preserves the next site</td></tr>
</tbody></table></div>
{{scene:Monday clinic, fictional|<p>A fellow asks why you always end a referral call by repeating the plan aloud. You show him last year&rsquo;s incident log: a patient with a clotted graft waited two days because the unit believed the surgeon had booked the declot, and the surgeon believed the unit would send the patient to the emergency department.</p><p class="tc-scene-take"><b>What this shows.</b> Both sides acted reasonably on what they thought the other had heard. Only a read-back would have revealed the gap.</p>}}
{{key:A referral is not finished when it is sent or received. It is finished when someone has accepted it, owns the next action, and has a fallback if that action does not happen.}}
"""),
        ("triage", "Triage", "Triage in four questions", """
<p>Access emergencies follow physiology, not appointment books. A thrombosed access is a dialysis problem first: the danger is the potassium and the fluid the patient has not removed, not the clot. A cold, weak hand is a limb problem: nerves tolerate ischemia poorly, and a thrill says nothing about the hand beyond the anastomosis. Bleeding through thin skin is a hemorrhage problem. Fever with an access is a sepsis problem. Each needs a different destination, and each can arrive labeled &ldquo;poor fistula.&rdquo;</p>
{{fig:vs01_b}}
{{flow:Four questions for every access referral|Is there a threat now?::Active bleeding, a cold or weak hand, fever or low blood pressure, breathlessness.|Did the last session happen?::When was the last complete treatment, and what are the potassium and the weight gain?|What exactly changed?::Thrill gone, pressures up, cannulation failing, swelling, pain, a skin change.|Who is asking, and who owns the patient?::Name and number of the caller and the attending nephrologist.}}
<p>The answers sort the referral. A threat goes to the emergency pathway of a hospital that can treat it, today, with a named receiving clinician. A missed or failed session goes to the attending nephrologist for a dialysis decision in parallel with any access plan. A change without threat goes to a dated clinic or imaging slot, with instructions for what to do if it worsens.</p>
{{call:Stop and arrange same-day assessment through the emergency pathway for active or recurrent bleeding, a cold, painful or weak hand, fever or hypotension with an access, or a patient who cannot dialyze and is breathless or has a dangerous potassium. Do not hold these for the next clinic.}}
"""),
        ("coverage", "Coverage", "Coverage that works at 2 a.m.", """
<p>No surgeon is always available. The question is whether the system knows who answers instead. The UK Kidney Association (UKKA) 2025 guideline recommends that surgical expertise in access creation be established and maintained to achieve good outcomes (statement 3.6, grade 1C).[[vs_ukka]] Expertise that cannot be reached at night does not help the patient bleeding at night.</p>
<p>A workable coverage arrangement names a primary surgeon and a backup, the hospital each operates in, the hours each covers, and what happens when neither is reachable: usually the emergency department of a hospital with vascular capability, with a phone call ahead. It lists which procedures each surgeon is privileged to perform. It is shared with every unit that refers to you and reviewed when people change.</p>
<p>Write recommendations a unit can act on. &ldquo;Please monitor&rdquo; is not an instruction. &ldquo;Do not cannulate the upper segment; if the thrill is lost, call Dr. Ilagan at this number and send the patient to the emergency department at this hospital&rdquo; is.</p>
{{flow:Closing the loop on a referral|Receive::Name, number and question of the caller.|Triage::Threat now, last session, what changed.|Assign::A named owner and a time for the next action.|Read back::The receiver repeats the plan.|Fallback::What happens if the action does not occur, and who to call.|Record::Names, times and the plan in the chart.}}
{{key:Your personal phone number is not a coverage arrangement. A name, a backup, a hospital and a time window are.}}
"""),
    ],
    "debrief": [
        "<p><strong>The questions.</strong> Ask Ms. Dimaculangan whether there is a threat now (bleeding, a cold or weak hand, fever, low pressure, breathlessness), whether today&rsquo;s session was completed and what the last potassium was, what exactly changed in the fistula, and who the attending nephrologist is and how to reach him. Suppose she tells you the thrill was lost this morning, the session was abandoned after twenty minutes, and the last session was Tuesday. This is no longer a clinic referral.</p>",
        "<p><strong>Who owns what.</strong> The attending nephrologist owns whether Mr. Santiago needs dialysis tonight and how it will be delivered, which may mean a temporary catheter. The POD and nurse own his bedside safety until he leaves. You own the surgical question: whether the fistula can be salvaged, by whom, and when. Call the attending yourself; do not rely on the unit to relay it.</p>",
        "<p><strong>Before Cebu.</strong> The referral is handled when a named clinician has accepted Mr. Santiago with a time: for example, Dr. Ilagan agrees to assess him at the emergency department of his hospital tonight, the attending nephrologist agrees to arrange dialysis access if salvage is not possible, and Ms. Dimaculangan reads the plan back. You document the call, the names, the times, and the fallback: if Dr. Ilagan cannot be reached within an hour, the patient goes to the emergency department named in your coverage arrangement.</p>",
    ],
    "skills": {"title": "Taking and closing an access referral",
               "intro": "Rehearse with a preceptor using a fictional referral, or observe at your own service. Sign-off is local.",
               "items": [("Asks for current threats before discussing scheduling", True),
                         ("Establishes when the last complete dialysis session occurred", True),
                         ("Identifies the attending nephrologist and the caller by name and number", False),
                         ("States which decision belongs to which professional", False),
                         ("Confirms a named receiving clinician and a time, with a read-back", True),
                         ("Documents the escalation route and the fallback if the action does not happen", False)],
               "placement": "Simulation or supervised referral calls"},
    "quiz": [
        ("A surgeon receives an access referral with no urgency information. What should happen first?",
         ["Book the next routine clinic slot", "Clarify current threats, the last completed session and the decision being requested",
          "Send a generic acknowledgment and wait for more details", "Ask the unit to order an ultrasound before any call"],
         1, "Triage information decides whether routine scheduling is safe. An acknowledgment alone resolves nothing clinically."),
        ("Who authorizes a surgeon to perform independent access surgery after completing this track?",
         ["The quiz engine on this site", "The course author", "The relevant hospital credentialing and privileging process",
          "The dialysis unit&rsquo;s clinical head"],
         2, "Learning completion cannot grant operative authority. Privileges come from the hospital where the surgeon operates."),
        ("Under the Philippine Society of Nephrology (PSN) 2024 hemodialysis guidelines, what does Section 1.2 b3 assign to the attending nephrologist?",
         ["Performing access surgery when no surgeon is available", "Coordinating access provision and care with a vascular surgeon or trained general surgeon",
          "Credentialing access surgeons for the dialysis unit", "Signing the operative consent"],
         1, "The clause makes access a coordinated responsibility. It does not credential a surgeon or transfer operative decisions."),
        ("A patient&rsquo;s fistula clotted this morning and the session was abandoned. Who decides whether he needs dialysis tonight?",
         ["The surgeon, because the access is the problem", "The dialysis nurse", "The attending nephrologist, in parallel with the surgical plan",
          "Nobody until the fistula is salvaged"],
         2, "Thrombosis is a dialysis-safety problem first. The nephrologist owns the dialysis decision while the surgeon owns salvage."),
        ("Which statement is an actionable surgical recommendation to a dialysis unit?",
         ["Please monitor the fistula", "Fistula reviewed, follow up as needed",
          "Do not cannulate the upper segment; if the thrill is lost, call the named backup and send the patient to the named emergency department",
          "Patient to be seen again sometime"],
         2, "An actionable recommendation names what is restricted, what to watch for, and who to call and where to go."),
    ],
    "terms": [("Closed loop", "A handoff that the receiver acknowledges and reads back, with a fallback if the action does not happen."),
              ("Privileges", "Hospital permission to perform specific procedures, granted by its credentialing committee.")],
    "readings": [("hemodialysis-access-lifeline.html", "Why the access is the patient&rsquo;s lifeline, and how teams protect it."),
                 ("dialysis-access-care.html", "What patients and nurses are taught about access care.")],
    "calcs": ["calc-catheter-exposure.html", "calc-access-intervention-burden.html"],
}

import importlib.util as _u
from pathlib import Path as _P
_s = _u.spec_from_file_location("vs_quizutil", _P(__file__).resolve().parent / "quizutil.py")
_q = _u.module_from_spec(_s); _s.loader.exec_module(_q)
MODULE["quiz"] = _q.balance(MODULE["quiz"])
