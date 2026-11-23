# -*- coding: utf-8 -*-
"""Dialysis Clinical Head, Module 13: Serious Events, Families, and Outside Scrutiny. Written for this series from published sources."""

MODULE = {
    "image_alt": "A physician speaking with a worried family in a private room near a dialysis unit, a nurse beside her.",
    "objectives": [
        "Lead the first fifteen minutes of a serious event: protect patients, preserve evidence, and assign communication.",
        "Recognize a possible shared exposure and look actively for other affected patients.",
        "Speak with a family about what is known, what is not, and when they will hear next, through the facility&rsquo;s disclosure process.",
        "Route media, regulator, and insurer enquiries to an authorized spokesperson while protecting patient privacy.",
        "Support staff involved in an event, separately from the fact-finding.",
        "Separate confirmed facts, open questions, and decisions at every review.",
    ],
    "big": """
{{plain:When one patient becomes unwell, it is an emergency. When a second patient from the same shift becomes unwell, it is a question: what do they share?}}
{{fig:dch13_common}}
<p>The picture has a limit. Two patients on the same shift share many things by chance, and most second illnesses are coincidences. But the water loop, a dialyzer lot, a medication vial, or a machine can harm several patients at once, and the cost of looking is small compared with the cost of missing a cluster.</p>
{{cards:Key terms for this module|Serious event::An event that caused, or could have caused, death or serious harm.|Shared exposure::Something two or more affected patients had in common that could explain harm.|Disclosure::Honest communication with a patient or family about an event, its consequences, and what is being done.|Communication-and-resolution program::An approach that combines prompt disclosure, investigation, explanation, apology when warranted, and fair resolution.|Second victim::A health worker distressed after being involved in an adverse event.|Spokesperson::The person authorized to speak for the facility to the media and outside parties.}}
""",
    "case": {"title": "A second patient feels unwell", "html": """
<p>At 11:20 on a Friday, Mr. Andres Villareal, 66, collapses at station 6, an hour into treatment. The team resuscitates him and he is transferred to the hospital emergency department. At 11:45, Mrs. Remedios Tan at station 8 on the same shift reports chest tightness and nausea.</p>
<p>Mr. Villareal&rsquo;s daughter, Ms. Cora Villareal, arrives at 12:10 and asks you directly, &ldquo;Did the clinic do this to my father?&rdquo; At 12:30 the receptionist tells you a reporter from a local radio station is on the line asking whether a patient died during dialysis.</p>
""", "questions": ["What do you do in the first fifteen minutes after hearing about Mrs. Tan?",
                  "What can you tell Ms. Villareal now, and when will you speak again?",
                  "What do you tell the receptionist to say to the reporter?"]},
    "sections": [
        ("first", "The first fifteen minutes", "Care, preserve, communicate", """
{{fig:dch13_first15}}
{{flow:The first fifteen minutes|Minutes 0 to 5: protect::Assess Mrs. Tan now. Check every patient on the shift for symptoms. Activate the clinical response for anyone unwell.|Minutes 5 to 10: preserve::Ask the technical lead to secure water results and samples, and to tag out the machines and lines used at stations 6 and 8. Keep the dialyzers, lines, vials, and lot numbers. Do not discard or clean what may be evidence.|Minutes 10 to 15: assign::Name one person to lead communication with each family, one to monitor the remaining patients, and one to keep a timeline.}}
<p>Then ask the cluster question explicitly: what did Mr. Villareal and Mrs. Tan share? Station neighbors, the same water loop, the same dialyzer lot, the same heparin or iron vial, the same staff member, the same machine model. Check the rest of the shift and the previous shift for similar symptoms.</p>
{{call:Stop new connections on any loop, machine, or product lot that may be shared until the responsible technical lead and you have reviewed the evidence. Escalate to the owner, infection prevention, and the quality lead at once. Check reporting obligations and deadlines with compliance.}}
{{key:Preserve before you clean. The evidence that explains a cluster is usually thrown away in the first hour.}}
"""),
        ("family", "The family", "Talking with a family before you know", """
<p>Families want to know what happened, whether it could have been prevented, and what is being done. Early, honest communication is both right and, in the hospitals that have studied it, compatible with sound risk management. In four Massachusetts hospitals, communication-and-resolution programs were associated with improved trends in new claims and legal defense costs at some hospitals and no worsening in any.[[dch_kachalia2018]] In New York hospitals, disclosure conversations happened in 92% of cases handled through such a program; three quarters of the events did not involve substandard care.[[dch_mello2016]]</p>
{{fig:dch13_family}}
<div class="table-wrap"><table>
<thead><tr><th>Say</th><th>Avoid</th></tr></thead>
<tbody>
<tr><td>&ldquo;Your father collapsed during dialysis. The team restarted his heart, and he is in the emergency department now.&rdquo;</td><td>Medical jargon, or blaming anyone</td></tr>
<tr><td>&ldquo;We do not yet know why. We are checking everything about his treatment today, including the water and the equipment.&rdquo;</td><td>Guessing a cause, or denying one before you know</td></tr>
<tr><td>&ldquo;I am sorry this happened.&rdquo;</td><td>Silence because of fear of liability</td></tr>
<tr><td>&ldquo;I will call you at 6 this evening, and here is a number you can call anytime.&rdquo;</td><td>&ldquo;We will let you know.&rdquo;</td></tr>
</tbody></table></div>
<p>Use your facility&rsquo;s disclosure process, consider who the patient would want informed, and document what was shared. Repeat the conversation when new findings arrive.</p>
"""),
        ("outside", "Outside scrutiny", "Media, regulators, and insurers", """
<p>Route every outside enquiry to the authorized spokesperson. Staff should know one sentence: &ldquo;I cannot discuss any patient. Let me give you the number of the person who can speak for the clinic.&rdquo; Confirming that a named person was a patient, or describing what happened, would breach the patient&rsquo;s privacy.[[dch_ra10173]]</p>
<p>Record each request from a regulator, insurer, or media outlet, with its deadline and owner. Check, with the quality, privacy, and compliance leads, which notifications are required and by when, and record the decision and the time.</p>
<p>At the first review meeting, separate three lists: confirmed facts, open questions with owners, and decisions with times. Agree the criteria for any restriction and for restoring normal operation, and tell affected patients what changed.</p>
"""),
        ("staff", "Staff", "Supporting the people involved", """
<p>Health workers involved in an adverse event often suffer guilt, anxiety, sleeplessness, and doubt. A systematic review found that between 10% and 43% of clinicians involved in adverse events experienced this second-victim response, and that how they cope affects their later patients and colleagues.[[dch_seys2013]]</p>
<p>Offer support separately from the investigation, so that seeking help is not confused with being investigated. Check on the involved staff over the following days, not only on the day itself. A team that is supported is more likely to report the next problem early.</p>
"""),
    ],
    "debrief": ["""
<p><strong>The first fifteen minutes.</strong> Assess Mrs. Tan now and check every other patient on the shift. Secure the water results and samples, tag out the machines at stations 6 and 8, and keep the dialyzers, lines, vials, and lot numbers. Ask what the two patients shared. Hold new connections on any shared loop, machine, or lot. Escalate to the owner, infection prevention, and the quality lead, and assign one person to the timeline.</p>
<p><strong>What to tell Ms. Villareal.</strong> What happened, in plain words; that her father is being cared for in the emergency department; that you do not yet know why and are checking everything, including the water and equipment; that you are sorry it happened; and the time you will call her again, with a number she can call meanwhile. Then call at that time, even if there is little new.</p>
<p><strong>The reporter.</strong> The receptionist says the clinic cannot discuss any patient and gives the spokesperson&rsquo;s contact. Log the call. The spokesperson, with compliance, decides what, if anything, the clinic will say.</p>
"""],
    "skills": {"title": "Serious event command and family conversation",
               "intro": "Run the first fifteen minutes and a family conversation in simulation; repeat the family conversation after a new finding is injected.",
               "items": [
                   ("Assesses the second patient and screens the rest of the shift.", True),
                   ("Asks explicitly what affected patients share.", True),
                   ("Secures water results, machines, lines, dialyzers, vials, and lot numbers before cleaning.", True),
                   ("Holds new connections on any possibly shared loop, machine, or lot.", True),
                   ("Assigns family communication, patient monitoring, and the timeline to named people.", False),
                   ("Tells the family what is known and unknown, apologizes, and sets a time for the next call.", False),
                   ("Keeps identifiable information within authorized channels and routes media to the spokesperson.", True),
                   ("Offers staff support separately from the investigation.", False),
               ],
               "placement": "Write your unit&rsquo;s one-sentence script for outside enquiries and check that every receptionist and nurse knows it."},
    "quiz": [
        ("A second patient on the same shift becomes unwell. What question should you ask?",
         ["Who is to blame?", "What do the two patients share?", "Is it a coincidence?", "Who is on break?"], 1,
         "Look actively for a shared exposure."),
        ("What should you do with the dialyzers, lines, and vials used for the affected patients?",
         ["Discard them", "Keep them with lot numbers as possible evidence", "Clean them", "Return them to stock"], 1,
         "Preserve before you clean."),
        ("What should happen to new connections on a possibly shared water loop?",
         ["Continue", "Hold until the technical lead and clinical head review the evidence", "Speed up", "Move to the afternoon"], 1,
         "Act on plausible shared exposure."),
        ("A daughter asks whether the clinic caused her father&rsquo;s collapse. What is the best answer now?",
         ["No", "Yes", "We do not yet know; we are checking everything, and I will call you at a set time", "Ask the lawyer"], 2,
         "Honest about uncertainty, specific about follow-up."),
        ("What did communication-and-resolution programs show in Massachusetts hospitals?",
         ["Worse liability", "Improved trends in some liability measures and no worsening", "No disclosure", "Higher costs everywhere"], 1,
         "Transparency without adverse financial consequence."),
        ("In New York hospitals&rsquo; program, what share of events involved substandard care?",
         ["All", "About a quarter", "Three quarters", "None"], 1,
         "Three quarters did not."),
        ("A reporter calls about a patient. What should reception say?",
         ["Confirm the patient&rsquo;s name", "That the clinic cannot discuss any patient, and give the spokesperson&rsquo;s contact", "Describe the event", "Hang up"], 1,
         "Privacy and accuracy both protect the patient."),
        ("Who decides on external notifications?",
         ["The receptionist", "The leadership team with quality, privacy, and compliance, recording the decision and time", "The family", "The vendor"], 1,
         "Check obligations and deadlines."),
        ("What share of clinicians involved in adverse events experience a second-victim response?",
         ["Under 1%", "Between 10% and 43%", "All", "None"], 1,
         "Support them separately from the review."),
        ("Why keep staff support separate from fact-finding?",
         ["Efficiency", "So seeking help is not confused with being investigated", "Human resources rules", "It does not matter"], 1,
         "Supported staff report earlier."),
        ("What three lists should the first review separate?",
         ["Good, bad, unknown", "Confirmed facts, open questions with owners, decisions with times", "Staff, patients, owners", "Costs, savings, losses"], 1,
         "Keeps uncertainty visible."),
        ("You promised to call the family at 6 p.m. but have little new. What should you do?",
         ["Skip the call", "Call at 6 p.m. and say so", "Text a delay", "Wait until morning"], 1,
         "Keep the promise."),
        ("Which is evidence that a cluster may be environmental?",
         ["Two patients with different symptoms on different days", "Similar reactions in patients on the same loop and shift", "One patient with a known infection", "A staff complaint"], 1,
         "Shared timing and location suggest shared exposure."),
        ("Who should lead family communication?",
         ["Whoever is free", "One named person, through the disclosure process", "The receptionist", "The owner"], 1,
         "One voice, consistent messages."),
        ("Should you apologize before the cause is known?",
         ["Never", "Yes, that the event happened, without assigning blame", "Only in writing", "Only if a lawyer agrees"], 1,
         "Sorry that it happened is not an admission of fault."),
    ],
    "terms": [("Serious event", "An event that caused, or could have caused, death or serious harm."),
              ("Shared exposure", "Something affected patients had in common."),
              ("Disclosure", "Honest communication about an event and what is being done."),
              ("Communication-and-resolution program", "Disclosure, investigation, explanation, apology when warranted, and fair resolution."),
              ("Second victim", "A health worker distressed after an adverse event."),
              ("Spokesperson", "The person authorized to speak for the facility.")],
    "readings": [("hemodialysis-complications.html", "Complications during a session."),
                 ("code-blue-acls-dialysis-unit.html", "Cardiac arrest response in a dialysis unit.")],
    "calcs": ["calc-dialysis-clinical-head-toolkit.html"],
}


import importlib.util as _u
from pathlib import Path as _P
_s = _u.spec_from_file_location("dch_quizutil", _P(__file__).resolve().parent / "quizutil.py")
_q = _u.module_from_spec(_s); _s.loader.exec_module(_q)
MODULE["quiz"] = _q.balance(MODULE["quiz"])
